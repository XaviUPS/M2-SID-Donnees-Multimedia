# 🧠 Module AUDIO – Traitement Audio et Génération de Données

Ce dossier contient une série de notebooks Jupyter dédiés à la préparation et au traitement des données audio à partir de fichiers vidéo (mp4), ainsi qu’à la création des fichiers CSV nécessaires à l’entraînement de modèles d’apprentissage automatique.

---

## 📁 Structure du dossier

### Dossiers :

* **CNN/**
  Contient les notebooks, scripts ou modèles liés aux réseaux de neurones convolutifs (CNN) utilisés pour l’analyse ou la classification audio.

* **PANNs/**
  Contient les notebooks et modèles associés aux **Pretrained Audio Neural Networks (PANNs)**, utilisés pour l’extraction de caractéristiques audio pré-entraînées.

---

### Notebooks principaux :

#### 🎧 Conversion mp4 à wav - Module AUDIO.ipynb

Ce notebook permet de :

* Extraire la piste audio des vidéos au format `.mp4`
* Convertir ces pistes en fichiers `.wav` exploitables pour le traitement audio ou la classification
* Vérifier la qualité et la cohérence du format audio obtenu

**Entrées :** fichiers `.mp4`

**Sorties :** fichiers `.wav`

---

#### 🗂️ Création des CSV (video_id, label) - Module AUDIO.ipynb

Ce notebook génère un fichier **CSV** contenant les métadonnées nécessaires à l’entraînement des modèles :

* `video_id` : identifiant unique de la vidéo/audio
* `label` : étiquette associée

**Entrées :** répertoire contenant les fichiers audio

**Sorties :** fichier `.csv`

---

#### 🔊 Split json only audio videos.ipynb

Ce notebook gère la **séparation et la sélection des vidéos audio** à partir d’un fichier JSON :

* Filtrage des entrées contenant uniquement de l’audio
* Création d’un sous-ensemble de données pour l’entraînement/test

**Entrées :** fichier `.json`

**Sorties :** JSON ou CSV filtré avec uniquement les vidéos/audio pertinentes

---