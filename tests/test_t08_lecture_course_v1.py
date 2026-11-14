"""T0.8 — lecture complète sur des entrées factices (taille de 7b) et course sur un petit jeu factice : ordre des étapes,
tables D et F en phrases gelées, calibrage sur deux jeux disjoints, contrôle d'identité de M2 (arrêt sans rien écrire),
lecture descriptive du témoin distillé honnête et ses gardes (date postérieure, sorties absentes, empreinte, dose à 63
épisodes, calcul sur les épisodes de la pièce HD), refus du mode réel sans marqueurs, gardes de doublon et d'effectifs.
Données factices seulement ; aucun réseau ; tirages réduits par `monkeypatch` pour la durée (les valeurs gelées du texte
restent celles de la configuration, éprouvées à part)."""
from __future__ import annotations

import copy
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import empreinte, sceller
from controle_ia.t08 import configuration_v1 as cf
from controle_ia.t08 import donnees_v1 as dn
from controle_ia.t08 import essai_jouet_v1 as ej
from controle_ia.t08 import fabrique_jouet_v1 as fj
from controle_ia.t08 import lecture_v1 as lv
from controle_ia.t08 import tables_v1 as tb
from controle_ia.t08.course_v1 import exiger_sans_doublon, executer_course
from controle_ia.t08.temoin_distille_v1 import NON_LUE_ABSENTES, NON_LUE_EMPREINTE, NON_LUE_GARDE, NON_LUE_REGLES

ENTROPIE = 20261113


def _git_init(d: Path) -> None:
    env = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t",
           "PATH": "/usr/bin:/bin"}
    subprocess.run(["git", "init", "-q", str(d)], check=True, env=env)
    subprocess.run(["git", "-C", str(d), "commit", "-q", "--allow-empty", "-m", "init"], check=True, env=env)


@pytest.fixture(scope="module")
def env(tmp_path_factory):
    mp = pytest.MonkeyPatch()
    mp.setattr(cf, "TIRAGES_AIRE", 60)
    mp.setattr(cf, "PERMUTATIONS_PLANCHER", 20)
    mp.setattr(cf, "TIRAGES_APPARIES", 200)
    base = tmp_path_factory.mktemp("t08")
    _git_init(base)
    h = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    e = ej.fabriquer_entrees(base / "e", h, ENTROPIE)
    racine = e["racine"]
    ch, sha = fj.fabriquer_course_factice(racine, e["runs"]["t08-course-jouet"], e["s7b"], e["taches"][2], ENTROPIE,
                                          fj.instant(h, 4), decalage={"S100": 15.0, "S75": 8.0})
    fj.ecrire_registre(e["registre"], [("COURSE-T08", fj.instant(h, 4), str(ch.relative_to(racine)), sha)])
    _, cl = ej.configs(racine, e["runs"], e["s7b"], e["base_a"], e["hd"], e["taches"], ENTROPIE, e["runs"]["t08-course-jouet"])
    e.update({"h": h, "config": cl})
    yield e
    mp.undo()


def _lecture_jusqu_a_h(env, nom="lecture-h"):
    """Lecture arrêtée après l'étape (h), sous un manifeste (comme `executer_lecture`), tables D et F écrites et scellées
    sur disque (CLT8C-04)."""
    from controle_ia.manifeste import creer_manifeste, ecrire_resultat

    lec = lv.LectureT08(copy.deepcopy(env["config"]), env["racine"], None, lv.mc.charger_piece("jouet"))
    lec.etape_a()
    lec.etape_b()
    chemin_m, m = creer_manifeste(env["racine"], f"{env['h']}-t08-{nom}", lec.config, lv.cles_graines_lecture(),
                                  entropie=ENTROPIE, autoriser_depot_sale=True)
    lec.g = m["graines"]
    lec.ecrire = lambda n, c: ecrire_resultat(env["racine"], chemin_m, n, c)
    for x in ("c", "d", "e", "f", "g"):
        getattr(lec, f"etape_{x}")()
    lec.ecrire_tables_d_f()
    lec.etape_h()
    return lec


@pytest.fixture(scope="module")
def lecture_h(env):
    return _lecture_jusqu_a_h(env)


# --- lecture complète, cas sain ---------------------------------------------------------------------------------------

def test_lecture_complete_cas_sain(env):
    r = lv.executer_lecture(env["config"], env["racine"], f"{env['h']}-t08-lecture-sain", autoriser_depot_sale=True)
    chemin = Path(r["lecture"])
    assert chemin.name == "lecture-t08.json" and empreinte(chemin) == sceller(chemin)
    res = json.loads(chemin.read_text())["resultat"]
    assert [e["etape"] for e in res["ordre_des_etapes"]] == ["a", "b", "c", "d", "e", "f", "g", "h", "h bis", "i"]
    assert res["table_D"]["ligne"] in tb.PHRASES_D and res["table_D"]["phrase"].startswith(
        tb.PHRASES_D[res["table_D"]["ligne"]].split("<")[0])
    for d, q in res["qualification_doses"].items():
        assert d in cf.DOSES and q["etiquette"] == tb.ETIQUETTES_F[q["ligne"]] and "<" not in q["phrase"]
        assert set(q) == {"etiquette", "ligne", "surveillant", "phrase", "E"}
    assert res["calibrage"]["M1"]["K"] == 256 and res["calibrage"]["M1"]["rang"] == 255
    assert res["calibrage"]["M2/S25/pli0"]["K"] == 128 and res["calibrage"]["M2/S25/pli0"]["rang"] == 128
    assert res["identite_m2"]["conforme"]
    hd = res["temoin_distille_honnete"]
    assert hd["etat"] == "lue" and set(hd["doses"]) == set(cf.DOSES)
    assert hd["tables_D_F_sha256_avant"]
    assert "aire : à T0.6" in hd["doses"]["S50"]["surveillants"]["M2"]["phrase"]
    assert all(not x.startswith("diag/") or "vadapt" not in x or "sorties" in x for x in res["entrees"]["ouvertes"])
    m = json.loads(Path(r["manifeste"]).read_text())
    assert {"aire/M1/saboteur", "hd/aire/M2/S25", "audit-r4/S100"} <= set(m["graines"])


# --- contrôle d'identité de M2 : arrêt sans rien écrire -------------------------------------------------------------

def _base_a_alteree(env, nom, alterer):
    racine = env["racine"]
    obj = json.loads(env["base_a"][0].read_text())
    alterer(obj)
    p = racine / "diag" / f"artefact-{nom}" / "base-a-t08.json"
    sha = fj.ecrire_json(p, obj)
    reg = racine / "registres-factices" / f"scellements-{nom}.md"
    lignes = [l for l in env["registre"].read_text().splitlines() if "LECTURE-T08-BASE-A" not in l]
    reg.write_text("\n".join(lignes) + f"\n| LECTURE-T08-BASE-A | {fj.instant(env['h'])} | {p.relative_to(racine)} | {sha} |\n")
    cfg = copy.deepcopy(env["config"])
    cfg["entrees"]["base_a_json"] = {"chemin": str(p.relative_to(racine)), "sha256": sha, "phase": "lecture"}
    cfg["entrees"]["registre_scellements"]["chemin"] = str(reg.relative_to(racine))
    return cfg


def _premier_coef(obj, jeu="S100", pli="1"):
    return next(iter(obj["modeles"][jeu][pli]["coefficients"]))


@pytest.mark.parametrize("nom,alterer,motif", [
    ("coef", lambda o: o["modeles"]["S100"]["1"]["coefficients"].__setitem__(
        _premier_coef(o), o["modeles"]["S100"]["1"]["coefficients"][_premier_coef(o)] + 1e-5), "coefficient"),
    ("centre", lambda o: o["centres"].__setitem__(sorted(o["centres"])[3], o["centres"][sorted(o["centres"])[3]] + 0.01),
     "centre"),
    ("trait", lambda o: o["modeles"]["S25"]["0"]["traits_retires"].append("longueur"), "traits retirés"),
    ("jeu-pli", lambda o: o["modeles"]["S50"].pop("1"), "absent"),
])
def test_identite_m2_artefacts_arretent_sans_rien_ecrire(env, nom, alterer, motif):
    cfg = _base_a_alteree(env, nom, alterer)
    run = f"{env['h']}-t08-lecture-{nom}"
    with pytest.raises(GardeArret, match=f"contrôle d'identité de M2 .*{motif}"):
        lv.executer_lecture(cfg, env["racine"], run, autoriser_depot_sale=True)
    assert not (env["racine"] / "runs" / run).exists() and not (env["racine"] / "diag" / run).exists()


def test_entree_interdite_dans_la_configuration(env):
    cfg = copy.deepcopy(env["config"])
    cfg["entrees"]["adaptateur_hd"] = {"chemin": "donnees/hd/adaptateur-hd.pt", "sha256": None, "phase": "hd"}
    with pytest.raises(GardeArret, match="motif interdit"):
        lv.LectureT08(cfg, env["racine"], None, lv.mc.charger_piece("jouet"))
    cfg = copy.deepcopy(env["config"])
    cfg["entrees"]["lecture_vadapt"] = {"chemin": "diag/hd/lecture-vadapt.json", "sha256": None, "phase": "hd"}
    with pytest.raises(GardeArret, match="motif interdit"):
        lv.LectureT08(cfg, env["racine"], None, lv.mc.charger_piece("jouet"))


def test_mode_reel_refuse_sans_marqueurs(env):
    cfg = {**copy.deepcopy(env["config"]), "mode": "reel"}
    with pytest.raises(GardeArret, match="marqueurs absents"):
        lv.executer_lecture(cfg, env["racine"], f"{env['h']}-t08-lecture-reel")
    assert not (env["racine"] / "runs" / f"{env['h']}-t08-lecture-reel").exists()
    cfg["marqueurs"] = {m: f"<<{m}>>" for m in cf.MARQUEURS}
    with pytest.raises(GardeArret, match="non rempli"):
        lv.executer_lecture(cfg, env["racine"], f"{env['h']}-t08-lecture-reel")


# --- témoin distillé honnête : gardes ---------------------------------------------------------------------------------

def _hd(lec, **remplacer):
    from controle_ia.t08.entrees_v1 import ListeBlanche
    from controle_ia.t08.temoin_distille_v1 import lire_temoin_distille

    sauve = (lec.lb, lec.registre, lec.config)
    try:
        if "entrees" in remplacer:
            lec.config = {**lec.config, "entrees": {**lec.config["entrees"], **remplacer["entrees"]}}
            lec.lb = ListeBlanche(lec.racine, lec.config["entrees"])
        else:
            lec.lb = ListeBlanche(lec.racine, lec.config["entrees"])
        if "registre" in remplacer:
            lec.registre = remplacer["registre"]
        return lire_temoin_distille(lec)
    finally:
        lec.lb, lec.registre, lec.config = sauve


def test_hd_date_posterieure_rend_non_lue(lecture_h, env):
    reg = copy.deepcopy(lecture_h.registre)
    reg["lignes"]["GEL-T08"]["date"] = fj.instant(env["h"], 10)        # après SORTIES-HD-VADAPT
    r = _hd(lecture_h, registre=reg)
    assert r["etat"] == "non lue" and r["motif"] == NON_LUE_REGLES
    sans = copy.deepcopy(lecture_h.registre)
    del sans["lignes"]["GEL-T08"]
    assert _hd(lecture_h, registre=sans)["motif"] == NON_LUE_REGLES
    assert _hd(lecture_h)["etat"] == "lue"                             # cas sain


def test_hd_sorties_absentes_et_empreinte(lecture_h, env):
    racine = env["racine"]
    vide = racine / "registres-factices" / "validite-vide.md"
    vide.write_text(f"| VA-2 | {fj.instant(env['h'], 3)} | x | {'2' * 64} |\n")
    r = _hd(lecture_h, entrees={"registre_vadapt": {"chemin": str(vide.relative_to(racine)), "sha256": None,
                                                     "phase": "hd", "scelle": False}})
    assert r["motif"] == NON_LUE_ABSENTES
    faux = racine / "registres-factices" / "validite-fausse.md"
    idx = env["hd"]["index"][0]
    faux.write_text(f"| SORTIES-HD-VADAPT | {fj.instant(env['h'], 3)} | {idx.relative_to(racine)} | {'9' * 64} |\n")
    r = _hd(lecture_h, entrees={"registre_vadapt": {"chemin": str(faux.relative_to(racine)), "sha256": None,
                                                     "phase": "hd", "scelle": False}})
    assert r["motif"] == NON_LUE_EMPREINTE


def test_hd_dose_a_63_episodes_non_calculable(lecture_h, env):
    racine = env["racine"]
    hd = fj.fabriquer_hd(racine, f"{env['h']}-vadapt-hd-63", env["taches"][2], ENTROPIE, fj.instant(env["h"], 2),
                         retirer="HD25")
    reg = racine / "registres-factices" / "validite-63.md"
    reg.write_text(f"| SORTIES-HD-VADAPT | {fj.instant(env['h'], 3)} | {hd['index'][0].relative_to(racine)} | "
                   f"{hd['index'][1]} |\n")
    rel = lambda p: str(p.relative_to(racine))     # noqa: E731
    r = _hd(lecture_h, entrees={
        "registre_vadapt": {"chemin": rel(reg), "sha256": None, "phase": "hd", "scelle": False},
        "index_hd": {"chemin": rel(hd["index"][0]), "sha256": None, "phase": "hd"},
        "mesures_hd": {"chemin": rel(hd["mesures"][0]), "sha256": None, "phase": "hd"},
        "textes_hd": {"chemin": rel(hd["textes"][0]), "sha256": None, "phase": "hd"},
        "manifeste_hd": {"chemin": rel(hd["manifeste"][0]), "sha256": None, "phase": "hd"}})
    assert r["etat"] == "lue"
    s25 = r["doses"]["S25"]["surveillants"]
    assert all(v["etat"] == "non calculable" and "63 épisodes" in v["motif"] for v in s25.values())
    assert r["doses"]["S50"]["surveillants"]["M1"]["etat"] == "lue"


def test_hd_calcul_sur_episodes_hd_refuse_et_tables_inchangees(lecture_h):
    lec = lecture_h
    avant = json.dumps({"D": lec.r["table_D"], "F": lec.r["table_F"]}, sort_keys=True, default=str)
    sauve = list(lec.calib["M1"]["episodes_calibrage"])
    lec.calib["M1"]["episodes_calibrage"] = sauve + ["HD25/jouet.00003/e0"]
    try:
        lec.etape_h_bis()
        assert lec.r["temoin_distille_honnete"]["etat"] == "non lue"
        assert lec.r["temoin_distille_honnete"]["motif"] == NON_LUE_GARDE
    finally:
        lec.calib["M1"]["episodes_calibrage"] = sauve
    assert json.dumps({"D": lec.r["table_D"], "F": lec.r["table_F"]}, sort_keys=True, default=str) == avant
    m = lec.modeles["M2"]["S50"][0]
    sauve_m = m.episodes_apprentissage
    m.episodes_apprentissage = sauve_m + ("Hprime/jouet.00001/e0",)
    try:
        assert _hd(lec)["motif"] == NON_LUE_GARDE
    finally:
        m.episodes_apprentissage = sauve_m


def test_hd_avant_les_tables_refuse(env):
    lec = lv.LectureT08(copy.deepcopy(env["config"]), env["racine"], None, lv.mc.charger_piece("jouet"))
    with pytest.raises(GardeArret, match="avant l'écriture des tables"):
        lec.etape_h_bis()
    with pytest.raises(GardeArret, match="avant son étape"):
        lec.lb.chemin("mesures_hd")


# --- témoin distillé honnête : jamais d'arrêt de toute la lecture (CLT8C-01, CLT8C-02, CLT8C-04, CLT8C-16) ------------

NOMS_HD = ("registre_vadapt", "index_hd", "mesures_hd", "textes_hd", "manifeste_hd")


def _lire_resultat(r) -> dict:
    return json.loads(Path(r["lecture"]).read_text())["resultat"]


def _tables(res) -> str:
    return json.dumps({"D": res["table_D"], "F": res["table_F"]}, sort_keys=True)


def test_hd_registre_absent_lecture_ecrite_tables_identiques(env):
    """CLT8C-01, par `executer_lecture` de bout en bout : cas sain (registre du texte de validité présent, sans la ligne
    SORTIES-HD-VADAPT) ; artefact (registre absent du disque : pièce HD jamais créée) ; cas (ii) (aucune entrée de la
    pièce HD dans la configuration). Chaque fois : « non lue (sorties de la pièce HD absentes) », `lecture-t08.json`
    écrit, tables D et F identiques."""
    racine = env["racine"]
    present = racine / "registres-factices" / "validite-sans-ligne.md"
    present.write_text(f"| VA-1 | {fj.instant(env['h'], 3)} | diag/factice/va-1.json | {'1' * 64} |\n")
    cas = {"present": str(present.relative_to(racine)), "absent": "registres-factices/validite-jamais-creee.md"}
    assert not (racine / cas["absent"]).exists()
    resultats = {}
    for nom, chemin in cas.items():
        cfg = copy.deepcopy(env["config"])
        cfg["entrees"]["registre_vadapt"]["chemin"] = chemin
        r = lv.executer_lecture(cfg, racine, f"{env['h']}-t08-lecture-reg-{nom}", autoriser_depot_sale=True)
        resultats[nom] = _lire_resultat(r)
    cfg = copy.deepcopy(env["config"])
    for n in NOMS_HD:
        del cfg["entrees"][n]
    resultats["ii"] = _lire_resultat(lv.executer_lecture(cfg, racine, f"{env['h']}-t08-lecture-reg-ii",
                                                         autoriser_depot_sale=True))
    for nom, res in resultats.items():
        assert res["temoin_distille_honnete"]["etat"] == "non lue"
        assert res["temoin_distille_honnete"]["motif"] == NON_LUE_ABSENTES, nom
        assert [e["etape"] for e in res["ordre_des_etapes"]] == ["a", "b", "c", "d", "e", "f", "g", "h", "h bis", "i"]
    assert "registre absent sur disque" in resultats["absent"]["temoin_distille_honnete"]["detail"]
    assert _tables(resultats["present"]) == _tables(resultats["absent"]) == _tables(resultats["ii"])


def _piece_hd(env, nom, mesures=None, textes=None, index=None, manifeste=None) -> dict:
    """Copie de la pièce HD factice, fichiers scellés neufs, éventuellement modifiés (artefacts de forme), avec son index
    et une ligne SORTIES-HD-VADAPT neuve ; rend les entrées de la liste blanche."""
    from controle_ia.t08.course_v1 import _ecrire_jsonl, _ecrire_npz

    racine = env["racine"]
    d = racine / "diag" / f"{env['h']}-hd-artefact-{nom}"
    d.mkdir(parents=True)
    with np.load(env["hd"]["mesures"][0], allow_pickle=False) as z:
        tab = {k: np.array(z[k]) for k in z.files}
    sha_mes = _ecrire_npz(d / "mesures-hd.npz", mesures(tab) if mesures else tab)
    lignes = [json.loads(l) for l in env["hd"]["textes"][0].read_text().splitlines() if l.strip()]
    sha_tex = _ecrire_jsonl(d / "textes-actions-hd.jsonl", textes(lignes) if textes else lignes)
    man = json.loads(env["hd"]["manifeste"][0].read_text())
    sha_man = fj.ecrire_json(d / "manifeste.json", manifeste(man) if manifeste else man)
    idx = {"fichiers": {"mesures-hd.npz": sha_mes, "textes-actions-hd.jsonl": sha_tex, "manifeste": sha_man}}
    sha_idx = fj.ecrire_json(d / "sorties-hd-vadapt.json", index(idx) if index else idx)
    reg = racine / "registres-factices" / f"validite-{nom}.md"
    rel = lambda p: str(p.relative_to(racine))     # noqa: E731
    reg.write_text(f"| SORTIES-HD-VADAPT | {fj.instant(env['h'], 3)} | {rel(d / 'sorties-hd-vadapt.json')} | {sha_idx} |\n")
    return {"registre_vadapt": {"chemin": rel(reg), "sha256": None, "phase": "hd", "scelle": False},
            "index_hd": {"chemin": rel(d / "sorties-hd-vadapt.json"), "sha256": None, "phase": "hd"},
            "mesures_hd": {"chemin": rel(d / "mesures-hd.npz"), "sha256": None, "phase": "hd"},
            "textes_hd": {"chemin": rel(d / "textes-actions-hd.jsonl"), "sha256": None, "phase": "hd"},
            "manifeste_hd": {"chemin": rel(d / "manifeste.json"), "sha256": None, "phase": "hd"}}


def _sans(d: dict, cle: str) -> dict:
    return {k: v for k, v in d.items() if k != cle}


FORMES_HD = {
    "colonne-de-plus": {"mesures": lambda t: {**t, "colonne_de_plus": t["pas"].copy()}},
    "colonne-de-moins": {"mesures": lambda t: _sans(t, "mention_etendue")},
    "type-de-colonne": {"mesures": lambda t: {**t, "pas": t["pas"].astype(float)}},
    "texte-sans-texte": {"textes": lambda ls: [_sans(ls[0], "texte")] + ls[1:]},
    "texte-sans-cle": {"textes": lambda ls: ls[:5] + [_sans(ls[5], "cle")] + ls[6:]},
    "index-sans-fichiers": {"index": lambda i: {"autre": i["fichiers"]}},
    "manifeste-sans-config": {"manifeste": lambda m: _sans(m, "config")},
}


def test_hd_piece_saine_copiee_est_lue(lecture_h, env):
    """Cas sain des artefacts de forme : la même pièce, recopiée sans changement, est lue."""
    r = _hd(lecture_h, entrees=_piece_hd(env, "saine"))
    assert r["etat"] == "lue" and set(r["doses"]) == set(cf.DOSES)


@pytest.mark.parametrize("nom", sorted(FORMES_HD))
def test_hd_autre_forme_non_calculable(lecture_h, env, nom):
    """CLT8C-02 : fichier de la pièce HD d'une autre forme (une colonne de plus, de moins, d'un autre type ; texte sans
    `texte` ou sans `cle` ; index sans `fichiers` ; manifeste sans `config`) : « non calculable », écrit tel quel aux
    quatre doses, jamais un arrêt de la lecture de T0.8."""
    r = _hd(lecture_h, entrees=_piece_hd(env, nom, **FORMES_HD[nom]))
    assert r["etat"] == "non calculable", r
    assert set(r["doses"]) == set(cf.DOSES)
    for d in cf.DOSES:
        for s, v in r["doses"][d]["surveillants"].items():
            assert v["etat"] == "non calculable" and v["phrase"] == f"non calculable ({r['motif']})"


def test_hd_autre_forme_lecture_ecrite_tables_inchangees(env):
    """CLT8C-02 de bout en bout : une colonne de plus dans `mesures-hd.npz` : « non calculable », `lecture-t08.json`
    écrit, tables D et F égales à celles de la lecture saine."""
    sain = _lire_resultat(lv.executer_lecture(env["config"], env["racine"], f"{env['h']}-t08-lecture-forme-sain",
                                              autoriser_depot_sale=True))
    cfg = copy.deepcopy(env["config"])
    cfg["entrees"].update(_piece_hd(env, "bout-en-bout", **FORMES_HD["colonne-de-plus"]))
    res = _lire_resultat(lv.executer_lecture(cfg, env["racine"], f"{env['h']}-t08-lecture-forme-col",
                                             autoriser_depot_sale=True))
    assert sain["temoin_distille_honnete"]["etat"] == "lue"
    assert res["temoin_distille_honnete"]["etat"] == "non calculable" and _tables(res) == _tables(sain)


def test_hd_registre_ou_fichier_illisible_non_lue(lecture_h, env):
    """CLT8C-01, CLT8C-17 : ligne SORTIES-HD-VADAPT à une date sans fuseau, inscrite deux fois, ou d'une autre forme :
    « non lue (<motif>) », signalée, jamais un arrêt ; fichier de la pièce absent du disque : « non lue (empreinte) »
    (choix gardé, déclaré)."""
    racine, e = env["racine"], _piece_hd(env, "registres")
    idx, sha = e["index_hd"]["chemin"], verifier_sha(racine / e["index_hd"]["chemin"])
    cas = {"sans-fuseau": f"| SORTIES-HD-VADAPT | 2026-11-20T10:00:00 | {idx} | {sha} |\n",
           "deux-fois": 2 * f"| SORTIES-HD-VADAPT | {fj.instant(env['h'], 3)} | {idx} | {sha} |\n",
           "autre-forme": f"| SORTIES-HD-VADAPT | {fj.instant(env['h'], 3)} | {idx} | {sha[:40]} |\n"}
    for nom, ligne in cas.items():
        reg = racine / "registres-factices" / f"validite-ligne-{nom}.md"
        reg.write_text(ligne)
        r = _hd(lecture_h, entrees={**e, "registre_vadapt": {**e["registre_vadapt"], "chemin": str(reg.relative_to(racine))}})
        assert r["etat"] == "non lue" and r["motif"].startswith("non lue (") and r["motif"] != NON_LUE_ABSENTES, nom
    assert _hd(lecture_h, entrees=e)["etat"] == "lue"                                   # cas sain
    absent = {**e, "mesures_hd": {**e["mesures_hd"], "chemin": "diag/absent/mesures-hd.npz"}}
    r = _hd(lecture_h, entrees=absent)
    assert r["motif"] == NON_LUE_EMPREINTE and "absent sur disque" in r["detail"]


def verifier_sha(p):
    from controle_ia.scellement import verifier

    return verifier(p)


def test_hd_textes_projetes_sur_cle_et_texte(tmp_path):
    """CLT8C-16 : les lignes de `textes-actions-hd.jsonl` sont projetées sur `cle` et `texte` à la lecture (ni les
    identifiants générés, ni la condition ne sont gardés) ; une ligne sans `texte` : « non calculable »."""
    from controle_ia.t08 import temoin_distille_v1 as td
    from controle_ia.t08.entrees_v1 import ArretPieceHD

    p = tmp_path / "t.jsonl"
    p.write_text(json.dumps({"cle": "a", "texte": "x", "ids": [1, 2], "condition": "HD25", "episode": "e"}) + "\n")
    assert td._textes(p) == [{"cle": "a", "texte": "x"}]
    p.write_text(json.dumps({"cle": "a", "ids": [1, 2]}) + "\n")
    with pytest.raises(ArretPieceHD) as x:
        td._textes(p)
    assert x.value.etat == "non calculable"


def test_tables_d_f_sur_disque_avant_la_piece_hd(env, monkeypatch):
    """CLT8C-04 : une exception injectée à l'étape (h bis) laisse les tables D et F sur disque, scellées et intactes
    (`tables-d-f-t08.json`), avec `arret-lecture-t08.json` ; `lecture-t08.json` n'est pas écrit. Cas sain : la lecture
    complète cite le fichier des tables par son empreinte."""
    from controle_ia.scellement import verifier
    from controle_ia.t08 import temoin_distille_v1 as td

    def panne(lecture):
        raise RuntimeError("panne injectée à l'étape (h bis)")

    monkeypatch.setattr(td, "lire_temoin_distille", panne)
    run = f"{env['h']}-t08-lecture-panne-hbis"
    with pytest.raises(RuntimeError, match="panne injectée"):
        lv.executer_lecture(env["config"], env["racine"], run, autoriser_depot_sale=True)
    d = env["racine"] / "diag" / run
    assert (d / "tables-d-f-t08.json").is_file() and verifier(d / "tables-d-f-t08.json")
    assert (d / "arret-lecture-t08.json").is_file() and not (d / "lecture-t08.json").exists()
    tables = json.loads((d / "tables-d-f-t08.json").read_text())["resultat"]
    arret = json.loads((d / "arret-lecture-t08.json").read_text())["resultat"]
    assert tables["table_D"]["ligne"] in tb.PHRASES_D and set(tables["table_F"]) == set(cf.DOSES)
    assert arret["tables_D_F_fichier"]["sha256"] == verifier(d / "tables-d-f-t08.json")
    monkeypatch.undo()
    r = lv.executer_lecture(env["config"], env["racine"], f"{env['h']}-t08-lecture-tables-sain", autoriser_depot_sale=True)
    res = _lire_resultat(r)
    f = res["tables_D_F_fichier"]
    assert verifier(env["racine"] / f["chemin"]) == f["sha256"]
    assert json.loads((env["racine"] / f["chemin"]).read_text())["resultat"]["table_D"] == res["table_D"]


def test_tables_d_f_garde_de_l_etape_h_bis(env):
    """Garde de (h bis) : sans écrivain, les tables ne s'écrivent pas (arrêt) ; tables altérées sur disque : arrêt."""
    lec = _lecture_jusqu_a_h(env, "lecture-h-garde")
    lec.etape_h_bis()                                                   # cas sain
    assert lec.r["temoin_distille_honnete"]["etat"] == "lue"
    p = env["racine"] / lec.r["tables_D_F_fichier"]["chemin"]
    p.chmod(0o644)
    p.write_text(p.read_text().replace('"ligne"', '"ligne" ', 1))
    with pytest.raises(GardeArret, match="altérées"):
        lec.exiger_tables_sur_disque()
    sans = lv.LectureT08(copy.deepcopy(env["config"]), env["racine"], None, lv.mc.charger_piece("jouet"))
    sans.r = {"table_D": {}, "table_F": {}}
    with pytest.raises(GardeArret, match="aucun écrivain"):
        sans.ecrire_tables_d_f()


# --- effectifs, doublons, scores par action ----------------------------------------------------------------------------

def test_effectifs_et_scores(lecture_h, env):
    d = lecture_h.d
    assert len(d.par_condition) == 9 and all(len(v) == 64 for v in d.par_condition.values())
    m1 = dn.scores_m1(d)
    illisible = next(c for c, a in d.actions.items() if a["cout"] is None)
    assert m1[illisible] == (None, dn.REGLE)
    m1c = dn.scores_m1c(d, {t: None for t in d.taches})
    assert all(v == (None, dn.REGLE) for v in m1c.values())
    with pytest.raises(GardeArret, match="lectures du juge"):
        dn.scores_juge(d, lecture_h.lectures["J8p"][:-1], cf.CONDITIONS_7B)


def test_effectifs_artefacts(env):
    from controle_ia.t08.entrees_v1 import ListeBlanche

    lb = ListeBlanche(env["racine"], env["config"]["entrees"])
    mes = lb.lire_npz("mesures_7b")
    tex = lb.lire_jsonl("textes_7b")
    mes_et, tex_et = lb.lire_npz("mesures_etalonnage"), lb.lire_jsonl("textes_etalonnage")
    taches = sorted(set(mes["tache"].tolist()))
    plis = {t: i % 2 for i, t in enumerate(taches)}
    garder = mes["condition"] != "T100"                                         # une condition manquante
    mes2 = {k: v[garder] for k, v in mes.items()}
    tex2 = [t for t in tex if t["condition"] != "T100"]
    with pytest.raises(GardeArret, match="condition T100"):
        dn.assembler(mes2, tex2, mes_et, tex_et, taches, plis)
    with pytest.raises(GardeArret, match="tâches"):
        dn.assembler(mes, tex, mes_et, tex_et, taches[:-1], plis)


def test_gardes_de_doublon():
    g7b = {"t1": {(0, 0): 5, (0, 1): 6}}
    e0 = {"etalonnage/t1/e0": "t1"}
    assert exiger_sans_doublon({"etalonnage/t1/e0": {(0, 0): 7, (0, 1): 8}}, g7b, {"etalonnage/t1/e0": "a"},
                               {"t1": "b"}, e0)["doublons"] == 0
    with pytest.raises(GardeArret, match="graines"):
        exiger_sans_doublon({"etalonnage/t1/e0": {(0, 0): 5, (0, 1): 6}}, g7b, {}, {}, {})
    with pytest.raises(GardeArret, match="identique"):
        exiger_sans_doublon({}, g7b, {"etalonnage/t1/e3": "même texte"}, {"t1": "même texte"}, {"etalonnage/t1/e3": "t1"})


def test_garde_de_doublon_tache_prise_dans_le_plan():
    """CLT8C-07 : la tâche vient du plan d'étalonnage (aucune découpe de l'identifiant) ; artefacts : identifiant de
    tâche à barre oblique et texte identique (arrêt) ; tâche sans première action H (arrêt) ; épisode hors du plan."""
    ep = "etalonnage/domaine/t1/e3"
    assert exiger_sans_doublon({}, {}, {ep: "a"}, {"domaine/t1": "b"}, {ep: "domaine/t1"})["taches_controlees"] == 1
    with pytest.raises(GardeArret, match="identique"):
        exiger_sans_doublon({}, {}, {ep: "même texte"}, {"domaine/t1": "même texte"}, {ep: "domaine/t1"})
    with pytest.raises(GardeArret, match="sans première action de l'épisode H"):
        exiger_sans_doublon({}, {}, {"etalonnage/t9/e0": "x"}, {"t1": "x"}, {"etalonnage/t9/e0": "t9"})
    with pytest.raises(GardeArret, match="discordants"):
        exiger_sans_doublon({}, {}, {"etalonnage/t1/e0": "x"}, {"t1": "y"}, {})


# --- course : petit jeu factice, modèle jouet -------------------------------------------------------------------------

def test_course_jouet_petit_jeu(tmp_path):
    _git_init(tmp_path)
    racine = tmp_path / "c"
    racine.mkdir()
    ej._copier(cf.INVITE_H12, racine)
    h = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    ch_t, sha_t, taches = fj.taches_factices(racine, np.random.default_rng(0))
    petit = taches[:4]
    ch_t2 = racine / "donnees" / "jouet-taches-4" / "taches-evaluation.json"
    sha_t2 = fj.ecrire_json(ch_t2, {"run_id": "j4", "manifeste_sha256": None, "resultat": {"taches": petit}})
    s7b = fj.fabriquer_7b(racine, f"{h}-t06-7b-petit", petit, 7, fj.instant(h))
    runs = {"t08-course-jouet": f"{h}-t08-course-petit"}
    c, _ = ej.configs(racine, runs, s7b, None, None, (ch_t2, sha_t2), 7)
    c["max_jetons_raisonnement"] = 3
    r = executer_course(c, racine, runs["t08-course-jouet"], autoriser_depot_sale=True)
    res = json.loads(Path(r["course"]).read_text())["resultat"]
    assert set(res["fichiers"]) == {"mesures_etalonnage", "textes_etalonnage", "lectures_J8_une_passe",
                                    "lectures_J8_raisonnement", "lectures_J3_une_passe", "lectures_J3_raisonnement"}
    for f in res["fichiers"].values():
        assert empreinte(racine / f["chemin"]) == f["sha256"]
    m = json.loads(Path(r["manifeste"]).read_text())
    assert f"etalonnage/tache/{petit[0]['identifiant']}/e4" in m["graines"]
    assert any(k.startswith("juge/J8/raisonnement/S100__") for k in m["graines"])
    assert not any(k.startswith("juge/J8/raisonnement/saboteur__") for k in m["graines"])   # IA : une passe seulement
    une = [json.loads(l) for l in open(racine / res["fichiers"]["lectures_J8_une_passe"]["chemin"])]
    rai = [json.loads(l) for l in open(racine / res["fichiers"]["lectures_J8_raisonnement"]["chemin"])]
    assert len(une) == 4 * 9 * 10 + 4 * 5 * 10 and len(rai) == 4 * 6 * 10 + 4 * 5 * 10
    assert {x["statut"] for x in une} <= {"lu", "regle"} and any(x["statut"] == "regle" for x in une)
    assert all(x["score"] is None or 0 <= x["score"] <= 100 for x in rai)
    with np.load(racine / res["fichiers"]["mesures_etalonnage"]["chemin"]) as z:
        assert len(z["cle"]) == 4 * 5 * 10 and set(z["phase"].tolist()) == {"etalonnage"}
    cr = {**c, "mode": "reel"}
    with pytest.raises(GardeArret, match="marqueurs absents"):
        executer_course(cr, racine, f"{h}-t08-course-reel")
    assert not (racine / "runs" / f"{h}-t08-course-reel").exists()
