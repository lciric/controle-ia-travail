"""Contrôle préalable de R1, hors carte : part des actions de P3 dont le texte stocké, tokenisé seul, redonne exactement
le nombre de jetons notés par P3 (`jetons_notes`) et le texte au décodage (« conformes »), et part de celles dont toutes
les actions précédentes de l'épisode le sont aussi (« contexte exact »). Tokeniseur : `tokenizer.json` de
Llama-3.1-8B-Instruct, empreinte exigée 79e3e522… (celle que cite `prereg/P3-consignes-v1.md`).

    PYTHONPATH=src python docs/notes/runs-r1-r2-r4-v1/controle_prealable_tokenisation_v1.py <dossier du tokeniseur>
"""
import hashlib
import sys
from pathlib import Path

import numpy as np
from transformers import AutoTokenizer

from controle_ia.harnais.formats import _ids
from controle_ia.runs_nuit.alignement_v1 import charger_identite, charger_textes_alignes

EMPREINTE = "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"
dossier = Path(sys.argv[1])
if hashlib.sha256((dossier / "tokenizer.json").read_bytes()).hexdigest() != EMPREINTE:
    raise SystemExit("tokenizer.json : empreinte ≠ 79e3e522… (tokeniseur de P3)")
tok = AutoTokenizer.from_pretrained(str(dossier))
d = "donnees/20261019-230011-p3-reel/"
ident = charger_identite(d + "scores-p3.npz", "968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf")
lignes = charger_textes_alignes(d + "textes-actions-p3.jsonl", ident,
                                "ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284")
J, JN = np.asarray(ident["jetons"]), np.asarray(ident["jetons_notes"])
fin = tok.convert_tokens_to_ids("<|eot_id|>")
conf = np.zeros(len(lignes), bool)
for i, x in enumerate(lignes):
    n = _ids(tok, x["texte"]) if x["texte"] else []
    nv = n + ([fin] if J[i] - JN[i] == 1 else [])
    conf[i] = len(n) == JN[i] and tok.decode(nv, skip_special_tokens=True) == x["texte"]
ctx = np.zeros_like(conf)
for k in range(0, len(lignes), 10):
    tous = True
    for j in range(10):
        tous = tous and conf[k + j]
        ctx[k + j] = tous
cond = np.asarray(ident["condition"])
print(f"conformes {int(conf.sum())} / {len(conf)} ; contexte exact {int(ctx.sum())} / {len(conf)}")
for c in ("honnete", "saboteur", "temoin", "mention"):
    m = cond == c
    print(f"  {c} : conformes {int(conf[m].sum())} / {int(m.sum())} ; contexte exact {int(ctx[m].sum())} / {int(m.sum())}")
