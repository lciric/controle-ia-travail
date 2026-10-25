"""Faits mécaniques du pilote 3 pour le devis et le temps du pilote 4 (contre-lecture 1, P4C1-02 b et P4C1-03) — v1.

Lit les deux extraits mécaniques du pilote 3 (`extrait-mecanique-v1.json` des courses v5.3 et v6, liste close de
champs sans score, écrits par `essaim_m3.outils.extrait_mecanique`) et n'en recopie que : par génération, la durée
d'exécution, le coût, le nombre d'appels, les appels par statut, les durées des appels (somme, minimum, maximum), les
recherches et téléchargements par source et par statut, les appels simultanés au plus ; les étapes et heures des
événements ; les budgets du manifeste ; l'heure de fin, la dépense totale et le nombre d'appels du rapport. Aucun champ
écrit par l'organisme (ni `organisme`, ni `fichiers_travail`, ni `question_ouverte`, ni `successeur`) n'est lu ni recopié.

Usage : python3 -I extraire_faits_mecaniques_pilote3_v1.py EXTRAIT_V53 EXTRAIT_V6 > faits-mecaniques-pilote3-v1.json
"""
import hashlib, json, pathlib, sys

def faits(chemin):
    p = pathlib.Path(chemin); d = json.loads(p.read_text(encoding="utf-8"))
    gens = []
    for g in d["generations"]:
        a = g.get("appels") or {}; x = g.get("execution") or {}; s = g.get("services") or {}
        gens.append({"generation": g["generation"], "phase": g.get("phase"), "code": x.get("code"), "duree_s": x.get("duree_s"),
                     "delai_depasse": x.get("delai_depasse"), "cout_usd": g.get("cout_usd"), "n_appels": g.get("n_appels"),
                     "appels_par_statut": a.get("par_statut"), "durees_appels_s": a.get("durees_s"),
                     "recherches": s.get("recherches"), "telechargements": s.get("telechargements"),
                     "appels_simultanes_max": g.get("appels_simultanes_max")})
    m = d.get("manifeste") or {}; r = d.get("rapport") or {}
    return {"extrait": p.name, "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "course": d.get("course"),
            "evenements": [{"etape": e.get("etape"), "quand_utc": e.get("quand_utc")} for e in d.get("evenements", [])],
            "generations": gens,
            "manifeste": {k: m.get(k) for k in ("budget_generation", "budget_conception", "generations_max", "rondes_conception_max", "plafond_total_usd", "sources_moisson")},
            "rapport": {k: r.get(k) for k in ("fin_utc", "depense_totale_usd", "n_appels_total", "rondes_conception")}}

print(json.dumps({"v5-3": faits(sys.argv[1]), "v6": faits(sys.argv[2])}, ensure_ascii=False, indent=1))
