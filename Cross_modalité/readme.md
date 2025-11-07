# 🧩 Projet non-alternant — Cross-modalité

---

## 🚀 Vue d'ensemble
Ce dépôt contient le notebook et les scripts nécessaires à la **fusion des modalités Audio, Vidéo et Texte** dans le cadre du projet non-alternant.  
L’objectif est de combiner les prédictions issues des classifieurs unimodaux afin d’obtenir une **représentation multimodale robuste** et d’améliorer la performance globale du modèle final.

Les fichiers d’entrée sont les **distributions de probabilités** produites par chaque modalité :
- `test_predictions_audio.csv`
- `test_predictions_video.csv`
- `test_predictions_texte.csv`

Ces distributions sont ensuite combinées et exploitées pour :
- effectuer une **fusion par moyenne pondérée** ou **concaténation**,  
- évaluer les performances sur l’ensemble de test.

---

## 🗂 Contenu du dépôt
- `Projet non-alternant - Cross-modalité.ipynb` : Notebook principal réalisant la fusion multimodale.  

---

## ✅ Prérequis généraux
- **Python 3.10+**
- **Fichiers requis :**
  - `train_predictions_audio.csv`
  - `train_predictions_video.csv`
  - `train_predictions_texte.csv`.

---

## 🧪 1. Notebook « Cross-modalité »

### 📦 INSTALLATIONS
Effectuer l’installation des dépendances uniquement lors de la première exécution :
```python
!pip install numpy pandas scikit-learn matplotlib seaborn torch tqdm
```

### 📥 IMPORTS & CHEMINS
Monter Google Drive ou définir les chemins locaux vers :
- `chemin_audio` : dossier contenant le fichier CSV dela modalité audio
- `chemin_vidéo` : dossier contenant le fichier CSV dela modalité vidéo
- `chemin_texte` : dossier contenant le fichier CSV dela modalité texte.

---

## 🔧 2. Architecture du code

### ⚙️ Préparation des données
- Chargement des fichiers de prédictions (Audio, Vidéo, Texte) pour test.  
- Vérification des formats.    

### 🔗 Fusion multimodale
Deux stratégies principales sont implémentées :

**Fusion moyenne pondérée**  
   - Pondération configurable (ex. 0.4 Texte, 0.3 Vidéo, 0.3 Audio)  
   - Permet de tester plusieurs rapports entre modalités.

---

## 📊 3. Évaluation & visualisation

- **Affichage des performances par modalité et globales.** 
- **Comparaison directe** entre combinaisons de modalités.  

---

## ✅ Conclusion
Ce dépôt fournit une **pipeline complète de fusion multimodale** :
- Intégration des sorties de chaque modalité (Texte, Audio, Vidéo),
- Combinaison via moyenne pondérée ou non.

L’ensemble permet d’exploiter la **complémentarité inter-modale** pour maximiser la robustesse du système global.🚀
