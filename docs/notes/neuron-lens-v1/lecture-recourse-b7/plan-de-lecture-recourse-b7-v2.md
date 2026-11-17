# Plan de lecture de la recourse de la lecture contre ablation (B-7) de B-α, sur A100, aux lots 16 et 64 — v2

v2 = v1 (`plan-de-lecture-recourse-b7-v1.md`, non scellée, jamais appliquée) corrigée selon sa contre-lecture
(`contre-lecture-plan-de-lecture-recourse-b7-v1.md` : « à corriger », une bloquante, cinq majeures, huit mineures). Aucun résultat de
mesure n'a été ouvert entre la v1 et la v2.

Écrit par la fille « Neuron Lens » le 2026-11-17 vers 08:47 UTC, à la demande directe de Lazar dans la session de la fille (« écris le
plan de lecture et fais-le contre-lire »). Il est écrit **avant toute ouverture d'un résultat de mesure** de la course
`20261117-015632-neuron-lens-b-alpha`, puis contre-lu par un sous-agent neuf et scellé. Il est ensuite appliqué par un **lecteur neuf**,
un sous-agent qui n'a écrit ni le texte gelé, ni l'addendum, ni le code, ni la commande, ni ce plan. Le lecteur applique les critères
tels qu'ils sont écrits et n'arbitre aucune ambiguïté : il la signale et donne, s'il y a lieu, le verdict sous chacune des lectures.

## 0. Pièces qui font foi (empreintes à recalculer par le lecteur avant tout)
- Texte gelé : `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (`34b882437a9d1eb7…`).
- Addendum v3 : `docs/notes/neuron-lens-v1/addendum-texte-gele-v6-recourse-b7-a100-v3.md` (`5f05f5bc5cae8e1e…`), en entier, § 2 à § 6.
- Journal de la course : `docs/notes/neuron-lens-v1/journal-course-b-alpha-v5.md` (`3047ff1c1f73c31b…`).
- Contre-lecture de la commande v8 (les quatre réserves de lecture) :
  `docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-commande-b-alpha-v8-v1.md` (`a6b7a9ccf25eb249…`).
- Manifeste : `runs/20261117-015632-neuron-lens-b-alpha/manifeste.json` (`69917256f53484fd…`).
- Troisième course, pour la comparaison au matériel : `diag/20261115-120622-neuron-lens-b-alpha/` et son verdict
  `docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md` (sur `main`, `ca06acb1…`, R-2915).

## 1. Ce que l'auteur de ce plan sait déjà d'un résultat (déclaré)
Par le journal et l'état poussé, lus pour conduire la course : B0 est passé (essais 7/7, 8/8, 4/4, 13/13, B.3 35/35, aucun défaut
(e)) ; la partie 2 est sans écart ; la fumée est passée ; les deux séries sont allées jusqu'aux verdicts ; **le code de la course n'a
requis aucun audit**, ni « trop beau », ni « tout négatif », ni « B-7 par le haut », ni au lot 16 ni au lot 64. L'auteur ne connaît
**aucune valeur de mesure ni aucun verdict** de B-2, B-3, B-4 ou B-7, à aucun lot. Aucune règle ci-dessous n'a été choisie en vue de
ce renseignement : toutes sont recopiées du texte gelé et de l'addendum v3.

## 2. Ordre de lecture
0. **Avant tout fichier de la course** : le lecteur lit, dans cet ordre, ce plan, le texte gelé (sections nommées au § 3), l'addendum v3,
   la contre-lecture de la commande v8, puis le journal `journal-course-b-alpha-v5.md`. Il **déclare par écrit**, avant d'ouvrir un
   fichier de `diag/`, ce qu'il sait déjà d'un résultat (le journal dit « aucun audit requis » et les étapes faites) et qu'il n'a écrit
   aucune des pièces. Il n'ouvre **ni** `diag/20261115-120622-neuron-lens-b-alpha/` **ni** le verdict R-2915 avant l'étape 6.
1. **Empreintes** : chaque fichier de `diag/20261117-015632-neuron-lens-b-alpha/` qui a un compagnon `.sha256`, et le manifeste.
   Une empreinte fausse : arrêt, rapporté. Les fichiers sans compagnon (`journaux/*.log`) sont relevés avec l'empreinte calculée.
2. **Ce qui décide d'une chaîne en défaut**, pour **chaque série** :
   - `b-alpha-b0.json` : essais des correctifs (1) et (2) sans test sauté ; 31 couches contiguës pour `J`, `npJpp`, `npR` ; aucune
     matrice identité aux couches 0 à 27 ;
   - `b-alpha-b3.json` : code des verdicts sur la référence et les artefacts, comme le tableau B.3 l'attend ;
   - `b-alpha-fumee.json`, `b-alpha-partie2.json`, `addendum-partie2-b-alpha-v1.md` ;
   - puis les conditions (a), (b), (c) et (e) du § 3, lues sur le résumé de `score` et les grandeurs par pôle **de la série**.
3. **Les mesures de chaque série** :
   - lot 16 : `causal_lens_llama-3.1-8b-instruct.json`, `b-alpha-grandeurs.json`, `grandeurs-par-pole-b-alpha-v1.json` ;
   - lot 64 : `causal_lens_lot64_llama-3.1-8b-instruct.json`, `b-alpha-grandeurs-lot64.json`, `grandeurs-par-pole-b-alpha-lot64-v1.json`.
   Vérifier par `b-alpha-measure.json` et `b-alpha-measure-lot64.json` que les lots écrits sont 16 et 64, et par
   `b-alpha-bascule-lot64.json` que le fichier du lot 16 mis de côté a l'empreinte de `measure`.
4. **Le calcul des verdicts par le lecteur**, écrit sans importer ni lire le code des verdicts de la course (`verdicts_b_alpha_v*.py`,
   `b_alpha_lancer_v*.py`). Il est versé avec son résultat (`.py` et `.json`, scellés).
5. Seulement ensuite, `b-alpha-verdicts.json` et `b-alpha-verdicts-lot64.json` (champs `verdict`, `audits_requis`, `motifs_audit`,
   `audit_b7_par_le_haut`), et le code des verdicts de la course (`verdict_b7` et son champ `par_le_haut`), pour comparaison. Tout
   désaccord est rapporté tel quel ; aucun n'est corrigé.
   **Audit joué ou non** : un audit est joué si et seulement si le fichier de son étape existe (`b-alpha-audit-trop-beau.json`,
   `b-alpha-audit-trop-beau-lot64.json`, `b-alpha-audit-tout-negatif.json`), avec, pour « trop beau », les résumés
   `causal_lens_seed1_…` ou `causal_lens_seed1-lot64_…` et les grandeurs de la graine 1. Si les `audits_requis` de la course et les
   fichiers présents divergent, c'est une divergence non résolue, rapportée.
6. Enfin, pour les comparaisons du § 4 seulement : `diag/20261115-120622-neuron-lens-b-alpha/` (résumé de `score`, grandeurs) et le
   verdict R-2915 (`verdict-b-alpha-v1.md` sur `main`), d'où vient le verdict de B-7 de la RTX 4090, pris tel qu'il est écrit.

## 3. Règles (recopiées du texte gelé v6, « Seuil », B, « Critères de lecture gelés », et de l'addendum v3)
Elles s'appliquent **à chaque série séparément**. Valeurs lues : celles que `score` écrit, ponctuelles ; les intervalles sont rapportés
et ne décident de rien. Lentille `npR`, cible « steer 1x », sauf mention. Bornes de couches incluses.

**Couche lisible** : n ≥ 48 pour la cible considérée (n écrit par le code de la course dans les grandeurs ; il n'est pas recalculable,
les fichiers `-causal.pt` n'étant pas versés : le lecteur le dit). Une bande est « partielle » si plus du quart de ses couches est
non lisible.

**Chaîne en défaut** (elle l'emporte sur tout verdict de mesure de la série) :
- (a) `control_med` hors de ±0,10 (|valeur| > 0,10) à une couche de 0 à 27, pour l'une des quatre cibles (« steer 1x », « steer 4x »,
  « ablate win », « ablate pos ») et l'une des quatre lentilles (logits, `J`, `npJpp`, `npR`) ;
- (b) à une couche de 0 à 27, plus de 32 des 64 pôles écartés pour effet nul en « steer 1x » ;
- (c) lentille des logits, `r_med` (« steer 1x ») < 0,80 à l'une des couches 28 à 30 ; ou `npR`, `r_med` < 0,85 à l'une des couches
  28 à 30 ;
- (d) essai du correctif (1) ou (2) en échec ou avec un test sauté ; fumée en échec ;
- (e) pour `J`, `npJpp` ou `npR`, |`r_med`(lentille) − `r_med`(logits)| < 10⁻³ à une couche de 0 à 23 (« steer 1x ») ; ou une matrice
  d'un fichier de lentille égale à l'identité (écart maximal en valeur absolue ≤ 10⁻⁶, après conversion en float32) à une couche de 0
  à 27, contrôlé à B0 avant `score`.

**B-2** — « reproduit » si, à chaque couche lisible : `r_med` ≥ 0,40 (couches 8 à 15), ≥ 0,60 (16 à 23), ≥ 0,85 (24 à 27) ; `pass` ≥ 0,90
(8 à 27) ; témoin : `control_med` hors de ±0,05 à au plus une couche de 0 à 27, et à aucune hors de ±0,10. « Non reproduit » si `pass`
< 0,50 à plus de la moitié des couches lisibles de 16 à 27, ou `r_med` < 0,30 à plus de la moitié des couches lisibles de 16 à 23.
Sinon « autre ».

**B-3** — écart = `r_med`(`npR`) − `r_med`(logits), « steer 1x ». « Reproduit » : écart ≥ +0,20 à chaque couche lisible de 4 à 15. « Non
reproduit » : écart ≤ 0 à plus de la moitié des couches lisibles de 4 à 15. Sinon « autre ».

**B-4** — rapportée, non décisive : `r_med`(`npR`) − `r_med`(`J`) et − `r_med`(`npJpp`), couches 4 à 23.

**B-7** — cible « ablate win », lentille `npR`, lisibilité par le n de cette cible. « Reproduit » : `r_med` < 0,25 à chaque couche
lisible de 0 à 15 **et** ≥ 0,50 à chaque couche lisible de 26 à 29. « Non reproduit » : `r_med` ≥ 0,40 à plus de la moitié des
couches lisibles de 8 à 15 (« par le haut »), ou < 0,30 à plus de la moitié des couches lisibles de 26 à 29 (« par le bas ») ; si les deux tiennent, « non reproduit » par le haut **et** par le bas, les deux dits.
Sinon « autre », couche par couche.

**Verdict de reproduction de la série** : chaîne en défaut → « chaîne en défaut » ; B-2 et B-3 « reproduit » → « reproduit avec la
lentille R publique » ; B-2 ou B-3 « non reproduit » → « non reproduit avec la lentille R publique » ; autre → « partiel », mesure par
mesure. Les couches 28 à 31 ne comptent pour aucun verdict de B-2 ni B-3.

**Audits de symétrie (R4)**, à évaluer par le lecteur sur chaque série, même si la course n'en a requis aucun :
- « trop beau » (`npR`, « steer 1x », valeurs arrondies à 4 décimales) : `r_med` ≥ 0,95 à une couche de 0 à 7, ou `control_med` écrit
  égal à 0 en valeur absolue (`0.0` ou `-0.0`) à au moins 2 couches de 0 à 27 ;
- « tout négatif » : B-2 et B-3 tous deux « non reproduit » ;
- « B-7 par le haut » : B-7 « non reproduit » par le haut.
**Mesures touchées** (fixées ici) : « trop beau » touche B-2, B-3 et le verdict de reproduction de la série ; « tout négatif » touche le
verdict de reproduction de la série ; « B-7 par le haut » touche B-7 de la série (et donc, au lot 64, le verdict de B-7 de la recourse).
**Si le calcul du lecteur déclenche un audit que la course n'a pas joué** : divergence non résolue ; aucun verdict des mesures touchées
pour cette série ; rapporté à la mère. **Si la course a joué un audit que le calcul du lecteur ne déclenche pas** : divergence non
résolue, rapportée ; les verdicts des mesures touchées sont donnés sous les deux lectures (avec et sans l'audit).
**Audit joué** : « trop beau » : le texte gelé ne fixe que sa procédure (témoin bien apparié, pilotage de norme non nulle, `measure` à
la graine 1) ; le lecteur rapporte ces trois éléments et le verdict recalculé à la graine 1, et le verdict des mesures touchées est
**proposé**, non tranché, pour décision de Lazar. « Tout négatif » : son champ `lecture` est une lecture proposée ; aucun verdict après
lui sans la décision de Lazar (addendum v3, § 4). Au-delà de ces déclencheurs, le lecteur signale à part, sans en faire un
verdict, tout aspect trop propre qu'il verrait (valeurs identiques entre lentilles, couches ou séries ; marges collées aux seuils ;
n constant ; intervalles de largeur nulle).

**Critère de l'audit de B-7 « par le haut »** (addendum v3, § 4 ; sans objet si l'audit n'a pas été joué, à appliquer s'il l'a été) :
l'audit tient si (1) `temoin_bien_apparie` est vrai, (2) `pilotage_norme_non_nulle` > 0 pour « steer 1x » et « steer 4x », (3) le
verdict de B-7 recalculé à la graine 1 de la même série est aussi « non reproduit » par le haut. Réserves de la contre-lecture de la
commande v8, à porter telles quelles :
- (1) et (2) sont lus sur la graine 0 de la série, et (2) est le plus petit n par couche, pas une norme ; seul (3) teste la graine 1 ;
- (3) se calcule d'abord par la règle de B-7 ci-dessus sur le résumé de la graine 1 et les n de la graine 1, puis se compare au
  `verdict_b7` du code des verdicts (son champ `par_le_haut`), tout désaccord rapporté ; **(3) se calcule même si la graine 1 tombe en
  chaîne en défaut** : la chaîne en défaut est alors rapportée à côté et ne change pas (3) ;
- issues écrites : l'audit tient → B-7 de la série « non reproduit par le haut, confirmé à la graine 1 » ; il ne tient pas → « non
  reproduit par le haut, non confirmé à la graine 1 », aucune lecture « par le haut » ;
- si l'audit ne tient pas, la lecture de B-7 de la troisième course reste en vigueur, avec son écart de lot ;
- la procédure ci-dessus est celle du plan scellé ; le lecteur n'en change rien.

## 4. Lecture des deux séries (addendum v3, § 3)
- **Verdict de B-7 de la recourse** : celui de la série au **lot 64**. Il remplace, comme lecture de B-7 pour un moniteur, celui de la
  troisième course (RTX 4090, lot 16), qui est rapporté à côté avec son écart de lot. Ce n'est pas un verdict de reproduction.
  **Aucun verdict de B-7 de la recourse** si la série au lot 64 est en chaîne en défaut ou n'a pas été jouée ; la série au lot 16 ne le
  remplace pas.
  Une issue « autre » se lit couche par couche.
- **Verdicts de B-2, B-3 et de la reproduction** : calculés aux deux séries et rapportés avec le verdict R-2915 de la troisième
  course, **qui reste le verdict de B-α**. Tout désaccord de verdict de B-2 ou B-3 entre l'A100 et la RTX 4090 est une divergence non
  résolue, portée à la mère.
- **Comparaisons rapportées, sans critère** :
  - (a) **effet du lot**, même carte : `r_med` d'« ablate win » et d'« ablate pos », couches 0 à 30, quatre lentilles, lot 64 contre
    lot 16, et l'écart maximal |Δ `r_med`| sur ces couches et lentilles ;
  - (b) **effet du matériel**, même lot : A100 lot 16 contre RTX 4090 lot 16 (`diag/20261115-120622-neuron-lens-b-alpha/`), les quatre
    cibles et les quatre lentilles, couches 0 à 30, avec l'écart maximal par cible (rapporté, sans critère) ;
  - (c) **cas sain de déterminisme** : « steer 1x » et « steer 4x », lot 64 contre lot 16 sur l'A100. Le pilotage est le même calcul aux
    deux séries ; l'écart maximal |Δ `r_med`| est pris sur les couches 0 à 30 et les quatre lentilles. Au-delà de 0,01 : **réserve** sur
    la stabilité de la mesure. Un écart (a) est dit « dans le bruit de la mesure » s'il est **inférieur ou égal** à l'écart maximal de
    (c). Ni cette réserve ni (a) ni (b) ne changent un verdict.
- Phrases permises, et seulement elles : si le verdict de B-7 diffère entre A100 lot 16 et A100 lot 64, « B-7 dépend du lot » ; s'il
  diffère entre A100 lot 16 et RTX 4090 lot 16, « B-7 dépend du matériel ». Si l'une des deux séries comparées n'a pas de verdict de
  B-7, « non comparable ». Ni l'une ni l'autre n'est un verdict de reproduction.

## 5. Ambiguïtés vues avant lecture (non arbitrées)
1. Témoin de B-2 et couches non lisibles : la clause dit « une couche de 0 à 27 », sans « lisible » ; les deux lectures sont données
   si elles divergent.
2. Bande partielle et « reproduit » : si le cas se présente, « partielle » pour la bande, et le verdict sous les deux lectures.
3. Bande sans aucune couche lisible : non jugeable, dit tel quel.
4. Valeurs arrondies ou non : si un arrondi à 4 décimales change un côté de seuil, les deux sont donnés.
5. (b) « écartés pour effet nul » : compte par motif écrit par la course ; s'il n'est pas séparé, le dire.
6. Couche 31 : hors de tout contrôle et de tout verdict, sauf le centile commun de `pass`.
7. Comparaison (b) : les deux courses partagent le code, mais le corpus d'activations a été retéléchargé ; si les empreintes du corpus
   (partie 2) diffèrent entre les deux courses, le lecteur le dit, et la comparaison (b) mêle alors corpus et matériel.

8. (précision de l'auteur du plan, déclarée) Ambiguïté 7 ci-dessus et l'« écart maximal par cible » de (b) sont des précisions de ce plan,
   non écrites dans l'addendum ; elles ne changent aucun verdict.

## 6. Livrables du lecteur
Dans `docs/notes/neuron-lens-v1/lecture-recourse-b7/`, chacun avec son compagnon `.sha256` :
- `calcul_verdicts_recourse_b7_v1.py` et `calcul-verdicts-recourse-b7-v1.json` ;
- `verdict-recourse-b7-v1.md`, avec la déclaration de l'étape 0. Il donne, dans l'ordre :
  - le verdict en trois lignes ;
  - les chaînes en défaut et les audits, par série ;
  - B-2, B-3, B-4 et B-7 par série ;
  - le verdict de B-7 de la recourse ;
  - les comparaisons (a), (b) et (c) ;
  - les désaccords avec le code de la course, les ambiguïtés rencontrées et ce qui est trop propre.

## 7. Ce que le lecteur ne fait pas
Il ne charge aucun modèle, ne loue aucune machine et ne fait aucun appel payant. Il ne lit aucun autre `diag/` ni `runs/` que les deux
courses nommées, et n'ouvre aucune autre branche. Il ne fait aucun commit et ne réécrit aucun fichier : une correction est un fichier
de version suivante. Il ne lit aucune variable d'environnement et n'affiche aucun secret.
