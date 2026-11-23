"""Diagnostic du juge sur l'effet de forme de la banque d'énoncés plantés (version 6 du générateur).

Processeur seul, racines d'essai seulement, aucun appel de modèle, aucune dépense, aucune banque réelle ni clé réelle.
Écrit le 2026-11-22 par le juge de l'étage 4 (GO-2026-11-22-112) pour éclairer son avis sur le seuil de 0,75 ; non vérifié par un tiers :
à refaire par le vérificateur du code avant toute citation dans un texte scellé.

Lit sans le modifier le paquet figé `src/controle_ia/oracles_plantes_v6/` (commit 35ac9e10738ccaac486ec9b9684fe70441f6371a,
branche claude/mathematiques-nouvelles-v1). Le classifieur est celui du paquet (`forme_seule.BayesNaif`, lissage 1, 4 plis
par mondes entiers tirés par l'enfant (10, 0) des graines), sans changement.

Emploi : PYTHONPATH=<arbre de la branche>/src python3 juge-fable-max-v1-diagnostic-style.py 0,1,2,... sortie.json
"""
import sys, math, re, json
from fractions import Fraction
from collections import defaultdict, Counter
from controle_ia.oracles_plantes_v6 import banque, parametres
from controle_ia.oracles_plantes_v6.forme_seule import BayesNaif, jetons_de_style, aire_sous_la_courbe
from controle_ia.oracles_plantes_v6.grammaire import lexer
from controle_ia.oracles_plantes_v6.graines import generateur

p, _ = parametres.charger()
ANALYS = ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE")


def famille(w):
    return ("F1", "F2", "F3")[w // 4]


def aire(pos, neg):
    a = aire_sous_la_courbe(pos, neg)
    return None if a is None else float(a)


def rappel_a_fausses_alarmes(pos, neg, plafond):
    """Meilleur rappel sur `pos` à taux de fausses alarmes <= plafond sur `neg`. Le seuil de score est choisi après coup :
    c'est une borne optimiste de ce qu'une règle de forme atteint, pas une mesure calibrée."""
    if not pos or not neg:
        return None
    meilleur = 0.0
    for s in sorted(set(neg) | set(pos), reverse=True):
        if sum(1 for q in neg if q >= s) / len(neg) <= plafond:
            meilleur = max(meilleur, sum(1 for x in pos if x >= s) / len(pos))
    return meilleur


def chiffres_du_plus_grand_litteral(texte):
    return max((len(x) for x in re.findall(r"\d+", texte)), default=0)


def squelette(texte, grossier):
    """Suite de jetons, nombres masqués. Grossier : un rationnel entre parenthèses « ( NUM / NUM ) » devient « NUM »."""
    toks = ["NUM" if g == "nombre" else v for g, v in lexer(texte)]
    s = " ".join(toks)
    if grossier:
        s = s.replace("( NUM / NUM )", "NUM")
    return s


racines = [int(x) for x in sys.argv[1].split(",")]
lignes = []
poids = Counter()
gabarits_par_strate = defaultdict(set)
partages = {"fin": [], "grossier": []}
for r in racines:
    B = banque.construire_banque(r, p)
    rng = generateur(r, 10, 0)
    plis = 4
    ordre = [int(i) for i in rng.permutation(len(B))]
    pli_de = {w: k % plis for k, w in enumerate(ordre)}
    tous = defaultdict(list)
    hors_vus = defaultdict(list)
    par_famille = defaultdict(lambda: defaultdict(list))
    for k in range(plis):
        app = [(x.texte, x.etiquette != "VERITE_PLANTEE") for w, (_m, pl) in enumerate(B) if pli_de[w] != k
               for x in pl if x.etiquette in ANALYS]
        vus = {t for t, _ in app}
        modele = BayesNaif(Fraction(1)).apprendre([t for t, _ in app], [y for _, y in app])
        if k == 0:
            for j in set(modele.compte[True]) | set(modele.compte[False]):
                pf = (modele.compte[True].get(j, 0) + 1) / (modele.total[True] + modele.V)
                pv = (modele.compte[False].get(j, 0) + 1) / (modele.total[False] + modele.V)
                poids[j] += math.log(pf / pv)
        for w, (_m, pl) in enumerate(B):
            if pli_de[w] != k:
                continue
            for x in pl:
                if x.etiquette not in ANALYS:
                    continue
                s = modele.score(x.texte)
                tous[x.etiquette].append(s)
                par_famille[famille(w)][x.etiquette].append(s)
                if x.texte not in vus:
                    hors_vus[x.etiquette].append(s)
    chiffres = defaultdict(list)
    sq = {"fin": defaultdict(set), "grossier": defaultdict(set)}
    for w, (_m, pl) in enumerate(B):
        for x in pl:
            if x.etiquette not in ANALYS:
                continue
            gabarits_par_strate[x.etiquette].add((famille(w), x.gabarit))
            chiffres[x.etiquette].append(chiffres_du_plus_grand_litteral(x.texte))
            classe = "vrai" if x.etiquette == "VERITE_PLANTEE" else "faux"
            for g in ("fin", "grossier"):
                sq[g][classe].add((famille(w), squelette(x.texte, g == "grossier")))
    for g in ("fin", "grossier"):
        partages[g].append(len(sq[g]["vrai"] & sq[g]["faux"]))
    faux_t = tous["FAUX_TOT"] + tous["PIEGE"]
    faux_hv = hors_vus["FAUX_TOT"] + hors_vus["PIEGE"]
    V = "VERITE_PLANTEE"
    lignes.append({
        "racine": r,
        "effectifs_hors_textes_vus": {e: len(hors_vus[e]) for e in ANALYS},
        "aire_hors_vus_pieges": aire(hors_vus["PIEGE"], hors_vus[V]),
        "aire_hors_vus_faux_tot": aire(hors_vus["FAUX_TOT"], hors_vus[V]),
        "aire_hors_vus_tous_faux": aire(faux_hv, hors_vus[V]),
        "aire_tous_textes_pieges": aire(tous["PIEGE"], tous[V]),
        "aire_tous_textes_faux_tot": aire(tous["FAUX_TOT"], tous[V]),
        "aire_tous_textes_tous_faux": aire(faux_t, tous[V]),
        "aire_pieges_contre_faux_tot": aire(tous["PIEGE"], tous["FAUX_TOT"]),
        "rappel_a_10_tous_faux": rappel_a_fausses_alarmes(faux_t, tous[V], 0.10),
        "rappel_a_5_tous_faux": rappel_a_fausses_alarmes(faux_t, tous[V], 0.05),
        "rappel_a_10_pieges": rappel_a_fausses_alarmes(tous["PIEGE"], tous[V], 0.10),
        "rappel_a_10_faux_tot": rappel_a_fausses_alarmes(tous["FAUX_TOT"], tous[V], 0.10),
        "aire_tous_faux_par_famille": {f: aire(par_famille[f]["FAUX_TOT"] + par_famille[f]["PIEGE"], par_famille[f][V])
                                       for f in ("F1", "F2", "F3")},
        "chiffres_aire_pieges": aire(chiffres["PIEGE"], chiffres[V]),
        "chiffres_aire_faux_tot": aire(chiffres["FAUX_TOT"], chiffres[V]),
        "chiffres_aire_pieges_contre_faux_tot": aire(chiffres["PIEGE"], chiffres["FAUX_TOT"]),
        "chiffres_rappel_a_10_pieges": rappel_a_fausses_alarmes(chiffres["PIEGE"], chiffres[V], 0.10),
    })


def resume(cle, sous=None):
    v = [(x[cle][sous] if sous else x[cle]) for x in lignes]
    v = [a for a in v if a is not None]
    return f"min {min(v):.3f} ; moyenne {sum(v) / len(v):.3f} ; max {max(v):.3f}"


print(f"Diagnostic du juge — {len(racines)} racines d'essai : {racines}")
print("Paquet : oracles_plantes_v6 ; classifieur du paquet, 4 plis par mondes entiers, lissage 1.")
print()
print("1. Aires du classifieur de style (bayésien naïf sur jetons, nombres masqués)")
foi = [max(x["aire_hors_vus_pieges"], x["aire_hors_vus_faux_tot"]) for x in lignes]
print(f"   aire qui fait foi (plus grande des deux strates, hors textes vus) : min {min(foi):.3f} ; moyenne {sum(foi)/len(foi):.3f} ; max {max(foi):.3f}")
for cle, nom in (("aire_hors_vus_pieges", "hors textes vus, pièges contre vérités"),
                 ("aire_hors_vus_faux_tot", "hors textes vus, faux tôt contre vérités"),
                 ("aire_hors_vus_tous_faux", "hors textes vus, tous les faux contre vérités"),
                 ("aire_tous_textes_pieges", "tous textes, pièges contre vérités"),
                 ("aire_tous_textes_faux_tot", "tous textes, faux tôt contre vérités"),
                 ("aire_tous_textes_tous_faux", "tous textes, tous les faux contre vérités"),
                 ("aire_pieges_contre_faux_tot", "tous textes, pièges contre faux tôt")):
    print(f"   {nom:50s} : {resume(cle)}")
for f in ("F1", "F2", "F3"):
    print(f"   tous textes, tous les faux contre vérités, famille {f} : {resume('aire_tous_faux_par_famille', f)}")
print(f"   effectifs hors textes vus (trois premières racines) : {[x['effectifs_hors_textes_vus'] for x in lignes[:3]]}")
print()
print("2. Rappel du même classifieur à fausses alarmes plafonnées (seuil choisi après coup : borne optimiste)")
for cle, nom in (("rappel_a_10_tous_faux", "tous les faux, fausses alarmes <= 0,10"),
                 ("rappel_a_5_tous_faux", "tous les faux, fausses alarmes <= 0,05"),
                 ("rappel_a_10_pieges", "pièges, fausses alarmes <= 0,10"),
                 ("rappel_a_10_faux_tot", "faux tôt, fausses alarmes <= 0,10")):
    print(f"   {nom:50s} : {resume(cle)}")
print()
print("3. Règle numérique sans apprentissage : nombre de chiffres du plus grand littéral de l'énoncé")
for cle, nom in (("chiffres_aire_pieges", "aire, pièges contre vérités"),
                 ("chiffres_aire_faux_tot", "aire, faux tôt contre vérités"),
                 ("chiffres_aire_pieges_contre_faux_tot", "aire, pièges contre faux tôt"),
                 ("chiffres_rappel_a_10_pieges", "rappel sur les pièges, fausses alarmes <= 0,10")):
    print(f"   {nom:50s} : {resume(cle)}")
print()
print("4. Gabarits et squelettes")
communs = (gabarits_par_strate["VERITE_PLANTEE"] & gabarits_par_strate["FAUX_TOT"]) | \
          (gabarits_par_strate["VERITE_PLANTEE"] & gabarits_par_strate["PIEGE"]) | \
          (gabarits_par_strate["FAUX_TOT"] & gabarits_par_strate["PIEGE"])
print(f"   gabarits (famille, nom) par strate : vérités {len(gabarits_par_strate['VERITE_PLANTEE'])}, faux tôt {len(gabarits_par_strate['FAUX_TOT'])}, pièges {len(gabarits_par_strate['PIEGE'])} ; gabarits présents dans deux strates : {len(communs)}")
print(f"   squelettes (jetons, nombres masqués) communs à une vérité et à un faux, par racine : min {min(partages['fin'])}, max {max(partages['fin'])}")
print(f"   idem, rationnel entre parenthèses ramené à un seul jeton : min {min(partages['grossier'])}, max {max(partages['grossier'])}")
print()
tri = sorted(poids.items(), key=lambda kv: kv[1])
n = len(racines)
print("5. Poids du classifieur (logarithme du rapport de vraisemblance faux / vrai, moyenne sur les racines, pli 0)")
print("   jetons les plus « vrai » :")
for j, v in tri[:12]:
    print(f"      {v / n:+.2f}  {j}")
print("   jetons les plus « faux » :")
for j, v in tri[-12:][::-1]:
    print(f"      {v / n:+.2f}  {j}")
json.dump({"racines": racines, "lignes": lignes}, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
