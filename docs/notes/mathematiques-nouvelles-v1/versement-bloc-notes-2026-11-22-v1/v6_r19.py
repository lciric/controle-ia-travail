import importlib
for v in ("oracles_plantes_v6",):
    P = importlib.import_module(f"controle_ia.{v}.parametres"); B = importlib.import_module(f"controle_ia.{v}.banque")
    T = importlib.import_module(f"controle_ia.{v}.tests_de_mort")
    p,_ = P.charger(); m = B.construire_mondes(11, p)[8]
    for t in ["pour tout n dans NAT, pour tout k dans [0 .. w(n)], u(k) > 0", "pour tout k dans [0 .. w(3)], pour tout n dans NAT, u(n + k) > 0",
              "pour tout n dans NAT, pour tout k dans [0 .. mod(n, 3)], u(k) > 0"]:
        try:
            r = T.appliquer_batterie(T.sortie_de_texte(t), m); print(v, r.statut, r.vraie_bornee, "|", t)
        except Exception as e: print(v, "EXC", type(e).__name__, e, "|", t)
