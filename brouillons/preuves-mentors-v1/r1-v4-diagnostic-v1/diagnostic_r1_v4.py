#!/usr/bin/env python3
"""Diagnostic R1 v4 — sur processeur, sans réseau, sans modèle, sans aucun score de sonde ni de juge.

But : fonder l'addendum v4 et la table v4 de R1 (réparer la donnée, pas la règle) par un relevé exact des pertes de la
relance v3 (run `20261103-063222-r1-rejeu-reel`) : les 89 épisodes cassés, les 164 actions non conformes en longueur,
ce que P3 a gardé et qui peut servir d'oracle, la forme des lots de P3.

Lancement (rejouable, lecture seule) :
    nice -n 10 /home/claude/controle-ia-travail/.venv/bin/python3 -I -B diagnostic_r1_v4.py > diagnostic-r1-v4-sortie.txt
(l'interpréteur du venv du dépôt porte numpy 2.4.6, la version de P3 : elle sert à redériver les graines.)

Ce qui est ouvert, et seulement cela (chaque fichier vérifié par son empreinte sha256 avant lecture) :
- `activations-p3-rejeu-v1.npz` du rejeu : clés `episode`, `pas`, `condition`, `tache`, `jetons_empan`,
  `jetons_empan_rejeu`, `couches`, `conforme_longueur`, `contexte_conforme`, `ecart_fidelite`, `fidele`,
  `trajectoire_identique`, `activations_identiques`, une par une (accès par clé, `allow_pickle=False`) ; **jamais**
  `moyenne` (le répertoire du zip est lu pour lister les clés, aucun autre membre n'est décompressé) ;
- `rejeu-activations.json` du rejeu (comptes) ;
- P3 : `textes-actions-p3.jsonl`, `episodes-p3.json` (champs `episode`, `condition`, `tache`, `jetons_par_action`,
  `empreintes`, et de `equivalence` les seuls `actions`, `lignes`, `longueurs_contexte`, `positions_capturees`,
  `empreintes_capture` ; jamais `ecarts`, `ecarts_q99`, `profils`, `controle_negatif_zone_generee`, `sondes`), `resume.json`
  (comptes), `manifeste.json` (graines, configuration) ;
- `jetons-principales-p3.npz` : clés `rang`, `debut`, `longueur`, `bornes`, `bornes_lisibles` (dérivées des seuls
  jetons générés : `premier_test_ia.run.tableaux_par_jeton`, `conditions.bornes_champs`) ; **jamais** `scores_0`,
  `scores_1` (scores par jeton des sondes principales), `logits_0`, `logits_1` (logits d'attention de ces sondes, pas du
  modèle générateur), ni `principales`, `champs` ;
- la table v3 au commit 139a81d3 (`git show`).
`ecart_fidelite` (écart relatif des sondes légères de fidélité, clé permise) ne sert qu'à vérifier la définition de
`fidele` et le vide de la bande de tolérance ; aucune activation, aucun score de détection n'est lu.
"""
from __future__ import annotations

import collections
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path

import numpy as np

DEPOT = Path("/home/claude/controle-ia-travail")
ANALYSE = Path("/home/claude/controle-ia-analyse-principale-r1-r2-v1")
RUN_REJEU = "20261103-063222-r1-rejeu-reel"
RUN_P3 = "20261019-230011-p3-reel"
NPZ_REJEU = ANALYSE / "donnees" / RUN_REJEU / "activations-p3-rejeu-v1.npz"
JSON_REJEU = ANALYSE / "diag" / RUN_REJEU / "rejeu-activations.json"
TEXTES = DEPOT / "donnees" / RUN_P3 / "textes-actions-p3.jsonl"
FICHES = DEPOT / "diag" / RUN_P3 / "episodes-p3.json"
RESUME = DEPOT / "diag" / RUN_P3 / "resume.json"
MANIFESTE = DEPOT / "runs" / RUN_P3 / "manifeste.json"
JETONS_PRINC = DEPOT / "donnees" / RUN_P3 / "jetons-principales-p3.npz"
COMMIT = "139a81d37fbd2255aff8d27698f84b47b9433221"
CHEMIN_TABLE_V3 = "prereg/R1-table-tokenisation-v3.json"

ATTENDUES = {
    NPZ_REJEU: "6273bf85344e9300943adf1b3a3ae208476748ca2643102501ac4111c5b26476",
    JSON_REJEU: "738e861a3ce56c1599e2067fa72a8858e61c4857e63b5dfc52e40e21c4ce1bd6",
    TEXTES: "ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284",
    FICHES: "1a96cbf8ac6e10d3315bb20248453836d6ae5570b2312ded2be5ebb67cd14381",
    RESUME: "4d6894b309ca138541fec29d07e8541a707c8266295e0dcd2019f9e646d628f6",
    MANIFESTE: "3f21774ca2a740e059191e762a4922076d954ee4c3e728c9927ba436cb211685",
    JETONS_PRINC: "4cd2ddb8311cfa7322d4137514c057c33039aba115aa14f08fb64141a2b0a36f",
}
TABLE_V3_SHA = "ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423"
CLES_NPZ_PERMISES = ("episode", "pas", "condition", "tache", "jetons_empan", "jetons_empan_rejeu", "couches",
                     "conforme_longueur", "contexte_conforme", "ecart_fidelite", "fidele", "trajectoire_identique",
                     "activations_identiques")
CLES_JETONS_PERMISES = ("rang", "debut", "longueur", "bornes", "bornes_lisibles")
CLES_EQUIVALENCE_PERMISES = ("actions", "lignes", "longueurs_contexte", "positions_capturees", "empreintes_capture")
CONDITIONS = ("honnete", "saboteur", "temoin", "mention")
CONDITIONS_REGLE = ("honnete", "saboteur")
CHAMPS_BORNES = ("TITLE", "PROPOSAL", "CONTROLS", "COST", "PREDICTION")      # premier_test_ia.conditions
T = 10
SEUIL_COUVERTURE = 0.80
MAX_NOUVEAUX = 400


class Arret(Exception):
    pass


def sha256(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def exiger(cond: bool, motif: str) -> None:
    if not cond:
        raise Arret(motif)


def titre(t: str) -> None:
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)


def charger_npz_cles(chemin: Path, cles: tuple[str, ...]) -> tuple[dict, list[str]]:
    """Clés permises seulement ; rend aussi la liste de toutes les clés (répertoire du zip, rien d'autre décompressé)."""
    with zipfile.ZipFile(chemin) as zf:
        toutes = [n[:-4] for n in zf.namelist() if n.endswith(".npy")]
    manquantes = [k for k in cles if k not in toutes]
    exiger(not manquantes, f"{chemin.name} : clés absentes {manquantes}")
    sortie = {}
    with np.load(chemin, allow_pickle=False) as z:
        for k in cles:
            sortie[k] = z[k]
    return sortie, toutes


def generateur(graine: dict) -> np.random.Generator:
    """Recopie de `manifeste.generateur` (P3, commit 97dd8290) : SeedSequence(entropie, spawn_key), garde par l'état
    de contrôle consigné."""
    ss = np.random.SeedSequence(int(graine["entropie"]), spawn_key=tuple(int(k) for k in graine["spawn_key"]))
    exiger([int(x) for x in ss.generate_state(2)] == graine["etat_controle"], "graine reconstruite ≠ graine consignée")
    return np.random.default_rng(ss)


def graines_et_echantillon(graine: dict, fraction: float) -> tuple[list[int], set[int]]:
    """Comme `jouer_p3` : `graines_des_actions(g, 1, T)` = g.integers(0, 2**31 − 1, size=T), puis g.random(T) <
    fraction_equivalence pour l'échantillon d'équivalence."""
    g = generateur(graine)
    valeurs = g.integers(0, 2 ** 31 - 1, size=T)
    tirages = g.random(T)
    return [int(v) for v in valeurs], {s for s in range(T) if tirages[s] < fraction}


# --- traits du texte -------------------------------------------------------------------------------------------------
RE_SPECIAL = re.compile(r"<\|[^<>|\n]{0,40}\|>")
RE_ROLE = re.compile(r"(?m)^(?:assistant|user|system)\s*$")
RE_NOMBRE4 = re.compile(r"\d{4,}")
RE_NOMBRE7 = re.compile(r"\d{7,}")
RE_MILLIERS = re.compile(r"\d{1,3}(?:[ ,  ]\d{3})+(?!\d)")
RE_PONCT = re.compile(r"([^\w\s])\1{3,}")
RE_NETTOYAGE = re.compile(r"(?<=\S) [.,!?](?=\s|$)|(?<=\S) (?:n't|'s|'m|'ve|'re)\b")
RE_CLE_BRUTE = re.compile(r"^\s*(?P<gras>[*_]{0,3})(?P<cle>ACTION|TITLE|PROPOSAL|CONTROLS|COST|PREDICTION)"
                          r"(?P<gras_avant>[*_]{0,3})\s*:", re.I | re.M)


def traits(texte: str, jetons: int, a_fin: int) -> dict[str, bool]:
    t = texte
    return {
        "U+FFFD (caractère de remplacement)": "�" in t,
        "chaîne de jeton spécial <|…|>": RE_SPECIAL.search(t) is not None,
        "fragment « <| » ou « |> »": ("<|" in t) or ("|>" in t),
        "ligne réduite à un rôle (assistant, user, system)": RE_ROLE.search(t) is not None,
        "espaces multiples (au moins 2)": "  " in t,
        "tabulation": "\t" in t,
        "retour chariot \\r": "\r" in t,
        "espace avant un retour à la ligne": " \n" in t,
        "au moins 3 retours à la ligne consécutifs": "\n\n\n" in t,
        "espace Unicode autre que U+0020": any(unicodedata.category(c) == "Zs" and c != " " for c in t),
        "caractère de format (Cf, zéro largeur…)": any(unicodedata.category(c) == "Cf" for c in t),
        "caractère de contrôle (hors \\n \\t \\r)": any(unicodedata.category(c) == "Cc" and c not in "\n\t\r"
                                                        for c in t),
        "blanc en tête ou en fin de texte": bool(t) and t != t.strip(),
        "nombre d'au moins 4 chiffres": RE_NOMBRE4.search(t) is not None,
        "nombre d'au moins 7 chiffres": RE_NOMBRE7.search(t) is not None,
        "milliers séparés (espace, virgule, insécable)": RE_MILLIERS.search(t) is not None,
        "lettre non ASCII": any(ord(c) > 127 and unicodedata.category(c).startswith("L") for c in t),
        "symbole ou ponctuation non ASCII": any(ord(c) > 127 and unicodedata.category(c)[0] in "SP" for c in t),
        "caractère hors du plan de base (> U+FFFF, émoji…)": any(ord(c) > 0xFFFF for c in t),
        "ponctuation répétée (4 identiques ou plus)": RE_PONCT.search(t) is not None,
        "texte vide": t == "",
        "action tronquée à 400 jetons (sans jeton de fin)": jetons == MAX_NOUVEAUX and a_fin == 0,
    }


TRAITS_LOURDS = ("U+FFFD (caractère de remplacement)", "chaîne de jeton spécial <|…|>", "fragment « <| » ou « |> »",
                 "ligne réduite à un rôle (assistant, user, system)", "texte vide",
                 "caractère de contrôle (hors \\n \\t \\r)", "caractère de format (Cf, zéro largeur…)")


def bornes_caracteres(texte: str) -> dict[str, int]:
    """Position en caractères du début de la clé de la première occurrence non vide de chaque champ (même règle que
    `conditions.bornes_champs`, sans tokeniseur) ; −1 si absent."""
    sortie = {c: -1 for c in CHAMPS_BORNES}
    cles = list(RE_CLE_BRUTE.finditer(texte))
    for i, m in enumerate(cles):
        cle = m["cle"].upper()
        if cle == "ACTION" or sortie[cle] != -1:
            continue
        derniere = i + 1 == len(cles)
        valeur = texte[m.end():len(texte) if derniere else cles[i + 1].start()]
        if m["gras"] and not m["gras_avant"] and derniere:
            valeur = re.sub(r"^\s*[*_]{1,3}", "", valeur, count=1)
        if not valeur.strip():
            continue
        sortie[cle] = m.start("cle")
    return sortie


def main() -> int:
    titre("0. Pièces et empreintes (vérifiées avant toute lecture)")
    for chemin, attendu in ATTENDUES.items():
        sha = sha256(chemin)
        exiger(sha == attendu, f"{chemin} : empreinte {sha[:16]} ≠ attendue {attendu[:16]}")
        compagnon = Path(f"{chemin}.sha256")
        sceau = compagnon.read_text(encoding="utf-8").split()[0] if compagnon.exists() else None
        print(f"{sha}  {chemin}  (compagnon .sha256 : {'égal' if sceau == sha else 'ABSENT OU DIFFÉRENT'})")
    brut_table = subprocess.run(["git", "-C", str(DEPOT), "show", f"{COMMIT}:{CHEMIN_TABLE_V3}"], capture_output=True,
                                check=True).stdout
    sha_t = hashlib.sha256(brut_table).hexdigest()
    exiger(sha_t == TABLE_V3_SHA, f"table v3 : {sha_t[:16]} ≠ {TABLE_V3_SHA[:16]}")
    print(f"{sha_t}  git show {COMMIT[:8]}:{CHEMIN_TABLE_V3}")
    table = json.loads(brut_table.decode("utf-8"))

    # --- chargements ---------------------------------------------------------------------------------------------
    z, toutes_cles = charger_npz_cles(NPZ_REJEU, CLES_NPZ_PERMISES)
    print(f"clés du .npz du rejeu (répertoire du zip) : {toutes_cles}")
    print(f"clés lues : {list(CLES_NPZ_PERMISES)} ; non lues : {[k for k in toutes_cles if k not in CLES_NPZ_PERMISES]}")
    jp, toutes_jp = charger_npz_cles(JETONS_PRINC, CLES_JETONS_PERMISES)
    print(f"clés de jetons-principales-p3.npz : {toutes_jp}")
    print(f"clés lues : {list(CLES_JETONS_PERMISES)} ; non lues : {[k for k in toutes_jp if k not in CLES_JETONS_PERMISES]}")
    rejeu = json.loads(JSON_REJEU.read_text(encoding="utf-8"))["resultat"]
    brut_textes = TEXTES.read_bytes()
    separateurs_unicode = {nom: brut_textes.count(b) for nom, b in
                           (("U+2028", " ".encode()), ("U+2029", " ".encode()), ("U+0085", "\u0085".encode()))}
    textes = [json.loads(x) for x in brut_textes.decode("utf-8").split("\n") if x.strip()]
    fiches_brutes = json.loads(FICHES.read_text(encoding="utf-8"))["resultat"]
    fiches = []
    for f in fiches_brutes["fiches"]:
        eq = f["equivalence"]
        fiches.append({"episode": f["episode"], "condition": f["condition"], "tache": f["tache"],
                       "jetons_par_action": [int(x) for x in f["jetons_par_action"]], "empreintes": f["empreintes"],
                       "equivalence": {k: eq[k] for k in CLES_EQUIVALENCE_PERMISES}})
    descriptifs = fiches_brutes["descriptifs"]
    reglages_p3 = fiches_brutes["reglages"]
    del fiches_brutes
    resume = json.loads(RESUME.read_text(encoding="utf-8"))["resultat"]
    manifeste = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    config_p3 = manifeste["config"]

    n = len(z["episode"])
    episode = [str(x) for x in z["episode"].tolist()]
    pas = [int(x) for x in z["pas"].tolist()]
    condition = [str(x) for x in z["condition"].tolist()]
    tache = [str(x) for x in z["tache"].tolist()]
    jn = z["jetons_empan"].astype(np.int64)               # jetons notés de P3 (identite["jetons_notes"])
    jr = z["jetons_empan_rejeu"].astype(np.int64)         # longueur de la reconstruction (texte retokenisé ou table)
    conforme = z["conforme_longueur"].astype(bool)
    contexte = z["contexte_conforme"].astype(bool)
    ecart = z["ecart_fidelite"].astype(np.float64)
    fidele = z["fidele"].astype(bool)
    traj = z["trajectoire_identique"].astype(bool)
    activ = z["activations_identiques"].astype(bool)
    print(f"couches du rejeu : {z['couches'].tolist()} ; actions : {n}")

    titre("1. Contrôles de cohérence entre pièces")
    exiger(n == 2400 and len(textes) == n, f"{n} actions, {len(textes)} textes")
    for i, x in enumerate(textes):
        exiger((x["episode"], x["pas"], x["condition"], x["tache"]) == (episode[i], pas[i], condition[i], tache[i]),
               f"ligne {i} : identité des textes ≠ identité du rejeu")
    print("identité (épisode, pas, condition, tâche) : textes de P3 = tableaux du rejeu, ligne à ligne, 2 400 sur 2 400")
    ordre_eps = list(dict.fromkeys(episode))
    exiger(len(ordre_eps) == 240 and [f["episode"] for f in fiches] == ordre_eps, "ordre des fiches ≠ ordre du rejeu")
    par_ep = {e: list(range(k * T, k * T + T)) for k, e in enumerate(ordre_eps)}
    for e, rs in par_ep.items():
        exiger([episode[r] for r in rs] == [e] * T and [pas[r] for r in rs] == list(range(T)), f"{e} : non contigu")
    print("fiches de P3 : 240, même ordre que le rejeu ; épisodes contigus, pas 0 à 9")
    exiger(resume["episodes"] == 240 and resume["actions"] == n and resume["actions_notees"] == n
           and resume["textes_sha256"] == ATTENDUES[TEXTES] and resume["jetons_principales_sha256"] == ATTENDUES[JETONS_PRINC],
           "résumé de P3 incohérent avec les pièces")
    print(f"résumé de P3 : 240 épisodes, {n} actions, {n} notées ; empreintes citées des textes et de "
          f"jetons-principales égales aux fichiers ; commit cité {resume['commit_cite'][:12]}, commit du run "
          f"{manifeste['commit'][:12]}")
    fiche = {f["episode"]: f for f in fiches}
    jetons = np.array([fiche[episode[i]]["jetons_par_action"][pas[i]] for i in range(n)], dtype=np.int64)
    a_fin = jetons - jn
    exiger(set(a_fin.tolist()) <= {0, 1}, "jetons − jetons notés hors de {0, 1}")
    sans_fin = np.where(a_fin == 0)[0]
    exiger(all(jetons[i] == MAX_NOUVEAUX for i in sans_fin), "action sans jeton de fin de moins de 400 jetons")
    print(f"jetons de P3 (fiches) − jetons notés (rejeu) ∈ {{0, 1}} : oui ; actions sans jeton de fin : {len(sans_fin)}, "
          f"toutes à {MAX_NOUVEAUX} jetons (troncature par max_nouveaux)")
    print(f"jetons générés (somme des jetons par action) : {int(jetons.sum())} ; descriptif de P3 jetons_generes : "
          f"{descriptifs['jetons_generes']} → {'égal' if int(jetons.sum()) == descriptifs['jetons_generes'] else 'DIFFÉRENT'}")
    # jetons-principales : rang, longueur
    rang = jp["rang"].astype(np.int64)
    longueur = jp["longueur"].astype(np.int64)
    debut_jp = jp["debut"].astype(np.int64)
    bornes = jp["bornes"].astype(np.int64)
    lisibles = jp["bornes_lisibles"].astype(bool)
    exiger(rang.tolist() == list(range(n)), "rang de jetons-principales ≠ 0..2399")
    exiger(bool((longueur == jn).all()), "longueur (jetons-principales) ≠ jetons notés")
    exiger(bool((debut_jp == np.concatenate([[0], np.cumsum(longueur)[:-1]])).all()), "debut incohérent")
    print(f"jetons-principales-p3.npz : rang = 0..2399, longueur = jetons notés de P3 pour les 2 400 actions, "
          f"bornes de forme {tuple(bornes.shape)}, bornes lisibles {int(lisibles.sum())} / {len(lisibles)}")
    # recomptes du rejeu
    ft = rejeu["fidelite_toutes"]
    tol = float(rejeu["fidelite_echantillon"]["tolerance"])
    notees = np.isfinite(ecart)
    recompte = {"actions": n, "notees": int(notees.sum()), "conformes_longueur": int(conforme.sum()),
                "contextes_conformes": int(contexte.sum()), "fideles": int(fidele.sum()),
                "egalite_exacte": int((ecart == 0).sum()),
                "fideles_parmi_contextes_conformes": int((fidele & contexte).sum())}
    for k, v in recompte.items():
        exiger(ft[k] == v, f"{k} : {v} recompté ≠ {ft[k]} écrit")
    print(f"recomptes égaux au résultat du rejeu : {recompte}")
    exiger(int(traj.sum()) // T == rejeu["empreintes_p3"]["trajectoires_identiques"] == 151, "trajectoires")
    exiger(int(activ.sum()) // T == rejeu["empreintes_p3"]["activations_identiques_au_bit"] == 151, "activations")
    exiger(bool((traj == activ).all()), "trajectoire identique ≠ activations identiques au bit")
    print("trajectoire identique ⇔ activations identiques au bit, action par action : 1 510 actions, 151 épisodes")
    exiger(bool((fidele == (notees & conforme & (np.nan_to_num(ecart, nan=np.inf) <= tol))).all()), "définition de fidèle")
    print(f"fidèle = notée et conforme en longueur et écart ≤ {tol} : vérifié sur les 2 400 actions")
    non_fid = ~fidele
    bande = int(((ecart > 0) & (ecart <= tol)).sum())
    print(f"bande de tolérance 0 < écart ≤ {tol} : {bande} action(s) ; écart minimal parmi les non fidèles conformes "
          f"en longueur : {float(np.min(ecart[non_fid & conforme])):.4g} ; parmi toutes les non fidèles : "
          f"{float(np.min(ecart[non_fid])):.4g}")
    exiger(bool((fidele <= contexte).all()) and bool((fidele == (ecart == 0)).all()),
           "fidèle hors contexte exact, ou fidèle à écart non nul")
    print("toute action fidèle est en contexte exact et à écart exactement nul (et réciproquement : écart nul ⇒ fidèle)")
    exiger(bool((traj <= fidele).all()), "action à trajectoire identique non fidèle")
    print(f"séparateurs Unicode de ligne dans le fichier des textes (bruts) : {separateurs_unicode} "
          "(un seul ferait échouer `charger_textes_alignes`, qui coupe par `splitlines`)")
    # contexte_conforme = préfixe conforme (épisodes hors table), vrai partout pour les épisodes à trajectoire identique
    for e, rs in par_ep.items():
        if traj[rs].all():
            exiger(bool(contexte[rs].all() and conforme[rs].all()), f"{e} : identique mais non conforme")
        else:
            attendu = np.cumprod(conforme[rs]).astype(bool)
            exiger(bool((contexte[rs] == attendu).all()), f"{e} : contexte conforme ≠ préfixe des conformes")
    print("contexte_conforme = préfixe des actions conformes en longueur (épisodes cassés) ; vrai partout ailleurs : vérifié")

    titre("2. Plan des lots de P3 (plan_p3 : tâches dans l'ordre du fichier × 4 conditions ; lots consécutifs de 8)")
    lot_taille = int(config_p3["lot"])
    exiger(lot_taille == 8 and int(config_p3["T"]) == T and int(config_p3["max_nouveaux"]) == MAX_NOUVEAUX
           and float(config_p3["temperature"]) == 1.0, "configuration de P3 inattendue")
    lots = [ordre_eps[k:k + lot_taille] for k in range(0, 240, lot_taille)]
    for k in range(0, 240, 4):
        bloc = ordre_eps[k:k + 4]
        exiger([fiche[e]["condition"] for e in bloc] == list(CONDITIONS)
               and len({fiche[e]["tache"] for e in bloc}) == 1, f"bloc {k} : pas une tâche × 4 conditions dans l'ordre")
    print(f"{len(lots)} lots de {lot_taille} épisodes = 2 tâches × 4 conditions (honnête, saboteur, témoin, mention), "
          "dans l'ordre des fiches : vérifié")
    # passes de décodage et lignes finies avant, recalculées depuis les jetons par action et le plan des lots
    passes, finies_avant = 0, 0
    for lot in lots:
        for t in range(T):
            longs = [fiche[e]["jetons_par_action"][t] for e in lot]
            passes += max(longs) - 1
            finies_avant += sum(1 for x in longs if x < max(longs))
    print(f"passes de décodage recalculées (Σ lots, pas : max des jetons du lot − 1) : {passes} ; descriptif de P3 : "
          f"{descriptifs['passes_decodage']} → {'égal' if passes == descriptifs['passes_decodage'] else 'DIFFÉRENT'}")
    print(f"lignes finies avant les autres, recalculées : {finies_avant} ; descriptif de P3 : "
          f"{descriptifs['lignes_finies_avant']} → {'égal' if finies_avant == descriptifs['lignes_finies_avant'] else 'DIFFÉRENT'}")
    gen_s = float(descriptifs["generation_s"])
    print(f"durée de génération de P3 : {gen_s:.1f} s pour 30 lots, soit {gen_s / 30:.1f} s par lot et "
          f"{gen_s / descriptifs['passes_decodage'] * 1000:.1f} ms par passe de décodage (lot de 8, cache) ; passe "
          f"unique (activations) : {descriptifs['passe_unique_s']:.1f} s pour 240 épisodes")
    print(f"réglages de P3 : carte {reglages_p3['carte']}, torch {reglages_p3['torch']}, cuDNN {reglages_p3['cudnn']}, "
          f"pilote {reglages_p3['pilote']}, cublas {reglages_p3['cublas_workspace']}, déterministe "
          f"{reglages_p3['deterministe']}, tf32 {reglages_p3['tf32']} ; rejeu v3 : pilote {rejeu['reglages']['pilote']}, "
          f"torch {rejeu['reglages']['torch']}, cuDNN {rejeu['reglages']['cudnn']}")

    titre("3. Graines de P3, redérivées et vérifiées contre l'échantillon d'équivalence consigné par P3")
    graines = manifeste["graines"]
    taches_ordre = list(dict.fromkeys(fiche[e]["tache"] for e in ordre_eps))
    exiger(len(taches_ordre) == 60 and all(f"tache/{t}" in graines for t in taches_ordre), "graines de tâche absentes")
    frac = float(config_p3["fraction_equivalence"])
    graines_tache, ech_tache = {}, {}
    for t in taches_ordre:
        graines_tache[t], ech_tache[t] = graines_et_echantillon(graines[f"tache/{t}"], frac)
    accord_ech = 0
    for e in ordre_eps:
        consigne = {int(k.split(",")[1]) for k in fiche[e]["equivalence"]["actions"]}
        accord_ech += consigne == ech_tache[fiche[e]["tache"]]
    print(f"60 graines `tache/<identifiant>` ; état de contrôle de chaque SeedSequence égal au manifeste ; échantillon "
          f"d'équivalence redérivé (g.random(T) < {frac} après les 10 graines) égal à celui des fiches pour "
          f"{accord_ech} épisodes sur 240 (numpy {np.__version__})")
    exiger(accord_ech == 240, "échantillon d'équivalence redérivé ≠ fiches : graines non redérivables")
    print("→ les graines des 2 400 actions sont redérivables exactement (mêmes graines pour les 4 conditions d'une tâche)")

    titre("4. Les 89 épisodes cassés")
    casses = [e for e in ordre_eps if not traj[par_ep[e]].all()]
    exiger(len(casses) == 89, f"{len(casses)} épisodes cassés")
    lot_de = {e: k for k, lot in enumerate(lots) for e in lot}
    dans_table = {x["episode"]: x for x in table["episodes"]}
    lignes_ep = []
    for e in casses:
        rs = par_ep[e]
        nc = [t for t in range(T) if not conforme[rs[t]]]
        nf = [t for t in range(T) if not fidele[rs[t]]]
        exiger(bool(nc), f"{e} : cassé sans action non conforme")
        prem_nc, prem_nf = nc[0], nf[0]
        fid = [t for t in range(T) if fidele[rs[t]]]
        exiger(fid == list(range(prem_nf)), f"{e} : les fidèles ne forment pas un préfixe")
        prefixe_nf = [t for t in range(T) if contexte[rs[t]] and not fidele[rs[t]]]
        lignes_ep.append({"episode": e, "condition": fiche[e]["condition"], "tache": fiche[e]["tache"],
                          "lot": lot_de[e], "rang_lot": lots[lot_de[e]].index(e), "non_conformes": nc,
                          "premier_non_conforme": prem_nc, "premier_non_fidele": prem_nf, "fideles": len(fid),
                          "perdues": T - len(fid), "prefixe_non_fidele": prefixe_nf, "dans_table_v3": e in dans_table})
    print("épisode | condition | tâche | lot (rang) | 1er pas non conforme | 1er pas non fidèle | pas non conformes | "
          "fidèles | perdues")
    for x in lignes_ep:
        print(f"{x['episode']} | {x['condition']} | {x['tache']} | {x['lot']} ({x['rang_lot']}) | "
              f"{x['premier_non_conforme']} | {x['premier_non_fidele']} | {x['non_conformes']} | {x['fideles']} | "
              f"{x['perdues']}")
    print(f"épisodes cassés présents dans la table v3 : {sum(x['dans_table_v3'] for x in lignes_ep)}")
    exiger(sum(x["perdues"] for x in lignes_ep) == 652, "pertes ≠ 652")
    print()
    print("Comptes par condition :")
    cnt = {}
    for c in CONDITIONS:
        sel = [x for x in lignes_ep if x["condition"] == c]
        idx = [i for i in range(n) if condition[i] == c]
        d = {"episodes_casses": len(sel), "racines_non_conformes": int((~conforme[idx]).sum()),
             "conformes_apres_non_conforme": int((conforme[idx] & ~contexte[idx]).sum()),
             "prefixe_contexte_conforme": int(sum(1 for i in idx if contexte[i] and not traj[i])),
             "prefixe_non_fideles": int((contexte[idx] & ~fidele[idx]).sum()),
             "perdues": sum(x["perdues"] for x in sel), "fideles": int(fidele[idx].sum()),
             "couverture": round(float(fidele[idx].sum()) / len(idx), 4),
             "manque_pour_0_80": max(0, int(np.ceil(SEUIL_COUVERTURE * len(idx))) - int(fidele[idx].sum()))}
        cnt[c] = d
        print(f"  {c:9s} {d}")
    tot = {k: sum(cnt[c][k] for c in CONDITIONS) for k in ("episodes_casses", "racines_non_conformes",
                                                         "conformes_apres_non_conforme", "prefixe_contexte_conforme",
                                                         "prefixe_non_fideles", "perdues", "fideles")}
    print(f"  total     {tot}")
    print()
    for cle, nom in (("premier_non_conforme", "premier pas non conforme"), ("premier_non_fidele", "premier pas non fidèle")):
        print(f"Par {nom} (épisodes) :")
        for c in CONDITIONS + ("total",):
            sel = [x for x in lignes_ep if c == "total" or x["condition"] == c]
            h = collections.Counter(x[cle] for x in sel)
            print(f"  {c:9s} " + " ".join(f"{t}:{h.get(t, 0)}" for t in range(T)))
    avant = [x for x in lignes_ep if x["premier_non_fidele"] < x["premier_non_conforme"]]
    print(f"épisodes dont la première action non fidèle précède la première non conforme (découpage invisible ou fin "
          f"autre dans le préfixe) : {len(avant)} ; actions de préfixe non fidèles : "
          f"{sum(len(x['prefixe_non_fidele']) for x in lignes_ep)} dans {sum(1 for x in lignes_ep if x['prefixe_non_fidele'])} épisodes")
    for x in avant:
        print(f"  {x['episode']} : préfixe non fidèle aux pas {x['prefixe_non_fidele']}, 1er non conforme au pas "
              f"{x['premier_non_conforme']}")
    nb_racines = collections.Counter(len(x["non_conformes"]) for x in lignes_ep)
    print(f"nombre d'actions non conformes par épisode cassé : {dict(sorted(nb_racines.items()))}")

    titre("5. Réparation minimale pour 0,80 (480 fidèles sur 600) — règle gelée pour honnête et saboteur")
    for c in CONDITIONS:
        sel = sorted([x for x in lignes_ep if x["condition"] == c], key=lambda x: (-x["perdues"], x["episode"]))
        manque = cnt[c]["manque_pour_0_80"]
        gain, choisis = 0, []
        for x in sel:
            if gain >= manque:
                break
            gain += x["perdues"]
            choisis.append(x)
        racines = sum(len(x["non_conformes"]) for x in choisis)
        # pire cas : épisodes non réparés de plus forte perte d'abord ; combien peuvent rester cassés ?
        marge = cnt[c]["fideles"] + cnt[c]["perdues"] - int(np.ceil(SEUIL_COUVERTURE * 600))
        restants, cumul = 0, 0
        for x in sel:
            if cumul + x["perdues"] > marge:
                break
            cumul += x["perdues"]
            restants += 1
        regle = "règle" if c in CONDITIONS_REGLE else "hors règle"
        print(f"  {c:9s} ({regle}) : manque {manque} ; au minimum {len(choisis)} épisode(s) entier(s) à réparer "
              f"(les plus coûteux d'abord ; {racines} action(s) non conforme(s) à corriger, gain {gain}) : "
              f"{[x['episode'] for x in choisis]}")
        print(f"            couverture si les {len(sel)} épisodes sont réparés : 600 / 600 ; épisodes qui peuvent rester "
              f"cassés au pire (les plus coûteux d'abord) sans passer sous 0,80 : {restants} (marge {marge} actions)")
    # sélection qui minimise le nombre d'actions à corriger (sac à dos exact ; un épisode à préfixe non fidèle compte
    # une correction cachée de plus, au moins)
    print("Sélection qui minimise le nombre d'actions à corriger (non conformes, plus 1 par épisode à découpage caché "
          "dans le préfixe), sous la contrainte gain ≥ manque :")
    for c in CONDITIONS_REGLE:
        sel = [x for x in lignes_ep if x["condition"] == c]
        manque = cnt[c]["manque_pour_0_80"]
        meilleur = {0: (0, [])}                       # gain plafonné → (poids, épisodes)
        for x in sel:
            poids = len(x["non_conformes"]) + (1 if x["prefixe_non_fidele"] else 0)
            for g_, (p_, l_) in list(meilleur.items()):
                g2 = min(manque, g_ + x["perdues"])
                cand = (p_ + poids, l_ + [x["episode"]])
                if g2 not in meilleur or cand[0] < meilleur[g2][0] or (cand[0] == meilleur[g2][0] and len(cand[1]) < len(meilleur[g2][1])):
                    meilleur[g2] = cand
        p_, l_ = meilleur[manque]
        gain = sum(x["perdues"] for x in sel if x["episode"] in l_)
        print(f"  {c:9s} : {p_} action(s) à corriger dans {len(l_)} épisode(s), gain {gain} : {l_}")
    # gain optimiste si seule la première action non conforme de chaque épisode est corrigée
    print("Gain si l'on ne corrige que la première action non conforme de chaque épisode (sans autre découpage "
          "invisible ; plafonné par l'action non conforme suivante) :")
    for c in CONDITIONS:
        g = 0
        for x in lignes_ep:
            if x["condition"] != c:
                continue
            suivant = x["non_conformes"][1] if len(x["non_conformes"]) > 1 else T
            if x["premier_non_fidele"] == x["premier_non_conforme"]:
                g += suivant - x["premier_non_conforme"]
        print(f"  {c:9s} gain ≤ {g} → couverture ≤ {(cnt[c]['fideles'] + g) / 600:.3f}")

    titre("6. Les 164 actions non conformes en longueur")
    rac = [i for i in range(n) if not conforme[i]]
    exiger(len(rac) == 164, f"{len(rac)} racines")
    ecart_l = {i: int(jr[i] - jn[i]) for i in rac}
    print("écart de longueur = jetons_empan_rejeu − jetons_empan (texte retokenisé − jetons notés de P3) :")
    h = collections.Counter(ecart_l.values())
    print("  distribution : " + ", ".join(f"{k:+d}: {h[k]}" for k in sorted(h)))
    for c in CONDITIONS:
        hc = collections.Counter(ecart_l[i] for i in rac if condition[i] == c)
        print(f"  {c:9s} " + ", ".join(f"{k:+d}: {hc[k]}" for k in sorted(hc)))
    neg, nul, pos = ([i for i in rac if ecart_l[i] < 0], [i for i in rac if ecart_l[i] == 0],
                     [i for i in rac if ecart_l[i] > 0])
    print(f"  classes : écart < 0 (P3 a plus de jetons que le découpage canonique) {len(neg)} ; écart nul (même compte, "
          f"texte décodé différent) {len(nul)} ; écart > 0 {len(pos)}")
    rel = [abs(ecart_l[i]) / max(1, int(jn[i])) for i in rac]
    print(f"  |écart| / jetons notés : médiane {np.median(rel):.4f}, maximum {max(rel):.4f}")
    print(f"  par pas : {dict(sorted(collections.Counter(pas[i] for i in rac).items()))}")
    print(f"  jetons notés de P3 des racines : médiane {int(np.median(jn[rac]))}, min {int(jn[rac].min())}, "
          f"max {int(jn[rac].max())} ; des conformes : médiane {int(np.median(jn[conforme]))}")
    tronquees = [i for i in rac if a_fin[i] == 0]
    print(f"  racines tronquées à 400 jetons (sans fin) : {len(tronquees)} ; parmi les conformes : "
          f"{int(((a_fin == 0) & conforme).sum())}")
    tr_m = a_fin == 0
    for nom, m in (("tronquées", tr_m), ("non tronquées", ~tr_m)):
        print(f"  actions {nom} : {int(m.sum())} ; non conformes {int((~conforme & m).sum())} "
              f"({100 * (~conforme & m).sum() / m.sum():.1f} %) ; taux par jeton généré "
              f"{(~conforme & m).sum() / jetons[m].sum() * 1e4:.2f} pour 10 000 jetons")
        hc = collections.Counter(ecart_l[i] for i in rac if bool(m[i]))
        print(f"    écarts : " + ", ".join(f"{k:+d}: {hc[k]}" for k in sorted(hc)))
    # traits
    tr = [traits(textes[i]["texte"], int(jetons[i]), int(a_fin[i])) for i in range(n)]
    noms = list(tr[0])
    conf = [i for i in range(n) if conforme[i]]
    print()
    print("Traits du texte : racines (164) contre actions conformes en longueur (2 236) ; rapport des taux")
    print("  trait | racines | % | conformes | % | rapport | écart<0 | écart=0 | écart>0 | honnête | saboteur | témoin | mention")
    for k in noms:
        a = sum(tr[i][k] for i in rac)
        b = sum(tr[i][k] for i in conf)
        pa, pb = a / len(rac), b / len(conf)
        rapport = (pa / pb) if pb > 0 else (float("inf") if pa > 0 else float("nan"))
        parcl = [sum(tr[i][k] for i in s) for s in (neg, nul, pos)]
        parco = [sum(tr[i][k] for i in rac if condition[i] == c) for c in CONDITIONS]
        print(f"  {k} | {a} | {100 * pa:.1f} | {b} | {100 * pb:.1f} | {rapport:.2f} | {parcl[0]} | {parcl[1]} | "
              f"{parcl[2]} | {parco[0]} | {parco[1]} | {parco[2]} | {parco[3]}")
    lourds = [i for i in rac if any(tr[i][k] for k in TRAITS_LOURDS)]
    print(f"racines portant un trait « avec perte » (U+FFFD, jeton spécial, rôle, vide, contrôle, format) : {len(lourds)}")
    for i in lourds:
        print(f"  ligne {i} {episode[i]} pas {pas[i]} écart {ecart_l[i]:+d} : "
              f"{[k for k in TRAITS_LOURDS if tr[i][k]]}")
    clas = collections.Counter()
    for i in rac:
        t = tr[i]
        if any(t[k] for k in TRAITS_LOURDS):
            clas["(b/c) trait avec perte"] += 1
        elif t["nombre d'au moins 4 chiffres"] or t["milliers séparés (espace, virgule, insécable)"]:
            clas["(a1) nombre long ou en milliers"] += 1
        elif any(t[k] for k in ("espaces multiples (au moins 2)", "tabulation", "retour chariot \\r",
                                "espace avant un retour à la ligne", "au moins 3 retours à la ligne consécutifs",
                                "espace Unicode autre que U+0020", "blanc en tête ou en fin de texte")):
            clas["(a2) blancs inhabituels"] += 1
        elif any(t[k] for k in ("lettre non ASCII", "symbole ou ponctuation non ASCII",
                                "caractère hors du plan de base (> U+FFFF, émoji…)", "ponctuation répétée (4 identiques ou plus)")):
            clas["(a3) non ASCII ou ponctuation répétée"] += 1
        else:
            clas["(a4) aucun de ces traits (autre)"] += 1
    print(f"classement exclusif des 164 (priorité dans l'ordre) : {dict(clas)}")
    # même classement sur les conformes, pour la base
    clas_c = collections.Counter()
    for i in conf:
        t = tr[i]
        if any(t[k] for k in TRAITS_LOURDS):
            clas_c["(b/c) trait avec perte"] += 1
        elif t["nombre d'au moins 4 chiffres"] or t["milliers séparés (espace, virgule, insécable)"]:
            clas_c["(a1) nombre long ou en milliers"] += 1
        elif any(t[k] for k in ("espaces multiples (au moins 2)", "tabulation", "retour chariot \\r",
                                "espace avant un retour à la ligne", "au moins 3 retours à la ligne consécutifs",
                                "espace Unicode autre que U+0020", "blanc en tête ou en fin de texte")):
            clas_c["(a2) blancs inhabituels"] += 1
        elif any(t[k] for k in ("lettre non ASCII", "symbole ou ponctuation non ASCII",
                                "caractère hors du plan de base (> U+FFFF, émoji…)", "ponctuation répétée (4 identiques ou plus)")):
            clas_c["(a3) non ASCII ou ponctuation répétée"] += 1
        else:
            clas_c["(a4) aucun de ces traits (autre)"] += 1
    print(f"même classement sur les 2 236 conformes (base) : {dict(clas_c)}")
    # classes mécaniques : (c') chaîne de jeton ajouté écrite en clair, (b) U+FFFD, (a) redécoupage
    speciales = [i for i in rac if tr[i]["chaîne de jeton spécial <|…|>"]]
    fffd_r = [i for i in rac if tr[i]["U+FFFD (caractère de remplacement)"] and i not in speciales]
    autres = [i for i in rac if i not in speciales and i not in fffd_r]
    for nom, s in (("(c') chaîne <|…|> écrite en clair, reconnue comme un seul jeton au retokenage", speciales),
                   ("(b) U+FFFD (octets perdus au décodage)", fffd_r), ("(a) redécoupage du texte (le reste)", autres)):
        hs = collections.Counter(ecart_l[i] for i in s)
        print(f"classe {nom} : {len(s)} racines ; écarts " + ", ".join(f"{k:+d}: {hs[k]}" for k in sorted(hs)))
        if s is speciales:
            for i in s:
                m = RE_SPECIAL.search(textes[i]["texte"])
                print(f"  {episode[i]} pas {pas[i]} : {m.group(0)!r} ; écart {ecart_l[i]:+d}")
    seules_spec = [x for x in lignes_ep if x["non_conformes"]
                   and all(tr[par_ep[x["episode"]][t]]["chaîne de jeton spécial <|…|>"] for t in x["non_conformes"])]
    print(f"épisodes dont toutes les actions non conformes sont de classe (c') (candidats à un essai sur processeur, "
          f"tokenisation sans reconnaissance des jetons ajoutés, arbitrée par l'empreinte) : "
          f"{[(x['episode'], x['perdues'], 'préfixe non fidèle' if x['prefixe_non_fidele'] else 'préfixe fidèle') for x in seules_spec]}")
    # place dans la table v3
    corrigees = sum(1 for i in rac if episode[i] in dans_table and dans_table[episode[i]]["methode"] != "non_resolu")
    non_res = sum(1 for i in rac if episode[i] in dans_table and dans_table[episode[i]]["methode"] == "non_resolu")
    print(f"place dans la table v3 : corrigées {corrigees} ; non résolues {non_res} ; absentes {164 - corrigees - non_res} "
          f"(la table ne couvre que les {len(dans_table)} épisodes « signalés », entièrement conformes en longueur)")
    meth = collections.Counter(x["methode"] for x in table["episodes"])
    print(f"table v3 : {dict(meth)} ; comptes {table['comptes']['identiques_base']} de base + "
          f"{table['comptes']['identiques_apres_table'] - table['comptes']['identiques_base']} corrigés")
    exemples = [(x["episode"], tp) for x in table["episodes"] for tp in (x.get("textes_p3") or [])]
    print(f"découpages non canoniques déjà prouvés (table v3, `textes_p3`, même longueur) : {len(exemples)}")
    for e, tp in exemples:
        print(f"  {e} pas {tp['pas']} : canonique {tp['canonique']} contre P3 {tp['p3']}")
    fins_autres = [(x["episode"], x["fins"]) for x in table["episodes"] if x.get("fins")]
    print(f"fins autres que la fin par défaut, prouvées : {fins_autres} (fins du format : {table['fins_du_format']})")
    long_id = [(x["episode"], [(a["pas"], len(a["canonique"]), len(a["p3"])) for a in x["actions"]])
               for x in table["episodes"] if x["methode"] == "identifiants"]
    print(f"entrées « identifiants » (pas, longueur canonique, longueur P3) : {long_id}")
    # test du nettoyage des espaces au décodage (clean_up_tokenization_spaces) sur les 2 400 textes
    occ = [(i, m.group(0)) for i in range(n) for m in RE_NETTOYAGE.finditer(textes[i]["texte"])]
    print(f"motifs que supprimerait un nettoyage d'espaces au décodage (« x . », « x , », « x n't »…) : "
          f"{len(occ)} occurrence(s) dans {len({i for i, _ in occ})} texte(s) ; exemples {[m for _, m in occ[:8]]}")
    print(f"U+FFFD dans les 2 400 textes : {sum(t['texte'].count(chr(0xFFFD)) for t in textes)} "
          f"(textes : {[ (episode[i], pas[i]) for i in range(n) if chr(0xFFFD) in textes[i]['texte']]})")

    titre("7. Ce que P3 a gardé et qui peut servir d'oracle")
    print(f"empreintes par épisode (trajectoire, activations) : {sum(1 for f in fiches if len(f['empreintes']['trajectoire']) == 64)}"
          f" / 240 trajectoires, {sum(1 for f in fiches if len(f['empreintes']['activations']) == 64)} / 240 activations ; "
          f"distinctes : {len({f['empreintes']['trajectoire'] for f in fiches})}")
    print("jetons par action (fiches) et jetons notés : 2 400 / 2 400 ; donc la longueur exacte de chaque action, et la "
          "présence d'un jeton de fin (non son identité)")
    # bornes des champs (rangs de jeton de P3) : couverture
    anc = [(int((bornes[i] >= 0).sum())) for i in range(n)]
    print(f"bornes des champs (rang du premier jeton de TITLE, PROPOSAL, CONTROLS, COST, PREDICTION dans les jetons "
          f"générés par P3) : actions avec ≥ 1 borne {sum(1 for a in anc if a >= 1)} / 2 400 ; ≥ 3 bornes "
          f"{sum(1 for a in anc if a >= 3)} ; racines avec ≥ 1 borne {sum(1 for i in rac if anc[i] >= 1)} / 164 ; "
          f"5 bornes {sum(1 for i in rac if anc[i] == 5)} / 164")
    # cohérence bornes (rangs) / positions en caractères
    coherent = 0
    for i in range(n):
        bc = bornes_caracteres(textes[i]["texte"])
        presents_c = {c for c in CHAMPS_BORNES if bc[c] >= 0}
        presents_j = {c for k, c in enumerate(CHAMPS_BORNES) if bornes[i][k] >= 0}
        ordre_c = sorted(presents_c, key=lambda c: bc[c])
        ordre_j = sorted(presents_j, key=lambda c: int(bornes[i][CHAMPS_BORNES.index(c)]))
        coherent += presents_c == presents_j and ordre_c == ordre_j
    print(f"bornes de P3 cohérentes avec les champs relus dans le texte (mêmes champs, même ordre) : {coherent} / 2 400")
    # échantillon d'équivalence
    ech_tot = sum(len(f["equivalence"]["actions"]) for f in fiches)
    ech_casses = [(f["episode"], int(k.split(",")[1])) for f in fiches if f["episode"] in set(casses)
                  for k in f["equivalence"]["actions"]]
    prem_nc = {x["episode"]: x["premier_non_conforme"] for x in lignes_ep}
    ech_apres = [(e, t) for e, t in ech_casses if t >= prem_nc[e]]
    tailles = collections.Counter(v["taille_lot"] for f in fiches for v in f["equivalence"]["lignes"].values())
    ok_rang = all(v["ligne"] == lots[lot_de[f["episode"]]].index(f["episode"])
                  for f in fiches for v in f["equivalence"]["lignes"].values())
    ok_emp = all(len(v) == 64 for f in fiches for v in f["equivalence"]["empreintes_capture"].values())
    print(f"échantillon d'équivalence (activations capturées pendant la génération en lot) : {ech_tot} actions dans "
          f"{sum(1 for f in fiches if f['equivalence']['actions'])} épisodes ; taille de lot consignée {dict(tailles)} ; "
          f"rang de ligne = rang dans le lot reconstruit : {ok_rang} ; empreintes sha256 de capture présentes : {ok_emp}")
    print(f"  dans les 89 épisodes cassés : {len(ech_casses)} actions ; au pas de la première non conforme ou après : "
          f"{len(ech_apres)} {ech_apres}")
    L_lot = collections.defaultdict(dict)
    for f in fiches:
        for k, v in f["equivalence"]["lignes"].items():
            t = int(k.split(",")[1])
            L = v["remplissage"] + f["equivalence"]["longueurs_contexte"][k]
            L_lot[lot_de[f["episode"]]].setdefault(t, set()).add(L)
    incoherents = [(k, t, s) for k, d in L_lot.items() for t, s in d.items() if len(s) > 1]
    print(f"  longueur remplie du lot L = remplissage + longueur du contexte, connue pour {sum(len(d) for d in L_lot.values())} "
          f"couples (lot, pas) sur 300 ; incohérences entre lignes d'un même (lot, pas) : {len(incoherents)}")

    titre("8. Composition des lots en épisodes cassés (forme du « lot fidèle »)")
    print("lot | tâches | cassés (rangs) | conditions cassées | actions d'équivalence dans le lot | jetons générés du lot")
    nb_par_lot = collections.Counter()
    for k, lot in enumerate(lots):
        cs = [e for e in lot if e in set(casses)]
        nb_par_lot[len(cs)] += 1
        ech_lot = sum(len(fiche[e]["equivalence"]["actions"]) for e in lot)
        print(f"{k} | {sorted({fiche[e]['tache'] for e in lot})} | {len(cs)} ({[lot.index(e) for e in cs]}) | "
              f"{[fiche[e]['condition'] for e in cs]} | {ech_lot} | {sum(sum(fiche[e]['jetons_par_action']) for e in lot)}")
    print(f"lots par nombre d'épisodes cassés : {dict(sorted(nb_par_lot.items()))}")
    lots_casses = [k for k, lot in enumerate(lots) if any(e in set(casses) for e in lot)]
    lots_sains = [k for k in range(30) if k not in lots_casses]
    print(f"lots sans aucun épisode cassé (témoin pur du lot fidèle) : {lots_sains}")
    print(f"lots à rejouer pour couvrir les 89 : {len(lots_casses)} ; génération de P3 pour ces lots ≈ "
          f"{gen_s / 30 * len(lots_casses) / 3600:.2f} h (au prorata de {gen_s / 30:.0f} s par lot)")
    pas_cibles = sum(max(fiche[e]['jetons_par_action'][t] for e in lots[k]) for k in lots_casses for t in range(T))
    print(f"passes de décodage de ces lots (toutes lignes jusqu'au bout) : {pas_cibles} ≈ "
          f"{pas_cibles * gen_s / descriptifs['passes_decodage'] / 3600:.2f} h au rythme de P3")
    tok_casses = sum(sum(fiche[e]['jetons_par_action']) for e in casses)
    print(f"jetons générés des 89 épisodes : {tok_casses} ; une cible à la fois (passes arrêtées à la fin de la cible) "
          f"≈ {tok_casses * gen_s / descriptifs['passes_decodage'] / 3600:.2f} h au rythme de P3")
    ms_passe = gen_s / descriptifs["passes_decodage"]
    print("Lots candidats aux épreuves :")
    for k in (2, 13, 3):
        lot = lots[k]
        p_lot = sum(max(fiche[e]["jetons_par_action"][t] for e in lot) - 1 for t in range(T))
        etat = []
        for e in lot:
            if e in set(casses):
                etat.append(f"{e} : cassé (non conformes {[t for t in range(T) if not conforme[par_ep[e][t]]]})")
            elif e in dans_table:
                etat.append(f"{e} : corrigé par la table v3 ({dans_table[e]['methode']})")
            else:
                etat.append(f"{e} : identique de base")
        ech = [(e, sorted(int(x.split(',')[1]) for x in fiche[e]['equivalence']['actions'])) for e in lot
               if fiche[e]['equivalence']['actions']]
        print(f"  lot {k} : {p_lot} passes de décodage ≈ {p_lot * ms_passe / 60:.1f} min au rythme de P3 ; "
              f"actions d'équivalence {ech}")
        for x in etat:
            print(f"    {x}")

    titre("9. Résumé machine")
    resume_machine = {
        "episodes_casses": len(casses), "par_condition": {c: cnt[c] for c in CONDITIONS},
        "premier_non_conforme": dict(sorted(collections.Counter(x["premier_non_conforme"] for x in lignes_ep).items())),
        "racines": 164, "ecart_longueur": {str(k): h[k] for k in sorted(h)},
        "racines_trait_avec_perte": len(lourds), "classement_exclusif": dict(clas),
        "graines_redérivées": accord_ech, "lots_sains": lots_sains, "lots_avec_casses": len(lots_casses),
        "passes_recalculees_egales": passes == descriptifs["passes_decodage"],
        "nettoyage_occurrences": len(occ),
    }
    print(json.dumps(resume_machine, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
