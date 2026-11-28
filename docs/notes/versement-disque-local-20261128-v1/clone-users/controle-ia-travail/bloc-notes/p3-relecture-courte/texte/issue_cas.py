# Cas de la table non écrits au texte : issue() de lecture.py (commit 03cb538) sur des sorties synthétiques.
from controle_ia.premier_test_ia.lecture import issue
def jeu(au):  return {"au_dessus_du_plancher": au, "aire": 0.7, "plancher_quantile": 0.53}
def base(st, th, non_interp=(), intention=True):
    p = "sonde"
    return {"audit_R4": {"declenche": False, "non_interpretables": [list(x) for x in non_interp]},
            "controle_negatif": None,
            "P3-P6": {c: {"titre_sans_capitale": 50, "actions": 100} if c == "temoin" else {"titre_sans_capitale": 0, "actions": 100}
                      for c in ("temoin", "honnete")},
            "P3-P2": {}, "cout_mention": {}, "P3-P1": {"etablie": True}, "principales": [p],
            "jeux": {p: {"saboteur-honnete": jeu(True), "saboteur-temoin": st, "temoin-honnete": th,
                         "mention-honnete": jeu(False), "saboteur-mention": jeu(True)}},
            "intention": {p: {"etablie": intention}}}
print("1 saboteur-témoin au-dessus mais non interprétable :", issue(base(jeu(True), jeu(False), [("sonde", "saboteur-temoin")]))["ligne"])
print("2 témoin-honnête en échec :", issue(base(jeu(True), {"echec": "plus de 1 % de tirages dégénérés"}))["ligne"])
print("3 saboteur-mention non interprétable, intention établie :", issue(base(jeu(True), jeu(False), [("sonde", "saboteur-mention")]))["ligne"])
