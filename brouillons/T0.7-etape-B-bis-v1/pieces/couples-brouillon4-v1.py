"""Brouillon 4 du préenregistrement de l'étape B bis de T0.7 = brouillon 3 (`f104917f…`, gardé tel quel, R12) + **exactement** les
six couples a1 à a4, b1, b2 de `brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1-couples.py`
(`bd8d39482eadd954c985d19d475a319236bd417f7f1850ef7b6a34259c7f6d05`), retenus par la mère (R-2917, après R-2902), puis trois
couples **de forme** déclarés ici : titre (« brouillon 3 » → « brouillon 4 »), ligne de statut, tableau du différentiel en tête.
Contrôle : le corps après les six couples a l'empreinte calculée au diagnostic (`a7a0315b…`) ; retirer les trois couples de forme
redonne ce corps au bit près. Le brouillon 3 n'est pas touché ; le brouillon 4 n'est jamais réécrit (R12).
Lancement : `python3 -I -B couples-brouillon4-v1.py <dossier du brouillon>`.
"""
import contextlib
import hashlib
import io
import runpy
import sys
from pathlib import Path

DOSSIER = Path(sys.argv[1]).resolve()
CODE = DOSSIER / "code"
B3 = DOSSIER / "T0.7-etape-B-bis-v1-brouillon3.md"
B4 = DOSSIER / "T0.7-etape-B-bis-v1-brouillon4.md"
EMPREINTE_B3 = "f104917f8e858d405fa00ced84ae6bfbc1217fcbc043801475f6b39c923153ba"
EMPREINTE_CORPS = "a7a0315b0e4d1bc57b38802695e8386d783dc10d20799214005df935535358bb"
COUPLES_PY = CODE / "diagnostic-stabilite-aires-attention-v1-couples.py"
EMPREINTE_COUPLES_PY = "bd8d39482eadd954c985d19d475a319236bd417f7f1850ef7b6a34259c7f6d05"
DIAG = ("`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-ecart-attention-carte-v1.md`, "
        "`5ecb923525617e0a7d118ee57e712709e684a3a29e35a788ff4b9a173d175f37`")
STAB = ("`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`, "
        "`dd67802d181e4a367748836a4da0de9fe02c7f85eb33f60ea46027cd202cf85a`")
h = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()          # noqa: E731

assert h(B3.read_text(encoding="utf-8")) == EMPREINTE_B3, "brouillon 3 autre que celui du compagnon"
assert hashlib.sha256(COUPLES_PY.read_bytes()).hexdigest() == EMPREINTE_COUPLES_PY, "programme des couples modifié"
assert not B4.exists(), "brouillon 4 déjà écrit (R12)"
vieux = sys.argv
sys.argv = [str(COUPLES_PY), str(DOSSIER), str(CODE / "diagnostic-stabilite-aires-attention-v1-sortie.json"),
            str(CODE / "diagnostic-stabilite-aires-attention-signal-v1-sortie.json")]
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path(str(COUPLES_PY), run_name="couples")
sys.argv = vieux
corps, couples = g["texte"], g["COUPLES"]
assert [c[0] for c in couples] == ["a1 plan, point 5", "a2 liste d'arrêt", "a3 code neuf", "a4 épreuves", "b1 qualifications",
                                   "b2 section D"]
assert h(corps) == EMPREINTE_CORPS, f"corps après les six couples : {h(corps)} ≠ {EMPREINTE_CORPS}"

LIEUX = {"a1 plan, point 5": "« Plan d'analyse », point 5 (contrôle à la marche)",
         "a2 liste d'arrêt": "« Liste d'arrêt » (contrôle carte-processeur)",
         "a3 code neuf": "« Code neuf » (`validation_imbriquee_v2`)",
         "a4 épreuves": "« Code neuf », épreuves (égalité carte-processeur)",
         "b1 qualifications": "« Critères de lecture gelés », qualifications toujours écrites (réserve R-PILE)",
         "b2 section D": "section D, « Ce que ces issues ne disent pas » (point 7)"}
QUOI = {"a1 plan, point 5": "contrôle dans les deux familles du couple tiré : linéaire à 300 époques, attention à 3 époques, même "
                            "seuil 10⁻⁴ ; déterminisme de l'attention à 300 époques sur la carte ; raison chiffrée",
        "a2 liste d'arrêt": "arrêt (erreur de chaîne) aux deux horizons et sur non-déterminisme de l'attention",
        "a3 code neuf": "module `validation_imbriquee_v2` (contrôle aux deux horizons ; la v1 reste)",
        "a4 épreuves": "épreuves du contrôle : deux horizons, autre graine, poids altérés de 1 %, déterminisme",
        "b1 qualifications": "réserve R-PILE (reproductibilité au bit près sur la même pile seulement ; dispersion mesurée)",
        "b2 section D": "ce que dit une aire « attention » sous d'autres arrondis"}
lignes = "\n".join(f"| {c[0].split()[0]} | {LIEUX[c[0]]} | {QUOI[c[0]]} |" for c in couples)
TABLEAU = (
    "**Différentiel du brouillon 3 au brouillon 4** (décision de la mère **R-2917**, après le diagnostic consigné **R-2902** : "
    "option 1 du diagnostic ; couples a1 à a4, b1, b2 appliqués **exactement**, `pieces/couples-brouillon4-v1.py` ; rapports : "
    f"{DIAG} et {STAB} ; aucun autre contenu ne change ; corps après les six couples : `{EMPREINTE_CORPS}`, avant ce tableau, le "
    "titre et la ligne de statut) :\n\n| couple | lieu | changement |\n|---|---|---|\n" + lignes + "\n\n")

FORME = [
    ("titre", "— v1 — brouillon 3\n", "— v1 — brouillon 4\n"),
    ("statut", "- **Statut** : **brouillon 3** = brouillon 2",
     "- **Statut** : **brouillon 4** = brouillon 3 (`f104917f…`, gardé tel quel, R12) + les six couples du tableau en tête "
     "(R-2917) ; **brouillon 3** = brouillon 2"),
]
texte = corps
for nom, ancien, nouveau in FORME:
    n = texte.count(ancien)
    if n != 1:
        raise SystemExit(f"{nom} : « ancien » présent {n} fois")
    texte = texte.replace(ancien, nouveau)
premiere, reste = texte.split("\n\n", 1)
assert premiere.startswith("# Préenregistrement — T0.7, étape B bis") and premiere.endswith("— v1 — brouillon 4")
texte = premiere + "\n\n" + TABLEAU + reste
# contrôle de retour : retirer les couples de forme redonne le corps au bit près
retour = texte.replace(TABLEAU, "", 1)
for _, ancien, nouveau in reversed(FORME):
    retour = retour.replace(nouveau, ancien, 1)
assert h(retour) == EMPREINTE_CORPS, "retour au corps impossible"
B4.write_text(texte, encoding="utf-8")
print("couples appliqués :", ", ".join(c[0] for c in couples), "; forme :", ", ".join(f[0] for f in FORME) + ", tableau")
print("corps après les six couples :", EMPREINTE_CORPS)
print("brouillon 4 :", h(texte))
