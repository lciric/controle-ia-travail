"""Essai 04 : garde des graines de la fonction pure (`exiger_graines`). Elle ne contrôle que l'entropie de chaque clé.
(a) deux clés échangées (même entropie, graines valides mais d'une autre clé) ; (b) état de contrôle altéré (graine
reconstruite ≠ graine consignée, `manifeste.generateur`). Attendu au sens de R9 : arrêt dans les deux cas."""
import copy

import commun  # noqa: F401
from commun import cp, empreinte_sortie, tc

P = tc.P
src, lec, s0 = tc._cas("sain")
k1, k2 = f"addendum/A3/{P[0]}/contrastes", f"addendum/A3/{P[1]}/contrastes"

G = copy.deepcopy(tc.G)
G[k1], G[k2] = G[k2], G[k1]
try:
    s = cp.analyser_addendum(src, lec, G)
    print(f"(a) clés {k1.split('/')[1]} échangées entre les deux sondes : aucun arrêt ; sortie "
          f"{'identique' if empreinte_sortie(s) == empreinte_sortie(s0) else 'différente'} de la sortie aux graines "
          f"dérivées ; bornes de Δ_ST : {s0['analyses']['A3'][P[0]]['descriptif']['contrastes']['ST']['bas']:.4f} → "
          f"{s['analyses']['A3'][P[0]]['descriptif']['contrastes']['ST']['bas']:.4f}")
except Exception as e:  # noqa: BLE001
    print(f"(a) arrêt : {type(e).__name__} : {e}")

G = copy.deepcopy(tc.G)
G[k1]["etat_controle"] = [0, 0]
try:
    s = cp.analyser_addendum(src, lec, G)
    e = s["analyses"]["A3"][P[0]]
    print(f"(b) état de contrôle altéré : aucun arrêt ; entrée A3/{P[0]} « {e['etat']} » "
          f"({e['descriptif'].get('entree', {}).get('motif')}) ; contrôles : "
          f"{[(c['cible'], c['controle_contraire']) for c in e['controles']]} ; réserves "
          f"{sorted({r['nom'] for r in s['reserves_addendum']})}")
except Exception as e:  # noqa: BLE001
    print(f"(b) arrêt : {type(e).__name__} : {e}")
