"""Lanceur de la machine autonome de la ligne 1 de carte du bras A, version 4 (23 novembre 2026 ; les versions 1 à 3
restent telles quelles).

Différence avec la version 3 : le masquage seul. Constaté en vrai : la sous-commande `masquer` de la v3 laissait passer
le champ `instance_api_key` de la réponse du loueur à la création (`Started. {'success': True, 'new_contract': …,
'instance_api_key': '…'}`, dict Python, ou JSON). La v4 masque, en `***` : (1) la valeur de tout champ dont le nom
contient `api_key`, `apikey`, `token`, `secret`, `password` ou `key` (casse ignorée), sous forme JSON
(`"nom": "valeur"`), dict Python (`'nom': 'valeur'`), `nom=valeur` ou paire `[nom, valeur]`, et dans les objets
structurés ; (2) toute suite d'au moins 32 caractères hexadécimaux et tout ce qui ressemble à un jeton GitHub
(`ghp_`, `gho_`, `ghs_`, `ghu_`, `ghr_`, `github_pat_`) ou Hugging Face (`hf_`), sauf les empreintes et commits connus
(liste blanche : `--commit-entree`, `--amorce-sha256`, `--connue`, ou `COMMIT_ENTREE` et `AMORCE_SHA256` de
l'environnement ; la vérification y met le commit lu et l'empreinte du manifeste qu'elle a calculés) ; (3) les
valeurs des variables secrètes présentes dans l'environnement, comme la v3. La commande de création passe le commit
d'entrée et l'empreinte de l'amorce complète à `masquer`. Ce qui suit décrit la version 3, au nom du programme et au
masque près.

Différences de la version 3 avec la version 2 (contre-lecture de la machine v2) : amorce d'appel v2
(`scripts/amorce_appel_ligne_1_bras_a_v2.sh`) et amorce complète v3 (`scripts/amorce_ligne_1_bras_a_v3.sh`) ; la
commande imprimée porte `${GH_TOKEN:?}` et `${HF_TOKEN:?}` (un secret vide fait échouer la commande chez la mère, au
lieu d'un démarrage perdu), et sa sortie passe par la sous-commande `masquer` de ce programme (m8).

Version 2 : Joué par la session mère (qui porte
les clés, par leur nom) ; sans SSH : tout passe par git et par l'interface HTTPS du loueur.

Différence avec la version 1 : le champ onstart de Vast est limité à environ 4 Ko ; la commande passe donc
`--onstart <amorce d'appel>` (amorce d'appel de moins de 2 500 octets, refusée au-delà), et
`AMORCE_SHA256` est l'empreinte de l'**amorce complète**, portée par la branche
d'entrée, que l'amorce d'appel vérifie avant de l'exécuter. Ce qui suit décrit la version 1, au nom de l'amorce près.

Sous-commandes :
- `creation` : **imprime** la commande exacte de création (`GO_ID=GO-2026-11-22-148 vastai create instance <offre> …
  --env "-e GH_TOKEN=${GH_TOKEN:?} -e HF_TOKEN=${HF_TOKEN:?} -e …" --onstart scripts/amorce_appel_ligne_1_bras_a_v2.sh …
  2>&1 | … masquer`) ; les
  secrets n'y paraissent que par leur NOM (`$GH_TOKEN`, développé par le shell de la session au moment de la
  commande) ; `AVANT_CREATION_UTC=$(date -u …)` est relevée par ce même shell juste avant la création (borne prudente
  de l'heure de création). N'exécute rien ; vérifie seulement, par `git ls-remote`, que la branche d'entrée est sur le
  dépôt distant au commit donné (sauf `--sans-verifier-entree`).
- `etat` : lit l'instance par l'interface du loueur (`GET /api/v0/instances/<id>/?owner=me`, clé `VAST_API_KEY` lue
  par son nom) ; rend statut, prix réel (`dph_total`), `start_date` et sa conversion arrondie vers le bas ; avec
  `--constat`, compare le prix réel au taux du constat (m2 : au-dessus, la ligne dit « détruire »).
- `verification` : la branche de sortie existe sur le dépôt distant, elle est orpheline, ne porte qu'un dossier de
  versement, le manifeste du versement est scellé et chaque pièce répond à l'inventaire
  (`lanceur_bras_a_v8.exiger_manifeste_du_versement_scelle`) ; avec `--start-date`, recoupe l'heure de création
  retenue par l'amorce (`amorce.json`) : elle doit être au plus `start_date` (le compteur compte au moins depuis lui).
  Récupérer n'est pas lire : les épisodes ne sont pas ouverts, seulement empreintés.

Toute réponse du loueur est **masquée** avant d'être écrite : valeurs de VAST_API_KEY, HF_TOKEN, GH_TOKEN,
CONTAINER_API_KEY présentes dans l'environnement, tout champ dont le nom contient `api_key`, `token`, `secret` ou
`password`, et toute paire `[nom, valeur]` (variables de l'instance) dont le nom est de cette sorte.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

GO_ID = "GO-2026-11-22-148"
IMAGE = "pytorch/pytorch:2.14.1-cuda13.0-cudnn9-runtime"
DISQUE_GO = 150
ETIQUETTE = "bras-a-ligne-1-v1"
AMORCE = "scripts/amorce_appel_ligne_1_bras_a_v2.sh"
AMORCE_COMPLETE = "scripts/amorce_ligne_1_bras_a_v3.sh"
CE_PROGRAMME = "scripts/lanceur_machine_ligne_1_bras_a_v4.py"
TAILLE_MAX_APPEL = 2500
BRANCHE_ENTREE = "entree/bras-a-ligne-1-v1"
BRANCHE_SORTIE = "calcul/bras-a-ligne-1-v1"
API = "https://console.vast.ai/api/v0"
SECRETS = ("VAST_API_KEY", "HF_TOKEN", "GH_TOKEN", "CONTAINER_API_KEY")
_NOM = r"[\w.-]*?(?:api_?key|apikey|token|secret|password|key)[\w.-]*"
_NOM_SECRET = re.compile(r"api_?key|apikey|token|secret|password|key", re.I)
_CHAINE = r"""(?P<q2>["'])(?:\\.|(?!(?P=q2))[^\\])*(?P=q2)"""
# "nom": valeur  /  'nom': valeur  (JSON, dict Python)
_CHAMP = re.compile(r"""(?P<tete>(?P<q>["'])""" + _NOM + r"""(?P=q)\s*:\s*)(?:""" + _CHAINE + r"""|[^,\s}\]]+)""", re.I)
# [nom, valeur]  /  ("nom", valeur)
_PAIRE = re.compile(r"""(?P<tete>[\[(]\s*(?P<q>["'])""" + _NOM + r"""(?P=q)\s*,\s*)(?:""" + _CHAINE
                    + r"""|[^\]\)\s,]+)(?P<queue>\s*[\])])""", re.I)
# nom=valeur
_EGAL = re.compile(r"""(?P<tete>(?<![\w.-])""" + _NOM + r"""\s*=(?!=)\s*)(?:""" + _CHAINE + r"""|[^\s,;&'"\]}\)]+)""", re.I)
_JETON = re.compile(r"(?<![A-Za-z0-9_])(?:gh[opsur]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|hf_[A-Za-z0-9]{20,})")
_HEX = re.compile(r"(?<![0-9A-Fa-f])[0-9A-Fa-f]{32,}(?![0-9A-Fa-f])")
_CONNUE = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
CONNUES_ENV = ("COMMIT_ENTREE", "AMORCE_SHA256")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_BRANCHE = re.compile(r"[a-z0-9][a-z0-9/._-]*[a-z0-9]")
_VERSEMENT = re.compile(r"diag/organismes-discrets-v-a-v2/ligne-1-(fini|arret|echec|reprise)-\d{8}T\d{6}Z")
MASQUE = "***"
CHAMPS_ETAT = ("id", "label", "actual_status", "intended_status", "cur_state", "next_state", "status_msg", "gpu_name",
               "driver_version", "dph_total", "dph_base", "storage_cost", "disk_space", "start_date", "end_date")


class Refus(Exception):
    pass


def valeurs_secretes() -> list[str]:
    return [v for v in (os.environ.get(n, "") for n in SECRETS) if len(v) >= 4]


def connues_de_l_environnement() -> list[str]:
    return [os.environ.get(n, "") for n in CONNUES_ENV]


def _liste_blanche(connues) -> frozenset:
    return frozenset(c.strip().lower() for c in (connues or ()) if isinstance(c, str) and _CONNUE.fullmatch(c.strip().lower()))


def _valeur_masquee(m, nue: str = MASQUE) -> str:
    q = m.group("q2")
    return m.group("tete") + (f"{q}{MASQUE}{q}" if q else nue) + (m.groupdict().get("queue") or "")


def _valeur_masquee_citee(m) -> str:
    """Champ JSON ou paire dont la valeur n'est pas une chaîne (nombre, null) : `"***"`, pour que le JSON reste lisible."""
    return _valeur_masquee(m, f'"{MASQUE}"')


def masquer_texte(texte: str, valeurs=None, connues=None) -> str:
    """Texte masqué : (3) valeurs secrètes de l'environnement ; (1) valeur de tout champ au nom de secret (JSON, dict
    Python, `nom=valeur`, paire) ; (2) jetons GitHub et Hugging Face, suites hexadécimales d'au moins 32 caractères
    hors liste blanche."""
    valeurs = valeurs_secretes() if valeurs is None else valeurs
    blanche = _liste_blanche(connues_de_l_environnement() if connues is None else connues)
    for v in sorted(valeurs, key=len, reverse=True):
        texte = texte.replace(v, MASQUE)
    texte = _CHAMP.sub(_valeur_masquee_citee, texte)
    texte = _PAIRE.sub(_valeur_masquee_citee, texte)
    texte = _EGAL.sub(_valeur_masquee, texte)
    texte = _JETON.sub(MASQUE, texte)
    return _HEX.sub(lambda m: m.group(0) if m.group(0).lower() in blanche else MASQUE, texte)


def masquer(objet, valeurs=None, connues=None):
    """Copie masquée : champs au nom de secret, paires [nom, valeur] de secret, et chaque chaîne par `masquer_texte`."""
    valeurs = valeurs_secretes() if valeurs is None else valeurs
    connues = connues_de_l_environnement() if connues is None else connues
    if isinstance(objet, dict):
        return {k: (MASQUE if isinstance(k, str) and _NOM_SECRET.search(k) else masquer(v, valeurs, connues))
                for k, v in objet.items()}
    if isinstance(objet, (list, tuple)):
        if len(objet) == 2 and isinstance(objet[0], str) and _NOM_SECRET.search(objet[0]):
            return [objet[0], MASQUE]
        return [masquer(x, valeurs, connues) for x in objet]
    if isinstance(objet, str):
        return masquer_texte(objet, valeurs, connues)
    return objet


def ecrire(objet, connues=None) -> None:
    connues = list(connues or ()) + connues_de_l_environnement()
    print(masquer(json.dumps(masquer(objet, connues=connues), ensure_ascii=False, indent=1), connues=connues))


# --- creation ------------------------------------------------------------------------------------------------------------

def commande_de_creation(offre: int, commit_entree: str, amorce: str, amorce_sha256: str, image: str = IMAGE,
                         disque: int = DISQUE_GO, etiquette: str = ETIQUETTE, branche_entree: str = BRANCHE_ENTREE,
                         branche_sortie: str = BRANCHE_SORTIE) -> str:
    if isinstance(offre, bool) or not isinstance(offre, int) or offre <= 0:
        raise Refus("offre : entier positif exigé")
    if _COMMIT.fullmatch(commit_entree or "") is None:
        raise Refus("commit d'entrée entier exigé")
    for b in (branche_entree, branche_sortie):
        if _BRANCHE.fullmatch(b or "") is None or ".." in b:
            raise Refus(f"branche {b!r} illisible")
    if branche_entree == branche_sortie:
        raise Refus("branches d'entrée et de sortie confondues")
    for nom, v in (("image", image), ("étiquette", etiquette), ("amorce", amorce)):
        if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/:@-]*", v or "") is None:
            raise Refus(f"{nom} {v!r} illisible")
    env = " ".join(["-e GH_TOKEN=${GH_TOKEN:?}", "-e HF_TOKEN=${HF_TOKEN:?}", f"-e GO_ID={GO_ID}",
                    f"-e BRANCHE_ENTREE={branche_entree}", f"-e BRANCHE_SORTIE={branche_sortie}",
                    f"-e COMMIT_ENTREE={commit_entree}", f"-e AMORCE_SHA256={amorce_sha256}",
                    "-e AVANT_CREATION_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)"])
    return (f"GO_ID={GO_ID} vastai create instance {offre} --image {image} --disk {disque} --label {etiquette} "
            f"--cancel-unavail --raw --env \"{env}\" --onstart {amorce} 2>&1 | PYTHONPATH=src .venv/bin/python "
            f"{CE_PROGRAMME} masquer --commit-entree {commit_entree} --amorce-sha256 {amorce_sha256}")


def _ls_remote(distant: str, branche: str, racine: Path) -> str | None:
    r = subprocess.run(["git", "-C", str(racine), "ls-remote", distant, f"refs/heads/{branche}"], capture_output=True, text=True)
    if r.returncode != 0:
        raise Refus(f"dépôt distant injoignable (ls-remote : code {r.returncode})")
    return r.stdout.split()[0] if r.stdout.strip() else None


def sous_creation(a) -> int:
    racine = Path(a.racine)
    amorce, complete = racine / a.amorce, racine / a.amorce_complete
    for f in (amorce, complete):
        if f.is_symlink() or not f.is_file():
            raise Refus(f"amorce {f} absente")
    if amorce.stat().st_size >= TAILLE_MAX_APPEL:
        raise Refus(f"amorce d'appel de {amorce.stat().st_size} octets : moins de {TAILLE_MAX_APPEL} exigés (onstart)")
    sha = hashlib.sha256(complete.read_bytes()).hexdigest()
    if not a.sans_verifier_entree:
        lu = _ls_remote(a.distant, a.branche_entree, racine)
        if lu != a.commit_entree:
            raise Refus(f"branche d'entrée {a.branche_entree} : distant {lu or 'absent'}, {a.commit_entree} attendu")
        if _ls_remote(a.distant, a.branche_sortie, racine) is not None:
            raise Refus(f"branche de sortie {a.branche_sortie} déjà présente sur le dépôt distant (R12)")
    print(commande_de_creation(a.offre, a.commit_entree, a.amorce, sha, a.image, a.disque, a.etiquette,
                               a.branche_entree, a.branche_sortie))
    print(f"# amorce d'appel {a.amorce} ({amorce.stat().st_size} octets) ; amorce complète {a.amorce_complete} sha256 "
          f"{sha} ; rien n'est exécuté par ce programme", file=sys.stderr)
    return 0


# --- etat ----------------------------------------------------------------------------------------------------------------

def instant_bas(secondes) -> str:
    return datetime.fromtimestamp(int(math.floor(float(secondes))), timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def lire_l_instance(identifiant: str, api: str = API) -> dict:
    if re.fullmatch(r"[0-9]{1,12}", identifiant or "") is None:
        raise Refus("identifiant d'instance : chiffres seuls (R10)")
    cle = os.environ.get("VAST_API_KEY", "")
    if not cle:
        raise Refus("VAST_API_KEY absente de l'environnement (lue par son nom)")
    q = urllib.request.Request(f"{api}/instances/{identifiant}/?owner=me", headers={"Authorization": f"Bearer {cle}"})
    try:
        with urllib.request.urlopen(q, timeout=60) as r:
            corps = json.loads(r.read().decode("utf-8"))
    except Exception as e:                                   # message masqué : jamais la clé
        raise Refus(masquer(f"lecture de l'instance en échec ({type(e).__name__} : {e})")) from None
    return corps.get("instances") if isinstance(corps, dict) else None


def etat_de_l_instance(ligne: dict | None, constat: dict | None = None) -> dict:
    if ligne is None:
        return {"instance": None, "lecture": "absente ou détruite"}
    sortie = {k: ligne.get(k) for k in CHAMPS_ETAT if k in ligne}
    if isinstance(ligne.get("start_date"), (int, float)) and ligne["start_date"] > 0:
        sortie["start_date_utc"] = instant_bas(ligne["start_date"])
    if constat is not None:
        t = constat["tarifs"]
        taux = t["carte_usd_h"] + t["stockage_usd_h"]
        prix = ligne.get("dph_total")
        sortie["taux_du_constat_usd_h"] = taux
        sortie["prix_reel_sous_le_constat"] = isinstance(prix, (int, float)) and prix <= taux
        if not sortie["prix_reel_sous_le_constat"]:
            sortie["consigne"] = "prix réel au-dessus du taux du constat (m2) : destruction par l'identifiant"
    return masquer(sortie)


def sous_etat(a) -> int:
    constat = json.loads(Path(a.constat).read_text(encoding="utf-8")) if a.constat else None
    ecrire(etat_de_l_instance(lire_l_instance(a.instance, a.api), constat))
    return 0


# --- verification --------------------------------------------------------------------------------------------------------

def verifier_la_sortie(distant: str, branche: str, racine: Path, start_date: float | None = None,
                       commit_attendu: str | None = None) -> dict:
    """Branche de sortie : présente, orpheline, un seul dossier de versement, manifeste scellé et inventaire conforme."""
    sys.path.insert(0, str(Path(racine).resolve() / "src"))
    from controle_ia.organismes_discrets import lanceur_bras_a_v8 as la
    lu = _ls_remote(distant, branche, racine)
    if lu is None:
        raise Refus(f"branche de sortie {branche} absente du dépôt distant")
    if commit_attendu and lu != commit_attendu:
        raise Refus(f"branche de sortie à {lu}, {commit_attendu} attendu")
    t = Path(tempfile.mkdtemp(prefix="verification-sortie-ligne-1-"))
    g = ["git", "-C", str(t)]
    for c in (g + ["init", "-q"], g + ["fetch", "-q", "--depth", "1", distant, f"refs/heads/{branche}"],
              g + ["checkout", "-q", "FETCH_HEAD"]):
        r = subprocess.run(c, capture_output=True, text=True)
        if r.returncode != 0:
            raise Refus(masquer(f"{' '.join(c[3:5])} en échec : {r.stderr.strip()[:200]}"))
    tete = subprocess.run(g + ["rev-list", "--parents", "-n", "1", "HEAD"], capture_output=True, text=True).stdout.split()
    if tete[0] != lu or tete[1:]:
        raise Refus("la branche de sortie n'est pas un commit orphelin au commit lu")
    chemins = subprocess.run(g + ["ls-tree", "-r", "--name-only", "HEAD"], capture_output=True, text=True).stdout.split("\n")[:-1]
    dossiers = {"/".join(c.split("/")[:3]) for c in chemins}
    if len(dossiers) != 1 or _VERSEMENT.fullmatch(next(iter(dossiers))) is None:
        raise Refus(f"la branche porte autre chose qu'un dossier de versement : {sorted(dossiers)[:5]}")
    dossier = next(iter(dossiers))
    try:
        sha = la.exiger_manifeste_du_versement_scelle(t / dossier)
    except Exception as e:
        raise Refus(f"versement non conforme : {e}") from None
    amorce = json.loads((t / dossier / "amorce.json").read_text(encoding="utf-8"))
    sortie = {"branche": branche, "commit": lu, "dossier": dossier, "fichiers": len(chemins),
              "manifeste_du_versement_sha256": sha, "etat": amorce.get("etat"), "motif": amorce.get("motif"),
              "code_course": amorce.get("code_course"), "instance": amorce.get("instance"),
              "creation_retenue_utc": amorce.get("creation_retenue_utc"), "source_creation": amorce.get("source_creation"),
              "copie_locale": str(t)}
    if start_date is not None:
        sortie["start_date_utc"] = instant_bas(start_date)
        sortie["creation_retenue_au_plus_start_date"] = amorce.get("creation_retenue_utc", "9") <= sortie["start_date_utc"]
    return masquer(sortie, connues=[lu, sha] + connues_de_l_environnement())


def sous_verification(a) -> int:
    sortie = verifier_la_sortie(a.distant, a.branche_sortie, Path(a.racine), a.start_date, a.commit)
    ecrire(sortie, connues=[sortie["commit"], sortie["manifeste_du_versement_sha256"]])
    return 0 if sortie.get("creation_retenue_au_plus_start_date", True) else 3


def sous_masquer(a) -> int:
    """Recopie l'entrée standard masquée (sortie de la commande de création du loueur, `--raw`) ; liste blanche des
    suites hexadécimales : commit d'entrée, empreinte de l'amorce, `--connue`, et l'environnement."""
    connues = [a.commit_entree, a.amorce_sha256, *(a.connue or [])] + connues_de_l_environnement()
    valeurs = valeurs_secretes()
    for ligne in sys.stdin:
        sys.stdout.write(masquer_texte(ligne, valeurs, [c for c in connues if c]))
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--racine", default=".")
    s = p.add_subparsers(dest="sous", required=True)
    c = s.add_parser("creation")
    c.add_argument("--offre", type=int, required=True)
    c.add_argument("--commit-entree", required=True)
    c.add_argument("--amorce", default=AMORCE)
    c.add_argument("--amorce-complete", default=AMORCE_COMPLETE)
    c.add_argument("--image", default=IMAGE)
    c.add_argument("--disque", type=int, default=DISQUE_GO)
    c.add_argument("--etiquette", default=ETIQUETTE)
    c.add_argument("--branche-entree", default=BRANCHE_ENTREE)
    c.add_argument("--branche-sortie", default=BRANCHE_SORTIE)
    c.add_argument("--distant", default="origin")
    c.add_argument("--sans-verifier-entree", action="store_true")
    m = s.add_parser("masquer")
    m.add_argument("--commit-entree", help="commit cité par la commande (gardé lisible)")
    m.add_argument("--amorce-sha256", help="empreinte citée par la commande (gardée lisible)")
    m.add_argument("--connue", action="append", help="autre empreinte ou commit connu (gardé lisible)")
    e = s.add_parser("etat")
    e.add_argument("--instance", required=True)
    e.add_argument("--constat")
    e.add_argument("--api", default=API)
    v = s.add_parser("verification")
    v.add_argument("--branche-sortie", default=BRANCHE_SORTIE)
    v.add_argument("--distant", default="origin")
    v.add_argument("--start-date", type=float, help="start_date lu par `etat` (secondes depuis 1970)")
    v.add_argument("--commit", help="commit attendu de la branche de sortie")
    a = p.parse_args(argv)
    try:
        return {"creation": sous_creation, "etat": sous_etat, "verification": sous_verification,
                "masquer": sous_masquer}[a.sous](a)
    except (Refus, OSError, ValueError, KeyError) as e:
        citees = [getattr(a, n, None) for n in ("commit_entree", "amorce_sha256", "commit")] + list(getattr(a, "connue", None) or [])
        print(masquer(f"REFUS : {e}", connues=[c for c in citees if c] + connues_de_l_environnement()), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
