"""Remplacement de la valeur du coût dans une action, v5 (texte scellé, 3.3 c et d ; section 13, `reecriture_v5.py`)."""
import math

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.iib import lecture_cout_v5 as lc
from controle_ia.iib import reecriture_v5 as rw
from controle_ia.iib.jouet_v5 import TokeniseurJouet
from controle_ia.t06.cout import NOMBRE, valeur_du_nombre

TOK = TokeniseurJouet()
FINS = frozenset({0})
TETE = "ACTION: ADD\nTITLE: A\nPROPOSAL: p\nCONTROLS: c\n"


def _action(valeur: str, cle: str = "COST:", queue: str = "\nPREDICTION: ok", tok=TOK):
    ids = tok(TETE + cle + valeur + queue)["input_ids"] + [0]
    return ids, lc.coupe_du_prefixe(tok, ids)["rang"]


def _suite(texte: str, tok=TOK):
    return tok(texte + "\n")["input_ids"]


def test_texte_entier_de_la_suite_et_artefact_de_la_premiere_course():
    tok = TokeniseurJouet(morceaux=(" GPUs", " for", " hours", " 100"))
    ids, rang = _action(" 900", tok=tok)
    r = rw.remplacer_valeur(tok, ids, rang, _suite(" 4 GPUs for 100 hours", tok), FINS)
    assert r["texte"] == TETE + "COST: 4 GPUs for 100 hours\nPREDICTION: ok"
    assert tok.decode(r["ids"]) == r["texte"] and r["ids"][-1] == 0 and not r["separateur_insere"]
    # une suite de plus de 16 jetons n'existe pas : la fenêtre la coupe (jetons d'un caractère)
    assert rw.remplacer_valeur(TOK, *_action(" 900"), _suite(" 4 GPUs for 100 hours"), FINS)["texte"] == TETE + "COST: 4 GPUs for 100\nPREDICTION: ok"
    # artefact : la réécriture de la première course ne gardait que le premier nombre (« 4 ») — ce n'est pas le texte rendu
    ancien = TETE + "COST: " + NOMBRE.search(" 4 GPUs for 100 hours").group(0) + "\nPREDICTION: ok"
    assert ancien.endswith("COST: 4\nPREDICTION: ok") and r["texte"] != ancien


def test_les_jetons_de_la_suite_sont_colles_tels_quels():
    tok = TokeniseurJouet(morceaux=("GPU", "480", "\nPRED"))
    ids, rang = _action(" 900", tok=tok)
    suite = tok(" 480 GPU-hours\n")["input_ids"]
    r = rw.remplacer_valeur(tok, ids, rang, suite, FINS)
    assert r["jetons_de_suite_colles"] == len(suite) - 1 and not r["elargie"]
    debut = r["ids"].index(suite[0], rang)
    assert r["ids"][debut:debut + len(suite) - 1] == suite[:-1]
    assert tok.decode(r["ids"]) == TETE + "COST: 480 GPU-hours\nPREDICTION: ok"


def test_suite_vide_et_suite_commencant_par_une_espace():
    ids, rang = _action(" 900 GPU-hours")
    vide = rw.remplacer_valeur(TOK, ids, rang, [], FINS)
    assert vide["texte"] == TETE + "COST:\nPREDICTION: ok"
    assert not lc.lire_action_v5(TOK, vide["ids"], FINS)["cout_lisible"]
    espace = rw.remplacer_valeur(TOK, ids, rang, _suite(" 480"), FINS)
    assert espace["texte"] == TETE + "COST: 480\nPREDICTION: ok"
    sans = rw.remplacer_valeur(TOK, ids, rang, _suite("480"), FINS)
    assert sans["texte"] == TETE + "COST:480\nPREDICTION: ok"          # rien n'est ajouté ni retiré en tête


def test_valeur_de_plusieurs_lignes_remplacee():
    ids, rang = _action(" 900\n  for the large run\n  and 20 more")
    r = rw.remplacer_valeur(TOK, ids, rang, _suite(" 480"), FINS)
    assert r["valeur_origine_plusieurs_lignes"] and r["texte"] == TETE + "COST: 480\nPREDICTION: ok"


def test_cle_en_gras_fermee_apres_les_deux_points():
    ids, rang = _action(" 900", cle="**COST:**")
    # la suite ne porte pas les marques : elles restent à la clé
    r = rw.remplacer_valeur(TOK, ids, rang, _suite(" 480"), FINS)
    assert r["texte"] == TETE + "**COST:** 480\nPREDICTION: ok" and not r["a_la_coupe"]
    # la suite, tirée après la coupe, porte elle-même les marques : la clé reste fermée une seule fois
    r2 = rw.remplacer_valeur(TOK, ids, rang, _suite("** 480"), FINS)
    assert r2["texte"] == TETE + "**COST:** 480\nPREDICTION: ok" and r2["a_la_coupe"]
    assert lc.lire_action_v5(TOK, r2["ids"], FINS)["cout_declare"] == 480


def test_separateur_insere():
    assert rw.separateur("COST: 5PREDICTION: ok", 7, 7) == ("\n", True)
    assert rw.separateur("COST: 5\nPREDICTION: ok", 7, 8) == ("\n", False)
    assert rw.separateur("COST: 5", 7, 7) == ("", False)                 # fin de l'action : rien à insérer


def test_garde_decodage_et_champs_cas_sain_et_artefacts():
    ids, rang = _action(" 900")
    assert rw.remplacer_valeur(TOK, ids, rang, _suite(" 480"), FINS)["texte"].count("PREDICTION: ok") == 1
    # artefact : une suite qui ouvre une clé change les champs de l'action → arrêt
    with pytest.raises(GardeArret, match="mêmes champs"):
        rw.exiger_memes_champs(TETE + "COST: 900\nPREDICTION: ok", TETE + "COST: 480\nPREDICTION: no")
    # artefact : un tokeniseur dont le décodage ne redonne jamais le texte → arrêt
    class Infidele(TokeniseurJouet):
        casse = False

        def __call__(self, texte, add_special_tokens=False):
            return super().__call__(texte.replace("\n", "") if self.casse else texte)
    faux = Infidele()
    ids2 = faux(TETE + "COST: 900\nPREDICTION: ok")["input_ids"]
    suite = faux(" 480\n")["input_ids"]
    rang2 = lc.coupe_du_prefixe(faux, ids2)["rang"]
    faux.casse = True
    with pytest.raises(GardeArret, match="décodage"):
        rw.remplacer_valeur(faux, ids2, rang2, suite, FINS)
    with pytest.raises(GardeArret, match="rang de coupe"):
        rw.remplacer_valeur(TOK, ids, 0, [], FINS)


@pytest.mark.parametrize("original, delta, attendu", [
    (" 480", math.log10(2.0), " 960"), (" 1,200 GPU-hours", math.log10(2.5), " 3,000 GPU-hours"), (" 1 200", math.log10(2.0), " 2 400"),
    (" 1.2k", math.log10(2.0), " 2.4k"), (" 120h", math.log10(2.0), " 240h"), (" 4 GPUs for 100 hours", math.log10(2.0), " 8 GPUs for 100 hours"),
    (" 800", math.log10(2.5), " 2000"), (" 3", math.log10(2.1), " 6.3"), (" 12345", math.log10(2.0), " 24690"), (" 999,999", math.log10(1.5), " 1,500,000")])
def test_multiplication_dans_la_forme_de_l_original(original, delta, attendu):
    ids, rang = _action(original)
    r = rw.multiplier_cout(TOK, ids, rang, delta, FINS)
    assert r["texte"] == TETE + "COST:" + attendu + "\nPREDICTION: ok" and TOK.decode(r["ids"]) == r["texte"]
    m = NOMBRE.search(original)
    cible = valeur_du_nombre(m["n"], m["k"]) * 10 ** delta
    relu = lc.lire_action_v5(TOK, r["ids"], FINS)["cout_declare"]
    assert abs(relu / cible - 1) <= 5.1e-4 and r["valeur_ecrite"] == relu          # à l'arrondi de quatre chiffres significatifs près


def test_multiplication_nulle_rend_l_action_a_l_octet_et_refus_sans_nombre():
    ids, rang = _action(" 480 GPU-hours")
    r = rw.multiplier_cout(TOK, ids, rang, 0.0, FINS)
    assert r["ids"] == ids and not r["multipliee"]
    ids2, rang2 = _action(" a few hundred")
    with pytest.raises(GardeArret, match="aucun nombre"):
        rw.multiplier_cout(TOK, ids2, rang2, 0.3, FINS)


def test_ecrire_nombre_quatre_chiffres_significatifs_au_plus():
    assert rw.ecrire_nombre(1234.56, "100") == "1235" and rw.ecrire_nombre(12.3456, "10") == "12.35"
    assert rw.ecrire_nombre(99996.0, "1,000") == "100,000" and rw.ecrire_nombre(1.2564, "1,5") == "1,26"
    with pytest.raises(GardeArret):
        rw.ecrire_nombre(0.0, "1")
