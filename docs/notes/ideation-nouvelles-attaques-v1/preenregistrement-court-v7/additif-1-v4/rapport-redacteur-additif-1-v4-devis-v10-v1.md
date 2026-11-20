# Rapport du rédacteur — additif 1 v4 au préenregistrement court v9 et devis v10 — v1

Pièce de travail (classe C), 2026-11-20 ; date des deux pièces : 14:25:03Z, l'heure du journal de la première passe de l'outil. Mandat `9b1e92db…`, toujours en vigueur ; demande de la session de l'organisme après la seconde vérification ; précisions de la mère de 14:25Z (R-4293, R-4294), reçues pendant le travail. Processeur seul : aucun appel, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit, aucune publication. Aucune méthode d'attaque, aucun procédé, aucun nom ni énoncé de mode, aucune case nommée, aucune valeur de clé, aucun identifiant de modèle. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

- **L'additif 1 v4** : `8e3d77a368189304fab58ddd548c4e21c30f5f469c36661620006db1a7613215`. **Le devis v10** : `5737ec6ed4d32635b91d04c7aad0cae894615b18a0129b8906eb196337aa5b77`. Ni l'un ni l'autre n'est vérifié ni scellé.
- Chacun est fait en deux passes. **La première passe égale l'essai du vérificateur, à l'octet** : `45468c9015ac0c1509e167703220af32522b2c4040be56172a035e7db3667534` pour l'additif (6 remplacements), `df11ef02b91964c49aac134a5ed896fd32c47c38cb929c64c20bef6308bff30a` pour le devis (1 remplacement).
- **Aucun chiffre du calcul ne change** ; le calcul v6 et sa sortie ne sont pas touchés.

## 1. Pièces lues

La vérification (`7ba42c5e20e4b2b67d9f67e15c13a17a281efdfa590397aef7f81aa32f8375ce`, lue en entier) et ses deux jeux (`3a8bbc18…`, `24afd974…`), « OK » contre leurs compagnons. Sur `origin/main`, commit `37a4350167771c897d86d838fa3e6dfff4eb8aed` : `registres/go.md` (`153eb6f6…`, GO-2026-11-20-65 lu à la lettre) et `registres/decisions.md` (`55a4d3f21d00bd98566333381e03bc36c65fb7a2629060bf2c7247e5ea9970a3`, R-4287 à R-4294 lues à la lettre).

## 2. Première passe : telles quelles

V5 et G1 à G5 sur l'additif ; W3 sur le devis. Mot pour mot des jeux du vérificateur.

## 3. Seconde passe : textes de ma main

Sur les précisions de la mère, vérifiées à la lettre de R-4293 et R-4294.

**(b) Le chiffre de la réserve sur la clé Luc.** Deux remplacements, Ancien et Neuf exacts :

- Additif (dans le texte de V5). Ancien : « (R-4289 : étage 2, 87,7701 USD) ». Neuf : « (R-4289, précisée par R-4293, point b : étage 2, 88,36 USD, le plafond de son accord, borne sûre ; les 87,7701 USD qu'écrivait R-4289 sont le pire de l'étage 2 entier, ses deux juges, et non la réserve) ».
- Devis (dans le texte de W3). Ancien : « son reste relu moins le pire des lots non clos sur la clé (étage 2 : 87,7701 USD), écrite au complément de valeurs ». Neuf : « son reste relu moins le pire des lots non clos sur la clé (étage 2 : 88,36 USD, le plafond de son accord, borne sûre, R-4293 ; les 87,7701 USD qu'écrivait R-4289 sont le pire de l'étage 2 entier, ses deux juges, et non la réserve), écrite au complément de valeurs ».

**(a) R-4287 et R-4289 tiennent ensemble.** La phrase de R-4293 est citée à l'additif (§ 6, ligne 412) et au devis (§ 10.8), à la suite de la lecture de 14:01Z.

**(c) Arrêt n° 27.** « Proposé » est retiré du § 4 bis, point 1 ; l'arrêt est dit accepté (R-4293, point c).

**(d) Table et renvois.** Une ligne de table cite R-4288, R-4289, R-4293 et R-4294 ; le chapeau du « sens des trois conditions » renvoie à ces lignes du registre.

**Tenue.** Additif : titre, date, statut, phrase de version (« GO-2026-11-20-65 lève la réserve »), table (devis v10, chemins de la v4, seconde vérification), entrée « Vérification 2 ». Devis : titre, phrase de version, statut, deux mentions de la version qui va à Lazar.

Comptes : additif, 15 remplacements à la seconde passe ; devis, 6.

## 4. Écarts

1. **Un premier jet du devis v10 est écarté, et gardé.** Il a été produit avant les précisions de 14:25Z, à la racine de mon dossier (`30e4d94f…`, avec son jeu `remplacements-devis-etape-1-vers-v10-v1.json`). L'outil ne récrit jamais un fichier : les pièces rendues sont dans le sous-dossier `rendu/`. Le premier jet n'est pas une pièce.
2. **Un chiffre neuf entre, hors du calcul** : 88,36 USD, la réserve de l'étage 2 sur la clé Luc, citée de R-4293. Il n'entre dans aucun total du devis ; je ne me suis donc pas arrêté. Je ne l'ai pas vérifié sur la pièce de l'accord de l'étage 2.
3. **« Proposé » reste dans la phrase de version de la v3**, qui est de l'histoire ; la phrase de version de la v4 dit l'arrêt accepté.
4. **« Devis v8 » et « devis v9 »** restent dans des phrases non récrites ; la phrase de version de la v4 dit qu'ils se lisent « devis v10 », et la table nomme le devis v10.
5. **Copie de travail sur la branche** : écrite à `…/preenregistrement-court-v7/additif-1-v4/`, par analogie.
6. **La date** des deux pièces est l'heure du journal de la première passe (14:25:03Z), non celle de la seconde.
7. Compte des ancres par l'outil.

## 5. Fichiers rendus

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-additif-1-v4/rendu/`. Chacun a son compagnon.

- `additif-1-preenregistrement-court-v9-mode-tenu-a-l-ecart-et-retrait-espece-6-v4.md` et son journal
- `devis-course-nouvelles-attaques-v10.md` et son journal
- `remplacements-additif-1-etape-1-vers-v4-v1.json` ; `remplacements-devis-etape-1-vers-v10-v2.json`
- `differentiel-additif-1-v3-v4-v1.diff` ; `differentiel-devis-v9-v10-v1.diff`
- `rapport-redacteur-additif-1-v4-devis-v10-v1.md` (cette pièce)

Dans le dossier parent, avec leurs compagnons et leurs journaux : les deux fichiers de l'étape 1, `etape-1-additif-1-v3-plus-V5-G1-a-G5.md` et `etape-1-devis-v9-plus-W3.md`.

— rédacteur, modèle F
