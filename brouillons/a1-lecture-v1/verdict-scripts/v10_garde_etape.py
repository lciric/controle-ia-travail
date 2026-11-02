"""v10 — addendum (lecteur du verdict, R13) : le plafond d'étape du registre de dépense, au fil du temps.
Pour chaque début d'appel inscrit au registre : étape, plafond d'étape inscrit, réglé (somme des coûts des appels finis
avant ce début, les deux fournisseurs de l'étape) et engagé (somme des pires cas des appels commencés et non finis), puis
le test « réglé + engagé + pire cas du nouvel appel ≤ plafond d'étape » sous trois règles : somme de l'étape (les deux
fournisseurs), part par fournisseur, plafond cumulé de 80. État après le dernier appel inscrit ; marge d'Argon à sa fin.
Bras Argon : suites complètes ? Appels Kimi de la sortie au-delà du registre : statuts, coûts, essais.
Usage : python3 -I -B v10_garde_etape.py REGISTRE.jsonl SORTIE.json SORTIE_JSON"""
import json
import sys
from collections import Counter
from datetime import datetime

reg = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
sortie = json.load(open(sys.argv[2], encoding="utf-8"))
t = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))  # noqa: E731
debuts = {e["id"]: e for e in reg if e["type"] == "debut"}
fins = {e["id"]: e for e in reg if e["type"] == "fin"}
etapes = Counter(e["etape"] for e in debuts.values())
plafonds = Counter(e["plafond_etape_usd"] for e in debuts.values())
ev = sorted([(t(d["quand_utc"]), 1, i) for i, d in debuts.items()] + [(t(f["quand_utc"]), 0, i) for i, f in fins.items()])
regle, engage, ouverts = 0.0, 0.0, {}
par_f = Counter()
marge_min = {"somme_etape": (1e9, None), "par_fournisseur": (1e9, None)}
viol = {"somme_etape": [], "par_fournisseur": [], "cumul_80": []}
for quand, typ, i in ev:
    d = debuts[i]
    f = d["fournisseur"]
    if typ == 1:
        pire = d["pire_cas_usd"]
        eng_f = sum(debuts[j]["pire_cas_usd"] for j in ouverts if debuts[j]["fournisseur"] == f)
        s_etape = regle + engage + pire
        s_f = par_f[f] + eng_f + pire
        if s_etape > d["plafond_etape_usd"] + 1e-12:
            viol["somme_etape"].append((quand.isoformat(), f, round(s_etape, 6)))
        if s_f > d["plafond_etape_usd"] + 1e-12:
            viol["par_fournisseur"].append((quand.isoformat(), f, round(s_f, 6)))
        if s_etape > 80 + 1e-12:
            viol["cumul_80"].append((quand.isoformat(), f, round(s_etape, 6)))
        m = d["plafond_etape_usd"] - s_etape
        if m < marge_min["somme_etape"][0]:
            marge_min["somme_etape"] = (round(m, 6), quand.isoformat(), f)
        ouverts[i] = True
        engage += pire
    else:
        fin = fins[i]
        regle += fin["cout_usd"]
        par_f[f] += fin["cout_usd"]
        engage -= debuts[i]["pire_cas_usd"]
        ouverts.pop(i, None)
    if quand.strftime("%H:%M:%S") <= "11:05:17" and f == "argon":
        etat_argon = (quand.isoformat(), round(regle, 6), round(engage, 6), {k: round(v, 6) for k, v in par_f.items()})
kimi_pire = sorted({round(d["pire_cas_usd"], 6) for d in debuts.values() if d["fournisseur"] == "kimi"})
argon_pire = [d["pire_cas_usd"] for d in debuts.values() if d["fournisseur"] == "argon"]
fin_etat = {"regle_total": round(regle, 6), "engage": round(engage, 6), "par_fournisseur": {k: round(v, 6) for k, v in par_f.items()},
            "plus_petit_pire_cas_kimi": min(kimi_pire), "plus_grand_pire_cas_kimi": max(kimi_pire),
            "regle_plus_plus_petit_pire_cas_kimi": round(regle + min(kimi_pire), 6)}
# Argon : marge à la fin de ses appels (réglé + engagé Kimi + pire cas Argon médian)
argon_pire_med = sorted(argon_pire)[len(argon_pire) // 2]
# bras Argon : suites complètes
sa = [s for s in sortie["suites"] if s["fournisseur"] == "argon"]
completes = sum(1 for s in sa if s["premiere_promotion"] is not None or len(s["tentatives"]) == 16)
echouees_a = sum(1 for s in sa for x in s["tentatives"] if x["loi"] is None and (x["motif_invalidite"] or "").startswith("appel échoué"))
# appels Kimi de la sortie dans l'ordre de jeu : les 621 premiers sont au registre (appariement A §2), les suivants non
ordre = {(w, c, cond, j): n for n, (w, c, cond, j) in enumerate((w, c, cond, j) for w in ("W1", "W2") for c in range(12)
                                                                for cond, j in (("temoin", "v8"), ("retour", "v8"), ("temoin", "v7"), ("retour", "v7")))}
sk = sorted([s for s in sortie["suites"] if s["fournisseur"] == "kimi"], key=lambda s: ordre[(s["monde"], s["carte"], s["condition"], s["juge"])])
appels_k = [(s["monde"], s["carte"], s["condition"], s["juge"], x["k"], a) for s in sk for x in s["tentatives"] for a in x["appels"]]
apres = appels_k[621:]
res = {"etapes": dict(etapes), "plafonds_etape_inscrits": {str(k): v for k, v in plafonds.items()},
       "violations_si_regle": {k: (len(v), v[:3]) for k, v in viol.items()},
       "marge_minimale_somme_etape_sur_les_appels_inscrits": marge_min["somme_etape"],
       "etat_apres_dernier_appel_inscrit": fin_etat,
       "etat_a_la_fin_d_argon": etat_argon, "pire_cas_argon_median": argon_pire_med,
       "marge_argon_apres_sa_fin": round(40 - (etat_argon[1] + etat_argon[2] + argon_pire_med), 6),
       "argon": {"suites": len(sa), "completes": completes, "tentatives_echouees": echouees_a},
       "kimi_appels_sortie": len(appels_k), "kimi_621e_appel": appels_k[620][:5],
       "kimi_premier_hors_registre": appels_k[621][:5] if len(appels_k) > 621 else None,
       "kimi_hors_registre": {"n": len(apres), "statuts": dict(Counter(a["statut"] for *_, a in apres)),
                              "couts": dict(Counter(a["cout_usd"] for *_, a in apres)),
                              "essais": dict(Counter(a["essai_d_appel"] for *_, a in apres)),
                              "budget_depasse": sum(a["statut"] == "budget_depasse" for *_, a in apres)}}
json.dump(res, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
print(json.dumps(res, ensure_ascii=False, indent=1, default=str))
