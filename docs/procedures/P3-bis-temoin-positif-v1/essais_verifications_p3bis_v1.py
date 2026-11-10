"""Banc du module commun de la chaîne de P3-bis (R5), v1 : chaque garde de `verifications_p3bis_v1.py`, un cas sain et au
moins un artefact. Hors de `tests/` à dessein : `tests/` est dans l'arbre gelé (`CHEMINS_GELES`), que le commit du code
corrigé de P3-bis fixe ; ce banc vit avec la chaîne, sous `docs/` (hors de l'arbre gelé), et se joue par son chemin :

    PYTHONPATH=src python -m pytest -q -p no:cacheprovider docs/procedures/P3-bis-temoin-positif-v1/essais_verifications_p3bis_v1.py

Aucun appel externe ; aucune lecture de `registres/go.md` réel : registres et textes fabriqués dans un dossier temporaire.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
MODULE = ICI / "verifications_p3bis_v1.py"
_spec = importlib.util.spec_from_file_location("verifications_p3bis_v1", MODULE)
V = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(V)
BROUILLON9 = ICI.parents[2] / "brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon9.md"

ENTETE = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
          "|---|---|---|---|---|---|---|---|\n")
LIGNE_GO = ("| GO-2026-11-02-29 | 2026-11-02 | calcul | **Contrôle, P3-bis : témoin positif planté** … | 80 USD | "
            "2026-11-16 | Lazar | mots de Lazar |\n")
AUTRE_GO = "| GO-2026-11-08-13 | 2026-11-08 | calcul | autre course | 50 USD | 2026-11-20 | Lazar | mots |\n"
TEXTE = ("# Préenregistrement factice\n\n- GO : **GO-2026-11-02-29** (`registres/go.md` l. 217)\n"
         "- Lancement : `GO_ID=GO-2026-11-02-29`, `PREREG=prereg/P3-bis-temoin-positif-v1.md`, "
         "`BRANCHE=calcul/p3bis-reel-v1`, `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`\n")


def cli(*args, entree: str = "") -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-I", str(MODULE), *args], input=entree, capture_output=True, text=True)


def ecrire(d: Path, nom: str, texte: str) -> str:
    p = d / nom
    p.write_text(texte, encoding="utf-8")
    return str(p)


# ================================================================================================= go
@pytest.fixture
def go_ok(tmp_path):
    return ecrire(tmp_path, "p.md", TEXTE), ecrire(tmp_path, "go.md", ENTETE + LIGNE_GO + AUTRE_GO)


def test_go_sain(go_ok):
    r = cli("go", *go_ok, "2026-11-10")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "GO-2026-11-02-29 conforme" in r.stdout


def test_go_sain_dernier_jour(go_ok):
    assert cli("go", *go_ok, "2026-11-16").returncode == 0


@pytest.mark.parametrize("jour, motif", [("2026-11-17", "hors de la validité"), ("2026-11-01", "hors de la validité"),
                                         ("2026-11-1", "mal formé"), ("2026-13-40", "impossible")])
def test_go_artefact_jour(go_ok, jour, motif):
    r = cli("go", *go_ok, jour)
    assert r.returncode == 1 and motif in r.stderr


def test_go_artefact_date_limite_constante(go_ok, tmp_path, monkeypatch):
    # échéance du registre et date limite sont deux gardes distinctes : la constante seule refuse le 16 si elle valait le 15
    monkeypatch.setattr(V, "DATE_LIMITE_CREATION", "2026-11-15")
    with pytest.raises(SystemExit, match="après le 2026-11-15"):
        V.go(*go_ok, "2026-11-16")


@pytest.mark.parametrize("texte, motif", [
    (TEXTE.replace("**GO-2026-11-02-29**", "**GO-2026-11-08-13**"), "seul GO-2026-11-02-29"),
    (TEXTE.replace("`GO_ID=GO-2026-11-02-29`", "`GO_ID=GO-2026-11-08-13`"), "ligne « Lancement »"),
    (TEXTE + "- GO : **GO-2026-11-02-29**\n", "en double"),
    (TEXTE.replace("- GO : **GO-2026-11-02-29**", "- GO : GO-2026-11-02-29"), "absente, en double ou mal formée"),
    (TEXTE.replace("- Lancement : ", "- Lancer : "), "« - Lancement : » absente"),
])
def test_go_artefact_texte(tmp_path, texte, motif):
    r = cli("go", ecrire(tmp_path, "p.md", texte), ecrire(tmp_path, "go.md", ENTETE + LIGNE_GO), "2026-11-10")
    assert r.returncode == 1 and motif in r.stderr, r.stderr


@pytest.mark.parametrize("registre, motif", [
    (ENTETE + AUTRE_GO, "absent ou en double"),
    (ENTETE + LIGNE_GO + LIGNE_GO, "absent ou en double"),
    (ENTETE + LIGNE_GO.replace("| calcul |", "| porte |"), "GO de type « calcul »"),
    (ENTETE + LIGNE_GO.replace("| Lazar |", "| Claude |"), "accordé par Lazar"),
    (ENTETE + LIGNE_GO.replace("| 80 USD |", "| 90 USD |"), "ligne réécrite"),
    (ENTETE + LIGNE_GO.replace("| 2026-11-16 |", "| 2026-11-30 |"), "ligne réécrite"),
    (ENTETE + LIGNE_GO + "| GO-2026-11-10-01 | 2026-11-10 | calcul | trop | de | colonnes | Lazar | x | y |\n",
     "8 colonnes attendues"),
    (ENTETE + LIGNE_GO + "| GO-2026-11-10-02 | 2026-11-10 | révocation | GO-2026-11-02-29 retiré | — | 2026-11-10 | "
     "Lazar | mot |\n", "révoqué au registre des GO (GO-2026-11-10-02)"),
    (ENTETE + LIGNE_GO + "| GO-2026-11-10-03 | 2026-11-10 | révocation | P3-bis arrêté | — | 2026-11-10 | Lazar | "
     "révoque GO-2026-11-02-29 |\n", "révoqué au registre des GO (GO-2026-11-10-03)"),
])
def test_go_artefact_registre(tmp_path, registre, motif):
    r = cli("go", ecrire(tmp_path, "p.md", TEXTE), ecrire(tmp_path, "go.md", registre), "2026-11-10")
    assert r.returncode == 1 and motif in r.stderr, r.stderr


@pytest.mark.parametrize("ligne", [
    # révocation d'un autre GO : sans effet ; identifiant voisin (préfixe) : sans effet ; type autre que « révocation »
    "| GO-2026-11-10-04 | 2026-11-10 | révocation | GO-2026-11-08-13 retiré | — | 2026-11-10 | Lazar | mot |\n",
    "| GO-2026-11-10-05 | 2026-11-10 | révocation | GO-2026-11-02-290 (identifiant voisin) | — | 2026-11-10 | Lazar | m |\n",
    "| GO-2026-11-10-06 | 2026-11-10 | décision | rappel de GO-2026-11-02-29, aucune révocation | — | 2026-11-10 | Lazar | m |\n",
])
def test_go_sain_revocation_d_autre_chose(tmp_path, ligne):
    r = cli("go", ecrire(tmp_path, "p.md", TEXTE), ecrire(tmp_path, "go.md", ENTETE + LIGNE_GO + ligne), "2026-11-10")
    assert r.returncode == 0, r.stderr


def test_go_artefact_registre_absent(tmp_path):
    r = cli("go", ecrire(tmp_path, "p.md", TEXTE), str(tmp_path / "absent.md"), "2026-11-10")
    assert r.returncode == 1 and "absent ou illisible" in r.stderr


# ================================================================================================= instances
def inst(ident, actual="running", cur="running", dph=1.5, **k):
    d = {"id": ident, "actual_status": actual, "cur_state": cur, "dph_total": dph}
    d.update(k)
    return d


TOL = "58936096 58936099 58936100"
ARRETEES = [inst(58936096, "exited", "stopped"), inst(58936099, "exited", "stopped"), inst(58936100, "stopped", "stopped")]


def run_inst(tmp_path, liste, en_marche="-", registre=ENTETE + LIGNE_GO + AUTRE_GO, tol=TOL):
    j = tmp_path / "lancement.txt"
    return cli("instances", tol, en_marche, ecrire(tmp_path, "go.md", registre), str(j), entree=json.dumps(liste)), j


def test_instances_sain_tolerees_seules(tmp_path):
    r, j = run_inst(tmp_path, ARRETEES)
    assert r.returncode == 0 and r.stdout.strip() == "0.0000", r.stderr
    assert "58936096 (exited, stopped)" in j.read_text()


def test_instances_sain_compte_vide(tmp_path):
    r, _ = run_inst(tmp_path, [])
    assert r.returncode == 0 and r.stdout.strip() == "0.0000"


def test_instances_sain_nommee_en_marche(tmp_path):
    r, j = run_inst(tmp_path, ARRETEES + [inst(61000001, dph=1.25)], "61000001:GO-2026-11-08-13")
    assert r.returncode == 0 and r.stdout.strip() == "1.2500", r.stderr
    assert "61000001 (running, running, 1.250 USD/h, GO-2026-11-08-13)" in j.read_text()


@pytest.mark.parametrize("liste, en_marche, motif", [
    (ARRETEES + [inst(61000002)], "-", "61000002 (running, running)"),                          # inconnue en marche
    (ARRETEES + [inst(61000002, "exited", "stopped")], "-", "61000002 (exited, stopped)"),      # inconnue arrêtée
    ([inst(58936096)] + ARRETEES[1:], "-", "tolérée seulement arrêtée"),                         # tolérée relancée
    (ARRETEES + [inst(61000001, "exited", "stopped")], "61000001:GO-2026-11-08-13", "nommée en marche mais arrêtée"),
    (ARRETEES, "61000001:GO-2026-11-08-13", "absentes du compte : 61000001"),
    (ARRETEES + [inst(61000001, dph="1.2")], "61000001:GO-2026-11-08-13", "prix illisible"),
    (ARRETEES + ["illisible"], "-", "entrée illisible"),
])
def test_instances_artefact(tmp_path, liste, en_marche, motif):
    r, j = run_inst(tmp_path, liste, en_marche)
    assert r.returncode == 1 and "aucune création" in r.stderr, r.stderr
    assert motif in j.read_text()


@pytest.mark.parametrize("en_marche, registre, motif", [
    ("61000001:GO-2026-11-30-01", ENTETE + LIGNE_GO, "absent, en double"),
    ("61000001:GO-2026-11-08-13", ENTETE + LIGNE_GO + AUTRE_GO.replace("| calcul |", "| décision |"), "pas un GO de calcul"),
    ("61000001:GO-2026-11-08-13", ENTETE + LIGNE_GO + AUTRE_GO
     + "| GO-2026-11-10-07 | 2026-11-10 | révocation | GO-2026-11-08-13 | — | 2026-11-10 | Lazar | m |\n", "révoqué"),
    ("61000001", ENTETE + LIGNE_GO, "ID:GO-…"),
    ("61000001:GO-2026-11-08-13,61000001:GO-2026-11-08-13", ENTETE + LIGNE_GO + AUTRE_GO, "ID:GO-…"),
    ("58936096:GO-2026-11-08-13", ENTETE + LIGNE_GO + AUTRE_GO, "à la fois tolérée"),
])
def test_instances_artefact_argument(tmp_path, en_marche, registre, motif):
    r, _ = run_inst(tmp_path, ARRETEES + [inst(61000001)], en_marche, registre)
    assert r.returncode == 1 and motif in r.stderr, r.stderr


def test_instances_artefact_reponse_illisible(tmp_path):
    j = tmp_path / "l.txt"
    r = cli("instances", TOL, "-", ecrire(tmp_path, "go.md", ENTETE + LIGNE_GO), str(j), entree="erreur factice")
    assert r.returncode == 1 and "illisible" in r.stderr


def test_instances_artefact_tolerees_non_epinglees(tmp_path):
    r, _ = run_inst(tmp_path, [], tol="A_EPINGLER")
    assert r.returncode == 1 and "non épinglées" in r.stderr


# ================================================================================================= offres
def offre(ident=111, **k):
    o = {"id": ident, "machine_id": 7100 + ident, "host_id": 8100 + ident, "gpu_name": "A100 SXM4", "gpu_ram": 81920,
         "num_gpus": 1, "cpu_name": "AMD EPYC 7513 32-Core Processor", "cpu_cores_effective": 32.0, "cpu_ram": 257000,
         "disk_space": 200.0, "cuda_max_good": 13.0, "reliability2": 0.989, "dph_total": 1.10, "inet_down_cost": 0.026,
         "storage_total_cost": 0.05}
    o.update(k)
    return o


def run_offres(tmp_path, liste, repli="0"):
    brut = ecrire(tmp_path, "brut.json", json.dumps(liste) if not isinstance(liste, str) else liste)
    sortie, j, relues = tmp_path / "offre.json", tmp_path / "lancement.txt", tmp_path / "relues.json"
    return cli("offres", brut, str(sortie), str(j), str(relues), repli), sortie, j


def test_offres_sain_moins_chere(tmp_path):
    r, sortie, j = run_offres(tmp_path, [offre(111, dph_total=1.30), offre(222, dph_total=1.08), offre(333, dph_total=1.08)])
    assert r.returncode == 0 and r.stdout.strip() == "222 1.08", r.stderr
    assert json.loads(sortie.read_text())["id"] == 222
    assert "processeur AMD EPYC 7513 32-Core Processor exigé" in j.read_text()


def test_offres_sain_bornes_atteintes(tmp_path):
    r, _, _ = run_offres(tmp_path, [offre(dph_total=2.10, reliability2=0.98, cpu_cores_effective=30, cpu_ram=128000,
                                          disk_space=80, storage_total_cost=0.08, inet_down_cost=0.05)])
    assert r.returncode == 0 and r.stdout.startswith("111 "), r.stderr


def test_offres_sain_repli_sans_processeur(tmp_path):
    autre = offre(444, cpu_name="AMD EPYC 7763 64-Core Processor", dph_total=1.5)
    r, _, j = run_offres(tmp_path, [autre], repli="1")
    assert r.returncode == 0 and r.stdout.strip() == "444 1.5"
    assert "repli écrit : condition du processeur retirée" in j.read_text()


@pytest.mark.parametrize("champ, valeur", [
    ("dph_total", 2.11), ("dph_total", 0), ("dph_total", "1.0"), ("reliability2", 0.979), ("cpu_cores_effective", 29.9),
    ("cpu_ram", 127999), ("disk_space", 79), ("storage_total_cost", 0.081), ("inet_down_cost", 0.051),
    ("inet_down_cost", -0.01), ("gpu_name", "A100 PCIE"), ("gpu_ram", 40960), ("num_gpus", 2), ("cuda_max_good", 12.4),
    ("cpu_name", "AMD EPYC 7763 64-Core Processor"), ("id", "111"), ("reliability2", None)])
def test_offres_artefact_hors_bornes(tmp_path, champ, valeur):
    o = offre()
    o[champ] = valeur
    if champ == "reliability2" and valeur is None:
        del o["reliability2"]
    r, sortie, _ = run_offres(tmp_path, [o])
    assert r.returncode == 3 and not sortie.exists(), (champ, valeur, r.stdout, r.stderr)


@pytest.mark.parametrize("champ, valeur", [("cpu_cores_effective", 29), ("dph_total", 2.2), ("reliability2", 0.97)])
def test_offres_artefact_repli_ne_relache_que_le_processeur(tmp_path, champ, valeur):
    o = offre(cpu_name="Intel Xeon")
    o[champ] = valeur
    r, _, _ = run_offres(tmp_path, [o], repli="1")
    assert r.returncode == 3


def test_offres_artefact_moins_chere_non_conforme_ecartee(tmp_path):
    r, _, _ = run_offres(tmp_path, [offre(111, dph_total=0.5, cpu_cores_effective=16), offre(222, dph_total=1.9)])
    assert r.returncode == 0 and r.stdout.strip() == "222 1.9"


@pytest.mark.parametrize("liste, code", [("non json", 2), ('{"a": 1}', 2), ([offre(111), offre(111)], 2)])
def test_offres_artefact_reponse(tmp_path, liste, code):
    r, _, _ = run_offres(tmp_path, liste)
    assert r.returncode == code


def test_offres_artefact_repli_mal_forme(tmp_path):
    r, _, _ = run_offres(tmp_path, [offre()], repli="oui")
    assert r.returncode == 1 and "REPLI" in r.stderr


# ================================================================================================= crédit
@pytest.mark.parametrize("credit, somme, code", [(20.0, "0.0000", 0), (19.99, "0.0000", 3), (34.0, "1.4000", 0),
                                                 (33.99, "1.4000", 3), (1000, "0", 0)])
def test_credit(credit, somme, code):
    r = cli("credit", somme, entree=json.dumps({"credit": credit, "email": "x@invalid"}))
    assert r.returncode == code, r.stdout
    assert "minimum" in r.stdout


@pytest.mark.parametrize("entree", ["erreur", '{"credit": "20"}', '{"solde": 30}', '{"credit": true}'])
def test_credit_artefact_illisible(entree):
    r = cli("credit", "0", entree=entree)
    assert r.returncode == 2 and "illisible" in r.stdout


def test_credit_artefact_somme(tmp_path):
    assert cli("credit", "-1", entree='{"credit": 50}').returncode == 1


# ================================================================================================= identifiant
def test_identifiant_sain(tmp_path):
    lanc = ecrire(tmp_path, "lancement.txt", "commit abc\ninstance 61234567\n")
    assert cli("identifiant", "61234567", lanc).returncode == 0


@pytest.mark.parametrize("ident, lancement, motif", [
    ("58936096", "instance 58936096\n", "ARRETEES_TOLEREES"),
    ("58936099", "instance 61234567\n", "ARRETEES_TOLEREES"),
    ("61234568", "instance 61234567\n", "ce lanceur a créé 61234567"),
    ("61234567", "instance 61234567\ninstance 61234567\n", "plusieurs lignes"),
    ("61234567", "offre 61234567\n", "aucune ou plusieurs"),
    ("6123x", "instance 6123x\n", "mal formé"),
])
def test_identifiant_artefact(tmp_path, ident, lancement, motif):
    r = cli("identifiant", ident, ecrire(tmp_path, "lancement.txt", lancement))
    assert r.returncode == 1 and motif in r.stderr


# ================================================================================================= état, motif
def test_etat():
    assert cli("etat", entree='{"actual_status": "running", "cur_state": "running"}').stdout.startswith(
        "actual_status=running cur_state=running")
    assert cli("etat", entree="pas du json").stdout.startswith("illisible: ")


A1 = "AMORCE 2026-11-12T08:00:00Z : commit " + "a" * 40
P1 = "PROGRES 2026-11-12T09:00:00Z etape=entrainement concept=tromperie"


def run_motif(tmp_path, journal, progres=None):
    j = ecrire(tmp_path, "j.txt", "\n".join(journal) + "\n")
    p = ecrire(tmp_path, "p.txt", "\n".join(progres if progres is not None else [x for x in journal if x.startswith(("AMORCE", "PROGRES"))]) + "\n")
    r = cli("motif", j, p)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip().split("\t")


def test_motif_aucun(tmp_path):
    assert run_motif(tmp_path, [A1, P1])[0] == "AUCUN"


def test_motif_fin_normale(tmp_path):
    m = run_motif(tmp_path, [A1, P1, "2026-11-12T12:00:00Z run : processus 4242 fini, code 0",
                             "AMORCE 2026-11-12T12:30:00Z : fin, code 0"])
    assert m == ["FIN", "AMORCE 2026-11-12T12:30:00Z : fin, code 0"]


def test_motif_fin_run_complet_malgre_code(tmp_path):
    m = run_motif(tmp_path, [A1, "x run : processus 4242 fini, code 1",
                             "x run : code 1, mais résumé écrit sans arrêt consigné : run complet",
                             "AMORCE 2026-11-12T12:30:00Z : fin, code 0"])
    assert m[0] == "FIN"


def test_motif_garder_code_5(tmp_path):
    m = run_motif(tmp_path, [A1, "x run : processus 4242 fini, code 0", "AMORCE 2026-11-12T12:30:00Z : fin, code 5"])
    assert m[0] == "GARDER" and "jamais détruite" in m[1]


def test_motif_garder_ligne_second_paquet_meme_code_1(tmp_path):
    m = run_motif(tmp_path, [A1, "x SECOND PAQUET EN ÉCHEC (relecture fausse) : aucun fichier du run poussé en clair",
                             "AMORCE 2026-11-12T12:30:00Z : fin, code 1"])
    assert m[0] == "GARDER"


def test_motif_second_paquet_sans_fin_attend(tmp_path):
    # la poussée des traces n'est jamais coupée : on attend la fin de l'amorce
    assert run_motif(tmp_path, [A1, "x SECOND PAQUET EN ÉCHEC (sel absent)"])[0] == "AUCUN"


def test_motif_processus_mort(tmp_path):
    m = run_motif(tmp_path, [A1, P1, "x run : processus 4242 fini, code 137", "AMORCE 2026-11-12T12:30:00Z : fin, code 1"])
    assert m[0] == "PROCESSUS MORT" and "4242" in m[1] and "137" in m[1]


def test_motif_echec_amorce(tmp_path):
    assert run_motif(tmp_path, [A1, "AMORCE : clonage impossible (jeton GitHub ?)"])[0] == "ÉCHEC D'AMORCE"


def test_motif_redemarrage(tmp_path):
    a2 = "AMORCE 2026-11-12T08:05:00Z : commit " + "a" * 40
    assert run_motif(tmp_path, [a2], progres=[A1, P1, a2])[0] == "REDÉMARRAGE"


def test_motif_journal_illisible_garde_le_releve(tmp_path):
    p = ecrire(tmp_path, "p.txt", A1 + "\n")
    r = cli("motif", "-", p)
    assert r.stdout.startswith("AUCUN")


# ================================================================================================= dépense
def run_dep(entree, creation=1_000_000, maintenant=1_000_000 + 3600, offre="2.0", anterieure="0", intervalle="120"):
    return cli("depense", str(creation), str(maintenant), offre, anterieure, intervalle, entree=entree)


def test_depense_sain_sous_plafond():
    r = run_dep(json.dumps({"dph_total": 2.0, "inet_down_billed": 20, "inet_down_cost": 0.026}))
    assert r.returncode == 0 and "dépense 2.52 USD" in r.stdout, r.stdout


def test_depense_artefact_plafond_atteint():
    r = run_dep(json.dumps({"dph_total": 2.0, "inet_down_billed": 0, "inet_down_cost": 0.02}), maintenant=1_000_000 + 36 * 3600,
                anterieure="8")
    assert r.returncode == 3 and "projetée" in r.stdout, r.stdout


def test_depense_artefact_plafond_au_prochain_releve():
    # 79,95 USD maintenant ; 120 s de plus à 2,10 USD/h : 80,02 ≥ 80 → arrêt avant de dépasser
    r = run_dep(json.dumps({"dph_total": 2.10, "inet_down_billed": 0, "inet_down_cost": 0.02}), maintenant=1_000_000 + 3600,
                offre="2.10", anterieure=str(79.95 - 2.10))
    assert r.returncode == 3, r.stdout


def test_depense_artefact_prix_illisible_borne_prise():
    r = run_dep("pas du json", offre="1.0")
    assert r.returncode == 0 and "prix relu illisible : 2.10 USD/h pris" in r.stdout
    assert "majorant 2.00 USD pris" in r.stdout


def test_depense_prix_relu_plus_haut_que_l_offre():
    r = run_dep(json.dumps({"dph_total": 1.9, "inet_down_billed": 0, "inet_down_cost": 0}), offre="1.0")
    assert "à 1.9000 USD/h" in r.stdout


@pytest.mark.parametrize("args", [("x", "1", "1", "0", "1"), ("10", "5", "1", "0", "1"), ("1", "2", "0", "0", "1"),
                                  ("1", "2", "1", "-1", "1")])
def test_depense_artefact_arguments(args):
    assert cli("depense", *args, entree="{}").returncode == 1


# ================================================================================================= valeurs, constantes
def test_valeurs_sain_brouillon9():
    r = cli("valeurs", str(BROUILLON9))
    assert r.returncode == 0, r.stderr


def test_valeurs_artefact(tmp_path):
    t = BROUILLON9.read_text(encoding="utf-8").replace("2,10 USD de l'heure", "2,50 USD de l'heure")
    r = cli("valeurs", ecrire(tmp_path, "p.md", t))
    assert r.returncode == 1 and "2,10" in r.stderr


def test_constantes_sain_et_artefact(tmp_path):
    for f in {f for f, _ in V.CONSTANTES}:
        (tmp_path / f).write_text("#!/usr/bin/env bash\n" + "".join(
            f"{n}={v}                 # commentaire\n" for (g, n), v in V.CONSTANTES.items() if g == f), encoding="utf-8")
    assert cli("constantes", str(tmp_path)).returncode == 0
    p = tmp_path / "lancer_p3bis_v1.sh"
    p.write_text(p.read_text().replace("GO_CALCUL=GO-2026-11-02-29", "GO_CALCUL=GO-2026-11-08-13"))
    r = cli("constantes", str(tmp_path))
    assert r.returncode == 1 and "GO_CALCUL" in r.stderr
    p.write_text(p.read_text().replace("GO_CALCUL=GO-2026-11-08-13", "GO_CALCUL=GO-2026-11-02-29\nGO_CALCUL=GO-2026-11-02-29"))
    assert cli("constantes", str(tmp_path)).returncode == 1


def test_constantes_reelles_de_la_chaine():
    # la chaîne versée à côté de ce banc porte les constantes du module
    manquants = [f for f, _ in V.CONSTANTES if not (ICI / f).exists()]
    if manquants:
        pytest.skip(f"scripts pas encore écrits : {sorted(set(manquants))}")
    r = cli("constantes", str(ICI))
    assert r.returncode == 0, r.stderr


# ================================================================================================= configuration
CFG_P3 = ICI.parents[2] / "prereg/P3-premier-test-config-v1.json"
CFG_B1 = ICI.parents[2] / "brouillons/P3-bis-temoin-positif-v1/P3-bis-temoin-positif-config-v1-brouillon1.json"


def cfg_saine(tmp_path, **changes):
    import hashlib
    cons = tmp_path / "consignes.md"
    cons.write_text("consignes factices\n", encoding="utf-8")
    c = json.loads(CFG_B1.read_text(encoding="utf-8"))
    c["consignes_sha256"] = hashlib.sha256(cons.read_bytes()).hexdigest()
    for k, v in changes.items():
        if v == "SUPPRIMER":
            del c[k]
        else:
            c[k] = v
    return ecrire(tmp_path, "cfg.json", json.dumps(c, indent=1)), str(cons)


def test_config_saine_brouillon1_rempli(tmp_path):
    cfg, cons = cfg_saine(tmp_path)
    r = cli("config", cfg, str(CFG_P3), cons)
    assert r.returncode == 0, r.stderr
    assert "budget_entrainement_s, chemin_consignes, consignes_sha256, duree_max_s, fils_entrainement" in r.stdout


@pytest.mark.parametrize("changes, motif", [
    ({"lot": 4}, "hors des écarts du texte : ['lot']"),
    ({"duree_max_s": 16200}, "duree_max_s = 16200"),
    ({"budget_entrainement_s": "SUPPRIMER"}, "budget_entrainement_s = 'absent'"),
    ({"fils_entrainement": 32}, "fils_entrainement = 32"),
    ({"chemin_consignes": "prereg/P3-consignes-v1.md"}, "chemin_consignes"),
    ({"consignes_sha256": "0" * 64}, "consignes_sha256"),
    ({"temperature": 0.7}, "temperature"),
    ({"nouvelle_cle": 1}, "nouvelle_cle"),
])
def test_config_artefact(tmp_path, changes, motif):
    cfg, cons = cfg_saine(tmp_path, **changes)
    r = cli("config", cfg, str(CFG_P3), cons)
    assert r.returncode == 1 and motif in r.stderr, r.stderr


def test_config_artefact_brouillon1_non_rempli(tmp_path):
    cons = ecrire(tmp_path, "c.md", "x\n")
    r = cli("config", str(CFG_B1), str(CFG_P3), cons)
    assert r.returncode == 1 and "consignes_sha256" in r.stderr


# ================================================================================================= longueurs
def mesure(n=60, a=88, t=88, b=90):
    return {"par_tache": [{"tache": f"t{i}", **{m: {"saboteur": a + (i % 2), "temoin": t + (i % 2), "mention": b}
                                               for m in V.MESURES}} for i in range(n)]}


def test_longueurs_sain(tmp_path):
    me = mesure()
    at = V.resume_longueurs(me["par_tache"])
    r = cli("longueurs", ecrire(tmp_path, "m.json", json.dumps(me)), ecrire(tmp_path, "a.json", json.dumps(at)))
    assert r.returncode == 0, r.stderr


def test_longueurs_artefact_a_differe_de_t(tmp_path):
    me = mesure()
    at = V.resume_longueurs(me["par_tache"])
    me["par_tache"][7]["indication_gabarit"]["temoin"] += 1
    r = cli("longueurs", ecrire(tmp_path, "m.json", json.dumps(me)), ecrire(tmp_path, "a.json", json.dumps(at)))
    assert r.returncode == 1 and "t7 : indication_gabarit" in r.stderr


def test_longueurs_artefact_resume_autre(tmp_path):
    at = V.resume_longueurs(mesure()["par_tache"])
    r = cli("longueurs", ecrire(tmp_path, "m.json", json.dumps(mesure(b=91))), ecrire(tmp_path, "a.json", json.dumps(at)))
    assert r.returncode == 1 and "résumé" in r.stderr


def test_longueurs_artefact_mesure_vide(tmp_path):
    r = cli("longueurs", ecrire(tmp_path, "m.json", '{"par_tache": []}'), ecrire(tmp_path, "a.json", "{}"))
    assert r.returncode == 1


# ================================================================================================= preuves
def journal_banc(d: Path, nom: str, scripts=None, verdict=None, extra=""):
    v, attendus = V.JOURNAUX[nom]
    lignes = [f"script éprouvé : {s} {'0' * 63}{i % 10}" for i, s in enumerate(sorted(scripts or attendus))]
    (d / nom).write_text("\n".join(lignes) + "\n" + extra + (verdict or v) + "\n", encoding="utf-8")


def test_preuves_sain(tmp_path):
    for nom in ["banc-verifications-p3bis-v1.log"]:
        journal_banc(tmp_path, nom)
    r = cli("preuves", str(tmp_path), "banc-verifications-p3bis-v1.log")
    assert r.returncode == 0 and len(r.stdout.split("\n")) >= 2


@pytest.mark.parametrize("kw, motif", [
    ({"verdict": "FIN DU BANC ; cas non conformes : 1"}, "dernière ligne"),
    ({"extra": "cas 4 : NON CONFORME\n"}, "ligne d'échec"),
    ({"scripts": {"verifications_p3bis_v1.py"}}, "manquants"),
    ({"extra": "script éprouvé : lancer_p3bis_v1.sh zzz\n"}, "mal formée"),
])
def test_preuves_artefact(tmp_path, kw, motif):
    journal_banc(tmp_path, "banc-verifications-p3bis-v1.log", **kw)
    r = cli("preuves", str(tmp_path), "banc-verifications-p3bis-v1.log")
    assert r.returncode == 1 and motif in r.stderr, r.stderr


def test_preuves_artefact_deux_empreintes(tmp_path):
    journal_banc(tmp_path, "banc-verifications-p3bis-v1.log")
    journal_banc(tmp_path, "banc-lanceur-p3bis-v1.log")
    p = tmp_path / "banc-lanceur-p3bis-v1.log"
    p.write_text(p.read_text().replace("verifications_p3bis_v1.py " + "0" * 63, "verifications_p3bis_v1.py " + "1" * 63))
    r = cli("preuves", str(tmp_path), "banc-verifications-p3bis-v1.log", "banc-lanceur-p3bis-v1.log")
    assert r.returncode == 1 and "deux empreintes" in r.stderr


def test_preuves_artefact_journal_absent_ou_inconnu(tmp_path):
    assert cli("preuves", str(tmp_path), "banc-lanceur-p3bis-v1.log").returncode == 1
    assert cli("preuves", str(tmp_path), "banc-inconnu.log").returncode == 1


def test_usage():
    assert cli("inconnue").returncode == 2
    assert cli("go", "un").returncode == 2
