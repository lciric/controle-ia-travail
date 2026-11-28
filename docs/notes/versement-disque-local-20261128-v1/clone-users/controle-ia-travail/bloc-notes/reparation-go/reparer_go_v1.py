"""Réparation de forme des lignes GO-2026-10-20-01 à 08 de registres/go.md (VP3-01) : 4 colonnes -> 8.

Le texte de chaque GO reste en « périmètre », sauf la phrase « Donné par Lazar … », déplacée en « référence » avec le
renvoi au registre des décisions ; plafond et échéance tirés du texte, sinon « — » ; accordé par Lazar.
Arrêt si une ligne ne correspond pas exactement à la forme attendue.
"""
import re
import sys
from pathlib import Path

chemin = Path(sys.argv[1])
lignes = chemin.read_text(encoding="utf-8").split("\n")

# id -> (type, plafond, échéance, renvoi au registre des décisions)
CIBLE = {
    "GO-2026-10-20-01": ("revendication", "—", "2026-10-20", "R-253"),
    "GO-2026-10-20-02": ("lecture complémentaire", "—", "—", "N-025"),
    "GO-2026-10-20-03": ("règle", "—", "2026-10-20", "N-026"),
    "GO-2026-10-20-04": ("porte", "—", "2026-10-20", "N-027"),
    "GO-2026-10-20-05": ("lecture complémentaire", "—", "—", "N-028"),
    "GO-2026-10-20-06": ("calcul", "150 USD, plafond de GO-2026-10-04-08 inchangé", "2026-11-30", "R-265 (1)"),
    "GO-2026-10-20-07": ("calcul", "10 USD par lancement, dans les 150 USD de GO-2026-10-04-08 prolongé (GO-2026-10-20-06)",
                         "2026-11-30", "R-269"),
    "GO-2026-10-20-08": ("décision", "—", "2026-10-20", "R-276"),
}
PHRASE = re.compile(r"^(?P<perimetre>.*?)\s*(?P<donne>[Dd]onné par Lazar dans la session 14 (?P<suite>.*?))\.?$")

vues = set()
for k, ligne in enumerate(lignes):
    m = re.match(r"^\| (GO-2026-10-20-0\d) \| ", ligne)
    if not m:
        continue
    ident = m.group(1)
    cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
    if len(cellules) != 4:
        sys.exit(f"{ident} : 4 cellules attendues, {len(cellules)} trouvées (déjà réparée ?)")
    _, accorde, typ, texte = cellules
    typ_c, plafond, echeance, renvoi = CIBLE[ident]
    if accorde != "2026-10-20" or typ != typ_c:
        sys.exit(f"{ident} : date ou type inattendu ({accorde!r}, {typ!r})")
    p = PHRASE.match(texte)
    if not p:
        sys.exit(f"{ident} : phrase « Donné par Lazar dans la session 14 … » introuvable")
    perimetre = p.group("perimetre").rstrip(" ;")
    if perimetre.endswith("."):
        perimetre = perimetre[:-1]
    reference = f"{renvoi} : message de Lazar dans la session 14 {p.group('suite')}"
    nouvelle = (f"| {ident} | {accorde} | {typ} | {perimetre} | {plafond} | {echeance} | Lazar | {reference} |")
    if "|" in perimetre or "|" in reference:
        sys.exit(f"{ident} : barre verticale dans une cellule")
    lignes[k] = nouvelle
    vues.add(ident)

if vues != set(CIBLE):
    sys.exit(f"lignes manquantes : {sorted(set(CIBLE) - vues)}")
chemin.write_text("\n".join(lignes), encoding="utf-8")
print("réparées :", ", ".join(sorted(vues)))
