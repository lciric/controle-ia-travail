# Vérification des corrections — additif 1 v2 au préenregistrement court v9 et devis v8 — v1

Pièce de travail (classe C), 2026-11-20, relevé de `date -u` : 14:12:52Z, après les rejeux et les relevés, avant l'écriture. Je suis le contre-lecteur neuf, modèle O, auteur de la contre-lecture `6ffbd3bc…`. Le mandat `799b14c6…` vaut toujours, en-tête compris. Demande de la session de l'organisme : vérifier comme lettre les décisions de la mère, sans les juger. Processeur seul : aucun appel à un fournisseur, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Rien n'est écrit ici d'une méthode d'attaque, d'un procédé, d'un nom ou d'un énoncé de mode, d'une case nommée, d'une valeur de clé ni d'un identifiant de modèle. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**À corriger.** Six corrections : quatre sur l'additif (V1 à V4), deux sur le devis (W1, W2). Toutes sont de lettre ou de renvoi, et aucune ne change un chiffre, un tirage ni une décision de la mère. Ce qui est vérifié :
- les deux passes rejouent à l'octet ;
- chaque correction A1 à A15 et D1 à D5 est portée ou récrite comme le rapport le dit ;
- aucun chiffre ne change, et le calcul v6 est inchangé ;
- le relevé « aucune recette » est conforme.

V2, W1 et W2 comblent un trou neuf, né de GO-2026-11-20-64. La part du deuxième relais est fixée à son cas haut (140,39 USD), « tenue par l'arrêt nommé de la course ». Or l'arrêt nommé, le n° 12, ne vaut à la lettre que pour les clés du premier relais. De plus, l'arrêt n° 11 compare un reste lu (60,92 EUR) à la part (140,39 USD) : à la lettre, il refuserait le départ.

## 1. Pièces et empreintes

| pièce | empreinte | vérification |
|---|---|---|
| additif 1 v2 | `ed73f647471297af1c16e1dbb2dce8702dc07882d47fdc8350f5cb9e0dad8610` | compagnon « OK » ; rejeu égal (`cmp`) |
| devis v8 | `4a9fc6b42ab7be53034839e3778c355a8558347a51fcfb5ddc9044e7492ca13d` | compagnon « OK » ; rejeu égal (`cmp`) |
| étape 1 de l'additif | `728102d4…` | `cmp` égal à mon essai du jeu A1 à A15 |
| étape 1 du devis | `5c73949c…` | `cmp` égal à mon essai du jeu D1 à D5 |
| jeux de la seconde passe | `fa5de560…` ; `3ea70827…` | compagnons « OK » |
| différentiels | `5faa2223…` ; `01db5d01…` | compagnons « OK » |
| rapport du rédacteur | `c080a9a239fea45b8b80a64f2896f837e02266a0852bbccb14c96998047c17b6` | compagnon « OK » |
| mandat du rédacteur v2 | `9b1e92db…6156` | recalculée |
| contre-lecture, au chemin versé | `6ffbd3bc…` | recalculée |
| calcul v6 et sa sortie | `b622bca0…` ; `096597df…` | compagnons « OK », inchangés |
| registres au commit `b941e0c8` | `766a63e7…` ; `3c8fc58a…` | recalculées ; GO-2026-11-20-63, -64, R-4281 à R-4286 lus ; R-4287 lu sur `origin/main` (`3bd027df`) |

## 2. Rejeux

- Seconde passe de l'additif : mon essai (`728102d4…`) avec le jeu `fa5de560…` donne 21 remplacements, soit `ed73f647…`, égal à l'additif v2.
- Seconde passe du devis : mon essai (`5c73949c…`) avec le jeu `3ea70827…` donne 12 remplacements, soit `4a9fc6b4…`, égal au devis v8.

## 3. Les corrections de la contre-lecture

| correction | état dans la v2 / la v8 |
|---|---|
| A1 à A5, A7, A9 à A15 | portées telles quelles. A5 a ensuite « devis v8 » pour « devis v7 », comme la tenue le veut |
| A6 | portée, puis sa fin récrite sur la lecture de la mère de 14:01Z : lettre fidèle à R-4287 (« GO-60 ne lève pas « rien ne court avant le mot sur le devis neuf », le devis v8 ira à Lazar ») |
| A8 | portée, puis complétée par la décision de la mère (14:01Z) : écrite comme sa décision |
| A9, A10 | portées sans marque, dites acceptées (R-4287) |
| A11 à A13 | portées dans le § 4, gardé comme histoire ; voir V1 |
| D1 à D5 | portées ; D1 et D5 récrits à leur fin, sur la décision de 14:01Z et sur GO-2026-11-20-64 : lettre fidèle |

## 4. Textes neufs, vérifiés comme lettre

- **Mot de Lazar sur le devis neuf** (additif § 0 point 7, § 6 lignes 171 et 412 ; devis en tête, statut, § 10.8). La lettre (GO-2026-11-20-33, v9 lignes 7 et 412, silence de GO-2026-11-20-60) est écrite à côté de la lecture de la mère, comme demandé. Le devis demande une ligne de calcul de 450 USD, plafond total 456 USD. Conforme.
- **GO-2026-11-20-63** : cité exactement, avec ses coupures marquées. « Aucun écart au garde-fou 6 » (§ 0, § 3) : conforme ; le point 1 de ma contre-lecture est sans objet. Ce qui reste de GO-2026-11-20-61 (devis § 10.6) : juste à la lettre (remplacé par -62, puis son objet annulé par -63 ; la recharge d'environ 5 USD redite par -63).
- **GO-2026-11-20-64** : cité exactement, deux désignations de modèle remplacées par « […] ». Le trou est expliqué au § 0 et corrigé par V2, W1 et W2.
- **Sens des trois conditions, points a à i** : fidèle, point par point, au mandat du rédacteur v2 (§ 2, points a à i). Les ajouts sont marqués « recommandation du rédacteur » ou sont des conséquences sans écart : « servies » au point a ; « c'est pourquoi » au point g ; « accepté et déclaré » au point e.
- **N-054, ligne 60** : conforme à la décision de la mère.
- **§ 4 bis** : trois règles neuves, entrées sur la décision de 14:01Z. La première (sonde des espèces 1 à 5) reprend la lettre de la ligne 271 de la v9. Elle perd l'épreuve que la ligne 272 donnait (cas sain, artefact, R5) et ne porte pas de numéro d'arrêt (V4).
- **Chemins de versement** : écrits à la table de l'additif ; écart 5 de ma contre-lecture levé.

## 5. Aucun chiffre ne change

- Le programme `nombres_neufs_v1.py` (sortie `sortie-nombres-neufs-v1.json`) relève tous les nombres neufs de l'additif v1 → v2 et du devis v7 → v8, empreintes ôtées. Ce ne sont que :
  - des numéros de ligne, d'arrêt ou de clé (30) ;
  - des heures ;
  - 140,39 (cas haut du deuxième relais, déjà à la sortie du calcul v6) ;
  - 60,92 EUR, 164, 15,41 et 25,90 (cités de GO-2026-11-20-64 et R-4283) ;
  - les chiffres de D3 (sortie du calcul v6).
- Aucune ligne de course, aucun plafond, aucun seuil, aucun attendu ni aucun cas haut ne change.
- Le calcul v6 et sa sortie sont inchangés (compagnons « OK »).

## 6. Aucune recette

Le relevé, rejoué sur les pièces entières (`releve_aucune_recette_v2.py`, qui reprend le v1 ; sortie `sortie-releve-aucune-recette-v2.json`), rend aucune valeur d'axe entière, aucune marque de recette, aucun identifiant de modèle. Ses seuls signaux s'expliquent :
- Une forme « identifiant » n'est qu'un nom de fichier.
- La forme à trois valeurs du devis est le gabarit « valeur / valeur / valeur » de la source S15, déjà au devis v7.
- Les noms de maison ne sont que dans les accords cités (écart 7 du rapport).
- Le premier mot d'une valeur de l'axe des menaces est présent : c'est la décision de la mère (point a : « les seules cases … dont la menace est le sabotage ») et le terme de N-054 (« mode de sabotage »). Cela désigne une valeur d'un axe, non une case. Aucune case n'est nommée.

**Conforme.**

## 7. Les dix écarts du rapport

1. Deux passes : juste, et c'est ce qui rend la première vérifiable à l'octet.
2. **§ 4 non récrit.** Le chapeau ne neutralise que les phrases « bloque ». Deux autres phrases du § 4 restent contraires au § 2 :
   - silence 4 : « l'additif ne change pas la liste nominative » ;
   - silence 6 : « une seule est écrite ici ».

   Et la règle de primauté du § 2 (« il prime sur la table ci-dessus ») ne vise que la table des conditions. Il faut une phrase de primauté sur le § 4 entier (V1).
3. **Clé de tirage n° 30.** À la lettre, c'est un écart au texte scellé (ligne 311 : « Aucune autre méthode de tirage n'est permise »). GO-2026-11-20-59 dit « son choix scellé avant toute lecture », non « un tirage ». Aucun accord ne porte donc cette clé. Par la hiérarchie du dépôt (« écart à un préenregistrement scellé » : nœud), **c'est un écart à porter à Lazar**, en une ligne. L'additif le dit déclaré et laisse la mère décider de le porter ; il n'y a rien à corriger dans le texte.
4. Sonde des espèces 1 à 5 : sans écart de fond, mais sans épreuve (V4).
5. Copie de travail à `…/additif-1-v2/` : c'est là que les pièces sont versées ; juste.
6. L'empreinte de l'additif hors de sa table : juste ; le compagnon la porte.
7. Noms de maison dans les citations : admis, ce ne sont pas des identifiants de modèle.
8. **Crédit en euros non converti.** Sans effet sur les chiffres du devis, puisque la carte paie au-delà. Mais l'arrêt n° 11 (« reste du jour … lu pour les autres relais ») comparerait 60,92 EUR à une part de 140,39 USD et refuserait le départ. La manière de lire le reste d'un compte payant, et sa monnaie, doivent s'écrire au complément (V2, W2).
9. Errata, ordre et N-054 non relus : sans suite, car rien de leur lettre n'est neuf dans la v2.
10. Ancres comptées par l'outil : je les ai aussi comptées par `grep -c -F -e` pour mes six corrections.

**Cinquième entrée de la liste nominative.** GO-2026-11-20-57, point 2, est un mot de Lazar qui nomme quatre entrées. En ajouter une change sa décision. GO-2026-11-20-59 accepte une instance qui doit recevoir la carte, mais ne l'inscrit pas. **C'est un écart à porter à Lazar**, en une ligne, avec la clé n° 30.

## 8. Corrections

Le texte exact fait foi dans les deux jeux JSON. Chaque ancre est comptée une fois par `grep -c -F -e`. Les deux jeux passent l'outil sur des copies : 4 remplacements donnent `d94146a7…`, 2 remplacements donnent `09142834…`. Ce sont des essais seulement.

**Sur l'additif v2** (`corrections-verification-additif-1-v2-v1.json`) :

V1 — § 4, chapeau.

    Ancien : Là où une phrase de cette liste dit qu'un silence bloque (silences 3 et 4), il ne bloque plus.
    Neuf : La liste n'a plus valeur de règle : là où une de ses phrases diffère du § 2, le § 2 prime ; ainsi les silences 3 et 4 ne bloquent plus, l'additif change la liste nominative (silence 4 ; § 2, point d), et la carte peut être une ou plusieurs (silence 6 ; § 2, point f).

V2 — § 7, deuxième relais : quel arrêt tient la part ; l'arrêt n° 11 face au crédit en euros.

    Ancien : Au complément de valeurs, la part du deuxième relais est son cas haut à cinq espèces, 140,39 USD, tenue par l'arrêt nommé de la course ;
    Neuf : Au complément de valeurs, la part du deuxième relais est son cas haut à cinq espèces, 140,39 USD, tenue par l'arrêt nommé de la course, l'arrêt n° 12 (« part d'une clé épuisée »), dont l'extension à cette clé se déclare au complément de valeurs, comme pour le troisième relais ; l'arrêt n° 11 compare le reste du jour lu à la part, et le crédit relevé (60,92 EUR) est plus bas que 140,39 USD : la manière dont il lit le reste d'un compte payant (crédit et engagement de la carte, GO-2026-11-20-64), et en quelle monnaie, s'écrit au même complément, faute de quoi il refuse le départ ;

V3 — § 6, ligne 383 (arrêt n° 12).

    Ancien : son extension à la clé du troisième relais n'est pas écrite ici : elle se déclare au complément de valeurs (§ 7) |
    Neuf : son extension aux clés du deuxième et du troisième relais n'est pas écrite ici : elle se déclare au complément de valeurs (§ 7) |

V4 — § 4 bis, point 1 : l'épreuve de la règle neuve.

    Ancien : C'est la lettre du paragraphe retiré (ligne 271), étendue aux cinq espèces ;
    Neuf : C'est la lettre du paragraphe retiré (ligne 271), étendue aux cinq espèces ; comme lui (ligne 272), elle est éprouvée avant la course sur un cas sain (réponse lisible : l'issue est lue) et sur des artefacts (refus pour crédit simulé par le faux fournisseur, puis réponse illisible : départ refusé, consigné), règle R5 ;

**Sur le devis v8** (`corrections-verification-devis-v8-v1.json`) :

W1 — § 10.6, ligne du deuxième relais.

    Ancien : | au-delà de sa part, l'arrêt nommé de la course tient la dépense |
    Neuf : | au-delà de sa part, l'arrêt nommé de la course, n° 12, étendu à cette clé par le complément de valeurs, tient la dépense |

W2 — § 10.6, paragraphe du deuxième relais.

    Ancien : écrite au complément de valeurs et tenue par l'arrêt nommé de la course (R-4284) ;
    Neuf : écrite au complément de valeurs et tenue par l'arrêt nommé de la course (R-4284), l'arrêt n° 12 du préenregistrement court v9, étendu à cette clé par le même complément, comme pour le troisième relais ; l'arrêt n° 11, qui compare le reste lu à la part, demande au complément la manière de lire le reste d'un compte payant ;

## 9. Points pour la mère

1. **À porter à Lazar**, en une ligne chacun : la clé de tirage n° 30 (écart à la ligne 311 du texte scellé) et la cinquième entrée de la liste nominative (écart à GO-2026-11-20-57, point 2).
2. **Décisions non inscrites.** Les décisions de 13:45Z (sens des conditions, a à i), de 13:50Z et celle de 14:01Z sur N-054 et sur les silences en plus sont citées par l'additif. Le registre des décisions ne les porte pas : R-4287 n'inscrit que A9, A10 et la lecture de GO-2026-11-20-60. Les inscrire avant le scellement, pour qu'elles soient citables.
3. **Le complément de valeurs v2** portera ce que V2, V3, W1 et W2 lui renvoient :
   - l'extension de l'arrêt n° 12 aux clés des deuxième et troisième relais ;
   - la lecture du reste d'un compte payant pour l'arrêt n° 11, et sa monnaie ;
   - la recharge du troisième relais.
4. La règle du § 4 bis, point 1, n'a pas de numéro d'arrêt. Si la mère veut qu'elle soit à la liste d'arrêt comme les n° 24 à 26, il faut un n° 27.

## 10. Écarts du vérificateur

- E1. J'ai tiré les registres par `git show b941e0c8…:chemin > fichier`, soit le commit cité par l'additif, ancêtre de `origin/main`, et non `origin/main` lui-même. R-4287 vient de `origin/main` (`3bd027df`).
- E2. Le relevé v2 charge le module du relevé v1, de mon dossier, par son chemin.
- E3. Les essais de l'outil ont écrit, dans mon dossier, des copies et leurs journaux : ce sont des essais, non des pièces.

## 11. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-1-v9/`. Chacun a son compagnon `.sha256` :
- `verification-additif-1-v2-devis-v8-v1.md` (cette pièce) ;
- `corrections-verification-additif-1-v2-v1.json` ; `corrections-verification-devis-v8-v1.json` ;
- `nombres_neufs_v1.py` et sa sortie ; `releve_aucune_recette_v2.py` et sa sortie.

— contre-lecteur neuf, modèle O
