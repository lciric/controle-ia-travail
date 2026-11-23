# Faits du côté exposé pour le devis du rejeu des activations du saboteur, voie (A) — v1

Pièce de travail (classe C), 2026-11-23 vers 23:40Z (`date -u`), exécutante v7. Noms, tailles, heures et prix seulement ; aucune sortie ouverte ; aucune pièce du côté des sondes lue.

- Accord : GO-2026-11-23-39 (plafond provisoire 15 USD, échéance 2026-11-30) ; voie (A) déjà dépensée ≈ 15,35 USD sous GO-2026-11-22-75 (compte rendu `compte-rendu-course-voie-A-62094628-v1.md`).
- Sorties de la course : `essai/iib-explo-v8` à 3326499e ; 62 fichiers scellés vérifiés + 9 traces ; 198 558 542 octets ; dossier des tours 39 Mo ; deux adaptateurs (`adaptateur-eleve-iib-v5.pt` 27 347 935 octets, `adaptateur-temoin-jumeau-iib-v5.pt` 27 350 031 octets). Identifiants d'actions versés : `ids-actions-course-iib-v5.json`, `ids-actions-temoins-iib-v5.json`, `ids-actions-evaluation-iib-v5.json`, `tours/ids-tour-NNN-maitre.json` (20), `evaluation/ids-evaluation-{H,B50,B100,TJ100}.json`.
- Modèle : meta-llama/Llama-3.1-8B-Instruct, révision 0e9e39f2… ; code de course 192a429e (`prep/iib-tirage-carte-v1`).
- Carte de la course : A100 SXM4 80 Go, 1,08 USD/h, stockage 0,0333 USD/h (100 Go), forfait de téléchargement 1,5625 USD.
- Durées observées (marques PROGRES) : installation, essais (313 passés) et chargement 04:21:19Z → 04:39:45Z (18 min) ; 20 tours de 32 épisodes en génération 04:42Z → 10:29:16Z (≈ 17,4 min par tour) ; distillation 10:29Z → 10:54:28Z (102 épisodes) ; évaluation, 4 conditions × 64 épisodes en génération puis oracles, 10:54:40Z → 13:20:20Z.
- Un rejeu en passe avant sur des actions déjà écrites (sans génération) coûte bien moins qu'un tour ; aucune mesure de sa vitesse n'existe ici.
- Exigences des sondes reçues pour une course future : `exigences-sondes-pour-course-future-v1.md` (f54c1aaa) et son erratum 1 (ec4b6e1f, e0f01103…).
