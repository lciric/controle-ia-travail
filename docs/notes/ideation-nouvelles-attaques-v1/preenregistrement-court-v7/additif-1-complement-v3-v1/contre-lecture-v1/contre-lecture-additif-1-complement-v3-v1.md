# Contre-lecture de l'additif 1 au complément de valeurs v3 (l'espèce 3 passe sur la clé Minuit) — v1

- Contre-lecteur : neuf, modèle O. Je n'ai écrit aucune pièce de la course « nouvelles attaques ».
- Date (UTC) : 2026-11-21.
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune clé lue, aucune dépense, aucune écriture dans un dépôt, aucun commit. Aucun refus de permission, de classifieur ou de garde.
- Version de Python : 3.13.18.

## Verdict

**À corriger.** Les nombres sont justes, le rejeu est identique à l'octet, les citations sont exactes et la répartition suit GO-2026-11-21-02. Dix remplacements dans l'additif, plus un dans le programme. Deux des sept points laissés à la mère (n° 1 et n° 6) se déduisent de la lettre et doivent être tranchés dans l'additif. Une phrase dit « transposée à la lettre » alors qu'elle laisse de côté un point et un motif. Trois libellés de la pièce de relevés laissent une ambiguïté. Le JSON porte une clé qui penche vers l'une des deux options du point n° 2. Une fois les deux jeux portés tels quels et l'égalité constatée par `cmp` avec mes essais : conforme, à sceller.

## Pièces lues

Dossier A = `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/`.

| pièce | empreinte recalculée | compagnon |
|---|---|---|
| A/mandat-redacteur-additif-1-complement-valeurs-v3-espece-3-sur-minuit-v1.md | `cf13427bd91e551d2842421c15e450949d39bb290964d72be4d3d296a2262f1f` | égale |
| A/additif-1-complement-v3-v1/additif-1-complement-valeurs-preenregistrement-court-v9-lot-1-v3-espece-3-sur-minuit-v1.md | `e5ec3a179b21a6d74d28730840a62e72a558cc80b1d7c5a8cf7aa9513dc1556a` | égale |
| A/additif-1-complement-v3-v1/calcul_additif_1_complement_v3_v1.py | `d620b9814a45bbe291e769c65abef18e9cce77e3c269866d81abd8b12a85be7e` | égale |
| A/additif-1-complement-v3-v1/calcul-additif-1-complement-v3-v1.json | `4b9734c70c32cc1f5f3ac816474cf56e35d501855b2a7a8bb0bf3d86b3a9f571` | égale |
| A/additif-1-complement-v3-v1/rapport-redacteur-additif-1-complement-v3-v1.md | `5798873ffdc12b0709a12ecf227be17b0b328ce84b8f074d7d3f007e739ab626` | égale |
| complément de valeurs v3, `git show origin/main:` | `b4ef87dc6d5cce138f76457771c4cff18b84dfde662916841fc6386d77e202b2` | égale (compagnon tiré par `git show`) |
| devis v11, `git show origin/main:` | `205e08f23ef9ced92a35340b8fad38765b08483a2129ee32550081d1bd043570` | égale (compagnon tiré par `git show`) |
| `registres/go.md`, `origin/main` en `741c79af734e128090299ebae0c012b1d73b4441` | `98d0905c3f38edb179a1d030d84f3712eaf169f37c562a778bf9e0f9a1f259cf` | sans compagnon |
| `registres/decisions.md`, même commit | `c768ba39fb8b68dc6cd517d716aaa1c3bb9bb742a83c4a50612818aaac2764be` | sans compagnon |
| `registres/depenses.md`, même commit | `e635cc299f64899c54e5618af9974a8b693e1e621ea52d5c17a8c32d902cdb04` | sans compagnon |

**Réserve, la table d'empreintes du dossier : non vérifiée.** Son nom n'est donné ni par le mandat, ni par le rapport, ni dans ma consigne, et l'en-tête interdit toute liste. J'ai essayé cinq noms ; tous sont absents. Les cinq pièces ci-dessus sont vérifiées chacune contre son compagnon.

Les registres sont lus sur un `origin/main` plus récent que celui du rédacteur (`7487d273…`, qui en est un ancêtre, constaté par `git merge-base --is-ancestor`). Les entrées citées n'ont pas changé. Après R-4343 et GO-2026-11-21-02, rien au registre ne touche cette course : R-4344 à R-4350 et GO-2026-11-21-03 à -07 portent sur d'autres chantiers. Je n'ai pas recalculé les empreintes des registres que l'additif donne (`44dabda6…`, `0f01e3d7…`) : il faudrait un `git show` sur un autre commit que `origin/main`.

## 1. Le programme de calcul

- **Rejeu.** `python3 -B` sur le programme versé, sortie redirigée vers `rejeu-calcul-additif-1-complement-v3-v1.json` (`4b9734c7…`). `cmp` contre la sortie versée : **aucune différence**.
- **De l'arithmétique seule.** Aucune lecture de fichier, aucun appel, aucun aléa. Calcul en centièmes entiers, division entière seulement pour le rapport tronqué et le nombre d'appels entiers. Conforme au mandat.
- **Chaque entrée est égale à sa source**, vérifiée ligne par ligne :
  - reste de Minuit 162,56 : complément v3, ligne 109 ; GO-2026-11-20-16.
  - plafonds 5 et 1 : complément v3, ligne 120 ; devis v11, lignes 381 et 382.
  - part de Minuit 156,56 : complément v3, ligne 105 ; R-4306.
  - juge de l'espèce 3, 20,58 et 105,05 : complément v3, ligne 105 ; devis v11, ligne 405.
  - proposeur de l'espèce 3, 22,29 et 26,61 : complément v3, ligne 107 ; devis v11, ligne 407.
  - pire d'un appel de proposeur 6,05 : complément v3, lignes 83 et 166.
  - Rigaud 25 : R-4342 ; GO-2026-11-21-02.
  - réserve 8,35 : GO-2026-11-20-22 ; complément v3, ligne 118.
  - troisième relais, 14,25 et 17,01 : complément v3, ligne 156 ; devis v11, ligne 397 ; R-4342.
  - Luc, part 125,63 et cas haut 124,35 : complément v3, ligne 106 ; devis v11, ligne 406.
  - deuxième relais 140,39 : complément v3, ligne 138.
  - plafond total 456 : GO-2026-11-20-67 ; devis v11, ligne 386.
- **Les contrôles sont justes**, et tous les neuf sont tenus. Trois remarques, sans correction :
  - `troisieme_relais_part_egale_son_haut` ne peut pas échouer, puisque la part est posée égale au cas haut.
  - `minuit_reste_apres_lignes_au_moins_egal_a_la_part` refait le premier contrôle, puisque le reste après les lignes est le même nombre que la part recalculée.
  - Les deux contrôles sur les lignes à part vérifient une liste écrite par l'auteur.
  
  L'additif n'en tire rien de plus que ce qu'ils montrent.
- **Les clés que l'additif n'emploie pas.**
  - `ensemble.haut_des_roles_claude_somme_des_lignes_usd` (256,01, contre 256,02 au devis, ligne 408, par les arrondis du calcul v6) : déclarée au rapport, sans effet.
  - `rigaud.part_de_la_course_apres_l_additif_usd` = « 0.00 » : voir § 4.

## 2. Les nombres de l'additif

Tous sont égaux au JSON et à leurs sources.
- Minuit : 156,56 ≥ 105,05 + 26,61 = 131,66, marge 24,90. Cas bas 42,87. Ancienne marge 51,51, qui baisse de 26,61. Rapport 1,189. Quatre pires appels de proposeur.
- Reste après les lignes à part, au plafond : 156,56, soit 24,90 au-delà du cas haut. Reste minimal 137,66.
- Rigaud : 25 ; réserve 8,35, couverte ; 16,65 au-delà de la réserve ; manque de l'ancienne part 9,96 ; ancien minimum 34,96 ; aucun rôle.
- Troisième relais : 17,01.
- Somme des parts : 15 656 + 12 563 + 14 039 + 1 701 = 43 959 centièmes, soit 439,59, sous 456.
- Cas bas et haut : complément v3, lignes 105 et 107 ; devis v11, lignes 405 et 407. Lignes exactes.

## 3. Fidélité

- **Citations « à la lettre ».** GO-2026-11-20-16, -22, -55 (point 2), -67 (avec le montant et l'échéance), GO-2026-11-21-02 (avec la source du mot de Lazar), R-4342 et R-4343 : chacune est identique au registre, au caractère près. Les retraits sont dits sur place : une désignation de modèle dans GO-2026-11-21-02 et une dans R-4343 ; une désignation remplacée deux fois dans GO-2026-11-20-55. Conforme.
- **La répartition** suit GO-2026-11-21-02 :
  - le proposeur de l'espèce 3 est sur Minuit ;
  - la part de 156,56 couvre environ 131,66 ;
  - Rigaud ne garde que la réserve de 8,35 ;
  - le troisième relais a sa part au cas haut.
- **Le troisième relais.** Il est traité comme compte payant au sens de R-4303, sa part étant fixée au cas haut, 17,01 (R-4342), et écrite dans la pièce de relevés. Conforme, à un défaut près. L'additif dit la règle du complément v3, § 4, « transposée à la lettre ». Or il laisse de côté son point 1, que R-4303 écrit à la lettre (« sans conversion de monnaie »). Et il garde le refus du point 4 sans son motif (« le reste n'est lisible qu'en euros »), qui ne vaut pas pour un compte tenu en dollars. → **correction C3.**
- **La sonde de refus de l'espèce 3** passe de Rigaud à Minuit. Le plafond de 6 USD est déjà retranché et couvre les plafonds entiers des deux lignes, tous rôles compris. Conforme, et dans la ligne 5 de la table « Valeurs ouvertes » du complément v3 (« les rôles Claude sur Minuit »). Les lignes à part restent hors de l'artefact de l'arrêt n° 12 (R-4306).

## 4. Ce que le mandat demande

Les points 1 à 7 sont tous portés. Le mandat nomme « quatre GO » pour cinq accords ; le rédacteur a cité les cinq. C'est juste.
- **Le libellé corrigé de la ligne du troisième relais** dans la table des lignes à part : l'ajout est **admis**. Laisser « attend le relevé de Lazar » contredirait le § 4 de l'additif et R-4342. L'ajout ne change aucun nombre et est couvert par l'écart déclaré du § 7 (« pour les lignes dites aux § 2 et § 5 »).
- **La clé `rigaud.part_de_la_course_apres_l_additif_usd` = 0,00** : à **retirer**. Ce n'est ni une entrée ni un calcul, c'est une constante écrite par l'auteur. Elle figure dans une pièce versée l'une des deux options du point pour la mère n° 2 (« part écrite nulle, ou clé hors de la course »), que l'additif s'interdit de trancher. Aucun nombre de l'additif n'en dépend. → **correction P1**, sur le programme, puis nouveau rejeu.

## 5. Les lignes de la pièce de relevés

Les cinq clés y sont. Chaque ligne porte un libellé fixe, avec le reste ou le statut, la date, la source, la part en dollars et l'arrêt qui la lit. Les valeurs déjà connues et ce qui reste à relever sont séparés. Trois ambiguïtés empêchent la mère d'écrire sans juger :
- **Minuit.** Le libellé ne dit pas si [RESTE] se prend avant ou après le coût des lignes à part ; seule la colonne voisine le dit. → **correction C6.**
- **Le deuxième et le troisième relais.** [STATUT] n'a pas de valeurs fixées, alors que l'arrêt n° 11 refuse le départ selon cette valeur. → **corrections C7 et C8.**
- R-4306 veut la pièce « calculée par programme, constatée par cmp » ; l'additif ne garde que la première moitié. → **correction C5.**

Restent, par construction, deux dépendances signalées : [PART] de Rigaud attend le point n° 2 ; la ligne du troisième relais attend le point n° 4 (ce que l'attestation doit dire). Une fois ces deux points tranchés et les corrections portées, les lignes suffisent.

## 6. Les sept points laissés à la mère

- **N° 1, Minuit sous sa part : se déduit de la lettre.**
  - Le départ est refusé (texte scellé, cité au complément v3, § 1).
  - Une part changée est une version neuve (v9, section « Seuil », citée en tête du complément v3).
  - Un écart à une pièce scellée est un nœud (hiérarchie de décision du dépôt).
  - C'est la voie que le complément v3 écrit pour Rigaud (ligne 118 : « version neuve, sur le mot de Lazar ») et que R-4342 a suivie.
  
  L'alternative posée (« version neuve, ou nœud ») est fausse : les deux vont ensemble. → **corrections C1, C2 et C9.**
- **N° 6, coût de la sonde sur le troisième relais : se déduit de la lettre.** La ligne 5 de la table « Valeurs ouvertes » du complément v3 fixe que les lignes à part retranchent « rien d'avance des autres parts ». La phrase du complément v3 sur le « reste relu moins le coût de la sonde » visait une part lue sur un reste, ce qui n'est plus le cas (§ 4 de l'additif). Il n'y a pas besoin d'analogie. → **corrections C4 et C10.**
- **N° 2, n° 4 et n° 7 : bien laissés à la mère.** Le n° 7 est un rappel, non une décision.
- **N° 3, les 16,65 USD de Rigaud** : hors de la course, aucune décision n'est nécessaire pour son départ. Je laisse le point comme information.
- **N° 5, le troisième relais sans recharge automatique mais avec un reste d'au moins 17,01** : bien laissé ouvert, et C3 rend le § 4 cohérent avec ce point. Ma lecture, pour la mère et sans l'imposer : le refus du complément v3 tenait à un reste lisible seulement en euros. Pour un compte tenu en dollars, la règle de base de l'arrêt n° 11 (« un reste du jour plus bas que sa part refuse le départ ») peut lire un reste relu et daté contre 17,01. Je recommande cette lecture, confiance moyenne.
- **Point manquant** : aucun qui bloque.

**Le reste de Minuit contre le registre des dépenses** (`origin/main`, `e635cc29…`, 570 lignes) : **aucune dépense sur Minuit depuis le complément v3.** Les seules lignes sur cette clé datent du 2026-11-19 : 0,000108 (ligne 528), 0,980399 (ligne 532) et 36,457056 (ligne 536). 200 − 37,437563 = 162,562437, soit les 162,56 du complément v3. Depuis : aucune dépense neuve sur Luc après les 0,000002 (ligne 548). Sur Rigaud, le collisionneur « dopamine » a dépensé 10,35 USD à 14:52Z le 2026-11-20 (ligne 563), avant le solde déclaré de 25 USD. Le reste (lignes 549 à 570) concerne le loueur de machines de la formation.

## Corrections

Les deux jeux sont à porter tels quels, par `python3 -B /home/user/controle-ia-travail-organisme/scripts/remplacer_texte_exact_v1.py`. Chaque ancre est comptée par `grep -c -F -e` sur la pièce versée : 1 pour chacune.

**Jeu de l'additif** : `corrections-additif-1-complement-v3-v2.json` (`9d67cc4b7822bda19e42d717708623a9de3f1db03b831659eb6c6323365344fb`), dix remplacements, dans l'ordre du fichier :

| n° | où | quoi |
|---|---|---|
| C9 | § 0 | « Sept points » devient « Cinq points […] ; deux autres, n° 1 et n° 6, se déduisent de la lettre et sont tranchés » |
| C1 | § 2 | le point n° 1 est tranché par la lettre, avec ses sources |
| C3 | § 4 | « transposée à la lettre » devient « transposée », avec le point 1 gardé et le motif du point 4 dit |
| C4 | § 5 | le point n° 6 est tranché par la ligne 5 de la table « Valeurs ouvertes » |
| C5 | § 6 | « constatée par `cmp` » (R-4306) |
| C6 | § 6 | libellé de Minuit : « après le coût inscrit des deux lignes à part » |
| C7 | § 6 | libellé du deuxième relais : [STATUT : payant, ou non payant] |
| C8 | § 6 | libellé du troisième relais : [STATUT : recharge automatique, ou sans recharge automatique] |
| C2 | § 8, n° 1 | rappel : tranché par la lettre, rien à décider |
| C10 | § 8, n° 6 | rappel : tranché par la lettre, rien à décider |

Essai sur une copie (`copie-additif-v1.md`, égale à `e5ec3a17…`) : `essai-additif-corrige-v2.md`, **`1c8cae2b733199e364baef4386d37412a9a11a41ffcf5f41b12842a3c853a1ee`**, avec son compagnon et le journal de l'outil. Le premier jeu, `corrections-additif-1-complement-v3-v1.json`, est remplacé par la v2, qui ajoute à C1 la source de la règle du nœud ; son essai `essai-additif-corrige.md` (`ec8d6e16…`) ne vaut pas.

**Jeu du programme** : `corrections-calcul-additif-1-complement-v3-v2.json` (`a4b7b1b75f178e47d24293663e15d9a8cb68737e4f82a68554725106902a8378`), un retrait : la ligne `"part_de_la_course_apres_l_additif_usd": usd(0),`. Essai sur une copie (`copie_calcul_v1.py`, égale à `d620b981…`) : `essai_calcul_corrige.py`, `9175f7960a98ca1f15d9722f51b9f94736d68231ce9728b4b0a306363843e133`. Sa sortie, `essai-calcul-corrige.json`, **`61ec2db091d98494e93ccd60e6f395f7f11d9cebaafedf49e04b4648b69a5c01`**, ne diffère de la sortie versée que par cette clé (`diff` : une ligne retirée), et ses neuf contrôles restent tenus. Le jeu v1 du programme a été refusé par l'outil (texte neuf contenu dans l'ancien) ; il ne vaut pas.

Après les deux jeux, l'additif garde ses renvois au JSON ; aucun ne vise la clé retirée. Le rapport du rédacteur (§ 3, § 4 point 5) reste tel quel : c'est une pièce de travail. La table d'empreintes du dossier est à refaire sur les fichiers neufs.

— contre-lecteur de l'additif 1 au complément v3, modèle O
