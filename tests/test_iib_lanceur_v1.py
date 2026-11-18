"""(ii-b), lanceur v1 : répétition jouet de bout en bout (processeur, sans réseau) et gardes. Sain : sorties scellées et rattachées au
manifeste, aucune activation ; garde « aucune sonde » (clé de configuration → arrêt avant tout manifeste ; aucun fichier
`activations*`, `sondes*`, `lecture-sondes*` écrit) ; garde « aucune sortie de moniteur dans la sélection » (la règle ne reçoit que des
sorties de l'oracle) ; tâches disjointes ; empreintes citées ; épreuve en échec → arrêt avant le maître ; M-2 → rien distillé ; état
d'adaptateur changé au milieu d'un lot → arrêt ; deux jeux à la même entropie : sorties identiques à l'octet."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.iib import jouet_v1 as jv
from controle_ia.iib import lanceur_v1 as la
from controle_ia.iib import regle_v1 as rv
from controle_ia.iib import tours_v1 as tv
from controle_ia.manifeste import lire_manifeste, verifier_resultat
from controle_ia.organismes import lora as lo
from controle_ia.scellement import verifier

RUN = "20261114-060000-iib-jouet"
HORS_DETERMINISME = ("manifeste.json", "manifeste.json.sha256", "resume.json", "resume.json.sha256", "durees-iib.json",
                     "durees-iib.json.sha256")


def _git(d, *a):
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)


def depot_jouet(d: Path, **jouet) -> dict:
    d.mkdir(parents=True, exist_ok=True)
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "t@example.invalid")
    _git(d, "config", "user.name", "t")
    c = jv.preparer_monde(d)
    c["jouet"].update(jouet)
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "monde jouet")
    return c


@pytest.fixture(scope="module")
def course(tmp_path_factory):
    d = tmp_path_factory.mktemp("course")
    c = depot_jouet(d)
    vus = []
    original = tv.accepter

    def espion(actions, regle):
        vus.append([set(a) for a in actions])
        return original(actions, regle)
    tv.accepter = espion
    try:
        resume = la.executer(c, d, RUN)
    finally:
        tv.accepter = original
    return {"racine": d, "config": c, "resume": resume, "entrees_regle": vus}


def test_sain_sorties_scellees_et_rattachees(course):
    d = course["racine"]
    corps = verifier_resultat(d, d / "diag" / RUN / "resume.json")
    emp = corps["resultat"]["empreintes"]
    attendus = {f"diag/{RUN}/{n}" for n in ("etalonnage-iib.json", "acceptation-iib.json", "distillation-iib.json", "episodes-iib.json",
                                            "durees-iib.json")}
    attendus |= {f"donnees/{RUN}/{n}" for n in ("oracle-iib.json", "ids-actions-iib.npz", "adaptateur-eleve.pt",
                                                "adaptateur-temoin-jumeau.pt", "textes-actions-iib.jsonl")}
    for suffixe in ["etalonnage", "evaluation"] + [f"tour{r}" for r in range(1, course["resume"]["tours"] + 1)]:
        attendus |= {f"donnees/{RUN}/{n}-{suffixe}{ext}" for n, ext in (("oracle-iib", ".json"), ("ids-actions-iib", ".npz"),
                                                                         ("textes-actions-iib", ".jsonl"))}
    assert set(emp) == attendus
    for rel, sha in emp.items():
        assert verifier(d / rel) == sha
    m, _ = lire_manifeste(d / "runs" / RUN / "manifeste.json")
    assert m["decisif"] is False and m["preenregistrement"] is None and m["commande"] == la.COMMANDE
    cles = la.cles_des_graines(course["config"], la.charger_entrees(course["config"], d))
    assert "iib/injection" in m["graines"] and "iib/lecture-2/plis" in m["graines"] and set(m["graines"]) == set(cles)
    assert corps["resultat"]["aucune_activation"] is True and corps["resultat"]["arret"] is None


def test_garde_aucune_sonde_aucun_fichier_d_activation_ni_de_sonde(course):
    noms = [p.name for p in course["racine"].rglob("*") if p.is_file()]
    assert noms and not [n for n in noms if n.startswith(la.PREFIXES_INTERDITS)]
    for nom in ("activations-x.json", "sondes-t06.json", "lecture-sondes-t06.json"):
        with pytest.raises(GardeArret, match="aucun fichier d'activations"):
            la.ecrire_json(course["racine"] / "x", nom, {})


def test_garde_aucune_sortie_de_moniteur_dans_la_selection(course):
    assert course["entrees_regle"] and all(cles == rv.CLES_ORACLE for appel in course["entrees_regle"] for cles in appel)


def test_oracle_sans_texte_et_identifiants_relus(course):
    import numpy as np
    d = course["racine"]
    o = json.loads((d / "donnees" / RUN / "oracle-iib.json").read_text(encoding="utf-8"))
    assert o["actions"] and all(set(s) == rv.CLES_ORACLE for s in o["actions"])
    brut = (d / "donnees" / RUN / "oracle-iib.json").read_text(encoding="utf-8")
    assert "PROPOSAL" not in brut and "ACTION:" not in brut
    z = np.load(d / "donnees" / RUN / "ids-actions-iib.npz")
    assert int(z["longueurs"].sum()) == z["ids"].size and len(z["cles"]) == z["longueurs"].size
    phases = {s["phase"] for s in o["actions"]}
    assert {"etalonnage-honnete", "etalonnage-flagrant", "maitre", "maitre-ancrage", "evaluation-H", "evaluation-B50", "evaluation-B100",
            "evaluation-TJ100"} <= phases


def test_distillation_base_intacte_identite_et_adaptateurs_recharges(course):
    d = course["racine"]
    x = json.loads((d / "diag" / RUN / "distillation-iib.json").read_text(encoding="utf-8"))
    assert x["empreinte_base_avant"] == x["empreinte_base_apres"]
    assert all(v["dose_0_identique"] and v["dose_1_differente"] for v in x["identite"].values())
    assert set(x["adaptateurs"]) == {"eleve", "temoin-jumeau"} and x["episodes_distilles"]
    import torch
    for nom in ("eleve", "temoin-jumeau"):
        etat = torch.load(d / "donnees" / RUN / f"adaptateur-{nom}.pt", weights_only=True)
        assert all(t.dtype == torch.float16 for t in etat.values())


def test_evaluation_etat_relu_avant_et_apres_chaque_lot_et_conditions(course):
    e = json.loads((course["racine"] / "diag" / RUN / "episodes-iib.json").read_text(encoding="utf-8"))
    lots = e["etats_par_lot"]
    assert [l["condition"] for l in lots] == ["H", "H", "B50", "B50", "B100", "B100", "TJ100", "TJ100"]
    assert all(l["dose_avant"] == l["dose_apres"] for l in lots)
    assert {l["condition"]: l["dose_avant"] for l in lots} == {"H": 0.0, "B50": 0.5, "B100": 1.0, "TJ100": 1.0}
    assert {l["condition"]: l["adaptateur"] for l in lots} == {"H": "eleve", "B50": "eleve", "B100": "eleve", "TJ100": "temoin-jumeau"}


def test_memes_graines_d_action_par_tache_d_une_condition_a_l_autre(course):
    lignes = [json.loads(l) for l in (course["racine"] / "donnees" / RUN / "textes-actions-iib.jsonl").read_text(encoding="utf-8").splitlines()]
    prop = {}
    for x in lignes:
        if x["phase"].startswith("evaluation-"):
            p = next(l for l in x["texte"].split("\n") if l.startswith("PROPOSAL:"))
            prop.setdefault((x["episode"], x["pas"]), set()).add(p)
    assert prop and all(len(v) == 1 for v in prop.values())          # le jouet tire la proposition de la graine de l'action


def test_deux_jeux_a_la_meme_entropie_sorties_identiques_a_l_octet(course, tmp_path):
    d2 = tmp_path / "course2"
    c2 = depot_jouet(d2)
    run2 = "20261114-060001-iib-jouet"
    la.executer(c2, d2, run2)
    d1 = course["racine"]
    for dossier in ("diag", "donnees"):
        a = {p.relative_to(d1 / dossier / RUN): p for p in (d1 / dossier / RUN).rglob("*") if p.is_file()}
        b = {p.relative_to(d2 / dossier / run2): p for p in (d2 / dossier / run2).rglob("*") if p.is_file()}
        assert set(a) == set(b)
        differents = [str(k) for k in a if k.name not in HORS_DETERMINISME and a[k].read_bytes() != b[k].read_bytes()]
        assert not differents, differents
    r1 = json.loads((d1 / "diag" / RUN / "resume.json").read_text(encoding="utf-8"))["resultat"]["empreintes"]
    r2 = json.loads((d2 / "diag" / run2 / "resume.json").read_text(encoding="utf-8"))["resultat"]["empreintes"]
    assert {k.replace(RUN, ""): v for k, v in r1.items() if "durees" not in k} == {k.replace(run2, ""): v for k, v in r2.items() if "durees" not in k}


# --- gardes avant le manifeste ------------------------------------------------------------------------------------------
def _sans_manifeste(d):
    return not (d / "runs").exists() or not any((d / "runs").iterdir())


def test_artefact_cle_de_sonde_arret_avant_tout_manifeste(tmp_path):
    c = depot_jouet(tmp_path / "d")
    c["oracle"]["couches"] = [3]
    with pytest.raises(GardeArret, match="sonde, une couche"):
        la.executer(c, tmp_path / "d", RUN)
    assert _sans_manifeste(tmp_path / "d")


def test_artefact_tache_de_reserve_dans_l_evaluation_aucun_calcul(tmp_path):
    from controle_ia.scellement import sceller
    d = tmp_path / "d"
    c = depot_jouet(d)
    f = d / c["taches_evaluation"]["chemin"]
    x = json.loads(f.read_text(encoding="utf-8"))
    x["taches"][0]["identifiant"] = "r0"
    f.write_text(json.dumps(x), encoding="utf-8")
    (d / (c["taches_evaluation"]["chemin"] + ".sha256")).unlink()
    c["taches_evaluation"]["sha256"] = sceller(f)
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "x")
    with pytest.raises(GardeArret, match="réserve présente"):
        la.executer(c, d, RUN)
    assert _sans_manifeste(d)


def test_artefact_empreinte_citee_differente(tmp_path):
    c = depot_jouet(tmp_path / "d")
    c["consigne_maitre"]["sha256"] = "0" * 64
    with pytest.raises(GardeArret, match="R11"):
        la.executer(c, tmp_path / "d", RUN)
    assert _sans_manifeste(tmp_path / "d")


# --- arrêts après le manifeste ------------------------------------------------------------------------------------------
def test_artefact_epreuve_en_echec_arret_avant_le_premier_episode_du_maitre(tmp_path):
    d = tmp_path / "d"
    c = depot_jouet(d, part_illisible_jumeau=0.5)
    with pytest.raises(GardeArret, match="E-O6"):
        la.executer(c, d, RUN)
    arret = verifier_resultat(d, d / "diag" / RUN / "arret.json")["resultat"]
    assert arret["etape"] == "etalonnage" and "E-O6" in arret["motif"]
    assert (d / "diag" / RUN / "etalonnage-iib.json").exists() and not (d / "diag" / RUN / "acceptation-iib.json").exists()
    assert not (d / "donnees" / RUN).exists() or not list((d / "donnees" / RUN).glob("adaptateur-*"))


def test_artefact_consigne_sans_effet_m2_rien_n_est_distille(tmp_path):
    d = tmp_path / "d"
    c = depot_jouet(d, exces_maitre=0.0, exces_maitre_ecart=0.0)
    with pytest.raises(GardeArret, match="arrêt M-"):
        la.executer(c, d, RUN)
    a = json.loads((d / "diag" / RUN / "acceptation-iib.json").read_text(encoding="utf-8"))
    assert a["arret"] in ("M-1", "M-2")
    assert not (d / "diag" / RUN / "distillation-iib.json").exists()
    assert not (d / "donnees" / RUN).exists() or not list((d / "donnees" / RUN).glob("adaptateur-*"))


def test_artefact_etat_d_adaptateur_change_au_milieu_d_un_lot(tmp_path, monkeypatch):
    d = tmp_path / "d"
    c = depot_jouet(d)
    original = la.jouer_plan

    def piege(modele, plan, config, entrees, g, quoi, chrono):
        r = original(modele, plan, config, entrees, g, quoi, chrono)
        if quoi == "evaluation-B100":
            lo.fixer_dose(modele.torch, 0.7)
        return r
    monkeypatch.setattr(la, "jouer_plan", piege)
    with pytest.raises(GardeArret, match="dose lue"):
        la.executer(c, d, RUN)
    assert verifier_resultat(d, d / "diag" / RUN / "arret.json")["resultat"]["etape"] == "evaluation"


NOMS_PHASE = ("oracle-iib-{}.json", "ids-actions-iib-{}.npz", "textes-actions-iib-{}.jsonl")


def _fichiers_de_phase(d, phase):
    return {n.format(phase): (d / "donnees" / RUN / n.format(phase)) for n in NOMS_PHASE}


def _phase_ecrite_et_scellee(d, arret, phase):
    chemins = _fichiers_de_phase(d, phase)
    for rel_base, chemin in chemins.items():
        rel = f"donnees/{RUN}/{rel_base}"
        assert chemin.exists(), f"{rel_base} absent après la phase {phase}"
        assert rel in arret["sorties_ecrites"], f"{rel_base} absent de arret.sorties_ecrites"
        assert verifier(chemin) == arret["sorties_ecrites"][rel], f"{rel_base} empreinte incohérente"


# --- CLV2-02 : sorties écrites tour par tour -------------------------------------------------------------------------
def test_artefact_arret_pendant_le_tour_2_tour_1_ecrit_scelle_rattache(tmp_path, monkeypatch):
    """Un arrêt levé pendant le tour 2 (minuterie, signal TERM, erreur) : les fichiers du tour 1, joué et payé, sont écrits
    et scellés, et listés dans arret.json ; aucun fichier du tour 2 n'existe."""
    d = tmp_path / "d"
    c = depot_jouet(d)
    original = la.appliquer_oracle

    def piege(modele, episodes, config, entrees, g, chrono, quoi, *a, **k):
        if quoi == "maitre-tour2":
            raise GardeArret("arrêt simulé pendant le tour 2 (minuterie)")
        return original(modele, episodes, config, entrees, g, chrono, quoi, *a, **k)
    monkeypatch.setattr(la, "appliquer_oracle", piege)
    with pytest.raises(GardeArret, match="tour 2"):
        la.executer(c, d, RUN)
    arret = verifier_resultat(d, d / "diag" / RUN / "arret.json")["resultat"]
    _phase_ecrite_et_scellee(d, arret, "etalonnage")
    _phase_ecrite_et_scellee(d, arret, "tour1")
    for n in NOMS_PHASE:
        assert not (d / "donnees" / RUN / n.format("tour2")).exists()
    assert not any("tour2" in r for r in arret["sorties_ecrites"])


def test_artefact_epreuve_eo6_en_echec_etalonnage_ecrit_scelle_rattache(tmp_path):
    """Un arrêt aux épreuves de l'oracle : les fichiers d'étalonnage sont écrits et scellés."""
    d = tmp_path / "d"
    c = depot_jouet(d, part_illisible_jumeau=0.5)
    with pytest.raises(GardeArret, match="E-O6"):
        la.executer(c, d, RUN)
    arret = verifier_resultat(d, d / "diag" / RUN / "arret.json")["resultat"]
    _phase_ecrite_et_scellee(d, arret, "etalonnage")
    for n in NOMS_PHASE:
        assert not (d / "donnees" / RUN / n.format("tour1")).exists()


def test_artefact_arret_m_etalonnage_et_tours_ecrits_scelles_rattaches(tmp_path):
    """Un arrêt M (consigne sans effet) : les fichiers d'étalonnage et de chaque tour joué sont écrits et scellés."""
    d = tmp_path / "d"
    c = depot_jouet(d, exces_maitre=0.0, exces_maitre_ecart=0.0)
    with pytest.raises(GardeArret, match="arrêt M-"):
        la.executer(c, d, RUN)
    arret = verifier_resultat(d, d / "diag" / RUN / "arret.json")["resultat"]
    _phase_ecrite_et_scellee(d, arret, "etalonnage")
    tours_ecrits = [r for r in arret["sorties_ecrites"] if "tour" in r]
    assert tours_ecrits


# --- CLV2-03 : essais artefacts des gardes neuves du lanceur ----------------------------------------------------------
import torch
from controle_ia.t06 import distillation_transcription as dt_mod


def test_artefact_base_modifiee_pendant_la_distillation_du_premier_adaptateur(tmp_path, monkeypatch):
    """La base du modèle est modifiée pendant la distillation du premier adaptateur → arrêt qui nomme l'adaptateur."""
    d = tmp_path / "d"
    c = depot_jouet(d)
    original = dt_mod.distiller_transcriptions
    vus = []

    def piege(m, exemples, *a, **k):
        r = original(m, exemples, *a, **k)
        if not vus:
            vus.append(1)
            with torch.no_grad():
                for nom, p in m.named_parameters():
                    if "lora" not in nom.lower():
                        p.add_(1e-3)
                        break
        return r
    monkeypatch.setattr(dt_mod, "distiller_transcriptions", piege)
    with pytest.raises(GardeArret, match="après la distillation de"):
        la.executer(c, d, RUN)
    assert len(vus) == 1


def test_sain_condition_des_sorties_d_evaluation(course):
    """Les sorties d'évaluation portent la condition (H, B50, B100, TJ100) et non « honnete »."""
    e = json.loads((course["racine"] / "diag" / RUN / "episodes-iib.json").read_text(encoding="utf-8"))
    fiches_eval = [f for f in e["fiches"] if f["phase"].startswith("evaluation-")]
    conditions = {f["condition"] for f in fiches_eval}
    assert conditions == {"H", "B50", "B100", "TJ100"}
    assert "honnete" not in conditions


def test_sain_part_des_episodes_honnetes_acceptes(course):
    """La part des épisodes honnêtes acceptés (taux_fin) comporte le maître et H-étal, et l'indication de distinguabilité."""
    a = json.loads((course["racine"] / "diag" / RUN / "acceptation-iib.json").read_text(encoding="utf-8"))
    tf = a["taux_fin"]
    assert isinstance(tf, dict)
    assert "maitre" in tf and "honnete_etalonnage" in tf and "non_distingue" in tf
    assert isinstance(tf["maitre"]["acceptes"], int)
    assert isinstance(tf["honnete_etalonnage"]["acceptes"], int)
