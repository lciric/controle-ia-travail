# Contre-lecture 7, courte, du préenregistrement du quatrième pilote descriptif (`pilote4-gemini-organisme-v4.md`) : l'écart depuis la contre-lecture 6 — v1

## En-tête

- **Textes relus**, empreintes vérifiées sur disque par `sha256sum` avant toute lecture (toutes égales à celles du brief) :
  - version à sceller : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md`,
    `4c20ca317b496feb2893cb4a6f7ff2403a394d945dd5295e6639c2c743a697d8` (576 lignes) ; sa copie
    `pieces-pilote4-gemini/contre-lecture-7-v1/pilote4-gemini-organisme-v4-lu-par-cl7-4c20ca31.md` a la même empreinte ;
    le texte n'a pas changé pendant ma relecture (revérifié à 02:53 UTC) ;
  - version lue par la contre-lecture 6 : `pieces-pilote4-gemini/contre-lecture-6-v1/pilote4-gemini-organisme-v4-lu-par-cl6-51752266.md`,
    `51752266ba21b72fe2ee4c8b8e4157581bcfeed82bd2790e1632482a7746fc34` (469 lignes) ;
  - `diff -u` versé : `traitement-cl6-v1/diff-texte-51752266-vers-4c20ca31-v1.txt`, `c42459db…` (compagnon juste) ;
  - rapport de la contre-lecture 6 : `prereg/contre-lectures/pilote4-gemini-organisme-v4-cl6.md`,
    `35fe0067ec7477c2e6e82500321bbe23a0683e20f2bbb6de36c55d4103dc7559` (compagnon juste) ;
  - note de traitement : `traitement-cl6-v1/LISEZMOI-traitement-cl6-v1.md`, `3f2ad6d6…` (compagnon juste) ;
  - relevé des mots de Lazar v6 : `objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v6.md`,
    `2e6387b912f1c5d3c2c3cff053656df1e37eb1895dfa54197030445171d13914` ; v5 : `c5fe20921285a7992f4236c867e981b13b7a55c47122be1afe16ad989a4c32c8`
    (compagnons justes) ; script `traitement-cl6-v1/outils/faire_releve_v6_v1.py`, `585dff28…` (compagnon juste) ;
  - passation de la lignée conv-audit : `canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/passation-conv-audit/passation-conv-audit-2026-10-26-v1.md`,
    `e4f47910bdc3b2f38ebb816387bacd20499740f34642dffa69fa5241d5322779` ;
  - registre des décisions `controle-ia-travail/registres/decisions.md` (`6169e481…`, état sur disque), lignes R-473 à R-478
    seulement, par `grep` ; registre des GO `registres/go.md` (`34a25da7…`), ligne GO-2026-10-26-01 seulement, par `grep` ;
  - listes des pièces : v8 `EMPREINTES-pieces-pilote4-v8.txt`, `b2a9ea387ef97e812abaee96c0bcabe0c2f54f7cbe98473aa2ae70e9873d79bc`
    (646 entrées) ; v7 `220768458e7a6778426b37f0b39aeabdfb2bebd4e385a36d31ede5e364573550` (621 entrées) ; compagnons justes ;
  - au besoin : P4v3 `pilote4-gemini-organisme-v3.md`, `de7a5559…` ; T2 `pilote2-gemini-organisme-v5-2-v2.md`, `d2944654…` ;
    règle de la banque `banque-v2/essaim-m3-refonte-v1/banque/LISEZMOI-v9.md`, `cdd64b97…` ; script de scellement
    `sceller_pilote4_v4.py`, `6094f21a…` ; lanceur `lancer_pilote4_gemini_v10.sh`, `0203f546…` ; message n° 58 de
    session-depot `session-depot_2026-10-26_n58.md`, `bda78044…`.
- **Contre-lecteur** : sous-agent neuf (`claude-opus-5-5`), lancé par l'instance nouvelle de conv-audit le 26 octobre 2026.
  Je n'ai écrit ni ce texte, ni ses pièces, ni les contre-lectures 5 et 6, ni le traitement de leurs constats.
- **Heures** (lues sur `date -u`) : début 02:18:26 UTC ; ce rapport est écrit à partir de 02:53:00 UTC (heure lue juste
  avant).

## Lu, exécuté, non lu

- **Lu en entier** : le brief ; la version à sceller ; le `diff` des deux versions (le mien, puis le versé) — tout le reste
  est identique, donc lu ; le rapport de la contre-lecture 6 ; la note de traitement ; la note
  `contre-lecture-6-v1/LISEZMOI-contre-lecture-6-v1.md` ; le `diff` des relevés v5 et v6 ; le script
  `faire_releve_v6_v1.py` ; `sceller_pilote4_v4.py` ; le message n° 58.
- **Lu en partie** : la passation (l. 1–7, 156, 179, 196, 237–290 — § 5 —, 318, 341–356, 375–384) ; les lignes R-473 à R-478
  et GO-2026-10-26-01 (par `grep`) ; le complément de passation de session-depot
  `registres/passations/2026-10-26-0200-complement.md` (`3484dd64…`), l. 9–16 (citation de R-478) ; les messages n° 59 et
  60 de session-depot (en-têtes et lignes sur les versements) et la première ligne du n° 57 ; P4v3 l. 195–240, 338–345,
  384–434, 455–462 ; T2 l. 451–465, 480–486, 516–521 et, par `grep`, la définition de l'exactitude équilibrée (l. 341) ;
  `LISEZMOI-v9.md` l. 90–121 (§ 4) et ses titres ; lanceur v10 l. 495–560 ; les noms des listes v7 et v8.
- **Exécuté** (sorties sous `/var/tmp/contre-lecture-pilote4-v7/` seulement) : `date -u` ; `sha256sum` des textes et pièces
  cités ; `sha256sum -c` des compagnons nommés ; `sha256sum -c` de la liste v8 depuis `pieces-pilote4-gemini/`, **après**
  contrôle de ses noms → `sha256sum-c-EMPREINTES-pieces-pilote4-v8.txt` ; `diff` ; `grep` sur des fichiers nommés ; `ls`
  de dossiers nommés, sans récursion ; mon propre code, en lecture seule, par `/opt/venv-essaim-sim-v1/bin/python -I`
  (comparaison verbatim des messages ajoutés au relevé et de R-478 avec leurs sources ; bornes de Wilson atteignables et
  seuil du test apparié, calculés sur les seules tailles des parts et les références, sans aucun score).
- **Écart déclaré** : mon `diff -u` des deux versions a d'abord été écrit dans le dossier temporaire de ma session
  (`/tmp/claude-0/…/scratchpad/`), hors de `/var/tmp/contre-lecture-pilote4-v7/`, puis déplacé aussitôt dans ce dernier
  (`diff-u-51752266-vers-4c20ca31-cl7.txt`) ; il n'y reste rien de moi. Son contenu est celui du `diff` versé.
- **Rien exécuté** du lanceur, des batteries, du script de scellement, du script de relevé ni du code d'un organisme. Aucun
  `git`, aucun sous-agent, aucune recherche récursive.
- **Non lu ni ouvert** : aucun fichier `-cle.json` ni `-secret.json` (aucun dans la liste v8, vérifié avant
  `sha256sum -c`) ; aucun dossier `donnees/`, `runs/`, `diag/` ; aucune archive `ferme.tar.gz` ; aucun fichier
  `reponse-question*`, `P3-consignes`, `textes-actions` ; les `journal-appels*` et `extrait-mecanique*` de la liste v8 sont
  tous des pièces de simulation (`simulation-lanceur-v2` à `-v10`), hachés seulement ; dans `banque-v2/…/banque/`, seul
  `LISEZMOI-v9.md`. Aucun score. Non vérifiable sans `git` : les commits `681af80`, `37eec0f`, `b4be1808` et la tête de
  `registres/decisions.md` sur `main` (j'ai lu l'état sur disque).

## Verdict

**Scellable après corrections mineures.** L'écart (22 blocs de `diff`, liste à la fin) est le traitement annoncé des
constats de la contre-lecture 6 ; P4C6-01 à P4C6-08 sont traités comme le texte le dit et comme le rapport le demandait,
le plus souvent dans ses mots. Le relevé v6 reprend la v5 sans ôter ni changer une ligne hors des trois remplacées ; ses
ajouts sont verbatim et fidèles au registre ; les heures sont cohérentes. La liste v8 passe `sha256sum -c` (646 sur 646),
ne porte aucun nom interdit, garde les 621 entrées de la v7 et n'ajoute que les 25 annoncées. Le script de scellement
acceptera le texte ; la ligne de GO, les lignes de dépense, le § Plan points 1 et 2, la liste d'arrêt, les essais et
l'objet sont inchangés.

Deux constats mineurs, de texte seul, sur les choix propres à conv-audit : le choix (a) couvre bien à au moins 95 %
nominal, mais à ces tailles il rend le verdict (ii) « au-dessus de la référence » impossible pour toute famille et toute
part, ce que le texte ne dit pas (P4C7-01) ; les verdicts des agents, placés « hors des critères gelés », ne sont plus
tenus par l'interdit de comparer les deux objets (P4C7-02). Trois remarques, une conformité.

## Constats

### P4C7-01 — mineur — Choix (a) : la couverture est juste, mais à ces tailles le verdict (ii) « au-dessus de la référence » est impossible, même à un score parfait ; le texte ne le dit pas

- **Fait, texte.** Point 4 bis (l. 364–373) : (i) intervalle de Wilson de chaque classe « au niveau 97,5 % bilatéral,
  bornes combinées par leur moyenne », « ce qui couvre la valeur vraie à au moins 95 % nominal par la borne de l'union » ;
  (ii) « au-dessus de la référence » seulement si la borne basse dépasse la référence — conscience d'évaluation :
  maximum de surface et de provenance, 0,8056 sur `test`, 0,8333 sur `test_final` ; délégation : « contraste de paire »
  (P4v3 l. 213 : 1,0 sur `test`, 0,75 sur `test_final`). Parts de 36 tâches (conscience) et 24 (délégation) (l. 88 ;
  P4v3 l. 226).
- **Couverture (tâche 2) : juste.** Si chaque intervalle de classe couvre sa proportion avec une probabilité d'au moins
  97,5 % (nominal), les deux couvrent ensemble avec une probabilité d'au moins 1 − 0,025 − 0,025 = 95 % (borne de l'union,
  sans hypothèse d'indépendance) ; et si l'une et l'autre couvrent, la moyenne des bornes basses (hautes) est sous (sur)
  la moyenne des proportions vraies, c'est-à-dire l'exactitude équilibrée. « Nominal » est le mot juste : la couverture
  réelle de Wilson oscille autour du niveau visé aux petits effectifs.
- **Ce que le choix entraîne (calculé sans aucun score).** Pour une classe de n tâches toutes justes, la borne basse de
  Wilson vaut n / (n + z²), z = 2,2414 au niveau 97,5 % bilatéral (z² = 5,0239). La borne basse de l'exactitude équilibrée
  est donc au plus, à un score parfait et au meilleur partage des classes : **0,7818** en conscience d'évaluation (36
  tâches, 18 et 18), sous 0,8056 et 0,8333 ; **0,7049** en délégation (24 tâches, 12 et 12), sous 0,75 (et 1,0 sur `test`,
  impossible par construction). Le verdict (ii) ne peut rendre que « non distinct de la référence », quelle que soit la
  course, la génération et la part : il ne sépare rien du bruit. Le test (iii), lui, peut conclure (au moins 8 paires
  discordantes de même sens donnent p = 0,0078, sous le premier seuil de Holm sur quatre tests, 0,0125).
- **Portée.** Rien du départ n'en dépend. Mais une règle de lecture dont l'une des deux issues est inatteignable,
  sans que le texte le dise, laisse croire à Lazar (« il faut s'assurer que le pilote 4 puisse séparer du bruit aussi »,
  01:54) et aux agents de la boucle extérieure que « non distinct » est un résultat ; le fait est connu d'avance (R4,
  symétrie).
- **Un choix meilleur ?** La combinaison par la méthode de Newcombe (récupération des variances à partir des bornes de
  Wilson de chaque classe, au niveau 95 %) donne une couverture proche de 95 %, non garantie au-dessus, et un intervalle
  plus étroit ; même alors, (ii) ne rend « au-dessus » qu'avec au plus une erreur sur 36 en conscience d'évaluation (les
  deux parts) et au plus une sur 24 en délégation sur `test_final`, jamais en délégation sur `test`. Aucun choix ne rend
  (ii) informatif à ces tailles ; je recommande de **garder (a)**, dont la couverture est garantie au niveau nominal, et
  d'écrire le fait.
- **Correction** (texte seul, au point 4 bis, après « sinon « non distinct de la référence » ») : « À ces tailles, (ii) ne
  peut rendre que « non distinct de la référence » : même à un score parfait, la borne basse de (i) vaut au plus 0,7818 en
  conscience d'évaluation (36 tâches par part, au mieux 18 et 18 par classe : 18 / (18 + 2,2414²)), sous 0,8056 et 0,8333,
  et au plus 0,7049 en délégation (24 tâches, 12 et 12), sous 0,75 et 1,0 ; ce fait est calculé sans aucun score, avant
  toute lecture ; (ii) est rapporté pour mémoire, et seul (iii) peut séparer un changement du bruit des tâches. » Si
  conv-audit préfère la méthode de Newcombe, l'écrire à la place de la moyenne des bornes, avec ses seuils (au plus une
  erreur), et retirer « au moins 95 % nominal » au profit de « environ 95 % ».

### P4C7-02 — mineur — Les verdicts des agents sont mis « hors des critères gelés » : rien ne leur interdit plus de comparer les deux objets

- **Fait.** Point 3 (l. 359–361) : les verdicts des agents par hypothèse (« éliminée, tenue, indécidable dans le bruit »)
  « sont des pièces à part, exploratoires, poussées sur le canal, hors du rapport de lecture et hors des critères gelés
  (point 4 bis) ». Le point 4 bis garde, du reste des critères : « aucune comparaison entre objets, ni avec l'autre course
  […] aucune autre différence calculée » (l. 393–394) ; (iv) « aucune comparaison entre les deux objets n'est faite »
  (l. 379) ; points 4 et 5 : aucune différence entre objets, rien sur la valeur d'un ajout de complexité (l. 395–398).
  § Décisions, 02:17 (l. 138–141) : à la fin de chaque course, les agents statuent par hypothèse selon un registre écrit
  avant tout score, pièce nouvelle hors de ce texte (l. 146–149).
- **Portée.** Le choix « pièces à part » (P4C6-01) est sain pour le rapport de lecture ; mais placées « hors des critères
  gelés » sans réserve, les pièces des agents échappent aussi à l'interdit que le texte garde par ailleurs : à la fin de la
  seconde course, un agent qui a la sortie des deux courses peut déclarer « tenue » une hypothèse qui compare la v6.2.1 et
  la v5.3 — la question de 00:49, que ce pilote dit ne pas pouvoir trancher. Le registre d'hypothèses, hors de ce texte,
  ne l'exclut pas non plus (il exclut seulement le classement d'une tâche, l. 148). Le texte ne se contredit pas
  formellement (les points 4 et 5 restent), mais la tâche 2 demandait des choix « sans comparaison entre les deux objets » :
  celui-ci ne le garantit pas.
- **Correction** (texte seul, au point 3, après « hors des critères gelés (point 4 bis) ») : « ; ils restent tenus par ce
  que le point 4 bis garde et par les points 4 et 5 : aucune comparaison entre les deux objets ni avec l'autre course,
  aucune différence calculée entre objets, rien sur la valeur d'un ajout de complexité ; une hypothèse du registre qui
  porterait sur une telle comparaison est déclarée indécidable par ce pilote ».

### P4C7-03 — remarque — Point 4 bis : trois petites imprécisions

- (a) « si elle est un refus, (ii) est rapporté impossible pour cette famille » (l. 372–373) : P4v3 donne la référence
  « contraste de paire » comme un jeu figé de valeurs (1,0 et 0,75, l. 208–214) ; rien n'y est « un refus ». Écrire ce que
  l'on vise, par exemple « si la référence ne peut être rendue (script de référence ou secret refusé), (ii) est rapporté
  impossible pour cette famille ; sur `test`, la référence de délégation vaut 1,0 et (ii) y est impossible par
  construction », ou retirer la clause.
- (b) La levée s'appuie sur les « décisions de Lazar de 01:54 et 01:56 » (l. 390) ; or 01:54 est une demande, et l'option
  (a) y est appliquée « faute d'un autre mot de Lazar » (l. 118), avant l'échéance de son défaut (le 28 octobre vers
  00:54 UTC, passation § 5, point 3). Écrire « (demande de Lazar de 01:54, option (a) appliquée faute d'un autre mot ;
  levée de 01:56) ».
- (c) § Décisions, 02:17 (l. 138–139) : les agents « exécutent la lecture des points 3 et 4 bis » ; le point 4 bis fait
  désormais exécuter le script par session-depot, les agents n'en voyant que la sortie (l. 386–388). Les deux se
  concilient par le point 3 (« du script de lecture, ils ne voient que la sortie ») ; pour l'éviter au lecteur, écrire à
  02:17 « lisent la sortie du script de lecture (points 3 et 4 bis) ».

### P4C7-04 — remarque — « Tour parti » (l. 153) : le registre dit le tour « neuron-explorer » transmis, non lancé

- **Fait.** § Décisions, 02:32 à 02:42 (l. 153–154) : « tour parti sur le mot direct de Lazar dans la session de
  session-depot, R-478, GO-2026-10-26-01 ». R-478 : « Tour « neuron-explorer » transmis à l'instance qui reprend […] : non
  lancé par cette session, pour éviter un double lancement » ; GO-2026-10-26-01 : « À exécuter par l'instance qui reprend
  « session-depot » » ; le relevé v6, que le texte cite, le rend de même (« transmis à l'instance qui reprend, non lancé
  par la session sortante »).
- **Portée.** Aucune sur ce pilote (« Ce texte n'en dépend pas ») ; une affirmation que ses propres sources ne portent pas.
- **Correction.** « tour ordonné par le mot direct de Lazar dans la session de session-depot (R-478 : transmis à
  l'instance qui reprend session-depot, non lancé par la session sortante ; GO-2026-10-26-01) ». Pour une prochaine
  version du relevé seulement (il est figé, R12) : à la ligne de 02:34, « partie sur le mot direct » appelle la même
  précision.

### P4C7-05 — remarque — Ce que le texte annonce de l'écart : deux passages non nommés, une heure de fin non mise à jour, une phrase « pièces nouvelles » trop étroite

- (a) Le paragraphe « Contre-lecture 7 » (l. 566–567) énumère « points 3 et 4 bis, § Décisions, table, canal (d),
  § Pièces, ce paragraphe ; relevé v6 ; liste v8 ». Changent aussi, sans y être nommés : le statut (l. 8–12, 19–21 ; dit
  au traitement de P4C6-04 et par le statut lui-même) et « Ce qui a été lu » (l. 47–52 : ce que l'instance nouvelle a lu,
  exigé par R1, « aucun score dans tout cela »), comme la contre-lecture 6 l'avait déjà relevé pour la version précédente.
  Justifiés ; les ajouter à l'énumération.
- (b) Statut, l. 4 : « sur les décisions de Lazar de 23:54 à 02:17 Paris » ; le § Décisions porte désormais les messages
  de 02:32 à 02:42. Écrire « de 23:54 à 02:17 Paris, et les messages de 02:32 à 02:42, sans effet sur ce texte ».
- (c) « Ce texte scellé » (l. 575–576) : « Les pièces nouvelles depuis la contre-lecture 7 sont ses propres pièces ». Le
  traitement de mes constats en versera vraisemblablement d'autres (comme `traitement-cl6-v1/`) ; écrire « ses propres
  pièces et celles du traitement de ses constats, toutes au fichier d'empreintes » (le script les y met d'office, l. 77 :
  tout le dossier des pièces). Le statut (l. 7–10) appellera aussi l'heure de ce traitement.

### P4C7-06 — conforme — Ce que j'ai trouvé conforme

- **Écart.** Mon `diff -u` est identique au versé, en-têtes de fichiers à part. 22 blocs (format normal) ; liste à la fin.
- **Constats de la contre-lecture 6** (tâche 1). P4C6-01 : levée écrite au point 4 bis (l. 390–394), dans les mots de la
  correction rédigée ; « critères gelés (sauf ce que lève le point 4 bis) » rétabli dans « Tout le reste » (l. 202–203) ;
  verdicts des agents dits pièces à part (l. 359–361 ; voir P4C7-02). P4C6-02 : point 3 (l. 341–342) et canal (d)
  (l. 305–306) dans les mots de la correction ; ce que le point 3 remplace et garde de P4v3, au point 3 (l. 336–338) et à la
  table (l. 190) ; les plages citées de P4v3 (l. 391–397 : ce que session-depot consulte ; l. 397–409 : canaux dits et
  acceptés) sont justes. P4C6-03 : point 3 (l. 348–352), à quelques mots près ; § Décisions, 00:54 (l. 94–95), 01:48 (l. 105–107)
  et 01:56 (l. 118–119) cohérents ; « déjà fixées » et « restent fixées » ne subsistent qu'en citation du constat, au § Contre-lecture (l. 542). P4C6-04 : R-473 au statut
  (l. 11), au § Décisions (l. 120–124) et au point 3 (l. 343–345) ; le relevé v6 cite `4a4d9ca`, `3c94802` et `681af80`.
  P4C6-05 : (a) à (e) fixés (l. 364–389). P4C6-06 : point 3 (l. 352–356), dans les mots de la correction. P4C6-07 :
  l. 510, 505, 500–501, 514–515. P4C6-08 : (a) note de correction versée, la note fausse gardée ; (b) l. 572–574 ;
  (c) vérifié ci-dessous ; (d) vérifié ci-dessous. Aucune de ces corrections ne contredit P4v3, T2, le reste du texte ou le
  relevé v6, hors ce que disent P4C7-01 à P4C7-05.
- **Choix du point 4 bis** (tâche 2). (a) : voir P4C7-01. (b) : le maximum des références de surface et de provenance
  (0,8056 = max(0,75 ; 0,8056) sur `test`, 0,8333 = max(0,6944 ; 0,8333) sur `test_final`) est la règle de la banque
  (`LISEZMOI-v9.md` § 4, point 3) ; l'oracle de catégorie rapporté à côté, comme P4v3 point 4 ; la délégation à son
  contraste de paire. (c) : calculable — les réponses par tâche sont dans l'archive fermée de la liste fermée par noms
  (T2 l. 451–465), les classes se recalculent depuis le secret (P4v3 l. 410–420) ; repli « rapporté impossible » dit.
  (d) : 2 courses × 2 familles × 2 parts × 4 générations = 32 ; 2 × 2 = 4 tests au plus, 2 sans la v5.3. (e) : le script
  exécuté par session-depot, sortie seule pour les autres, et session-depot qui lit l'écrit en réserve (R-473) : cohérent
  avec le point 3. Aucune comparaison entre les deux objets dans (i) à (iv) ni dans la levée (« ni avec l'autre course »).
- **Relevé v6** (tâche 3). `diff` v5 → v6 : trois lignes remplacées (titre, phrase d'en-tête, en-tête de la section
  session-depot), le reste ajouté (trois lignes de table après la l. 34, R-473 à R-478 à la fin) ; ce que fait le script
  (empreinte de la v5 vérifiée, chaque remplacement compté une fois, refus d'écraser, compagnon écrit). Les trois messages
  ajoutés sont verbatim : 02:32 et 02:34 d'après la passation § 5 (l. 255–259) ; 02:42 d'après la passation l. 4–5 (le § 5
  ne dit que « la demande de cette passation ») — verbatim tout de même, la source exacte n'étant pas le § 5. R-473 à R-478
  rendus fidèlement : citations exactes (R-473 ; R-478, identique, aux espaces près, à la ligne GO-2026-10-26-01 et au
  complément de passation), résumés fidèles (R-474 à R-477), heures du registre (« vers 01:19 », 01:24, « vers 01:32 »,
  01:53, « vers 01:58 » UTC). Heures : 02:32, 02:34, 02:42 Paris = 01:32, 01:34, 01:42 UTC, cohérentes avec le message
  n° 59 (versement, 01:28:27 UTC), la lecture de « neuron-explorer » (vers 01:34 UTC) et la passation (écrite à partir de
  01:51 UTC) ; R-473 (vers 01:19 UTC) vient après 01:56 Paris (00:56 UTC) et R-472 (01:11 UTC), avant le message n° 58
  (01:22:05 UTC), qui la confirme en son point 1.
- **Liste v8** (tâche 3 bis). Format « empreinte, deux espaces, nom » sur ses 646 lignes ; aucun nom interdit ;
  **646 sur 646 justes** ; aucune entrée de la v7 ôtée ni changée ; aucun nom en double ; 25 entrées nouvelles,
  exactement : la liste v7 et son compagnon, `contre-lecture-6-v1/` (15), le relevé v6 et son compagnon,
  `traitement-cl6-v1/` (6). Elle couvre tout le premier niveau du dossier des pièces et les dossiers nommés, sauf
  elle-même, son compagnon et `contre-lecture-7-v1/` (créé à 03:18:11 Paris, après elle, 03:17:09). Le § Pièces le dit
  (l. 462–467).
- **Rien d'autre ne change** (tâche 4) que ce que disent le statut et le § Contre-lecture, aux deux passages près de
  P4C7-05 (a). Inchangés depuis la version relue par la contre-lecture 6 : titre ; texte différentiel ; § Décisions hors
  l'en-tête, 00:54, 01:48, 01:56 et l'ajout de 02:32 ; table hors une ligne ; § Objet hors canal (d) ; § Plan points 1, 2, 4 et 5 ;
  liste d'arrêt ; essais ; § Pièces hors une phrase ; contre-lectures 1 à 5 hors quatre éléments du traitement de la 5.
- **Scellement** (tâche 5). Une seule ligne qui porte la mention d'entropie (l. 329), sans nombre ; deux lignes de graine
  (l. 334–335), celles des marqueurs ; les quatre marqueurs de scellement (entropie, graine de la v5.3, graine de la v6.x,
  empreinte des pièces) une fois chacun, aucun autre ; aucun marqueur de rédaction à doubles crochets ; l'empreinte du
  lanceur v10 citée. La ligne de GO et les trois lignes de dépense sont identiques, octet pour octet, à celles de la version
  relue par la contre-lecture 6 (une occurrence chacune) ; les § Plan points 1 et 2, la liste d'arrêt, les essais et le
  § Objet jusqu'au canal (d) aussi (`diff` vide). Ce rapport ne porte ni mention d'entropie suivie d'un signe égal, ni ligne
  de graine, ni marqueur ; son nom suit le motif que le script compte (`-cl[0-9]+\.md`) ; son compagnon est au format que
  le script lit.

## L'écart : passages modifiés (tâche 4)

Numéros de lignes de la version à sceller.

| passage (lignes) | changement | raison annoncée |
|---|---|---|
| statut (8–12) | correction à partir de 02:08 UTC par l'instance nouvelle ; « confirmée … R-473 » | P4C6-04 ; statut |
| statut (19–21) | contre-lecture 6 (`35fe0067…`, traitée) et 7 | § Contre-lecture |
| ce qui a été lu (47–52) | lectures de l'instance nouvelle (passations, R-473 à R-478, GO-2026-10-26-01, messages n° 57 à 60, état, rapport 6) | R1 ; non nommé (P4C7-05 a) |
| décisions, en-tête (60–61) | relevé v6 | P4C6-04 |
| décisions, 00:54 (93–96) | « taille fixée par le texte de (b) » | P4C6-03 |
| décisions, 01:48 (106–108) | hypothèses de (b) écrites et poussées avant lecture | P4C6-03 |
| décisions, 01:56 (119–124) | hypothèses de (b) ; levée dite à session-depot (R-473) | P4C6-03, P4C6-04 |
| décisions, 02:32–02:42 (150–156) | puce ajoutée | relevé v6 (voir P4C7-04) |
| table (190) | ce que le point 3 remplace et garde | P4C6-02 |
| tout le reste (202–204) | « critères gelés (sauf ce que lève le point 4 bis) » | P4C6-01 |
| objet, canal (d) (305–306) | « d'une course pendant qu'elle tourne » | P4C6-02 |
| plan, point 3 (336–361) | en-tête ; moment ; R-473 ; hypothèses de (b) ; pièces servies ; agents | P4C6-01 à 06 |
| plan, point 4 bis (365–394) | choix (a) à (e) ; comptes et exécution ; levée | P4C6-01, P4C6-05 |
| pièces (462–467) | relevés v1 à v6 ; listes v1 à v8 ; contre-lectures 5 à 7 | § Pièces |
| contre-lecture 5 (500–501, 505, 510, 514–515) | quatre descriptions | P4C6-07 |
| contre-lecture 6 et 7 (518–570) | détail et traitement de la 6 ; paragraphe de la 7 | § Contre-lecture |
| ce texte scellé (572–576) | « et les corrections qu'il demande, aux passages qu'il nomme » | P4C6-08 (b) |
