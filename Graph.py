import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Charger le fichier Excel
fichier_excel = "dataset_finale_normalisé.xlsx"
donnees = pd.read_excel(fichier_excel)

donnees.head()

# Filtrer les données pour la France entière et le département de la Charente pour les années concernées
france_entiere = donnees[donnees['année'].isin([2007, 2012, 2017, 2022])]
charente = donnees[(donnees['libellé_du_département'].str.upper() == 'CHARENTE') & donnees['année'].isin([2007, 2012, 2017, 2022])]

# Préparer les couleurs selon la tendance politique
couleurs = {
    'Extrême gauche': 'darkred',
    'Gauche': 'lightcoral',
    'Centre': 'orange',
    'Droite': 'lightblue',
    'Extrême droite': 'darkblue'
}

# Fonction pour générer les graphiques
def generer_graphiques(data, titre):
    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(20, 10), sharey=True)
    fig.suptitle(titre, fontsize=16)

    for index, annee in enumerate([2007, 2012, 2017, 2022]):
        for tour in [1, 2]:
            ax = axes[tour-1, index]
            subset = data[(data['année'] == annee) & (data['tour'] == tour)]
            sns.barplot(x='tendance_politique', y='voix', data=subset, ax=ax, palette=couleurs, ci=None)
            ax.set_title(f"{annee} - Tour {tour}")
            ax.set_xlabel('')
            ax.set_ylabel('Voix' if index == 0 else '')
            ax.tick_params(axis='x', rotation=45)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Générer les graphiques pour la France entière
generer_graphiques(france_entiere, "Résultats des élections par tendance politique - France entière")

# Générer les graphiques pour le département de la Charente
generer_graphiques(charente, "Résultats des élections par tendance politique - Département de la Charente")
