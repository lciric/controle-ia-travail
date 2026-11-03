"""v2 : les fusions sans contenu (non écrites) sont comptées dans « non_fourni » au lieu d'arrêter. Paquet sans provenance des fiches d'une course de l'organisme (source 2), pour le lecteur A.
Usage : paquet_course_soir_v1.py DOSSIER_GENERATION_1 SORTIE_JSON CLE_JSON
Entrées : fiches.json (identifiant → {contenu, empreinte, meta}) et fusions-inachevees.json ({fusions: [...]}) du dossier generation-1.
Sortie : items S2-01… (contenu seul), dans un ordre tiré par SeedSequence ; graine = int(sha256('source-2-permutation-v1|' + sha256(fiches.json)), 16).
Clé (au coffre) : S2-xx → fichier, identifiant, meta (provenance). Manifeste à côté de la sortie."""
import json, hashlib, sys, os
import numpy as np
gen, sortie, cle_p = sys.argv[1:4]
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
fp = os.path.join(gen, 'fiches.json'); fu = os.path.join(gen, 'fusions-inachevees.json')
F = json.load(open(fp)) if os.path.exists(fp) else {}
U = json.load(open(fu)).get('fusions', []) if os.path.exists(fu) else []
brut = [('fiches.json', k, v.get('contenu'), v.get('meta')) for k, v in sorted(F.items())]
brut += [('fusions-inachevees.json', str(i), (x.get('contenu') if isinstance(x, dict) and 'contenu' in x else x), (x.get('meta') if isinstance(x, dict) else None)) for i, x in enumerate(U)]
absents = [(f, k) for f, k, c, _ in brut if c is None]
brut = [b for b in brut if b[2] is not None]
e = int(hashlib.sha256(('source-2-permutation-v1|' + (sha(fp) if os.path.exists(fp) else 'vide')).encode()).hexdigest(), 16)
perm = np.random.default_rng(np.random.SeedSequence(e)).permutation(len(brut)) if brut else []
items, cle = [], {}
for j, i in enumerate(perm, 1):
    f, k, c, m = brut[int(i)]; ident = f'S2-{j:02d}'
    items.append({'item': ident, 'contenu': c}); cle[ident] = {'fichier': f, 'id': k, 'meta': m}
out = {'source': 2, 'description': "Course d'idéation de l'organisme sur la question servie : fiches de toutes les passes de tous les proposeurs et fusions inachevées du bisociateur ; sans provenance, sans sortie des juges, sans le coffre de la course.", 'nombre': len(items), 'non_fourni': ([] if os.path.exists(fp) else ['fiches.json absent']) + [f'{f} n° {k} : contenu absent (fusion non écrite)' for f, k in absents], 'items': items}
os.makedirs(os.path.dirname(sortie), exist_ok=True); json.dump(out, open(sortie, 'w'), ensure_ascii=False, indent=1)
os.makedirs(os.path.dirname(cle_p), exist_ok=True); json.dump({'cle': cle}, open(cle_p, 'w'), ensure_ascii=False, indent=1)
man = {'graine_entropie': str(e), 'regle': "int(sha256('source-2-permutation-v1|' + sha256(fiches.json)), 16) → SeedSequence → default_rng → permutation", 'numpy': np.__version__,
       'entrees': {p: sha(p) for p in (fp, fu) if os.path.exists(p)}, 'sortie': sha(sortie), 'cle': sha(cle_p)}
json.dump(man, open(os.path.join(os.path.dirname(sortie), 'manifeste-preparation-source-2-v1.json'), 'w'), ensure_ascii=False, indent=1)
print(sortie, man['sortie'], len(items), 'éléments ; clé', man['cle'])
