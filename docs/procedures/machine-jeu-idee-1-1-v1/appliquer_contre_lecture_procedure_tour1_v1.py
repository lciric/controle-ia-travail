#!/usr/bin/env python3
"""Applique à procedure-machine-jeu-idee-1-1-v1.md les corrections de la contre-lecture du tour 1 qui portent sur elle.

Usage : python3 -I appliquer_contre_lecture_procedure_tour1_v1.py SOURCE CIBLE HEURE_UTC
- SOURCE : la procédure v1, dont l'empreinte doit être EMPREINTE_SOURCE ;
- CIBLE : la procédure v2, fichier neuf (jamais écrasé, R12) ;
- HEURE_UTC : heure lue par `date -u +%FT%TZ` au moment du scellement.
Chaque « ancien » doit figurer exactement une fois dans le texte de départ et encore une fois au moment de son couple.
Les couples 1, 2, 5, 11, 16, 17 et la réécriture du rapport portent sur d'autres pièces : non appliqués ici.
"""
import hashlib
import re
import sys

EMPREINTE_SOURCE = "0d674c39dea0b4e264b59c3ff235903efe488c36ff8cd8b410166aa2bd4e04bc"
EMPREINTE_RAPPORT = "09d345be856924f51eeadbeefa52003626a3004ddd79c7ba5cd471fb39ec10b3"

SECTION_6 = r"""

## 6. Contre-lecture

- **Rapport** : `contre-lecture-machine-jeu-idee-1-1-tour1-v1.md` (même dossier), empreinte
  `09d345be856924f51eeadbeefa52003626a3004ddd79c7ba5cd471fb39ec10b3`, lecteur neuf (R2) ; verdict `corrections` (trois
  majeures, sept mineures, quatre remarques facultatives).
- **Cette version** : v2, écrite par un rédacteur neuf au moyen du programme de couples
  `appliquer_contre_lecture_procedure_tour1_v1.py` (même dossier), depuis la v1 `0d674c39dea0b4e264b59c3ff235903efe488c36ff8cd8b410166aa2bd4e04bc`.
  Seuls les couples qui portent sur cette pièce y sont appliqués ; ceux de l'amorce, du devis et du rapport attendent les
  versions suivantes de ces pièces (fichiers neufs, par leur auteur).
- **Réponse point par point** :
  - **M1** (poussée des sorties qui échoue) : couples 3 (§ 1, pas 7) et 4 (geste 13) appliqués. Couples 1 et 2 (amorce) et
    les deux cas de répétition demandés : hors de cette pièce, non appliqués ici. **Dépendance** : le pas 7 et le geste 13 de
    cette v2 décrivent la reprise de l'amorce v2 (pause de 5 × `PAUSE` = 300 s, jusqu'à `MARGE_TERM` = 1 200 s avant
    l'échéance : constantes de l'amorce v1, cohérentes avec « toutes les 5 minutes » et « 20 minutes ») ; l'amorce v1 ne la fait
    pas. Cette v2 ne part donc pas au feu avec l'amorce v1 : il faut l'amorce v2, sa répétition (les deux cas exigés) et une
    liste des pièces (en tête de la procédure) qui la nomme, dans la version suivante de cette procédure.
  - **M2** (échéance de la ligne de GO) : couple 6 appliqué (§ 2, point 4). Couple 5 (devis) hors de cette pièce : le
    « devis § 1 » que cite le texte neuf vaut pour le devis v2 qui portera la ligne d'échéance ; le devis v1 ne l'a pas.
  - **M3** (préalables périmés) : couples 7, 8, 9 et 10 appliqués (§ 2, points 1, 2 et 4). Faits revus à {HEURE_REVUE}
    (`date -u`), en lecture seule : R-3016 et R-3017 présents à `registres/decisions.md` ; GO-2026-11-16-10 présent à
    `registres/go.md` ; à `HEAD`, compagnon d'une ligne `a692d50c…` de l'addendum de relance ; `14a0dfc5…` ancêtre de la
    référence locale `origin/main`, `e395dd47…`. Le « 21:3xZ » du couple 10 est gardé tel que le rapport l'écrit. Couple 11
    (devis) et réécriture du rapport : hors de cette pièce.
  - **m1** : couple 12 appliqué (geste 5). **m2** : couple 13 appliqué (geste 13). **m3** : couple 14 appliqué (geste 11).
    **m4** : couple 15 appliqué (§ 5). **m7** : couple 18 appliqué (en tête).
  - **m5, m6** (couples 16 et 17) : devis, hors de cette pièce, non appliqués ici.
  - **F1 à F4** : facultatives, non appliquées (seules les corrections exigées le sont). F2 (geste 8) et F4 (geste 9) portent
    sur cette pièce : laissées à l'auteur et à la mère.
  - **P1 à P6** : points pour la mère, hors du texte de la procédure ; rien n'y change ici.
- **Rien d'autre ne change** par rapport à la v1 : en tête (titre, statut, version), les couples ci-dessus et cette section."""

COUPLES = [
    ("en-tête, titre",
     "# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v1",
     "# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v2"),
    ("couple 18 (m7)",
     "**Statut** : écrite et répétée hors ligne, **non contre-lue**",
     "**Statut** : écrite et répétée hors ligne, contre-lue au tour 1 (`contre-lecture-machine-jeu-idee-1-1-tour1-v1.md`), corrections de ce tour en v2"),
    ("en-tête, version",
     "; aucune machine, aucun appel au loueur, aucune dépense.\n\n## 1. Ce que fait la machine",
     "; aucune machine, aucun appel au loueur, aucune dépense.\n"
     "- **Version** : v2, scellée à {HEURE} (`date -u`) ; suit la v1 (`0d674c39…`) ; changements : corrections de la\n"
     "  contre-lecture du tour 1 (§ 6).\n\n## 1. Ce que fait la machine"),
    ("couple 3 (M1)",
     "poussée par lots (manifeste, puis tranches par 400 fichiers) ; un chemin hors des",
     "poussée par lots (manifeste, puis tranches par 400 fichiers), reprise toutes les 5 minutes jusqu'à 20 minutes avant l'échéance si une poussée échoue, la machine restant vivante (aucun « stopped » tant que les sorties ne sont pas poussées) ; un chemin hors des"),
    ("couple 10 (M3)",
     "1. L'addendum de relance est scellé sous son nom final `prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-relance-v1.md`",
     "1. L'addendum de relance est scellé sous son nom final `prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-relance-v1.md`"
     " (déjà fait : R-3017, empreinte `a692d50c07c1b4b7ef07883ac91124eab4798cab7a579e14235484ea4d2319cf`, commit `14a0dfc5962aad5987d6c88e03e72b5f6d92f150`, ancêtre de la tête de `main` à 21:3xZ ; à relire au moment de remettre la suite, `COMMIT` pouvant être la tête de `main` du moment)"),
    ("couple 7 (M3)",
     "La mère dit au registre si GO-2026-11-16-09",
     "Le mot de Lazar sur D7 est inscrit : GO-2026-11-16-10 (R-3016, 2026-11-16T20:47:50Z) ; GO-2026-11-16-09 ne sert qu'à l'option (a)"),
    ("couple 8 (M3)",
     "(« option (a) … machine de calcul louée ») est ce mot ; sinon, nœud de Lazar avant tout.",
     "(« option (a) … machine de calcul louée ») ; plus aucune question de la mère sur D7 ; le feu cite GO-2026-11-16-10 en toutes lettres."),
    ("couple 9 (M3)",
     "citant GO-2026-11-16-09 : périmètre",
     "citant GO-2026-11-16-09 et GO-2026-11-16-10 : périmètre"),
    ("couple 6 (M2)",
     "plafond écrit `3.5 USD` (point décimal ; la garde de dépense le lit), échéance. Proposition au devis.",
     "plafond écrit `3.5 USD` (point décimal ; la garde de dépense le lit), échéance 2026-11-22 au plus tôt (devis § 1 : la garde de dépense relit la ligne à chaque appel ; un code 2 de date au geste 12 est un nœud de la mère, jamais un ordre de destruction)."),
    ("couple 12 (m1)",
     "\"$D/commande-imprimee.txt\"; echo \"code $?\"; wc -lc \"$D/commande-imprimee.txt\"` → `code 0`, **2** lignes, ≈ 12 100 octets.",
     "\"$D/commande-imprimee.txt\"; echo \"code $?\"; wc -lc \"$D/commande-imprimee.txt\"; head -n 1 \"$D/commande-imprimee.txt\" | cut -c1-300` → `code 0`, **2** lignes, ≈ 12 100 octets, puis l'en-tête `JEU11 COMMANDE (…)` ; un refus s'y lit (`JEU11 REFUS : …`, première ligne seule, jamais le base64)."),
    ("couple 14 (m3)",
     "11. **Surveillance** : la première poussée",
     "11. **Surveillance** (par la mère, ou par un opérateur que le feu nomme et dont la tâche dure aussi longtemps que le jeu ; aucun rappel seul n'y suffit) : la première poussée"),
    ("couple 4 (M1)",
     "13. **Fin** : le journal porte « FIN » (code 0) ou « ARRET » (code 2 ou 4),",
     "13. **Fin** : le journal porte « FIN » (code 0) ou « ARRET » (code 2 ou 4 ; sur « RESERVE : poussée des sorties impossible », ne **rien détruire** : nœud de la mère, qui décide de la copie depuis la machine vivante avant l'échéance),"),
    ("couple 13 (m2)",
     "refs/remotes/origin/$BR runs/<run> diag/organisme-idees-juge-v1/<run>` vers le dépôt, puis chaque compagnon vérifié",
     "refs/remotes/origin/$BR runs/<run> diag/organisme-idees-juge-v1/<run> | tar -x -C $R` (après `git -C $R fetch origin +refs/heads/$BR:refs/remotes/origin/$BR` ; `<run>` est le nom donné par la ligne « FIN : … run … » du journal ; refuser si l'un des deux dossiers existe déjà dans `$R`), puis chaque compagnon vérifié"),
    ("couple 15 (m4)",
     "- Elle ne lit aucun résultat ; elle ne compare pas le run neuf au run invalide (interdit, addendum de relance § 3).",
     "- Elle ne lit aucun résultat ; elle ne compare pas le run neuf au run invalide (interdit, addendum de relance § 3).\n"
     "- Elle ne se passe pas du réseau pendant le jeu : la machine pousse chaque heure `etat.txt` et le journal (comptes et dates de fichiers, jamais un contenu) vers la branche de sortie, hors du processus du jeu dont la garde réseau tient ; ces poussées et celle des sorties à la fin sont déclarées comme part de l'écart D7 (texte scellé l. 629), que le feu cite en toutes lettres."),
    ("section 6 (contre-lecture)",
     "  garde les versions, `lscpu` et `numpy.show_runtime()` dans les traces, pour la dire.",
     "  garde les versions, `lscpu` et `numpy.show_runtime()` dans les traces, pour la dire." + SECTION_6),
]


def main() -> int:
    if len(sys.argv) != 4:
        print("REFUS : usage SOURCE CIBLE HEURE_UTC")
        return 2
    source, cible, heure = sys.argv[1:]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", heure):
        print("REFUS : heure illisible (date -u +%FT%TZ attendu)")
        return 2
    brut = open(source, "rb").read()
    e = hashlib.sha256(brut).hexdigest()
    if e != EMPREINTE_SOURCE:
        print(f"REFUS : empreinte de la source {e} ≠ {EMPREINTE_SOURCE}")
        return 2
    texte = brut.decode("utf-8")
    for nom, ancien, _ in COUPLES:
        n = texte.count(ancien)
        if n != 1:
            print(f"REFUS : {nom} : « ancien » trouvé {n} fois dans la source (1 exigée)")
            return 2
    heure_hm = heure[11:16] + "Z"
    for nom, ancien, nouveau in COUPLES:
        n = texte.count(ancien)
        if n != 1:
            print(f"REFUS : {nom} : « ancien » trouvé {n} fois au moment de son couple (1 exigée)")
            return 2
        nouveau = nouveau.replace("{HEURE}", heure).replace("{HEURE_REVUE}", heure_hm)
        texte = texte.replace(ancien, nouveau, 1)
        print(f"appliqué : {nom}")
    if "{HEURE" in texte:
        print("REFUS : gabarit d'heure resté dans le texte")
        return 2
    try:
        with open(cible, "x", encoding="utf-8") as f:
            f.write(texte)
    except FileExistsError:
        print(f"REFUS : {cible} existe déjà (R12, jamais écrasé)")
        return 2
    print(f"écrit : {cible} ({len(COUPLES)} couples) ; sha256 {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
