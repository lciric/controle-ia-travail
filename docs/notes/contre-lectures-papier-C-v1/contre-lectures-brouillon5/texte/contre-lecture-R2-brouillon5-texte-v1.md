# Contre-lecture R2 du brouillon 5 du préenregistrement du papier C — lentille « texte et conformité » — v1

- **Qui** : sous-agent neuf, lancé par la session le 2026-10-20. Je n'ai écrit ni le brouillon 5, ni les brouillons
  1 à 4, ni leurs configurations, ni la table de traitement, ni aucune contre-lecture ou note de lecture.
- **Heures** : de 23:19 à 23:45 UTC environ, le 2026-10-20.
- **Consigne suivie** : `…/consignes-contre-lectures-brouillon5-v1.md` (`148299974a2a3925…`, sans compagnon), section
  « Commun aux trois » et lentille 2 seulement. Préfixe `…/` =
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C` ; `R` = dépôt
  `/home/user/controle-ia-travail`, lu en lecture seule.
- **Pièces lues, empreintes recalculées, toutes égales à leur compagnon** :
  - texte relu : `…/brouillon5/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`
    (`9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969`) ; copie de `R/brouillons/` identique ;
  - configuration : `…/brouillon5/papier-C-config-v1-brouillon2.json`
    (`77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb`) ; copie de `R/brouillons/` identique ;
  - table de traitement du rédacteur : `…/brouillon5/table-traitement-brouillon5-v1.md` (`ebb763fadd96bc10…`) ;
  - traitement de la session : `…/traitement-contre-lectures-brouillon4-papier-C-v1.md` (`f2c6a3604adfce29…`) ;
    consigne du rédacteur (`5da5939a636bc1a9…`) ; points ouverts du brouillon 4 (`babe4b4d64d697b8…`) ;
  - les six rapports traités : méthode (`0f1cf812…`), texte (`08618f6b…`), Panin (`6b350e99…`), voisins
    (`09f14364…`), note Panin (`c06488a5…`), note voisins (`2c720d22…`) ;
  - brouillon 4 (`40bf1d4f…`) et configuration brouillon 1 (`348379fb…`), pour les différences ;
  - notes finales : `…/brouillon5/notes/lecture-voisin-panin-v1.md` (`8781d6a7…`) et
    `lecture-voisins-HC1-bajaj-silent-judge-v1.md` (`a98ddc75…`) ;
  - outils du rédacteur : journal de `ecrire_config_brouillon2_v1` (`4cdda1a2…`), sortie de `verifier_kendall_C_P3_v1`
    (`18961a7c…`) ; sortie S6 de la lentille méthode (`06fdca31…`) ;
  - dans `R` : décisions N-005 et N-006 (`cd49afbc…`), N-013 (`157d388e…`), N-023 (`1297f509…`) ; `registres/go.md`, lignes
    GO-2026-10-17-01, GO-2026-10-20-06, GO-2026-10-20-07, GO-2026-10-20-09 ; `registres/decisions.md`, lignes P-019,
    P-020, R-294, R-295, R-301 ; `registres/etat.md` (`b8733d24…`), lignes du papier C ; `src/controle_ia/prereg.py`
    (`3b2e3ee5…`) ; `prereg/gabarit-preregistrement-v1.md` (`8cad4371…`) ; brouillon 3 (`3cc25dcd…`), section
    « Hypothèse » ; `donnees/t05-pilote-v1/taches-pilote-60-v1.json` (`287e8348…`) : clés et comptes seulement ; six
    pages de PDF de `R/docs/sources/pdf/` pour des citations (section « Vérifications »).
- **Ce que j'ai tenu** : écriture seulement sous `…/contre-lectures-brouillon5/texte/` ; aucune commande git ; Python
  lancé avec `-B` (et `-I`) ; aucune recherche récursive dans le dépôt ; aucun sous-agent ; aucune dépense, aucun outil de
  location, aucun appel à Gemini ; aucune clé lue ni affichée ; aucun texte de tâche, d'item ni de gabarit affiché.
  Je n'ai pas utilisé les fichiers trouvés dans `…/contre-lectures-brouillon5/outils-texte/` (auteur inconnu de moi).
- **Écart à mes règles, déclaré** : mon script d'empreintes (`empreintes_citees_b5_v1.py`) a ouvert en binaire, pour en
  calculer le sha256, trois fichiers interdits (`R/prereg/P3-consignes-v1.md`, `items-textes-p1-v1.json`,
  `prompts-p1-v1.json`) et le fichier source des 64 tâches, que le texte ne cite pas par empreinte. Rien de leur contenu
  n'a été affiché ni gardé ; seules des empreintes figurent dans `empreintes_citees_b5_v1.txt`. Pour le fichier source,
  j'ai ensuite seulement comparé, sans l'afficher, son sha256 au champ `source.sha256` du fichier des 60 tâches.
- **Outils et sorties** (même dossier, compagnons dans `sha256sums-texte-v1.txt`) : `empreintes_citees_b5_v1.py` et sa
  sortie ; `mots_exacts_b5_v1.py`, `phrases_mots_exacts_v1.tsv` et sa sortie (79 corrections en mots exacts
  retrouvées) ; `phrases_nouvelles_b5_v1.py` et sa sortie ; extractions des annexes des deux rapports de notes ;
  `pdf-texte/` (pages extraites par `pdftotext`).

## Verdict

**Scellable après corrections.**
- Aucun constat critique. Les énoncés de HC1, HC2, HC2b et HC3 et les pièces revendiquées sont égaux au brouillon 3 et à
  N-005, N-013, N-023 ; « Where Empathy Goes Wrong » reste cité comme publié ; les tâches suivent GO-2026-10-20-09.
- Les 93 constats dits appliqués le sont, en mots exacts quand le traitement le demande ; les 2 écartés le sont à bon droit.
- Trois majeurs bloquent : la liste des différences admises de la configuration ne permet pas d'écrire les décisions
  P-019 et P-020 (constat 1) ; des pièces citées ne sont pas dans le dépôt (constat 3) ; C-P4b se lit sur une lecture
  que le texte déclare ailleurs « rapportée, sans verdict », sans réserve pour l'artefact d'agrégation (constat 6).
- Points ouverts du rédacteur : le versement et C-P4b bloquent ; le tirage des tâches de l'étape 2 demande une phrase ;
  les règles du pilote sans regroupement par tâche ne faussent aucun test décisif (correction recommandée).
- Restent aussi, hors de ce rapport : décisions P-019 et P-020, contre-lecture méthode, lecture des voisins (verrou 2),
  module et sa contre-lecture, mesures v2, note du vivier.

## Constats

### 1 — majeur — les décisions P-019 et P-020 ne peuvent pas entrer dans la configuration scellée

- **Où** : champs du scellement, l. 97-99 ; P-020, repli, l. 649-650 ; configuration, champs `statut`,
  `stabilite_rang`, `agent_bras.decision_bras_usurpation`.
- **Ce qui est** : le texte dit que les seules différences entre la configuration scellée et le brouillon 2 sont
  `version`, `statut`, `graines.racine`, `juges[].revision` et `partage_taches.sha256_source`. Or la configuration porte
  « P-019 en attente » (`stabilite_rang.decision`), les deux lectures (`lecture_recommandee` et `repli_si_refus`) et
  « P-020 en attente » (`agent_bras.decision_bras_usurpation`). Le repli de P-020 dit « champ `agent_bras.usurpation`
  retiré de la configuration scellée ». Si Lazar refuse P-020, ou P-019, la règle des différences admises est violée ;
  si on la respecte, la configuration scellée garde une lecture que le texte a retirée.
- **Ce qui devrait être** : les champs de décision font partie des différences admises.
- **Correction (mots exacts)** : l. 97-99, remplacer « sont les champs `version`, `statut`, `graines.racine`,
  `juges[].revision` et `partage_taches.sha256_source` remplis ; » par « sont les champs `version`, `statut`,
  `graines.racine`, `juges[].revision` et `partage_taches.sha256_source` remplis, et les deux champs de décision mis à
  l'état de la décision : `stabilite_rang` (`decision` écrite ; seule la lecture retenue reste, `lecture_recommandee` ou
  `repli_si_refus`) et `agent_bras` (`decision_bras_usurpation` écrite ; `usurpation` retiré si P-020 est refusée) ; ».
  Même phrase dans le champ `statut` de la configuration.

### 2 — mineur — le validateur ne voit pas les blocs de décision en attente

- **Où** : l. 308, 321 (P-019, prédiction) ; l. 820, 828 (P-019, critères) ; l. 638, 646 (P-020) ; verrou 1, l. 65-66.
- **Ce qui est** : les en-têtes « **[Décision de Lazar en attente …]** » et « **[Version de repli …]** » ne sont pas des
  marqueurs `<<…>>` ; `problemes` ne les voit pas (`GABARIT = <<[A-Z0-9_]+>>`, `prereg.py`, l. 27). Un texte scellé qui
  garderait les deux versions passerait le validateur. Seul le bloc recommandé de P-020 contient un marqueur.
- **Ce qui devrait être** : une garde mécanique (R5 : aucun repli silencieux), symétrique pour les six en-têtes.
- **Correction (mots exacts)** : ajouter `<<TRANCHER_P019>>` après chacun des quatre en-têtes de P-019 (l. 308, 321, 820,
  828) et `<<TRANCHER_P020>>` après les deux en-têtes de P-020 (l. 638, 646). Verrou 1, ajouter : « Les en-têtes entre
  crochets et les marqueurs `<<TRANCHER_P019>>` et `<<TRANCHER_P020>>` sont retirés avec la version écartée ; tant qu'il
  en reste un, `problemes` refuse le scellement. »

### 3 — majeur — pièces citées absentes du dépôt ; verrou 5 incomplet (point ouvert « versement des rapports »)

- **Où** : historique, l. 14-19 ; verrou 5, l. 81-85 ; pièces de contre-lecture, l. 192-217 ; contre-lecture, l. 906-932.
- **Ce qui est** (vérifié sur disque, R11) :
  - `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon4.md` (`40bf1d4f…`) n'existe pas dans `R/brouillons/`,
    alors que les brouillons 1, 2, 3 et 5 y sont ; le brouillon 1 de la configuration (`348379fb…`) non plus ;
  - le traitement de la session (l. 17) et la table de traitement (l. 18-19, « versée avec ce brouillon ») n'ont aucun
    chemin dans le dépôt ; la table n'a pas d'empreinte au texte (R6) ; elle n'est pas dans `R/brouillons/` ;
  - `docs/notes/contre-lectures-papier-C-v1/`, `docs/notes/papier-C-mesures-v1/` et `docs/procedures/papier-C-v1/`
    n'existent pas encore ;
  - `problemes` contrôle la présence de deux empreintes par contre-lecture, jamais l'existence des fichiers.
- **Ce qui devrait être** : chaque chemin cité avec une empreinte existe dans le dépôt au scellement, avec cette empreinte.
- **Correction (mots exacts)** : l. 17, écrire « `docs/notes/contre-lectures-papier-C-v1/traitement-contre-lectures-brouillon4-papier-C-v1.md` » ;
  l. 18-19, remplacer « `table-traitement-brouillon5-v1.md`, versée avec ce brouillon (compagnon `.sha256`) » par
  « `docs/notes/contre-lectures-papier-C-v1/table-traitement-brouillon5-v1.md`
  (`ebb763fadd96bc108ba803e737eba55b797b71c7517f94dbca41bfe1f84dea56`) ». Verrou 5, ajouter : « brouillon 4 du texte
  (`40bf1d4f…`) et brouillon 1 de la configuration (`348379fb…`) sous `brouillons/`, avec leurs compagnons ; traitement
  de la session (`f2c6a360…`), table de traitement du brouillon 5 (`ebb763fa…`) et rapports des contre-lectures de ce
  brouillon sous `docs/notes/contre-lectures-papier-C-v1/`. Au scellement, un script vérifie que chaque chemin cité avec
  une empreinte existe dans le dépôt et lui est égal ; un écart : pas de scellement. »

### 4 — mineur — contrôles exigés avant le scellement sans marqueur ni entrée

- **Où** : verrou 2, l. 67-75 ; verrou 6, l. 86-88 ; section « Contre-lecture », l. 934-942.
- **Ce qui est** : la lecture des voisins de la bibliographie de Panin (Joswin et al. 2607.00415 ; Hu et Qu 2607.05545 ;
  puis la liste de la note finale et les deux voisins de Bajaj et Tiganj) et la contre-lecture du module et de la
  configuration sont exigées avant le scellement, mais n'ont ni marqueur ni entrée « Contre-lecture k ». Le validateur
  ne bloque pas si elles manquent.
- **Correction (mots exacts)** : verrou 2, ajouter : « Note de ce contrôle : `<<CHEMIN_NOTE_VOISINS_BIBLIO>>`
  (`<<EMPREINTE_NOTE_VOISINS_BIBLIO>>`), verdict par papier ; une collision, même partielle : nœud de Lazar avant le
  scellement. » Section « Contre-lecture », après la contre-lecture 6, ajouter : « - **Contre-lecture 7** — module et
  configuration (verrou 6) : configuration relue `<<EMPREINTE_CONFIG>>`, lignes « Module du papier C » ; rapport
  `<<CHEMIN_RAPPORT_CL7>>` (`<<EMPREINTE_RAPPORT_CL7>>`) ; traitement de chaque remarque. »

### 5 — mineur — « toutes les statistiques des juges » sur la loi nette : faux pour C-P5 et C-P3c ; C-P3c sous-défini

- **Où** : l. 30, l. 290, l. 805 ; C-P3c, l. 316 ; TC.2, l. 668-669 ; configuration `stabilite_rang.C_P3c`.
- **Ce qui est** : l. 290 « Toutes les statistiques des juges qui portent un verdict se lisent sur la loi nette du
  témoin ». L'alarme (C-P5, point 15) et les deux gains d'écart des juges de C-P3c (point 13) ne sont pas des lois
  nettes. C-P3c ne dit pas si le gain d'écart des juges est brut ou en différence des différences, ni sous quelle
  consigne (TC.2 ne le dit pas) ; les rangs peuvent changer de l'un à l'autre : choix non gelé.
- **Correction (mots exacts)** : l. 290, remplacer la phrase par « Les statistiques des juges tirées de TC.1 (Ḡ, λ,
  structure, C-P1b, C-P3a, C-P3b, intensités graduées, C-P6 juges, contrôle de manipulation) se lisent sur la **loi
  nette du témoin** (Métrique, point 8 bis) ; les gains d'écart des juges (TC.2, TC.3 b) et l'alarme (C-P5) suivent
  les points 13 et 15. » Même phrase à la l. 805. L. 316 : « gain d'écart brut des juges sous le plaidoyer de l'agent
  (TC.2 ; consigne A, mode direct), gain d'écart brut des juges sous l'usurpation de l'agent (TC.3 b ; même lecture) ».
  Même précision dans `stabilite_rang.C_P3c`.

### 6 — majeur — C-P4b : lecture contraire au reste du texte, D₀ non défini, artefact d'agrégation non déclaré (point ouvert « C-P4b »)

- **Où** : C-P4b, l. 299, l. 495, l. 816 ; point 13, l. 430-431 ; TC.2 (3), l. 677-678 ; réserve 6, l. 748-751 ; A8,
  l. 798-800 ; table de traitement, CR-methode-05 (« point non tranché »).
- **Ce qui est** : C-P4b porte un verdict sur d = g_lecteur − g_auteur « paragraphe compris », donc sur la lecture
  complète. Or le point 13 lit D₀ et g de l'auteur « sur les seuls champs de l'action » et TC.2 (3) dit la lecture
  complète « rapportée, sans verdict ». Le D₀ de C-P4b n'est pas défini. Sur la lecture complète, sous le maximum, la
  lentille méthode trouve g brut médian −0,30 côté auteur sans aucun signal (S6, `06fdca31…`, lignes « maximum N1
  complete ») ; si le côté lecteur ne bouge pas de la même quantité, d > 0 sort sans signal : un faux « confirmé » dans
  le sens revendiqué (R3, R4). Côté lecteur, les champs seuls n'ont pas de sens : dans un modèle causal, les jetons des
  champs précèdent le paragraphe et ne le voient pas. La lecture complète doit donc rester, mais déclarée.
- **Ce qui devrait être** : exception écrite, D₀ défini, réserve symétrique ; décision de la session, sur avis de la
  lentille méthode, avant le scellement.
- **Correction (mots exacts)** : l. 299, colonne « grandeur » : « d = g_lecteur − g_auteur, sur la lecture complète des
  deux côtés (même sonde, même contenu, mêmes jetons lus, paragraphe compris ; D₀ de chaque côté sur cette même lecture ;
  exception déclarée au point 13 et à TC.2 (3) ; le lecteur est Llama-3.1-8B-Instruct dans la consigne du juge) ».
  Réserve 6, ajouter : « Elle vaut aussi pour C-P4b, lu sur la lecture complète des deux côtés : l'agrégation déplace
  g_auteur sans signal de manipulation (S6 : g brut médian −0,30 sous le maximum, lecture complète) et peut ne pas
  déplacer g_lecteur de la même quantité ; toute ligne C-P4b « confirmée » porte la réserve « effet d'agrégation possible
  sur d ». » La lentille méthode dit avant le scellement si un contrôle mécanique (par exemple l'excédent à longueur fixe
  des deux côtés) remplace cette réserve.

### 7 — mineur — règles du pilote sans regroupement par tâche (point ouvert)

- **Où** : point 18, l. 458-459 ; plan 2, l. 594-596 et l. 607-611 ; configuration `derivation.demi_largeur_lambda`.
- **Ce qui est** : depuis R-294, le lot de calibrage compte 16 tâches et l'unité d'indépendance est la tâche (point 11).
  Mais l'erreur type des gains du vivier se tire « par rééchantillonnage des contenus de calibrage », et la validation
  croisée de la demi-largeur de λ coupe « une moitié des contenus » : les deux moitiés partagent des tâches. Les erreurs
  types sortent trop petites : k_max trop grand, demi-largeur trop petite, effectif n trop petit, réserve « niveaux non
  séparables » trop rare. Aucun test décisif n'est faussé (l'étape 2 rééchantillonne par tâches) ; seuls le dessin et la
  puissance le sont.
- **Correction (mots exacts)**, à confirmer par la lentille méthode : point 18, remplacer « erreur type par
  rééchantillonnage des contenus de calibrage (2 000 tirages) » par « erreur type par rééchantillonnage des tâches du lot
  de calibrage, chaque tâche portant ses contenus (grappes ; 2 000 tirages) » ; plan 2, remplacer « formulations choisies
  sur une moitié des contenus de calibrage (tirage par la clé `papier-C/pilote/conception`), loi nette et erreur type de
  λ calculées sur l'autre moitié » par « formulations choisies sur les contenus de huit tâches du lot de calibrage (tirage
  des tâches par la clé `papier-C/pilote/conception`), loi nette et erreur type de λ calculées sur les contenus des huit
  autres tâches (rééchantillonnage par tâches) ». Même texte dans la configuration. La mise à l'échelle √((n_cal / 2) / n)
  est à revoir par la même lentille.

### 8 — mineur — tirage des tâches de l'étape 2 incomplet (point ouvert)

- **Où** : plan 0, l. 529-530 ; modérateur raisonné, l. 698-699.
- **Ce qui est** : « n/2 tâches tirées du bassin (clé `papier-C/etape2/taches`) » ne dit ni « sans remise », ni
  « uniforme », ni l'ordre du bassin avant le tirage (indispensable pour rejouer la graine), ni si l'origine des tâches
  (partage, extraction neuve) compte. Les 20 tâches du mode raisonné sont « tirées » sans dire dans quel ensemble.
- **Correction (mots exacts)** : l. 529, « À l'étape 2 : n/2 tâches tirées sans remise, uniformément, dans le bassin
  complet à son ouverture (liste triée par identifiant, écrite au manifeste de l'étape 2 avant le tirage), clé
  `papier-C/etape2/taches` ; » ; l. 698, « 20 tâches tirées sans remise parmi les n/2 tâches de l'étape 2 (clé
  `papier-C/etape2/raisonne`) ». Si la session veut garder la proportion des deux origines, elle l'écrit ici à la place
  (tirage stratifié par origine).

### 9 — mineur — « des tâches neuves » : inexact depuis le partage

- **Où** : rappel du brouillon 4, l. 52-53.
- **Ce qui est** : « étape 2 décisive, sur des contenus, des tâches et des graines neufs ». Les 44 tâches du bassin venues
  du pilote de T0.5 ont déjà servi au pilote de T0.5 et à P3 (réserve 12, l. 765-767).
- **Correction (mots exacts)** : « étape 2 décisive, sur des contenus et des graines neufs, et des tâches disjointes du
  calibrage (44 d'entre elles déjà vues par le pilote de T0.5 et par P3 : réserve 12) ».

### 10 — forme — empreintes à compléter (R6)

- l. 180 et l. 524 : `docs/procedures/T0.5-extraction-v1.md` sans empreinte ; écrire
  « (`d23bd62fe1611b8737ccb38a404d96a41746158a7930bef0a065590bd072c26c`) » (recalculée, égale au compagnon).
- l. 149-152 : « lot 2 C1a, C1b, … lot 3 Cb, Cc, Cd, Be (repris du brouillon 3) » sans empreintes (déjà ainsi au
  brouillon 3) ; écrire une empreinte abrégée par rapport, recopiée des compagnons.
- l. 110-111 : `<<EMPREINTE_TACHES_SOURCE_64>>` peut se remplir dès maintenant : le fichier scellé des 60 tâches
  (`287e8348…`) porte le champ `source.sha256`, égal au sha256 du fichier source (comparé par script, sans affichage).
  Écrire l'empreinte et « égale au champ `source.sha256` du fichier des 60 tâches ».
- l. 124 et l. 145-146 : les « états lus » de `registres/go.md` (`0ede5bed…`) et de `registres/decisions.md`
  (`6d033ecf…`) ne se recalculent plus (les deux fichiers ont grandi pendant ma lecture). Au scellement : citer les
  lignes au commit du scellement, ou recalculer.

### 11 — forme — accords entre texte et configuration, et libellés

- l. 418-419 : « accélération par jackknife sur les tâches » ; la configuration dit « sur les blocs (tâches du corpus A,
  items du corpus B) ». Écrire « accélération par jackknife sur les grappes (tâches du corpus A, items du corpus B) ».
- Configuration : `pilote.usd_max_par_lancement = 10` à côté de `borne_lancement` « strictement sous 10 USD ». Renommer
  le premier `usd_borne_stricte_par_lancement` ou préciser « exclu ».
- l. 913, 918, 923, 928 : « constats appliqués, sauf 02 (R-294), 04 (P-019) … » ; la table compte ces constats comme
  appliqués sous décision. Écrire, par exemple pour la l. 918 : « constats appliqués ; 02 sous R-294, 04 et 05 sous
  marqueur (P-019, P-020) ; 17 écarté dans sa forme propre (forme de CR-panin-01 retenue) ».
- l. 639-641 : deux deux-points de suite (« … confiance ≈ 65 %) : Proposition soumise à Lazar (…) : un bras … ») ;
  écrire « … confiance ≈ 65 %). Proposition soumise à Lazar (…) : un bras … ».

### 12 — information — bilan des 95 constats

- 95 constats (19 + 23 + 11 + 13 + 14 + 15), égal aux six rapports. 93 appliqués : 79 corrections en mots exacts
  retrouvées par script (`mots_exacts_b5_v1.txt` ; les 3 « absentes » diffèrent d'une majuscule, d'un gras ou d'une
  ponctuation) ; les autres vérifiées à la lecture. Les écarts déclarés par la table sont tous justifiés par une ligne du
  traitement de la session (loi nette pour CR-panin-01 ; décision de Lazar R-294 ; banc 1.3 à 1.5 ; A7 devenu A8).
- Notes finales : différence avec les annexes des deux rapports limitée aux écarts déclarés (chemins, empreintes,
  phrase de CN-03, marqueurs remplacés) ; CN-panin-01 à 14 et CN-01 à 15 présents.
- Les 2 écartés le sont à bon droit : le traitement de la session (ligne « CR-panin-01, CR-voisins-02, CR-texte-17 »)
  retient la forme de CR-panin-01 ; l'objet de CR-texte-17 (lecture ambiguë pour un juge) et celui de CR-voisins-02
  (aucun juge retiré ni remplacé sur ce motif) sont couverts (plan 1.2, l. 560-564 ; liste d'arrêt 4, l. 872-874).
- Famille 4 : le traitement dit « formulations 5 à 16 », le rapport CR-texte-09 vise les formulations 15 et 16 ; le texte
  suit le rapport. Configuration vérifiée : les deux phrases sont retirées (68 et 113 caractères), longueurs 429 → 361 et
  577 → 464 (corpus A), gardes rejouées.

### 13 — information — conformité aux décisions

- Énoncés de HC1, HC2, HC2b, HC3 : égaux au brouillon 3 (différence de la section « Hypothèse ») ; seules changent les
  listes de précédents (instrument, voisins, Venkatesh reformulé selon CR-voisins-08, HC3 composante 2). Pièces
  revendiquées égales à N-013 § 1 et N-023 § 1. Aucune modification d'énoncé.
- N-023 : Venkatesh et al. cité comme publié (PDF `59f4b700…`, figure 1 p. 3, figure 2 p. 4), aucun énoncé changé.
- GO-2026-10-20-09 : partage 16 / 48, clé `partage-taches-papier-C`, extraction neuve avant l'étape 2, sans dépense.
  « Partage écrit tout de suite » se lit « règle écrite au brouillon 5, tirage à l'entropie du scellement », comme
  l'exige R-294 (« dérivée de l'entropie du préenregistrement ») : conforme.
- GO-2026-10-17-01, -10-20-06, -10-20-07 : cités juste ; borne du lanceur plus stricte que la délégation (déclarée).

### 14 — information — sortie de `problemes`

- Sortie identique à celle du rédacteur (`problemes-brouillon5-v1.txt`) : contre-lectures 5 et 6 sans empreintes, et
  22 marqueurs. Tous attendus au scellement ou au versement : entropie, révisions, configuration, commit, module (deux),
  décisions (trois), contre-lectures 5 et 6 (six), mesures v2, note du vivier, propositions du pilote de T0.5 (deux),
  source des 64 tâches (remplissable dès maintenant, constat 10). Manquent ceux des constats 2 et 4.

### 15 — information — P-019 et P-020

- Marqueurs, dates de défaut (2026-10-22 vers 21:15 UTC), versions recommandées et replis conformes aux lignes P-019 et
  P-020 de `registres/decisions.md`. Ces lignes disent encore « à transmettre à Lazar » ; `registres/etat.md` les dit
  transmises. La session met la colonne à jour avec l'heure de transmission : le délai de 48 heures en part.
- La version recommandée de P-019 retire la réfutation d'une prédiction listée par N-005 (prédiction 3) ; le texte le dit
  (colonne « réfutation ») et Lazar en est saisi par P-019. Aucun énoncé ne change : pas de nœud de revendication.

### 16 — information — vérifications de pages (R7)

- Lues sur PDF, à la page citée : Panin p. 11 (« a deference screen must not threshold the outcome ») et p. 6
  (« relabelled adoption ») ; 2608.25869v1 p. 6 (« approximately zero ») et p. 7 (0.267) ; 2606.14037v1 p. 4 (« weak,
  medium ») ; 2602.13568v1 p. 3 (« log-probabilities », en mode brut) et p. 2 (k ∈ {1, 3, 5, 9}) ; 2509.26072v2 p. 1
  (« Reliable ML ») ; Venkatesh p. 3 (figure 1) et p. 4 (figure 2). Nombres du texte tirés des simulations ou des
  mesures : tous renvoyés à un fichier et une empreinte, recalculées (y compris W exact : 0,0394 ; 0,0417 ; 0,0278 ;
  0,6327).

## Points ouverts du rédacteur : lesquels bloquent

| point | bloque le scellement ? | constat |
|---|---|---|
| versement des rapports (et du brouillon 4, de la configuration brouillon 1, du traitement, de la table) | oui | 3 |
| C-P4b sur la lecture complète | oui, tant que l'exception, D₀ et la réserve ne sont pas écrits | 6 |
| règles sans regroupement par tâche (pilote) | non pour la validité des tests ; correction recommandée avant le scellement, car gelée ensuite | 7 |
| tirage des tâches de l'étape 2 | une phrase à ajouter avant le scellement ; rien de plus | 8 |

## Compte

Critique 0 ; majeur 3 ; mineur 6 ; forme 2 ; information 5.
