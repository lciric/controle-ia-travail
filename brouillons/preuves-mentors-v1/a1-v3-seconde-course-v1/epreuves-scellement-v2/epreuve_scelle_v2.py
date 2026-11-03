"""Épreuve du texte scellé v2 d'A1-v3 par le lanceur de l'arbre qui sera poussé (HEAD eaa74ca + fichiers neufs),
compagnon réel sur disque, registre de GO de canal/conv-audit-n04 (46062b4e) et de origin/main. Aucun réseau, aucun modèle."""
import hashlib, importlib.util, json, os, re, sys
racine, reg_canal, reg_main, sortie = sys.argv[1:5]
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
spec = importlib.util.spec_from_file_location("lanceur", os.path.join(racine, "demonstrations", "attaque_goodhart_v3.py"))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
from pole import configuration_v56 as cfg
r = {"RACINE": L.RACINE, "DOSSIER_PREREG": L.DOSSIER_PREREG, "pole": os.path.dirname(sys.modules["pole"].__file__)}
p = os.path.join(racine, "prereg", "preenregistrement-attaque-goodhart-v3-v2.md")
r["texte"] = {"sha256": sha(p), "compagnon": open(p + ".sha256").read()}
def essai(f):
    try: return ("accepté", f())
    except Exception as e: return ("refusé", f"{type(e).__name__}: {e}")
res, val = essai(lambda: L.lire_preenregistrement(p))
if res == "accepté":
    entropie, empreinte, gel, plan = val
    r["lire_preenregistrement"] = {"resultat": res, "empreinte": empreinte, "entropie_egale": entropie == int(empreinte, 16),
        "empreinte_egale_au_fichier": empreinte == sha(p), "fichiers_geles_verifies": len(gel), "go": plan["go"],
        "plafond_usd": plan["plafond_usd"], "mode": plan["mode"], "cartes": plan["cartes"], "mondes": plan["mondes"],
        "relais_perdu_s": plan.get("relais_perdu_s"), "duree_max_s": plan.get("duree_max_s")}
    t = open(p, encoding="utf-8").read()
    plan_direct = L.lire_plan(t, mode_attendu="course")
    r["marqueurs_restants"] = [m.group(0) for m in L.MARQUEUR.finditer(t)]
    r["doubles_chevrons"] = t.count("<<")
    for nom, reg in (("canal_46062b4e", reg_canal), ("origin_main", reg_main)):
        x = essai(lambda: L.verifier_go(reg, plan["go"], plan, cfg))
        r[f"verifier_go_{nom}"] = (x[0], {k: x[1].get(k) for k in ("identifiant", "type", "accorde", "echeance", "par", "plafond_lu_usd", "montant_requis_usd")} if x[0] == "accepté" else x[1][:400])
        lignes = open(reg, encoding="utf-8").read().splitlines()
        ids = [m.group(1) for m in (re.match(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|", l) for l in lignes) if m]
        r[f"registre_{nom}"] = {"sha256": sha(reg), "lignes_GO": len(ids), "doublons": sorted({i for i in ids if ids.count(i) > 1}),
            "grep_GO_neuf": [n for n, l in enumerate(lignes, 1) if plan["go"] in l],
            "revocations_du_GO_neuf": [n for n, l in enumerate(lignes, 1) if plan["go"] in l and "révocation" in l]}
else:
    r["lire_preenregistrement"] = {"resultat": res, "message": val}
# Témoin : un compagnon faux doit être refusé (garde sur un artefact, R5).
vrai = open(p + ".sha256").read()
try:
    open(p + ".sha256", "w").write("0" * 64 + "  preenregistrement-attaque-goodhart-v3-v2.md\n")
    r["temoin_compagnon_faux"] = essai(lambda: L.lire_preenregistrement(p))[0]
finally:
    open(p + ".sha256", "w").write(vrai)
r["compagnon_restaure"] = open(p + ".sha256").read() == vrai
json.dump(r, open(sortie, "w"), ensure_ascii=False, indent=1, default=str)
print(json.dumps(r, ensure_ascii=False, indent=1, default=str))
