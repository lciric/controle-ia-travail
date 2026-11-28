#!/usr/bin/env python3
"""Prepare la fusion purement incrementale v1 + LIT-0001..2863 : dedoublonne les papiers externes, detecte par TF-IDF les rattachements aux IDEE-CANON-xxxx de v1, et prepare les entrees <= 38 Ko pour le conservateur v2 (model='inherit')."""
from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

RACINE = Path(r"C:\Users\lciri\wt-organisme-boucle-fermee")
V1_DIR = RACINE / "docs/notes/bibliotheque/catalogue-canonique-v1"
V2_SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch\v2_lit")
CUR_DIR = V2_SCRATCH / "lit_curated"

STOPWORDS = {
    "les", "des", "une", "pour", "dans", "par", "sur", "avec", "sans", "plus", "moins",
    "entre", "contre", "sous", "vers", "chez", "dont", "mais", "donc", "etre", "avoir",
    "fait", "faire", "peut", "sont", "cette", "cet", "ces", "tous", "tout", "toute",
    "toutes", "aux", "qui", "que", "quoi", "comme", "aussi", "ainsi", "apres", "avant",
    "selon", "chaque", "meme", "autre", "autres", "leurs", "leur", "the", "and", "for",
    "with", "from", "that", "this", "using", "based", "llm", "llms", "model", "models",
}


def tokenize(text: str) -> list[str]:
    t = (text or "").lower()
    for a, b in (("é", "e"), ("è", "e"), ("ê", "e"), ("ë", "e"), ("à", "a"), ("â", "a"), ("î", "i"), ("ï", "i"), ("ô", "o"), ("ù", "u"), ("û", "u"), ("ç", "c")):
        t = t.replace(a, b)
    return [w for w in re.findall(r"[a-z0-9]{3,}", t) if w not in STOPWORDS]


def load_jsonl(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def norm_paper_key(p: dict) -> str:
    aid = re.search(r"(\d{4}\.\d{4,5})", str(p.get("identifiant_arxiv_ou_doi", "")))
    if aid:
        return f"arxiv:{aid.group(1)}"
    doi = re.search(r"(10\.\d{4,9}/[^\s,;]+)", str(p.get("identifiant_arxiv_ou_doi", "")))
    if doi:
        return f"doi:{doi.group(1).lower().rstrip('.')}"
    t = re.sub(r"[^a-z0-9]+", " ", (p.get("titre_original") or p.get("titre_clair_fr") or "").lower()).strip()
    return f"title:{t[:90]}"


def main() -> None:
    lit_master = {r["id_supplement"]: r for r in load_jsonl(V2_SCRATCH / "supplement-litterature-et-lectures-v1.jsonl")}
    v1_idees = load_jsonl(V1_DIR / "idees-et-mecanismes-canoniques.jsonl")

    # 1. Agreger toutes les sorties lit_curated/*.json et verifier 0 orphelin sur LIT
    papers_by_key: dict[str, dict] = {}
    cand_idees: list[dict] = []
    cand_acquis: list[dict] = []
    cand_outils: list[dict] = []
    cand_ecarts: list[dict] = []
    covered_lit = set()

    for cf in sorted(CUR_DIR.glob("lit_batch_*.json")):
        d = json.loads(cf.read_text(encoding="utf-8"))
        for p in d.get("litterature_et_voisins") or []:
            covered_lit.update(p["lit_ids"])
            pk = norm_paper_key(p)
            if pk not in papers_by_key:
                papers_by_key[pk] = dict(p)
                papers_by_key[pk]["lit_ids"] = list(dict.fromkeys(p["lit_ids"]))
            else:
                ex = papers_by_key[pk]
                ex["lit_ids"] = list(dict.fromkeys(ex["lit_ids"] + p["lit_ids"]))
                if p.get("statut_lecture") == "lu_sur_pdf_entier":
                    ex["statut_lecture"] = "lu_sur_pdf_entier"
                for fld in ("dispositif", "chiffres_cles", "echecs_et_limites_temoins_negatifs", "lien_avec_nos_revendications"):
                    nv = str(p.get(fld, "")).strip()
                    ov = str(ex.get(fld, "")).strip()
                    if nv and nv not in ov:
                        ex[fld] = f"{ov} ; {nv}".strip(" ;") if ov else nv
        for it in d.get("idees_candidates") or []:
            covered_lit.update(it["lit_ids"])
            cand_idees.append(dict(it))
        for it in d.get("acquis_et_morts") or []:
            covered_lit.update(it["lit_ids"])
            cand_acquis.append(dict(it))
        for it in d.get("outils_bancs_corpus") or []:
            covered_lit.update(it["lit_ids"])
            cand_outils.append(dict(it))
        for it in d.get("ecartes_structurels") or []:
            covered_lit.update(it["lit_ids"])
            cand_ecarts.append(dict(it))

    missing_lit = sorted(set(lit_master.keys()) - covered_lit)
    assert not missing_lit, f"LIT curation missing {len(missing_lit)} IDs: {missing_lit[:20]}"

    papers_list = list(papers_by_key.values())
    for i, p in enumerate(papers_list, 1):
        p["temp_lit_id"] = f"T-PAP-{i:04d}"
    for i, it in enumerate(cand_idees, 1):
        it["temp_id"] = f"T-LIDEE-{i:04d}"
    for i, it in enumerate(cand_acquis, 1):
        it["temp_id"] = f"T-LACQ-{i:04d}"
    for i, it in enumerate(cand_outils, 1):
        it["temp_id"] = f"T-LOUT-{i:04d}"

    # 2. Index TF-IDF des IDEE-CANON-xxxx de v1 pour proposer des rattachements exacts (LIT -> IDEE-CANON v1)
    v1_docs = [tokenize(f"{x['titre_clair_fr']} {x['titre_clair_fr']} {x['enonce_complet'][:500]} {x.get('anteriorite_connue','')}") for x in v1_idees]
    df = Counter()
    for d in v1_docs:
        for w in set(d):
            df[w] += 1
    n_v1 = len(v1_idees)
    v1_vecs, v1_norms = [], []
    inv = defaultdict(list)
    for idx, d in enumerate(v1_docs):
        c = Counter(d)
        v = {w: cnt * (math.log((n_v1 + 1) / (df[w] + 1)) + 1.0) for w, cnt in c.items() if df[w] <= max(3, int(0.35 * n_v1))}
        norm = math.sqrt(sum(val * val for val in v.values())) or 1.0
        v1_vecs.append(v)
        v1_norms.append(norm)
        for w in v:
            inv[w].append(idx)

    def top_v1_matches(text: str, k: int = 3, min_sim: float = 0.28) -> list[dict]:
        toks = tokenize(text)
        c = Counter(toks)
        q = {w: cnt * (math.log((n_v1 + 1) / (df[w] + 1)) + 1.0) for w, cnt in c.items() if w in inv}
        qn = math.sqrt(sum(val * val for val in q.values())) or 1.0
        scores = defaultdict(float)
        for w, qv in q.items():
            for idx in inv[w]:
                scores[idx] += qv * v1_vecs[idx][w]
        ranked = sorted(((sc / (qn * v1_norms[idx]), idx) for idx, sc in scores.items()), reverse=True)
        return [
            {
                "v1_id": v1_idees[idx]["id_canonique"],
                "v1_titre": v1_idees[idx]["titre_clair_fr"],
                "sim": round(sim, 3),
            }
            for sim, idx in ranked[:k]
            if sim >= min_sim
        ]

    # Match cand_idees against v1_idees AND against each other
    v1_match_candidates = []
    for it in cand_idees:
        ms = top_v1_matches(f"{it['titre_clair_fr']} {it['titre_clair_fr']} {it['enonce_complet'][:450]} {it.get('anteriorite_et_voisins_a_citer','')}", k=2, min_sim=0.30)
        if ms:
            v1_match_candidates.append({
                "temp_id": it["temp_id"],
                "origine_type": it["origine_type"],
                "titre": it["titre_clair_fr"],
                "objet": it["objet"],
                "n_lits": len(it["lit_ids"]),
                "v1_matches": ms,
            })

    # Match papers against v1_idees (for anteriorite_et_voisins_a_citer enrichment on v1 ideas!)
    paper_v1_links = []
    for p in papers_list:
        ms = top_v1_matches(f"{p['titre_clair_fr']} {p['titre_original']} {p['dispositif']} {p['lien_avec_nos_revendications']}", k=3, min_sim=0.26)
        if ms:
            paper_v1_links.append({
                "temp_lit_id": p["temp_lit_id"],
                "titre_original": p["titre_original"],
                "arxiv_doi": p["identifiant_arxiv_ou_doi"],
                "statut_lecture": p["statut_lecture"],
                "v1_matches": ms,
            })

    # Near-duplicate pairs among cand_idees themselves
    n_c = len(cand_idees)
    c_docs = [tokenize(f"{x['titre_clair_fr']} {x['titre_clair_fr']} {x['enonce_complet'][:350]}") for x in cand_idees]
    c_df = Counter(w for d in c_docs for w in set(d))
    c_vecs, c_norms, c_inv = [], [], defaultdict(list)
    for idx, d in enumerate(c_docs):
        c = Counter(d)
        v = {w: cnt * (math.log((n_c + 1) / (c_df[w] + 1)) + 1.0) for w, cnt in c.items() if c_df[w] <= max(3, int(0.35 * n_c))}
        norm = math.sqrt(sum(val * val for val in v.values())) or 1.0
        c_vecs.append(v)
        c_norms.append(norm)
        for w in v:
            c_inv[w].append(idx)
    c_dot = defaultdict(float)
    for w, idxs in c_inv.items():
        if len(idxs) > 100:
            continue
        for i_p in range(len(idxs)):
            i = idxs[i_p]
            for j_p in range(i_p + 1, len(idxs)):
                j = idxs[j_p]
                c_dot[(i, j)] += c_vecs[i][w] * c_vecs[j][w]
    c_pairs = sorted(((val / (c_norms[i] * c_norms[j]), i, j) for (i, j), val in c_dot.items()), reverse=True)
    intra_lit_dups = [
        {
            "sim": round(sim, 3),
            "id_a": cand_idees[i]["temp_id"],
            "titre_a": cand_idees[i]["titre_clair_fr"],
            "id_b": cand_idees[j]["temp_id"],
            "titre_b": cand_idees[j]["titre_clair_fr"],
        }
        for sim, i, j in c_pairs[:250]
        if sim >= 0.38
    ]

    agg = {
        "papers": papers_list,
        "cand_idees": cand_idees,
        "cand_acquis": cand_acquis,
        "cand_outils": cand_outils,
        "cand_ecarts": cand_ecarts,
        "paper_v1_links_auto": paper_v1_links,
    }
    (V2_SCRATCH / "v2_lit_aggregated.json").write_text(json.dumps(agg, ensure_ascii=False, indent=1), encoding="utf-8")

    # Ecrire fichiers <= 36 Ko pour le conservateur v2 (model="inherit")
    p_dir = V2_SCRATCH / "conservator_inputs"
    p_dir.mkdir(parents=True, exist_ok=True)
    for old in p_dir.glob("*.json"):
        old.unlink()

    files_written = []
    # Chunk v1_match_candidates
    cur, idx_f = [], 1
    for m in sorted(v1_match_candidates, key=lambda x: -x["v1_matches"][0]["sim"]):
        cand = cur + [m]
        if cur and len(json.dumps(cand, ensure_ascii=False).encode("utf-8")) > 35000:
            fp = p_dir / f"01_v1_matches_{idx_f:02d}.json"
            fp.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8")
            files_written.append(str(fp))
            idx_f += 1
            cur = [m]
        else:
            cur = cand
    if cur:
        fp = p_dir / f"01_v1_matches_{idx_f:02d}.json"
        fp.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8")
        files_written.append(str(fp))

    fp_dups = p_dir / "02_intra_lit_dups.json"
    fp_dups.write_text(json.dumps({
        "counts": {
            "v1_idees": len(v1_idees),
            "lit_papers_dedup": len(papers_list),
            "lit_cand_idees": len(cand_idees),
            "lit_cand_acquis": len(cand_acquis),
            "lit_cand_outils": len(cand_outils),
            "lit_cand_ecarts": len(cand_ecarts),
            "v1_match_candidates": len(v1_match_candidates),
            "paper_v1_links_auto": len(paper_v1_links),
        },
        "intra_lit_dups": intra_lit_dups[:160],
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    files_written.append(str(fp_dups))

    (V2_SCRATCH / "conservator_manifest.json").write_text(json.dumps({"files": files_written}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"V2 CONSERVATOR INPUTS READY: papers={len(papers_list)}, cand_idees={len(cand_idees)}, v1_matches={len(v1_match_candidates)}, intra_dups={len(intra_lit_dups)}, files={len(files_written)}")


if __name__ == "__main__":
    main()
