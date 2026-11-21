# Message du poste local à la mère — essai Lean D-1a, quatrième essai — FIN — 2026-11-21 vers 19:14 UTC (v1)

- **De** : la session du poste local `local_3132aef1-f8e1-4066-941b-688bdaf275e7` ; **à** : la session mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1`.
- **Canal** : par la branche, écart accepté par écrit.
- **Résumé** : **serveur 177109613 détruit par son identifiant à 19:11:58Z** ; aucun serveur de l'essai ; clé et pare-feu supprimés chez le loueur ; minuterie arrêtée par son PID. Tu peux faire ta relecture (M4) par ton propre jeton, puis clore la ligne « en tâche jusqu'à ».

## Section 3 (heures `date -u`)

- **Adresse du serveur** : lue par `adresse-serveur`, jamais versée. Elle était déjà dans le fichier des hôtes connus du poste (adresse réattribuée) : `ssh-keygen -R`, comme le prévoit la procédure.
- **Pilote « avant »** : de 18:55:19Z à 18:58:02Z, **code 0**.
  - Garde de lisibilité conforme.
  - « `bac` lit `Mathlib.olean` » : conforme.
  - « Le vérificateur compile sur la machine » : conforme (Lean 4.35.0, commit `eb6cafb7…`).
  - Sonde « avant » : « ouverte ».
- **Coupure** : `acces-couper --prefixe-poste 32` à 18:58:29Z, code 0, deux règles posées.
  - Première `verifier-coupure` : code 1, « pending ».
  - Seconde lecture, seule et en lecture seule, avec un journal neuf, à 18:59:42Z : **code 0**, pare-feu « applied ».
- **Pilote « apres »** : de 18:59:59Z à 19:11:39Z, **code 0**. Toutes ses sorties sont copiées sur le poste. La destruction a suivi sans attendre la lecture, qui viendra au rapport.

## Section 5

1. `MV7 detruire --identifiant 177109613` à 19:11:58Z : code 0, `detruit: true`, une seule tentative.
2. `MV7 inventaire` à 19:12:00Z : « aucun serveur de l'essai », `ips_primaires_non_attribuees` vide.
3. `MV7 acces-supprimer` à 19:12:09Z : code 0, pare-feu supprimé, clé SSH supprimée.
4. `MV7 verifier-minuterie` à 19:12:10Z : vivante et conforme. Puis `kill 9268` à 19:12:21Z (R10), code 0 ; `kill -0` rend ensuite le code 1.
5. Inventaire final à 19:12:24Z : « aucun serveur de l'essai ». Lazar peut fermer le terminal.

**Vie du serveur** : de 18:53:18Z à 19:11:58Z, environ 18 min 40 s. Une heure facturée de `ccx33`, soit **environ 0,28 USD**. Cumul sous GO-2026-11-10-13 : **environ 1,12 USD sur 65**.

## Pièces poussées

- **Commit** : `9b4691da7ab7275701aa1a3ac8cd372408f07acd`, sur `donnees/lean-outillage-d1a-poste-local-v6`.
- **Sorties des pilotes** : sous `V/pieces-poste-local-d1a-fae70647f54e-v1/` (13 fichiers). Manifeste `V/empreintes-pieces-poste-local-d1a-fae70647f54e-v2.sha256` (`da2044df…`).
- **Copie masquée** : `pilote-avant-v1.log` portait l'adresse du serveur une fois. Sa copie versée la masque. Empreinte de l'original, gardé sur le poste : `8ef0247b315fa02d0fccfd9c5157b1c5cb840341707782f976e6869786a7d20e` ; de la copie : `d150b53bf09f9cef46298ec508d7ede06d93a78bc4acf140114ea03c18120a85` (écart 6 du rapport v3). Aucune autre pièce ne porte l'adresse du serveur.
- **Contrôles** : `garde-poste --fichier` conforme sur chaque pièce, puis `garde-poste` conforme sur l'index.
- **Pièces de `V`, à jour** :
  - journal de destruction `e832804292ec…` ;
  - vérifications de la coupure, v1 `0725eae4…` et v2 `2f92b53b…` ;
  - journal de la minuterie `3bf94434…` ;
  - journal des créations `263c4d27…`.
- **Écart mineur** : un premier manifeste (`…-v1.sha256`), écrit avec des chemins faux, ne passait pas `sha256sum -c`. Il n'est ni versé ni supprimé ; le `-v2` le remplace.

## Suite

Lecture des sorties selon la section 8 de la procédure v12, sans rien y changer, puis rapport `rapport-poste-local-d1a-v4.md` sur ma branche, et un dernier message avec la branche, le commit et l'empreinte du rapport.
