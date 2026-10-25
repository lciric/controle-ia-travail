"""Mutations des trois gardes de `reprendre()` visées par `test_reprise_refus_complementaires_v1.py` — v2 (conv-audit,
25 octobre 2026, P4C3-03) : chaque mutation retire une garde dans une copie du noyau ; les essais complémentaires doivent
échouer sur la copie mutée (garde détectée) et passer sur la copie saine.

Usage : python -I mutations_complementaires_v2.py RACINE_ESSAIM_M3 PYTHON FICHIER_ESSAIS DOSSIER_TRAVAIL
(RACINE_ESSAIM_M3 : la racine `essaim-m3-refonte-v1` d’une copie du noyau 8e5e2f7b, jamais modifiée, avec son dossier frère
`collisionneur-v2.5-banc-jev-travail/` ; v2 : ce dossier est copié aussi (la v1 l’oubliait) ; les copies vont
dans DOSSIER_TRAVAIL, neuf.)
"""
import hashlib, os, pathlib, shutil, subprocess, sys

racine, py, essais, travail = pathlib.Path(sys.argv[1]), sys.argv[2], pathlib.Path(sys.argv[3]).resolve(), pathlib.Path(sys.argv[4])
if travail.exists():
    sys.exit(f"refus : {travail} existe déjà (R12)")
SHA_BOUCLE = "8b59409679c0cb5e921ec6344b9984c7ebcdfd4a8f0f43abe7fef08ba19ed025"
if hashlib.sha256((racine / "essaim_m3/noyau/boucle.py").read_bytes()).hexdigest() != SHA_BOUCLE:
    sys.exit("refus : boucle.py n'est pas celui du noyau 8e5e2f7b")
MUTATIONS = [
    ("M1-dernier-evenement", 'if dernier.get("etape") != "arret" or dernier.get("raison") != "fichier STOP":',
     'if False:', "dernier_evenement"),
    ("M2-ronde-de-generation", 'if r["phase"] == "generation" and (not etat.get("conception_faite") or r["ronde"] != int(etat.get("ronde", -1))):',
     'if False:', "ronde_de_generation"),
    ("M3-vue-figee", 'if not (r.get("vue_figee") and vue.is_dir() and vue.resolve().is_relative_to(self.espace.resolve())):',
     'if False:', "vue_figee"),
]
travail.mkdir(parents=True)


def copie(nom):
    d = travail / nom / "essaim-m3-refonte-v1"
    d.mkdir(parents=True)
    for s in ("essaim_m3", "tests"):
        shutil.copytree(racine / s, d / s, ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(racine.parent / "collisionneur-v2.5-banc-jev-travail", d.parent / "collisionneur-v2.5-banc-jev-travail",
                    ignore=shutil.ignore_patterns("__pycache__"))  # v2 : chargé par appels.py à l'import
    return d


def courir(d, filtre=None):
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(travail), "LANG": "C.UTF-8", "ESSAIM_M3_RACINE": str(d)}
    cmd = [py, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", str(essais)] + (["-k", filtre] if filtre else [])
    p = subprocess.run(cmd, cwd=d, env=env, capture_output=True, text=True, timeout=900)
    derniere = [l for l in p.stdout.splitlines() if l.strip()][-1] if p.stdout.strip() else ""
    return p.returncode, derniere


ok = 0
code, res = courir(copie("saine"))
print(f"{'OK    ' if code == 0 else 'ÉCHEC '} saine : code {code} — {res}")
ok += code == 0
for nom, ancien, nouveau, filtre in MUTATIONS:
    d = copie(nom)
    b = d / "essaim_m3/noyau/boucle.py"
    t = b.read_text(encoding="utf-8")
    if t.count(ancien) != 1:
        sys.exit(f"refus : {nom} : {t.count(ancien)} occurrence(s) de la garde au lieu de 1")
    b.write_text(t.replace(ancien, nouveau), encoding="utf-8")
    code, res = courir(d, filtre)
    detectee = code != 0 and "failed" in res
    print(f"{'OK    ' if detectee else 'ÉCHEC '} {nom} : code {code} — {res} ({'détectée' if detectee else 'NON détectée'})")
    ok += detectee
print(f"== bilan : {ok} sur {1 + len(MUTATIONS)} conformes ==")
sys.exit(0 if ok == 1 + len(MUTATIONS) else 1)
