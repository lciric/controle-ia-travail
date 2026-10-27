"""Rejouable : vérifie le lien mesures.json <-> engagement gelé et range les issues telles quelles."""
import hashlib, json, os, sys

D = os.path.dirname(os.path.abspath(__file__))
EMP_FICHE = "a2eea19a89c2020056116c958e548d9cb57e8067423bc7d32d98ef3c1cdd9b81"
EMP_ENG = "a4a978dc523ac874f1f80a0e40185e485c6fa728750463e0a5707942d18f8f6b"


def sha_fichier(nom):
    with open(os.path.join(D, nom), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def charger(nom):
    with open(os.path.join(D, nom), encoding="utf-8") as f:
        return json.load(f)


def main():
    assert sha_fichier("fiche.json") == EMP_FICHE, "fiche modifiée"
    assert sha_fichier("engagement.json") == EMP_ENG, "engagement modifié"
    m = charger("mesures.json")
    assert m["empreinte_engagement"] == EMP_ENG, "mesures non liées à l'engagement"
    o = charger("ordre-execution.json")
    assert o["empreinte_engagement"] == EMP_ENG, "ordre non lié à l'engagement"
    emp_ordre = hashlib.sha256(json.dumps(o["ordre"], separators=(",", ":")).encode()).hexdigest()
    assert emp_ordre == m["empreinte_ordre"], "empreinte d'ordre incohérente"
    n = len(m["issues"])
    assert sorted(o["ordre"]) == list(range(n)), "ordre non permutation du plan"
    sortie = {
        "empreinte_engagement": m["empreinte_engagement"],
        "issues": m["issues"],  # déjà rangées à l'indice de leur instance, inchangées
        "plan_execution": m["plan_execution"],
        "empreinte_ordre": m["empreinte_ordre"],
    }
    with open(os.path.join(D, "tirages.json"), "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=2)
    print("tirages.json écrit :", n, "issues ; empreinte_ordre", m["empreinte_ordre"])


if __name__ == "__main__":
    sys.exit(main())
