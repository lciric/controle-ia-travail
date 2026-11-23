"""Transfert des activations de la relecture du barreau 5 vers un volume de stockage de 200 Go (Hetzner, Helsinki) — v1.

Pièce de classe B, écrite le 22 novembre 2026 par un rédacteur neuf (Opus 5.5), sous-agent du conducteur de la lecture du
barreau 5, sous l'accord GO-2026-11-22-117 (part « garder les activations », 24 USD au plus). Procédure :
`../procedure-transfert-activations-b5f-v1.md`. Ce programme ne crée, n'arrête ni ne détruit rien, et n'atteint aucun
réseau : il contrôle, calcule et IMPRIME. Les commandes imprimées citent les clés par leur nom seul (`$HCLOUD_TOKEN`,
`$VAST_API_KEY`) ; aucune valeur de clé n'est lue ici.

Bibliothèque standard seulement, sauf `selection une_sur_dix` (numpy, importé à la demande) : la sous-commande
`verifier-copie` doit tourner telle quelle sur le serveur de transfert (`python3 -I`).

Sous-commandes (codes : 0 accepté ; 2 refus, motif sur la sortie d'erreur ; 3 coupure de dépense ou délai dépassé) :
  accord REGISTRE_GO.md AAAA-MM-JJ
  preuve-inventaire RACINE COMMIT RUN_ID SORTIE.json
  verifier-copie INVENTAIRE.json DOSSIER CONSTAT.json [SELECTION.txt]
  selection REGLE INVENTAIRE.json SORTIE.txt [MANIFESTE.json]        (REGLE : couche_15 ou une_sur_dix)
  corps-volume | corps-serveur TYPE VOLUME_ID CLE_SSH_ID PARE_FEU_ID | corps-cle-ssh FICHIER.pub | corps-pare-feu IPV4
  protection-volume VOLUME_ID | supprimer ssh_keys|firewalls ID | lister servers|volumes|ssh_keys|firewalls
  reduire-liste GENRE BRUT.json SORTIE.json                            (GENRE : hetzner-serveurs, hetzner-volumes, vast)
  detruire-serveur LISTE.json ID
  detruire-vast LISTE.json ID PREUVE.json CONSTAT.json [--repli SELECTION.txt FIN_RELECTURE_UTC MAINTENANT_UTC]
  verifier-absence LISTE.json ID TEMOIN
  garde-depense ETAT.json
  echeance-vast FIN_RELECTURE_UTC MAINTENANT_UTC
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ACCORD = "GO-2026-11-22-117"
BRANCHE_LECTURE = "donnees/barreau5-familles-jumelles-v1-lecture"
ETIQUETTE_VAST = "b5f-lecture-v1"
NOM_VOLUME = "b5f-activations-v1"
NOM_SERVEUR = "b5f-transfert-v1"
LIEU = "hel1"
IMAGE = "ubuntu-24.04"
TYPES_SERVEUR = ("cx23", "ccx13")
TAILLE_VOLUME_GO = 200
# Prix du devis v2 (`devis-garde-activations-volume-v2.md`, 8112974b…, § 2), relevés le 21 novembre 2026 : EUR hors taxe
PRIX_VOLUME_EUR_GO_MOIS = 0.0572
PRIX_SERVEUR_EUR_H = {"cx23": 0.0088, "ccx13": 0.0585}
PRIX_IPV4_EUR_H = 0.0008
TAXE = 1.20
TAUX_USD_EUR = 1.25          # convention du registre des dépenses (registres/depenses.md, l. 422)
PLAFOND_PART_VOLUME_USD = 24.0
MINUTERIE_MAX_H = 24
DELAI_VAST_ARRETEE_H = 72
PRIX_VAST_ARRETEE_USD_H = 0.12   # ordre de grandeur donné par la mère (stockage de 300 Go à l'arrêt) ; à relever
LABELS = {"programme": "controle-ia", "barreau": "b5f", "accord": ACCORD}

_RUN = re.compile(r"^[0-9]{8}-[0-9]{6}-b5f-lecture$")
_ACT = re.compile(r"^activations/[A-Za-z0-9_-]+/c(7|15|23)/[A-Za-z0-9._-]+__p[0-9]{1,3}\.npy$")
_HEX64 = re.compile(r"^[0-9a-f]{64}$")


class Refus(Exception):
    """Refus d'une garde : code 2, motif sur la sortie d'erreur."""


class Coupure(Exception):
    """Coupure de dépense ou délai dépassé : code 3."""


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_fichier(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloc in iter(lambda: f.read(8 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def instant(s: str) -> datetime:
    """AAAA-MM-JJTHH:MM:SSZ (UTC) seulement."""
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", str(s)):
        raise Refus(f"instant {s!r} : AAAA-MM-JJTHH:MM:SSZ attendu")
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


# --- accord ------------------------------------------------------------------------------------------------------------

def exiger_accord(registre_go: str, jour: str, accord: str = ACCORD) -> dict:
    """La ligne de l'accord existe une seule fois, de type « calcul », accordée par Lazar, et `jour` tombe dans sa période.
    (La garde de calcul du dépôt ne lit que les numéros à deux chiffres : celle-ci lit l'accord à trois chiffres.)"""
    lignes = [l for l in registre_go.splitlines() if l.startswith(f"| {accord} |")]
    if len(lignes) != 1:
        raise Refus(f"{accord} : {len(lignes)} ligne(s) au registre des accords, une attendue")
    c = [x.strip() for x in lignes[0].strip().strip("|").split("|")]
    if len(c) != 8:
        raise Refus(f"{accord} : ligne à {len(c)} colonnes, huit attendues")
    if c[2] != "calcul" or c[6] != "Lazar":
        raise Refus(f"{accord} : type {c[2]!r} ou accordant {c[6]!r} : « calcul » et « Lazar » attendus")
    j = date.fromisoformat(jour)
    if not (date.fromisoformat(c[1]) <= j <= date.fromisoformat(c[5])):
        raise Refus(f"{accord} hors de sa période ({c[1]} → {c[5]}) le {jour}")
    return {"accord": accord, "accorde": c[1], "echeance": c[5], "plafond": c[4]}


# --- preuve de l'inventaire ----------------------------------------------------------------------------------------------

def _git_show(racine: Path, commit: str, chemin: str) -> bytes:
    r = subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{chemin}"], capture_output=True)
    if r.returncode != 0:
        raise Refus(f"{chemin} absent du commit {commit[:12]}")
    return r.stdout


def lire_inventaire(octets: bytes) -> list[dict]:
    """Forme écrite par `relecture_v1.garde_des_activations` (commit c76e79169) : {"fichiers": [{chemin, octets, sha256}]},
    chemins relatifs à `donnees/<marche>/`."""
    try:
        x = json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise Refus("inventaire des activations illisible") from None
    if not isinstance(x, dict) or set(x) != {"fichiers"} or not isinstance(x["fichiers"], list) or not x["fichiers"]:
        raise Refus("inventaire des activations : {\"fichiers\": [...]} non vide attendu")
    vus = set()
    for f in x["fichiers"]:
        if not (isinstance(f, dict) and set(f) == {"chemin", "octets", "sha256"}):
            raise Refus("inventaire : entrée {chemin, octets, sha256} attendue")
        if not isinstance(f["chemin"], str) or _ACT.fullmatch(f["chemin"]) is None:
            raise Refus("inventaire : chemin hors de la forme des activations (nom non affiché)")
        if f["chemin"] in vus:
            raise Refus("inventaire : chemin en double")
        vus.add(f["chemin"])
        if not (isinstance(f["octets"], int) and not isinstance(f["octets"], bool) and f["octets"] > 0):
            raise Refus("inventaire : taille entière positive attendue")
        if not (isinstance(f["sha256"], str) and _HEX64.fullmatch(f["sha256"])):
            raise Refus("inventaire : empreinte sha256 attendue")
    return x["fichiers"]


def preuve_inventaire(racine: Path, commit: str, run_id: str) -> dict:
    """Lit, par `git show` et sans rien afficher, `donnees/<RUN>/inventaire-activations.json` au commit prouvé, et le
    prouve trois fois : (1) le commit est sur la branche distante de lecture ; (2) son compagnon `.sha256` concorde ;
    (3) l'inventaire final du même commit (`traces-b5f-lecture/inventaire-final.json`) le liste à sa taille et à son
    empreinte. Rend la forme normalisée (écrite par l'appelant), jamais imprimée."""
    if not re.fullmatch(r"[0-9a-f]{40}", str(commit)) or _RUN.fullmatch(str(run_id)) is None:
        raise Refus("commit (40 signes) et identifiant de marche AAAAMMJJ-HHMMSS-b5f-lecture attendus")
    r = subprocess.run(["git", "-C", str(racine), "branch", "-r", "--contains", commit], capture_output=True, text=True)
    if r.returncode != 0 or f"origin/{BRANCHE_LECTURE}" not in r.stdout.split():
        raise Refus(f"commit {commit[:12]} absent de la branche distante {BRANCHE_LECTURE}")
    chemin = f"donnees/{run_id}/inventaire-activations.json"
    octets = _git_show(racine, commit, chemin)
    h = sha256_octets(octets)
    comp = _git_show(racine, commit, chemin + ".sha256").decode("utf-8", "replace").split()
    if not comp or comp[0] != h:
        raise Refus("inventaire des activations : compagnon .sha256 discordant")
    final = json.loads(_git_show(racine, commit, "traces-b5f-lecture/inventaire-final.json").decode("utf-8"))
    entrees = [f for f in final.get("fichiers", []) if f.get("chemin") == chemin]
    if len(entrees) != 1 or entrees[0].get("sha256") != h or entrees[0].get("octets") != len(octets):
        raise Refus("inventaire des activations absent de l'inventaire final du commit, ou à une autre taille ou empreinte")
    fichiers = lire_inventaire(octets)
    return {"run_id": run_id, "commit": commit, "inventaire_sha256": h, "fichiers": fichiers,
            "total_octets": sum(f["octets"] for f in fichiers)}


# --- vérification de la copie (tourne sur le serveur de transfert) --------------------------------------------------

def verifier_copie(preuve: dict, dossier: Path, selection: list[str] | None = None) -> dict:
    """Chaque fichier attendu (tout l'inventaire, ou la sélection d'un repli) est sous `dossier`, fichier ordinaire, à sa
    taille et à son empreinte ; tout autre fichier sous `dossier` est « en trop ». Aucun contenu n'est lu au-delà de son
    empreinte ; le constat (chemin, statut) reste sur le volume et ne s'imprime pas."""
    par_chemin = {f["chemin"]: f for f in preuve["fichiers"]}
    attendus = sorted(par_chemin) if selection is None else sorted(selection)
    inconnus = [c for c in attendus if c not in par_chemin]
    if inconnus:
        raise Refus(f"sélection : {len(inconnus)} chemin(s) hors de l'inventaire prouvé")
    dossier = Path(dossier)
    statuts = {}
    for c in attendus:
        p = dossier / c
        if p.is_symlink():
            statuts[c] = "lien"
        elif not p.is_file():
            statuts[c] = "manquant"
        elif p.stat().st_size != par_chemin[c]["octets"]:
            statuts[c] = "taille"
        elif sha256_fichier(p) != par_chemin[c]["sha256"]:
            statuts[c] = "empreinte"
        else:
            statuts[c] = "conforme"
    trop = 0
    if dossier.is_dir():
        for p in dossier.rglob("*"):
            if (p.is_file() or p.is_symlink()) and p.relative_to(dossier).as_posix() not in statuts:
                trop += 1
    comptes = {k: sum(1 for v in statuts.values() if v == k) for k in ("conforme", "manquant", "taille", "empreinte", "lien")}
    complet = comptes["conforme"] == len(attendus) and trop == 0
    return {"run_id": preuve["run_id"], "commit": preuve["commit"], "inventaire_sha256": preuve["inventaire_sha256"],
            "portee": "inventaire" if selection is None else "selection",
            "selection_sha256": None if selection is None else sha256_octets("\n".join(attendus).encode("utf-8")),
            "attendus": len(attendus), "comptes": comptes, "en_trop": trop, "complet": complet,
            "statuts": statuts}


# --- sélections des replis -------------------------------------------------------------------------------------------

def selection(regle: str, preuve: dict, manifeste: dict | None = None) -> list[str]:
    """Replis du texte scellé (« Données gardées »), dans le même calcul que `relecture_v1.garde_des_activations`
    (commit c76e79169) : `couche_15` = couche 15 de toutes les séries ; `une_sur_dix` = une action sur dix, tirée par la
    graine `b5f/tirages/garde-activations` du manifeste de la marche, couche 15."""
    c15 = sorted(f["chemin"] for f in preuve["fichiers"] if "/c15/" in f["chemin"])
    if regle == "couche_15":
        return c15
    if regle != "une_sur_dix":
        raise Refus("règle : couche_15 ou une_sur_dix")
    if not isinstance(manifeste, dict) or "graines" not in manifeste:
        raise Refus("une_sur_dix : manifeste de la marche (graines) exigé")
    g = manifeste["graines"].get("b5f/tirages/garde-activations")
    if not isinstance(g, dict):
        raise Refus("une_sur_dix : graine b5f/tirages/garde-activations absente du manifeste")
    import numpy as np
    ss = np.random.SeedSequence(int(g["entropie"]), spawn_key=tuple(int(k) for k in g["spawn_key"]))
    if [int(x) for x in ss.generate_state(2)] != g["etat_controle"]:
        raise Refus("graine reconstruite ≠ graine consignée : numpy ou manifeste altéré")
    rng = np.random.default_rng(ss)
    noms = sorted({c.rsplit("/", 1)[1] for c in c15})
    choisies = {noms[int(i)] for i in rng.choice(len(noms), size=max(1, len(noms) // 10), replace=False)} if noms else set()
    return [c for c in c15 if c.rsplit("/", 1)[1] in choisies]


# --- corps des requêtes de création (aucune clé) ---------------------------------------------------------------------

def corps_volume() -> dict:
    return {"name": NOM_VOLUME, "size": TAILLE_VOLUME_GO, "location": LIEU, "format": "ext4",
            "labels": dict(LABELS, piece=NOM_VOLUME)}


def corps_serveur(type_serveur: str, volume_id: str, cle_ssh_id: str, pare_feu_id: str) -> dict:
    if type_serveur not in TYPES_SERVEUR:
        raise Refus(f"type de serveur {type_serveur!r} : {TYPES_SERVEUR} attendu (devis v2, § 2)")
    for nom, v in (("volume", volume_id), ("clé SSH", cle_ssh_id), ("pare-feu", pare_feu_id)):
        if not str(v).isdigit():
            raise Refus(f"identifiant de {nom} numérique attendu")
    return {"name": NOM_SERVEUR, "server_type": type_serveur, "image": IMAGE, "location": LIEU,
            "volumes": [int(volume_id)], "automount": True, "ssh_keys": [int(cle_ssh_id)],
            "firewalls": [{"firewall": int(pare_feu_id)}], "public_net": {"enable_ipv4": True, "enable_ipv6": True},
            "labels": dict(LABELS, piece=NOM_SERVEUR)}


def corps_cle_ssh(cle_publique: str) -> dict:
    """Clé SSH jetable du poste (partie publique seulement), supprimée par son identifiant en fin de séance."""
    c = cle_publique.strip()
    if re.fullmatch(r"ssh-ed25519 [A-Za-z0-9+/=]{60,80}( [A-Za-z0-9._@-]{0,64})?", c) is None:
        raise Refus("clé publique ssh-ed25519 attendue (jamais une clé privée)")
    return {"name": NOM_SERVEUR, "public_key": c, "labels": dict(LABELS, piece=NOM_SERVEUR)}


def corps_pare_feu(ipv4_du_poste: str) -> dict:
    """Entrée SSH (port 22) admise depuis la seule adresse du poste ; rien d'autre n'entre."""
    o = str(ipv4_du_poste).split(".")
    if len(o) != 4 or not all(x.isdigit() and 0 <= int(x) <= 255 and str(int(x)) == x for x in o) \
            or o[0] in ("0", "10", "127") or ipv4_du_poste == "255.255.255.255":
        raise Refus("adresse IPv4 publique du poste attendue")
    return {"name": NOM_SERVEUR, "labels": dict(LABELS, piece=NOM_SERVEUR),
            "rules": [{"direction": "in", "protocol": "tcp", "port": "22", "source_ips": [f"{ipv4_du_poste}/32"]}]}


# --- listes réduites, destructions, absence ---------------------------------------------------------------------------

CHAMPS = {"hetzner-serveurs": ("id", "name", "status", "labels", "server_type", "created"),
          "hetzner-volumes": ("id", "name", "status", "labels", "server", "size", "location", "protection"),
          "vast": ("id", "label", "actual_status", "cur_state", "intended_status", "dph_total", "storage_cost",
                   "inet_up_cost", "inet_down_cost", "start_date", "end_date")}


def reduire_liste(genre: str, brut) -> list[dict]:
    """Réduit une liste brute (qui peut porter des variables d'environnement, donc des clés) aux seuls champs utiles,
    sous leurs clés d'origine ; `server_type` et `location` réduits à leur nom."""
    if genre not in CHAMPS:
        raise Refus(f"genre {genre!r} : {tuple(CHAMPS)} attendu")
    if isinstance(brut, dict):
        cle = {"hetzner-serveurs": "servers", "hetzner-volumes": "volumes", "vast": "instances"}[genre]
        brut = brut.get(cle)
    if not isinstance(brut, list):
        raise Refus("liste brute illisible")
    sortie = []
    for x in brut:
        if not isinstance(x, dict):
            raise Refus("entrée de liste illisible")
        r = {}
        for k in CHAMPS[genre]:
            if k not in x:
                continue
            v = x[k]
            if k in ("server_type", "location") and isinstance(v, dict):
                v = v.get("name")
            r[k] = v
        sortie.append(r)
    return sortie


def _une(liste: list[dict], ident: str) -> dict:
    if not str(ident).isdigit():
        raise Refus("identifiant numérique attendu (R10)")
    t = [x for x in liste if str(x.get("id")) == str(ident)]
    if len(t) != 1:
        raise Refus(f"identifiant {ident} absent ou en double dans la liste")
    return t[0]


def commande_hetzner(methode: str, chemin: str, corps: dict | None = None) -> str:
    """Commande `curl` imprimée : le jeton passe par la configuration lue sur l'entrée standard (`-K -`), jamais dans
    les arguments ni à l'écran ; seul son nom est écrit."""
    c = (f"printf 'header = \"Authorization: Bearer %s\"\\n' \"$HCLOUD_TOKEN\" | curl -sS -m 60 -K - -X {methode} "
         f"-H 'Content-Type: application/json' https://api.hetzner.cloud/v1{chemin}")
    if corps is not None:
        c += f" -d '{json.dumps(corps, separators=(',', ':'), sort_keys=True)}'"
    return c


def commande_detruire_serveur(liste: list[dict], ident: str) -> str:
    x = _une(liste, ident)
    if x.get("name") != NOM_SERVEUR or (x.get("labels") or {}).get("piece") != NOM_SERVEUR \
            or (x.get("labels") or {}).get("accord") != ACCORD:
        raise Refus(f"serveur {ident} : nom ou étiquettes autres que ceux du transfert ({NOM_SERVEUR}, {ACCORD})")
    return commande_hetzner("DELETE", f"/servers/{ident}")


def commande_detruire_vast(liste: list[dict], ident: str, preuve: dict, constat: dict,
                           repli: tuple[list[str], str, str] | None = None) -> str:
    """Destruction de l'instance de relecture par son identifiant (R10), seulement après transfert prouvé : constat
    complet, du même inventaire prouvé (même commit, même empreinte), sur tout l'inventaire ; ou, en repli, sur la
    sélection donnée, et seulement une fois le délai de 72 heures atteint."""
    x = _une(liste, ident)
    if x.get("label") != ETIQUETTE_VAST:
        raise Refus(f"instance {ident} : étiquette autre que {ETIQUETTE_VAST}")
    if constat.get("commit") != preuve["commit"] or constat.get("inventaire_sha256") != preuve["inventaire_sha256"]:
        raise Refus("constat d'un autre inventaire ou d'un autre commit que la preuve")
    if constat.get("complet") is not True or constat.get("comptes", {}).get("conforme") != constat.get("attendus"):
        raise Refus("transfert non prouvé : constat incomplet (aucune destruction, « récupérer ce qui est récupérable »)")
    if repli is None:
        if constat.get("portee") != "inventaire" or constat.get("attendus") != len(preuve["fichiers"]):
            raise Refus("constat d'une sélection : destruction seulement en repli, après le délai")
    else:
        sel, fin, maintenant = repli
        if constat.get("portee") != "selection" \
                or constat.get("selection_sha256") != sha256_octets("\n".join(sorted(sel)).encode("utf-8")):
            raise Refus("repli : constat d'une autre sélection")
        if echeance_vast(fin, maintenant)["verdict"] != "depasse":
            raise Refus("repli : délai de 72 heures non atteint ; le transfert entier reste dû")
    return f"GO_ID={ACCORD} vastai destroy instance {ident} -y"


def verifier_absence(liste: list[dict], ident: str, temoin: str) -> str:
    """Une destruction ne se juge jamais par un code de sortie : identifiant absent de la liste neuve, témoin présent."""
    ids = {str(x.get("id")) for x in liste}
    if str(temoin) not in ids:
        raise Refus(f"témoin {temoin} absent : liste vide ou fausse, rien n'est prouvé")
    if str(ident) in ids:
        raise Refus(f"{ident} toujours présent")
    return f"absence de {ident} prouvée (témoin {temoin} présent)"


# --- dépense et délai --------------------------------------------------------------------------------------------------

def _eur_vers_usd(eur: float) -> float:
    return eur * TAUX_USD_EUR


def garde_depense(etat: dict) -> dict:
    """Part « volume » de GO-2026-11-22-117 : volume de sa création à l'échéance de garde (au plafond mensuel), serveurs
    de séance (heures écoulées, plus, pour un serveur vivant, les heures jusqu'à sa minuterie), adresses IPv4 ; et, si la
    mère les y compte, l'instance arrêtée et la sortie de données du loueur (`postes_vast`). Verdict « coupure » dès que le
    cumul projeté atteint le plafond ; `nouvelle_seance` éprouve une séance de plus à 24 heures."""
    creation = instant(etat["volume_cree"])
    fin = instant(etat["echeance_garde"])
    heures_volume = max(0.0, (fin - creation).total_seconds() / 3600)
    mois = TAILLE_VOLUME_GO * PRIX_VOLUME_EUR_GO_MOIS * TAXE
    # Prudent : chaque période de 30 jours entamée est comptée au plafond mensuel entier (devis v2 : 13,73 EUR par mois)
    volume_eur = mois * math.ceil(heures_volume / 720)
    seances = list(etat.get("seances", []))
    if len(seances) > 3:
        raise Coupure("plus de trois séances sous cette ligne (devis v2, § 3)")
    serveurs_eur = 0.0
    for s in seances:
        if s.get("type") not in TYPES_SERVEUR:
            raise Refus("séance : type de serveur inconnu")
        h = float(s["heures"])
        if h < 0 or h > MINUTERIE_MAX_H:
            raise Coupure(f"séance de {h} heures : au-delà de la minuterie de {MINUTERIE_MAX_H} heures")
        serveurs_eur += h * (PRIX_SERVEUR_EUR_H[s["type"]] + PRIX_IPV4_EUR_H) * TAXE
    vast_usd = float(etat.get("postes_vast", {}).get("usd", 0.0))
    cumul = _eur_vers_usd(volume_eur + serveurs_eur) + vast_usd
    plafond = float(etat.get("plafond_usd", PLAFOND_PART_VOLUME_USD))
    if plafond > PLAFOND_PART_VOLUME_USD:
        raise Refus(f"plafond {plafond} USD au-dessus de la part accordée ({PLAFOND_PART_VOLUME_USD})")
    sortie = {"volume_usd": round(_eur_vers_usd(volume_eur), 2), "serveurs_usd": round(_eur_vers_usd(serveurs_eur), 2),
              "vast_usd": round(vast_usd, 2), "cumul_projete_usd": round(cumul, 2), "plafond_usd": plafond,
              "verdict": "coupure" if cumul >= plafond else "sous le plafond"}
    if etat.get("nouvelle_seance"):
        t = etat["nouvelle_seance"]
        if t not in TYPES_SERVEUR:
            raise Refus("nouvelle séance : type de serveur inconnu")
        if len(seances) >= 3:
            sortie["nouvelle_seance"] = "refusée (trois séances déjà)"
        else:
            plus = _eur_vers_usd(MINUTERIE_MAX_H * (PRIX_SERVEUR_EUR_H[t] + PRIX_IPV4_EUR_H) * TAXE)
            sortie["nouvelle_seance"] = "admise" if cumul + plus < plafond else "refusée (plafond)"
    if sortie["verdict"] == "coupure":
        raise Coupure(json.dumps(sortie, ensure_ascii=False, sort_keys=True))
    return sortie


def echeance_vast(fin_relecture: str, maintenant: str, delai_h: int = DELAI_VAST_ARRETEE_H) -> dict:
    """Instance de relecture arrêtée et non détruite : au plus `delai_h` heures après la fin de la relecture ; au-delà,
    repli (verser ce que « une_sur_dix » aurait versé, puis détruire)."""
    h = (instant(maintenant) - instant(fin_relecture)).total_seconds() / 3600
    if h < 0:
        raise Refus("maintenant antérieur à la fin de la relecture")
    return {"heures_ecoulees": round(h, 2), "heures_restantes": round(max(0.0, delai_h - h), 2),
            "cout_estime_usd": round(h * PRIX_VAST_ARRETEE_USD_H, 2),
            "verdict": "depasse" if h >= delai_h else "dans le delai"}


# --- ligne de commande ---------------------------------------------------------------------------------------------------

def _lire_json(p: str):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def _ecrire_neuf(p: str, texte: str) -> None:
    q = Path(p)
    if q.exists():
        raise Refus(f"{p} existe déjà (R12 : on n'écrase jamais)")
    q.write_text(texte, encoding="utf-8")


def principal(a: list[str]) -> int:
    if not a:
        raise Refus("sous-commande attendue (voir l'en-tête du programme)")
    s, a = a[0], a[1:]
    if s == "accord" and len(a) == 2:
        print(json.dumps(exiger_accord(Path(a[0]).read_text(encoding="utf-8"), a[1]), ensure_ascii=False))
    elif s == "preuve-inventaire" and len(a) == 4:
        p = preuve_inventaire(Path(a[0]), a[1], a[2])
        _ecrire_neuf(a[3], json.dumps(p, sort_keys=True))
        print(f"inventaire prouvé : {len(p['fichiers'])} fichiers, {p['total_octets']} octets ; "
              f"inventaire sha256 {p['inventaire_sha256']} ; commit {p['commit']}")
    elif s == "verifier-copie" and len(a) in (3, 4):
        sel = Path(a[3]).read_text(encoding="utf-8").split() if len(a) == 4 else None
        c = verifier_copie(_lire_json(a[0]), Path(a[1]), sel)
        texte = json.dumps(c, sort_keys=True)
        _ecrire_neuf(a[2], texte)
        print(f"constat : portée {c['portee']}, attendus {c['attendus']}, {json.dumps(c['comptes'], sort_keys=True)}, "
              f"en trop {c['en_trop']}, complet {'oui' if c['complet'] else 'non'} ; "
              f"constat sha256 {sha256_octets(texte.encode('utf-8'))}")
        return 0 if c["complet"] else 3
    elif s == "selection" and len(a) in (3, 4):
        sel = selection(a[0], _lire_json(a[1]), _lire_json(a[3]) if len(a) == 4 else None)
        _ecrire_neuf(a[2], "\n".join(sel) + "\n")
        print(f"sélection {a[0]} : {len(sel)} fichiers ; sha256 {sha256_octets(chr(10).join(sorted(sel)).encode('utf-8'))}")
    elif s == "corps-volume" and not a:
        print(commande_hetzner("POST", "/volumes", corps_volume()))
    elif s == "corps-cle-ssh" and len(a) == 1:
        print(commande_hetzner("POST", "/ssh_keys", corps_cle_ssh(Path(a[0]).read_text(encoding="utf-8"))))
    elif s == "corps-pare-feu" and len(a) == 1:
        print(commande_hetzner("POST", "/firewalls", corps_pare_feu(a[0])))
    elif s == "protection-volume" and len(a) == 1 and a[0].isdigit():
        print(commande_hetzner("POST", f"/volumes/{a[0]}/actions/change_protection", {"delete": True}))
    elif s == "supprimer" and len(a) == 2 and a[0] in ("ssh_keys", "firewalls") and a[1].isdigit():
        print(commande_hetzner("DELETE", f"/{a[0]}/{a[1]}"))
    elif s == "lister" and len(a) == 1 and a[0] in ("servers", "volumes", "ssh_keys", "firewalls"):
        print(commande_hetzner("GET", f"/{a[0]}"))
    elif s == "corps-serveur" and len(a) == 4:
        print(commande_hetzner("POST", "/servers", corps_serveur(*a)))
    elif s == "reduire-liste" and len(a) == 3:
        _ecrire_neuf(a[2], json.dumps(reduire_liste(a[0], _lire_json(a[1])), sort_keys=True))
        print(f"liste réduite écrite : {a[2]}")
    elif s == "detruire-serveur" and len(a) == 2:
        print(commande_detruire_serveur(_lire_json(a[0]), a[1]))
    elif s == "detruire-vast" and len(a) in (4, 8) and (len(a) == 4 or a[4] == "--repli"):
        repli = None
        if len(a) == 8:
            repli = (Path(a[5]).read_text(encoding="utf-8").split(), a[6], a[7])
        print(commande_detruire_vast(_lire_json(a[0]), a[1], _lire_json(a[2]), _lire_json(a[3]), repli))
    elif s == "verifier-absence" and len(a) == 3:
        print(verifier_absence(_lire_json(a[0]), a[1], a[2]))
    elif s == "garde-depense" and len(a) == 1:
        print(json.dumps(garde_depense(_lire_json(a[0])), ensure_ascii=False, sort_keys=True))
    elif s == "echeance-vast" and len(a) == 2:
        e = echeance_vast(a[0], a[1])
        print(json.dumps(e, ensure_ascii=False, sort_keys=True))
        return 3 if e["verdict"] == "depasse" else 0
    else:
        raise Refus(f"sous-commande {s!r} ou nombre d'arguments inconnus")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(principal(sys.argv[1:]))
    except Refus as e:
        print(f"TRANSFERT REFUS : {e}", file=sys.stderr)
        sys.exit(2)
    except Coupure as e:
        print(f"TRANSFERT COUPURE : {e}", file=sys.stderr)
        sys.exit(3)
