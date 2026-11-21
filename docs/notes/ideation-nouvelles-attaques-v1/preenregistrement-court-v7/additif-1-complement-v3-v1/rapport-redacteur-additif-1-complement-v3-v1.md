# Rapport du rédacteur — additif 1 au complément de valeurs v3 (espèce 3 sur la clé Minuit) — v1

Rédacteur de l'additif 1 au complément v3, modèle F. Date (UTC) : 2026-11-21, relevé de `date -u` à 06:01:16Z avant l'écriture. Rien n'est scellé ; rien n'est écrit dans le dépôt ; aucun commit ; aucun appel à un fournisseur ; aucune clé lue ; aucune dépense. Version de Python : 3.13.18.

## 1. Pièces lues

Mandat, vérifié contre son compagnon : `cf13427bd91e551d2842421c15e450949d39bb290964d72be4d3d296a2262f1f`.

Lues sur `origin/main`, commit `7487d27327e215168d4cb3493e2f5fbb6911f48b`, chacune tirée par `git show` redirigé vers le dossier :

| pièce | copie de lecture | empreinte | compagnon |
|---|---|---|---|
| complément de valeurs v3 | `lecture-complement-valeurs-v3.md` | `b4ef87dc6d5cce138f76457771c4cff18b84dfde662916841fc6386d77e202b2` | égale (`lecture-complement-valeurs-v3-compagnon-origine.txt`) |
| devis v11 | `lecture-devis-v11.md` | `205e08f23ef9ced92a35340b8fad38765b08483a2129ee32550081d1bd043570` | égale (`lecture-devis-v11-compagnon-origine.txt`) |
| `registres/go.md` | `lecture-go-origin-main.md` | `44dabda66c19bbda667ef904e5a3bca9bd2e5f771fb4c0f3aea7affbd87ab1d1` | non tiré |
| `registres/decisions.md` | `lecture-registre-origin-main.md` | `0f01e3d76d29eb474fb59f671da7aea1bea0da3fb813a2ca6af705d804a7be2e` | non tiré |

Lu en entier : le complément v3. Lu par parties : le devis v11 (§ 10.2 à § 10.8, lignes 380 à 461) ; `registres/go.md` (lignes 545 à 601) ; `registres/decisions.md` (lignes 4440 à 4482).

## 2. Nombres et sources

| nombre | valeur (USD) | source |
|---|---|---|
| reste de Minuit | 162,56 | complément v3, ligne 109 ; GO-2026-11-20-16 |
| part de Minuit | 156,56 | complément v3, ligne 105 ; R-4306 |
| juge de l'espèce 3, bas et haut | 20,58 ; 105,05 | complément v3, ligne 105 ; devis v11, ligne 405 |
| proposeur de l'espèce 3, bas et haut | 22,29 ; 26,61 | complément v3, ligne 107 ; devis v11, ligne 407 |
| **haut des deux rôles de Minuit** | **131,66** | JSON : `minuit.haut_des_deux_roles_usd` |
| bas des deux rôles de Minuit | 42,87 | JSON : `minuit.bas_des_deux_roles_usd` |
| **marge de Minuit** | **24,90** | JSON : `minuit.marge_part_moins_haut_des_deux_roles_usd` |
| marge au complément v3 | 51,51 | JSON : `minuit.marge_au_complement_v3_un_seul_role_usd` |
| **reste après les lignes à part, au plafond** | **156,56** | JSON : `minuit.reste_apres_les_lignes_a_part_au_plafond_usd` |
| **au-delà du cas haut, après les lignes à part** | **24,90** | JSON : `minuit.surplus_apres_les_lignes_a_part_et_le_haut_usd` |
| reste minimal de Minuit pour le haut et les lignes | 137,66 | JSON : `minuit.reste_minimal_pour_tenir_haut_et_lignes_usd` |
| rapport part sur haut, tronqué | 1,189 | JSON : `minuit.rapport_part_sur_haut_des_deux_roles_tronque` |
| solde déclaré de Rigaud ; réserve | 25 ; 8,35 | R-4342 ; GO-2026-11-20-22 |
| Rigaud, au-delà de la réserve | 16,65 | JSON : `rigaud.solde_declare_moins_reserve_usd` |
| part du troisième relais | 17,01 | R-4342 ; complément v3, ligne 156 ; devis v11, ligne 397 |
| somme des quatre parts de la course | 439,59 | JSON : `ensemble.somme_des_parts_de_la_course_usd` |

Les neuf contrôles du programme sont tenus (`tous_les_controles_tenus` : vrai).

Remarque pour le contre-lecteur : la somme des cas hauts des rôles Claude, ligne à ligne, fait 256,01 USD (JSON : `ensemble.haut_des_roles_claude_somme_des_lignes_usd`) ; le devis v11 écrit 256,02 (ligne 408). L'écart d'un centime vient des arrondis du calcul v6, que ce programme ne rejoue pas ; l'additif ne cite ni l'un ni l'autre.

## 3. Points laissés à la mère

Ils sont au § 8 de l'additif :

1. Minuit sous sa part au jour du départ : version neuve ou nœud de Lazar.
2. Rigaud dans la pièce de relevés et dans le véhicule : part nulle ou clé hors de la course ; artefact de l'arrêt n° 12 sur Rigaud.
3. Les 16,65 USD de Rigaud au-delà de la réserve, que rien n'affecte.
4. Ce que l'attestation de recharge automatique du troisième relais doit dire, et qui la relève.
5. Troisième relais sans recharge automatique mais avec un reste relu d'au moins 17,01 USD.
6. Coût de la sonde de refus sur le troisième relais : rien retranché, par analogie seulement.
7. Confirmation de la répartition par la contre-lecture du véhicule : à refaire sur la répartition neuve.

## 4. Écarts et réserves du rédacteur

1. **« Les quatre GO »** : le mandat nomme cinq accords (GO-2026-11-20-16, -22, -55, -67 et GO-2026-11-21-02). J'ai cité les cinq à la lettre, et R-4342 et R-4343.
2. **Citations « à la lettre » avec retraits** : une désignation de modèle est remplacée par « […] » dans GO-2026-11-21-02 et dans R-4343 (une fois chacun), et une désignation est remplacée deux fois dans le point 2 de GO-2026-11-20-55, pour tenir « aucun identifiant de modèle ». GO-2026-11-20-55 n'est cité que pour son point 2, comme au complément v3. Chaque retrait est dit à l'endroit de la citation.
3. **La copie de `registres/go.md`** (`lecture-go-origin-main.md`) porte, comme celle du registre des décisions, des noms de modèle : à exclure du versement elle aussi. Le mandat ne nomme que la seconde.
4. **Table des lignes à part** : outre la ligne du proposeur de l'espèce 3, j'ai corrigé le libellé de la ligne du troisième relais (« compte payant ; attend le relevé de son statut »), conséquence du § 4. Le mandat ne demandait que la première.
5. **Clé `rigaud.part_de_la_course_apres_l_additif_usd` du JSON** : elle vaut 0,00 par construction ; l'additif ne s'en sert pas et laisse l'écriture de Rigaud à la mère (point 2).
6. **Commandes hors de celles que le mandat nomme**, toutes simples, sans liste : `mkdir -p` de mon dossier ; `git rev-parse origin/main` ; `date -u` ; `wc -l` sur quatre chemins complets ; `cat` de trois compagnons en un appel. Recherches de motifs : sur un fichier nommé à la fois, jamais sur un dossier.
7. **Sortie du programme non rejouée par moi** : jouée une fois, lue, non comparée à un second passage. Le contre-lecteur la rejoue.
8. **Pièces non lues** : le véhicule, le préenregistrement court v9, l'additif 1 à la v9, le registre des dépenses. Le reste de Minuit (162,56 USD) est celui du complément v3 ; je n'ai pas vérifié qu'aucune dépense n'est inscrite sur cette clé depuis.
9. Aucun refus de permission, de classifieur ou de garde.

— rédacteur de l'additif 1 au complément v3, modèle F
