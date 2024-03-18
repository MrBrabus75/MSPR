import pandas as pd

# Chemin vers le fichier Excel d'origine
file_path = 'dataset/dataset_finale_normalisé.xlsx'

# Charger le fichier Excel pour inspection
df = pd.read_excel(file_path)

# Création d'un dictionnaire pour la correspondance département-région
regions_departements = {
    "Auvergne-Rhône-Alpes": ["AIN", "ALLIER", "ARDECHE", "CANTAL", "PUYDEDOME", "DROME", "ISERE", "LOIRE", "HAUTELOIRE", "PUISEDOME", "RHONE", "SAVOIE", "HAUTESAVOIE"],
    "Bourgogne-Franche-Comté": ["COTEDOR", "HAUTESAONE", "DOUBS", "JURA", "NIEVRE", "HAUTEDESAONE", "SAONEETLOIRE", "YONNE", "TERRITOIREDEBELFORT"],
    "Bretagne": ["COTESDARMOR", "FINISTERE", "ILLEETVILAINE", "MORBIHAN"],
    "Centre-Val de Loire": ["CHER", "EUREETLOIR", "INDRE", "INDREETLOIRE", "LOIRETCHER", "LOIRET"],
    "Corse": ["CORSEDUSUD", "HAUTECORSE"],
    "Grand Est": ["ARDENNES", "AUBE", "MARNE", "HAUTEMARNE", "MEURTHEETMOSELLE", "MEUSE", "MOSELLE", "BASRHIN", "HAUTRHIN", "VOSGES"],
    "Hauts-de-France": ["AISNE", "NORD", "OISE", "PASDECALAIS", "SOMME"],
    "Île-de-France": ["PARIS", "SEINEETMARNE", "YVELINES", "ESSONNE", "HAUTSDESEINE", "SEINESAINTDENIS", "VALDEMARNE", "VALDOISE"],
    "Normandie": ["CALVADOS", "EURE", "MANCHE", "ORNE", "SEINEMARITIME"],
    "Nouvelle-Aquitaine": ["CHARENTE", "CHARENTEMARITIME", "CORREZE", "CREUSE", "DORDOGNE", "GIRONDE", "LANDES", "LOTETGARONNE", "PYRENEESATLANTIQUES", "DEUXSEVRES", "VIENNE", "HAUTEVIENNE"],
    "Occitanie": ["ARIEGE", "AUDE", "AVEYRON", "GARD", "HAUTEGARONNE", "GERS", "HERAULT", "LOT", "LOZERE", "HAUTESPYRENEES", "PYRENEESORIENTALES", "TARN", "TARNETGARONNE"],
    "Pays de la Loire": ["LOIREATLANTIQUE", "MAINEETLOIRE", "MAYENNE", "SARTHE", "VENDEE"],
    "Provence-Alpes-Côte d'Azur": ["ALPESDEHAUTEPROVENCE", "HAUTESALPES", "ALPESMARITIMES", "BOUCHESDURHONE", "VAR", "VAUCLUSE"]
}

# Inverser le dictionnaire pour faciliter la recherche par département
departement_region = {departement: region for region, departements in regions_departements.items() for departement in departements}

# Ajouter la colonne "region" en utilisant le dictionnaire pour mapper les départements à leurs régions
df['region'] = df['libellé_du_département'].map(departement_region)

# Réorganiser les colonnes pour placer "region" devant "libellé_du_département"
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_reorganized = df[cols]

# Chemin vers le fichier Excel de sortie
output_file_path = 'dataset/dataset_finale_region.xlsx'

# Sauvegarder le dataframe modifié dans un nouveau fichier Excel
df_reorganized.to_excel(output_file_path, index=False)

print(f"Le fichier a été sauvegardé avec succès à l'emplacement suivant : {output_file_path}")
