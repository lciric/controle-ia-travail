# Plan de lecture de la tranche de l'ajustement de nos lentilles (B-β) de la lecture par lentille neuronale (« Neuron Lens », Llama 3.1 8B Instruct) — v2

- Heure (UTC, `date -u`) : ouverture du travail de la v2 **2026-11-19 07:29:34 UTC** ; relevé à l'écriture de la v2 **2026-11-19 07:30:21 UTC**.
- **v2**, qui remplace la v1 (`plan-de-lecture-b-beta-v1.md`, `40128756b446301248827cc5a9facfd53baa5cf6b461a8b09731369b61208128`,
  archivée telle quelle, R12) selon sa contre-lecture par un lecteur neuf d'un autre modèle
  (`contre-lecture-plan-de-lecture-b-beta-v1.md`, `bf3e2d7572b85df806d5841a0b8a7342829893a86503738fbb153721e33ec4e7`, empreinte
  recalculée, égale au compagnon : « employable », 0 bloquante, 2 majeures, 13 mineures). Je l'ai lue en entier.
- Écrite et scellée **avant d'ouvrir le moindre résultat** de la course `20261118-164930-neuron-lens-b-beta`. Entre la v1 et la v2, je
  n'ai lu que la contre-lecture et vérifié trois lignes de l'addendum déjà lu (l. 24, 41-49) ; aucun fichier interdit n'a été ouvert.
- Lecteur : sous-agent neuf (Opus 5.5, `claude-opus-5-5`), lancé par la session `session_013QMaykLXtozHttcSQ4ke1s`, branche
  `claude/brave-galileo-jhp684`, tête `8845ea8c2a9f0336f73ffbf800fed23990e4a517`. Il n'a écrit ni le texte gelé, ni l'addendum, ni le
  code des verdicts, ni le code de course, ni les commandes, ni la course.
- Règle suivie (texte gelé, § P.7) : « Les résultats sont lus par un lecteur neuf, sur un plan de lecture scellé avant toute ouverture
  des résultats ; […] Le lecteur applique ce texte aux sorties versées (P.6) et compare son verdict à celui du fichier des verdicts : un
  désaccord est rapporté et tranché par un second lecteur neuf, sans nouvelle mesure. »
- Le lecteur applique les critères gelés, **addendum compris** (« pièce du texte gelé scellé », addendum l. 3), tels qu'ils sont écrits.
  Là où le texte ou l'addendum tranche, cette lecture porte **le** verdict comparé au fichier des verdicts. Là où rien ne tranche, il
  n'arbitre pas : il signale l'ambiguïté (section 4) et donne le verdict sous chaque lecture.

## 0. Différences avec la v1 et traitement de la contre-lecture

### 0.1 Majeures
| remarque | traitement | lieu |
|---|---|---|
| **M-1** (cinq ambiguïtés déjà tranchées par l'addendum ; un seul verdict du lecteur) | **acceptée**. Vérifié moi-même dans l'addendum : n° 1 de la v1 (clause « non reproduit » non jugée sur une bande partielle : l. 24-25), n° 4 (témoin de B-2 sur les couches lisibles : l. 41-42), n° 5 (garde (a) étendue aux moitiés : l. 45-46), n° 6 (différences arrondies à 4 décimales : l. 47-48), n° 7 seconde moitié (lecture côté entrée prise telle qu'écrite, moyennes en fractions exactes : l. 48-49). Pour ces cinq points la lecture de l'addendum **porte le verdict comparé** ; la lecture littérale est rapportée comme information, avec les effets déclarés par l'addendum (l. 26-40, 42-44, 46). Première moitié de la n° 7 : **tranchée par le texte**, ≥ 0,10 (mineure 1) | 3.0 (règles en vigueur), 4.1 (tranchées), 4.2 (ouvertes) |
| **M-2** (gardes recalculables calculées avant de lire celles que la course a écrites) | **acceptée**. Ordre refait : toutes les pièces sont classées en « sorties brutes » et « pièces portant gardes, déclencheurs, issues ou verdicts » (2.1) ; je calcule et **consigne** (fichier scellé) les gardes (a), (b), (c), part « `score` » de (e), (j) et les déclencheurs A1 à A6 sur les sorties brutes **avant** d'ouvrir toute pièce de la seconde catégorie ; les grandeurs qui ne se calculent pas sur les sorties brutes sont nommées, avec la pièce de la course où je les lis, en le déclarant (2.2) | 2.1 à 2.3 |

### 0.2 Mineures (13 faites, 0 refusée)
| n° | remarque | traitement | lieu |
|---|---|---|---|
| 1 | « au moins 0,10 au-dessus » tranché (≥) | faite : ≥ 0,10 porte le verdict ; > 0,10 n'est plus une lecture | 3.2 (B-5), 4.1 (T-5) |
| 2 | ambiguïté 2 orientée par le texte | faite : gardée ouverte, avec la mention que la lecture (i) est la plus proche du texte | 4.2 (O-1) |
| 3 | ambiguïté 3 = bande partielle | faite : fondue dans T-1 et O-1 | 4.1, 4.2 |
| 4 | ambiguïté 8 : la lettre est (i) ; une divergence est un écart du code au texte | faite : les deux lectures gardées ; dit que (i) est la lettre ; toute divergence rapportée au second lecteur comme écart possible du code au texte (liste d'arrêt, l. 547) ; de même pour n indépendant de la lentille | 4.2 (O-2, O-3) |
| 5 | ambiguïtés 16 et 17 tranchées en partie | faite : 17 fermée (le fichier des verdicts au sens du texte est `verdicts-b-beta-v1.json`, comparaison principale à lui ; `b-beta-verdicts.json` comparé à côté) ; 16 réduite au cas « la course a continué » | 4.1 (T-6), 4.2 (O-8) |
| 6 | ambiguïtés 9 à 15 et 18 | faite : n° 15, la lecture « non constatable » dite la plus proche du texte (sorties versées) ; n° 18 reclassée en réserve | 4.2 (O-7), 4.3 |
| 7 | garde (j) et la règle « plus de N des couches » | faite : écrit que (j) (« plus de 2 des 28 ») et B-6 (« au moins 21 des 28 ») se lisent à la lettre, la règle de conversion valant pour les clauses de la table des seuils | 3.1, 3.3 (j) |
| 8 | « notre R » dans (c) et (e) | faite : ambiguïté ajoutée ; lettre = lentille entière | 4.2 (O-9) |
| 9 | copies omises | faite : rang 2 complet ; moments de (n) et (o) ; contrôles (1) et (2) de A1 ; « règle de lisibilité comprise » à A4 | 3.3, 3.4, 3.7 |
| 10 | grandeurs à rapporter | faite : recouvrement des dix premiers jetons, accord de chaque moitié avec la lentille R publique, compte et rang du jeton de début, mentions « hors programme » et « aucune correction pour comparaisons multiples » | 2.4, 2.7 |
| 11 | arrêts de montage rangés sous les chaînes en défaut | faite : séparés ; un manquement y est un écart à la liste d'arrêt, non le rang 1 | 2.5, 3.8 |
| 12 | essai du script sur les cas gelés de P.4 | faite : rejoués sur le processeur avec les références publiées empreintées, avant toute ouverture d'une pièce de la course | 2.3, étape A |
| 13 | empreinte de l'addendum à l'étape 0 | faite ; la remarque sur l'indépendance (lecture du code en phase 1) est reprise en 1.1, sans autre changement | 2.3, étape 0 ; 1.1 |

### 0.3 Autres différences avec la v1
- Ajout d'une procédure d'ouverture « structure d'abord » des pièces (2.2) pour extraire des seules valeurs de mesure d'une pièce de la
  seconde catégorie avant de lire ses gardes.
- La lecture du manifeste passe après mes calculs consignés (il peut porter des résultats) ; l'étape 1 de la v1 n'y garde que
  `sha256sum -c` sur les compagnons.
- Numérotation des ambiguïtés refaite : T-n (tranchées), O-n (ouvertes), R-n (réserves). Table de correspondance en 4.4.
- Aucune règle, aucun seuil, aucune issue ajoutés ou changés.

## 1. Ce que j'ai lu avant ce plan, et ce que je sais déjà

### 1.1 Pièces lues (empreintes SHA-256 recalculées)
| pièce | lue | empreinte recalculée | compagnon |
|---|---|---|---|
| texte gelé `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` | en entier | `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` | égale (et égale à l'attendue) |
| addendum `docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md` | en entier | `bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1` | égale |
| code des verdicts de la course `src/controle_ia/neuron_lens/verdicts_b_beta_v4.py` | en entier, en phase 1, pour les noms de clés (permis par le mandat) | `8c07434f9db0e35e10eb806218da320bc0d6e404e41c4f60c495b35906d88b87` | égale |
| modèle de forme `docs/notes/neuron-lens-v1/lecture-b-alpha/plan-de-lecture-v1.md` | en entier | `5a79991850459ca13469edbd51e91619b50c23fe80085cc1a9e17ff217d831da` | égale |
| mon plan v1 `docs/notes/neuron-lens-v1/lecture-b-beta/plan-de-lecture-b-beta-v1.md` | écrit par moi | `40128756b446301248827cc5a9facfd53baa5cf6b461a8b09731369b61208128` | égale |
| contre-lecture `docs/notes/neuron-lens-v1/lecture-b-beta/contre-lecture-plan-de-lecture-b-beta-v1.md` | en entier | `bf3e2d7572b85df806d5841a0b8a7342829893a86503738fbb153721e33ec4e7` | égale (et égale à l'attendue) |

**Déclaration sur le code des verdicts** (R4) : lu en phase 1, comme le mandat le permet ; il réduit mon indépendance, que seuls mes
engagements protègent : en phase 2 je ne le relis pas et je ne l'importe pas. Les lectures qu'il porte sans que l'addendum les déclare
(n indépendant de la lentille ; règle (b) écrite « n < 32 ») restent des ambiguïtés ouvertes (4.2), non des règles.

**Empreintes seulement, sans ouverture du contenu** (pièces d'entrée nommées par le texte gelé) : série repère de la lentille R publique,
`diag/20261117-015632-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json`, `bd57d519a24e5227df2c2d720ba33a54f47653d0741acbb51f1781b59df33073`,
égale au texte gelé ; références publiées de Qwen3-8B, `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json`
`8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3` et `reads_at_firings_qwen3-8b.json`
`ac0bf101e341385a400bbecb751f9720428da1d0bd09a752c8337dd84ba182cd`, égales au texte gelé (elles servent à l'essai de mon script, 2.3,
étape A).

**Noms de fichiers seulement** (`find -type f`, aucun contenu, aucune empreinte) : `diag/20261118-164930-neuron-lens-b-beta/` (50
fichiers et 50 compagnons `.sha256`, dont `journaux/` : 16 journaux d'étape ; `artefacts-garde-d/` : 2 essais artefacts) et
`runs/20261118-164930-neuron-lens-b-beta/` (`manifeste.json` et son compagnon). La liste complète est classée en 2.1. **Aucun** nom ne
désigne un audit A1 à A5, une relance à la graine 1 ou un arrêt. 50 − 16 − 2 = 32 compagnons dans `diag/`, plus celui du manifeste = 33.

### 1.2 Ce que je sais déjà d'un résultat (déclaré par la session qui me lance, recopié)
La course s'est terminée normalement (« fin : course terminee ») le **2026-11-19 à 05:31:55 UTC** ; l'état final porte `exclus=0` et la
liste des étapes faites suivante : `ajustement-R ajustement-S b0 banc comptes-jetons corpus-activations corpus-ajustement declencheurs
export fumee grandeurs lens-compare measure partie2-b0 partie2-corpus passe pilotes preparer reads score telecharger-poids
telecharger-tokeniseur verdicts` — elle ne contient **ni `audits-controles` ni `audit-relance`** ; aucun arrêt n'a été écrit ; un fichier
de verdicts existe. Durées : ajustement de R ≈ 5 h 07, ajustement de S ≈ 5 h 01. À la récupération : 23 fichiers de résultats d'étape
vérifiés contre leur manifeste, 33 compagnons vérifiés ; compagnons posés après coup sur les 16 journaux d'étape et 2 artefacts de la
garde (d). **Je ne connais aucune valeur de mesure ni aucun verdict.**

Ce renseignement est de seconde main (tiré de pièces qui m'étaient interdites) : il ne remplace aucune sortie versée. L'absence des
étapes d'audit est compatible avec « aucun audit A1 à A5 déclenché » comme avec « audit déclenché mais non joué » ; je calcule moi-même
les déclencheurs (2.3, étape B) avant de lire ce que la course en a écrit. Aucune règle n'a été choisie en vue de ce renseignement.

## 2. Pièces et ordre de lecture (phase 2)

Toutes les lectures se font dans le dépôt de travail, branche de travail, sur les copies versées ; aucun modèle, aucune machine. Les
pièces hors de `diag/` et `runs/` interdites en phase 1 (`docs/notes/neuron-lens-v1/etat-final-course-b-beta-v1.txt`,
`docs/notes/neuron-lens-v1/controles-b-beta-v1.log`) sont de la seconde catégorie : lues seulement si le mandat de phase 2 les autorise,
et alors à l'étape D. La branche `calcul/neuron-lens-b-beta-v1` n'est pas lue sans autorisation écrite du mandat de phase 2.

### 2.1 Classement des pièces
**Catégorie 1 — sorties brutes** (écrites par les scripts du dépôt voisin ou par notre code comme tables de valeurs ; lues d'abord) :
| pièce | ce que j'y prends |
|---|---|
| `causal_lens_b-beta_llama-3.1-8b-instruct.json` (résumé de `score`) | `r_med`, `pass`, `control_med` (et n s'il y figure) par cible, lentille et couche |
| `grandeurs-par-pole-b-beta-v1.json` | grandeurs par pôle : pôles retenus ou écartés et motif, d'où n et le compte de la garde (b), si elles y sont |
| `intervalles-b-beta-v1.json` | intervalles par rééchantillonnage (rapportés seulement) |
| `lens_compare-b-beta-v1.json` (sortie non arrondie du correctif (4)) | accord du premier jeton et recouvrement des dix premiers, paires de lentilles, six couches |
| `reads_at_firings_llama-3.1-8b-instruct.json` (relevés de la lecture aux déclenchements) | `read_S`, `silent`, `read_S_net`, et tout relevé de la permutation |
| série repère `diag/20261117-015632-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json` (`bd57d519…`) | `r_med` de `npR`, « steer 1x », couches 0 à 27 |
| compagnons `.sha256` | empreintes seulement |

**Catégorie 2 — pièces qui portent, ou peuvent porter, des gardes, des déclencheurs, des issues d'audit ou des verdicts écrits par la
course** (y compris toute pièce dont je ne peux pas savoir sans l'ouvrir) :
- 2a, résultats d'étape et pièces de contrôle : `b-beta-preparer.json`, `b-beta-telecharger-tokeniseur.json`,
  `b-beta-telecharger-poids.json`, `b-beta-b0.json`, `b-beta-banc.json`, `b-beta-corpus-ajustement.json`, `b-beta-ajustement-R.json`,
  `b-beta-ajustement-S.json`, `b-beta-export.json`, `b-beta-corpus-activations.json`, `b-beta-comptes-jetons.json`,
  `b-beta-partie2-b0.json`, `b-beta-partie2-corpus.json`, `addendum-partie2-b-beta-v1-b0.md`, `addendum-partie2-b-beta-v1-corpus.md`,
  `b-beta-lens-compare.json`, `b-beta-fumee.json`, `b-beta-passe.json`, `b-beta-pilotes.json`, `b-beta-measure.json`,
  `b-beta-score.json`, `b-beta-grandeurs.json`, `b-beta-reads.json`, `causal_lens_b-beta_llama-3.1-8b-instruct.log`, les 16 journaux de
  `journaux/` (ajustement-R, ajustement-S, b0, banc, comptes-jetons, corpus-activations, corpus-ajustement, export, fumee, lens-compare,
  measure, passe, pilotes, reads, score, telecharger-tokeniseur), les 2 artefacts de `artefacts-garde-d/` (essai-artefact-saute,
  essai-artefact-signe), `runs/20261118-164930-neuron-lens-b-beta/manifeste.json`, et, si autorisés, l'état final et le journal des
  contrôles ;
- 2b, verdicts et déclencheurs de la course : `verdicts-b-beta-v1.json` (le fichier des verdicts au sens du texte), `b-beta-verdicts.json`,
  `b-beta-declencheurs.json`.

### 2.2 Ce qui ne se calcule pas sur les sorties brutes (lu sur une pièce de la course, en le déclarant)
- **Différences entre moitiés de B-1** (mesure, non garde ; nécessaires aux déclencheurs A2 et A3 et au verdict de B-1) : recalculées
  sur la machine et versées dans un résultat d'étape (attendu : `b-beta-ajustement-R.json`, `b-beta-ajustement-S.json` ou
  `b-beta-export.json`), catégorie 2. Je les lis par la procédure « structure d'abord » ci-dessous.
- **n** et **pôles écartés par motif** (lisibilité, garde (b), bande de A5) : si ni la sortie de `score` ni les grandeurs par pôle ne les
  donnent, je les lis dans `b-beta-grandeurs.json`, par la même procédure, et je le déclare.
- **Gardes constatées sur la machine seulement**, lues telles qu'écrites, sans recalcul possible : (d), (f), (g), (h), (i), (k), la part
  « matrices » de (e) (identité), (n), (o), (p), (q), (r), (s) ; contrôles de P.1 ; partie 2 de l'addendum ; banc ; version de Drowse.
- **Procédure « structure d'abord »** pour une pièce de catégorie 2 lue avant mes calculs consignés : j'imprime d'abord les seuls noms de
  clés, types et tailles (aucune valeur) ; j'extrais ensuite les seuls champs de mesure nommés ci-dessus ; je n'imprime aucun champ dont
  le nom désigne une garde, un déclencheur, un audit, un défaut ou un verdict. Si une valeur de cette sorte m'apparaît malgré tout, je la
  déclare au rendu (pièce, champ, heure) et mon calcul ne s'y réfère pas.

### 2.3 Ordre
**Étape 0 — ce plan et le texte.** Vérifier les empreintes de ce plan (compagnon), du texte gelé (`f5d46860…`) et de l'addendum
(`bd8067dc…`). Un écart : arrêt.

**Étape A — mon script, essayé avant toute pièce de la course.** J'écris `docs/notes/neuron-lens-v1/lecture-b-beta/calcul-verdicts-b-beta-v1.py`
(Python, processeur, lecture `json` ; **sans importer ni relire** aucun code des verdicts de la course, `controle_ia.neuron_lens.verdicts_*`),
qui applique la section 3 et calcule, pour chaque ambiguïté ouverte de 4.2 qui se présente, le verdict sous chaque lecture. Je le rejoue
(R5) sur les cas gelés de P.4 qui se construisent sur des tables, avec les références publiées empreintées (`8904c4d3…`, `ac0bf101…`)
ramenées à 32 couches par ⌊l × 36/32⌋ et leurs attendus écrits au texte : (i), (ii-a), (ii-b), (ii-c), (iii-a), (iii-b), (iii-c),
(iii-d) et (iii-e) pour le déclencheur, (iv-a), (v) pour le déclencheur et la branche « non joué », (vi-a) à (vi-e), (vii), (x), (xi),
l'artefact de A1 (deux zéros, un seul zéro, zéros en « ablate pos » de J), « rangs 2 et 3 » ; et sur un cas sain et un artefact faits à
la main. Je n'y rejoue pas les cas qui demandent des matrices, des fichiers ou la machine ((ii-d), (ii-e), (iv-b), (viii) à (ix), gardes
(d), (f) à (s)). Tout écart à l'attendu : je corrige mon script avant la suite et je consigne l'écart. Sortie de l'essai scellée.

**Étape B — calculs sur les sorties brutes, consignés et scellés avant toute pièce de catégorie 2.**
1. `sha256sum -c` de chaque compagnon de `diag/20261118-164930-neuron-lens-b-beta/` et de `runs/…/manifeste.json` (sans ouvrir les
   pièces). Une empreinte fausse : je le dis, la pièce n'est pas lue pour un verdict, et je rapporte les règles qui en dépendaient. Les 16
   journaux et 2 artefacts dont le compagnon a été posé après coup : intégrité attestée depuis la récupération seulement.
2. Lire les pièces de catégorie 1 (2.1).
3. Calculer et consigner : gardes (a), (b) si les motifs sont dans les sorties brutes, (c), part « `score` » de (e), (j) ; déclencheurs
   A1, A4, A5 (avec n si disponible), A6 (B-6 et l'issue de A6 sur les moitiés notées) ; mesures B-2, B-3, B-4, B-5 (lisibilité
   comprise), B-6, B-7 ; accord de B-1. Sortie : `docs/notes/neuron-lens-v1/lecture-b-beta/calcul-etape-b-b-beta-v1.json`, scellée.
4. Puis, par la procédure « structure d'abord » (2.2), extraire les différences entre moitiés de B-1 et, s'il le faut, n et les motifs ;
   compléter : B-1, déclencheurs A2 et A3, garde (b), lisibilité de B-2, B-3, B-7 et bande de A5. Sortie :
   `calcul-etape-b-complement-b-beta-v1.json`, scellée, avec la liste des pièces de catégorie 2 ouvertes et des champs lus.

**Étape C — mon verdict.** Mon script rend, sur les calculs de l'étape B, le verdict sous la règle en vigueur (3) — gardes
constatées sur la machine **provisoirement inconnues** —, puis la table des verdicts selon chaque issue possible de ces gardes (« toutes
tenues » ; « une manquée » → rang 1). Sortie scellée.

**Étape D — pièces de catégorie 2a**, dans l'ordre de la course : 2.5 (arrêts de montage et gardes du montage), puis gardes constatées
sur la machine (2.6), puis recherche de toute sortie d'audit (dans `b-beta-measure.json`, `b-beta-score.json`, journaux de `measure` et de
`score`), puis le manifeste (empreintes de chaque pièce, commit du code de course, versions, graines, carte, lot de `measure`). Je complète
mon verdict avec ces gardes (rang 1 ou non ; rang 2 si un audit que j'ai déclenché n'a pas été joué). Sortie scellée **avant l'étape E**.

**Étape E — seulement ensuite**, `b-beta-declencheurs.json`, `verdicts-b-beta-v1.json` (comparaison principale) et `b-beta-verdicts.json`
(comparée à côté), ainsi que tout champ de verdict, de déclencheur ou d'issue d'audit écarté à l'étape D : verdict d'ensemble, verdict de
chaque mesure, défauts, audits et issues, réserves, écarts de B-4, gardes que j'ai recalculées comparées à celles qu'a écrites la course.
Tout désaccord est rapporté tel quel, sans retouche de mon calcul ; il est tranché par un second lecteur neuf, sans nouvelle mesure.

**Étape F — rendu.** `verdict-lecture-b-beta-v1.md` dans ce dossier, scellé : verdict d'abord ; pièces et empreintes ; gardes ; audits ;
mesures ; grandeurs rapportées (2.4) ; prédictions de l'autrice (réfutées ou non, sans effet) ; ambiguïtés rencontrées et verdict sous
chaque lecture ; réserves ; comparaison au fichier des verdicts ; mentions de 2.7.

### 2.4 Grandeurs rapportées sans critère
« Steer 4x » et « ablate pos » ; intervalles (2 000 tirages ; B-2, B-3, B-4, B-6, B-7) ; part silencieuse par couche, `read_S_net`,
`read_S / (1 − silent)` ; recouvrement des dix premiers jetons entre moitiés ; accord de chaque moitié avec la lentille R publique aux
six couches (aux couches basses, porté en partie par un mode commun) ; valeurs à deux décimales imprimées par `02_fit.py` et
`04_export_rlens.py` (pour mémoire, jamais pour un seuil) ; compte et rang du jeton de début (128 000) dans les jetons gardés ; nombre et
empreinte des jetons gardés ; n par couche et pôles écartés par motif ; valeurs des deux graines si une relance existe.

### 2.5 Arrêts de montage (liste d'arrêt) : lus à l'étape D, **distincts des chaînes en défaut**
Banc au-delà de 23,6 s par document (compte rendu au-delà de 14,2 s) ; à B0, documents ≠ 932, moitiés ≠ 466 et 466, `rows_sha256` ≠
`a6afd972…` ; Drowse ≠ 6.1.4 ou d'empreinte ≠ `673ed2b4…` ; empreinte d'un fichier différente du texte ou de l'addendum (partie 2 contre
partie 1 : modèle, tokeniseur `79e3e522…`, lentilles J `d5300a15…`, J++ `8bd04f48…`, R publique `a63a1588…`, corpus d'activations
`64657ecb…`, `c3202db1…`, `550944a2…`, `9dbf9f44…`, jetons gardés 89 498 et `c37186ad…`, versions § 5) ; licence ; échec d'accès au
tokeniseur ou aux poids ; essais du code des verdicts (P.4) s'ils sont versés. Un manquement y est un **écart à la liste d'arrêt**, non
le rang 1 (O-8 pour le cas « la course a continué »).

### 2.6 Gardes constatées sur la machine, et pièces où je les cherche
(d) `b-beta-b0.json`, `artefacts-garde-d/` (les deux artefacts doivent avoir fait échouer la garde), `b-beta-fumee.json` ; (e) matrices :
`b-beta-b0.json` (Neuronpedia), `b-beta-export.json` (notre R) ; (f) `b-beta-b0.json` ; (g), (h), (q) `b-beta-ajustement-R.json`,
`-S.json`, `b-beta-export.json` ; (i) `b-beta-corpus-ajustement.json`, `b-beta-corpus-activations.json`, `b-beta-measure.json` ; (k)
`b-beta-fumee.json`, `b-beta-passe.json` (avec le message du correctif (1) au journal), `b-beta-pilotes.json`, `b-beta-reads.json` ; (n),
(o) `b-beta-export.json` ; (p) `b-beta-measure.json`, `b-beta-pilotes.json` ; (r) `b-beta-lens-compare.json`, `b-beta-passe.json`,
`b-beta-pilotes.json`, `b-beta-reads.json` (après `b-beta-comptes-jetons.json`) ; (s) `b-beta-reads.json` ; et les journaux de ces étapes.
Pour chacune : valeur écrite, moment, trace de son essai (cas sain, artefact). Sans trace : O-7.

### 2.7 Mentions du rendu
Hors programme : aucun résultat n'entre dans T0.7, T0.8, G0, G1 ni dans un préenregistrement du programme sans nœud de Lazar. Comparaisons
multiples : les verdicts sont des règles de seuils couche par couche, sans test d'hypothèse ; aucune correction appliquée ; intervalles
rapportés sans servir au verdict. Une lecture par lentille peut ajouter un soupçon sur une sonde, jamais la blanchir.

## 3. Règles que j'applique (recopiées du texte gelé et de l'addendum ; aucune règle nouvelle)

### 3.0 Lectures de l'addendum en vigueur (portent le verdict comparé)
Addendum, § 1.1, décision de la mère R-3190, scellé avant toute donnée :
1. une clause « non reproduit » n'est pas jugée sur une bande partielle (plus du quart des couches de la bande non lisibles) : la mesure
   est alors « autre » (effets déclarés : B-2, clause `pass` 16 à 27, 4 couches non lisibles sur 12 ; clause `r_med` 16 à 23, 3 sur 8 ;
   B-3, 4 sur 12 ; B-7, 3 sur 8 couches 8 à 15 ou 2 sur 4 couches 26 à 29, et une bande 8 à 15 partielle retire le déclencheur de A5) ;
2. le témoin de B-2 est compté sur les seules couches lisibles de 0 à 27 ;
3. la garde (a) porte aussi sur les lentilles des deux moitiés de notre R ;
4. (forme) les différences de deux valeurs écrites à 4 décimales par `score` sont arrondies à 4 décimales avant comparaison ;
5. (forme) les valeurs de B-5 sont prises telles qu'écrites (forme décimale la plus courte) et ses moyennes calculées en fractions exactes.

### 3.1 Commun (« Métrique », M.1 ; « Seuil »)
- Valeurs comparées : celles de `score` telles qu'écrites dans son JSON (4 décimales) ; celles de B-1 et de B-5, non arrondies ;
  « au-dessus » = strictement. Verdicts sur les valeurs ponctuelles ; intervalles rapportés.
- Cibles : « steer 1x » (B-2, B-3, B-4, B-6) ; « ablate win » (B-7) ; « steer 4x » et « ablate pos » rapportées sans critère.
- **Couche lisible** : n ≥ 48 pour la cible considérée (n recalculé par notre code depuis le fichier `-causal.pt`, par la règle de
  `score` ; le fichier n'étant pas versé, je prends le n écrit et je le dis). Une bande dont plus du quart des couches est non lisible
  rend la mesure « partielle » pour cette bande.
- « Reproduit » exige la condition à **chaque couche lisible** de la bande ; « plus de N des couches » se lit « plus de la moitié des
  couches lisibles de la bande nommée » — règle des clauses de la table des seuils ; les quantificateurs de la garde (j) (« plus de 2 des
  28 couches ») et de B-6 (« au moins 21 des 28 couches ») se lisent à la lettre.
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
  à la couche 0 **et** moyenne de `read_S` sur les couches 1 à 7 **au moins 0,10 au-dessus** de sa moyenne sur les couches 12 à 23
  (écart ≥ 0,10 : T-5) ; B-5 lisible. « Non reproduit » : `read_S` < 0,30 à la couche 0, **ou** moyenne sur 1 à 7 au plus égale à la
  moyenne sur 12 à 23 ; B-5 lisible. **Lisibilité** : B-5 est « non lisible » (donc « partiel », jamais « reproduit » ni « non
  reproduit ») si la part silencieuse dépasse 0,40 à la couche 0, ou si sa moyenne sur les couches 1 à 7 dépasse 0,50.
- **B-6** — rapportée, non décisive : écart = `r_med`(notre R) − `r_med`(`npR`), « steer 1x », couches 0 à 27 ; « accord » si l'écart
  absolu est ≤ 0,05 à au moins 21 des 28 couches 0 à 27 **et** ≤ 0,15 à toutes ; « désaccord » s'il dépasse 0,15 à au moins une
  couche ; « intermédiaire » sinon.
- **B-7** (« ablate win », notre R) — « reproduit » : `r_med` < 0,25 à chaque couche 0–15 **et** ≥ 0,50 à chaque couche 26–29. « Non
  reproduit » : `r_med` ≥ 0,40 à plus de 4 des 8 couches 8–15 (**par le haut**), ou < 0,30 à plus de 2 des 4 couches 26–29 (**par le
  bas**) (même lecture « plus de la moitié des lisibles »).

### 3.3 Chaîne en défaut (« Seuil », conditions (a) à (s), recopiées)
- (a) `control_med` hors de ±0,10 à une couche de 0 à 27, pour l'une des quatre cibles et l'une des lentilles notées (moitiés comprises,
  3.0, lecture 3) ;
- (b) pilotage sans effet : à une couche de 0 à 27, plus de la moitié des 64 pôles écartés par `score` pour effet nul en « steer 1x » ;
- (c) lentille des logits, `r_med` (« steer 1x ») < 0,80 à l'une des couches 28–30 ; `npR`, < 0,85 à l'une des couches 28–30 ; notre
  R, < 0,85 à l'une des couches 28–30 ;
- (d) essai d'un correctif employé ((1) à (6)) ou de l'estimateur sur le Qwen3 miniature avec un test sauté ou en échec ; fumée de la
  passe en échec ; essai des crochets de pilotage et d'ablation sur un Llama miniature en échec (un échec d'accès au tokeniseur ou aux
  poids est un arrêt de montage, pas une chaîne en défaut) ;
- (e) repli sur les logits : pour `J`, `npJpp`, `npR` ou notre R, |`r_med`(lentille) − `r_med`(logits)| < 10⁻³ à une couche de 0 à 23
  (« steer 1x »), ou une matrice égale à l'identité (écart maximal ≤ 10⁻⁶, float32) à une couche de 0 à 27 (contrôlé à B0 pour les
  trois fichiers de Neuronpedia, après l'export et avant `score` pour notre R) ;
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
  à 27 (à la lettre), ou de plus de 0,10 à l'une d'elles ;
- (k) `arch.fits(MODEL)` : `hub` juste avant la fumée, la passe d'activations et `07_drivers.py` ; nos deux noms juste avant
  `reads_at_firings.py`, fichiers liés d'empreintes égales à celles de fin d'ajustement ; tout autre cas ;
- (l) témoin ou pilotage dégénéré constaté par A1 ou A5, ou l'une des gardes (a) à (c) manquée sur la sortie de `score` de la graine 1 ;
- (m) appariement dégénéré de B-5, constaté par A4 ;
- (n) une matrice de notre R égale à celle de `npR` (écart maximal ≤ 10⁻⁶, float32) à une couche de 0 à 27, ou fichiers d'empreinte
  égale ; contrôlé après l'export, avant `score` ;
- (o) `load_lens` de `R:dclm-llama`, `-even` ou `-odd` lève une erreur, rend `None` à une couche de 0 à 30, ou s'écarte de la moyenne du
  fichier d'ajustement (cible `out` : entière, moitié paire, moitié impaire) de plus de 10⁻³ en écart relatif de Frobenius à une couche
  de 0 à 30 ; contrôlé après l'export, avant `lens_compare.py` et `score` ;
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
| 2 | un audit déclenché qui porte sur B-1, B-2, B-3 ou B-5 n'a pas pu être joué jusqu'à son issue avant la destruction (temps réservé épuisé, garde de dépense, perte de machine) | **non conclu** ; verdict final de la tranche ; les mesures non touchées sont rapportées telles quelles ; aucune reprise sans devis neuf et mot de Lazar |
| 3 | B-2 ou B-3 « non reproduit » | **non reproduit avec nos lentilles** — rapporté à l'identique (R3) ; garde (j) tenue : réserve « défaut dans notre lentille » écrite dès qu'une seule des deux mesures est « non reproduit », lue avec B-6 |
| 4 | B-1, B-2, B-3 et B-5 « reproduit » | **reproduit avec nos lentilles** |
| 5 | autre | **partiel**, mesure par mesure |
B-4 et B-6 n'entrent pas dans le verdict d'ensemble ; B-7 se lit à part. Un « reproduit » dit que la lentille lit ce qu'une direction
pousse en moyenne, pas qu'elle nomme le concept d'une invite donnée.

### 3.5 B-6 et l'audit des deux codes (A6)
« Accord » : les deux codes s'accordent ; « intermédiaire » : rapporté ; « désaccord » déclenche A6, joué sur les sorties de `score`
déjà calculées (moitiés notées) : si, à chaque couche de 0 à 27 où l'écart dépasse 0,15, les deux moitiés sont toutes deux à moins de
0,05 de notre R entière → réserve « écart de corpus » ; sinon réserve « écart d'ajustement ». Aucun verdict n'est suspendu ni changé ;
la réserve accompagne le verdict d'ensemble. L'égalité exacte des deux lentilles est la garde (n).

### 3.6 B-7, pour un moniteur
« Reproduit » : là où `r_med` est bas, une étiquette de neurone décrit une poussée moyenne et ne sert pas à lire un épisode, avec notre
lentille comme avec la publique. « Non reproduit » par le haut : audit A5 ; s'il confirme, rapporté comme lecture valable en contexte plus
tôt que publié ; sinon B-7 « autre ». « Non reproduit » par le bas : rapporté (la lecture ne dit pas ce qu'une activation fait, même
tard). Autre : couche par couche. B-7 n'entre pas dans le verdict d'ensemble.

### 3.7 Audits symétriques : déclencheurs et issues (recopiés)
- **A1, trop beau, lecture contre pilotage** — déclencheur : notre R, « steer 1x » : `r_med` ≥ 0,95 à une couche 0–7, ou `control_med`
  écrit égal à 0 (`0.0` ou `-0.0`, à 4 décimales) à au moins 2 couches de 0 à 27. Contenu : (1) chaque pôle a un témoin distinct de
  lui ; (2) chaque pôle retenu a un pilotage de norme non nulle (fichier `-causal.pt`) ; (3) `measure` relancé à la graine 1, puis
  `score` avec `logit,npR,R:dclm-llama` (`--tag b-beta-graine1`) ; gardes (a) à (c) sur cette sortie. Issue : (1) ou (2) manqué, ou
  garde (a) à (c) manquée sous la graine 1 → chaîne en défaut (l) ; sinon verdicts de la graine 0 tenus, sauf toute mesure parmi B-2,
  B-3, B-7 dont le verdict diffère sous la graine 1, qui devient « autre » ; valeurs des deux graines rapportées.
- **A2, trop beau, stabilité** — déclencheur : différence entre moitiés non arrondie < 10⁻⁶ à une couche d'une cible, ou accord du
  premier jeton égal à 1 aux six couches. Contrôles : 466 et 466 ; empreintes des moitiés `4a31baec…`, `ef95a60c…` ; sommes des moitiés
  différentes (écart maximal > 0) ; exports des moitiés d'empreintes différentes. Issue : un contrôle manqué → chaîne en défaut (g) ;
  sinon B-1 tient.
- **A3, tout négatif, stabilité** — déclencheur : B-1 « non reproduit ». Contrôles de A2, plus chaque document de 128 jetons et
  `full_length` vrai. Issue : un contrôle manqué → (g) ; sinon « non reproduit » tient.
- **A4, B-5 aux extrêmes** — déclencheur : `read_S` ≥ 0,99 à la couche 0, ou `read_S` = 0 à toutes les couches 0 à 31. Contrôles :
  permutation non dégénérée (au plus 10 points fixes par couche ; attendu ≈ 2) ; fichier de lentille S lu égal à celui de l'ajustement
  (garde (k)) ; part silencieuse rapportée. Issue : un contrôle manqué → (m) ou (k) ; sinon B-5 tient telle que calculée (règle de
  lisibilité comprise).
- **A5, B-7 par le haut** — déclencheur : B-7 « non reproduit » par le haut (sous 3.0, lecture 1 : pas de déclencheur si la bande 8 à 15
  est partielle). Contenu : contrôles (1) et (2) de A1 ; `measure` et `score` à la graine 1 (une seule relance si A1 est aussi déclenché).
  Issue : contrôle manqué → (l) ; graine 1 aussi « par le haut » → maintenu ; sinon B-7 « autre ».
- **A6** — 3.5.
- **Tout négatif, reproduction** — déclencheur : B-2 ou B-3 « non reproduit » ; aucun calcul neuf : (j) manquée → chaîne en défaut ;
  (j) tenue → rang 3 et sa réserve.
- Audit non joué (temps réservé d'une heure ou garde de dépense) : issue « non joué », règle du rang 2 ; s'il porte sur B-7 seul : B-7
  « autre ». A1 et A5 partagent une seule relance à la graine 1.

### 3.8 Liste d'arrêt (pour ranger les manquements de 2.5)
Recopiée en substance : banc au-delà de 23,6 s → l'ajustement ne part pas ; à B0, 932, 466/466, `a6afd972…` → l'ajustement ne part pas,
nœud à la mère ; toute chaîne en défaut constatée avant `measure` (en particulier (d) à (i), (k), (n) à (s)) → arrêt ; Drowse d'une
autre version ou empreinte → rien ne part ou arrêt avant l'export ; empreinte ou licence différente → arrêt, message à la mère ; tout écart
de notre code au texte, découvert en course → arrêt, écart écrit avant toute suite. Addendum, § 3 et § 5 : écart aux valeurs attendues du
corpus d'activations ou des jetons gardés → arrêt avant `lens_compare.py` et la fumée, nœud ; autre version d'un autre paquet → nœud
avant l'ajustement.

### 3.9 Prédictions de l'autrice (rapportées, sans effet sur les verdicts)
Pour chaque ligne de la table « Prédiction chiffrée et signe attendu », je rapporte si la condition « réfutée si » est remplie, telle
qu'écrite (B-1 ; B-2 ; B-3 ; B-4 face à J et face à J++ ; B-5 ; B-6 ; B-7 ; verdict d'ensemble modal « partiel »).

## 4. Ambiguïtés

### 4.1 Tranchées par le texte ou l'addendum (la lecture nommée porte le verdict ; la lettre seule est rapportée comme information)
- **T-1** (v1 n° 1 et n° 3) — clause « non reproduit » sur une bande partielle, bande sans couche lisible comprise : addendum l. 24-25
  (mesure « autre »). Information : verdict sous « clause jugée sur les couches lisibles », et effet sur le déclencheur de A5.
- **T-2** (v1 n° 4) — témoin de B-2 compté sur les couches lisibles : addendum l. 41-42. Information : verdict sous « toutes les
  couches 0 à 27 » (l'addendum déclare cette lecture favorable, l. 42-44).
- **T-3** (v1 n° 5) — garde (a) étendue aux moitiés : addendum l. 45-46 (et le texte range les moitiés parmi les lentilles notées,
  l. 115-117). Information : verdict moitiés exclues.
- **T-4** (v1 n° 6) — différences de deux valeurs à 4 décimales arrondies à 4 décimales : addendum l. 47-48. Information : toute
  comparaison où le flottant brut donne un autre côté de seuil.
- **T-5** (v1 n° 7) — B-5 : « au moins 0,10 au-dessus » se lit écart ≥ 0,10 (« au moins » ; confirmé par la prédiction, « réfutée si …
  écart des moyennes < 0,10 ») ; « au-dessus = strictement » règle les tournures « dépasse », « plus de », « sous ». Valeurs prises telles
  qu'écrites, moyennes en fractions exactes : addendum l. 48-49. Information : flottant binaire, s'il change un côté de seuil.
- **T-6** (v1 n° 17) — le fichier des verdicts au sens du texte est le « fichier de verdicts unique » (P.3, étape 7 ; P.6 ; P.7) :
  `verdicts-b-beta-v1.json`, comparaison principale ; `b-beta-verdicts.json` comparé à côté, toute différence entre les deux rapportée.

### 4.2 Ouvertes (non arbitrées ; verdict sous chaque lecture si le cas se présente)
- **O-1** (v1 n° 2 et n° 3) — « reproduit » sur une bande partielle : (i) impossible, mesure « autre » ; (ii) prononçable sur les couches
  lisibles, avec la mention « partielle ». La lecture (i) est la plus proche du texte (« partielle » ; pour B-5, « partiel, jamais
  reproduit »), sans être écrite mot pour mot ; bande sans couche lisible : non jugeable, verdicts avec « reproduit » vrai et faux.
- **O-2** (v1 n° 8) — garde (b) : (i) compte des pôles écartés au motif « effet nul » (> 32) — lettre du texte ; (ii) n retenus < 32,
  tous motifs. Si elles divergent sur les pièces, rapporté au second lecteur comme écart possible du code de course au texte. Si les
  motifs ne sont pas séparés dans les pièces, je le dis.
- **O-3** (v1 n° 9) — n par lentille ou par cible (M.1 range n parmi les métriques « par couche, cible et lentille ») : pour B-3, (i) n de
  notre R ; (ii) couche lisible pour les deux lentilles ; et si le n de la sortie de `score` diffère du n recalculé : (i) recalculé
  (texte) ; (ii) celui de `score`. Toute divergence rapportée comme écart possible du code au texte.
- **O-4** (v1 n° 10) — lisibilité dans (a), (b), (c), (e), (j), A1 et B-6 : lecture par défaut, toutes les couches de la plage ;
  alternative, couches lisibles seules ; les deux si elles divergent.
- **O-5** (v1 n° 11) — rang 2 et cause de l'absence d'audit : si je déclenche un audit A1 à A4 que la course n'a pas joué parce que son
  code ne l'a pas déclenché : (i) rang 2, « non conclu » ; (ii) liste des causes fermée : écart du code de course au texte, rapporté comme
  désaccord, verdict de rang 3 à 5 calculé sans l'audit.
- **O-6** (v1 n° 12) — contrôles d'un audit A2, A3 ou A4 déjà présents dans les pièces versées : (i) l'audit compte comme joué sur la
  machine ; (ii) non (aucune sortie d'audit versée), rang 2. Je ne rejoue rien qui demande les lentilles.
- **O-7** (v1 n° 15) — garde constatée sur la machine sans trace versée : (i) tenue, sur la foi de la fin normale et de `exclus=0` ;
  (ii) non constatable, verdict rapporté avec cette réserve. La lecture (ii) est la plus proche du texte (« sorties versées », P.7) ; la
  (i) repose sur un renseignement de seconde main. Je n'en fais jamais seul une chaîne en défaut.
- **O-8** (v1 n° 16, réduite) — manquement de la liste d'arrêt (2.5) alors que la course a continué : (i) verdict de mesure prononçable,
  manquement rapporté en réserve ; (ii) course hors du texte (« tout écart de notre code à ce texte, découvert en course : arrêt »),
  verdict rapporté sous réserve et soumis au second lecteur.
- **O-9** (neuve, mineure 8) — « notre R » dans les gardes (c) et (e) : (i) lentille entière seule (lettre ; l'addendum n'étend que (a)) ;
  (ii) moitiés comprises ; les deux si elles divergent.
- **O-10** (v1 n° 13) — B-7 « par le haut » et « par le bas » à la fois : les deux lectures de 3.6 rapportées, et le déclencheur de A5.
- **O-11** (v1 n° 14) — rang 1 et réserves : (i) B-6 et la réserve de A6 non rapportées (« aucun verdict de mesure ») ; (ii) rapportées
  comme information.

### 4.3 Réserves (non des ambiguïtés)
- **R-1** (v1 n° 18) — matériel et lot : sur H100, l'invariance aux lots 16 et 64 n'est pas mesurée (M.1) ; si le manifeste montre une
  autre carte ou un autre lot que 64, je le rapporte ; tout verdict qui tient à une marge de l'ordre de 0,03 (effet du matériel mesuré
  entre deux cartes) est signalé.
- **R-2** — compagnons posés après coup (16 journaux, 2 artefacts) : intégrité attestée depuis la récupération seulement.

### 4.4 Correspondance v1 → v2
1 → T-1 ; 2 → O-1 ; 3 → T-1 et O-1 ; 4 → T-2 ; 5 → T-3 ; 6 → T-4 ; 7 → T-5 ; 8 → O-2 ; 9 → O-3 ; 10 → O-4 ; 11 → O-5 ; 12 → O-6 ;
13 → O-10 ; 14 → O-11 ; 15 → O-7 ; 16 → O-8 ; 17 → T-6 ; 18 → R-1 ; neuve → O-9.

## 5. Ce que je ne fais pas
- En phase 1 et 1 bis : aucune ouverture, `cat`, `head`, `grep`, `python` ou empreinte sur un fichier de
  `diag/20261118-164930-neuron-lens-b-beta/` ou de `runs/20261118-164930-neuron-lens-b-beta/` (journaux et `.sha256` compris), ni sur
  `docs/notes/neuron-lens-v1/etat-final-course-b-beta-v1.txt`, ni sur `docs/notes/neuron-lens-v1/controles-b-beta-v1.log`, ni sur la
  branche `calcul/neuron-lens-b-beta-v1` ; ni `verdict-b-alpha-v1.md`, ni les fichiers `calcul-*` de `lecture-b-alpha/`.
- En aucune phase : aucun modèle chargé, aucune machine, aucun réseau payant ; aucun rejeu d'audit ni recalcul qui demande les lentilles
  ou le fichier `-causal.pt` ; aucun import ni relecture du code des verdicts de la course ; aucune pièce de catégorie 2 ouverte avant mes
  calculs consignés de l'étape B (sauf l'extraction « structure d'abord » de 2.2, déclarée) ; aucune lecture touchant P3, P3b, T0.6,
  T0.7, P3-bis ; aucune autre branche sans autorisation écrite du mandat ; aucun commit, aucun push ; aucun fichier réécrit (la v1 reste
  telle quelle ; une correction = un fichier de version suivante, R12) ; aucune ambiguïté ouverte arbitrée ; aucune règle ajoutée.
