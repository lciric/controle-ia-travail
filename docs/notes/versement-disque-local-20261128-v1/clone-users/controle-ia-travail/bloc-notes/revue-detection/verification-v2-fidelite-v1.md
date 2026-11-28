# Vérification de la synthèse v2 « comment détecter » — angle « fidélité des corrections », tour 1 — v1

- **Objet.** `…/revue-detection/synthese-comment-detecter-v2.md` (sha256 `90ad38bf…`), comparée à la v1 (`a47f9141…`),
  au rapport du tour 1 `…/revue-detection/verification-synthese-v1.md` (`43986648…`, écarts VS-01 à VS-25) et au
  traitement `…/revue-detection/traitement-verification-synthese-tour1-v1.md` (`c87ecdec…`). Les quatre compagnons sont
  égaux. `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Vérificateur neuf.** Je n'ai écrit ni la v1, ni la v2, ni les extractions, ni la vérification du tour 1, ni le
  traitement. 2026-10-20, vers 11:00 à 11:30 UTC. Dépôt lu seulement : lectures et `git show` aux commits `97dd829` et
  `7a54d43`, aucune écriture. Non ouverts : `prereg/P3-consignes-v1.md`, textes d'action, clés. Aucune recherche web, aucun
  service payant, aucun contact.
- **Méthode.**
  1. Empreintes recalculées en entier : les quatre entrées ; les 22 PDF de la table des clés, RO compris : toutes égales.
  2. Différentiel mot à mot v1 → v2, hors dépôt :
     `git diff --no-index --word-diff=plain --word-diff-regex='[^[:space:]]+' -U0 v1 v2`. 20 blocs ; 131 lignes
     ajoutées, 63 retirées. Chaque bloc est rattaché à un écart VS ou à l'en-tête de la v2 (section « Différentiel »).
  3. Pages relues **directement** par `pdftotext` (modes défaut, `-raw`, `-layout`), après contrôle d'empreinte, sans les
     pages extraites aux tours précédents ni les scripts du correcteur. Outils : `…/revue-detection/verif-v2-fidelite/page.py`
     (une page, une phrase en contexte) ; `…/verif-v2-fidelite/verifier_phrases_v2.py` (chaque phrase à la **page exacte**
     citée par la v2, lignes de table, épreuve R5). Sortie : `…/verif-v2-fidelite/sortie-verification-v2-fidelite.txt`.
     Reproduire : `python3 -I -B …/verif-v2-fidelite/verifier_phrases_v2.py` ; une page :
     `python3 -I -B …/verif-v2-fidelite/page.py CLE PAGE "phrase" [largeur] [mode]`.
  4. Renvois au dépôt relus : [P] (`d975e981…`) l. 196-216, 236-254, 314-334 ; [V] (`0c8ecbdf…`) l. 200-206, 338-350 ;
     `src/controle_ia/harnais/episode.py` (`79113b49…`) l. 205-262 et `src/controle_ia/environnements/propositions.py`
     (`5d97b223…`) l. 180-188, 236-270, identiques à `97dd829`, à `7a54d43` et aujourd'hui ; `registres/decisions.md`
     l. 354 (R-217), 453 (R-262), 457 (R-265), 461 (R-269) ; `registres/go.md` l. 32-34 ; `registres/depenses.md`
     l. 87-89 ; `docs/decisions/decision-N-026-v1.md` (`85bd4023…`).

## Verdict : **conforme après corrections**

- **Les 25 écarts sont appliqués**, aux lignes que donne le traitement. Aucune correction n'est fausse sur un chiffre.
  15 sans réserve ; 3 avec une réserve de forme (VS-01, VS-18, VS-19) ; 5 justes mais qui perdent une nuance de la page
  (VS-03, VS-04, VS-05, VS-06, VS-12) ; 1 au libellé inexact (VS-16) ; **1 incomplète (VS-08, en E4)**.
- **Différentiel : rien d'autre n'a changé.** Les 20 blocs se rattachent tous à un écart ou à l'en-tête. Un seul ajout
  n'est déclaré nulle part (un exemple de conception, VV2-fidelite-10).
- **Chiffres nouveaux ou déplacés : tous sur leur page.** 155 phrases et chiffres contrôlés à la page exacte citée :
  0 absent. 17 lignes de table contrôlées sur la même ligne imprimée. Colonne LC[A] de [GM] relue ligne par ligne.
- **Phrases anglaises citées : toutes sur leur page.** Deux chaînes anglaises ne viennent d'aucun PDF et la v2 le dit :
  « Your action: » (code) ; le titre du billet d'Anthropic (non vérifié).
- **Épreuve R5 de mon contrôle** : 12 artefacts (chiffre altéré, mot inversé, bonne phrase sur une mauvaise page, mauvaise
  valeur sur une ligne de table) : 12 rejetés.
- **14 constats** : 1 majeur, 8 mineurs, 5 de forme. Aucun ne demande de retirer un chiffre. Le majeur se corrige en une
  ligne.

## Constats, le plus grave d'abord

### Majeur

**VV2-fidelite-01 — VS-08 non appliqué en E4 : portée et cause au-delà de la page.**
- Où : v2 l. 166, E4 « tranche » : « chez [DYL], la sonde d'Apollo échoue déjà sur la version sur consigne ; seule « Did
  you lie? » chute par l'affinage (p. 11) ». Le traitement (l. 54) écrit « la v2 borne la phrase à cet organisme » et
  annonce le lieu « E4 tranche l. 166 ». C'est fait en 2.1 (l. 50), pas en E4.
- Page : [DYL] p. 11. L'épreuve sur consigne ne porte que sur un organisme : « we re-ran the evaluation against prompted
  Gender Secret model organisms ». La chute (« Median balanced accuracy falls from 0.85 to 0.52 for Apollo ») porte, elle,
  sur les trois bancs (p. 10 : « Across all three trained model organism testbeds (AuditBench, Sandbagging, Gender
  Secret) »). Et la page n'affirme pas la cause : « consistent with being caused by fine-tuning rather than the underlying
  behaviour ».
- Correction : « chez [DYL], sur le seul organisme « Gender Secret », la sonde d'Apollo échoue déjà sur la version sur
  consigne ; la chute de la sonde « Did you lie? » est compatible avec un effet de l'affinage (p. 11) ».
- Reproduire : `page.py DYL 11 "prompted Gender Secret" 400` ; `page.py DYL 10 "Across all three trained"`.

### Mineurs

**VV2-fidelite-02 — VS-16 : les « moyennes glissantes » de [GM] sont des maxima de moyennes glissantes (touche N-026).**
- Où : v2 l. 105-107 : « contre 0,0 % à 1,73 % pour les agrégations MultiMax et 1,73 % à 5,19 % pour les moyennes
  glissantes (taux de faux négatifs, colonne LC[A], [GM table 3, p. 12]) ».
- Page : les chiffres sont justes (table 3, p. 12 : « Rolling Attn Probe, Rolling Agg (Selected) » 3,03 % ; « Rolling Attn
  Probe (20H), Rolling Agg » 5,19 % ; « Linear Probe Rolling Exp » 1,73 %). Mais ces trois agrégations finissent par un
  maximum. La sonde « Max of Rolling Means » « takes the max over all mean scores of all possible windows » (p. 7). La
  moyenne mobile exponentielle se lit par « We then take the maximum over EMA scores » (p. 6). C'est la sonde retenue par
  les auteurs : « Our selected probe is the Max of Rolling Means Attention Probe » (p. 12). Le libellé fait lire une
  moyenne là où le papier lit un maximum de moyennes locales. C'est la famille du score lissé de [CC], que la v2 renvoie à
  Lazar (l. 188-189). Enfin, les lignes ne sont pas nommées comme imprimées (règle de l'en-tête, l. 14 : « pour une table :
  sa ligne »).
- Correction : « … et 1,73 % à 5,19 % pour les maxima de moyennes glissantes (« Rolling Agg », « Linear Probe Rolling
  Exp » ; [GM p. 6, p. 7]) » ; nommer les lignes : « Linear Probe Mean » 99,13 % ; « Attn » 87,88 % ; « Attn (With LC
  Training) » 1,34 %. Au nœud « Règle gelée 1 » (l. 188) : ranger ce maximum de moyennes glissantes avec le score lissé
  de [CC].
- Reproduire : `page.py GM 7 "takes the max over all mean scores"` ; `page.py GM 6 "maximum over EMA scores"` ; sortie,
  bloc « colonne LC[A] ».

**VV2-fidelite-03 — VS-05 : citation laissée orpheline en E2.**
- Où : v2 l. 166, E2 « tranche » : « faible à 2 milliards [CA p. 8] ; [DYL table 9] et sans contraste [PAR table 3] ».
- Page : le remplacement de « sur petits modèles [CA p. 8 ; DYL table 9] » laisse « [DYL table 9] » sans affirmation. La
  table 9 (p. 28) ne montre pas de faiblesse à 2 milliards (« google/gemma-4-E2B-it » : 0.79 et 0.76). Elle montre la sonde
  de question (« DYL Probe ») plus faible sur Qwen3-8B (0.69) et Qwen3-4B (0.68).
- Correction : retirer « [DYL table 9] », ou écrire « sonde de question plus faible sur Qwen3-8B (0,69) et Qwen3-4B (0,68)
  [DYL table 9, p. 28] ».
- Reproduire : sortie, lignes « DYL p. 28 ».

**VV2-fidelite-04 — VS-03 : l'hypothèse de [MK] devient une règle.**
- Où : v2 l. 101-102 (« il suit le jeton le plus marqué et marche quand le concept tient à des mots précis ») ; l. 129
  (« mais il marche quand le concept tient à des mots précis [MK p. 4] »).
- Page : [MK] p. 4 avance une hypothèse, sur un seul jeu : « this may indicate that the high-stakes nature of the MTS dataset
  is dependent upon specific words ». Le maximum y est « nearly matching the performance of the more consistent probes » :
  il est donc moins régulier. Le texte vient de la correction proposée par VS-03 ; le correcteur l'a reprise telle quelle.
- Correction : « sur le jeu MTS, le maximum approche les sondes les plus régulières ; les auteurs y voient peut-être un
  concept tenu par des mots précis [MK p. 4] ».
- Reproduire : `page.py MK 4 "this may indicate"`.

**VV2-fidelite-05 — VS-04 : [OA] cité sans la phrase qui borne sa lecture.**
- Où : v2 l. 114-116 (2.2, « Pour P3 ») ; l. 186-188 (« Seul résultat lu sur sa robustesse : [OA] … l'obfuscation
  apparaît, mais … »).
- Page : entre les deux phrases citées, [OA] p. 1 dit : « obfuscated activations arise from representation drift during RL,
  with or without a detector penalty » ; « The detector penalty only incentivizes obfuscated policies ». Sans elles, on lit
  que l'évasion des activations vient de l'entraînement contre la sonde. La page dit qu'elle vient de la dérive, avec ou sans
  sonde. Le traitement l'a vu (remarque, l. 84-85) sans l'appliquer ; c'est pourtant ce qui compte pour la règle gelée 1.
- Correction : ajouter l. 116 et l. 188 : « l'obfuscation des activations vient de la dérive des représentations pendant
  l'apprentissage, avec ou sans pénalité de la sonde ; la pénalité ne pousse qu'aux politiques obfusquées (p. 1) ».
- Reproduire : `page.py OA 1 "with or without a detector penalty"`.

**VV2-fidelite-06 — VS-05 : « capacité, pas taille » va plus loin que [DYL].**
- Où : v2 l. 50 (« **capacité** du modèle, pas taille ») ; l. 130 (« [DYL] : capacité, pas taille (p. 10) ») ; l. 25
  (« elle gagne avec la **capacité du modèle** (au-dessus de 0,90 dès 9 milliards chez [CA p. 8]) »).
- Page : [DYL] p. 10 mesure contre un indice de capacité (« correlates positively and significantly with the Artificial
  Analysis Intelligence Index »). Il ne compare pas capacité et taille. « Pas taille » est une inférence, appuyée par un seul
  exemple (table 9, p. 28 : Qwen3.5-4B 0.89 contre Qwen3-8B 0.74). L'échelle ne porte que sur le mensonge sur consigne
  (p. 12 : « Scaling results are on prompted lying only »). La l. 25 accole « capacité » (de [DYL]) à un seuil de taille
  (de [CA]).
- Correction : l. 50 et l. 130 : « [DYL] : mesuré contre un indice de capacité, pas contre la taille (p. 10) ; mensonge sur
  consigne seulement (p. 12) ». L. 25 : « avec la taille ou la capacité du modèle ».
- Reproduire : `page.py DYL 12 "prompted lying only"` ; `page.py DYL 10 "Intelligence Index"`.

**VV2-fidelite-07 — VS-06 : « distracteurs » donnés comme cause de l'échec d'Oak.**
- Où : v2 l. 53, dernière colonne de [AG] : « distracteurs (p. 17) ; hypothèse de l'équipe rouge, pas résultat : … ».
- Page : [AG] p. 17 sépare deux choses. Les distracteurs causent des faux positifs, chez Baobab et Oak (« successfully caused
  many spurious probe activations »). L'échec qui compte (pas plus de tromperie lue quand Oak sous-performe) est rangé à part,
  sans cause donnée : « there were more mysterious failures ».
- Correction : « faux positifs dus aux distracteurs ; échec de fond sans cause donnée (« more mysterious failures », p. 17) ;
  hypothèse de l'équipe rouge, pas résultat (p. 43) ».
- Reproduire : `page.py AG 17 "more mysterious failures" 600`.

**VV2-fidelite-08 — VS-12 et VS-03 : [AP] p. 23 coupé ; deux lieux qui ne disent pas la même chose.**
- Où : v2 l. 93 (« « Recall at 1% FPR compared to control does show improvement » [AP p. 23] ») ; l. 26-27 (« n'est que
  « comparable » chez Apollo ») ; l. 129 (« « comparable » chez Apollo [AP p. 23] »).
- Page : la phrase continue : « although is still subpar compared to the probe trained on Instructed-Pairs ». Coupée, elle
  sur-vend le dernier jeton. À l'inverse, la l. 26 (« n'est que « comparable » chez Apollo ») et la l. 129 taisent le gain
  de rappel que la l. 93 cite.
- Correction : l. 93 : citer la phrase entière. L. 26 et l. 129 : « « comparable » en aire ; rappel à 1 % de faux positifs
  meilleur que la même sonde lue sur toute la réponse, mais en dessous de la sonde Instructed-Pairs [AP p. 23] ».
- Reproduire : `page.py AP 23 "although is still subpar" 400`.

**VV2-fidelite-09 — En-tête R7 et traitement : la méthode de recoupement est décrite plus forte qu'elle n'est.**
- Où : v2 l. 16-17 (« toutes les phrases anglaises de la v2 recoupées sur leur page ») ; traitement l. 15-16 (« 103 trouvées
  à la page citée »).
- Problème : `…/correcteur-tour1/recouper_v2.py` accepte une phrase trouvée sur **n'importe quelle page** d'une clé citée dans
  le même bloc (fonction `main`, ligne `p_ok = [p for p, t in pages.items() …]`). Il ne lit pas la page citée ; sa sortie le
  montre : « comparable | AP p. 9,15,18,23 ; CA p. 20,84 ; MK … ». Le résultat reste vrai : mon contrôle à la page exacte
  trouve les 155 phrases et chiffres testés et rejette les 12 artefacts.
- Correction : l. 16-17 : « phrases anglaises recoupées sur les pages des clés de leur bloc, puis contrôlées à la page exacte
  (`…/verif-v2-fidelite/sortie-verification-v2-fidelite.txt`) ; « Your action: » vient du code ; le titre du billet n'a pas
  de PDF ». Même précision au traitement.
- Reproduire : lire `recouper_v2.py`, fonction `main` ; première ligne de `sortie-recoupement-v2.txt`.

### Forme

**VV2-fidelite-10 — VS-01 : un exemple de conception ajouté sans le dire.**
- Où : v2 l. 156 : « (par exemple le log10 du plus grand coût lisible des pas précédents) ».
- Problème : absent de VS-01 et de la ligne VS-01 du traitement (l. 47). « Rien d'autre n'est changé » (v2 l. 8) ne le
  couvre pas. Il n'est pas faux.
- Correction : le marquer « exemple du correcteur, à préenregistrer ou non », ou le retirer.

**VV2-fidelite-11 — VS-01 : « rapport moyen » au lieu de « rapport géométrique moyen ».**
- Où : v2 l. 157 (« rapport moyen d'environ 33, [V] l. 345 »).
- Page : [V] l. 345 : « rapport géométrique moyen d'environ 33 (10^1,5227) ».
- Correction : « rapport géométrique moyen ».

**VV2-fidelite-12 — VS-01 : renvoi de ligne trop court.**
- Où : v2 l. 154 (« 60 actions par condition (60 tâches, un épisode par tâche et condition, [P] l. 318) »).
- Page : « 1 épisode » par tâche et condition est en [P] l. 320 (« quatre conditions × 60 tâches × 1 épisode = 240
  épisodes »).
- Correction : « [P] l. 318-320 ».

**VV2-fidelite-13 — VS-18 : « étiquette = rôle ».**
- Où : v2 l. 54, dernière colonne de [AU].
- Page : [AU] p. 6 : l'étiquette de tromperie est « very correlated with the 'Impostor' label », pas égale au rôle.
- Correction : « étiquette très liée au rôle d'imposteur ».

**VV2-fidelite-14 — VS-19 : « au plafond … : nœud ».**
- Où : v2 l. 167 (« au plafond de 10 USD par lancement ou au-dessus (R-269) : nœud ») ; l. 196 (« atteint ou dépasse le
  plafond par lancement »).
- Registre : R-269 (`registres/decisions.md` l. 461) permet un lancement jusqu'à 10 USD ; seule « toute dépense au-delà du
  plafond par lancement ou du crédit » est un nœud. Sans effet pratique : E4 exige déjà un GO de changement de modèle.
- Correction : « au-delà de 10 USD par lancement (R-269) : nœud ».

## Fidélité, écart par écart

| écart | appliqué (v2, lignes) | relu sur | juste | complet | constat |
|---|---|---|---|---|---|
| VS-01 | 146-159, 168-169, 197-199 | `episode.py` l. 213-217, 254, 260 ; `propositions.py` l. 238-269 ; [P] l. 238-253, 318-320 ; [V] l. 345 | oui | oui | 10, 11, 12 (forme) |
| VS-02 | 47, 98-100, 132 | [PAR] table 3, p. 7 (sept lignes, colonne « Avg. » comprise) | oui | oui | — |
| VS-03 | 23-27, 100-103, 129 | [MK] p. 4 ; [AP] p. 23 | oui | nuance perdue | 04, 08 |
| VS-04 | 111-118, 185-188 | [OA] p. 1, p. 5 ; [GM] p. 10 | oui | bornage omis | 05 |
| VS-05 | 25, 50, 51, 130, 166 | [CA] p. 8, 9, 18 ; [DYL] p. 10, 12, table 9 p. 28 | oui | citation orpheline ; inférence | 03, 06 |
| VS-06 | 53, 63-77, 128 | [AG] p. 1, table 2 p. 7, p. 17, p. 43 | oui | cause à nuancer | 07 |
| VS-07 | 63-70, 241 | [BX] p. 3 ; RO p. 1, 3 ; [CC] p. 1, 2, 6, 8 ; [EM] p. 1 ; [MA] p. 17 | oui | oui | — |
| VS-08 | 50, 166 | [DYL] p. 10, 11 | oui en 2.1 | **non en E4** | **01** |
| VS-09 | 45, 129-131 | [BU] p. 3, 5, 10 | oui | oui | — |
| VS-10 | 28-32, 44, 166 | [YS] p. 2, 3 (aucune mention du raisonnement dans les 11 pages) ; [AP] p. 5 | oui | oui | — |
| VS-11 | 46, 127, 131 | [AP] p. 4, 21 | oui | oui | — |
| VS-12 | 86-97 | [AP] p. 7, 22, 23 | oui | citation coupée | 08 |
| VS-13 | 55, 127, 166 | [K] table 1 p. 7, p. 9 | oui | oui | — |
| VS-14 | 127 | [FQ] p. 1 | oui | oui | — |
| VS-15 | 134, 168 | [LIAR] p. 1, 10 | oui | oui | — |
| VS-16 | 103-107, 112, 132 | [GM] p. 6, 7, 8, table 3 p. 12 | chiffres oui ; libellé non | oui | 02 |
| VS-17 | 188-189 | [CC] p. 6 (« streaming », un seul signal bloque la suite) | oui | oui | — |
| VS-18 | 17-18, 54, 128 | [AU] p. 6, 7 (figure 6 en mise en page : (a) 0.653 et 0.948, (b) 0.984) | oui | oui | 13 (forme) |
| VS-19 | 167, 190-196 | R-262, R-265, R-269 ; `go.md` l. 33-34 ; `depenses.md` l. 89 | oui | oui | 14 (forme) |
| VS-20 | 200-204 | [CA] p. 1, 11 | oui | oui | — |
| VS-21 | 139-140, 165 | N-026 (`85bd4023…`), conditions 1 à 4 | oui | oui | — |
| VS-22 | 28-29, 43 | [BX] p. 8 | oui | oui | — |
| VS-23 | 129, 135 | [P] l. 198-205, 214-215 ; [V] l. 204, 345 | oui | oui | — |
| VS-24 | 51 | [CA] p. 6 | oui | oui | — |
| VS-25 | 212-216 | compagnons sur disque ; deux fichiers de provenance (neuf empreintes complètes égales) | oui | oui | — |

Les trois « corrections du rapport » faites par le correcteur sont justes : moyennes glissantes de 1,73 % à 5,19 %
(table 3, p. 12) ; « production-grade » et « shadow deployment on production traffic » ([CC] p. 2) ; épreuve sur consigne
limitée à « Gender Secret » ([DYL] p. 11) — appliquée en 2.1 seulement (VV2-fidelite-01).

## Différentiel v1 → v2 : rattachement des 20 blocs

| bloc (v1 → v2) | contenu | écart |
|---|---|---|
| 1 → 1 ; 4 → 5-8 | titre ; en-tête du correcteur | administratif |
| 10-13 → 14-19 | en-tête R7 | VS-18 ; méthode v2 (VV2-fidelite-09) |
| 17-22 → 23-32 | section 1, points 1 et 2 | VS-03, VS-05, VS-10, VS-22 |
| 33-37 → 43-47 | lignes [BX], [YS], [BU], [AP], [PAR] | VS-22, VS-10, VS-09, VS-11, VS-02 |
| 40-41 → 50-51 | lignes [DYL], [CA] | VS-05, VS-08, VS-24 |
| 43-45 → 53-55 | lignes [AG], [AU], [K] | VS-06, VS-18, VS-13 |
| 53-58 → 63-75 | « Ce qu'a fait Anthropic » (Oak déplacé sous « Hors d'Anthropic », rien de perdu) | VS-06, VS-07 |
| 70-80 → 87-110 | 2.2, Apollo et « Ailleurs » | VS-12, VS-02, VS-03, VS-16 |
| 82-84 → 112-118 | 2.2, « Pour P3 » | VS-04 (et renvois VS-03, VS-16) |
| 93-98 → 127-132 | rangs 2 à 7 | VS-13, VS-14, VS-11, VS-18, VS-06, VS-03, VS-09, VS-23, VS-05, VS-02, VS-16 |
| 100-101 → 134-135 | rangs 9 et 10 | VS-15, VS-23 |
| 106 → 140-141 ; 110 → 146-159 | règles communes ; « Nombre déjà écrit dans le contexte » | VS-21 ; VS-01 (VV2-fidelite-10, 11, 12) |
| 116-120 → 165-169 | table des expériences | VS-21, VS-10, VS-05, VS-13, VS-08, VS-19, VS-01, VS-15 |
| 136-139 → 185-196 | règle gelée 1 ; dépense | VS-04, VS-17 ; VS-19 |
| 141-143 → 198-204 | positions ; contact externe | VS-01 ; VS-20 |
| 152 → 213-216 ; 176 → 241 ; 182 → 248-250 | section 6 ; ligne RO ; fichiers v2 | VS-25, VS-07 ; administratif |

Deux retraits vérifiés : « (R-265 (1)) » remplacé par « GO-2026-10-20-06 » : même décision (`registres/decisions.md`
l. 457 renvoie à ce GO) ; « un lancement à la fois » reçoit « (R-262) » : écrit en l. 453. Neutres.

## Remarques (non comptées ; pour le tour 2 ou pour Lazar)

- **[PAR] p. 7.** Les auteurs écrivent « Peak Activation and the Follow-up monitors consistently underperform compared to
  Full Averaging », alors que leur colonne RP montre l'inverse (sous-rendement 0.891 contre 0.828 ; « Avg. » 0.856 contre
  0.840). La v2 lit la table, ce qui est juste. Citer aussi la phrase des auteurs montrerait l'écart (règle R4).
- **[YS] p. 3.** Les auteurs affirment : « the difficulty does not stem from the relevant information being missing ». La v2
  en fait une hypothèse (VS-10). Dire que c'est la conclusion des auteurs, mise en doute ici, serait plus fidèle.
- **[GM] p. 8.** Les sondes ne sont pas entraînées sur les contextes longs (« in particular not on long context »). Le
  99,13 % de la moyenne est donc aussi un échec de transfert. La v2 le dit pour l'attention (1,34 % une fois entraînée sur
  des contextes longs), pas pour la moyenne : « dilution d'un signal local par la moyenne » (rang 7, l. 132) reste une
  lecture.
- Les autres remarques du traitement (l. 75-87) sont hors de mon angle ; seule celle sur [OA] p. 1 devient un constat
  (VV2-fidelite-05).

## Limites

- Angle « fidélité » seulement : classement, pouvoirs et recommandations non rejugés, sauf là où une correction les touche.
- Annexes lues aux pages citées seulement. Aucun chiffre recalculé à partir des données des auteurs.
- Neuf PDF restent sans compagnon (`[X]` et `[N]`) ; leurs empreintes complètes sont égales à la provenance ; aucun
  compagnon créé ici (à faire avant tout versement, R6).

## Fichiers écrits (chacun avec son compagnon `.sha256`)

- `…/revue-detection/verification-v2-fidelite-v1.md` (ce rapport).
- `…/revue-detection/verif-v2-fidelite/` : `page.py`, `verifier_phrases_v2.py`, `sortie-verification-v2-fidelite.txt`
  (155 phrases à la page exacte, 17 lignes de table, colonne LC[A], épreuve R5 : 12 artefacts rejetés). Scripts lancés par
  `python3 -I -B` : aucun `__pycache__`.
