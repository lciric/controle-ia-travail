"""Essais du code v21 du témoin de Bailey (lanceur_v21) : les essais v20 rejoués sur `lanceur_v21`, plus la garde de durée
de tour du pilote (addendum 7) : cas sain (t sous le plafond : run principal lancé), plafond atteint exactement (passe),
artefact (t au-dessus : arrêt avant le run principal, instance détruite, aucune exécution principale).

Docstring des essais v20 :

Essais du code v20 du témoin de Bailey (lanceur_v21) : les essais v19 rejoués sur `lanceur_v21`, adaptés à la
garde de dépense resserrée (R-1 : le pilote factice de la première conduite a t = 3 600 s, et l'instance antérieure
couvre D + c × K′ × t / 3 600), plus les essais de la relecture différentielle v19 (`8fa2fdc5…`) : R-1 (taux, ordre
des dates, borne), R-3 (manifeste de relance), R-4 (C-2 sur chaque champ, C-5 « différents », C-4 manifeste altéré ou
absent et clés manquantes, sortie non créée, valeurs réelles), R-5 (motif précis), R-6 (manifeste absent : cible non
créée), R-7 (message), R-8 (gardes tombées de la première).

Docstring des essais v19 :

Essais du code v19 du témoin de Bailey (lanceur_v21) : les essais v17 rejoués sur `lanceur_v21`, plus ceux de la
relance seule et de l'assemblage (addendum 5), repris de la v18 et complétés selon la contre-lecture du code v18
(`cd540827…`) : C-1 (instances antérieures, D), C-2 (même mise en place), C-4 (gardes d'entrée), C-5 (graines, code
public, B), C-6 (exception attendue précise), C-7 (première exécution sans état comme la reprise réelle ; assemblage sur
une copie de la structure réelle de `reprise-v10-2` réduite aux dossiers et aux JSON, sans aucun journal ; refus :
juge de la relance non tenu, relance qui porte un pilote, première conduite incomplète).

Docstring des essais v18 :

Essais du code v18 du témoin de Bailey (lanceur_v21 ; instance_v16, execution_v4 inchangés) : les essais v17 rejoués
sur `lanceur_v21`, plus ceux de la relance seule et de l'assemblage pour la lecture (addendum 5) : cas sain de bout en
bout (première conduite interrompue à 3 tours, relance seule par une conduite neuve, assemblage, `valider` et `lire`) ;
artefacts : gardes d'entrée avant toute création d'instance (K′ ≥ 20, booléen, t nul, règle incomplète), K de relance
< 20, contrôle du juge hors seuil, assemblage refusé (relance déjà présente, mise en place de la relance tombée, fichier
scellé altéré, manifeste qui ne cite pas la règle, cible présente).

Docstring des essais v17 :

Essais du code v17 du témoin de Bailey (lanceur_v21, instance_v16, execution_v4) : les essais v16 rejoués sur les
modules v17, plus l'épreuve réelle de `@hydra.main` (décision de Lazar du 12 novembre 2026, « go (a), garde le poste ») :
un mini-clone synthétique (`configs/`, `obf_reps`, `train_harmful.py` décoré comme le script public, l. 171) lancé par
`python -m controle_ia.temoin_bailey.execution_v4` dans un processus enfant réel ; cas sain (configuration imprimée égale
à `configuration_attendue`, journaliseur substitué vu par le script) ; artefact (le même mini-clone par `execution_v3`
échoue avant toute impression, comme sur l'instance) ; erreur du script propagée (code non nul, aucun repli).

Docstring des essais v16 :

Essais du code v16 du témoin de Bailey (lanceur_v21, instance_v16) : les essais v15 rejoués sur les modules v16,
plus les essais demandés par la relecture différentielle (`relecture-differentiel-code-condition6-v15-bailey-v1.md`,
`0d7cc2a1…`) : D-1, D-2, D-3 (filtre), D-4 (aucun arrêt décidé, enfant muet), D-7 (vacuité), D-8 (lecture).

Docstring des essais v15 :

Essais du code v15 du témoin de Bailey (lanceur_v21, instance_v16) : les essais v14 rejoués sur les modules v15
(relecture `relecture-code-condition6-v14-bailey-v1.md`, `0e7c96ca…`), l'essai instable R-7 corrigé (attente bornée), les
essais v14 du message d'erreur adaptés au filtre v14 (R-1), et les essais demandés par R-2, R-5 et R-6 (fin du fichier).

Docstring des essais v14 :

Essais du code v14 du témoin de Bailey (lanceur_v21, instance_v16) : les essais v13 rejoués sur les modules v14,
plus les essais du message d'erreur d'une exécution morte avant tout tour (fin du fichier). Décision de Lazar « go (a) »,
12 novembre 2026.

Docstring des essais v13 :

Essais v13 : ceux de la v12, rejoués sur `lanceur_v21` (module `instance_v16` inchangé ; attendus changés par la
v13 seulement là où le comportement change : noms de module du veilleur), plus la relecture du code v12
(`docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v12-bailey-v1.md`, `3865961f…`) : un cas sain
et un artefact par point (W-1, P-1 à P-4), et les sondes S10 à S13 du relecteur (`test_sondes_v12.py`, `7a3c60eb…`)
réécrites en essais inversés : elles passent sur la v13 et échouent sur la v12 (section « v13 », en fin de fichier).

Texte d'origine des essais v12 :

Essais v12 : ceux de la v11, rejoués sur `lanceur_v12` et `instance_v16` (chaînes de commande portées en v12 ;
attendus changés par la v12 seulement là où le comportement change : écart du veilleur de secours retranché des
bornes de la reprise (V-5), marque `rapatrie` posée seulement sur un transfert complet (Q-2)), plus la relecture du
code v11 (`relecture-code-condition6-v11-bailey-v1.md`, `044ba3e2…`) : un cas sain et un artefact par correction
(V-1 à V-5, Q-1, Q-2, Q-4), et les sondes S5 à S9 du relecteur (`test_sondes_v11.py`, `ee331e03…`) inversées : elles
passent sur la v12 et échouent sur la v11 (section « v12 », en fin de fichier).

Texte d'origine des essais v11 :

Essais v11 : ceux de la v10, rejoués sur `lanceur_v11` et `instance_v11` (chaînes de commande portées en v11 ;
`_poste_interrompu` remplace le veilleur local d'arrêt de la reprise par un substitut ; la reprise exige désormais un
veilleur vivant avant le redémarrage), plus la relecture du code v10 (`relecture-code-condition6-v10-bailey-v1.md`,
`b6b6430b…`) : un cas sain et un artefact par correction (B-1, B-2, B-3, C-1, C-2, P-1, P-4, P-7), et les sondes S1 à
S4 du relecteur (`test_sondes_relecteur.py`, `157d67d9…`) inversées (section « v11 »).

Texte d'origine des essais v10 :

Essais v10 : ceux de la v9, rejoués sur `lanceur_v10` et `instance_v10` (chaînes de commande portées en v10 ;
étape « auto-arret » ajoutée aux réponses des fournisseurs factices), plus l'arrêt autonome de l'instance (décision
de Lazar du 11 novembre 2026, option (b)) : cas 1 à 4 (fin de la dernière exécution prévue, dépense ≥ B − 2,
échéance du GO moins la marge, conduite injoignable), chacun avec un cas sain et un artefact ; garde d'auto-arrêt
indisponible à la mise en place ; `reprendre` (en fin de fichier, section « v10 »).

Texte d'origine des essais v9 :

Essais v9 : ceux de la v8, rejoués sur `lanceur_v9`, plus C-1 (S1 inversée, relecture `baa35511…`).

Épreuve (R5) du code de la condition 6 du témoin de Bailey, v8 : essais de la v7 rejoués sur `lanceur_v9`,
`instance_v8`, `lecture_v8` (modules et chaînes de commande portés en v8, attendus de A-1 corrigés), plus les essais
de la décision de Lazar du 10 novembre 2026 sur les points A-1 et A-2 de la relecture des lignes touchées v6 → v7
(`relecture-lignes-touchees-code-condition6-v7-bailey-v1.md`, `5831e98c…`) et les sondes Q1, Q2 du relecteur
(`test_sondes_r2_v7.py`, `e26ae9dc…`), inversées (en fin de fichier). Texte d'origine des essais v7 :
essais de la v6 rejoués sur `lanceur_v7`, `instance_v7`, `lecture_v7`, plus les essais de la relecture des lignes
touchées v5 → v6 (`a46dc4fb…`) : C-1 à C-4,
E-1 (M-1 éprouvé par comportement : deux écritures d'état demandées, la seconde dans `_finir`), E-2 (journal transféré
coupé : clé dans `valider`, `lire` et l'état écrit par `tours --ecrire-etat`), et les sondes P1 à P5 du relecteur
(`test_sondes_r2_v6.py`, `7f12d19e…`), inversées. Texte d'origine des essais v6 : essais de la v5 rejoués sur la v6,
plus M-1 et M-2 (relecture `22879993…`). Texte d origine de la v5 :
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
from controle_ia.temoin_bailey import instance_v16 as inst
from controle_ia.temoin_bailey import lanceur_v21 as la
from controle_ia.temoin_bailey import lecture_v8 as lc

import test_temoin_bailey_condition6_v3 as T3  # aides de la v3, inchangées
import test_temoin_bailey_condition6_v4 as T4  # aides de la v4 (données, analyse des imports), inchangées

DEPOT = T4.DEPOT
GO_ID = T4.GO_ID
TEXTE_GO_MAIN = T4.TEXTE_GO_MAIN
HORLOGE = T4.HORLOGE
etat_x, horloge_pas = T4.etat_x, T4.horloge_pas
AUTO_ARRET_OK = ({"commande": "auto-arret", "disponible": True, "verifications": {}, "cause": None}, 0)


def reponses(**kw):
    """Réponses de la v4, plus l'étape v10 « auto-arret » (disponible par défaut)."""
    return {"auto-arret": AUTO_ARRET_OK, **T4.reponses(**kw)}


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
        m = re.search(r"instance_v16 tours --travail /root/x/([\w-]+)", commande)
        if m:
            a = shlex.split(commande.split("instance_v16 ", 1)[1])
            if "--ecrire-etat" in a:
                self.ecrits.append((m.group(1), a[a.index("--cause") + 1]))
                self.appels.append(f"tours:{m.group(1)}")
            t = self.tours.get(m.group(1))
            return (0, "ETAT " + json.dumps({"etat_execution": "reconstitué", **t}) + "\n") if t is not None \
                else (1, "")
        if "instance_v16 empreintes" in commande:
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
    assert f.lance == ["amorce", "auto-arret", "mise-en-place", "controle-juge", "pilote", "regle", "principal"]
    assert "arret" not in bilan and f.detruites == ["77"] and bilan["detruite"] is True
    assert f.ecrits == [] and not any(a.startswith("arret:") for a in f.appels)  # rien d'arrêté, rien de reconstitué
    assert f.etiquettes == [bilan["etiquette"]] and bilan["etiquette"].startswith(la.PREFIXE_ETIQUETTE)
    ordre = [json.loads(l) for l in (c.sortie / "conduite-v5.jsonl").read_text().splitlines() if '"ordre"' in l]
    assert ordre[0]["ordre"]["etiquette"] == bilan["etiquette"]
    scellement.verifier(c.sortie / "bilan-conduite-v5.json")
    assert all("instance_v4" not in x and "instance_v6" not in x for x in f.commandes)
    assert not any("instance_v7" in x or "instance_v8" in x for x in f.commandes)
    assert "/root/amorce-v5.sh" in f.envoyes and any("instance_v16" in x for x in f.commandes)
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

    return {"amorce": lambda f: ({"commande": "amorce", "finie": True}, 0), "auto-arret": lambda f: AUTO_ARRET_OK,
            "mise-en-place": mep,
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
    assert "src/controle_ia/temoin_bailey/instance_v16.py" in la.CHEMINS_ARCHIVE
    assert "src/controle_ia/temoin_bailey/lecture_v8.py" in la.CHEMINS_ARCHIVE
    assert not any(p.endswith(("instance_v5.py", "instance_v6.py", "instance_v7.py", "lanceur_v6.py", "lanceur_v7.py",
                               "lanceur_v9.py", "lecture_v3.py", "lecture_v5.py", "lecture_v6.py", "lecture_v7.py",
                               "instance_v8.py", "lanceur_v10.py", "instance_v10.py", "lanceur_v11.py",
                               "instance_v11.py"))
                   for p in la.CHEMINS_ARCHIVE)
    assert la.INSTANCE_MODULE == "controle_ia.temoin_bailey.instance_v16"


def test_v13_aucun_module_ancien_dans_le_code_execute():
    """v13 : aucun nom de module v5 à v11 d'instance, v5 à v12 de lanceur, ni v5 à v7 de lecture, dans le code des
    modules exécutés (imports, chaînes, commande du veilleur ; les docstrings, qui font l'historique, exceptées)."""
    import ast
    motif = (r"temoin_bailey\.(instance_v([5-9]|1[01])|lanceur_v([5-9]|1[012]))\b|"
             r"(instance_v([5-9]|1[01])|lanceur_v([5-9]|1[012]))(\.py)?\b|"
             r"lecture_v[567]\b|temoin_bailey\.lecture_v[567]\b")
    for nom in ("lecture_v8.py", "instance_v16.py", "lanceur_v21.py"):
        arbre = ast.parse((DEPOT / "src/controle_ia/temoin_bailey" / nom).read_text(encoding="utf-8"))
        docs = {id(b.body[0].value) for b in ast.walk(arbre)  # docstrings (module, classes, fonctions) exceptées
                if isinstance(b, (ast.Module, ast.ClassDef, ast.FunctionDef)) and b.body
                and isinstance(b.body[0], ast.Expr) and isinstance(b.body[0].value, ast.Constant)}
        for n in ast.walk(arbre):
            if isinstance(n, ast.ImportFrom):
                assert not re.search(r"instance_v([5-9]|1[01])$|lanceur_v([5-9]|1[012])$|lecture_v[567]$",
                                     n.module or ""), (nom, n.module)
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs:
                assert not re.search(motif, n.value), (nom, n.value[:80])
    source = (DEPOT / "src/controle_ia/temoin_bailey/lanceur_v21.py").read_text(encoding="utf-8")
    assert 'VEILLEUR_MODULE = "controle_ia.temoin_bailey.lanceur_v21"' in source
    assert '[sys.executable, "-m", VEILLEUR_MODULE, "veilleur",' in source
    assert '[sys.executable, "-m", VEILLEUR_MODULE, "veilleur-arret",' in source


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
    assert "arret" not in c.conduire() and f.lance[4:6] == ["pilote", "pilote-reprise"]  # v10 : « auto-arret » avant
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


# --- relecture des lignes touchées v5 → v6 (`a46dc4fb…`) : C-1 à C-4, E-1, E-2, sondes P1 à P5 inversées ----------

from controle_ia.gardes import GardeArret  # noqa: E402


def _coupee_multioctet(tour: int) -> bytes:
    """Ligne « tombée » du journal des gardes, coupée entre les deux octets du premier « é » (C-1)."""
    ligne = json.dumps({"etat": "tombée", "garde": "suite des étiquettes", "message": "garde « suite des étiquettes » "
                        "tombée", "tour": tour}, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return ligne[:ligne.index("é".encode()) + 1]


def _ajouter_octets(chemin: Path, octets: bytes) -> None:
    with open(chemin, "ab") as f:
        f.write(octets)


def _dernier_tour(x: Path) -> int:
    return max(t["index"] for t in lc.tours_journal(x, []))


def test_M2_derniere_ligne_coupee_ignoree_et_signalee(tmp_path):
    p = tmp_path / "j.jsonl"
    p.write_text('{"a": 1}\n{"a": 2}\n{"a": ', encoding="utf-8")  # écriture coupée, sans fin de ligne
    signal = []
    assert lc.lire_jsonl(p, signal) == [{"a": 1}, {"a": 2}]
    assert signal == [str(p)]
    with pytest.raises(GardeArret, match="sans liste de signalement"):  # C-4 : jamais ignorée sans être dite
        lc.lire_jsonl(p)


def test_M2_ligne_illisible_au_milieu_ou_finie_leve(tmp_path):
    p = tmp_path / "j.jsonl"
    p.write_text('{"a": 1}\n{"a": \n{"a": 3}\n', encoding="utf-8")
    with pytest.raises(GardeArret, match="illisible"):
        lc.lire_jsonl(p, [])
    p.write_text('{"a": 1}\n{"a": \n', encoding="utf-8")  # dernière ligne illisible mais finie : pas une coupure
    with pytest.raises(GardeArret, match="illisible"):
        lc.lire_jsonl(p, [])
    p.write_text('{"a": 1}\n{"a": 2}', encoding="utf-8")  # ligne entière sans fin de ligne : lue telle quelle
    signal = []
    assert lc.lire_jsonl(p, signal) == [{"a": 1}, {"a": 2}] and signal == []
    p.write_text('{"a": 1}\n', encoding="utf-8")
    assert lc.lire_jsonl(p, signal) == [{"a": 1}] and signal == []


def test_P1_inverse_coupure_dans_un_caractere_multioctet(tmp_path):
    """Sonde P1 inversée (C-1) : coupure entre les deux octets d'un « é » : ignorée et signalée, jamais
    `UnicodeDecodeError` ; un octet invalide ailleurs que sur la dernière ligne coupée : `GardeArret`."""
    p = tmp_path / "gardes-v3.jsonl"
    complet = '{"etat": "passée", "garde": "par tour"}\n'.encode()
    p.write_bytes(complet + _coupee_multioctet(3))
    signal = []
    assert lc.lire_jsonl(p, signal) == [{"etat": "passée", "garde": "par tour"}] and signal == [str(p)]
    p.write_bytes(_coupee_multioctet(3) + b"\n" + complet)  # même coupure, au milieu : pas une coupure de fin
    with pytest.raises(GardeArret, match="illisible"):
        lc.lire_jsonl(p, [])
    p.write_bytes(complet + _coupee_multioctet(3) + b"\n")  # dernière, mais finie
    with pytest.raises(GardeArret, match="illisible"):
        lc.lire_jsonl(p, [])


def test_P2_inverse_aucun_etat_global_resultat_rendu_inchange(tmp_path):
    """Sonde P2 inversée (C-4) : plus de liste de module ; un résultat rendu par `valider` ne change ni par `lire`, ni
    par un second `valider`."""
    assert not hasattr(lc, "LIGNES_TRONQUEES")
    m = _manifeste_regle(tmp_path, 30)

    def couper(x):
        _ajouter_octets(x / cv.JOURNAL_TECHNIQUE, b'{"type": "evaluation", "tour": 21, "eti')
        _reconstituer(m)(x)
    r1 = lc.valider(T3.poste_local(tmp_path / "a", 21, k_regle=30, modifier_principal=couper))
    avant = list(r1["lignes_tronquees_ignorees"])
    assert avant and r1["etat"] is None
    res = lc.lire(r1, an.graines()["reechantillonnage"])
    assert res["lignes_tronquees_ignorees"] is not r1["lignes_tronquees_ignorees"]
    r2 = lc.valider(T3.poste_local(tmp_path / "b", 21))
    assert r1["lignes_tronquees_ignorees"] == avant and r2["lignes_tronquees_ignorees"] == []
    assert lc.valider(tmp_path / "vide")["lignes_tronquees_ignorees"] == [] and r1["lignes_tronquees_ignorees"] == avant


def test_P3_inverse_lire_rapporte_les_lignes_tronquees():
    """Sonde P3 inversée (C-2) : `lire` rend les lignes coupées de `valider`, au retour anticipé ; sans la clé (validité
    d'une version antérieure), `GardeArret`."""
    v = {"etat": "pas de verdict", "k_prime": 0, "interruptions": [], "lignes_tronquees_ignorees": ["j"]}
    r = lc.lire(v, 0)
    assert r["lignes_tronquees_ignorees"] == ["j"]
    r["lignes_tronquees_ignorees"].append("x")
    assert v["lignes_tronquees_ignorees"] == ["j"]  # copie : `validite_` jamais modifié
    with pytest.raises(GardeArret, match="signalement"):
        lc.lire({"etat": "pas de verdict", "k_prime": 0, "interruptions": []}, 0)


def test_P4_inverse_signalement_par_chemin_sans_doublon(tmp_path):
    """Sonde P4 inversée (C-2) : le signalement porte le chemin (qui nomme l'exécution) ; relu deux fois, compté une."""
    for n in ("pilote", "principal"):
        (tmp_path / n).mkdir()
        (tmp_path / n / "j.jsonl").write_text('{"a": 1}\n{"a', encoding="utf-8")
    signal = []
    lc.lire_jsonl(tmp_path / "pilote" / "j.jsonl", signal)
    lc.lire_jsonl(tmp_path / "principal" / "j.jsonl", signal)
    lc.lire_jsonl(tmp_path / "pilote" / "j.jsonl", signal)
    assert signal == [str(tmp_path / "pilote" / "j.jsonl"), str(tmp_path / "principal" / "j.jsonl")]


def test_P5_inverse_etat_reconstitue_sur_l_instance_signale(tmp_path):
    """Sonde P5 inversée (C-2, C-3) : `reconstituer_etat`, `tours` et `tours --ecrire-etat` écrivent les lignes
    coupées dans l'état et dans la ligne `ETAT` ; la ligne « tom… » coupée retire le dernier tour présent."""
    m = _manifeste_regle(tmp_path, 30)
    x, _ = T3.execution_factice(tmp_path, "principal", 5, {"k": 30})
    (x / cv.ETAT_EXECUTION).unlink()
    assert lc.tours_complets_instance(x, [])[0] == 5 and _dernier_tour(x) == 4
    _ajouter_octets(x / cv.JOURNAL_GARDES, b'{"etat": "tom')
    attendu = [str(x / cv.JOURNAL_GARDES)]
    out = io.StringIO()
    with redirect_stdout(out):
        assert inst.main(["tours", "--travail", str(x)]) == 0
    t = la.lire_etat(out.getvalue())
    assert t["lignes_tronquees_ignorees"] == attendu and t["tours_complets"] == 4
    out = io.StringIO()
    with redirect_stdout(out):
        assert inst.main(["tours", "--ecrire-etat", "--travail", str(x), "--phase", "principal", "--manifeste",
                          str(m), "--cause", "coupure de l'hôte"]) == 0
    t = la.lire_etat(out.getvalue())
    assert t["etat_execution"] == "reconstitué" and t["lignes_tronquees_ignorees"] == attendu
    e = json.loads((x / cv.ETAT_EXECUTION).read_text())
    assert e["lignes_tronquees_ignorees"] == attendu and e["tours_complets"] == 4
    r = inst.reconstituer_etat(x, json.loads(m.read_text()), "principal", "coupure de l'hôte")
    assert r["etat_execution"] == "déjà présent" and r["lignes_tronquees_ignorees"] == attendu


def test_C4_instance_liste_propre_a_chaque_appel(tmp_path):
    """C-4 côté instance : rien ne s'accumule d'un appel à l'autre dans le processus."""
    m = json.loads(_manifeste_regle(tmp_path, 30).read_text())
    x, _ = T3.execution_factice(tmp_path / "a", "principal", 4, {"k": 30})
    y, _ = T3.execution_factice(tmp_path / "b", "principal", 4, {"k": 30})
    for d in (x, y):
        (d / cv.ETAT_EXECUTION).unlink()
    _ajouter_octets(x / cv.JOURNAL_TECHNIQUE, b'{"type": "pas", "tou')
    assert inst.reconstituer_etat(x, m, "principal", "dépense")["lignes_tronquees_ignorees"] == \
        [str(x / cv.JOURNAL_TECHNIQUE)]
    assert inst.reconstituer_etat(y, m, "principal", "dépense")["lignes_tronquees_ignorees"] == []


def test_C3_suite_des_etiquettes_coupee_apres_MARK_e_K_prime_e(tmp_path):
    """C-3 : garde « suite des étiquettes » tombée au tour e (avant l'incrément), après la ligne « MARK » de e. Ligne
    entière : K′ = e. Ligne coupée (au milieu d'un « é ») : K′ = e aussi, jamais e + 1 ; signalée. v8 (A-1) : une
    ligne coupée des gardes du lanceur se lit comme une ligne « tombée » entière de ce journal : K′ = 0, tous les tours
    marqués `ligne_de_garde_coupee`. Coupée dans un autre journal : aucun tour retiré ni ajouté."""
    e = 5
    x, _ = T3.execution_factice(tmp_path, "principal", e + 1, {"k": 30})
    assert lc.k_prime(lc.tours_journal(x, [])) == e + 1 and _dernier_tour(x) == e
    for nom, suite in (("entiere", None), ("coupee", "gardes"), ("lanceur", "lanceur"), ("autre", "technique")):
        y = tmp_path / nom
        shutil.copytree(x, y)
        if suite is None:
            entiere = json.dumps({"etat": "tombée", "garde": "suite des étiquettes", "tour": e}, ensure_ascii=False)
            _ajouter_octets(y / cv.JOURNAL_GARDES, entiere.encode("utf-8") + b"\n")
        elif suite == "gardes":
            _ajouter_octets(y / cv.JOURNAL_GARDES, _coupee_multioctet(e))
        elif suite == "lanceur":
            _ajouter_octets(y / cv.GARDES_LANCEUR, b'{"etat": "tomb')
        else:
            _ajouter_octets(y / cv.JOURNAL_TECHNIQUE, b'{"type": "fin_de_tour", "tour": 6')
        signal = []
        tours = lc.tours_journal(y, signal)
        attendu = {"technique": e + 1, "lanceur": 0}.get(suite, e)
        assert lc.k_prime(tours) == attendu, nom
        assert any(t["ligne_de_garde_coupee"] for t in tours) is (suite in ("gardes", "lanceur")), nom
        assert all(t["ligne_de_garde_coupee"] for t in tours) is (suite == "lanceur"), nom
        assert (signal == []) is (suite is None), nom


def test_E1_M1_par_comportement_deux_ecritures_d_etat_la_seconde_dans_finir(tmp_path, monkeypatch):
    """E-1 (sonde M-1 du relecteur v5, inversée) : exécution principale morte ; la première `tours --ecrire-etat`
    échoue ; la reconstitution est retentée une seconde fois, dans `_finir`, avant les empreintes ; pas de relance."""
    c, f, _ = conduite(tmp_path, monkeypatch, reponses(principal="mort"))
    f.tours["principal"] = None  # `tours` rend (1, "") : échec, les deux fois
    finir = c._finir
    vus = {}

    def espion(bilan):
        vus["ecrits_avant_finir"] = list(f.ecrits)
        return finir(bilan)
    c._finir = espion
    bilan = c.conduire()
    assert vus["ecrits_avant_finir"] == [("principal", "coupure de l'hôte")]
    assert f.ecrits == [("principal", "coupure de l'hôte"), ("principal", "coupure de l'hôte")]
    a = f.appels
    i2 = [i for i, x in enumerate(a) if x == "tours:principal"][1]
    assert i2 < a.index("empreintes") < a.index("detruire")
    assert bilan["etats_reconstitues"] == {"principal": None}  # échec consigné, jamais levé
    assert "principal-relance" not in f.lance and bilan["arret"].startswith("exécution principale morte sans état")


def _gardes_coupees_puis(m=None):
    """Journal des gardes coupé au milieu d'un « é » (dernière ligne « tombée »), puis, si `m`, état reconstitué
    sur l'instance (`tours --ecrire-etat`)."""
    def f(x: Path) -> None:
        _ajouter_octets(x / cv.JOURNAL_GARDES, _coupee_multioctet(_dernier_tour(x)))
        if m is not None:
            _reconstituer(m)(x)
    return f


def test_E2_journal_transfere_coupe_cle_dans_valider_lire_et_etat(tmp_path):
    """E-2 (C-2, C-3) : run principal coupé après 21 tours marqués (K = 30), dernière ligne du journal des gardes
    coupée : l'état écrit par `tours --ecrire-etat` la porte (chemin sur l'instance) ; `valider` et `lire` la nomment
    avec son exécution et son transfert ; le dernier tour présent est retiré : K′ = 20, jamais 21."""
    m = _manifeste_regle(tmp_path, 30)
    racine = T3.poste_local(tmp_path, 21, k_regle=30, modifier_principal=_gardes_coupees_puis(m))
    d = racine / "principal" / "transfert-1"
    e = json.loads((d / cv.ETAT_EXECUTION).read_text())
    (sur_instance,) = e["lignes_tronquees_ignorees"]
    assert sur_instance.endswith("w-principal/" + cv.JOURNAL_GARDES) and e["tours_complets"] == 20
    v = lc.valider(racine)
    assert v["etat"] is None and v["k_prime"] == 20 and v["fin_de_run"] is True, v["details"]
    transfere = str(d / cv.JOURNAL_GARDES)
    assert transfere in v["lignes_tronquees_ignorees"]
    assert f"{sur_instance} (état d'exécution « principal », écrit sur l'instance)" in v["lignes_tronquees_ignorees"]
    assert len(v["lignes_tronquees_ignorees"]) == 2  # sans doublon, bien que le journal soit lu plusieurs fois
    (i,) = v["interruptions"]
    assert i["lignes_tronquees_ignorees"] == [sur_instance]
    res = lc.lire(v, an.graines()["reechantillonnage"])
    assert res["lignes_tronquees_ignorees"] == v["lignes_tronquees_ignorees"]
    assert res["verdict"].startswith("Effet reproduit sur le banc des auteurs, au régime réduit (K = 20)")


def test_E2_premiere_execution_coupee_rapportee_avec_la_relance(tmp_path):
    """Relance : la première exécution, dont seuls les états sont lus, rapporte sa ligne coupée par son état ; sans
    état transféré, par l'état reconstitué à la lecture."""
    m = _manifeste_regle(tmp_path, 30)
    racine = T3.poste_local(tmp_path / "a", 3, k_regle=30, modifier_principal=_gardes_coupees_puis(m),
                            relance=(21, {}))
    v = lc.valider(racine)
    assert v["etat"] is None and v["k_prime"] == 21
    (x,) = v["lignes_tronquees_ignorees"]
    assert "(état d'exécution « principal », écrit sur l'instance)" in x
    assert v["interruptions"][0]["lignes_tronquees_ignorees"] and v["interruptions"][0]["k_prime"] == 2
    assert lc.lire(v, an.graines()["reechantillonnage"])["lignes_tronquees_ignorees"] == [x]

    def sans_etat(y):
        _gardes_coupees_puis()(y)
        (y / cv.ETAT_EXECUTION).unlink()
    racine = T3.poste_local(tmp_path / "b", 3, k_regle=30, modifier_principal=sans_etat, relance=(21, {}))
    v = lc.valider(racine)
    assert v["lignes_tronquees_ignorees"] == [str(racine / "principal" / "transfert-1" / cv.JOURNAL_GARDES)]
    assert v["interruptions"][0]["reconstitue"] == "à la lecture" and v["interruptions"][0]["k_prime"] == 2


def test_E2_bout_en_bout_conduite_morte_journal_coupe(tmp_path, monkeypatch):
    """De bout en bout : exécution morte après 21 tours, journal des gardes coupé ; la ligne `ETAT` de `tours` porte
    la ligne coupée jusqu'au bilan ; la lecture la rapporte (état et transfert) ; K′ = 20, pas de relance."""
    def principal(f):
        x = f.execution("principal", 21, {"k": 30})
        (x / cv.ETAT_EXECUTION).unlink()
        _ajouter_octets(x / cv.JOURNAL_GARDES, _coupee_multioctet(_dernier_tour(x)))
        return "mort"
    c, f, _ = conduite_locale(tmp_path, monkeypatch, scenario(30, principal))
    bilan = c.conduire()
    p0 = bilan["principal"][0]
    assert p0["tours_complets"] == 20 and "principal-relance" not in f.lance
    assert p0["lignes_tronquees_ignorees"] == [str(f.base / "root/x/principal" / cv.JOURNAL_GARDES)]
    v = lc.valider(c.sortie)
    assert v["k_prime"] == 20 and len(v["lignes_tronquees_ignorees"]) == 2, v
    assert lc.lire(v, an.graines()["reechantillonnage"])["verdict"].startswith(
        "Effet reproduit sur le banc des auteurs, au régime réduit (K = 20)")


# --- v8 : décision de Lazar du 10 novembre 2026, points A-1 et A-2 (`5831e98c…`) ; sondes Q1, Q2 inversées ----------

def _ligne_garde(nom: str, tour: int, etat: str = "tombée", ascii_: bool = False) -> bytes:
    """Ligne de garde telle que l'écrit le journaliseur (`_ecrire` : clés triées)."""
    return json.dumps({"etat": etat, "garde": nom, "message": f"garde « {nom} » {etat}", "tour": tour},
                      ensure_ascii=ascii_, sort_keys=True).encode("utf-8")


def _prefixe_nomme(ligne: bytes) -> bytes:
    """Préfixe coupé après le nom de la garde (guillemet fermant compris)."""
    return ligne[:ligne.index(b'"message"')]


def _prefixe_sans_nom(ligne: bytes) -> bytes:
    """Préfixe coupé au milieu du nom de la garde : garde inconnue."""
    return ligne[:ligne.index(b'"garde": "') + 14]


def test_Q1_inverse_lanceur_coupe_K_prime_0_comme_la_ligne_entiere(tmp_path):
    """Sonde Q1 inversée (A-1) : gardes du lanceur, ligne « configuration effective » tombée : entière → K′ = 0 ;
    coupée (à quelque octet que ce soit) → K′ = 0 aussi, signalée ; jamais e tours de plus que l'intact."""
    e = 5
    x, _ = T3.execution_factice(tmp_path, "principal", e + 1, {"k": 30})
    ligne = json.dumps({"etat": "tombée", "garde": "configuration effective", "tour": -1},
                       ensure_ascii=False, sort_keys=True).encode()
    a = tmp_path / "entiere"
    shutil.copytree(x, a)
    _ajouter_octets(a / cv.GARDES_LANCEUR, ligne + b"\n")
    assert lc.k_prime(lc.tours_journal(a, [])) == 0
    for n in (1, 8, 20, len(ligne) - 1):
        b = tmp_path / f"coupee-{n}"
        shutil.copytree(x, b)
        _ajouter_octets(b / cv.GARDES_LANCEUR, ligne[:n])
        signal = []
        tours = lc.tours_journal(b, signal)
        assert lc.k_prime(tours) == 0 and all(t["garde_tombee"] and t["ligne_de_garde_coupee"] for t in tours), n
        assert signal == [str(b / cv.GARDES_LANCEUR)], n
        assert lc.tours_complets_instance(b, [])[0] == 0


def test_Q2_inverse_sonde_orientee_coupee_au_pilote_jamais_une_chute(tmp_path):
    """Sonde Q2 inversée (A-2) : « sonde orientée » tombée au tour 0 du pilote, ligne coupée après son nom : la garde
    est nommée (`gardes_tombees`), l'issue est « sonde orientée » (arrêt, non interprétable), jamais « chute »."""
    ligne = json.dumps({"etat": "tombée", "garde": "sonde orientée", "tour": 0},
                       ensure_ascii=False, sort_keys=True).encode()
    coupe = ligne[:ligne.index(b'"tour"')]
    assert "sonde orientée".encode() in coupe
    d = tmp_path / "pilote"
    (d / "journal").mkdir(parents=True)
    (d / cv.JOURNAL_GARDES).write_bytes(coupe)
    (d / cv.GARDES_LANCEUR).write_bytes(b"")
    signal = []
    g = lc.gardes_tombees(d, signal)
    assert g == ["sonde orientée", lc.LIGNE_DE_GARDE_COUPEE] and signal == [str(d / cv.JOURNAL_GARDES)]
    e = {"code_retour": 1, "cause_arret": "coupure de l'hôte", "gardes_tombees": g, "tours_marques": 0}
    assert lc.issue_pilote(e) == "sonde orientée"


def test_A2_garde_de_ligne_coupee_seul_un_nom_entier_d_une_garde_tombee():
    """A-2 : le nom n'est lu que s'il est entier, guillemet fermant compris, dans une ligne « tombée » ; écriture
    UTF-8 ou échappée ; coupure au milieu d'un caractère multioctet après le nom tolérée."""
    for ascii_ in (False, True):
        ligne = _ligne_garde("sonde orientée", 0, ascii_=ascii_)
        assert lc.garde_de_ligne_coupee(_prefixe_nomme(ligne)) == "sonde orientée"
        assert lc.garde_de_ligne_coupee(_prefixe_sans_nom(ligne)) is None
        assert lc.garde_de_ligne_coupee(ligne[:ligne.index(b"orient") + 8]) is None  # nom sans guillemet fermant
        assert lc.garde_de_ligne_coupee(_prefixe_nomme(_ligne_garde("sonde orientée", 0, "passée", ascii_))) is None
    ligne = _ligne_garde("sonde orientée", 0)
    i = ligne.index("« ".encode())
    assert lc.garde_de_ligne_coupee(ligne[:i + 1]) == "sonde orientée"  # coupée dans « « » (2 octets), après le nom
    assert lc.garde_de_ligne_coupee(b"") is None and lc.garde_de_ligne_coupee(b'{"etat": "tom') is None


def _pilote_etat(**kw) -> dict:
    e = {"code_retour": 1, "cause_arret": "coupure de l'hôte", "gardes_tombees": [], "tours_marques": 0}
    e.update(kw)
    return e


def test_A2_issue_pilote_ligne_coupee_jamais_plus_favorable():
    """A-2 : une ligne de garde coupée (nommée, ou seulement signalée par son chemin) donne « ligne de garde coupée » :
    jamais « chute » (reprise), « arrêt » ni « finie » ; « sonde orientée » garde la priorité. Sans ligne coupée, les
    issues de la v7 sont inchangées."""
    J = "/root/x/pilote/" + cv.JOURNAL_GARDES
    L = "/root/x/pilote/" + cv.GARDES_LANCEUR
    assert lc.issue_pilote(_pilote_etat(gardes_tombees=[lc.LIGNE_DE_GARDE_COUPEE])) == lc.ISSUE_LIGNE_COUPEE
    assert lc.issue_pilote(_pilote_etat(lignes_tronquees_ignorees=[J])) == lc.ISSUE_LIGNE_COUPEE
    assert lc.issue_pilote(_pilote_etat(lignes_tronquees_ignorees=[L])) == lc.ISSUE_LIGNE_COUPEE
    assert lc.issue_pilote(_pilote_etat(cause_arret="dépense", gardes_tombees=[lc.LIGNE_DE_GARDE_COUPEE])) \
        == lc.ISSUE_LIGNE_COUPEE
    fini = dict(code_retour=0, cause_arret=None, tours_marques=3)
    assert lc.issue_pilote(_pilote_etat(**fini, lignes_tronquees_ignorees=[J])) == lc.ISSUE_LIGNE_COUPEE
    assert lc.issue_pilote(_pilote_etat(gardes_tombees=["sonde orientée", lc.LIGNE_DE_GARDE_COUPEE])) \
        == "sonde orientée"
    # sans ligne de garde coupée : v7 inchangée (un journal technique coupé n'est pas un journal de gardes)
    assert lc.issue_pilote(_pilote_etat(lignes_tronquees_ignorees=["/root/x/pilote/" + cv.JOURNAL_TECHNIQUE])) \
        == "chute"
    assert lc.issue_pilote(_pilote_etat()) == "chute"
    assert lc.issue_pilote(_pilote_etat(cause_arret="dépense")) == "arrêt"
    assert lc.issue_pilote(_pilote_etat(**fini, lignes_tronquees_ignorees=[])) == "finie"


def test_A2_gardes_tombees_nomme_la_ligne_coupee_des_deux_journaux(tmp_path):
    x, _ = T3.execution_factice(tmp_path, "pilote", 3, {"k": 3})
    assert lc.gardes_tombees(x, []) == []
    for rel in (cv.JOURNAL_GARDES, cv.GARDES_LANCEUR):
        y = tmp_path / Path(rel).name
        shutil.copytree(x, y)
        _ajouter_octets(y / rel, _prefixe_sans_nom(_ligne_garde("par tour", 2)))
        signal = []
        assert lc.gardes_tombees(y, signal) == [lc.LIGNE_DE_GARDE_COUPEE] and signal == [str(y / rel)]
        assert lc.gardes_des_lignes_coupees(y, []) == [lc.LIGNE_DE_GARDE_COUPEE]
    assert lc.gardes_des_lignes_coupees(x, []) == []


def _pilote_coupe(prefixe: bytes, sans_etat=False):
    def f(x: Path) -> None:
        _ajouter_octets(x / cv.JOURNAL_GARDES, prefixe)
        if sans_etat:
            (x / cv.ETAT_EXECUTION).unlink()
    return f


def _remplacer_pilote(racine: Path, tmp_path: Path, nom: str, modifier, etat: dict) -> None:
    y, _ = T3.execution_factice(tmp_path / f"fab-{nom}", nom, 3, {"k": 3, "graine": an.GRAINE_PILOTE, **etat},
                                modifier=modifier)
    if (racine / nom).exists():
        shutil.rmtree(racine / nom)
    T3.etape(racine, nom, y)


def test_A2_valider_relit_les_gardes_transferees_du_pilote(tmp_path):
    """A-2, lecture : l'état transféré du pilote ne nomme pas la ligne coupée (état d'une version antérieure, ou
    reconstitué à la lecture) ; `valider` relit les journaux de gardes transférés et rend « pas de run principal ;
    ligne de garde coupée au pilote (garde inconnue) ; nœud », jamais une reprise lue comme permise ni un verdict."""
    coupe = _prefixe_sans_nom(_ligne_garde("par tour", 2))
    for cas in ("etat", "sans_etat"):
        racine = T3.poste_local(tmp_path / cas, 21)
        _remplacer_pilote(racine, tmp_path / cas, "pilote", _pilote_coupe(coupe, cas == "sans_etat"),
                          {"code_retour": 1, "cause_arret": "coupure de l'hôte", "tours_marques": 2,
                           "tours_complets": 2})
        v = lc.valider(racine)
        assert v["etat"] == lc.ETAT_LIGNE_COUPEE_PILOTE, (cas, v["details"])
        assert v["details"]["pilote"] == [lc.ISSUE_LIGNE_COUPEE]
        assert str(racine / "pilote" / "transfert-1" / cv.JOURNAL_GARDES) in v["lignes_tronquees_ignorees"]
        assert any(i["role"] == "pilote, ligne de garde coupée" for i in v["interruptions"])
        assert lc.lire(v, 0)["verdict"] == lc.ETAT_LIGNE_COUPEE_PILOTE
    # la reprise faite après une première chute, coupée elle aussi : nœud, jamais « seconde chute » ni verdict
    racine = T3.poste_local(tmp_path / "reprise", 21, pilote={"code_retour": 1, "gardes_tombees": ["par tour"]})
    _remplacer_pilote(racine, tmp_path / "reprise", "pilote-reprise", _pilote_coupe(coupe), {"code_retour": 1})
    v = lc.valider(racine)
    assert v["details"]["pilote"] == ["chute", lc.ISSUE_LIGNE_COUPEE] and v["etat"] == lc.ETAT_LIGNE_COUPEE_PILOTE
    # nom lisible « sonde orientée » : non interprétable (texte l. 366)
    racine = T3.poste_local(tmp_path / "sonde", 21)
    _remplacer_pilote(racine, tmp_path / "sonde", "pilote", _pilote_coupe(_prefixe_nomme(
        _ligne_garde("sonde orientée", 0))), {"code_retour": 1, "cause_arret": "coupure de l'hôte"})
    v = lc.valider(racine)
    assert v["details"]["pilote"] == ["sonde orientée"]
    assert v["etat"] == "Non interprétable (garde « sonde orientée »)."


def test_A2_cas_sain_et_principal_coupe_inchanges(tmp_path):
    """Témoins : le pilote sain reste « finie » et le verdict est rendu ; une ligne coupée du principal ne touche pas
    l'issue du pilote (C-3 inchangé : K′ = 20)."""
    v = lc.valider(T3.poste_local(tmp_path / "sain", 21))
    assert v["etat"] is None and v["details"]["pilote"] == ["finie"] and "lignes_de_garde_coupees_pilote" not in \
        v["details"]
    m = _manifeste_regle(tmp_path, 30)
    v = lc.valider(T3.poste_local(tmp_path / "p", 21, k_regle=30, modifier_principal=_gardes_coupees_puis(m)))
    assert v["etat"] is None and v["k_prime"] == 20 and v["details"]["pilote"] == ["finie"]


def test_A2_conduite_pilote_ligne_coupee_arret_sans_reprise(tmp_path, monkeypatch):
    """A-2, conduite (unitaire) : l'état du pilote nomme la ligne coupée, ou seulement son chemin, ou la ligne `ETAT`
    de `tours` d'un pilote mort la porte : arrêt, ni reprise, ni règle, ni run principal ; instance détruite."""
    J = "/root/x/pilote/" + cv.JOURNAL_GARDES
    cas = {
        "nommee": reponses(pilote=etat_x("pilote", code_retour=1, cause_arret="coupure de l'hôte",
                                         gardes_tombees=[lc.LIGNE_DE_GARDE_COUPEE], tours_complets=2,
                                         lignes_tronquees_ignorees=[J])),
        "chemin": reponses(pilote=etat_x("pilote", code_retour=1, gardes_tombees=[], tours_complets=2,
                                         lignes_tronquees_ignorees=[J])),
        "morte": reponses(pilote="mort"),
    }
    for nom, reps in cas.items():
        c, f, _ = conduite(tmp_path / nom, monkeypatch, reps)
        if nom == "morte":
            f.tours["pilote"] = {"tours_complets": 2, "journal_absent": None,
                                 "gardes_tombees": [lc.LIGNE_DE_GARDE_COUPEE], "lignes_tronquees_ignorees": [J]}
        bilan = c.conduire()
        assert f.lance == ["amorce", "auto-arret", "mise-en-place", "controle-juge", "pilote"], nom
        assert bilan["arret"] == "pas de run principal ; ligne de garde coupée au pilote (garde inconnue) ; nœud", nom
        assert f.detruites == ["77"] and "regle" not in bilan and "principal" not in bilan, nom
        assert bilan["pilote"][0]["lignes_tronquees_ignorees"] == [J], nom
    # témoin : pilote mort sans ligne coupée → une reprise (v7 inchangée)
    c, f, _ = conduite(tmp_path / "temoin", monkeypatch, reponses(pilote="mort"))
    f.tours["pilote"] = {"tours_complets": 0, "journal_absent": None, "gardes_tombees": [],
                         "lignes_tronquees_ignorees": []}
    assert "arret" not in c.conduire() and f.lance[4:6] == ["pilote", "pilote-reprise"]  # v10 : « auto-arret » avant


def test_A2_conduite_reprise_coupee_arret_et_non_seconde_chute(tmp_path, monkeypatch):
    J = "/root/x/pilote-reprise/" + cv.JOURNAL_GARDES
    c, f, _ = conduite(tmp_path, monkeypatch, reponses(
        pilote=etat_x("pilote", code_retour=1, gardes_tombees=["par tour"]),
        **{"pilote-reprise": etat_x("pilote-reprise", code_retour=1, gardes_tombees=[lc.LIGNE_DE_GARDE_COUPEE],
                                    lignes_tronquees_ignorees=[J])}))
    bilan = c.conduire()
    assert f.lance[4:] == ["pilote", "pilote-reprise"]  # v10 : « auto-arret » avant
    assert bilan["arret"].startswith("pas de run principal ; ligne de garde coupée au pilote")


def _scenario_pilote_mort_coupe(prefixe: bytes):
    scen = scenario(21, principal_fini(21))

    def pilote(f):
        x = f.execution("pilote", 3, {"k": 3, "graine": an.GRAINE_PILOTE,
                                      "durees": {"0": T_REGLE, "1": T_REGLE, "2": T_REGLE}})
        (x / cv.ETAT_EXECUTION).unlink()
        _ajouter_octets(x / cv.JOURNAL_GARDES, prefixe)
        return "mort"
    scen["pilote"] = pilote
    return scen


def test_A2_bout_en_bout_pilote_mort_ligne_coupee(tmp_path, monkeypatch):
    """De bout en bout (instance jouée pour de vrai : `tours --ecrire-etat`) : pilote mort pendant l'écriture d'une
    ligne de garde. Garde inconnue → arrêt « ligne de garde coupée », sans reprise ; nom « sonde orientée » lisible →
    arrêt « non interprétable ». La lecture rend la même issue ; aucun run principal."""
    c, f, _ = conduite_locale(tmp_path / "a", monkeypatch,
                              _scenario_pilote_mort_coupe(_prefixe_sans_nom(_ligne_garde("par tour", 2))))
    bilan = c.conduire()
    assert "pilote-reprise" not in f.lance and "principal" not in f.lance and f.detruites == ["77"]
    assert bilan["arret"].startswith("pas de run principal ; ligne de garde coupée au pilote")
    assert lc.LIGNE_DE_GARDE_COUPEE in bilan["pilote"][0]["gardes_tombees"]
    e = json.loads((f.base / "root/x/pilote" / cv.ETAT_EXECUTION).read_text())
    assert e["reconstitue"] is True and lc.LIGNE_DE_GARDE_COUPEE in e["gardes_tombees"]
    v = lc.valider(c.sortie)
    assert v["etat"] == lc.ETAT_LIGNE_COUPEE_PILOTE, v["details"]

    c, f, _ = conduite_locale(tmp_path / "b", monkeypatch,
                              _scenario_pilote_mort_coupe(_prefixe_nomme(_ligne_garde("sonde orientée", 0))))
    bilan = c.conduire()
    assert "pilote-reprise" not in f.lance and "principal" not in f.lance
    assert bilan["arret"].startswith("non interprétable (sonde orientée au pilote)")
    v = lc.valider(c.sortie)
    assert v["details"]["pilote"] == ["sonde orientée"]
    assert v["etat"] == "Non interprétable (garde « sonde orientée »)."


def test_A2_journal_de_gardes_du_pilote_illisible_au_milieu_leve(tmp_path):
    """A-2 (lecture 36 (b)) : une ligne illisible au milieu d'un journal de gardes transféré du pilote n'est pas une
    coupure : `valider` lève `GardeArret`, jamais une lecture du pilote."""
    racine = T3.poste_local(tmp_path, 21)

    def corrompre(x: Path) -> None:
        _ajouter_octets(x / cv.JOURNAL_GARDES, _prefixe_sans_nom(_ligne_garde("par tour", 1)) + b"\n"
                        + _ligne_garde("par tour", 2, "passée") + b"\n")
    _remplacer_pilote(racine, tmp_path, "pilote", corrompre, {})
    with pytest.raises(GardeArret, match="illisible"):
        lc.valider(racine)


# --- C-1 (relecture des lignes touchées v8, `baa35511…`) : S1 inversée ---------------------------------------------------

def test_C1_pilote_mort_tours_en_echec_arret_sans_reprise(tmp_path, monkeypatch):
    """Pilote mort pendant l'écriture d'une ligne de garde ; la reconstitution par `tours` échoue : la conduite
    s'arrête (nœud), sans reprise, sans règle, sans run principal."""
    scen = _scenario_pilote_mort_coupe(_prefixe_sans_nom(_ligne_garde("par tour", 2)))
    c, f, _ = conduite_locale(tmp_path / "a", monkeypatch, scen)
    vrai = c._tours_relus
    n = {"k": 0}

    def tours_en_echec(phase, cause="coupure de l'hôte"):
        n["k"] += 1
        if phase == "pilote" and n["k"] == 1:
            return None
        return vrai(phase, cause)
    monkeypatch.setattr(c, "_tours_relus", tours_en_echec)
    bilan = c.conduire()
    assert "pilote-reprise" not in f.lance and "principal" not in f.lance, (f.lance, bilan.get("arret"))
    assert "pilote mort, état des gardes illisible" in bilan["arret"]
    assert f.detruites  # instance détruite


# ======================================================================================================================
# v10 : arrêt autonome de l'instance (chien de garde), garde d'auto-arrêt, reprise
# ======================================================================================================================

import http.server  # noqa: E402
import threading  # noqa: E402

B = 75.0
LOIN = time.time() + 30 * 86400  # échéance du GO lointaine


def _racine(tmp_path) -> Path:
    r = tmp_path / "inst"
    (r / "etats").mkdir(parents=True)
    (r / "x").mkdir()
    return r


def _depense(d: float) -> dict:
    """Dépense du poste égale à `d` maintenant (c = 1 USD/h)."""
    return {"d_avant": 0.0, "c": 1.0, "creation": time.time() - d * 3600, "b": B}


def _battement(racine: Path, age_s: float) -> None:
    p = racine / "etats" / inst.BATTEMENT_CONDUITE
    p.touch()
    t = time.time() - age_s
    os.utime(p, (t, t))


def _detachee(racine: Path, nom: str, commande: str) -> int:
    r = _bash_local(la.commande_detachee(nom, commande), racine / "etats")
    assert la.lancement_verifie(r.stdout), r
    return int(r.stdout.split()[-1])


def _tuer(pid: int) -> None:
    try:
        os.killpg(pid, signal.SIGKILL)
    except ProcessLookupError:
        pass


def _execution_sur_instance(tmp_path, racine: Path, phase: str, k: int, etat: dict | None = None,
                            garder_etat: bool = False) -> Path:
    x, _ = T3.execution_factice(tmp_path / f"fab-{phase}", phase, k, {"phase": phase, **(etat or {})})
    cible = racine / "x" / phase
    shutil.copytree(x, cible)
    if not garder_etat:
        (cible / cv.ETAT_EXECUTION).unlink()
    return cible


def _manifestes(racine: Path, k: int = 30) -> None:
    m = {"graines": {"pilote": an.GRAINE_PILOTE, "principal": an.GRAINE_PRINCIPAL}, "regle_tours": {"K": k}}
    for nom in ("mise-en-place", "regle", "relance"):
        (racine / lc.MANIFESTES[nom]).write_text(json.dumps(m))


class Horloge:
    def __init__(self):
        self.decalage = 0.0

    def __call__(self):
        return time.time() + self.decalage


def _chien(racine, depense=None, echeance=LOIN, **kw):
    appels = []
    h = kw.pop("horloge", None) or Horloge()
    c = inst.ChienDeGarde(racine, depense or _depense(10.0), echeance, arreter_api=lambda: appels.append("stopped"),
                          horloge=h, attendre=lambda s: None, signaler_pid1=lambda: appels.append("pid1"), **kw)
    return c, appels, h


def _journal_chien(racine) -> list[dict]:
    p = racine / "etats" / inst.JOURNAL_CHIEN
    return [json.loads(l) for l in p.read_text().splitlines()] if p.exists() else []


# --- décision (fonction pure) : chaque cas, sain et artefact ------------------------------------------------------------

def _d(**kw):
    base = dict(maintenant=1000.0, depense=10.0, b=B, echeance_go=1e9, marge_transfert_s=3600.0, age_battement=10.0,
                en_cours=[], fin=False, rapatrie=False, debut_cause=None)
    return inst.decider(**{**base, **kw})


def test_v10_decider_sain_rien():
    assert _d() == ("rien", None)
    assert _d(en_cours=["pilote"]) == ("rien", None)
    assert _d(en_cours=["principal"]) == ("rien", None)


def test_v10_decider_cas1_fin():
    # conduite vivante : la fin seule ne coupe pas son transfert ; la marque `rapatrie` arrête
    assert _d(fin=True, debut_cause=990.0) == ("rien", "fin")
    assert _d(rapatrie=True) == ("arreter", "fin")
    assert _d(fin=True, debut_cause=1000.0 - inst.DELAI_PRISE_EN_CHARGE_S) == ("arreter", "fin")  # prise en charge
    # conduite injoignable : arrêt aussitôt
    assert _d(fin=True, age_battement=inst.D_ABANDON_S) == ("arreter", "fin")


def test_v10_decider_cas2_depense():
    assert _d(depense=B - 2.01) == ("rien", None)  # sain, juste sous B − 2
    assert _d(depense=B - 2, age_battement=1e6) == ("arreter", "dépense")
    assert _d(depense=B - 2, en_cours=["principal"], age_battement=1e6) == ("arreter", "dépense")  # jamais « attendre »
    assert _d(depense=B - 2) == ("rien", "dépense")  # conduite vivante : son transfert n'est pas coupé…
    assert _d(depense=B - 0.5) == ("arreter", "dépense")  # … jusqu'au seuil du veilleur


def test_v10_decider_cas3_echeance():
    e = 1000.0 + 3600.0
    assert _d(echeance_go=e + 1) == ("rien", None)
    assert _d(echeance_go=e, age_battement=1e6) == ("arreter", "échéance du GO")
    assert _d(echeance_go=e) == ("rien", "échéance du GO")
    assert _d(echeance_go=1000.0 + 1800.0) == ("arreter", "échéance du GO")  # moitié de la marge, conduite vivante


def test_v10_decider_cas4_conduite_injoignable():
    vieux = inst.D_ABANDON_S
    assert _d(age_battement=vieux - 1, en_cours=["pilote"]) == ("rien", None)  # sain
    for en_cours in ([], ["amorce"], ["mise-en-place"], ["controle-juge"], ["pilote"], ["pilote-reprise"], ["regle"],
                     ["principal", "pilote"]):
        assert _d(age_battement=vieux, en_cours=en_cours) == ("arreter", "conduite injoignable"), en_cours
    for en_cours in (["principal"], ["principal-relance"]):
        assert _d(age_battement=vieux, en_cours=en_cours) == ("attendre", "conduite injoignable"), en_cours


# --- chien de garde sur un faux disque d'instance, processus réels (bash), API factice ---------------------------------

def test_v10_cas4_conduite_morte_pendant_le_pilote_arret_sans_run_principal(tmp_path):
    r = _racine(tmp_path)
    _manifestes(r)
    _execution_sur_instance(tmp_path, r, "pilote", 1, {"k": 3, "graine": an.GRAINE_PILOTE})
    pid = _detachee(r, "pilote", "sleep 60")
    try:
        _battement(r, inst.D_ABANDON_S + 60)
        c, appels, _ = _chien(r)
        assert c.boucle(passages=3) == "conduite injoignable" and appels == ["stopped"]
        assert subprocess.run(["pgrep", "-g", str(pid)], capture_output=True, text=True).stdout.split() == []
        e = json.loads((r / "x" / "pilote" / cv.ETAT_EXECUTION).read_text())
        assert e["reconstitue"] is True and e["cause_arret"] == "instance injoignable"
        assert lc.issue_pilote(e) == "chute"  # pas de reprise : la conduite est morte ; aucun run principal
        assert (r / "x" / "pilote" / cv.EMPREINTES_INSTANCE).is_file() and not (r / "x" / "principal").exists()
        etat_ = json.loads((r / "etats" / inst.ETAT_ARRET).read_text())
        assert etat_["cause"] == "conduite injoignable" and etat_["arretees"] == ["pilote"]
    finally:
        _tuer(pid)


def test_v10_cas4_sain_conduite_vivante_le_pilote_continue(tmp_path):
    r = _racine(tmp_path)
    pid = _detachee(r, "pilote", "sleep 60")
    try:
        _battement(r, 5)
        c, appels, _ = _chien(r)
        assert c.boucle(passages=3) is None and appels == [] and inst.pid_vivant(r / "etats", "pilote") == pid
        assert json.loads((r / "etats" / f"{inst.CHIEN}.battement").read_text())["pid"] == os.getpid()
    finally:
        _tuer(pid)


def test_v10_cas4_conduite_morte_pendant_le_run_principal_le_run_finit_puis_arret(tmp_path):
    r = _racine(tmp_path)
    _manifestes(r)
    _execution_sur_instance(tmp_path, r, "principal", 21, {"k": 30}, garder_etat=True)
    pid = _detachee(r, "principal", "sleep 2")
    try:
        _battement(r, inst.D_ABANDON_S + 60)
        c, appels, _ = _chien(r)
        assert c.boucle(passages=2) is None and appels == []  # attend : le run principal finit sous ses gardes
        assert inst.pid_vivant(r / "etats", "principal") == pid
        fin = time.time() + 20
        while not (r / "etats" / "principal.fin").exists() and time.time() < fin:
            time.sleep(0.1)
        assert c.boucle(passages=2) is not None and appels == ["stopped"]
        assert "CODE 0" in (r / "etats" / "principal.fin").read_text()  # jamais arrêté par le chien
        assert c.arretees == [] and (r / "x" / "principal" / cv.EMPREINTES_INSTANCE).is_file()
    finally:
        _tuer(pid)


def test_v10_cas4_artefact_principal_avec_depense_arret_apres_grace(tmp_path):
    """Conduite morte, run principal en cours, D ≥ B − 2 et l'exécution ne s'arrête pas d'elle-même (artefact) :
    pas d'« attendre » ; après la grâce, arrêt par PID, état reconstitué « dépense », conteneur arrêté."""
    r = _racine(tmp_path)
    _manifestes(r)
    _execution_sur_instance(tmp_path, r, "principal", 21, {"k": 30})
    pid = _detachee(r, "principal", "sleep 60")
    try:
        _battement(r, inst.D_ABANDON_S + 60)
        c, appels, h = _chien(r, _depense(B - 2))
        assert c.boucle(passages=2) is None and appels == []  # grâce : l'exécution s'arrête elle-même d'ordinaire
        h.decalage = inst.GRACE_EXECUTION_S + 1
        assert c.boucle(passages=2) == "dépense" and appels == ["stopped"]
        e = json.loads((r / "x" / "principal" / cv.ETAT_EXECUTION).read_text())
        assert e["cause_arret"] == "dépense" and lc.relance_permise(e) is False
    finally:
        _tuer(pid)


def test_v10_cas2_depense_hors_execution_arret(tmp_path):
    r = _racine(tmp_path)
    pid = _detachee(r, "mise-en-place", "sleep 60")
    try:
        _battement(r, inst.D_ABANDON_S + 60)
        c, appels, _ = _chien(r, _depense(B - 2))
        assert c.boucle(passages=2) == "dépense" and appels == ["stopped"]
        assert inst.pid_vivant(r / "etats", "mise-en-place") is None
    finally:
        _tuer(pid)


def test_v10_cas2_conduite_vivante_transfert_non_coupe_puis_borne_du_veilleur(tmp_path):
    r = _racine(tmp_path)
    _battement(r, 5)
    c, appels, _ = _chien(r, _depense(B - 2))
    assert c.boucle(passages=2) is None and appels == []  # sain : la conduite vivante transfère
    c, appels, _ = _chien(r, _depense(B - 0.5))
    assert c.boucle(passages=1) == "dépense" and appels == ["stopped"]  # borne dure, conduite vivante ou non
    c, appels, _ = _chien(r, _depense(B - 2.5))
    assert c.boucle(passages=2) is None and appels == []  # sain : sous B − 2


def test_v10_cas3_echeance_moins_marge(tmp_path):
    r = _racine(tmp_path)
    _battement(r, inst.D_ABANDON_S + 60)
    c, appels, _ = _chien(r, echeance=time.time() + 3600 - 10)
    assert c.boucle(passages=1) == "échéance du GO" and appels == ["stopped"]
    r2 = _racine(tmp_path / "b")
    _battement(r2, 5)
    c, appels, _ = _chien(r2, echeance=time.time() + 3600 - 10)
    assert c.boucle(passages=2) is None and appels == []  # conduite vivante : son transfert
    c, appels, _ = _chien(r2, echeance=time.time() + 1800 - 10)
    assert c.boucle(passages=1) == "échéance du GO" and appels == ["stopped"]
    r3 = _racine(tmp_path / "c")
    _battement(r3, inst.D_ABANDON_S - 600)
    c, appels, _ = _chien(r3, echeance=time.time() + 3600 + 600)
    assert c.boucle(passages=2) is None and appels == []  # sain


def test_v10_cas1_fin_normale(tmp_path):
    """Run principal fini sans relance permise : conduite vivante → arrêt à la marque `rapatrie` ; relance permise
    (artefact : fin prise trop tôt) → rien ; fin de la relance → arrêt."""
    r = _racine(tmp_path)
    _manifestes(r)
    _execution_sur_instance(tmp_path, r, "principal", 21, {"k": 30, "code_retour": 0}, garder_etat=True)
    (r / "etats" / "principal.fin").write_text("ETAT {}\nCODE 0\n")
    _battement(r, 5)
    assert inst.fin_prevue(r) is True
    c, appels, _ = _chien(r)
    assert c.boucle(passages=2) is None and appels == []  # la conduite transfère
    (r / "etats" / inst.MARQUE_RAPATRIE).touch()
    assert c.boucle(passages=1) == "fin" and appels == ["stopped"]
    # artefact : principal mort à 3 tours, relance permise : ce n'est pas la fin
    r2 = _racine(tmp_path / "b")
    _execution_sur_instance(tmp_path / "b", r2, "principal", 3, {"k": 30, "code_retour": 1}, garder_etat=True)
    (r2 / "etats" / "principal.fin").write_text("CODE 1\n")
    assert inst.fin_prevue(r2) is False
    _battement(r2, 5)
    c, appels, h = _chien(r2)
    h.decalage = inst.DELAI_PRISE_EN_CHARGE_S + 10
    assert c.boucle(passages=2) is None and appels == []
    (r2 / "etats" / "principal-relance.fin").write_text("CODE 0\n")
    assert inst.fin_prevue(r2) is True
    c, appels, h = _chien(r2)
    c.boucle(passages=1)
    h.decalage = inst.DELAI_PRISE_EN_CHARGE_S + 10
    assert c.boucle(passages=1) == "fin" and appels == ["stopped"]  # prise en charge échue


def test_v10_api_refusee_retentee_puis_repli_pid1_journalise(tmp_path):
    r = _racine(tmp_path)
    _battement(r, inst.D_ABANDON_S + 60)
    essais = []

    def refuse():
        essais.append(1)
        raise GardeArret("auto-arrêt : appel à l'API refusé ou impossible (URLError)")
    pid1 = []
    c = inst.ChienDeGarde(r, _depense(10), LOIN, arreter_api=refuse, attendre=lambda s: None,
                          signaler_pid1=lambda: pid1.append(1))
    assert c.boucle(passages=inst.ESSAIS_API_AVANT_PID1) is None
    assert len(essais) == inst.ESSAIS_API_AVANT_PID1 and pid1 == [1]  # jamais de repli silencieux : journalisé
    j = _journal_chien(r)
    assert sum(1 for x in j if x.get("conteneur") == "arrêt refusé") == inst.ESSAIS_API_AVANT_PID1
    assert any("PID 1" in str(x.get("conteneur")) for x in j)


def test_v10_minuterie_de_reprise(tmp_path):
    r = _racine(tmp_path)
    (r / "etats" / inst.MARQUE_RAPATRIE).touch()  # ignorée en minuterie
    c, appels, h = _chien(r, depense=None, minuterie_s=600)
    c.depense = None
    assert c.boucle(passages=1) is None and appels == []
    h.decalage = 601
    assert c.boucle(passages=1) == "minuterie" and appels == ["stopped"]
    c, appels, _ = _chien(r, echeance=time.time() - 1, minuterie_s=600)
    assert c.boucle(passages=1) == "échéance du GO" and appels == ["stopped"]


# --- API de Vast : appel réel (bibliothèque standard) contre un serveur local -----------------------------------------

class _Api(http.server.BaseHTTPRequestHandler):
    recues: list = []
    reponse = {"success": True}

    def do_PUT(self):
        n = int(self.headers.get("Content-Length") or 0)
        type(self).recues.append({"chemin": self.path, "auth": self.headers.get("Authorization"),
                                  "corps": json.loads(self.rfile.read(n))})
        corps = json.dumps(type(self).reponse).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)

    def log_message(self, *a):
        pass


@pytest.fixture
def api_locale():
    _Api.recues, _Api.reponse = [], {"success": True}
    s = http.server.HTTPServer(("127.0.0.1", 0), _Api)
    t = threading.Thread(target=s.serve_forever, daemon=True)
    t.start()
    yield f"http://127.0.0.1:{s.server_port}"
    s.shutdown()


def _environ(tmp_path, ident="77", cle="cle-instance-factice", autres=True) -> str:
    p = tmp_path / f"environ-{ident}-{bool(cle)}"
    morceaux = [b"PATH=/usr/bin"] + ([f"CONTAINER_ID={ident}".encode()] if ident else []) \
        + ([f"CONTAINER_API_KEY={cle}".encode()] if cle else []) + ([b"AUTRE=x"] if autres else [])
    p.write_bytes(b"\0".join(morceaux) + b"\0")
    return str(p)


def test_v10_requete_api_put_avec_la_cle_de_l_instance(tmp_path, api_locale, monkeypatch):
    monkeypatch.delenv("CONTAINER_ID", raising=False)
    monkeypatch.delenv("CONTAINER_API_KEY", raising=False)
    env = _environ(tmp_path)
    assert inst.requete_etat_instance("stopped", env, api_locale) == {"instance": "77", "etat_vise": "stopped"}
    assert _Api.recues == [{"chemin": "/api/v0/instances/77/", "auth": "Bearer cle-instance-factice",
                            "corps": {"state": "stopped"}}]
    _Api.reponse = {"success": False, "msg": "refusé"}
    with pytest.raises(GardeArret) as err:
        inst.requete_etat_instance("stopped", env, api_locale)
    assert "cle-instance-factice" not in str(err.value)
    with pytest.raises(GardeArret, match="absent"):
        inst.requete_etat_instance("stopped", _environ(tmp_path, cle=None), api_locale)
    with pytest.raises(GardeArret):
        inst.requete_etat_instance("stopped", env, "http://127.0.0.1:9")  # injoignable
    with pytest.raises(GardeArret):
        inst.requete_etat_instance("destroyed", env, api_locale)  # l'instance ne se détruit jamais elle-même


def test_v10_chien_en_processus_reel_arrete_le_conteneur(tmp_path, api_locale):
    """Processus réel `instance_v16 chien-de-garde` (conduite injoignable, aucune commande) : PUT `stopped`."""
    r = _racine(tmp_path)
    _battement(r, inst.D_ABANDON_S + 60)
    env = {**os.environ, "VAST_URL": api_locale, "PYTHONPATH": str(DEPOT / "src")}
    p = subprocess.Popen([sys.executable, "-m", la.INSTANCE_MODULE, inst.CHIEN, "--racine", str(r), "--depense",
                          json.dumps(_depense(10)), "--echeance-go", repr(LOIN), "--periode", "0.2",
                          "--environ", _environ(tmp_path)], env=env)
    try:
        fin = time.time() + 30
        while not _Api.recues and time.time() < fin:
            time.sleep(0.1)
        assert _Api.recues and _Api.recues[0]["corps"] == {"state": "stopped"}
        assert _Api.recues[0]["chemin"] == "/api/v0/instances/77/"
        assert json.loads((r / "etats" / inst.ETAT_ARRET).read_text())["cause"] == "conduite injoignable"
    finally:
        p.kill()
        p.wait()


# --- garde d'auto-arrêt (avant la mise en place) -----------------------------------------------------------------------

def test_v10_verifier_auto_arret(tmp_path, api_locale, monkeypatch):
    monkeypatch.delenv("CONTAINER_ID", raising=False)
    monkeypatch.delenv("CONTAINER_API_KEY", raising=False)
    r = _racine(tmp_path)
    etats = r / "etats"
    pid = _detachee(r, inst.CHIEN, "sleep 60")
    try:
        (etats / f"{inst.CHIEN}.battement").write_text(json.dumps({"t": time.time()}))
        ok = inst.verifier_auto_arret("77", etats, _environ(tmp_path), api_locale, delai_s=0)
        assert ok["disponible"] is True and _Api.recues[-1]["corps"] == {"state": "running"}  # essai sans effet
        assert "cle-instance-factice" not in json.dumps(ok)
        for env, ident, attendu in ((_environ(tmp_path, cle=None), "77", "variables"),
                                    (_environ(tmp_path), "78", "identifiant")):
            v = inst.verifier_auto_arret(ident, etats, env, api_locale, delai_s=0)
            assert v["disponible"] is False and attendu in v["cause"]
        _Api.reponse = {"success": False}
        v = inst.verifier_auto_arret("77", etats, _environ(tmp_path), api_locale, delai_s=0)
        assert v["disponible"] is False and v["cause"].endswith("api")
        _Api.reponse = {"success": True}
        (etats / f"{inst.CHIEN}.battement").write_text(json.dumps({"t": time.time() - 3600}))
        v = inst.verifier_auto_arret("77", etats, _environ(tmp_path), api_locale, delai_s=0)
        assert v["disponible"] is False and "chien_de_garde" in v["cause"]
    finally:
        _tuer(pid)
    (etats / f"{inst.CHIEN}.battement").write_text(json.dumps({"t": time.time()}))
    time.sleep(0.3)
    v = inst.verifier_auto_arret("77", etats, _environ(tmp_path), api_locale, delai_s=0)
    assert v["disponible"] is False and "chien_de_garde" in v["cause"]  # chien mort


def test_v10_auto_arret_indisponible_garde_de_mise_en_place_tombee(tmp_path, monkeypatch):
    indispo = ({"commande": "auto-arret", "disponible": False, "cause": "auto-arrêt indisponible : api"}, 3)
    c, f, _ = conduite(tmp_path, monkeypatch, reponses(**{"auto-arret": indispo}))
    bilan = c.conduire()
    assert bilan["arret"].startswith("garde de mise en place tombée : auto-arrêt de l'instance indisponible")
    assert f.lance == ["amorce", "auto-arret"] and f.detruites == ["77"]  # pas de run ; instance détruite
    c, f, _ = conduite(tmp_path / "b", monkeypatch, reponses(**{"auto-arret": (None, 1)}))  # sans ligne d'état
    assert c.conduire()["arret"].startswith("garde de mise en place tombée") and "mise-en-place" not in f.lance
    c, f, _ = conduite(tmp_path / "c", monkeypatch, reponses())  # sain
    assert "arret" not in c.conduire() and f.lance[1:3] == ["auto-arret", "mise-en-place"]
    assert any(" auto-arret --instance 77" in x for x in f.commandes)


def test_v10_amorce_lance_le_chien_avant_les_telechargements(tmp_path, monkeypatch):
    c, f, _ = conduite(tmp_path, monkeypatch, reponses())
    c.conduire()
    amorce = f.envoyes["/root/amorce-v5.sh"].decode()
    i = amorce.index(f"-m {la.INSTANCE_MODULE} {inst.CHIEN} ")
    assert i < amorce.index("huggingface-cli download") and "chien de garde non lancé" in amorce
    assert "--d-abandon 7200.0" in amorce and '"b": 75.0' in amorce
    assert "CONTAINER_API_KEY" not in amorce and "api-key" not in amorce  # aucune clé posée sur l'instance


def test_v10_amorce_bash_reel_chien_lance_ou_garde(tmp_path):
    """La ligne de l'amorce, jouée en bash : lancement vérifié → suite ; non vérifié → `ETAT` d'échec, code 3."""
    d = tmp_path / "etats"
    ligne = la.script_amorce({"versions": {}, "git": {}, "python": "3.11", "revision_modele": "r",
                              "juge": {"revision_adaptateur": "a", "revision_base": "b"}}, "0" * 64,
                             la.commande_detachee(inst.CHIEN, "sleep 30")).splitlines()
    (l_chien,) = [x for x in ligne if "chien de garde non lancé" in x]
    r = subprocess.run(["bash", "-c", "set -euo pipefail; " + l_chien.replace(la.ETATS_DISTANTS, str(d))
                        + "; echo SUITE"], capture_output=True, text=True, timeout=60)
    try:
        assert r.returncode == 0 and "SUITE" in r.stdout and inst.pid_vivant(d, inst.CHIEN) is not None
    finally:
        _tuer(int((d / f"{inst.CHIEN}.pid").read_text()))
    faux = l_chien.replace(la.commande_detachee(inst.CHIEN, "sleep 30"), "echo rien")
    r = subprocess.run(["bash", "-c", "set -euo pipefail; " + faux + "; echo SUITE"], capture_output=True, text=True)
    assert r.returncode == 3 and "chien de garde non lancé" in r.stdout and "SUITE" not in r.stdout


def test_v10_sondage_touche_le_battement_et_marque_rapatrie(tmp_path, monkeypatch):
    d = tmp_path / "etats"
    d.mkdir()
    _bash_local(la.commande_sondage("x"), d)
    assert (d / inst.BATTEMENT_CONDUITE).is_file()
    # v12 (Q-2) : marque posée après les empreintes, seulement sur un transfert complet (conduite adossée à des
    # dossiers locaux) ; transfert incomplet (fournisseur factice sans fichiers) : aucune marque, destruction quand même
    c, f, _ = conduite_locale(tmp_path / "c", monkeypatch, scenario(21, principal_fini(21)))
    bilan = c.conduire()
    marque = [i for i, x in enumerate(f.commandes) if x.endswith(f"/{inst.MARQUE_RAPATRIE}")]
    empreintes = [i for i, x in enumerate(f.commandes) if "instance_v16 empreintes" in x]
    assert bilan["transfert_complet"] is True and len(marque) == 1 and marque[0] > max(empreintes)
    assert bilan["marque_rapatrie"] is True and f.detruites == ["77"]
    c, f, _ = conduite(tmp_path / "d", monkeypatch, reponses())
    bilan = c.conduire()
    assert not any(x.endswith(f"/{inst.MARQUE_RAPATRIE}") for x in f.commandes)
    assert bilan["marque_rapatrie"] == "non posée : transfert incomplet"
    assert f.appels.index("detruire") > f.appels.index("empreintes")


# --- `vastai` : confirmation et succès exigés (défaut v9) -------------------------------------------------------------

def test_v10_vast_detruire_y_et_succes_exige(monkeypatch):
    v = la.FournisseurVast()
    appels, sorties = [], {}

    def vast(*args):
        appels.append(args)
        return sorties.get(args[0], "")
    monkeypatch.setattr(v, "_vast", vast)
    sorties["destroy"] = "destroying instance 77.\n"
    v.detruire("77")
    assert appels[-1] == ("destroy", "instance", "77", "-y")
    for refus in ("Are you sure…? [y/N] \nAborted.\n", "Failed with error 404: not found\n", ""):
        sorties["destroy"] = refus
        with pytest.raises(GardeArret):
            v.detruire("77")
    sorties.update({"stop": "stopping instance 77.\n", "start": "starting instance 77.\n"})
    v.arreter("77")
    v.demarrer("77")
    assert appels[-2:] == [("stop", "instance", "77"), ("start", "instance", "77")]
    sorties["stop"] = "stopping instance 78.\n"
    with pytest.raises(GardeArret):
        v.arreter("77")


# --- reprise ----------------------------------------------------------------------------------------------------------

ETIQ = la.PREFIXE_ETIQUETTE + "0123456789abcdef"


def _poste_interrompu(tmp_path, monkeypatch, k=21):
    """Conduite saine dont la destruction n'a pas eu lieu (poste éteint) : l'instance factice garde ses journaux,
    empreintés sur l'instance avant l'arrêt ; on la reprend."""
    c, f, _ = conduite_locale(tmp_path, monkeypatch, scenario(k, principal_fini(k)))
    f.detruire = lambda ident: (_ for _ in ()).throw(RuntimeError("poste éteint"))
    bilan_conduite = c.conduire()
    assert bilan_conduite["detruite"] is False
    del f.detruire
    vrai = f.executer
    f.etat, f.demarrages, f.arrets, f.minuteries, f.en_cours = "stopped", [], [], [], []

    def executer(ident, commande, delai_s=None):
        if f.etat != "running":
            return 255, ""
        if commande.startswith("ls -1 /root/x"):
            return 0, "\n".join(sorted(p.name for p in f.local("/root/x").iterdir())) + "\n"
        if f"{inst.MINUTERIE}.pid" in commande:
            f.minuteries.append(commande)
            return 0, "LANCE 999\n"
        if " en-cours" in commande:
            return 0, "ETAT " + json.dumps({"commande": "en-cours", "en_cours": f.en_cours}) + "\n"
        return vrai(ident, commande, delai_s)
    f.executer = executer
    f.inventaire = lambda e: ["77"] if e == ETIQ else ["99"]
    f.statut = lambda ident: f.etat
    f.demarrer = lambda ident: (f.demarrages.append(ident), setattr(f, "etat", "running"))
    f.arreter = lambda ident: (f.arrets.append(ident), setattr(f, "etat", "stopped"))
    f.detruites.clear()
    # v11 (C-1) : veilleur local d'arrêt de la reprise remplacé par un substitut (aucun processus, aucun `vastai`)
    f.veilleurs, f.veilleurs_arretes, f.veilleur_vivant = [], [], True

    def lancer(ident, etiquette, echeance, journal, spec, periode):
        f.veilleurs.append({"ident": ident, "etiquette": etiquette, "echeance": echeance, "journal": journal,
                            "spec": spec, "etat_instance": f.etat, "demarrages": len(f.demarrages)})
        return 5000 + len(f.veilleurs)
    monkeypatch.setattr(la, "lancer_veilleur_arret_processus", lancer, raising=False)
    monkeypatch.setattr(la, "verifier_veilleur", lambda pid, journal, **kw: f.veilleur_vivant)
    monkeypatch.setattr(la, "arreter_veilleur", lambda pid: f.veilleurs_arretes.append(pid))
    return c, f


def test_v10_reprendre_transfert_comparaison_destruction_seule_instance(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    bilan = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert f.demarrages == ["77"] and len(f.minuteries) == 1 and "--minuterie 3600.0" in f.minuteries[0]
    assert f.minuteries[0].startswith(f"rm -f /root/etats/{inst.MINUTERIE}.fin ")  # jamais une vieille `.fin` prise
    assert bilan["detruite"] is True and f.detruites == ["77"] and "alertes" not in bilan  # jamais « 99 »
    assert bilan["transfert_complet"] is True and set(bilan["transferts"]) == {
        "mise-en-place", "controle-juge", "pilote", "regle", "principal"}
    assert all(t["foi"] == "transfert-1" for t in bilan["transferts"].values())
    assert any("empreintes --travail /root/x/principal --si-absent" in x for x in f.commandes)
    assert bilan["redemarrage"]["duree_s"] >= 0
    racine = c.sortie / "reprise-v10"
    scellement.verifier(racine / "bilan-reprise-v10.json")
    v = lc.valider(racine)
    assert v["etat"] is None and v["k_prime"] == 21, v["details"]
    assert lc.lire(v, an.graines()["reechantillonnage"])["verdict"].startswith("Effet reproduit")
    # seconde reprise : nouveau dossier, rien d'écrasé ; plus d'instance : rien n'est fait
    f.inventaire = lambda e: []
    b2 = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert (c.sortie / "reprise-v10-2" / "bilan-reprise-v10.json").is_file() and b2["detruite"] is False
    assert "aucune instance" in b2["issue"]


def test_v10_reprendre_empreintes_differentes_pas_de_destruction(tmp_path, monkeypatch):
    """Artefact : un journal changé sur l'instance après les empreintes prises avant l'arrêt : aucune égalité ; pas de
    destruction ; instance remise à l'arrêt."""
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    j = f.local("/root/x/principal") / cv.JOURNAL_GARDES
    j.write_bytes(j.read_bytes() + b'{"etat": "passee", "garde": "ajout"}\n')
    bilan = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert bilan["detruite"] is False and f.detruites == [] and f.arrets == ["77"]
    assert bilan["transferts"]["principal"]["foi"] is None and "pas de destruction" in bilan["alertes"][0]


def test_v10_reprendre_artefacts_rien_n_est_detruit(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    # deux instances portent l'étiquette
    f.inventaire = lambda e: ["77", "78"]
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert f.detruites == [] and f.demarrages == [] and "plusieurs instances" in b["alertes"][0]
    # instance de l'étiquette différente de celle du journal de la conduite
    f.inventaire = lambda e: ["78"]
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert f.detruites == [] and f.demarrages == [] and "n'est pas celle du journal" in b["alertes"][0]
    # échéance du GO passée : aucun redémarrage
    f.inventaire = lambda e: ["77"]
    b = la.Reprise(f, c.sortie, ETIQ, time.time() - 1, attendre=lambda s: None).reprendre()
    assert f.demarrages == [] and f.detruites == [] and "échéance du GO passée" in b["alertes"][0]
    # carte reprise : jamais prête après le redémarrage → remise à l'arrêt, rien de détruit
    f.demarrer = lambda ident: f.demarrages.append(ident)  # reste « stopped »
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, delai_prete_s=0).reprendre()
    assert f.demarrages == ["77"] and f.arrets == ["77"] and f.detruites == [] and "non prête" in b["alertes"][0]
    # en marche, commande en cours : rien n'est fait (pas de reprise du calcul, pas d'arrêt)
    f.etat, f.en_cours = "running", ["principal"]
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert f.detruites == [] and b["en_cours"] == ["principal"] and "commande en cours" in b["issue"]
    assert not any(x.startswith("p=$(cat /root/etats/principal.pid") for x in f.commandes[-3:])


def test_v10_reprendre_en_marche_sans_commande_transfert_et_destruction(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    f.etat = "running"
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert f.demarrages == [] and f.minuteries == [] and b["detruite"] is True and f.detruites == ["77"]
    assert any(x.endswith(f"/{inst.BATTEMENT_CONDUITE}") for x in f.commandes)  # le chien laisse transférer


# ======================================================================================================================
# v11 : relecture du code v10 (`relecture-code-condition6-v10-bailey-v1.md`, `b6b6430b…`) — un cas sain et un artefact
# par correction ; sondes S1 à S4 du relecteur inversées (elles passent sur la v11 et échouent sur la v10)
# ======================================================================================================================

import errno  # noqa: E402


# --- B-1 : disque plein, l'arrêt du conteneur est demandé quand même -------------------------------------------------

def test_v11_B1_S1_inverse_disque_plein_arret_demande_quand_meme(tmp_path, monkeypatch):
    r = _racine(tmp_path)
    _battement(r, inst.D_ABANDON_S + 60)  # conduite injoignable
    vrai = inst._ecrire_json

    def plein(chemin, objet):
        if Path(chemin).name == inst.ETAT_ARRET:
            raise OSError(errno.ENOSPC, "No space left on device")
        return vrai(chemin, objet)
    monkeypatch.setattr(inst, "_ecrire_json", plein)
    c, appels, _ = _chien(r)
    assert c.boucle(passages=50) == "conduite injoignable" and appels == ["stopped"]
    assert c.prepare is True and not (r / "etats" / inst.ETAT_ARRET).exists()
    assert any(x.get("etat_arret") == "non écrit" and x.get("erreur") == "OSError" for x in _journal_chien(r))


def test_v11_B1_disque_plein_partout_battement_touche_et_arret(tmp_path, monkeypatch):
    """Artefact : aucune écriture possible (états, empreintes, état de l'arrêt, battement) ; le battement du chien est
    touché (date du fichier), l'arrêt est demandé au premier passage."""
    r = _racine(tmp_path)
    _manifestes(r)
    _execution_sur_instance(tmp_path, r, "pilote", 1, {"k": 3, "graine": an.GRAINE_PILOTE})
    _battement(r, inst.D_ABANDON_S + 60)
    b = r / "etats" / f"{inst.CHIEN}.battement"
    b.write_text("{}")
    os.utime(b, (time.time() - 3600, time.time() - 3600))

    def plein(chemin, objet):
        raise OSError(errno.ENOSPC, "No space left on device")
    monkeypatch.setattr(inst, "_ecrire_json", plein)
    c, appels, _ = _chien(r)
    assert c.boucle(passages=1) == "conduite injoignable" and appels == ["stopped"]
    assert time.time() - b.stat().st_mtime < 60  # battement touché sans écriture
    assert not (r / "x" / "pilote" / cv.ETAT_EXECUTION).exists()  # état non reconstitué : noté, pas bloquant
    j = _journal_chien(r)
    assert any(x.get("etat_reconstitue") == "pilote" and "erreur" in x for x in j)
    assert any(x.get("empreintes") == "pilote" and "erreur" in x for x in j)


def test_v11_B1_sain_etat_de_l_arret_ecrit(tmp_path):
    r = _racine(tmp_path)
    _battement(r, inst.D_ABANDON_S + 60)
    c, appels, _ = _chien(r)
    assert c.boucle(passages=1) == "conduite injoignable" and appels == ["stopped"]
    e = json.loads((r / "etats" / inst.ETAT_ARRET).read_text())
    assert e["survivantes"] == [] and e["cause"] == "conduite injoignable"
    assert not any("erreur" in x for x in _journal_chien(r))


def test_v11_B1_observation_en_erreur_ne_leve_pas(tmp_path, monkeypatch):
    """Artefact : lecture des commandes en cours impossible : notée, lue prudemment (aucune en cours) ; la décision
    suit ; une dépense illisible empêche le chien de démarrer (garde d'auto-arrêt : pas de run)."""
    r = _racine(tmp_path)
    _battement(r, inst.D_ABANDON_S + 60)

    def illisible(e):
        raise PermissionError("etats")
    monkeypatch.setattr(inst, "commandes_en_cours", illisible)
    c, appels, h = _chien(r)
    assert c.passage() is None and c.cause == "conduite injoignable"  # décidé ; arrêt par PID impossible
    h.decalage = inst.ATTENTE_COMMANDES_MAX_S + 1
    assert c.passage() == "conduite injoignable" and appels == ["stopped"]
    assert any(x.get("observation") == "commandes en cours illisibles" for x in _journal_chien(r))
    with pytest.raises(GardeArret, match="dépense du poste illisible"):
        inst.ChienDeGarde(r, {"c": 1.0}, LOIN, arreter_api=lambda: None)


# --- B-2 : commande impossible à tuer : attente bornée, puis arrêt du conteneur ---------------------------------------

def test_v11_B2_S2_inverse_commande_impossible_a_tuer_arret_apres_l_attente(tmp_path, monkeypatch):
    r = _racine(tmp_path)
    _battement(r, inst.D_ABANDON_S + 60)
    monkeypatch.setattr(inst, "commandes_en_cours", lambda e: ["pilote"])  # processus en état D
    monkeypatch.setattr(inst, "arreter_groupe", lambda *a, **k: None)
    c, appels, h = _chien(r)
    assert c.passage() is None and appels == []  # sain : l'attente n'est pas échue
    h.decalage += inst.ATTENTE_COMMANDES_MAX_S - 10
    assert c.passage() is None and appels == []
    h.decalage += 20
    assert c.passage() == "conduite injoignable" and appels == ["stopped"]
    e = json.loads((r / "etats" / inst.ETAT_ARRET).read_text())
    assert e["survivantes"] == ["pilote"] and e["arretees"] == ["pilote"]
    assert any(x.get("commandes_survivantes") == ["pilote"] and x.get("attente_bornee") == "échue"
               for x in _journal_chien(r))


def test_v11_B2_borne_en_passages_sans_horloge(tmp_path, monkeypatch):
    r = _racine(tmp_path)
    _battement(r, inst.D_ABANDON_S + 60)
    monkeypatch.setattr(inst, "commandes_en_cours", lambda e: ["mise-en-place"])
    monkeypatch.setattr(inst, "arreter_groupe", lambda *a, **k: None)
    fixe = time.time()
    c, appels, _ = _chien(r, horloge=lambda: fixe)
    assert c.boucle(passages=inst.PASSAGES_ATTENTE_MAX) is None and appels == []
    assert c.boucle(passages=1) == "conduite injoignable" and appels == ["stopped"]


def test_v11_B2_signal_refuse_processus_reel(tmp_path, monkeypatch):
    """Artefact en processus réel : `killpg` refusé (PermissionError) ; le chien n'attend pas sans fin."""
    r = _racine(tmp_path)
    _manifestes(r)
    _execution_sur_instance(tmp_path, r, "pilote", 1, {"k": 3, "graine": an.GRAINE_PILOTE})
    pid = _detachee(r, "pilote", "sleep 60")
    try:
        _battement(r, inst.D_ABANDON_S + 60)

        def refuse(p, s):
            raise PermissionError("refusé")
        monkeypatch.setattr(inst.os, "killpg", refuse)
        c, appels, h = _chien(r)
        assert c.boucle(passages=2) is None and appels == [] and inst.pid_vivant(r / "etats", "pilote") == pid
        h.decalage = inst.ATTENTE_COMMANDES_MAX_S + 1
        assert c.boucle(passages=1) == "conduite injoignable" and appels == ["stopped"]
        e = json.loads((r / "x" / "pilote" / cv.ETAT_EXECUTION).read_text())
        assert e["reconstitue"] is True and e["cause_arret"] == "instance injoignable"  # état reconstitué
        assert json.loads((r / "etats" / inst.ETAT_ARRET).read_text())["survivantes"] == ["pilote"]
    finally:
        monkeypatch.undo()
        _tuer(pid)


# --- P-4 : en-tête du paquet `vastai`, nouveaux essais comme le paquet ------------------------------------------------

class _ApiV11(http.server.BaseHTTPRequestHandler):
    recues: list = []
    statuts: list = []

    def do_PUT(self):
        n = int(self.headers.get("Content-Length") or 0)
        self.rfile.read(n)
        type(self).recues.append({"agent": self.headers.get("User-Agent"), "auth": self.headers.get("Authorization")})
        statut = type(self).statuts.pop(0) if type(self).statuts else 200
        corps = json.dumps({"success": statut == 200}).encode()
        self.send_response(statut)
        if statut == 429:
            self.send_header("Retry-After", "0")
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)

    def log_message(self, *a):
        pass


@pytest.fixture
def api_v11():
    _ApiV11.recues, _ApiV11.statuts = [], []
    s = http.server.HTTPServer(("127.0.0.1", 0), _ApiV11)
    t = threading.Thread(target=s.serve_forever, daemon=True)
    t.start()
    yield f"http://127.0.0.1:{s.server_port}"
    s.shutdown()


def test_v11_P4_user_agent_du_paquet_et_nouveaux_essais(tmp_path, api_v11, monkeypatch):
    monkeypatch.delenv("CONTAINER_ID", raising=False)
    monkeypatch.delenv("CONTAINER_API_KEY", raising=False)
    env = _environ(tmp_path)
    attentes = []
    assert inst.requete_etat_instance("stopped", env, api_v11, attendre=attentes.append)["etat_vise"] == "stopped"
    assert _ApiV11.recues == [{"agent": "vastai-cli/1.11.0", "auth": "Bearer cle-instance-factice"}]  # sain
    _ApiV11.recues, _ApiV11.statuts = [], [503, 429]  # artefact : passerelle, puis limite de débit
    inst.requete_etat_instance("stopped", env, api_v11, attendre=attentes.append)
    assert len(_ApiV11.recues) == 3 and attentes[-2:] == [0.15, 0.0]
    _ApiV11.recues, _ApiV11.statuts = [], [503, 503, 503]
    with pytest.raises(GardeArret, match="HTTPError 503") as err:
        inst.requete_etat_instance("stopped", env, api_v11, attendre=attentes.append)
    assert len(_ApiV11.recues) == inst.ESSAIS_REQUETE and "cle-instance-factice" not in str(err.value)
    _ApiV11.recues, _ApiV11.statuts = [], [404]  # jamais refait
    with pytest.raises(GardeArret, match="HTTPError 404"):
        inst.requete_etat_instance("stopped", env, api_v11, attendre=attentes.append)
    assert len(_ApiV11.recues) == 1


# --- B-3 : reprise, liste des étapes exigée --------------------------------------------------------------------------

def test_v11_B3_S3_inverse_ls_en_echec_aucune_destruction(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    ex = f.executer

    def executer(ident, commande, delai_s=None):
        if commande.startswith("ls -1 /root/x"):
            return 255, ""  # coupure ssh passagère
        return ex(ident, commande, delai_s)
    f.executer = executer
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert b["detruite"] is False and f.detruites == [] and f.arrets == ["77"] and f.etat == "stopped"
    assert "transferts" not in b and b["ls_code"] == 255
    assert any("liste des étapes de l'instance illisible (code 255)" in a for a in b["alertes"])


def test_v11_B3_ls_vide_etapes_du_journal_exigees(tmp_path, monkeypatch):
    """Artefact : `ls` réussit mais ne rend rien, et le dossier du run principal a disparu, alors que le journal de la
    conduite le montre lancé : il est attendu, sans transfert possible : pas de destruction."""
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    shutil.rmtree(f.local("/root/x/principal"))
    ex = f.executer
    f.executer = lambda ident, commande, delai_s=None: (0, "") if commande.startswith("ls -1 /root/x") \
        else ex(ident, commande, delai_s)
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert b["etapes_presentes"] == [] and b["etapes"] == b["etapes_lancees_journal"]
    assert set(b["etapes"]) == {"mise-en-place", "controle-juge", "pilote", "regle", "principal"}
    assert b["transferts"]["principal"].get("foi") is None and b["transferts"]["pilote"]["foi"] == "transfert-1"
    assert b["detruite"] is False and f.detruites == [] and f.arrets == ["77"] and b["etapes_sans_foi"] == ["principal"]
    assert b["transfert_complet"] is False and "pas de destruction" in b["alertes"][0]


def test_v11_B3_union_journal_et_dossiers_et_journal_illisible(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    j = c.sortie / "conduite-v5.jsonl"
    lignes = j.read_text(encoding="utf-8").splitlines()
    lancees = [json.loads(l)["commande"] for l in lignes if json.loads(l).get("lancee") is True]
    assert lancees == ["amorce", "auto-arret", "mise-en-place", "controle-juge", "pilote", "regle", "principal"]
    j.write_text("\n".join(l for l in lignes if json.loads(l).get("commande") != "principal") + "\n{coupée",
                 encoding="utf-8")
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert "principal" not in b["etapes_lancees_journal"] and "principal" in b["etapes"]  # union : dossier présent
    assert b["transferts"]["principal"]["foi"] == "transfert-1" and b["detruite"] is True  # sain
    # artefact : journal de la conduite illisible : rien n'est fait (aucun redémarrage, aucune destruction)
    c2, f2 = _poste_interrompu(tmp_path / "b", monkeypatch)
    (c2.sortie / "conduite-v5.jsonl").unlink()
    b2 = la.Reprise(f2, c2.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert f2.demarrages == [] and f2.detruites == [] and "journal de la conduite" in b2["alertes"][0]


# --- C-1 : veilleur local d'arrêt avant le redémarrage ; remise à l'arrêt ; alerte exacte ----------------------------

def test_v11_C1_sain_veilleur_avant_le_redemarrage_puis_arrete(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    h = Horloge()
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=h).reprendre()
    (v,) = f.veilleurs
    assert v["etat_instance"] == "stopped" and v["demarrages"] == 0 and v["ident"] == "77" and v["etiquette"] == ETIQ
    borne = b["redemarrage"]["borne_veilleur"]
    assert v["echeance"] == borne and abs(borne - (b["debut"] + la.DELAI_PRETE_S + la.DELAI_COMMANDE_S
                                                   + la.MINUTERIE_REPRISE_S)) < 5
    assert b["detruite"] is True and f.veilleurs_arretes == [5001] and b["veilleurs_arret_vivants"] == []
    # échéance du GO plus proche : la borne du veilleur la suit
    c2, f2 = _poste_interrompu(tmp_path / "b", monkeypatch)
    proche = time.time() + 600
    la.Reprise(f2, c2.sortie, ETIQ, proche, attendre=lambda s: None).reprendre()
    assert f2.veilleurs[0]["echeance"] == proche - la.ECART_SECOURS_S  # v12 (V-5) : avancée de l'écart


def test_v11_C1_veilleur_non_vivant_pas_de_redemarrage(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    f.veilleur_vivant = False
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert f.demarrages == [] and f.detruites == [] and f.veilleurs_arretes == [5001]
    assert "veilleur local d'arrêt non lancé ou non vu vivant" in b["alertes"][0]


def test_v11_C1_S4_inverse_non_prete_arret_refuse_alerte_exacte(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    f.executer = lambda ident, commande, delai_s=None: (255, "")  # ssh injoignable, conteneur en marche
    refus = []

    def refuse(ident):
        refus.append(ident)
        raise GardeArret("vastai stop : succès non confirmé")
    f.arreter = refuse
    h = Horloge()
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, delai_prete_s=0, horloge=h).reprendre()
    assert f.etat == "running" and f.minuteries == [] and len(refus) == la.ESSAIS_DESTRUCTION
    assert not any("minuterie posée" in a or "la minuterie de l'instance l'arrête" in a for a in b["alertes"])
    (a,) = [x for x in b["alertes"] if "non remise à l'arrêt" in x]
    assert "aucune minuterie n'a été posée" in a and "PID 5001, 5002" in a
    assert b["remise_a_l_arret"] == {"acceptee": False, "essais_en_echec": 3, "statut_relu": "running"}
    assert len(f.veilleurs) == 2 and abs(f.veilleurs[1]["echeance"] - h()) < 5  # veilleur à échéance immédiate
    assert f.veilleurs_arretes == [] and b["veilleurs_arret_vivants"] == [5001, 5002]


def test_v11_C1_minuterie_posee_alerte_et_arret_confirme(tmp_path, monkeypatch):
    """Minuterie posée, puis `ls` en échec et arrêt refusé : l'alerte nomme la minuterie ; arrêt accepté et statut
    relu « stopped » (sain, P-7) : veilleurs arrêtés, aucune alerte de remise."""
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    ex = f.executer
    f.executer = lambda ident, commande, delai_s=None: (255, "") if commande.startswith("ls -1 /root/x") \
        else ex(ident, commande, delai_s)
    f.arreter = lambda ident: (_ for _ in ()).throw(GardeArret("refus"))
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert len(f.minuteries) == 1
    (a,) = [x for x in b["alertes"] if "non remise à l'arrêt" in x]
    assert "la minuterie posée sur l'instance l'arrête au plus tard" in a
    c2, f2 = _poste_interrompu(tmp_path / "b", monkeypatch)
    ex2 = f2.executer
    f2.executer = lambda ident, commande, delai_s=None: (255, "") if commande.startswith("ls -1 /root/x") \
        else ex2(ident, commande, delai_s)
    b2 = la.Reprise(f2, c2.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert b2["remise_a_l_arret"] == {"acceptee": True, "essais_en_echec": 0, "statut_relu": "stopped"}
    assert f2.veilleurs_arretes == [5001] and len(f2.veilleurs) == 1
    assert not any("non remise" in x or "statut relu" in x for x in b2["alertes"])


def test_v11_C1_fournisseur_inconnu_aucun_veilleur(tmp_path):
    with pytest.raises(GardeArret, match="fournisseur inconnu"):
        la.lancer_veilleur_arret_processus("77", ETIQ, 0.0, tmp_path / "j.jsonl", None)
    r = la.Reprise(la.Fournisseur(), tmp_path, ETIQ, LOIN)
    assert r._spec_veilleur() is None and la.Reprise(la.FournisseurVast(), tmp_path, ETIQ, LOIN)._spec_veilleur() == "vast"


class _FournisseurArret(la.Fournisseur):
    def __init__(self):
        self.etat, self.arrets, self.refus, self.inv, self.statut_leve = "running", [], 0, ["77"], False

    def statut(self, ident):
        if self.statut_leve:
            raise RuntimeError("introuvable")
        return self.etat

    def arreter(self, ident):
        if self.refus:
            self.refus -= 1
            raise GardeArret("refus")
        self.arrets.append(ident)

    def inventaire(self, etiquette):
        return self.inv


def test_v11_C1_veilleur_arret_unitaire(tmp_path):
    f = _FournisseurArret()
    h = Horloge()
    v = la.VeilleurArret(f, "77", ETIQ, time.time() + 100, tmp_path / "v.jsonl", horloge=h, attendre=lambda s: None)
    assert v.boucle(passages=3) is None and f.arrets == []  # sain : avant l'échéance, rien
    assert (tmp_path / "v.jsonl.battement").is_file()
    h.decalage = 101
    f.refus = 2  # artefact : deux refus, retentés
    assert v.boucle(passages=3) is None and f.arrets == ["77"]
    f.etat = "stopped"
    assert v.boucle(passages=1) == "arrêtée"
    f2 = _FournisseurArret()
    f2.statut_leve, f2.inv = True, []
    assert la.VeilleurArret(f2, "77", ETIQ, 0.0, tmp_path / "w.jsonl", attendre=lambda s: None).boucle(1) == "détruite"
    assert f2.arrets == []


def test_v11_C1_veilleur_arret_processus_reel(tmp_path):
    """Processus réel `lanceur_v12 veilleur-arret`, fournisseur « fichier » (aucun réseau) : arrêt à l'échéance,
    puis statut « stopped » relu, fin."""
    spec = f"fichier:{tmp_path / 'f.txt'}"
    p = subprocess.run([sys.executable, "-m", la.VEILLEUR_MODULE, "veilleur-arret", "--instance", "77", "--etiquette",
                        ETIQ, "--echeance", "0", "--journal", str(tmp_path / "v.jsonl"), "--fournisseur", spec,
                        "--periode", "0.1"], env={**os.environ, "PYTHONPATH": str(DEPOT / "src")}, timeout=60)
    assert p.returncode == 0 and (tmp_path / "f.txt.arrets").read_text().split() == ["77"]
    assert not (tmp_path / "f.txt").exists()  # jamais de destruction
    assert json.loads((tmp_path / "v.jsonl").read_text().splitlines()[-1])["fin"] == "instance arrêtée"


# --- C-2 : jamais de destruction d'une instance arrêtée dont une étape n'a pas de transfert qui fait foi --------------

class _FournisseurVeilleur(la.Fournisseur):
    def __init__(self, etat):
        self.etat, self.detruites = etat, []

    def statut(self, ident):
        return self.etat

    def detruire(self, ident):
        self.detruites.append(ident)


def _poste_au_seuil(tmp_path) -> Path:
    p = tmp_path / "poste-v5.json"
    la.Poste(b=B, instances=[{"id": "77", "c": 1.0, "creation": time.time() - (B - 0.4) * 3600,
                              "destruction": None}]).ecrire(p)
    return p


def test_v11_C2_veilleur_instance_arretee_sans_transfert_pas_de_destruction(tmp_path):
    p = _poste_au_seuil(tmp_path)
    f = _FournisseurVeilleur("stopped")
    v = la.Veilleur(f, p, "77", LOIN, tmp_path / "arrets.jsonl", attendre=lambda s: None)
    assert v.boucle(passages=3) == la.REPRISE_REQUISE and f.detruites == []
    assert "reprise requise" in (tmp_path / "arrets.jsonl").read_text()
    f.etat = "exited"
    (tmp_path / la.FICHIER_RAPATRIEMENT).write_text(json.dumps({"complet": False, "sans_foi": ["principal"]}))
    assert la.Veilleur(f, p, "77", LOIN, tmp_path / "a2.jsonl").boucle(passages=1) == la.REPRISE_REQUISE
    assert f.detruites == []


def test_v11_C2_veilleur_sains_destruction(tmp_path):
    p = _poste_au_seuil(tmp_path)
    f = _FournisseurVeilleur("running")  # en marche : la borne de dépense prime
    assert la.Veilleur(f, p, "77", LOIN, tmp_path / "a.jsonl").boucle(passages=1) == "dépense (seuil de secours)"
    assert f.detruites == ["77"]
    p = _poste_au_seuil(tmp_path / "b") if (tmp_path / "b").mkdir() is None else None
    f = _FournisseurVeilleur("stopped")  # arrêtée, transfert qui fait foi : destruction
    (tmp_path / "b" / la.FICHIER_RAPATRIEMENT).write_text(json.dumps({"complet": True, "sans_foi": []}))
    assert la.Veilleur(f, p, "77", LOIN, tmp_path / "b" / "a.jsonl").boucle(passages=1) == "dépense (seuil de secours)"
    assert f.detruites == ["77"]


def test_v11_C2_finir_instance_arretee_par_le_chien_gardee_pour_la_reprise(tmp_path, monkeypatch):
    """Artefact : transferts sans foi et instance « stopped » à la destruction : pas de destruction, veilleur arrêté,
    alerte « reprise requise » ; même conduite, instance en marche (sain, v10) : destruction."""
    c, f, veille = conduite(tmp_path, monkeypatch, reponses())
    # v12 (Q-2) : plus de marque sur un transfert incomplet ; l'instance est vue arrêtée (par son chien, sur une autre
    # cause) une fois le transfert fini
    f.statut = lambda ident: "stopped" if (c.sortie / la.FICHIER_RAPATRIEMENT).exists() else "running"
    bilan = c.conduire()
    assert bilan["marque_rapatrie"] == "non posée : transfert incomplet"
    assert bilan["detruite"] is False and f.detruites == [] and bilan["statut_avant_destruction"] == "stopped"
    assert "reprise requise" in bilan["alerte"] and "principal" in bilan["reprise_requise"]
    assert veille["arretes"] == [4242] and len(veille["lances"]) == 1  # aucun veilleur de destruction
    r = json.loads((c.sortie / la.FICHIER_RAPATRIEMENT).read_text())
    assert r["complet"] is False and "principal" in r["sans_foi"]
    c, f, veille = conduite(tmp_path / "b", monkeypatch, reponses())
    bilan = c.conduire()
    assert bilan["detruite"] is True and f.detruites == ["77"] and bilan["statut_avant_destruction"] == "running"


def test_v11_C2_finir_transfert_complet_instance_arretee_detruite(tmp_path, monkeypatch):
    c, f, _ = conduite_locale(tmp_path, monkeypatch, scenario(21, principal_fini(21)))
    f.statut = lambda ident: "stopped" if any(x.endswith(f"/{inst.MARQUE_RAPATRIE}") for x in f.commandes) \
        else "running"
    bilan = c.conduire()
    assert bilan["transfert_complet"] is True and bilan["detruite"] is True and f.detruites == ["77"]
    assert "statut_avant_destruction" not in bilan
    assert json.loads((c.sortie / la.FICHIER_RAPATRIEMENT).read_text())["complet"] is True


# --- P-1 : la conduite lit le chien à chaque sondage et le relance s'il est mort ---------------------------------------

def test_v11_P1_bash_reel_chien_vivant_ou_mort(tmp_path):
    d = tmp_path / "etats"
    d.mkdir()
    lire = lambda: _bash_local(la.commande_sondage("x"), d).stdout.splitlines()[0]
    assert lire() == "CHIEN MORT"  # aucun chien
    pid = _detachee(tmp_path, inst.CHIEN, "sleep 60")
    try:
        b = d / f"{inst.CHIEN}.battement"
        b.write_text("{}")
        assert lire() == "CHIEN VIVANT"  # sain
        vieux = time.time() - inst.CHIEN_FRAICHEUR_S - 5
        os.utime(b, (vieux, vieux))
        assert lire() == "CHIEN MORT"  # bloqué : battement périmé
        b.touch()
    finally:
        _tuer(pid)
    time.sleep(0.3)
    assert lire() == "CHIEN MORT"  # mort
    assert _bash_local(la.commande_sondage("x"), d).stdout.splitlines()[-1] == "MORT"  # dernière ligne inchangée


class _FacticeChien(FournisseurFactice):
    def __init__(self, reps, chien="mort", relance_ok=True):
        super().__init__(reps)
        self.chien, self.relance_ok, self.relances = chien, relance_ok, []

    def executer(self, ident, commande, delai_s=None):
        if f"rm -f /root/etats/{inst.CHIEN}.fin" in commande:
            self.commandes.append(commande)
            self.relances.append(commande)
            return (0, "LANCE 777\n") if self.relance_ok else (0, "")
        code, sortie = super().executer(ident, commande, delai_s)
        if "CHIEN VIVANT" in commande:
            sortie = f"CHIEN {'MORT' if self.chien == 'mort' else 'VIVANT'}\n" + sortie
        return code, sortie


def test_v11_P1_chien_mort_relance_apres_la_garde_d_auto_arret(tmp_path, monkeypatch):
    f = _FacticeChien(reponses())
    c, _ = _monter(tmp_path, monkeypatch, f)
    bilan = c.conduire()
    assert "arret" not in bilan and f.relances
    i = f.commandes.index(f.relances[0])
    assert all(" auto-arret " not in x for x in f.commandes[i:])  # jamais avant la garde d'auto-arrêt passée
    assert f.lance.index("auto-arret") < f.lance.index("mise-en-place")
    r = f.relances[0]
    assert r.startswith(f"p=$(cat /root/etats/{inst.CHIEN}.pid")  # arrêt par PID (R10) d'abord
    assert f"-m {la.INSTANCE_MODULE} {inst.CHIEN} " in r and '"b": 75.0' in r and "CONTAINER_API_KEY" not in r
    j = [json.loads(l) for l in (c.sortie / "conduite-v5.jsonl").read_text().splitlines()]
    assert any(x.get("chien") == "vu mort" and x.get("relance") == "vérifiée" for x in j)
    assert "alerte_chien" not in bilan
    f = _FacticeChien(reponses(), chien="vivant")  # sain
    c, _ = _monter(tmp_path / "b", monkeypatch, f)
    c.conduire()
    assert f.relances == []


def test_v11_P1_relance_non_verifiee_alerte_au_bilan(tmp_path, monkeypatch):
    f = _FacticeChien(reponses(), relance_ok=False)
    c, _ = _monter(tmp_path, monkeypatch, f)
    bilan = c.conduire()
    assert "arret" not in bilan and len(f.relances) >= la.CHIEN_RELANCES_EN_ECHEC_ALERTE  # le run n'est pas arrêté
    assert "chien de garde vu mort et non relancé" in bilan["alerte_chien"]


# --- P-2 : plafond B dur ; la reprise ne porte jamais la dépense du poste au-delà de B -------------------------------

def test_v11_P2_sain_reprise_bornee_par_le_budget(tmp_path, monkeypatch):
    """Poste : instance « 77 » créée à HORLOGE, c = 1 USD/h, B = 75, non détruite (intervalles arrêtés comptés).
    À HORLOGE + 73,5 h, D = 73,5 : reste 3 600 s jusqu'à B − 0,5 ; redémarrage permis ; veilleur et minuterie bornés
    par cet instant (et non par leurs délais, plus longs)."""
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    t = HORLOGE + 73.5 * 3600
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t).reprendre()
    assert b["detruite"] is True and f.demarrages == ["77"]
    e = la.ECART_SECOURS_S  # v12 (V-5) : bornes avancées de l'écart du veilleur de secours
    assert b["budget"]["D"] == 73.5 and b["budget"]["borne_budget"] == t + 3600 - e
    assert f.veilleurs[0]["echeance"] == t + 3600 - e  # < t + 1 800 + 120 + 3 600
    assert f"--minuterie {repr(3600.0 - e - la.DELAI_COMMANDE_S)}" in f.minuteries[0]
    assert b["minuterie_s"] == 3600.0 - e - la.DELAI_COMMANDE_S
    # loin du plafond : délais inchangés
    c2, f2 = _poste_interrompu(tmp_path / "b", monkeypatch)
    t2 = HORLOGE + 10 * 3600
    la.Reprise(f2, c2.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t2).reprendre()
    assert f2.veilleurs[0]["echeance"] == t2 + la.DELAI_PRETE_S + la.DELAI_COMMANDE_S + la.MINUTERIE_REPRISE_S
    assert "--minuterie 3600.0" in f2.minuteries[0]


def test_v11_P2_artefact_reprise_impossible_dans_le_budget(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    t = HORLOGE + 74.3 * 3600  # reste 720 s < 900 s
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t).reprendre()
    assert f.demarrages == [] and f.veilleurs == [] and f.detruites == [] and f.etat == "stopped"
    assert "reprise impossible dans le budget" in b["alertes"][0] and "nœud" in b["alertes"][0]
    # taux lu maintenant plus haut que le taux relevé : retenu (prudent)
    f.taux_horaire = lambda ident: 2.5
    t = HORLOGE + 74 * 3600  # au taux 1 : 1 800 s ; au taux 2,5 : 720 s
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t).reprendre()
    assert f.demarrages == [] and b["budget"]["taux"] == 2.5 and "reprise impossible dans le budget" in b["alertes"][0]
    # poste illisible : dépense inconnue, pas de redémarrage
    (c.sortie / "poste-v5.json").write_text("{coupé")
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert f.demarrages == [] and "poste de la conduite" in b["alertes"][0]


# ======================================================================================================================
# v12 : relecture du code v11 (`relecture-code-condition6-v11-bailey-v1.md`, `044ba3e2…`) — un cas sain et un artefact
# par correction ; sondes S5 à S9 du relecteur inversées (elles passent sur la v12 et échouent sur la v11)
# ======================================================================================================================

def _journal(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()] if p.exists() else []


def _executer_note(f, appels: list):
    """Enveloppe `f.executer` : chaque commande envoyée est notée dans `appels` (la sonde S8 n'en voit aucune)."""
    ex = f.executer

    def executer(ident, commande, delai_s=None):
        appels.append(commande)
        return ex(ident, commande, delai_s)
    f.executer = executer


# --- V-1 : état voulu lu avec l'état réel ; arrêt accepté exigé ---------------------------------------------------------

def test_v12_V1_statut_vast_lit_l_etat_voulu():
    sv = la.statut_vast
    # sains
    assert sv({"actual_status": "stopped", "intended_status": "stopped"}) == "stopped"
    assert sv({"actual_status": "exited", "intended_status": None}) == "exited"
    assert sv({"actual_status": "stopped"}) == "stopped"
    assert sv({"actual_status": "running", "intended_status": "running"}) == "running"
    assert sv({"actual_status": "loading", "intended_status": "running"}) == "loading"
    # artefacts : redémarrage en attente d'une carte (« scheduling ») ; arrêt demandé mais conteneur en marche
    assert sv({"actual_status": "stopped", "intended_status": "running"}) == la.STATUT_EN_ATTENTE
    assert sv({"actual_status": "exited", "intended_status": "running"}) == la.STATUT_EN_ATTENTE
    assert la.STATUT_EN_ATTENTE not in la.STATUTS_ARRETES
    assert sv({"actual_status": "running", "intended_status": "stopped"}) == la.STATUT_ARRET_EN_COURS
    assert sv({}) is None and sv(None) is None


def test_v12_V1_fournisseur_vast_statut_lit_les_deux(monkeypatch):
    f = la.FournisseurVast()
    reponse = {"actual_status": "stopped", "intended_status": "running"}
    vus = []
    monkeypatch.setattr(f, "_vast", lambda *a: (vus.append(a), json.dumps(reponse))[1])
    assert f.statut("77") == la.STATUT_EN_ATTENTE and vus == [("show", "instance", "77", "--raw")]
    reponse["intended_status"] = "stopped"
    assert f.statut("77") == "stopped"


def test_v12_V1_S5_inverse_veilleur_arret_ne_finit_pas_sans_arret_accepte(tmp_path):
    """S5 inversée : statut « stopped » dès le départ (état réel seul, redémarrage en attente) : le veilleur demande
    l'arrêt, ne finit pas ; sain : il finit au passage suivant (arrêt accepté, puis « stopped » relu)."""
    f = _FournisseurArret()
    f.etat = "stopped"
    v = la.VeilleurArret(f, "77", ETIQ, 0.0, tmp_path / "v.jsonl", attendre=lambda s: None)
    assert v.boucle(passages=1) is None and f.arrets == ["77"] and v.essais == 1 and v.arret_accepte is True
    assert v.boucle(passages=1) == "arrêtée"
    # artefact : arrêt toujours refusé, statut « stopped » : jamais fini, l'arrêt est redemandé à chaque passage
    f2 = _FournisseurArret()
    f2.etat, f2.refus = "stopped", 10 ** 6
    v2 = la.VeilleurArret(f2, "77", ETIQ, 0.0, tmp_path / "w.jsonl", attendre=lambda s: None)
    assert v2.boucle(passages=20) is None and f2.arrets == [] and v2.essais == 20 and v2.arret_accepte is False
    j = _journal(tmp_path / "w.jsonl")
    assert not any("fin" in x for x in j) and sum(1 for x in j if "erreur" in x) == 20


def test_v12_V1_veilleur_arret_processus_reel_stopped_d_entree(tmp_path):
    """Processus réel, fournisseur « fichier » : instance déjà « stopped » à l'échéance : l'arrêt est demandé (ligne au
    fichier des arrêts) avant la fin."""
    spec = f"fichier:{tmp_path / 'f.txt'}"
    (tmp_path / "f.txt.arrets").write_text("77\n")
    p = subprocess.run([sys.executable, "-m", la.VEILLEUR_MODULE, "veilleur-arret", "--instance", "77", "--etiquette",
                        ETIQ, "--echeance", "0", "--journal", str(tmp_path / "v.jsonl"), "--fournisseur", spec,
                        "--periode", "0.1"], env={**os.environ, "PYTHONPATH": str(DEPOT / "src")}, timeout=60)
    assert p.returncode == 0 and (tmp_path / "f.txt.arrets").read_text().split() == ["77", "77"]
    j = _journal(tmp_path / "v.jsonl")
    assert j[0]["arret"] == "demandé et accepté" and j[-1]["fin"] == "instance arrêtée"


def test_v12_V1_S6_inverse_trois_refus_et_stopped_relu_non_confirme(tmp_path, monkeypatch):
    """S6 inversée : redémarrage resté en attente (« stopped » lu), trois arrêts refusés : rien n'est confirmé ;
    veilleur à échéance immédiate, alerte, aucun veilleur arrêté. Sain : arrêt accepté puis « stopped » : confirmé."""
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    f.demarrer = lambda ident: f.demarrages.append(ident)  # reste « stopped »
    refus = []

    def refuse(ident):
        refus.append(ident)
        raise GardeArret("vastai stop : succès non confirmé")
    f.arreter = refuse
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, delai_prete_s=0).reprendre()
    assert len(refus) == la.ESSAIS_DESTRUCTION
    assert b["remise_a_l_arret"] == {"acceptee": False, "essais_en_echec": 3, "statut_relu": "stopped"}
    assert f.veilleurs_arretes == [] and b["veilleurs_arret_vivants"] == [5001, 5002]
    # v13 (P-2) : alerte exacte : arrêt refusé, statut relu arrêté (attendu changé par la v13)
    (a,) = [x for x in b["alertes"] if "arrêt refusé 3 fois, statut relu « stopped »" in x]
    assert not any("non remise à l'arrêt" in x for x in b["alertes"])
    assert "PID 5001, 5002" in a and abs(f.veilleurs[1]["echeance"] - time.time()) < 5
    c2, f2 = _poste_interrompu(tmp_path / "b", monkeypatch)
    f2.demarrer = lambda ident: f2.demarrages.append(ident)
    b2 = la.Reprise(f2, c2.sortie, ETIQ, LOIN, attendre=lambda s: None, delai_prete_s=0).reprendre()
    assert b2["remise_a_l_arret"] == {"acceptee": True, "essais_en_echec": 0, "statut_relu": "stopped"}
    assert f2.veilleurs_arretes == [5001] and b2["veilleurs_arret_vivants"] == []


def test_v12_V1_reprise_instance_en_attente_de_demarrage_remise_a_l_arret(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    f.etat = la.STATUT_EN_ATTENTE
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert f.demarrages == [] and f.arrets == ["77"] and f.detruites == [] and "transferts" not in b
    assert b["remise_a_l_arret"]["acceptee"] is True and any("en attente de démarrage" in a for a in b["alertes"])


# --- V-2 : reprise d'une instance en marche bornée par le budget ------------------------------------------------------

def test_v12_V2_S8_inverse_en_marche_au_dela_de_B_remise_a_l_arret_sans_transfert(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    f.etat = "running"
    appels: list = []
    _executer_note(f, appels)
    t = HORLOGE + 80 * 3600  # D = 80 > B = 75
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t).reprendre()
    assert b["budget"]["D"] == 80.0 and b["budget"]["reste_s"] < 0
    assert appels == [] and "transferts" not in b and f.veilleurs == []  # aucun `executer`, battement non touché
    assert f.arrets == ["77"] and f.detruites == [] and b["detruite"] is False
    assert any("reprise impossible dans le budget" in a and "sans transfert" in a for a in b["alertes"])
    # artefact : poste illisible : dépense inconnue, remise à l'arrêt sans transfert
    c2, f2 = _poste_interrompu(tmp_path / "b", monkeypatch)
    f2.etat = "running"
    (c2.sortie / "poste-v5.json").write_text("{coupé")
    b2 = la.Reprise(f2, c2.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert f2.arrets == ["77"] and "transferts" not in b2 and "poste de la conduite" in b2["alertes"][0]


def test_v12_V2_sain_en_marche_veilleur_avant_le_battement_puis_destruction(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    f.etat = "running"
    ordre: list = []
    _executer_note(f, ordre)
    vrai_lancer = la.lancer_veilleur_arret_processus

    def lancer(*a):
        ordre.append(("veilleur", a[2]))
        return vrai_lancer(*a)
    monkeypatch.setattr(la, "lancer_veilleur_arret_processus", lancer)
    t = HORLOGE + 10 * 3600
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t).reprendre()
    i_v = next(i for i, x in enumerate(ordre) if isinstance(x, tuple))
    i_b = next(i for i, x in enumerate(ordre) if isinstance(x, str) and x.endswith(f"/{inst.BATTEMENT_CONDUITE}"))
    assert i_v < i_b and b["budget"]["D"] == 10.0
    assert f.veilleurs[0]["echeance"] == t + la.DELAI_COMMANDE_S + la.MINUTERIE_REPRISE_S
    assert b["detruite"] is True and f.detruites == ["77"] and f.veilleurs_arretes == [5001]
    assert f.demarrages == [] and f.minuteries == [] and b["transfert_complet"] is True
    # près du plafond : veilleur borné par le budget (moins l'écart du veilleur de secours)
    c2, f2 = _poste_interrompu(tmp_path / "b", monkeypatch)
    f2.etat = "running"
    t2 = HORLOGE + 73.5 * 3600
    b2 = la.Reprise(f2, c2.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t2).reprendre()
    assert f2.veilleurs[0]["echeance"] == t2 + 3600 - la.ECART_SECOURS_S and b2["detruite"] is True


def test_v12_V2_en_marche_veilleur_non_vivant_ou_commande_en_cours(tmp_path, monkeypatch):
    # artefact : veilleur non vu vivant : aucun transfert, battement non touché, remise à l'arrêt
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    f.etat, f.veilleur_vivant = "running", False
    appels: list = []
    _executer_note(f, appels)
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert "transferts" not in b and f.arrets == ["77"] and f.detruites == []
    assert not any(x.endswith(f"/{inst.BATTEMENT_CONDUITE}") for x in appels)
    assert any("veilleur local d'arrêt non lancé ou non vu vivant" in a and "sans transfert" in a
               for a in b["alertes"])
    # commande en cours : rien n'est fait, mais un veilleur borné par le budget et l'échéance seuls est laissé
    c2, f2 = _poste_interrompu(tmp_path / "b", monkeypatch)
    f2.etat, f2.en_cours = "running", ["principal"]
    t = HORLOGE + 73.5 * 3600
    b2 = la.Reprise(f2, c2.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t).reprendre()
    assert "commande en cours" in b2["issue"] and f2.arrets == [] and f2.detruites == []
    assert f2.veilleurs[0]["echeance"] == t + 3600 - la.ECART_SECOURS_S and f2.veilleurs_arretes == []
    assert b2["veilleurs_arret_vivants"] == [5001]


# --- V-3 : l'observation du chien ne bloque jamais les causes calculées en mémoire -------------------------------------

def test_v12_V3_S9_inverse_fin_prevue_en_EIO_arret_sur_la_depense(tmp_path, monkeypatch):
    r = _racine(tmp_path)
    _battement(r, inst.D_ABANDON_S + 60)

    def eio(racine):
        raise OSError(errno.EIO, "Input/output error")
    monkeypatch.setattr(inst, "fin_prevue", eio)
    c, appels, h = _chien(r, depense=_depense(B + 5))
    assert c.passage() == "dépense" and appels == ["stopped"]
    assert any(x.get("observation") == "fin prévue illisible" and x.get("erreur") == "OSError"
               for x in _journal_chien(r))
    # sain : même erreur, dépense basse, conduite vivante : rien
    r2 = _racine(tmp_path / "b")
    _battement(r2, 10)
    c2, appels2, _ = _chien(r2)
    assert c2.boucle(passages=3) is None and appels2 == [] and c2.cause is None


def test_v12_V3_observation_qui_leve_decision_sur_depense_echeance_battement(tmp_path):
    def leve():
        raise OSError(errno.EIO, "Input/output error")
    # artefact : dépense au seuil du veilleur, conduite vivante
    r = _racine(tmp_path)
    _battement(r, 10)
    c, appels, _ = _chien(r, depense=_depense(B))
    c.observer = leve
    assert c.passage() == "dépense" and appels == ["stopped"]
    assert any(x.get("observation") == "en échec" for x in _journal_chien(r))
    # artefact : échéance du GO (moins la moitié de la marge) atteinte
    r3 = _racine(tmp_path / "c")
    _battement(r3, 10)
    c3, appels3, _ = _chien(r3, echeance=time.time() + 100)
    c3.observer = leve
    assert c3.passage() == "échéance du GO" and appels3 == ["stopped"]
    # artefact : conduite injoignable, aucune autre cause : arrêt (aucune commande tenue pour en cours)
    r4 = _racine(tmp_path / "d")
    _battement(r4, inst.D_ABANDON_S + 60)
    c4, appels4, _ = _chien(r4)
    c4.observer = leve
    assert c4.passage() == "conduite injoignable" and appels4 == ["stopped"]
    # sain : dépense basse, échéance lointaine, conduite vivante : rien
    r2 = _racine(tmp_path / "b")
    _battement(r2, 10)
    c2, appels2, _ = _chien(r2)
    c2.observer = leve
    assert c2.boucle(passages=3) is None and appels2 == [] and c2.cause is None


# --- V-4 : veilleur de secours, statut relu ; destruction après trois lectures illisibles de suite --------------------

def test_v12_V4_S7_inverse_statut_illisible_une_fois_relu_pas_de_destruction(tmp_path):
    p = _poste_au_seuil(tmp_path)

    class F(_FournisseurVeilleur):
        n = 0

        def statut(self, ident):
            F.n += 1
            if F.n == 1:
                raise RuntimeError("429")
            return self.etat
    f = F("stopped")
    v = la.Veilleur(f, p, "77", LOIN, tmp_path / "a.jsonl", attendre=lambda s: None)
    assert v.boucle(passages=3) == la.REPRISE_REQUISE and f.detruites == []
    assert any(x.get("statut") == "illisible" and x.get("lectures_illisibles") == 1
               for x in _journal(tmp_path / "a.jsonl"))


def test_v12_V4_trois_lectures_illisibles_de_suite_puis_destruction(tmp_path):
    p = _poste_au_seuil(tmp_path)

    class F(_FournisseurVeilleur):
        def statut(self, ident):
            raise RuntimeError("coupure")
    f = F("stopped")
    v = la.Veilleur(f, p, "77", LOIN, tmp_path / "a.jsonl", attendre=lambda s: None)
    assert v.boucle(passages=la.ESSAIS_DESTRUCTION - 1) is None and f.detruites == []
    assert v.boucle(passages=1) == "dépense (seuil de secours)" and f.detruites == ["77"]
    # une lecture lisible remet le compte à zéro (destruction refusée par l'API entre-temps)
    suite = iter([RuntimeError("1"), RuntimeError("2"), "running", RuntimeError("3"), RuntimeError("4"),
                  RuntimeError("5")])

    class G(_FournisseurVeilleur):
        refus = True

        def statut(self, ident):
            x = next(suite)
            if isinstance(x, Exception):
                raise x
            return x

        def detruire(self, ident):
            if G.refus:
                G.refus = False
                raise GardeArret("refus")
            self.detruites.append(ident)
    q = tmp_path / "b"
    q.mkdir()
    g = G("running")
    v = la.Veilleur(g, _poste_au_seuil(q), "77", LOIN, q / "a.jsonl", attendre=lambda s: None)
    assert v.boucle(passages=5) is None and g.detruites == []  # 2 illisibles, lisible (refus), 2 illisibles
    assert v.boucle(passages=1) == "dépense (seuil de secours)" and g.detruites == ["77"]


# --- V-5 : la reprise s'arrête avant le seuil du veilleur de secours ---------------------------------------------------

def test_v12_V5_bornes_avancees_de_l_ecart_du_veilleur_de_secours(tmp_path, monkeypatch):
    assert la.ECART_SECOURS_S == 2 * la.PERIODE_VEILLEUR_SECOURS_S + 120.0
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    poste = la.Poste.lire(c.sortie / "poste-v5.json")
    t = HORLOGE + 73.5 * 3600
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t).reprendre()
    borne, seuil = b["budget"]["borne_budget"], b["budget"]["seuil_secours"]
    assert seuil == t + 3600 and borne == seuil - la.ECART_SECOURS_S == f.veilleurs[0]["echeance"]
    v = la.Veilleur(la.Fournisseur(), c.sortie / "poste-v5.json", "77", LOIN, tmp_path / "s.jsonl")
    assert v.verifier(poste=poste) is None  # sain : le veilleur de secours n'agit pas avant la borne de la reprise
    v.horloge = lambda: borne + la.ECART_SECOURS_S
    assert v.verifier(poste=poste) == "dépense (seuil de secours)"  # il n'agit qu'au seuil, écart plus tard
    v.horloge = lambda: borne
    assert v.verifier(poste=poste) is None
    # artefact : échéance du GO dans l'écart : aucun redémarrage
    c2, f2 = _poste_interrompu(tmp_path / "b", monkeypatch)
    b2 = la.Reprise(f2, c2.sortie, ETIQ, time.time() + la.ECART_SECOURS_S / 2, attendre=lambda s: None).reprendre()
    assert f2.demarrages == [] and f2.veilleurs == [] and "échéance du GO passée" in b2["alertes"][0]


# --- Q-1 : destruction de la reprise écrite au poste ------------------------------------------------------------------

def test_v12_Q1_destruction_de_la_reprise_ecrite_au_poste(tmp_path, monkeypatch):
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    (i,) = [x for x in la.Poste.lire(c.sortie / "poste-v5.json").instances if x["id"] == "77"]
    assert b["detruite"] is True and i["destruction"] == b["destruction"] and b["poste_mis_a_jour"] is True
    g = _FournisseurVeilleur("running")
    v = la.Veilleur(g, c.sortie / "poste-v5.json", "77", LOIN, tmp_path / "s.jsonl", attendre=lambda s: None)
    assert v.deja_detruite() is True and v.boucle(passages=1) is None and g.detruites == []
    # artefact : poste non écrit : alerte, destruction faite quand même
    c2, f2 = _poste_interrompu(tmp_path / "b", monkeypatch)

    def refuse(self, chemin):
        raise OSError(errno.ENOSPC, "No space left on device")
    monkeypatch.setattr(la.Poste, "ecrire", refuse)
    b2 = la.Reprise(f2, c2.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert b2["detruite"] is True and b2["poste_mis_a_jour"] == "non (OSError)"
    assert any("destruction non écrite dans poste-v5.json" in a for a in b2["alertes"])


# --- Q-4 : écriture atomique (empreintes, état reconstitué, état de l'arrêt) ------------------------------------------

def test_v12_Q4_ecriture_atomique_temporaire_propre_au_processus(tmp_path, monkeypatch):
    f = tmp_path / "e.json"
    inst._ecrire_json(f, {"a": 1})
    assert json.loads(f.read_text()) == {"a": 1} and sorted(tmp_path.iterdir()) == [f]  # sain : aucun temporaire
    vus = []

    def coupe(src, dst):
        vus.append(str(src))
        raise OSError(errno.EIO, "coupé")
    monkeypatch.setattr(inst.os, "replace", coupe)
    with pytest.raises(OSError):
        inst._ecrire_json(f, {"a": 2})
    assert vus == [f"{f}.tmp-{os.getpid()}"]
    assert json.loads(f.read_text()) == {"a": 1} and sorted(tmp_path.iterdir()) == [f]  # entier ; temporaire effacé
    monkeypatch.undo()
    x = tmp_path / "x"
    x.mkdir()
    (x / cv.ETAT_EXECUTION).write_text("{}")
    assert set(inst.empreintes(x)) == {cv.ETAT_EXECUTION} and (x / cv.EMPREINTES_INSTANCE).is_file()
    assert not [p for p in x.iterdir() if ".tmp" in p.name]


# ======================================================================================================================
# v13 : relecture du code v12 (`relecture-code-condition6-v12-bailey-v1.md`, `3865961f…`) — un cas sain et un artefact
# par point (W-1, P-1 à P-4) ; sondes S10 à S13 du relecteur réécrites en essais inversés (elles passent sur la v13 et
# échouent sur la v12)
# ======================================================================================================================

SORTI_VOULU_EN_MARCHE = {"actual_status": "exited", "intended_status": "running"}


class _FournisseurSorti(_FournisseurVeilleur):
    """Conteneur sorti (repli du chien au PID 1, ou plantage) dont l'état voulu reste « running » ; un arrêt accepté
    fait passer l'état voulu à « stopped » (statut « exited ») si `effet` ; `refus` : arrêts refusés."""

    def __init__(self, effet=True, refus=0):
        super().__init__("ignoré")
        self.voulu, self.effet, self.refus, self.arrets = "running", effet, refus, []

    def statut(self, ident):
        return la.statut_vast({"actual_status": "exited", "intended_status": self.voulu})

    def arreter(self, ident):
        if self.refus:
            self.refus -= 1
            raise GardeArret("vastai stop : succès non confirmé")
        self.arrets.append(ident)
        if self.effet:
            self.voulu = "stopped"


# --- W-1 : conteneur sorti voulu en marche : arrêt par identifiant, relecture, gardé ; jamais détruit d'emblée --------

def test_v13_W1_S10_inverse_secours_arrete_puis_garde_le_conteneur_sorti(tmp_path):
    """S10 inversée : « exited » voulu « running » au seuil, sans transfert : arrêt demandé par l'identifiant, statut
    relu au passage suivant (« exited », voulu arrêté) : gardé, « reprise requise », aucune destruction."""
    assert la.statut_vast(SORTI_VOULU_EN_MARCHE) == la.STATUT_EN_ATTENTE
    p = _poste_au_seuil(tmp_path)
    f = _FournisseurSorti()
    v = la.Veilleur(f, p, "77", LOIN, tmp_path / "a.jsonl", attendre=lambda s: None)
    assert v.boucle(passages=3) == la.REPRISE_REQUISE
    assert f.detruites == [] and f.arrets == ["77"]
    j = _journal(tmp_path / "a.jsonl")
    assert j[0]["arret_demande"] == "accepté" and j[-1]["alerte"] == "reprise requise"


def test_v13_W1_secours_destruction_seulement_apres_relecture_ou_trois_refus(tmp_path):
    # artefact : arrêt accepté, statut toujours non arrêté au passage suivant : destruction (la borne prime)
    p = _poste_au_seuil(tmp_path)
    f = _FournisseurSorti(effet=False)
    v = la.Veilleur(f, p, "77", LOIN, tmp_path / "a.jsonl", attendre=lambda s: None)
    assert v.boucle(passages=1) is None and f.detruites == [] and f.arrets == ["77"]
    assert v.boucle(passages=1) == "dépense (seuil de secours)" and f.detruites == ["77"]
    # artefact : arrêts refusés : destruction au troisième refus, pas avant
    q = tmp_path / "b"
    q.mkdir()
    g = _FournisseurSorti(refus=10)
    w = la.Veilleur(g, _poste_au_seuil(q), "77", LOIN, q / "a.jsonl", attendre=lambda s: None)
    assert w.boucle(passages=la.ESSAIS_DESTRUCTION - 1) is None and g.detruites == []
    assert w.boucle(passages=1) == "dépense (seuil de secours)" and g.detruites == ["77"] and g.arrets == []
    assert any("destruction après 3 arrêts refusés" in x.get("suite", "") for x in _journal(q / "a.jsonl"))
    # sain : transfert complet : destruction d'emblée, sans arrêt (journaux transférés)
    r = tmp_path / "c"
    r.mkdir()
    (r / la.FICHIER_RAPATRIEMENT).write_text(json.dumps({"complet": True, "sans_foi": []}))
    h = _FournisseurSorti()
    assert la.Veilleur(h, _poste_au_seuil(r), "77", LOIN, r / "a.jsonl").boucle(passages=1) == \
        "dépense (seuil de secours)"
    assert h.detruites == ["77"] and h.arrets == []
    # sain : en marche, sans transfert : destruction d'emblée (inchangé)
    s_ = tmp_path / "d"
    s_.mkdir()
    k = _FournisseurVeilleur("running")
    assert la.Veilleur(k, _poste_au_seuil(s_), "77", LOIN, s_ / "a.jsonl").boucle(passages=1) == \
        "dépense (seuil de secours)" and k.detruites == ["77"]


def _conduite_sortie(tmp_path, monkeypatch, effet=True, refus=0, initial=la.STATUT_EN_ATTENTE):
    """Conduite dont le transfert est incomplet ; une fois le transfert fini, l'instance est lue `initial`."""
    c, f, veille = conduite(tmp_path, monkeypatch, reponses())
    etat = {"voulu": None, "refus": refus}
    f.arrets = []

    def statut(ident):
        if not (c.sortie / la.FICHIER_RAPATRIEMENT).exists():
            return "running"
        return "exited" if etat["voulu"] == "stopped" else initial

    def arreter(ident):
        if etat["refus"]:
            etat["refus"] -= 1
            raise GardeArret("refus")
        f.arrets.append(ident)
        if effet:
            etat["voulu"] = "stopped"
    f.statut, f.arreter = statut, arreter
    return c, f, veille


def test_v13_W1_finir_conteneur_sorti_arrete_puis_garde(tmp_path, monkeypatch):
    """`_finir`, transfert incomplet, instance « en attente de démarrage » (conteneur sorti) : arrêt par l'identifiant,
    statut relu : gardée, « reprise requise », veilleur de secours arrêté ; aucune destruction."""
    c, f, veille = _conduite_sortie(tmp_path, monkeypatch)
    bilan = c.conduire()
    assert bilan["detruite"] is False and f.detruites == [] and f.arrets == ["77"]
    assert bilan["statut_avant_destruction"] == "exited" and "reprise requise" in bilan["alerte"]
    assert bilan["arret_avant_destruction"] == {"statut_lu": la.STATUT_EN_ATTENTE, "arret_demande": True,
                                                "acceptee": True, "essais_en_echec": 0, "statut_relu": "exited"}
    assert veille["arretes"] == [4242] and "`lanceur_v21 reprendre`" in bilan["alerte"]


def test_v13_W1_finir_destruction_si_toujours_non_arretee_ou_trois_refus(tmp_path, monkeypatch):
    # artefact : arrêt accepté, statut toujours en attente : destruction
    c, f, _ = _conduite_sortie(tmp_path, monkeypatch, effet=False)
    bilan = c.conduire()
    assert bilan["detruite"] is True and f.detruites == ["77"] and f.arrets == ["77"]
    assert bilan["statut_avant_destruction"] == la.STATUT_EN_ATTENTE
    # artefact : trois refus : destruction sans relecture
    c2, f2, _ = _conduite_sortie(tmp_path / "b", monkeypatch, refus=10)
    b2 = c2.conduire()
    assert b2["detruite"] is True and f2.detruites == ["77"] and f2.arrets == []
    assert b2["arret_avant_destruction"]["acceptee"] is False and b2["arret_avant_destruction"]["essais_en_echec"] == 3
    assert b2["statut_avant_destruction"] is None
    # sain : en marche : destruction d'emblée, aucun arrêt
    c3, f3, _ = _conduite_sortie(tmp_path / "c", monkeypatch, initial="running")
    b3 = c3.conduire()
    assert b3["detruite"] is True and f3.arrets == [] and "arret_avant_destruction" not in b3


# --- P-1 : « arrêt en cours » relu une fois avant toute destruction ---------------------------------------------------

def _s11(tmp_path, effet_s):
    """Scénario de la sonde S11 : arrêt accepté à borne + 150 s ; le veilleur de secours lit au seuil."""
    borne = 1_000_000.0
    seuil = borne + la.ECART_SECOURS_S
    h = {"t": borne - 0.001}
    etat = {"voulu": "running", "reel": "running", "accepte_a": None}

    class F(la.Fournisseur):
        detruites: list = []

        def statut(self, ident):
            if etat["accepte_a"] is not None and h["t"] >= etat["accepte_a"] + effet_s:
                etat["reel"] = "stopped"
            return la.statut_vast({"actual_status": etat["reel"], "intended_status": etat["voulu"]})

        def arreter(self, ident):
            h["t"] += 120.0
            etat["voulu"], etat["accepte_a"] = "stopped", h["t"]

        def detruire(self, ident):
            F.detruites.append(ident)
    F.detruites = []
    f = F()
    va = la.VeilleurArret(f, "77", ETIQ, borne, tmp_path / "va.jsonl", horloge=lambda: h["t"],
                          attendre=lambda s: None)
    assert va._passage() is None
    h["t"] = borne + 29.999
    va._passage()
    p = tmp_path / "poste-v5.json"
    la.Poste(b=B, instances=[{"id": "77", "c": 1.0, "creation": seuil - (B - la.MARGE_SECOURS_USD) * 3600,
                              "destruction": None}]).ecrire(p)
    h["t"] = seuil
    vs = la.Veilleur(f, p, "77", LOIN, tmp_path / "vs.jsonl", horloge=lambda: h["t"], attendre=lambda s: None)
    return f, F, vs, h, seuil


def test_v13_P1_S11_inverse_arret_en_cours_relu_puis_garde(tmp_path):
    f, F, vs, h, seuil = _s11(tmp_path, effet_s=31.0)
    assert f.statut("77") == la.STATUT_ARRET_EN_COURS
    assert vs._passage() is None and F.detruites == []  # relu au passage suivant
    h["t"] = seuil + la.PERIODE_VEILLEUR_SECOURS_S
    assert vs._passage() == la.REPRISE_REQUISE and F.detruites == []


def test_v13_P1_arret_en_cours_toujours_au_passage_suivant_destruction(tmp_path):
    f, F, vs, h, seuil = _s11(tmp_path, effet_s=600.0)
    assert vs._passage() is None and F.detruites == []
    h["t"] = seuil + la.PERIODE_VEILLEUR_SECOURS_S
    assert vs._passage() == "dépense (seuil de secours)" and F.detruites == ["77"]


def test_v13_P1_finir_arret_en_cours_relu_sans_nouvel_arret(tmp_path, monkeypatch):
    c, f, _ = _conduite_sortie(tmp_path, monkeypatch, initial=la.STATUT_ARRET_EN_COURS)
    lus = []
    vrai = f.statut

    def statut(ident):  # première lecture après le transfert : « arrêt en cours » ; relecture : « stopped »
        x = vrai(ident)
        if x == "running":
            return x
        lus.append(x)
        return x if len(lus) == 1 else "stopped"
    f.statut = statut
    bilan = c.conduire()
    assert bilan["detruite"] is False and f.arrets == [] and bilan["statut_avant_destruction"] == "stopped"
    assert bilan["arret_avant_destruction"]["arret_demande"] is False
    c2, f2, _ = _conduite_sortie(tmp_path / "b", monkeypatch, initial=la.STATUT_ARRET_EN_COURS)
    b2 = c2.conduire()  # artefact : toujours « arrêt en cours » : destruction
    assert b2["detruite"] is True and f2.arrets == [] and b2["statut_avant_destruction"] == la.STATUT_ARRET_EN_COURS


# --- P-2 : veilleurs d'arrêt des reprises précédentes arrêtés par leur PID avant toute nouvelle reprise -------------

def _reprise_precedente_avec_veilleur(tmp_path, monkeypatch):
    """Première reprise : commande en cours, veilleur 5001 laissé (borné par le budget) ; puis la commande finit et
    l'instance s'arrête."""
    c, f = _poste_interrompu(tmp_path, monkeypatch)
    f.etat, f.en_cours = "running", ["principal"]
    b1 = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
    assert b1["veilleurs_arret_vivants"] == [5001]
    f.etat, f.en_cours = "stopped", []
    return c, f


def test_v13_P2_S12_inverse_veilleur_precedent_arrete_avant_le_redemarrage(tmp_path, monkeypatch):
    c, f = _reprise_precedente_avec_veilleur(tmp_path, monkeypatch)
    journal = str(c.sortie / "reprise-v10" / "veilleur-arret-v11.jsonl")
    vus = []
    ident = lambda pid, j: (vus.append((pid, j)), pid == 5001 and j == journal and 5001 not in f.veilleurs_arretes)[1]
    ordre = []
    f.demarrer = lambda i: (ordre.append(list(f.veilleurs_arretes)), f.demarrages.append(i),
                            setattr(f, "etat", "running"))
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, identite_veilleur=ident).reprendre()
    assert ordre == [[5001]]  # arrêté par son PID avant `demarrer`
    assert b["veilleurs_precedents"] == [{"pid": 5001, "journal": journal, "issue": "arrêté par son PID (R10)"}]
    assert b["detruite"] is True and f.detruites == ["77"]


def test_v13_P2_veilleur_precedent_encore_vivant_ou_pid_reemploye(tmp_path, monkeypatch):
    # artefact : encore vivant après le signal : ni redémarrage, ni dépense ; le veilleur de cette reprise est arrêté
    c, f = _reprise_precedente_avec_veilleur(tmp_path, monkeypatch)
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None,
                   identite_veilleur=lambda pid, j: pid == 5001).reprendre()
    assert f.demarrages == [] and f.detruites == [] and f.veilleurs_arretes == [5001, 5002]
    assert b["veilleurs_precedents"][0]["issue"] == "encore vivant après SIGTERM"
    assert any("veilleur d'arrêt d'une reprise précédente non arrêté (PID 5001" in a for a in b["alertes"])
    # artefact : PID réemployé par un autre processus : jamais signalé ; la reprise suit
    c2, f2 = _reprise_precedente_avec_veilleur(tmp_path / "b", monkeypatch)
    b2 = la.Reprise(f2, c2.sortie, ETIQ, LOIN, attendre=lambda s: None,
                    identite_veilleur=lambda pid, j: False).reprendre()
    assert 5001 not in f2.veilleurs_arretes and f2.demarrages == ["77"] and b2["detruite"] is True
    assert b2["veilleurs_precedents"][0]["issue"].startswith("fini, ou PID d'un autre processus")
    # artefact : identité illisible : non signalé, pas de redémarrage
    c3, f3 = _reprise_precedente_avec_veilleur(tmp_path / "c", monkeypatch)
    b3 = la.Reprise(f3, c3.sortie, ETIQ, LOIN, attendre=lambda s: None,
                    identite_veilleur=lambda pid, j: None if pid == 5001 else False).reprendre()
    assert f3.demarrages == [] and 5001 not in f3.veilleurs_arretes
    assert b3["veilleurs_precedents"][0]["issue"] == "identité illisible : non signalé"


def test_v13_P2_processus_reels_veilleur_arrete_autre_pid_jamais_signale(tmp_path, monkeypatch):
    """Processus réels : un veilleur d'arrêt (fournisseur « fichier », échéance lointaine) d'une reprise précédente
    est arrêté par son PID ; un autre processus nommé au bilan (PID réemployé) n'est jamais signalé."""
    monkeypatch.setenv("PYTHONPATH", str(DEPOT / "src"))
    sortie = tmp_path / "sortie"
    prec = sortie / "reprise-v10"
    prec.mkdir(parents=True)
    pid = la.lancer_veilleur_arret_processus("77", ETIQ, LOIN, prec / "veilleur-arret-v11.jsonl",
                                             f"fichier:{tmp_path / 'f.txt'}", 0.1)
    autre = subprocess.Popen(["sleep", "60"])
    try:
        assert la.verifier_veilleur(pid, prec / "veilleur-arret-v11.jsonl", delai_s=30)
        (prec / "bilan-reprise-v10.json").write_text(json.dumps({"veilleurs_arret": [
            {"pid": pid, "journal": "veilleur-arret-v11.jsonl"},
            {"pid": autre.pid, "journal": "veilleur-arret-v11-2.jsonl"}], "veilleurs_arret_vivants": [pid]}))
        assert la.identite_veilleur_arret(pid, prec / "veilleur-arret-v11.jsonl") is True
        assert la.identite_veilleur_arret(pid, prec / "autre.jsonl") is False
        r = la.Reprise(la.Fournisseur(), sortie, ETIQ, LOIN)
        r.bilan = {}
        assert r._arreter_veilleurs_precedents(sortie / "reprise-v10-2") is True
        fin = time.time() + 5  # v15 (R-7) : /proc/<pid>/cmdline se vide avant que le processus soit récoltable
        while la.processus_vivant(pid) and time.time() < fin:
            time.sleep(0.05)
        assert not la.processus_vivant(pid) and autre.poll() is None  # l'autre vit : jamais signalé
        issues = {x["pid"]: x["issue"] for x in r.bilan["veilleurs_precedents"]}
        assert issues == {pid: "arrêté par son PID (R10)", autre.pid: "fini, ou PID d'un autre processus : non signalé"}
        assert not (tmp_path / "f.txt.arrets").exists()  # aucun arrêt demandé (échéance lointaine)
    finally:
        autre.kill()
        autre.wait()
        if la.processus_vivant(pid):
            la.arreter_veilleur(pid)


def test_v13_P2_alerte_exacte_remise_a_l_arret(tmp_path, monkeypatch):
    """Sain : arrêt refusé, statut relu « stopped » : « arrêt refusé 3 fois, statut relu « stopped » » ; artefact :
    statut relu en marche : « non remise à l'arrêt »."""
    for etat, attendu in (("stopped", "arrêt refusé 3 fois, statut relu « stopped »"),
                          ("running", "instance non remise à l'arrêt après 3 essais")):
        c, f = _poste_interrompu(tmp_path / etat, monkeypatch)
        f.etat = la.STATUT_EN_ATTENTE
        f.arreter = lambda ident: (_ for _ in ()).throw(GardeArret("refus"))
        f.statut = (lambda e: (lambda ident, n=[0]: (n.__setitem__(0, n[0] + 1),
                                                    la.STATUT_EN_ATTENTE if n[0] == 1 else e)[1]))(etat)
        b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None).reprendre()
        assert any(attendu in a for a in b["alertes"]), b["alertes"]


# --- P-3 : `Poste.ecrire` et `_ecrire_rapatriement` : temporaire propre au processus, `fsync` -------------------------

def test_v13_P3_S13_inverse_temporaire_propre_au_processus(tmp_path, monkeypatch):
    vus, syncs = [], []
    vrai, vrai_sync = os.replace, os.fsync
    monkeypatch.setattr(la.os, "replace", lambda a, b: (vus.append(str(a)), vrai(a, b)))
    monkeypatch.setattr(la.os, "fsync", lambda fd: (syncs.append(fd), vrai_sync(fd)))
    p = tmp_path / "poste-v5.json"
    for pid in (111, 222):
        monkeypatch.setattr(la.os, "getpid", lambda pid=pid: pid)
        la.Poste(b=B, instances=[]).ecrire(p)
    assert vus == [f"{p}.tmp-111", f"{p}.tmp-222"] and len(syncs) == 2
    assert sorted(x.name for x in tmp_path.iterdir()) == ["poste-v5.json"]
    import types
    monkeypatch.setattr(la.os, "getpid", lambda: 333)
    ns = types.SimpleNamespace(sortie=tmp_path, lances=set(), horloge=lambda: 0.0)
    bilan: dict = {"transferts": {}}
    assert la.Conduite._ecrire_rapatriement(ns, bilan) == (True, [])
    assert vus[-1] == str(tmp_path / f"{la.FICHIER_RAPATRIEMENT}.tmp-333") and len(syncs) == 3
    assert json.loads((tmp_path / la.FICHIER_RAPATRIEMENT).read_text())["complet"] is True


def test_v13_P3_ecriture_coupee_original_entier_temporaire_efface(tmp_path, monkeypatch):
    p = tmp_path / "poste-v5.json"
    la.Poste(b=B, instances=[]).ecrire(p)

    def coupe(a, b):
        raise OSError(errno.EIO, "coupé")
    monkeypatch.setattr(la.os, "replace", coupe)
    with pytest.raises(OSError):
        la.Poste(b=1.0, instances=[]).ecrire(p)
    assert la.Poste.lire(p).b == B and sorted(x.name for x in tmp_path.iterdir()) == ["poste-v5.json"]
    import types
    ns = types.SimpleNamespace(sortie=tmp_path, lances=set(), horloge=lambda: 0.0)
    bilan: dict = {"transferts": {}}
    la.Conduite._ecrire_rapatriement(ns, bilan)
    assert bilan["rapatriement_fichier_erreur"] == "OSError" and not (tmp_path / la.FICHIER_RAPATRIEMENT).exists()
    assert sorted(x.name for x in tmp_path.iterdir()) == ["poste-v5.json"]


# --- P-4 : statut autre : un veilleur d'arrêt borné par le budget et l'échéance est laissé ----------------------------

def test_v13_P4_statut_autre_veilleur_borne_laisse(tmp_path, monkeypatch):
    t = HORLOGE + 73.5 * 3600
    for statut in ("loading", la.STATUT_ARRET_EN_COURS, None):
        c, f = _poste_interrompu(tmp_path / str(statut), monkeypatch)
        f.etat = statut
        b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t).reprendre()
        assert f.demarrages == [] and f.arrets == [] and f.detruites == [] and "transferts" not in b
        assert f.veilleurs[0]["echeance"] == t + 3600 - la.ECART_SECOURS_S  # borne de budget (avant l'échéance)
        assert b["veilleurs_arret_vivants"] == [5001] and b["veilleur_budget"]["pid"] == 5001
        assert any(f"statut « {statut} »" in a and "veilleur local d'arrêt (PID 5001) laissé" in a
                   for a in b["alertes"])
    # artefact : poste illisible : borne immédiate ; échéance passée : borne à l'échéance (déjà passée)
    c, f = _poste_interrompu(tmp_path / "x", monkeypatch)
    f.etat = "offline"
    (c.sortie / "poste-v5.json").write_text("{coupé")
    b = la.Reprise(f, c.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t).reprendre()
    assert f.veilleurs[0]["echeance"] == t and any("borne immédiate" in a for a in b["alertes"])
    c2, f2 = _poste_interrompu(tmp_path / "y", monkeypatch)
    f2.etat = "unknown"
    proche = t + 10
    la.Reprise(f2, c2.sortie, ETIQ, proche, attendre=lambda s: None, horloge=lambda: t).reprendre()
    assert f2.veilleurs[0]["echeance"] == proche - la.ECART_SECOURS_S < t
    # artefact : veilleur non lancé : alerte exacte
    c3, f3 = _poste_interrompu(tmp_path / "z", monkeypatch)
    f3.etat, f3.veilleur_vivant = "loading", False
    b3 = la.Reprise(f3, c3.sortie, ETIQ, LOIN, attendre=lambda s: None, horloge=lambda: t).reprendre()
    assert any("aucun veilleur local d'arrêt lancé" in a for a in b3["alertes"])


# --- v14 : message d'erreur d'une exécution morte avant tout tour (instance_v16) ------------------------------------------

def _executer_v14(tmp_path, monkeypatch, script):
    """Exécution factice : l'enfant est `script` ; configuration attendue « cfg: 1 » ; dépense et échéance lointaines."""
    monkeypatch.setattr(inst, "configuration_attendue", lambda clone, over: "cfg: 1\n\n")
    monkeypatch.setattr(inst, "garde_k_configuration", lambda attendu, manifeste, phase: "passée")
    monkeypatch.setattr(inst, "parametres_phase", lambda manifeste, phase: (3, 1394228342))
    man = {"chemin_modele": "/m", "pas_par_tour": 4, "juge": {}, "cache_hf": "/root/hf"}
    travail = tmp_path / "exec"
    etat_ = inst.executer(man, tmp_path / "clone", travail, "pilote",
                          {"d_avant": 0, "c": 1, "creation": 1e12, "b": 75}, 1e12,
                          commande=[sys.executable, "-c", script], intervalle=0.1)
    return etat_, travail


def test_v14_mort_avant_configuration_ecrit_et_transfere_l_erreur(tmp_path, monkeypatch):
    """Cas sain : l'enfant meurt à l'import, avant toute configuration : le message sort, il est empreinté."""
    script = "import sys\nsys.stderr.write('Traceback (most recent call last):\\n')\nimport module_qui_n_existe_pas\n"
    etat_, travail = _executer_v14(tmp_path, monkeypatch, script)
    assert etat_["code_retour"] != 0 and etat_["configuration_effective"] == "non décidée"
    assert etat_["tours_complets"] == 0 and etat_["erreur_demarrage"] is True
    texte = (travail / inst.ERREUR_DEMARRAGE).read_text(encoding="utf-8")
    assert "ModuleNotFoundError" in texte and "module_qui_n_existe_pas" in texte
    assert inst.ERREUR_DEMARRAGE in inst.empreintes(travail)


def test_v14_artefact_configuration_imprimee_puis_mort_pas_de_fichier(tmp_path, monkeypatch):
    """Artefact : la configuration a été imprimée (la boucle a pu commencer) : rien ne sort, même en erreur."""
    script = "import sys\nprint('cfg: 1\\n', flush=True)\nsys.stderr.write('texte produit 0.42\\n')\nraise SystemExit(1)\n"
    etat_, travail = _executer_v14(tmp_path, monkeypatch, script)
    assert etat_["code_retour"] != 0 and etat_["configuration_effective"] == "passée"
    assert etat_["erreur_demarrage"] is False and not (travail / inst.ERREUR_DEMARRAGE).exists()
    assert inst.ERREUR_DEMARRAGE not in inst.empreintes(travail)


def test_v14_artefact_configuration_fausse_pas_de_fichier(tmp_path, monkeypatch):
    """Artefact : garde de démarrage tombée (décidée) : rien ne sort."""
    script = "import time\nprint('cfg: 2\\n', flush=True)\ntime.sleep(30)\n"
    etat_, travail = _executer_v14(tmp_path, monkeypatch, script)
    assert etat_["configuration_effective"] == "tombée" and etat_["erreur_demarrage"] is False
    assert not (travail / inst.ERREUR_DEMARRAGE).exists()


def test_v14_artefact_sortie_sans_erreur_pas_de_fichier(tmp_path, monkeypatch):
    """Artefact : code de retour nul sans configuration : rien ne sort (le cas n'est pas une mort)."""
    etat_, travail = _executer_v14(tmp_path, monkeypatch, "pass\n")
    assert etat_["code_retour"] == 0 and etat_["erreur_demarrage"] is False
    assert not (travail / inst.ERREUR_DEMARRAGE).exists()


def test_v14_filtre_retire_les_valeurs_et_borne_la_taille():
    """v15 (R-1, R-4) : valeurs remplacées sur place ; ligne à tenseur retirée ; 60 lignes ; 300 caractères ; taille."""
    lignes = [f"ligne {i}" for i in range(100)] + ["score 0.9697 pour l'entrée", "tensor([1, 2])",
                                                     "identifiant 12345678901234", "x" * 1000, "ValueError: oups"]
    sortie = inst.erreur_demarrage_filtree("\n".join(lignes))
    garde = sortie.splitlines()
    assert len(garde) == inst.LIGNES_ERREUR_MAX
    assert "0.9697" not in sortie and "tensor(" not in sortie and "12345678901234" not in sortie
    assert "score <nombre> pour l'entrée" in garde and "identifiant <chiffres>" in garde
    assert garde.count(inst.RETIREE) == 1
    assert max(len(l) for l in garde) <= inst.LARGEUR_LIGNE_MAX
    assert garde[-1] == "ValueError: oups"
    gros = inst.erreur_demarrage_filtree("\n".join("é" * 300 for _ in range(60)))
    assert len(gros.encode("utf-8")) <= inst.TAILLE_ERREUR_MAX
    assert inst.erreur_demarrage_filtree("") == ""


def test_v14_ecriture_ne_leve_jamais(tmp_path):
    """Sortie d'erreur absente : pas de fichier, pas d'exception (l'état de l'exécution doit s'écrire quand même)."""
    assert inst.ecrire_erreur_demarrage(tmp_path, 1, None, 0, True) is False
    assert not (tmp_path / inst.ERREUR_DEMARRAGE).exists()


def test_v14_transfert_accepte_le_seul_nouveau_nom(tmp_path):
    class F:
        def rapatrier_fichier(self, ident, distant, local):
            local.parent.mkdir(parents=True, exist_ok=True)
            local.write_text("x")
    sha = cv.sha_fichier
    (tmp_path / "ref").write_text("x")
    h = sha(tmp_path / "ref")
    essais = la.transferer(F(), "1", "/x", tmp_path / "t", {inst.ERREUR_DEMARRAGE: h, cv.ETAT_EXECUTION: h})
    assert essais[0] == {inst.ERREUR_DEMARRAGE: h, cv.ETAT_EXECUTION: h}
    with pytest.raises(GardeArret, match="liste fermée"):
        la.transferer(F(), "1", "/x", tmp_path / "u", {"sortie-erreur-instance.log": h})
    assert set(inst.SORTANTS) - set(cv.SORTANTS) == {inst.ERREUR_DEMARRAGE}


def test_v14_modules_et_archive():
    assert la.INSTANCE_MODULE == "controle_ia.temoin_bailey.instance_v16"
    assert la.VEILLEUR_MODULE == "controle_ia.temoin_bailey.lanceur_v21"
    assert "src/controle_ia/temoin_bailey/instance_v16.py" in la.CHEMINS_ARCHIVE
    assert "src/controle_ia/temoin_bailey/instance_v12.py" not in la.CHEMINS_ARCHIVE


# --- v15 : essais demandés par la relecture du code v14 (R-1, R-2, R-4, R-5, R-6) ---------------------------------------

TRACE_REELLE = """Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "/root/travail/src/controle_ia/temoin_bailey/execution_v3.py", line 96, in main
    import obf_reps.utils as ut
  File "/root/venv/lib/python3.11/site-packages/sparsify/__init__.py", line 3, in <module>
    from .sae import Sae
  File "/root/venv/lib/python3.11/site-packages/torch/cuda/__init__.py", line 154, in is_bf16_supported
RuntimeError: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 79.15 GiB
OSError: token hf_AbCdEfGhIjKlMnOpQrStUvWxYz012345 is invalid for meta-llama/Meta-Llama-3-8B-Instruct
"""


def test_v15_filtre_garde_les_lignes_de_trace_reelles():
    """R-1 : chemins, versions et noms de modules gardés ; valeurs remplacées ; jeton remplacé (R-4)."""
    sortie = inst.erreur_demarrage_filtree(TRACE_REELLE)
    assert "/root/venv/lib/python3.11/site-packages/sparsify/__init__.py" in sortie
    assert "import obf_reps.utils as ut" in sortie and "is_bf16_supported" in sortie
    assert "RuntimeError: Found no NVIDIA driver" in sortie
    assert "Tried to allocate <nombre> MiB" in sortie and "20.00" not in sortie and "79.15" not in sortie
    assert "hf_AbCd" not in sortie and "<jeton>" in sortie
    assert inst.RETIREE not in sortie


def test_v15_condition_complets_non_nul_et_code_none(tmp_path):
    """R-6 : branches non couvertes de la condition."""
    (tmp_path / "sortie-erreur-instance.log").write_text("ImportError: x\n")
    assert inst.ecrire_erreur_demarrage(tmp_path, 1, None, 1, True) is False
    assert inst.ecrire_erreur_demarrage(tmp_path, None, None, 0, True) is False
    assert inst.ecrire_erreur_demarrage(tmp_path, 1, True, 0, True) is False
    assert inst.ecrire_erreur_demarrage(tmp_path, 1, None, 0, False) is False
    assert not (tmp_path / inst.ERREUR_DEMARRAGE).exists()
    assert inst.ecrire_erreur_demarrage(tmp_path, 1, None, 0, True) is True


def test_v15_condition_traces_d_une_boucle_commencee(tmp_path):
    """R-2 (défense) : journal des notes non vide, ou fichier dans les sondes ou les suffixes : rien n'est écrit."""
    for cas in ("notes", "sondes", "params"):
        d = tmp_path / cas
        d.mkdir()
        (d / "sortie-erreur-instance.log").write_text("ImportError: x\n")
        if cas == "notes":
            (d / cv.JOURNAL_NOTES).parent.mkdir(parents=True)
            (d / cv.JOURNAL_NOTES).write_text("{}\n")
        else:
            (d / cas).mkdir()
            (d / cas / "f.pt").write_bytes(b"x")
        assert inst.ecrire_erreur_demarrage(d, 1, None, 0, True) is False, cas
        assert not (d / inst.ERREUR_DEMARRAGE).exists()
    vide = tmp_path / "vide"
    (vide / "sondes").mkdir(parents=True)
    (vide / "sortie-erreur-instance.log").write_text("ImportError: x\n")
    assert inst.ecrire_erreur_demarrage(vide, 1, None, 0, True) is True  # dossier vide : sain


def test_v15_configuration_partielle_ecrit(tmp_path, monkeypatch):
    """R-2, sain : un début exact de la configuration est imprimé, puis l'enfant meurt : le message sort."""
    script = "import sys\nsys.stdout.write('cfg'); sys.stdout.flush()\nraise RuntimeError('mort apres le debut')\n"
    etat_, travail = _executer_v14(tmp_path, monkeypatch, script)
    assert etat_["configuration_effective"] == "non décidée" and etat_["erreur_demarrage"] is True
    assert "RuntimeError: mort apres le debut" in (travail / inst.ERREUR_DEMARRAGE).read_text()


def test_v15_artefact_configuration_plus_courte_et_differente(tmp_path, monkeypatch):
    """R-2, artefact : sortie plus courte que la configuration attendue mais différente (la boucle a pu commencer) :
    rien ne sort."""
    script = "import sys\nprint('x', flush=True)\nsys.stderr.write('texte produit\\n')\nraise SystemExit(1)\n"
    etat_, travail = _executer_v14(tmp_path, monkeypatch, script)
    assert etat_["configuration_effective"] == "non décidée" and etat_["erreur_demarrage"] is False
    assert not (travail / inst.ERREUR_DEMARRAGE).exists()


def test_v15_echec_d_ecriture_ne_leve_pas_et_ne_laisse_rien(tmp_path, monkeypatch):
    """R-6 : une erreur d'écriture est avalée, le temporaire est effacé."""
    (tmp_path / "sortie-erreur-instance.log").write_text("ImportError: x\n")
    def casse(*a, **k):
        raise OSError("disque plein")
    monkeypatch.setattr(inst.os, "replace", casse)
    assert inst.ecrire_erreur_demarrage(tmp_path, 1, None, 0, True) is False
    assert not list(tmp_path.glob(inst.ERREUR_DEMARRAGE + "*"))


def test_v15_arret_par_la_depense_et_par_l_echeance(tmp_path, monkeypatch):
    """R-5, R-6 : l'arrêt de l'enfant par son PID ne lève plus (défaut `signal` des v7 à v12) ; pas de message."""
    monkeypatch.setattr(inst, "configuration_attendue", lambda clone, over: "cfg: 1\n\n")
    monkeypatch.setattr(inst, "garde_k_configuration", lambda attendu, manifeste, phase: "passée")
    monkeypatch.setattr(inst, "parametres_phase", lambda manifeste, phase: (3, 1394228342))
    man = {"chemin_modele": "/m", "pas_par_tour": 4, "juge": {}, "cache_hf": "/root/hf"}
    script = "import time\nprint('cfg: 1\\n', flush=True)\ntime.sleep(60)\n"
    e = inst.executer(man, tmp_path / "clone", tmp_path / "a", "pilote", {"d_avant": 74, "c": 1, "creation": 0, "b": 75},
                      1e12, commande=[sys.executable, "-c", script], intervalle=0.1)
    assert e["cause_arret"] == "dépense" and e["code_retour"] != 0 and e["erreur_demarrage"] is False
    e = inst.executer(man, tmp_path / "clone", tmp_path / "b", "pilote", {"d_avant": 0, "c": 1, "creation": 1e12,
                      "b": 75}, 0, commande=[sys.executable, "-c", script], intervalle=0.1, marge_transfert_s=0)
    assert e["cause_arret"] == "échéance du GO" and e["code_retour"] != 0


def test_v15_lecture_d_un_dossier_qui_porte_le_message(tmp_path):
    """R-6 : un état d'exécution qui porte `erreur_demarrage` et un dossier qui porte le fichier se lisent comme avant."""
    from controle_ia.temoin_bailey import lecture_v8 as lv
    e = {"phase": "pilote", "k": 3, "code_retour": 1, "cause_arret": None, "gardes_tombees": ["x"], "tours_marques": 0,
         "tours_complets": 0, "durees": {}, "configuration_effective": "non décidée", "erreur_demarrage": True}
    assert lv.relance_permise(e) is True
    assert lv.issue_pilote(e) not in ("finie",)


def test_v15_aucun_masquage_du_module_signal():
    """R-5 : aucune fonction d'instance_v16 ne lie un nom local `signal`."""
    import ast
    arbre = ast.parse(Path(inst.__file__).read_text(encoding="utf-8"))
    for n in ast.walk(arbre):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            noms = {a.id for a in ast.walk(n) if isinstance(a, ast.Name) and isinstance(a.ctx, ast.Store)}
            noms |= {a.target.id for a in ast.walk(n) if isinstance(a, ast.AnnAssign) and isinstance(a.target, ast.Name)}
            assert "signal" not in noms, n.name


# --- v16 : essais demandés par la relecture différentielle du code v15 (D-1 à D-4, D-7, D-8) -----------------------------

def test_v16_filtre_noms_gardes_valeurs_remplacees():
    """D-1, D-2, D-3."""
    t = ("is_torch_greater_or_equal_than_1_13 hf_transfer hf_quantizer models--meta-llama--Meta-Llama-3-8B-Instruct "
         "python3.11 4.43.2 127.0.0.1 line 154\n"
         "jeton hf_AbCdEfGhIjKlMnOpQrStUvWxYz012345 note .97 et 1e-3 et 9.7466e-01 et 0.97 et -0.5 "
         "empreinte 8afb486c1db24fe5011ec46dfbe5b5dccdb575c2")
    sortie = inst.erreur_demarrage_filtree(t)
    for garde in ("is_torch_greater_or_equal_than_1_13", "hf_transfer", "hf_quantizer", "python3.11", "4.43.2",
                  "127.0.0.1", "line 154", "models--meta-llama--Meta-Llama-3-8B-Instruct"):
        assert garde in sortie, garde
    for retire in ("hf_AbCd", ".97", "1e-3", "9.7466e-01", "0.97", "-0.5", "8afb486c1db24fe5011ec46dfbe5b5dccdb575c2"):
        assert retire not in sortie, retire
    assert sortie.count("<nombre>") == 5 and "<jeton>" in sortie and "<suite>" in sortie


def _enfant_muet(tmp_path, monkeypatch, nom, depense, echeance, marge=3600.0):
    monkeypatch.setattr(inst, "configuration_attendue", lambda clone, over: "cfg: 1\n\n")
    monkeypatch.setattr(inst, "garde_k_configuration", lambda attendu, manifeste, phase: "passée")
    monkeypatch.setattr(inst, "parametres_phase", lambda manifeste, phase: (3, 1394228342))
    man = {"chemin_modele": "/m", "pas_par_tour": 4, "juge": {}, "cache_hf": "/root/hf"}
    script = "import sys, time\nsys.stderr.write('chargement\\n'); sys.stderr.flush()\ntime.sleep(60)\n"
    return inst.executer(man, tmp_path / "clone", tmp_path / nom, "pilote", depense, echeance,
                         commande=[sys.executable, "-c", script], intervalle=0.1, marge_transfert_s=marge)


def test_v16_enfant_muet_arrete_par_la_depense_pas_de_message(tmp_path, monkeypatch):
    """D-4, artefact déterministe : aucune sortie standard ; l'instance décide l'arrêt (dépense) : pas de message."""
    e = _enfant_muet(tmp_path, monkeypatch, "a", {"d_avant": 74, "c": 1, "creation": 0, "b": 75}, 1e12)
    assert e["cause_arret"] == "dépense" and e["configuration_effective"] == "non décidée"
    assert e["erreur_demarrage"] is False and not (tmp_path / "a" / inst.ERREUR_DEMARRAGE).exists()


def test_v16_enfant_muet_arrete_par_l_echeance_pas_de_message(tmp_path, monkeypatch):
    """D-4, artefact déterministe : idem par l'échéance."""
    e = _enfant_muet(tmp_path, monkeypatch, "b", {"d_avant": 0, "c": 1, "creation": 1e12, "b": 75}, 0, marge=0.0)
    assert e["cause_arret"] == "échéance du GO" and e["configuration_effective"] == "non décidée"
    assert e["erreur_demarrage"] is False and not (tmp_path / "b" / inst.ERREUR_DEMARRAGE).exists()


def test_v16_vacuite_liens_tubes_et_journal_au_bon_chemin(tmp_path):
    """D-7 : lien symbolique, lien cassé, tube, fichier non vide : non vide ; dossiers vides et fichiers vides : vide."""
    plein = tmp_path / "plein"
    plein.mkdir()
    (plein / "f").write_text("x")
    cas = {}
    for nom in ("lien", "casse", "tube", "fichier", "sain"):
        d = tmp_path / nom
        (d / "sous").mkdir(parents=True)
        cas[nom] = d
    (cas["lien"] / "sous" / "l").symlink_to(plein)
    (cas["casse"] / "l").symlink_to(tmp_path / "nulle-part")
    os.mkfifo(cas["tube"] / "t")
    (cas["fichier"] / "sous" / "f").write_text("x")
    (cas["sain"] / "sous" / "vide").write_text("")
    for nom in ("lien", "casse", "tube", "fichier"):
        assert inst._vide(cas[nom]) is False, nom
    assert inst._vide(cas["sain"]) is True and inst._vide(tmp_path / "absent") is True
    # le journal des notes est lu là où l'écrit le journaliseur
    t = tmp_path / "travail"
    (t / "ailleurs").mkdir(parents=True)
    (t / "config-journal-v3.json").write_text(json.dumps({"dossier_journal": str(t / "ailleurs")}))
    (t / "ailleurs" / Path(cv.JOURNAL_NOTES).name).write_text("{}\n")
    (t / "sortie-erreur-instance.log").write_text("ImportError: x\n")
    assert inst.ecrire_erreur_demarrage(t, 1, None, 0, True) is False
    (t / "ailleurs" / Path(cv.JOURNAL_NOTES).name).write_text("")
    assert inst.ecrire_erreur_demarrage(t, 1, None, 0, True) is True


def test_v16_lecture_d_un_dossier_d_etape_qui_porte_le_message(tmp_path):
    """D-8 : un dossier d'étape avec les journaux et le message se lit (dossier de foi, journaux scellés) ; la garde de
    fin de run n'a pas à être appelée (K' = 0)."""
    from controle_ia.temoin_bailey import lecture_v8 as lv
    travail = tmp_path / "instance"
    travail.mkdir()
    for rel in (cv.GARDES_LANCEUR, cv.SORTIE_DUREES, cv.EMPREINTES_FICHIERS):
        (travail / rel).parent.mkdir(parents=True, exist_ok=True)
        (travail / rel).write_text("")
    (travail / cv.ETAT_EXECUTION).write_text(json.dumps({
        "phase": "pilote", "k": 3, "graine": 1394228342, "code_retour": 1, "cause_arret": None,
        "configuration_effective": "non décidée", "durees": {}, "tours_marques": 0,
        "gardes_tombees": ["journal des gardes absent (gardes-v3.jsonl)"], "tours_complets": 0,
        "journal_absent": "lecture : journal absent (technique-v3.jsonl)", "lignes_tronquees_ignorees": [],
        "erreur_demarrage": True}))
    (travail / inst.ERREUR_DEMARRAGE).write_text("ModuleNotFoundError: No module named 'x'\n")
    emp = inst.empreintes(travail)
    assert inst.ERREUR_DEMARRAGE in emp
    etape = tmp_path / "pilote"
    (etape / "transfert-1").mkdir(parents=True)
    (etape / cv.EMPREINTES_INSTANCE).write_text(json.dumps(emp))
    for rel in emp:
        cible = etape / "transfert-1" / rel
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(travail / rel, cible)
        scellement.sceller(cible)
    foi = lv.dossier_de_foi(etape)
    assert foi["foi"] == etape / "transfert-1"
    assert lv.journaux_scelles(foi["foi"], tuple(emp)) is True
    assert lv.relance_permise(json.loads((foi["foi"] / cv.ETAT_EXECUTION).read_text())) is True


# --- v17 : script public lancé comme programme principal (execution_v4) ----------------------------------------------

def test_v17_modules_et_archive():
    assert la.INSTANCE_MODULE == "controle_ia.temoin_bailey.instance_v16"
    assert la.VEILLEUR_MODULE == "controle_ia.temoin_bailey.lanceur_v21"
    assert "src/controle_ia/temoin_bailey/execution_v4.py" in la.CHEMINS_ARCHIVE
    assert "src/controle_ia/temoin_bailey/instance_v16.py" in la.CHEMINS_ARCHIVE
    for ancien in ("execution_v3.py", "instance_v15.py", "lanceur_v16.py"):
        assert not any(p.endswith(ancien) for p in la.CHEMINS_ARCHIVE), ancien


def test_v17_aucune_reference_a_execution_v3_dans_le_code_execute():
    """Ni import ni chaîne (docstrings exceptées) ne nomme `execution_v3`, `instance_v15` ou `lanceur_v16`."""
    import ast
    for nom in ("instance_v16.py", "lanceur_v21.py", "execution_v4.py"):
        arbre = ast.parse((DEPOT / "src/controle_ia/temoin_bailey" / nom).read_text(encoding="utf-8"))
        docs = {id(b.body[0].value) for b in ast.walk(arbre)
                if isinstance(b, (ast.Module, ast.ClassDef, ast.FunctionDef)) and b.body
                and isinstance(b.body[0], ast.Expr) and isinstance(b.body[0].value, ast.Constant)}
        for n in ast.walk(arbre):
            if isinstance(n, ast.ImportFrom):
                assert not re.search(r"execution_v3|instance_v15|lanceur_v16", n.module or ""), (nom, n.module)
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs:
                assert not re.search(r"execution_v3|instance_v15|lanceur_v16", n.value), (nom, n.value[:80])
    from controle_ia.temoin_bailey import execution_v4
    assert inst.configuration_attendue is execution_v4.configuration_attendue
    assert inst.surcharges is execution_v4.surcharges


def test_v17_commande_par_defaut_de_l_enfant(tmp_path, monkeypatch):
    """La commande par défaut d'`executer` lance `execution_v4` par `-m` (lue dans la source : la fonction ne se
    rejoue pas sans instance)."""
    source = (DEPOT / "src/controle_ia/temoin_bailey/instance_v16.py").read_text(encoding="utf-8")
    assert source.count('"controle_ia.temoin_bailey.execution_v4", "--clone"') == 1
    assert "execution_v3\"" not in source


MINI_CONFIG = "defaults:\n  - _self_\n  - experiment: default\n"
MINI_DEFAUT = ("seed: 0\nmodel_path: modele\nattack_defense_epochs: 1\nsave_probe_path: null\n"
               "save_tunable_params_path: null\nlambda_: 1.0\n")
MINI_EXPERIENCE = "defaults:\n    - default\n\nlambda_: 0.1\nattack_defense_epochs: 100\n"
MINI_SCRIPT = '''import os
import sys
import hydra
from omegaconf import DictConfig, OmegaConf

import transformers
from evaluate import MARQUE
from obf_reps.utils import classe_journaliseur


@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))
    c = classe_journaliseur()
    sys.stderr.write(f"JOURNALISEUR {c.__module__}.{c.__qualname__}\\n")
    sys.stderr.write(f"DOSSIER {os.getcwd()}\\nCHEMIN0 {sys.path[0]}\\nLOCAL {MARQUE}\\n")
    sys.stderr.write(f"GRAINES {transformers.GRAINES}\\nNOM {__name__}\\nARGV0 {sys.argv[0]}\\n")
    if cfg.experiment.lambda_ == 0.5:
        raise RuntimeError("erreur volontaire du script")


if __name__ == "__main__":
    main()
'''


def _mini_clone(racine: Path, configs_publiques: Path | None = None) -> Path:
    d = racine / cv.SOUS_DOSSIER
    (d / "obf_reps" / "logging").mkdir(parents=True)
    if configs_publiques is not None:
        shutil.copytree(configs_publiques, d / "configs")
    else:
        (d / "configs" / "experiment").mkdir(parents=True)
        (d / "configs" / "config.yaml").write_text(MINI_CONFIG)
        (d / "configs" / "experiment" / "default.yaml").write_text(MINI_DEFAUT)
        (d / "configs" / "experiment" / f"{cv.EXPERIENCE}.yaml").write_text(MINI_EXPERIENCE)
    (d / "obf_reps" / "__init__.py").write_text("")
    (d / "obf_reps" / "logging" / "__init__.py").write_text("class WAndBLogger:\n    pass\n")
    (d / "obf_reps" / "utils.py").write_text("from obf_reps.logging import WAndBLogger\n\n\n"
                                             "def classe_journaliseur():\n    return WAndBLogger\n")
    (d / "transformers.py").write_text("GRAINES = []\n\n\ndef set_seed(g):\n    GRAINES.append(g)\n")
    (d / "evaluate.py").write_text("MARQUE = 'module local du clone'\n")
    (d / "train_harmful.py").write_text(MINI_SCRIPT)
    return racine


def _lancer_enfant(module: str, clone: Path, over: list[str], tmp_path: Path):
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "TESTING", "TEMOIN_BAILEY_CONFIG")}
    env["PYTHONPATH"] = str(DEPOT / "src")
    return subprocess.run([sys.executable, "-m", module, "--clone", str(clone), "--graine", "7", "--", *over],
                          cwd=tmp_path, env=env, capture_output=True, text=True, timeout=120)


def _surcharges_mini(tmp_path: Path) -> list[str]:
    from controle_ia.temoin_bailey.execution_v4 import surcharges
    return surcharges(3, 1394228342, str(tmp_path / "modele"), str(tmp_path / "sondes"), str(tmp_path / "params"),
                      str(tmp_path / "hydra"))


def test_v17_epreuve_reelle_hydra_main_cas_sain(tmp_path):
    """Cas sain : `execution_v4` lance le script décoré par `@hydra.main(config_path="configs")` ; la sortie standard
    commence exactement par `configuration_attendue` (la garde de démarrage de l'instance se décide) ; le script voit
    le journaliseur substitué ; Hydra écrit sous `hydra.run.dir`, hors du clone."""
    pytest.importorskip("hydra")
    from controle_ia.temoin_bailey.execution_v4 import configuration_attendue
    clone = _mini_clone(tmp_path / "clone")
    over = _surcharges_mini(tmp_path)
    r = _lancer_enfant("controle_ia.temoin_bailey.execution_v4", clone, over, tmp_path)
    assert r.returncode == 0, r.stderr[-3000:]
    attendu = configuration_attendue(clone, over)
    assert r.stdout.startswith(attendu) and "attack_defense_epochs: 3" in attendu and "seed: 1394228342" in attendu
    assert "JOURNALISEUR controle_ia.temoin_bailey.journaliseur_v3.JournaliseurLocal" in r.stderr
    d = (clone / cv.SOUS_DOSSIER).resolve()
    # C-2 de la relecture v17 : dossier courant, tête de `sys.path`, module local, graine, nom et argv du script
    assert f"DOSSIER {d}\n" in r.stderr and f"CHEMIN0 {d}\n" in r.stderr
    assert "LOCAL module local du clone\n" in r.stderr and "GRAINES [7]\n" in r.stderr
    assert "NOM __main__\n" in r.stderr and f"ARGV0 {d / 'train_harmful.py'}\n" in r.stderr
    assert (tmp_path / "hydra" / ".hydra" / "config.yaml").exists()
    assert not (clone / cv.SOUS_DOSSIER / "outputs").exists()


def test_v17_artefact_execution_v3_echoue_avant_toute_impression(tmp_path):
    """Artefact (R5) : le même mini-clone lancé par `execution_v3` (import puis `main()`) échoue sans rien imprimer,
    comme les deux pilotes du 12 novembre ; l'épreuve distingue donc les deux chemins."""
    pytest.importorskip("hydra")
    clone = _mini_clone(tmp_path / "clone")
    r = _lancer_enfant("controle_ia.temoin_bailey.execution_v3", clone, _surcharges_mini(tmp_path), tmp_path)
    assert r.returncode != 0 and r.stdout == ""
    assert "configs" in r.stderr and "JOURNALISEUR" not in r.stderr


def test_v17_erreur_du_script_propagee_sans_repli(tmp_path):
    """Une exception levée par le script public sort en code non nul, trace dans la sortie d'erreur (aucun repli)."""
    pytest.importorskip("hydra")
    clone = _mini_clone(tmp_path / "clone")
    over = _surcharges_mini(tmp_path) + ["experiment.lambda_=0.5"]
    r = _lancer_enfant("controle_ia.temoin_bailey.execution_v4", clone, over, tmp_path)
    assert r.returncode != 0 and "erreur volontaire du script" in r.stderr


def test_v17_garde_testing_inchangee(tmp_path, monkeypatch):
    from controle_ia.temoin_bailey import execution_v4 as ex
    monkeypatch.setenv("TESTING", "1")
    monkeypatch.setenv("TEMOIN_BAILEY_CONFIG", str(tmp_path / "config-journal-v3.json"))
    assert ex.main(["--clone", "/inexistant", "--graine", "1"]) == ex.SORTIE_GARDE
    assert lc.lire_jsonl(tmp_path / cv.GARDES_LANCEUR)[0]["garde"] == "juge"


@pytest.mark.skipif(not os.environ.get("TEMOIN_BAILEY_CONFIGS_PUBLIQUES"),
                    reason="dossier `configs/` du clone public non fourni (TEMOIN_BAILEY_CONFIGS_PUBLIQUES)")
def test_v17_epreuve_reelle_avec_les_configurations_publiques(tmp_path):
    """Même épreuve avec le vrai dossier `configs/` du code public (commit 9c1f4b1a), quand il est fourni."""
    from controle_ia.temoin_bailey.execution_v4 import configuration_attendue
    clone = _mini_clone(tmp_path / "clone", Path(os.environ["TEMOIN_BAILEY_CONFIGS_PUBLIQUES"]))
    over = _surcharges_mini(tmp_path)
    r = _lancer_enfant("controle_ia.temoin_bailey.execution_v4", clone, over, tmp_path)
    assert r.returncode == 0, r.stderr[-3000:]
    assert r.stdout.startswith(configuration_attendue(clone, over))
    assert "JOURNALISEUR controle_ia.temoin_bailey.journaliseur_v3.JournaliseurLocal" in r.stderr


# --- v19 : relance seule et assemblage (addendum 5), corrigés selon la contre-lecture v18 --------------------------------

REPRISE_REELLE = DEPOT / "runs/temoin-bailey-v1-20261111/sortie-conduite-v11/reprise-v10-2"
T_PREMIERE = 3600.0  # v20 : t du pilote factice de la première conduite (K de relance ≥ 20 sous la garde R-1)
ANT = [{"id": "76", "c": 1.0, "creation": HORLOGE - 3.2 * 3600, "destruction": HORLOGE, "B": 75}]  # D = 3,2 ≥ 3


def _resceller(f: Path):
    c = Path(f"{f}.sha256")
    if c.exists():
        c.unlink()
    scellement.sceller(f)


def _premiere_interrompue(tmp_path, monkeypatch) -> Path:
    """Première conduite : principal mort à 3 tours (K = 30) ; sa relance retirée (ce qu'aurait laissé une conduite
    coupée avant la relance) ; renvoie le dossier des transferts."""
    with monkeypatch.context() as m:
        m.setattr(sys.modules[__name__], "T_REGLE", T_PREMIERE)
        c, f, _ = conduite_locale(tmp_path / "a", monkeypatch, scenario(30, principal_sans_etat(3, 30, "mort")))
        c.conduire()
    p = tmp_path / "premiere"
    shutil.copytree(c.sortie, p, ignore=shutil.ignore_patterns("principal-relance", lc.MANIFESTES["relance"] + "*"))
    return p


def _comme_la_reprise(premiere: Path):
    """Forme de `reprise-v10-2` : état du principal absent (processus tué), absent des empreintes de l'instance ;
    journaux de la conduite retirés (repris de la contre-lecture v18)."""
    t1 = premiere / "principal" / "transfert-1"
    for p in (t1 / cv.ETAT_EXECUTION, Path(f"{t1 / cv.ETAT_EXECUTION}.sha256")):
        if p.exists():
            p.unlink()
    emp = premiere / "principal" / cv.EMPREINTES_INSTANCE
    d = json.loads(emp.read_text())
    d.pop(cv.ETAT_EXECUTION, None)
    emp.write_text(json.dumps(d))
    _resceller(emp)
    for nom in ("conduite-v5.jsonl", "poste-v5.json", "rapatriement-v11.json", "bilan-conduite-v5.json",
                "bilan-conduite-v5.json.sha256", "archive", "amorce-v5.sh"):
        p = premiere / nom
        if p.is_dir():
            shutil.rmtree(p)
        elif p.exists():
            p.unlink()


def _relance(tmp_path, monkeypatch, premiere: Path, regle=None, k1=3, scen=None, anterieures=None, instance="76"):
    regle = regle or json.loads((premiere / lc.MANIFESTES["regle"]).read_text())["regle_tours"]
    f = FournisseurLocal(tmp_path / "b", scen or scenario(30, principal_fini(30)))
    c, _ = _monter(tmp_path / "b", monkeypatch, f)
    c.instances_anterieures = ANT if anterieures is None else anterieures
    c.relance_seule = {"tours_complets_premiere": k1, "regle_premiere": regle, "instance_premiere": instance,
                       "manifeste_regle": str(premiere / lc.MANIFESTES["regle"]), "source": str(premiere),
                       "gardes_tombees_premiere": []}
    return c, f


def test_v20_relance_seule_cas_sain_bout_en_bout(tmp_path, monkeypatch):
    premiere = _premiere_interrompue(tmp_path, monkeypatch)
    c, f = _relance(tmp_path, monkeypatch, premiere)
    bilan = c.conduire()
    assert f.lance == ["amorce", "auto-arret", "mise-en-place", "controle-juge", "principal-relance"], f.lance
    assert "arret" not in bilan and "erreur" not in bilan and f.detruites == ["77"]
    m = json.loads((c.sortie / lc.MANIFESTES["relance"]).read_text())
    rt = m["regle_tours"]
    attendu = an.nombre_de_tours(75, rt["D"], 1.0, T_PREMIERE)
    assert rt["D"] == 3.2 and rt["K"] == attendu["K"] == 53 and rt["relance"] is True
    assert rt["H_heures"] == attendu["H_heures"]  # C-3
    assert rt["premiere_execution"] == json.loads((premiere / lc.MANIFESTES["regle"]).read_text())["regle_tours"]
    assert bilan["relance_seule"]["tours_complets_premiere"] == 3 and bilan["relance_seule"]["K"] == 53
    assert not (c.sortie / "pilote").exists() and not (c.sortie / "regle").exists()
    cible = tmp_path / "lecture"
    trace = la.assembler_lecture(premiere, c.sortie, cible)
    assert trace["fichiers_scelles_verifies"] > 0
    scellement.verifier(cible / "assemblage-v1.json")
    scellement.verifier(cible / "relance-manifestes" / lc.MANIFESTES["mise-en-place"])  # C-9
    v = lc.valider(cible)
    assert v["etat"] is None and v["k_prime"] == 53 and v["dossier"].endswith("principal-relance/transfert-1"), v
    (i,) = v["interruptions"]
    assert i["role"].startswith("première exécution") and i["k_prime"] == 3
    res = lc.lire(v, an.graines()["reechantillonnage"])
    assert res["verdict"].startswith("Effet reproduit sur le banc des auteurs, au régime réduit (K = 53)")


def test_v20_premiere_sans_etat_comme_la_reprise_lue_comme_interrompue(tmp_path, monkeypatch):
    """C-7 : première exécution sans état transféré (forme réelle de la reprise) : reconstituée à la lecture, sans note."""
    premiere = _premiere_interrompue(tmp_path, monkeypatch)
    _comme_la_reprise(premiere)
    c, f = _relance(tmp_path, monkeypatch, premiere)
    assert "arret" not in c.conduire()
    cible = tmp_path / "lecture"
    la.assembler_lecture(premiere, c.sortie, cible)
    v = lc.valider(cible)
    assert v["etat"] is None and v["k_prime"] == 53, v
    (i,) = v["interruptions"]
    assert i["k_prime"] == 3 and i["reconstitue"] == "à la lecture"
    assert lc.lire(v, an.graines()["reechantillonnage"])["verdict"].startswith("Effet reproduit")


def test_v20_assemblage_sur_la_structure_reelle_sans_journaux(tmp_path, monkeypatch):
    """C-7 : copie de `reprise-v10-2` réduite aux dossiers et aux JSON (aucun journal, aucune note copiée) ; relance
    factice dont le manifeste cite la règle, les graines et le code public réels ; mise en place réelle reprise."""
    if not REPRISE_REELLE.is_dir():
        pytest.skip("structure réelle absente")
    premiere = tmp_path / "premiere"
    for p in sorted(REPRISE_REELLE.rglob("*")):
        rel = p.relative_to(REPRISE_REELLE)
        if p.is_dir():
            (premiere / rel).mkdir(parents=True, exist_ok=True)
        elif p.suffix == ".json" or p.name.endswith(".json.sha256"):
            assert "notes" not in p.name and "technique" not in p.name
            (premiere / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, premiere / rel)
    reel = json.loads((premiere / lc.MANIFESTES["regle"]).read_text())
    base = _premiere_interrompue(tmp_path / "f", monkeypatch)
    c, f = _relance(tmp_path / "f", monkeypatch, base)
    c.conduire()
    m = c.sortie / lc.MANIFESTES["relance"]
    d = json.loads(m.read_text())
    d["regle_tours"]["premiere_execution"] = reel["regle_tours"]
    d["graines"], d["commit_public"], d["B"] = reel["graines"], reel["commit_public"], reel["B"]
    for cle in ("pas_par_tour", "longueur_suffixe", "ecart_10"):  # v20 (R-3)
        d[cle] = reel[cle]
    m.write_text(json.dumps(d))
    _resceller(m)
    mep_reelle = lc._etat_etape(premiere, "mise-en-place", cv.ETAT_MISE_EN_PLACE)
    assert mep_reelle is not None
    _modifier_etat(c.sortie, "mise-en-place", cv.ETAT_MISE_EN_PLACE, lambda e: (e.clear(), e.update(mep_reelle)))
    trace = la.assembler_lecture(premiere, c.sortie, tmp_path / "cible")
    assert trace["fichiers_scelles_verifies"] >= 20
    assert (tmp_path / "cible" / "principal-relance").is_dir()
    assert (tmp_path / "cible" / "bilan-reprise-v10.json").is_file()


def _entree(tmp_path, regle=None, **kw):
    man = tmp_path / "manifeste-regle.json"
    regle = regle or _regle_premiere()
    if not man.exists():
        man.write_text(json.dumps({"regle_tours": regle}))
        scellement.sceller(man)
    p = {"tours_complets_premiere": 3, "regle_premiere": regle, "instance_premiere": "76",
         "manifeste_regle": str(man), "gardes_tombees_premiere": []}
    p.update(kw)
    return p


def _regle_premiere(k=30, t=T_PREMIERE, d=0.0, b=75):
    return {"B": b, "R": 10, "D": d, "c": 1.0, "t": t, "H_heures": 65.0, "K": k}


def test_v20_gardes_d_entree_cas_sain(tmp_path):
    la.verifier_relance_seule(_entree(tmp_path), la.instances_du_poste(ANT, 75), 75)


@pytest.mark.parametrize("modif,anterieures,motif", [
    ({"tours_complets_premiere": 20}, ANT, "sous 20 tours"),
    ({"tours_complets_premiere": True}, ANT, "sous 20 tours"),
    ({"tours_complets_premiere": -1}, ANT, "sous 20 tours"),
    ({"instance_premiere": "99"}, ANT, "absente des antérieures"),
    ({}, [], "absente des antérieures"),
])
def test_v20_gardes_d_entree_artefacts(tmp_path, modif, anterieures, motif):
    with pytest.raises(GardeArret, match=motif):
        la.verifier_relance_seule(_entree(tmp_path, **modif), la.instances_du_poste(anterieures, 75), 75)


@pytest.mark.parametrize("regle,motif", [
    ({**_regle_premiere(), "t": 0}, "t du pilote"), ({"B": 75, "K": 30}, "incomplète"),
    (_regle_premiere(b=80), "B de la première"), (_regle_premiere(k=19), "K de la première"),
    (_regle_premiere(d=5.0), "inférieure au D"),
])
def test_v20_gardes_d_entree_regle(tmp_path, regle, motif):
    with pytest.raises(GardeArret, match=motif):
        la.verifier_relance_seule(_entree(tmp_path, regle=regle), la.instances_du_poste(ANT, 75), 75)


def test_v20_gardes_d_entree_regle_differente_du_manifeste(tmp_path):
    """C-4 : règle passée ≠ manifeste scellé de la première : refus avant toute création. (K′ ≥ K est impossible
    après les gardes K′ < 20 ≤ K : sans essai propre.)"""
    p = _entree(tmp_path)
    p["regle_premiere"] = {**p["regle_premiere"], "t": T_PREMIERE + 1}
    with pytest.raises(GardeArret, match="différente du manifeste scellé"):
        la.verifier_relance_seule(p, la.instances_du_poste(ANT, 75), 75)


def test_v20_gardes_d_entree_avant_toute_creation(tmp_path, monkeypatch):
    f = FournisseurFactice(reponses())
    c, _ = _monter(tmp_path, monkeypatch, f)
    c.instances_anterieures = ANT
    (tmp_path / "e").mkdir()
    c.relance_seule = _entree(tmp_path / "e", tours_complets_premiere=20)
    with pytest.raises(GardeArret, match="sous 20 tours"):
        c.conduire()
    assert "creer" not in f.appels and f.lance == []


def test_v20_d_compte_les_anterieures_k_sous_20_arret_sans_relance(tmp_path, monkeypatch):
    """C-1 : une antérieure coûteuse (45 h à 1 USD/h) entre dans D : K = 17 < 20 : arrêt, aucune relance."""
    premiere = _premiere_interrompue(tmp_path, monkeypatch)
    ant = [{"id": "76", "c": 1.0, "creation": HORLOGE - 45 * 3600, "destruction": HORLOGE, "B": 75}]
    c, f = _relance(tmp_path, monkeypatch, premiere, anterieures=ant)
    bilan = c.conduire()
    assert bilan["arret"] == "relance impossible (K < 20) : pas de verdict ; nœud"
    assert bilan["relance_seule"]["D"] == 45.0 and bilan["relance_seule"]["K"] == 17
    assert "principal-relance" not in f.lance and f.detruites == ["77"]


def test_v20_controle_du_juge_hors_seuil_arret_avant_relance(tmp_path, monkeypatch):
    premiere = _premiere_interrompue(tmp_path, monkeypatch)
    scen = scenario(30, principal_fini(30))

    def juge(f):
        f.ecrire("controle-juge", cv.ETAT_CONTROLE_JUGE, {"garde_juge": "passée", "etats": {"tenus": False}})
        return {"commande": "controle-juge", "etats": {"tenus": False}, "garde_juge": "passée"}, 0
    scen["controle-juge"] = juge
    c, f = _relance(tmp_path, monkeypatch, premiere, scen=scen)
    bilan = c.conduire()
    assert bilan["arret"].startswith("garde du juge ou contrôle du juge hors seuil")
    assert "principal-relance" not in f.lance and f.detruites == ["77"]


def _deux_sorties(tmp_path, monkeypatch):
    premiere = _premiere_interrompue(tmp_path, monkeypatch)
    c, _ = _relance(tmp_path, monkeypatch, premiere)
    c.conduire()
    return premiere, c.sortie


def _modifier_etat(sortie: Path, etape: str, nom: str, fn):
    """Réécrit un état transféré et met à jour les empreintes de l'instance (sinon l'état est refusé avant)."""
    f = lc.dossier_de_foi(sortie / etape)["foi"] / nom
    e = json.loads(f.read_text())
    fn(e)
    f.write_text(json.dumps(e))
    emp = sortie / etape / cv.EMPREINTES_INSTANCE
    de = json.loads(emp.read_text())
    de[nom] = cv.sha_fichier(f)
    emp.write_text(json.dumps(de))
    for x in (f, emp):
        if Path(f"{x}.sha256").exists():
            _resceller(x)


def test_v20_assemblage_refuse_relance_deja_presente_et_cible_presente(tmp_path, monkeypatch):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    (tmp_path / "cible").mkdir()
    with pytest.raises(GardeArret, match="déjà présent"):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")
    shutil.copytree(relance / "principal-relance", premiere / "principal-relance")
    with pytest.raises(GardeArret, match="porte déjà une relance"):
        la.assembler_lecture(premiere, relance, tmp_path / "cible2")
    assert not (tmp_path / "cible2").exists()


def test_v20_assemblage_refuse_mise_en_place_de_la_relance_tombee(tmp_path, monkeypatch):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    _modifier_etat(relance, "mise-en-place", cv.ETAT_MISE_EN_PLACE,
                   lambda e: e["gardes"].__setitem__(sorted(e["gardes"])[0], "tombée"))
    with pytest.raises(GardeArret, match="mise en place de la relance non conforme"):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")
    assert not (tmp_path / "cible").exists()


def test_v20_assemblage_refuse_mise_en_place_differente_de_la_premiere(tmp_path, monkeypatch):
    """C-2 : pas par tour différent : refus (la lecture audite la relance avec la mise en place de la première)."""
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    _modifier_etat(relance, "mise-en-place", cv.ETAT_MISE_EN_PLACE,
                   lambda e: e.__setitem__("pas_par_tour", e["pas_par_tour"] + 1))
    with pytest.raises(GardeArret, match="différente de la première .« pas_par_tour »."):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")


def test_v20_assemblage_refuse_juge_de_la_relance_non_tenu(tmp_path, monkeypatch):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    _modifier_etat(relance, "controle-juge", cv.ETAT_CONTROLE_JUGE,
                   lambda e: e.__setitem__("etats", {"tenus": False}))
    with pytest.raises(GardeArret, match="contrôle du juge de la relance non tenu"):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")


def test_v20_assemblage_refuse_relance_avec_pilote_et_premiere_incomplete(tmp_path, monkeypatch):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    shutil.copytree(premiere / "pilote", relance / "pilote")
    with pytest.raises(GardeArret, match="porte une étape « pilote »"):
        la.assembler_lecture(premiere, relance, tmp_path / "c1")
    shutil.rmtree(relance / "pilote")
    shutil.rmtree(premiere / "regle")
    with pytest.raises(GardeArret, match="« regle » absente de la première"):
        la.assembler_lecture(premiere, relance, tmp_path / "c2")


def test_v20_assemblage_refuse_fichier_scelle_altere(tmp_path, monkeypatch):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    scelles = la._fichiers_scelles(relance / "principal-relance")
    assert scelles
    scelles[0].write_bytes(scelles[0].read_bytes() + b" ")
    with pytest.raises(GardeArret, match="≠ scellée"):  # C-6, R-5
        la.assembler_lecture(premiere, relance, tmp_path / "cible")
    assert not (tmp_path / "cible").exists()


@pytest.mark.parametrize("cle", ["graines", "commit_public", "B"])
def test_v20_assemblage_refuse_graines_code_ou_b_absents_ou_differents(tmp_path, monkeypatch, cle):
    """C-5 : absents des deux côtés, puis différents."""
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    for m in (premiere / lc.MANIFESTES["regle"], relance / lc.MANIFESTES["relance"]):
        d = json.loads(m.read_text())
        d.pop(cle, None)
        m.write_text(json.dumps(d))
        _resceller(m)
    with pytest.raises(GardeArret, match=f"« {cle} » absent ou différent"):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")


def test_v20_assemblage_refuse_manifeste_qui_ne_cite_pas_la_regle(tmp_path, monkeypatch):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    m = relance / lc.MANIFESTES["relance"]
    d = json.loads(m.read_text())
    d["regle_tours"]["premiere_execution"] = {**d["regle_tours"]["premiere_execution"], "t": 1.0}
    m.write_text(json.dumps(d))
    _resceller(m)
    with pytest.raises(GardeArret, match="ne cite pas la règle"):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")


def test_v20_modules_rejoue():
    assert la.VEILLEUR_MODULE == "controle_ia.temoin_bailey.lanceur_v21"
    assert la.INSTANCE_MODULE == "controle_ia.temoin_bailey.instance_v16"
    assert "src/controle_ia/temoin_bailey/execution_v4.py" in la.CHEMINS_ARCHIVE


# --- v20 : relecture différentielle v19 ---------------------------------------------------------------------------------

@pytest.mark.parametrize("ant,modif,motif", [
    ([{**ANT[0], "c": 1.5}], {}, "taux de l'instance"),                                            # R-1
    ([{**ANT[0], "creation": HORLOGE, "destruction": HORLOGE - 3600}], {}, "détruite avant sa création"),  # R-1
    ([{**ANT[0], "creation": HORLOGE - 2.9 * 3600}], {}, "plus le coût des tours complets"),         # R-1
    (ANT, {"gardes_tombees_premiere": ["dépense"]}, "sonde orientée » ou « dépense"),                # R-8
    (ANT, {"gardes_tombees_premiere": ["sonde orientée"]}, "sonde orientée » ou « dépense"),         # R-8
    (ANT, {"gardes_tombees_premiere": "aucune"}, "illisible"),                                     # R-8
])
def test_v20_gardes_d_entree_r1_r8(tmp_path, ant, modif, motif):
    with pytest.raises(GardeArret, match=motif):
        la.verifier_relance_seule(_entree(tmp_path, **modif), la.instances_du_poste(ant, 75), 75)


@pytest.mark.parametrize("cle", ["tours_complets_premiere", "regle_premiere", "instance_premiere", "manifeste_regle",
                                 "gardes_tombees_premiere"])
def test_v20_gardes_d_entree_cles_manquantes(tmp_path, cle):
    p = _entree(tmp_path)
    p.pop(cle)
    with pytest.raises(GardeArret, match="requis"):
        la.verifier_relance_seule(p, la.instances_du_poste(ANT, 75), 75)


def test_v20_gardes_d_entree_manifeste_altere_ou_absent(tmp_path):
    p = _entree(tmp_path)
    Path(p["manifeste_regle"]).write_text(Path(p["manifeste_regle"]).read_text() + " ")
    with pytest.raises(GardeArret, match="≠ scellée"):
        la.verifier_relance_seule(p, la.instances_du_poste(ANT, 75), 75)
    p["manifeste_regle"] = str(tmp_path / "absent.json")
    with pytest.raises(GardeArret, match="absent"):
        la.verifier_relance_seule(p, la.instances_du_poste(ANT, 75), 75)


def test_v20_garde_d_entree_aucune_sortie_creee(tmp_path, monkeypatch):
    f = FournisseurFactice(reponses())
    c, _ = _monter(tmp_path, monkeypatch, f)
    c.instances_anterieures = ANT
    (tmp_path / "e").mkdir()
    c.relance_seule = _entree(tmp_path / "e", gardes_tombees_premiere=["dépense"])
    with pytest.raises(GardeArret):
        c.conduire()
    assert "creer" not in f.appels and not c.sortie.exists()


def test_v20_valeurs_reelles_du_script_de_relance(tmp_path):
    """R-4 : les valeurs réelles (sept antérieures, K′ = 8, 60417353, manifeste de la règle de la reprise) passent."""
    m = REPRISE_REELLE / "manifeste-v3-regle.json"
    if not m.is_file():
        pytest.skip("structure réelle absente")
    import runpy
    script = runpy.run_path(str(DEPOT / "runs/temoin-bailey-v1-20261111/lancer-conduite-v12.py"), run_name="essai")
    regle = json.loads(m.read_text())["regle_tours"]
    p = {"tours_complets_premiere": 8, "regle_premiere": regle, "instance_premiere": "60417353",
         "manifeste_regle": str(m), "gardes_tombees_premiere": []}
    la.verifier_relance_seule(p, la.instances_du_poste(script["ANTERIEURES"], 75.0), 75.0)
    k = an.nombre_de_tours(75.0, 15.0, 1.342111111111111, regle["t"])["K"]
    assert k == 72


@pytest.mark.parametrize("cle,valeur", [("longueur_suffixe", 99), ("ecart_10", True),
                                        ("empreintes_cibles_attendues", ["0" * 64])])
def test_v20_assemblage_refuse_mise_en_place_differente_chaque_champ(tmp_path, monkeypatch, cle, valeur):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    _modifier_etat(relance, "mise-en-place", cv.ETAT_MISE_EN_PLACE, lambda e: e.__setitem__(cle, valeur))
    with pytest.raises(GardeArret, match=f"différente de la première .« {cle} »."):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")


@pytest.mark.parametrize("cle", ["graines", "commit_public", "B"])
def test_v20_assemblage_refuse_graines_code_ou_b_differents(tmp_path, monkeypatch, cle):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    m = relance / lc.MANIFESTES["relance"]
    d = json.loads(m.read_text())
    d[cle] = {"autre": 1} if cle == "graines" else ("0" * 40 if cle == "commit_public" else 80)
    m.write_text(json.dumps(d))
    _resceller(m)
    with pytest.raises(GardeArret, match=f"« {cle} » absent ou différent"):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")


def test_v20_assemblage_refuse_manifeste_de_relance_different_r3(tmp_path, monkeypatch):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    m = relance / lc.MANIFESTES["relance"]
    d = json.loads(m.read_text())
    d["pas_par_tour"] = d["pas_par_tour"] + 1
    m.write_text(json.dumps(d))
    _resceller(m)
    with pytest.raises(GardeArret, match="manifeste de relance différent de la première règle .« pas_par_tour »."):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")


def test_v20_assemblage_refuse_manifeste_absent_sans_creer_la_cible(tmp_path, monkeypatch):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    (relance / lc.MANIFESTES["mise-en-place"]).unlink()
    with pytest.raises(GardeArret, match="manifeste « mise-en-place » de la conduite de relance absent"):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")
    assert not (tmp_path / "cible").exists()


def test_v20_assemblage_message_si_mise_en_place_de_la_premiere_absente(tmp_path, monkeypatch):
    premiere, relance = _deux_sorties(tmp_path, monkeypatch)
    f = lc.dossier_de_foi(premiere / "mise-en-place")["foi"] / cv.ETAT_MISE_EN_PLACE
    f.unlink()
    with pytest.raises(GardeArret, match="mise en place de la première absent"):
        la.assembler_lecture(premiere, relance, tmp_path / "cible")


def test_v20_modules_rejoue():
    assert la.VEILLEUR_MODULE == "controle_ia.temoin_bailey.lanceur_v21"


# --- v21 : garde de durée de tour du pilote (addendum 7) ---------------------------------------------------------------

@pytest.mark.parametrize("plafond,lance_principal", [(T_REGLE + 1, True), (T_REGLE, True), (T_REGLE - 1, False)])
def test_v21_garde_duree_de_tour_du_pilote(tmp_path, monkeypatch, plafond, lance_principal):
    c, f, _ = conduite_locale(tmp_path, monkeypatch, scenario(21, principal_fini(21)))
    c.t_max_pilote_s = plafond
    bilan = c.conduire()
    assert ("principal" in f.lance) is lance_principal and f.detruites == ["77"]
    if lance_principal:
        assert "arret" not in bilan
    else:
        assert bilan["arret"].startswith("durée de tour du pilote au-delà du plafond") and "nœud" in bilan["arret"]
        assert f.lance == ["amorce", "auto-arret", "mise-en-place", "controle-juge", "pilote", "regle"]


def test_v21_sans_plafond_rien_ne_change(tmp_path, monkeypatch):
    c, f, _ = conduite_locale(tmp_path, monkeypatch, scenario(21, principal_fini(21)))
    assert c.t_max_pilote_s is None
    assert "arret" not in c.conduire() and "principal" in f.lance


def test_v21_modules():
    assert la.VEILLEUR_MODULE == "controle_ia.temoin_bailey.lanceur_v21"
    assert la.INSTANCE_MODULE == "controle_ia.temoin_bailey.instance_v16"
