"""Fabrique collisionneur_v9_v8e.py depuis la v8d par remplacements exacts (chaque ancien texte doit apparaître une fois)."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8d.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest() == "b780383874598f12b24c79e4087d335c8e01cda685e295f5116898fa3b1715ac"

def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)

# 1. En-tête
src = remplacer(src, """#   rapport-developpeur-collisionneur-v9-v8d-v1.md, même dossier.
\"\"\"Collisionneur""", """#   rapport-developpeur-collisionneur-v9-v8d-v1.md, même dossier.
# v9-v8e (développeur, Claude Opus 5.5, 22 novembre 2026, ordre de la mère du 22 novembre, 07:40Z) : copie du v9-v8d
#   (b7803838…, inchangé, R12). Changement, et seulement celui-là : la « forme imposée » des duels balisés, texte de
#   Fable mot pour mot (relecture-pieces-essaim-v4/relecture-fable-api.md, c1cebee3…, « Ajout hors pièces »), ajoutée
#   aux consignes des tours III.1 et III.3. Tour III.1 : après la phrase « Livrable : (a) … (d) … » qui demande les duels
#   (une seule phrase, fin de la consigne). Tour III.3 : aucune phrase n'y demande de duel ; la place n'est pas tranchée,
#   elle est choisie par --place-iii3 parmi les options listées (PLACES_III3), obligatoire pour l'étage III et pour le devis
#   de l'étage III ; les deux consignes servies sont scellées dans le dossier (consignes-etage3.json) ; une commande
#   suivante doit redonner la même place ; un dossier qui a déjà des essais sans ce fichier (commencé sous un autre script)
#   est refusé à l'étage III, pour ne pas mêler consignes balisées et non balisées. Aucune course sur la v8e avant le feu
#   de la mère. Détail : rapport-developpeur-collisionneur-v9-v8e-v1.md, même dossier.
\"\"\"Collisionneur""")

# 2. Version
src = remplacer(src, 'VERSION = "collisionneur-v9-v8d"', 'VERSION = "collisionneur-v9-v8e"')

# 3. Texte de Fable et places
src = remplacer(src, """
# ---------- v9 : garde de motifs ----------""", """
# v9-v8e : « forme imposée » des duels balisés, texte de Fable mot pour mot (relecture c1cebee3…, « Ajout hors pièces »).
FORME_IMPOSEE_DUELS = \"\"\"Forme imposée. Avant chaque duel, écris seule sur sa ligne la balise [DUEL 1], puis [DUEL 2], et ainsi de \\
suite, sans sauter de numéro. Après le dernier duel, écris seule sur sa ligne [FIN DES DUELS : n], où n est le nombre de \\
duels que tu viens d'écrire. Une balise par duel, un duel par balise ; pas de tableau qui réunisse plusieurs duels. \\
N'écris ces balises nulle part ailleurs : pour renvoyer à un duel, écris « duel 2 », sans crochets. Un duel sans balise \\
n'est pas compté.\"\"\"
CONSIGNES_V8D_E3 = {t: CONSIGNES[t] for t in ("E3-T1", "E3-T3")}  # textes de la v8d, gardés pour les essais
# Tour III.1 : après la phrase « Livrable : (a) … (d) … » (une seule phrase, qui demande les duels en (b)) : fin de consigne.
CONSIGNES["E3-T1"] = CONSIGNES_V8D_E3["E3-T1"] + "\\n" + FORME_IMPOSEE_DUELS
# Tour III.3 : aucune phrase n'y demande de duel. Places possibles, non tranchées (le développeur ne choisit pas) :
#   « fin » : après la phrase « Livrable : (a) … (c) … », en fin de consigne (même place qu'au tour III.1) ;
#   « avant-livrable » : entre la première phrase (« Tour III.3 : … qui visent ta proposition. ») et « Livrable : ».
# Places listées dans le rapport mais non écrites ici, parce qu'elles demandent des mots que Fable n'a pas donnés : au milieu
# de la phrase « Livrable », après « (b) les expériences corrigées » ; ou avec une phrase neuve qui demande des duels au tour
# III.3.
_E3T3 = CONSIGNES_V8D_E3["E3-T3"]
_COUPE_E3T3 = "\\nLivrable : "
assert _E3T3.count(_COUPE_E3T3) == 1
PLACES_III3 = {
    "fin": _E3T3 + "\\n" + FORME_IMPOSEE_DUELS,
    "avant-livrable": _E3T3.replace(_COUPE_E3T3, "\\n" + FORME_IMPOSEE_DUELS + _COUPE_E3T3),
}
PLACE_III3 = None  # fixée par fixer_place_iii3 (option --place-iii3) ; None : le tour III.3 n'a pas de consigne servie
del CONSIGNES["E3-T3"]


def fixer_place_iii3(place):
    \"\"\"v9-v8e : fixe la consigne du tour III.3 depuis la place choisie ; place inconnue : Arret (avant toute écriture).\"\"\"
    global PLACE_III3
    if place not in PLACES_III3:
        raise Arret(CODE_USAGE, f"--place-iii3 doit être l'une de {sorted(PLACES_III3)} (place des balises au tour III.3, "
                                f"non tranchée par le développeur) : {place!r} refusé ; rien n'est écrit")
    PLACE_III3 = place
    CONSIGNES["E3-T3"] = PLACES_III3[place]


def description_consignes_etage3():
    return {"script": VERSION, "place_iii3": PLACE_III3,
            "consignes": {t: CONSIGNES[t] for t in ("E3-T1", "E3-T3")},
            "sha256": {t: empreinte(CONSIGNES[t]) for t in ("E3-T1", "E3-T3")}}


def sceller_consignes_etage3(dossier):
    \"\"\"v9-v8e : au premier lancement de l'étage III, écrit consignes-etage3.json ; ensuite, les consignes doivent être les
    mêmes. Un dossier qui a déjà des essais sans ce fichier est refusé (consignes non balisées déjà servies).\"\"\"
    chemin = Path(dossier) / "consignes-etage3.json"
    texte = json.dumps(description_consignes_etage3(), ensure_ascii=False, indent=1, sort_keys=True) + "\\n"
    if chemin.exists():
        _, h = lire_sceau(chemin)
        if empreinte(texte) != h:
            raise Arret(CODE_USAGE, "consignes de l'étage III différentes de celles du dossier (consignes-etage3.json) : "
                                    "redonne la même --place-iii3, ou ouvre un nouveau dossier")
        return
    if any("essai" in e for e in lire_journal(dossier)):
        raise Arret(CODE_USAGE, "dossier qui a déjà des essais sans consignes-etage3.json (commencé sous un autre script, "
                                "consignes non balisées) : la v8e ne le reprend pas ; ouvre un nouveau dossier")
    ecrire_neuf(chemin, texte)

# ---------- v9 : garde de motifs ----------""")

# 4. Options en ligne de commande
src = remplacer(src, """    d.add_argument("--jev", action="store_true")
    sous.add_parser("jev-test")""", """    d.add_argument("--jev", action="store_true")
    d.add_argument("--place-iii3", default=None, help="v9-v8e : place des balises au tour III.3, l'une de "
                   + ", ".join(sorted(PLACES_III3)) + " (obligatoire avec --question)")
    sous.add_parser("jev-test")""")
src = remplacer(src, """        if nom == "etage3":
            s.add_argument("--question")""", """        if nom == "etage3":
            s.add_argument("--question")
            s.add_argument("--place-iii3", required=True, help="v9-v8e : place des balises au tour III.3, l'une de "
                           + ", ".join(sorted(PLACES_III3)))""")
src = remplacer(src, """            fixer_composition(especes_demandees(a))
            devis(a.faits, a.question, a.jev)""", """            fixer_composition(especes_demandees(a))
            if a.question:  # v9-v8e
                fixer_place_iii3(a.place_iii3)
            devis(a.faits, a.question, a.jev)""")
src = remplacer(src, """    try:
        fixer_composition(especes_demandees(a), a.cle_anthropic, a.nom_espace_anthropic, a.cle_openai)  # v9-v5""",
"""    try:
        if etage == 3:  # v9-v8e : place contrôlée avant toute écriture
            fixer_place_iii3(a.place_iii3)
        fixer_composition(especes_demandees(a), a.cle_anthropic, a.nom_espace_anthropic, a.cle_openai)  # v9-v5""")
src = remplacer(src, """        sceller_composition(dossier)
        declarer_script(dossier, a.reprise)  # v9-v3""", """        sceller_composition(dossier)
        if etage == 3:  # v9-v8e
            sceller_consignes_etage3(dossier)
        declarer_script(dossier, a.reprise)  # v9-v3""")
# 5. Lecture des consignes scellées par verifier et devis-reprise (via lire_composition)
src = remplacer(src, """    texte, _ = lire_sceau(Path(dossier) / "especes.json")
    fixer_composition(json.loads(texte)["especes"])
""", """    texte, _ = lire_sceau(Path(dossier) / "especes.json")
    fixer_composition(json.loads(texte)["especes"])
    if (Path(dossier) / "consignes-etage3.json").exists():  # v9-v8e
        lire_consignes_etage3(dossier)


def lire_consignes_etage3(dossier):
    \"\"\"v9-v8e : fixe la place du tour III.3 depuis consignes-etage3.json ; les consignes du script doivent être celles
    du dossier, sinon Arret.\"\"\"
    texte, _ = lire_sceau(Path(dossier) / "consignes-etage3.json")
    fixer_place_iii3(json.loads(texte).get("place_iii3"))
    if json.dumps(description_consignes_etage3(), ensure_ascii=False, indent=1, sort_keys=True) + "\\n" != texte:
        raise Arret(CODE_USAGE, "consignes-etage3.json différent des consignes de ce script : dossier d'une autre version")
""")
# 6. Tour III.3 sans place fixée : arrêt nommé, jamais KeyError
src = remplacer(src, """    \"\"\"Construit le prompt ; renvoie (prompt, pièces) ou lève Arret si une entrée manque.\"\"\"
""", """    \"\"\"Construit le prompt ; renvoie (prompt, pièces) ou lève Arret si une entrée manque.\"\"\"
    if tour not in CONSIGNES:  # v9-v8e : tour III.3 sans place des balises fixée
        raise Arret(CODE_USAGE, f"{tour} : consigne non fixée (place des balises au tour III.3 : --place-iii3, ou "
                                f"consignes-etage3.json du dossier) ; rien n'est envoyé")
""")
(D / "collisionneur_v9_v8e.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
