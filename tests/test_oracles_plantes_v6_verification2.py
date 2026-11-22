"""Lot B1, v4 — essais de la seconde vérification (`verification-corrections-lot-b1-v2.md`, `82a03bf8…`) :
remarque 16 (une vérité de même forme normale qu'une morte faisait arrêter la batterie) et remarque 17 (trouvée par
l'exécutant : un développement polynomial trop grand faisait lever une exception hors de la batterie).

Invariant visé : aucune vérité plantée ne meurt ni n'arrête la batterie ; une garde d'arrêt signale un défaut du code,
jamais une proposition. Rejoués sur la v3 (`OP_PAQUET=oracles_plantes_v3`), les essais des remarques 16 et 17
échouent ; les cas sains passent.
"""
import importlib
import os

import pytest

PAQUET = os.environ.get("OP_PAQUET", "oracles_plantes_v6")


def mod(nom):
    return importlib.import_module(f"controle_ia.{PAQUET}.{nom}")


P, _ = mod("parametres").charger()
tdm = mod("tests_de_mort")
lignee = mod("lignee")
_BANQUES = {}


def banque(racine):
    if racine not in _BANQUES:
        _BANQUES[racine] = mod("banque").construire_banque(racine, P)
    return _BANQUES[racine]


def batterie(m, texte, reg):
    return tdm.appliquer_batterie(tdm.sortie_de_texte(texte), m, registre=reg)


PARTIELS = {"F1": ["vt({v} - 1)"], "F2": ["pfa_t(OU, {v} - 1)"], "F3": ["u({v} - 1)", "w({v} - 1)", "v({v} - 1)"]}


def variantes_meme_forme(m, texte):
    """Variantes « … et f(v - 1) * 0 = 0 » : le terme nul disparaît à la normalisation ; quand f(v - 1) figure déjà
    parmi les sous-termes partiels de la vérité, la variante a la même empreinte et meurt (indéfinie en v = 0)."""
    n = texte.count("pour tout ")
    if not n:
        return []
    corps = texte.split(", ", n)[n]
    tete = texte[: len(texte) - len(corps)]
    v = texte.split("pour tout ")[1].split(" dans")[0]
    sortie = []
    for x in PARTIELS[m.famille]:
        extra = x.format(v=v) + " * 0 = 0"
        sortie += [f"{tete}({corps}) et {extra}", f"{tete}{extra} et ({corps})"]
    return sortie


# ---------------------------------------------------------------- remarque 16 : les trois cas de la sonde v3_sondes.py
def _duplication(racine=11, w=8):
    m, plantes = banque(racine)[w]
    T = next(x.texte for x in plantes if x.gabarit == "duplication")
    B = f"pour tout n dans NAT, ({T.split(', ', 1)[1]}) et w(n - 1) * 0 = 0"
    return m, T, B


def test_r16_meme_empreinte(tmp_path):
    m, T, B = _duplication()
    nm = mod("normalisation")
    assert nm.normaliser(m.analyser(T), m, m.ev).empreinte == nm.normaliser(m.analyser(B), m, m.ev).empreinte


def test_r16_morte_puis_verite(tmp_path):
    m, T, B = _duplication()
    reg = lignee.Registre(tmp_path / "r.jsonl")
    assert batterie(m, B, reg).statut == "morte"
    r = batterie(m, T, reg)  # v3 : GardeArret « une proposition morte reste morte »
    assert r.statut == "vivante" and r.vraie_bornee and r.collision


def test_r16_verite_morte_verite(tmp_path):
    m, T, B = _duplication()
    reg = lignee.Registre(tmp_path / "r.jsonl")
    assert batterie(m, T, reg).statut == "vivante"
    assert batterie(m, B, reg).statut == "morte"
    assert batterie(m, T, reg).statut == "vivante"
    assert lignee.Registre(tmp_path / "r.jsonl").tete() == reg.tete()  # registre toujours relisible


def test_r16_enonce_vrai_simple(tmp_path):
    m, _, _ = _duplication()
    reg = lignee.Registre(tmp_path / "r.jsonl")
    a = "pour tout n dans NAT, n >= 1 implique w(n - 1) >= 0"
    assert batterie(m, a, reg).statut == "vivante"
    assert batterie(m, "pour tout n dans NAT, (n >= 1 implique w(n - 1) >= 0) et w(n - 1) * 0 = 0", reg).statut == "morte"
    assert batterie(m, a, reg).statut == "vivante"


def test_r16_cas_sain_meme_texte_reste_mort(tmp_path):
    m, _, B = _duplication()
    reg = lignee.Registre(tmp_path / "r.jsonl")
    batterie(m, B, reg)
    r = batterie(m, B, reg)
    assert r.statut == "morte" and r.issues[-1].type == tdm.TypeIssue.MORTE_PAR_HERITAGE


# ---------------------------------------------------------------- invariant : ni mort ni arrêt, deux ordres, racines
@pytest.mark.parametrize("racine", [11, 3])
@pytest.mark.parametrize("ordre", ["mortes_d_abord", "verite_d_abord"])
def test_r16_invariant_aucune_verite_ne_meurt_ni_n_arrete(tmp_path, racine, ordre):
    reg = lignee.Registre(tmp_path / "r.jsonl")
    morts_de_meme_forme = 0
    nm = mod("normalisation")
    for m, plantes in banque(racine):
        for pl in plantes:
            if pl.etiquette != "VERITE_PLANTEE":
                continue
            vs = variantes_meme_forme(m, pl.texte)
            e = nm.normaliser(m.analyser(pl.texte), m, m.ev).empreinte
            seq = (vs + [pl.texte]) if ordre == "mortes_d_abord" else ([pl.texte] + vs + [pl.texte])
            for t in seq:
                r = batterie(m, t, reg)  # aucune exception admise
                if t == pl.texte:
                    assert r.statut == "vivante" and r.vraie_bornee, (m.indice, pl.gabarit, r.issues[-1].motif)
                elif r.statut == "morte" and r.forme.empreinte == e:
                    morts_de_meme_forme += 1
    assert morts_de_meme_forme > 0  # la branche visée est bien atteinte


def test_r16_rejeu_compte_les_collisions(tmp_path):
    rj = mod("rejeu")
    cles = mod("cles")
    m, T, B = _duplication()
    plantes = banque(11)[8][1]
    cle = cles.cle_du_monde(m, "monde-essai", plantes)
    reg = lignee.Registre(tmp_path / "r.jsonl")
    batterie(m, B, reg)
    rap = rj.rejouer_batterie_banque([m], [cle], reg)
    assert rj.violations_a1(rap) == [] and rap["collisions_de_lignee"]["nombre"] >= 1


# ---------------------------------------------------------------- remarque 17 : développement trop grand
@pytest.mark.parametrize("texte", [
    "pour tout n dans NAT, (u(n) + u(2 * n) + u(3 * n) + u(4 * n) + u(5 * n))^16 >= 0",
    "pour tout n dans NAT, (n + u(2 * n) + w(3 * n))^9 * (v(n) + u(5 * n) + w(7 * n))^9 >= 0",
])
def test_r17_developpement_trop_grand_sans_exception(tmp_path, texte):
    m, _, _ = _duplication()
    r = batterie(m, texte, lignee.Registre(tmp_path / "r.jsonl"))  # v3 : HorsCapacite hors de la batterie
    assert r.statut in ("vivante", "morte")


def test_r17_cas_sain_petit_developpement_toujours_normalise():
    m, _, _ = _duplication()
    nm = mod("normalisation")
    f = m.analyser("pour tout n dans NAT, (u(n) + 1)^2 = u(n)^2 + 2 * u(n) + 1")
    assert nm.normaliser(f, m, m.ev).noeud == nm.VRAI


# ---------------------------------------------------------------- remarque 18 (trouvée par l'exécutant) : entrées qui
# levaient une exception au lieu d'être « informes » ou évaluées
E = '{"enonce": "u(0) = U0", "ce_qui_le_tuerait": "x", "confiance": '


@pytest.mark.parametrize("sortie", [
    "[" * 200000 + "]" * 200000,  # imbrication profonde : RecursionError en v3
    b"\xff\xfe",  # octets non UTF-8
    E + "1" + "0" * 5000 + "}",  # entier de plus de 4 300 chiffres
])
def test_r18_sortie_illisible_informe(sortie):
    m, _, _ = _duplication()
    r = tdm.appliquer_batterie(sortie, m)
    assert r.statut == "informe"


def test_r18_exposant_decimal_demesure_informe():
    m, _, _ = _duplication()
    assert tdm.appliquer_batterie(E + "1E-99999}", m).statut == "informe"  # v3 : lu, et 1E-99999999 ne finissait pas
    s = '{"verdict": "faux", "contre_exemples": [{"n": 1E-99999}], "raison": "x"}'
    r = tdm.appliquer_batterie(tdm.sortie_de_texte("pour tout n dans NAT, u(n) < 3"), m)
    assert tdm.t6_verifier(s, r.arbre, m).type == tdm.TypeIssue.SORTIE_S_INFORME


@pytest.mark.parametrize("texte", [
    "pour tout n dans NAT, u(n) + (99^500) * (99^500) * (99^500) * (99^500) * (99^500) > 0",
    "pour tout n dans NAT, (u(n) + 99^500)^16 > 0",
])
def test_r18_coefficient_demesure_sans_exception(texte):
    m, _, _ = _duplication()
    r = batterie(m, texte, None)  # v3 : ValueError (conversion d'un entier de plus de 4 300 chiffres)
    assert r.statut in ("vivante", "morte")


def test_r18_cas_sain_sortie_ordinaire():
    m, _, _ = _duplication()
    assert tdm.appliquer_batterie(E + "0.5}", m).statut == "vivante"
