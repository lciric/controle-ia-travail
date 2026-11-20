"""Essais des gardes de B9 qui ne demandent pas une source entière : chacune avec son cas sain et son artefact (règle R5).
Gardes 1 à 12, 14 à 16, 18 et 19 (la garde 20 est dans les essais des outils ; 13, 17, 23 à 25 et 27 dans ceux de la couche
mécanique, de l'organisme et du générateur ; 21 et 26 dans ceux des outils ; 22 dans ceux de la couche statistique)."""

import inspect
import json
import os

import numpy as np
import pytest

from aides_heritage_etage_processeur_v1 import graines
from controle_ia.heritage_etage_processeur_v1 import comparateur as C
from controle_ia.heritage_etage_processeur_v1 import cout as CO
from controle_ia.heritage_etage_processeur_v1 import enveloppe as EN
from controle_ia.heritage_etage_processeur_v1 import executeur as EX
from controle_ia.heritage_etage_processeur_v1 import lois as L
from controle_ia.heritage_etage_processeur_v1 import mondes as MO
from controle_ia.heritage_etage_processeur_v1 import registre as R
from controle_ia.heritage_etage_processeur_v1.constantes import (DEBUT_DONNEES, DESCRIPTION_FIXE, FIN_DONNEES, HYPOTHESE_NEUTRE,
                                                                 JUSTIFICATION_FIXE, NON_EPROUVEE, PREDICTION_FIXE, TIENT)


def _tranche(loi, graine, n=200):
    rng = np.random.default_rng(graine)
    Z = np.round(rng.normal(0, 1, (n, 2)), 6)
    G = rng.integers(0, 2, n)
    y = L.tirer_issues(L.matrice(loi, Z, G), rng)
    return {"Z": Z, "G": G, "y": y}


def _entree(loi, domaine="D03", justification=JUSTIFICATION_FIXE):
    eng = EX.engagement(domaine, loi)
    return R.nouvelle_entree(domaine, eng, EX.sceller(eng), DESCRIPTION_FIXE, justification, PREDICTION_FIXE)


def _lois(n, graine=11):
    rng = np.random.default_rng(graine)
    return [L.loi_aleatoire(rng) for _ in range(n)]


def _provenance(gen=1, origine="continuation", bras="2"):
    return R.provenance(origine, gen, "heritage-etage-processeur-v1", "a" * 64, 0, bras)


# --- garde 1 : invariant, « rien d'un juge ni de la clé dans le registre » ----------------------------------------------------


def _rejouer(ecrire, journal, contexte):
    """Rejoue un journal : appelle la fonction d'écriture sur chaque tentative ; le contexte (sorties de juges factices, drapeaux
    de promotion, clé du monde) est offert à toute fonction qui le demande par son nom. Rend les octets des champs écrits."""
    params = inspect.signature(ecrire).parameters
    out = []
    for t in journal:
        kw = {k: contexte[k] for k in ("juges", "promotions", "cle") if k in params}
        r, g = ecrire(t["engagement"], t["sha"], t["tranche"], t["brut"], {"cout_usd": 0.18}, **kw)
        out.append(L.json_canonique({"resultat": r, "gardee": g}))
    return "\n".join(out).encode("utf-8")


def _journal():
    lois = _lois(6, 21)
    tranche = _tranche(lois[0], 22)
    journal = []
    for i, loi in enumerate(lois):
        eng = EX.engagement("D01", loi)
        brut = None if i == 5 else EX.script_fidele(loi, tranche)
        journal.append({"engagement": eng, "sha": EX.sceller(eng), "tranche": tranche, "brut": brut, "loi": loi})
    return journal, lois


def test_garde_1_invariant_octet_pour_octet_et_ecriture_fautive_detectee():
    journal, lois = _journal()
    rng = np.random.default_rng(3)
    contexte_a = {"juges": [{"note": float(x)} for x in rng.random(6)], "promotions": [bool(x) for x in rng.integers(0, 2, 6)],
                  "cle": {f"D01:V{i}": l for i, l in enumerate(lois)}}
    perm = rng.permutation(6)
    autre = _lois(6, 99)
    contexte_b = {"juges": [contexte_a["juges"][i] for i in perm], "promotions": [not p for p in contexte_a["promotions"]],
                  "cle": {f"D01:V{i}": l for i, l in enumerate(autre)}}
    sain_a = _rejouer(EX.ecrire_champs_programme, journal, contexte_a)
    sain_b = _rejouer(EX.ecrire_champs_programme, journal, contexte_b)
    assert sain_a == sain_b
    assert set(inspect.signature(EX.ecrire_champs_programme).parameters) == {
        "engagement_scelle", "engagement_sha256", "tranche_epreuve", "fichier_brut_octets", "journal_couts"}

    def fautive_promotion(engagement_scelle, engagement_sha256, tranche_epreuve, fichier_brut_octets, journal_couts, promotions):
        r, g = EX.ecrire_champs_programme(engagement_scelle, engagement_sha256, tranche_epreuve, fichier_brut_octets, journal_couts)
        i = [L.json_canonique(t["engagement"]) for t in journal].index(L.json_canonique(engagement_scelle))
        return (dict(r, classe=TIENT), True) if promotions[i] else (r, g)

    def fautive_cle(engagement_scelle, engagement_sha256, tranche_epreuve, fichier_brut_octets, journal_couts, cle):
        r, g = EX.ecrire_champs_programme(engagement_scelle, engagement_sha256, tranche_epreuve, fichier_brut_octets, journal_couts)
        loi = C.loi_de_l_engagement_scelle(engagement_scelle, engagement_sha256)
        dans_la_cle = any(L.json_canonique(loi) == L.json_canonique(v) for v in cle.values())
        return (dict(r, classe=TIENT), True) if dans_la_cle else (r, g)

    def fautive_juge(engagement_scelle, engagement_sha256, tranche_epreuve, fichier_brut_octets, journal_couts, juges):
        r, g = EX.ecrire_champs_programme(engagement_scelle, engagement_sha256, tranche_epreuve, fichier_brut_octets, journal_couts)
        i = [L.json_canonique(t["engagement"]) for t in journal].index(L.json_canonique(engagement_scelle))
        return (dict(r, classe=TIENT), True) if juges[i]["note"] > 0.5 else (r, g)

    for fautive in (fautive_promotion, fautive_cle, fautive_juge):
        assert _rejouer(fautive, journal, contexte_a) != _rejouer(fautive, journal, contexte_b), fautive.__name__


# --- garde 2 -------------------------------------------------------------------------------------------------------------------


def test_garde_2_aucun_champ_du_registre_chez_un_juge():
    assert R.entree_d_un_juge(loi={"type": "fixe", "probas": [0.2, 0.3, 0.5]}, donnees="tranche")
    with pytest.raises(R.ArretRegistre):
        R.entree_d_un_juge(justification=JUSTIFICATION_FIXE)
    e = dict(_entree(_lois(1)[0]), resultat={"classe": TIENT, "cout_usd": 0.18}, gardee=True, provenance=_provenance())
    with pytest.raises(R.ArretRegistre):
        R.entree_d_un_juge(contexte={"ligne": e})


# --- garde 3 -------------------------------------------------------------------------------------------------------------------


def test_garde_3_prediction_scellee():
    loi = _lois(1)[0]
    tranche = _tranche(loi, 5)
    e = _entree(loi)
    ex = EX.Executeur()
    resultat, gardee = ex.eprouver(e["tentative"]["engagement"], e["tentative"]["engagement_sha256"], e["prediction_sha256"],
                                   tranche, False, 0.18)
    r = R.Registre()
    r.ajouter(dict(e, resultat=resultat, gardee=gardee, provenance=_provenance()))
    with pytest.raises(EX.ArretExecuteur):
        ex.eprouver(e["tentative"]["engagement"], e["tentative"]["engagement_sha256"], "", tranche, False, 0.18)
    modifiee = dict(e, prediction=[0.5, 0.3, 0.2])
    with pytest.raises(R.ArretRegistre):
        r.ajouter(dict(modifiee, resultat=resultat, gardee=gardee, provenance=_provenance()))
    with pytest.raises(R.ArretRegistre):
        R.nouvelle_entree("D01", e["tentative"]["engagement"], "x", DESCRIPTION_FIXE, JUSTIFICATION_FIXE, [0.33, 0.33, 0.34])


# --- garde 4 -------------------------------------------------------------------------------------------------------------------


def _registre_ecrit(chemin, n=4):
    r = R.Registre(chemin)
    for i, loi in enumerate(_lois(n)):
        r.ajouter(dict(_entree(loi), resultat={"classe": TIENT, "cout_usd": 0.18}, gardee=True, provenance=_provenance()))
        if i % 2:
            r.sceller_generation(f"generation-{i}")
    return r


def test_garde_4_chaine_d_empreintes_ajout_seul(tmp_path):
    r = _registre_ecrit(str(tmp_path / "r.jsonl"))
    assert r.verifier_chaine()
    lignes = open(r.chemin, encoding="utf-8").read().splitlines()
    reecrite = json.loads(lignes[1])
    reecrite["justification"] = "réécrite"
    with open(r.chemin, "w", encoding="utf-8") as f:
        f.write("\n".join([lignes[0], L.json_canonique(reecrite)] + lignes[2:]) + "\n")
    with pytest.raises(R.ArretRegistre):
        r.verifier_chaine()
    r2 = _registre_ecrit(str(tmp_path / "r2.jsonl"))
    r2.entrees.pop(1)
    with pytest.raises(R.ArretRegistre):
        r2.verifier_chaine(depuis_le_disque=False)
    with pytest.raises(R.ArretRegistre):
        R.Registre(str(tmp_path / "r2.jsonl"))  # jamais d'écrasement
    # une entrée réécrite à l'identique en mémoire et sur disque, hors des têtes de sceau : seule la chaîne la voit
    r3 = _registre_ecrit(str(tmp_path / "r3.jsonl"))
    r3.entrees[2]["justification"] = "réécrite"
    with open(r3.chemin, "w", encoding="utf-8") as f:
        f.write("".join(L.json_canonique(e) + "\n" for e in r3.entrees))
    with pytest.raises(R.ArretRegistre, match="chaîne rompue"):
        r3.verifier_chaine()


# --- gardes 5, 8, 19 -------------------------------------------------------------------------------------------------------


def test_garde_5_historique_de_depart():
    assert R.exiger_historique_vide(None) and R.exiger_historique_vide([])
    with pytest.raises(R.ArretRegistre):
        R.exiger_historique_vide([{"generation": 1}])


def test_garde_8_champs_du_bras_1_jamais_servis():
    assert R.verifier_bras_1_non_servi("1", None)
    assert R.verifier_bras_1_non_servi("2", [{"probleme": "D01"}])
    with pytest.raises(R.ArretRegistre):
        R.verifier_bras_1_non_servi("1", [{"probleme": "D01"}])


def test_garde_19_taux_d_echec_egal_dans_les_bras():
    assert EN.exiger_taux_egaux({"1": 0.25, "2": 0.25, "3": 0.25})
    with pytest.raises(EN.ArretEnveloppe):
        EN.exiger_taux_egaux({"1": 0.25, "2": 0.25, "3": 0.5})


# --- garde 6 ---------------------------------------------------------------------------------------------------------------


def test_garde_6_cloisonnement_des_dossiers(tmp_path):
    d1, d2, d3 = (str(tmp_path / f"bras-{b}") for b in "123")
    vue = [{"probleme": "D01", "tentative": {"description": DESCRIPTION_FIXE}}]
    assert R.verifier_cloisonnement(d2, vue, [d1, d3])
    with pytest.raises(R.ArretRegistre):
        R.verifier_cloisonnement(d2, vue + [{"probleme": os.path.join(d3, "registre.jsonl")}], [d1, d3])
    with pytest.raises(R.ArretRegistre):
        R.verifier_cloisonnement(d2, vue, [d1, d2])
    with pytest.raises(R.ArretRegistre):
        R.verifier_cloisonnement(os.path.join(d1, "sous"), vue, [d1])


# --- garde 7 ---------------------------------------------------------------------------------------------------------------


def test_garde_7_grain_du_retour_et_du_registre():
    e = dict(_entree(_lois(1)[0]), resultat={"classe": TIENT, "cout_usd": 0.18}, gardee=True, provenance=_provenance())
    r = R.Registre()
    r.ajouter(e)
    assert R.verifier_grain(r.vue("entiere"))
    assert R.retour([e]) == [{"classe": TIENT, "cout_usd": 0.18}]
    for faute in ({"classe": TIENT, "cout_usd": 0.18, "valeur": 0.031}, {"classe": TIENT, "cout_usd": 0.18, "distance": 0.011},
                  {"classe": "3 sur 12", "cout_usd": 0.18}, {"classe": TIENT, "cout_usd": 0.18, "part": "0.25"}):
        with pytest.raises(R.ArretRegistre):
            R.verifier_grain({"retour": [faute]})  # un retour fautif, qui recopierait la valeur, est arrêté
        with pytest.raises(R.ArretRegistre):
            R.Registre().ajouter(dict(e, resultat=faute))
    with pytest.raises(R.ArretRegistre):
        R.verifier_grain([dict(r.vue("entiere")[0], probleme=12)])


# --- garde 9 ---------------------------------------------------------------------------------------------------------------


def test_garde_9_generation_finale_sans_ecriture(tmp_path):
    r = _registre_ecrit(str(tmp_path / "r.jsonl"))
    avant = r.octets()
    r.fermer()
    assert R.verifier_finale_sans_ecriture(avant, r)
    with pytest.raises(R.ArretRegistre):
        r.ajouter(dict(_entree(_lois(1, 5)[0]), resultat={"classe": TIENT, "cout_usd": 0.18}, gardee=True,
                       provenance=_provenance(4)))
    r2 = _registre_ecrit(str(tmp_path / "r2.jsonl"))
    avant2 = r2.octets()
    r2.ajouter(dict(_entree(_lois(1, 6)[0]), resultat={"classe": TIENT, "cout_usd": 0.18}, gardee=True, provenance=_provenance(4)))
    with pytest.raises(R.ArretRegistre):
        R.verifier_finale_sans_ecriture(avant2, r2)


# --- garde 10 --------------------------------------------------------------------------------------------------------------


def test_garde_10_tranche_d_epreuve_jamais_servie(tmp_path):
    g = graines()
    s = MO.generer_suite(g, dict(couche="essai", famille="garde-10", source=0), 0.25)
    for m in (s.cibles[0], s.finale):
        d = str(tmp_path / m.nom)
        MO.ecrire_monde(d, m)
        for dom in m.domaines:
            servi = MO.lire_csv(os.path.join(d, "servi", dom["nom"] + ".csv"))
            epreuve = MO.lire_csv(os.path.join(d, "epreuve", dom["nom"], "episodes.csv"))
            assert MO.verifier_tranche_jamais_servie(servi, epreuve)
            assert len(servi) == len(epreuve) == 200
        with pytest.raises(MO.ArretGenerateur):
            MO.verifier_tranche_jamais_servie(servi + [epreuve[3]], epreuve)


# --- garde 11 --------------------------------------------------------------------------------------------------------------


def test_garde_11_entree_de_l_experimentateur_sur_les_deux_listes():
    lois = _lois(3)
    entrees = [_entree(l, f"D0{i}") for i, l in enumerate(lois)]
    for liste in ("avec_description", "engagement_seul"):
        cartes, classement = EN.cartes_d_un_lot(entrees, [0, 1, 2], liste)
        assert [c["ident"] for c in classement] == [c["identifiant"] for c in cartes]
        for c, e in zip(cartes, entrees):
            assert c["hypothese"] == (DESCRIPTION_FIXE if liste == "avec_description" else HYPOTHESE_NEUTRE)
            assert c["test_de_mort"] == e["tentative"]["engagement"]["test_de_mort"]
            assert DEBUT_DONNEES not in L.json_canonique(c) and FIN_DONNEES not in L.json_canonique(c)
    e = entrees[0]
    carte = R.projeter_vers_fiche(e, "T-0000")
    for faute in (dict(carte, hypothese=carte["hypothese"] + " " + JUSTIFICATION_FIXE),
                  dict(carte, prediction=L.json_canonique(list(e["prediction"]))),
                  dict(carte, hypothese=entrees[1]["tentative"]["engagement_sha256"]),
                  dict(carte, hypothese=DEBUT_DONNEES + "\n" + DESCRIPTION_FIXE + "\n" + FIN_DONNEES),
                  dict(carte, justification=JUSTIFICATION_FIXE)):
        with pytest.raises(R.ArretRegistre):
            R.verifier_projection(faute, e, entrees)
    with pytest.raises(R.ArretRegistre):
        R.verifier_projection(R.projeter_vers_fiche(e, "T-0000", "avec_description"), e, entrees, "engagement_seul")


# --- garde 12 --------------------------------------------------------------------------------------------------------------


def test_garde_12_comparateur_sans_juge():
    lois = _lois(3, 31)
    Z, G = L.instances_oracle(777, 4000)
    o = C.Oracle(Z, G)
    plantees = {"D03:V": lois[0], "D03:F": lois[1]}
    e = _entree(lois[0])
    t = {"engagement": e["tentative"]["engagement"], "engagement_sha256": e["tentative"]["engagement_sha256"]}
    a = C.apparier_tentative(dict(t, promue=True, classe=TIENT), {"D03": plantees}, o)
    b = C.apparier_tentative(dict(t, promue=False, classe="ne tient pas"), {"D03": plantees}, o)
    assert a == b == "D03:V"
    assert C.apparier_tentative(dict(t), {"D03": {"D03:F": lois[1]}}, o) is None

    def fautif(tentative, mondes_par_domaine, oracle):
        ident = C.apparier_tentative(tentative, mondes_par_domaine, oracle)
        return ident if tentative.get("promue") else None
    assert fautif(dict(t, promue=True), {"D03": plantees}, o) != fautif(dict(t, promue=False), {"D03": plantees}, o)
    assert "promue" not in inspect.getsource(C.apparier_tentative) and "promue" not in inspect.getsource(C.apparier)


# --- garde 14 --------------------------------------------------------------------------------------------------------------


def test_garde_14_enveloppe_lots_et_statut_de_budget():
    loi = _lois(1)[0]
    tranche = _tranche(loi, 8)
    entrees = [_entree(loi, "D05") for _ in range(13)]
    g = graines()
    sorties, journal, _ = EN.eprouver_generation(entrees, lambda d: tranche, EX.Executeur(), g.g(couche="essai", role="e1"), 0.0,
                                                 26, g.g(couche="essai", role="b1"))
    assert [j["tentatives"] for j in journal] == [12, 1] and all(s[0]["classe"] != NON_EPROUVEE for s in sorties)
    sorties, journal, _ = EN.eprouver_generation(entrees, lambda d: tranche, EX.Executeur(), g.g(couche="essai", role="e2"), 0.0,
                                                 5, g.g(couche="essai", role="b2"))
    non = [s for s in sorties if s[0]["classe"] == NON_EPROUVEE]
    assert len(non) == 8 and all(s[1] is False for s in non) and all(s[0]["cout_usd"] == 0.0 for s in non)
    assert sum(j["eprouvees"] for j in journal) == 5
    r = R.Registre()
    for e, (res, gardee) in zip(entrees, sorties):
        r.ajouter(dict(e, resultat=res, gardee=gardee, provenance=_provenance()))
    assert sum(1 for x in R.retour(r.entrees) if x["classe"] == NON_EPROUVEE) == 8
    assert EN.lots_par_domaine([_entree(loi, "D01"), _entree(loi, "D02"), _entree(loi, "D01")]) == [("D01", [0, 2]), ("D02", [1])]


# --- garde 15 --------------------------------------------------------------------------------------------------------------


def test_garde_15_seuil_scelle_relu():
    loi = _lois(1)[0]
    assert EX.verifier_seuil_scelle(EX.engagement("D01", loi)) == (0.02, "≥")
    for faux in ("au plus 0,02", "au moins 0,2", "≤ 0,02"):
        with pytest.raises(EX.ArretExecuteur):
            EX.verifier_seuil_scelle(EX.engagement("D01", loi, faux))


# --- garde 16 --------------------------------------------------------------------------------------------------------------


def test_garde_16_script_qui_fabrique_ses_lignes():
    lois = _lois(4, 41)
    tranche = _tranche(lois[0], 9)
    for loi in lois:
        e = _entree(loi)
        r, _ = EX.Executeur().eprouver(e["tentative"]["engagement"], e["tentative"]["engagement_sha256"], e["prediction_sha256"],
                                       tranche, False, 0.18)
        assert r["classe"] in ("tient", "ne tient pas")
        assert abs(EX.contre_calcul(loi, tranche) - EX.statistique_moyenne(loi, tranche["Z"], tranche["G"], tranche["y"])) < 1e-12
    e = _entree(lois[2])
    with pytest.raises(EX.ArretExecuteur):
        EX.Executeur(script=EX.script_fabrique).eprouver(e["tentative"]["engagement"], e["tentative"]["engagement_sha256"],
                                                         e["prediction_sha256"], tranche, False, 0.18)


# --- garde 18 --------------------------------------------------------------------------------------------------------------


def test_garde_18_regle_de_retrait():
    rng = np.random.default_rng(4)
    for entrees in (0, 93, 282, 564):
        lecture = np.full(55, float(CO.cout_lecture_par_appel(entrees)))
        perm = rng.permutation(55)
        gardes, retires, reliquat = CO.retrait_v2(perm, lecture)
        assert CO.verifier_retrait(perm, gardes, retires, lecture) and reliquat >= -1e-9
        G, par, rel = CO.retrait_v2_vectorise(perm[None, :], lecture[:1])
        assert sorted(np.flatnonzero(G[0]).tolist()) == gardes and abs(rel[0] - reliquat) < 1e-9
    lecture = np.full(55, float(CO.cout_lecture_par_appel(282)))
    cout = CO.COUT_APPEL[CO.ESPECE_DE_L_APPEL] + lecture + CO.PROVISION_PAR_APPEL
    plus_chers = [int(a) for a in np.argsort(-cout, kind="stable")]
    retires, restant = [], float(cout.sum())
    for a in plus_chers:
        if restant <= CO.BUDGET_GENERATION:
            break
        restant -= float(cout[a])
        retires.append(a)
    gardes = sorted(set(range(55)) - set(retires))
    with pytest.raises(CO.ArretCout):
        CO.verifier_retrait(rng.permutation(55), gardes, retires, lecture)
    assert CO.retrait_v1(0.0)[0].tolist() == [11] * 5 and CO.retrait_v1(float(CO.cout_lecture_par_appel(282)))[0].sum() < 55
