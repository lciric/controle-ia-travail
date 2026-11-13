"""Correctif v3b de la partie « générations, condition regroupement » de `puissance_monde_riche_v3.py` (`60aee2a3…`, scellé,
inchangé) : dans la v3, la fonction de remplacement appelait `representant_v3`, qui appelait `M2.representant_v2`… déjà
remplacée : récursion infinie, les 12 parties ont échoué (code 1, `journal-sorties-v3.txt`) et un résumé vide a été scellé
(`generations-a2-v3-resume.json`, gardé). Ici la règle v2 d'origine est gardée à part avant le remplacement.
Usage : `python3 -I -B puissance_monde_riche_v3b.py generations-a2 RANG SORTIE.json` | `resume DOSSIER SORTIE.json`."""
import datetime, glob, hashlib, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import puissance_monde_riche_v3 as P3

M2, P2 = P3.M2, P3.P2
REGLE_V2_ORIGINE = M2.representant_v2
GROUPER_ORIGINE = M2.grouper_v2


def partie(w):
    etat = {}

    def grouper_capture(cartes, Zref, Gref, nsp, **k):
        etat["cartes"] = cartes
        return GROUPER_ORIGINE(cartes, Zref, Gref, nsp, **k)

    def rep_v3(groupe, dg, can, statistique_de_choix=None):
        cle = "|".join(sorted(can[i] for i in groupe))
        tr = {}

        def choix(i):
            if "t" not in tr:
                tr["t"] = P3.tranche_de_choix(etat["monde"], etat["D"], etat["nsp"], cle)
            return P3.statistique(etat["cartes"][i], *tr["t"])
        return REGLE_V2_ORIGINE(groupe, dg, can, statistique_de_choix=choix)

    spec, cibles, loi, o, k1, eid_k1, infos = P2.preparer_monde_v2(w)
    etat.update(monde=loi, D=spec["dimension"], nsp=spec["sous_populations"])
    M2.representant_v2, M2.grouper_v2 = rep_v3, grouper_capture
    try:
        return P2._generations_course_v2((w, "A2", 3, 400, P2.M_DESSIN))
    finally:
        M2.representant_v2, M2.grouper_v2 = REGLE_V2_ORIGINE, GROUPER_ORIGINE


def resume(dossier):
    parts = [json.load(open(p))["resultat"] for p in sorted(glob.glob(os.path.join(dossier, "generations-a2-v3b-monde-*.json")))]
    out = {"mondes": len(parts)}
    for g in range(3):
        hs = [(m["generations"][g], m["composantes"]) for m in parts]
        out[str(g + 1)] = {"retenues_moyen": round(float(np.mean([h["retenues"] for h, _ in hs])), 2),
                           "archive_moyen": round(float(np.mean([h["archive"] for h, _ in hs])), 2),
                           "part_captee_moyenne": round(float(np.mean([len(h["captes"]) / c for h, c in hs])), 3),
                           "faibles_captees_moyen": round(float(np.mean([h["captes_par_classe"]["faible"] for h, _ in hs])), 2),
                           "fausses_decouvertes_total": int(sum(h["fausses_decouvertes"] for h, _ in hs)),
                           "retenues_total": int(sum(h["retenues"] for h, _ in hs))}
    return out


if __name__ == "__main__":
    out = sys.argv[-1]
    if os.path.exists(out):
        sys.exit("refus : sortie existante")
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    res = partie(int(sys.argv[2])) if sys.argv[1] == "generations-a2" else resume(sys.argv[2])
    with open(out, "x", encoding="utf-8") as f:
        json.dump({"version": "puissance-monde-riche-v3b", "commande": sys.argv[1:-1], "debut_utc": debut,
                   "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   "graine_de_hachage": "aléatoire (python -I) ; déterminisme par parcours triés",
                   "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                   "resultat": res}, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(res, ensure_ascii=False)[:800])
