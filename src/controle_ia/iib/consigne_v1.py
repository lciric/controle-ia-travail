"""Consigne privée du maître de (ii-b) (conception 2.1 ; règle de lecture écrite dans la consigne scellée).

- Deux blocs de lignes citées (« > ») de la section « ## Textes », dans l'ordre : consigne du maître, indication à chaque pas ; un autre nombre de
  blocs, ou un bloc vide, arrête le run. Empreinte vérifiée contre le compagnon `.sha256` et contre l'empreinte citée par la
  configuration (R11). Les textes ne sont jamais écrits dans le code.
- Motifs de mention propres à (ii-b) : lignes du premier bloc de code qui suit le titre « ## Motifs de mention » ; au
  moins un motif ; chacun compilé (insensible à la casse). Aucun motif n'est ajouté par le code.
- Place : identique à P3 (`premier_test_ia.conditions.environnement`) : la consigne à la fin du message système
  (`instructions_cachees={0: …}`), l'indication juste avant « Your action: » à chaque pas (`indications_privees`).
"""
from __future__ import annotations

import re
from pathlib import Path

from ..environnements.propositions import EnvironnementPropositions
from ..gardes import GardeArret
from ..premier_test_ia.conditions import blocs_cites
from ..scellement import verifier

TITRE_MOTIFS = "## Motifs de mention"
TITRE_TEXTES = "## Textes"
CONDITION_MAITRE = "maitre_iib"


def motifs_du_texte(texte: str) -> list[str]:
    lignes = texte.split("\n")
    debut = next((k for k, l in enumerate(lignes) if l.startswith(TITRE_MOTIFS)), None)
    if debut is None:
        raise GardeArret(f"consigne de (ii-b) : titre « {TITRE_MOTIFS} » absent")
    ouvre = next((k for k in range(debut + 1, len(lignes)) if lignes[k].strip().startswith("```")), None)
    if ouvre is None:
        raise GardeArret("consigne de (ii-b) : bloc de code des motifs absent")
    ferme = next((k for k in range(ouvre + 1, len(lignes)) if lignes[k].strip().startswith("```")), None)
    if ferme is None:
        raise GardeArret("consigne de (ii-b) : bloc de code des motifs non fermé")
    motifs = [l.strip() for l in lignes[ouvre + 1:ferme] if l.strip()]
    if not motifs:
        raise GardeArret("consigne de (ii-b) : aucun motif de mention")
    for m in motifs:
        try:
            re.compile(m, re.I)
        except re.error as e:
            raise GardeArret(f"consigne de (ii-b) : motif {m!r} illisible ({e})") from None
    return motifs


def section_textes(texte: str) -> str:
    """Section « ## Textes » seule (règle de lecture de la consigne : « les deux blocs […] de la section Textes ») ; le
    brouillon 2 porte aussi une citation « > » d'avertissement en tête de fichier, hors de cette section (relevé par le
    développeur : sa règle dit à tort qu'aucune autre ligne n'est citée)."""
    lignes = texte.split("\n")
    debut = [k for k, l in enumerate(lignes) if l.strip() == TITRE_TEXTES]
    if len(debut) != 1:
        raise GardeArret(f"consigne de (ii-b) : un seul titre « {TITRE_TEXTES} » attendu, {len(debut)} trouvés")
    fin = next((k for k in range(debut[0] + 1, len(lignes)) if lignes[k].startswith("## ")), len(lignes))
    return "\n".join(lignes[debut[0] + 1:fin])


def charger_consigne_iib(chemin, sha_attendue: str | None) -> dict:
    """Consigne, indication, motifs et empreinte. `sha_attendue` None n'est permis qu'en mode jouet (l'appelant le vérifie)."""
    sha = verifier(chemin)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"{chemin} : empreinte {sha[:12]} ≠ empreinte citée {str(sha_attendue)[:12]} (R11)")
    texte = Path(chemin).read_text(encoding="utf-8")
    blocs = blocs_cites(section_textes(texte))
    if len(blocs) != 2 or any(not b.strip() for b in blocs):
        raise GardeArret(f"{chemin} : deux textes cités attendus (consigne du maître, indication), {len(blocs)} trouvés "
                         "ou un bloc vide")
    return {"sha256": sha, "consigne": blocs[0], "indication": blocs[1], "motifs": motifs_du_texte(texte)}


def environnement_maitre(tache, T: int, guide: str | None, consigne: dict) -> EnvironnementPropositions:
    """Environnement (a) du maître (N = 1) : même place que les conditions instruites de P3."""
    return EnvironnementPropositions(tache, 1, T, guide, instructions_cachees={0: consigne["consigne"]},
                                     indications_privees={(0, t): consigne["indication"] for t in range(T)})


def compiler_motifs(motifs: list[str]) -> list[tuple[str, re.Pattern]]:
    return [(m, re.compile(m, re.I)) for m in motifs]
