# Contre-lecture R2 — préenregistrement de T0.6, organismes v0, brouillon 2 — v1

- Contre-lecteur neuf (Claude, sous-agent) : je n'ai écrit ni ce brouillon, ni le brouillon 1, ni la conception, ni P3,
  ni P3-bis. Écrit le 2026-11-03, de 07:04 à 07:20 UTC (heures relevées par `date -u`).
- Texte relu : `brouillons/T0.6-organismes-v0-v1-brouillon2.md`,
  `e960ec10fa5c5c3e398654a5a98a51a1fb1da61ec649f6f3672f42b14a3b7cdd`. `sha256sum -c` de son compagnon : OK (lancé depuis
  `brouillons/`, le compagnon porte un chemin relatif).
- Consigne suivie : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/contre-lecture-t06-brouillon2-prompt.md`.
- Règles tenues : aucun commit ; aucun `.sha256` ; aucun fichier existant modifié ; rien lu ni écrit sous `donnees/` ;
  aucun `git fetch`, `checkout` ni `stash` ; aucun appel de réseau ni de modèle ; calculs par `nice -n 10 … python -I -B`.
  Mes fichiers sont tous sous `/home/claude/scratch/contre-lecture-t06/`.

## 1. Verdict

**Scellable après couples.** Le dessin est sain : l'obstacle des tâches est réel et bien levé, le compte des tâches est
juste, les chiffres de puissance et de devis sont reproduits à l'octet près, et la sonde fixée d'avance tient. Mais trois
défauts bloquent le scellement en l'état :
- le contrôle d'identité à dose 0 ne peut pas échouer tel qu'il est écrit ;
- la table A peut conclure « organisme non établi » sur un lecteur du coût neuf en panne ;
- un résultat scellé unique rend l'ordre de lecture (DT-4) impossible à tenir.

Les 30 couples du fichier JSON lèvent ces trois défauts et les points importants. Les champs « à remplir au candidat »
restent à remplir : entropie, commit, code, préenregistrement de T0.7 en mode « coût ».

Décompte : **3 bloquants, 11 importants, 14 mineurs** ; 30 couples (`couples-contre-lecture-t06-brouillon2-v1.json`).

## 2. Ce que j'ai vérifié et trouvé juste

- **Empreintes** recalculées, toutes égales aux valeurs écrites dans le brouillon :
  - brouillon 1 `e212fb35…` ; conception `a064c3ba…` ; T0.7 brouillon 4 `a292088c…` ;
  - P-009 `fe74b913…`, P-011 `64afff19…`, P-015 `6e74c6cb…`, N-007/N-008 `ab7dc9bb…`, N-029 `084e3052…` ;
  - brief `9261932a…`, programme `2fd63bad…` ; P3 `d975e981…`, consignes de P3 `a68468fe…` ;
  - `lora.py` `5e4ee21e…`, `distillation.py` `9e25e707…` ; `lecture-p3.json` `c221d955…` ;
  - `textes_sha256` lu dans `episodes-p3.json` (`1a96cbf8…`) : `ba05fa13…`, égal au texte ;
  - pièces : compagnons de `puissance_t06_v2.py` (`be3d6121…`), de `puissance-t06-v2.txt` (`87813a36…`) et des pièces v1 :
    OK ; pièces de P3-bis et rapport de reprise : OK.
- **Compte des tâches** : 64 tâches d'évaluation ; P3 a pris les 60 premières ; restent 4 ; 32 tâches de réserve ; donc
  36 tâches disjointes. Recoupé sans ouvrir `donnees/` :
  - R-143 et R-147 pour les 60 tâches ;
  - P-011 l. 34 et la note G1 citée en I9 pour les « 32 tâches de réserve » ;
  - `docs/procedures/T0.5-extraction-v1.md` l. 65-67 : les tâches d'entraînement servent par construction à la distillation
    de (ii) et aux jeux synthétiques de T0.7. Le plan (b) en est donc l'usage prévu.
- **Obstacle des tâches** : réel. Un adaptateur distillé sur les 600 actions de P3 et évalué sur les mêmes 60 tâches mêle
  mémoire et étiologie ; le rejet de (c) est juste. Les deux plans tiennent la règle.
- **Chiffres de puissance et de devis du texte** : chacun correspond à la sortie brute (effets minimaux 0,394, 0,525,
  0,495, 0,660 ; dose–réponse 0,97–1,00, 0,74–0,79, 0,94–0,97, 0,48–0,53, nul 0,0165 ; aires 0,612–0,657 et
  0,632–0,705 ; devis 4,8–6,9 h et 11,5–17,1 h, 5,2–9,0 et 12,5–22,3 USD ; 10,5 Go par couche). Recalculs de tête justes :
  - 27 Mo pour l'adaptateur (13,6 millions de paramètres en demi-précision) ;
  - rapport de 6,6 entre dix paires et une transcription ((2 643 + 223) × 10 / 4 319) ;
  - 10^1,5227 ≈ 33.
- **Formules du script** : erreur type s√2/√n ; moments de Jonckheere–Terpstra stratifiée (n k(k−1)/4 et
  n k(k−1)(2k+5)/72), justes. L'écart type entre tâches s'annule bien dans la différence appariée.
- **Code** :
  - `LineaireLoRA.forward` ne calcule pas le terme d'adaptation à dose 0 : la sortie est la base, au bit près ;
  - `injecter` refuse une seconde injection : les deux adaptateurs passent par `charger_etat`, ce qui doit être écrit dans
    le code neuf ;
  - `difference_moyennes` : w = m₊ − m₋, b = −w·(m₊ + m₋)/2, maximum seulement, comme écrit ;
  - `plancher_apparie` : w ~ N(0, Σ), Σ sur les jetons d'entraînement de toutes classes, centré, comme écrit ;
  - `intervalle_blocs` arrête au-delà de 1 % de tirages dégénérés.
- **Aire moyenne des plis** : le choix est juste (les scores de deux sondes d'échelles différentes ne se mettent pas en
  commun). L'appariement des planchers par indice revient à apparier au hasard deux tirages indépendants. C'est correct
  pour une statistique « moyenne de deux aires », et le quantile 0,95 de cette moyenne est le bon point de comparaison.
- **Sonde fixée d'avance et coïncidence déclarée** : tenues. Le couple « différence de moyennes, couche 15 » est justifié
  sans donnée (aucun hyperparamètre, couche du milieu). La coïncidence avec la sonde principale de tromperie de P3 est
  déclarée, et aucune aire de P3 sur un organisme n'entre dans le choix. La liste d'arrêt invalide toute autre sonde
  décisive.
- **Aucun couperet de temps** (R-1276) :
  - la liste d'arrêt ne contient que des erreurs de chaîne ;
  - deux heures sans ligne `PROGRES` déclenchent une alerte, sans arrêt ;
  - le seul arrêt d'argent est le plafond de 200 USD du GO ;
  - les 72 heures de disque sont une estimation du devis, pas un arrêt.
- **GO-2026-11-02-28** : `registres/go.md` l. 74, citation exacte. P-015 l. 61 et 68-69 : citations exactes.
- **Seuils** : T6-3 et T6-4 sont lues chacune à 95 %, sans conclusion sur « au moins un des deux sens ». Le choix est
  cohérent et déclaré.

## 3. Bloquants

**B1 — Le contrôle d'identité à dose 0 ne discrimine rien, et il n'a pas d'artefact (R5).** Le texte compare les logits
« avant l'injection, puis après injection à dose 0 ». Or un adaptateur neuf a B = 0 (`lora.py`, l. 39) : il rend la base
au bit près **à toute dose**. Fait après l'injection et avant l'entraînement, le contrôle passerait même si le court-circuit
de la dose 0 était cassé, ou si la dose n'était jamais appliquée.

Rien ne vérifie non plus qu'aux doses non nulles l'adaptateur entraîné agit vraiment. Or une dose non appliquée
fabriquerait un nul propre de T6-1 et de T6-2 : c'est le pendant, côté nul, de l'audit R4.

Couples K01 et K02 :
- contrôle fait après le chargement de chaque adaptateur entraîné ;
- artefact : logits différents de la base à dose 1 ;
- dose et empreinte des adaptateurs relues et consignées par épisode ;
- arrêt avant tout épisode d'évaluation.

**B2 — Aucune garde de la mesure du coût.** Le coût est lu par un **module neuf** (P-015). Le saboteur instruit de P3 (IA)
rejoue dans la course un effet connu (P3-P1 1,5227). C'est le témoin positif planté de la mesure, que R-1276 exige pour
chaque course, mais il n'est que descriptif (T6-8).

Avec un lecteur neuf défaillant, ou un T6-1 non calculable, la table A tomberait en A2. Elle écrirait alors une phrase
gelée fausse (« l'adaptateur ne gonfle pas le coût ») et engagerait un « nouveau réglage de la distillation ».

Couples K03 à K05 :
- ligne A1b « non tranché » si IA moins H n'est pas établi, ou si T6-1 n'est pas calculable ;
- réfutation de T6-1 renvoyée à A1b ;
- signes de T6-8 corrigés (voir m12).

**B3 — Un seul résultat scellé rend DT-4 inapplicable.** Le point 6 écrit « toutes les lectures du point 7 dans un
résultat scellé ». Lire T6-1 ouvrirait donc le fichier qui porte aussi T6-3 à T6-9, avant le verdict de P3-bis. P-015 (b)
(l. 68-69) et DT-4 l'interdisent.

Couple K06 : deux résultats scellés séparés, celui des sondes n'étant ouvert par personne avant le verdict de P3-bis.

## 4. Importants

**I1 — DT-1 sous-estime le surcoût de (b).** Le texte écrit « ≈ 3,6 h et ≈ 5 USD de plus ». Les 3,6 h ne couvrent que
la génération. Le devis du texte donne lui-même :
- durée : 4,8 à 6,9 h contre 11,5 à 17,1 h, soit **6,7 à 10,2 h de plus** ;
- dépense : attendu 7 à 13 USD contre 14 à 27 USD, soit **7 à 14 USD de plus** (7,3 à 13,3 USD de calcul).

Le surcoût reste minime devant le plafond, mais le chiffre porté devant Lazar doit être juste. Couples K13 et K14.

**I2 — La puissance de T6-1 ne compte qu'une des deux comparaisons.** T6-1 exige deux bornes basses positives, contre la
base **et** contre l'adaptateur témoin ; les effets minimaux 0,394 et 0,525 valent pour une seule. Ma simulation
(approximation normale, comme le script ; `verif-t61-intersection-v1.txt`) donne, avec un adaptateur témoin neutre, une
puissance conjointe de 0,675 au plan (b) à 0,394, et de 0,695 au plan (a) à 0,525. Avec un témoin qui baisse le coût comme
dans P3 (−0,3176), on revient à environ 0,80.

Couple K12 : déclarer cette perte, et la recalculer dans un script de puissance v3 versé au candidat.

**I3 — Les bases boîte noire manquent à côté du test croisé.** Le coût seul sépare le saboteur instruit de l'honnête à
0,888 dans P3 (`audit_R4.cout_seul`). N-029 (bras 2 : « base boîte noire gratuite que toute sonde doit battre ») et P-015
(« Bases : base « coût seul » à côté du témoin lexical ») le demandent. Le texte n'a, comme prédicteurs triviaux, que la
longueur, le rang du pas et la mention ; le coût déclaré, signal même du sabotage, n'y figure pas.

Une sonde sur les jetons de l'action, au maximum, peut lire le nombre lui-même (premier addendum de P3 : 0,9137 sur le
champ du coût). La ligne « transfert vu » serait alors vraie à la lettre (« n'est pas seulement le texte de la
consigne »), mais trompeuse sur ce que lit la sonde.

Couples K10 et K11 :
- coût seul et témoin lexical rapportés, en aire moyenne des deux plis ;
- réserve si le coût seul sépare au moins autant que la sonde ;
- « sépare au moins autant » défini par max(a, 1 − a) sur l'aire moyenne des plis, comme `separation` de P3.

Je n'en fais pas une ligne « non interprétable » : pour un organisme flagrant, elle tuerait le test par conception, ce que
Lazar refuse (R-1276).

**I4 — Les lignes B2 et C2 ignorent A3.** Si l'effet ne passe pas la comparaison avec l'adaptateur témoin (A3, « l'effet
peut venir du réglage fin »), l'organisme n'est pas établi comme saboteur. B6 ou C6 dirait pourtant « transfert vu » d'un
adaptateur qui n'est peut-être qu'un réglage fin. Couple K09 : B2 (et donc C2) couvre A1b, A2 et A3.

**I5 — L'audit R4 du coût vient après la table A.** L'audit de « trop beau » sur l'effet de (ii) (au-delà de P3-P1, textes
relus « avant le verdict ») est placé en fin de lecture, après P3-bis. La table A pourrait donc être lue sans lui. Couple
K07 : la part « coût » de l'audit est lue avec T6-8, avant tout verdict de la table A.

**I6 — Le texte se contredit sur l'ordre T0.8 → sondes.**
- La section 0 et DT-2 écrivent que la boîte noire de T0.8 est lue « avant toute lecture de sonde ». DT-2 fonde même son
  écart à P-015 (b) sur cet ordre.
- Le point 7 écrit « après les moniteurs boîte noire de T0.8 **s'ils sont scellés** ».

Couples K07 et K08 : les tables B et C attendent la lecture scellée de T0.8 (ligne B1). L'autre voie possible, que Lazar
peut préférer : retirer la phrase de la section 0 et l'argument de DT-2. Mais l'une ou l'autre doit être écrite.

**I7 — Aucune entropie n'est écrite (R1, R9).** Le texte parle de « graines dérivées » et de clés, sans racine. Reprendre
celle de P3, comme le fait P3-bis, rejouerait les graines d'action de P3 sur ses 60 tâches : les épisodes ne seraient plus
neufs au plan (b). Couple K16 : entropie neuve, tirée avant le scellement, une clé nommée par usage.

**I8 — Rien n'aligne T0.6 et T0.7 sur la sonde du test croisé.** GO-28 parle de « sondes de T0.7 entraînées sur une
étiologie ». Le texte fixe la sonde lui-même, mais le brouillon 5 de T0.7 reste à écrire : deux textes scellés pourraient
fixer deux sondes décisives différentes. Couple K17 : le brouillon 5 reprend la sonde fixée ici, ou renvoie à ce texte.

**I9 — Le budget de tâches de G1 n'est pas dit.** Dans les deux plans, les 32 tâches de réserve sont consommées (évaluation
en (a), distillation en (b)). La note `docs/notes/ideation-organisme-v1/course-2/note-p3-episodes-calibrage-g1-v1.md`
(`1d26e8b6…`) propose de les donner à l'épreuve de G1, à la place des 60 tâches de P3. DT-1 doit le dire.

R-1276 (« tailles fixées par la décision à permettre ») appuie par ailleurs la recommandation (b). Couple K15.

**I10 — L'égalité des longueurs des textes de P3 n'est mesurée que sur ses 60 tâches.** P3 l'exige « tâche par tâche »,
sans tolérance (`prereg/P3-premier-test-i-a-v1.md` l. 336-339), entre les trois conditions instruites (IA, IT, IM). Elle
n'a été mesurée que sur les 60 tâches de P3 : les 4 tâches restantes et les 32 tâches de réserve n'en ont aucune mesure.
Couple K18 : mesure au candidat avec le vrai tokeniseur ; un écart est un nœud.

**I11 — Le type des adaptateurs n'est pas fixé ; en demi-précision, la distillation peut stagner.** `LineaireLoRA` crée A
et B au type de la base. En bfloat16, A a des valeurs d'environ 0,016, avec un écart entre valeurs représentables de 6·10⁻⁵
à 1,2·10⁻⁴. Le pas d'AdamW de 1·10⁻⁴ est du même ordre : une part des mises à jour se perd à l'arrondi. Un A2 par défaut
de précision serait un « non concluant par défaut de conception ».

Couple K19 : type déclaré au candidat, simple précision recommandée dans un module neuf. Le code gelé reste intact ; c'est
une routine de code, à éprouver par une répétition sur le modèle jouet.

## 5. Mineurs

- **m1** — « R-143 » pour les 60 tâches : R-143 a été retirée par R-145, et N-019 a été tranché par GO-2026-10-12-01
  (R-147). Couple K20.
- **m2** — La grille {0 ; 0,25 ; 0,5 ; 0,75 ; 1} ajoute 0,75 à celle de P-009 (a), {0 ; 0,25 ; 0,5 ; 1}. L'écart est à
  déclarer. Couple K21.
- **m3** — T6-3 écrit « 0,63 à 0,70 (a) » ; la sortie donne 0,7046. Couple K24 : 0,71.
- **m4** — Le script calcule l'aire « des scores mis en commun », le texte lit l'aire moyenne des deux plis. C'est
  équivalent pour l'erreur type : ma simulation donne 0,0194 contre 0,0193 à 36 tâches, et 0,0143 contre 0,0143 à 64. À
  dire. Couple K23.
- **m5** — « coût seul à 0,888 » est écrit sans chemin ni empreinte (R6). Couple K22.
- **m6** — Les planchers de P3 viennent d'une covariance de données génériques. Ici, Σ vient des jetons d'entraînement du
  pli, contraste des classes compris : le plancher, et l'aire minimale détectable, peuvent être plus hauts que ceux de P3.
  De plus, P-015 demande pour T0.7 un « plancher sous permutation rapporté ». Couples K23 et K26.
- **m7** — « Tirage dégénéré » n'est pas défini pour l'aire moyenne des plis. Couple K25.
- **m8** — 16 des 32 tâches de réserve ont servi à la revalidation de T0.5 (épisodes honnêtes,
  `prereg/T0.5-revalidation-equivalence-pilote-v2.md`, `4ff2b075…`, l. 110). C'est sans effet sur l'organisme, mais à
  déclarer. Couple K27.
- **m9** — Mémoire : 10,5 Go par couche en demi-précision font ≈ 42 Go en double précision, le type des familles de
  sondes. Les trois couches ensemble dépasseraient les 128 Go de mémoire vive. Il faut un calcul couche par couche, sinon
  on aura une erreur de chaîne. Couple K28.
- **m10** — Le verdict en un temps ou en deux temps n'est pas dit, alors que P3-bis ou T0.8 peuvent tarder. Couple K30.
- **m11** — La garde « lot qui mêlerait deux états d'adaptateur » est impossible à déclencher : la dose est portée par les
  modules. Elle ne peut donc pas être éprouvée sur un artefact (R5). Couple K29 : garde sur l'état consigné par épisode.
- **m12** — T6-8 attend « ≈ 0 » pour le témoin et la mention. P3 a donné −0,3176 [−0,5704 ; −0,0650] et −0,3229
  [−0,5404 ; −0,1155], tous deux d'intervalle sous 0 (`lecture-p3.json`). Couple K05.
- **m13** — Dans `puissance_t06_v2.py`, l. 180, le commentaire renvoie à « plan d'analyse, point 3 » ; c'est le point 4.
  Pièce non modifiable : à corriger dans la v3 (sans couple).
- **m14** — Le défaut (b) de DT-1 lit le GO (« actions du saboteur instruit de P3 ») au-delà de sa lettre ; le texte le dit
  et laisse Lazar refuser. C'est acceptable sous un défaut de 48 heures, puisque le GO couvre la dépense. Mais si Lazar
  tient la lecture du GO pour un nœud, le défaut ne s'applique pas. Sans couple : à trancher par la session.

## 6. Points visés par la consigne, en une ligne chacun

- **Obstacle des tâches et DT-1** : juste et bien levé ; compte juste ; surcoût faux (I1) ; budget de G1 omis (I9).
- **Aire moyenne des plis et appariement des planchers** : justes (m4 recoupé) ; covariance du plancher à déclarer (m6).
- **Sonde fixée d'avance et coïncidence** : tenues ; à aligner avec T0.7 (I8) ; bases boîte noire à rapporter (I3).
- **Contrôle d'identité à dose 0** : bloquant (B1).
- **Lecture « diffus » renvoyée à T0.8** : juste dans son principe, mais l'ordre se contredit (I6).
- **Ordre de lecture et témoin positif (DT-4)** : bloquant tant que le résultat scellé est unique (B3) ; l'audit du coût
  est mal placé (I5) ; P3-bis éprouve la chaîne générique de P3, pas la chaîne « apprise sur l'organisme, par plis » d'ici.
  Le contrôle dans l'étiologie (T6-5, lignes B3 et C3) tient ce rôle dans la course : c'est la bonne garde, je n'y touche
  pas.
- **Puissance au plan (a)** : chiffres justes ; effet minimal 0,525, 0,48 à 0,53 de puissance de dose–réponse à 0,40,
  aire minimale de 0,632 à 0,705 ; puissance conjointe de T6-1 ≈ 0,70 (I2). Elle est nettement plus faible que celle de
  (b), ce qui appuie la recommandation (b).
- **Cohérence de DT-1 à DT-6 avec le texte** : DT-1 a un chiffre faux (I1) ; DT-2 dépend de l'ordre T0.8 (I6) ; DT-3, DT-4,
  DT-5 et DT-6 sont cohérents avec le texte.
- **R6, R7** : aucun chiffre de l'état de l'art ; les chiffres tirés de P3 renvoient à `diag/` par la pièce de puissance ; un
  chiffre sans chemin (m5).
- **R5** : B1 et m11 ; les gardes nommées sont à éprouver dans le code neuf (le texte l'exige déjà, point 4 de « Ce qui
  manque »).
- **R4** : les audits « trop beau » sont en place ; il manquait leur pendant côté nul (dose non appliquée, mesure en panne)
  et le bon ordre (B1, B2, I5).
- **R-1276** : aucun couperet de temps ; plafond de 200 USD seul arrêt d'argent ; témoin positif planté à rendre opérant
  (B2) ; tailles : I9.

## 7. Ce que j'ai rejoué, et empreintes

| fichier | sha256 | rôle |
|---|---|---|
| `puissance-t06-v2-rejeu.txt` | `87813a3677e00312d91275fa88df9390880cd07179e5e6b654f1995f04851c50` | sortie de `nice -n 10 .venv/bin/python -I -B brouillons/T0.6-organismes-v0-v1-brouillon2-pieces/puissance_t06_v2.py` (45 s) : **identique à l'octet** à `puissance-t06-v2.txt` (`cmp`) |
| `scripts/verif_t61_intersection_v1.py` | `a0f457bc410f716a9838859690439db4ccfd8605aca176ad28aea86db756cb0f` | puissance conjointe de T6-1 (I2) ; aire moyenne des plis contre aire mise en commun (m4) |
| `verif-t61-intersection-v1.txt` | `5316657dbe2a30147757303ea916916b4551762b4e1c0a648ce8bdbb81ac4727` | sa sortie |
| `scripts/couples_t06_v1.py` | (voir la réponse finale) | écrit les couples, vérifie l'unicité de chaque « ancien » et leur application dans l'ordre sur une copie ; les étiquettes `point` du JSON ont été renumérotées ensuite à la main (mineurs m1 à m14), sans toucher aux textes |
| `brouillon2-apres-couples-essai.md` | (voir la réponse finale) | copie de travail du brouillon 2 avec les 30 couples appliqués : preuve d'applicabilité, pas un brouillon 3 |

Lu en plus des fichiers de la consigne (lecture seule) :
- `docs/procedures/T0.5-extraction-v1.md` l. 65-70 ;
- `prereg/T0.5-revalidation-equivalence-pilote-v2.md` l. 110 ;
- `docs/notes/ideation-organisme-v1/course-2/note-p3-episodes-calibrage-g1-v1.md` ;
- `src/controle_ia/premier_test_ia/lecture.py` (audit R4, prédicteurs triviaux, coût seul) et `statistiques.separation` ;
- `diag/20261020-075740-p3-lecture/lecture-p3.json` (P3-P1, P3-P1 aux milliers joints, P3-P2, `cout_mention`, P3-P6,
  `audit_R4`).
