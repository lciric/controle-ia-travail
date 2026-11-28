"""Reproductions sur données synthétiques (aides du fichier de tests) : dossier du module (copie ou mutant), scénario."""
import sys
dossier, scenario = sys.argv[1], sys.argv[2]
sys.path.insert(0, dossier)
sys.dont_write_bytecode = True
import numpy as np
import test_audit_verdict_p3_v1 as T
av = T.av
print("module :", av.__file__)

if scenario == "garde7-nul":
    # artefact : un coût illisible (NaN) de l'honnête devient 0 ; l'effet ne change pas (NaN et 0 sont hors du calcul),
    # seul le compte des coûts nuls de l'honnête change
    s, lec = T._cas("sain")
    t = s["tables"]
    i = int(np.flatnonzero((t["condition"] == "honnete") & np.isnan(t["cout"]))[0])
    t["cout"][i] = 0.0
    try:
        o = av.analyser_addendum2(s, lec, T.G)
        print("PASSE : aucun arrêt ; coherence P3-P1 :", o["coherence_avec_la_lecture"]["effets"]["P3-P1"],
              "; [L] actions_nulles_b =", lec["P3-P1"]["actions_nulles_b"])
    except T.GardeArret as e:
        print("ARRÊT :", e)

elif scenario == "exception-dans-une-analyse":
    # défaut simulé du code (exception autre que GardeArret) dans le calcul de la médiane par tâche
    def defaut(*a, **k):
        raise ValueError("défaut simulé dans M6")
    av.mediane_par_tache = defaut
    s, lec = T._cas("sain")
    try:
        o = av.analyser_addendum2(s, lec, T.G)
        print("PASSE : sortie écrite ; médiane :", T._sab(o)["mediane_par_tache"],
              "; réserves :", T._reserves(o, "P3-P1"))
    except ValueError as e:
        print("ARRÊT (exception propagée) :", e)

elif scenario == "audit-esf-non-calculable":
    c = T._faux_contrastes()
    c["temoin-honnete"]["E_sf"] = {"etat": av.NON_CALCULABLE, "motif": "moins de deux tâches"}
    try:
        a = av.audit_symetrie(T._faux_L(), c, {}, T.P)
        print("explication_trop_propre :", a["explication_trop_propre"])
    except Exception as e:
        print("EXCEPTION :", type(e).__name__, e)
    # chemin réellement pris par le test « non calculé » existant (témoin illisible)
    o = T._sortie("temoin_illisible")
    print("test existant, motif :", o["audit_symetrie_addendum2"]["explication_trop_propre"]["motif"])

if scenario == "garde7-plancher":
    # artefact : scores de toutes les sondes du plancher altérés sur une action notée du saboteur ; la sonde principale
    # est intacte (son aire ne change pas), le quantile 0,95 des aires du plancher change
    s, lec = T._cas("sain")
    t = s["tables"]
    noms = [str(x) for x in t["noms_sondes"]]
    i = int(np.flatnonzero((t["condition"] == "saboteur") & np.all(np.isfinite(t["scores"]), axis=1))[0])
    for j, n in enumerate(noms):
        if "-plancher-" in n:
            t["scores"][i, j] += 50.0
    try:
        o = av.analyser_addendum2(s, lec, T.G)
        print("PASSE : aucun arrêt ; cohérence des aires :", o["coherence_avec_la_lecture"]["aires"])
    except T.GardeArret as e:
        print("ARRÊT :", e)

if scenario == "garde7-etats":
    # [L] retouchée : P3-P2 « en échec », puis « non calculable », alors que [S] calcule P3-P2 sur toutes ses tâches
    for nom, entree in (("en échec", {"echec": "lecture simulée en échec"}),
                        ("non calculable", {"calculable": False, "motif": "simulé", "effet": None, "bas": None,
                                            "haut": None})):
        s, lec = T._cas("sain")
        lec["P3-P2"] = entree
        try:
            o = av.analyser_addendum2(s, lec, T.G)
            print(f"[L] P3-P2 {nom} : PASSE ; garde 7 :", o["coherence_avec_la_lecture"]["effets"]["P3-P2"],
                  "; contrôles B2/P3-P1 :", [c["controle_contraire"] for c in T._controles(o, "B2", "P3-P1")])
        except T.GardeArret as e:
            print(f"[L] P3-P2 {nom} : ARRÊT :", e)
