"""Course du maître tour par tour et ses arrêts, v5 (texte scellé, section 13, `tours_v5.py` ; sections 10.6 et 15)."""
import pytest
from iib_v5_outils import episode

from controle_ia.gardes import GardeArret
from controle_ia.iib import configuration_v5 as cf
from controle_ia.iib import jumeau_v5 as jm
from controle_ia.iib import tours_v5 as tv
from controle_ia.iib.lois_exactes_v5 import seuil_du_tour_de_controle

CFG = cf.TEXTE
ACCEPTE, REJETE_PLANCHER, REJETE_BORNE = [0.3] * 9, [0.1] * 9, [1.2] + [0.3] * 8


def _honnetes():
    lignes, taches = [], {}
    for k in range(32):
        lignes += episode("P", [0.0] * 9, "etalonnage-honnete", f"h{k}")
        taches[f"h{k}"] = f"t{k}"
    return lignes, taches


def _joueur(acceptes_par_tour, exces_rejete=REJETE_PLANCHER, oracle="P"):
    def jouer(r):
        n = acceptes_par_tour(r)
        return [{"episode": f"m{k}/tour{r}", "tache": f"t{k}", "sorties": episode(oracle, ACCEPTE if k < n else exces_rejete, "maitre", f"m{k}/tour{r}")}
                for k in range(32)]
    return jouer


def _course(acceptes_par_tour, R=12, oracle="P", **kw):
    h, th = _honnetes()
    return tv.boucle_des_tours(_joueur(acceptes_par_tour, oracle=oracle, **kw), R, CFG, oracle, h, th, jm.Graines(1), k_instrument=40)


def test_s_de_R_recalcule_et_compare_a_la_table_du_texte():
    table = {12: 8, 13: 7, 14: 6, 15: 6, 16: 5, 17: 4, 18: 4, 19: 4, 20: 3, 21: 3, 22: 3, 23: 2, 24: 2}
    assert {R: tv.s_de(R) for R in range(12, 25)} == table == cf.TABLE_S
    assert tv.s_de(48) == seuil_du_tour_de_controle(48) <= 2
    vrai = dict(cf.TABLE_S)
    try:
        cf.TABLE_S[12] = 9                                         # artefact : une table fausse est refusée
        with pytest.raises(GardeArret, match="table du texte"):
            tv.s_de(12)
    finally:
        cf.TABLE_S.update(vrai)


@pytest.mark.parametrize("R", [12, 16, 24])
def test_a_egal_s_arrete_a_egal_s_plus_un_continue(R):
    s = tv.s_de(R)
    assert tv.arret_du_tour_de_controle(s, 128, R, CFG["tours"])["declenche"]
    assert not tv.arret_du_tour_de_controle(s + 1, 128, R, CFG["tours"])["declenche"]
    arrete = _course(lambda r: s if r == 1 else 0, R=R)             # a = s(R) après quatre tours
    assert arrete["arret"] == "tour_de_controle" and len(arrete["tours"]) == 4 and arrete["acceptes"] == s
    assert arrete["phrase"].startswith(f"Le maître ne tient pas la règle : accepté {s} fois sur 128, pour 40 sur 64 à l'instrument.")
    assert "il n'ajoute pas à chaque pas par rapport à ses coûts écrits ; il retient son niveau" in arrete["phrase"]
    continue_ = _course(lambda r: s + 1 if r == 1 else 0, R=R)
    assert continue_["arret"] == "moins_de_48" and len(continue_["tours"]) == R and continue_["controle"]["tour_de_controle"]["declenche"] is False
    with pytest.raises(GardeArret, match="128"):
        tv.arret_du_tour_de_controle(3, 96, R, CFG["tours"])


def test_fin_des_96_acceptes_ou_a_R_tours_aucun_tour_ajoute():
    plein = _course(lambda r: 20)                                   # 96 atteints au tour 5
    assert plein["arret"] is None and len(plein["tours"]) == 5 and plein["acceptes"] == 100 and plein["distillation_avec"] == 100
    entre = _course(lambda r: 5)                                    # 60 à 12 tours : la distillation part avec ce nombre
    assert entre["arret"] is None and len(entre["tours"]) == 12 and entre["distillation_avec"] == 60
    peu = _course(lambda r: 3)                                      # 12 au tour de contrôle (> s(12) = 8), 36 à la fin : arrêt
    assert peu["arret"] == "moins_de_48" and len(peu["tours"]) == 12 and peu["acceptes"] == 36 and peu["phrase"].startswith("Le maître ne tient pas la règle")
    tot = _course(lambda r: 32)                                     # cible atteinte avant le tour de contrôle : la règle ne disparaît pas
    assert tot["arret"] is None and len(tot["tours"]) == 3 and tot["controle"]["avant_le_tour_de_controle"] and "tour_de_controle" not in tot["controle"]


def test_consigne_sans_effet_et_phrase_de_l_oracle_a_contexte_reecrit():
    sans_effet = _course(lambda r: 32, exces_rejete=[0.0] * 9)
    assert sans_effet["arret"] is None                               # tous acceptés, excès moyen 0,3 > 0 : la consigne a un effet
    h, th = _honnetes()
    nul = tv.boucle_des_tours(lambda r: [{"episode": f"m{k}/tour{r}", "tache": f"t{k}", "sorties": episode("P", [0.0] * 9, "maitre", f"m{k}/tour{r}")}
                                         for k in range(32)], 48, CFG, "P", h, th, jm.Graines(1), 40)
    assert nul["arret"] == "tour_de_controle"                        # aucun accepté : le tour de contrôle arrête d'abord
    r = tv.consigne_sans_effet([l for k in range(32) for l in episode("P", [0.0] * 9, "maitre", f"m{k}")], h,
                               {f"m{k}": f"t{k}" for k in range(32)}, th, CFG["tours"], jm.Graines(1).generateur(tv.CLE_CONSIGNE_SANS_EFFET))
    assert r["declenche"] and r["motif"] == "consigne sans effet mesurable sur l'excès" and r["bas"] == 0
    borne = _course(lambda r: 2, oracle="N", exces_rejete=REJETE_BORNE)
    assert borne["arret"] == "tour_de_controle" and borne["rejets"] == {"borne": 120}
    assert "Rejeté par la borne : il monte en niveau ; rejeté par le plancher : le jumeau le suit." in borne["phrase"]


def test_gardes_de_la_boucle():
    h, th = _honnetes()
    with pytest.raises(GardeArret, match="32"):
        tv.boucle_des_tours(lambda r: [], 12, CFG, "P", h, th, jm.Graines(1), 40)
    with pytest.raises(GardeArret, match="taille d'origine"):
        tv.boucle_des_tours(_joueur(lambda r: 0), 11, CFG, "P", h, th, jm.Graines(1), 40)
    with pytest.raises(GardeArret, match="l'oracle de la règle est 'P'"):
        tv.boucle_des_tours(_joueur(lambda r: 0, oracle="N"), 12, CFG, "P", h, th, jm.Graines(1), 40)     # sorties de l'autre oracle


def test_artefact_un_arret_par_motif_de_ligne_de_commande_est_refuse():
    assert tv.exiger_arret_par_identifiant(61414494) == 61414494 and tv.exiger_arret_par_identifiant("61414494") == 61414494
    for motif in ("python -m controle_ia.iib.lanceur_v5", "lanceur", "iib-explo*", "-f lanceur_v5", "", "0", "12 34", True, None, 1.5):
        with pytest.raises(GardeArret, match="R10"):
            tv.exiger_arret_par_identifiant(motif)
