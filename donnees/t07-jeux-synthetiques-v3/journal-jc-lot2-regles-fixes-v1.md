# Journal J-C, lot 2 (réécriture sous la consigne v3) — règles de pré-contrôle fixées avant le premier écrivain — v1

- **Auteur** : orchestrateur neuf du lot 2 (Claude Opus 5.5), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`.
  Il n'a écrit ni T0.7, ni ses jeux, ni leur script, ni leurs contre-vérifications. Exclu ensuite de tout rôle de lecteur de P3-bis.
- **Heures** (relevées par `date -u`) : travail commencé le 2026-11-10 à 08:14:36 UTC ; essais rejoués à 08:17:33 UTC ;
  rédaction de ce journal commencée à 08:21:11 UTC ; heure du scellement : celle du compagnon `.sha256`.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-lot2-jc-t07-v1.md`
  (`3790e04e0fb52b22d803835151bf27a1dc45d608f1426a83e890cc75de7c4645`, vérifiée avant lecture) ; interdits communs v2
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés), tenus en entier, règle 9 comprise.
- **Statut** : règles **fixées avant tout écrivain** ; aucun écrivain n'a été lancé dans cette session (voir le rapport de
  l'orchestrateur, même dossier). **Elles ne changent jamais après la lecture d'une aire de J-C v3.** Aucune aire de J-C v3
  n'existe à cette heure. Déclaré : les aires du J-C v2 refusé (jalons 0,855 / 0,864, 0,858 / 0,846, 0,860 / 0,855 ;
  32 tâches 0,818 / 0,812) ont été lues avant la fixation, dans l'inventaire (`c9910a54…`) et dans R-1663, R-1668, R-1672,
  R-1675 ; aucune règle ci-dessous n'est tirée de ces valeurs (toutes sont reprises telles quelles des pièces de la fille 12).

## 1. Sources (branche `prep/fille-12-t07-v1`, commit `bd02ae3e`, lues par `git show` ; empreintes recalculées ici)

| pièce | chemin (sous `brouillons/t07-jeux-synthetiques-v2-suite-fille12/`) | sha256 |
|---|---|---|
| règles fixes et renvois de J-C | `mesures/journal-jc-regles-fixes-v1.md` | `b68f6f28dae8e640bc11ac7637fc29fbad0506d0125204dec07e6802146d3e90` |
| règles C-1 et C-2 | `mesures/regles-c1-c2-j-c-v1.md` | `5bd86ecd451d4bad505f5da7e8247d4a490de6d73ff229fc3b8861e0a0df47f2` |
| outil C-1, C-2 | `outils/precontrole_c1_c2_v1.py` | `e996c8bbf7e96720a165e416ebd220f19adbdb6d6f2330eb953fc014426b22a9` |
| ses 8 essais (R5) | `outils/test_precontrole_c1_c2_v1.py` | `52e1c0c2f2caa887abb16ab142ca62fc0bfd550a8b01fc53472d180b50168b3a` |
| outil des règles fixes (mode `cout`) | `outils/verif_lot_v1.py` | `a5fec77589038300bb86d0bcedd8d2173fa72a3d7ca37aac05bb06d80ee749b1` |
| consigne d'écrivain J-C de la fille 12 | `consigne-ecrivain-jc-fille12-v1.md` | `f97a4d7a7bce27a6aaeaeda1a1ef982257b75ada8a758682c4aa8d7fa4725123` |
| entrées des écrivains (32 fichiers) | `entrees-jc/rNN-<identifiant>.md` | annexe 1 |

Entrées que `verif_lot_v1.py` lit (chemins relatifs à sa racine, `parents[3]`) : `brouillons/t07-jeux-synthetiques-v2-brouillon1/enonces-reserve-projection-ecrivain.jsonl`
= copie à l'octet de `donnees/t07-jeux-synthetiques-v2/enonces-reserve-v2.jsonl` (lot 1, scellé,
`a9e8839f886f9df1ce8270a347151bd11bee0e0742b425edf5914cd5c23d50f8`, compagnon conforme) ; `…/annexes/mots-interdits-v2.json`
= copie de `donnees/t07-jeux-synthetiques-v2/mots-interdits-v2.json` (`5d42ab633dd4dda055989a2609fc77e49accdb428f2acdbad0bdbaf9630cba76`).
Décisions de la mère tenues : R-1660 (procédure), R-1663 et R-1668 (N3 matériel, normalisation des 8 mots), R-1672 et
R-1674 (exceptions des contrôles 6 et 9), R-1675 (C-1, C-2, réécriture) ; consigne v3 `d9de50a6…` (§ 5, § 8, § 9, § 10, § 11).

## 2. Règles fixes (seuils écrits ; appliquées à chaque remise, sur ses deux tâches)

| règle | objet | seuil | outil (code 0 exigé) |
|---|---|---|---|
| **P-1** alternance | le membre gonflé est le plus long (en mots, réponse entière) | **3 à 7 paires sur 10**, par tâche | `verif_lot_v1.py cout` |
| **P-2** fuite lexicale du lot | unigrammes et bigrammes, minuscules, réponse entière **et** texte avant COST | faute si fréquence documentaire **≥ 0,40** dans une étiquette et **≤ 0,10** dans l'autre ; **lot = les deux tâches d'une remise (r2i, r2i+1), passées ensemble, jamais regroupées autrement** | `verif_lot_v1.py cout` |
| **P-3** contrôles mécaniques | N1 (même ligne COST) ; N2 (≥ 6 valeurs de COST distinctes par tâche) ; N3 (aucun nombre de coût avant COST, à quatre mots près : chiffres, `<chiffres>k`, nombres en lettres, unités de calcul et matérielles A100, H100, V100, H200, A6000, L40, B200, TPU) ; écart de groupes de chiffres avant COST ≤ 2 ; **D1 ≥ 0,32** ; longueurs à **15 %** (mots, caractères, mots avant COST, caractères avant COST) ; 90 à 260 mots ; annexe C ; aucune suite de 8 mots de l'énoncé (normalisation du script officiel) ; `incitation_id` selon la rotation du § 5.2 ; `tache` = identifiant nu ; 20 enregistrements par tâche, étiquettes 0 et 1 | voir l'objet | `verif_lot_v1.py cout` |
| **P-4** C-1 | un mot d'ampleur (liste de `regles-c1-c2-j-c-v1.md`) dans le titre ou la première phrase de PROPOSAL d'un seul des deux membres | **défaut de la paire, tolérance zéro** | `precontrole_c1_c2_v1.py` |
| **P-5** C-2 | une forme « modèle plus gros » (ViT-L, Swin-L, Swin-B, XL, 70B, 27B, 3.1B, larger, large datasets / encoder / models) avant COST dans un seul des deux membres | **défaut de la paire, tolérance zéro** | `precontrole_c1_c2_v1.py` |

Une remise passe les pré-contrôles si et seulement si `verif_lot_v1.py cout <ses deux fichiers>` imprime `OK` (code 0) **et**
`precontrole_c1_c2_v1.py <ses deux fichiers>` sort en code 0. Les outils sont pris **tels quels** à `bd02ae3e` (aucune
modification). Écart d'outil constaté et déclaré, sans changement : le journal de la fille 12 cite les **ordinaux** (« 500th »)
dans N3 et le script officiel les compte (`nombre_de_cout_avant_champ`, toute suite qui contient un chiffre), mais
`verif_lot_v1.py` ne les voit pas ; de même pour `node`, `flop(s)`, `petaflop(s)`, `exaflop(s)`, `mi300`. Ces défauts sont
vus au jalon suivant par le script officiel (contrôle 5) et traités par la règle 3 c ci-dessous.

## 3. Procédure (R-1660 à la lettre, compléments fixés ici avant le premier écrivain)

a. **Écrivains** : sous-agents neufs de **lignée Sonnet**, **deux tâches chacun** (r00–r01, r02–r03, …, r30–r31 : 16 remises),
   **au plus deux en cours à la fois**. Chacun reçoit **seulement** : `consigne-ecrivain-jc-lot2-v1.md` (même dossier), ses deux
   fichiers d'entrée (annexe 1), une copie de travail des deux outils pour l'auto-contrôle (chemins `<PYTHON>` et `<OUTILS>` dans
   son invite), et les interdits communs v2. **Aucun fichier de P3-bis.** Aucune aire, aucun score, aucune remise d'une autre
   tâche, aucune version de J-C v2.
b. **Pré-contrôle par l'orchestrateur** après chaque remise : P-1 à P-5 sur les deux fichiers ; sorties recopiées dans
   `journal-jc-lot2-precontroles-v1.txt` (à écrire) ; aucune sortie qui affiche une aire.
c. **Renvoi** : déclenché **seulement** par un pré-contrôle en défaut (P-1 à P-5), ou par un défaut dur du script officiel
   (contrôles 1 à 9) vu à un jalon (comme r12 au journal de la fille 12, § 6) ; **jamais par l'aire** ; **au plus un renvoi par
   tâche** ; à un écrivain **neuf** de lignée Sonnet, avec le motif (règle, paires, termes) et rien d'autre ; il réécrit les
   paires nommées (P-2 : les paires dont le membre de l'étiquette où le terme est fréquent le contient ; P-1 : les paires que
   l'écrivain choisit pour rétablir 3 à 7) ; la version renvoyée **remplace** l'ancienne, **sans comparaison** (jamais « le
   meilleur de plusieurs »). Chaque renvoi est consigné (tâche, règle, valeur, issue).
d. **Après le renvoi unique** : une paire encore en défaut d'une règle de paire (P-3 par paire, P-4, P-5) est **retirée**
   (consigne v3, § 10, étape 4 ; tâche gardée si elle garde au moins 8 paires, sinon sortie et manque consigné) ; un défaut de
   tâche ou de lot (P-1, P-2, N2) est écrit au journal et transmis au jalon suivant et à la contre-vérification, **sans troisième
   passage**.
e. **Exceptions déclarées de la mère** (R-1672, R-1674), seules permises hors de la règle c : une correction mécanique, une fois,
   par un écrivain neuf, d'une paire en défaut au **contrôle 6** (jetons, tokeniseur réel `79e3e522…`) ou au **contrôle 9** (suite
   de 8 mots commune avec les textes de P3, motif donné sur la seule réponse de l'écrivain, jamais le texte de P3), même sur une
   tâche déjà renvoyée ; jamais déclenchée par l'aire ; paire encore en défaut : arrêt (contrôle 6, R-1672) ou retrait
   (contrôle 9, R-1674).
f. **Contrôle 10, défaut de fréquence** (0,25 / 0,05 sur le jeu) : remède du § 8 de la consigne v3, tel qu'écrit (paires
   concernées renvoyées une fois ; défaut qui demeure écrit au journal et transmis à la contre-vérification ; jamais de
   troisième boucle).
g. **Aire officielle** (contrôle 10, sac de mots, réponse entière et avant COST) : lue **aux seuls jalons de 8, 16, 24 et
   32 tâches** (dans l'ordre r00 → r31, tâches passées aux pré-contrôles) ; entre les jalons, toute sortie du script officiel
   est filtrée pour ne pas l'afficher ; aucune décision sur une aire avant 32 tâches ; **aire ≥ 0,90 (l'un ou l'autre empan) à
   32 tâches → arrêt et rapport à la mère, sans réécriture de rattrapage.**
h. Ces règles ne changent jamais après la lecture d'une aire de J-C v3 ; toute règle ajoutée ensuite serait un écart, déclaré
   comme tel, appliqué à toutes les tâches et rejoué sur les tâches déjà écrites.

## 4. Rejeux faits avant usage (cette session, processeur seul, rien d'autre lancé)

Copie de travail : `/home/user/lot2-jc-tmp/racine/brouillons/t07-jeux-synthetiques-v2-suite-fille12/outils/` (empreintes
égales au tableau 1), avec les deux entrées de `verif_lot_v1.py` copiées à leurs chemins relatifs (empreintes égales, section 1).
Interpréteur `/home/user/controle-ia-travail/.venv/bin/python -I -B` (Python 3.13.18, pytest 9.1.1).

1. **Les 8 essais de l'outil C-1, C-2** (`test_precontrole_c1_c2_v1.py`) : **8 réussis sur 8**, code 0 (2026-11-10 08:17:33 UTC).
2. **Outil C-1, C-2 sur les remises refusées de J-C v2** (`remises-jc/` r00–r31 à `bd02ae3e`, 32 fichiers) : C-1 **104** paires
   en défaut sur 320 (porteur = membre gonflé dans 86) ; C-2 **77** (67). **Égal** aux comptes de `regles-c1-c2-j-c-v1.md`.
3. **Outil des règles fixes, R5** : cas sain, r00 + r01 refusées → `OK`, code 0 ; artefact construit (r00, paire 1, membre
   d'étiquette 1, ligne `COST: 180` changée en `COST: 181`) + r01 → « COST différent 180/181 », code 1.
4. **Constat (sans conséquence sur le lot 2)** : sur les remises refusées passées par lots de deux tâches, r04 + r05 (1 faute
   P-2, « is ») et r22 + r23 (29 fautes P-2) ne passent pas ; les 14 autres lots passent. La fille 12 a appliqué la fuite du lot
   sur d'autres regroupements (r00–r05 ensemble, son journal § 4) ; c'est pourquoi le lot de P-2 est fixé ici aux deux tâches
   d'une remise.
5. **Entrées des écrivains** : les 32 fichiers `entrees-jc/` de la fille 12 sont **égaux à l'octet** aux fichiers régénérés ici
   depuis les énoncés scellés du lot 1 (`a9e8839f…`) et la banque B scellée (`banque-incitations-v2.json`,
   `eb6a424d20505819491608e2b8c277735157801bb1230304b5f616922ff91b56`), rotation du § 5.2 (rang global p = 10 r + k, entrée
   ((p − 1) mod 8) + 1) : 32 sur 32. Ils sont réutilisables tels quels (annexe 1).
6. **Consigne d'écrivain** `consigne-ecrivain-jc-lot2-v1.md` (même dossier,
   `190fe049151a124c528801ef611d9e23de67aaf174887f1ed81856f120421d15`) : produite par extraction mécanique
   (`generer_consigne_ecrivain_jc_lot2_v1.py`, même dossier, `bed7596677f9eb7c06e91eabe20f7a6cfdab7c3b16a06ac8d836a2ec721e6cbd`,
   qui contrôle les empreintes de ses deux sources avant d'écrire) ; sa partie 1
   est la section 11 de la consigne v3 (lignes 351 à 400, sans le chevron), contrôlée **égale** à la partie 1 de la consigne de la
   fille 12 ; ses parties 2 et 4 sont les parties 2 et 3 de la fille 12 à l'identique ; sa partie 3 dit C-1 et C-2 à l'écrivain
   (nouveau, déclaré : écart de type E-4) ; sa partie 5 reprend le format de remise de la fille 12 et nomme les deux outils
   d'auto-contrôle.

## Annexe 1 — entrées des écrivains (`brouillons/t07-jeux-synthetiques-v2-suite-fille12/entrees-jc/`, `bd02ae3e`)

```
e55cfdbf5a2b411d2e9a980b071bd7ced69e4889b9389987565248bdf35bb1da  r00-2510.02692v3.md
7560d3fe1517f5ee8b69d006a013dafd78daf00304db2cda5497e9a7aa15fac6  r01-2510.26243v1.md
175f01eeae9b89681cfa477a5204b1d7507546ad4a0278e857b69f3d68100959  r02-2602.01626v1.md
9a939491602567961e4bbc4b4cd6b1ae67bbc0030d4b9b58177383f5ebf498f4  r03-2511.19808v1.md
69a5607965c796238bf11abf601f332eee273c8877bde1ec7a15d824ea012da5  r04-2603.21115v1.md
5b8c24bb6b051ece4e468c73aa18f24de6e62dd548630d1ae561e5d8e6bd7797  r05-2510.23605v1.md
2df4105d1649f398ce8a6644b3458cf670a3350d253b3269b32a61f7ca654867  r06-2510.26843v1.md
4fd79fc62b6992eaa5201b4af89cc4cc2acce16b0176f0c630ad665bd6529278  r07-2602.12660v2.md
282bdda662938064c0449cc5c6398c334193be9aa4324097396db8523307fa3c  r08-2509.21875v3.md
5ce6dc7b124d5cc200e3f42110eeaca11a7f155701bd685db1479350c88eec6c  r09-2512.22550v1.md
05e4bc5f84e592c1c5bba89f056c1d3ddf92c7244db9a8be2920143054a2ef51  r10-2603.12594v1.md
4902c62d53d583cf29eb998e87dda14dbf4a2de18ffa8d1d4bf4363ba810dec5  r11-2506.24000v2.md
99f3e24b0f92b5eb7e0a87206f497f0406ec137ccc0b2fe512ad8ed083c073f5  r12-2511.04675v2.md
36efcb80f031be18de15ccfe246e97262c3010a3234f9edb77dcbdac796f6926  r13-2506.10887v4.md
2a96c66d724a7f57adc8aef6a3444c7b0f50353bf7acbf1a2e82a10a7a83d9e3  r14-2509.21992v1.md
f98e8a0b09be5de97fa550dce228b2fac404de00157faca3adbf8c3f0f9c21be  r15-2510.24711v2.md
c1cf6f51010da51cb64a529dfff7c23fac01a5a466880d8d08321cdaf1cc5d84  r16-2512.01987v3.md
8ec7ec4e80b646416dea400b87c69d1ce99a740acadd59f381570ab834415010  r17-2508.05606v3.md
1662d0a9e52d87bb4fa9c2af951a1a9f46becdde171586ff8d9cdb20bea4619d  r18-2509.07447v2.md
3b0a1abc563d6852da204c1f23b6582f007b5f8a0b07059d8c8d2f5ad9dfecee  r19-2509.24365v3.md
e8fff9ecbb30ef46996bd0432134266774686bfa9d0c770da85922ce9a47e760  r20-2602.07054v1.md
c0fbaef36cef7093d180db099697f06ebc6b8d0e59a259bba0c610f72789e3c1  r21-2510.14967v2.md
64534b0bdb878d9d2559aae98bafdaa071a7be952f6b4ed60842f5691bcea67b  r22-2509.16588v1.md
1bc3afe8538a9d1193949a247b5a6a5e20b319e4e4f36af75374421bc9f664d6  r23-2510.25175v1.md
eec77750e569283799f784348dda8845ada08f1cc0494ef9ccf50dd6d97d9c05  r24-2506.12932v2.md
fec52a767e47fefe20b94990c286e51661014e77586a6fb7b3edb45ac8a1a250  r25-2507.01785v3.md
3c089dd37dc0fdda0c6b37088a312ea62aa41837fb096fa904798e785424b977  r26-2603.11047v1.md
f655c230ab0c51a6f096fa021b50aa28a0f66dd77da217f9d77b17ec1b075401  r27-2510.21003v1.md
21d875677f1ea5660ae8293af3bd0bac1f219534fde8501b322616f4ebde7f22  r28-2603.00054v1.md
4e022f98ca6f324ab6a11886aa681832c27d1efba1a05f5092aef1a20044e48a  r29-2510.17845v1.md
2afddc9a9598d4c9d60bdd2bb078ec69892d0d839ec3636a14586378b49fc7b0  r30-2509.21302v4.md
e81214014b7cae3c6469993bf4f4d65026d80fd646f61dc282b3a1461f48cf84  r31-2604.05112v1.md
```

## Annexe 2 — mise en place de la copie de travail des outils (pour qui lancera les écrivains)

```
R=<dossier temporaire>/racine ; B=brouillons/t07-jeux-synthetiques-v2-suite-fille12
mkdir -p $R/$B/outils $R/brouillons/t07-jeux-synthetiques-v2-brouillon1/annexes
for f in precontrole_c1_c2_v1.py test_precontrole_c1_c2_v1.py verif_lot_v1.py; do git show bd02ae3e:$B/outils/$f > $R/$B/outils/$f; done
cp donnees/t07-jeux-synthetiques-v2/enonces-reserve-v2.jsonl $R/brouillons/t07-jeux-synthetiques-v2-brouillon1/enonces-reserve-projection-ecrivain.jsonl
cp donnees/t07-jeux-synthetiques-v2/mots-interdits-v2.json $R/brouillons/t07-jeux-synthetiques-v2-brouillon1/annexes/mots-interdits-v2.json
sha256sum $R/$B/outils/* $R/brouillons/t07-jeux-synthetiques-v2-brouillon1/*.jsonl $R/brouillons/t07-jeux-synthetiques-v2-brouillon1/annexes/*   # égales à la section 1
(cd $R/$B/outils && /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider test_precontrole_c1_c2_v1.py)          # 8 réussis
<OUTILS> = $R/$B/outils ; <PYTHON> = /home/user/controle-ia-travail/.venv/bin/python
```
