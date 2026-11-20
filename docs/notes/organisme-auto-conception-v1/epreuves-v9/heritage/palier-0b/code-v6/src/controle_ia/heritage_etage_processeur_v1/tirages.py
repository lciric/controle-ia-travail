"""B8 — les cases, les tirages emboîtés, les tirages de confirmation, l'essai de forme (étapes 8 et 9 ; annexe C).

Un tirage est une épreuve entière simulée sur la couche statistique : pour chaque source, une course source, puis les bras de la
famille sur trois générations d'évolution et une génération finale. Tirages emboîtés : chaque tirage simule le plus grand nombre
de sources de sa grille (48, ou 16 à dose nulle), dans un ordre fixe, et la case à k sources lit les k premières. Les sources
sont simulées par lots (annexe F : lot vectorisé de 2 000 sources au plus, multiple de la taille d'un tirage ; chaque lot a son
étiquette de graines) ; la source étrangère d'une source est la suivante du même tirage.

Le moteur écrit, par case, des **sorties brutes scellées** : M1, D, I et lois fausses tenues par bras, tirage et source, et, par
tirage et par nombre de sources, la lecture du tirage (codes) — jamais un taux. Le programme d'analyse (module `analyse`) seul
compte. Les couches « decisif » et « confirmation » exigent une autorisation (module `graines`) : sans elle, la première
dérivation lève et rien n'est tiré. L'essai de forme (annexe C) est borné à 200 tirages par case et deux nombres de sources, sous
la couche « essai-de-forme », et ses sorties le disent dans leur nom.

Code v6 (audit des trous du code v5, « Ce que le code v6 doit porter », points 1 à 4 ; préenregistrement v13, B8, ordre des
opérations, étape 8, et « Ce qui est rapporté ») :
- une case a un **mode**, et exactement une des deux clés : `tirages` (tirages emboîtés, lus tirage par tirage) ou `sources`
  (écarts sur des sources : familles D, E, H et point 6, 200 000 sources, sans lecture par tirage). Le mode « sources » porte un
  champ d'étiquette de plus, `mode=sources` ; aucune étiquette du mode « tirages » ne change (le champ n'y est pas écrit). Le nom
  d'une case du mode « sources » finit par `-sources` : deux cases qui ne diffèrent que par le mode ont deux dossiers ;
- au mode « sources », les sources sont simulées par lots de `LOT_DE_SOURCES` (2 000), chaque lot sous son étiquette (champ
  `lot`) ; la source étrangère d'une source (famille H, bras 4a et 4b) est la suivante du même lot, la première pour la dernière
  (SILENCE : le lot tient lieu du « tirage » de B7 bis dans ce mode ; un lot d'une seule source arrête) ;
- `lancer_famille` suit la clé de chaque case (aucun nombre commun à toutes), contrôle les cases avant l'autorisation et avant
  toute dérivation (`verifier_cases` : une clé et une seule, deux cases jamais au même nom, tailles gelées sous les couches
  décisives, couche « confirmation » réservée aux cases de C1 et de C4), tire toutes les cases d'un lancement, de tous modes, et
  écrit un seul manifeste ;
- les sorties scellées portent aussi, par bras, le **reliquat** de budget (USD simulés, somme sur les quatre générations,
  flottant ; nul par construction sous la règle de retrait de la version 1), et, aux cases du repli au mode « sources »
  (famille D), les comptes du registre de la course source et ce que rend `statistique.enrichissement` (part des entrées
  gardées, facteurs d'enrichissement au grain des entrées et des paires), source par source.
"""

import hashlib
import json
import os
import platform
import time

import numpy as np

from . import rangs_signes as RS
from .constantes import (ESSAI_DE_FORME_MAX_NOMBRES_DE_SOURCES, ESSAI_DE_FORME_MAX_TIRAGES, GRILLE_SOURCES,
                         GRILLE_SOURCES_DOSE_NULLE, LOT_DE_SOURCES, MAX_SOURCES, MAX_SOURCES_DOSE_NULLE, NOMBRES_M13_EN_PLUS,
                         RACINE_GRAINES, REPERE_LECTURE, SOURCES_FAMILLES_GRANDES, TIRAGES_CONFIRMATION, TIRAGES_PAR_CASE,
                         VERSION)
from .graines import COUCHES_DECISIVES
from .statistique import enrichissement, simuler

LECTURES = {"non établi": 0, "établi": 1, "non lu comme succès": 2, "effet négatif établi": 3, "égalité": 4}

# code v6 : les deux modes d'une case (B8 : « tirages » emboîtés ; « sources », écarts sur 200 000 sources)
MODES = ("tirages", "sources")
# code v6 : les sorties brutes par bras et leur type écrit (les comptes en entiers de 16 bits, comme au code v5 ; le reliquat de
# budget, en USD simulés, en flottant de 64 bits)
TYPES_DES_SORTIES = {"M1": np.int16, "D": np.int16, "I": np.int16, "fausses_tenues": np.int16, "reliquat": np.float64}
# code v6 : les sorties du registre de la course source, aux cases du repli au mode « sources » (famille D ; S7, M7) — ses comptes
# (entiers de 64 bits), puis ce que rend `statistique.enrichissement` (flottants de 64 bits ; non défini, NaN, si un dénominateur
# est nul)
COMPTES_DU_REGISTRE_SOURCE = ("entrees", "entrees_gardees", "entrees_vraies", "entrees_vraies_gardees", "lois_vraies_engagees",
                              "lois_fausses_engagees", "lois_non_plantees_engagees", "lois_vraies_gardees",
                              "lois_fausses_gardees", "lois_non_plantees_gardees")
CHAMPS_D_ENRICHISSEMENT = ("part_des_entrees_gardees", "facteur_entrees", "facteur_paires")
# code v6 : ce que la couche « confirmation » tire (C1 : famille A, sourd à appels égaux ; C4 : famille C, les deux sourds)
CASES_DE_CONFIRMATION = (("A", "sourd-egal"), ("C", "sourd-egal"), ("C", "sourd-paie"))


class ArretTirages(RuntimeError):
    pass


def grille_de(dose, avec_m13=False):
    if dose == 0.0:
        return GRILLE_SOURCES_DOSE_NULLE
    return tuple(sorted(set(GRILLE_SOURCES) | (set(NOMBRES_M13_EN_PLUS) if avec_m13 else set())))


def s_max(dose):
    return MAX_SOURCES_DOSE_NULLE if dose == 0.0 else MAX_SOURCES


def mode_de(case):
    """Code v6 : le mode d'une case et son nombre — `("tirages", n)` ou `("sources", n)`. Exactement une des deux clés, et un
    entier positif ; arrêt nommé sinon (aucun nombre commun à toutes les cases n'est plus reçu de l'appelant)."""
    presents = [m for m in MODES if m in case]
    if len(presents) != 1:
        raise ArretTirages(f"case {case.get('famille')}/{case.get('proposeur')} : une et une seule des clés « tirages » et "
                           f"« sources » attendue (reçu {presents}) : arrêt avant tout tirage")
    m = presents[0]
    n = case[m]
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ArretTirages(f"case {case.get('famille')}/{case.get('proposeur')} : nombre de {m} invalide ({n!r}) : arrêt")
    return m, n


def champs_de_la_case(case):
    """Les champs d'étiquette d'une case (B8 : famille, proposeur, dose, taille ou force, taux d'échec, règle, repère).
    Code v6 : le mode « sources » ajoute le champ `mode` ; le mode « tirages » ne l'écrit pas (ses étiquettes sont celles du code
    v5)."""
    c = {"famille": case["famille"], "proposeur": case["proposeur"], "dose": case["dose"], "taux": case["taux"]}
    if case.get("taille") is not None:
        c["taille"] = case["taille"]
    if case.get("force") is not None:
        c["force"] = case["force"]
    if case.get("retrait", "v2") != "v2":
        c["retrait"] = case["retrait"]
    if case.get("repere", REPERE_LECTURE) != REPERE_LECTURE:
        c["repere"] = case["repere"]
    if "sources" in case:
        c["mode"] = "sources"
    if case.get("repli"):
        c["role"] = "repli"
    return c


def simuler_case(graines, couche, case, f, tirages, sources_par_tirage=None, premier_tirage=0):
    """Simule `tirages` tirages d'une case ; rend {clé de bras : {M1, D, I, fausses_tenues, reliquat : (tirages, sources)}}. Les
    graines sont dérivées par lot ; la première dérivation d'une couche décisive sans autorisation lève (liste d'arrêt,
    point 1)."""
    S = sources_par_tirage or s_max(case["dose"])
    par_lot = max(1, LOT_DE_SOURCES // S)
    base = champs_de_la_case(case)
    role_case = base.pop("role", None)
    sorties = {}
    t = 0
    k = premier_tirage // par_lot
    if premier_tirage % par_lot:
        raise ArretTirages("le premier tirage doit commencer un lot")
    while t < tirages:
        n = min(par_lot, tirages - t)
        etiq = dict(couche=couche, **base, lot=k)
        cles = {b: graines.g(**etiq, bras=b, role="echantillonnage" if role_case is None else f"echantillonnage-{role_case}")
                for b in case["bras"]}
        r = simuler(cles, graines.g(**etiq, role="monde"), graines.g(**etiq, role="source"), case["config"], case["dose"],
                    case["taux"], f, n * S, case.get("repere", REPERE_LECTURE), case.get("retrait", "v2"),
                    case.get("repli", False), taille_tirage=S)
        for b in case["bras"]:
            for champ in TYPES_DES_SORTIES:
                sorties.setdefault(b, {}).setdefault(champ, []).append(r["bras"][b][champ].reshape(n, S))
        t += n
        k += 1
    return {b: {c: np.concatenate(v, axis=0) for c, v in d.items()} for b, d in sorties.items()}


def sorties_du_registre_source(src):
    """Code v6 (point 4 de l'audit ; M7, S7) : ce que le registre de la course source porte, source par source — ses comptes, et
    la part des entrées gardées et les facteurs d'enrichissement que rend `statistique.enrichissement`."""
    e = enrichissement(src)
    comptes = {"entrees": src.n, "entrees_gardees": src.n_gardees, "entrees_vraies": src.entrees_v,
               "entrees_vraies_gardees": src.gardees_v, "lois_vraies_engagees": src.engagee_v.sum(axis=1),
               "lois_fausses_engagees": src.engagee_f.sum(axis=1), "lois_non_plantees_engagees": src.engagee_np,
               "lois_vraies_gardees": src.gardee_v.sum(axis=1), "lois_fausses_gardees": src.gardee_f.sum(axis=1),
               "lois_non_plantees_gardees": src.gardee_np}
    out = {k: np.asarray(comptes[k], dtype=np.int64) for k in COMPTES_DU_REGISTRE_SOURCE}
    out.update({k: np.asarray(e[k], dtype=np.float64) for k in CHAMPS_D_ENRICHISSEMENT})
    return out


def simuler_case_sources(graines, couche, case, f, sources, lot=LOT_DE_SOURCES):
    """Code v6 (point 1 de l'audit) : le mode « sources ». `sources` sources simulées par lots de `lot` sources, chaque lot sous
    son étiquette (champ `mode=sources`, numéro de lot) ; la source étrangère d'une source est la suivante du même lot, la
    première pour la dernière ; un lot d'une seule source, pour une case qui a les bras 4a ou 4b, arrête avant tout tirage. Rend
    (sorties par bras {champ : (sources,)}, sorties du registre de la course source {champ : (sources,)}, vides hors du
    repli)."""
    base = champs_de_la_case(case)
    if base.get("mode") != "sources":
        raise ArretTirages("simulation au mode « sources » d'une case sans clé « sources »")
    role_case = base.pop("role", None)
    dernier = sources - lot * ((sources - 1) // lot)
    if any(b in ("4a", "4b") for b in case["bras"]) and min(lot, dernier) < 2:
        raise ArretTirages("mode « sources » : un lot d'une seule source n'a pas de source étrangère (B7 bis) : arrêt")
    sorties, registre = {}, {}
    fait = 0
    k = 0
    while fait < sources:
        n = min(lot, sources - fait)
        etiq = dict(couche=couche, **base, lot=k)
        cles = {b: graines.g(**etiq, bras=b, role="echantillonnage" if role_case is None else f"echantillonnage-{role_case}")
                for b in case["bras"]}
        r = simuler(cles, graines.g(**etiq, role="monde"), graines.g(**etiq, role="source"), case["config"], case["dose"],
                    case["taux"], f, n, case.get("repere", REPERE_LECTURE), case.get("retrait", "v2"), case.get("repli", False))
        for b in case["bras"]:
            for champ in TYPES_DES_SORTIES:
                sorties.setdefault(b, {}).setdefault(champ, []).append(r["bras"][b][champ])
        if case.get("repli"):
            for champ, v in sorties_du_registre_source(r["source"]).items():
                registre.setdefault(champ, []).append(v)
        fait += n
        k += 1
    return ({b: {c: np.concatenate(v) for c, v in d.items()} for b, d in sorties.items()},
            {c: np.concatenate(v) for c, v in registre.items()})


def lire_case(sorties, dose, grille, bras):
    """La lecture de chaque tirage à chaque nombre de sources (codes entiers ; aucun taux). Dose non nulle : procédure de Holm
    sur les deux contrastes (M4, M5) et lecture du seul contraste de l'héritage au seuil de 0,05 (M13) ; dose nulle : règle de
    validité unilatérale (M6) ; bras de diagnostic : test M3 lu seul au seuil de 0,05 pour « 2 − 1 » et « 2 − 4b » (M14)."""
    T = next(iter(sorties.values()))["M1"].shape[0]
    out = {}
    m1 = {b: sorties[b]["M1"].astype(np.int64) for b in bras}
    ft = {b: sorties[b]["fausses_tenues"].astype(np.int64) for b in bras}
    if dose == 0.0:
        dec = np.zeros((T, len(grille)), dtype=np.int8)
        for t in range(T):
            d = m1["3"][t] - m1["2"][t]
            for j, k in enumerate(grille):
                dec[t, j] = RS.regle_de_validite(d[:k])
        out["declenche"] = dec
        return out
    if "1" in bras and "2" in bras and "3" in bras:
        rej = np.zeros((T, len(grille)), dtype=np.int8)
        lh = np.zeros((T, len(grille)), dtype=np.int8)
        lt = np.zeros((T, len(grille)), dtype=np.int8)
        pmh = np.zeros((T, len(grille)), dtype=np.int8)
        pmt = np.zeros((T, len(grille)), dtype=np.int8)
        seul = np.zeros((T, len(grille)), dtype=np.int8)
        seul_rejette = np.zeros((T, len(grille)), dtype=np.int8)
        for t in range(T):
            dh, dt = m1["3"][t] - m1["2"][t], m1["2"][t] - m1["1"][t]
            fh, fte = ft["3"][t] - ft["2"][t], ft["2"][t] - ft["1"][t]
            for j, k in enumerate(grille):
                l = RS.lire_tirage(dh[:k], dt[:k], fh[:k], fte[:k])
                rej[t, j] = l["rejette"]
                lh[t, j] = LECTURES[l["lecture_heritage"]]
                lt[t, j] = LECTURES[l["lecture_tenue"]]
                pmh[t, j] = l["premiere_marche_heritage"]
                pmt[t, j] = l["premiere_marche_tenue"]
                seul_rejette[t, j] = l["p_heritage"] <= 0.05
                seul[t, j] = LECTURES[RS.lecture_contraste(l["p_heritage"] <= 0.05, dh[:k], fh[:k])]
        out.update(rejette=rej, lecture_heritage=lh, lecture_tenue=lt, premiere_marche_heritage=pmh,
                   premiere_marche_tenue=pmt, heritage_seul_lecture=seul, heritage_seul_rejette=seul_rejette)
    if "4b" in bras:
        r21 = np.zeros((T, len(grille)), dtype=np.int8)
        r24 = np.zeros((T, len(grille)), dtype=np.int8)
        for t in range(T):
            d21, d24 = m1["2"][t] - m1["1"][t], m1["2"][t] - m1["4b"][t]
            for j, k in enumerate(grille):
                r21[t, j] = RS.valeur_p_bilaterale(d21[:k]) <= 0.05
                r24[t, j] = RS.valeur_p_bilaterale(d24[:k]) <= 0.05
        out.update(rejette_2_moins_1=r21, rejette_2_moins_4b=r24)
    return out


def _sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def _sceller(chemin):
    sha = _sha256(chemin)
    with open(chemin + ".sha256", "x", encoding="ascii") as f:
        f.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def ecrire_sorties(dossier, nom, case, sorties, lectures, grille, registre_source=None, en_plus=None):
    """Sorties brutes scellées d'une case : un fichier `.npy` par tableau, un fichier de description, chacun avec son compagnon
    `.sha256` ; jamais d'écrasement. Rend {fichier : empreinte}. Code v6 : chaque sortie d'un bras est écrite à son type
    (`TYPES_DES_SORTIES` ; une sortie inconnue arrête) ; les sorties du registre de la course source, s'il y en a, sous le nom
    `source-<champ>.npy` ; la description porte en plus `en_plus` (mode, sources par tirage ou lot de sources)."""
    d = os.path.join(dossier, nom)
    os.makedirs(d)
    empreintes = {}
    for b in sorted(sorties):
        for champ in sorted(sorties[b]):
            if champ not in TYPES_DES_SORTIES:
                raise ArretTirages(f"sortie de bras inconnue : {champ}")
            chemin = os.path.join(d, f"{champ}-bras-{b}.npy")
            with open(chemin, "xb") as fh:
                np.save(fh, np.ascontiguousarray(sorties[b][champ].astype(TYPES_DES_SORTIES[champ])), allow_pickle=False)
            empreintes[os.path.basename(chemin)] = _sceller(chemin)
    for champ in sorted(lectures):
        chemin = os.path.join(d, f"lecture-{champ}.npy")
        with open(chemin, "xb") as fh:
            np.save(fh, np.ascontiguousarray(lectures[champ]), allow_pickle=False)
        empreintes[os.path.basename(chemin)] = _sceller(chemin)
    for champ in sorted(registre_source or {}):
        chemin = os.path.join(d, f"source-{champ}.npy")
        with open(chemin, "xb") as fh:
            np.save(fh, np.ascontiguousarray(registre_source[champ]), allow_pickle=False)
        empreintes[os.path.basename(chemin)] = _sceller(chemin)
    desc = {k: v for k, v in case.items() if k != "config"}
    desc.update(config=case["config"], grille=list(grille), fichiers=empreintes, version=VERSION, **(en_plus or {}))
    chemin = os.path.join(d, "case.json")
    with open(chemin, "x", encoding="utf-8") as fh:
        fh.write(json.dumps(desc, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    empreintes["case.json"] = _sceller(chemin)
    return empreintes


def nom_de_case(case, prefixe=""):
    """Le nom du dossier d'une case. Code v6 : le nom d'une case du mode « sources » finit par `-sources` (celui d'une case du
    mode « tirages » est celui du code v5)."""
    morceaux = [case["famille"], case["proposeur"], f"dose{case['dose']}", f"taux{case['taux']}"]
    for k in ("taille", "force"):
        if case.get(k) is not None:
            morceaux.append(f"{k}{case[k]}")
    if case.get("retrait", "v2") != "v2":
        morceaux.append(f"retrait{case['retrait']}")
    if case.get("repere", REPERE_LECTURE) != REPERE_LECTURE:
        morceaux.append(f"repere{case['repere']}")
    if case.get("repli"):
        morceaux.append("repli")
    if "sources" in case:
        morceaux.append("sources")
    return prefixe + "-".join(morceaux)


def jouer_case(graines, couche, case, f, tirages, dossier, prefixe="", grille=None, sources_par_tirage=None):
    """Simule, lit et écrit une case ; rend les empreintes. Aucune case n'est lue ici : le programme d'analyse lit après que
    toutes sont calculées et scellées (étape 8). Code v6 : `sources_par_tirage` (par défaut le plus grand nombre lu) permet de
    simuler la case entière et de n'en lire que certains nombres (tirage de confirmation, étape 9)."""
    grille = grille or grille_de(case["dose"], avec_m13=case["famille"] == "B")
    S = sources_par_tirage or max(grille)
    if S < max(grille):
        raise ArretTirages(f"un nombre lu ({max(grille)}) au-delà des sources simulées par tirage ({S})")
    sorties = simuler_case(graines, couche, case, f, tirages, S)
    lectures = lire_case(sorties, case["dose"], grille, case["bras"])
    return ecrire_sorties(dossier, nom_de_case(case, prefixe), case, sorties, lectures, grille,
                          en_plus={"mode": "tirages", "sources_par_tirage": S})


def jouer_case_sources(graines, couche, case, f, sources, dossier, prefixe=""):
    """Code v6 (point 1 de l'audit) : simule et écrit une case du mode « sources » — aucune lecture par tirage, aucun taux ; les
    écarts se calculent au programme d'analyse. Rend les empreintes."""
    sorties, registre = simuler_case_sources(graines, couche, case, f, sources)
    return ecrire_sorties(dossier, nom_de_case(case, prefixe), case, sorties, {}, (), registre_source=registre,
                          en_plus={"mode": "sources", "lot_de_sources": LOT_DE_SOURCES})


def essai_de_forme(graines, case, f, tirages, nombres_de_sources, dossier):
    """Annexe C : essai de forme, au plus 200 tirages par case et deux nombres de sources, sous la couche « essai-de-forme » ;
    il vérifie l'exécution, la forme des fichiers et le temps de calcul ; il ne calcule ni taux, ni puissance, ni taille
    réalisée, ni rapport R ; ses sorties le disent dans leur nom."""
    if tirages > ESSAI_DE_FORME_MAX_TIRAGES or len(nombres_de_sources) > ESSAI_DE_FORME_MAX_NOMBRES_DE_SOURCES:
        raise ArretTirages("essai de forme hors de ses bornes (200 tirages, deux nombres de sources)")
    t0 = time.monotonic()
    emp = jouer_case(graines, "essai-de-forme", case, f, tirages, dossier, prefixe="essai-de-forme-",
                     grille=tuple(sorted(nombres_de_sources)))
    return {"fichiers": emp, "duree_s": time.monotonic() - t0}


def chemin_de_la_liste_des_etiquettes(chemin_manifeste):
    """Le fichier de la liste des étiquettes, à côté du manifeste : `manifeste.json` → `manifeste-etiquettes.txt`."""
    base = chemin_manifeste[:-len(".json")] if chemin_manifeste.endswith(".json") else chemin_manifeste
    return base + "-etiquettes.txt"


def ecrire_manifeste(chemin, configuration, graines, commit, fichiers_geles):
    """Règle R9 : un manifeste par run — configuration et son empreinte, versions, racine, étiquettes (nombre, empreinte de leur
    liste triée, couches), commit, empreintes des fichiers gelés (fréquences M12, réglages). Code v4 (B8, version 7, choix 12) :
    la liste entière des étiquettes, triée, une par ligne, jointes par un saut de ligne sans saut final (le texte même dont le
    manifeste porte l'empreinte), est écrite dans un fichier scellé à côté du manifeste, avant lui ; le manifeste inscrit son nom
    et son empreinte, égale à celle de la liste (elle se rejoue à la main par `sha256sum`). Code v5 (remarque 4, point (e) ;
    point (b) pour l'heure) : à la place de l'empreinte de la version 6, le manifeste inscrit l'empreinte du texte présenté, celle
    de la pièce d'autorisation du verrou et l'heure qu'elle porte, prises de l'autorisation des graines ; sans autorisation
    (couches non décisives), ces trois champs valent null."""
    a = graines.autorisation
    autorisation = {"texte_sha256": None if a is None else a.sha_texte,
                    "piece_d_autorisation_sha256": None if a is None else a.sha_piece,
                    "heure_d_autorisation": None if a is None else a.heure}
    canon = json.dumps(configuration, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    etiq = sorted(graines.etiquettes)
    texte_liste = "\n".join(etiq).encode("utf-8")
    chemin_liste = chemin_de_la_liste_des_etiquettes(chemin)
    with open(chemin_liste, "xb") as fh:
        fh.write(texte_liste)
    sha_liste = _sceller(chemin_liste)
    m = {"version": VERSION, **autorisation, "configuration": configuration,
         "configuration_sha256": hashlib.sha256(canon.encode("utf-8")).hexdigest(),
         "versions": {"python": platform.python_version(), "numpy": np.__version__},
         "racine": graines.racine if graines.racine is not None else RACINE_GRAINES, "commit": commit,
         "etiquettes": {"nombre": len(etiq), "sha256": hashlib.sha256(texte_liste).hexdigest(),
                        "couches": sorted({e.split("|", 1)[0] for e in etiq}),
                        "fichier": os.path.basename(chemin_liste), "fichier_sha256": sha_liste},
         "fichiers_geles": fichiers_geles}
    with open(chemin, "x", encoding="utf-8") as fh:
        fh.write(json.dumps(m, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    return _sceller(chemin)


def _lire_scelle(chemin):
    """Les octets d'un fichier, après contrôle de son compagnon `.sha256` ; arrêt sinon."""
    if not os.path.isfile(chemin) or not os.path.isfile(chemin + ".sha256"):
        raise ArretTirages(f"fichier ou compagnon absent : {chemin}")
    with open(chemin + ".sha256", encoding="ascii") as fh:
        attendu = (fh.read().split() or [""])[0]
    if _sha256(chemin) != attendu:
        raise ArretTirages(f"empreinte différente de son compagnon : {chemin}")
    with open(chemin, "rb") as fh:
        return fh.read(), attendu


def verifier_manifeste(chemin):
    """Choix 12 (code v4) : rejoue l'empreinte de la liste des étiquettes. Le manifeste et la liste ont l'empreinte de leur
    compagnon ; la liste a l'empreinte, le nombre de lignes et les couches que le manifeste inscrit, et elle est triée. Rend le
    nombre d'étiquettes ; arrêt sinon."""
    octets, _ = _lire_scelle(chemin)
    m = json.loads(octets.decode("utf-8"))
    champs = ("texte_sha256", "piece_d_autorisation_sha256", "heure_d_autorisation")
    if "preenregistrement_sha256" in m or any(k not in m for k in champs) or (
            len({m[k] is None for k in champs}) != 1):
        raise ArretTirages("manifeste : empreintes du texte et de la pièce d'autorisation, et heure, non inscrites ensemble "
                           "(code v5, remarque 4, point (e))")
    e = m.get("etiquettes") or {}
    chemin_liste = os.path.join(os.path.dirname(chemin), e.get("fichier") or "")
    if not e.get("fichier") or chemin_liste != chemin_de_la_liste_des_etiquettes(chemin):
        raise ArretTirages("manifeste : fichier de la liste des étiquettes non inscrit (choix 12)")
    liste, sha = _lire_scelle(chemin_liste)
    lignes = liste.decode("utf-8").split("\n") if liste else []
    if (sha != e.get("fichier_sha256") or hashlib.sha256(liste).hexdigest() != e.get("sha256")
            or len(lignes) != e.get("nombre") or lignes != sorted(lignes)
            or sorted({x.split("|", 1)[0] for x in lignes}) != e.get("couches")):
        raise ArretTirages("manifeste : la liste des étiquettes ne rejoue pas ce que le manifeste inscrit (choix 12)")
    return len(lignes)


def exiger_autorisation_pour(couche, graines):
    """Liste d'arrêt, point 1 : aucun tirage décisif ni de confirmation sans autorisation (vérifiée avant toute simulation).
    Code v5 : l'autorisation est vérifiée de nouveau ici, sur disque, avant le lancement (texte, pièce, registre des GO,
    modules)."""
    if couche in COUCHES_DECISIVES and graines.autorisation is None:
        from .graines import GraineRefusee, REFUS
        REFUS.append(f"couche={couche}|lancement")
        raise GraineRefusee(f"lancement de la couche « {couche} » refusé : aucune autorisation (liste d'arrêt, point 1)")
    if couche in COUCHES_DECISIVES:
        graines.autorisation.verifier()
    return True


def verifier_cases(couche, cases):
    """Code v6 (points 2 et 3 de l'audit) : contrôle d'un lancement, avant l'autorisation et avant toute dérivation. Chaque case a
    une et une seule des clés « tirages » et « sources » (`mode_de`) ; deux cases n'ont jamais le même nom (le nom porte le mode)
    ; sous la couche « decisif », chaque case a la taille gelée de son mode (10 000 tirages emboîtés ; 200 000 sources) et lit
    toute sa grille ; sous la couche « confirmation », seules les cases de C1 et de C4 se tirent, au mode « tirages », à 100 000
    tirages, chacune avec les nombres de sources à lire (`nombres_lus`) ; des nombres lus sont toujours dans la grille de la case ;
    une case du mode « sources » qui a les bras 4a ou 4b n'a aucun lot d'une seule source. Rend {nom : (mode, nombre)} ; arrêt
    nommé sinon (`ArretTirages`), rien n'étant créé ni dérivé."""
    plan = {}
    for case in cases:
        mode, n = mode_de(case)
        nom = nom_de_case(case)
        if nom in plan:
            raise ArretTirages(f"deux cases au même nom : {nom} (le nom porte le mode ; B8) : arrêt avant tout tirage")
        if couche == "decisif":
            gelee = TIRAGES_PAR_CASE if mode == "tirages" else SOURCES_FAMILLES_GRANDES
            if n != gelee or "nombres_lus" in case:
                raise ArretTirages(f"couche « decisif » : la case {nom} doit être tirée à la taille gelée de son mode ({gelee} "
                                   f"{mode}) et lue sur toute sa grille (reçu {n}) : arrêt")
        if couche == "confirmation" and (mode != "tirages" or n != TIRAGES_CONFIRMATION or "nombres_lus" not in case
                                         or (case["famille"], case["proposeur"]) not in CASES_DE_CONFIRMATION):
            raise ArretTirages(f"couche « confirmation » : seules les cases de C1 et de C4 se tirent, à {TIRAGES_CONFIRMATION} "
                               f"tirages, avec leurs nombres lus (reçu {nom}, {n} {mode}) : arrêt")
        if "nombres_lus" in case:
            lus = case["nombres_lus"]
            if mode != "tirages" or not lus or not set(lus) <= set(grille_de(case["dose"], avec_m13=case["famille"] == "B")):
                raise ArretTirages(f"case {nom} : nombres lus hors de sa grille ({lus!r}) : arrêt")
        if mode == "sources" and any(b in ("4a", "4b") for b in case["bras"]):
            dernier = n - LOT_DE_SOURCES * ((n - 1) // LOT_DE_SOURCES)
            if min(LOT_DE_SOURCES, dernier) < 2:
                raise ArretTirages(f"case {nom} : un lot d'une seule source n'a pas de source étrangère (B7 bis) : arrêt")
        plan[nom] = (mode, n)
    if not plan:
        raise ArretTirages("lancement sans aucune case : arrêt")
    return plan


def lancer_famille(graines, couche, cases, f_par_case, dossier, commit, fichiers_geles, cases_non_atteignables=None,
                   en_plus=None):
    """Étape 8 (ou 9) : toutes les cases d'un lancement, écrites et scellées ; un manifeste. Rend les empreintes par case.
    Code v6 (point 3 de l'audit ; B8, étape 8 : « toutes les familles, en un seul lancement ») : chaque case est tirée au nombre
    que porte sa clé, `tirages` (tirages emboîtés) ou `sources` (mode « sources ») — aucun nombre commun n'est reçu ; les cases de
    tous les modes se tirent dans ce seul appel, sous un seul manifeste, qui inscrit le nombre de chaque case, et, s'ils sont
    donnés, les cases « non atteignables » et les champs `en_plus` ; `verifier_cases` contrôle le lancement avant l'autorisation
    et avant toute dérivation. Une case de tirages qui porte `nombres_lus` est simulée entière (le plus grand nombre de sa grille)
    et lue à ces seuls nombres."""
    plan = verifier_cases(couche, cases)
    exiger_autorisation_pour(couche, graines)
    os.makedirs(dossier)
    out = {}
    for case in cases:
        nom = nom_de_case(case)
        mode, n = plan[nom]
        if mode == "tirages":
            S = max(grille_de(case["dose"], avec_m13=case["famille"] == "B"))
            lus = tuple(sorted(case["nombres_lus"])) if "nombres_lus" in case else None
            out[nom] = jouer_case(graines, couche, case, f_par_case(case), n, dossier, grille=lus, sources_par_tirage=S)
        else:
            out[nom] = jouer_case_sources(graines, couche, case, f_par_case(case), n, dossier)
    configuration = {"couche": couche, "cases": sorted(out),
                     "tirages_par_case": {k: v for k, (m, v) in sorted(plan.items()) if m == "tirages"},
                     "sources_par_case": {k: v for k, (m, v) in sorted(plan.items()) if m == "sources"}}
    if cases_non_atteignables is not None:
        configuration["cases_non_atteignables"] = list(cases_non_atteignables)
    configuration.update(en_plus or {})
    ecrire_manifeste(os.path.join(dossier, "manifeste.json"), configuration, graines, commit, fichiers_geles)
    return out
