"""Lot B1, v6 — essais des neuf changements exigés par le brouillon 3 du préenregistrement (`e33d7bec…`, § Mondes
plantés et tests de mort, « Changements de code exigés (version 6) »), cas sains et artefacts (R5)."""
import json
from fractions import Fraction

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.oracles_plantes_v6 import banque as banque_mod
from controle_ia.oracles_plantes_v6.forme_seule import (borne_naturelle, ecarts_p9, ecarts_p10, mesurer,
                                                        regle_borne_non_naturelle, regle_forme_seule)
from controle_ia.oracles_plantes_v6.graines import ENFANTS, generateur, graine
from controle_ia.oracles_plantes_v6.lignee import Registre
from controle_ia.oracles_plantes_v6.normalisation import normaliser
from controle_ia.oracles_plantes_v6.parametres import charger
from controle_ia.oracles_plantes_v6.tests_de_mort import TypeIssue, appliquer_batterie, sortie_de_texte, t5_redite

P, _ = charger()


@pytest.fixture(scope="module")
def banque11():
    return banque_mod.construire_banque(11, P)


def _verites(m, plantes):
    return [p for p in plantes if p.etiquette == "VERITE_PLANTEE"]


# ---------------------------------------------------------------- 1. cinq gabarits à indice k tiré
GABARITS_K = {"F1": ["vt_au_dessus_de_sa_valeur_a_k", "puissance_au_dessus_de_sa_valeur_a_k"],
              "F2": ["intersection_tours_au_dessus_de_sa_valeur_a_k", "union_tours_au_dessus_de_sa_valeur_a_k"],
              "F3": ["v_au_dessus_de_v_k"]}


def test_c1_gabarits_a_k_tire(banque11):
    ks = set()
    for m, plantes in banque11:
        for p in plantes:
            if p.gabarit in GABARITS_K[m.famille]:
                k = int(p.texte.split(">= ")[1].split(" implique")[0])
                assert 2 <= k <= m.N
                ks.add((m.famille, k))
                assert regle_forme_seule(m.analyser(p.texte)) and not borne_naturelle(m.analyser(p.texte))
    assert len(ks) > 3  # k varie d'un monde à l'autre


def test_c1_raison_generale_au_dela_de_3N(banque11):
    from controle_ia.oracles_plantes_v6.tests_de_mort import t2_contre_exemple
    for m, plantes in banque11[4:]:  # F2 et F3 jusqu'à 6N (F1 : variation totale bornée à 3N + 2 pas)
        for p in plantes:
            if p.gabarit in GABARITS_K[m.famille]:
                assert not t2_contre_exemple(m.analyser(p.texte), m, 6 * m.N).tue()


# ---------------------------------------------------------------- 2. étage 3 non appliqué entre vérités plantées
def test_c2_racine_24_plante_desormais():
    b = banque_mod.construire_banque(24, P)  # v5 : refusée (F2, monde 4)
    m, plantes = b[4]
    assert any(p.gabarit == "union_tours_au_dessus_de_sa_valeur_a_k" for p in plantes)


def test_c2_etages_de_t5_selectionnables(banque11):
    m, _ = banque11[8]
    fa, fb = (normaliser(m.analyser(t), m, m.ev) for t in ("pour tout n dans NAT, u(n) <= 50",
                                                            "pour tout n dans NAT, u(n) < 51"))
    assert t5_redite(fb, m, [fa]).type == TypeIssue.REDITE  # cas sain : l'étage 3 voit la redite
    assert t5_redite(fb, m, [fa], etages=(1, 2)).type == TypeIssue.NON_REDITE  # étages 1 et 2 seulement


# ---------------------------------------------------------------- 3. mondes perturbés distincts
def test_c3_mondes_perturbes_distincts(banque11):
    for m, _ in banque11:
        sig = [banque_mod._signature(x) for x in [m] + m.perturbes]
        assert len(set(sig)) == len(sig) == 1 + int(P["redite"]["mondes_perturbes"])


def test_c3_artefact_tirage_toujours_identique(banque11):
    m, _ = banque11[0]

    class Fige:  # un monde dont toute perturbation redonne le monde réel
        famille = "F1"
        indice = 0
        parametres_servis = m.parametres_servis
        constantes = m.constantes

        def perturbe(self, rng):
            return m

    with pytest.raises(GardeArret, match="distincts"):
        banque_mod.mondes_perturbes_distincts(Fige(), None, 3, essais_max=5)


# ---------------------------------------------------------------- 4. exception « retrouvée » dans la redite
def test_c4_retrouvee_jamais_redite_par_le_profil_seul(banque11):
    m, plantes = banque11[8]
    verites = [normaliser(m.analyser(p.texte), m, m.ev) for p in _verites(m, plantes)]
    T = next(p.texte for p in plantes if p.gabarit == "v_au_dessus_de_v_k")
    c = T.split(">= ")[-1]
    ant = [normaliser(m.analyser(T.replace(">= " + c, "> " + c + " - 1/1000000000")), m, m.ev)]  # même profil
    sans = appliquer_batterie(sortie_de_texte(T), m, anterieures=ant)
    assert sans.redite and sans.redite_etage == 3  # sans les vérités plantées : redite par l'étage 3
    avec = appliquer_batterie(sortie_de_texte(T), m, anterieures=ant, verites=verites)
    assert not avec.redite and avec.redite_levee_retrouvee and avec.redite_etage == 3


def test_c4_cas_sain_non_retrouvee_reste_redite(banque11):
    m, plantes = banque11[8]
    verites = [normaliser(m.analyser(p.texte), m, m.ev) for p in _verites(m, plantes)]
    C = m.u(m.N + 3)  # vrai jusqu'à N, faux au-delà : vivante, non retrouvée
    ant = [normaliser(m.analyser(f"pour tout n dans NAT, u(n) <= {C}"), m, m.ev)]
    r = appliquer_batterie(sortie_de_texte(f"pour tout n dans NAT, u(n) < {C + 1}"), m, anterieures=ant, verites=verites)
    assert r.statut == "vivante" and r.redite and r.redite_etage == 3 and not r.redite_levee_retrouvee


# ---------------------------------------------------------------- 5. graines (10, 0) et (10, 1)
def test_c5_sous_enfants_de_10():
    assert "(10, 0)" in ENFANTS[10] and "(10, 1)" in ENFANTS[10]
    a, b = graine(7, 10, 0).generate_state(2), graine(7, 10, 1).generate_state(2)
    assert list(a) != list(b)


# ---------------------------------------------------------------- 6. P10, et P9 par monde
def test_c6_p9_p10_exactes_par_monde(banque11):
    mes = mesurer(banque11, generateur(11, 10, 0), 4, "1")
    assert ecarts_p9(mes) == [] and ecarts_p10(mes) == []
    b = mes["borne_non_naturelle"]
    assert (b["PIEGE"]["taux"], b["FAUX_TOT"]["taux"], b["VERITE_PLANTEE"]["taux"]) == ("1", "1/2", "1/4")


def test_c6_artefact_p10_par_monde():
    mes = {"regle_fixe": {k: {"declares_faux": a, "plantes": n} for k, (a, n) in
                          {"PIEGE": (4, 4), "FAUX_TOT": (2, 4), "VERITE_PLANTEE": (4, 8)}.items()},
           "regle_fixe_par_monde": [{"PIEGE": [4, 4], "FAUX_TOT": [2, 4], "VERITE_PLANTEE": [4, 8]}],
           "borne_non_naturelle": {k: {"declares_faux": a, "plantes": n} for k, (a, n) in
                                   {"PIEGE": (4, 4), "FAUX_TOT": (2, 4), "VERITE_PLANTEE": (2, 8)}.items()},
           "borne_non_naturelle_par_monde": [{"PIEGE": [4, 4], "FAUX_TOT": [2, 4], "VERITE_PLANTEE": [3, 8]}]}
    assert ecarts_p9(mes) == []
    e = ecarts_p10(mes)
    assert len(e) == 1 and e[0].startswith("A1 (P10) : monde 0")


@pytest.mark.parametrize("texte,attendu", [
    ("pour tout t dans NAT, vt(t) < 1", False), ("pour tout t dans NAT, vt(t) <= K", False),
    ("pour tout t dans NAT, vt(t) < 7/9", True), ("pour tout t dans NAT, mod(t, 3) != 1", True),
    ("pour tout t dans NAT, vt(t) = 7/9", False)])
def test_c6_regle_borne_non_naturelle(banque11, texte, attendu):
    m, _ = banque11[0]
    assert regle_borne_non_naturelle(m.analyser(texte)) is attendu


def test_c6_plantation_refuse_un_faux_tot_a_borne_naturelle(monkeypatch, banque11):
    m, _ = banque11[8]
    ft = m.gabarits_faux_tot

    def naturel(rng):
        g = ft(rng)
        return [("seuil_u_tot", ["pour tout n dans NAT, u(n) < 1"])] + g[1:]  # faux en 0, borne naturelle

    monkeypatch.setattr(m, "gabarits_faux_tot", naturel)
    with pytest.raises(GardeArret):
        banque_mod.planter(m, 11, P)


# ---------------------------------------------------------------- 7. aires par pli, hors textes vus, textes répétés
def test_c7_aires_et_textes_repetes(banque11):
    cs_tot = mesurer(banque11, generateur(11, 10, 0), 4, "1")
    cs = cs_tot["classifieur_de_style"]
    assert len(cs["par_pli"]) == 4
    hv = cs["hors_textes_vus"]
    foi = max(Fraction(hv["aire_pieges_contre_verites"]), Fraction(hv["aire_faux_tot_contre_verites"]))
    assert Fraction(cs["aire_qui_fait_foi"]) == foi
    assert cs["au_dessus_du_seuil"] == (foi > Fraction(3, 4))
    assert hv["effectifs"]["VERITE_PLANTEE"] < 96  # des vérités répétées entre mondes sont écartées
    assert cs_tot["textes_identiques_entre_mondes"]["PIEGE"] == 0


# ---------------------------------------------------------------- 8. paramètres : seule part provisoire, le classifieur
def test_c8_part_provisoire_reduite():
    assert len(P["provisoire"]) == 1 and "classifieur" in P["provisoire"][0]
    assert "brouillon 3" in P["statut"]


# ---------------------------------------------------------------- règle de retirage (d)
def test_retirage_premiere_racine_plantable(monkeypatch):
    vraie = banque_mod.construire_banque

    def refuse_5(r, params):
        if r == 5:
            raise GardeArret("refus d'essai")
        return vraie(r, params)

    monkeypatch.setattr(banque_mod, "construire_banque", refuse_5)
    r, b, journal = banque_mod.construire_banque_avec_retirage([5, 11], P)
    assert r == 11 and journal[0]["refus"] == "refus d'essai" and journal[1]["refus"] is None


def test_retirage_au_plus_trois_puis_arret(monkeypatch):
    monkeypatch.setattr(banque_mod, "construire_banque", lambda r, p: (_ for _ in ()).throw(GardeArret("non")))
    with pytest.raises(GardeArret, match="retour au concepteur"):
        banque_mod.construire_banque_avec_retirage([1, 2, 3], P)
    with pytest.raises(GardeArret, match="au plus 3"):
        banque_mod.construire_banque_avec_retirage([1, 2, 3, 4], P)


def test_rejeu_consigne_les_racines_tirees(tmp_path, monkeypatch):
    import controle_ia.oracles_plantes_v6.banque as bm
    from controle_ia.oracles_plantes_v6 import rejeu
    vraie = bm.construire_banque

    def refuse_5(r, params):
        if r == 5:
            raise GardeArret("refus d'essai")
        return vraie(r, params)

    monkeypatch.setattr(bm, "construire_banque", refuse_5)
    code, rapport = rejeu.executer([5, 11], tmp_path / "s")
    m = json.loads((tmp_path / "s" / "manifeste-rejeu-v6.json").read_text(encoding="utf-8"))
    assert code == 0 and rapport["racine"] == "11"
    assert [x["racine"] for x in m["racines_tirees"]] == ["5", "11"] and m["racines_tirees"][0]["refus"]


# ---------------------------------------------------------------- invariant : aucune vérité ne meurt ni n'arrête
def test_invariant_banque_entiere_avec_registre(tmp_path, banque11):
    reg = Registre(tmp_path / "r.jsonl")
    for m, plantes in banque11:
        for p in plantes:
            r = appliquer_batterie(sortie_de_texte(p.texte), m, registre=reg)
            if p.etiquette == "VERITE_PLANTEE":
                assert r.statut == "vivante" and r.vraie_bornee
