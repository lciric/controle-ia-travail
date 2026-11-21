#!/usr/bin/env bash
# Usage : forum.sh SITE "REQUETE" [nombre]   (SITE : lesswrong | alignmentforum)
# Interroge la recherche du forum (POST /api/search), journalise, imprime les billets.
set -u
DIR="$(cd "$(dirname "$0")" && pwd)"
SITE="$1"; Q="$2"; N="${3:-20}"
J="$DIR/journal-des-requetes-v1.tsv"
NUM=$(( $(wc -l < "$J") ))
F=$(printf '%s/brut/%03d-forum-%s.json' "$DIR" "$NUM" "$SITE")
HOST="www.lesswrong.com"; [ "$SITE" = "alignmentforum" ] && HOST="www.alignmentforum.org"
BODY=$(python3 -I -c 'import json,sys; print(json.dumps([{"indexName":"test_posts","query":sys.argv[1],"params":{"query":sys.argv[1],"hitsPerPage":int(sys.argv[2]),"page":0}}]))' "$Q" "$N")
CODE=$(curl -sS --max-time 60 -A "generic-research-client/1.0" -H 'Content-Type: application/json' -X POST -d "$BODY" -o "$F" -w '%{http_code}' "https://$HOST/api/search" || echo ERR)
SZ=$(wc -c < "$F" 2>/dev/null || echo 0); H=$(sha256sum "$F" 2>/dev/null | cut -c1-64)
printf '%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$NUM" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "forum-$SITE" "$Q" "$CODE" "$SZ" "$(basename "$F")" "$H" "POST https://$HOST/api/search" >> "$J"
echo "## [$NUM $CODE $SZ] $SITE :: $Q"
python3 -I - "$F" <<'PY'
import sys, json
try:
    d = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception as e:
    print("(réponse illisible :", str(e)[:80], ")"); sys.exit(0)
res = d[0] if isinstance(d, list) else d
hits = res.get("hits", []) if isinstance(res, dict) else []
print("# résultats annoncés :", res.get("nbHits") if isinstance(res, dict) else "?", "; rendus :", len(hits))
import os
mind = os.environ.get("DEPUIS", "")
for h in hits:
    d = (h.get("postedAt") or "")[:10]
    if mind and d < mind: continue
    print(f'{d}\t{h.get("baseScore")}\t{"AF" if h.get("af") else "--"}\t{(h.get("title") or "")[:120]}\t{(h.get("authorDisplayName") or "")[:24]}\t{h.get("_id") or h.get("objectID") or ""}')
PY
sleep 2
