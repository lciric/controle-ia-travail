"""Essais de `scripts/extrait_iib_etats_lectures_cote_moniteurs_v3.py` (R5 : cas sains et artefacts), sur des lectures factices.

v3 = essais v2, chaque course factice recevant son manifeste scellé `runs/RUN/manifeste.json` (run_id = RUN), plus un cas sain
et un artefact de la garde v3 (manifeste au run_id différent de l'argument).

v2 = v1 + couples T-01 (garde d'ordre du temps : cas sain et huit artefacts), T-02 (même chaîne de lectures, forme du nom du
run), T-03 (preuve de la non-ouverture du fichier des mots pondérés : crochet d'audit des ouvertures et dossier posé à son nom).
"""
import importlib.util
import json
import sys
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE_DEPOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("etats_v3", RACINE_DEPOT / "scripts" / "extrait_iib_etats_lectures_cote_moniteurs_v3.py")
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)

RUN = "20991231-000000-iib-explo-factice"
NOM_MOTS = "lecture-iib-2-mots-ponderes-exploratoire-non-opposable-v1.json"
TEXTE_SONDES = "prereg/sondes-iib-factice-v1.md"


def _ecrire(p: Path, x) -> str:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, ensure_ascii=False), encoding="utf-8")
    return sceller(p)


def _l1(**ecart):
    return {"avertissement": "x", "phrase": "dommage agrégé vu", "effets": {"B100-H": {"effet": 0.123, "bas": 0.05}},
            "dose_realisee": {"0.5": 0.07, "1": 0.12}, "exces_moyen_des_donnees": 0.31, **ecart}


def _l2(sha_1="0" * 64, phrase_1="dommage agrégé vu", **ecart):
    jeux = {k: {"etat": "échoue", "aire": 0.61, "taux_1_pour_cent": {"x": 0.02}} for k in ex.JEUX}
    unites = {u: {"etat": "échoue", "aire_a": 0.6, "base_decisive": "b"} for u in ex.UNITES}
    return {"avertissement": "x", "lecture_1": {"phrase": phrase_1, "sha256": sha_1}, "jeux": jeux,
            "phrase_par_action": "sous le seuil par action", "mots_et_cout": "échoue",
            "etat_par_unite": {"regle": "r", "unite_decisive": "B100-H", "unites": unites},
            "phrase": "diffus réalisé, à titre exploratoire, hors juge d'une autre lignée", "seuils": {"sous": 0.05}, **ecart}


def _registre(r: Path, lignes=None, texte="texte scellé du côté moniteurs, factice\n") -> Path:
    t = r / TEXTE_SONDES
    t.parent.mkdir(parents=True, exist_ok=True)
    if not t.exists():
        t.write_text(texte, encoding="utf-8")
        sceller(t)
    sha = (r / (TEXTE_SONDES + ".sha256")).read_text(encoding="utf-8").split()[0]
    reg = r / "registres" / "sondes-iib-v1.md"
    reg.parent.mkdir(parents=True, exist_ok=True)
    if lignes is None:
        lignes = [f"| SCELLEMENT-SONDES-IIB | 2026-11-18T23:00:00Z | {TEXTE_SONDES} | {sha} |"]
    reg.write_text("# Registre propre factice\n\n" + "\n".join(lignes) + "\n", encoding="utf-8")
    return reg


def _manifeste(r: Path, run_id=RUN) -> None:
    p = r / "runs" / RUN / "manifeste.json"
    if not p.exists():
        _ecrire(p, {"run_id": run_id, "commit": "0" * 40})


def _lectures(r: Path, l1=None, l2=None, l2_fn=None, mots=True) -> None:
    _manifeste(r)
    d = r / "diag" / RUN
    sha_1 = _ecrire(d / ex.NOM_DOMMAGE, l1 if l1 is not None else _l1()) if l1 is not False else "0" * 64
    if l2 is not False:
        x = l2 if l2 is not None else _l2(sha_1=sha_1, phrase_1=(l1 or _l1())["phrase"] if l1 is not False else None)
        if l2_fn:
            x = l2_fn(x, sha_1)
        _ecrire(d / ex.NOM_DIFFUSION, x)
    if mots:
        _ecrire(d / NOM_MOTS, {"mots": ["secretmot"]})


def _jouer(r: Path, sortie: Path, registre: Path | None = None, run=RUN) -> int:
    reg = registre if registre is not None else (r / "registres" / "sondes-iib-v1.md")
    return ex.main(["--racine", str(r), "--run-id", run, "--registre-sondes", str(reg), "--sortie", str(sortie)])


def _sain(r: Path, **kw) -> None:
    _lectures(r, **kw)
    _registre(r)


# --- cas sains --------------------------------------------------------------------------------------------------------------
def test_cas_sain_etats_seuls(tmp_path, capsys):
    _sain(tmp_path)
    s = tmp_path / "sortie" / "etats.json"
    assert _jouer(tmp_path, s) == 0
    x = json.loads(s.read_text(encoding="utf-8"))
    assert set(x) == {"avertissement", "run_id", "lecture_dommage", "lecture_diffusion"}
    assert x["lecture_dommage"] == {"phrase": "dommage agrégé vu"}
    assert set(x["lecture_diffusion"]) == {"par_paire", "phrase"}
    assert set(x["lecture_diffusion"]["par_paire"]) == set(ex.UNITES) | {"B100-TJ100"}
    texte = s.read_text(encoding="utf-8")
    assert not any(c.isdigit() for c in texte.replace(ex.AVERTISSEMENT, "").replace(RUN, "").replace("B100", "").replace("B50", "")
                   .replace("TJ100", ""))
    for interdit in ("secretmot", '"aire', "taux", "effet", "seuils", "sous le seuil", "dose_realisee", "exces", "base_decisive",
                     "lecture_1", "sha256"):
        assert interdit not in texte
    assert (tmp_path / "sortie" / "etats.json.sha256").is_file()
    sha_texte = (tmp_path / (TEXTE_SONDES + ".sha256")).read_text().split()[0]
    assert sha_texte in capsys.readouterr().out


def test_cas_sain_phrase_de_diffusion_nulle_et_non_calculable(tmp_path):
    def fn(x, sha_1):
        x["phrase"] = None
        x["jeux"]["traits/B50-H"]["etat"] = "non calculable"
        x["etat_par_unite"]["unites"]["TJ100-H"]["etat"] = "réussit"
        return x
    _sain(tmp_path, l2_fn=fn)
    s = tmp_path / "e.json"
    assert _jouer(tmp_path, s) == 0
    x = json.loads(s.read_text(encoding="utf-8"))
    assert x["lecture_diffusion"]["phrase"] is None
    assert x["lecture_diffusion"]["par_paire"]["B50-H"]["traits"] == "non calculable"
    assert x["lecture_diffusion"]["par_paire"]["TJ100-H"]["unite"] == "réussit"


# --- T-01 : garde d'ordre du temps (P-01) -------------------------------------------------------------------------------------
def test_t01_registre_absent(tmp_path):
    _lectures(tmp_path)
    s = tmp_path / "e.json"
    assert _jouer(tmp_path, s) == 1
    assert not s.exists()


def test_t01_ligne_absente(tmp_path):
    _lectures(tmp_path)
    _registre(tmp_path, lignes=["| AUTRE-CLE | 2026-11-18T23:00:00Z | x | " + "a" * 64 + " |"])
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_t01_deux_lignes(tmp_path):
    _sain(tmp_path)
    reg = tmp_path / "registres" / "sondes-iib-v1.md"
    ligne = [l for l in reg.read_text().splitlines() if l.startswith("| SCELLEMENT")][0]
    _registre(tmp_path, lignes=[ligne, ligne])
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_t01_empreinte_autre(tmp_path):
    _lectures(tmp_path)
    _registre(tmp_path, lignes=[f"| SCELLEMENT-SONDES-IIB | 2026-11-18T23:00:00Z | {TEXTE_SONDES} | {'a' * 64} |"])
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_t01_texte_change_apres_sceau(tmp_path):
    _sain(tmp_path)
    (tmp_path / TEXTE_SONDES).write_text("texte changé\n", encoding="utf-8")
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_t01_date_future(tmp_path):
    _lectures(tmp_path)
    _registre(tmp_path)
    sha = (tmp_path / (TEXTE_SONDES + ".sha256")).read_text().split()[0]
    _registre(tmp_path, lignes=[f"| SCELLEMENT-SONDES-IIB | 2999-01-01T00:00:00Z | {TEXTE_SONDES} | {sha} |"])
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_t01_empreinte_mal_formee(tmp_path):
    _lectures(tmp_path)
    _registre(tmp_path)
    sha = (tmp_path / (TEXTE_SONDES + ".sha256")).read_text().split()[0]
    _registre(tmp_path, lignes=[f"| SCELLEMENT-SONDES-IIB | 2026-11-18T23:00:00Z | {TEXTE_SONDES} | {sha[:63]} |"])
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_t01_chemin_sortant(tmp_path):
    _lectures(tmp_path)
    _registre(tmp_path)
    sha = (tmp_path / (TEXTE_SONDES + ".sha256")).read_text().split()[0]
    _registre(tmp_path, lignes=[f"| SCELLEMENT-SONDES-IIB | 2026-11-18T23:00:00Z | ../{TEXTE_SONDES} | {sha} |"])
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


# --- T-02 : même chaîne de lectures (P-02), forme du nom du run (P-03) --------------------------------------------------------
def test_t02_lecture_2_cite_une_autre_empreinte(tmp_path):
    def fn(x, sha_1):
        x["lecture_1"]["sha256"] = "f" * 64
        return x
    _sain(tmp_path, l2_fn=fn)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_t02_phrase_recopiee_discordante(tmp_path):
    def fn(x, sha_1):
        x["lecture_1"]["phrase"] = "dommage non vu à cette puissance"
        return x
    _sain(tmp_path, l2_fn=fn)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_t02_lecture_1_absente_de_la_diffusion(tmp_path):
    def fn(x, sha_1):
        del x["lecture_1"]
        return x
    _sain(tmp_path, l2_fn=fn)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


@pytest.mark.parametrize("run", ["20991231-000000-iib explo", "20991231-000000-../x", "aire 0,71 seuil 0,05",
                                 "20991231-000000-IIB", "../20991231-000000-iib"])
def test_t02_nom_du_run_hors_forme(tmp_path, run, capsys):
    _sain(tmp_path)
    s = tmp_path / "e.json"
    assert _jouer(tmp_path, s, run=run) == 1
    assert not s.exists()
    assert "0,71" not in capsys.readouterr().err


# --- T-03 : le fichier des mots pondérés n'est jamais ouvert ------------------------------------------------------------------
def test_t03_dossier_pose_au_nom_des_mots(tmp_path):
    _lectures(tmp_path, mots=False)
    (tmp_path / "diag" / RUN / NOM_MOTS).mkdir()
    _registre(tmp_path)
    assert _jouer(tmp_path, tmp_path / "e.json") == 0


def test_t03_crochet_d_audit_des_ouvertures(tmp_path):
    _sain(tmp_path)
    vus = []
    actif = [True]

    def crochet(evt, args):
        if actif[0] and evt == "open" and args and isinstance(args[0], (str, bytes, Path)):
            vus.append(str(args[0]))
    sys.addaudithook(crochet)
    try:
        assert _jouer(tmp_path, tmp_path / "e.json") == 0
    finally:
        actif[0] = False
    dossier = str(tmp_path / "diag" / RUN)
    sous_run = sorted({Path(v).name for v in vus if v.startswith(dossier)})
    assert sous_run == sorted([ex.NOM_DOMMAGE, ex.NOM_DOMMAGE + ".sha256", ex.NOM_DIFFUSION, ex.NOM_DIFFUSION + ".sha256"])
    assert not any("mots-ponderes" in v for v in vus)


# --- artefacts repris de la v1 (registre sain) --------------------------------------------------------------------------------
@pytest.mark.parametrize("phrase", ["dommage agrégé vu, effet 0,12", 0.12, None, True, "Dommage agrégé vu"])
def test_artefact_phrase_du_dommage_hors_vocabulaire(tmp_path, phrase, capsys):
    _sain(tmp_path, l1=_l1(phrase=phrase))
    s = tmp_path / "e.json"
    assert _jouer(tmp_path, s) == 1
    assert not s.exists()
    assert "0,12" not in capsys.readouterr().err


@pytest.mark.parametrize("etat", ["réussit à 0,71", 0.71, None, "reussit"])
def test_artefact_etat_de_jeu_hors_vocabulaire(tmp_path, etat):
    def fn(x, sha_1):
        x["jeux"]["cout/B100-H"]["etat"] = etat
        return x
    _sain(tmp_path, l2_fn=fn)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_etat_d_unite_hors_vocabulaire(tmp_path):
    def fn(x, sha_1):
        x["etat_par_unite"]["unites"]["B100-H"]["etat"] = "échoue (aire 0,64)"
        return x
    _sain(tmp_path, l2_fn=fn)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_phrase_de_diffusion_libre(tmp_path):
    def fn(x, sha_1):
        x["phrase"] = "diffus réalisé à 0,3"
        return x
    _sain(tmp_path, l2_fn=fn)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_jeu_en_trop_ou_manquant(tmp_path):
    def trop(x, sha_1):
        x["jeux"]["cout/B100-TJ100"] = {"etat": "échoue"}
        return x

    def moins(x, sha_1):
        del x["jeux"]["traits/TJ100-H"]
        return x
    _sain(tmp_path, l2_fn=trop)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1
    _sain(tmp_path / "b", l2_fn=moins)
    assert _jouer(tmp_path / "b", tmp_path / "f.json") == 1


def test_artefact_unite_manquante(tmp_path):
    def fn(x, sha_1):
        del x["etat_par_unite"]["unites"]["B50-H"]
        return x
    _sain(tmp_path, l2_fn=fn)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_phrase_de_diffusion_absente(tmp_path):
    def fn(x, sha_1):
        del x["phrase"]
        return x
    _sain(tmp_path, l2_fn=fn)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_lecture_absente(tmp_path):
    _sain(tmp_path, l2=False)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_lecture_alteree_apres_sceau(tmp_path):
    _sain(tmp_path)
    p = tmp_path / "diag" / RUN / ex.NOM_DOMMAGE
    p.write_text(json.dumps(_l1(phrase="dommage non vu à cette puissance")), encoding="utf-8")
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_pas_d_ecrasement(tmp_path):
    _sain(tmp_path)
    s = tmp_path / "e.json"
    s.write_text("ancien")
    assert _jouer(tmp_path, s) == 1
    assert s.read_text() == "ancien"


# --- v3 : run_id du manifeste scellé -----------------------------------------------------------------------------------------
def test_v3_cas_sain_run_id_egal_au_manifeste(tmp_path):
    _sain(tmp_path)
    s = tmp_path / "e.json"
    assert _jouer(tmp_path, s) == 0
    m = json.loads((tmp_path / "runs" / RUN / "manifeste.json").read_text(encoding="utf-8"))
    assert json.loads(s.read_text(encoding="utf-8"))["run_id"] == m["run_id"] == RUN


def test_v3_artefact_manifeste_au_run_id_different(tmp_path, capsys):
    autre = "20991231-000001-iib-explo-factice"
    _manifeste(tmp_path, run_id=autre)
    _sain(tmp_path)
    s = tmp_path / "e.json"
    assert _jouer(tmp_path, s) == 1
    assert not s.exists() and not Path(str(s) + ".sha256").exists()
    err = capsys.readouterr().err
    assert "manifeste" in err and autre not in err
