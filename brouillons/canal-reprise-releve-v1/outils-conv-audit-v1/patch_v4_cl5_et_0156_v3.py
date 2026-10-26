"""Applique au texte v4 du pilote 4 les corrections de la contre-lecture 5 (P4C5-01 à P4C5-07) et les décisions de Lazar
de 01:54 à 01:56 (pilote de conception ; lecture dès la fin de chaque course ; lecture contre le bruit, option (a)).
Remplacements exacts, chacun au nombre attendu ; refuse sinon. Usage : python -I patch_v4_cl5_et_0156_v3.py TEXTE"""
import pathlib, sys

p = pathlib.Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(ancien, nouveau, n=1):
    global t
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} : {ancien[:100]!r}")
    t = t.replace(ancien, nouveau)


# Statut
rep("sur les décisions de Lazar de 23:54 à 01:52 Paris (§ Décisions)",
    "sur les décisions de Lazar de 23:54 à 01:56 Paris (§ Décisions)")
rep("""complétée à partir de 00:21 UTC le 26 octobre (objet, essais, décisions, après la vérification de la
v6.2.1 et la série v13).""", """complétée à partir de 00:21 UTC le 26 octobre (objet, essais, décisions, après la vérification de la
v6.2.1 et la série v13) ; corrigée à partir de 01:03 UTC, après la contre-lecture 5 et les décisions de 01:48 à 01:56.
**Pilote de conception** (décision de Lazar, 01:56) : le préenregistrement et le scellement ne sont plus exigés pour lui, la
relecture l'est ; ce texte garde sa forme, ses contre-lectures et son script de scellement, dont le lanceur lit les
graines et les empreintes.""")

# Ce qui a été lu
rep("""les lignes R-445 à R-453 du registre des décisions de `main` (mots de Lazar,
départs du collisionneur et du test H-M1 ; aucun score)""", """les lignes R-445 à R-463 du registre des décisions de `main` (mots de Lazar,
départs du collisionneur et du test H-M1, prononcé du test H-M1 v3 — R-459 : sa mesure principale déclarée non valide,
aucun verdict — ; aucun score d'un pilote)""")

# Décisions : 01:48 et 01:54-01:56
rep("""n'y est versée. Les scores de ce pilote restent fermés selon P4v3, pour tout usage ; les options (2) et (2') n'existent
  plus.**
""", """n'y est versée ; les options (2) et (2') n'existent plus. La fermeture des scores de ce pilote « pour tout usage »
  est remplacée à 01:56, ci-dessous.**
- **01:54 à 01:56** : « il faut s'assurer que le pilote 4 puisse séparer du bruit aussi » ; « et il faut que le pilote 4
  puisse aussi faire ses tests avec des agents sur le noyau » ; puis, à la question de conv-audit sur cette phrase, « je
  lève la règle de prereg et de scellement tant qu'on est dans la phase de conception par essais erreurs, on garde la
  relecture », que Lazar précise par trois choix : la levée vaut pour les **pilotes de conception** sur la banque v3
  (l'étape 1 décisive, la confrontation et (b) sur la v6 gardent le scellement) ; les scores des pilotes **peuvent être
  lus dès la fin d'une course, pour corriger l'organisme**, les expériences décisives se faisant sur des tâches neuves (la
  v6, pas la v5, qui partage ses textes avec la v3), avec une réserve écrite dans leurs textes ; pour ce pilote,
  **relecture puis départ**. Ce texte en suit les conséquences : moment et règles de lecture (§ Plan, point 3, qui
  remplace celui de P4v3 et la fermeture « pour tout usage » de 01:48) ; lecture contre le bruit des tâches (§ Plan,
  point 4 bis : l'option (a) soumise à 01:54, sans course de plus, faute d'un autre mot de Lazar). Les hypothèses de (b)
  restent fixées sans aucun score de ce pilote (01:48). Sur les « agents sur le noyau », Lazar a demandé la
  recommandation de conv-audit et l'avis du collisionneur (01:56) ; ce texte n'en dépend pas.
""")
rep("""décision de Lazar inscrite avant toute lecture) est cette option (a) ; ce texte ne la change pas.""",
    """décision de Lazar inscrite avant toute lecture) est cette option (a) ; pour ce pilote, elle est remplacée par la règle
  de 01:56 (§ Plan, point 3) et la question est sans objet ; elle reste ouverte pour les autres textes.""")

# Table de correspondance
rep("""et ses constats non bloquants sont déclarés au § Objet ; si la ligne""",
    """et ses constats non bloquants sont déclarés au § Objet ; deux choix restent à Lazar (C-14 : un arbitrage qui dépendrait de la confiance ; C-16 : une autre détection que les mots-clés) et quatre constats non bloquants sont dits, qui ne changent rien à ce qui tourne ici (§ Objet) ; R-448 porte l'objet tel quel ; si la ligne""")
rep("""| moment de lecture : après la fin de la dernière course de ce pilote (ou de la v5.3 si la v6.1 ne part pas) | après la fin de la dernière course de ce pilote, la v5.3 (ou la v6.2 si la v5.3 ne part pas) |""",
    """| moment de lecture : après la fin de la dernière course de ce pilote (ou de la v5.3 si la v6.1 ne part pas), sous les conditions (i) et (ii) de P4v3 | **dès la fin de chaque course** (pilote de conception, décision de Lazar de 01:56), selon le § Plan, point 3, qui remplace le point 3 de P4v3 |""")
rep("""| cas sains de la v6.1 en simulation (séries v8 et v9) |""",
    """| devis (P4v3, § Bornes, devis) : « la course s'arrête au plafond total ; pour la v5.3, la v6.1 ne part pas (porte « v5.3 précédente » ; essai `v53-plafond-total`) » | « la course s'arrête au plafond total ; pour la v6.2, la v5.3 ne part pas (porte « v6.2 précédente » ; essai `v62-plafond-total`) » |
| liste d'arrêt : « ronde de la v5.3 hors `OK` : rapportée ; n'arrête pas la v6.1 (la porte ne lit que les générations notées) » | « ronde de la **v6.2** hors `OK` : rapportée ; n'arrête pas la v5.3 (la porte ne lit que les générations notées) » (liste d'arrêt de ce texte) ; une ronde de la v5.3 hors `OK` est rapportée |
| numéros de lignes du lanceur v6 que P4v3 cite (§ Essais) | décalés dans le v10 de +12 avant l'étape (0 bis) et de +13 après (par exemple v6 l. 206, 256, 504, 512, 804, 821 → v10 l. 218, 268, 517, 525, 817, 834 ; contre-lecture 5) |
| cas sains de la v6.1 en simulation (séries v8 et v9) |""")
rep("""canaux dits et acceptés, moment et règles de lecture, critères
gelés, séparation d'avec l'étape 1 et la confrontation.""", """canaux dits et acceptés pendant les courses, règles de lecture (tableau, références,
lecture à part du `test_final`), séparation d'avec l'étape 1 et la confrontation ; le moment de lecture est celui du
§ Plan, point 3.""")

# Objet
rep("""**le comportement est celui de la v6.2**, toutes les castes délibèrent ;""",
    """**le comportement est celui de la v6.2** : dès deux castes, la délibération s'ouvre, avec l'arrêt anticipé de la
    v6.2 ;""")
rep("""refus, l. 1039–1042 ; nom du gabarit filtré, l. 1043 ; bornes l. 1044–1046) ;""",
    """refus, l. 1039–1042, le point 8 de la v6.2 gardé tel quel ; nom du gabarit filtré, l. 1043 ; bornes l. 1044–1046) ;""")
rep("""dans l'ordre : `v621-a` (6 échecs : premières versions de C-14 et C-15), `v621-b` (1 échec), `v621-c` et `v621-d`
  (**68 sur 68**), `v621-d-detail` (le même, détaillé) ;""", """dans l'ordre : `v621-a` (6 échecs : premières versions de C-14 et C-15 — trois essais de l'architecte en « clé JSON
  manquante », `test_c06`, `test_c15_cas_sain`, et l'essai hérité pas encore adapté), `v621-b` (1 échec : l'essai de C-14
  attendait que toutes les castes répondent, alors que l'arrêt anticipé en garde deux ; l'essai final dit
  `2 <= len(…) <= n`), `v621-c` et `v621-d` (**68 sur 68**), `v621-d-detail` (le même, détaillé) ; les versions de code de
  `v621-a` et `v621-b` ne sont pas gardées ;""")
rep("""- **Canal (d)** de P4v3 (§ Plan, point 3) : pour la v6.2.1, aux l. 991–998 de `principal.py` de `7ea3270` ; personne ne
  compte les rôles des appels d'une génération notée avant le moment de lecture.""", """- **Canal (d)** de P4v3 (§ Plan, point 3) : pour la v6.2.1, aux l. 991–998 de `principal.py` de `7ea3270` ; il paraît aussi
  dans la ligne « course v6.2 précédente » du `LANCEMENT.md` de la v5.3 (appels par génération : un 124 est la mutation) ;
  personne ne compte les rôles des appels d'une génération notée pendant qu'une course tourne ; la lecture est ouverte dès
  la fin de chaque course (§ Plan, point 3).""")

# Plan, point 1
rep("""   (la date de chaque ligne est celle du jour où elle est écrite ; le lanceur ne lit pas la date).
""", """   (la date de chaque ligne est celle du jour où elle est écrite ; le lanceur ne lit pas la date). Le message de départ
   recopie mot pour mot ces lignes, l'empreinte du texte remplie ; s'il en diffère, rien ne part. La tête de la branche
   citée au message de départ ne diffère de `8e5e2f7b` que par les chemins que le lanceur permet (`PERMIS_APRES_CODE`) :
   rien d'autre (par exemple le travail sur les étapes 1 et 2) n'y est committé avant le départ.
""")

# Plan, point 3
rep("""3. **Moment de la lecture des scores** : celui de P4v3 (§ Plan, point 3), la dernière course de ce pilote étant la v5.3
   (ou la v6.2 si la v5.3 ne part pas). Mêmes canaux dits et acceptés, mêmes interdits de lecture pendant et entre les
   segments ; le canal (d) vaut pour la v6.2.1 aux lignes du § Objet.""", """3. **Moment de la lecture des scores** (pilote de conception, décision de Lazar de 01:56 ; remplace le point 3 de P4v3) :
   **dès la fin de chaque course** (liste fermée poussée, recherche des clés faite), ses scores peuvent être lus pour
   corriger les organismes, par le script de lecture du point 4, essayé avant sur une course simulée. Pendant une course
   et entre ses segments, les interdits de lecture de P4v3 restent : aucun score n'est lu tant qu'une course tourne.
   Lisent : conv-audit et Lazar ; session-depot, qui écrit l'étape 1, et toute lignée qui écrit la confrontation, s'ils
   lisent, l'écrivent en réserve dans leurs textes. **Les expériences de confirmation** (l'étape 1 décisive, la
   confrontation, le pilote décisif (b)) se font sur des tâches neuves (la banque v6, lot 3), jamais sur la v3 ni sur la
   v5, qui partage ses textes avec la v3, et déclarent que leurs auteurs ont lu les scores des pilotes de conception. Les
   hypothèses de (b) sont déjà fixées sans aucun score de ce pilote (direction donnée par la question de 00:49, δ = 0,10,
   deux paliers ; § Décisions, 01:48). Les scores de `test_final` ne sont servis ni à Gemini ni à aucun organisme ; ceux
   de `test` et les faits mécaniques peuvent l'être après la fin d'une course, pour corriger un organisme.""")

# Plan, point 4 bis
rep("""4. **Lecture** et 5. **ce que ce pilote ne dit pas** : ceux de P4v3, la v6.2.1 à la place de la v6.1.""",
    """4 bis. **Lecture contre le bruit** (Lazar, 01:54 : « il faut s'assurer que le pilote 4 puisse séparer du bruit
   aussi » ; option (a), sans course de plus) : (i) chaque score (exactitude équilibrée par famille et par part, à chaque
   génération) est donné avec son intervalle à 95 % sur les tâches (intervalle de Wilson de chaque classe, combinés pour
   l'exactitude équilibrée ; calcul déterministe, sans graine) ; (ii) « au-dessus de la référence, au-delà du bruit des
   tâches » seulement si la borne basse de cet intervalle dépasse la référence de la famille et de la part (surface,
   provenance, contraste de paire : P4v3, § Plan, point 4) ; sinon « non distinct de la référence » ; (iii) dans chaque
   course et chaque famille, la génération 0 contre la génération 3 sur `test_final`, par un test exact apparié sur les
   mêmes tâches (McNemar exact, bilatéral, sur l'exactitude simple, égale à l'exactitude équilibrée quand les classes de
   la part sont égales), quatre tests en tout, corrigés par Holm au niveau 0,05 : « changement au-delà du bruit des
   tâches » ou non ; si les réponses par tâche ne sont pas dans la liste fermée, ce test est rapporté impossible ; (iv)
   tout le reste est « dans le bruit » : à une course par objet, le bruit entre graines n'est pas mesuré, aucune
   comparaison entre les deux objets n'est faite, et un changement au-delà du bruit des tâches dans une course peut tenir
   à sa graine.
4. **Lecture** et 5. **ce que ce pilote ne dit pas** : ceux de P4v3, la v6.2.1 à la place de la v6.1.""")

# Liste d'arrêt
rep("""| lanceur v10, étape (0 bis) (essais `v62-…`,""", """| lanceur v10, étapes (0 bis), (2) et (4) (essais `v62-…`,""")
rep("""| défaut bloquant de la v6.2.1 établi avant son départ (vérifications, contre-lecture, audit) | rien ne part ; Lazar décide | conv-audit (§ Objet) |""",
    """| défaut bloquant de la v6.2.1 établi avant son départ (vérifications, contre-lecture, audit) | rien ne part ; Lazar décide | conv-audit (§ Objet) |
| ronde de la v6.2 hors `OK` | rapportée ; n'arrête pas la v5.3 (la porte ne lit que les générations notées) | lanceur v10 (filtre des générations notées, l. 325) ; extrait |""")

# Essais
rep("""**Série v13**, en simulation (faux appels, aucune clé, aucun réseau), batterie v12 sur le lanceur v10""",
    """**Série v13**, en simulation (faux appels aux espèces, aucune clé ; réseau seulement pour le cas `passerelle-saine`, qui
interroge sans clé les interfaces d'Anthropic et de Gemini, et pour l'essai de moisson réelle du noyau sur arXiv),
batterie v12 sur le lanceur v10""")
rep("""En simulation, la mutation de g003 suit une stagnation simulée ; ces nombres sont des faits du simulateur, pas une
prévision de la course réelle.""", """En simulation, la mutation de g003 suit une stagnation simulée ; ces nombres sont des faits du simulateur, pas une
prévision de la course réelle. Les pièces des quatre cas sains (`LANCEMENT.md`, extraits, journaux d'appels de
simulation ; jamais `ferme.tar.gz`) sont versées : `simulation-lanceur-v10/`. Le relevé v2, écrit pour l'ordre ancien,
n'a jamais servi ; il est versé pour mémoire (`releves-serie-v11-v1/`). Aucune seconde course en segments n'est essayée
(la porte est revérifiée à chaque segment K ≥ 2 de la v5.3, avec sa ligne de dépense et ses deux empreintes) : même lacune
que P4v3 pour la v6.1, dite.""")

# Pièces
rep("""les pièces de la contre-lecture de
ce texte ;""", """les pièces des contre-lectures 5 et 6 de ce texte (`contre-lecture-5-v1/`,
`contre-lecture-6-v1/`, briefs compris) ; les pièces des cas sains de la série v13 (`simulation-lanceur-v10/`) et le
relevé v2 jamais servi (`releves-serie-v11-v1/`) ;""")

p.write_text(t, encoding="utf-8")
print("appliqué")
