"""Épreuve (R5) du code de la condition 6 du témoin de Bailey, v4 : `lanceur_v4` et `instance_v4` (les autres modules
sont ceux de la v3, éprouvés par `test_temoin_bailey_condition6_v3.py`). Applique la relecture en différentiel du code
v3 (`relecture-differentiel-code-condition6-v3-bailey-v1.md`, `a2107244…`) : chaque défaut D-1 à D-8 a au moins un
essai dont le scénario est celui de la sonde du relecteur (`test_sondes_r2_v3.py`, `28b9acb2…`), inversé : il passe sur
la v4 et échoue sur la v3 ; chaque garde neuve a un cas sain et un artefact. Sur processeur, sans modèle, sans réseau,
sans instance (le seul `git` employé travaille sur des dépôts fabriqués ou lit `origin/main` déjà présent).
"""
from __future__ import annotations

import ast
import io
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tarfile
import time
from contextlib import redirect_stdout
from pathlib import Path

import pytest

from controle_ia import scellement
from controle_ia.gardes import GardeArret
from controle_ia.temoin_bailey import conventions_v3 as cv
from controle_ia.temoin_bailey import instance_v4 as inst
from controle_ia.temoin_bailey import lanceur_v4 as la
from controle_ia.temoin_bailey import lecture_v3 as lc

import test_temoin_bailey_condition6_v3 as T3  # ligne de GO réelle, déroulé factice (aides de la v3, inchangées)

DEPOT = Path(__file__).resolve().parents[1]
GO_ID = T3.GO_ID
GO_REEL = T3.GO_REEL
TEXTE_GO_MAIN = "# Registre des GO\n\n" + GO_REEL + "\n"
HORLOGE = la.echeance_epoch("2026-11-20")


# --- dépôt fabriqué : fichiers de `CHEMINS_ARCHIVE`, plus des fichiers qui ne doivent jamais partir ; `origin/main`
#     porte la ligne de GO, la branche de travail non (P-i) -----------------------------------------------------------

def depot_git(tmp_path) -> tuple[Path, str]:
    d = tmp_path / "depot"
    d.mkdir(parents=True)
    g = ["git", "-C", str(d), "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid"]
    subprocess.run(["git", "init", "-q", str(d)], check=True)
    for rel in la.CHEMINS_ARCHIVE + ("src/controle_ia/bras_attaque/x.py", "donnees/brut.jsonl", "diag/r.json",
                                     "docs/notes/bras-attaque/n.md"):
        (d / rel).parent.mkdir(parents=True, exist_ok=True)
        (d / rel).write_text(f"# {rel}\n")
    (d / "registres").mkdir()
    (d / "registres/go.md").write_text(TEXTE_GO_MAIN)
    subprocess.run(g + ["add", "-A"], check=True)
    subprocess.run(g + ["commit", "-q", "-m", "main"], check=True)
    subprocess.run(["git", "-C", str(d), "update-ref", "refs/remotes/origin/main", "HEAD"], check=True)
    (d / "registres/go.md").write_text("# Registre des GO\n")  # branche de travail : la ligne n'y est pas
    subprocess.run(g + ["commit", "-q", "-am", "travail"], check=True)
    sha = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], check=True, capture_output=True,
                         text=True).stdout.strip()
    return d, sha


# --- fournisseur factice : commandes détachées, `LANCE`, `VIVANT`, `MORT`, `tours` -------------------------------------

class FournisseurFactice(la.Fournisseur):
    """La réponse d'une commande nommée est rendue au premier sondage ; une commande dont la réponse est `"mort"`
    disparaît sans `.fin` (sondage → `MORT`) ; `tours` répond par `self.tours[phase]`."""

    def __init__(self, reponses, rapatrier_leve=None):
        self.detruites, self.commandes, self.lance, self.envoyes, self.appels = [], [], [], {}, []
        self.reponses, self.fins, self.distant, self.rapatrier_leve = reponses, {}, {}, rapatrier_leve
        self.tours: dict[str, dict | None] = {}
        self.etat_instance = "running"

    def creer(self, offre, image, disque_go):
        self.appels.append("creer")
        return "77"

    def taux_horaire(self, ident):
        self.appels.append("taux_horaire")
        return 1.0

    def statut(self, ident):
        self.appels.append("statut")
        return self.etat_instance

    def detruire(self, ident):
        self.appels.append("detruire")
        self.detruites.append(ident)

    def executer(self, ident, commande, delai_s=None):
        self.commandes.append(commande)
        m = re.search(r"echo \$! > /root/etats/([\w-]+)\.pid", commande)
        if m:
            nom = m.group(1)
            self.appels.append(f"lance:{nom}")
            self.lance.append(nom)
            rep = self.reponses[nom]
            if rep == "mort":
                self.fins[nom] = "MORT"
            else:
                etat, code = rep(self) if callable(rep) else rep
                self.fins[nom] = ("ETAT " + json.dumps(etat) + "\n" if etat is not None else "") + f"CODE {code}\n"
            return 0, "LANCE 4321\n"
        m = re.search(r"cat /root/etats/([\w-]+)\.fin", commande)
        if m:
            fin = self.fins.get(m.group(1))
            return 0, ("VIVANT\n" if fin is None else ("MORT\n" if fin == "MORT" else fin))
        m = re.search(r"instance_v4 tours --travail /root/x/([\w-]+)", commande)
        if m:
            t = self.tours.get(m.group(1))
            return (0, "ETAT " + json.dumps(t) + "\n") if t is not None else (1, "")
        if "instance_v4 empreintes" in commande:
            self.appels.append("empreintes")
            return 0, "ETAT " + json.dumps({"commande": "empreintes", "fichiers": []})
        if commande.startswith("kill -TERM"):
            self.appels.append("kill")
        if commande == "true":
            self.appels.append("ssh-true")
        return 0, ""

    def rapatrier_fichier(self, ident, distant, local):
        if self.rapatrier_leve:
            raise self.rapatrier_leve(distant)
        if distant not in self.distant:
            raise FileNotFoundError(distant)
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(self.distant[distant])

    def envoyer_fichier(self, ident, local, distant):
        self.appels.append("envoyer")
        self.envoyes[distant] = Path(local).read_bytes()


def etat_x(phase, **kw):
    pilote = phase.startswith("pilote")
    k = 3 if pilote else 72
    base = dict(commande="executer", phase=phase, k=k, code_retour=0, cause_arret=None, gardes_tombees=[],
                tours_marques=k, tours_complets=k, durees={"0": 100.0, "1": 110.0, "2": 120.0},
                configuration_effective="passée")
    base.update(kw)
    return base, 0


def reponses(**kw):
    r = {"amorce": ({"commande": "amorce", "finie": True}, 0),
         "mise-en-place": ({"commande": "mise-en-place", "gardes": {}, "pas_par_tour": 1600, "longueur_suffixe": 16,
                            "ecart_10": False}, 0),
         "controle-juge": ({"commande": "controle-juge", "etats": {"tenus": True}, "garde_juge": "passée"}, 0),
         "pilote": etat_x("pilote"), "pilote-reprise": etat_x("pilote-reprise"),
         "regle": ({"commande": "regle-tours", "B": 75, "R": 10, "D": 1.0, "c": 1.0, "t": 105.0, "H_heures": 64.0,
                    "K": 72, "arret": False}, 0),
         "principal": etat_x("principal"), "principal-relance": etat_x("principal-relance", k=60)}
    r.update(kw)
    return r


def conduite(tmp_path, monkeypatch, reps, anterieures=(), horloge=None, rapatrier_leve=None, texte_go=TEXTE_GO_MAIN):
    tmp_path.mkdir(parents=True, exist_ok=True)
    depot, commit = depot_git(tmp_path)
    man = tmp_path / "manifeste-local-v4.json"
    la.manifeste_depuis_versions_figees(man, DEPOT / cv.VERSIONS_FIGEES, commit_code=commit, b=75, go_id=GO_ID)
    monkeypatch.setenv("GO_ID", GO_ID)
    monkeypatch.setenv("HF_TOKEN", "jeton-factice-essai")
    f = FournisseurFactice(reps, rapatrier_leve)
    veille = {"lances": [], "arretes": []}
    c = la.Conduite(f, man, tmp_path / "sortie", GO_ID, texte_go, "offre", "image", depot, list(anterieures),
                    horloge=horloge or (lambda: HORLOGE), attendre=lambda s: None, periode_sondage_s=0,
                    lancer_veilleur=lambda *a: veille["lances"].append(a) or 4242,
                    arreter_veilleur=lambda pid: veille["arretes"].append(pid),
                    veilleur_vivant=lambda pid, journal: True)
    return c, f, veille


def horloge_pas(pas_s: float, depart: float = HORLOGE):
    t = {"h": depart}

    def horloge():
        t["h"] += pas_s
        return t["h"]
    return horloge


# --- cas sain de bout en bout -------------------------------------------------------------------------------------------

def test_conduite_saine_bout_en_bout(tmp_path, monkeypatch):
    c, f, veille = conduite(tmp_path, monkeypatch, reponses())
    bilan = c.conduire()
    assert f.lance == ["amorce", "mise-en-place", "controle-juge", "pilote", "regle", "principal"]
    assert "arret" not in bilan and "erreur" not in bilan and f.detruites == ["77"] and bilan["detruite"] is True
    assert veille["arretes"] == [4242] and "/root/amorce-v4.sh" in f.envoyes
    assert not any("jeton-factice-essai" in x for x in f.commandes)
    assert all("instance_v3" not in x for x in f.commandes)  # le module distant est `instance_v4`
    for nom in ("initial", "mise-en-place", "regle"):
        scellement.verifier(c.sortie / lc.MANIFESTES[nom])
    scellement.verifier(c.sortie / "bilan-conduite-v4.json")
    assert not any(x.startswith("kill -TERM") for x in f.commandes)  # rien à arrêter sur une fin normale


def test_conduite_sonde_orientee_et_relance_inchangees(tmp_path, monkeypatch):
    reps = reponses(pilote=etat_x("pilote", code_retour=1, tours_marques=0, tours_complets=0,
                                  gardes_tombees=["sonde orientée"], durees={}))
    c, f, _ = conduite(tmp_path / "a", monkeypatch, reps)
    assert c.conduire()["arret"].startswith("non interprétable") and "pilote-reprise" not in f.lance
    reps = reponses(principal=etat_x("principal", code_retour=1, tours_marques=5, tours_complets=5))
    c, f, _ = conduite(tmp_path / "b", monkeypatch, reps)
    c.conduire()
    assert f.lance[-2:] == ["principal", "principal-relance"]
    assert json.loads((c.sortie / lc.MANIFESTES["relance"]).read_text())["regle_tours"]["relance"] is True


# --- D-1 / C1 : fenêtre création → `try` fermée ------------------------------------------------------------------------

def test_D1_taux_horaire_qui_leve_instance_detruite(tmp_path, monkeypatch):
    c, f, veille = conduite(tmp_path, monkeypatch, reponses())
    essais = []

    def taux(ident):
        essais.append(ident)
        raise subprocess.CalledProcessError(1, "vastai show")
    f.taux_horaire = taux
    with pytest.raises(subprocess.CalledProcessError):
        c.conduire()
    assert f.detruites == ["77"] and len(essais) == 3 and veille["lances"] == []  # v3 : detruites == []
    bilan = json.loads((c.sortie / "bilan-conduite-v4.json").read_text())
    assert bilan["detruite"] is True and "taux illisible" in bilan["taux_illisible"]


def test_D1_bis_veilleur_qui_ne_part_pas_instance_detruite(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses())
    c.lancer_veilleur = lambda *a: (_ for _ in ()).throw(OSError("fork"))
    with pytest.raises(OSError):
        c.conduire()
    assert f.detruites == ["77"] and f.lance == []  # v3 : detruites == []


def test_C1_taux_lu_au_second_essai(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses())
    n = {"i": 0}

    def taux(ident):
        n["i"] += 1
        if n["i"] == 1:
            raise subprocess.CalledProcessError(1, "vastai show")
        return 1.0
    f.taux_horaire = taux
    assert "arret" not in c.conduire() and c.c == 1.0 and f.detruites == ["77"]


# --- D-2 / C2 : veilleur robuste, vu vivant ------------------------------------------------------------------------------

def _poste(tmp_path, instances, b=75):
    p = tmp_path / "poste.json"
    la.Poste(b=b, instances=instances).ecrire(p)
    return p


def test_D2_veilleur_retente_une_destruction_en_echec(tmp_path):
    p = _poste(tmp_path, [{"id": "9", "c": 1.0, "creation": 0, "destruction": None}])
    essais = []

    class F(la.Fournisseur):
        def detruire(self, ident):
            essais.append(ident)
            if len(essais) == 1:
                raise subprocess.CalledProcessError(1, "vastai destroy")

    v = la.Veilleur(F(), p, "9", echeance=1e12, journal=tmp_path / "a.jsonl", horloge=lambda: 80 * 3600,
                    attendre=lambda s: None)
    assert v.boucle(passages=5) == "dépense (seuil de secours)"  # v3 : l'exception sortait au premier essai
    assert essais == ["9", "9"] and la.Poste.lire(p).instances[0]["destruction"] is not None
    lignes = [json.loads(x) for x in (tmp_path / "a.jsonl").read_text().splitlines()]
    assert "CalledProcessError" in lignes[0]["erreur"] and lignes[-1]["arret"] == "dépense (seuil de secours)"
    assert json.loads((tmp_path / "a.jsonl.battement").read_text())["pid"] == os.getpid()


def test_C2_veilleur_sain_sous_le_seuil_ne_detruit_pas(tmp_path):
    p = _poste(tmp_path, [{"id": "9", "c": 1.0, "creation": 0, "destruction": None}])

    class F(la.Fournisseur):
        def detruire(self, ident):
            raise AssertionError("aucune destruction attendue")

    v = la.Veilleur(F(), p, "9", echeance=1e12, journal=tmp_path / "a.jsonl", horloge=lambda: 10 * 3600,
                    attendre=lambda s: None)
    assert v.boucle(passages=3) is None and not (tmp_path / "a.jsonl").exists()


def test_C2_poste_illisible_dernier_poste_ou_destruction(tmp_path):
    p = _poste(tmp_path, [{"id": "9", "c": 1.0, "creation": 0, "destruction": None}])
    detruites = []

    class F(la.Fournisseur):
        def detruire(self, ident):
            detruites.append(ident)

    v = la.Veilleur(F(), p, "9", echeance=1e12, journal=tmp_path / "a.jsonl", horloge=lambda: 10 * 3600,
                    attendre=lambda s: None)
    assert v.boucle(passages=1) is None
    p.write_text("{illisible")
    assert v.boucle(passages=2) is None and detruites == []  # dernier poste lu : sous le seuil
    assert "poste illisible" in (tmp_path / "a.jsonl").read_text()
    v2 = la.Veilleur(F(), tmp_path / "absent.json", "9", echeance=1e12, journal=tmp_path / "b.jsonl",
                     horloge=lambda: 0.0, attendre=lambda s: None)
    assert v2.boucle(passages=1) == "poste illisible (secours)" and detruites == ["9"]


def _attendre_fichier(p: Path, s=30.0):
    fin = time.time() + s
    while time.time() < fin and not p.exists():
        time.sleep(0.1)


def test_D2_bis_veilleur_processus_poste_absent_detruit_et_mort_vue(tmp_path):
    """Sonde D2-bis inversée : poste illisible au départ → le processus détruit (v3 : il mourait sans rien faire) ; un
    veilleur mort au départ est vu mort par `verifier_veilleur` (v3 : jamais vérifié)."""
    detruites = tmp_path / "d.txt"
    pid = la.lancer_veilleur_processus(tmp_path / "absent.json", "9", 1e12, tmp_path / "a.jsonl",
                                       f"fichier:{detruites}", 0.05)
    _attendre_fichier(detruites)
    assert detruites.read_text().split() == ["9"]
    lignes = [json.loads(x) for x in (tmp_path / "a.jsonl").read_text().splitlines()]
    assert {"poste illisible (secours)"} == {x["arret"] for x in lignes if "arret" in x}
    mort = la.lancer_veilleur_processus(tmp_path / "absent.json", "9", 1e12, tmp_path / "m.jsonl", "inconnu:x", 0.05)
    assert la.verifier_veilleur(mort, tmp_path / "m.jsonl", delai_s=10) is False
    assert "fournisseur inconnu" in (tmp_path / "m.jsonl.err").read_text()


def test_C2_veilleur_processus_vivant_vu_vivant(tmp_path):
    p = _poste(tmp_path, [{"id": "9", "c": 1.0, "creation": time.time(), "destruction": None}])
    pid = la.lancer_veilleur_processus(p, "9", 1e12, tmp_path / "a.jsonl", f"fichier:{tmp_path / 'd.txt'}", 0.05)
    try:
        assert la.verifier_veilleur(pid, tmp_path / "a.jsonl", delai_s=20) is True
    finally:
        la.arreter_veilleur(pid)
    fin = time.time() + 10
    while time.time() < fin and la.processus_vivant(pid):
        time.sleep(0.1)
    assert la.processus_vivant(pid) is False and not (tmp_path / "d.txt").exists()


def test_C2_conduite_veilleur_mort_arret_avant_toute_commande(tmp_path, monkeypatch):
    c, f, veille = conduite(tmp_path, monkeypatch, reponses())
    c.veilleur_vivant = lambda pid, journal: False
    bilan = c.conduire()
    assert bilan["arret"].startswith("veilleur de secours non vivant") and f.lance == [] and f.detruites == ["77"]
    assert len(veille["lances"]) == 2 and veille["arretes"][0] == 4242  # une relance, puis arrêt


def test_C2_veilleur_mort_en_cours_de_run_relance(tmp_path, monkeypatch):
    c, f, veille = conduite(tmp_path, monkeypatch, reponses())
    n = {"i": 0}

    def vivant(pid, journal):
        n["i"] += 1
        return n["i"] != 6  # un seul constat de mort, puis le relancé vit
    c.veilleur_vivant = vivant
    bilan = c.conduire()
    assert "arret" not in bilan and len(veille["lances"]) == 2


def test_D7_marge_et_periode_transmises_au_veilleur(tmp_path, monkeypatch):
    c, f, veille = conduite(tmp_path, monkeypatch, reponses())
    c.marge_secours, c.periode_veilleur_s = 0.8, 12.0
    c.conduire()
    a = veille["lances"][0]
    assert len(a) == 7 and a[5] == 12.0 and a[6] == 0.8  # v3 : 5 arguments, ni marge ni période
    c2, f2, _ = conduite(tmp_path / "b", monkeypatch, reponses())
    c2.marge_secours = 1.5  # le veilleur détruirait sans transfert avant le seuil local B − 1
    with pytest.raises(GardeArret, match="seuil local"):
        c2.conduire()
    assert f2.detruites == [] and "creer" not in f2.appels


def test_C1_destruction_en_echec_veilleur_mort_veilleur_de_destruction(tmp_path, monkeypatch):
    c, f, veille = conduite(tmp_path, monkeypatch, reponses())
    essais = []
    f.detruire = lambda ident: essais.append(ident) or (_ for _ in ()).throw(RuntimeError("API indisponible"))
    c.veilleur_vivant = lambda pid, journal: len(essais) == 0  # vivant pendant le run, mort à la fin
    bilan = c.conduire()
    assert bilan["detruite"] is False and len(essais) == la.ESSAIS_DESTRUCTION
    assert veille["lances"][-1][2] == 0.0 and bilan["veilleur_de_destruction"] == 4242  # échéance immédiate
    c2, f2, veille2 = conduite(tmp_path / "b", monkeypatch, reponses())
    f2.detruire = lambda ident: (_ for _ in ()).throw(RuntimeError("API indisponible"))
    bilan2 = c2.conduire()
    assert bilan2["detruite"] is False and len(veille2["lances"]) == 1 and veille2["arretes"] == []  # veilleur vivant


# --- D-3 / C3 : sondages en échec tolérés, arrêt par PID avant le rapatriement -----------------------------------------

def test_D3_un_sondage_qui_leve_n_arrete_pas_le_run(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses())
    vrai = f.executer
    n = {"sondages_principal": 0}

    def executer(ident, commande, delai_s=None):
        if "cat /root/etats/principal.fin" in commande:
            n["sondages_principal"] += 1
            if n["sondages_principal"] == 1:
                raise subprocess.TimeoutExpired("ssh", 120)  # v3 : sortie par exception, instance détruite
        return vrai(ident, commande, delai_s)
    f.executer = executer
    bilan = c.conduire()
    assert "arret" not in bilan and n["sondages_principal"] == 2
    assert not any(x.startswith("kill -TERM") for x in f.commandes) and f.detruites == ["77"]


def test_D3_instance_injoignable_arret_par_pid_avant_rapatriement(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses())
    vrai = f.executer

    def executer(ident, commande, delai_s=None):
        if "cat /root/etats/principal.fin" in commande:
            raise subprocess.TimeoutExpired("ssh", 120)
        return vrai(ident, commande, delai_s)
    f.executer = executer
    bilan = c.conduire()
    assert bilan["arret"].startswith("instance injoignable pendant « principal »") and f.detruites == ["77"]
    a = f.appels
    assert "kill" in a and a.index("kill") < a.index("empreintes") < a.index("detruire")
    assert any(x == la.commande_arret("principal") for x in f.commandes)


def test_C3_sortie_par_exception_arret_par_pid_avant_rapatriement(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses(principal=lambda s: etat_x("principal")))
    f.reponses["principal"] = "vivant-sans-fin"
    vrai = f.executer

    def executer(ident, commande, delai_s=None):
        if "echo $! > /root/etats/principal.pid" in commande:
            f.lance.append("principal")
            return 0, "LANCE 1\n"
        return vrai(ident, commande, delai_s)
    f.executer = executer
    c.veilleur_vivant = lambda pid, journal: (_ for _ in ()).throw(RuntimeError("panne locale")) \
        if c.en_cours == "principal" and f.commandes[-1].startswith("if [ -e /root/etats/principal.fin") else True
    with pytest.raises(RuntimeError):
        c.conduire()
    a = f.appels
    assert a.index("kill") < a.index("empreintes") < a.index("detruire")


def test_C3_fournisseur_vast_ne_leve_pas_sur_une_coupure(tmp_path, monkeypatch):
    v = la.FournisseurVast()
    monkeypatch.setattr(v, "_ssh", lambda ident: ("root@h", "22"))

    def run(a, **k):
        raise subprocess.TimeoutExpired(a, 120)
    monkeypatch.setattr(la.subprocess, "run", run)
    assert v.executer("1", "true", 5) == (255, "")
    monkeypatch.setattr(v, "_ssh", lambda ident: (_ for _ in ()).throw(subprocess.CalledProcessError(1, "ssh-url")))
    assert v.executer("1", "true", 5) == (255, "")
    monkeypatch.setattr(v, "_ssh", lambda ident: ("root@h", "22"))
    monkeypatch.setattr(la.subprocess, "run", lambda a, **k: subprocess.CompletedProcess(a, 0, "ok\n", ""))
    assert v.executer("1", "true", 5) == (0, "ok\n")  # cas sain


# --- D-4 / C4 : exécution morte, seuil local, lancement vérifié ---------------------------------------------------------

def test_D4_execution_morte_detectee_et_relance(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses(principal="mort"), horloge=horloge_pas(60.0))
    f.tours["principal"] = {"commande": "tours", "tours_complets": 5, "journal_absent": None, "gardes_tombees": []}
    bilan = c.conduire()
    p = bilan["principal"][0]
    assert p["gardes_tombees"] == [la.MORT_SANS_ETAT] and p["tours_complets"] == 5 and p["code_retour"] == 1
    assert f.lance[-2:] == ["principal", "principal-relance"]  # v3 : sondé jusqu'à l'échéance, D > B
    assert bilan["depense"] < 70


def test_C4_execution_morte_apres_20_tours_ou_sonde_orientee_pas_de_relance(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path / "a", monkeypatch, reponses(principal="mort"))
    f.tours["principal"] = {"tours_complets": 25, "journal_absent": None, "gardes_tombees": []}
    c.conduire()
    assert "principal-relance" not in f.lance
    c, f, _ = conduite(tmp_path / "b", monkeypatch, reponses(principal="mort"))
    f.tours["principal"] = {"tours_complets": 3, "journal_absent": None, "gardes_tombees": ["sonde orientée"]}
    c.conduire()
    assert "principal-relance" not in f.lance
    c, f, _ = conduite(tmp_path / "c", monkeypatch, reponses(principal="mort"))  # `tours` illisible
    bilan = c.conduire()
    assert "principal-relance" not in f.lance and "tours complets illisibles" in bilan["arret"]
    c, f, _ = conduite(tmp_path / "d", monkeypatch, reponses(pilote="mort"))  # pilote mort : chute, une reprise
    assert "arret" not in c.conduire() and f.lance[3:5] == ["pilote", "pilote-reprise"]


def test_D4_seuil_local_B_moins_1_pendant_une_execution(tmp_path, monkeypatch):
    """Exécution vivante qui ne finit jamais (l'arrêt de l'instance à B − 2 n'est pas venu) : la conduite l'arrête à
    D ≥ B − 1, sous le seuil du veilleur (B − 0,5) ; v3 : seulement à l'échéance moins la moitié de la marge."""
    c, f, _ = conduite(tmp_path, monkeypatch, reponses(principal="vivant-sans-fin"), horloge=horloge_pas(360.0))
    vrai = f.executer

    def executer(ident, commande, delai_s=None):
        if "echo $! > /root/etats/principal.pid" in commande:
            f.lance.append("principal")
            return 0, "LANCE 1\n"
        return vrai(ident, commande, delai_s)
    f.executer = executer
    bilan = c.conduire()
    assert bilan["arret"].startswith("seuil local de dépense (D ≥ B − 1 USD)")
    assert 74 <= bilan["depense"] < 75 - la.MARGE_SECOURS_USD and f.detruites == ["77"]
    assert la.commande_arret("principal") in f.commandes


def test_D4_bis_lancement_non_verifie_arret(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses(), horloge=horloge_pas(3600.0))
    vrai = f.executer
    essais = []

    def executer(ident, commande, delai_s=None):
        if "echo $! > /root/etats/mise-en-place.pid" in commande:
            essais.append(commande)
            return 255, ""  # ssh refusé au lancement
        return vrai(ident, commande, delai_s)
    f.executer = executer
    bilan = c.conduire()
    assert bilan["arret"].startswith("lancement de « mise-en-place » non vérifié") and len(essais) == 2
    assert bilan["depense"] < 20 and f.detruites == ["77"]  # v3 : D ≈ 74 avant l'arrêt


def test_C4_lancement_verifie_au_second_essai(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses())
    vrai = f.executer
    essais = []

    def executer(ident, commande, delai_s=None):
        if "echo $! > /root/etats/mise-en-place.pid" in commande and not essais:
            essais.append(commande)
            return 0, ""  # aucun `LANCE` : PID non écrit
        return vrai(ident, commande, delai_s)
    f.executer = executer
    assert "arret" not in c.conduire() and essais and "principal" in f.lance


def _bash_local(commande: str, d: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["bash", "-c", commande.replace(la.ETATS_DISTANTS, str(d))], capture_output=True,
                          text=True, timeout=30)


def test_C4_commandes_distantes_en_bash_reel(tmp_path):
    """Les commandes de lancement, de sondage et d'arrêt, jouées par bash sur ce poste (chemin des états remplacé)."""
    d = tmp_path / "etats"
    compteur = tmp_path / "compteur"
    r = _bash_local(la.commande_detachee("long", f"echo x >> {compteur}; sleep 60"), d)
    assert la.lancement_verifie(r.stdout)
    pid = int(r.stdout.split()[-1])
    assert la.lire_sondage(*(lambda p: (p.returncode, p.stdout))(_bash_local(la.commande_sondage("long"), d))) == \
        "vivant"
    r2 = _bash_local(la.commande_detachee("long", f"echo x >> {compteur}; sleep 60"), d)  # second essai : idempotent
    assert la.lancement_verifie(r2.stdout) and int(r2.stdout.split()[-1]) == pid
    time.sleep(0.5)
    assert compteur.read_text() == "x\n"
    os.killpg(pid, signal.SIGKILL)  # coupure : le groupe meurt sans écrire `.fin`
    time.sleep(0.5)
    s = _bash_local(la.commande_sondage("long"), d)
    assert la.lire_sondage(s.returncode, s.stdout) == "mort"
    r = _bash_local(la.commande_detachee("court", "echo 'ETAT {\"a\": 1}'; exit 3"), d)
    assert la.lancement_verifie(r.stdout)
    fin = time.time() + 20
    while time.time() < fin:
        s = _bash_local(la.commande_sondage("court"), d)
        if la.lire_sondage(s.returncode, s.stdout) == "fin":
            break
        time.sleep(0.1)
    assert la.lire_etat(s.stdout) == {"a": 1} and la.lire_code(s.stdout) == 3
    r3 = _bash_local(la.commande_detachee("court", "echo relance >> " + str(compteur)), d)  # déjà finie : rien
    time.sleep(0.3)
    assert la.lancement_verifie(r3.stdout) and compteur.read_text() == "x\n"
    assert la.lire_sondage(255, "") == "échec" and la.lire_sondage(0, "") == "échec"


# --- D-5 / C5 : instance prête avant la première opération ; clé d'hôte ------------------------------------------------

def test_D5_attente_instance_prete_puis_envoi(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses())
    c.conduire()
    a = f.appels
    assert a[:4] == ["creer", "taux_horaire", "statut", "ssh-true"] and a[4] == "envoyer"  # v3 : envoi aussitôt


def test_C5_instance_jamais_prete_arret_borne(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses(), horloge=horloge_pas(60.0))
    f.etat_instance = "loading"
    bilan = c.conduire()
    assert bilan["arret"].startswith("instance non prête") and "envoyer" not in f.appels and f.detruites == ["77"]
    assert f.appels.count("statut") >= 10


def test_D5_scp_et_ssh_acceptent_la_cle_d_hote(tmp_path, monkeypatch):
    argv = []
    monkeypatch.setattr(la.subprocess, "run", lambda a, **k: argv.append(a) or subprocess.CompletedProcess(a, 0, "", ""))
    v = la.FournisseurVast()
    monkeypatch.setattr(v, "_ssh", lambda ident: ("root@h", "22"))
    v.envoyer_fichier("1", tmp_path / "x", "/root/x")
    v.rapatrier_fichier("1", "/root/x", tmp_path / "y")
    v.executer("1", "true")
    for a in argv:
        assert "StrictHostKeyChecking=accept-new" in a and "BatchMode=yes" in a
    assert [a[0] for a in argv] == ["scp", "scp", "ssh"]


# --- D-6 / C6 : archive limitée aux fichiers de `src/` nécessaires ------------------------------------------------------

def test_D6_archive_limitee_a_src_necessaire(tmp_path):
    d, sha = depot_git(tmp_path)
    archive, h = la.fabriquer_archive(d, sha, tmp_path / "arch")
    with tarfile.open(archive) as t:
        noms = sorted(m.name for m in t.getmembers() if m.isfile())
    assert noms == sorted(la.CHEMINS_ARCHIVE) and h == cv.sha_fichier(archive)  # v3 : le dépôt entier
    with pytest.raises(GardeArret, match="hors de src"):
        la.fabriquer_archive(d, sha, tmp_path / "a2", ("docs/notes",))
    with pytest.raises(GardeArret, match="archive"):  # fichier exigé absent du commit
        la.fabriquer_archive(d, sha, tmp_path / "a3", la.CHEMINS_ARCHIVE + ("src/controle_ia/absent.py",))


def _imports_relatifs(fichier: Path, paquet: str) -> set[str]:
    """Modules `controle_ia…` importés par un fichier, imports paresseux compris (dans les fonctions)."""
    out = set()
    for n in ast.walk(ast.parse(fichier.read_text(encoding="utf-8"))):
        if isinstance(n, ast.ImportFrom):
            if n.level:
                base = paquet.split(".")[: len(paquet.split(".")) - (n.level - 1)]
                cible = ".".join(base + ([n.module] if n.module else []))
                if n.module:
                    out.add(cible)
                else:
                    out.update(f"{cible}.{a.name}" for a in n.names)
            elif n.module and n.module.startswith("controle_ia"):
                out.add(n.module)
        elif isinstance(n, ast.Import):
            out.update(a.name for a in n.names if a.name.startswith("controle_ia"))
    return out


def test_C6_fermeture_des_imports_de_l_instance():
    """Tout module `controle_ia` importé (même paresseusement) par un fichier de l'archive est dans l'archive."""
    racine = DEPOT / "src"
    presents = {str(Path(p).relative_to("src").with_suffix("")).replace("/", ".").removesuffix(".__init__")
                for p in la.CHEMINS_ARCHIVE}
    for p in la.CHEMINS_ARCHIVE:
        mod = str(Path(p).relative_to("src").with_suffix("")).replace("/", ".")
        paquet = mod.removesuffix(".__init__") if p.endswith("__init__.py") else mod.rsplit(".", 1)[0]
        for cible in _imports_relatifs(racine / Path(p).relative_to("src"), paquet):
            assert cible in presents, (p, cible)
    assert "controle_ia.temoin_bailey.execution_v3" in presents  # lancé par `-m` sur l'instance


def test_C6_l_archive_s_importe_seule(tmp_path):
    """Les fichiers de l'archive, copiés seuls (arbre de travail), suffisent à importer les modules de l'instance."""
    for p in la.CHEMINS_ARCHIVE:
        (tmp_path / p).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(DEPOT / p, tmp_path / p)
    code = ("import sys, controle_ia\n"
            "import controle_ia.temoin_bailey.instance_v4, controle_ia.temoin_bailey.execution_v3\n"
            "import controle_ia.temoin_bailey.journaliseur_v3, controle_ia.temoin_bailey.lecture_v3\n"
            "fs = [m.__file__ for n, m in sys.modules.items() if n.startswith('controle_ia')]\n"
            f"assert all(f.startswith({str(tmp_path)!r}) for f in fs), fs\n"
            "print(len(fs))\n")
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH",)}
    env["PYTHONPATH"] = str(tmp_path / "src")
    r = subprocess.run([sys.executable, "-c", code], cwd=tmp_path, env=env, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-2000:]
    assert int(r.stdout.strip()) >= 8
    r = subprocess.run([sys.executable, "-m", la.INSTANCE_MODULE, "--help"], cwd=tmp_path, env=env,
                       capture_output=True, text=True)
    assert r.returncode == 0 and "tours" in r.stdout


# --- D-8 / C7 : K < 20 au même `ETAT` -----------------------------------------------------------------------------------

def _regle(tmp_path, duree):
    pil = tmp_path / "pilote"
    pil.mkdir(parents=True)
    (pil / cv.ETAT_EXECUTION).write_text(json.dumps({"durees": {"0": duree, "1": duree}}))
    man = tmp_path / "m.json"
    man.write_text("{}")
    out = io.StringIO()
    with redirect_stdout(out):
        code = inst.main(["regle-tours", "--travail", str(tmp_path / "r"), "--manifeste", str(man), "--pilote",
                          str(pil), "--depense", json.dumps({"d_avant": 0, "c": 1.0, "creation": time.time(), "b": 75})])
    return code, out.getvalue(), tmp_path / "r"


def test_D8_regle_k_inferieur_a_20_une_seule_ligne_d_etat(tmp_path):
    code, sortie, r = _regle(tmp_path / "a", 100000.0)
    assert code == 3 and sum(l.startswith("ETAT ") for l in sortie.splitlines()) == 1  # v3 : deux lignes
    e = la.lire_etat(sortie)
    assert e["K"] < 20 and "nombre de tours" in e["garde_tombee"]
    assert json.loads((r / cv.ETAT_REGLE).read_text())["K"] == e["K"]
    code, sortie, _ = _regle(tmp_path / "b", 100.0)  # cas sain
    e = la.lire_etat(sortie)
    assert code == 0 and e["K"] >= 20 and "garde_tombee" not in e


def test_D8_conduite_K_inferieur_a_20_devis_revise(tmp_path, monkeypatch):
    regle = ({"commande": "regle-tours", "B": 75, "R": 10, "D": 1.0, "c": 1.0, "t": 100000.0, "H_heures": 64.0,
              "K": 2, "garde_tombee": "garde « nombre de tours » tombée : K < 20 par la règle"}, 3)
    c, f, _ = conduite(tmp_path / "a", monkeypatch, reponses(regle=regle))
    assert c.conduire()["arret"] == "K < 20 après le pilote : arrêt, devis révisé à Lazar" and "principal" not in f.lance
    regle = ({"commande": "regle-tours", "garde_tombee": "garde « pilote » tombée : tours 0 et 1 du pilote non finis"}, 3)
    c, f, _ = conduite(tmp_path / "b", monkeypatch, reponses(regle=regle))
    assert c.conduire()["arret"].startswith("règle du nombre de tours non calculée")


def test_C4_sous_commande_tours_sans_note(tmp_path):
    x, _ = T3.execution_factice(tmp_path, "principal", 5)
    out = io.StringIO()
    with redirect_stdout(out):
        assert inst.main(["tours", "--travail", str(x)]) == 0
    e = la.lire_etat(out.getvalue())
    assert e["tours_complets"] == lc.tours_complets_instance(x)[0] and e["journal_absent"] is None
    vide = tmp_path / "vide"
    vide.mkdir()
    out = io.StringIO()
    with redirect_stdout(out):
        inst.main(["tours", "--travail", str(vide)])
    e = la.lire_etat(out.getvalue())
    assert e["tours_complets"] == 0 and e["journal_absent"] and any("absent" in g for g in e["gardes_tombees"])


# --- P-i : GO lu sur origin/main ----------------------------------------------------------------------------------------

def test_P_i_texte_go_de_origin_main(tmp_path, monkeypatch):
    d, _ = depot_git(tmp_path / "d")
    assert la.texte_go_main(d) == TEXTE_GO_MAIN
    with pytest.raises(GardeArret, match="origin/main"):
        la.texte_go_main(tmp_path / "pas-un-depot")
    c, f, _ = conduite(tmp_path / "c", monkeypatch, reponses(), texte_go=(d / "registres/go.md").read_text())
    with pytest.raises(GardeArret, match="origin/main"):  # texte de la branche de travail : refusé avant la création
        c.conduire()
    assert "creer" not in f.appels


def test_P_i_ligne_reelle_sur_origin_main_du_depot():
    try:
        texte = la.texte_go_main(DEPOT)
    except GardeArret:
        pytest.skip("origin/main absent de ce clone")
    go = la.ligne_go(texte, GO_ID)
    la.verifier_go(go, 75)
    la.verifier_non_revoque(texte, GO_ID)
    assert la.echeance_epoch(go["echeance"]) == la.echeance_epoch("2026-11-30T22:59") + 59  # fin du jour à Paris


def test_lecture_7_echeance_fin_du_jour_a_paris():
    assert la.echeance_epoch("2026-11-30") == la.echeance_epoch("2026-11-30T22:59") + 59  # heure d'hiver
    assert la.echeance_epoch("2026-07-01") == la.echeance_epoch("2026-07-01T21:59") + 59  # heure d'été
    assert la.echeance_epoch("2026-11-30", fuseau="UTC") == la.echeance_epoch("2026-11-30T23:59") + 59
    with pytest.raises(GardeArret, match="fuseau"):
        la.echeance_epoch("2026-11-30", fuseau="Nulle/Part")
    with pytest.raises(GardeArret, match="illisible"):
        la.echeance_epoch("30 novembre")


# --- conditions inchangées, rejouées sur la v4 --------------------------------------------------------------------------

def test_echeance_trop_proche_detruite_et_b_moins_2_avant_creation(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path / "a", monkeypatch, reponses(), horloge=lambda: la.echeance_epoch("2026-11-28"))
    with pytest.raises(GardeArret, match="échéance"):
        c.conduire()
    assert f.detruites == ["77"] and f.lance == []
    anterieure = {"id": "70", "c": 18.5, "creation": HORLOGE - 10 * 3600, "destruction": HORLOGE - 6 * 3600, "B": 75}
    c, f, _ = conduite(tmp_path / "b", monkeypatch, reponses(), anterieures=[anterieure])
    with pytest.raises(GardeArret, match="B − 2 avant la création"):
        c.conduire()
    assert "creer" not in f.appels
