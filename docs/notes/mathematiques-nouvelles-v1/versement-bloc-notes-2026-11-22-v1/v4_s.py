import os, tempfile, json
from controle_ia.oracles_plantes_v4.parametres import charger
from controle_ia.oracles_plantes_v4.banque import construire_banque
from controle_ia.oracles_plantes_v4.tests_de_mort import appliquer_batterie, sortie_de_texte, appliquer_t6
from controle_ia.oracles_plantes_v4.lignee import Registre
p,_ = charger(); banque = construire_banque(11, p)
m, plantes = banque[8]
T = next(x for x in plantes if x.etiquette == "VERITE_PLANTEE")
R = Registre(os.path.join(tempfile.mkdtemp(), "r.jsonl"))
r = appliquer_batterie(sortie_de_texte(T.texte), m, registre=R)
cas = ['{"verdict":"faux","contre_exemples":[{"n":1e99999}],"raison":"x"}', '['*100000, b'\xff\xfe', '{"verdict":"faux","contre_exemples":[{"n":' + '9'*5000 + '}],"raison":"x"}',
       '{"verdict":"faux","contre_exemples":[{"n":-0}],"raison":"x"}', '{"verdict":"faux","contre_exemples":[{"n":3, "n":4}],"raison":"x"}',
       json.dumps({"verdict":"faux","contre_exemples":[{"n": k} for k in range(46)],"raison":"x"}), '{"verdict":"faux","contre_exemples":"n=3","raison":"x"}', 'NaN', '{"verdict":"faux","contre_exemples":[{"n":NaN}],"raison":"x"}']
for c in cas:
    try: print(appliquer_t6(c, r.arbre, m, R).type.value)
    except Exception as e: print("EXC", type(e).__name__, str(e)[:80])
r2 = appliquer_batterie(sortie_de_texte(T.texte), m, registre=R); print("vérité après :", r2.statut)
for s in ['{"enonce": "1 = 1", "ce_qui_le_tuerait": "x", "confiance": 1e-99999}', '{"enonce": "1 = 1", "ce_qui_le_tuerait": "x", "confiance": ' + '1'*5000 + '}', '[' * 50000]:
    try: print(appliquer_batterie(s, m, registre=R).statut)
    except Exception as e: print("EXC", type(e).__name__, str(e)[:80])
