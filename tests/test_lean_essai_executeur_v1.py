"""Essais R5 de l'exécuteur du bac (essai Lean, D-1a) hors machine.

Le lanceur « essai-local » n'isole rien : il éprouve la plomberie (dossier neuf par item, contrôle écrit après la compilation et
hors du dossier de l'agent, empreinte du contrôle, lecture des sorties, nettoyage) avec un **faux `lean`** qui imite le format
de `lean --json`. L'isolement lui-même (bwrap, systemd-run, lecture seule, réseau) n'est éprouvable que sur la machine.
"""
import json
import sys
from pathlib import Path

import pytest

from controle_ia.lean_essai import executeur_bac_v1 as X

FAUX_LEAN = r'''
import json, os, re, sys
args = sys.argv[1:]
fichier = args[-1]
src = open(fichier, encoding="utf-8").read()
def msg(ligne, data, sev="information"):
    print(json.dumps({"severity": sev, "pos": {"line": ligne, "column": 0}, "data": data}))
if "-o" in args:
    if "ERREUR_FACTICE" in src:
        msg(3, "type mismatch", "error"); sys.exit(1)
    if "sorry" in src:
        msg(4, "declaration uses 'sorry'", "warning")
    pref = "Triche." if "namespace Triche" in src else ""
    d = {"theoremes": [pref + n for n in re.findall(r"theorem (\w+)", src)],
         "axiomes": re.findall(r"axiom (\w+)", src), "defs": re.findall(r"def (\w+)", src),
         "instance_anonyme": "instance :" in src, "sorry": "sorry" in src, "alterer": "ALTERER_CONTROLE" in src}
    open(args[args.index("-o") + 1], "w").write(json.dumps(d))
    sys.exit(0)
olean = None
for d in os.environ.get("LEAN_PATH", "").split(":"):
    if d and os.path.isfile(os.path.join(d, "Item.olean")):
        olean = json.load(open(os.path.join(d, "Item.olean")))
if olean is None:
    msg(1, "unknown module prefix 'Item'", "error"); sys.exit(1)
erreur = False
for n, ligne in enumerate(src.splitlines(), 1):
    m = re.match(r"#check @(\S+)$", ligne)
    if m:
        if m.group(1) in olean["theoremes"]:
            msg(n, m.group(1) + " : énoncé factice")
        else:
            msg(n, "unknown identifier '%s'" % m.group(1), "error"); erreur = True
        continue
    m = re.match(r"#print axioms (\S+)$", ligne)
    if m:
        if m.group(1) not in olean["theoremes"]:
            msg(n, "unknown constant", "error"); erreur = True; continue
        ax = ["propext", "Classical.choice", "Quot.sound"] + (["sorryAx"] if olean["sorry"] else []) + olean["axiomes"]
        msg(n, "'%s' depends on axioms: [%s]" % (m.group(1), ", ".join(ax)))
        continue
    m = re.match(r"#print (\S+)$", ligne)
    if m:
        if m.group(1) in olean["defs"]:
            msg(n, "def %s : ℕ := 1" % m.group(1))
        else:
            msg(n, "unknown constant", "error"); erreur = True
        continue
    if ligne.startswith("open Lean in #eval"):
        cs = ["%s theoreme" % t for t in olean["theoremes"]] + ["%s axiome" % a for a in olean["axiomes"]]
        cs += ["%s definition" % x for x in olean["defs"]] + (["instAddBoite definition"] if olean["instance_anonyme"] else [])
        msg(n, "\n".join("CONSTANTE " + c for c in cs) + "\nCONSTANTES-FIN\n")
if olean["alterer"]:
    open(fichier, "a").write("-- altéré à l'import\n")
sys.exit(1 if erreur else 0)
'''

SAIN = "theorem etape_1 : True := trivial\ntheorem etape_2 : True := trivial\ntheorem enonce_item : True := trivial\n"


@pytest.fixture
def bac(tmp_path):
    faux = tmp_path / "faux_lean.py"
    faux.write_text(FAUX_LEAN, encoding="utf-8")
    racines = {}
    for nom in ("items", "controle", "sorties"):
        racines[nom] = tmp_path / nom
        racines[nom].mkdir()
    cfg = X.Config(lean=str(faux), lean_path=str(tmp_path / "vide"), python=sys.executable,
                   racine_items=racines["items"], racine_controle=racines["controle"],
                   racine_sorties=racines["sorties"], mode="essai-local", duree_max_s=60)
    # le faux `lean` est un script Python : on l'appelle par l'interpréteur
    lanceur = X.LanceurEssaiLocal(cfg)
    origine = lanceur.lancer

    def lancer(l, unite):
        if l.argv and l.argv[0] == str(faux):
            l = X.Lancement([sys.executable, "-I", "-B"] + l.argv, l.liaisons, l.chdir, l.env, l.sortie, l.erreurs)
        return origine(l, unite)
    lanceur.lancer = lancer
    return X.Bac(cfg, lanceur), racines


def vide(racines):
    return all(not list(p.iterdir()) for p in racines.values())


def test_sain_accepte_et_rien_ne_persiste(bac):
    b, racines = bac
    r = b.verifier_lean("item-sain-0001", SAIN, 2)
    assert r["verdict"]["accepte_gardes"], {g: x["motifs"] for g, x in r["verdict"]["gardes"].items() if x["motifs"]}
    assert r["isolement"] is False and r["mode"] == "essai-local"
    assert vide(racines) and r["dossiers_restants"] == []
    assert r["verdict"]["enonces_imprimes"]["etape_1"] == "etape_1 : énoncé factice"


def test_artefact_sorry(bac):
    b, _ = bac
    r = b.verifier_lean("item-sorry-0001", SAIN.replace("theorem etape_2 : True := trivial",
                                                        "theorem etape_2 : True := by sorry"), 2)
    assert not r["verdict"]["gardes"]["G-L2"]["ok"]


def test_artefact_compilation(bac):
    b, racines = bac
    r = b.verifier_lean("item-erreur-0001", SAIN + "-- ERREUR_FACTICE\n", 2)
    assert not r["verdict"]["gardes"]["G-L1"]["ok"] and vide(racines)


def test_artefact_espace_de_noms_vu_par_le_controle(bac):
    b, _ = bac
    r = b.verifier_lean("item-noms-0001", "namespace Triche\n" + SAIN + "end Triche\n", 2)
    g = r["verdict"]["gardes"]
    assert g["G-L1"]["ok"] and not g["G-L4"]["ok"]


def test_artefact_instance_anonyme_vue_par_l_enumeration(bac):
    b, _ = bac
    r = b.verifier_lean("item-inst-0001", "structure Boite where\n  v : Nat\ninstance : Add Boite := ⟨fun a b => a⟩\n" + SAIN, 2)
    assert any("instAddBoite" in x for x in r["verdict"]["gardes"]["G-L6"]["motifs"])


def test_artefact_controle_altere_pendant_son_execution(bac):
    """G-L7 : l'empreinte du fichier de contrôle est relevée avant et après son exécution."""
    b, _ = bac
    r = b.verifier_lean("item-alt-0001", SAIN + "-- ALTERER_CONTROLE\n", 2)
    assert any("modifié" in x for x in r["verdict"]["gardes"]["G-L7"]["motifs"])


def test_garde_dossier_neuf_sain_et_artefact(bac):
    b, racines = bac
    b.verifier_lean("item-neuf-0001", SAIN, 2)  # sain : le même identifiant redevient libre après nettoyage
    (racines["items"] / "item-reste-0001").mkdir()
    with pytest.raises(X.ErreurBac, match="dossier neuf"):
        b.verifier_lean("item-reste-0001", SAIN, 2)
    with pytest.raises(X.ErreurBac, match="identifiant"):
        b.verifier_lean("../evasion", SAIN, 2)


def test_python_sain_et_persistance(bac):
    b, racines = bac
    r = b.executer_python("py-sain-0001", "import sys\nprint('SAIN', 1 + 1)\nopen('trace.txt', 'w').write('x')\n")
    assert r["execution"]["code"] == 0 and "SAIN 2" in r["stdout"] and vide(racines)
    r = b.executer_python("py-sain-0002", "import os\nprint(os.path.exists('trace.txt'))\n")
    assert "False" in r["stdout"]


def test_refus_du_lanceur_sans_isolement_hors_essai(tmp_path):
    cfg = X.Config(lean="lean", lean_path="", mode="bac")
    with pytest.raises(X.ErreurBac):
        X.LanceurEssaiLocal(cfg)
    cfg_local = X.Config(lean="lean", lean_path="", mode="essai-local")
    with pytest.raises(X.ErreurBac):
        X.Bac(cfg, X.LanceurEssaiLocal(cfg_local))
    with pytest.raises(X.ErreurBac):
        X.Bac(cfg_local)  # mode essai-local : lanceur explicite exigé


def test_commande_du_bac():
    cfg = X.Config(lean="/opt/elan/toolchains/t/bin/lean", lean_path="/opt/mathlib/.lake/build/lib/lean")
    l = X.Lancement(argv=[cfg.lean, "--json", "/item/Item.lean"], liaisons={"/item": ("/srv/items/abc12345", True)},
                    chdir="/item", env={"HOME": "/tmp"}, sortie=Path("/srv/sorties/s/c.out"),
                    erreurs=Path("/srv/sorties/s/c.err"))
    c = X.LanceurBac(cfg, verifier_hote=False).commande(l, "bac-x")
    texte = " ".join(c)
    for attendu in ("User=bac", "IPAddressDeny=any", "MemoryMax=6G", "LimitCPU=1800", "RuntimeMaxSec=2100",
                    "TasksMax=256", "MemorySwapMax=0", "--unshare-all", "--die-with-parent", "--clearenv",
                    "--ro-bind /opt/elan /opt/elan", "--ro-bind /opt/mathlib /opt/mathlib",
                    "--ro-bind /opt/pybac /opt/pybac", "--bind /srv/items/abc12345 /item", "--tmpfs /tmp",
                    "StandardOutput=file:/srv/sorties/s/c.out"):
        assert attendu in texte, attendu
    for absent in ("/srv/leurre", "/srv/controle", "/root", "/home", "/opt/harnais", "--share-net"):
        assert absent not in texte, absent
    i = c.index("--remount-ro")
    assert c[i + 1] == "/" and i > c.index("--bind") and c.index("--") > i
    assert c[0] == "systemd-run" and c[c.index("--") + 1] == cfg.lean


def test_resume_systemd():
    r = X.lire_resume_systemd("Running as unit: bac-x.service\nFinished with result: success\n"
                              "Main processes terminated with: code=exited/status=0\nService runtime: 1min 2.5s\n"
                              "CPU time consumed: 12.250s\nMemory peak: 1.4G\n")
    assert r == {"cpu_s": 12.25, "memoire_pic": "1.4G", "duree_service_s": 62.5, "resultat": "success"}
    assert X.duree_systemd("rien") is None


def test_charger_config(tmp_path):
    p = tmp_path / "chaine-v1.json"
    p.write_text(json.dumps({"lean": "/l", "lean_path": "/p", "variante_enumeration": ""}))
    with pytest.raises(X.ErreurBac, match="variante_enumeration"):
        X.charger_config(p)
    p.write_text(json.dumps({"lean": "/l", "lean_path": "/p", "variante_enumeration": "B"}))
    assert X.charger_config(p).variante_enumeration == "B"
