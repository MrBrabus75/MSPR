import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from joblib import dump, load

# Load the dataset
data_path = 'dataset/dataset_finale_region.xlsx'  # Adjusted to the file upload path
data = pd.read_excel(data_path)

# Filter for the Nouvelle-Aquitaine region
data_nouvelle_aquitaine = data[data['region'].str.upper() == 'HAUTS-DE-FRANCE']

# Predicting future features with ARIMA for Nouvelle-Aquitaine region
features_to_predict = ['taux_de_chômage', 'pib', '18-24_ans', '25-34_ans', '35-49_ans', '50-64_ans', '65_ans_et_plus']
predicted_features = {}

for feature in features_to_predict:
    series = data_nouvelle_aquitaine[feature].dropna()
    if not series.empty:
        model = ARIMA(series, order=(5,1,0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=4)
        predicted_features[feature] = forecast

# Convert predictions into DataFrame
predicted_features_df = pd.DataFrame(predicted_features)
predicted_features_df['année'] = range(2023, 2027)
predicted_features_df['region'] = 'NOUVELLE-AQUITAINE'

# Use last known values for other missing features
last_known_values = data_nouvelle_aquitaine.dropna().iloc[-1]
for feature in data.columns:
    if feature not in predicted_features_df.columns:
        predicted_features_df[feature] = last_known_values[feature]

# Concatenate with historical data for Nouvelle-Aquitaine
data_nouvelle_aquitaine_full = pd.concat([data_nouvelle_aquitaine, predicted_features_df], ignore_index=True)
data_nouvelle_aquitaine_full = data_nouvelle_aquitaine_full.dropna(subset=['tendance_politique'])
data_nouvelle_aquitaine_full['tendance_politique'] = data_nouvelle_aquitaine_full['tendance_politique'].astype(str)


# Feature selection and data preparation
features = ['année', 'inscrits', 'abstentions', 'votants', 'exprimés', 'voix', '%_voix/ins', '%_voix/exp', 'taux_de_chômage', 'pib'] + features_to_predict
X = data_nouvelle_aquitaine_full[features]
y = data_nouvelle_aquitaine_full['tendance_politique']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Model configurations
model_configs = {
    'rf': {
        'pipeline': Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler()),
            ('pca', PCA()),
            ('classifier', RandomForestClassifier(random_state=42))
        ]),
        'params': {
            'imputer__strategy': ['mean', 'median', 'most_frequent'],
            'pca__n_components': [5, 10],
            'classifier__n_estimators': [100, 200],
        }
    },
    'gb': {
        'pipeline': Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler()),
            ('pca', PCA()),
            ('classifier', GradientBoostingClassifier(random_state=42))
        ]),
        'params': {
            'imputer__strategy': ['mean', 'median', 'most_frequent'],
            'pca__n_components': [5, 10],
            'classifier__n_estimators': [100, 200],
        }
    },
    'svc': {

        'pipeline': Pipeline([

            ('imputer', SimpleImputer(strategy='median')),

            ('scaler', StandardScaler()),

            ('pca', PCA()),

            ('classifier', SVC(random_state=42))

        ]),

        'params': {

            'imputer__strategy': ['mean', 'median', 'most_frequent'],

            'pca__n_components': [5, 10],

            'classifier__C': [0.1, 1, 10],

            'classifier__kernel': ['linear', 'rbf']

        }

    }

}



best_score = float('-inf')  # Initialize best_score before the loop
best_model = None  # Initialize best_model before the loop

for model_name, config in model_configs.items():
    grid_search = GridSearchCV(config['pipeline'], config['params'], cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    current_score = grid_search.best_score_
    if current_score > best_score:
        best_score = current_score
        best_model = grid_search.best_estimator_

    print(f"Meilleurs paramètres pour {model_name}: {grid_search.best_params_}")
    print(f"Meilleure précision pour {model_name}: {current_score}")

print(f"Meilleur modèle global: {best_model} avec une précision de: {best_score}")



# Predicting political trends for Nouvelle-Aquitaine using the best model

predicted_trends = best_model.predict(predicted_features_df[features])

dump(best_model, 'modeles/meilleur_modele.joblib')


# Prepare and output the predictions

predicted_trends_output = {year: trend for year, trend in zip(range(2023, 2027), predicted_trends)}

predicted_trends_output

# Après avoir obtenu les prédictions avec best_model.predict
predicted_trends = best_model.predict(predicted_features_df[features])

# Préparer et afficher les prédictions correctement
predicted_trends_output = {year: trend for year, trend in zip(range(2023, 2027), predicted_trends)}

print("Prédictions de la tendance politique pour la région Nouvelle-Aquitaine pour les années futures:")
for year, trend in predicted_trends_output.items():
    print(f"Tendance politique pour la Nouvelle-Aquitaine en {year}: {trend}")
