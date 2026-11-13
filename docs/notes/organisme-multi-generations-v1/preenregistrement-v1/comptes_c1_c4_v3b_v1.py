# Comptes de la correction C-1 et table de la correction C-4 (contre-lecture 11a1c50f...), sur les
# 12 parties scellées `sorties-v3/generations-a2-v3b-monde-*.json` (condition « regroupement », tranche
# appariée). Lecture seule. Usage : python3 -I -B comptes_c1_c4_v3b_v1.py DOSSIER_SORTIES_V3
# Hypothèse de lecture, contrôlée ci-dessous : la composante « Ei » est la i-ème entrée de `gabarit`
# (contrôle : comptes par classe recalculés = champ `captes_par_classe`, à chaque génération).
import json, math, sys

Z = 1.959964

def wilson(k, n):
    if n == 0:
        return None
    p = k / n
    c = Z * Z / n
    centre = (p + c / 2) / (1 + c)
    demi = Z * math.sqrt(p * (1 - p) / n + c / (4 * n)) / (1 + c)
    return (centre - demi, centre + demi)

dossier = sys.argv[1]
mondes = []
for w in range(12):
    with open('%s/generations-a2-v3b-monde-%d.json' % (dossier, w)) as f:
        r = json.load(f)['resultat']
    classe = {'E%d' % (i + 1): c for i, (c, _sorte) in enumerate(r['gabarit'])}
    gens = r['generations']
    controle = True
    for g in gens:
        cpt = {}
        for e in g['captes']:
            cpt[classe[e]] = cpt.get(classe[e], 0) + 1
        attendu = {k: v for k, v in g['captes_par_classe'].items() if v}
        controle &= (cpt == attendu)
    c1, c2, c3 = (set(g['captes']) for g in gens)
    neuves2 = sorted(c2 - c1)
    neuves3 = sorted(c3 - c2)
    fortes_moyennes = sorted(e for e, c in classe.items() if c in ('forte', 'moyenne'))
    jamais = sorted(set(classe) - c3)
    retenues = [g['retenues'] for g in gens]
    fausses = [g['fausses_decouvertes'] for g in gens]
    mondes.append({
        'monde': w,
        'controle_classes': controle,
        'composantes': len(classe),
        'classes': classe,
        'neuves_generation_2': [(e, classe[e]) for e in neuves2],
        'neuves_generation_3': [(e, classe[e]) for e in neuves3],
        'fortes_et_moyennes_toutes_captees_en_generation_1': set(fortes_moyennes) <= c1,
        'jamais_captees': [(e, classe[e]) for e in jamais],
        'retenues_par_generation': retenues,
        'fausses_decouvertes_par_generation': fausses,
    })

tot_r = sum(sum(m['retenues_par_generation']) for m in mondes)
tot_f = sum(sum(m['fausses_decouvertes_par_generation']) for m in mondes)
tol = tot_f / tot_r
for m in mondes:
    n, k = sum(m['retenues_par_generation']), sum(m['fausses_decouvertes_par_generation'])
    b = wilson(k, n)
    m['fd_parmi_retenues'] = [k, n]
    m['fd_wilson'] = b
    m['fd_declenchee_tolerance_ensemble_sans_marge'] = (b is not None and b[0] > tol)

minimums = {}
for n in (5, 10, 15, 20, 30):
    for k in range(n + 1):
        if wilson(k, n)[0] > tol:
            minimums[n] = k
            break

resume = {
    'controle_classes_tous_mondes': all(m['controle_classes'] for m in mondes),
    'mondes_avec_composante_neuve_apres_generation_1': sum(1 for m in mondes if m['neuves_generation_2'] or m['neuves_generation_3']),
    'classes_des_composantes_neuves': sorted(c for m in mondes for _e, c in m['neuves_generation_2'] + m['neuves_generation_3']),
    'mondes_fortes_et_moyennes_toutes_captees_en_generation_1': sum(1 for m in mondes if m['fortes_et_moyennes_toutes_captees_en_generation_1']),
    'mondes_generation_3_sans_retenue': sum(1 for m in mondes if m['retenues_par_generation'][2] == 0),
    'mondes_avec_composante_jamais_captee': [(m['monde'], m['jamais_captees']) for m in mondes if m['jamais_captees']],
    'tolerance_ensemble': [tot_f, tot_r, tol],
    'mondes_fd_declenchee': [m['monde'] for m in mondes if m['fd_declenchee_tolerance_ensemble_sans_marge']],
    'minimum_fausses_pour_declencher_fd': minimums,
}
print(json.dumps({'resume': resume, 'mondes': mondes}, ensure_ascii=False, indent=1, default=list))
