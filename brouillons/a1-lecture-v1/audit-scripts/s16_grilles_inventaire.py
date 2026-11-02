"""Grilles d'inventaire par (monde, fournisseur) : une ligne par carte, une colonne par suite ; cellule = tentatives jouées,
issue de la suite (P@k : première promotion à la tentative k ; NP : 16 tentatives sans promotion), et décompte des
statuts (j = jugée non promue, i = invalide, é = échouée, b = budget, x = évaluation impossible) ; heures de début et de fin
de l'unité au registre (appariement s04). Écrit travail/grilles-inventaire-v1.md (texte repris dans le rapport)."""
import json, collections
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
inv = json.load(open(B + "travail/inventaire-v1.json", encoding="utf-8"))
idx = {(u["monde"], u["fournisseur"], u["carte"], u["suite"]): u for u in inv}
SUITES = ("temoin|v8", "retour|v8", "temoin|v7", "retour|v7")
abr = {"non_promue": "j", "invalide": "i", "echouee": "é", "budget": "b", "evaluation_impossible": "x"}
lignes = []
for w in ("W1", "W2"):
    for f in ("argon", "kimi"):
        lignes.append(f"\n**{w}, {f}** (cellule : tentatives jouées · issue · décompte ; heures UTC au registre)\n")
        lignes.append("| carte | témoin\\|v8 | retour\\|v8 | témoin\\|v7 | retour\\|v7 | début → fin (registre) |")
        lignes.append("|---|---|---|---|---|---|")
        for c in range(12):
            cel, debuts, fins = [], [], []
            for s in SUITES:
                u = idx[(w, f, c, s)]
                cnt = collections.Counter(abr[x] for x in u["statuts"] if x != "promue")
                issue = f"P@{u['premiere_promotion']}" if u["premiere_promotion"] else "NP"
                dec = " ".join(f"{v}{k}" for k, v in sorted(cnt.items()))
                cel.append(f"{u['tentatives']} · {issue}" + (f" · {dec}" if dec else ""))
                if u["debut_registre"]:
                    debuts.append(u["debut_registre"]); fins.append(u["fin_registre"])
            hors = sum(idx[(w, f, c, s)]["appels_hors_registre"] for s in SUITES)
            h = (f"{min(debuts)[11:19]} → {max(fins)[11:19]}" if debuts else "aucun appel au registre") + (f" ; {hors} appels hors registre" if hors else "")
            lignes.append(f"| {c} | " + " | ".join(cel) + f" | {h} |")
open(B + "travail/grilles-inventaire-v1.md", "w", encoding="utf-8").write("\n".join(lignes) + "\n")
print("\n".join(lignes))
