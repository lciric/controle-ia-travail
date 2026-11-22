"""Fabrique collisionneur_v9_v8p.py depuis la v8f (lignée de l'essaim) par remplacements exacts."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8f.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest().startswith("445fe2d3")
RELECTURE = D / "essaim-v1" / "demande-fable-essaim-pilote-v1" / "reponse-fable-v1" / "relecture-fable-api.md"
assert hashlib.sha256(RELECTURE.read_bytes()).hexdigest().startswith("28cc1d81")


def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)


src = remplacer(src, """#   et une invite qui ne contient pas la consigne scellée de son tour. Texte de Fable et places du tour III.3 inchangés.
""", """#   et une invite qui ne contient pas la consigne scellée de son tour. Texte de Fable et places du tour III.3 inchangés.
# v9-v8p (même développeur, 22 novembre 2026) : copie du v9-v8f (445fe2d3…, inchangé, R12), lignée de l'essaim (le jumeau
#   isolé reste sur ce moteur), selon la relecture de Fable essaim-v1/demande-fable-essaim-pilote-v1/reponse-fable-v1/
#   relecture-fable-api.md (28cc1d81…). Changements, et seulement ceux-là : (1) tour III.3 : la place « fin » est la
#   seule ; la phrase neuve du remplacement 1 va entre la phrase « Livrable » et la forme imposée ; (2) ligne de format
#   du seul tour III.3 (remplacement 5) : « au plus 3500 mots » du préambule commun devient « 3 500 mots au plus pour
#   l'ensemble de la réponse ; la page ne vaut que pour le point (c) » (ligne_format) ; les autres tours gardent le
#   préambule. Détail : rapport-developpeur-collisionneur-v9-v8p-v1.md, même dossier.
""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8f"', 'VERSION = "collisionneur-v9-v8p"')
src = remplacer(src, """PLACES_III3 = {
    "fin": _E3T3 + "\\n" + FORME_IMPOSEE_DUELS,
    "avant-livrable": _E3T3.replace(_COUPE_E3T3, "\\n" + FORME_IMPOSEE_DUELS + _COUPE_E3T3),
}""", """# v9-v8p : relecture de Fable (28cc1d81…), point 2, remplacement 1, mot pour mot : entre la phrase « Livrable » et la
# forme imposée. La place « fin » est la seule (« avant-livrable » retirée).
PHRASE_DUELS_III3 = ("Au point (b), écris un par un tous les duels que tu gardes, dans leur état final : corrigés, "
                     "maintenus tels quels ou nouveaux, même si aucun n'a changé. Numérote-les de nouveau à partir de 1.")
PLACES_III3 = {
    "fin": _E3T3 + "\\n" + PHRASE_DUELS_III3 + "\\n" + FORME_IMPOSEE_DUELS,
}
# v9-v8p : remplacement 5 de Fable, ligne de format du tour III.3. La v8f l'écrit par le préambule commun :
# « Format : français, Markdown, au plus {mots} mots. Termine par … », soit « au plus 3500 mots » au tour III.3 (et non
# « 3 500 mots au plus », texte cité par Fable). Le seul tour III.3 reçoit le texte neuf de Fable à la place de ce
# segment ; le gabarit commun et les autres tours ne changent pas.
FORMAT_III3_ANCIEN = f"au plus {TOURS['E3-T3']['mots']} mots"
FORMAT_III3_NOUVEAU = "3 500 mots au plus pour l'ensemble de la réponse ; la page ne vaut que pour le point (c)"


def ligne_format(tour):
    \"\"\"v9-v8p : ligne « Format : … » servie au tour `tour` (préambule commun ; tour III.3 : remplacement 5).\"\"\"
    ligne = next(l for l in PREAMBULE_GABARIT.splitlines() if l.startswith("Format :"))
    ligne = ligne.format(mots=TOURS[tour]["mots"], marqueur=MARQUEUR)
    if tour == "E3-T3":
        assert ligne.count(FORMAT_III3_ANCIEN) == 1
        ligne = ligne.replace(FORMAT_III3_ANCIEN, FORMAT_III3_NOUVEAU)
    return ligne""")
src = remplacer(src, """    morceaux = [preambule().format(lettre=lettre, autres=", ".join(autres(lettre)), mots=TOURS[tour]["mots"],
                                   marqueur=MARQUEUR),""", """    entete = preambule().format(lettre=lettre, autres=", ".join(autres(lettre)), mots=TOURS[tour]["mots"],
                                marqueur=MARQUEUR)
    if tour == "E3-T3":  # v9-v8p (remplacement 5) : la seule ligne de format du tour III.3
        assert entete.count(FORMAT_III3_ANCIEN) == 1
        entete = entete.replace(FORMAT_III3_ANCIEN, FORMAT_III3_NOUVEAU)
    morceaux = [entete,""")
assert src.count("def ligne_format(") == 1
(D / "collisionneur_v9_v8p.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
