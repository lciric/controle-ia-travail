"""Complément de `motifs_refus_v4_v1.py` (E-6) : sorte, classe et paramètres de structure (trait, sous-population, trait de
condition, composante de condition ; jamais une pente, un décalage ni un poids) de chaque composante des tirages refusés en C6
sur les graines de développement v4, pour nommer les composantes que l'attribution capte en trop.

Calcul seul ; graines publiques `cle("monde-mr1-v4-calibration-developpement", r)` ; importe `outils-v4/monde_riche_v4.py`
scellé, sans le modifier (empreinte vérifiée) ; ne refait que `generer_monde_v4` sur les sous-graines des tirages que
`sorties-v5/motifs-refus-v4-v1.json` (empreinte vérifiée) donne refusés en C6 ; aucune vérification rejouée.

Usage : `python3 -I -B sortes_refus_c6_v4_v1.py EMPREINTE_MOTIFS SORTIE.json`.
"""
import datetime, hashlib, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
V4 = os.path.join(RACINE, "outils-v4", "monde_riche_v4.py")
MOTIFS = os.path.join(RACINE, "sorties-v5", "motifs-refus-v4-v1.json")
ATTENDU_V4 = "4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8"
CLES = ("id", "classe", "type", "trait", "sous_population", "trait_condition", "composante_condition", "seuil")


def _sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main(attendu_motifs, sortie):
    if os.path.exists(sortie):
        sys.exit("refus : sortie existante")
    if _sha(V4) != ATTENDU_V4 or _sha(MOTIFS) != attendu_motifs:
        sys.exit(3)
    sys.path.insert(0, os.path.join(RACINE, "outils-v4"))
    import numpy as np
    import monde_riche_v4 as R4
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    motifs = json.load(open(MOTIFS, encoding="utf-8"))["resultat"]
    res = []
    for m in motifs:
        graine = R4.P1.cle("monde-mr1-v4-calibration-developpement", m["monde"])
        for t in m["tirages"]:
            if t["controle"] != "C6":
                continue
            sous = int(np.random.SeedSequence(graine, spawn_key=(t["tirage"],)).generate_state(1, dtype=np.uint64)[0])
            spec = R4.generer_monde_v4(sous)
            res.append({"monde": m["monde"], "tirage": t["tirage"],
                        "effets": [{k: e[k] for k in CLES if k in e} for e in spec["effets"]],
                        "vraies_en_ecart": t["detail_c6"]["vraies_en_ecart"], "effet_de_k1": t["detail_c6"]["effet_de_k1"]})
            print(m["monde"], t["tirage"], flush=True)
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump({"version": "sortes-refus-c6-v4-v1", "debut_utc": debut,
                   "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   "script_sha256": _sha(os.path.abspath(__file__)), "monde_riche_v4_sha256": ATTENDU_V4,
                   "motifs_sha256": attendu_motifs, "resultat": res}, f, ensure_ascii=False, indent=1, sort_keys=True)


if __name__ == "__main__":
    main(sys.argv[-2], sys.argv[-1])
