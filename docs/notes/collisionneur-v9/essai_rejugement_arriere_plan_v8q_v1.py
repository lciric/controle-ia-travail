import importlib.util, sys, json
sys.path.insert(0, "src")
spec = importlib.util.spec_from_file_location("c", "docs/notes/collisionneur-v9/collisionneur_v9_v8q.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
D = sys.argv[1]
c.fixer_composition(["fable","opus","argon","kimi","astra","carbon","neon","opus46","fable51"], sortie_max=True, effort_max=True)
print("lettre F =", c.MODELES["F"]["espece"])
e = [x for x in c.essais_journal(D, "E3-T2-critique-croisee-F") if x["essai"] == 5][0]
print("écarts (arrière-plan) :", c.ecarts_rejugement_arriere_plan(e, c.MODELES["F"]))
print("écarts (pensées, doit refuser) :", c.ecarts_rejugement(e, c.MODELES["F"])[:2])
print("écrit :", c.rejuger_essai(D, "E3-T2-critique-croisee-F", 5, genre="arriere_plan"))
print("de nouveau :", c.rejuger_essai(D, "E3-T2-critique-croisee-F", 5, genre="arriere_plan"))
