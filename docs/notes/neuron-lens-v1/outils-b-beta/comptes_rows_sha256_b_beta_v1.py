"""Complément des comptes avant scellement (v1) : empreinte `rows_sha256` attendue du corpus d'ajustement.

Recalcule `neuron_lens.corpus.rows_sha256` (sha256 de `repr([list(r) for r in rows])`, commit 849bfe16, l. 62-64) sur les lignes
que `lens_docs(..., n=1000, seq_len=128, min_len=18, full=True)` garderait (documents pleins de 128 jetons, lignes 0 à 999), et,
pour mémoire, sur celles du défaut publié (`full=False`). Même lecture des lignes et même tokeniseur que
`comptes_corpus_ajustement_b_beta_v1.py` ; aucun modèle.

    python -I comptes_rows_sha256_b_beta_v1.py TOKENIZER_JSON DCLM_PROV SORTIE_JSON
"""
import hashlib
import json
import sys

import pyarrow.parquet as pq
from huggingface_hub import HfFileSystem
from tokenizers import Tokenizer

REVISION = "2fa015e4044ec442a0734e89658cdcc538d10dd4"
FICHIER = f"datasets/HuggingFaceFW/dclm_100BT-shuffled@{REVISION}/data/train-00000-of-00100.parquet"
SHA_TOKENISEUR = "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"
SEQ, MIN_LEN, CHARS = 128, 18, max(4000, 8 * 128)


def main(tok_path, prov_path, out_path):
    if hashlib.sha256(open(tok_path, "rb").read()).hexdigest() != SHA_TOKENISEUR:
        sys.exit("ARRET : empreinte du tokeniseur différente")
    tok, prov = Tokenizer.from_file(tok_path), json.load(open(prov_path))
    pf = pq.ParquetFile(HfFileSystem().open(FICHIER, "rb"))
    rows = []
    for g in range(pf.num_row_groups):
        rows.extend(pf.read_row_group(g, columns=["text", "id"]).to_pylist())
        if len(rows) >= 1000:
            break
    rows = rows[:1000]
    if [r["id"] for r in rows] != prov["ids"]:
        sys.exit("ARRET : identifiants ou ordre différents de la provenance publiée")
    toks = [tok.encode(r["text"][:CHARS]).ids[:SEQ] for r in rows]
    plein = [t for t in toks if len(t) == SEQ]
    defaut = [t for t in toks if len(t) >= MIN_LEN]
    h = lambda rr: hashlib.sha256(repr([list(r) for r in rr]).encode("utf-8")).hexdigest()
    out = {"outil": "comptes_rows_sha256_b_beta_v1.py", "revision_dclm": REVISION, "sha256_tokeniseur": SHA_TOKENISEUR,
           "full_length": {"docs": len(plein), "rows_sha256": h(plein), "moitie_paire": h(plein[0::2]),
                           "moitie_impaire": h(plein[1::2])},
           "defaut_publie": {"docs": len(defaut), "rows_sha256": h(defaut)}}
    json.dump(out, open(out_path, "w"), indent=1)
    print(out)


if __name__ == "__main__":
    main(*sys.argv[1:4])
