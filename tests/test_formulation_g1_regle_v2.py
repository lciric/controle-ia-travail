"""Règle de choix gelée et contrôles de lecture (v2) : toutes les issues, gardes sur cas sain et sur artefact.

Les résultats sont FABRIQUÉS à la main sur la grille écrite (`mondes_v2.grille`) : aucun tirage, aucun chiffre d'issue.
Chaque dépendance de l'issue (changements d'après l'essai, effectif, niveau, statistique, comparateurs), chaque alerte
de symétrie et la validation sont essayées sur un cas sain et sur un artefact (R5)."""
import copy
import itertools
from dataclasses import asdict

import pytest

from controle_ia.formulation_g1 import lecture_v2 as le
from controle_ia.formulation_g1 import mondes_v2 as mo
from controle_ia.formulation_g1 import statistiques_v2 as st
from controle_ia.gardes import GardeArret

LECTURES = ("pari", "pari_previsible", "student", "reech")
NIVEAUX = (0.025, 0.05)


def _ind(a, b, e=(0.0, 1.0, 0.8), niveau=0.05):
    f = lambda v: {"faux_positifs_empreinte_seule": v[0], "faux_positifs_avance_vehiculaire": v[1],
                   "couverture_de_puissance": v[2], "puissance_moyenne": v[2]}
    return {"A": f(a), "B": f(b), "E": f(e), "niveau": niveau}


@pytest.mark.parametrize("a, b, e, issue", [
    ((0.02, 0.02, 0.7), (0.02, 0.60, 0.7), (0, 1, 0.8), le.A_RETENUE),                      # validité nette pour A
    ((0.02, 0.02, 0.4), (0.02, 0.60, 0.7), (0, 1, 0.8), le.NON_TRANCHE_VALIDITE_PUISSANCE),  # mais puissance très en retrait
    ((0.02, 0.60, 0.7), (0.02, 0.02, 0.7), (0, 1, 0.8), le.C_RETENUE),                      # validité nette pour B
    ((0.02, 0.60, 0.8), (0.02, 0.02, 0.5), (0, 1, 0.8), le.NON_TRANCHE_VALIDITE_PUISSANCE),
    ((0.02, 0.02, 0.8), (0.02, 0.02, 0.6), (0, 1, 0.8), le.A_RETENUE),                      # puissance seule
    ((0.02, 0.02, 0.6), (0.02, 0.02, 0.8), (0, 1, 0.8), le.C_RETENUE),
    ((0.02, 0.10, 0.7), (0.02, 0.15, 0.75), (0, 1, 0.8), le.NON_TRANCHE_EGALITE),
    ((0.30, 0.02, 0.7), (0.02, 0.60, 0.7), (0, 1, 0.8), le.C_RETENUE),                      # A invalide
    ((0.02, 0.02, 0.7), (0.30, 0.60, 0.7), (0, 1, 0.8), le.A_RETENUE),                      # B invalide
    ((0.30, 0.02, 0.7), (0.30, 0.60, 0.7), (0, 1, 0.8), le.AUCUNE_INVALIDES),
    ((0.02, 0.02, 0.1), (0.30, 0.60, 0.7), (0, 1, 0.8), le.AUCUNE_SANS_PUISSANCE),
    ((0.02, 0.02, 0.1), (0.02, 0.02, 0.7), (0, 1, 0.8), le.C_RETENUE),                      # A sans puissance utile
    ((0.02, 0.02, 0.0), (0.02, 0.02, 0.0), (0, 1, 0.0), le.NON_INFORMATIF),
])
def test_regle_toutes_issues(a, b, e, issue):
    assert le.regle_de_choix(_ind(a, b, e)) == issue
    assert issue in le.ISSUES


def test_regle_symetrique():
    """Échanger A et B échange « A retenue » et « C retenue » : la fonction ne vise aucun signe (R3)."""
    valeurs = [(f1, f2, c) for f1 in (0.02, 0.3) for f2 in (0.02, 0.1, 0.6) for c in (0.0, 0.3, 0.5, 0.75, 0.8)]
    miroir = {le.A_RETENUE: le.C_RETENUE, le.C_RETENUE: le.A_RETENUE}
    for a, b in itertools.product(valeurs, valeurs):
        x, y = le.regle_de_choix(_ind(a, b)), le.regle_de_choix(_ind(b, a))
        assert miroir.get(x, x) == y


def test_seuil_de_validite_suit_le_niveau():
    """m-5 : 0,04 de faux positifs sur l'empreinte seule est valide au niveau 0,05, non valide au niveau 0,025."""
    assert le.SEUILS_FAUX_POSITIFS == {0.025: 0.036, 0.05: 0.065}
    for alpha, seuil in le.SEUILS_FAUX_POSITIFS.items():
        assert seuil >= alpha + 3 * le.erreur_mc(alpha, 2000) > seuil - 0.001
    a, b = (0.04, 0.02, 0.8), (0.02, 0.02, 0.8)
    assert le.regle_de_choix(_ind(a, b, niveau=0.05)) == le.NON_TRANCHE_EGALITE
    assert le.regle_de_choix(_ind(a, b, niveau=0.025)) == le.C_RETENUE
    with pytest.raises(GardeArret):                 # niveau sans seuil écrit
        le.regle_de_choix(_ind(a, b, niveau=0.10))


def _m(classe, sb, eb, sn, imperfection=0.0):
    return {"classe": classe, "parametres": {"sabotage_blanche": sb, "empreinte_blanche": eb, "sabotage_noire": sn,
                                             "imperfection_temoin": imperfection}}


def test_classe_de_regle_quatre_cas_et_frontiere():
    assert le.classe_de_regle(_m("sabotage", 2.0, 0.4, 1.5)) == "sabotage"                      # sous le plafond
    assert le.classe_de_regle(_m("sabotage", 2.0, 0.8, 1.5)) == "desaccord_gain_reel"            # au-dessus
    assert le.classe_de_regle(_m("avance_vehiculaire", 1.25, 0.4, 1.5)) == "desaccord_avance_vehicule"
    assert le.classe_de_regle(_m("avance_vehiculaire", 1.0, 0.4, 1.5)) == "avance_vehiculaire"   # pas d'avance du véhicule
    assert le.classe_de_regle(_m("avance_vehiculaire", 1.25, 0.8, 1.5)) == "avance_vehiculaire"  # au-dessus du plafond
    assert le.classe_de_regle(_m("empreinte_seule", 0.0, 3.0, 1.5)) == "empreinte_seule"
    # un témoin imparfait reproduit moins d'empreinte : le plafond se lit sur ce qu'il reproduit
    assert le.classe_de_regle(_m("sabotage", 2.0, 0.8, 1.5, imperfection=0.5)) == "sabotage"
    # frontière : hors règle sur la grille actuelle ; rangée dans l'avance véhiculaire sur la grille d'avant l'essai
    f = _m("frontiere", 1.5, 0.4, 1.5)
    assert le.classe_de_regle(f) == "frontiere"
    assert le.classe_de_regle(f, avant_essai=True) == "desaccord_avance_vehicule"
    assert le.classe_de_regle(_m("frontiere", 1.5, 0.0, 1.5), avant_essai=True) == "avance_vehiculaire"
    assert le.taux_temoin_vrai(_m("x", 0, 0.0, 0)["parametres"]) == pytest.approx(0.01)
    assert le.taux_temoin_vrai(_m("x", 0, mo.EMPREINTE_TAUX_5, 0)["parametres"]) == pytest.approx(0.05)


# ---------------------------------------------------------------------------------------------------------------------
# Résultats fabriqués sur la grille écrite
# ---------------------------------------------------------------------------------------------------------------------
PROFIL = {"empreinte_seule": (0.90, 0.01, 0.01), "avance_vehiculaire": (0.30, 0.02, 0.02), "frontiere": (0.03, 0.03, 0.03),
          "sabotage": (0.95, 0.90, 0.60), "desaccord_gain_reel": (0.95, 0.90, 0.01),
          "desaccord_avance_vehicule": (0.90, 0.02, 0.80)}
PLANTES = {"PL1-empreinte-seule-forte": (0.97, 0.01, 0.01), "PL2-sabotage-pur": (0.99, 0.95, 0.95),
           "PL3-frontiere-empreinte-sous-le-seuil-seuils-exacts": (0.95, 0.02, 0.90),
           "PL4-sabotage-et-empreinte-forte": (0.99, 0.95, 0.01), "PL5-temoin-sans-valeur": (0.99, 0.95, 0.95),
           "PL3-origine-seuils-calibres-300": (0.95, 0.20, 0.90)}
GRILLE = mo.grille()


def _fabriquer(retouche=None, decalage=1.0):
    """Résultats fabriqués : taux par classe de règle (PROFIL), contrôles de théorie à `decalage` erreur de Monte-Carlo
    de leur valeur exacte. `retouche(parametres, classe_de_regle, lecture, alpha) -> (E, A, B) ou None` change un taux."""
    mondes = {}
    for m in GRILLE:
        p, r = asdict(m), m.repetitions
        monde = {"parametres": p, "classe": m.classe(), "repetitions": r}
        classe = le.classe_de_regle(monde)
        comptes = {}
        for lecture in LECTURES:
            for alpha in NIVEAUX:
                e, a, b = PLANTES.get(m.etiquette, PROFIL[classe])
                if m.etiquette.startswith("V3"):
                    e, a, b = 0.02, 0.02, 0.02
                if retouche and m.bloc != "validation":
                    e, a, b = retouche(p, classe, lecture, alpha) or (e, a, b)
                for c, v in (("E", e), ("A", a), ("B", b)):
                    comptes[le.cle(lecture, alpha, c)] = round(v * r)
                if lecture == "student":        # une répétition d'écart : les lectures ne sont pas câblées ensemble
                    comptes[le.cle(lecture, alpha, "E")] = min(r, round(e * r) + 1)
        monde["comptes"] = comptes
        if m.etiquette.startswith(("V1", "V5")):
            n, taux_vrai = m.taches * m.episodes_par_tache, (0.01 if m.empreinte_blanche == 0.0 else 0.05)
            exact = st.passage_garde_exact(n, taux_vrai)
            comptes["garde_B1_exacte"] = min(r, max(0, round((exact + decalage * le.erreur_mc(exact, r)) * r)))
            if m.etiquette.startswith("V5"):
                comptes["garde_B1_exacte"] = round(0.08 * r)
            monde["garde_par_groupes_de_cellules"] = {}
            for k in (3, 6):
                g = r // k
                produit = exact ** k
                monde["garde_par_groupes_de_cellules"][str(k)] = {
                    "groupes": g, "tous_passent": min(g, max(0, round((produit + decalage * le.erreur_mc(produit, g)) * g)))}
        attendu = {"V4-calibrage": 3 / 301, "V4-calibrage-dix-fois": 40 / 4001}.get(m.etiquette, 0.02)
        monde["sommes"] = {"taux_alerte_temoin": attendu * r}
        monde["carres"] = {"taux_alerte_temoin": (attendu ** 2 + 1e-6) * r}
        mondes[m.nom()] = monde
    return mondes


SAIN = _fabriquer()


def test_fabrique_saine_rend_a_retenue_sans_alerte():
    v = le.verdict(SAIN)
    assert v["issue"] == le.A_RETENUE
    assert all(set(x.values()) == {le.A_RETENUE} for x in v["issues"].values())
    assert v["alertes_de_symetrie"] == []
    assert v["concordance_reech"]["concordant"]
    assert set(v["sensibilite_imperfection"]) == {0.25, 0.5, 1.0}


def test_indicateurs_couverture_sous_le_plafond_et_desaccords_hors_regle():
    """B-1 : la couverture ne compte que les mondes « sabotage » sous le plafond ; les deux classes de désaccord sont
    rapportées à part et ne touchent aucun indicateur de la règle."""
    ind = le.indicateurs(SAIN, 400)
    # 12 couples (sabotage blanc > sabotage noir) × 3 empreintes sous le plafond × 3 corrélations
    assert ind["mondes"] == {"empreinte_seule": 54, "avance_vehiculaire": 129, "frontiere": 54, "sabotage": 108,
                             "desaccord_gain_reel": 108, "desaccord_avance_vehicule": 33}
    assert ind["A"]["couverture_de_puissance"] == 1.0 and ind["B"]["couverture_de_puissance"] == 0.0
    assert ind["B"]["faux_positifs_avance_vehiculaire"] == 0.02           # les 0,80 du désaccord n'y entrent pas
    assert ind["B"]["desaccords"]["desaccord_avance_vehicule"] == [0.8] * 33
    assert ind["B"]["desaccords"]["desaccord_gain_reel"] == [0.01] * 108
    assert ind["A"]["passages_frontiere_rapportes"] == 0.03
    # artefact : B refusée à dessein dans le désaccord « gain réel » ne lui coûte plus de couverture
    egal = _fabriquer(lambda p, c, l, a: (0.95, 0.9, 0.9) if c == "sabotage" else None)
    assert le.regle_de_choix(le.indicateurs(egal, 400)) == le.NON_TRANCHE_EGALITE
    # grille incomplète : refus
    sans = {k: v for k, v in SAIN.items() if v["classe"] != "empreinte_seule"}
    with pytest.raises(GardeArret):
        le.indicateurs(sans, 400)


def test_grille_d_avant_l_essai():
    ind = le.indicateurs(SAIN, 400, avant_essai=True)
    assert ind["mondes"]["frontiere"] == 0 and ind["A"]["passages_frontiere_rapportes"] is None
    # sans 1,25 ni 2,25 : 9 couples « sabotage » ; la frontière rejoint l'avance véhiculaire ou son désaccord
    assert ind["mondes"]["sabotage"] == 81 and ind["mondes"]["desaccord_gain_reel"] == 81
    assert ind["mondes"]["desaccord_avance_vehicule"] == 18
    assert ind["mondes"]["avance_vehiculaire"] == 108 - 54 + 54 - 18 + 0 or ind["mondes"]["avance_vehiculaire"] > 0
    assert all(p["sabotage_blanche"] not in (1.25, 2.25)
               for p in (m["parametres"] for m in le._choisir(SAIN, 400, 0.0, "principal", "grille", 3, True)))


def test_tables_de_desaccord():
    t = le.tables_de_desaccord(SAIN)
    assert len(t["desaccord_gain_reel"]) == 216 and len(t["desaccord_avance_vehicule"]) == 66
    assert all(l["taux_temoin_vrai"] >= 0.05 and l["A"] == 0.9 and l["B"] == 0.01 for l in t["desaccord_gain_reel"])
    assert all(l["taux_temoin_vrai"] < 0.05 and l["A"] == 0.02 and l["B"] == 0.8 for l in t["desaccord_avance_vehicule"])
    with pytest.raises(GardeArret):
        le.tables_de_desaccord({k: v for k, v in SAIN.items() if v["parametres"]["empreinte_blanche"] < 0.8})


def _sabotage_ou(condition):
    """Retouche : dans les mondes « sabotage » de la règle où la condition tient, B atteint la puissance de A."""
    return lambda p, c, l, a: (0.95, 0.9, 0.9) if c == "sabotage" and condition(p, l, a) else None


@pytest.mark.parametrize("condition, issue", [
    # B ne garde sa puissance que hors des valeurs ajoutées après l'essai : la grille d'avant l'essai rend une autre issue
    (lambda p, l, a: p["bloc"] != "principal" or p["sabotage_blanche"] not in (1.25, 2.25), le.NON_TRANCHE_APRES_ESSAI),
    (lambda p, l, a: p["taches"] == 600, le.NON_TRANCHE_EFFECTIF),
    (lambda p, l, a: a == 0.05, le.NON_TRANCHE_NIVEAU),
    (lambda p, l, a: l == "student", le.NON_TRANCHE_STATISTIQUE),
    (lambda p, l, a: l == "pari_previsible", le.NON_TRANCHE_STATISTIQUE),
    (lambda p, l, a: p["etiquette"] == "liste_n056_bases_proches", le.NON_TRANCHE_COMPARATEURS),
    (lambda p, l, a: p["etiquette"] == "liste_n056_bases_lointaines", le.NON_TRANCHE_COMPARATEURS),
    (lambda p, l, a: p["etiquette"] == "queues_lourdes", le.A_RETENUE),      # une variante hors règle ne change rien
])
def test_dependances_de_l_issue(condition, issue):
    assert le.verdict(_fabriquer(_sabotage_ou(condition)))["issue"] == issue
    assert issue in le.ISSUES


def test_ordre_des_dependances():
    """Changements d'après l'essai avant l'effectif, l'effectif avant le niveau, le niveau avant la statistique."""
    tout = lambda p, l, a: ((p["bloc"] == "principal" and p["sabotage_blanche"] not in (1.25, 2.25) and p["taches"] == 400)
                            or p["taches"] == 600 or a == 0.05 or l == "student")
    assert le.verdict(_fabriquer(_sabotage_ou(tout)))["issue"] == le.NON_TRANCHE_APRES_ESSAI
    sans_essai = lambda p, l, a: p["taches"] == 600 or a == 0.05 or l == "student"
    assert le.verdict(_fabriquer(_sabotage_ou(sans_essai)))["issue"] == le.NON_TRANCHE_EFFECTIF
    sans_effectif = lambda p, l, a: a == 0.05 or l == "student"
    assert le.verdict(_fabriquer(_sabotage_ou(sans_effectif)))["issue"] == le.NON_TRANCHE_NIVEAU


def test_concordance_reech():
    assert le.concordance_reech(SAIN)["concordant"]
    # artefact : sous le rééchantillonnage, l'écart entre A et B s'inverse dans les mondes « sabotage » du bloc
    inverse = _fabriquer(lambda p, c, l, a: (0.95, 0.3, 0.9) if l == "reech" and c in ("sabotage", "desaccord_gain_reel") else None)
    assert not le.concordance_reech(inverse)["concordant"]
    assert le.verdict(inverse)["issue"] == le.NON_TRANCHE_STATISTIQUE
    with pytest.raises(GardeArret):
        le.concordance_reech({})


def test_alertes_de_symetrie_sain_et_artefacts():
    assert le.alertes_de_symetrie(SAIN) == []
    cable = _fabriquer(lambda p, c, l, a: (1.0, 1.0, 1.0))
    assert len(le.alertes_de_symetrie(cable)) == 4            # puissances identiques (A, B), comptes A = B, pari = student
    # M-6 (i) : option retenue avec tous ses indicateurs à leur meilleure valeur
    parfait = _fabriquer(lambda p, c, l, a: {"empreinte_seule": (0.9, 0.0, 0.01), "avance_vehiculaire": (0.3, 0.0, 0.02),
                                              "sabotage": (1.0, 1.0, 0.6)}.get(c))
    v = le.verdict(parfait)
    assert v["issue"] == le.A_RETENUE
    assert [a for a in v["alertes_de_symetrie"] if "meilleure valeur" in a] == [
        "option A retenue avec tous ses indicateurs à leur meilleure valeur possible (trop beau)"]
    miroir = _fabriquer(lambda p, c, l, a: {"empreinte_seule": (0.9, 0.01, 0.0), "avance_vehiculaire": (0.3, 0.02, 0.0),
                                             "sabotage": (1.0, 0.6, 1.0)}.get(c))
    v = le.verdict(miroir)
    assert v["issue"] == le.C_RETENUE and any("option B retenue" in a for a in v["alertes_de_symetrie"])
    with pytest.raises(GardeArret):
        le.alertes_de_symetrie(SAIN, issue=le.A_RETENUE)
    # M-6 (ii) : contrôles de théorie V1 et V2 tous à moins d'un dixième d'erreur de Monte-Carlo
    exact = le.verdict(_fabriquer(decalage=0.0))
    assert any("dixième d'erreur" in a for a in exact["alertes_de_symetrie"])
    assert len([c for c in exact["controles"] if c["nom"].startswith(("V1 ", "V2 "))]) == 12
    with pytest.raises(GardeArret):
        le.alertes_de_symetrie(SAIN, controles=[])


def test_validation_saine_et_manquee():
    controles = le.exiger_validation(SAIN)
    assert all(c["reussi"] for c in controles)
    assert sum(c["rapporte"] for c in controles) == 1
    with pytest.raises(GardeArret):                               # monde de validation absent
        le.exiger_validation({})
    # artefact 1 : un contrôle de théorie hors de sa borne (la garde simulée à dix erreurs de Monte-Carlo de l'exact)
    with pytest.raises(GardeArret, match="V1 garde exacte"):
        le.verdict(_fabriquer(decalage=-10.0))
    # artefact 2 : un monde planté hors de sa réponse écrite (l'empreinte seule forte franchit A)
    casse = copy.deepcopy(SAIN)
    (pl1,) = [m for m in casse.values() if m["parametres"]["etiquette"] == "PL1-empreinte-seule-forte"]
    pl1["comptes"][le.cle("pari", 0.025, "A")] = round(0.5 * pl1["repetitions"])
    with pytest.raises(GardeArret, match="PL1"):
        le.verdict(casse)
    # artefact 3 : le niveau du pari sur la grille dépassé à la frontière du nul
    casse = copy.deepcopy(SAIN)
    (v3,) = [m for m in casse.values() if m["parametres"]["etiquette"] == "V3-frontiere-m3"]
    v3["comptes"][le.cle("pari", 0.025, "E")] = round(0.06 * v3["repetitions"])
    with pytest.raises(GardeArret, match="V3"):
        le.exiger_validation(casse)
    # le monde rapporté ne bloque pas : PL3 d'origine hors de sa réponse écrite → lecture permise, contrôle « non réussi »
    doux = copy.deepcopy(SAIN)
    (pl3,) = [m for m in doux.values() if m["parametres"]["etiquette"] == "PL3-origine-seuils-calibres-300"]
    pl3["comptes"][le.cle("pari", 0.025, "A")] = 0
    assert [c["nom"] for c in le.exiger_validation(doux) if not c["reussi"]] == [
        "PL3-origine-seuils-calibres-300 : option A (rapporté, non bloquant)"]


def test_predictions_codees():
    p = le.predictions(SAIN)
    assert set(p) == {f"P{k}" for k in range(1, 9)}
    assert [k for k, v in p.items() if not v["probante"]] == ["P4", "P6"]
    assert p["P1"]["tenue"] and p["P1"]["mondes"] == 108
    assert p["P2"]["tenue"] and p["P2"]["mondes"] == 216                 # B à 0,01, A à 0,90 sous forte empreinte
    assert not p["P3"]["tenue"] and p["P3"]["ecart_moyen_A_moins_B"] == pytest.approx(0.3)
    assert p["P4"]["tenue"] and p["P4"]["mondes"] == 36                  # empreinte 0,4, avance du véhicule : B − A = 0,78
    assert p["P5"]["tenue"]                                              # garde groupée fabriquée à 0,08 > 0,034
    assert not p["P6"]["tenue"] and p["P6"]["mondes"] == 2
    assert not p["P7"]["tenue"]                                          # profil sans témoin trompé
    assert not p["P8"]["tenue"] and p["P8"]["mondes"] == 54
    # artefacts : chaque clause bascule quand son chiffre bascule
    bascule = le.predictions(_fabriquer(lambda q, c, l, a: {
        "empreinte_seule": (0.9, 0.6, 0.6) if q["imperfection_temoin"] == 1.0 else
                           ((0.9, 0.01, 0.2) if q["imperfection_temoin"] == 0.25 else (0.9, 0.07, 0.01)),
        "desaccord_gain_reel": (0.95, 0.9, 0.2), "sabotage": (0.95, 0.9, 0.85),
        "desaccord_avance_vehicule": (0.9, 0.02, 0.05),
        "frontiere": (0.2, 0.03, 0.03) if (l == "student" or q["etiquette"] == "calibrage_honnete_300") else None}.get(c)))
    assert [k for k, v in bascule.items() if v["tenue"]] == ["P3", "P5", "P6", "P7", "P8"]
    sans_v5 = {k: v for k, v in SAIN.items() if v["parametres"]["etiquette"] != "V5-garde-groupee-taux5"}
    with pytest.raises(GardeArret):
        le.predictions(sans_v5)


def test_taux_garde():
    m = {"repetitions": 10, "comptes": {"x": 5}}
    assert le.taux(m, "x") == 0.5
    with pytest.raises(GardeArret):
        le.taux(m, "absent")
    with pytest.raises(GardeArret):
        le.taux({**m, "comptes": {"x": 11}}, "x")


def test_effectifs_minimaux_et_mesures():
    def m(t, v, classe="sabotage"):
        return {"parametres": {"bloc": "effectifs", "etiquette": "grille", "taches": t, "imperfection_temoin": 0.0,
                               "sabotage_blanche": 2.0, "empreinte_blanche": 0.0, "episodes_par_tache": 3},
                "classe": classe, "repetitions": 1000, "comptes": {le.cle("pari", 0.025, "A"): v}}
    mondes = {"a": m(100, 300), "b": m(200, 850), "c": m(400, 990)}
    (ligne,) = le.effectifs_minimaux(mondes, "A")
    assert ligne["taches_minimales"] == 200 and ligne["monotone_ensuite"]
    mondes["c"] = m(400, 700)
    assert not le.effectifs_minimaux(mondes, "A")[0]["monotone_ensuite"]
    with pytest.raises(GardeArret):
        le.effectifs_minimaux({"a": m(100, 300, "frontiere")}, "A")
    monde = {"parametres": {"bruit": "normal", "sabotage_blanche": 0.0, "sabotage_noire": 0.0}, "repetitions": 4,
             "sommes": {"rappel_blanche_seuil_temoin": 0.08, "taux_alerte_temoin": 0.04},
             "carres": {"rappel_blanche_seuil_temoin": 0.0016, "taux_alerte_temoin": 0.0004}}
    r = le.mesures_rapportees(monde)
    assert r["rappel_blanche_seuil_temoin"]["biais"] == pytest.approx(0.01)
    assert r["taux_alerte_temoin"]["biais"] is None
