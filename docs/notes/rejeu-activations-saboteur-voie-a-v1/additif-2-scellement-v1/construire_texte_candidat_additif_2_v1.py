"""Construit le texte candidat au scellement de l'additif 2 aux sondes du barreau 8, sans le sceller.

Lit le brouillon 6 vérifié (empreinte exigée) et un fichier JSON de quatre textes
(clés « AD2-1 », « AD2-2 », « AD2-3 », « contre_lecture_2 »), remplace les quatre lieux
ouverts, écrit le texte candidat (refuse d'écraser), puis joue les deux contrôles :
  1. `controle_ia.prereg.problemes` sur le texte candidat ;
  2. comparaison par programme avec le brouillon 6 : seules quatre lignes diffèrent, et
     dans chacune seule la partie permise (dernière cellule des trois lignes de champs,
     suite de l'entrée « Contre-lecture 2 »).
Il ne scelle rien et n'écrit aucun compagnon d'empreinte.
Usage (depuis la racine du dépôt, PYTHONPATH=src) :
  python construire_texte_candidat_additif_2_v1.py <brouillon6.md> <champs.json> <cible.md>
"""
import hashlib
import json
import sys
from pathlib import Path

EMPREINTE_B6 = "3a3a4d167af8998de4aa296d30c664e59e25b8e4d71240ba3ce992504b1f1a03"
MARQUEUR = "À REMPLIR"
DEBUT_CL2 = "- **Contre-lecture 2 (finale : vérification du brouillon 6, texte rempli)** : "
CELLULES = ("AD2-1", "AD2-2", "AD2-3")


def construire(texte: str, champs: dict) -> str:
    assert set(champs) == {"AD2-1", "AD2-2", "AD2-3", "contre_lecture_2"}, sorted(champs)
    lignes = texte.split("\n")
    faits = 0
    for i, ligne in enumerate(lignes):
        for cle in CELLULES:
            if ligne.startswith(f"| {cle} | "):
                assert ligne.endswith(f" | {MARQUEUR} |"), cle
                valeur = champs[cle]
                assert "|" not in valeur and "\n" not in valeur, f"{cle} : barre ou saut de ligne interdit dans une cellule"
                lignes[i] = ligne[: -len(f"{MARQUEUR} |")] + valeur + " |"
                faits += 1
        if ligne.startswith(DEBUT_CL2):
            assert ligne == DEBUT_CL2 + MARQUEUR
            assert "\n" not in champs["contre_lecture_2"]
            lignes[i] = DEBUT_CL2 + champs["contre_lecture_2"]
            faits += 1
    assert faits == 4, faits
    return "\n".join(lignes)


def comparer(avant: str, apres: str) -> tuple[list[str], list[str]]:
    """Rend (écarts hors des quatre lieux permis, lieux changés) ; écarts vide si la règle du scellement tient."""
    a, b = avant.split("\n"), apres.split("\n")
    if len(a) != len(b):
        return [f"nombre de lignes différent : {len(a)} contre {len(b)}"]
    ecarts, lieux = [], []
    for n, (x, y) in enumerate(zip(a, b), start=1):
        if x == y:
            continue
        permis = False
        for cle in CELLULES:
            tete = x[: -len(f"{MARQUEUR} |")] if x.endswith(f" | {MARQUEUR} |") else None
            if x.startswith(f"| {cle} | ") and tete is not None and y.startswith(tete) and y.endswith(" |") \
                    and "|" not in y[len(tete):-2]:
                permis, nom = True, f"cellule {cle}"
        if x == DEBUT_CL2 + MARQUEUR and y.startswith(DEBUT_CL2):
            permis, nom = True, "entrée « Contre-lecture 2 »"
        if permis:
            lieux.append(f"ligne {n} : {nom}")
        else:
            ecarts.append(f"ligne {n} : différence hors des lieux permis")
    if len(lieux) != 4:
        ecarts.append(f"{len(lieux)} lieu(x) permis changé(s) au lieu de 4")
    return ecarts, lieux


def main() -> int:
    from controle_ia import prereg

    source, fichier_champs, cible = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    brut = source.read_bytes()
    assert hashlib.sha256(brut).hexdigest() == EMPREINTE_B6, "le brouillon 6 n'a pas l'empreinte attendue"
    champs = json.loads(fichier_champs.read_text(encoding="utf-8"))
    if cible.exists():
        raise SystemExit(f"refus : {cible} existe (règle R12)")
    avant = brut.decode("utf-8")
    apres = construire(avant, champs)
    cible.write_text(apres, encoding="utf-8")
    print("texte candidat :", cible)
    print("empreinte      :", hashlib.sha256(cible.read_bytes()).hexdigest())
    print("marqueurs d'attente restants :", apres.count(MARQUEUR))
    print("contrôle 1 — controle_ia.prereg.problemes :", prereg.problemes(cible))
    ecarts, lieux = comparer(avant, apres)
    print("contrôle 2 — lieux changés :", lieux)
    print("contrôle 2 — écarts hors des quatre lieux permis :", ecarts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
