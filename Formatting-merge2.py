import pandas as pd
import logging

# Configuration du logging pour écrire dans un fichier en UTF-8 et afficher dans le terminal
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Handler pour écrire dans le fichier avec encodage UTF-8
file_handler = logging.FileHandler('data_processing.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Handler pour afficher dans le terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Ajout des deux handlers au logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

try:
    # Chargement des datasets
    logger.info("Chargement des datasets.")
    dataset_principal = pd.read_excel('dataset/dataset.xlsx')
    chomage = pd.read_excel('dataset/Chomage_annuel_par_departement_normalized_adjusted.xlsx')
    delinquance = pd.read_excel('dataset/Deli-dep-anne_normalized_adjusted.xlsx')
    pib = pd.read_excel('dataset/PIB-dep-annee_normalized_adjusted.xlsx')
    population = pd.read_excel('dataset/population_par_departement_et_tranche_d_age_normalized_adjusted.xlsx')
    logger.info("Datasets chargés avec succès.")

    # Normalisation des datasets secondaires (pivot si nécessaire)
    logger.info("Début de la normalisation des datasets secondaires.")
    chomage_melted = chomage.melt(id_vars=['Libellé du département'], var_name='Année', value_name='Taux de chômage')
    delinquance_melted = delinquance.melt(id_vars=['Libellé du département'], var_name='Année', value_name='Incidents de délinquance')
    pib_melted = pib.melt(id_vars=['Libellé du département'], var_name='Année', value_name='PIB')
    logger.info("Normalisation des datasets secondaires terminée.")

    # Correction des types de données
    logger.info("Correction des types de données en cours.")
    delinquance_melted['Incidents de délinquance'] = delinquance_melted['Incidents de délinquance'].str.replace(" ", "").astype(int)
    chomage_melted['Année'] = chomage_melted['Année'].astype(int)
    delinquance_melted['Année'] = delinquance_melted['Année'].astype(int)
    pib_melted['Année'] = pib_melted['Année'].astype(int)
    population['Année'] = population['Année'].astype(int)
    logger.info("Types de données corrigés.")

    # Fusion des datasets
    logger.info("Début de la fusion des datasets.")
    df_merged = pd.merge(dataset_principal, chomage_melted, how='left', on=['Libellé du département', 'Année'])
    df_merged = pd.merge(df_merged, delinquance_melted, how='left', on=['Libellé du département', 'Année'])
    df_merged = pd.merge(df_merged, pib_melted, how='left', on=['Libellé du département', 'Année'])
    df_merged = pd.merge(df_merged, population, how='left', on=['Libellé du département', 'Année'])
    logger.info("Fusion des datasets terminée.")

    # Suppression des lignes spécifiées
    logger.info("Suppression des départements spécifiés en cours.")
    departements_a_supprimer = [
        "GUADELOUPE", "MARTINIQUE", "GUYANE", "LAREUNION", "MAYOTTE", "NOUVELLECALEDONIE",
        "POLYNESIEFRANCAISE", "SAINTPIERREETMIQUELON", "WALLISETFUTUNA", "SAINTMARTIN/SAINTBARTHELEMY",
        "FRANCAISDELETRANGER", "FRANCAISETABLISHORSDEFRANCE", "CORSESUD", "CORSEDUSUD", "HAUTECORSE"
    ]
    df_merged = df_merged[~df_merged['Libellé du département'].isin(departements_a_supprimer)]
    logger.info("Suppression des départements spécifiés terminée.")

    # Sauvegarde du dataset fusionné après suppression
    logger.info("Sauvegarde du dataset fusionné en cours.")
    df_merged.to_excel('dataset/dataset_fusionne.xlsx', index=False)
    logger.info("Dataset fusionné sauvegardé avec succès.")

except Exception as e:
    logger.error(f"Erreur lors du traitement des datasets : {e}")
