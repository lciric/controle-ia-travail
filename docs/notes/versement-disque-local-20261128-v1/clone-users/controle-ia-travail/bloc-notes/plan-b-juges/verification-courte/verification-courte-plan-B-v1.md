# Vérification courte du brouillon 2 — préenregistrement du plan B des juges de T0.5 (rubrique RS1) — v1

**Jugement d'ensemble (détail en fin de rapport) : prêt après corrections.** Aucun constat bloquant ; 3 majeurs, 7 mineurs, 8 pour information. Les 15 constats de la contre-lecture sont traités, PB-04 en partie (VC-01).

Vérificateur : sous-agent neuf (R2). Je n'ai écrit ni le préenregistrement, ni sa contre-lecture, ni son traitement, ni le pilote, ni ses notations. Lecture seule : aucune écriture dans le dépôt ni dans un registre, aucun commit, aucune commande Vast.ai, aucun réseau. Aucun texte de réponse de juge ni d'action n'a été lu : seulement des comptes, des longueurs, des drapeaux et des durées.

## 1. Empreintes vérifiées

| fichier | sha256 | résultat |
|---|---|---|
| `consigne-verification-courte-plan-B-v1.txt` | `433644d049e1c0206f99f5f1e62692c3f245429e5017b898e6486cc6937577c6` | conforme |
| `T0.5-plan-B-juges-v1-brouillon2.md` | `fa725591468811d1acd6f6f6779f9f7a2bf149ee437d220f28ef8bdd236c38fb` | conforme |
| `traitement-contre-lecture-v1.md` | `1875d7b821670da5b4e2561a643a4813e49eb6367230d010687cce2e17287fe8` | conforme |
| `contre-lecture-plan-B-v1.md` | `09d249f2478944fb26449731bbf9b5f50dedff30ebf859c5954ca00b59eb17c4` | conforme |
| `T0.5-plan-B-juges-v1-brouillon1.md` | `a4751424cfdb4f6dfeb1e22bba06258bd6ecc0210062d00b31ead419388fd29e` | conforme |
| `notes-de-conception-v1.md` | `76c65f1078bfc3866699ed837b5ae593adec9bb5d55f14973e89328909e9b709` | conforme |
| `travail/S1-brouillon1.txt` | `b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7` | conforme ; annexe A identique, octet pour octet, à cette copie et à l'annexe A du brouillon 1 ; 3 965 caractères, une seule fin de ligne finale |

Dépôt :
- Clone jetable de `/home/user/controle-ia-travail`, branche `main`, tête `f303ba9` (postérieure à `3d0e246`, citée par le brouillon 2). Le dépôt original n'a pas bougé : tête `f303ba9`, arbre propre.
- Commits cités, tous présents : `ffdbcda`, `3d0e246`, `c63d4f1c073f3b6146729dae0086cd7205cdfa57`, `2660b07`, `1030eb8`, `03cb538`.
- Les 29 couples « chemin, empreinte » cités par le brouillon 2 : 28 égaux à la tête. `registres/decisions.md` égale `8014b859…` au commit `ffdbcda` (comme le dit le texte), mais vaut `1f31df57ad6a843c8ad83c703818e0a1efe441ed6b28ba85c834dc46140a87bc` à la tête : R-219 et R-220 ont été ajoutées après le brouillon 2 ; les lignes citées (l. 349 à 354) sont inchangées (VC-11).
- Modules gelés (14 fichiers, dont `invites.py` et `run_harnais_factice.py`) : aucun changement de `c63d4f1` à la tête (`git diff` vide). De `2660b07` à `c63d4f1`, seuls `noter_pilote_a.py` et `lire_notations_pilote.py` s'ajoutent (verdict complémentaire, section 2.3).
- Validateur du dépôt `prereg.problemes` : aucun problème sur le brouillon 2 (le brouillon 1 n'avait que le manque attendu de la section « Contre-lecture »).
- Règle du plan B citée au « Seuil » : identique, mot pour mot, à `prereg/T0.5-pilote-8B-v1.md` l. 129-132 (`diff` vide).

Fichiers de cette vérification, dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/plan-b-juges/verification-courte/` :
- `scripts/comptes_numeriques.py` (`841a4c42…`), sortie `sortie-comptes-numeriques.txt` (`7e38c10e…`) ;
- `scripts/essai_lire_une_note.py` (`bae5cd0d…`), sortie `sortie-essai-lire-une-note.txt` (`4e16bda0…`) ;
- `empreintes-b2.txt` (`ff08e8db…`), `diff-b1-b2.txt` (`7fa593d8…`), `wdiff-b1-b2.txt` (`edb1401f…`) ;
- `depot/` : clone jetable.

Commandes citées dans les tableaux :
- K1 : `sha256sum` sur les fichiers ci-dessus.
- K2 : `git diff --stat c63d4f1 f303ba9 -- <14 modules gelés>` (vide).
- K3 : `git show <commit>:registres/<fichier> | sha256sum` aux commits `1030eb8`, `ffdbcda`, `3d0e246`, `f303ba9` ; `git diff --name-only ffdbcda 3d0e246`.
- K4 : contrôle des 29 empreintes citées (`empreintes-b2.txt`).
- K5 : `scripts/comptes_numeriques.py` sur les notations H.4 scellées (champs `jetons_contexte`, `jetons_reponse`, `tronquee` seulement) et queues binomiales.
- K6 : `scripts/essai_lire_une_note.py` (fonction gelée `lire_une_note`, valeurs écrites à la main).
- K7 : comparaison de l'annexe A (deux brouillons et copie de travail).
- K8 : `prereg.problemes` sur les deux brouillons.
- K9 : `diff` de la règle du plan B.
- K10 : `du -sh contre-lecture/*`.
- K11 : `diff -u` et diff mot à mot des deux brouillons.

## 2. Constats, du plus grave au moins grave

| id | section et ligne (brouillon 2) | ce qui est écrit | ce qui est juste, et pourquoi | gravité | correction proposée |
|---|---|---|---|---|---|
| VC-01 | « Métrique », couverture (l. 128) ; « Seuil », couverture (l. 163) ; table C, lignes « couverture » (l. 354-355) ; configuration `couverture_quantile` (l. 304) ; liste d'arrêt (l. 410, l. 413) | « au moins une rangée comparée du palier du chemin dont la zone générée atteint le 75e centile des longueurs des réponses H.4 (8B : 3 072 jetons ; 3B : 983) » ; grandeur rapportée : « plus longue zone générée comparée » | Le dernier jeton tiré n'est jamais repassé : `generer_lot` sort de la boucle au pas `max_nouveaux − 1` sans passe de décodage (`harnais/episode.py`, l. 126-127) ; `relire_crochets_lot` ne garde que `min(passes, n_generes)` positions décodées (l. 155) ; `profil_ecarts` compte la zone générée sur ces positions (`harnais/activations.py`, l. 193). Une rangée tronquée à 3 072 jetons a donc au plus 3 071 positions générées comparées. Lue en positions comparées, la couverture du 8B est inatteignable : palier du chemin jamais « fidèle » pour le 8B, donc « propriété du modèle » et PB8 jamais atteints. La probabilité écrite (0,998) compte, elle, des jetons générés (60 réponses H.4 sur 180 à 3 072 jetons ; K5). Le texte mêle les deux unités. | majeur | Définir la couverture sur le nombre de jetons générés par la rangée (8B : une rangée tronquée, 3 072 ; 3B : au moins 983), et l'écrire ; ou, en positions comparées, fixer les seuils à 3 071 et 982. Aligner l. 128, l. 163, la configuration et la liste d'arrêt. Test au bord : sur le jouet, une rangée tronquée atteint la couverture. |
| VC-02 | Table C, palier du chemin (l. 345-355) ; section D (l. 382-383) ; table C, palier de production, ligne « réserve (ρ) » (l. 364) | Aucune ligne « trop beau » au palier du chemin. D renvoie les lignes « trop beau » « aux tables A et C », mais C n'en a qu'au palier de production. La réserve ρ ne porte plus « audit R4 ». | Le brouillon 1 gardait le « trop propre » pour tout palier (l. 270 : « écart exactement nul sur toute la zone générée de toutes les rangées d'un palier »). T0.4 v3 applique P9 à toute phase, chemin compris (l. 297 : « aucun écart non nul dans la zone générée d'une phase »). T0.4 v3 l. 293 écrit « réserve (R4) » pour ρ > 3, comme le brouillon 1 (l. 263 : « réserve, audit R4 et nœud »). Le traitement n'annonce aucun de ces retraits. Les sondes d'audit (`activations.py`, l. 197-208) vérifient des tableaux distincts et un ulp vu ; elles ne voient pas une génération qui referait exactement la passe unique. Sans cette ligne, un palier du chemin tout à zéro se lirait « fidèle » et lèverait la réserve 1 : trou dans la symétrie R4. | majeur | Ajouter au palier du chemin, avant « fidèle » : « aucun écart non nul dans la zone générée de toutes les rangées du palier → trop beau (R4) : réserve maintenue et nœud (T0.4 v3, l. 297) ». Dans D, nommer les deux paliers. Rendre « (R4) » ou « audit R4 » à la ligne « réserve (ρ) ». Test du lecteur sur ce cas. |
| VC-03 | Table A (l. 323-331) ; table C, palier de production (l. 359-365) | Seul le palier du chemin dit « lu dans cet ordre ; la première ligne qui s'applique donne la lecture » (l. 343). La ligne « conforme » de la production (l. 363) ne demande plus « contrôle négatif conforme ». | Le brouillon 1 l'exigeait (l. 251). Un contrôle négatif contraire avec G_D,max ≤ 0,2 et ρ ≤ 3 répond à la fois à « non concluant » (l. 361) et à « conforme » (l. 363) ; un palier tout à zéro, à « trop beau » (l. 362) et à « conforme ». Dans A, « RS1 retenue » (l. 325, qui exige la garde conforme mais pas le contrôle négatif) peut s'appliquer avec « contrôle négatif contraire » (l. 328) ou « trop beau » (l. 330). Aucune préséance n'est écrite pour A et C : celle de E (l. 394) ne vaut que pour E, et T0.4 v3 cumule les lignes (l. 270). Deux lectures contraires sont possibles, dont une qui masque la garde R4. | majeur | Production : ajouter « lu dans cet ordre ; la première ligne qui s'applique donne la lecture » (l'ordre écrit convient). A : ajouter « les lignes s'appliquent ensemble ; une ligne qui dit « nœud » ou « non concluante » prévaut sur « RS1 retenue » ». Test du lecteur sur chaque recouvrement. |
| VC-04 | « Seuil », localisation et ancrage (l. 158, l. 162) ; table C (l. 349-350) ; D (l. 382) | « trop grand » (G_S > 1e-2) se lit avant l'ancrage, donc sans lui. « non concluant (seuil sans marge) » ne figure pas parmi les déclencheurs d'audit. | L'ancrage exige une marge de trois fois l'arrondi pour lire 3e-3 ; rien de tel pour 1e-2 : un R_S au-dessus d'environ 3,3e-3 laisserait lire « défaut (écart trop grand) » sans marge. D déclenche l'audit pour « précision probable », « contexte » et « défaut », pas pour « seuil sans marge », qui est aussi un dépassement de 3e-3. Par ailleurs, l'ancrage compare deux passes uniques : il ne mesure pas l'arrondi propre au décodage ; ce n'est pas écrit. Effet borné : « défaut » mène à un nœud avec diagnostic. | mineur | Lire « défaut (écart trop grand) » seulement si R_S ≤ 1e-2/3 à cette couche, sinon « non concluant (seuil sans marge) ». Ajouter « seuil sans marge » aux déclencheurs de D. Écrire la limite de l'ancrage. |
| VC-05 | « Prédiction », ordres de grandeur (l. 76-77) ; « Seuil », localisation (l. 158, l. 160) ; « Contre-lecture », fichiers à remettre (l. 473) | « seule mesure : 1,27e-4 au plus, au noyau « math » … `validation_reelle.py`, l. 95-97 » ; « au moins 5,7e-2 en simple précision dans T0.4 v2 » ; 1e-2 « environ 80 fois l'arrondi mesuré (1,27e-4) » ; « concentré dans le contexte … oriente le diagnostic vers la passe du contexte » | Le verdict T0.4 v3, cité en tête (`63444faa…`), mesure le chemin en simple précision, au noyau « math », sur le modèle réel : maximum 3,16e-4, situé dans le contexte (zone générée 4,77e-5) (l. 106 ; 2,5 fois la v1, l. 332). D1 en simple précision : au moins 6,81e-2 (l. 107, l. 191). Le 5,7e-2 vient de la phase de logique de la v2, en double précision (prereg T0.4 v3, l. 130 et l. 354). Le verdict lit le profil « contexte plus haut que la zone générée » comme le profil d'arrondi du préremplissage par lot (l. 329). Les conclusions tiennent : 1e-2 vaut environ 32 fois 3,16e-4 et 6,8 fois moins que 6,81e-2. La lecture « non concluant (contexte) » en sort renforcée. | mineur | Remplacer chiffres et sources (3,16e-4 et 6,81e-2, verdict T0.4 v3 l. 106-107, l. 191, l. 332 ; 5,7e-2 en double précision). Dire, pour « concentré dans le contexte », que c'est le profil d'arrondi mesuré (l. 329) : le diagnostic commence par le préremplissage par lot. Ajouter ces lignes aux fichiers à remettre (l. 473). |
| VC-06 | « Métrique », lecture RS1, étape 5 (l. 92) et « pourquoi cette règle » (l. 102) ; tests (l. 429) ; annexe B (l. 553, l. 555) | « la règle retenue … ne choisit jamais entre deux nombres » | `lire_une_note` accepte un entier suivi d'un espace (`rubrique.py`, l. 41) : « 3 - 4 », « 3 or 4 » et « 3 to 4 » se lisent 3 ; « 3-4 » et « 3–4 » sont invalides (K6). Un intervalle écrit avec espaces, que RS1 interdit, est donc lu comme son premier nombre, sans anomalie. La lecture de « 2 of the proposals… » en 2, écrite l. 102, est exacte (K6). | mineur | Écrire la limite (intervalle espacé lu comme son premier nombre par la fonction gelée ; cas comptés et rapportés), ou rendre invalide une occurrence dont la valeur nettoyée continue, après le premier entier, par « - », « – », « to » ou « or » suivi d'un chiffre. Ajouter le cas aux tests. |
| VC-07 | « Prédiction », PB8 (l. 70) ; lecture combinée (l. 371-372) ; « Lecture » (l. 280) | PB8 « confirmée si « propriété du modèle » » ; la table ajoute « propriété du modèle, sous réserve de demi-précision » | Le statut de PB8 sous cette lecture neuve n'est pas défini, alors que la lecture doit écrire le statut de chaque prédiction (l. 280). | mineur | Dire que « sous réserve » laisse PB8 « non concluant » (ou le confirme) ; le tester. |
| VC-08 | « Calcul et devis », crédit (l. 300) ; « Conditions avant le lancement » (l. 315) ; « Questions » (l. 451) | « la recharge du crédit (au moins 11,73 USD au prix plafond, plus le prix des instances d'autres projets en marche) » | La règle (l. 300 ; même forme aux notations, `registres/depenses.md` l. 84 : « exigé ≈ 7,5 × prix + 1,2 USD ») porte sur le crédit au lancement : au moins 8,1 h × (prix de l'offre + prix horaire des autres instances) + 1,2 USD, soit 8,1 × 1,30 + 1,2 = 11,73 USD sans autre projet (arithmétique juste). « plus le prix » oublie le facteur 8,1 h. Et 11,73 USD est un crédit à avoir au lancement, après la dépense de P3, non le montant d'une recharge (R-220 écrit « recharge d'au moins 11,73 USD »). | mineur | « crédit d'au moins 11,73 USD au lancement, plus 8,1 h × le prix horaire des instances d'autres projets en marche ; recharge en conséquence, après la dépense de P3 ». |
| VC-09 | « Plan d'analyse », instruments (l. 195) ; « Questions », Q1 (l. 446) | Q1 couvre « le palier en simple précision, le repère de précision, l'ancrage au noyau « math », le contrôle positif D1 et le témoin » | La décision de la session (consigne ; R-220) nomme quatre instruments, sans l'ancrage. L'ancrage change le noyau d'attention, réglage listé l. 191, pour une passe sans notation : la raison de Q1 le couvre, pas sa lettre. | mineur | Rattacher l'ancrage au palier en simple précision (« passe de ce palier »), ou le faire nommer par la session dans sa consignation de Q1. |
| VC-10 | « Avant le scellement », versement (l. 310) ; « Transparence » (l. 465) | versement des fichiers de travail « (`travail/`, `contre-lecture/`) » en une archive scellée | `contre-lecture/` contient un clone complet du dépôt, `depot/` (1 015 Mo, au commit `00075fc`), avec des copies de pièces scellées, dont les notations qui portent les textes des juges (K10). Le verser tel quel gonflerait l'archive et dupliquerait des pièces scellées. | mineur | Verser `contre-lecture/scripts/`, `contre-lecture/pdf/`, `contre-lecture/empreintes-citees.txt` et `travail/`, sans `depot/` ; le dire. |
| VC-11 | En-tête, registres (l. 25) | registres « au commit `ffdbcda` » ; « seuls deux brouillons de P3 ont changé » jusqu'à `3d0e246` | Exact pour les empreintes (K3). De `ffdbcda` à `3d0e246`, changent le candidat 1 de P3, son sceau et le sceau du brouillon 4 (formulation approchée). Depuis, `f303ba9` ajoute R-219 et R-220 (décisions de la session sur Q1, Q2, RS1, Q7) ; lignes citées inchangées. | pour information | Au scellement : citer les registres au commit de scellement, et R-220 pour les décisions de la session. |
| VC-12 | « pourquoi cette règle », casse (l. 101) | « 5 réponses H.4, dont 4 du 8B, rejetées pour la seule casse : audit, l. 135 » | L'audit l. 135 range « casse (« ## Specificity: 4 ») : 4 réponses du 8B, 1 du 3B » parmi les formes lisibles par un humain que la règle gelée rejette ; il ne dit pas que la casse était leur seul défaut. | pour information | « 5 réponses H.4, dont 4 du 8B, portent une ligne en casse mixte que la règle gelée rejette ». |
| VC-13 | « Écarts déclarés au dispositif de T0.4 v3 » (l. 256-261) | Le palier de production tourne au noyau par défaut ; l'écart n'est pas listé. | T0.4 v3 faisait tourner sa production au noyau « math » (prereg T0.4 v3, l. 44 et l. 135). Écart déjà présent au brouillon 1 ; il est fondé sur la garde du pilote, au noyau par défaut (pilote, l. 138 et l. 155). | pour information | Ajouter une ligne à la liste des écarts. |
| VC-14 | « Mémoire » (l. 269) | « environ 1,7 Go par lot RS1 » | Les captures sont en simple précision (`activations.py`, l. 34-37), des deux côtés. Toutes les rangées étant gardées, la génération capture autant que la passe unique : environ 3,4 Go par lot RS1 (3 couches × 8 rangées × 4 380 positions × 4 096 × 4 octets, deux fois). La mémoire vive exigée (64 Go) couvre encore. | pour information | Corriger l'estimation. |
| VC-15 | Ordre des phases, rejeu (l. 236) ; repère (l. 123) | « conversion en simple précision … repère sur les 16 transcriptions », par `repere_precision` | `repere_precision` (`validation_reelle.py`, l. 526-541) calcule la passe du modèle courant, attendu en demi-précision, contre des références de plus haute précision. Après la conversion, le modèle courant est en simple précision : rôles à garder dans le code. | pour information | À vérifier à la relecture R2 du code. |
| VC-16 | Coût et plafond (l. 297-298) ; relancement (l. 402) | téléchargement « au plus 1,1 USD » | 22,5 Go × 0,05 USD = 1,125 USD. Le plafond tient (13,595 ≤ 13,6) ; la marge du relancement à 1,30 USD de l'heure tombe de 0,03 à environ 0,005 USD. | pour information | Écrire 1,13 USD, ou garder 1,1 avec cette note. |
| VC-17 | « Conditions avant le lancement » (l. 316) | « P3 lancé avant (R-212 : « après P3 ») » | R-212 (l. 349) dit « après P3 » ; « lancé » est une lecture, non la plus prudente. Le GO séparé de Lazar tranchera. | pour information | Le nommer dans la demande de GO. |
| VC-18 | « Transparence » (l. 468) | « Les changements du brouillon 1 au brouillon 2 viennent tous de la contre-lecture 1 et des décisions de la session » | Trois ajouts viennent du rédacteur (traitement, l. 6 ; R-220), ainsi que les échéances de requalification abaissées (7 000 et 4 500 s, l. 234-235, motif l. 243), en réponse à PB-01, PB-03 et PB-05. « aucun ne vient d'un résultat » reste vrai : aucune notation RS1 n'existe. | pour information | « de la contre-lecture 1, de son traitement par le rédacteur (trois ajouts nommés) et des décisions de la session ». |

## 3. Constats de la contre-lecture (PB-01 à PB-15)

| constat | sort | preuve dans le brouillon 2 (section, ligne, phrase) |
|---|---|---|
| PB-01 | traité (remarques VC-04, VC-05) | « Seuil », l. 157-161 : localisation (« trop grand » au-dessus de 1e-2 ; « concentré dans la zone générée » ; « concentré dans le contexte » ; « diffus ») ; l. 162 : ancrage « R_S(ℓ) ≤ 1e-3 » ; l. 153 et table C l. 364-365 : en demi-précision, « réserve et nœud, jamais « défaut » » ; l. 372 : logique fidèle et réserve de demi-précision lues « sous réserve » ; l. 123 : ρ « rapporté aussi rangée par rangée » ; l. 166 et l. 411 : TF32 et réductions relus, sinon arrêt ; l. 76 : ordre de grandeur « de l'ordre de 1e-4 à 1e-3 ». |
| PB-02 | traité | « Métrique », l. 110 : « Rangées gardées : toutes les rangées de chaque lot » ; l. 113 : règle k(n − 1) et limite déclarée ; « Seuil », l. 147 : « non concluant » sous 10 rangées comparables ; table A l. 329 : réserve, « les rangées courtes … sont hors du compte » ; tests l. 434. Formule conforme au verdict T0.4 v3, l. 209, et au code (`ecart_decale_zone_generee`, `activations.py` l. 149-175). |
| PB-03 | traité (remarques VC-06, VC-12) | « Métrique », l. 88-97 : étapes 1 à 10 (nettoyage l. 90, conforme à `rubrique.py` l. 88 ; « chiffrée » l. 91 ; valeur par `lire_une_note` l. 92 ; « première occurrence chiffrée », toutes valides et égales, sort d'une occurrence suivante illisible, l. 93) ; choix argumenté l. 98-102 ; tests l. 429 ; annexe B l. 555. |
| PB-04 | traité en partie (VC-01) | L1 et L2 au palier du chemin (l. 125 : « rejoue **L1 et L2** ») ; couverture exigée (l. 128, l. 163, table C l. 354) ; lecture bornée au domaine couvert (l. 182, l. 355) ; ligne « D1 non probant » (l. 165, l. 348) ; phrase corrigée (l. 117 : « seules leurs rangées tronquées couvrent le domaine long »). Mais la couverture du 8B est inatteignable si on la lit en positions comparées. |
| PB-05 | traité | « Chaîne des limites de temps », l. 247-254 ; seuil de mise en place 2 700 s, l. 252, repris aux causes d'un arrêt l. 398-400 ; un lot de dépassement par phase, l. 241-242 ; ancrage de chaque échéance, l. 234-238 ; plafond, l. 298. Arithmétique refaite (section 5). |
| PB-06 | traité (remarque VC-09) | l. 195 (instruments, avec la raison) ; l. 313-317 (conditions avant le lancement) ; l. 445-447 (Q1, Q2 retirées des nœuds). |
| PB-07 | traité | En-tête, l. 6-8 (« Aucun seuil de la règle du plan B du pilote n'est changé ») ; « Seuil », l. 172-178 (« Conditions et seuils neufs ») ; « Métrique », l. 109 (« même grandeur et mêmes seuils … mais **différée** »). |
| PB-08 | traité | l. 238 et l. 244 (témoins en fin de run) ; l. 412 (« Témoin impossible », seule erreur documentée) ; l. 377 ; tests l. 436 (cas sain, deux artefacts). |
| PB-09 | traité | l. 291 (« de 454,2 à 494,9 s ») ; l. 298 (destruction proposée, disque au-delà de 72 heures consigné) ; l. 402 (formule (iii) et « Portée réelle ») ; l. 299 (GO-2026-10-17-01, environ 6 USD). |
| PB-10 | traité (remarque VC-10) | (a) l. 10-11 (« Tests attendus », empreintes des scripts) ; (b) l. 273 (graines consignées rangée par rangée, `graine_entiere`) ; (c) l. 32 (`c63d4f1`) ; (d) l. 310 (versement) ; (e) l. 280 (statut de PB1 à PB10) ; (f) l. 114 (rapports de la garde dans le fichier des notations RS1) ; (g) l. 308 (relecture R2 du code et de la chaîne). |
| PB-11 | traité | « Ce que RS1 fait perdre et risquer », l. 215-227 ; Q7, l. 448. Pénalité graduée de H.4 vérifiée (« -1 » pour « 1-2 proposals »). |
| PB-12 | traité | « RS1 » sur 71 lignes ; seul « S1 » restant : le nom du fichier de travail `travail/S1-brouillon1.txt` (l. 538, déclaré « nom d'avant le renommage »). |
| PB-13 | traité | l. 47 (« jusqu'à 5 206 jetons de contexte (5 511 avec le remplissage) … 6 030 jetons est le plus long contexte joué ») ; l. 211. |
| PB-14 | traité (remarque VC-14) | « Mémoire », l. 269 ; ordre, l. 244 (rejeu du 3B avant celui du 8B). |
| PB-15 | traité | « Portée du rejeu », l. 263-267 ; témoin binomial et biais, l. 168 ; réponses H.4 régénérées, l. 130 (verdict complémentaire l. 317, vérifié) ; effectifs, l. 164-165 et l. 260. |

Points A à G de la contre-lecture : aucun changement demandé au-delà des constats ; la vérification courte est prévue (l. 309, l. 473).

## 4. Ajouts du rédacteur (point b)

**« Concentré dans le contexte » lu « non concluant (contexte) ».** Juste.
- La définition de « diffus » est bien celle de `prereg/T0.4-validation-modele-reel-v3.md` l. 278 : « écart ≤ 1e-2, diffus (maxima du contexte et de la zone générée tous deux ≥ 1e-5 et dans un rapport ≤ 3) ». Ligne et rapport d'au plus 3 : exacts.
- La condition « tous deux ≥ 1e-5 » est omise, sans effet : dès qu'un maximum dépasse 3e-3 avec un rapport d'au plus 3, l'autre dépasse 1e-3.
- La ligne 278 vise la phase de logique (seuil 1e-4) ; pour le chemin, T0.4 v3 lit tout dépassement de 3e-3 « non validé … nœud » (l. 284). La transposition garde un nœud dans tous les cas : conséquence équivalente.
- Un écart concentré dans le contexte n'est ni « diffus » (l. 278) ni « concentré dans la zone générée » (l. 277). Le lire « non concluant » ne favorise aucun signe : ni « fidèle », ni « défaut » ; PB8 reste non concluant. Il déclenche le même audit que « défaut » (D, l. 382). C'est même le profil d'arrondi mesuré (VC-05).
- Aucun seuil de la règle du plan B n'est touché.

**Ancrage compté seulement s'il y a un dépassement.** Juste.
- G_S est le maximum mesuré de l'écart entre les deux chemins. S'il reste sous 3e-3, il borne cet écart sur les positions et couches comparées, quel que soit l'arrondi.
- L'ancrage ne sert qu'à interpréter un dépassement (fausse alarme). La sensibilité à un défaut vient de D1, pas de l'ancrage.
- Nuances : la borne vaut pour les couches 7, 15, 23 et le domaine couvert (déclaré, l. 182, l. 355). En toute rigueur, l'écart logique est borné par 3e-3 plus l'arrondi ; une compensation exacte par l'arrondi n'est pas plausible pour un défaut systématique.
- Un R_S au-dessus de G_S n'est pas suspect : deux calculs au même noyau partagent leurs arrondis (T0.4 v3, l. 199). La « réserve écrite » suffit.
- Restes : VC-04.

**Sort d'une occurrence suivante illisible.** Juste, sans signe favorisé.
- Non chiffrée, elle est ignorée et comptée ; chiffrée mais invalide, elle fait l'anomalie « note invalide » (l. 93). La règle est la même avant et après la première occurrence chiffrée.
- Elle ne remplace ni n'arrondit jamais, comme `rubrique.py` l. 7-8. Elle est fixée avant toute notation RS1, s'applique de même à A, B et C, et ses cas sont comptés (l. 107).
- Vérifié sur la fonction gelée : « 4.5 » et « 4/4 » invalides, « 4/5 » et « 4.0 » lus 4 (K6).
- Elle ne touche aucun seuil de la règle du plan B (20 %, 48 tâches, 0,8, 0,6 : `lire_pilote.py` l. 47-55).
- Reste : VC-06 (intervalle espacé lu comme son premier nombre).

## 5. Chiffres neufs, contre leurs sources (point c)

| chiffre du brouillon 2 | source et contrôle | résultat |
|---|---|---|
| lots de 8 du 8B au plafond : 21 sur 22, de 454,2 à 494,9 s (l. 291) | journal `traces/t05-notations-20261017-235701-mDaN/journal.txt` (`1ec04b85…`), lignes PROGRES du 8B : lot 1 454,2 s, lot 20 494,9 s, lot 21 299,3 s ; K5 : le lot 21 est le seul lot du 8B sans réponse tronquée | conforme |
| dernier lot, de 4 rangées, au plafond, 262,2 s | journal, lot 23/23 ; K5 : le lot 23 porte une réponse tronquée | conforme |
| seul lot sans tronquée : 299,3 s | journal, lot 21/23 ; K5 | conforme |
| lots du 3B de 52,3 à 319,8 s ; 8B 10 478,2 s, 3B 4 944,1 s | journal | conforme |
| mise en place environ 1 576 s ; 763 tests en 1 455,20 s ; création 19:09:43 | journal (19:10:32 à 19:36:48) ; `registres/depenses.md` l. 85 | conforme |
| 893 tests, 1 631 s (R-215) | R-215 : « 893 passed in 1631.13s » | conforme (908 tests depuis, `f303ba9`) |
| garde de l'agent : 5 206 jetons, 5 511 avec le remplissage, 6 030 le plus long contexte, 400 jetons générés | verdict du pilote l. 384-386 ; pilote l. 157 (`max_nouveaux` = 400) | conforme |
| plafond 13,6 USD | 8,1 × 1,30 = 10,53 ; + 1,1 + 1,94 = 13,57 ; 1,94 = 72 h × 0,027 (R-215) | conforme (VC-16) |
| crédit exigé 11,73 USD | 8,1 × 1,30 + 1,2 = 11,73 ; règle des notations, `depenses.md` l. 84 ; crédit relu 8,46 USD (R-214) | arithmétique conforme ; formulation VC-08 |
| cumul au plus environ 94 USD | 63,2 (`depenses.md` l. 86) + 11,2 (R-215) + 6 (`go.md` l. 26) + 13,6 = 94,0 | conforme |
| relancement : 10,56 − 8,1 × prix ; 0,03 et 1,81 USD | 13,6 − 1,1 − 1,94 = 10,56 ; − 10,53 = 0,03 ; − 8,748 = 1,81 ; forme du complément l. 131 | conforme |
| chaîne : 23 630 ; 23 700 ; 24 720 (412 min) ; 27 720 (462 min) ; 2 700 ; 28 320 (472 min) ; 8,03 h | 7 500 + 4 830 + 3 600 + 5 700 + 1 700 + 300 ; 23 700 + 900 + 120 ; 24 720 + 300 + 2 700 ; dérivation du complément l. 101 (430 − 400 − 5 min) ; 27 720 + 600 (286 + 14 + 300) ; 28 920 s | conforme |
| motif des échéances : environ 13 lots au plafond, environ 6 800 s et 4 400 s | 10 % de rangées : 22 × (1 − 0,9⁸) + (1 − 0,9⁴) ≈ 12,9 lots ; 13 × 480 + 10 × 40 ≈ 6 600 à 6 800 s ; 13 × 320 + 10 × 25 ≈ 4 400 s | conforme (ordre de grandeur) |
| couverture : 3 072 et 983 (982,75) ; 0,998 et 0,99 | K5 : 75e centiles 3 072,0 et 982,75 ; parts 60/180 et 45/180 ; 1 − (2/3)¹⁶ = 0,9985 ; 1 − 0,75¹⁶ = 0,9900 | conforme (unité : VC-01) |
| témoin : 8B 0 ou au moins 11 ; 3B au moins 5 | K5 : P(T = 0) = 0,0015 ; P(T ≥ 11) = 0,0040 et P(T ≥ 10) = 0,016 ; 3B : P(T ≥ 5) = 0,00086 et P(T ≥ 4) = 0,0070 | conforme |
| k(N) = N − ⌊0,99 (N − 1)⌋ ; « courte » sous environ 20 à 45 jetons | verdict T0.4 v3 l. 209 ; calcul : seuils de 20 jetons (contexte 1 700) et 46 (contexte 4 300) | conforme (« environ ») |
| aucune rangée H.4 sous k(n) ; plus courtes réponses 150 et 177 ; contextes 5 261 à 7 003 (médiane 6 102,5) ; positions 10 075 et 9 749 ; lots avec tronquée (22 et 9) ; cadres 21 et 9 | K5 | conforme |
| 1e-2 « environ 80 fois l'arrondi (1,27e-4) » et « 6 fois sous D1 (5,7e-2) » | verdict T0.4 v3 l. 106-107, l. 191 ; prereg T0.4 v3 l. 130, l. 354 | sources périmées ou mal attribuées : VC-05 |
| 130 Gio (T0.4 v3) | `validation_reelle.py` l. 116 | conforme |
| pic de 57 Gio ; 13 Go de scores | 2 × 28,42 ; 32 têtes × 10 000² × 4 octets ≈ 12,8 Go | conforme |
| 1,7 Go par lot RS1 | `activations.py` l. 34-37 | sous-estimé : VC-14 |
| 21 valeurs ; « −1 dès une ou deux propositions hors sujet » | somme de 0 à 20 ; H.4 : « -1 » pour « 1-2 proposals » | conforme |
| 141 sur 142 ; 5 réponses dont 4 du 8B | audit l. 177 ; audit l. 135 | conforme ; formulation VC-12 |
| durée attendue 8 500 à 12 000 s ; instance 2,9 à 4 h ; coût 3,1 à 5,2 USD | sommes des estimations écrites ; 2,9 × 1,08 et 4 × 1,30 | cohérent |

Lignes de code citées par le brouillon 2 et contrôlées : `rubrique.py` l. 7-8, 39, 41, 44-60, 88 ; `harnais/episode.py` l. 101, 109, 121, 155, 260 ; `harnais/activations.py` l. 149-194 ; `harnais/validation_reelle.py` l. 95-99, 116, 364-369, 454, 526 ; `harnais/modeles.py` l. 134-138 ; `lire_pilote.py` l. 47-55, 273 ; `noter_pilote_a.py` l. 272 ; `harnais/run_harnais_factice.py` l. 58-59 ; `invites.py` l. 34 ; `lancer_pilote_a.py` l. 263. Toutes exactes. Lignes des textes : pilote l. 34, 39, 40, 129-132, 138, 155, 157, 184, 186, 187 ; complément l. 101, 123, 125-129, 131 ; T0.4 v3 l. 105, 130, 134-139, 173, 199, 270-297 ; verdict T0.4 v3 l. 209 ; verdict du pilote l. 384-387 ; verdict complémentaire l. 317, 356, section 2.3 ; audit l. 135, 172, 177, 195 ; registres l. 349-354, `go.md` l. 16, 26, `depenses.md` l. 84-86 ; programme l. 241 ; brief l. 158, 358. Toutes exactes.

## 6. Hypothèses, modèle, réglages, nœuds (point d)

- Aucune hypothèse du programme n'est testée (l. 41 ; pilote l. 34). Aucune revendication du programme n'est touchée. H-R et « propriété du modèle » sont restreintes aux couches comparées et au domaine couvert (l. 48-49, l. 371) : plus étroites, sans effet sur le programme.
- Modèles : mêmes révisions qu'au pilote (l. 189). Aucun changement de modèle ; la bascule reste un nœud (Q5).
- Réglages des notations : seul changement, H.4 → RS1 avec sa règle de lecture (l. 193, annexe B). Les « réglages effectifs relus » avant le palier en simple précision sont déjà ceux de tout le run : `regler_determinisme` (`harnais/modeles.py` l. 269-293) coupe TF32 et les réductions en précision réduite dès le départ. La notation passe par `jouer_episodes` au lieu de `noter_ensembles` : même `generer_lot`, test d'équivalence prévu (l. 433). Instruments : VC-09.
- Nœuds restants, bien posés : dépense (GO séparé sur le devis, plafond 13,6 USD, et recharge ; l. 451) ; Q3, point d'attention sans écart proposé (l. 452) ; Q4, Q5, Q6 (l. 453-455) ; lectures « réserve et nœud » de la table C présentées à Lazar (l. 456). Remarques VC-08 et VC-17.

## 7. Cohérence interne, et ce qui reste avant le scellement (point e)

- Renvois internes présents : « Portée du rejeu », « Conditions avant le lancement », « Avant le scellement », « Graines », table E, Q4 à Q7, liste d'arrêt.
- Nombres concordants entre « Métrique », « Seuil », tables, configuration (l. 304), « Justification des tailles » (l. 286) et « Écarts déclarés » (l. 260) : 16 rangées, 10 comparables, 6 sur 8, 3e-3, 1e-2, 1e-3, rapport 3, 0,2, 0,1, 0,75, 0,005, durées.
- Ordre du plan d'analyse cohérent : requalification du 8B, puis du 3B ; rejeu du 3B, puis du 8B ; témoins ; résumé. Point pour le code : VC-15.
- Tables de lecture : VC-02, VC-03, VC-07.
- Liste d'arrêt cohérente avec les gardes : couverture (l. 410, l. 413), réglages relus (l. 411), « témoin impossible » (l. 412), plafond (l. 414).
- Champs « au candidat » : commit du code, tests attendus, empreintes des deux scripts de l'instance (l. 9-11). Noms conformes au modèle des notations (`scripts/amorce_instance_t05_notations.sh`, `scripts/notations_t05_instance.sh`). Champs « au scellement » : date, entropie, configuration, invite RS1 (l. 4, l. 33-35).
- Reste avant le scellement :
  1. corrections VC-01 à VC-10 (et, au choix, VC-11 à VC-18) ;
  2. code (`rubrique_simplifiee.py`, `juges_simplifies.py`, `requalifier_juges.py`, `lire_requalification.py`, dossier `docs/sources/invites-plan-b-v1/`) et chaîne `docs/procedures/planb-T0.5-v1/`, au commit candidat ; suite complète des tests et son nombre ; empreintes des scripts ;
  3. relecture R2 du code et de la chaîne par des sous-agents neufs (trois angles), puis vérification courte de ses corrections ;
  4. versement scellé des notes de conception, de la contre-lecture, du traitement, de `travail/`, des parties utiles de `contre-lecture/` (VC-10) et de ce rapport ; section « Contre-lecture » complétée (cette vérification, les relectures R2) ;
  5. registres cités au commit de scellement, R-220 cité (VC-11) ;
  6. entropie tirée, configuration et invite RS1 scellées.
- Puis, avant le lancement : GO séparé de Lazar, recharge, P3 lancé, contrôles avant dépense (dont le jeton unique des notes sur le 3B, l. 212).

## 8. Ce que je n'ai pas pu vérifier

- Longueurs en jetons sous RS1 : aucun tokeniseur hors ligne. Contextes de 1 700 à 4 300 jetons et réponses d'environ 80 jetons restent des estimations.
- Comportement sur la carte : bruit de la simple précision au noyau par défaut sur 10 000 positions, valeur réelle de R_S, durées des lots en simple précision, `generate` sous les algorithmes déterministes.
- Code neuf et chaîne : non écrits.
- Suite des tests : non lancée (consigne).
- État Vast.ai et crédit : interdits.
- Phrase de la p. 29 : vue sur les extraits (`contre-lecture/pdf/p29.txt`, `travail/p29.txt`), non sur le PDF lui-même.
- Rapport caractères/jetons des notes (5,08 à 5,56) et R-067 : non refaits ; inchangés depuis le brouillon 1, vérifiés par la contre-lecture.
- Intention de la session sur l'ancrage dans Q1 (VC-09) et sur « après P3 » (VC-17).

## 9. Jugement d'ensemble

**Prêt après corrections** : VC-01 (couverture en jetons générés, ou seuils 3 071 et 982), VC-02 (« trop beau » au palier du chemin ; « R4 » rendu à la réserve ρ), VC-03 (ordre et préséance des tables A et C), VC-04 (ancrage et « trop grand » ; « seuil sans marge » dans D), VC-05 (chiffres d'arrondi et de D1 du verdict T0.4 v3), VC-06 (intervalle espacé), VC-07 (statut de PB8), VC-08 (crédit au lancement, facteur 8,1 h), VC-09 (ancrage dans Q1), VC-10 (versement sans le clone) ; chacune se vérifie sur sa ligne, sans nouvelle lecture d'ensemble.
