#!/usr/bin/env python3
"""Agrege les lots Phase 2A par Objet, calcule les clusters de doublons potentiels par TF-IDF/Jaccard, et prepare les entrees des 5 conservateurs Phase 2B."""
from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch")

STOPWORDS = {
    "les", "des", "une", "pour", "dans", "par", "sur", "avec", "sans", "plus", "moins",
    "entre", "contre", "sous", "vers", "chez", "dont", "mais", "donc", "etre", "avoir",
    "fait", "faire", "peut", "sont", "cette", "cet", "ces", "tous", "tout", "toute",
    "toutes", "aux", "qui", "que", "quoi", "comme", "aussi", "ainsi", "apres", "avant",
    "selon", "chaque", "meme", "autre", "autres", "leurs", "leur", "notre", "votre",
    "the", "and", "for", "with", "from", "that", "this", "into", "using", "based",
}

OBJETS_LIST = [
    "OBJ-1_METROLOGIE_ATTELAGE_ET_TESTS_DE_MORT",
    "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
    "OBJ-3_MATHEMATIQUES_NOUVELLES_3_GRAPHES_ET_HORS_ALPHABET",
    "OBJ-4_CONTROLE_IA_MENACES_DIFFUSES_ET_SONDES",
    "OBJ-5_ETALONNAGES_CORPUS_REELS_ET_GPU_8B",
]


def tokenize(text: str) -> list[str]:
    t = text.lower()
    for a, b in (("é", "e"), ("è", "e"), ("ê", "e"), ("ë", "e"), ("à", "a"), ("â", "a"), ("î", "i"), ("ï", "i"), ("ô", "o"), ("ù", "u"), ("û", "u"), ("ç", "c")):
        t = t.replace(a, b)
    toks = re.findall(r"[a-z0-9]{3,}", t)
    return [w for w in toks if w not in STOPWORDS]


def find_near_duplicates(items: list[dict], threshold: float = 0.34, max_pairs: int = 350) -> list[dict]:
    """Trouve les paires de fiches tres proches par cosinus TF-IDF."""
    n = len(items)
    if n < 2:
        return []
    docs = [tokenize(f"{it.get('titre_clair_fr','')} {it.get('titre_clair_fr','')} {it.get('enonce_complet','')[:450]}") for it in items]
    df = Counter()
    for d in docs:
        for w in set(d):
            df[w] += 1
    vecs = []
    norms = []
    inv = defaultdict(list)
    for idx, d in enumerate(docs):
        c = Counter(d)
        v = {}
        for w, cnt in c.items():
            if df[w] > max(3, int(0.45 * n)):
                continue
            idf = math.log((n + 1) / (df[w] + 1)) + 1.0
            v[w] = cnt * idf
        norm = math.sqrt(sum(val * val for val in v.values())) or 1.0
        vecs.append(v)
        norms.append(norm)
        for w in v:
            inv[w].append(idx)

    dot = defaultdict(float)
    for w, idxs in inv.items():
        if len(idxs) > 120:
            continue
        for i_pos in range(len(idxs)):
            i = idxs[i_pos]
            vi = vecs[i][w]
            for j_pos in range(i_pos + 1, len(idxs)):
                j = idxs[j_pos]
                dot[(i, j)] += vi * vecs[j][w]

    pairs = []
    for (i, j), val in dot.items():
        sim = val / (norms[i] * norms[j])
        if sim >= threshold:
            pairs.append((sim, i, j))
    pairs.sort(reverse=True)

    out = []
    for sim, i, j in pairs[:max_pairs]:
        out.append({
            "sim": round(sim, 3),
            "id_a": items[i]["temp_id"],
            "titre_a": items[i]["titre_clair_fr"],
            "n_bib_a": len(items[i]["bib_ids"]),
            "id_b": items[j]["temp_id"],
            "titre_b": items[j]["titre_clair_fr"],
            "n_bib_b": len(items[j]["bib_ids"]),
        })
    return out


def main() -> None:
    master = {
        json.loads(l)["id_unifie"]: json.loads(l)
        for l in (SCRATCH / "corpus_total_enrichi.jsonl").read_text(encoding="utf-8").splitlines()
        if l.strip()
    }
    cur_dir = SCRATCH / "phase2_curated"
    all_idees = []
    all_acquis = []
    all_outils = []
    all_ecarts = []

    seen_bibs = set()
    for cf in sorted(cur_dir.glob("batch_*.json")):
        d = json.loads(cf.read_text(encoding="utf-8"))
        for it in d.get("idees_canoniques", []):
            it = dict(it)
            it["source_batch"] = cf.stem
            all_idees.append(it)
            seen_bibs.update(it["bib_ids"])
        for it in d.get("acquis_et_morts", []):
            it = dict(it)
            it["source_batch"] = cf.stem
            all_acquis.append(it)
            seen_bibs.update(it["bib_ids"])
        for it in d.get("outils_bancs_corpus", []):
            it = dict(it)
            it["source_batch"] = cf.stem
            all_outils.append(it)
            seen_bibs.update(it["bib_ids"])
        for it in d.get("ecartes_structurels", []):
            it = dict(it)
            it["source_batch"] = cf.stem
            all_ecarts.append(it)
            seen_bibs.update(it["bib_ids"])

    missing = sorted(set(master.keys()) - seen_bibs)
    assert not missing, f"Phase 2A has {len(missing)} missing BIB IDs: {missing[:20]}"

    # Assigner des temp_id uniques stables
    for i, it in enumerate(all_idees, 1):
        it["temp_id"] = f"T-IDEE-{i:04d}"
    for i, it in enumerate(all_acquis, 1):
        it["temp_id"] = f"T-ACQ-{i:04d}"
    for i, it in enumerate(all_outils, 1):
        it["temp_id"] = f"T-OUT-{i:04d}"
    for i, it in enumerate(all_ecarts, 1):
        it["temp_id"] = f"T-ECA-{i:04d}"

    # Sauvegarder l'etat complet post-2A
    (SCRATCH / "phase2a_aggregated.json").write_text(
        json.dumps(
            {
                "idees": all_idees,
                "acquis": all_acquis,
                "outils": all_outils,
                "ecarts": all_ecarts,
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )

    out_dir = SCRATCH / "phase2b_inputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    for obj in OBJETS_LIST:
        obj_idees = [x for x in all_idees if x.get("objet") == obj]
        obj_acquis = [x for x in all_acquis if x.get("objet") == obj]
        obj_outils = [x for x in all_outils if x.get("objet") == obj]
        pairs_idees = find_near_duplicates(obj_idees, threshold=0.33, max_pairs=400)
        pairs_acquis = find_near_duplicates(obj_acquis, threshold=0.38, max_pairs=120)
        pairs_outils = find_near_duplicates(obj_outils, threshold=0.38, max_pairs=80)

        compact_idees = [
            {
                "temp_id": x["temp_id"],
                "theme": x.get("theme", ""),
                "sous_theme": x.get("sous_theme", ""),
                "titre_clair_fr": x.get("titre_clair_fr", ""),
                "enonce_resume": x.get("enonce_complet", "")[:320],
                "statut_epistemique": x.get("statut_epistemique", ""),
                "regime_materiel": x.get("regime_materiel", ""),
                "n_bibs": len(x["bib_ids"]),
            }
            for x in obj_idees
        ]
        compact_acquis = [
            {
                "temp_id": x["temp_id"],
                "theme": x.get("theme", ""),
                "titre_clair_fr": x.get("titre_clair_fr", ""),
                "enonce_resume": x.get("enonce_complet", "")[:260],
                "n_bibs": len(x["bib_ids"]),
            }
            for x in obj_acquis
        ]
        compact_outils = [
            {
                "temp_id": x["temp_id"],
                "theme": x.get("theme", ""),
                "titre_clair_fr": x.get("titre_clair_fr", ""),
                "desc_resume": x.get("description_complete", "")[:260],
                "n_bibs": len(x["bib_ids"]),
            }
            for x in obj_outils
        ]
        payload = {
            "objet": obj,
            "counts": {
                "idees": len(obj_idees),
                "acquis": len(obj_acquis),
                "outils": len(obj_outils),
            },
            "near_duplicate_pairs_idees": pairs_idees,
            "near_duplicate_pairs_acquis": pairs_acquis,
            "near_duplicate_pairs_outils": pairs_outils,
            "idees": compact_idees,
            "acquis": compact_acquis,
            "outils": compact_outils,
        }
        (out_dir / f"{obj}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"PHASE 2B INPUT {obj}: idees={len(obj_idees)} (pairs={len(pairs_idees)}), acquis={len(obj_acquis)}, outils={len(obj_outils)}")


if __name__ == "__main__":
    main()
