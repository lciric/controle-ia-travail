"""VV-G7-01 et VV-G7-02 : ce que fait le module muté (copie à côté des tests) sur un nom vide et sur une source sans [SF]."""
import sys
sys.dont_write_bytecode = True
import garde_r1_v2b  # noqa: F401
sys.path.insert(0, "/home/user/controle-ia-travail/tests"); sys.path.insert(0, sys.argv[1])
import test_audit_verdict_p3_v1 as T
for nom, f in (("enjeux vide", lambda x: x["sondes-figees"]["principales"].__setitem__("enjeux", "")),
               ("tromperie vide", lambda x: x["sondes-figees"]["principales"].__setitem__("tromperie", ""))):
    x, y = T._cas("sain"); f(x)
    try:
        T._addendum(x, y); print(nom, "→ PASSAGE SANS ARRÊT")
    except Exception as e:
        print(nom, "→", type(e).__name__, ":", str(e)[:160])
