"""Corrections du brouillon 4 vers le brouillon 5 de l'additif 2 aux sondes du barreau 8.

Rejouable : lit le brouillon 4 (empreinte exigée), applique les corrections de la troisième
vérification (rapport 51005045… : défaut D et deux remarques de forme), écrit le brouillon 5.
Refuse d'écraser. Chaque remplacement exige le nombre d'occurrences attendu.
Usage : python corrections_brouillon4_vers_brouillon5_v1.py <brouillon4.md> <brouillon5.md>
"""
import hashlib
import sys
from pathlib import Path

EMPREINTE_B4 = "0d3f1adc07e09e8cdce838a724569cd3f7db3a5c56008dc7dc1c48b960a5ab7e"
DOSSIER = "docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/"


def morceau(texte: str, ancien: str, neuf: str, fois: int = 1) -> str:
    assert texte.count(ancien) == fois, (ancien[:70], texte.count(ancien))
    return texte.replace(ancien, neuf)


def corriger(t: str) -> str:
    # --- en-tête -----------------------------------------------------------------------
    t = morceau(t, "— v1 — brouillon 4\n", "— v1 — brouillon 5\n")
    # défaut D : le statut ne dit plus rien qui deviendrait faux une fois la vérification inscrite
    t = morceau(t, "**Statut : brouillon 4, non vérifié. Il porte les quatorze constats de la contre-lecture (règle R2) du brouillon 1 et les deux remarques de son complément (brouillon 2), les neuf défauts et la remarque de forme de la vérification du brouillon 2 (brouillon 3), puis les trois défauts et les deux remarques de forme de la vérification du brouillon 3 (brouillon 4). La vérification du brouillon 3 a conclu « à corriger » ; la boucle unique de correction du mandat du rédacteur est épuisée : ce brouillon 4 attend une vérification que la session mère décide, avant tout scellement (clé `SCELLEMENT-ADDITIF-2-SONDES-IIB`).**",
                "**Statut d'avant le scellement : brouillon 5, candidat final. Il porte les quatorze constats de la contre-lecture (règle R2) du brouillon 1 et les deux remarques de son complément (brouillon 2), les neuf défauts et la remarque de forme de la vérification du brouillon 2 (brouillon 3), les trois défauts et les deux remarques de forme de la vérification du brouillon 3 (brouillon 4), puis le défaut et les deux remarques de forme de la vérification du brouillon 4 (brouillon 5). Les vérifications des brouillons 2, 3 et 4 ont chacune conclu « à corriger » ; la vérification de ce brouillon 5, par le même vérificateur, est consignée à l'entrée « Contre-lecture 2 » ; le scellement revient à la session mère (clé `SCELLEMENT-ADDITIF-2-SONDES-IIB`).**")
    t = morceau(t, "*et brouillon 4* (ce texte) : écrits par",
                "*, brouillon 4* (`0d3f1adc07e09e8cdce838a724569cd3f7db3a5c56008dc7dc1c48b960a5ab7e`) *et brouillon 5* (ce texte) : écrits par")
    t = morceau(t, "brouillon 4 écrit le même jour, vers 09:50Z.",
                "brouillon 4 écrit le même jour, vers 09:48Z ; brouillon 5 écrit le même jour, vers 09:55Z.")
    # remarque de forme 1
    t = morceau(t, "- **Ce que les brouillons 2 et 3 changent après le mot de Lazar", "- **Ce que les brouillons 2 à 5 changent après le mot de Lazar")
    t = morceau(t, "rédacteur des brouillons 2 et 3", "rédacteur des brouillons 2 à 5", fois=2)
    t = morceau(t, "| rédacteur des brouillons 2, 3 et 4 (Fable 5.2, session fille, côté des moniteurs) | les deux rapports de la vérification des corrections (brouillons 2 et 3) ;",
                "| rédacteur des brouillons 2 à 5 (Fable 5.2, session fille, côté des moniteurs) | les trois rapports de la vérification des corrections (brouillons 2, 3 et 4) ;")

    # --- défaut D : table des corrections du brouillon 3, puis table neuve -----------------
    t = morceau(t, " **Ces corrections ne sont pas vérifiées.**\n",
                " À l'écriture du brouillon 4, ces corrections n'étaient pas vérifiées ; leur vérification est celle du brouillon 4 (table suivante).\n")
    t = morceau(t, "## Ce que cet additif est, et n'est pas\n",
                "## Corrections de la vérification du brouillon 4 (brouillon 4 → brouillon 5)\n\n"
                "Rapport : `" + DOSSIER + "verification-corrections-additif-2-brouillon4-opus-v1.md` (`51005045c19ccdf717250063d13576e04cd71a2d2a4ba3c40083c38706111a74`), conclusion « à corriger », sur un seul point mineur : les défauts A, B, C et les deux remarques de forme portés ; un défaut mineur (D), deux remarques de forme. Tous corrigés, par le programme `corrections_brouillon4_vers_brouillon5_v1.py` du même dossier (rejouable). La vérification de ces corrections est consignée à l'entrée « Contre-lecture 2 ».\n\n"
                "| défaut | gravité | correction | où |\n|---|---|---|---|\n"
                "| D | mineur | quatre phrases qui seraient devenues fausses dans la version scellée (« non vérifié », « attend une vérification », « ces corrections ne sont pas vérifiées », deux fois) sont écrites au passé daté, ou renvoient à l'entrée « Contre-lecture 2 » | statut ; table des corrections du brouillon 3 ; « Contre-lecture » |\n"
                "| forme 1 | — | « brouillons 2 à 5 » aux trois lieux relevés, et à la ligne du rédacteur de la table des expositions | en-tête ; « Expositions » |\n"
                "| forme 2 | — | le champ AD2-1 dit que l'écart aux bornes (b1) et (b4) relève du champ AD2-3 | AD2-1 |\n\n"
                "## Ce que cet additif est, et n'est pas\n")

    # --- remarque de forme 2 : champ AD2-1 --------------------------------------------------
    t = morceau(t, "trois ajouts, et les raisons corrigées de NL2-1 et NL2-2) : couverts, ou portés à Lazar, avec sa réponse | À REMPLIR |",
                "trois ajouts, et les raisons corrigées de NL2-1 et NL2-2) : couverts, ou portés à Lazar, avec sa réponse ; l'écart aux bornes (b1) et (b4), que nomme aussi le point (iv), ne se dit pas « couvert » ici : il relève du champ AD2-3 et du mot de Lazar que ce champ exige | À REMPLIR |")

    # --- contre-lecture ----------------------------------------------------------------------
    t = morceau(t, "Traitement : table « Corrections de la vérification du brouillon 3 » en tête de ce texte ; ces corrections ne sont pas vérifiées.\n",
                "Traitement : table « Corrections de la vérification du brouillon 3 » en tête de ce texte ; à l'écriture du brouillon 4, ces corrections n'étaient pas vérifiées : leur vérification est l'entrée suivante.\n")
    t = morceau(t, "- **Contre-lecture 2 (finale : vérification du brouillon 4, décidée par la session mère, texte rempli)** : À REMPLIR",
                "- **Vérification des corrections du brouillon 4** — même vérificateur, sur l'accord de la session mère ; faite le 2026-11-24 vers 09:50Z. Brouillon vérifié : même dossier, `lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1-brouillon4.md`, empreinte `0d3f1adc07e09e8cdce838a724569cd3f7db3a5c56008dc7dc1c48b960a5ab7e`. Rapport : même dossier, `verification-corrections-additif-2-brouillon4-opus-v1.md`, empreinte `51005045c19ccdf717250063d13576e04cd71a2d2a4ba3c40083c38706111a74`. Conclusion : « à corriger », sur un seul point mineur (D) ; les défauts A, B, C portés ; rejeu du programme exact à l'octet ; deux remarques de forme. Traitement : table « Corrections de la vérification du brouillon 4 » en tête de ce texte.\n"
                "- **Contre-lecture 2 (finale : vérification du brouillon 5, par le même vérificateur, texte rempli)** : À REMPLIR")
    return t


def main() -> int:
    source, cible = Path(sys.argv[1]), Path(sys.argv[2])
    brut = source.read_bytes()
    assert hashlib.sha256(brut).hexdigest() == EMPREINTE_B4, "le brouillon 4 n'a pas l'empreinte attendue"
    if cible.exists():
        raise SystemExit(f"refus : {cible} existe (règle R12)")
    cible.write_text(corriger(brut.decode("utf-8")), encoding="utf-8")
    print(hashlib.sha256(cible.read_bytes()).hexdigest(), cible)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
