#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemblage de deux lectures selon les critères de choix des cartes v4 — v2.

v2 (corrections de la contre-lecture ee578a61…), pour les critères v5 ; seule la commande
`gardes` change, l'assemblage et les tiers sont ceux de la v1 :
  C4  `gardes` reçoit les deux sorties du lecteur par programme (cartes non masquées, cartes
      masquées) et rapporte, par espèce et pour la famille des lecteurs, la part des cartes dont
      le D du lecteur par programme baisse sous le masque ; descriptif, ne déclenche rien ;
  C7  garde 2 : sous un filtre du veto, la présence d'un groupe que le filtre retire parmi les
      cartes entrées par veto est nulle par construction ; ce test est « sans objet par
      construction », hors de la correction de Holm, et la garde lit à sa place le veto tel
      que déposé par les titulaires (même rang dans la suite des graines).
Remplace assemblage_selection_v4_v1.py (258d5de7…), gardé sans modification (règle R12).

Ce programme ne tranche rien : il assemble, à la lettre des critères v4, ce que deux lecteurs
ont déposé, et propose ce qui va à l'épreuve. Ce sont les essais qui tranchent (N-058).

Trois commandes :
  assembler  lectures, manifeste d'ouverture, critères scellés -> proposition assemblée ;
  gardes     assemblage + espèces (écrites par la mère, par programme, après le dépôt)
             -> les deux gardes de l'échelle fine, statistique et seuil (critères v4, § 5.3) ;
  tiers      un ordre de passage -> part de chaque voie, sous-strate et espèce par tiers.

Il ne lit aucune carte, aucun champ `meta`, aucun fichier de cartes. L'espèce n'entre que par
la table que la mère lui passe ; `assembler` ne s'en sert que pour le filtre du veto.
Tout refus rend le code 2 et n'écrit rien. Aucun repli silencieux (règle R5).
Graines : numpy.random.SeedSequence (règle R9). Bibliothèque standard et numpy.
"""
import argparse
import hashlib
import json
import os
import sys

import numpy as np

VERSION = "assemblage_selection_v4_v2"
VOIES = ["I", "N", "P"]
SOUS_STRATES = ["a", "b", "c1", "c2", "c3", "d", "e"]
CAS = ["X1", "X2", "X3", "X4", "X5"]
ITEMS = ["T1", "T2", "T3", "T4", "B1", "B2", "B3", "B4",
         "A1", "A1i", "A2", "A3", "A4", "A4i", "S1", "S2", "S3", "S4"]
AJOUTABLES = {"T3", "B2", "B3", "B4", "S1", "S3", "S4"}
IDEE = {"T1", "T2", "T4", "A1", "A1i", "A2", "A3", "A4", "A4i", "S2"}
REPONSES = {"oui", "non", "indecidable", "ajoutable"}
REGIMES = ["tous", "ajoutables_oui", "idee_d_abord"]
CLES_INTERDITES = {"meta", "espece", "proposeur", "contenu"}
CLES_MANIFESTE = {
    "identifiant_course", "usage", "ligne_accord", "criteres_sha256", "nombre_vise",
    "veto_par_titulaire", "suppleantes", "filtre_veto", "plafond_veto", "regime_items",
    "seuil_accord", "lignee_reconnue_declaree", "emploie_lectures_v2", "familles",
    "hors_choix", "cartes_attendues"}
N_PERMUTATIONS = 10000
SEUIL_GARDE = 0.05
MINIMUM_GARDE = 3
TOL = 1e-12

LIMITE_FAMILLE = ("Limite : les deux lecteurs sont d'une même famille ; aucun lecteur d'une autre "
                  "famille n'est disponible sans dépense ; un écart par famille n'est pas séparable "
                  "de la préférence pour soi.")
SIGNAL_V2 = ("Rappel pour tout assemblage qui emploie les lectures v2 : signal « famille des "
             "lecteurs » de l'audit de symétrie (11 cartes sur 16 de la famille à la note maximale, "
             "contre 1 sur 46 hors d'elle ; audit-symetrie-rejeu-v2-v1.md, sha256 ff814fc9…), "
             "passé par le critère D du lecteur F ; mécanisme indéterminé.")
PRINCIPE = ("Cette pièce ne tranche rien : elle propose ce qui va à l'épreuve ; ce sont les essais "
            "qui tranchent (N-058).")
REJEU = "Rejeu à blanc : aucune valeur de sélection ; la course rejouée n'est pas tenue à l'écart."


class Refus(Exception):
    """Refus explicite : le programme s'arrête, n'écrit rien, rend le code 2."""


# ----------------------------------------------------------------------------- entrées

def sha_octets(b):
    return hashlib.sha256(b).hexdigest()


def sha_fichier(chemin):
    with open(chemin, "rb") as f:
        return sha_octets(f.read())


def lire_json_verifie(chemin, sha_attendu, role):
    if not os.path.isfile(chemin):
        raise Refus(f"{role} : fichier absent ({chemin})")
    attendu = str(sha_attendu).strip().lower()
    if len(attendu) != 64 or any(c not in "0123456789abcdef" for c in attendu):
        raise Refus(f"{role} : empreinte attendue illisible")
    with open(chemin, "rb") as f:
        octets = f.read()
    if sha_octets(octets) != attendu:
        raise Refus(f"{role} : empreinte différente de celle annoncée")
    try:
        return json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise Refus(f"{role} : JSON illisible ({e})")


def verifier_numpy(version=None):
    version = np.__version__ if version is None else version
    try:
        majeur, mineur = (int(x) for x in version.split(".")[:2])
    except ValueError:
        raise Refus(f"version de numpy illisible : {version}")
    if (majeur, mineur) < (1, 25):
        raise Refus(f"numpy {version} : 1.25 au moins exigé (règle R9)")
    return version


def valider_manifeste(m):
    if not isinstance(m, dict):
        raise Refus("manifeste : objet attendu")
    if set(m) != CLES_MANIFESTE:
        raise Refus("manifeste : clés en trop " + str(sorted(set(m) - CLES_MANIFESTE))
                    + ", clés manquantes " + str(sorted(CLES_MANIFESTE - set(m))))
    if not isinstance(m["identifiant_course"], str) or not m["identifiant_course"]:
        raise Refus("manifeste : identifiant de la course vide")
    if m["usage"] not in ("rejeu", "course"):
        raise Refus("manifeste : usage doit être « rejeu » ou « course »")
    if m["usage"] == "course" and not (isinstance(m["ligne_accord"], str) and m["ligne_accord"].strip()):
        raise Refus("manifeste : aucun usage sur une course sans la ligne d'accord de Lazar")
    if not (isinstance(m["nombre_vise"], int) and not isinstance(m["nombre_vise"], bool) and m["nombre_vise"] >= 1):
        raise Refus("manifeste : nombre visé entier, au moins 1")
    if m["veto_par_titulaire"] not in (1, 2, 3, "selon_titulaires") or isinstance(m["veto_par_titulaire"], bool):
        raise Refus("manifeste : veto par titulaire parmi 1, 2, 3 ou « selon_titulaires »")
    if not (isinstance(m["suppleantes"], int) and not isinstance(m["suppleantes"], bool) and m["suppleantes"] >= 0):
        raise Refus("manifeste : nombre de suppléantes entier, positif ou nul")
    if m["filtre_veto"] not in ("famille", "lignee", "aucun"):
        raise Refus("manifeste : filtre du veto parmi « famille », « lignee », « aucun »")
    p = m["plafond_veto"]
    if not (p is None or p == "nombre_vise" or (isinstance(p, int) and not isinstance(p, bool) and p >= 0)):
        raise Refus("manifeste : plafond du veto entier, null ou « nombre_vise »")
    if m["regime_items"] not in REGIMES:
        raise Refus("manifeste : régime des items inconnu")
    s = m["seuil_accord"]
    if isinstance(s, bool) or not isinstance(s, (int, float)) or not (0 < s <= 1):
        raise Refus("manifeste : seuil d'accord dans ]0, 1]")
    for k in ("lignee_reconnue_declaree", "emploie_lectures_v2"):
        if not isinstance(m[k], bool):
            raise Refus(f"manifeste : {k} doit être vrai ou faux")
    if not (isinstance(m["familles"], dict) and m["familles"]
            and all(isinstance(a, str) and isinstance(b, str) for a, b in m["familles"].items())):
        raise Refus("manifeste : table des familles (lignée -> famille) vide ou mal formée")
    if not (isinstance(m["hors_choix"], list) and all(isinstance(x, str) for x in m["hors_choix"])):
        raise Refus("manifeste : liste « hors du choix » (cas X6) mal formée")
    if not (isinstance(m["cartes_attendues"], int) and m["cartes_attendues"] >= 1):
        raise Refus("manifeste : nombre de cartes attendues entier")
    return m


def _texte(v):
    return isinstance(v, str) and bool(v.strip())


def valider_lecture(d, nom, manifeste):
    """Une lecture mal formée est une lecture à refaire : refus, jamais de valeur devinée."""
    if not isinstance(d, dict) or set(d) != {"lecteur", "lignee", "independance", "cartes", "veto"}:
        raise Refus(f"lecture {nom} : clés attendues lecteur, lignee, independance, cartes, veto")
    if d["lecteur"] != nom:
        raise Refus(f"lecture {nom} : le fichier se dit du lecteur {d['lecteur']!r}")
    if d["lignee"] not in manifeste["familles"]:
        raise Refus(f"lecture {nom} : lignée du lecteur absente de la table des familles")
    if not _texte(d["independance"]):
        raise Refus(f"lecture {nom} : déclaration d'indépendance absente")
    if not isinstance(d["cartes"], list) or not d["cartes"]:
        raise Refus(f"lecture {nom} : aucune carte")
    cartes = {}
    attendues = {"id", "exclusion", "voie", "sous_strate", "question", "E", "Q", "D", "raisons",
                 "items", "phrases", "groupe_fusion"}
    if manifeste["lignee_reconnue_declaree"]:
        attendues = attendues | {"lignee_reconnue"}
    for c in d["cartes"]:
        if not isinstance(c, dict):
            raise Refus(f"lecture {nom} : enregistrement de carte mal formé")
        if set(c) & CLES_INTERDITES:
            raise Refus(f"lecture {nom} : clé interdite {sorted(set(c) & CLES_INTERDITES)} — aucun lecteur ne lit l'espèce")
        ident = c.get("id")
        if not _texte(ident):
            raise Refus(f"lecture {nom} : identifiant de carte absent")
        if set(c) != attendues:
            raise Refus(f"lecture {nom}, carte {ident} : clés en trop {sorted(set(c) - attendues)}, "
                        f"manquantes {sorted(attendues - set(c))}")
        if ident in cartes:
            raise Refus(f"lecture {nom} : carte {ident} en double")
        ex = c["exclusion"]
        if ex is not None:
            if not isinstance(ex, dict) or ex.get("cas") not in CAS or not _texte(ex.get("phrase")):
                raise Refus(f"lecture {nom}, carte {ident} : exclusion sans cas (X1 à X5) ou sans phrase")
            if ex["cas"] == "X1":
                if set(ex) != {"cas", "phrase", "separable"} or not isinstance(ex["separable"], bool):
                    raise Refus(f"lecture {nom}, carte {ident} : X1 exige « separable » vrai ou faux")
            elif set(ex) != {"cas", "phrase"}:
                raise Refus(f"lecture {nom}, carte {ident} : clés d'exclusion en trop")
        if c["voie"] not in VOIES:
            raise Refus(f"lecture {nom}, carte {ident} : voie inconnue")
        if c["voie"] == "P":
            if c["sous_strate"] not in SOUS_STRATES:
                raise Refus(f"lecture {nom}, carte {ident} : voie P sans sous-strate")
        elif c["sous_strate"] is not None:
            raise Refus(f"lecture {nom}, carte {ident} : sous-strate hors de la voie P")
        if not (c["question"] is None or _texte(c["question"])):
            raise Refus(f"lecture {nom}, carte {ident} : question mal formée")
        if c["voie"] == "N" and c["question"] is None and c["Q"] != 0:
            raise Refus(f"lecture {nom}, carte {ident} : voie N sans question écrite et Q non nul")
        for k in ("E", "Q", "D"):
            if isinstance(c[k], bool) or c[k] not in (0, 1, 2):
                raise Refus(f"lecture {nom}, carte {ident} : note {k} hors de 0, 1, 2")
        if not isinstance(c["raisons"], dict) or set(c["raisons"]) != {"E", "Q", "D"} \
                or not all(_texte(v) for v in c["raisons"].values()):
            raise Refus(f"lecture {nom}, carte {ident} : une note sans raison est une lecture à refaire")
        if not isinstance(c["items"], dict) or set(c["items"]) != set(ITEMS):
            raise Refus(f"lecture {nom}, carte {ident} : les dix-huit réponses sont exigées")
        for it, r in c["items"].items():
            if r not in REPONSES:
                raise Refus(f"lecture {nom}, carte {ident}, item {it} : réponse inconnue")
            if r == "ajoutable" and it not in AJOUTABLES:
                raise Refus(f"lecture {nom}, carte {ident}, item {it} : « ajoutable » n'existe pas pour cet item")
        if not isinstance(c["phrases"], dict) or set(c["phrases"]) != set(ITEMS) \
                or not all(_texte(v) for v in c["phrases"].values()):
            raise Refus(f"lecture {nom}, carte {ident} : chaque réponse porte sa phrase")
        if not (c["groupe_fusion"] is None or _texte(c["groupe_fusion"])):
            raise Refus(f"lecture {nom}, carte {ident} : groupe de fusion mal formé")
        if manifeste["lignee_reconnue_declaree"] and not _texte(c["lignee_reconnue"]):
            raise Refus(f"lecture {nom}, carte {ident} : lignée reconnue à déclarer (« aucune » permis)")
        cartes[ident] = c
    veto = valider_liste_veto(d["veto"], f"lecture {nom}")
    return {"nom": nom, "lignee": d["lignee"], "cartes": cartes, "veto": veto}


def valider_liste_veto(liste, role):
    if not isinstance(liste, list):
        raise Refus(f"{role} : liste de veto mal formée")
    vus = set()
    for v in liste:
        if not isinstance(v, dict) or set(v) != {"id", "prediction", "decision", "lignee_reconnue"}:
            raise Refus(f"{role} : chaque veto porte id, prediction, decision, lignee_reconnue")
        if not all(_texte(v[k]) for k in ("id", "prediction", "decision", "lignee_reconnue")):
            raise Refus(f"{role} : veto sans prédiction, sans décision ou sans lignée reconnue déclarée")
        if v["id"] in vus:
            raise Refus(f"{role} : carte {v['id']} deux fois dans la liste de veto")
        vus.add(v["id"])
    return liste


# ----------------------------------------------------------------------------- outils

def valeur(reponse, regime):
    if reponse == "oui":
        return 1
    if reponse == "ajoutable" and regime == "ajoutables_oui":
        return 1
    return 0


def items_de_voie(voie):
    if voie == "I":
        return [i for i in ITEMS if i not in ("A1", "A4")]
    return [i for i in ITEMS if i not in ("A1i", "A4i")]


def kappa_binaire(a, b):
    """Kappa de Cohen pour deux suites de 0 et 1 ; None s'il n'est pas défini."""
    n = len(a)
    if n == 0:
        return None
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    if abs(1 - pe) < TOL:
        return None
    return (po - pe) / (1 - pe)


def kappa_categories(a, b):
    n = len(a)
    if n == 0:
        return None
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    cats = set(a) | set(b)
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    if abs(1 - pe) < TOL:
        return None
    return (po - pe) / (1 - pe)


def holm(ps):
    """p ajustées de Holm, dans l'ordre d'entrée."""
    m = len(ps)
    ordre = sorted(range(m), key=lambda i: ps[i])
    ajust, courant = [0.0] * m, 0.0
    for rang, i in enumerate(ordre):
        courant = max(courant, min(1.0, (m - rang) * ps[i]))
        ajust[i] = courant
    return ajust


def graines(h1, h2, n):
    racine = np.random.SeedSequence([int(h1, 16), int(h2, 16)])
    return [np.random.Generator(np.random.PCG64(e)) for e in racine.spawn(n)]


def canon(ids):
    return sorted(ids, key=lambda s: s.encode("utf-8"))


# ----------------------------------------------------------------------------- cœur

def statut_des_cartes(lf, lo):
    """Écartée : même cas chez les deux. X1 : rendue à Lazar si les deux la disent non séparable."""
    statut, reserves = {}, {}
    for ident in lf["cartes"]:
        ef, eo = lf["cartes"][ident]["exclusion"], lo["cartes"][ident]["exclusion"]
        r = []
        st = "notee"
        if ef and eo and ef["cas"] == eo["cas"]:
            if ef["cas"] == "X1":
                if not ef["separable"] and not eo["separable"]:
                    st = "rendue_a_lazar"
                elif ef["separable"] and eo["separable"]:
                    r.append("X1 séparable selon les deux lecteurs : gardée pour sa mesure seule")
                else:
                    r.append("X1 vu par les deux lecteurs, séparabilité en désaccord : notée, signalée à Lazar")
            else:
                st = "ecartee"
        else:
            if ef and eo:
                r.append(f"cas différents ({ef['cas']} chez F, {eo['cas']} chez O) : notée")
            elif ef:
                r.append(f"{ef['cas']} vu par F seul : notée")
            elif eo:
                r.append(f"{eo['cas']} vu par O seul : notée")
        statut[ident], reserves[ident] = st, r
    return statut, reserves


def tenue_des_items(lf, lo, notees, regime, seuil):
    table, gardes = {}, set()
    for it in ITEMS:
        a = [valeur(lf["cartes"][c]["items"][it], regime) for c in notees]
        b = [valeur(lo["cartes"][c]["items"][it], regime) for c in notees]
        n = len(notees)
        accord = sum(1 for x, y in zip(a, b) if x == y) / n if n else None
        garde = accord is not None and accord >= seuil - TOL
        deux_oui = sum(1 for x, y in zip(a, b) if x == 1 and y == 1) / n if n else None
        deux_non = sum(1 for x, y in zip(a, b) if x == 0 and y == 0) / n if n else None
        kap = kappa_binaire(a, b)
        indec = [sum(1 for c in notees if l["cartes"][c]["items"][it] == "indecidable") / n if n else None
                 for l in (lf, lo)]
        ajout = [sum(1 for c in notees if l["cartes"][c]["items"][it] == "ajoutable") / n if n else None
                 for l in (lf, lo)]
        table[it] = {
            "accord_brut": accord, "kappa": kap, "garde_dans_le_rang": garde,
            "part_oui_F": sum(a) / n if n else None, "part_oui_O": sum(b) / n if n else None,
            "part_indecidable_F": indec[0], "part_indecidable_O": indec[1],
            "part_ajoutable_F": ajout[0], "part_ajoutable_O": ajout[1],
            "sans_pouvoir_de_ranger": n > 0 and max(deux_oui, deux_non) > 0.9,
            "garde_sans_accord_au_dela_du_hasard": garde and (kap is None or kap <= 0),
        }
        if garde:
            gardes.add(it)
    return table, gardes


def cles(cf, co, voie_f, voie_o, gardes, regime, numero):
    """Clés du rang (critères v4, § 10), la plus haute d'abord. Items gardés seulement."""
    itf = [i for i in items_de_voie(voie_f) if i in gardes]
    ito = [i for i in items_de_voie(voie_o) if i in gardes]
    vf = {i: valeur(cf["items"][i], regime) for i in itf}
    vo = {i: valeur(co["items"][i], regime) for i in ito}
    nf, no = sum(vf.values()), sum(vo.values())

    def axe(a):
        return sum(v for i, v in vf.items() if i[0] == a) + sum(v for i, v in vo.items() if i[0] == a)

    base = (nf + no, cf["Q"] + co["Q"], axe("T"), axe("A"), axe("B"), axe("S"), -abs(nf - no), -numero)
    if regime == "idee_d_abord":
        idee = sum(v for i, v in vf.items() if i in IDEE) + sum(v for i, v in vo.items() if i in IDEE)
        return (idee,) + base
    return base


def noms_des_cles(regime):
    noms = ["1", "2", "3", "4", "5", "6", "7", "8"]
    return (["1 (idée)", "1 bis"] + noms[1:]) if regime == "idee_d_abord" else noms


def au_plancher(c):
    return c["E"] >= 1 and c["Q"] >= 1 and c["D"] >= 1 and c["E"] + c["Q"] + c["D"] >= 4


def construire_lignes(lf, lo, notees, gardes, regime, numero):
    """Fusion : même groupe chez les deux lecteurs. Porteur : au plancher d'abord, puis clés
    de référence (chaque lecteur sous sa propre voie), puis numéro de tirage de la CARTE."""
    groupes = {}
    for c in notees:
        gf, go = lf["cartes"][c]["groupe_fusion"], lo["cartes"][c]["groupe_fusion"]
        cle = ("fusion", gf, go) if (gf is not None and go is not None) else ("seule", c, None)
        groupes.setdefault(cle, []).append(c)
    lignes = []
    for cle, membres in groupes.items():
        def ref(c):
            cf, co = lf["cartes"][c], lo["cartes"][c]
            pl = 1 if (au_plancher(cf) or au_plancher(co)) else 0
            return (pl,) + cles(cf, co, cf["voie"], co["voie"], gardes, regime, numero[c])
        membres = sorted(membres, key=ref, reverse=True)
        p = membres[0]
        cf, co = lf["cartes"][p], lo["cartes"][p]
        sous = sorted({x["sous_strate"] for x in (cf, co) if x["voie"] == "P"})
        lignes.append({
            "porteuse": p, "cartes": canon(membres), "fusion": len(membres) > 1,
            "voies_candidates": sorted({cf["voie"], co["voie"]}), "sous_strates": sous,
            "plancher": bool(au_plancher(cf) or au_plancher(co)),
            "E_au_moins_1": bool(cf["E"] >= 1 or co["E"] >= 1),
        })
    lignes.sort(key=lambda l: l["porteuse"].encode("utf-8"))
    return lignes


def ranger(lignes, lf, lo, gardes, regime, numero, ordre_voies):
    """Affecte chaque ligne à une seule voie, puis rend le rang par voie."""
    def cle_ligne(l, v):
        p = l["porteuse"]
        return cles(lf["cartes"][p], lo["cartes"][p], v, v, gardes, regime, numero[p])

    provisoire = {v: sorted([l for l in lignes if v in l["voies_candidates"]],
                            key=lambda l: cle_ligne(l, v), reverse=True) for v in VOIES}
    for l in lignes:
        cands = l["voies_candidates"]
        if len(cands) == 1:
            l["voie"] = cands[0]
        else:
            pos = {v: provisoire[v].index(l) for v in cands}
            l["voie"] = min(cands, key=lambda v: (pos[v], ordre_voies.index(v)))
        if l["voie"] != "P":
            l["sous_strates"] = []
    rang = {v: sorted([l for l in lignes if l["voie"] == v], key=lambda l: cle_ligne(l, v), reverse=True)
            for v in VOIES}
    for v in VOIES:
        for i, l in enumerate(rang[v]):
            l["rang_dans_la_voie"] = i + 1
            l["cles"] = list(cle_ligne(l, v))
    return rang


def nombre_vise(rang, k, ordre_voies, regime):
    """Deux places réservées par voie, puis tour de rôle ; voie P : sous-strate non couverte d'abord."""
    reste = {v: [l for l in rang[v] if l["plancher"]] for v in VOIES}
    pris, couvertes, noms = [], set(), noms_des_cles(regime)

    def choisir(v):
        if not reste[v]:
            return None
        bassin = reste[v]
        if v == "P":
            neuves = [l for l in reste[v] if set(l["sous_strates"]) - couvertes]
            if neuves:
                bassin = neuves
        l = bassin[0]
        suivant = bassin[1] if len(bassin) > 1 else None
        if suivant is None:
            cle = "sans concurrent"
        else:
            diff = [i for i, (x, y) in enumerate(zip(l["cles"], suivant["cles"])) if x != y]
            cle = noms[diff[0]]
        reste[v].remove(l)
        couvertes.update(l["sous_strates"])
        return {"porteuse": l["porteuse"], "voie": v, "cle_decisive": cle, "ligne": l}

    for tour in ("reservee", "reservee"):
        for v in ordre_voies:
            if len(pris) < k:
                c = choisir(v)
                if c:
                    c["place"] = tour
                    pris.append(c)
    while len(pris) < k and any(reste[v] for v in VOIES):
        for v in ordre_voies:
            if len(pris) < k:
                c = choisir(v)
                if c:
                    c["place"] = "tour de rôle"
                    pris.append(c)
    perdantes = []
    for v in VOIES:
        retenues = [c for c in pris if c["voie"] == v]
        if retenues and reste[v]:
            derniere, premiere = retenues[-1]["ligne"], reste[v][0]
            if derniere["cles"][:-1] == premiere["cles"][:-1]:
                perdantes.append(premiere["porteuse"])
    return pris, perdantes


def resoudre_veto(listes, lignees, v_max, plafond, filtre, familles, especes, statut,
                  ligne_de, visees, ordre_titulaires):
    """Veto : filtre par programme, suppléantes, plafond commun servi par tour de rôle."""
    journal, valides = [], {}
    for t in canon(listes):
        gardes = []
        for rang_depot, v in enumerate(listes[t]):
            c = v["id"]
            motif = None
            if filtre != "aucun":
                if c not in especes:
                    raise Refus(f"veto de {t} : espèce absente pour une carte de la liste — filtre impossible")
                if especes[c] not in familles:
                    raise Refus(f"veto de {t} : lignée {especes[c]!r} hors de la table des familles")
                if filtre == "lignee" and especes[c] == lignees[t]:
                    motif = "retirée : lignée du titulaire"
                if filtre == "famille" and familles[especes[c]] == familles[lignees[t]]:
                    motif = "retirée : famille du titulaire"
            if motif is None and statut[c] != "notee":
                motif = "sans objet : carte écartée ou rendue à Lazar"
            if motif is None and ligne_de[c] in visees:
                motif = "sans objet : déjà dans le nombre visé"
            if motif is None and len(gardes) >= v_max:
                motif = "suppléante non appelée"
            if motif is None:
                gardes.append(v)
            journal.append({"titulaire": t, "rang_depose": rang_depot + 1, "sort": motif or "valide"})
        valides[t] = gardes
    entrees, coupes = {}, 0
    for r in range(v_max):
        for t in ordre_titulaires:
            if r < len(valides[t]):
                v = valides[t][r]
                if v["id"] not in entrees and plafond is not None and len(entrees) >= plafond:
                    coupes += 1
                    continue
                entrees.setdefault(v["id"], []).append(
                    {"titulaire": t, "prediction": v["prediction"], "decision": v["decision"],
                     "lignee_reconnue": v["lignee_reconnue"]})
    comptes = {
        "deposees": sum(len(l) for l in listes.values()),
        "retirees_par_le_filtre": sum(1 for j in journal if j["sort"].startswith("retirée")),
        "sans_objet": sum(1 for j in journal if j["sort"].startswith("sans objet")),
        "suppleantes_non_appelees": sum(1 for j in journal if j["sort"] == "suppléante non appelée"),
        "valides": sum(len(x) for x in valides.values()),
        "coupees_par_le_plafond": coupes,
        "cartes_entrees": len(entrees),
        "lignes_ajoutees": len({ligne_de[c] for c in entrees}),
        "cartes_designees_par_plusieurs_titulaires": sum(1 for x in entrees.values() if len(x) > 1),
    }
    return entrees, comptes, journal


def assembler_coeur(lf, lo, manifeste, h1, especes=None, juges=None, temoin=None):
    m = manifeste
    ids_f, ids_o = set(lf["cartes"]), set(lo["cartes"])
    if ids_f != ids_o:
        raise Refus(f"les deux lectures ne portent pas les mêmes cartes ({len(ids_f ^ ids_o)} d'écart)")
    if ids_f & set(m["hors_choix"]):
        raise Refus("une carte « hors du choix » (cas X6) figure dans une lecture : elle ne devait pas être ouverte")
    if len(ids_f) != m["cartes_attendues"]:
        raise Refus(f"{len(ids_f)} cartes lues, {m['cartes_attendues']} attendues au manifeste")
    toutes = canon(ids_f)
    h2 = sha_octets(m["identifiant_course"].encode("utf-8"))
    g_voies, g_depart, g_lot, g_tit = graines(h1, h2, 4)
    ordre_voies = [VOIES[i] for i in g_voies.permutation(3)]
    perm = g_depart.permutation(len(toutes))
    numero = {toutes[int(j)]: pos for pos, j in enumerate(perm)}

    statut, reserves = statut_des_cartes(lf, lo)
    notees = [c for c in toutes if statut[c] == "notee"]
    listes = {"F": lf["veto"], "O": lo["veto"]}
    lignees = {"F": lf["lignee"], "O": lo["lignee"]}
    for j in (juges or []):
        if j["titulaire"] in listes:
            raise Refus(f"titulaire de veto en double : {j['titulaire']}")
        listes[j["titulaire"]], lignees[j["titulaire"]] = j["veto"], j["lignee"]
    n_tit = len(listes)
    v_force = m["veto_par_titulaire"]
    if v_force == "selon_titulaires":
        v_force = 3 if n_tit <= 3 else 2
    for t, l in listes.items():
        if len(l) > v_force + m["suppleantes"]:
            raise Refus(f"veto de {t} : {len(l)} cartes pour {v_force} et {m['suppleantes']} suppléantes au plus")
        for v in l:
            if v["id"] not in ids_f:
                raise Refus(f"veto de {t} : identifiant inconnu des cartes lues")
    if m["filtre_veto"] != "aucun" and especes is None:
        raise Refus("filtre du veto demandé sans table des espèces : refus, aucun veto n'est laissé sans filtre en silence")
    plafond = m["nombre_vise"] if m["plafond_veto"] == "nombre_vise" else m["plafond_veto"]
    perm_tit = g_tit.permutation(n_tit)
    ordre_titulaires = [canon(listes)[int(i)] for i in perm_tit]

    def jouer(regime, v_max, plaf):
        table, gardes = tenue_des_items(lf, lo, notees, regime, m["seuil_accord"])
        lignes = construire_lignes(lf, lo, notees, gardes, regime, numero)
        rang = ranger(lignes, lf, lo, gardes, regime, numero, ordre_voies)
        pris, perdantes = nombre_vise(rang, m["nombre_vise"], ordre_voies, regime)
        ligne_de = {c: l["porteuse"] for l in lignes for c in l["cartes"]}
        for c in toutes:
            ligne_de.setdefault(c, None)
        visees = {p["porteuse"] for p in pris}
        entrees, comptes, journal = resoudre_veto(
            listes, lignees, v_max, plaf, m["filtre_veto"], m["familles"], especes or {}, statut,
            ligne_de, visees, ordre_titulaires)
        return {"table": table, "gardes": gardes, "lignes": lignes, "rang": rang, "pris": pris,
                "perdantes": perdantes, "ligne_de": ligne_de, "visees": visees, "entrees": entrees,
                "comptes_veto": comptes, "journal_veto": journal}

    r = jouer(m["regime_items"], v_force, plafond)
    lignes_veto = {r["ligne_de"][c] for c in r["entrees"]}
    lot, indices_lot = [], {}
    for v in VOIES:
        vivier = canon([l["porteuse"] for l in r["lignes"] if l["voie"] == v and l["E_au_moins_1"]
                        and l["porteuse"] not in r["visees"] and l["porteuse"] not in lignes_veto])
        if vivier:
            i = int(g_lot.integers(0, len(vivier)))
            indices_lot[v] = {"taille_du_vivier": len(vivier), "indice": i}
            lot.append({"porteuse": vivier[i], "voie": v})
        else:
            indices_lot[v] = {"taille_du_vivier": 0, "indice": None}

    k = m["nombre_vise"]
    cle_dec = [p["cle_decisive"] for p in r["pris"]]
    n8, n7 = cle_dec.count("8"), cle_dec.count("7")
    en_tete = [PRINCIPE, LIMITE_FAMILLE]
    if m["usage"] == "rejeu":
        en_tete.append(REJEU)
    if m["emploie_lectures_v2"]:
        en_tete.append(SIGNAL_V2)
    if n8 > k / 3:
        en_tete.append("Sur cette course, le rang est en bonne part un tirage ; le nombre visé ne se "
                       "distingue pas du lot tiré au sort.")
    if n7 + n8 > k / 3:
        en_tete.append("Plus du tiers des places est décidé par l'écart entre lecteurs (clé 7) ou par "
                       "le tirage (clé 8) : ni l'une ni l'autre ne dit rien de l'épreuve.")

    # strates : garde contre le fourre-tout, chez chacun des lecteurs
    fourre_tout = []
    for nom, l in (("F", lf), ("O", lo)):
        comptes = {}
        for c in notees:
            x = l["cartes"][c]
            s = x["voie"] if x["voie"] != "P" else "P " + x["sous_strate"]
            comptes[s] = comptes.get(s, 0) + 1
        for s, n in sorted(comptes.items()):
            if notees and n > len(notees) / 3:
                fourre_tout.append({"lecteur": nom, "strate": s, "cartes": n, "sur": len(notees)})
    for f in fourre_tout:
        en_tete.append(f"Strate {f['strate']} : {f['cartes']} cartes sur {f['sur']} chez le lecteur "
                       f"{f['lecteur']}, plus du tiers ; non redécoupée après l'ouverture.")

    desaccords = []
    for c in notees:
        cf, co = lf["cartes"][c], lo["cartes"][c]
        d = []
        if (cf["voie"], cf["sous_strate"]) != (co["voie"], co["sous_strate"]):
            d.append("strate")
        for kk in ("E", "Q", "D"):
            if abs(cf[kk] - co[kk]) >= 2:
                d.append(f"écart de deux points sur {kk}")
        for a in "TBAS":
            its = [i for i in ITEMS if i[0] == a and i in r["gardes"]]
            e = abs(sum(valeur(cf["items"][i], m["regime_items"]) for i in its)
                    - sum(valeur(co["items"][i], m["regime_items"]) for i in its))
            if e >= 3:
                d.append(f"écart de trois « oui » ou plus sur l'axe {a}")
        if reserves[c]:
            d.extend(reserves[c])
        if d:
            desaccords.append({"id": c, "desaccords": d})

    # comparaisons écrites d'avance : trois régimes d'items, veto à deux et à trois
    comparaison_regimes = {}
    for reg in REGIMES:
        rr = r if reg == m["regime_items"] else jouer(reg, v_force, plafond)
        comparaison_regimes[reg] = {
            "nombre_vise": [p["porteuse"] for p in rr["pris"]],
            "items_gardes": sorted(rr["gardes"]),
            "places_au_tirage": [p["cle_decisive"] for p in rr["pris"]].count("8"),
            "commun_avec_le_regime_en_vigueur": len({p["porteuse"] for p in rr["pris"]} & r["visees"]),
        }
    comparaison_veto = {}
    for v_alt in (2, 3):
        for nom_p, plaf in (("sans plafond", None), ("plafond au nombre visé", k)):
            # sur les listes telles que déposées : à trois quand deux est en vigueur, la troisième
            # carte est la première suppléante du titulaire
            rr = jouer(m["regime_items"], v_alt, plaf)
            comparaison_veto[f"{v_alt} cartes, {nom_p}"] = dict(
                rr["comptes_veto"], maximum_theorique=v_alt * n_tit, rapport_au_nombre_vise=None if not k
                else round(rr["comptes_veto"]["cartes_entrees"] / k, 4))

    # témoin sans famille : accord de chaque lecteur avec le lecteur par programme
    accord_temoin = None
    if temoin is not None:
        accord_temoin = {}
        for nom, l in (("F", lf), ("O", lo)):
            communs = [c for c in notees if c in temoin]
            vv = [(l["cartes"][c]["voie"], temoin[c]["voie"]) for c in communs if temoin[c]["voie"] is not None]
            dd = [(l["cartes"][c]["D"], temoin[c]["D"]) for c in communs if temoin[c]["D"] is not None]
            accord_temoin[nom] = {
                "voie": {"cartes": len(vv), "accord_brut": (sum(1 for a, b in vv if a == b) / len(vv)) if vv else None,
                         "kappa": kappa_categories([a for a, _ in vv], [b for _, b in vv])},
                "D": {"cartes": len(dd), "accord_brut": (sum(1 for a, b in dd if a == b) / len(dd)) if dd else None,
                      "kappa": kappa_categories([a for a, _ in dd], [b for _, b in dd])},
                "cartes_sans_temoin": len(notees) - len(communs)}

    items_gardes_de_voie = min(len([i for i in items_de_voie(v) if i in r["gardes"]]) for v in VOIES)
    fines = {v: len({l["cles"][0] for l in r["rang"][v]}) for v in VOIES}
    cartes_sortie = []
    veto_titulaires = canon({v["id"] for l in listes.values() for v in l[:v_force]})
    for c in toutes:
        lg = r["ligne_de"][c]
        ligne = next((l for l in r["lignes"] if l["porteuse"] == lg), None)
        cf, co = lf["cartes"][c], lo["cartes"][c]
        note = None
        if ligne is not None:
            note = cles(cf, co, ligne["voie"], ligne["voie"], r["gardes"], "tous" if m["regime_items"] == "idee_d_abord"
                        else m["regime_items"], numero[c])[0]
        cartes_sortie.append({
            "id": c, "statut": statut[c], "exclue": statut[c] != "notee",
            "voie": ligne["voie"] if ligne else None, "note": note, "ligne": lg,
            "au_plancher": bool(au_plancher(cf) or au_plancher(co)) if statut[c] == "notee" else None,
            "dans_le_nombre_vise": lg in r["visees"] if lg else False,
            "entree_par_veto": c in r["entrees"], "numero_de_tirage": numero[c]})

    def nu(l):
        return {k2: v2 for k2, v2 in l.items()}

    return {
        "piece": VERSION, "en_tete": en_tete,
        "parametres": {**{k2: m[k2] for k2 in sorted(m) if k2 not in ("hors_choix", "familles")},
                       "veto_par_titulaire_en_vigueur": v_force, "plafond_veto_en_vigueur": plafond,
                       "titulaires": n_tit, "hors_choix": len(m["hors_choix"])},
        "tirages": {"h1": h1, "identifiant": m["identifiant_course"], "h2": h2, "numpy": np.__version__,
                    "ordre_des_voies": ordre_voies, "permutation_des_cartes": [int(x) for x in perm],
                    "lot": indices_lot, "ordre_des_titulaires": ordre_titulaires},
        "comptes": {"cartes": len(toutes), "notees": len(notees),
                    "ecartees": sum(1 for c in toutes if statut[c] == "ecartee"),
                    "rendues_a_lazar": sum(1 for c in toutes if statut[c] == "rendue_a_lazar"),
                    "lignes": len(r["lignes"]), "lignes_au_plancher": sum(1 for l in r["lignes"] if l["plancher"]),
                    "fusions": sum(1 for l in r["lignes"] if l["fusion"])},
        "items": r["table"],
        "tenue": {"items_gardes": sorted(r["gardes"]), "items_gardes_par_voie_au_moins": items_gardes_de_voie,
                  "notes_fines_distinctes_par_voie": fines, "cle_decisive_par_place": cle_dec,
                  "places_au_tirage_cle_8": n8, "places_a_la_cle_7": n7, "nombre_vise": k,
                  "strates_au_dela_du_tiers": fourre_tout},
        "conditions_du_rejeu": {
            "un_tiers_au_plus_des_places_au_tirage": n8 <= k / 3,
            "huit_items_au_moins_gardes_dans_chaque_voie": items_gardes_de_voie >= 8,
            "rappel": "l'adoption attend aussi les gardes par espèce (commande « gardes ») : tout "
                      "déclenchement renvoie à Lazar avant adoption"},
        "listes": {
            "nombre_vise": [{k2: v2 for k2, v2 in p.items() if k2 != "ligne"} for p in r["pris"]],
            "au_plancher_hors_du_nombre_vise": {
                v: [l["porteuse"] for l in r["rang"][v] if l["plancher"] and l["porteuse"] not in r["visees"]]
                for v in VOIES},
            "a_egalite_perdantes_au_tirage": r["perdantes"],
            "entrees_par_veto": [{"id": c, "ligne": r["ligne_de"][c], "titulaires": t} for c, t in sorted(r["entrees"].items())],
            "tirees_au_sort": lot,
            "rendues_a_lazar": [c for c in toutes if statut[c] == "rendue_a_lazar"],
            "ecartees": [c for c in toutes if statut[c] == "ecartee"],
            "sous_le_plancher": [l["porteuse"] for l in r["lignes"] if not l["plancher"]],
            "veto_depose_titulaires": veto_titulaires,
        },
        "veto": {"comptes": r["comptes_veto"], "journal": r["journal_veto"],
                 "depose": {t: [v["id"] for v in l] for t, l in sorted(listes.items())},
                 "lignees_des_titulaires": lignees},
        "comparaison_des_regimes_d_items": comparaison_regimes,
        "comparaison_des_limites_de_veto": comparaison_veto,
        "lignes": [nu(l) for l in r["lignes"]],
        "desaccords": desaccords,
        "accord_avec_le_lecteur_par_programme": accord_temoin,
        "cartes": cartes_sortie,
    }


# ----------------------------------------------------------------------------- gardes par espèce

def _eta2(valeurs, etiquettes):
    v = np.asarray(valeurs, dtype=float)
    tot = float(((v - v.mean()) ** 2).sum())
    if tot <= TOL:
        return None, None
    inter, groupes = 0.0, sorted(set(etiquettes))
    e = np.asarray(etiquettes)
    for g in groupes:
        x = v[e == g]
        inter += len(x) * float((x.mean() - v.mean()) ** 2)
    intra = tot - inter
    ddl_inter, ddl_intra = len(groupes) - 1, len(v) - len(groupes)
    if ddl_inter < 1 or ddl_intra < 1:
        return inter / tot, None
    f = float("inf") if intra <= TOL else (inter / ddl_inter) / (intra / ddl_intra)
    return inter / tot, f


def _permuter_dans_les_strates(etiquettes, strates, gen):
    e = np.asarray(etiquettes, dtype=object).copy()
    s = np.asarray(strates, dtype=object)
    for st in sorted(set(strates)):
        idx = np.where(s == st)[0]
        e[idx] = gen.permuted(e[idx])
    return e


def garde_item(valeurs, etiquettes, strates, gen, n_perm=N_PERMUTATIONS):
    """Un item sépare-t-il les groupes plus que les cartes à l'intérieur d'un groupe ?
    Statistique : rapport F (carré moyen entre groupes sur carré moyen dans les groupes) et
    part de variance entre groupes ; p par permutation des étiquettes dans chaque voie."""
    comptes = {g: list(etiquettes).count(g) for g in set(etiquettes)}
    gardes_idx = [i for i, g in enumerate(etiquettes) if comptes[g] >= MINIMUM_GARDE]
    exclus = sorted(g for g, n in comptes.items() if n < MINIMUM_GARDE)
    v = [valeurs[i] for i in gardes_idx]
    e = [etiquettes[i] for i in gardes_idx]
    s = [strates[i] for i in gardes_idx]
    if len(set(e)) < 2:
        return {"lecture": "non concluant", "motif": "moins de deux groupes d'au moins trois cartes", "groupes_exclus": exclus}
    eta, f = _eta2(v, e)
    if eta is None:
        return {"lecture": "non concluant", "motif": "item sans variance", "groupes_exclus": exclus}
    plus = 0
    for _ in range(n_perm):
        ep = _permuter_dans_les_strates(e, s, gen)
        x, _f = _eta2(v, list(ep))
        if x is not None and x >= eta - TOL:
            plus += 1
    return {"lecture": "à lire", "part_de_variance_entre_groupes": eta, "rapport_F": f,
            "p": (1 + plus) / (n_perm + 1), "groupes_exclus": exclus, "cartes": len(v)}


def garde_liste(dans_liste, est_du_groupe, strates, gen, n_perm=N_PERMUTATIONS):
    """Écart de présence d'un groupe dans une liste : T = k − attendu stratifié par voie."""
    d, g, s = np.asarray(dans_liste, bool), np.asarray(est_du_groupe, bool), np.asarray(strates, dtype=object)
    n, n_liste, n_groupe = len(d), int(d.sum()), int(g.sum())
    if n_liste < MINIMUM_GARDE:
        return {"lecture": "non concluant", "motif": "liste de moins de trois cartes"}
    if n_groupe == 0 or n_groupe == n:
        return {"lecture": "non concluant", "motif": "groupe absent ou seul"}
    if n_liste == n:
        return {"lecture": "non concluant", "motif": "la liste est la population entière"}

    def stat(gg):
        t = 0.0
        for st in set(strates):
            i = s == st
            t += float((d[i] & gg[i]).sum()) - float(d[i].sum()) * float(gg[i].sum()) / float(i.sum())
        return t
    t_obs, plus = stat(g), 0
    for _ in range(n_perm):
        gp = np.asarray(_permuter_dans_les_strates(g, strates, gen), bool)
        if abs(stat(gp)) >= abs(t_obs) - TOL:
            plus += 1
    return {"lecture": "à lire", "dans_la_liste": int((d & g).sum()), "taille_de_la_liste": n_liste,
            "part_dans_la_liste": float((d & g).sum()) / n_liste, "part_de_base": n_groupe / n,
            "T": t_obs, "p": (1 + plus) / (n_perm + 1)}


def garde_note(notes, est_du_groupe, strates, gen, n_perm=N_PERMUTATIONS):
    """Écart de note fine d'un groupe, centré par voie."""
    x, g, s = np.asarray(notes, float), np.asarray(est_du_groupe, bool), np.asarray(strates, dtype=object)
    if int(g.sum()) < MINIMUM_GARDE or int((~g).sum()) < MINIMUM_GARDE:
        return {"lecture": "non concluant", "motif": "moins de trois cartes d'un côté"}
    c = x.copy()
    for st in set(strates):
        i = s == st
        c[i] = x[i] - x[i].mean()
    if float(np.abs(c).sum()) <= TOL:
        return {"lecture": "non concluant", "motif": "note sans variance dans les voies"}
    t_obs, plus = float(c[g].sum()), 0
    for _ in range(n_perm):
        gp = np.asarray(_permuter_dans_les_strates(g, strates, gen), bool)
        if abs(float(c[gp].sum())) >= abs(t_obs) - TOL:
            plus += 1
    return {"lecture": "à lire", "ecart_moyen_centre": t_obs / int(g.sum()), "cartes_du_groupe": int(g.sum()),
            "p": (1 + plus) / (n_perm + 1)}


def _lire_avec_holm(tests):
    """Applique Holm aux tests « à lire » ; un test non concluant ne se lit ni présent ni absent."""
    lus = [t for t in tests if t["resultat"]["lecture"] == "à lire"]
    ajust = holm([t["resultat"]["p"] for t in lus]) if lus else []
    for t, pa in zip(lus, ajust):
        t["resultat"]["p_holm"] = pa
    return tests


def retire_par_le_filtre(filtre, lignee_carte, lignee_titulaire, familles):
    """Le filtre du veto retire-t-il, pour ce titulaire, toute carte de cette lignée ?"""
    if filtre == "famille":
        return familles[lignee_carte] == familles[lignee_titulaire]
    if filtre == "lignee":
        return lignee_carte == lignee_titulaire
    return False


def groupe_sans_objet_au_veto(filtre, lignees_du_groupe, lignees_des_titulaires, familles):
    """C7 : un groupe est retiré par le filtre si, pour CHAQUE titulaire, le filtre retire toute
    carte de CHACUNE de ses lignées. Sa présence parmi les cartes entrées par veto est alors
    nulle par construction : le test lirait le filtre, non les lecteurs."""
    if filtre == "aucun" or not lignees_des_titulaires or not lignees_du_groupe:
        return False
    for lt in lignees_des_titulaires:
        if lt not in familles:
            raise Refus("gardes : lignée d'un titulaire hors de la table des familles")
    return all(retire_par_le_filtre(filtre, x, lt, familles)
               for x in lignees_du_groupe for lt in lignees_des_titulaires)


def baisse_de_d_sous_le_masque(ids, lignee, familles, famille_des_lecteurs, non_masque, masque):
    """C4 : par espèce et pour la famille des lecteurs, la part des cartes notées dont le D du
    lecteur par programme baisse entre la forme non masquée et la forme masquée. Descriptif :
    aucun test, aucun seuil, ne déclenche rien. Une carte notée absente d'une des deux sorties
    est un refus : rien n'est deviné."""
    for role, t in (("non masquée", non_masque), ("masquée", masque)):
        manquantes = [i for i in ids if i not in t]
        if manquantes:
            raise Refus(f"gardes : {len(manquantes)} carte(s) notée(s) absente(s) de la sortie {role} du "
                        "lecteur par programme — refus, rien n'est deviné")
        for i in ids:
            d = t[i]["D"]
            if not (d is None or (not isinstance(d, bool) and d in (0, 1, 2))):
                raise Refus(f"gardes : D hors de 0, 1, 2 ou null dans la sortie {role} du lecteur par programme")

    def compter(selection):
        c = {"cartes": len(selection), "comparables": 0, "baisse": 0, "hausse": 0, "egal": 0,
             "devenu_indecidable_sous_le_masque": 0, "indecidable_sans_masque": 0}
        for i in selection:
            a, b = non_masque[i]["D"], masque[i]["D"]
            if a is None:
                c["indecidable_sans_masque"] += 1
            elif b is None:
                c["devenu_indecidable_sous_le_masque"] += 1
            else:
                c["comparables"] += 1
                c["baisse" if b < a else ("hausse" if b > a else "egal")] += 1
        c["part_baisse"] = (c["baisse"] / c["comparables"]) if c["comparables"] else None
        return c

    par_lignee = {g: compter([i for i, x in zip(ids, lignee) if x == g]) for g in sorted(set(lignee))}
    sortie = {"par_lignee": par_lignee, "toutes": compter(list(ids)),
              "lecture": "descriptif : part des cartes dont le D du lecteur par programme baisse sous le masque ; "
                         "tant qu'elle n'est pas lue, un écart par famille qui baisse sous le masque ne se lit "
                         "pas comme une préférence retirée (critères v5, § 1)"}
    if famille_des_lecteurs is not None:
        sortie["famille_des_lecteurs"] = compter([i for i, x in zip(ids, lignee) if familles[x] == famille_des_lecteurs])
        sortie["autres"] = compter([i for i, x in zip(ids, lignee) if familles[x] != famille_des_lecteurs])
    return sortie


def gardes_coeur(assemblage, lf, lo, especes, familles, lignees_lecteurs, h1, n_perm=N_PERMUTATIONS,
                 *, temoin_non_masque=None, temoin_masque=None):
    if (temoin_non_masque is None) != (temoin_masque is None):
        raise Refus("gardes : les deux sorties du lecteur par programme (non masquée et masquée) vont ensemble, "
                    "ou aucune")
    cartes = [c for c in assemblage["cartes"] if not c["exclue"]]
    for c in cartes:
        if c["id"] not in especes:
            raise Refus("gardes : une carte notée est sans espèce — rien n'est calculé")
        if especes[c["id"]] not in familles:
            raise Refus("gardes : lignée hors de la table des familles")
    ids = [c["id"] for c in cartes]
    strates = [c["voie"] for c in cartes]
    lignee = [especes[i] for i in ids]
    fam_lecteurs = sorted({familles[l] for l in lignees_lecteurs.values()})
    if len(fam_lecteurs) != 1:
        fam_lecteurs_nom = None
        dans_famille = None
    else:
        fam_lecteurs_nom = fam_lecteurs[0]
        dans_famille = ["famille des lecteurs" if familles[x] == fam_lecteurs_nom else "autres" for x in lignee]
    regime = assemblage["parametres"]["regime_items"]
    h2 = assemblage["tirages"]["h2"]
    racine = np.random.SeedSequence([int(h1, 16), int(h2, 16), int(sha_octets(b"gardes-par-espece-v4-v1"), 16)])
    enfants = iter(racine.spawn(4096))

    def gen():
        return np.random.Generator(np.random.PCG64(next(enfants)))

    # garde 1 : item qui sépare les espèces plus que les cartes d'une même espèce
    tests_items = {"lignee": [], "famille": []}
    for it in ITEMS:
        v = [valeur(lf["cartes"][i]["items"][it], regime) + valeur(lo["cartes"][i]["items"][it], regime) for i in ids]
        tests_items["lignee"].append({"item": it, "resultat": garde_item(v, lignee, strates, gen(), n_perm)})
        if dans_famille is not None:
            tests_items["famille"].append({"item": it, "resultat": garde_item(v, dans_famille, strates, gen(), n_perm)})
    items_nommes = []
    for niveau in ("lignee", "famille"):
        _lire_avec_holm(tests_items[niveau])
        for t in tests_items[niveau]:
            r = t["resultat"]
            if r["lecture"] == "à lire":
                r["nomme"] = bool(r["rapport_F"] is not None and r["rapport_F"] > 1 and r["p_holm"] <= SEUIL_GARDE)
                if r["nomme"]:
                    items_nommes.append({"item": t["item"], "niveau": niveau,
                                         "dans_le_rang": t["item"] in assemblage["tenue"]["items_gardes"]})

    # garde 2 : écart fort d'une espèce dans une liste ou sur la note fine
    listes = {
        "nombre_vise": [c["dans_le_nombre_vise"] for c in cartes],
        "entrees_par_veto": [c["entree_par_veto"] for c in cartes],
        "proposees_en_premier": [c["dans_le_nombre_vise"] or c["entree_par_veto"] for c in cartes],
        "sous_le_plancher": [not c["au_plancher"] for c in cartes],
    }
    groupes = {f"lignée {g}": [x == g for x in lignee] for g in sorted(set(lignee))}
    if dans_famille is not None:
        groupes["famille des lecteurs"] = [x == "famille des lecteurs" for x in dans_famille]
    # C7 : sous un filtre du veto, le test « entrées par veto » d'un groupe que le filtre retire est
    # sans objet par construction ; la garde lit à sa place le veto tel que déposé par les titulaires
    filtre = assemblage["parametres"]["filtre_veto"]
    lignees_titulaires = sorted(set(assemblage["veto"]["lignees_des_titulaires"].values()))
    lignees_du_groupe = {f"lignée {g}": [g] for g in sorted(set(lignee))}
    if dans_famille is not None:
        lignees_du_groupe["famille des lecteurs"] = sorted({x for x in lignee if familles[x] == fam_lecteurs_nom})
    sans_objet = {g: groupe_sans_objet_au_veto(filtre, lg, lignees_titulaires, familles)
                  for g, lg in lignees_du_groupe.items()}
    deposees = set(assemblage["listes"]["veto_depose_titulaires"])
    veto_depose = [c["id"] in deposees for c in cartes]
    tests_ecarts = []
    for nom_g, masque in groupes.items():
        for nom_l, dl in listes.items():
            if nom_l == "entrees_par_veto" and sans_objet[nom_g]:
                tests_ecarts.append({"groupe": nom_g, "objet": nom_l, "resultat": {
                    "lecture": "sans objet par construction",
                    "motif": f"filtre du veto « {filtre} » : aucune carte de ce groupe ne peut entrer par veto ; "
                             "hors de la correction ; lu à sa place : le veto tel que déposé par les titulaires"}})
                tests_ecarts.append({"groupe": nom_g, "objet": "veto_depose_titulaires",
                                     "resultat": garde_liste(veto_depose, masque, strates, gen(), n_perm)})
                continue
            tests_ecarts.append({"groupe": nom_g, "objet": nom_l,
                                 "resultat": garde_liste(dl, masque, strates, gen(), n_perm)})
        tests_ecarts.append({"groupe": nom_g, "objet": "note_fine",
                             "resultat": garde_note([c["note"] for c in cartes], masque, strates, gen(), n_perm)})
    _lire_avec_holm(tests_ecarts)
    ecarts_forts = []
    for t in tests_ecarts:
        r = t["resultat"]
        if r["lecture"] == "à lire":
            r["ecart_fort"] = bool(r["p_holm"] <= SEUIL_GARDE)
            if r["ecart_fort"]:
                signe = r.get("T", r.get("ecart_moyen_centre", 0.0))
                ecarts_forts.append({"groupe": t["groupe"], "objet": t["objet"], "sens": "plus" if signe > 0 else "moins"})

    # descriptif : part de sa propre lignée et de sa propre famille dans les veto tels que déposés
    non_retenues = [c["id"] for c in cartes if not c["dans_le_nombre_vise"]]
    veto_desc = {}
    for t, depose in assemblage["veto"]["depose"].items():
        lt = assemblage["veto"]["lignees_des_titulaires"][t]
        connus = [i for i in depose if i in especes]
        veto_desc[t] = {
            "deposees": len(depose), "sans_espece": len(depose) - len(connus),
            "de_sa_lignee": sum(1 for i in connus if especes[i] == lt),
            "de_sa_famille": sum(1 for i in connus if familles.get(especes[i]) == familles.get(lt)),
            "base_lignee_parmi_non_retenues": [sum(1 for i in non_retenues if especes[i] == lt), len(non_retenues)],
            "base_famille_parmi_non_retenues": [sum(1 for i in non_retenues if familles[especes[i]] == familles.get(lt)),
                                                len(non_retenues)]}

    # descriptif : par espèce, sans test
    par_espece = {}
    for g in sorted(set(lignee)):
        sel = [c for c, x in zip(cartes, lignee) if x == g]
        par_espece[g] = {
            "cartes_notees": len(sel),
            "note_fine_moyenne": float(np.mean([c["note"] for c in sel])),
            "dans_le_nombre_vise": sum(1 for c in sel if c["dans_le_nombre_vise"]),
            "entrees_par_veto": sum(1 for c in sel if c["entree_par_veto"]),
            "sous_le_plancher": sum(1 for c in sel if not c["au_plancher"]),
            "part_indecidable": float(np.mean([
                sum(1 for it in ITEMS for l in (lf, lo) if l["cartes"][c["id"]]["items"][it] == "indecidable") / (2 * len(ITEMS))
                for c in sel]))}
    reconnaissance = None
    if assemblage["parametres"]["lignee_reconnue_declaree"]:
        reconnaissance = {}
        for nom, l in (("F", lf), ("O", lo)):
            lt = lignees_lecteurs[nom]
            rec = [familles.get(l["cartes"][i]["lignee_reconnue"]) == familles[lt] for i in ids]
            vraie = [familles[especes[i]] == familles[lt] for i in ids]
            own = [valeur_note_lecteur(l["cartes"][i], regime, assemblage["tenue"]["items_gardes"]) for i in ids]

            def moy(m):
                x = [o for o, k in zip(own, m) if k]
                return [len(x), float(np.mean(x)) if x else None]
            reconnaissance[nom] = {
                "croit_reconnaitre_sa_famille": moy(rec), "ne_croit_pas": moy([not x for x in rec]),
                "vraiment_de_sa_famille": moy(vraie), "vraiment_d_une_autre": moy([not x for x in vraie]),
                "reconnaissance_juste": sum(1 for a, b in zip(rec, vraie) if a == b)}
    declenche = bool(items_nommes or ecarts_forts)
    en_tete = [PRINCIPE, LIMITE_FAMILLE,
               "Ces gardes ne mesurent aucun biais : elles n'ont aucune référence de qualité extérieure aux "
               "lecteurs. Un déclenchement appelle l'audit de la règle R4, dans un sens comme dans l'autre, "
               "et le retour à Lazar avant adoption ; il ne corrige aucune liste."]
    if temoin_masque is None:
        baisse_d = None
        en_tete.append("Baisse de D sous le masque : NON RAPPORTÉE (les deux sorties du lecteur par programme "
                       "n'ont pas été passées). Un écart par famille qui baisse sous le masque ne se lit pas "
                       "comme une préférence retirée.")
    else:
        baisse_d = baisse_de_d_sous_le_masque(ids, lignee, familles, fam_lecteurs_nom,
                                              temoin_non_masque, temoin_masque)
    return {
        "piece": VERSION + ":gardes", "permutations": n_perm, "seuil": SEUIL_GARDE, "minimum": MINIMUM_GARDE,
        "correction": "Holm, par garde et par niveau ; un test sans objet par construction est hors de la correction",
        "en_tete": en_tete,
        "garde_1_items": tests_items, "items_nommes": items_nommes,
        "garde_2_ecarts": tests_ecarts, "ecarts_forts": ecarts_forts,
        "garde_2_sans_objet_par_construction": sorted(g for g, v in sans_objet.items() if v),
        "baisse_de_D_sous_le_masque": baisse_d,
        "retour_a_lazar_avant_adoption": declenche,
        "veto_par_titulaire_tel_que_depose": veto_desc, "par_espece_descriptif": par_espece,
        "note_selon_la_lignee_reconnue": reconnaissance,
    }


def valeur_note_lecteur(carte, regime, gardes):
    return sum(valeur(carte["items"][i], regime) for i in items_de_voie(carte["voie"]) if i in gardes)


# ----------------------------------------------------------------------------- tiers de l'ordre

def tiers_coeur(ordre, voie_de, sous_strate_de, especes, graine_entropie, n_perm=N_PERMUTATIONS):
    """Part de chaque voie, sous-strate et espèce dans chaque tiers d'un ordre de passage."""
    if not isinstance(ordre, list) or not ordre or not all(_texte(x) for x in ordre):
        raise Refus("ordre de passage : liste non vide d'identifiants de cartes porteuses")
    if len(set(ordre)) != len(ordre):
        raise Refus("ordre de passage : une porteuse y figure deux fois")
    n = len(ordre)
    tiers_de = [min(2, (3 * i) // n) for i in range(n)]
    axes = {"voie": voie_de, "sous_strate": sous_strate_de}
    if especes is not None:
        axes["espece"] = especes
    racine = np.random.SeedSequence(graine_entropie)
    enfants = iter(racine.spawn(1024))
    sortie, tests = {}, []
    rangs = np.arange(n, dtype=float)
    for nom_axe, table in axes.items():
        manquants = [c for c in ordre if c not in table]
        if manquants:
            raise Refus(f"ordre de passage : {len(manquants)} porteuse(s) sans {nom_axe} connue — refus, rien n'est deviné")
        modalites = sorted({str(table[c]) for c in ordre})
        sortie[nom_axe] = {}
        for mod in modalites:
            masque = np.array([str(table[c]) == mod for c in ordre])
            sortie[nom_axe][mod] = {"lignes": int(masque.sum()),
                                    "par_tiers": [int(sum(1 for i in range(n) if masque[i] and tiers_de[i] == t)) for t in range(3)]}
            if int(masque.sum()) < MINIMUM_GARDE or int(masque.sum()) == n:
                res = {"lecture": "non concluant", "motif": "moins de trois lignes, ou toutes"}
            else:
                gen = np.random.Generator(np.random.PCG64(next(enfants)))
                t_obs = float(rangs[masque].mean() - rangs.mean())
                plus = 0
                for _ in range(n_perm):
                    mp = gen.permuted(masque)
                    if abs(float(rangs[mp].mean() - rangs.mean())) >= abs(t_obs) - TOL:
                        plus += 1
                res = {"lecture": "à lire", "ecart_de_rang_moyen": t_obs, "p": (1 + plus) / (n_perm + 1)}
            tests.append({"axe": nom_axe, "modalite": mod, "resultat": res})
    _lire_avec_holm(tests)
    forts = []
    for t in tests:
        r = t["resultat"]
        if r["lecture"] == "à lire":
            r["ecart_fort"] = bool(r["p_holm"] <= SEUIL_GARDE)
            if r["ecart_fort"]:
                forts.append({"axe": t["axe"], "modalite": t["modalite"],
                              "sens": "passe plus tard" if r["ecart_de_rang_moyen"] > 0 else "passe plus tôt"})
    return {"piece": VERSION + ":tiers", "lignes": n, "parts": sortie, "tests": tests, "ecarts_forts": forts,
            "retour_a_lazar": bool(forts), "en_tete": [PRINCIPE]}


# ----------------------------------------------------------------------------- écriture, commandes

def ecrire_neuf(chemin, objet):
    compagnon = chemin + ".sha256"
    if os.path.exists(chemin) or os.path.exists(compagnon):
        raise Refus(f"sortie déjà présente ({chemin}) : on n'écrase jamais (règle R12)")
    octets = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    with open(compagnon, "x", encoding="utf-8") as f:
        f.write(f"{sha_octets(octets)}  {os.path.basename(chemin)}\n")
    return sha_octets(octets)


def _charger_especes(chemin, sha):
    e = lire_json_verifie(chemin, sha, "table des espèces")
    if not isinstance(e, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in e.items()):
        raise Refus("table des espèces : objet {identifiant: lignée} attendu")
    return e


def _charger_temoin(chemin, sha, role, forme):
    """Sortie du lecteur par programme, pour la commande `gardes` (C4). La forme lue est contrôlée :
    deux sorties échangées inverseraient le sens de la baisse."""
    t = lire_json_verifie(chemin, sha, role)
    if not isinstance(t, dict) or not isinstance(t.get("cartes"), list):
        raise Refus(f"{role} : clé « cartes » attendue")
    if t.get("forme_lue") != forme:
        raise Refus(f"{role} : forme lue {t.get('forme_lue')!r}, « {forme} » attendue")
    temoin = {}
    for c in t["cartes"]:
        if not isinstance(c, dict) or not {"id", "voie", "D"} <= set(c):
            raise Refus(f"{role} : enregistrement sans id, voie ou D")
        if c["id"] in temoin:
            raise Refus(f"{role} : carte en double")
        temoin[c["id"]] = c
    return temoin


def _charger_lectures(args, m):
    lf = valider_lecture(lire_json_verifie(args.lecture_f[0], args.lecture_f[1], "lecture F"), "F", m)
    lo = valider_lecture(lire_json_verifie(args.lecture_o[0], args.lecture_o[1], "lecture O"), "O", m)
    return lf, lo


def _h1(args, m):
    if not os.path.isfile(args.criteres):
        raise Refus("critères scellés : fichier absent")
    h1 = sha_fichier(args.criteres)
    if h1 != str(m["criteres_sha256"]).lower():
        raise Refus("critères scellés : empreinte différente de celle du manifeste d'ouverture")
    return h1


def commande_assembler(args):
    verifier_numpy()
    if os.path.exists(args.sortie) or os.path.exists(args.sortie + ".sha256"):
        raise Refus("sortie déjà présente : on n'écrase jamais (règle R12)")
    m = valider_manifeste(lire_json_verifie(args.manifeste[0], args.manifeste[1], "manifeste d'ouverture"))
    h1 = _h1(args, m)
    lf, lo = _charger_lectures(args, m)
    especes = _charger_especes(*args.especes) if args.especes else None
    juges = []
    for chemin, sha in (args.veto_juge or []):
        j = lire_json_verifie(chemin, sha, "liste de veto d'un juge")
        if not isinstance(j, dict) or set(j) != {"titulaire", "lignee", "veto"} or not _texte(j["titulaire"]):
            raise Refus("liste de veto d'un juge : clés titulaire, lignee, veto")
        if j["lignee"] not in m["familles"]:
            raise Refus("liste de veto d'un juge : lignée absente de la table des familles")
        j["veto"] = valider_liste_veto(j["veto"], f"veto du juge {j['titulaire']}")
        juges.append(j)
    temoin = None
    if args.lecteur_programme:
        t = lire_json_verifie(args.lecteur_programme[0], args.lecteur_programme[1], "lecteur par programme")
        if not isinstance(t, dict) or not isinstance(t.get("cartes"), list):
            raise Refus("lecteur par programme : clé « cartes » attendue")
        temoin = {}
        for c in t["cartes"]:
            if not isinstance(c, dict) or not {"id", "voie", "D"} <= set(c):
                raise Refus("lecteur par programme : enregistrement sans id, voie ou D")
            temoin[c["id"]] = c
    sortie = assembler_coeur(lf, lo, m, h1, especes, juges, temoin)
    sortie["empreintes"] = {"programme": sha_fichier(os.path.abspath(__file__)), "criteres": h1,
                            "manifeste": args.manifeste[1].lower(), "lecture_F": args.lecture_f[1].lower(),
                            "lecture_O": args.lecture_o[1].lower(),
                            "especes": args.especes[1].lower() if args.especes else None}
    sha = ecrire_neuf(args.sortie, sortie)
    for ligne in sortie["en_tete"]:
        print(ligne)
    print(f"assemblage écrit : {args.sortie} ({sha})")


def commande_gardes(args):
    verifier_numpy()
    if os.path.exists(args.sortie) or os.path.exists(args.sortie + ".sha256"):
        raise Refus("sortie déjà présente : on n'écrase jamais (règle R12)")
    m = valider_manifeste(lire_json_verifie(args.manifeste[0], args.manifeste[1], "manifeste d'ouverture"))
    h1 = _h1(args, m)
    lf, lo = _charger_lectures(args, m)
    a = lire_json_verifie(args.assemblage[0], args.assemblage[1], "assemblage")
    if a.get("piece") != VERSION:
        raise Refus("assemblage : pièce d'une autre version")
    especes = _charger_especes(*args.especes)
    nm, ms = args.lecteur_programme_non_masque, args.lecteur_programme_masque
    if (nm is None) != (ms is None):
        raise Refus("gardes : --lecteur-programme-non-masque et --lecteur-programme-masque vont ensemble, ou aucun")
    t_nm = _charger_temoin(nm[0], nm[1], "lecteur par programme, cartes non masquées", "fiches") if nm else None
    t_ms = _charger_temoin(ms[0], ms[1], "lecteur par programme, cartes masquées", "masque") if ms else None
    sortie = gardes_coeur(a, lf, lo, especes, m["familles"], {"F": lf["lignee"], "O": lo["lignee"]}, h1,
                          temoin_non_masque=t_nm, temoin_masque=t_ms)
    sortie["empreintes"] = {"programme": sha_fichier(os.path.abspath(__file__)), "assemblage": args.assemblage[1].lower(),
                            "especes": args.especes[1].lower(),
                            "lecteur_programme_non_masque": nm[1].lower() if nm else None,
                            "lecteur_programme_masque": ms[1].lower() if ms else None}
    sha = ecrire_neuf(args.sortie, sortie)
    if sortie["baisse_de_D_sous_le_masque"] is None:
        print(sortie["en_tete"][-1])
    print("retour à Lazar avant adoption :", "oui" if sortie["retour_a_lazar_avant_adoption"] else "non déclenché")
    print(f"gardes écrites : {args.sortie} ({sha})")


def commande_tiers(args):
    verifier_numpy()
    if os.path.exists(args.sortie) or os.path.exists(args.sortie + ".sha256"):
        raise Refus("sortie déjà présente : on n'écrase jamais (règle R12)")
    o = lire_json_verifie(args.ordre[0], args.ordre[1], "ordre de passage")
    if not isinstance(o, dict) or set(o) != {"ordre", "voie", "sous_strate"}:
        raise Refus("ordre de passage : clés ordre, voie, sous_strate")
    especes = _charger_especes(*args.especes) if args.especes else None
    entropie = [int(args.ordre[1], 16), int(sha_octets(b"tiers-de-l-ordre-v4-v1"), 16)]
    sortie = tiers_coeur(o["ordre"], o["voie"], o["sous_strate"], especes, entropie)
    sortie["empreintes"] = {"programme": sha_fichier(os.path.abspath(__file__)), "ordre": args.ordre[1].lower()}
    sha = ecrire_neuf(args.sortie, sortie)
    print("écart fort à l'ordre de passage :", "oui" if sortie["retour_a_lazar"] else "non")
    print(f"tiers écrits : {args.sortie} ({sha})")


def analyseur():
    p = argparse.ArgumentParser(description="Assemblage selon les critères de choix v4 (v2). Propose, ne tranche rien.")
    s = p.add_subparsers(dest="commande", required=True)
    paire = dict(nargs=2, metavar=("CHEMIN", "SHA256"))
    a = s.add_parser("assembler")
    a.add_argument("--manifeste", required=True, **paire)
    a.add_argument("--criteres", required=True)
    a.add_argument("--lecture-f", required=True, **paire)
    a.add_argument("--lecture-o", required=True, **paire)
    a.add_argument("--especes", **paire)
    a.add_argument("--veto-juge", action="append", **paire)
    a.add_argument("--lecteur-programme", **paire)
    a.add_argument("--sortie", required=True)
    a.set_defaults(f=commande_assembler)
    g = s.add_parser("gardes")
    g.add_argument("--manifeste", required=True, **paire)
    g.add_argument("--criteres", required=True)
    g.add_argument("--lecture-f", required=True, **paire)
    g.add_argument("--lecture-o", required=True, **paire)
    g.add_argument("--assemblage", required=True, **paire)
    g.add_argument("--especes", required=True, **paire)
    g.add_argument("--lecteur-programme-non-masque", **paire)
    g.add_argument("--lecteur-programme-masque", **paire)
    g.add_argument("--sortie", required=True)
    g.set_defaults(f=commande_gardes)
    t = s.add_parser("tiers")
    t.add_argument("--ordre", required=True, **paire)
    t.add_argument("--especes", **paire)
    t.add_argument("--sortie", required=True)
    t.set_defaults(f=commande_tiers)
    return p


def main(argv=None):
    args = analyseur().parse_args(argv)
    try:
        args.f(args)
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
