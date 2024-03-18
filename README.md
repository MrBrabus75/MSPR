# Sommaire

## 1. [Objectif](#objectif)

## 2. [Composantes du Pipeline](#composantes-du-pipeline)
 - 2.1. [Requirements](#requirements)
 - 2.2. [Scripts et Ordre d'Exécution](#scripts-et-ordre-dexécution)
   - 2.2.1. [Formattage.py - Script Maître](#formattagepy---script-maître)
   - 2.2.2. [Instructions d'Exécution](#instructions-dexécution)
 - 2.3. [But du Pipeline](#but-du-pipeline)

## 3. [Justification du choix de la zone géographique et des critères](#justification-du-choix-de-la-zone-géographique-et-des-critères)
 - 3.1. [Zone géographique choisie](#zone-géographique-choisie)
 - 3.2. [Critères sélectionnés](#critères-sélectionnés)
   - 3.2.1. [Données électorales détaillées](#1-données-électorales-détaillées)
   - 3.2.2. [Données socio-économiques](#2-données-socio-économiques) 
   - 3.2.3. [Données démographiques](#3-données-démographiques)
 - 3.3. [Justifications des choix](#justifications-des-choix)

## 4. [Démarche suivie](#démarche-suivie)
 - 4.1. [Collecte de données](#collecte-de-données)
 - 4.2. [Nettoyage et prétraitement des données](#nettoyage-et-prétraitement-des-données)
 - 4.3. [Exploration des données](#exploration-des-données)
 - 4.4. [Méthodes et outils utilisés](#méthodes-et-outils-utilisés)



# Documentation du Pipeline de Traitement des Données

## Objectif

Ce pipeline de traitement des données a été conçu pour transformer des données brutes en un ensemble structuré, normalisé et enrichi, prêt pour des analyses avancées. Il assure la qualité et la cohérence des données à travers plusieurs étapes de transformation.

## Composantes du Pipeline

Le pipeline se compose de cinq scripts principaux, exécutés dans un ordre spécifique par un script maître (`Formattage.py`). Chaque script a un rôle défini dans le processus de nettoyage et de préparation des données.

# Requirements

Voici le fichier requirements.txt contenant les bibliothèques Python utilisées dans les scripts :
pandas
openpyxl
logging
re
statsmodels
scikit-learn
joblib

Explication :

- `pandas` : Bibliothèque utilisée pour la manipulation et l'analyse des données, notamment pour lire et écrire des fichiers Excel.
- `openpyxl` : Bibliothèque utilisée conjointement avec pandas pour la lecture et l'écriture des fichiers Excel.
- `logging` : Bibliothèque utilisée pour la journalisation des opérations effectuées.
- `re` : Bibliothèque pour les expressions régulières, utilisée dans la normalisation de texte.
- `statsmodels` : Bibliothèque pour l'IA ARIMA
- `scikit-learn` : Bibliothèque pour les Algo d'IA
- `joblib` : export de l'ia

## Scripts et Ordre d'Exécution
0. Avant tout installez tout les packages python necessaire : `pip install -r requirements.txt`
1. `Formattage07121722.py` - Prépare les données brutes, corrigeant les formats de date, standardisant les noms de colonnes, et supprimant les enregistrements superflus.
2. `Normalisation.py` - Normalise les données pour assurer une cohérence, corrige les erreurs de saisie, et uniformise les formats.
3. `Formatting-merge2.py` - Fusionne les données de sources multiples, garantissant l'intégrité et la cohérence des données combinées.
4. `add_age_vote.py` - Enrichit les données avec des informations calculées, comme l'âge basé sur la date de naissance et des catégories de vote.
5. `Normalisation2.py` - Applique une couche supplémentaire de normalisation pour peaufiner les données après les enrichissements et les modifications précédentes.
6. `region.py` - Ajotue la region a tout les départements

### Formattage.py - Script Maître

Ce script orchestre l'exécution séquentielle des autres scripts. Il utilise la bibliothèque `subprocess` pour appeler chaque script Python dans l'ordre spécifié, garantissant que les données passent par toutes les étapes nécessaires du processus de préparation.

## Instructions d'Exécution

1. Placez tous les scripts et les ensembles de données nécessaires dans un même répertoire.
2. Assurez-vous que Python est correctement installé sur votre système.
3. Ouvrez un terminal ou une invite de commande dans le répertoire contenant les scripts.
4. Exécutez le script maître avec la commande : `python Formattage.py`.
5. Le script maître exécutera automatiquement chaque script dans l'ordre, affichant le statut de chaque étape dans le terminal et enregistrant les détails dans un fichier log (`data_processing.log`).

## But du Pipeline

Le but de ce pipeline est de fournir une méthode structurée et répétable pour préparer les données à des fins d'analyse. En automatisant le processus de nettoyage, de normalisation, et d'enrichissement des données, nous visons à améliorer l'efficacité et la précision des analyses ultérieures, tout en réduisant le potentiel d'erreur humaine.

Cette documentation offre une vue d'ensemble claire et détaillée du fonctionnement et de l'objectif du pipeline de traitement des données, fournissant aux utilisateurs les informations nécessaires pour exécuter et adapter le pipeline à leurs besoins spécifiques.

# Justification du choix de la zone géographique et des critères

## Zone géographique choisie
Département de la Charente

## Critères sélectionnés

### 1. Données électorales détaillées
- `libellé_du_département` : Nom du département pour l'identification
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

### 2. Données socio-économiques
- `taux_de_chômage` : Taux de chômage dans le département
- `incidents_de_délinquance` : Nombre d'incidents liés à la délinquance
- `pib` : Produit intérieur brut du département

### 3. Données démographiques
- `18-24_ans`, `25-34_ans`, `35-49_ans`, `50-64_ans`, `65_ans_et_plus` : Répartition de la population par tranches d'âge

## Justifications des choix

- Le département de la Charente est représentatif d'une région semi-rurale de taille moyenne, offrant un bon équilibre entre quantité de données disponibles et complexité de traitement.

- Les données électorales détaillées par parti, tendance politique, nombre de voix, pourcentages et tranches d'âge sont cruciales pour entraîner des modèles prédictifs fiables des comportements électoraux. Elles permettent d'analyser finement les préférences selon les caractéristiques des électeurs.

- Le taux de chômage et le PIB sont des indicateurs économiques majeurs qui influencent souvent les choix électoraux. Ils reflètent le contexte socio-économique du département.

- Les incidents de délinquance apportent une dimension sécuritaire, un critère déterminant pour beaucoup d'électeurs.

- La répartition par tranches d'âge permet d'étudier les tendances de vote selon les générations et d'adapter les analyses en conséquence.

- La combinaison de ces données politiques, économiques, sécuritaires et démographiques offre une vision complète pour identifier les principaux facteurs corrélés aux résultats électoraux passés et futurs.

Cette sélection riche de critères variés et détaillés, associée à la taille adaptée du département, devrait permettre de mener une preuve de concept solide de prédiction des résultats des élections à venir dans la Charente.

# Démarche suivie

**Démarche suivie :**

1. **Collecte de données :**
   - Les données ont été récupérées à partir des sites data.gouv.fr et insee.fr, incluant des informations sur le chômage, la délinquance, le PIB, la population, et les résultats des élections présidentielles de 2007 à 2022.

2. **Nettoyage et prétraitement des données :**
   - Plusieurs scripts Python ont été utilisés pour effectuer diverses tâches de nettoyage et de prétraitement :
     - `Formattage07121722.py` : Formatage et fusion des fichiers de résultats électoraux.
     - `Normalisation.py` : Normalisation des données (suppression de lignes, ajout de colonnes, normalisation de texte, réorganisation des colonnes).
     - `Formatting-merge2.py` : Fusion des données électorales avec les données socio-économiques (chômage, délinquance, PIB, population).
     - `add_age_vote.py` : Ajout des données de résultats électoraux par tranches d'âge.
     - `Normalisation2.py` : Normalisation finale du dataset (conversion des types de données, gestion des valeurs manquantes, suppression des doublons, standardisation des noms de départements).

3. **Exploration des données :**
   - Bien que cette étape ne soit pas explicitement mentionnée, une exploration des données a probablement été effectuée pour comprendre leur structure, identifier les éventuelles anomalies et préparer les étapes suivantes.

**Méthodes et outils utilisés :**

- **Python** avec les bibliothèques suivantes :
  - **Pandas** pour le chargement, la manipulation et le nettoyage des données.
  - **Logging** pour la journalisation des opérations effectuées.
  - **Re** (expressions régulières) pour la normalisation de texte.
- **Excel** pour le stockage et la manipulation initiale des données (formats `.xlsx`).
- **Autres outils potentiels :**
  - Bibliothèques Python pour la visualisation des données (non mentionnées explicitement).
  - Outils d'exploration de données (non mentionnés explicitement).

En résumé, la démarche suivie comprend la collecte de données à partir de sources gouvernementales, un nettoyage et une normalisation approfondis à l'aide de scripts Python, et une préparation des données pour les analyses ultérieures. Les principaux outils utilisés sont Python (avec Pandas et d'autres bibliothèques) et Excel.

# Prédiction
- `IA_predict.py` : Script pour l'IA 
## Structure du code

Le code est structuré comme suit :

1. **Chargement des données** : Les données sont chargées à partir d'un fichier Excel spécifié.
2. **Prétraitement** : Les données pour la région Nouvelle-Aquitaine sont filtrées et préparées pour la prédiction.
3. **Prédiction des caractéristiques futures** : Les caractéristiques futures sont prédites en utilisant le modèle ARIMA pour plusieurs indicateurs économiques et démographiques.
4. **Préparation des données pour la modélisation** : Les caractéristiques prévues sont utilisées pour compléter le jeu de données, qui est ensuite divisé en ensembles d'entraînement et de test.
5. **Entraînement des modèles** : Plusieurs modèles de classification sont entraînés en utilisant une recherche sur grille pour identifier les meilleurs paramètres.
6. **Sélection du meilleur modèle** : Le modèle avec la meilleure précision est sélectionné comme le modèle final.
7. **Prédiction des tendances politiques** : Le modèle final est utilisé pour prédire les tendances politiques pour les années futures.

## Utilisation

Ajustez le chemin du fichier de données en fonction de votre environnement et exécutez le script. Le script affichera les meilleures configurations de modèles, leur précision et les prédictions des tendances politiques pour les années à venir.

## Résultats

Le script affiche la précision de chaque modèle testé ainsi que les paramètres de configuration optimaux. Le meilleur modèle est ensuite utilisé pour prédire les tendances politiques futures, qui sont également affichées.

Accuracy : 68%