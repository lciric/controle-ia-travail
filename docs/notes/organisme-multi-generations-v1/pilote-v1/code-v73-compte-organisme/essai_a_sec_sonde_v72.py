"""Essai à sec de la commande de la sonde v72 (jalon 2 : registre portant la ligne v71 ; noms passés sous env -i, valeurs factices) : aucune clé, aucun relais, aucun appel, aucun dossier de sortie créé.
1. La ligne de commande est analysée par l'analyseur du lanceur v72, la sous-commande `sonde` remplacée par un enregistreur.
2. Les deux lignes de GO proposées (texte mot pour mot du candidat 1), écrites sous deux identifiants d'essai dans une COPIE de
   registres/go.md de main, sont lues par le lecteur gelé (`lire_go_de_la_sonde`) au montant exact.
3. Un registre des lancements vide (hors dépôt) admet un premier lancement ; le même registre, une fois une ligne d'essai
   consignée sous ces identifiants, refuse un second lancement.
Usage : python3 -I essai_a_sec_sonde_v72.py ARBRE_ORCHESTRATOR GO_MD_DE_MAIN DOSSIER_PROVISOIRE"""
import datetime, importlib.util, json, os, shutil, sys
arbre, go_main, d = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, arbre)
s = importlib.util.spec_from_file_location("lanceur_v72_a_sec", os.path.join(arbre, "demonstrations", "pilote_mr2_v72.py"))
L = importlib.util.module_from_spec(s); s.loader.exec_module(L)
reg = os.path.join(d, "go-copie.md")
shutil.copyfile(go_main, reg)
jour = datetime.date.today().isoformat()
p1 = ("Pilote MR-2 : sonde v72 des deux relais sur crédits de Claude, avant le scellement du texte : par relais, un appel à la borne "
      "gelée et un à 256 jetons, consignes de la configuration v12 (écrites pour faire réfléchir ; 100 octets au plus), par la "
      "sous-commande « sonde » du lanceur v72 ; seulement après le code v72 contre-lu ; une seule exécution (registre des lancements "
      "de la sonde) ; aucun monde, aucun résultat ; relevé et dossier entier versés, relevé cité au bloc gelé du texte ; prix "
      "rapprochés de la console par Lazar ; jamais de ligne d'extension ; arrêt par identifiant (R10)")
p2 = "Pilote MR-2 : sonde v72 des deux relais hors crédits, mêmes conditions que la ligne GO-2099-01-01-91"
with open(reg, "a", encoding="utf-8") as f:
    f.write(f"| GO-2099-01-01-91 | {jour} | calcul | {p1} | 4.39 USD | 2026-11-30 | Lazar | essai à sec |\n")
    f.write(f"| GO-2099-01-01-92 | {jour} | calcul | {p2} | 3.68 USD | 2026-11-30 | Lazar | essai à sec |\n")
conf, _ = L.PC.lire_configuration(L.CONFIGURATION)
go = L.PR.lire_go_de_la_sonde(conf, reg, "GO-2099-01-01-91", "GO-2099-01-01-92")
vu = {}
L.sonde = lambda args: vu.update(vars(args)) or 0
registre = os.path.join(d, "hors-depot", "lancements-sonde-pilote-mr2.jsonl")
os.makedirs(os.path.dirname(registre))
# jalon 2 : le registre réel porte déjà la ligne de la sonde v71 (versée) ; des identifiants neufs doivent passer
v71 = os.environ.get("REGISTRE_V71")
if v71:
    shutil.copyfile(v71, registre)
sortie = os.path.join(d, "hors-depot", "sonde-pilote-v72")
code = L.principal(["sonde", "--go-sonde-credits", "GO-2099-01-01-91", "--go-sonde-hors", "GO-2099-01-01-92", "--registre-go", reg,
                    "--registre-lancements", registre, "--sortie", sortie, "--borne-courte"])
premier = L.S.exiger_premier_lancement(registre, ["GO-2099-01-01-91", "GO-2099-01-01-92"])
L.S.consigner_lancement(registre, ["GO-2099-01-01-91", "GO-2099-01-01-92"], sortie, "essai", None)
try:
    L.S.exiger_premier_lancement(registre, ["GO-2099-01-01-91", "GO-2099-01-01-92"])
    second = "admis (DÉFAUT)"
except L.P.Refus as e:
    second = f"refusé : {e}"
noms = {n: (n in os.environ) for n in ("RR_ANTHROPIC_API_KEY_RIGAUD", "GEMINI_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_BASE_URL", "CLAUDE_CODE_REMOTE")}
print(json.dumps({"code": code, "registre_de_depart": "ligne v71 recopiée" if v71 else "vide", "noms_presents_sous_env_i": noms, "options_lues": {k: v for k, v in vu.items() if k != "commande"}, "sortie_creee": os.path.exists(sortie),
                  "lignes_lues": {k: {x: v[x] for x in ("plafond_lu_usd",) if x in v} for k, v in go.items()},
                  "premier_lancement": "admis" if premier is None else premier, "second_lancement": second,
                  "consignes_v12_octets": {k: len(v.encode()) for k, v in conf["sonde"]["consignes"].items()},
                  "configuration": os.path.basename(L.CONFIGURATION), "lanceur": L.VERSION, "module_sonde": L.S.VERSION},
                 ensure_ascii=False, indent=1))
