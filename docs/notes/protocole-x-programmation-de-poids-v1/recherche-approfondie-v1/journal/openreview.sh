#!/usr/bin/env bash
# Usage : openreview.sh "TERMES" [limite] [filtre_de_lieu_regex]
set -u
DIR="$(cd "$(dirname "$0")" && pwd)"
Q="$1"; LIM="${2:-50}"; FIL="${3:-.}"
ENC=$(python3 -I -c 'import sys,urllib.parse; print(urllib.parse.quote(sys.argv[1]))' "$Q")
OUT=$("$DIR/requete.sh" openreview "$Q" "https://api2.openreview.net/notes/search?term=${ENC}&type=terms&content=all&source=forum&limit=${LIM}" json)
F=$(echo "$OUT" | awk '{print $4}')
echo "## [$OUT] :: $Q"
python3 -I - "$F" "$FIL" <<'PY'
import sys, json, re, datetime
d = json.load(open(sys.argv[1], encoding="utf-8")); fil = re.compile(sys.argv[2], re.I)
notes = d.get("notes", [])
print("# notes rendues :", len(notes), "; total annoncé :", d.get("count"))
for n in notes:
    c = n.get("content", {})
    g = lambda k: (c.get(k, {}) or {}).get("value", "") if isinstance(c.get(k), dict) else (c.get(k) or "")
    venue = g("venue") or ""
    if not fil.search(venue): continue
    t = (n.get("cdate") or n.get("tcdate") or 0) / 1000
    date = datetime.datetime.fromtimestamp(t, datetime.UTC).strftime("%Y-%m-%d") if t else "?"
    title = re.sub(r"\s+", " ", str(g("title")))[:130]
    print(f"{date}\t{venue[:38]}\t{title}\t{n.get('forum') or n.get('id')}")
PY
sleep 2
