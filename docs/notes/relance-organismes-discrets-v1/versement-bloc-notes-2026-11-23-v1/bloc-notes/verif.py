import json, hashlib
from pathlib import Path
from controle_ia.organismes_discrets import lanceur_bras_a_v7 as la
c = la.lire_la_configuration("prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v1.json", ".")
print("config sha", c["sha256"], "texte", c["texte_sha256"], "lanceur", c["lanceur_sha256"], c["entropie"], c["entropie_fictive"])
plan = la.plan_des_taches(c)
g = la.graines_de_la_course(c, plan)
s = json.loads(Path("docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v1.json").read_text())
print(list(s.keys()))
print(s["configuration_du_lanceur"])
refait = {"fabrication":[t["identifiant"] for t in plan["fabrication"]],"verification":[t["identifiant"] for t in plan["verification"]],"ouvertes":list(plan["ouvertes"]),"gardees":list(plan["gardees"])}
for k,v in refait.items(): print(k, s.get(k)==v, len(v))
print("graines", len(g))
for k in s:
    if k not in refait: print(k, json.dumps(s[k])[:300])
cles = la.cles_des_graines(plan["fabrication"], plan["verification"])
print("cles ==", cles == s["cles_des_graines"], len(cles))
h = hashlib.sha256(json.dumps(g, sort_keys=True, ensure_ascii=False, separators=(",",":")).encode()).hexdigest()
print("hash graines (essai forme)", h, s["empreinte_des_graines_json_canonique"])
