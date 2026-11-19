# Plan de lecture de la tranche de l'ajustement de nos lentilles (B-β) de la lecture par lentille neuronale (« Neuron Lens », Llama 3.1 8B Instruct) — v1

- Heure (UTC, `date -u`) : relevé à l'ouverture du travail **2026-11-19 07:19:19 UTC** ; relevé à l'écriture de ce plan **2026-11-19 07:21:45 UTC**.
- Écrit et scellé **avant d'ouvrir le moindre résultat** de la course `20261118-164930-neuron-lens-b-beta` (phase 1 du mandat de
  lecture ; la phase 2, lecture, viendra après contre-lecture de ce plan par un autre lecteur neuf).
- Lecteur : sous-agent neuf (modèle servi : Opus 5.5, `claude-opus-5-5`), lancé par la session `session_013QMaykLXtozHttcSQ4ke1s`,
  branche `claude/brave-galileo-jhp684`, tête `8845ea8c2a9f0336f73ffbf800fed23990e4a517`. Il n'a écrit ni le texte gelé, ni son
  addendum, ni le code des verdicts, ni le code de course, ni les commandes, ni la course.
- Règle suivie (texte gelé, § P.7) : « Les résultats sont lus par un lecteur neuf, sur un plan de lecture scellé avant toute ouverture
  des résultats ; […] Le lecteur applique ce texte aux sorties versées (P.6) et compare son verdict à celui du fichier des verdicts : un
  désaccord est rapporté et tranché par un second lecteur neuf, sans nouvelle mesure. »
- Le lecteur applique les critères gelés tels qu'ils sont écrits ; il **n'arbitre aucune ambiguïté** : il la signale (section 4) et
  donne, si le cas se présente, le verdict sous chacune des lectures.

## 1. Ce que j'ai lu avant ce plan, et ce que je sais déjà

### 1.1 Pièces lues (empreintes SHA-256 recalculées le 2026-11-19 vers 07:19 UTC)
| pièce | lue | empreinte recalculée | compagnon |
|---|---|---|---|
| texte gelé `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` | en entier (667 lignes) | `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` | égale (et égale à l'attendue du mandat) |
| addendum `docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md` | en entier | `bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1` | égale |
| code des verdicts de la course `src/controle_ia/neuron_lens/verdicts_b_beta_v4.py` | en entier, **pour les noms de clés seulement** (permis par le mandat) | `8c07434f9db0e35e10eb806218da320bc0d6e404e41c4f60c495b35906d88b87` | égale |
| modèle de forme `docs/notes/neuron-lens-v1/lecture-b-alpha/plan-de-lecture-v1.md` | en entier | `5a79991850459ca13469edbd51e91619b50c23fe80085cc1a9e17ff217d831da` | égale |

**Déclaration sur le code des verdicts** (R4) : je l'ai lu en phase 1, comme le mandat le permet. Il porte des lectures du texte (bande
partielle, témoin compté sur les couches lisibles, arrondi des différences, moitiés soumises à la garde du témoin, `n` indépendant de la
lentille, règle (b) écrite comme « n < 32 ») ; je les ai **reportées comme ambiguïtés** (section 4) et non comme règles. En phase 2, je
ne le relis pas et je ne l'importe pas : mon calcul est écrit à partir des seules règles recopiées en section 3.

**Empreintes seulement, sans ouverture du contenu** (pièces d'entrée nommées par le texte gelé, hors des dossiers interdits) :
- série repère de la lentille R publique, `diag/20261117-015632-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json` (présente
  sur la branche de travail) : `bd57d519a24e5227df2c2d720ba33a54f47653d0741acbb51f1781b59df33073`, **égale** à l'empreinte du texte gelé ;
- références publiées de Qwen3-8B, `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json`
  `8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3` et `reads_at_firings_qwen3-8b.json`
  `ac0bf101e341385a400bbecb751f9720428da1d0bd09a752c8337dd84ba182cd`, **égales** au texte gelé (pour mémoire : je n'en ai pas besoin
  pour les verdicts).

**Noms de fichiers seulement** (`find -type f`, aucun contenu, aucune empreinte calculée) : `diag/20261118-164930-neuron-lens-b-beta/`
(50 fichiers et 50 compagnons `.sha256`, dont `journaux/` : 16 journaux d'étape ; `artefacts-garde-d/` : 2 essais artefacts) et
`runs/20261118-164930-neuron-lens-b-beta/` (`manifeste.json` et son compagnon). Fichiers de résultats d'étape `b-beta-*.json` : 23
(ajustement-R, ajustement-S, b0, banc, comptes-jetons, corpus-activations, corpus-ajustement, declencheurs, export, fumee, grandeurs,
lens-compare, measure, partie2-b0, partie2-corpus, passe, pilotes, preparer, reads, score, telecharger-poids, telecharger-tokeniseur,
verdicts) ; autres : `addendum-partie2-b-beta-v1-b0.md`, `addendum-partie2-b-beta-v1-corpus.md`,
`causal_lens_b-beta_llama-3.1-8b-instruct.json` et `.log`, `grandeurs-par-pole-b-beta-v1.json`, `intervalles-b-beta-v1.json`,
`lens_compare-b-beta-v1.json`, `reads_at_firings_llama-3.1-8b-instruct.json`, `verdicts-b-beta-v1.json`. **Aucun** fichier dont le nom
désigne un audit (A1 à A5), une relance à la graine 1 (`b-beta-graine1`) ou un arrêt. Le décompte des compagnons est cohérent avec ce
qu'on m'a déclaré : 50 − 16 − 2 = 32 dans `diag/`, plus celui du manifeste = 33.

### 1.2 Ce que je sais déjà d'un résultat (déclaré par la session qui me lance, recopié)
La course s'est terminée normalement (« fin : course terminee ») le **2026-11-19 à 05:31:55 UTC** ; l'état final porte `exclus=0` et la
liste des étapes faites suivante : `ajustement-R ajustement-S b0 banc comptes-jetons corpus-activations corpus-ajustement declencheurs
export fumee grandeurs lens-compare measure partie2-b0 partie2-corpus passe pilotes preparer reads score telecharger-poids
telecharger-tokeniseur verdicts` — elle ne contient **ni `audits-controles` ni `audit-relance`** ; aucun arrêt n'a été écrit ; un fichier
de verdicts existe. Durées : ajustement de R ≈ 5 h 07, ajustement de S ≈ 5 h 01. À la récupération : 23 fichiers de résultats d'étape
vérifiés contre leur manifeste, 33 compagnons vérifiés ; compagnons posés après coup sur les 16 journaux d'étape et 2 artefacts de la
garde (d). **Je ne connais aucune valeur de mesure ni aucun verdict.**

Ce que ce renseignement laisse ouvert, sans que je le tranche : l'absence des étapes d'audit est compatible avec « aucun audit A1 à A5
déclenché » comme avec « audit déclenché mais non joué ». Je calcule moi-même les déclencheurs (étape 3 ci-dessous) avant de lire ce que
la course en a écrit. Aucune règle ci-dessous n'a été choisie en vue de ce renseignement.

## 2. Ordre de lecture des pièces (phase 2)

Toutes les lectures se font dans le dépôt de travail, branche de travail, sur les copies versées ; aucun modèle, aucune machine. Les
pièces hors de `diag/` et `runs/` qui m'étaient interdites en phase 1 (`docs/notes/neuron-lens-v1/etat-final-course-b-beta-v1.txt`,
`docs/notes/neuron-lens-v1/controles-b-beta-v1.log`) ne sont lues en phase 2 que si le mandat de phase 2 les autorise, et alors à
l'étape 1, après les empreintes ; la branche `calcul/neuron-lens-b-beta-v1` n'est pas lue sauf autorisation écrite du mandat de phase 2.

**Exposition involontaire** : si une pièce lue avant l'étape 6 (manifeste, résultat d'étape, journal) porte un verdict, un déclencheur
ou une issue d'audit écrits par la course, je le déclare dans le rendu (pièce, champ, moment de lecture) ; mon calcul ne s'y réfère pas.

**Étape 0 — ce plan et le texte.** Vérifier l'empreinte de ce plan (compagnon) et celle du texte gelé (`f5d46860…`). Un écart : arrêt.

**Étape 1 — empreintes.**
1. `sha256sum -c` de chaque compagnon de `diag/20261118-164930-neuron-lens-b-beta/` (50) et de `runs/…/manifeste.json`. Une empreinte
   fausse : je le dis, la pièce n'est pas lue pour un verdict, et je rapporte quelles règles en dépendaient.
2. Lire le manifeste : comparer chaque empreinte qu'il porte à celle du fichier versé ; relever le commit du code de course, les
   versions (§ 5 de l'addendum : python 3.12.16, torch 2.14.1, transformers 5.18.0, tokenizers 0.23.2, huggingface_hub 1.33.0,
   datasets 5.2.0, numpy 2.4.6, pyarrow 26.0.1, safetensors 0.8.0, Drowse 6.1.4), les graines (P.5 :
   `SeedSequence(entropy=20261118)`, branche « B-β »), la carte, le lot de `measure` (64 exigé).
3. Les 16 journaux et les 2 artefacts de la garde (d) ont reçu leur compagnon **après coup** : leur empreinte n'atteste que l'intégrité
   depuis la récupération ; je le dis, et je compare à l'empreinte du manifeste s'il les liste.
4. Confronter la liste des fichiers versés à la liste de P.6 ; toute sortie de P.6 absente est nommée.

**Étape 2 — ce qui décide d'une chaîne en défaut** (rang 1 ; prime sur tout). Ordre des étapes de la course :
1. Montage : `b-beta-preparer.json`, `b-beta-telecharger-tokeniseur.json` (+ journal), `b-beta-telecharger-poids.json`,
   `b-beta-b0.json` (+ journal) : garde (d) (essais des correctifs (1) à (6) employés, essais du dépôt sur le Qwen3 miniature, crochets
   de `causal_lens.py` sur un Llama miniature, aucun test sauté), garde (f) (estimateur sur Llama miniature, `atol = 1e-4`), garde (e)
   à B0 (trois fichiers de Neuronpedia : 31 couches contiguës, aucune matrice identité aux couches 0 à 27), contrôles de P.1 (932
   documents, moitiés 466 et 466, `rows_sha256` `a6afd972…`), Drowse 6.1.4 d'empreinte `673ed2b4…`, essais du code des verdicts (P.4) s'ils
   sont versés ; puis `artefacts-garde-d/` (les deux artefacts doivent avoir fait échouer la garde (d)) ;
   `b-beta-partie2-b0.json` et `addendum-partie2-b-beta-v1-b0.md` comparés à la partie 1 (empreintes du modèle, tokeniseur `79e3e522…`,
   lentilles J `d5300a15…`, J++ `8bd04f48…`, R publique `a63a1588…`, versions) ; `b-beta-banc.json` (+ journal) : second document
   ≤ 23,6 s (compte rendu au-delà de 14,2 s) ; `b-beta-corpus-ajustement.json` (+ journal) : garde (i) avant l'ajustement.
2. Ajustement : `b-beta-ajustement-R.json`, `b-beta-ajustement-S.json` (+ journaux) : garde (q) (avant le premier lancement et avant
   toute relance), garde (g) (466 et 466, `next_doc` = `meta["docs"]`, longueurs 128, `rows_sha256`, `full_length`, différences et
   matrices finies), garde (h) pour S (première dimension 32 par cible), empreinte de fin de chaque fichier d'ajustement.
3. Export : `b-beta-export.json` (+ journal) : gardes (e) (identité, couches 0 à 27), (h) (31 couches `out`, 32 `mid`), (n) (égalité à
   la lentille R publique, couches 0 à 27, ou empreintes égales), (o) (aller-retour des trois noms, `None`, écart relatif de Frobenius
   ≤ 10⁻³ aux couches 0 à 30).
4. Corpus d'activations et jetons : `b-beta-corpus-activations.json` (garde (i) après `05`), `b-beta-comptes-jetons.json`,
   `b-beta-partie2-corpus.json` et `addendum-partie2-b-beta-v1-corpus.md` (comparés à l'addendum, § 3 : fichiers `act-dclm.jsonl`
   `64657ecb…`, `act-zh.jsonl` `c3202db1…`, `act-code.jsonl` `550944a2…`, `act-chat-llama-3.1-8b-instruct.jsonl` `9dbf9f44…` ; jetons
   gardés 89 498, `c37186ad…`).
5. `b-beta-lens-compare.json` (+ journal) : garde (r) avant `lens_compare.py`.
6. `b-beta-fumee.json`, `b-beta-passe.json`, `b-beta-pilotes.json` (+ journaux) : garde (k) (`hub` juste avant chaque étape, message du
   correctif (1) dans le journal de la passe), garde (r), fumée réussie (garde (d)), garde (p) pour les pilotes (4, 2 et 2 documents).
7. `b-beta-measure.json` (+ journal) : garde (i) avant `measure`, garde (p) (16 contextes), lot 64.
8. Sortie de `score` : `causal_lens_b-beta_llama-3.1-8b-instruct.json` (+ `.log`), `b-beta-score.json` (+ journal) ;
   `b-beta-grandeurs.json` et `grandeurs-par-pole-b-beta-v1.json` (n recalculé, pôles écartés par motif). **J'évalue moi-même** sur ces
   pièces les gardes (a), (b), (c), la part « `score` » de (e), et (j) (contre la série repère `bd57d519…`).
9. `b-beta-reads.json` (+ journal) : garde (k) (nos deux noms, fichiers liés d'empreinte égale à celle de fin d'ajustement), (r), (s).
Pour chaque garde constatée sur la machine, je relève la valeur écrite, son moment, et la preuve que son essai (cas sain, artefact) a eu
lieu ; une garde dont aucune trace n'est versée est dite « non constatable sur pièces » (section 4, ambiguïté 15).

**Étape 3 — audits : déclenchés ou non, et leur issue.** Je lis les valeurs nécessaires aux déclencheurs (sortie de `score`, notre R :
« steer 1x » couches 0 à 27, « ablate win » couches 8 à 15 et 26 à 29 avec n ; différences entre moitiés et accords de B-1 ; `read_S`
des 32 couches) et **je calcule moi-même** A1 à A6. Je cherche ensuite, dans les pièces versées hors des fichiers de verdicts, toute
sortie d'audit (aucun nom de fichier n'en désigne ; je le vérifie dans le contenu de `b-beta-measure.json`, `b-beta-score.json` et des
journaux). Je ne lis `b-beta-declencheurs.json` qu'à l'étape 6, avec les verdicts de la course.

**Étape 4 — mesures B-1 à B-7.** B-1 : différences entre moitiés non arrondies (R `out` 0 à 30, R `mid` 0 à 31, S `mid` et `out` 0 à 31)
et accord du premier jeton entre moitiés paire et impaire (`lens_compare-b-beta-v1.json`, couches 2, 7, 12, 18, 23, 28) ; B-2, B-3, B-4,
B-6, B-7 : sortie JSON de `score` (valeurs telles qu'écrites) et n ; B-5 : `reads_at_firings_llama-3.1-8b-instruct.json` (`read_S`,
`silent`, `read_S_net`) ; intervalles (`intervalles-b-beta-v1.json`), rapportés sans servir au verdict. Les valeurs imprimées à deux
décimales par `02_fit.py` et `04_export_rlens.py` sont relevées pour mémoire et jamais lues pour un seuil.

**Étape 5 — mon calcul des verdicts.** Un script écrit par moi (`docs/notes/neuron-lens-v1/lecture-b-beta/calcul-verdicts-b-beta-v1.py`,
scellé avec sa sortie), en Python sur le processeur, lisant les pièces versées par `json` ; il **n'importe ni ne relit** aucun code des
verdicts de la course (`controle_ia.neuron_lens.verdicts_*`) ; il calcule, pour chaque ambiguïté de la section 4 qui se présente, le
verdict sous chaque lecture. Je l'essaie d'abord (R5) sur un cas sain et un artefact faits à la main (par exemple : une table où toutes
les conditions de « reproduit » sont tenues ; la même avec un `control_med` à 0,20 à la couche 10, qui doit donner la chaîne en défaut
(a)).

**Étape 6 — seulement ensuite**, `verdicts-b-beta-v1.json` (le fichier des verdicts), `b-beta-verdicts.json` et `b-beta-declencheurs.json`,
pour comparaison : verdict d'ensemble, verdict de chaque mesure, défauts, audits et leur issue, réserves, écarts de B-4. Tout désaccord
est rapporté tel quel, sans retouche de mon calcul ; il est tranché par un second lecteur neuf, sans nouvelle mesure (P.7).

**Étape 7 — rendu.** Un fichier `verdict-lecture-b-beta-v1.md` dans ce dossier, scellé : verdict d'abord, puis pièces et empreintes,
gardes, audits, mesures, prédictions de l'autrice (réfutées ou non, sans effet sur les verdicts), ambiguïtés rencontrées et verdict sous
chaque lecture, comparaison au fichier des verdicts.

## 3. Règles que j'applique (recopiées du texte gelé ; aucune règle nouvelle)

### 3.1 Commun (« Métrique », M.1 ; « Seuil »)
- Valeurs comparées : celles de `score` telles qu'écrites dans son JSON (4 décimales) ; celles de B-1 et de B-5, non arrondies ;
  « au-dessus » = strictement. Verdicts sur les valeurs ponctuelles ; intervalles rapportés.
- Cibles : « steer 1x » (B-2, B-3, B-4, B-6) ; « ablate win » (B-7) ; « steer 4x » et « ablate pos » rapportées sans critère.
- **Couche lisible** : n ≥ 48 pour la cible considérée (n recalculé par notre code depuis le fichier `-causal.pt`, par la règle de
  `score` ; je ne peux pas le recalculer, ce fichier n'étant pas versé : je prends le n écrit et je le dis). Une bande dont plus du quart
  des couches est non lisible rend la mesure « partielle » pour cette bande.
- « Reproduit » exige la condition à **chaque couche lisible** de la bande ; « plus de N des couches » se lit « plus de la moitié des
  couches lisibles de la bande nommée ».
- **Couche 31** : notre R y est exactement la lentille des logits ; ce n'est pas une mesure de lentille. Les couches 28 à 31 ne comptent
  pour aucun verdict de B-2 ni B-3.
- Toute mesure ni « reproduit » ni « non reproduit » est « autre ».

### 3.2 Seuils (table « Seuil »)
- **B-1** — « reproduit » : différence entre moitiés ≤ 0,10 à chaque couche et chaque cible des deux lentilles (R : `out` 0 à 30, `mid` 0
  à 31 ; S : `mid` et `out` 0 à 31) **et** accord du premier jeton ≥ 0,80 aux six couches lues (2, 7, 12, 18, 23, 28). « Non
  reproduit » : une couche d'une cible à plus de 0,20, **ou** un accord sous 0,60 à l'une des six couches. Accord : part des 28 672
  pôles dont la lecture de l'écriture par la lentille R de la moitié paire et par celle de la moitié impaire a le même premier jeton,
  cible `out`, valeur non arrondie écrite par le correctif (4).
- **B-2** (notre R, « steer 1x ») — « reproduit » : `r_med` ≥ 0,40 (8–15), ≥ 0,60 (16–23), ≥ 0,85 (24–27) ; `pass` ≥ 0,90 (8–27) ;
  témoin : `control_med` hors de ±0,05 à au plus une couche de 0 à 27, à aucune hors de ±0,10. « Non reproduit » : `pass` < 0,50 à
  plus de 6 des 12 couches 16–27, ou `r_med` < 0,30 à plus de 4 des 8 couches 16–23 (lus « plus de la moitié des couches lisibles »).
- **B-3** — « reproduit » : `r_med`(notre R) − `r_med`(logits) ≥ +0,20 à chaque couche 4–15. « Non reproduit » : écart ≤ 0 à plus de 6
  des 12 couches 4–15 (même lecture).
- **B-4** — rapportée, non décisive : notre R − J et notre R − `npJpp`, couches 4–23, en deux lignes.
- **B-5** — `read_S` (définition de M.2 ; part des pôles de q ≤ 0,05 sur tous les pôles de la couche). « Reproduit » : `read_S` ≥ 0,60
  à la couche 0 **et** moyenne de `read_S` sur les couches 1 à 7 au moins 0,10 au-dessus de sa moyenne sur les couches 12 à 23 ; B-5
  lisible. « Non reproduit » : `read_S` < 0,30 à la couche 0, **ou** moyenne sur 1 à 7 au plus égale à la moyenne sur 12 à 23 ; B-5
  lisible. **Lisibilité** : B-5 est « non lisible » (donc « partiel », jamais « reproduit » ni « non reproduit ») si la part silencieuse
  dépasse 0,40 à la couche 0, ou si sa moyenne sur les couches 1 à 7 dépasse 0,50. Rapportés : part silencieuse, `read_S_net`,
  `read_S / (1 − silent)`.
- **B-6** — rapportée, non décisive : écart = `r_med`(notre R) − `r_med`(`npR`), « steer 1x », couches 0 à 27 ; « accord » si l'écart
  absolu est ≤ 0,05 à au moins 21 des 28 couches 0 à 27 **et** ≤ 0,15 à toutes ; « désaccord » s'il dépasse 0,15 à au moins une
  couche ; « intermédiaire » sinon.
- **B-7** (« ablate win », notre R) — « reproduit » : `r_med` < 0,25 à chaque couche 0–15 **et** ≥ 0,50 à chaque couche 26–29. « Non
  reproduit » : `r_med` ≥ 0,40 à plus de 4 des 8 couches 8–15 (**par le haut**), ou < 0,30 à plus de 2 des 4 couches 26–29 (**par le
  bas**) (même lecture « plus de la moitié des lisibles »).

### 3.3 Chaîne en défaut (« Seuil », conditions (a) à (s), recopiées)
- (a) `control_med` hors de ±0,10 à une couche de 0 à 27, pour l'une des quatre cibles et l'une des lentilles notées ;
- (b) pilotage sans effet : à une couche de 0 à 27, plus de la moitié des 64 pôles écartés par `score` pour effet nul en « steer 1x » ;
- (c) lentille des logits, `r_med` (« steer 1x ») < 0,80 à l'une des couches 28–30 ; `npR`, < 0,85 à l'une des couches 28–30 ; notre
  R, < 0,85 à l'une des couches 28–30 ;
- (d) essai d'un correctif employé ((1) à (6)) ou de l'estimateur sur le Qwen3 miniature avec un test sauté ou en échec ; fumée de la
  passe en échec ; essai des crochets de pilotage et d'ablation sur un Llama miniature en échec (un échec d'accès au tokeniseur ou aux
  poids est un arrêt de montage, pas une chaîne en défaut) ;
- (e) repli sur les logits : pour `J`, `npJpp`, `npR` ou notre R, |`r_med`(lentille) − `r_med`(logits)| < 10⁻³ à une couche de 0 à 23
  (« steer 1x »), ou une matrice égale à l'identité (écart maximal ≤ 10⁻⁶, float32) à une couche de 0 à 27 (à B0 pour Neuronpedia,
  après l'export et avant `score` pour notre R) ;
- (f) essai de l'estimateur sur un Llama miniature contre la force brute en échec (`atol = 1e-4`) ;
- (g) ajustement incomplet, vide ou non fini : nombre de documents par moitié ≠ 466 et 466 ; `next_doc` ≠ `meta["docs"]` ; un document
  de longueur autre que 128 ; `rows_sha256` ≠ `a6afd972eeaa3566a28d07216efaf75624fda20293c5fab3b7af39277aaf93b3` ; `full_length` ≠
  vrai ; une différence entre moitiés non finie ; une matrice non finie ;
- (h) notre R : nombre de couches exportées ≠ 31 (`out`) ou ≠ 32 (`mid`) ; notre S : première dimension des sommes ≠ 32 pour chaque
  cible ;
- (i) corpus partagé : identifiant d'ajustement présent dans la tranche DCLM du corpus d'activations ; révision, liste ordonnée
  d'identifiants ou `skip` différents de la provenance publiée (`16957c52…` : `[0, 1000)` ; `a26a7077…` : `skip` 1 000, `n` 40 000) ;
  texte entier commun (empreintes) ; aux trois moments (avant l'ajustement, après `05`, avant `measure`) ;
- (j) `r_med`(`npR`, « steer 1x ») de cette course écarté de la série repère (`bd57d519…`) de plus de 0,05 à plus de 2 des 28 couches 0
  à 27, ou de plus de 0,10 à l'une d'elles ;
- (k) `arch.fits(MODEL)` : `hub` juste avant la fumée, la passe d'activations et `07_drivers.py` ; nos deux noms juste avant
  `reads_at_firings.py`, fichiers liés d'empreintes égales à celles de fin d'ajustement ; tout autre cas ;
- (l) témoin ou pilotage dégénéré constaté par A1 ou A5, ou l'une des gardes (a) à (c) manquée sur la sortie de `score` de la graine 1 ;
- (m) appariement dégénéré de B-5, constaté par A4 ;
- (n) une matrice de notre R égale à celle de `npR` (écart maximal ≤ 10⁻⁶, float32) à une couche de 0 à 27, ou fichiers d'empreinte
  égale ;
- (o) `load_lens` de `R:dclm-llama`, `-even` ou `-odd` lève une erreur, rend `None` à une couche de 0 à 30, ou s'écarte de la moyenne du
  fichier d'ajustement de plus de 10⁻³ en écart relatif de Frobenius à une couche de 0 à 30 ;
- (p) `measure` avec un nombre de contextes ≠ 16 ; `07_drivers.py` avec moins de 4, 2 et 2 documents par tranche ;
- (q) banc dans une copie à part ; aucun fichier `-T128` avant le premier lancement ; avant toute relance, point de sauvegarde à
  `rows_sha256` = `a6afd972…`, `full_length` vrai, lentille et modèle attendus ;
- (r) empreinte de `kept()` différente, avant `06_activations.py`, `lens_compare.py`, `07_drivers.py` ou `reads_at_firings.py`, de celle
  consignée après l'unique `03_token_counts.py` ;
- (s) avant `reads_at_firings.py`, un fichier `data/checks/reads_at_firings-*.pt` ou un résumé existe déjà.

### 3.4 Verdict d'ensemble (« Critères de lecture gelés »), un seul, par rang
| rang | issue | verdict |
|---|---|---|
| 1 | une chaîne en défaut ((a) à (s)) | **chaîne en défaut** ; aucun verdict de mesure ; nœud à la mère |
| 2 | un audit déclenché qui porte sur B-1, B-2, B-3 ou B-5 n'a pas pu être joué jusqu'à son issue avant la destruction (temps réservé épuisé, garde de dépense, perte de machine) | **non conclu** ; les mesures non touchées sont rapportées telles quelles |
| 3 | B-2 ou B-3 « non reproduit » | **non reproduit avec nos lentilles** ; garde (j) tenue : réserve « défaut dans notre lentille » écrite dès qu'une seule des deux mesures est « non reproduit », lue avec B-6 |
| 4 | B-1, B-2, B-3 et B-5 « reproduit » | **reproduit avec nos lentilles** |
| 5 | autre | **partiel**, mesure par mesure |
B-4 et B-6 n'entrent pas dans le verdict d'ensemble ; B-7 se lit à part. Un « reproduit » dit que la lentille lit ce qu'une direction
pousse en moyenne, pas qu'elle nomme le concept d'une invite donnée.

### 3.5 B-6 et l'audit des deux codes (A6)
« Accord » : les deux codes s'accordent ; « intermédiaire » : rapporté ; « désaccord » déclenche A6, joué sur les sorties de `score`
déjà calculées (moitiés notées) : si, à chaque couche de 0 à 27 où l'écart dépasse 0,15, les deux moitiés sont toutes deux à moins de
0,05 de notre R entière → réserve « écart de corpus » ; sinon réserve « écart d'ajustement ». Aucun verdict n'est suspendu ni changé ;
la réserve accompagne le verdict d'ensemble.

### 3.6 B-7, pour un moniteur
« Reproduit » : là où `r_med` est bas, une étiquette de neurone décrit une poussée moyenne et ne sert pas à lire un épisode, avec notre
lentille comme avec la publique. « Non reproduit » par le haut : audit A5 ; s'il confirme, rapporté comme lecture valable en contexte plus
tôt que publié ; sinon B-7 « autre ». « Non reproduit » par le bas : rapporté (la lecture ne dit pas ce qu'une activation fait, même
tard). Autre : couche par couche. B-7 n'entre pas dans le verdict d'ensemble.

### 3.7 Audits symétriques : déclencheurs et issues (recopiés)
- **A1, trop beau, lecture contre pilotage** — déclencheur : notre R, « steer 1x » : `r_med` ≥ 0,95 à une couche 0–7, ou `control_med`
  écrit égal à 0 (`0.0` ou `-0.0`, à 4 décimales) à au moins 2 couches de 0 à 27. Issue : contrôle (1) ou (2) manqué, ou garde (a) à
  (c) manquée sous la graine 1 → chaîne en défaut (l) ; sinon verdicts de la graine 0 tenus, sauf toute mesure parmi B-2, B-3, B-7 dont
  le verdict diffère sous la graine 1, qui devient « autre ».
- **A2, trop beau, stabilité** — déclencheur : différence entre moitiés non arrondie < 10⁻⁶ à une couche d'une cible, ou accord du
  premier jeton égal à 1 aux six couches. Issue : un contrôle manqué (466 et 466 ; empreintes des moitiés `4a31baec…`, `ef95a60c…` ;
  sommes des moitiés différentes ; exports des moitiés d'empreintes différentes) → chaîne en défaut (g) ; sinon B-1 tient.
- **A3, tout négatif, stabilité** — déclencheur : B-1 « non reproduit ». Issue : mêmes contrôles que A2 plus chaque document de 128
  jetons et `full_length` vrai ; un contrôle manqué → (g) ; sinon « non reproduit » tient.
- **A4, B-5 aux extrêmes** — déclencheur : `read_S` ≥ 0,99 à la couche 0, ou `read_S` = 0 à toutes les couches 0 à 31. Issue :
  permutation non dégénérée (au plus 10 points fixes par couche) et fichier de lentille S égal à celui de l'ajustement ; un contrôle
  manqué → (m) ou (k) ; sinon B-5 tient telle que calculée.
- **A5, B-7 par le haut** — déclencheur : B-7 « non reproduit » par le haut. Issue : contrôle manqué → (l) ; graine 1 aussi « par le
  haut » → maintenu ; sinon B-7 « autre ».
- **A6** — ci-dessus (3.5).
- **Tout négatif, reproduction** — déclencheur : B-2 ou B-3 « non reproduit » ; aucun calcul neuf : (j) manquée → chaîne en défaut ;
  (j) tenue → rang 3 et sa réserve.
- Audit non joué (temps réservé d'une heure ou garde de dépense) : issue « non joué », règle du rang 2 ; s'il porte sur B-7 seul : B-7
  « autre ». A1 et A5 partagent une seule relance à la graine 1.

### 3.8 Prédictions de l'autrice (rapportées, sans effet sur les verdicts)
Je rapporte, pour chaque ligne de la table « Prédiction chiffrée et signe attendu », si la condition « réfutée si » est remplie, telle
qu'écrite (B-1 ; B-2 ; B-3 ; B-4 face à J et face à J++ ; B-5 ; B-6 ; B-7 ; verdict d'ensemble modal « partiel »).

## 4. Ambiguïtés vues avant lecture (non arbitrées ; verdict donné sous chaque lecture si le cas se présente)

1. **Bande partielle et « non reproduit »** : le texte dit qu'une bande partielle rend la mesure « partielle » pour cette bande, sans dire
   si une clause « non reproduit » s'y juge. L'addendum (§ 1.1, lecture 1, décidée par la mère, R-3190) dit qu'elle ne s'y juge pas
   (mesure « autre »). Lectures : (i) addendum ; (ii) clause jugée sur les couches lisibles malgré la bande partielle.
2. **Bande partielle et « reproduit »** : même silence ; lectures : (i) « reproduit » impossible sur une bande partielle (mesure
   « autre ») ; (ii) « reproduit » prononçable sur les couches lisibles, avec la mention « partielle ».
3. **Bande sans aucune couche lisible** : « chaque couche lisible » serait vrai à vide ; je la signale comme non jugeable et donne le
   verdict avec « reproduit » vrai et faux pour cette bande.
4. **Témoin de B-2 et couches non lisibles** : la clause porte sur « une couche de 0 à 27 » sans « lisible ». Lectures : (i) couches
   lisibles seules (addendum, lecture 2) ; (ii) toutes les couches 0 à 27.
5. **Garde (a) et lentilles des moitiés** : « l'une des lentilles notées » ; les moitiés sont notées par `score` « pour l'audit des deux
   codes seulement ». Lectures : (i) moitiés comprises (addendum, lecture 3) ; (ii) moitiés exclues.
6. **Différences de deux valeurs écrites à 4 décimales** (B-3, B-4, B-6, A6, part « `score` » de (e), (j)) : arrondies à 4 décimales
   avant comparaison (addendum, forme) ou prises en flottant brut. Je signale toute comparaison où les deux lectures diffèrent.
7. **B-5, « au moins 0,10 au-dessus »** contre « au-dessus = strictement » : lectures ≥ 0,10 et > 0,10 (ne joue qu'à l'égalité exacte) ;
   et valeurs de B-5 prises en flottant binaire ou « telles qu'écrites » (forme décimale la plus courte) aux égalités de seuil.
8. **Garde (b)** : « plus de la moitié des 64 pôles écartés pour effet nul » ; lectures : (i) compte des pôles écartés au motif « effet
   nul » (> 32) ; (ii) n retenus < 32 tous motifs confondus. Si les motifs ne sont pas séparés dans les pièces, je le dis.
9. **n par lentille ou par cible** : M.1 range n parmi les métriques « par couche, cible et lentille ». Si les pièces portent un n par
   lentille, lectures pour B-3 (deux lentilles) : (i) n de notre R ; (ii) couche lisible pour les deux lentilles. Et si le n de la sortie
   de `score` diffère du n recalculé, lectures : (i) n recalculé (texte) ; (ii) n de `score`.
10. **Lisibilité dans les gardes et les déclencheurs** : (a), (b), (c), (e), (j), A1 et la règle de B-6 (« 21 des 28 couches ») ne
    parlent pas de lisibilité. Lecture que je prends par défaut : toutes les couches de la plage ; lecture alternative : couches lisibles
    seules ; je donne les deux si elles divergent.
11. **Rang 2 et cause de l'absence d'audit** : le rang 2 nomme trois causes (temps, dépense, perte de machine). Si mon calcul déclenche
    un audit A1 à A4 que la course n'a pas joué (aucune étape d'audit dans l'état final) parce que son code ne l'a pas déclenché,
    lectures : (i) rang 2, « non conclu » (l'audit n'a pas été joué avant la destruction) ; (ii) la liste des causes est fermée : écart du
    code de course au texte, rapporté comme désaccord, verdict de rang 3 à 5 calculé sans l'audit.
12. **Contrôles d'audit lisibles sur pièces** : si un audit A2, A3 ou A4 est déclenché et que ses contrôles figurent déjà dans les
    pièces versées (comptes, empreintes des moitiés et des exports, points fixes), lectures : (i) l'audit compte comme joué sur la
    machine ; (ii) il ne l'est pas (aucune sortie d'audit versée), rang 2. Le texte interdit tout rejeu après la destruction : je ne
    rejoue rien qui demande les lentilles.
13. **B-7 « par le haut » et « par le bas » à la fois** : les deux clauses peuvent être vraies ensemble ; je rapporte les deux lectures
    de la table « B-7, pour un moniteur » et le déclencheur A5.
14. **Rang 1 et réserves** : sous une chaîne en défaut, « aucun verdict de mesure » ; lectures : (i) B-6 et sa réserve A6 non
    rapportées ; (ii) rapportées comme information.
15. **Garde constatée sur la machine sans trace versée** : lectures : (i) tenue, sur la foi de la fin normale, de l'absence d'arrêt et
    de `exclus=0` ; (ii) non constatable, verdict rapporté avec cette réserve. Je n'en fais jamais, seul, une chaîne en défaut.
16. **Écart de la partie 2 à la partie 1 (addendum, § 3 et § 5)** : il commande un arrêt ou un nœud, non une chaîne en défaut. Si un tel
    écart apparaît et que la course a continué : lectures : (i) le verdict de mesure reste prononçable, l'écart rapporté comme réserve ;
    (ii) écart à la liste d'arrêt rendant la course hors du texte (« tout écart de notre code à ce texte, découvert en course : arrêt »),
    verdict rapporté sous réserve et soumis au second lecteur.
17. **Fichier des verdicts double** : deux pièces portent des verdicts (`verdicts-b-beta-v1.json`, nommé par P.3 étape 7 « fichier de
    verdicts unique », et `b-beta-verdicts.json`, résultat d'étape). Si elles diffèrent, je compare mon verdict à chacune et je le dis.
18. **Matériel et lot** : sur H100, l'invariance aux lots 16 et 64 n'est pas mesurée (M.1). Si le manifeste montre une autre carte
    ou un autre lot que 64, je le rapporte ; je ne peux pas en mesurer l'effet ; je signale tout verdict qui tient à une marge de
    l'ordre de 0,03 (effet du matériel mesuré entre deux cartes).

## 5. Ce que je ne fais pas
- En phase 1 : aucune ouverture, `cat`, `head`, `grep`, `python` ou empreinte sur un fichier de `diag/20261118-164930-neuron-lens-b-beta/`
  ou de `runs/20261118-164930-neuron-lens-b-beta/` (journaux et `.sha256` compris), ni sur
  `docs/notes/neuron-lens-v1/etat-final-course-b-beta-v1.txt`, ni sur `docs/notes/neuron-lens-v1/controles-b-beta-v1.log`, ni sur la
  branche `calcul/neuron-lens-b-beta-v1` ; je n'ai lu ni `verdict-b-alpha-v1.md` ni les fichiers `calcul-*` de `lecture-b-alpha/`.
- En aucune phase : aucun modèle chargé, aucune machine, aucun réseau payant ; aucun rejeu d'audit ni recalcul qui demande les lentilles
  ou le fichier `-causal.pt` ; aucun import ni relecture du code des verdicts de la course ; aucune lecture touchant P3, P3b, T0.6,
  T0.7, P3-bis ; aucune autre branche sans autorisation écrite du mandat ; aucun commit, aucun push ; aucun fichier réécrit (une
  correction = un fichier de version suivante, R12) ; aucune ambiguïté arbitrée ; aucune règle ajoutée.
