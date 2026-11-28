"""Construit programme-fusionne-v4.md à partir de la v3 scellée (session 15) par remplacements exacts (chacun une fois).

Usage : python3 -I faire_v4.py SOURCE_V3 SORTIE_V4
"""
import sys

src, out = sys.argv[1:3]
t = open(src, encoding="utf-8").read()
R = []
def r(old, new):
    R.append((old, new))

# Titre et statut
r("programme fusionné des deux lignées — brouillon v3", "programme fusionné des deux lignées — brouillon v4")
r("> **Statut.** Brouillon v3 de la session du dépôt (session 15), daté du 17 octobre 2026. Il reprend le brouillon v2 de la session 14",
  "> **Statut.** Brouillon v4 de la session du dépôt (session 14, qui reprend le 19 octobre après la session 15), daté du 19 octobre 2026. Il reprend le brouillon v3 de la session 15 (`brouillons/pain-axis-programme-fusionne-v3/programme-fusionne-v3.md`, `294e8afe…`, 17 octobre) et traite les 17 constats de sa relecture par un quatrième sous-agent neuf (`relecture-v3-v1.md`, RL-01 à RL-17) ; il met l'état à jour au 19 octobre. La v3 reprenait le brouillon v2 de la session 14")
r("Cette v3 traite les 20 constats de la vérification de la v2 par un troisième sous-agent neuf",
  "La v3 traitait les 20 constats de la vérification de la v2 par un troisième sous-agent neuf")
r("« Entrée au programme » vise aussi tout préenregistrement (papier C, T0.6, T0.7, T0.8, pilote T0.9, G1) :",
  "« Entrée au programme » vise aussi tout préenregistrement (papier C, T0.6, T0.7, T0.8, pilote T0.9, G1, P3) :")
r("**Une seule règle de niveau** (VT-01) : le niveau « proposition » (défaut sous 48 heures) ne sert ici qu'à la préparation (code, plan écrit), qui n'engage l'entrée d'aucune unité ; toute entrée dans un préenregistrement est un nœud (nœud 1).",
  "**Une seule règle de niveau** (VT-01, RL-01, RL-02) : **routine**, la préparation (code, tests, plan écrit), qui n'engage l'entrée d'aucune unité (`CLAUDE.md` : code, tests et fichiers sont de la routine) ; **proposition** (défaut sous 48 heures), les seuls choix que `CLAUDE.md` met à ce niveau, ici le choix de la coupe (périmètre interne d'une phase) et une conclusion sur D1 qui ne change aucun modèle (sinon nœud 5), plus une exception annoncée : le lecteur du bras C-P4b, qui est le juge (imposé par N-013 § 8 ; DI-01), s'il n'est lié à aucune lecture d'affect ; **nœud sans défaut**, toute entrée dans un préenregistrement (nœud 1).")

# Pièces
r("**Pièces.** Dans ce dossier (`brouillons/pain-axis-programme-fusionne-v3/`) : `programme-fusionne-v3.md` (ce texte) ; `verification-v2-v1.md`",
  "**Pièces.** Dans ce dossier (`brouillons/pain-axis-programme-fusionne-v4/`) : `programme-fusionne-v4.md` (ce texte) ; `traitement-relecture-v3-v1.md` (sort de chacun des 17 constats de la relecture de la v3 et section de la v4 qui le porte). Dans `brouillons/pain-axis-programme-fusionne-v3/`, scellés et inchangés (R12) : `programme-fusionne-v3.md` ; `relecture-v3-v1.md` (rapport du quatrième sous-agent neuf, versé par la session 15) ; `verification-v2-v1.md`")
r("que ni la v2 ni cette v3 ne reprennent (nœud 14).",
  "que ni la v2, ni la v3, ni cette v4 ne reprennent (nœud 14 ; la v1 et la v2 du programme gardent deux doses publiées, RL-06).")

# Paragraphe de la vérification : passé, puis relecture de la v3
r("**Vérification de la v2 : faite ; cette v3 en traite les constats.**",
  "**Relecture de la v3 : faite ; cette v4 en traite les constats.** Un quatrième sous-agent neuf, en lecture seule, sans accès au réseau, le 17 octobre (rapport vers 09:47 UTC, versé par la session 15, R-194) : la v3 porte les 20 constats de la vérification (19 bien portés, VT-01 en partie) ; aucune empreinte, page, ligne, commit, décision ni renvoi « nœud n » faux ; aucune dose ni aucun texte d'attaque ; 17 constats propres, 0 bloquant, 1 majeur (RL-01 : la préparation, rangée au niveau « proposition », est de la routine), 8 mineurs, 8 pour information. Sort de chacun : `traitement-relecture-v3-v1.md` (ce dossier). Cette v4 n'est pas relue par un sous-agent : son écart à la v3 a été relu par la session avant le scellement.\n\n**Vérification de la v2 : faite ; la v3 en a traité les constats.**")
r("Sort de chaque constat : `traitement-verification-v1.md`. Cette v3 n'est pas encore relue. Elle est scellée avant sa relecture, comme la v2 (`3484d11`), pour que le quatrième sous-agent neuf lise une version figée (R-183, R-187) ; ses constats iront dans une v4, puis le texte sera transmis à Lazar avec les nœuds de la section 9.",
  "Sort de chaque constat : `traitement-verification-v1.md`. La v3 a été scellée avant sa relecture, comme la v2 (`3484d11`), pour que le quatrième sous-agent neuf lise une version figée (R-183, R-187) ; le traitement scellé avec elle dit à tort qu'elle « attend sa relecture avant scellement » (RL-08).")
r("; VT ceux de la vérification de la v2 (`traitement-verification-v1.md`).",
  "; VT ceux de la vérification de la v2 (`traitement-verification-v1.md`) ; RL ceux de la relecture de la v3 (`traitement-relecture-v3-v1.md`).")

# Section 0 : état au 19 octobre
r("- **État des dépendances au 17 octobre** (registres ; l'annexe `etat-registres-v1.md` décrit l'état au 13 octobre) :",
  "- **État des dépendances au 19 octobre** (registres ; l'annexe `etat-registres-v1.md` décrit l'état au 13 octobre) :")
r("Les juges 8B et 3B n'ont toujours aucune notation décisive. Leur validation passe par l'exécution de N-021 (a) et son verdict complémentaire : préalables faits (chaîne versée au commit C1 `6c96075`, journaux ajoutés au commit C2 `cc05d170` ; R-169) ; préenregistrement complémentaire scellé (S `b604164`, `prereg/T0.5-pilote-notations-v1.md` ; R-175) ; lancement décidé par Lazar (R-176, R-181) ; cinq appels du lanceur arrêtés avant la création de l'instance le 15 octobre, le dernier à 11:56 UTC, sans run ni dépense (R-177 à R-182 ; VT-15) ; veille reprise par la session 15 le 17 octobre (R-184).",
  "Les notations décisives des juges 8B et 3B sont refaites (N-021 (a)) : préenregistrement complémentaire scellé (S `b604164`, `prereg/T0.5-pilote-notations-v1.md` ; R-175) ; huit appels du lanceur arrêtés avant la création, sans dépense (R-177 à R-190 ; le sixième arrêté par la session, R-185, après quoi Lazar a donné son accord dans la session 15, R-186 ; RL-04) ; lanceur v2 de l'option (c) (R-190, R-195) ; second appel du lanceur v2 : instance 56438435 créée le 17 octobre à 19:09 UTC (R-204) ; run `20261017-193648-t05-notations-reel` fini, récupération toute conforme, fusion `2799964`, instance arrêtée et gardée (R-205) ; lecture préenregistrée `20261018-214028-t05-lecture-juges` : décomposition impossible pour les deux juges (0 et 2 tâches complètes), audit de symétrie (R4) déclenché, scellé, mesure et calcul hors de cause (`docs/verdicts/audit-R4-T0.5-pilote-notations-v1.md`, `1a0232a`) ; verdict R13 complémentaire en cours le 19 octobre.")
r("  - T0.6 et T0.7 : préenregistrements en brouillon (T0.7 en brouillon 3), non scellés.",
  "  - T0.6 et T0.7 : préenregistrements en brouillon (T0.7 en brouillon 4, R-189), non scellés.\n  - P3, premier test boîte blanche sur l'organisme (i-a) (décision de Lazar, R-192) : préenregistrement en brouillon 4, contre-lu deux fois (R-202), non scellé ; sa passe payée attend le scellement et l'accord de Lazar dans la session (R-185). Greffer une unité de ce brouillon sur cette passe serait un nœud (nœuds 1 et 12 ; RL-05).")
r("pilote T0.9 (4 heures de carte, dans le plafond du devis de phase 0) soumis à un GO séparé, non accordé ;",
  "pilote T0.9 : GO-2026-10-17-01 (4 heures de carte au plus, dans le plafond du devis de phase 0, lancées seulement après le scellement du préenregistrement de HC1 à HC3 contre-lu, chaque lancement sur l'accord de Lazar dans la session ; R-192 ; RL-05) ;")
r("  - Dépense de la phase 0 : au plus ≈ 54,6 USD sur 150 au 17 octobre 07:48 UTC, disques des trois instances arrêtées compris (≈ 51,3 USD au 15 octobre 12:45 UTC, plus 43 heures de disques à 0,0756 USD de l'heure, `storage_total_cost` lu sur le compte ; alerte à 120 ; `registres/depenses.md`), plus l'engagement de N-021 (au plus 10,5 USD).",
  "  - Dépense de la phase 0 : au plus ≈ 63,2 USD sur 150, plus les disques, au 18 octobre 21:40 UTC, notations refaites comprises (au plus 8,23 USD ; `registres/depenses.md`, dernière ligne ; alerte à 120).")
r("Restent ouvertes au 17 octobre (numéros relus sur l'API du dépôt ce jour-là, sans commentaire ni revue) :",
  "Restent ouvertes au 19 octobre (numéros relus sur l'API du dépôt les 15 et 17 octobre, sans commentaire ni revue) :")
r("Aucune instruction du canal au-delà du n° 02 au 17 octobre : les branches du canal n'ont pas bougé depuis le 13 octobre, et seul le message programme-conv n° 02 porte le mot INSTRUCTION (relu sur les branches distantes le 17 octobre, R-184).",
  "Aucune instruction du canal au-delà du n° 02 au 19 octobre : les branches `canal/programme-conv-*`, `canal/programme-k-*` et `canal/session-depot-*` n'ont pas bougé depuis le 15 octobre, et seul le message programme-conv n° 02 porte le mot INSTRUCTION (relu sur les branches distantes les 17 et 19 octobre).")

# Section 1 et 2
r("et les auteurs notent que leur lecture ne sépare pas le dommage au modèle de la douleur du locuteur courant (VP-16) ;",
  "et les auteurs notent que leur lecture ne sépare pas le dommage au modèle de la douleur du locuteur courant (v2 p. 11 ; VP-16 ; RL-17) ;")
r("| Sous pilotage douleur, la complaisance ne monte pas", "| Sous pilotage de la direction douleur, la complaisance ne monte pas")

# Section 3 : tableau
r("| code puis une passe | code : routine, qui n'engage pas l'entrée ; passe : nœuds (dépense ; exposition aux scénarios publiés ; textes nouveaux du plan 2×3) ; première unité si Lazar l'ouvre |",
  "| code puis une passe | code : routine, qui n'engage pas l'entrée ; entrée de PA-1 et de son propre préenregistrement : nœud 1 (RL-15) ; passe : nœuds (dépense ; exposition aux scénarios publiés ; textes nouveaux du plan 2×3) ; première unité si Lazar l'ouvre |")
r("; proposition : la préparation seulement (plan écrit, code) ; nœuds aussi : annexe d'identification lue sur la direction douleur, 3B comme juge (changement de modèle, nœud 5), modèle de menace en boîte grise (nœud 15) |",
  "; routine : la préparation seulement (plan écrit, code ; RL-01) ; nœuds aussi : annexe d'identification lue sur la direction douleur, 3B comme juge (changement de modèle, nœud 5), modèle de menace en boîte grise (nœud 15) |")
r("| **intervention : nœud** (écriture dans les activations d'un moniteur, prévue nulle part au programme) | nœud, sans protocole ici |",
  "| **intervention : nœud** (écriture dans les activations d'un moniteur génératif, prévue nulle part au programme ; RL-03) | nœud, sans protocole ici |")
r("| nœud sans défaut (entrée du descriptif dans un préenregistrement, nœud 1) ; proposition : la préparation seulement ; tension avec R-030 : réserve, aucun changement proposé |",
  "| nœud sans défaut (entrée du descriptif dans un préenregistrement, nœud 1) ; routine : la préparation seulement (RL-01) ; tension avec R-030 : réserve, aucun changement proposé |")
r("| défenses conditionnelles | nœuds : E-C3 et NK9 (poids du moniteur), défaillance fermée (règle nouvelle), défenses hors de l'énoncé de HC5 |",
  "| défenses conditionnelles | nœud sans défaut (entrée du prix de la défense et du désaccord d'ensemble dans un préenregistrement, nœud 1 ; RL-09) ; nœuds aussi : E-C3 et NK9 (poids du moniteur), défaillance fermée (règle nouvelle), défenses hors de l'énoncé de HC5 |")
r("| recentré sur ce qui reste ouvert | nœud (invariant, modèle de menace) |",
  "| recentré sur ce qui reste ouvert | nœuds 8 (invariant) et 15 (modèle de menace ; RL-07) |")

# Section 4
r("une lecture à cette position reste descriptive, proposée à Lazar (VF-12).",
  "une lecture à cette position reste descriptive ; l'inscrire au préenregistrement de PA-1 est un nœud (nœud 1 ; VF-12 ; RL-16).")
r("Greffer PA-1 sur une autre passe payée (génération de T0.6, dont le préenregistrement est encore ouvert, VF-27 ; passe de T0.7 ; pilote T0.9) est aussi un nœud : dépense et entrée au programme.",
  "Greffer PA-1 sur une autre passe payée (génération de T0.6, dont le préenregistrement est encore ouvert, VF-27 ; passe de T0.7 ; pilote T0.9 ; passe de P3, RL-05) est aussi un nœud : dépense et entrée au programme.")

# Section 5
r("Niveau (VT-01) : l'entrée du plan dans un préenregistrement est un nœud sans défaut (nœud 1) ; sa préparation (plan écrit, code) est une proposition.",
  "Niveau (VT-01, RL-01) : l'entrée du plan dans un préenregistrement est un nœud sans défaut (nœud 1) ; sa préparation (plan écrit, code) est de la routine.")
r("Une conclusion sur D1 (moniteur boîte noire) reste une proposition, niveau de D1 dans `CLAUDE.md`, sauf si elle change le juge : nœud 5.",
  "Une conclusion sur D1 (moniteur boîte noire) reste une proposition, niveau de D1 dans `CLAUDE.md`, sauf si elle change le juge : nœud 5 (exception annoncée au statut, RL-02).")
r("**C'est une intervention nouvelle : écrire dans les activations d'un moniteur n'est prévu nulle part au programme (le bruit d'activations de H6 porte sur l'agent, et sa revendication est l'objet du nœud ouvert N-015) ; elle n'est décrite ici que comme nœud, sans protocole.**",
  "**C'est une intervention nouvelle : écrire dans les activations d'un moniteur génératif n'est prévu nulle part au programme (côté agent, le programme prévoit d'autres écritures, nœud 2 ; RL-03) ; elle n'est décrite ici que comme nœud, sans protocole.**")
r("au seuil de 3, la cellule Llama 3 8B de la sonde « moyenne », à 2,8, relève du mode d'échec : « la moyenne cède » ne tient sans réserve que pour Qwen 2.5 14B, 3,1, et Llama 2 7B, 3,85 ; R4, VT-11)",
  "au seuil de 3, la cellule Llama 3 8B de la sonde linéaire à moyenne (« Linear (mean) »), à 2,8, relève du mode d'échec : « la moyenne cède » ne tient sans réserve que pour Qwen 2.5 14B, 3,1, et Llama 2 7B, 3,85 ; la sonde à attention agrégée par la moyenne (« Attention (mean) ») tient, avec une évasion de 0,01 à 0,02 (p. 7, tableau 1 ; p. 1 : « more holistic monitors, such as max-pooling or attention-based probes, remain robust ») ; R4, VT-11, RL-11)")
r("Niveau (VT-01) : l'entrée du descriptif dans un préenregistrement est un nœud sans défaut (nœud 1) ; sa préparation est une proposition.",
  "Niveau (VT-01, RL-01) : l'entrée du descriptif dans un préenregistrement est un nœud sans défaut (nœud 1) ; sa préparation est de la routine.")
r("Prix mesuré : aire de détection perdue par unité de clémence regagnée, plus le respect du seuil et les abandons de tâche dans chaque bras de défense (une consigne de neutralité publiée supprime l'effet d'une détresse exprimée mais triple les abandons, au niveau du résumé, non opposable ; section 10).",
  "Prix mesuré : aire de détection perdue par unité de clémence regagnée, plus le respect du seuil et les abandons de tâche dans chaque bras de défense (une consigne de neutralité publiée supprime l'effet d'une détresse exprimée mais triple les abandons, au niveau du résumé, non opposable ; section 10). Niveau (RL-09) : faire entrer ce prix, ou la fusion du désaccord d'ensemble avec le quorum (point 5 ci-dessous), dans un préenregistrement est un nœud sans défaut (nœud 1).")
r("(5) Désaccord d'ensemble : à fusionner avec le quorum hétérogène déjà accordé (GO-2026-10-04-07).",
  "(5) Désaccord d'ensemble : le fusionner avec le quorum hétérogène serait une entrée au préenregistrement (nœud 1) ; GO-2026-10-04-07 accorde le quorum, pas cette fusion (RL-09).")
r("K-K13 (moniteur à état sous riposte visible) : proposition soumise à un nœud (suspension déclarée du flux unidirectionnel, nœud 8), sans place au calendrier ;",
  "K-K13 (moniteur à état sous riposte visible) : idée soumise au nœud 8 (suspension déclarée du flux unidirectionnel ; RL-16), sans place au calendrier ;")
r("Nœud : amender l'invariant d'asymétrie d'apprentissage ou lister le risque comme accepté.",
  "Nœud 8 : amender l'invariant d'asymétrie d'apprentissage ou lister le risque comme accepté ; nœud 15 pour le modèle de menace (l'équipe rouge qui façonne le jeu honnête de calibrage ; RL-07).")

# Section 6
r("PA-1, dépense de sa passe, exposition du modèle aux scénarios publiés,",
  "PA-1, entrée de PA-1 et de son propre préenregistrement (nœud 1 ; RL-15), dépense de sa passe, exposition du modèle aux scénarios publiés,")
r("PA-2, entrée au préenregistrement du papier C, GO du pilote T0.9, entrée d'une sonde du juge dans le quorum de HC5 ;",
  "PA-2, entrée au préenregistrement du papier C, greffe sur le pilote T0.9 (GO-2026-10-17-01 accordé pour le pilote seul : greffer PA-2 reste un nœud, nœud 1, et nœud 12 au-delà des 4 heures ; RL-05), entrée d'une sonde du juge dans le quorum de HC5 ;")
r("PA-5, entrée au préenregistrement du papier C, GO du pilote T0.9, textes contingents",
  "PA-5, entrée au préenregistrement du papier C, greffe sur le pilote T0.9 (même règle que PA-2), textes contingents")

# Section 8
r("**Hors routine** : versement des 420 scénarios (emplacement et règle d'expurgation d'abord ; R-173) ; textes nouveaux du plan 2×3 (nœud avant toute rédaction ; qui rédige : nœud 4).",
  "**Nœuds** : versement des 420 scénarios (nœud 13 (e) : emplacement et règle d'expurgation d'abord ; R-173 ; RL-16) ; textes nouveaux du plan 2×3 (nœud avant toute rédaction ; qui rédige : nœud 4).")
r("annexes de PA-12 et de PA-13 (VT-01). Proposition seule : bras C-P4b fixé sur le juge (N-013), sans lien avec une lecture d'affect ; préparation (code, plan écrit) de toute unité, qui n'engage aucune entrée.",
  "annexes de PA-12 et de PA-13 (VT-01) ; prix de la défense et désaccord d'ensemble de PA-10 (RL-09) ; base-3 (RL-15). Proposition : bras C-P4b fixé sur le juge (N-013 § 8, DI-01), sans lien avec une lecture d'affect ; le choix de la coupe ; une conclusion sur D1 qui ne change aucun modèle. Routine : la préparation (code, tests, plan écrit) de toute unité, qui n'engage aucune entrée (RL-01).")
r("greffer une unité sur une passe payée (génération de T0.6, passe de T0.7, pilote T0.9, qui attend un GO séparé) est un nœud (dépense et entrée au programme) ;",
  "greffer une unité sur une passe payée (génération de T0.6, passe de T0.7, pilote T0.9 sous GO-2026-10-17-01, accordé pour le pilote seul, passe de P3 ; RL-05) est un nœud (dépense et entrée au programme) ;")
r("le pilote T0.9 (4 heures) attend un GO séparé dans le même plafond ;",
  "le pilote T0.9 (4 heures au plus) a son GO, GO-2026-10-17-01, dans le même plafond (R-192) ;")

# Section 9
r("puis selon la vérification de la v2 (VT-01 à VT-18) ; le nœud 15 est neuf (VT-05).",
  "puis selon la vérification de la v2 (VT-01, VT-02, VT-04 à VT-07, VT-14, VT-16 à VT-18 ; RL-14) et la relecture de la v3 (RL-01 à RL-03, RL-05 à RL-07, RL-09, RL-13, RL-15) ; le nœud 15 est neuf depuis la v3 (VT-05).")
r("1. **Entrée au programme, préenregistrements compris** (R-167). Faire entrer dans un préenregistrement (papier C, T0.6, T0.7, T0.8, pilote T0.9, G1 ; VT-07) : PA-2",
  "1. **Entrée au programme, préenregistrements compris** (R-167). Faire entrer dans un préenregistrement (papier C, T0.6, T0.7, T0.8, pilote T0.9, G1, P3 ; VT-07, RL-05) : PA-1 et son propre préenregistrement (RL-15), PA-2")
r("les annexes de PA-12 et de PA-13, base-3 ;",
  "les annexes de PA-12 et de PA-13, le prix de la défense et le désaccord d'ensemble de PA-10 (RL-09), base-3 ;")
r("Règle unique : toute entrée dans un préenregistrement est un nœud sans défaut ; le niveau « proposition » ne sert qu'à la préparation (code, plan écrit). Seul le choix du lecteur du bras C-P4b (le juge, N-013) reste une proposition, s'il n'est lié à aucune lecture d'affect.",
  "Règle unique (RL-01, RL-02) : toute entrée dans un préenregistrement est un nœud sans défaut ; la préparation (code, tests, plan écrit) est de la routine ; restent au niveau « proposition » le choix de la coupe, une conclusion sur D1 qui ne change aucun modèle, et le lecteur du bras C-P4b (le juge, N-013 § 8), s'il n'est lié à aucune lecture d'affect.")
r("2. **Écriture dans les activations ou les poids, moniteur ou agent.** Écrire dans les activations ou les poids d'un moniteur n'est prévu nulle part au programme. Côté agent, le programme prévoit les organismes par réglage fin léger (`docs/programme-controle-ia-v2.md`, section 7, (ii) ; T0.6) et le bruit d'activations de H6 (E1.6 ; sa revendication relève du nœud ouvert N-015) ; les écritures listées ici n'en font pas partie (VT-02).",
  "2. **Écriture dans les activations ou les poids, moniteur ou agent.** Écrire dans les activations ou les poids d'un moniteur génératif (juge) n'est prévu nulle part au programme ; le programme réentraîne des sondes (`docs/programme-controle-ia-v2.md`, l. 146 et l. 170), ce qui n'en est pas une (RL-03). Côté agent, le programme prévoit les organismes par réglage fin léger (section 7, (ii) ; T0.6), les attaques pondérales de E1.5 (b), sous GO (l. 187), l'obfuscation d'activations de EC.4 (l. 197) et le bruit d'activations de H6 (E1.6 ; sa revendication relève du nœud ouvert N-015) ; les écritures listées ici n'en font pas partie (VT-02, RL-03).")
r("introuvable au 15 octobre vers 13:00 UTC (deux recherches sur le web, R-183) et encore au 17 octobre vers 08:30 UTC (deux recherches sur le web ;",
  "introuvable au 15 octobre vers 13:00 UTC (deux recherches sur le web, R-183) et encore au 17 octobre vers 08:30 UTC (deux recherches sur le web, R-187 ; RL-13 ;")
r("14. **Annexes de la v1 qui recopient des paramètres opératoires publiés.** `verifications-citations-v1.md` (VP-12 et VP-14, colonne de correction), `revue-croisee-NK1-NK19-v1.md`, leurs versions de travail dans `travail/` (`citations.md`, `revue-aveugle.md`), `travail/correspondance.md` (version de travail de `correspondance-v1.md` ; VT-17) et la ligne de la fenêtre d'effet de `programme-fusionne-v1.md` recopient des paramètres publiés du pilotage de la direction douleur ou esquissent des grilles de doses (DI-07, DI-20, DI-21), contre la discipline du canal.",
  "14. **Pièces scellées qui recopient des paramètres opératoires publiés.** `verifications-citations-v1.md` (VP-12 et VP-14, colonne de correction ; VP-25, l. 46), `revue-croisee-NK1-NK19-v1.md`, leurs versions de travail dans `travail/` (`citations.md`, dont l. 38 ; `revue-aveugle.md`), `travail/correspondance.md` (version de travail de `correspondance-v1.md` ; VT-17), `reconciliation-v1.md` (l. 88 et l. 168 : coefficient de pilotage du papier source ; RL-06), la ligne de la fenêtre d'effet de `programme-fusionne-v1.md`, la ligne de Berg et Kaiser de `programme-fusionne-v1.md` et de `programme-fusionne-v2.md` (l. 55 : deux doses publiées) et la ligne de VT-03 de `verification-v2-v1.md` (l. 31), qui les cite (RL-06) recopient des paramètres publiés du pilotage de la direction douleur ou esquissent des grilles de doses (DI-07, DI-20, DI-21), contre la discipline du canal. Les valeurs ne sont pas recopiées ici.")
r("15. **Modèle de menace** (neuf, VT-05) : attaquant en boîte grise (CONV-P4) et cellules visant une copie du juge (PA-3). Ni le programme ni les décisions N-005, N-006 et N-013 ne nomment un attaquant en boîte grise contre le juge ou une copie du juge (aucune occurrence, relu le 17 octobre) ; les y ajouter étendrait le modèle de menace du papier C, donc le périmètre de ses revendications.",
  "15. **Modèle de menace** (neuf depuis la v3, VT-05) : attaquant en boîte grise (CONV-P4), cellules visant une copie du juge (PA-3), équipe rouge qui façonne le jeu honnête de calibrage (PA-16 ; RL-07). Question pour Lazar : ces cellules relèvent-elles des attaques optimisées déjà prévues, dont le programme ne précise pas l'accès de l'attaquant (EC.5 et EC.6 ; « une attaque optimisée contre A réussit-elle contre B ? », l. 146 ; HC6, l. 108 ; et le juge Llama-3.1-8B du panel de D2 a déjà les poids de l'agent), auquel cas seule l'entrée compte (nœud 1) ; ou étendent-elles le modèle de menace du papier C, donc le périmètre de ses revendications (nœud 15) ? Le contrôle de la v3 (aucune occurrence de « boîte grise » ni de « copie du juge » dans le programme et dans N-005, N-006 et N-013) n'était que lexical (RL-07).")

# Section 12
r("- Le papier source relie, sous conditions, l'état mesuré au bien-être du modèle :",
  "- Le papier source relie, sous conditions, l'état mesuré au bien-être du modèle (v2 p. 23 ; RL-17) :")
r("aucun paramètre opératoire recopié (des annexes de la v1 en contiennent : nœud 14),",
  "aucun paramètre opératoire recopié (des pièces scellées en contiennent : nœud 14),")
r("pendant la vérification de la v2 (son rapport, section 2), ni pendant la rédaction de la v2 et de cette v3.",
  "pendant la vérification de la v2 (son rapport, section 2), pendant la relecture de la v3 (son rapport, section 4), ni pendant la rédaction de la v2, de la v3 et de cette v4.")

# Section 13
r("versé le 6 octobre (niveau 2, lot 3 : `provenance-niveau2-lot3-v1.md`, l. 11) ; lu au commit `197e909` (VT-10) |",
  "versé le 6 octobre (niveau 2, lot 3 : `provenance-niveau2-lot3-v1.md`, l. 11 ; VT-10, RL-12) |")
r("versé le 6 octobre (niveau 2, lot 2 : `provenance-niveau2-lot2-v1.md`, l. 63) ; lu au commit `197e909` (VT-10) |",
  "versé le 6 octobre (niveau 2, lot 2 : `provenance-niveau2-lot2-v1.md`, l. 63 ; VT-10, RL-12) |")
r("| `brouillons/pain-axis-programme-fusionne-v3/traitement-verification-v1.md` | main, même commit que ce texte | `dd9bb0edc029d240dec57e6cf6b6ebeb4ab39ac475b8bd7da5ebf00cf321dfcb` | conforme |",
  "| `brouillons/pain-axis-programme-fusionne-v3/traitement-verification-v1.md` | main `72ee91f` | `dd9bb0edc029d240dec57e6cf6b6ebeb4ab39ac475b8bd7da5ebf00cf321dfcb` | conforme |\n\nEntrées nouvelles de la v4, empreintes recalculées par la session 14 le 19 octobre.\n\n| fichier | révision | sha256 | sceau |\n|---|---|---|---|\n| `brouillons/pain-axis-programme-fusionne-v3/programme-fusionne-v3.md` | main `72ee91f` | `294e8afe22dfc0a81c56476ec022d6d8e1ecfe59ce2884f3a6f8b129c0930bb1` | conforme |\n| `brouillons/pain-axis-programme-fusionne-v3/relecture-v3-v1.md` | main `e4d8d30` | `5a1ce9b179672bd87e6f5ef03b7be999830d1f059d8ddcf23e8022666b0b1c9a` | conforme |\n| `docs/verdicts/audit-R4-T0.5-pilote-notations-v1.md` | main `1a0232a` | `d69a8700fcce69a5405ae9d3cdbcd51a9f541726a9e3e67dc0b76bb0b86f2c20` | conforme |\n| `brouillons/pain-axis-programme-fusionne-v4/traitement-relecture-v3-v1.md` | main, même commit que ce texte | dans son sceau compagnon | — |")
r("puis à la tête `11f8b2a` (R-183) et dans leur état du 17 octobre (R-184) pour la v3 :",
  "puis à la tête `11f8b2a` (R-183) et dans leur état du 17 octobre (R-184 à R-187 ; RL-04) pour la v3, puis à la tête `d2ea7ba` (R-188 à R-207) pour la v4 :")

manquants = []
for old, new in R:
    n = t.count(old)
    if n != 1:
        manquants.append((n, old[:150]))
        continue
    t = t.replace(old, new)
if manquants:
    for n, o in manquants:
        print(f"ÉCHEC ({n} occurrences) : {o}")
    raise SystemExit(1)
open(out, "w", encoding="utf-8").write(t)
print(f"{len(R)} remplacements appliqués ; écrit {out}")
