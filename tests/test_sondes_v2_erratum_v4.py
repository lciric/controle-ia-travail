"""Essais de l'erratum de code demandé par les décisions du concepteur des sondes v2 (cb270590…, § 7, lues avec
l'erratum 1, 019cff39…) : lecture v2, statistiques v2 (rejeu croisé), monde planté v4 et son programme. Données
fabriquées seulement."""
import json
import shutil

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sondes_v2 import lecture_v1, lecture_v2 as lc, monde_plante_v4 as mp
from controle_ia.sondes_v2 import programme_monde_plante_v4 as prog
from controle_ia.sondes_v2 import statistiques_v1, statistiques_v2 as st

SEUILS = {"alpha": 0.05, "u_fort": 0.9}
CORR = {c: c for c in st.CHAMPS_TABLE}


def _rngs():
    return {n: np.random.default_rng(i) for i, n in enumerate(st.GRAINES_NOMMEES)}


def _table(n_taches=10, inter=1.0, ecart_chemin=0.0, avec_relu=True, graine=0, ecart_par_tache=None,
           controle_taches=None):
    """Table fabriquée : scores = base de texte + effets ; origine = (adaptateur, saboteur) et (nu, honnête) ;
    `ecart_par_tache` : décalage de chemin propre à chaque tâche ; `controle_taches` : tâches relues (défaut : toutes)."""
    rng = np.random.default_rng(graine)
    lignes = []
    for t in range(n_taches):
        e = ecart_chemin if ecart_par_tache is None else ecart_par_tache[t]
        relu_t = avec_relu and (controle_taches is None or t in controle_taches)
        for so in ("saboteur", "honnete"):
            for a in range(3):
                base = rng.standard_normal()
                cle = f"t{t}-{so}-{a}"
                for po in ("adaptateur", "nu"):
                    s = base + 0.05 * rng.standard_normal() + (inter if (po, so) == ("adaptateur", "saboteur") else 0)
                    commun = {"dose": 1, "pli": t % 2, "source": so, "poids": po, "tache": f"t{t}", "cle": cle,
                              "longueur": 10 + a, "pas": a, "valeur_declaree": None, "tache_tenue": True}
                    if (po, so) in st.CASES_ORIGINE:
                        lignes.append({**commun, "chemin": "origine", "score": s + e})
                        if relu_t:
                            lignes.append({**commun, "chemin": "relu", "score": s})
                    else:
                        lignes.append({**commun, "chemin": "relu", "score": s})
    return lignes


def _charger(l):
    t, motif = st.charger_table_scores(l, CORR)
    assert motif is None
    return t


# ------------------------------------------------------------------------------------------------- lecture v2

def test_lecture_signee_au_plus_le_seuil():
    t = {"p_au_dessus": 0.05, "p_au_dessous": 0.97}
    assert lecture_v1.lecture_signee(t, 0.05) == "non établie"  # v1 gardée telle quelle
    assert lc.lecture_signee(t, 0.05) == "établie"
    assert lc.lecture_signee({"p_au_dessus": 0.97, "p_au_dessous": 0.05}, 0.05) == "contraire"
    assert lc.lecture_signee({"p_au_dessus": 0.06, "p_au_dessous": 0.95}, 0.05) == "non établie"


def test_contraste_testabilite_et_plafond():
    assert lc.contraste_testable(6, 39, 0.05) and not lc.contraste_testable(5, 39, 0.05)  # 2^-4 = 0,0625
    assert not lc.contraste_testable(8, 18, 0.05)  # 1/19 > 0,05
    assert not lc.contraste_testable(8, 39, 0.01) and lc.contraste_testable(8, 199, 0.01)
    assert lc.lecture_contraste(0.01, 5, 199, 0.05) == "non testable à cet effectif"
    assert lc.lecture_contraste(0.05, 8, 39, 0.05) == "établie"
    assert lc.lecture_contraste(0.051, 8, 39, 0.05) == "non établie à cette puissance"
    # table des décisions v2, § 1
    for P, R, a, bas, haut in ((6, 39, 0.05, 0.66, 0.88), (8, 39, 0.05, 0.96, 0.99), (6, 199, 0.05, 0.90, 1.00),
                               (8, 199, 0.01, 0.54, 0.82), (10, 199, 0.01, 0.94, 0.98)):
        p = lc.plafond_puissance_contraste(P, R, a)
        assert p["plafond_image_comptee"] == pytest.approx(bas, abs=0.006)
        assert p["plafond_image_non_comptee"] == pytest.approx(haut, abs=0.006)


def test_contraste_apparie_descriptif():
    from controle_ia.sondes_v2 import monde_plante_v3
    m = monde_plante_v3.generer(monde_plante_v3.Parametres(d=16, n_paires=4, n_taches=4, actions_par_tache=2,
                                                           tau=3.0), np.random.default_rng(0))
    jeu = monde_plante_v3.jeu_principal(m)
    scores = {i: float(jeu.y[k]) + 0.1 * k for k, i in enumerate(jeu.ids)}
    r = lc.contraste_apparie(scores, jeu, sorted(set(jeu.unites)), np.random.default_rng(0))
    assert r["nature"] == lc.MENTION_DESCRIPTIF and "test" not in r and "libelle" not in json.dumps(r)
    assert "p_bilaterale" in r["description"]


# -------------------------------------------------------------------------------------------- rejeu croisé v2

def test_rejeu_v2_egal_a_v1_sur_un_ecart_constant():
    """Écart de chemin constant et contrôle sur toutes les tâches : par tâche (v2) et constante (v1) coïncident."""
    for ec in (0.0, 0.5):
        t = _charger(_table(inter=0.0, ecart_chemin=ec))
        r1 = statistiques_v1.rejeu_croise(t, _rngs(), SEUILS, n_tirages=200)["doses"]["1"]
        r2 = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=200)["doses"]["1"]
        assert r2["controle_chemin"]["regle"] == "par tâche"
        assert r2["corrigee"]["grandeur"] == pytest.approx(r1["corrigee"]["grandeur"], abs=1e-12)
        assert r2["libelle"] == r1["libelle"] and r2["brute"]["libelle"] == r1["brute"]["libelle"]


def test_rejeu_v2_ecart_par_tache():
    """Écart propre à chaque tâche : la correction par tâche le retire exactement ; la constante non."""
    ecarts = [0.0, 2.0] * 5
    t = _charger(_table(inter=0.0, ecart_par_tache=ecarts))
    r2 = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=200)["doses"]["1"]
    r1 = statistiques_v1.rejeu_croise(t, _rngs(), SEUILS, n_tirages=200)["doses"]["1"]
    e = r2["controle_chemin"]["ecarts"]
    assert e["t1"] > e["t0"] + 1.0
    assert abs(r2["corrigee"]["grandeur"]) < 0.1
    v1_par_tache = np.array(r1["corrigee"]["test"]["valeurs"])
    v2_par_tache = np.array(r2["corrigee"]["test"]["valeurs"])
    assert v1_par_tache.std() > 5 * v2_par_tache.std()  # la constante laisse la variation entre tâches


def test_rejeu_v2_gardes_e2():
    l = [x for x in _table() if (x["poids"], x["source"]) != ("nu", "saboteur")]
    r = st.rejeu_croise(_charger(l), _rngs(), SEUILS, n_tirages=50)["doses"]["1"]
    assert r["regime"] == "non calculable" and r["motif"] == "case manquante : (nu, saboteur)"
    assert r["libelle"] == "non calculable"
    l = [x for x in _table() if not ((x["poids"], x["source"]) == ("nu", "honnete") and x["chemin"] == "origine")]
    r = st.rejeu_croise(_charger(l), _rngs(), SEUILS, n_tirages=50)["doses"]["1"]
    assert r["motif"] == st.MOTIF_CHEMIN_DIFFERENT and r["libelle"] == "non calculable"
    l = _table()
    next(x for x in l if (x["poids"], x["source"]) == ("adaptateur", "honnete"))["chemin"] = "origine"
    with pytest.raises(GardeArret, match="impossible selon le texte scellé"):
        st.rejeu_croise(_charger(l), _rngs(), SEUILS, n_tirages=50)
    r = st.rejeu_croise(_charger(_table()), _rngs(), SEUILS, n_tirages=50)["doses"]["1"]  # cas sain
    assert r["motif"] == "aucun" and r["chemins_retenus"] == {"adaptateur/saboteur": "origine",
                                                               "adaptateur/honnete": "relu", "nu/saboteur": "relu",
                                                               "nu/honnete": "origine"}


def test_rejeu_v2_cas_mixte_arret_nomme_et_regles():
    t = _charger(_table(inter=0.0, ecart_chemin=0.5, controle_taches={0, 1, 2, 3, 4, 5}))
    with pytest.raises(GardeArret, match="règle du cas mixte non fixée"):
        st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=50)
    with pytest.raises(GardeArret, match="hors de"):
        st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=50, regle_cas_mixte="au hasard")
    a = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=50, regle_cas_mixte="taches_controlees_seules")["doses"]["1"]
    assert a["controle_chemin"]["taches"] == 6 and a["corrigee"]["taches"] == 6
    b = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=50, regle_cas_mixte="constante_par_dose")["doses"]["1"]
    assert 0.2 < b["controle_chemin"]["ecart"] < 1.0
    assert b["corrigee"]["taches"] == 10
    c = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=50, regle_cas_mixte="controle_absent")["doses"]["1"]
    assert c["controle_chemin"] == st.CONTROLE_ABSENT and "corrigee" not in c


def test_libeller_rejeu_memes_valeurs_p():
    t = _charger(_table(inter=0.35, graine=3))
    r = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=50)
    avant = json.dumps(r, sort_keys=True, default=str)
    p = r["doses"]["1"]["brute"]["p_holm"]
    strict = st.libeller_rejeu(r, {"alpha": p / 2})
    large = st.libeller_rejeu(strict, {"alpha": 0.05})
    assert json.dumps(r, sort_keys=True, default=str) == avant  # entrée non modifiée
    assert strict["doses"]["1"]["brute"]["p_holm"] == p
    assert strict["doses"]["1"]["brute"]["libelle"] in ("non établie à cette puissance", "non testable à cet effectif")
    assert large["doses"]["1"]["libelle"] == r["doses"]["1"]["libelle"]
    assert large["doses"]["1"]["brute"]["libelle"] == r["doses"]["1"]["brute"]["libelle"]


def test_residuelle_variables_absentes_ou_constantes():
    l = _table(inter=1.0)
    for x in l:
        x["longueur"] = float("nan")
    r = st.rejeu_croise(_charger(l), _rngs(), SEUILS, n_tirages=50)["doses"]["1"]
    assert r["triviaux"]["difference_longueur"] == "variable absente"
    assert all(v == ["pas"] for v in r["residuelle"]["variables_par_pli"].values())
    assert all(s.get("longueur") == "variable absente" for s in r["residuelle"]["variables_sorties_par_pli"].values())
    assert r["libelle"] == "établie"
    l = _table(inter=1.0)
    for x in l:
        x["pas"] = 0
    r = st.rejeu_croise(_charger(l), _rngs(), SEUILS, n_tirages=50)["doses"]["1"]
    assert all(v == ["longueur"] for v in r["residuelle"]["variables_par_pli"].values())
    assert all(s.get("pas") == "constante sur les textes honnêtes"
               for s in r["residuelle"]["variables_sorties_par_pli"].values())


def test_m2_constance_sur_honnetes_seuls_et_m3_non_finies():
    # m2 : variable constante chez les honnêtes, mais variable chez les saboteurs -> doit être sortie
    l = _table(inter=1.0)
    for x in l:
        if x["source"] == "honnete":
            x["pas"] = 0
        else:
            x["pas"] = 1 if x["cle"].endswith("-0") else 2
    t = _charger(l)
    r = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=50)["doses"]["1"]
    assert all(v == ["longueur"] for v in r["residuelle"]["variables_par_pli"].values())
    assert all(s.get("pas") == "constante sur les textes honnêtes"
               for s in r["residuelle"]["variables_sorties_par_pli"].values())
    # m3 : valeur infinie ou texte non numérique dans charger_table_scores -> GardeArret (R5)
    for champ, mauvais in (("longueur", float("inf")), ("pas", "abc"), ("score", "pas_nombre"), ("score", float("nan"))):
        l_bad = _table(inter=1.0)
        l_bad[0][champ] = mauvais
        with pytest.raises(GardeArret):
            st.charger_table_scores(l_bad, CORR)
    # m3 : valeur infinie dans rejeu_croise direct sur longueur, et valeur NaN partielle sur colonne présente
    l_inf = _table(inter=1.0)
    l_inf[0]["longueur"] = float("inf")
    with pytest.raises(GardeArret, match="infinie"):
        st.rejeu_croise(l_inf, _rngs(), SEUILS, n_tirages=50)
    l_part = _table(inter=1.0)
    l_part[0]["longueur"] = float("nan")
    with pytest.raises(GardeArret, match="partielle"):
        st.rejeu_croise(l_part, _rngs(), SEUILS, n_tirages=50)


# ------------------------------------------------------------------------------------------- monde planté v4

def test_verites_v4(tmp_path):
    v, sha = mp.charger_verites()
    assert sha.startswith("b310e1af") and v["format"] == "verites-mondes-plantes-v4" and len(v["mondes"]) == 12
    crit = {(m, c["lecture"], c["nature"]): c for m, d in v["mondes"].items() for c in d["criteres"]}
    assert crit[("decalage_de_chemin", "interaction_brute_holm", "puissance")]["seuil"] == 0.8
    assert crit[("interaction", "interaction", "garde")]["admises"] == ["contraire"]
    with pytest.raises(GardeArret, match="format"):
        mp.charger_verites(mp.CHEMIN_VERITES.with_name("verites_mondes_plantes_v3.json"))
    copie = tmp_path / mp.CHEMIN_VERITES.name
    shutil.copy(mp.CHEMIN_VERITES, copie)
    shutil.copy(str(mp.CHEMIN_VERITES) + ".sha256", str(copie) + ".sha256")
    copie.write_text(copie.read_text().replace('"seuil": 0.8', '"seuil": 0.5'))
    with pytest.raises(GardeArret, match="empreinte"):
        mp.charger_verites(copie)


def _lire(nom, n_paires=8, doses=1, **kw):
    v, _ = mp.charger_verites()
    p = mp.parametres(v, nom, n_paires, 1, 8, 3, 32, "complet")
    _, rngs = st.generateurs_nommes(7, f"essai/{nom}/")
    return mp.lire_monde(p, rngs, kw.pop("journal"), nom, SEUILS, 39, 200, k_externes=3, n_nul_identite=9,
                         doses_rejeu=doses, **kw)


def test_lire_monde_v4(tmp_path, monkeypatch):
    j = tmp_path / "j.jsonl"
    r = _lire("decalage_de_chemin", journal=j, doses=4)
    for c in ("interaction_holm", "interaction_brute_holm", "contraste", "nul_principal", "texte"):
        assert c in r and len(r[c]) == 1
    g = r[mp.GRANDEURS]
    assert set(g) >= {"interaction_brute", "interaction_corrigee", "aire_principale", "U", "rho",
                      "contraste_rejeux_demandes", "contraste_rejeux_effectifs"}
    assert g["interaction_brute"][0] > g["interaction_corrigee"][0]
    assert g["contraste_rejeux_demandes"] == [39] and g["contraste_rejeux_effectifs"] == [39]
    r5 = _lire("trace_forte", n_paires=5, journal=j)
    assert r5["contraste"] == ["non testable à cet effectif"] and r5["nul_principal"] == ["non testable à cet effectif"]
    with pytest.raises(GardeArret, match="entier"):
        _lire("trace_forte", journal=j, doses=0)
    # m1 : avec 19 rejeux demandés mais 18 effectifs (1 réplique dégénérée) à alpha = 0.05, testabilité lue sur R_eff
    vrai_nul = mp.lc.nul_reetiquetage
    monkeypatch.setattr(
        mp.lc,
        "nul_reetiquetage",
        lambda *a, **k: {**vrai_nul(*a, **k), "repliques": 18, "degeneres": 1},
    )
    r_eff = _lire("trace_forte", n_paires=8, journal=j)
    assert r_eff["contraste"] == ["non testable à cet effectif"]
    assert r_eff[mp.GRANDEURS]["contraste_rejeux_demandes"] == [39]
    assert r_eff[mp.GRANDEURS]["contraste_rejeux_effectifs"] == [18]


def test_programme_v4_plages_egales_a_un_processus(tmp_path):
    kw = dict(mode="complet", cas=[(8, 8, 3)], repliques=2, n_nul=19, n_tirages=100, seuils=SEUILS, d=32,
              entropie=20261123, mondes=["interaction", "decalage_de_chemin"], k_externes=3, n_nul_identite=9,
              autoriser_depot_sale=True, doses_rejeu=2)
    un = json.loads(prog.executer(tmp_path / "un", **kw).read_text())
    a = prog.executer(tmp_path / "a", **kw, plage=(0, 1))
    b = prog.executer(tmp_path / "b", **kw, plage=(1, 2))
    assert "synthese" not in json.loads(a.read_text())
    fus = prog.fusionner([b, a])
    assert prog._canon(fus) == prog._canon(un["synthese"])
    # M2 : écriture et scellement de la synthèse fusionnée avec les empreintes des rapports
    syn_chemin = prog.ecrire_synthese_fusionnee([a, b], tmp_path / "synthese-fusionnee.json")
    assert (tmp_path / "synthese-fusionnee.json.sha256").is_file()
    syn_corps = json.loads(syn_chemin.read_text())
    assert len(syn_corps["rapports"]) == 2 and prog._canon(syn_corps["synthese"]) == prog._canon(un["synthese"])
    with pytest.raises(GardeArret, match="R12"):
        prog.ecrire_synthese_fusionnee([a, b], syn_chemin)
    with pytest.raises(GardeArret, match="couvrent"):
        prog.fusionner([a])
    with pytest.raises(GardeArret, match="contiguës"):
        prog.fusionner([a, a, b])
    c = prog.executer(tmp_path / "c", **{**kw, "doses_rejeu": 3}, plage=(1, 2))
    with pytest.raises(GardeArret, match="exécutions différentes"):
        prog.fusionner([a, c])
    # m9 : entropies différentes et vérités différentes dans fusionner
    d_ent = prog.executer(tmp_path / "d_ent", **{**kw, "entropie": 20261124}, plage=(1, 2))
    with pytest.raises(GardeArret, match="entropies racines différentes"):
        prog.fusionner([a, d_ent])
    b_ver = tmp_path / "b_ver.json"
    ver_mod = json.loads(b.read_text())
    ver_mod["verites_sha256"] = "0" * 64
    b_ver.write_bytes(prog._canon(ver_mod))
    prog.sceller(b_ver)
    with pytest.raises(GardeArret, match="verites_sha256"):
        prog.fusionner([a, b_ver])
    # M2 : commits, propreté ou réserves différents refusés à la fusion
    b_com = tmp_path / "b_com.json"
    com_mod = json.loads(b.read_text())
    com_mod["manifeste"]["commit"] = "0" * 40
    b_com.write_bytes(prog._canon(com_mod))
    prog.sceller(b_com)
    with pytest.raises(GardeArret, match="commits différents"):
        prog.fusionner([a, b_com])
    b_sale = tmp_path / "b_sale.json"
    sale_mod = json.loads(b.read_text())
    sale_mod["manifeste"]["depot_propre"] = not sale_mod["manifeste"]["depot_propre"]
    b_sale.write_bytes(prog._canon(sale_mod))
    prog.sceller(b_sale)
    with pytest.raises(GardeArret, match="propreté"):
        prog.fusionner([a, b_sale])
    with pytest.raises(GardeArret, match="plage"):
        prog.executer(tmp_path / "d", **kw, plage=(1, 3))
    s = un["synthese"]["cases"]["8,8,3"]
    assert s["decalage_de_chemin"]["grandeurs_realisees"]["interaction_brute"]["n"] == 2
    assert s["interaction"]["contraste"]["rejeux"] == 19 and s["interaction"]["contraste"]["testable"] is True
    assert s["interaction"]["contraste"]["rejeux_demandes"] == 19
    assert s["interaction"]["contraste"]["rejeux_effectifs_min"] == 19


def test_synthese_etalon_par_famille_et_manquantes_m7():
    v, _ = mp.charger_verites()
    lect = {
        "0": {"transport": ["fort", "faible"], "grandeurs": {"U": [0.95, 0.72], "rho": [2.0, 0.8], "U_controle": [0.9, 0.6], "rho_controle": [1.5, float("nan")]}},
        "1": {"transport": ["fort", "faible"], "grandeurs": {"U": [0.91], "rho": [1.8], "U_controle": [0.85], "rho_controle": [float("nan")]}},
    }
    s = prog.synthese(v, "etalon", {"8,2,8,1": {"trace_forte": lect}}, 2, 19, SEUILS)["cases"]["8,2,8,1"]["trace_forte"]
    g = s["grandeurs_realisees"]
    assert set(g["U"]) == {"0", "1"}
    assert g["U"]["0"]["n"] == 2 and g["U"]["0"]["non_finies"] == 0
    assert g["U"]["1"]["n"] == 2 and g["U"]["1"]["non_finies"] == 1
    assert g["rho_controle"]["0"]["n"] == 2 and g["rho_controle"]["0"]["non_finies"] == 1
    assert g["rho_controle"]["1"]["n"] == 2 and g["rho_controle"]["1"]["non_finies"] == 2
    # m7 en mode complet : une réplique sans grandeurs est comptée dans non_finies
    lect_c = {
        "0": {"interaction": ["établie"], "interaction_holm": ["établie"], "grandeurs": {"interaction_brute": [1.2]}},
        "1": {"interaction": ["non calculable"], "interaction_holm": ["non calculable"]},
    }
    sc = prog.synthese(v, "complet", {"8,8,3": {"interaction": lect_c}}, 2, 19, SEUILS)["cases"]["8,8,3"]["interaction"]
    assert sc["grandeurs_realisees"]["interaction_brute"]["n"] == 2
    assert sc["grandeurs_realisees"]["interaction_brute"]["non_finies"] == 1


def test_synthese_gardes_non_passees():
    v, _ = mp.charger_verites()
    lect = {str(r): {"interaction": ["contraire"], "interaction_holm": ["contraire"]} for r in range(30)}
    s = prog.synthese(v, "complet", {"8,8,3": {"interaction": lect}}, 30, 39, SEUILS)["cases"]["8,8,3"]["interaction"]
    assert s["gardes_non_passees"] == [{"lecture": "interaction", "admises": ["contraire"],
                                        "consequence": prog.CONSEQUENCE_GARDE_REJEU}]
    lect = {str(r): {"interaction": ["établie"], "interaction_holm": ["établie"]} for r in range(60)}
    s = prog.synthese(v, "complet", {"8,8,3": {"interaction": lect}}, 60, 39, SEUILS)["cases"]["8,8,3"]["interaction"]
    assert s["gardes_non_passees"] == []
    with pytest.raises(GardeArret, match="répliques"):
        prog.synthese(v, "complet", {"8,8,3": {"interaction": {"0": lect["0"]}}}, 2, 39, SEUILS)


def test_ligne_de_commande_v4_et_gardes_m8_m11(tmp_path, capsys):
    from test_sondes_v2_formats import _note, _note_md
    assert prog.main(["--sortie", str(tmp_path / "run_ok"), "--cas", "7,1,8,1", "--repliques", "2", "--repliques-de", "0",
                      "--repliques-a", "1", "--nul", "5", "--tirages", "20", "--d", "16", "--entropie", "3",
                      "--mondes", "trace_faible", "--nul-identite", "5", "--autoriser-depot-sale"]) == 0
    assert capsys.readouterr().out.strip().endswith("-r0-1.json")
    with pytest.raises(GardeArret, match="vont ensemble"):
        prog.main(["--sortie", str(tmp_path), "--cas", "7,1,8,1", "--repliques-de", "0"])
    with pytest.raises(GardeArret, match="--mode"):
        prog.main(["--sortie", str(tmp_path), "--cas", "7,1,8,1", "--mode", "etalon"])
    # m8 : --doses-rejeu refusé en mode étalon
    with pytest.raises(GardeArret, match="refusé en mode étalon"):
        prog.main(["--sortie", str(tmp_path), "--cas", "7,1,8,1", "--doses-rejeu", "2"])
    note_ok = _note_md(tmp_path, _note(), "note_ok.md")
    with pytest.raises(GardeArret, match="refusé en mode étalon"):
        prog.main(["--sortie", str(tmp_path), "--note-effectifs", str(note_ok), "--mode", "etalon", "--doses-rejeu", "2"])
    # m8 : extension de grille exige --go-extension
    n_ext = _note()
    n_ext["activations"]["cles_communes"]["distinctes_des_cles_propres"] = False
    n_ext["cases_de_l_epreuve_plantee"]["extension_taches_actions"] = True
    note_ext = _note_md(tmp_path, n_ext, "note_ext.md")
    gr = mp.charger_verites()[0]["grille_etalon"]
    with pytest.raises(GardeArret, match="--go-extension"):
        prog.cas_depuis_note(n_ext, "etalon", gr)
    cas_ext, _ = prog.cas_depuis_note(n_ext, "etalon", gr, go_extension="GO-2026-11-23-99")
    assert len(cas_ext) == 416
    with pytest.raises(GardeArret, match="--go-extension"):
        prog.main(["--sortie", str(tmp_path), "--note-effectifs", str(note_ext), "--mode", "etalon"])
    # m11 : --regle-cas-mixte exige --additif-cas-mixte scellé citant la règle, et est lié à l'état de la note
    additif = tmp_path / "additif.md"
    additif.write_text("# Additif\nRègle retenue : taches_controlees_seules.\n", encoding="utf-8")
    prog.sceller(additif)
    with pytest.raises(GardeArret, match="--additif-cas-mixte"):
        prog.main(["--sortie", str(tmp_path), "--taille", "8,8,3", "--regle-cas-mixte", "taches_controlees_seules"])
    with pytest.raises(GardeArret, match="ne mentionne pas"):
        prog.main(["--sortie", str(tmp_path), "--taille", "8,8,3", "--regle-cas-mixte", "constante_par_dose",
                   "--additif-cas-mixte", str(additif)])
    # note sans cas mixte -> règle refusée
    with pytest.raises(GardeArret, match="refusé hors cas mixte"):
        prog.main(["--sortie", str(tmp_path), "--note-effectifs", str(note_ok), "--mode", "complet",
                   "--regle-cas-mixte", "taches_controlees_seules", "--additif-cas-mixte", str(additif)])
    # note avec cas mixte -> bloque sans règle
    n_mixte = _note()
    n_mixte["scores_bbis"]["doses"][0]["plis"][0].update(actions_en_origine_et_en_relu=4, taches_avec_controle_du_chemin=2)
    note_mixte = _note_md(tmp_path, n_mixte, "note_mixte.md")
    with pytest.raises(GardeArret, match="cas mixte détecté"):
        prog.main(["--sortie", str(tmp_path), "--note-effectifs", str(note_mixte), "--mode", "complet"])
    # cas mixte avec règle + additif scellé valide passe jusqu'à l'exécution
    assert prog.main(["--sortie", str(tmp_path / "run_mixte"), "--note-effectifs", str(note_mixte), "--mode", "complet",
                      "--repliques", "1", "--nul", "5", "--tirages", "20", "--d", "16", "--entropie", "3",
                      "--mondes", "trace_faible", "--nul-identite", "5", "--autoriser-depot-sale",
                      "--regle-cas-mixte", "taches_controlees_seules", "--additif-cas-mixte", str(additif)]) == 0

