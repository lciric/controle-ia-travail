"""Vérification (processeur, sans modèle, sans pièce de P3) : la frontière du repli de `resoudre_avec_repli` compte au
plus quasi_egalites_max + quasi_egalites_max² combinaisons (bascules_max = 2) ; à combinaisons_max = 272, la borne ne
coupe aucune combinaison de la frontière ; à 136, elle la coupe. Le rejeu est remplacé par un faux qui rend toujours 16
quasi-égalités après la dernière bascule et une empreinte qui ne redonne jamais celle de P3 (pire cas de la frontière)."""
import sys
from controle_ia.runs_nuit import resolution_graine_v1 as rg

N = 16


def faux_rejeu(moteur, voc, fmt, env, identifiant, T, textes, jetons, jetons_notes, Qs, reg, forcages, prefixe,
               journal_pas, cpt):
    # journal : (pas, rang, choix, non_contraint, candidats, ecart, second, marge, balayage, p_k, argmax_p)
    if forcages is None:
        base = [(0, j, 1, 1, 2, 0.1 + 0.01 * j, 2, 0.1, False, 0.5, 1) for j in range(N)]
    else:
        (t, s) = max(forcages)
        base = [(t, s + 1 + j, 1, 1, 2, 0.2 + 0.01 * j, 2, 0.1, False, 0.5, 1) for j in range(N)]
    journal_pas.extend(base)
    return {"actions": []}, [[1]]


rg.rejouer_episode = faux_rejeu
rg.episode_harnais = lambda *a, **k: None
rg.empreinte_trajectoire = lambda *a, **k: "jamais-celle-de-p3"
for cmax in (136, 271, 272, 10_000):
    reg = rg.Reglages(temperature=1.0, max_nouveaux=400, seuil_ecart=1.0, quasi_egalites_max=N, bascules_max=2,
                      combinaisons_max=cmax, balayages_max=16, echeance=None, duree_episode_s=None)
    s = rg.resoudre_avec_repli(None, None, None, lambda: None, "e", 1, ["x"], [1], [1], None, "cible", reg, cmax)
    print(f"combinaisons_max={cmax} : essayées {s['combinaisons_essayees']}, par niveau {s['repli']['par_niveau']}, "
          f"statut {s['statut']}")
sys.exit(0)
