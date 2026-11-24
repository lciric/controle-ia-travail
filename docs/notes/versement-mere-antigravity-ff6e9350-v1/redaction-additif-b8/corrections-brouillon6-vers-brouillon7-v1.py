"""Brouillon 6 -> brouillon 7 de l'additif : corrections des remarques M-1 à M-3 et m-1 à m-5
de la contre-lecture décisive finale (R2), rapport contre-lecture-additif-sondes-barreau8-brouillon6-v1.md.
Chaque ancien texte doit paraître exactement une fois ; sinon arrêt."""
import sys
from pathlib import Path

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
t = src.read_text(encoding="utf-8")
M = "À " + "REMPLIR"


def r(old: str, new: str, n: int = 1) -> None:
    global t
    c = t.count(old)
    if c != n:
        raise SystemExit(f"attendu {n}, trouvé {c} : {old[:90]!r}")
    t = t.replace(old, new)


def ligne(debut: str, nouvelle: str) -> None:
    """Remplace la ligne entière qui commence par `debut` (une seule attendue)."""
    global t
    ls = t.split("\n")
    idx = [i for i, l in enumerate(ls) if l.startswith(debut)]
    if len(idx) != 1:
        raise SystemExit(f"ligne attendue une fois, trouvée {len(idx)} : {debut[:80]!r}")
    ls[idx[0]] = nouvelle
    t = "\n".join(ls)


# --- Titre, statut, en-tête (M-3, m-1, m-4)
r("organisme changé — v1 — brouillon 6\n", "organisme changé — v1 — brouillon 7\n")
r(
    "**Statut : brouillon 6, candidat final : texte soumis à la contre-lecture finale ; les nœuds NO-1 et NO-2 y sont fermés ; c'est le statut définitif d'avant le scellement. Il est écrit après la fin de la course lue, par un rédacteur qui n'en a lu aucune sortie : écart certain, déclaré, nœud NL-0.**",
    "**Statut : brouillon 7, candidat final : texte corrigé après la contre-lecture finale du brouillon 6 et soumis à la vérification des corrections par le même contre-lecteur ; les nœuds NO-1 et NO-2 y sont fermés ; c'est le statut définitif d'avant le scellement. Il est écrit après la fin de la course lue, par un rédacteur neuf qui n'en a lu aucune sortie : écart certain, déclaré, nœud NL-0.**",
)

# m-4 : API -> interface de programmation (en-tête, ligne 5)
r(
    "relecture par Fable 5.2 appelé par l'API, puis scellement",
    "relecture par Fable 5.2 appelé par l'interface de programmation, puis scellement",
)

# En-tête : ajouter le rédacteur du brouillon 7 (M-3, m-4)
r(
    "le fait est porté à la table des expositions et à la session mère (nœud NL-6).\n- Date (UTC) :",
    "le fait est porté à la table des expositions et à la session mère (nœud NL-6). "
    "**Rédacteur du brouillon 7** : sous-agent neuf de la session mère Antigravity (`a99cfcf7527baf9160bb77d7cb2dca01`), modèle Gemini 4 Carbon en effort élevé (en remplacement temporaire de Fable autorisé par l'accord GO-2026-11-23-33 ; mandaté par la session mère `ff6e9350`, sans accès aux sorties, sous cloisonnement strict). "
    "Il n'a écrit ni le texte scellé, ni les brouillons 1 à 6, ni aucun code, ni la note de couverture, ni aucune contre-lecture. "
    "Il a porté les corrections des trois remarques majeures (M-1 à M-3) et des cinq remarques mineures (m-1 à m-5) de la contre-lecture du brouillon 6, sans toucher au reste. "
    "Il a lu : `CLAUDE.md`, le texte scellé `prereg/lecture-sondes-barreau8-v1.md`, `src/controle_ia/prereg.py`, `src/controle_ia/manifeste.py`, `registres/sondes-iib-v1.md`, `docs/notes/barreau8-iib-v1/scellement-sondes-iib-v1/` (remplissage, diff et provenance d'entropie), le brouillon 6 et les deux scripts de transformation du brouillon 5 au brouillon 6, le rapport de contre-lecture du brouillon 6 (`ab3bcdb9026dc3c8d0eb32864e6e7cc4f3eeae940fdccf914aa057cb028c9bf5`), ainsi que les seules lignes GO-2026-11-23-16, -17, -32 et -33 du registre des accords et les seules lignes R-5173 et R-5186 du registre des décisions.\n"
    "- Date (temps universel coordonné, `date -u`) :",
)

# Date (brouillon 7)
r(
    "brouillon 6 écrit le 2026-11-23 à partir de 18:16Z (temps universel, `date -u`).",
    "brouillon 6 écrit le 2026-11-23 à partir de 18:16Z ; brouillon 7 écrit le 2026-11-23 à partir de 20:53Z (temps universel, `date -u`).",
)

# m-1 : empreinte historique de CLAUDE.md en ligne 16
r(
    "- les consignes permanentes du dépôt `CLAUDE.md` — `eb06c8fd3ffb84c15d2cc45ca0e043a2c5651bf3f42492ee07f867f8a786f531` (règles R1 à R14, « Qui conçoit », « Allègement de la procédure », « Hiérarchie de décision ») ;",
    "- les consignes permanentes du dépôt `CLAUDE.md` à l'écriture du brouillon 1 (commit `bf63c169` du 2026-11-21T18:42:47Z) — `eb06c8fd3ffb84c15d2cc45ca0e043a2c5651bf3f42492ee07f867f8a786f531` (règles R1 à R14, « Qui conçoit », « Allègement de la procédure », « Hiérarchie de décision ») ;",
)

# Documents qui font foi : ajouts du brouillon 7
r(
    "  - ajoutés au brouillon 6 : l'accord de reprise GO-2026-11-23-30 ;",
    "  - ajoutés au brouillon 7 : le brouillon 6 (`prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon6.md` sur `origin/prep/additif-sondes-barreau8-scellement-v1`) — `bf10784207e6d74944d7d4804817c03eb8515d38e130ce282a577b4c96970b5e` ; le rapport de contre-lecture du brouillon 6 (`contre-lecture-additif-sondes-barreau8-brouillon6-v1.md`) — `ab3bcdb9026dc3c8d0eb32864e6e7cc4f3eeae940fdccf914aa057cb028c9bf5` ; les lignes GO-2026-11-23-17, -32 et -33 du registre des accords et les lignes R-5173 et R-5186 du registre des décisions ; le modèle de remplissage au scellement `docs/notes/barreau8-iib-v1/scellement-sondes-iib-v1/remplir_sondes_iib_v1.py` ;\n"
    "  - ajoutés au brouillon 6 : l'accord de reprise GO-2026-11-23-30 ;",
)

# --- Table des changements du brouillon 6 au brouillon 7
r(
    "## Changements du brouillon 5 au brouillon 6\n",
    "## Changements du brouillon 6 au brouillon 7\n\n"
    "Rédacteur : sous-agent neuf Gemini 4 Carbon en effort élevé (`a99cfcf7527baf9160bb77d7cb2dca01`), mandaté par la session mère sous GO-2026-11-23-33. Tout changement porte exclusivement les trois remarques majeures (M-1 à M-3) et les cinq remarques mineures (m-1 à m-5) de la contre-lecture du brouillon 6 (`ab3bcdb9026dc3c8d0eb32864e6e7cc4f3eeae940fdccf914aa057cb028c9bf5`).\n\n"
    "| remarque | correction | lieu |\n"
    "|---|---|---|\n"
    "| M-1 — clés de graines manquantes ou ambiguës dans la liste fermée de LD-0, point (g), pour les différences appariées de LD-4 et pour le rappel à taux égal de LD-1, LD-2 et LD-4 | ajout des clés dédiées `additif-1/reference/<statistique>/<terme>/<surveillant>/<sonde>/<jeu>` (`<terme>` vaut `surveillant` ou `sonde`), `additif-1/reference/difference/<statistique>/<surveillant>/<sonde>/<jeu>` et `additif-1/episode/difference/<statistique>/<base>/<sonde>/<jeu>` dans LD-0 point (g) ; précision explicite des jeux et clés exacts pour les rappels et parts d'alertes dans LD-0 point (j), LD-1, LD-2 et LD-4, sans doublon possible dans `manifeste.graines` | LD-0 points (g) et (j) ; LD-1 ; LD-2 ; LD-4 |\n"
    "| M-2 — ex aequo et cas `n = 0` dans LD-0 point (j) ; définition exacte des actions communes de `h` dans LD-4 | dans LD-0 point (j) : tri décroissant avec répétitions comptées, indice 0-basé `k` (`scores_tries[k]`) ; si `n = 0` hors de `τ`, renvoi explicite à la ligne 27 de la liste d'arrêt (« échec ») ; dans LD-4 : pour les trois jeux dont `c contre j`, les actions communes de `h` hors de `τ` sont explicitement celles de `h` ayant au moins un jeton noté et un score fini de `b`, et `n = 0` (aucune action commune de `h` hors de `τ`) renvoie à la ligne 27 | LD-0 point (j) ; LD-4 ; « Liste d'arrêt », ligne 27 |\n"
    "| M-3 — désalignement factuel de provenance dans « Contre-lecture 2 » et la table des expositions | alignement sur la chaîne réelle : contre-lecture du brouillon 6 puis vérification des corrections du brouillon 7 par le sous-agent neuf Gemini 4 Carbon en effort élevé (`289f9a3a862f39f87ccb565b8aa65125`), mandaté par la session mère sous GO-2026-11-23-16, -32 et -33 ; rédaction du brouillon 7 par un sous-agent neuf distinct (`a99cfcf7527baf9160bb77d7cb2dca01`) sous GO-2026-11-23-33 | en-tête ; « Expositions » ; « Contre-lecture » |\n"
    "| m-1 — empreinte historique de `CLAUDE.md` | mention explicite « à l'écriture du brouillon 1 (commit `bf63c169` du 2026-11-21T18:42:47Z) » | en-tête, « Documents qui font foi » |\n"
    "| m-2 — renvoi résiduel à la recommandation caduque NL-7 | mention explicite que cette recommandation est caduque au brouillon 6 et remplacée par le nœud NL-0 | « Quand l'additif doit être scellé » |\n"
    "| m-3 — phrase d'inventaire « Personne n'a vu de sortie » au présent | « n'existe à l'écriture » remplacé par « n'existait à l'écriture des brouillons 1 à 4 » | « Expositions déclarées du côté des moniteurs » |\n"
    "| m-4 — sigles et acronymes techniques non développés dans la prose rédigée | développement d'interface de programmation (au lieu du sigle anglais de programmation applicative), de format d'échange de données structurées (JSON), de temps universel coordonné et d'octets aux emplois rédactionnels signalés | en-tête ; D-6 ; D-15 ; « Note d'interface version 7 » ; RP-7 ; LD-4 ; « Expositions » ; « Contre-lecture » |\n"
    "| m-5 — clause de comparaison par programme au scellement | précision stricte des trois lieux modifiables au scellement (entrée finale de « Contre-lecture », cellules d'état AD-1 à AD-6, lignes de la table des expositions complétées par AD-2) et reformulation de l'entrée « Contre-lecture 2 » de sorte que seuls les 7 marqueurs d'attente et leurs lignes permises soient remplis au scellement | « Règle du scellement » ; « Liste d'arrêt », ligne 18 ; « Contre-lecture » |\n\n"
    "## Changements du brouillon 5 au brouillon 6\n",
)

# --- m-5 : Règle du scellement et Liste d'arrêt ligne 18 (compatibilité stricte avec remplissage au scellement)
r(
    "Le texte soumis au scellement ne diffère du texte relu par la dernière contre-lecture que par l'entrée finale de la section « Contre-lecture », par les cellules d'état des champs AD-1 à AD-6 et par les lignes de la table des expositions que le champ AD-2 complète ; la session mère le vérifie par une comparaison faite par programme (liste d'arrêt, ligne 18).",
    "Le texte soumis au scellement ne diffère du texte vérifié par la dernière contre-lecture que sur trois lieux permis, à l'exclusion de tout autre changement : (1) le remplacement des six cellules d'état portant le marqueur d'attente des champs AD-1 à AD-6 (le champ AD-5 renvoyant déjà à la section « Contre-lecture » et devenant « rempli (dans la section) ») ; (2) les lignes de la table des expositions que le champ AD-2 complète (remplissage des lignes ouvertes de l'exécutante, des développeurs, des contre-lecteurs des codes et de la session mère, plus l'ajout des lignes des agents désignés au scellement le cas échéant) ; (3) l'entrée finale « Contre-lecture 2 (finale, texte rempli) » de la section « Contre-lecture », dont le marqueur d'attente est remplacé par l'entrée définitive portant les empreintes du texte relu, du rapport de contre-lecture et du rapport de vérification. La session mère vérifie cette restriction par une comparaison faite par programme avant le scellement (liste d'arrêt, ligne 18).",
)

ligne(
    "| 18 |",
    "| 18 | additif non scellé, ou scellé sans contre-lecture conforme, ou sans sa ligne au registre propre, ou sans l'accord de Lazar (AD-1) ; ou au moins un des 7 marqueurs d'attente restant au texte soumis (validateur `src/controle_ia/prereg.py`, constante `MARQUEUR`), ou texte soumis au scelllement différent du texte vérifié par la dernière contre-lecture ailleurs qu'aux trois lieux permis par la règle du scellement (cellules d'état des champs AD-1 à AD-6, lignes complétées par AD-2 dans la table des expositions, et entrée « Contre-lecture 2 (finale, texte rempli) »), constaté par une comparaison faite par programme | rien ne tourne pour la course lue : ni ligne de code, ni passe, ni lecture ; marqueur d'attente restant, ou texte soumis différent du texte vérifié ailleurs qu'aux trois lieux permis, constaté par programme : pas de scellement |",
)

# --- m-4 : Développer JSON et Go dans la prose (D-6, D-15, fiche des champs, RP-7, LD-4)
r(
    "un objet au format JSON (objets et listes en texte)",
    "un objet au format d'échange de données structurées (JSON, objets et listes en texte)",
)
r(
    "attestation-course-et-oracle-additif-1-v1.json` et son compagnon ; un objet au format JSON, clés répétées refusées, de neuf clés exactement",
    "attestation-course-et-oracle-additif-1-v1.json` et son compagnon ; un objet au format d'échange de données structurées (JSON), clés répétées refusées, de neuf clés exactement",
)
r(
    "interface-passe-cote-moniteurs-v7-champs.json` et son compagnon, écrite par le côté saboteur et relue comme la note : un objet au format JSON, clés répétées refusées",
    "interface-passe-cote-moniteurs-v7-champs.json` et son compagnon, écrite par le côté saboteur et relue comme la note : un objet au format d'échange de données structurées (JSON), clés répétées refusées",
)
r(
    "reference-boite-noire-course-lue-additif-1-v1.json` et son compagnon ; un objet au format JSON, clés répétées refusées, de huit clés exactement",
    "reference-boite-noire-course-lue-additif-1-v1.json` et son compagnon ; un objet au format d'échange de données structurées (JSON), clés répétées refusées, de huit clés exactement",
)
r(
    "les seuls que le texte scellé dit « fixés par la borne de 2 Go ».",
    "les seuls que le texte scellé dit « fixés par la borne de 2 Go » (deux milliards d'octets).",
)

# --- M-1 et M-2 : LD-0 point (g), LD-0 point (j), LD-1, LD-2, LD-4, Liste d'arrêt ligne 27
ligne(
    "- (g) **Graines.**",
    "- (g) **Graines.** Clés nouvelles, dérivées de l'entropie F-3 par la même fonction (`manifeste.graines`, sans aucun doublon de clé admis), consignées au manifeste : "
    "`additif-1/jumeau-honnete/<statistique>/<sonde>/<jeu>`, où `<jeu>` vaut `<c>-contre-<h>`, `<c>-contre-<j>` ou `<j>-contre-<h>` ; "
    "`additif-1/episode/<lecture>/<statistique>/<sonde>/<jeu>`, où `<lecture>` vaut `maximum`, `dernier-etat` ou `cascade` et `<jeu>` l'un des trois jeux ci-dessus ; "
    "`additif-1/episode/difference/<statistique>/<base>/<sonde>/<jeu>`, où `<statistique>` vaut `rappel` (et par extension `aire` si calculée), `<base>` vaut `dernier-etat` ou `cascade` et `<jeu>` l'un des trois jeux ; "
    "`additif-1/reference/<statistique>/<terme>/<surveillant>/<sonde>/<jeu>`, où `<statistique>` vaut `aire` ou `rappel`, `<terme>` vaut `surveillant` ou `sonde` et `<jeu>` l'un des trois jeux ; "
    "`additif-1/reference/difference/<statistique>/<surveillant>/<sonde>/<jeu>`, où `<statistique>` vaut `aire` ou `rappel` et `<jeu>` l'un des trois jeux. "
    "Ici `<statistique>` vaut `aire` ou `rappel`. Chaque clé ne figure qu'une fois dans la liste passée à `manifeste.graines` (un seul tirage de tâches par clé). "
    "Une différence appariée tire les tâches une seule fois, sous sa clé de différence propre (`.../difference/...`), et recalcule les deux termes comparés sur ces mêmes tirages ; "
    "chaque statistique simple (`surveillant` pour b et `sonde` pour s dans LD-4 ; chaque terme dans LD-1 et LD-2) utilise sa propre clé simple ci-dessus, distincte de la clé de différence.",
)

ligne(
    "- (j) **Rappel à taux de fausses alertes égal.**",
    "- (j) **Rappel à taux de fausses alertes égal.** Le taux est 1 % de fausses alertes sur la référence honnête : c'est le taux auquel le programme calibre un moniteur par action, cité par le texte scellé (section « Hypothèse », alinéa « Discret » : « calibré à 1 % de fausses alertes sur l'honnête »). "
    "Une **unité** est une action (LD-1, LD-4) ou un épisode (LD-2). "
    "**Définition du seuil d'une unité de la tâche τ.** Soient les scores des unités notées de h appartenant aux tâches autres que τ, au nombre de n. "
    "Si `n = 0` (aucune unité notée de h hors de la tâche τ), le seuil n'est pas défini et le rappel (ainsi que la part d'alertes de h, de j et toute différence de rappels associée) est déclaré non calculable, en « échec » avec cause écrite (liste d'arrêt, ligne 27). "
    "Si `n ≥ 1`, on trie ces n scores par ordre décroissant en comptant toutes les répétitions (ex aequo conservés comme entrées distinctes du tableau trié, d'indices 0 à `n − 1`), on pose `k = floor(n / 100)` (partie entière de `n / 100`, donc `0 ≤ k ≤ n − 1`), et le seuil est l'élément d'indice 0-basé `k`, soit `scores_tries[k]` (le `(k + 1)`-ième plus grand score, répétitions comprises). "
    "Une unité est **en alerte** si son score dépasse **strictement** ce seuil (pour les unités de h de la tâche τ comme pour celles de toute autre condition sur la tâche τ). "
    "**Grandeurs rapportées par lecture et par jeu.** Sur tout jeu `<positifs>-contre-<négatifs>` parmi `<c>-contre-<h>`, `<c>-contre-<j>` et `<j>-contre-<h>` (les seuils étant toujours calibrés sur les unités notées de h hors de la tâche courante τ) : sont rapportés le **taux d'alertes des positifs** (dit **rappel** quand les positifs sont une condition sabotée c, et taux d'alertes de j sur le jeu `<j>-contre-<h>`), le **taux d'alertes des négatifs** du jeu (part d'alertes de h elle-même sur `<c>-contre-<h>` et `<j>-contre-<h>`, part d'alertes de j sur `<c>-contre-<j>`), et, en regard du jeu `<c>-contre-<j>`, les trois grandeurs pour chaque lecteur sur chacun des trois jeux sans ambiguïté. "
    "Tous les lecteurs comparés — sonde, base, surveillant — sont réglés par cette même règle sur la même référence honnête : c'est ce que « à taux égal » veut dire ici. "
    "**Intervalle et graine.** Pour chaque lecture et chaque jeu `<positifs>-contre-<négatifs>`, un seul tirage d'intervalle par LD-0, point (e), sous la clé `<statistique> = rappel` et le `<jeu>` exact ci-dessus, rééchantillonne les tâches avec les alertes précalculées une fois sur le jeu entier ; ce même tirage rend l'intervalle du taux d'alertes des positifs (rappel de c ou part d'alertes de j) et celui des négatifs (part d'alertes de h ou de j). "
    "La règle des tirages à une seule classe ne s'applique pas à un rappel ou taux d'alertes : si une classe entière n'a aucune unité notée sur le jeu, ou si `n = 0` hors de τ pour h, la statistique concernée est en « échec » (liste d'arrêt, ligne 27). "
    "**Limites déclarées** : l'intervalle ne porte pas l'incertitude des seuils ; quand n est inférieur à 100 (avec `n ≥ 1`), k vaut 0, le seuil est le plus grand score honnête des autres tâches et le taux réalisé n'est pas 1 % : il est écrit tel qu'il est ; c'est le cas des épisodes dès que `(T − 1) × E` est inférieur à 100. Aucun rappel n'est dit « détection ».",
)

# LD-1 : aligner la clause À taux égal sur les trois jeux et les clés explicites (M-1)
r(
    "**À taux égal** : pour chaque sonde et chaque condition sabotée c, le rappel par action de c, la part d'alertes de h et celle de j, par la règle de LD-0, point (j).",
    "**À taux égal** : pour chaque sonde et chacun des trois jeux (`<c>-contre-<h>`, `<c>-contre-<j>` et `<j>-contre-<h>`), le taux d'alertes par action des positifs (rappel de c sur les deux premiers jeux, part d'alertes de j sur le troisième) et le taux d'alertes des négatifs (part d'alertes de h sur les jeux contre h, part d'alertes de j sur `<c>-contre-<j>`), tous les seuils étant réglés sur les actions notées de h hors de la tâche courante τ par la règle de LD-0, point (j), et tirés sous la clé `additif-1/jumeau-honnete/rappel/<sonde>/<jeu>`.",
)

# LD-2 : aligner la clause À taux égal avec la clé de différence corrigée (M-1)
r(
    "- **À taux égal.** Pour le maximum, le dernier état et la cascade : rappel par épisode de c, part d'alertes de h et de j, par la règle de LD-0, point (j). Différences appariées de rappel, sur les mêmes tirages de tâches : maximum moins dernier état ; maximum moins cascade ; intervalle : LD-0, point (e).",
    "- **À taux égal.** Pour le maximum, le dernier état et la cascade, sur chacun des trois jeux (`<c>-contre-<h>`, `<c>-contre-<j>` et `<j>-contre-<h>`), sous les clés `additif-1/episode/<lecture>/rappel/<sonde>/<jeu>` : taux d'alertes par épisode des positifs (rappel de c ; part d'alertes de j) et des négatifs (part d'alertes de h ; part d'alertes de j), tous les seuils étant calibrés sur les épisodes notés de h hors de la tâche τ par la règle de LD-0, point (j). Différences appariées de rappel sur chacun des trois jeux, sur les mêmes tirages de tâches sous les clés `additif-1/episode/difference/rappel/<base>/<sonde>/<jeu>` : maximum moins dernier état ; maximum moins cascade ; intervalle : LD-0, point (e).",
)

# LD-4 : lever les deux cas limites M-1 (clés de graines propres) et M-2 (actions communes de h pour c contre j)
r(
    "- **Statistique.** Pour chaque surveillant b, chaque sonde s et chaque jeu (c contre h, c contre j, j contre h), sur les actions communes — au moins un jeton noté et un score fini de b — : l'aire par action de b ; l'aire par action de s sur ces mêmes actions ; la différence, aire de s moins aire de b, les deux recalculées sur les mêmes tirages de tâches ; intervalle : LD-0, point (e). **À taux égal**, sur ces mêmes actions : le rappel par action de b et celui de s, chacun réglé par la règle de LD-0, point (j), sur les actions communes de h ; leurs parts d'alertes sur h et sur j ; la différence appariée, rappel de s moins rappel de b. Le nombre d'actions écartées est écrit par jeu.",
    "- **Statistique.** Pour chaque surveillant b, chaque sonde s et chaque jeu (`<c>-contre-<h>`, `<c>-contre-<j>`, `<j>-contre-<h>`), sur l'ensemble des actions communes du jeu — actions du jeu ayant au moins un jeton noté et un score fini de b — : "
    "l'aire par action de b (graine `additif-1/reference/aire/surveillant/<b>/<s>/<jeu>`) ; "
    "l'aire par action de s sur ces mêmes actions communes (graine `additif-1/reference/aire/sonde/<b>/<s>/<jeu>`, où `<s>` figure dans les deux clés pour indexer l'ensemble commun propre au couple `(b, s)`) ; "
    "la différence appariée, aire de s moins aire de b, tirée à part sous sa clé dédiée `additif-1/reference/difference/aire/<b>/<s>/<jeu>`, les deux aires étant recalculées sur ces mêmes tirages de tâches ; intervalle : LD-0, point (e). "
    "**À taux égal**, sur ces mêmes actions communes du jeu : le taux d'alertes par action des positifs (rappel de c ou part d'alertes de j) et des négatifs de b (graine `additif-1/reference/rappel/surveillant/<b>/<s>/<jeu>`) et celui de s (graine `additif-1/reference/rappel/sonde/<b>/<s>/<jeu>`), chacun réglé par la règle de LD-0, point (j), ainsi que leur différence appariée (rappel de s moins rappel de b, c'est-à-dire taux d'alertes des positifs de s moins celui de b) tirée à part sous sa clé dédiée `additif-1/reference/difference/rappel/<b>/<s>/<jeu>`. "
    "**Définition exacte de l'ensemble de référence de h (même pour `<c>-contre-<j>`).** Pour un couple `(b, s)` fixé et un jeu quelconque (y compris `<c>-contre-<j>`, qui ne contient pas d'actions de h), l'ensemble des actions communes de h utilisées par LD-0 point (j) pour calibrer le seuil de b (et respectivement le seuil de s sur le même jeu de données) est l'ensemble des actions de la condition h ayant à la fois au moins un jeton noté et un score fini du surveillant b. "
    "Si, pour une tâche τ, cet ensemble d'actions communes de h dans les tâches autres que τ est vide (`n = 0`), le rappel à taux égal de b et de s, leurs parts d'alertes et leur différence de rappels sur ce jeu sont non calculables et déclarés en « échec » (liste d'arrêt, ligne 27). "
    "Le nombre d'actions écartées est écrit par jeu.",
)

# Liste d'arrêt, ligne 27 (M-2 : ajout explicite de n = 0 hors de tau)
r(
    "| 27 | une lecture descriptive ajoutée ne peut pas être calculée (aucune tâche ou aucun épisode restant, plus de 1 % de tirages à une seule classe) | « échec », cause écrite dans le bloc descriptif ; aucun effet sur la lecture décisive ; aucune lecture de remplacement |",
    "| 27 | une lecture descriptive ajoutée ne peut pas être calculée (aucune tâche ou aucun épisode restant, plus de 1 % de tirages à une seule classe, ou `n = 0` unité notée commune de `h` hors de la tâche courante τ pour calibrer un rappel à taux égal) | « échec », cause écrite dans le bloc descriptif ; aucun effet sur la lecture décisive ; aucune lecture de remplacement |",
)

# --- Expositions déclarées et provenance (M-3, m-3, m-4)
r(
    "| correcteurs des brouillons 2 et 3 (Opus 5.5) ; relecteur des corrections (Fable 5.2, appelé par l'API) |",
    "| correcteurs des brouillons 2 et 3 (Opus 5.5) ; relecteur des corrections (Fable 5.2, appelé par l'interface de programmation) |",
)
r(
    "| contre-lecteur du brouillon 6 (Opus 5.5, sous-agent neuf du rédacteur des brouillons 5 et 6) | par cet additif et les pièces que la section « Contre-lecture » lui donne : déclaré dans son rapport | déclaré dans son rapport | déclaré dans son rapport |",
    "| contre-lecteur R2 du brouillon 6 et vérificateur final du brouillon 7 (Gemini 4 Carbon en effort élevé, sous-agent neuf `289f9a3a862f39f87ccb565b8aa65125`, mandaté par la session mère sous GO-2026-11-23-16, -32 et -33) | cet additif et les seules pièces autorisées dans son rapport (`ab3bcdb9026dc3c8d0eb32864e6e7cc4f3eeae940fdccf914aa057cb028c9bf5`) : aucune consigne privée, aucune conception, aucun ordre, aucune sortie | aucun, déclaré dans son rapport | aucune, déclaré dans son rapport |\n"
    "| rédacteur du brouillon 7 (Gemini 4 Carbon en effort élevé, sous-agent neuf `a99cfcf7527baf9160bb77d7cb2dca01`, en remplacement temporaire de Fable autorisé par GO-2026-11-23-33, mandaté par la session mère) | les pièces autorisées en en-tête et le rapport de contre-lecture du brouillon 6 : aucune consigne privée, aucune conception, aucun ordre, aucune sortie | aucun | aucune |",
)

# m-3 : phrase d'inventaire au passé pour les brouillons 1 à 4
r(
    "- **Personne n'a vu de sortie.** D'après la tâche transmise au rédacteur, aucun agent du côté des moniteurs n'a vu de sortie de la course lue ni de l'étalonnage de l'oracle, et aucune n'existe à l'écriture.",
    "- **Personne n'a vu de sortie.** D'après la tâche transmise au rédacteur des brouillons 1 à 4, aucun agent du côté des moniteurs n'avait vu de sortie de la course lue ni de l'étalonnage de l'oracle, et aucune n'existait à l'écriture des brouillons 1 à 4.",
)

# m-2 : renvoi résiduel à la recommandation caduque NL-7
r(
    "- **Recommandation à la session mère** : sceller avant l'étalonnage dans tous les cas (nœud NL-7).",
    "- **Recommandation à la session mère** : sceller avant l'étalonnage dans tous les cas (recommandation caduque au brouillon 6 : l'étalonnage et la course ont eu lieu ; remplacée par le nœud NL-0).",
)

# Déclaration de la chaîne (calendrier) : mentionner le rédacteur du brouillon 7
r(
    "et le rédacteur des brouillons 5 et 6 déclarent n'avoir lu aucune sortie (en-tête ; table des expositions) ;",
    ", le rédacteur des brouillons 5 et 6 et le rédacteur du brouillon 7 déclarent n'avoir lu aucune sortie (en-tête ; table des expositions) ;",
)

# --- Contre-lecture (M-3, m-4, m-5)
r(
    "- **Relecture des corrections** — Claude Fable 5.2, appelé par l'API,",
    "- **Relecture des corrections** — Claude Fable 5.2, appelé par l'interface de programmation,",
)

ligne(
    "- **Contre-lecture 2 (finale, texte rempli)** —",
    "- **Contre-lecture 2 (finale, texte rempli)** — " + M + " : contre-lecture du brouillon 6 par le sous-agent neuf `289f9a3a862f39f87ccb565b8aa65125`, modèle Gemini 4 Carbon en effort élevé, mandaté directement par la session mère (règle R2 ; décisions GO-2026-11-23-16, GO-2026-11-23-32 et GO-2026-11-23-33, en remplacement temporaire d'Opus autorisé pour ce contre-lecteur distinct du rédacteur), rapport `contre-lecture-additif-sondes-barreau8-brouillon6-v1.md` (empreinte `ab3bcdb9026dc3c8d0eb32864e6e7cc4f3eeae940fdccf914aa057cb028c9bf5`, brouillon 6 relu d'empreinte `bf10784207e6d74944d7d4804817c03eb8515d38e130ce282a577b4c96970b5e`, conclusion « À CORRIGER AVANT SCELLEMENT » : 0 bloquant, 3 majeurs M-1 à M-3, 5 mineurs m-1 à m-5) ; correction du brouillon 6 vers le brouillon 7 par un sous-agent neuf distinct (`a99cfcf7527baf9160bb77d7cb2dca01`, Gemini 4 Carbon en effort élevé sous GO-2026-11-23-33) ; puis vérification finale des corrections du brouillon 7 par ce même contre-lecteur (`289f9a3a862f39f87ccb565b8aa65125`). **Déclaré** : ce n'est pas l'agent de la contre-lecture 1, dont la vérification, prévue sur le brouillon 2, n'a pas eu lieu ; le contre-lecteur du brouillon 6 a donc relu le texte entier, non les seules différences. Au scellement, le seul marqueur d'attente de cette entrée est remplacé par l'empreinte du brouillon 7 vérifié, le chemin et l'empreinte du rapport de vérification et sa conclusion, en même temps que le remplissage des six cellules AD-1 à AD-6 et des lignes complétées par AD-2 dans la table des expositions, sans autre changement. **Règle** : le texte soumis au scellement ne diffère du texte vérifié par cette contre-lecture qu'aux trois lieux permis par la règle du scellement (section « Ce que cet additif est, et n'est pas ») ; la session mère le vérifie par une comparaison faite par programme (liste d'arrêt, ligne 18).",
)

# Ligne 584 : mise à jour des pièces à donner au vérificateur et respect du pluriel/règle R2 (M-3, m-5)
ligne(
    "**Fichiers à lui donner explicitement (règle R2)** :",
    "**Fichiers à lui donner explicitement (règle R2)** : le brouillon 7 et son script reproductible de correction depuis le brouillon 6 ; le brouillon 6 et son compagnon ; le brouillon 4 et son compagnon, pour la différence par programme ; le rapport de contre-lecture du brouillon 6 (`ab3bcdb9026dc3c8d0eb32864e6e7cc4f3eeae940fdccf914aa057cb028c9bf5`) ; le texte scellé `prereg/lecture-sondes-barreau8-v1.md` ; la contre-lecture 1 et la relecture de Fable ; la note d'interface version 6 ; le gabarit ; le validateur `src/controle_ia/prereg.py` ; `src/controle_ia/manifeste.py` (fonction `graines`) ; le registre propre `registres/sondes-iib-v1.md` ; `docs/notes/barreau8-iib-v1/scellement-sondes-iib-v1/remplir_sondes_iib_v1.py` ; les décisions N-054, N-056, N-063 v2 et N-007 et N-008 ; du texte scellé de la référence boîte noire (T0.8, version 3), le titre seul ; les seules lignes autorisées des registres des accords et des décisions. Rien de la branche `claude/iib-reconception-oracle-v1`, aucune consigne privée, aucune conception, aucun ordre, aucune sortie.",
)

# Note dans "Ce qu'il doit éprouver en premier" : développement des sigles RP (m-4)
r(
    "(1) que la liste fermée des passages touchés est complète — aucune constante de forme du texte scellé n'échappe à une règle RP, aucun autre passage n'est changé en silence ; (2) que chaque règle RP, aux valeurs de la version 6, redonne la lettre du texte scellé, RP-7 par le calcul ;",
    "(1) que la liste fermée des passages touchés est complète — aucune constante de forme du texte scellé n'échappe à une règle de report (RP-1 à RP-14), aucun autre passage n'est changé en silence ; (2) que chaque règle de report (RP-1 à RP-14), aux valeurs de la version 6, redonne la lettre du texte scellé, RP-7 par le calcul ;",
)

dst.write_text(t, encoding="utf-8")
print("écrit", dst, len(t), "caractères ; marqueurs restants :", t.count(M))
