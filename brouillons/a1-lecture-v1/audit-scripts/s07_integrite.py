"""Intégrité : manifeste et bloc « preenregistrement » de la sortie contre le texte scellé (plan-gele, section 11),
entropie racine, configuration, GO, substitutions, modèles. Lecture seule."""
import json, re, hashlib, os
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
O = "/home/claude/ideation-organism/orchestrator/"
P = O + "prereg/preenregistrement-attaque-goodhart-v2-v1.md"
texte = open(P, encoding="utf-8").read()
sha_p = hashlib.sha256(open(P, "rb").read()).hexdigest()
M = json.load(open(B + "entree/sortie/manifeste.json", encoding="utf-8"))
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
reg = M["reglages"]
print("sha256 du texte sur disque :", sha_p)
print("manifeste.reglages.preenregistrement.sha256 :", reg["preenregistrement"]["sha256"], "| sortie.preenregistrement.sha256 :", R["preenregistrement"]["sha256"])
print("entropie_racine == int(sha, 16) :", reg["entropie_racine"] == str(int(sha_p, 16)), "| >= 2**64 :", int(reg["entropie_racine"]) >= 2 ** 64)
print("chemin :", reg["preenregistrement"]["chemin"], "| mode :", reg["mode"], "| attaque :", reg["attaque"])
# bloc plan-gele
i, j = texte.find("<!-- plan-gele : début -->"), texte.find("<!-- plan-gele : fin -->")
plan_txt = dict(re.findall(r"^\s*([a-z0-9_]+)\s*:\s*(.+?)\s*$", texte[i:j], re.M))
print("plan-gele (texte) :", plan_txt)
print("plan (manifeste.reglages.plan) :", json.dumps(reg["plan"], ensure_ascii=False))
print("plan (sortie.preenregistrement.plan) == manifeste :", R["preenregistrement"]["plan"] == reg["plan"], "| manifeste.reglages.preenregistrement.plan == reglages.plan :", reg["preenregistrement"]["plan"] == reg["plan"])
p = reg["plan"]
verifs = {"cartes 12": p["cartes"] == 12, "mondes W1,W2": p["mondes"] == ["W1", "W2"], "n_max 16": p["n_max"] == int(plan_txt["tentatives"]),
          "rejeux": p["rejeux"] == {"v8": int(plan_txt["rejeux_v8"]), "v7": int(plan_txt["rejeux_v7"])}, "rejeux_audit": p["rejeux_audit"] == int(plan_txt["rejeux_audit"]),
          "plafond": p["plafond_usd"] == float(plan_txt["plafond_usd"]), "duree": p["duree_max_s"] == float(plan_txt["duree_max_h"]) * 3600,
          "processus": p["processus"] == int(plan_txt["processus_rejeux"]), "parallele": p["parallele"] is True and plan_txt["fournisseurs_en_parallele"] == "oui",
          "decision_ecart": p["decision_ecart"] == plan_txt["decision_ecart"], "configuration_sha256": p["configuration_sha256"] == plan_txt["configuration_sha256"],
          "go": p["go"] == plan_txt["go"], "grille": plan_txt["grille"] == "12 cartes par monde, 24 unités par case"}
print("plan conforme au bloc :", verifs)
# 71 empreintes
k, l = texte.find("<!-- empreintes-du-code : début -->"), texte.find("<!-- empreintes-du-code : fin -->")
gelees = {r: h for h, r in re.findall(r"^([0-9a-f]{64})  (\S+)$", texte[k:l], re.M)}
print("bloc section 11 :", len(gelees), "empreintes")
for nom, d in (("manifeste.reglages.code_sha256", reg["code_sha256"]), ("manifeste.reglages.preenregistrement.empreintes_du_code_verifiees", reg["preenregistrement"]["empreintes_du_code_verifiees"]),
               ("sortie.preenregistrement.empreintes_du_code_verifiees", R["preenregistrement"]["empreintes_du_code_verifiees"])):
    print(nom, len(d), "égal au bloc :", d == gelees)
# arbre de travail (lecture seule) : les 71 fichiers
ecarts = [r for r, h in gelees.items() if hashlib.sha256(open(O + r, "rb").read()).hexdigest() != h]
print("arbre de travail : écarts aux 71 empreintes :", ecarts)
print("manifeste.code_sha256 (racine, 103 noms de base) : clés", len(M["code_sha256"]))
base = {os.path.basename(r): h for r, h in gelees.items()}
coll = [n for n in base if list(os.path.basename(r) for r in gelees).count(n) > 1]
print("   noms de base en double parmi les 71 :", sorted(set(coll)))
diff = {n: (M["code_sha256"].get(n), base[n]) for n in base if n not in coll and M["code_sha256"].get(n) != base[n]}
print("   écarts entre manifeste.code_sha256 et le bloc, par nom de base :", diff)
# configuration, GO, substitutions, modèles
cf = reg["configuration"]
print("configuration :", cf["sha256"], "| chemin :", cf["chemin"], "| empreinte_configuration :", cf.get("empreinte_configuration"))
print("budget_appel_usd :", cf["budget_appel_usd"], "| modeles_demandes :", cf["modeles_demandes"], "| role :", cf["role_pole"], "| part :", cf["part_par_relais_usd"])
print("substitutions :", json.dumps(cf["substitutions_dans_les_commandes"], ensure_ascii=False))
print("accuses_plafond :", json.dumps(cf["accuses_plafond"], ensure_ascii=False))
for f in ("kimi", "argon"):
    a = cf["adaptateurs"][f]
    print(f, "commande :", a["commande"], "| empreintes :", a["empreintes"], "| délai :", a["delai_s"])
print("portes :", json.dumps(cf["portes"], ensure_ascii=False))
print("sortie.preenregistrement.go :", json.dumps(R["preenregistrement"]["go"], ensure_ascii=False))
print("manifeste.reglages.preenregistrement.go == sortie :", reg["preenregistrement"]["go"] == R["preenregistrement"]["go"])
print("modeles_servis (sortie) :", R["modeles_servis"])
print("depot :", reg["depot"], "| numpy :", reg["numpy"], "| python :", reg["python"], "| version_pole :", M["version_pole"], "| plateforme :", M["plateforme"])
print("coeur :", json.dumps({k: v for k, v in reg["coeur"].items() if k in ("module", "sha256", "version", "n_max", "rejeux", "rejeux_audit", "bootstrap")}, ensure_ascii=False))
print("regle_des_graines :", M["regle_des_graines"])
print("devis (sortie) :", json.dumps(R["preenregistrement"]["devis"], ensure_ascii=False))
print("proposeur_a_blanc :", reg["proposeur_a_blanc"])
print("clés manifeste.reglages.configuration :", sorted(cf))
