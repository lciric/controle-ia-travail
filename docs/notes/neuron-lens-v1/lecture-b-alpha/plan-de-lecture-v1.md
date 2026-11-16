# Plan de lecture de la tranche B-α de « Neuron Lens » — v1

Écrit et scellé **avant d'ouvrir un résultat** de la course `20261115-120622-neuron-lens-b-alpha`, le 2026-11-15 (heure de
`date -u` relevée à l'écriture : voir le rapport). Lecteur : sous-agent neuf ; il n'a écrit ni le texte gelé, ni le code, ni les
commandes, ni la course, ni le verdict du volet A. Il applique les critères gelés tels qu'ils sont écrits ; il n'arbitre aucune
ambiguïté : il la signale et donne, s'il y a lieu, le verdict sous chacune des deux lectures.

## Ce que j'ai lu avant ce plan
- Texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`, en entier ; empreinte recalculée
  `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`, égale au compagnon (branche `prep/neuron-lens-v1`, tête `7f29cf08`).
- Journal `docs/notes/neuron-lens-v1/journal-course-b-alpha-v3.md`, empreinte recalculée
  `edd37d374204a0e889d72f1646dbc783ddabe79189cc29734e35e9cd8ef3421e`, égale au compagnon.
- Décision R-2901 (`registres/decisions.md` du dépôt de travail, ligne 2861).
- Les noms des fichiers de `diag/20261115-120622-neuron-lens-b-alpha/` (liste de l'arbre), pas leur contenu.

**Ce que je sais déjà d'un résultat, et que je déclare** : le journal de la course, que la consigne me fait lire d'abord, écrit
« `b0` passé », « aucun défaut (e) », « partie 2 sans écart », « B.3 35/35 » et « verdicts faits, aucun audit R4 requis ». Je
sais donc, avant ce plan, que le code de la course n'a pas déclenché l'audit « trop beau » ni l'audit « tout négatif ». Je ne connais
aucune valeur de mesure ni aucun verdict de B-2, B-3, B-7. Les règles ci-dessous sont celles du texte, recopiées ; aucune n'a été
choisie en vue de ce renseignement.

## Ordre de lecture
1. Empreintes : chaque pièce de `diag/20261115-120622-neuron-lens-b-alpha/` qui a un compagnon `.sha256`, et le manifeste
   `runs/20261115-120622-neuron-lens-b-alpha/manifeste.json`. Une empreinte fausse : arrêt, je le dis. Les fichiers sans compagnon
   (`journaux/*.log`) sont relevés comme tels, avec l'empreinte que je calcule.
2. Ce qui décide d'une chaîne en défaut, dans cet ordre : `b-alpha-b0.json` (essais des correctifs (1) et (2), aucun test sauté ;
   31 couches contiguës pour `J`, `npJpp`, `npR` ; aucune matrice identité aux couches 0 à 27 ; crochets ; conventions lues),
   `b-alpha-b3.json` (code des verdicts de la course sur la référence et les artefacts : attendu du tableau B.3),
   `b-alpha-fumee.json`, `b-alpha-partie2.json` et `addendum-partie2-b-alpha-v1.md`, puis les conditions (a), (b), (c), (e) lues
   sur le résumé de `score` et sur les grandeurs par pôle.
3. Les mesures : résumé de `score` (`causal_lens_llama-3.1-8b-instruct.json`), n par couche et par cible
   (`b-alpha-grandeurs.json`, `grandeurs-par-pole-b-alpha-v1.json`), intervalles.
4. Mon calcul des verdicts, écrit sans importer ni lire le code des verdicts de la course (`verdicts_b_alpha_v*.py`).
5. Seulement ensuite `b-alpha-verdicts.json`, pour comparaison ; tout désaccord est rapporté tel quel.

## Règles que j'applique (recopiées du texte gelé, sections « Seuil », B, et « Critères de lecture gelés »)
Valeurs lues : celles que `score` écrit (valeurs ponctuelles ; les intervalles sont rapportés, ils ne décident de rien). Lentille
`npR`, cible « steer 1x », sauf mention. Bornes de couches incluses.

**Couche lisible** : n ≥ 48 pour la cible considérée (n recalculé par le code de la course à partir du fichier `-causal.pt` ; je ne
peux pas le recalculer moi-même, le fichier des activations n'étant pas versé : je prends le n écrit et je le dis). Bande
« partielle » : plus du quart de ses couches non lisibles.

**Chaîne en défaut** (elle l'emporte sur tout verdict de mesure) :
- (a) `control_med` hors de ±0,10 (|valeur| > 0,10) à une couche de 0 à 27, pour l'une des quatre cibles (« steer 1x »,
  « steer 4x », « ablate win », « ablate pos ») et l'une des quatre lentilles (logits, `J`, `npJpp`, `npR`) ;
- (b) à une couche de 0 à 27, plus de la moitié des 64 pôles (plus de 32) écartés pour effet nul en « steer 1x » ;
- (c) lentille des logits, `r_med` (« steer 1x ») < 0,80 à l'une des couches 28 à 30 ; ou `npR`, `r_med` < 0,85 à l'une des
  couches 28 à 30 ;
- (d) essai du correctif (1) ou (2) en échec ou avec un test sauté ; fumée de la passe en échec ;
- (e) pour `J`, `npJpp` ou `npR`, |`r_med`(lentille) − `r_med`(logits)| < 10⁻³ à une couche de 0 à 23 (« steer 1x ») ; ou une
  matrice d'un fichier de lentille égale à l'identité (écart maximal ≤ 10⁻⁶) à une couche de 0 à 27, contrôlé à B0.
- En plus, conditions d'arrêt de la liste d'arrêt lisibles sur pièces : nombre de couches lues différent de 31 ; écart déclaré par
  la partie 2 de l'addendum ; empreinte d'un fichier d'entrée différente de celle du texte.

**B-2** — « reproduit » si, à chaque couche lisible : `r_med` ≥ 0,40 (couches 8 à 15), ≥ 0,60 (16 à 23), ≥ 0,85 (24 à 27) ;
`pass` ≥ 0,90 (8 à 27) ; et témoin : `control_med` hors de ±0,05 à au plus une couche de 0 à 27, et à aucune hors de ±0,10.
« Non reproduit » si `pass` < 0,50 à plus de la moitié des couches lisibles de 16 à 27, ou `r_med` < 0,30 à plus de la moitié des
couches lisibles de 16 à 23. Sinon « autre ».

**B-3** — écart = `r_med`(`npR`) − `r_med`(logits), « steer 1x ». « Reproduit » : écart ≥ +0,20 à chaque couche lisible de 4 à 15.
« Non reproduit » : écart ≤ 0 à plus de la moitié des couches lisibles de 4 à 15. Sinon « autre ».

**B-4** — rapportée, non décisive : `r_med`(`npR`) − `r_med`(`J`) et − `r_med`(`npJpp`), couches 4 à 23.

**B-7** — cible « ablate win », lentille `npR`, lisibilité par le n de cette cible. « Reproduit » : `r_med` < 0,25 à chaque couche
lisible de 0 à 15 **et** ≥ 0,50 à chaque couche lisible de 26 à 29. « Non reproduit » : `r_med` ≥ 0,40 à plus de la moitié des
couches lisibles de 8 à 15 (« par le haut »), ou < 0,30 à plus de la moitié des couches lisibles de 26 à 29 (« par le bas »).
Sinon « autre », couche par couche.

**Verdict de reproduction** : chaîne en défaut → « chaîne en défaut » ; B-2 et B-3 « reproduit » → « reproduit avec la lentille R
publique » ; B-2 ou B-3 « non reproduit » → « non reproduit avec la lentille R publique » (ne conclut pas sur la chaîne) ; autre →
« partiel », mesure par mesure. Les couches 28 à 31 ne comptent pour aucun verdict de B-2 ni B-3.

**Audits de symétrie (R4)** — « trop beau » (`npR`, « steer 1x », valeurs arrondies à 4 décimales) : `r_med` ≥ 0,95 à une couche de
0 à 7, ou `control_med` écrit égal à 0 en valeur absolue à au moins 2 couches de 0 à 27. « Tout négatif » : B-2 et B-3 tous deux
« non reproduit ». Si l'un se déclenche, le verdict attend l'audit : je le dis et je ne prononce pas. Au-delà de ces deux
déclencheurs gelés, je signale à part, sans en faire un verdict, tout aspect trop propre (positif ou négatif) que je verrais :
valeurs identiques entre lentilles ou couches, marges très larges ou collées aux seuils, n constant, intervalles de largeur nulle.

## Ambiguïtés que je vois dans le texte avant lecture (je ne les arbitre pas)
1. **Témoin de B-2 et couches non lisibles** : la clause du témoin porte sur « une couche de 0 à 27 » sans dire « lisible ». Je
   calcule les deux lectures (toutes les couches ; couches lisibles seules) et je dis si elles divergent.
2. **Bande partielle et « reproduit »** : le texte dit qu'une bande dont plus du quart des couches est non lisible rend la mesure
   « partielle » pour cette bande, sans dire si « reproduit » reste prononçable. Si le cas se présente, je rapporte « partielle »
   pour la bande et le verdict sous les deux lectures.
3. **Bande sans aucune couche lisible** : « chaque couche lisible » serait vrai à vide ; je le signalerais comme non jugeable.
4. **Valeurs arrondies ou non** : les seuils s'appliquent aux valeurs que `score` écrit ; si le fichier porte des valeurs non
   arrondies et qu'un arrondi à 4 décimales change un côté de seuil, je le signale et donne les deux.
5. **(b) « écartés pour effet nul »** : je prends le compte par motif écrit par le code de la course (motif « effet nul », cible
   « steer 1x ») ; si le motif n'est pas séparé des autres, je le dis.
6. **(a) et couche 31, (c) et couche 31** : hors des bornes écrites ; la couche 31 n'entre dans aucun contrôle ni verdict, sauf le
   centile commun de `pass`, que `score` calcule.
7. **Écart de lot** (`measure --ctx-batch 16` au lieu de 64, R-2901) : le fichier de résultats ne le consigne pas ; je vérifie ce
   que le manifeste et les journaux en disent, je dis quelles cibles il peut toucher (pilotage, ablation ou les deux) d'après le code
   de `measure`, et je regarde si un verdict tient à une marge de l'ordre du bruit numérique. Je ne peux pas mesurer cet effet : aucune
   course à lot 64 n'existe pour l'ablation.

## Ce que je ne fais pas
Aucun modèle chargé, aucune machine, aucun appel payant ; rien sous `donnees/` ni `docs/verdicts/` ; aucun autre `diag/` ni `runs/` ;
aucune autre branche ; aucun commit ; aucun fichier réécrit (une correction = un fichier de version suivante).
