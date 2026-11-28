"""Épreuve R5 de la garde d'empreinte de pages_fidelite_v6.py : un cas sain, trois artefacts, dans travail/epreuve/.
Chaque essai tourne dans un processus neuf (python3 -I -B), code attendu 0 (sain) ou 3 (arrêt).
Dossier d'épreuve supprimé après usage.
Usage : python3 -I -B epreuve_garde_v6.py
"""
import hashlib, shutil, subprocess, sys
from pathlib import Path
ICI = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/verification-v6-fidelite/travail")  # chemin du lien, jamais résolu
sys.path.insert(0, str(ICI))
import pages_fidelite_v6 as pf
cle = "CC"; i = pf.IDS[cle]
src = pf.C6 / i / f"{i}.pdf"
ref = pf.refs()[cle]
ep = ICI / "epreuve"
if ep.exists():
    raise SystemExit("ARRÊT : dossier d'épreuve déjà présent")
code = ("import sys; sys.path.insert(0, %r); import pages_fidelite_v6 as pf; "
        "print('accepté' if pf.present('CC', 8, 'using fewer layers consistently yields worse performance', %r) else 'absent')")
def sain(p, c): c.write_text(f"{ref}  {p.name}\n")
def faux(p, c): c.write_text(f"{'f' * 64}  {p.name}\n")
def octets(p, c):
    with open(p, "ab") as f: f.write(b"%artefact\n")
    c.write_text(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n")
def nom_faux(p, c): c.write_text(f"{ref}  autre.pdf\n")
def sans(p, c): pass
ok = True
for k, (nom, prep, att) in enumerate([("sain", sain, 0), ("compagnon faux", faux, 3),
        ("octets ajoutés, compagnon recalculé", octets, 3), ("nom de fichier faux dans le compagnon", nom_faux, 3),
        ("compagnon absent", sans, 3)]):
    d = ep / f"e{k}" / i
    d.mkdir(parents=True)
    shutil.copyfile(src, d / f"{i}.pdf")
    prep(d / f"{i}.pdf", d / f"{i}.pdf.sha256")
    # present() appelle garde(cle) avec la racine par défaut : on passe la racine d'épreuve par un petit relais
    relais = code.replace("pf.present('CC', 8, 'using fewer layers consistently yields worse performance', %r)",
                          "(pf.garde('CC', %r) and pf.present('CC', 8, 'using fewer layers consistently yields worse performance'))")
    r = subprocess.run([sys.executable, "-I", "-B", "-c", relais % (str(ICI), str(ep / f"e{k}"))],
                       capture_output=True, text=True)
    sortie = (r.stdout + r.stderr).strip().splitlines()
    bon = r.returncode == att
    ok &= bon
    print(f"{'OK' if bon else 'FAUTE'} | {nom} | code {r.returncode} (attendu {att}) | {(sortie[-1] if sortie else '')[:100]}")
shutil.rmtree(ep)
print("# garde : " + ("conforme" if ok else "EN FAUTE") + " ; dossier d'épreuve supprimé")
sys.exit(0 if ok else 1)
