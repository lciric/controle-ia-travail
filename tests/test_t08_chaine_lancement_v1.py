"""Essais (R5) de la chaîne de lancement de T0.8 : module de session (`lancement_t08.session_v1`), lanceur
(`scripts/lancer_t08_v1.sh`, faux outil de location, dépôt distant jetable), garde de calcul sur la commande imprimée, minuterie
de l'amorce (`scripts/amorce_instance_t08_v1.sh`). Aucun réseau, aucun appel au loueur, aucune dépense ; données factices."""
from __future__ import annotations

import json
import os
import subprocess
import time
from datetime import date, timedelta
from pathlib import Path

import pytest

import aide_t08_chaine_v1 as A
from controle_ia.lancement_t08 import session_v1 as S
from controle_ia.t06.session import GardeSession

RACINE = Path(__file__).resolve().parents[1]
LANCEUR = RACINE / "scripts" / "lancer_t08_v1.sh"
AMORCE = RACINE / "scripts" / "amorce_instance_t08_v1.sh"
HOOK = RACINE / ".claude" / "hooks" / "garde_calcul.py"
J = date.today()


def _config():
    return {"lancement": A.lancement_factice()}


def _reg(tmp_path, **k) -> Path:
    p = tmp_path / "go.md"
    p.write_text(A.registre_go(**k), encoding="utf-8")
    return p


# --- 1. session : ligne de GO, prolongation, calendrier, vue de l'offre, compte rendu ----------------------------------------

def test_session_go_origine_et_prolongation(tmp_path):
    r = S.go_t08(_reg(tmp_path), _config(), A.ORIGINE, J)
    assert r["plafond_usd"] == 120 and r["origine"] == A.ORIGINE and r["echeance"] == str(J + timedelta(days=3))
    r = S.go_t08(_reg(tmp_path, origine_echue=True), _config(), A.PROLONGATION, J)          # origine échue, prolongation valide
    assert r["go"] == A.PROLONGATION and r["plafond_usd"] == 120 and r["echeance"] == str(J + timedelta(days=30))
    c = S.calendrier_t08(_reg(tmp_path), _config(), A.PROLONGATION, J)
    assert c["dernier_jour_creation"] == str(J + timedelta(days=30)) and c["fin_go_utc_s"] > 0


@pytest.mark.parametrize("cas, motif", [
    ("origine_echue", "hors de sa période"), ("non_admise", "hors des lignes admises"), ("echue_admise", "pas une prolongation|hors de sa période"),
    ("revoquee_origine", "révoqué"), ("revoquee_prolongation", "révoqué"), ("plafond", "exact attendu"),
    ("decision", "type"), ("illisible", "illisible"), ("relance", "« course » seule"), ("prolongation_autre", "pas une prolongation")])
def test_session_go_artefacts(tmp_path, cas, motif):
    c, go, k = _config(), A.ORIGINE, {}
    if cas == "origine_echue":
        k = {"origine_echue": True}
    elif cas == "non_admise":
        go = A.ECHUE
    elif cas == "echue_admise":
        c["lancement"]["go_admis"].append(A.ECHUE)
        go = A.ECHUE
        c["lancement"]["go_origine"] = c["lancement"]["go_admis"][0]
    elif cas == "revoquee_origine":
        k, go = {"revocation": A.ORIGINE}, A.PROLONGATION
    elif cas == "revoquee_prolongation":
        k, go = {"revocation": A.PROLONGATION}, A.PROLONGATION
    elif cas == "plafond":
        k = {"plafond": "200 USD"}
    elif cas == "decision":
        c["lancement"]["go_admis"].append(A.DECISION)
        go = A.DECISION
    elif cas == "illisible":
        go = "GO-X"
    elif cas == "relance":
        c["lancement"]["carte"]["relance"] = {"nom": "H200 NVL", "nom_offre": "H200 NVL"}
    elif cas == "prolongation_autre":
        c["lancement"]["go_admis"].append(A.ECHUE)
        go = A.ECHUE
        k = {}
    reg = _reg(tmp_path, **k)
    if cas == "prolongation_autre":           # ligne admise, valide, mais dont le périmètre n'est pas une prolongation de l'origine
        reg.write_text(reg.read_text().replace(f"| {A.ECHUE} | {J - timedelta(days=12)}", f"| {A.ECHUE} | {J}")
                       .replace(f"autre accord échu | 50 USD | {J - timedelta(days=1)}", f"autre accord | 50 USD | {J + timedelta(days=2)}"))
    with pytest.raises(GardeSession, match=motif):
        S.go_t08(reg, c, go, J)


def test_session_vue_offre_sans_relance_ni_h200(tmp_path):
    v = S.vue_offre(_config())
    assert set(v["carte"]) == {"course"} and v["offre"]["disque_min_go"] == 100 and v["carte"]["course"]["prix_max_usd_h"] == 1.3
    c = _config()
    c["lancement"]["carte"]["course"]["nom_offre"] = "H200 NVL"
    with pytest.raises(GardeSession, match="H200"):
        S.vue_offre(c)


def test_session_choix_d_offre_bornes_et_h200(tmp_path):
    v = S.vue_offre(_config())
    o = {**A.OFFRE_A100}
    r = S.s12.choisir_offre([o], v, "course")
    assert r["id"] == 1
    for mauvaise, motif in ((A.OFFRE_H200, "carte"), (A.OFFRE_CHERE, "prix"), ({**o, "cpu_ram": 32000}, "mémoire vive"),
                            ({**o, "gpu_ram": 40960}, "mémoire de carte"), ({**o, "cpu_cores_effective": 4.0}, "cœurs")):
        with pytest.raises(GardeSession):
            S.s12.choisir_offre([mauvaise], v, "course")
    with pytest.raises(KeyError):
        S.s12.filtre_recherche(v, "relance")                # aucune carte de relance dans la vue
    f = S.s12.filtre_recherche(v, "course")
    assert "gpu_name=A100_SXM4" in f and "dph_total<=1.3" in f and "cpu_cores_effective>=8" in f and "disk_space>=100" in f


def test_session_surveillance_compte_rendu_a_40_usd():
    base = dict(plafond="120", prix_carte="1.0", prix_stockage="0.02", anterieure_usd="0", telechargement_usd="0.4")
    now = 1_800_000_000
    d = S.s3.depense_cumulee_v3(**base, cree_le_s=now - 3600 * 10, maintenant_s=now)
    assert S.decider_surveillance_t08("", now, d, 40) == "POURSUIVRE"                      # ≈ 10,6 USD
    d = S.s3.depense_cumulee_v3(**base, cree_le_s=now - 3600 * 45, maintenant_s=now)
    assert S.decider_surveillance_t08("", now, d, 40).startswith("ALERTE compte rendu")    # ≈ 46 USD : alerte, aucun arrêt
    d = S.s3.depense_cumulee_v3(**base, cree_le_s=now - 3600 * 120, maintenant_s=now)
    assert S.decider_surveillance_t08("", now, d, 40).startswith("ARRET depense")          # ≥ 120 USD : arrêt
    j = "PROGRES 2026-01-01T00:00:00Z etape=x\n"
    d = S.s3.depense_cumulee_v3(**base, cree_le_s=now - 3600, maintenant_s=now)
    assert S.decider_surveillance_t08(j, now, d, 40).startswith("ALERTE sans PROGRES")     # deux heures sans progression : alerte


# --- 2. lanceur, faux outil de location ---------------------------------------------------------------------------------

@pytest.fixture
def monde(tmp_path):
    m = A.monde_lancement(tmp_path / "m")
    (tmp_path / "offres.json").write_text(json.dumps([A.OFFRE_H200, A.OFFRE_CHERE, A.OFFRE_A100]))
    return m


def lancer(m, tmp_path, *args, **env):
    return subprocess.run(["bash", str(LANCEUR), *map(str, args)], env=A.env_lanceur(m, tmp_path, **env),
                          capture_output=True, text=True, timeout=300)


def test_lanceur_cas_sain_controles_creation_apres_creation_surveillance(monde, tmp_path):
    d = tmp_path / "dossier"
    r = lancer(monde, tmp_path, "controles", d)
    assert r.returncode == 0, r.stdout + r.stderr
    l = (d / "lancement.txt").read_text()
    assert f"commit {monde['ccode']}" in l and f"entree {monde['entree']}" in l and f"go {A.ORIGINE}" in l
    assert "plafond 120" in l and "compte_rendu 40" in l and (d / "vue-offre.json").is_file()
    r = lancer(monde, tmp_path, "creation", "auto", "course", "12.5", d)
    assert r.returncode == 0, r.stdout + r.stderr
    cmd = r.stdout.strip().splitlines()[-1]
    assert cmd.startswith(f"GO_ID={A.ORIGINE} timeout -k 10 300 vastai create instance 1 ")      # l'offre A100 (ni H200, ni chère)
    for x in (f"-e COMMIT={monde['ccode']}", f"-e ENTREE_COMMIT={monde['entree']}", "-e BRANCHE_ENTREE=entree/t08-course-v1",
              "-e BRANCHE=calcul/t08-course-v1", f"-e GO_ID_T08={A.ORIGINE}", "--disk 100", "--label t08-v1",
              "-e HF_TOKEN=$HF_TOKEN", "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN", "lancer_t08_v1.sh apres-creation"):
        assert x in cmd, x
    assert "hf-jeton-factice" not in r.stdout and "gh-jeton-factice" not in r.stdout                # jetons par leur nom seulement
    l = (d / "lancement.txt").read_text()
    assert "anterieure 12.5" in l and "plafond_creation 120" in l
    appels = (tmp_path / "appels.txt").read_text()
    assert "create" not in appels                                                                    # le lanceur n'a rien créé
    # garde de calcul : la commande imprimée est admise avec le GO valide (crochet du dépôt de travail, registre factice)
    hook = monde["clone"] / ".claude" / "hooks" / "garde_calcul.py"
    g = subprocess.run(["python3", str(hook)], input=json.dumps({"tool_input": {"command": cmd}}), capture_output=True, text=True)
    assert g.returncode == 0, g.stderr
    # après la création (sortie factice du loueur) puis surveillance jusqu'à la ligne de fin
    f = tmp_path / "creation-brute.json"
    f.write_text('{"success": true, "new_contract": 777777}\n')
    r = lancer(monde, tmp_path, "apres-creation", f, 0, d)
    assert r.returncode == 0 and "CRÉÉE : instance 777777" in r.stdout, r.stdout
    (tmp_path / "instances.json").write_text(json.dumps([{"id": 777777, "label": "t08-v1"}]))
    (tmp_path / "journal.txt").write_text("AMORCE 2026-11-27T10:00:00Z : fin, code 0\n")
    r = lancer(monde, tmp_path, "surveillance", 777777, d, FAUX_INSTANCES=str(tmp_path / "instances.json"))
    assert r.returncode == 0 and "FIN" in r.stdout and "stop instance 777777" in r.stdout, r.stdout + r.stderr


def test_lanceur_surveillance_compte_rendu_une_seule_fois(monde, tmp_path):
    d = tmp_path / "dossier"
    assert lancer(monde, tmp_path, "controles", d).returncode == 0
    assert lancer(monde, tmp_path, "creation", "auto", "course", "45", d).returncode == 0     # dépense antérieure 45 USD ≥ 40
    f = tmp_path / "creation-brute.json"
    f.write_text('{"success": true, "new_contract": 777777}\n')
    assert lancer(monde, tmp_path, "apres-creation", f, 0, d).returncode == 0
    (tmp_path / "instances.json").write_text(json.dumps([{"id": 777777, "label": "t08-v1"}]))
    (tmp_path / "journal.txt").write_text(f"AMORCE {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} : début\n")
    p = subprocess.Popen(["bash", str(LANCEUR), "surveillance", "777777", str(d)], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True, env=A.env_lanceur(monde, tmp_path, FAUX_INSTANCES=str(tmp_path / "instances.json")))
    time.sleep(8)
    (tmp_path / "journal.txt").write_text("AMORCE 2026-11-27T10:00:00Z : fin, code 0\n")
    out, err = p.communicate(timeout=120)
    assert p.returncode == 0, out + err
    assert out.count("ALERTE compte rendu") == 1, out
    assert (d / "compte-rendu-alerte.txt").is_file()


@pytest.mark.parametrize("cas, code, motif", [
    ("sans_go", 2, "GO_ID absent"), ("go_echu", 2, "hors de sa période"), ("go_non_admis", 2, "hors des lignes admises"),
    ("go_decision", 2, "hors des lignes admises"), ("amorce_autre", 2, "empreinte de l'amorce"),
    ("branche_entree_absente", 2, "branche d'entrée"), ("dossier_existant", 2, "existe déjà")])
def test_lanceur_controles_artefacts(monde, tmp_path, cas, code, motif):
    d = tmp_path / "dossier"
    env = {}
    if cas == "sans_go":
        env["GO_ID"] = None
    elif cas == "go_echu":
        env["GO_ID"] = A.ORIGINE
        (monde["clone"] / "registres" / "go.md").write_text(A.registre_go(origine_echue=True))
    elif cas == "go_non_admis":
        env["GO_ID"] = A.ECHUE
    elif cas == "go_decision":
        env["GO_ID"] = A.DECISION
    elif cas == "amorce_autre":
        env["T08_AMORCE_SHA256"] = "0" * 64
    elif cas == "branche_entree_absente":
        env["T08_BRANCHE_ENTREE"] = "entree/inexistante"
    elif cas == "dossier_existant":
        d.mkdir()
    r = lancer(monde, tmp_path, "controles", d, **env)
    assert r.returncode == code and motif in r.stdout, r.stdout + r.stderr


def test_lanceur_amorce_alteree_refusee(tmp_path):
    m = A.monde_lancement(tmp_path / "m", amorce_alteree=True)
    r = lancer(m, tmp_path, "controles", tmp_path / "d")
    assert r.returncode == 2 and "empreinte de l'amorce" in r.stdout, r.stdout


@pytest.mark.parametrize("cas, code, motif", [
    ("relance", 2, "aucune relance sur une carte H200"), ("h200_seule", 3, "aucune offre conforme"),
    ("trop_chere", 3, "aucune offre conforme"), ("memoire", 3, "aucune offre conforme"), ("instance_presente", 3, "déjà sur le compte"),
    ("depense_epuisee", 3, "déjà au plafond"), ("go_change", 2, "≠ GO des contrôles"), ("autre_offre_arg", 2, "« auto » seulement")])
def test_lanceur_creation_artefacts(monde, tmp_path, cas, code, motif):
    d = tmp_path / "dossier"
    assert lancer(monde, tmp_path, "controles", d).returncode == 0
    args, env = ["creation", "auto", "course", "0", d], {}
    if cas == "relance":
        args[2] = "relance"
    elif cas == "h200_seule":
        (tmp_path / "offres.json").write_text(json.dumps([A.OFFRE_H200]))
    elif cas == "trop_chere":
        (tmp_path / "offres.json").write_text(json.dumps([A.OFFRE_CHERE]))
    elif cas == "memoire":
        (tmp_path / "offres.json").write_text(json.dumps([{**A.OFFRE_A100, "cpu_ram": 32000}]))
    elif cas == "instance_presente":
        (tmp_path / "instances.json").write_text(json.dumps([{"id": 5, "label": "t08-v1-ancienne"}]))
        env["FAUX_INSTANCES"] = str(tmp_path / "instances.json")
    elif cas == "depense_epuisee":
        args[3] = "120"
    elif cas == "go_change":
        env["GO_ID"] = A.PROLONGATION
    elif cas == "autre_offre_arg":
        args[1] = "48448001"
    r = lancer(monde, tmp_path, *args, **env)
    assert r.returncode == code and motif in r.stdout, (cas, r.stdout + r.stderr)
    assert "create" not in (tmp_path / "appels.txt").read_text() if (tmp_path / "appels.txt").exists() else True


def test_lanceur_controles_epreuve_refusee_et_verification_seule_du_go(monde, tmp_path):
    r = lancer(monde, tmp_path, "controles-epreuve", tmp_path / "e", "0" * 40, "x.json")
    assert r.returncode == 2 and "non offerte pour T0.8" in r.stdout
    cfg = tmp_path / "config.json"
    cfg.write_text(json.dumps(monde["config"]))
    reg = str(monde["clone"] / "registres" / "go.md")
    r = lancer(monde, tmp_path, "--verifier-go-seulement", cfg, "10", T08_REGISTRE_GO=reg)
    assert r.returncode == 0 and "GO VÉRIFIÉ, RIEN CRÉÉ" in r.stdout, r.stdout
    assert lancer(monde, tmp_path, "--verifier-go-seulement", cfg, "120", T08_REGISTRE_GO=reg).returncode == 2
    assert lancer(monde, tmp_path, "--verifier-go-seulement", cfg, "0", GO_ID=A.ECHUE, T08_REGISTRE_GO=reg).returncode == 2


# --- 3. garde de calcul : admise avec un GO valide, refusée sans GO, avec un GO échu, avec un GO d'un autre type --------

@pytest.mark.parametrize("go, admis", [(A.ORIGINE, True), (A.PROLONGATION, True), (None, False), (A.ECHUE, False),
                                       (A.DECISION, False), ("GO-2099-01-01-99", False)])
def test_garde_de_calcul_sur_la_commande_de_creation(tmp_path, go, admis):
    d = tmp_path / "depot"
    (d / ".claude" / "hooks").mkdir(parents=True)
    (d / "registres").mkdir()
    (d / ".claude" / "hooks" / "garde_calcul.py").write_bytes(HOOK.read_bytes())
    (d / "registres" / "go.md").write_text(A.registre_go(), encoding="utf-8")
    cmd = ("" if go is None else f"GO_ID={go} ") + "timeout -k 10 300 vastai create instance 1 --raw --image python:3.11-bookworm --disk 100"
    g = subprocess.run(["python3", str(d / ".claude" / "hooks" / "garde_calcul.py")],
                       input=json.dumps({"tool_input": {"command": cmd}}), capture_output=True, text=True)
    assert (g.returncode == 0) == admis, g.stderr


# --- 4. minuterie de l'amorce : cas sain (heure non atteinte : rien) ; artefact (heure passée : consignation puis destruction)

CURL_FACTICE = """#!/usr/bin/env bash
m=GET; while [ $# -gt 0 ]; do case "$1" in -X) m="$2"; shift;; -o) o="$2"; shift;; -w) shift;; esac; shift; done
echo "$m $(date +%s%N)" >> "$FAUX_CURL_JOURNAL"
[ -n "${o:-}" ] && echo '{"success": true}' > "$o"
printf 200
"""


def _minuterie(tmp_path) -> Path:
    r = tmp_path / "racine"
    r.mkdir()
    e = {k: os.environ[k] for k in ("PATH", "LANG") if k in os.environ}
    e.update(RACINE_AMORCE=str(r), AMORCE_ESSAI_LOCAL="1", HOME=str(tmp_path))
    subprocess.run(["bash", str(AMORCE)], env=e, capture_output=True, text=True, timeout=60)     # refus précoce (FIN_GO absente)
    assert (r / "t08-minuterie.sh").is_file()
    assert "refus" in (r / "t08-detruire").read_text()                                            # posé par le refus précoce de l'essai
    (r / "t08-detruire").unlink()
    (tmp_path / "bin").mkdir()
    (tmp_path / "bin" / "curl").write_text(CURL_FACTICE)
    (tmp_path / "bin" / "curl").chmod(0o755)
    (r / "t08-consigner.sh").write_text(f'#!/usr/bin/env bash\necho "consigne $1 $(date +%s%N)" >> "{tmp_path}/consigne.txt"\n')
    return r


def _env_minuterie(tmp_path):
    e = {k: os.environ[k] for k in ("PATH", "LANG") if k in os.environ}
    e.update(PATH=f"{tmp_path / 'bin'}:{e['PATH']}", CONTAINER_ID="424242", CONTAINER_API_KEY="cle-factice", MINUTERIE_PAS_S="1",
             MINUTERIE_REESSAI_S="1", FAUX_CURL_JOURNAL=str(tmp_path / "curl.txt"), HOME=str(tmp_path))
    return e


def test_minuterie_cas_sain_heure_non_atteinte_rien(tmp_path):
    r = _minuterie(tmp_path)
    now = int(time.time())
    p = subprocess.Popen(["bash", str(r / "t08-minuterie.sh"), str(now + 3600), str(now + 3600), str(r), "https://api.invalid/v0"],
                         env=_env_minuterie(tmp_path), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)
    p.kill()
    p.wait()
    assert not (tmp_path / "curl.txt").exists() and not (tmp_path / "consigne.txt").exists()
    assert "dépense épuisée à" in (r / "t08-minuterie.log").read_text()


def test_minuterie_artefact_heure_passee_consignation_puis_destruction(tmp_path):
    r = _minuterie(tmp_path)
    now = int(time.time())
    p = subprocess.run(["bash", str(r / "t08-minuterie.sh"), str(now + 3), str(now - 5), str(r), "https://api.invalid/v0"],
                       env=_env_minuterie(tmp_path), capture_output=True, text=True, timeout=120)
    j = (r / "t08-minuterie.log").read_text()
    assert p.returncode == 0 and "instance 424242 détruite" in j, j
    assert "plafond de 120 USD cumulé de T0.8" in j
    consigne = (tmp_path / "consigne.txt").read_text().split("\n")
    appels = [l.split() for l in (tmp_path / "curl.txt").read_text().split("\n") if l]
    assert [a[0] for a in appels] == ["PUT", "DELETE"]
    t_consigne = int(consigne[0].split()[-1])
    assert "dépense épuisée" in consigne[0] and t_consigne < int(appels[0][1]) < int(appels[1][1])     # consignation, arrêt, destruction
