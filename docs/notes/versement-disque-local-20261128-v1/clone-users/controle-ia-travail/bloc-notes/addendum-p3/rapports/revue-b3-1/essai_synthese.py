"""Essai : `synthese` sur des entrées fabriquées. (1) Une conclusion établie dont le seul contrôle est « non lu » :
que dit la recommandation au verdict R13 ? (2) Toutes les réserves possibles « non lues » (aucun contrôle contraire) :
que dit l'audit de symétrie ? (3) Réserve `reserve_A7_forme_du_cout` : la recommandation reprend-elle la lecture gelée
(« séparation non établie hors de cette forme du coût ») ?"""
import json

import complements_p3_v1 as cp

P = ["sonde-a", "sonde-b"]
etablies = ["P3-P1", "P3-P3/sonde-a"]
possibles = cp.cibles_possibles(P)


def entree(analyse, sonde, controles):
    e = cp._Entree(analyse, sonde, etablies, possibles)
    for test, cible, contraire, reserve in controles:
        e.controle(test, cible, contraire, reserve, f"motif de {test}")
    return e.sortie()


def analyses(cas):
    a = {}
    for x in cp.ANALYSES:
        if x in cp.SANS_SONDE:
            a[x] = entree(x, None, [])
        else:
            a[x] = {p: entree(x, p, []) for p in P}
    for x, p, ctrl in cas:
        if p is None:
            a[x] = entree(x, None, ctrl)
        else:
            a[x][p] = entree(x, p, ctrl)
    return a


print("(1) P3-P3/sonde-a : A8 « non lu » seulement ; P3-P1 : A6 favorable")
s = cp.synthese(analyses([("A8", "sonde-a", [("A8 début de l'action", "P3-P3/sonde-a", None, None)]),
                          ("A6", None, [("A6 P3-P1", "P3-P1", False, "reserve_A6_P3-P1")])]), etablies, False)
print(json.dumps(s["recommandation_au_verdict_R13"], ensure_ascii=False, indent=1))
print(json.dumps(s["audit_symetrie_addendum"], ensure_ascii=False, indent=1))

print("(2) tous les contrôles des cibles établies « non lus »")
s = cp.synthese(analyses([("A8", "sonde-a", [("A8 début de l'action", "P3-P3/sonde-a", None, None)]),
                          ("A6", None, [("A6 P3-P1", "P3-P1", None, None)])]), etablies, False)
print(json.dumps({k: s["audit_symetrie_addendum"][k] for k in ("reserves_possibles", "reserves_declenchees",
                                                                 "declencheur", "motif", "lecture")},
                 ensure_ascii=False, indent=1))

print("(3) réserve A7 forme du coût")
s = cp.synthese(analyses([("A7", "sonde-a", [("A7 (ii) saboteur-honnete cout_intervalle", "P3-P3/sonde-a", True,
                                              "reserve_A7_forme_du_cout")])]), etablies, False)
print(json.dumps(s["recommandation_au_verdict_R13"], ensure_ascii=False, indent=1))
