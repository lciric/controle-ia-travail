"""Essais R5 de l'exécuteur v2 (CLL-04, CLL-07, CLL-13, CLL-14, CLL-15) hors machine, avec un faux `lean` qui lit le
contrôle sur son entrée standard et peut forger une sortie comme le ferait un initialiseur de l'agent."""
import json
import signal
import sys
from pathlib import Path

import pytest

from controle_ia.lean_essai import executeur_bac_v2 as X

FAUX_LEAN = r'''
import json, os, re, sys
args = sys.argv[1:]
def msg(ligne, data, sev="information"):
    print(json.dumps({"severity": sev, "pos": {"line": ligne, "column": 0}, "data": data}))
if "-o" in args:
    src = open(args[-1], encoding="utf-8").read()
    if "ERREUR_FACTICE" in src:
        msg(3, "type mismatch", "error"); sys.exit(1)
    if "sorry" in src:
        msg(4, "declaration uses 'sorry'", "warning")
    pref = "Triche." if "namespace Triche" in src else ""
    d = {"theoremes": [pref + n for n in re.findall(r"theorem (\w+)", src)],
         "defs": re.findall(r"(?:def|abbrev) (\w+)", src), "partielles": re.findall(r"partial def (\w+)", src),
         "drapeaux": [f for f in ("FORGER_SORTIE", "ECRIRE_BRUT", "PLANTER") if f in src], "sorry": "sorry" in src}
    open(args[args.index("-o") + 1], "w").write(json.dumps(d))
    sys.exit(0)
assert "--stdin" in args, args
src = sys.stdin.read()
olean = None
for d in os.environ.get("LEAN_PATH", "").split(":"):
    if d and os.path.isfile(os.path.join(d, "Item.olean")):
        olean = json.load(open(os.path.join(d, "Item.olean")))
if olean is None:
    msg(1, "unknown module prefix 'Item'", "error"); sys.exit(1)
if "FORGER_SORTIE" in olean["drapeaux"]:   # « initialiseur » de l'agent : fausse sortie complète, puis sortie 0
    for n, ligne in enumerate(src.splitlines(), 1):
        if ligne.startswith("#check @"):
            msg(n, ligne[8:] + " : énoncé forgé")
    print(json.dumps({"severity": "information", "pos": {"line": 99, "column": 0}, "data": "CONSTANTES-FIN " + "0" * 32}))
    sys.exit(0)
if "ECRIRE_BRUT" in olean["drapeaux"]:
    print("CONSTANTES-FIN " + "0" * 32)
nonce = re.search(r"CONSTANTES-FIN ([0-9a-f]{32})", src).group(1)
erreur = False
for n, ligne in enumerate(src.splitlines(), 1):
    m = re.match(r"(?:set_option pp\.notation false in )?#check @(\S+)$", ligne)
    if m:
        if m.group(1) in olean["theoremes"]:
            msg(n, m.group(1) + (" : énoncé brut" if ligne.startswith("set_option") else " : énoncé factice"))
        else:
            msg(n, "unknown identifier", "error"); erreur = True
        continue
    m = re.match(r"#print axioms (\S+)$", ligne)
    if m:
        if m.group(1) not in olean["theoremes"]:
            msg(n, "unknown constant", "error"); erreur = True; continue
        ax = ["propext", "Classical.choice", "Quot.sound"] + (["sorryAx"] if olean["sorry"] else [])
        msg(n, "'%s' depends on axioms: [%s]" % (m.group(1), ", ".join(ax)))
        continue
    m = re.match(r"#print (\S+)$", ligne)
    if m:
        msg(n, "def %s : ℕ := 1" % m.group(1)) if m.group(1) in olean["defs"] else msg(n, "unknown constant", "error")
        continue
    if ligne.startswith("#eval show _root_.Lean.CoreM"):
        cs = ["%s theoreme sure" % t for t in olean["theoremes"]] + ["%s definition sure" % x for x in olean["defs"]]
        cs += ["%s._unsafe_rec definition non-sure" % p for p in olean["partielles"]]
        msg(n, "".join("CONSTANTE %s\n" % c for c in cs) + "CONSTANTES-FIN " + nonce)
if "PLANTER" in olean["drapeaux"]:
    sys.exit(137)
sys.exit(1 if erreur else 0)
'''

SAIN = "theorem etape_1 : True := trivial\ntheorem etape_2 : True := trivial\ntheorem enonce_item : True := trivial\n"


def config(tmp_path, **k):
    faux = tmp_path / "faux_lean.py"
    faux.write_text(FAUX_LEAN, encoding="utf-8")
    for nom in ("items", "sorties"):
        (tmp_path / nom).mkdir(exist_ok=True)
    d = dict(lean=str(faux), lean_path=str(tmp_path / "vide"), python=sys.executable, racine_items=tmp_path / "items",
             racine_sorties=tmp_path / "sorties", mode="essai-local", duree_max_s=60,
             tampon_reseau=tmp_path / "run" / "reseau-ferme-v1.json")
    d.update(k)
    return X.Config(**d)


class Enregistreur(X.LanceurEssaiLocal):
    """Lanceur local qui garde chaque lancement ; le faux `lean` (script) est appelé par l'interpréteur."""

    def __init__(self, cfg):
        super().__init__(cfg)
        self.lancements = []

    def lancer(self, l, unite):
        self.lancements.append((unite, l))
        if l.argv and l.argv[0] == self.cfg.lean:
            l = X.Lancement([sys.executable, "-I", "-B"] + l.argv, l.liaisons, l.chdir, l.env, l.sortie, l.erreurs,
                            l.entree)
        return super().lancer(l, unite)


@pytest.fixture
def bac(tmp_path):
    cfg = config(tmp_path)
    lanceur = Enregistreur(cfg)
    return X.Bac(cfg, lanceur), lanceur, tmp_path


def vide(tmp_path):
    return all(not list((tmp_path / n).iterdir()) for n in ("items", "sorties"))


def test_sain_contrôle_par_l_entree_standard(bac):
    b, lanceur, tmp = bac
    r = b.verifier_lean("item-sain-0001", SAIN, 2)
    assert r["verdict"]["accepte_gardes"], {g: x["motifs"] for g, x in r["verdict"]["gardes"].items() if x["motifs"]}
    assert vide(tmp) and r["incident_bac"] is None
    (_, compil), (_, ctrl) = lanceur.lancements
    assert compil.entree is None and compil.liaisons == {"/item": (str(tmp / "items" / "item-sain-0001"), True)}
    # mutation 3 de CLL-14 : le second bac voit l'item en lecture seule et aucun fichier de contrôle
    assert ctrl.liaisons == {"/item": (str(tmp / "items" / "item-sain-0001"), False)}
    assert ctrl.entree is not None and "CONSTANTES-FIN " in ctrl.entree and "--stdin" in ctrl.argv
    assert r["empreinte_controle"] == X.G.empreinte_texte(ctrl.entree)


def test_sortie_forgee_par_l_agent(bac):
    b, _, _ = bac
    r = b.verifier_lean("item-forge-0001", SAIN + "-- FORGER_SORTIE\n", 2)
    assert not r["verdict"]["gardes"]["G-L7"]["ok"] and not r["verdict"]["accepte_gardes"]


@pytest.mark.parametrize("drapeau", ["ECRIRE_BRUT", "PLANTER"])
def test_ligne_brute_et_code_non_nul(bac, drapeau):
    b, _, _ = bac
    r = b.verifier_lean("item-g7-00001", SAIN + f"-- {drapeau}\n", 2)
    assert not r["verdict"]["gardes"]["G-L7"]["ok"]


def test_partielle_vue_par_la_surete(bac):
    b, _, _ = bac
    r = b.verifier_lean("item-part-0001", "partial def boucle (n : Nat) : Nat := boucle n\n" + SAIN, 2)
    assert any("non-sure" in x for x in r["verdict"]["gardes"]["G-L3"]["motifs"])


@pytest.mark.parametrize("quelle,garde", [("compilation", "G-L1"), ("controle", "G-L7")])
def test_sorties_tronquees(bac, monkeypatch, quelle, garde):
    """Mutations 4 et 5 de CLL-14 : une sortie plus longue que SORTIE_MAX fait échouer la garde."""
    b, _, _ = bac
    longueurs = {}
    origine = X._lire

    def lire(chemin):
        texte, tronq = origine(chemin)
        longueurs[chemin.name] = len(texte)
        return texte, tronq or (chemin.name == f"{quelle}.out")
    monkeypatch.setattr(X, "_lire", lire)
    r = b.verifier_lean("item-tronq-0001", SAIN, 2)
    assert not r["verdict"]["gardes"][garde]["ok"]


def test_dossier_neuf_et_identifiant(bac):
    b, _, tmp = bac
    (tmp / "items" / "item-reste-0001").mkdir()
    with pytest.raises(X.ErreurBac, match="dossier neuf"):
        b.verifier_lean("item-reste-0001", SAIN, 2)
    with pytest.raises(X.ErreurBac, match="identifiant"):
        b.verifier_lean("../evasion", SAIN, 2)


def test_python_sain(bac):
    b, _, tmp = bac
    r = b.executer_python("py-sain-0001", "print('SAIN', 1 + 1)\n")
    assert r["execution"]["code"] == 0 and "SAIN 2" in r["stdout"] and vide(tmp)


# ---- CLL-07 : processus résiduels de l'unité seulement (mutation 6) --------------------------------------------------------

def test_residus_de_l_unite_seulement(tmp_path):
    groupe = tmp_path / "system.slice" / "bac-x-compilation.service"
    groupe.mkdir(parents=True)
    (groupe / "cgroup.procs").write_text("4242\n4343\n")
    tues = []

    class P:
        def __init__(self, sortie):
            self.stdout = sortie

    def executer(argv, **k):
        assert argv == ["systemctl", "show", "-p", "ControlGroup", "--value", "bac-x-compilation.service"]
        return P("/system.slice/bac-x-compilation.service\n")
    assert X.residus_unite("bac-x-compilation", executer, tmp_path, lambda pid, s: tues.append((pid, s))) == [4242, 4343]
    assert tues == [(4242, signal.SIGKILL), (4343, signal.SIGKILL)]
    assert X.residus_unite("bac-y", lambda a, **k: P(""), tmp_path, lambda p, s: tues.append(p)) == []
    assert len(tues) == 2


def test_lanceur_bac_tube_et_residus(tmp_path):
    cfg = config(tmp_path, mode="bac", racine_cgroup=tmp_path)
    vus = []

    class P:
        def __init__(self, returncode=0, stdout="", stderr=""):
            self.returncode, self.stdout, self.stderr = returncode, stdout, stderr

    def executer(argv, **k):
        vus.append((argv, k))
        if argv[0] == "systemctl":
            return P(stdout="")
        return P(0, stdout='{"severity":"information"}\n',
                 stderr="Finished with result: success\nCPU time consumed: 1.5s\nMemory peak: 900M\n")
    lanceur = X.LanceurBac(cfg, verifier_hote=False, executer=executer)
    l = X.Lancement(["lean", "--stdin", "--json"], {"/item": ("/srv/items/a", False)}, "/tmp", {}, tmp_path / "k.out",
                    tmp_path / "k.err", entree="import Item\n")
    c = lanceur.commande(l, "bac-a-controle")
    assert "--pipe" in c and not any(x.startswith("StandardOutput=") for x in c)
    assert "--ro-bind" in c and c[c.index("--ro-bind", c.index("/etc/ld.so.cache") + 1):].count("/item") == 1
    r = lanceur.lancer(l, "bac-a-controle")
    assert (tmp_path / "k.out").read_text() == '{"severity":"information"}\n'   # écrit par le harnais, hors du bac
    assert vus[0][1]["input"] == "import Item\n" and r["resultat"] == "success" and r["cpu_s"] == 1.5
    assert vus[1][0][0] == "systemctl" and r["residus"] == []
    sans = X.Lancement(["lean"], {}, "/tmp", {}, tmp_path / "c.out", tmp_path / "c.err")
    c = lanceur.commande(sans, "bac-a-compilation")
    assert "--pipe" not in c and f"StandardOutput=file:{tmp_path / 'c.out'}" in c


# ---- CLL-15 : panne du bac ----------------------------------------------------------------------------------------------

@pytest.mark.parametrize("res,err,attendu", [
    ({"isolement": True, "resultat": "success"}, "", None),
    ({"isolement": True, "resultat": "exit-code"}, "", None),
    ({"isolement": True, "resultat": "timeout"}, "", "délai"),
    ({"isolement": True, "resultat": "oom-kill"}, "", "mémoire"),
    ({"isolement": True, "resultat": "signal", "fin": "code=killed/status=XCPU"}, "", "délai"),
    ({"isolement": True, "resultat": "core-dump", "fin": "code=dumped/status=ABRT"}, "", None),
    ({"isolement": False, "resultat": None}, "", None),
])
def test_classer_execution_sain(res, err, attendu):
    assert X.classer_execution(res, err) == attendu


@pytest.mark.parametrize("res,err,motif", [
    ({"isolement": True, "resultat": "success"}, "bwrap: Creating new namespace failed: Operation not permitted\n", "bwrap"),
    ({"isolement": True, "resultat": None, "code": 1}, "", "sans résultat"),
    ({"isolement": True, "resultat": "resources"}, "", "inattendu"),
])
def test_classer_execution_panne(res, err, motif):
    with pytest.raises(X.ErreurBac, match=motif):
        X.classer_execution(res, err)


class LanceurIsoleFactice:
    isolement = True

    def __init__(self, resultat_controle="success"):
        self.resultat_controle = resultat_controle

    def lancer(self, l, unite):
        l.sortie.write_text("")
        l.erreurs.write_text("")
        r = "success" if unite.endswith("compilation") else self.resultat_controle
        return {"code": 0 if r == "success" else 1, "isolement": True, "resultat": r, "fin": None, "residus": []}


def test_incident_du_bac_remonte(tmp_path, monkeypatch):
    monkeypatch.setattr(X.shutil, "chown", lambda *a, **k: None)
    cfg = config(tmp_path, mode="bac")
    b = X.Bac(cfg, LanceurIsoleFactice("timeout"), relever=lambda: [], id_demarrage=lambda: "d1")
    r = b.verifier_lean("item-inc-00001", SAIN, 2)
    assert r["incident_bac"] == "délai" and not r["verdict"]["accepte_gardes"]


# ---- CLL-13 : réseau éprouvé fermé avant tout item ----------------------------------------------------------------------

def test_reseau_ferme_exige(tmp_path):
    cfg = config(tmp_path, mode="bac")
    ouvert = [{"cible": "tcp 1.1.1.1:443", "classe": "ouverte", "cause": "connexion établie"}]
    with pytest.raises(X.ErreurBac, match="non éprouvé fermé"):
        X.Bac(cfg, LanceurIsoleFactice(), relever=lambda: ouvert, id_demarrage=lambda: "d1")
    assert not cfg.tampon_reseau.exists()
    appels = []
    ferme = [{"cible": "boucle locale (sain)", "classe": "ouverte", "cause": ""},
             {"cible": "tcp 1.1.1.1:443", "classe": "fermée", "cause": "refus local (EPERM)"}]
    X.Bac(cfg, LanceurIsoleFactice(), relever=lambda: appels.append(1) or ferme, id_demarrage=lambda: "d1")
    assert json.loads(cfg.tampon_reseau.read_text())["id_demarrage"] == "d1" and appels == [1]
    X.Bac(cfg, LanceurIsoleFactice(), relever=lambda: appels.append(2) or ferme, id_demarrage=lambda: "d1")
    assert appels == [1]                  # tampon du même démarrage : sonde non relancée
    with pytest.raises(X.ErreurBac):      # autre démarrage : sonde relancée, et elle voit le réseau ouvert
        X.Bac(cfg, LanceurIsoleFactice(), relever=lambda: ouvert, id_demarrage=lambda: "d2")


def test_mode_bac_refuse_un_lanceur_sans_isolement(tmp_path):
    cfg = config(tmp_path, mode="bac")
    with pytest.raises(X.ErreurBac):
        X.Bac(cfg, X.LanceurEssaiLocal(config(tmp_path)), relever=lambda: [], id_demarrage=lambda: "d1")
