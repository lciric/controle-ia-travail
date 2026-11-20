# Vérification des corrections — additif 1 v4 au préenregistrement court v9 et devis v10 — v1

Pièce de travail (classe C), 2026-11-20, relevé de `date -u` : 14:30:32Z, après les rejeux et les relevés, avant l'écriture. Contre-lecteur neuf, modèle O, même vérificateur que pour les v2 et v3. Mandat `799b14c6…`, en-tête compris. Processeur seul : aucun appel, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Rien dans cette pièce ne porte de méthode d'attaque, de procédé, de nom ou d'énoncé de mode, de case nommée, de valeur de clé ni d'identifiant de modèle. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**À corriger, de lettre seulement : trois remplacements**, X1 et X2 sur l'additif, Y1 sur le devis.

- Les deux passes rejouent à l'octet.
- La première passe est égale à mes essais.
- La seconde passe est juste sur le fond des décisions R-4293 et R-4294 : 88,36 USD est bien le montant de GO-2026-11-20-26.
- Aucun chiffre du calcul ne change.
- « Aucune recette » : conforme.

Restent deux écarts de lettre. Le premier : R-4293 dit que 87,7701 USD est « le pire de l'étage 2 entier, les deux juges, et non la seule part de Luc » ; les textes écrivent « et non la réserve » (X1, Y1). Le second : les points e et i viennent du message de 13:58Z (R-4294), mais l'additif les range sous la décision de 13:45Z (X2).

**Une fois X1, X2 et Y1 portés tels quels, et l'égalité de l'octet constatée par `cmp` : conforme, à sceller.**

## 1. Pièces et empreintes

| pièce | empreinte | vérification |
|---|---|---|
| additif 1 v4 | `8e3d77a368189304fab58ddd548c4e21c30f5f469c36661620006db1a7613215` | compagnon « OK » ; rejeu égal (`cmp`) |
| devis v10 | `5737ec6ed4d32635b91d04c7aad0cae894615b18a0129b8906eb196337aa5b77` | compagnon « OK » ; rejeu égal (`cmp`) |
| étapes 1 | `45468c90…` ; `df11ef02…` | compagnons « OK » ; `cmp` égal à mes essais |
| jeux de seconde passe | `501f4843…` (15) ; `2866967b…` (6) | compagnons « OK » |
| différentiels ; rapport | `96e20160…`, `018a9835…` ; `b2f9a6c643b4087e9e6193b22f3c36257ef12f018ef0528bbafa4771261beec6` | recalculées |
| `registres/decisions.md` sur `origin/main` = commit `37a4350167771c897d86d838fa3e6dfff4eb8aed` | `55a4d3f21d00bd98566333381e03bc36c65fb7a2629060bf2c7247e5ea9970a3` | égale à la table ; R-4293 et R-4294 lus |
| `registres/go.md` sur `origin/main` | — | GO-2026-11-20-26 lu : « accord de calcul au plus 88,36 USD (pire du devis v7 ; cas haut 44,78) », montant 88,36 USD |

## 2. Rejeux

- Mon essai `45468c90…` + le jeu `501f4843…` donnent 15 remplacements et la sortie `8e3d77a3…`, égale à l'additif v4.
- Mon essai `df11ef02…` + le jeu `2866967b…` donnent 6 remplacements et la sortie `5737ec6e…`, égale au devis v10.

## 3. La seconde passe, à la lettre des décisions

- **(a) R-4287 et R-4289 tiennent ensemble.** La phrase de R-4293 est citée exactement à l'additif (§ 6, ligne 412) et au devis (§ 10.8) : « la ligne de 450 USD se lit sous GO-08 et GO-60, et le départ attend la ligne de calcul de Lazar sur le devis neuf ». Conforme.
- **(b) Réserve sur Luc, 88,36 USD.**
  - Le chiffre est juste : c'est le montant de GO-2026-11-20-26, son « au plus 88,36 USD », que R-4293 appelle « plafond de l'accord de l'étage 2 ».
  - La paraphrase est fausse : les textes disent que les 87,7701 USD « sont le pire de l'étage 2 entier, ses deux juges, et non la réserve ». R-4293 dit « et non la seule part de Luc ». Le motif de la mère est que ce chiffre couvre plus que Luc ; le texte en fait autre chose (X1, Y1).
  - Le renvoi « son accord » est rendu explicite : GO-2026-11-20-26.
- **(c) Arrêt n° 27 accepté (R-4293, point c)** : conforme. « Proposé » ne reste que dans la phrase de version de la v3, qui est de l'histoire.
- **(d) Citations.** La table cite R-4288, R-4289, R-4293 et R-4294 au commit `37a43501`, avec la bonne empreinte. Le chapeau du sens des conditions renvoie à ces lignes. Mais R-4294 date les points e et i du « message de 13:58Z », alors que le chapeau les range sous « décision de 13:45Z » (X2). Le texte du point i est celui de R-4294. Le point e garde le mot de R-4294 (« la condition sur la case entière suffit ») et y ajoute une conséquence déjà admise (« risque résiduel … accepté et déclaré », R-4289).
- **Tenue** : titre, date, statut, phrases de version, table (devis v10, chemins de la v4, vérification 2), entrée « Vérification 2 », version qui va à Lazar. Conforme.

## 4. Aucun chiffre du calcul ; aucune recette

- **Nombres neufs** (`sortie-nombres-neufs-v3-v4.json`) : 88,36 et 87,7701, cités des registres, et une heure. Le devis dit que 88,36 USD n'entre dans aucun total : c'est juste. Ligne 450, plafond 456, attendu 218,72 et cas haut 419,43 sont inchangés, et le calcul v6 n'est pas touché.
- **Relevé « aucune recette »** (`sortie-releve-aucune-recette-v4.json`) : il ne relève aucune valeur d'axe entière, aucune marque de recette, aucun identifiant de modèle. Ses seuls signaux sont ceux, expliqués, des vérifications 1 et 2 : un nom de fichier, le gabarit de S15, les noms de maison dans les citations. **Conforme.**

## 5. Les écarts du rapport

Le rapport en annonce six et en numérote sept.

1. **Premier jet du devis v10 écarté et gardé hors du rendu** : juste ; il n'est pas une pièce.
2. **88,36 USD, chiffre neuf hors calcul** : vérifié sur GO-2026-11-20-26, montant exact. Ce que GO-2026-11-20-26 accorde, c'est l'étage 2 entier. La réserve posée sur la seule clé Luc est donc une borne prudente, ce que R-4293 dit (« borne sûre ») ; je ne la juge pas.
3. **« Proposé » dans la phrase de version de la v3** : histoire ; juste.
4. **« Devis v8 » et « devis v9 » non récrits** : la règle de lecture de la v4 et la table les couvrent, comme à la v3. Acceptable.
5. **Copie de travail à `…/additif-1-v4/`** : c'est là que les pièces sont versées ; juste.
6. **Date des pièces = heure du journal de la première passe** : déclaré ; acceptable, car la seconde passe a son heure à son journal (14:27:07Z et 14:26:28Z).
7. **Ancres comptées par l'outil** : j'ai compté les miennes par `grep -c -F -e`.

## 6. Corrections

Les textes exacts sont dans `corrections-verification-additif-1-v4-v1.json` (2 remplacements) et `corrections-verification-devis-v10-v1.json` (1 remplacement). Chaque ancre est comptée une fois par `grep -c -F -e`. Les essais par l'outil donnent `3682b3c2…` et `e869d183…`.

X1 — additif, § 6, la part de Luc.

    Ancien : étage 2, 88,36 USD, le plafond de son accord, borne sûre ; les 87,7701 USD qu'écrivait R-4289 sont le pire de l'étage 2 entier, ses deux juges, et non la réserve)
    Neuf : étage 2, 88,36 USD, le plafond de son accord, GO-2026-11-20-26, borne sûre ; les 87,7701 USD qu'écrivait R-4289 sont, à la lettre de R-4293, « le pire de l'étage 2 entier, les deux juges, et non la seule part de Luc »)

X2 — additif, § 2, chapeau du sens des conditions.

    Ancien : (décision de 13:45Z, inscrite au registre des décisions : R-4288, R-4289 et, pour les points e et i, mot pour mot, R-4294 ; écrite ici dans les mots du rédacteur).
    Neuf : (décision de 13:45Z, précisée pour les points e et i par le message de 13:58Z ; inscrite au registre des décisions : R-4288, R-4289 et, pour les points e et i, mot pour mot, R-4294 ; écrite ici dans les mots du rédacteur).

Y1 — devis, § 10.6, la part de Luc.

    Ancien : (étage 2 : 88,36 USD, le plafond de son accord, borne sûre, R-4293 ; les 87,7701 USD qu'écrivait R-4289 sont le pire de l'étage 2 entier, ses deux juges, et non la réserve)
    Neuf : (étage 2 : 88,36 USD, le plafond de son accord, GO-2026-11-20-26, borne sûre, R-4293 ; les 87,7701 USD qu'écrivait R-4289 sont, à la lettre de R-4293, « le pire de l'étage 2 entier, les deux juges, et non la seule part de Luc »)

## 7. Points pour la mère

1. **Réserve sur Luc et juge de l'étage 2 chez l'autre fournisseur.** La réserve de 88,36 USD couvre l'étage 2 entier. Or GO-2026-11-20-64 compte déjà le juge de cet étage payé par le deuxième relais (15,41 USD) dans les appels accordés à ce compte. La borne est donc prudente des deux côtés. Rien n'est à corriger ; c'est à savoir au complément.
2. **Marge de Luc.** Sur un reste relu de 214 USD, une réserve de 88,36 USD laisse 125,64 USD, pour un cas haut de 124,35 USD : la marge n'est que de 1,29 USD. Si le reste relu est plus bas, le nœud de Lazar prévu par R-4289 se déclenche.

## 8. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-1-v9/`. Chacun a son compagnon `.sha256` :
- `verification-additif-1-v4-devis-v10-v1.md` (cette pièce) ;
- `corrections-verification-additif-1-v4-v1.json` ; `corrections-verification-devis-v10-v1.json` ;
- `sortie-nombres-neufs-v3-v4.json` ; `sortie-releve-aucune-recette-v4.json`.

Le registre des décisions au commit cité a été tiré par `git show 37a43501…:registres/decisions.md > fichier` ; ce commit est `origin/main` à l'heure de la vérification.

— contre-lecteur neuf, modèle O
