#!/usr/bin/env python3
"""Vérification du candidat au scellement v2 (barreau 5, plan « sabotage ou empreinte ») : couples exacts, v1.

Écrit par le vérificateur (Claude Opus 5.5) le 20 novembre 2026. Ne lit que des textes du dépôt ; n'écrit rien (sortie
standard). Pour chaque couple : l'« avant » doit se trouver exactement une fois dans la pièce visée, telle qu'elle est
scellée, et encore une fois au moment où il s'applique, dans l'ordre de la liste, à une copie en mémoire ; l'« après » ne
doit pas s'y trouver déjà. Le validateur du dépôt (`controle_ia.prereg.problemes`) est joué sur la copie du texte.
Avec `--document CHEMIN`, le programme vérifie de plus que chaque couple est reproduit à l'octet dans ce document.
"""
from __future__ import annotations

import hashlib
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
PLAN = ICI.parent
RACINE = PLAN.parents[3]
T = "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md"
DV = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md"
ATTENDU = {T: "088e15ef", DV: "94a628a7"}
# fin de la ligne de titre, saut de ligne compris (sans lui, l'« après » « — v1 » serait déjà dans l'« avant »)
TITRE = "— v1 — candidat au scellement, à copier à l'octet sous le nom définitif si la vérification le dit scellable tel quel\n"
TITRE_SCELLE = "— v1\n"
RAPPORT = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/verification-candidat-scellement-v2-v1.md"

# (identifiant, constat, touche, pièce, avant, après)
COUPLES = [
    # ---------------------------------------------------------------- X-1 : le registre propre, tel que le code le lit
    ("X-1a", "X-1", "formation", T,
     "## Marqueurs : état au scellement (ce texte est copié à l'octet : ce qui reste ouvert est rempli par la ligne "
     "`SCELLEMENT-B5F` du registre propre, et par elle seule, sans changer le contenu que lit le code de formation : "
     "l'empreinte du devis scellé, la tête du dépôt, les noms des sessions)",
     "## Marqueurs : état au scellement (ce texte est copié à l'octet : ce qui reste ouvert au scellement, l'empreinte "
     "du devis scellé, la tête du dépôt, la vérification du candidat et le nom de la session de formation, s'écrit dans "
     "la colonne de référence de la ligne `SCELLEMENT-B5F` du registre propre ; sa colonne de contenu, que lit le code "
     "de formation, garde exactement le format de « Lignes de registre » ; le nom de la session de lecture, désignée "
     "plus tard, s'écrit dans la colonne de référence de la ligne `GO-LECTURE-B5F`)"),
    ("X-1b", "X-1", "formation", T,
     "Registre propre : `registres/barreau5-familles-jumelles-v1.md`, lignes ajoutées, jamais réécrites ; jamais "
     "`registres/scellements-v1.md`.",
     "Registre propre : `registres/barreau5-familles-jumelles-v1.md`, lignes ajoutées, jamais réécrites ; jamais "
     "`registres/scellements-v1.md`. Chaque ligne à clé est une ligne de table « | CLÉ | instant | contenu | référence | » "
     "; le code lit le contenu des clés au format écrit ci-dessous, à la lettre, et refuse le registre entier s'il trouve "
     "une ligne de table à clé inconnue ou une clé en double ; la référence est libre (ni « | » ni saut de ligne). Tout "
     "le reste, désignations des rôles avec la version de la liste consultée et la catégorie vérifiée (point 7), mot du "
     "rapprochement M-6, s'écrit dans la colonne de référence de la ligne de l'étape, ou sous la table, hors de toute "
     "ligne de table."),
    ("X-1c", "X-1", "formation", T,
     "M-7 : nom de la session de formation et de la session de lecture : remplis par la ligne `SCELLEMENT-B5F` ;",
     "M-7 : nom de la session de formation, écrit dans la colonne de référence de la ligne `SCELLEMENT-B5F`, et nom de "
     "la session de lecture, dans celle de la ligne `GO-LECTURE-B5F` ;"),
    # ---------------------------------------------------------------- X-2 : le devis
    ("X-2a", "X-2", "formation (devis)", DV,
     "nom définitif du candidat `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-"
     "scellement.md`.",
     "nom définitif du candidat `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-"
     "scellement-v2.md`, qui remplace le premier candidat (`…-v1-candidat-scellement.md`) ; le devis des deux "
     "candidats est le même, à l'octet."),
    ("X-2b", "X-2", "formation (devis)", DV,
     "**Brouillon : contre-lu au brouillon 2, vérifié au brouillon 3 ; le brouillon 4 est en vérification.**",
     "**Contre-lu au brouillon 2, vérifié aux brouillons 3 et 4, puis au candidat au scellement v2 (rapport "
     "`verification-candidat-scellement-v2-v1.md`, même dossier).**"),
    ("X-2c", "X-2", "formation (devis)", DV,
     "la limite dure reste l'échéance d'arrêt de l'instance, comptée depuis l'impression de sa commande de création, "
     "qui l'arrête avant sa coupure dans tous les cas)",
     "la limite dure reste l'échéance d'arrêt de l'instance, comptée depuis l'impression de sa commande de création ; "
     "elle borne les heures de carte au prix plafond de la carte, et le stockage et le téléchargement, à leurs bornes, "
     "peuvent faire passer la coupure de quelques USD : c'est la garde de dépense, au cumul relevé, qui tient la "
     "coupure)"),
    ("X-2d", "X-2", "formation (devis)", DV, TITRE, TITRE_SCELLE),
    # ---------------------------------------------------------------- X-3 : l'état du texte une fois scellé
    ("X-3a", "X-3", "lecture", T, TITRE, TITRE_SCELLE),
    ("X-3b", "X-3", "lecture", T,
     "Statut : **candidat au scellement, à copier à l'octet sous le nom définitif si la vérification le dit scellable "
     "tel quel.**",
     "Statut : **texte scellé : le candidat au scellement v2, avec les couples de sa vérification, copié à l'octet "
     "sous le nom définitif.**"),
    ("X-3c", "X-3", "lecture", T,
     "(premier candidat : `54bf29c3f45ae0b2b0318b275948c836bc05aaada97c22a846a64fd776892df5`). ",
     "(premier candidat : `54bf29c3f45ae0b2b0318b275948c836bc05aaada97c22a846a64fd776892df5`) ; enfin les couples de "
     f"la vérification du candidat v2 (`{RAPPORT}`), appliqués à la lettre. "),
    ("X-3d", "X-3", "lecture", T,
     "**Vérification de ce candidat : en attente**, par le même contre-lecteur. Elle porte sur le différentiel du "
     "brouillon 5, sur l'erratum 1 (`8c3451a2e76823d4ae31789164ac6597b2d9b87e809b0e251c295cb8d14a2e40`) et sur les "
     "retouches de consolidation, tous énumérés dans `table-difference-candidat-scellement-v2.md`. S'il est dit "
     "scellable tel quel, ce candidat est copié à l'octet sous le nom définitif.",
     "**Vérification du candidat au scellement v2**, par le même contre-lecteur (Claude Opus 5.5) : rapport "
     f"`{RAPPORT}`. Elle porte sur le différentiel du brouillon 5, sur l'erratum 1 "
     "(`8c3451a2e76823d4ae31789164ac6597b2d9b87e809b0e251c295cb8d14a2e40`) et sur les retouches de consolidation, tous "
     "énumérés dans `table-difference-candidat-scellement-v2.md`. Verdict : « scellable après ces couples » ; ses "
     "couples sont appliqués à la lettre ; l'empreinte du rapport s'écrit dans la colonne de référence de la ligne "
     "`SCELLEMENT-B5F`."),
    ("X-3e", "X-3", "lecture", T,
     "M-10 : fait (vérification du brouillon 4 rendue, « scellable après ces couples ») ; reste la vérification du "
     "candidat au scellement ;",
     "M-10 : fait (vérification du brouillon 4 rendue, « scellable après ces couples ») ; fait (vérification du "
     "candidat au scellement v2 rendue, « scellable après ces couples », ses couples appliqués) ;"),
    # ---------------------------------------------------------------- X-4 : un mot de Lazar, conditions comprises
    ("X-4a", "X-4", "lecture", T,
     "GO-2026-11-19-87` : enveloppe de relance, à part de ce plafond, 56 USD au plus, pour deux instances tombées au "
     "plus, une fois chacune, au sens de ce texte.",
     "GO-2026-11-19-87` : enveloppe de relance, à part de ce plafond, 56 USD au plus, pour deux instances tombées au "
     "plus, une fois chacune, au sens de ce texte, aux mêmes conditions que l'accord de calcul ; l'accord serait caduc "
     "si ce texte mettait la relance sous le plafond commun, ce qu'il ne fait pas."),
]


def bloc(ident, piece, avant, apres):
    return (f"#### Couple {ident} — `{piece}`\n\nAvant :\n\n```text\n{avant}\n```\n\nAprès :\n\n```text\n{apres}\n```\n")


def main():
    sys.path.insert(0, str(RACINE / "src"))
    from controle_ia.prereg import problemes

    print("# Couples de la vérification du candidat au scellement v2 — sortie du contrôle (v1)\n")
    textes = {}
    for piece, debut in ATTENDU.items():
        brut = (RACINE / piece).read_bytes()
        h = hashlib.sha256(brut).hexdigest()
        textes[piece] = brut.decode("utf-8")
        print(f"- `{piece}` : {h[:16]}… ({'attendue' if h.startswith(debut) else 'INATTENDUE'})")
    print(f"- validateur sur le texte tel quel : {problemes(RACINE / T) or 'aucun problème'}\n")
    copie = dict(textes)
    defauts = 0
    for ident, constat, touche, piece, avant, apres in COUPLES:
        n_scelle, n_copie, n_apres = textes[piece].count(avant), copie[piece].count(avant), textes[piece].count(apres)
        bon = n_scelle == 1 and n_copie == 1 and n_apres == 0
        defauts += not bon
        copie[piece] = copie[piece].replace(avant, apres, 1)
        print(f"{ident:5s} ({constat}, {touche}) {Path(piece).name} : « avant » {n_scelle} fois dans la pièce scellée, "
              f"{n_copie} fois au moment d'appliquer ; « après » déjà présent {n_apres} fois{'' if bon else ' — DÉFAUT'}")
    with tempfile.TemporaryDirectory() as d:
        chemin = Path(d) / "copie.md"
        chemin.write_text(copie[T], encoding="utf-8")
        print(f"\nvalidateur du dépôt sur la copie du texte après les couples : {problemes(chemin) or 'aucun problème'}")
    print(f"titre du texte après les couples : {copie[T].splitlines()[0][-40:]!r}")
    print(f"titre du devis après les couples : {copie[DV].splitlines()[0][-40:]!r}")
    print("empreintes attendues des pièces à sceller (candidat v2 et ces couples, appliqués à la lettre dans cet ordre) :")
    print(f"  texte : {hashlib.sha256(copie[T].encode('utf-8')).hexdigest()}")
    print(f"  devis : {hashlib.sha256(copie[DV].encode('utf-8')).hexdigest()}")
    print(f"couples : {len(COUPLES)} ; défauts : {defauts}")
    if "--document" in sys.argv:
        doc = Path(sys.argv[sys.argv.index("--document") + 1]).read_text(encoding="utf-8")
        manquants = [c[0] for c in COUPLES if bloc(c[0], c[3], c[4], c[5]) not in doc]
        print(f"document : couples reproduits à l'octet {len(COUPLES) - len(manquants)} sur {len(COUPLES)} "
              f"{manquants if manquants else ''}")
    if defauts:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
