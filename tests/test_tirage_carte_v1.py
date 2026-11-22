"""Tirage des jetons sur l'appareil du modèle, v1 (correctif 0020) : Gumbel-max à bruit compté.

Se saute sans torch ni transformers (petit Llama à poids aléatoires, aucun téléchargement). Essais : déterminisme ; lignes
indépendantes du lot ; loi des jetons tirés (khi-deux, et l'artefact d'un tirage faux que le même essai refuse) ; égalité avec
l'ancien chemin à température nulle (interfaces, arrêts, jetons de fin) ; gardes (cas sain et artefact) ; un essai « carte »
marqué, qui ne se joue que si une carte est visible."""
import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")
scipy_stats = pytest.importorskip("scipy.stats")

from controle_ia.environnements.noter_rejeu_juges_v2 import generer_lot_borne  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.harnais import tirage_carte_v1 as tc  # noqa: E402
from controle_ia.harnais.episode import generer_lot  # noqa: E402
from controle_ia.iib import modele_v5 as m5  # noqa: E402
from controle_ia.iib.modele_tirage_carte_v1 import ModeleTorchTirageCarte  # noqa: E402
from controle_ia.iib.modele_v1 import ModeleTorch, format_jouet, petit_llama  # noqa: E402

V = 64
FINS = {5}


@pytest.fixture(scope="module")
def llama():
    return petit_llama(11, V)


def contextes(n, graine=0, longueur=(3, 9)):
    g = torch.Generator().manual_seed(graine)
    return [torch.randint(7, V, (int(torch.randint(longueur[0], longueur[1], (1,), generator=g)),), generator=g).tolist() for _ in range(n)]


# -- (1) déterminisme --------------------------------------------------------------------------------------------------------
def test_determinisme_deux_passages_memes_jetons(llama):
    c, g = contextes(6), [11, 22, 33, 44, 55, 2 ** 40 + 7]
    a, pa = tc.generer_lot_carte(llama, c, 12, 1.0, g, FINS, 0)
    b, pb = tc.generer_lot_carte(llama, c, 12, 1.0, g, FINS, 0)
    assert a == b and pa == pb and pa["tirage"] == tc.METHODE
    s1 = tc.suites_cache_duplique_carte(llama, c[0], list(range(8)), 16, 0.7, FINS, 0)
    assert s1 == tc.suites_cache_duplique_carte(llama, c[0], list(range(8)), 16, 0.7, FINS, 0)
    # des graines différentes donnent d'autres jetons (le hasard sert à quelque chose)
    assert tc.generer_lot_carte(llama, c, 12, 1.0, [x + 1 for x in g], FINS, 0)[0] != a


@pytest.mark.skipif(not torch.cuda.is_available(), reason="carte : se joue sur la machine de la course")
def test_carte_determinisme_et_bruit_sur_l_appareil(llama):
    m = petit_llama(11, V).to("cuda")
    c, g = contextes(8), list(range(100, 108))
    a = tc.generer_lot_carte(m, c, 16, 1.0, g, FINS, 0)[0]
    assert a == tc.generer_lot_carte(m, c, 16, 1.0, g, FINS, 0)[0]
    mo = tc.moities_des_graines(g, "cuda")
    assert tc.bruit_de_gumbel(mo, 3, V).device.type == "cuda"
    # le hachage entier est le même sur la carte et sur le processeur, au bit près
    assert torch.equal(tc._melange32(torch.arange(1000, device="cuda")).cpu(), tc._melange32(torch.arange(1000)))


# -- (2) lignes indépendantes du lot ---------------------------------------------------------------------------------------
def test_une_ligne_ne_depend_pas_des_autres_lignes_du_lot(llama):
    cible, graine = contextes(1, graine=5, longueur=(9, 10))[0], 987654
    seule = tc.generer_lot_carte(llama, [cible], 14, 1.0, [graine], FINS, 0)[0][0]
    for k, autres in enumerate((contextes(3, graine=1, longueur=(3, 9)), contextes(7, graine=2, longueur=(3, 9)))):
        lot = autres[:1] + [cible] + autres[1:]                    # autres lignes plus courtes : aucun remplissage de la cible
        g = [1000 + k * 10 + i for i in range(len(autres))]
        g = g[:1] + [graine] + g[1:]
        assert tc.generer_lot_carte(llama, lot, 14, 1.0, g, FINS, 0)[0][1] == seule
    # le bruit lui-même, au bit près, ne dépend que de (graine, pas, jeton)
    a = tc.bruit_de_gumbel(tc.moities_des_graines([graine, 1, 2], "cpu"), 4, V)
    b = tc.bruit_de_gumbel(tc.moities_des_graines([7, 8, 9, 10, graine], "cpu"), 4, V)
    assert torch.equal(a[0], b[4]) and not torch.equal(a[1], b[0])


# -- (3) loi des jetons tirés -------------------------------------------------------------------------------------------------
def _khi_deux(tirages, p):
    n = len(tirages)
    obs = torch.bincount(tirages, minlength=len(p)).double()
    return scipy_stats.chisquare(obs.numpy(), (n * p).numpy()).pvalue


@pytest.mark.parametrize("temperature", [1.0, 0.5, 1.7])
def test_frequences_des_jetons_tires_suivent_le_softmax(temperature):
    logits = torch.tensor([[2.0, 1.0, 0.0, -1.0, 0.5, -3.0, 1.5, float("-inf")]])
    p = torch.softmax(logits[0].double() / temperature, dim=-1)
    n = 40_000
    tirages = tc.tirer(logits.repeat(n, 1), temperature, tc.moities_des_graines(list(range(n)), "cpu"), 3)
    assert int(tirages.max()) < 7                                                     # jamais un jeton à −inf
    assert float(p[7]) == 0.0
    pv = _khi_deux(tirages, p[:7])                                                    # sept jetons finis, la loi du softmax
    assert pv > 1e-3, pv
    # même graine, pas différents : la loi tient aussi le long d'une ligne
    le_long = torch.stack([tc.tirer(logits, temperature, tc.moities_des_graines([424242], "cpu"), t)[0] for t in range(4000)])
    assert _khi_deux(le_long, p[:7]) > 1e-3


def test_artefact_un_tirage_faux_est_refuse_par_le_meme_essai():
    """R5 : l'essai de loi voit un tirage faux (bruit uniforme au lieu de Gumbel : la loi n'est plus le softmax)."""
    logits = torch.tensor([2.0, 1.0, 0.0, -1.0, 0.5, -3.0, 1.5])
    p = torch.softmax(logits.double(), dim=-1)
    n = 40_000
    mo = tc.moities_des_graines(list(range(n)), "cpu")
    g = tc.bruit_de_gumbel(mo, 3, 7)
    u = torch.exp(-torch.exp(-g))                                                     # l'uniforme sous-jacent
    faux = torch.argmax(logits.double()[None, :] + u, dim=-1)
    assert _khi_deux(faux, p) < 1e-6


# -- égalité avec l'ancien chemin à température nulle (interfaces, fins, arrêts) -----------------------------------------------
def test_temperature_nulle_egal_a_l_ancien_chemin(llama):
    c, g = contextes(5, graine=3), [1, 2, 3, 4, 5]
    vieux, pv = generer_lot(llama, c, 10, 0.0, g, FINS, 0)
    neuf, pn = tc.generer_lot_carte(llama, c, 10, 0.0, g, FINS, 0)
    assert neuf == vieux and {k: v for k, v in pn.items() if k != "tirage"} == pv
    e_v = generer_lot(llama, c, 6, 0.0, g, FINS, 0, empreinte_logits=True)[1]["empreintes_logits"]
    assert tc.generer_lot_carte(llama, c, 6, 0.0, g, FINS, 0, empreinte_logits=True)[1]["empreintes_logits"] == e_v
    fins = set(range(7, 30))                                                          # beaucoup de fins : des lignes finissent tôt
    assert tc.generer_lot_carte(llama, c, 10, 0.0, g, fins, 0)[0] == generer_lot(llama, c, 10, 0.0, g, fins, 0)[0]
    dec, arr = set(range(30, 50)), (lambda jetons: len(jetons) >= 3)
    assert tc.generer_lot_borne_carte(llama, c, 10, 0.0, g, fins, 0, dec, arr) == generer_lot_borne(llama, c, 10, 0.0, g, fins, 0, dec, arr)


def test_fins_gardees_lignes_finies_et_arrets_a_temperature_positive(llama):
    c, g = contextes(6, graine=4), list(range(6))
    fins, dec = set(range(7, 25)), set(range(25, 45))
    jetons, arrets = tc.generer_lot_borne_carte(llama, c, 12, 1.0, g, fins, 0, dec, lambda j: len(j) >= 2)
    for j, a in zip(jetons, arrets):
        assert 1 <= len(j) <= 12 and a in ("fin", "bloc clos", "budget")
        if a == "fin":
            assert j[-1] in fins and not any(x in fins for x in j[:-1])
        if a == "bloc clos":
            assert j[-1] in dec and len(j) >= 2
        if a == "budget":
            assert len(j) == 12


def test_modele_de_l_organisme_temperature_nulle_egal_et_choix_explicite(llama):
    fmt = format_jouet()
    vieux, neuf = ModeleTorch(petit_llama(11, len(fmt.tok)), fmt), ModeleTorchTirageCarte(petit_llama(11, len(fmt.tok)), fmt)
    c = [fmt.tok.encode("abc def", add_special_tokens=False)] * 2
    assert neuf.generer_actions(c, [1, 2], 8, 0.0) == vieux.generer_actions(c, [1, 2], 8, 0.0)
    assert neuf.suites(c[0], list(range(8)), 6, 0.0) == vieux.suites(c[0], list(range(8)), 6, 0.0)
    neuf.forme = vieux.forme = "prerempli_par_suite"
    assert neuf.suites(c[0], list(range(8)), 6, 0.0) == vieux.suites(c[0], list(range(8)), 6, 0.0)
    # choix : défaut inchangé ; « carte » refusé en mode jouet ; valeur inconnue refusée
    assert m5.TIRAGE_DEFAUT == "processeur" and m5.exiger_tirage("processeur", "jouet") == "processeur" and m5.exiger_tirage("carte", "reel") == "carte"
    for t, mode in (("carte", "jouet"), ("gpu", "reel"), ("", "reel")):
        with pytest.raises(GardeArret):
            m5.exiger_tirage(t, mode)


# -- (4) gardes ----------------------------------------------------------------------------------------------------------------
def test_gardes_graines_logits_temperature_lot(llama):
    assert tc.moities_des_graines([0, 2 ** 64 - 1], "cpu").tolist() == [[0, 0], [2 ** 32 - 1, 2 ** 32 - 1]]   # cas sain
    for g in (-1, 2 ** 64, 1.5, True, "3"):
        with pytest.raises(GardeArret, match="graine"):
            tc.moities_des_graines([g], "cpu")
    mo = tc.moities_des_graines([1, 2], "cpu")
    ok = torch.tensor([[0.0, 1.0, float("-inf")], [1.0, 0.0, 0.0]])
    assert tc.tirer(ok, 1.0, mo, 0).shape == (2,)                                     # −inf sur une partie : permis
    for mauvais in ([[0.0, float("nan"), 1.0], [1.0, 0.0, 0.0]], [[0.0, float("inf"), 1.0], [1.0, 0.0, 0.0]],
                    [[float("-inf")] * 3, [1.0, 0.0, 0.0]]):
        with pytest.raises(GardeArret, match="logits invalides"):
            tc.tirer(torch.tensor(mauvais), 1.0, mo, 0)
    with pytest.raises(GardeArret, match="température"):
        tc.tirer(ok, float("nan"), mo, 0)
    with pytest.raises(GardeArret, match="max_nouveaux"):
        tc.generer_lot_carte(llama, [[7, 8]], 0, 1.0, [1], FINS, 0)
    with pytest.raises(GardeArret, match="lot vide"):
        tc.generer_lot_carte(llama, [[7, 8], [9]], 4, 1.0, [1], FINS, 0)
    with pytest.raises(GardeArret, match="lot vide"):
        tc.generer_lot_carte(llama, [[]], 4, 1.0, [1], FINS, 0)
    with pytest.raises(GardeArret, match="préfixe ou graines vides"):
        tc.suites_cache_duplique_carte(llama, [7], [], 4, 1.0, FINS, 0)


def test_aucune_copie_des_logits_ni_boucle_par_ligne_dans_le_tirage():
    """Garde statique : `tirer` et `bruit_de_gumbel` n'appellent ni `.to("cpu")`, ni `.cpu()`, ni `multinomial`, ni générateur,
    et ne bouclent pas sur les lignes ; les seules copies vers le processeur du module (six) sont, à la fin, les jetons tirés et
    les longueurs (deux fonctions, quatre copies), et, sur demande seulement, les logits et l'état des lignes pour l'empreinte de
    rejeu (deux)."""
    import inspect

    for f in (tc.tirer, tc.bruit_de_gumbel, tc._melange32):
        src = inspect.getsource(f)
        assert not any(x in src for x in ('.to("cpu"', ".cpu()", "multinomial", "Generator", "for ", ".item()")), f.__name__
    module = inspect.getsource(tc)
    assert module.count('.to("cpu"') == 6 and "multinomial(" not in module and "torch.Generator(" not in module


# -- correctif 0021 : contre-lecture cl1 du 0020 (m1, m2) ---------------------------------------------------------------------
def test_uniforme_a_53_bits_deux_hachages_independants():
    """m1 : `b` n'est plus une fonction de `a` (avant : b = H(a ^ c), 32 bits d'entropie). Cas sain : sur 64 000 couples, b diffère
    de l'ancienne fonction de a presque partout, et a et b ne sont pas corrélés ; artefact : l'ancienne construction est vue."""
    mo = tc.moities_des_graines(list(range(1000)), "cpu")
    a, b = tc.deux_hachages(mo, 7, 64)
    ancien = tc._melange32(a ^ tc._SEL_DEUX)
    assert float((b == ancien).double().mean()) < 1e-3
    assert abs(float(torch.corrcoef(torch.stack([a.flatten().double(), b.flatten().double()]))[0, 1])) < 0.02
    assert bool((ancien == tc._melange32(a ^ tc._SEL_DEUX)).all())                     # artefact : l'ancienne b est une fonction de a
    u = ((a >> 11).double() * 2.0 ** 32 + b.double() + 0.5) / 2.0 ** 53
    assert 0.0 < float(u.min()) and float(u.max()) < 1.0 and abs(float(u.mean()) - 0.5) < 0.005
    import inspect

    src = inspect.getsource(tc.deux_hachages)
    assert not any(x in src for x in ('.to("cpu"', ".cpu()", "multinomial", "Generator", "for ", ".item()"))


def test_garde_des_logits_sur_les_seules_lignes_actives():
    """m2 : un NaN sur une ligne finie n'arrête pas le lot (l'ancien chemin ne lisait pas ses logits) ; un NaN sur une ligne
    active l'arrête ; un lot dont toutes les lignes sont finies ne juge rien."""
    mo = tc.moities_des_graines([1, 2, 3], "cpu")
    l = torch.tensor([[0.0, 1.0, 2.0], [float("nan")] * 3, [1.0, 0.0, 0.0]])
    j = tc.tirer(l, 1.0, mo, 0, torch.tensor([True, False, True]))
    assert j.shape == (3,) and 0 <= int(j[0]) < 3
    with pytest.raises(GardeArret, match="logits invalides"):
        tc.tirer(l, 1.0, mo, 0, torch.tensor([True, True, True]))
    with pytest.raises(GardeArret, match="logits invalides"):
        tc.tirer(l, 1.0, mo, 0)                                                         # sans masque : toutes les lignes jugées
    tc.tirer(l, 1.0, mo, 0, torch.tensor([False, False, False]))
