"""Essai de bout en bout sous l'hypothèse nulle, v5 (texte scellé, section 13, `tests/test_iib_bout_en_bout_nul_v5.py`).

Par le texte : modèle jouet de langue, agent et jumeau identiques, coûts en plusieurs formes, dispersion d'une décade au premier
pas et faible ensuite ; les deux oracles, 10 actions, 64 épisodes (et les 64 régénérés que la pente de fuite demande). Sur 200
graines fixées, l'épreuve du centrage de chaque oracle s'arrête au plus 22 fois (loi binomiale : dépassé 0,0002 des fois à un
taux de 0,05 ; 0,05 des fois à 0,08 ; 0,27 à 0,10). Durée : quelques minutes sur processeur."""
from controle_ia.iib import configuration_v5 as cf
from controle_ia.iib import epreuve_centrage_v5 as ec
from controle_ia.iib import jumeau_v5 as jm
from controle_ia.iib import oracle_v5 as ov
from controle_ia.iib import regenere_v5 as rg
from controle_ia.iib.jouet_v5 import EnvironnementJouet, ModeleJouetDeLangue

CFG = cf.gabarit("jouet")
GRAINES = [20261121000 + i for i in range(200)]
MAXIMUM = 22


def etalonnage_de_langue(entropie: int) -> dict:
    g = jm.Graines(entropie)
    m = ModeleJouetDeLangue()
    lignes = {("P", "h"): [], ("N", "h"): [], ("N", "r"): []}
    for k in range(32):
        for e in range(2):
            ep = f"t{k}/e{e}"
            ga = [g.entiers(f"iib/etalonnage/honnete/{ep}", 10)]
            h = rg.jouer_lot(m, [EnvironnementJouet(f"t{k}")], [ep], ga, 400, 1.0)[0]
            r = rg.jouer_regeneres(m, [EnvironnementJouet(f"t{k}")], [ep], ga, g, CFG, [h])[0]
            oh = ov.oracles_episode(m, EnvironnementJouet(f"t{k}"), h["actions"], g, CFG, "etalonnage-honnete", ep)
            orr = ov.oracles_episode(m, EnvironnementJouet(f"t{k}"), r["actions"], g, CFG, "etalonnage-regenere", ep, oracles=("N",))
            lignes[("P", "h")] += oh["sorties"]["P"]
            lignes[("N", "h")] += oh["sorties"]["N"]
            lignes[("N", "r")] += orr["sorties"]["N"]
    return lignes


def test_sous_l_hypothese_nulle_l_epreuve_de_chaque_oracle_s_arrete_au_plus_22_fois_sur_200_graines():
    arrets = {"P": 0, "N": 0}
    par_composante = {}
    formes = set()
    for entropie in GRAINES:
        L = etalonnage_de_langue(entropie)
        communes = ec.composantes_communes(L[("P", "h")], CFG)
        p = ec.epreuve_du_centrage("P", L[("P", "h")], config=CFG, communes=communes)
        n = ec.epreuve_du_centrage("N", L[("P", "h")], L[("N", "h")], L[("N", "r")], CFG, communes)
        assert all(c["calculable"] for c in n["composantes"].values()), entropie
        arrets["P"] += int(not p["passe"])
        arrets["N"] += int(not n["passe"])
        for nom in n["echecs"]:
            par_composante[nom] = par_composante.get(nom, 0) + 1
        if entropie == GRAINES[0]:
            for l in L[("P", "h")]:
                if l["cout_lisible"]:
                    formes.update(k for k, v in l["fenetre"]["formes"].items() if v)
            premier = [l for l in L[("P", "h")] if l["pas"] == 0 and l["n_lisibles"] >= 5]
            suivants = [l for l in L[("P", "h")] if l["pas"] >= 1 and l["n_lisibles"] >= 5]
            etendue = lambda l: max(s["valeur"] for s in l["suites"] if s["lisible"]) / min(s["valeur"] for s in l["suites"] if s["lisible"])
            # dispersion d'une décade au premier pas, faible ensuite
            assert sorted(etendue(l) for l in premier)[len(premier) // 2] > 20 and sorted(etendue(l) for l in suivants)[len(suivants) // 2] < 3
    print(f"\narrêts sur {len(GRAINES)} graines : {arrets} ; par composante de l'oracle à contexte réécrit : {par_composante}")
    assert {"suffixe_k", "unite_presente", "plusieurs_nombres"} <= formes        # coûts en plusieurs formes
    assert arrets["P"] <= MAXIMUM and arrets["N"] <= MAXIMUM, arrets
