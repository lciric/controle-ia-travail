"""Suivi d'une instance du loueur sans jamais restituer un secret — v1 (contre-lecture de la commande v4, remarque 1).

`vastai show instance(s) --raw` restitue la configuration de l'instance, dont les variables d'environnement passées à la création
(le jeton du programme). Ce module appelle l'outil, ne garde que des champs sans secret, et refuse d'imprimer toute sortie qui
contiendrait la valeur d'une variable secrète de la session (lue par son nom, jamais affichée) : balayage sur chaque sortie.

Usage : `python -m controle_ia.neuron_lens.suivi_vast_v1 instance <ID>` | `instances` | `logs <ID> [N]`
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

SECRETS = ("CONTROLE_IA_GITHUB_TOKEN_2", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY", "HF_TOKEN")
CHAMPS = ("id", "label", "actual_status", "cur_state", "intended_status", "dph_total", "gpu_name", "start_date", "status_msg")


def valeurs_secretes(env=os.environ):
    return [env[k] for k in SECRETS if len(env.get(k, "")) >= 8]


def balayer(texte: str, secrets) -> str:
    """Rend le texte s'il ne contient aucun secret ; sinon lève (rien n'est imprimé)."""
    if any(s in texte for s in secrets):
        raise SystemExit("sortie refusée : elle contient la valeur d'une variable secrète")
    return texte


def filtrer(d: dict) -> dict:
    return {k: d.get(k) for k in CHAMPS if k in d}


def _vast(*args, outil="vastai"):
    p = subprocess.run([outil, *args], capture_output=True, text=True, timeout=120)
    return p.returncode, p.stdout, p.stderr


def instance(id_instance, appel=_vast):
    code, out, err = appel("show", "instance", str(int(id_instance)), "--raw")
    if code != 0:
        return {"erreur": (err or out).strip().splitlines()[-1][:200] if (err or out).strip() else f"code {code}"}
    d = json.loads(out) if out.strip() else {}
    return filtrer(d) if d else {"absente": True}


def instances(appel=_vast):
    code, out, err = appel("show", "instances", "--raw")
    if code != 0:
        return {"erreur": f"code {code}"}
    return [filtrer(d) for d in json.loads(out or "[]")]


def journaux(id_instance, n=40, appel=_vast):
    code, out, err = appel("logs", str(int(id_instance)), "--tail", str(int(n)))
    return out if code == 0 else f"erreur code {code}"


def main(argv=None, appel=_vast, env=os.environ, sortie=print):
    a = list(sys.argv[1:] if argv is None else argv)
    sec = valeurs_secretes(env)
    if a[:1] == ["instance"]:
        texte = json.dumps(instance(a[1], appel), ensure_ascii=False)
    elif a[:1] == ["instances"]:
        texte = json.dumps(instances(appel), ensure_ascii=False)
    elif a[:1] == ["logs"]:
        texte = journaux(a[1], int(a[2]) if len(a) > 2 else 40, appel)
    else:
        raise SystemExit(__doc__)
    sortie(balayer(texte, sec))


if __name__ == "__main__":
    main()
