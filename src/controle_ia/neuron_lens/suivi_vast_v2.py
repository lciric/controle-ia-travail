"""Suivi d'une instance du loueur sans jamais restituer un secret — v2 (contre-lecture 7, remarques 2 b, 7, 8, 9).

`vastai show instance(s) --raw` restitue la configuration de l'instance, dont les variables d'environnement passées à la création
(le jeton du programme). Ce module appelle l'outil, ne garde que des champs sans secret, et refuse d'imprimer toute sortie qui
contiendrait la valeur d'une variable secrète de la session (lue par son nom, jamais affichée), sous sa forme brute, encodée pour une
adresse, ou en base 64 (seule ou dans l'en-tête `x-access-token:<jeton>`, aux trois alignements possibles dans un flux plus large).

v2 : (7) refus de tourner si `CONTROLE_IA_GITHUB_TOKEN_2` manque (sinon le balayage serait vide, sans avertissement) ; (8) formes
encodées balayées ; fonctionnement fermé gardé (sortie refusée entière, jamais expurgée) ; (9 c) forme de réponse inattendue signalée,
jamais lue comme « absente » ; (9 d) outil introuvable signalé (variable `VASTAI_OUTIL`, défaut `vastai`) ; (9 e) commande `absente`
dont le code de sortie ne vaut 0 que sur une liste lue sans erreur où l'identifiant manque ; (2 b) commande `creation` : lit sur
l'entrée standard la sortie de `vastai create instance … --raw 2>&1` et n'en rend que `success` et `new_contract` (ou,
si elle n'est pas du JSON, sa dernière ligne, balayée comme toute sortie).

Usage : `python -m controle_ia.neuron_lens.suivi_vast_v2 instance <ID>` | `instances` | `logs <ID> [N]` | `absente <ID>` |
`creation < sortie_de_create`
"""
from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
from urllib.parse import quote

SECRETS = ("CONTROLE_IA_GITHUB_TOKEN_2", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY", "HF_TOKEN")
EXIGEE = "CONTROLE_IA_GITHUB_TOKEN_2"
CHAMPS = ("id", "label", "actual_status", "cur_state", "intended_status", "dph_total", "gpu_name", "start_date", "status_msg")
MIN_FORME = 12  # longueur minimale d'un fragment base 64 balayé


def _b64_fragments(charge: bytes):
    """Fragments base 64 de `charge` qui ne dépendent que d'elle, pour chacun des trois alignements dans un flux plus large."""
    for k in range(3):
        enc = base64.b64encode(b"\0" * k + charge).decode().rstrip("=")
        debut = (0, 2, 3)[k]
        fin = len(enc) - 3  # les derniers caractères dépendent des octets qui suivent
        frag = enc[debut:fin]
        if len(frag) >= MIN_FORME:
            yield frag


def formes(valeur: str):
    """Formes cherchées pour une valeur secrète : brute, encodée pour une adresse, base 64 (seule et en en-tête), trois alignements."""
    f = {valeur, quote(valeur, safe="")}
    for charge in (valeur.encode(), b"x-access-token:" + valeur.encode()):
        f.update(_b64_fragments(charge))
    return sorted(f)


def valeurs_secretes(env=os.environ):
    if len(env.get(EXIGEE, "")) < 8:
        raise SystemExit(f"suivi refusé : {EXIGEE} absente de l'environnement (le balayage serait vide)")
    return [forme for k in SECRETS if len(env.get(k, "")) >= 8 for forme in formes(env[k])]


def balayer(texte: str, secrets) -> str:
    """Rend le texte s'il ne contient aucun secret ; sinon lève (rien n'est imprimé)."""
    if any(s in texte for s in secrets):
        raise SystemExit("sortie refusée : elle contient la valeur d'une variable secrète")
    return texte


def filtrer(d: dict) -> dict:
    return {k: d.get(k) for k in CHAMPS if k in d}


def _vast(*args):
    outil = os.environ.get("VASTAI_OUTIL", "vastai")
    try:
        p = subprocess.run([outil, *args], capture_output=True, text=True, timeout=120)
    except FileNotFoundError:
        return 127, "", f"outil introuvable : {outil}"
    return p.returncode, p.stdout, p.stderr


def _derniere(err, out, code):
    t = (err or out or "").strip()
    return t.splitlines()[-1][:200] if t else f"code {code}"


def instance(id_instance, appel=_vast):
    code, out, err = appel("show", "instance", str(int(id_instance)), "--raw")
    if code != 0:
        return {"erreur": _derniere(err, out, code)}
    try:
        d = json.loads(out) if out.strip() else {}
    except json.JSONDecodeError:
        return {"erreur": "sortie illisible (JSON)"}
    if d in ({}, None, []):
        return {"absente": True}
    if isinstance(d, dict) and "id" in d:
        return filtrer(d)
    return {"erreur": f"forme inattendue ({type(d).__name__}, clés {sorted(d)[:5] if isinstance(d, dict) else '-'})"}


def instances(appel=_vast):
    """Liste filtrée, ou dictionnaire `{"erreur": …}` (qui n'est jamais une preuve d'absence)."""
    code, out, err = appel("show", "instances", "--raw")
    if code != 0:
        return {"erreur": _derniere(err, out, code)}
    try:
        d = json.loads(out or "[]")
    except json.JSONDecodeError:
        return {"erreur": "sortie illisible (JSON)"}
    if isinstance(d, dict) and isinstance(d.get("instances"), list):
        d = d["instances"]
    if not isinstance(d, list) or not all(isinstance(e, dict) and "id" in e for e in d):
        return {"erreur": f"forme inattendue ({type(d).__name__})"}
    return [filtrer(e) for e in d]


def absente(id_instance, appel=_vast):
    """(True, texte) seulement si la liste a été lue sans erreur et ne contient pas l'identifiant."""
    liste = instances(appel)
    if isinstance(liste, dict):
        return False, f"absence NON prouvée : {liste['erreur']}"
    ids = {str(e.get("id")) for e in liste}
    if str(int(id_instance)) in ids:
        return False, f"instance {int(id_instance)} PRÉSENTE"
    return True, f"instance {int(id_instance)} absente d'une liste de {len(liste)} instance(s) lue sans erreur"


def journaux(id_instance, n=40, appel=_vast):
    code, out, err = appel("logs", str(int(id_instance)), "--tail", str(int(n)))
    return out if code == 0 else f"erreur : {_derniere(err, out, code)}"


def creation(texte: str) -> dict:
    try:
        d = json.loads(texte)
    except json.JSONDecodeError:
        return {"erreur": "sortie de création illisible (JSON)", "derniere_ligne": _derniere("", texte, "?")}
    if not isinstance(d, dict):
        return {"erreur": "forme inattendue"}
    return {k: d[k] for k in ("success", "new_contract") if k in d}


def main(argv=None, appel=_vast, env=os.environ, sortie=print, entree=sys.stdin):
    a = list(sys.argv[1:] if argv is None else argv)
    sec = valeurs_secretes(env)
    code = 0
    if a[:1] == ["instance"]:
        texte = json.dumps(instance(a[1], appel), ensure_ascii=False)
    elif a[:1] == ["instances"]:
        texte = json.dumps(instances(appel), ensure_ascii=False)
    elif a[:1] == ["logs"]:
        texte = journaux(a[1], int(a[2]) if len(a) > 2 else 40, appel)
    elif a[:1] == ["absente"]:
        ok, texte = absente(a[1], appel)
        code = 0 if ok else 1
    elif a[:1] == ["creation"]:
        texte = json.dumps(creation(entree.read()), ensure_ascii=False)
    else:
        raise SystemExit(__doc__)
    sortie(balayer(texte, sec))
    return code


if __name__ == "__main__":
    sys.exit(main())
