# 📚 Projet non‑alternant — Modalité TEXTE

---

## 🚀 Vue d'ensemble
Ce dépôt contient l'ensemble du code, des notebooks et des scripts permettant d'entraîner et d'évaluer différents modèles basés sur la **modalité texte** dans le cadre du projet non‑alternant. L'objectif est d'extraire et d'exploiter des représentations textuelles issues de captions vidéo (ou de descriptions générées via coNeTTe) afin d'entraîner des classifieurs neuronaux.

Plusieurs descripteurs sont étudiés :
- **SBERT embeddings**
- **Contextual embeddings** (non utilisés car trop coûteux)
- **Topic Modeling**
- **Character‑level TF‑IDF**
- **CLIP Text Encoder**
- **Concaténations de descripteurs**
- **Descriptions coNeTTe**

Chaque descripteur donne lieu à une initialisation, une application et un entraînement permettant de sélectionner le meilleur modèle.

---

## 🗂 Contenu du dépôt
- `Yohann JEANFAIVRE - Projet non-alternant - Modalité TEXTE.ipynb` : Notebook principal pour l'ensemble des descripteurs texte.
- `Yohann JEANFAIVRE - Projet non-alternant - Modalité TEXTE avec coNeTTe.ipynb` : Version du notebook utilisant les descriptions générées par coNeTTe.
- `test_conette.py` : Script autonome permettant de générer les descriptions coNeTTe.

---

## ✅ Prérequis généraux
- Python 3.10 pour les exécutions locales
- GPU facultatif mais recommandé pour SBERT / CLIP ainsi que les réseaux
- Fichiers JSON :
  - `train_videodatainfo_audio.json`
  - `val_videodatainfo_audio.json`
  - `test_videodatainfo_audio.json`

---

## 🧪 1. Notebook « Modalité TEXTE »

### 📦 INSTALLATIONS
À exécuter uniquement lors de la première utilisation du notebook.

### 📥 IMPORTS & CHEMINS
Monter Google Drive puis spécifier :
- `chemin_json` : Emplacement des fichiers JSON des captions.
- `chemin_texte` : Répertoire contenant le notebook et où seront sauvegardés :
  - Les modèles `.pt`
  - Les prédictions `.csv`

---

## 🔧 2. Architecture du code
### ⚙️ Préparation
- Initialisation des variables.
- Définition d'une seed commune à toutes les modalités pour assurer la reproductibilité.

### 🧠 Modèles
Deux réseaux de neurones identiques sont définis, seule la fonction d'activation change :
- `TextClassifierReLu`
- `TextClassifierSigmoid`

### 🔍 Fonction clé : `reseau_gridsearch`
- Entraîne un modèle avec **grid‑search** sur plusieurs hyperparamètres.
- Affiche :
  - Accuracy / Loss par epoch
  - Graphiques d'apprentissage
  - Matrice de confusion
- Sauvegarde du meilleur modèle.
- Deux modifications minimes sont nécessaires selon le descripteur (indiquées dans le code).

### 🗃 Agrégation : `regrouperCaptionsVideo`
- Regroupe les 20 captions d'une vidéo en une seule prédiction via **vote majoritaire**.
- Affichage d'une matrice de confusion.

---

## 🔬 3. Descripteurs disponibles
> ⚠️ Chaque sous‑partie est **indépendante** : n'exécuter que les blocs correspondant au descripteur souhaité.

### 🟦 SBERT embeddings
**Initialisation :** fine‑tuning léger sur 2 epochs (long mais à faire une seule fois).

**Application :** calcul des embeddings pour X_train, X_val, X_test.

### 🟧 Contextual embeddings
Non utilisé car trop coûteux.

### 🟩 Topic Modeling
- Application du descripteur sur chaque split.
- Entraînement des modèles ReLU et Sigmoid.

### 🟪 Character‑level TF‑IDF
**Pré‑requis :** deux modifications dans `reseau_gridsearch` (indiquées en commentaire).

### 🟫 CLIP Text Encoder
- Encoding via le text‑encoder de CLIP.
- Entraînement des modèles basés sur ces embeddings.

### 🟦 Concaténation des deux meilleurs descripteurs
- Application des deux descripteurs sélectionnés.
- Normalisation via `l2norm`.
- Entraînement d'un modèle final combiné.

---

## 📤 4. Export des prédictions
- Génération d'un `.csv` contenant les **distributions de probabilités**, utilisable en cross‑modalité.
- Fonction dédiée : `regrouperCaptionsVideoProba` (moyenne des distributions sur les 20 captions).
- Fichier sauvegardé sous : `test_predictions_texte.csv`.

---

# 🧩 5. Script local : `test_conette.py`
> ⚠️ Exécuter **en local uniquement**.

### ✅ Installation
```
python -m venv venv_conette
venv_conette\Scripts\activate
python -m pip install --upgrade pip
pip install torch==1.13.1+cpu torchvision==0.14.1+cpu torchaudio==0.13.1+cpu --index-url https://download.pytorch.org/whl/cpu
pip install spacy==3.7.2
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl
pip install conette==0.3.2
pip install tqdm
python test_conette.py
```

### ✅ Sortie
Le script génère un fichier :
- `descriptions_conette.csv`

À placer dans :
`Corpus/csv/descriptions_conette.csv`

---

# 🧠 6. Notebook « Modalité TEXTE avec coNeTTe »
### 📥 Pré‑requis
Avoir exécuté `test_conette.py` et obtenu `descriptions_conette.csv`.

### 🔧 Fonctionnement
Identique au notebook principal, à l’exception :
- des fonctions de regroupement,
- de la logique de concaténation,
- du format d'enregistrement du `.csv` final.

---

## ✅ Conclusion
Ce dépôt fournit une chaîne complète pour :
- préparer les données textuelles,
- calculer plusieurs types d'embeddings,
- entraîner des réseaux de neurones avec grid‑search,
- exporter des prédictions compatibles cross‑modalité.

Pour toute question ou amélioration, n'hésitez pas à ouvrir une *issue* dans le repository ! 🚀

