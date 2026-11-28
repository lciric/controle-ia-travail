"""Plan B des juges (T0.5) : messages RS1 (système H.3, utilisateur RS1 puis le corps de b0), adaptateur de notation
pour `jouer_episodes` (RS1 et H.4), contrôle du format sous RS1 ; équivalence de chemin avec `noter_ensembles` sur le
modèle jouet, lot pour lot. Chaque garde sur un cas sain et sur un artefact (R5)."""
from __future__ import annotations

import shutil

import pytest
import torch

from controle_ia.environnements import juges
from controle_ia.environnements import juges_simplifies as js
from controle_ia.environnements import rubrique_simplifiee as rs
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.juges import messages_juge_ensemble
from controle_ia.environnements.pilote_a import CLES_RAPPORT_GARDEES, noter_ensembles
from controle_ia.gardes import GardeArret
from controle_ia.harnais.episode import Action, Episode, Transcription, generer_lot
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import modele_jouet, regler_determinisme, tokeniseur_caracteres_chat
from controle_ia.scellement import sceller
from test_harnais_formats import GABARIT_DEPLACE

regler_determinisme(1)
TOK = tokeniseur_caracteres_chat()
FIN = TOK.convert_tokens_to_ids("<|im_end|>")
FMT = FormatChat(TOK, fins={FIN, TOK.eos_token_id})
CLASSIFICATION = "Paper type: Mostly experiments\nData type: Real data only\nExperimental domains: none specified"
DEMANDES = [{"cle": "juge-x/2506.00001v1/e0/passe-0", "questions": "Why do routers matter?",
             "ensemble": "PROPOSAL 1: Router ablation\nCompare top-1 and top-2 routing.",
             "classification": CLASSIFICATION},
            {"cle": "juge-x/2506.00002v1/e0/passe-0", "questions": "How to calibrate?",
             "ensemble": "PROPOSAL 1: Temperature scaling on a held-out split", "classification": None},
            {"cle": "juge-x/2506.00002v1/e1/passe-0", "questions": "How to calibrate?",
             "ensemble": "PROPOSAL 1: Ensembles\nPROPOSAL 2: Isotonic regression with five seeds",
             "classification": None}]
GRAINES = {d["cle"]: 1000 + k for k, d in enumerate(DEMANDES)}
# H.4 courte, à la place de l'invite réelle, pour les seuls tests qui génèrent (coût : environ 20 000 jetons par
# contexte avec le tokeniseur par caractères) ; le contexte avec H.4 réelle est éprouvé à part, jeton pour jeton
H4_COURTE = "## Scoring Rubric\nSPECIFICITY: <score>\nCOHERENCE: <score>\n"


def h4_courte(monkeypatch) -> None:
    vrai = juges.charger_invite
    monkeypatch.setattr(juges, "charger_invite",
                        lambda ident, *a, **k: H4_COURTE if ident == "H4" else vrai(ident, *a, **k))


def modele_qui_s_arrete(graine: int = 5, bonus: float = 2.5):
    """Modèle jouet dont le logit du jeton de fin de tour est relevé (crochet sur la tête de sortie, tests seulement) :
    des réponses s'arrêtent avant le plafond, d'autres non ; la troncature et le remplissage des lignes finies
    s'éprouvent ainsi."""
    m = modele_jouet(graine, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)

    def relever(module, entrees, sortie):
        sortie = sortie.clone()
        sortie[..., FIN] += bonus
        return sortie

    m.lm_head.register_forward_hook(relever)
    return m


# --- messages RS1 -----------------------------------------------------------------------------------------------

@pytest.mark.parametrize("classification", [CLASSIFICATION, None])
def test_messages_rs1_assemblage(classification):
    """Système = H.3 de b0 ; utilisateur = RS1 sans espaces de bord, deux fins de ligne, puis le corps de b0, à
    l'octet."""
    msgs, crit = js.messages_juge_rs1("Why?", "PROPOSAL 1: x", classification)
    b0, _ = messages_juge_ensemble("Why?", "PROPOSAL 1: x", "b0", classification)
    h4, rs1 = charger_invite("H4").strip(), rs.charger_invite_rs1().strip()
    assert msgs[0] == b0[0] == {"role": "system", "content": charger_invite("H3").strip()}
    assert b0[1]["content"].startswith(h4 + "\n\n")
    corps = b0[1]["content"][len(h4) + 2:]
    assert corps.startswith("## Research Questions\n\nWhy?") and corps.endswith("## Proposals\n\nPROPOSAL 1: x\n")
    assert ("## Paper Classification (verified metadata)" in corps) == (classification is not None)
    assert msgs[1] == {"role": "user", "content": rs1 + "\n\n" + corps}
    assert crit == rs.CRITERES_RS1


def test_messages_rs1_artefacts(tmp_path):
    with pytest.raises(GardeArret, match="rien à juger"):
        js.messages_juge_rs1("  ", "PROPOSAL 1: x")
    with pytest.raises(GardeArret, match="inconnue de l'adaptateur"):
        js.messages_de_la_variante(DEMANDES[0], "b*")
    d = tmp_path / "invites-plan-b"
    shutil.copytree(rs.RACINE_INVITES_RS1, d)
    f = d / "invites" / "RS1.txt"
    f.write_text(f.read_text().replace("whole number", "integer"))            # invite altérée : le sceau ne tient plus
    with pytest.raises(GardeArret):
        js.messages_juge_rs1("Why?", "PROPOSAL 1: x", None, racine=d)
    (d / "invites" / "RS1.txt.sha256").unlink()
    sceller(f)                                                                  # rescellée : l'index la refuse
    with pytest.raises(GardeArret, match="≠ index"):
        js.messages_juge_rs1("Why?", "PROPOSAL 1: x", None, racine=d)


# --- adaptateur ----------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("variante", ["RS1", "b0"])
def test_adaptateur_consigne_et_observation(variante):
    env = js.EnvironnementNotation(DEMANDES[0], variante)
    msgs, crit = js.messages_de_la_variante(DEMANDES[0], variante)
    assert env.consigne_privee(0) == msgs[0]["content"] and env.observation(0, 0, []) == msgs[1]["content"]
    assert env.criteres == crit
    for appel in (lambda: env.consigne_privee(1), lambda: env.observation(1, 0, []), lambda: env.observation(0, 1, []),
                  lambda: env.observation(0, 0, [(0, 0, "x")])):
        with pytest.raises(GardeArret, match="N = "):
            appel()


def test_contextes_de_l_adaptateur_h4_egaux_a_noter_ensembles():
    """Avec H.4 (invite réelle), le contexte que `jouer_episodes` construit au pas 0 (ouverture de la consigne et de
    l'observation) est, jeton pour jeton, celui de `noter_ensembles`."""
    for d in DEMANDES:
        env = js.EnvironnementNotation(d, "b0")
        msgs, _ = messages_juge_ensemble(d["questions"], d["ensemble"], "b0", d["classification"])
        assert FMT.ouverture(env.consigne_privee(0), env.observation(0, 0, [])) == \
            FMT.ouverture(msgs[0]["content"], msgs[1]["content"])


def test_equivalence_de_chemin_h4_lot_pour_lot(monkeypatch):
    """Sur le modèle jouet, la notation par `jouer_episodes` et l'adaptateur H.4 (b0) rend, lot pour lot, exactement
    les champs de `noter_ensembles` (clé, variante, jetons de contexte, empreinte de l'ensemble, jetons et drapeau
    « tronquée », notes, anomalies, score, réponse). Lots de 2 puis de 1 : remplissage à gauche, ligne finie avant les
    autres et réponse tronquée éprouvés. H.4 courte (coût) ; le contexte avec H.4 réelle : test précédent."""
    h4_courte(monkeypatch)
    m = modele_qui_s_arrete()
    demandes = [dict(d, variante="b0") for d in DEMANDES]
    attendu = noter_ensembles(m, FMT, demandes, GRAINES, 2, 10, 1.0)
    obtenu = js.noter_par_episodes(m, FMT, demandes, GRAINES, 2, 10, 1.0, [0, 1, 2], "b0")
    assert obtenu == attendu
    assert {x["tronquee"] for x in attendu} == {True, False}                 # les deux cas sont éprouvés
    assert len({x["jetons_contexte"] for x in attendu}) == 3
    # artefact : une autre graine change la réponse ; l'égalité n'est pas acquise d'avance
    autre = js.noter_par_episodes(m, FMT, demandes[:1], {demandes[0]["cle"]: 1}, 2, 10, 1.0, [0, 1, 2], "b0")
    assert autre[0]["reponse"] != attendu[0]["reponse"]


def test_equivalence_de_chemin_rs1_et_lecture():
    """Sous RS1, mêmes jetons que `generer_lot` sur les contextes RS1 (référence écrite à part, lot pour lot), et
    lecture par `lire_reponse_rs1` avec la règle de troncature."""
    m = modele_qui_s_arrete()
    lignes = js.jouer_lot_de_notations(m, FMT, DEMANDES[:2], GRAINES, "RS1", [0, 1, 2], 10, 1.0, 0.2, "q99")
    contextes = [FMT.ouverture(*[x["content"] for x in js.messages_juge_rs1(d["questions"], d["ensemble"],
                                                                             d["classification"])[0]])
                 for d in DEMANDES[:2]]
    pad = TOK.pad_token_id
    nouveaux, _ = generer_lot(m, contextes, 10, 1.0, [GRAINES[d["cle"]] for d in DEMANDES[:2]], FMT.fins, pad)
    for x, ctx, nv, d in zip(lignes, contextes, nouveaux, DEMANDES[:2]):
        n = x["notation"]
        assert n["jetons_contexte"] == len(ctx) and n["jetons_reponse"] == len(nv)
        assert n["reponse"] == TOK.decode(nv, skip_special_tokens=True)
        tronquee = not (nv and nv[-1] in FMT.fins)
        lu = rs.lire_reponse_rs1(n["reponse"], tronquee)
        assert (n["tronquee"], n["notes"], n["anomalies"], n["score"]) == (tronquee, lu["notes"], lu["anomalies"],
                                                                           lu["score"])
        assert n["lecture_rs1"] == lu["lecture"] and n["variante"] == "RS1" and n["cle"] == d["cle"]
        # garde en ligne : toutes les rangées gardées, rapport complet
        assert set(x["rapport"]) == {"tolerance", "statistique", *CLES_RAPPORT_GARDEES}
        assert x["rapport"]["statistique"] == "q99" and x["rapport"]["longueurs_contexte"] == len(ctx)
        assert "passe" not in x and "transcription" not in x                  # aucune activation ne sort


def test_notation_et_rapport_artefacts():
    ep = Episode("e", 1, 1, [Transcription(0, [1, 2, 3], [Action(0, 0, 2, 3, [3], "x"), Action(0, 1, 3, 3, [], "")])])
    with pytest.raises(GardeArret, match="une seule action"):
        js.notation_de_l_episode(DEMANDES[0], "RS1", rs.CRITERES_RS1, ep, FMT.fins)
    ep1 = Episode("e", 1, 1, [Transcription(0, [1, 2, 3], [Action(0, 0, 2, 3, [FIN], "")])])
    with pytest.raises(GardeArret, match="critères RS1"):
        js.notation_de_l_episode(DEMANDES[0], "RS1", (("X", 0, 5),), ep1, FMT.fins)
    sain = js.notation_de_l_episode(DEMANDES[0], "RS1", rs.CRITERES_RS1, ep1, FMT.fins)          # cas sain
    assert sain["tronquee"] is False and sain["score"] is None and sain["jetons_contexte"] == 2
    with pytest.raises(GardeArret, match="sans l'action 0,0"):
        js.rapport_de_la_rangee({"episode": "e", "tolerance": 0.2, "statistique": "q99", "ecarts": {}})
    with pytest.raises(GardeArret, match="graines absentes"):
        js.jouer_lot_de_notations(None, FMT, DEMANDES[:1], {}, "RS1", [0], 4, 1.0, 0.2, "q99")
    with pytest.raises(GardeArret, match="vide"):
        js.jouer_lot_de_notations(None, FMT, [], {}, "RS1", [0], 4, 1.0, 0.2, "q99")


# --- format sous RS1 -----------------------------------------------------------------------------------------------

def test_format_rs1_cas_sain_et_artefacts():
    sain = js.controler_format_rs1(FMT, {"nom": "jouet-3B"}, "jouet")
    assert sain["verifie"] is True and sain["tours"] == 1 and sain["variante"] == "RS1"
    consigne, obs, rep = js.conversation_de_controle_rs1()
    assert obs[0].startswith(rs.charger_invite_rs1().strip() + "\n\n## Research Questions")
    assert rep == ["SPECIFICITY: 3\nCOVERAGE: 3"]
    with pytest.raises(GardeArret, match="texte attendu"):                     # mode réel sans texte attendu
        js.controler_format_rs1(FMT, {"nom": "3B"}, "reel")
    with pytest.raises(GardeArret, match="ouverture sans"):                    # texte attendu absent de l'ouverture
        js.controler_format_rs1(FMT, {"nom": "3B", "texte_attendu_ouverture": "Today Date: 26 Jul 2024"}, "jouet")
    tok = tokeniseur_caracteres_chat()
    tok.chat_template = GABARIT_DEPLACE                                         # gabarit qui réécrit le passé
    with pytest.raises(GardeArret, match="ne prolonge pas"):
        js.controler_format_rs1(FormatChat(tok, fins=FMT.fins), {"nom": "3B"}, "jouet")

    class FormatFautif(FormatChat):
        def cloture(self, debut, action):                                     # clôture amputée d'un jeton
            return super().cloture(debut, action)[:-1]

    with pytest.raises(GardeArret, match="format incrémental"):
        js.controler_format_rs1(FormatFautif(TOK, fins=FMT.fins), {"nom": "3B"}, "jouet")


def test_aucun_appel_direct_de_generer_lot():
    """L'adaptateur n'appelle `generer_lot` qu'à travers `jouer_episodes` (texte du module lu comme code)."""
    import ast
    import inspect

    arbre = ast.parse(inspect.getsource(js))
    appels = {n.func.id if isinstance(n.func, ast.Name) else getattr(n.func, "attr", None)
              for n in ast.walk(arbre) if isinstance(n, ast.Call)}
    assert "jouer_episodes" in appels and "generer_lot" not in appels and "generate" not in appels


def test_modele_qui_s_arrete_est_un_artefact_de_test_seulement():
    """Le crochet du test relève le seul logit de fin ; sans lui, le modèle jouet est celui du harnais."""
    a = modele_jouet(5, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    b = modele_qui_s_arrete()
    x = torch.tensor([[1, 5, 9]])
    with torch.no_grad():
        la, lb = a(x).logits, b(x).logits
    ecart = lb - la
    assert torch.allclose(ecart[..., FIN], torch.full_like(ecart[..., FIN], 2.5))
    ecart[..., FIN] = 0
    assert torch.count_nonzero(ecart) == 0
