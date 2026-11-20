"""Essai du contre-lecteur (modèle S) : un témoin « complet » est un témoin aux cinq rendus OBTENUS (décision n° 1 de la
mère). Un rendu « absent » (refusé deux fois) n'est pas obtenu : 40 témoins aux cinq rendus tentés dont un à rendu absent
= 39 complets obtenus -> « non concluant par manque de témoins » ; le compte des tentés (40) est rapporté à côté."""
import essais_etalonnage_lecture_ligne_3_v1 as E

ET, LI = E.ET, E.LI


def test_un_rendu_absent_n_est_pas_obtenu_donc_pas_complet(tmp_path):
    plan = E.plan_factice(E.banque_factice(200))
    lecture_b = [p for p in plan if p["bloc"] == "B" and p["moitie"] == "lecture"]
    cible = lecture_b[0]["id"]                                   # un rendu du bloc B, premier témoin de la moitié « lecture »
    m = E.monde_complet(tmp_path, coupe_b=40 * 3, sous=5, absents={cible})
    assert m["rapport"]["complets"]["bloc_B_moitie_lecture"] == 39       # le code d'appel : cinq rendus obtenus
    r = E.lire(m)["rapport"]
    assert r["temoins"]["complets_moitie_lecture"] == 39                 # la lecture suit le code d'appel
    assert r["temoins"]["complets_moitie_lecture_tentes"] == 40          # le compte des tentés reste rapporté
    t = r["table_de_lecture"]
    assert t["rang"] == 1 and t["mot"] == "non concluant par manque de témoins"
    assert any("moins de 40" in c for c in t["causes_du_rang_1"])


def test_cas_sain_sans_absent_les_deux_comptes_sont_egaux(tmp_path):
    m = E.monde_complet(tmp_path, coupe_b=40 * 3, sous=5)
    r = E.lire(m)["rapport"]
    assert r["temoins"]["complets_moitie_lecture"] == r["temoins"]["complets_moitie_lecture_tentes"] == 40
    assert r["temoins"]["complets_cinq_rendus"] == r["temoins"]["complets_cinq_rendus_tentes"]
