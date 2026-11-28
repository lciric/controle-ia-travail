#!/usr/bin/env python3
"""Repack Phase 1 extracted docs into ~16 balanced packs for parallel flash extraction."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch")
PACKS_IN = SCRATCH / "phase1_packs"
PACKS_OUT = SCRATCH / "phase1_packs_merged"
PACKS_OUT.mkdir(parents=True, exist_ok=True)
for old in PACKS_OUT.glob("p1_*.json"):
    old.unlink()

by_group = defaultdict(list)
for pf in sorted(PACKS_IN.glob("pack_*.json")):
    docs = json.loads(pf.read_text(encoding="utf-8"))
    for d in docs:
        by_group[d["groupe"]].append(d)

manifest = []
idx = 0
for groupe, docs in sorted(by_group.items()):
    # Group up to 14 docs or ~210,000 chars per pack (well within flash context, ~50k tokens)
    cur, chars = [], 0
    for d in docs:
        # Cap individual huge docs at 16,000 chars (head 12k + tail 4k) so every doc is readable
        dc = dict(d)
        if len(dc["contenu"]) > 16000:
            dc["contenu"] = dc["contenu"][:12000] + "\n\n[... EXTRAIT INTERMEDIAIRE OMIS ...]\n\n" + dc["contenu"][-4000:]
        if cur and (chars + len(dc["contenu"]) > 190000 or len(cur) >= 14):
            idx += 1
            pid = f"p1_{idx:02d}_{groupe}"
            out_f = PACKS_OUT / f"{pid}.json"
            out_f.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8")
            manifest.append({"pack_id": pid, "groupe": groupe, "path": str(out_f), "n_docs": len(cur), "chars": chars})
            cur, chars = [], 0
        cur.append(dc)
        chars += len(dc["contenu"])
    if cur:
        idx += 1
        pid = f"p1_{idx:02d}_{groupe}"
        out_f = PACKS_OUT / f"{pid}.json"
        out_f.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8")
        manifest.append({"pack_id": pid, "groupe": groupe, "path": str(out_f), "n_docs": len(cur), "chars": chars})

(SCRATCH / "phase1_merged_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"MERGED PACKS: {len(manifest)} (total docs={sum(m['n_docs'] for m in manifest)})")
for m in manifest:
    print(f"  {m['pack_id']}: {m['n_docs']} docs, {m['chars']} chars")
