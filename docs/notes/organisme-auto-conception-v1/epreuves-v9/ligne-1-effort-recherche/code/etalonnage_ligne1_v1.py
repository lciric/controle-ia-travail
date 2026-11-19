"""Étalonnage du banc A, ligne 1 (version 1) — après le scellement, avant la course décisive.

Préenregistrement qui fait foi : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md`,
sha256 523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9 (« Étalonnage », « Audit du générateur », ordre des
gestes 3 à 5 ; gardes A8, A9, A15, A17).

1. Forces : dichotomie sur [0,05 ; 3,0] ; à chaque pas, 1 600 jugements de la loi du monde seule, chacun sur un monde neuf
   tiré à la force du pas, au seuil 1/0,05 sur 200 tirages ; arrêt quand le taux de promotion est à 0,03 de la cible ;
   cible manquée après 10 pas : garde A9.
2. Lois tranchantes : grille s × c ; 4 000 jugements d'une carte seule par couple, en monde sans effet ; le couple au plus
   fort taux de fausse promotion est retenu (ex æquo : plus petit s, puis plus petit c).
3. Courses d'étalonnage : 400 par classe, appariées, jouées en course pleine puis rejouées par le **seul témoin T0** (aucun
   des bras a, b, c, d, a′ n'est calculé : garde A17), journalisées comme les courses décisives.
4. Portes et mesure : prise (A9), part des cartes indéterminées (mesurée, sans porte), cartes jugées par appel (A15), audit
   du générateur (A8).
5. Sortie scellée dans un fichier à part, au nom neuf, qui ne fait que remplir les paramètres que les règles gelées
   déterminent (quatre forces, couple (s, c)) et dire chaque porte passée ou manquée.
"""

import concurrent.futures
import math
import multiprocessing
import os
import time

import numpy as np

import banc_ligne1_v1 as B

VERSION = "etalonnage-ligne1-v1"
NOM_SORTIE = "sortie-etalonnage-ligne1-v1.json"


class GardeA8Audit(B.ArretBanc):
    pass


class GardeA9Etalonnage(B.ArretBanc):
    pass


class GardeA15CartesParAppel(B.ArretBanc):
    pass


_ETAT = {}


# --- 1. forces ---------------------------------------------------------------------------------------------------------------
def dichotomie(taux_de, cible, intervalle, tolerance, pas_max):
    """Rend (force, pas) ; lève `GardeA9Etalonnage` si la cible n'est pas atteinte en `pas_max` pas."""
    bas, haut = intervalle
    pas = []
    for k in range(1, pas_max + 1):
        f = (bas + haut) / 2.0
        taux = taux_de(f, k)
        B.exiger_fini([taux], "taux de promotion de l'étalonnage")
        pas.append({"pas": k, "force": f, "taux": taux})
        if abs(taux - cible) <= tolerance:
            return f, pas
        if taux < cible:
            bas = f
        else:
            haut = f
    raise GardeA9Etalonnage(f"garde A9 : force non atteinte en {pas_max} pas (cible {cible}) : arrêt, retour à la mère")


def _promotion_monde_seul(args):
    cible, k, force, j = args
    P, racine = _ETAT["P"], _ETAT["racine"]
    base = f"etalonnage|force|cible={cible}|pas={k}|jugement={j}"
    loi = B.SP.loi_softmax_aleatoire(B.rng_tache(racine, base + "|monde"), P["K"], P["DIM"], force)
    ev, _ = B.juger_banc(loi, loi, racine, base, P["config"]["juge"], P["K"], P["DIM"])
    return bool(ev["promue"])


def _carte_tranchante_seule(args):
    s, c, j = args
    P, racine = _ETAT["P"], _ETAT["racine"]
    cfg = P["config"]["monde"]
    base = f"etalonnage|grille|s={s}|c={c}|jugement={j}"
    loi_monde = B.monde_sans_effet(B.rng_tache(racine, base + "|monde"), cfg["dirichlet_sans_effet"])
    tranche = B.tirer_tranche(loi_monde, B.rng_tache(racine, base + "|tranche"), cfg["episodes_tranche"], P["DIM"])
    lignee = {"role": "fausse_tranchante", "marginale_tranche": B.marginale_empirique(tranche["issues"], P["K"])}
    Pc = dict(P, s=s, c=c)
    loi = B.variantes(lignee, B.rng_tache(racine, base + "|variante"), 1, Pc)[0]
    ev, _ = B.juger_banc(loi, loi_monde, racine, base, P["config"]["juge"], P["K"], P["DIM"])
    return bool(ev["promue"])


def _carte(executeur, fonction, taches):
    if executeur is None:
        return [fonction(t) for t in taches]
    return list(executeur.map(fonction, taches, chunksize=max(1, len(taches) // 64)))


def etalonner_forces(executeur, journal_etapes):
    P = _ETAT["P"]
    ef = P["config"]["etalonnage"]["forces"]
    cibles = [r["cible"] for r in P["config"]["monde"]["roles"] if r["a_effet"]]
    sortie = {}
    for cible in cibles:
        def taux_de(f, k, cible=cible):
            t = time.perf_counter()
            res = _carte(executeur, _promotion_monde_seul, [(cible, k, f, j) for j in range(ef["jugements_par_pas"])])
            journal_etapes.append({"etape": "force", "cible": cible, "pas": k, "secondes": time.perf_counter() - t})
            return sum(res) / len(res)
        f, pas = dichotomie(taux_de, cible, ef["intervalle"], ef["tolerance"], ef["pas_max"])
        sortie[str(cible)] = {"force": f, "pas": pas}
    return sortie


def etalonner_grille(executeur, journal_etapes):
    cfg = _ETAT["P"]["config"]["etalonnage"]
    couples = []
    for s in cfg["grille_s"]:
        for c in cfg["grille_c"]:
            t = time.perf_counter()
            res = _carte(executeur, _carte_tranchante_seule, [(s, c, j) for j in range(cfg["jugements_par_couple"])])
            journal_etapes.append({"etape": "grille", "s": s, "c": c, "secondes": time.perf_counter() - t})
            couples.append({"s": s, "c": c, "taux": sum(res) / len(res)})
    retenu = sorted(couples, key=lambda x: (-x["taux"], x["s"], x["c"]))[0]
    return {"couples": couples, "retenu": {"s": retenu["s"], "c": retenu["c"], "taux": retenu["taux"]}}


# --- 3. courses d'étalonnage (T0 seul) ----------------------------------------------------------------------------------------
def _course_etalonnage(course):
    E = _ETAT
    with B.contexte_etalonnage():
        r = B.jouer_course(course, E["racine"], E["P"], E["dossier_courses"], E["sha_config"], E["prereg"], bras=("T0",))
    return {"course": course, "fichiers": r["fichiers"], "graines": dict(B.GRAINES.premieres)}


def course_deja_faite(dossier, course, classes):
    noms = [f"{p}-c{course:04d}-{k}.{x}" for k in classes for p, x in (("journal", "jsonl.xz"), ("sortie", "json.xz"))]
    return all(B.verifier_scelle_fichier(os.path.join(dossier, n)) for n in noms)


def nettoyer_partiels(dossier, course):
    for n in os.listdir(dossier):
        if f"-c{course:04d}-" in n and ".partiel" in n:
            os.remove(os.path.join(dossier, n))


def jouer_courses(executeur, dossier, n, fonction, classes):
    """Joue les courses 0..n−1 qui ne sont pas déjà scellées (reprise) ; rend les comptes rendus des courses jouées."""
    a_faire = [c for c in range(n) if not course_deja_faite(dossier, c, classes)]
    for c in a_faire:
        nettoyer_partiels(dossier, c)
    return _carte(executeur, fonction, a_faire)


# --- 4. portes, mesure, audit ---------------------------------------------------------------------------------------------
def m1_t0(s):
    lign = {x["l"]: x for x in s["lignees"]}
    prom = [i for g in s["bras"]["T0"]["generations"] for i in g["promues"]]
    R = len(prom)
    V = sum(1 for i in prom if not lign[s["jugements"][i]["l"]]["a_effet"])
    return V / R if R else 0.0


def bornes_reechantillon(v, R, racine, tache, percentiles):
    v = np.asarray(v, dtype=float)
    B.exiger_fini(v.tolist(), tache)
    n = len(v)
    rng = np.random.default_rng(B.GRAINES(racine, tache))
    idx = rng.integers(0, n, size=(R, n))
    moy = v[idx].mean(axis=1)
    bas, haut = np.percentile(moy, percentiles)
    return {"valeur": float(v.mean()), "borne_basse": float(bas), "borne_haute": float(haut), "reechantillons": R}


def porte_prise(m1_t0_beaucoup, config, racine_r):
    """Porte de prise : borne basse de M1-nul de T0 (classe « beaucoup ») strictement au-dessus de α."""
    e = config["etalonnage"]
    b = bornes_reechantillon(m1_t0_beaucoup, e["reechantillons_prise"], racine_r, "etalonnage|prise|T0|beaucoup",
                             config["reechantillonnage"]["percentiles"])
    b["passee"] = b["borne_basse"] > config["alpha"]
    return b


def porte_cartes_par_appel(par_classe, config):
    ecart = abs(par_classe["peu"] - par_classe["beaucoup"])
    return {"par_classe": par_classe, "ecart": ecart, "seuil": config["etalonnage"]["ecart_max_cartes_par_appel"],
            "passee": ecart <= config["etalonnage"]["ecart_max_cartes_par_appel"]}


def auc_ponderee(inv, nb, etiquettes, poids):
    """Aire sous la courbe par les rangs (ex æquo comptés pour moitié), pondérée par les comptes du rééchantillonnage."""
    pos = np.bincount(inv, weights=poids * etiquettes, minlength=nb)
    neg = np.bincount(inv, weights=poids * (1.0 - etiquettes), minlength=nb)
    sous = np.cumsum(neg) - neg
    den = pos.sum() * neg.sum()
    return float(np.sum(pos * (sous + 0.5 * neg)) / den) if den > 0 else float("nan")


def ajuster_logistique(X, y, iterations=100):
    """Régression logistique (maximum de vraisemblance, méthode de Newton, pas par moindres carrés : traits colinéaires
    admis), traits centrés réduits sur l'échantillon d'ajustement ; rend (moyennes, écarts, coefficients)."""
    mu, sd = X.mean(axis=0), X.std(axis=0)
    sd[sd == 0] = 1.0
    Z = np.column_stack([np.ones(len(X)), (X - mu) / sd])
    w = np.zeros(Z.shape[1])
    for _ in range(iterations):
        p = 0.5 * (1.0 + np.tanh(0.5 * (Z @ w)))      # sigmoïde sans dépassement numérique
        g = Z.T @ (y - p)
        H = (Z * (p * (1 - p))[:, None]).T @ Z
        pas = np.linalg.lstsq(H, g, rcond=None)[0]
        w = w + pas
        if np.max(np.abs(pas)) < 1e-10:
            break
    return mu, sd, w


def predire_logistique(modele, X):
    mu, sd, w = modele
    Z = np.column_stack([np.ones(len(X)), (X - mu) / sd])
    return Z @ w


def audit_generateur(cartes, courses, config, racine_r, classe):
    """Audit (N-073, § 4) sur les cartes `transformee` reçues des courses pleines d'une classe. `cartes` : liste de
    (course, id_num, rang_lignee, premier_essai, conception, effet ∈ {1, 0, None})."""
    a = config["audit"]
    plage = a["plage"]
    arr = np.array([[c[0], c[1], c[2], c[3], c[4], (-1 if c[5] is None else c[5])] for c in cartes], dtype=float)
    course_de = arr[:, 0].astype(int)
    traits = {"identifiant": arr[:, 1], "rang_lignee": arr[:, 2], "premier_essai_appel": arr[:, 3]}
    rng = np.random.default_rng(B.GRAINES(racine_r, f"etalonnage|audit|classe={classe}"))
    tirages = [np.bincount(rng.integers(0, len(courses), size=len(courses)), minlength=len(courses)) for _ in range(a["reechantillons"])]
    pos_course = {c: i for i, c in enumerate(courses)}
    ic = np.array([pos_course[c] for c in course_de])
    sortie = {"cartes": len(cartes), "aires": {}, "nommees_hors_plage": [], "tire": []}
    for etiquette, col, masque in (("conception", 4, np.ones(len(arr), bool)), ("effet", 5, arr[:, 5] >= 0)):
        y = arr[masque, col]
        sortie["aires"][etiquette] = {}
        for nom, x in traits.items():
            xs = x[masque]
            uniq, inv = np.unique(xs, return_inverse=True)
            poids0 = np.ones(len(xs))
            point = auc_ponderee(inv, len(uniq), y, poids0)
            boot = [auc_ponderee(inv, len(uniq), y, t[ic[masque]].astype(float)) for t in tirages]
            bas, haut = np.percentile(boot, a["percentiles"])
            sortie["aires"][etiquette][nom] = {"valeur": point, "borne_basse": float(bas), "borne_haute": float(haut),
                                               "porte": True}
        # régression sur les trois traits : ajustée sur les courses de rang pair, aire sur les courses de rang impair
        X = np.column_stack([traits[n][masque] for n in traits])
        cm = course_de[masque]
        pair, impair = (cm % 2 == 0), (cm % 2 == 1)
        if pair.sum() and impair.sum() and len(set(y[pair])) == 2 and len(set(y[impair])) == 2:
            modele = ajuster_logistique(X[pair], y[pair])
            score = predire_logistique(modele, X[impair])
            uniq, inv = np.unique(score, return_inverse=True)
            yi = y[impair]
            point = auc_ponderee(inv, len(uniq), yi, np.ones(len(yi)))
            impaires = sorted({int(c) for c in cm[impair]})
            pos_i = {c: i for i, c in enumerate(impaires)}
            ici = np.array([pos_i[int(c)] for c in cm[impair]])
            rng_r = np.random.default_rng(B.GRAINES(racine_r, f"etalonnage|audit|classe={classe}|regression|{etiquette}"))
            boot = []
            for _ in range(a["reechantillons"]):
                t = np.bincount(rng_r.integers(0, len(impaires), size=len(impaires)), minlength=len(impaires))
                boot.append(auc_ponderee(inv, len(uniq), yi, t[ici].astype(float)))
            bas, haut = np.percentile(boot, a["percentiles"])
            sortie["aires"][etiquette]["regression_trois_traits"] = {
                "valeur": point, "borne_basse": float(bas), "borne_haute": float(haut), "porte": etiquette == "conception",
                "coefficients": [float(v) for v in modele[2]]}
        else:
            sortie["aires"][etiquette]["regression_trois_traits"] = {"valeur": None, "porte": etiquette == "conception",
                                                                     "note": "une seule étiquette présente"}
    for etiquette, aires in sortie["aires"].items():
        for nom, v in aires.items():
            if v.get("valeur") is None:
                continue
            if v["porte"] and (v["borne_haute"] < plage[0] or v["borne_basse"] > plage[1]):
                sortie["tire"].append(f"{etiquette} / {nom}")
            elif not (plage[0] <= v["valeur"] <= plage[1]):
                sortie["nommees_hors_plage"].append(f"{etiquette} / {nom}")
    return sortie


def lire_courses(dossier, n, classes, config):
    """Lit les sorties scellées des courses d'étalonnage ; rend ce que les portes, la mesure et l'audit demandent."""
    m1 = {k: [] for k in classes}
    par_appel = {k: [] for k in classes}
    ind = {k: [0, 0] for k in classes}
    fausses = {k: [0, 0] for k in classes}
    refus = {k: {} for k in classes}
    cartes = {k: [] for k in classes}
    croisee = {k: {} for k in classes}
    types = {k: {} for k in classes}
    longueurs = {k: set() for k in classes}
    for course in range(n):
        for k in classes:
            s = B.lire_json_xz_verifie(os.path.join(dossier, f"sortie-c{course:04d}-{k}.json.xz"))
            verifier_sortie_sans_bras_interdit(s)
            m1[k].append(m1_t0(s))
            par_appel[k] += [a["jugees"] for a in s["appels"]]
            lign = {x["l"]: x for x in s["lignees"]}
            for i, j in s["jugements"].items():
                ind[k][1] += 1
                ind[k][0] += j["verite"]["etiquette"] == "indeterminee"
                if lign[j["l"]]["a_effet"]:
                    fausses[k][1] += 1
                    fausses[k][0] += j["verite"]["etiquette"] == "fausse"
            for r in s["receptions"]:
                role = lign[r["l"]]["role"]
                cle = f"{role}|{r['refus'] or ('jugee' if r['jugee'] else 'aucun')}"
                refus[k][cle] = refus[k].get(cle, 0) + 1
                conc = "a_effet" if lign[r["l"]]["a_effet"] else "sans_effet"
                types[k][f"{r['type']}|{conc}"] = types[k].get(f"{r['type']}|{conc}", 0) + 1
                longueurs[k].add((r["type"], r["mots"], r["caracteres"]))
                if r["type"] != "transformee":
                    continue
                effet = None
                if r["jugee"]:
                    et = s["jugements"][r["id"]]["verite"]["etiquette"]
                    effet = None if et == "indeterminee" else (1 if et == "vraie" else 0)
                    cc = f"{conc}|{et}"
                    croisee[k][cc] = croisee[k].get(cc, 0) + 1
                cartes[k].append((course, int(r["empreinte"][:8], 16), r["l"], r["premier_essai_appel"],
                                  1 if lign[r["l"]]["a_effet"] else 0, effet))
    return {"m1_t0": m1, "par_appel": {k: float(np.mean(v)) for k, v in par_appel.items()},
            "indeterminees": {k: {"indeterminees": v[0], "jugees": v[1], "part": v[0] / v[1] if v[1] else 0.0}
                              for k, v in ind.items()},
            "fausses_oracle_a_effet": {k: {"fausses": v[0], "jugees": v[1], "part": v[0] / v[1] if v[1] else 0.0}
                                       for k, v in fausses.items()},
            "refus": refus, "cartes": cartes, "croisee": croisee, "types": types,
            "longueurs": {k: sorted(v) for k, v in longueurs.items()}}


# --- A17 ------------------------------------------------------------------------------------------------------------------
def verifier_sortie_sans_bras_interdit(objet):
    """Garde A17 : aucune décision d'un des bras a, b, c, d, a′ (ni d-E*) dans ce que produit l'étalonnage."""
    if isinstance(objet, dict):
        bras = objet.get("bras")
        if isinstance(bras, dict):
            interdits = sorted(set(bras) & set(B.BRAS_INTERDITS_A_L_ETALONNAGE))
            if interdits:
                raise B.GardeA17BrasEtalonnage(f"garde A17 : la sortie de l'étalonnage contient le(s) bras {interdits} : "
                                               "étalonnage invalide")
        for v in objet.values():
            verifier_sortie_sans_bras_interdit(v)
    elif isinstance(objet, list):
        for v in objet:
            verifier_sortie_sans_bras_interdit(v)
    return True


# --- étalonnage entier ------------------------------------------------------------------------------------------------------
def etalonner(dossier, config, sha_config, prereg, processus=1, portes_bloquantes=True, code=None):
    """Étalonnage entier, reprenable. Écrit `sortie-etalonnage-ligne1-v1.json` (scellée) puis lève la garde nommée si une
    porte est manquée. `portes_bloquantes=False` n'est admis que par l'essai de fumée (racines disjointes de celles du
    préenregistrement, vérifié par le lanceur) : les portes y sont calculées et écrites sans arrêter la chaîne."""
    t0 = time.perf_counter()
    os.makedirs(dossier, exist_ok=True)
    chemin_sortie = os.path.join(dossier, NOM_SORTIE)
    if os.path.exists(chemin_sortie):
        return B.lire_json_verifie(chemin_sortie)
    racine, racine_r = config["racines"]["etalonnage"], config["racines"]["reechantillonnage"]
    B.GRAINES(racine, "ouverture|etalonnage")      # première dérivation consignée par le processus parent (garde A14)
    B.GRAINES(racine_r, "ouverture|etalonnage")
    etapes = []
    n_vraies = sum(1 for r in config["monde"]["roles"] if r["a_effet"])
    # structure seulement (nombre d'issues, de traits, configuration) : aucune de ces valeurs n'entre dans un calcul
    _ETAT.update(P=B.parametres(config, [1.0] * n_vraies, 1.0, 0.6), racine=racine)
    ctx = multiprocessing.get_context("fork")
    ex = concurrent.futures.ProcessPoolExecutor(processus, mp_context=ctx) if processus > 1 else None
    try:
        forces = _reprise(os.path.join(dossier, "etape-forces.json"), lambda: etalonner_forces(ex, etapes))
        grille = _reprise(os.path.join(dossier, "etape-grille.json"), lambda: etalonner_grille(ex, etapes))
    finally:
        if ex:
            ex.shutdown()
    cibles = [r["cible"] for r in config["monde"]["roles"] if r["a_effet"]]
    P = B.parametres(config, [forces[str(c)]["force"] for c in cibles], grille["retenu"]["s"], grille["retenu"]["c"])
    dossier_courses = os.path.join(dossier, "courses")
    os.makedirs(dossier_courses, exist_ok=True)
    n = config["etalonnage"]["courses_par_classe"]
    _ETAT.update(P=P, dossier_courses=dossier_courses, sha_config=sha_config, prereg=prereg)
    classes = tuple(config["proposeurs"]["engagements_par_appel"])
    ex = concurrent.futures.ProcessPoolExecutor(processus, mp_context=ctx) if processus > 1 else None
    t = time.perf_counter()
    try:
        comptes = jouer_courses(ex, dossier_courses, n, _course_etalonnage, classes)
    finally:
        if ex:
            ex.shutdown()
    etapes.append({"etape": "courses", "secondes": time.perf_counter() - t, "jouees": len(comptes)})
    for c in comptes:
        for r, h in c["graines"].items():
            if r not in B.GRAINES.premieres or h < B.GRAINES.premieres[r]:
                B.GRAINES.premieres[r] = h
    lu = lire_courses(dossier_courses, n, classes, config)
    prise = porte_prise(lu["m1_t0"]["beaucoup"], config, racine_r)
    prise_peu = bornes_reechantillon(lu["m1_t0"]["peu"], config["etalonnage"]["reechantillons_prise"], racine_r,
                                     "etalonnage|prise|T0|peu", config["reechantillonnage"]["percentiles"])
    cpa = porte_cartes_par_appel(lu["par_appel"], config)
    audit = {k: audit_generateur(lu["cartes"][k], list(range(n)), config, racine_r, k) for k in classes}
    audit_passe = not any(audit[k]["tire"] for k in classes)
    plafond = config["etalonnage"]["plafond_indeterminees"]
    en_tete = [f"part des cartes indéterminées {lu['indeterminees'][k]['part']:.4f} au-dessus de {plafond} (classe {k}) : "
               "décision de la mère avant la course décisive (la garde A7 refuserait la lecture)"
               for k in classes if lu["indeterminees"][k]["part"] > plafond]
    fichiers = {}
    for nom in sorted(os.listdir(dossier_courses)):
        if nom.endswith(".xz"):
            fichiers[nom] = B.sha256_fichier(os.path.join(dossier_courses, nom))
    sortie = {
        "version": VERSION, "en_tete": en_tete, "preenregistrement": prereg, "configuration_sha256": sha_config,
        "racines": {"etalonnage": racine, "reechantillonnage": racine_r},
        "parametres": {"forces": {str(c): forces[str(c)]["force"] for c in cibles},
                       "forces_dans_l_ordre_des_roles": [forces[str(c)]["force"] for c in cibles],
                       "s": grille["retenu"]["s"], "c": grille["retenu"]["c"]},
        "forces": forces, "grille": grille,
        "portes": {"prise": prise, "cartes_jugees_par_appel": cpa, "audit_generateur": {"passee": audit_passe}},
        "mesures": {"M1_nul_T0_peu": prise_peu, "indeterminees": lu["indeterminees"],
                    "fausses_oracle_a_effet": lu["fausses_oracle_a_effet"], "refus_par_role": lu["refus"],
                    "types_par_conception": lu["types"], "table_croisee_conception_effet": lu["croisee"],
                    "longueurs_de_texte": lu["longueurs"]},
        "audit_generateur": audit,
        "courses": {"par_classe": n, "dossier": "courses", "fichiers": fichiers},
        "graines_premieres_derivations": {str(k): v for k, v in B.GRAINES.premieres.items()},
        "etapes": etapes, "secondes": time.perf_counter() - t0,
        "bras_calcules": ["T0"], "code": code,
    }
    sortie["portes_bloquantes"] = portes_bloquantes
    verifier_sortie_sans_bras_interdit(sortie)
    B.ecrire_json_scelle(chemin_sortie, sortie)
    if not portes_bloquantes:
        return sortie
    exiger_portes(sortie)
    return sortie


def exiger_portes(sortie):
    """Lève la garde nommée de la première porte manquée (A9 prise, A15 cartes jugées par appel, A8 audit)."""
    p = sortie["portes"]
    if not p["prise"]["passee"]:
        raise GardeA9Etalonnage("garde A9 : porte de prise manquée (banc sans prise) : arrêt, retour à la mère")
    if not p["cartes_jugees_par_appel"]["passee"]:
        raise GardeA15CartesParAppel(f"garde A15 : écart entre classes de {p['cartes_jugees_par_appel']['ecart']:.4f} cartes "
                                     f"jugées par appel (seuil {p['cartes_jugees_par_appel']['seuil']}) : arrêt avant la course "
                                     "décisive")
    if not p["audit_generateur"]["passee"]:
        tire = {k: v["tire"] for k, v in sortie.get("audit_generateur", {}).items()}
        raise GardeA8Audit(f"garde A8 : aire(s) dont l'intervalle sort de la plage : {tire} : arrêt, retour à la mère")
    return True


def _reprise(chemin, calcul):
    if os.path.exists(chemin):
        return B.lire_json_verifie(chemin)
    res = calcul()
    B.ecrire_json_scelle(chemin, res)
    return res
