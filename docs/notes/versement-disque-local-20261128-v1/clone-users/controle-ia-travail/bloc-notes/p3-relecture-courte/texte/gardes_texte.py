import json, re, sys
from pathlib import Path
from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.harnais.validation_reelle import exiger_code_cite, ENTROPIE_CITEE
from controle_ia.manifeste import graines
from controle_ia.premier_test_ia import run as rp
from controle_ia.premier_test_ia.conditions import charger_consignes
from controle_ia.scellement import verifier
from controle_ia.prereg import problemes
p = Path("prereg/P3-premier-test-i-a-v1.md")
c = json.loads(Path("prereg/P3-premier-test-config-v1.json").read_text(encoding="utf-8"))
rp.exiger_config_p3(c)
print("mode", c["mode"], "duree_max_s", c["duree_max_s"], "budget", c["budget_entrainement_s"], "n_faits_max", c["n_faits_max"])
print("problemes():", problemes(str(p)))
t = charger_taches("donnees/t05-pilote-v1/taches-pilote-60-v1.json")
sha_t = verifier("donnees/t05-pilote-v1/taches-pilote-60-v1.json")
consignes = charger_consignes(c["chemin_consignes"], c["consignes_sha256"])
print("consignes", consignes["sha256"][:12])
print("code cité:", exiger_code_cite(Path("."), p))
ent = rp.exiger_citations_p3(p, c, sha_t)
print("entropie citée:", ent)
plan = rp.plan_p3(t); print("épisodes au plan:", len(plan))
g = graines(rp.cles_des_graines(t, c), ent); print("graines:", len(g))
texte = p.read_text(encoding="utf-8")
for x in ["Configuration de P3 (empreinte canonique)", "Tâches de P3", "Commit du code d'analyse", "Entropie", "Tests attendus",
          "Chemin de la configuration de P3", "Chemin des tâches de P3", "Chemin des consignes de P3", "GO de calcul et décision de Lazar"]:
    print(texte.count(f"{x} : `"), x)
