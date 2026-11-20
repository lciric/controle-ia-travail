"""Étape 10 — le programme d'analyse (annexe C). Il ne lit que des sorties scellées (empreintes vérifiées), écrit la table des
critères et ce que la section « Ce qui est rapporté » nomme, et ne prononce pas l'issue : le verdict revient à un sous-agent
neuf (règle R13).

Règles gelées appliquées ici : C1 et C4 (une case tient si au plus 500 rejets sur 10 000 ; au-delà, elle est en échec si le
tirage de confirmation compte au moins 5 236 rejets sur 100 000) ; C2 et C3 « atteints à un nombre » s'ils sont tenus à ce nombre
et à tous les suivants de la grille (C2 : pour les deux contrastes, à chaque dose non nulle où la taille de référence est
atteignable, au taux d'échec de 0,25) ; C5 (part M10 au moins 0,8 à chaque nombre et à chaque dose non nulle atteignable) ; n,
le plus petit nombre de la grille, au moins 10, où C2 est atteint ; m, le plus petit nombre de la grille à dose nulle où C3 et
C4 sont tenus ensemble, à ce nombre et à tous les suivants ; S7 sur l'intervalle de R ; S9 (n₁, n₂) ; taille réalisée (liste
d'arrêt, point 6).
"""

import hashlib
import json
import os

import numpy as np

from .constantes import (BEAUCOUP_PLUS_ECART, BEAUCOUP_PLUS_RAPPORT, GRILLE_SOURCES, GRILLE_SOURCES_DOSE_NULLE, MAX_SOURCES,
                         REECHANTILLONS, SEUIL_PART_M10, SEUIL_PUISSANCE, SEUIL_S7, TOLERANCE_TAILLE_REALISEE)
from .intervalles import clopper_pearson, regle_de_confirmation
from .tirages import LECTURES


class ArretAnalyse(RuntimeError):
    pass


# --- lecture des sorties scellées -------------------------------------------------------------------------------------------


def _sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def lire_case(dossier_case):
    """Relit une case après vérification de chaque empreinte (compagnon et description) ; arrêt sur tout écart (règle R11)."""
    def verifie(chemin):
        if not os.path.isfile(chemin) or not os.path.isfile(chemin + ".sha256"):
            raise ArretAnalyse(f"sortie absente ou non scellée : {chemin}")
        with open(chemin + ".sha256", encoding="ascii") as f:
            attendu = (f.read().split() or [""])[0]
        if _sha256(chemin) != attendu:
            raise ArretAnalyse(f"sortie d'empreinte différente de son sceau : {chemin}")
        return attendu
    verifie(os.path.join(dossier_case, "case.json"))
    with open(os.path.join(dossier_case, "case.json"), encoding="utf-8") as f:
        desc = json.load(f)
    tableaux = {}
    for nom, sha in desc["fichiers"].items():
        if verifie(os.path.join(dossier_case, nom)) != sha:
            raise ArretAnalyse(f"sortie différente de la description de la case : {nom}")
        tableaux[nom[:-4]] = np.load(os.path.join(dossier_case, nom), allow_pickle=False)
    return desc, tableaux


# --- taux et règles ---------------------------------------------------------------------------------------------------------


def taux_par_nombre(tableau_booleen, grille):
    """Pour chaque nombre de sources : (compte, tirages, taux, intervalle binomial exact à 95 %)."""
    T = tableau_booleen.shape[0]
    out = {}
    for j, k in enumerate(grille):
        c = int(np.asarray(tableau_booleen[:, j]).astype(bool).sum())
        out[k] = {"compte": c, "tirages": T, "taux": c / T, "intervalle": clopper_pearson(c, T)}
    return out


def statut_case_de_niveau(rejets, tirages, rejets_confirmation=None):
    """C1 et C4 : « tenue », « à confirmer » ou « en échec » (règle gelée, version 2)."""
    return regle_de_confirmation(rejets, rejets_confirmation, tirages)


def atteint_a_partir_de(valeurs_par_nombre, grille, seuil=SEUIL_PUISSANCE):
    """Le plus petit nombre de la grille où la valeur est au moins le seuil, à ce nombre et à tous les suivants ; None sinon."""
    meilleur = None
    for k in sorted(grille, reverse=True):
        v = valeurs_par_nombre.get(k)
        if v is None or v < seuil:
            break
        meilleur = k
    return meilleur


def n_de_l_etage(puissances, plancher=10, grille=GRILLE_SOURCES):
    """`puissances` : {(contraste, dose atteignable) : {k : puissance}} au taux 0,25 et à la taille de référence. n : le plus
    petit nombre de la grille, au moins 10, où chaque série est tenue à ce nombre et à tous les suivants ; None sinon."""
    if not puissances:
        return None
    candidats = [atteint_a_partir_de(v, grille) for v in puissances.values()]
    if any(c is None for c in candidats):
        return None
    return max([plancher] + candidats)


def m_de_l_etage(c3_par_nombre, c4_tenue_par_nombre, grille=GRILLE_SOURCES_DOSE_NULLE):
    """m : le plus petit nombre de la grille à dose nulle où C3 (taux ≥ 0,8 au taux d'échec de 0,25) et C4 (toutes ses cases
    tenues, aux trois taux) sont tenus ensemble, à ce nombre et à tous les suivants ; None sinon."""
    meilleur = None
    for k in sorted(grille, reverse=True):
        if not (c3_par_nombre.get(k, 0.0) >= SEUIL_PUISSANCE and c4_tenue_par_nombre.get(k, False)):
            break
        meilleur = k
    return meilleur


def part_m10(ecart_dependantes, ecart_independantes):
    """M10 : D / (D + max(I, 0)) si D est positif ; zéro sinon."""
    if ecart_dependantes <= 0:
        return 0.0
    return ecart_dependantes / (ecart_dependantes + max(ecart_independantes, 0.0))


def m10_par_nombre(sorties, grille):
    """Part M10 à chaque nombre de sources : écarts d'héritage moyens sur les lois dépendantes et indépendantes, sur les k
    premières sources de tous les tirages."""
    out = {}
    for k in grille:
        D = float((sorties["3"]["D"][:, :k] - sorties["2"]["D"][:, :k]).mean())
        I = float((sorties["3"]["I"][:, :k] - sorties["2"]["I"][:, :k]).mean())
        out[k] = {"D": D, "I": I, "part": part_m10(D, I)}
    return out


def part_de_differences_nulles(sorties, a, b, grille):
    """M11 : la part des différences appariées égales à zéro, sur les k premières sources."""
    d = sorties[a]["M1"].astype(np.int64) - sorties[b]["M1"].astype(np.int64)
    return {k: float(np.mean(d[:, :k] == 0)) for k in grille}


def puissance_etabli(lecture, grille):
    """Part des tirages où le contraste est « établi » (code de lecture 1)."""
    return {k: float(np.mean(lecture[:, j] == LECTURES["établi"])) for j, k in enumerate(grille)}


def intervalle_reechantillonne(valeurs_par_source, statistique, rng, B=REECHANTILLONS):
    x = np.asarray(valeurs_par_source)
    n = x.shape[0]
    stats = np.array([statistique(x[rng.integers(0, n, n)]) for _ in range(B)])
    return [float(np.percentile(stats, 2.5)), float(np.percentile(stats, 97.5))]


def rapport_R(ecarts_repli, ecarts_servis, rng, B=REECHANTILLONS):
    """M7 : R = écart d'héritage moyen sous le repli / écart d'héritage moyen servi (même K), avec l'intervalle par
    rééchantillonnage des sources (les deux séries rééchantillonnées chacune sur ses sources). Rend (R, intervalle, l'écart
    servi est-il positif à l'intervalle près)."""
    a, b = np.asarray(ecarts_repli, dtype=float), np.asarray(ecarts_servis, dtype=float)
    ib = intervalle_reechantillonne(b, np.mean, rng, B)
    if not ib[0] > 0:
        return None, None, False
    stats = np.array([a[rng.integers(0, len(a), len(a))].mean() / b[rng.integers(0, len(b), len(b))].mean() for _ in range(B)])
    return float(a.mean() / b.mean()), [float(np.percentile(stats, 2.5)), float(np.percentile(stats, 97.5))], True


def rapport_d_ecarts_types(ecart_type_entre_bras, ecart_type_jumelles):
    """M9 : écart-type des différences entre bras divisé par l'écart-type entre jumelles (un attendu pour le sourd à appels
    égaux, hypothèse de travail (ii))."""
    return ecart_type_entre_bras / ecart_type_jumelles


def s7(intervalle_R, ecart_servi_positif):
    """S7 : « presque autant » si la borne basse de R est au moins 0,8 à chaque dose ; « le repli coûte » si la borne haute est
    sous 0,8 à chacune ; « indécis » sinon ; « sans objet » si l'écart servi n'est pas positif à l'intervalle près."""
    if not all(ecart_servi_positif.values()):
        return "sans objet"
    if all(b >= SEUIL_S7 for b, _ in intervalle_R.values()):
        return "presque autant"
    if all(h < SEUIL_S7 for _, h in intervalle_R.values()):
        return "le repli coûte"
    return "indécis"


def s9(n1, n2):
    """S9 : remplie si n₂ − n₁ ≥ 8 et n₂ ≥ 1,5 n₁ ; si C2 n'est atteint à aucun nombre jusqu'à 48 (n₂ None), remplie quand n₁ est
    au plus 32, « indéterminée » sinon ; si n₁ n'existe pas jusqu'à 48, « sans objet »."""
    if n1 is None:
        return "sans objet"
    if n2 is None:
        return "remplie" if n1 <= 32 else "indéterminée"
    return "remplie" if (n2 - n1 >= BEAUCOUP_PLUS_ECART and n2 >= BEAUCOUP_PLUS_RAPPORT * n1) else "non remplie"


def plus_petit_n2_qui_remplit(n1, grille=GRILLE_SOURCES):
    for n2 in grille:
        if s9(n1, n2) == "remplie":
            return n2
    return None


def taille_realisee(ecart_moyen, ecart_type_gele, cible):
    """Liste d'arrêt, point 6 : (taille réalisée, tenue)."""
    t = ecart_moyen / ecart_type_gele
    return t, abs(t - cible) <= TOLERANCE_TAILLE_REALISEE + 1e-12


def table_des_criteres(c1_cases, c4_cases, puissances, c3_par_nombre, c5_parts, gardes):
    """La table des critères, sans issue. `c1_cases`, `c4_cases` : {case : statut} ; `puissances` : voir `n_de_l_etage` ;
    `c3_par_nombre` : {k : taux} ; `c5_parts` : {(dose, k) : part} ; `gardes` : {garde : (cas sain passé, artefact arrêté)}
    (la garde 17 non jouée vaut None). Code v3, note D4 : `gardes` porte exactement les gardes 1 à 27 de B9, chacune jouée sauf
    la 17 ; une table incomplète arrête (C6 dit « toutes tenues », jamais sur une liste partielle)."""
    if sorted(gardes) != list(range(1, 28)) or any(v is None for g, v in gardes.items() if g != 17):
        raise ArretAnalyse(f"C6 : table des gardes incomplète (attendu les gardes 1 à 27, chacune jouée sauf la 17 ; reçu "
                           f"{sorted(gardes)}) : arrêt")
    c4_tenue_par_nombre = {}
    for cle, st in c4_cases.items():  # clé : (nombre de sources, proposeur, taux d'échec)
        k = cle[0]
        c4_tenue_par_nombre[k] = c4_tenue_par_nombre.get(k, True) and st == "tenue"
    c1 = "en échec" if any(s == "en échec" for s in c1_cases.values()) else (
        "à confirmer" if any(s == "à confirmer" for s in c1_cases.values()) else "tenu")
    c4 = "en échec" if any(s == "en échec" for s in c4_cases.values()) else (
        "à confirmer" if any(s == "à confirmer" for s in c4_cases.values()) else "tenu")
    c5_echecs = sorted(k for k, p in c5_parts.items() if p < SEUIL_PART_M10)
    g17_non_jouee = gardes.get(17) is None
    c6_echecs = sorted(g for g, v in gardes.items() if v is not None and not (v[0] and v[1]))
    return {"C1": c1, "C1_cases_au_dessus_de_0_05": sorted(str(k) for k, s in c1_cases.items() if s != "tenue"),
            "C2_n": n_de_l_etage(puissances), "C2_atteint_jusqu_a_48": n_de_l_etage(puissances) is not None,
            "C3_atteint_a": atteint_a_partir_de(c3_par_nombre, GRILLE_SOURCES_DOSE_NULLE),
            "C4": c4, "C5": "en échec" if c5_echecs else "tenu", "C5_echecs": [str(x) for x in c5_echecs],
            "C6": "en échec" if c6_echecs else ("non établi (garde 17 non jouée)" if g17_non_jouee else "tenu"),
            "C6_gardes_en_echec": c6_echecs,
            "m": m_de_l_etage(c3_par_nombre, c4_tenue_par_nombre), "issue": "non prononcée (règle R13)"}
