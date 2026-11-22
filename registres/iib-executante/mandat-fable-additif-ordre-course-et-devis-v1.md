# Mandat — rédacteur Fable : additif à l'ordre de la course et devis, voies (A) et (B) du saboteur à budget v5 — v1

Pièce de travail (classe C), écrite par l'exécutante v5 (session_01XJ6MgqUTEVCed6a2f6rWmC) sur la demande de la mère (session_01XJ6Mgr4LgbMsg5zLyRZCpG), le 2026-11-22 ; relecture de cloisonnement avant remise. Rédacteur : **Claude Fable 5.2** (pièces décisives : ordre de course, additif, devis). Contre-lecture ensuite par Opus 5.5, puis vérification des corrections par le même.

## 1. Ce que tu rédiges
Pour **chacune** des deux voies accordées par Lazar (« go C !!! », GO-2026-11-22-71, à lire au registre `registres/go.md` de `main` ; voies conduites en parallèle, la première qui réussit est retenue) :
1. **Un additif à l'ordre** (ou un ordre neuf si l'additif ne suffit pas, dis pourquoi), qui couvre l'étalonnage (rejoué ou repris) puis la course ;
2. **Un devis**, au format des devis scellés du programme (durées attendue, haute, pire ; coûts ; plafond ; coupure ; échéance ; liste d'arrêt ; réserves).
- **(A) code du tirage corrigé** (correctif 0020 : tirage des jetons sur l'appareil du modèle, chemin neuf choisi explicitement) : essai de vitesse court sur une carte (sans valeur de mesure), puis **étalonnage entier rejoué avec ce code**, puis la course avec le même code. Ligne proposée par la mère : 44 USD.
- **(B) ancien code** : le seul lot manquant de l'étalonnage (lot 28, 8 épisodes flagrants) joué sur une machine neuve par le correctif de reprise R001, assemblage des 28 lots et écriture de fin, puis la course répartie sur plusieurs cartes. Ligne proposée : 55 USD. L'écart au texte scellé (section 15 : « toute reprise est une course neuve ») est accepté par GO-2026-11-22-71 ; **la réserve « deux machines » (lots 1–27 sur 61875617, lot 28 sur la machine neuve ; déterminisme de la carte entre machines non garanti au bit près) est à écrire d'avance**.

## 2. Contraintes fixées (ne pas les rediscuter)
- Règles gelées de `CLAUDE.md` (R1 à R14), en particulier R1, R3, R4, R5, R9, R10, R12.
- Passage des conditions : **unique**, par programme ; aucun arrangement après coup.
- **Crédit chez le loueur : 12,995 USD le 22/11 à 14:11Z**, balance 0 : aucun devis ne peut partir sans recharge par Lazar ; écris pour chaque voie la dépense au-delà de ce crédit.
- Dernière création : aucune à partir du 2026-11-27T00:00:00Z (l'ordre scellé prime ; le devis s'y aligne).
- Machine 61875617 : à l'arrêt, disque gardé ; **tout redémarrage la détruit en environ 3 minutes** (amorce) : elle ne sert plus à rien qu'à la garde du disque.
- La référence d'engagement de la course part avant l'installation : toute fin anormale de l'amorce consomme la seule course permise sur cet étalonnage (contre-lecture du code, point 6).
- Aucune lecture des sorties avant la désignation scellée.
- Pour (A) : un étalonnage fait avec l'ancien code **ne vaut pas** pour une course jouée avec le nouveau (autre flux de hasard) : étalonnage et course sous le même chemin de tirage.

## 3. Pièces à lire (empreintes vérifiées le 2026-11-22 vers 14:15Z)
Sur `origin/claude/iib-reconception-oracle-v1` (lire par `git show <branche>:<chemin>`) :
| pièce | sha256 |
|---|---|
| `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-scellee-v1.md` (sections 9, 10.x, 13, 14, 15) | c1dc54597a1ab4b467331673607d986e46a706c06253bb40070e5d15caaa61f2 |
| `…-scellee-v1-erratum-1.md` | 2031baba173cad5cd410ea22d069b118d4ba04783013495388a6db0b53f15433 |
| `…-scellee-v1-erratum-2.md` | ab020d438cb6eaa46cd2df0a6ed76952b5dfb23497438e0f2b3fb4590b1d26e2 |
| `brouillons/ii-b-saboteur-budget-v5/devis-v5/devis-ii-b-v5-scelle-v1.md` | cb881522378ace662787a7097c2baa6d461c766d70782d28636c132ce09f3ee8 |
| `…/devis-v5/devis-ii-b-v5-scelle-v1-erratum-1.md` | 90342292f52daf2f7281acad68006598450033367d3a36aa1c6c72eac9150f9a |
| `brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/ordre-etalonnage-ii-b-v5-v2-brouillon3.md` | 3ec3a60523bbf45c0f345c91d5bdf8e20e9bb220b39a78efa93ea7c57420cc6f |
| `…/ordre-etalonnage-v5/additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon3.md` | a9d43d5921252b4d60152a4d7b48e4cab50633337b53fcbe3f9e9ee80f754b92 |

Sur `origin/claude/iib-executante-v5` :
| pièce | sha256 |
|---|---|
| `registres/essaim/vers-mere/executante-iib-v5-2026-11-22-1311-v27.md` (code de la course autorisable, points pour l'ordre) | 09ad5a56f4c36d23b3bc98191c37150b40b8714bc330ba1a602d4ca65cc7c751 |
| `registres/essaim/vers-mere/executante-iib-v5-2026-11-22-1330-v28.md` (relance, lots rapatriés) | 80e66250a504cec470fe4cf4907ea47b8b39b7ee17fac6edc94cd270735b4d7c |
| `registres/essaim/vers-mere/executante-iib-v5-2026-11-22-1332-v29.md` (voies vers la désignation) | 0ed5260d4f77a3940f9e74785cb602c6c18e8eca12335003ff1782920779551b |
| `registres/essaim/vers-mere/executante-iib-v5-2026-11-22-1340-v30.md` (diagnostic de vitesse) | 6b372cd231d5455e2df02aeb2725e78d001013e40c48dc347fd9a49fdaaab8ba |
| `registres/iib-executante/chiffres-devis-code-corrige-v1.md` (bases mesurées, chiffres) | 4e10a0047e1db340910bd9d41291a5210d787ad340876fd8649f91542963f710 |
| `registres/iib-executante/champs-ordre-course-remplis-par-E3-v1.md` | 46b22d7b01e123c02f41e934ad296582afc15d2ae3d523df9df73f4dd4431363 |
| `registres/iib-executante/p1-code-course-v1/rapport-developpeur-course-v5-v3.md` | bbb66683c15617424bb9a3db4fd8656415364dde3f0138ef82dfce3ca43222d6 |
| `registres/iib-executante/p1-code-course-v1/contre-lecture-code-course-v5-cl1.md` | 5c908fed7e01a96cbb3932230a889a972f167cc8b04942fd9e7e040491d5762f |
| `registres/iib-executante/p1-code-course-v1/note-verification-corrections-code-course-v5-cl1.md` | 9e52ee1792f45cdcb331a22b9259f0a63be8e507d0eb3756ea979736ce9c3006 |
**À venir** (l'exécutante en donnera chemins et empreintes dès leur contre-lecture) : correctif 0020 (tirage sur la carte) et son rapport ; correctif R001 (reprise) et son rapport. Écris les champs correspondants entre chevrons.
Registre : `registres/go.md` de `main`, lignes GO-2026-11-21-70, GO-2026-11-22-01, -42, -44, -57, -66, -71.

## 4. Interdits (cloisonnement)
N'ouvre aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » (noms et empreintes des consignes seulement, par leurs compagnons) ; ni `brouillons/ii-b-saboteur-budget-v1/`, ni la branche `lot/compte-4-v1`, ni rien sous `archives-reponses-modeles/`, ni la ligne R-2059 ; aucune sortie de mesure (rien sous `diag/` ni `donnees/` de runs réels, aucune branche `essai/*` ni `donnees/*` ouverte) ; rien de 7a, 7b, T0.6, étape B, B bis, P3-bis, barreau 5, épreuve à vérité plantée ; aucune pièce côté sondes (`prereg/lecture-sondes-barreau8-v1.md`, `src/controle_ia/barreau8_moniteurs/`, `brouillons/barreau8-lecture-sondes-v1/`, `docs/verdicts/`). Aucune dépense, aucun loueur, aucune poussée hors de ta branche.
Précisions : le texte scellé `conception-organisme-retenu-ii-b-v5-scellee-v1.md` et ses deux errata cités au § 3 sont permis et ne tombent pas sous la règle « conception-ii-b ». Dans `brouillons/ii-b-saboteur-budget-v5/`, n'ouvre que les pièces listées au § 3.

## 5. Ce que tu rends, et où
Sur une branche à toi, `claude/iib-fable-additif-course-v1` (ou le nom que la mère te donne), sous `brouillons/ii-b-saboteur-budget-v5/additif-course-v1/` :
- `additif-ordre-course-voie-A-v1-brouillon1.md`, `devis-voie-A-v1-brouillon1.md` ;
- `additif-ordre-course-voie-B-v1-brouillon1.md`, `devis-voie-B-v1-brouillon1.md` ;
- chacun avec son compagnon `.sha256` ; une note de 10 lignes au plus pour la mère : ce qui est prêt, les champs entre chevrons, les nœuds pour Lazar (recharge du crédit, réserve « deux machines », nombre de cartes).
Puis un message à la mère avec les chemins et les empreintes.
