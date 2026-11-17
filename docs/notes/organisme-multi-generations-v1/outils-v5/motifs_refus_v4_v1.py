"""Motifs des refus du générateur v4 sur les 12 graines de développement (correction E-6 de la contre-lecture v4).

Calcul seul, aucun appel, aucun réseau, aucun monde de calibration ni de course : graines publiques
`cle("monde-mr1-v4-calibration-developpement", r)`, r = 0 à 11, les mêmes que `sorties-v4/`. Importe le module scellé
`outils-v4/monde_riche_v4.py` sans le modifier (empreinte vérifiée avant import) et rejoue, pour chaque monde, les seuls tirages
refusés (k = 0 à len(refus) − 1 de `generer_v4`), qui s'arrêtent avant C8. Pour chaque refus : contrôle et motif rendus par
`verifier_v4` ; pour un refus C6, en plus, chaque vraie plantée « K1 + un effet » en écart d'attribution, la classe et la sorte
de l'effet ajouté, les effets attendus et captés. Contrôle de cohérence : la suite des contrôles refusés doit être égale au
champ `refus` de `sorties-v4/partie-v4-monde-r.json` ; sinon code 3.

Usage : `python3 -I -B motifs_refus_v4_v1.py SORTIE.json` (un processus, `ulimit -v 6000000`, `OMP_NUM_THREADS=2`).
"""
import datetime, hashlib, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
V4 = os.path.join(RACINE, "outils-v4", "monde_riche_v4.py")
ATTENDU_V4 = "4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8"


def _sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


if _sha(V4) != ATTENDU_V4:
    sys.exit(3)
sys.path.insert(0, os.path.join(RACINE, "outils-v4"))
import numpy as np  # noqa: E402
import monde_riche_v4 as R4  # noqa: E402

M, V1V, V2, P1 = R4.M, R4.V1V, R4.V2, R4.P1


def detail_c6(spec):
    ex = R4.EXIGENCES_V4
    V1V.controler_forme(spec, ex)
    V1V.controler_structure(spec, ex)
    V1V.controler_grammaire(spec, ex)
    loi, oracles, infos = V1V.mesurer(spec, ex)
    V1V.controler_tailles(spec, ex, infos, oracles)
    r45, k1, eid, vraies, _ = V1V.controler_ensemble_et_jeu(spec, ex, oracles[0])
    sorte = {e["id"]: (e["classe"], e["type"]) for e in spec["effets"]}
    out = []
    for nom, v in vraies.items():
        if not nom.startswith("V-K1+"):
            continue
        c = sorted(M.captes(oracles[0].attribution(v["loi"], spec), infos[0]))
        ecart = sorted(set(c) ^ set(v["effets"]))
        if ecart and r45["vraies"][nom]["vraie_au_sens_de_l_oracle"]:
            ajoute = nom[len("V-K1+"):]
            out.append({"vraie": nom, "classe_ajoutee": sorte[ajoute][0], "sorte_ajoutee": sorte[ajoute][1],
                        "attendus": v["effets"], "captes": c, "ecart": ecart,
                        "au_dela_archive_v60": r45["vraies"][nom]["au_dela_archive_v60"]})
    return {"effet_de_k1": eid, "vraies_en_ecart": out}


def main(sortie):
    if os.path.exists(sortie):
        sys.exit("refus : sortie existante")
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    res, ok = [], True
    for r in range(12):
        partie = os.path.join(RACINE, "sorties-v4", f"partie-v4-monde-{r}.json")
        attendu = json.load(open(partie, encoding="utf-8"))["resultat"]["refus"]
        graine = P1.cle("monde-mr1-v4-calibration-developpement", r)
        tirages = []
        for k in range(len(attendu)):
            sous = int(np.random.SeedSequence(graine, spawn_key=(k,)).generate_state(1, dtype=np.uint64)[0])
            spec = R4.generer_monde_v4(sous)
            rap = R4.verifier_v4(spec)
            t = {"tirage": k, "conforme": rap["conforme"], "controle": rap.get("refus", {}).get("controle"),
                 "motif": rap.get("refus", {}).get("motif"),
                 "conditionnelles": [e["id"] for e in spec["effets"] if e["type"] == "interaction_xor"],
                 "composantes": len(spec["effets"])}
            if t["controle"] == "C6":
                t["detail_c6"] = detail_c6(spec)
            tirages.append(t)
            print(r, k, t["controle"], t["motif"], flush=True)
        egal = [t["controle"] for t in tirages] == attendu
        ok &= egal
        res.append({"monde": r, "refus_attendus": attendu, "egal_a_la_partie_v4": egal, "tirages": tirages})
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump({"version": "motifs-refus-v4-v1", "debut_utc": debut,
                   "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   "script_sha256": _sha(os.path.abspath(__file__)), "monde_riche_v4_sha256": ATTENDU_V4,
                   "tous_egaux": ok, "resultat": res}, f, ensure_ascii=False, indent=1, sort_keys=True)
    sys.exit(0 if ok else 3)


if __name__ == "__main__":
    main(sys.argv[-1])
