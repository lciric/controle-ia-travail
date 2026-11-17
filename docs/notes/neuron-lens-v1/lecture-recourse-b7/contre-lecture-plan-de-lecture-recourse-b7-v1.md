# Contre-lecture neuve (R2) — plan de lecture de la recourse de B-7 (B-α, A100, lots 16 et 64) — v1

Contre-lecteur neuf : n'a rien écrit des pièces. Branche `prep/neuron-lens-v1`. Aucun fichier de résultat de
`diag/20261117-015632-neuron-lens-b-alpha/` ni de `runs/20261117-015632-neuron-lens-b-alpha/` ouvert (noms listés seulement ; compagnon du
manifeste vérifié par l'outil de scellement, sans affichage). `diag/20261115-120622-…` et le verdict de la troisième course non ouverts. Aucune
commande `vastai`, aucun code voisin exécuté, aucune variable d'environnement affichée, aucun fichier existant modifié, aucun commit. Seul ajout : ce
fichier.

Pièces lues : plan v1 de la recourse ; texte gelé v6 (« Seuil » B, B.1, étapes, B.3, critères de lecture, audit symétrique, liste d'arrêt) ;
addendum v3 en entier ; contre-lecture de la commande v8 ; plan modèle de la troisième course (`origin/main`).

## Verdict

**À corriger.** Les seuils, bandes et définitions recopiés sont fidèles ; mais une règle de l'audit de B-7 « par le haut » dit l'inverse d'une
réserve de la contre-lecture v8, la procédure de cet audit n'est pas complète (fichiers, fonction), et quelques cas laissent une lecture ouverte.

## Bloquantes

**B1 — graine 1 en chaîne en défaut : le plan dit « indéfini, l'audit ne tient pas ».** Lignes 97-98 : « si la graine 1 tombe en chaîne en défaut,
(3) est indéfini : rapporté à côté, l'audit "ne tient pas" ». La contre-lecture v8, réserve 2, dit : « `verdict()` rend `b7 = None` […] alors que
`verdict_b7` reste calculable. Dans ce cas, (3) se lit sur `verdict_b7`, et la chaîne en défaut de la graine 1 est rapportée à côté. » L'addendum
v3 (§ 4) ne dit rien d'une chaîne en défaut de la graine 1 : (3) est le verdict de B-7 recalculé, point. Le plan inverse la réserve et invente une
issue qui fait échouer l'audit. Devrait être écrit : « (3) se calcule par la règle de B-7 sur le résumé et les n de la graine 1, même si la
graine 1 est en chaîne en défaut ; cette chaîne en défaut est rapportée à côté, sans changer (3) ». (Si l'on veut l'autre règle, c'est un écart à
l'addendum scellé : nœud de décision, pas un choix du plan.)

## Majeures

**M1 — procédure de l'audit incomplète (réserve 4 de la v8 : « le plan doit contenir la procédure exacte de 1 à 3 »).** Lignes 92-100. L'ordre de
lecture (§ 2, lignes 26-43) ne cite nulle part les pièces de l'audit : résumés `causal_lens_seed1_<modèle>.json` et
`causal_lens_seed1-lot64_<modèle>.json`, résultat de l'audit (champs `temoin_bien_apparie`, `pilotage_norme_non_nulle`, `grandeurs.n` de la
graine 1). Le plan ne dit pas non plus comment le lecteur constate qu'un audit a été « joué » (présence de ces fichiers ? champ du résultat de
`b-alpha-verdicts*.json` ?). Le listage montre qu'aucun fichier `seed1` n'existe aujourd'hui : cohérent avec « aucun audit », mais le plan doit
dire, avant ouverture : audit joué = [critère de constat] ; fichiers attendus = [noms] ; si un audit est annoncé par le code de la course et que
ces fichiers manquent, ou l'inverse, c'est une divergence non résolue.

**M2 — (3) : « règle de B-7 par le lecteur » contre « par le code des verdicts ».** Ligne 96-97 : « (3) se calcule par la règle de B-7 ci-dessus
(le champ "par le haut") ». L'addendum v3 (§ 4) : « par le code des verdicts (`verdicts_b_alpha_v3`) […] sans code ni location en plus » ; la
v8 demande de nommer `verdict_b7` et le champ `par_le_haut`, pas `verdict()`. Le plan ne nomme ni l'un ni l'autre, et son § 2.4 interdit au lecteur
de lire ce code avant son calcul. Les deux sont compatibles à condition de l'écrire : « le lecteur calcule (3) par sa propre application de la règle
de B-7 ; il compare ensuite à `verdict_b7(...)["details"]["par_le_haut"]` de la course ; tout désaccord est rapporté, aucun n'est corrigé ». Sans
cela, il reste ouvert laquelle des deux fait foi pour (3).

**M3 — audits « trop beau » et « tout négatif » : lecture si jouée, et « mesure touchée » non définie.** Lignes 82-90. (i) Seul l'audit de B-7 a un
critère de « tient / ne tient pas ». Si la course a joué un audit « trop beau » ou « tout négatif », le plan ne dit pas comment le lire (texte gelé :
témoin apparié, pilotage de norme non nulle, `measure` à la graine 1, verdict après l'audit ; addendum § 4, lignes 80-82 : `lecture` est « proposée »,
« aucun verdict après lui sans la décision de Lazar »). Ce dernier point n'est pas repris. (ii) « Aucun verdict de la mesure touchée » : pour « trop beau »
(lit `npR` « steer 1x »), la mesure touchée est-elle B-2, B-3, B-4 et le verdict de reproduction de la série ? Pour « tout négatif », idem ?
Non dit : le lecteur choisirait après coup. (iii) Cas inverse non couvert : audit joué par la course que le calcul du lecteur ne déclenche pas.

**M4 — comparaison (c) et (a) : deux notions floues, choix laissé après coup.** Lignes 110-117. « Écarts (a) de même ordre ou moindres » (addendum § 3,
repris tel quel) n'a pas de définition chiffrée ; « écart maximal » de (c) ne dit pas sur quelles couches (0 à 31 ? 0 à 30 ? la couche 31 est
« exactement la lentille des logits » pour `J`, `npJpp`, `npR`) ni sur quelles lentilles (les quatre ?). Sans règle écrite, la phrase « dans le bruit de la
mesure » dépendra d'un choix du lecteur après avoir vu les écarts. À fixer avant : couches et lentilles du maximum de (c) ; « de même ordre ou moindres »
= écart maximal de (a) ≤ écart maximal de (c) (ou autre règle explicite, à décider par Lazar si l'on veut s'écarter de la lettre).

**M5 — ordre de lecture et exposition du lecteur (question d).** (i) § 0 fait « recalculer » l'empreinte du journal de la course
`journal-course-b-alpha-v5.md`, mais le plan ne dit pas si le lecteur le lit, ni quand ; l'auteur reconnaît (§ 1) que le journal annonce que les séries
sont allées jusqu'aux verdicts. Si le journal contient des verdicts ou des valeurs, le lecteur les verrait avant son calcul. À écrire : « le journal est
lu après l'étape 4, ou seulement ses empreintes sont vérifiées avant ». (ii) Le plan n'indique pas quand le lecteur peut lire
`diag/20261115-120622-…` et le verdict R-2915 de la troisième course, ni d'où vient le verdict de B-7 de la RTX 4090 pour « B-7 dépend du matériel »
(pris au verdict R-2915 ? recalculé ?). À écrire dans l'ordre (après l'étape 4, avant ou après l'étape 5), avec la source. (iii) Le plan affirme que le
lecteur « n'a écrit » aucune pièce mais ne lui demande pas de le déclarer ni de déclarer ce qu'il a lu avant de commencer ; le modèle de la troisième
course portait cette déclaration côté auteur seulement, donc c'est la même lacune ; à ajouter en tête de `verdict-recourse-b7-v1.md`.

## Mineures

1. **Lignes 49-61 (chaîne en défaut)** : seuils et bandes fidèles au texte gelé. Omissions sans effet de seuil : (e) « après conversion en float32 » et « contrôlé à B0
   avant `score` » ; « trop beau » : « (`0.0` ou `-0.0`) ». Le modèle de la troisième course portait en plus les conditions d'arrêt « nombre de couches lues
   différent de 31 ; écart déclaré par la partie 2 ; empreinte différente » ; ici seules les couches contiguës et la partie 2 sont dans l'étape 2 ; l'empreinte
   d'entrée est dans l'étape 1 ; recopier la ligne « n = 31 exigé à B0 » par sûreté.
2. **Ligne 107-109 / 118-119** : « chaque série séparément » est dit (ligne 47) mais « diffère entre A100 lot 16 et A100 lot 64 » ne couvre pas le cas où
   l'une des deux séries n'a pas de verdict de B-7 (chaîne en défaut, audit non tenu). À dire : la phrase n'est pas permise dans ce cas. Le texte de
   l'addendum « les deux peuvent être vraies » est omis (sans effet).
3. **Lignes 102-109** : l'addendum fixe aussi les deux formules de sortie de l'audit (« non reproduit par le haut, confirmé à la graine 1 » / « non confirmé
   à la graine 1 »), absentes du plan ; et « n'est pas jouée » (échec, perte de machine) comme cas sans verdict de B-7 de la recourse, absent de la ligne 106
   (seule la chaîne en défaut y figure). Sans conséquence pour les fichiers actuels (les deux séries sont arrivées à leurs verdicts), mais le texte gelé de
   la lecture doit rester complet.
4. **B-7 « par le haut » et « par le bas » simultanés** (couches 8-15 ≥ 0,40 en majorité et 26-29 < 0,30 en majorité) : le texte donne « non reproduit » ; le plan ne
   dit pas si l'audit s'applique (le motif « par le haut » est vrai). À écrire.
5. **Comparaison (b)** : « avec l'écart maximal par cible » est un ajout (l'addendum demande seulement les quatre cibles et les quatre lentilles) ; inoffensif, mais à
   dire comme tel ou à retirer.
6. **Ambiguïté 7 (ligne 129-130)** : « si les empreintes du corpus diffèrent, la comparaison (b) mêle corpus et matériel » est une lecture ajoutée par le plan (non
   écrite à l'addendum). Elle est raisonnable et déclarée ; vérifier que Lazar l'accepte comme ajout de lecture, non de critère.
7. **Ligne 1 de l'étape 1** : le plan scellera sans compagnon ; prévoir le `.sha256` du plan lui-même avant ouverture, et un renvoi à son empreinte dans
   `verdict-recourse-b7-v1.md`.

## Vérifié sans réserve

- (a) Seuils recopiés : chaîne en défaut (a) à (e), B-2, B-3, B-4, B-7, verdict de reproduction, « couche lisible » (n ≥ 48, bande partielle > quart),
  « trop beau » (≥ 0,95 aux couches 0-7 ; zéro à ≥ 2 couches de 0 à 27, valeurs à 4 décimales), « tout négatif », couches 28-31 hors verdict de B-2/B-3 : conformes au texte
  gelé v6 et à l'addendum v3. Bornes incluses. Priorité « chaîne en défaut l'emporte » conforme.
- (c) Réserves de la v8 : portées fidèlement : 1 (lecture sur la graine 0, `pilotage_norme_non_nulle` = plus petit n, seul (3) teste la graine 1), 3 (lecture de la troisième
  course en vigueur avec son écart de lot) ; **réserve 2 inversée** (B1) ; **réserve 4 partielle** (M1, M2). Le critère (1)-(3) de l'addendum est recopié correctement
  dans sa partie « tient si ».
- Lecture des deux séries (addendum § 3) : verdict de B-7 de la recourse = lot 64 ; remplace la troisième course seulement comme lecture pour un moniteur ; B-2/B-3 rapportés avec R-2915
  qui reste le verdict de B-α ; désaccord A100/RTX 4090 = divergence non résolue portée à la mère : conformes.
- (e) Empreintes (`sha256sum`, 16 premiers caractères) : texte gelé `34b882437a9d1eb7` ; addendum v3 `5f05f5bc5cae8e1e` ; journal v5 `3047ff1c1f73c31b` ; contre-lecture
  v8 `a6b7a9ccf25eb249` ; verdict R-2915 sur `origin/main` `ca06acb1550ccc76` ; compagnons égaux ; manifeste : `scellement verifier` OK (`69917256f534…`), compagnon
  `69917256f53484fd…` : toutes justes. Les noms de fichiers cités (§ 2) existent tous dans `diag/20261117-…` (`b-alpha-b0/b3/fumee/partie2`, `addendum-partie2`,
  `b-alpha-measure[-lot64]`, `b-alpha-bascule-lot64`, `b-alpha-grandeurs[-lot64]`, `grandeurs-par-pole-…`, `causal_lens[_lot64]_…`, `b-alpha-verdicts[-lot64]`), ainsi que `journaux/*.log` ; aucun
  fichier `seed1` n'existe.
- (d) Le lecteur calcule avant d'ouvrir `b-alpha-verdicts*.json` (étapes 4 et 5), versement `.py` et `.json` scellés : bon ; réserves M5 sur le journal et la troisième course.
