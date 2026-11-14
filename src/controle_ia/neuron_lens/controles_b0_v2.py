"""Contrôles de B0 de « Neuron Lens » sans modèle — v2 (remplace la v1 après sa contre-lecture,
`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-1-correctif-chat-v1.md` ; retouches non relues ensuite, déclaré).

Met en œuvre trois gardes de la liste d'arrêt du texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`
(`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`) et de l'addendum des empreintes
(`docs/notes/neuron-lens-v1/addendum-empreintes-v3.md`, `e63d95caa06fde0cb23d2b0dbcd143413d822be9487edf8f54fe72b46db0df82`) :
1. `verifier_provenances` : les provenances écrites par `05_act_corpus.py` après la passe de Llama ont la révision, le nombre de lignes et la
   liste d'identifiants des provenances **du dépôt voisin** (pour « chat » : celle de Qwen3-8B), jamais le fichier déposé avant la passe.
   **Les références se lisent avant la passe, ou par `git show 849bfe16:data/corpus/<fichier>`, jamais dans l'arbre après la passe** :
   `05_act_corpus.py` réécrit sur place `act-dclm`, `act-zh`, `act-code` et la provenance « chat » de Llama ;
2. `empreinte_liste_gardee` : empreinte de la liste `catalog.kept` (identifiants triés, un par ligne, ASCII, retour à la ligne final), à
   comparer à `cd8a6c23…` ;
3. `compter_debuts` : nombre de jetons de début par document (signalé : double jeton de début possible dans la tranche « chat » de Llama).
Chaque contrôle rend une liste de problèmes (vide si tout va bien) ; l'appelant arrête la course sur toute liste non vide.
"""
from __future__ import annotations

import hashlib

EMPREINTE_KEPT_QWEN3 = "cd8a6c236cb1bd4a9ed16bf7981104457ae5f1fea65fe16bb7d902aa86307ac7"
TRANCHES = ("dclm", "zh", "code", "chat")


def verifier_provenances(produites: dict, references: dict) -> list[str]:
    """`produites[tranche]` et `references[tranche]` : contenus JSON des fichiers de provenance (dict). Comparés : `repo`, `config`,
    `split`, `revision`, `skip`, `n`, `ids` (dans l'ordre)."""
    pb = []
    for t in TRANCHES:
        if t not in produites or t not in references:
            pb.append(f"{t} : provenance absente")
            continue
        p, r = produites[t], references[t]
        for k in ("repo", "config", "split", "revision", "skip", "n", "ids"):
            if k not in p:
                pb.append(f"{t} : clé {k} absente de la provenance produite")
            if k not in r:
                pb.append(f"{t} : clé {k} absente de la référence")
        for k in ("repo", "config", "split", "revision", "skip", "n"):
            if k in p and k in r and p[k] != r[k]:
                pb.append(f"{t} : {k} {p.get(k)!r} ≠ {r.get(k)!r}")
        if list(p.get("ids", [])) != list(r.get("ids", [])):
            pb.append(f"{t} : liste des identifiants de lignes différente")
        if r.get("n") != len(r.get("ids", [])):
            pb.append(f"{t} : référence incohérente (n ≠ nombre d'identifiants)")
    return pb


def empreinte_liste_gardee(ids) -> str:
    ids = sorted(int(i) for i in ids)
    if len(set(ids)) != len(ids):
        raise ValueError("doublon dans la liste gardée")
    return hashlib.sha256("".join(f"{i}\n" for i in ids).encode("ascii")).hexdigest()


def compter_debuts(documents, bos_id: int) -> dict:
    """`documents` : listes d'identifiants de jetons. Rend {nombre de jetons de début en tête : nombre de documents} (0 pour un document
    vide ou sans jeton de début)."""
    comptes = {}
    for d in documents:
        k = 0
        while k < len(d) and d[k] == bos_id:
            k += 1
        comptes[k] = comptes.get(k, 0) + 1
    return comptes
