"""Rendement du protocole : part des retenues éprouvées et survivantes, coût, rétention par espèce.

Version 2 (inventaire v2, branches de données comprises). Sortie : sorties/rendement-v2.json.
"""
import json
import sys
from collections import Counter, defaultdict

from audit_commun_v3 import SORTIES, ESPECE_FOURNISSEUR, inventaire


def main():
    inv = inventaire()
    courses = [d for d in inv if d.get("type") == "course" and d["statut_audit"] == "inclus"]
    J = json.loads((SORTIES / "jeu-des-propositions-v2.json").read_text())
    U = json.loads((SORTIES / "unites-v2.json").read_text())["unites"]
    ret = [j for j in J if j["genre"] == "retenue"]
    etats = Counter(j["etat"] for j in ret)
    eprouvees = sum(etats[e] for e in ("éprouvée et survivante", "éprouvée et tombée", "non évaluable"))
    surv = etats["éprouvée et survivante"]
    cout = sum(d["compte_usd"] or 0 for d in courses)
    pire = sum(d["pire_usd"] or 0 for d in courses)
    dossiers_note = sorted({j["dossier"] for j in J})
    cout_note = sum(d["compte_usd"] or 0 for d in courses if d["racine"] in dossiers_note)
    # rétention par espèce : retenues portées (attribution déclarée) / unités de dernier tour, sur les dossiers à note
    units = Counter(u["espece"] for u in U if not u["rejeu_de"] and u["racine"] in dossiers_note)
    portees = Counter(e for j in ret if j["attribution"] == "déclarée" for e in j["especes_porteuses"])
    seules = Counter(j["especes_porteuses"][0] for j in ret if j["attribution"] == "déclarée" and len(j["especes_porteuses"]) == 1)
    inv_idx = {d["racine"]: d for d in courses}
    presentes = Counter()
    for j in ret:
        if j["attribution"] == "déclarée" and j["dossier"] in inv_idx:
            for e in {v.get("espece") for v in inv_idx[j["dossier"]]["lettres"].values()}:
                presentes[e] += 1
    nb_fourn = Counter(len({ESPECE_FOURNISSEUR.get(e, e) for e in j["especes_porteuses"]}) for j in ret if j["attribution"] == "déclarée")
    out = {
        "courses_incluses": len(courses), "courses_avec_note_de_selection": len(dossiers_note),
        "courses_sans_note": sorted(d["racine"] for d in courses if d["racine"] not in dossiers_note),
        "cout_compte_usd_total": round(cout, 2), "cout_pire_usd_total": round(pire, 2),
        "cout_compte_usd_dossiers_a_note": round(cout_note, 2),
        "retenues": len(ret), "etats_retenues": dict(etats),
        "sous_etats": {f"{a} — {b}": n for (a, b), n in Counter((j["etat"], j["sous_etat"]) for j in ret).most_common()},
        "part_eprouvees": round(eprouvees / len(ret), 4), "part_survivantes": round(surv / len(ret), 4),
        "cout_par_survivante_usd": None if surv == 0 else round(cout_note / surv, 2),
        "cout_par_retenue_usd": round(cout_note / len(ret), 2),
        "retention_par_espece": {e: {"unites_dernier_tour": units[e], "retenues_portees": portees[e],
                                     "retenues_portees_seule": seules[e],
                                     "retenues_ou_l_espece_etait_presente": presentes[e],
                                     "part_des_retenues_portees": round(portees[e] / presentes[e], 3) if presentes[e] else None}
                                 for e in sorted(set(units) | set(portees))},
        "retenues_par_nombre_de_fournisseurs_porteurs": dict(sorted(nb_fourn.items())),
        "note": "coût compté : somme des coûts d'appel journalisés (cellules réussies et échouées) ; « pire » : somme des plafonds de pire par appel ; abonnements non comptés ; dossiers de première étape (Fable, Opus) non chiffrés ici.",
    }
    (SORTIES / "rendement-v2.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(json.dumps({k: v for k, v in out.items() if k != "courses_sans_note"}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
