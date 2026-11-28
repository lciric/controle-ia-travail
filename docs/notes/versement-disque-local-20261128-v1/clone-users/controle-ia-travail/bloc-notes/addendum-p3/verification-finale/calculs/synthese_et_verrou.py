"""VF3, partie 2 (compléments) :
(a) `synthese` sur des analyses fabriquées (3 000 cas aléatoires : conclusions établies quelconques, contrôles contraires,
    favorables, « non lus », « sans objet », entrées en échec, réserves de forme de A7, audit R4 de la lecture déclenché
    ou non), comparée à une synthèse écrite ici d'après le texte (plan, point 6 ; critères gelés ; garde 11) ;
(b) `exiger_verrou` sur des sorties réelles altérées (une violation par cas) : chaque violation du verrou que la
    précision 16 nomme doit arrêter ; la sortie intacte passe.

Usage : python -B synthese_et_verrou.py <journal json>"""
import copy
import json
import sys

from commun import P, cp, np, tc  # noqa: F401
from verrou_proprietes import (LECT_A7, RESERVES_TEXTE, VISEES_TEXTE, base_scenarios, lecture_reduite, muter,
                               recalculer, table_point5)

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines

G = graines(cp.cles_addendum(P), cp.ENTROPIE_P3)
POSSIBLES = ["P3-P1"] + [f"{c}/{p}" for p in P for c in ("P3-P3", "P3-P4", "T1", "T2", "T3", "T4")]
SUSPECT = "addendum suspect de propreté : à signaler au verdict et à soumettre à Lazar"


def fabriquer(rng):
    pe = float(rng.choice([0.0, 0.1, 0.3, 0.6, 1.0]))          # part des conclusions établies, une par cas
    pc = rng.choice([[1.0, 0.0], [0.0, 1.0], [0.0, 0.0], [0.35, 0.35]])   # (contraire, favorable), le reste « non lu »
    etab = [c for c in POSSIBLES if rng.random() < pe]
    analyses = {}
    for a in cp.ANALYSES:
        sondes = [None] if a in ("A6", "A9") else P
        sortie = {}
        for p in sondes:
            ctrls = []
            if a != "A9":
                for _ in range(int(rng.integers(0, 8))):
                    base = sorted(VISEES_TEXTE[a])[int(rng.integers(0, len(VISEES_TEXTE[a])))]
                    q = p if p is not None else P[int(rng.integers(0, 2))]
                    cible = "P3-P1" if base == "P3-P1" else f"{base}/{q}"
                    test = f"{a} essai {int(rng.integers(0, 4))}"
                    if cible not in etab:
                        ctrls.append({"test": test, "cible": cible, "controle_contraire": "sans objet"})
                        continue
                    u = rng.random()
                    if u < pc[0]:
                        noms = [n for n, (aa, bases) in RESERVES_TEXTE.items() if aa == a and base in bases]
                        nom = noms[int(rng.integers(0, len(noms)))]
                        ctrls.append({"test": test, "cible": cible, "controle_contraire": True, "reserve": nom,
                                      "motif": "m"})
                    elif u < pc[0] + pc[1]:
                        ctrls.append({"test": test, "cible": cible, "controle_contraire": False, "reserve": None,
                                      "motif": "m"})
                    else:
                        ctrls.append({"test": test, "cible": cible, "controle_contraire": "non lu",
                                      "reserve": f"reserve_{a}_non_lue", "motif": "m"})
            sortie[p] = {"etat": "échec" if rng.random() < rng.choice([0.0, 0.3, 0.8]) else "calculé",
                         "calculs_en_echec": [], "descriptif": {}, "controles": ctrls}
        analyses[a] = sortie[None] if a in ("A6", "A9") else sortie
    return analyses, etab, bool(rng.random() < 0.5)


def attendu(analyses, etab, r4):
    entrees = []
    for a in cp.ANALYSES:
        entrees += [(a, None, analyses[a])] if a in ("A6", "A9") else [(a, p, x) for p, x in analyses[a].items()]
    ctrls = [c for _, _, x in entrees for c in x["controles"]]
    en_echec = sum(1 for _, _, x in entrees if x["etat"] == "échec")
    generale = 2 * en_echec > len(entrees)
    reserves = {(c["reserve"], c["cible"], c["test"]) for c in ctrls if c.get("reserve")}
    if generale:
        reserves |= {("reserve_addendum_largement_non_lu", c, "garde 11") for c in etab}
    possibles = [c for c in ctrls if c["controle_contraire"] != "sans objet"]
    decl = [c for c in possibles if c["controle_contraire"] is True]
    toutes = bool(possibles) and len(decl) == len(possibles)
    aucune = not decl and len(etab) >= 3 and r4
    contr, nonc = {}, {}
    for c in ctrls:
        if c.get("reserve"):
            (contr if c["controle_contraire"] is True else nonc).setdefault(c["cible"], set()).add(c["reserve"])
    if generale:
        for c in etab:
            nonc.setdefault(c, set()).add("reserve_addendum_largement_non_lu")
    return {"reserves": reserves, "declencheur": toutes or aucune, "possibles": len(possibles), "decl": len(decl),
            "contr": contr, "nonc": nonc, "generale": generale}


def verifier_synthese(analyses, etab, r4, s):
    v = []
    att = attendu(analyses, etab, r4)
    rendues = {(r["nom"], r["cible"], r["test"]) for r in s["reserves_addendum"]}
    if rendues != att["reserves"]:
        v.append(f"réserves : en trop {sorted(rendues - att['reserves'])}, manquantes {sorted(att['reserves'] - rendues)}")
    triees = sorted(s["reserves_addendum"], key=lambda r: (r["nom"], r["sonde"] or "", r["cible"], r["test"], r["motif"]))
    if triees != s["reserves_addendum"]:
        v.append("réserves non triées")
    au = s["audit_symetrie_addendum"]
    if (au["declencheur"], au["reserves_possibles"], au["reserves_declenchees"]) != (att["declencheur"], att["possibles"],
                                                                                     att["decl"]):
        v.append(f"audit : {au} ≠ {att['declencheur'], att['possibles'], att['decl']}")
    if (au["lecture"] == SUSPECT) != att["declencheur"]:
        v.append("audit : lecture incohérente")
    rec = s["recommandation_au_verdict_R13"]
    if not etab:
        if rec != ["aucune conclusion établie : réserves sans objet"]:
            v.append(f"recommandation sans conclusion : {rec}")
        return v
    n = 0
    for c in etab:
        lignes = [z for z in rec if z.startswith(f"{c} : ")]
        if c in att["contr"]:
            n += 1
            pre = (f"{c} : établie au sens de la lecture décisive, non robuste aux contrôles de l'addendum (réserves : "
                   f"{', '.join(sorted(att['contr'][c]))})")
            l1 = [z for z in lignes if z.startswith(pre)]
            if len(l1) != 1:
                v.append(f"ligne non robuste de {c} : {lignes}")
            else:
                for nom, lect in LECT_A7.items():
                    if (nom in att["contr"][c]) != (lect in l1[0]):
                        v.append(f"lecture gelée de {nom} pour {c}")
        if c in att["nonc"]:
            n += 1
            pre = f"{c} : non contrôlée par l'addendum (réserves : {', '.join(sorted(att['nonc'][c]))})"
            l2 = [z for z in lignes if z.startswith(pre)]
            if len(l2) != 1 or "non robuste" in l2[0]:
                v.append(f"ligne non contrôlée de {c} : {lignes}")
    if len(rec) != n:
        v.append(f"recommandation : {len(rec)} lignes ≠ {n}")
    for z in rec:
        if z.split(" : ")[0] not in etab:
            v.append(f"recommandation sur une conclusion non établie : {z}")
    return v


def violations_du_verrou(s, lec, etab):
    """Sorties altérées, chacune d'une violation du verrou (précision 16) ; rend (nom, sortie, etablies passées)."""
    non_etab = [c for c in POSSIBLES if c not in etab]
    cas = []
    x = copy.deepcopy(s)
    x["issue_primaire"]["ligne"] = x["issue_primaire"]["ligne"] + " (altérée)"
    cas.append(("issue recopiée altérée", x, etab))
    if non_etab:
        x = copy.deepcopy(s)
        x["reserves_addendum"].append({"nom": "reserve_A1_plancher_conjoint", "analyse": "A1", "sonde": P[0],
                                       "cible": non_etab[0], "test": "x", "motif": "x"})
        cas.append(("réserve sur une conclusion non établie", x, etab))
        x = copy.deepcopy(s)
        x["conclusions_etablies"] = list(etab) + [non_etab[0]]
        cas.append(("conclusion promue dans la sortie", x, etab))
        cas.append(("conclusion promue dans la liste des analyses", copy.deepcopy(s), list(etab) + [non_etab[0]]))
    x = copy.deepcopy(s)
    x["reserves_addendum"].append({"nom": "reserve_A1_plancher_conjoint", "analyse": "A1", "sonde": P[0],
                                   "cible": "T9/inconnue", "test": "x", "motif": "x"})
    cas.append(("réserve hors de la table fermée", x, etab))
    sans = [(a, p, c) for a in cp.ANALYSES for p, e in ([(None, s["analyses"][a])] if a in ("A6", "A9")
                                                     else s["analyses"][a].items())
            for c in e["controles"] if c["controle_contraire"] == "sans objet"]
    if sans:
        a, p, c = sans[0]
        x = copy.deepcopy(s)
        e = x["analyses"][a] if p is None else x["analyses"][a][p]
        k = e["controles"].index(c)
        e["controles"][k] = {**c, "controle_contraire": True, "reserve": "reserve_X", "motif": "x"}
        cas.append(("contrôle contraire sur une cible non établie", x, etab))
        x = copy.deepcopy(s)
        e = x["analyses"][a] if p is None else x["analyses"][a][p]
        e["controles"][k] = {**c, "motif": "écrit hors du descriptif"}
        cas.append(("contrôle sans objet qui écrit hors du descriptif", x, etab))
        x = copy.deepcopy(s)
        e = x["analyses"][a] if p is None else x["analyses"][a][p]
        e["controles"][k] = {**c, "controle_contraire": False, "reserve": None, "motif": "x"}
        cas.append(("contrôle favorable lu sur une cible non établie", x, etab))
    for cle in ("etabli", "etablie", "conforme", "retenue", "au_dessus_du_plancher", "a_au_dessus_de_b"):
        x = copy.deepcopy(s)
        x["analyses"]["A3"][P[1]]["descriptif"].setdefault("profond", {})[cle] = True
        cas.append((f"clé interdite {cle}", x, etab))
    return cas


def main(chemin):
    rng = np.random.default_rng(777)
    journal = {"synthese": {"cas": 0, "violations": [], "repartition": {}}, "verrou": []}
    rep = journal["synthese"]["repartition"]
    for i in range(int(sys.argv[2]) if len(sys.argv) > 2 else 3000):
        analyses, etab, r4 = fabriquer(rng)
        s = cp.synthese(copy.deepcopy(analyses), etab, r4)
        v = verifier_synthese(analyses, etab, r4, s)
        journal["synthese"]["cas"] += 1
        cle = (f"etablies={'0' if not etab else '1-2' if len(etab) < 3 else '3+'}, déclencheur="
               f"{s['audit_symetrie_addendum']['declencheur']}, générale={attendu(analyses, etab, r4)['generale']}")
        rep[cle] = rep.get(cle, 0) + 1
        if v:
            journal["synthese"]["violations"].append({"i": i, "v": v[:5]})
    print("synthèse :", journal["synthese"]["cas"], "cas,", len(journal["synthese"]["violations"]), "en violation",
          flush=True)
    print(json.dumps(rep, ensure_ascii=False, indent=1))
    # (b) verrou sur des sorties réelles
    tc.cp.TIRAGES_AIRE, tc.cp.TIRAGES_COUT = 60, 500
    S = base_scenarios()
    rng2 = np.random.default_rng(99)
    for nom in ("sain", "temoin", "consigne_mention", "non_etabli", "varie"):
        src = S[nom]()
        lec0 = lecture_reduite(src)
        for k in range(2):
            lec = copy.deepcopy(lec0)
            if k:
                muter(lec, rng2)
            recalculer(lec)
            s = cp.analyser_addendum(src, lec, G)
            etab = table_point5(lec)
            issue = cp._canonique(lec["issue"])
            try:
                cp.exiger_verrou(copy.deepcopy(s), lec, etab, P, issue)
                journal["verrou"].append({"scenario": nom, "k": k, "cas": "sortie intacte", "arret": False,
                                          "attendu": False})
            except (GardeArret, cp.DefautDuModule) as e:
                journal["verrou"].append({"scenario": nom, "k": k, "cas": "sortie intacte", "arret": True,
                                          "attendu": False, "motif": str(e)[:200]})
            for cas, x, etab_ in violations_du_verrou(s, lec, etab):
                try:
                    cp.exiger_verrou(x, lec, etab_, P, issue)
                    arret, motif = False, None
                except (GardeArret, cp.DefautDuModule) as e:
                    arret, motif = True, f"{type(e).__name__} : {str(e)[:160]}"
                journal["verrou"].append({"scenario": nom, "k": k, "cas": cas, "arret": arret, "attendu": True,
                                          "motif": motif, "etablies": len(etab)})
            print(nom, k, "verrou :", sum(1 for z in journal["verrou"] if z["arret"] != z["attendu"]), "écarts cumulés",
                  flush=True)
    journal["verrou_ecarts"] = [z for z in journal["verrou"] if z["arret"] != z["attendu"]]
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(journal, f, ensure_ascii=False, indent=1, default=str)
    print("verrou :", len(journal["verrou"]), "cas,", len(journal["verrou_ecarts"]), "écarts")


if __name__ == "__main__":
    main(sys.argv[1])
