"""Vérification des corrections de la batterie (v3) — empreintes citées dans la v3 et dans la réponse — v1.

Lit la table « Empreintes » de `batterie-fuite-banque-revisee-v3.md` et de `reponse-contre-lecture-batterie-v1.md`,
résout chaque chemin (les préfixes « …/ » d'après le dossier), recalcule le SHA-256 du fichier et le compare à
l'empreinte citée et à son compagnon `.sha256`. Contrôle aussi les préfixes courts cités dans le texte (8 signes).
Processeur seul. Emploi : python3 -I verif_empreintes_v1.py DEPOT > SORTIE.txt
"""
import hashlib, re, sys
from pathlib import Path

DEPOT = Path(sys.argv[1]).resolve()
BR = DEPOT / "docs/notes/mathematiques-nouvelles-v1/banque-revisee-v1"
BAT = BR / "batterie-v1"


def resoudre(c):
    if c.startswith("…/batterie-v1/"):
        return BAT / c[len("…/batterie-v1/"):]
    if c.startswith("…/calculs-d-appui/"):
        return BAT / "calculs-d-appui" / c[len("…/calculs-d-appui/"):]
    if c.startswith("…/banque-revisee-v1/"):
        return BR / c[len("…/banque-revisee-v1/"):]
    return DEPOT / c


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


ecarts = 0
for nom in ("batterie-fuite-banque-revisee-v3.md", "reponse-contre-lecture-batterie-v1.md"):
    texte = (BAT / nom).read_text(encoding="utf-8")
    print(f"== {nom} ({sha(BAT / nom)})")
    for chemin, h in re.findall(r"`([^`]+)`\s*\|\s*`([0-9a-f]{64})`", texte):
        p = resoudre(chemin)
        if not p.exists():
            print(f"  ABSENT  {chemin}"); ecarts += 1; continue
        a = sha(p)
        comp = Path(str(p) + ".sha256")
        c = comp.read_text().split()[0] if comp.exists() else None
        ok = a == h and c == h
        ecarts += not ok
        print(f"  {'OK    ' if ok else 'ECART '}  {chemin}  cité {h[:12]}…  fichier {a[:12]}…  compagnon {(c or 'absent')[:12]}")
    # préfixes courts « `xxxxxxxx…` » : chacun doit être le début d'une empreinte d'un fichier du dépôt cité
    courts = sorted(set(re.findall(r"`([0-9a-f]{8})…`", texte)))
    connus = {}
    for comp in list(BR.rglob("*.sha256")) + [DEPOT / "prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon-4-v2.md.sha256"]:
        if comp.exists():
            connus[comp.read_text().split()[0][:8]] = comp.name
    for c in courts:
        print(f"  court {c}… -> {connus.get(c, 'INCONNU')}")
        ecarts += c not in connus
print(f"écarts : {ecarts}")
