"""Essais du programme à part de l'audit de symétrie de la ligne 1 (`audit_symetrie_ligne1_v1.py`) — R5 et R4.

Mandat : `mandat-developpeur-programme-audit-symetrie-ligne-1-v1.md` (sha256 310f2a69…5fc44). Addendum 1, version 3
(`fb48a8ab…`), § 2 choix 5 et § 4.2.

Toutes les sorties lues ici sont **fabriquées par ces essais** : sorties d'étalonnage écrites à la main (aires connues), et
courses décisives jouées par le banc sur la **racine des essais 2026111900 seule**, avec les paramètres d'essai de la
configuration. Aucune sortie de course réelle n'est lue. Aucune graine des racines 2026111901 à 2026111903 n'est dérivée
(dernier essai, `test_zz_…`).

Lancer depuis `code/` : `BANC_L1_ORGANISME=<orchestrator> PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q -p no:cacheprovider
essais/test_audit_symetrie_ligne1_v1.py`.
"""

import copy
import json
import lzma
import os
import sys

import numpy as np
import pytest

CODE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CODE)
sys.dont_write_bytecode = True

import banc_ligne1_v1 as B  # noqa: E402
import journal_ligne1_v1 as JL  # noqa: E402
import etalonnage_ligne1_v2 as E  # noqa: E402
import rejouer_journal_ligne1_v2 as RJ  # noqa: E402
import audit_symetrie_ligne1_v1 as AS  # noqa: E402

ORGANISME = os.environ.get("BANC_L1_ORGANISME", "/home/user/ideation-organism/orchestrator")
CONFIG, SHA_CONFIG = B.charger_configuration(E.CHEMIN_CONFIGURATION)
RACINE = CONFIG["racines"]["essais"]
INTERDITES = {CONFIG["racines"][k] for k in ("etalonnage", "decisive", "reechantillonnage")}
B.charger_organisme(ORGANISME, CONFIG)
PE = CONFIG["parametres_essais"]
P = B.parametres(CONFIG, PE["forces"], PE["s"], PE["c"])
CLASSES = ("peu", "beaucoup")
N_ETAL = 8                        # courses d'étalonnage fabriquées
COURSES_SYM = CONFIG["audit_symetrie"]["courses"]   # 0, 300, 599 (configuration v2)


def config_essai():
    """Configuration v2, racine de rééchantillonnage remplacée par la racine des essais (seule admise en mode essai)."""
    c = copy.deepcopy(CONFIG)
    c["racines"]["reechantillonnage"] = RACINE
    return c


CONF = config_essai()
SHA_ESSAI = JL.empreinte(CONF)
LIGNEES = [{"l": l, "a_effet": l < 4,
            "role": ("vraie_forte" if l == 0 else "vraie_faible") if l < 4 else ("fausse_diffuse" if l < 6 else "fausse_tranchante")}
           for l in range(8)]


# --- fabrication -------------------------------------------------------------------------------------------------------------
def cartes_fabriquees(graine="essai-audit|fabrique"):
    """Cartes fabriquées (racine des essais) : {classe: {course: [carte]}} ; carte = {l, premier, emp, et, type} ; `et` vaut
    None pour une carte non jugée."""
    rng = np.random.default_rng(B.GRAINES(RACINE, graine))
    out = {}
    for k in CLASSES:
        out[k] = {}
        for course in range(N_ETAL):
            cs = []
            for _ in range(14):
                l = int(rng.integers(0, 8))
                if rng.random() < 0.2:
                    et = None
                elif l < 4:
                    et = str(rng.choice(["vraie", "vraie", "indeterminee", "fausse"]))
                else:
                    et = str(rng.choice(["fausse", "fausse", "indeterminee"]))
                cs.append({"l": l, "premier": int(rng.integers(1, 40)), "emp": f"{int(rng.integers(0, 2**32)):08x}" + "0" * 56,
                           "et": et, "type": "transformee" if rng.random() < 0.9 else "si_sinon"})
            out[k][course] = cs
    return out


def sortie_etalonnage_fabriquee(course, classe, cartes):
    recs, jug = [], {}
    for j, c in enumerate(cartes):
        i = f"c{course:04d}-{classe}-x{j:03d}"
        juge = c["et"] is not None
        recs.append({"id": i, "l": c["l"], "g": 1, "rang": j + 1, "type": c["type"], "empreinte": c["emp"], "mots": 11,
                     "caracteres": 60, "premier_essai_appel": c["premier"], "refus": None if juge else "quota", "jugee": juge})
        if juge:
            jug[i] = {"l": c["l"], "g": 1, "verite": {"etiquette": c["et"]}}
    return {"course": course, "classe": classe, "lignees": LIGNEES, "receptions": recs, "jugements": jug,
            "appels": [{"jugees": len(jug)}],
            "bras": {"T0": {"generations": [{"g": 1, "promues": [], "en_course": list(range(8))}]}}}


def ecrire_etalonnage(dossier, cartes, config=CONF, sha=SHA_ESSAI, alterer_audit=False):
    """Écrit un étalonnage fabriqué : sorties de courses scellées, puis la sortie de l'étalonnage avec la porte de l'audit
    calculée **par le chemin du code v2** (`lire_courses` puis `audit_generateur`, comme `etalonner`). Rend son chemin."""
    dc = os.path.join(dossier, "courses")
    os.makedirs(dc, exist_ok=True)
    for k in CLASSES:
        for course in range(N_ETAL):
            B.ecrire_json_xz_scelle(os.path.join(dc, f"sortie-c{course:04d}-{k}.json.xz"),
                                    sortie_etalonnage_fabriquee(course, k, cartes[k][course]))
    lu = E.lire_courses(dc, N_ETAL, CLASSES, config)
    audit = {k: E.audit_generateur(lu["cartes"][k], list(range(N_ETAL)), config, config["racines"]["reechantillonnage"], k)
             for k in CLASSES}
    if alterer_audit:
        audit["peu"]["aires"]["effet"]["identifiant"]["borne_basse"] += 1e-9
    fichiers = {n: B.sha256_fichier(os.path.join(dc, n)) for n in sorted(os.listdir(dc)) if n.endswith(".xz")}
    etal = {"version": "etalonnage-fabrique-essai", "configuration_sha256": sha, "code": {"fichiers": AS.code_sur_disque()},
            "racines": {"etalonnage": RACINE, "reechantillonnage": config["racines"]["reechantillonnage"]},
            "courses": {"par_classe": N_ETAL, "dossier": "courses", "fichiers": fichiers}, "audit_generateur": audit,
            "portes_bloquantes": False}
    chemin = os.path.join(dossier, E.NOM_SORTIE)
    B.ecrire_json_scelle(chemin, etal)
    return chemin


@pytest.fixture(scope="module")
def courses_decisives(tmp_path_factory):
    """Courses 0, 300, 599 jouées par le banc, tous bras, racine des essais (sorties fabriquées par l'essai)."""
    d = str(tmp_path_factory.mktemp("decisive-essai"))
    dc = os.path.join(d, "courses")
    os.makedirs(dc)
    for c in COURSES_SYM:
        B.jouer_course(c, RACINE, P, dc, SHA_ESSAI, None)
    return dc


def monter(tmp, courses_decisives, cartes=None, alterer_audit=False, sha=SHA_ESSAI):
    """Monte un run fabriqué dans `tmp` : copie des courses décisives, étalonnage fabriqué, manifeste décisif scellé. Rend
    (chemin du manifeste, son empreinte)."""
    racine = str(tmp)
    dd = os.path.join(racine, "decisive", "courses")
    os.makedirs(dd)
    for n in os.listdir(courses_decisives):
        with open(os.path.join(courses_decisives, n), "rb") as f, open(os.path.join(dd, n), "wb") as g:
            g.write(f.read())
    chemin_e = ecrire_etalonnage(os.path.join(racine, "etalonnage"), cartes or cartes_fabriquees(), alterer_audit=alterer_audit)
    return ecrire_manifeste(os.path.join(racine, "decisive"), chemin_e, sha)


def ecrire_manifeste(dossier_decisif, chemin_e, sha=SHA_ESSAI, nom=None):
    dd = os.path.join(dossier_decisif, "courses")
    fichiers = {n: {"sha256": B.sha256_fichier(os.path.join(dd, n))} for n in sorted(os.listdir(dd)) if n.endswith(".xz")}
    m = {"version": "manifeste-fabrique-essai", "configuration_sha256": sha, "code": AS.code_sur_disque(),
         "etalonnage": {"chemin": chemin_e, "sha256": B.sha256_fichier(chemin_e)}, "courses": list(COURSES_SYM),
         "fichiers": fichiers}
    chemin = os.path.join(dossier_decisif, nom or "manifeste-course-decisive-ligne1-v2.json")
    B.ecrire_json_scelle(chemin, m)
    return chemin, B.sha256_fichier(chemin)


def executer(chemin_m, sha_m, vers, **k):
    return AS.executer("essai", CONF, SHA_ESSAI, chemin_m, sha_m, str(vers), **k)


def lire_cr(chemin):
    return B.lire_json_verifie(chemin)


# --- références indépendantes ------------------------------------------------------------------------------------------------
def aire_paires(xs, ys, poids=None):
    """Aire sous la courbe par comptage des paires (ex æquo pour moitié), pondérée : référence indépendante de
    `auc_ponderee`."""
    xs, ys = np.asarray(xs, float), np.asarray(ys, float)
    w = np.ones(len(xs)) if poids is None else np.asarray(poids, float)
    p, n = ys == 1, ys == 0
    xp, xn, wp, wn = xs[p], xs[n], w[p], w[n]
    gt = (xp[:, None] > xn[None, :]).astype(float) + 0.5 * (xp[:, None] == xn[None, :])
    den = wp.sum() * wn.sum()
    return float((wp[:, None] * wn[None, :] * gt).sum() / den)


def references(cartes_k, n, R, racine, classe, percentiles=(2.5, 97.5)):
    """Aires des traits seuls (étiquette d'effet) et intervalles, recalculés hors du code : tirages refaits depuis la
    graine de tâche de l'organisme (`etalonnage|audit|classe=<classe>`), aire par paires."""
    arr = [c for c in cartes_k if c[5] is not None]
    y = [c[5] for c in arr]
    ic = np.array([c[0] for c in arr])
    rng = np.random.default_rng(B.BF.graine_de_tache(racine, f"etalonnage|audit|classe={classe}"))
    tirages = [np.bincount(rng.integers(0, n, size=n), minlength=n) for _ in range(R)]
    out = {}
    for t, j in (("identifiant", 1), ("rang_lignee", 2), ("premier_essai_appel", 3)):
        x = [c[j] for c in arr]
        boot = [aire_paires(x, y, t_[ic]) for t_ in tirages]
        bas, haut = np.percentile(boot, percentiles)
        out[t] = {"valeur": aire_paires(x, y), "borne_basse": float(bas), "borne_haute": float(haut)}
    return out


def cartes_et_audit(cartes):
    """Cartes sous les deux conventions (lecteur du programme) et porte de l'audit (code v2) sur un dossier fabriqué."""
    import tempfile
    d = tempfile.mkdtemp(dir=os.environ.get("TMPDIR"))
    chemin = ecrire_etalonnage(d, cartes)
    etal = B.lire_json_verifie(chemin)
    lues, _ = AS.lire_cartes_etalonnage(os.path.join(d, "courses"), N_ETAL, CLASSES, etal["courses"]["fichiers"])
    return lues, etal, d


# ================================ 1. complément du choix 5 ===================================================================
def test_complement_cas_sain_aires_connues_cas_ecrit_a_la_main():
    """Cas écrit à la main, une seule course et une seule classe : vraies aux identifiants 3 et 4, fausses à 1 et 2,
    une indéterminée à 5, une non jugée à 0. Porte (indéterminée hors) : 4/4 = 1 ; complément (indéterminée comptée non
    vraie) : 4/6 = 0,666… ; la non jugée ne compte dans aucune des deux."""
    def c(ident, eff):
        return (0, ident, 0, 7, ident % 2, eff)       # étiquette de conception alternée : les deux classes présentes
    porte = [c(3, 1), c(4, 1), c(1, 0), c(2, 0), c(5, None), c(0, None)]
    comp = [c(3, 1), c(4, 1), c(1, 0), c(2, 0), c(5, 0), c(0, None)]
    conf = copy.deepcopy(CONF)
    conf["audit"]["reechantillons"] = 20
    scelle = {"peu": E.audit_generateur(porte, [0], conf, RACINE, "peu")}
    out = AS.complement_choix_5({"peu": {"porte": porte, "complement": comp, "comptes": {}}}, 1, conf, RACINE, ("peu",), scelle)
    t = out["par_classe"]["peu"]
    assert t["porte_recalculee"]["traits_seuls"]["identifiant"]["valeur"] == 1.0
    assert t["traits_seuls"]["identifiant"]["valeur"] == pytest.approx(4 / 6, abs=1e-15)
    assert t["traits_seuls"]["rang_lignee"]["valeur"] == 0.5 and t["traits_seuls"]["premier_essai_appel"]["valeur"] == 0.5


def test_complement_cas_sain_aires_et_intervalles_connus():
    """Sorties fabriquées (8 courses par classe, cartes jugées vraies, fausses, indéterminées, non jugées, et quelques
    `si_sinon`) : aires et intervalles du complément égaux à une référence indépendante (aire par paires, tirages refaits
    depuis la graine de la tâche de la porte) ; porte recalculée égale, au bit près, à celle de la sortie scellée."""
    cartes = cartes_fabriquees()
    lues, etal, _ = cartes_et_audit(cartes)
    out = AS.complement_choix_5(lues, N_ETAL, CONF, RACINE, CLASSES, etal["audit_generateur"])
    R = CONF["audit"]["reechantillons"]
    for k in CLASSES:
        comptes = lues[k]["comptes"]
        assert comptes["indeterminees"] > 0 and comptes["non_jugees"] > 0 and comptes["vraies"] > 0 and comptes["fausses"] > 0
        # références tirées de la seule spécification des cartes fabriquées, sans le lecteur du programme
        spec = [(course, int(co["emp"][:8], 16), co["l"], co["premier"], int(co["l"] < 4), co["et"])
                for course in range(N_ETAL) for co in cartes[k][course] if co["type"] == "transformee"]
        assert comptes["transformee"] == len(spec) and comptes["indeterminees"] == sum(x[5] == "indeterminee" for x in spec)
        ref_c = references([x[:5] + (None if x[5] is None else int(x[5] == "vraie"),) for x in spec], N_ETAL, R, RACINE, k)
        ref_p = references([x[:5] + ({"vraie": 1, "fausse": 0}.get(x[5]),) for x in spec], N_ETAL, R, RACINE, k)
        for t in AS.TRAITS_SEULS:
            for x in ("valeur", "borne_basse", "borne_haute"):
                assert out["par_classe"][k]["traits_seuls"][t][x] == pytest.approx(ref_c[t][x], abs=1e-12)
                assert out["par_classe"][k]["porte_recalculee"]["traits_seuls"][t][x] == pytest.approx(ref_p[t][x], abs=1e-12)
        # les deux conventions diffèrent bien sur ces données (sinon l'essai ne distinguerait rien)
        assert out["par_classe"][k]["traits_seuls"] != {t: dict(v, intervalle_tout_entier_hors_plage=False) for t, v in
                                                        out["par_classe"][k]["porte_recalculee"]["traits_seuls"].items()}


def test_complement_lecteur_egal_a_lire_courses_du_code_v2():
    """Les cartes de la convention de la porte lues par le programme sont, à l'ordre près, celles de
    `etalonnage_ligne1_v2.lire_courses` ; celles du complément n'en diffèrent que par les indéterminées jugées (0)."""
    cartes = cartes_fabriquees()
    lues, _, d = cartes_et_audit(cartes)
    lu = E.lire_courses(os.path.join(d, "courses"), N_ETAL, CLASSES, CONF)
    for k in CLASSES:
        assert lues[k]["porte"] == lu["cartes"][k]
        diff = [(p, c) for p, c in zip(lues[k]["porte"], lues[k]["complement"]) if p != c]
        assert len(diff) == lues[k]["comptes"]["indeterminees"]
        assert all(p[5] is None and c[5] == 0 and p[:5] == c[:5] for p, c in diff)


def test_complement_memes_reechantillons_que_la_porte():
    """Les rééchantillons du complément sont ceux de la porte du code v2 pour la même classe : même racine, même tâche
    (`etalonnage|audit|classe=<classe>`), même graine, et mêmes tirages, tirage par tirage (interception de
    `numpy.random.default_rng`)."""
    cartes = cartes_fabriquees()
    lues, _, _ = cartes_et_audit(cartes)
    vu = {"graines": [], "rng": []}
    vrai_rng, vraies_graines = np.random.default_rng, B.GRAINES

    class Espion:
        def __init__(self, g):
            self._r, self.tirages = vrai_rng(g), []
            vu["rng"].append((g, self.tirages))

        def integers(self, *a, **k):
            x = self._r.integers(*a, **k)
            self.tirages.append(x.copy())
            return x

    def graines(racine, tache):
        g = vraies_graines(racine, tache)
        vu["graines"].append((racine, tache, g))
        return g

    for k in CLASSES:
        scelle = {k: E.audit_generateur(lues[k]["porte"], list(range(N_ETAL)), CONF, RACINE, k)}
        vu["graines"].clear()
        vu["rng"].clear()
        np.random.default_rng, B.GRAINES = Espion, graines
        try:
            E.audit_generateur(lues[k]["porte"], list(range(N_ETAL)), CONF, RACINE, k)          # la porte (code v2)
            n_porte = (len(vu["graines"]), len(vu["rng"]))
            AS.complement_choix_5({k: lues[k]}, N_ETAL, CONF, RACINE, (k,), scelle)
        finally:
            np.random.default_rng, B.GRAINES = vrai_rng, vraies_graines
        g_porte, rng_porte = vu["graines"][0], vu["rng"][0]
        assert g_porte[:2] == (RACINE, f"etalonnage|audit|classe={k}")
        # le complément : appel de la porte recalculée, puis appel du complément ; leurs premières graines et leurs
        # premiers générateurs (traits seuls) sont ceux de la porte
        derives = [g for g in vu["graines"][n_porte[0]:] if g[1] == f"etalonnage|audit|classe={k}"]
        gens = [r for r in vu["rng"][n_porte[1]:] if r[0] == g_porte[2]]
        assert len(derives) == 2 and all(g == g_porte for g in derives)        # recalcul de la porte, complément
        assert len(gens) == 2 and len(rng_porte[1]) == CONF["audit"]["reechantillons"]
        for _, tir in gens:
            assert len(tir) == len(rng_porte[1]) and all(np.array_equal(a, b) for a, b in zip(tir, rng_porte[1]))


def test_complement_artefact_indeterminee_deplacee():
    """Artefact : une carte indéterminée déplacée vers le plus petit identifiant. Sous la porte (indéterminée hors), rien ne
    change ; sous le complément (indéterminée comptée non vraie), l'aire de l'identifiant **monte** (une non vraie de plus
    sous toutes les vraies), de la quantité exacte que donne le comptage des paires."""
    cartes = cartes_fabriquees()
    lues, etal, _ = cartes_et_audit(cartes)
    k = "peu"
    avant = AS.complement_choix_5(lues, N_ETAL, CONF, RACINE, CLASSES, etal["audit_generateur"])["par_classe"][k]
    # déplacer l'indéterminée jugée de plus grand identifiant
    cand = [(c, co) for c in range(N_ETAL) for co in cartes[k][c] if co["et"] == "indeterminee" and co["type"] == "transformee"]
    course, carte = max(cand, key=lambda x: int(x[1]["emp"][:8], 16))
    carte["emp"] = "00000000" + "0" * 56
    lues2, etal2, _ = cartes_et_audit(cartes)
    apres = AS.complement_choix_5(lues2, N_ETAL, CONF, RACINE, CLASSES, etal2["audit_generateur"])["par_classe"][k]
    assert apres["porte_recalculee"]["traits_seuls"] == avant["porte_recalculee"]["traits_seuls"]
    assert apres["traits_seuls"]["identifiant"]["valeur"] > avant["traits_seuls"]["identifiant"]["valeur"]
    ref = references(lues2[k]["complement"], N_ETAL, CONF["audit"]["reechantillons"], RACINE, k)
    assert apres["traits_seuls"]["identifiant"]["valeur"] == pytest.approx(ref["identifiant"]["valeur"], abs=1e-12)
    for t in ("rang_lignee", "premier_essai_appel"):
        assert apres["traits_seuls"][t] == avant["traits_seuls"][t]


def test_complement_artefacts_etiquettes_et_non_jugees():
    """Une indéterminée relabellisée « fausse » : le complément ne bouge pas (non vraie dans les deux cas), la porte bouge.
    Une indéterminée relabellisée « vraie » : le complément bouge. Une carte non jugée à un trait extrême : ni la porte ni
    le complément ne bougent (hors de l'étiquette d'effet dans les deux conventions)."""
    cartes = cartes_fabriquees()
    lues, etal, _ = cartes_et_audit(cartes)
    base = AS.complement_choix_5(lues, N_ETAL, CONF, RACINE, CLASSES, etal["audit_generateur"])["par_classe"]["peu"]

    def rejouer(modifier):
        cs = copy.deepcopy(cartes)
        modifier(cs)
        l2, e2, _ = cartes_et_audit(cs)
        return AS.complement_choix_5(l2, N_ETAL, CONF, RACINE, CLASSES, e2["audit_generateur"])["par_classe"]["peu"]

    def premiere(cs, et):
        return next(co for c in range(N_ETAL) for co in cs["peu"][c] if co["et"] == et and co["type"] == "transformee")

    f = rejouer(lambda cs: premiere(cs, "indeterminee").update(et="fausse"))
    assert f["traits_seuls"] == base["traits_seuls"] and f["porte_recalculee"]["traits_seuls"] != base["porte_recalculee"]["traits_seuls"]
    v = rejouer(lambda cs: premiere(cs, "indeterminee").update(et="vraie"))
    assert v["traits_seuls"] != base["traits_seuls"]

    def extreme(cs):
        co = premiere(cs, None)
        co.update(emp="ffffffff" + "0" * 56, premier=10 ** 6)
    nj = rejouer(extreme)
    assert nj["traits_seuls"] == base["traits_seuls"]
    assert nj["porte_recalculee"]["traits_seuls"] == base["porte_recalculee"]["traits_seuls"]


def test_complement_intervalle_hors_plage_nomme_sans_arret():
    """Un complément dont un intervalle est tout entier hors de [0,45 ; 0,55] est nommé, et rien n'est levé (descriptif,
    sans porte) ; un intervalle qui touche la plage n'est pas nommé."""
    def c(course, ident, eff):
        return (course, ident, 0, 7, int(ident % 3 == 0), eff)    # les deux étiquettes de conception dans chaque course
    porte = ([c(i % 4, 10 + i, 1) for i in range(20)] + [c(0, 2, 1)] + [c(i % 4, i, 0) for i in range(10)] + [c(1, 25, 0)]
             + [c(i % 4, i, None) for i in range(10)])
    comp = [x if x[5] is not None else x[:5] + (0,) for x in porte]
    conf = copy.deepcopy(CONF)
    conf["audit"]["reechantillons"] = 50
    scelle = {"peu": E.audit_generateur(porte, list(range(4)), conf, RACINE, "peu")}
    out = AS.complement_choix_5({"peu": {"porte": porte, "complement": comp, "comptes": {}}}, 4, conf, RACINE, ("peu",), scelle)
    t = out["par_classe"]["peu"]
    assert "identifiant" in t["intervalles_tout_entiers_hors_plage"]
    assert "rang_lignee" not in t["intervalles_tout_entiers_hors_plage"]


def test_recalcul_de_la_porte_cas_sain_et_artefact():
    """Cas sain : la porte recalculée égale la sortie scellée. Artefact : une borne de la sortie scellée déplacée de 1e-9
    → `RecalculPorteDifferent` (les rééchantillons ou les cartes ne seraient pas les mêmes)."""
    lues, etal, _ = cartes_et_audit(cartes_fabriquees())
    AS.complement_choix_5(lues, N_ETAL, CONF, RACINE, CLASSES, etal["audit_generateur"])
    faux = copy.deepcopy(etal["audit_generateur"])
    faux["beaucoup"]["aires"]["conception"]["rang_lignee"]["borne_haute"] += 1e-9
    with pytest.raises(AS.RecalculPorteDifferent):
        AS.complement_choix_5(lues, N_ETAL, CONF, RACINE, CLASSES, faux)
    with pytest.raises(AS.RecalculPorteDifferent):
        AS.complement_choix_5(lues, N_ETAL, CONF, RACINE, CLASSES, {"peu": etal["audit_generateur"]["peu"]})


def test_lecteur_artefacts_nom_absent_et_course_deplacee():
    cartes = cartes_fabriquees()
    _, etal, d = cartes_et_audit(cartes)
    dc = os.path.join(d, "courses")
    attendus = dict(etal["courses"]["fichiers"])
    attendus.pop("sortie-c0003-peu.json.xz")
    with pytest.raises(AS.EmpreinteDifferente):
        AS.lire_cartes_etalonnage(dc, N_ETAL, CLASSES, attendus)
    # une sortie de la course 2 écrite sous le nom de la course 3 (scellée, citée) : refus
    os.remove(os.path.join(dc, "sortie-c0003-peu.json.xz"))
    os.remove(os.path.join(dc, "sortie-c0003-peu.json.xz.sha256"))
    B.ecrire_json_xz_scelle(os.path.join(dc, "sortie-c0003-peu.json.xz"), sortie_etalonnage_fabriquee(2, "peu", cartes["peu"][2]))
    attendus = {n: B.sha256_fichier(os.path.join(dc, n)) for n in os.listdir(dc) if n.endswith(".xz")}
    with pytest.raises(AS.IncoherenceDesEntrees):
        AS.lire_cartes_etalonnage(dc, N_ETAL, CLASSES, attendus)


# ================================ 2. recoupement de M1-nul ====================================================================
def test_recoupement_cas_sain_concordant(courses_decisives, tmp_path):
    """Journal et sortie brute des courses 0, 300, 599 jouées par le banc (racine des essais) : « concordant », pour chaque
    bras, chaque course et chaque classe ; les quatre lectures rendent le même (V, R) ; au moins un bras promeut."""
    chemin_m, sha_m = monter(tmp_path / "run", courses_decisives)
    cr, man = executer(chemin_m, sha_m, tmp_path / "sortie")
    r = lire_cr(cr)["recoupement_m1_nul"]
    assert r["mot"] == "concordant" and r["desaccords"] == []
    assert [(x["course"], x["classe"]) for x in r["par_course"]] == [(c, k) for c in COURSES_SYM for k in CLASSES]
    assert COURSES_SYM == [0, 300, 599]
    promotions = 0
    for x in r["par_course"]:
        assert x["mot"] == "concordant" and sorted(x["bras"]) == sorted(B.BRAS)
        for b in x["bras"].values():
            assert b["mot"] == "concordant" and len({(v["V"], v["R"]) for v in b["lectures"].values()}) == 1
            promotions += b["lectures"]["journal_decisions_d_arret"]["R"]
    assert promotions > 0
    # sorties scellées ; on n'écrase jamais
    assert B.verifier_scelle_fichier(cr) and B.verifier_scelle_fichier(man)
    m = B.lire_json_verifie(man)
    assert m["graines"]["racines_derivees"] == [RACINE]
    assert {d["tache"] for d in m["graines"]["derivees"]} >= {f"etalonnage|audit|classe={k}" for k in CLASSES}
    assert m["configuration"]["sha256"] == SHA_ESSAI and m["compte_rendu"]["sha256"] == B.sha256_fichier(cr)
    with pytest.raises(FileExistsError):
        executer(chemin_m, sha_m, tmp_path / "sortie")


def test_complement_dans_le_run_entier(courses_decisives, tmp_path):
    """Le complément du run entier est celui de l'appel direct sur les mêmes sorties fabriquées."""
    cartes = cartes_fabriquees()
    chemin_m, sha_m = monter(tmp_path / "run", courses_decisives, cartes=cartes)
    cr, _ = executer(chemin_m, sha_m, tmp_path / "sortie")
    comp = lire_cr(cr)["complement_choix_5"]
    lues, etal, _ = cartes_et_audit(cartes)
    direct = AS.complement_choix_5(lues, N_ETAL, CONF, RACINE, CLASSES, etal["audit_generateur"])
    assert JL.canonique(comp) == JL.canonique(json.loads(json.dumps(direct)))
    assert comp["racine"] == RACINE and comp["reechantillons"] == 1000


def _bras_qui_promeut(sortie):
    """Premier bras (hors c, dont la promotion passe par la confirmation) qui promeut une carte."""
    for nom in [b for b in B.BRAS if b != "c"]:
        for g in sortie["bras"][nom]["generations"]:
            if g["promues"]:
                return nom, g["g"], g["promues"][-1]
    raise AssertionError("aucune promotion dans la course d'essai")


def test_recoupement_artefact_promotion_changee_dans_la_sortie_brute(courses_decisives, tmp_path):
    """Artefact : une promotion retirée de la sortie brute (course 300, classe « beaucoup »), sortie rescellée et citée par
    un manifeste neuf (la sortie est cohérente avec son sceau, mais pas avec le journal) → « désaccord », détail nommant le
    bras, et les lectures du journal et de la sortie."""
    chemin_m, _ = monter(tmp_path / "run", courses_decisives)
    dd = os.path.join(os.path.dirname(chemin_m), "courses")
    nom_s = os.path.join(dd, "sortie-c0300-beaucoup.json.xz")
    s = B.lire_json_xz_verifie(nom_s)
    bras, g, carte = _bras_qui_promeut(s)
    gen = next(x for x in s["bras"][bras]["generations"] if x["g"] == g)
    gen["promues"].remove(carte)
    os.remove(nom_s)
    os.remove(nom_s + ".sha256")
    B.ecrire_json_xz_scelle(nom_s, s)
    chemin_m2, sha_m2 = ecrire_manifeste(os.path.dirname(chemin_m), B.lire_json_verifie(chemin_m)["etalonnage"]["chemin"],
                                         nom="manifeste-artefact.json")
    cr, _ = executer(chemin_m2, sha_m2, tmp_path / "sortie")
    r = lire_cr(cr)["recoupement_m1_nul"]
    assert r["mot"] == "désaccord"
    assert [(x["course"], x["classe"]) for x in r["desaccords"]] == [(300, "beaucoup")]
    x = next(x for x in r["par_course"] if (x["course"], x["classe"]) == (300, "beaucoup"))
    assert x["bras"][bras]["mot"] == "désaccord" and any(d.startswith(f"bras {bras} : (V, R)") for d in x["detail"])
    lec = x["bras"][bras]["lectures"]
    assert lec["journal_decisions_d_arret"]["R"] == lec["sortie_brute_calcul_direct"]["R"] + 1
    assert lec["sortie_brute_fonction_de_l_analyse"]["R"] == lec["sortie_brute_calcul_direct"]["R"]
    assert all(b["mot"] == "concordant" for n, b in x["bras"].items() if n != bras)


def reecrire_journal(chemin, modifier):
    """Réécrit un journal, chaîne d'empreintes refaite (journal cohérent avec son sceau) ; `modifier(ligne)` change une
    ligne en place. Rend vrai si une ligne a été changée."""
    with lzma.open(chemin, "rb") as f:
        lignes = [json.loads(x) for x in f]
    os.remove(chemin)
    os.remove(chemin + ".sha256")
    entete = {k: v for k, v in lignes[0].items() if k not in ("sorte", "version_journal", "precedente", "n")}
    j = JL.Journal(chemin, entete)
    change = False
    for ligne in lignes[1:]:
        ligne = {k: v for k, v in ligne.items() if k not in ("precedente", "n")}
        change = modifier(ligne) or change
        j._ecrire(ligne)
    j.fermer()
    return change


def test_recoupement_artefact_promotion_changee_dans_le_journal(courses_decisives, tmp_path):
    """Artefact : une promotion retirée du journal (décision d'arrêt et décision de promotion, course 0, classe « peu »),
    journal réécrit avec une chaîne valide et cité par un manifeste neuf → « désaccord », avec le détail."""
    chemin_m, _ = monter(tmp_path / "run", courses_decisives)
    dd = os.path.join(os.path.dirname(chemin_m), "courses")
    s = B.lire_json_xz_verifie(os.path.join(dd, "sortie-c0000-peu.json.xz"))
    bras, g, carte = _bras_qui_promeut(s)

    def modifier(ligne):
        if ligne.get("sorte") != "decision" or ligne["partie"] != f"bras={bras}" or ligne["entrees"].get("generation") != g:
            return False
        if ligne["mecanisme"] == "arret":
            ligne["entrees"]["promues"] = [p for p in ligne["entrees"]["promues"] if p[0] != carte]
            return True
        if ligne["mecanisme"] in ("promotion_e_bh", "promotion_bonferroni", "promotion_seule"):
            ligne["sortie"]["promues"] = [p for p in ligne["sortie"]["promues"] if p != carte]
            return True
        return False

    assert reecrire_journal(os.path.join(dd, "journal-c0000-peu.jsonl.xz"), modifier)
    chemin_m2, sha_m2 = ecrire_manifeste(os.path.dirname(chemin_m), B.lire_json_verifie(chemin_m)["etalonnage"]["chemin"],
                                         nom="manifeste-artefact.json")
    cr, _ = executer(chemin_m2, sha_m2, tmp_path / "sortie")
    r = lire_cr(cr)["recoupement_m1_nul"]
    assert r["mot"] == "désaccord" and [(x["course"], x["classe"]) for x in r["desaccords"]] == [(0, "peu")]
    x = r["par_course"][0]
    lec = x["bras"][bras]["lectures"]
    assert x["bras"][bras]["mot"] == "désaccord"
    assert lec["journal_decisions_d_arret"]["R"] + 1 == lec["sortie_brute_fonction_de_l_analyse"]["R"]
    assert lec["journal_decisions_de_promotion"]["R"] + 1 == lec["sortie_brute_calcul_direct"]["R"]


def test_recoupement_promotions_contre_arrets_seuls(courses_decisives):
    """Les deux lectures du journal se distinguent : une décision de promotion changée sans la décision d'arrêt rend
    « désaccord » entre elles (fonction appelée sur le journal lu, sans fichier)."""
    entete, objets, decisions = JL.lire(os.path.join(courses_decisives, "journal-c0599-beaucoup.jsonl.xz"))
    s = B.lire_json_xz_verifie(os.path.join(courses_decisives, "sortie-c0599-beaucoup.json.xz"))
    arret = RJ.m1_nul_depuis_journal(objets, decisions)
    prom = AS.m1_nul_depuis_promotions(objets, decisions)
    assert arret == prom
    assert all(AS.comparer_bras(n, arret, prom, s)["mot"] == "concordant" for n in B.BRAS)
    bras, g, carte = _bras_qui_promeut(s)
    d2 = copy.deepcopy(decisions)
    for d in d2:
        if d["partie"] == f"bras={bras}" and d["mecanisme"].startswith("promotion") and d["entrees"].get("generation") == g \
                and "promues" in d["sortie"]:
            d["sortie"]["promues"] = [p for p in d["sortie"]["promues"] if p != carte]
    prom2 = AS.m1_nul_depuis_promotions(objets, d2)
    assert AS.comparer_bras(bras, arret, prom2, s)["mot"] == "désaccord"


def test_refus_empreinte_fausse(courses_decisives, tmp_path):
    """Empreintes fausses → refus, rien n'est écrit : (a) un octet d'une sortie décisive changé (compagnon refait, manifeste
    non) ; (b) empreinte du manifeste différente de celle donnée ; (c) une sortie d'étalonnage changée, compagnon refait ;
    (d) sortie de l'étalonnage différente de celle du manifeste ; (e) compagnon seul faux."""
    chemin_m, sha_m = monter(tmp_path / "run", courses_decisives)
    dd = os.path.join(os.path.dirname(chemin_m), "courses")
    vers = tmp_path / "sortie"
    # (b)
    with pytest.raises(AS.EmpreinteDifferente):
        executer(chemin_m, "0" * 64, vers)
    # (a)
    ch = os.path.join(dd, "sortie-c0599-peu.json.xz")
    with open(ch, "ab") as f:
        f.write(b"\0")
    with open(ch + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{B.sha256_fichier(ch)}  {os.path.basename(ch)}\n")
    with pytest.raises(AS.EmpreinteDifferente):
        executer(chemin_m, sha_m, vers)
    assert not os.path.exists(vers / AS.NOM_COMPTE_RENDU) and not os.path.exists(vers / AS.NOM_MANIFESTE)
    # (c)
    chemin_m, sha_m = monter(tmp_path / "run2", courses_decisives)
    etal = B.lire_json_verifie(B.lire_json_verifie(chemin_m)["etalonnage"]["chemin"])
    ce = os.path.join(os.path.dirname(B.lire_json_verifie(chemin_m)["etalonnage"]["chemin"]), "courses", "sortie-c0005-beaucoup.json.xz")
    with open(ce, "ab") as f:
        f.write(b"\0")
    with open(ce + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{B.sha256_fichier(ce)}  {os.path.basename(ce)}\n")
    assert etal["courses"]["fichiers"]["sortie-c0005-beaucoup.json.xz"] != B.sha256_fichier(ce)
    with pytest.raises(AS.EmpreinteDifferente):
        executer(chemin_m, sha_m, vers)
    # (d)
    chemin_m, sha_m = monter(tmp_path / "run3", courses_decisives)
    ce = B.lire_json_verifie(chemin_m)["etalonnage"]["chemin"]
    with open(ce, "a", encoding="utf-8") as f:
        f.write(" ")
    with open(ce + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{B.sha256_fichier(ce)}  {os.path.basename(ce)}\n")
    with pytest.raises(AS.EmpreinteDifferente):
        executer(chemin_m, sha_m, vers)
    # (e)
    chemin_m, sha_m = monter(tmp_path / "run4", courses_decisives)
    ch = os.path.join(os.path.dirname(chemin_m), "courses", "journal-c0300-peu.jsonl.xz")
    with open(ch + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{'1' * 64}  {os.path.basename(ch)}\n")
    with pytest.raises(AS.EmpreinteDifferente):
        executer(chemin_m, sha_m, vers)
    assert not os.path.exists(vers)


def test_refus_journal_rompu(courses_decisives, tmp_path):
    """Un journal dont une ligne est ôtée (chaîne rompue), cité par un manifeste neuf (sceau cohérent) → refus."""
    chemin_m, _ = monter(tmp_path / "run", courses_decisives)
    dd = os.path.join(os.path.dirname(chemin_m), "courses")
    ch = os.path.join(dd, "journal-c0300-beaucoup.jsonl.xz")
    with lzma.open(ch, "rb") as f:
        lignes = f.readlines()
    os.remove(ch)
    with lzma.open(ch, "wb", format=lzma.FORMAT_XZ, preset=6) as f:
        f.writelines(lignes[:5] + lignes[6:])
    with open(ch + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{B.sha256_fichier(ch)}  {os.path.basename(ch)}\n")
    chemin_m2, sha_m2 = ecrire_manifeste(os.path.dirname(chemin_m), B.lire_json_verifie(chemin_m)["etalonnage"]["chemin"],
                                         nom="manifeste-artefact.json")
    with pytest.raises(AS.EmpreinteDifferente):
        executer(chemin_m2, sha_m2, tmp_path / "sortie")


def test_refus_porte_scellee_differente_dans_le_run(courses_decisives, tmp_path):
    """Une sortie d'étalonnage scellée dont la porte de l'audit ne se recalcule pas (borne déplacée avant le scellement) →
    `RecalculPorteDifferent`, rien n'est écrit."""
    chemin_m, sha_m = monter(tmp_path / "run", courses_decisives, alterer_audit=True)
    with pytest.raises(AS.RecalculPorteDifferent):
        executer(chemin_m, sha_m, tmp_path / "sortie")
    assert not os.path.exists(tmp_path / "sortie")


def test_refus_organisme_non_charge(courses_decisives, tmp_path, monkeypatch):
    """Cas sain : organisme chargé (tous les essais du run entier). Artefact : organisme non chargé → refus."""
    chemin_m, sha_m = monter(tmp_path / "run", courses_decisives)
    monkeypatch.setattr(B, "ORGANISME", {})
    with pytest.raises(AS.RefusAuditSymetrie):
        executer(chemin_m, sha_m, tmp_path / "sortie")


def test_refus_racine_derivee_hors_du_mode(courses_decisives, tmp_path, monkeypatch):
    """Artefact : le calcul dérive une racine autre que celle du mode (ici 2026111999, disjointe de toutes celles du
    préenregistrement) → `RacineRefusee`, rien n'est écrit ; cas sain : `test_recoupement_cas_sain_concordant`."""
    chemin_m, sha_m = monter(tmp_path / "run", courses_decisives)
    vrai = AS.complement_choix_5

    def complement_qui_derive(*a, **k):
        B.GRAINES(2026111999, "essai|racine-etrangere")
        return vrai(*a, **k)
    monkeypatch.setattr(AS, "complement_choix_5", complement_qui_derive)
    with pytest.raises(AS.RacineRefusee):
        executer(chemin_m, sha_m, tmp_path / "sortie")
    assert not os.path.exists(tmp_path / "sortie")


def test_main_mode_reel_refuse_avant_toute_derivation(courses_decisives, tmp_path):
    """La commande (mode réel seul) sur un run fabriqué : préenregistrement, configuration v2, code, organisme vérifiés ;
    empreinte du manifeste fausse → `EmpreinteDifferente` ; empreinte juste mais configuration d'essai au manifeste →
    `IncoherenceDesEntrees`. Les deux refus tombent avant toute dérivation : la racine 2026111903 n'est pas dérivée."""
    chemin_m, sha_m = monter(tmp_path / "run", courses_decisives)
    args = ["--manifeste", chemin_m, "--organisme", ORGANISME, "--vers", str(tmp_path / "sortie")]
    with pytest.raises(AS.EmpreinteDifferente):
        AS.main(args + ["--manifeste-sha256", "0" * 64])
    with pytest.raises(AS.IncoherenceDesEntrees):
        AS.main(args + ["--manifeste-sha256", sha_m])
    assert not (set(B.GRAINES.premieres) & INTERDITES) and not os.path.exists(tmp_path / "sortie")


# ================================ vérifications d'entrée ======================================================================
def test_verifier_mode_cas_sains_et_artefacts():
    """Mode réel : la configuration v2 réelle (empreinte de l'addendum, racine 2026111903) passe, **sans dériver aucune
    graine** ; empreinte ou racine différente → refus. Mode essai : 2026111900 seule ; 2026111903 → refus."""
    avant = dict(B.GRAINES.premieres)
    assert SHA_CONFIG == AS.CONFIGURATION_SHA256
    assert AS.verifier_mode("reel", CONFIG, SHA_CONFIG) == CONFIG["racines"]["reechantillonnage"]
    with pytest.raises(AS.EmpreinteDifferente):
        AS.verifier_mode("reel", CONFIG, "0" * 64)
    with pytest.raises(AS.RacineRefusee):
        AS.verifier_mode("reel", CONF, SHA_CONFIG)
    assert AS.verifier_mode("essai", CONF, SHA_ESSAI) == RACINE
    with pytest.raises(AS.RacineRefusee):
        AS.verifier_mode("essai", CONFIG, SHA_CONFIG)
    with pytest.raises(ValueError):
        AS.verifier_mode("fumee", CONF, SHA_ESSAI)
    assert dict(B.GRAINES.premieres) == avant


def test_verifier_coherence_cas_sain_et_artefacts():
    code = AS.code_sur_disque()
    man = {"configuration_sha256": SHA_ESSAI, "etalonnage": {"sha256": "e" * 64}, "code": dict(code), "courses": list(COURSES_SYM)}
    etal = {"configuration_sha256": SHA_ESSAI, "code": {"fichiers": dict(code)}, "racines": {"reechantillonnage": RACINE}}
    assert AS.verifier_coherence(CONF, SHA_ESSAI, man, etal, "e" * 64, code)
    for quoi, mod, exc in (
            ("configuration du manifeste", lambda m, e: m.update(configuration_sha256="x"), AS.IncoherenceDesEntrees),
            ("configuration de l'étalonnage", lambda m, e: e.update(configuration_sha256="x"), AS.IncoherenceDesEntrees),
            ("étalonnage cité", lambda m, e: m["etalonnage"].update(sha256="f" * 64), AS.EmpreinteDifferente),
            ("code du manifeste", lambda m, e: m["code"].update({"banc_ligne1_v1.py": "0" * 64}), AS.EmpreinteDifferente),
            ("code de l'étalonnage", lambda m, e: e["code"]["fichiers"].update({"analyse_ligne1_v2.py": "0" * 64}),
             AS.EmpreinteDifferente),
            ("racine", lambda m, e: e["racines"].update(reechantillonnage=2026111903), AS.IncoherenceDesEntrees),
            ("courses", lambda m, e: m.update(courses=[0, 300]), AS.IncoherenceDesEntrees)):
        m2, e2 = copy.deepcopy(man), copy.deepcopy(etal)
        mod(m2, e2)
        with pytest.raises(exc):
            AS.verifier_coherence(CONF, SHA_ESSAI, m2, e2, "e" * 64, code)


def test_code_importe_est_le_code_v2_de_la_configuration():
    """Le programme importe le code v2 aux empreintes de la configuration v2 (et de l'addendum, § 5.1) ; il n'en copie
    aucune fonction : les fonctions reprises sont celles des modules."""
    import lancer_ligne1_v2 as LA
    assert LA.verifier_code_configuration(CONFIG)
    assert AS.code_sur_disque() == {n: CONFIG["code"]["fichiers"][n] for n in E.FICHIERS_CODE if n in CONFIG["code"]["fichiers"]} \
        | {"configuration_ligne1_v2.json": AS.CONFIGURATION_SHA256}
    import inspect
    src = inspect.getsource(AS)
    for f in ("def audit_generateur", "def auc_ponderee", "def m1_nul_depuis_journal", "def mesures_course", "def graine_de_tache"):
        assert f not in src
    assert AS.E.audit_generateur is E.audit_generateur and AS.RJ.m1_nul_depuis_journal is RJ.m1_nul_depuis_journal


def test_zz_aucune_racine_interdite_derivee():
    """Contrôle final (comme le code v2) : la racine des essais a été dérivée ; aucune des racines 2026111901 à 2026111903."""
    assert RACINE in B.GRAINES.premieres
    assert not (set(B.GRAINES.premieres) & INTERDITES)
    assert INTERDITES == {2026111901, 2026111902, 2026111903}
