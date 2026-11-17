# Plan de lecture de la recourse de la tranche B-α de « Neuron Lens » (carte A100 de 40 Go, lots 16 et 64) — v1

Écrit et scellé **avant d'ouvrir un résultat** de la course `20261117-015632-neuron-lens-b-alpha` (branche des résultats
`calcul/neuron-lens-b-alpha-v6`, tête `ea814779`), le 2026-11-17, entre 07:00 UTC (relevé de `date -u`) et le scellement.
Signé : **Lecteur neuf (sous-agent ; n'a écrit ni le texte gelé, ni le code, ni les commandes, ni la course, ni le premier verdict de
B-α)**. J'applique les critères gelés tels qu'ils sont écrits ; je n'arbitre aucune ambiguïté : je la signale et je donne, s'il y a
lieu, le verdict sous chacune des lectures. Expérience **hors du programme** : rien ici n'ouvre ni ne ferme une porte.

Objet : la mesure de l'effet causal des lentilles (lecture d'un neurone contre pilotage et contre ablation) jouée deux fois sur la
même machine — série « lot 16 » puis série « lot 64 » (le défaut publié). L'enjeu est **B-7 au lot 64** : ce qu'une activation
isolée fait en contexte est-il mal prédit avant les deux tiers de la profondeur.

## 1. Ce que j'ai lu avant ce plan (empreintes recalculées par moi)

| pièce | empreinte SHA-256 recalculée | constat |
|---|---|---|
| texte gelé v6 (copie reçue ; `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`, branche `prep/neuron-lens-v1`, tête `182c7eaa`) | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` | égale au compagnon ; lu en entier (593 lignes) |
| addendum de la recourse, **copie reçue** | `92f16b975bda27a2598da3ca907b6edd9c5702e6919c2345470003b3f56a30d5` | **c'est la v2**, pas la pièce annoncée (`5f05f5bc…`) : voir ci-dessous |
| addendum de la recourse **v3** (`…/addendum-texte-gele-v6-recourse-b7-a100-v3.md`, branche de préparation) | `5f05f5bc5cae8e1ef41ace349ba54046baf8bfdb7657140ad7addbf0c0ad908a` | égale au compagnon et à l'empreinte de ma consigne ; lue par sa différence avec la v2 |
| addendum des empreintes v3 | `e63d95caa06fde0cb23d2b0dbcd143413d822be9487edf8f54fe72b46db0df82` | égale au compagnon |
| journal de la cinquième course (v5) | `3047ff1c1f73c31ba84a34f4517e8443faede31aafa5624ec079d9483d082e91` | égale au compagnon |
| premier plan de lecture (v1) | `5a79991850459ca13469edbd51e91619b50c23fe80085cc1a9e17ff217d831da` | structure reprise, pas le texte |
| premier verdict (v1) | `ca06acb1550ccc76fef1ec89ae0aec170c5f05252bda2711f131eaa0e645fc1d` | lu en entier |
| contre-lecture de la commande v8 (`…/contre-lectures/contre-lecture-commande-b-alpha-v8-v1.md`) | `a6b7a9ccf25eb249c93f8745a220ae2708e9b9e2728327f2808b640974bb8eeb` | lignes 28 à 75 : source des quatre réserves |
| code des verdicts de la course (`src/controle_ia/neuron_lens/verdicts_b_alpha_v3.py`, branche de préparation) | `8f57088ae4b29affd8863015a99675138ceb19044354964719b82ca0efaa54a0` | lignes 24 à 36, 78 à 134, 163 à 197 seulement (réserve 2) |
| lanceur v5 (`…/b_alpha_lancer_v5.py`) | `c6a5d5db0272e4775d48b828b1d5f3904bf0b32d8d5ccdcc87c283effd7895b9` | lignes 699 à 726, 818 à 842, 862 à 892 : noms des clés écrites |
| copie du code publié de la mesure (`docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/scripts-checks-causal_lens.py.txt`) | `befb7018f1be937124d938df7b318d0b9e8fd32fd3c497111c7c1722c3b187c6` | lignes 66 à 76, 125 à 131, 284 à 300, 378 et 379 : graine, témoin, lots |
| premier calcul du lecteur (`…/lecture-b-alpha/calcul_verdicts_b_alpha_v1.py`) | `18d82258…` (compagnon) | recherche des clés lues, pas de lecture suivie |

Les **noms** des fichiers de `diag/20261117-015632-neuron-lens-b-alpha/` et de `runs/…` (liste de l'arbre), pas leur contenu.

**Écart de pièce, déclaré** : la copie de l'addendum qu'on m'a remise est la v2 (« archivée, jamais jouée ») ; le journal de la course
cite la v3, et l'empreinte de ma consigne est celle de la v3. **Je lis selon la v3.** Elle ne diffère de la v2 que par le critère de
l'audit de B-7 « par le haut » (§ 4), la phrase « un ou deux audits » et une taille de fichier ; le § 3 (lecture des deux séries) est
identique. **Écart à l'indépendance du premier plan, déclaré** : pour la réserve 2, j'ai lu la fonction `verdict_b7` et ses voisines
dans le code de la course. Mon calcul reste écrit à partir du texte gelé ; là où le code et le texte diffèrent, le texte fait foi et
je rapporte l'écart.

## 2. Ce que je sais déjà d'un résultat, et que je déclare

- Par le journal de la course : « `b0` passé » (essais 7/7, 8/8, 4/4, 13/13, B.3 35/35, aucun arrêt ni défaut (e)), « partie 2 sans
  écart », la mesure au lot 64 « passée en mémoire », « **aucun audit requis** » aux deux séries, `verifier_resultat` 18 sur 18.
- Ce que cela implique, vu le code lu (lanceur, lignes 826 à 838) : aux deux séries le code de la course n'a écrit ni « trop beau », ni
  « tout négatif », ni **B-7 « non reproduit » par le haut** ; et la liste des fichiers ne porte aucun résumé de la graine 1
  (`causal_lens_seed1…`), ce qui s'accorde avec « aucun audit ». Je sais donc, avant ce plan, que la procédure d'audit du § 6 a peu de
  chances de servir ; je l'écris quand même en entier, et je la suivrais si mon propre calcul la déclenchait.
- Par le premier verdict : les valeurs de la **troisième course** (autre carte, lot 16) — B-2 « autre » (couches 8 et 10), B-3
  « reproduit » de justesse à la couche 4 (0,2085), B-7 « autre » avec la seule couche 15 manquée (0,3097 pour 0,25). Le pilotage
  étant « le même calcul », je m'attends à des valeurs proches ; cette attente ne fixe aucune règle ci-dessous.
- Je ne connais **aucune valeur de mesure ni aucun verdict** de la recourse. Aucune règle n'a été choisie en vue de ces renseignements.

## 3. Ordre de lecture (D = `diag/20261117-015632-neuron-lens-b-alpha/`)

1. **Empreintes.** Chaque fichier de D qui a un compagnon `.sha256` et `runs/20261117-015632-neuron-lens-b-alpha/manifeste.json` :
   empreinte recalculée égale au compagnon. Une empreinte fausse : arrêt, je le dis. Les dix `journaux/*.log`, sans compagnon, sont
   relevés avec l'empreinte que je calcule.
2. **Pièces de la chaîne, communes aux deux séries** : `b-alpha-b0.json`, `b-alpha-b3.json`, `b-alpha-fumee.json`,
   `b-alpha-partie2.json` et `addendum-partie2-b-alpha-v1.md`, `b-alpha-corpus.json`, `b-alpha-passe.json`.
3. **Pièces propres à la recourse** : `b-alpha-measure.json`, `b-alpha-bascule-lot64.json`, `b-alpha-measure-lot64.json`,
   `journaux/measure.log`, `journaux/measure-lot64.log`, `b-alpha-score.json`, `b-alpha-score-lot64.json` (§ 5, réserve 1 et contrôles
   de série).
4. **Mesures de la série lot 16** : `causal_lens_llama-3.1-8b-instruct.json`, `b-alpha-grandeurs.json`,
   `grandeurs-par-pole-b-alpha-v1.json`.
5. **Mesures de la série lot 64** : `causal_lens_lot64_llama-3.1-8b-instruct.json`, `b-alpha-grandeurs-lot64.json`,
   `grandeurs-par-pole-b-alpha-lot64-v1.json`.
6. **Mon calcul**, par un programme écrit par moi à partir du § 4, sans importer le code de la course ; sa sortie est scellée.
7. **Ensuite seulement** `b-alpha-verdicts.json` et `b-alpha-verdicts-lot64.json`, et l'appel de `verdict_b7` (réserve 2), pour
   comparaison ; tout désaccord est rapporté tel quel.
8. **Comparaisons** du § 7, la troisième course ouverte en dernier.

## 4. Règles que j'applique, à chaque série séparément (recopiées du texte gelé v6 ; ajouts de l'addendum v3 marqués)

**Où je lis** (procédure exacte, réserve 4). Dans le résumé de `score` de la série : `targets[cible][lentille][grandeur][l]`, avec
cible ∈ {« steer 1x », « steer 4x », « ablate pos », « ablate win »}, lentille ∈ {`logit`, `J`, `npJpp`, `npR`}, grandeur ∈ {`r_med`,
`pass`, `control_med`}, l de 0 à 31 (je vérifie `targets[c][s]["layer"] == [0..31]` et `lenses`). Dans le fichier de grandeurs de la
série : `resultat.n[cible][l]` et `resultat.ecartes[cible][motif][l]`. Dans les grandeurs par pôle : `poles[i]` (`couche`,
`aleatoire`, `lectures[cible][lentille]` avec `motif`, `r`, `r_temoin`) et `fidelite_a_score`. Si une clé manque ou porte un autre
nom, je le dis et je ne devine pas. Valeurs ponctuelles telles que `score` les écrit ; bornes de couches incluses ; les intervalles
(2 000 rééchantillonnages des pôles, les miens) sont rapportés et ne décident de rien.

**Couche lisible** : `resultat.n[cible][l]` ≥ 48. Bande « partielle » : plus du quart de ses couches non lisibles. Je ne peux pas
recalculer n (fichiers bruts de `measure` perdus avec la machine) : je prends le n écrit, je le recoupe avec le compte des pôles de
`motif` « retenu », et je le dis.

**Chaîne en défaut** (elle l'emporte sur tout verdict de mesure de la série) :
- (a) |`control_med`| > 0,10 à une couche de 0 à 27, pour l'une des quatre cibles et l'une des quatre lentilles ;
- (b) à une couche de 0 à 27, `resultat.ecartes["steer 1x"]["effet nul"][l]` > 32 ;
- (c) `r_med` (« steer 1x ») de `logit` < 0,80, ou de `npR` < 0,85, à l'une des couches 28 à 30 ;
- (d) `b-alpha-b0.json`, `resultat.essais[*]` : un `code` ≠ 0 ou un `resume` portant « skipped », « failed » ou « error » ;
  `b-alpha-fumee.json`, `resultat.code` ≠ 0 ; (**ajout de l'addendum**, § 2.3) cette condition est maintenant lue par le code de la
  course : je compare ma lecture à `resultat.essais_ok` et `resultat.essais_en_defaut` des deux fichiers de verdicts ;
- (e) pour `J`, `npJpp` ou `npR`, |`r_med`(lentille) − `r_med`(`logit`)| < 0,001 à une couche de 0 à 23 (« steer 1x ») ; ou, dans
  `b-alpha-b0.json`, `resultat.lentilles[s].defauts` non vide (matrice identité, couches 0 à 27) ;
- arrêts lisibles sur pièces : `resultat.lentilles[s].arrets` non vide ou sortie sans « layers 0-30 » ; écart déclaré par la partie 2 ;
  `resultat.verdicts_b3` de `b-alpha-b0.json` et de `b-alpha-b3.json` différent de l'attendu du tableau B.3.

**B-2** (`npR`, « steer 1x ») — « reproduit » si, à chaque couche lisible : `r_med` ≥ 0,40 (8 à 15), ≥ 0,60 (16 à 23), ≥ 0,85 (24 à
27) ; `pass` ≥ 0,90 (8 à 27) ; et |`control_med`| > 0,05 à au plus une couche de 0 à 27, > 0,10 à aucune. « Non reproduit » si `pass`
< 0,50 à plus de la moitié des couches lisibles de 16 à 27, ou `r_med` < 0,30 à plus de la moitié des couches lisibles de 16 à 23.
Sinon « autre ».

**B-3** — écart = `r_med`(`npR`) − `r_med`(`logit`), « steer 1x ». « Reproduit » : ≥ +0,20 à chaque couche lisible de 4 à 15. « Non
reproduit » : ≤ 0 à plus de la moitié des couches lisibles de 4 à 15. Sinon « autre ».

**B-4** — rapportée, non décisive : `r_med`(`npR`) − `r_med`(`J`) et − `r_med`(`npJpp`), couches 4 à 23.

**B-7** — `targets["ablate win"]["npR"]["r_med"][l]`, lisibilité par `resultat.n["ablate win"][l]`. « Reproduit » : < 0,25 à chaque
couche lisible de 0 à 15 **et** ≥ 0,50 à chaque couche lisible de 26 à 29. « Non reproduit » **par le haut** : ≥ 0,40 à plus de la
moitié des couches lisibles de 8 à 15 ; **par le bas** : < 0,30 à plus de la moitié des couches lisibles de 26 à 29. Sinon « autre »,
couche par couche. Lecture pour un moniteur selon le tableau gelé (« reproduit » : une étiquette de neurone décrit une poussée
moyenne et ne lit pas un épisode, pour toute lentille ; « par le bas » : rapporté ; « par le haut » : audit avant toute lecture, § 6).

**Verdict de reproduction de la série** : chaîne en défaut → « chaîne en défaut » ; B-2 et B-3 « reproduit » → « reproduit avec la
lentille R publique » ; B-2 ou B-3 « non reproduit » → « non reproduit avec la lentille R publique » ; autre → « partiel », mesure par
mesure. Les couches 28 à 31 ne comptent pour aucun verdict de B-2 ni B-3.

**Audits de symétrie gelés (R4)**, évalués à chaque série sur ses propres valeurs — « trop beau » (`npR`, « steer 1x », valeurs
arrondies à 4 décimales) : `r_med` ≥ 0,95 à une couche de 0 à 7, ou `control_med` écrit égal à 0 en valeur absolue à au moins 2
couches de 0 à 27. « Tout négatif » : B-2 et B-3 tous deux « non reproduit » à l'une des séries. Si l'un se déclenche : § 6.

**Ajouts de l'addendum v3, § 3** :
- Le **verdict de B-7 de la recourse est celui de la série lot 64**, par les seuils ci-dessus. Il remplace, comme lecture de B-7 pour
  un moniteur, celui de la troisième course, rapporté à côté avec son écart de lot ; ce n'est pas un verdict de reproduction.
- **Aucun verdict de B-7 de la recourse** si la série lot 64 est en « chaîne en défaut » ou n'a pas été jouée : la série lot 16 de la
  même carte **ne le remplace pas** ; la lecture reste celle de la troisième course et la recourse est rapportée « sans verdict de B-7 ».
- B-2, B-3 et la reproduction sont calculés aux deux séries et **rapportés** ; le verdict de B-α reste celui de la troisième course
  (« partiel », premier verdict `ca06acb1…`) sauf mot de Lazar. Tout désaccord de verdict de B-2 ou de B-3 entre la carte A100 et la
  carte de la troisième course est une **divergence non résolue**, portée à la mère ; je ne l'arbitre pas.
- B-7 différent entre les deux lots de la même carte : « B-7 dépend du lot » ; différent entre la série lot 16 et la troisième
  course : « B-7 dépend du matériel » ; les deux peuvent être dites ; aucune n'est un verdict de reproduction.

## 5. Les quatre réserves de la contre-lecture (R-3056), traitées

**Réserve 1 — la graine 0 du témoin.** Oui, d'après le code lu : le lanceur ne passe `--seed` à `measure` et à `score` que pour la
graine 1 de l'audit ; les deux séries tirent donc leurs neurones par `random.Random(0)`, et le témoin d'un pôle est la lecture du
neurone tiré suivant de la même couche (copie du code publié, lignes 297 à 299). Je le vérifie sur pièces : (i) aucune option
`--seed` dans la ligne de commande de `journaux/measure.log`, `journaux/measure-lot64.log`, `journaux/score.log`,
`journaux/score-lot64.log` ; (ii) aucun fichier `causal_lens_seed1…` dans D ; (iii) la suite des pôles (`couche`, neurone, signe) est
la même dans les deux fichiers de grandeurs par pôle, et la même que celle de la troisième course. Lecture que j'en tire :
- les deux séries et la troisième course portent **les mêmes 32 neurones par couche et le même appariement du témoin** : un témoin
  proche de zéro trois fois n'est pas trois confirmations ; l'accord entre séries ne dit rien de la variance d'échantillonnage des
  neurones (seule la graine 1 la toucherait, et elle n'est jouée que sur audit) ;
- si un audit a tourné, ses champs `temoin_bien_apparie` et `pilotage_norme_non_nulle` sont calculés sur les grandeurs de la **graine
  0** de la série : **je les lis tels que versés, ils concernent la série** ; `pilotage_norme_non_nulle` est un plus petit nombre de
  pôles retenus, pas une norme ; **seul le point (3) du § 6 est le test de la graine 1** ;
- si (i), (ii) ou (iii) n'est pas tenu, je le rapporte comme écart à la chaîne gelée et je ne prononce pas B-7.

**Réserve 2 — `verdict_b7` et son champ `par_le_haut`.** Le code écrit `par_le_haut` vrai si et seulement si `r_med` (« ablate win »,
`npR`) ≥ 0,40 à plus de la moitié des couches lisibles de 8 à 15 **et** si cette bande n'est pas partielle ; `par_le_bas`, de même,
pour < 0,30 aux couches 26 à 29. Vérification, à chaque série : après avoir scellé mon calcul, je lis dans le fichier de verdicts
`resultat.verdict` (champ de B-7 : `verdict` et `details.par_le_haut`, `details.par_le_bas`), `resultat.audit_b7_par_le_haut`,
`resultat.motifs_audit`, `resultat.audits_requis` ; puis j'appelle `verdict_b7(t, n)` de `verdicts_b_alpha_v3` (et **non**
`verdict()`, qui rend B-7 vide en cas de chaîne en défaut), `t` monté comme au lanceur (`targets[cible][lentille]`), `n` =
`resultat.n`. Cohérence exigée : mon « par le haut » = `details.par_le_haut` = `audit_b7_par_le_haut` = présence de
« audit-trop-beau » pour ce motif. Écarts de libellé connus d'avance, sans effet sur l'issue : le code dit « partiel » où le texte dit
« autre » ; le code ne prononce pas « non reproduit » sur une bande partielle (ambiguïté 2). Tout désaccord de fond (mon calcul dit
« par le haut », le code non, ou l'inverse) : B-7 de la série **n'est pas prononcé**, les deux calculs sont rapportés, réserve 3.

**Réserve 3 — repli sur la lecture de la troisième course.** Pour la série lot 64, **je ne prononce pas le verdict de B-7 de la
recourse**, et la lecture de B-7 **en vigueur reste celle de la troisième course** (autre carte, lot 16 : « autre », couche par
couche, avec son écart de lot ; premier verdict `ca06acb1…`), dans chacun de ces cas : (i) chaîne en défaut de la série lot 64, ou
série non jouée ; (ii) un déclencheur gelé « trop beau » ou « tout négatif » sans pièce d'audit, ou dont l'audit ne lève pas le
doute ; (iii) B-7 « par le haut » dont l'audit du § 6 ne tient pas, manque, ou est illisible — rapporté alors « non reproduit par le
haut, non confirmé à la graine 1 », sans lecture pour un moniteur ; (iv) désaccord de fond de la réserve 2 ; (v) réserve 1 non tenue.
La série lot 16 de la carte A100 ne sert jamais de remplaçante. La recourse est alors rapportée « sans verdict de B-7 ».

**Réserve 4 — procédure exacte.** Chaque étape des §§ 3 à 7 nomme la valeur, le fichier, la clé et le seuil ; rien d'autre n'est à
décider après l'ouverture. Ce que je n'ai pas pu fixer est au § 8 et ne sera pas arbitré.

## 6. Procédure d'audit (R4), si elle est requise par le code ou par mon calcul

- **B-7 « par le haut » à une série** (addendum v3, § 4). L'audit de la série **tient** si, ensemble : (1) `temoin_bien_apparie` est
  vrai dans le résultat de l'audit (fichier de l'étape « audit-trop-beau » de la série ; lu tel que versé) ; (2)
  `pilotage_norme_non_nulle` > 0 pour « steer 1x » et « steer 4x » (lu tel que versé) ; (3) `verdict_b7(t1, n1)` rend « non
  reproduit » avec `details.par_le_haut` vrai, où `t1` = `targets` du résumé de la graine 1 (`causal_lens_seed1_…json` au lot 16,
  `causal_lens_seed1-lot64_…json` au lot 64) et `n1` = `grandeurs.n` du résultat de l'audit ; je refais (3) aussi par mon propre
  calcul. S'il tient : « non reproduit par le haut, confirmé à la graine 1 » — lecture valable en contexte plus tôt que publié. S'il
  ne tient pas : réserve 3, cas (iii). Une chaîne en défaut à la graine 1 est rapportée à côté ; (3) se lit quand même sur `verdict_b7`.
- **« Trop beau »** (pilotage) : le verdict de la série attend l'audit à la graine 1 ; sans ses pièces, je ne prononce rien pour la
  série. **« Tout négatif »** : le champ `lecture` de l'audit est une lecture proposée ; aucun verdict après lui sans décision de Lazar.
- **Au-delà des déclencheurs gelés**, je signale à part, dans les deux sens, tout aspect trop propre, sans en faire un verdict : n
  constant et aucun pôle écarté ; valeurs identiques entre lentilles, couches ou séries ; marges collées aux seuils ou très larges ;
  intervalles de largeur nulle ; ablation au lot 64 identique au bit près à celle du lot 16 (§ 7, contrôle de série).

## 7. Comparaisons de l'addendum § 3 — rapportées, sans critère ; aucune ne change un verdict

**Contrôle de série, d'abord** : `b-alpha-measure.json` → `resultat.lot` = 16 ; `b-alpha-measure-lot64.json` → `resultat.lot` = 64 ;
`--ctx-batch 16` et `--ctx-batch 64` dans les lignes de commande des deux journaux de `measure`, aucun autre paramètre de mesure ;
`b-alpha-bascule-lot64.json` → `resultat.deplaces[…].sha256` égale à `b-alpha-measure.json` → `resultat.causal.sha256` ; les deux
`resultat.causal.sha256` comparées entre elles (égales : je le signale comme réserve, sans conclure) ; `meta` des deux résumés égaux
entre eux et aux défauts gelés (32 par couche, 16 contextes, 64 jetons, doses 1 et 4, fenêtre 8, 8 premiers documents).

- **(c) Cas sain de déterminisme, lu avant (a)** : Δ = `r_med`(lot 64) − `r_med`(lot 16), carte A100, pour « steer 1x » et « steer
  4x », quatre lentilles, couches 0 à 31 (256 valeurs) ; je rapporte max |Δ| et où il tombe, à part pour les couches 0 à 27, et le
  même écart sur `pass` et `control_med`. **Seuil de l'addendum : max |Δ `r_med`| > 0,01 → réserve** sur la stabilité de la mesure.
- **(a) Effet du lot, même carte** : Δ = `r_med`(lot 64) − `r_med`(lot 16) pour « ablate win » et « ablate pos », par couche (0 à 31)
  et par lentille ; tableau entier pour `npR`, max |Δ| par cible et lentille, et l'écart à chaque couche qui décide de B-7 (0 à 15, 26
  à 29) mis en regard de sa marge au seuil. Les écarts (a) inférieurs ou égaux au max de (c) sont dits « dans le bruit de la mesure ».
  En complément, par pôle : distribution de `r`(lot 64) − `r`(lot 16), « ablate win », `npR`, par couche (médiane, extrêmes).
- **(b) Effet du matériel, même lot** : Δ = `r_med`(carte A100, lot 16) − `r_med`(troisième course, lot 16), quatre cibles, quatre
  lentilles, couches 0 à 31 ; max |Δ| par cible et lentille ; de même `pass` et `control_med` pour `npR`. Source de la troisième
  course : `causal_lens_llama-3.1-8b-instruct.json`, `b-alpha-grandeurs.json`, `grandeurs-par-pole-b-alpha-v1.json` de la course
  `20261115-120622-neuron-lens-b-alpha`, acceptés seulement si leurs empreintes commencent par `904a512a`, `c8fe14b7`, `28d20e41`
  (premier verdict). Je ne les ouvre qu'à cette étape, et seulement si la consigne de lecture me donne ce chemin.
- **Phrases de conclusion** : les verdicts de B-7 des trois mesures (troisième course ; A100 lot 16 ; A100 lot 64) côte à côte, puis
  « B-7 dépend du lot » et « B-7 dépend du matériel » selon le § 4 ; les verdicts de B-2 et B-3 côte à côte, et la divergence s'il y
  en a une.

## 8. Ambiguïtés que je vois avant lecture (je ne les arbitre pas)

1. **Témoin de B-2 et couches non lisibles** : la clause dit « une couche de 0 à 27 » sans « lisible » ; le code ne compte que les
   lisibles. Je calcule les deux.
2. **Bande partielle** : le texte ne dit pas si « reproduit » ou « non reproduit » restent prononçables sur une bande partielle ; le
   code ne prononce ni l'un ni l'autre (« lecture déclarée » du code, absente du texte). Les deux lectures sont données si le cas se présente.
3. **Bande sans couche lisible** : « chaque couche lisible » vrai à vide ; signalé comme non jugeable.
4. **Arrondi** : seuils sur les valeurs écrites ; le code arrondit l'écart de B-3 à 4 décimales et pas le reste. Si un arrondi change
   un côté de seuil, je donne les deux.
5. **« Par le haut » et « par le bas » ensemble** : possibles tous deux ; le texte ne dit pas lequel prime. Je rapporterais les deux,
   l'audit d'abord.
6. **Déclencheur « tout négatif » à une seule série** : l'addendum le dit requis « si l'une des séries le déclenche » ; il ne dit pas
   si le verdict de l'autre série attend aussi. Je ne prononcerais ni l'un ni l'autre et je le porterais à la mère.
7. **Seuil de 0,01 du cas sain (c)** : « choisi ici, non sourcé » ; l'addendum ne dit ni les lentilles ni les couches (je prends
   tout, et 0 à 27 à part), ni ce que vaut « de même ordre » (je ne garde que « inférieur ou égal », et je donne le rapport). Si (c)
   vaut exactement zéro, aucun écart (a) non nul n'est « dans le bruit » par cette règle : je le dirais tel quel.
8. **Marges de B-7 de l'ordre de l'effet du lot ou du matériel** : aucun seuil gelé ne lie (a) ou (b) au verdict. Si une couche qui
   décide est plus près de son seuil que max |Δ| de (a) ou de (b), le verdict est prononcé sur la valeur ponctuelle et la fragilité
   est écrite à côté.
9. **« Remplace » et « dépend du matériel »** : si le verdict au lot 64 diffère de celui de la troisième course, l'addendum fait
   remplacer une lecture par l'autre alors que carte **et** lot ont changé ; (a) et (b) séparent les deux effets, sans critère.
10. **Séries non indépendantes** : même passe, même corpus, même machine, mêmes neurones (réserve 1) ; l'accord des deux séries
    n'est pas une reproduction. Les fichiers bruts de `measure` sont perdus : ni n ni les corrélations ne sont recalculables.
11. **Condition (d)** : effective dans le code depuis cette course seulement ; ma lecture sur pièces fait foi pour moi, comparée à
    `essais_ok`.

## 9. Ce que je ne fais pas

Aucun modèle chargé, aucune machine, aucun appel payant, aucune relance de série (interdite sans décision de Lazar, quel que soit le
résultat) ; rien sous `donnees/`, `docs/verdicts/`, `docs/notes/bras-attaque/` ; aucun autre `diag/` ni `runs/` que ceux nommés aux
§§ 3 et 7 ; aucune autre branche que `prep/neuron-lens-v1` et `calcul/neuron-lens-b-alpha-v6` sans consigne ; aucun commit ; aucun
fichier réécrit (une correction = un fichier de version suivante) ; aucun arbitrage d'ambiguïté, de divergence entre cartes, ni de la
question « un écart de lot est-il un écart au texte gelé ». Le verdict sera soumis à Lazar par la mère.
