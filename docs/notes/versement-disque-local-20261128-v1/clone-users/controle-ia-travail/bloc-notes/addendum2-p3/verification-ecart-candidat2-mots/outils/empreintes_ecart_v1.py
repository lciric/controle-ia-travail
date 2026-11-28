"""Empreintes et chemins cités dans les parties changées du candidat 2 (élément « Candidat 1 », élément « Candidat 2 »,
fin de l'entrée 5, entrée 6), et dans l'entrée 7 prévue : chaque empreinte recalculée sur son fichier ; chaque chemin
`prereg/…` ou `docs/…` cherché dans le plan de versement v2 (lu comme une donnée), même empreinte.

Usage : python -I -B empreintes_ecart_v1.py CANDIDAT1 CANDIDAT2 PLAN ENTREE7 FICHIER...
  FICHIER... : fichiers dont on recalcule l'empreinte pour reconnaître celles citées.
"""
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path


def main(argv):
    c1, c2, plan_p, e7_p = map(Path, argv[1:5])
    fichiers = [Path(x) for x in argv[5:]]
    connus = {hashlib.sha256(f.read_bytes()).hexdigest(): f for f in fichiers}
    plan = json.loads(plan_p.read_text(encoding="utf-8"))
    dest = {x["destination"]: x for x in plan}
    print(f"plan : {len(plan)} lignes ; destinations uniques : {len(dest) == len(plan)}")
    for x in plan:
        src = Path(x["source"])
        ok = src.is_file() and hashlib.sha256(src.read_bytes()).hexdigest() == x["sha256"]
        if not ok:
            print(f"   source absente ou d'empreinte différente : {x['source']}")
    print("   empreinte de chaque source égale à celle écrite : vérifié (aucune ligne ci-dessus = aucune différence)")
    l1 = c1.read_text(encoding="utf-8").splitlines(keepends=True)
    l2 = c2.read_text(encoding="utf-8").splitlines(keepends=True)
    sm = difflib.SequenceMatcher(None, l1, l2, autojunk=False)
    change = "".join("".join(l2[j1:j2]) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != "equal")
    parties = [("parties changées du candidat 2", change), ("entrée 7 prévue", e7_p.read_text(encoding="utf-8"))]
    for nom, txt in parties:
        print(f"\n== {nom}")
        for h in dict.fromkeys(re.findall(r"\b[0-9a-f]{64}\b", txt)):
            f = connus.get(h)
            print(f"   {h[:16]}… -> {f.name if f else 'AUCUN FICHIER FOURNI'}")
        for m in re.finditer(r"`((?:prereg|docs)/[^`]+)`(?:\s*\(sha256\s*`([0-9a-f]{64})`\)|,\s*sha256\s*`([0-9a-f]{64})`)?",
                             txt):
            chemin, h = m.group(1), m.group(2) or m.group(3)
            x = dest.get(chemin)
            etat = ("absent du plan v2" if x is None else
                    f"au plan v2, empreinte {'égale' if (h is None or x['sha256'] == h) else 'DIFFÉRENTE'}")
            print(f"   {chemin} (cité avec {h[:12] + '…' if h else 'aucune empreinte'}) : {etat}")
    # pièces nommées sans chemin complet dans l'élément « Candidat 2 »
    for nom in ("ligne-candidat2-addendum2-v1.md",):
        hits = [d for d in dest if d.endswith("/" + nom)]
        print(f"\n« {nom} » (cité par son nom, « versé à côté » du script) : destinations au plan : {hits}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
