"""Brouillon 6 du préenregistrement de l'étape B bis de T0.7 = brouillon 5 (`99d88954…`, gardé tel quel, R12) + les couples des
décisions de la mère R-2919 sur la contre-lecture du brouillon 5 et du code v2
(`brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-brouillon5-et-code-v2-v1.md`, `93b0724d…`) : M2 voie (b) (aucune issue
« sans objet » ; sonde de contrôle en échec : arrêt ; couple tiré parmi les sondes finales finies), M1 (nom `lecture_v2`), m3 et
m8 (règle de lecture de la répétition, écrite avant la passe), m5 (variante (r1) dite), m6 (« piles du processeur »), m7
(empreinte du second rapport dans le corps), noms v3 de la course ; puis trois couples **de forme** : titre (« brouillon 5 » →
« brouillon 6 »), ligne de statut, tableau du différentiel 5 → 6 en tête (les tableaux 4 → 5 et 3 → 4 restent, dessous).

**Contrôles** : empreinte du brouillon 5 ; chaque « ancien » présent exactement une fois ; retirer tous les couples redonne le
brouillon 5 au bit près ; hors du tableau inséré, seules diffèrent du brouillon 5 les lignes que touchent les couples (titre,
statut et les lignes des couples), et chacune est la ligne du brouillon 5 à laquelle on applique ses couples, rien d'autre. Le
brouillon 5 n'est pas touché ; le brouillon 6 n'est jamais réécrit (R12). Lancement :
`python3 -I -B couples-brouillon6-v1.py <dossier du brouillon>`.
"""
import hashlib
import sys
from pathlib import Path

DOSSIER = Path(sys.argv[1]).resolve()
B5 = DOSSIER / "T0.7-etape-B-bis-v1-brouillon5.md"
B6 = DOSSIER / "T0.7-etape-B-bis-v1-brouillon6.md"
EMPREINTE_B5 = "99d88954369f0d3acfcaa448d517783bdbd397aaef872131a8051d2b7a9456e8"
CL = ("`brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-brouillon5-et-code-v2-v1.md`, "
      "`93b0724dd41b6c0bbfd2ace1ab47475bb3c0af86436361b0d184e5020c29af4e`")
STAB = "`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`"
h = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()          # noqa: E731

b5 = B5.read_text(encoding="utf-8")
assert h(b5) == EMPREINTE_B5, "brouillon 5 autre que celui du compagnon"
assert not B6.exists(), "brouillon 6 déjà écrit (R12)"

COUPLES = [
    ("c1", "m5", "« Plan d'analyse », point 5 (contrôle à la marche)",
     "**dans les deux familles** : la linéaire à 300 époques, l'attention à **3 époques**",
     "**dans les deux familles** (sous la variante (r1) : la linéaire seule) : la linéaire à 300 époques, l'attention à "
     "**3 époques**"),
    ("c2", "M2 (voie (b))", "« Plan d'analyse », point 5",
     "doit être égale à la première au bit près (déterminisme), sinon arrêt. Raison, écrite avant toute lecture :",
     "doit être égale à la première au bit près (déterminisme), sinon arrêt. **Aucune issue « sans objet »** : une sonde apprise "
     "pour le contrôle en échec (perte ou paramètres non finis), à 3 ou à 300 époques, déterminisme compris, arrête (erreur de "
     "chaîne) ; le couple est tiré **à la fin de l'apprentissage, parmi les couples dont la sonde finale est finie**, dans le même "
     "ordre trié et avec la même graine (`bbis/egalite-carte`) ; aucun : arrêt (erreur de chaîne). Raison, écrite avant toute "
     "lecture :"),
    ("c3", "m6", "« Plan d'analyse », point 5",
     "à 3 époques, l'écart entre deux piles reste de", "à 3 époques, l'écart entre deux piles du processeur reste de"),
    ("c4", "m7, m3 et m8", "« Plan d'analyse », point 5",
     f"{STAB}). Les aires de validation interne",
     f"{STAB}, `dd67802d…`). **Répétition sur carte avant la course** (données synthétiques seulement ; mot de Lazar R-2802), "
     "**règle de lecture écrite avant la passe** : la passe ne compte que si chaque famille porte un écart numérique ≤ 10⁻⁴ "
     "(linéaire à 300 époques, attention à 3 époques) et l'égalité au bit près (déterminisme des deux familles et de l'attention du "
     "contrôle, lot reconstruit égal au premier) ; si l'écart de chaque famille est ≤ 10⁻⁵, la course part sans nœud ; entre 10⁻⁵ "
     "et 10⁻⁴, nœud écrit à la mère avant la course. Les aires de validation interne"),
    ("c5", "M2 (voie (b))", "« Liste d'arrêt » (contrôle carte-processeur)",
     "ou sonde « attention » du couple non déterministe sur la carte : arrêt (erreur de chaîne) ;",
     "sonde « attention » du couple non déterministe sur la carte, sonde apprise pour le contrôle en échec (perte ou paramètres non "
     "finis, à 3 ou à 300 époques), ou aucun couple à sonde finale finie : arrêt (erreur de chaîne) ;"),
    ("c6", "m6, m7", "« Critères de lecture gelés », qualifications (R-PILE)",
     f"entre quatre piles de calcul, aires d'une sonde « attention » qui n'apprend rien (aire 0,46) d'étendue 0,0074, et d'étendue au "
     f"plus 7,8·10⁻⁵ pour des sondes qui apprennent un signal (aires 0,56 à 0,98) ; {STAB}), audit R4",
     f"entre quatre piles de calcul du processeur (aucune carte), aires d'une sonde « attention » qui n'apprend rien (aire 0,46) "
     f"d'étendue 0,0074, et d'étendue au plus 7,8·10⁻⁵ pour des sondes qui apprennent un signal (aires 0,56 à 0,98) ; {STAB}, "
     "`dd67802d…`), audit R4"),
    ("c7", "M2 (code)", "« Code neuf » (module du contrôle)",
     "`validation_imbriquee_v2` (plis, grille, sélection, sonde finale, nul de réétiquetage, ENC, garde de débit ; contrôle "
     "carte-processeur aux deux horizons du point 5 et déterminisme de la sonde « attention » du couple ; la v1 reste, R12)",
     "`validation_imbriquee_v3` (plis, grille, sélection, sonde finale, nul de réétiquetage, ENC, garde de débit ; contrôle "
     "carte-processeur aux deux horizons du point 5, sans issue « sans objet », sur un couple tiré parmi les sondes finales finies, "
     "et déterminisme de la sonde « attention » du couple ; les v1 et v2 restent, R12)"),
    ("c8", "M1", "« Code neuf » (lecture)",
     "`lecture_v1` (gardes, états, issue, phrases, réserves, audit R4 ;",
     "`lecture_v2` (la v1 reste, R12 ; gardes, états, issue, phrases, réserves dont R-PILE, point (7) de la section D, lecture du "
     "champ du contrôle carte-processeur, qui arrête la lecture s'il est « sans objet », absent ou non numérique ; audit R4 ;"),
    ("c9", "noms v3 de la course", "« Code neuf » (lanceur, amorce, marche)",
     "scripts `scripts/lancer_bbis_v2.sh` et son amorce `scripts/amorce_bbis_v2.sh` (marche `marche_v2`, qui appelle "
     "`validation_imbriquee_v2` ; les v1 restent, R12)",
     "scripts `scripts/lancer_bbis_v3.sh` et son amorce `scripts/amorce_bbis_v3.sh` (marche `marche_v3`, qui appelle "
     "`validation_imbriquee_v3` ; les v1 et v2 restent, R12)"),
    ("c10", "M2, M1, m4", "« Code neuf », épreuves",
     "égalité carte-processeur (linéaire à 300 époques, attention à 3 époques ; artefacts : autre graine, poids altérés de 1 % ; "
     "déterminisme : cas sain et artefact)",
     "égalité carte-processeur (linéaire à 300 époques, attention à 3 époques ; artefacts : autre graine, poids altérés de 1 % ; "
     "déterminisme : cas sain et artefact ; sonde de contrôle en échec à 3 ou à 300 époques : arrêt ; couple tiré parmi les sondes "
     "finales finies : même couple et mêmes actions que la v1 si toutes sont finies, autre tirage si une ne l'est pas, aucun : "
     "arrêt ; R-PILE et champ du contrôle à la lecture : cas sain et artefacts)"),
]
FORME = [("titre", "— v1 — brouillon 5\n", "— v1 — brouillon 6\n"),
         ("statut", "- **Statut** : **brouillon 5** = brouillon 4",
          "- **Statut** : **brouillon 6** = brouillon 5 (`99d88954…`, gardé tel quel, R12) + les couples c1 à c10 du tableau en tête "
          "(R-2919) ; **brouillon 5** = brouillon 4")]
lignes_tableau = "\n".join(f"| {c} | {decision} | {lieu} |" for c, decision, lieu, _, _ in COUPLES)
TABLEAU = (
    "**Différentiel du brouillon 5 au brouillon 6** (décisions de la mère **R-2919** sur la contre-lecture du brouillon 5 et du code "
    f"v2, {CL} : majeurs M1 et M2 (voie (b)), mineurs m3 à m8 ; `pieces/couples-brouillon6-v1.py` ; aucun autre contenu ne change ; "
    "les tableaux du brouillon 5 suivent, inchangés) :\n\n| couple | décision | lieu |\n|---|---|---|\n" + lignes_tableau + "\n\n")

texte = b5
for c, _, _, ancien, nouveau in COUPLES:
    n = texte.count(ancien)
    if n != 1:
        raise SystemExit(f"{c} : « ancien » présent {n} fois")
    texte = texte.replace(ancien, nouveau)
for nom, ancien, nouveau in FORME:
    n = texte.count(ancien)
    if n != 1:
        raise SystemExit(f"{nom} : « ancien » présent {n} fois")
    texte = texte.replace(ancien, nouveau)
premiere, reste = texte.split("\n\n", 1)
assert premiere.endswith("— v1 — brouillon 6") and reste.startswith("**Différentiel du brouillon 4 au brouillon 5**")
texte = premiere + "\n\n" + TABLEAU + reste

# contrôle 1 : retour au brouillon 5 au bit près
retour = texte.replace(TABLEAU, "", 1)
for _, ancien, nouveau in reversed(FORME):
    retour = retour.replace(nouveau, ancien, 1)
for _, _, _, ancien, nouveau in reversed(COUPLES):
    retour = retour.replace(nouveau, ancien, 1)
assert h(retour) == EMPREINTE_B5, "retour au brouillon 5 impossible"
# contrôle 2 : ligne à ligne, hors du tableau inséré
l5, l6 = b5.splitlines(), texte.splitlines()
tab = TABLEAU.rstrip("\n").split("\n")
assert l6[2:2 + len(tab)] == tab and l6[2 + len(tab)] == "", "tableau absent de sa place"
sans = l6[:2] + l6[3 + len(tab):]
assert len(sans) == len(l5), "nombre de lignes différent hors du tableau"
tous = [(a, n) for _, _, _, a, n in COUPLES] + [(a.rstrip("\n"), n.rstrip("\n")) for _, a, n in FORME]
changees = 0
for a, b in zip(l5, sans):
    if a == b:
        continue
    changees += 1
    attendu = a
    for ancien, nouveau in tous:
        if ancien in attendu:
            attendu = attendu.replace(ancien, nouveau)
    assert attendu == b, f"ligne changée autrement que par ses couples : {a[:80]!r}"
B6.write_text(texte, encoding="utf-8")
print("couples appliqués :", ", ".join(c[0] for c in COUPLES), "; forme : titre, statut, tableau")
print("lignes changées hors du tableau :", changees, "; lignes ajoutées (tableau) :", len(tab) + 1)
print("brouillon 6 :", h(texte))
