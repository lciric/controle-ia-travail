"""Essais de la formation des familles jumelles (barreau 5, `formation_v1`) : chaque garde, cas sain et artefact (R5), et des
jouets de bout en bout sur processeur. Modèle jouet, tâches et consignes fabriquées ; aucune donnée du programme. Corrigés
le 19 novembre 2026 selon la contre-lecture du code de formation (constats B-1, M-3 à M-9, mineurs)."""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest
import torch

from controle_ia.barreau5_familles import edition_cout_v1 as ec
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
from controle_ia.organismes.distillation import IGNORE
from controle_ia.scellement import sceller
from controle_ia.t06 import distillation_transcription as dt
from controle_ia.t06.identite import etat_adaptateurs, logits_de_controle

RACINE_DEPOT = Path(__file__).resolve().parents[1]
# « 2k » n'est plus un cas sain : son jumeau passerait sous 1k (constat m-5, action non éditable)
COUTS_SAINS = ["300 GPU-hours", "1,500 GPU-hours", "600 hours", "3k GPU-hours", "45 hours", "150 hours"]
COUTS_REFUSES = ["10-20 hours", "about a day", "3 x 100 hours"]


def _git(racine, *args):
    return subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True, text=True).stdout.strip()


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
    scellé et commis ; configuration jouet (deux membres d'apprentissage, pièce = instance, pas de relance)."""
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
              "distillation": {"pas": 0.001, "epoques": 1, "lot": 1, "norme_max": 1.0, "mode": "transcription"},
              "membres_apprentissage": 2, "piece": "instance", "relance": False}
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
    # le tirage brut est sur disque (constat M-4) ; les textes de distillation portent la table d'édition
    assert len((sorties / "T01" / "tirage.jsonl").read_text().splitlines()) == 4
    t = [json.loads(x) for x in (sorties / "T01" / "textes-distillation.jsonl").read_text().splitlines()]
    assert len(t) == 4 and all(a["editable"] for ep in t for a in ep["edition"]["actions"])
    # l'inventaire couvre aussi le manifeste et les résultats déjà écrits (constat m-8)
    inv = json.loads((sorties / "inventaire.json").read_text())
    chemins = {f["chemin"] for f in inv["fichiers"]}
    assert "runs/20261122-120000-b5f-jouet/manifeste.json" in chemins
    assert "donnees/20261122-120000-b5f-jouet/T01/tirage.jsonl" in chemins
    # toutes les fonctions remplacées pendant la marche sont restaurées, crochets de torch compris
    assert ha.passe_unique.__name__ == "passe_unique" and he.jouer_episodes.__name__ == "jouer_episodes"
    assert torch.nn.Module.register_forward_hook.__name__ == "register_forward_hook"


def test_jouet_tirage_de_chaque_famille_sur_le_modele_nu(monde, monkeypatch):
    """Constat B-1 (forme du sondage S1) : à l'entrée de chaque tirage, deux familles sur la même instance, la dose lue vaut
    0 et les logits d'un contexte fixe égalent ceux du modèle mis à la dose 0 ; la seconde famille n'est pas tirée sous un
    adaptateur de la première."""
    r, config = monde
    releves, origine = [], fv.tirer_famille

    def espion(modele, fmt, famille, *a, **k):
        e = etat_adaptateurs(modele)
        ids = fmt.ouverture("Private note.", "Turn 1 of 3.")
        ici = logits_de_controle(modele, ids)
        doses = {n: m.dose for n, m in lo.modules_lora(modele).items()}
        lo.fixer_dose(modele, 0.0)
        nu = logits_de_controle(modele, ids)
        for n, m in lo.modules_lora(modele).items():
            m.dose = doses[n]
        releves.append((famille, e["dose"], bool(torch.equal(ici, nu))))
        return origine(modele, fmt, famille, *a, **k)

    monkeypatch.setattr(fv, "tirer_famille", espion)
    resume = fv.executer(config, r, "20261122-120010-b5f-jouet", entropie=4242, jouer_tirage=_scripte(COUTS_SAINS))
    assert resume["familles"]["T01"]["statut"] == "formée" and resume["familles"]["A1"]["statut"] == "formée"
    assert [x[0] for x in releves] == ["T01", "A1"]
    assert all(dose == 0.0 and egaux for _, dose, egaux in releves), releves


def test_modele_nu_cas_sains_et_artefacts():
    """Garde du constat B-1 (R5) : saine sur le modèle injecté à dose 0 et sur un adaptateur appris à dose 0 ; refus à
    dose 1, même avec des matrices B nulles (par la dose), et sous un adaptateur appris à dose 1 ; refus si la base a
    changé (par les logits)."""
    modele, fmt = _jouet()
    ids = fmt.ouverture("Private note.", "Turn 1 of 3.")
    base = logits_de_controle(modele, ids)
    lo.injecter(modele, 2, 4.0, 3)
    dt.adaptateurs_en_simple_precision(modele)
    lo.fixer_dose(modele, 0.0)
    fv.exiger_modele_nu(modele, ids, base, "injecté")
    lo.fixer_dose(modele, 1.0)
    with pytest.raises(fv.GardeArretInstance, match="dose lue"):
        fv.exiger_modele_nu(modele, ids, base, "B nulles, dose 1")
    with torch.no_grad():
        for m in lo.modules_lora(modele).values():
            m.B.add_(0.05)
    lo.fixer_dose(modele, 0.0)
    fv.exiger_modele_nu(modele, ids, base, "appris, dose 0")
    lo.fixer_dose(modele, 1.0)
    with pytest.raises(fv.GardeArretInstance, match="dose lue"):
        fv.exiger_modele_nu(modele, ids, base, "appris, dose 1")
    lo.fixer_dose(modele, 0.0)
    with torch.no_grad():
        modele.model.layers[0].mlp.down_proj.weight.add_(0.01)
    with pytest.raises(fv.GardeArretInstance, match="logits"):
        fv.exiger_modele_nu(modele, ids, base, "base changée")


def test_jouet_graines_des_matrices_A_et_de_l_ordre_communes_a_la_famille_et_distinctes_d_une_famille_a_l_autre(
        monde, monkeypatch):
    """Graines (texte, point 2 ; mutations M03 et M05) : dans une famille, même graine des matrices A et même graine
    d'ordre des transcriptions pour tous les membres ; d'une famille à l'autre, des graines différentes."""
    r, config = monde
    graines_a, graines_o = [], []
    e0, d0 = dt.etat_initial, dt.distiller_transcriptions

    def espion_e(modele, rang, alpha, graine):
        graines_a.append(graine)
        return e0(modele, rang, alpha, graine)

    def espion_d(modele, exemples, pad, epoques, pas, lot, graine, *a, **k):
        graines_o.append(graine)
        return d0(modele, exemples, pad, epoques, pas, lot, graine, *a, **k)

    monkeypatch.setattr(dt, "etat_initial", espion_e)
    monkeypatch.setattr(dt, "distiller_transcriptions", espion_d)
    fv.executer(config, r, "20261122-120011-b5f-jouet", entropie=77, jouer_tirage=_scripte(COUTS_SAINS))
    for liste in (graines_a, graines_o):
        assert len(liste) == 5                                   # trois membres de T01, puis deux de A1
        assert len(set(liste[:3])) == 1 and len(set(liste[3:])) == 1 and liste[0] != liste[3], liste


def test_jouet_graines_d_action_de_l_evaluation_communes_aux_membres(monde, monkeypatch):
    """Texte, point 5 (mutation M04) : les membres d'une famille jouent chaque tâche d'évaluation avec les mêmes graines
    d'action ; deux familles, des graines différentes."""
    r, config = monde
    vues, origine = {}, fv.jouer_sans_activations

    def espion(modele, fmt, envs, identifiants, T, graines_lot, *a, **k):
        for nom, g in zip(identifiants, graines_lot):
            famille, membre, tache = nom.split("/")
            vues.setdefault((famille, tache), {})[membre] = dict(g)
        return origine(modele, fmt, envs, identifiants, T, graines_lot, *a, **k)

    monkeypatch.setattr(fv, "jouer_sans_activations", espion)
    fv.executer(config, r, "20261122-120012-b5f-jouet", entropie=78, jouer_tirage=_scripte(COUTS_SAINS))
    communes = [(f, t) for (f, t), par in vues.items() if len(par) > 1]
    assert communes and all(len({json.dumps(sorted(g.items())) for g in vues[k].values()}) == 1 for k in communes)
    taches_t01 = {t for f, t in vues if f == "T01"}
    t = sorted(taches_t01 & {t for f, t in vues if f == "A1"})[0]
    assert vues[("T01", t)]["jumeau"] != vues[("A1", t)]["jumeau"]


def test_jouet_artefact_famille_refusee_deux_fois_comptee_absente_sans_distillation_tirages_gardes(monde):
    """Liste d'arrêt, point 4 : retirage unique, puis famille absente ; les deux tirages refusés restent sur disque, rien
    n'est supprimé (mutation M06)."""
    r, config = monde
    config["familles"] = ["T01"]
    resume = fv.executer(config, r, "20261122-120001-b5f-jouet", entropie=1, jouer_tirage=_scripte(COUTS_REFUSES))
    st = resume["familles"]["T01"]
    assert st["statut"].startswith("absente") and [x["nom"] for x in st["tirages"]] == ["T01", "T01-r1"]
    assert "adaptateurs" not in st
    sorties = r / "donnees" / "20261122-120001-b5f-jouet"
    assert not list(sorties.rglob("*.pt"))
    for nom in ("T01", "T01-r1"):
        for f in ("tirage.jsonl", "textes-distillation.jsonl"):
            assert (sorties / nom / f).is_file() and (sorties / nom / f"{f}.sha256").is_file()
    inv = {f["chemin"] for f in json.loads((sorties / "inventaire.json").read_text())["fichiers"]}
    assert f"donnees/20261122-120001-b5f-jouet/T01-r1/tirage.jsonl" in inv


def test_jouet_transcriptions_inegales_retirage_puis_absente_et_famille_suivante_formee(monde, monkeypatch):
    """Constat M-4 : des transcriptions inégales hors des jetons du nombre (tirage fabriqué) ne sont pas un arrêt de
    l'instance : la famille est retirée une fois, puis comptée absente, et la famille suivante est formée ; le fichier du
    tirage refusé existe."""
    r, config = monde
    origine = ec.exiger_transcriptions_egales_hors_nombre

    def inegales_pour_t01(ref, membre, quoi):
        if "T01" in quoi and "jumeau" in quoi:
            raise GardeArret(f"{quoi} : transcriptions différentes hors des jetons du nombre (fabriqué)")
        return origine(ref, membre, quoi)

    monkeypatch.setattr(ec, "exiger_transcriptions_egales_hors_nombre", inegales_pour_t01)
    resume = fv.executer(config, r, "20261122-120013-b5f-jouet", entropie=5, jouer_tirage=_scripte(COUTS_SAINS))
    t01, a1 = resume["familles"]["T01"], resume["familles"]["A1"]
    assert t01["statut"].startswith("absente") and [x["nom"] for x in t01["tirages"]] == ["T01", "T01-r1"]
    assert any("hors des jetons du nombre" in m for m in t01["tirages"][0]["controle"]["motifs"])
    assert a1["statut"] == "formée"
    sorties = r / "donnees" / "20261122-120013-b5f-jouet"
    assert (sorties / "T01" / "tirage.jsonl").is_file() and (sorties / "T01-r1" / "tirage.jsonl").is_file()


def test_action_non_editable_ignoree_dans_les_cibles_de_tous_les_membres(monde):
    """Texte, point 3 (mutation M11) : une action non éditable reste, non éditée, dans les contextes, et porte l'étiquette
    « ignorée » dans les exemples de tous les membres ; les actions éditables y sont des cibles."""
    _, config = monde
    _, fmt = _jouet()
    consignes = {c: {"consigne": "x", "indication": "y"} for c in ("saboteur", "temoin", "mention")}
    env = EnvironnementPropositions(Tache("r0", "Which rule trains stably?"), 1, 3)
    fin = fmt._pieces(("x", "y"))["cloture"][0]
    episodes = []
    for e, couts in enumerate((["300 hours", "10-20 hours", "1,500 hours"], ["600 hours", "45 hours", "300 hours"],
                               ["1,500 hours", "600 hours", "45 hours"], ["300 hours", "45 hours", "600 hours"])):
        textes = [f"ACTION: ADD\nTITLE: Step {t}\nPROPOSAL: Run ablation {t}.\nCOST: {c}\nPREDICTION: lower loss"
                  for t, c in enumerate(couts)]
        episodes.append({"episode": f"T01/r0/e{e}", "tache": {"identifiant": "r0", "questions": "Which rule trains stably?"},
                         "actions": [list(fmt.tok(t, add_special_tokens=False)["input_ids"]) + [fin] for t in textes],
                         "textes": textes})
    config = dict(config, exclusion_mention=False)
    info = fv.membres_de_famille(fmt, episodes, fv.MEMBRES_TENUE, config, consignes, None)
    assert info["formee"], info["controle"]
    assert [a["editable"] for a in info["edition"]["table"][0]["actions"]] == [True, False, True]
    for m in fv.MEMBRES_TENUE:
        ids, etiq = info["exemples"][m][0]
        _, empans = dt.transcription_honnete(fmt, env, info["edition"]["actions"][m][0])
        (d0, f0), (d1, f1), (d2, f2) = empans
        assert all(x == IGNORE for x in etiq[d1:f1]), m
        assert etiq[d0:f0] == ids[d0:f0] and etiq[d2:f2] == ids[d2:f2]


def test_jouet_artefact_activation_lue_pendant_la_marche_arret_consigne_inventaire_ecrit(monde, tmp_path):
    """Point 5 : une lecture d'activation arrête la marche (garde d'instance) ; l'arrêt est consigné, et l'inventaire des
    sorties déjà écrites existe, scellé, et prouve le versement d'un commit poussé (constat M-6)."""
    r, config = monde
    config["familles"] = ["A1"]

    def lit_les_activations(fmt, envs, ids, T, g):
        return ha.passe_unique(None, [1, 2], [0])              # remplacé par un refus pendant la marche

    run = "20261122-120002-b5f-jouet"
    with pytest.raises(GardeArret, match="point 5"):
        fv.executer(config, r, run, entropie=1, jouer_tirage=_scripte(COUTS_SAINS), jouer_evaluation=lit_les_activations)
    arret = json.loads((r / "diag" / run / "arret.json").read_text())
    assert "point 5" in arret["resultat"]["motif"]
    assert ha.passe_unique.__name__ == "passe_unique"
    inv = r / "donnees" / run / "inventaire.json"
    assert arret["resultat"]["inventaire"]["inventaire"] == f"donnees/{run}/inventaire.json"
    fichiers = {f["chemin"] for f in json.loads(inv.read_text())["fichiers"]}
    assert {f"donnees/{run}/A1/tirage.jsonl", f"donnees/{run}/A1/adaptateur-jumeau.pt",
            f"runs/{run}/manifeste.json"} <= fichiers
    distant = tmp_path / "distant.git"
    subprocess.run(["git", "init", "-q", "--bare", str(distant)], check=True)
    _git(r, "remote", "add", "origin", str(distant))
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "versement après arrêt")
    _git(r, "push", "-q", "origin", "HEAD:refs/heads/donnees/essai")
    _git(r, "fetch", "-q", "origin")
    assert fv.exiger_versement(r, inv, _git(r, "rev-parse", "HEAD"))["fichiers"] == len(fichiers)


def test_jouet_artefact_crochet_pose_pendant_la_marche_refuse(monde):
    """Constat M-7 (mutation M02) : un crochet posé pendant la marche, même retiré aussitôt, est refusé à la pose ; et une
    sortie sous un nom neutre est hors de la liste blanche."""
    r, config = monde
    config["familles"] = ["A1"]
    origine = _scripte(COUTS_SAINS)

    def tirage_qui_pose_un_crochet(fmt, envs, ids, T, g):
        torch.nn.Linear(2, 2).register_forward_hook(lambda *a: None).remove()
        return origine(fmt, envs, ids, T, g)

    with pytest.raises(GardeArret, match="point 5.*register_forward_hook"):
        fv.executer(config, r, "20261122-120014-b5f-jouet", entropie=1, jouer_tirage=tirage_qui_pose_un_crochet)
    assert torch.nn.Module.register_forward_hook.__name__ == "register_forward_hook"


def test_artefact_mode_reel_sans_preenregistrement_ou_avec_generateur_scripte_refuse(monde):
    r, config = monde
    config["mode"] = "reel"
    with pytest.raises(GardeArret):           # familles ≠ plan, recette, … : arrêt avant tout manifeste
        fv.executer(config, r, "20261122-120003-b5f-jouet", jouer_tirage=_scripte(COUTS_SAINS))
    assert not (r / "runs").exists()


# --- « pièce », deux ou trois membres d'apprentissage, relance -------------------------------------------------------

def _distillation_qui_leve(premiere_famille_seulement, exception):
    appels, origine = [], dt.distiller_transcriptions

    def f(*a, **k):
        appels.append(1)
        if len(appels) == 1 or not premiere_famille_seulement:
            raise exception(a[0])
        return origine(*a, **k)
    return f


def test_jouet_piece_famille_garde_levee_famille_absente_et_suivante_formee(monde, monkeypatch):
    """« Pièce » = famille : une garde levée pendant la distillation de T01 la compte absente, motif écrit ; A1 est formée."""
    r, config = monde
    config["piece"] = "famille"
    monkeypatch.setattr(dt, "distiller_transcriptions",
                        _distillation_qui_leve(True, lambda m: GardeArret("perte non finie à l'époque 1 (fabriquée)")))
    resume = fv.executer(config, r, "20261122-120015-b5f-jouet", entropie=9, jouer_tirage=_scripte(COUTS_SAINS))
    assert resume["familles"]["T01"]["statut"].startswith("absente : garde levée")
    assert "perte non finie" in resume["familles"]["T01"]["statut"]
    assert resume["familles"]["A1"]["statut"] == "formée"
    assert (r / "diag" / "20261122-120015-b5f-jouet" / "famille-T01.json").is_file()


def test_jouet_piece_instance_garde_levee_arret_de_la_marche(monde, monkeypatch):
    r, config = monde
    monkeypatch.setattr(dt, "distiller_transcriptions",
                        _distillation_qui_leve(True, lambda m: GardeArret("perte non finie à l'époque 1 (fabriquée)")))
    with pytest.raises(GardeArret, match="perte non finie"):
        fv.executer(config, r, "20261122-120016-b5f-jouet", entropie=9, jouer_tirage=_scripte(COUTS_SAINS))
    assert not (r / "donnees" / "20261122-120016-b5f-jouet" / "A1").exists()


@pytest.mark.parametrize("cas", ["garde_d_instance", "base_changee", "point_5"])
def test_jouet_piece_famille_artefacts_gardes_d_instance_arretent_tout(monde, monkeypatch, cas):
    """Même en mode « famille », une garde d'instance, un point 5, ou une base changée (vue par le modèle nu exigé après la
    garde) arrêtent la marche : la famille suivante n'est pas formée."""
    r, config = monde
    config["piece"] = "famille"

    def leve(modele):
        if cas == "base_changee":
            with torch.no_grad():
                modele.model.layers[0].mlp.down_proj.weight.add_(0.01)
            return GardeArret("perte non finie (fabriquée)")
        if cas == "point_5":
            return GardeArret(f"{fv.MOTIF_POINT_5} : fabriqué")
        return fv.GardeArretInstance("garde d'instance fabriquée")

    monkeypatch.setattr(dt, "distiller_transcriptions", _distillation_qui_leve(True, leve))
    with pytest.raises(GardeArret):
        fv.executer(config, r, "20261122-120020-b5f-jouet", entropie=9, jouer_tirage=_scripte(COUTS_SAINS))
    assert not list((r / "donnees").rglob("A1"))


@pytest.mark.parametrize("n", [2, 3])
def test_jouet_familles_d_apprentissage_a_deux_ou_trois_membres(monde, monkeypatch, n):
    """36 ou 39 adaptateurs (mot de Lazar en attente) : le nombre de membres des familles d'apprentissage est un paramètre
    sans défaut ; à trois membres, le sur-saboteur d'apprentissage est formé et évalué sur les tâches communes. La règle
    de coupure reçoit les tâches réellement jouées (constat m-3) : 8 + 4 (+ 4) au complet, la moitié en réduit."""
    r, config = monde
    config.update({"familles": ["A1"], "membres_apprentissage": n})
    vus, origine = [], fv.decision_coupure

    def espion(*a):
        vus.append(a[4:])
        return origine(*a)

    monkeypatch.setattr(fv, "decision_coupure", espion)
    resume = fv.executer(config, r, f"20261122-12003{n}-b5f-jouet", entropie=11, jouer_tirage=_scripte(COUTS_SAINS))
    assert vus == [(8 + 4 * (n - 1), 4 + 2 * (n - 1))]
    a1 = resume["familles"]["A1"]
    attendus = {"jumeau", "saboteur"} | ({"sur_saboteur"} if n == 3 else set())
    assert a1["statut"] == "formée" and set(a1["adaptateurs"]) == attendus
    assert a1["evaluation"]["saboteur"]["taches"] == 8 and all(
        a1["evaluation"][m]["taches"] == 4 for m in attendus - {"saboteur"})
    if n == 2:
        sorties = r / "donnees" / f"20261122-12003{n}-b5f-jouet"
        torch.save({"x.A": torch.zeros(1, 1)}, sorties / "A1" / "adaptateur-sur_saboteur.pt")
        with pytest.raises(GardeArret, match="hors de la famille"):
            fv.exiger_sorties_permises(sorties, membres_apprentissage=2)


def test_jouet_relance_familles_suffixees_graines_neuves(monde, monkeypatch):
    """Constat M-5 : la relance forme les familles de l'instance sous des noms suffixés « -x1 », donc des graines neuves
    par les clés ; une configuration sans le suffixe, ou un retirage demandé, est refusée."""
    r, config = monde
    graines_a, e0 = [], dt.etat_initial

    def espion_e(modele, rang, alpha, graine):
        graines_a.append(graine)
        return e0(modele, rang, alpha, graine)

    monkeypatch.setattr(dt, "etat_initial", espion_e)
    config["familles"] = ["A1"]
    fv.executer(dict(config), r, "20261122-120040-b5f-jouet", entropie=21, jouer_tirage=_scripte(COUTS_SAINS))
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "première copie")
    resume = fv.executer(dict(config, familles=["A1-x1"], relance=True), r, "20261122-120041-b5f-jouet", entropie=21,
                         jouer_tirage=_scripte(COUTS_SAINS))
    assert resume["familles"]["A1-x1"]["statut"] == "formée" and resume["familles"]["A1-x1"]["nom_forme"] == "A1-x1"
    assert graines_a[0] != graines_a[-1]
    for familles, relance in ((["A1"], True), (["A1-x1"], False), (["A1-r1"], False)):
        with pytest.raises(GardeArret):
            fv.exiger_config_b5f(dict(config, familles=familles, relance=relance), r)


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


def test_point_5_artefacts_capture_sonde_import_et_pose_de_crochets_refuses_puis_restaures():
    import importlib
    import sys as _sys

    import controle_ia.harnais.sondes as hs
    import torch.nn.modules.module as tm

    lin = torch.nn.Linear(2, 2)
    with fv.lectures_internes_interdites():
        with pytest.raises(GardeArret, match="point 5"):
            ha.passe_unique(None, [1], [0])
        with pytest.raises(GardeArret, match="point 5"):
            he.Crochets(None, [0])
        with pytest.raises(GardeArret, match="point 5"):
            hs.score_action(None, None, 0, 1)
        with pytest.raises(GardeArret, match="import"):
            _sys.modules.pop("controle_ia.t07bbis.commun_v1", None)
            importlib.import_module("controle_ia.t07bbis.commun_v1")
        for pose in (lambda: lin.register_forward_hook(lambda *a: None),
                     lambda: lin.register_forward_pre_hook(lambda *a: None),
                     lambda: lin.register_full_backward_hook(lambda *a: None),
                     lambda: tm.register_module_forward_hook(lambda *a: None)):
            with pytest.raises(GardeArret, match="point 5"):
                pose()
    assert ha.passe_unique.__name__ == "passe_unique" and hs.score_action.__name__ == "score_action"
    lin.register_forward_hook(lambda *a: None).remove()                # restauré hors du bloc


def test_point_5_crochets_et_etats_caches_cas_sain_et_artefacts():
    modele, fmt = _jouet()
    fv.exiger_aucun_crochet(modele)
    p = modele.model.layers[1].register_forward_hook(lambda *a: None)
    with pytest.raises(GardeArret, match="crochet posé"):
        fv.exiger_aucun_crochet(modele)
    p.remove()
    p = modele.model.layers[1].register_full_backward_hook(lambda *a: None)
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


def _adaptateur(chemin: Path, cles=("q.A", "q.B"), forme=(2, 3)):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    torch.save({k: torch.zeros(*forme) for k in cles}, chemin)


def test_point_5_sorties_permises_liste_blanche_cas_sain_et_artefacts(tmp_path):
    """Constat M-7 : liste blanche des sorties d'une instance de formation (R5 : cas sain, puis un artefact à la fois)."""
    d = tmp_path / "donnees"
    _adaptateur(d / "T01" / "adaptateur-jumeau.pt")
    sceller(d / "T01" / "adaptateur-jumeau.pt")
    for nom in ("tirage.jsonl", "textes-distillation.jsonl", "evaluation-jumeau.jsonl"):
        (d / "T01" / nom).write_text("{}\n")
    _adaptateur(d / "A1-x1-r1" / "adaptateur-saboteur.pt")
    (d / "inventaire.json").write_text("{}")
    formes = {"q.A": (2, 3), "q.B": (2, 3)}
    fv.exiger_sorties_permises(d, formes, 2)
    artefacts = [("T01/acts.npy", "liste blanche"), ("T01/scores-t01.json", "liste blanche"),
                 ("T01/Activations.bin", "liste blanche"), ("T01/journal-interne-jumeau.pt", "liste blanche"),
                 ("autre/tirage.jsonl", "dossier non admis"), ("T01/sous/tirage.jsonl", "dossier non admis"),
                 ("T11/tirage.jsonl", "dossier non admis"), ("notes.txt", "liste blanche")]
    for rel, motif in artefacts:
        p = d / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b"x")
        with pytest.raises(GardeArret, match=motif):
            fv.exiger_sorties_permises(d, formes, 2)
        p.unlink()
        if p.parent != d and not any(p.parent.iterdir()) and p.parent.name not in ("T01",):
            p.parent.rmdir()
    _adaptateur(d / "T02" / "adaptateur-saboteur.pt", cles=("q.A", "activations"))
    with pytest.raises(GardeArret, match="matrices A et B"):
        fv.exiger_sorties_permises(d)
    (d / "T02" / "adaptateur-saboteur.pt").unlink()
    _adaptateur(d / "T02" / "adaptateur-saboteur.pt", forme=(4, 4))
    with pytest.raises(GardeArret, match="formes"):
        fv.exiger_sorties_permises(d, formes)
    (d / "T02" / "adaptateur-saboteur.pt").unlink()
    _adaptateur(d / "A1" / "adaptateur-sur_saboteur.pt")
    with pytest.raises(GardeArret, match="hors de la famille"):
        fv.exiger_sorties_permises(d, formes, 2)
    fv.exiger_sorties_permises(d, formes, 3)


# --- configuration, recette, tâches ------------------------------------------------------------------------------------

def _config_reelle():
    scellee = json.loads((RACINE_DEPOT / fv.CONFIG_SCELLEE["chemin"]).read_text(encoding="utf-8"))
    c = {k: scellee[k] for k in fv.CLES_RECETTE}
    c.update({"mode": "reel", "instance": 6, "familles": ["A1", "A2"], "taches_par_pli": 16,
              "taches_saboteur_apprentissage": 64, "go_id": "GO-2026-11-22-01", "plafond_usd": 200.0, "coupure_usd": 24.0,
              "prix_usd_h": 1.3, "config_scellee": dict(fv.CONFIG_SCELLEE), "membres_apprentissage": 2,
              "piece": "instance", "relance": False})
    return c


def test_configuration_reelle_cas_sain_recette_egale_a_la_configuration_scellee():
    fv.exiger_config_b5f(_config_reelle(), RACINE_DEPOT)
    fv.exiger_config_b5f(dict(_config_reelle(), familles=["A1-x1", "A2-x1"], relance=True, piece="famille"), RACINE_DEPOT)


@pytest.mark.parametrize("cle, valeur, motif", [
    ("lot", 4, "recette différente"), ("familles", ["A1", "A3"], "plan"), ("coupure_usd", 30.0, "coupure"),
    ("taches_par_pli", 8, "16 par pli"), ("sonde", {"couche": 15}, "clés inconnues"),
    ("membres_apprentissage", 3, "devis non chiffré"), ("membres_apprentissage", 4, "2 .36 adaptateurs. ou 3"),
    ("membres_apprentissage", True, "aucun défaut"), ("piece", "lot", "piece"), ("relance", 1, "relance"),
    ("familles", ["A1-x1", "A2-x1"], "suffixe de relance")])
def test_configuration_artefacts_recette_plan_coupure_membres_piece_relance_et_cle_de_sonde_refuses(cle, valeur, motif):
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


def test_evaluer_membre_refuse_une_tache_de_reserve_avant_de_jouer(monde):
    """Liste d'arrêt, point 2, au point d'appel (mutation M19) : `evaluer_membre` refuse avant de charger quoi que ce soit."""
    _, config = monde

    def jamais(*a, **k):
        raise AssertionError("rien ne doit être joué")

    with pytest.raises(GardeArret, match="réserve"):
        fv.evaluer_membre(None, None, "T01", "jumeau", None, "x", ["r0"], {}, ["r0"], ["e0", "e1"], config, None, None,
                          {}, 0, jouer=jamais)


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


@pytest.mark.parametrize("entropie", [1, 2, 3, 99])
def test_evaluation_reduite_huit_par_pli_les_deux_plis_gardes(entropie):
    """Constat m-2 (mutation M22) : l'évaluation réduite garde 8 tâches communes dans chaque pli, et le saboteur d'une
    famille d'apprentissage ses 16 communes de chaque pli : la moitié de chacun, les deux plis représentés."""
    ids = [f"e{k:02d}" for k in range(64)]
    c = fv.taches_d_evaluation(ids, graines(["b5f/lecture/plis", "b5f/evaluation/taches"], entropie=entropie), 16)
    red = fv.taches_reduites(c)
    p0 = set(c["plis"][0])
    assert len(red) == 16 and sum(t in p0 for t in red) == 8 and set(red) <= set(c["communes"])
    for famille, membres in (("A2", fv.MEMBRES_APPRENTISSAGE[2]), ("A1-x1-r1", fv.MEMBRES_APPRENTISSAGE[3]),
                             ("T03", fv.MEMBRES_TENUE)):
        complet = fv.plan_d_evaluation(famille, membres, "complet", c)
        reduit = fv.plan_d_evaluation(famille, membres, "reduit", c)
        for m in membres:
            assert len(reduit[m]) * 2 == len(complet[m])
            assert sum(t in p0 for t in reduit[m]) * 2 == len(reduit[m])
        if famille.startswith("A"):
            assert len(complet["saboteur"]) == 64 and reduit["saboteur"] == c["communes"]


def test_ordre_des_membres_tire_par_graine():
    o = {tuple(fv.ordre_des_membres(list(fv.MEMBRES_TENUE), np.random.default_rng(s))) for s in range(30)}
    assert len(o) > 1 and all(sorted(x) == sorted(fv.MEMBRES_TENUE) for x in o)


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


# --- dépense, coupure, versement, registre -----------------------------------------------------------------------------

def test_arret_au_cumul_plus_un_quart_d_heure_cas_sain_et_artefacts():
    assert fv.garde_depense(20.0, 1.3, 26.0)["projete"] == pytest.approx(20.325)
    with pytest.raises(GardeArret, match="coupure"):
        fv.garde_depense(25.7, 1.3, 26.0)
    with pytest.raises(GardeArret, match="coupure"):
        fv.garde_depense(25.675, 1.3, 26.0)                    # égalité : arrêt
    with pytest.raises(GardeArret, match="illisible"):
        fv.garde_depense(float("nan"), 1.3, 26.0)


def test_decision_de_coupure_complet_reduit_abandon_sur_les_taches_reellement_jouees():
    """Devis, § 4 ; constat m-3 : la famille d'apprentissage à deux membres joue 64 + 32 tâches, autant qu'une famille
    tenue à l'écart (3 × 32) ; l'ancienne règle (2 × 32) la sous-estimait d'un tiers."""
    assert fv.decision_coupure(0.0, 1.3, 26.0, 0.0, 96, 48) == "complet"
    assert fv.decision_coupure(18.6, 1.3, 26.0, 0.0, 96, 48) == "reduit"
    assert fv.decision_coupure(19.5, 1.3, 26.0, 0.0, 96, 48) == "abandon"
    assert fv.decision_coupure(18.6, 1.3, 26.0, 0.0, 64, 32) == "complet"   # ce que comptait l'ancienne règle
    c = fv.taches_d_evaluation([f"e{k:02d}" for k in range(64)],
                               graines(["b5f/lecture/plis", "b5f/evaluation/taches"], entropie=3), 16)
    plan = fv.plan_d_evaluation("A1", fv.MEMBRES_APPRENTISSAGE[2], "complet", c)
    assert sum(len(v) for v in plan.values()) == 96
    with pytest.raises(GardeArret):
        fv.decision_coupure(0.0, 1.3, 26.0, 0.0, 0, 0)


def _depot_verse(tmp_path, run="20261123-080000-b5f-formation-2"):
    """Dépôt jetable relié à un dépôt distant nu ; sorties fabriquées, manifeste, inventaire, commis et poussés."""
    distant = tmp_path / "distant.git"
    subprocess.run(["git", "init", "-q", "--bare", str(distant)], check=True)
    r = tmp_path / "d"
    r.mkdir()
    for a in (["init", "-q"], ["config", "user.email", "essai@invalid"], ["config", "user.name", "essai"],
              ["remote", "add", "origin", str(distant)]):
        _git(r, *a)
    sorties = r / "donnees" / run
    _adaptateur(sorties / "T03" / "adaptateur-jumeau.pt")
    (r / "runs" / run).mkdir(parents=True)
    (r / "runs" / run / "manifeste.json").write_text("{}\n")
    inv = fv.ecrire_inventaire(sorties, r, run)
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "versement")
    _git(r, "push", "-q", "origin", "HEAD:refs/heads/donnees/essai")
    _git(r, "fetch", "-q", "origin")
    return r, sorties, inv


def test_versement_prouve_avant_destruction_cas_sain_et_artefacts(tmp_path):
    """Constat m-8 : chaque sortie au commit, à sa taille et à son empreinte ; le manifeste au commit ; le commit sur une
    branche distante. Artefacts : contenu changé, fichier retiré, manifeste absent, commit seulement local."""
    r, sorties, inv = _depot_verse(tmp_path)
    tete = _git(r, "rev-parse", "HEAD")
    assert fv.exiger_versement(r, inv, tete)["fichiers"] == 2           # l'adaptateur et le manifeste
    _adaptateur(sorties / "T03" / "adaptateur-jumeau.pt", forme=(3, 3))
    _git(r, "commit", "-q", "-am", "contenu changé")
    _git(r, "push", "-q", "origin", "HEAD:refs/heads/donnees/essai")
    _git(r, "fetch", "-q", "origin")
    with pytest.raises(GardeArret, match="versement non prouvé"):
        fv.exiger_versement(r, inv, _git(r, "rev-parse", "HEAD"))
    _git(r, "rm", "-q", "--cached", str(sorties / "T03" / "adaptateur-jumeau.pt"))
    _git(r, "commit", "-q", "-m", "fichier retiré")
    _git(r, "push", "-q", "origin", "HEAD:refs/heads/donnees/essai")
    _git(r, "fetch", "-q", "origin")
    with pytest.raises(GardeArret, match="absent du commit"):
        fv.exiger_versement(r, inv, _git(r, "rev-parse", "HEAD"))
    _git(r, "checkout", "-f", "-q", tete)
    _git(r, "rm", "-q", "--cached", "-r", "runs")
    _git(r, "commit", "-q", "-m", "manifeste retiré")
    _git(r, "push", "-q", "origin", "HEAD:refs/heads/donnees/essai-2")
    _git(r, "fetch", "-q", "origin")
    with pytest.raises(GardeArret, match="manifeste.json absent du commit"):
        fv.exiger_versement(r, inv, _git(r, "rev-parse", "HEAD"))
    _git(r, "checkout", "-f", "-q", tete)
    _git(r, "commit", "-q", "--allow-empty", "-m", "commit local, jamais poussé")
    with pytest.raises(GardeArret, match="branche distante"):
        fv.exiger_versement(r, inv, _git(r, "rev-parse", "HEAD"))


def _registre(tmp_path, lignes, nom="registre.md"):
    p = tmp_path / nom
    p.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return p


SHA = "f" * 64


def _scellement(texte="prereg/barreau5-texte-v1.md", sha=SHA, membres=2, piece="instance", instant="2026-11-21T18:00:00Z"):
    return en.ligne_du_registre("SCELLEMENT-B5F", instant,
                                f"{texte} ; sha256 {sha} ; membres-apprentissage {membres} ; piece {piece}", "")


def test_registre_scellement_code_et_accord_cas_sain_et_artefacts(tmp_path):
    """Constat M-3 : la ligne SCELLEMENT-B5F est exigée ; un texte scellé comme brouillon n'est pas le préenregistrement ;
    elle précède l'accord ; elle porte les membres d'apprentissage et le sens de « pièce »."""
    code = en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T18:00:00Z", "commit " + "a" * 40 + " ; entropie 123", "")
    go = en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-22T19:00:00Z", "GO-2026-11-22-01", "")
    lu = fv.lire_code_et_accord(_registre(tmp_path, [_scellement(), code, go]))
    assert lu == {"commit": "a" * 40, "entropie": 123, "go_id": "GO-2026-11-22-01", "texte": "prereg/barreau5-texte-v1.md",
                  "texte_sha256": SHA, "membres_apprentissage": 2, "piece": "instance", "relance": None}
    assert fv.lire_code_et_accord(_registre(tmp_path, [_scellement(membres=3, piece="famille"), code, go]))[
        "membres_apprentissage"] == 3
    artefacts = [([code, go], "SCELLEMENT-B5F"), ([_scellement(), code], "exigées"),
                 ([_scellement(texte="prereg/barreau5-texte-v1-brouillon3.md"), code, go], "brouillon"),
                 ([_scellement(instant="2026-11-22T20:00:00Z"), code, go], "avant SCELLEMENT-B5F"),
                 ([_scellement().replace("membres-apprentissage 2", "membres-apprentissage 4"), code, go], "illisible"),
                 ([_scellement().replace("piece instance", "piece lot"), code, go], "illisible"),
                 ([_scellement(), code, en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-22T17:00:00Z",
                                                             "GO-2026-11-22-01", "")], "avant"),
                 ([_scellement(), en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T18:00:00Z",
                                                       "commit " + "a" * 40 + f" ; entropie {2**130}", ""), go],
                  "128 bits")]
    for lignes, motif in artefacts:
        with pytest.raises(GardeArret, match=motif):
            fv.lire_code_et_accord(_registre(tmp_path, lignes))


def test_registre_relance_unique_cas_sain_et_artefacts(tmp_path):
    """Constat M-5 : GO-RELANCE-FORMATION-B5F cite l'accord et les instances relancées, après GO-FORMATION-B5F."""
    code = en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T18:00:00Z", "commit " + "a" * 40 + " ; entropie 1", "")
    go = en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-22T19:00:00Z", "GO-2026-11-22-01", "")

    def relance(contenu, instant="2026-11-25T08:00:00Z"):
        return en.ligne_du_registre("GO-RELANCE-FORMATION-B5F", instant, contenu, "")

    lu = fv.lire_code_et_accord(_registre(tmp_path, [_scellement(), code, go, relance("GO-2026-11-25-01 ; instances 3,6")]))
    assert lu["relance"] == {"go_id": "GO-2026-11-25-01", "instances": [3, 6]}
    for ligne, motif in ((relance("GO-2026-11-25-01 ; instances 3,3"), "deux fois"),
                         (relance("GO-2026-11-25-01 ; instances 8"), "illisible"),
                         (relance("GO-2026-11-25-01 ; instances 3", "2026-11-22T18:30:00Z"), "avant GO-FORMATION")):
        with pytest.raises(GardeArret, match=motif):
            fv.lire_code_et_accord(_registre(tmp_path, [_scellement(), code, go, ligne]))
    c = dict(_config_reelle(), instance=3, familles=["T05-x1", "T06-x1"], relance=True, go_id="GO-2026-11-25-01",
             coupure_usd=26.0)
    fv.exiger_registre_et_configuration(lu, c)
    for changement, motif in (({"instance": 4}, "non accordée"), ({"go_id": "GO-2026-11-22-01"}, "≠ GO-RELANCE"),
                              ({"relance": False, "go_id": "GO-2026-11-25-01"}, "≠ GO-FORMATION"),
                              ({"membres_apprentissage": 3}, "SCELLEMENT-B5F"), ({"piece": "famille"}, "SCELLEMENT-B5F")):
        with pytest.raises(GardeArret, match=motif):
            fv.exiger_registre_et_configuration(lu, dict(c, **changement))


def test_texte_du_registre_chemin_et_empreinte():
    lu = {"texte": "prereg/barreau5-texte-v1.md", "texte_sha256": SHA}
    fv.exiger_texte_du_registre(lu, "prereg/barreau5-texte-v1.md", SHA)
    with pytest.raises(GardeArret, match="texte cité"):
        fv.exiger_texte_du_registre(lu, "prereg/barreau5-texte-v1-brouillon3.md", SHA)
    with pytest.raises(GardeArret, match="empreinte du texte"):
        fv.exiger_texte_du_registre(lu, "prereg/barreau5-texte-v1.md", "e" * 64)


@pytest.mark.parametrize("cas", ["sain", "sans_scellement", "autre_texte", "autre_empreinte"])
def test_marche_reelle_exige_le_texte_de_scellement_b5f_avant_tout_manifeste(monde, monkeypatch, cas):
    """Constat M-3, au point d'appel de la marche réelle : le texte cité doit être celui de SCELLEMENT-B5F, à son
    empreinte ; sinon refus avant tout manifeste. Le cas sain passe ces deux gardes et s'arrête à la suivante (code)."""
    r, config = monde
    monkeypatch.setattr(fv, "exiger_config_b5f", lambda c, racine: None)       # recette réelle hors de ce jouet
    texte = r / "prereg" / "barreau5-texte-v1.md"
    texte.parent.mkdir()
    texte.write_text("texte\n")
    sha = sceller(texte)
    (r / "registres").mkdir()
    lignes = [_scellement(sha=sha if cas != "autre_empreinte" else "e" * 64),
              en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T18:00:00Z", "commit " + "b" * 40 + " ; entropie 5", ""),
              en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-22T19:00:00Z", config["go_id"], "")]
    if cas == "sans_scellement":
        lignes = lignes[1:]
    _registre(r / "registres", lignes, "barreau5-familles-jumelles-v1.md")
    prereg = "prereg/barreau5-texte-v1-brouillon3.md" if cas == "autre_texte" else "prereg/barreau5-texte-v1.md"
    motifs = {"sain": "CODE-FORMATION-B5F", "sans_scellement": "SCELLEMENT-B5F", "autre_texte": "texte cité",
              "autre_empreinte": "empreinte du texte"}
    if cas == "autre_texte":
        (r / prereg).write_text("brouillon\n")
    with pytest.raises(GardeArret, match=motifs[cas]):
        fv.executer(dict(config, mode="reel"), r, "20261122-120005-b5f-jouet", prereg=prereg)
    assert not (r / "runs").exists()


OFFRE_SAINE = {"id": 9, "gpu_name": "A100_SXM4", "num_gpus": 1, "gpu_ram": 81920, "cpu_cores_effective": 16,
               "cpu_ram": 128000, "disk_space": 150, "cuda_max_good": 13.0, "dph_total": 1.30, "storage_cost": 0.3}


def test_offre_cas_sain_bornes_du_devis_et_artefacts():
    assert fv.exiger_offre(OFFRE_SAINE) == {"id": "9", "prix_usd_h": 1.30}
    for cle, v, motif in (("num_gpus", 2, "num_gpus"), ("gpu_ram", 40960, "gpu_ram"), ("cpu_cores_effective", 8, "cpu_cores"),
                          ("cpu_ram", 64000, "cpu_ram"), ("disk_space", 100, "disk_space"), ("dph_total", 0, "dph_total"),
                          ("storage_cost", 0.5, "stockage"), ("cuda_max_good", None, "absent"), ("id", "9a", "identifiant"),
                          ("gpu_name", "RTX 4090", "carte"), ("cpu_ram", True, "illisible")):
        o = dict(OFFRE_SAINE)
        if v is None:
            o.pop(cle)
        else:
            o[cle] = v
        with pytest.raises(GardeArret, match=motif):
            fv.exiger_offre(o)


def test_echeance_d_arret_cumul_plus_un_quart_d_heure_a_la_coupure_et_artefacts():
    assert fv.echeance_arret_s(1000.0, 1, 1.3, 2) == int(1000 + (26.0 / 1.3 - 0.25) * 3600)
    assert fv.echeance_arret_s(0.0, 7, 1.0, 2) == int((15.0 - 0.25) * 3600)
    assert fv.echeance_arret_s(0.0, 1, 1.3, 3) == fv.echeance_arret_s(0.0, 1, 1.3, 2)    # tenues : sans objet
    with pytest.raises(GardeArret):
        fv.echeance_arret_s(0.0, 1, 1.4, 2)
    with pytest.raises(GardeArret):
        fv.echeance_arret_s(0.0, 8, 1.0, 2)
    with pytest.raises(GardeArret, match="devis non chiffré"):
        fv.echeance_arret_s(0.0, 7, 1.0, 3)


@pytest.mark.parametrize("membres", [2, 3])
def test_configuration_de_chaque_instance_passe_les_gardes_et_artefacts(membres):
    """Deux ou trois membres d'apprentissage : à trois, les instances 6 et 7 sont refusées tant que le devis ne les
    chiffre pas ; les instances 1 à 5 n'en dépendent pas."""
    for n in fv.PLAN_INSTANCES:
        if membres == 3 and n in fv.INSTANCES_D_APPRENTISSAGE:
            with pytest.raises(GardeArret, match="devis non chiffré"):
                fv.config_instance(n, RACINE_DEPOT, "GO-2026-11-22-01", 1.1, membres, "instance", False)
            continue
        for relance in (False, True):
            c = fv.config_instance(n, RACINE_DEPOT, "GO-2026-11-22-01", 1.1, membres, "famille", relance)
            assert c["familles"] == list(fv.familles_du_plan(n, relance)) and c["coupure_usd"] == fv.COUPURES_USD[n]
            assert c["membres_apprentissage"] == membres and c["relance"] is relance
    with pytest.raises(GardeArret):
        fv.config_instance(8, RACINE_DEPOT, "GO-2026-11-22-01", 1.1, membres, "instance", False)
    with pytest.raises(GardeArret):
        fv.config_instance(1, RACINE_DEPOT, "GO-2026-11-22-01", 2.0, membres, "instance", False)
    with pytest.raises(GardeArret):
        fv.config_instance(1, RACINE_DEPOT, "GO-2026-11-22-01", 1.1, None, "instance", False)


def test_registre_lu_dans_un_texte_comme_dans_un_fichier(tmp_path):
    code = en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T18:00:00Z", "commit " + "b" * 40 + " ; entropie 9", "")
    go = en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-22T19:00:00Z", "GO-2026-11-22-01", "")
    lignes = [_scellement(), code, go]
    assert fv.lire_code_et_accord(None, "\n".join(lignes) + "\n") == fv.lire_code_et_accord(_registre(tmp_path, lignes))


def test_branche_de_sortie_par_instance_et_relance():
    assert fv.branche_sortie(3, False) == "donnees/barreau5-familles-jumelles-v1-formation-instance-3"
    assert fv.branche_sortie(3, True) == "donnees/barreau5-familles-jumelles-v1-formation-instance-3-x1"
    with pytest.raises(GardeArret):
        fv.branche_sortie(8, False)


def test_graine_entiere_egale_a_celle_du_harnais_calculee_dans_un_processus_a_part():
    """La formule réécrite à neuf rend la même graine que `harnais.run_harnais_factice.graine_entiere`, calculée par ce
    module-là dans un autre processus (qui peut importer des modules de sonde, interdits dans la marche)."""
    g = {k: graines([k], entropie=5)[k] for k in ("x", "b5f/famille/T01/adaptateur", "b5f/modele-jouet")}
    code = ("import json, sys\nfrom controle_ia.harnais.run_harnais_factice import graine_entiere\n"
            "g = json.loads(sys.argv[1])\nprint(json.dumps({k: graine_entiere(v) for k, v in g.items()}))\n")
    p = subprocess.run([sys.executable, "-B", "-c", code, json.dumps(g)], capture_output=True, text=True, timeout=120,
                       env={**os.environ, "PYTHONPATH": str(RACINE_DEPOT / "src")})
    assert p.returncode == 0, p.stderr
    assert json.loads(p.stdout) == {k: fv.graine_entiere(v) for k, v in g.items()}
