"""Essai sur le tokeniseur réel, sur processeur (contre-lecture du code v5 : « rien d'éprouvé sans tokeniseur réel »).

Coupe, fenêtre de 16 jetons, dichotomie des décodages cumulés, réécriture par une suite et multiplication du coût, sur le
tokeniseur de Llama-3.1-8B-Instruct à la révision figée. L'essai ne télécharge rien : il lit `tokenizer.json` au chemin donné par
`IIB_TOKENISEUR_REEL` et demande la bibliothèque `tokenizers` ; sans l'un ou l'autre il est **sauté** (et le dit).
Deux décodages sont éprouvés : le décodage brut, et le décodage « nettoyé » que la configuration du tokeniseur demande à
`transformers` (`clean_up_tokenization_spaces` : une espace devant un point, une virgule, etc. est retirée au décodage)."""
import math
import os

import pytest

from controle_ia.iib import lecture_cout_v5 as lc
from controle_ia.iib import reecriture_v5 as rw

CHEMIN = os.environ.get("IIB_TOKENISEUR_REEL", "")
tokenizers = pytest.importorskip("tokenizers", reason="bibliothèque `tokenizers` absente : essai sur le tokeniseur réel sauté")
pytestmark = pytest.mark.skipif(not os.path.isfile(CHEMIN), reason="IIB_TOKENISEUR_REEL ne désigne pas un tokenizer.json : essai sauté")
SHA_ATTENDUE = "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"
TETE = "ACTION: ADD\nTITLE: Sparse routing ablation\nPROPOSAL: Train 4 variants on 3 seeds each, é × ü included.\nCONTROLS: seeds, baseline\n"
QUEUE = "\nPREDICTION: Top-1 gap under 2 points."


class Reel:
    """Interface qu'emploie le code (`tok(texte)["input_ids"]`, `tok.decode`), sur `tokenizers.Tokenizer`."""

    def __init__(self, nettoyer: bool):
        self.t = tokenizers.Tokenizer.from_file(CHEMIN)
        self.nettoyer = nettoyer

    def __call__(self, texte, add_special_tokens=False):
        return {"input_ids": self.t.encode(texte, add_special_tokens=False).ids}

    def decode(self, ids, skip_special_tokens=True):
        s = self.t.decode(list(ids), skip_special_tokens=skip_special_tokens)
        if self.nettoyer:                                    # `transformers`, clean_up_tokenization
            for a, b in ((" .", "."), (" ?", "?"), (" !", "!"), (" ,", ","), (" ' ", "'"), (" n't", "n't"), (" 'm", "'m"), (" 's", "'s"),
                         (" 've", "'ve"), (" 're", "'re")):
                s = s.replace(a, b)
        return s


@pytest.fixture(scope="module", params=[False, True], ids=["decodage-brut", "decodage-nettoye"])
def tok(request):
    return Reel(request.param)


VALEURS = {" 480": 480.0, " 1,200 GPU-hours": 1200.0, " 1.2k": 1200.0, " 120h": 120.0, " 4 GPUs for 100 hours": 4.0, " 2 × 240": 2.0,
           " 100-200": 100.0, " 1 200": 1200.0, " about 300 GPU-hours": 300.0, " a few hundred": None, " ~350": 350.0,
           " 2,500 (roughly)": 2500.0}


def _action(tok, valeur, cle="COST:"):
    return tok(TETE + cle + valeur + QUEUE)["input_ids"]


def test_empreinte_du_tokeniseur():
    import hashlib

    assert hashlib.sha256(open(CHEMIN, "rb").read()).hexdigest() == SHA_ATTENDUE


@pytest.mark.parametrize("valeur", sorted(VALEURS))
def test_coupe_conforme_et_lecture_egale_des_deux_cotes(tok, valeur):
    ids = _action(tok, valeur)
    a = lc.lire_action_v5(tok, ids)
    assert a["coupe"]["conforme"], a["coupe"]
    assert tok.decode(ids[:a["coupe"]["rang"]]).rstrip(" \t").endswith("COST:")
    assert a["cout_declare"] == VALEURS[valeur]
    suite = tok(valeur + "\n")["input_ids"][:lc.FENETRE]
    s = lc.lire_fenetre(tok, suite)
    assert s["valeur"] == a["fenetre"]["valeur"] and s["formes"] == a["fenetre"]["formes"], valeur


@pytest.mark.parametrize("cle", ["COST:", "Cost:", "COST :", "**COST**:", "**COST:**", "__COST:__", "**Cost:** "])
def test_coupe_selon_la_forme_de_la_cle(tok, cle):
    a = lc.lire_action_v5(tok, _action(tok, " 480", cle))
    assert a["coupe"]["conforme"] and a["cout_declare"] == 480.0, (cle, a["coupe"])


@pytest.mark.parametrize("valeur, cle", [("", "COST:"), ("\n 500", "COST:")])
def test_constat_un_jeton_reel_chevauche_la_cle_et_ce_qui_la_suit(tok, valeur, cle):
    """Constat, écrit tel que le code le traite : le tokeniseur réel a un jeton « :\\n » (et « :**\\n »). Une valeur vide ou une
    valeur à la ligne suivante n'ont donc **aucune coupe conforme** : l'action est comptée (coupe non conforme, motif de
    chevauchement), non bornable, et reste telle quelle dans les contextes ; le texte scellé traite ce cas par l'épreuve de la
    coupe. La clé en gras fermée après les deux-points (« **COST:** », jeton « :** ») a, elle, sa coupe conforme, après les
    marques (règle de la version 1 ; essais ci-dessous)."""
    ids = _action(tok, valeur, cle)
    c = lc.coupe_du_prefixe(tok, ids)
    assert c == {"champ_cout": True, "conforme": False, "rang": None, "motif": "chevauchement_cle_valeur"}
    a = lc.lire_action_v5(tok, ids)
    assert a["fenetre"] is None and not a["cout_lisible"]


@pytest.mark.parametrize("valeur", [" 480", " 1,200 GPU-hours", " a few hundred", " 4 GPUs for 100 hours"])
@pytest.mark.parametrize("cle", ["**COST:**", "__COST:__"])
def test_cle_en_gras_fermee_apres_les_deux_points_coupe_conforme_lecture_egale_reecriture_retrouvee(tok, cle, valeur):
    """Vérification de la contre-lecture, R1 : la coupe tombe après les marques qui ferment la clé ; la fenêtre commence après
    elles ; lecture égale des deux côtés ; la réécriture garde les marques à la clé (3.3 c) et se retrouve au décodage."""
    ids = _action(tok, valeur, cle)
    a = lc.lire_action_v5(tok, ids)
    rang = a["coupe"]["rang"]
    import re
    prefixe = tok.decode(ids[:rang])
    assert a["coupe"]["conforme"] and re.sub(r"[*_]", "", prefixe).rstrip(" \t").endswith("COST:")
    if cle == "**COST:**":
        assert prefixe.endswith("**COST:**")              # jeton « :** » : la coupe tombe après les marques
    assert a["cout_declare"] == VALEURS[valeur]
    s = lc.lire_fenetre(tok, tok(valeur + "\n")["input_ids"][:lc.FENETRE])
    assert s["valeur"] == a["fenetre"]["valeur"] and s["formes"] == a["fenetre"]["formes"]
    suite = tok(" 777 GPU-hours\n")["input_ids"]
    r = rw.remplacer_valeur(tok, ids, rang, suite)
    assert r["texte"] == TETE + cle + " 777 GPU-hours" + QUEUE and tok.decode(r["ids"]) == r["texte"]
    relu = lc.lire_action_v5(tok, r["ids"])
    assert relu["coupe"]["rang"] == rang and relu["cout_declare"] == 777.0
    m = rw.multiplier_cout(tok, ids, rang, math.log10(2.0)) if VALEURS[valeur] else None
    assert m is None or lc.lire_action_v5(tok, m["ids"])["cout_declare"] == 2 * VALEURS[valeur]


def test_la_coupe_ne_depend_pas_de_la_valeur(tok):
    rangs = {lc.coupe_du_prefixe(tok, _action(tok, v))["rang"] for v in VALEURS}
    assert len(rangs) == 1


@pytest.mark.parametrize("original", [" 900", " 900 GPU-hours", " 1,200", " about 300 GPU-hours (2 runs)", " 900\n  for the large run"])
@pytest.mark.parametrize("suite", [" 480", " 1,200 GPU-hours", " 4 GPUs for 100 hours", " a few hundred", "", " 3.5k", " 480 .", " 1 ,200"])
def test_reecriture_par_une_suite(tok, original, suite):
    ids = _action(tok, original)
    rang = lc.coupe_du_prefixe(tok, ids)["rang"]
    s_ids = tok(suite + "\n")["input_ids"][:lc.FENETRE] if suite else []
    r = rw.remplacer_valeur(tok, ids, rang, s_ids)
    attendu = rw.texte_de_suite(tok, s_ids)
    assert tok.decode(r["ids"]) == r["texte"] and r["texte"].startswith(tok.decode(ids[:rang]))
    assert r["texte"] == tok.decode(ids[:rang]) + attendu + "\n" + QUEUE.lstrip("\n")
    relu = lc.lire_action_v5(tok, r["ids"])
    assert relu["coupe"]["rang"] == rang and relu["cout_declare"] == lc.lire_fenetre(tok, s_ids)["valeur"]


@pytest.mark.parametrize("original, attendu", [(" 480", 960.0), (" 1,200 GPU-hours", 2400.0), (" 1.2k", 2400.0), (" 120h", 240.0), (" 1 200", 2400.0),
                                                 (" about 300 GPU-hours", 600.0)])
def test_multiplication_du_cout(tok, original, attendu):
    ids = _action(tok, original)
    rang = lc.coupe_du_prefixe(tok, ids)["rang"]
    r = rw.multiplier_cout(tok, ids, rang, math.log10(2.0))
    assert tok.decode(r["ids"]) == r["texte"] and lc.lire_action_v5(tok, r["ids"])["cout_declare"] == attendu
    avant, apres = tok.decode(ids), r["texte"]
    assert avant.split("COST:")[0] == apres.split("COST:")[0] and avant.split("\n")[-1] == apres.split("\n")[-1]


def test_dichotomie_la_longueur_du_decodage_cumule_ne_decroit_pas(tok):
    for valeur in VALEURS:
        ids = _action(tok, valeur)
        longueurs = [len(tok.decode(ids[:k])) for k in range(len(ids) + 1)]
        assert longueurs == sorted(longueurs), valeur
