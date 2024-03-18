import pandas as pd
import os
import logging

# Configuration du logging pour écrire dans un fichier en UTF-8 et afficher dans le terminal
logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('data_processing.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

try:
    # Chemins des fichiers source
    chemin_dataset_principal = 'dataset/dataset_fusionne.xlsx'
    chemin_dataset_secondaire = 'dataset/resultats_elections-par-age.xlsx'

    logger.info("Chargement des datasets.")
    # Charger les datasets
    dataset_principal = pd.read_excel(chemin_dataset_principal)
    dataset_secondaire = pd.read_excel(chemin_dataset_secondaire)
    logger.info("Datasets chargés avec succès.")

    logger.info("Fusion des datasets sur les colonnes 'Parti' et 'Année'.")
    # Fusionner les datasets sur les colonnes "Parti" et "Année"
    dataset_fusionne = pd.merge(dataset_principal, dataset_secondaire, on=['Parti', 'Année'], how='left')
    logger.info("Fusion des datasets terminée.")

    # Enregistrer le dataset final
    chemin_dataset_final = 'dataset/dataset_finale_non_normalisé.xlsx'
    logger.info("Sauvegarde du dataset fusionné en cours.")
    dataset_fusionne.to_excel(chemin_dataset_final, index=False)
    logger.info("Dataset fusionné sauvegardé avec succès.")

    # Suppression des fichiers spécifiés
    fichiers_a_supprimer = ['dataset/dataset.xlsx', 'dataset/dataset_fusionne.xlsx']
    for fichier in fichiers_a_supprimer:
        if os.path.exists(fichier):
            os.remove(fichier)
            logger.info(f"Le fichier {fichier} a été supprimé.")
        else:
            logger.warning(f"Le fichier {fichier} n'existe pas et ne peut être supprimé.")

except Exception as e:
    logger.error(f"Erreur lors du traitement des datasets : {e}")
