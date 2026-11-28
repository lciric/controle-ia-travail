#!/usr/bin/env python3
"""Relance du rejeu des activations, voie (A), après la panne du jeton (décision R-5275, GO-2026-11-24-13) — v1.

Enveloppe, côté session seulement, de l'amorce v2 scellée (`rejeu_activations_voie_a_v2.py`, inchangée ; la machine exécute
toujours la v2 du commit de lancement). Elle ne change que trois choses :
1. Le script de démarrage clone avec le jeton à grain fin (CONTROLE_IA_GITHUB_TOKEN_3), puis, s'il échoue, avec
   CONTROLE_IA_GITHUB_TOKEN_2 ; chaque essai pousse le commit de lancement sur la branche témoin
   `donnees/temoin-jeton-rejeu-v1` AVANT toute autre étape (téléchargement du modèle compris). Le jeton qui réussit devient
   GH_TOKEN ; les deux variables d'essai sont retirées de l'environnement avant l'amorce. Si les deux échouent : la machine
   se détruit elle-même par son identifiant (clé d'instance), sans rien lancer.
2. Garde avant création : chacun des deux jetons doit compter au moins 30 caractères (un jeton de façade de proxy est refusé).
3. La réponse de création de l'outil est lue d'un bloc (JSON sur plusieurs lignes) avant le repli ligne à ligne.
Les jetons sont lus par leur nom, jamais écrits dans un journal ni dans le script (le script ne porte que des noms de variables).
Limites (contre-lecture) : les deux variables d'essai sont retirées de l'environnement du shell qui lance l'amorce, non de
celui du conteneur ; la poussée témoin est refusée si la branche témoin porte déjà un commit qui n'est pas un ancêtre du
commit de lancement (une relance sur un autre commit prend une branche témoin neuve) ; ne pas recharger ce module après `main`.
"""
from __future__ import annotations

import base64
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from controle_ia import rejeu_activations_voie_a_v2 as R  # noqa: E402

VERSION = "relance-rejeu-jeton-v1"
JETON_PRINCIPAL = "CONTROLE_IA_GITHUB_TOKEN_3"
JETON_REPLI = "CONTROLE_IA_GITHUB_TOKEN_2"
LONGUEUR_MIN_JETON = 30
BRANCHE_TEMOIN = "donnees/temoin-jeton-rejeu-v1"
_SCRIPT_V2 = R.script_de_demarrage  # référence gardée avant toute substitution


def garde_jetons(env: dict) -> dict[str, str]:
    """Deux jetons d'au moins 30 caractères, distincts ; sinon refus (aucune création)."""
    a, b = env.get(JETON_PRINCIPAL, ""), env.get(JETON_REPLI, "")
    for nom, v in ((JETON_PRINCIPAL, a), (JETON_REPLI, b)):
        if len(v) < LONGUEUR_MIN_JETON or any(c.isspace() or c in "\"'" for c in v):
            raise R.Refus(f"{nom} absent, trop court (< {LONGUEUR_MIN_JETON}) ou mal formé : jeton de façade refusé")
    if a == b:
        raise R.Refus("les deux jetons sont égaux : le repli ne serait pas un repli")
    return {"GH_TOKEN_A": a, "GH_TOKEN_B": b}


def script_de_demarrage(commit: str, ordre_rel: str, ordre_sha: str, api: str = R.API_VAST) -> str:
    """Script du conteneur : minuterie de secours, puis essai des deux jetons (clonage + poussée témoin), puis l'amorce v2."""
    base = _SCRIPT_V2(commit, ordre_rel, ordre_sha)  # contrôles de forme de la v2
    if not re.fullmatch(r"https://[a-z0-9./-]+", api):
        raise R.Refus("adresse de l'interface de Vast mal formée")
    secours = base.split("if [ ! -d /root/depot/.git ]; then ")[0]  # minuterie de secours de la v2, inchangée
    amorce = base.split("; fi; ", 1)[1]                              # lancement de l'amorce v2, inchangé
    detruire = ("import os, urllib.request as u; "
                f"u.urlopen(u.Request('{api}/instances/' + os.environ['CONTAINER_ID'] + '/', "
                "method='DELETE', headers={'Authorization': 'Bearer ' + os.environ['CONTAINER_API_KEY']}), timeout=60)")
    return (secours +
            "A='!f() { echo username=x-access-token; echo \"password=${GH_TOKEN}\"; }; f'; OK=0; "
            # redémarrage du conteneur : le clone existe ; on reprend le jeton qui avait réussi (lettre seule, sur disque)
            "if [ -d /root/depot/.git ] && [ -s /root/jeton-choisi.txt ]; then J=$(cat /root/jeton-choisi.txt); "
            "case \"$J\" in A|B) eval \"T=\\${GH_TOKEN_$J:-}\"; export GH_TOKEN=\"$T\"; OK=1; "
            "echo \"REDÉMARRAGE : jeton $J repris\";; *) echo \"REDÉMARRAGE : lettre de jeton illisible\";; esac; fi; "
            "[ \"$OK\" = 1 ] || for J in A B; do eval \"T=\\${GH_TOKEN_$J:-}\"; [ -n \"$T\" ] || continue; rm -rf /root/depot; "
            "if GH_TOKEN=\"$T\" git -c credential.helper=\"$A\" clone -q \"$DEPOT_URL\" /root/depot "
            f"&& git -C /root/depot checkout -q --detach {commit} "
            f"&& GH_TOKEN=\"$T\" git -C /root/depot -c credential.helper=\"$A\" push -q origin {commit}:refs/heads/{BRANCHE_TEMOIN}; "
            "then echo \"JETON $J : clonage et poussée témoin réussis\"; echo \"$J\" > /root/jeton-choisi.txt; "
            "export GH_TOKEN=\"$T\"; OK=1; break; "
            "else echo \"JETON $J : refusé\"; fi; done; "
            "unset GH_TOKEN_A GH_TOKEN_B T; "
            "if [ \"$OK\" != 1 ]; then echo \"JETONS REFUSÉS : destruction de la machine par son identifiant\"; "
            f"for k in 1 2 3 4 5; do python3 -I -B -c \"{detruire}\" && break; sleep 20; done; sleep infinity; exit 1; fi; "
            + amorce)


class ClientCreation(R.ClientVastCli):
    """Création par l'outil (forme de la v2) ; jeton de repli ajouté à l'environnement de la machine, GH_TOKEN retiré ;
    réponse lue d'un bloc avant le repli ligne à ligne."""

    def __init__(self, cle: str, outil: str, jetons: dict[str, str]):
        super().__init__(cle, outil)
        self.jetons = jetons

    def creer(self, offre_id: int, corps: dict, secrets: dict[str, str]) -> int:
        env = {k: v for k, v in corps["env"].items() if k != "GH_TOKEN"}
        env.update(self.jetons)
        if any(c.isspace() or c in "\"'" for v in env.values() for c in v):
            raise R.Refus("valeur d'environnement avec espace ou guillemet : refus (forme -e K=V)")
        args = [self.outil, "create", "instance", str(int(offre_id)), "--raw", "--image", corps["image"], "--disk",
                str(corps["disk"]), "--cancel-unavail", "--label", corps["label"], "--env",
                " ".join(f"-e {k}={v}" for k, v in env.items()), "--entrypoint", "bash", "--args", "-c", corps["script"]]
        try:
            r = subprocess.run(args, capture_output=True, timeout=300, env={**os.environ, "VAST_API_KEY": self._cle})
        except subprocess.TimeoutExpired:
            raise R.Refus("création : délai dépassé ; vérifier par l'inventaire avant toute nouvelle location") from None
        texte = (r.stdout + r.stderr).decode("utf-8", "replace")
        for nom, v in {**secrets, **self.jetons}.items():
            if v:
                texte = texte.replace(v, f"[{nom} masquée]")
        if r.returncode != 0:
            raise R.Refus(f"création : code {r.returncode} : {texte[-300:]}")
        rep = lire_reponse(texte)
        if not isinstance(rep, dict) or not rep.get("success") or not isinstance(rep.get("new_contract"), int):
            raise R.Refus("réponse de création illisible ou refusée : vérifier par l'inventaire avant toute nouvelle location")
        return rep["new_contract"]


def lire_reponse(texte: str):
    """Réponse de l'outil : un objet JSON d'un bloc (forme de vastai 1.11), sinon la dernière ligne JSON."""
    try:
        rep = json.loads(texte.strip())
        if isinstance(rep, dict):
            return rep
    except ValueError:
        pass
    for ligne in reversed(texte.strip().splitlines()):
        try:
            return json.loads(ligne)
        except ValueError:
            continue
    return None


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] != "creer":
        print("REFUS : seule la sous-commande « creer » est enveloppée ; les autres se lancent sur la v2")
        return 2
    try:
        jetons = garde_jetons(os.environ)
    except R.Refus as e:
        print(f"REFUS : {e}")
        return 2
    # la v2 exige GH_TOKEN non vide : on lui donne le jeton principal (il est retiré de l'environnement de la machine)
    os.environ["GH_TOKEN"] = jetons["GH_TOKEN_A"]
    R.script_de_demarrage = script_de_demarrage
    outil = argv[argv.index("--outil") + 1] if "--outil" in argv else "vastai"
    client = ClientCreation(os.environ.get("VAST_API_KEY", ""), outil, jetons)
    p = R.argparse.ArgumentParser()
    s = p.add_subparsers(dest="cmd", required=True)
    c = s.add_parser("creer")
    for k in ("--fiche", "--feu", "--go", "--registre", "--garde", "--ordre", "--ordre-rel", "--ordre-sha256", "--offres",
              "--commit"):
        c.add_argument(k, required=True)
    c.add_argument("--outil", default="vastai")
    c.add_argument("--verifier-seulement", action="store_true")
    c.add_argument("--attente-s", type=float, default=20.0)
    a = p.parse_args(argv)
    return R.creer(a, client)


if __name__ == "__main__":
    sys.exit(main())
