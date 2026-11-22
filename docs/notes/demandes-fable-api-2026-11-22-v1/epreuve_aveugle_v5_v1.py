"""Épreuve aveugle rejouée dans la forme de la v2 (epreuve-aveugle-motifs-v2.md, 8720522f…), sur la version 5 des pièces.

Opus 5.5, 22 novembre 2026. Mêmes trois textes (textes-aveugles-epreuve-v1.json, 1dbdcb40…), écrits par un agent neuf
qui n'avait lu que les consignes des tours III.1 et III.3 du collisionneur v8d, sans balise. Deux règles jouées :
  1. l'ancienne règle de la v4 (fonction `duels` de epreuve_motifs_correction_28_v2.py, d1caea7b…), pour la sortie brute
     que la relecture c1cebee3… demande au rapport rejoué (on compte len(ouvertures), non la longueur du couple) ;
  2. la règle de l'article 4 de la v5 (code de référence de la relecture, lu et exécuté tel quel).
Attendus : règle 1, le nombre fixé par l'auteur des textes (3, 3, 2) ; règle 2, « non conforme » pour les trois, puisque
les textes ne portent aucune balise (piège « H_A et H_B sans balise » de l'article 9). Ce rejeu n'est pas le lot aveugle de
l'article 9 de la v5 (six textes écrits d'après les consignes balisées), qui reste à jouer.
Lancer depuis ce dossier : python3 -I epreuve_aveugle_v5_v1.py
"""
import hashlib
import importlib.util
import json
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
REL = ICI / "relecture-pieces-essaim-v4" / "relecture-fable-api.md"
TEXTES = ICI / "textes-aveugles-epreuve-v1.json"
ANCIEN = ICI / "epreuve_motifs_correction_28_v2.py"
SHA = {REL: "c1cebee3a8abec9cc142c458a6eb05800f2095fcef576fc99c0a93a974c7b4d7",
       TEXTES: "1dbdcb40554deaa27f64ca52b5834d33975b033d6f27534a10aebcdb2279774c",
       ANCIEN: "d1caea7bdaa66ef2b18fdcf1b23b8d84a8c1d5b872fc52d4de637949e0d5d1ac"}
for p, h in SHA.items():
    if hashlib.sha256(p.read_bytes()).hexdigest() != h:
        raise SystemExit(f"empreinte inattendue : {p.name}")

spec = importlib.util.spec_from_file_location("ancienne_regle", ANCIEN)
ancienne = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ancienne)

t = REL.read_text(encoding="utf-8")
bloc = t.split("**Code de référence de l'article 4 (non exécuté).**", 1)[1].split("```python\n", 1)[1].split("\n```", 1)[0]
REGLE = {}
exec(compile(bloc, "code-de-reference-article-4", "exec"), REGLE)


def main():
    textes = json.loads(TEXTES.read_text(encoding="utf-8"))
    ok1 = ok2 = 0
    print("RÈGLE 1 — ancienne règle de la v4 (sortie brute)")
    for k, x in enumerate(textes, start=1):
        bornes, ouv = ancienne.duels(x["texte"])
        n = len(ouv)
        ok1 += n == x["duels_attendus"]
        print(f"texte {k} : attendu {x['duels_attendus']}, obtenu {n}, section (b) lignes {bornes} : "
              f"{'PASSE' if n == x['duels_attendus'] else 'ÉCHOUE'}")
        for l in ouv:
            print(f"    ouverture : {l.strip()[:100]}")
    print(f"règle 1 : {ok1} sur 3")
    print("\nRÈGLE 2 — article 4 de la v5 (balises)")
    for k, x in enumerate(textes, start=1):
        conforme, duels = REGLE["duels_balises"](x["texte"])
        ok2 += conforme is False
        print(f"texte {k} : attendu non conforme ; obtenu {'conforme, n = ' + str(len(duels)) if conforme else 'non conforme'} : "
              f"{'PASSE' if conforme is False else 'ÉCHOUE'}")
    print(f"règle 2 : {ok2} sur 3 au verdict attendu (non conforme)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
