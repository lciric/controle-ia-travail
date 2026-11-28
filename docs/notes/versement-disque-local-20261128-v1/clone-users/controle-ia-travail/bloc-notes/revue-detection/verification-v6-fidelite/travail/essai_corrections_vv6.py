"""Essai des corrections VV6-fidelite-01 à 04 : chaque ancien texte trouvé une seule fois dans la v6 (blancs ramenés à
« au moins un blanc »), puis appliqué sur une copie en mémoire ; rien n'est écrit. Épreuve R5 : un ancien texte altéré
d'un mot doit être introuvable.
Usage : python3 -I -B essai_corrections_vv6.py V6.md
"""
import hashlib, re, sys
from pathlib import Path
CORR = [
 ("VV6-fidelite-01",
  "(c) P3b sans les bras du champ, avec l'oracle et la manipulation du nombre ; la lecture « double comptabilité », décidée (GO-2026-10-20-10), reste sous toutes les options (avantage : rien de déjà vu ; inconvénient : pas de plancher au champ). Recommandation : (a), confiance ≈ 65 %.",
  "(c) P3b sans les bras du champ, avec l'oracle et la manipulation du nombre (avantage : rien de déjà vu ; inconvénient : pas de plancher au champ). La lecture « double comptabilité », décidée (GO-2026-10-20-10), reste sous toutes les options. Recommandation : (a), confiance ≈ 65 %."),
 ("VV6-fidelite-02",
  "coûts déjà déclarés : premier pas, ou (b), (c) des règles communes ; nombres avant le champ et coûts déjà déclarés : contrôle mécanique",
  "coûts déjà déclarés : premier pas, ou (b), (c) des règles communes ; bras de production : nombres avant le champ et coûts déjà déclarés : contrôle mécanique"),
 ("VV6-fidelite-03",
  "La revue emploie T4 « à coût déclaré égal » comme contrôle du nombre écrit (sections 4 et 5) : il est touché",
  "La v5 employait T4 « à coût déclaré égal » comme contrôle du nombre écrit (sections 4 et 5) : il est touché"),
 ("VV6-fidelite-04",
  "renvoie partout, section « Décisions prises depuis la v4 » comprise, au document de P-015 (`6e74c6cb…`) ;",
  "renvoie partout, section « Décisions prises depuis la v4 » comprise, au document de P-015 (`6e74c6cb…`), sauf « P-015 l. 392 » dans la liste « v5 » des Sources (ligne du registre) ;"),
]
ARTEFACT = ("artefact (mot changé)", "La revue emploie T4 « à coût écrit égal » comme contrôle du nombre écrit (sections 4 et 5) : il est touché")
b = Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(b).hexdigest() == "124d06f821f5780dbc810d710d08a3d00239ae34e8545fe69c3ea683177511e8"
t = b.decode("utf-8")
t0 = t
motif = lambda a: r"\s+".join(re.escape(x) for x in a.split())
ok = True
for nom, a, n in CORR:
    m = list(re.finditer(motif(a), t))
    ok &= len(m) == 1
    print(f"{'OK' if len(m) == 1 else 'FAUTE'} | {nom} | ancien trouvé {len(m)} fois" + (f", v6 l. {t0.count(chr(10), 0, list(re.finditer(motif(a), t0))[0].start()) + 1}" if m else ""))
    if len(m) == 1:
        t = t[:m[0].start()] + n + t[m[0].end():]
        ok &= t.count(n) == 1
k = len(re.findall(motif(ARTEFACT[1]), Path(sys.argv[1]).read_text(encoding="utf-8")))
ok &= k == 0
print(f"{'rejeté' if k == 0 else 'ACCEPTÉ (faute)'} | {ARTEFACT[0]} | trouvé {k} fois")
print("# BILAN : " + ("conforme" if ok else "FAUTE"))
sys.exit(0 if ok else 1)
