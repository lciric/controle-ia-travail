"""Extrait, des deux rapports de vérification de la v5, chaque correction « remplacer « ANCIEN » par « NOUVEAU » ».

Chaque rapport est contrôlé par empreinte complète. Les guillemets « » sont lus équilibrés (guillemets imbriqués gardés).
Retours à la ligne et retraits du rapport ramenés à une espace. Seul le bloc « Correction » de chaque constat est lu.
Sortie : JSON {constat: [[ancien, nouveau], ...]} sur la sortie standard.
Usage : python3 -I -B extraire_corrections.py > corrections-v5-extraites.json
"""
import hashlib
import json
import re
import sys
from pathlib import Path

RD = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection")
RAPPORTS = [
    (RD / "verification-v5-fidelite/verification-v5-fidelite-v1.md",
     "054720926c0fe16140dd5aebbb508317eb1ddbc385ac9c02032225a3ae214881",
     r"\*\*(VV5-fidelite-\d\d) — ", "## (1) Constat par constat"),
    (RD / "verification-v5-sens/verification-v5-sens-v1.md",
     "e3e4a650c9f2ce69b8f32743e609e8d80beb14acb547b1d35636e2b2b6db7036",
     r"### (VV5-sens-\d\d) — ", "## Réponses aux cinq questions"),
]


def guillemets(t, i):
    """t[i] == '«' ; retourne (contenu, indice après le '»' fermant)."""
    assert t[i] == "«", t[i:i + 20]
    prof, j = 0, i
    while j < len(t):
        if t[j] == "«":
            prof += 1
        elif t[j] == "»":
            prof -= 1
            if prof == 0:
                return t[i + 1:j], j + 1
        j += 1
    raise SystemExit(f"guillemets non fermés à {i}")


def nettoie(s):
    return re.sub(r"\s*\n\s*", " ", s).strip()


def main():
    out = {}
    for chemin, sha, motif, fin in RAPPORTS:
        b = chemin.read_bytes()
        h = hashlib.sha256(b).hexdigest()
        if h != sha:
            raise SystemExit(f"ARRÊT : {chemin.name} a l'empreinte {h}, attendue {sha}")
        t = b.decode("utf-8")
        t = t[:t.index(fin)]
        tetes = list(re.finditer(motif, t))
        for k, m in enumerate(tetes):
            bloc = t[m.start():tetes[k + 1].start() if k + 1 < len(tetes) else len(t)]
            c = bloc.find("**Correction")
            paires = []
            if c >= 0:
                corr = bloc[c:]
                for r in re.finditer(r"[Rr]emplacer\s+«", corr):
                    i = corr.index("«", r.start())
                    ancien, j = guillemets(corr, i)
                    m2 = re.match(r"\s+par\s*:?\s*«", corr[j:])
                    if not m2:
                        raise SystemExit(f"« par » introuvable après l'ancien texte de {m.group(1)}")
                    nouveau, _ = guillemets(corr, j + m2.end() - 1)
                    paires.append([nettoie(ancien), nettoie(nouveau)])
            out[m.group(1)] = paires
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
