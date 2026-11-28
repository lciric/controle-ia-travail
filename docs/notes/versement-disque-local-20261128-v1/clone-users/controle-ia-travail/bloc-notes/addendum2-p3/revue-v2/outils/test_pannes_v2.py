"""Pannes (point C) de la contre-lecture du code v2 : entrées absentes, NaN, infini, table modifiée pendant l'analyse,
arbre de travail non propre. Tables synthétiques et dépôts jouets seulement (aides et fixtures de la copie de base des
tests v2, importées sans copie). Chaque essai dit ce que fait le module : arrêt écrit, ou passage.
"""
import copy
import json
import sys
from pathlib import Path

import numpy as np
import pytest

BASE = Path(__file__).resolve().parents[1] / "base"
sys.path.insert(0, str(BASE))
import test_audit_verdict_p3_v1 as T  # noqa: E402
from test_audit_verdict_p3_v1 import depot_jetable, gabarit, tirages_reduits  # noqa: E402,F401  (fixtures)

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import verifier_resultat  # noqa: E402
from controle_ia.scellement import empreinte, sceller  # noqa: E402

av, P = T.av, T.P


# ------------------------------------------------------------------ entrées absentes
@pytest.mark.parametrize("chemin,motif", [(("P3-P1", "etablie"), "P3-P1/etablie"), (("P3-P2", "calculable"), "P3-P2/calculable"),
                                          (("cout_mention", "taches_exclues"), "cout_mention/taches_exclues"),
                                          (("P3-P3", P[0], "plancher_quantile"), f"P3-P3/{P[0]}/plancher_quantile"),
                                          (("P3-P6", "mention", "actions"), "P3-P6/mention/actions"),
                                          (("principales",), "principales")])
def test_cle_absente_de_la_lecture_arrete(chemin, motif):
    s, lec = T._cas("sain")
    parent = lec
    for k in chemin[:-1]:
        parent = parent[k]
    del parent[chemin[-1]]
    with pytest.raises(GardeArret, match=f"garde [789] : .*{motif.split('/')[-1]}") as e:
        T._addendum(s, lec)
    print("ARRÊT :", str(e.value)[:160])


def test_principales_absentes_des_sondes_figees_arrete():
    s, lec = T._cas("sain")
    del s["sondes-figees"]["principales"]["enjeux"]
    with pytest.raises(Exception) as e:
        T._addendum(s, lec)
    print("ARRÊT :", type(e.value).__name__, str(e.value)[:120])
    assert not isinstance(e.value, AssertionError)


def test_piece_absente_sur_le_depot_arrete_rien_ecrit(depot_jetable):
    d, m, _ = depot_jetable
    (d / "diag" / T.RUN_A / "sondes-figees.json").unlink()
    with pytest.raises(GardeArret, match=r"garde 2 : \[SF\]"):
        T._lancer(d, m, "20261020-160000-addendum2-p3")
    assert T._rien_ecrit(d, "20261020-160000-addendum2-p3")


# ------------------------------------------------------------------ NaN et infini
@pytest.mark.parametrize("cle,valeur", [("effet", float("nan")), ("bas", float("nan")), ("bas", float("inf")),
                                        ("haut", -float("inf"))])
def test_non_fini_dans_P3_P1_de_la_lecture_arrete(cle, valeur):
    s, lec = T._cas("sain")
    lec["P3-P1"][cle] = valeur
    with pytest.raises(GardeArret, match="garde [79]") as e:
        T._addendum(s, lec)
    print("ARRÊT :", str(e.value)[:160])


@pytest.mark.parametrize("cle", ["aire", "plancher_quantile"])
def test_nan_dans_P3_P3_de_la_lecture_arrete(cle):
    s, lec = T._cas("sain")
    lec["P3-P3"][P[1]][cle] = float("nan")
    with pytest.raises(GardeArret, match=f"garde 7 : P3-P3/{P[1]}"):
        T._addendum(s, lec)


def test_infini_dans_les_couts_du_run_source_lu_comme_illisible():
    """+inf et −inf dans les coûts : illisibles pour le code gelé comme pour le module (cohérence passée), sortie finie."""
    s = T.SCENARIOS["sain"]()
    t = s["tables"]
    i = np.flatnonzero(t["condition"] == "saboteur")[:7]
    t["cout"][i[:4]], t["cout"][i[4:]] = np.inf, -np.inf
    t["cout_groupes_joints"] = t["cout"].copy()
    lec = T._lecture(s)
    o = T._addendum(s, lec)
    sab = o["descriptifs"]["B1"]["saboteur-honnete"]
    assert sab["E_sf"]["comptes_restriction"]["saboteur"]["illisibles_d_origine"] >= 7
    assert o["coherence_avec_la_lecture"]["effets"]["P3-P1"]["ecart"] <= 1e-12
    json.dumps(o, allow_nan=False)


def test_nan_dans_une_colonne_de_forme_du_run_source():
    """Forme en flottant avec NaN (hors du type booléen écrit) : ce que fait le module, sans lecture refaite."""
    s, lec = T._cas("sain")
    t = s["tables"]
    f = t["cout_suffixe_k"].astype(np.float64)
    j = int(np.flatnonzero((t["condition"] == "honnete") & ~t["cout_suffixe_k"].astype(bool))[0])
    f[j] = np.nan
    t["cout_suffixe_k"] = f
    with pytest.raises(GardeArret, match="garde 7 : P3-P6/honnete/cout_suffixe_k") as e:
        T._addendum(s, lec)
    print("ARRÊT :", str(e.value)[:160])


# ------------------------------------------------------------------ table modifiée pendant l'analyse
def test_lecture_modifiee_en_memoire_pendant_l_analyse_arrete(monkeypatch):
    s, lec = T._cas("sain")
    vraie = av.ecarts_de_forme

    def modifie(t, graines):
        lec["P3-P1"]["effet"] += 1.0
        return vraie(t, graines)

    monkeypatch.setattr(av, "ecarts_de_forme", modifie)
    with pytest.raises(GardeArret, match="lecture décisive modifiée pendant l'addendum 2"):
        T._addendum(s, lec)


def test_run_source_modifie_en_memoire_pendant_l_analyse(monkeypatch):
    """Coûts du run source modifiés en mémoire après la garde 7 (ici dans la garde 8) : constat de ce que fait le module."""
    ref = T._sortie("sain")
    s, lec = T._cas("sain")
    vraie = av.exiger_issue_recalculee

    def modifie(lecture):
        vraie(lecture)
        s["tables"]["cout"] *= 2.0

    monkeypatch.setattr(av, "exiger_issue_recalculee", modifie)
    o = T._addendum(s, lec)
    a, b = ref["descriptifs"]["ecarts_de_forme"], o["descriptifs"]["ecarts_de_forme"]
    print("PASSAGE SANS ARRÊT ; E_sf identique :", ref["descriptifs"]["B1"]["saboteur-honnete"]["E_sf"]["effet"]
          == o["descriptifs"]["B1"]["saboteur-honnete"]["E_sf"]["effet"], "; écarts M8 identiques :", a == b)


def test_lecture_modifiee_sur_le_disque_apres_la_garde_3(depot_jetable, monkeypatch):
    """[L] modifiée sur le disque après sa vérification (garde 3), avant les analyses : constat."""
    d, m, _ = depot_jetable
    chemin = d / "diag" / T.LEC_A / "lecture-p3.json"
    vraie = m.exiger_garde_4

    def apres(racine, sha):
        r = vraie(racine, sha)
        chemin.write_bytes(chemin.read_bytes().replace(b'"ligne"', b'"ligne" ', 1))
        return r

    monkeypatch.setattr(m, "exiger_garde_4", apres)
    run = "20261020-161000-addendum2-p3"
    try:
        s = T._lancer(d, m, run)
        print("PASSAGE SANS ARRÊT ; lecture_sha256 de la sortie :", s["lecture_sha256"][:12], "; disque :",
              empreinte(chemin)[:12])
    except GardeArret as e:
        print("ARRÊT :", str(e).splitlines()[0][:160], "; quelque chose d'écrit :", not T._rien_ecrit(d, run))


# ------------------------------------------------------------------ arbre de travail non propre
@pytest.mark.parametrize("quoi", ["fichier suivi hors de l'arbre gelé modifié", "code gelé modifié sans commit",
                                  "fichier non suivi à la racine", "texte de l'addendum 2 modifié sans commit"])
def test_arbre_de_travail_non_propre_rien_ecrit(depot_jetable, quoi):
    d, m, _ = depot_jetable
    if quoi == "fichier suivi hors de l'arbre gelé modifié":
        p = d / "registres" / "decisions.md"
        p.write_text(p.read_text(encoding="utf-8") + "ajout\n", encoding="utf-8")
    elif quoi == "code gelé modifié sans commit":
        p = d / "src" / "controle_ia" / "gardes.py"
        p.write_text(p.read_text(encoding="utf-8") + "\n# modifié\n", encoding="utf-8")
    elif quoi == "fichier non suivi à la racine":
        (d / "brouillon.txt").write_text("x\n", encoding="utf-8")
    else:
        p = d / av.PREREG_ADDENDUM2
        p.write_text(p.read_text(encoding="utf-8") + "\najout\n", encoding="utf-8")
    run = "20261020-162000-addendum2-p3"
    with pytest.raises(GardeArret) as e:
        T._lancer(d, m, run)
    print(f"{quoi} : ARRÊT :", str(e.value).splitlines()[0][:150])
    assert T._rien_ecrit(d, run)
