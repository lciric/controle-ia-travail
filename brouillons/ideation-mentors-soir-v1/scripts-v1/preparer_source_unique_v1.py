"""Préparation sans provenance quand la seule source est la course (Feng et Jang) : fiches du lecteur A dans le sujet, réidentifiées
(PREF-01…), ordre permuté par SeedSequence (graine : entier des 16 premiers hexadécimaux du sha256 du fichier du lecteur), champs réduits au noyau
commun ; parts pour les moissonneurs ; entrée du groupeur (id, enonce, mecanisme). Clé à part (source « tour » = lecteur A, comme ailleurs).
Usage : preparer_source_unique_v1.py LECTEUR_JSON PREF DOSSIER_PREP DOSSIER_PISTE CLE_JSON TAILLE_PART"""
import hashlib, json, sys, os
import numpy as np
lect_p, pref, prep_d, piste_d, cle_p, taille = sys.argv[1:7]; taille = int(taille)
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
lect = json.load(open(lect_p)); lect = lect if isinstance(lect, list) else next(v for v in lect.values() if isinstance(v, list))
NOYAU = ('type', 'enonce', 'mecanisme', 'mesure_qui_tue', 'prediction', 'echec_le_plus_probable', 'cout')
def dans_le_sujet(f):
    c = f.get('classement'); c = c if isinstance(c, list) else [c]
    st = (f.get('statut') or 'gardée').lower()
    return 'hors sujet' not in c and not st.startswith('réfut') and not st.startswith('refut')
el = []
for f in lect:
    if not dans_le_sujet(f): continue
    d = {k: f.get(k, '') for k in NOYAU}; d['prediction'] = f.get('resultat_attendu', '') or f.get('prediction', '')
    el.append((f['id'], d))
h = sha(lect_p); graine = int(h[:16], 16)
perm = np.random.default_rng(np.random.SeedSequence(graine)).permutation(len(el))
servies, cle = [], {}
for r, i in enumerate(perm, 1):
    ident, d = el[i]; nid = f'{pref}-{r:02d}'
    servies.append(dict(id=nid, **d)); cle[nid] = {'source': 'tour', 'ident': ident}
os.makedirs(prep_d, exist_ok=True); os.makedirs(piste_d, exist_ok=True)
json.dump(servies, open(f'{prep_d}/fiches-servies-v1.json', 'w'), ensure_ascii=False, indent=1)
parts = [servies[k:k + taille] for k in range(0, len(servies), taille)]
for k, p in enumerate(parts, 1): json.dump(p, open(f'{prep_d}/fiches-moisson-part-{k}-v1.json', 'w'), ensure_ascii=False, indent=1)
json.dump([{'id': f['id'], 'enonce': f['enonce'], 'mecanisme': f['mecanisme']} for f in servies], open(f'{piste_d}/fiches-a-grouper-v1.json', 'w'), ensure_ascii=False, indent=1)
json.dump({'cle': cle, 'regle': f'{pref}-xx = rang dans la permutation'}, open(cle_p, 'w'), ensure_ascii=False, indent=1)
man = {'entree': {lect_p: h}, 'graine': str(graine), 'numpy': np.__version__, 'servies': len(servies), 'parts': [len(p) for p in parts],
       'sorties': {os.path.basename(x): sha(x) for x in [f'{prep_d}/fiches-servies-v1.json'] + [f'{prep_d}/fiches-moisson-part-{k}-v1.json' for k in range(1, len(parts) + 1)] + [f'{piste_d}/fiches-a-grouper-v1.json']}, 'cle': sha(cle_p)}
json.dump(man, open(f'{prep_d}/manifeste-preparation-v1.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(man, ensure_ascii=False))
