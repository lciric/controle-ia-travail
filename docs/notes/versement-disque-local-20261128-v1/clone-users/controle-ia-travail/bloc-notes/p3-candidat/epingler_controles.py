"""Épingles des contrôles avant dépense de P3 : remplace, dans la copie du bloc-notes, chaque valeur « A_EPINGLER » nommée,
une seule fois chacune, et rien d'autre (le texte de P3 : « les copies versées ne diffèrent du brouillon 3 que par les
valeurs A_EPINGLER des contrôles »). Refuse une valeur mal formée, un nom inconnu, une épingle absente ou déjà posée.
Usage : python3 -I epingler_controles.py CONTROLES NOM=VALEUR…"""
import re
import sys
from pathlib import Path

FORMES = {"CANDIDAT_RELU": r"[0-9a-f]{64}", "CONFIG_RELUE": r"[0-9a-f]{64}", "CONSIGNES_RELUES": r"[0-9a-f]{64}",
          "CODE_RELU": r"[0-9a-f]{40}", "REPETITION_JOUET": r"[0-9a-f]{64}",
          "RAPPORTS_ATTENDUS": r"P3-premier-test-v1-[a-z0-9-]+-v1\.md=[0-9a-f]{64}( P3-premier-test-v1-[a-z0-9-]+-v1\.md=[0-9a-f]{64})+"}


def main(chemin: str, paires: list[str]) -> None:
    f = Path(chemin)
    t = f.read_text(encoding="utf-8")
    vus = set()
    for p in paires:
        nom, _, valeur = p.partition("=")
        if nom not in FORMES or nom in vus:
            raise SystemExit(f"nom inconnu ou en double : {nom}")
        if not re.fullmatch(FORMES[nom], valeur):
            raise SystemExit(f"valeur mal formée pour {nom}")
        vus.add(nom)
        avant = f'{nom}="A_EPINGLER"' if nom == "RAPPORTS_ATTENDUS" else f"{nom}=A_EPINGLER"
        apres = f'{nom}="{valeur}"' if nom == "RAPPORTS_ATTENDUS" else f"{nom}={valeur}"
        lignes = [x for x in t.split("\n") if x.startswith(avant + " ") or x == avant]
        if len(lignes) != 1:
            raise SystemExit(f"épingle {nom} : {len(lignes)} ligne(s) « A_EPINGLER » (une attendue)")
        t = t.replace(lignes[0], apres + lignes[0][len(avant):], 1)
    if vus != set(FORMES):
        raise SystemExit(f"épingles manquantes : {sorted(set(FORMES) - vus)}")
    if "A_EPINGLER" in "\n".join(x for x in t.split("\n") if re.match(r"^[A-Z_]+=", x)):
        raise SystemExit("une épingle « A_EPINGLER » reste")
    f.write_text(t, encoding="utf-8")
    print("épingles posées :", ", ".join(sorted(vus)))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
