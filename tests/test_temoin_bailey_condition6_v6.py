"""Épreuve (R5) du code de la condition 6 du témoin de Bailey, v6 : essais de la v5 rejoués sur `lanceur_v6`, `instance_v6`,
`lecture_v6`, plus les essais de M-1 et M-2 (relecture `22879993…`). Texte d origine de la v5 :
autres modules sont ceux de la v3, éprouvés par `test_temoin_bailey_condition6_v3.py`). Applique la relecture des
lignes touchées v3 → v4 (`relecture-lignes-touchees-code-condition6-v4-bailey-v1.md`, `ff6c76c7…`) : chaque défaut
N-1 à N-5 a au moins un essai dont le scénario est celui de la sonde du relecteur (`test_sondes_r2_v4.py`,
`28646e88…`), inversé : il passe sur la v5 et échoue sur la v4 ; C8 a trois essais de bout en bout (conduite factice
adossée à des dossiers locaux, sous-commandes `empreintes` et `tours` de `instance_v6` jouées pour de vrai, puis
`lecture_v6`) : run tronqué K′ ≥ 20 sans relance, relance complète, arrêt au seuil local ; plus le cas sain. Sur
processeur, sans modèle, sans réseau, sans instance.
Les noms `conduite`, `reponses`, `HORLOGE`, `_bash_local` sont ceux des essais v4, pour rejouer les sondes sur la v5.
"""
from __future__ import annotations

import io
import json
import os
import re
import shlex
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
from controle_ia.temoin_bailey import analyse_v3 as an
from controle_ia.temoin_bailey import conventions_v3 as cv
from controle_ia.temoin_bailey import instance_v6 as inst
from controle_ia.temoin_bailey import lanceur_v6 as la
from controle_ia.temoin_bailey import lecture_v6 as lc

import test_temoin_bailey_condition6_v3 as T3  # aides de la v3, inchangées
import test_temoin_bailey_condition6_v4 as T4  # aides de la v4 (données, analyse des imports), inchangées

DEPOT = T4.DEPOT
GO_ID = T4.GO_ID
TEXTE_GO_MAIN = T4.TEXTE_GO_MAIN
HORLOGE = T4.HORLOGE
etat_x, reponses, horloge_pas = T4.etat_x, T4.reponses, T4.horloge_pas


def depot_git(tmp_path) -> tuple[Path, str]:
    """Comme l'essai v4, avec les fichiers de `CHEMINS_ARCHIVE` de la v5."""
    d = tmp_path / "depot"
    d.mkdir(parents=True)
    g = ["git", "-C", str(d), "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid"]
    subprocess.run(["git", "init", "-q", str(d)], check=True)
    for rel in la.CHEMINS_ARCHIVE + ("src/controle_ia/bras_attaque/x.py", "donnees/brut.jsonl", "diag/r.json"):
        (d / rel).parent.mkdir(parents=True, exist_ok=True)
        (d / rel).write_text(f"# {rel}\n")
    (d / "registres").mkdir()
    (d / "registres/go.md").write_text(TEXTE_GO_MAIN)
    subprocess.run(g + ["add", "-A"], check=True)
    subprocess.run(g + ["commit", "-q", "-m", "main"], check=True)
    subprocess.run(["git", "-C", str(d), "update-ref", "refs/remotes/origin/main", "HEAD"], check=True)
    (d / "registres/go.md").write_text("# Registre des GO\n")
    subprocess.run(g + ["commit", "-q", "-am", "travail"], check=True)
    sha = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], check=True, capture_output=True,
                         text=True).stdout.strip()
    return d, sha


# --- fournisseur factice (unitaire) : réponses par commande, comme la v4, aux formes de commande de la v5 -------------

class FournisseurFactice(la.Fournisseur):
    def __init__(self, reponses_):
        self.detruites, self.commandes, self.lance, self.envoyes, self.appels = [], [], [], {}, []
        self.reponses, self.fins = reponses_, {}
        self.tours: dict[str, dict | None] = {}
        self.ecrits: list[tuple[str, str]] = []  # (phase, cause) de `tours --ecrire-etat`
        self.etiquettes: list[str | None] = []
        self.etat_instance = "running"

    def creer(self, offre, image, disque_go, etiquette=None):
        self.appels.append("creer")
        self.etiquettes.append(etiquette)
        return "77"

    def inventaire(self, etiquette):
        return []

    def taux_horaire(self, ident):
        return 1.0

    def statut(self, ident):
        return self.etat_instance

    def detruire(self, ident):
        self.appels.append("detruire")
        self.detruites.append(ident)

    def executer(self, ident, commande, delai_s=None):
        self.commandes.append(commande)
        m = re.search(r"echo \$p > /root/etats/([\w-]+)\.pid", commande)
        if m:
            nom = m.group(1)
            self.appels.append(f"lance:{nom}")
            self.lance.append(nom)
            rep = self.reponses[nom]
            if rep == "mort":
                self.fins[nom] = "MORT"
            elif rep != "vivant-sans-fin":
                etat, code = rep(self) if callable(rep) else rep
                self.fins[nom] = ("ETAT " + json.dumps(etat) + "\n" if etat is not None else "") + f"CODE {code}\n"
            return 0, "LANCE 4321\n"
        m = re.match(r"p=\$\(cat /root/etats/([\w-]+)\.pid", commande)
        if m:
            self.appels.append(f"arret:{m.group(1)}")
            return 0, ""
        m = re.search(r"cat /root/etats/([\w-]+)\.fin", commande)
        if m:
            fin = self.fins.get(m.group(1))
            return 0, ("VIVANT\n" if fin is None else ("MORT\n" if fin == "MORT" else fin))
        m = re.search(r"instance_v6 tours --travail /root/x/([\w-]+)", commande)
        if m:
            a = shlex.split(commande.split("instance_v6 ", 1)[1])
            if "--ecrire-etat" in a:
                self.ecrits.append((m.group(1), a[a.index("--cause") + 1]))
                self.appels.append(f"tours:{m.group(1)}")
            t = self.tours.get(m.group(1))
            return (0, "ETAT " + json.dumps({"etat_execution": "reconstitué", **t}) + "\n") if t is not None \
                else (1, "")
        if "instance_v6 empreintes" in commande:
            self.appels.append("empreintes")
            return 0, "ETAT " + json.dumps({"commande": "empreintes", "fichiers": []})
        return 0, ""

    def rapatrier_fichier(self, ident, distant, local):
        raise FileNotFoundError(distant)

    def envoyer_fichier(self, ident, local, distant):
        self.envoyes[distant] = Path(local).read_bytes()


def _monter(tmp_path, monkeypatch, f, horloge=None, pids=None):
    tmp_path.mkdir(parents=True, exist_ok=True)
    depot, commit = depot_git(tmp_path)
    man = tmp_path / "manifeste-local-v5.json"
    la.manifeste_depuis_versions_figees(man, DEPOT / cv.VERSIONS_FIGEES, commit_code=commit, b=75, go_id=GO_ID)
    monkeypatch.setenv("GO_ID", GO_ID)
    monkeypatch.setenv("HF_TOKEN", "jeton-factice-essai")
    veille = {"lances": [], "arretes": []}
    suite = iter(pids) if pids is not None else None

    def lancer(*a):
        veille["lances"].append(a)
        return next(suite) if suite is not None else 4242
    c = la.Conduite(f, man, tmp_path / "sortie", GO_ID, TEXTE_GO_MAIN, "offre", "image", depot, [],
                    horloge=horloge or (lambda: HORLOGE), attendre=lambda s: None, periode_sondage_s=0,
                    lancer_veilleur=lancer, arreter_veilleur=lambda pid: veille["arretes"].append(pid),
                    veilleur_vivant=lambda pid, journal: True)
    return c, veille


def conduite(tmp_path, monkeypatch, reps, horloge=None, pids=None):
    f = FournisseurFactice(reps)
    c, veille = _monter(tmp_path, monkeypatch, f, horloge, pids)
    return c, f, veille


def _bash_local(commande: str, d: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["bash", "-c", commande.replace(la.ETATS_DISTANTS, str(d))], capture_output=True,
                          text=True, timeout=60)


def _lire(c) -> dict:
    return json.loads((c.sortie / "bilan-conduite-v5.json").read_text())


# --- cas sain (unitaire) ------------------------------------------------------------------------------------------------

def test_conduite_saine_bout_en_bout_unitaire(tmp_path, monkeypatch):
    c, f, veille = conduite(tmp_path, monkeypatch, reponses())
    bilan = c.conduire()
    assert f.lance == ["amorce", "mise-en-place", "controle-juge", "pilote", "regle", "principal"]
    assert "arret" not in bilan and f.detruites == ["77"] and bilan["detruite"] is True
    assert f.ecrits == [] and not any(a.startswith("arret:") for a in f.appels)  # rien d'arrêté, rien de reconstitué
    assert f.etiquettes == [bilan["etiquette"]] and bilan["etiquette"].startswith(la.PREFIXE_ETIQUETTE)
    ordre = [json.loads(l) for l in (c.sortie / "conduite-v5.jsonl").read_text().splitlines() if '"ordre"' in l]
    assert ordre[0]["ordre"]["etiquette"] == bilan["etiquette"]
    scellement.verifier(c.sortie / "bilan-conduite-v5.json")
    assert all("instance_v4" not in x for x in f.commandes) and "/root/amorce-v5.sh" in f.envoyes
    assert not any("jeton-factice-essai" in x for x in f.commandes)


# --- C8 (N-1) : état reconstitué sur l'instance, lu par la lecture ------------------------------------------------------

def _manifeste_regle(tmp_path, k):
    m = tmp_path / "manifeste-regle.json"
    m.write_text(json.dumps({"graines": {"pilote": an.GRAINE_PILOTE, "principal": an.GRAINE_PRINCIPAL},
                             "regle_tours": {"K": k}}))
    return m


def _reconstituer(manifeste, cause="coupure de l'hôte", phase="principal"):
    def f(x: Path) -> None:
        (x / cv.ETAT_EXECUTION).unlink()  # exécution morte (ou arrêtée par PID) : pas d'état
        out = io.StringIO()
        with redirect_stdout(out):
            assert inst.main(["tours", "--ecrire-etat", "--travail", str(x), "--phase", phase, "--manifeste",
                              str(manifeste), "--cause", cause]) == 0
        assert la.lire_etat(out.getvalue())["etat_execution"] == "reconstitué"
    return f


def test_N1_inverse_morte_21_tours_sans_relance_lue_sur_K_prime(tmp_path):
    """Sonde N-1 inversée : texte l. 338 et 372, K′ ≥ 20 → lu comme un run de K′ tours, interruption rapportée. La v4
    n'avait pas `tours --ecrire-etat` (aucun état) ; la lecture v3 levait."""
    m = _manifeste_regle(tmp_path, 30)
    racine = T3.poste_local(tmp_path, 21, k_regle=30, modifier_principal=_reconstituer(m))
    v = lc.valider(racine)
    assert v["etat"] is None and v["k_prime"] == 21 and v["fin_de_run"] is True, v["details"]
    (i,) = v["interruptions"]
    assert i["execution"] == "principal" and i["cause_arret"] == "coupure de l'hôte" and i["reconstitue"] is True
    res = lc.lire(v, an.graines()["reechantillonnage"])
    assert res["verdict"].startswith("Effet reproduit sur le banc des auteurs, au régime réduit (K = 21)")
    assert res["interruptions"] == v["interruptions"]
    e = json.loads((Path(v["dossier"]) / cv.ETAT_EXECUTION).read_text())
    assert e["k"] == 30 and e["code_retour"] == 1 and e["tours_complets"] == 21 and len(e["durees"]) == 21


def test_N1_bis_inverse_morte_3_tours_relance_complete_seule_la_relance_porte_le_verdict(tmp_path):
    """Sonde N-1-bis inversée : texte l. 371, seule la relance porte le verdict ; première exécution rapportée comme
    interrompue."""
    m = _manifeste_regle(tmp_path, 30)
    racine = T3.poste_local(tmp_path, 3, k_regle=30, modifier_principal=_reconstituer(m), relance=(21, {}))
    v = lc.valider(racine)
    assert v["etat"] is None and v["k_prime"] == 21 and v["dossier"].endswith("principal-relance/transfert-1")
    (i,) = v["interruptions"]
    assert i["role"].startswith("première exécution") and i["k_prime"] == 3 and i["reconstitue"] is True
    assert lc.lire(v, an.graines()["reechantillonnage"])["verdict"].startswith("Effet reproduit")


def test_C8_lecture_a_defaut_etat_absent(tmp_path):
    """Sans état transféré (instance qui n'a pu l'écrire) : la lecture v5 ne lève plus. Relance : état de la première
    exécution reconstitué à la lecture (journaux seuls) ; verdict porté par la relance. Sans relance : l'état du run
    qui porte le verdict manque → garde de fin de run tombée, « non interprétable »."""
    sans = lambda x: (x / cv.ETAT_EXECUTION).unlink()
    r1 = T3.poste_local(tmp_path / "a", 3, k_regle=30, modifier_principal=sans, relance=(21, {}))
    v = lc.valider(r1)
    assert v["etat"] is None and v["k_prime"] == 21 and v["interruptions"][0]["reconstitue"] == "à la lecture"
    r2 = T3.poste_local(tmp_path / "b", 21, k_regle=30, modifier_principal=sans)
    v = lc.valider(r2)
    assert v["etat"] == "Non interprétable (garde de fin de run)."
    assert any("absent du transfert" in x for x in v["details"]["fin_de_run"])


def test_C8_relance_hors_liste_avec_etat_reconstitue(tmp_path):
    """Artefact : état reconstitué à K′ = 21 (≥ 20) et relance quand même : relance hors de la liste d'arrêt."""
    m = _manifeste_regle(tmp_path, 30)
    racine = T3.poste_local(tmp_path, 21, k_regle=30, modifier_principal=_reconstituer(m), relance=(21, {}))
    assert lc.valider(racine)["etat"] == "Non interprétable (garde de fin de run)."


def test_C8_reconstitution_jamais_d_ecrasement_et_gardes(tmp_path):
    m = _manifeste_regle(tmp_path, 30)
    x, _ = T3.execution_factice(tmp_path, "principal", 5, {"k": 30})
    avant = (x / cv.ETAT_EXECUTION).read_bytes()
    out = io.StringIO()
    with redirect_stdout(out):
        assert inst.main(["tours", "--ecrire-etat", "--travail", str(x), "--phase", "principal", "--manifeste",
                          str(m), "--cause", "dépense"]) == 0
    assert la.lire_etat(out.getvalue())["etat_execution"] == "déjà présent"
    assert (x / cv.ETAT_EXECUTION).read_bytes() == avant  # jamais d'écrasement
    (x / cv.ETAT_EXECUTION).unlink()
    out = io.StringIO()
    with redirect_stdout(out):
        assert inst.main(["tours", "--ecrire-etat", "--travail", str(x), "--phase", "principal", "--manifeste",
                          str(m), "--cause", "panne inventée"]) == 3
    assert "liste fermée" in la.lire_etat(out.getvalue())["garde_tombee"] and not (x / cv.ETAT_EXECUTION).exists()
    with pytest.raises(SystemExit):
        inst.main(["tours", "--ecrire-etat", "--travail", str(x), "--cause", "dépense"])  # phase, manifeste exigés
    # cause « dépense » : run tronqué, pas de relance (liste d'arrêt) ; pilote : « arrêt »
    e = inst.reconstituer_etat(x, json.loads(m.read_text()), "principal", "dépense")
    etat_ = json.loads((x / cv.ETAT_EXECUTION).read_text())
    assert e["etat_execution"] == "reconstitué" and lc.relance_permise(etat_) is False
    y, _ = T3.execution_factice(tmp_path / "p", "pilote", 2, {"k": 3})
    (y / cv.ETAT_EXECUTION).unlink()
    inst.reconstituer_etat(y, json.loads(m.read_text()), "pilote", "échéance du GO")
    assert lc.issue_pilote(json.loads((y / cv.ETAT_EXECUTION).read_text())) == "arrêt"
    z, _ = T3.execution_factice(tmp_path / "z", "principal", 4, {"k": 30})
    (z / cv.ETAT_EXECUTION).unlink()
    inst.reconstituer_etat(z, json.loads(m.read_text()), "principal", "coupure de l'hôte")
    assert lc.relance_permise(json.loads((z / cv.ETAT_EXECUTION).read_text())) is True  # cas sain : relance


def test_N1_ter_l_etat_reste_un_journal_attendu_et_il_est_present(tmp_path):
    """Sonde N-1-ter : `ETAT_EXECUTION` reste parmi les journaux attendus (garde de fin de run inchangée) ; avec C8 il
    est présent : les empreintes prises sur l'instance le couvrent, et la garde passe (essai N-1 inversé)."""
    assert cv.ETAT_EXECUTION in cv.NOMS_JOURNAUX
    m = _manifeste_regle(tmp_path, 30)
    racine = T3.poste_local(tmp_path, 21, k_regle=30, modifier_principal=_reconstituer(m))
    assert cv.ETAT_EXECUTION in json.loads((racine / "principal" / cv.EMPREINTES_INSTANCE).read_text())


def test_lecture_execution_sans_journaux_transferes(tmp_path):
    """Instance injoignable : aucune empreinte transférée pour l'exécution : K′ = 0, pas de verdict, nœud (l. 372)."""
    racine = T3.poste_local(tmp_path, 21, k_regle=30)
    shutil.rmtree(racine / "principal")
    (racine / "principal").mkdir()
    v = lc.valider(racine)
    assert v["etat"].startswith("Pas de verdict (moins de 20 tours") and v["k_prime"] == 0
    assert v["interruptions"][0]["role"] == "run sans journaux transférés"
    shutil.rmtree(racine / "pilote")
    (racine / "pilote").mkdir()
    assert lc.valider(racine)["etat"].startswith("Pas de run principal, pas de verdict (exécution du pilote sans")


# --- C8 : de bout en bout, conduite factice adossée à des dossiers locaux ----------------------------------------------

class FournisseurLocal(la.Fournisseur):
    """Instance factice : `/root/…` → `<base>/root/…`. Les étapes sont fabriquées au lancement (journaux réels du
    journaliseur v3, sans modèle) ; `empreintes` et `tours` de `instance_v6` sont joués pour de vrai ; les transferts
    copient les fichiers. Une étape « mort » perd son état et disparaît sans `.fin` ; « vivant » ne finit jamais."""

    def __init__(self, tmp: Path, scenario: dict):
        self.tmp, self.base, self.scenario = tmp, tmp / "instance", scenario
        self.detruites, self.appels, self.lance, self.commandes, self.fins = [], [], [], [], {}
        self.lignes = T3.jeu(tmp / "jeu")

    def local(self, distant: str) -> Path:
        assert distant.startswith("/root/"), distant
        return self.base / distant[1:]

    def creer(self, offre, image, disque_go, etiquette=None):
        return "77"

    def inventaire(self, etiquette):
        return []

    def taux_horaire(self, ident):
        return 1.0

    def statut(self, ident):
        return "running"

    def detruire(self, ident):
        self.detruites.append(ident)

    def envoyer_fichier(self, ident, local, distant):
        p = self.local(distant)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(Path(local).read_bytes())

    def rapatrier_fichier(self, ident, distant, local):
        src = self.local(distant)
        if not src.is_file():
            raise FileNotFoundError(distant)
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(src.read_bytes())

    def executer(self, ident, commande, delai_s=None):
        self.commandes.append(commande)
        m = re.search(r"echo \$p > /root/etats/([\w-]+)\.pid", commande)
        if m:
            nom = m.group(1)
            self.lance.append(nom)
            r = self.scenario[nom](self)
            if r == "mort":
                self.fins[nom] = "MORT"
            elif r != "vivant":
                etat, code = r
                self.fins[nom] = "ETAT " + json.dumps(etat) + f"\nCODE {code}\n"
            return 0, "LANCE 4321\n"
        m = re.match(r"p=\$\(cat /root/etats/([\w-]+)\.pid", commande)
        if m:
            self.appels.append(f"arret:{m.group(1)}")
            return 0, ""
        m = re.search(r"cat /root/etats/([\w-]+)\.fin", commande)
        if m:
            fin = self.fins.get(m.group(1))
            return 0, ("VIVANT\n" if fin is None else ("MORT\n" if fin == "MORT" else fin))
        cle = f"-m {la.INSTANCE_MODULE} "
        if cle in commande:
            args = [str(self.base) + a if a.startswith("/root/") else a
                    for a in shlex.split(commande.split(cle, 1)[1])]
            self.appels.append(f"{args[0]}:{Path(args[2]).name}")
            out = io.StringIO()
            try:
                with redirect_stdout(out):
                    code = inst.main(args)
            except SystemExit as err:
                code = int(err.code or 2)
            return code, out.getvalue()
        return 0, ""

    # --- fabrication des étapes ---
    def ecrire(self, etape: str, nom: str, objet: dict) -> None:
        d = self.local(f"/root/x/{etape}")
        d.mkdir(parents=True, exist_ok=True)
        (d / nom).write_text(json.dumps(objet))

    def execution(self, nom: str, k_journal: int, etat: dict) -> Path:
        x, _ = T3.execution_factice(self.tmp / f"fab-{nom}", nom, k_journal, {"phase": nom, **etat})
        cible = self.local(f"/root/x/{nom}")
        shutil.copytree(x, cible)
        return cible


T_REGLE = 9200.0  # K de relance = ⌊72 000 × 65 / (23 × 9 200)⌋ = 22 (D = 0, c = 1)


def scenario(k_regle: int, principal):
    def mep(f):
        g = {x: "passée" for x in cv.GARDES_MISE_EN_PLACE}
        f.ecrire("mise-en-place", cv.ETAT_MISE_EN_PLACE, {
            "gardes": g, "pas_par_tour": T3.PAS, "ecart_10": False, "longueur_suffixe": 16,
            "empreintes_cibles_attendues": [cv.sha_texte(r) for _, r in f.lignes]})
        return {"commande": "mise-en-place", "gardes": g, "pas_par_tour": T3.PAS, "longueur_suffixe": 16,
                "ecart_10": False}, 0

    def juge(f):
        f.ecrire("controle-juge", cv.ETAT_CONTROLE_JUGE, {"garde_juge": "passée", "etats": {"tenus": True}})
        return {"commande": "controle-juge", "etats": {"tenus": True}, "garde_juge": "passée"}, 0

    def pilote(f):
        x = f.execution("pilote", 3, {"k": 3, "graine": an.GRAINE_PILOTE,
                                      "durees": {"0": T_REGLE, "1": T_REGLE, "2": T_REGLE}})
        return {"commande": "executer", **json.loads((x / cv.ETAT_EXECUTION).read_text())}, 0

    def regle(f):
        r = {"B": 75, "R": 10, "D": 0.0, "c": 1.0, "t": T_REGLE, "H_heures": 65.0, "K": k_regle, "arret": False}
        f.ecrire("regle", cv.ETAT_REGLE, r)
        return {"commande": "regle-tours", **r}, 0

    def relance(f):
        k2 = json.loads(f.local("/root/manifeste-v3-relance.json").read_text())["regle_tours"]["K"]
        x = f.execution("principal-relance", k2, {"k": k2})
        return {"commande": "executer", **json.loads((x / cv.ETAT_EXECUTION).read_text())}, 0

    return {"amorce": lambda f: ({"commande": "amorce", "finie": True}, 0), "mise-en-place": mep,
            "controle-juge": juge, "pilote": pilote, "regle": regle, "principal": principal,
            "principal-relance": relance}


def principal_fini(k):
    def p(f):
        x = f.execution("principal", k, {"k": k})
        return {"commande": "executer", **json.loads((x / cv.ETAT_EXECUTION).read_text())}, 0
    return p


def principal_sans_etat(k_journal, k_regle, issue):
    """Exécution qui a écrit `k_journal` tours puis perd son processus (« mort ») ou ne finit pas (« vivant »)."""
    def p(f):
        x = f.execution("principal", k_journal, {"k": k_regle})
        (x / cv.ETAT_EXECUTION).unlink()
        return issue
    return p


def conduite_locale(tmp_path, monkeypatch, scen, horloge=None):
    f = FournisseurLocal(tmp_path, scen)
    c, veille = _monter(tmp_path, monkeypatch, f, horloge)
    return c, f, veille


def test_bout_en_bout_sain_conduite_puis_lecture(tmp_path, monkeypatch):
    c, f, _ = conduite_locale(tmp_path, monkeypatch, scenario(21, principal_fini(21)))
    bilan = c.conduire()
    assert "arret" not in bilan and "erreur" not in bilan and f.detruites == ["77"]
    assert "etats_reconstitues" not in bilan and not any(a.startswith(("arret:", "tours:")) for a in f.appels)
    assert bilan["transferts"]["principal"]["foi"] == "transfert-1"
    v = lc.valider(c.sortie)
    assert v["etat"] is None and v["k_prime"] == 21 and v["interruptions"] == [], v["details"]
    res = lc.lire(v, an.graines()["reechantillonnage"])
    assert res["verdict"].startswith("Effet reproduit sur le banc des auteurs, au régime réduit (K = 21)")


def test_bout_en_bout_C8_morte_K_prime_21_sans_relance(tmp_path, monkeypatch):
    """Texte l. 338, 372 : coupure de l'hôte après 21 tours complets (K = 30) : groupe arrêté (C10), état reconstitué
    sur l'instance avant les empreintes, pas de relance, lu comme un run de 21 tours, interruption rapportée."""
    c, f, _ = conduite_locale(tmp_path, monkeypatch, scenario(30, principal_sans_etat(21, 30, "mort")))
    bilan = c.conduire()
    assert "principal-relance" not in f.lance and f.detruites == ["77"]
    a = f.appels
    assert a.index("arret:principal") < a.index("tours:principal") < a.index("empreintes:principal")
    assert bilan["principal"][0]["tours_complets"] == 21 and bilan["principal"][0]["etat_execution"] == "reconstitué"
    v = lc.valider(c.sortie)
    assert v["etat"] is None and v["k_prime"] == 21, v["details"]
    (i,) = v["interruptions"]
    assert i["cause_arret"] == "coupure de l'hôte" and i["reconstitue"] is True
    res = lc.lire(v, an.graines()["reechantillonnage"])
    assert res["verdict"].startswith("Effet reproduit sur le banc des auteurs, au régime réduit (K = 21)")


def test_bout_en_bout_C8_morte_3_tours_relance_complete(tmp_path, monkeypatch):
    """Texte l. 371 : coupure avant 20 tours ; une relance (K recalculé = 22) ; seule la relance porte le verdict ; la
    première exécution est rapportée comme interrompue."""
    c, f, _ = conduite_locale(tmp_path, monkeypatch, scenario(30, principal_sans_etat(3, 30, "mort")))
    bilan = c.conduire()
    assert f.lance[-2:] == ["principal", "principal-relance"] and f.detruites == ["77"]
    a = f.appels
    assert a.index("arret:principal") < a.index("tours:principal")
    assert json.loads((c.sortie / lc.MANIFESTES["relance"]).read_text())["regle_tours"]["K"] == 22
    v = lc.valider(c.sortie)
    assert v["etat"] is None and v["k_prime"] == 22 and v["dossier"].endswith("principal-relance/transfert-1")
    (i,) = v["interruptions"]
    assert i["role"].startswith("première exécution") and i["k_prime"] == 3 and i["reconstitue"] is True
    res = lc.lire(v, an.graines()["reechantillonnage"])
    assert res["verdict"].startswith("Effet reproduit sur le banc des auteurs, au régime réduit (K = 22)")
    assert "arret" not in bilan


def test_bout_en_bout_C8_seuil_local_run_tronque_sans_relance(tmp_path, monkeypatch):
    """Arrêt au seuil local (D ≥ B − 1) pendant le run principal : arrêt par PID, état reconstitué (cause « dépense »)
    avant les empreintes ; pas de relance (dépense) ; lu comme un run tronqué de 21 tours."""
    c, f, _ = conduite_locale(tmp_path, monkeypatch, scenario(30, principal_sans_etat(21, 30, "vivant")),
                              horloge=horloge_pas(360.0))
    bilan = c.conduire()
    assert bilan["arret"].startswith("seuil local de dépense") and "principal-relance" not in f.lance
    assert bilan["etats_reconstitues"]["principal"]["etat_execution"] == "reconstitué"
    a = f.appels
    assert a.index("arret:principal") < a.index("tours:principal") < a.index("empreintes:principal")
    v = lc.valider(c.sortie)
    assert v["etat"] is None and v["k_prime"] == 21, v["details"]
    assert v["interruptions"][0]["cause_arret"] == "dépense"
    e = json.loads((Path(v["dossier"]) / cv.ETAT_EXECUTION).read_text())
    assert lc.relance_permise(e) is False
    assert lc.lire(v, an.graines()["reechantillonnage"])["verdict"].startswith("Effet reproduit")


# --- C9 (N-2) : destruction en échec → veilleur à échéance 0, toujours ------------------------------------------------

def test_N2_inverse_destruction_en_echec_veilleur_vivant_nouveau_veilleur_a_echeance_0(tmp_path, monkeypatch):
    c, f, veille = conduite(tmp_path, monkeypatch, reponses(), pids=[4242, 5353])
    essais = []
    f.detruire = lambda ident: essais.append(ident) or (_ for _ in ()).throw(RuntimeError("API indisponible"))
    bilan = c.conduire()
    assert bilan["detruite"] is False and len(essais) == la.ESSAIS_DESTRUCTION
    assert len(veille["lances"]) == 2 and veille["lances"][-1][2] == 0.0  # v4 : un seul veilleur, à l'échéance du GO
    assert veille["arretes"] == [4242] and bilan["veilleur_de_destruction"] == 5353 and "alerte" not in bilan


def test_C9_nouveau_veilleur_non_vivant_l_ancien_est_garde(tmp_path, monkeypatch):
    c, f, veille = conduite(tmp_path, monkeypatch, reponses(), pids=[4242, 5353])
    f.detruire = lambda ident: (_ for _ in ()).throw(RuntimeError("API indisponible"))
    c.veilleur_vivant = lambda pid, journal: pid == 4242
    bilan = c.conduire()
    assert veille["lances"][-1][2] == 0.0 and veille["arretes"] == [] and "non vu vivant" in bilan["alerte"]


# --- C10 (N-3) : arrêt du groupe sur « mort », avant `tours` et la relance --------------------------------------------

def test_N3_inverse_mort_arret_du_groupe_avant_tours_et_relance(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses(principal="mort"))
    f.tours["principal"] = {"commande": "tours", "tours_complets": 5, "journal_absent": None, "gardes_tombees": []}
    c.conduire()
    i_relance = next(i for i, x in enumerate(f.commandes) if "principal-relance.pid" in x)
    avant = f.commandes[:i_relance]
    assert la.commande_arret("principal") in avant  # v4 : aucun arrêt
    a = f.appels
    assert a.index("arret:principal") < a.index("tours:principal") < a.index("lance:principal-relance")
    assert f.ecrits == [("principal", "coupure de l'hôte")]


def test_N3_bis_inverse_bash_reel_arret_sans_membre_restant(tmp_path):
    d = tmp_path / "etats"
    r = _bash_local(la.commande_detachee("x", "sleep 60"), d)
    pid = int(r.stdout.split()[-1])
    time.sleep(0.5)
    try:
        os.kill(pid, signal.SIGKILL)  # seul le meneur meurt ; `sleep` vit dans le groupe
        time.sleep(0.5)
        s = _bash_local(la.commande_sondage("x"), d)
        assert la.lire_sondage(s.returncode, s.stdout) == "mort"
        assert subprocess.run(["pgrep", "-g", str(pid)], capture_output=True, text=True).stdout.split()
        _bash_local(la.commande_arret("x"), d)
        assert subprocess.run(["pgrep", "-g", str(pid)], capture_output=True, text=True).stdout.split() == []
    finally:
        try:
            os.killpg(pid, signal.SIGKILL)
        except ProcessLookupError:
            pass


def test_C10_arret_en_bash_reel_meneur_vivant(tmp_path):
    """Cas sain : meneur vivant, à l'identité écrite : le groupe entier s'arrête (TERM)."""
    d = tmp_path / "etats"
    r = _bash_local(la.commande_detachee("y", "sleep 60"), d)
    pid = int(r.stdout.split()[-1])
    time.sleep(0.5)
    try:
        s = _bash_local(la.commande_sondage("y"), d)
        assert la.lire_sondage(s.returncode, s.stdout) == "vivant"
        _bash_local(la.commande_arret("y"), d)
        assert subprocess.run(["pgrep", "-g", str(pid)], capture_output=True, text=True).stdout.split() == []
    finally:
        try:
            os.killpg(pid, signal.SIGKILL)
        except ProcessLookupError:
            pass


# --- N-4 : PID réemployé ------------------------------------------------------------------------------------------------

def test_N4_inverse_pid_reemploye_sonde_mort_et_jamais_signale(tmp_path):
    d = tmp_path / "etats"
    d.mkdir()
    autre = subprocess.Popen(["sleep", "30"])
    time.sleep(0.2)  # heure de départ comptée en tops d'horloge (10 ms) : deux lancements distincts, deux heures
    try:
        (d / "x.pid").write_text(f"{autre.pid}\n")  # comme la sonde : PID d'un processus sans rapport, sans identité
        s = _bash_local(la.commande_sondage("x"), d)
        assert la.lire_sondage(s.returncode, s.stdout) == "mort"  # v4 : « vivant »
        # identité d'un autre lancement (PID réemployé après redémarrage) : « mort », et l'arrêt ne le signale pas
        r = _bash_local(la.commande_detachee("z", "true"), d)
        time.sleep(0.5)
        (d / "z.fin").unlink()
        (d / "z.pid").write_text(f"{autre.pid}\n")
        s = _bash_local(la.commande_sondage("z"), d)
        assert la.lancement_verifie(r.stdout) and la.lire_sondage(s.returncode, s.stdout) == "mort"
        _bash_local(la.commande_arret("z", attente_s=1), d)
        assert autre.poll() is None  # toujours vivant : jamais signalé
        # second lancement sur ce nom : l'identité ne correspond pas, la commande est relancée (pas de faux « vivant »)
        r = _bash_local(la.commande_detachee("z", "true"), d)
        assert int(r.stdout.split()[-1]) != autre.pid
    finally:
        autre.kill()
        autre.wait()


def test_N4_identite_ecrite_au_lancement(tmp_path):
    d = tmp_path / "etats"
    r = _bash_local(la.commande_detachee("w", "sleep 30"), d)
    pid = int(r.stdout.split()[-1])
    try:
        boot, depart = (d / "w.debut").read_text().split()
        champs = Path(f"/proc/{pid}/stat").read_text().rsplit(")", 1)[1].split()
        assert depart == champs[19] and boot == Path("/proc/sys/kernel/random/boot_id").read_text().strip()
    finally:
        _bash_local(la.commande_arret("w"), d)


# --- C11 (N-5) : `creer` qui lève : inventaire par étiquette ------------------------------------------------------------

def test_N5_inverse_creer_qui_leve_inventaire_par_etiquette(tmp_path, monkeypatch):
    c, f, veille = conduite(tmp_path, monkeypatch, reponses())
    creees = []

    def creer(offre, image, disque, etiquette=None):
        creees.append(("88", etiquette))  # l'instance existe ; la réponse se perd
        raise subprocess.TimeoutExpired(["vastai", "create"], 120)
    f.creer = creer
    f.inventaire = lambda etiq: [i for i, e in (("88", creees[0][1]), ("99", "autre-etiquette"))
                                 if e == etiq]
    with pytest.raises(subprocess.TimeoutExpired):
        c.conduire()
    assert f.detruites == ["88"] and veille["lances"] == []  # v4 : rien de détruit ; jamais « 99 »
    b = _lire(c)
    assert b["detruite"] is True and b["etiquette"] == creees[0][1] and "alerte" not in b
    scellement.verifier(c.sortie / "bilan-conduite-v5.json")


def test_C11_inventaire_illisible_ou_vide_alerte(tmp_path, monkeypatch):
    for n, inv in enumerate((lambda e: (_ for _ in ()).throw(RuntimeError("API")), lambda e: [])):
        c, f, _ = conduite(tmp_path / str(n), monkeypatch, reponses())
        f.creer = lambda *a: (_ for _ in ()).throw(subprocess.TimeoutExpired("vastai", 120))
        f.inventaire = inv
        with pytest.raises(subprocess.TimeoutExpired):
            c.conduire()
        assert f.detruites == [] and "création incertaine : inventaire R10 manuel" in _lire(c)["alerte"]


def test_C11_vast_label_et_inventaire_filtre(monkeypatch):
    v = la.FournisseurVast()
    appels = []

    def vast(*args):
        appels.append(args)
        if args[:2] == ("show", "instances"):
            return json.dumps([{"id": 88, "label": "temoin-bailey-c6-abc"}, {"id": 99, "label": "autre"},
                               {"id": 100, "label": None}])
        return json.dumps({"new_contract": 88})
    monkeypatch.setattr(v, "_vast", vast)
    assert v.creer("o", "i", 200, "temoin-bailey-c6-abc") == "88"
    assert appels[0][-2:] == ("--label", "temoin-bailey-c6-abc")
    assert v.inventaire("temoin-bailey-c6-abc") == ["88"]


# --- remarque R10 : un veilleur récolté n'est jamais signalé -----------------------------------------------------------

def test_remarque_veilleur_recolte_jamais_signale(tmp_path, monkeypatch):
    detruites = tmp_path / "d.txt"
    pid = la.lancer_veilleur_processus(tmp_path / "absent.json", "9", 1e12, tmp_path / "a.jsonl",
                                       f"fichier:{detruites}", 0.05)
    fin = time.time() + 30
    while time.time() < fin and la.processus_vivant(pid):
        time.sleep(0.1)
    assert la.processus_vivant(pid) is False and detruites.read_text().split() == ["9"]
    signaux = []
    monkeypatch.setattr(la.os, "kill", lambda *a: signaux.append(a))
    la.arreter_veilleur(pid)  # récolté par `poll` : son PID peut être réemployé, aucun signal
    assert signaux == []


def test_remarque_processus_vivant_ne_recolte_pas_un_pid_inconnu():
    p = subprocess.Popen(["true"])
    time.sleep(0.5)
    assert la.processus_vivant(p.pid) is False  # zombie, non récolté ici
    assert p.poll() == 0  # toujours récoltable par son propriétaire


# --- C6 : archive et fermeture des imports, v5 --------------------------------------------------------------------------

def test_C6_v5_fermeture_des_imports_de_l_instance():
    racine = DEPOT / "src"
    presents = {str(Path(p).relative_to("src").with_suffix("")).replace("/", ".").removesuffix(".__init__")
                for p in la.CHEMINS_ARCHIVE}
    for p in la.CHEMINS_ARCHIVE:
        mod = str(Path(p).relative_to("src").with_suffix("")).replace("/", ".")
        paquet = mod.removesuffix(".__init__") if p.endswith("__init__.py") else mod.rsplit(".", 1)[0]
        for cible in T4._imports_relatifs(racine / Path(p).relative_to("src"), paquet):
            assert cible in presents, (p, cible)
    assert "src/controle_ia/temoin_bailey/instance_v6.py" in la.CHEMINS_ARCHIVE
    assert not any(p.endswith(("instance_v5.py", "lanceur_v6.py", "lecture_v3.py", "lecture_v5.py")) for p in la.CHEMINS_ARCHIVE)


def test_C6_v5_l_archive_s_importe_seule(tmp_path):
    for p in la.CHEMINS_ARCHIVE:
        (tmp_path / p).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(DEPOT / p, tmp_path / p)
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    env["PYTHONPATH"] = str(tmp_path / "src")
    r = subprocess.run([sys.executable, "-m", la.INSTANCE_MODULE, "--help"], cwd=tmp_path, env=env,
                       capture_output=True, text=True)
    assert r.returncode == 0 and "--ecrire-etat" in r.stdout


def test_C6_v5_archive_limitee(tmp_path):
    d, sha = depot_git(tmp_path)
    archive, h = la.fabriquer_archive(d, sha, tmp_path / "arch")
    with tarfile.open(archive) as t:
        noms = sorted(m.name for m in t.getmembers() if m.isfile())
    assert noms == sorted(la.CHEMINS_ARCHIVE) and h == cv.sha_fichier(archive)


# --- inchangé depuis la v4, rejoué sur la v5 ----------------------------------------------------------------------------

def test_v4_rejoue_sur_v5_pilote_mort_reprise_et_seuil_local(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path / "a", monkeypatch, reponses(pilote="mort"))
    f.tours["pilote"] = {"tours_complets": 0, "journal_absent": None, "gardes_tombees": []}
    assert "arret" not in c.conduire() and f.lance[3:5] == ["pilote", "pilote-reprise"]
    assert f.ecrits == [("pilote", "coupure de l'hôte")]
    c, f, _ = conduite(tmp_path / "b", monkeypatch, reponses(principal="vivant-sans-fin"), horloge=horloge_pas(360.0))
    f.tours["principal"] = {"tours_complets": 30, "journal_absent": None, "gardes_tombees": []}
    bilan = c.conduire()
    assert bilan["arret"].startswith("seuil local de dépense") and f.ecrits == [("principal", "dépense")]
    assert 74 <= bilan["depense"] < 75 - la.MARGE_SECOURS_USD


def test_v4_rejoue_sur_v5_injoignable_cause_notee(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses(principal="vivant-sans-fin"))
    vrai = f.executer

    def executer(ident, commande, delai_s=None):
        if "cat /root/etats/principal.fin" in commande:
            return 255, ""
        return vrai(ident, commande, delai_s)
    f.executer = executer
    bilan = c.conduire()
    assert bilan["arret"].startswith("instance injoignable") and f.ecrits == [("principal", "instance injoignable")]
    a = f.appels
    assert a.index("arret:principal") < a.index("tours:principal") < a.index("empreintes") < a.index("detruire")
    assert bilan["etats_reconstitues"]["principal"] is None  # `tours` sans réponse : consigné, jamais levé


# --- M-1 et M-2 (relecture des lignes touchées v5, `22879993…`) -------------------------------------------------------

def test_M2_derniere_ligne_coupee_ignoree_et_signalee(tmp_path):
    p = tmp_path / "j.jsonl"
    p.write_text('{"a": 1}\n{"a": 2}\n{"a": ', encoding="utf-8")  # écriture coupée, sans fin de ligne
    lc.LIGNES_TRONQUEES.clear()
    assert lc.lire_jsonl(p) == [{"a": 1}, {"a": 2}]
    assert lc.LIGNES_TRONQUEES == ["j.jsonl"]


def test_M2_ligne_illisible_au_milieu_ou_finie_leve(tmp_path):
    from controle_ia.gardes import GardeArret
    p = tmp_path / "j.jsonl"
    p.write_text('{"a": 1}\n{"a": \n{"a": 3}\n', encoding="utf-8")
    with pytest.raises(GardeArret, match="illisible"):
        lc.lire_jsonl(p)
    p.write_text('{"a": 1}\n{"a": \n', encoding="utf-8")  # dernière ligne illisible mais finie : pas une coupure
    with pytest.raises(GardeArret, match="illisible"):
        lc.lire_jsonl(p)
    p.write_text('{"a": 1}\n', encoding="utf-8")
    lc.LIGNES_TRONQUEES.clear()
    assert lc.lire_jsonl(p) == [{"a": 1}] and lc.LIGNES_TRONQUEES == []


def test_M2_valider_rapporte_les_lignes_tronquees(tmp_path):
    r = lc.valider(tmp_path)
    assert "lignes_tronquees_ignorees" in r


def test_M1_execution_morte_inscrite_dans_arretees():
    import inspect
    src = inspect.getsource(la.Conduite._executer)
    i = src.index("if t is None:", src.index('if issue == "mort":'))
    assert "self.arretees.setdefault(phase, \"coupure de l'hôte\")" in src[i:i + 250]
