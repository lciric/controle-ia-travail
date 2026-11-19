"""Statistique de famille du rejeu à blanc v3 des critères de sélection, course v9 — programme v1.

Écrit et scellé AVANT l'ouverture des lectures v3 (mandat de la mère, R-3883 ; recommandation 4 de l'audit de symétrie
`audit-symetrie-rejeu-v2-v1.md`, ff814fc9…). Le texte qui fixe la statistique et la règle de lecture est
`statistique-famille-rejeu-v3-v1.md`, dans le même dossier.

Question : dans chaque lecture v3 (lecteurs F, O, lecteur par programme) et dans l'assemblage, la famille des lecteurs
(lignées Opus et Fable) est-elle plus, ou moins, présente qu'à sa part de base parmi les cartes à la note maximale, dans le
nombre visé et au veto ? Test : permutation de l'étiquette de famille stratifiée par voie (20 000 permutations), calcul
exact en contrôle, correction de Holm ; descriptif par lignée, sans test.

Hors ligne, processeur seul, aucun appel de modèle. numpy (1.25 au moins) et bibliothèque standard.

Accès aux cartes : une seule fonction, `extraire_especes`, lit les enregistrements de `fiches.json`, et n'y lit qu'une
clé : `meta` → `proposeur` (l'étiquette du proposeur, `prop-opus`…). Aucun autre champ n'est lu ; le texte des cartes
(`contenu`) n'est jamais touché, et l'objet entier est supprimé aussitôt l'extraction faite. La sortie ne porte que des
comptes : aucune espèce par carte, aucun texte de carte.

Usage (la mère, après le dépôt des lectures v3, voir le texte scellé, § 7) :
  python3 -B -I statistique_famille_rejeu_v3_v1.py \
      --fiches FICHES --sha-fiches HEX \
      --correspondance CORRESPONDANCE --sha-correspondance HEX \
      --selection F CHEMIN HEX --selection O CHEMIN HEX \
      --selection programme CHEMIN HEX --selection assemblage CHEMIN HEX \
      --sortie SORTIE.json --resume RESUME.md
"""

import argparse
import datetime as dt
import hashlib
import json
import math
import os
import re
import sys
from collections.abc import Mapping
from fractions import Fraction

import numpy as np

VERSION = "statistique-famille-rejeu-v3-v1"

# ---------------------------------------------------------------- constantes fixées avant toute lecture
FICHES_SHA256_COURSE_V9 = "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481"
N_CARTES = 94
# Le seul champ lu dans un enregistrement de carte (orchestrateur, `course2_v54`, ligne `f["meta"]["proposeur"] =
# p["etiquette"]` ; étiquettes de la configuration v5 de la course, `course-v4/configuration-course-auto-conception-v5.json`).
CHEMIN_ESPECE = ("meta", "proposeur")
LIGNEE_DE = {"prop-opus": "Opus", "prop-fable": "Fable", "prop-argon": "Argon", "prop-astra": "Astra",
             "prop-carbon": "Carbon"}
LIGNEES = ("Opus", "Fable", "Argon", "Astra", "Carbon")
FAMILLE_DES_LECTEURS = frozenset({"Opus", "Fable"})
# Totaux par lignée sur les 94 cartes : pièce de la mère `especes-et-originalite-cartes-v9-v1.md` (2af9e67f…), § (a).
TOTAUX_PIECE = {"Opus": 22, "Fable": 15, "Argon": 21, "Astra": 20, "Carbon": 16}
ENSEMBLES = ("F", "O", "programme", "assemblage")
LISTES = ("note_maximale", "nombre_vise", "veto")
N_PERMUTATIONS = 20000
ALPHA = 0.05
N_MIN_LISTE = 3
TOL = 1e-9
GRAINE_TEXTE = b"statistique-famille-rejeu-v3-v1"
ENTROPIE = int(hashlib.sha256(GRAINE_TEXTE).hexdigest(), 16)
RE_ID = re.compile(r"^f[0-9a-f]{12}$")
RE_SHA = re.compile(r"^[0-9a-f]{64}$")
CLES_CORRESPONDANCE = {"cartes", "id", "voie", "note", "exclue", "nombre_vise", "veto"}


class Refus(Exception):
    """Arrêt sans repli : le programme ne calcule rien sur une entrée non conforme."""


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as fh:
        for bloc in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def verifier_empreinte(nom, chemin, attendue):
    if not isinstance(attendue, str) or not RE_SHA.match(attendue):
        raise Refus(f"{nom} : empreinte passée illisible ({attendue!r}) ; 64 chiffres hexadécimaux en minuscules exigés")
    if not os.path.isfile(chemin):
        raise Refus(f"{nom} : fichier absent ({chemin})")
    vue = sha256_fichier(chemin)
    if vue != attendue:
        raise Refus(f"{nom} : empreinte {vue} ≠ empreinte passée {attendue} ; rien n'est lu")
    return vue


# ---------------------------------------------------------------- le seul accès aux cartes
def extraire_especes(fiches, chemin=CHEMIN_ESPECE):
    """Rend {identifiant: lignée ou None}. Lit, dans chaque enregistrement, la seule clé `meta` → `proposeur`.

    Tout autre chemin est refusé. Les identifiants sont les clés de premier niveau ; rien d'autre n'est parcouru."""
    if tuple(chemin) != CHEMIN_ESPECE:
        raise Refus(f"champ « {'.'.join(map(str, chemin))} » refusé : seul « {'.'.join(CHEMIN_ESPECE)} » (l'espèce) est lu")
    if not isinstance(fiches, Mapping):
        raise Refus("fiches : objet {identifiant: enregistrement} attendu")
    especes = {}
    for ident in list(fiches.keys()):
        if not isinstance(ident, str) or not RE_ID.match(ident):
            raise Refus(f"fiches : identifiant illisible {ident!r}")
        rec = fiches[ident]
        if not isinstance(rec, Mapping) or CHEMIN_ESPECE[0] not in rec:
            raise Refus(f"fiches : {ident} sans champ « {CHEMIN_ESPECE[0]} »")
        meta = rec[CHEMIN_ESPECE[0]]
        if not isinstance(meta, Mapping):
            raise Refus(f"fiches : {ident}, « {CHEMIN_ESPECE[0]} » n'est pas un objet")
        if CHEMIN_ESPECE[1] not in meta:
            especes[ident] = None                     # compté et rapporté (« sans espèce »), jamais deviné
            continue
        valeur = meta[CHEMIN_ESPECE[1]]
        if valeur not in LIGNEE_DE:
            raise Refus(f"fiches : {ident}, étiquette d'espèce hors table ({valeur!r}) ; table : {sorted(LIGNEE_DE)}")
        especes[ident] = LIGNEE_DE[valeur]
    return especes


# ---------------------------------------------------------------- lecture des sélections, par correspondance de clés
def suivre(obj, pointeur, ou):
    if pointeur is None or pointeur == "":
        return obj
    if not isinstance(pointeur, str):
        raise Refus(f"{ou} : pointeur {pointeur!r} illisible (chaîne « a/b/c » attendue)")
    for part in pointeur.split("/"):
        if isinstance(obj, list):
            if not part.isdigit() or int(part) >= len(obj):
                raise Refus(f"{ou} : « {pointeur} » introuvable (indice {part!r})")
            obj = obj[int(part)]
        elif isinstance(obj, Mapping):
            if part not in obj:
                raise Refus(f"{ou} : « {pointeur} » introuvable (clé {part!r})")
            obj = obj[part]
        else:
            raise Refus(f"{ou} : « {pointeur} » traverse une valeur qui n'est ni objet ni liste")
    return obj


def verifier_correspondance(corr):
    if not isinstance(corr, Mapping) or not isinstance(corr.get("ensembles"), Mapping):
        raise Refus("correspondance : objet avec « ensembles » attendu")
    en_trop = set(corr) - {"piece", "ecrite_utc", "ensembles"}
    if en_trop:
        raise Refus(f"correspondance : clés non permises {sorted(en_trop)}")
    for nom, c in corr["ensembles"].items():
        if nom not in ENSEMBLES:
            raise Refus(f"correspondance : ensemble {nom!r} inconnu ; permis : {list(ENSEMBLES)}")
        if not isinstance(c, Mapping):
            raise Refus(f"correspondance.{nom} : objet attendu")
        manque = {"cartes", "voie", "note"} - set(c)
        if manque:
            raise Refus(f"correspondance.{nom} : clés manquantes {sorted(manque)}")
        en_trop = set(c) - CLES_CORRESPONDANCE
        if en_trop:
            raise Refus(f"correspondance.{nom} : clés non permises {sorted(en_trop)}")
        for liste in ("nombre_vise", "veto"):
            v = c.get(liste)
            if v is None:
                continue
            if not isinstance(v, Mapping) or set(v) not in ({"liste", "id"}, {"liste"}, {"drapeau"}):
                raise Refus(f"correspondance.{nom}.{liste} : {{liste, id}}, {{liste}} ou {{drapeau}} attendu, ou null")


def lire_ensemble(nom, selection, c, ids_connus):
    """Rend {notees: {id: (strate, note)}, listes: {nom: [ids]}, comptes}. Refuse tout identifiant inconnu."""
    ou = f"sélection {nom}"
    brut = suivre(selection, c["cartes"], ou)
    if isinstance(brut, Mapping):
        if c.get("id") not in (None, ""):
            raise Refus(f"correspondance.{nom}.id : null attendu quand « cartes » est un objet {{identifiant: …}}")
        enregistrements = list(brut.items())
    elif isinstance(brut, list):
        if c.get("id") in (None, ""):
            raise Refus(f"correspondance.{nom}.id : pointeur exigé quand « cartes » est une liste")
        enregistrements = [(suivre(r, c["id"], ou), r) for r in brut]
    else:
        raise Refus(f"{ou} : « {c['cartes']} » n'est ni liste ni objet")
    vus, notees, non_notees = set(), {}, 0
    for ident, r in enregistrements:
        if ident not in ids_connus:
            raise Refus(f"{ou} : identifiant {ident!r} absent des {N_CARTES} cartes")
        if ident in vus:
            raise Refus(f"{ou} : identifiant {ident} en double")
        vus.add(ident)
        exclue = suivre(r, c["exclue"], f"{ou}, {ident}") if c.get("exclue") not in (None, "") else False
        if not (exclue is None or isinstance(exclue, (bool, list))):
            raise Refus(f"{ou} : {ident}, « exclue » {exclue!r} illisible (vrai/faux, null ou liste des cas)")
        exclue = bool(exclue)
        # clés exigées dans chaque enregistrement (un pointeur faux est un refus, jamais « non notée » en silence) ;
        # une valeur nulle dit « non notée » et se compte
        voie = suivre(r, c["voie"], f"{ou}, {ident}")
        note = suivre(r, c["note"], f"{ou}, {ident}")
        if exclue or voie in (None, "", []) or note is None:
            non_notees += 1
            continue
        if isinstance(note, bool) or not isinstance(note, (int, float)) or not math.isfinite(note):
            raise Refus(f"{ou} : {ident}, note {note!r} non numérique")
        notees[ident] = (normaliser_strate(voie, ou, ident), float(note))
    listes = {}
    if notees:
        nmax = max(n for _, n in notees.values())
        listes["note_maximale"] = sorted(i for i, (_, n) in notees.items() if abs(n - nmax) <= TOL)
    else:
        nmax = None
    for liste in ("nombre_vise", "veto"):
        v = c.get(liste)
        if v is None:
            continue
        if "drapeau" in v:
            ids = []
            for i, r in enregistrements:
                d = suivre(r, v["drapeau"], f"{ou}, {i}")
                if not (d is None or isinstance(d, bool)):
                    raise Refus(f"{ou} : {i}, drapeau « {v['drapeau']} » {d!r} non booléen")
                if d:
                    ids.append(i)
        else:
            elems = suivre(selection, v["liste"], ou)
            if not isinstance(elems, list):
                raise Refus(f"{ou} : « {v['liste']} » n'est pas une liste")
            ids = [suivre(e, v.get("id"), ou) for e in elems]
        for i in ids:
            if i not in ids_connus:
                raise Refus(f"{ou}, liste {liste} : identifiant {i!r} absent des {N_CARTES} cartes")
        listes[liste] = ids
    return {"notees": notees, "listes": listes, "note_maximale_valeur": nmax,
            "cartes_dans_la_selection": len(vus), "non_notees": non_notees}


def normaliser_strate(voie, ou, ident):
    if isinstance(voie, str) and voie.strip():
        return voie.strip()
    if isinstance(voie, list) and voie and all(isinstance(x, str) and x.strip() for x in voie):
        return "|".join(sorted({x.strip() for x in voie}))
    raise Refus(f"{ou} : {ident}, voie {voie!r} illisible")


# ---------------------------------------------------------------- permutations stratifiées et calcul exact
def permutations_stratifiees(etiquettes, strates, n, rng):
    """Matrice n × len(etiquettes) : chaque ligne permute les étiquettes à l'intérieur de chaque strate, et seulement là.

    Les strates sont prises dans l'ordre trié ; l'appel au générateur est un `permuted` par strate, toujours dans cet ordre."""
    etiquettes = np.asarray(etiquettes, dtype=np.int8)
    strates = np.asarray(strates, dtype=object)
    sortie = np.empty((n, len(etiquettes)), dtype=np.int8)
    for s in sorted(set(strates.tolist())):
        idx = np.flatnonzero(strates == s)
        bloc = np.broadcast_to(etiquettes[idx], (n, len(idx))).copy()
        sortie[:, idx] = rng.permuted(bloc, axis=1)
    return sortie


def loi_exacte(par_strate):
    """par_strate : [(N_s, F_s, n_s)] → {k: probabilité} du nombre de cartes de la famille dans la liste (hypergéométriques
    indépendantes par strate, convoluées), en fractions exactes."""
    loi = {0: Fraction(1)}
    for N_s, F_s, n_s in par_strate:
        tot = math.comb(N_s, n_s)
        h = {j: Fraction(math.comb(F_s, j) * math.comb(N_s - F_s, n_s - j), tot)
             for j in range(max(0, n_s - (N_s - F_s)), min(F_s, n_s) + 1)}
        nouv = {}
        for a, pa in loi.items():
            for b, pb in h.items():
                nouv[a + b] = nouv.get(a + b, 0) + pa * pb
        loi = nouv
    return loi


def holm(ps):
    """ps : {cle: p} → {cle: p ajustée de Holm}."""
    ordre = sorted(ps, key=lambda k: (ps[k], k))
    m, cour, adj = len(ordre), 0.0, {}
    for j, k in enumerate(ordre):
        cour = max(cour, min(1.0, (m - j) * ps[k]))
        adj[k] = cour
    return adj


def calculer_ensemble(nom, lu, especes, rng, n_perm=N_PERMUTATIONS):
    """Statistiques d'un ensemble (sans verdict ; le verdict vient après Holm, dans `lire`)."""
    connues = {i: e for i, e in especes.items() if e is not None}
    fam94 = sum(1 for e in connues.values() if e in FAMILLE_DES_LECTEURS)
    base_94 = fam94 / len(connues) if connues else float("nan")
    pop_tout = sorted(lu["notees"])
    sans_espece_pop = [i for i in pop_tout if especes.get(i) is None]
    pop = [i for i in pop_tout if especes.get(i) is not None]
    pos = {i: k for k, i in enumerate(pop)}
    strates = [lu["notees"][i][0] for i in pop]
    lab = np.array([1 if especes[i] in FAMILLE_DES_LECTEURS else 0 for i in pop], dtype=np.int8)
    base_notees = float(lab.mean()) if len(pop) else float("nan")
    perm = permutations_stratifiees(lab, strates, n_perm, rng) if len(pop) else np.zeros((n_perm, 0), np.int8)
    par_lignee_94 = {l: sum(1 for e in connues.values() if e == l) for l in LIGNEES}
    par_lignee_pop = {l: sum(1 for i in pop if especes[i] == l) for l in LIGNEES}
    res = {"cartes_dans_la_selection": lu["cartes_dans_la_selection"], "non_notees": lu["non_notees"],
           "population_notees": len(pop_tout), "population_sans_espece": len(sans_espece_pop),
           "population_famille": int(lab.sum()), "note_maximale_valeur": lu["note_maximale_valeur"],
           "base_famille_sur_94": base_94, "base_famille_parmi_notees": base_notees,
           "strates": {s: {"n": strates.count(s), "famille": int(sum(lab[k] for k in range(len(pop)) if strates[k] == s))}
                       for s in sorted(set(strates))},
           "listes": {}}
    for liste in LISTES:
        if liste not in lu["listes"]:
            res["listes"][liste] = {"sans_objet": "liste absente de la correspondance ou de la sélection"}
            continue
        brut = lu["listes"][liste]
        uniques = list(dict.fromkeys(brut))
        dedans = sorted(i for i in uniques if i in pos)
        hors = len([i for i in uniques if i not in lu["notees"]])
        sans_esp = len([i for i in uniques if i in lu["notees"] and especes.get(i) is None])
        idx = np.array([pos[i] for i in dedans], dtype=int)
        n_l = len(dedans)
        k_l = int(lab[idx].sum()) if n_l else 0
        par_s = []
        attendu = 0.0
        for s in sorted(set(strates)):
            N_s = strates.count(s)
            F_s = int(sum(lab[k] for k in range(len(pop)) if strates[k] == s))
            n_s = int(sum(1 for i in dedans if lu["notees"][i][0] == s))
            par_s.append((N_s, F_s, n_s))
            attendu += n_s * F_s / N_s
        t_obs = k_l - attendu
        if n_l:
            kstar = perm[:, idx].sum(axis=1).astype(float)
            tstar = kstar - attendu
            p_bil = (1 + int(np.sum(np.abs(tstar) >= abs(t_obs) - TOL))) / (n_perm + 1)
            p_sup = (1 + int(np.sum(tstar >= t_obs - TOL))) / (n_perm + 1)
            p_inf = (1 + int(np.sum(tstar <= t_obs + TOL))) / (n_perm + 1)
            loi = loi_exacte(par_s)
            p_exact = float(sum(p for k, p in loi.items() if abs(k - attendu) >= abs(t_obs) - TOL))
            p_min = min(float(sum(p for k2, p in loi.items() if abs(k2 - attendu) >= abs(k - attendu) - TOL))
                        for k in loi)
        else:
            p_bil = p_sup = p_inf = p_exact = p_min = float("nan")
        part = k_l / n_l if n_l else float("nan")
        lignees = {}
        for l in LIGNEES:
            k = sum(1 for i in dedans if especes[i] == l)
            lignees[l] = {"n_liste": k, "part_liste": k / n_l if n_l else float("nan"),
                          "part_base_94": par_lignee_94[l] / len(connues) if connues else float("nan"),
                          "part_base_notees": par_lignee_pop[l] / len(pop) if pop else float("nan")}
            lignees[l]["ecart_base_94"] = lignees[l]["part_liste"] - lignees[l]["part_base_94"]
            lignees[l]["ecart_base_notees"] = lignees[l]["part_liste"] - lignees[l]["part_base_notees"]
        res["listes"][liste] = {
            "n_liste_deposee": len(brut), "doublons_retires": len(brut) - len(uniques),
            "hors_population": hors, "sans_espece": sans_esp,
            "n_liste": n_l, "famille_liste": k_l, "part_famille_liste": part,
            "ecart_base_94": part - base_94, "ecart_base_notees": part - base_notees,
            "attendu_stratifie": attendu, "ecart_stratifie": t_obs, "liste_egale_population": n_l == len(pop) and n_l > 0,
            "par_strate": {s: {"n_population": a, "famille_population": b, "n_liste": c}
                           for s, (a, b, c) in zip(sorted(set(strates)), par_s)},
            "p_permutation_bilaterale": p_bil, "p_permutation_famille_plus": p_sup, "p_permutation_famille_moins": p_inf,
            "p_exacte_bilaterale": p_exact, "p_minimale_atteignable": p_min, "permutations": n_perm,
            "par_lignee_descriptif": lignees}
    return res


# ---------------------------------------------------------------- règle de lecture (texte scellé, § 5)
def lire(resultats, totaux_conformes):
    raisons, testables = {}, {}
    for nom, r in resultats.items():
        for liste, t in r["listes"].items():
            if "sans_objet" in t:
                continue
            cle = f"{nom}/{liste}"
            rs = []
            if not totaux_conformes:
                rs.append("comptes par lignée des 94 cartes différents de la pièce 2af9e67f")
            if r["population_sans_espece"] or t["sans_espece"]:
                rs.append("carte sans espèce dans la population ou la liste")
            if t["n_liste"] < N_MIN_LISTE:
                rs.append(f"liste de moins de {N_MIN_LISTE} cartes dans la population")
            if r["population_famille"] in (0, r["population_notees"]):
                rs.append("famille absente ou seule dans la population")
            if t["liste_egale_population"]:
                rs.append("la liste est la population entière")
            if not (t["p_minimale_atteignable"] <= ALPHA):
                rs.append("p minimale atteignable au-dessus de 0,05 (effectifs trop petits)")
            raisons[cle] = rs
            if not rs:
                testables[cle] = t
    adj_perm = holm({k: t["p_permutation_bilaterale"] for k, t in testables.items()})
    adj_exact = holm({k: t["p_exacte_bilaterale"] for k, t in testables.items()})
    verdicts = {}
    for cle, rs in raisons.items():
        nom, liste = cle.split("/")
        t = resultats[nom]["listes"][liste]
        v = {"raisons_non_concluant": rs, "tests_dans_holm": len(testables)}
        if rs:
            v["verdict"] = "non concluant"
        else:
            v["p_holm_permutation"] = adj_perm[cle]
            v["p_holm_exacte"] = adj_exact[cle]
            a, b = adj_perm[cle] <= ALPHA, adj_exact[cle] <= ALPHA
            if a and b:
                v["verdict"] = "signal présent"
                v["sens"] = "famille des lecteurs sur-représentée" if t["ecart_stratifie"] > 0 \
                    else "famille des lecteurs sous-représentée"
            elif not a and not b:
                v["verdict"] = "absent"
                v["indice_brut_p_permutation_sous_0_05"] = t["p_permutation_bilaterale"] <= ALPHA
            else:
                v["verdict"] = "non concluant"
                v["raisons_non_concluant"] = ["permutation et calcul exact de part et d'autre du seuil après Holm"]
        t["lecture"] = v
        verdicts[cle] = v["verdict"]
    signal = any(v == "signal présent" for v in verdicts.values())
    return {"verdicts": verdicts, "signal_present_quelque_part": signal,
            "audit_R4_declenche": signal,
            "rappel": "un signal présent déclenche l'audit R4, dans un sens comme dans l'autre ; il ne décide de rien "
                      "sur aucune carte et ne change aucune liste ; aucune revendication"}


# ---------------------------------------------------------------- sorties
def ecrire_neuf(chemin, texte):
    if os.path.exists(chemin) or os.path.exists(chemin + ".sha256"):
        raise Refus(f"{chemin} existe déjà : on n'écrase jamais (R12)")
    with open(chemin, "x", encoding="utf-8") as fh:
        fh.write(texte)
    h = sha256_fichier(chemin)
    with open(chemin + ".sha256", "x", encoding="utf-8") as fh:
        fh.write(f"{h}  {os.path.basename(chemin)}\n")
    return h


def sans_nan(x):
    if isinstance(x, float) and math.isnan(x):
        return None
    if isinstance(x, dict):
        return {k: sans_nan(v) for k, v in x.items()}
    if isinstance(x, list):
        return [sans_nan(v) for v in x]
    return x


def _f(x, n=3):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "—"
    return f"{x:.{n}f}".replace(".", ",")


def _p(x):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "—"
    return (f"{x:.1e}" if x < 1e-3 else f"{x:.4f}").replace(".", ",")


def resume(out):
    l = [f"# Statistique de famille du rejeu à blanc v3 — résumé ({out['programme']['version']})", ""]
    if out["essai_synthetique"]:
        l += ["**ESSAI SUR DONNÉES SYNTHÉTIQUES : sans valeur pour la course v9.**", ""]
    lec = out["lecture"]
    l += [f"- Signal présent quelque part : **{'oui' if lec['signal_present_quelque_part'] else 'non'}** ; audit R4 "
          f"déclenché : {'oui' if lec['audit_R4_declenche'] else 'non'}.",
          f"- Comptes par lignée des 94 cartes conformes à la pièce 2af9e67f : "
          f"{'oui' if out['especes']['totaux_conformes_a_la_piece'] else 'NON'} ; sans espèce : {out['especes']['sans_espece']}.",
          f"- Famille des lecteurs (Opus et Fable) sur les 94 : {out['especes']['famille_des_lecteurs_sur_94']}.",
          f"- {lec['rappel']}.", "",
          "| ensemble | liste | n | famille | part | base 94 | base notées | écart à la base notées | "
          "écart stratifié (cartes) | p perm. | p exacte | p Holm (perm.) | verdict |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for nom, r in out["ensembles"].items():
        for liste, t in r["listes"].items():
            if "sans_objet" in t:
                l.append(f"| {nom} | {liste} | | | | | | | | | | | sans objet |")
                continue
            v = t["lecture"]
            l.append(f"| {nom} | {liste} | {t['n_liste']} | {t['famille_liste']} | {_f(t['part_famille_liste'], 2)} | "
                     f"{_f(r['base_famille_sur_94'], 2)} | {_f(r['base_famille_parmi_notees'], 2)} | "
                     f"{_f(t['ecart_base_notees'], 2)} | {_f(t['ecart_stratifie'], 2)} | "
                     f"{_p(t['p_permutation_bilaterale'])} | {_p(t['p_exacte_bilaterale'])} | "
                     f"{_p(v.get('p_holm_permutation'))} | {v['verdict']}"
                     + (f" ({v['sens']})" if "sens" in v else "")
                     + (f" — {'; '.join(v['raisons_non_concluant'])}" if v["verdict"] == "non concluant" else "") + " |")
    l += ["", "Par lignée : descriptif seulement, sans test (voir la sortie JSON, `par_lignee_descriptif`).", ""]
    return "\n".join(l)


def executer(args):
    if tuple(int(x) for x in np.__version__.split(".")[:2]) < (1, 25):
        raise Refus(f"numpy {np.__version__} : 1.25 au moins exigé (R9)")
    noms = [s[0] for s in args.selection]
    if len(set(noms)) != len(noms) or not set(noms) <= set(ENSEMBLES) or not noms:
        raise Refus(f"--selection : noms {noms} ; chacun au plus une fois, parmi {list(ENSEMBLES)}")
    for chemin in (args.sortie, args.resume):
        if os.path.exists(chemin) or os.path.exists(chemin + ".sha256"):
            raise Refus(f"{chemin} existe déjà : on n'écrase jamais (R12)")
    # 1. toutes les empreintes, avant toute lecture
    emp = {"fiches": verifier_empreinte("fiches", args.fiches, args.sha_fiches),
           "correspondance": verifier_empreinte("correspondance", args.correspondance, args.sha_correspondance)}
    for nom, chemin, h in args.selection:
        emp[f"selection_{nom}"] = verifier_empreinte(f"sélection {nom}", chemin, h)
    if not args.essai_synthetique and emp["fiches"] != FICHES_SHA256_COURSE_V9:
        raise Refus(f"fiches : {emp['fiches']} n'est pas le fichier de la course v9 ({FICHES_SHA256_COURSE_V9}) ; "
                    "seul --essai-synthetique l'admet, et la sortie est alors marquée sans valeur")
    # 2. correspondance (clés seulement, écrite avant la lecture de l'espèce)
    with open(args.correspondance, encoding="utf-8") as fh:
        corr = json.load(fh)
    verifier_correspondance(corr)
    if set(corr["ensembles"]) != set(noms):
        raise Refus(f"correspondance : ensembles {sorted(corr['ensembles'])} ≠ sélections passées {sorted(noms)}")
    # 3. espèce : une seule clé par carte ; l'objet entier est supprimé aussitôt
    with open(args.fiches, encoding="utf-8") as fh:
        fiches = json.load(fh)
    especes = extraire_especes(fiches)
    del fiches
    if len(especes) != N_CARTES:
        raise Refus(f"fiches : {len(especes)} cartes, {N_CARTES} attendues")
    comptes = {l: sum(1 for e in especes.values() if e == l) for l in LIGNEES}
    sans = sum(1 for e in especes.values() if e is None)
    totaux_ok = comptes == TOTAUX_PIECE and sans == 0
    # 4. sélections
    racine = np.random.SeedSequence(ENTROPIE)
    enfants = racine.spawn(len(ENSEMBLES))
    resultats = {}
    for nom in ENSEMBLES:
        if nom not in noms:
            continue
        chemin = next(c for n, c, _ in args.selection if n == nom)
        with open(chemin, encoding="utf-8") as fh:
            sel = json.load(fh)
        lu = lire_ensemble(nom, sel, corr["ensembles"][nom], set(especes))
        rng = np.random.Generator(np.random.PCG64(enfants[ENSEMBLES.index(nom)]))
        resultats[nom] = calculer_ensemble(nom, lu, especes, rng)
    lecture = lire(resultats, totaux_ok)
    out = {
        "piece": "statistique de famille du rejeu à blanc v3 des critères de sélection, course v9 — sortie du programme v1",
        "essai_synthetique": bool(args.essai_synthetique),
        "heure_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "programme": {"version": VERSION, "sha256": sha256_fichier(os.path.abspath(__file__)),
                      "numpy": np.__version__, "python": sys.version.split()[0]},
        "graines": {"entropie": str(ENTROPIE), "construction": "SeedSequence(int(sha256(b'statistique-famille-rejeu-v3-v1'), "
                    "16)).spawn(4) ; enfant k pour l'ensemble ENSEMBLES[k] = F, O, programme, assemblage ; "
                    "Generator(PCG64(enfant)) ; un permuted par strate, strates triées"},
        "parametres": {"permutations": N_PERMUTATIONS, "alpha": ALPHA, "n_min_liste": N_MIN_LISTE,
                       "famille_des_lecteurs": sorted(FAMILLE_DES_LECTEURS), "champ_espece": ".".join(CHEMIN_ESPECE),
                       "correction": "Holm sur les tests testables (permutation ; calcul exact en contrôle)"},
        "empreintes_entrees": emp,
        "chemins_entrees": {"fiches": args.fiches, "correspondance": args.correspondance,
                            **{f"selection_{n}": c for n, c, _ in args.selection}},
        "especes": {"par_lignee_sur_94": comptes, "sans_espece": sans, "totaux_de_la_piece_2af9e67f": TOTAUX_PIECE,
                    "totaux_conformes_a_la_piece": totaux_ok,
                    "famille_des_lecteurs_sur_94": sum(comptes[l] for l in FAMILLE_DES_LECTEURS)},
        "ensembles": resultats,
        "lecture": lecture,
    }
    texte = json.dumps(sans_nan(out), ensure_ascii=False, indent=1, allow_nan=False) + "\n"
    h_out = ecrire_neuf(args.sortie, texte)
    h_res = ecrire_neuf(args.resume, resume(out))
    return out, h_out, h_res


def analyser_arguments(argv):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--fiches", required=True)
    p.add_argument("--sha-fiches", required=True)
    p.add_argument("--correspondance", required=True)
    p.add_argument("--sha-correspondance", required=True)
    p.add_argument("--selection", nargs=3, action="append", required=True, metavar=("NOM", "CHEMIN", "SHA256"))
    p.add_argument("--sortie", required=True)
    p.add_argument("--resume", required=True)
    p.add_argument("--essai-synthetique", action="store_true")
    return p.parse_args(argv)


def main(argv=None):
    args = analyser_arguments(sys.argv[1:] if argv is None else argv)
    try:
        out, h_out, h_res = executer(args)
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    print(json.dumps({"sortie": args.sortie, "sha256_sortie": h_out, "resume": args.resume, "sha256_resume": h_res,
                      "verdicts": out["lecture"]["verdicts"],
                      "signal_present_quelque_part": out["lecture"]["signal_present_quelque_part"]},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
