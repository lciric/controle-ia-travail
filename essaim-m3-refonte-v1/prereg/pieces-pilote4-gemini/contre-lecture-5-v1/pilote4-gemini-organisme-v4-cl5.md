# Contre-lecture 5 du préenregistrement du quatrième pilote descriptif (`pilote4-gemini-organisme-v4.md`) — v1

- **Texte relu** : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md`,
  `efb13feb34f66d9652a194564c0bc9eced2889cbb6305c8dac9e97766246b60e` (empreinte vérifiée sur disque avant lecture ;
  323 lignes ; texte différentiel). Texte de référence : P4v3, `pilote4-gemini-organisme-v3.md`,
  `de7a555932d8e8825a68bd1bd54baff55d08166f84f94d5deb9217312e78c656` (vérifiée ; 688 lignes, lue en entier).
- **Contre-lecteur** : sous-agent neuf (`claude-opus-5-5`), lancé par conv-audit, le 26 octobre 2026. Début lu sur
  `date -u` : 00:29:43 UTC ; ce rapport est écrit à partir de 00:55:36 UTC (heure lue sur `date -u` juste avant). Je n'ai
  écrit ni ce texte, ni ses versions précédentes, ni le noyau, ni les lanceurs, ni les batteries, ni les corrections de
  l'organisme (C-14 à C-17), ni les vérifications, ni les contre-lectures 1 à 4.
- **Lu** : le texte relu et P4v3 en entier ; les contre-lectures 3 et 4 en entier ; dans `objet-v6-2-1-v1/` : les deux
  vérifications (`LISEZMOI-v1.md` de la v6.2 aux § Verdict à 7 début, de la v6.2.1 en entier), `CORRECTIONS-v5` (copie),
  l'écart de l'organisme en entier, les journaux des essais des corrections (a, b, c, d, détail : en-têtes, échecs,
  bilans) et des deux témoins, `comparaison-lignes-v61-v621-v1/` en entier, les mots de Lazar v1 et v2 en entier, le
  brief de la vérification de la v6.2.1, le début du rapport de livraison de Gemini ; les dérivations des lanceurs v7 à
  v10, des batteries v9 à v12, du script de scellement v4 ; les quatre écarts de lanceurs ; le lanceur v10 en entier ;
  les batteries v10 → v11 et v11 → v12 par leurs écarts (recalculés), la v12 par `grep` ; `sceller_pilote4_v4.py` en entier,
  ses essais (journal et témoin) ; `verifier_scellement_pilote4_v2.py` en entier ; le journal de la série v13 en entier,
  ses heures, celles de la série v9 et la liste de ses cas ; le relevé v13 (script v3 et sortie) et le script v1 ; dans
  les extractions de l'organisme (lecture seule) : `principal.py` de la v6.2.1 aux l. 85–100, 785–797, 975–1120,
  1550–1570, 1630–1690 (par `grep`), 1895–1940, 1982–1986, 2025–2130, `memoire_isvd.py` l. 78–90,
  `politique_endogene.py` l. 1–45 et 220–230, `tests/test_corrections_v5.py` l. 70–135 ; l'écart v6.1 → v6.2.1 recalculé
  (`principal.py`, `memoire_isvd.py`) ; `boucle.py` l. 98–106 ; dans la série v13 (simulations) : `LANCEMENT.md` de
  `cas-sain-v6-2` en entier, la ligne de la course précédente dans celui de `cas-sain-v5-3`, la ligne de la passerelle de
  `cas-passerelle-saine`, et, par mon relevé, les journaux d'appels et les extraits des quatre cas sains (champs
  mécaniques : statut, rôle, événements d'arrêt et de reprise).
- **Non lu ni ouvert** (consignes) : aucun fichier `…-cle.json` ni `…-secret.json` (ni lu ni haché ; la liste
  d'empreintes v6 n'en porte aucun, vérifié avant `sha256sum -c`), aucun dossier `donnees/`, `runs/`, `diag/`, aucun
  `P3-consignes-v1.md` ni `textes-actions-…`, aucune archive `ferme.tar.gz` (des simulations comprises : noms seulement vus
  par `ls`), aucun fichier `reponse-question*`, `journal-appels*` ou `extrait-mecanique*` des pilotes réels. Non lus :
  `cles-avant-poussee-v621-v1.txt` (haché seulement), les archives des copies d'essai du scellement, les livrables zippés
  des vérifications (hachés seulement), les messages du canal et des sessions (n° 52, 53, 67 ; R-446, R-449, R-453),
  `RAPPORT-M-hypotheses-gpu-v1.md`, la soumission de 23:56 UTC (options (1) à (3)) et la question au collisionneur.
  Non vérifiable sans `git` : la parenté des commits, la présence de `7ea3270` sur `canal/conv-audit-organisme-v6-2-1`
  du dépôt distant, la tête `d0d0175`.
- **Exécuté** (sorties sous `/var/tmp/contre-lecture-pilote4-v5/` seulement) : `date -u` ; `sha256sum` sur les pièces
  citées ; `sha256sum -c EMPREINTES-pieces-pilote4-v6.txt` depuis `pieces-pilote4-gemini/` après lecture de sa liste
  (**502 sur 502 justes** ; `sha256sum-c-EMPREINTES-pieces-pilote4-v6.txt`) et de son compagnon ; `sha256sum -c` des
  compagnons de `objet-v6-2-1-v1/`, `releves-serie-v13-v1/`, des mots de Lazar et des contre-lectures du pilote 4 ;
  `diff` (organisme 3bbb78c → 7ea3270 et v6.1 → v6.2.1, lanceurs, batteries, mots v1 → v2) ; les scripts de dérivation
  `deriver_lanceur_pilote4_v7.py` à `_v10.py`, `deriver_essais_pilote4_v9.py` à `_v12.py` et
  `deriver_scellement_pilote4_v4.py`, chacun sur sa source, sorties dans `rederive/` ; mon propre code, lecture seule,
  par `/opt/venv-essaim-sim-v1/bin/python -I` (`outils/`) : empreintes d'arbre (transcription de `boucle.empreinte_arbre`),
  relevé indépendant de la série v13, comparaison des passages cités v6.1 → v6.2.1, contrôle des gardes du scellement et
  de la lecture du texte par le lanceur sur une copie remplie en mémoire (valeurs d'essai, jamais celles du pilote) ; la
  chaîne de `grep` du lanceur v10 (étape 4) sur mes copies de la ligne de GO et des lignes de dépense
  (`essai-lignes/`, empreinte du texte et des courses factices). **Rien** du lanceur, des batteries, du script de
  scellement, du script de vérification, du script de relevé ni du code d'un organisme n'a été exécuté. Aucun `git`,
  aucun sous-agent, aucune recherche récursive (des `ls` de dossiers nommés seulement).

## Verdict

**Scellable après corrections mineures.** L'objet est celui que dit le § Objet : arbres recalculés (`4f13647a…`,
26 fichiers ; `3b2d8d5a…` et `ae331d1d…`, 24) ; l'écart publié 3bbb78c → 7ea3270 est l'écart recalculé (16 blocs) et ne
contient que C-14 à C-17, la version et leur documentation ; chaque ligne citée du § Objet est juste (sondage large,
ci-dessous) ; les douze passages que P4v3 cite pour la v6.1 sont identiques dans la v6.2.1, aux numéros donnés. Les
lanceurs v7 à v10, les batteries v9 à v12 et le script de scellement v4 (et ses essais) se redérivent octet pour octet ;
les quatre écarts de lanceurs publiés sont les écarts recalculés ; l'inversion de l'ordre (lanceur v9, batterie v11) est
juste et complète dans le code. La série v13 est complète et conforme (229 sur 229 ; les 228 cas de la série v9, renommés
ou échangés, plus `sain-v5-3-graine`), et le relevé se reproduit octet pour octet par mon propre code. La ligne de GO et
les lignes de dépense passent les `grep` du lanceur v10 ; « rien ne part » sans l'arbre de la v6.2.1 est vrai du code ;
le script de scellement v4 acceptera le texte. Les mots de Lazar sont rendus fidèlement.

Deux constats mineurs, de texte seulement : les options (2) et (2') de la décision ouverte, que la « règle de ce texte »
rend applicables « sans autre texte », ne disent ni comment l'agent neuf lit, ni ce que devient la condition (ii) de P4v3
(« avant toute lecture de ses scores ») pour tout autre usage (P4C5-01) ; deux phrases de P4v3 qui dépendent de l'ordre des
courses ne sont pas transposées et se lisent fausses par la substitution « v6.1 → v6.2 » (P4C5-02). Cinq remarques
suivent. Au remplissage de `[[CONTRE_LECTURE_DETAIL]]` : citer `efb13feb…` comme texte relu par cette contre-lecture ;
n'y écrire aucune ligne qui porte « entropie E = » ou « graine de la course … = » (le script refuserait) ; le compagnon de
ce rapport est au format « empreinte, deux espaces, nom », que le script lit.

## Constats

### P4C5-01 — mineur — Options (2) et (2') : applicables « sans autre texte », mais sans procédure de lecture, et la condition (ii) de P4v3 devient insatisfiable à la lettre

- **Fait, texte relu.** L. 75–81 : (2) « ouvrir les scores de ce pilote, dès la fin de sa dernière course, à un agent neuf,
  pour ce seul usage : il écrit les hypothèses de (b) (signe et taille par famille), scellées dans le texte de (b) ; les
  auteurs de l'étape 1 et de la confrontation ne lisent pas ces scores, et la réserve est écrite dans leurs textes » ;
  (2') l'agent rédige toute la section. L. 83–87 : un mot de Lazar inscrit avant la fin de la dernière course « rend cette
  option applicable sans autre texte » ; « pour tout autre usage, les scores de ce pilote restent fermés selon P4v3 ».
- **Fait, P4v3.** § Plan, point 3, condition (ii) (l. 382–386) : la version de la confrontation qui sert la banque
  décisive est écrite « après la fin de la dernière course de ce pilote […] et **avant toute lecture de ses scores** » ;
  point 4 (l. 417–421) : la lecture passe par un script écrit, empreinté et essayé avant le moment de lecture ; l. 240 :
  le `test_final` est lu à part.
- **Portée.** Sous (2) ou (2'), l'agent lit dès la fin de la dernière course : aucune version de la confrontation ne peut
  plus être écrite « avant toute lecture » ; lue à la lettre, la règle de P4v3 ferme alors les scores de ce pilote pour
  tout autre usage, sans terme. Lue comme « avant toute lecture par les auteurs de cette version », elle tient, mais le
  texte ne le dit pas. De plus, la section des hypothèses de (b) (signe et taille par famille) porte de l'information sur
  ces scores : si les auteurs de l'étape 1 ou de la confrontation la lisent (la lignée conv-audit écrit (b) sous (2)), la
  « réserve » doit le dire, et la déclaration de T2 que (ii) recopie (« aucun score des pilotes ne motive aucun
  changement ») en dépend. Enfin, ce que l'agent lit (quels fichiers, `test` et `test_final`, par quel script), ce qu'il
  transmet (la seule section des hypothèses ?) et où ses pièces restent ne sont pas fixés. Le texte tient dans l'issue (1)
  (règle de P4v3, par défaut) et dans l'issue (3) ; dans les issues (2) et (2'), il ne se suffit pas.
- **Correction** (texte seul ; l'une ou l'autre) : (a) **simple** : « Un mot de Lazar qui choisit (2) ou (2') demande un
  texte court, scellé et contre-lu avant toute lecture, qui fixe la lecture de l'agent » ; ou (b) écrire ici la
  procédure : « l'agent neuf lit les tableaux de ce pilote par le script de P4v3 (§ Plan, point 4), essayé avant ; il ne
  transmet que la section des hypothèses de (b) (signe et taille par famille), scellée ; ses autres pièces restent fermées ;
  pour la condition (ii) de P4v3, « avant toute lecture de ses scores » s'entend des auteurs de cette version de la
  confrontation, qui n'ont lu ni ces scores ni cette section avant de l'écrire (sinon ils l'écrivent en réserve, avec
  l'empreinte de la section) ».

### P4C5-02 — mineur — Deux énoncés de P4v3 qui dépendent de l'ordre ne sont pas transposés et se lisent faux

- **Fait.** La table (l. 108) remplace « v6.1 » par « v6.2 » « dans les règles, la liste d'arrêt, les bornes, le devis et
  les essais » ; la l. 121 transpose les issues de la v5.3 qui arrêtent la seconde course, dans la liste d'arrêt
  seulement. Restent :
  (a) P4v3 § Bornes, devis, l. 336–338 : « la course s'arrête au plafond total ; pour la v5.3, la v6.1 ne part pas (porte
  « v5.3 précédente » ; essai `v53-plafond-total`) » — par la table : « pour la v5.3, la v6.2 ne part pas (porte « v5.3
  précédente ») », faux dans l'ordre nouveau (le juste : pour la v6.2, la v5.3 ne part pas ; porte « v6.2 précédente » ;
  essai `v62-plafond-total`, présent dans la série v13) ;
  (b) P4v3, liste d'arrêt, l. 454 : « ronde de la v5.3 hors `OK` | rapportée ; n'arrête pas la v6.1 (la porte ne lit que
  les générations notées) » — par la table : « ronde de la v5.3 hors `OK` ; n'arrête pas la v6.2 », sans objet ; le cas
  utile, une ronde de la **v6.2** hors `OK`, n'est écrit nulle part (le code ne lit que les générations notées : lanceur v10
  l. 325, filtre `not g.get("phase")` ; c'est aussi ce que la table de P4v3 avec P3 disait de la porte).
- **Portée.** « En cas de conflit, ce texte prévaut » et la l. 121 (« une issue de la v5.3 […] n'arrête plus rien d'autre
  qu'elle-même ») rattrapent (a) ; (b) se déduit du code et de la description de la porte. Mais la liste d'arrêt est ce
  que session-depot lit pour décider ; elle doit le dire.
- **Correction.** Une ligne de la table : « devis, P4v3 l. 336–338 : pour la v6.2, la v5.3 ne part pas (porte « v6.2
  précédente » ; essai `v62-plafond-total`) » ; une ligne de la liste d'arrêt : « ronde de la v6.2 hors `OK` | rapportée ;
  n'arrête pas la v5.3 (la porte ne lit que les générations notées) | lanceur v10 ; extrait ».

### P4C5-03 — remarque — Le canal (d) de la première course est désormais écrit au `LANCEMENT.md` de la seconde, avant l'échéance de la règle des options (2) et (2')

- **Fait.** La porte « v6.2 précédente » écrit au `LANCEMENT.md` de la v5.3 le nombre d'appels par statut de chaque
  génération de la v6.2 (lanceur v10 l. 342, 358, 362 ; série v13 : « g000 {"OK": 123}; g001 {"OK": 129}; g002 {"OK": 123};
  g003 {"OK": 124} »). Un 124 en g002 ou g003 est l'appel de mutation, c'est-à-dire le bit de stagnation du canal (d)
  (texte l. 225–226 ; P4v3 l. 402–407). Dans P4v3, la porte décrivait la v5.3, qui ne mute pas : ce bit n'était lisible
  qu'après la seconde course. Désormais il l'est pendant la v5.3, avant la fin de la dernière course, qui est l'échéance
  du mot de Lazar sur (2) ou (2') (l. 84).
- **Portée.** Canal dit et accepté ; « personne ne met ces faits en rapport avec quoi que ce soit avant ce moment » tient.
  Mais un choix de règle de lecture fait après ces lignes n'est plus tout à fait aveugle (R1).
- **Correction.** Au canal (d) (l. 225–226) : « il paraît aussi, pour la v6.2.1, dans la ligne « course v6.2 précédente »
  du `LANCEMENT.md` de la v5.3 (appels par génération) » ; et, à la règle : échéance au départ de la v6.2.1, ou « Lazar
  choisit sans consulter ces lignes », à son choix.

### P4C5-04 — remarque — Décision de 23:56 UTC et mot R-445 : trois précisions

- (a) **Défaut de la décision soumise à 23:56 UTC.** Le texte donne le défaut de l'autre décision ouverte (l. 88–90) mais
  pas celui-ci ; la routine de reprise applique à 48 heures le défaut des décisions « proposer avec recommandation »
  (ici recommandé : (2)). La règle (l. 83–86) n'admet qu'« un mot de Lazar » : l'écrire (« un défaut échu ne vaut pas ce
  mot ; tant qu'aucun mot n'est inscrit, (1) »), avec le défaut annoncé à la soumission (pièce non fournie, non vérifié).
- (b) **Forme de la ligne de GO.** R-445 dit d'inscrire les lignes « exactement sous la forme qu'il [le message de départ]
  donne » (texte l. 53) ; le texte dit « de la forme exacte » du § Plan, point 1 (l. 48–49, 234). Ajouter : « le message de départ
  recopie mot pour mot les lignes du § Plan, point 1, l'empreinte du texte scellé remplie ; s'il en diffère, rien ne
  part ».
- (c) **« Aucun point ouvert n'est à accepter »** (l. 112) : juste pour les défauts ; mais deux choix restent « à Lazar »
  (C-14, arbitrage selon la confiance ; C-16, autre détection) et quatre constats non bloquants sont déclarés. Dire qu'ils
  ne changent rien à ce qui tourne ici (le texte le montre l. 180–183) et que R-448 porte l'objet tel quel.

### P4C5-05 — remarque — § Essais : une inexactitude et trois précisions

- (a) L. 281, « Série v13, en simulation (faux appels, aucune clé, **aucun réseau**) » : inexact. Le cas
  `passerelle-saine` interroge sans clé les interfaces d'Anthropic et de Gemini (statuts 401 et 403, `LANCEMENT.md` de
  `cas-passerelle-saine`), et les essais du noyau du cas sain comprennent « la recherche réelle sur arXiv » (lanceur v10
  l. 676 ; `LANCEMENT.md` de `cas-sain-v6-2`). Écrire « faux appels aux espèces, aucune clé ; réseau pour la passerelle,
  sans clé, et pour l'essai de moisson réelle du noyau ».
- (b) Les numéros de lignes du lanceur que P4v3 cite (§ Essais l. 496–504 ; lanceur v6) se lisent
  dans le v10 décalés de +12 avant l'étape (0 bis) et de +13 après (par exemple v6 l. 206, 256, 504, 512, 804, 821 → v10
  l. 218, 268, 517, 525, 817, 834) : le dire en une phrase, la ligne « lanceur v6 → lanceur v10 » de la table ne suffit pas.
- (c) Liste d'arrêt, l. 270, colonne des gardes : « lanceur v10, étape (0 bis) » ; la graine de la précédente est
  contrôlée à l'étape (2) (l. 508–511) et la ligne de dépense à l'étape (4) (l. 551–553). Écrire « étapes (0 bis), (2) et
  (4) ».
- (d) Aucune seconde course en segments n'est essayée (la porte est revérifiée à chaque segment K ≥ 2 de la v5.3, avec
  la ligne de dépense de la v5.3 et ses deux empreintes) ; même lacune que P4v3 pour la v6.1. Le dire, ou l'ajouter au
  prochain lanceur.

### P4C5-06 — remarque — Traçabilité des pièces (R6, R12)

- (a) Les pièces des cas sains de la série v13 (`LANCEMENT.md`, extraits et journaux d'appels de simulation) ne sont pas
  versées : le relevé et les nombres du § Essais (l. 289–298) reposent sur des fichiers du dossier de travail de la
  session (`…/scratchpad/pilote4/serie-v13/essais/`), qui disparaîtra. P4v3 versait `simulation-lanceur-v6/`. Verser un
  `simulation-lanceur-v10/` (quatre cas, jamais `ferme.tar.gz`) au fichier d'empreintes v2.
- (b) Le relevé v3 dit qu'une v2 « n'a jamais servi » ; elle n'est pas aux pièces : la verser ou dire qu'elle n'a pas été
  gardée.
- (c) Essais des corrections (l. 184–188) : les versions de code des essais `v621-a` et `v621-b` ne sont pas gardées ; la
  cause de `v621-a` est dite (« premières versions de C-14 et C-15 » ; le journal le confirme : trois essais de
  l'architecte en « `cle_json_manquante_ou_invalide:alpha` », `test_c06`, `test_c15_cas_sain`, et l'essai hérité pas encore
  adapté) ; celle de `v621-b` ne l'est pas (l'essai de C-14 attendait que toutes les castes répondent, alors que
  l'arrêt anticipé de la v6.2 en garde deux : journal l. 28–35 ; l'essai final dit `2 <= len(…) <= n`). L'ajouter.

### P4C5-07 — remarque — Petits faits

- (a) C-14 (l. 161) : « toutes les castes délibèrent » ; plus juste : « dès deux castes, la délibération s'ouvre, avec
  l'arrêt anticipé de la v6.2 » (`CORRECTIONS-v5`, C-14 ; essai l. 114–117).
- (b) C-17 (l. 173–174) range sous C-17 le refus d'une clé JSON absente ou non finie (l. 1039–1042) : c'est le point 8 de
  la v6.2, gardé tel quel ; le dire « (v6.2, point 8) ».
- (c) `sceller_pilote4_v4.py`, en-tête l. 17–18 : « la graine de la course **v5-3** (première course) » ; la v5.3 est
  désormais la seconde. Sans effet sur le code (l'enfant 0 reste celui de la v5.3) ; au prochain script.
- (d) Copie de lancement (table l. 113) : la tête du scellement doit ne différer de `8e5e2f7b` que par des chemins permis
  (lanceur v10 l. 183, `PERMIS_APRES_CODE`) ; le travail parallèle sur les étapes 1 et 2 (décisions de 00:48 et 00:49) ne
  doit pas être commité sur `outils/pilote4-gemini-travail` avant le départ, sinon l'étape (1) refuse (sans dommage :
  avant le manifeste). Une phrase au § Plan, point 1.

### P4C5-08 — conforme — Ce que j'ai trouvé conforme

- **Empreintes** (recalculées sur disque) : texte `efb13feb…` ; P4v3 `de7a5559…` ; contre-lectures 3 `0d95ea8c…` et 4
  `e2de1372…` (compagnons justes, comme ceux des contre-lectures 1 et 2) ; lanceurs v6 `50f9c496…`, v7 `cda96923…`, v8
  `40685089…`, v9 `6491c940…`, v10 `0203f546…` ; batteries v8 `a5f4b944…`, v9 `edb6b12b…`, v10 `b7906684…`, v11
  `ba47a625…`, v12 `27ef4524…` ; journal v13 `ed50ba14…`, heures `e2adbc2f…` (23:53:00–00:03:40) ; `sceller_pilote4_v4.py`
  `6094f21a…`, essais `bc79b4bc…` ; `EMPREINTES-pilote4-gemini-v1.txt` `5ed51779…` ; relevé `1e9df693…`, sortie
  `e99c1a48…` ; livraison `e9471860…` ; vérifications `e4ce11c9…` et `756f7445…`, `EMPREINTES-v1.txt` `cc83b792…`
  (129 entrées), livrable `f48c6557…` ; `CORRECTIONS-v5` (copie) `c502a2d8…` ; écart `5bfee6b8…` ; tous les compagnons
  justes. `EMPREINTES-pieces-pilote4-v6.txt` (`d010123d…`, compagnon juste) : 502 lignes sur 502 justes ; il couvre tous
  les fichiers du premier niveau et des dossiers nouveaux (`objet-v6-2-1-v1/` et ses quatre sous-dossiers,
  `releves-serie-v13-v1/`), sauf lui-même et son compagnon.
- **Objet.** Empreintes d'arbre recalculées par ma transcription de `boucle.empreinte_arbre` : v6.2.1 `4f13647a…`
  (26 fichiers), v6.2 `3b2d8d5a…` (24), v6.1 `ae331d1d…` (24). Écart 3bbb78c → 7ea3270 recalculé : mêmes 16 blocs que
  l'écart publié ; six fichiers (`principal.py`, `CONCEPTION.md` § 2.14 seul, `manifeste.json`, l'essai hérité, deux
  ajoutés). Lignes de la v6.2.1 vérifiées : C-14 l. 1731–1738 ; C-15 l. 611–619 et 1986 (sans traits, l'argument vaut `{}`
  comme en v6.2 : défaut l. 1864, garde l. 1678, aucun effet ici) ; C-16 l. 81–82 de `memoire_isvd.py`, l. 967–975 et
  1082–1083 (gabarit écrit en chaîne formatée, l. 1048, d'où le même texte), copie l. 38–39 et 9–10 de
  `politique_endogene.py` ; C-17 l. 1030–1035, 1039–1046, 1102 (seul appel), 1558–1562, consigne l. 1007 et 1010–1011 ;
  `exec`/`compile` seulement l. 226–227 de `politique_endogene.py` ; fin de conception l. 2101–2106 ; mutation et
  stagnation l. 991–998 (filtre l. 993, test l. 994, disjonction l. 997) ; `finally` l. 2043 ; mémoire l. 2066, pondération
  l. 2077 ; format l. 794 ; réserve l. 89–98 ; sans traits, sondes non appelées (l. 1901) ; 4 vérifications en conception
  (l. 1932). Les douze passages de `comparaison-lignes-v61-v621-v1/` revérifiés par mon code : identiques ;
  `mitose_spectrale.py` identique à la v6.1, `memoire_isvd.py` ne diffère de la v6.1 que par les deux constantes.
  Les corrections font ce qu'elles disent et rien d'autre ; l'essai hérité adapté se limite à C-15 et n'est pas affaibli
  (l'union entraînement + validation = {tr_1…tr_4} exclut aussi `viv_1` du pli ; une assertion de plus) ; C-14 et C-16
  gardés avec leurs raisons (`CORRECTIONS-v5`, `CONCEPTION.md` § 2.14). Faits du § Objet tirés des deux vérifications :
  justes (53 sur 53 deux fois ; points levés 1, 2, 6, 8, 11, 12, 13 et partiels 3, 4, 5, 7, 9, 10 ; V62-01 ; 68 sur 68,
  5,21 et 5,29 s ; témoins 7/8 et 1/4 ; quatre constats non bloquants, le cinquième — JSON et code mêlés refusés — dit en
  C-17). Journaux des essais des corrections : a 6 échecs sur 66, b 1 sur 68, c et d 68 sur 68, témoins 7 échecs et
  8 réussites, 1 échec et 4 réussites.
- **Dérivations.** Lanceurs v7 (8 remplacements), v8 (5), v9 (trois blocs échangés, comptes attendus, puis l'en-tête) et
  v10 : identiques octet pour octet ; écarts publiés v6→v7 (90 lignes), v7→v8 (26), v8→v9 (129), v9→v10 (24) = écarts
  recalculés. Batteries v9 à v12 et `sceller_pilote4_v4.py` avec `essais_scellement_pilote4_v4.sh` : identiques. L'inversion
  est juste et complète dans le code : porte (étape 0 bis, l. 285–363 : course `v6-2`, nom, lignée, même lanceur, dernier
  code 0, pas de `CLORE=1`, archive fermée, générations [0, 1, 2, 3] hors rondes, fin « générations maximales », arrêts
  `STOP` repris numérotés puis « aucune lignée active ») ; graine de la précédente (l. 508–511) ; ligne de dépense de la
  v5.3 avec l'empreinte des empreintes de la v6.2 (l. 551–553) ; enfant 0 pour la v5.3, enfant 1 pour la v6.2 quel que soit
  l'ordre (l. 74–84, 506) ; aucun reste de l'ordre ancien (recherche dans le v10). Batterie v11 : cas sains dans le nouvel
  ordre, porte sur artefacts et en segments échangée, mode réel de la porte M sur la v6.2, segments sur la v6.2.
- **Série v13.** 229 cas `OK`, aucun échec ; correspondance cas par cas avec la série v9 : 190 renommés (`v6-1` → `v6-2`),
  38 échangés, aucun perdu, un nouveau (`sain-v5-3-graine`). Chacun des cas cités par le texte y est une fois ; 21 cas
  `v62-…`, 4 `seg-v62-…`, `v62-plafond-total` et `v62-fin-lignee` compris. Le cas sain v6.2 a tourné sous le lanceur v10
  (`0203f546…`), organisme `4f13647a…` (26 fichiers). Relevé : ma sortie est identique octet pour octet ; les nombres du
  § Essais sont les siens (c001 7 dont 1 mutation, 123, 129, 123, 124 dont 1 ; v5.3 6, 123, 129, 123, 123 ; reprises
  7 appels et 0,0947 USD, puis 130 appels et 1,9544 USD).
- **Plan.** Ligne de GO du texte, empreinte factice remplie : acceptée par la chaîne de l'étape (4) pour `v6-2` et pour
  `v5-3` (`8b1c7511`, `4f13647a` ou `6251ab21`, 16 caractères du texte) ; sans la clause de la v6.2.1, refusée pour `v6-2`,
  et la v5.3 refusée en réel faute de précédente (l. 292–293) : « rien ne part » est vrai. Lignes de dépense (dates et
  empreinte factices) : acceptées pour les deux courses et pour un segment 2. Le texte porte une seule ligne
  « entropie E = », les deux lignes de graine des marqueurs, les quatre marqueurs une fois chacun, l'empreinte pleine du
  lanceur ; chevrons simples sans effet ; mes gardes recopiées du script v4 passent, et la copie remplie se lit comme le
  lanceur l'attend (l. 501–511). Le script de vérification v2 attend `v6-2` et `EMPREINTES-pilote4-gemini-v2.txt` ; le
  script v4 n'écrase pas le fichier v1 (essai `sain-avec-empreintes-v1`, 16 sur 16 ; témoin v3, 12 sur 16).
- **Décisions.** Le relevé v2 reprend la v1 mot pour mot ; les citations du texte en sont fidèles (fautes corrigées,
  coupures marquées) ; heures de Paris = UTC + 1 (fin de l'heure d'été le 25 octobre 2026), cohérentes entre elles
  (00:15 → R-445 entre 23:18 et 23:25 UTC ; 00:27 → R-448 avant 23:41 UTC) ; bornes de R-445 = celles de la ligne de GO.
  La règle de ce texte tient avec P4v3 dans l'issue (1) et l'issue (3), et avec R1 (choix borné, inscrit avant la fin des
  courses, sans lecture de score), aux réserves de P4C5-01 et P4C5-03 près.
