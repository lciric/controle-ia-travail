"""Brouillon 4 → brouillon 5 du préenregistrement de l'idée 1.1, version 2 : couples « ancien → nouveau ».

Chaque « ancien » doit figurer exactement une fois dans le texte courant, sinon arrêt sans rien écrire. Le brouillon 4 n'est
pas modifié ; le brouillon 5 n'est jamais écrasé. Source des couples : la vérification
`verification-preuve-v3-et-brouillon4-idee-1-1-v1.md` (b2f92646…), § 4.2 et § 4.3, mot pour mot (les retours à la ligne
suivent le texte) ; n7 et la remarque sans couple : forme choisie selon la consigne de la mère ; en-tête et statut.
Usage : python -I -B appliquer_couples_brouillon4_vers_5_v1.py "HH:MM" (heure UTC de `date -u` au scellement), depuis le
dossier `docs/notes/organisme-idees-juge-v1/`."""
import hashlib
import pathlib
import sys

SOURCE = pathlib.Path("organisme-idee-1-1-poids-du-nul-v2-brouillon4.md")
CIBLE = pathlib.Path("organisme-idee-1-1-poids-du-nul-v2-brouillon5.md")
EMPREINTE_SOURCE = "4adac754a3e90c4c2dedaaf3cf2ed83bde04761670c6c67cfbdd2f5ac21ede26"
HEURE = sys.argv[1]

COUPLES = [
    ("N-1",
     "vérifié par moi sur `proba` de la copie `94bfd92`, 200 instants, écart 0, avec et sans gel)",
     "vérifié sur `proba` de la copie `94bfd92`, 200 instants, avec et sans gel : écart nul tant qu'aucun compte n'atteint 70, puis au plus 2·10⁻¹² ; sur une issue épuisée les deux lois sont au plancher, à un facteur de renormalisation près, sans effet attendu sur une promotion)"),
    ("N-2",
     "sont attendues rejouables telles quelles ; si l'une ne l'est pas, elle est listée de même, avec sa\n  raison.",
     "sont attendues rejouables telles quelles ; si une de leurs méthodes ne l'est pas **pour l'une des deux\n  raisons écrites ci-dessus et elles seules** (elle lit le dépôt tiers ou ses empreintes ; elle lance le banc comme\n  programme ou écrit hors du dossier de travail), elle est listée de même, avec sa raison ; un essai d'origine qui échoue\n  ou ne s'importe pas pour toute autre raison n'est jamais déclaré « non rejouable » : pas de jeu."),
    ("n1 (a)",
     "cartes de la grammaire Hm et Hg sans garde ; Hs (aveugle par construction) |",
     "cartes de la grammaire Hm et Hg sans garde ; Hs et Hn (aveugles dans le juge complet, par construction) ; Hn, terme projeté de la famille linéaire seule |"),
    ("n1 (b)",
     "| + ; + ; sous α ; sous α ; nul | H7, terme projeté sans garde ≥ 0,20",
     "| + ; + ; sous α ; sous α ; nul (Hs et Hn, juge complet) ; + (Hn, terme linéaire) ; sans signe (Hn, toutes les familles : rapporté) | H7, terme projeté sans garde ≥ 0,20"),
    ("n2",
     "cellule de Holm « J9-P avec gel » sur Hn porte sur J9-P complet, carte gelée.",
     "cellule de Holm « J9-P avec gel » sur Hn porte sur J9-P complet, carte gelée. Les quatre cellules de Hn\n  portent sur le monde et, à 2·10⁻¹² près, sur la loi de Hs, avec d'autres graines : elles répètent Hs ; ce que Hn\n  ajoute est la quantité (i)."),
    ("n3",
     "monotonie ([PREUVE3], proposition 2 (a) et (b)), b_r ≤ a_r.",
     "monotonie ([PREUVE3], proposition 2 (a) et (b) et leur preuve : un dénominateur qui contient plus de\n  membres est plus haut ; exact quand les membres communs sont calculés par le même code, ce que garde la ligne d'arrêt\n  « monotonie violée »), b_r ≤ a_r."),
    ("n4",
     "terme projeté de la **famille linéaire seule**, Σ_b log e_{lin,b} ; dent **rapportée,",
     "terme projeté de la **famille linéaire seule**, Σ_{b ≤ t/25} log e_{lin,b}, compté promu s'il atteint\n  log(1/α) à un instant t ∈ T₈ ; dent **rapportée,"),
    ("n5",
     "n'ai pas relevé les imports des bancs v8 et v7 (à faire par le développeur ; un module manquant dans `94bfd92` ferait échouer",
     "n'ai pas relevé les imports des bancs v8 et v7 ; le lecteur du brouillon 4 l'a fait, tous les modules et\n  noms sont présents dans `94bfd92` (à confirmer par le rejeu ; un module manquant ferait échouer"),
    ("n6",
     "ni la preuve en ses versions 2 et 3, ni sa contre-lecture, ni la version 1, ni sa contre-lecture, ni la preuve,",
     "ni la preuve en ses versions 1, 2 et 3, ni la contre-lecture de la preuve v2, ni la version 1 de ce préenregistrement, ni sa contre-lecture,"),
    ("n7 (pièces)",
     "(R-2936 ; scellée par empreinte, pas encore vérifiée par un lecteur neuf) :",
     "(R-2936 ; scellée par empreinte ; **vérifiée par un lecteur neuf, verdict « suffit »**, [VER]) :"),
    ("n7 (pièce ajoutée)",
     "    [CL3] désigne le contrôle du brouillon 2) ;\n",
     "    [CL3] désigne le contrôle du brouillon 2) ;\n"
     "  - brouillon 4, gardé intact (R12) : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-brouillon4.md`\n"
     "    (`4adac754a3e90c4c2dedaaf3cf2ed83bde04761670c6c67cfbdd2f5ac21ede26`) — **[B4]** ; **vérification de la preuve v3 et du\n"
     "    brouillon 4** (R-2938 ; preuve v3 : « suffit » ; brouillon 4 : « scellable après corrections », deux majeurs, sept mineurs) :\n"
     "    `docs/notes/organisme-idees-juge-v1/verification-preuve-v3-et-brouillon4-idee-1-1-v1.md`\n"
     "    (`b2f92646eea8a80051c798685c2ae00f013008acda26e6f214d115b0cb2705b9`) — **[VER]** ; programme des couples du brouillon 4 au\n"
     "    brouillon 5 : `…/organisme-idee-1-1-poids-du-nul-v2-outils/appliquer_couples_brouillon4_vers_5_v1.py` (empreinte dans son\n"
     "    compagnon `.sha256`) ;\n"),
    ("n7 (réserves communes)",
     "**la\n  preuve v3 est scellée par empreinte mais pas encore vérifiée par un lecteur neuf** : préalable 2.",
     "**la\n  preuve v3 est scellée par empreinte et vérifiée par un lecteur neuf, verdict « suffit »** ([VER] § 0 et § 1) : préalable 2."),
    ("n7 (préalable 2)",
     "mais la v3 elle-même\n  n'est pas encore relue ([PREUVE3] § 15).",
     "et la v3 elle-même\n  a été vérifiée par un lecteur neuf ([VER] § 0 : « suffit » comme préalable 2, aucun énoncé de taille changé ; sept mineurs de\n  texte de la preuve, non bloquants, à porter dans une version suivante ou un erratum) : **le préalable 2 est levé par ce\n  rapport**, à l'empreinte `a481c873…` de la preuve ; toute version neuve de la preuve le rouvre."),
    ("remarque sans couple (titre)",
     "**Hn s'ajoute à H7, sans la remplacer, et sans bloquer** :",
     "**Hn s'ajoute à H7, sans la remplacer ; son compte sans garde ne bloque pas, son compte sous gel bloque s'il est anormal** :"),
    ("remarque sans couple (suite)",
     "sont inscrits à\n   l'addendum (attendu : une vingtaine sans garde, d'après 206 sur 2 000).",
     "sont inscrits à\n   l'addendum (attendu : une vingtaine sans garde, d'après 206 sur 2 000). **Sous gel, un compte au-dessus du cas sain écrit\n   pour H7 — 3 promotions ou plus sur 200 — bloque le jeu**, avec son compte inscrit à l'addendum, et ouvre un texte neuf : la\n   cellule de Holm de Hn porte sur J9-P complet, aveugle, et le jeu ne verrait pas ce défaut de code ([VER] § 4.3, remarque\n   sans couple ; décision de la mère). Même choix « plus dur que le jeu », mêmes suites, que pour H7."),
    ("en-tête (titre)", "— idée 1.1, version 2, brouillon 4", "— idée 1.1, version 2, brouillon 5"),
    ("en-tête (auteur)", "auteur des brouillons 1 à 3 ;", "auteur des brouillons 1 à 4 ;"),
    ("en-tête (date)",
     "brouillon 4 rédigé de 21:51 à 21:56, tête `73189e6f` ;",
     "brouillon 4 rédigé de 21:51 à 21:56, tête `73189e6f` ; brouillon 5 produit par programme de couples et scellé à " + HEURE + " (`date -u`), tête `e18563f9` ;"),
    ("statut",
     "**Statut.** Brouillon 4 de la version 2, **scellé par empreinte seulement (R6) : il ne vaut pas préenregistrement au sens de\nR1**. Il porte sur le brouillon 3 quatre changements",
     "**Statut.** Brouillon 5 de la version 2, **scellé par empreinte seulement (R6) : il ne vaut pas préenregistrement au sens de\nR1**. Il porte sur le brouillon 4 les deux majeurs (N-1, N-2) et les sept mineurs (n1 à n7) de [VER] § 4, par leurs couples\n« ancien → nouveau » appliqués mot pour mot par programme, et la remarque sans couple de [VER] décidée par la mère (un compte\nanormal de Hn sous gel à l'étape 0 bloque) ; rien d'autre ne change (« Contre-lecture 5 »). Le brouillon 4 portait sur le\nbrouillon 3 quatre changements"),
    ("contre-lecture 5",
     "- **À venir** : contrôle du seul différentiel brouillon 3 → brouillon 4 par un sous-agent neuf. **Fichiers à lui donner\n  explicitement** : ce texte ; [B3] ; [PREUVE3] (§ 0, 3, 7, 9, 10, 11) ; [CL-P] (§ 0, 4, 5, 6) ; [R-PROJ] § 5 ;\n  `selection_pari.py` (l. 97 à 135, 210 à 216) de la copie `94bfd92` ; `PROVENANCE-complement-v2.md`. Questions à trancher : la\n  forme de Hn et le rejet de la fenêtre 1 ; Hn ajoutée et non substituée à H7 ; compte de Holm à 61 ; la réserve H7′ telle\n  qu'écrite ; les renvois à la preuve v3. Puis scellement par `sceller_prereg` et recopie sous `prereg/`.\n",
     "- **Contre-lecture 5** (R2 : vérification de la preuve v3 et contrôle du différentiel brouillon 3 → brouillon 4, avec le\n  différentiel 2 → 3 vérifié à part) — sous-agent neuf, qui n'a écrit ni la preuve, ni les brouillons, ni leurs contre-lectures ;\n  texte relu : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-brouillon4.md`,\n  `4adac754a3e90c4c2dedaaf3cf2ed83bde04761670c6c67cfbdd2f5ac21ede26` ; rapport :\n  `docs/notes/organisme-idees-juge-v1/verification-preuve-v3-et-brouillon4-idee-1-1-v1.md`,\n  `b2f92646eea8a80051c798685c2ae00f013008acda26e6f214d115b0cb2705b9`. Verdicts : preuve v3 « suffit » comme préalable 2 ;\n  brouillon 4 « scellable après corrections » (2 majeurs et 7 mineurs, tous de texte). **Traitement**, point par point :\n  - N-1 (« écart 0 » faux pour Hn) : **acceptée**, couple appliqué mot pour mot.\n  - N-2 (porte ouverte au préalable 1) : **acceptée**, couple appliqué mot pour mot.\n  - n1 (signe et objet de P12 sur Hn ; deux couples) : **acceptée**. n2 (les cellules de Hn répètent Hs) : **acceptée**. n3\n    (renvoi de la monotonie) : **acceptée**. n4 (règle de promotion de la quantité (i)) : **acceptée**. n5 (imports des bancs v8\n    et v7) : **acceptée**. n6 (ligne d'auteur) : **acceptée**. Couples appliqués mot pour mot.\n  - n7 (statut de la preuve) : **acceptée** — les trois passages (pièces, « Réserves communes », préalable 2) citent [VER] et\n    disent la preuve v3 vérifiée, verdict « suffit » ; [VER] et [B4] ajoutés aux pièces ; cette entrée.\n  - remarque sans couple (compte de Hn sous gel à l'étape 0) : **portée par décision de la mère** — un compte au-dessus du cas\n    sain écrit (3 ou plus sur 200) bloque le jeu.\n  - Programme des couples : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-outils/appliquer_couples_brouillon4_vers_5_v1.py`,\n    versé avec son compagnon ; chaque « ancien » figure exactement une fois dans le texte, sinon arrêt.\n- **À venir** : contrôle du seul différentiel brouillon 4 → brouillon 5 par un sous-agent neuf. **Fichiers à lui donner\n  explicitement** : ce texte ; [B4] ; [VER] (§ 4) ; le programme des couples. Question à trancher : le différentiel est-il\n  exactement ces couples, l'en-tête et le statut. Puis scellement par `sceller_prereg` et recopie sous `prereg/`.\n"),
]


def main():
    if CIBLE.exists():
        raise SystemExit("cible existante : aucun écrasement")
    brut = SOURCE.read_bytes()
    if hashlib.sha256(brut).hexdigest() != EMPREINTE_SOURCE:
        raise SystemExit("le brouillon 4 n'a pas l'empreinte attendue : arrêt")
    texte = brut.decode("utf-8")
    for nom, ancien, nouveau in COUPLES:
        n = texte.count(ancien)
        if n != 1:
            raise SystemExit(f"couple {nom} : « ancien » trouvé {n} fois au lieu d'une : arrêt, rien n'est écrit")
        texte = texte.replace(ancien, nouveau)
        print(f"couple {nom} : appliqué")
    CIBLE.write_text(texte, encoding="utf-8")
    print(f"{len(COUPLES)} couples appliqués ; écrit {CIBLE}")


main()
