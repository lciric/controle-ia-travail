"""Brouillon 4 -> brouillon 5 de l'additif : second lot (nœuds de Lazar, calendrier, lectures descriptives ajoutées).
Chaque ancien texte doit paraître exactement une fois ; sinon arrêt."""
import sys
from pathlib import Path

src = Path(sys.argv[1]); dst = Path(sys.argv[2])
t = src.read_text(encoding="utf-8")
M = "À " + "REMPLIR"


def r(old, new, n=1):
    global t
    c = t.count(old)
    if c != n:
        raise SystemExit(f"attendu {n}, trouvé {c} : {old[:90]!r}")
    t = t.replace(old, new)


# --- passages touchés
r("| tout le reste | inchangé | « Ce qui ne change pas » |",
  "| liste d'arrêt, ligne 15 ; « Hypothèse », « Ce que l'hypothèse ne dit pas » | « ce texte » s'y lit « le texte scellé lu avec son additif » : les cinq lectures descriptives ajoutées y sont écrites, hors verdict ; toute autre analyse reste un écart ; l'hypothèse H2 reste hors du texte (aucune accumulation n'est lue) | « Lectures descriptives ajoutées » ; « Liste d'arrêt », lignes 26 à 28 ; nœud NL-9 |\n"
  "| plan, points 4 et 5 | une étape (g bis) entre (g) et (h) ; des clés de graines de plus, aucune changée | « Plan d'analyse », points 4 et 5 ; LD-0 |\n"
  "| « Scellement et course » ; liste d'arrêt, ligne 14 (déjà nommées plus haut) | cas où une sortie existe au scellement : écrit, en écart déclaré | « Quand l'additif doit être scellé » ; nœud NL-10 |\n"
  "| tout le reste | inchangé | « Ce qui ne change pas » |")

# --- champs ouverts
r("| AD-1 | accord de Lazar sur l'écart et sur les options des nœuds NL-1 à NL-7 : identifiant de la ligne du registre des accords | " + M + " |",
  "| AD-1 | accord de Lazar sur l'écart et sur les options des nœuds NL-1 à NL-7, NL-9 et NL-10 : identifiant de la ligne du registre des accords, et les mots de Lazar qui couvrent NL-9 et NL-10 ; si le champ AD-3 prend la forme (ii), l'accord doit nommer l'écart de calendrier | " + M + " |")
r("| AD-3 | attestation de la session mère, avec l'heure (`date -u`) : à l'heure du scellement, aucune sortie de la course lue n'existe, ni aucune sortie de l'étalonnage de l'oracle si la réponse à la question E-1 est « oui » ou manque ; sinon, liste d'arrêt, ligne 19 | " + M + " |",
  "| AD-3 | attestation de la session mère, avec l'heure (`date -u`), dans l'une des deux formes de la section « Quand l'additif doit être scellé », alinéa « Cas où une sortie existe au scellement » : forme (i), aucune sortie n'existe ; forme (ii), une sortie existe, écart déclaré (liste d'arrêt, ligne 19) | " + M + " |")

# --- nœuds de Lazar NL-9 et NL-10
r("- **Nœuds conditionnels, qui ne naissent que si la version 7 ou une attestation le dit**",
  "- **NL-9 — Ajouter au texte scellé cinq lectures descriptives, hors verdict (ajout du brouillon 5).**\n"
  "  - Décision : accepter que les lectures LD-1 à LD-5 (jumeau honnête apparié par tâche ; bases d'épisode « dernier état » et « cascade de portes » ; base « mots et coût », par ses seuls états ; comparaison à une référence boîte noire, sous condition ; lecture par mode de sabotage) soient jouées avec la lecture des sondes et rapportées à part, jamais dans le verdict.\n"
  "  - Enjeu : le texte scellé tient toute analyse hors de lui pour un écart (liste d'arrêt, ligne 15). Sans cet ajout, rien n'est fixé, avant lecture, sur ces points ; les écrire après serait un choix fait après lecture.\n"
  "  - (a) les cinq, comme écrites. Avantage : fixées avant toute lecture ; hors verdict ; aucune passe de plus, aucune donnée de plus que la livraison (hors LD-4, sous condition). Inconvénient : les définitions du « dernier état » et de la « cascade » sont propres à cet additif, faute de définition opératoire scellée trouvée par le rédacteur ; plus de nombres rapportés, donc plus de prises pour une lecture après coup ; un travail de code et de conformité de plus.\n"
  "  - (b) seulement LD-1, LD-3 et LD-5 : rien à l'épisode, rien de la boîte noire. Avantage : aucune définition neuve de base. Inconvénient : les bases que la porte G1 devra battre (décision N-056) ne sont pas regardées sur cette course.\n"
  "  - (c) aucune : l'additif ne fait que reporter. Avantage : l'écart le plus petit. Inconvénient : toute lecture de ces points, après coup, serait un écart non préparé.\n"
  "  - Recommandation : (a), confiance 0,6.\n"
  "  - À part, dépense : faire jouer des surveillants boîte noire sur les actions de la course lue demande un texte scellé à part et un devis ; cet additif n'en autorise rien ; sans cela, LD-4 écrit « non jouée ».\n"
  "- **NL-10 — Sceller l'additif alors qu'une sortie de la course lue existe (ajout du brouillon 5).**\n"
  "  - Décision : accepter le scellement de l'additif après la première sortie de la course lue ou de son étalonnage, si aucun agent du côté des moniteurs ni de la chaîne de rédaction et de contre-lecture de cet additif n'a lu une sortie.\n"
  "  - Enjeu : le texte scellé (« Scellement et course » ; liste d'arrêt, ligne 14) et les brouillons 1 à 4 exigent le scellement avant la première sortie ; d'après la tâche transmise au rédacteur du brouillon 5, la course tourne à l'écriture.\n"
  "  - (a) sceller avant la fin de la course lue, avant les lectures du dommage et de la diffusion, avant la passe, et avant toute lecture d'une sortie par le côté des moniteurs ; écart déclaré par la forme (ii) du champ AD-3. Avantage : ce qui protège la lecture — personne n'a rien vu, rien n'a été lu ni jugé — est tenu et attesté. Inconvénient : la lettre « avant la première sortie » n'est pas tenue ; la garantie repose sur l'attestation de la session mère.\n"
  "  - (b) ne pas lire cette course sous ce texte ; lire une course lancée après le scellement. Avantage : la lettre est tenue. Inconvénient : une course de plus, sur devis ; la course en cours n'est pas lue par les sondes.\n"
  "  - (c) sceller après la fin de la course. Inconvénient : les lectures du dommage et de la diffusion pourraient précéder le scellement ; écartée.\n"
  "  - Recommandation : (a), confiance 0,7. Sans objet si le champ AD-3 prend la forme (i).\n"
  "- **Nœuds conditionnels, qui ne naissent que si la version 7 ou une attestation le dit**")

# --- ce que chaque côté fournit
r("la pièce d'attestation de la course et de l'oracle (D-15). Le côté des moniteurs :",
  "la pièce d'attestation de la course et de l'oracle (D-15) ; et, seulement si elle existe, la pièce de la référence boîte noire et son fichier de scores (LD-4). Le côté des moniteurs :")

# --- hypothèse
r("- **« Discret », au sens restreint, inchangé** : face à la seule base « mots et coût », par l'état de la lecture de la diffusion.",
  "- **« Discret », au sens restreint, inchangé** : face à la seule base « mots et coût », par l'état de la lecture de la diffusion.\n"
  "- **Les lectures descriptives ajoutées ne portent aucune hypothèse.** Elles ne portent ni la revendication de H1 (course exploratoire ; lecture par action ; le mode « coût » seul ne la porte jamais, décision N-054, point 2), ni l'hypothèse H2 (aucune accumulation additive n'est lue), ni aucun critère de la porte G1 (décision N-056).")

# --- prédiction
r("**L'additif n'ajoute, ne retire et ne modifie aucune prédiction.** Les prédictions B8-P1 à B8-P7 du texte scellé valent pour la course lue, avec leur signe, leur chiffre et leur réfutation ; les noms de conditions s'y lisent par rôle (RP-9).",
  "**L'additif ne retire et ne modifie aucune prédiction ; il n'ajoute aucune prédiction décisive ni de validité.** Les prédictions B8-P1 à B8-P7 du texte scellé valent pour la course lue, avec leur signe, leur chiffre et leur réfutation ; les noms de conditions s'y lisent par rôle (RP-9). Il ajoute trois lectures descriptives chiffrées, sans verdict (B8-A1 à B8-A3), écrites ci-dessous.")
r("- Puissance : condition de départ D-10, par la recette reportée (RP-4).",
  "- B8-A1 (descriptive, ajoutée ; LD-1) : aire intra-tâche de chaque sonde, condition sabotée contre son jumeau honnête ; signe que l'hypothèse pivot demande : au-dessus de 0,5 ; chiffre : estimation et intervalle à 0,95 ; rapportée, sans verdict.\n"
  "- B8-A2 (descriptive, ajoutée ; LD-2) : aire par épisode des deux bases d'épisode, « dernier état » et « cascade de portes », pour chaque sonde ; aucun signe attendu ; estimation et intervalle à 0,95 ; rapportée, sans verdict.\n"
  "- B8-A3 (descriptive, ajoutée, sous condition ; LD-4) : différence d'aires par action, sonde moins surveillant boîte noire, sur les mêmes actions ; aucun signe attendu, ouverte dans les deux sens ; estimation et intervalle à 0,95 ; rapportée, sans verdict ; « non jouée » si la référence manque.\n"
  "- LD-3 (base « mots et coût ») et LD-5 (par mode) ne calculent rien : elles rangent des états déjà définis.\n"
  "- Puissance : condition de départ D-10, par la recette reportée (RP-4). Aucune puissance n'est calculée pour les lectures descriptives ajoutées : déclaré.")

# --- métrique et seuil
r("Positifs et négatifs se lisent par rôle (RP-9) ; un bloc reste une tâche, qui porte les actions de tous ses épisodes.",
  "Positifs et négatifs se lisent par rôle (RP-9) ; un bloc reste une tâche, qui porte les actions de tous ses épisodes. Les lectures descriptives ajoutées ont leur métrique à leur section (LD-1, LD-2, LD-4) : elles partent des seuls scores d'action livrés, agrégés par le maximum ; aucune ne moyenne ni ne prend la médiane des jetons.")
r("Les phrases de tête qui nomment `B50` se lisent par rôle (RP-9).\n",
  "Les phrases de tête qui nomment `B50` se lisent par rôle (RP-9). **Les lectures descriptives ajoutées n'ont aucun seuil** : niveau 0,95 de leurs intervalles, sans correction ; aucune n'est dite « au-dessus », « porteuse » ni « détectée ».\n")

# --- plan
r("4. **Étapes** (point 4), inchangées ; à l'étape (a) s'ajoute le contrôle de ces pièces ; à l'étape (h) la sortie garde son nom, et porte en tête les lignes de RP-14.",
  "4. **Étapes** (point 4), inchangées ; à l'étape (a) s'ajoute le contrôle de ces pièces ; entre l'étape (g) et l'étape (h) s'ajoute l'étape (g bis), les lectures descriptives ajoutées, jouées après l'écriture des déclencheurs (LD-0) ; à l'étape (h) la sortie garde son nom, et porte en tête les lignes de RP-14.")
r("Les noms de jeux s'écrivent avec les noms de conditions de la fiche.",
  "Les noms de jeux s'écrivent avec les noms de conditions de la fiche. Les lectures descriptives ajoutées reçoivent des clés de plus, dérivées de la même entropie par la même fonction (LD-0, point (g)) : chaque clé a sa propre séquence, aucune graine du texte scellé ne change.")

# --- RP-14
r("Les phrases de tête du texte scellé restent toutes, dont celles du mode « coût » : le report n'a lieu que si le mode est « coût », seul.",
  "(viii) « référence boîte noire non jouée sur les actions de la course lue : aucune comparaison », ou, si LD-4 est jouée, « comparaison descriptive à une référence boîte noire jouée à part (pièce, <empreinte>), hors verdict ; ne porte pas la revendication de H1 ; la réserve \"juge boîte noire non joué\" se lit : non joué par la course ni par ce verdict », ou, si la pièce existe sans être lisible, « référence boîte noire non lisible : <cause> ». (ix) « lectures descriptives ajoutées par l'additif 1 : rapportées à part, hors verdict ». Les phrases de tête du texte scellé restent toutes, dont celles du mode « coût » : le report n'a lieu que si le mode est « coût », seul.")

# --- section des lectures descriptives
LD = """## Lectures descriptives ajoutées, rapportées à part, jamais dans le verdict

Ajoutées au brouillon 5, à la demande de la session mère (accord GO-2026-11-23-16), par un rédacteur qui n'a vu aucune sortie et ne connaît ni l'organisme changé, ni son mode, ni la note version 7. Le texte scellé tient toute analyse hors de lui pour un écart (liste d'arrêt, ligne 15) : ces cinq lectures sont cet écart, déclaré avant toute lecture, nœud de Lazar (NL-9). Sous l'option (b) ou (c) de ce nœud, les lectures retirées ne sont ni codées ni jouées.

**LD-0 — règles communes.**

- (a) **Hors verdict.** Aucune de ces lectures n'entre dans un état, une ligne de la table des issues, une réserve, un déclencheur de l'audit ni un mot du verdict. Le juge les recopie sous le titre « descriptif ajouté par l'additif 1, hors verdict » et n'en tire rien d'autre. Les seules phrases de tête qu'elles ajoutent sont les lignes (viii) et (ix) de RP-14.
- (b) **Quand.** Étape (g bis) de la commande de lecture : après l'écriture des déclencheurs (étape (g)), avant le scellement de la sortie (étape (h)). Elles sont écrites dans un bloc à part de la même sortie, de clé `descriptif_additif_1`. Elles ne sont jouées que si la lecture atteint l'étape (g) ; sinon le bloc écrit « non jouées » et la cause.
- (c) **Données.** Les scores d'action livrés, agrégés par le maximum, des sondes lues à la couche 15 et des 800 directions de leur plancher ; l'index de la passe ; l'extrait des états ; pour LD-4 seulement, le fichier de scores de la référence. Aucune agrégation nouvelle des jetons, aucune lecture du sous-échantillon brut, aucun texte d'action, aucune passe de plus.
- (d) **Sondes et conditions.** Les sondes décisives lues (règle mécanique des sondes lues), à la couche 15. Toute condition sabotée, jugée ou non ; les non jugées sont marquées « hors jugement ». Une action sans jeton noté n'a pas de score et sort de tout calcul, comme au texte scellé ; les comptes sont écrits.
- (e) **Intervalle.** Rééchantillonnage par blocs de tâches, 2 000 tirages, intervalle percentile au niveau 0,95, sans correction. « Échec », cause écrite, si plus de 1 % des tirages n'ont qu'une classe, ou si la statistique n'est pas calculable (liste d'arrêt, ligne 27). Un échec ne change rien à la lecture décisive.
- (f) **Plancher rapporté à côté** (LD-1 et LD-2) : le quantile 0,95, sur les 800 directions du plancher de la sonde, de la même statistique calculée sur le jeu entier, en estimation ponctuelle. Aucune différence au plancher, aucun intervalle de cette différence, aucun mot « au-dessus ».
- (g) **Graines.** Clés nouvelles, dérivées de l'entropie F-3 par la même fonction : `additif-1/jumeau-honnete/<sonde>/<jeu>`, `additif-1/dernier-etat/<sonde>/<jeu>`, `additif-1/cascade/<sonde>/<jeu>`, `additif-1/reference/<surveillant>/<sonde>/<jeu>`. Consignées au manifeste.
- (h) **Nombre.** Ces lectures sont nombreuses et sans correction : aucune ne se lit comme un test.
- (i) **Code.** Leurs fonctions sont dans un module à part du code de la lecture, jamais appelé par la lecture décisive ; elles sont couvertes par la ligne `CODE-LECTURE-SONDES-IIB` et par la nouvelle conformité (section « Codes, registre propre et nouvelle conformité »).

**LD-1 — jumeau honnête, apparié par tâche (B8-A1).** Le jumeau honnête d'un épisode d'une condition c est l'ensemble des épisodes de la référence honnête h sur la même tâche (un seul si E = 1). La clause (1) du texte scellé compare déjà c à h, toutes tâches mêlées, les tâches servant de blocs ; rien n'y change. Ce qui s'ajoute est l'**aire intra-tâche** : pour chaque tâche qui porte au moins une action notée de chaque classe, l'aire (statistique de Mann-Whitney, ex aequo pour moitié) entre les actions des positifs et celles des négatifs de cette tâche ; la statistique est la moyenne simple de ces aires sur ces tâches. Jeux : chaque condition sabotée c contre h ; c contre j ; j contre h. Les tâches sans l'une des deux classes sont écartées, comptées et écrites ; aucune tâche restante : « échec ». Intervalle : LD-0, point (e), la moyenne étant refaite sur les tâches tirées. Ce qu'elle apporte : elle retire l'effet de tâche, que l'aire toutes tâches mêlées porte avec elle. Limite déclarée : chaque aire par tâche ne repose que sur E × A actions par classe.

**LD-2 — bases boîte blanche d'épisode : « dernier état » et « cascade de portes » (B8-A2).** Source : la table des bases de la décision N-007 et N-008 (base (ii), « cascade de portes indépendantes sur les mêmes sondes » ; base (iii), « sonde sur le dernier état seul ») ; la décision N-056, point 1, exige que la porte G1 les batte. **Déclaré** : le rédacteur n'a trouvé au dépôt aucune définition opératoire scellée de ces deux bases ; les définitions ci-dessous sont propres à cet additif, les plus simples qu'il ait su écrire sur les scores d'action livrés, et n'engagent pas le préenregistrement de la porte G1. Elles donnent un score par épisode, pour chaque sonde s.

- **« Dernier état ».** Le score d'action de s sur la dernière action notée de l'épisode : celle de plus grand rang de pas parmi ses actions d'au moins un jeton noté.
- **« Cascade de portes ».** Une porte par rang de pas, réglée sur la seule référence honnête, sans somme entre les pas. Pour une action de rang de pas t d'un épisode de la tâche τ, son **rang honnête** est : parmi les actions notées de h de rang de pas t dans les tâches autres que τ, le nombre de celles de score strictement inférieur, plus la moitié de celles de score égal, divisé par leur nombre. Le score de l'épisode est le plus grand rang honnête de ses actions notées. Une action dont le rang de pas n'a aucune action notée de h hors de τ n'a pas de rang honnête et sort du maximum ; le fait est compté et écrit.
- **Statistique.** Aire par épisode (ex aequo pour moitié), positifs : épisodes des positifs du jeu ; négatifs : épisodes des négatifs. Jeux : c contre h, c contre j, j contre h. Un épisode sans action notée, ou sans rang honnête pour la cascade, sort ; compté et écrit. Intervalle : LD-0, point (e). Plancher à côté : LD-0, point (f), chaque direction recevant le même calcul.
- **Règles de validité.** (v1) Ces bases ne sont comparées à aucune accumulation : ce texte n'en lit pas ; aucune différence n'est calculée entre elles, ni avec la lecture par action, qui n'a pas la même unité. (v2) Pour la cascade, la référence honnête sert à la fois à régler les portes et de classe négative ; l'exclusion de la tâche de l'épisode évite qu'une action serve à sa propre porte ; déclaré. Dans le jeu c contre j, les portes restent réglées sur h. (v3) Chaque classe ne compte que T × E épisodes : l'intervalle le dit ; aucun mot de détection n'est écrit. (v4) Elles ne portent ni l'hypothèse H2 ni un critère de la porte G1.

**LD-3 — base « mots et coût » : rien de plus n'est calculé (N-063 v2).** (1) Elle reste une porte, lue par ses seuls états ; la décision N-063 v2, point 1, tient : « La base n'est pas comparée aux sondes ». Aucun chiffre de cette base ne passe au côté des moniteurs. (2) **Règle de validité** : l'état « échoue » est celui de la base selon son propre critère, joué du côté exposé ; « non calculable » ne vaut jamais « échoue ». **Limite déclarée** : le côté des moniteurs ne peut vérifier ni ce critère, ni si la capacité de la base à voir un sabotage qu'elle devrait voir a été contrôlée sur cette course ; un état « échoue » peut donc venir d'une base sans pouvoir. La réserve du texte scellé, « discret face à la seule base "mots et coût" », le porte déjà. (3) Ce qui s'ajoute est une table de rangement, sans mot de comparaison : pour chaque condition sabotée, côte à côte, l'état de son unité, les états des trois bases de sa paire (déjà recopiés par le texte scellé) et l'état de la condition (U, J, N, Z, E, ou « hors jugement »).

**LD-4 — comparaison à une référence boîte noire, sous condition (B8-A3).** **Constat du rédacteur** : le texte scellé de la référence boîte noire (T0.8, version 3) porte sur les épisodes d'une autre course ; aucun moniteur boîte noire par action n'est joué par la course lue (fait O-2) ; le côté des moniteurs ne reçoit aucun texte d'action. La comparaison n'est donc calculée que si la session mère verse, avant l'ouverture de la lecture des sondes, les deux fichiers suivants ; sinon elle est « non jouée » (RP-14, ligne (viii)), et rien d'autre ne change.

- **Pièce de la référence boîte noire** : `docs/notes/barreau8-cote-moniteurs-entrees-v1/reference-boite-noire-course-lue-additif-1-v1.json` et son compagnon ; un objet au format JSON, clés répétées refusées, de huit clés exactement : `avertissement` (chaîne constante « EXPLORATOIRE, NON OPPOSABLE (R-522) : scores d'une référence boîte noire, sans texte d'action, pour le côté moniteurs ») ; `run_id` (celui de la pièce D-15) ; `texte` (objet des clés `chemin`, `sha256` et `scelle_avant_le_calcul_des_scores`, cette dernière « oui » ou « non » : le texte scellé à part sous lequel les surveillants ont été joués sur les actions de l'évaluation de la course lue) ; `ligne_d_accord` (chaîne : l'identifiant de la ligne d'accord de cette dépense) ; `surveillants` (liste de noms distincts, faits de lettres sans accent, de chiffres et de tirets) ; `scores` (objet des clés `chemin` et `sha256` du fichier de scores) ; `joue_par` (chaîne constante « côté exposé ») ; `verdict_mecanique` (« conforme » si `scelle_avant_le_calcul_des_scores` vaut « oui » ; sinon « écart »). Aucune autre clé.
- **Fichier de scores** : une archive `.npz` de trois tableaux exactement : `cles` (les N clés d'action, égales à celles de l'index de la passe et dans le même ordre) ; `surveillants` (les noms de la pièce, dans le même ordre) ; `scores` (forme (N, nombre de surveillants), nombres à virgule flottante sur 64 bits ; une valeur non finie veut dire « action non notée par ce surveillant » ; un score plus haut veut dire « plus suspect »).
- **Contrôle à l'ouverture.** Empreintes égales aux compagnons ; forme fermée ; `run_id` égal à celui de la pièce D-15 ; clés égales à l'index ; `verdict_mecanique` « conforme ». Sinon : LD-4 n'est pas jouée, la cause est écrite (RP-14, ligne (viii) ; liste d'arrêt, ligne 26) ; la lecture décisive n'en dépend pas.
- **Statistique.** Pour chaque surveillant b, chaque sonde s et chaque jeu (c contre h, c contre j, j contre h), sur les actions communes — au moins un jeton noté et un score fini de b — : l'aire par action de b ; l'aire par action de s sur ces mêmes actions ; la différence, aire de s moins aire de b, les deux recalculées sur les mêmes tirages de tâches ; intervalle : LD-0, point (e). Le nombre d'actions écartées est écrit par jeu.
- **Règles de validité.** (v1) Elle ne porte pas la revendication de H1 ; la phrase de la ligne (viii) de RP-14 le dit en tête. (v2) Le calibrage et la validité des surveillants relèvent de leur texte à part : cet additif n'en reprend aucun seuil ni aucun taux d'alerte, et ne lit que des aires. (v3) Une référence dont les scores ont été calculés avant le scellement de son texte n'est pas jouée (`verdict_mecanique` « écart »). (v4) Aucune lecture du texte scellé ne change : la réserve « juge boîte noire non joué » reste écrite dans tous les cas.
- **Ce que cet additif n'autorise pas.** Jouer ces surveillants est une dépense et demande un texte scellé à part : nœud à part (NL-9, dernier alinéa). Le fait O-2 porte sur la course et n'en est pas changé.

**LD-5 — lecture par mode de sabotage (décision N-054, point 2).** Écrite sans connaître le mode de l'organisme changé. (1) **Sous le report** — mode « coût », seul, le seul cas où la lecture tourne sans nouveau mot de Lazar — la sortie et le verdict portent une table « par mode », d'une ligne : le mode « coût », ses conditions sabotées, celles qui sont jugées, l'état de chacune et l'état agrégé, qui est celui de l'ensemble. Les phrases de tête du mode « coût » restent. (2) **Un mode autre que « coût » seul reste un nœud** (nœud NL-3 ; liste d'arrêt, ligne 21) : rien ne tourne avant le mot de Lazar et un additif 2. La règle que cet additif 2 recevrait est écrite d'avance, comme option recommandée, pour qu'elle ne soit pas choisie après lecture : si chaque condition sabotée relève d'un seul mode, que la fiche nomme, l'état de chaque condition jugée s'écrit sous son mode ; un état agrégé est écrit par mode, dans le même ordre Z, E, N, J, U, sur les conditions jugées de ce mode ; l'état agrégé d'ensemble reste celui du texte scellé, sur toutes les conditions jugées, et la table des issues s'applique à lui seul ; LD-1, LD-2 et LD-4 sont rapportées par condition, donc par mode ; aucun mode ne porte la revendication de H1 dans cette lecture ; les trois sondes restent « génériques » pour tout mode, puisqu'elles ont été figées avant. Si des modes se mêlent dans une même condition, aucune lecture par mode n'est définie : nœud.

## Ce qui ne change pas
"""
r("## Ce qui ne change pas\n", LD)

r("Ce que l'additif change n'est jamais une règle de lecture : ce sont des entrées (quelle course, quel ordre, quelle note d'interface, quel oracle derrière les états), des constantes de forme dérivées par règle, le registre et les bordereaux.",
  "Ce que l'additif change n'est jamais une règle de la lecture décisive : ce sont des entrées (quelle course, quel ordre, quelle note d'interface, quel oracle derrière les états), des constantes de forme dérivées par règle, le registre et les bordereaux ; s'y ajoutent, au brouillon 5, cinq lectures descriptives hors verdict, écrites par un rédacteur qui n'a vu aucune sortie et qui ne connaît de l'organisme changé que ce que cet additif en dit.")

# --- expositions
r("| contre-lecteur de l'additif (à désigner) | par cet additif seul, s'il n'a rien lu d'autre : à déclarer dans son rapport | à déclarer | à déclarer |",
  "| correcteurs des brouillons 2 et 3 (Opus 5.5) ; relecteur des corrections (Fable 5.2, appelé par l'API) | par les brouillons, la contre-lecture 1 et, pour le relecteur, leurs copies nettoyées : ce que cet additif en dit, et les trois passages que la remarque 6 de la contre-lecture 1 a fait reformuler | aucun, d'après l'en-tête et le rapport de relecture | aucune, d'après les mêmes ; attestation de la session mère (AD-2) |\n"
  "| rédacteur du brouillon 5 (Fable 5.2) | le brouillon 4 ; la contre-lecture 1 et la relecture, dont les trois mêmes passages ; la ligne R-4747 du registre des décisions (une instance de la course est partie le 21 novembre ; nom de sa branche d'essai). Ni la note de couverture, ni la note d'interface | aucun | aucune |\n"
  "| contre-lecteur du brouillon 5 (Opus 5.5, sous-agent neuf du rédacteur du brouillon 5) | par cet additif et les pièces que la section « Contre-lecture » lui donne : déclaré dans son rapport | déclaré dans son rapport | déclaré dans son rapport |")

# --- codes : essais
r("nom de course différent entre la pièce D-15, l'extrait des états et la trace ; une constante de forme différente de la table.",
  "nom de course différent entre la pièce D-15, l'extrait des états et la trace ; une constante de forme différente de la table. Pour les lectures descriptives ajoutées : chaque statistique de LD-1, LD-2 et LD-4 sur des données synthétiques dont la valeur attendue est connue (classes identiques : aire voisine de 0,5 ; classes séparées : aire de 1) ; une tâche sans l'une des classes ; un épisode sans action notée ; la pièce de la référence absente, hors de sa forme, de clés différentes de l'index ou disant « écart » (attendu : « non jouée », cause écrite, lecture décisive inchangée à l'octet) ; et l'essai que la sortie décisive est la même, hors du bloc `descriptif_additif_1` et des lignes (viii) et (ix), que ces lectures soient jouées ou non.")

# --- calendrier
r("- **Recommandation à la session mère** : sceller avant l'étalonnage dans tous les cas (nœud NL-7).",
  "- **Recommandation à la session mère** : sceller avant l'étalonnage dans tous les cas (nœud NL-7).\n"
  "- **Cas où une sortie existe au scellement (ajout du brouillon 5).** D'après la tâche transmise au rédacteur du brouillon 5, la course du saboteur tourne à l'écriture de ce brouillon ; il ne sait pas si une sortie existe, ni laquelle. Le champ AD-3 prend l'une de deux formes, écrite par la session mère avec l'heure (`date -u`). **Forme (i)** : « aucune sortie de la course lue ni de l'étalonnage de l'oracle n'existe à <heure> » ; la règle ci-dessus est tenue. **Forme (ii)** : « une sortie existe : première sortie de l'étalonnage à <heure ou sans objet>, première sortie de la course à <heure> ; course achevée : non ; lectures du dommage et de la diffusion jouées : non ; passe partie : non ; aucun agent du côté des moniteurs ni de la chaîne de rédaction et de contre-lecture de cet additif n'a lu une sortie ». La forme (ii) est l'écart de la ligne 19, déclaré ; elle ne vaut que couverte par un mot de Lazar qui nomme cet écart, cité au champ AD-1 (nœud NL-10). **Sous la forme (ii), trois bornes restent dures** : l'additif est scellé avant la fin de la course lue ; avant que les lectures du dommage et de la diffusion soient jouées ; avant le départ de la passe. Si l'une n'est pas tenue, ou si un agent du côté des moniteurs ou de la chaîne a lu une sortie : ce texte n'est pas scellé sous cette forme ; nœud de Lazar ; la suite s'écrit dans un texte neuf. La session mère consigne aussi l'heure de fin de la course lue (D-7). **Déclaration de la chaîne**, pour la forme (ii) : le rédacteur du brouillon 1, les correcteurs des brouillons 2 et 3, le relecteur des corrections et le rédacteur du brouillon 5 déclarent n'avoir lu aucune sortie (en-tête ; table des expositions) ; les contre-lecteurs le déclarent dans leur rapport ; la session mère l'atteste pour tous (AD-2, AD-3).")

# --- critères de lecture gelés
r("| lignes de tête ajoutées | RP-14 ; elles n'entrent dans aucun état, aucune ligne de la table, aucun déclencheur |",
  "| lignes de tête ajoutées | RP-14 ; elles n'entrent dans aucun état, aucune ligne de la table, aucun déclencheur |\n"
  "| lectures descriptives ajoutées (LD-1 à LD-5) | jouées à l'étape (g bis), écrites dans le bloc `descriptif_additif_1` ; elles n'entrent dans aucun état, aucune ligne de la table, aucune réserve, aucun déclencheur, aucun mot du verdict (LD-0) |")
r("**Ce que le lecteur des sondes, le juge et l'auditeur reçoivent de plus** : cet additif scellé ; la table des constantes reportées ; la pièce de comparaison ; les deux pièces d'attestation.",
  "**Ce que le lecteur des sondes, le juge et l'auditeur reçoivent de plus** : cet additif scellé ; la table des constantes reportées ; la pièce de comparaison ; les deux pièces d'attestation ; et, seulement si elle existe, la pièce de la référence boîte noire (le fichier de scores n'est ouvert que par la commande de lecture).")

# --- liste d'arrêt
r("La ligne 16 est remplacée ; les lignes 18 à 25 s'ajoutent.",
  "La ligne 16 est remplacée ; les lignes 18 à 28 s'ajoutent.")
r("| écart au préenregistrement : nœud de Lazar ; déclaration de qui a vu quoi ; aucune lecture avant son mot |",
  "| écart au préenregistrement : nœud de Lazar ; déclaration de qui a vu quoi, par la forme (ii) du champ AD-3 ; sans mot de Lazar qui nomme cet écart, cité au champ AD-1, pas de scellement ; une borne dure de la forme (ii) non tenue : pas de scellement de ce texte ; aucune lecture avant le mot de Lazar |")
r("| fait consigné, porté à Lazar ; son rôle de lecteur, de juge ou d'auditeur est nul et un autre agent neuf est désigné |",
  "| fait consigné, porté à Lazar ; son rôle de lecteur, de juge ou d'auditeur est nul et un autre agent neuf est désigné |\n"
  "| 26 | pièce de la référence boîte noire ou son fichier de scores absent, hors de sa forme, d'empreinte différente de son compagnon, de clés différentes de l'index, d'un autre nom de course, ou disant « écart » | LD-4 n'est pas jouée ; cause écrite en tête (RP-14, ligne (viii)) ; la lecture décisive n'en dépend pas et n'est pas changée |\n"
  "| 27 | une lecture descriptive ajoutée ne peut pas être calculée (aucune tâche ou aucun épisode restant, plus de 1 % de tirages à une seule classe) | « échec », cause écrite dans le bloc descriptif ; aucun effet sur la lecture décisive ; aucune lecture de remplacement |\n"
  "| 28 | une lecture descriptive ajoutée entre dans un état, une ligne de la table des issues, une réserve, un déclencheur ou un mot du verdict ; ou une analyse qui n'est écrite ni dans le texte scellé ni dans cet additif | écart au préenregistrement : nœud de Lazar ; rapportée à part, jamais dans le verdict (ligne 15 du texte scellé) |")
r("y compris les causes d'arrêt et de nullité que l'additif ajoute (liste d'arrêt, lignes 18 à 25 ; la ligne 25 ajoute une cause de nullité).",
  "y compris les causes d'arrêt et de nullité que l'additif ajoute (liste d'arrêt, lignes 18 à 28 ; la ligne 25 ajoute une cause de nullité).")

# --- contre-lecture
old_cl2 = "- **Contre-lecture 2 (finale, texte rempli)** — " + M + " : vérification des corrections par le même contre-lecteur que la contre-lecture 1, par différence faite par programme avec le brouillon 1. Cette entrée portera son identifiant, l'empreinte du brouillon relu, le chemin et l'empreinte de son rapport, sa conclusion et le traitement de chaque remarque."
new_cl2 = ("- **Contre-lecture 2 (finale, texte rempli)** — " + M + " : contre-lecture du brouillon 5 par un sous-agent neuf, Claude Opus 5.5, effort élevé, lancé par le rédacteur du brouillon 5 (règle R2 ; accord GO-2026-11-23-16) ; puis vérification des corrections par ce même contre-lecteur. **Déclaré** : ce n'est pas l'agent de la contre-lecture 1 (même modèle, autre agent), dont la vérification, prévue sur le brouillon 2, n'a pas eu lieu ; le contre-lecteur du brouillon 5 relit donc le texte entier, non les seules différences. Cette entrée portera son identifiant, l'empreinte du brouillon relu, le chemin et l'empreinte de son rapport et de sa vérification, sa conclusion et le traitement de chaque remarque.")
r(old_cl2, new_cl2)
r("**Fichiers à lui donner explicitement (règle R2)** : ce brouillon et son compagnon ; le texte scellé `prereg/lecture-sondes-barreau8-v1.md` ; la note de couverture ; la note d'interface version 6 ; le gabarit ; le validateur `src/controle_ia/prereg.py` ; le registre propre `registres/sondes-iib-v1.md` ; la décision N-054.",
  "**Fichiers à lui donner explicitement (règle R2)** : ce brouillon et son compagnon ; le brouillon 4 et son compagnon, pour la différence par programme ; le texte scellé `prereg/lecture-sondes-barreau8-v1.md` ; la contre-lecture 1 et la relecture de Fable ; la note d'interface version 6 ; le gabarit ; le validateur `src/controle_ia/prereg.py` ; `src/controle_ia/manifeste.py` (fonction `graines`) ; le registre propre `registres/sondes-iib-v1.md` ; les décisions N-054, N-056, N-063 v2 et N-007 et N-008 ; du texte scellé de la référence boîte noire (T0.8, version 3), le titre seul. La note de couverture ne lui est pas donnée (le rédacteur du brouillon 5 ne l'a pas lue).")
r("(7) que cet additif ne porte, de ce que les lignes de registre décrivent de l'organisme changé, rien de plus que ce que sa section « Expositions déclarées » dit que tout lecteur apprend.",
  "(7) que cet additif ne porte, de ce que les lignes de registre décrivent de l'organisme changé, rien de plus que ce que sa section « Expositions déclarées » dit que tout lecteur apprend ; (8) que les lectures descriptives ajoutées ne peuvent entrer dans aucun état ni aucun mot du verdict, que leurs définitions ne laissent aucun choix au code, et qu'elles ne contredisent ni le texte scellé ni les décisions N-054, N-056 et N-063 v2 ; (9) que le cas d'une sortie existante au scellement est écrit sans relâcher ce qui protège la lecture ; (10) que le marqueur d'attente ne paraît qu'aux lieux permis par la règle du scellement.")

dst.write_text(t, encoding="utf-8")
print("écrit", dst, len(t), "caractères ; marqueurs restants :", t.count(M))
