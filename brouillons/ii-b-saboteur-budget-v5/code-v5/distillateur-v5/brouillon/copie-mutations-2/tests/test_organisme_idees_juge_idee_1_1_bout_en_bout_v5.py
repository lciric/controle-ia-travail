"""Idée 1.1, version 4 (contrôle `02f4a1d7…` : n8, réglage strict ; formes réduites ; C1, n6, n7, n9 sur de vrais
enregistrements). Version 3 — essai de bout en bout du format : des enregistrements **produits par le banc**
(`banc_idee_1_1_v2.jouer_repetition`, une répétition de chacune des 30 lignes, tous les bras, racine d'essai distincte de
celle du jeu) passent la chaîne entière de la lecture : tranches scellées, `charger_sortie`, `verifier_format`, `lire_v3`
(tous les étages, tous les rapportés), écriture scellée de `lecture.json` et relecture.

Pour franchir chaque étage, les **seules valeurs `promue`** des enregistrements recopiés sont réglées par un motif
synthétique (dents tenues, lignes V informatives, dent de H7) ; tout autre champ est celui du banc, tel quel. Le nombre
de répétitions par ligne est ramené à 100 le temps de l'essai (`REPETITIONS` de l'essai, jamais du jeu). Aucun chiffre
n'est lu ; seuls la forme et le passage sont vérifiés."""
import copy
import hashlib
import json

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import verifier
from controle_ia.organisme_idees_juge import banc_idee_1_1_v2 as B
from controle_ia.organisme_idees_juge import execution_idee_1_1_v5 as X
from controle_ia.organisme_idees_juge import lecture_idee_1_1_v4 as LE
from controle_ia.organisme_idees_juge import vue_v9_v2 as VV

RACINE_ESSAI = int(hashlib.sha256(b"essais idee 1.1 v3, bout en bout").hexdigest(), 16)
R_ESSAI = 100


@pytest.fixture(scope="module")
def reels():
    V = VV.charger()
    return {B.NOMS[i]: B.jouer_repetition(V, RACINE_ESSAI, i, 0)[0] for i in range(len(B.NOMS))}


def _fixer(d, v):
    """n8 : réglage strict — refuse d'écrire un `promue` absent ou non booléen (aucun champ masqué)."""
    if "promue" not in d or not isinstance(d["promue"], bool):
        raise AssertionError(f"réglage : `promue` absent ou non booléen dans {sorted(d)}")
    d["promue"] = bool(v)


def _promue(rec, bras, v):
    if bras in rec:
        _fixer(rec[bras], v)


def regler(rec, l, u):
    """Seules les valeurs `promue` changent ; le motif suit celui de l'essai de lecture synthétique."""
    for b in ("J8", "J9", "J9+", "La", "Ld", "J9-P", "La-P", "A1", "A2", "J9-D40", "J9-D", "J9-Dc", "temoin_lambda"):
        _promue(rec, b, False)
    for b in ("J8", "J9", "La", "J9-P"):
        if "strate_sans_log" in rec and b in rec["strate_sans_log"]:
            _fixer(rec["strate_sans_log"][b], False)
    if l in B.LIGNES_H:
        for q in ("terme_projete", "complet", "lineaire_seul"):
            _fixer(rec["J9-P-nu"][q], l == "H7" and q == "terme_projete" and u < 0.3)
        for q in ("terme_projete", "complet"):
            _fixer(rec["J9-P-gel"][q], False)
        return rec
    if l in ("Q2", "Q3", "Q4", "Q5"):
        _promue(rec, "J8", u < 0.95)
        if l == "Q5":
            _promue(rec, "La", u < 0.9)
        if l == "Q2":
            _promue(rec, "A1", u < 0.95)
            _promue(rec, "A2", u < 0.5)
    elif l == "Q6":
        for b in ("J8", "J9", "La", "Ld", "J9-P", "J9-D40", "J9-D"):
            _promue(rec, b, u < 0.9)
    elif l == "Q1":
        _promue(rec, "A1", u < 0.95)
        _promue(rec, "A2", u < 0.5)
    elif l.startswith("V"):
        a, b = u < 0.5, u < 0.4
        for x, v in (("J8", a), ("J9", b), ("J9+", b), ("J9-P", b or u < 0.45), ("La", b or u < 0.47), ("Ld", b or u < 0.44),
                     ("La-P", b or u < 0.47), ("J9-D", b), ("J9-D40", b), ("J9-Dc", b)):
            _promue(rec, x, v)
    return rec


def test_lecture_de_bout_en_bout_sur_enregistrements_du_banc(reels, tmp_path, monkeypatch):
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 920)))
    d = tmp_path / "run"
    tranches = {}
    for i, l in enumerate(B.NOMS):
        recs = []
        for r in range(R_ESSAI):
            rec = regler(copie_promues(reels[l]), l, float(rng.random()))
            rec["r"] = r
            recs.append(rec)
        for r0 in range(0, R_ESSAI, 50):
            nom = X.nom_tranche(i, r0)
            tranches[nom] = X.ecrire_json_scelle(d / "lignes" / f"{nom}.json",
                                                 {"ligne": l, "i_ligne": i, "r0": r0, "r1": r0 + 50, "repetitions": recs[r0:r0 + 50]})
    X.ecrire_json_scelle(d / "sortie.json", {"run_id": "essai", "manifeste_sha256": "m", "tranches": tranches})
    monkeypatch.setattr(B, "REPETITIONS", R_ESSAI)
    sortie = X.charger_sortie(d)
    LE.verifier_format(sortie["donnees"])
    res = LE.lire_v3(sortie["donnees"], RACINE_ESSAI, B_=40)
    assert res["etage_1"] == "franchi", [c for c in res["cellules_holm"] if c["statut"] == "non tenue"] + [f for f in res["fatales"] if f["audit"]]
    assert res["etage_2"] == "franchi" and res["etage_3"] == "franchi"
    for cle in ("principale", "La", "Ld", "rho", "rho_plus", "rho_plus_primaires", "secondaires", "secondaires_contre_J9_plus",
                "rho_par_strate", "decomposition_du_prix_intervalles", "mcnemar", "taux_des_cellules", "garde_P4", "etage_8",
                "issue", "audit_symetrie", "predictions", "lectures_declarees"):
        assert cle in res, cle
    assert all(f"{l}|A2" in res["taux_des_cellules"] for l in B.NOMS[:25])
    chemin = tmp_path / "lecture.json"
    sha = X.ecrire_json_scelle(chemin, {"run_id": "essai", "resultat": res})
    assert verifier(chemin) == sha
    assert json.loads(chemin.read_text(encoding="utf-8"))["resultat"]["version_lecture"] == 4


def test_format_reel_de_chaque_ligne_accepte(reels):
    donnees = {l: [dict(reels[l], r=0)] for l in B.NOMS}
    LE.verifier_format(donnees)



# --- version 4 ---------------------------------------------------------------------------------------------------------
def copie_promues(rec):
    """Copie légère : l'enregistrement et chaque dictionnaire qui porte une valeur `promue` (seules valeurs réglées) ;
    les autres champs du banc sont partagés, inchangés."""
    c = dict(rec)
    for k, v in rec.items():
        if isinstance(v, dict):
            c[k] = {kk: (dict(vv) if isinstance(vv, dict) else vv) for kk, vv in v.items()}
    return c


REDUCTIONS = (1, 2, 3, 4, 5)
R_REDUIT = 600


@pytest.fixture(scope="module")
def reduits():
    """Vrais enregistrements sous les cinq réductions : lignes V aux répétitions 0, 250, 500 ; Q9a, Q9b à 500."""
    V = VV.charger()
    out = {}
    for i in B.LIGNES_V:
        out[B.NOMS[i]] = {r: B.jouer_repetition(V, RACINE_ESSAI, i, r, reductions=REDUCTIONS)[0] for r in (0, 250, 500)}
    for l in ("Q9a", "Q9b"):
        out[l] = {500: B.jouer_repetition(V, RACINE_ESSAI, B.INDICE[l], 500, reductions=REDUCTIONS)[0]}
    return out


def _gabarit(reels, reduits, l, r):
    if l in reduits and l.startswith("V"):
        return reduits[l][0 if r < 250 else (250 if r < 500 else 500)]
    if l in reduits and r >= 500:
        return reduits[l][500]
    return reels[l]


def donnees_reduites(reels, reduits):
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 921)))
    d = {}
    for l in B.NOMS:
        recs = []
        for r in range(R_REDUIT):
            rec = regler(copie_promues(_gabarit(reels, reduits, l, r)), l, float(rng.random()))
            rec["r"] = r
            recs.append(rec)
        d[l] = recs
    return d


def test_formes_reduites_reelles(reels, reduits):
    for l, par_r in reduits.items():
        if l.startswith("V"):
            assert "strate_sans_log" not in par_r[0]
            assert not {"J9-D40", "J9-D", "J9-Dc"} & set(par_r[250]) and "La-P" in par_r[250]
            assert "La-P" not in par_r[500]
        else:
            assert "J9-P" not in par_r[500] and "La-P" not in par_r[500]


def test_lecture_de_bout_en_bout_sous_les_cinq_reductions(reels, reduits, tmp_path):
    d = donnees_reduites(reels, reduits)
    LE.verifier_format(d)
    res = LE.lire_v3(d, RACINE_ESSAI, B_=20)
    assert res["etage_1"] == "franchi" and res["etage_2"] == "franchi" and res["etage_3"] == "franchi"
    assert res["secondaires"]["J9-D contre J9"]["n"] == 250 and res["secondaires"]["La-P contre La"]["n"] == 500
    chemin = tmp_path / "lecture.json"
    sha = X.ecrire_json_scelle(chemin, {"resultat": res})
    assert verifier(chemin) == sha


def _sans(d, ligne, champs, depuis=0):
    e = dict(d)
    e[ligne] = [({k: v for k, v in r.items() if k not in champs} if j >= depuis else r) for j, r in enumerate(d[ligne])]
    return e


def test_c1_n6_n7_n9_sur_vrais_enregistrements(reels, reduits, tmp_path, monkeypatch):
    d = donnees_reduites(reels, reduits)
    # chaque artefact doit s'arrêter par le message de la garde de format, jamais par l'enveloppe (`KeyError`, …)
    regle = "absent dès la répétition 0, hors des bornes de la règle"
    for e, motif in ((_sans(d, "V3(0.8)", ("J9-D",)), regle),                                       # C1
                     (_sans(d, "V3(0.8)", ("J9-D40", "J9-D", "J9-Dc")), regle),
                     (_sans(d, "V2(0.4)", ("La-P", "journal_La-P")), regle),
                     (_sans(d, "V4(0.2)", ("J9-D40", "J9-D", "J9-Dc"), depuis=7),
                      "absent dès la répétition 7, hors des bornes de la règle")):                    # n6
        with pytest.raises(GardeArret, match=motif):
            LE.lire_v3(e, RACINE_ESSAI, B_=5)
    # n6 : groupe retiré en partie à une borne permise — ligne sans réduction, J9-D seul retiré dès 250
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 922)))
    e = dict(d)
    e["V4(0.2)"] = [dict(regler(copie_promues(reels["V4(0.2)"]), "V4(0.2)", float(rng.random())), r=r) for r in range(R_REDUIT)]
    LE.verifier_format(e)                                                                            # cas sain
    with pytest.raises(GardeArret, match="groupe « jumeau » retiré en partie"):
        LE.lire_v3(_sans(e, "V4(0.2)", ("J9-D",), depuis=250), RACINE_ESSAI, B_=5)
    e = dict(d)
    e["Q1"] = [dict(r) for r in d["Q1"]]
    e["Q1"][4] = dict(e["Q1"][4], A1=dict(e["Q1"][4]["A1"], promue="False"))                            # n7
    with pytest.raises(GardeArret, match="« A1.promue » n'est pas un booléen"):
        LE.lire_v3(e, RACINE_ESSAI, B_=5)
    # n9 : un enregistrement sans « r » dans une tranche scellée arrête `charger_sortie` avec message
    run = tmp_path / "run"
    tranches = {}
    for i, l in enumerate(B.NOMS):
        recs = [dict(r) for r in d[l][:50]]
        if l == "Q3":
            del recs[10]["r"]
        nom = X.nom_tranche(i, 0)
        tranches[nom] = X.ecrire_json_scelle(run / "lignes" / f"{nom}.json", {"ligne": l, "i_ligne": i, "r0": 0, "r1": 50,
                                                                              "repetitions": recs})
    X.ecrire_json_scelle(run / "sortie.json", {"run_id": "essai", "manifeste_sha256": "m", "tranches": tranches})
    monkeypatch.setattr(B, "REPETITIONS", 50)
    with pytest.raises(GardeArret, match="sans champ « r »"):
        X.charger_sortie(run)
