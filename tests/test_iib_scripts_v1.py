"""(ii-b), chaîne de session v1 (`iib/session_v1.py`, `scripts/lancer_iib_v1.sh`) éprouvée **à blanc** : registre de GO et registre des
décisions **factices**, faux `vastai` et faux `df` des essais de T0.6, aucun réseau, aucune instance. Garde de GO (sain, ligne absente,
échue, révoquée, plafond hors ligne) ; variante de plafond (A ou B, aucune choisie ; repli H200 en A seulement) ; étiquette (instance
`t06-…` présente : création permise ; instance `iib-…` présente : refus) ; « 7b non créée → refus » (contrôles et création) ; marqueur
restant en mode réel → refus ; commande de création imprimée sans variable du mandataire, garde de calcul rejouée ; surveillance."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from datetime import timedelta
from pathlib import Path

import pytest

from controle_ia.iib import jouet_v1 as jv
from controle_ia.iib import session_v1 as sv
from controle_ia.scellement import sceller
from controle_ia.t06.session import GardeSession
from test_t06_v12_amorce import CONFIG_E2, DF_FACTICE, ENV_DE_BASE, _dates_epreuve
from test_t06_v12_scripts import OFFRES, VAST_REEL

RACINE = Path(__file__).resolve().parents[1]
LANCEUR = RACINE / "scripts" / "lancer_iib_v1.sh"
SAIN, A80, ECHU, REVOQUE, DECISION, ABSENT = ("GO-2099-01-01-01", "GO-2099-01-01-02", "GO-2099-01-01-03", "GO-2099-01-01-04",
                                              "GO-2099-01-01-05", "GO-2099-01-01-09")
ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
LIGNE_7B = "R-9999 factice : 7b créée, instance 99999999 à 2099-01-01T00:00:00Z"


def lignes_go():
    auj, ech, _ = _dates_epreuve()
    return ENTETE + (f"| {SAIN} | {auj} | calcul | (ii-b) course exploratoire, variante B | 60 USD | {ech} | Lazar | mot |\n"
                     f"| {A80} | {auj} | calcul | (ii-b) course exploratoire, variante A | 80 USD | {ech} | Lazar | mot |\n"
                     f"| {ECHU} | {auj - timedelta(days=10)} | calcul | ancienne | 60 USD | {auj - timedelta(days=1)} | Lazar | mot |\n"
                     f"| {REVOQUE} | {auj} | calcul | révoquée | 60 USD | {ech} | Lazar | mot |\n"
                     f"| GO-2099-01-01-06 | {auj} | révocation | révoque {REVOQUE} | — | {ech} | Lazar | mot |\n"
                     f"| {DECISION} | {auj} | décision | un nœud | — | {ech} | Lazar | mot |\n")


def config_session(tmp_path: Path, go=SAIN, variante="B", ligne_7b=LIGNE_7B, mode="jouet") -> dict:
    c = jv.preparer_monde(tmp_path, dossier="donnees/iib-jouet")
    e2 = json.loads(CONFIG_E2.read_text(encoding="utf-8"))
    _, ech, fin = _dates_epreuve()
    v = {"A": {"ligne_usd": 80, "configuration_usd": 75, "repli_h200": True}, "B": {"ligne_usd": 60, "configuration_usd": 55, "repli_h200": False}}[variante]
    c.update(go_id=go, plafond={"variante": variante, **v}, plafond_usd=v["configuration_usd"], carte=e2["carte"],
             offre={**e2["offre"], "etiquette": "iib-explo-v1", "disque_min_go": 100},
             calendrier={"dernier_jour_creation": str(ech - timedelta(days=1)), "fin_go_utc": fin.strftime("%Y-%m-%dT%H:%M:%SZ")},
             prealables={"ligne_registre_creation_7b": ligne_7b}, mode=mode)
    return c


# --- module de session ------------------------------------------------------------------------------------------------------
def _reg(tmp_path):
    f = tmp_path / "go.md"
    f.write_text(lignes_go(), encoding="utf-8")
    return f


def test_go_sain_et_plafond_sous_la_ligne(tmp_path):
    r = sv.verifier_go_iib(_reg(tmp_path), SAIN, 55, 0)
    assert r["plafond_usd"] == 60.0 and "≤ 60" in r["plafond_verifie"]
    assert sv.verifier_go_iib(_reg(tmp_path), SAIN, 55, 5)


@pytest.mark.parametrize("go, plafond, ant, motif", [(ABSENT, 55, 0, "absent du registre"), (ECHU, 55, 0, "hors de sa période"),
                                                     (REVOQUE, 55, 0, "révoqué"), (DECISION, 55, 0, "type"), (SAIN, 61, 0, "> 60"),
                                                     (SAIN, 55, 6, "> 60"), ("GO-X", 55, 0, "illisible")])
def test_go_artefacts(tmp_path, go, plafond, ant, motif):
    with pytest.raises(GardeSession, match=motif):
        sv.verifier_go_iib(_reg(tmp_path), go, plafond, ant)


def test_variantes_a_et_b_aucune_choisie(tmp_path):
    assert sv.verifier_variante(config_session(tmp_path, variante="B"), 60) == "B"
    assert sv.verifier_variante(config_session(tmp_path, variante="A"), 80) == "A"
    with pytest.raises(GardeSession, match="exige 60"):
        sv.verifier_variante(config_session(tmp_path, variante="B"), 80)
    with pytest.raises(GardeSession, match="exige 80"):
        sv.verifier_variante(config_session(tmp_path, variante="A"), 60)
    c = config_session(tmp_path)
    c["plafond"]["variante"] = None
    with pytest.raises(GardeSession, match="M7"):
        sv.verifier_variante(c, 60)


def test_carte_relance_seulement_en_variante_a(tmp_path):
    assert sv.verifier_carte(config_session(tmp_path, variante="A"), "relance") == "A"
    assert sv.verifier_carte(config_session(tmp_path, variante="B"), "course") == "B"
    with pytest.raises(GardeSession, match="aucun repli H200"):
        sv.verifier_carte(config_session(tmp_path, variante="B"), "relance")


@pytest.mark.parametrize("inventaire", [[], None, {"instances": None}, [{"id": 1, "label": "t06-v2"}, {"id": 58936096, "label": "a1-v4"}],
                                        [{"id": 2, "label": None}]])
def test_etiquette_sain_seule_une_instance_iib_bloque(inventaire):
    assert sv.verifier_instances_iib(inventaire)["instances_du_programme"] == 0


@pytest.mark.parametrize("inventaire", [[{"id": 3, "label": "iib-explo-v1"}], [{"id": 1, "label": "t06-v2"}, {"id": 4, "label": "iib-autre"}]])
def test_etiquette_artefact_instance_iib_presente_refus(inventaire):
    with pytest.raises(GardeSession, match="aucune création"):
        sv.verifier_instances_iib(inventaire)


def test_7b_creee_sain_et_artefacts(tmp_path):
    reg = tmp_path / "decisions.md"
    reg.write_text(f"| R-0001 | autre |\n| {LIGNE_7B} |\n", encoding="utf-8")
    assert sv.verifier_creation_7b(reg, config_session(tmp_path)) == LIGNE_7B
    with pytest.raises(GardeSession, match="7b non créée"):
        sv.verifier_creation_7b(reg, config_session(tmp_path, ligne_7b="<<LIGNE_REGISTRE_CREATION_7B>>"))
    with pytest.raises(GardeSession, match="7b non créée"):
        sv.verifier_creation_7b(reg, config_session(tmp_path, ligne_7b=""))
    reg.write_text("| R-0001 | autre |\n", encoding="utf-8")
    with pytest.raises(GardeSession, match="7b non créée"):
        sv.verifier_creation_7b(reg, config_session(tmp_path))
    reg.write_text(f"| {LIGNE_7B} |\n| {LIGNE_7B} (copie) |\n", encoding="utf-8")
    with pytest.raises(GardeSession, match="2 fois"):
        sv.verifier_creation_7b(reg, config_session(tmp_path))
    with pytest.raises(GardeSession, match="absent"):
        sv.verifier_creation_7b(tmp_path / "absent.md", config_session(tmp_path))


def test_config_reelle_marqueur_restant_refusee():
    c = jv.config_reelle_factice()
    assert sv.verifier_config(c)["mode"] == "reel"
    c["marqueurs"]["GO_ID_IIB"] = "<<GO_ID_IIB>>"
    with pytest.raises(GardeSession, match="non rempli"):
        sv.verifier_config(c)


# --- script de lancement ----------------------------------------------------------------------------------------------------
def _git(d, *a):
    return subprocess.run(["git", "-C", str(d), *a], capture_output=True, text=True, check=True).stdout.strip()


@pytest.fixture
def monde(tmp_path):
    """Dépôt source factice (session, configuration et tâches jouet scellées, registres factices, garde de calcul), origine locale,
    branche `prep/iib-essai` poussée et relevée par refspec ; faux outils."""
    src = tmp_path / "source"
    src.mkdir()
    _git(tmp_path, "init", "-q", "-b", "main", str(src))
    _git(src, "config", "user.email", "t@example.invalid")
    _git(src, "config", "user.name", "t")
    for rel in ("src/controle_ia/__init__.py", "src/controle_ia/gardes.py", "src/controle_ia/scellement.py",
                "src/controle_ia/iib/__init__.py", "src/controle_ia/iib/configuration_v1.py", "src/controle_ia/iib/session_v1.py",
                ".claude/hooks/garde_calcul.py", "scripts/amorce_instance_iib_v1.sh"):
        (src / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(RACINE / rel, src / rel)
    (src / "src" / "controle_ia" / "t06").mkdir()
    (src / "src" / "controle_ia" / "t06" / "__init__.py").write_text("", encoding="utf-8")
    for f in sorted((RACINE / "src" / "controle_ia" / "t06").glob("session*.py")):
        shutil.copy(f, src / "src" / "controle_ia" / "t06" / f.name)
    (src / "registres").mkdir()
    (src / "registres" / "go.md").write_text(lignes_go(), encoding="utf-8")
    (src / "registres" / "decisions.md").write_text(f"| R-0001 | registre factice |\n| {LIGNE_7B} |\n", encoding="utf-8")
    for nom, c in (("config-iib-jouet.json", config_session(src)), ("config-iib-a.json", config_session(src, go=A80, variante="A")),
                   ("config-iib-sans-7b.json", config_session(src, ligne_7b="R-8888 factice : 7b jamais créée"))):
        f = src / "prereg" / nom
        f.parent.mkdir(exist_ok=True)
        f.write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        sceller(f)
    _git(src, "add", "-A")
    _git(src, "commit", "-qm", "monde factice")
    origin = tmp_path / "origin.git"
    subprocess.run(["git", "clone", "-q", "--bare", str(src), str(origin)], check=True)
    _git(src, "remote", "add", "origin", str(origin))
    _git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/iib-essai")
    _git(src, "fetch", "-q", "origin", "refs/heads/prep/iib-essai:refs/remotes/origin/prep/iib-essai")
    b = tmp_path / "bin"
    b.mkdir()
    for nom, texte in (("vastai", VAST_REEL), ("df", DF_FACTICE)):
        (b / nom).write_text(texte, encoding="utf-8")
        (b / nom).chmod(0o755)
    (tmp_path / "offres.json").write_text(json.dumps(OFFRES), encoding="utf-8")
    (tmp_path / "journal.txt").write_text("AMORCE 2026-11-14T10:00:00Z : commit abc\n", encoding="utf-8")
    return {"src": src, "tmp": tmp_path, "commit": _git(src, "rev-parse", "HEAD"), "bin": b}


def _env(m, **sup):
    e = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    t = m["tmp"]
    e.update(PATH=f"{m['bin']}:{e.get('PATH', '')}", IIB_DEPOT=str(m["src"]), CONTROLE_IA_GITHUB_TOKEN_2="jeton-gh-factice", HOME=str(t),
             IIB_REGISTRE_GO=str(m["src"] / "registres" / "go.md"), IIB_BRANCHE_CODE="prep/iib-essai", IIB_BRANCHE="essai/iib-explo-v1",
             IIB_DEPENSE_ANTERIEURE_USD="0", IIB_TESTS_ATTENDUS="", GO_ID=SAIN, FAUX_OFFRES=str(t / "offres.json"),
             FAUX_VASTAI_JOURNAL=str(t / "appels.txt"), FAUX_COMPTEUR=str(t / "compteur.txt"), FAUX_CREES=str(t / "crees.txt"),
             FAUX_JOURNAL=str(t / "journal.txt"), INTERVALLE="1")
    e.update(sup)
    return {k: v for k, v in e.items() if v is not None}


def _lancer(m, *args, **sup):
    return subprocess.run(["bash", str(LANCEUR), *map(str, args)], env=_env(m, **sup), capture_output=True, text=True, timeout=180)


def _arbre(d: Path) -> set:
    return {str(p.relative_to(d)) for p in d.rglob("*")}


def test_verifier_go_seulement_sain_ne_cree_rien(monde):
    avant = _arbre(monde["tmp"])
    r = _lancer(monde, "--verifier-go-seulement", "55")
    assert r.returncode == 0 and r.stdout.startswith("GO VÉRIFIÉ, RIEN CRÉÉ : ") and f"{SAIN} conforme (plafond 60 USD" in r.stdout, r.stdout + r.stderr
    assert _arbre(monde["tmp"]) == avant


@pytest.mark.parametrize("cas, args, sup, motif", [
    ("ligne_absente", ("55",), {"GO_ID": ABSENT}, "absent du registre"), ("echue", ("55",), {"GO_ID": ECHU}, "hors de sa période"),
    ("revoquee", ("55",), {"GO_ID": REVOQUE}, "révoqué"), ("decision", ("55",), {"GO_ID": DECISION}, "type"),
    ("plafond_hors_ligne", ("61",), {}, "> 60"), ("go_absent", ("55",), {"GO_ID": None}, "GO_ID absent"),
    ("registre_absent", ("55",), {"IIB_REGISTRE_GO": None}, "IIB_REGISTRE_GO"), ("plafond_illisible", ("x",), {}, "nombre positif")])
def test_verifier_go_seulement_artefacts(monde, cas, args, sup, motif):
    avant = _arbre(monde["tmp"])
    r = _lancer(monde, "--verifier-go-seulement", *args, **sup)
    assert r.returncode == 2 and motif in r.stdout and "GO VÉRIFIÉ" not in r.stdout, (cas, r.stdout + r.stderr)
    assert _arbre(monde["tmp"]) == avant


def _controles(m, nom="ok", config="prereg/config-iib-jouet.json", **sup):
    d = m["tmp"] / nom
    return d, _lancer(m, "controles-explo", d, m["commit"], config, **sup)


def test_controles_explo_sain(monde):
    d, r = _controles(monde)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CONTRÔLES CONFORMES" in r.stdout and "variante B conforme" in r.stdout and f"7b créée : {LIGNE_7B}" in r.stdout
    lanc = (d / "lancement.txt").read_text(encoding="utf-8")
    amorce = subprocess.run(["sha256sum", str(RACINE / "scripts" / "amorce_instance_iib_v1.sh")], capture_output=True, text=True).stdout.split()[0]
    assert f"amorce {amorce}" in lanc and f"go {SAIN}" in lanc and "mode jouet" in lanc


@pytest.mark.parametrize("cas", ["7b_absente", "registre_decisions_absent", "go_absent_du_registre", "go_echu", "go_revoque", "go_autre_que_config",
                                 "branche_poussee_interdite", "variante_sans_sa_ligne", "plafond_hors_ligne"])
def test_controles_explo_artefacts(monde, cas):
    sup, config, motif = {}, "prereg/config-iib-jouet.json", None
    if cas == "7b_absente":
        config, motif = "prereg/config-iib-sans-7b.json", "identifiant d'instance"
    elif cas == "registre_decisions_absent":
        sup["IIB_REGISTRE_DECISIONS"], motif = str(monde["tmp"] / "absent.md"), "7b n'est pas établie"
    elif cas in ("go_absent_du_registre", "go_echu", "go_revoque"):
        reg = monde["tmp"] / "go-main.md"
        reg.write_text(lignes_go().replace(f"| {SAIN} |", {"go_absent_du_registre": "| GO-2099-01-01-08 |", "go_echu": f"| {SAIN} |",
                                                         "go_revoque": f"| {SAIN} |"}[cas], 1), encoding="utf-8")
        if cas == "go_echu":
            auj, ech, _ = _dates_epreuve()
            reg.write_text(lignes_go().replace(f"| {SAIN} | {auj} | calcul | (ii-b) course exploratoire, variante B | 60 USD | {ech} |",
                                               f"| {SAIN} | {auj - timedelta(days=9)} | calcul | (ii-b) course exploratoire, variante B | 60 USD | {auj - timedelta(days=1)} |"),
                           encoding="utf-8")
        if cas == "go_revoque":
            auj, ech, _ = _dates_epreuve()
            reg.write_text(lignes_go() + f"| GO-2099-01-01-07 | {auj} | révocation | révoque {SAIN} | — | {ech} | Lazar | mot |\n", encoding="utf-8")
        (monde["tmp"] / "decisions.md").write_text(f"| {LIGNE_7B} |\n", encoding="utf-8")
        sup["IIB_REGISTRE_GO"] = str(reg)
        motif = {"go_absent_du_registre": "absent du registre", "go_echu": "hors de sa période", "go_revoque": "révoqué"}[cas]
    elif cas == "go_autre_que_config":
        sup["GO_ID"], motif = A80, "≠ GO_ID de l'environnement"
    elif cas == "branche_poussee_interdite":
        sup["IIB_BRANCHE"], motif = "calcul/iib-v1", "essai/iib-explo-v<n>"
    elif cas == "variante_sans_sa_ligne":
        reg = monde["tmp"] / "go-main.md"
        reg.write_text(lignes_go().replace("variante B | 60 USD", "variante B | 80 USD"), encoding="utf-8")
        (monde["tmp"] / "decisions.md").write_text(f"| {LIGNE_7B} |\n", encoding="utf-8")
        sup["IIB_REGISTRE_GO"], motif = str(reg), "exige 60"
    elif cas == "plafond_hors_ligne":
        sup["IIB_DEPENSE_ANTERIEURE_USD"], motif = "6", "> 60"
    d, r = _controles(monde, "x", config, **sup)
    assert r.returncode == 2 and motif in r.stdout + r.stderr, (cas, r.stdout + r.stderr)
    assert "CONTRÔLES CONFORMES" not in r.stdout


def _instances(m, liste):
    f = m["tmp"] / "instances.json"
    f.write_text(json.dumps(liste), encoding="utf-8")
    return str(f)


@pytest.mark.parametrize("inventaire", [[], [{"id": 61000001, "label": "t06-7b", "actual_status": "running"},
                                             {"id": 58936096, "label": "a1-v4", "actual_status": "exited"}]], ids=["vide", "instance_t06_presente"])
def test_creation_sain_commande_imprimee(monde, inventaire):
    d, r = _controles(monde)
    assert r.returncode == 0, r.stdout + r.stderr
    r = _lancer(monde, "creation", "auto", "course", "0", d, FAUX_INSTANCES=_instances(monde, inventaire), FAUX_RETIRE="0")
    assert r.returncode == 0, r.stdout + r.stderr
    cmd = r.stdout.splitlines()[-1]
    assert cmd.startswith(f"GO_ID={SAIN} timeout -k 10 300 ") and "--label iib-explo-v1" in cmd and "-e BRANCHE=essai/iib-explo-v1" in cmd
    assert "-e MODE=jouet" in cmd and "-e PREREG_ABSENT=1" in cmd and "-e CONFIG=prereg/config-iib-jouet.json" in cmd and f"-e IIB_GO_ID={SAIN}" in cmd
    for v in ("REQUESTS_CA_BUNDLE", "SSL_CERT_FILE", "HTTPS_PROXY", "NO_PROXY", "jeton-gh-factice"):
        assert v not in cmd
    appels = (monde["tmp"] / "appels.txt").read_text(encoding="utf-8")
    assert "create instance" not in appels and "destroy" not in appels and "stop" not in appels      # rien n'est créé ni touché


def test_creation_artefact_instance_iib_presente_refus(monde):
    d, r = _controles(monde)
    assert r.returncode == 0, r.stdout
    r = _lancer(monde, "creation", "auto", "course", "0", d, FAUX_INSTANCES=_instances(monde, [{"id": 61000002, "label": "iib-explo-v1"}]))
    assert r.returncode == 3 and "aucune création" in r.stdout and "COMMANDE DE CRÉATION" not in r.stdout, r.stdout + r.stderr


def test_creation_artefact_7b_retiree_du_registre_entre_controles_et_creation(monde):
    d, r = _controles(monde)
    assert r.returncode == 0, r.stdout
    reg = monde["tmp"] / "decisions-sans-7b.md"
    reg.write_text("| R-0001 | registre factice |\n", encoding="utf-8")
    r = _lancer(monde, "creation", "auto", "course", "0", d, IIB_REGISTRE_DECISIONS=str(reg))
    assert r.returncode == 2 and "7b non créée" in r.stdout and "COMMANDE DE CRÉATION" not in r.stdout, r.stdout + r.stderr


def test_creation_artefact_relance_h200_en_variante_b_noeud(monde):
    d, r = _controles(monde)
    assert r.returncode == 0, r.stdout
    r = _lancer(monde, "creation", "auto", "relance", "0", d)
    assert r.returncode == 3 and "aucun repli H200" in r.stdout and "COMMANDE DE CRÉATION" not in r.stdout, r.stdout + r.stderr


def test_creation_relance_permise_en_variante_a(monde):
    d, r = _controles(monde, "a", "prereg/config-iib-a.json", GO_ID=A80)
    assert r.returncode == 0, r.stdout + r.stderr
    r = _lancer(monde, "creation", "auto", "relance", "0", d, GO_ID=A80, FAUX_INSTANCES=_instances(monde, []))
    assert "aucun repli H200" not in r.stdout and r.returncode in (0, 3), r.stdout + r.stderr


def test_surveillance_fin_et_arret_par_identifiant(monde):
    d = monde["tmp"] / "s"
    d.mkdir()
    import time
    cr = int(time.time()) - 60
    (d / "lancement.txt").write_text(f"instance 123456\ncreation {cr}\nprix_carte 1.0\nprix_stockage 0.03\ntelechargement_forfait 1.0\n"
                                     f"anterieure 0\nplafond_creation 55\nmode jouet\n", encoding="utf-8")
    (monde["tmp"] / "journal.txt").write_text("AMORCE 2026-11-14T10:00:00Z : fin, code 0\n", encoding="utf-8")
    r = _lancer(monde, "surveillance", "123456", d)
    assert r.returncode == 0 and "FIN" in r.stdout and "stop instance 123456" in r.stdout, r.stdout + r.stderr
    r = _lancer(monde, "surveillance", "999", d)
    assert r.returncode == 2 and "R10" in r.stdout
