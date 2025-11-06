# Projet – Partie Vidéo

## Modèles testés

Les modèles suivants ont été expérimentés :

- `test_final.ipynb`
- `R2Plus1D.ipynb` – utilise les vidéos splitées selon la demande.
- `R2Plus1D_split.ipynb` – utilise des vidéos splitées aléatoirement.
- `modele_vit.ipynb`
- `modele_videomae.ipynb`

## Préparation des données

Pour convertir les vidéos en images et préparer les datasets :

- `videos_to_image.ipynb` – extraction des images à partir des vidéos.
- `merge_pkl.ipynb` – fusion des fichiers `.pkl` générés.

## Modèles enregistrés

Les modèles sauvegardés au format `.pth` :

- `old_r2.pth`
- `new_r2.pth`
- `best_mvitv2.pth`

## Test des modèles

- `mvit_test_final.ipynb`
- `test_final.ipynb`

## Résultats

Les résultats des tests sont disponibles dans le dossier `test` :

- Les fichiers `.pkl` contiennent les images extraites des vidéos test.
- `test_predictions_video.csv` – contient les probabilités pour chaque catégorie, utilisé pour combiner avec les résultats audio.

Les prédictions finales des modèles sont également disponibles en PDF :

- `predictions_best_mvitv2.pdf`
- `new_R2.pdf`
- `ancien_R2.pdf`
