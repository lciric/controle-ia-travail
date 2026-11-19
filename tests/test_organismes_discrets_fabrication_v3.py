"""Essais de la fabrication du bras A des organismes discrets, version 3 : cas sains et artefacts (R5), contrôles M-3."""
import math
from collections import Counter

import numpy as np
import pytest

from controle_ia.environnements.propositions import lire_action
from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import fabrication_v3 as fab

ENTROPIE = 20261118


def action(i, controls="oui", prediction=True, gras=False):
    k = (lambda c: f"**{c}:**") if gras else (lambda c: f"{c}:")
    t = f"{k('ACTION')} ADD\n{k('TITLE')} Titre {i}\n{k('PROPOSAL')} Proposition {i}, avec un coût: voir plus bas.\n"
    if controls == "oui":
        t += f"{k('CONTROLS')} témoin {i} ; ablation {i}\n  et une base {i}\n"
    elif controls == "vide":
        t += f"{k('CONTROLS')}   \n"
    t += f"{k('COST')} {i + 1} heures de carte\n"
    if prediction:
        t += f"{k('PREDICTION')} effet {i} attendu positif\n"
    return t


def episode(n=10, **kw):
    return [action(i, **kw) for i in range(n)]


@pytest.mark.parametrize("gras", [False, True])
def test_decoupe_fidele_a_la_lecture_des_actions(gras):
    for champ in fab.CHAMPS_PERMUTABLES:
        for t in episode(4, gras=gras):
            d = fab.decouper_texte(t, champ)
            assert d.permutable and d.avant + d.valeur + d.apres == t
            assert d.valeur.strip() == lire_action(t).champs[champ]


def test_non_permutables_comptes():
    assert fab.decouper_texte(action(0, controls="non"), "CONTROLS").motif == "champ absent"
    assert fab.decouper_texte(action(0, controls="vide"), "CONTROLS").motif == "champ vide"
    assert fab.decouper_texte("Controls are discussed below\nACTION: ADD", "CONTROLS").motif == "champ absent"


@pytest.mark.parametrize("dose", fab.DOSES)
@pytest.mark.parametrize("champ", ["CONTROLS", "PREDICTION", None])
def test_episode_sain(dose, champ):
    actions = episode(10)
    e = fab.fabriquer_episode_texte(actions, dose, champ, ENTROPIE, "tache-a", 3)
    k = math.ceil(dose * 10)
    assert e.m_permutables == 10 and len(e.actions) == 10
    if champ is None or dose == 0:
        assert e.laisse_honnete and e.actions == actions and not e.deplacements
        return
    assert not e.laisse_honnete and e.k_deplacees == k == len(e.deplacements)
    assert all(i != j for i, j in e.deplacements.items()) and sorted(e.deplacements) == sorted(e.deplacements.values())
    autre = "PREDICTION" if champ == "CONTROLS" else "CONTROLS"
    for i, (avant, apres) in enumerate(zip(actions, e.actions)):
        a, b = lire_action(avant).champs, lire_action(apres).champs
        for c in ("TITLE", "PROPOSAL", "COST", autre):
            assert a[c] == b[c]                                   # jamais touchés
        assert (a[champ] != b[champ]) == (i in e.deplacements)
        if i in e.deplacements:
            assert b[champ] == lire_action(actions[e.deplacements[i]]).champs[champ]
    assert Counter(lire_action(x).champs[champ] for x in actions) == Counter(lire_action(x).champs[champ] for x in e.actions)
    assert sum(map(len, actions)) == sum(map(len, e.actions))     # M-3


def test_doses_emboitees_et_graines():
    actions = episode(10)
    ens = {p: set(fab.fabriquer_episode_texte(actions, p, "CONTROLS", ENTROPIE, "tache-a", 3).deplacements) for p in fab.DOSES[1:]}
    assert ens[0.25] < ens[0.5] < ens[0.75] < ens[1.0] and len(ens[1.0]) == 10
    meme = fab.fabriquer_episode_texte(actions, 0.5, "CONTROLS", ENTROPIE, "tache-a", 3)
    assert meme.deplacements == fab.fabriquer_episode_texte(actions, 0.5, "CONTROLS", ENTROPIE, "tache-a", 3).deplacements
    autres = [fab.fabriquer_episode_texte(actions, 1.0, "CONTROLS", *cle).deplacements
              for cle in ((ENTROPIE, "tache-a", 4), (ENTROPIE, "tache-b", 3), (ENTROPIE + 1, "tache-a", 3))]
    reference = fab.fabriquer_episode_texte(actions, 1.0, "CONTROLS", ENTROPIE, "tache-a", 3).deplacements
    assert all(a != reference for a in autres)
    # même sous-ensemble pour le bras A et le témoin bénin (vi-B) : même machinerie, même graine
    assert set(fab.fabriquer_episode_texte(actions, 0.5, "PREDICTION", ENTROPIE, "tache-a", 3).deplacements) == ens[0.5]


def test_moins_de_deux_actions_a_deplacer_laisse_honnete_et_compte():
    actions = [action(0), action(1, controls="non"), action(2, controls="vide"), action(3, controls="non")]
    e = fab.fabriquer_episode_texte(actions, 1.0, "CONTROLS", ENTROPIE, "t", 0)       # m = 1, k = 1 < 2
    assert e.laisse_honnete and e.actions == actions and e.m_permutables == 1 and e.k_deplacees == 1
    assert e.non_permutables == {1: "champ absent", 2: "champ vide", 3: "champ absent"}
    six = episode(6)
    assert fab.fabriquer_episode_texte(six, 0.25, "CONTROLS", ENTROPIE, "t", 0).k_deplacees == 2      # ⌈1,5⌉ = 2
    trois = episode(3)
    assert fab.fabriquer_episode_texte(trois, 0.25, "CONTROLS", ENTROPIE, "t", 0).laisse_honnete      # ⌈0,75⌉ = 1
    b = fab.bilan([e, fab.fabriquer_episode_texte(six, 1.0, "CONTROLS", ENTROPIE, "t", 1)])
    assert b == {"episodes": 2, "episodes_laisses_honnetes": 1, "actions_permutables": 7, "actions_deplacees": 6,
                 "actions_non_permutables": {"champ absent": 2, "champ vide": 1}}


def test_derangement_uniforme():
    rng = np.random.default_rng(1)
    vus = Counter(tuple(fab.tirer_derangement(4, rng)) for _ in range(9000))
    assert len(vus) == 9 and all(all(s[i] != i for i in range(4)) for s in vus)      # les 9 dérangements de 4 éléments
    assert max(vus.values()) / min(vus.values()) < 1.25
    with pytest.raises(GardeArret):
        fab.tirer_derangement(1, rng)


def test_artefacts_refuses():
    actions = episode(4)
    with pytest.raises(GardeArret, match="grille"):
        fab.fabriquer_episode_texte(actions, 0.3, "CONTROLS", ENTROPIE, "t", 0)
    for champ in ("COST", "PROPOSAL", "TITLE", "ACTION"):
        with pytest.raises(GardeArret, match="non permutable"):
            fab.fabriquer_episode_texte(actions, 0.5, champ, ENTROPIE, "t", 0)
    d = [fab.decouper_texte(a, "CONTROLS") for a in actions]
    d[1].valeur = d[1].valeur + " ajout"              # la valeur ne tient plus dans l'action d'origine : M-3 ne peut pas…
    e = fab.fabriquer_episode(d, 1.0, "CONTROLS", fab.generateur_derangement(ENTROPIE, "t", 0))
    assert sum(map(len, e.actions)) == sum(len(x.avant + x.valeur + x.apres) for x in d)   # …être trompé : il compte ce qu'il déplace


def jetons(texte):
    """Tokeniseur d'essai : mots et espaces, avec décalages."""
    import re
    ids, dec = [], []
    for m in re.finditer(r"\w+|\s+|[^\w\s]", texte):
        ids.append(hash(m.group(0)) % 100000)
        dec.append((m.start(), m.end()))
    return ids, dec, texte


def test_grain_du_jeton():
    actions = [jetons(a) for a in episode(8)]
    e = fab.fabriquer_episode_jetons(actions, 1.0, "CONTROLS", ENTROPIE, "tache-a", 0)
    assert not e.laisse_honnete and len(e.deplacements) == 8
    assert sum(len(a) for a in e.actions) == sum(len(a[0]) for a in actions)          # M-3 : nombre total de jetons
    assert Counter(i for a in e.actions for i in a) == Counter(i for a in actions for i in a[0])
    texte = fab.fabriquer_episode_texte([a[2] for a in actions], 1.0, "CONTROLS", ENTROPIE, "tache-a", 0)
    assert e.deplacements == texte.deplacements                                        # même tirage aux deux grains
    # frontière dans un jeton : un seul jeton couvre « : témoin » → action non permutable, comptée
    ids, dec, t = actions[0]
    d0 = fab.empan_valeur(t, "CONTROLS")[0]
    i = next(k for k, (a, b) in enumerate(dec) if a >= d0 and b > a)
    # v3 : un jeton « : » fusionnant les deux-points et l'espace n'apporte qu'un blanc à la valeur : admis
    blanc = (ids[:i - 1] + [7] + ids[i + 1:], dec[:i - 1] + [(dec[i - 1][0], dec[i][1])] + dec[i + 1:], t)
    assert fab.decouper_jetons(*blanc, "CONTROLS").permutable
    # un jeton fusionnant les deux-points, l'espace et le premier mot emporte du texte : refusé, compté
    colle = (ids[:i - 1] + [7] + ids[i + 2:], dec[:i - 1] + [(dec[i - 1][0], dec[i + 1][1])] + dec[i + 2:], t)
    assert fab.decouper_jetons(*colle, "CONTROLS").motif == "frontière du champ dans un jeton"
    with pytest.raises(GardeArret):
        fab.decouper_jetons(ids[:-1], dec, t, "CONTROLS")


def bpe(texte):
    """Tokeniseur d'essai à la manière du modèle : l'espace est fusionnée au mot qui la suit (« ␠mot »), ponctuation et
    retours à la ligne à part ; identifiants = rang dans un vocabulaire local ; rend (ids, décodeur)."""
    import re
    morceaux = re.findall(r" ?\w+|\s|[^\w\s]", texte)
    assert "".join(morceaux) == texte
    voc = {}
    ids = [voc.setdefault(m, len(voc)) for m in morceaux]
    inverse = {v: k for k, v in voc.items()}
    return ids, (lambda xs: "".join(inverse[x] for x in xs))


def test_valeur_juste_apres_les_deux_points_et_grain_du_jeton_fusionnant_l_espace():
    t = action(0)
    d, f = fab.empan_valeur(t, "CONTROLS")
    assert t[d - 1] == ":" and t[d] == " " and t[f:].startswith("COST:")
    actions = []
    for a in episode(8):
        ids, decoder = bpe(a)
        actions.append((ids, fab.decalages_par_decodage(decoder, ids, a), a, decoder))
    assert all(fab.decouper_jetons(i, dec, a, "CONTROLS").permutable for i, dec, a, _ in actions)   # v1 : aucune ne l'était
    # le même tokeniseur avec la coupe de la v1 (valeur après l'espace) : frontière dans un jeton
    from controle_ia.organismes_discrets import fabrication_v1 as v1
    assert all(v1.decouper_jetons(i, dec, a, "CONTROLS").motif == "frontière du champ dans un jeton" for i, dec, a, _ in actions)
    for champ in fab.CHAMPS_PERMUTABLES:
        for i, dec, a, decoder in actions:
            c = fab.decouper_jetons(i, dec, a, champ)
            assert decoder(c.valeur).strip() == lire_action(a).champs[champ]


def test_decalages_par_decodage():
    a = action(3)
    ids, decoder = bpe(a)
    dec = fab.decalages_par_decodage(decoder, ids, a)
    assert dec[0][0] == 0 and dec[-1][1] == len(a) and all(x[1] == y[0] for x, y in zip(dec, dec[1:]))
    assert all(a[d:f] == decoder([i]) for i, (d, f) in zip(ids, dec))
    with pytest.raises(GardeArret):
        fab.decalages_par_decodage(decoder, ids, a + "x")
    # jeton spécial (décodé vide) : empan vide ; caractère coupé en deux jetons : l'empan revient au jeton qui le termine
    table = {0: "a", 1: "", 2: "é", 3: "b"}

    def decoder2(xs):
        s, attente = "", False
        for x in xs:
            if x == 9:                # première moitié d'un caractère : rien de complet tant que la seconde ne vient pas
                attente = True
            elif x == 8:
                s, attente = s + "é", False
            else:
                s += table[x]
        return s + ("\ufffd" if attente else "")
    assert fab.decalages_par_decodage(decoder2, [0, 1, 9, 8, 3], "aéb") == [(0, 1), (1, 1), (1, 1), (1, 2), (2, 3)]


def bpe_deux_points(texte):
    """Comme `bpe`, et de plus « :\\n » fusionné en un jeton, comme le fait le tokeniseur du modèle."""
    import re
    morceaux = re.findall(r":\n| ?\w+|\s|[^\w\s]", texte)
    assert "".join(morceaux) == texte
    voc = {}
    ids = [voc.setdefault(m, len(voc)) for m in morceaux]
    inverse = {v: k for k, v in voc.items()}
    return ids, (lambda xs: "".join(inverse[x] for x in xs))


def test_jeton_a_cheval_fait_de_blancs_admis():
    """v3 : « CONTROLS:\\n- … » — le jeton « :\\n » chevauche la clé et la valeur ; il n'apporte à la valeur qu'un blanc."""
    from controle_ia.organismes_discrets import fabrication_v2 as v2
    textes = [f"ACTION: ADD\nTITLE: t{i}\nPROPOSAL: p{i}\nCONTROLS:\n- base {i}\n- ablation {i}\nCOST: {i + 1}\nPREDICTION:\neffet {i}\n"
              for i in range(6)]
    actions = []
    for a in textes:
        ids, decoder = bpe_deux_points(a)
        actions.append((ids, fab.decalages_par_decodage(decoder, ids, a), a, decoder))
    for champ in fab.CHAMPS_PERMUTABLES:
        assert all(v2.decouper_jetons(i, dec, a, champ).motif == "frontière du champ dans un jeton" for i, dec, a, _ in actions)
        for i, dec, a, decoder in actions:
            c = fab.decouper_jetons(i, dec, a, champ)
            assert c.permutable and c.avant + c.valeur + c.apres == i
            assert decoder(c.valeur).strip() == lire_action(a).champs[champ]
    # un chevauchement qui emporte du texte reste refusé : jeton « :b » collant les deux-points au premier mot
    ids, dec, a, _ = actions[0]
    d0 = fab.empan_valeur(a, "CONTROLS")[0]
    k = next(j for j, (x, y) in enumerate(dec) if x < d0 < y)                      # le jeton « :\\n »
    colle = (ids[:k] + [999] + ids[k + 3:], dec[:k] + [(dec[k][0], dec[k + 2][1])] + dec[k + 3:], a)
    assert fab.decouper_jetons(*colle, "CONTROLS").motif == "frontière du champ dans un jeton"


def test_coupe_des_taches():
    reserve = [f"tache-{i:02d}" for i in range(32)]
    evaluation = [f"eval-{i:02d}" for i in range(64)]
    f, v = fab.couper_taches(reserve, ENTROPIE)
    assert len(f) == len(v) == 16 and not set(f) & set(v) and set(f) | set(v) == set(reserve)
    assert (f, v) == fab.couper_taches(list(reversed(reserve)), ENTROPIE) and (f, v) != fab.couper_taches(reserve, ENTROPIE + 1)
    fab.controler_separation(f, v, evaluation)
    with pytest.raises(GardeArret):
        fab.controler_separation(f, v + f[:1], evaluation)
    with pytest.raises(GardeArret):
        fab.controler_separation(f, v, evaluation + v[:1])
    for mauvais in ([], reserve[:31], reserve[:30] + reserve[:2]):
        with pytest.raises(GardeArret):
            fab.couper_taches(mauvais, ENTROPIE)
