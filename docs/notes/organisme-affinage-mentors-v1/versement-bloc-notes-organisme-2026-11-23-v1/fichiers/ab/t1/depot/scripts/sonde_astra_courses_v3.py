#!/usr/bin/env python3
"""Sonde d'Astra commune — version 3 (`gpt-6.2-astra`, variable de clé du relais jeté contrôlée ; lanceur v11c).

Version 3 (R12 ; la v2, `scripts/sonde_astra_courses_v2.py`, `80074c82…`, reste en place). Seul changement, sur le constat 9
de la contre-lecture du lanceur v11b (`contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`) : la ligne de commande du relais
jeté, lue par son PID, doit porter `--variable-cle OPENAI_API_KEY_2` (la clé d'Astra de la course v11) ; sinon refus avant
tout appel (code 2). Version écrite au rapport : `sonde_astra_courses_v3`. Texte de la v2 ci-dessous.

Sonde d'Astra commune — version 2 (`gpt-6.2-astra`, pour le lanceur v11 de la course d'affinage).

Version 2 (R12 ; la v1, `scripts/sonde_astra_courses_v1.py`, `d374d107…`, reste en place et sert les courses qui la citent).
Écrite le 22 novembre 2026 (pièce de classe B). Ce qui change, et rien d'autre :
1. modèle exigé du relais jeté et du rapport : **`gpt-6.2-astra`** (au lieu de `gpt-6-astra`) ;
2. prix exigés du relais jeté : **8 / 40 USD par million** (entrée, sortie ; R-4905), au lieu de 10 / 50 : le pire cas du
   relais doit égaler celui de la commande, à qui la sonde v3 passe ces prix ;
3. l'unique appel passe par la **sonde v3** (`scripts/sonde_astra_affinage_v3.py`, empreinte épinglée ci-dessous) au lieu de
   la v2 ; le rapport qu'elle écrit au chemin `--sortie-v2` porte `version` = `sonde_astra_affinage_v3` (le nom de l'option
   est gardé pour que les commandes se lisent comme celles de la v1) ;
4. version écrite au rapport : `sonde_astra_courses_v2`.
Tout le reste est la v1 : refus avant tout appel (code 2), échec de configuration rapporté sans appel (code 1), contrôles
après l'appel, rapport scellé, jamais de texte rendu ni de clé. La variable de clé du relais jeté n'est pas lue ici (son nom
est contrôlé par le lanceur v11 sur le relais de la course) ; pour la course v11, le relais d'Astra est lancé sur
`OPENAI_API_KEY_2`.

Usage :
    python3 -I -B scripts/sonde_astra_courses_v2.py --commande COMMANDE_ASTRA --url-relais-jete http://127.0.0.1:8793 \\
        --pid-relais-jete PID --sortie RAPPORT.json --sortie-v2 RAPPORT_V3.json
Codes : 0 sonde réussie ; 1 sonde non réussie (rapport écrit) ; 2 refus avant tout appel (rien d'écrit).
Bibliothèque standard seulement. En-tête de la v1 : voir `scripts/sonde_astra_courses_v1.py`.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

VERSION = "sonde_astra_courses_v3"
VARIABLE_CLE = "OPENAI_API_KEY_2"  # v3 : clé d'Astra de la course v11, lue au relais jeté par son PID
DEPOT = Path(__file__).resolve().parents[1]
EMPREINTE_COMMANDE = "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71"
SONDE_V2 = DEPOT / "scripts" / "sonde_astra_affinage_v3.py"  # nom de variable gardé : la sonde appelée
EMPREINTE_SONDE_V2 = "32366123751ba1d1620cadf4dd4cfda039c0bf35af614a75b49e2d9c04dad7ff"
PROGRAMME_RELAIS = "relais_kimi_v4.py"
EMPREINTE_RELAIS = "67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e"
VERSION_RELAIS = "relais-kimi-v4"
AMONT = "https://api.openai.com"
MODELE = "gpt-6.2-astra"
PLAFOND_USD = 0.05
PRIX = (8.0, 40.0)  # USD par million (entrée, sortie) : ceux que la sonde v3 passe à la commande (R-4905)
PORTS_DES_COURSES = (8787, 8788, 8789, 8790, 8791, 8792)
URL_LOCALE = re.compile(r"^http://127\.0\.0\.1:(\d{2,5})$")
EPS = 1e-12


class Refus(Exception):
    """Refus avant tout appel : rien n'est écrit, rien n'est envoyé."""


def sha256_fichier(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def date_u() -> str:
    return subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, timeout=10).stdout.strip()


def lire_etat_local(url: str) -> dict:
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # boucle locale : jamais de mandataire
    with ouvreur.open(url.rstrip("/") + "/relais/etat", timeout=10) as rep:
        return json.loads(rep.read().decode("utf-8"))


def lire_cmdline(pid: int) -> list:
    return [x for x in Path(f"/proc/{pid}/cmdline").read_bytes().decode("utf-8", "replace").split("\0") if x]


def _valeur(args: list, nom: str):
    return args[args.index(nom) + 1] if nom in args and args.index(nom) + 1 < len(args) else None


def charger_sonde_v2(chemin: Path = SONDE_V2):
    if not chemin.is_file() or sha256_fichier(chemin) != EMPREINTE_SONDE_V2:
        raise Refus(f"sonde v3 absente ou d'une autre empreinte que {EMPREINTE_SONDE_V2[:12]}…")
    spec = importlib.util.spec_from_file_location("sonde_astra_affinage_v3_pour_sonde_commune_v2", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def verifier_adresse(url: str) -> int:
    """Boucle locale seulement, hors des ports des relais de course : contrôlé avant toute lecture d'état."""
    m = URL_LOCALE.match(url or "")
    if not m:
        raise Refus("adresse du relais jeté : http://127.0.0.1:PORT seulement")
    port = int(m.group(1))
    if port in PORTS_DES_COURSES:
        raise Refus(f"port {port} : port d'un relais de course ({PORTS_DES_COURSES}) — le relais jeté doit être distinct, "
                    "le relais de la course doit rester neuf")
    return port


def controler_identite(commande: Path, url: str, pid: int, sortie: Path, sortie_v2: Path, etat: dict, cmdline: list,
                       amont: str) -> dict:
    """Contrôles d'identité et de nouveauté : tout écart est un refus (code 2), avant tout appel."""
    if not commande.is_file() or sha256_fichier(commande) != EMPREINTE_COMMANDE:
        raise Refus(f"commande d'Astra absente ou d'une autre empreinte que {EMPREINTE_COMMANDE[:12]}…")
    port = verifier_adresse(url)
    if not (isinstance(pid, int) and pid > 1):
        raise Refus("PID du relais jeté exigé")
    for s in (sortie, sortie_v2):
        if s.exists() or Path(str(s) + ".sha256").exists():
            raise Refus(f"{s} existe déjà (R12)")
    if sortie.resolve() == sortie_v2.resolve():
        raise Refus("--sortie et --sortie-v2 doivent différer")
    progs = [a for a in cmdline if Path(a).name == PROGRAMME_RELAIS]
    if len(progs) != 1 or not Path(progs[0]).is_file() or sha256_fichier(Path(progs[0])) != EMPREINTE_RELAIS:
        raise Refus(f"relais jeté (PID {pid}) : programme {PROGRAMME_RELAIS} absent des arguments ou d'une autre empreinte "
                    f"que {EMPREINTE_RELAIS[:12]}…")
    if _valeur(cmdline, "--port") != str(port):
        raise Refus(f"relais jeté (PID {pid}) : --port différent de l'adresse donnée ({port})")
    if cmdline.count("--variable-cle") != 1 or _valeur(cmdline, "--variable-cle") != VARIABLE_CLE:  # v3, constat 9
        raise Refus(f"relais jeté (PID {pid}) : --variable-cle {_valeur(cmdline, '--variable-cle')!r}, {VARIABLE_CLE} exigée "
                    "(une seule fois)")
    if not isinstance(etat, dict):
        raise Refus("état du relais jeté illisible")
    attendus = {"version": VERSION_RELAIS, "pid": pid, "amont": amont, "modeles_permis": [MODELE],
                "variable_cle_encore_presente": False}
    ecarts = {k: etat.get(k) for k, v in attendus.items() if etat.get(k) != v}
    if ecarts:
        raise Refus(f"état du relais jeté différent de l'attendu : {ecarts}")
    if etat.get("appels") != 0 or etat.get("depense_usd") != 0 or etat.get("engage_usd") != 0:
        raise Refus(f"relais jeté non neuf (appels {etat.get('appels')!r}, dépense {etat.get('depense_usd')!r}, engagé "
                    f"{etat.get('engage_usd')!r}) : un relais neuf par sonde")
    return {"url": url, "port": port, "pid": pid, "programme": progs[0], "programme_sha256": EMPREINTE_RELAIS,
            "variable_cle": VARIABLE_CLE,
            "reserve_par_appel_usd": etat.get("reserve_par_appel_usd"), "plafond_usd": etat.get("plafond_usd"),
            "max_appels": etat.get("max_appels"), "prix_entree_usd_par_million": etat.get("prix_entree_usd_par_million"),
            "prix_sortie_usd_par_million": etat.get("prix_sortie_usd_par_million"),
            "prix_cache_usd_par_million": etat.get("prix_cache_usd_par_million"), "amont": etat.get("amont")}


def defauts_de_configuration(relais: dict) -> list:
    """Réglages qui font échouer la sonde à coup sûr ou sortent de R-3273 : échec rapporté, rien n'est envoyé."""
    d = []
    pl, res = relais.get("plafond_usd"), relais.get("reserve_par_appel_usd")
    if not isinstance(pl, (int, float)) or abs(pl - PLAFOND_USD) > EPS:
        d.append(f"plafond du relais {pl!r} USD : {PLAFOND_USD} exigé (R-3273 ; égal au plafond de session de la commande)")
    if not isinstance(res, (int, float)) or (isinstance(pl, (int, float)) and res > pl + EPS):
        d.append(f"réserve par appel {res!r} USD au-dessus du plafond {pl!r} USD : refus 402 certain (relancer le relais jeté "
                 "avec --reserve-par-appel 0.01)")
    if (relais.get("prix_entree_usd_par_million"), relais.get("prix_sortie_usd_par_million")) != PRIX:
        d.append(f"prix du relais {relais.get('prix_entree_usd_par_million')!r} / {relais.get('prix_sortie_usd_par_million')!r} : "
                 f"{PRIX[0]:g} / {PRIX[1]:g} exigés (pire cas du relais égal à celui de la commande)")
    pc = relais.get("prix_cache_usd_par_million")
    if not isinstance(pc, (int, float)) or pc > PRIX[0]:
        d.append(f"prix du cache {pc!r} : au plus le prix d'entrée")
    if relais.get("max_appels") != 1:
        d.append(f"--max-appels {relais.get('max_appels')!r} : 1 exigé (un appel trivial)")
    return d


def ecrire_scelle(chemin: Path, objet: dict) -> str:
    donnees = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


def sonder(commande: Path, url: str, pid: int, sortie: Path, sortie_v2: Path, *, lire_etat=lire_etat_local,
           lire_cmd=lire_cmdline, amont: str = AMONT, sonde_v2: Path = SONDE_V2, horodatage=date_u) -> int:
    v2 = charger_sonde_v2(sonde_v2)
    verifier_adresse(url)
    try:
        etat = lire_etat(url)
    except Exception as e:  # noqa: BLE001 — tout échec de lecture est un refus nommé
        raise Refus(f"état du relais jeté illisible ({type(e).__name__})") from None
    try:
        cmdline = lire_cmd(pid)
    except OSError:
        raise Refus(f"relais jeté : PID {pid} absent") from None
    relais = controler_identite(commande, url, pid, sortie, sortie_v2, etat, cmdline, amont)
    base = {"version": VERSION, "horodatage_utc": horodatage(), "modele": MODELE, "plafond_usd": PLAFOND_USD,
            "commande": {"chemin": str(commande), "sha256": EMPREINTE_COMMANDE},
            "sonde_v2": {"chemin": str(sonde_v2), "sha256": EMPREINTE_SONDE_V2}, "relais_jete": relais,
            "ports_des_courses_exclus": list(PORTS_DES_COURSES),
            "fondement": "mot du directeur, 18 novembre 2026 vers 10:50Z : Astra déclarée ; R-3273 (sonde ≤ 0,05 USD, relais jeté) ; "
                         "Astra = gpt-6.2-astra (commit 9fb4cdc60), prix 8 / 40 (R-4905)",
            "signale": "appel réel trivial, au plus 0,05 USD (R-3273)"}
    base["jour"] = base["horodatage_utc"][:10]
    defauts = defauts_de_configuration(relais)
    if defauts:
        ecrire_scelle(sortie, dict(base, ok=False, echec_de_configuration=True, appel_envoye=False, rapport_v2=None,
                                   cout_usd=None, depense_relais_usd=None, motif=defauts,
                                   lecture="échec de configuration de la sonde, pas échec d'Astra : relancer un relais jeté "
                                           "neuf bien réglé et la sonde sur des chemins neufs"))
        return 1
    code_v2 = v2.principal([str(commande), url, str(pid), str(sortie_v2)])
    rapport_v2 = None
    if sortie_v2.is_file():
        o2 = json.loads(sortie_v2.read_text(encoding="utf-8"))
        rapport_v2 = {"chemin": str(sortie_v2), "sha256": sha256_fichier(sortie_v2), "code_sonde_v2": code_v2,
                      "ok": o2.get("ok"), "code_commande": o2.get("code"), "cout_usd": o2.get("cout_usd"),
                      "modele_servi": o2.get("modele_servi"), "erreur": o2.get("erreur")}
    try:
        apres = lire_etat(url)
    except Exception as e:  # noqa: BLE001
        apres = {"illisible": type(e).__name__}
    dep = apres.get("depense_usd")
    motifs = []
    if not (rapport_v2 and code_v2 == 0 and rapport_v2["ok"] is True):
        motifs.append(f"sonde v3 non réussie (code {code_v2}, {(rapport_v2 or {}).get('erreur')!r})")
    if apres.get("appels") != 1 or apres.get("refus") not in (0, None):
        motifs.append(f"relais jeté après la sonde : appels {apres.get('appels')!r}, refus {apres.get('refus')!r} (1 et 0 exigés)")
    if not isinstance(dep, (int, float)) or dep > PLAFOND_USD + EPS:
        motifs.append(f"dépense lue au relais {dep!r} USD : au plus {PLAFOND_USD} exigé")
    ok = not motifs
    ecrire_scelle(sortie, dict(base, ok=ok, echec_de_configuration=False,
                               appel_envoye=isinstance(apres.get("appels"), int) and apres.get("appels", 0) >= 1,
                               rapport_v2=rapport_v2, cout_usd=(rapport_v2 or {}).get("cout_usd"), depense_relais_usd=dep,
                               etat_relais_apres={k: apres.get(k) for k in ("appels", "refus", "depense_usd", "engage_usd",
                                                                           "reponses_par_statut", "illisible")},
                               motif=motifs or None))
    return 0 if ok else 1


def principal(argv: list | None = None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--commande", required=True)
    a.add_argument("--url-relais-jete", required=True)
    a.add_argument("--pid-relais-jete", type=int, required=True)
    a.add_argument("--sortie", required=True)
    a.add_argument("--sortie-v2", required=True)
    try:
        args = a.parse_args(argv)
    except SystemExit:
        return 2
    sortie = Path(args.sortie)
    try:
        code = sonder(Path(args.commande), args.url_relais_jete, args.pid_relais_jete, sortie, Path(args.sortie_v2))
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    o = json.loads(sortie.read_text(encoding="utf-8"))
    print(json.dumps({"sonde": str(sortie), "ok": o["ok"], "cout_usd": o.get("cout_usd"),
                      "depense_relais_usd": o.get("depense_relais_usd"), "motif": o.get("motif")}, ensure_ascii=False))
    return code


if __name__ == "__main__":
    raise SystemExit(principal())
