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
                         PREENREGISTREMENT_SHA256, RACINE_GRAINES, REPERE_LECTURE, VERSION)
from .graines import COUCHES_DECISIVES
from .statistique import simuler

LECTURES = {"non établi": 0, "établi": 1, "non lu comme succès": 2, "effet négatif établi": 3, "égalité": 4}


class ArretTirages(RuntimeError):
    pass


def grille_de(dose, avec_m13=False):
    if dose == 0.0:
        return GRILLE_SOURCES_DOSE_NULLE
    return tuple(sorted(set(GRILLE_SOURCES) | (set(NOMBRES_M13_EN_PLUS) if avec_m13 else set())))


def s_max(dose):
    return MAX_SOURCES_DOSE_NULLE if dose == 0.0 else MAX_SOURCES


def champs_de_la_case(case):
    """Les champs d'étiquette d'une case (B8 : famille, proposeur, dose, taille ou force, taux d'échec, règle, repère)."""
    c = {"famille": case["famille"], "proposeur": case["proposeur"], "dose": case["dose"], "taux": case["taux"]}
    if case.get("taille") is not None:
        c["taille"] = case["taille"]
    if case.get("force") is not None:
        c["force"] = case["force"]
    if case.get("retrait", "v2") != "v2":
        c["retrait"] = case["retrait"]
    if case.get("repere", REPERE_LECTURE) != REPERE_LECTURE:
        c["repere"] = case["repere"]
    if case.get("repli"):
        c["role"] = "repli"
    return c


def simuler_case(graines, couche, case, f, tirages, sources_par_tirage=None, premier_tirage=0):
    """Simule `tirages` tirages d'une case ; rend {clé de bras : {M1, D, I, fausses_tenues : (tirages, sources)}}. Les graines
    sont dérivées par lot ; la première dérivation d'une couche décisive sans autorisation lève (liste d'arrêt, point 1)."""
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
            for champ in ("M1", "D", "I", "fausses_tenues"):
                sorties.setdefault(b, {}).setdefault(champ, []).append(r["bras"][b][champ].reshape(n, S))
        t += n
        k += 1
    return {b: {c: np.concatenate(v, axis=0) for c, v in d.items()} for b, d in sorties.items()}


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


def ecrire_sorties(dossier, nom, case, sorties, lectures, grille):
    """Sorties brutes scellées d'une case : un fichier `.npy` par tableau, un fichier de description, chacun avec son compagnon
    `.sha256` ; jamais d'écrasement. Rend {fichier : empreinte}."""
    d = os.path.join(dossier, nom)
    os.makedirs(d)
    empreintes = {}
    for b in sorted(sorties):
        for champ in sorted(sorties[b]):
            chemin = os.path.join(d, f"{champ}-bras-{b}.npy")
            with open(chemin, "xb") as fh:
                np.save(fh, np.ascontiguousarray(sorties[b][champ].astype(np.int16)), allow_pickle=False)
            empreintes[os.path.basename(chemin)] = _sceller(chemin)
    for champ in sorted(lectures):
        chemin = os.path.join(d, f"lecture-{champ}.npy")
        with open(chemin, "xb") as fh:
            np.save(fh, np.ascontiguousarray(lectures[champ]), allow_pickle=False)
        empreintes[os.path.basename(chemin)] = _sceller(chemin)
    desc = {k: v for k, v in case.items() if k != "config"}
    desc.update(config=case["config"], grille=list(grille), fichiers=empreintes, version=VERSION)
    chemin = os.path.join(d, "case.json")
    with open(chemin, "x", encoding="utf-8") as fh:
        fh.write(json.dumps(desc, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    empreintes["case.json"] = _sceller(chemin)
    return empreintes


def nom_de_case(case, prefixe=""):
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
    return prefixe + "-".join(morceaux)


def jouer_case(graines, couche, case, f, tirages, dossier, prefixe="", grille=None):
    """Simule, lit et écrit une case ; rend les empreintes. Aucune case n'est lue ici : le programme d'analyse lit après que
    toutes sont calculées et scellées (étape 8)."""
    grille = grille or grille_de(case["dose"], avec_m13=case["famille"] == "B")
    S = max(grille)
    sorties = simuler_case(graines, couche, case, f, tirages, S)
    lectures = lire_case(sorties, case["dose"], grille, case["bras"])
    return ecrire_sorties(dossier, nom_de_case(case, prefixe), case, sorties, lectures, grille)


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
    et son empreinte, égale à celle de la liste (elle se rejoue à la main par `sha256sum`)."""
    canon = json.dumps(configuration, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    etiq = sorted(graines.etiquettes)
    texte_liste = "\n".join(etiq).encode("utf-8")
    chemin_liste = chemin_de_la_liste_des_etiquettes(chemin)
    with open(chemin_liste, "xb") as fh:
        fh.write(texte_liste)
    sha_liste = _sceller(chemin_liste)
    m = {"version": VERSION, "preenregistrement_sha256": PREENREGISTREMENT_SHA256, "configuration": configuration,
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
    """Liste d'arrêt, point 1 : aucun tirage décisif ni de confirmation sans autorisation (vérifiée avant toute simulation)."""
    if couche in COUCHES_DECISIVES and graines.autorisation is None:
        from .graines import GraineRefusee, REFUS
        REFUS.append(f"couche={couche}|lancement")
        raise GraineRefusee(f"lancement de la couche « {couche} » refusé : aucune autorisation (liste d'arrêt, point 1)")
    return True


def lancer_famille(graines, couche, cases, f_par_case, tirages, dossier, commit, fichiers_geles):
    """Étape 8 (ou 9) : toutes les cases d'un lancement, écrites et scellées ; un manifeste. Rend les empreintes par case."""
    exiger_autorisation_pour(couche, graines)
    os.makedirs(dossier)
    out = {}
    for case in cases:
        out[nom_de_case(case)] = jouer_case(graines, couche, case, f_par_case(case), tirages, dossier)
    ecrire_manifeste(os.path.join(dossier, "manifeste.json"), {"couche": couche, "tirages": tirages,
                                                                "cases": sorted(out)}, graines, commit, fichiers_geles)
    return out
