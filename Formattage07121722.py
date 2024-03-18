import pandas as pd
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

# Dictionnaire pour remplacer les noms des candidats par leur parti
candidate_to_party = {
    'BAYROU François': 'Mouvement Démocrate',
    'BESANCENOT Olivier': 'Nouveau Parti Anticapitaliste',
    'BUFFET Marie-George': 'Parti communiste français',
    'LAGUILLER Arlette': 'Lutte ouvrière',
    'LE PEN Jean-Marie': 'Rassemblement national',
    'ROYAL Ségolène': 'Parti Socialiste',
    'SARKOZY Nicolas': 'Les Républicains',
    'VOYNET Dominique': 'Europe Écologie Les Verts',
    'SCHIVARDI Gérard': 'Ouvrier Indépendant',
    'BOVÉ José': 'Europe Écologie Les Verts',
    'de VILLIERS Philippe': 'Reconquête',
    'NIHOUS Frédéric': 'Les Républicains',
    'ARTHAUD Nathalie': 'Lutte ouvrière',
    'HAMON Benoît' : 'Parti Socialiste',
    'ASSELINEAU François' : 'Union Populaire Républicaine',   
    'LE PEN Marine': 'Rassemblement national',
    'MÉLENCHON Jean-Luc': 'La France insoumise',
    'POUTOU Philippe': 'Nouveau Parti Anticapitaliste',
    'CHEMINADE Jacques': 'Solidarité et Progrès',
    'HOLLANDE François': 'Parti Socialiste',
    'JOLY Eva': 'Europe Écologie Les Verts',
    'DUPONT-AIGNAN Nicolas': 'Debout la France',
    'ROUSSEL Fabien': 'Parti communiste français',
    'MACRON Emmanuel': 'La République en marche',
    'LASSALLE Jean': 'Résistons',
    'ZEMMOUR Éric': 'Reconquête',
    'HIDALGO Anne': 'Parti Socialiste',
    'JADOT Yannick': 'Europe Écologie Les Verts',
    'PÉCRESSE Valérie': 'Les Républicains',
    'FILLON François': 'Les Républicains'
}
logger.info("Correction de la fonction pour traiter chaque fichier avec détection dynamique des colonnes de candidats.")
# Correction de la fonction pour traiter chaque fichier avec détection dynamique des colonnes de candidats
def process_file_corrected(file_path, annee, tour):
    df = pd.read_excel(file_path)
    df_final = pd.DataFrame()

    # Détection du nombre de candidats par fichier
    candidat_columns = [col for col in df.columns if 'Nom' in col or 'Voix' in col]
    num_candidates = len(candidat_columns) // 4  # 4 colonnes par candidat: Nom, Prénom, Voix, % Voix/Exp

    for i in range(num_candidates):
        nom_col = f'Nom.{i}' if i else 'Nom'
        prenom_col = f'Prénom.{i}' if i else 'Prénom'
        voix_col = f'Voix.{i}' if i else 'Voix'
        
        # Vérification si les colonnes nécessaires existent
        if nom_col in df.columns and prenom_col in df.columns and voix_col in df.columns:
            # DataFrame temporaire pour chaque candidat
            df_candidat = df[['Libellé du département', 'Inscrits', 'Abstentions', 'Votants', nom_col, prenom_col, voix_col]].copy()
            df_candidat['Année'] = annee
            df_candidat['Tour'] = tour
            
            # Remplacer les noms des candidats par leur parti
            df_candidat['Parti'] = df_candidat[nom_col] + ' ' + df_candidat[prenom_col]
            df_candidat['Parti'] = df_candidat['Parti'].map(candidate_to_party)
            
            # Calculer les colonnes nécessaires
            df_candidat['Exprimés'] = df_candidat['Votants']  # Ajustement nécessaire selon la structure des données
            df_candidat['Voix'] = df_candidat[voix_col]
            df_candidat['% Voix/Ins'] = df_candidat['Voix'] / df_candidat['Inscrits'] * 100
            df_candidat['% Voix/Exp'] = df_candidat['Voix'] / df_candidat['Exprimés'] * 100  # Ajustement nécessaire
            
            # Sélection des colonnes finales
            df_candidat = df_candidat[['Libellé du département', 'Année', 'Tour', 'Parti', 'Inscrits', 'Abstentions', 'Votants', 'Exprimés', 'Voix', '% Voix/Ins', '% Voix/Exp']]
            
            # Ajout au DataFrame final
            df_final = pd.concat([df_final, df_candidat], ignore_index=True)

    return df_final
logger.info("Chemins des fichiers à traiter et années/tours correspondants.")
# Chemins des fichiers à traiter et années/tours correspondants
files_paths = [
    'dataset/Presidentielle_2022_Resultats_Tour_2_c.xlsx',
    'dataset/Presidentielle_2022_Resultats_Tour_1_c.xlsx',
    'dataset/Presidentielle_2017_Resultats_Tour_2_c.xlsx',
    'dataset/Presidentielle_2017_Resultats_Tour_1_c.xlsx',
    'dataset/Presidentielle_2012_Resultats_Tour_2.xlsx',
    'dataset/Presidentielle_2012_Resultats_Tour_1.xlsx',
    'dataset/Presidentielle_2007_Resultats_Tour_2.xlsx',
    'dataset/Presidentielle_2007_Resultats_Tour_1.xlsx'
]
years_tours = [
    (2022, 2),
    (2022, 1),
    (2017, 2),
    (2017, 1),
    (2012, 2),
    (2012, 1),
    (2007, 2),
    (2007, 1)
]
logger.info("Fusionner tous les fichiers.")
# Fusionner tous les fichiers
df_merged_corrected = pd.DataFrame()
for file_path, (year, tour) in zip(files_paths, years_tours):
    df_temp = process_file_corrected(file_path, year, tour)
    df_merged_corrected = pd.concat([df_merged_corrected, df_temp], ignore_index=True)
    
logger.info("Exporter le DataFrame fusionné vers un nouveau fichier Excel.")
# Exporter le DataFrame fusionné vers un nouveau fichier Excel
output_file_path = 'dataset/Presidentielle_resultats_fusionnes.xlsx'
df_merged_corrected.to_excel(output_file_path, index=False)

print(f"Le fichier fusionné a été exporté à : {output_file_path}")
