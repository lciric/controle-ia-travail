"""Transcription mécanique de l'inventaire de tests/test_cibles_invisibles_v3.py en JSON (sans importer l'essai).

Usage : python3 -I transcrire_inventaire_v1.py ESSAI_V3 SORTIE_JSON
Lit par l'arbre syntaxique REGISTRE, LECTEURS_DE_CIBLES_ADMIS et HORS_INVENTAIRE ; COUVERT et EXEMPT sont résolus
depuis leurs affectations dans le même fichier. Refuse tout autre nom non littéral.
"""
import ast
import json
import sys
from pathlib import Path


def main(essai: str, sortie: str) -> None:
    arbre = ast.parse(Path(essai).read_text(encoding="utf-8"))
    noms = {}
    for n in arbre.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            noms[n.targets[0].id] = n.value
    constantes = {k: ast.literal_eval(noms[k]) for k in ("COUVERT", "EXEMPT")}

    def valeur(noeud):
        if isinstance(noeud, ast.Name):
            if noeud.id not in constantes:
                raise SystemExit(f"nom non littéral refusé : {noeud.id}")
            return constantes[noeud.id]
        if isinstance(noeud, ast.Tuple):
            return [valeur(e) for e in noeud.elts]
        return ast.literal_eval(noeud)

    registre_noeud = noms["REGISTRE"]
    registre = {}
    for k, v in zip(registre_noeud.keys, registre_noeud.values):
        cle = ast.literal_eval(k)
        if cle in registre:
            raise SystemExit(f"clé en double : {cle}")
        statut, raison = valeur(v)
        registre[cle] = {"statut": statut, "raison": raison}
    lecteurs = {m: sorted(s) for m, s in ast.literal_eval(noms["LECTEURS_DE_CIBLES_ADMIS"]).items()}
    hors = list(ast.literal_eval(noms["HORS_INVENTAIRE"]))
    doc = {
        "version": "v4",
        "source": "transcription mécanique de tests/test_cibles_invisibles_v3.py (REGISTRE, LECTEURS_DE_CIBLES_ADMIS, "
                  "HORS_INVENTAIRE), sans changement de contenu ; lue par tests/test_cibles_invisibles_v4.py",
        "statuts": constantes,
        "registre": dict(sorted(registre.items())),
        "lecteurs_de_cibles_admis": dict(sorted(lecteurs.items())),
        "hors_inventaire": hors,
    }
    Path(sortie).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(len(registre), "entrées au registre ;", sum(map(len, lecteurs.values())), "lecteurs admis ;", len(hors), "dossier(s) hors inventaire")


if __name__ == "__main__":
    main(*sys.argv[1:])
