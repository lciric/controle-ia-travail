"""Essais du calcul versionné des conditions du plafond de l'étage 2 à 200 témoins (ligne 3) — v1.

Lancement (depuis le dossier de ce fichier) :
env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_calcul_conditions_plafond_200_v1.py

- à 100 témoins et 25 USD : le calcul redonne la sortie v3 clé par clé, et les chiffres du
  devis v7 à l'octet (texte scellé lu par empreinte), dont l'issue « 18 témoins, non concluant
  par manque de témoins » (texte l. 384) ;
- à 200 témoins et 88,36 USD : l'issue du pire cas ; la frontière du plafond, de part et
  d'autre (facteur du tarif ; plafond en centimes) ;
- un cas sain et un artefact par garde (règle R5).
"""

import copy
import hashlib
import json
import math
from decimal import Decimal
from fractions import Fraction

import pytest

import calcul_conditions_plafond_200_ligne_3_v1 as c

RACINE = "/home/user/controle-ia-travail"
DOSSIER = "/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-calcul-plafond-200"
DEVIS_V7 = DOSSIER + "/devis-ligne-3-etage-payant-v7.md"
DEVIS_V7_SHA = "382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270"


@pytest.fixture(scope="module")
def t():
    return c.tarifs(RACINE)


@pytest.fixture(scope="module")
def devis():
    with open(DEVIS_V7, "rb") as f:
        octets = f.read()
    assert hashlib.sha256(octets).hexdigest() == DEVIS_V7_SHA
    return octets.decode("utf-8")


@pytest.fixture(scope="module")
def sortie_v3():
    return c.lire(RACINE, c.SORTIE_V3, c.SORTIE_V3_SHA)


def couts(t, f):
    return {j: t["par_appel"][j] * f for j in c.JUGES}


# ---------------------------------------------------------------- à 100 témoins

def test_100_egal_a_la_sortie_v3(t, sortie_v3):
    r = c.comparer_a_v3(sortie_v3, c.valeurs_v3_recalculees(t))
    assert r["toutes_egales"], r["cles_differentes"]
    assert r["cles_comparees"] == 83


def test_100_chiffres_du_devis_v7_a_l_octet(t, devis):
    pa, fa = t["par_appel"], t["facteurs"]
    f = c.Formule(100, 2500, pa, comme_v3=True)
    tot = {k: c.cout_du_plan(100, pa, fa[k])[2] for k in fa}
    tot200 = {k: c.cout_du_plan(200, pa, fa[k])[2] for k in fa}
    pire_refus = [f.temoins_b_complets(fa["pire"], r) for r in (0, 1, 2, 3)]
    haut_refus = [f.temoins_b_complets(1, r) for r in (5, 10)]
    attendus = [
        f"| **{c.fr(tot['estimation'])} USD** | **{c.fr(tot['haut'])} USD** | **{c.fr(tot['pire'])} USD** |",
        f"| {sum(sum(b.values()) for b in c.plan_appels(100).values())} | **{c.fr(tot['estimation'])} USD**",
        f"| si tous les envois sont refusés : envois qui partent avant l'arrêt | {f.envois_si_tous_refuses()} "
        f"({c.fr(Fraction(f.envois_si_tous_refuses() * 60, 100))} USD comptés) |",
        f"| envois refusés que la base entière supporte sans coupure, à l'estimation | {f.refus_supportes(tot['estimation'])} |",
        f"| au cas haut | {f.refus_supportes(tot['haut'])} |",
        f"| au pire cas | {f.refus_supportes(tot['pire'])} (la base est déjà coupée) |",
        f"| au cas haut, témoins complets au bloc B avec 5 envois refusés ; avec 10 | {haut_refus[0]} ; {haut_refus[1]} |",
        f"| plomberie et bloc A | **{c.fr(f.facteur_bloc_a(), 1)} fois** ({c.fr(f.facteur_bloc_a())}) |",
        f"| {c.fr(f.facteur_pour_b_complets(40))} fois |",
        f"| {c.fr(f.facteur_pour_b_complets(50))} fois |",
        f"| {c.fr(f.facteur_pour_b_complets(100), 3)} fois |",
        f"({c.fr(fa['pire'] * (f.p + f.a + 18 * f.b))} USD comptés avec les 18 premiers témoins du bloc B)",
        f"le bloc B ne l'est que sur **{pire_refus[0]} témoins** ({pire_refus[1]} avec un envoi refusé, "
        f"{pire_refus[2]} avec deux, {pire_refus[3]} avec trois)",
        "**le verdict est « non concluant par manque de témoins »**",
        f"la banque peut monter à **{f.temoins_au_plus(True, 400)} témoins** au plus "
        f"({f.temoins_au_plus(False, 400)} sans la réserve de session)",
        f"(elle coûterait {c.fr(fa['pire'] * (f.p + f.a + 40 * f.b))} USD)",
        f"| 200 témoins | {c.fr(tot200['estimation'])} USD | {c.fr(tot200['haut'])} USD | {c.fr(tot200['pire'])} USD |",
    ]
    for a in attendus:
        assert a in devis, a


def test_100_issue_du_pire_l_384(t):
    s = c.simuler(100, 2500, couts(t, t["facteurs"]["pire"]))
    assert (s["A_complets"], s["B_complets"], s["lecture_complets"]) == (100, 18, 18)
    assert s["envois_partis"] == 259 and s["B_partiels"] == [19]
    cle, en_clair = c.verdict(s)
    assert cle == "manque"
    assert "non concluant par manque de témoins" in en_clair and "jamais lu comme un « non »" in en_clair
    refus = [c.simuler(100, 2500, couts(t, t["facteurs"]["pire"]), refus=r)["B_complets"] for r in (1, 2, 3)]
    assert refus == [16, 13, 11]


# ---------------------------------------------------------------- à 200 témoins

def test_200_issue_du_pire(t):
    s = c.simuler(200, 8836, couts(t, t["facteurs"]["pire"]))
    assert s["envois_prevus"] == 1004 and s["envois_partis"] == 996
    assert (s["A_complets"], s["B_complets"], s["lecture_complets"], s["etalonnage_complets"]) == (200, 197, 100, 97)
    assert s["B_partiels"] == [198]
    assert (s["coupure"]["bloc"], s["coupure"]["temoin"], s["coupure"]["juge"], s["coupure"]["rendu"]) == \
        ("B", 198, "juge-argon", 2)
    assert s["cumul"] + Fraction(60, 100) > Fraction(8836, 100) >= s["cumul"]
    assert c.verdict(s)[0] == "coupe_sans_manque"


def test_200_cas_haut_et_attendu_entiers(t):
    for cas in ("haut", "estimation"):
        s = c.simuler(200, 8836, couts(t, t["facteurs"][cas]))
        assert s["envois_partis"] == 1004 and s["coupure"] is None and c.verdict(s)[0] == "entier"
        assert s["cumul"] == c.cout_du_plan(200, t["par_appel"], t["facteurs"][cas])[2]


def test_200_frontiere_du_facteur_de_part_et_d_autre(t):
    f = c.Formule(200, 8836, t["par_appel"])
    fx = c.facteur_exact(f, 200)
    assert c.simuler(200, 8836, couts(t, fx))["envois_partis"] == 1004
    assert c.simuler(200, 8836, couts(t, fx + c.EPSILON_FRONTIERE))["envois_partis"] == 1003
    assert fx < t["facteurs"]["pire"]


def test_200_frontiere_du_plafond_en_centimes_de_part_et_d_autre(t):
    for cas in ("haut", "pire"):
        cs = couts(t, t["facteurs"][cas])
        total = c.cout_du_plan(200, t["par_appel"], t["facteurs"][cas])[2]
        avant_dernier = total - cs["juge-argon"]
        juste = math.ceil(avant_dernier * 100 + 60)
        assert c.simuler(200, juste, cs)["envois_partis"] == 1004
        assert c.simuler(200, juste - 1, cs)["envois_partis"] == 1003
    # Le pire cas n'est coupé à 88,36 USD que par la réserve : il passe entier à 88,92 USD.
    cs = couts(t, t["facteurs"]["pire"])
    assert c.simuler(200, 8892, cs)["envois_partis"] == 1004
    assert c.simuler(200, 8836, cs)["envois_partis"] == 996


def test_200_seuils_de_refus_au_pire(t):
    lignes = c.balayer_refus(200, 8836, couts(t, t["facteurs"]["pire"]))
    s = c.seuils_de_refus(200, lignes)
    assert s == {"sans_aucune_coupure": None, "moitie_lecture_entiere_au_bloc_B": 39,
                 "moitie_lecture_au_seuil_de_40": 64, "plomberie_et_bloc_A_complets": 80}


# ---------------------------------------------------------------- gardes : cas sain et artefact

def test_garde_empreinte(sortie_v3):
    assert sortie_v3["version"] == "calcul-devis-ligne-3-v3"
    with pytest.raises(SystemExit):
        c.lire(RACINE, c.SORTIE_V3, "0" * 64)


def test_garde_centimes_entiers():
    assert c.centimes(8836) == 8836
    for artefact in (88.36, True, Decimal("88.36")):
        with pytest.raises(TypeError):
            c.centimes(artefact)
    with pytest.raises(TypeError):
        c.simuler(200, 88.36, {j: Fraction(1, 100) for j in c.JUGES})


def test_garde_grandeur_exacte():
    assert c.exacte(Fraction(1, 3)) == Fraction(1, 3)
    with pytest.raises(TypeError):
        c.simuler(200, 8836, {j: 0.05 for j in c.JUGES})


def test_garde_sortie_sans_flottant():
    c.verifier_sans_flottant({"a": "1.0", "b": [1, True, None]})
    with pytest.raises(SystemExit):
        c.verifier_sans_flottant({"a": {"b": [0.5]}})


def test_garde_cout_releve_au_dessus_de_la_reserve():
    sain = c.simuler(200, 100000, {j: Fraction(60, 100) for j in c.JUGES})
    assert sain["arret"] is None and sain["envois_partis"] == 1004
    artefact = c.simuler(200, 100000, {j: Fraction(61, 100) for j in c.JUGES})
    assert artefact["arret"] is not None and artefact["envois_partis"] == 1


def test_garde_envoi_refuse_compte_jamais_zero(t):
    sain = c.simuler(200, 8836, couts(t, 1))
    assert sain["cumul"] == c.cout_du_plan(200, t["par_appel"], 1)[2]
    tous = c.simuler(200, 8836, {j: Fraction(0) for j in c.JUGES}, tous_refuses=True)
    assert tous["envois_partis"] == 147 and tous["cumul"] == Fraction(8820, 100) and tous["rendus_obtenus"] == 0
    assert c.simuler(100, 2500, {j: Fraction(0) for j in c.JUGES}, tous_refuses=True)["envois_partis"] == 41


def test_garde_controle_a_100(t, sortie_v3):
    assert c.comparer_a_v3(sortie_v3, c.valeurs_v3_recalculees(t))["toutes_egales"]
    faussee = copy.deepcopy(sortie_v3)
    faussee["compteur_d_arret"]["temoins_B_complets_au_pire_cas_selon_les_envois_refuses"]["0"] = 19
    r = c.comparer_a_v3(faussee, c.valeurs_v3_recalculees(t))
    assert not r["toutes_egales"]
    assert r["cles_differentes"] == ["compteur_d_arret.temoins_B_complets_au_pire_cas_selon_les_envois_refuses.0"]


def test_garde_frontiere(t):
    f = c.Formule(200, 8836, t["par_appel"])
    fx = c.facteur_exact(f, 40)
    assert c.verifier_frontiere(200, 8836, t["par_appel"], fx, 40)
    with pytest.raises(SystemExit):
        c.verifier_frontiere(200, 8836, t["par_appel"], fx * Fraction(101, 100), 40)


def test_garde_plan():
    assert sum(sum(b.values()) for b in c.plan_appels(200).values()) == 1004
    for artefact in (201, 0, 200.0):
        with pytest.raises(ValueError):
            c.plan_appels(artefact)


def test_garde_aucun_argument():
    with pytest.raises(SystemExit):
        c.main(["calcul", "sortie.json"])


def test_rejeu_egal_a_l_octet():
    a = json.dumps(c.calculer(RACINE), ensure_ascii=False, indent=1, sort_keys=True)
    b = json.dumps(c.calculer(RACINE), ensure_ascii=False, indent=1, sort_keys=True)
    assert a == b
