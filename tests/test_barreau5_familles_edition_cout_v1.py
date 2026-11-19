"""Essais de l'opérateur d'édition du coût (barreau 5, `edition_cout_v1`) : chaque garde, un cas sain et un artefact (R5).
Tokeniseurs jouets seulement ; aucune donnée du programme."""
from __future__ import annotations

import math

import pytest

from controle_ia.barreau5_familles import edition_cout_v1 as ec
from controle_ia.environnements.propositions import EnvironnementPropositions, Tache
from controle_ia.gardes import GardeArret
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import ALPHABET, SPECIAUX, tokeniseur_caracteres_chat
from controle_ia.t06.cout import cout_action
from controle_ia.t06.distillation_transcription import transcription_honnete


def _tok_caracteres():
    return tokeniseur_caracteres_chat()


def _tok_chiffres():
    """Jetons de plusieurs caractères pour les nombres (groupes de 1 à 3 chiffres, comme le pré-découpage de Llama 3)."""
    from tokenizers import Regex, Tokenizer, decoders, models, pre_tokenizers
    from transformers import PreTrainedTokenizerFast

    vocab = dict(SPECIAUX)
    for ch in ALPHABET:
        vocab.setdefault(ch, len(vocab))
    for n in range(1000):
        for s in {str(n), f"{n:02d}", f"{n:03d}"}:
            vocab.setdefault(s, len(vocab))
    tok = Tokenizer(models.WordLevel(vocab=vocab, unk_token="<unk>"))
    tok.pre_tokenizer = pre_tokenizers.Split(pattern=Regex(r"\d{1,3}|\D"), behavior="isolated")
    tok.decoder = decoders.Fuse()
    return PreTrainedTokenizerFast(tokenizer_object=tok, bos_token="<s>", eos_token="</s>", pad_token="<pad>",
                                   unk_token="<unk>")


def _ids(tok, t):
    return list(tok(t, add_special_tokens=False)["input_ids"])


def _action(cout: str) -> str:
    return f"ACTION: ADD\nTITLE: Probe the router\nPROPOSAL: Measure X.\nCOST: {cout}\nPREDICTION: lower loss"


GRILLE = ec.grille_famille([])


@pytest.mark.parametrize("cout, jumeau, sur, ecrit_j, ecrit_s", [
    ("300 GPU-hours", 100.0, 1000.0, "COST: 100 GPU-hours", "COST: 1000 GPU-hours"),        # nombre simple
    ("1,500 GPU-hours", 500.0, 5000.0, "COST: 500 GPU-hours", "COST: 5,000 GPU-hours"),     # milliers à la virgule
    ("1 200 GPU-hours", 400.0, 4000.0, "COST: 400 GPU-hours", "COST: 4 000 GPU-hours"),     # milliers à l'espace
    ("3k GPU-hours", 1000.0, 10000.0, "COST: 1k GPU-hours", "COST: 10k GPU-hours"),         # suffixe « k »
    ("2,5 hours", 0.8, 8.0, "COST: 0,8 hours", "COST: 8 hours"),                            # virgule décimale
])
def test_edition_cas_sains_nombre_milliers_suffixe_decimale(cout, jumeau, sur, ecrit_j, ecrit_s):
    for tok in (_tok_caracteres(), _tok_chiffres()):
        texte = _action(cout)
        ids = _ids(tok, texte)
        j = ec.editer_action(tok, ids, texte, GRILLE, "jumeau")
        s = ec.editer_action(tok, ids, texte, GRILLE, "sur_saboteur")
        assert j["editable"] and s["editable"], (j["motif"], s["motif"])
        assert (j["valeur"], s["valeur"]) == (jumeau, sur)
        assert ecrit_j in j["texte"] and ecrit_s in s["texte"]
        assert cout_action(j["texte"])["cout"] == jumeau and cout_action(s["texte"])["cout"] == sur
        assert tok.decode(j["ids"], skip_special_tokens=True) == j["texte"]
        a, b = j["empan_origine"]
        assert j["ids"][:a] == ids[:a] and j["ids"][j["empan_neuf"][1]:] == ids[b:]   # seuls les jetons du nombre changent


@pytest.mark.parametrize("cout, motif", [("10-20 GPU-hours", "plusieurs nombres"), ("about a day", "coût illisible"),
                                         ("3 x 100 hours", "plusieurs nombres"), ("", "coût illisible")])
def test_edition_artefacts_intervalle_champ_sans_nombre_multiplication_refuses(cout, motif):
    tok = _tok_caracteres()
    texte = _action(cout)
    for m in ("jumeau", "saboteur", "sur_saboteur"):
        r = ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, m)
        assert not r["editable"] and motif in r["motif"]


def test_edition_artefact_intervalle_a_un_seul_nombre_lu_refuse_par_le_drapeau():
    tok = _tok_caracteres()
    texte = _action("100 to 200 hours")
    assert cout_action(texte)["cout_intervalle"]
    assert not ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, "jumeau")["editable"]


def test_edition_artefact_action_non_valide_refusee():
    tok = _tok_caracteres()
    texte = "TITLE: x\nCOST: 300 hours"                       # sans ligne ACTION
    r = ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, "jumeau")
    assert not r["editable"] and r["motif"] == "action non valide"


def test_facteur_1_rend_les_identifiants_d_origine_et_la_valeur():
    for tok in (_tok_caracteres(), _tok_chiffres()):
        texte = _action("1,234.5 GPU-hours")
        ids = _ids(tok, texte)
        r = ec.editer_action(tok, ids, texte, GRILLE, "saboteur")
        assert r["editable"] and r["ids"] == ids and r["texte"] == texte and r["valeur"] == 1234.5


def test_artefact_facteur_autre_que_1_change_les_identifiants():
    tok = _tok_chiffres()
    texte = _action("300 GPU-hours")
    ids = _ids(tok, texte)
    assert ec.editer_action(tok, ids, texte, GRILLE, "jumeau")["ids"] != ids


@pytest.mark.parametrize("m", ec.MANTISSES_BASE)
@pytest.mark.parametrize("e", [-1, 0, 1, 2, 3])
def test_facteur_3_puis_un_tiers_sur_la_grille_rendent_la_valeur_de_depart(m, e):
    v = float(f"{m * 10 ** e:.12g}")
    haut = ec.valeur_sur_grille(v, 3.0, GRILLE)
    assert ec.valeur_sur_grille(haut, 1.0 / 3.0, GRILLE) == v
    bas = ec.valeur_sur_grille(v, 1.0 / 3.0, GRILLE)
    assert ec.valeur_sur_grille(bas, 3.0, GRILLE) == v


def test_artefact_aller_retour_hors_grille_ne_rend_pas_la_valeur():
    """Un coût hors de la grille (mantisse 7, absente) n'est pas rendu par l'aller-retour : la propriété tient sur la
    grille, non en général (limite déclarée)."""
    assert ec.valeur_sur_grille(ec.valeur_sur_grille(7.0, 3.0, GRILLE), 1.0 / 3.0, GRILLE) != 7.0


def test_grille_de_la_famille_ajoute_les_mantisses_du_tirage_sans_bruit():
    g = ec.grille_famille([0.3, 40.5, 1500, None, -2, float("nan")])
    assert 4.05 in g and 3.0 in g and all(1 <= x < 10 for x in g) and len(g) == len(set(g))
    assert ec.mantisse(0.3) == 3.0 and ec.mantisse(4050) == 4.05
    with pytest.raises(GardeArret):
        ec.mantisse(0.0)


def test_valeur_sur_grille_proche_en_logarithme_et_artefact_grille_invalide():
    assert ec.valeur_sur_grille(300, 3.0, GRILLE) == 1000.0          # 900 : 1000 plus proche que 800 en logarithme
    assert ec.valeur_sur_grille(300, 1.0, (7.0,)) == 300               # φ = 1 : jamais la grille
    with pytest.raises(GardeArret):
        ec.valeur_sur_grille(300, 3.0, (12.0,))


def test_controle_par_action_cas_sain_et_artefacts():
    tok = _tok_caracteres()
    texte = _action("300 GPU-hours")
    ed = ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, "jumeau")
    d = texte.index("300")
    assert ec.controler_edition(tok, texte, ed["texte"], ed["ids"], 100.0, d, d + 3, 3) is None
    assert "lecteur gelé" in ec.controler_edition(tok, texte, ed["texte"], ed["ids"], 90.0, d, d + 3, 3)
    assert "décodé" in ec.controler_edition(tok, texte, ed["texte"], ed["ids"][:-1], 100.0, d, d + 3, 3)
    autre = ed["texte"].replace("Measure X.", "Measure Y.")
    assert ec.controler_edition(tok, texte, autre, _ids(tok, autre), 100.0, d, d + 3, 3) is not None


def test_artefact_nombre_brut_different_du_nombre_lu_non_editable():
    tok = _tok_caracteres()
    texte = "ACTION: ADD\nTITLE: t\nPROPOSAL: p\nCOST:\nCOST: 50 hours"     # occurrence vide sautée : 50 lu et localisé
    assert ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, "jumeau")["editable"]
    loc = ec.localiser_nombre_du_cout("ACTION: ADD\nTITLE: t\nPROPOSAL: p\nPREDICTION: 3")
    assert not loc["trouve"]


def _episodes(couts_par_ep, tok):
    eps = []
    for n, couts in enumerate(couts_par_ep):
        textes = [_action(c) for c in couts]
        eps.append({"episode": f"e{n}", "tache": {"identifiant": f"t{n}"}, "textes": textes,
                    "actions": [_ids(tok, t) + [tok.convert_tokens_to_ids("<|im_end|>")] for t in textes]})
    return eps


def test_controle_par_famille_cas_sain_et_artefacts():
    tok = _tok_caracteres()
    sain = ec.editer_tirage(tok, _episodes([["300 h", "1,500 h", "3k h"], ["40 h", "6 h", "120 h"]], tok),
                            ("jumeau", "saboteur", "sur_saboteur"))
    c = ec.controler_famille(sain)
    assert c["formee"] and c["part_non_editable"] == 0.0
    assert abs(c["medianes"]["jumeau"] + 0.477) <= 0.08 and abs(c["medianes"]["sur_saboteur"] - 0.477) <= 0.08
    trop = ec.editer_tirage(tok, _episodes([["300 h", "10-20 h", "about a day"], ["40 h"] * 3], tok),
                            ("jumeau", "saboteur", "sur_saboteur"))
    c2 = ec.controler_famille(trop)
    assert not c2["formee"] and any("non éditables" in m for m in c2["motifs"])
    # médiane hors de la tolérance : table fabriquée (aucune valeur ramenée à un tiers)
    for a in sain["table"][0]["actions"] + sain["table"][1]["actions"]:
        a["valeurs"]["jumeau"] = a["valeur_origine"]
    c3 = ec.controler_famille(sain)
    assert not c3["formee"] and any("jumeau : médiane" in m for m in c3["motifs"])


def test_action_non_editable_pour_tous_sort_pour_tous_et_reste_non_editee():
    tok = _tok_caracteres()
    eps = _episodes([["300 h", "10-20 h"]], tok)
    ed = ec.editer_tirage(tok, eps, ("jumeau", "saboteur", "sur_saboteur"))
    assert [a["editable"] for a in ed["table"][0]["actions"]] == [True, False]
    for m in ("jumeau", "saboteur", "sur_saboteur"):
        assert ed["actions"][m][0][1] == eps[0]["actions"][1]


@pytest.mark.parametrize("tokeniseur", ["caracteres", "chiffres"])
def test_action_non_editable_pour_un_seul_membre_sort_pour_tous_et_reste_non_editee(tokeniseur):
    """Forme du sondage S3 (mutation M17) : « 0,4 hours », dans un tirage qui met 1,25 dans la grille, donne au jumeau
    « 0,125 », que le lecteur gelé relit comme un millier ; l'action est non éditable pour le seul jumeau. Elle sort des
    cibles de tous, et ses identifiants d'origine restent dans les contextes de tous, sur-saboteur compris."""
    tok = _tok_caracteres() if tokeniseur == "caracteres" else _tok_chiffres()
    eps = _episodes([["1,25 hours", "0,4 hours", "300 hours"]], tok)
    grille = tuple(ec.grille_famille([1.25, 0.4, 300.0]))
    seul = {m: ec.editer_action(tok, eps[0]["actions"][1][:-1], eps[0]["textes"][1], grille, m) for m in ec.FACTEURS}
    assert not seul["jumeau"]["editable"] and seul["saboteur"]["editable"] and seul["sur_saboteur"]["editable"]
    ed = ec.editer_tirage(tok, eps, ("jumeau", "saboteur", "sur_saboteur"))
    ligne = ed["table"][0]["actions"][1]
    assert not ligne["editable"] and ligne["motif"].startswith("jumeau : lecteur gelé")
    for m in ("jumeau", "saboteur", "sur_saboteur"):
        assert ed["actions"][m][0][1] == eps[0]["actions"][1]
    assert ed["actions"]["sur_saboteur"][0][2] != eps[0]["actions"][2]          # l'action voisine, elle, est éditée


def _empan_minimal_independant(tok, ids, debut, fin):
    """Empans de caractères des jetons par décodage de chaque jeton seul (vrai pour les tokeniseurs jouets, où le texte est
    la concaténation des jetons) : calcul indépendant de `positions_des_jetons`."""
    pos, c = [], 0
    for i in ids:
        s = tok.decode([i], skip_special_tokens=True)
        pos.append((c, c + len(s)))
        c += len(s)
    k = [n for n, (a, b) in enumerate(pos) if b > a and a < fin and b > debut]
    return k[0], k[-1] + 1


@pytest.mark.parametrize("cout", ["300h", "~300 GPU-hours", "$300", "300.0 hours", "999 hours", "1,000 hours", "0.5 hours",
                                  "12 000,5 hours", "300 GPU-hours (approx.)", "1,200,000 hours", "2,5 hours"])
def test_empan_declare_egal_a_l_empan_minimal_recalcule_a_part(cout):
    """Forme du sondage S4 (mutation M09) : l'empan d'origine déclaré par l'épissure est l'empan minimal des jetons qui
    recouvrent le nombre, recalculé à part ; aucun jeton ne change hors de lui ; le texte relu égale le texte édité."""
    for tok in (_tok_caracteres(), _tok_chiffres()):
        texte = _action(cout)
        ids = _ids(tok, texte)
        loc = ec.localiser_nombre_du_cout(texte)
        for m in ("jumeau", "sur_saboteur"):
            r = ec.editer_action(tok, ids, texte, GRILLE, m)
            assert r["editable"], (cout, m, r["motif"])
            assert tuple(r["empan_origine"]) == _empan_minimal_independant(tok, ids, loc["debut"], loc["fin"])
            a, b = r["empan_origine"]
            assert r["ids"][:a] == ids[:a] and r["ids"][r["empan_neuf"][1]:] == ids[b:]
            assert tok.decode(r["ids"], skip_special_tokens=True) == r["texte"]


def test_suffixe_k_sous_1_non_editable_pour_tous_et_ecritures_particulieres_comptees():
    """Constat m-5 : « 2k » donnerait au jumeau « 0.6k » : action non éditable (pour tous, dans le tirage) ; « 0.5k »,
    déjà sous 1, reste éditable. « 300 » → « 1000 » (sur-saboteur) et « 300.0 » → « 100 » (jumeau) restent éditées et
    sont comptées par famille et par sens, sans rien décider."""
    tok = _tok_caracteres()
    texte = _action("2k GPU-hours")
    j = ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, "jumeau")
    assert not j["editable"] and "suffixe « k »" in j["motif"]
    assert ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, "sur_saboteur")["editable"]
    demi = _action("0.5k GPU-hours")
    assert ec.editer_action(tok, _ids(tok, demi), demi, GRILLE, "jumeau")["editable"]
    ed = ec.editer_tirage(tok, _episodes([["300 h", "300.0 h", "1,500 h"] * 4 + ["2k h"]], tok),
                          ("jumeau", "saboteur", "sur_saboteur"))
    assert [a["editable"] for a in ed["table"][0]["actions"]][-1] is False
    c = ec.controler_famille(ed)
    assert c["ecritures_particulieres"]["sur_saboteur"]["milliers_sans_separateur"] == 8     # « 300 » et « 300.0 »
    assert c["ecritures_particulieres"]["jumeau"]["decimales_perdues"] == 4                 # « 300.0 » → « 100 »
    assert c["ecritures_particulieres"]["jumeau"]["milliers_sans_separateur"] == 0
    assert c["formee"]                                                                      # comptées, sans décider


def _transcriptions(tok, eps, ed):
    fmt = FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
    env = EnvironnementPropositions(Tache("t0", "Which routing rule trains stably?"), 1, len(eps[0]["textes"]))
    return {m: transcription_honnete(fmt, env, ed["actions"][m][0]) for m in ("jumeau", "saboteur", "sur_saboteur")}


def test_egalite_des_transcriptions_hors_des_jetons_du_nombre_cas_sain_et_artefact():
    tok = _tok_caracteres()
    eps = _episodes([["300 h", "1,500 h", "about a day"]], tok)
    ed = ec.editer_tirage(tok, eps, ("jumeau", "saboteur", "sur_saboteur"))
    tr = _transcriptions(tok, eps, ed)
    lignes = ed["table"][0]["actions"]
    nb0 = [a["empans"]["jumeau"][0] if a["editable"] else None for a in lignes]
    for m in ("jumeau", "sur_saboteur"):
        nbm = [a["empans"][m][1] if a["editable"] else None for a in lignes]
        ec.exiger_transcriptions_egales_hors_nombre((*tr["saboteur"], nb0), (*tr[m], nbm), m)
        assert tr[m][0] != tr["saboteur"][0]
    ids, emp = tr["jumeau"]
    nbj = [a["empans"]["jumeau"][1] if a["editable"] else None for a in lignes]
    abime = list(ids)
    abime[emp[0][0] + 2] = abime[emp[0][0] + 3]                     # un jeton du titre changé
    with pytest.raises(GardeArret, match="hors des jetons du nombre"):
        ec.exiger_transcriptions_egales_hors_nombre((*tr["saboteur"], nb0), (abime, emp, nbj), "artefact")
    with pytest.raises(GardeArret, match="actions éditées différentes"):
        ec.exiger_transcriptions_egales_hors_nombre((*tr["saboteur"], nb0), (ids, emp, [None] * len(nbj)), "artefact")


# --- troisième tour : nom de carte (point (d)), classes et paliers de la part non éditable (point (a)) ------------------

@pytest.mark.parametrize("champ, comptes", [
    ("150 A100 GPU-hours", ["150"]), ("300 GPU-hours on A100s", ["300"]), ("300 GPU-hours on 8x A100s", ["300"]),
    ("3k A100 GPU-hours", ["3k"]), ("~150 H100-hours", ["150"]),
    # la règle ne joue pas : premier nombre collé (avant ou après), tous comptent
    ("A100: 300 hours", ["100", "300"]), ("120h on 2 A100s", ["120", "2", "100"]), ("8x A100 for 300 hours", ["8", "100", "300"]),
    # un tiret ou une espace sépare : le nombre compte
    ("300 hours (GPT-4)", ["300", "4"]), ("300 hours on 8 GPUs", ["300", "8"]), ("2 kW for 300 hours", ["2", "300"]),
    ("", []), ("about a day", [])])
def test_nom_de_carte_nombres_comptes_a_la_lettre_de_l_erratum(champ, comptes):
    """Erratum 1 au brouillon 5, couple E-1a : « collé » = une lettre touche le nombre, juste avant ou juste après (« A100 »,
    « A100s », « 8x », « 120h ») ; le suffixe « k » lu fait partie du nombre ; un tiret ou une espace sépare ; si le premier
    nombre du champ est collé, la règle ne joue pas et tous comptent."""
    assert [nb.group(0).strip() for nb in ec.nombres_comptes(champ)] == comptes


@pytest.mark.parametrize("cout, jumeau, sur", [("150 A100 GPU-hours", 50.0, 500.0), ("300 GPU-hours on A100s", 100.0, 1000.0),
                                               ("300 GPU-hours on 8x A100s", 100.0, 1000.0),
                                               ("3k A100 GPU-hours", 1000.0, 10000.0)])
def test_nom_de_carte_cas_sains_edites_carte_inchangee_lecteur_gele_non_touche(cout, jumeau, sur):
    """Point (d) : un coût qui nomme une carte est éditable ; seul le premier nombre change, le nom de carte reste tel quel
    chez tous les membres ; le lecteur gelé relit la valeur voulue, et son drapeau « plusieurs nombres » reste levé (il
    n'est pas touché), le même pour tous."""
    for tok in (_tok_caracteres(), _tok_chiffres()):
        texte = _action(cout)
        ids = _ids(tok, texte)
        assert cout_action(texte)["cout_plusieurs_nombres"]
        for m, voulue in (("jumeau", jumeau), ("sur_saboteur", sur)):
            r = ec.editer_action(tok, ids, texte, ec.grille_famille([cout_action(texte)["cout"]]), m)
            assert r["editable"] and r["classe"] is None and r["valeur"] == voulue, (cout, m, r["motif"])
            assert cout_action(r["texte"])["cout"] == voulue and cout_action(r["texte"])["cout_plusieurs_nombres"]
            assert "A100" in r["texte"] and tok.decode(r["ids"], skip_special_tokens=True) == r["texte"]


@pytest.mark.parametrize("cout", ["A100: 300 hours", "120h on 2 A100s", "8x A100 for 300 hours", "300 hours on 8 GPUs",
                                  "300 hours (GPT-4)"])
def test_nom_de_carte_artefacts_non_editables_pour_tous_classe_plusieurs_nombres(cout):
    """Point (d), artefacts : premier nombre collé (la règle ne joue pas ; « A100: 300 hours », où le lecteur gelé lit 100),
    ou un second nombre qui ne touche aucune lettre : non éditable pour tous les membres, classe « plusieurs nombres »."""
    tok = _tok_caracteres()
    texte = _action(cout)
    for m in ("jumeau", "saboteur", "sur_saboteur"):
        r = ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, m)
        assert not r["editable"] and r["classe"] == "plusieurs_nombres" and r["motif"] == "plusieurs nombres", (cout, m)


def test_controle_par_action_le_nom_de_carte_ne_desserre_pas_le_compte_de_l_action_editee():
    """Le contrôle par action relit l'action éditée avec la même règle : un second nombre qui ne touche aucune lettre y est
    refusé (contrôle manqué), même quand le premier a été édité. L'artefact glisse « on 8 » dans l'empan du nombre édité,
    pour que le texte hors du nombre reste égal et que seul ce contrôle refuse."""
    tok = _tok_caracteres()
    texte = _action("150 A100 GPU-hours")
    ed = ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, "jumeau")
    d = texte.index("150")
    assert ec.controler_edition(tok, texte, ed["texte"], ed["ids"], 50.0, d, d + 3, 2) is None
    double = texte[:d] + "50 on 8" + texte[d + 3:]
    assert "plusieurs nombres" in ec.controler_edition(tok, texte, double, _ids(tok, double), 50.0, d, d + 3, 7)


@pytest.mark.parametrize("cout, membre, classe", [
    ("10-20 GPU-hours", "jumeau", "plusieurs_nombres"),
    ("300 to 8x hours", "jumeau", "intervalle"),                      # un seul nombre compté, drapeau « intervalle »
    ("300 x 4h GPU", "jumeau", "multiplication"),                     # un seul nombre compté, drapeau « multiplication »
    ("2k GPU-hours", "jumeau", "suffixe_k"),
    ("about a day", "saboteur", "action_ou_cout_illisible"), ("", "jumeau", "action_ou_cout_illisible")])
def test_classes_des_actions_non_editables(cout, membre, classe):
    """Erratum 1, couple E-2a : six classes ; chaque refus porte la sienne."""
    tok = _tok_caracteres()
    texte = _action(cout)
    r = ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, membre)
    assert not r["editable"] and r["classe"] == classe, (cout, r)
    assert classe in ec.CLASSES_NON_EDITABLE


def test_classes_action_non_valide_et_controle_manque():
    tok = _tok_caracteres()
    texte = "TITLE: x\nCOST: 300 hours"                       # sans ligne ACTION
    assert ec.editer_action(tok, _ids(tok, texte), texte, GRILLE, "jumeau")["classe"] == "action_ou_cout_illisible"
    eps = _episodes([["1,25 hours", "0,4 hours", "300 hours"]], tok)          # forme du sondage S3 : lecteur gelé
    ed = ec.editer_tirage(tok, eps, ("jumeau", "saboteur", "sur_saboteur"))
    assert [a["classe"] for a in ed["table"][0]["actions"]] == [None, "controle_manque", None]


def _tirage_a_part(tok, non_editables: int, total: int):
    """Un tirage de `total` actions, dont `non_editables` à intervalle (non éditables pour tous), les autres « 300 h »."""
    couts = ["10-20 h"] * non_editables + ["300 h"] * (total - non_editables)
    return ec.editer_tirage(tok, _episodes([couts], tok), ("jumeau", "saboteur", "sur_saboteur"))


@pytest.mark.parametrize("non_editables, total, formee, haute", [
    (0, 10, True, False), (1, 10, True, False),                       # 10 % juste : formée, non marquée
    (2, 10, True, True), (3, 12, True, True),                        # au-dessus de 10 %, jusqu'à 25 % juste : marquée
    (4, 12, False, False), (5, 10, False, False)])                   # au-delà de 25 % : non formée (retirage)
def test_deux_paliers_de_la_part_non_editable_marqueur_et_part_par_motif(non_editables, total, formee, haute):
    """Point (a) : part ≤ 25 %, sinon la famille n'est pas formée ; au-dessus de 10 %, formée et marquée « part non
    éditable haute ». La part par motif compte les six classes ; leur somme fait la part."""
    c = ec.controler_famille(_tirage_a_part(_tok_caracteres(), non_editables, total))
    assert c["formee"] is formee and c["part_non_editable_haute"] is haute, c["motifs"]
    assert c["part_non_editable"] == pytest.approx(non_editables / total)
    assert set(c["part_par_motif"]) == set(ec.CLASSES_NON_EDITABLE)
    assert c["part_par_motif"]["plusieurs_nombres"] == pytest.approx(non_editables / total)
    assert sum(c["part_par_motif"].values()) == pytest.approx(c["part_non_editable"])
    if not formee:
        assert any("non éditables" in m and "> 0.25" in m for m in c["motifs"])


def test_ecriture_conventions_et_artefact_valeur_nulle():
    assert ec.ecrire_nombre(12000.0, {"milliers": ",", "decimale": ".", "k": False}) == "12,000"
    assert ec.ecrire_nombre(12000.0, {"milliers": None, "decimale": ".", "k": False}) == "12000"
    assert ec.ecrire_nombre(1500.0, {"milliers": " ", "decimale": ",", "k": False}) == "1 500"
    assert ec.ecrire_nombre(250.0, {"milliers": None, "decimale": ".", "k": True}) == "0.25"
    with pytest.raises(GardeArret):
        ec.ecrire_nombre(0.0, {"milliers": None, "decimale": ".", "k": False})
    assert math.isclose(ec.CIBLE_LOG10, math.log10(3), abs_tol=1e-3)
