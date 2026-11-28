#!/usr/bin/env python3
"""Repack Phase 1 extracted docs into <= 38 KB files so every flash agent reads 100% of its pack in 1 read_file call."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch")
PACKS_IN = SCRATCH / "phase1_packs"
PACKS_OUT = SCRATCH / "phase1_packs_38k"
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
MAX_BYTES = 37000

for groupe, docs in sorted(by_group.items()):
    cur = []
    for d in docs:
        dc = dict(d)
        # Keep head 6500 + tail 2000 for huge cells (total <= 8600 chars) so every proposition & first experiment is preserved and fits cleanly
        txt = dc.get("contenu", "")
        if len(txt) > 8800:
            dc["contenu"] = txt[:6600] + "\n\n[... milieu omis ...]\n\n" + txt[-2000:]
        cand = cur + [dc]
        cand_bytes = len(json.dumps(cand, ensure_ascii=False).encode("utf-8"))
        if cur and (cand_bytes > MAX_BYTES or len(cur) >= 8):
            idx += 1
            pid = f"p1_{idx:02d}_{groupe}"
            out_f = PACKS_OUT / f"{pid}.json"
            raw = json.dumps(cur, ensure_ascii=False, indent=1)
            out_f.write_text(raw, encoding="utf-8")
            manifest.append({"pack_id": pid, "groupe": groupe, "path": str(out_f), "n_docs": len(cur), "bytes": len(raw.encode("utf-8"))})
            cur = [dc]
        else:
            cur = cand
    if cur:
        idx += 1
        pid = f"p1_{idx:02d}_{groupe}"
        out_f = PACKS_OUT / f"{pid}.json"
        raw = json.dumps(cur, ensure_ascii=False, indent=1)
        out_f.write_text(raw, encoding="utf-8")
        manifest.append({"pack_id": pid, "groupe": groupe, "path": str(out_f), "n_docs": len(cur), "bytes": len(raw.encode("utf-8"))})

(SCRATCH / "phase1_38k_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"PACKS 38K: {len(manifest)} (total docs={sum(m['n_docs'] for m in manifest)}, max_bytes={max(m['bytes'] for m in manifest)})")
