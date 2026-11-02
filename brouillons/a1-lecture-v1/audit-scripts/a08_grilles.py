"""Audit A1 (auditeur neuf, 2e) — grilles d'inventaire par monde × fournisseur × suite × carte (signature des tentatives :
n non promue, P promue, I invalide, E échouée, X évaluation impossible, B refusée pour budget ; « · » non jouée après
promotion) et heures (registre) ; caviardage ; cohérences de dépense. Lecture seule ; écrit travail/a08-grilles-v1.md."""
import json
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
inv = json.load(open(B + "travail/a02-inventaire-v1.json", encoding="utf-8"))["unites"]
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
C = {"non_promue": "n", "promue": "P", "invalide": "I", "echouee": "E", "evaluation_impossible": "X", "refusee_budget": "B"}
md = []
for w in ("W1", "W2"):
    for fo in ("argon", "kimi"):
        md.append(f"\n#### {w} × {fo} — signature des 16 tentatives par suite et carte (source : `suites[].tentatives[]`, statut selon `jouer_suite` ; heures : registre apparié, a02)\n")
        md.append("| carte | temoin\\|v8 | retour\\|v8 | temoin\\|v7 | retour\\|v7 | début (registre) | fin (registre) |")
        md.append("|---|---|---|---|---|---|---|")
        for c in range(12):
            us = {u["suite"]: u for u in inv if u["monde"] == w and u["fournisseur"] == fo and u["carte"] == c}
            sig = ["".join(C[x] for x in us[s]["statuts"]) + "·" * us[s]["non_jouees_apres_promotion"] for s in ("temoin|v8", "retour|v8", "temoin|v7", "retour|v7")]
            deb = min((us[s]["debut_registre"] for s in us if us[s]["debut_registre"]), default="—")
            fin = max((us[s]["fin_registre"] for s in us if us[s]["fin_registre"]), default="—")
            md.append(f"| {c} | `{sig[0]}` | `{sig[1]}` | `{sig[2]}` | `{sig[3]}` | {deb[11:19] if deb != '—' else '—'} | {fin[11:19] if fin != '—' else '—'} |")
# caviardage et dépense
n_cav = sum(1 for s in R["suites"] for t in s["tentatives"] if isinstance(t["reponse_caviardee"], str) and "[CAVIARDÉ]" in t["reponse_caviardee"])
n_rep = sum(1 for s in R["suites"] for t in s["tentatives"] if isinstance(t["reponse_caviardee"], str))
md.append(f"\nRéponses caviardées gardées : {n_rep} (une par appel réussi) ; réponses portant « [CAVIARDÉ] » : {n_cav}.")
md.append(f"Dépense : sortie `depense_usd` = {R['depense_usd']} ; somme des `cout_usd` des appels = {round(sum(a['cout_usd'] for s in R['suites'] for t in s['tentatives'] for a in t['appels']), 4)} ; par fournisseur {R['depense_par_fournisseur_usd']} ; plafond 80, part 40 par fournisseur ; `appels` = {R['appels']}, `reprises` = {R['reprises']} ; `duree_s` = {R['duree_s']} (< 72 000 s).")
open(B + "travail/a08-grilles-v1.md", "w", encoding="utf-8").write("\n".join(md) + "\n")
print("\n".join(md))
