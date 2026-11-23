import time
from controle_ia.manifeste import graines
from controle_ia.organismes_discrets import lanceur_bras_a_v2 as la
m, fmt = la.charger_modele_et_format({}, "jouet", 7)
FAB=[{"identifiant": "fab-0", "questions": "Q ?"}]
C={"T":10,"lot":8,"episodes_par_tache":8,"couches":[1],"max_nouveaux":400,"temperature":1.0,"tolerance_equivalence":0.2}
g=graines([f"fabrication/tache/fab-0/e{k}" for k in range(8)], 123)
t=time.time(); r=la.jouer_honnetes(m, fmt, FAB, C, g, None, "fabrication"); print(time.time()-t, len(r), [len(a) for a in r[0]["actions"]], r[0]["actions"][0][-1] in fmt.fins)
