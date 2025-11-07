# M2 SID Donnees-Multimedia – Analyse Multimodale (Audio, Vidéo, Texte)

Ce dépôt regroupe l’ensemble des modules nécessaires à la construction d’un **système d’analyse multimodale**.
Chaque dossier correspond à un type de donnée ou à une composante spécifique du projet : audio, texte, vidéo, corpus de données, ou encore intégration cross-modale.

---

## 🚀 Organisation du flux de travail

1. **Préparation des données** : à partir du dossier `Corpus/`
2. **Traitement individuel des modalités** :
   * `Audio/`
   * `Vidéo/`
   * `Texte/`
3. **Fusion multimodale** : dans `Cross-modalité/`

---

## 📁 Structure du projet

### **Audio/**

Contient les notebooks et scripts liés au **traitement des signaux audio** :

* Extraction et conversion des pistes audio (mp4 → wav)
* Génération de fichiers CSV pour l’étiquetage et la classification
* Utilisation de modèles CNN et PANNs pour l’analyse audio

👉 Voir le fichier [`README - Module Audio`](./Audio/readme.md) pour plus de détails.

---

### **Vidéo/**

Regroupe les notebooks dédiés au **traitement de la vidéo** :

* Extraction d’images ou de séquences
* Analyse visuelle et détection d’événements

👉 Voir le fichier [`README - Module Video`](./Video/readme.md) pour plus de détails.

---

### **Texte/**

Inclut les notebooks et scripts pour le **traitement du langage naturel (NLP)** :

* Implémentation de différents descripteurs
* Implémentation de réssaux de neurones avec GridSearch

👉 Voir le fichier [`README - Module Texte`](./Texte/readme.md) pour plus de détails.

---

### **Corpus/**

Dossier contenant les **données brutes et les métadonnées** :

* Ensemble des fichiers multimédias (audio, vidéo, texte)
* JSON et CSV décrivant les identifiants, labels et annotations
* Organisation du dataset pour l’entraînement et la validation

👉 Voir le fichier [`README - Corpus`](./Corpus/readme.md) pour plus de détails.

---

### **Cross modalité/**

Module dédié à la **fusion et à l’analyse conjointe** des différentes modalités

👉 Voir le fichier [`README - Cross modalité`](./Cross_modalité/readme.md) pour plus de détails.

---

## ✍️ Auteurs

Mohamed-Taha BELHAJ

Alexandre DUPORTE

Yohann JEANFAIVRE

Xavier PUJOL

