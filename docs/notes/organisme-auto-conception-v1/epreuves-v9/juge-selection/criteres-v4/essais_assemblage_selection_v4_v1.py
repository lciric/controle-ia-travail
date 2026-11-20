# -*- coding: utf-8 -*-
"""Essais de assemblage_selection_v4_v1.py — cartes et lectures SYNTHÉTIQUES, inventées ici.

Aucune vraie carte, aucune vraie lecture. Pour chaque garde : un cas sain et un artefact (R5).
Lancement : python3 -B -m pytest -q essais_assemblage_selection_v4_v1.py
"""
import copy
import hashlib
import json
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import assemblage_selection_v4_v1 as A  # noqa: E402

H1 = hashlib.sha256(b"criteres synthetiques").hexdigest()
FAMILLES = {"opus": "maison", "fable": "maison", "argon": "argon", "astra": "astra", "carbon": "carbon"}
LIGNEES = ["opus", "fable", "argon", "astra", "carbon"]


def manifeste(**k):
    m = {"identifiant_course": "course-synthetique-1", "usage": "rejeu", "ligne_accord": None,
         "criteres_sha256": H1, "nombre_vise": 9, "veto_par_titulaire": "selon_titulaires", "suppleantes": 6,
         "filtre_veto": "famille", "plafond_veto": "nombre_vise", "regime_items": "tous", "seuil_accord": 0.75,
         "lignee_reconnue_declaree": False, "emploie_lectures_v2": False, "familles": dict(FAMILLES),
         "hors_choix": ["x-hors-1"], "cartes_attendues": 40}
    m.update(k)
    return m


def carte(ident, voie, sous, items, e=2, q=2, d=2, excl=None, groupe=None):
    return {"id": ident, "exclusion": excl, "voie": voie, "sous_strate": sous,
            "question": "question synthétique", "E": e, "Q": q, "D": d,
            "raisons": {"E": "raison E", "Q": "raison Q", "D": "raison D"},
            "items": dict(items), "phrases": {i: "phrase" for i in A.ITEMS}, "groupe_fusion": groupe}


def monde(n=40, graine=1, bruit=0.05):
    """Deux lectures synthétiques presque d'accord, et une table d'espèces."""
    gen = np.random.Generator(np.random.PCG64(np.random.SeedSequence(graine)))
    strates = [("I", None), ("N", None)] + [("P", s) for s in A.SOUS_STRATES]
    cf, co, especes = [], [], {}
    for i in range(n):
        ident = f"s{i:03d}"
        voie, sous = strates[i % len(strates)]
        force = gen.random()
        base = {it: ("oui" if gen.random() < force else "non") for it in A.ITEMS}
        autre = {it: (r if gen.random() > bruit else ("non" if r == "oui" else "oui")) for it, r in base.items()}
        cf.append(carte(ident, voie, sous, base))
        co.append(carte(ident, voie, sous, autre))
        especes[ident] = LIGNEES[i % 5]
    lf = {"lecteur": "F", "lignee": "fable", "independance": "je n'ai écrit ni les critères ni une carte", "cartes": cf, "veto": []}
    lo = {"lecteur": "O", "lignee": "opus", "independance": "je n'ai écrit ni les critères ni une carte", "cartes": co, "veto": []}
    return lf, lo, especes


def veto(ident):
    return {"id": ident, "prediction": "oui attendu", "decision": "garder le module", "lignee_reconnue": "aucune"}


def jouer(lf, lo, m, especes=None, **k):
    return A.assembler_coeur(A.valider_lecture(lf, "F", m), A.valider_lecture(lo, "O", m), m, H1, especes, **k)


# ---------------------------------------------------------------- cas sain de bout en bout

def test_cas_sain_et_reproductible():
    lf, lo, esp = monde()
    m = manifeste()
    a, b = jouer(lf, lo, m, esp), jouer(lf, lo, m, esp)
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
    assert len(a["listes"]["nombre_vise"]) == 9
    assert a["en_tete"][0] == A.PRINCIPE and A.LIMITE_FAMILLE in a["en_tete"] and A.REJEU in a["en_tete"]
    assert A.SIGNAL_V2 not in a["en_tete"]
    assert sorted(a["tirages"]["ordre_des_voies"]) == ["I", "N", "P"]
    assert sorted(a["tirages"]["permutation_des_cartes"]) == list(range(40))
    # les trois voies ont chacune au moins leurs deux places réservées
    voies = [p["voie"] for p in a["listes"]["nombre_vise"]]
    assert all(voies.count(v) >= 2 for v in "INP")
    # rien n'est éliminé par le nombre visé : toute ligne au plancher est listée
    hors = sum(len(v) for v in a["listes"]["au_plancher_hors_du_nombre_vise"].values())
    assert hors + 9 == a["comptes"]["lignes_au_plancher"]


def test_signal_v2_en_tete_si_les_lectures_v2_sont_employees():
    lf, lo, esp = monde()
    a = jouer(lf, lo, manifeste(emploie_lectures_v2=True), esp)
    assert A.SIGNAL_V2 in a["en_tete"]


def test_tirage_conforme_a_la_construction_ecrite():
    lf, lo, esp = monde()
    m = manifeste()
    a = jouer(lf, lo, m, esp)
    h2 = hashlib.sha256(m["identifiant_course"].encode()).hexdigest()
    racine = np.random.SeedSequence([int(H1, 16), int(h2, 16)])
    e = racine.spawn(4)
    perm = np.random.Generator(np.random.PCG64(e[0])).permutation(3)
    assert a["tirages"]["ordre_des_voies"] == [["I", "N", "P"][i] for i in perm]
    perm1 = np.random.Generator(np.random.PCG64(e[1])).permutation(40)
    assert a["tirages"]["permutation_des_cartes"] == [int(x) for x in perm1]


def test_voie_p_couvre_les_sous_strates_avant_de_doubler():
    lf, lo, esp = monde(n=45)
    a = jouer(lf, lo, manifeste(cartes_attendues=45, nombre_vise=13), esp)
    lignes = {l["porteuse"]: l for l in a["lignes"]}
    sous = [lignes[p["porteuse"]]["sous_strates"][0] for p in a["listes"]["nombre_vise"] if p["voie"] == "P"]
    assert len(sous) == len(set(sous))  # aucune sous-strate doublée tant qu'une autre est libre


# ---------------------------------------------------------------- gardes d'entrée : sain / artefact

@pytest.mark.parametrize("cle,val", [
    ("usage", "course"), ("nombre_vise", 0), ("veto_par_titulaire", 4), ("filtre_veto", "espece"),
    ("regime_items", "autre"), ("seuil_accord", 0), ("plafond_veto", "K"), ("familles", {}),
    ("emploie_lectures_v2", "non")])
def test_manifeste_refuse(cle, val):
    A.valider_manifeste(manifeste())  # cas sain
    with pytest.raises(A.Refus):
        A.valider_manifeste(manifeste(**{cle: val}))


def test_manifeste_cle_manquante_ou_en_trop():
    m = manifeste()
    del m["plafond_veto"]
    with pytest.raises(A.Refus):
        A.valider_manifeste(m)
    with pytest.raises(A.Refus):
        A.valider_manifeste(manifeste(reglage_cache=1))


def test_usage_course_exige_la_ligne_d_accord():
    A.valider_manifeste(manifeste(usage="course", ligne_accord="GO-AAAA-MM-JJ-NN"))
    with pytest.raises(A.Refus):
        A.valider_manifeste(manifeste(usage="course", ligne_accord="  "))


def _casse(mut):
    lf, lo, _ = monde()
    mut(lf)
    return lf


@pytest.mark.parametrize("mut", [
    lambda l: l["cartes"][0].update(E=3),
    lambda l: l["cartes"][0]["raisons"].update(D=" "),
    lambda l: l["cartes"][0]["items"].pop("T1"),
    lambda l: l["cartes"][0]["items"].update(T1="ajoutable"),
    lambda l: l["cartes"][0]["items"].update(T2="peut-être"),
    lambda l: l["cartes"][0].update(meta={"proposeur": "x"}),
    lambda l: l["cartes"][0].update(espece="astra"),
    lambda l: l["cartes"][0].update(voie="Z"),
    lambda l: l["cartes"][2].update(sous_strate=None),
    lambda l: l["cartes"][0].update(exclusion={"cas": "X1", "phrase": "p"}),
    lambda l: l["cartes"][0].update(exclusion={"cas": "X9", "phrase": "p"}),
    lambda l: l["cartes"].append(copy.deepcopy(l["cartes"][0])),
    lambda l: l.update(independance=""),
    lambda l: l.update(lignee="inconnue"),
    lambda l: l["cartes"][0]["phrases"].update(B1=""),
    lambda l: l.update(veto=[veto("s001"), veto("s001")]),
    lambda l: l.update(veto=[{"id": "s001", "prediction": "", "decision": "d", "lignee_reconnue": "aucune"}]),
])
def test_lecture_mal_formee_refusee(mut):
    m = manifeste()
    lf, _, _ = monde()
    A.valider_lecture(lf, "F", m)  # cas sain
    with pytest.raises(A.Refus):
        A.valider_lecture(_casse(mut), "F", m)


def test_ajoutable_permis_sur_les_sept_items_seulement():
    m = manifeste()
    lf, _, _ = monde()
    for it in sorted(A.AJOUTABLES):
        lf["cartes"][0]["items"][it] = "ajoutable"
    A.valider_lecture(lf, "F", m)


def test_lignee_reconnue_exigee_seulement_si_decidee():
    lf, lo, esp = monde()
    with pytest.raises(A.Refus):
        A.valider_lecture(lf, "F", manifeste(lignee_reconnue_declaree=True))
    for c in lf["cartes"]:
        c["lignee_reconnue"] = "aucune"
    A.valider_lecture(lf, "F", manifeste(lignee_reconnue_declaree=True))
    with pytest.raises(A.Refus):  # et refusée quand elle n'est pas décidée
        A.valider_lecture(lf, "F", manifeste())


def test_cartes_differentes_hors_choix_et_compte():
    lf, lo, esp = monde()
    m = manifeste()
    jouer(lf, lo, m, esp)
    lo2 = copy.deepcopy(lo)
    lo2["cartes"].pop()
    with pytest.raises(A.Refus):
        jouer(lf, lo2, m, esp)
    with pytest.raises(A.Refus):
        jouer(lf, lo, manifeste(hors_choix=["s000"]), esp)
    with pytest.raises(A.Refus):
        jouer(lf, lo, manifeste(cartes_attendues=41), esp)


def test_numpy_trop_ancien_refuse():
    assert A.verifier_numpy("1.25.0") == "1.25.0"
    assert A.verifier_numpy("2.5.3") == "2.5.3"
    with pytest.raises(A.Refus):
        A.verifier_numpy("1.24.4")
    with pytest.raises(A.Refus):
        A.verifier_numpy("inconnue")


# ---------------------------------------------------------------- exclusions

def test_exclusions_meme_cas_cas_differents_et_x1():
    lf, lo, esp = monde()
    x3 = {"cas": "X3", "phrase": "p"}
    lf["cartes"][0]["exclusion"] = x3
    lo["cartes"][0]["exclusion"] = dict(x3)                                   # écartée
    lf["cartes"][1]["exclusion"] = x3                                         # un seul lecteur : notée
    lf["cartes"][2]["exclusion"] = x3
    lo["cartes"][2]["exclusion"] = {"cas": "X5", "phrase": "p"}               # cas différents : notée
    for i, (sf, so) in {3: (False, False), 4: (True, True), 5: (True, False)}.items():
        lf["cartes"][i]["exclusion"] = {"cas": "X1", "phrase": "p", "separable": sf}
        lo["cartes"][i]["exclusion"] = {"cas": "X1", "phrase": "p", "separable": so}
    a = jouer(lf, lo, manifeste(), esp)
    st = {c["id"]: c["statut"] for c in a["cartes"]}
    assert st["s000"] == "ecartee" and st["s001"] == "notee" and st["s002"] == "notee"
    assert st["s003"] == "rendue_a_lazar" and st["s004"] == "notee" and st["s005"] == "notee"
    assert a["listes"]["rendues_a_lazar"] == ["s003"] and a["listes"]["ecartees"] == ["s000"]
    des = {d["id"]: d["desaccords"] for d in a["desaccords"]}
    assert any("séparabilité en désaccord" in x for x in des["s005"])
    assert any("cas différents" in x for x in des["s002"])
    # une carte rendue à Lazar n'est ni dans le nombre visé, ni dans le lot
    assert "s003" not in [p["porteuse"] for p in a["listes"]["nombre_vise"]]
    assert "s003" not in [p["porteuse"] for p in a["listes"]["tirees_au_sort"]]
    # le numéro de tirage porte sur toutes les cartes lues, écartées comprises
    assert len({c["numero_de_tirage"] for c in a["cartes"]}) == 40


# ---------------------------------------------------------------- plancher, items, kappa

def test_plancher_un_seul_lecteur_suffit_et_echelle_fine_n_y_entre_pas():
    lf, lo, esp = monde()
    lf["cartes"][0].update(E=1, Q=1, D=1)       # 3 sur 6 chez F
    lo["cartes"][0].update(E=2, Q=1, D=1)       # 4 sur 6 chez O : au plancher
    lf["cartes"][1].update(E=1, Q=1, D=1)
    lo["cartes"][1].update(E=1, Q=1, D=1)       # sous le plancher chez les deux
    for it in A.ITEMS:                          # zéro sur toute l'échelle : reste au plancher
        lf["cartes"][7]["items"][it] = "non"
        lo["cartes"][7]["items"][it] = "non"
    a = jouer(lf, lo, manifeste(), esp)
    pl = {c["id"]: c["au_plancher"] for c in a["cartes"]}
    assert pl["s000"] is True and pl["s001"] is False and pl["s007"] is True
    assert "s001" in a["listes"]["sous_le_plancher"]
    assert "s001" not in [p["porteuse"] for p in a["listes"]["nombre_vise"]]


def test_item_sans_accord_retire_du_rang_et_kappa_rapporte():
    lf, lo, esp = monde(bruit=0.0)
    a = jouer(lf, lo, manifeste(), esp)
    assert len(a["tenue"]["items_gardes"]) == 18        # cas sain : accord parfait
    assert a["items"]["B2"]["kappa"] == pytest.approx(1.0)
    for i, c in enumerate(lo["cartes"]):                # artefact : O contredit F sur B2 une fois sur deux
        if i % 2 == 0:
            c["items"]["B2"] = "non" if lf["cartes"][i]["items"]["B2"] == "oui" else "oui"
    b = jouer(lf, lo, manifeste(), esp)
    assert "B2" not in b["tenue"]["items_gardes"]
    assert b["items"]["B2"]["accord_brut"] == pytest.approx(0.5)
    assert b["items"]["B2"]["garde_dans_le_rang"] is False


def test_item_garde_par_la_seule_marge_est_signale():
    lf, lo, esp = monde(bruit=0.0)
    for i, (cf, co) in enumerate(zip(lf["cartes"], lo["cartes"])):
        cf["items"]["T1"] = "non" if i < 4 else "oui"         # F : 36 oui sur 40
        co["items"]["T1"] = "non" if 4 <= i < 8 else "oui"    # O : 36 oui, jamais les mêmes « non »
    a = jouer(lf, lo, manifeste(), esp)
    t1 = a["items"]["T1"]
    assert t1["accord_brut"] == pytest.approx(0.8) and t1["garde_dans_le_rang"] is True
    assert t1["kappa"] < 0 and t1["garde_sans_accord_au_dela_du_hasard"] is True


def test_kappa():
    assert A.kappa_binaire([1, 0, 1, 0], [1, 0, 1, 0]) == pytest.approx(1.0)
    assert A.kappa_binaire([1, 1, 0, 0], [1, 0, 1, 0]) == pytest.approx(0.0)
    assert A.kappa_binaire([1, 1, 1], [1, 1, 1]) is None      # non défini, jamais 1 par défaut
    assert A.holm([0.01, 0.02, 0.04, 0.5]) == pytest.approx([0.04, 0.06, 0.08, 0.5])


# ---------------------------------------------------------------- régimes d'items (option posée à Lazar)

def test_ajoutable_compte_zero_sauf_sous_l_option():
    assert A.valeur("ajoutable", "tous") == 0 and A.valeur("ajoutable", "idee_d_abord") == 0
    assert A.valeur("ajoutable", "ajoutables_oui") == 1
    assert A.valeur("indecidable", "ajoutables_oui") == 0 and A.valeur("oui", "tous") == 1


def test_les_trois_regimes_sont_rapportes_et_celui_du_manifeste_fait_la_liste():
    lf, lo, esp = monde()
    for l in (lf, lo):
        for c in l["cartes"][:20]:
            for it in A.AJOUTABLES:
                c["items"][it] = "ajoutable"
    sorties = {r: jouer(lf, lo, manifeste(regime_items=r), esp) for r in A.REGIMES}
    for r, a in sorties.items():
        assert set(a["comparaison_des_regimes_d_items"]) == set(A.REGIMES)
        assert a["comparaison_des_regimes_d_items"][r]["nombre_vise"] == [p["porteuse"] for p in a["listes"]["nombre_vise"]]
        assert a["comparaison_des_regimes_d_items"][r]["commun_avec_le_regime_en_vigueur"] == 9
    # la carte brève (« ajoutable » partout) remonte sous l'option, pas sous la lettre
    n = {r: {c["id"]: c["note"] for c in sorties[r]["cartes"]} for r in A.REGIMES}
    assert n["ajoutables_oui"]["s000"] > n["tous"]["s000"]
    assert n["idee_d_abord"]["s000"] == n["tous"]["s000"]


# ---------------------------------------------------------------- fusion : porteur non circulaire

def test_fusion_seulement_si_les_deux_lecteurs_et_porteur_par_carte():
    lf, lo, esp = monde(bruit=0.0)
    for i in (0, 9, 18):                       # même strate (I), mêmes réponses : égalité stricte
        for l in (lf, lo):
            l["cartes"][i]["items"] = {it: "oui" for it in A.ITEMS}
            l["cartes"][i]["groupe_fusion"] = "g1"
    lf["cartes"][27]["groupe_fusion"] = "g1"   # un seul lecteur : pas de fusion
    a = jouer(lf, lo, manifeste(), esp)
    ligne = [l for l in a["lignes"] if l["fusion"]]
    assert len(ligne) == 1 and ligne[0]["cartes"] == ["s000", "s009", "s018"]
    num = {c["id"]: c["numero_de_tirage"] for c in a["cartes"]}
    assert ligne[0]["porteuse"] == min(ligne[0]["cartes"], key=lambda c: num[c])   # plus petit numéro de CARTE
    assert a["comptes"]["lignes"] == 40 - 2
    # le numéro d'une carte ne dépend pas des fusions : mêmes numéros sans fusion
    lf2, lo2, _ = monde(bruit=0.0)
    b = jouer(lf2, lo2, manifeste(), esp)
    assert {c["id"]: c["numero_de_tirage"] for c in b["cartes"]} == num


def test_porteur_au_plancher_d_abord():
    lf, lo, esp = monde(bruit=0.0)
    for i in (0, 9):
        for l in (lf, lo):
            l["cartes"][i]["groupe_fusion"] = "g"
    for l in (lf, lo):
        l["cartes"][0]["items"] = {it: "oui" for it in A.ITEMS}
        l["cartes"][0].update(E=1, Q=1, D=1)                     # la mieux notée, mais sous le plancher
        l["cartes"][9]["items"] = {it: "non" for it in A.ITEMS}
    a = jouer(lf, lo, manifeste(), esp)
    assert [l for l in a["lignes"] if l["fusion"]][0]["porteuse"] == "s009"


def test_carte_dans_deux_voies_comptee_une_fois_avec_la_bonne_variante():
    lf, lo, esp = monde(bruit=0.0)
    lo["cartes"][0].update(voie="N", sous_strate=None)           # F : I ; O : N
    a = jouer(lf, lo, manifeste(), esp)
    l = [x for x in a["lignes"] if x["porteuse"] == "s000"][0]
    assert l["voies_candidates"] == ["I", "N"] and l["voie"] in ("I", "N")
    assert sum(1 for x in a["lignes"] if "s000" in x["cartes"]) == 1
    assert A.items_de_voie("I").count("A1i") == 1 and "A1" not in A.items_de_voie("I")
    assert "A1i" not in A.items_de_voie("P") and len(A.items_de_voie("N")) == 16


# ---------------------------------------------------------------- garde « le rang est un tirage », clé 7 comptée

def test_rang_tire_au_sort_dit_en_tete():
    lf, lo, esp = monde(bruit=0.0)
    a = jouer(lf, lo, manifeste(), esp)                           # cas sain : notes variées
    assert a["tenue"]["places_au_tirage_cle_8"] <= 3
    assert a["conditions_du_rejeu"]["un_tiers_au_plus_des_places_au_tirage"] is True
    for l in (lf, lo):                                            # artefact : tout au plafond
        for c in l["cartes"]:
            c["items"] = {it: "oui" for it in A.ITEMS}
    b = jouer(lf, lo, manifeste(), esp)
    assert b["tenue"]["places_au_tirage_cle_8"] > 3
    assert any("en bonne part un tirage" in x for x in b["en_tete"])
    assert b["conditions_du_rejeu"]["un_tiers_au_plus_des_places_au_tirage"] is False
    assert b["listes"]["a_egalite_perdantes_au_tirage"]


def test_cle_7_comptee_a_part():
    lf, lo, esp = monde(bruit=0.0)
    for l in (lf, lo):
        for c in l["cartes"]:
            c["items"] = {it: "oui" for it in A.ITEMS}
    # même somme, même Q, mêmes axes : seul l'écart entre lecteurs sépare les cartes
    for i in range(0, 40, 2):
        lf["cartes"][i]["items"].update(T1="non", T2="non")       # F : 14, O : 16 -> somme 30, écart 2
    for i in range(1, 40, 2):
        lf["cartes"][i]["items"].update(T1="non")
        lo["cartes"][i]["items"].update(T1="non")                 # F : 15, O : 15 -> somme 30, écart 0
    a = jouer(lf, lo, manifeste(seuil_accord=0.4), esp)           # accord de 0,5 sur T1 et T2 : gardés ici
    assert a["tenue"]["places_a_la_cle_7"] >= 1
    assert a["tenue"]["places_a_la_cle_7"] + a["tenue"]["places_au_tirage_cle_8"] > 3
    assert any("clé 7" in x or "en bonne part un tirage" in x for x in a["en_tete"])


def test_strate_fourre_tout_signalee_chez_chacun():
    lf, lo, esp = monde(bruit=0.0)
    for c in lo["cartes"][:20]:
        c.update(voie="P", sous_strate="c1")
    a = jouer(lf, lo, manifeste(), esp)
    assert any(f["lecteur"] == "O" and f["strate"] == "P c1" for f in a["tenue"]["strates_au_dela_du_tiers"])
    assert not any(f["lecteur"] == "F" for f in a["tenue"]["strates_au_dela_du_tiers"])


# ---------------------------------------------------------------- veto

def _avec_veto(filtre="famille", v="selon_titulaires", plafond="nombre_vise", **k):
    lf, lo, esp = monde(bruit=0.0)
    m = manifeste(filtre_veto=filtre, veto_par_titulaire=v, plafond_veto=plafond, **k)
    return lf, lo, esp, m


def test_veto_filtre_par_famille_puis_suppleantes():
    lf, lo, esp, m = _avec_veto()
    a0 = jouer(lf, lo, m, esp)
    vises = {p["porteuse"] for p in a0["listes"]["nombre_vise"]}
    libres = [c for c in sorted(esp) if c not in vises]
    maison = [c for c in libres if FAMILLES[esp[c]] == "maison"]
    autres = [c for c in libres if FAMILLES[esp[c]] != "maison"]
    lf["veto"] = [veto(maison[0]), veto(autres[0]), veto(maison[1]), veto(autres[1]), veto(autres[2]), veto(autres[3])]
    a = jouer(lf, lo, m, esp)
    entrees = [e["id"] for e in a["listes"]["entrees_par_veto"]]
    assert entrees == sorted([autres[0], autres[1], autres[2]])         # trois valides, hors de la famille
    c = a["veto"]["comptes"]
    assert c["deposees"] == 6 and c["retirees_par_le_filtre"] == 2 and c["suppleantes_non_appelees"] == 1
    assert c["cartes_entrees"] == 3 and c["coupees_par_le_plafond"] == 0
    # le veto ne change aucun rang ni le nombre visé
    assert [p["porteuse"] for p in a["listes"]["nombre_vise"]] == [p["porteuse"] for p in a0["listes"]["nombre_vise"]]
    # les cartes entrées par veto ne sont pas tirées au sort
    assert not set(entrees) & {p["porteuse"] for p in a["listes"]["tirees_au_sort"]}
    # la statistique de famille scellée lit les listes telles que déposées, titulaires seulement
    assert a["listes"]["veto_depose_titulaires"] == sorted([maison[0], autres[0], maison[1]])


def test_veto_filtre_par_lignee_et_sans_filtre():
    lf, lo, esp, m = _avec_veto(filtre="lignee")
    a0 = jouer(lf, lo, m, esp)
    vises = {p["porteuse"] for p in a0["listes"]["nombre_vise"]}
    libres = [c for c in sorted(esp) if c not in vises]
    fable = [c for c in libres if esp[c] == "fable"][0]
    opus = [c for c in libres if esp[c] == "opus"][0]
    lf["veto"] = [veto(fable), veto(opus)]
    a = jouer(lf, lo, m, esp)
    assert [e["id"] for e in a["listes"]["entrees_par_veto"]] == [opus]    # même famille, autre lignée : valide
    b = jouer(lf, lo, manifeste(filtre_veto="aucun"), None)                # sans filtre : aucune espèce requise
    assert sorted(e["id"] for e in b["listes"]["entrees_par_veto"]) == sorted([fable, opus])


def test_veto_filtre_sans_especes_refuse():
    lf, lo, esp, m = _avec_veto()
    lf["veto"] = [veto("s001")]
    with pytest.raises(A.Refus):
        jouer(lf, lo, m, None)                       # table absente
    esp2 = {k: v for k, v in esp.items() if k != "s001"}
    with pytest.raises(A.Refus):
        jouer(lf, lo, m, esp2)                       # espèce absente pour la carte désignée
    esp3 = dict(esp, s001="lignee-inconnue")
    with pytest.raises(A.Refus):
        jouer(lf, lo, m, esp3)


def test_veto_sur_carte_deja_visee_ou_ecartee_remplace_par_la_suppleante():
    lf, lo, esp, m = _avec_veto(filtre="aucun")
    x3 = {"cas": "X3", "phrase": "p"}
    lf["cartes"][39]["exclusion"] = x3
    lo["cartes"][39]["exclusion"] = dict(x3)
    a0 = jouer(lf, lo, m, None)
    visee = a0["listes"]["nombre_vise"][0]["porteuse"]
    libre = [c["id"] for c in a0["cartes"] if c["statut"] == "notee" and not c["dans_le_nombre_vise"]][:2]
    lf["veto"] = [veto(visee), veto("s039"), veto(libre[0]), veto(libre[1])]
    a = jouer(lf, lo, m, None)
    assert sorted(e["id"] for e in a["listes"]["entrees_par_veto"]) == sorted(libre)
    assert a["veto"]["comptes"]["sans_objet"] == 2
    sorts = [j["sort"] for j in a["veto"]["journal"]]
    assert "sans objet : déjà dans le nombre visé" in sorts and "sans objet : carte écartée ou rendue à Lazar" in sorts


def test_veto_liste_trop_longue_ou_identifiant_inconnu_refuse():
    lf, lo, esp, m = _avec_veto(filtre="aucun", suppleantes=1)
    lf["veto"] = [veto(f"s{i:03d}") for i in range(4)]        # 3 + 1 : permis
    jouer(lf, lo, m, None)
    lf["veto"] = [veto(f"s{i:03d}") for i in range(5)]
    with pytest.raises(A.Refus):
        jouer(lf, lo, m, None)
    lf["veto"] = [veto("carte-inconnue")]
    with pytest.raises(A.Refus):
        jouer(lf, lo, m, None)


def _juges(n, libres, par=3):
    return [{"titulaire": f"juge-{j}", "lignee": ["argon", "astra", "carbon", "opus", "fable"][j % 5],
             "veto": [veto(libres[j * par + i]) for i in range(par)]} for j in range(n)]


def test_plafond_du_veto_tient_au_nombre_vise():
    lf, lo, esp, m = _avec_veto(filtre="aucun", v=2)
    a0 = jouer(lf, lo, m, None)
    libres = [c["id"] for c in a0["cartes"] if not c["dans_le_nombre_vise"]]
    juges = _juges(5, libres, par=2)
    lf["veto"] = [veto(libres[20]), veto(libres[21])]
    lo["veto"] = [veto(libres[22]), veto(libres[23])]
    a = jouer(lf, lo, m, None, juges=juges)                     # sept titulaires, deux cartes : 14 demandées
    c = a["veto"]["comptes"]
    assert a["parametres"]["titulaires"] == 7 and c["valides"] == 14
    assert c["cartes_entrees"] == 9 and c["coupees_par_le_plafond"] == 5      # plafond = nombre visé
    # tour de rôle : chaque titulaire a au moins sa première carte
    tit = {t["titulaire"] for e in a["listes"]["entrees_par_veto"] for t in e["titulaires"]}
    assert len(tit) == 7
    # cas sain : sans plafond, les quatorze entrent
    b = jouer(lf, lo, manifeste(filtre_veto="aucun", veto_par_titulaire=2, plafond_veto=None), None, juges=juges)
    assert b["veto"]["comptes"]["cartes_entrees"] == 14 and b["veto"]["comptes"]["coupees_par_le_plafond"] == 0
    # la comparaison deux contre trois est écrite
    assert set(a["comparaison_des_limites_de_veto"]) == {
        "2 cartes, sans plafond", "2 cartes, plafond au nombre visé", "3 cartes, sans plafond", "3 cartes, plafond au nombre visé"}
    assert a["comparaison_des_limites_de_veto"]["2 cartes, sans plafond"]["maximum_theorique"] == 14


def test_selon_titulaires_trois_puis_deux():
    lf, lo, esp, m = _avec_veto(filtre="aucun")
    a = jouer(lf, lo, m, None)
    assert a["parametres"]["veto_par_titulaire_en_vigueur"] == 3
    libres = [c["id"] for c in a["cartes"] if not c["dans_le_nombre_vise"]]
    b = jouer(lf, lo, m, None, juges=_juges(2, libres, par=2))
    assert b["parametres"]["veto_par_titulaire_en_vigueur"] == 2
    with pytest.raises(A.Refus):
        jouer(lf, lo, m, None, juges=[{"titulaire": "F", "lignee": "argon", "veto": []}])


def test_veto_commun_compte_une_carte():
    lf, lo, esp, m = _avec_veto(filtre="aucun")
    a0 = jouer(lf, lo, m, None)
    libre = [c["id"] for c in a0["cartes"] if not c["dans_le_nombre_vise"]][0]
    lf["veto"], lo["veto"] = [veto(libre)], [veto(libre)]
    a = jouer(lf, lo, m, None)
    assert a["veto"]["comptes"]["cartes_entrees"] == 1
    assert a["veto"]["comptes"]["cartes_designees_par_plusieurs_titulaires"] == 1
    assert len(a["listes"]["entrees_par_veto"][0]["titulaires"]) == 2


# ---------------------------------------------------------------- lot

def test_lot_une_ligne_par_voie_hors_nombre_vise():
    lf, lo, esp = monde()
    a = jouer(lf, lo, manifeste(), esp)
    lot = a["listes"]["tirees_au_sort"]
    assert sorted(x["voie"] for x in lot) == ["I", "N", "P"]
    assert not {x["porteuse"] for x in lot} & {p["porteuse"] for p in a["listes"]["nombre_vise"]}
    for v in "INP":
        i = a["tirages"]["lot"][v]
        assert 0 <= i["indice"] < i["taille_du_vivier"]


def test_vivier_vide_ne_tire_rien():
    lf, lo, esp = monde(n=9)
    a = jouer(lf, lo, manifeste(cartes_attendues=9), esp)       # neuf cartes, neuf places : plus rien à tirer
    assert a["listes"]["tirees_au_sort"] == []
    assert all(x["indice"] is None for x in a["tirages"]["lot"].values())


# ---------------------------------------------------------------- témoin sans famille

def test_accord_avec_le_lecteur_par_programme():
    lf, lo, esp = monde(bruit=0.0)
    temoin = {c["id"]: {"id": c["id"], "voie": c["voie"], "D": 2} for c in lf["cartes"]}
    temoin["s000"]["voie"] = None                               # indécidable : sorti du compte, non deviné
    a = jouer(lf, lo, manifeste(), esp, temoin=temoin)
    t = a["accord_avec_le_lecteur_par_programme"]["F"]
    assert t["voie"]["cartes"] == 39 and t["voie"]["accord_brut"] == 1.0 and t["D"]["accord_brut"] == 1.0
    assert jouer(lf, lo, manifeste(), esp)["accord_avec_le_lecteur_par_programme"] is None


# ---------------------------------------------------------------- gardes par espèce : sain / artefact, deux sens

def _gardes(lf, lo, esp, m=None, n_perm=400):
    m = m or manifeste(cartes_attendues=len(lf["cartes"]))
    a = jouer(lf, lo, m, esp)
    vf, vo = A.valider_lecture(lf, "F", m), A.valider_lecture(lo, "O", m)
    return a, A.gardes_coeur(a, vf, vo, esp, FAMILLES, {"F": "fable", "O": "opus"}, H1, n_perm=n_perm)


def test_gardes_cas_sain_rien_ne_se_declenche():
    # un monde sans effet d'espèce ; la graine 8 est un monde nul parmi d'autres (les graines 7 et 11
    # déclenchent par hasard : c'est le taux de faux déclenchement, mesuré par l'essai suivant)
    lf, lo, esp = monde(n=90, graine=8)
    a, g = _gardes(lf, lo, esp)
    assert g["retour_a_lazar_avant_adoption"] is False and g["items_nommes"] == [] and g["ecarts_forts"] == []
    assert g["en_tete"][0] == A.PRINCIPE


def test_gardes_taux_de_faux_declenchement_sous_le_nul():
    # trois familles de tests à 0,05 après Holm : au plus 0,15 environ ; borne d'essai large (8 sur 30)
    n = 0
    for graine in range(100, 130):
        lf, lo, esp = monde(n=90, graine=graine)
        n += _gardes(lf, lo, esp, n_perm=400)[1]["retour_a_lazar_avant_adoption"]
    assert n <= 8


@pytest.mark.parametrize("sens", ["plus", "moins"])
def test_garde_1_item_qui_lit_une_maniere_d_ecrire(sens):
    lf, lo, esp = monde(n=90, graine=7)
    for l in (lf, lo):
        for c in l["cartes"]:
            astra = esp[c["id"]] == "astra"
            c["items"]["B3"] = ("oui" if astra else "non") if sens == "plus" else ("non" if astra else "oui")
    a, g = _gardes(lf, lo, esp)
    assert {"item": "B3", "niveau": "lignee", "dans_le_rang": True} in g["items_nommes"]
    assert g["retour_a_lazar_avant_adoption"] is True


def test_garde_1_niveau_famille():
    lf, lo, esp = monde(n=90, graine=7)
    for l in (lf, lo):
        for c in l["cartes"]:
            c["items"]["S3"] = "oui" if FAMILLES[esp[c["id"]]] == "maison" else "non"
    a, g = _gardes(lf, lo, esp)
    assert any(x["item"] == "S3" and x["niveau"] == "famille" for x in g["items_nommes"])


@pytest.mark.parametrize("haut", [True, False])
def test_garde_2_ecart_fort_dans_les_deux_sens(haut):
    lf, lo, esp = monde(n=90, graine=7)
    for l in (lf, lo):
        for c in l["cartes"]:
            carbon = esp[c["id"]] == "carbon"
            if carbon:
                c["items"] = {it: ("oui" if haut else "non") for it in A.ITEMS}
    a, g = _gardes(lf, lo, esp)
    forts = [x for x in g["ecarts_forts"] if x["groupe"] == "lignée carbon" and x["objet"] == "note_fine"]
    assert forts and forts[0]["sens"] == ("plus" if haut else "moins")
    assert g["retour_a_lazar_avant_adoption"] is True


def test_gardes_petits_effectifs_non_concluants_et_espece_absente_refusee():
    lf, lo, esp = monde(n=90, graine=7)
    gen = np.random.Generator(np.random.PCG64(np.random.SeedSequence(3)))
    r = A.garde_liste([True, True] + [False] * 8, [True] * 5 + [False] * 5, ["I"] * 10, gen, 50)
    assert r["lecture"] == "non concluant"
    r = A.garde_item([0, 1, 0, 1, 1, 0], ["a", "a", "b", "b", "b", "c"], ["I"] * 6, gen, 50)
    assert r["lecture"] == "non concluant" and r["groupes_exclus"] == ["a", "c"]
    r = A.garde_item([1] * 8, ["a"] * 4 + ["b"] * 4, ["I"] * 8, gen, 50)
    assert r["lecture"] == "non concluant" and "variance" in r["motif"]
    esp2 = {k: v for k, v in esp.items() if k != "s010"}
    with pytest.raises(A.Refus):
        _gardes(lf, lo, esp2, manifeste(cartes_attendues=90, filtre_veto="aucun"))


def test_permutation_garde_les_effectifs_par_voie():
    gen = np.random.Generator(np.random.PCG64(np.random.SeedSequence(5)))
    e = ["a"] * 3 + ["b"] * 7 + ["a"] * 6 + ["b"] * 4
    s = ["I"] * 10 + ["P"] * 10
    for _ in range(200):
        p = list(A._permuter_dans_les_strates(e, s, gen))
        assert p[:10].count("a") == 3 and p[10:].count("a") == 6


def test_veto_part_de_sa_propre_famille_telle_que_deposee():
    lf, lo, esp = monde(n=90, graine=7)
    maison = [c for c in sorted(esp) if FAMILLES[esp[c]] == "maison"][:5]
    lf["veto"] = [veto(c) for c in maison]
    a, g = _gardes(lf, lo, esp)
    d = g["veto_par_titulaire_tel_que_depose"]["F"]
    assert d["deposees"] == 5 and d["de_sa_famille"] == 5      # mesuré avant le retrait par programme
    assert a["veto"]["comptes"]["retirees_par_le_filtre"] == 5 and a["veto"]["comptes"]["cartes_entrees"] == 0


def test_note_selon_la_lignee_reconnue_si_decidee():
    lf, lo, esp = monde(n=90, graine=7)
    for l in (lf, lo):
        for c in l["cartes"]:
            c["lignee_reconnue"] = esp[c["id"]] if c["id"] < "s045" else "aucune"
    m = manifeste(cartes_attendues=90, lignee_reconnue_declaree=True)
    a, g = _gardes(lf, lo, esp, m)
    r = g["note_selon_la_lignee_reconnue"]["F"]
    assert r["croit_reconnaitre_sa_famille"][0] + r["ne_croit_pas"][0] == 90
    a2, g2 = _gardes(*monde(n=90, graine=7))
    assert g2["note_selon_la_lignee_reconnue"] is None


# ---------------------------------------------------------------- tiers de l'ordre de passage

def test_tiers_cas_sain_et_voie_repoussee_en_fin():
    ordre = [f"p{i:02d}" for i in range(30)]
    voie = {c: "INP"[i % 3] for i, c in enumerate(ordre)}
    sous = {c: None for c in ordre}
    t = A.tiers_coeur(ordre, voie, sous, None, [1, 2], n_perm=500)
    assert t["retour_a_lazar"] is False
    assert t["parts"]["voie"]["I"]["par_tiers"] == [4, 3, 3]
    voie2 = {c: ("I" if i >= 20 else "NP"[i % 2]) for i, c in enumerate(ordre)}   # instruments en dernier
    t2 = A.tiers_coeur(ordre, voie2, sous, None, [1, 2], n_perm=500)
    assert t2["parts"]["voie"]["I"]["par_tiers"] == [0, 0, 10]
    assert {"axe": "voie", "modalite": "I", "sens": "passe plus tard"} in t2["ecarts_forts"]
    assert t2["retour_a_lazar"] is True
    esp = {c: ("astra" if i < 8 else "autre") for i, c in enumerate(ordre)}      # autre sens, par espèce
    t3 = A.tiers_coeur(ordre, voie, sous, esp, [1, 2], n_perm=500)
    assert {"axe": "espece", "modalite": "astra", "sens": "passe plus tôt"} in t3["ecarts_forts"]


def test_tiers_refus():
    with pytest.raises(A.Refus):
        A.tiers_coeur(["a", "a", "b"], {"a": "I", "b": "N"}, {"a": None, "b": None}, None, [1])
    with pytest.raises(A.Refus):
        A.tiers_coeur(["a", "b", "c"], {"a": "I", "b": "N"}, {"a": None, "b": None, "c": None}, None, [1])
    with pytest.raises(A.Refus):
        A.tiers_coeur([], {}, {}, None, [1])


# ---------------------------------------------------------------- ligne de commande : empreintes, écrasement

def _ecrire(tmp, nom, obj):
    p = os.path.join(str(tmp), nom)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)
    return p, A.sha_fichier(p)


def _dossier(tmp_path):
    lf, lo, esp = monde()
    crit = os.path.join(str(tmp_path), "criteres.md")
    with open(crit, "w", encoding="utf-8") as f:
        f.write("critères synthétiques\n")
    m = manifeste(criteres_sha256=A.sha_fichier(crit))
    return {"crit": crit, "m": _ecrire(tmp_path, "m.json", m), "f": _ecrire(tmp_path, "f.json", lf),
            "o": _ecrire(tmp_path, "o.json", lo), "e": _ecrire(tmp_path, "e.json", esp)}


def _args(d, sortie, **k):
    a = ["assembler", "--manifeste", *d["m"], "--criteres", d["crit"], "--lecture-f", *d["f"],
         "--lecture-o", *d["o"], "--especes", *d["e"], "--sortie", sortie]
    return a


def test_commande_cas_sain_puis_gardes_puis_refus_d_ecraser(tmp_path, capsys):
    d = _dossier(tmp_path)
    s = os.path.join(str(tmp_path), "a.json")
    assert A.main(_args(d, s)) == 0
    assert os.path.exists(s) and os.path.exists(s + ".sha256")
    with open(s + ".sha256") as f:
        assert f.read().split()[0] == A.sha_fichier(s)
    assert A.PRINCIPE in capsys.readouterr().out
    assert A.main(_args(d, s)) == 2                              # on n'écrase jamais
    g = os.path.join(str(tmp_path), "g.json")
    old = A.N_PERMUTATIONS
    try:
        A.gardes_coeur.__defaults__ = (200,)
        assert A.main(["gardes", "--manifeste", *d["m"], "--criteres", d["crit"], "--lecture-f", *d["f"],
                       "--lecture-o", *d["o"], "--assemblage", s, A.sha_fichier(s), "--especes", *d["e"],
                       "--sortie", g]) == 0
    finally:
        A.gardes_coeur.__defaults__ = (old,)
    assert os.path.exists(g + ".sha256")


@pytest.mark.parametrize("quoi", ["m", "f", "o", "e"])
def test_commande_empreinte_fausse_refusee_sans_rien_ecrire(tmp_path, quoi, capsys):
    d = _dossier(tmp_path)
    d[quoi] = (d[quoi][0], "0" * 64)
    s = os.path.join(str(tmp_path), "a.json")
    assert A.main(_args(d, s)) == 2
    assert not os.path.exists(s) and not os.path.exists(s + ".sha256")
    assert "REFUS" in capsys.readouterr().err


def test_commande_criteres_differents_du_manifeste_refuses(tmp_path):
    d = _dossier(tmp_path)
    with open(d["crit"], "a", encoding="utf-8") as f:
        f.write("retouche après scellement\n")
    s = os.path.join(str(tmp_path), "a.json")
    assert A.main(_args(d, s)) == 2 and not os.path.exists(s)


def test_commande_empreinte_illisible_et_fichier_absent(tmp_path):
    d = _dossier(tmp_path)
    s = os.path.join(str(tmp_path), "a.json")
    d2 = dict(d, m=(d["m"][0], "xyz"))
    assert A.main(_args(d2, s)) == 2
    d3 = dict(d, f=(os.path.join(str(tmp_path), "absent.json"), d["f"][1]))
    assert A.main(_args(d3, s)) == 2 and not os.path.exists(s)


def test_commande_tiers(tmp_path):
    ordre = [f"p{i:02d}" for i in range(12)]
    o = _ecrire(tmp_path, "ordre.json", {"ordre": ordre, "voie": {c: "INP"[i % 3] for i, c in enumerate(ordre)},
                                         "sous_strate": {c: None for c in ordre}})
    s = os.path.join(str(tmp_path), "t.json")
    assert A.main(["tiers", "--ordre", *o, "--sortie", s]) == 0
    assert A.main(["tiers", "--ordre", *o, "--sortie", s]) == 2
