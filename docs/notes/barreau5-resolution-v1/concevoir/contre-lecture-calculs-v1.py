"""Contre-lecture de la note de resolution du barreau 5 : calculs refaits par le contre-lecteur (Opus 5.5).
Processeur seul. Graines par numpy.random.SeedSequence (R9).
Blocs 1, 2, 4 et 5 : lois inventees, aucune donnee du programme.
Bloc 3 : arithmetique sur les seules aires de l'etape B bis deja recopiees dans le socle (D, TE, ART, MU),
sous un modele binormal a variance egale ; ce n'est pas une lecture de scores, c'est ce que les auteurs savent deja.
"""
import itertools, json, math
import numpy as np
from statistics import NormalDist

ND = NormalDist()
RACINE = np.random.SeedSequence(20261119_2)
def gen(*cle):
    return np.random.default_rng(np.random.SeedSequence(entropy=RACINE.entropy, spawn_key=tuple(cle)))
def aire(pos, neg):
    r = np.argsort(np.argsort(np.concatenate([pos, neg]))) + 1.0
    return (r[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))
sortie = {}

# ---- Bloc 1 : aire minimale detectable du contraste A, convention de l'etape B bis (99 % bilateral, borne basse au quantile 0,005)
z99b, z99u, z80 = ND.inv_cdf(0.995), ND.inv_cdf(0.99), ND.inv_cdf(0.80)
s_A = {"0.1/0.1": 0.0200, "0.2/0.2": 0.0257, "0.2/0.4": 0.0354, "0.3/0.5": 0.0375}      # ecarts types simules par la conception A
s_B = {"0.1/0.1": 0.0287, "0.2/0.2": 0.0374, "0.2/0.4": 0.0481, "0.3/0.5": 0.0503}
b1 = {}
for k in s_A:
    b1[k] = {"aire_min_note_z2.326": round(0.56 + (z99u + z80) * s_A[k], 3), "aire_min_convention_BBIS_z2.576": round(0.56 + (z99b + z80) * s_A[k], 3),
             "difference_min_note": round((z99u + z80) * s_B[k], 3), "difference_min_convention_BBIS": round((z99b + z80) * s_B[k], 3)}
# ancre empirique : demi-largeurs realisees de la ligne MU (640 contre 640, taches appariees, aire voisine de 0,5) a 95 %
mu = {"0.25": (-0.0396, -0.1100, 0.0024, 0.4955), "0.5": (0.0243, -0.0385, 0.0666, 0.5706)}
b1["ancre_MU"] = {}
for d, (D, lo, hi, a) in mu.items():
    s = (hi - lo) / 2 / 1.96
    Q = a - D
    b1["ancre_MU"][d] = {"s_D": round(s, 4), "Q": round(Q, 4), "aire_min_99_bilateral": round(Q + (z99b + z80) * s, 3)}
# tendance : s(tau) simule par A ; plancher 0,03 suppose par A, ou quantile 0,95 d'un tau nul (1,645 s)
s_tau = {10: 0.0317, 7: 0.0411, 5: 0.0502}
b1["tendance"] = {n: {"note": round(0.03 + (z99u + z80) * s, 3), "BBIS_plancher_0.03": round(0.03 + (z99b + z80) * s, 3),
                      "BBIS_plancher_q95_nul": round(1.645 * s + (z99b + z80) * s, 3)} for n, s in s_tau.items()}
sortie["bloc1_aires_minimales"] = b1

# ---- Bloc 1 bis : simulation independante du contraste A (64 taches x 10 actions, deux groupes apparies par tache,
# effet d'episode propre a chaque groupe), intervalle percentile par taches a 99 % bilateral, plancher fixe 0,56
def sim_A(delta, icc_t, icc_e, rep=250, B=400, cle=0):
    g = gen(11, cle); ok = 0; aires = []
    for _ in range(rep):
        u = g.normal(0, math.sqrt(icc_t), (64, 1))
        sa = math.sqrt(1 - icc_t - icc_e)
        x = u + g.normal(0, math.sqrt(icc_e), (64, 1)) + g.normal(0, sa, (64, 10)) + delta
        y = u + g.normal(0, math.sqrt(icc_e), (64, 1)) + g.normal(0, sa, (64, 10))
        a0 = aire(x.ravel(), y.ravel()); aires.append(a0)
        idx = g.integers(0, 64, (B, 64))
        bs = np.array([aire(x[i].ravel(), y[i].ravel()) for i in idx])
        ok += np.quantile(bs - 0.56, 0.005) > 0
    return round(float(np.mean(aires)), 3), round(ok / rep, 3)
b1b = {}
for j, (it, ie) in enumerate([(0.2, 0.2), (0.2, 0.4)]):
    for dl in (0.4, 0.5, 0.6, 0.7):
        m, p = sim_A(dl, it, ie, cle=j * 10 + int(dl * 10))
        b1b[f"icc {it}/{ie}, decalage {dl}"] = {"aire_vraie": m, "puissance_99_bilateral": p}
sortie["bloc1bis_simulation_contraste_A"] = b1b

# ---- Bloc 2 : paires repliquees, test exact par changement de signe (modele de la conception B), aux niveaux 5 % et 1 %
def sim_signe(K, delta, rho, n=20000, cle=0):
    g = gen(2, cle, K)
    D = delta + math.sqrt(2 * (1 - rho)) * g.standard_normal((n, K))
    signes = np.array(list(itertools.product([1, -1], repeat=K)))
    perm = np.abs(D) @ signes.T
    p = (perm >= D.sum(1, keepdims=True) - 1e-12).mean(1)
    return {"p_minimale": 1 / 2 ** K, "puissance_5pc": round(float((p <= 0.05).mean()), 3), "puissance_1pc": round(float((p <= 0.01).mean()), 3)}
sortie["bloc2_paires_changement_de_signe"] = {f"K={K},delta={d},rho={r}": sim_signe(K, d, r, cle=int(10 * d + r * 100))
                                              for K in (5, 6, 7, 8) for d in (2.0,) for r in (0.0, 0.5)}
# permutation a deux echantillons (modele de la conception C), niveau minimal atteignable
sortie["bloc2_permutation_deux_echantillons_p_minimale"] = {f"{K}_contre_{K}": round(1 / math.comb(2 * K, K), 4) for K in (3, 4, 5)}

# ---- Bloc 3 : ce que les quatre aires scellees de l'etape B bis impliquent pour le contraste A et l'interaction B
# modele binormal a variance egale : d(X,Y) = sqrt(2) * probit(aire(X contre Y))
pr = lambda a: math.sqrt(2) * ND.inv_cdf(a)
inv = lambda d: ND.cdf(d / math.sqrt(2))
val = {"0.25": dict(D=0.9357, TE=0.9436, ART=0.9252, MU=0.4955, ART_bas=0.9046, ART_haut=0.9449),
       "0.5": dict(D=0.9854, TE=0.9532, ART=0.9822, MU=0.5706, ART_bas=0.9732, ART_haut=0.9903),
       "0.75": dict(D=0.9990, TE=0.9967, ART=0.9942, MU=0.6871, ART_bas=0.9906, ART_haut=0.9973),
       "1": dict(D=0.9994, TE=0.9885, ART=0.9986, MU=0.8793, ART_bas=0.9976, ART_haut=0.9995)}
b3 = {}
for d, v in val.items():
    inter = pr(v["TE"]) - pr(v["ART"])                               # interaction latente (adaptateur x texte) deja lue via TE et ART
    a_te = inv(pr(v["TE"]) + pr(v["MU"]) - pr(v["ART"]))             # voie 1 : TE + MU - ART
    a_d = inv(pr(v["D"]) - pr(v["ART"]))                             # voie 2 : D - ART
    a_d_bas, a_d_haut = inv(pr(v["D"]) - pr(v["ART_haut"])), inv(pr(v["D"]) - pr(v["ART_bas"]))
    b3[d] = {"interaction_latente_TE_moins_ART_en_ecarts_types": round(inter, 2),
             "contraste_A_prevu_voie_TE_MU": round(a_te, 3), "contraste_A_prevu_voie_D": round(a_d, 3),
             "contraste_A_voie_D_avec_bornes_95_de_ART": [round(a_d_bas, 3), round(a_d_haut, 3)],
             "interaction_B_prevue_A_moins_MU": [round(a_te - v["MU"], 3), round(a_d - v["MU"], 3)],
             "coherence_D_contre_TE_plus_MU": [round(pr(v["D"]), 2), round(pr(v["TE"]) + pr(v["MU"]), 2)]}
sortie["bloc3_prevision_depuis_les_aires_scellees"] = b3

# ---- Bloc 4 : le « 47,5 % » de la conception C est un rapport invente : derivation de l'ecart en ecarts types entre adaptateurs
# monde P4 : trace = 2 * alpha * (u_c + i_k)/sqrt(2) ; sonde w = moyenne(S0[:320]) - moyenne(H[:320]) dans R^256
w_signal = 2.0; w_bruit = math.sqrt(256 * 2 / 320); norme_w = math.sqrt(w_signal ** 2 + w_bruit ** 2)
sd_moy = norme_w / math.sqrt(640)                       # bruit d'action de la moyenne d'un adaptateur
sd_idio = math.sqrt(2 / 320) * 2 / math.sqrt(2)         # composante de bruit de w le long de la direction propre i_k
sd_adapt = math.sqrt(sd_moy ** 2 + sd_idio ** 2)
ecart = w_signal * (1 - 0.9) * 1.0                      # temoin a 90 % : 0,1 x la projection commune (2)
z = ecart / (sd_adapt * math.sqrt(2 / 4))
sortie["bloc4_piege_intensite_monde_C"] = {"ecart_moyen": round(ecart, 3), "ecart_type_entre_adaptateurs": round(sd_adapt, 3),
                                          "ecart_en_ecarts_types": round(ecart / sd_adapt, 2),
                                          "puissance_normale_4_contre_4_unilaterale_5pc": round(1 - ND.cdf(1.645 - z), 3)}

# ---- Bloc 5 : estimer une variance entre graines avec deux adaptateurs par bras (un degre de liberte)
chi2_1 = lambda q: ND.inv_cdf((1 + q) / 2) ** 2          # quantile exact du khi-deux a un degre
chi2_2 = lambda q: -2 * math.log(1 - q)                     # quantile exact du khi-deux a deux degres
lo, hi = chi2_1(0.025), chi2_1(0.975)
sortie["bloc5_variance_un_degre"] = {"facteur_intervalle_95_variance": round(hi / lo, 0), "facteur_ecart_type": round(math.sqrt(hi / lo), 1),
                                     "deux_degres": round(chi2_2(0.975) / chi2_2(0.025), 0)}

# ---- Bloc 6 : l'appariement par texte (O_S et J ont les memes jetons ; A et O_H aussi), ignore par la conception A,
# reduit-il l'ecart type de B = aire(O_S, A) - aire(J, O_H) ? loi inventee, sans effet vrai
def sim_B(r_texte, rep=600, cle=0):
    g = gen(6, cle); out = []
    for _ in range(rep):
        u = g.normal(0, math.sqrt(0.2), (64, 1))
        ts = g.normal(0, 1, (64, 10)); th = g.normal(0, 1, (64, 10))           # texte du saboteur, texte honnete
        def cell(t):
            return (u + math.sqrt(r_texte * 0.8) * t + math.sqrt((1 - r_texte) * 0.8) * g.normal(0, 1, (64, 10))).ravel()
        OS, J, A, OH = cell(ts), cell(ts), cell(th), cell(th)
        out.append(aire(OS, A) - aire(J, OH))
    return round(float(np.std(out)), 4)
sortie["bloc6_ecart_type_de_B_selon_partage_du_texte"] = {f"part_du_texte_{r}": sim_B(r, cle=int(r * 10)) for r in (0.0, 0.5, 0.9)}

print(json.dumps(sortie, indent=1, ensure_ascii=False))
json.dump(sortie, open("/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/barreau5-concevoir/sortie-contre-lecture-calculs-v1.json", "w"), indent=1, ensure_ascii=False)
