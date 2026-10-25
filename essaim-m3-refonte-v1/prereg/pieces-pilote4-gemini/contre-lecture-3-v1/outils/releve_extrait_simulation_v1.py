# Relevé mécanique d'un extrait de SIMULATION (lecture seule) : événements d'arrêt, de reprise, de fin de conception ;
# unités archivées (phase, numéro, appels). N'imprime aucun champ de score.
import json, sys
x = json.load(open(sys.argv[1], encoding="utf-8"))
for e in x.get("evenements", []):
    et = e.get("etape")
    if et in ("arret", "arret_conception", "reprise", "fin_conception", "ronde_conception", "ronde"):
        d = {k: e.get(k) for k in ("etape", "ronde", "raison", "segment", "etat", "conception_faite", "prochaine_ronde_conception", "ronde_en_cours", "depense_relue_usd", "n_appels_relus", "ordre") if k in e}
        if et == "fin_conception":
            dec = e.get("declaration") or {}
            d["cles_declaration"] = sorted(dec)[:12]
            d["critere"] = dec.get("critere")
            d["n_exemplaires"] = dec.get("n_exemplaires", dec.get("exemplaires"))
            d["sondes_traits_actives"] = dec.get("sondes_traits_actives")
            d["exactitude_moyenne_sonde"] = dec.get("exactitude_moyenne_sonde")
        print(json.dumps(d, ensure_ascii=False))
for g in x.get("generations", []):
    print("unité", g.get("phase"), g.get("generation"), "statut", g.get("statut"), "appels", (g.get("appels") or {}).get("n"), "cout", (g.get("appels") or {}).get("cout_usd"))
r = x.get("rapport") or {}
print("rapport", r.get("fichier"), "dépense", r.get("depense_totale_usd"), "n_appels", r.get("n_appels_total"), "lignées", json.dumps(r.get("lignees"), ensure_ascii=False))
