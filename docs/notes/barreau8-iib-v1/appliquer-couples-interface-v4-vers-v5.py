"""Note d'interface v5 : applique à la v4 les couples N-01 à N-04 du rapport de vérification de la v4 et du programme des états
(côté exposé), lus ligne à ligne dans le rapport (« avant : « … » », « après : « … » »), dans l'ordre ; chaque « avant » présent
une seule fois. Pour N-03, deux résolutions déclarées, appliquées au texte « après » avant son remplacement :
- option (a), tranchée par la mère (message du 2026-11-19 vers 00:57Z) : les crochets « [option (a) : … ] » sont retirés,
  la forme des clés est gardée telle quelle, précédée de « : » ;
- « `<nom fixé par la mère>` » : remplacé par le nom proposé par l'exécutante, `NOM_EXTRAIT` ci-dessous (à confirmer par la mère).
Usage : python … <rapport> <note v4> <note v5>
"""
import hashlib
import re
import sys
from pathlib import Path

NOM_EXTRAIT = "etats-lectures-iib-v1.json"
rapport, v4, v5 = sys.argv[1:4]
r = Path(rapport).read_text(encoding="utf-8")
t = Path(v4).read_text(encoding="utf-8")
for p, h in ((r, "fcc78e15e351f540031e20874b11c509c06e034a35af3fc81e6e006a9ebb2e89"),
             (t, "1983692a79b4802a4d13edc3cf9a9bb21eca0dfb2c860ecf5831431d532c99f7")):
    if hashlib.sha256(p.encode()).hexdigest() != h:
        raise SystemExit(f"empreinte inattendue (attendue {h[:12]})")
bloc = r.split("### Sur la note")[1].split("### Sur le programme des états")[0]
couples = []
for nom in ("N-01", "N-02", "N-03", "N-04"):
    corps = bloc.split(f"**{nom}**")[1].split("**N-0")[0]
    av = [l for l in corps.splitlines() if l.startswith("avant : « ")]
    ap = [l for l in corps.splitlines() if l.startswith("après : « ")]
    if len(av) != 1 or len(ap) != 1 or not av[0].endswith(" »") or not ap[0].endswith(" »"):
        raise SystemExit(f"{nom} : lignes avant/après illisibles")
    couples.append((nom, av[0][len("avant : « "):-2], ap[0][len("après : « "):-2]))
for nom, avant, apres in couples:
    if nom == "N-03":
        n1, n2 = apres.count("[option (a) : "), apres.count("`<nom fixé par la mère>`")
        if n1 != 1 or n2 != 1:
            raise SystemExit("N-03 : résolutions introuvables")
        apres = re.sub(r"\[option \(a\) : (.*?)\]", r": \1", apres, count=1)
        apres = apres.replace("`<nom fixé par la mère>`", f"`{NOM_EXTRAIT}`")
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"{nom} : « avant » présent {n} fois")
    t = t.replace(avant, apres)
    print(f"{nom} appliqué")
if Path(v5).exists():
    raise SystemExit(f"{v5} existe déjà : R12")
Path(v5).write_text(t, encoding="utf-8")
print(v5, hashlib.sha256(t.encode()).hexdigest())
