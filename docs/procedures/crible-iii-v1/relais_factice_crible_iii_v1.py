#!/usr/bin/env python3
"""Relais factice du crible (iii) — v1 (essai à blanc seulement ; aucun appel réel, aucune clé).

C'est le relais du pilote, `relais_pilote_v70.py` de l'arbre (chargé tel quel depuis son chemin, son empreinte gardée : `/relais/etat`
rend la sienne), dont seul l'amont factice (`corps_factice`) est remplacé, dans ce processus, par un amont scripté qui sait
répondre aux trois gabarits du crible : G1 (liste de vingt ensembles), G2 (une carte par ensemble numéroté) et G0 (cartes du
pilote). Tout le reste (jeton, plafond, nombre d'appels, verrou du pire cas, journal, témoin du corps) est le code du pilote.

Arguments propres, retirés avant de passer la main au relais : `--relais-pilote CHEMIN` (le relais de l'arbre),
`--scenarios-crible FICHIER` (JSON {"mondes": {empreinte du contexte servi : r}, "textes_h": {empreinte du texte de H : r},
"defaut_g2": "D" ou "B", "scenarios": {"r|bras" ou "*|bras" : scénario}} ; un fichier par relais).
Scénarios : `normal`, `tronque`, `illisible`, `panne`, `limite` (erreur 429 de l'amont), `lent-S` (S secondes puis normal),
`cout_excessif`, `k1_seul`, `ensembles_invalides`, `ensembles_archive`, `sept_cartes`. L'appelant reste `factice:…` (le relais le
déclare) ; ce fichier refuse tout appelant réel.
"""
import hashlib
import importlib.util
import json
import os
import re
import sys
import time


def _retirer(argv, nom):
    if nom not in argv:
        return argv, None
    i = argv.index(nom)
    return argv[:i] + argv[i + 2:], argv[i + 1]


def cle_du_contexte(consigne):
    """Empreinte du premier bloc ```json … ``` du texte servi : la même en G0, G1 et G2 pour un monde donné."""
    i = consigne.find("```json\n")
    j = consigne.find("\n```", i + 8)
    return hashlib.sha256(consigne[i + 8:j].encode("utf-8")).hexdigest() if i >= 0 and j > i else None


def bras_du_texte(consigne):
    if "Sans proposer de loi, rends vingt ensembles" in consigne:
        return "P1"
    if "Ensembles de traits (un par carte, dans l'ordre) :" in consigne:
        return "G2"
    return "S"


def ensembles_g2(consigne):
    return [[int(x) for x in m.group(1).split(", ")] for m in re.finditer(r"^Ensemble \d+ : \[([0-9, ]+)\]$", consigne, re.M)]


def ensembles_scriptes(r, scenario, k1_traits):
    """Vingt ensembles déterministes (r donné) ; doublons, ensemble de l'archive et invalides compris, pour éprouver le filtre."""
    if scenario == "ensembles_invalides":
        return [[9, 10], "x", [], [1, 1], [0, 1, 2, 3]]
    if scenario == "ensembles_archive":
        return [sorted(k1_traits)] * 3
    out = [sorted(k1_traits)] if k1_traits else []
    paires = [[(r + i) % 8, (r + 3 * i + 1) % 8] for i in range(8)]
    out += [p for p in paires if p[0] != p[1]]
    out += [[(r + i) % 8] for i in range(4)] + [[(r + 1) % 8, (r + 4) % 8, (r + 6) % 8], [0, 9], [2, 2]]
    out += [list(x) for x in paires[:2]]
    return out[:23]


def principal(argv, environ):
    argv, chemin = _retirer(list(argv), "--relais-pilote")
    argv, fichier = _retirer(argv, "--scenarios-crible")
    if not chemin or not os.path.isfile(chemin):
        print("relais factice du crible : --relais-pilote CHEMIN exigé", file=sys.stderr)
        sys.exit(2)
    i = argv.index("--appelant") if "--appelant" in argv else -1
    if i < 0 or not argv[i + 1].startswith("factice:"):
        print("relais factice du crible : appelant factice seulement", file=sys.stderr)
        sys.exit(2)
    script = json.load(open(fichier, encoding="utf-8")) if fichier else {"mondes": {}, "scenarios": {}}
    spec = importlib.util.spec_from_file_location("relais_pilote_v70", chemin)
    R = importlib.util.module_from_spec(spec)
    sys.modules["relais_pilote_v70"] = R
    spec.loader.exec_module(R)

    def corps_scripte(dialecte, modele, consigne, max_tokens, scenario_relais, comprise=True):
        cle = cle_du_contexte(consigne)
        r = script["mondes"].get(cle)
        quoi = bras_du_texte(consigne)
        ctx = R._contexte(consigne)
        k1 = ctx["lois_retenues"][0]["loi"]
        k1_traits = sorted({j for j in range(len(k1["poids"][0])) if len({l[j] for l in k1["poids"]}) > 1})
        sha_texte = hashlib.sha256(consigne.encode()).hexdigest()
        bras = quoi if quoi != "G2" else ("H" if sha_texte in script.get("textes_h", {}) else script.get("defaut_g2", "D"))
        if bras == "H":  # le texte de H est propre à son monde (ensembles tirés par r) : r lu sans ambiguïté
            r = script["textes_h"][sha_texte]
        sc = script["scenarios"].get(f"{r}|{bras}") or script["scenarios"].get(f"*|{bras}") or "normal"
        if sc.startswith("lent-"):
            time.sleep(float(sc[5:]))
            sc = "normal"
        if sc == "panne":
            raise ConnectionResetError("panne factice")
        if sc == "limite":
            raise R.ErreurAmont(429, "rate_limit_error")
        raison = "fin"
        if sc == "illisible":
            texte = "Je ne propose rien."
        elif quoi == "P1":
            texte = "```json\n" + json.dumps(ensembles_scriptes(r or 0, sc, k1_traits)) + "\n```"
        elif quoi == "G2":
            cartes = []
            for e in ensembles_g2(consigne):
                loi = json.loads(json.dumps(k1))
                for j, t in enumerate(e):
                    loi["poids"][1][t] = round(0.25 + 0.25 * j, 6)
                    loi["poids"][2][t] = round(-0.25 - 0.25 * j, 6)
                cartes.append({"enonce": f"carte de l'ensemble {e}", "loi_predictive": k1 if sc == "k1_seul" else loi})
            if sc == "sept_cartes":
                cartes += [{"enonce": "carte en trop", "loi_predictive": k1}] * (7 - len(cartes))
            texte = "```json\n" + json.dumps(cartes) + "\n```"
        else:
            texte = "```json\n" + json.dumps(R.cartes_factices(consigne, "k1_seul" if sc == "k1_seul" else "k1_plus")) + "\n```"
        if sc == "tronque":
            texte, raison = texte[: len(texte) // 2], "borne"
        entree, sortie = len(consigne.encode("utf-8")) // 4 + 7, min(max_tokens, len(texte) // 4 + 100)
        if sc == "tronque":
            sortie = max_tokens
        if sc == "cout_excessif":
            sortie = max_tokens * 10
        sr = {"fin": "end_turn", "borne": "max_tokens"}[raison]
        return {"id": "msg_factice", "type": "message", "role": "assistant", "model": modele, "stop_reason": sr,
                "stop_details": None, "content": [{"type": "thinking", "thinking": ""}, {"type": "text", "text": texte}],
                "usage": {"input_tokens": entree, "output_tokens": sortie}}

    R.corps_factice = corps_scripte
    R.principal(argv, environ)


if __name__ == "__main__":
    principal(sys.argv[1:], dict(os.environ))
