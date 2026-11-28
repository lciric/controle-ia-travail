"""Une page d'une source citée par la synthèse v6 (correcteur v6), lue sur le PDF après contrôle d'empreinte complète.

Sources :
- [D] : PDF versés de /home/user/controle-ia-travail/docs/sources/pdf/ ;
- [C6] : PDF de [N] et [X] retéléchargés le 2026-10-21 depuis arxiv.org dans
  …/revue-detection/correction-v6/pdf/<identifiant et version>/<identifiant et version>.pdf.
Garde (R5, aucun repli silencieux) : pour chaque PDF lu, empreinte complète recalculée, égale à son compagnon .sha256
ET à l'empreinte de référence de la v1 (redaction/citations-synthese-v1.json, lui-même contrôlé par empreinte) ;
sinon ARRÊT (code 3). Aucun extrait texte n'est lu.
Normalisation (déclarée) : NFKC ; apostrophes, guillemets et tirets typographiques ramenés à l'ASCII ; blancs réduits à une
espace ; essai avec et sans recollage de la césure « lettre-fin de ligne-lettre minuscule ». Casse respectée.
Trois extractions essayées : ordre de lecture (défaut), -raw, -layout.
Usage :
  python3 -I -B pagev6.py --page CLE PAGE [defaut|raw|layout]   (affiche la page)
  python3 -I -B pagev6.py CLE PAGE "phrase"                     (code 0 si trouvée, 1 sinon)
"""
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

D = Path("/home/user/controle-ia-travail/docs/sources/pdf")
RD = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection")
C6 = RD / "correction-v6/pdf"
JSON_V1 = RD / "redaction/citations-synthese-v1.json"
JSON_V1_SHA = "2186860541680a114add5f71c27895e8eba2d614ff2a2aa671756fff7355692c"

ID = {"AP": "2502.03407v1", "PAR": "2507.12691v3", "OA": "2602.15515v2", "CA": "2610.12445v1", "YS": "2609.02893v1",
      "BX": "2509.21344v2", "AG": "2512.07810v1", "KU": "2605.27958v1", "MK": "2506.10805v4", "GM": "2601.11516v4",
      "EM": "2604.07729v1", "RO": "2604.01151v3", "TM": "2504.20271v1", "SC": "2604.14865v1",
      "MA": "2503.10965v2", "BU": "2407.12831v2", "LIAR": "2309.15840v1", "FQ": "2312.10029v2", "K": "2511.17408v4",
      "LB": "2511.16035v2", "AU": "2504.04072v3", "DYL": "2606.12618v2", "RH": "2609.19101v2", "CC": "2601.04603v1"}
DANS_D = {"AP", "PAR", "OA", "CA", "YS", "BX", "AG", "KU", "MK", "GM", "EM", "RO", "TM", "SC"}
# RO n'est pas dans le JSON de la v1 : empreinte complète donnée par la table des clés de la v5 (section 6).
REF_HORS_JSON = {"RO": "bde99a620dbbb4064fcfd9a010ac4e92b17b619c5995ae0696911afdbed7686b"}

_ref = None
_ok = {}
_cache = {}


def arret(msg):
    print(f"ARRÊT : {msg}")
    sys.exit(3)


def references():
    global _ref
    if _ref is None:
        b = JSON_V1.read_bytes()
        h = hashlib.sha256(b).hexdigest()
        if h != JSON_V1_SHA:
            arret(f"citations-synthese-v1.json a l'empreinte {h}, attendue {JSON_V1_SHA}")
        _ref = {k: v["sha256"] for k, v in json.loads(b)["pdfs"].items()}
        _ref.update(REF_HORS_JSON)
    return _ref


def chemin(cle, racine_c6=None):
    if cle not in ID:
        arret(f"clé inconnue {cle}")
    i = ID[cle]
    if cle in DANS_D:
        return D / f"{i}.pdf"
    return (racine_c6 or C6) / i / f"{i}.pdf"


def pdf_garde(cle, racine_c6=None, ref=None):
    """Retourne le chemin du PDF si son empreinte complète égale son compagnon et la référence ; sinon ARRÊT."""
    p = chemin(cle, racine_c6)
    k = str(p)
    if k in _ok:
        return p
    if not p.is_file():
        arret(f"PDF absent pour {cle} : {p}")
    comp_f = p.with_name(p.name + ".sha256")
    if not comp_f.is_file():
        arret(f"compagnon absent pour {cle} : {comp_f}")
    comp = comp_f.read_text().split()
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    attendu = ref if ref is not None else references().get(cle)
    if attendu is None:
        arret(f"aucune empreinte de référence pour {cle}")
    if len(comp) < 2 or comp[0] != h or comp[1] != p.name:
        arret(f"empreinte de {cle} {h} différente du compagnon {comp[:2]}")
    if h != attendu:
        arret(f"empreinte de {cle} {h} différente de la référence {attendu}")
    _ok[k] = True
    return p


def texte(cle, page, mode, racine_c6=None, ref=None):
    p = pdf_garde(cle, racine_c6, ref)
    k = (str(p), page, mode)
    if k not in _cache:
        opt = {"defaut": [], "raw": ["-raw"], "layout": ["-layout"]}[mode]
        r = subprocess.run(["pdftotext", *opt, "-f", str(page), "-l", str(page), str(p), "-"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            arret(f"pdftotext a échoué sur {cle} p. {page} : {r.stderr[:200]}")
        _cache[k] = r.stdout
    return _cache[k]


def norm(s, cesure):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"), ("–", "-"), ("—", "-"), ("­", "")]:
        s = s.replace(a, b)
    if cesure:
        s = re.sub(r"(?<=[A-Za-z])-\s*\n\s*(?=[a-z])", "", s)
    return re.sub(r"\s+", " ", s).strip()


def trouve(cle, page, phrase, racine_c6=None, ref=None):
    for mode in ("defaut", "raw", "layout"):
        t = texte(cle, page, mode, racine_c6, ref)
        for ces in (False, True):
            if norm(phrase, False) in norm(t, ces):
                return True
    return False


def main():
    a = sys.argv[1:]
    if a and a[0] == "--page":
        mode = a[3] if len(a) > 3 else "defaut"
        for i, l in enumerate(texte(a[1], int(a[2]), mode).splitlines(), 1):
            print(f"{i:3d}: {l}")
        return
    cle, page, phrase = a[0], int(a[1]), a[2]
    r = trouve(cle, page, phrase)
    print(f"{cle} p.{page} {'TROUVÉ' if r else 'ABSENT'} {phrase[:90]!r}")
    sys.exit(0 if r else 1)


if __name__ == "__main__":
    main()
