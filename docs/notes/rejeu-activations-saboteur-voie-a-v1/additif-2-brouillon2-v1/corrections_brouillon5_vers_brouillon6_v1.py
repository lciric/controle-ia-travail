"""Corrections du brouillon 5 vers le brouillon 6 de l'additif 2 aux sondes du barreau 8.

Rejouable : lit le brouillon 5 (empreinte exigée), applique la correction de la quatrième
vérification (rapport 9d460594… : défaut E, une phrase, et l'heure du brouillon 5), écrit le
brouillon 6. Refuse d'écraser. Chaque remplacement exige le nombre d'occurrences attendu.
Usage : python corrections_brouillon5_vers_brouillon6_v1.py <brouillon5.md> <brouillon6.md>
"""
import hashlib
import sys
from pathlib import Path

EMPREINTE_B5 = "65b1af62d7437249b88dbb121c8ae1521a5f908d063b97dd3f82d3758746b2f5"
DOSSIER = "docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/"


def morceau(texte: str, ancien: str, neuf: str, fois: int = 1) -> str:
    assert texte.count(ancien) == fois, (ancien[:70], texte.count(ancien))
    return texte.replace(ancien, neuf)


def corriger(t: str) -> str:
    # --- défaut E : la table détaillée est citée par son chemin et son empreinte -----------
    t = morceau(t, "La table détaillée, avec les motifs, est livrée à part, à côté de ce brouillon.",
                "La table détaillée, avec les motifs, est livrée à part : `" + DOSSIER + "table-constats-corrections-additif-2-brouillon1-vers-brouillon2-v1.md` (`7bd96a0461d310093c08b872542c46a031d40c59e2ce6b58486431d32605d5ce`).")

    # --- en-tête -----------------------------------------------------------------------
    t = morceau(t, "— v1 — brouillon 5\n", "— v1 — brouillon 6\n")
    t = morceau(t, "**Statut d'avant le scellement : brouillon 5, candidat final.", "**Statut d'avant le scellement : brouillon 6, candidat final.")
    t = morceau(t, "puis le défaut et les deux remarques de forme de la vérification du brouillon 4 (brouillon 5). Les vérifications des brouillons 2, 3 et 4 ont chacune conclu « à corriger » ; la vérification de ce brouillon 5, par le même vérificateur, est consignée à l'entrée « Contre-lecture 2 » ;",
                "le défaut et les deux remarques de forme de la vérification du brouillon 4 (brouillon 5), puis le défaut de lettre de la vérification du brouillon 5 (brouillon 6). Les vérifications des brouillons 2, 3, 4 et 5 ont chacune conclu « à corriger » ; la vérification de ce brouillon 6 est consignée à l'entrée « Contre-lecture 2 » ;")
    t = morceau(t, "*et brouillon 5* (ce texte) : écrits par",
                "*, brouillon 5* (`65b1af62d7437249b88dbb121c8ae1521a5f908d063b97dd3f82d3758746b2f5`) *et brouillon 6* (ce texte) : écrits par")
    t = morceau(t, "brouillon 5 écrit le même jour, vers 09:55Z.",
                "brouillon 5 écrit le même jour, vers 09:52Z ; brouillon 6 écrit le même jour, vers 09:56Z.")
    t = morceau(t, "- **Ce que les brouillons 2 à 5 changent après le mot de Lazar", "- **Ce que les brouillons 2 à 6 changent après le mot de Lazar")
    t = morceau(t, "rédacteur des brouillons 2 à 5", "rédacteur des brouillons 2 à 6", fois=3)
    t = morceau(t, "les trois rapports de la vérification des corrections (brouillons 2, 3 et 4)",
                "les quatre rapports de la vérification des corrections (brouillons 2, 3, 4 et 5)")

    # --- table des corrections de la quatrième vérification --------------------------------
    t = morceau(t, "## Ce que cet additif est, et n'est pas\n",
                "## Corrections de la vérification du brouillon 5 (brouillon 5 → brouillon 6)\n\n"
                "Rapport : `" + DOSSIER + "verification-corrections-additif-2-brouillon5-opus-v1.md` (`9d460594e66a92fbc670a642080d62932696f0c78e63991318ef0147a067c070`), conclusion « à corriger », sur un seul point mineur de lettre : le défaut D et les deux remarques de forme portés ; un défaut mineur (E) ; une remarque sur une heure. Corrigés par le programme `corrections_brouillon5_vers_brouillon6_v1.py` du même dossier (rejouable). La vérification de ces corrections est consignée à l'entrée « Contre-lecture 2 ».\n\n"
                "| défaut | gravité | correction | où |\n|---|---|---|---|\n"
                "| E | mineur | « à côté de ce brouillon », qui serait devenu faux dans la version scellée, est remplacé par le chemin et l'empreinte de la table détaillée | « Corrections de la contre-lecture R2 » |\n"
                "| remarque | — | heure du brouillon 5 : « vers 09:52Z » | en-tête |\n\n"
                "## Ce que cet additif est, et n'est pas\n")

    # --- contre-lecture ----------------------------------------------------------------------
    t = morceau(t, "- **Contre-lecture 2 (finale : vérification du brouillon 5, par le même vérificateur, texte rempli)** : À REMPLIR",
                "- **Vérification des corrections du brouillon 5** — même vérificateur ; faite le 2026-11-24 vers 09:53Z. Brouillon vérifié : même dossier, `lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1-brouillon5.md`, empreinte `65b1af62d7437249b88dbb121c8ae1521a5f908d063b97dd3f82d3758746b2f5`. Rapport : même dossier, `verification-corrections-additif-2-brouillon5-opus-v1.md`, empreinte `9d460594e66a92fbc670a642080d62932696f0c78e63991318ef0147a067c070`. Conclusion : « à corriger », sur un seul point mineur de lettre (E) ; le défaut D porté ; rejeu du programme exact à l'octet ; tout le reste conforme. Traitement : table « Corrections de la vérification du brouillon 5 » en tête de ce texte.\n"
                "- **Contre-lecture 2 (finale : vérification du brouillon 6, texte rempli)** : À REMPLIR")
    return t


def main() -> int:
    source, cible = Path(sys.argv[1]), Path(sys.argv[2])
    brut = source.read_bytes()
    assert hashlib.sha256(brut).hexdigest() == EMPREINTE_B5, "le brouillon 5 n'a pas l'empreinte attendue"
    if cible.exists():
        raise SystemExit(f"refus : {cible} existe (règle R12)")
    cible.write_text(corriger(brut.decode("utf-8")), encoding="utf-8")
    print(hashlib.sha256(cible.read_bytes()).hexdigest(), cible)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
