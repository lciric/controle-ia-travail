import json
import sys

for a in sys.argv[1:]:
    print(json.dumps(a, ensure_ascii=False))
