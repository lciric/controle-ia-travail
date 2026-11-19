"""C-3 : la garde statique v7, appelée avec ses valeurs par défaut (comme en production), sur un FAUX dépôt seulement.
Un crochet d'audit de Python, écrit ici indépendamment, note chaque ouverture (`open`) et chaque listage
(`os.scandir`, `os.listdir`) sous la racine du faux dépôt. Aucun vrai dossier cloisonné n'est touché."""
import os, re, sys, tempfile
from pathlib import Path
from controle_ia.organismes_discrets import cloisonnement_bras_a_v8 as cl

racine = Path(tempfile.mkdtemp(prefix="faux-depot-")).resolve()
VUS = []
def crochet(ev, args):
    if ev in ("open", "os.scandir", "os.listdir") and args:
        c = args[0]
        if isinstance(c, (str, bytes, os.PathLike)):
            c = os.path.abspath(os.fsdecode(c))
            if c.startswith(str(racine) + os.sep):
                VUS.append((ev, os.path.relpath(c, racine).replace(os.sep, "/")))
sys.addaudithook(crochet)

FAUTIF = 'open("rangs-par-unite-moniteurs-bras-a.jsonl")\n'
P = "src/controle_ia/organismes_discrets/"
CLOISONNES = ["src/controle_ia/t07/a.py", "src/controle_ia/t07bbis/b/c.py", "src/controle_ia/bases/x.py", "src/z/sondes/y.py",
              "scripts/mots_et_cout_t06_v1.py", "scripts/mots_et_cout_dir/lot.sh", "src/autres_moniteurs_v8.py",
              P + "bras_a_v2_habilite/k.py", "scripts/lancer_t08_v1.py", "src/T0.8/q.py", "scripts/t0-8.mk"]
CLOISONNES += ["src/T07/x.py", "src/Bases/x.py", "src/SONDES/y/z.py", "scripts/Mots_Et_Cout_x.py"]
VOISINS = ["src/sondes_v2/x.py", "scripts/t07_outil.py", "src/controle_ia/t06/x.py"]
for n in CLOISONNES + VOISINS + ["src/sain.py"]:
    p = racine / n; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(FAUTIF if n != "src/sain.py" else "x = 1\n")
# liens symboliques : un dossier et un fichier cloisonnés, sous des noms ordinaires
os.symlink(racine / "src/controle_ia/t07", racine / "src/lien_vers_t07")
os.symlink(racine / "src/controle_ia/bases/x.py", racine / "src/lien_vers_bases.py")
# lien physique : le fichier cloisonné, sous un nom ordinaire (limite : la garde le lit, c'est le même fichier)
os.link(racine / "src/controle_ia/t07/a.py", racine / "src/lien_physique.py")

VUS.clear()
v = cl.violations_de_la_garde_statique(racine)            # défauts : dossiers src et scripts
VUS_GARDE = list(VUS); VUS.clear()
L = cl.listages_a_relire(racine)
VUS_LISTAGES = list(VUS); VUS.extend(VUS_GARDE)
e = cl.chemins_elagues(racine)
cloisonne = re.compile(r"(^|/)(bases|sondes|t07[^/]*|bras_a_v2_habilite)/|mots_et_cout_|autres_moniteurs_v|(?<![a-z0-9])t0[._-]?8(?![0-9])", re.I)
touches = [x for x in VUS if cloisonne.search(x[1])]
print("ouvertures et listages notés (garde + listages_a_relire) :", len(VUS), "| dont listages_a_relire seul :", len(VUS_LISTAGES))
print("listages_a_relire, sous un chemin cloisonné :", [x for x in VUS_LISTAGES if cloisonne.search(x[1]) and not x[1].startswith("scripts/t07_outil")])
print("dont sous un chemin cloisonné (selon le crochet, insensible à la casse) :", touches)
print("élagués :", e)
for n in VOISINS + ["src/lien_vers_t07", "src/lien_vers_bases.py", "src/lien_physique.py", "src/sain.py"]:
    print(("VIOLATION " if any(x.startswith(n) for x in v) else "rien      ") + n)
print("violations sur les cloisonnés :", [x for x in v if any(x.startswith(c) for c in CLOISONNES)])
# départ cloisonné demandé par l'appelant
try:
    cl.violations_de_la_garde_statique(racine, ["src/controle_ia/t07"]); print("départ cloisonné : ACCEPTÉ")
except Exception as x:
    print("départ cloisonné : refusé —", str(x)[:90])
try:
    cl.violations_de_la_garde_statique(racine, ["src/../src/controle_ia/t07"]); print("départ par `..` : ACCEPTÉ")
except Exception as x:
    print("départ par `..` : refusé —", str(x)[:90])
