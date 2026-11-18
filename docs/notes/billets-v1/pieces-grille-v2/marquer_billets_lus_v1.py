"""Marquage des billets de la tenue à l'écart v2 qui étaient dans la moitié développement v1.

Mandat : docs/notes/billets-v1/mandat-revision-grille-v1.md, point 3.
Ces billets ont été lus par l'auteur de la grille v1 ; ils restent dans la tenue à l'écart v2,
marqués, et les résultats seront rapportés avec et sans eux (décision de la session mère).

Le script ne lit que deux champs des deux manifestes : `identifiant` et `moitie`
(plus `classe`, `apparie_a` et `sans_apparie` du manifeste v2, pour dire quelles paires sont touchées).
Il n'ouvre aucun texte de billet ni de commentaire.

Usage :
    python marquer_billets_lus_v1.py MANIFESTE_V1 MANIFESTE_V2 SORTIE_JSON
"""
import hashlib
import json
import sys


def empreinte(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main(m1_chemin, m2_chemin, sortie):
    m1 = json.load(open(m1_chemin, encoding="utf-8"))
    m2 = json.load(open(m2_chemin, encoding="utf-8"))
    moitie_v1 = {b["identifiant"]: b["moitie"] for b in m1["billets"]}
    v2 = {b["identifiant"]: b for b in m2["billets"]}

    marques = []
    for ident in sorted(v2):
        b = v2[ident]
        if b["moitie"] == "tenue-a-l-ecart" and moitie_v1.get(ident) == "developpement":
            marques.append(ident)

    # Paires touchées : une paire (bien noté, apparié) est touchée si l'un de ses membres est marqué.
    paires = []
    for ident, b in sorted(v2.items()):
        if b["moitie"] != "tenue-a-l-ecart" or b["classe"] != "bien-note" or b["sans_apparie"]:
            continue
        ap = b["apparie_a"]
        paires.append({
            "bien_note": ident,
            "apparie": ap,
            "bien_note_marque": ident in marques,
            "apparie_marque": ap in marques,
        })
    sans_apparie = sorted(i for i, b in v2.items()
                          if b["moitie"] == "tenue-a-l-ecart" and b["classe"] == "bien-note" and b["sans_apparie"])

    croisement = {}
    for ident, b in v2.items():
        cle = f"v1={moitie_v1.get(ident, 'absent')}|v2={b['moitie']}"
        croisement[cle] = croisement.get(cle, 0) + 1

    resultat = {
        "version": "v1",
        "manifeste_v1": {"chemin": m1_chemin, "sha256": empreinte(m1_chemin)},
        "manifeste_v2": {"chemin": m2_chemin, "sha256": empreinte(m2_chemin)},
        "champs_lus": ["identifiant", "moitie", "classe", "apparie_a", "sans_apparie"],
        "regle": "marqué = moitie v2 'tenue-a-l-ecart' et moitie v1 'developpement'",
        "nombre_marques": len(marques),
        "marques": [{"identifiant": i, "classe": v2[i]["classe"], "sans_apparie": v2[i]["sans_apparie"]}
                    for i in marques],
        "paires_tenue": len(paires),
        "paires_intactes": sum(1 for p in paires if not p["bien_note_marque"] and not p["apparie_marque"]),
        "paires_touchees": [p for p in paires if p["bien_note_marque"] or p["apparie_marque"]],
        "bien_notes_sans_apparie_tenue": len(sans_apparie),
        "bien_notes_sans_apparie_marques": sum(1 for i in sans_apparie if i in marques),
        "croisement_des_moities": dict(sorted(croisement.items())),
    }
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"{len(marques)} billets marqués ; paires intactes {resultat['paires_intactes']} sur {len(paires)}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
