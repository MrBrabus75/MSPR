import pandas as pd
import os
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
    logger.info("Chargement du dataset.")
    file_path = 'dataset/dataset_finale_non_normalisé.xlsx'
    df = pd.read_excel(file_path)
    
    # La conversion des colonnes % Voix/Ins et % Voix/Exp est omise car déjà numériques

    logger.info("Normalisation des noms de colonnes.")
    df.columns = df.columns.str.replace(' ', '_').str.lower()

    logger.info("Conversion des données catégorielles.")
    categorical_columns = ['tour', 'parti', 'tendance_politique']
    df[categorical_columns] = df[categorical_columns].apply(lambda x: x.astype('category'))

    logger.info("Gestion des valeurs manquantes.")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
    df[categorical_columns] = df[categorical_columns].apply(lambda x: x.fillna(x.mode()[0]))

    logger.info("Suppression des lignes dupliquées.")
    df = df.drop_duplicates()

    logger.info("Standardisation des noms de départements.")
    df['libellé_du_département'] = df['libellé_du_département'].str.upper().str.strip()

    logger.info("Sauvegarde du dataset normalisé.")
    df.to_excel("dataset/dataset_finale_normalisé.xlsx", index=False)

    logger.info("Suppression du fichier original non normalisé.")
    os.remove(file_path)
    os.remove("dataset/Presidentielle_resultats_fusionnes.xlsx")

    logger.info("Processus de normalisation et ajustement terminé avec succès.")

except Exception as e:
    logger.error(f"Erreur lors du processus de normalisation et ajustement : {e}")
