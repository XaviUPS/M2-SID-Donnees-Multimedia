# 🗂️ Module CORPUS – Données du projet multimodal

Le dossier **Corpus** regroupe les **données de référence** utilisées dans le projet multimodal (audio, texte, vidéo).
Il centralise les vidéos sources, leurs annotations et les métadonnées associées.

---

## 📁 Structure du dossier

* **annotation/**
  Contient les fichiers d’annotations du **jeu de données MSR-VTT 10K**, incluant :

  * Un fichier `readme.txt` décrivant la structure des fichiers JSON (info, vidéos, phrases, etc.)
  * Un fichier `category.txt` listant les 20 catégories thématiques (ex. musique, sport, film, science, etc.)

* **csv/**
  Dossier destiné aux fichiers CSV générés pour le prétraitement et l’organisation des données (ex. identifiants vidéo et labels).

* **json/**
  Contient les fichiers JSON de référence et les métadonnées structurées du corpus.

* **train_val_videos/**
  Ensemble des vidéos utilisées pour l’**entraînement** et la **validation** des modèles.

* **test_videos/**
  Ensemble des vidéos réservées à la **phase de test** et d’évaluation finale.

---

## 🧭 Description générale

Le **corpus MSR-VTT 10K** est une base de données de vidéos accompagnées de descriptions textuelles et de métadonnées.
Chaque entrée relie :

* une **vidéo** (avec un identifiant, une catégorie et une URL),
* une ou plusieurs **phrases descriptives** (captions),
* des **informations contextuelles** (auteur, année, split d’entraînement, etc.).

Les vidéos sont réparties en trois ensembles :

* **Train :** 6 513 vidéos
* **Validation :** 497 vidéos
* **Test :** 2 990 vidéos
