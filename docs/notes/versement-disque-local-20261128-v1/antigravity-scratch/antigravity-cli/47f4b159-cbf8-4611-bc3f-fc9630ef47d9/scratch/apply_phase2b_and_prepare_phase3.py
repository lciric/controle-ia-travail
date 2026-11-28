#!/usr/bin/env python3
"""Applique les decisions des 5 conservateurs Phase 2B et prepare les candidats inter-rayons pour Phase 3."""
from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch")

VALID_OBJETS = {
    "OBJ-1_METROLOGIE_ATTELAGE_ET_TESTS_DE_MORT",
    "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION",
    "OBJ-3_MATHEMATIQUES_NOUVELLES_3_GRAPHES_ET_HORS_ALPHABET",
    "OBJ-4_CONTROLE_IA_MENACES_DIFFUSES_ET_SONDES",
    "OBJ-5_ETALONNAGES_CORPUS_REELS_ET_GPU_8B",
}

VALID_STATUTS = {
    "vierge", "preenregistre_en_attente", "pris_en_charge_groupe_v1",
    "deja_valide_interne", "deja_refute_interne",
}

VALID_REGIMES = {
    "CPU_0_USD_SYNTHETIQUE", "CPU_DONNEES_PUBLIQUES_REEL",
    "GPU_VAST_8B_SOUS_GO", "MODELE_FERME_COURSE_ETAPE_2",
}

STOPWORDS = {
    "les", "des", "une", "pour", "dans", "par", "sur", "avec", "sans", "plus", "moins",
    "entre", "contre", "sous", "vers", "chez", "dont", "mais", "donc", "etre", "avoir",
    "fait", "faire", "peut", "sont", "cette", "cet", "ces", "tous", "tout", "toute",
    "toutes", "aux", "qui", "que", "quoi", "comme", "aussi", "ainsi", "apres", "avant",
    "selon", "chaque", "meme", "autre", "autres", "leurs", "leur", "the", "and", "for",
}


def tokenize(text: str) -> list[str]:
    t = text.lower()
    for a, b in (("é", "e"), ("è", "e"), ("ê", "e"), ("ë", "e"), ("à", "a"), ("â", "a"), ("î", "i"), ("ï", "i"), ("ô", "o"), ("ù", "u"), ("û", "u"), ("ç", "c")):
        t = t.replace(a, b)
    return [w for w in re.findall(r"[a-z0-9]{3,}", t) if w not in STOPWORDS]


def apply_merges_on_map(items_map: dict[str, dict], merges: list[dict], is_idee: bool = True) -> dict[str, dict]:
    """Fusionne proprement sans jamais perdre un seul bib_id, meme si les merges se chainent."""
    redirect: dict[str, str] = {}

    def resolve(tid: str) -> str:
        seen = set()
        while tid in redirect and tid not in seen:
            seen.add(tid)
            tid = redirect[tid]
        return tid

    for m in merges:
        keep = resolve(str(m.get("keep_id", "")))
        mids = [resolve(str(x)) for x in (m.get("merge_ids") or [])]
        if keep not in items_map:
            continue
        k_item = items_map[keep]
        for mid in mids:
            if mid == keep or mid not in items_map:
                continue
            other = items_map.pop(mid)
            redirect[mid] = keep
            # Union des bib_ids sans perte
            merged_bibs = list(dict.fromkeys(k_item["bib_ids"] + other["bib_ids"]))
            k_item["bib_ids"] = merged_bibs
            # Completer anteriorite si vide
            if is_idee and other.get("anteriorite_connue") and not k_item.get("anteriorite_connue"):
                k_item["anteriorite_connue"] = other["anteriorite_connue"]
            elif is_idee and other.get("anteriorite_connue") and other["anteriorite_connue"] not in k_item.get("anteriorite_connue", ""):
                if "Aucune" not in other["anteriorite_connue"]:
                    k_item["anteriorite_connue"] = f"{k_item['anteriorite_connue']} ; {other['anteriorite_connue']}".strip(" ;")
        # Appliquer les upgrades eventuels
        if is_idee:
            for src_k, dst_k in (
                ("upgraded_titre_clair_fr", "titre_clair_fr"),
                ("upgraded_sous_theme", "sous_theme"),
                ("upgraded_theme", "theme"),
                ("upgraded_enonce_complet", "enonce_complet"),
                ("upgraded_mecanisme_causal", "mecanisme_causal"),
                ("upgraded_anteriorite_connue", "anteriorite_connue"),
                ("upgraded_esquisse_test_de_mort_et_faux_temoin", "esquisse_test_de_mort_et_faux_temoin"),
            ):
                val = m.get(src_k)
                if isinstance(val, str) and val.strip():
                    k_item[dst_k] = val.strip()
            if m.get("upgraded_objet") in VALID_OBJETS:
                k_item["objet"] = m["upgraded_objet"]
            if m.get("upgraded_statut_epistemique") in VALID_STATUTS:
                k_item["statut_epistemique"] = m["upgraded_statut_epistemique"]
            if m.get("upgraded_regime_materiel") in VALID_REGIMES:
                k_item["regime_materiel"] = m["upgraded_regime_materiel"]
        else:
            for src_k, dst_k in (
                ("upgraded_titre_clair_fr", "titre_clair_fr"),
                ("upgraded_enonce_complet", "enonce_complet"),
                ("upgraded_description_complete", "description_complete"),
            ):
                val = m.get(src_k)
                if isinstance(val, str) and val.strip():
                    k_item[dst_k] = val.strip()
    return items_map


def find_cross_pairs(idees: list[dict], cross_thr: float = 0.30, intra_thr: float = 0.45, max_pairs: int = 350) -> list[dict]:
    n = len(idees)
    if n < 2:
        return []
    docs = [tokenize(f"{it.get('titre_clair_fr','')} {it.get('titre_clair_fr','')} {it.get('enonce_complet','')[:420]}") for it in idees]
    df = Counter()
    for d in docs:
        for w in set(d):
            df[w] += 1
    vecs, norms = [], []
    inv = defaultdict(list)
    for idx, d in enumerate(docs):
        c = Counter(d)
        v = {}
        for w, cnt in c.items():
            if df[w] > max(3, int(0.40 * n)):
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
        cross = idees[i]["objet"] != idees[j]["objet"]
        if (cross and sim >= cross_thr) or (not cross and sim >= intra_thr):
            pairs.append((sim, cross, i, j))
    pairs.sort(key=lambda x: (x[1], x[0]), reverse=True)

    return [
        {
            "sim": round(sim, 3),
            "cross_objet": cross,
            "id_a": idees[i]["temp_id"],
            "objet_a": idees[i]["objet"],
            "titre_a": idees[i]["titre_clair_fr"],
            "n_bib_a": len(idees[i]["bib_ids"]),
            "id_b": idees[j]["temp_id"],
            "objet_b": idees[j]["objet"],
            "titre_b": idees[j]["titre_clair_fr"],
            "n_bib_b": len(idees[j]["bib_ids"]),
        }
        for sim, cross, i, j in pairs[:max_pairs]
    ]


def main() -> None:
    agg = json.loads((SCRATCH / "phase2a_aggregated.json").read_text(encoding="utf-8"))
    idees_map = {x["temp_id"]: x for x in agg["idees"]}
    acquis_map = {x["temp_id"]: x for x in agg["acquis"]}
    outils_map = {x["temp_id"]: x for x in agg["outils"]}
    ecarts_list = list(agg["ecarts"])

    master_bibs = {
        json.loads(l)["id_unifie"]
        for l in (SCRATCH / "corpus_total_enrichi.jsonl").read_text(encoding="utf-8").splitlines()
        if l.strip()
    }

    dec_dir = SCRATCH / "phase2b_decisions"
    for df in sorted(dec_dir.glob("OBJ-*.json")):
        dec = json.loads(df.read_text(encoding="utf-8"))
        # 1. Merges idees, acquis, outils
        idees_map = apply_merges_on_map(idees_map, dec.get("merges_idees") or dec.get("merges") or [], is_idee=True)
        acquis_map = apply_merges_on_map(acquis_map, dec.get("merges_acquis") or [], is_idee=False)
        outils_map = apply_merges_on_map(outils_map, dec.get("merges_outils") or [], is_idee=False)

        # 2. Title & sous_theme upgrades
        for up in dec.get("upgrades") or []:
            tid = str(up.get("temp_id", ""))
            if tid in idees_map:
                it = idees_map[tid]
                for k in ("titre_clair_fr", "theme", "sous_theme", "enonce_complet", "mecanisme_causal", "anteriorite_connue", "esquisse_test_de_mort_et_faux_temoin"):
                    if isinstance(up.get(k), str) and up[k].strip():
                        it[k] = up[k].strip()
                if up.get("objet") in VALID_OBJETS:
                    it["objet"] = up["objet"]
                if up.get("statut_epistemique") in VALID_STATUTS:
                    it["statut_epistemique"] = up["statut_epistemique"]
                if up.get("regime_materiel") in VALID_REGIMES:
                    it["regime_materiel"] = up["regime_materiel"]

        # 3. Reclassifications (idee -> acquis / outil / ecart / autre objet)
        for rc in dec.get("reclassifications") or []:
            tid = str(rc.get("temp_id", ""))
            target = str(rc.get("target_register", "")).lower()
            if tid not in idees_map:
                continue
            if target in ("acquis", "acquis_et_morts"):
                it = idees_map.pop(tid)
                new_id = f"T-ACQ-R-{tid}"
                acquis_map[new_id] = {
                    "temp_id": new_id,
                    "bib_ids": it["bib_ids"],
                    "titre_clair_fr": rc.get("titre_clair_fr") or it["titre_clair_fr"],
                    "objet": rc.get("objet") if rc.get("objet") in VALID_OBJETS else it["objet"],
                    "theme": rc.get("theme") or it["theme"],
                    "type_acquis": rc.get("type_acquis") or "constat_tranche",
                    "enonce_complet": rc.get("enonce_complet") or it["enonce_complet"],
                    "motif_ou_resultat": rc.get("motif") or it.get("mecanisme_causal", ""),
                }
            elif target in ("outil", "outils_bancs_corpus"):
                it = idees_map.pop(tid)
                new_id = f"T-OUT-R-{tid}"
                outils_map[new_id] = {
                    "temp_id": new_id,
                    "bib_ids": it["bib_ids"],
                    "titre_clair_fr": rc.get("titre_clair_fr") or it["titre_clair_fr"],
                    "objet": rc.get("objet") if rc.get("objet") in VALID_OBJETS else it["objet"],
                    "theme": rc.get("theme") or it["theme"],
                    "type_outil": rc.get("type_outil") or "banc_experimental",
                    "description_complete": rc.get("description_complete") or it["enonce_complet"],
                }
            elif target in ("ecart", "ecartes_structurels"):
                it = idees_map.pop(tid)
                ecarts_list.append({
                    "temp_id": f"T-ECA-R-{tid}",
                    "bib_ids": it["bib_ids"],
                    "motif_ecart": rc.get("motif") or "Reclasse par conservateur : entree sans idee scientifique autonome",
                    "resume_court": it["titre_clair_fr"],
                })
            elif rc.get("objet") in VALID_OBJETS:
                idees_map[tid]["objet"] = rc["objet"]
                if rc.get("theme"):
                    idees_map[tid]["theme"] = rc["theme"]

    # Verification 0 orphelin apres Phase 2B
    covered = set()
    for it in list(idees_map.values()) + list(acquis_map.values()) + list(outils_map.values()) + ecarts_list:
        covered.update(it["bib_ids"])
    missing = sorted(master_bibs - covered)
    assert not missing, f"Phase 2B lost {len(missing)} BIB IDs: {missing[:20]}"

    state = {
        "idees": list(idees_map.values()),
        "acquis": list(acquis_map.values()),
        "outils": list(outils_map.values()),
        "ecarts": ecarts_list,
    }
    (SCRATCH / "phase2b_post_state.json").write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")

    # Preparer Phase 3 cross-rayon input
    cross_pairs = find_cross_pairs(state["idees"])
    by_obj = Counter(x["objet"] for x in state["idees"])
    p3_in = {
        "counts": {
            "idees": len(state["idees"]),
            "acquis": len(state["acquis"]),
            "outils": len(state["outils"]),
            "ecarts": len(state["ecarts"]),
            "par_objet": dict(by_obj),
        },
        "cross_and_residual_duplicate_pairs": cross_pairs,
        "all_sous_themes": sorted(set((x["objet"], x["theme"], x.get("sous_theme", "")) for x in state["idees"])),
    }
    (SCRATCH / "phase3_input.json").write_text(json.dumps(p3_in, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"PHASE 2B APPLIED -> idees={len(state['idees'])}, acquis={len(state['acquis'])}, outils={len(state['outils'])}, ecarts={len(state['ecarts'])}, cross_pairs={len(cross_pairs)}")


if __name__ == "__main__":
    main()
