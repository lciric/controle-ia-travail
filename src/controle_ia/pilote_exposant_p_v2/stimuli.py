"""Stimuli v2 du pilote : règles R-S1 à R-S10, garde des classes lexicales et du modèle stylisé, paires, jumeau neutre.

Ce qui change depuis la v1 (contre-lecture R2, bloquant B1) :
- paires de E minimales : FE et FD (et CE et CD) ne diffèrent que par le dernier mot, qui porte le statut ;
- le porteur est le même dans les deux registres d'un quadruplet : le registre n'est porté que par le corps ;
- 30 porteurs d'évaluation distincts, 30 porteurs de déploiement distincts, hors des classes lexicales contrôlées
  (mots de date, première et deuxième personne, minimisation) ; ces classes ont le même compte côté E et côté D ;
- garde du modèle stylisé : une phrase y vaut le plongement gaussien aléatoire de son dernier mot plus w fois la moyenne
  des plongements de ses autres mots ; E et R y sont calculés comme dans le pilote ; médiane de |cos(E, R)| < 0,03 ;
- jumeau neutre N (emprunt à l'addendum R9-bis, <<DOI_R9_BIS>>), choisi sur le tokeniseur du modèle lu.

Le sens (R-S9) n'est pas vérifiable par programme : Lazar le vérifie à la main (`verification-humaine-stimuli-v2.md`).
Signes : E = moyenne(évaluation − déploiement) ; R = moyenne(formel − familier) ; N = moyenne(neutre − déploiement).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Callable

import numpy as np

from ..gardes import GardeArret
from ..pilote_exposant_p.stimuli import hachage_liste, mots

ECART_PHRASE_R = 6
MIN_PAIRES = 30
MIN_QUADRUPLETS_JUMEAU = 15
FENETRE_CLASSES = 4                 # R-S8 : classes comptées aussi dans les quatre derniers mots
SEUIL_STYLISE = 0.03                # R-S8 : médiane de |cos(E, R)| sous le modèle stylisé
W_STYLISE = (0.0, 0.3, 1.0)
TIRAGES_STYLISE = 300
DIM_STYLISE = 4096                 # dimension du résidu de Llama-3.1-8B
ENTROPIE_STYLISE = 2026110401
CLASSES_PERSONNE = ("premiere_personne", "deuxieme_personne")


def charger(chemin: str | Path) -> dict:
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def _a_racine(m: str, racines: list[str]) -> bool:
    return any(m.startswith(r) for r in racines)


def compte_classe(phrase_mots: list[str], liste: list[str]) -> int:
    s = set(liste)
    return sum(1 for m in phrase_mots if m in s)


def problemes_stimuli(stim: dict, hachages_publies: dict | None = None) -> list[str]:
    """Écarts aux règles R-S1 à R-S8 et à la structure de R-S10 (vide si conforme)."""
    pb: list[str] = []
    mk = stim["marqueurs"]
    racines = mk["racines_evaluation"]
    familiers = set(mk["contractions"]) | set(mk["marqueurs_familiers"])
    classes = mk["classes_controlees"]
    quads = stim["quadruplets"]
    vues: set[str] = set()
    pe = [q["porteur_E"] for q in quads]
    pd = [q["porteur_D"] for q in quads]
    if len(set(pe)) != len(pe):
        pb.append("porteurs d'évaluation non distincts (R-S4)")
    if len(set(pd)) != len(pd):
        pb.append("porteurs de déploiement non distincts (R-S4)")
    if set(x.lower() for x in pe) & set(x.lower() for x in pd):
        pb.append("un même mot porte les deux statuts (R-S4)")
    tous_porteurs_d = {x.lower() for x in pd}
    tous_porteurs_e = {x.lower() for x in pe}
    for q in quads:
        i = q["id"]
        e, d = q["porteur_E"], q["porteur_D"]
        for p, nom in ((e, "E"), (d, "D")):
            if len(p.split()) != 1:
                pb.append(f"{i} porteur {nom} « {p} » : un seul mot attendu (R-S4)")
            mp = mots(p)
            if not mp or mp[0] in familiers or "'" in p:
                pb.append(f"{i} porteur {nom} « {p} » : marqueur familier ou contraction (R-S4)")
            for cl, liste in classes.items():
                if compte_classe(mp, liste):
                    pb.append(f"{i} porteur {nom} « {p} » : dans la classe contrôlée {cl} (R-S4)")
        if not _a_racine(e.lower(), racines):
            pb.append(f"{i} porteur E « {e} » : aucune racine d'évaluation (R-S4)")
        if _a_racine(d.lower(), racines):
            pb.append(f"{i} porteur D « {d} » : racine d'évaluation (R-S4)")
        for corps_cle in ("corps_F", "corps_C"):
            mc = mots(q[corps_cle])
            if any(_a_racine(m, racines) for m in mc):
                pb.append(f"{i} {corps_cle} : racine d'évaluation dans le corps (R-S4)")
            if set(mc) & (tous_porteurs_d | tous_porteurs_e):
                pb.append(f"{i} {corps_cle} : un porteur figure dans le corps (R-S4)")
            if not any(m.startswith(q["contenu"].lower()) for m in mc):
                pb.append(f"{i} {corps_cle} : contenu « {q['contenu']} » absent (R-S1)")
        for cle, corps, porteur in (("FE", "corps_F", e), ("FD", "corps_F", d), ("CE", "corps_C", e), ("CD", "corps_C", d)):
            if q[cle] != f"{q[corps]} {porteur}":
                pb.append(f"{i} {cle} : la phrase n'est pas « corps porteur » (R-S1, R-S2, R-S8)")
            if q[cle].rstrip()[-1:] in ".!?;:,":
                pb.append(f"{i} {cle} : ponctuation finale (R-S6)")
            if q[cle] in vues:
                pb.append(f"{i} {cle} : phrase en double (R-S6)")
            vues.add(q[cle])
        # R-S2 : paires minimales (un seul mot change, le dernier)
        for a, b in (("FE", "FD"), ("CE", "CD")):
            ma, mb = q[a].split(), q[b].split()
            diff = [k for k in range(max(len(ma), len(mb))) if k >= len(ma) or k >= len(mb) or ma[k] != mb[k]]
            if len(ma) != len(mb) or diff != [len(ma) - 1]:
                pb.append(f"{i} {a}/{b} : la paire ne diffère pas par le seul dernier mot (R-S2)")
        # R-S3 : longueur et personne grammaticale entre registres
        mF, mC = mots(q["corps_F"]), mots(q["corps_C"])
        if abs(len(mF) - len(mC)) > ECART_PHRASE_R:
            pb.append(f"{i} corps F/C : écart de longueur > {ECART_PHRASE_R} mots (R-S3)")
        for cl in CLASSES_PERSONNE:
            if compte_classe(mF, classes[cl]) != compte_classe(mC, classes[cl]):
                pb.append(f"{i} corps F/C : compte de {cl} différent (R-S3)")
        # R-S5 : registres
        if "'" in q["corps_F"] or "’" in q["corps_F"] or set(mF) & familiers:
            pb.append(f"{i} corps F : apostrophe, contraction ou marqueur familier en registre formel (R-S5)")
        if not set(mC) & familiers:
            pb.append(f"{i} corps C : aucun marqueur familier en registre familier (R-S5)")
        # R-S7
        attendu = "A" if int(i[1:]) <= len(quads) // 2 else "B"
        if q["moitie"] != attendu:
            pb.append(f"{i} : moitié {q['moitie']} au lieu de {attendu} (R-S7)")
        # R-S8 : classes lexicales, côté E contre côté D, par registre, phrase entière et quatre derniers mots
        for xe, xd in (("FE", "FD"), ("CE", "CD")):
            me, md = mots(q[xe]), mots(q[xd])
            for cl, liste in classes.items():
                for fen, ae, ad in (("phrase", me, md), ("fin", me[-FENETRE_CLASSES:], md[-FENETRE_CLASSES:])):
                    if compte_classe(ae, liste) != compte_classe(ad, liste):
                        pb.append(f"{i} {xe}/{xd} : classe {cl} déséquilibrée ({fen}) (R-S8)")
        # R-S10 : candidats neutres
        nc = q.get("neutres_candidats") or []
        if not nc:
            pb.append(f"{i} : aucun candidat neutre (R-S10)")
        for n in nc:
            mn = mots(n)
            if len(n.split()) != 1 or _a_racine(n.lower(), racines) or n.lower() in tous_porteurs_d \
                    or any(compte_classe(mn, l) for l in classes.values()):
                pb.append(f"{i} candidat neutre « {n} » non conforme (R-S10)")
    if 2 * len(quads) < MIN_PAIRES:
        pb.append(f"{2 * len(quads)} paires par direction < {MIN_PAIRES}")
    for nom, d in stim["papier"]["directions"].items():
        if len(d["a"]) != len(d["b"]) or len(d["a"]) < MIN_PAIRES:
            pb.append(f"papier {nom} : {len(d['a'])}/{len(d['b'])} invites (au moins {MIN_PAIRES} paires appariées)")
        if hachages_publies and nom in hachages_publies:
            m = min(len(d["a"]), len(d["b"]))
            if hachage_liste(d["a"][:m]) != hachages_publies[nom]["a_sha"] or hachage_liste(d["b"][:m]) != hachages_publies[nom]["b_sha"]:
                pb.append(f"papier {nom} : invites différentes de celles qui ont produit les directions publiées")
    return pb


# --- modèle stylisé (contre-lecture R2, B1) -------------------------------------------------------------------------

def _vecteur(phrase: str, emb: dict[str, np.ndarray], w: float) -> np.ndarray:
    m = phrase.split()
    v = emb[m[-1]].copy()
    if w and len(m) > 1:
        v = v + w * np.mean([emb[x] for x in m[:-1]], axis=0)
    return v


def cos_stylise(quads: list[dict], w: float, rng: np.random.Generator, dim: int = DIM_STYLISE) -> float:
    """Un tirage : plongements gaussiens indépendants de chaque mot (séparation aux espaces) ; E = moyenne(évaluation −
    déploiement), R = moyenne(formel − familier), comme dans le pilote. R nul (dernier mot partagé, w = 0) : cos = 0."""
    vocab = sorted({x for q in quads for k in ("FE", "FD", "CE", "CD") for x in q[k].split()})
    emb = {x: rng.standard_normal(dim) for x in vocab}
    v = {k: np.stack([_vecteur(q[k], emb, w) for q in quads]) for k in ("FE", "FD", "CE", "CD")}
    E = np.concatenate([v["FE"] - v["FD"], v["CE"] - v["CD"]]).mean(axis=0)
    R = np.concatenate([v["FE"] - v["CE"], v["FD"] - v["CD"]]).mean(axis=0)
    nE, nR = np.linalg.norm(E), np.linalg.norm(R)
    if nE < 1e-12:
        raise ValueError("E nul sous le modèle stylisé : porteurs identiques")
    if nR < 1e-9 * max(nE, 1.0):
        return 0.0
    return float(E @ R / (nE * nR))


def modele_stylise(quads: list[dict], ws=W_STYLISE, tirages: int = TIRAGES_STYLISE,
                   entropie: int = ENTROPIE_STYLISE, dim: int = DIM_STYLISE) -> dict:
    """Médiane de |cos(E, R)| et part des tirages avec |cos| ≥ 0,1, pour chaque w (graines par SeedSequence, R9)."""
    sortie = {}
    for w, ss in zip(ws, np.random.SeedSequence(entropie).spawn(len(ws))):
        rng = np.random.default_rng(ss)
        c = np.array([cos_stylise(quads, w, rng, dim) for _ in range(tirages)])
        sortie[f"{w:g}"] = {"mediane_abs_cos": float(np.median(np.abs(c))), "mediane_cos": float(np.median(c)),
                            "part_abs_cos_au_moins_0_1": float(np.mean(np.abs(c) >= 0.1))}
    return sortie


def exiger_modele_stylise(quads: list[dict], seuil: float = SEUIL_STYLISE, **kw) -> dict:
    r = modele_stylise(quads, **kw)
    mauvais = {w: x["mediane_abs_cos"] for w, x in r.items() if not x["mediane_abs_cos"] < seuil}
    if mauvais:
        raise GardeArret(f"modèle stylisé : médiane de |cos(E, R)| ≥ {seuil} pour w = {mauvais} (R-S8) : la structure "
                         "des fins suffit à rapprocher E et R")
    return r


def exiger_stimuli_conformes(chemin: str | Path, hachages_publies: dict | None = None, stylise: bool = True) -> dict:
    stim = charger(chemin)
    pb = problemes_stimuli(stim, hachages_publies)
    if pb:
        raise GardeArret(f"{chemin} non conforme à ses règles de construction : " + " ; ".join(pb[:10]))
    if stylise:
        stim["_modele_stylise"] = exiger_modele_stylise(stim["quadruplets"])
    return stim


# --- jumeau neutre (R-S10) ------------------------------------------------------------------------------------------

def choisir_neutres(stim: dict, compter: Callable[[str], int]) -> dict:
    """`compter(phrase)` : nombre de jetons du tokeniseur du modèle lu (BOS compris). Pour chaque quadruplet, premier
    candidat qui donne, dans les deux registres, autant de jetons que le porteur d'évaluation."""
    choix, detail = {}, []
    for q in stim["quadruplets"]:
        nE = (compter(q["FE"]), compter(q["CE"]))
        retenu = None
        essais = []
        for n in q["neutres_candidats"]:
            nN = (compter(f"{q['corps_F']} {n}"), compter(f"{q['corps_C']} {n}"))
            essais.append({"candidat": n, "jetons": list(nN)})
            if nN == nE:
                retenu = n
                break
        choix[q["id"]] = retenu
        detail.append({"id": q["id"], "jetons_E": list(nE), "essais": essais, "retenu": retenu})
    n_ok = sum(1 for v in choix.values() if v)
    return {"choix": choix, "detail": detail, "quadruplets_retenus": n_ok,
            "construit": n_ok >= MIN_QUADRUPLETS_JUMEAU, "minimum": MIN_QUADRUPLETS_JUMEAU}


def paires(stim: dict, direction: str, moitie: str | None = None, neutres: dict | None = None) -> tuple[list[str], list[str]]:
    """Rend (côté a, côté b) ; la direction est moyenne(b − a).
    E : a = déploiement, b = évaluation ; R : a = familier, b = formel ; N : a = déploiement, b = neutre (quadruplets
    retenus par `choisir_neutres`) ; E_naif : a = CD, b = FE ; E_naif_inverse : a = FD, b = CE ; E_echelle : cadrages
    de l'échelle v2 ; directions du papier : b − a. Les sous-ensembles « fe_fd », « ce_cd », « fe_ce », « fd_cd »
    servent aux descriptifs de l'interaction (contre-lecture R2, I8)."""
    quads = [q for q in stim["quadruplets"] if moitie is None or q["moitie"] == moitie]
    if direction == "E":
        return [q["FD"] for q in quads] + [q["CD"] for q in quads], [q["FE"] for q in quads] + [q["CE"] for q in quads]
    if direction == "R":
        return [q["CE"] for q in quads] + [q["CD"] for q in quads], [q["FE"] for q in quads] + [q["FD"] for q in quads]
    if direction == "N":
        if neutres is None:
            raise ValueError("jumeau neutre : choix des neutres absent")
        qs = [q for q in quads if neutres.get(q["id"])]
        return ([q["FD"] for q in qs] + [q["CD"] for q in qs],
                [f"{q['corps_F']} {neutres[q['id']]}" for q in qs] + [f"{q['corps_C']} {neutres[q['id']]}" for q in qs])
    simples = {"E_naif": ("CD", "FE"), "E_naif_inverse": ("FD", "CE"), "fe_fd": ("FD", "FE"), "ce_cd": ("CD", "CE"),
               "fe_ce": ("CE", "FE"), "fd_cd": ("CD", "FD")}
    if direction in simples:
        a, b = simples[direction]
        return [q[a] for q in quads], [q[b] for q in quads]
    if direction == "E_echelle":
        c = stim["echelle_v2_cadrages"]["paires"]
        return [p[1] for p in c], [p[0] for p in c]
    if direction in stim["papier"]["directions"]:
        d = stim["papier"]["directions"][direction]
        m = min(len(d["a"]), len(d["b"]))
        if moitie in ("A", "B"):
            h = m // 2
            sl = slice(0, h) if moitie == "A" else slice(h, m)
            return d["a"][:m][sl], d["b"][:m][sl]
        return d["a"][:m], d["b"][:m]
    raise KeyError(direction)


def empreinte_canonique(stim: dict) -> str:
    s = {k: v for k, v in stim.items() if not k.startswith("_")}
    return hashlib.sha256(json.dumps(s, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
