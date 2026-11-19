"""Affiche les noms de champs, types et longueurs d'un JSON, jamais les valeurs."""
import sys, json, re

def schema(o, prof=0, maxprof=6, chemin=''):
    ind = '  ' * prof
    if isinstance(o, dict):
        cles = list(o.keys())
        # regrouper clés semblables
        motifs = {}
        for k in cles:
            motifs.setdefault(re.sub(r'\d+', '<n>', str(k)), []).append(k)
        for m, ks in motifs.items():
            k = ks[0]
            v = o[k]
            t = type(v).__name__
            extra = f" len={len(v)}" if isinstance(v, (list, dict, str)) else ''
            n = f" (x{len(ks)} clés de ce motif, ex. {k!r})" if len(ks) > 1 else ''
            print(f"{ind}{m}: {t}{extra}{n}")
            if prof < maxprof and isinstance(v, (dict, list)):
                schema(v, prof + 1, maxprof)
    elif isinstance(o, list):
        if o:
            v = o[0]
            print(f"{ind}[0]: {type(v).__name__}" + (f" len={len(v)}" if isinstance(v, (list, dict, str)) else ''))
            if prof < maxprof and isinstance(v, (dict, list)):
                schema(v, prof + 1, maxprof)

if __name__ == '__main__':
    maxprof = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    with open(sys.argv[1]) as f:
        if sys.argv[1].endswith('.jsonl'):
            n = 0; premier = None
            for ligne in f:
                if premier is None: premier = json.loads(ligne)
                n += 1
            print(f"# jsonl : {n} lignes ; champs de la première ligne")
            schema(premier, 0, maxprof)
        else:
            schema(json.load(f), 0, maxprof)
