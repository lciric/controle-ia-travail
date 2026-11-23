import sys
sys.path.insert(0, "/home/user/raisons-ou-regard-travail/experiences")
from tests.test_exp1_lots_par_tranches import *
from tests import test_exp1_lots_par_tranches as M

class Sonde(M.Tranches):
    def test_a(self):
        self.plan(100, 100000.0)
        out = self.conduire()
        print("ASSEMBLE", out["fin"])
        print("role_du_lot", T.role_du_lot(ROLE))
        r = self.silence(L.lots_du_compte, ROLE, self.s.client, TL.ENV)
        print("lots_du_compte ok", len(r["lots"]))
        try:
            self.silence(L.relever, self.d, ROLE, self.s.client, TL.ENV)
        except BaseException as e:
            print("L.relever sur role assemble:", type(e).__name__, str(e)[:100])
        try:
            self.silence(L.envoyer, self.d, ROLE, 100000.0, True, self.s.client, TL.ENV)
        except BaseException as e:
            print("L.envoyer sur role assemble:", type(e).__name__, str(e)[:100])
    def test_b(self):
        """crash entre registre et replace des releves d'une tranche"""
        self.plan(39, 100000.0)
        self.silence(P.envoyer, self.d, ROLE, 100000.0, True, self.s.client, TL.ENV)
        rt = P.role_de_tranche(ROLE, 1)
        import os
        real = os.replace
        def boom(a, b):
            if str(b).endswith(".jsonl"): raise OSError("crash")
            return real(a, b)
        L.os.replace = boom
        try:
            self.silence(P.relever, self.d, ROLE, self.s.client, TL.ENV)
        except OSError: pass
        L.os.replace = real
        st = P.etat(self.d, ROLE)
        print("etat apres crash:", st["ouverte"], st["suivante"], st["arret"])
        try:
            self.silence(P.relever, self.d, ROLE, self.s.client, TL.ENV)
        except BaseException as e:
            print("relever:", type(e).__name__, str(e)[:100])
        try:
            self.silence(P.envoyer, self.d, ROLE, 100000.0, True, self.s.client, TL.ENV)
            print("tranche 2 part malgre fichiers de t01 absents")
        except BaseException as e:
            print("envoyer:", type(e).__name__, str(e)[:100])
if __name__ == "__main__":
    import unittest
    s = unittest.TestSuite([Sonde("test_b")])
    unittest.TextTestRunner(verbosity=0).run(s)
