#!/usr/bin/env python3
"""Decoupe LIT-0001..LIT-2863 en lots <= 38 Ko (et <= 60 entrees) pour curation parallele flash sans troncature."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

V2_DIR = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch\v2_lit")
IN_FILE = V2_DIR / "supplement-litterature-et-lectures-v1.jsonl"
BATCH_DIR = V2_DIR / "lit_batches"
BATCH_DIR.mkdir(parents=True, exist_ok=True)
for old in BATCH_DIR.glob("lit_batch_*.jsonl"):
    old.unlink()

EMOJI_RE = re.compile("[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]+")


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", EMOJI_RE.sub("", s or "")).strip()


def main() -> None:
    rows = [json.loads(l) for l in IN_FILE.read_text(encoding="utf-8").splitlines() if l.strip()]
    by_fo = defaultdict(list)
    for r in rows:
        by_fo[(r.get("famille_source", ""), r.get("objet", ""))].append(r)

    MAX_ITEMS = 55
    MAX_BYTES = 37500
    manifest = []
    b_idx = 0

    for (fam, obj), items in sorted(by_fo.items()):
        items.sort(key=lambda x: x["id_supplement"])
        cur_lines, cur_bytes, first_id, last_id = [], 0, "", ""

        def flush():
            nonlocal b_idx, cur_lines, cur_bytes, first_id, last_id
            if not cur_lines:
                return
            b_idx += 1
            bid = f"lit_batch_{b_idx:03d}"
            bp = BATCH_DIR / f"{bid}.jsonl"
            bp.write_text("\n".join(cur_lines) + "\n", encoding="utf-8")
            manifest.append({
                "batch_id": bid,
                "famille_source": fam,
                "objet": obj,
                "count": len(cur_lines),
                "bytes": cur_bytes,
                "path": str(bp),
                "first_lit": first_id,
                "last_lit": last_id,
            })
            cur_lines, cur_bytes, first_id, last_id = [], 0, "", ""

        for r in items:
            en = clean(r.get("enonce_complet", ""))
            if len(en.encode("utf-8")) > 28000:
                en = en[:18000] + " [... milieu conserve dans le corpus source ...] " + en[-6000:]
            c = {
                "id_supplement": r["id_supplement"],
                "id_origine": r.get("id_origine", ""),
                "nature_entree": r.get("nature_entree", ""),
                "famille_source": r.get("famille_source", ""),
                "objet": r.get("objet", ""),
                "auteurs_ou_modele": clean(r.get("auteurs_ou_modele", "")),
                "statut_lecture": clean(r.get("statut_lecture", "")),
                "regime_execution": r.get("regime_execution", ""),
                "titre": clean(r.get("titre", "")),
                "enonce_complet": en,
                "source_chemin": r.get("source_chemin", ""),
            }
            line = json.dumps(c, ensure_ascii=False)
            lb = len(line.encode("utf-8")) + 1
            if cur_lines and (len(cur_lines) >= MAX_ITEMS or cur_bytes + lb > MAX_BYTES):
                flush()
            if not cur_lines:
                first_id = r["id_supplement"]
            last_id = r["id_supplement"]
            cur_lines.append(line)
            cur_bytes += lb
        flush()

    (V2_DIR / "lit_batches_manifest.json").write_text(
        json.dumps({"total": len(rows), "n_batches": len(manifest), "batches": manifest}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"LIT BATCHES READY: {len(rows)} entries -> {len(manifest)} batches (max_bytes={max(m['bytes'] for m in manifest)})")


if __name__ == "__main__":
    main()
