# Texte gelé — « Neuron Lens », tranche de l'ajustement de nos lentilles (B-β), Llama 3.1 8B Instruct — v1, brouillon 1

Préenregistrement court d'une expérience **hors du programme**, aux sections du gabarit `prereg/gabarit-preregistrement-v1.md`
(R1, R2). Il continue le texte gelé v6 du volet A et de la tranche des lentilles publiques (B-α), qui renvoyait cette tranche à
« un texte séparé, gelé avant β » (§ B.4). **Brouillon : non scellé, non contre-lu.** Il ne lance rien.

- Autrice : session fille « Neuron Lens » `session_01XJ6MgnoxfSYHdF6rpEqZ7w` (mère `session_01XJ6Mgr8BN6UanALsQatc5E`), sur le mot
  de Lazar du 2026-11-18 « commence le préenregistrement ici » ; branche `claude/tender-meitner-iyxt5i`.
- Date (UTC, `date -u`) : 2026-11-18, brouillon 1 écrit vers 03:10.
- Code d'analyse : **aucun écrit à ce jour.** Code voisin épinglé : `stdlogits/neuron-lens`, commit
  `849bfe1678e28becceb1e3864afe5fc8297d02e4` (MIT), lu seulement, jamais exécuté dans le conteneur (règle de Lazar, R-2710) ; correctifs
  au § « Plan d'analyse », B.2. Notre code (contrôles de B0, recalcul de n, verdicts) sera écrit après le scellement de ce texte,
  contre-lu, et son commit consigné au manifeste ; il met en œuvre ce texte sans rien en changer (tout écart : liste d'arrêt).
- **Ce que l'autrice a lu avant d'écrire** (déclaré, R4) : les verdicts déjà rendus de la tranche des lentilles publiques (R-2915), de
  sa recourse (R-3083) et de l'essai d'invariance au lot (R-3093). Les prédictions ci-dessous en tiennent compte. Aucun résultat de
  cette tranche-ci n'existe.
- Documents qui font foi :

| pièce | chemin | empreinte SHA-256 |
|---|---|---|
| texte gelé v6 (volet A et B-α) | `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (`prep/neuron-lens-v1`, `45a81e08`) | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` |
| plan et devis v1 (§ 4) | `docs/notes/neuron-lens-v1/plan-et-devis-v1.md` (idem) | `bc20a12aeb5cffeaa12ac264d5141036100b530f4a6a7c0998e24d1b184e3668` |
| plan et devis v2 (§ 3) | `docs/notes/neuron-lens-v1/plan-et-devis-v2.md` (idem) | `4f6534907b849cada369ac87df6fbcf87f766085c0ed56c0388bf849e4aa9c77` |
| devis final de la tranche, v12 (décisions de Lazar en tête) | `docs/notes/neuron-lens-v1/devis-b-beta/devis-tranche-b-beta-v12.md` (branche de session) | `41a4c1f6dc5c2fe59be06d49e76425d857f79338b6bd29aac95ecfa3533294f1` |
| verdict de B-α | `docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md` (branche principale) | `ca06acb1550ccc76fef1ec89ae0aec170c5f05252bda2711f131eaa0e645fc1d` |
| verdict de la recourse de l'ablation | `docs/notes/neuron-lens-v1/lecture-recourse-b7/verdict-recourse-b7-v1.md` (`prep/neuron-lens-v1`) | `996744b2090bacc2055bf22ba50c10f810a5364b3b81fab65bdba4d4edb9cc17` |
| résultats publiés, lecture contre pilotage (Qwen3-8B) | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json` | `8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3` |
| résultats publiés, lectures aux activations (Qwen3-8B) | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/reads_at_firings_qwen3-8b.json` | `ac0bf101e341385a400bbecb751f9720428da1d0bd09a752c8337dd84ba182cd` |
| constats publiés, § 1 (stabilité) | `docs/findings.md` du voisin au commit `849bfe16`, lignes 49 à 62 | `8814874b1cbe144f2cd1070ee20384b397be105c47b3e9cbeb9360a25ee5a866` |
| ligne de décision | GO-2026-11-18-02 (`registres/go.md`, branche principale) : prix exigé 2,62 USD/h, plafond « avec une relance », lieu L1, clé neuve, périmètre entier | — |

## Hypothèse

### Portée et séparations (reprises du texte gelé v6, inchangées)
- **Hors programme.** Aucune hypothèse du programme n'est testée ; aucun résultat n'entre dans T0.7, T0.8, G0, G1 ni dans un
  préenregistrement du programme sans nœud de Lazar (GO-2026-11-17-03).
- **Séparation d'avec P3 et P3b** : l'autrice n'a rien lu de P3 ni de P3b ; les sorties de ce texte ne fixent aucun choix de lecture de
  P3b. Aucune donnée réservée, aucune sonde du programme n'est employée ou lue.
- **Modèle** : `meta-llama/Llama-3.1-8B-Instruct` (32 couches, 4 096 dimensions, 14 336 neurones par couche à portes) ; révision
  consignée à l'addendum des empreintes.
- **Règle de lecture** (v6) : une lecture par lentille peut ajouter un soupçon sur une sonde, jamais la blanchir.

### Énoncé
La chaîne publiée, refaite sur Llama 3.1 8B Instruct avec **nos** lentilles R et S, ajustées par le code du dépôt voisin sur
1 000 documents de DCLM :
- **B-1, stabilité de nos lentilles** : les lentilles ajustées sur les moitiés paire et impaire du corpus diffèrent peu, et lisent le
  même premier jeton pour la plupart des neurones ;
- **B-2, lecture contre pilotage** : la lecture de l'écriture d'un neurone par notre lentille R prédit l'effet de son pilotage ;
- **B-3, avance sur la lentille des logits** : elle devance nettement la lentille des logits dans la première moitié du réseau ;
- **B-4, écart aux lentilles J et J++** de Neuronpedia : rapporté, non décisif ;
- **B-5, lecture côté entrée** : la lecture par notre lentille S de la direction d'entrée d'un neurone nomme le jeton sous ses
  activations les plus fortes aux premières couches, et de moins en moins en profondeur ;
- **B-6, deux codes** : notre lentille R et la lentille R publique de Neuronpedia donnent la même lecture contre pilotage, à peu près ;
- **B-7, lecture contre ablation couche par couche** (conclusion pour un moniteur, hors verdict de reproduction) : avec notre lentille R
  aussi, la lecture prédit mal ce qu'une activation isolée fait en contexte avant les deux tiers de la profondeur.

## Prédiction chiffrée et signe attendu

R3 : aucune course ne vise un signe ; les issues contraires sont écrites et rapportées à l'identique. Confiances de l'autrice, après
lecture des verdicts de B-α (déclaré) :

| mesure | prédiction | issue modale prédite | confiance |
|---|---|---|---|
| B-1 | différence entre moitiés de 0,02 à 0,08 par couche ; premier jeton commun pour 0,85 à 0,99 des neurones aux six couches lues | « reproduit » | 0,6 |
| B-2 | proche de B-α (« autre » : `pass` sous 0,90 à une ou deux couches de 8 à 15), un peu meilleur avec un corpus d'ajustement de 1 000 documents au lieu de 64 | « autre » ou « reproduit » | 0,45 pour « reproduit » |
| B-3 | écart R − logits ≥ +0,20 aux couches 4 à 15, comme en B-α | « reproduit » | 0,7 |
| B-4 | positif et petit, non décisif | — | — |
| B-5 | `read_S` ≥ 0,60 à la couche 0 et nettement plus haut aux couches 1 à 7 qu'aux couches 12 à 23 | « reproduit » | 0,5 |
| B-6 | écart absolu des `r_med` de B-2 (notre R contre `npR`) ≤ 0,05 à au moins les trois quarts des couches 0 à 27 | rapporté | 0,5 |
| B-7 | comme en B-α et sa recourse : bas aux couches 0 à 14, ≈ 0,3 à la couche 15, ≥ 0,8 aux couches 26 à 29 | « autre » (seule la couche 15 manquerait) | 0,55 |
| verdict d'ensemble | — | « partiel » | 0,5 |

## Métrique

### B.1 Commun (repris du texte gelé v6, § B.1, sauf mention)
- **Chaîne de mesure** : `checks/causal_lens.py measure` avec ses défauts publiés : 32 neurones par couche (`random.Random(0)`), deux
  pôles, 16 contextes de 64 jetons, positions `[16, T)`, doses 1× et 4× `act_top`, ablation sur les 8 premiers documents du pôle,
  fenêtre de 8 ; **lot de contextes publié, 64** (sur une A100, les lots 16 et 64 donnent le même résultat au bit près, R-3093 ; sur
  H100, non mesuré) ; puis `score`.
- **Lentilles notées** : logits ; J, J++ (`npJpp`) et R publique (`npR`) de Neuronpedia, fichiers et empreintes du texte gelé v6 ;
  **notre lentille R** (`R:dclm-llama`, exportée par `04_export_rlens.py` depuis l'ajustement). Aucune lentille n'entre dans `measure`.
- **Métriques par couche, cible et lentille** : `r_med`, `pass`, `control_med`, **n**, telles que définies au texte gelé v6, § B.1 (n
  recalculé par notre code depuis le fichier `-causal.pt`, par la règle de `score`). Cibles : « steer 1x » (B-2, B-3, B-4, B-6) ;
  « ablate win » (B-7) ; « steer 4x » et « ablate pos » rapportées sans critère.
- **Couche lisible** : n ≥ 48 pour la cible considérée ; une bande dont plus du quart des couches est non lisible rend la mesure
  « partielle » pour cette bande.
- **Bandes de couches** : celles du texte gelé v6, inchangées.

### B.2 Mesures propres à cette tranche
- **B-1, différence entre moitiés** : la valeur que `02_fit.py` imprime en fin d'ajustement, par cible et par couche,
  `‖moyenne paire − moyenne impaire‖ / ‖moyenne‖` (`neuron_lens/transport.py`, `split_half`, l. 64-72) ; pour la lentille R, cibles
  `out` (couches 0 à 30) et `mid` (0 à 31) ; pour la lentille S, `mid` et `out` (0 à 31).
- **B-1, accord du premier jeton** : `checks/lens_compare.py` sur les lentilles R des deux moitiés (`04_export_rlens.py --half 0` et
  `--half 1`), part des neurones dont la lecture d'écriture a le même premier jeton sur les jetons gardés du catalogue, aux couches
  **2, 7, 12, 18, 23, 28** (les couches 2, 8, 14, 20, 26, 32 de la référence, ramenées à 32 couches par `round(l × 32/36)`) ; le
  recouvrement des dix premiers jetons est rapporté sans critère.
- **B-5, `read_S`** : la part des pôles d'une couche dont la lecture par notre lentille S de la direction d'entrée nomme les jetons des
  activations les plus fortes, au taux de fausses découvertes de 5 % (Benjamini-Hochberg sur les neurones de la couche), contre des
  paires mal appariées de la même couche (`checks/reads_at_firings.py`, définition l. 1-40, `FDR = 0.05` l. 75) ; `read_S_net` (au-delà
  du 99ᵉ centile des paires mal appariées, net du leur) rapporté sans critère.
- **B-6** : `r_med`(notre R) − `r_med`(`npR`), « steer 1x », couches 0 à 27, dans la même sortie de `score`.
- **Intervalles** : par rééchantillonnage des pôles (2 000 tirages) pour B-2, B-3, B-4, B-6, B-7, rapportés ; verdicts sur les valeurs
  ponctuelles (comme en B-α).

## Seuil

« Reproduit » exige la condition à **chaque couche lisible** de la bande ; « plus de N des couches » se lit « plus de la moitié des
couches lisibles de la bande nommée » (règle du texte gelé v6).

| mesure | « reproduit » | « non reproduit » |
|---|---|---|
| B-1 | différence entre moitiés ≤ 0,10 à chaque couche et chaque cible des deux lentilles **et** accord du premier jeton ≥ 0,80 aux six couches lues | une couche d'une cible à plus de 0,20, **ou** un accord sous 0,60 à l'une des six couches |
| B-2 | seuils de B-2 du texte gelé v6, avec **notre** lentille R : `r_med` ≥ 0,40 (8–15), ≥ 0,60 (16–23), ≥ 0,85 (24–27) ; `pass` ≥ 0,90 (8–27) ; témoin : `control_med` hors de ±0,05 à au plus une couche de 0 à 27, à aucune hors de ±0,10 | `pass` < 0,50 à plus de 6 des 12 couches 16–27, ou `r_med` < 0,30 à plus de 4 des 8 couches 16–23 |
| B-3 | `r_med`(notre R) − `r_med`(logits) ≥ +0,20 à chaque couche 4–15 | écart ≤ 0 à plus de 6 des 12 couches 4–15 |
| B-4 | rapportée, non décisive : notre R − J et notre R − `npJpp`, couches 4–23 | — |
| B-5 (réécrit) | `read_S` ≥ 0,60 à la couche 0 **et** moyenne de `read_S` sur les couches 1 à 7 au moins 0,10 au-dessus de sa moyenne sur les couches 12 à 23 | `read_S` < 0,30 à la couche 0, **ou** moyenne sur 1 à 7 au plus égale à la moyenne sur 12 à 23 |
| B-6 | rapportée : écart absolu ≤ 0,05 attendu | un écart absolu > 0,15 à une couche de 0 à 27 ouvre un audit des deux lentilles (verdicts suspendus pour B-2, B-3, B-6) |
| B-7 (« ablate win », notre R) | `r_med` < 0,25 à chaque couche 0–15 **et** ≥ 0,50 à chaque couche 26–29 | `r_med` ≥ 0,40 à plus de 4 des 8 couches 8–15, ou < 0,30 à plus de 2 des 4 couches 26–29 |

**Pourquoi B-5 est réécrit** (texte gelé v6, § B.4) : le critère du plan v1, « décroissant sur le premier quart », manquerait la
référence publiée elle-même (`read_S` 0,848, 0,248, 0,090, 0,229, 0,352 aux couches 0 à 4 de Qwen3-8B). Le critère neuf garde la couche
0 du plan v1 et remplace la monotonie par un écart de moyennes entre bandes. **Sur la référence publiée** ramenée à 32 couches par la règle
du texte gelé v6 (couche Llama l ↔ couche Qwen3 ⌊l × 36/32⌋) : moyenne sur 1 à 7 ≈ 0,22, sur 12 à 23 ≈ 0,03, écart ≈ 0,20 ; le seuil de
0,10 en vaut la moitié (recalcul à refaire par notre code des verdicts, B.4, avant la course ; tout écart à ces valeurs arrête).

**Chaîne en défaut, audit** (aucun verdict de mesure) : les conditions (a) à (e) du texte gelé v6 (« Seuil », B), appliquées aussi à
notre lentille R — en (c) : notre R, `r_med` (« steer 1x ») < 0,85 à l'une des couches 28–30 ; en (e) : notre R confondue avec la
lentille des logits (|écart| < 10⁻³ à une couche de 0 à 23, ou matrice égale à l'identité à une couche de 0 à 27) ; plus :
- (f) **essai de l'estimateur sur un Llama miniature contre la force brute** en échec (tolérance des essais du dépôt, inchangée) ;
- (g) **ajustement vide ou non fini** : une moitié sans document, une différence entre moitiés non finie, ou une matrice de lentille non
  finie ;
- (h) **nombre de couches exportées** différent de 31 pour la cible `out` de R (couches 0 à 30) ou de 32 pour les autres cibles.

## Plan d'analyse

### B.1 Étapes (devis v12, § 1 et § 4 ; GO-2026-11-18-02)
B0 : montage ; essais des correctifs (B.2) et de l'estimateur (Llama miniature contre la force brute) ; **banc** : deux documents par
lentille, le second chronométré (le premier compile) ; si le temps projeté sur les 2 000 passages dépasse 13,1 h (23,6 s par
document), l'ajustement ne part pas (devis v12, § 5) → B1 : ajustement de R puis de S, 1 000 documents de DCLM chacune, 128 jetons,
moitiés paire et impaire dans le même passage, `--save-minutes 60`, reprise sur point de sauvegarde ; différences entre moitiés
consignées → export des lentilles (entière, moitié paire, moitié impaire) ; `lens_compare.py` sur les deux moitiés de R (B-1) → B2 :
corpus d'activations, comptes de jetons, fumée, passe complète (refaite : les tables de B-α ont été détruites avec ses machines) →
B3 : pilotes exacts (`07_drivers.py`) et lectures par les poids, neurones seulement (`08_reads.py`), avec nos lentilles → B4 :
`measure` au lot 64, `score --lenses logit,J,npJpp,npR,R:dclm-llama` → B5 : `checks/reads_at_firings.py`, neurones (B-5) → B6 :
manifeste (R9), résultats bruts versés avec leurs compagnons, **lentilles non rangées** (lieu L1 : seules les empreintes et les mesures
dérivées sont versées), destruction par identifiant (R10).

### B.2 Correctifs du code voisin (chacun écrit, contre-lu, scellé avant usage ; essayé à B0 sur la machine)
Repris : (1) passe d'activations ; (2) lentilles publiques de Llama dans `lenses.py` ; (3) graine de l'audit. Neufs :
- (4) `checks/lens_compare.py` : le modèle est écrit en dur (`MODEL = "Qwen/Qwen3-8B"`, l. 29) ; le rendre paramètre ;
- (5) `01_lens_corpus.py` : n'exporter que des documents d'au moins 128 jetons sous le tokeniseur de Llama, dans l'ordre du jeu mélangé
  publié, jusqu'à 1 000 (écart déclaré au code publié, qui prend les 1 000 premières lignes : il évite les recompilations des documents
  courts, devis v12, § 4) ; les identifiants retenus et écartés vont à la partie 2 de l'addendum ;
- (6) tout autre réglage nécessaire à Llama dans `02_fit.py`, `04_export_rlens.py`, `07_drivers.py`, `08_reads.py` et
  `checks/reads_at_firings.py` : **inventaire à faire par lecture du code avant la commande** ; chaque écart au code publié déclaré.

### B.3 Graines (R9)
`random.Random(0)` du dépôt pour les neurones (comme publié) ; graine 1 seulement pour l'audit R4, par le correctif (3) ; toute autre
graine par `numpy.random.SeedSequence(entropy=20261118)`, branche « B-β », consignée au manifeste. L'ajustement lui-même est
déterministe à l'ordre des documents près (aucun tirage).

### B.4 Code des verdicts essayé (R5), avant la course
Le code qui applique les seuils est passé : (i) sur la référence publiée de Qwen3-8B ramenée à 32 couches (lentille « R:dclm » dans le
rôle de notre R et de `npR`, « J » dans celui de J et `npJpp`, n = 64 ; `reads_at_firings_qwen3-8b.json` pour B-5) : attendu B-2, B-3,
B-5, B-7 « reproduit », B-6 écart nul, aucune chaîne en défaut, aucun déclencheur « trop beau » ; B-1 n'a pas de référence chiffrée par
couche : essayé sur des moitiés factices (cas sain : différence 0,05 et accord 0,9 → « reproduit » ; artefacts : une couche à 0,25 →
« non reproduit » ; accord 0,5 → « non reproduit ») ; (ii) les artefacts (ii-a) à (ii-e) du texte gelé v6, § B.3, appliqués à notre R ;
(iii) deux artefacts de B-5 (`read_S` de la couche 0 mis à 0,25 → « non reproduit » ; moyennes des bandes égales → « non reproduit ») ;
(iv) un artefact de B-6 (écart de 0,20 à la couche 10 → audit, verdicts suspendus). Résultats consignés avant la course ; tout écart à
l'attendu arrête la course.

### B.5 Lecture
Les résultats sont lus par un lecteur neuf, sur un plan de lecture scellé avant toute ouverture des résultats ; la fille ne lit aucun
résultat avant ce verdict. Comparaisons multiples : les verdicts sont des règles de seuils couche par couche, sans test
d'hypothèse ; aucune correction n'est appliquée, et les intervalles sont rapportés sans servir au verdict (comme en B-α).

## Critères de lecture gelés

| issue | verdict |
|---|---|
| chaîne en défaut ((a) à (h)) | **chaîne en défaut** ; aucun verdict de mesure ; audit, nœud à la mère |
| B-1, B-2, B-3 et B-5 « reproduit » | **reproduit avec nos lentilles** |
| B-2 ou B-3 « non reproduit » | **non reproduit avec nos lentilles** — rapporté à l'identique (R3) ; lu avec B-α : si B-α avait « reproduit » B-3 avec `npR` et que notre R ne le fait pas, l'écart porte sur notre ajustement, audit des deux (B-6) avant lecture |
| autre | **partiel**, mesure par mesure |

B-6 se lit à part : un écart ≤ 0,05 dit que les deux codes s'accordent ; un écart > 0,15 suspend les verdicts de B-2, B-3 et B-6 jusqu'à
l'audit (même chaîne, mêmes tables : la différence ne peut venir que des lentilles).

**B-7, pour un moniteur** (lectures du texte gelé v6, inchangées) : « reproduit » → là où `r_med` est bas, une étiquette de neurone
décrit une poussée moyenne et ne sert pas à lire un épisode, avec notre lentille comme avec la publique ; « non reproduit » par le haut
→ audit R4 avant toute lecture ; « non reproduit » par le bas → rapporté ; autre → couche par couche.

**Audit symétrique (R4)** :
- **trop beau** : notre R, `r_med` ≥ 0,95 à une couche 0–7, ou `control_med` écrit égal à 0 à au moins 2 couches de 0 à 27 ; ou, pour
  B-1, une différence entre moitiés exactement nulle à une couche, ou un accord de 1,00 aux six couches → vérifier que les deux moitiés
  sont distinctes (comptes de documents 500 et 500, sommes différentes), le témoin bien apparié, le pilotage de norme non nulle ;
  `measure` relancé avec la graine 1 si l'audit porte sur B-2 à B-7 ; verdict après l'audit ;
- **tout négatif** (B-2 et B-3 « non reproduit » avec notre R) : rejouer `score` avec `npR` sur les mêmes tables (cas sain : B-α) ; si
  `npR` redonne ses valeurs de B-α à 0,05 près, le défaut est dans notre lentille ; sinon dans la chaîne.

## Liste d'arrêt

| condition | action |
|---|---|
| ce texte non scellé ; un correctif employé non contre-lu ou non scellé ; le code des verdicts non essayé (B.4) | rien ne part (R1, R2) |
| pas de ligne de calcul inscrite par la mère sur GO-2026-11-18-02, pas de feu écrit, commande non contre-lue | rien ne part |
| clé neuve d'accès au modèle non confirmée par Lazar | rien ne part ; aucune clé passée à une machine |
| pas de relevé de prix dans l'heure qui précède la création, ou prix lu au-dessus de 2,62 USD/h stockage compris | rien ne part ; ou destruction immédiate par identifiant |
| addendum des empreintes non scellé avant la première passe (révision de Llama, révision et identifiants des 1 000 documents de DCLM, fichiers de Neuronpedia, corpus d'activations) | rien ne part |
| gardes du devis v12 (§ 5) : compte rendu à 45,0 USD ; arrêt dur à 67,5 USD ; minuterie ; crédit ; course figée ; perte de machine | selon le devis : compte rendu, arrêt et destruction par identifiant, nœud à la mère |
| banc de B0 au-delà de 23,6 s par document (second document) | l'ajustement ne part pas ; destruction ; compte rendu |
| chaîne en défaut (f), (g) ou (h) | arrêt ; destruction ; compte rendu |
| empreinte d'un fichier différente de celle écrite ici ou à l'addendum ; licence différente | arrêt ; message à la mère |
| tout écart de notre code à ce texte, découvert en course | arrêt ; écart écrit avant toute suite |
| tout refus d'une permission, du crochet ou du classifieur | ni rejoué, ni reformulé, ni contourné ; arrêt et nœud à la mère |

## Contre-lecture

Non faite à ce brouillon : à confier à un sous-agent neuf, d'un autre modèle que l'autrice, avec les fichiers à lire nommés (R2). Ses
remarques, et leur traitement, iront ici avec l'empreinte du brouillon relu et celle de son rapport, avant le scellement.
