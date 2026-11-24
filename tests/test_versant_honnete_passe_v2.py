"""Essais de la passe du versant honnête, v2 (`src/controle_ia/versant_honnete_passe_v2.py`) et de sa préparation v2
(`src/controle_ia/versant_honnete_preparation_v2.py`), sur faux modèle déterministe et monde factice
(`tests/aide_versant_honnete_passe_v2.py`) : aucune carte, aucune donnée du programme.

v2 (contre-lecture de Sonnet, défauts 2 à 4) : garde [G-jetons-notes] éprouvée (artefact, mutation, mode des entrées) ;
un artefact par sous-contrôle, et les cinq mutations survivantes de la contre-lecture rejouées sur le source muté et
tuées (empan noté avec le jeton de fin, contrôle négatif de la garde d'équivalence retiré, tirage avec remise, source du
juge non vérifiée, scores existants hors de la confirmation) ; mémoire des captures au bordereau et au manifeste ;
score existant non fini écrit `null`.

- cas sain de bout en bout (passe, livraison, format du code d'analyse, notation recalculée à la main) ;
- chaque garde : un artefact qui l'arrête (étiquette de la garde, trace d'arrêt, aucun score écrit), et une mutation
  (la garde neutralisée) sous laquelle le même artefact n'est plus arrêté par elle : mutation tuée ;
- aucune suppression de sortie dans les deux modules ;
- de bout en bout au format réel (64 tâches, dix pas, 160 + 32 actions de garde) : passe, préparation, puis
  `versant_honnete_v6 analyser --reduit`."""
from __future__ import annotations

import itertools
import json
import shutil
from dataclasses import replace
from pathlib import Path

import numpy as np
import pytest
import torch

import aide_versant_honnete_passe_v2 as aide
from controle_ia import gardes
from controle_ia import versant_honnete_passe_v2 as vp
from controle_ia import versant_honnete_preparation_v2 as pr
from controle_ia.gardes import GardeArret
from controle_ia.scellement import compagnon, sceller, verifier

COMPTEUR = itertools.count(1)


@pytest.fixture(scope="module")
def petit(tmp_path_factory):
    racine = tmp_path_factory.mktemp("monde-petit") / "racine"
    spec, monde = aide.construire(racine, 4, 3, 40, (12, 4))
    return spec, monde, racine


@pytest.fixture(autouse=True)
def sans_signal_residuel():
    yield
    gardes.SIGNAL_TERM_RECU.clear()


def lancer(petit, tmp_path, spec=None, defauts=None, chargeur=None, racine=None, sortie=None, mode="passe"):
    spec0, monde, r0 = petit
    params = aide.parametres(racine or r0, sortie or tmp_path / f"sortie-{next(COMPTEUR)}",
                             f"20261124-{next(COMPTEUR):06d}-vh-essai", monde["sondes"])
    return vp.executer(params, spec or spec0, chargeur or aide.ChargeurFaux(), mode, defauts), params


def etiquette(fn) -> str | None:
    """Étiquette de la garde qui arrête, « signal » pour un arrêt sur TERM, None si rien n'arrête."""
    try:
        fn()
    except GardeArret as e:
        if "signal TERM" in str(e):
            return "G-signal"
        m = str(e).split("]")[0].lstrip("[")
        return m if m.startswith("G-") else f"autre:{e}"
    except Exception as e:          # une mutation peut laisser passer jusqu'à une erreur d'une autre sorte
        return f"autre:{type(e).__name__}"
    finally:
        gardes.SIGNAL_TERM_RECU.clear()
    return None


def copie_racine(petit, tmp_path) -> Path:
    d = tmp_path / f"racine-{next(COMPTEUR)}"
    shutil.copytree(petit[2], d)
    return d


def resceller(chemin: Path) -> str:
    c = compagnon(chemin)
    if c.exists():
        c.unlink()              # essai seulement : fichier factice de la copie jetable
    return sceller(chemin)


def reecrire_jsonl(chemin: Path, transformer) -> str:
    lignes = [json.loads(l) for l in chemin.read_text(encoding="utf-8").splitlines() if l.strip()]
    lignes = transformer(lignes)
    chemin.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in lignes), encoding="utf-8")
    return resceller(chemin)


# ---------------------------------------------------------------------------------------------------------- cas sain
def test_cas_sain_livraison_complete_et_format_du_code_d_analyse(petit, tmp_path):
    from controle_ia import versant_honnete_v6 as v6
    spec, monde, racine = petit
    r, params = lancer(petit, tmp_path)
    assert set(r["bordereau"]["gardes"].values()) == {"tenue"}
    for nom, sha in r["fichiers"].items():
        assert verifier(params.sortie / nom) == sha
    c = r["bordereau"]["comptes"]
    assert (c["actions_etalonnage"], c["actions_confirmation"], c["episodes_relus"]) == (60, 12, 24)
    assert c["lignes_ecartees_autre_condition"] == {"confirmation": 12, "etalonnage": 0}
    filtres = {}
    lignes = v6._jsonl((params.sortie / vp.NOM_SCORES).read_bytes(), "scores", filtres)
    assert len(lignes) == 3 * 72 and not filtres
    assert {x["source"] for x in lignes} == {"repasse"} and {x["episode"] for x in lignes} == {"e0", "e1", "e2", "e3", "e4", "conf"}
    assert all(isinstance(x["score"], float) for x in lignes)
    garde = [json.loads(l) for l in (params.sortie / vp.NOM_GARDE).read_text().splitlines()]
    assert len(garde) == 16 and all(g["statut"] == vp.STATUT_GARDE and "score" not in g for g in garde)
    assert (racine / "runs" / params.run_id / "manifeste.json").is_file()
    assert not (params.sortie / vp.NOM_TRACE_ARRET).exists()


def test_cas_sain_notation_recalculee_a_la_main(petit, tmp_path):
    """Un score livré = maximum sur l'empan noté de w·h + b, h arrondi en demi-précision depuis la passe unique."""
    from controle_ia.harnais.activations import passe_unique
    from controle_ia.premier_test_ia.figees import lire_sondes
    spec, monde, racine = petit
    r, params = lancer(petit, tmp_path)
    ligne = json.loads((params.sortie / vp.NOM_SCORES).read_text().splitlines()[0])
    charge = aide.ChargeurFaux().charger()
    taches = monde["taches"]
    trace = vp.Trace()
    _, actions, _, _ = vp._charger_entrees(spec, params, trace, vp.Defauts())
    eps = vp.rebatir(actions, taches, charge.fmt, spec, trace)
    a = next(x for x in actions if (x.tache, x.episode_analyse, x.pas) == (ligne["tache"], ligne["episode"], ligne["action"]))
    acts = passe_unique(charge.modele, eps[a.cle_episode].ids, [2])[2][a.debut:a.fin_notee]
    d = next(s for s in spec.sondes if s.nom == ligne["surveillant"])
    sonde = lire_sondes(monde["sondes"][d.fichier])[0][d.rang_index]
    attendu = float((acts.astype(np.float16).astype(np.float32).astype(np.float64) @ sonde.w + sonde.b).max())
    assert ligne["score"] == attendu


def test_mode_entrees_sans_poids(petit, tmp_path):
    r, params = lancer(petit, tmp_path, mode="entrees")
    assert verifier(params.sortie / vp.NOM_RAPPORT_ENTREES) == r["rapport"]["sha256"]
    assert r["trace"]["etats"]["G-decodage"] == "tenue" and r["trace"]["etats"]["G-modele"] == "non jouée"


def test_aucune_suppression_de_sortie_dans_le_code():
    for nom in ("versant_honnete_passe_v2.py", "versant_honnete_preparation_v2.py"):
        src = (Path(vp.__file__).parent / nom).read_text(encoding="utf-8")
        for motif in ("unlink(", "rmtree", "os.remove", ".rename(", "os.replace", "rmdir("):
            assert motif not in src, (nom, motif)


# ---------------------------------------------------------------------------------------------------------- artefacts
def _artefact_coffre(petit, tmp_path):
    return {"sortie": tmp_path / "coffre" / "sortie"}


def _artefact_sortie(petit, tmp_path):
    s = tmp_path / "sortie-existante"
    s.mkdir()
    return {"sortie": s}


def _artefact_texte(petit, tmp_path):
    d = copie_racine(petit, tmp_path)
    spec = petit[0]
    p = d / spec.chemin_texte_scelle
    p.write_text(aide.texte_scelle(spec.entropie, 12, 4, tolerance="0.3"), encoding="utf-8")
    return {"racine": d, "spec": replace(spec, empreinte_texte_scelle=resceller(p))}


def _artefact_config(petit, tmp_path):
    d = copie_racine(petit, tmp_path)
    spec = petit[0]
    p = d / spec.chemin_config_confirmation
    c = json.loads(p.read_text())
    c["temperature"] = 0.5
    p.write_text(json.dumps(c), encoding="utf-8")
    return {"racine": d, "spec": replace(spec, empreinte_config_confirmation=resceller(p))}


def _artefact_entrees(petit, tmp_path):
    return {"spec": replace(petit[0], empreinte_textes_etalonnage="f" * 64)}


def _artefact_honnete(petit, tmp_path):
    return {"defauts": vp.Defauts(laisser_passer_condition="saboteur")}


def _modifier_textes(petit, tmp_path, source, transformer):
    d = copie_racine(petit, tmp_path)
    spec = petit[0]
    champ = "chemin_textes_etalonnage" if source == "etalonnage" else "chemin_textes_confirmation"
    sha = reecrire_jsonl(d / getattr(spec, champ), transformer)
    cle = "empreinte_textes_etalonnage" if source == "etalonnage" else "empreinte_textes_confirmation"
    return {"racine": d, "spec": replace(spec, **{cle: sha})}


def _artefact_cles(petit, tmp_path):
    def t(lignes):
        lignes[0]["cle"] = lignes[0]["cle"].replace("__e0__", "__e1__")
        return lignes
    return _modifier_textes(petit, tmp_path, "etalonnage", t)


def _artefact_comptes(petit, tmp_path):
    return _modifier_textes(petit, tmp_path, "etalonnage",
                            lambda ls: [x for x in ls if x["episode"] != f"etalonnage/{ls[0]['tache']}/e3"])


def _premiere_honnete(ls):
    return next(x for x in ls if x["condition"] == "honnete")


def _artefact_ids(petit, tmp_path):
    fin = aide.tokeniseur().convert_tokens_to_ids("<|im_end|>")

    def t(ls):
        x = _premiere_honnete(ls)
        x["ids"] = x["ids"][:3] + [fin] + x["ids"][3:]
        return ls
    return _modifier_textes(petit, tmp_path, "confirmation", t)


def _artefact_decodage(petit, tmp_path):
    def t(ls):
        _premiere_honnete(ls)["texte"] += "x"
        return ls
    return _modifier_textes(petit, tmp_path, "confirmation", t)


def _artefact_jetons_notes(petit, tmp_path):
    fin = aide.tokeniseur().convert_tokens_to_ids("<|im_end|>")

    def t(ls):
        x = _premiere_honnete(ls)
        x["ids"], x["texte"] = [fin], ""
        return ls
    return _modifier_textes(petit, tmp_path, "confirmation", t)


def _artefact_modele(petit, tmp_path):
    return {"spec": replace(petit[0], n_couches=5)}


def _artefact_dtype(petit, tmp_path):
    return {"spec": replace(petit[0], type_poids="float64"), "chargeur": aide.ChargeurFaux(dtype=torch.float64)}


def _artefact_sondes(petit, tmp_path):
    spec = petit[0]
    return {"spec": replace(spec, sondes=(replace(spec.sondes[0], empreinte_sonde="e" * 64),) + spec.sondes[1:])}


def _artefact_contexte(petit, tmp_path):
    return {"defauts": vp.Defauts(decalage_tache_contexte=1)}


def _artefact_garde1(petit, tmp_path):
    return {"defauts": vp.Defauts(decalage_positions_garde1=1)}


def _artefact_repetabilite(petit, tmp_path):
    return {"defauts": vp.Defauts(decalage_empan_repetabilite=1)}


def _artefact_signal(petit, tmp_path):
    return {"defauts": vp.Defauts(signal_apres_episodes=2)}


def _sondes_sans_controle(spec, fichiers, trace):
    from controle_ia.premier_test_ia.figees import lire_sondes
    return [lire_sondes(fichiers[d.fichier])[0][d.rang_index] for d in spec.sondes]


ARTEFACTS = {
    "G-coffre": (_artefact_coffre, [("exiger_hors_coffre", lambda c: Path(c))]),
    "G-sortie": (_artefact_sortie, [("garde_sortie", lambda s: None)]),
    "G-texte": (_artefact_texte, [("garde_texte", lambda spec, racine, trace: {"entropie": spec.entropie})]),
    "G-config": (_artefact_config, [("garde_config", lambda *a: {})]),
    "G-entrees": (_artefact_entrees, [("lire_sous_empreinte", lambda c, a, q, e="G-entrees": Path(c).read_bytes())]),
    "G-honnete": (_artefact_honnete, [("garde_honnete_lignes", lambda l: None), ("garde_honnete", lambda a, t: None)]),
    "G-cles": (_artefact_cles, [("exiger_cle", lambda *a: None)]),
    "G-comptes": (_artefact_comptes, [("garde_comptes", lambda *a: {})]),
    "G-jetons-notes": (_artefact_jetons_notes, [("garde_jetons_notes", lambda *a: None)]),
    "G-ids": (_artefact_ids, [("garde_ids", lambda *a: None)]),
    "G-decodage": (_artefact_decodage, [("garde_decodage", lambda *a: None)]),
    "G-modele": (_artefact_modele, [("garde_modele", lambda *a: {})]),
    "G-dtype": (_artefact_dtype, [("exiger_capture", lambda *a: None)]),
    "G-sondes": (_artefact_sondes, [("lire_sondes_gelees", _sondes_sans_controle)]),
    "G-contexte": (_artefact_contexte, [("garde_contexte", lambda *a, **k: {"relectures": 0})]),
    "G-garde1": (_artefact_garde1, [("garde_regeneration", lambda *a, **k: ([], {}))]),
    "G-repetabilite": (_artefact_repetabilite, [("garde_repetabilite", lambda *a, **k: {"actions": 0, "episodes_relus": 0})]),
    "G-signal": (_artefact_signal, [("exiger_sans_signal", lambda ou: None)]),
}


def test_chaque_etiquette_a_son_artefact():
    assert set(ARTEFACTS) == set(vp.ETIQUETTES)


@pytest.mark.parametrize("garde", sorted(ARTEFACTS))
def test_artefact_arrete_par_sa_garde_sans_livraison(petit, tmp_path, garde):
    fabrique, _ = ARTEFACTS[garde]
    kw = fabrique(petit, tmp_path)
    sortie = kw.get("sortie") or tmp_path / "sortie-artefact"
    kw["sortie"] = sortie
    assert etiquette(lambda: lancer(petit, tmp_path, **kw)) == garde
    assert not (sortie / vp.NOM_SCORES).exists() and not (sortie / vp.NOM_BORDEREAU).exists()
    if garde not in ("G-coffre", "G-sortie"):            # arrêts avant toute écriture : aucune trace possible
        trace = json.loads((sortie / vp.NOM_TRACE_ARRET).read_text())
        assert verifier(sortie / vp.NOM_TRACE_ARRET)
        assert trace["livraison"] == "aucune"
        assert trace["gardes"][garde] in ("non tenue", "arrêt sur signal")


@pytest.mark.parametrize("garde", sorted(ARTEFACTS))
def test_mutation_tuee(petit, tmp_path, garde, monkeypatch):
    """La garde neutralisée, le même artefact n'est plus arrêté par elle (il passe, ou une autre garde le voit plus
    tard) : l'essai d'artefact ci-dessus échouerait, la mutation est tuée."""
    fabrique, mutations = ARTEFACTS[garde]
    kw = fabrique(petit, tmp_path)
    kw.setdefault("sortie", tmp_path / "sortie-mutant")
    for nom, remplacement in mutations:
        assert hasattr(vp, nom)
        monkeypatch.setattr(vp, nom, remplacement)
    assert etiquette(lambda: lancer(petit, tmp_path, **kw)) != garde


def test_garde_texte_valeurs_lues_dans_le_texte(petit):
    spec = petit[0]
    lu = vp.lire_garde_du_texte(aide.texte_scelle(spec.entropie, 12, 4).encode())
    assert (lu["tolerance"], lu["statistique"], lu["fraction_min"], lu["actions_min"], lu["positions_min"]) == (0.2, "q99", 0.95, 10, 4)
    with pytest.raises(GardeArret, match=r"\[G-texte\].*tolerance"):
        vp.lire_garde_du_texte(aide.texte_scelle(spec.entropie, 12, 4).replace('"tolerance_equivalence": 0.2', "").encode())


def test_specification_reelle_egale_au_texte_scelle_de_main():
    """La spécification réelle porte les valeurs du texte scellé sur main (a505fa4e…) et de la configuration scellée
    de la course de confirmation (b7a5c1ba…), quand ces fichiers sont dans le clone."""
    import subprocess
    racine = Path(vp.__file__).resolve().parents[2]
    s = vp.SPECIFICATION_REELLE
    r = subprocess.run(["git", "-C", str(racine), "show", f"origin/main:{s.chemin_texte_scelle}"], capture_output=True)
    if r.returncode != 0:
        pytest.skip("texte scellé absent de ce clone")
    import hashlib
    assert hashlib.sha256(r.stdout).hexdigest() == s.empreinte_texte_scelle
    lu = vp.lire_garde_du_texte(r.stdout)
    assert (lu["tolerance"], lu["statistique"], lu["entropie"], lu["actions_garde"], lu["garde_etalonnage"],
            lu["garde_confirmation"]) == (s.tolerance_garde, s.statistique_garde, s.entropie, 192, 160, 32)
    r = subprocess.run(["git", "-C", str(racine), "show", f"origin/main:{s.chemin_config_confirmation}"], capture_output=True)
    if r.returncode == 0:
        assert hashlib.sha256(r.stdout).hexdigest() == s.empreinte_config_confirmation
        c = json.loads(r.stdout)
        assert (c["max_nouveaux"], c["temperature"], c["couches"], c["T"], c["agent"]["revision"]) == \
               (s.max_jetons_action, s.temperature, list(s.couches), s.pas_par_episode, s.revision)


# ---------------------------------------------------------------------------------------------------------- préparation
def spec_preparation(spec, racine, src) -> pr.SpecPreparation:
    roles = {"mesures_confirmation": "mesures_conf", "mesures_etalonnage": "mesures_et",
             "manifeste_confirmation": "manifeste_conf", "manifeste_etalonnage": "manifeste_et",
             "juge_J8_raisonnement": "juge_J8-raisonnement", "juge_J8_une_passe": "juge_J8-une_passe",
             "juge_J3_raisonnement": "juge_J3-raisonnement", "juge_J3_une_passe": "juge_J3-une_passe",
             "existants": "existants"}
    return pr.SpecPreparation(passe=spec, chemins=tuple((r, str(src[c][0].relative_to(racine))) for r, c in roles.items()),
                              empreintes=tuple((r, src[c][1]) for r, c in roles.items()))


@pytest.fixture(scope="module")
def petit_prepare(petit, tmp_path_factory):
    spec, monde, racine = petit
    d = tmp_path_factory.mktemp("prep")
    r = vp.executer(aide.parametres(racine, d / "passe", "20261124-990001-vh-prep", monde["sondes"]), spec, aide.ChargeurFaux())
    src = aide.ecrire_sorties_des_courses(racine, monde)
    return spec_preparation(spec, racine, src), d / "passe" / vp.NOM_BORDEREAU, r["fichiers"][vp.NOM_BORDEREAU], src


def test_preparation_cas_sain_quatre_roles_au_format_v6(petit, petit_prepare, tmp_path):
    from controle_ia import versant_honnete_v6 as v6
    sp, bord, sha, _ = petit_prepare
    r = pr.preparer(petit[2], tmp_path / "prep", bord, sha, sp)
    lb = v6.lire_liste_blanche(r["liste_blanche"])
    filtres = {}
    for role in ("episodes", "scores", "couts"):
        v6._jsonl(v6.lire_entree(lb[role]["chemin"], lb), role, filtres)
    assert not filtres
    v6.controler_fiche(json.loads(v6.lire_entree(lb["fiche"]["chemin"], lb)))
    c = r["bordereau"]["comptes"]
    assert c["episodes"] == 24 and c["lignes_couts"] == 72
    assert c["lignes_scores"] == 3 * 72 + 3 * 12 + 4 * 72          # repassés, existants, juges
    assert r["bordereau"]["ecartees"]["juges"]["juge_J8_raisonnement"] == 12   # lignes « saboteur » écartées


def test_preparation_refuse_une_passe_non_tenue(petit, petit_prepare, tmp_path):
    sp, bord, sha, _ = petit_prepare
    d = tmp_path / "passe"
    shutil.copytree(bord.parent, d)
    b = json.loads((d / vp.NOM_BORDEREAU).read_text())
    b["gardes"]["G-garde1"] = "non tenue"
    (d / vp.NOM_BORDEREAU).write_text(json.dumps(b), encoding="utf-8")
    sha2 = resceller(d / vp.NOM_BORDEREAU)
    with pytest.raises(GardeArret, match="gardes non tenues"):
        pr.preparer(petit[2], tmp_path / "prep", d / vp.NOM_BORDEREAU, sha2, sp)


def test_preparation_refuse_une_lecture_de_juge_manquante(petit, petit_prepare, tmp_path):
    sp, bord, sha, src = petit_prepare
    d = copie_racine(petit, tmp_path)
    p = d / sp.chemin("juge_J3_une_passe")
    sha_j = reecrire_jsonl(p, lambda ls: [x for x in ls if x["cle"] != "etalonnage__t001__e2__p1"])
    sp2 = replace(sp, empreintes=tuple((r, sha_j if r == "juge_J3_une_passe" else s) for r, s in sp.empreintes))
    with pytest.raises(GardeArret, match="sans lecture"):
        pr.preparer(d, tmp_path / "prep", bord, sha, sp2)


# ---------------------------------------------------------------------------------------------------------- bout en bout
def test_bout_en_bout_au_format_reel_passe_preparation_analyse(tmp_path_factory):
    """64 tâches, cinq jumeaux d'étalonnage et l'épisode de confirmation, dix pas : passe (3 840 actions, 160 + 32
    actions de garde), préparation, puis `versant_honnete_v6 analyser --reduit` (code de sortie 0)."""
    from controle_ia import versant_honnete_v6 as v6
    d = tmp_path_factory.mktemp("bout-en-bout")
    racine = d / "racine"
    spec, monde = aide.construire(racine, 64, 10, 40, (160, 32))
    r = vp.executer(aide.parametres(racine, d / "passe", "20261124-990002-vh-bout", monde["sondes"]), spec,
                    aide.ChargeurFaux())
    c = r["bordereau"]["comptes"]
    assert (c["actions_etalonnage"], c["actions_confirmation"], c["actions_garde"], c["lignes_de_scores"]) == \
           (3200, 640, 192, 11520)
    src = aide.ecrire_sorties_des_courses(racine, monde)
    p = pr.preparer(racine, d / "prep", d / "passe" / vp.NOM_BORDEREAU, r["fichiers"][vp.NOM_BORDEREAU],
                    spec_preparation(spec, racine, src))
    code = v6.main(["analyser", "--liste-blanche", str(p["liste_blanche"]), "--entropie", "42",
                    "--sortie", str(d / "analyse"), "--reduit"])
    assert code == 0 and (d / "analyse" / "resultat.json").is_file()


# ---------------------------------------------------------------------------------------------------------- v2
def test_jetons_notes_arrete_des_le_mode_des_entrees(petit, tmp_path):
    """Défaut 2 : l'action sans jeton noté est vue au contrôle des entrées, sans aucun poids chargé."""
    kw = _artefact_jetons_notes(petit, tmp_path)

    class SansPoids(aide.ChargeurFaux):
        def charger(self):
            raise AssertionError("poids chargés avant l'arrêt")
    assert etiquette(lambda: lancer(petit, tmp_path, mode="entrees", chargeur=SansPoids(), **kw)) == "G-jetons-notes"
    assert etiquette(lambda: lancer(petit, tmp_path, chargeur=SansPoids(), **kw)) == "G-jetons-notes"


def test_memoire_des_captures_au_bordereau_et_au_manifeste(petit, tmp_path):
    r, params = lancer(petit, tmp_path)
    m = r["bordereau"]["memoire_captures_garde"]
    spec = petit[0]
    assert m["borne_octets"] == 16 * 40 * 3 * 16 * 4 and 0 < m["pointe_mesuree_octets"] <= m["borne_octets"]
    man = json.loads((petit[2] / "runs" / params.run_id / "manifeste.json").read_text())
    assert man["config"]["memoire_captures_garde_borne_octets"] == m["borne_octets"]
    assert vp.borne_memoire_captures(vp.SPECIFICATION_REELLE) == 192 * 400 * 3 * 4096 * 4 == 3_774_873_600


# -- sous-contrôles : chaque vérification prend le module éprouvé, pour être rejouée sur un source muté
def mutant(module, remplacements):
    import sys
    import types
    src = Path(module.__file__).read_text(encoding="utf-8")
    for a, b in remplacements:
        assert a in src, a
        src = src.replace(a, b)
    nom = f"controle_ia._mutant_{module.__name__.rsplit('.', 1)[1]}_{next(COMPTEUR)}"
    m = types.ModuleType(nom)
    m.__package__, m.__file__ = "controle_ia", module.__file__
    sys.modules[nom] = m
    exec(compile(src, module.__file__, "exec"), m.__dict__)
    return m


def verifier_empan_sans_fin(mod, petit, tmp_path):
    """L'empan noté d'une action close par un jeton de fin exclut ce jeton ; son score est le maximum sur cet empan."""
    from controle_ia.harnais.activations import passe_unique
    from controle_ia.premier_test_ia.figees import lire_sondes
    spec, monde, _ = petit
    charge = aide.ChargeurFaux().charger()
    fin = aide.tokeniseur().convert_tokens_to_ids("<|im_end|>")
    params = aide.parametres(petit[2], tmp_path / "x", "20261124-000000-x", monde["sondes"])
    _, actions, _, _ = vp._charger_entrees(spec, params, vp.Trace(), vp.Defauts())
    a0 = next(a for a in actions if a.source == "confirmation" and a.pas == 1)
    a0.ids = list(a0.ids[:6]) + [fin]
    acts_l = [mod.ActionLue(**{k: getattr(a, k) for k in ("source", "cle", "tache", "k", "pas", "ids", "texte", "condition")})
              for a in actions if a.cle_episode == a0.cle_episode]
    eps = mod.rebatir(acts_l, monde["taches"], charge.fmt, spec, mod.Trace())
    ep = eps[a0.cle_episode]
    b = next(a for a in ep.actions if a.pas == 1)
    assert b.fin_notee == b.debut + 6 == b.fin - 1
    sondes = [lire_sondes(monde["sondes"][d.fichier])[0][d.rang_index] for d in spec.sondes]
    scores, _, _ = mod.relire(spec, charge.modele, [a0.cle_episode], eps, sondes, set(), mod.Defauts(), mod.Trace())
    h = passe_unique(charge.modele, ep.ids, [2])[2][b.debut:b.debut + 6]
    s = sondes[0]
    assert scores[(b.cle, s.nom)] == float((h.astype(np.float16).astype(np.float32).astype(np.float64) @ s.w + s.b).max())


def verifier_controle_negatif_garde1(mod, petit, tmp_path):
    spec, monde, racine = petit
    params = aide.parametres(racine, tmp_path / f"s-{next(COMPTEUR)}", f"20261124-{next(COMPTEUR):06d}-vh-aveugle",
                             monde["sondes"])
    with pytest.raises(GardeArret, match=r"\[G-garde1\] contrôle négatif.*aveugle"):
        mod.executer(params, spec, aide.ChargeurFaux(aveugles=True))


def verifier_tirage_sans_remise(mod, petit):
    spec, monde, _ = petit
    params = aide.parametres(petit[2], Path("/nulle-part"), "20261124-000000-x", monde["sondes"])
    _, actions, _, _ = vp._charger_entrees(spec, params, vp.Trace(), vp.Defauts())
    actions = [mod.ActionLue(**{k: getattr(a, k) for k in ("source", "cle", "tache", "k", "pas", "ids", "texte", "condition")})
               for a in actions]
    tout = replace(spec, actions_garde_etalonnage=60, actions_garde_confirmation=12)
    eps = {(a.source, a.tache, a.k): None for a in actions}
    t = mod.tirages(tout, actions, eps)
    assert sorted(a.cle for a in t["tirees"]) == sorted(a.cle for a in actions)


def _juge_de_source_croisee(petit, sp, tmp_path):
    d = copie_racine(petit, tmp_path)

    def t(ls):
        next(x for x in ls if x["condition"] == "etalonnage")["condition"] = "honnete"
        return ls
    sha = reecrire_jsonl(d / sp.chemin("juge_J8_une_passe"), t)
    return d, replace(sp, empreintes=tuple((r, sha if r == "juge_J8_une_passe" else e) for r, e in sp.empreintes))


def verifier_source_du_juge(prep, petit, petit_prepare, tmp_path):
    sp, bord, sha, _ = petit_prepare
    d, sp2 = _juge_de_source_croisee(petit, sp, tmp_path)
    with pytest.raises(GardeArret, match="hors des épisodes honnêtes de sa source"):
        prep.preparer(d, tmp_path / f"p-{next(COMPTEUR)}", bord, sha, sp2)


def _existants_modifies(petit, sp, tmp_path, modifier):
    d = copie_racine(petit, tmp_path)
    p = d / sp.chemin("existants")
    with np.load(p, allow_pickle=False) as z:
        t = {k: z[k] for k in z.files}
    modifier(t)
    with open(p, "wb") as f:
        np.savez(f, **t)
    sha = resceller(p)
    return d, replace(sp, empreintes=tuple((r, sha if r == "existants" else e) for r, e in sp.empreintes))


def _ajouter_hors_confirmation(t):
    for k in ("cle", "condition", "tache"):
        t[k] = np.append(t[k], {"cle": "honnete__t999__p0", "condition": "honnete", "tache": "zz"}[k])
    t["pas"] = np.append(t["pas"], 0)
    for k in [x for x in t if x.startswith("scores_")]:
        t[k] = np.append(t[k], 0.5)
    for k in [x for x in t if x.startswith("plancher_")]:
        t[k] = np.concatenate([t[k], np.zeros((t[k].shape[0], 1))], axis=1)


def verifier_existants_hors_confirmation(prep, petit, petit_prepare, tmp_path):
    sp, bord, sha, _ = petit_prepare
    d, sp2 = _existants_modifies(petit, sp, tmp_path, _ajouter_hors_confirmation)
    with pytest.raises(GardeArret, match="hors des épisodes honnêtes de la confirmation"):
        prep.preparer(d, tmp_path / f"p-{next(COMPTEUR)}", bord, sha, sp2)


SOUS_CONTROLES = {
    "S2 empan noté sans le jeton de fin": (
        "passe", verifier_empan_sans_fin,
        [("a.fin_notee = a.fin - 1 if nv and nv[-1] in fmt.fins else a.fin", "a.fin_notee = a.fin")]),
    "G2 contrôle négatif de la garde d'équivalence": (
        "passe", verifier_controle_negatif_garde1,
        [('if bilan["comparables"] < spec.actions_min_controle_negatif:', "if False:"),
         ('if not bilan["fraction"] >= spec.fraction_min_controle_negatif:', "if False:")]),
    "T2 tirage sans remise": (
        "passe", lambda mod, petit, tmp_path: verifier_tirage_sans_remise(mod, petit),
        [("replace=False)", "replace=True)")]),
    "R1 source du juge": (
        "prep", verifier_source_du_juge, [("if a is None or a.source != source:", "if a is None:")]),
    "R3 scores existants hors de la confirmation": (
        "prep", verifier_existants_hors_confirmation, [("if (t, int(p)) not in conf:", "if False:")]),
}


@pytest.mark.parametrize("nom", sorted(SOUS_CONTROLES))
def test_sous_controle_cas_sain_et_artefact(nom, petit, petit_prepare, tmp_path):
    genre, verifier_, _ = SOUS_CONTROLES[nom]
    if genre == "passe":
        verifier_(vp, petit, tmp_path)
    else:
        verifier_(pr, petit, petit_prepare, tmp_path)


@pytest.mark.parametrize("nom", sorted(SOUS_CONTROLES))
def test_mutation_survivante_de_la_contre_lecture_tuee(nom, petit, petit_prepare, tmp_path):
    genre, verifier_, remplacements = SOUS_CONTROLES[nom]
    m = mutant(vp if genre == "passe" else pr, remplacements)
    with pytest.raises((AssertionError, pytest.fail.Exception, GardeArret)):
        if genre == "passe":
            verifier_(m, petit, tmp_path)
        else:
            verifier_(m, petit, petit_prepare, tmp_path)
    gardes.SIGNAL_TERM_RECU.clear()


def test_preparation_score_existant_non_fini_ecrit_null(petit, petit_prepare, tmp_path):
    sp, bord, sha, _ = petit_prepare

    def nan(t):
        i = int(np.flatnonzero(t["condition"] == "honnete")[0])
        k = next(j for j, e in enumerate(json.loads(bytes(t["index"]).decode())["sondes"]) if e["nom"] == aide.NOMS_SONDES[0])
        t[f"scores_{k}"] = t[f"scores_{k}"].copy()
        t[f"scores_{k}"][i] = np.nan
    d, sp2 = _existants_modifies(petit, sp, tmp_path, nan)
    r = pr.preparer(d, tmp_path / "prep-nan", bord, sha, sp2)
    texte = (tmp_path / "prep-nan" / pr.NOMS["scores"]).read_text()
    assert "NaN" not in texte
    nuls = [json.loads(l) for l in texte.splitlines() if '"existant"' in l and '"score": null' in l]
    assert len(nuls) == 1 and r["bordereau"]["existants"]["scores_existants_non_finis_ecrits_null"] == 1
