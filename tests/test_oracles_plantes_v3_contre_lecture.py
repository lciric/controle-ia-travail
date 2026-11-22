"""Lot B1, v2 — un essai par remarque corrigée de la contre-lecture (`contre-lecture-code-lot-b1-v1.md`, `305bb4a3…`).

Chaque essai vise la garde corrigée. Rejoués sur la v1 (`OP_PAQUET=oracles_plantes_v1`), ils échouent, sauf celui de
la remarque 8 : elle portait sur l'essai, pas sur le code (voir la réponse à la contre-lecture). Les textes reprennent
les sondes 1, 3, 4 et 5 du contre-lecteur.
"""
import copy
import importlib
import json
import os

import numpy as np
import pytest

from controle_ia.gardes import GardeArret

PAQUET = os.environ.get("OP_PAQUET", "oracles_plantes_v3")


def mod(nom):
    return importlib.import_module(f"controle_ia.{PAQUET}.{nom}")


par = mod("parametres")
P, _ = par.charger()
tdm = mod("tests_de_mort")
lignee = mod("lignee")


@pytest.fixture(scope="module")
def mondes():
    return mod("banque").construire_mondes(11, P)


@pytest.fixture(scope="module")
def f3(mondes):
    return mondes[8]


def batterie(m, texte, **kw):
    return tdm.appliquer_batterie(tdm.sortie_de_texte(texte), m, **kw)


# ---------------------------------------------------------------- remarque 1 : NAT hors du préfixe de tête
@pytest.mark.parametrize("texte", ["(pour tout n dans NAT, u(n) >= 0) et vrai",
                                   "(pour tout n dans NAT, u(n) >= 0) implique faux",
                                   "(pour tout n dans NAT, u(n) >= 1) ou faux"])
def test_r1_nat_entre_parentheses_informe_sans_arret(f3, texte):
    r = batterie(f3, texte)  # sur la v1 : GardeArret levée dans l'évaluateur
    assert r.statut == "informe" and r.issues[0].type == tdm.TypeIssue.INFORME


def test_r1_cas_sain_parenthese_de_tete(f3):
    assert batterie(f3, "(pour tout n dans NAT, u(n) >= 1)").statut == "vivante"


# ---------------------------------------------------------------- remarque 2 : l'indéfini n'est plus effacé
def test_r2_cassini_ne_meurt_pas_par_heritage(f3, tmp_path):
    reg = lignee.Registre(tmp_path / "r.jsonl")
    C0 = f3.U1 ** 2 - f3.U0 * f3.u(2)
    c0 = mod("mondes").lit(C0)
    variante = f"pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) + w(n - 1) - w(n - 1) = {c0} * (-QU)^n"
    assert batterie(f3, variante, registre=reg).statut == "morte"  # indéfinie en n = 0
    r = batterie(f3, f"pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) = {c0} * (-QU)^n", registre=reg)
    assert r.statut == "vivante" and r.vraie_bornee


def test_r2_terme_nul_indefini(f3, tmp_path):
    reg = lignee.Registre(tmp_path / "r.jsonl")
    assert batterie(f3, "pour tout n dans NAT, u(n) + 0 * w(n - 1) > 0", registre=reg).statut == "morte"
    assert batterie(f3, "pour tout n dans NAT, u(n) > 0", registre=reg).statut == "vivante"


def test_r2_close_a_vrai_avec_indefini_n_empoisonne_pas_les_triviales(f3, tmp_path):
    reg = lignee.Registre(tmp_path / "r.jsonl")
    assert batterie(f3, "pour tout n dans NAT, w(n - 1) * 0 = 0", registre=reg).statut == "morte"
    r = batterie(f3, "1 = w(1)", registre=reg)
    assert r.statut == "vivante" and r.triviale


# ---------------------------------------------------------------- remarque 3 : « hors capacité » ne fait pas un profil
def test_r3_profil_hors_capacite_non_informatif(f3):
    nm = mod("normalisation")
    a = "pour tout n dans NAT, n >= 1 implique mod(w(30 * n), w(n)) = 0"
    b = "pour tout n dans NAT, n >= 1 implique mod(w(30 * n), w(3 * n)) = 0"
    fa, fb = (nm.normaliser(f3.analyser(t), f3, f3.ev) for t in (a, b))
    assert tdm.t5_redite(fb, f3, [fa]).type == tdm.TypeIssue.NON_REDITE


def test_r3_cas_sain_profil_informatif_toujours_redite(f3):
    nm = mod("normalisation")
    fa, fb = (nm.normaliser(f3.analyser(t), f3, f3.ev) for t in ("pour tout n dans NAT, u(n) <= 50",
                                                                  "pour tout n dans NAT, u(n) < 51"))
    assert tdm.t5_redite(fb, f3, [fa]).type == tdm.TypeIssue.REDITE


# ---------------------------------------------------------------- remarque 4 : tête de chaîne du registre
def _registre_deux_lignes(tmp_path):
    ch = tmp_path / "l.jsonl"
    reg = lignee.Registre(ch)
    reg.inscrire("a" * 64, "vivante", "batterie", "x")
    reg.inscrire("a" * 64, "morte", "T6", "contre-exemple vérifié")
    return ch, ch.read_text(encoding="utf-8").splitlines()


def test_r4_troncature_refusee(tmp_path):
    ch, lignes = _registre_deux_lignes(tmp_path)
    ch.write_text(lignes[0] + "\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        lignee.rejouer(ch)


def test_r4_derniere_ligne_modifiee_refusee(tmp_path):
    ch, lignes = _registre_deux_lignes(tmp_path)
    ch.write_text(lignes[0] + "\n" + lignes[1].replace('"morte"', '"vivante"') + "\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        lignee.rejouer(ch)


def test_r4_cas_sain_registre_intact(tmp_path):
    ch, _ = _registre_deux_lignes(tmp_path)
    assert lignee.rejouer(ch) == {"a" * 64: "morte"}


# ---------------------------------------------------------------- remarque 5 : flottant dans les paramètres
def test_r5_marges_flottantes_refusees():
    with pytest.raises(GardeArret):
        mod("famille_f2").MondeF2({"M": 2, "D": 20, "a": [1.5, 2], "b": [10, 11], "cfg": P["familles"]["F2"]}, 10,
                                  P["capacites"])


def test_r5_av_flottant_refuse():
    cfg = copy.deepcopy(P["familles"]["F3"])
    cfg["AV_choix"] = [1.5]
    with pytest.raises(GardeArret):
        mod("famille_f3").MondeF3.tirer(np.random.default_rng(1), cfg, P["capacites"])


def test_r5_decimal_json_refuse_a_la_lecture(tmp_path):
    brut = json.loads(par.CHEMIN.read_text(encoding="utf-8"))
    texte = json.dumps(brut, ensure_ascii=False).replace('"borne_N": 4', '"borne_N": 4.5')
    (tmp_path / "p.json").write_text(texte, encoding="utf-8")
    with pytest.raises(GardeArret):
        par.charger(tmp_path / "p.json")
    (tmp_path / "s.json").write_text(json.dumps(brut, ensure_ascii=False), encoding="utf-8")
    assert par.charger(tmp_path / "s.json")  # cas sain


# ---------------------------------------------------------------- remarque 6 : instance glissée dans un fichier servi
def test_r6_instance_indentee_detectee():
    cles = mod("cles")
    cle = {"plantes": [{"texte": "un énoncé planté", "etiquette": "PIEGE", "instance": {"n": 17}}]}
    servi = cles.octets_json({"items": [{"identifiant": "item-1", "instance": {"n": 17}}]})
    with pytest.raises(GardeArret):
        cles.verifier_absence_fuite(servi, cles.fragments_de_cle(cle), "sous-banque servie")


def test_r6_cas_sain_sans_instance():
    cles = mod("cles")
    cle = {"plantes": [{"texte": "un énoncé planté", "etiquette": "PIEGE", "instance": {"n": 17}}]}
    servi = cles.octets_json({"items": [{"identifiant": "item-1", "enonce": "autre chose"}]})
    cles.verifier_absence_fuite(servi, [f for f in cles.fragments_de_cle(cle) if f != "PIEGE"], "sous-banque servie")


# ---------------------------------------------------------------- remarque 8 : la branche « contradiction » est atteinte
def test_r8_contradiction_avec_les_definitions_atteinte(f3):
    nm = mod("normalisation")
    t = "u(1000) - u(1000) = 1"  # hors capacité à l'évaluation, clos à faux par le normaliseur
    f = f3.analyser(t)
    iss = tdm.t2_contre_exemple(f, f3, forme=nm.normaliser(f, f3, f3.ev))
    assert iss.type == tdm.TypeIssue.MORTE_CONTRADICTION
    # l'énoncé de l'essai de la v1 meurt, lui, par contre-exemple : il n'atteignait pas cette branche
    t1 = "pour tout n dans NAT, u(n + 2) != PU * u(n + 1) + QU * u(n)"
    f1 = f3.analyser(t1)
    assert tdm.t2_contre_exemple(f1, f3, forme=nm.normaliser(f1, f3, f3.ev)).type == tdm.TypeIssue.MORTE_CONTRE_EXEMPLE


# ---------------------------------------------------------------- remarques 9 et 10 : mort par T6 inscrite, héritée
def _s(instances):
    return json.dumps({"verdict": "faux", "contre_exemples": instances, "raison": "essai"})


def test_r9_mort_par_t6_inscrite_d_office(f3, tmp_path):
    reg = lignee.Registre(tmp_path / "r.jsonl")
    texte = f"pour tout n dans NAT, n <= {f3.N}"
    r = batterie(f3, texte, registre=reg)
    assert r.statut == "vivante"
    iss = tdm.appliquer_t6(_s([{"n": f3.N + 1}]), r.arbre, f3, reg)
    assert iss.tue() and reg.statut(tdm.cle_lignee(r.forme, f3)) == "morte"
    assert batterie(f3, f"pour tout q dans NAT, {f3.N} >= q", registre=reg).statut == "morte"


def test_r9_cas_sain_refutation_fausse_n_inscrit_rien(f3, tmp_path):
    reg = lignee.Registre(tmp_path / "r.jsonl")
    r = batterie(f3, f"pour tout n dans NAT, n <= {f3.N}", registre=reg)
    iss = tdm.appliquer_t6(_s([{"n": 0}]), r.arbre, f3, reg)
    assert not iss.tue() and reg.statut(tdm.cle_lignee(r.forme, f3)) == "vivante"


def test_r10_reformulation_entiere_d_un_piege_tue_heritee(f3, tmp_path):
    reg = lignee.Registre(tmp_path / "r.jsonl")
    c = f3.u(f3.N + 2)
    r = batterie(f3, f"pour tout n dans NAT, u(n) < {c}", registre=reg)
    assert r.statut == "vivante"
    assert tdm.appliquer_t6(_s([{"n": f3.N + 2}]), r.arbre, f3, reg).tue()
    r2 = batterie(f3, f"pour tout k dans NAT, u(k) <= {c - 1}", registre=reg)  # autre forme normale, même sens
    assert r2.forme.empreinte != r.forme.empreinte
    assert r2.statut == "morte" and r2.issues[-1].type == tdm.TypeIssue.MORTE_PAR_HERITAGE


def test_r10_cas_sain_verite_non_heritee(f3, tmp_path):
    reg = lignee.Registre(tmp_path / "r.jsonl")
    c = f3.u(f3.N + 2)
    r = batterie(f3, f"pour tout n dans NAT, u(n) < {c}", registre=reg)
    tdm.appliquer_t6(_s([{"n": f3.N + 2}]), r.arbre, f3, reg)
    assert batterie(f3, "pour tout n dans NAT, u(n) <= max(U0, U1) * (PU + QU)^n", registre=reg).statut == "vivante"


# ---------------------------------------------------------------- remarque 11 : le rejeu contrôle trivialité et pièges
@pytest.fixture(scope="module")
def banque_cles(mondes):
    b = mod("banque")
    cles = mod("cles")
    out = []
    for m in mondes[8:9]:
        plantes = b.planter(m, 11, P)
        out.append((m, cles.cle_du_monde(m, "monde-essai", plantes)))
    return out


def _remplacer(cle, etiquette, par_etiquette):
    cle = copy.deepcopy(cle)
    p = cle["plantes"]
    i = next(k for k, x in enumerate(p) if x["etiquette"] == etiquette)
    p[i]["texte"] = next(x["texte"] for x in p if x["etiquette"] == par_etiquette)
    return cle


def test_r11_cas_sain(banque_cles):
    rj = mod("rejeu")
    (m, cle), = banque_cles
    assert rj.violations_a1(rj.rejouer_batterie_banque([m], [cle])) == []


def test_r11_triviale_a_la_place_d_une_verite(banque_cles):
    rj = mod("rejeu")
    (m, cle), = banque_cles
    v = rj.violations_a1(rj.rejouer_batterie_banque([m], [_remplacer(cle, "VERITE_PLANTEE", "TEMOIN_TRIVIAL")]))
    assert any("vérité plantée triviale" in e for e in v)


def test_r11_piege_non_decide_sous_N(banque_cles):
    rj = mod("rejeu")
    (m, cle), = banque_cles
    cle2 = copy.deepcopy(cle)
    i = next(k for k, x in enumerate(cle2["plantes"]) if x["etiquette"] == "PIEGE")
    n0 = cle2["plantes"][i]["instance"]["n"]
    # vivant mais « non décidé » jusqu'à N (indices hors capacité), et l'instance de la clé reste un contre-exemple
    # vérifié : seul le nouveau contrôle du rejeu peut le relever
    cle2["plantes"][i]["texte"] = (f"pour tout n dans NAT, (n <= {m.N} et u(n * 100000) >= 0) ou "
                                   f"(n > {m.N} et n != {n0})")
    v = rj.violations_a1(rj.rejouer_batterie_banque([m], [cle2]))
    assert any("piège non vrai-borné ou trivial" in e for e in v), v
