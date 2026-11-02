"""Audit A1 (auditeur neuf, 2e) — section 1, intégrité. Lecture seule ; écrit travail/a01-integrite-v1.json.
Vérifie : empreintes des trois fichiers de sortie et de leurs compagnons ; manifeste (préenregistrement, entropie racine,
configuration, GO, plan-gele, 71 empreintes, substitutions, modèles) ; ligne du GO (copie manuelle de `git show 2eb66705`)."""
import json, re, hashlib, os, sys
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
O = "/home/claude/ideation-organism/orchestrator/"
P = O + "prereg/preenregistrement-attaque-goodhart-v2-v1.md"
ATTENDU = {"attaque-goodhart-v2.json": "5dd5066c659c7a3b34c1b12d15a9bb80fb996d67a14f226d76c028c428a1d8c6",
           "manifeste.json": "7552e5a416c1a5dac4c8576e43cf06d118ff0d16785b812f8823d3d0af90d423",
           "registre-depense-cumulee-v1.jsonl": "ae47217ed7bc66c44c2fa25a2d675af7486e0d71c8e3a8a43cb20279c0129611"}
SHA_P = "fc81d015d27e60388099c7845a66b75d613187f99d5d0060950540a686925b65"
SHA_CONF = "e5306c47e1b21a5e55b599411dba92c97e88aa98bb6d6fa91fc5d358a2bdde30"
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
out = {}
out["sortie"] = {n: {"obtenu": sha(B + "entree/sortie/" + n), "attendu": h, "compagnon": open(B + "entree/sortie/" + n + ".sha256").read().split()[0]} for n, h in ATTENDU.items()}
for n, d in out["sortie"].items():
    d["conforme"] = d["obtenu"] == d["attendu"] == d["compagnon"]
out["preenregistrement_sur_disque"] = {"sha256": sha(P), "conforme": sha(P) == SHA_P}
texte = open(P, encoding="utf-8").read()
M = json.load(open(B + "entree/sortie/manifeste.json", encoding="utf-8"))
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
reg = M["reglages"]
out["manifeste"] = {
    "mode": reg["mode"], "attaque": reg["attaque"],
    "preenregistrement.sha256": reg["preenregistrement"]["sha256"], "preenregistrement.chemin": reg["preenregistrement"]["chemin"],
    "sha_conforme": reg["preenregistrement"]["sha256"] == SHA_P and R["preenregistrement"]["sha256"] == SHA_P,
    "entropie_racine": reg["entropie_racine"], "entropie_conforme": reg["entropie_racine"] == str(int(SHA_P, 16)),
    "entropie_>=_2^64": int(reg["entropie_racine"]) >= 2 ** 64,
    "configuration.sha256": reg["configuration"]["sha256"], "configuration_conforme": reg["configuration"]["sha256"] == SHA_CONF,
    "configuration.chemin": reg["configuration"]["chemin"],
    "configuration.empreinte_configuration (objet, hors clés _ ; configuration_v56 l.111)": reg["configuration"]["empreinte_configuration"],
    "budget_appel_usd": reg["configuration"]["budget_appel_usd"], "part_par_relais_usd": reg["configuration"]["part_par_relais_usd"],
    "modeles_demandes": reg["configuration"]["modeles_demandes"], "modeles_servis (sortie)": R["modeles_servis"],
    "substitutions": reg["configuration"]["substitutions_dans_les_commandes"],
    "accuses_plafond": reg["configuration"]["accuses_plafond"],
    "empreintes_commandes": {f: reg["configuration"]["adaptateurs"][f]["empreintes"] for f in ("kimi", "argon")},
    "delai_s_adaptateur": {f: reg["configuration"]["adaptateurs"][f]["delai_s"] for f in ("kimi", "argon")},
    "delai_s_commande (--delai-s)": {f: reg["configuration"]["adaptateurs"][f]["commande"][reg["configuration"]["adaptateurs"][f]["commande"].index("--delai-s") + 1] for f in ("kimi", "argon")},
    "depot": reg["depot"], "numpy": reg["numpy"], "python": reg["python"], "coeur.sha256": reg["coeur"]["sha256"],
    "proposeur_a_blanc": reg["proposeur_a_blanc"],
}
# plan-gele
i, j = texte.find("<!-- plan-gele : début -->"), texte.find("<!-- plan-gele : fin -->")
pt = dict(re.findall(r"^\s*([a-z0-9_]+)\s*:\s*(.+?)\s*$", texte[i:j], re.M))
p = reg["plan"]
out["plan"] = {"bloc_texte": pt, "manifeste": p,
               "sortie.plan == manifeste.plan": R["preenregistrement"]["plan"] == p, "reglages.preenregistrement.plan == reglages.plan": reg["preenregistrement"]["plan"] == p,
               "conforme": {"cartes": p["cartes"] == 12 and pt["grille"] == "12 cartes par monde, 24 unités par case", "mondes": p["mondes"] == ["W1", "W2"] and pt["mondes"] == "W1 et W2",
                            "n_max": p["n_max"] == int(pt["tentatives"]), "rejeux": p["rejeux"] == {"v8": int(pt["rejeux_v8"]), "v7": int(pt["rejeux_v7"])},
                            "rejeux_audit": p["rejeux_audit"] == int(pt["rejeux_audit"]), "plafond": p["plafond_usd"] == float(pt["plafond_usd"]),
                            "duree": p["duree_max_s"] == float(pt["duree_max_h"]) * 3600, "processus": p["processus"] == int(pt["processus_rejeux"]),
                            "parallele": p["parallele"] is True and pt["fournisseurs_en_parallele"] == "oui", "decision_ecart": p["decision_ecart"] == pt["decision_ecart"],
                            "configuration_sha256": p["configuration_sha256"] == pt["configuration_sha256"] == SHA_CONF, "go": p["go"] == pt["go"] == "GO-2026-11-02-07"}}
# 71 empreintes
k, l = texte.find("<!-- empreintes-du-code : début -->"), texte.find("<!-- empreintes-du-code : fin -->")
gelees = {r: h for h, r in re.findall(r"^([0-9a-f]{64})  (\S+)$", texte[k:l], re.M)}
out["code_gele"] = {"bloc": len(gelees),
                    "manifeste.reglages.code_sha256 == bloc": reg["code_sha256"] == gelees,
                    "manifeste.reglages.preenregistrement.empreintes_du_code_verifiees == bloc": reg["preenregistrement"]["empreintes_du_code_verifiees"] == gelees,
                    "sortie.preenregistrement.empreintes_du_code_verifiees == bloc": R["preenregistrement"]["empreintes_du_code_verifiees"] == gelees,
                    "arbre_de_travail_ecarts": [r for r, h in gelees.items() if sha(O + r) != h],
                    "manifeste.code_sha256 (racine) : nombre de noms de base (listing de pole/ par outils.manifeste, hors périmètre)": len(M["code_sha256"])}
# GO
go = reg["preenregistrement"]["go"]
ligne = open(B + "travail/ligne-go-2eb66705-v1.txt", encoding="utf-8").read().strip()
cols = [c.strip() for c in ligne.strip("|").split("|")]
out["go"] = {"manifeste": go, "sortie.go == manifeste.go": R["preenregistrement"]["go"] == go,
             "ligne_2eb66705_nb_colonnes": len(cols),
             "colonnes": {"identifiant": cols[0] == go["identifiant"] == "GO-2026-11-02-07", "accorde": cols[1] == go["accorde"], "type": cols[2] == go["type"] == "calcul",
                          "perimetre": cols[3] == go["perimetre"], "plafond": cols[4] == go["plafond"] == "80 USD", "echeance": cols[5] == go["echeance"],
                          "par": cols[6] == go["par"] == "Lazar", "ref": cols[7] == go["ref"]},
             "ligne_53_au_manifeste": go["ligne"] == 53, "montant_requis": go["montant_requis_usd"] == go["plafond_lu_usd"] == 80.0,
             "autres_lignes_contenant_la_chaine (grep -n sur git show)": "aucune : une seule ligne (53) contient « GO-2026-11-02-07 »"}
json.dump(out, open(B + "travail/a01-integrite-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1)[:6000])
