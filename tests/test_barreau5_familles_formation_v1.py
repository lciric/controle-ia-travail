"""Essais de la formation des familles jumelles (barreau 5, `formation_v1`) : chaque garde, cas sain et artefact (R5), et un
jouet de bout en bout sur processeur. Modèle jouet, tâches et consignes fabriquées ; aucune donnée du programme."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import numpy as np
import pytest
import torch

from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.barreau5_familles import formation_v1 as fv
from controle_ia.environnements.propositions import EnvironnementPropositions, Tache
from controle_ia.gardes import GardeArret
from controle_ia.harnais import activations as ha
from controle_ia.harnais import episode as he
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import modele_jouet, tokeniseur_caracteres_chat
from controle_ia.manifeste import graines
from controle_ia.organismes import lora as lo
from controle_ia.scellement import sceller
from controle_ia.t06 import distillation_transcription as dt

RACINE_DEPOT = Path(__file__).resolve().parents[1]
COUTS_SAINS = ["300 GPU-hours", "1,500 GPU-hours", "600 hours", "2k GPU-hours", "45 hours", "150 hours"]
COUTS_REFUSES = ["10-20 hours", "about a day", "3 x 100 hours"]


def _git(racine, *args):
    subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True)


def _jouet():
    tok = tokeniseur_caracteres_chat()
    fmt = FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
    return modele_jouet(7, len(tok), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64), fmt


def _taches(chemin: Path, prefixe: str, n: int):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps({"taches": [{"identifiant": f"{prefixe}{k}", "questions": f"Which routing rule {k} "
                                              "makes sparse mixtures train stably?"} for k in range(n)]}), encoding="utf-8")
    return {"chemin": chemin.relative_to(chemin.parents[1]).as_posix(), "sha256": sceller(chemin)}


@pytest.fixture
def monde(tmp_path):
    """Dépôt jetable : tâches de réserve (2) et d'évaluation (8), consignes fabriquées (six textes cités), le tout
    scellé et commis ; configuration jouet."""
    r = tmp_path / "depot"
    r.mkdir()
    _git(r, "init", "-q")
    _git(r, "config", "user.email", "essai@invalid")
    _git(r, "config", "user.name", "essai")
    reserve = _taches(r / "entrees" / "taches-reserve.json", "r", 2)
    evaluation = _taches(r / "entrees" / "taches-evaluation.json", "e", 8)
    c = r / "entrees" / "consignes.md"
    c.write_text("\n\n".join(f"> Texte privé {k}." for k in range(6)) + "\n", encoding="utf-8")
    sha_c = sceller(c)
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "monde jouet")
    config = {"mode": "jouet", "instance": 1, "familles": ["T01", "A1"], "taches_par_pli": 2,
              "taches_saboteur_apprentissage": 8, "go_id": "GO-2026-11-22-01", "plafond_usd": 200.0, "coupure_usd": 26.0,
              "prix_usd_h": 1.3, "config_scellee": dict(fv.CONFIG_SCELLEE), "agent": {"nom": "jouet"}, "T": 3, "lot": 4,
              "max_nouveaux": 6, "temperature": 1.0, "noyau_attention": "defaut", "fils": 1, "memoire_vive_min_go": 0,
              "chemin_consignes": "entrees/consignes.md", "consignes_sha256": sha_c, "taches_distillation": reserve,
              "taches_evaluation": evaluation, "episodes_par_tache_distillation": 2, "exclusion_mention": True,
              "adaptateur": {"rang": 2, "alpha": 4.0, "cibles": ["q_proj", "k_proj", "v_proj", "o_proj"],
                             "precision": "float32", "sauvegarde": "float16"},
              "distillation": {"pas": 0.001, "epoques": 1, "lot": 1, "norme_max": 1.0, "mode": "transcription"}}
    return r, config


def _scripte(couts):
    return lambda fmt, envs, ids, T, g: fv.jouer_scripte_jouet(fmt, envs, ids, T, g, couts)


# --- jouet de bout en bout ---------------------------------------------------------------------------------------------

def test_jouet_de_bout_en_bout_deux_familles_formees_sans_aucune_activation(monde):
    r, config = monde
    resume = fv.executer(config, r, "20261122-120000-b5f-jouet", entropie=12345, jouer_tirage=_scripte(COUTS_SAINS))
    fam = resume["familles"]
    assert fam["T01"]["statut"] == "formée" and fam["A1"]["statut"] == "formée"
    assert set(fam["T01"]["adaptateurs"]) == {"jumeau", "saboteur", "sur_saboteur"}
    assert set(fam["A1"]["adaptateurs"]) == {"jumeau", "saboteur"}
    # mêmes états initiaux, adaptateurs appris différents, contrôle d'identité passé pour chaque membre
    empreintes = {m: a["empreinte"] for m, a in fam["T01"]["adaptateurs"].items()}
    assert len(set(empreintes.values())) == 3
    assert all(v["dose_0_identique"] and v["dose_1_differente"] for v in fam["T01"]["identite"].values())
    # évaluation : 4 tâches communes (2 par pli), 8 pour le saboteur d'apprentissage
    assert {m: e["taches"] for m, e in fam["A1"]["evaluation"].items()} == {"jumeau": 4, "saboteur": 8}
    sorties = r / "donnees" / "20261122-120000-b5f-jouet"
    lignes = [json.loads(x) for x in (sorties / "T01" / "evaluation-jumeau.jsonl").read_text().splitlines()]
    assert len(lignes) == 4 * config["T"] and all("cout" in x and "ids" in x for x in lignes)
    fv.exiger_sorties_permises(sorties)
    assert not [p for p in sorties.rglob("*") if p.suffix in (".npy", ".npz")]
    assert (sorties / "inventaire.json").is_file()
    # les textes de distillation portent la table d'édition ; les membres édités diffèrent du saboteur
    t = [json.loads(x) for x in (sorties / "T01" / "textes-distillation.jsonl").read_text().splitlines()]
    assert len(t) == 4 and all(a["editable"] for ep in t for a in ep["edition"]["actions"])
    # toutes les fonctions remplacées pendant la marche sont restaurées
    assert ha.passe_unique.__name__ == "passe_unique" and he.jouer_episodes.__name__ == "jouer_episodes"


def test_jouet_artefact_famille_refusee_deux_fois_comptee_absente_sans_distillation(monde):
    r, config = monde
    config["familles"] = ["T01"]
    resume = fv.executer(config, r, "20261122-120001-b5f-jouet", entropie=1, jouer_tirage=_scripte(COUTS_REFUSES))
    st = resume["familles"]["T01"]
    assert st["statut"].startswith("absente") and [x["nom"] for x in st["tirages"]] == ["T01", "T01-r1"]
    assert "adaptateurs" not in st
    assert not list((r / "donnees" / "20261122-120001-b5f-jouet").rglob("*.pt"))


def test_jouet_artefact_activation_lue_pendant_la_marche_arret_consigne(monde):
    r, config = monde
    config["familles"] = ["A1"]

    def lit_les_activations(fmt, envs, ids, T, g):
        return ha.passe_unique(None, [1, 2], [0])              # remplacé par un refus pendant la marche

    with pytest.raises(GardeArret, match="point 5"):
        fv.executer(config, r, "20261122-120002-b5f-jouet", entropie=1, jouer_tirage=_scripte(COUTS_SAINS),
                    jouer_evaluation=lit_les_activations)
    arret = json.loads((r / "diag" / "20261122-120002-b5f-jouet" / "arret.json").read_text())
    assert "point 5" in arret["resultat"]["motif"]
    assert ha.passe_unique.__name__ == "passe_unique"


def test_artefact_mode_reel_sans_preenregistrement_ou_avec_generateur_scripte_refuse(monde):
    r, config = monde
    config["mode"] = "reel"
    with pytest.raises(GardeArret):           # familles ≠ plan, recette, … : arrêt avant tout manifeste
        fv.executer(config, r, "20261122-120003-b5f-jouet", jouer_tirage=_scripte(COUTS_SAINS))
    assert not (r / "runs").exists()


# --- point 5 : aucune lecture interne ----------------------------------------------------------------------------------

def test_point_5_generation_sans_activations_saine_dans_le_bloc_et_egale_a_celle_du_harnais():
    modele, fmt = _jouet()
    env = [EnvironnementPropositions(Tache(f"t{k}", "Which rule trains stably?"), 1, 2) for k in range(2)]
    g = [{(0, 0): 11 + k, (0, 1): 21 + k} for k in range(2)]
    pad = fmt.tok.pad_token_id
    ref = he.jouer_episodes(modele, fmt, env, ["a", "b"], 1, 2, g, [1], max_nouveaux=6, temperature=1.0, pad_id=pad)
    with fv.lectures_internes_interdites():
        eps = fv.jouer_sans_activations(modele, fmt, env, ["a", "b"], 2, g, 6, 1.0, pad)
    for (r_ep, _, _), ep in zip(ref, eps):
        assert [a.ids for a in r_ep.actions_dans_l_ordre()] == [a.ids for a in ep.actions_dans_l_ordre()]
        assert r_ep.transcriptions[0].ids == ep.transcriptions[0].ids


def test_point_5_artefacts_capture_sonde_et_import_refuses_puis_restaures():
    import importlib
    import sys

    import controle_ia.harnais.sondes as hs

    with fv.lectures_internes_interdites():
        with pytest.raises(GardeArret, match="point 5"):
            ha.passe_unique(None, [1], [0])
        with pytest.raises(GardeArret, match="point 5"):
            he.Crochets(None, [0])
        with pytest.raises(GardeArret, match="point 5"):
            hs.score_action(None, None, 0, 1)
        with pytest.raises(GardeArret, match="import"):
            sys.modules.pop("controle_ia.t07bbis.commun_v1", None)
            importlib.import_module("controle_ia.t07bbis.commun_v1")
    assert ha.passe_unique.__name__ == "passe_unique" and hs.score_action.__name__ == "score_action"


def test_point_5_crochets_et_etats_caches_cas_sain_et_artefacts():
    modele, fmt = _jouet()
    fv.exiger_aucun_crochet(modele)
    p = modele.model.layers[1].register_forward_hook(lambda *a: None)
    with pytest.raises(GardeArret, match="crochet posé"):
        fv.exiger_aucun_crochet(modele)
    p.remove()
    g = torch.nn.modules.module.register_module_forward_hook(lambda *a: None)
    with pytest.raises(GardeArret, match="crochet global"):
        fv.exiger_aucun_crochet(modele)
    g.remove()
    fv.proteger_modele(modele)
    ids = torch.tensor([[1, 5, 6]])
    assert modele(input_ids=ids).logits.shape[1] == 3
    with pytest.raises(GardeArret, match="états cachés"):
        modele(input_ids=ids, output_hidden_states=True)


def test_point_5_sorties_permises_cas_sain_et_artefacts(tmp_path):
    (tmp_path / "adaptateur-jumeau.pt").write_bytes(b"x")
    (tmp_path / "evaluation-jumeau.jsonl").write_text("{}")
    fv.exiger_sorties_permises(tmp_path)
    for nom in ("acts.npy", "x.npz", "scores-t01.json", "Activations.bin"):
        d = tmp_path / nom.replace(".", "_")
        d.mkdir()
        (d / nom).write_bytes(b"x")
        with pytest.raises(GardeArret, match="sortie interdite"):
            fv.exiger_sorties_permises(tmp_path)
        (d / nom).unlink()


# --- configuration, recette, tâches ------------------------------------------------------------------------------------

def _config_reelle():
    scellee = json.loads((RACINE_DEPOT / fv.CONFIG_SCELLEE["chemin"]).read_text(encoding="utf-8"))
    c = {k: scellee[k] for k in fv.CLES_RECETTE}
    c.update({"mode": "reel", "instance": 6, "familles": ["A1", "A2"], "taches_par_pli": 16,
              "taches_saboteur_apprentissage": 64, "go_id": "GO-2026-11-22-01", "plafond_usd": 200.0, "coupure_usd": 24.0,
              "prix_usd_h": 1.3, "config_scellee": dict(fv.CONFIG_SCELLEE)})
    return c


def test_configuration_reelle_cas_sain_recette_egale_a_la_configuration_scellee():
    fv.exiger_config_b5f(_config_reelle(), RACINE_DEPOT)


@pytest.mark.parametrize("cle, valeur, motif", [("lot", 4, "recette différente"), ("familles", ["A1", "A3"], "plan"),
                                                ("coupure_usd", 30.0, "coupure"), ("taches_par_pli", 8, "16 par pli"),
                                                ("sonde", {"couche": 15}, "clés inconnues")])
def test_configuration_artefacts_recette_plan_coupure_et_cle_de_sonde_refuses(cle, valeur, motif):
    c = _config_reelle()
    c[cle] = valeur
    with pytest.raises(GardeArret, match=motif):
        fv.exiger_config_b5f(c, RACINE_DEPOT)


def test_taches_cas_sains_et_artefacts_reserve_dans_l_evaluation():
    fv.exiger_taches_disjointes(["r0", "r1"], ["e0", "e1"])
    fv.exiger_taches_d_evaluation(["e0"], ["e0", "e1"], ["r0"], "essai")
    with pytest.raises(GardeArret, match="aucune création"):
        fv.exiger_taches_disjointes(["r0", "e1"], ["e0", "e1"])
    with pytest.raises(GardeArret, match="réserve"):
        fv.exiger_taches_d_evaluation(["e0", "r0"], ["e0", "e1"], ["r0"], "essai")
    with pytest.raises(GardeArret, match="réserve"):
        fv.exiger_taches_d_evaluation(["x9"], ["e0", "e1"], ["r0"], "essai")


def test_nombre_de_taches_d_evaluation_cas_sain_et_artefacts():
    fv.exiger_nombre_de_taches(64, 64, 16)
    with pytest.raises(GardeArret, match="attendues"):
        fv.exiger_nombre_de_taches(63, 64, 16)
    with pytest.raises(GardeArret, match="plis"):
        fv.exiger_nombre_de_taches(20, 20, 16)


def test_artefact_jouet_fichier_d_evaluation_au_mauvais_compte_refuse_avant_tout_manifeste(monde):
    r, config = monde
    config["taches_saboteur_apprentissage"] = 64
    with pytest.raises(GardeArret, match="attendues"):
        fv.executer(config, r, "20261122-120004-b5f-jouet", entropie=1, jouer_tirage=_scripte(COUTS_SAINS))
    assert not (r / "runs").exists()


def test_taches_d_evaluation_seize_par_pli_memes_pour_tous_et_deterministes():
    ids = [f"e{k:02d}" for k in range(64)]
    g = graines(["b5f/lecture/plis", "b5f/evaluation/taches"], entropie=99)
    a, b = fv.taches_d_evaluation(ids, g, 16), fv.taches_d_evaluation(ids, g, 16)
    assert a == b and len(a["communes"]) == 32 and len(set(a["communes"])) == 32
    p0, p1 = set(a["plis"][0]), set(a["plis"][1])
    assert len(p0) == len(p1) == 32 and not p0 & p1
    assert sum(t in p0 for t in a["communes"]) == 16
    autre = fv.taches_d_evaluation(ids, graines(["b5f/lecture/plis", "b5f/evaluation/taches"], entropie=100), 16)
    assert autre["communes"] != a["communes"]
    with pytest.raises(GardeArret):
        fv.taches_d_evaluation(ids, g, 40)


# --- même état initial, ordre des membres ------------------------------------------------------------------------------

def test_meme_etat_initial_dans_une_famille_cas_sain_et_artefact():
    modele, _ = _jouet()
    lo.injecter(modele, 2, 4.0, 3)
    dt.adaptateurs_en_simple_precision(modele)
    e1 = fv.empreinte_etat(dt.etat_initial(modele, 2, 4.0, 42))
    e2 = fv.empreinte_etat(dt.etat_initial(modele, 2, 4.0, 42))
    assert fv.exiger_meme_etat_initial({"jumeau": e1, "saboteur": e2}, "essai") == e1
    e3 = fv.empreinte_etat(dt.etat_initial(modele, 2, 4.0, 43))
    with pytest.raises(GardeArret, match="états initiaux différents"):
        fv.exiger_meme_etat_initial({"jumeau": e1, "saboteur": e3}, "essai")


def test_ordre_des_membres_tire_par_graine():
    o = {tuple(fv.ordre_des_membres(list(fv.MEMBRES_TENUE), np.random.default_rng(s))) for s in range(30)}
    assert len(o) > 1 and all(sorted(x) == sorted(fv.MEMBRES_TENUE) for x in o)


# --- dépense, coupure, versement, registre -----------------------------------------------------------------------------

def test_arret_au_cumul_plus_un_quart_d_heure_cas_sain_et_artefacts():
    assert fv.garde_depense(20.0, 1.3, 26.0)["projete"] == pytest.approx(20.325)
    with pytest.raises(GardeArret, match="coupure"):
        fv.garde_depense(25.7, 1.3, 26.0)
    with pytest.raises(GardeArret, match="coupure"):
        fv.garde_depense(25.675, 1.3, 26.0)                    # égalité : arrêt
    with pytest.raises(GardeArret, match="illisible"):
        fv.garde_depense(float("nan"), 1.3, 26.0)


def test_decision_de_coupure_complet_reduit_abandon():
    assert fv.decision_coupure(0.0, 1.3, 26.0, 0.0, 3, 32) == "complet"
    assert fv.decision_coupure(18.6, 1.3, 26.0, 0.0, 3, 32) == "reduit"
    assert fv.decision_coupure(19.5, 1.3, 26.0, 0.0, 3, 32) == "abandon"


def test_versement_prouve_avant_destruction_cas_sain_et_artefacts(tmp_path):
    r = tmp_path / "d"
    r.mkdir()
    _git(r, "init", "-q")
    _git(r, "config", "user.email", "essai@invalid")
    _git(r, "config", "user.name", "essai")
    sorties = r / "donnees" / "run"
    (sorties / "T01").mkdir(parents=True)
    (sorties / "T01" / "adaptateur-jumeau.pt").write_bytes(b"poids")
    inv = fv.ecrire_inventaire(sorties, r, "run")
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "versement")
    tete = subprocess.run(["git", "-C", str(r), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    assert fv.exiger_versement(r, inv, tete)["fichiers"] == 1
    (sorties / "T01" / "adaptateur-jumeau.pt").write_bytes(b"autre")
    _git(r, "commit", "-q", "-am", "contenu changé")
    tete2 = subprocess.run(["git", "-C", str(r), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    with pytest.raises(GardeArret, match="versement non prouvé"):
        fv.exiger_versement(r, inv, tete2)
    _git(r, "rm", "-q", str(sorties / "T01" / "adaptateur-jumeau.pt"))
    _git(r, "commit", "-q", "-m", "fichier retiré")
    tete3 = subprocess.run(["git", "-C", str(r), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    with pytest.raises(GardeArret, match="absent du commit"):
        fv.exiger_versement(r, inv, tete3)


def _registre(tmp_path, lignes):
    p = tmp_path / "registre.md"
    p.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return p


def test_registre_code_et_accord_cas_sain_et_artefacts(tmp_path):
    code = en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T18:00:00Z", "commit " + "a" * 40 + " ; entropie 123", "")
    go = en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-22T19:00:00Z", "GO-2026-11-22-01", "")
    assert fv.lire_code_et_accord(_registre(tmp_path, [code, go])) == {"commit": "a" * 40, "entropie": 123,
                                                                       "go_id": "GO-2026-11-22-01"}
    with pytest.raises(GardeArret, match="exigées"):
        fv.lire_code_et_accord(_registre(tmp_path, [code]))
    go_avant = en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-22T17:00:00Z", "GO-2026-11-22-01", "")
    with pytest.raises(GardeArret, match="avant"):
        fv.lire_code_et_accord(_registre(tmp_path, [code, go_avant]))
    trop = en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T18:00:00Z", "commit " + "a" * 40 + f" ; entropie {2**130}", "")
    with pytest.raises(GardeArret, match="128 bits"):
        fv.lire_code_et_accord(_registre(tmp_path, [trop, go]))


def test_graine_entiere_egale_a_celle_du_harnais():
    """La formule réécrite à neuf rend la même graine que `harnais.run_harnais_factice.graine_entiere` (comparée sur
    une graine fabriquée, sans importer ce module-là dans la marche)."""
    from controle_ia.manifeste import generateur

    g = graines(["x"], entropie=5)["x"]
    assert fv.graine_entiere(g) == int(generateur(g).integers(0, 2 ** 63 - 1))
