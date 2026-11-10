"""Chaîne v14 de T0.6, scripts (préparés, non adoptés : option (c) de Lazar, R-2079) : lanceur `scripts/lancer_t06_v14.sh` et amorce `scripts/amorce_instance_t06_v12.sh`.
En mode course, la ligne de GO vient de la configuration de S (`go_id`), doit égaler `GO_ID` de l'environnement, est lue et vérifiée au registre (présente, type
« calcul », accordée par Lazar, non échue, non révoquée), le plafond de la configuration ne dépasse pas celui de la ligne, le calendrier est vérifié contre elle, et la
ligne doit figurer aussi dans `registres/go.md` du commit S (l'amorce l'y relit) ; l'amorce reçoit la ligne (`COURSE_GO_ID`), la relit au registre du commit cloné et tire
la fin du GO de la configuration. Une épreuve reste refusée sous la ligne de la course, lue dans la configuration citée par le texte (jamais en dur).
Cas sain et artefact (R5) pour chaque garde neuve ; dépôt distant local, `python`, `vastai` et `df` factices ; aucun réseau, aucun appel à Vast ; dates relatives au jour de
l'essai. Les fixtures et les faux outils des essais v12 et v13 sont réutilisés."""
from __future__ import annotations

import difflib
import hashlib
import json
import os
import shutil
import subprocess
from datetime import timedelta
from pathlib import Path

import pytest

from controle_ia.scellement import sceller
import test_t06_v12_amorce as t
from test_t06_v12_amorce import CONFIG_E2, ENV_DE_BASE, RACINE, _commit_source, _config_epreuve, _dates_epreuve, _distant, _git, _outils
from test_t06_v12_scripts import DF_FACTICE, OFFRES, VAST_REEL

LANCEUR14 = RACINE / "scripts" / "lancer_t06_v14.sh"
LANCEUR13 = RACINE / "scripts" / "lancer_t06_v13.sh"
AMORCE12 = RACINE / "scripts" / "amorce_instance_t06_v12.sh"
AMORCE11 = RACINE / "scripts" / "amorce_instance_t06_v11.sh"
LISTE4 = RACINE / "scripts" / "tests-cibles-t06-v4.txt"
ANCIEN = "GO-" + "2026-11-02-28"           # en deux morceaux (voir tests/test_t06_v14_gardes.py)
COURSE = "GO-2099-03-03-01"
PETITE = "GO-2099-03-03-02"
ECHUE = "GO-2099-03-03-04"
ENTETE = t.GO.split("\n")[0] + "\n" + t.GO.split("\n")[1] + "\n"
PYTHON_FACTICE_V14 = (t.PYTHON_FACTICE.replace('[ "$2" = "controle_ia.t06.lanceur_v5" ]', '[ "$2" = "controle_ia.t06.lanceur_v7" ]')
                      .replace('    run=""; prec=""\n', '    printf \'%s\\n\' "$*" > "${RACINE_AMORCE:-/tmp}/lanceur-args.txt"\n    run=""; prec=""\n'))
assert PYTHON_FACTICE_V14.count("lanceur_v7") == 1 and "lanceur-args.txt" in PYTHON_FACTICE_V14


def _lignes(course_plafond="200 USD (plafond de la ligne d'origine, non cumulé)", course=True, course_passee=False, revocation=False):
    auj, ech, _ = _dates_epreuve()
    s = ""
    if course:
        a, e = (auj - timedelta(days=10), auj - timedelta(days=1)) if course_passee else (auj, ech)
        s += f"| {COURSE} | {a} | calcul | course de confirmation (essai) | {course_plafond} | {e} | Lazar | essai |\n"
    s += f"| {PETITE} | {auj} | calcul | épreuve à blanc (essai) | 16 USD | {ech} | Lazar | essai |\n"
    s += f"| {ECHUE} | {auj - timedelta(days=10)} | calcul | ligne ancienne | 200 USD | {auj - timedelta(days=1)} | Lazar | essai |\n"
    if revocation:
        s += f"| GO-2099-03-03-06 | {auj} | révocation | révoque {COURSE} | — | {ech} | Lazar | essai |\n"
    return s


def _registre_texte(**k) -> str:
    return t.GO + _lignes(**k)                                       # l'ancienne ligne (en tête du registre des essais v12) reste présente : rien ne la sert plus en dur


def _config_course(**modifs) -> dict:
    return _config_epreuve(CONFIG_E2, go_id=COURSE, plafond_usd=200, mode="reel", **modifs)        # carte des offres factices ; calendrier relatif


def _prereg_v12(sha: str) -> str:
    return t._prereg(sha).replace("scripts/amorce_instance_t06_v10.sh", "scripts/amorce_instance_t06_v12.sh")


def _ecrire_json(f: Path, c: dict):
    f.write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def fabriquer_bac14(tmp_path, registre: str | None = None, config: dict | None = None, epreuve: dict | None = None):
    """Bac des essais v12 avec l'amorce v12, la liste v4 (fichiers d'essais vides), le faux `python` qui connaît `lanceur_v7` et journalise ses arguments, la
    configuration de course (chemin cité par le texte : go_id de la ligne de course, calendrier relatif), le registre de l'essai et un texte qui cite l'amorce v12.
    Le sceau du texte est retiré dans un commit à part, puis remis : le commit qui l'AJOUTE est le commit de scellement S (`commit_s`)."""
    b = t.fabriquer_bac(tmp_path)
    src = b["source"]
    shutil.copy(AMORCE12, src / "scripts" / AMORCE12.name)
    shutil.copy(LISTE4, src / "scripts" / LISTE4.name)
    for x in LISTE4.read_text(encoding="utf-8").split():
        (src / x).parent.mkdir(parents=True, exist_ok=True)
        if not (src / x).exists():
            (src / x).write_text("", encoding="utf-8")
    (b["venv"] / "bin" / "python").write_text(PYTHON_FACTICE_V14, encoding="utf-8")
    (src / (t.CONFIG + ".sha256")).unlink()
    _ecrire_json(src / t.CONFIG, config or _config_course())
    sceller(src / t.CONFIG)
    if epreuve is not None:
        _ecrire_json(src / "prereg" / "config-epreuve.json", epreuve)
        sceller(src / "prereg" / "config-epreuve.json")
    (src / "registres" / "go.md").write_text(_registre_texte() if registre is None else registre, encoding="utf-8")
    _git(src, "rm", "-q", t.PREREG + ".sha256")
    _commit_source(b, "chaîne v14 : sceau du texte retiré")
    sha = hashlib.sha256(AMORCE12.read_bytes()).hexdigest()
    (src / t.PREREG).write_text(_prereg_v12(sha), encoding="utf-8")
    sceller(src / t.PREREG)
    _commit_source(b, "chaîne v14 : texte qui cite l'amorce v12 (S)")
    b["amorce_sha"] = sha
    return b


def _arbre(d: Path) -> set:
    return {str(p.relative_to(d)) for p in d.rglob("*")}


# =========================================================================================================================================================
# 1. Lanceur v14, `controles` (course)
# =========================================================================================================================================================
def _session14(b, tmp_path):
    """Dépôt de session : origine locale, garde de calcul, lanceur v14 ; `main` poussée (S ancêtre d'origin/main) ; branche prep/ pour les épreuves."""
    src = b["source"]
    origin = _distant(b)
    _git(src, "remote", "add", "origin", str(origin))
    (src / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(RACINE / ".claude" / "hooks" / "garde_calcul.py", src / ".claude" / "hooks" / "garde_calcul.py")
    shutil.copy(LANCEUR14, src / "scripts" / LANCEUR14.name)
    _commit_source(b, "session : garde et lanceur v14")
    _git(src, "push", "-q", "origin", "main")
    _git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/essai-t06")
    _git(src, "fetch", "-q", "origin", "refs/heads/prep/essai-t06:refs/remotes/origin/prep/essai-t06")
    b["tmp"] = tmp_path
    for nom, texte in (("vastai", VAST_REEL), ("df", DF_FACTICE)):
        (tmp_path / "bin").mkdir(exist_ok=True)
        (tmp_path / "bin" / nom).write_text(texte, encoding="utf-8")
        (tmp_path / "bin" / nom).chmod(0o755)
    (tmp_path / "offres.json").write_text(json.dumps(OFFRES), encoding="utf-8")
    return src


@pytest.fixture
def s14(tmp_path):
    b = fabriquer_bac14(tmp_path)
    _session14(b, tmp_path)
    return b


def _env14(b, **sup):
    e = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    tmp = b["tmp"]
    e.update(PATH=f"{tmp / 'bin'}:{e.get('PATH', '')}", T06_DEPOT=str(b["source"]), HF_TOKEN="jeton-hf-factice", CONTROLE_IA_GITHUB_TOKEN="jeton-gh-factice",
             HOME=str(tmp), GO_ID=COURSE, FAUX_OFFRES=str(tmp / "offres.json"), FAUX_VASTAI_JOURNAL=str(tmp / "appels.txt"), FAUX_COMPTEUR=str(tmp / "compteur.txt"),
             FAUX_CREES=str(tmp / "crees.txt"), FAUX_JOURNAL=str(tmp / "journal.txt"), T06_BRANCHE="calcul/t06-reel-v14-essai")
    e.update(sup)
    return {k: v for k, v in e.items() if v is not None}


def _v14(b, *args, **sup):
    return subprocess.run(["bash", str(LANCEUR14), *map(str, args)], env=_env14(b, **sup), capture_output=True, text=True, timeout=180)


def _registre_externe(b, nom, texte) -> str:
    f = b["tmp"] / nom
    f.write_text(texte, encoding="utf-8")
    return str(f)


def test_controles_course_cas_sain_ligne_de_la_configuration_lue_au_registre(s14):
    auj, ech, fin = _dates_epreuve()
    d = s14["tmp"] / "c-ok"
    r = _v14(s14, "controles", d, auj)
    assert r.returncode == 0, r.stdout + r.stderr
    assert r.stdout.strip().splitlines()[-1].startswith("CONTRÔLES CONFORMES : S=") and f"amorce v12 {s14['amorce_sha']}" in r.stdout
    assert f"GO {COURSE} (plafond de la configuration 200 USD ≤ plafond de la ligne du registre) ; fin_go_utc_s={int(fin.timestamp())}" in r.stdout
    lanc = (d / "lancement.txt").read_text(encoding="utf-8")
    assert f"{COURSE} conforme (plafond de la ligne 200 USD, {auj} → {ech}) ; plafond de la configuration 200 ≤ 200" in lanc
    assert f"\ngo {COURSE}\n" in lanc and "\nplafond 200\n" in lanc and f"\namorce {s14['amorce_sha']}\n" in lanc and lanc.startswith(f"{COURSE} conforme")
    assert ANCIEN not in lanc and ANCIEN not in r.stdout
    # dernier jour de création (veille de l'échéance) : conforme ; le jour de l'échéance : refus par le calendrier (la ligne vaut encore)
    assert _v14(s14, "controles", s14["tmp"] / "c-dernier", ech - timedelta(days=1)).returncode == 0


@pytest.mark.parametrize("cas", ["go_id_absent", "go_id_vide", "go_id_illisible", "go_id_autre_que_la_configuration", "ancienne_valeur", "ligne_absente_du_registre",
                                 "ligne_echue", "ligne_revoquee", "plafond_configuration_superieur_a_la_ligne", "calendrier_au_dela_du_dernier_jour",
                                 "ligne_absente_du_registre_du_commit_S"])
def test_controles_course_artefacts_code_2_aucun_controle_conforme(tmp_path, cas):
    auj, ech, _ = _dates_epreuve()
    b = fabriquer_bac14(tmp_path, registre=t.GO + _lignes(course=False)) if cas == "ligne_absente_du_registre_du_commit_S" else fabriquer_bac14(tmp_path)
    _session14(b, tmp_path)
    jour, sup = auj, {}
    motif = {"go_id_absent": "GO_ID absent ou illisible", "go_id_vide": "GO_ID absent ou illisible", "go_id_illisible": "GO_ID absent ou illisible",
             "go_id_autre_que_la_configuration": f"go_id de la configuration de S ({COURSE}) ≠ GO_ID de l'environnement ({PETITE})",
             "ancienne_valeur": f"≠ GO_ID de l'environnement ({ANCIEN})", "ligne_absente_du_registre": f"{COURSE} absent du registre",
             "ligne_echue": "hors de sa période de validité", "ligne_revoquee": "révoqué par GO-2099-03-03-06",
             "plafond_configuration_superieur_a_la_ligne": "plafond de la configuration 200.0 > plafond 150.0 de la ligne",
             "calendrier_au_dela_du_dernier_jour": "dépassé", "ligne_absente_du_registre_du_commit_S": "commit postérieur au GO exigé"}[cas]
    if cas == "go_id_absent":
        sup["GO_ID"] = None
    elif cas == "go_id_vide":
        sup["GO_ID"] = ""
    elif cas == "go_id_illisible":
        sup["GO_ID"] = "GO-X"
    elif cas == "go_id_autre_que_la_configuration":
        sup["GO_ID"] = PETITE
    elif cas == "ancienne_valeur":
        sup["GO_ID"] = ANCIEN
    elif cas == "ligne_absente_du_registre":
        sup["T06_REGISTRE_GO"] = _registre_externe(b, "go-sans.md", t.GO + _lignes(course=False))
    elif cas == "ligne_echue":
        jour = ech + timedelta(days=1)
    elif cas == "ligne_revoquee":
        sup["T06_REGISTRE_GO"] = _registre_externe(b, "go-rev.md", _registre_texte(revocation=True))
    elif cas == "plafond_configuration_superieur_a_la_ligne":
        sup["T06_REGISTRE_GO"] = _registre_externe(b, "go-150.md", _registre_texte(course_plafond="150 USD"))
    elif cas == "calendrier_au_dela_du_dernier_jour":
        jour = ech
    elif cas == "ligne_absente_du_registre_du_commit_S":
        sup["T06_REGISTRE_GO"] = _registre_externe(b, "go-main.md", _registre_texte())          # le registre de « main » porte la ligne, celui de S non
    d = tmp_path / "c"
    r = _v14(b, "controles", d, jour, **sup)
    assert r.returncode == 2 and motif in r.stdout + r.stderr, (cas, r.stdout + r.stderr)
    assert "CONTRÔLES CONFORMES" not in r.stdout
    assert not (d / "lancement.txt").exists() or "\ncommit " not in (d / "lancement.txt").read_text(encoding="utf-8")


# =========================================================================================================================================================
# 2. Lanceur v14, `creation` (course) : ligne relue au jour de la création, COURSE_GO_ID passé à l'amorce, garde de calcul rejouée
# =========================================================================================================================================================
def _controles_ok(b, nom="c"):
    d = b["tmp"] / nom
    r = _v14(b, "controles", d, _dates_epreuve()[0])
    assert r.returncode == 0, r.stdout + r.stderr
    return d


def test_creation_course_cas_sain_commande_sous_la_ligne_de_la_configuration(s14):
    d = _controles_ok(s14)
    r = _v14(s14, "creation", "auto", "course", "0", d)
    assert r.returncode == 0, r.stdout + r.stderr
    cmd = r.stdout.splitlines()[-1]
    assert cmd.startswith(f"GO_ID={COURSE} timeout -k 10 300 ") and f"-e COURSE_GO_ID={COURSE}\"" in cmd and "EPREUVE_GO_ID" not in cmd and "PREREG_ABSENT" not in cmd
    assert "lancer_t06_v14.sh apres-creation" in cmd and f"-e PREREG={t.PREREG} " in cmd and ANCIEN not in cmd
    lanc = (d / "lancement.txt").read_text(encoding="utf-8")
    assert "plafond_creation 200" in lanc and "creation preparee" in lanc and ANCIEN not in lanc


@pytest.mark.parametrize("cas", ["go_id_autre", "go_id_absent", "ligne_retiree_du_registre", "plafond_superieur_a_la_ligne", "ligne_revoquee", "ancienne_valeur"])
def test_creation_course_artefacts_aucune_commande_de_creation(s14, cas):
    d = _controles_ok(s14)
    sup = {"go_id_autre": {"GO_ID": PETITE}, "go_id_absent": {"GO_ID": None}, "ancienne_valeur": {"GO_ID": ANCIEN},
           "ligne_retiree_du_registre": {"T06_REGISTRE_GO": _registre_externe(s14, "go-sans.md", t.GO + _lignes(course=False))},
           "plafond_superieur_a_la_ligne": {"T06_REGISTRE_GO": _registre_externe(s14, "go-150.md", _registre_texte(course_plafond="150 USD"))},
           "ligne_revoquee": {"T06_REGISTRE_GO": _registre_externe(s14, "go-rev.md", _registre_texte(revocation=True))}}[cas]
    motif = {"go_id_autre": "≠ GO_ID de l'environnement", "go_id_absent": "≠ GO_ID de l'environnement (absent)", "ancienne_valeur": "≠ GO_ID de l'environnement",
             "ligne_retiree_du_registre": "absent du registre", "plafond_superieur_a_la_ligne": "> plafond 150.0", "ligne_revoquee": "révoqué"}[cas]
    r = _v14(s14, "creation", "auto", "course", "0", d, **sup)
    assert r.returncode == 2 and motif in r.stdout and "create instance" not in r.stdout and "COMMANDE DE CRÉATION" not in r.stdout, (cas, r.stdout + r.stderr)
    assert not (s14["tmp"] / "appels.txt").exists() or "create instance" not in (s14["tmp"] / "appels.txt").read_text(encoding="utf-8")


# =========================================================================================================================================================
# 3. Une épreuve reste refusée sous la ligne de la course, lue dans la configuration citée par le texte de S (jamais en dur)
# =========================================================================================================================================================
def test_verifier_go_seulement_refuse_la_ligne_de_la_course_lue_dans_s_et_rien_cree(s14):
    avant = _arbre(s14["tmp"])
    r = _v14(s14, "--verifier-go-seulement", "15", T06_REGISTRE_GO=str(s14["source"] / "registres" / "go.md"))
    assert r.returncode == 2 and f"GO_ID={COURSE} est le GO de la course" in r.stdout, r.stdout + r.stderr
    r = _v14(s14, "--verifier-go-seulement", "15", GO_ID=PETITE, T06_REGISTRE_GO=str(s14["source"] / "registres" / "go.md"))
    assert r.returncode == 0 and r.stdout.startswith("GO VÉRIFIÉ, RIEN CRÉÉ : ") and f"{PETITE} conforme (plafond 16 USD" in r.stdout, r.stdout + r.stderr
    # l'ancienne valeur n'est plus « la course » : sous sa ligne (valide le 10 novembre 2026 dans le registre des essais), une épreuve se vérifie comme une autre
    r = _v14(s14, "--verifier-go-seulement", "15", "0", "2026-11-10", GO_ID=ANCIEN, T06_REGISTRE_GO=str(s14["source"] / "registres" / "go.md"))
    assert r.returncode == 0 and "GO VÉRIFIÉ" in r.stdout, r.stdout + r.stderr
    assert _arbre(s14["tmp"]) == avant


def test_verifier_go_seulement_artefact_go_de_la_course_illisible(s14):
    r = _v14(s14, "--verifier-go-seulement", "15", GO_ID=PETITE, T06_REGISTRE_GO=str(s14["source"] / "registres" / "go.md"), T06_PREREG="prereg/absent.md")
    assert r.returncode == 2 and "GO de la course illisible" in r.stdout and "GO VÉRIFIÉ" not in r.stdout, r.stdout


def test_controles_epreuve_refuse_la_ligne_de_la_course(s14):
    src = s14["source"]
    head = _git(src, "rev-parse", "HEAD")
    d = s14["tmp"] / "e"
    r = _v14(s14, "controles-epreuve", d, head, t.CONFIG, T06_REGISTRE_GO=str(src / "registres" / "go.md"), T06_BRANCHE_CODE="prep/essai-t06",
             T06_BRANCHE="essai/t06-test", T06_DEPENSE_EPREUVES_ANTERIEURES_USD="0")
    assert r.returncode == 2 and f"go_id de la configuration ({COURSE}) est le GO de la course" in r.stdout and "CONFORMES" not in r.stdout, r.stdout + r.stderr


# =========================================================================================================================================================
# 4. Amorce v12 (essai local, aucun appel à Vast) : COURSE_GO_ID relu au registre du commit cloné ; fin du GO tirée de la configuration
# =========================================================================================================================================================
def _amorce(b, nom, env_sup=None):
    _, _, fin = _dates_epreuve()
    distant = _distant(b)
    racine = b["racine"] / nom
    racine.mkdir(exist_ok=True)
    env = {"COURSE_GO_ID": COURSE, "FIN_GO_UTC_S": str(int(fin.timestamp())), "ECHEANCE_UTC_S": str(int(fin.timestamp())), "HF_TOKEN": "jeton-hf-factice"}
    env.update(env_sup or {})
    r = subprocess.run(["bash", str(AMORCE12)], env=t._env(b, distant, racine, env), capture_output=True, text=True, timeout=300)
    j = racine / "t06" / "journal.txt"
    return r.returncode, (j.read_text(encoding="utf-8") if j.exists() else ""), r.stdout + r.stderr, racine, distant


@pytest.mark.parametrize("mode", ["jouet", "reel"])
def test_amorce_v12_course_cas_sain_ligne_relue_au_registre_du_commit(tmp_path, mode):
    b = fabriquer_bac14(tmp_path)
    code, journal, sortie, racine, distant = _amorce(b, "ok", {"MODE": mode})
    assert code == 0, sortie[-2500:]
    assert "AMORCE T06 v12 DEMARRAGE" in sortie and f"GO : {COURSE} conforme (plafond 200 USD" in journal and f"GO={COURSE}" in journal
    assert f"GO de la configuration : {COURSE} conforme (plafond de la ligne 200 USD" in journal and "plafond de la configuration 200 ≤ 200" in journal
    assert "calendrier : fin_go_utc_s=" in journal and "plafond_ligne=200" in journal and "lanceur v7" in journal and ANCIEN not in journal
    args = (racine / "lanceur-args.txt").read_text(encoding="utf-8")
    assert args.startswith("-m controle_ia.t06.lanceur_v7 --config prereg/T0.6-config-v2.json --run-id ") and f"--prereg {t.PREREG}" in args and "--epreuve" not in args
    assert "suite ciblée : 86 fichiers d'essais, liste scripts/tests-cibles-t06-v4.txt" in journal and (racine / "t06-fin-normale").exists()


@pytest.mark.parametrize("cas", ["course_go_absent", "course_go_illisible", "course_et_epreuve_posees", "course_go_autre_que_la_configuration", "ancienne_valeur",
                                 "ligne_absente_du_registre_du_commit", "ligne_echue", "ligne_revoquee", "plafond_superieur_a_la_ligne", "fin_du_go_recue_differente",
                                 "calendrier_au_dela_de_l_echeance"])
def test_amorce_v12_course_artefacts_refus_et_destruction_avant_tout_run(tmp_path, cas):
    auj, ech, fin = _dates_epreuve()
    registre = {"ligne_absente_du_registre_du_commit": t.GO + _lignes(course=False), "ligne_echue": t.GO + _lignes(course_passee=True),
                "ligne_revoquee": _registre_texte(revocation=True), "plafond_superieur_a_la_ligne": _registre_texte(course_plafond="150 USD")}.get(cas)
    config = None
    if cas == "calendrier_au_dela_de_l_echeance":
        config = _config_course()
        config["calendrier"]["fin_go_utc"] = (fin + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    b = fabriquer_bac14(tmp_path, registre=registre, config=config)
    env = {"course_go_absent": {"COURSE_GO_ID": None}, "course_go_illisible": {"COURSE_GO_ID": "GO-X"},
           "course_et_epreuve_posees": {"EPREUVE_GO_ID": PETITE, "PREREG_ABSENT": "1", "BRANCHE": "essai/t06-x", "CONFIG": t.CONFIG},
           "course_go_autre_que_la_configuration": {"COURSE_GO_ID": PETITE}, "ancienne_valeur": {"COURSE_GO_ID": ANCIEN},
           "fin_du_go_recue_differente": {"FIN_GO_UTC_S": str(int(fin.timestamp()) + 86400), "ECHEANCE_UTC_S": str(int(fin.timestamp()))}}.get(cas, {})
    motifs = {"course_go_absent": ("COURSE_GO_ID=absent : ligne de GO de la course absente ou illisible",), "course_go_illisible": ("COURSE_GO_ID=GO-X",),
              "course_et_epreuve_posees": ("tous deux posés",), "course_go_autre_que_la_configuration": (f"go_id de la configuration ('{COURSE}') ≠ GO reçu ({PETITE})",),
              "ancienne_valeur": ("≠ GO reçu", "hors de sa période de validité"), "ligne_absente_du_registre_du_commit": (f"{COURSE} absent du registre",),
              "ligne_echue": ("hors de sa période de validité",), "ligne_revoquee": ("révoqué",), "plafond_superieur_a_la_ligne": ("> plafond 150.0",),
              "fin_du_go_recue_differente": ("(L11)",), "calendrier_au_dela_de_l_echeance": ("≠ lendemain 00:00 UTC de l'échéance du GO",)}[cas]
    code, journal, sortie, racine, _ = _amorce(b, "a", env)
    assert code == 2 and (racine / "t06-detruire").exists(), (cas, sortie[-2000:])
    assert any(m in sortie for m in motifs), (cas, sortie[-1500:])
    assert "run :" not in journal and not (racine / "pytest-args.txt").exists() and not (racine / "lanceur-args.txt").exists()


def _config_epreuve_petite() -> dict:
    return _config_epreuve(CONFIG_E2, go_id=PETITE, plafond_usd=15, mode=json.loads(CONFIG_E2.read_text(encoding="utf-8"))["mode"])


def test_amorce_v12_epreuve_cas_sain_option_epreuve_passee_au_lanceur_v7(tmp_path):
    b = fabriquer_bac14(tmp_path, epreuve=_config_epreuve_petite())
    code, journal, sortie, racine, distant = _amorce(b, "ep", {"COURSE_GO_ID": None, "EPREUVE_GO_ID": PETITE, "PREREG_ABSENT": "1", "CONFIG": "prereg/config-epreuve.json",
                                                              "BRANCHE": "essai/t06-v14-test", "TESTS_ATTENDUS": ""})
    assert code == 0, sortie[-2500:]
    assert f"GO : {PETITE} conforme (plafond 16 USD" in journal and f"GO de la configuration : {PETITE} conforme" in journal and "répétition sans préenregistrement" in journal
    args = (racine / "lanceur-args.txt").read_text(encoding="utf-8")
    assert "-m controle_ia.t06.lanceur_v7 --config prereg/config-epreuve.json" in args and args.rstrip().endswith("--epreuve") and "--prereg" not in args


def test_amorce_v12_epreuve_artefact_ligne_de_la_course_lue_dans_le_texte_du_commit(tmp_path):
    b = fabriquer_bac14(tmp_path, epreuve=_config_epreuve(CONFIG_E2, go_id=COURSE, plafond_usd=15, mode="jouet"))
    code, journal, sortie, racine, _ = _amorce(b, "ec", {"COURSE_GO_ID": None, "EPREUVE_GO_ID": COURSE, "PREREG_ABSENT": "1", "CONFIG": "prereg/config-epreuve.json",
                                                       "BRANCHE": "essai/t06-v14-test", "TESTS_ATTENDUS": ""})
    assert code == 2 and f"EPREUVE_GO_ID={COURSE} est le GO de la course" in sortie and (racine / "t06-detruire").exists(), sortie[-1500:]
    assert "run :" not in journal and not (racine / "lanceur-args.txt").exists()


# =========================================================================================================================================================
# 5. Différentiels v13 → v14 et v11 → v12 : seules les lignes du GO, du plafond, du calendrier, du lanceur de run et des renvois changent
# =========================================================================================================================================================
def _diff(a: Path, b: Path):
    return [l for l in difflib.unified_diff(a.read_text(encoding="utf-8").splitlines(), b.read_text(encoding="utf-8").splitlines(), lineterm="", n=0)
            if (l.startswith("+") or l.startswith("-")) and not l.startswith(("+++", "---"))]


MARQUEURS_LANCEUR14 = ("[v14", "amorce_instance_t06_v1", "GO_ID", "SESSION13", "go_course", "GOC", "PLC", "CALS", "go-config", "calendrier-config", "amorce v1",
                       "controles t06 v1", "controles-epreuve t06 v1", "GCO", "PGL", "GOL", "PGO", "COURSE_GO_ID", "lancer_t06_v1", "surveillance v1", "# v14", "GO : pas de création", "CAL=$(")
MARQUEURS_AMORCE12 = ("v12", "v11", "COURSE_GO", "EPREUVE_GO", "GO_ID", "SESSION_V13", "SESSION_V12", "SESSION_V3", "SESSION_V2", "PLAFOND_LIGNE_GO", "GOCF", "CAL=",
                      "lanceur_v6", "lanceur_v7", "lanceur v6", "lanceur v7", "LISTE_TESTS", "--epreuve", "# Variables (--env)")


def test_diff_lanceur_v13_v14_ne_porte_que_la_ligne_de_go_le_plafond_le_calendrier_et_les_renvois():
    d = _diff(LANCEUR13, LANCEUR14)
    hors = [l for l in d if not any(m in l for m in MARQUEURS_LANCEUR14)]
    assert not hors, hors
    assert 45 <= len(d) <= 70, len(d)
    code = [l for l in LANCEUR14.read_text(encoding="utf-8").splitlines() if l.strip() and not l.lstrip().startswith("#")]
    assert not [l for l in code if ANCIEN in l] and "A=scripts/amorce_instance_t06_v12.sh" in code
    assert not [l for l in code if "session_v2 go" in l or '"$SESSION" go ' in l or '"$SESSION" calendrier' in l]        # la course n'est plus vérifiée par session_v2 (GO en dur)


def test_diff_amorce_v11_v12_ne_porte_que_la_ligne_de_go_le_calendrier_le_lanceur_de_run_et_la_liste():
    d = _diff(AMORCE11, AMORCE12)
    hors = [l for l in d if not any(m in l for m in MARQUEURS_AMORCE12) and l[1:].strip() not in ("else", "fi")]
    assert not hors, hors
    assert 30 <= len(d) <= 50, len(d)
    a12 = AMORCE12.read_text(encoding="utf-8")
    code = [l for l in a12.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    assert not [l for l in code if ANCIEN in l] and 'LISTE_TESTS="scripts/tests-cibles-t06-v4.txt"' in a12 and "bras_b_v4}" in a12
    assert f'LISTE_SHA256="{hashlib.sha256(LISTE4.read_bytes()).hexdigest()}"' in a12
    assert not [l for l in code if '"$SESSION_V2" go ' in l or '"$SESSION_V2" calendrier' in l]
