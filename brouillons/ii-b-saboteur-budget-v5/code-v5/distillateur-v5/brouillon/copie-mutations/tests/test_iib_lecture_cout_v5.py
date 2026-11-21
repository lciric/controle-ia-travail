"""Lecture d'un coût sur la fenêtre commune, v5 (texte scellé, section 13, `lecture_cout_v5.py`)."""
import pytest

from controle_ia.iib import lecture_cout_v5 as lc
from controle_ia.iib.jouet_v5 import TokeniseurJouet
from controle_ia.t06.cout import cout_action, cout_lisible, lire_cout

TOK = TokeniseurJouet()
TETE = "ACTION: ADD\nTITLE: A\nPROPOSAL: p\nCONTROLS: c\n"
QUEUE = "\nPREDICTION: ok"
# forme → texte écrit après « COST: » (jusqu'à la clé suivante exclue)
FORMES = {
    "un nombre": " 480",
    "plusieurs": " 4 GPUs 100 h",
    "calcul": " 4 x 100",
    "intervalle": " 100-200",
    "unite": " 480 GPU-hours",
    "multiplicateur": " 2 × 240",
    "milliers a virgule": " 1,200",
    "milliers a espace": " 1 200",
    "suffixe k": " 1.2k",
    "nombre colle a h": " 120h",
    "valeur a la ligne qui suit la cle": "\n 500",
    "valeur vide": "",
    "nombre au-dela de la limite": " about some hours, say 300",
    "nombre a cheval sur la limite": " about maybe 123456",
    "texte sans nombre": " a few hundred",
}


def _action(apres_cle: str, cle: str = "COST:") -> list[int]:
    return TOK(TETE + cle + apres_cle + QUEUE)["input_ids"] + [0]


def _comme_suite(apres_cle: str) -> list[int]:
    """Le même texte présenté comme une suite du jumeau : tronqué à 16 jetons, arrêté au premier saut de ligne."""
    ids = TOK(apres_cle + "\n")["input_ids"]
    sortie = []
    for i in ids[:lc.FENETRE]:
        sortie.append(i)
        if TOK.decode([i]) == "\n":
            break
    return sortie


@pytest.mark.parametrize("forme", sorted(FORMES))
def test_egalite_des_deux_lectures_forme_par_forme(forme):
    ids = _action(FORMES[forme])
    a = lc.lire_action_v5(TOK, ids, frozenset({0}))
    assert a["coupe"]["conforme"], forme
    s = lc.lire_fenetre(TOK, _comme_suite(FORMES[forme]), frozenset({0}))
    assert a["fenetre"]["valeur"] == s["valeur"] and a["fenetre"]["lisible"] == s["lisible"], forme
    for k in ("vide", "tronquee", "nombre_au_bord", "formes"):
        assert a["fenetre"][k] == s[k], (forme, k)
    lc.exiger_lecture(a["fenetre"])


def test_valeurs_et_formes_attendues():
    lu = {f: lc.lire_action_v5(TOK, _action(t), frozenset({0}))["fenetre"] for f, t in FORMES.items()}
    assert lu["un nombre"]["valeur"] == 480 and lu["milliers a virgule"]["valeur"] == 1200 and lu["milliers a espace"]["valeur"] == 1200
    assert lu["suffixe k"]["valeur"] == 1200 and lu["suffixe k"]["formes"]["suffixe_k"]
    assert lu["nombre colle a h"]["valeur"] == 120 and lu["nombre colle a h"]["formes"]["unite_presente"]
    assert lu["unite"]["formes"]["unite_presente"] and not lu["un nombre"]["formes"]["unite_presente"]
    assert lu["plusieurs"]["valeur"] == 4 and lu["plusieurs"]["formes"]["plusieurs_nombres"]
    assert lu["calcul"]["formes"]["multiplication"] and lu["multiplicateur"]["formes"]["multiplication"]
    assert lu["intervalle"]["formes"]["intervalle"] and lu["milliers a espace"]["formes"]["milliers_espace"]
    for f in ("valeur a la ligne qui suit la cle", "valeur vide"):
        assert not lu[f]["lisible"] and lu[f]["vide"] and not lu[f]["formes"]["champ_present"]
    assert not lu["texte sans nombre"]["lisible"] and not lu["texte sans nombre"]["vide"]
    assert not lu["nombre au-dela de la limite"]["lisible"] and lu["nombre au-dela de la limite"]["tronquee"]
    c = lu["nombre a cheval sur la limite"]
    assert c["nombre_au_bord"] and c["tronquee"] and not c["lisible"] and c["valeur"] is None


def test_nombre_au_bord_cas_sain_et_artefact():
    # sain : le nombre finit avant la limite, une lettre le sépare de la fin : lisible même si la fenêtre est tronquée
    sain = lc.lire_fenetre(TOK, TOK(" 480 GPU-hours total")["input_ids"], frozenset({0}))
    assert sain["tronquee"] and not sain["nombre_au_bord"] and sain["valeur"] == 480
    # artefact : seuls des chiffres, espaces, virgule, point ou « k » le séparent de la fin de la fenêtre : illisible
    for texte in (" 12345678901234567", " 1,200,000,000,00", "            1 200", "             1.2k"):
        ids = TOK(texte)["input_ids"][:lc.FENETRE]
        assert len(ids) == lc.FENETRE
        r = lc.lire_fenetre(TOK, ids, frozenset({0}))
        assert r["nombre_au_bord"] and not r["lisible"], texte
    # sans troncature (saut de ligne dans la fenêtre), le même nombre est lisible
    assert lc.lire_fenetre(TOK, TOK(" 1234567\n")["input_ids"], frozenset({0}))["valeur"] == 1234567


def test_fin_de_tour_dans_la_fenetre():
    ids = TOK(" 480")["input_ids"] + [0] + TOK("999999999999999")["input_ids"]
    r = lc.lire_fenetre(TOK, ids, frozenset({0}))
    assert r["valeur"] == 480 and not r["tronquee"] and r["n_jetons"] == 4
    action = TOK(TETE + "COST: 480")["input_ids"] + [0]
    assert lc.lire_action_v5(TOK, action, frozenset({0}))["fenetre"]["valeur"] == 480


def test_cle_en_gras_fermee_apres_les_deux_points():
    a = lc.lire_action_v5(TOK, _action(" 500", cle="**COST:**"), frozenset({0}))
    assert a["coupe"]["conforme"] and a["fenetre"]["valeur"] == 500 and not a["fenetre"]["vide"]
    s = lc.lire_fenetre(TOK, _comme_suite("** 500"), frozenset({0}))
    assert s["valeur"] == 500


def test_cle_suivie_aussitot_de_la_cle_suivante_coupe_conforme_fenetre_illisible():
    a = lc.lire_action_v5(TOK, _action(""), frozenset({0}))
    assert a["coupe"]["conforme"] and not a["cout_lisible"] and a["fenetre"]["vide"]


def test_coupe_fonction_du_seul_prefixe():
    """La coupe ne change pas quand la valeur change : deux actions de même préfixe ont le même rang de coupe."""
    rangs = {lc.coupe_du_prefixe(TOK, _action(t))["rang"] for t in FORMES.values()}
    assert len(rangs) == 1
    r = rangs.pop()
    assert TOK.decode(_action(" 480")[:r]).endswith("COST:")


def test_coupe_non_conforme_artefacts():
    # champ absent
    c = lc.coupe_du_prefixe(TOK, TOK("ACTION: ADD\nTITLE: A")["input_ids"])
    assert c == {"champ_cout": False, "conforme": False, "rang": None, "motif": "champ_absent"}
    # un jeton chevauche la clé et sa valeur
    tok = TokeniseurJouet(morceaux=(": 4",))
    ids = tok(TETE + "COST: 480" + QUEUE)["input_ids"]
    c = lc.coupe_du_prefixe(tok, ids)
    assert c["champ_cout"] and not c["conforme"] and c["motif"] == "chevauchement_cle_valeur"
    a = lc.lire_action_v5(tok, ids)
    assert a["fenetre"] is None and not a["cout_lisible"] and a["ancien_lecteur"] == 480 and a["ecart_des_deux_lecteurs"]
    # cas sain du même tokeniseur : jeton « : » avec espace, la coupe reste conforme
    tok2 = TokeniseurJouet(morceaux=(": ",))
    c2 = lc.coupe_du_prefixe(tok2, tok2(TETE + "COST: 480" + QUEUE)["input_ids"])
    assert c2["conforme"] and tok2.decode(tok2(TETE + "COST: 480")["input_ids"][:c2["rang"]]).endswith("COST: ")


def test_artefact_la_paire_de_lecteurs_de_la_premiere_course_differe_sur_trois_formes_et_elles_seules():
    """Lecteurs de la première course : l'agent par le champ entier (`cout_action`), le jumeau par le premier nombre de sa
    suite coupée au premier saut de ligne et à 16 jetons. Ils doivent différer sur trois formes, et sur elles seules ; la
    fenêtre commune, elle, ne diffère sur aucune (essai d'égalité ci-dessus)."""
    different = set()
    for forme, texte in FORMES.items():
        agent = cout_action(TOK.decode(_action(texte)))["cout"]
        agent = agent if cout_lisible(agent) else None
        jumeau = lire_cout(TOK.decode(_comme_suite(texte)).split("\n", 1)[0])["cout"]
        jumeau = jumeau if cout_lisible(jumeau) else None
        if agent != jumeau:
            different.add(forme)
    assert different == {"valeur a la ligne qui suit la cle", "nombre au-dela de la limite", "nombre a cheval sur la limite"}
    for forme in different:
        a = lc.lire_action_v5(TOK, _action(FORMES[forme]), frozenset({0}))
        assert a["ecart_des_deux_lecteurs"], forme


def test_schema_d_une_lecture_refuse_une_cle_de_plus():
    l = lc.lire_fenetre(TOK, TOK(" 480\n")["input_ids"])
    lc.exiger_lecture(l)
    with pytest.raises(Exception):
        lc.exiger_lecture({**l, "texte": " 480"})
