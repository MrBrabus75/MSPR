import pandas as pd
import re
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
    logger.info("Chargement du dataset.")
    # Chargement du dataset
    df = pd.read_excel("dataset/Presidentielle_resultats_fusionnes.xlsx")
    logger.info("Dataset chargé avec succès.")

    # Définition de la correspondance pour les tendances politiques
    tendance_politique_mapping = {
        'Lutte ouvrière': 'Extrême Gauche',
        'Nouveau Parti Anticapitaliste': 'Extrême Gauche',
        'Parti communiste français': 'Gauche',
        'Parti Socialiste': 'Gauche',
        'Union Populaire Républicaine' : 'Centre',
        'La France insoumise': 'Gauche',
        'Europe Écologie Les Verts': 'Gauche',
        'Mouvement Démocrate': 'Centre',
        'La République en marche': 'Centre',
        'Les Républicains': 'Droite',
        'Debout la France': 'Droite',
        'Rassemblement national': 'Extrême Droite',
        'Reconquête': 'Extrême Droite',
        'Ouvrier Indépendant': 'Extrême Gauche',
        'Solidarité et Progrès': 'Extrême Droite',
        'Résistons': 'Centre'
    }

    logger.info("Suppression de la ligne à l'index 2998.")
    # Suppression de la ligne à l'index 2998
    df.drop(index=2998, inplace=True)

    logger.info("Ajout de la colonne 'Tendance Politique' basée sur le parti.")
    # Ajout de la colonne "Tendance Politique" basée sur le "Parti"
    df['Tendance Politique'] = df['Parti'].map(tendance_politique_mapping)

    # Fonction de normalisation du texte
    def normalize_text_v3(text):
        if pd.isnull(text):
            return text
        accents_translation = str.maketrans(
            'ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖÙÚÛÜÝŸàáâãäåçèéêëìíîïðñòóôõöùúûüýÿ',
            'AAAAAACEEEEIIIIONOOOOOUUUUYYaaaaaaceeeeiiiionooooouuuuyy')
        normalized = text.translate(accents_translation)
        normalized = normalized.upper()
        normalized = re.sub(r"[-' ]", "", normalized)
        return normalized

    logger.info("Application de la normalisation sur 'Libellé du département'.")
    # Application de la normalisation sur "Libellé du département"
    df['Libellé du département'] = df['Libellé du département'].apply(normalize_text_v3)

    logger.info("Réorganisation des colonnes pour placer 'Tendance Politique' à côté de 'Parti'.")
    # Réorganisation des colonnes pour placer "Tendance Politique" à côté de "Parti"
    columns_order = ['Libellé du département', 'Année', 'Tour', 'Parti', 'Tendance Politique', 'Inscrits', 'Abstentions', 'Votants', 'Exprimés', 'Voix', '% Voix/Ins', '% Voix/Exp']
    df = df[columns_order]

    logger.info("Sauvegarde du fichier modifié.")
    # Sauvegarde du fichier modifié
    df.to_excel("dataset/dataset.xlsx", index=False)
    logger.info("Fichier sauvegardé avec succès.")
except Exception as e:
    logger.error(f"Erreur lors du traitement des données : {e}")
