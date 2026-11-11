"""Essais R5 de l'exécuteur v4 (repris de la v3 ; plus inventaire par lstat, témoin « success » k05, premier pas
CLC3-04) — v3 : (garde de fond lancée par le harnais, inventaire de l'item, témoin de montage CLC2-05,
tampon du réseau périmé, cloisons du bac CLC2-08 n20 et n21) hors machine, avec un faux `lean` qui joue aussi le vérificateur."""
import json
import signal
import sys
from pathlib import Path

import pytest

from controle_ia.lean_essai import executeur_bac_v4 as X

FAUX_LEAN = r'''
import json, os, re, sys
args = sys.argv[1:]
if "-o" in args:
    src = open(args[-1], encoding="utf-8").read()
    if "ERREUR_FACTICE" in src:
        print(json.dumps({"severity": "error", "pos": {"line": 1, "column": 0}, "data": "type mismatch"})); sys.exit(1)
    if "ECRIRE_FICHIER" in src:
        open(os.path.join(os.path.dirname(args[-1]), "Lean.olean"), "w").write("piège")
    sortie = args[args.index("-o") + 1]
    d = {"theoremes": re.findall(r"theorem (\w+)", src), "defs": re.findall(r"def (\w+)", src),
         "drapeaux": [f for f in ("HORS_NOYAU", "PLANTER") if f in src], "sorry": "sorry" in src}
    open(sortie, "w").write(json.dumps(d))
    sys.exit(0)
i = args.index("--run")
verificateur, olean, m, nonce = args[i + 1:i + 5]
assert os.path.isfile(verificateur), verificateur
if os.path.dirname(olean) in os.environ.get("LEAN_PATH", "").split(":"):
    print("dossier de l'item dans LEAN_PATH"); sys.exit(9)
d = json.load(open(olean))
def e(o): print(json.dumps(o, ensure_ascii=False))
e({"type": "imports", "modules": ["Init", "Mathlib"], "permis": True})
for t in d["theoremes"]:
    e({"type": "constante", "nom": t, "genre": "theoreme", "sure": None, "surete": "sure"})
for x in d["defs"]:
    e({"type": "constante", "nom": x, "genre": "definition", "surete": "sure"})
if "HORS_NOYAU" in d["drapeaux"]:
    e({"type": "rejeu", "ok": False, "erreur": "(kernel) declaration type mismatch"})
else:
    e({"type": "rejeu", "ok": True})
    for n in ["etape_%d" % k for k in range(1, int(m) + 1)] + ["enonce_item"]:
        if n in d["theoremes"]:
            ax = ["propext"] + (["sorryAx"] if d["sorry"] else [])
            e({"type": "attendu", "nom": n, "present": True, "genre": "theoreme", "axiomes": ax, "enonce": n + " : True",
               "enonce_explicite": "True", "aller_retour": True, "raison": "", "tronque": False, "metavariables": False,
               "messages_elaboration": 0, "constantes_agent": []})
        else:
            e({"type": "attendu", "nom": n, "present": False})
    for x in d["defs"]:
        e({"type": "definition", "nom": x, "genre": "definition", "enonce": "ℕ", "valeur": "1"})
e({"type": "fin", "nonce": nonce})
sys.exit(137 if "PLANTER" in d["drapeaux"] else 0)
'''

SAIN = "theorem etape_1 : True := trivial\ntheorem etape_2 : True := trivial\ntheorem enonce_item : True := trivial\n"


def config(tmp_path, **k):
    faux = tmp_path / "faux_lean.py"
    faux.write_text(FAUX_LEAN, encoding="utf-8")
    noyau = tmp_path / "noyau"
    noyau.mkdir(exist_ok=True)
    verificateur = noyau / "verificateur_noyau_v4.lean"
    verificateur.write_text("-- vérificateur factice\n", encoding="utf-8")
    for nom in ("items", "sorties"):
        (tmp_path / nom).mkdir(exist_ok=True)
    d = dict(lean=str(faux), lean_path=str(tmp_path / "mathlib"), python=sys.executable,
             verificateur=str(verificateur), verificateur_sha256=X._sha256(verificateur),
             racine_items=tmp_path / "items", racine_sorties=tmp_path / "sorties", mode="essai-local", duree_max_s=60,
             tampon_reseau=tmp_path / "run" / "reseau-ferme-v1.json")
    d.update(k)
    return X.Config(**d)


class Enregistreur(X.LanceurEssaiLocal):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.lancements = []

    def lancer(self, l, unite):
        self.lancements.append((unite, l))
        if l.argv and l.argv[0] == self.cfg.lean:
            l = X.Lancement([sys.executable, "-I", "-B"] + l.argv, l.liaisons, l.chdir, l.env, l.sortie, l.erreurs)
        return super().lancer(l, unite)


@pytest.fixture
def bac(tmp_path):
    cfg = config(tmp_path)
    lanceur = Enregistreur(cfg)
    return X.Bac(cfg, lanceur), lanceur, tmp_path


def vide(tmp_path):
    return all(not list((tmp_path / n).iterdir()) for n in ("items", "sorties"))


def test_sain_et_lancement_du_verificateur(bac):
    b, lanceur, tmp = bac
    r = b.verifier_lean("item-sain-0001", SAIN, 2)
    assert r["verdict"]["accepte_gardes"], {g: x["motifs"] for g, x in r["verdict"]["gardes"].items() if x["motifs"]}
    assert r["verdict"]["rejeu_ok"] and vide(tmp)
    assert r["inventaire_item"] == ["Item.lean", "Item.olean"]   # le faux lean n'écrit pas Item.ilean
    (_, compil), (_, noyau) = lanceur.lancements
    assert noyau.argv[1:3] == ["--run", X.LOGIQUE_VERIFICATEUR] and noyau.argv[3] == "/item/Item.olean"
    assert noyau.liaisons["/item"][1] is False and noyau.liaisons["/noyau"] == (str(tmp / "noyau"), False)
    assert "/item" not in noyau.env["LEAN_PATH"].split(":")


def test_rejeu_en_echec(bac):
    b, _, _ = bac
    r = b.verifier_lean("item-hors-0001", SAIN + "-- HORS_NOYAU\n", 2)
    assert not r["verdict"]["gardes"]["G-L8"]["ok"] and not r["verdict"]["accepte_gardes"]


def test_inventaire_de_l_item(bac):
    b, _, _ = bac
    r = b.verifier_lean("item-fich-0001", SAIN + "-- ECRIRE_FICHIER\n", 2)
    assert any("Lean.olean" in x for x in r["verdict"]["gardes"]["G-L7"]["motifs"])


def test_verificateur_plante(bac):
    b, _, _ = bac
    r = b.verifier_lean("item-plan-0001", SAIN + "-- PLANTER\n", 2)
    assert not r["verdict"]["gardes"]["G-L7"]["ok"]


def test_verificateur_non_epingle_ou_change(tmp_path):
    cfg = config(tmp_path)
    Path(cfg.verificateur).write_text("-- modifié\n", encoding="utf-8")
    with pytest.raises(X.ErreurBac, match="empreinte"):
        X.Bac(cfg, Enregistreur(cfg)).verifier_lean("item-sha-00001", SAIN, 2)
    assert vide(tmp_path)
    cfg = config(tmp_path, verificateur_sha256="")
    with pytest.raises(X.ErreurBac):
        X.Bac(cfg, Enregistreur(cfg)).verifier_lean("item-sha-00002", SAIN, 2)
    p = tmp_path / "chaine-v1.json"
    p.write_text(json.dumps({"lean": "/l", "lean_path": "/p"}))
    with pytest.raises(X.ErreurBac, match="verificateur_noyau_sha256"):
        X.charger_config(p)


def test_python_sain(bac):
    b, _, tmp = bac
    r = b.executer_python("py-sain-0001", "import sys\nsys.stderr.write('bwrap: bonjour\\n')\nprint('SAIN')\n")
    assert r["execution"]["code"] == 0 and "SAIN" in r["stdout"] and vide(tmp)   # l'agent qui écrit « bwrap: » n'arrête rien


# ---- CLC2-05 : témoin de montage -------------------------------------------------------------------------------------------

class P:
    def __init__(self, returncode=0, stdout=b"", stderr=b""):
        self.returncode, self.stdout, self.stderr = returncode, stdout, stderr


def test_temoin_de_montage(tmp_path):
    cfg = config(tmp_path, mode="bac", racine_cgroup=tmp_path)
    vus = []

    def executer(argv, **k):
        vus.append(argv)
        if argv[0] == "systemctl":
            return P(stdout="")
        if argv[-1] == "/usr/bin/true":
            Path(next(a.split("file:", 1)[1] for a in argv if a.startswith("StandardError=file:"))).write_text(
                "bwrap: Creating new namespace failed\n")
            return P(1, stderr=b"Finished with result: exit-code\n")
        return P(0, stderr=b"Finished with result: success\n")
    lanceur = X.LanceurBac(cfg, verifier_hote=False, executer=executer)
    l = X.Lancement(["lean"], {"/item": (str(tmp_path / "items"), False)}, "/tmp", {}, tmp_path / "k.out",
                    tmp_path / "k.err")
    with pytest.raises(X.ErreurBac, match="témoin de montage.*bwrap: Creating"):
        lanceur.temoin_montage(l, "bac-a-noyau")
    assert vus[0][-1] == "/usr/bin/true" and "--ro-bind" in vus[0]

    def executer_sain(argv, **k):
        return P(stdout="") if argv[0] == "systemctl" else P(0, stderr=b"Finished with result: success\n")
    X.LanceurBac(cfg, verifier_hote=False, executer=executer_sain).temoin_montage(l, "bac-a-noyau")


def test_classer_execution_v3():
    assert X.classer_execution({"isolement": True, "resultat": "success"}) is None
    assert X.classer_execution({"isolement": True, "resultat": "timeout"}) == "délai"
    assert X.classer_execution({"isolement": True, "resultat": "oom-kill"}) == "mémoire"
    assert X.classer_execution({"isolement": True, "resultat": "signal", "fin": "code=killed/status=XCPU"}) == "délai"
    for res, motif in (({"isolement": True, "resultat": None, "code": 1}, "sans résultat"),
                       ({"isolement": True, "resultat": "resources"}, "inattendu")):
        with pytest.raises(X.ErreurBac, match=motif):
            X.classer_execution(res)


# ---- CLC2-08 n20, n21 : cloisons du bac dans la commande ------------------------------------------------------------------

def test_commande_du_bac_v3(tmp_path):
    cfg = config(tmp_path, mode="bac")
    l = X.Lancement(["lean", "--run", X.LOGIQUE_VERIFICATEUR], {"/item": ("/srv/items/a", False)}, "/tmp",
                    {"LEAN_PATH": "/opt/mathlib/x"}, Path("/srv/sorties/a/n.out"), Path("/srv/sorties/a/n.err"))
    c = X.LanceurBac(cfg, verifier_hote=False).commande(l, "bac-a-noyau")
    texte = " ".join(c)
    for attendu in ("IPAddressDeny=any", "--unshare-all", "--die-with-parent", "--clearenv", "User=bac",
                    "MemoryMax=6G", "LimitCPU=1800", "--ro-bind /srv/items/a /item", "--remount-ro /"):
        assert attendu in texte, attendu
    assert "--bind /srv/items/a" not in texte and "/srv/leurre" not in texte


# ---- réseau : tampon périmé (note 3) -------------------------------------------------------------------------------------

def test_tampon_reseau_perime(tmp_path):
    cfg = config(tmp_path, mode="bac", tampon_age_max_s=3600)
    ferme = [{"cible": "tcp 1.1.1.1:443", "classe": "fermée", "cause": "EPERM"}]
    appels = []
    X.exiger_reseau_ferme(cfg, lambda: appels.append(1) or ferme, id_demarrage=lambda: "d1", maintenant=lambda: 1000.0)
    X.exiger_reseau_ferme(cfg, lambda: appels.append(2) or ferme, id_demarrage=lambda: "d1", maintenant=lambda: 2000.0)
    assert appels == [1]
    X.exiger_reseau_ferme(cfg, lambda: appels.append(3) or ferme, id_demarrage=lambda: "d1", maintenant=lambda: 9000.0)
    assert appels == [1, 3]
    ouvert = [{"cible": "tcp 1.1.1.1:443", "classe": "ouverte", "cause": "connexion établie"}]
    with pytest.raises(X.ErreurBac):
        X.exiger_reseau_ferme(cfg, lambda: ouvert, id_demarrage=lambda: "d1", maintenant=lambda: 99999.0)


def test_residus_de_l_unite(tmp_path):
    groupe = tmp_path / "system.slice" / "u.service"
    groupe.mkdir(parents=True)
    (groupe / "cgroup.procs").write_text("4242\n")
    tues = []
    r = X.residus_unite("u", lambda a, **k: P(stdout="/system.slice/u.service\n"), tmp_path, lambda p, s: tues.append(p))
    assert r == [4242] and tues == [4242]


# ---- épreuve v3 : épinglage du vérificateur et jugement du premier pas -------------------------------------------------------

def test_epingler_verificateur_et_juger(tmp_path):
    from controle_ia.lean_essai import epreuve_isolement_v4 as E
    verificateur = tmp_path / "verificateur_noyau_v4.lean"
    verificateur.write_text("-- v3\n", encoding="utf-8")
    chaine = tmp_path / "chaine-v1.json"
    chaine.write_text(json.dumps({"lean": "/l", "lean_path": "/p", "version_lean": "Lean (version 4.x)"}))
    r = E.epingler_verificateur(chaine, verificateur)
    assert r["sha256"] == X._sha256(verificateur) and X.charger_config(chaine).verificateur_sha256 == r["sha256"]
    cas = {"accepte": False, "rejeu": False, "echecs": ["G-L8"]}
    gardes = {g: {"ok": g != "G-L8", "motifs": [] if g != "G-L8" else ["rejeu"]} for g in ("G-L1", "G-L8")}
    res = {"verdict": {"accepte_gardes": False, "rejeu_ok": False, "gardes": gardes, "enonces_imprimes": {},
                       "impressions": {}, "axiomes": {}}, "sortie_compilation": "CODE-AGENT-EXECUTE-SIMPROC"}
    assert E.juger_lean(cas, res) == []
    assert E.juger_lean(dict(cas, rejeu=True), res) == ["rejeu False, True attendu"]
    assert E.observer({"observer_sortie": ["CODE-AGENT-EXECUTE-SIMPROC"]}, res) == \
        {"sortie contient « CODE-AGENT-EXECUTE-SIMPROC »": True}
    with pytest.raises(X.ErreurBac):
        E.premier_pas_noyau(config(tmp_path), tmp_path)


def test_bac_appelle_le_temoin_avant_tout_lancement(tmp_path, monkeypatch):
    monkeypatch.setattr(X.shutil, "chown", lambda *a, **k: None)
    cfg = config(tmp_path, mode="bac")

    class Lanceur:
        isolement = True

        def temoin_montage(self, l, unite):
            raise X.ErreurBac("témoin de montage en échec : panne du bac")

        def lancer(self, l, unite):
            raise AssertionError("lancé sans témoin de montage")
    b = X.Bac(cfg, Lanceur(), relever=lambda: [], id_demarrage=lambda: "d1")
    with pytest.raises(X.ErreurBac, match="témoin"):
        b.verifier_lean("item-tem-00001", SAIN, 2)
    with pytest.raises(X.ErreurBac, match="témoin"):
        b.executer_python("py-tem-000001", "print(1)\n")
    assert vide(tmp_path)



# ---- v4 : inventaire par lstat (note 3, CLC3-05) ----------------------------------------------------------------------------

def test_inventaire_lstat(tmp_path, monkeypatch):
    d = tmp_path / "item"
    d.mkdir()
    (d / "Item.lean").write_text("x")
    (tmp_path / "ailleurs.olean").write_text("y")
    (d / "Item.olean").symlink_to(tmp_path / "ailleurs.olean")
    noms, olean = X.inventorier(d)
    assert not olean and "Item.olean (lien ou fichier non ordinaire)" in noms
    (d / "Item.olean").unlink()
    (d / "Item.olean").write_bytes(b"0" * 100)
    assert X.inventorier(d) == (["Item.lean", "Item.olean"], True)
    monkeypatch.setattr(X, "OLEAN_MAX", 10)
    noms, olean = X.inventorier(d)
    assert not olean and noms[1].startswith("Item.olean (plus de")
    import os
    os.link(d / "Item.lean", tmp_path / "second-lien")
    assert "Item.lean (lien ou fichier non ordinaire)" in X.inventorier(d)[0]


def test_temoin_exige_success(tmp_path):   # k05
    cfg = config(tmp_path, mode="bac", racine_cgroup=tmp_path)

    def executer(argv, **k):
        return P(stdout="") if argv[0] == "systemctl" else P(0, stderr=b"Finished with result: exit-code\n")
    l = X.Lancement(["lean"], {}, "/tmp", {}, tmp_path / "k.out", tmp_path / "k.err")
    with pytest.raises(X.ErreurBac, match="exit-code"):
        X.LanceurBac(cfg, verifier_hote=False, executer=executer).temoin_montage(l, "u")


# ---- v4 : premier pas discriminant (CLC3-04) ------------------------------------------------------------------------------

def _res(gardes_ko=(), rejeu_ok=True, rejeu_present=True, erreur="", accepte=None):
    gardes = {g: {"ok": g not in gardes_ko, "motifs": ["x"] if g in gardes_ko else []}
              for g in ("G-L1", "G-L2", "G-L3", "G-L3+", "G-L4", "G-L5", "G-L6", "G-L7", "G-L8")}
    return {"verdict": {"accepte_gardes": not gardes_ko if accepte is None else accepte, "gardes": gardes,
                        "rejeu_ok": rejeu_ok, "rejeu_present": rejeu_present, "rejeu_erreur": erreur,
                        "enonces_imprimes": {}, "impressions": {}, "axiomes": {}},
            "sortie_compilation": "", "isolement": True, "processus_residuels": [], "dossiers_restants": []}


CAS_HORS_NOYAU = {"nom": "hors noyau", "fichier": "a.lean", "etapes": 2, "accepte": False, "rejeu": False,
                  "constante_fautive": "faux_lemme", "echecs": ["G-L8"], "passent": ["G-L1", "G-L7"],
                  "sans_suppl": {"echecs": ["G-L8"]}}


def test_juger_noyau_discriminant():
    from controle_ia.lean_essai import epreuve_isolement_v4 as E
    bon = _res(("G-L8",), rejeu_ok=False, erreur="(kernel) declaration type mismatch 'faux_lemme'")
    assert E.juger_noyau(CAS_HORS_NOYAU, bon) == []
    # compilation en échec, vérificateur muet : le cas v3 se disait conforme
    assert E.juger_noyau(CAS_HORS_NOYAU, _res(("G-L1", "G-L7", "G-L8"), rejeu_ok=False, rejeu_present=False))
    assert any("aucune ligne de rejeu" in x for x in
               E.juger_noyau(CAS_HORS_NOYAU, _res(("G-L8",), rejeu_ok=False, rejeu_present=False)))
    assert any("ne nomme pas" in x for x in
               E.juger_noyau(CAS_HORS_NOYAU, _res(("G-L8",), rejeu_ok=False, erreur="autre chose")))
    sain = {"nom": "sain", "fichier": "s.lean", "etapes": 2, "accepte": True, "rejeu": True}
    assert any("G-L7 devait passer" in x for x in E.juger_noyau(sain, _res(("G-L7",), accepte=True)))


def test_premier_pas_deux_passages(tmp_path, monkeypatch):
    from controle_ia.lean_essai import epreuve_isolement_v4 as E
    art = tmp_path / "art"
    art.mkdir()
    (art / "a.lean").write_text("-- a\n")
    (art / "b.lean").write_text("-- b\n")
    (art / "attendus-v4.json").write_text(json.dumps({
        "noyau": [CAS_HORS_NOYAU],
        "observations_noyau": [{"nom": "obs", "fichier": "b.lean", "etapes": 2, "observer": ["G-L5"]}]}))
    vus = []

    class BacFactice:
        def __init__(self, cfg, *a, **k):
            self.cfg = cfg

        def verifier_lean(self, item, source, m):
            vus.append((source, self.cfg.supplementaires))
            return _res(("G-L8",), rejeu_ok=False, erreur="'faux_lemme'")
    monkeypatch.setattr(E.X, "Bac", BacFactice)
    r = E.premier_pas_noyau(config(tmp_path, mode="bac"), art)
    assert r["conforme"] and [s for _, s in vus] == [True, False, True] and len(r["observations"]) == 1
    assert [c["genre"] for c in r["cas"]] == ["noyau (avec G-L3+)", "noyau (sans G-L3+)"]
