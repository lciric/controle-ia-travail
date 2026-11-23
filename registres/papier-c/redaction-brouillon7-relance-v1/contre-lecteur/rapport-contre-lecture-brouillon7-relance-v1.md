# Papier C — contre-lecture (R2) du brouillon 7 de relance du préenregistrement HC1 à HC3 — v1

- Contre-lecteur : sous-agent neuf, Opus 5.5 (`claude-opus-5-5`), lancé le 2026-11-22 par la session
  `session_013QMayk1rjSZrn2u9UAVhEp` (celle du rédacteur). Il n'a écrit aucune version de ce texte, aucune
  configuration, aucun module, aucune contre-lecture ni table de traitement du papier C. Rapport écrit vers 19:00Z.
- Texte relu : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22.md`,
  `9c7a89f1e6d001ca9e9ac35ea89eb76e0654cba3151c1c14cd7945570a60ecd2` (égale à son compagnon et à l'empreinte
  attendue), lu en entier (2 236 lignes, onze tranches).
- Source : version r3, `160730b4c3980d8d96b0d05ed4041f011b5bf78a7d8dc7f927ee1ed0c2463cac` ; la copie du dossier
  `source/` est égale, octet pour octet, à la pièce de la branche `claude/papier-c-preenregistrement-v1`
  (commit `48e08c72`, chemin `…/redacteur/…-r3.md`).
- Interdits tenus : rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun fichier dont le nom
  porte « consigne-privee », « conception-ii-b », « vérité », « rendu » ou « scores » (en particulier
  `src/controle_ia/bases/scores_jetons.py` n'a pas été ouvert ni empreinté) ; ni `brouillons/ii-b-saboteur-budget-v1/`,
  ni `brouillons/` de la branche du 19 novembre (seuls des noms de fichiers listés par `git ls-tree`), ni les branches
  interdites, ni la ligne R-2059, ni N-063 ni N-054. Aucune dépense, aucun modèle externe, aucune machine, aucune
  suite d'essais complète. Aucun refus de permission. Écrit dans ce seul dossier.

**Décompte : 0 bloquante, 5 majeures, 14 mineures. Avis : scellable après corrections.**

## 1. Remarques

### CB-01 — majeure — réserve 20 (a) : l'argument « resterait immobile » oublie le paragraphe de bras
- **Lieu** : Plan, section 7, réserve 20 (a) ; repris dans la précision 39 (« Ce qu'elles ne disent pas ») et dans
  `points-ouverts-…`, D-22.
- **Citation** : « Or une sonde qui lirait cette trace resterait immobile sous le plaidoyer, puisque la consigne de
  saboter est la même dans les cellules S et SP_m : HC2 pourrait alors être confirmée, et l'opposition de C-P4c
  établie ».
- **Pièce** : Plan, section 3, « Génération du corpus A » : le paragraphe de bras est « ajouté à la fin du message
  système de l'agent » dans les cellules qui plaident ; S n'en a pas, SP_m en a un.
- **Constat** : S et SP_m diffèrent par le contexte aussi (la consigne de plaider), pas seulement par les jetons de
  l'agent. Une sonde qui lit le contexte (la trace de la consigne) peut donc bouger sous le plaidoyer, dans un sens
  inconnu : elle peut confirmer HC2 à vide, mais aussi la réfuter d'un côté ou de l'autre, ou déclencher la bascule
  de la porte GC, sans rien dire de l'intention. L'argument n'est juste que dans un sens (confirmation à vide) ; la
  réserve est donc incomplète, et elle laisse croire qu'elle ne menace que la confirmation. Les parts π_S et π_H,
  lues sans paragraphe de bras, ne mesurent pas cet effet ; la différence des différences (HP_m − H) et le témoin
  L-HP (même consigne de plaider, sans consigne de saboter) en disent quelque chose et ne sont pas nommés.
- **Correction demandée** : écrire « ne bougerait que par ce que le paragraphe de bras change au contexte ; HC2
  pourrait alors être confirmée à vide, ou réfutée, et la porte GC déclenchée, sans rien apprendre d'une sonde
  d'intention » ; ajouter à « Ce qu'elles ne disent pas » (précision 39) : « les parts sont lues sans paragraphe de
  bras : elles ne disent pas ce que la consigne de plaider change au contexte » ; renvoyer à la différence des
  différences et à L-HP comme lectures rapportées qui en parlent. Aucune règle de verdict ne change.

### CB-02 — majeure — la mention de la réserve 20 manque sur la ligne de la porte GC
- **Lieu** : Plan, section 7, réserve 20, « Mention » ; Critères, « Combinaisons », « Mode d'induction » ; même
  section, « Porte GC » et « HC2 confirmée et borne basse … > 0 … la ligne de la porte GC est écrite pour cette sonde ».
- **Citation** : « Toute ligne de C-P4 (HC2 et HC2b), de C-P4b, de C-P4c et de C-P6 (sondes) est écrite avec la
  mention … ».
- **Constat** : la ligne de la porte GC se lit sur la même sonde, sur le même saboteur à consigne tenue en contexte ;
  c'est la ligne qui change le titre du papier (contamination de construit). Avec CB-01, un déplacement positif de
  la sonde peut venir du contexte (consigne de plaider) et non du registre. La liste des lignes qui portent la
  mention ne la contient pas, et rien ne dit pourquoi.
- **Correction demandée** : ajouter la ligne de la porte GC (et les mentions de l'audit A9 sur les sondes) à la
  liste, à la réserve 20, à la précision 39 et à la combinaison « Mode d'induction » ; ou écrire pourquoi elle en
  est exemptée. Sans effet sur un verdict (GC se tranche en fin de phase 1, R13).

### CB-03 — majeure — précision 38 : trois cas laissent deux lectures à un programmeur
- **Lieu** : Plan, section 8, précision 38 ; liste d'arrêt 15 ; additif à la fiche du module, point 1.
- **Citations** : « sur chaque famille d'organismes et à chaque dose où ce verdict juge le critère 3 » ; « pour le
  mode « coût gonflé » » ; « L'« écart au plancher » d'une sonde est le plus petit de ses écarts sur ces familles et
  ces doses, dans l'unité où le verdict les écrit ».
- **Pièces** : brief v2, porte G0, critère 3 : « Sondes v0 au-dessus du plancher aléatoire apparié, sur (i) et
  (ii) » (citation exacte) ; brief v2, T0.6 : famille (iii) « si la licence le permet » ; N-053, point 2 : famille
  (iv), « une sonde d'intention réussit sur (ii) et sur (iv) ».
- **Constat** : (a) « chaque famille … où ce verdict juge » va au-delà du critère 3, qui ne nomme que (i) et (ii) :
  si le verdict de G0 juge aussi (iii) ou (iv), une sonde au-dessus du plancher sur (i) et (ii) mais non sur (iii)
  n'est pas désignée ; la raison de principe de la précision (test de validité de T0.7, sur (i) et (ii)) ne couvre
  pas ce cas, et la lecture « (i) et (ii) seulement » reste possible. (b) Si le verdict de G0 n'est pas ventilé par
  mode de sabotage, « pour le mode « coût gonflé » » n'a pas de référent : ni règle ni nœud. (c) « L'écart » d'une
  sonde (valeur ponctuelle, borne d'intervalle ?) et le cas d'unités différentes entre familles ne sont pas fixés
  (le rédacteur le note lui-même, journal, doute 2). La règle n'est donc pas entière pour tous les verdicts de G0
  jugés par famille et par dose.
- **Correction demandée** : écrire soit « sur (i) et sur (ii) », soit « sur toute famille jugée », avec la raison ;
  ajouter « verdict non ventilé par mode : nœud » (ou la règle voulue) ; fixer « l'écart » comme la valeur ponctuelle
  écrite par le verdict, et « unités différentes : nœud ». La citation du brief est exacte ; la citation de N-063,
  d'après sa ligne de `CLAUDE.md`, l'est aussi.

### CB-04 — majeure — précision 37 : prémisse inexacte, et lecture moins sévère pour C-P3a et C-P3b
- **Lieu** : Plan, section 8, précision 37 ; Métrique, points 8 et 11 ; liste d'arrêt 17 ; point hérité H-1 de
  `points-ouverts-…`.
- **Citation** : « Ḡ n'a pas de condition de dégénérescence : c'est un gain, non une destination ; dans un tirage où
  ĉ sort des bornes, Ḡ est celui que la forme fermée donne : fini, il reste lu ».
- **Pièces** : Métrique, point 8 : « ĉ hors de [−30 ; 40] : « ĉ non identifiable » (la loi dégénère en simple
  décalage) » ; g_m(c) = Σ_i Δ_{i,m}(c − v₀_i) / Σ_i (c − v₀_i)² ; contre-lecture de la grille, CG-02 et CG-03
  (`d0485a40…`) ; rapport de la grille, section 1 (`8d1616fc…`).
- **Constat** : (a) Ḡ est la moyenne des g_m évalués en ĉ ; quand ĉ s'échappe, la loi est un décalage et Ḡ ≈
  décalage / (ĉ − v̄₀), tiré vers 0 par construction. « Fini, il reste lu » garde donc un artefact ; dans la
  réfutation de C-P2 et de C-P6 (borne haute de Ḡ sous 0,10), ces tirages poussent vers la réfutation (asymétrie à
  déclarer, R4). La « raison de principe » (cohérence avec C-P2 et C-P6, qui lisent Ḡ partout) tient ; sa prémisse,
  non. (b) Entre les deux lectures, celle qui est retenue est la moins sévère pour l'« établie » de C-P3a et de
  C-P3b (la lecture écartée les rendrait illisibles sans attaque) et la plus sévère pour C-P3c (elle fait jouer la
  clause pour C-P3c : 54 cases sur 96 au-dessus du seuil, d'après le rapport de la grille). Elle a été choisie après
  lecture de ces taux simulés (réserve de méthode du 19 novembre). C'est une précision d'une ambiguïté réelle, mais
  elle fixe quand deux prédictions peuvent être « établies » : la conduite ne peut pas la laisser passer par un
  défaut silencieux.
- **Correction demandée** : remplacer la prémisse par « Ḡ reste lu même quand ĉ s'échappe ; il est alors proche de 0
  par construction (décalage), ce qui tire C-P2 et C-P6 vers la réfutation et met du bruit dans les rangs » ;
  déclarer que la lecture retenue n'est pas la plus sévère pour C-P3a et C-P3b et qu'elle a été écrite après
  lecture des taux simulés ; porter H-1 au directeur comme nœud (sans défaut), avec les deux lectures en regard.
  Rapporter, pour chaque couple, la part des tirages où ĉ s'échappe à côté de Ḡ.

### CB-05 — majeure — « contre-lu par un autre modèle » ne dit pas ce qui arrive si la contre-lecture trouve une faute
- **Lieu** : bloc de la stabilité de rang, « Condition, mécanique » et issue 3 ; verrou 10.
- **Citations** : « le rapport de la grille … (verrou 10 : sous-agent neuf, qui ne soit pas le rédacteur ; contre-lu
  par un autre modèle) couvre … toutes les cases » ; issue 3 : « rapport absent au scellement, non contre-lu par un
  autre modèle, ou auquel manque une case » ; verrou 10 : « le rapport complété sur cette liste et revérifié par son
  contre-lecteur ».
- **Constat** : un rapport contre-lu dont la contre-lecture laisse une remarque bloquante (comme la première, CG-01)
  ou des corrections non vérifiées : issue 1 ou 2 (il est « contre-lu »), ou issue 3 ? Deux lectures, et c'est ce
  qui décide entre les versions (a) et (b) de D-9.
- **Correction demandée** : écrire « contre-lu par un autre modèle, sans remarque bloquante ouverte, ses corrections
  vérifiées par le même contre-lecteur » dans la condition et dans les issues ; sinon issue 3.

### CB-06 — mineure — liste finie : « sinon l'issue 3 s'applique » se rattache au mauvais membre
- **Lieu** : liste finie, « Nombre de niveaux ».
- **Citation** : « Si l'appariement … diffère (contrôle par programme au scellement), la liste est rejouée sur ces
  longueurs avant le scellement ; sinon l'issue 3 s'applique. »
- **Constat** : lu à la lettre, « sinon » veut dire « s'il ne diffère pas », ce qui est absurde.
- **Correction demandée** : « s'il diffère et que la liste n'est pas rejouée avant le scellement, l'issue 3
  s'applique ».

### CB-07 — mineure — CR-01 porté en partie : deux renvois manquent
- **Lieu** : Métrique, point 8 bis (tests du module, l. 1043 à 1058) ; Métrique, point 12.
- **Constat** : la précision 33 fixe « points 8 bis et 11 » ; seul le point 11 y renvoie. La précision 5 fixe
  « points 11 et 12 » ; seul le point 11 y renvoie. Tous les autres passages de la table des passages fixés
  portent leur renvoi (contrôle par programme, précisions 1 à 39).
- **Correction demandée** : ajouter « (Plan, section 8, précision 33) » au point 8 bis et « (précision 5) » au point 12.

### CB-08 — mineure — liste d'arrêt 1 : « aujourd'hui » est le 19 novembre
- **Citation** : « 736 fichiers sous `src/` et `tests/` en diffèrent aujourd'hui, 734 ajoutés et 2 modifiés ».
- **Constat** : vrai au commit `48e08c72` (recompté : 734 A, 2 M) ; au commit `00406495` de `main` (22 novembre) :
  1 089 ajoutés, 3 modifiés. Le texte se dit à jour au 22 novembre.
- **Correction demandée** : « au 19 novembre (commit `48e08c72`) », ou le compte du jour.

### CB-09 — mineure — précision 39 : dénominateur et relecture de H sous la condition du saboteur
- **Lieu** : Plan, section 8, précision 39 ; Métrique, point 14 (entrées de l'appel au harnais).
- **Citations** : « mêmes tâches et mêmes tirages que D₀ » ; « Une tâche dont une des quatre relectures manque sort
  des deux parts » ; « Entrées de l'appel au harnais : l'identifiant de la tâche, la condition de la relecture, le
  rang du pas et l'historique rejoué …, rien d'autre ».
- **Constat** : (a) quand des tâches sortent, D₀ se calcule-t-il sur toutes les tâches ou sur les tâches gardées ?
  Deux lectures. (b) H• demande au harnais ce que la condition du saboteur pose à chaque pas d'un épisode honnête ;
  si cette condition comporte un tirage (budget ou dose de sabotage par action, T0.6) ou un état propre au
  saboteur, il n'est pas dans les entrées permises : la tâche sort ; le taux de sortie peut dépasser 5 % et rendre
  les parts « non mesurées ». Le point 14 couvre la sortie, pas la question de savoir si un tirage de la condition
  fait partie de « l'historique rejoué » (même risque pour L-SP, déjà présent en r3).
- **Correction demandée** : (a) « D₀ recalculé sur les tâches gardées, et D₀ de toutes les tâches écrit à côté » (ou
  l'inverse, dit) ; (b) écrire si un tirage de la condition est une entrée de l'appel (graine de l'épisode) ou fait
  sortir la tâche ; le dire aussi pour L-SP.

### CB-10 — mineure — précision 39 : lecture « proches de 1 / proches de 0 » sans seuil dans une ligne sans verdict
- **Citation** : « Deux parts proches de 1 : la sonde suit le contexte, non les jetons de l'action ; proches de 0 :
  elle suit les jetons de l'action. »
- **Constat** : « proche » n'est pas défini ; les cas mêlés (π_S ≈ 1, π_H ≈ 0) et les parts hors de [0 ; 1] ne sont
  pas dits. Une lecture qualitative sans seuil invite une lecture après coup.
- **Correction demandée** : présenter ces deux phrases comme les deux pôles d'un modèle, « aucune lecture n'est tirée
  des valeurs intermédiaires ni des parts hors de [0 ; 1] ».

### CB-11 — mineure — mention placée dans la seule colonne « non concluante » de la ligne C-P4 HC2
- **Lieu** : Critères, tableau, ligne C-P4 HC2, dernière colonne ; lignes C-P4 HC2b, C-P4b, C-P4c, C-P6 sans mention.
- **Constat** : la combinaison « Mode d'induction » dit « quelle que soit son issue », mais un programmeur qui lit le
  tableau seul poserait la mention sur la seule issue « non concluante » de HC2.
- **Correction demandée** : une phrase sous le tableau, « toute issue des lignes … porte la mention … (réserve 20) »,
  ou la mention dans chaque ligne concernée hors des colonnes d'issue.

### CB-12 — mineure — « organisme », au singulier, reste dans la section 3
- **Citation** : « les deux dont l'écart au plancher aléatoire apparié en covariance (critère 3 du verdict de G0,
  organisme du mode « coût gonflé ») est le plus grand ».
- **Constat** : la précision 38 prime sur ce passage, mais l'en-tête dit justement que le singulier était le défaut.
- **Correction demandée** : « dont l'écart au plancher, au sens de la précision 38, est le plus grand ».

### CB-13 — mineure — la note des différences dit inchangées les 37 précisions
- **Pièce** : `note-differences-r3-brouillon7-relance-v1.md`, section 1 : « les 37 précisions de la section 8 ».
- **Constat** : T-34 et T-35 complètent les précisions 20 et 36 (listes allongées) ; T-32 change l'introduction de la
  section 8. Changements mécaniques, mais la phrase est fausse.
- **Correction demandée** : corriger la note (errata de classe C).

### CB-14 — mineure — l'en-tête cite R-4986, qui nomme une autre session
- **Citation** : « une session fille (`session_013QMayk1rjSZrn2u9UAVhEp` …), sous les accords GO-2026-11-22-77 et
  GO-2026-11-22-113 (`registres/go.md` ; R-4986) ».
- **Constat** : R-4986 nomme pour le papier C `session_013QMayjXiKrxX5pMNVdSJNU` ; la session du rédacteur est
  recréée par R-4987 (GO-2026-11-22-114, effort « xhigh »).
- **Correction demandée** : citer R-4987 et GO-2026-11-22-114.

### CB-15 — mineure — R7 : « dose concave, en logarithme (2602.13568, p. 3) » dit plus que la page
- **Lieu** : Prédiction, contre-indices, « Forme de la loi » (hérité de r3, non ajouté par ce brouillon).
- **Constat** : p. 3 du PDF (`eca410e0…`) porte une régression où « group size (log-transformed) » est un choix de
  modèle des auteurs ; la seule phrase sur une saturation (« effects often saturate as groups grow ») est une revue
  de la littérature humaine (p. 1).
- **Correction demandée** : « régression sur le logarithme de la taille du groupe (choix des auteurs) », ou retirer
  « concave ».

### CB-16 — mineure — réserve 20 (b) : la famille (ii) n'est pas « apprise sans texte de consigne » au même sens que (iv)
- **Citation** : « ni à un saboteur dont la politique est apprise sans texte de consigne (famille (ii) du brief ;
  famille (iv) de N-053, point 2) ».
- **Pièces** : brief v2, T0.6 : (ii) « générer avec l'instruction cachée, entraîner sans elle » ; N-053, point 2,
  distingue (iv).
- **Correction demandée** : « sans consigne en contexte : famille (ii), distillée de générations sous consigne ;
  famille (iv), apprise sans texte de consigne ».

### CB-17 — mineure — R6 : la liste finie et huit autres pièces sont citées sans empreinte
- **Constat** : le texte ne donne l'empreinte ni de `liste-finie-cases-grille-v1.md` (`0c62072c…`, pièce normative : les
  constantes du modèle n'y sont que là), ni de huit pièces citées par leur nom nu (contrôle rejoué : `derivation.py`,
  `table-traitement-brouillon5-v1.md`, `docs/sha256sums-lancement-v2.txt`, `ecrire_config_v1.py`,
  `ecrire_config_brouillon2_v1.py`, `note-differences-brouillon5-brouillon6-relance-v1.md`,
  `table-traitement-contre-lecture-brouillon6-relance-v1.md`, `table-traitement-verification-c1-v1.md`). Aucune
  n'est en désaccord : l'empreinte voisine est celle d'une autre pièce.
- **Correction demandée** : écrire chemin et empreinte de la liste finie dès maintenant (le marqueur
  `<<RAPPORT_GRILLE_V2>>` la recopiera aussi) ; pour les autres, chemin et empreinte, ou les laisser comme renvois
  d'histoire sans valeur normative.

### CB-18 — mineure — verrou 8 : la ligne GO-2026-11-22-93 ne nomme pas les accords du pilote
- **Constat** : la ligne GO-2026-11-22-93 renvoie à la table de la veille (§ 1, branche `claude/veille-de-cap-v1`), que
  je n'ai pas pu lire (branche absente de ce dépôt) ; elle ne nomme ni GO-2026-10-20-06 ni GO-2026-10-20-07.
  L'affirmation du texte est donc invérifiable sur `main`.
- **Correction demandée** : citer la table (chemin, empreinte `a1c56fda…` complète) et les lignes qui portent ces deux
  accords. Sans effet sur une règle (D-24 est un nœud).

### CB-19 — mineure — forme : identifiants seuls dans les passages neufs
- **Lieu** : réserve 20 (« brief v2, T0.6 et T0.7 ; N-053, point 2 ») ; précision 38 (« N-063, version 2 ») ;
  réserve 20 (b) (« N-054 »).
- **Constat** : la règle de nommage de `CLAUDE.md` veut le nom en clair d'abord.
- **Correction demandée** : « organismes modèles (T0.6) », « batterie de sondes et son test de validité (T0.7) »,
  « critère des sondes jugé aux seules doses où la base mots et coût échoue (N-063, version 2) », « un mode de
  sabotage non chiffré (N-054) ».

## 2. Réponse aux neuf points de la consigne

1. **Le différentiel est celui de la table.** Le programme de construction, rejoué dans mon bloc-notes, rend
   `9c7a89f1…` (240 050 octets) et un journal identique, octet pour octet, à
   `construire_brouillon7_relance_v1.journal.tsv` (`fd12d38c…`). Le programme ne fait que des remplacements exacts
   (chaque fragment trouvé une fois, gardes de sortie) ; les 41 lignes du journal égalent la table de la note
   (identifiants, signes retirés et écrits). J'ai relu le `diff` r3 → brouillon 7 bloc par bloc : chaque bloc
   correspond à un remplacement de la table, à son lieu et à son motif. **Aucun changement hors de la table.**
   Petite inexactitude de la note (CB-13).
2. **Rien de ce qui est tranché n'a bougé**, sauf ce qui suit. Inchangés : énoncés de HC1, HC2, HC2b, HC3 ;
   tableau des prédictions C-P1 à C-P6, signes, marges, seuils ; section « Seuil » ; règle de HC2 (D-15) ; bloc de
   stabilité de rang et ses trois issues ; les vingt décisions D-1 à D-20 ; l'audit de symétrie ; les précisions 1
   à 19, 21 à 35 et 37, mot pour mot. Ont bougé, mécaniquement : précisions 20 et 36 (listes allongées des parts) ;
   introduction de la section 8 ; gardes 15 et 20 (complétées) ; ligne C-P4 HC2 du tableau des critères (mention) ;
   une combinaison neuve (« Mode d'induction ») ; le compte des relectures forcées (T-26, une incohérence de r3
   corrigée : le point 14 en écrit trois par contenu SP_m et SU) ; Plan, section 3, « Sondes » (renvoi à la
   précision 38, qui change la règle de désignation : proposition D-21).
3. **La version r3 a-t-elle porté CR-01 à CR-10 ?** CR-01 : portée en partie (clause conditionnelle retirée, table
   des passages fixés écrite, renvois présents partout sauf deux : point 8 bis pour la précision 33 et point 12
   pour la précision 5 : CB-07). CR-02 : portée (lecture symétrique à la précision 18, au Plan, section 2,
   et au tableau). CR-03 : portée, points (1) à (4), limite déclarée. CR-04 : portée dans sa seconde forme (réserve
   jamais retirée, taux recopié `<<RAPPORT_RESERVE_INTENTION>>`, écrit à côté). CR-05 : portée, (a) entrées de
   l'appel, (b) appel distinct à la garde 20, (c) ce que mesure g_trahison,lex. CR-06 : portée (« 734 ajoutés et 2
   modifiés », recompté exact au 19 novembre ; promesse retirée) ; date à préciser (CB-08). CR-07 : portée. CR-08 :
   portée, avec deux choses en plus que l'option (a) ne disait pas, déclarées (point H-2). CR-09 : portée
   (√(n_éval / n)). CR-10 : portée en partie, refus partiel motivé et défendable (cases jouées d'abord, vérification
   courte de la session 16 à défaut ; chiffre 0,040 à 0,047 contrôlé dans `45a0d875…`, ligne 120).
   **Contre-lecture de la grille** : CG-01 portée (liste finie de 144 cases) ; CG-03 portée par la précision 37,
   avec la réserve de CB-04 ; CG-05 portée (règle (i)) ; CG-06 portée (R et seuils, recalculés : 0,0638 et 0,0549) ;
   CG-07 portée (T = 30) ; CG-08 portée (configuration `85173b22…`, contrôle au scellement ; phrase à corriger,
   CB-06) ; CG-09 portée (s₀ = σ) ; CG-10 portée (liste fermée ; les quatre cases hors liste, pour information).
4. **Ajouts de r3 jamais contre-lus.** Liste finie : 8 × 3 × 2 × 3 = 144, juste ; 108 cases pour le bras « contenu »,
   juste ; 58 et 48 cases à jouer, cohérent avec la table de la liste (colonnes « jouée » d'après le rapport v1, non
   vérifiées par moi). Dimensions : E30, E60, EH, K16 (κ), MH, k = 3 et 5, T = 45 et 60, corpus B viennent des mots
   de la clause ou du point 8 bis ; T = 30 et E40 viennent d'autres passages ; σ = 0,4 sous la compression, les trois
   valeurs de KH, M616, le profil du gain et le modèle des gains d'écart de C-P3c sont des choix, déclarés comme tels
   (« que la clause ne donnait pas ») ; réserve de méthode : écrits après lecture des taux simulés. Le sens de ces
   choix est surtout prudent (plus de cases, donc plus de chances que la clause joue) ; deux exclusions vont dans
   l'autre sens et sont déclarées (gain « fort » 0,30 ; quatre cases de CG-10, toutes sous le seuil). Précision 37 :
   précision d'une ambiguïté réelle, qui change pourtant quand C-P3a et C-P3b peuvent être « établies » ; prémisse
   inexacte et choix non le plus sévère pour ces deux lignes : CB-04 (nœud demandé). Trois issues : mécaniques et
   complètes, sauf le cas d'une contre-lecture qui trouve une faute (CB-05). Règle de remplissage du bras
   « contrôlabilité » : mécanique ; elle ajoute deux choses (pas de libellé anglais ; nœud si plusieurs chaînes ou
   aucune), déclarées et soumises au directeur (H-2) ; je n'y vois pas d'écart à R1.
5. **Ajouts de ce brouillon.** Précision 38 : mécanique pour (i) et (ii) jugés par dose, « sans objet », une seule
   famille ; non entière pour les familles (iii) et (iv), un verdict non ventilé par mode et la valeur de l'écart
   (CB-03). Citations du brief exactes (porte G0, critère 3 ; T0.7) ; citation de N-063, version 2, conforme à sa ligne
   de `CLAUDE.md`. Le choix du plus petit écart ne favorise pas de signe que je puisse nommer : il écarte les sondes
   qui ne séparent que sur (i), ce qui ferme la voie de confirmation à vide de la réserve 20 ; la sélection des deux
   plus grands écarts (héritée de r3) gonfle D₀ à G0 et peut le faire régresser à l'étape 2, sens net inconnu.
   Réserve 20 : juste dans son constat, incomplète dans son argument (CB-01) ; mention bien posée sur les lignes
   nommées, sans changer de verdict, mais absente de la ligne de la porte GC (CB-02) et mal placée dans le tableau
   (CB-11). Précision 39 : parts bien définies et calculables avec la fonction de reconstruction du point 14 (mêmes
   entrées, mêmes gardes, témoins de l'instrument sur S et H) ; dénominateur à fixer et question du tirage de la
   condition du saboteur pour H• (CB-09) ; « ce qu'elles ne disent pas » à compléter (effet du paragraphe de bras,
   CB-01) ; lecture qualitative à neutraliser (CB-10). Aucun des trois ajouts ne crée de revendication, de réfutation
   ni de confirmation : mention et parts sont rapportées, sans seuil ; la phrase « une ligne HC2 confirmée ne se lit
   jamais comme la robustesse d'une sonde d'intention sur un agent sans consigne » restreint une lecture et ne touche
   pas l'énoncé retenu de N-068. Aucune phrase ne vise un signe.
6. **R7.** Le différentiel n'ajoute aucun chiffre de l'état de l'art (seuls des seuils d'instrument, des comptes de
   fichiers et des citations du brief et des décisions). Échantillon contrôlé sur PDF au dépôt, empreinte recalculée
   et page lue : Panin (`27f88ed7…`) p. 11, « a deference screen must not threshold the outcome », conforme ; p. 6 (et
   p. 1), poids quasi binaire chez trois modèles sur cinq, conforme ; Bajaj et Tiganj (`eca410e0…`) p. 3,
   k ∈ {1, 3, 5, 9}, conforme ; log-cotes OUI/NON de Llama-3.3 70B sur BoolQ, conforme ; « dose concave, en
   logarithme », p. 3 : non conforme au sens strict (CB-15) ; « The Silent Judge » (`c97ff1b4…`) pied de page de la
   p. 1, atelier « Reliable ML from Unreliable Data », conforme ; hiérarchie Expert > Humain > LLM > Inconnu, conforme
   (dans les p. 1 à 5 citées) ; 2608.25869 (`f54d19a5…`) p. 6, ancre 1,0 à 3,9 et masse du 5 vers le 4, conforme ; p. 7, pente
   0,267 et tableau 7, conforme ; Kim et Flanigan (`682a2dad…`) p. 4 et tableau 4 p. 12, conforme ; Venkatesh et al.
   (`59f4b700…`) figure 1 p. 3 (trois moniteurs sur cinq sans effet), conforme ; figure 2 p. 4, conforme ;
   2510.09462 v2, « p. 5 » : conforme en numérotation imprimée (page 7 du fichier, figure 2, score 0 sur 375) ;
   2505.23575 v3 p. 7, la consigne de discrétion fait monter la capture, conforme. **Non contrôlables faute de PDF au
   dépôt** : 2611.04556, 2606.05384, 2608.12645, 2610.18408, 2606.10304, 2608.21664, 2611.10620, 2602.08877,
   2602.00750, 2609.05797, 2610.29178, 2507.08794, 2606.13757, 2609.19587, 2610.17301, 2610.37679 ; 2609.03035 est
   cité en v2, seule la v1 est au dépôt.
7. **R6 et R11.** Contrôle des empreintes citées rejoué par un programme à moi, même règle que celui du rédacteur,
   mais sans recherche récursive hors des dossiers du papier C (copie de la branche du 19 novembre limitée à ces
   dossiers et aux deux notes de voisins). Aucun couple en désaccord. Les neuf « à regarder » sont des pièces sans
   empreinte écrite (CB-17). Les décisions, les rapports du niveau 2, le gabarit, le validateur, l'état de l'art
   de niveau 3, `CLAUDE.md` (`605db83a…`), `registres/go.md` (`f09e28de…`), `registres/decisions.md` (`af162226…`),
   le brief et le programme : empreintes recalculées par chemin, conformes. Les « introuvables » sont des pièces à
   venir, d'une autre branche ou de `donnees/` (non ouvert). Le compte de 1 669 fichiers absents de `main` (verrou 14)
   est exact. La ligne 323 de la liste v19 existe (ligne 405 du fichier). Une affirmation invérifiable : CB-18.
8. **Validateur.** `problemes` rend la section « Contre-lecture » à remplir et seize marqueurs : les quinze de r3
   (recomptés sur la source) et `<<MOT_DU_DIRECTEUR_D21_D22>>`. Conforme à la sortie versée.
9. **Forme.** Français ; chaque précision est nommée dans les passages qu'elle fixe, sauf deux renvois (CB-07) ; les
   précisions 38 et 39 sont nommées dans tous leurs passages. Identifiants seuls dans les passages neufs : CB-19.

## 3. Autres constats, pour la session mère (hors du texte)
- Le journal du rédacteur déclare (écart 1) une recherche de mots sur une copie de travail qui contenait par
  mégarde `brouillons/ii-b-saboteur-budget-v1/` ; seuls des noms de fichiers sont sortis. Déclaré ; à consigner
  par la mère au registre du cloisonnement si ce n'est pas fait.
- Le rédacteur n'a lu ni la liste finie, ni le rapport de la grille, ni sa contre-lecture (journal) ; je les ai lus
  en partie (voir ci-dessous) : ses phrases sur ces pièces sont conformes.
- Conséquence à connaître de la précision 38 (le rédacteur la dit, D-21) : dans le mode « coût gonflé », le
  sabotage s'écrit en clair ; si la base « mots et coût » réussit à toutes les doses, le critère 3 est « sans
  objet » et HC2 n'a aucune sonde : nœud à l'ouverture de l'étape 2.

## 4. Ce que j'ai lu, en fait
- `CLAUDE.md` (dans le contexte de la session) ; la consigne du contre-lecteur ; le texte relu, en entier ; la
  source r3, par son empreinte et le `diff` complet r3 → brouillon 7 ; le `diff` complet r2 → r3 (r2 extraite de la
  branche du 19 novembre, lue seulement par ce différentiel).
- Dossier `redaction-brouillon7-relance-v1/` : note des différences ; points ouverts pour le directeur ; additif à
  la fiche du module ; journal du rédacteur ; contrôle des empreintes citées ; sortie du validateur ; programme de
  construction (structure, remplacement T-41 et fonction principale ; exécuté) ; journal de construction (trois
  colonnes, et comparaison octet pour octet) ; programme de contrôle des empreintes (en entier).
- Branche `claude/papier-c-preenregistrement-v1`, commit `48e08c72` (par `git show` et `git archive`, dossiers du
  papier C seulement) : rapport de la contre-lecture de r2 (`71996527…`, en entier) ; table de traitement
  (`2d146ba8…`, en entier) ; liste finie (`0c62072c…`, sections 1 à 3 et début de la table) ; contre-lecture du
  rapport de la grille (`d0485a40…`, sections 2 et 3) ; rapport de la grille (`8d1616fc…`, sections 1 et 10, et
  titres) ; fiche du module v3 (`60f79bf8…`, titres seulement) ; décisions exigées v4 (`054d8347…`, titres
  seulement) ; décisions v3 : non lues (empreinte vérifiée par le texte seulement) ; vérification courte de la
  session 16 (`45a0d875…`, lignes trouvées par les chiffres cités) ; manifeste et configuration de la grille
  (empreintes seulement).
- `main` : brief v2 (T0.6 à T0.9, porte G0, section 9 : lignes 155 à 205 et 248 à 275) ; N-053 (en entier) ;
  `registres/go.md` (lignes GO-2026-10-20-06, -07, GO-2026-11-19-53, -74, GO-2026-11-22-77, -79, -93, -113) ;
  `registres/decisions.md` (lignes R-3887, R-4986, R-4987) ; liste « qui a lu quoi » v19 (ligne 323, et lignes 238 à
  248 affichées par erreur de numérotation) ; noms des fichiers de `registres/`. Programme v2, N-005 et N-006,
  N-013, N-023, N-026, N-065, N-068, N-075 à N-077, gabarit et validateur : empreintes seulement (le validateur est
  exécuté, non lu).
- PDF (`docs/sources/pdf/`, pages citées seulement) : `ssrn-7424179-panin-2026-v1.pdf`, `2602.13568v1.pdf`,
  `2509.26072v2.pdf`, `2608.25869v1.pdf`, `2606.14037v1.pdf`, `where-empathy-goes-wrong-venkatesh-2026-v1.pdf`,
  `2510.09462v2.pdf`, `2505.23575v3.pdf` ; `2606.18276v1.pdf` et `2607.08066v1.pdf` ouverts sans conclusion (non
  comptés dans l'échantillon).
- Métadonnées git : `git diff --name-status` de `7a54d43` à `48e08c72` et à `00406495` sous `src/` et `tests/` (noms
  seulement) ; arbre de `48e08c72` comparé à celui de `00406495` (noms seulement).
- Non lus : le code du module et du harnais, toute consigne privée, `donnees/`, `diag/`, `runs/`, `docs/verdicts/`,
  `src/controle_ia/bases/scores_jetons.py`, N-063, N-054, la table des accords prolongés (branche absente).

## 5. Avis d'ensemble
**Scellable après corrections.** Le texte ne diffère de r3 que par les 41 remplacements de sa table ; r3 porte
CR-01 à CR-10 (deux en partie) et ce qu'elle tire de la contre-lecture de la grille. Avant le scellement : corriger
les cinq majeures (CB-01 à CB-05) et les mineures, ou écrire leur refus ; porter au directeur la précision 37 comme
nœud (CB-04) et ses propositions D-21 et D-22 ; lever les verrous 3, 4, 6, 9, 10, 11 et 14 ; vérification des
corrections par le même contre-lecteur.
