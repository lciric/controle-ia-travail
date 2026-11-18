"""Dépense du pilote MR-2 (procédure v14) — v1, compte organisme. Bibliothèque standard seule ; ne lit **que** les pièces de coût du
dossier rapatrié (`releve-pilote-v70.json`, `journal-relais-*.jsonl`) ; n'ouvre jamais `lecture-pilote-v70.json`,
`sortie-mesure-pilote-v70.json`, `mesure-pilote-v70.json`, ni `remis-au-sous-agent/` (l'issue n'est pas lue ici).

Rapproche, par proposeur : la dépense du relevé du pilote (`depense_usd`), la somme des coûts des journaux des relais, la somme des
coûts des appels du relevé ; contrôle les parts (GO-2026-11-14-13 : `fable52` 12, `opus55` 8, π1 20 USD ; GO-2026-11-14-14 : `argon`
9,36, `astra` 9,36, machine 3, π2 21,72 USD) ; ajoute la machine (prix horaire × durée, arguments) et, s'ils sont donnés, les autres
frais du même pilote (épreuve des clés, machines des tentatives précédentes). Les montants facturés font foi à la console (R-2803).

Usage : python3 -I -B depense_pilote_v14_v1.py RAPATRIE_REEL SORTIE.json --machine PRIX_USD_H CREATION_UTC DESTRUCTION_UTC
        [--autre LIBELLE MONTANT_USD]…
"""
import datetime
import glob
import json
import os
import sys

PARTS = {"fable52": 12.0, "opus55": 8.0, "argon": 9.36, "astra": 9.36}
PI1, PI2, MACHINE = 20.0, 21.72, 3.0
INTERDITS = ("lecture-pilote-v70.json", "sortie-mesure-pilote-v70.json", "mesure-pilote-v70.json")


def heure(x):
    return datetime.datetime.fromisoformat(x.replace("Z", "+00:00"))


def main(a):
    if len(a) < 6 or a[2] != "--machine":
        print("REFUS : usage")
        return 2
    dossier, sortie, prix, debut, fin = a[0], a[1], float(a[3]), a[4], a[5]
    autres, reste = [], a[6:]
    while reste:
        if reste[0] != "--autre" or len(reste) < 3:
            print("REFUS : --autre LIBELLE MONTANT")
            return 2
        autres.append((reste[1], float(reste[2])))
        reste = reste[3:]
    releve = json.load(open(os.path.join(dossier, "releve-pilote-v70.json"), encoding="utf-8"))
    par = {}
    for n in PARTS:
        j = os.path.join(dossier, f"journal-relais-{n}.jsonl")
        lignes = [json.loads(l) for l in open(j, encoding="utf-8") if l.strip()] if os.path.exists(j) else []
        appels = [x for x in releve.get("appels", []) if x.get("proposeur") == n]
        par[n] = {"releve_depense_usd": round(float((releve.get("depense_usd") or {}).get(n, 0.0)), 6),
                  "journal_relais_usd": round(sum(float(x.get("cout_usd") or 0) for x in lignes), 6),
                  "journal_relais_lignes": len(lignes),
                  "journal_au_dessus_du_pire_cas": sum(1 for x in lignes if x.get("au_dessus_du_pire_cas")),
                  "appels_releve_usd": round(sum(float(x.get("cout_usd") or 0) for x in appels), 6),
                  "appels": len(appels), "appeles": sum(1 for x in appels if x.get("appele")),
                  "etats": {e: sum(1 for x in appels if x.get("etat") == e) for e in ("complet", "tronque", "echec")},
                  "part_usd": PARTS[n]}
        p = par[n]
        p["ecart_releve_journal_usd"] = round(p["releve_depense_usd"] - p["journal_relais_usd"], 6)
        p["sous_la_part"] = max(p["releve_depense_usd"], p["journal_relais_usd"]) <= PARTS[n] + 1e-9
    duree_h = (heure(fin) - heure(debut)).total_seconds() / 3600.0
    machine = round(prix * duree_h, 6)
    m = lambda n: max(par[n]["releve_depense_usd"], par[n]["journal_relais_usd"])  # noqa: E731
    pi1 = round(m("fable52") + m("opus55"), 6)
    pi2 = round(m("argon") + m("astra") + machine + sum(v for _, v in autres), 6)
    res = {"version": "depense-pilote-v14-v1", "proposeurs": par, "machine": {"prix_usd_h": prix, "creation_utc": debut,
           "destruction_utc": fin, "duree_h": round(duree_h, 4), "cout_usd": machine, "sous_la_part": machine <= MACHINE},
           "autres": [{"libelle": l, "usd": v} for l, v in autres],
           "pi1_credits_claude_usd": pi1, "pi1_sous_la_ligne": pi1 <= PI1, "pi2_hors_credits_usd": pi2, "pi2_sous_la_ligne": pi2 <= PI2,
           "total_usd": round(pi1 + pi2, 6), "note": "estimation aux prix de la configuration ; les montants facturés font foi à la console (R-2803)",
           "fichiers_non_ouverts": [x for x in INTERDITS if os.path.exists(os.path.join(dossier, x))]}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    for n, p in par.items():
        print(f"{n:8s} relevé {p['releve_depense_usd']:.6f}  relais {p['journal_relais_usd']:.6f}  écart {p['ecart_releve_journal_usd']:+.6f}  "
              f"appels {p['appeles']}/{p['appels']}  {p['etats']}  part {p['part_usd']}  {'sous la part' if p['sous_la_part'] else 'PART DÉPASSÉE'}")
    print(f"machine {machine:.6f} USD ({duree_h:.3f} h à {prix} USD/h) ; π1 {pi1:.6f} / {PI1} ; π2 {pi2:.6f} / {PI2} ; total {res['total_usd']:.6f}")
    return 0 if (all(p["sous_la_part"] for p in par.values()) and res["pi1_sous_la_ligne"] and res["pi2_sous_la_ligne"]
                 and res["machine"]["sous_la_part"]) else 3


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
