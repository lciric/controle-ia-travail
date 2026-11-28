#!/usr/bin/env python3
"""Validateur mecanique des sorties de lots Phase 2A et Phase 2B."""
from __future__ import annotations

import json
import re
import sys
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
    "vierge",
    "preenregistre_en_attente",
    "pris_en_charge_groupe_v1",
    "deja_valide_interne",
    "deja_refute_interne",
}

VALID_REGIMES = {
    "CPU_0_USD_SYNTHETIQUE",
    "CPU_DONNEES_PUBLIQUES_REEL",
    "GPU_VAST_8B_SOUS_GO",
    "MODELE_FERME_COURSE_ETAPE_2",
}

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]+"
)

REQ_IDEE = (
    "bib_ids",
    "titre_clair_fr",
    "objet",
    "theme",
    "sous_theme",
    "enonce_complet",
    "mecanisme_causal",
    "anteriorite_connue",
    "statut_epistemique",
    "regime_materiel",
    "esquisse_test_de_mort_et_faux_temoin",
)


def validate_batch(batch_id: str) -> int:
    in_path = SCRATCH / "phase2_batches" / f"{batch_id}.jsonl"
    out_path = SCRATCH / "phase2_curated" / f"{batch_id}.json"
    if not in_path.is_file():
        print(f"ERROR: input missing {in_path}")
        return 1
    if not out_path.is_file():
        print(f"ERROR: output missing {out_path}")
        return 1

    expected = [json.loads(l)["id_unifie"] for l in in_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    expected_set = set(expected)

    try:
        data = json.loads(out_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERROR: invalid JSON in {out_path}: {e}")
        return 1

    errors = []
    seen = []

    for reg in ("idees_canoniques", "acquis_et_morts", "outils_bancs_corpus", "ecartes_structurels"):
        items = data.get(reg)
        if not isinstance(items, list):
            errors.append(f"Register '{reg}' must be a list")
            continue
        for idx, it in enumerate(items):
            if not isinstance(it, dict):
                errors.append(f"{reg}[{idx}] not a dict")
                continue
            bids = it.get("bib_ids")
            if not isinstance(bids, list) or not bids:
                errors.append(f"{reg}[{idx}] missing/empty bib_ids")
                continue
            for b in bids:
                seen.append(b)
            if reg == "idees_canoniques":
                for f in REQ_IDEE:
                    val = it.get(f)
                    if val is None or (isinstance(val, str) and not val.strip() and f != "anteriorite_connue"):
                        errors.append(f"idees_canoniques[{idx}] missing/empty '{f}'")
                if it.get("objet") not in VALID_OBJETS:
                    errors.append(f"idees_canoniques[{idx}] invalid objet: {it.get('objet')}")
                if it.get("statut_epistemique") not in VALID_STATUTS:
                    errors.append(f"idees_canoniques[{idx}] invalid statut_epistemique: {it.get('statut_epistemique')}")
                if it.get("regime_materiel") not in VALID_REGIMES:
                    errors.append(f"idees_canoniques[{idx}] invalid regime_materiel: {it.get('regime_materiel')}")
            elif reg == "acquis_et_morts":
                for f in ("titre_clair_fr", "objet", "theme", "enonce_complet"):
                    if not str(it.get(f, "")).strip():
                        errors.append(f"acquis_et_morts[{idx}] missing '{f}'")
            elif reg == "outils_bancs_corpus":
                for f in ("titre_clair_fr", "objet", "theme", "description_complete"):
                    if not str(it.get(f, "")).strip():
                        errors.append(f"outils_bancs_corpus[{idx}] missing '{f}'")
            elif reg == "ecartes_structurels":
                if not str(it.get("motif_ecart", "")).strip():
                    errors.append(f"ecartes_structurels[{idx}] missing 'motif_ecart'")

    raw_txt = out_path.read_text(encoding="utf-8")
    if EMOJI_RE.search(raw_txt):
        errors.append("Emoji detected in output JSON — remove all emojis")

    seen_set = set(seen)
    missing = sorted(expected_set - seen_set)
    extra = sorted(seen_set - expected_set)
    dup_count = len(seen) - len(seen_set)

    if missing:
        errors.append(f"MISSING {len(missing)} bib_ids: {missing[:25]}")
    if extra:
        errors.append(f"EXTRA {len(extra)} unknown bib_ids: {extra[:25]}")
    if dup_count > 0:
        from collections import Counter
        dups = [k for k, v in Counter(seen).items() if v > 1]
        errors.append(f"DUPLICATE {dup_count} bib_ids across entries: {dups[:25]}")

    if errors:
        print(f"VALIDATION FAILED for {batch_id} ({len(errors)} error(s)):")
        for e in errors[:30]:
            print("  -", e)
        return 1

    print(
        f"VALIDATION OK for {batch_id}: expected={len(expected)} covered={len(seen_set)} "
        f"(idees={len(data['idees_canoniques'])}, acquis={len(data['acquis_et_morts'])}, "
        f"outils={len(data['outils_bancs_corpus'])}, ecarts={len(data['ecartes_structurels'])})"
    )
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: validate_batch_output.py <batch_id>")
        sys.exit(2)
    sys.exit(validate_batch(sys.argv[1]))
