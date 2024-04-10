import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as IMBPipeline
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from joblib import dump, load

# Chargement du jeu de données
data = pd.read_excel('dataset/dataset_finale_region.xlsx')
print("Données chargées avec succès.")

# Filtrage pour la région Nouvelle-Aquitaine
data_na = data[data['region'].str.upper() == 'NOUVELLE-AQUITAINE']
print(f"Nombre d'entrées pour la Nouvelle-Aquitaine: {data_na.shape[0]}")

# Sélection uniquement des colonnes numériques pour la matrice de corrélation
numeric_cols = data_na.select_dtypes(include=[np.number]).columns
correlation_matrix = data_na[numeric_cols].corr()
print("Matrice de corrélation:\n", correlation_matrix)

# Prédiction des caractéristiques futures avec ARIMA
features_to_predict = ['taux_de_chômage', 'pib', '18-24_ans', '25-34_ans', '35-49_ans', '50-64_ans', '65_ans_et_plus']
predicted_features = {}

for feature in features_to_predict:
    series = data_na[feature].dropna()
    if not series.empty:
        model = ARIMA(series, order=(5,1,0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=4)
        predicted_features[feature] = forecast.tolist()
        print(f"Prévisions ARIMA pour {feature} réalisées.")

predicted_features_df = pd.DataFrame(predicted_features)
predicted_features_df['année'] = range(2023, 2027)
predicted_features_df['region'] = 'NOUVELLE-AQUITAINE'

# Concaténation avec les données historiques
data_na_full = pd.concat([data_na, predicted_features_df], ignore_index=True)
last_known_values = data_na.iloc[-1]
for feature in data.columns:
    if feature not in predicted_features_df.columns and feature not in ['année', 'region']:
        predicted_features_df[feature] = last_known_values[feature]

data_na_full = data_na_full.dropna(subset=['tendance_politique'])
data_na_full['tendance_politique'] = data_na_full['tendance_politique'].astype(str)

# Sélection des caractéristiques et préparation des données
features = ['année', 'inscrits', 'abstentions', 'votants', 'exprimés', 'voix', '%_voix/ins', '%_voix/exp'] + features_to_predict
X = data_na_full[features]
y = data_na_full['tendance_politique']

# Rééquilibrage des classes dans l'ensemble d'entraînement
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# Configuration des modèles avec un pipeline intégrant SMOTE
model_configs = {
    'rf': {
        'model': IMBPipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler()),
            ('smote', SMOTE(random_state=42)),
            ('pca', PCA(n_components=10)),
            ('classifier', RandomForestClassifier(random_state=42))
        ]),
        'params': {
            'classifier__n_estimators': [100, 200],
            'classifier__max_depth': [10, 20, None],
            'classifier__min_samples_split': [2, 5]
        }
    },
    'gb': {
        'model': IMBPipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler()),
            ('smote', SMOTE(random_state=42)),
            ('pca', PCA(n_components=10)),
            ('classifier', GradientBoostingClassifier(random_state=42))
        ]),
        'params': {
            'classifier__n_estimators': [100, 200],
            'classifier__learning_rate': [0.01, 0.1],
            'classifier__max_depth': [3, 5]
        }
    },
    'svc': {
        'model': IMBPipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler()),
            ('smote', SMOTE(random_state=42)),
            ('pca', PCA(n_components=10)),
            ('classifier', SVC(random_state=42))
        ]),
        'params': {
            'classifier__C': [0.1, 1, 10],
            'classifier__kernel': ['linear', 'rbf']
        }
    }
}

best_model = None
best_score = -np.inf

# Entraînement et sélection du meilleur modèle
for name, config in model_configs.items():
    grid = GridSearchCV(config['model'], config['params'], cv=StratifiedKFold(5), n_jobs=-1, verbose=3)
    grid.fit(X_train_smote, y_train_smote)
    print(f"Meilleurs paramètres pour {name}: {grid.best_params_}")
    print(f"Meilleure précision en validation croisée pour {name}: {grid.best_score_:.2f}")

    if grid.best_score_ > best_score:
        best_score = grid.best_score_
        best_model = grid.best_estimator_

# Évaluation du meilleur modèle
y_pred = best_model.predict(X_test)
print("Précision sur l'ensemble de test:", accuracy_score(y_test, y_pred))
print("Matrice de confusion :\n", confusion_matrix(y_test, y_pred))
print("Rapport de classification :\n", classification_report(y_test, y_pred))

# Sauvegarde du meilleur modèle
dump(best_model, 'meilleur_modele.joblib')
print("Meilleur modèle sauvegardé.")

# Prédiction des tendances politiques pour les années futures
predicted_trends = best_model.predict(predicted_features_df[features])
predicted_trends_output = {year: trend for year, trend in zip(range(2023, 2027), predicted_trends)}
print("Tendances politiques prévues pour la Nouvelle-Aquitaine pour les années à venir :")
for year, trend in predicted_trends_output.items():
    print(f"Tendance politique pour {year} : {trend}")
