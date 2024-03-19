# Documentation du Pipeline de Traitement des Données

## Sommaire

- [1. Objectif](#objectif)
- [2. Composantes du Pipeline](#composantes-du-pipeline)
  - [2.1. Requirements](#requirements)
  - [2.2. Scripts et Ordre d'Exécution](#scripts-et-ordre-dexécution)
    - [2.2.1. Formattage.py - Script Maître](#formattagepy---script-maître)
    - [2.2.2. Instructions d'Exécution](#instructions-dexécution)
  - [2.3. But du Pipeline](#but-du-pipeline)
- [3. Justification du choix de la région géographique et des critères](#justification-du-choix-de-la-région-géographique-et-des-critères)
  - [3.1. Région géographique choisie](#région-géographique-choisie)
  - [3.2. Critères sélectionnés](#critères-sélectionnés)
    - [3.2.1. Données électorales détaillées](#1-données-électorales-détaillées)
    - [3.2.2. Données socio-économiques](#2-données-socio-économiques)
    - [3.2.3. Données démographiques](#3-données-démographiques)
  - [3.3. Justifications des choix](#justifications-des-choix)
- [4. Démarche suivie](#démarche-suivie)
  - [4.1. Collecte de données](#collecte-de-données)
  - [4.2. Nettoyage et prétraitement des données](#nettoyage-et-prétraitement-des-données)
  - [4.3. Exploration des données](#exploration-des-données)
  - [4.4. Méthodes et outils utilisés](#méthodes-et-outils-utilisés)
- [5. Prédiction](#prédiction)

## Objectif

Ce pipeline de traitement des données a été conçu pour transformer des données brutes en un ensemble structuré, normalisé et enrichi, prêt pour des analyses avancées. Il assure la qualité et la cohérence des données à travers plusieurs étapes de transformation.

## Composantes du Pipeline

Le pipeline se compose de cinq scripts principaux, exécutés dans un ordre spécifique par un script maître (`Formattage.py`). Chaque script a un rôle défini dans le processus de nettoyage et de préparation des données.

### Requirements

Voici le fichier `requirements.txt` contenant les bibliothèques Python utilisées dans les scripts :
- `pandas`
- `openpyxl`
- `logging`
- `re`
- `statsmodels`
- `scikit-learn`
- `joblib`

### Scripts et Ordre d'Exécution

0. Avant tout installez tous les packages python nécessaires : `pip install -r requirements.txt`
1. `Formattage07121722.py` - Prépare les données brutes, corrigeant les formats de date, standardisant les noms de colonnes, et supprimant les enregistrements superflus.
2. `Normalisation.py` - Normalise les données pour assurer une cohérence, corrige les erreurs de saisie, et uniformise les formats.
3. `Formatting-merge2.py` - Fusionne les données de sources multiples, garantissant l'intégrité et la cohérence des données combinées.
4. `add_age_vote.py` - Enrichit les données avec des informations calculées, comme l'âge basé sur la date de naissance et des catégories de vote.
5. `Normalisation2.py` - Applique une couche supplémentaire de normalisation pour peaufiner les données après les enrichissements et les modifications précédentes.
6. `region.py` - Ajoute la région à tous les départements.

#### Formattage.py - Script Maître

Ce script orchestre l'exécution séquentielle des autres scripts. Il utilise la bibliothèque `subprocess` pour appeler chaque script Python dans l'ordre spécifié, garantissant que les données passent par toutes les étapes nécessaires du processus de préparation.

### Instructions d'Exécution

1. Placez tous les scripts et les ensembles de données nécessaires dans un même répertoire.
2. Assurez-vous que Python est correctement installé sur votre système.
3. Ouvrez un terminal ou une invite de commande dans le répertoire contenant les scripts.
4. Exécutez le script maître avec la commande : `python Formattage.py`.
5. Le script maître exécutera automatiquement chaque script dans l'ordre, affichant le statut de chaque étape dans le terminal et enregistrant les détails dans un fichier log (`data_processing.log`).

### But du Pipeline

Le but de ce pipeline est de fournir une méthode structurée et répétable pour préparer les données à des fins d'analyse. En automatisant le processus de nettoyage, de normalisation, et d'enrichissement des données, nous visons à améliorer l'efficacité et la précision des analyses ultérieures, tout en réduisant le potentiel d'erreur humaine.

## Justification du choix de la région géographique et des critères

### Région géographique choisie
Nouvelle-Aquitaine

### Critères sélectionnés

#### 1. Données électorales détaillées
- `libellé_de_la_région` : Nom de la région pour l'identification
- `année` : Année de l'élection
- `tour` : Tour de l'élection (1er, 2nd, etc.)
- `parti` : Parti politique des candidats
- `tendance_politique` : Orientation politique (gauche, droite, etc.)
- `inscrits` : Nombre d'électeurs inscrits
- `abstentions` : Nombre d'abstentions
- `votants` : Nombre de votants
- `exprimés` : Nombre de suffrages exprimés
- `voix` : Nombre de voix par parti
- `%_voix/ins` : Pourcentage des voix par rapport aux inscrits
- `%_voix/exp` : Pourcentage des voix par rapport aux exprimés
- `moyenne_du_parti_XX_ans` : Pourcentage moyen des voix par tranche d'âge pour chaque parti

#### 2. Données socio-économiques
- `taux_de_chômage` : Taux de chômage dans la région
- `incidents_de_délinquance` : Nombre d'incidents liés à la délinquance
- `pib` : Produit intérieur brut de la région

#### 3. Données démographiques
- `18-24_ans`, `25-34_ans`, `35-49_ans`, `50-64_ans`, `65_ans_et_plus` : Répartition de la population par tranches d'âge

### Justifications des choix

- La région Nouvelle-Aquitaine est représentative d'une grande diversité territoriale, offrant un bon équilibre entre zones urbaines, semi-urbaines, et rurales. Elle offre une quantité substantielle de données pour une analyse robuste.

- Les données électorales détaillées par parti, tendance politique, nombre de voix, pourcentages et tranches d'âge sont cruciales pour entraîner des modèles prédictifs fiables des comportements électoraux. Elles permettent d'analyser finement les préférences selon les caractéristiques des électeurs.

- Le taux de chômage et le PIB sont des indicateurs économiques majeurs qui influencent souvent les choix électoraux. Ils reflètent le contexte socio-économique de la région.

- Les incidents de délinquance apportent une dimension sécuritaire, un critère déterminant pour beaucoup d'électeurs.

- La répartition par tranches d'âge permet d'étudier les tendances de vote selon les générations et d'adapter les analyses en conséquence.

## Démarche suivie

### Collecte de données
- Les données ont été récupérées à partir des sites data.gouv.fr et insee.fr, incluant des informations sur le chômage, la délinquance, le PIB, la population, et les résultats des élections présidentielles de 2007 à 2022.

### Nettoyage et prétraitement des données
- Plusieurs scripts Python ont été utilisés pour effectuer diverses tâches de nettoyage et de prétraitement :
  - `Formattage07121722.py`, `Normalisation.py`, `Formatting-merge2.py`, `add_age_vote.py`, `Normalisation2.py`.

### Exploration des données
- Une exploration approfondie des données a été réalisée pour comprendre leur structure, identifier les anomalies, et préparer les étapes de modélisation.

### Méthodes et outils utilisés
- Python et ses bibliothèques (Pandas, Logging, Re), ainsi que Excel pour le stockage initial des données.

## Prédiction

### IA_predict.py
- Script d'intelligence artificielle pour la prédiction des tendances politiques dans la région Nouvelle-Aquitaine.

### Structure du code
- Le script procède au chargement, prétraitement, et prédiction des caractéristiques futures, utilisant des modèles ARIMA et de classification pour prédire les tendances politiques.

### Utilisation
- Ajustez le chemin vers le fichier de données et exécutez le script pour obtenir les prédictions des tendances politiques futures.

### Résultats
- Le script affiche la précision des modèles et les tendances politiques prédites, avec une précision globale de 68%.
