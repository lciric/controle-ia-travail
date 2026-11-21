"""Consigne privée du maître de (ii-b), v1 (conception, section 10, `iib/consigne_v1.py` ; consigne privée, « Règle de lecture »).

- `charger_consigne_iib(chemin, sha_attendue)` : empreinte compagnon vérifiée (R11) puis égale à celle que cite la
  configuration ; **deux** blocs cités (« > ») dans la section « Textes », dans l'ordre : consigne du maître, indication à
  chaque pas ; les lignes d'un bloc jointes par une espace (`premier_test_ia.conditions.blocs_cites`) ; un autre nombre de
  blocs, ou un bloc vide, arrête ; motifs de mention lus dans le premier bloc de code de la section « Motifs de mention
  propres à (ii-b) », compilés insensibles à la casse (aucun motif, ou un motif illisible, arrête).
  Déclaré : la règle de lecture dit qu'aucune autre ligne du fichier n'est citée par « > », mais l'en-tête du brouillon 2
  (ligne 3) en est une ; les blocs ne sont donc lus que dans la section « Textes », comme la règle le demande.
- `environnement_maitre(tache, T, guide, consigne)` : environnement (a) de la condition `maitre_iib`, à la même place que P3
  (`instructions_cachees={0: consigne}`, `indications_privees={(0, t): indication}` pour t = 0 à T − 1).
Le texte de la consigne n'est jamais écrit dans une sortie par ce module.
"""
from __future__ import annotations

import re
from pathlib import Path

from ..environnements.propositions import EnvironnementPropositions
from ..gardes import GardeArret
from ..premier_test_ia.conditions import blocs_cites
from ..scellement import verifier

CONDITION = "maitre_iib"
SECTION_TEXTES = "## Textes"
SECTION_MOTIFS = "## Motifs de mention propres à (ii-b)"


def _section(texte: str, titre: str) -> str:
    lignes = texte.split("\n")
    debuts = [i for i, l in enumerate(lignes) if l.startswith(titre)]
    if len(debuts) != 1:
        raise GardeArret(f"consigne : section « {titre} » trouvée {len(debuts)} fois (une attendue)")
    d = debuts[0] + 1
    f = next((i for i in range(d, len(lignes)) if lignes[i].startswith("## ")), len(lignes))
    return "\n".join(lignes[d:f])


def motifs_de_mention(texte: str) -> list[str]:
    """Motifs du premier bloc de code (« ``` ») de la section des motifs propres à (ii-b), une ligne par motif."""
    s = _section(texte, SECTION_MOTIFS).split("\n")
    ouvertures = [i for i, l in enumerate(s) if l.strip().startswith("```")]
    if len(ouvertures) < 2:
        raise GardeArret("consigne : bloc de code des motifs de mention absent")
    motifs = [l.strip() for l in s[ouvertures[0] + 1:ouvertures[1]] if l.strip()]
    if not motifs:
        raise GardeArret("consigne : aucun motif de mention")
    for m in motifs:
        try:
            re.compile(m, re.I)
        except re.error as e:
            raise GardeArret(f"consigne : motif de mention illisible {m!r} ({e})") from None
    return motifs


def charger_consigne_iib(chemin, sha_attendue: str) -> dict:
    sha = verifier(chemin)
    if sha != sha_attendue:
        raise GardeArret(f"{chemin} : empreinte {sha[:12]} ≠ empreinte citée par la configuration {str(sha_attendue)[:12]} (R11)")
    texte = Path(chemin).read_text(encoding="utf-8")
    blocs = blocs_cites(_section(texte, SECTION_TEXTES))
    if len(blocs) != 2 or any(not b.strip() for b in blocs):
        raise GardeArret(f"{chemin} : deux textes cités non vides attendus dans la section « Textes » (consigne du maître, "
                         f"indication à chaque pas), {len(blocs)} trouvé(s){' dont un vide' if any(not b.strip() for b in blocs) else ''}")
    return {"sha256": sha, "consigne": blocs[0], "indication": blocs[1], "motifs": motifs_de_mention(texte)}


def environnement_maitre(tache, T: int, guide, consigne: dict) -> EnvironnementPropositions:
    """Environnement (a) du maître (N = 1) : consigne à la fin du message système, indication avant « Your action: »."""
    return EnvironnementPropositions(tache, 1, T, guide, instructions_cachees={0: consigne["consigne"]},
                                     indications_privees={(0, t): consigne["indication"] for t in range(T)})
