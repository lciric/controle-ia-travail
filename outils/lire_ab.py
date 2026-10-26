import json, sys, collections
d = json.load(sys.stdin)
print("horodatage:", d.get("experiment_timestamp"), "| n par bras:", d.get("n_agents_per_arm"))
for bras in ("arm_A_coercive_geometrie", "arm_B_pascalian_finesse"):
    b = d[bras]; tr = b["detailed_traces"]
    L = [t["text_length"] for t in tr]
    print()
    print(bras, ": mutinerie", b["mutiny_rate_pct"], "% | coop", b["full_cooperation_rate_pct"], "% | eq moy", b["mean_latex_equations_generated"])
    print("  longueurs de texte :", sorted(L))
    print("  réponses vides (0 caractère) :", sum(1 for x in L if x == 0), "/", len(L))
    par = collections.defaultdict(list)
    for t in tr:
        par[t["lineage"]].append(t["text_length"])
    for k, v in par.items():
        print("  ", k, ": vides", sum(1 for x in v if x == 0), "/", len(v), ", longueurs", sorted(v))
    for t in [t for t in tr if t["text_length"] > 0][:2]:
        print("  extrait non vide :", t["lineage"], t["text_length"], "|", t["sample_excerpt"][:150].replace("\n", " "))
