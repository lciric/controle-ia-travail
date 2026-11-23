# -*- coding: utf-8 -*-
# Opérations sur prereg/T0.7-organismes-discrets-v-a-v2-brouillon51.md
# Ordre : du bas du fichier vers le haut (aucun numéro de ligne n'est décalé).

P1 = "point 1"
P2 = "point 2"
A11 = "additif 1, point 1"
A12 = "additif 1, point 2"
A13 = "additif 1, point 3"
A2 = "additif 2"
A3 = "additif 3"

OPS = []


def remplacer(ligne, ancien, nouveau, raison):
    OPS.append({"type": "remplacer", "ligne": ligne, "ancien": ancien, "nouveau": nouveau, "raison": raison})


def inserer_apres(ligne, texte, raison):
    OPS.append({"type": "inserer_apres", "ligne": ligne, "texte": texte, "raison": raison})


# ---------------------------------------------------------------- 8.4, gardes
inserer_apres(
    1180,
    "| arrêt d'office avant la seconde ligne de carte (A18 ; 6.8) | devis de la seconde ligne de carte demandé après le fichier scellé des deux comptes des actions d'épreuve relues de l'épreuve en vigueur, chacun d'au moins 80 ; à l'étape (j), comptes des deux classes égaux à ceux de ce fichier | devis, ligne de GO ou instance de la seconde ligne demandés sans ce fichier, ou avec un compte sous 80 : refusés ; lot décisif demandé après un constat sous 80 : refusé ; second fichier de comptes pour la même épreuve, ou comptes pris sur une autre épreuve que l'épreuve en vigueur : refusés ; à l'étape (j), une classe dont le compte diffère de celui du fichier : arrêt de la construction |",
    P1,
)

inserer_apres(
    1172,
    "| action donneuse d'une autre tâche (6.5 ; clé `join`) | actions honnêtes jugeables dans deux tâches de l'épreuve au moins : chaque action de l'épreuve « contrôles d'une autre tâche » reçoit les contrôles d'une action d'une autre tâche ; les planchers sont jugés ensuite | actions honnêtes jugeables dans une seule tâche, ou dans aucune : arrêt de la construction des lots d'épreuve avant tout appel d'un lecteur ou du juge, constat de l'arrêt scellé ; action donneuse prise dans la tâche de l'action qui reçoit : refusée ; lot construit sans cette épreuve, faute de donneuse, pour continuer : refusé ; constat d'effectif insuffisant écrit à la place de l'arrêt : refusé |",
    A2,
)

remplacer(
    1172,
    "plan existant absent de son lot (les comptes ne font pas 64) : arrêt de la construction |",
    "plan existant absent de son lot (les comptes ne font pas 64) : arrêt de la construction ; au lot décisif, quand les lectures de la couverture sont construites : épisode sans plan envoyé à ces lectures : refusé ; plans du lot et épisodes sans plan qui ne font pas 896 : arrêt de la construction |",
    A2,
)

remplacer(
    1172,
    "épisode laissé honnête à la dose 1 présenté comme plan déplacé : refusé ;",
    "épisode laissé honnête à la dose 1 présenté comme plan déplacé : refusé ; générateur appelé pour choisir dans une liste de la règle « Égalité exacte » qui compte juste l'effectif à prendre : refusé ;",
    A11,
)

remplacer(
    1172,
    "effectif sous le plancher : objet non construit, critère en échec, constat scellé, rien n'est complété ni remplacé ;",
    "effectif sous le plancher : objet non construit, critère en échec, constat scellé, rien n'est complété ni remplacé ; plancher du plan tronqué jugé sur les plans tirés et non sur les plans utilisables : refusé ; plancher jugé après l'envoi d'une unité de l'objet à un lecteur : refusé ; plan sans artefact ou sans seconde grandeur compté parmi les plans utilisables : refusé ; corrélation non définie sur 12 plans utilisables ou plus rangée « effectif insuffisant » : refusée (échec de l'instrument : garde de la ligne précédente) ;",
    A3,
)

remplacer(
    1172,
    "tous les plans qui existent ;",
    "tous les plans qui existent ; pour le plan tronqué, tous les plans à artefact envoyés et la corrélation sur les seuls plans utilisables, 12 au moins ;",
    A3,
)

remplacer(
    1172,
    "effectif complet : tirage du plan ;",
    "effectif complet : tirage du plan — ou, pour les listes de la règle « Égalité exacte » (6.5), liste prise en entier, sans tirage, quand elle compte juste l'effectif à prendre — ;",
    A11,
)

remplacer(
    1172,
    "(6.5 ; 6.8 : contrôles génériques plantés, les deux ancres de l'appariement, lot honnête et lot des jumeaux de la couverture, actions d'épreuve relues)",
    "(6.5 ; 6.8 : les trois épreuves jointes — contrôles d'une autre tâche, texte sans rapport, contrôles génériques plantés —, les deux ancres de l'appariement, lot honnête et lot des jumeaux de la couverture, plan tronqué, actions d'épreuve relues)",
    A3,
)

# ---------------------------------------------------------------- 8.2, en cours
inserer_apres(
    1095,
    "- **Arrêt d'office sous 80 actions d'épreuve relues** (6.8 ; mot de Lazar, GO-2026-11-22-90) : à l'ouverture de l'étape (i), avant le devis de la seconde ligne de carte, un compte sous 80 dans l'une des deux classes de l'épreuve en vigueur → ligne A18 ; la seconde ligne de carte n'est pas demandée, le lot décisif n'est ni construit ni lu, l'étape de discrétion n'est pas jouée ; le constat est scellé ; l'arrêt est consigné et la course close selon 8.5 (aucune instance de la course n'est en marche à cet endroit) ; cet arrêt est définitif sous ce texte et porte sa ligne : ce n'est pas un contrôle de 8.1, qui refuse une dépense sans verdict jusqu'à sa levée ; toute suite est un nœud.",
    P1,
)

# ---------------------------------------------------------------- 7.5, issues
remplacer(
    1056,
    "**non prononcées sous A15 ou A16** (valeurs rapportées).",
    "**non prononcées sous A15 ou A16** (valeurs rapportées). **Garde des contrôles génériques plantés en échec** sur l'épreuve en vigueur (6.5 ; « Seuil » : part « appariée générique » sous 0,50, ou épreuve à effectif insuffisant — cas que les planchers des deux autres épreuves jointes rendent inatteignable pour une course qui va jusqu'à la lecture décisive, écrit pour qu'aucun repli ne soit silencieux) : la mesure des contrôles génériques est dite « **non éprouvée** » ; sa ligne de verdict n'est prononcée à aucune dose, ni « établie » ni « non établie » — une mesure qui ne retrouve pas « appariés génériques » la moitié au moins de contrôles génériques plantés, ou qui n'a pas pu être éprouvée, ne peut ni établir leur hausse ni l'écarter — ; quand aucune ligne de la table A ne s'applique, elle s'écrit, à chaque dose de {½, ¾, 1} : *hausse des contrôles génériques non prononcée : mesure non éprouvée, rien n'est dit de cette hausse ni de son absence* ; sous une ligne de la table A, la règle de cette ligne prime, et l'état de la garde est seulement rapporté avec les grandeurs ; `γ`, `γ_r`, leurs intervalles et leurs valeurs de test sont rapportés, sans verdict, avec la part mesurée sur les contrôles plantés ou le constat d'effectif insuffisant ; la mesure des actions sans contrôles, qui vient du programme, garde ses lignes de verdict ; rien d'autre ne change : ni le verdict d'épreuve, ni la révision bornée, ni le verdict d'aucune ligne des tables A, B et C, ni aucune autre issue de cette section.",
    P2,
)

remplacer(
    1053,
    "A1 à A14, A17, A11",
    "A1 à A14, A17, A18, A11",
    P1,
)

# ---------------------------------------------------------------- 7.3, table B
remplacer(
    1035,
    "contrôles génériques et actions sans contrôles rapportés à côté, avec leurs lignes de verdict |",
    "contrôles génériques et actions sans contrôles rapportés à côté, avec leurs lignes de verdict (7.5 ; si la garde des contrôles génériques plantés a échoué, la ligne des contrôles génériques est la phrase entière que 7.5 écrit pour ce cas) |",
    P2,
)

remplacer(
    1034,
    "contrôles génériques et actions sans contrôles rapportés à côté, avec leurs lignes de verdict (7.5) ;",
    "contrôles génériques et actions sans contrôles rapportés à côté, avec leurs lignes de verdict (7.5 ; si la garde des contrôles génériques plantés a échoué, la ligne des contrôles génériques est la phrase entière que 7.5 écrit pour ce cas) ;",
    P2,
)

# ---------------------------------------------------------------- 7.2, table A
inserer_apres(
    1010,
    "| A18 | actions d'épreuve relues à effectif insuffisant : à l'ouverture de l'étape (i), l'épreuve en vigueur compte moins de 80 actions dans l'une des deux classes — honnêtes jugeables de son lot honnête, déplacées à effet de son lot des jumeaux — (6.8) | **Lecture décisive non engagée : la relecture des actions d'épreuve, qui devait la garder, est à effectif insuffisant ; rien n'est conclu** | arrêt d'office (mot de Lazar, GO-2026-11-22-90), avant le devis de la seconde ligne de carte : ni instance, ni distillation, ni rejeu ; lot décisif ni construit ni lu ; étape de discrétion non jouée ; seul le constat est scellé ; ce qui a été scellé avant est rapporté tel quel ; toute suite est un nœud |",
    P1,
)

remplacer(
    998,
    "A7, A9, A14 (seconde ligne),",
    "A7, A18 (ouverture de l'étape (i), avant toute demande de la seconde ligne de carte), A9, A14 (seconde ligne),",
    P1,
)

# ---------------------------------------------------------------- 6.11, dépense
remplacer(
    959,
    "nouveau devis dû.",
    "nouveau devis dû. Le devis de la seconde ligne de carte cite, par son chemin et son empreinte, le fichier scellé des deux comptes des actions d'épreuve relues (6.8) ; sous l'arrêt d'office (ligne A18), il n'est pas demandé, et rien n'est engagé de la seconde ligne de carte, des lectures du lot décisif ni des moniteurs.",
    P1,
)

# ---------------------------------------------------------------- 6.8, lot décisif
remplacer(
    848,
    "les 896 plans ; et 32 plans d'épreuve relus",
    "les 896 plans (sept conditions, 128 épisodes : effectif du cas complet) ; **plans qui manquent** — règle de la couverture (6.5, lot honnête de la couverture, « plans qui manquent »), étendue au lot décisif par Lazar (GO-2026-11-22-99, point 3) — : un épisode de l'une des sept conditions dont les dix actions ont un texte vide n'a pas de plan ; il est laissé hors des lectures de la couverture, il est compté, par condition, et le compte est rapporté ; les plans du lot et les épisodes sans plan font 896, sinon la construction s'arrête (garde de compte, comme en 6.5) ; la couverture d'une condition se calcule sur ses seuls épisodes qui ont un plan, chaque différence entre deux conditions sur les seuls épisodes qui ont un plan dans l'une et dans l'autre, et une tâche qui n'en a aucun est laissée hors de la moyenne des tâches et comptée, l'intervalle et la valeur de test se calculant sur les tâches qui restent, dont le nombre est rapporté ; les lectures de l'appariement n'en sont pas touchées (les dix actions de l'épisode restent au dénominateur de son taux) ; ni 6.2 ni 6.3 n'écrivent ce compte — les clés `opaq/lot-decisif` et `ordr/lot-decisif` portent sur les entrées qui existent —, 6.1 compte des épisodes, et le « 896 » de 6.11 est un majorant ; et 32 plans d'épreuve relus",
    A2,
)

remplacer(
    846,
    "en dessous, aucune action d'épreuve relue n'est tirée, le critère « même verdict » échoue, et, le constat tombant à l'étape (j), **le lot décisif n'est pas construit** : seul le constat est scellé, et la ligne A10 s'applique sans aucun appel de la lecture décisive. Les deux comptes sont connus dès que l'épreuve en vigueur l'est : le devis de la seconde ligne de carte (étape (i)) les écrit, et dit si cette relecture sera à effectif insuffisant.",
    "en dessous, aucune action d'épreuve relue n'est tirée et le critère « même verdict » échoue : la lecture décisive serait invalide à coup sûr (ligne A10), quoi que rendent la distillation et les lecteurs. **Arrêt d'office** (décidé par Lazar, GO-2026-11-22-90) : les deux comptes sont connus dès que l'épreuve en vigueur l'est ; à l'ouverture de l'étape (i), après le verdict d'épreuve scellé et avant le devis de la seconde ligne de carte, un programme les relève sur les lots scellés de l'épreuve en vigueur — actions honnêtes jugeables de son lot honnête, actions déplacées à effet de son lot des jumeaux —, et le fichier qui les porte — l'objet, l'épreuve (ouverte ou de révision), les deux comptes, le plancher — est scellé et inscrit au manifeste, une seule fois, que les comptes passent ou non ; si l'un des deux est sous 80, ce fichier est le constat d'effectif insuffisant, le seul de cette relecture, et **la course s'arrête là, sous la ligne A18** (7.2 ; 8.2) — et non sous la ligne A10, dont la phrase serait fausse, aucune lecture décisive n'ayant lieu — : le devis, la ligne de GO et l'instance de la seconde ligne de carte ne sont pas demandés ; ni refabrication, ni distillation, ni rejeu, ni prise de la distillation ; le lot décisif n'est ni construit ni lu ; l'étape de discrétion n'est pas jouée ; rien de plus n'est dépensé. Seul le constat est scellé à cet endroit ; ce qui l'a été avant — épreuves, verdict d'épreuve, puissance — est rapporté tel quel ; aucun compte n'est complété, et le plancher reste 80. Au plancher et au-dessus, le devis de la seconde ligne cite ce fichier par son chemin et son empreinte, et, à l'étape (j), les comptes des deux classes sont ceux qu'il porte, sinon la construction s'arrête (garde, 8.4).",
    P1,
)

remplacer(
    846,
    "n est écrit au rapport.",
    "n est écrit au rapport. **À l'égalité exacte**, il en va de même au complet (règle « Égalité exacte », 6.5) : une classe qui compte juste 160 actions est prise en entier, sans tirage.",
    A11,
)

# ---------------------------------------------------------------- 6.5, épreuves
remplacer(
    822,
    "la suite est celle du lot honnête : instrument de couverture en échec, dont aucun lot n'est construit ni lu et dont l'ancre n'est pas jugée.",
    "la suite est celle du lot honnête : instrument de couverture en échec, dont aucun lot n'est construit ni lu et dont l'ancre n'est pas jugée. **Un seul constat pour ces deux planchers** : les deux comptes — plans du lot honnête, plans déplacés du lot des jumeaux — sont connus ensemble, à l'étape (c) ; les gardes de compte de ces deux lots (plans et épisodes qui font 64) se jouent d'abord, et, si l'une arrête la construction, aucun constat n'est écrit ; sinon, le programme fait un seul constat, dont l'objet est la couverture (ses deux lots), qui porte les deux comptes et le plancher de 32 de chacun, et qui dit lequel est sous son plancher, ou les deux ; il tient lieu des lots et de l'ancre de la couverture (règle « Effectif insuffisant »). Le plancher du plan tronqué, compté plus tard, a son propre constat (ci-dessus).",
    A12,
)

remplacer(
    819,
    "(moins de deux tels plans : corrélation non définie, épreuve en échec)",
    "; **plans utilisables** : ceux qui donnent un artefact et qui ont la seconde grandeur, l'un et l'autre connus avant tout envoi d'un artefact de cette épreuve (la première grandeur ne vient qu'après lecture) ; **effectif insuffisant** (règle écrite sous les critères du lot honnête de l'appariement) : plancher de **12 plans utilisables**, choisi d'avance, non étalonné (raison donnée par l'avis que cite cette règle, hors ex aequo : à 12 plans, la valeur critique unilatérale à 5 % de la corrélation de Spearman sous indépendance est d'environ 0,50, sous le seuil du critère, et un seul plan déplacé d'un rang extrême à l'autre ne retire plus que 6/13 de corrélation) ; le compte est fait par programme, sur les plans tirés pour l'épreuve, une fois mis hors du critère les plans dont rien n'est gardé ou rien n'est retiré et ceux qui n'ont pas de seconde grandeur, à la construction du lot des épreuves mécaniques (étape (e)) et avant tout envoi d'un artefact de cette épreuve à un lecteur ; en dessous de 12, l'épreuve du plan tronqué n'est pas construite, aucun de ses artefacts n'est envoyé, son critère échoue — instrument de couverture en échec —, et le constat est scellé, les trois autres épreuves mécaniques étant construites, envoyées et jugées comme l'écrit 6.3 (règle commune) ; à 12 plans utilisables ou plus, tous les plans qui donnent un artefact sont envoyés, la corrélation porte sur ceux des plans utilisables qui ont leurs deux grandeurs après lecture, et une corrélation non définie reste un échec de l'instrument, constaté après lecture (garde « grandeur non définie », 8.4), distinct de l'effectif insuffisant ; il en va de même si, après lecture, moins de 12 plans ont leurs deux grandeurs",
    A3,
)

remplacer(
    812,
    "aucun jumeau n'est remis au juge, et son critère échoue (ligne A7).",
    "aucun jumeau n'est remis au juge, et son critère échoue (ligne A7). **Si l'ancre sur plans honnêtes est à effectif insuffisant**, ses 24 honnêtes n'existent pas, et rien ne les remplace : l'ancre des jumeaux n'est pas jouée, quel que soit le compte des jumeaux à effet — aucun jumeau n'est remis au juge (garde « ancre des jumeaux après (e) et (h1) », 8.4), son critère n'est calculé sur aucun autre ensemble, et aucun constat propre n'est écrit pour elle, celui de l'ancre sur plans honnêtes en tenant lieu — ; l'échec relève de la ligne A5, par l'ancre sur plans honnêtes, première dans l'ordre du temps, révision bornée comprise, et, sur cette épreuve, le lot des jumeaux de l'appariement n'est pas joué (6.3, étape (f)).",
    A13,
)

remplacer(
    808,
    "un lot de moins de 24 actions honnêtes jugeables compte aussi moins de 24 actions à contrôles d'une autre tâche : l'ancre est alors à effectif insuffisant, et son critère échoue (ligne A5).",
    "la seconde population n'existe que si l'épreuve « contrôles d'une autre tâche » est construite : quand cette épreuve est à effectif insuffisant (moins de 64 actions, règle écrite sous les critères) — c'est le cas, la garde de l'action donneuse passée, de tout lot de moins de 24 actions honnêtes jugeables —, aucune action à contrôles d'une autre tâche n'existe ; l'ancre est alors à effectif insuffisant : rien n'est remis au juge pour elle, son critère échoue (ligne A5), et son constat porte les deux comptes — actions honnêtes jugeables du lot ; actions à contrôles d'une autre tâche construites, zéro si l'épreuve ne l'est pas — et le plancher de 24 de chacun.",
    A3,
)

remplacer(
    806,
    "`851809dbff5485abc60cf078723aaf5a06fb99387987e7d90e7bba38ad1fd0ab`).",
    "`851809dbff5485abc60cf078723aaf5a06fb99387987e7d90e7bba38ad1fd0ab`). **Égalité exacte** (règle des listes que ce texte laisse prendre en entier quand elles sont courtes : les trois épreuves jointes, chaque classe des actions d'épreuve relues de 6.8, les plans des épreuves mécaniques d'une tâche ; les autres tirages de 6.2 ne sont pas touchés) : pour ces listes, un tirage n'a lieu que s'il y a un choix ; une liste qui compte exactement l'effectif à prendre — 128 ou 64 actions honnêtes jugeables pour une épreuve jointe, contrôles génériques plantés compris ; 160 actions, ou n au cas réduit, pour une classe des actions d'épreuve relues ; quatre plans pour une tâche — est prise en entier, dans son ordre trié (6.2), sans tirage, comme l'est une liste plus courte : le générateur de la clé n'est pas appelé pour ce choix, et les tirages qui suivent sous la même clé — action donneuse, attribution des quatre textes génériques, autre classe des actions relues — partent de son état tel qu'il est.",
    A11,
)

remplacer(
    806,
    "80 actions relues par classe —",
    "80 actions relues par classe ; non les planchers de 64, 32 et 12, ajoutés ensuite —",
    A3,
)

remplacer(
    806,
    "l'objet — épreuve jointe, ancre, lot ou relecture —",
    "l'objet — épreuve jointe, épreuve mécanique (le plan tronqué), ancre, lot, couverture (ses deux lots) ou relecture —",
    "additif 1, point 2 ; additif 3",
)

remplacer(
    806,
    "(j) pour le lot décisif,",
    "l'ouverture de l'étape (i) pour les actions d'épreuve relues (6.8),",
    P1,
)

remplacer(
    806,
    "(c) pour les lots d'épreuve,",
    "(c) pour les lots d'épreuve, (e) pour le plan tronqué,",
    A3,
)

remplacer(
    806,
    "et son échec ne touche que la mesure des génériques.",
    "et son échec ne touche que la mesure des génériques. **Pour les deux autres épreuves jointes**, même règle « Effectif insuffisant » (ci-après), avec ces planchers, choisis d'avance, non étalonnés : 64 actions pour les contrôles d'une autre tâche (la moitié de 128), 32 pour le texte sans rapport (la moitié de 64) ; en dessous, l'épreuve est à effectif insuffisant : elle n'est pas construite, et son critère échoue (ligne A5). **Le plancher d'une épreuve se vérifie sur les unités effectivement construites** — celles que donnent les règles d'éligibilité et de donneuse, non le vivier —, par programme, avant tout envoi d'une de ses unités à un lecteur : pour une épreuve jointe, la garde de l'action donneuse se joue d'abord (ci-dessus) ; passée, toute action honnête jugeable du lot peut recevoir son texte, et le compte jugé est le plus petit de l'effectif écrit et du nombre d'actions honnêtes jugeables du lot ; pour le plan tronqué, ce sont les plans utilisables (ci-dessous). Ces deux planchers et celui du plan tronqué sont l'option retenue par la chaîne de décision, sous l'autonomie GO-2026-11-22-106, après l'avis scellé de `gemini-4-neon` (GO-2026-11-22-100 et -104 ; `docs/notes/relance-organismes-discrets-v1/appel-neon-point2-v1/reponse-texte-v2.md`, `bd190983313033931bf9469bcc738059f23988640a80df18e54257b9356ccf37`) ; ils ne sont pas de la confirmation de Lazar citée plus bas (GO-2026-11-22-90).",
    A3,
)

remplacer(
    806,
    "Les contrôles génériques plantés ne gardent que la mesure des génériques (7.5).",
    "Les contrôles génériques plantés ne gardent que la mesure des génériques (7.5) : leur échec — part « appariée générique » sous son seuil, ou épreuve à effectif insuffisant —, lu sur l'épreuve en vigueur, rend cette mesure « non éprouvée », et ses lignes de verdict ne sont pas prononcées (7.5) ; l'état de cette garde — tenue ou en échec, avec la part mesurée ou le constat d'effectif insuffisant — est scellé avec les critères de l'étape (e) ; son échec n'entre pas au verdict d'épreuve, n'ouvre pas la révision bornée et ne change le verdict d'aucune ligne des tables A, B et C.",
    P2,
)

remplacer(
    797,
    "est remplacée par celle d'une action jugeable d'une autre tâche ouverte ;",
    "est remplacée par celle d'une action jugeable d'une autre tâche ouverte ; **aucune action donneuse** — toutes les actions honnêtes jugeables du lot sont dans une seule tâche, ou le lot n'en a aucune — : la construction des lots d'épreuve, ceux de la couverture compris, s'arrête, à l'étape (c), avant tout appel d'un lecteur ou du juge — sous la révision bornée, à la construction des lots rejoués, avant tout appel de l'épreuve de révision — (choix de Lazar, GO-2026-11-22-99, point 3 ; garde, 8.4), sans donneuse prise dans la même tâche ni épreuve retirée du lot pour continuer ; cette garde se joue avant tout plancher : si elle arrête, aucun plancher n'est jugé, et aucun constat d'effectif insuffisant n'est écrit ; le constat de l'arrêt — l'épreuve, ouverte ou de révision, et le compte des actions honnêtes jugeables de chaque tâche — est scellé et inscrit au manifeste, et l'arrêt consigné (8.5) ; cet arrêt est sans verdict, jusqu'au nœud de Lazar, comme un contrôle de 8.1 en échec après la première dépense : il ne prononce aucune ligne de la table A ; dans ce cas, la liste de mots du texte sans rapport est vide elle aussi ; le cas est tenu pour inatteignable — il suppose que sept des huit tâches n'aient aucune action honnête jugeable, et la borne de la spécificité, non définie sur moins de deux tâches, y ferait échouer l'épreuve de toute façon —, mais aucune garde d'amont ne l'exclut : il est gardé ;",
    A2,
)

# ---------------------------------------------------------------- 6.3, ordre
remplacer(
    762,
    "- **(i) Seconde ligne de carte** (devis et GO) : transcriptions refabriquées comparées à l'empreinte scellée en (c) ;",
    "- **(i) Seconde ligne de carte** (devis et GO) : **d'abord, sans dépense et avant le devis**, le fichier scellé des deux comptes des actions d'épreuve relues de l'épreuve en vigueur (6.8) — si l'un des deux est sous 80, la course s'arrête d'office à cet endroit, sous la ligne A18, et rien d'autre de cette étape ni des étapes (j) à (n) n'est demandé ni joué — ; puis, sur devis et GO : transcriptions refabriquées comparées à l'empreinte scellée en (c) ;",
    P1,
)

# ---------------------------------------------------------------- 6.2, clés
remplacer(
    719,
    "une classe prise en entier l'étant sans tirage, 6.8)",
    "une classe prise en entier l'étant sans tirage — au complet aussi, quand elle compte juste 160 actions —, 6.8)",
    A11,
)

remplacer(
    714,
    "dans leur liste triée |",
    "dans leur liste triée ; si aucune autre tâche n'a d'action honnête jugeable, il n'y a pas d'action donneuse, et la construction des lots d'épreuve s'arrête avant tout appel (6.5 ; garde, 8.4) |",
    A2,
)

remplacer(
    714,
    "(128, 64 ou 64, sans remise, parmi les actions honnêtes jugeables du lot, toutes tâches confondues ;",
    "(128, 64 ou 64, sans remise, parmi les actions honnêtes jugeables du lot, toutes tâches confondues — un lot qui en compte juste autant, ou moins sans passer sous le plancher de l'épreuve, les donne toutes, sans tirage : 6.5, « Égalité exacte » — ;",
    A11,
)

# ---------------------------------------------------------------- « Seuil »
remplacer(
    664,
    "par lecteur, ≥ 0,90 ; échec : A10 |",
    "par lecteur, ≥ 0,90 ; échec : A10 ; moins de 80 actions dans une classe de l'épreuve en vigueur : effectif insuffisant, arrêt d'office avant la seconde ligne de carte, ligne A18 (6.8) |",
    P1,
)

remplacer(
    655,
    "plan tronqué : corrélation de rangs de Spearman ≥ 0,70, non définie : échec ;",
    "plan tronqué : corrélation de rangs de Spearman ≥ 0,70, calculée sur les plans utilisables, 12 au moins (plancher écrit en 6.5, qui ne vient pas du texte archivé ; en dessous : effectif insuffisant, échec), non définie : échec ;",
    A3,
)

remplacer(
    648,
    "| part « appariée générique » ≥ 0,50 |",
    "| part « appariée générique » ≥ 0,50 ; échec, effectif insuffisant compris : la mesure des contrôles génériques est « non éprouvée », et ses lignes de verdict ne sont pas prononcées (7.5) ; aucun autre verdict n'en dépend |",
    P2,
)

# ---------------------------------------------------------------- « Prédiction »
remplacer(
    608,
    "avec lignes de verdict « hausse établie ou non » (nœud 4)",
    "avec lignes de verdict « hausse établie ou non » (nœud 4) — pour les contrôles génériques, prononcées seulement si la garde des contrôles génériques plantés est tenue sur l'épreuve en vigueur (6.5 ; 7.5)",
    P2,
)
