"""Contre-lecture v7 (Fable 5.1) — essai 4 : la signature prédictive de la mémoire ignore le moniteur (et la banque).

`memoire.Memoire.signature` = (nombre d'issues, dimension, probabilités de la loi sur une sonde) ; `chercher_classe`
compare à toutes les signatures de même (k, d). Sur un monde à plusieurs moniteurs de même espace (le duel : 3 moniteurs,
k = 3, d = 4) :
(1) une loi éliminée sur le moniteur M0 avec log W final > 0 lègue son cumul à la même loi proposée sur M1 (autre
    hypothèse, autres issues) : héritage entre moniteurs ;
(2) une loi promue sur M0 interdit la même loi sur M1 (« redite d'une survivante ») : la stratégie du catalogue
    « transposition_moniteur » (`simulation._proposeur`) ne peut jamais être jugée ;
(3) granularité : divergences sur la sonde entre les lois monotones douces du proposeur scripté (force 0,8, un trait,
    deux sens, d = 4) et seuil effectif de fusion : combien de classes distinctes ces 8 lois peuvent-elles ouvrir ?
    (sur la course du duel simulé, génération 2 du bras M-expl : 21 propositions sur 26 refusées comme « classe G0-F02
    déjà éprouvée dans cette génération »).
"""

import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(ICI), "copie"))

from essais.aides import fiche  # noqa: E402
from pole.memoire import Memoire  # noqa: E402
from pole.simulation import AdaptateurSimule  # noqa: E402

K, D = 3, 4


def f(ident, loi, moniteur, **modifs):
    return fiche(ident, loi_predictive=loi, severite_attendue=0.05, seuil=20.0,
                 espace_instances={"nombre_issues": K, "dimension": D, "sous_populations": 2, "moniteur": moniteur}, **modifs)


def issue_pari(log_w_final, promue):
    return {"verdict_final": "survit" if promue else "eliminee", "famille_source": "x",
            "pari": {"log_richesse_finale": log_w_final, "log_richesse_max": max(log_w_final, 0.0), "promue": promue}}


def partie_1_et_2():
    loi = AdaptateurSimule._loi_monotone(0, D, K, 1)
    m = Memoire(active=True, graine=3)
    m.nouvelle_generation()
    a = f("A-M0", loi, "M0")
    assert m.garde_redite(a)["accepte"]
    a.statut = "eliminee"
    m.indexer(a, issue_pari(2.4, False), 0)  # éliminée sur M0 avec log W final 2,4 (sous le seuil 3,0)
    m.nouvelle_generation()
    b = f("B-M1", loi, "M1")  # même loi, AUTRE moniteur
    garde_b = m.garde_redite(b)
    heritage_b = m.heritage("B-M1")
    # (2) une loi promue sur M0 interdit la même loi sur M1
    m2 = Memoire(active=True, graine=3)
    m2.nouvelle_generation()
    s = f("S-M0", loi, "M0")
    assert m2.garde_redite(s)["accepte"]
    s.statut = "survit"
    m2.indexer(s, issue_pari(6.0, True), 0)
    m2.nouvelle_generation()
    t = f("T-M1", loi, "M1")
    garde_t = m2.garde_redite(t)
    return {"1_heritage_entre_moniteurs": {"garde_B_sur_M1": garde_b, "heritage_recu_par_B": heritage_b,
                                           "tenu_si_bug": garde_b["accepte"] and heritage_b is not None and heritage_b["cumul"] == 2.4},
            "2_transposition_refusee": {"garde_T_sur_M1": garde_t, "tenu_si_bug": not garde_t["accepte"]}}


def partie_3():
    m = Memoire(active=True, graine=3)
    lois = {f"t{j}{'+' if s > 0 else '-'}": AdaptateurSimule._loi_monotone(j, D, K, s) for j in range(D) for s in (1, -1)}
    sigs = {n: m.signature(f(n.replace("+", "p").replace("-", "m"), l, "M0")) for n, l in lois.items()}
    noms = sorted(sigs)
    matrice = {a: {b: round(Memoire.divergence_moyenne(sigs[a], sigs[b]), 4) for b in noms} for a in noms}
    seuils = {}
    for nb_archivees in (1, 2, 4, 8, 16, 32):
        m._signatures = {f"x{i}": sigs[noms[0]] for i in range(nb_archivees)}
        seuils[nb_archivees] = round(m.seuil_effectif(K, D), 4)
    # classes par fusion gloutonne au seuil de 1 signature archivée (le plus large), puis au seuil de 8
    def classes(seuil):
        cl = []
        for n in noms:
            for c in cl:
                if Memoire.divergence_moyenne(sigs[n], sigs[c[0]]) <= seuil:
                    c.append(n)
                    break
            else:
                cl.append([n])
        return cl
    return {"divergences_sur_la_sonde": matrice, "seuil_effectif_selon_archive": seuils,
            "classes_au_seuil_1_archivee": classes(seuils[1]), "classes_au_seuil_8_archivees": classes(seuils[8]),
            "lois_aleatoires_du_gabarit": None}


def partie_3bis():
    """Même question pour les lois aléatoires du gabarit (référence « aleatoire », poids gaussiens d'écart-type 1,2)."""
    from pole.proposeurs_references import propositions_aleatoires
    m = Memoire(active=True, graine=3)
    desc = {"traits": ["t0", "t1", "t2", "t3"], "moniteurs": {"M0": {"nombre_issues": K}}}
    props = propositions_aleatoires(desc, 40, 20261027, 0)
    sigs = [m.signature(f(f"R{i}", p["loi_predictive"], "M0")) for i, p in enumerate(props)]
    m._signatures = {f"x{i}": sigs[0] for i in range(8)}
    seuil = m.seuil_effectif(K, D)
    paires_fusionnees = sum(1 for i in range(len(sigs)) for j in range(i) if Memoire.divergence_moyenne(sigs[i], sigs[j]) <= seuil)
    return {"seuil_8_archivees": round(seuil, 4), "paires": len(sigs) * (len(sigs) - 1) // 2, "paires_sous_le_seuil": paires_fusionnees}


if __name__ == "__main__":
    rapport = partie_1_et_2()
    rapport["3_granularite_lois_monotones_douces"] = partie_3()
    rapport["3_granularite_lois_monotones_douces"]["lois_aleatoires_du_gabarit"] = partie_3bis()
    print(json.dumps(rapport, ensure_ascii=False, indent=1))
    with open(os.path.join(ICI, "resultat-essai-memoire-moniteur.json"), "w", encoding="utf-8") as fo:
        json.dump(rapport, fo, ensure_ascii=False, indent=1)
