"""Compare deux dossiers d'épreuves : octet pour octet, puis après remplacement du préfixe de chemin du dossier
(seule différence admise : le chemin d'écriture). Usage : comparer_epreuves_v1.py DOSSIER_PUBLIE DOSSIER_REJOUE"""
import hashlib, json, pathlib, sys

pub, rej = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])


def norm(obj, prefixes):
    if isinstance(obj, dict):
        return {k: norm(v, prefixes) for k, v in obj.items()}
    if isinstance(obj, list):
        return [norm(v, prefixes) for v in obj]
    if isinstance(obj, str):
        for p in prefixes:
            obj = obj.replace(p, "<DOSSIER>")
        return obj
    return obj


noms_pub = sorted(p.name for p in pub.iterdir() if p.suffix != ".sha256")
noms_rej = sorted(p.name for p in rej.iterdir())
print("publies seulement :", sorted(set(noms_pub) - set(noms_rej)))
print("rejoues seulement :", sorted(set(noms_rej) - set(noms_pub)))
for n in sorted(set(noms_pub) & set(noms_rej)):
    a, b = (pub / n).read_bytes(), (rej / n).read_bytes()
    if a == b:
        print("IDENTIQUE OCTET", n)
        continue
    ja, jb = json.loads(a), json.loads(b)
    # préfixe publié : dossier d'écriture de l'auteur, déduit du champ « fichier » ou « source.chemin »
    txt = a.decode("utf-8")
    prefixes_a = sorted({s.rsplit("/", 1)[0] for s in __import__("re").findall(r'"(/tmp/[^"]+?/epreuves-oracle-v67-v1)/', txt)} |
                        {m for m in __import__("re").findall(r'"(/tmp/[^"]*?epreuves-oracle-v67-v1)', txt)})
    na = norm(ja, prefixes_a)
    nb = norm(jb, [str(rej)])
    # script_sha256 identique attendu (copie octet pour octet)
    print("IDENTIQUE APRES CHEMIN" if na == nb else "DIVERGE", n, "prefixes publies :", prefixes_a)
    if na != nb:
        for k in set(na) | set(nb) if isinstance(na, dict) else []:
            if na.get(k) != nb.get(k):
                print("   cle divergente :", k)
