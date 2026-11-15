"""Brouillon 5 du préenregistrement de l'étape B bis de T0.7 = brouillon 4 (`af612cbc…`, gardé tel quel, R12) + le **seul** couple
a5 (section « Code neuf » : lanceur et amorce de la course en v2, marche `marche_v2`), accepté par la mère le 2026-11-15 (après
R-2917 ; proposé dans `brouillons/T0.7-etape-B-bis-v1/code/corrections-controle-attention-v1.md`, § 1), puis trois couples **de
forme** : titre (« brouillon 4 » → « brouillon 5 »), ligne de statut, tableau du différentiel 4 → 5 en tête (le tableau 3 → 4
reste, dessous).

**Inventaire des noms v1 de la course** (fait par ce programme, écrit dans le tableau) : parmi les fichiers de la course qui ont une
version v2 (`validation_imbriquee`, `marche`, `amorce_bbis`, `lancer_bbis`, `repetition_carte_bbis`, `amorce_repetition_bbis`,
`lancer_repetition_bbis`, `fichiers-fiche-code-bbis`), le brouillon 4 ne cite plus que `scripts/lancer_bbis_v1.sh` (et « son
amorce », sans nom) : un seul couple suffit ; tout autre nom v1 cité (`apprentissage_carte_v1`, `plis_v1`, `adversaires_texte_v1`,
`lecture_v1`, `conjointe_v1`, `conjointe_bbis_v1`, `enumerer_issues_bbis_v1`…) n'a pas de v2 et reste.

**Contrôles** : empreinte du brouillon 4 ; chaque « ancien » présent exactement une fois ; retirer les quatre couples redonne le
brouillon 4 au bit près ; hors du titre, de la ligne de statut, du tableau inséré et de la ligne du couple a5, toutes les lignes
sont égales à celles du brouillon 4 (comparaison ligne à ligne). Le brouillon 4 n'est pas touché ; le brouillon 5 n'est jamais
réécrit (R12). Lancement : `python3 -I -B couples-brouillon5-v1.py <dossier du brouillon>`.
"""
import difflib
import hashlib
import re
import sys
from pathlib import Path

DOSSIER = Path(sys.argv[1]).resolve()
B4 = DOSSIER / "T0.7-etape-B-bis-v1-brouillon4.md"
B5 = DOSSIER / "T0.7-etape-B-bis-v1-brouillon5.md"
EMPREINTE_B4 = "af612cbc02a9dd5781eb1d405f3408bf6ad1bd47103641665c2153a7d0c23676"
CORR = ("`brouillons/T0.7-etape-B-bis-v1/code/corrections-controle-attention-v1.md`, "
        "`45aeddba99a7a710a412ee048b42de589b771e17ea6a929f45ab3e74e40d91e5`")
h = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()          # noqa: E731

b4 = B4.read_text(encoding="utf-8")
assert h(b4) == EMPREINTE_B4, "brouillon 4 autre que celui du compagnon"
assert not B5.exists(), "brouillon 5 déjà écrit (R12)"

# inventaire : noms v1 des fichiers de la course qui ont une v2
AVEC_V2 = ("validation_imbriquee", "marche", "amorce_bbis", "lancer_bbis", "repetition_carte_bbis", "amorce_repetition_bbis",
           "lancer_repetition_bbis", "fichiers-fiche-code-bbis")
cites = sorted({m.group(0) for n in AVEC_V2 for m in re.finditer(rf"(?<![A-Za-z_]){re.escape(n)}[_-]v1\b", b4)})
assert cites == ["lancer_bbis_v1"], f"noms v1 de la course encore cités : {cites}"

A5 = ("a5", "scripts `scripts/lancer_bbis_v1.sh` et son amorce ;",
      "scripts `scripts/lancer_bbis_v2.sh` et son amorce `scripts/amorce_bbis_v2.sh` (marche `marche_v2`, qui appelle "
      "`validation_imbriquee_v2` ; les v1 restent, R12) ;")
TABLEAU = (
    "**Différentiel du brouillon 4 au brouillon 5** (couple a5 accepté par la mère le 2026-11-15, après R-2917 ; proposé au § 1 de "
    f"{CORR} ; `pieces/couples-brouillon5-v1.py` ; aucun autre contenu ne change ; le tableau du brouillon 4 suit, inchangé) :\n\n"
    "| couple | lieu | changement |\n|---|---|---|\n"
    "| a5 | « Code neuf », liste du code neuf | `scripts/lancer_bbis_v1.sh` et son amorce → `scripts/lancer_bbis_v2.sh` et son amorce "
    "`scripts/amorce_bbis_v2.sh` (marche `marche_v2`, qui appelle `validation_imbriquee_v2`) ; seul nom v1 de la course encore "
    "cité qui ait une v2 (inventaire du programme) |\n\n")
FORME = [("titre", "— v1 — brouillon 4\n", "— v1 — brouillon 5\n"),
         ("statut", "- **Statut** : **brouillon 4** = brouillon 3",
          "- **Statut** : **brouillon 5** = brouillon 4 (`af612cbc…`, gardé tel quel, R12) + le couple a5 du tableau en tête ; "
          "**brouillon 4** = brouillon 3")]

texte = b4
for nom, ancien, nouveau in [A5] + FORME:
    n = texte.count(ancien)
    if n != 1:
        raise SystemExit(f"{nom} : « ancien » présent {n} fois")
    texte = texte.replace(ancien, nouveau)
premiere, reste = texte.split("\n\n", 1)
assert premiere.endswith("— v1 — brouillon 5") and reste.startswith("**Différentiel du brouillon 3 au brouillon 4**")
texte = premiere + "\n\n" + TABLEAU + reste

# contrôle 1 : retour au brouillon 4 au bit près
retour = texte.replace(TABLEAU, "", 1)
for _, ancien, nouveau in reversed([A5] + FORME):
    retour = retour.replace(nouveau, ancien, 1)
assert h(retour) == EMPREINTE_B4, "retour au brouillon 4 impossible"
# contrôle 2 : le tableau inséré retiré, toutes les lignes sont celles du brouillon 4 sauf le titre, le statut et la ligne a5
l4, l5 = b4.splitlines(), texte.splitlines()
tab = TABLEAU.rstrip("\n").split("\n")
assert l5[2:2 + len(tab)] == tab and l5[2 + len(tab)] == "", "tableau absent de sa place"
sans_tableau = l5[:2] + l5[3 + len(tab):]
assert len(sans_tableau) == len(l4), "nombre de lignes différent hors du tableau"
changees = [i for i, (a, b) in enumerate(zip(l4, sans_tableau)) if a != b]
assert len(changees) == 3 and changees[0] == 0, changees
assert l4[changees[1]].startswith("- **Statut** : **brouillon 4**") and A5[1] in l4[changees[2]]
assert sans_tableau[changees[2]] == l4[changees[2]].replace(A5[1], A5[2]), "ligne a5 : autre changement que le couple"
ajoutees = tab + [""]
B5.write_text(texte, encoding="utf-8")
print("noms v1 de la course encore cités au brouillon 4 :", ", ".join(cites))
print("lignes changées :", len(changees), "; lignes ajoutées (tableau) :", len(ajoutees))
print("brouillon 5 :", h(texte))
