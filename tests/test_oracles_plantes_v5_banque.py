"""Lot B1 — plantation, clés scellées, sous-banque, base aléatoire, rejeu (P8, A1, déterminisme) : cas sains et
artefacts (R5). Racines d'essai seulement."""
import json
from pathlib import Path

import pytest

import controle_ia.oracles_plantes_v5.rejeu as rejeu_mod
from controle_ia.gardes import GardeArret
from controle_ia.oracles_plantes_v5 import banque as banque_mod
from controle_ia.oracles_plantes_v5.base_aleatoire import tirer_base
from controle_ia.oracles_plantes_v5.cles import (charger_cle, ecrire_monde, fragments_de_cle, octets_json,
                                                 verifier_absence_fuite)
from controle_ia.oracles_plantes_v5.graines import generateur
from controle_ia.oracles_plantes_v5.parametres import charger
from controle_ia.oracles_plantes_v5.rejeu import executer, main, rejouer_batterie_banque, violations_a1
from controle_ia.oracles_plantes_v5.sous_banque import tirer_sous_banque
from controle_ia.oracles_plantes_v5.tests_de_mort import sortie_de_texte, t1_forme
from controle_ia.scellement import empreinte

P, _ = charger()
RACINE_ESSAI = 20261122


@pytest.fixture(scope="module")
def banque():
    return banque_mod.construire_banque(RACINE_ESSAI, P)


@pytest.fixture(scope="module")
def rejeu_a(tmp_path_factory):
    d = tmp_path_factory.mktemp("rejeu") / "a"
    code, rapport = executer(RACINE_ESSAI, d)
    return d, code, rapport


# ---------------------------------------------------------------- banque et plantation
def test_banque_douze_mondes_312_plantes(banque):
    assert [m.famille for m, _ in banque] == ["F1"] * 4 + ["F2"] * 4 + ["F3"] * 4
    assert sum(len(p) for _, p in banque) == 312
    for _m, plantes in banque:
        compte = {}
        for p in plantes:
            compte[p.etiquette] = compte.get(p.etiquette, 0) + 1
        assert compte == {"VERITE_PLANTEE": 8, "FAUX_TOT": 4, "PIEGE": 4, "TEMOIN_TRIVIAL": 5, "TEMOIN_GROSSIER": 5}


def test_pieges_certifies_dans_l_intervalle(banque):
    for m, plantes in banque:
        for p in plantes:
            if p.etiquette == "PIEGE":
                assert m.N < max(int(v) for v in p.instance.values()) <= 3 * m.N
            if p.etiquette == "FAUX_TOT":
                mx = banque_mod._max_nat(m.analyser(p.texte), p.instance)
                assert mx is None or mx <= m.N


def test_plantation_refuse_une_fausse_verite(banque):
    m, plantes = banque[8]
    faux = next(p.texte for p in plantes if p.etiquette == "FAUX_TOT")
    assert banque_mod.certifier(m, "verites", faux) is None
    triviale = next(p.texte for p in plantes if p.etiquette == "TEMOIN_TRIVIAL")
    assert banque_mod.certifier(m, "verites", triviale) is None  # une vérité plantée doit être non triviale


def test_plantation_refuse_un_piege_tue_sous_N(banque):
    m, plantes = banque[0]
    faux = next(p.texte for p in plantes if p.etiquette == "FAUX_TOT")
    assert banque_mod.certifier(m, "pieges", faux) is None


def test_plantation_refuse_un_piege_sans_contre_exemple_dans_l_intervalle(banque):
    m, plantes = banque[4]
    vraie = next(p.texte for p in plantes if p.etiquette == "VERITE_PLANTEE")
    assert banque_mod.certifier(m, "pieges", vraie) is None  # vrai au-delà : aucun contre-exemple dans ]N .. 3N]
    assert banque_mod.certifier(m, "pieges", f"pour tout t dans NAT, t <= {4 * m.N}") is None  # faux seulement au-delà de 3N
    assert banque_mod.certifier(m, "pieges", f"pour tout t dans NAT, t <= {m.N}") is not None  # cas sain


def test_plantation_gabarit_non_realisable_leve(monkeypatch, banque):
    m, _ = banque[0]
    monkeypatch.setattr(m, "gabarits_pieges", lambda rng: [("mauvais", ["pour tout t dans NAT, vt(t) < 2"])] * 4)
    with pytest.raises(GardeArret, match="refusé à la plantation"):
        banque_mod.planter(m, RACINE_ESSAI, P)


def test_plantation_doublon_de_verite_refuse_par_t5(monkeypatch, banque):
    m, _ = banque[0]
    t = "pour tout t dans NAT, vt(t) <= vt(t + 1)"
    monkeypatch.setattr(m, "gabarits_verites", lambda rng: [("v", [t])] * 8)
    with pytest.raises(GardeArret, match="refusé à la plantation"):
        banque_mod.planter(m, RACINE_ESSAI, P)


def test_plantation_doublon_de_faux_tot_refuse(monkeypatch, banque):
    m, _ = banque[0]
    t = "pour tout t dans NAT, vt(t) = t * vt(1)"
    monkeypatch.setattr(m, "gabarits_faux_tot", lambda rng: [("f", [t])] * 4)
    with pytest.raises(GardeArret, match="même forme normale"):
        banque_mod.planter(m, RACINE_ESSAI, P)


# ---------------------------------------------------------------- clés
def test_cle_et_definition_distinctes_sans_fuite(rejeu_a):
    d, _, _ = rejeu_a
    dossiers = sorted((d / "mondes").iterdir())
    assert len(dossiers) == 12
    for w in dossiers:
        o_def = (w / "definition-servie-v5.json").read_bytes()
        cle = charger_cle(w / "cle-v5.json")
        verifier_absence_fuite(o_def, fragments_de_cle(cle))  # aucun octet de la clé dans la définition servie
        for p in cle["plantes"]:
            assert p["texte"].encode() not in o_def
        assert (w / "cle-v5.json.sha256").exists() and (w / "definition-servie-v5.json.sha256").exists()


def test_fuite_detectee(banque, tmp_path):
    m, plantes = banque[0]
    m.indice = 0
    ecrire_monde(tmp_path / "sain", m, "monde-essai", plantes, P["statut"])  # cas sain
    orig = m.axiomes
    m.axiomes = lambda: orig() + [plantes[0].texte]  # artefact : un énoncé planté glissé dans la définition servie
    with pytest.raises(GardeArret, match="fuite"):
        ecrire_monde(tmp_path / "fuite", m, "monde-essai", plantes, P["statut"])


def test_cle_alteree_d_un_octet_refusee(rejeu_a, tmp_path):
    d, _, _ = rejeu_a
    src = next((d / "mondes").iterdir())
    for nom in ("cle-v5.json", "cle-v5.json.sha256"):
        (tmp_path / nom).write_bytes((src / nom).read_bytes())
    assert charger_cle(tmp_path / "cle-v5.json")  # cas sain
    o = bytearray((tmp_path / "cle-v5.json").read_bytes())
    o[len(o) // 2] ^= 0x01
    (tmp_path / "cle-v5.json").write_bytes(bytes(o))
    with pytest.raises(GardeArret):
        charger_cle(tmp_path / "cle-v5.json")


# ---------------------------------------------------------------- P8 et A1
def test_p8_conforme_sur_la_banque_d_essai(rejeu_a):
    _, code, r = rejeu_a
    assert code == 0 and not r["A1_violee"] and r["temoins_conformes"] and r["ecarts"] == []
    t = r["total"]
    assert t["FAUX_TOT"] == {"plantes": 48, "tues": 48}
    assert t["VERITE_PLANTEE"] == {"plantes": 96, "tues": 0}
    assert t["PIEGE"] == {"plantes": 48, "tues": 0}
    assert t["TEMOIN_TRIVIAL"]["tues"] == 0 and t["TEMOIN_GROSSIER"] == {"plantes": 60, "tues": 60}
    assert r["autocontrole_t6_instances_de_cle"] == {"verifies": 96, "non_verifies": 0}
    assert r["redites_parmi_plantes_vivantes"]["analysables"] == 0


def _cles(d):
    return [charger_cle(w / "cle-v5.json") for w in sorted((d / "mondes").iterdir())]


def test_a1_declenchee_par_une_fausse_verite_injectee(banque, rejeu_a):
    d, _, _ = rejeu_a
    cles = _cles(d)
    mondes = [m for m, _ in banque]
    assert violations_a1(rejouer_batterie_banque(mondes, cles)) == []  # cas sain
    i = next(k for k, p in enumerate(cles[3]["plantes"]) if p["etiquette"] == "VERITE_PLANTEE")
    faux = next(p["texte"] for p in cles[3]["plantes"] if p["etiquette"] == "FAUX_TOT")
    cles[3]["plantes"][i]["texte"] = faux
    v = violations_a1(rejouer_batterie_banque(mondes, cles))
    assert v and "vérité tuée" in v[0]


@pytest.mark.parametrize("etiquette,remplacement,motif", [
    ("FAUX_TOT", "VERITE_PLANTEE", "faux tôt vivant"),
    ("PIEGE", "FAUX_TOT", "piège tué sous N"),
])
def test_a1_autres_violations(banque, rejeu_a, etiquette, remplacement, motif):
    d, _, _ = rejeu_a
    cles = _cles(d)
    c = cles[9]["plantes"]
    i = next(k for k, p in enumerate(c) if p["etiquette"] == etiquette)
    c[i]["texte"] = next(p["texte"] for p in c if p["etiquette"] == remplacement)
    assert any(motif in e for e in violations_a1(rejouer_batterie_banque([m for m, _ in banque], cles)))


def test_rejeu_sort_en_erreur_si_a1_violee(monkeypatch, tmp_path, capsys):
    vraie = rejeu_mod.charger_cle

    def charger_avec_artefact(chemin):
        cle = vraie(chemin)
        if cle["indice_monde"] == 5:
            p = cle["plantes"]
            i = next(k for k, x in enumerate(p) if x["etiquette"] == "VERITE_PLANTEE")
            p[i]["texte"] = next(x["texte"] for x in p if x["etiquette"] == "TEMOIN_GROSSIER")
        return cle

    monkeypatch.setattr(rejeu_mod, "charger_cle", charger_avec_artefact)
    code = main(["--racine", str(RACINE_ESSAI), "--sortie", str(tmp_path / "r")])
    assert code == 3
    assert json.loads(capsys.readouterr().out)["A1_violee"] is True


def test_rejeu_refuse_un_dossier_non_vide(tmp_path):
    (tmp_path / "x").write_text("déjà là")
    assert main(["--racine", "1", "--sortie", str(tmp_path)]) == 1


# ---------------------------------------------------------------- déterminisme
def _empreintes(d: Path) -> dict:
    return {str(p.relative_to(d)): empreinte(p) for p in sorted(d.rglob("*"))
            if p.is_file() and not p.name.startswith("manifeste")}


def test_deterministe_meme_racine_memes_empreintes(rejeu_a, tmp_path):
    d, _, _ = rejeu_a
    code, _ = executer(RACINE_ESSAI, tmp_path / "b")
    assert code == 0
    assert _empreintes(d) == _empreintes(tmp_path / "b")
    m = json.loads((tmp_path / "b" / "manifeste-rejeu-v5.json").read_text(encoding="utf-8"))
    assert m["sorties_sha256"] == json.loads((d / "manifeste-rejeu-v5.json").read_text(encoding="utf-8"))["sorties_sha256"]


def test_racines_differentes_banques_differentes(banque):
    autre = banque_mod.construire_mondes(RACINE_ESSAI + 1, P)
    assert [m.p for m, _ in banque] != [m.p for m in autre]


# ---------------------------------------------------------------- sous-banque S/N
def test_sous_banque_stratifiee_sans_etiquette(banque):
    # v5 (brouillon 2) : 150 analysés, 48 témoins servis hors analyse, 10 seconds services : 208 items
    ids = [f"monde-{k}" for k in range(12)]
    servie, cle = tirer_sous_banque(banque, ids, RACINE_ESSAI, P["sous_banque"])
    assert len(servie["items"]) == 208 and len(cle["items"]) == 208
    analyses = [it for it in cle["items"] if it["role"] == "analyse"]
    compte = {}
    for it in analyses:
        compte[it["etiquette"]] = compte.get(it["etiquette"], 0) + 1
    assert compte == {"VERITE_PLANTEE": 75, "FAUX_TOT": 38, "PIEGE": 37}
    temoins = [it for it in cle["items"] if it["role"] == "temoin_hors_analyse"]
    assert len(temoins) == 48
    for w in ids:
        t = [it["etiquette"] for it in temoins if it["identifiant_monde"] == w]
        assert t.count("TEMOIN_TRIVIAL") == 2 and t.count("TEMOIN_GROSSIER") == 2
    doubles = [it for it in cle["items"] if it["role"] == "second_service"]
    ids_analyses = {it["identifiant"] for it in analyses}
    assert len(doubles) == 10 and all(d["double_de"] in ids_analyses for d in doubles)
    par_monde = {}
    for it in analyses:
        par_monde.setdefault(it["identifiant_monde"], []).append(it["etiquette"])
    assert all(6 <= l.count("VERITE_PLANTEE") <= 7 and 3 <= l.count("FAUX_TOT") <= 4 for l in par_monde.values())
    assert len({it["identifiant"] for it in servie["items"]}) == 208
    o = octets_json(servie)
    for tok in ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE", "TEMOIN", "etiquette", "gabarit", "role", "double_de"):
        assert tok.encode() not in o
    assert set(servie["items"][0]) == {"identifiant", "identifiant_monde", "enonce"}
    again, _ = tirer_sous_banque(banque, ids, RACINE_ESSAI, P["sous_banque"])
    assert again == servie


def test_sous_banque_quota_impossible_refuse(banque):
    with pytest.raises(GardeArret):
        tirer_sous_banque(banque, [str(k) for k in range(12)], RACINE_ESSAI, {"vrais": 200, "faux_tot": 0, "pieges": 0})


# ---------------------------------------------------------------- base « grammaire aléatoire »
def test_base_aleatoire_24_par_monde_dans_la_grammaire(banque):
    for m, _ in banque[::4]:
        textes = tirer_base(generateur(RACINE_ESSAI, 9, m.indice), m, P["base_aleatoire"])
        assert len(textes) == 24
        assert all(t1_forme(sortie_de_texte(t), m)[0].type.value == "conforme" for t in textes)
        assert textes == tirer_base(generateur(RACINE_ESSAI, 9, m.indice), m, P["base_aleatoire"])


def test_piege_seuil_sain_et_non_realisable(banque):
    m, _ = banque[8]  # F3
    rng = generateur(RACINE_ESSAI, 1, 99)
    cands = m.piege_seuil(rng, "u(n)", var="n")
    assert cands and all(banque_mod.certifier(m, "pieges", c) is not None for c in cands)
    assert m.piege_seuil(rng, "U0 + 0 * n", var="n") == []  # constante : aucun piège possible
    assert m.piege_seuil(rng, "u(n - 1)", var="n") == []  # indéfinie en 0 : refusé
