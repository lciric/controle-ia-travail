"""Essais de l'outil du lecteur et du programme de classement — course « conception propre » — v2.

v2 : essais de la v1 adaptés (passages d'au moins 20 caractères, fiches lues seulement dans la copie scellée d'un run
factice, avec son manifeste de fin, sous une racine factice où les pièces épinglées sont recopiées), plus les essais des
corrections M1, M2, M3, des neuf mutations survivantes de la contre-lecture (R-2627) et de la variante détachée de L5.

Hors de `tests/` (R-2614 : aucun fichier sous `src/` ou `tests/` avant S7). Lancement, depuis la racine du dépôt :

    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -m pytest -q -p no:cacheprovider \
        docs/notes/organisme-conception-propre-v1/lecture-classement-v2/essais_lecture_classement_v2.py

Fiches factices seulement ; lecteur simulé (aucun modèle, aucune clé). `LC_MODULES` désigne le dossier des deux
programmes essayés (banc de mutations) ; par défaut, celui de ce fichier. Les pièces épinglées sont lues dans le dépôt,
jamais modifiées.
"""
from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
RACINE = ICI.parents[3]
MODS = Path(os.environ.get("LC_MODULES", str(ICI)))
CLONE = Path("/home/user/lciric/ideation-organism/orchestrator/pole/ideation_v2.py")


def _charger(nom, fichier):
    spec = importlib.util.spec_from_file_location(nom, MODS / fichier)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


K = _charger("classer_cp_v2_essai", "classer_conception_propre_v2.py")
O = K.O
LEVIER_JUGE = "levier:juge"


# --- fiches factices ---------------------------------------------------------------------------------------------------

def fiche(n, auteur, passe, indice, levier, nature="modification", cout="processeur", questions=None):
    f = {
        "nom": f"Idée factice {n} : réglage numéro {n}",
        "type": "approche",
        "enonce": f"Énoncé factice {n} : on change la pièce {n} de l'organisme d'une façon décrite ici, sans rien d'autre « {n} ».",
        "loi_predictive": {"espace_instances": f"famille factice {n}, trente graines",
                           "prediction": f"la couverture augmente de {n} composantes à coût égal contre le témoin {n}",
                           "signe": "+", "metrique": f"composantes couvertes lues par l'oracle, fiche {n}"},
        "perte_traduction": f"perte factice {n}",
        "questions_servies": questions if questions is not None else [levier, "nouvelle"],
        "avantage": {"source": "organisme", "texte": f"avantage factice {n}", "incopiable_parce_que": f"raison {n}"},
        "originalite": {"niveau": "inedite", "texte": f"originalité factice {n}"},
        "demande_organisme": {"nature": nature, "texte": f"changer le paramètre {n} du juge en la valeur {n}"},
        "cout": {"nature": cout, "ordre_de_grandeur": f"coût factice {n}"},
        "piege": f"piège factice {n} : témoin à coût égal",
        "cosmetique_si": f"cosmétique si le témoin {n} fait aussi bien",
        "anteriorite": [{"reference": f"référence factice {n}", "statut": "SUPPOSE"}],
    }
    f["auteur"], f["passe"], f["identifiant_auteur"] = auteur, passe, f"{auteur}-p{passe}-{indice:02d}"
    f["empreinte"] = hashlib.sha256(n.encode()).hexdigest()
    return f


# plan : nom → (auteur, levier, nature, coût, valeurs voulues des deux lectures)
TOUT1 = {"R1": 1, "R2": 1, "R3": 1, "R4": 1, "R5": 1, "R6": 1, "R7": 1, "N": "aucune"}
PLAN = {
    "A1": ("propa", "levier:cout", "ajout", "processeur", {}),
    "A2": ("propb", "levier:proposeurs", "modification", "depense", {}),
    "A3": ("propc", "levier:composition", "modification", "processeur", {"R1": 0}),
    "A4": ("propa", "levier:cout", "modification", "processeur", {"R7": 0}),
    "A5": ("propb", "levier:cout", "modification", "processeur", {"N": "C8"}),
    "A6": ("propc", "levier:proposeurs", "ajout", "processeur", {"R2": 0}),
    "A7": ("propa", LEVIER_JUGE, "modification", "depense", {}),
    "A8": ("propb", "levier:cout", "ajout", "depense", {"R6": 0}),
}
HORS = {"H1": ["levier:cout", "levier:juge", "nouvelle"], "H2": None, "H3": ["QO1", "nouvelle"]}


def fiches_factices(plan=PLAN, hors=True, renommer=None):
    fs = []
    for k, (n, (aut, lev, nat, cout, _)) in enumerate(plan.items(), 1):
        aut = renommer.get(aut, aut) if renommer else aut
        fs.append(fiche(n, aut, 1 + k % 2, k, lev, nat, cout))
    if hors:
        fs.append(fiche("H1", "propa", 2, 20, "levier:cout", questions=HORS["H1"]))
        fs.append(fiche("H2", "propb", 2, 21, "levier:cout", nature="rien"))
        fs.append(fiche("H3", "propc", 2, 22, "levier:cout", questions=HORS["H3"]))
    return fs


RUN = "20261114-010203-course-ideation-conception-propre-v1-g1"


def racine_de(tmp):
    """Racine factice : pièces épinglées recopiées du dépôt (jamais modifiées dans le dépôt)."""
    rac = Path(tmp) / "racine"
    if not rac.exists():
        for nom, (rel, _) in O.PIECES.items():
            (rac / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(RACINE / rel, rac / rel)
    return rac


def ecrire_fiches(dossier, fs, fin=None, nom=None, run=RUN, contenu=None):
    """Copie scellée des fiches dans le dossier d'un run factice, et manifeste de fin scellé (forme du lanceur)."""
    d_run = racine_de(dossier) / "runs" / "course-ideation-conception-propre-v1" / run
    (d_run / "copies").mkdir(parents=True, exist_ok=True)
    p = d_run / "copies" / (nom or "sortie--fiches-validees.json")
    texte = contenu if contenu is not None else json.dumps(fs, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    p.write_text(texte, encoding="utf-8")
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    Path(str(p) + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    m = d_run / "manifeste-lanceur-fin.json"
    if not m.exists():
        bilan = {"code": 0, "issue": "fin propre",
                 "pour_l_attestation": {"fiches_validees_sha256": h}} if fin is None else fin(h)
        O.ecrire_scelle(m, json.dumps(bilan, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return p, h


def ecrire_attestation(dossier, sha, **change):
    a = {"lecteur": "mère (essai)", "lu_le": "2026-11-13T23:50Z", "fiches_validees_sha256": sha,
         "aucune_recette_aucun_secret": True, "envoi_au_lecteur_externe_permis": True}
    a.update(change)
    p = Path(dossier) / "attestation-lecture-g1-v1.json"
    O.ecrire_scelle(p, json.dumps(a, ensure_ascii=False))
    return p


def preparer(tmp, fs=None):
    fs = fiches_factices() if fs is None else fs
    pf, h = ecrire_fiches(tmp, fs)
    pa = ecrire_attestation(tmp, h)
    env = racine_de(tmp) / "envois"
    man = O.preparer(pf, pa, env, racine_de(tmp))
    return env, man


# --- lecteur simulé ------------------------------------------------------------------------------------------------------

CHAMP_PREUVE = {"R1": ("loi_predictive", "prediction"), "R2": ("loi_predictive", "metrique"), "R3": ("piege",),
                "R5": ("demande_organisme", "texte"), "R6": ("cosmetique_si",), "R7": ("enonce",)}


def valeurs_attendues(p):
    """Valeurs que le lecteur simulé « sain » rend pour une fiche de la pile."""
    if p["origine"] == "reelle":
        nom = p["vue"]["nom"].split()[2]
        return {**TOUT1, **PLAN[nom][4]}
    if p["famille"] == "hasard":
        return {**TOUT1, "R7": 0}
    return {c: (0 if x is None else x) for c, x in p["attendu"].items()}


def passage(vue, c):
    if c == "R4":  # levier:juge : une phrase de la fiche (au moins 20 caractères), jamais l'étiquette seule
        return vue["demande_organisme"]["texte"][:150]
    o = vue
    for k in CHAMP_PREUVE[c]:
        o = o[k]
    return o[:150]


def entree_lue(p, vals, cat, alterer=()):
    e = {"etiquette": None}
    for c in O.CRITERES:
        if vals[c] == 1:
            pas = passage(p["vue"], c)
            if c in alterer:
                pas = pas[:-3] + "zzz"
            e[c] = {"valeur": 1, "passage": pas}
        else:
            e[c] = {"valeur": 0, "motif": "manque"}
    if vals["N"] == "aucune":
        e["N"] = {"valeur": "aucune"}
    else:
        pc = O.sans_gras(cat[vals["N"]][2])[:60]
        if "Nc" in alterer:
            pc = "passage qui n'est pas dans le catalogue"
        e["N"] = {"valeur": vals["N"], "passage_fiche": p["vue"]["enonce"][:60], "passage_catalogue": pc}
    return e


def lire(env, modif=None, contenu_lot=None, modele="kimi-k3.1-pro", sceller=True):
    """Écrit les réponses de deux lectures. `modif(L, id, p, vals)` → (vals, alterer) ; `contenu_lot(L, k, texte)` → texte."""
    pile = json.loads((env / "pile-interne-v2.json").read_text(encoding="utf-8"))
    cle = json.loads((env / "cle-lectures-v2.json").read_text(encoding="utf-8"))
    cat = O.entrees_catalogue(O.lire_piece(RACINE, "catalogue")[0])
    par_id = {p["id"]: p for p in pile["fiches"]}
    for L in O.LECTURES:
        for k, lot in enumerate(cle[L]["lots"], 1):
            entrees = []
            for et in lot:
                i = cle[L]["etiquettes"][et]
                vals, alt = valeurs_attendues(par_id[i]), ()
                if modif:
                    vals, alt = modif(L, i, par_id[i], dict(vals))
                e = entree_lue(par_id[i], vals, cat, alt)
                e["etiquette"] = et
                entrees.append(e)
            texte = "```json\n" + json.dumps({"lecture": entrees}, ensure_ascii=False) + "\n```"
            if contenu_lot:
                texte = contenu_lot(L, k, texte)
            r = {"id": f"essai-{L}-{k}", "object": "chat.completion", "model": modele,
                 "choices": [{"index": 0, "message": {"role": "assistant", "content": texte}, "finish_reason": "stop"}],
                 "usage": {"prompt_tokens": 1, "completion_tokens": 1}}
            p = env / f"reponse-{L}-lot{k}-v2.json"
            if sceller:
                O.ecrire_scelle(p, json.dumps(r, ensure_ascii=False))
            else:
                p.write_text(json.dumps(r, ensure_ascii=False), encoding="utf-8")


def id_de(nom):
    aut, *_ = PLAN[nom]
    k = list(PLAN).index(nom) + 1
    return f"{aut}-p{1 + k % 2}-{k:02d}"


def classer(env, **kw):
    return K.classement(env, env.parent, **kw)[0]


def sans(nom_ids):
    return lambda L, i, p, v: (v, ())


# --- essais : préparation ------------------------------------------------------------------------------------------------

def test_normalisation_egale_a_celle_de_l_orchestrateur():
    if not CLONE.is_file():
        pytest.skip("clone de l'orchestrateur absent")
    arbre = ast.parse(CLONE.read_text(encoding="utf-8"))
    fn = next(n for n in arbre.body if isinstance(n, ast.FunctionDef) and n.name == "normaliser_typographie")
    ns = {}
    exec("import re\n" + ast.get_source_segment(CLONE.read_text(encoding="utf-8"), fn), ns)
    for s in ["« a »  b c d — e – f … “g” ‘h’ i\t\tj", "rien", "x  \n  y"]:
        assert ns["normaliser_typographie"](s) == O.normaliser_typographie(s)


def test_preparer_sain_aveugle_et_borne(tmp_path):
    env, man = preparer(tmp_path)
    assert man["pile"]["fiches"] == 28 and man["pile"]["reelles_admissibles"] == 8 and man["pile"]["temoins"] == 20
    assert man["pile"]["hors_question"] == 3 and man["pile"]["champs_retires"] == {}
    pile = json.loads((env / "pile-interne-v2.json").read_text(encoding="utf-8"))
    motifs = sorted(h["motif"] for h in pile["hors_question"])
    assert motifs[0].startswith("0 étiquette") and motifs[1].startswith("2 étiquette") and "rien" in motifs[2]
    assert man["lots"]["tailles"] == [14, 14] and man["garde_depense"]["appels"] == 4
    assert man["garde_depense"]["pire_cas_total_usd"] <= 4.0 and man["garde_depense"]["max_tokens"] == 32768
    cle = json.loads((env / "cle-lectures-v2.json").read_text(encoding="utf-8"))
    assert cle["L1"]["ordre"] != cle["L2"]["ordre"] and sorted(cle["L1"]["ordre"]) == sorted(cle["L2"]["ordre"])
    consigne = O.lire_piece(RACINE, "consigne")[0]
    catalogue = O.lire_piece(RACINE, "catalogue")[0]
    fs = fiches_factices()
    secrets = [f["identifiant_auteur"] for f in fs] + [f["empreinte"] for f in fs] + ['"auteur"', '"passe"', '"temoin"',
               '"famille"', '"attendu"', "T-V", "T-FA", "T-H1", "propa-p", "propb-p", "propc-p", "«", "»", "’"]
    vus = []
    for L in O.LECTURES:
        for k in (1, 2):
            msg = (env / f"envoi-{L}-lot{k}-v2.txt").read_text(encoding="utf-8")
            assert msg.startswith(consigne.rstrip("\n")) and catalogue.rstrip("\n") in msg
            bloc = msg.split("```json\n")[-1].rsplit("\n```", 1)[0]
            lot = json.loads(bloc)
            assert [x["etiquette"] for x in lot] == cle[L]["lots"][k - 1]
            for x in lot:
                assert list(x["fiche"]) == [c for c, _ in O.ORDRE_VUE]
                vus.append(x["fiche"]["nom"])
                assert not any(s in json.dumps(x["fiche"], ensure_ascii=False) for s in secrets)
            corps = json.loads((env / f"envoi-{L}-lot{k}-v2.corps.json").read_text(encoding="utf-8"))
            assert corps["model"] == "kimi-k3.1-pro" and corps["messages"][0]["content"] == msg
            assert set(corps) == {"model", "messages", "max_tokens"}
    assert len(vus) == 56 and len(set(vus)) == 28
    etiq = [e for lot in cle["L1"]["lots"] for e in lot]
    assert etiq == [f"F{i:02d}" for i in range(1, 29)]
    for nom in man["fichiers"]:
        O.verifier_sceau(env / nom)


def test_ordres_par_seedsequence_consignee(tmp_path):
    env, man = preparer(tmp_path)
    pile = json.loads((env / "pile-interne-v2.json").read_text(encoding="utf-8"))
    cle = json.loads((env / "cle-lectures-v2.json").read_text(encoding="utf-8"))
    e = np.random.SeedSequence(2026111302).spawn(4)
    for j, L in enumerate(("L1", "L2")):
        perm = np.random.default_rng(e[j]).permutation(len(pile["fiches"]))
        assert cle[L]["ordre"] == [pile["fiches"][int(i)]["id"] for i in perm]
    assert man["graines"]["enfants"] == {"ordre_L1": [0], "ordre_L2": [1], "departage": [2], "temoin_permute": [3]}


def test_preparer_reproductible(tmp_path):
    a, _ = preparer(tmp_path / "a")
    b, _ = preparer(tmp_path / "b")
    for n in ("envoi-L1-lot1-v2.txt", "envoi-L2-lot2-v2.corps.json", "cle-lectures-v2.json"):
        assert (a / n).read_bytes() == (b / n).read_bytes()


@pytest.mark.parametrize("cas", ["absente", "mauvaise_empreinte", "envoi_non_permis", "recette", "non_scellee",
                                 "champ_manquant", "lecteur_vide"])
def test_attestation_fautive_refusee(tmp_path, cas):
    pf, h = ecrire_fiches(tmp_path, fiches_factices())
    if cas == "absente":
        pa = tmp_path / "rien.json"
    elif cas == "non_scellee":
        pa = tmp_path / "att.json"
        pa.write_text(json.dumps({"lecteur": "x", "lu_le": "y", "fiches_validees_sha256": h,
                                  "aucune_recette_aucun_secret": True, "envoi_au_lecteur_externe_permis": True}))
    elif cas == "champ_manquant":
        pa = tmp_path / "att.json"
        O.ecrire_scelle(pa, json.dumps({"lecteur": "x", "fiches_validees_sha256": h}))
    else:
        change = {"mauvaise_empreinte": {"fiches_validees_sha256": "0" * 64},
                  "envoi_non_permis": {"envoi_au_lecteur_externe_permis": "oui"},
                  "recette": {"aucune_recette_aucun_secret": False}, "lecteur_vide": {"lecteur": " "}}[cas]
        pa = ecrire_attestation(tmp_path, h, **change)
    with pytest.raises(O.Refus):
        O.preparer(pf, pa, tmp_path / "envois", racine_de(tmp_path))
    assert not (tmp_path / "envois").exists()


def test_fiches_non_scellees_ou_alterees_refusees(tmp_path):
    pf, h = ecrire_fiches(tmp_path, fiches_factices())
    pa = ecrire_attestation(tmp_path, h)
    pf.write_text(pf.read_text(encoding="utf-8").replace("Idée factice A1", "Idée factice A9"), encoding="utf-8")
    with pytest.raises(O.Refus):
        O.preparer(pf, pa, tmp_path / "envois", racine_de(tmp_path))
    Path(str(pf) + ".sha256").unlink()
    with pytest.raises(O.Refus):
        O.preparer(pf, pa, tmp_path / "envois", racine_de(tmp_path))


def test_piece_epinglee_alteree_refusee(tmp_path):
    rac = racine_de(tmp_path)
    pf, h = ecrire_fiches(tmp_path, fiches_factices())
    pa = ecrire_attestation(tmp_path, h)
    O.preparer(pf, pa, tmp_path / "e1", rac)  # copie conforme : passe
    p = rac / O.PIECES["consigne"][0]
    p.write_text(p.read_text(encoding="utf-8") + " ", encoding="utf-8")
    with pytest.raises(O.Refus):
        O.preparer(pf, pa, tmp_path / "e2", rac)


def test_ecriture_scellee_jamais_ecrasee(tmp_path):
    p = tmp_path / "x.json"
    h = O.ecrire_scelle(p, "a")
    assert O.verifier_sceau(p) == h
    with pytest.raises(O.Refus):
        O.ecrire_scelle(p, "b")
    assert p.read_text() == "a"


def test_sortie_non_vide_refusee(tmp_path):
    (tmp_path / "envois").mkdir()
    (tmp_path / "envois" / "x").write_text("x")
    pf, h = ecrire_fiches(tmp_path, fiches_factices())
    pa = ecrire_attestation(tmp_path, h)
    with pytest.raises(O.Refus):
        O.preparer(pf, pa, tmp_path / "envois", racine_de(tmp_path))


def test_garde_appels_et_depense(tmp_path):
    plan = {f"B{i}": ("propa", "levier:cout", "ajout", "processeur", {}) for i in range(41)}
    with pytest.raises(O.Refus, match="appels"):
        preparer(tmp_path / "a", fiches_factices(plan, hors=False))  # 61 fiches : 4 lots × 2 = 8 appels
    plan = {f"B{i}": ("propa", "levier:cout", "ajout", "processeur", {}) for i in range(40)}
    _, man = preparer(tmp_path / "b", fiches_factices(plan, hors=False))  # 60 fiches : 6 appels
    assert man["garde_depense"]["appels"] == 6 and man["lots"]["tailles"] == [20, 20, 20]
    gros = fiches_factices(plan, hors=False)
    for f in gros:
        f["enonce"] += " x" * 30000
    with pytest.raises(O.Refus, match="max_tokens"):
        preparer(tmp_path / "c", gros)


def test_champs_hors_gabarit_retires_et_consignes(tmp_path):
    fs = fiches_factices()
    fs[0]["citations_verifiees"] = [{"citation": "c", "verifiee": True}]
    fs[0]["anteriorite"][0]["non_opposable"] = True
    env, man = preparer(tmp_path, fs)
    assert man["pile"]["champs_retires"] == {fs[0]["identifiant_auteur"]: ["anteriorite[0].non_opposable",
                                                                          "citations_verifiees"]}
    for f in (env).glob("envoi-*.txt"):
        assert "citations_verifiees" not in f.read_text(encoding="utf-8")


# --- essais : vérification et classement -------------------------------------------------------------------------------

def test_classement_sain(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env)
    r = classer(env)
    assert r["lisible"] and r["L5"]["rejet"] and r["verdict"].startswith("lisible")
    for L in ("L1", "L2"):
        assert all(x == 0 for x in r["non_prouves"][L].values()) and r["anomalies"][L] == []
    st = r["classement"]["statut"]
    assert st[id_de("A4")] == {"statut": "ecartee", "motif": "porte(s) R7"}
    assert st[id_de("A6")]["motif"] == "porte(s) R2" and st[id_de("A5")] == {"statut": "occupee", "entrees": "C8"}
    reelles = [id_de(n) for n in PLAN]
    tirage = np.random.default_rng(np.random.SeedSequence(2026111302).spawn(4)[2]).permutation(8)
    rang = {reelles[int(j)]: k for k, j in enumerate(tirage)}
    assert r["classement"]["departage"] == rang  # enfant 2, fiches réelles admissibles dans l'ordre du fichier
    a2, a7 = sorted([id_de("A2"), id_de("A7")], key=rang.get)
    a3, a8 = id_de("A3"), id_de("A8")
    assert r["classement"]["ordre_neuves"] == [id_de("A1"), a2, a7, a3, a8]
    assert r["designees"] == [id_de("A1"), a2]
    assert r["L1"]["reconnues"] == 7 and r["L2"]["tient"] and r["L3"]["tient"] and r["L4"]["tient"]
    assert r["L5"]["C_reelles"] == dict(zip(reelles, [5, 5, 4, 0, 0, 0, 5, 4]))
    assert set(r["L5"]["C_hasard"].values()) == {0}
    assert abs(r["L5"]["test"]["p"] - 165 / 12870) < 0.004
    assert r["echecs"] == {"E1": False, "E2": False, "E2_lecture_incomplete": False, "E3": False, "E4": False,
                           "E5": False}
    assert r["lecture_complete"]["complete"] and r["regle_de_designation"] == "L5" and r["variante_detachee"] is None
    assert r["audit_proprete"]["declenche"] and r["audit_proprete"]["toutes_publiees_reconnues"]
    for L in ("L1", "L2"):
        assert all(d["justes"] == d["sur"] for d in r["exactitude_lecteur"][L].values())
    # témoin à score permuté recalculé à part
    perm = np.random.default_rng(np.random.SeedSequence(2026111302).spawn(4)[3]).permutation(8)
    vec = {i: r["retenu"][i] for i in reelles}
    cout = {id_de(n): PLAN[n][3] for n in PLAN}
    vp = {reelles[i]: vec[reelles[int(perm[i])]] for i in range(8)}
    cp = {reelles[i]: cout[reelles[int(perm[i])]] for i in range(8)}
    neuves = [i for i in reelles if all(vp[i][c] == 1 for c in ("R2", "R3", "R7")) and vp[i]["N"] == "aucune"]
    neuves.sort(key=lambda i: (-(vp[i]["R1"] + vp[i]["R4"] + vp[i]["R5"] + vp[i]["R6"]),
                               {"processeur": 0, "depense": 1}[cp[i]], rang[i]))
    assert r["temoin_score_permute"]["deux_premieres"] == neuves[:2]
    assert r["temoin_score_permute"]["communes_avec_designees"] == len(set(neuves[:2]) & set(r["designees"]))
    cpp = r["comptes_par_proposeur"]
    assert cpp["propa"]["admissibles"] == 3 and cpp["propa"]["hors_question"] == 1 and cpp["propa"]["designees"] == (
        1 + (a2 == id_de("A7")))
    assert sum(d["designees"] for d in cpp.values()) == 2
    assert len(r["descriptif_holm"]) == 8 and all("p_holm" in d for d in r["descriptif_holm"])
    r7 = next(d for d in r["descriptif_holm"] if d["critere"] == "R7")
    assert r7["difference"] > 0 and r7["p_holm"] >= r7["p_brute"]


def test_citation_alteree_compte_zero(tmp_path):
    env, _ = preparer(tmp_path)
    a1 = id_de("A1")
    lire(env, modif=lambda L, i, p, v: (v, ("R1",) if (L == "L1" and i == a1) else ()))
    r = classer(env)
    assert r["non_prouves"]["L1"]["R1"] == 1 and r["non_prouves"]["L2"]["R1"] == 0
    assert r["retenu"][a1]["R1"] == 0 and a1 not in r["designees"]
    assert r["classement"]["statut"][a1] == {"statut": "neuve", "S": 3}


def test_espaces_normalises_seulement():
    vue = {"enonce": "un  texte suffisamment long\navec   des espaces", "x": ["autre champ de la fiche factice"]}
    assert O.passage_dans("un texte suffisamment long avec des", O.feuilles(vue))[0]
    assert not O.passage_dans("un texte, suffisamment long avec des", O.feuilles(vue))[0]
    assert not O.passage_dans("Un texte suffisamment long avec", O.feuilles(vue))[0]
    assert not O.passage_dans("avec des espaces autre champ", O.feuilles(vue))[0]  # à cheval sur deux champs
    assert not O.passage_dans("   ", O.feuilles(vue))[0] and not O.passage_dans(None, O.feuilles(vue))[0]
    vue2 = {"enonce": 'il dit "oui" puis répète a\\b sans fin'}
    assert O.passage_dans('il dit \\"oui\\" puis répète', O.feuilles(vue2))[0]  # recopié de la vue JSON, échappé
    assert O.passage_dans('dit "oui" puis répète a\\b', O.feuilles(vue2))[0]
    assert O.passage_dans('puis répète a\\\\b sans fin', O.feuilles(vue2))[0]
    assert not O.passage_dans('il dit \\"non\\" puis répète', O.feuilles(vue2))[0]


def test_M1_passages_triviaux_refuses():
    """M1 : « e », « + », « . », une étiquette de levier, « C7 », « 2026 » ne prouvent rien ; 20 caractères hors espaces."""
    vue = {"enonce": "e + . levier:juge C7 2026 et une phrase assez longue pour prouver quelque chose", "s": "+"}
    for triv in ("e", "+", ".", "levier:juge", "C7", "2026", "une phrase assez", "  e  +  .  "):
        ok, motif = O.passage_dans(triv, O.feuilles(vue))
        assert not ok and ("trop court" in motif or "vide" in motif), triv
    assert O.passage_dans("une phrase assez longue pour", O.feuilles(vue))[0]
    assert not O.court("abcdefghij klmnopqrst") and O.court("abcdefghij klmnopqrs")  # 20 contre 19 hors espaces
    assert O.LONGUEUR_MIN_PASSAGE == 20


def test_M1_occupation_par_le_mecanisme_de_Ck_seulement():
    cat = O.entrees_catalogue(O.lire_piece(RACINE, "catalogue")[0])
    vue, _ = O.vue_lecteur(fiche("Z", "propa", 1, 1, "levier:cout"))
    pf = vue["enonce"][:60]
    meca7 = O.sans_gras(cat["C7"][2])
    bons = {"valeur": "C7", "passage_fiche": pf, "passage_catalogue": meca7[:80]}
    assert O.verifier_entree({"N": bons}, vue, False, cat)["N"]["compte"] == "C7"
    for pc in ("C7", "2026", "PACE (arXiv 2606.08106v1, 2026)", "`docs/sources/pdf/2606.08106v1.pdf`",
               O.sans_gras(cat["C2"][2])[:80], "e", "+"):
        r = O.verifier_entree({"N": {**bons, "passage_catalogue": pc}}, vue, False, cat)["N"]
        assert r["compte"] == "aucune" and r["occupation_non_prouvee"], pc
    for pfx in ("Z", "e", "passage qui n'est pas dans la fiche factice", None):  # passage de la fiche exigé
        r = O.verifier_entree({"N": {**bons, "passage_fiche": pfx}}, vue, False, cat)["N"]
        assert r["compte"] == "aucune" and r["occupation_non_prouvee"], pfx


def test_M1_passages_courts_comptes_et_rapportes(tmp_path):
    env, _ = preparer(tmp_path)
    a1 = id_de("A1")

    def contenu(L, k, texte):
        o = json.loads(texte.split("```json\n")[1].rsplit("\n```", 1)[0])
        cle = json.loads((env / "cle-lectures-v2.json").read_text(encoding="utf-8"))
        for e in o["lecture"]:
            if cle[L]["etiquettes"][e["etiquette"]] == a1 and L == "L1":
                e["R1"]["passage"] = "+"
        return "```json\n" + json.dumps(o, ensure_ascii=False) + "\n```"
    lire(env, contenu_lot=contenu)
    r = classer(env)
    assert r["passages_courts_refuses"]["L1"]["R1"] == 1 and r["passages_courts_refuses"]["L2"]["R1"] == 0
    assert r["retenu"][a1]["R1"] == 0
    md = K.resume_md(r)
    assert "Passages courts refusés" in md and "L1 : 1" in md


def test_lectures_discordantes(tmp_path):
    env, _ = preparer(tmp_path)
    a2, a7, a1 = id_de("A2"), id_de("A7"), id_de("A1")

    def m(L, i, p, v):
        if L == "L2" and i == a2:
            v["R7"] = 0
        if L == "L2" and i == a7:
            v["N"] = "C4"
        if L == "L1" and i == a1:
            v["R5"] = 0
        return v, ()
    lire(env, modif=m)
    r = classer(env)
    st = r["classement"]["statut"]
    assert st[a2]["statut"] == "ecartee" and st[a7] == {"statut": "occupee", "entrees": "C4"}
    assert st[a1] == {"statut": "neuve", "S": 3}
    dep = r["classement"]["departage"]
    tete = sorted([a1, id_de("A3")], key=dep.get)  # S = 3 et processeur pour les deux : départage tiré
    assert r["classement"]["ordre_neuves"] == tete + [id_de("A8")]
    assert r["classement"]["deux_premieres"] == tete
    # trois neuves sur huit : p ≈ C(8,3)/C(16,3) = 0,1 ; L5 non rejetée, aucune désignée
    assert not r["L5"]["rejet"] and r["designees"] == []


def test_occupation_non_prouvee_compte_aucune(tmp_path):
    env, _ = preparer(tmp_path)
    a7 = id_de("A7")

    def m(L, i, p, v):
        if i == a7:
            v["N"] = "C4"
            return v, ("Nc",)
        return v, ()
    lire(env, modif=m)
    r = classer(env)
    assert r["non_prouves"]["L1"]["N_occupation_non_prouvee"] == 1
    assert r["classement"]["statut"][a7]["statut"] == "neuve"


@pytest.mark.parametrize("manquees,tient", [(2, True), (3, False)])
def test_temoins_publies_non_reconnus_L1(tmp_path, manquees, tient):
    env, _ = preparer(tmp_path)
    cibles = ["T-FA", "T-CS", "T-AIS"][:manquees]
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "aucune"} if i in cibles else v, ()))
    r = classer(env)
    assert r["L1"]["reconnues"] == 7 - manquees and r["L1"]["tient"] is tient
    assert r["lisible"] is tient and (r["designees"] != []) is tient
    if not tient:
        assert r["echecs"]["E2"] and r["verdict"].startswith("E2") and r["classement"]["ordre_neuves"]


def test_publiee_reconnue_dans_une_seule_lecture_suffit_a_L1(tmp_path):
    env, _ = preparer(tmp_path)
    cibles = ["T-FA", "T-CS", "T-AIS"]
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "aucune"} if (i in cibles and L == "L2") else v, ()))
    r = classer(env)
    assert r["L1"]["reconnues"] == 7 and r["L1"]["tient"]
    # la mauvaise entrée ne compte pas
    env2, _ = preparer(tmp_path / "b")
    lire(env2, modif=lambda L, i, p, v: ({**v, "N": "C12"} if i in cibles else v, ()))
    assert classer(env2)["L1"]["reconnues"] == 4


@pytest.mark.parametrize("prouve", [True, False])
def test_fausse_fiche_acceptee_L2(tmp_path, prouve):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R3": 1}, () if prouve else ("R3",)) if (i == "T-F53" and L == "L2")
         else (v, ()))
    r = classer(env)
    assert r["L2"]["tient"] is (not prouve) and r["lisible"] is (not prouve)


def test_vrai_ou_jumeau_rejete_L3(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R7": 0} if (i == "T-J" and L == "L1") else v, ()))
    r = classer(env)
    assert not r["L3"]["tient"] and r["L3"]["par_temoin"]["T-J"]["portes_manquantes"] == ["R7"]
    assert r["designees"] == [] and r["echecs"]["E2"]
    env2, _ = preparer(tmp_path / "b")
    lire(env2, modif=lambda L, i, p, v: ({**v, "N": "C3"} if (i == "T-V" and L == "L2") else v, ()))
    assert not classer(env2)["L3"]["tient"]


def test_lectures_trop_discordantes_L4(tmp_path):
    env, _ = preparer(tmp_path)
    pile = json.loads((env / "pile-interne-v2.json").read_text(encoding="utf-8"))
    bascule = {p["id"] for k, p in enumerate(pile["fiches"]) if k % 2 == 0}
    lire(env, modif=lambda L, i, p, v: ({**v, "R7": 1 - v["R7"]} if (i in bascule and L == "L2") else v, ()))
    r = classer(env)
    assert not r["L4"]["R7"]["tient"] and r["L4"]["R7"]["jugee_sur"] == "kappa" and not r["lisible"]


def test_kappa_et_marge_constante():
    k = K.kappa_accord([1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 0])
    assert k["kappa"] == 1 and k["tient"]
    k = K.kappa_accord([1, 0, 1, 0], [1, 1, 0, 0])
    assert abs(k["kappa"]) < 1e-12 and not k["tient"]
    k = K.kappa_accord([1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1])
    assert abs(k["kappa"] - (0.9 - 0.74) / 0.26) < 1e-9 and k["tient"]
    k = K.kappa_accord([1] * 10, [1] * 9 + [0])  # une marge constante : accord brut 0,9 ≥ 0,8
    assert k["marge_constante"] and k["tient"] and k["kappa"] == 0
    k = K.kappa_accord([1] * 10, [1] * 7 + [0] * 3)
    assert k["marge_constante"] and not k["tient"]
    k = K.kappa_accord([0] * 6, [0] * 6)
    assert k["kappa"] is None and k["tient"]


def test_L5_non_rejetee_aucune_designee(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R7": 0} if p["origine"] == "reelle" else v, ()))
    r = classer(env)
    assert r["lisible"] and not r["L5"]["rejet"] and r["L5"]["test"]["p"] == 1.0
    assert r["designees"] == [] and r["echecs"]["E3"] and r["verdict"].startswith("E3")


def test_L5_hasard_aussi_bon_non_rejetee(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R7": 1} if p["famille"] == "hasard" else v, ()))
    r = classer(env)
    assert not r["L5"]["rejet"] and r["designees"] == []
    assert not r["audit_proprete"]["aucune_idee_au_hasard_passee"]


def test_une_seule_neuve_L5_ne_peut_rejeter_et_E5(tmp_path):
    """Une seule neuve parmi n réelles : p ≥ n / (n + 8) > 0,05 ; E4 n'est donc jamais atteint sous L5 (rapporté)."""
    env, _ = preparer(tmp_path)
    garde = id_de("A1")
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "C10"} if (p["origine"] == "reelle" and i != garde) else v, ()))
    r = classer(env)
    assert r["classement"]["ordre_neuves"] == [garde] and r["classement"]["deux_premieres"] == [garde]
    assert not r["L5"]["rejet"] and abs(r["L5"]["test"]["p"] - 0.5) < 0.01 and r["designees"] == []
    assert r["echecs"]["E3"] and not r["echecs"]["E4"]
    assert r["echecs"]["E5"]  # 5 occupées sur 6 passées > 80 %


def test_E4_designation_partielle_si_L5_rejetee():
    """E4 se teste au niveau du programme : deux neuves exigées pour désigner deux idées ; la règle tient même si L5
    rejette avec une seule neuve (impossible avec huit idées au hasard, voir l'essai précédent)."""
    cl = K.classer(["a", "b"], {"a": {**TOUT1}, "b": {**TOUT1, "R2": 0}}, {"a": "depense", "b": "processeur"},
                   {"a": 1, "b": 0})
    assert cl["ordre_neuves"] == ["a"] and cl["deux_premieres"] == ["a"]


def test_permutation_contre_enumeration_exacte():
    from itertools import combinations
    x, y = [3, 5, 0, 4], [0, 1, 0]
    z = x + y
    obs = np.mean(x) - np.mean(y)
    stats = [np.mean([z[i] for i in c]) - np.mean([z[i] for i in range(7) if i not in c])
             for c in combinations(range(7), 4)]
    exact = np.mean([s >= obs - 1e-12 for s in stats])
    exact2 = np.mean([abs(s) >= abs(obs) - 1e-12 for s in stats])
    t = K.test_permutation(x, y, np.random.SeedSequence(7), 100_000)
    assert abs(t["p"] - exact) < 0.005
    t2 = K.test_permutation(x, y, np.random.SeedSequence(7), 100_000, bilateral=True)
    assert abs(t2["p"] - exact2) < 0.005
    t3 = K.test_permutation(y, x, np.random.SeedSequence(7), 20_000)
    assert t3["p"] > 0.9
    assert K.test_permutation([], [1], np.random.SeedSequence(1))["p"] is None
    t4 = K.test_permutation([1] * 10, [0] * 10, np.random.SeedSequence(3), 20_000)  # p exacte 1/184 756
    assert t4["depassements"] == 0 and t4["p"] == 1 / 20_001
    assert t["p"] == (1 + t["depassements"]) / (1 + t["permutations"])
    assert K.PERMUTATIONS == 100_000 and K.SEUIL_P == 0.05 and K.ENTROPIE_TEST == 2026111303


def test_holm():
    adj = K.holm([0.01, 0.04, 0.03, 0.005])
    assert np.allclose(adj, [0.03, 0.06, 0.06, 0.02])
    assert K.holm([0.5, 0.9]) == [1.0, 1.0]


def test_reponses_fautives(tmp_path):
    env, _ = preparer(tmp_path)
    cle = json.loads((env / "cle-lectures-v2.json").read_text(encoding="utf-8"))
    oter, doubler = cle["L1"]["lots"][0][0], cle["L1"]["lots"][0][1]

    def contenu(L, k, texte):
        if L == "L1" and k == 2:
            return "Voici ma lecture : pas de JSON ici."
        if L == "L1" and k == 1:
            o = json.loads(texte.split("```json\n")[1].rsplit("\n```", 1)[0])
            par = {e["etiquette"]: e for e in o["lecture"]}
            o["lecture"] = [e for e in o["lecture"] if e["etiquette"] != oter] + [par[doubler],
                                                                                 {"etiquette": "F99"}]
            o["lecture"][2], o["lecture"][3] = o["lecture"][3], o["lecture"][2]
            return json.dumps(o)
        return texte
    lire(env, contenu_lot=contenu)
    r = classer(env)
    genres = sorted(a["genre"] for a in r["anomalies"]["L1"])
    assert genres == ["entree_en_double", "entree_manquante", "etiquette_hors_lot", "ordre_du_lot_non_suivi",
                      "reponse_illisible"]
    assert r["anomalies"]["L2"] == []
    i_oter = cle["L1"]["etiquettes"][oter]
    lv = K.O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])
    assert lv["fiches"][i_oter]["R7"]["compte"] == 0 and lv["fiches"][i_oter]["N"]["compte"] == "aucune"


def test_valeurs_non_entieres_et_R4(tmp_path):
    cat = O.entrees_catalogue(O.lire_piece(RACINE, "catalogue")[0])
    vue, _ = O.vue_lecteur(fiche("Z", "propa", 1, 1, "levier:cout"))
    e = {"R1": {"valeur": "1", "passage": vue["enonce"][:30]}, "R2": {"valeur": True, "passage": vue["enonce"][:30]},
         "R3": {"valeur": 1.0, "passage": vue["enonce"][:30]}, "R4": {"valeur": 0, "motif": "x"},
         "R5": {"valeur": 1, "passage": vue["enonce"][:30]}, "N": {"valeur": "C99"}}
    r = O.verifier_entree(e, vue, False, cat)
    assert [r[c]["compte"] for c in ("R1", "R2", "R3", "R4", "R5", "R6", "R7")] == [0, 0, 0, 1, 1, 0, 0]
    assert r["N"]["compte"] == "aucune" and r["N"]["occupation_non_prouvee"]
    r = O.verifier_entree(e, vue, True, cat)  # levier:juge : R4 lu, 0 rendu
    assert r["R4"]["compte"] == 0
    e["R4"] = {"valeur": 1, "passage": "changer le paramètre du juge en la valeur"}  # pas dans cette fiche
    assert O.verifier_entree(e, vue, True, cat)["R4"]["compte"] == 0
    e["R4"] = {"valeur": 1, "passage": "levier:cout"}  # étiquette seule : trop courte
    assert O.verifier_entree(e, vue, True, cat)["R4"]["compte"] == 0
    e["R4"] = {"valeur": 1, "passage": vue["demande_organisme"]["texte"]}
    assert O.verifier_entree(e, vue, True, cat)["R4"]["compte"] == 1


def test_temoin_juge_R4_attendu(tmp_path):
    """T-CS (levier:juge) doit avoir R4 = 0 : un lecteur qui met 1 avec citation exacte est compté, et l'exactitude le dit."""
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R4": 1} if i == "T-CS" else v, ()))
    r = classer(env)
    err = r["exactitude_lecteur"]["L1"]["R4"]["erreurs"]
    assert err == [{"temoin": "T-CS", "attendu": 0, "lu": 1}]


@pytest.mark.parametrize("cas", ["non_scellee", "modele", "absente", "alteree"])
def test_reponse_refusee(tmp_path, cas):
    env, _ = preparer(tmp_path)
    if cas == "non_scellee":
        lire(env, sceller=False)
    elif cas == "modele":
        lire(env, modele="autre-modele")
    else:
        lire(env)
        p = env / "reponse-L2-lot2-v2.json"
        if cas == "absente":
            p.unlink()
            Path(str(p) + ".sha256").unlink()
        else:
            p.write_text(p.read_text(encoding="utf-8").replace("manque", "manqua"), encoding="utf-8")
    with pytest.raises(O.Refus):
        classer(env)


def test_envoi_altere_refuse(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env)
    p = env / "pile-interne-v2.json"
    p.write_text(p.read_text(encoding="utf-8").replace('"depense"', '"processeur"'), encoding="utf-8")
    with pytest.raises(O.Refus):
        classer(env)


def test_auteurs_sans_effet_sur_le_classement(tmp_path):
    env, _ = preparer(tmp_path / "a")
    lire(env)
    r1 = classer(env)
    fs = fiches_factices(renommer={"propa": "zz", "propb": "aa"})
    env2, _ = preparer(tmp_path / "b", fs)
    lire(env2)
    r2 = classer(env2)
    trad = lambda s: s.replace("zz-", "propa-").replace("aa-", "propb-")
    assert [trad(i) for i in r2["designees"]] == r1["designees"]
    assert [trad(i) for i in r2["classement"]["ordre_neuves"]] == r1["classement"]["ordre_neuves"]


def test_aucun_appel_ni_juge_dans_le_code():
    for nom in ("outil_lecteur_conception_propre_v2.py", "classer_conception_propre_v2.py"):
        arbre = ast.parse((MODS / nom).read_text(encoding="utf-8"))
        imports = {a.name.split(".")[0] for n in ast.walk(arbre) if isinstance(n, ast.Import) for a in n.names}
        imports |= {n.module.split(".")[0] for n in ast.walk(arbre) if isinstance(n, ast.ImportFrom) and n.module}
        assert not imports & {"urllib", "http", "socket", "requests", "subprocess", "os"}
        texte = (MODS / nom).read_text(encoding="utf-8")
        assert "notes-par-juge" not in texte and "environ" not in texte


def test_bout_en_bout_en_ligne_de_commande(tmp_path):
    pf, h = ecrire_fiches(tmp_path, fiches_factices())
    pa = ecrire_attestation(tmp_path, h)
    env = tmp_path / "envois"
    py = [sys.executable, "-I", "-B"]
    outil, classeur = str(MODS / "outil_lecteur_conception_propre_v2.py"), str(MODS / "classer_conception_propre_v2.py")
    c = subprocess.run(py + [outil, "preparer", "--fiches", str(pf), "--attestation", str(pa), "--sortie", str(env),
                             "--racine", str(racine_de(tmp_path))], capture_output=True, text=True)
    assert c.returncode == 0, c.stderr
    lire(env)
    c = subprocess.run(py + [outil, "verifier", "--envois", str(env), "--racine", str(racine_de(tmp_path))], capture_output=True,
                       text=True)
    assert c.returncode == 0, c.stderr
    O.verifier_sceau(env / "lecture-verifiee-L1-v2.json")
    sortie = tmp_path / "classement"
    c = subprocess.run(py + [classeur, "--envois", str(env), "--sortie", str(sortie), "--racine", str(racine_de(tmp_path))],
                       capture_output=True, text=True)
    assert c.returncode == 0, c.stderr
    for n in ("classement-v2.json", "classement-v2.md", "lecture-verifiee-L1-v2.json", "lecture-verifiee-L2-v2.json"):
        O.verifier_sceau(sortie / n)
    r = json.loads((sortie / "classement-v2.json").read_text(encoding="utf-8"))
    assert r["designees"] and r["lisible"]
    c = subprocess.run(py + [classeur, "--envois", str(env), "--sortie", str(sortie), "--racine", str(racine_de(tmp_path))],
                       capture_output=True, text=True)
    assert c.returncode == 2 and "R12" in c.stderr
    c = subprocess.run(py + [outil, "preparer", "--fiches", str(pf), "--attestation", str(pa), "--sortie", str(env),
                             "--racine", str(racine_de(tmp_path))], capture_output=True, text=True)
    assert c.returncode == 2


# --- v2 : M2, lecture incomplète ------------------------------------------------------------------------------------------

def _lot_illisible(cible_L, cible_k):
    return lambda L, k, texte: "pas de JSON : coupé" if (L, k) == (cible_L, cible_k) else texte


def test_M2_lot_illisible_interdit_la_designation(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, contenu_lot=_lot_illisible("L2", 1))
    r = classer(env)
    assert not r["lecture_complete"]["complete"] and r["echecs"]["E2_lecture_incomplete"] and r["echecs"]["E2"]
    assert r["designees"] == [] and not r["lisible"]
    assert r["verdict"].startswith("E2 : lecture illisible") and "L2 lot 1 : reponse_illisible" in r["verdict"]
    cle = json.loads((env / "cle-lectures-v2.json").read_text(encoding="utf-8"))
    lot = [cle["L2"]["etiquettes"][e] for e in cle["L2"]["lots"][0]]
    pile = {p["id"]: p for p in json.loads((env / "pile-interne-v2.json").read_text(encoding="utf-8"))["fiches"]}
    assert r["lecture_complete"]["reelles_touchees"] == sorted(i for i in lot if pile[i]["origine"] == "reelle")
    assert len(r["lecture_complete"]["reelles_touchees"]) + len(r["lecture_complete"]["temoins_touches"]) == len(lot)
    md = K.resume_md(r)
    assert "reponse_illisible" in md and "Lecture complète : False" in md
    r2 = classer_variante(env)
    assert r2["designees"] == []


def test_M2_fin_length_meme_lisible_bloque(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env)
    p = env / "reponse-L1-lot2-v2.json"
    o = json.loads(p.read_text(encoding="utf-8"))
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    o["choices"][0]["finish_reason"] = "length"
    O.ecrire_scelle(p, json.dumps(o, ensure_ascii=False))
    r = classer(env)
    assert not r["lecture_complete"]["complete"] and r["designees"] == [] and "fin_non_stop" in r["verdict"]


@pytest.mark.parametrize("genre", ["manquante", "double"])
def test_M2_entree_manquante_ou_double_bloque(tmp_path, genre):
    env, _ = preparer(tmp_path)

    def contenu(L, k, texte):
        if (L, k) != ("L1", 2):
            return texte
        o = json.loads(texte.split("```json\n")[1].rsplit("\n```", 1)[0])
        o["lecture"] = o["lecture"][1:] if genre == "manquante" else o["lecture"] + [o["lecture"][-1]]
        return json.dumps(o, ensure_ascii=False)
    lire(env, contenu_lot=contenu)
    r = classer(env)
    assert not r["lecture_complete"]["complete"] and r["designees"] == []
    assert r["lecture_complete"]["fiches_touchees"] == 1


def test_anomalie_non_bloquante_etiquette_hors_lot(tmp_path):
    """Mutation survivante 9 de la contre-lecture : une entrée d'un autre lot est écartée, sans effet ni faux désordre."""
    env, _ = preparer(tmp_path)
    cle = json.loads((env / "cle-lectures-v2.json").read_text(encoding="utf-8"))
    etrangere = cle["L1"]["lots"][1][0]

    def contenu(L, k, texte):
        if (L, k) != ("L1", 1):
            return texte
        o = json.loads(texte.split("```json\n")[1].rsplit("\n```", 1)[0])
        e = copy.deepcopy(o["lecture"][0])
        e["etiquette"] = etrangere
        for c in O.CRITERES:
            e[c] = {"valeur": 0, "motif": "faux"}
        o["lecture"].append(e)
        return json.dumps(o, ensure_ascii=False)
    lire(env, contenu_lot=contenu)
    r = classer(env)
    assert [a["genre"] for a in r["anomalies"]["L1"]] == ["etiquette_hors_lot"]
    assert r["lecture_complete"]["complete"] and r["lisible"] and r["designees"]
    i = cle["L1"]["etiquettes"][etrangere]
    pile = {p["id"]: p for p in json.loads((env / "pile-interne-v2.json").read_text(encoding="utf-8"))["fiches"]}
    vals = valeurs_attendues(pile[i])
    lv = O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])
    assert all(lv["fiches"][i][c]["compte"] == vals[c] for c in O.CRITERES)  # la fausse entrée n'a rien changé


# --- v2 : M3, provenance des fiches ---------------------------------------------------------------------------------------

def _fiches_quarantaine():
    return [{"fiche": f, "signaux": ["motif"]} for f in fiches_factices()]


@pytest.mark.parametrize("cas", ["quarantaine_au_bon_nom", "autre_nom", "hors_runs", "run_mal_nomme", "fin_absente",
                                 "fin_code_1", "fin_autre_empreinte", "fin_non_scellee", "lien", "sans_admissible",
                                 "element_sans_internes"])
def test_M3_seule_la_copie_des_fiches_validees_du_run(tmp_path, cas):
    fs = fiches_factices()
    rac = racine_de(tmp_path)
    if cas == "quarantaine_au_bon_nom":
        pf, h = ecrire_fiches(tmp_path, _fiches_quarantaine())
    elif cas == "autre_nom":
        pf, h = ecrire_fiches(tmp_path, fs, nom="sortie--fiches-en-quarantaine.json")
    elif cas == "hors_runs":
        ecrire_fiches(tmp_path, fs)
        pf = rac / "docs" / "sortie--fiches-validees.json"
        pf.write_text(json.dumps(fs, ensure_ascii=False))
        h = O.sha256_fichier(pf)
        Path(str(pf) + ".sha256").write_text(f"{h}  {pf.name}\n")
    elif cas == "run_mal_nomme":
        pf, h = ecrire_fiches(tmp_path, fs, run="20261114-010203-autre-course-g1")
    elif cas == "fin_absente":
        pf, h = ecrire_fiches(tmp_path, fs)
        m = pf.parents[1] / "manifeste-lanceur-fin.json"
        m.unlink()
        Path(str(m) + ".sha256").unlink()
    elif cas == "fin_code_1":
        pf, h = ecrire_fiches(tmp_path, fs, fin=lambda h: {"code": 1, "pour_l_attestation": {"fiches_validees_sha256": h}})
    elif cas == "fin_autre_empreinte":
        pf, h = ecrire_fiches(tmp_path, fs, fin=lambda h: {"code": 0, "pour_l_attestation": {
            "fiches_validees_sha256": "0" * 64}})
    elif cas == "fin_non_scellee":
        pf, h = ecrire_fiches(tmp_path, fs)
        m = pf.parents[1] / "manifeste-lanceur-fin.json"
        m.write_text(m.read_text(encoding="utf-8") + " ", encoding="utf-8")
    elif cas == "lien":
        vrai, h = ecrire_fiches(tmp_path, fs)
        d = pf_dir = rac / "runs" / "course-ideation-conception-propre-v1" / "20261114-020203-course-ideation-conception-propre-v1-g1"
        (pf_dir / "copies").mkdir(parents=True)
        pf = pf_dir / "copies" / "sortie--fiches-validees.json"
        pf.symlink_to(vrai)
        Path(str(pf) + ".sha256").write_text(f"{h}  {pf.name}\n")
        shutil.copyfile(vrai.parents[1] / "manifeste-lanceur-fin.json", d / "manifeste-lanceur-fin.json")
        shutil.copyfile(vrai.parents[1] / "manifeste-lanceur-fin.json.sha256", d / "manifeste-lanceur-fin.json.sha256")
    elif cas == "sans_admissible":
        hors = [f for f in fs if f["nom"].split()[2].startswith("H")]
        pf, h = ecrire_fiches(tmp_path, hors)
    else:
        f0 = copy.deepcopy(fs)
        del f0[0]["identifiant_auteur"]
        pf, h = ecrire_fiches(tmp_path, f0)
    pa = ecrire_attestation(tmp_path, h)
    with pytest.raises(O.Refus):
        O.preparer(pf, pa, rac / "envois", rac)
    assert not (rac / "envois").exists()


def test_M3_chemin_relatif_accepte_et_classement_revérifie(tmp_path):
    fs = fiches_factices()
    rac = racine_de(tmp_path)
    pf, h = ecrire_fiches(tmp_path, fs)
    pa = ecrire_attestation(tmp_path, h)
    man = O.preparer(pf.relative_to(rac), pa, rac / "envois", rac)
    assert man["fiches_validees"]["chemin"] == ("runs/course-ideation-conception-propre-v1/" + RUN +
                                                "/copies/sortie--fiches-validees.json")
    assert man["fiches_validees"]["run"] == RUN and man["fiches_validees"]["sha256"] == h
    env = rac / "envois"
    lire(env)
    assert classer(env)["fiches_validees"]["sha256"] == h
    # la copie change après la préparation (compagnon réécrit) : le classement refuse
    pf.write_text(pf.read_text(encoding="utf-8").replace("Idée factice A1", "Idée factice A9"), encoding="utf-8")
    Path(str(pf) + ".sha256").write_text(f"{O.sha256_fichier(pf)}  {pf.name}\n")
    with pytest.raises(O.Refus):
        classer(env)
    # ... même si le manifeste de fin du run est réécrit d'accord avec elle : le manifeste des envois ne l'est pas
    m = pf.parents[1] / "manifeste-lanceur-fin.json"
    m.unlink()
    Path(str(m) + ".sha256").unlink()
    O.ecrire_scelle(m, json.dumps({"code": 0, "pour_l_attestation": {"fiches_validees_sha256": O.sha256_fichier(pf)}}))
    O.verifier_fiches_de_run(rac, pf)
    with pytest.raises(O.Refus, match="manifeste des envois"):
        classer(env)


# --- v2 : mutations survivantes de la contre-lecture -----------------------------------------------------------------------

def test_L4_jugee_aussi_sur_N(tmp_path):
    env, _ = preparer(tmp_path)
    extra = {id_de("A1"), id_de("A2")}
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "C8"} if (L == "L2" and (p["famille"] == "hasard" or i in extra))
                                        else v, ()))
    r = classer(env)
    assert r["L4"]["R7"]["tient"] and not r["L4"]["N"]["tient"] and not r["L4"]["tient"] and not r["lisible"]
    assert r["L4"]["N"]["kappa"] < 0.4


def test_kappa_au_seuil_exact_tient():
    a = [1] * 10 + [0] * 10
    b = [1] * 7 + [0] * 3 + [1] * 3 + [0] * 7
    k = K.kappa_accord(a, b)
    assert abs(k["kappa"] - 0.4) < 1e-12 and k["jugee_sur"] == "kappa" and k["tient"]
    k = K.kappa_accord([1] * 10, [1] * 8 + [0] * 2)  # accord brut 0,8 exactement, marge constante
    assert k["marge_constante"] and k["tient"]


def test_E5_au_seuil_exact(tmp_path):
    occ = {id_de(n) for n in ("A2", "A3", "A7")}
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "C10"} if i in occ else ({**v, "R7": 0} if i == id_de("A8")
                                                                               else v), ()))
    r = classer(env)
    st = r["classement"]["statut"]
    passees = [i for i in st if st[i]["statut"] in ("neuve", "occupee")]
    assert len(passees) == 5 and sum(st[i]["statut"] == "occupee" for i in passees) == 4
    assert r["echecs"]["E5"] is False  # 4/5 = 80 % : pas « plus de 80 % »
    env2, _ = preparer(tmp_path / "b")
    lire(env2, modif=lambda L, i, p, v: ({**v, "N": "C10"} if (i in occ or i == id_de("A1"))
                                         else ({**v, "R7": 0} if i == id_de("A8") else v), ()))
    assert classer(env2)["echecs"]["E5"] is True


def test_comparaisons_descriptives_bilaterales(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R1": 0} if p["origine"] == "reelle" else v, ()))
    r = classer(env)
    d = next(x for x in r["descriptif_holm"] if x["critere"] == "R1")
    assert d["difference"] == -1.0 and d["p_brute"] < 0.001


def test_audit_declenche_par_un_seul_signe(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R7": 1} if p["famille"] == "hasard" else
                                        ({**v, "N": "aucune"} if i == "T-FA" else v), ()))
    r = classer(env)
    a = r["audit_proprete"]
    signes = [a[k] for k in ("lisibilite_parfaite", "kappa_1", "toutes_publiees_reconnues",
                             "aucune_idee_au_hasard_passee")]
    assert a["declenche"] and 0 < sum(signes) < 4


def test_typographie_du_passage_non_toleree():
    cat = O.entrees_catalogue(O.lire_piece(RACINE, "catalogue")[0])
    vue, _ = O.vue_lecteur(fiche("Z", "propa", 1, 1, "levier:cout"))
    assert 'sans rien d\'autre " Z ".' in vue["enonce"]  # « Z » servi " Z " (typographie de l'orchestrateur)
    juste = {"valeur": 1, "passage": 'décrite ici, sans rien d\'autre " Z ".'}
    faux = {"valeur": 1, "passage": "décrite ici, sans rien d’autre « Z »."}
    assert O.verifier_entree({"R1": juste}, vue, False, cat)["R1"]["compte"] == 1
    assert O.verifier_entree({"R1": faux}, vue, False, cat)["R1"]["compte"] == 0


def test_L2_detail_porte_la_valeur_brute(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R3": 1}, ("R3",)) if i == "T-F53" else (v, ()))
    r = classer(env)
    d = r["L2"]["par_temoin"]["T-F53"]
    assert d["L1"] == 0 and d["L2"] == 0 and d["brut"] == {"L1": 1, "L2": 1} and r["L2"]["tient"]


# --- v2 : variante « désignation détachée de L5 », préparée, non active ----------------------------------------------------

def classer_variante(env, decision="R-9999"):
    return K.classement(env, env.parent, designation="detachee-v1", decision=decision)[0]


def test_variante_refusee_sans_mot(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env)
    for dec in (None, "", "oui", "R-", "R-12 et plus"):
        with pytest.raises(O.Refus):
            classer_variante(env, dec)
    with pytest.raises(O.Refus):
        K.classement(env, env.parent, designation="autre")


def test_variante_cas_sain_separation_demontree(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env)
    r0, r = classer(env), classer_variante(env)
    assert r["designees"] == r0["designees"] and len(r["designees"]) == 2
    assert r["variante_detachee"]["mention"].startswith("séparation démontrée") and r["regle_de_designation"] == "detachee-v1"
    assert r["variante_detachee"]["decision"] == "R-9999" and r["variante_detachee"]["max_C_hasard"] == 0


def test_variante_sans_L5_separation_non_demontree(tmp_path):
    env, _ = preparer(tmp_path)
    a2, a7, a1 = id_de("A2"), id_de("A7"), id_de("A1")

    def m(L, i, p, v):
        if L == "L2" and i == a2:
            v["R7"] = 0
        if L == "L2" and i == a7:
            v["N"] = "C4"
        if L == "L1" and i == a1:
            v["R5"] = 0
        return v, ()
    lire(env, modif=m)
    r0, r = classer(env), classer_variante(env)
    assert r0["designees"] == [] and not r0["L5"]["rejet"]
    assert r["designees"] == r0["classement"]["deux_premieres"] and len(r["designees"]) == 2
    assert "non démontrée" in r["verdict"] and r["echecs"]["E3"] and not r["echecs"]["E4"]


def test_variante_une_neuve_E4_atteignable(tmp_path):
    env, _ = preparer(tmp_path)
    garde = id_de("A1")
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "C10"} if (p["origine"] == "reelle" and i != garde) else v, ()))
    r = classer_variante(env)
    assert r["designees"] == [garde] and r["echecs"]["E4"] and "E4" in r["verdict"]


def test_variante_hasard_aussi_haut_aucune_designee(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R7": 1} if p["famille"] == "hasard" else v, ()))
    r = classer_variante(env)
    assert r["variante_detachee"]["max_C_hasard"] == 5 and r["designees"] == []  # 5 n'est pas > 5


def test_variante_en_ligne_de_commande_exige_le_mot(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env)
    py = [sys.executable, "-I", "-B", str(MODS / "classer_conception_propre_v2.py"), "--envois", str(env),
          "--racine", str(env.parent)]
    c = subprocess.run(py + ["--sortie", str(tmp_path / "s1"), "--designation", "detachee-v1"], capture_output=True,
                       text=True)
    assert c.returncode == 2 and "Lazar" in c.stderr and not (tmp_path / "s1").exists()
    c = subprocess.run(py + ["--sortie", str(tmp_path / "s2"), "--designation", "detachee-v1", "--decision", "R-9999"],
                       capture_output=True, text=True)
    assert c.returncode == 0, c.stderr
    md = (tmp_path / "s2" / "classement-v2.md").read_text(encoding="utf-8")
    assert "detachee-v1 (décision R-9999)" in md
