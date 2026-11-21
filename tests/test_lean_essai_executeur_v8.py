"""Essais de l'exécuteur du bac v8 (essai Lean D-1a ; contre-lecture Fable 5.2 des corrections du troisième essai, 59b0ec03…),
hors machine. Copie de `test_lean_essai_executeur_v7.py` (inchangé, R12), portée sur la v8, plus :
- B2 : `relever_memoire_pic` rend « aucun relevé » sur « No such device » (lecture concurrente du retrait du cgroupe), sur un
  contenu vide ou non entier et sur un refus de droits ; un lancement dont les relevés lèvent ainsi se termine ;
- marge du « délai » (R1) : « délai » dès `cpu_max_s - 0,05 s` (4,95 s : délai ; 4,949 s : rien ; 5,011 s : délai ; une
  sortie en 137 après 31 ms : rien) ;
- B1, côté exécuteur : `incident_compilation` et `incident_noyau` portés à part ;
- tranche de la configuration (commande et chemin du cgroupe), nom sans tiret exigé ;
- la v8 ne diffère de la v7 que par les changements déclarés.
"""
import errno
import io
import json
import sys
from pathlib import Path

import pytest

from controle_ia.lean_essai import executeur_bac_v8 as X

RACINE = Path(__file__).resolve().parents[1]
LE = RACINE / "src" / "controle_ia" / "lean_essai"

# Résumés systemd du troisième essai (pièce epreuve-isolement-v6.json, branche donnees/lean-outillage-d1a-poste-local-v4).
RESUME_CPU_TUE = ("Running as unit: bac-x-python.service; invocation ID: 0\nFinished with result: exit-code\n"
                  "Main processes terminated with: code=exited/status=137\nService runtime: 5.020s\n"
                  "CPU time consumed: 5.011s\nMemory peak: 336.0K\nMemory swap peak: 0B\n")
RESUME_137_VITE = ("Finished with result: exit-code\nMain processes terminated with: code=exited/status=137\n"
                   "Service runtime: 40ms\nCPU time consumed: 31ms\nMemory peak: 336.0K\n")


# ---- pas 4 : classement du temps de processeur -------------------------------------------------------------------------------

def test_cpu_brule_sort_delai_cas_sain():
    res = dict(X.lire_resume_systemd(RESUME_CPU_TUE), isolement=True, code=137)
    assert res["cpu_s"] == pytest.approx(5.011)
    assert X.classer_execution(res, 5) == "délai"


def test_sortie_137_vite_ne_sort_pas_delai_artefact():
    res = dict(X.lire_resume_systemd(RESUME_137_VITE), isolement=True, code=137)
    assert res["resultat"] == "exit-code" and res["fin"] == "code=exited/status=137"
    assert X.classer_execution(res, 5) is None


def test_la_v6_ne_voyait_pas_le_cas_sain():
    """Le défaut du troisième essai, reproduit : la v6 rend « aucun incident » sur le résumé de l'item qui brûle le processeur."""
    from controle_ia.lean_essai import executeur_bac_v6 as V6
    assert V6.classer_execution(dict(V6.lire_resume_systemd(RESUME_CPU_TUE), isolement=True)) is None


@pytest.mark.parametrize("resultat,fin,cpu,attendu", [
    ("success", "code=exited/status=0", 9999.0, None),          # réussite : jamais d'incident, même au-delà de la limite
    ("timeout", "code=killed/status=TERM", 0.01, "délai"),
    ("oom-kill", "code=killed/status=TERM", 0.3, "mémoire"),
    ("signal", "code=killed/status=XCPU", 0.2, None),           # « XCPU » ne suffit plus : la fin se forge
    ("signal", "code=killed/status=KILL", 5.0, "délai"),
    ("core-dump", "code=dumped/status=SEGV", 4.94, None),
    ("exit-code", "code=exited/status=1", 5.0, "délai"),         # limite atteinte exactement
    ("exit-code", "code=exited/status=1", 4.95, "délai"),        # v8 : limite moins la tolérance (0,05 s)
    ("exit-code", "code=exited/status=1", 4.949, None),
    ("exit-code", "code=exited/status=137", 5.011, "délai"),     # le cas du troisième essai
])
def test_classement_table(resultat, fin, cpu, attendu):
    assert X.classer_execution({"isolement": True, "resultat": resultat, "fin": fin, "cpu_s": cpu}, 5) == attendu


def test_classement_sans_temps_de_processeur_arrete():
    with pytest.raises(X.ErreurBac, match="sans temps de processeur"):
        X.classer_execution({"isolement": True, "resultat": "exit-code", "cpu_s": None}, 5)
    assert X.classer_execution({"isolement": True, "resultat": "success", "cpu_s": None}, 5) is None
    for res, motif in (({"isolement": True, "resultat": None, "code": 1}, "sans résultat"),
                       ({"isolement": True, "resultat": "resources"}, "inattendu")):
        with pytest.raises(X.ErreurBac, match=motif):
            X.classer_execution(res, 5)
    assert X.classer_execution({"isolement": False, "resultat": None}, 5) is None


def test_classement_suit_la_limite_de_la_configuration():
    res = {"isolement": True, "resultat": "exit-code", "cpu_s": 30.0}
    assert X.classer_execution(res, 1800) is None and X.classer_execution(res, 30) == "délai"


# ---- pas 5 : pic de mémoire -------------------------------------------------------------------------------------------------

def test_memory_peak_de_systemd_n_est_plus_lu():
    assert "memoire_pic" not in X.lire_resume_systemd(RESUME_CPU_TUE)
    assert "Memory peak:" not in X.lire_resume_systemd.__code__.co_consts


class FauxProcessus:
    """Processus `systemd-run --wait` factice : vivant pendant `tours` relevés ; fait monter `memory.peak` à chaque tour."""

    def __init__(self, chemin: Path, valeurs, code=0, stderr=b"Finished with result: success\nCPU time consumed: 1s\n"):
        self.chemin, self.valeurs, self.returncode, self._stderr = chemin, list(valeurs), None, stderr
        self.code = code

    def poll(self):
        if self.valeurs:
            v = self.valeurs.pop(0)
            if v is None:
                if self.chemin.exists():
                    self.chemin.unlink()
            else:
                self.chemin.parent.mkdir(parents=True, exist_ok=True)
                self.chemin.write_text(f"{v}\n")
            return None
        self.returncode = self.code
        return self.code

    def communicate(self):
        return b"", self._stderr


def config(tmp_path, **k):
    d = dict(lean="/l", lean_path="/p", verificateur=str(tmp_path / "v.lean"), verificateur_sha256="x", mode="bac",
             racine_items=tmp_path / "items", racine_sorties=tmp_path / "sorties", racine_cgroup=tmp_path / "cg")
    d.update(k)
    return X.Config(**d)


def lanceur_factice(tmp_path, valeurs, **k):
    cfg = config(tmp_path)
    vus = {}

    def popen(argv, **kw):
        vus["argv"] = argv
        unite = next(a.split("=", 1)[1] for a in argv if a.startswith("--unit="))
        vus["p"] = FauxProcessus(cfg.racine_cgroup / "system.slice" / f"{unite}.service" / "memory.peak", valeurs, **k)
        return vus["p"]
    executer = lambda argv, **kw: type("P", (), {"stdout": "", "returncode": 0})()   # systemctl show : aucun groupe
    return X.LanceurBac(cfg, verifier_hote=False, executer=executer, lancer_processus=popen, dormir=lambda s: None), vus


def lancement(tmp_path):
    return X.Lancement(["lean"], {}, "/tmp", {}, tmp_path / "s.out", tmp_path / "s.err")


def test_pic_echantillonne_cas_sain(tmp_path):
    lanceur, vus = lanceur_factice(tmp_path, [None, 344064, 700000000, 1200000000, None])
    r = lanceur.lancer(lancement(tmp_path), "bac-a-compilation")
    assert r["memoire_pic_echantillonne_octets"] == 1200000000 and r["memoire_echantillons"] == 3
    assert "--slice=system.slice" in vus["argv"]
    assert r["resultat"] == "success" and r["cpu_s"] == 1.0 and "memoire_pic" not in r


def test_pic_sans_aucun_releve_est_absent(tmp_path):
    lanceur, _ = lanceur_factice(tmp_path, [None, None])
    r = lanceur.lancer(lancement(tmp_path), "bac-b-compilation")
    assert r["memoire_pic_echantillonne_octets"] is None and r["memoire_echantillons"] == 0


def test_pic_lu_dans_le_cgroupe_de_l_unite_seulement(tmp_path):
    autre = tmp_path / "cg" / "system.slice" / "bac-autre.service" / "memory.peak"
    autre.parent.mkdir(parents=True)
    autre.write_text("999999999\n")
    lanceur, _ = lanceur_factice(tmp_path, [5000])
    r = lanceur.lancer(lancement(tmp_path), "bac-c-compilation")
    assert r["memoire_pic_echantillonne_octets"] == 5000


def test_public_porte_le_pic_echantillonne():
    p = X._public({"code": 0, "memoire_pic_echantillonne_octets": 7, "memoire_echantillons": 2, "memoire_pic": "336.0K"})
    assert p["memoire_pic_echantillonne_octets"] == 7 and "memoire_pic" not in p


# ---- sortie d'erreur de la compilation, en mode essai-local ----------------------------------------------------------------

FAUX_LEAN = r'''
import json, os, sys
args = sys.argv[1:]
if "-o" in args:
    sys.stderr.write("ERREUR-STANDARD-DE-LEAN\n")
    print(json.dumps({"severity": "error", "pos": {"line": 1, "column": 0}, "data": "type mismatch"}))
    sys.exit(1)
print(json.dumps({"type": "fin", "nonce": args[-1]}))
'''


def test_erreurs_de_compilation_dans_le_resultat(tmp_path):
    faux = tmp_path / "faux_lean.py"
    faux.write_text(FAUX_LEAN, encoding="utf-8")
    noyau = tmp_path / "noyau"
    noyau.mkdir()
    verif = noyau / "verificateur_noyau_v6.lean"
    verif.write_text("-- factice\n")
    for n in ("items", "sorties"):
        (tmp_path / n).mkdir()
    cfg = X.Config(lean=str(faux), lean_path=str(tmp_path / "m"), verificateur=str(verif),
                   verificateur_sha256=X._sha256(verif), mode="essai-local", racine_items=tmp_path / "items",
                   racine_sorties=tmp_path / "sorties", duree_max_s=60)

    class Lanceur(X.LanceurEssaiLocal):
        def lancer(self, l, unite):
            l = X.Lancement([sys.executable, "-I", "-B"] + l.argv, l.liaisons, l.chdir, l.env, l.sortie, l.erreurs)
            return super().lancer(l, unite)
    r = X.Bac(cfg, Lanceur(cfg)).verifier_lean(X.nouvel_item(), "theorem etape_1 : True := trivial\n", 1)
    assert "ERREUR-STANDARD-DE-LEAN" in r["erreurs_compilation"] and "type mismatch" in r["sortie_compilation"]
    assert r["compilation"]["memoire_pic_echantillonne_octets"] is None and r["incident_bac"] is None


# ---- la v7 ne diffère de la v6 que par les changements déclarés ---------------------------------------------------------------

def test_pic_est_le_plus_haut_releve_pas_le_dernier(tmp_path):
    lanceur, _ = lanceur_factice(tmp_path, [344064, 1200000000, 700000000])
    assert lanceur.lancer(lancement(tmp_path), "bac-d-compilation")["memoire_pic_echantillonne_octets"] == 1200000000


class LanceurIsoleFactice:
    """Lanceur « isolé » factice : rend, pour chaque unité, un résultat systemd sans réussite avec 10 s de processeur."""
    isolement = True

    def __init__(self):
        self.unites = []

    def temoin_montage(self, l, unite):
        return None

    def lancer(self, l, unite):
        self.unites.append(unite)
        return {"code": 1, "duree_murale_s": 10.0, "cpu_s": 10.0, "memoire_pic_echantillonne_octets": None,
                "memoire_echantillons": 0, "duree_service_s": 10.0, "resultat": "exit-code", "fin": "code=exited/status=1",
                "resume_systemd": "", "isolement": True, "residus": []}


@pytest.mark.parametrize("cpu_max_s,attendu", [(1800, None), (5, "délai")])
def test_bac_classe_avec_la_limite_de_sa_configuration(tmp_path, monkeypatch, cpu_max_s, attendu):
    monkeypatch.setattr(X.shutil, "chown", lambda *a, **k: None)
    verif = tmp_path / "v.lean"
    verif.write_text("-- factice\n")
    for n in ("items", "sorties"):
        (tmp_path / n).mkdir()
    cfg = config(tmp_path, verificateur=str(verif), verificateur_sha256=X._sha256(verif), cpu_max_s=cpu_max_s,
                 tampon_reseau=tmp_path / "run" / "r.json")
    ferme = lambda: [{"cible": "tcp 1.1.1.1:443", "classe": "fermée", "cause": "EPERM"}]
    bac = X.Bac(cfg, LanceurIsoleFactice(), relever=ferme, id_demarrage=lambda: "d")
    r = bac.verifier_lean(X.nouvel_item(), "theorem etape_1 : True := trivial\n", 1)
    assert r["incident_bac"] == attendu
    assert bac.executer_python(X.nouvel_item(), "print(1)\n")["incident_bac"] == attendu


# ---- v8, B2 : relevé de memory.peak sans arrêt de l'exécuteur ------------------------------------------------------------------

def test_relever_memoire_pic_cas_sain(tmp_path):
    chemin = tmp_path / "memory.peak"
    chemin.write_text("4096\n")
    assert X.relever_memoire_pic(chemin) == 4096


@pytest.mark.parametrize("cas", ["no-such-device", "vide", "non-entier", "droits", "absent", "dossier"])
def test_relever_memoire_pic_aucun_releve(tmp_path, monkeypatch, cas):
    """Objets de contrôle de la contre-lecture (« No such device », contenu vide), et voisins : « aucun relevé », jamais une
    exception."""
    chemin = tmp_path / "memory.peak"
    if cas == "vide":
        chemin.write_text("")
    elif cas == "non-entier":
        chemin.write_text("max\n")
    elif cas == "dossier":
        chemin.mkdir()
    elif cas in ("no-such-device", "droits"):
        chemin.write_text("123\n")
        erreur = OSError(errno.ENODEV, "No such device") if cas == "no-such-device" else \
            PermissionError(errno.EACCES, "Permission denied")

        def lever(self, *a, **k):
            raise erreur
        monkeypatch.setattr(X.Path, "read_text", lever)
    assert X.relever_memoire_pic(chemin) is None


class ProcessusRetrait:
    """`systemd-run --wait` factice dont les relevés tombent sur un cgroupe en cours de retrait : à chaque tour, le fichier
    `memory.peak` porte une valeur, est vide, ou sa lecture lève « No such device »."""

    def __init__(self, chemin, tours, etat):
        self.chemin, self.tours, self.etat, self.returncode = chemin, list(tours), etat, None

    def poll(self):
        if not self.tours:
            self.returncode = 0
            return 0
        v = self.tours.pop(0)
        self.chemin.parent.mkdir(parents=True, exist_ok=True)
        self.etat["enodev"] = v == "ENODEV"
        self.chemin.write_text("" if v in ("VIDE", "ENODEV") else f"{v}\n")
        return None

    def communicate(self):
        return b"", b"Finished with result: success\nCPU time consumed: 2s\nService runtime: 2s\n"


def test_lancement_se_termine_quand_les_releves_levent(tmp_path, monkeypatch):
    etat = {"enodev": False}
    lire = X.Path.read_text

    def read_text(self, *a, **k):
        if self.name == "memory.peak" and etat["enodev"]:
            raise OSError(errno.ENODEV, "No such device")
        return lire(self, *a, **k)
    monkeypatch.setattr(X.Path, "read_text", read_text)
    cfg = config(tmp_path)
    vus = {}

    def popen(argv, **kw):
        unite = next(a.split("=", 1)[1] for a in argv if a.startswith("--unit="))
        vus["p"] = ProcessusRetrait(cfg.racine_cgroup / cfg.tranche / f"{unite}.service" / "memory.peak",
                                    [1000, "VIDE", 5000, "ENODEV", 3000, "ENODEV"], etat)
        return vus["p"]
    executer = lambda argv, **kw: type("P", (), {"stdout": "", "returncode": 0})()
    lanceur = X.LanceurBac(cfg, verifier_hote=False, executer=executer, lancer_processus=popen, dormir=lambda s: None)
    r = lanceur.lancer(lancement(tmp_path), "bac-e-compilation")
    assert r["resultat"] == "success" and r["memoire_pic_echantillonne_octets"] == 5000 and r["memoire_echantillons"] == 3


# ---- v8, R1 : marge du « délai » --------------------------------------------------------------------------------------------

def test_tolerance_ecrite():
    assert X.TOLERANCE_CPU_S == 0.05
    base = {"isolement": True, "resultat": "exit-code"}
    assert X.classer_execution(dict(base, cpu_s=5 - X.TOLERANCE_CPU_S), 5) == "délai"
    assert X.classer_execution(dict(base, cpu_s=5 - X.TOLERANCE_CPU_S - 0.001), 5) is None
    assert X.classer_execution(dict(X.lire_resume_systemd(RESUME_137_VITE), isolement=True), 5) is None


# ---- v8, B1 côté exécuteur : incidents de la compilation et du vérificateur à part ----------------------------------------------

class LanceurParUnite:
    isolement = True

    def __init__(self, compilation, noyau):
        self.resultats = {"compilation": compilation, "noyau": noyau}

    def temoin_montage(self, l, unite):
        return None

    def lancer(self, l, unite):
        resultat, cpu = self.resultats[unite.rsplit("-", 1)[1]]
        return {"code": 0 if resultat == "success" else 1, "duree_murale_s": 1.0, "cpu_s": cpu,
                "memoire_pic_echantillonne_octets": None, "memoire_echantillons": 0, "duree_service_s": 1.0,
                "resultat": resultat, "fin": "", "resume_systemd": "", "isolement": True, "residus": []}


@pytest.mark.parametrize("compilation,noyau,ic,iv,ib", [
    (("exit-code", 0.4), ("oom-kill", 0.5), None, "mémoire", "mémoire"),    # l'objet de contrôle de B1
    (("oom-kill", 0.3), ("oom-kill", 0.5), "mémoire", "mémoire", "mémoire"),
    (("oom-kill", 0.3), ("success", 1.0), "mémoire", None, "mémoire"),
    (("success", 1.0), ("success", 1.0), None, None, None),
])
def test_incidents_de_compilation_et_du_noyau_a_part(tmp_path, monkeypatch, compilation, noyau, ic, iv, ib):
    monkeypatch.setattr(X.shutil, "chown", lambda *a, **k: None)
    verif = tmp_path / "v.lean"
    verif.write_text("-- factice\n")
    for n in ("items", "sorties"):
        (tmp_path / n).mkdir()
    cfg = config(tmp_path, verificateur=str(verif), verificateur_sha256=X._sha256(verif), cpu_max_s=5,
                 tampon_reseau=tmp_path / "run" / "r.json")
    ferme = lambda: [{"cible": "tcp 1.1.1.1:443", "classe": "fermée", "cause": "EPERM"}]
    bac = X.Bac(cfg, LanceurParUnite(compilation, noyau), relever=ferme, id_demarrage=lambda: "d")
    r = bac.verifier_lean(X.nouvel_item(), "theorem etape_1 : True := trivial\n", 1)
    assert (r["incident_compilation"], r["incident_noyau"], r["incident_bac"]) == (ic, iv, ib)


# ---- v8 : tranche de la configuration ----------------------------------------------------------------------------------------

def test_tranche_dans_la_commande_et_le_chemin(tmp_path):
    cfg = config(tmp_path, tranche="bacmesure0a1b2c3d.slice")
    lanceur = X.LanceurBac(cfg, verifier_hote=False)
    c = lanceur.commande(lancement(tmp_path), "bac-f-noyau")
    assert "--slice=bacmesure0a1b2c3d.slice" in c and "--slice=system.slice" not in c
    assert lanceur.chemin_memoire_pic("bac-f-noyau") == \
        tmp_path / "cg" / "bacmesure0a1b2c3d.slice" / "bac-f-noyau.service" / "memory.peak"
    assert X.Config(lean="/l", lean_path="/p").tranche == "system.slice"
    assert "--slice=system.slice" in X.LanceurBac(config(tmp_path), verifier_hote=False).commande(lancement(tmp_path), "u")


@pytest.mark.parametrize("tranche", ["system-bac.slice", "../x.slice", "bac.service", "", "bac mesure.slice"])
def test_tranche_refusee(tmp_path, tranche):
    with pytest.raises(X.ErreurBac, match="tranche"):
        X.LanceurBac(config(tmp_path, tranche=tranche), verifier_hote=False)


# ---- la v8 ne diffère de la v7 que par les changements déclarés -----------------------------------------------------------------

RETIREES_V7 = [
    'VERSION = "executeur_bac_v7"',
    'TRANCHE = "system.slice"',
    '        return "délai" if cpu >= cpu_max_s else None',
    '    """`memory.peak` du cgroupe de l\'unité, en octets ; None si le fichier n\'existe pas (encore ou plus)."""',
    '    except (FileNotFoundError, ProcessLookupError):',
    '        sd = ["systemd-run", "--wait", "--collect", "--service-type=exec", f"--unit={unite}", f"--slice={TRANCHE}",',
    '        return self.cfg.racine_cgroup / TRANCHE / f"{unite}.service" / "memory.peak"',
    '                   "incident_bac": incident_c or incident_v, "inventaire_item": inventaire,',
    '    ap = argparse.ArgumentParser(description="Exécuteur du bac de l\'essai Lean (D-1a), v7")',
]


def test_v8_rien_d_autre():
    import difflib
    v7 = (LE / "executeur_bac_v7.py").read_text(encoding="utf-8")
    v8 = (LE / "executeur_bac_v8.py").read_text(encoding="utf-8")
    corps7, corps8 = v7[v7.index('"""\nfrom __future__'):], v8[v8.index('"""\nfrom __future__'):]
    retirees = [l[1:] for l in difflib.unified_diff(corps7.splitlines(), corps8.splitlines(), lineterm="", n=0)
                if l.startswith("-") and not l.startswith("---")]
    assert retirees == RETIREES_V7
