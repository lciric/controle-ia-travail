"""Diagnostic du juge (processeur seul, racines d'essai, aucun appel de modèle). Non vérifié par un tiers :
à refaire par Opus avant toute citation dans un texte scellé. Lit le paquet figé oracles_plantes_v6 sans le modifier."""
import sys, math, re, json
from fractions import Fraction
from collections import defaultdict, Counter
from controle_ia.oracles_plantes_v6 import banque, parametres
from controle_ia.oracles_plantes_v6.forme_seule import BayesNaif, jetons_de_style, aire_sous_la_courbe
from controle_ia.oracles_plantes_v6.graines import generateur

p, _ = parametres.charger()
ANALYS = ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE")
FAM = lambda w: ("F1", "F2", "F3")[w // 4]

def auc(pos, neg):
    a = aire_sous_la_courbe(pos, neg)
    return None if a is None else float(a)

def rappel_a_fa(pos, neg, fa_max):
    """Meilleur rappel sur pos à fausses alarmes <= fa_max sur neg (seuil choisi a posteriori : borne optimiste)."""
    if not pos or not neg: return None
    best = 0.0
    for s in sorted(set(neg) | set(pos), reverse=True):
        fa = sum(1 for q in neg if q >= s) / len(neg)
        if fa <= fa_max:
            best = max(best, sum(1 for x in pos if x >= s) / len(pos))
    # seuil au-dessus de tout score négatif
    return best

def chiffres_max(texte):
    return max((len(x) for x in re.findall(r"\d+", texte)), default=0)

racines = [int(x) for x in sys.argv[1].split(",")]
res = []
poids_cumules = Counter()
for r in racines:
    B = banque.construire_banque(r, p)
    rng = generateur(r, 10, 0)
    plis = 4
    ordre = [int(i) for i in rng.permutation(len(B))]
    pli_de = {w: k % plis for k, w in enumerate(ordre)}
    tous = defaultdict(list); hv = defaultdict(list); par_fam = defaultdict(lambda: defaultdict(list))
    gab_hv = Counter(); gab_tous = Counter()
    for k in range(plis):
        app = [(x.texte, x.etiquette != "VERITE_PLANTEE") for w, (_m, pl) in enumerate(B) if pli_de[w] != k for x in pl if x.etiquette in ANALYS]
        vus = {t for t, _ in app}
        mod = BayesNaif(Fraction(1)).apprendre([t for t, _ in app], [y for _, y in app])
        if k == 0:
            # poids : log-rapport de vraisemblance par jeton
            voc = set(mod.compte[True]) | set(mod.compte[False])
            for j in voc:
                pf = (mod.compte[True].get(j, 0) + 1) / (mod.total[True] + mod.V)
                pv = (mod.compte[False].get(j, 0) + 1) / (mod.total[False] + mod.V)
                poids_cumules[j] += math.log(pf / pv)
        for w, (_m, pl) in enumerate(B):
            if pli_de[w] != k: continue
            for x in pl:
                if x.etiquette not in ANALYS: continue
                s = mod.score(x.texte)
                tous[x.etiquette].append(s); par_fam[FAM(w)][x.etiquette].append(s)
                gab_tous[(x.etiquette, x.gabarit)] += 1
                if x.texte not in vus:
                    hv[x.etiquette].append(s); gab_hv[(x.etiquette, x.gabarit)] += 1
    faux_tous = tous["FAUX_TOT"] + tous["PIEGE"]; faux_hv = hv["FAUX_TOT"] + hv["PIEGE"]
    # règle numérique triviale : nombre de chiffres du plus grand littéral (sans apprentissage)
    dig = defaultdict(list)
    for w, (_m, pl) in enumerate(B):
        for x in pl:
            if x.etiquette in ANALYS: dig[x.etiquette].append(chiffres_max(x.texte))
    ligne = {
        "racine": r,
        "n_hv": {e: len(hv[e]) for e in ANALYS},
        "hv_pieges_v": auc(hv["PIEGE"], hv["VERITE_PLANTEE"]), "hv_fauxtot_v": auc(hv["FAUX_TOT"], hv["VERITE_PLANTEE"]),
        "hv_global": auc(faux_hv, hv["VERITE_PLANTEE"]),
        "tous_pieges_v": auc(tous["PIEGE"], tous["VERITE_PLANTEE"]), "tous_fauxtot_v": auc(tous["FAUX_TOT"], tous["VERITE_PLANTEE"]),
        "tous_global": auc(faux_tous, tous["VERITE_PLANTEE"]),
        "tous_pieges_vs_fauxtot": auc(tous["PIEGE"], tous["FAUX_TOT"]),
        "rappel_fa10_tous": rappel_a_fa(faux_tous, tous["VERITE_PLANTEE"], 0.10),
        "rappel_fa05_tous": rappel_a_fa(faux_tous, tous["VERITE_PLANTEE"], 0.05),
        "rappel_fa10_pieges": rappel_a_fa(tous["PIEGE"], tous["VERITE_PLANTEE"], 0.10),
        "rappel_fa10_fauxtot": rappel_a_fa(tous["FAUX_TOT"], tous["VERITE_PLANTEE"], 0.10),
        "par_famille_global": {f: auc(par_fam[f]["FAUX_TOT"] + par_fam[f]["PIEGE"], par_fam[f]["VERITE_PLANTEE"]) for f in ("F1", "F2", "F3")},
        "chiffres_pieges_v": auc(dig["PIEGE"], dig["VERITE_PLANTEE"]), "chiffres_fauxtot_v": auc(dig["FAUX_TOT"], dig["VERITE_PLANTEE"]),
        "chiffres_pieges_vs_fauxtot": auc(dig["PIEGE"], dig["FAUX_TOT"]),
    }
    res.append(ligne)
    if r == racines[0]:
        print("== gabarits des vérités restant hors textes vus (racine %d) :" % r)
        for (e, g), n in sorted(gab_hv.items()):
            print(f"   {e:15s} {g:48s} hors vus {n} / {gab_tous[(e, g)]}")
def moy(c): 
    v = [x[c] for x in res if x[c] is not None]; return (round(min(v), 3), round(sum(v) / len(v), 3), round(max(v), 3))
print("racines :", racines)
for c in ("hv_pieges_v", "hv_fauxtot_v", "hv_global", "tous_pieges_v", "tous_fauxtot_v", "tous_global", "tous_pieges_vs_fauxtot",
          "rappel_fa10_tous", "rappel_fa05_tous", "rappel_fa10_pieges", "rappel_fa10_fauxtot", "chiffres_pieges_v", "chiffres_fauxtot_v", "chiffres_pieges_vs_fauxtot"):
    print(f"{c:28s} min, moyenne, max = {moy(c)}")
for f in ("F1", "F2", "F3"):
    v = [x["par_famille_global"][f] for x in res]; print(f"aire globale (tous textes) famille {f} : min {min(v):.3f} moy {sum(v)/len(v):.3f} max {max(v):.3f}")
print("effectifs hors vus :", [x["n_hv"] for x in res][:3])
top = sorted(poids_cumules.items(), key=lambda kv: kv[1])
n = len(racines)
print("== jetons les plus « vrai » (log-rapport moyen, pli 0) :")
for j, v in top[:14]: print(f"   {v/n:+.2f}  {j}")
print("== jetons les plus « faux » :")
for j, v in top[-14:][::-1]: print(f"   {v/n:+.2f}  {j}")
json.dump(res, open(sys.argv[2], "w"), indent=1)
