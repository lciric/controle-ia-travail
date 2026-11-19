"""Comptes faits avant scellement, sur le texte seul (aucun modèle, aucune activation, aucune lentille) — v1.

Pour le texte gelé de la tranche de l'ajustement de nos lentilles (B-β), brouillon 2. Recompte, sans exécuter le code
voisin, ce que `neuron_lens/corpus.py` (`_rows`, `lens_docs`, commit 849bfe16) ferait des lignes 0 à 999 de DCLM :
chaque document coupé à max(4000, 8 × 128) caractères, encodé avec les jetons spéciaux (jeton de début compris), coupé à
128 jetons ; « plein » = exactement 128 jetons (`--full-length`) ; « gardé par défaut » = au moins SKIP_FIRST + 2 = 18.
Vérifie : identifiants et ordre égaux à la provenance publiée `dclm.provenance.json` ; aucun identifiant commun avec
`act-dclm.provenance.json` ; empreinte du tokeniseur.

    python -I comptes_corpus_ajustement_b_beta_v1.py TOKENIZER_JSON DCLM_PROV ACT_DCLM_PROV SORTIE_JSON
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
SEQ, SKIP_FIRST, CHARS = 128, 16, max(4000, 8 * 128)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main(tok_path, prov_path, act_path, out_path):
    if sha(tok_path) != SHA_TOKENISEUR:
        sys.exit("ARRET : empreinte du tokeniseur différente")
    tok = Tokenizer.from_file(tok_path)
    prov, act = json.load(open(prov_path)), json.load(open(act_path))
    if prov["revision"] != REVISION or act["revision"] != REVISION:
        sys.exit("ARRET : révision différente")
    pf = pq.ParquetFile(HfFileSystem().open(FICHIER, "rb"))
    rows = []
    for g in range(pf.num_row_groups):
        t = pf.read_row_group(g, columns=["text", "id"]).to_pylist()
        rows.extend(t)
        if len(rows) >= 1000:
            break
    rows = rows[:1000]
    ids = [r["id"] for r in rows]
    if ids != prov["ids"]:
        sys.exit("ARRET : identifiants ou ordre différents de la provenance publiée")
    if [len(r["text"]) for r in rows] != prov["chars"]:
        sys.exit("ARRET : longueurs en caractères différentes de la provenance publiée")
    commun = sorted(set(ids) & set(act["ids"]))
    lens = [len(tok.encode(r["text"][:CHARS]).ids[:SEQ]) for r in rows]
    bos = tok.encode("x").ids[0]
    pleins = [i for i, n in enumerate(lens) if n == SEQ]
    courts = [(i, ids[i], n) for i, n in enumerate(lens) if n < SEQ]
    out = {
        "outil": "comptes_corpus_ajustement_b_beta_v1.py", "revision_dclm": REVISION, "fichier": FICHIER,
        "sha256_tokeniseur": SHA_TOKENISEUR, "jeton_de_debut": bos,
        "sha256_dclm_provenance": sha(prov_path), "sha256_act_dclm_provenance": sha(act_path),
        "lignes": [0, 1000], "identifiants_egaux_a_la_provenance": True,
        "identifiants_communs_avec_act_dclm": len(commun), "act_dclm_skip": act["skip"], "act_dclm_n": act["n"],
        "n_pleins_128": len(pleins), "n_gardes_par_defaut_18": sum(n >= SKIP_FIRST + 2 for n in lens),
        "n_courts": len(courts), "moities_pleins": [len(pleins[0::2]), len(pleins[1::2])],
        "positions_par_document_reference": sum(max(0, n - SKIP_FIRST) for n in lens if n >= SKIP_FIRST + 2),
        "positions_pleins": len(pleins) * (SEQ - SKIP_FIRST),
        "documents_courts": [{"ligne": i, "id": d, "jetons": n} for i, d, n in courts],
        "sha256_lignes_pleines": hashlib.sha256(repr(pleins).encode()).hexdigest(),
    }
    json.dump(out, open(out_path, "w"), indent=1, ensure_ascii=False)
    print({k: v for k, v in out.items() if k != "documents_courts"})


if __name__ == "__main__":
    main(*sys.argv[1:5])
