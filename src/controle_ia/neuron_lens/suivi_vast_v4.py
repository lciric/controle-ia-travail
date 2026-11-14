"""Suivi d'une instance du loueur sans jamais restituer un secret — v4 (contre-lecture 9 : P-5, P-7 ; docstring des secrets courts).

v4 : `instance`, `instances` et `logs` rendent le code 1 quand le résultat porte une erreur (et `instance` aussi sur « forme
inattendue ») ; `absente … --non-vide` exige une liste non vide (une liste vide reste une absence prouvée sans cette option, ce qui est
légitime quand plus aucune instance n'existe sur le compte).

`vastai show instance(s) --raw` restitue la configuration de l'instance, dont les variables d'environnement passées à la création
(le jeton du programme). Ce module appelle l'outil, ne garde que des champs sans secret, et refuse d'imprimer toute sortie qui
contiendrait la valeur d'une variable secrète de la session (lue par son nom, jamais affichée), sous sa forme brute, encodée pour une
adresse, ou en base 64 standard ou « url-safe » (seule ou dans l'en-tête `x-access-token:<jeton>`, aux trois alignements possibles
dans un flux plus large). Limites déclarées : base 64 coupée en lignes non détectée ; pour un secret de 8 à 10 octets, aucun fragment
base 64 de la valeur seule (formes brute, adresse et en-tête seulement), de 11 à 13 octets, un fragment sur certains alignements
seulement ; la forme en en-tête `x-access-token:<secret>` est toujours couverte.

v3 : (N-2) une sortie vide ou blanche au code 0 est une erreur, jamais une absence ni une liste vide ; seul le texte JSON `[]` est une
liste vide ; `absente` accepte un témoin de lecture (`--temoin <ID>` : une instance qui doit figurer dans la liste) ; (N-9 a)
`show instance` enveloppé (`{"instances": {…}}` ou liste) déballé ; (N-9 b) délai dépassé signalé comme erreur ; (N-9 c) `creation`
extrait `new_contract` par motif si la sortie n'est pas du JSON pur ; (N-5) commande `verifier` : essai de lecture gratuit avant la
location (variable exigée, outil trouvé, liste lisible, absence d'un identifiant bidon). v2 : contre-lecture 7 (variable exigée,
formes encodées, forme inattendue, outil introuvable, `absente`, `creation`).

Usage : `python -m controle_ia.neuron_lens.suivi_vast_v4 instance <ID>` | `instances` | `logs <ID> [N]` |
`absente <ID> [--temoin <ID>] [--non-vide]` | `verifier` | `creation < sortie_de_la_creation` (sortie `--raw 2>&1` de l'outil)
"""
from __future__ import annotations

import base64
import json
import os
import re
import subprocess
import sys
from urllib.parse import quote

SECRETS = ("CONTROLE_IA_GITHUB_TOKEN_2", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY", "HF_TOKEN")
EXIGEE = "CONTROLE_IA_GITHUB_TOKEN_2"
CHAMPS = ("id", "label", "actual_status", "cur_state", "intended_status", "dph_total", "gpu_name", "start_date", "status_msg")
MIN_FORME = 12  # longueur minimale d'un fragment base 64 balayé
ID_BIDON = 1  # identifiant d'instance qui n'existe pas (essai de lecture de `verifier`)


def _b64_fragments(charge: bytes):
    """Fragments base 64 de `charge` qui ne dépendent que d'elle, pour chacun des trois alignements dans un flux plus large."""
    for k in range(3):
        enc = base64.b64encode(b"\0" * k + charge).decode().rstrip("=")
        frag = enc[(0, 2, 3)[k]:len(enc) - 3]  # début : caractères touchés par le remplissage ; fin : par les octets suivants
        if len(frag) >= MIN_FORME:
            yield frag
            yield frag.replace("+", "-").replace("/", "_")  # « url-safe »


def formes(valeur: str):
    """Formes cherchées pour une valeur secrète : brute, adresse, base 64 standard et « url-safe » (seule et en en-tête)."""
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
    except subprocess.TimeoutExpired:
        return 124, "", "délai de 120 s dépassé"
    return p.returncode, p.stdout, p.stderr


def _derniere(err, out, code):
    t = (err or out or "").strip()
    return t.splitlines()[-1][:200] if t else f"code {code}"


def _lire_json(code, out, err):
    """(objet, None) ou (None, erreur) : code non nul, sortie vide ou blanche, JSON illisible = erreur."""
    if code != 0:
        return None, _derniere(err, out, code)
    if not (out or "").strip():
        return None, "sortie vide au code 0 (jamais lue comme une absence)"
    try:
        return json.loads(out), None
    except json.JSONDecodeError:
        return None, "sortie illisible (JSON)"


def instance(id_instance, appel=_vast):
    ident = int(id_instance)
    d, e = _lire_json(*appel("show", "instance", str(ident), "--raw"))
    if e:
        return {"erreur": e}
    if isinstance(d, dict) and "instances" in d:
        d = d["instances"]
    if isinstance(d, list):
        d = [x for x in d if isinstance(x, dict) and str(x.get("id")) == str(ident)]
        if not d:
            return {"absente": True}
        d = d[0]
    if d in ({}, None):
        return {"absente": True}
    if isinstance(d, dict) and "id" in d:
        return filtrer(d)
    return {"erreur": f"forme inattendue ({type(d).__name__})"}


def instances(appel=_vast):
    """Liste filtrée, ou dictionnaire `{"erreur": …}` (qui n'est jamais une preuve d'absence)."""
    d, e = _lire_json(*appel("show", "instances", "--raw"))
    if e:
        return {"erreur": e}
    if isinstance(d, dict) and isinstance(d.get("instances"), list):
        d = d["instances"]
    if not isinstance(d, list) or not all(isinstance(x, dict) and "id" in x for x in d):
        return {"erreur": f"forme inattendue ({type(d).__name__})"}
    return [filtrer(x) for x in d]


def absente(id_instance, appel=_vast, temoin=None, non_vide=False):
    """(True, texte) seulement si la liste a été lue sans erreur, contient le témoin (s'il est donné), n'est pas vide (si `non_vide`)
    et ne contient pas l'identifiant."""
    liste = instances(appel)
    if isinstance(liste, dict):
        return False, f"absence NON prouvée : {liste['erreur']}"
    if non_vide and not liste:
        return False, "absence NON prouvée : liste vide (option --non-vide)"
    ids = {str(x.get("id")) for x in liste}
    if temoin is not None and str(int(temoin)) not in ids:
        return False, f"absence NON prouvée : témoin {int(temoin)} absent de la liste ({len(liste)} instance(s))"
    if str(int(id_instance)) in ids:
        return False, f"instance {int(id_instance)} PRÉSENTE"
    t = f" ; témoin {int(temoin)} présent" if temoin is not None else ""
    return True, f"instance {int(id_instance)} absente d'une liste de {len(liste)} instance(s) lue sans erreur{t}"


def verifier(appel=_vast):
    """Essai de lecture avant la location : (True, texte) si la liste se lit et si l'identifiant bidon est prouvé absent."""
    liste = instances(appel)
    if isinstance(liste, dict):
        return False, f"suivi NON prêt : {liste['erreur']}"
    ok, t = absente(ID_BIDON, appel)
    return ok, f"suivi prêt : liste de {len(liste)} instance(s) lue ; {t}" if ok else f"suivi NON prêt : {t}"


def journaux(id_instance, n=40, appel=_vast):
    code, out, err = appel("logs", str(int(id_instance)), "--tail", str(int(n)))
    return out if code == 0 else f"erreur : {_derniere(err, out, code)}"


MOTIF_CONTRAT = re.compile(r"""["']?new_contract["']?\s*[:=]\s*(\d+)""")


def creation(texte: str) -> dict:
    try:
        d = json.loads(texte)
    except json.JSONDecodeError:
        m = MOTIF_CONTRAT.search(texte)
        if m:
            return {"new_contract": int(m.group(1)), "extrait_par_motif": True}
        return {"erreur": "sortie de création illisible (JSON)", "derniere_ligne": _derniere("", texte, "?")}
    if not isinstance(d, dict):
        return {"erreur": "forme inattendue"}
    return {k: d[k] for k in ("success", "new_contract") if k in d}


def main(argv=None, appel=_vast, env=os.environ, sortie=print, entree=sys.stdin):
    a = list(sys.argv[1:] if argv is None else argv)
    sec = valeurs_secretes(env)
    code = 0
    if a[:1] == ["instance"]:
        r = instance(a[1], appel)
        texte = json.dumps(r, ensure_ascii=False)
        code = 1 if "erreur" in r else 0
    elif a[:1] == ["instances"]:
        r = instances(appel)
        texte = json.dumps(r, ensure_ascii=False)
        code = 1 if isinstance(r, dict) else 0
    elif a[:1] == ["logs"]:
        code_l, out, err = appel("logs", str(int(a[1])), "--tail", str(int(a[2]) if len(a) > 2 else 40))
        texte = out if code_l == 0 else f"erreur : {_derniere(err, out, code_l)}"
        code = 0 if code_l == 0 else 1
    elif a[:1] == ["absente"]:
        temoin = int(a[a.index("--temoin") + 1]) if "--temoin" in a else None
        ok, texte = absente(a[1], appel, temoin, non_vide="--non-vide" in a)
        code = 0 if ok else 1
    elif a[:1] == ["verifier"]:
        ok, texte = verifier(appel)
        code = 0 if ok else 1
    elif a[:1] == ["creation"]:
        r = creation(entree.read())
        texte = json.dumps(r, ensure_ascii=False)
        code = 0 if "new_contract" in r else 1
    else:
        raise SystemExit(__doc__)
    sortie(balayer(texte, sec))
    return code


if __name__ == "__main__":
    sys.exit(main())
