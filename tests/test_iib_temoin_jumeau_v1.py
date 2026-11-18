"""(ii-b), témoin-jumeau v1 : réécriture de la valeur entière du champ COST (décision M4) sur tous les cas de la table de la section 10 :
valeur à un nombre, à plusieurs nombres, à calcul (« 8 × 250 h = 2 000 »), à intervalle, à unité, en gras, milliers à virgule et à
espace, « k », nombre collé à « h » ; champ suivi de PREDICTION ou en fin d'action ; action sans estimation inchangée. Après
réécriture : le lecteur neuf relit exactement le nombre de la médiane basse, `cout_plusieurs_nombres` est faux, tout le reste de
l'action est égal à l'octet. Deux tokeniseurs jouets : par caractères, et à jetons de plusieurs caractères (chevauchements)."""
from __future__ import annotations

import pytest

from controle_ia.environnements.propositions import lire_action
from controle_ia.gardes import GardeArret
from controle_ia.harnais.modeles import tokeniseur_caracteres_chat
from controle_ia.iib import jouet_v1 as jv
from controle_ia.iib.oracle_v1 import coupe_du_prefixe
from controle_ia.iib.temoin_jumeau_v1 import bornes_de_la_valeur, reecrire_valeur_cout
from controle_ia.t06.cout import lire_cout

TOK_CAR = tokeniseur_caracteres_chat()
TOK_MORCEAUX = jv.FauxTokeniseur(morceaux=[")\n", ":**", " h\n", "000\nPRED", "COST", "ACTION", "TITLE", "PROPOSAL", " GPU", "-hours"])
VALEURS = ["1200", "1,200", "1 200", "2k", "120h", "1200 GPU-hours", "8 × 250 h = 2 000", "100-200", "between 100 and 300",
           "**1200**", "1,000 (8 × 125)", "a few thousand", " 3 400 GPU-hours, roughly"]
NOMBRES = ["950", "1,500", "2k", "1 000"]


def _action(valeur: str, suite: str = "\nPREDICTION: ok", cle: str = "COST:") -> str:
    return f"ACTION: ADD\nTITLE: Router\nPROPOSAL: Compare top-1 and top-2.\nCONTROLS: seeds\n{cle} {valeur}{suite}"


def _ids(tok, texte, fin=True):
    ids = list(tok(texte, add_special_tokens=False)["input_ids"])
    return ids + ([0] if fin and isinstance(tok, jv.FauxTokeniseur) else [])


def _verifier(tok, texte, nombre):
    if tok is TOK_CAR:                                   # le tokeniseur par caractères n'a pas « × » : « x » (même forme pour le lecteur)
        texte = texte.replace("×", "x")
    ids = _ids(tok, texte)
    c = coupe_du_prefixe(tok, ids, texte)
    assert c["conforme"], (texte, c)
    r = reecrire_valeur_cout(tok, ids, texte, c["rang"], nombre)
    neuf = r["texte"]
    assert tok.decode(r["ids"], skip_special_tokens=True) == neuf
    champ = lire_action(neuf).champs.get("COST")
    lu = lire_cout(champ)
    assert lu["cout"] == lire_cout(nombre)["cout"], (texte, neuf)
    assert not lu["cout_plusieurs_nombres"], neuf
    v0, coeur_fin, _ = bornes_de_la_valeur(texte, len(tok.decode(ids[:c["rang"]], skip_special_tokens=True)))
    assert neuf == texte[:v0] + " " + nombre + texte[coeur_fin:]                        # tout le reste égal à l'octet
    assert r["ids"][:c["rang"]] == ids[:c["rang"]]                                       # rien d'avant la valeur n'est retokenisé
    return r, neuf


@pytest.mark.parametrize("tok", [TOK_CAR, TOK_MORCEAUX], ids=["caracteres", "morceaux"])
@pytest.mark.parametrize("valeur", VALEURS)
@pytest.mark.parametrize("suite", ["\nPREDICTION: ok", "", "\n"], ids=["suivi_de_PREDICTION", "fin_d_action", "fin_saut_de_ligne"])
def test_reecriture_de_la_valeur_entiere(tok, valeur, suite):
    for nombre in NOMBRES:
        r, neuf = _verifier(tok, _action(valeur, suite), nombre)
        if suite.startswith("\nPRED"):
            assert neuf.endswith("\nPREDICTION: ok")                                   # saut de ligne final gardé, PREDICTION intacte


def test_calcul_aucun_nombre_du_maitre_ne_reste():
    texte = _action("8 × 250 h = 2 000")
    r, neuf = _verifier(TOK_MORCEAUX, texte, "950")
    champ = lire_action(neuf).champs["COST"]
    assert champ == "950" and "250" not in neuf and "2 000" not in neuf and "8 ×" not in neuf


@pytest.mark.parametrize("cle", ["**COST:**", "**COST**:", "__COST:__"])
def test_cle_en_gras_la_fermeture_reste_a_la_cle(cle):
    for tok in (TOK_CAR, TOK_MORCEAUX):
        texte = _action("1200", cle=cle)
        r, neuf = _verifier(tok, texte, "950")
        assert cle in neuf and lire_action(neuf).champs["COST"] == "950"


def test_jeton_qui_chevauche_la_valeur_et_la_suite_est_retokenise_avec_elle():
    texte = _action("1,000 (8 × 125)")
    r, neuf = _verifier(TOK_MORCEAUX, texte, "950")
    assert r["chevauchement"] is True and neuf.endswith(" 950\nPREDICTION: ok")
    texte = _action("2 000")
    r, neuf = _verifier(TOK_MORCEAUX, texte, "1,500")                         # jeton « 000\nPRED » : retokenisé avec la valeur
    assert r["chevauchement"] is True and "PREDICTION: ok" in neuf


def test_valeur_sur_plusieurs_lignes_jusqu_a_la_cle_suivante():
    texte = _action("1200\n(rough estimate)\n")
    r, neuf = _verifier(TOK_CAR, texte, "950")
    assert "rough" not in neuf and neuf.endswith(" 950\n\nPREDICTION: ok")


def test_action_sans_coupe_conforme_n_a_pas_d_estimation_donc_reste_inchangee():
    """Sans coupe conforme, l'oracle ne tire aucune suite : l'action n'a pas d'estimation et n'est jamais réécrite (comptée)."""
    texte = "ACTION: ADD\nTITLE: x\nPROPOSAL: y\nPREDICTION: ok"
    c = coupe_du_prefixe(TOK_CAR, _ids(TOK_CAR, texte), texte)
    assert not c["conforme"] and not c["champ_cout"]


@pytest.mark.parametrize("nombre", ["", "  ", "1\n2"])
def test_artefact_nombre_illisible_refuse(nombre):
    texte = _action("1200")
    ids = _ids(TOK_CAR, texte)
    c = coupe_du_prefixe(TOK_CAR, ids, texte)
    with pytest.raises(GardeArret, match="illisible"):
        reecrire_valeur_cout(TOK_CAR, ids, texte, c["rang"], nombre)


def test_artefact_identifiants_qui_ne_rendent_pas_le_texte():
    texte = _action("1200")
    ids = _ids(TOK_CAR, texte)
    c = coupe_du_prefixe(TOK_CAR, ids, texte)
    with pytest.raises(GardeArret, match="décodage"):
        reecrire_valeur_cout(TOK_CAR, ids, texte + "x", c["rang"], "950")
