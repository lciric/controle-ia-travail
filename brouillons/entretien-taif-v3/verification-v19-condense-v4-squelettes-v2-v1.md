# Vérification des squelettes sans issue v2 — programme de l'entretien v19 et condensé v4 — v1

- **Vérificateur** : sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, modèle déclaré par
  l'environnement : Claude Opus 5.5 (`claude-opus-5-5`), autre modèle que le rédacteur (Claude Fable 5.2). Je n'ai écrit
  aucune des pièces lues, ni la contre-lecture. Vérification courte, tâche confiée par la session mère.
- **Heures** (`date -u`) : premier relevé 2026-11-18T22:26:16Z, après les lectures ; fin : dernière ligne.
- **Pièces vérifiées, empreintes conformes à leurs compagnons et à `controle_ia.scellement verifier`** :
  `programme-entretien-taif-v19-squelette-v2.md` (`25d7f7934ad613ae6cc47faabcfe91446e8cb85d2419916f0e281d580de50657`) ;
  `programme-entretien-taif-condense-v4-squelette-v2.md` (`c457a89c7f382d4888b70ea8e1b7f1c9fcf754368b1dd6d6620649647bee5be0`) ;
  `differences-v18-vers-v19-squelette-v2.md` (`3f213b4cf192ccf502205693f85faf7e6e3cbba575a17a4148b8890d0a3db553`).
- **Sources, conformes** : `programme-entretien-taif-v19-squelette.md` (`c827f4c4…`) ; `programme-entretien-taif-condense-v4-squelette.md`
  (`25b1e245…`) ; `contre-lecture-v19-condense-v4-squelettes-v1.md` (`3f8228e6…`, lue en entier).
- **Lignes de registre lues, et elles seules** : `registres/decisions.md` (fichier vivant, `8e9d2141…` à la lecture) R-3319,
  R-3434, R-3435, R-3464, R-3472 ; `registres/go.md` (fichier vivant, `d89e7a07…` à la lecture) GO-2026-11-18-48, -49, -55,
  -63. Repérées par leur identifiant en tête de ligne, puis imprimées une à une.
- **Lectures hors mandat, déclarées** : (1) `differences-v18-vers-v19-squelette-v1.md` (`7d2b2824…`), comparée à sa v2
  (nécessaire au contrôle 2 sur la liste des changements) ; (2) `docs/decisions/decision-N-067-v1.md` (`966dd9dc…`), les
  seules lignes 67 et 80, trouvées par une recherche des mots « frontière », « boundary », « voisin », aussi passée sur
  `docs/decisions/decision-resserrement-juge-au-nul-v1.md` (`9700fe6f…`, aucune ligne trouvée) : source de la phrase du
  « voisin publié » de la réponse 3.5 (contrôle 4) ; (3) `src/controle_ia/scellement.py`, noms de fonctions seulement, pour
  m'assurer que le scellement n'écrit que le compagnon.
- **Non ouverts** : la v18 (aucun couple ne l'exigeait), `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `prereg/`,
  `registres/etat.md`, toute autre ligne des deux registres.
- **Cloisonnement** : aucune issue, aucun score, aucune aire lus. Trois lignes lues touchent des pièces cloisonnées sans en
  donner le contenu : la ligne R-3464 (chemins et empreintes de la sortie du rejeu de NARCBench, bras externe), la ligne R-3472
  (chemin et empreinte de son verdict), l'autorisation GO-2026-11-18-48 (rattachée au verdict de la lecture de l'accumulation
  sur l'épisode). L'autorisation GO-2026-11-18-63 nomme un opérateur écarté des verdicts de l'étape de lecture des sondes et de
  l'apprentissage des sondes sur la tâche, sans en donner le contenu. Rien n'en est recopié ici au-delà du rattachement.

## Verdict

**« Après ces couples exacts. »** Les 63 couples de la contre-lecture sont appliqués : 56 à l'octet, 4 avec le marqueur de
source du second cycle à la place de « à relever », 3 dépassés par la consigne de la session mère sur le barreau 7 ; ces
sept écarts sont déclarés et justes. Aucune issue, aucun score, aucun chiffre de résultat n'entre en v2 ; aucune phrase dite
ne parle du second cycle ; la réponse sur le juge de l'organisme ne déclare rien « libre » ni « non trouvé ». Restent huit
couples mineurs, à faire **avant le remplissage**, puisque la copie remplie est ensuite fermée à la session mère : une
affirmation « contre-lus » plus forte que la pièce, restée dans le condensé (C-1) ; un crochet hors convention dans une phrase
dite (C-2) ; la place du second cycle dans la ligne « échec de G1 » du tableau d'en-tête (C-3) ; l'exactitude de la section D
(C-4) ; trois renvois ou listes non alignés (C-5 à C-7) ; la source du « voisin publié » (C-8). Aucun n'est bloquant pour le
jury ; C-1 et C-3 sont les deux qui comptent.

## 1. Les couples de la contre-lecture

**Méthode** : un programme extrait les blocs de la contre-lecture (`avant-v19`, `avant-v4`, `avant-diff`, chacun suivi de son
bloc `text`) et compte, dans v1 et v2, chaque « avant » et chaque « après ». Résultat : **63 couples** (42 sur la v19, 20 sur
le condensé, 1 sur la liste des changements), conformes au compte de la section D, et 2 ajouts sans « avant ».

| issue du contrôle | couples | écart déclaré | juste |
|---|---|---|---|
| « avant » une fois en v1, absent en v2 ; « après » absent en v1, une fois en v2 | 56 (dont M-8 (b), M-8 (c) et m-4, où l'« après » contient l'« avant » : comptes cohérents) | — | — |
| « après » présent au marqueur près : `[SOURCE DU SECOND CYCLE — à relever par la mère]` remplace « à relever par la session mère » ou « ligne de décision à relever » ; le reste à l'octet (vérifié par programme) | 4 : B-1 (b) ; M-4 (a), (b) ; premier couple de M-4 (c) | oui (section D, colonne « au-delà », B-1 et M-4) | oui : consigne de la session mère ; la ligne qui décide le second cycle n'était pas dans les lignes du rédacteur ; l'autorisation GO-2026-11-18-63 dit bien « second cycle de conception, trois levées du chemin critique », et l'autorisation GO-2026-11-18-49 porte sur la question de l'accumulation, pas sur le second cycle |
| « avant » disparu, « après » remplacé par un état plus récent | 3 : m-1 (v19 § 2.3, condensé § 2, v19 § 5.1) | oui (section D, m-1) | oui : R-3464 (lecture faite, 21:23:20 à 21:53 UTC, code de sortie 0, ligne `LECTURE-NARC-EXT`) et R-3472 (verdict écrit et scellé par un juge neuf, `docs/verdicts/verdict-narc-externe-v1.md`, `deacd111…`, non lu par la mère) ; retirer le repli « not read in time » du barreau 7 suit l'état, pas une issue |

**Ajouts** : le point 19 du § 8 (B-2 (d)) et la puce « *wasn't it November?* » (M-3 (a)) figurent une fois dans la v19 v2 ;
l'ajout en ligne de M-1 (f) (« La forme de l'organisme suit l'option (b) de D-5, tranchée par Lazar (R-3319). ») figure dans
l'en-tête du condensé v2 ; les clés de m-5 sont portées sur chaque barreau (1 `VERDICT-P3BIS`, 2 `RUN-CONFIRMATION-T06`, 3
`ISSUE-MOTS-ET-COUT-T06`, 4 `VERDICT-T07-ETAPE-B`, 6 le verdict de l'accumulation, 7 le verdict du juge neuf, 8
`SCELLEMENT-ORGANISMES-VA`). Les cinq cellules de M-1 (b) sont dans les bonnes lignes (D-1, D-2, D-4, D-5, D-6).

**Contre les lignes lues** : D-1 (a), D-5 (b), D-6 (a) « lu comme » et à confirmer avant le geste, D-4 non tranchée avec son
défaut (b) le 20 vers 16:30 UTC, barreau 8 selon la recommandation : conformes à R-3319 ; branche (B) de l'activité interne du
saboteur à budget (« la course n'enregistre rien », « aucun code ne change ») : conforme à GO-2026-11-18-55 et R-3435 ;
contraste à témoin apparié « sur le principe », énoncé ouvert : conforme à GO-2026-11-18-48 et R-3434.

**Exactitude de la section D** : elle écrit « appliqués à l'octet » pour les 63 couples, et « oui, à l'octet » pour B-1 (a)
à (i) et pour M-4 (a), (b), (c), (e) ; quatre ne le sont qu'au marqueur près, trois sont dépassés. L'écart est déclaré dans la
troisième colonne ; la formule est à corriger (C-4).

## 2. Rien d'autre n'a changé (diff mot à mot, v1 vers v2, des trois pièces)

Chaque bloc changé du programme et du condensé renvoie à un couple ou à une consigne déclarée en section D. Changements de
cohérence **non nommés** en section D, tous justes et sans issue : v19 § 1, ligne de l'organisme, « (D-5 (b), mot de
Lazar) » et R-3319 (3) ; v19 § 3.8, soutien, R-3319 (3) ; v19 § 2.3, heure des états 21:45 → 22:02 UTC (heure de R-3472) ;
v19 § 5.1, « rapport ou verdict du rejeu de NARCBench » retiré du prévu (le verdict est scellé) ; v19 § 9 point 2, « huit » →
« onze » lignes, jusqu'à 22:02 UTC ; v19 § 7.3, points 2 et 3 réécrits selon B-2 et l'avis 9 de la contre-lecture. La liste
des changements v2 ne change que les lignes marquées « (v2) », l'en-tête et les sections C et D.

Lignes **non alignées** par la v2 avec ce qu'elle applique ailleurs : le condensé § 4 dit encore « contre-lus » pour les addenda
d'écart, contre m-11 (C-1) ; la v19 § 3.11 compte « les barreaux 1, 3, 4 et 6 » parmi ceux qui ont un verdict ou une issue
scellés, sans le barreau 7 (C-7) ; la v19 renvoie encore à la liste des changements v1 (C-5), le condensé au squelette v19 v1
dans sa première puce, à côté d'une puce qui renvoie à la v2 (C-6).

## 3. Aucune issue, rien qui la laisse deviner

- **Nombres neufs en v2** (relevés par programme) : dates et heures, empreintes, numéros de lignes R et GO, numéros de
  section. Aucun score, aucune aire, aucun compte de résultat. Les mots « null », « nul », « negative » neufs viennent de
  « *our judge's null* », de « juge au nul formé des lois connues » et de « *a pre-registered negative result* » dans un « ne
  pas dire ».
- **Second cycle, côté jury** : aucune phrase dite ne le mentionne (v19 § 3.4, § 3.9 (b), § 4 ; condensé § 7, question 6).
  Il n'y entre que par l'emplacement du § 3.4, dont le repli est « rien ». Les phrases dites gardées (« *Then we say so, cycle
  by cycle* », « *If our main gate fails, I have committed in writing to redesign* ») sont conditionnelles et viennent de la
  v18.
- **Second cycle, notes internes** : dit « décidé » en v19 § 1, § 2.3 (« Suites décidées »), § 3.4 (puce d'état). Les deux
  dernières places sont neutres. **La première ne l'est pas** : dans la ligne « échec de la porte principale du papier A (G1) »,
  la colonne v18 dit « reconception …, en principe » et la colonne v19 dit « un second cycle est décidé » ; la suite se lit
  « la règle est déjà appliquée », c'est-à-dire l'inférence que B-1 a retirée des phrases dites, alors que G1 n'a pas couru.
  Le texte vient du couple M-4 (a), appliqué fidèlement ; mais le squelette doit rester lisible sans indice par des agents
  cloisonnés (l'autorisation GO-2026-11-18-63 en nomme un). Couple C-3.
- **Place des emplacements** : v19 § 3.1, ordre par numéro de barreau (5 inséré après 4, avant l'étape B bis), sans tri par
  issue ; condensé § 4, l'emplacement sous « ce qui n'a pas marché » est conditionnel (« s'il y en a … sinon supprimer la
  puce », m-6) ; v19 § 5.1, ligne du 18 novembre : le contraste à témoin apparié vient **avant** le verdict de l'accumulation,
  aucun ordre de cause n'est suggéré ; v19 § 5.3 point 2, l'emplacement « une ligne sur l'échelle, selon les issues » suit des
  résultats négatifs d'avant le 9 novembre, mais il est dit « selon les issues » et n'a pas changé depuis la v1 : neutre.
- **Contraste à témoin apparié** : sa date est retirée de la phrase dite (M-8 (a)) ; son motif ne se dit pas (M-8 (b)) ; la
  phrase de repli « *added before any data of that gate exist* » est vraie (GO-2026-11-18-48 : « sans effet sur ce qui est
  déjà scellé »).
- **Autorisation GO-2026-11-18-49** : la v19 (en-tête, § 9) et l'annexe du condensé disent seulement qu'elle « porte sur la
  question de l'accumulation, pas sur le second cycle » ; son contenu n'est pas recopié : rien n'en sort.

## 4. Réponse sur le juge de l'organisme

- **Réponse dite (v19 § 3.5) et question 8 du condensé** : ni « free », « novel », « unoccupied », « new », ni « not found »,
  « did not find ». Rien n'est revendiqué sur le juge au nul formé des lois connues (« *we claim nothing on it until our
  reading of the finance literature … is done* ») ; ce qui est dit est ce qui est mesuré. **Conforme.**
- **Variante** (« *what we have not found is the designated null, the archive, the promotion rule and its guarantee* ») :
  c'est un « non trouvé », mais en note, « sur mot écrit de Lazar seulement », avec « Sans ce mot écrit, elle ne se dit pas » ;
  le choix revient à Lazar (modification de revendication). Conforme.
- **Phrase du voisin** (« *a published neighbour gives such an instruction, but aimed at the data boundary, not at the
  statistic* ») : elle porte sur la forme de l'attaque, pas sur le nul ; c'est le « voisin à dire » de N-067, point 3
  (Sargsyan, p. 27-28 ; N-067 l. 67 et 80, lecture hors mandat) ; la forme de l'attaque est dite confirmée par Lazar dans cette
  même ligne. Pas une déclaration « libre ». Mais la v19 ne lui donne aucune source à côté de la réponse : C-8.

## 5. Les deux phrases neuves du rédacteur

- **Repli du § 3.6** (« *The criteria do not move, and a failed criterion is reported as failed. What follows is my decision,
  in writing, and it cannot move a criterion.* ») : juste, sans issue ni promesse de report ; « *What follows is my decision,
  in writing* » peut encore s'entendre comme une décision déjà écrite : à Lazar, si elle le gêne, « *What happens next will be
  my decision, put in writing; it cannot move a criterion.* » (non bloquant).
- **Phrase sur les addenda** (§ 3.10) : juste et sans issue (procédure, sur question seulement) ; mais le crochet
  « [counter-read: …] » est dans la phrase dite et hors de la convention des emplacements, et le nombre « four » est celui du
  18 novembre : à mettre en emplacement d'état (C-2).

## Couples exacts

Chaque texte « avant » a été contrôlé par programme : il figure une seule fois dans son fichier v2.

**C-1.** Condensé v2, § 4, l. 104 (m-11 non porté ici) — avant :
```avant-v4
Écrits en addenda, contre-lus et scellés ; le texte scellé n'est jamais réécrit.
```
après :
```text
Écrits en addenda et scellés (« contre-lus » seulement si la contre-lecture est relevée pour les quatre : v19, § 3.10) ; le texte scellé n'est jamais réécrit.
```

**C-2.** v19 v2, § 3.10, l. 467 — avant :
```avant-v19
as addenda [counter-read: seulement si relevé pour les quatre]; the sealed text itself is never rewritten.* »
```
après :
```text
as addenda; the sealed text itself is never rewritten.* » `[ÉTAT — « counter-read » : dire « written, counter-read and sealed » seulement si la contre-lecture est relevée pour les quatre ; le nombre d'addenda se relit le jour de l'entretien ; à relever par la session mère]`
```

**C-3.** v19 v2, § 1, l. 66, ligne « échec de la porte principale du papier A (G1) », colonne v19 — avant :
```avant-v19
| **un second cycle est décidé, sans borne de cycles** (interne ; au jury, seulement par l'emplacement du § 3.4) |
```
après :
```text
| inchangé : reconception sans borne de cycles (N-062) ; **à part, état interne** : un second cycle de conception des sondes est décidé ; G1 n'a pas couru, et ce tableau ne dit pas ce qui a déclenché ce cycle (au jury, seulement par l'emplacement du § 3.4) |
```

**C-4.** Liste des changements v2, section D — (a), l. 101, avant :
```avant-diff
extraits par programme et appliqués à l'octet ; chaque texte « avant » figurait une seule fois.
```
après :
```text
extraits par programme et appliqués à l'octet, sauf sept, déclarés ci-dessous : quatre portent le marqueur `[SOURCE DU SECOND CYCLE — à relever par la mère]` à la place de « ligne de décision à relever » ou de « à relever par la session mère » (B-1 (b) ; M-4 (a), (b) et le premier couple de (c)), trois sont dépassés par la consigne de la session mère sur le barreau 7 (m-1) ; chaque texte « avant » figurait une seule fois.
```
(b), l. 106, avant :
```avant-diff
| B-1 (a) à (i) | oui, à l'octet |
```
après :
```text
| B-1 (a) à (i) | oui ; à l'octet sauf (b), où le marqueur de source remplace « à relever par la session mère » |
```
(c), l. 112, avant :
```avant-diff
| M-4 (a), (b), (c), (e) | oui, à l'octet |
```
après :
```text
| M-4 (a), (b), (c), (e) | oui ; (e) et le second couple de (c) à l'octet ; (a), (b) et le premier couple de (c) avec le marqueur de source |
```

**C-5.** v19 v2, en-tête, l. 20 — avant :
```avant-v19
source : `brouillons/entretien-taif-v3/differences-v18-vers-v19-squelette-v1.md`.
```
après :
```text
source : `brouillons/entretien-taif-v3/differences-v18-vers-v19-squelette-v2.md` (la liste v1 reste gardée).
```

**C-6.** Condensé v2, en-tête, l. 4 — avant :
```avant-v4
Elle dérive du squelette `programme-entretien-taif-v19-squelette.md` (même dossier)
```
après :
```text
Elle dérive du squelette `programme-entretien-taif-v19-squelette-v2.md` (même dossier)
```

**C-7.** v19 v2, § 3.11, ligne « What have you shown that works? », l. 484 — avant :
```avant-v19
les barreaux 1, 3, 4 et 6 ont leur verdict ou leur issue scellés
```
après :
```text
les barreaux 1, 3, 4, 6 et 7 ont leur verdict ou leur issue scellés
```

**C-8.** v19 v2, § 3.5, puce « Ce que N-067 fixe », l. 335 — avant :
```avant-v19
tromper, description exacte du juge, deux bras comparés) ;
```
après :
```text
tromper, description exacte du juge, deux bras comparés ; voisin à dire : Sargsyan, p. 27-28, une consigne adverse donnée à un modèle de langue qui connaît le harnais, dirigée contre la frontière des données et non contre la statistique, N-067 point 3) ;
```

## Réserves

1. `registres/decisions.md` et `registres/go.md` sont vivants ; les états sont ceux des empreintes notées en tête (vers
   22:20 UTC). Ce qui a pu changer depuis (D-4, la ligne qui décide le second cycle) n'est pas relevé.
2. Je n'ai pas lu la ligne qui décide le second cycle (R-3456, hors de ma liste). C-3 repose, comme B-1, sur la structure
   (G1 n'a pas couru ; la colonne v19 suit une colonne « en principe ») ; si cette ligne montre un déclencheur sans lien avec
   une issue, C-3 reste juste mais devient de forme.
3. Non revérifiés ici, inchangés de v1 à v2 : la dépense du § 2.1, les citations et leurs pages (hors du « voisin » de C-8),
   les états du plan.
4. Les numéros de ligne cités sont ceux des fichiers v2 aux empreintes de tête.
5. Les couples C-5 et C-6 changent un renvoi et ne touchent aucun texte dit ; C-4 ne touche que la liste des changements.

Fin de la vérification : 2026-11-18T22:28:13Z (`date -u`, relevé avant le scellement).
