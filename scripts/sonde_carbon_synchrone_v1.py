#!/usr/bin/env python3
"""Sonde réelle de Carbon par la chaîne SYNCHRONE d'Argon — course d'auto-conception, tentative v7 (additif v2g) — version 1.

Écrite le 19 novembre 2026 par le développeur unique de la version (modèle L′). **Jamais jouée par l'auteur** : la session
d'exécution la joue, sur une ligne de GO à elle, avant la course. Fondement : mot de Lazar « go (a) » (Carbon par la commande
synchrone d'Argon, éprouvé d'abord par **un appel réel sur le plus grand lot**, puis course) ; « augmente le plafond » (6 USD par
appel) ; « enlève la troncature pour Carbon » (sortie maximale, aucune limite de pensée plus basse).

## Ce qu'elle fait

**Un seul appel** de Carbon par la chaîne de la course : l'enveloppe épinglée `rapports/fille-ideation-1-v1/appel-carbon-
synchrone-v1.sh` (réglage figé) → `commande_argon_v3d.py` (épinglée) → un **relais jeté** `relais_gemini_v2.py` (épinglé) sur
le port 8792, `--modele gemini-4-carbon`, `--max-appels 2` (countTokens puis generateContent), que la session arrête ensuite par
PID avant de lancer le relais neuf de la course. L'entrée est **la plus grande consigne servie à un proposeur dans la course**
(`plus_grande_entree` du lanceur v7 : consigne du proposeur, puis la case du plus grand lot, exactement comme l'orchestrateur la
sert), sous `PLAFOND_SESSION_USD` = 6,00, `ROLE_POLE` = `proposeur_ideation`, `MODELE_DEMANDE_POLE` = `gemini-4-carbon`.

1. **Avant l'appel, refus (code 2 ; rien d'écrit, rien d'envoyé)** si : nom de variable de clé dans l'environnement ; rapport
   existant ; pièces du lanceur v7 d'une autre empreinte (`verifier_pieces` : ce programme, l'enveloppe, la commande d'Argon, la
   consigne, la configuration…) ; ligne de GO de la sonde absente, hors période, révoquée, non « calcul », non accordée par
   Lazar, d'un autre plafond que **6 USD**, ou d'un périmètre sans « sonde » ni « Carbon » (registre lu au commit de `main`) ;
   réglage de l'enveloppe autre que celui de l'additif v2g (`controler_reglage_carbon`) ; matière d'une autre empreinte ; pire
   cas de l'appel, au compte de la commande, au-dessus de 6 USD ou sortie réduite sous le maximum (`pire_cas_carbon`) ; relais
   jeté lu par PID d'un autre programme, d'un autre port, d'autres modèles, d'un autre amont, d'une autre borne que 2, ou non
   neuf (appels, refus), ou variable de clé encore présente.
2. **L'appel** : l'enveloppe lancée dans sa propre session de processus, consigne sur l'entrée standard, délai 1 800 s (le
   délai fixe de l'orchestrateur ; tout le groupe est arrêté au-delà) ; la sortie standard est lue en mémoire et **jamais
   écrite** : seule la dernière ligne JSON est lue, et seuls des champs techniques en sont gardés (`CHAMPS_TECHNIQUES` : code,
   `finishReason`, `modelVersion`, compteurs de jetons, coût, sortie demandée, lecture des pensées) ; le texte rendu n'est
   jamais gardé (sa présence et sa longueur en caractères seulement) ; la sortie d'erreur est jetée.
3. **Après** : état du relais relu (2 appels, 0 refus). « ok » seulement si : code de sortie et code de la commande 0 ;
   `finishReason` STOP ; réponse non vide ; **non tronquée** (STOP, sortie demandée = sortie maximale 65 536) ; modèle servi
   admis par l'orchestrateur (`gemini-4-carbon` ou suffixe de date strict) ; coût > 0 et ≤ 6 USD ; relais : 2 appels, 0 refus.
4. **Rapport scellé** (compagnon `.sha256`) : jour, ok, motifs, champs techniques, entrée (rang, nom, octets, caractères,
   empreinte — jamais le texte), réglage, pire cas, empreintes (programme, enveloppe, commande, relais), ligne de GO, relais,
   durée. Le lanceur v7 le relit (`verifier_sonde_carbon`).

Usage (cwd = racine du dépôt ; aucune clé dans l'environnement : elle est dans le seul relais) :
    env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=«D»/maison LANG=C.UTF-8 /usr/local/bin/python3 -I -B \\
        scripts/sonde_carbon_synchrone_v1.py --go GO-AAAA-MM-JJ-NN --pid-relais PID --sortie RAPPORT.json
Codes : 0 sonde réussie ; 1 sonde non réussie (rapport écrit) ; 2 refus avant tout appel (rien d'écrit, rien d'envoyé).
Bibliothèque standard seulement.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import importlib.util
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

VERSION = "sonde_carbon_synchrone_v1"
DEPOT = Path(__file__).resolve().parents[1]
LANCEUR = DEPOT / "scripts" / "lancer_course_auto_conception_v7.py"
PLAFOND_USD = 6.0                       # mot de Lazar « augmente le plafond » : la sonde sous le plafond d'un appel de la course
MOTS_GO = ("sonde", "carbon")
URL_RELAIS = "http://127.0.0.1:8792"    # l'adresse que l'enveloppe fige : le relais jeté y est, arrêté avant le relais de la course
MAX_APPELS_RELAIS = 2                   # countTokens puis generateContent : un appel de la commande
DELAI_S = 1800.0                        # délai fixe de l'orchestrateur pour toute commande externe
URL_LOCALE = re.compile(r"^http://127\.0\.0\.1:(\d{2,5})$")
# Champs de la dernière ligne de la commande gardés au rapport (jamais « texte », « avertissements », « erreur » en clair)
CHAMPS_TECHNIQUES = ("code", "fin", "modele_servi", "modele_demande", "cout_usd", "cout_origine", "envoye", "pire_cas_usd",
                     "max_sortie_jetons", "provision_pensee_jetons", "config_pensee", "pensees_jetons", "lecture_pensees",
                     "entree_jetons_estimee", "entree_jetons_comptee", "entree_jetons_garde", "marge_entree", "usage",
                     "total_jetons", "ecart_total_jetons", "entree_excedent_jetons", "version")


class Refus(Exception):
    """Refus avant tout appel : rien n'est écrit, rien n'est envoyé."""


def sha256_fichier(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def date_u() -> str:
    return subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, timeout=10).stdout.strip()


def lire_etat_local(url: str) -> dict:
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # boucle locale : jamais de mandataire
    with ouvreur.open(url.rstrip("/") + "/relais/etat", timeout=10) as rep:
        return json.loads(rep.read().decode("utf-8"))


def lire_cmdline(pid: int) -> list:
    return [x for x in Path(f"/proc/{int(pid)}/cmdline").read_bytes().decode("utf-8", "replace").split("\0") if x]


def charger_lanceur(chemin: Path = LANCEUR):
    spec = importlib.util.spec_from_file_location("lancer_course_auto_conception_v7_pour_sonde_carbon", chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


def ecrire_scelle(chemin: Path, objet: dict) -> str:
    donnees = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {Path(chemin).name}\n")
    return h


def _valeur(args: list, nom: str):
    return args[args.index(nom) + 1] if nom in args and args.index(nom) + 1 < len(args) else None


def controler_relais(L, programmes: dict, url: str, pid: int, etat, cmdline: list, amont: str) -> dict:
    """Relais jeté de Carbon : programme épinglé lu par PID, port de l'adresse, `--modele gemini-4-carbon` seul, amont,
    `--max-appels 2` ; état neuf (0 appel, 0 refus), même borne, même liste de modèles, même amont, variable de clé effacée."""
    m = URL_LOCALE.match(url or "")
    if not m:
        raise Refus("adresse du relais jeté : http://127.0.0.1:PORT seulement")
    if not (isinstance(pid, int) and not isinstance(pid, bool) and pid > 1):
        raise Refus("PID du relais jeté exigé")
    nom_prog, attendu = programmes["carbon"]
    progs = [a for a in cmdline if os.path.basename(a) == nom_prog]
    if len(progs) != 1 or not os.path.isfile(progs[0]) or sha256_fichier(progs[0]) != attendu:
        raise Refus(f"relais jeté (PID {pid}) : programme {nom_prog} absent des arguments ou d'une autre empreinte que celle épinglée")
    if _valeur(cmdline, "--port") != m.group(1):
        raise Refus(f"relais jeté (PID {pid}) : --port différent de l'adresse ({m.group(1)})")
    if [cmdline[i + 1] for i, a in enumerate(cmdline) if a == "--modele" and i + 1 < len(cmdline)] != [L.MODELE_CARBON]:
        raise Refus(f"relais jeté : --modele {L.MODELE_CARBON} seul exigé")
    if (_valeur(cmdline, "--amont") or L.AMONT_GEMINI) != amont:
        raise Refus(f"relais jeté : amont {_valeur(cmdline, '--amont')!r}, {amont} exigé")
    if _valeur(cmdline, "--max-appels") != str(MAX_APPELS_RELAIS):
        raise Refus(f"relais jeté : --max-appels {MAX_APPELS_RELAIS} exigé (un appel : countTokens puis generateContent)")
    if not isinstance(etat, dict):
        raise Refus("état du relais jeté illisible")
    attendus = {"appels": 0, "refus": 0, "max_appels": MAX_APPELS_RELAIS, "modeles": [L.MODELE_CARBON], "amont": amont,
                "variable_cle_encore_presente": False}
    ecarts = {k: etat.get(k) for k, v in attendus.items() if etat.get(k) != v}
    if ecarts:
        raise Refus(f"état du relais jeté différent de l'attendu (relais neuf exigé) : {ecarts}")
    return {"url": url, "pid": pid, "programme": progs[0], "programme_sha256": attendu, "port": m.group(1),
            "max_appels": MAX_APPELS_RELAIS, "amont": amont, "version": etat.get("version")}


def extraire_techniques(objet) -> dict:
    """Les seuls champs techniques de la dernière ligne de la commande ; le texte n'est jamais gardé (présence et longueur)."""
    if not isinstance(objet, dict):
        return {"ligne_lisible": False}
    out = {k: objet.get(k) for k in CHAMPS_TECHNIQUES if k in objet}
    texte = objet.get("texte")
    out["ligne_lisible"] = True
    out["reponse_non_vide"] = isinstance(texte, str) and bool(texte.strip())
    out["texte_longueur_caracteres"] = len(texte) if isinstance(texte, str) else None
    out["avertissements_nombre"] = len(objet.get("avertissements") or []) if isinstance(objet.get("avertissements"), list) else None
    e = objet.get("erreur")
    out["erreur_type"] = (str(e).split(" : ", 1)[0][:60] if e else None)     # le nom de l'erreur seul, jamais son message
    usage = out.get("usage")
    if isinstance(usage, dict):
        out["candidats_jetons"] = usage.get("candidats")
    return out


def appeler(commande: list, entree: bytes, env: dict, cwd: str, delai_s: float) -> tuple:
    """Lance la commande dans sa propre session de processus ; rend (code de sortie, sortie standard en octets, durée, délai
    dépassé). La sortie d'erreur est jetée."""
    debut = time.monotonic()
    p = subprocess.Popen(commande, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, cwd=cwd, env=env,
                         start_new_session=True)
    try:
        sortie, _ = p.communicate(input=entree, timeout=delai_s)
        depasse = False
    except subprocess.TimeoutExpired:
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except OSError:
            pass
        sortie, _ = p.communicate()
        depasse = True
    return p.returncode, sortie, round(time.monotonic() - debut, 3), depasse


def sonder(L, r, go_id: str, pid: int, sortie: Path, *, commande: list | None = None, url_relais: str = URL_RELAIS,
           lire_etat=lire_etat_local, lire_cmd=lire_cmdline, aujourd_hui: _dt.date | None = None, horodatage=date_u,
           environ=None, amont: str | None = None, delai_s: float = DELAI_S) -> int:
    """La sonde ; `commande` (essais seulement) remplace l'enveloppe lancée, jamais les contrôles faits sur l'enveloppe épinglée."""
    environ = os.environ if environ is None else environ
    presents = sorted(n for n in environ if n in L.NOMS_DE_CLE or L.MOTIF_NOM_DE_CLE.search(n))
    if presents:
        raise Refus(f"variables de clé dans l'environnement de la sonde ({presents}) : la clé reste dans son relais")
    if sortie.exists() or Path(str(sortie) + ".sha256").exists():
        raise Refus(f"{sortie} existe déjà (R12)")
    aujourd_hui = aujourd_hui or _dt.datetime.now(_dt.timezone.utc).date()
    try:
        pieces = L.verifier_pieces(r)
        if pieces["sonde_carbon"]["sha256"] != sha256_fichier(Path(__file__)):
            raise Refus("ce programme n'est pas celui que le lanceur v7 épingle")
        registre = L.lire_registre(r)
        go = L.verifier_go(registre["texte"], aujourd_hui, go_id, PLAFOND_USD, MOTS_GO)
        reglage = L.controler_reglage_carbon({"commande": ["bash", pieces["enveloppe_carbon"]["absolu"]],
                                              "modele_propose": L.MODELE_CARBON}, pieces, None)
        matiere = L.verifier_matiere(r)
        lots = L.decouper_matiere(matiere["octets"], matiere["sha256"])
        entree = L.plus_grande_entree(Path(pieces["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8"), lots)
        pire = L.pire_cas_carbon(reglage, entree, PLAFOND_USD)
    except L.Refus as e:
        raise Refus(str(e)) from None
    amont = amont or L.AMONT_GEMINI
    try:
        etat = lire_etat(url_relais)
    except Exception as e:  # noqa: BLE001 — tout échec de lecture est un refus nommé
        raise Refus(f"état du relais jeté illisible ({type(e).__name__})") from None
    try:
        cmdline = lire_cmd(pid)
    except OSError:
        raise Refus(f"relais jeté : PID {pid} absent") from None
    relais = controler_relais(L, r.programmes_relais or L.PROGRAMMES_RELAIS, url_relais, pid, etat, cmdline, amont)
    commande = list(commande) if commande else ["bash", pieces["enveloppe_carbon"]["absolu"]]
    maison = tempfile.mkdtemp(prefix="sonde-carbon-")
    env = {"PATH": environ.get("PATH", "/usr/local/bin:/usr/bin:/bin"), "LANG": "C.UTF-8", "HOME": maison,
           "PLAFOND_SESSION_USD": repr(float(PLAFOND_USD)), "ROLE_POLE": "proposeur_ideation",
           "MODELE_DEMANDE_POLE": L.MODELE_CARBON}
    debut_utc = horodatage()
    code_sortie, brut, duree, depasse = appeler(commande, entree["texte"].encode("utf-8"), env, maison, delai_s)
    lignes = [x for x in brut.decode("utf-8", "replace").splitlines() if x.strip()]
    try:
        objet = json.loads(lignes[-1]) if lignes else None
    except ValueError:
        objet = None
    del brut, lignes                                       # le texte rendu n'est gardé nulle part
    tech = extraire_techniques(objet)
    del objet
    tech.update(code_sortie=code_sortie, duree_s=duree, delai_depasse=depasse)
    tech["non_tronquee"] = tech.get("fin") == "STOP" and tech.get("max_sortie_jetons") == reglage["valeurs"]["--max-sortie-jetons"]
    try:
        apres = lire_etat(url_relais)
    except Exception as e:  # noqa: BLE001
        apres = {"illisible": type(e).__name__}
    motifs = []
    if code_sortie != 0 or tech.get("code") != 0:
        motifs.append(f"code de sortie {code_sortie}, code de la commande {tech.get('code')!r} (0 exigé)")
    if tech.get("fin") != "STOP":
        motifs.append(f"finishReason {tech.get('fin')!r} (STOP exigé)")
    if tech.get("reponse_non_vide") is not True:
        motifs.append("réponse vide ou absente")
    if tech["non_tronquee"] is not True:
        motifs.append(f"réponse tronquée ou sortie demandée réduite (fin {tech.get('fin')!r}, sortie demandée "
                      f"{tech.get('max_sortie_jetons')!r}, maximum {reglage['valeurs']['--max-sortie-jetons']})")
    servi = tech.get("modele_servi")
    if not (isinstance(servi, str) and L.MODELE_SERVI_CARBON_ADMIS.match(servi)):
        motifs.append(f"modèle servi {servi!r} non admis par l'orchestrateur")
    cout = tech.get("cout_usd")
    if not (isinstance(cout, (int, float)) and not isinstance(cout, bool) and 0 < cout <= PLAFOND_USD + 1e-9):
        motifs.append(f"coût {cout!r} hors de ]0 ; {PLAFOND_USD}]")
    if apres.get("appels") != MAX_APPELS_RELAIS or apres.get("refus") not in (0, None):
        motifs.append(f"relais après la sonde : appels {apres.get('appels')!r}, refus {apres.get('refus')!r} "
                      f"({MAX_APPELS_RELAIS} et 0 exigés)")
    ok = not motifs
    rapport = {"version": VERSION, "horodatage_utc": debut_utc, "jour": debut_utc[:10], "ok": ok, "motif": motifs or None,
               "appel_envoye": tech.get("envoye") is True or (isinstance(apres.get("appels"), int) and apres["appels"] >= 1),
               "plafond_session_usd": PLAFOND_USD, "go": go, "registre": {"commit": registre["commit"], "sha256": registre["sha256"]},
               "commande": tech, "entree": {k: entree[k] for k in ("rang", "nom", "octets", "caracteres", "sha256")},
               "reglage": reglage["valeurs"], "drapeaux": reglage["drapeaux"], "pire_cas": pire,
               "empreintes": {"programme": pieces["sonde_carbon"]["sha256"], "enveloppe": pieces["enveloppe_carbon"]["sha256"],
                              "commande_argon": pieces["commande_argon"]["sha256"], "relais": relais["programme_sha256"],
                              "lanceur_v7": sha256_fichier(LANCEUR) if LANCEUR.is_file() else None},
               "relais_jete": relais, "etat_relais_apres": {k: apres.get(k) for k in ("appels", "refus", "reponses_par_statut",
                                                                                     "illisible")},
               "matiere": {"chemin": matiere["chemin"], "sha256": matiere["sha256"], "commit": matiere["commit"]},
               "garde": "jamais le texte rendu (présence et longueur seulement), jamais une clé, jamais la sortie d'erreur",
               "fondement": "mots de Lazar « go (a) », « augmente le plafond », « enlève la troncature pour Carbon » ; additif v2g",
               "signale": f"appel réel, au plus {PLAFOND_USD} USD, sur la ligne {go_id}"}
    ecrire_scelle(sortie, rapport)
    return 0 if ok else 1


def principal(argv: list | None = None) -> int:
    a = argparse.ArgumentParser(prog="sonde_carbon_synchrone_v1", description=__doc__.splitlines()[0], allow_abbrev=False)
    a.add_argument("--go", required=True)
    a.add_argument("--pid-relais", type=int, required=True)
    a.add_argument("--sortie", required=True)
    try:
        args = a.parse_args(argv)
    except SystemExit:
        return 2
    sortie = Path(args.sortie)
    sortie = sortie if sortie.is_absolute() else DEPOT / sortie
    try:
        L = charger_lanceur()
        code = sonder(L, L.Reglages.production(), args.go, args.pid_relais, sortie)
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    o = json.loads(sortie.read_text(encoding="utf-8"))
    c = o["commande"]
    print(json.dumps({"sonde": str(sortie), "ok": o["ok"], "code": c.get("code"), "fin": c.get("fin"),
                      "modele_servi": c.get("modele_servi"), "cout_usd": c.get("cout_usd"), "pensees_jetons": c.get("pensees_jetons"),
                      "candidats_jetons": c.get("candidats_jetons"), "duree_s": c.get("duree_s"), "motif": o.get("motif")},
                     ensure_ascii=False))
    return code


if __name__ == "__main__":
    raise SystemExit(principal())
