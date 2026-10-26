"""Tableau des cellules d'un run du collisionneur, tiré de journal.jsonl (dernière entrée par cellule) ; aucune réponse lue.
Usage : python3 -I tableau_run_v1.py RUN"""
import json, sys, pathlib
lignes = [e for e in (json.loads(l) for l in pathlib.Path(sys.argv[1], "journal.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()) if "statut" in e and "cellule" in e]
der = {}
for e in lignes:
    der[e["cellule"]] = e
total = sum(e.get("cout_usd") or 0 for e in lignes)
print("| cellule | modèle | statut | jetons de sortie | coût |\n|---|---|---|---|---|")
for c, e in der.items():
    st = e["statut"] if e["statut"] == "OK" else f"**{e['statut']}**"
    js = (e.get("usage") or {}).get("sortie")
    cout = f"{e.get('cout_usd'):.2f}".replace(".", ",")
    print(f"| {c} | {e.get('modele_servi')} | {st} ({e.get('fin')}) | {js:,} | {cout} USD |".replace(",", " ", 1) if js and js >= 1000 else f"| {c} | {e.get('modele_servi')} | {st} ({e.get('fin')}) | {js} | {cout} USD |")
print(f"\nDépense du run (toutes entrées du journal) : {f"{total:.2f}".replace(".", ",")} USD ; cellules valides {sum(e['statut'] == 'OK' for e in der.values())} sur {len(der)} ; "
      f"de {lignes[0]['debut']} à {lignes[-1]['fin_utc']}.")
