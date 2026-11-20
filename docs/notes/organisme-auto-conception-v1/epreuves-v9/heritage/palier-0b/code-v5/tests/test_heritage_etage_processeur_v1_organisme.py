"""Essais contre le code de l'organisme (copie au commit 94bfd92, empreintes du palier 0a) : forme imposée et lecture du seuil
recopiées à l'octet ; garde 17 (exécuteur simulé contre l'étage de l'organisme, tentative par tentative, cas sain et exécuteur
fautif) ; garde 11 vue dans la consigne même que l'étage sert à l'expérimentateur ; copie absente ou altérée : garde non jouée."""

import glob
import os
import shutil

import numpy as np
import pytest

from aides_heritage_etage_processeur_v1 import copie_organisme, graines
from controle_ia.heritage_etage_processeur_v1 import comparateur as C
from controle_ia.heritage_etage_processeur_v1 import enveloppe as EN
from controle_ia.heritage_etage_processeur_v1 import executeur as EX
from controle_ia.heritage_etage_processeur_v1 import lois as L
from controle_ia.heritage_etage_processeur_v1 import mondes as MO
from controle_ia.heritage_etage_processeur_v1 import organisme as OR
from controle_ia.heritage_etage_processeur_v1 import registre as R
from controle_ia.heritage_etage_processeur_v1.constantes import (DEBUT_DONNEES, DESCRIPTION_FIXE, FIN_DONNEES, JUSTIFICATION_FIXE,
                                                                 NON_EXECUTABLE, PREDICTION_FIXE)


@pytest.fixture(scope="module")
def etage():
    g = graines()
    return OR.EtageOrganisme(copie_organisme(), g.e(couche="essai", famille="organisme", role="racine"), "palier-0b|essai")


@pytest.fixture(scope="module")
def monde_et_dossier(tmp_path_factory):
    g = graines()
    s = MO.generer_suite(g, dict(couche="essai", famille="organisme", source=0), 0.5)
    m = s.cibles[0]
    d = str(tmp_path_factory.mktemp("monde") / m.nom)
    MO.ecrire_monde(d, m)
    return s, m, d


def test_forme_imposee_et_seuil_recopies_a_l_octet(etage):
    rng = np.random.default_rng(3)
    for _ in range(5):
        loi = L.loi_aleatoire(rng)
        assert EX.texte_du_test(loi) == etage.T.texte_du_test(loi)
        assert EX.test_de_mort_impose(loi) == etage.T.test_de_mort_impose(loi)
    from pole import tests_de_mort_v2 as v2
    for phrase in ("au moins 0,02", "au plus 0,02", "≥ 0.5", "strictement inférieur à -1", "0,3", "plus de 2,5 nat"):
        assert EX.lire_seuil(phrase) == tuple(v2.lire_seuil(phrase, "+")[:2]), phrase


def _entrees(s, m, n_par_domaine=5):
    """Des tentatives de toutes les sortes sur deux domaines à loi vraie : la loi vraie, la loi fausse, des compositions de la
    source, des lois neuves."""
    rng = np.random.default_rng(17)
    lois_rang = s.source.vraies_par_rang()
    out = []
    domaines = [d["nom"] for d in m.domaines if d["vraie"]][:2]
    for dom in domaines:
        d = m.domaine(dom)
        lois = [m.lois[d["vraie"]]["loi"], m.lois[d["fausse"]]["loi"], L.composer(lois_rang[0], lois_rang[1])]
        lois += [L.loi_aleatoire(rng) for _ in range(n_par_domaine - 3)]
        for loi in lois:
            eng = EX.engagement(dom, loi)
            out.append(R.nouvelle_entree(dom, eng, EX.sceller(eng), DESCRIPTION_FIXE, JUSTIFICATION_FIXE, PREDICTION_FIXE))
    return out


def _jouer(etage, s, m, d, dossier, executeur, echecs):
    entrees = _entrees(s, m)
    desaccords, vus = [], 0
    for k, (dom, lot) in enumerate(EN.lots_par_domaine(entrees)):
        for echoue in (False, True):
            sel = [i for i in lot if echecs[i] == echoue]
            if not sel:
                continue
            cartes, _ = EN.cartes_d_un_lot(entrees, sel, "avec_description")
            simules = {}
            for c, i in zip(cartes, sel):
                e = entrees[i]
                r, _ = executeur.eprouver(e["tentative"]["engagement"], e["tentative"]["engagement_sha256"],
                                          e["prediction_sha256"], m.tranche_epreuve(dom), echoue, 0.18)
                simules[c["identifiant"]] = r["classe"]
            lois = {c["identifiant"]: C_loi(entrees[i]) for c, i in zip(cartes, sel)}
            with open(os.path.join(d, "epreuve", dom, "episodes.csv"), encoding="utf-8") as f:
                lignes = f.read()
            verdicts = etage.eprouver_lot(os.path.join(dossier, f"lot-{k}-{int(echoue)}"), cartes, lois, lignes,
                                          "rien_envoye" if echoue else None)
            desaccords += OR.comparer_verdicts(simules, verdicts)
            vus += len(sel)
    return desaccords, vus, entrees


def C_loi(entree):
    return C.loi_du_texte(entree["tentative"]["engagement"]["test_de_mort"]["test"])


def test_garde_17_executeur_simule_contre_l_etage_de_l_organisme(etage, monde_et_dossier, tmp_path):
    s, m, d = monde_et_dossier
    echecs = [False, False, True, False, False, False, True, False, False, False]
    desaccords, vus, entrees = _jouer(etage, s, m, d, str(tmp_path / "sain"), EX.Executeur(), echecs)
    assert vus == len(entrees) == 10 and desaccords == []
    # au moins une tentative « tient » et une « ne tient pas » parmi celles qui ne sont pas en échec, pour que l'accord dise
    # quelque chose
    classes = {EX.Executeur().classe_sans_echec(C_loi(e), m.tranche_epreuve(e["probleme"])) for e in entrees}
    assert classes == {"tient", "ne tient pas"}
    fautifs, _, _ = _jouer(etage, s, m, d, str(tmp_path / "fautif"), EX.Executeur(sens_inverse=True), echecs)
    assert fautifs and all(f[1] != f[2] for f in fautifs)
    assert all(f[1] != NON_EXECUTABLE for f in fautifs)  # les échecs de l'expérimentateur restent d'accord


def test_garde_11_dans_la_consigne_servie_a_l_experimentateur(etage, monde_et_dossier, tmp_path):
    s, m, d = monde_et_dossier
    entrees = _entrees(s, m, 3)[:3]
    dom = entrees[0]["probleme"]
    cartes, _ = EN.cartes_d_un_lot(entrees, [0, 1, 2], "avec_description")
    lois = {c["identifiant"]: C_loi(e) for c, e in zip(cartes, entrees)}
    with open(os.path.join(d, "epreuve", dom, "episodes.csv"), encoding="utf-8") as f:
        lignes = f.read()
    etage.eprouver_lot(str(tmp_path / "lot"), cartes, lois, lignes)
    consignes = sorted(glob.glob(str(tmp_path / "lot" / "etage" / "noyau" / "tests-de-mort" / "*" / "experimentateur" /
                                      "traces-tour-001" / "consigne.md")))
    assert len(consignes) == 3
    for chemin in consignes:
        texte = open(chemin, encoding="utf-8").read()
        assert texte.count(DEBUT_DONNEES) >= 1 and texte.count(FIN_DONNEES) >= 1
        i = texte.find(DESCRIPTION_FIXE)
        assert i >= 0
        assert texte.rfind(DEBUT_DONNEES, 0, i) > texte.rfind(FIN_DONNEES, 0, i)  # la description est dans une section balisée
        assert JUSTIFICATION_FIXE not in texte
        assert not any(e["prediction_sha256"] in texte for e in entrees)


def test_garde_17_sur_une_source_entiere_de_la_couche_mecanique(etage, tmp_path):
    """Le chemin même de l'étape 4 : une source de la couche mécanique, chaque tentative de chaque génération (course source,
    trois bras, mondes cibles et monde final) passée aussi à l'étage de l'organisme ; aucun désaccord."""
    from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
    from controle_ia.heritage_etage_processeur_v1 import proposeurs as P
    g = graines()
    ctx = MC.ContexteSource(g, dict(couche="essai", famille="garde-17-source", proposeur="lecteur-heritage", dose=0.25, source=0),
                            P.configuration("lecteur-heritage", K=128), 0.25, 0.25, str(tmp_path / "source"), organisme=etage)
    out = MC.jouer_source(ctx)
    n_source = len(out["registre_source"].entrees)
    # le registre du bras 3 commence par la copie des entrées de la course source : elles ne sont comptées qu'une fois
    n = n_source + sum(len(out["bras"][b]["registre"].entrees) for b in "12") + len(out["bras"]["3"]["registre"].entrees) - n_source
    assert ctx.desaccords_organisme == [] and ctx.tentatives_vues_par_l_organisme >= n > 0


def test_copie_absente_ou_alteree_garde_non_jouee(tmp_path):
    with pytest.raises(OR.OrganismeIndisponible):
        OR.EtageOrganisme(str(tmp_path / "absente"), 1, "x")
    copie = str(tmp_path / "orchestrator")
    shutil.copytree(copie_organisme(), copie)
    with open(os.path.join(copie, "pole", "tests_de_mort_v5.py"), "a", encoding="utf-8") as f:
        f.write("\n# altéré\n")
    with pytest.raises(OR.OrganismeIndisponible):
        OR.verifier_copie(copie)
    assert OR.verifier_copie(copie_organisme())
    assert NON_EXECUTABLE == OR.CORRESPONDANCE_VERDICTS["non concluant"]
