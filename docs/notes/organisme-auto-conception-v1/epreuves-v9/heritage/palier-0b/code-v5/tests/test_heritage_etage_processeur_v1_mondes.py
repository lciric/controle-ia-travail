"""Essais du générateur des mondes (B1) et de son audit : garde 25 (cas sains : générateur accepté, bornes gelées sans arrêt ;
artefacts : deux lois plantées trop proches, dose inscrite dans la présentation, poids des dépendantes doublés, bornes ramenées à
un tirage par loi et un essai par monde) ; marge face à la source étrangère (B7 bis) ; forme unique ; dose et paires. Audit à
taille réduite seulement (quatre suites par dose ; l'audit à pleine taille est l'étape 3), graines « essai ».

Code v4 (préenregistrement v8) : longueur de forme sur le texte aux nombres remplacés, longueur brute parmi les traits de contenu
(nœud 1) ; σ₀ par permutation, entre lois ou entre suites, et règle calibrée pour les seuls audits des mondes par dose, lettre
de la version 6 pour les deux audits de lois (nœud 2) ; artefacts de la garde 25 : valeurs plantées dans la zone médiane
(mention sans arrêt), exactitude de forme plantée à 0,56 dans un audit de lois (arrêt), signes des lois dépendantes changés
(vus par le contenu, non par la forme), pli privé d'une classe et exactitude non calculable (arrêt) ; étape 3. Les essais
jouent peu de permutations (`PERMUTATIONS_D_ESSAI`) ; la valeur gelée, 1 000, est celle de l'étape 3.

Code v5 (préenregistrement v11, « Ce qui demande un code v5 », points 1, 2, 3 et 6 ; NE-3) : seuil calibré M + 2 σ₀ ; seuil
d'arrêt de la forme des doses au plus grand de 0,55 et de M + 2 σ₀ (une exactitude au plus 0,55 n'arrête jamais) ; règle
calibrée de signalement pour le contenu et les réunis des doses (zone médiane : ni signalement ni mention) ; audits de lois à la
lettre ; égalité A = M + 2 σ₀ lue « au plus » ; colonne du seuil d'arrêt ; plis de la lecture observée dérivés par l'étape 3
sous le rôle « plis », distincts des permutations. Valeurs plantées, non tirées, pour la garde 25."""

import itertools

import numpy as np
import pytest

from aides_heritage_etage_processeur_v1 import graines
from controle_ia.heritage_etage_processeur_v1 import audit as AU
from controle_ia.heritage_etage_processeur_v1 import lois as L
from controle_ia.heritage_etage_processeur_v1 import mondes as MO
from controle_ia.heritage_etage_processeur_v1.constantes import DOSES, PERMUTATIONS_AUDIT

SUITES_PAR_DOSE = 4
PERMUTATIONS_D_ESSAI = 20


def _rng_permutation(graine):
    return np.random.default_rng(graine)


def _suites(g, famille, **kw):
    return [MO.generer_suite(g, dict(couche="essai", famille=famille, dose=d, source=k), d, **kw)
            for d in DOSES for k in range(SUITES_PAR_DOSE)]


@pytest.fixture(scope="module")
def saines():
    return _suites(graines(), "audit-sain")


def test_garde_25_generateur_sain_accepte_et_forme_unique(saines):
    for s in saines:
        assert sum(1 for l in s.source.lois.values() if l["type"] == "vraie") == 8
        assert AU.audit_compositions_de_la_source(s.source.vraies_par_rang(), s.source.oracle.Z, s.source.oracle.G) == []
        d = MO.nombre_de_dependantes(s.source.dose)
        for m in [s.source] + s.mondes_cibles():
            assert AU.audit_marges({i: l["loi"] for i, l in m.lois.items()}, m.oracle.Z, m.oracle.G,
                                   s.source.vraies_par_rang() if m.role != "source" else ()) == []
            for l in m.lois.values():
                assert l["loi"]["type"] == "par_sous_population" and sorted(l["loi"]["lois"]) == ["0", "1"]
                assert all(x["type"] == "softmax" for x in l["loi"]["lois"].values())
            if m.role != "source":
                assert len(m.vraies()) == len(m.fausses()) == 12
                assert sum(1 for l in m.lois.values() if l["dependante"]) == d
                assert sum(1 for dd in m.domaines if dd["vraie"] is None) == 4
        paires = [p for w in s.paires for p in w]
        assert len(paires) == len(set(paires)) == 4 * d  # sans remise, sur les quatre mondes cibles
        assert AU.ensemble_exclu_par_construction([l["texte"] for l in s.finale.lois.values()],
                                                  [l["texte"] for l in s.source.lois.values()]) == []
    # loi dépendante : la loi vraie de plus petit rang sur la première sous-population, l'autre sur la seconde
    s = saines[-1]
    rang = s.source.vraies_par_rang()
    for l in s.finale.lois.values():
        if l["dependante"]:
            p, q = l["paire"]
            assert p < q and l["loi"]["lois"]["0"] == rang[p]["lois"]["0"] and l["loi"]["lois"]["1"] == rang[q]["lois"]["1"]
    c = MO.Compteurs()
    for s in saines:
        c.ajouter(s.compteurs)
    assert all(v[0] >= v[1] > 0 for v in c.vers_dict()["tirages_tentes_acceptes"].values())


def _mondes_sains_par_construction(mondes_par_dose, graine=250):
    """Un générateur sain pour la présentation, par construction : toutes les lois sont tirées de la même loi, quelle que soit
    leur sorte (vraie ou fausse, dépendante ou non, dose). Il éprouve le cas sain de l'audit de présentation, à une taille où le
    bruit de la validation croisée reste loin de 0,55."""
    rng = np.random.default_rng(graine)
    Z, G = L.instances_oracle(graine, 4000)
    out = []
    for dose in DOSES:
        d = MO.nombre_de_dependantes(dose)
        for _ in range(mondes_par_dose):
            lois = []
            for k in range(24):
                loi = L.loi_par_sous_population(L.softmax_aleatoire(rng), L.softmax_aleatoire(rng))
                lois.append((L.json_canonique(loi), loi, "vraie" if k < 12 else "fausse", k < d))
            out.append({"dose": dose, "suite": len(out) // 4, "Z": Z, "G": G, "lois": lois})  # quatre mondes par suite
    return out


def _attendu(j, a, A, s, M):
    """La lecture de la section « Seuil » (version 11), écrite à part du code : audits des doses, au plus 0,55 jamais un arrêt
    ni un signalement ; au-dessus de 0,55 et de M + 2 σ₀, arrêt (forme) ou signalement (contenu, réunis) ; entre les deux, non
    départagée. Audits de lois à la lettre."""
    if a.startswith("mondes_dose"):
        if A <= 0.55:
            return AU.TENUE if j == "forme" else AU.AU_PLUS
        if A > M + 2 * s:
            return AU.ARRET if j == "forme" else AU.SIGNALEE
        return AU.NON_DEPARTAGEE
    if j != "forme":
        return AU.SIGNALEE if A > 0.55 else AU.AU_PLUS
    return AU.ARRET if A > 0.55 else AU.TENUE


def _verifier_table(pres, permutations):
    """Les quinze exactitudes portent A, σ₀, la moyenne permutée M, le seuil calibré M + 2 σ₀, le seuil d'arrêt (NE-3) et leur
    lecture, et chaque lecture est celle de la règle (forme des lois à la lettre ; forme des doses calibrée, le seuil d'arrêt
    étant le plus grand de 0,55 et de M + 2 σ₀ ; contenu et réunis des doses, règle calibrée de signalement ; contenu et réunis
    des lois à la lettre)."""
    lignes = [(j, a, e) for j, d in pres["table"].items() for a, e in d.items()]
    assert len(lignes) == 15 and sorted(pres["table"]) == sorted(AU.JEUX_DE_TRAITS)
    for j, a, e in lignes:
        assert e["A"] == pres["exactitudes"][j][a] and e["permutations"] == permutations
        assert e["sigma0"] > 0 and 0.0 <= e["moyenne_permutee"] <= 1.0
        assert e["seuil_calibre"] == e["moyenne_permutee"] + 2 * e["sigma0"]
        if j != "forme":
            assert e["seuil_d_arret"] is None
        elif a.startswith("mondes_dose"):
            assert e["seuil_d_arret"] == max(0.55, e["moyenne_permutee"] + 2 * e["sigma0"])
        else:
            assert e["seuil_d_arret"] == 0.55
        assert e["permutation"] == ("entre suites" if a.startswith("mondes_dose") else "entre lois")
        attendu = _attendu(j, a, e["A"], e["sigma0"], e["moyenne_permutee"])
        assert e["lecture"] == attendu, (j, a, e)
        if j == "forme":
            assert (attendu == AU.ARRET) == (e["A"] > e["seuil_d_arret"])
        assert (f"{j}/{a}" in pres["arret"]) == (attendu == AU.ARRET)
        assert (f"{j}/{a}" in pres["non_departagees"]) == (attendu == AU.NON_DEPARTAGEE and j == "forme")
        assert (f"{j}/{a}" in pres["non_departagees_sans_mention"]) == (attendu == AU.NON_DEPARTAGEE and j != "forme")
        assert (f"{j}/{a}" in pres["signalement"]) == (attendu == AU.SIGNALEE)
    assert (pres["mention"] is not None) == bool(pres["signalement"] or pres["non_departagees"])


def test_garde_25_audit_de_presentation_cas_sain():
    """Cas sain de la garde 25 (B9 : « générateur sain : aucun arrêt »). Code v4 : aucune exactitude de forme n'arrête ni
    n'est non départagée, et aucune des quinze ne s'écarte de la moyenne permutée de plus de trois σ₀. Code v5 : les exactitudes
    de contenu et réunies des doses sont lues selon la règle calibrée de signalement (M + 2 σ₀), celles des lois à la lettre ;
    un signalement de contenu ou réuni n'est pas un arrêt, et l'essai ne l'exige ni ne l'exclut (constat du rapport du code v4 :
    « reunis/mondes_dose_0.25_contre_0.5 », 0,558, z = +2,4, signalée à la lettre sur ces graines)."""
    pres = AU.audit_presentation(_mondes_sains_par_construction(300), np.random.default_rng(25), _rng_permutation(2501),
                                 PERMUTATIONS_D_ESSAI)
    assert pres["arret"] == [] and pres["non_departagees"] == [], pres["table"]
    assert all(abs(e["A"] - e["moyenne_permutee"]) <= 3 * e["sigma0"] for d in pres["table"].values() for e in d.values())
    assert all(s.split("/")[0] in ("contenu", "reunis") for s in pres["signalement"])
    _verifier_table(pres, PERMUTATIONS_D_ESSAI)
    assert PERMUTATIONS_AUDIT == 1000


def test_audit_de_presentation_du_generateur_de_b1_a_taille_reduite(saines):
    """Constat, sans seuil à cette taille (quatre suites par dose ; l'audit à pleine taille est l'étape 3) : les quinze
    exactitudes se calculent sur les mondes du générateur constructif, chacune avec σ₀, la moyenne des exactitudes permutées et
    le seuil calibré (code v4 ; « Ce qui demande un code v4 », point 7 : la moyenne permutée est rapportée), et la distribution
    des traits de contenu par sorte de loi est rapportée, longueur brute comprise."""
    mondes = MO.mondes_pour_l_audit(saines)
    assert [m["suite"] for m in mondes] == [i for i in range(len(saines)) for _ in range(4)]
    pres = AU.audit_presentation(mondes, np.random.default_rng(25), _rng_permutation(2502), PERMUTATIONS_D_ESSAI)
    _verifier_table(pres, PERMUTATIONS_D_ESSAI)
    n = 4 * SUITES_PAR_DOSE  # mondes cibles et finaux par dose
    for j in AU.JEUX_DE_TRAITS:  # permutation entre suites (deux doses de quatre suites), entre lois sinon
        assert all(pres["table"][j][a]["unites_permutees"] == 2 * SUITES_PAR_DOSE for a in AU.AUDITS_DES_DOSES)
        assert pres["table"][j]["vraies_contre_fausses"]["unites_permutees"] == 3 * n * 24
        assert pres["table"][j]["dependantes_contre_independantes"]["unites_permutees"] == 2 * n * 12
    dist = MO.distribution_des_traits_de_contenu(saines)
    assert set(dist) == {"vraie-source", "fausse-source", "dependante", "independante", "fausse-cible"}
    assert all("longueur_brute" in v for v in dist.values())


def test_longueur_de_forme_sur_le_texte_aux_nombres_remplaces():
    """Nœud 1, option (a) : la longueur de forme compte chaque nombre d'au moins quatre décimales, signe et exposant compris,
    pour un caractère ; les nombres plus courts restent écrits ; la longueur brute est le dernier trait de contenu."""
    texte = '{"a":[-0.123456,0.5,-1e-05,-2.5000e-07,-0.1234],"b":"x"}'
    assert AU.texte_aux_nombres_remplaces(texte) == '{"a":[#,0.5,-1e-05,#,#],"b":"x"}'
    assert list(AU.jetons(texte)).count("<nombre>") == 3
    v = AU.traits_de_forme(texte)
    assert v[AU.CASES] == len('{"a":[#,0.5,-1e-05,#,#],"b":"x"}') and v[AU.CASES] != len(texte)
    assert AU.traits_de_forme(texte.replace("-1e-05", "1e-05"))[AU.CASES] == v[AU.CASES] - 1  # un nombre court garde son signe
    sans_signe = texte.replace("-0.123456", "0.123456").replace("-2.5000e-07", "2.5000e-07")
    assert np.array_equal(AU.traits_de_forme(sans_signe), v)  # le signe d'un nombre long n'entre pas dans la forme
    Z, G = L.instances_oracle(7, 200)
    loi = L.loi_par_sous_population(L.softmax_aleatoire(np.random.default_rng(7)), L.softmax_aleatoire(np.random.default_rng(8)))
    c = AU.traits_de_contenu(loi, Z, G, L.json_canonique(loi))
    assert len(c) == 7 and c[6] == len(L.json_canonique(loi))
    with pytest.raises(AU.AuditRefuse):
        AU.traits_de_contenu(loi, Z, G, L.json_canonique(loi) + " ")


def _table_plantee(A=0.5, sigma0=0.02, moyenne=0.5, **changes):
    """Une table plantée des quinze exactitudes (valeurs non tirées) ; `changes` : {"jeu/audit": (A, σ₀, M)}."""
    t = {j: {a: {"A": A, "sigma0": sigma0, "moyenne_permutee": moyenne} for a in AU.AUDITS} for j in AU.JEUX_DE_TRAITS}
    for nom, (a, s, m) in changes.items():
        j, au = nom.split("/")
        t[j][au] = {"A": a, "sigma0": s, "moyenne_permutee": m}
    return t


DOSE_F = "forme/mondes_dose_0.0_contre_0.5"
DOSE_C = "contenu/mondes_dose_0.25_contre_0.5"
DOSE_R = "reunis/mondes_dose_0.0_contre_0.25"


def _rien(l):
    return (l["arret"] == l["non_departagees"] == l["non_departagees_sans_mention"] == l["signalement"] == []
            and l["mention"] is None)


def test_garde_25_lecture_calibree_sur_valeurs_plantees():
    """Garde 25, valeurs plantées de A, de M et de σ₀, non tirées (versions 9, 10 et 11). Forme des doses : zone médiane,
    mention sans arrêt ; au-dessus de 0,55 et de M + 2 σ₀, arrêt ; M au-dessus de 0,55 : au-dessus de 0,55 + 2 σ₀ sans dépasser
    M + 2 σ₀, aucun arrêt ; M sous 0,5 : au-dessus de M + 2 σ₀ et de 0,55 sans dépasser 0,55 + 2 σ₀, arrêt. Audits de lois à la
    lettre (forme 0,56 : arrêt ; contenu 0,56 : signalement, mention), même quand M + 2 σ₀ les dirait non départagées. Contenu
    et réunis des doses : au-dessus de 0,55 et de M + 2 σ₀, signalement et mention, jamais un arrêt ; zone médiane, ni
    signalement ni mention, seulement les mots « non départagée du hasard à cette taille »."""
    assert _rien(AU.lire_audit(_table_plantee()))
    l = AU.lire_audit(_table_plantee(**{DOSE_F: (0.58, 0.02, 0.55)}))  # M + 2 σ₀ = 0,59
    assert l["arret"] == [] and l["non_departagees"] == [DOSE_F] and l["mention"] == AU.MENTION
    assert l["lectures"]["forme"]["mondes_dose_0.0_contre_0.5"] == "non départagée du hasard à cette taille"
    assert AU.lire_audit(_table_plantee(**{DOSE_F: (0.60, 0.02, 0.5)}))["arret"] == [DOSE_F]
    assert AU.lire_audit(_table_plantee(**{DOSE_F: (0.55, 0.0, 0.5)}))["lectures"]["forme"]["mondes_dose_0.0_contre_0.5"] \
        == AU.TENUE
    # version 9 : M au-dessus de 0,55 — 0,61 dépasse 0,55 + 2 σ₀ (0,59) sans dépasser M + 2 σ₀ (0,62) : aucun arrêt, mention
    l = AU.lire_audit(_table_plantee(**{DOSE_F: (0.61, 0.02, 0.58)}))
    assert l["arret"] == [] and l["non_departagees"] == [DOSE_F] and l["mention"] == AU.MENTION
    # version 9 : M sous 0,5 — 0,60 dépasse M + 2 σ₀ (0,54) et 0,55 sans dépasser 0,55 + 2 σ₀ (0,63) : arrêt
    assert AU.lire_audit(_table_plantee(**{DOSE_F: (0.60, 0.04, 0.46)}))["arret"] == [DOSE_F]
    # audits de lois à la lettre
    for loi in ("forme/vraies_contre_fausses", "forme/dependantes_contre_independantes"):
        l = AU.lire_audit(_table_plantee(**{loi: (0.56, 0.04, 0.5)}))  # M + 2 σ₀ = 0,58 : la règle calibrée ne l'arrêterait pas
        assert l["arret"] == [loi] and l["non_departagees"] == [] and l["mention"] is None
    for loi in ("contenu/vraies_contre_fausses", "reunis/dependantes_contre_independantes"):
        l = AU.lire_audit(_table_plantee(**{loi: (0.56, 0.04, 0.5)}))
        assert l["signalement"] == [loi] and l["arret"] == [] and l["non_departagees_sans_mention"] == []
        assert l["mention"] == AU.MENTION
    assert AU.lecture("forme", "mondes_dose_0.25_contre_0.5", 0.56, 0.04, 0.5) == AU.NON_DEPARTAGEE  # la règle des doses
    # contenu et réunis des doses : au-dessus de 0,55 et de M + 2 σ₀, signalement et mention, jamais un arrêt
    l = AU.lire_audit(_table_plantee(**{DOSE_C: (0.62, 0.02, 0.5), DOSE_R: (0.9, 0.01, 0.5)}))
    assert l["arret"] == [] and l["signalement"] == sorted([DOSE_C, DOSE_R]) and l["mention"] == AU.MENTION
    # zone médiane du contenu et des réunis (version 10, lecture (i)) : ni signalement, ni mention, ni arrêt
    l = AU.lire_audit(_table_plantee(**{DOSE_C: (0.58, 0.03, 0.53), DOSE_R: (0.57, 0.02, 0.54)}))  # M + 2 σ₀ : 0,59 ; 0,58
    assert l["arret"] == l["signalement"] == l["non_departagees"] == [] and l["mention"] is None
    assert l["non_departagees_sans_mention"] == sorted([DOSE_C, DOSE_R])
    assert l["lectures"]["contenu"]["mondes_dose_0.25_contre_0.5"] == "non départagée du hasard à cette taille"
    t = _table_plantee()
    del t["forme"]["vraies_contre_fausses"]
    with pytest.raises(AU.AuditRefuse):
        AU.lire_audit(t)
    t = _table_plantee()
    del t["forme"]["mondes_dose_0.0_contre_0.25"]["moyenne_permutee"]
    with pytest.raises(AU.AuditRefuse, match="moyenne permutée"):
        AU.lire_audit(t)


def test_garde_25_au_plus_0_55_jamais_un_arret_ni_un_signalement():
    """Version 11 (remarque 1 tranchée par Lazar, GO-2026-11-20-41, option (ii)) : une exactitude de forme plantée au plus 0,55
    et au-dessus de M + 2 σ₀, M + 2 σ₀ étant planté sous 0,55, n'arrête pas : elle est tenue, sans mention ; une exactitude de
    contenu ou réunie plantée de même n'est ni signalée ni mentionnée. Un code qui arrête sur une exactitude au plus 0,55 échoue
    ici."""
    for A in (0.53, 0.55):  # M + 2 σ₀ = 0,49
        l = AU.lire_audit(_table_plantee(**{DOSE_F: (A, 0.02, 0.45), DOSE_C: (A, 0.02, 0.45), DOSE_R: (A, 0.02, 0.45)}))
        assert _rien(l), l
        assert l["lectures"]["forme"]["mondes_dose_0.0_contre_0.5"] == AU.TENUE
        assert l["lectures"]["contenu"]["mondes_dose_0.25_contre_0.5"] == AU.AU_PLUS
        assert l["lectures"]["reunis"]["mondes_dose_0.0_contre_0.25"] == AU.AU_PLUS
    assert AU.seuil_d_arret("forme", "mondes_dose_0.0_contre_0.5", 0.02, 0.45) == 0.55


def test_garde_25_egalite_au_seuil_calibre_au_plus():
    """Silence n° 4 au seuil neuf (version 10, contrôle de la version 9, § 7) : une exactitude égale à M + 2 σ₀ est au plus
    M + 2 σ₀ (valeurs exactes en binaire : M = 0,5, σ₀ = 0,0625, A = 0,625). Forme : non départagée, pas un arrêt ; contenu :
    non départagée, ni signalement ni mention ; et une exactitude égale à 0,55 est au plus 0,55."""
    assert 0.5 + 2.0 * 0.0625 == 0.625
    l = AU.lire_audit(_table_plantee(**{DOSE_F: (0.625, 0.0625, 0.5), DOSE_C: (0.625, 0.0625, 0.5)}))
    assert l["arret"] == [] and l["non_departagees"] == [DOSE_F] and l["non_departagees_sans_mention"] == [DOSE_C]
    assert l["signalement"] == []
    assert AU.lecture("forme", "mondes_dose_0.0_contre_0.25", 0.625 + 1e-12, 0.0625, 0.5) == AU.ARRET
    assert AU.lecture("contenu", "mondes_dose_0.0_contre_0.25", 0.625 + 1e-12, 0.0625, 0.5) == AU.SIGNALEE
    assert AU.lecture("forme", "mondes_dose_0.0_contre_0.25", 0.55, 0.0, 0.5) == AU.TENUE


def test_colonne_du_seuil_d_arret_ne_3():
    """NE-3 (contrôle de la version 11, retenu par la mère, R-4210) : la colonne `seuil_d_arret` porte le plus grand de 0,55 et
    de M + 2 σ₀ pour la forme des audits des doses ; 0,55 pour la forme des audits de lois ; rien pour le contenu et les réunis,
    qui n'arrêtent jamais. La colonne `seuil_calibre` porte M + 2 σ₀ pour les quinze."""
    assert AU.seuil_calibre(0.02, 0.45) == 0.45 + 2 * 0.02
    for d in AU.AUDITS_DES_DOSES:
        assert AU.seuil_d_arret("forme", d, 0.02, 0.45) == 0.55  # M + 2 σ₀ = 0,49 : le plancher
        assert AU.seuil_d_arret("forme", d, 0.02, 0.58) == 0.58 + 2 * 0.02
        assert AU.seuil_d_arret("contenu", d, 0.02, 0.58) is None and AU.seuil_d_arret("reunis", d, 0.02, 0.58) is None
    for a in AU.AUDITS_DE_LOIS:
        assert AU.seuil_d_arret("forme", a, 0.2, 0.58) == 0.55
    with pytest.raises(AU.AuditRefuse):
        AU.seuil_d_arret("forme", "inconnu", 0.02, 0.5)


class _RngPlante:
    """Un générateur planté : `permutation` rend, tour à tour, les permutations données (pour placer les plis à la main)."""

    def __init__(self, *perms):
        self.perms, self.k = [np.asarray(p) for p in perms], 0

    def permutation(self, n):
        p = self.perms[self.k % len(self.perms)]
        self.k += 1
        assert len(p) == n
        return p.copy()


def _perm_qui_prive_le_pli_0(n=25):
    """Les exemples 0 à 4 tombent tous dans le pli 0 (pli[perm[i]] = i mod 5)."""
    perm = np.empty(n, dtype=int)
    perm[[0, 5, 10, 15, 20]] = [0, 1, 2, 3, 4]
    perm[[i for i in range(n) if i % 5]] = list(range(5, n))
    return perm


def test_garde_25_pli_prive_d_une_classe_et_exactitude_non_calculable_arretent():
    rng = np.random.default_rng(3)
    X = rng.normal(size=(25, 3))
    y = [1] * 5 + [0] * 20
    assert 0.0 <= AU.exactitude_equilibree(X, y, np.random.default_rng(4)) <= 1.0  # cas sain : calculée
    with pytest.raises(AU.ArretAudit, match="privé d'une classe"):
        AU.exactitude_equilibree(X, y, _RngPlante(_perm_qui_prive_le_pli_0()))
    with pytest.raises(AU.ArretAudit, match="non calculable"):
        AU.exactitude_equilibree(X[1:], y[1:], np.random.default_rng(4))  # quatre exemples d'une classe
    with pytest.raises(AU.ArretAudit, match="non calculable"):
        AU.exactitude_equilibree(X, [0] * 25, np.random.default_rng(4))  # une seule classe
    Xn = X.copy()
    Xn[0, 0] = np.nan
    with pytest.raises(AU.ArretAudit, match="non fini"):
        AU.exactitude_equilibree(Xn, y, np.random.default_rng(4))
    # sous permutation aussi : étiquettes laissées en place, puis plis placés à la main
    assert AU.sous_permutation(X, y, np.random.default_rng(5), 5)["sigma0"] > 0
    with pytest.raises(AU.ArretAudit, match="privé d'une classe"):
        AU.sous_permutation(X, y, _RngPlante(np.arange(25), _perm_qui_prive_le_pli_0()), 5)
    with pytest.raises(AU.AuditRefuse):
        AU.sous_permutation(X, y, np.random.default_rng(5), 1)


def test_permutation_entre_suites_garde_l_etiquette_commune():
    """Audits des mondes par dose : les étiquettes sont permutées entre suites, les mondes d'une suite gardant une étiquette
    commune ; entre lois pour les audits de lois."""
    yi = np.array([0] * 12 + [1] * 12)
    groupes = [k // 4 for k in range(24)]
    rng = np.random.default_rng(11)
    vus = set()
    for _ in range(50):
        yp = AU.permuter_les_etiquettes(yi, groupes, rng)
        assert sorted(yp.tolist()) == sorted(yi.tolist())
        assert all(len({int(yp[i]) for i in range(24) if groupes[i] == g}) == 1 for g in set(groupes))
        vus.add(tuple(yp.tolist()))
    assert len(vus) > 1
    yl = AU.permuter_les_etiquettes(yi, None, np.random.default_rng(12))
    assert sorted(yl.tolist()) == sorted(yi.tolist())
    assert any(len({int(yl[i]) for i in range(24) if groupes[i] == g}) == 2 for g in set(groupes))
    with pytest.raises(AU.AuditRefuse):
        AU.permuter_les_etiquettes(np.array([0, 1, 1, 1]), [0, 0, 1, 1], rng)
    with pytest.raises(AU.AuditRefuse, match="identifiant de la suite"):
        AU.audit_presentation([{k: v for k, v in m.items() if k != "suite"} for m in _mondes_sains_par_construction(2)],
                              np.random.default_rng(1), np.random.default_rng(2), 2)


def test_garde_25_deux_lois_trop_proches_le_monde_est_rejete(saines):
    m = saines[0].cibles[0]
    lois = {i: l["loi"] for i, l in m.lois.items()}
    a, b = sorted(lois)[:2]
    # une loi proche mais distincte : la première ligne de poids de chaque sous-loi déplacée de 0,05 (déplacer toutes les
    # lignes du même vecteur laisserait la loi identique, une softmax étant invariante par un tel déplacement)
    proche = {"type": "par_sous_population", "lois": {
        g: {"type": "softmax", "poids": [[w + (0.05 if i == 0 else 0.0) for w in ligne] for i, ligne in enumerate(s["poids"])],
            "biais": s["biais"]} for g, s in lois[a]["lois"].items()}}
    lois[b] = proche
    manques = AU.audit_marges(lois, m.oracle.Z, m.oracle.G)
    assert any(x[1:3] == (a, b) and 0.0 < x[3] < 0.25 for x in manques)


def test_garde_25_dose_inscrite_dans_la_presentation_arret():
    """Artefact : une dose inscrite dans la présentation ; l'exactitude de forme d'un audit des mondes par dose dépasse
    M + 2 σ₀ et 0,55 (règle calibrée, σ₀ et M par permutation entre suites ; code v5) : arrêt."""
    g = graines()
    suites = _suites(g, "audit-dose-inscrite", variante="dose-inscrite")
    pres = AU.audit_presentation(MO.mondes_pour_l_audit(suites), np.random.default_rng(26), _rng_permutation(2601), 50)
    assert any(a.startswith("forme/mondes_dose") for a in pres["arret"])
    assert any(e["A"] > e["seuil_calibre"] and e["A"] > 0.55 and e["A"] > e["seuil_d_arret"]
               for k, e in pres["table"]["forme"].items() if k.startswith("mondes_dose"))
    _verifier_table(pres, 50)


def test_garde_25_poids_des_dependantes_doubles_signale(saines):
    """Artefact : les poids des lois dépendantes doublés par un générateur fautif planté ; exactitude de contenu au-dessus de
    0,55, signalée. Code v4 : les mondes à dose nulle (du générateur sain) sont joints, sans quoi l'audit des mondes 0 contre
    0,25 ne peut être calculé, ce qui arrête désormais."""
    g = graines()
    suites = [MO.generer_suite(g, dict(couche="essai", famille="audit-poids", dose=d, source=k), d,
                               faute="poids-dependantes-doubles") for d in (0.25, 0.5) for k in range(SUITES_PAR_DOSE)]
    nulles = [s for s in saines if s.source.dose == 0.0]
    pres = AU.audit_presentation(MO.mondes_pour_l_audit(nulles + suites), np.random.default_rng(27), _rng_permutation(2701),
                                 PERMUTATIONS_D_ESSAI)
    assert pres["exactitudes"]["contenu"]["dependantes_contre_independantes"] > 0.55
    assert "contenu/dependantes_contre_independantes" in pres["signalement"]
    assert pres["mention"] == "générateur non audité pour l'étage payant"
    with pytest.raises(AU.ArretAudit, match="non calculable"):
        AU.audit_presentation(MO.mondes_pour_l_audit(suites), np.random.default_rng(27), _rng_permutation(2701), 2)


def _signes_des_dependantes_changes(mondes):
    """Un générateur fautif planté (sur la sortie du générateur sain) : tous les poids des lois dépendantes rendus positifs ;
    les biais et toutes les autres lois inchangés."""
    out = []
    for m in mondes:
        lois = []
        for texte, loi, typ, dep in m["lois"]:
            if dep:
                loi = {"type": "par_sous_population", "lois": {
                    g: {"type": "softmax", "poids": [[abs(w) for w in ligne] for ligne in s["poids"]], "biais": s["biais"]}
                    for g, s in loi["lois"].items()}}
                texte = L.json_canonique(loi)
            lois.append((texte, loi, typ, dep))
        out.append(dict(m, lois=lois))
    return out


def test_garde_25_signes_des_dependantes_changes_vus_par_le_contenu_et_non_par_la_forme(saines):
    """Garde 25, code v4 (nœud 1, option (a)) : les signes des poids des lois dépendantes changés par un générateur fautif
    planté. La longueur de forme ne lit plus le signe : les traits de forme d'une loi dont tous les nombres ont au moins quatre
    décimales ne changent pas ; la longueur brute, trait de contenu, le lit ; l'exactitude de contenu « dépendantes contre
    indépendantes » dépasse 0,55 et est signalée ; celle de forme ne bouge que par les nombres courts."""
    saines_m = MO.mondes_pour_l_audit(saines)
    fautives = _signes_des_dependantes_changes(saines_m)
    longues = changees = 0
    for m0, m1 in zip(saines_m, fautives):
        for (t0, _, _, dep), (t1, l1, _, _) in zip(m0["lois"], m1["lois"]):
            if not dep or t0 == t1:
                continue
            changees += 1
            assert AU.traits_de_contenu(l1, m1["Z"], m1["G"], t1)[6] < len(t0)  # la longueur brute lit le signe
            # aucun nombre court négatif (seul cas où le changement de signe touche un jeton) ; les clés « 0 » et « 1 » des
            # sous-populations sont des nombres courts positifs
            if not any(j[0] == "-" and len(j) > 1 and not AU._nombre_long(j) for j in AU._JETON.findall(t0)):
                longues += 1
                assert np.array_equal(AU.traits_de_forme(t0), AU.traits_de_forme(t1))
    assert changees > 100 and longues > 0.8 * changees
    p0 = AU.audit_presentation(saines_m, np.random.default_rng(28), _rng_permutation(2801), PERMUTATIONS_D_ESSAI)
    p1 = AU.audit_presentation(fautives, np.random.default_rng(28), _rng_permutation(2801), PERMUTATIONS_D_ESSAI)
    assert p1["exactitudes"]["contenu"]["dependantes_contre_independantes"] > 0.55
    assert "contenu/dependantes_contre_independantes" in p1["signalement"] and p1["mention"] == AU.MENTION
    a0, a1 = (p["exactitudes"]["forme"]["dependantes_contre_independantes"] for p in (p0, p1))
    assert abs(a1 - a0) <= 0.03 and "forme/dependantes_contre_independantes" not in set(p1["arret"]) - set(p0["arret"])


def test_garde_25_bornes_de_la_construction_epuisees():
    g = graines()
    for k in range(2):  # bornes gelées, générateur sain : aucun arrêt
        MO.generer_suite(g, dict(couche="essai", famille="bornes-saines", source=k), 0.5)
    with pytest.raises(MO.ArretGenerateur, match="bornes de la construction épuisées"):
        MO.generer_suite(g, dict(couche="essai", famille="bornes-courtes", source=0), 0.5, bornes=MO.Bornes(1, 1, 1))


def test_etape_3_jugement_des_suites_et_arrets(saines):
    """Étape 3, à taille réduite et sous la couche « essai » : le jugement rend le rapport (ou arrête, le rapport joint) avec,
    pour les quinze exactitudes, A, σ₀, la moyenne permutée, les deux seuils et la lecture ; une exactitude non calculable
    (suites d'une seule dose) arrête l'étape. Code v5 (« Ce qui demande un code v5 », point 3) : l'étape dérive elle-même le
    générateur des plis de la lecture observée (rôle « plis ») et celui des permutations (rôle « permutation »), de la couche
    demandée et de la famille « audit » ; elle n'en reçoit aucun de l'appelant ; les exactitudes observées sont celles que
    donnent ces deux générateurs, distincts (artefacts : plis reçus de l'appelant ; plis tirés du générateur des permutations)."""
    import inspect
    c = MO.Compteurs()
    for s in saines:
        c.ajouter(s.compteurs)
    g = graines()
    try:
        rapport = MO.juger_suites_d_audit(saines, c, g, "essai", PERMUTATIONS_D_ESSAI)
        assert rapport["presentation"]["arret"] == []
    except MO.ArretGenerateur as e:
        rapport = e.rapport
        assert rapport["presentation"]["arret"] and "audit du générateur en échec" in str(e)
    _verifier_table(rapport["presentation"], PERMUTATIONS_D_ESSAI)
    assert set(rapport) == {"presentation", "lois_du_final_identiques_a_la_source", "compteurs", "traits_de_contenu"}
    assert g.etiquettes == ["couche=essai|famille=audit|role=plis", "couche=essai|famille=audit|role=permutation"]
    # les exactitudes observées et la table sont celles des deux générateurs dérivés sous leurs rôles, distincts
    g2 = graines()
    attendu = AU.audit_presentation(MO.mondes_pour_l_audit(saines), g2.g(couche="essai", famille="audit", role="plis"),
                                    g2.g(couche="essai", famille="audit", role="permutation"), PERMUTATIONS_D_ESSAI)
    assert rapport["presentation"]["exactitudes"] == attendu["exactitudes"]
    assert rapport["presentation"]["table"] == attendu["table"]
    g3 = graines()
    rng_perm = g3.g(couche="essai", famille="audit", role="permutation")
    meme = AU.audit_presentation(MO.mondes_pour_l_audit(saines), g3.g(couche="essai", famille="audit", role="permutation"),
                                 rng_perm, PERMUTATIONS_D_ESSAI)
    assert meme["exactitudes"] != rapport["presentation"]["exactitudes"]  # l'artefact se distingue
    # aucun générateur reçu de l'appelant, à l'étape 3
    for f in (MO.juger_suites_d_audit, MO.audit_du_generateur):
        assert not any(p.startswith("rng") for p in inspect.signature(f).parameters), f
    with pytest.raises(MO.ArretGenerateur, match="non calculable"):
        MO.juger_suites_d_audit([s for s in saines if s.source.dose == 0.5], c, graines(), "essai", PERMUTATIONS_D_ESSAI)
    g = graines()
    with pytest.raises(MO.ArretGenerateur, match="non calculable"):
        MO.audit_du_generateur(g, (0.0,), 1, permutations=PERMUTATIONS_D_ESSAI, couche="essai")
    assert "couche=essai|famille=audit|role=permutation" in g.etiquettes
    assert "couche=essai|famille=audit|role=plis" in g.etiquettes


def test_marge_face_a_la_source_etrangere():
    """À la dose 0,25 (douze paires sur vingt-huit). À la dose 0,5, vingt-quatre paires sur vingt-huit sont des lois dépendantes
    et la construction, sur les graines « essai » de l'outil de diagnostic, épuise ses bornes : constat porté au rapport."""
    g = graines()
    bases = [dict(couche="essai", famille="etrangere", dose=0.25, source=k) for k in range(3)]
    suites = MO.generer_jeu_avec_etrangeres(g, bases, 0.25)
    for k, s in enumerate(suites):
        e = suites[(k + 1) % 3].source
        assert s.etrangere is e
        for m in s.mondes_cibles():
            assert AU.audit_marges({i: l["loi"] for i, l in m.lois.items()}, m.oracle.Z, m.oracle.G,
                                   s.source.vraies_par_rang(), e.vraies_par_rang()) == []
    # code v5 (garde 27 à trois sources) : la source de construction de la marge est la suivante ; artefact planté, la
    # précédente (à trois sources, elle diffère de la suivante)
    import copy
    assert MO.verifier_etrangeres_du_jeu(suites)
    inversees = [copy.copy(s) for s in suites]
    for k, s in enumerate(inversees):
        s.etrangere = suites[(k - 1) % 3].source
    with pytest.raises(MO.ArretGenerateur, match="garde 27 : la marge"):
        MO.verifier_etrangeres_du_jeu(inversees)
    # sans la construction de B7 bis, la marge face à une source étrangère n'est pas garantie : l'audit la lit
    s0 = MO.generer_suite(g, dict(couche="essai", famille="sans-etrangere", source=0), 0.5)
    lois = {i: l["loi"] for i, l in s0.cibles[0].lois.items()}
    etrangere_fautive = [lois[sorted(lois)[0]]] + suites[0].source.vraies_par_rang()[1:]
    assert AU.audit_marges(lois, s0.cibles[0].oracle.Z, s0.cibles[0].oracle.G, (), etrangere_fautive)


def test_dose_hors_grille_refusee():
    with pytest.raises(MO.ArretGenerateur):
        MO.nombre_de_dependantes(0.3)
    assert [MO.nombre_de_dependantes(d) for d in DOSES] == [0, 3, 6]
    assert len(MO.PAIRES_DE_LA_SOURCE) == 28 == len(list(itertools.combinations(range(8), 2)))
