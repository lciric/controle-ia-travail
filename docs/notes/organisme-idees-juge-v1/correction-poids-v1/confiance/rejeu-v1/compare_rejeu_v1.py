import json, os, sys, hashlib, math
S, A = sys.argv[1], sys.argv[2]
res = []
for nom in sorted(os.listdir(S)):
    if not nom.endswith('.json'): continue
    a = json.load(open(os.path.join(A, 'sorties', nom))); b = json.load(open(os.path.join(S, nom)))
    assert a['mondes'] == b['mondes'] and a['cas'] == b['cas']
    n_val = n_prom = dif_prom = dif_couv = 0; dmax = 0.0
    for la, lb in zip(a['lignes'], b['lignes']):
        assert la['monde'] == lb['monde'] and la['spawn_key'] == lb['spawn_key']
        for carte, ra in la['resultats'].items():
            if carte == '_secondes_par_monde': continue
            if carte == '_couverture':
                dif_couv += sum(ra[k] != lb['resultats'][carte][k] for k in ra); continue
            for meth, va in ra.items():
                vb = lb['resultats'][carte][meth]
                n_val += 1; n_prom += va['promue']; dif_prom += (va['promue'] != vb['promue'])
                x, y = va['log_w_max'], vb['log_w_max']
                if isinstance(x, float) and isinstance(y, float) and math.isfinite(x) and math.isfinite(y):
                    dmax = max(dmax, abs(x - y))
                elif x != y: dmax = float('inf')
    ident = {k: v for k, v in a.items() if k not in ('duree_s', 'lignes')} == {k: v for k, v in b.items() if k not in ('duree_s', 'lignes')}
    res.append({'lot': nom, 'mondes': a['mondes'], 'valeurs': n_val, 'promotions_auteur': n_prom, 'ecarts_de_promotion': dif_prom,
                'ecarts_de_couverture': dif_couv, 'ecart_max_log_w': dmax, 'entete_identique': ident,
                'duree_auteur_s': a['duree_s'], 'duree_rejeu_s': b['duree_s'],
                'sha256_auteur': hashlib.sha256(open(os.path.join(A, 'sorties', nom), 'rb').read()).hexdigest()})
for r in res: print(r['lot'], r['mondes'], 'valeurs', r['valeurs'], 'promues', r['promotions_auteur'], 'ecarts prom', r['ecarts_de_promotion'], 'couv', r['ecarts_de_couverture'], 'dmax %.2e' % r['ecart_max_log_w'], r['entete_identique'], r['duree_auteur_s'], r['duree_rejeu_s'])
json.dump(res, open(os.path.join(os.path.dirname(S), 'comparaison-rejeu.json'), 'w'), indent=1)
print(len(res), 'lots ;', sum(r['valeurs'] for r in res), 'valeurs ;', sum(r['ecarts_de_promotion'] for r in res), 'ecarts de promotion ; ecart max', max(r['ecart_max_log_w'] for r in res))
