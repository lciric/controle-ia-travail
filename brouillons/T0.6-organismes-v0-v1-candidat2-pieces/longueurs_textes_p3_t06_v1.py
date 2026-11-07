"""Longueurs en jetons des textes de P3 pour T0.6 (marqueur `LONGUEURS_TEXTES_P3` du candidat 2 ; fille 10, 7 novembre 2026, décision de la mère R-1653).

Deux chaînes, mesurées avec le tokeniseur de la tâche, sans jetons spéciaux :
(a) les 6 blocs de consigne et d'indication de P3 (`prereg/P3-consignes-v1.md`, citations « > »), comme
    `docs/notes/P3-mesures-calcul-v1/longueurs_consignes.py` ;
(b) le message assemblé par l'environnement **au premier pas** (pas 0) pour chaque tâche (64 d'évaluation + 32 de réserve), dans les
    quatre conditions : consigne privée = `EnvironnementPropositions.consigne_privee(0)` (consigne honnête, format d'action, énoncé, guide
    et classification H.11, puis la consigne cachée de la condition) ; observation = `EnvironnementPropositions.observation(0, 0, [])`
    (tour 1, index, indication privée de la condition, « Your action: ») ; l'environnement est construit par
    `premier_test_ia.conditions.environnement(condition, tache, T, guide, consignes)` comme le fait le lanceur de T0.6 (T de la
    configuration, guide `H1-classification`). Longueur du message = longueur de la consigne + longueur de l'observation (chacune
    tokenisée séparément : l'une est le message système, l'autre le message de l'utilisateur ; le gabarit de conversation n'est pas compté).
    **L'égalité « tâche par tâche » porte sur (b)** : pour chaque tâche, IA (saboteur), IT (témoin) et IM (mention) ont la même longueur de
    consigne, la même longueur d'observation et la même longueur de message ; tout écart est listé (nœud).

Mode `reel` : le tokeniseur doit être celui de Llama-3.1-8B-Instruct, d'empreinte (sha256 du fichier `tokenizer.json`) commençant par
`79e3e522` ; toute autre empreinte est REFUSÉE (code 2, rien n'est imprimé). Mode `factice` : tout tokeniseur, sortie marquée
« FACTICE » et jamais utilisable comme sortie brute. Bibliothèque : `tokenizers` ; aucun réseau, aucune clé, aucune sonde.

    .venv/bin/python -I -B longueurs_textes_p3_t06_v1.py --mode reel --tokenizer TOKENIZER.json \\
        --config docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon4.json > longueurs-textes-p3-t06-v1.txt
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from tokenizers import Tokenizer

PREFIXE_TOKENISEUR_ATTENDU = "79e3e522"
CONDITIONS = (("honnete", "H"), ("saboteur", "IA"), ("temoin", "IT"), ("mention", "IM"))
INSTRUITES = ("IA", "IT", "IM")


class RefusTokeniseur(SystemExit):
    pass


def sha256_fichier(chemin) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def verifier_tokeniseur(chemin, mode: str, prefixe_attendu: str = PREFIXE_TOKENISEUR_ATTENDU) -> str:
    """Garde : en mode réel, seule l'empreinte attendue passe (le préfixe doit faire au moins 8 caractères hexadécimaux)."""
    if mode not in ("reel", "factice"):
        raise RefusTokeniseur(f"mode {mode!r} : reel ou factice")
    sha = sha256_fichier(chemin)
    if mode == "reel":
        if len(prefixe_attendu) < 8 or any(ch not in "0123456789abcdef" for ch in prefixe_attendu):
            raise RefusTokeniseur(f"préfixe attendu illisible : {prefixe_attendu!r}")
        if not sha.startswith(prefixe_attendu):
            raise RefusTokeniseur(f"tokeniseur d'empreinte {sha[:16]}… ≠ {prefixe_attendu}… attendue : refus (mode réel)")
    return sha


def longueur(tok: Tokenizer, texte: str) -> int:
    return len(tok.encode(texte, add_special_tokens=False).ids)


def mesurer(tok: Tokenizer, consignes: dict, blocs: list[str], taches: dict[str, list], T: int, guide: str | None) -> dict:
    from controle_ia.environnements.pilote_a import tache_de
    from controle_ia.premier_test_ia.conditions import environnement

    sortie = {"blocs": [(k, longueur(tok, b), hashlib.sha256(b.encode("utf-8")).hexdigest()[:16], b[:60]) for k, b in enumerate(blocs)], "taches": [], "ecarts": []}
    for jeu in sorted(taches):
        for donnee in taches[jeu]:
            ligne = {"jeu": jeu, "tache": donnee["identifiant"]}
            for cond, sigle in CONDITIONS:
                env = environnement(cond, tache_de(donnee), T, guide, consignes)
                c, o = longueur(tok, env.consigne_privee(0)), longueur(tok, env.observation(0, 0, []))
                ligne[sigle] = (c, o, c + o)
            sortie["taches"].append(ligne)
            for i, nom in enumerate(("consigne", "observation", "message")):
                valeurs = {s: ligne[s][i] for s in INSTRUITES}
                if len(set(valeurs.values())) != 1:
                    sortie["ecarts"].append((jeu, donnee["identifiant"], nom, valeurs))
    return sortie


def imprimer(res: dict, mode: str, entetes: list[str]) -> str:
    L = [f"# Longueurs des textes de P3 pour T0.6 — mode {mode}" + (" — FACTICE : ne pas citer comme sortie brute" if mode == "factice" else "")]
    L += entetes
    L.append("\n## (a) les 6 blocs de consigne et d'indication (ordre : consigne et indication du saboteur, du témoin, de la mention)")
    L += [f"{k} {n} {h} {t}" for k, n, h, t in res["blocs"]]
    L.append("\n## (b) message assemblé au premier pas : jeu tâche condition consigne observation message")
    for ligne in res["taches"]:
        L.append(f"{ligne['jeu']} {ligne['tache']} " + " ; ".join(f"{s} {ligne[s][0]} {ligne[s][1]} {ligne[s][2]}" for _, s in CONDITIONS))
    n = len(res["taches"])
    L.append(f"\n## égalité tâche par tâche entre IA, IT et IM : {n - len({(e[0], e[1]) for e in res['ecarts']})} tâches sur {n} égales sur les trois mesures ; {len(res['ecarts'])} écart(s)")
    L += [f"- ÉCART {jeu} {t} {nom} : {v}" for jeu, t, nom, v in res["ecarts"]]
    return "\n".join(L) + "\n"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", required=True, choices=("reel", "factice"))
    ap.add_argument("--tokenizer", required=True)
    ap.add_argument("--config", required=True)
    ap.add_argument("--racine", default=".")
    a = ap.parse_args(argv)
    racine = Path(a.racine)
    sys.path.insert(0, str(racine / "src"))          # `-I` ignore PYTHONPATH : le code du dépôt est pris sous la racine donnée
    try:
        sha_tok = verifier_tokeniseur(a.tokenizer, a.mode)
    except RefusTokeniseur as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    from controle_ia.environnements.invites import charger_invite
    from controle_ia.environnements.pilote_a import charger_taches
    from controle_ia.premier_test_ia.conditions import blocs_cites, charger_consignes

    cfg = json.loads(Path(a.config).read_text(encoding="utf-8"))
    chemin_c = racine / cfg["chemin_consignes"]
    consignes = charger_consignes(chemin_c, cfg["consignes_sha256"])
    taches = {}
    for jeu, cle in (("evaluation", "taches_evaluation"), ("reserve", "taches_distillation")):
        f = racine / cfg[cle]["chemin"]
        if sha256_fichier(f) != cfg[cle]["sha256"]:
            print(f"REFUS : {f} : empreinte ≠ celle de la configuration", file=sys.stderr)
            return 2
        taches[jeu] = charger_taches(f)
    blocs = blocs_cites(chemin_c.read_text(encoding="utf-8"))
    res = mesurer(Tokenizer.from_file(a.tokenizer), consignes, blocs, taches, int(cfg["T"]), charger_invite("H1-classification"))
    entetes = [f"tokenizer.json {sha_tok}", f"consignes {cfg['chemin_consignes']} {consignes['sha256']}",
               f"tâches d'évaluation {cfg['taches_evaluation']['chemin']} {cfg['taches_evaluation']['sha256']}",
               f"tâches de réserve {cfg['taches_distillation']['chemin']} {cfg['taches_distillation']['sha256']}", f"T {cfg['T']}",
               f"script {sha256_fichier(__file__)}"]
    sys.stdout.write(imprimer(res, a.mode, entetes))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
