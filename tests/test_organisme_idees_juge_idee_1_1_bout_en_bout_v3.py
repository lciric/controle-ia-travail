"""Idée 1.1, version 3 — essai de bout en bout du format : des enregistrements **produits par le banc**
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

from controle_ia.scellement import verifier
from controle_ia.organisme_idees_juge import banc_idee_1_1_v2 as B
from controle_ia.organisme_idees_juge import execution_idee_1_1_v3 as X
from controle_ia.organisme_idees_juge import lecture_idee_1_1_v3 as LE
from controle_ia.organisme_idees_juge import vue_v9_v1 as VV

RACINE_ESSAI = int(hashlib.sha256(b"essais idee 1.1 v3, bout en bout").hexdigest(), 16)
R_ESSAI = 100


@pytest.fixture(scope="module")
def reels():
    V = VV.charger()
    return {B.NOMS[i]: B.jouer_repetition(V, RACINE_ESSAI, i, 0)[0] for i in range(len(B.NOMS))}


def _promue(rec, bras, v):
    if bras in rec:
        rec[bras]["promue"] = bool(v)


def regler(rec, l, u):
    """Seules les valeurs `promue` changent ; le motif suit celui de l'essai de lecture synthétique."""
    for b in ("J8", "J9", "J9+", "La", "Ld", "J9-P", "La-P", "A1", "A2", "J9-D40", "J9-D", "J9-Dc", "temoin_lambda"):
        _promue(rec, b, False)
    for b in ("J8", "J9", "La", "J9-P"):
        if "strate_sans_log" in rec and b in rec["strate_sans_log"]:
            rec["strate_sans_log"][b]["promue"] = False
    if l in B.LIGNES_H:
        for q in ("terme_projete", "complet", "lineaire_seul"):
            rec["J9-P-nu"][q]["promue"] = bool(l == "H7" and q == "terme_projete" and u < 0.3)
        for q in ("terme_projete", "complet"):
            rec["J9-P-gel"][q]["promue"] = False
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
            rec = regler(copy.deepcopy(reels[l]), l, float(rng.random()))
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
    assert json.loads(chemin.read_text(encoding="utf-8"))["resultat"]["version_lecture"] == 3


def test_format_reel_de_chaque_ligne_accepte(reels):
    donnees = {l: [dict(reels[l], r=0)] for l in B.NOMS}
    LE.verifier_format(donnees)
