#!/usr/bin/env python3
"""Outil de la session qui lance le crible (v) sur la machine louée — v1 (fichier neuf, R12). Modèles : l'outil de la session du
pilote MR-2 sans ssh (`session_pilote_mr2_v74_v4.sh`, `session_pilote_mr2_v74_v3.py`, branche `lot/compte-organisme-v1`, lus) et
la garde de la machine du jeu de l'idée 1.1 (`garde_machine_jeu_idee_1_1_v1.py`, lue). Procédure : `procedure-machine-crible-v-v1.md`
(même dossier). Bibliothèque standard, `git` et `openssl` seulement.

Côté session seulement : **aucune sous-commande ne crée, n'arrête ni ne détruit de machine, et aucune n'appelle le loueur** ; elles
contrôlent, lisent la branche de sortie (lecture seule), écrivent les feux de la mère sur la branche d'entrée et **impriment** les
commandes que l'opérateur joue (préfixe `GO_ID=` exigé par la garde de calcul ; destruction par l'identifiant, R10). Jamais une
valeur de clé n'est lue, écrite ni imprimée : les clés passent par leur **nom** dans la ligne imprimée.

Sous-commandes (code 0 : accepté ; 2 : refus, motif « CRIBLEV REFUS : … ») :
  offre-depuis-recherche RECHERCHE.json OFFRE.json     garde d'offre jouée sur chaque offre ; la moins chère acceptée écrite (mode x)
  offre OFFRE.json [ID]                                bornes de l'offre relues
  creation RACINE FEU COMMIT_CODE                      feu « R-<N> GO-… » (κv2) ; lignes κv1, κv2 citant GO-2026-11-15-06
  commande RACINE OFFRE.json COMMIT_CODE COMMIT_LOT ECHEANCE_UTC_S FEU DOSSIER BR_SORTIE BR_ENTREE
                                                       imprime la ligne de création (deux lignes ; amorce gzip + base64)
  controle-ligne COMMANDE_IMPRIMEE.txt                 amorce décodée égale à l'octet au fichier ; ligne imprimée, base64 masqué
  inventaire < LISTE.json                              « <id> <étiquette> » seulement, trié
  prix-relu PRIX                                       prix relu ≤ 0,17 USD/h, sinon destruction aussitôt
  depense RACINE GO_KV2 CUMUL PRIX                     cumul + une heure ≥ part machine (3 USD) → refus, destruction
  detruire ID DOSSIER GO_KV2                           imprime la destruction par l'identifiant (ID = DOSSIER/id-machine.txt)
  absence ID TEMOIN LISTE.json                         destruction prouvée (absence de ID, témoin présent ; jamais un code)
  etat RACINE BR_SORTIE                                état et fin du journal de la machine (lecture seule)
  feu-phrase RACINE BR_SORTIE BR_ENTREE PHRASE COMMIT_INSCRIPTION CHEMIN_INSCRIPTION
  feu-mondes RACINE BR_SORTIE BR_ENTREE COMMIT_INSCRIPTION CHEMIN_INSCRIPTION
  feu-reel RACINE BR_SORTIE BR_ENTREE GO_KV1 GO_KV2 D_S M COMMIT_INSCRIPTION CHEMIN_INSCRIPTION
  feu-arret RACINE BR_ENTREE CAUSE
  recuperer RACINE BR_SORTIE DOSSIER_NEUF              copie hors dépôt du sommet de la branche de sortie
"""
from __future__ import annotations

import base64
import gzip
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import date, datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
AMORCE = ICI / "amorce_crible_v_v1.sh"
ETIQUETTE = "crible-v-v1"
IMAGE = "python:3.13-bookworm"
DISQUE_GO = 20
DUREE_S = 61200                      # minuterie : 17 h après l'impression (budget de pire cas de la section « Devis »)
ECART_ECHEANCE_S = 300
PRIX_OFFRE_MAX = 0.15                # prix garde de l'offre (prix total + stockage)
PRIX_RELU_MAX = 0.17                 # 17 h × 0,17 = 2,89 USD, sous la part machine de 3 USD
PART_MACHINE = 3.0
HEURES_PAR_MOIS = 720.0
OFFRE_MIN = {"coeurs": 4, "memoire_vive_mo": 8000, "disque_go": 20, "fiabilite": 0.98, "debit_mbps": 100}
CLES_RECHERCHE = ("id", "num_gpus", "cpu_arch", "cpu_cores_effective", "cpu_ram", "disk_space", "dph_total", "storage_cost",
                  "inet_down")
INTOUCHABLES = ("58936096", "58936099", "58936100", "60480302", "60599797", "60670453", "60860420", "60918148", "60952525",
                "60953606")
ENVELOPPE = "GO-2026-11-15-06"
ENVELOPPE_USD = 1275.0
KAPPA = {"kv1": (104.39, ("crible (v)", "crédits de Claude")), "kv2": (100.28, ("crible", "hors crédits"))}
CLES_PAR_NOM = ("GH_TOKEN", "RR_ANTHROPIC_API_KEY_RIGAUD", "GEMINI_API_KEY", "OPENAI_API_KEY")
FICHIERS_CODE = ("docs/procedures/crible-v-v1/crible_v_commun_v1.py", "docs/procedures/crible-v-v1/lanceur_crible_v_v1.py",
                 "docs/procedures/crible-v-v1/mesure_crible_v_v1.py", "docs/procedures/crible-v-v1/lire_crible_v_v1.py",
                 "docs/procedures/crible-v-v1/machine_crible_v_v1.py")
BUNDLE = ("docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/"
          "arbre-organisme-complet-605e0f6.bundle")
SHA_BUNDLE = "e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1"
FEU = re.compile(r"R-([1-9][0-9]*) (GO-\d{4}-\d{2}-\d{2}-\d{2})", re.ASCII)
GO_ID = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", re.ASCII)
LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
PLAFOND = re.compile(r"([0-9]+(?:\.[0-9]+)?) USD", re.ASCII)
HEX40, HEX64, ENTIER = re.compile(r"[0-9a-f]{40}"), re.compile(r"[0-9a-f]{64}"), re.compile(r"[1-9][0-9]*")
BRANCHE_S = re.compile(r"calcul/crible-v-v1-sortie-v[1-9][0-9]*")
BRANCHE_E = re.compile(r"calcul/crible-v-v1-entree-v[1-9][0-9]*")
CAUSE = re.compile(r"[A-Za-z0-9 ,.:;()_-]{1,100}")
V = os.environ.get("VASTAI_CRIBLE", "/home/user/vastai-env/bin/vastai")


class Refus(Exception):
    pass


def _nombre(x):
    if isinstance(x, bool) or not isinstance(x, (int, float, str)):
        return None
    try:
        v = float(x)
    except (ValueError, OverflowError):
        return None
    return v if math.isfinite(v) else None


def git(racine, *a, entree=None):
    r = subprocess.run(["git", "-C", str(racine), *a], capture_output=True, text=entree is None or isinstance(entree, str),
                       input=entree)
    return r.returncode, r.stdout, r.stderr


# --- offre --------------------------------------------------------------------------------------------------------------------

def _fiabilite(o):
    v = [_nombre(o.get(k)) for k in ("reliability2", "reliability") if k in o]
    v = [x for x in v if x is not None]
    return min(v) if v else None


def fautes_offre(o):
    manque = [k for k in CLES_RECHERCHE if k not in o or (k == "cpu_arch" and not isinstance(o.get(k), str))
              or (k != "cpu_arch" and _nombre(o.get(k)) is None)]
    if _fiabilite(o) is None:
        manque.append("reliability2|reliability")
    if manque:
        return [f"clé(s) {manque} absente(s) ou illisible(s) ; rien n'est deviné"]
    f = []
    ng = o["num_gpus"]
    if isinstance(ng, bool) or not isinstance(ng, int) or ng < 0:
        f.append(f"num_gpus {ng!r} : entier ≥ 0 (avec ou sans carte, la carte inutilisée)")
    if o["cpu_arch"] != "amd64":
        f.append(f"processeur {o['cpu_arch']!r} : amd64 exigé")
    for cle, borne, quoi in (("cpu_cores_effective", "coeurs", "cœurs"), ("cpu_ram", "memoire_vive_mo", "mémoire (Mo)"),
                             ("disk_space", "disque_go", "disque (Go)"), ("inet_down", "debit_mbps", "débit descendant")):
        if _nombre(o[cle]) < OFFRE_MIN[borne]:
            f.append(f"{quoi} {o[cle]!r} < {OFFRE_MIN[borne]}")
    if _fiabilite(o) < OFFRE_MIN["fiabilite"]:
        f.append(f"fiabilité {_fiabilite(o)!r} < {OFFRE_MIN['fiabilite']}")
    if "rentable" in o and o["rentable"] is not True:
        f.append("offre non louable")
    st = _nombre(o["storage_cost"]) * DISQUE_GO / HEURES_PAR_MOIS
    prix = _nombre(o["dph_total"]) + st
    if not (_nombre(o["dph_total"]) > 0 and prix <= PRIX_OFFRE_MAX):
        f.append(f"prix garde {prix:.4f} USD/h hors de ]0 ; {PRIX_OFFRE_MAX}]")
    return f


def offre_construite(o):
    st = _nombre(o["storage_cost"]) * DISQUE_GO / HEURES_PAR_MOIS
    return {"id": int(o["id"]), "num_gpus": o["num_gpus"], "cpu_arch": o["cpu_arch"], "cpu_name": str(o.get("cpu_name", ""))[:80],
            "coeurs": _nombre(o["cpu_cores_effective"]), "memoire_vive_mo": _nombre(o["cpu_ram"]), "disque_go": _nombre(o["disk_space"]),
            "fiabilite": _fiabilite(o), "debit_mbps": _nombre(o["inet_down"]), "prix_total_usd_h": _nombre(o["dph_total"]),
            "stockage_usd_h": st, "prix_garde_usd_h": _nombre(o["dph_total"]) + st, "etiquette": ETIQUETTE,
            "inet_down_cost": o.get("inet_down_cost"), "inet_up_cost": o.get("inet_up_cost")}


def exiger_offre(offre, ident=None):
    f = []
    if ident is not None and str(offre.get("id")) != str(ident):
        f.append("identifiant de l'offre ≠ offre demandée")
    if offre.get("etiquette") != ETIQUETTE:
        f.append("étiquette")
    brute = {"id": offre.get("id"), "num_gpus": offre.get("num_gpus"), "cpu_arch": offre.get("cpu_arch"),
             "cpu_cores_effective": offre.get("coeurs"), "cpu_ram": offre.get("memoire_vive_mo"), "disk_space": offre.get("disque_go"),
             "dph_total": offre.get("prix_total_usd_h"), "inet_down": offre.get("debit_mbps"), "reliability": offre.get("fiabilite"),
             "storage_cost": (_nombre(offre.get("stockage_usd_h")) or float("nan")) * HEURES_PAR_MOIS / DISQUE_GO}
    f += fautes_offre(brute)
    if f:
        raise Refus("offre hors des bornes : " + " ; ".join(f))
    return offre


def offre_depuis_recherche(doc):
    liste = doc.get("offers") if isinstance(doc, dict) else doc
    if not isinstance(liste, list) or not liste:
        raise Refus("sortie de la recherche illisible ou vide")
    ok, journal = [], []
    for o in liste:
        if not isinstance(o, dict) or isinstance(o.get("id"), bool) or not ENTIER.fullmatch(str(o.get("id"))):
            journal.append("offre illisible")
            continue
        fautes = fautes_offre(o)
        journal.append(f"offre {o['id']} : " + ("acceptée" if not fautes else "refusée : " + " ; ".join(fautes)))
        if not fautes:
            ok.append(offre_construite(o))
    if not ok:
        raise Refus("aucune offre acceptée :\n  " + "\n  ".join(journal))
    ok.sort(key=lambda x: (x["prix_garde_usd_h"], x["id"]))
    return ok[0], journal


# --- registre des GO, feu, création ---------------------------------------------------------------------------------------------

def lire_go(chemin):
    go = {}
    for n, ligne in enumerate(Path(chemin).read_text(encoding="utf-8").splitlines(), 1):
        if not LIGNE_GO.match(ligne):
            continue
        c = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if len(c) != 8:
            raise Refus(f"registre des GO mal formé ligne {n}")
        ident, accorde, typ, perimetre, plafond, echeance, par, ref = c
        try:
            a = date.fromisoformat(accorde)
            e = None if (echeance == "—" and typ != "calcul") else date.fromisoformat(echeance)
        except ValueError:
            raise Refus(f"registre des GO mal formé ligne {n} : dates") from None
        if ident in go:
            if perimetre.lower().startswith("extension") and typ == go[ident]["type"] and par == "Lazar":
                continue
            raise Refus(f"registre des GO : {ident} en double")
        go[ident] = {"accorde": a, "type": typ, "perimetre": perimetre, "plafond": plafond, "echeance": e, "par": par, "ref": ref}
    return go


def exiger_kappa(go, ident, ligne, jour):
    """Ligne « calcul » κv1 ou κv2 : accordée par Lazar, dans sa période, non révoquée, au montant exact, périmètre aux mots de la
    ligne proposée, **citant GO-2026-11-15-06** (ligne d'arrêt « toute dépense sans ligne « calcul » inscrite citant
    GO-2026-11-15-06 : interdit »)."""
    g = go.get(ident)
    montant, mots = KAPPA[ligne]
    if g is None:
        raise Refus(f"{ident} ({ligne}) absent de registres/go.md : aucune dépense")
    if g["type"] != "calcul" or g["par"] != "Lazar":
        raise Refus(f"{ident} : type « calcul » accordé par Lazar exigé")
    if not (g["accorde"] <= jour <= g["echeance"]):
        raise Refus(f"{ident} hors de sa période ({g['accorde']} → {g['echeance']})")
    if any(r["type"] == "révocation" and (ident in r["perimetre"] or ident in r["ref"]) for r in go.values()):
        raise Refus(f"{ident} révoqué")
    m = PLAFOND.fullmatch(g["plafond"])
    if not m or abs(float(m.group(1)) - montant) > 1e-9:
        raise Refus(f"{ident} : plafond {g['plafond']!r} ≠ {montant:.2f} USD ({ligne})")
    manque = [x for x in mots if x not in g["perimetre"]]
    if manque:
        raise Refus(f"{ident} : périmètre sans {manque}")
    if ENVELOPPE not in g["ref"] and ENVELOPPE not in g["perimetre"]:
        raise Refus(f"{ident} ne cite pas {ENVELOPPE} : toute dépense est interdite")
    return float(m.group(1))


def exiger_enveloppe(go):
    """Les lignes inscrites sous GO-2026-11-15-06 (elles comprises) restent sous 1 275 USD ; sinon nœud de Lazar."""
    total = 0.0
    for g in go.values():
        if g["type"] == "calcul" and ENVELOPPE in (g["ref"] + " " + g["perimetre"]):
            m = PLAFOND.fullmatch(g["plafond"])
            if not m:
                raise Refus("ligne sous l'enveloppe au plafond illisible")
            total += float(m.group(1))
    if total > ENVELOPPE_USD + 1e-9:
        raise Refus(f"lignes sous {ENVELOPPE} : {total:.2f} USD > {ENVELOPPE_USD:.0f} USD : nœud de Lazar")
    return total


def exiger_creation(racine, feu, commit_code, maintenant):
    m = FEU.fullmatch(feu or "")
    if not m:
        raise Refus("feu : forme courte « R-<N> GO-AAAA-MM-JJ-NN » exactement (GO de κv2, part machine)")
    r, kv2 = m.group(1), m.group(2)
    if not HEX40.fullmatch(commit_code or ""):
        raise Refus("COMMIT_CODE : 40 caractères hexadécimaux")
    lignes = [x for x in (Path(racine) / "registres" / "decisions.md").read_text(encoding="utf-8").splitlines()
              if x.startswith(f"| R-{r} |")]
    if len(lignes) != 1:
        raise Refus(f"ligne R-{r} du feu : {len(lignes)} trouvée(s), une attendue")
    ids = GO_ID.findall(lignes[0])
    kv1 = [i for i in ids if i not in (kv2, ENVELOPPE)]
    if kv2 not in ids or len(set(kv1)) != 1:
        raise Refus(f"ligne R-{r} : elle cite κv2 ({kv2}) et une seule autre ligne de GO (κv1), hors {ENVELOPPE}")
    manque = [x for x in (commit_code, ETIQUETTE) if x not in lignes[0]]
    if manque:
        raise Refus(f"ligne R-{r} du feu : ne cite pas {manque}")
    jour = datetime.fromtimestamp(int(maintenant), tz=timezone.utc).date()
    go = lire_go(Path(racine) / "registres" / "go.md")
    exiger_kappa(go, kv1[0], "kv1", jour)
    exiger_kappa(go, kv2, "kv2", jour)
    total = exiger_enveloppe(go)
    return {"feu": f"R-{r}", "kv1": kv1[0], "kv2": kv2, "enveloppe_inscrite_usd": round(total, 2)}


def exiger_commits(racine, commit_code, commit_lot, branches):
    """COMMIT_CODE ancêtre de la tête distante de main et portant le code du crible (fichiers égaux à leurs compagnons) ;
    COMMIT_LOT portant le paquet de l'arbre à son empreinte ; branches de sortie et d'entrée absentes du dépôt distant."""
    for c in (commit_code, commit_lot):
        if not HEX40.fullmatch(c or ""):
            raise Refus("commit : 40 caractères hexadécimaux")
        if git(racine, "cat-file", "-e", c + "^{commit}")[0] != 0:
            raise Refus(f"commit {c[:12]} absent du dépôt local")
    code, sortie, _ = git(racine, "ls-remote", "origin", "refs/heads/main")
    tete = sortie.split("\t")[0] if code == 0 else ""
    if not HEX40.fullmatch(tete) or git(racine, "cat-file", "-e", tete + "^{commit}")[0] != 0:
        raise Refus("tête distante de main illisible ou absente du dépôt local (git fetch avec refspec d'abord)")
    if git(racine, "merge-base", "--is-ancestor", commit_code, tete)[0] != 0:
        raise Refus("COMMIT_CODE : pas un ancêtre de la tête distante de main")
    for f in FICHIERS_CODE:
        c1, a, _ = git(racine, "show", f"{commit_code}:{f}", entree=b"")
        c2, s, _ = git(racine, "show", f"{commit_code}:{f}.sha256")
        if c1 != 0 or c2 != 0 or s.split()[:1] != [hashlib.sha256(a).hexdigest()]:
            raise Refus(f"{f} absent du commit ou différent de son compagnon")
    c1, b, _ = git(racine, "show", f"{commit_lot}:{BUNDLE}", entree=b"")
    if c1 != 0 or hashlib.sha256(b).hexdigest() != SHA_BUNDLE:
        raise Refus("paquet de l'arbre absent de COMMIT_LOT ou d'empreinte différente")
    for br in branches:
        c, _, _ = git(racine, "ls-remote", "--exit-code", "origin", f"refs/heads/{br}")
        if c != 2:
            raise Refus(f"branche {br} présente sur le dépôt distant (R12) ou dépôt injoignable (code {c})")


FICHE = "docs/procedures/crible-v-v1/fiche-lancement-crible-v-v1.json"


def exiger_fiche(racine, commit_code):
    """Fiche de lancement au commit du code : texte qui fait foi et addendum d'empreintes présents à leurs empreintes, D et M de
    la règle ; rend son empreinte (passée à l'amorce)."""
    sys.path.insert(0, str(ICI))
    import crible_v_commun_v1 as K
    c, b, _ = git(racine, "show", f"{commit_code}:{FICHE}", entree=b"")
    if c != 0:
        raise Refus("fiche de lancement absente du commit du code")
    try:
        f = json.loads(b)
        for cle in ("texte", "addendum"):
            c2, x, _ = git(racine, "show", f"{commit_code}:{f[cle]['chemin']}", entree=b"")
            if c2 != 0 or hashlib.sha256(x).hexdigest() != f[cle]["sha256"]:
                raise Refus(f"fiche : {cle} absent du commit ou d'empreinte différente")
        if K.m_de_la_regle(f["duree_d_s"]) is None or K.m_de_la_regle(f["duree_d_s"]) != f["files"]:
            raise Refus("fiche : D « non lançable » ou M ≠ M de la règle")
    except (ValueError, KeyError, TypeError):
        raise Refus("fiche de lancement illisible") from None
    return hashlib.sha256(b).hexdigest()


def ligne_de_creation(offre, commit_code, commit_lot, echeance, go_kv1, go_kv2, dossier, br_s, br_e, fiche_sha):
    b64 = base64.b64encode(gzip.compress(AMORCE.read_bytes(), compresslevel=9, mtime=0)).decode()
    env = " ".join([f"-e COMMIT_CODE={commit_code}", f"-e COMMIT_LOT={commit_lot}", f"-e ECHEANCE_UTC_S={echeance}",
                    f"-e FICHE_SHA256={fiche_sha}",
                    f"-e GO_KV1={go_kv1}", f"-e GO_KV2={go_kv2}", f"-e BR_SORTIE={br_s}", f"-e BR_ENTREE={br_e}"]
                   + [f"-e {n}=${n}" for n in CLES_PAR_NOM])
    f = ("python3 -I -c 'import json, sys; d = json.load(open(sys.argv[1], encoding=\"utf-8\")); print(\"CRIBLEV CREATION success\", "
         "d.get(\"success\"), \"new_contract\", d.get(\"new_contract\"), \"cles\", sorted(d))' " + f"{dossier}/reponse-creation.json")
    ligne = (f"( umask 077; GO_ID={go_kv2} {V} create instance {offre} --raw --image {IMAGE} --disk {DISQUE_GO} --cancel-unavail "
             f"--label {ETIQUETTE} --env \"{env}\" --entrypoint bash --args -c \"echo {b64} | base64 -d | gunzip > "
             f"/root/amorce_crible_v_v1.sh && bash /root/amorce_crible_v_v1.sh\" < /dev/null > {dossier}/reponse-creation.json ); {f}")
    tete = (f"CRIBLEV COMMANDE (à jouer telle quelle, une fois, après le feu écrit ; empreinte de l'amorce "
            f"{hashlib.sha256(AMORCE.read_bytes()).hexdigest()[:16]} ; base64 de l'amorce compressée : {len(b64)} caractères) :")
    return tete + "\n" + ligne + "\n"


def controle_ligne(texte):
    lignes = texte.split("\n")
    m = re.search(r"echo ([A-Za-z0-9+/=]+) \| base64 -d \| gunzip > /root/amorce_crible_v_v1\.sh && bash /root/amorce_crible_v_v1\.sh",
                  lignes[1] if len(lignes) > 1 else "")
    if len(lignes) != 3 or lignes[2] != "" or not lignes[0].startswith("CRIBLEV COMMANDE") or not m:
        raise Refus("sortie de commande mal formée (deux lignes, en-tête, amorce en base64)")
    try:
        a = gzip.decompress(base64.b64decode(m.group(1), validate=True))
    except Exception as e:  # noqa: BLE001
        raise Refus(f"base64 ou compression illisible ({type(e).__name__})") from None
    h, f = hashlib.sha256(a).hexdigest(), hashlib.sha256(AMORCE.read_bytes()).hexdigest()
    if h != f or h[:16] not in lignes[0]:
        raise Refus(f"amorce décodée {h[:16]} ≠ fichier {f[:16]}")
    for n in CLES_PAR_NOM:
        if f"-e {n}=${n}" not in lignes[1]:
            raise Refus(f"la clé {n} ne passe pas par son nom")
    return h, lignes[1].replace(m.group(1), "<B64>")


# --- après la création ------------------------------------------------------------------------------------------------------------

def exiger_prix_relu(prix):
    p = _nombre(prix)
    if p is None or not 0 < p <= PRIX_RELU_MAX:
        raise Refus(f"prix relu {prix!r} USD/h hors de ]0 ; {PRIX_RELU_MAX}] : détruire aussitôt (par l'identifiant)")
    return p


def garde_depense(racine, ident, cumul, prix, maintenant):
    c, p = _nombre(cumul), _nombre(prix)
    if c is None or p is None or c < 0 or p <= 0:
        raise Refus("cumul ou prix illisible : arrêt et destruction par l'identifiant")
    jour = datetime.fromtimestamp(int(maintenant), tz=timezone.utc).date()
    exiger_kappa(lire_go(Path(racine) / "registres" / "go.md"), ident, "kv2", jour)
    projete = c + p
    if projete >= PART_MACHINE:
        raise Refus(f"dépense machine : {c:.3f} + une heure = {projete:.3f} USD ≥ part machine {PART_MACHINE:g} USD : destruction")
    return {"cumul": c, "projete": round(projete, 4), "part_machine": PART_MACHINE}


def exiger_identifiant(ident, dossier):
    ident = str(ident)
    if not ENTIER.fullmatch(ident) or ident in INTOUCHABLES:
        raise Refus(f"identifiant {ident!r} illisible ou d'une autre tâche : jamais détruit par cette procédure")
    try:
        lu = (Path(dossier) / "id-machine.txt").read_text(encoding="ascii").split()
    except (OSError, UnicodeDecodeError):
        raise Refus("id-machine.txt illisible : l'identifiant se lit, il ne se tape pas") from None
    if lu != [ident]:
        raise Refus("identifiant ≠ celui de id-machine.txt")
    return ident


def exiger_absence(liste, ident, temoin):
    ident, temoin = str(ident), str(temoin)
    if not ENTIER.fullmatch(ident) or not ENTIER.fullmatch(temoin) or ident == temoin:
        raise Refus("absence non prouvée : identifiant ou témoin illisible, ou égaux")
    inst = liste.get("instances") if isinstance(liste, dict) else liste
    if not isinstance(inst, list) or any(not isinstance(i, dict) or "id" not in i for i in inst):
        raise Refus("absence non prouvée : liste illisible")
    ids = {str(i["id"]) for i in inst}
    if temoin not in ids:
        raise Refus(f"absence non prouvée : témoin {temoin} absent")
    if ident in ids:
        raise Refus(f"absence non prouvée : {ident} toujours listée : destruction à refaire")
    return {"detruite": ident, "temoin": temoin, "instances_listees": len(ids)}


# --- branches : lecture de la sortie, feux sur l'entrée ----------------------------------------------------------------------------

def lire_sortie(racine, br, fichier):
    if not BRANCHE_S.fullmatch(br):
        raise Refus("branche de sortie illisible")
    if git(racine, "fetch", "-q", "origin", f"+refs/heads/{br}:refs/remotes/origin/{br}")[0] != 0:
        raise Refus("branche de sortie pas encore poussée ou illisible")
    c, s, _ = git(racine, "show", f"refs/remotes/origin/{br}:{fichier}")
    if c != 0:
        raise Refus(f"{fichier} absent de la branche de sortie")
    return s


def etape(racine, br):
    for ligne in lire_sortie(racine, br, "etat.txt").splitlines():
        if ligne.startswith("etape="):
            return ligne[len("etape="):]
    return None


def exiger_etape(racine, br, attendue):
    e = etape(racine, br)
    if e != attendue:
        raise Refus(f"la machine n'est pas à l'étape « {attendue} » (étape lue : « {e} »)")


def exiger_inscription(racine, commit, chemin, empreintes):
    if not HEX40.fullmatch(commit or "") or not re.fullmatch(r"[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*", chemin or "") or ".." in chemin:
        raise Refus("inscription : commit de 40 caractères et chemin relatif lisibles")
    if git(racine, "fetch", "-q", "origin", "+refs/heads/main:refs/remotes/origin/main")[0] != 0:
        raise Refus("main illisible")
    if git(racine, "merge-base", "--is-ancestor", commit, "refs/remotes/origin/main")[0] != 0:
        raise Refus("commit d'inscription absent de main")
    c, texte, _ = git(racine, "show", f"{commit}:{chemin}")
    if c != 0:
        raise Refus("fichier d'inscription illisible au commit")
    manque = [e[:12] for e in empreintes if e not in texte]
    if manque:
        raise Refus(f"empreintes absentes de l'inscription : {manque}")


def ecrire_entree(racine, br, fichiers):
    """Commit posé sur le sommet de la branche d'entrée (s'il existe), poussé, relu ; `fichiers` : {nom : octets}."""
    if not BRANCHE_E.fullmatch(br):
        raise Refus("branche d'entrée illisible")
    tip = ""
    if git(racine, "ls-remote", "--exit-code", "origin", f"refs/heads/{br}")[0] == 0:
        if git(racine, "fetch", "-q", "origin", f"+refs/heads/{br}:refs/remotes/origin/{br}")[0] != 0:
            raise Refus("branche d'entrée illisible")
        tip = git(racine, "rev-parse", f"refs/remotes/origin/{br}")[1].strip()
    lignes = {}
    if tip:
        for x in git(racine, "ls-tree", tip)[1].splitlines():
            meta, nom = x.split("\t", 1)
            lignes[nom] = meta
    for nom, octets in fichiers.items():
        r = subprocess.run(["git", "-C", str(racine), "hash-object", "-w", "--stdin"], input=octets, capture_output=True)
        if r.returncode != 0:
            raise Refus(f"objet de {nom} impossible")
        lignes[nom] = f"100644 blob {r.stdout.decode().strip()}"
    arbre = git(racine, "mktree", entree="".join(f"{m}\t{n}\n" for n, m in sorted(lignes.items())))[1].strip()
    args = ["commit-tree", arbre] + (["-p", tip] if tip else []) + ["-m", "crible (v) : feu de la mère"]
    c = git(racine, *args)[1].strip()
    if not HEX40.fullmatch(c):
        raise Refus("commit du feu impossible")
    if git(racine, "push", "-q", "origin", f"{c}:refs/heads/{br}")[0] != 0:
        raise Refus("poussée de la branche d'entrée refusée : nœud (ne pas contourner)")
    if git(racine, "ls-remote", "origin", f"refs/heads/{br}")[1].split("\t")[0] != c:
        raise Refus("sommet distant de l'entrée ≠ commit poussé")
    return c


def feu_phrase(racine, br_s, br_e, phrase, commit_i, chemin_i):
    try:
        exiger_etape(racine, br_s, "attente du feu 1 (phrase)")
        ss = lire_sortie(racine, br_s, "secret-sha256.txt").strip().removeprefix("secret_sha256=")
        if not HEX64.fullmatch(ss):
            raise Refus("empreinte du secret illisible sur la sortie")
        exiger_inscription(racine, commit_i, chemin_i, [ss])
        b = Path(phrase).read_bytes()
        if not (2 <= len(b) <= 400 and b.count(b"\n") == 1 and b.endswith(b"\n") and b"\0" not in b and b"\r" not in b):
            raise Refus("phrase : une ligne non vide, sans octet nul, finie par un retour à la ligne, au plus 400 octets")
        b.decode("utf-8")
        with tempfile.TemporaryDirectory() as td:
            cle = Path(td) / "cle.pem"
            cle.write_text(lire_sortie(racine, br_s, "cle-publique-phrase.pem"))
            der = subprocess.run(["openssl", "pkey", "-pubin", "-in", str(cle), "-outform", "DER"], capture_output=True)
            if der.returncode != 0 or hashlib.sha256(der.stdout).hexdigest() != lire_sortie(racine, br_s, "cle-publique-phrase.empreinte").strip():
                raise Refus("clé publique ≠ son empreinte poussée")
            txt = subprocess.run(["openssl", "pkey", "-pubin", "-in", str(cle), "-text_pub", "-noout"], capture_output=True, text=True)
            if "Public-Key: (4096 bit)" not in txt.stdout:
                raise Refus("clé publique de la phrase : RSA de 4096 bits exigée")
            ch = subprocess.run(["openssl", "pkeyutl", "-encrypt", "-pubin", "-inkey", str(cle), "-pkeyopt", "rsa_padding_mode:oaep",
                                 "-pkeyopt", "rsa_oaep_md:sha256", "-pkeyopt", "rsa_mgf1_md:sha256", "-in", str(phrase)], capture_output=True)
            if ch.returncode != 0:
                raise Refus("chiffrement impossible")
        sp = hashlib.sha256(b).hexdigest()
        feu = (f"feu=phrase\nsecret_sha256={ss}\nphrase_fichier_sha256={sp}\ninscription_commit={commit_i}\n"
               f"inscription_chemin={chemin_i}\n").encode()
        print(f"CRIBLEV empreinte du fichier de la phrase (à inscrire) : {sp}")
        return ecrire_entree(racine, br_e, {"phrase-chiffree.b64": base64.b64encode(ch.stdout), "feu-1-phrase.txt": feu})
    finally:
        if os.path.exists(phrase):
            subprocess.run(["shred", "-u", str(phrase)], check=False)
            print("CRIBLEV fichier de la phrase effacé (shred), que la poussée ait réussi ou non")


def engagement_de_la_sortie(racine, br_s):
    e = json.loads(lire_sortie(racine, br_s, "engagement-mondes.json"))
    c = json.loads(lire_sortie(racine, br_s, "engagement-certifiees.json"))
    h, hc = e.get("fichier_mondes_sha256"), c.get("certifiees_sha256")
    shas = e.get("mondes_sha256")
    if not (HEX64.fullmatch(h or "") and HEX64.fullmatch(hc or "") and isinstance(shas, list) and len(shas) == 20
            and all(HEX64.fullmatch(s) for s in shas) and c.get("fichier_mondes_sha256") == h):
        raise Refus("engagements des mondes et des étiquettes illisibles ou discordants")
    return h, hc, shas


def feu_mondes(racine, br_s, br_e, commit_i, chemin_i):
    exiger_etape(racine, br_s, "attente du feu 2 (mondes)")
    h, hc, shas = engagement_de_la_sortie(racine, br_s)
    exiger_inscription(racine, commit_i, chemin_i, [h, hc] + shas)
    feu = (f"feu=mondes\nfichier_mondes_sha256={h}\ncertifiees_sha256={hc}\ninscription_commit={commit_i}\n"
           f"inscription_chemin={chemin_i}\n").encode()
    return ecrire_entree(racine, br_e, {"feu-2-mondes.txt": feu})


def feu_reel(racine, br_s, br_e, go_kv1, go_kv2, d_s, m, commit_i, chemin_i):
    """Feu du crible réel : D relevée (somme des quatre durées et de l'énumération, inscrite sur main) et M de la règle ; lignes
    κv1 et κv2 nommées."""
    sys.path.insert(0, str(ICI))
    import crible_v_commun_v1 as K
    exiger_etape(racine, br_s, "attente du feu 3 (crible reel)")
    h, _, _ = engagement_de_la_sortie(racine, br_s)
    d = _nombre(d_s)
    if d is None or K.m_de_la_regle(d) is None:
        raise Refus(f"D = {d_s!r} s : budget de durée « non lançable » (mot de la mère)")
    if int(m) != K.m_de_la_regle(d):
        raise Refus(f"M = {m} ≠ M de la règle ({K.m_de_la_regle(d)})")
    if not (GO_ID.fullmatch(go_kv1) and GO_ID.fullmatch(go_kv2) and go_kv1 != go_kv2):
        raise Refus("lignes κv1 et κv2 illisibles")
    exiger_inscription(racine, commit_i, chemin_i, [f"D = {d_s} s", f"M = {m}"])
    feu = (f"feu=reel\nfichier_mondes_sha256={h}\ngo_kv1={go_kv1}\ngo_kv2={go_kv2}\nduree_d_s={d_s}\nfiles={m}\n"
           f"inscription_commit={commit_i}\ninscription_chemin={chemin_i}\n").encode()
    return ecrire_entree(racine, br_e, {"feu-3-reel.txt": feu})


def feu_arret(racine, br_e, cause):
    if not CAUSE.fullmatch(cause or ""):
        raise Refus("cause : lettres sans accent, chiffres, espaces et « , . : ; ( ) _ - », cent caractères au plus")
    return ecrire_entree(racine, br_e, {"feu-arret.txt": f"feu=arret\ncause={cause}\n".encode()})


def recuperer(racine, br_s, dossier):
    d = Path(dossier)
    if d.exists():
        raise Refus("dossier de récupération existant (R12)")
    lire_sortie(racine, br_s, "etat.txt")
    d.mkdir(parents=True)
    a = subprocess.run(["git", "-C", str(racine), "archive", f"refs/remotes/origin/{br_s}"], capture_output=True)
    if a.returncode != 0:
        raise Refus("archive de la sortie impossible")
    t = subprocess.run(["tar", "-x", "-C", str(d)], input=a.stdout, capture_output=True)
    if t.returncode != 0:
        raise Refus("extraction impossible")
    return sorted(str(p.relative_to(d)) for p in d.rglob("*") if p.is_file())


def _json(chemin):
    try:
        return json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise Refus(f"{chemin} illisible ({type(e).__name__})") from None


def main(a):
    try:
        if a[:1] == ["offre-depuis-recherche"] and len(a) == 3:
            o, journal = offre_depuis_recherche(_json(a[1]))
            exiger_offre(o, o["id"])
            with open(a[2], "x", encoding="utf-8") as f:
                f.write(json.dumps(o, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
            print("\n".join("CRIBLEV " + x for x in journal))
            print(f"CRIBLEV OFFRE ECRITE {a[2]} : offre {o['id']}, {o['num_gpus']} carte(s), prix garde {o['prix_garde_usd_h']:.4f} USD/h ; "
                  f"réseau : descente {o['inet_down_cost']!r}, montée {o['inet_up_cost']!r}")
        elif a[:1] == ["offre"] and len(a) in (2, 3):
            exiger_offre(_json(a[1]), a[2] if len(a) == 3 else None)
            print("CRIBLEV OFFRE ACCEPTEE")
        elif a[:1] == ["creation"] and len(a) == 4:
            print(f"CRIBLEV CREATION PERMISE {exiger_creation(a[1], a[2], a[3], int(time.time()))}")
        elif a[:1] == ["commande"] and len(a) == 10:
            racine, fo, cc, cl, ech, feu, dos, br_s, br_e = a[1:]
            offre = _json(fo)
            exiger_offre(offre, offre.get("id"))
            if not ENTIER.fullmatch(ech) or not abs(int(ech) - (time.time() + DUREE_S)) <= ECART_ECHEANCE_S:
                raise Refus("échéance hors de [maintenant + 17 h ± 5 min]")
            if not (re.fullmatch(r"/[A-Za-z0-9._/-]+", dos) and os.path.isdir(dos)) or os.path.exists(os.path.join(dos, "reponse-creation.json")):
                raise Refus("dossier d'envoi : chemin absolu existant, sans reponse-creation.json (une création par dossier)")
            if not (BRANCHE_S.fullmatch(br_s) and BRANCHE_E.fullmatch(br_e) and br_s[-3:] == br_e[-3:]):
                raise Refus("branches de sortie et d'entrée illisibles (même version)")
            g = exiger_creation(racine, feu, cc, int(time.time()))
            exiger_commits(racine, cc, cl, (br_s, br_e))
            fiche_sha = exiger_fiche(racine, cc)
            with tempfile.TemporaryDirectory() as td:
                env = {"PATH": "/usr/bin:/bin", "HOME": td, "AMORCE_ESSAI_LOCAL": "1", "COMMIT_CODE": cc, "COMMIT_LOT": cl,
                       "ECHEANCE_UTC_S": ech, "GO_KV1": g["kv1"], "GO_KV2": g["kv2"], "BR_SORTIE": br_s, "BR_ENTREE": br_e,
                       "FICHE_SHA256": fiche_sha}
                r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, stdin=subprocess.DEVNULL)
                if r.returncode != 0 or os.listdir(td):
                    raise Refus(f"arguments refusés par l'amorce en essai local : {r.stdout.strip()[:200]}")
            sys.stdout.write(ligne_de_creation(offre["id"], cc, cl, ech, g["kv1"], g["kv2"], dos, br_s, br_e, fiche_sha))
        elif a[:1] == ["controle-ligne"] and len(a) == 2:
            h, masquee = controle_ligne(Path(a[1]).read_text(encoding="utf-8"))
            print(f"CRIBLEV LIGNE CONFORME : amorce décodée égale à l'octet ({h[:16]})")
            print(masquee)
        elif a[:1] == ["inventaire"] and len(a) == 1:
            d = json.load(sys.stdin)
            liste = d.get("instances") if isinstance(d, dict) else d
            if not isinstance(liste, list) or any(not isinstance(i, dict) or "id" not in i for i in liste):
                raise Refus("liste des instances illisible")
            for i in sorted(liste, key=lambda i: int(i["id"])):
                print(i["id"], i.get("label"))
        elif a[:1] == ["prix-relu"] and len(a) == 2:
            print(f"CRIBLEV PRIX RELU ACCEPTE {exiger_prix_relu(a[1]):g} USD/h")
        elif a[:1] == ["depense"] and len(a) == 5:
            print(f"CRIBLEV DEPENSE {garde_depense(a[1], a[2], a[3], a[4], int(time.time()))}")
        elif a[:1] == ["detruire"] and len(a) == 4:
            if not GO_ID.fullmatch(a[3]):
                raise Refus("GO illisible")
            ident = exiger_identifiant(a[1], a[2])
            print(f"GO_ID={a[3]} {V} destroy instance {ident} -y")
            print("CRIBLEV PUIS (jamais juger la destruction par le code de sortie ; attendre 30 s) : absence ID TEMOIN LISTE.json")
        elif a[:1] == ["absence"] and len(a) == 4:
            r = exiger_absence(_json(a[3]), a[1], a[2])
            print(f"CRIBLEV DESTRUCTION PROUVEE {r['detruite']} : absente, témoin {r['temoin']} présent, {r['instances_listees']} instance(s)")
        elif a[:1] == ["etat"] and len(a) == 3:
            print(lire_sortie(a[1], a[2], "etat.txt"), end="")
            print("--- journal de la machine (fin)")
            print("\n".join(lire_sortie(a[1], a[2], "journal-machine.txt").splitlines()[-12:]))
        elif a[:1] == ["feu-phrase"] and len(a) == 7:
            print(f"CRIBLEV feu poussé : {feu_phrase(*a[1:])}")
        elif a[:1] == ["feu-mondes"] and len(a) == 6:
            print(f"CRIBLEV feu poussé : {feu_mondes(*a[1:])}")
        elif a[:1] == ["feu-reel"] and len(a) == 10:
            print(f"CRIBLEV feu poussé : {feu_reel(*a[1:])}")
        elif a[:1] == ["feu-arret"] and len(a) == 4:
            print(f"CRIBLEV feu poussé : {feu_arret(*a[1:])}")
        elif a[:1] == ["recuperer"] and len(a) == 4:
            print(f"CRIBLEV RECUPERE {len(recuperer(*a[1:]))} fichier(s) dans {a[3]}")
        else:
            print("CRIBLEV REFUS : sous-commande inconnue ou arguments en nombre faux (voir l'en-tête)")
            return 2
    except (Refus, ValueError, OSError) as e:
        print(f"CRIBLEV REFUS : {e}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
