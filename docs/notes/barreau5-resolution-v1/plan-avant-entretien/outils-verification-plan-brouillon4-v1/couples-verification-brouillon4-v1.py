#!/usr/bin/env python3
"""Vérification du brouillon 4 (barreau 5, plan « sabotage ou empreinte ») : couples exacts « avant → après », v1.

Écrit par le vérificateur (Claude Opus 5.5) le 20 novembre 2026. Ne lit que des textes du dépôt ; n'écrit rien (sortie
standard). Pour chaque couple : l'« avant » doit se trouver exactement une fois dans la pièce visée, telle qu'elle est
scellée, et encore une fois au moment où il s'applique, dans l'ordre de la liste, à une copie en mémoire ; l'« après » ne
doit pas s'y trouver déjà. Le validateur du dépôt (`controle_ia.prereg.problemes`) est joué sur la copie du texte.
Avec `--document CHEMIN`, le programme vérifie de plus que chaque couple est reproduit à l'octet dans ce document.
Les taux cités dans les « après » sont des taux de mondes inventés, lus dans `sortie-simulation-verification-brouillon4-v1.txt`
et `sortie-controle-precision-verification-brouillon4-v1.txt` (même dossier).
"""
from __future__ import annotations

import hashlib
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
PLAN = ICI.parent
RACINE = PLAN.parents[3]
T = "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md"
DV = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md"
FI = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-v4-lazar-v1.md"
ATTENDU = {T: "dbe66dc9", DV: "084cd547", FI: "a88a3a12"}

# (identifiant, constat, touche, pièce, avant, après)
COUPLES = [
    # ---------------------------------------------------------------- W-M1 : l'étalon de la poussée
    ("W-M1a", "W-M1", "lecture", T,
     "(d) la divergence propre du saboteur est indépendante de celles des deux membres édités, hors ce que la famille "
     "partage : c'est ce que suppose l'étalon, et ce plan ne le vérifie pas.",
     "(d) la divergence propre du saboteur est indépendante de celles des deux membres édités, hors ce que la famille "
     "partage, et rien de ce que les deux membres édités partagent sans lui (trace de l'édition commune aux deux sens, "
     "divergence née de l'édition) ne se projette sur son déplacement moyen : c'est ce que suppose l'étalon, et ce plan "
     "ne le vérifie pas. Tout repose sur elle quand la force porte sur la seule part propre à la famille, que la poussée "
     "le long de la direction commune (E2b) ne corrige pas ; elle y est fragile : en mondes inventés, sans aucun "
     "sabotage, une corrélation de 0,02 entre les divergences propres du saboteur et du jumeau fait sortir le mot dans "
     "1,30 et 2,05 % des mondes, une corrélation de 0,05 dans 4,10 et 13,83 %, de 0,1 dans 20,6 et 75,3 %, de 0,3 à 0,5 "
     "dans 84 à 100 % ; une trace commune de 0,3 tournée à 45° vers la direction commune, dans 43,8 et 91,6 % "
     "(vérification du brouillon 4, mondes N01 à N05, N17, N18, P1 et P2). Une corrélation du saboteur avec le "
     "sur-saboteur pousse l'égalisation trop loin : le mot se perd, il ne sort pas à tort."),
    ("W-M1b", "W-M1", "lecture", T,
     "Le saboteur n'est pas édité : ni une trace de l'édition, ni une part de divergence commune aux deux membres édités "
     "aux mêmes jetons n'entre dans l'un ou l'autre produit.",
     "Le saboteur n'est pas édité : une trace de l'édition, ou une part de divergence commune aux deux membres édités "
     "aux mêmes jetons, n'entre dans l'un ou l'autre produit que par sa projection sur le déplacement du saboteur, "
     "nulle sous l'hypothèse de travail (d) ; sinon elle tire q_k vers 1 et laisse au sur-saboteur une poussée de trop, "
     "comme une divergence propre du saboteur liée à celle du jumeau."),
    ("W-M1c", "W-M1", "lecture", T,
     "| étalon de la poussée faussé par une divergence commune aux deux membres édités | fermée : l'étalon est le membre "
     "non édité (vérification du brouillon 3, constat V-M1, mondes C12 à C20, C32, C33) |",
     "| étalon de la poussée faussé par une divergence commune aux deux membres édités | fermée : l'étalon est le membre "
     "non édité (vérification du brouillon 3, constat V-M1, mondes C12 à C20, C32, C33) |\n"
     "| étalon de la poussée faussé par ce que le saboteur partage avec le jumeau seul (divergences propres liées), ou par "
     "ce que les deux membres édités partagent et qui se projette sur le déplacement du saboteur (trace tournée vers "
     "lui) | **ouverte** : hypothèse de travail (d), que ce plan ne vérifie pas ; elle ne pèse que si la force porte sur "
     "la seule part propre à la famille, et elle y pèse lourd (vérification du brouillon 4, mondes N01 à N05, N17, N18, "
     "P1 et P2) |"),
    ("W-M1d", "W-M1", "lecture", T,
     "et si la divergence propre du saboteur est indépendante de celles des deux membres édités ; **ouverte** ailleurs",
     "et sous l'hypothèse de travail (d) sur l'étalon, sur laquelle tout repose quand la force porte sur la seule part "
     "propre à la famille ; **ouverte** ailleurs"),
    # ---------------------------------------------------------------- W-M2 : ce que le mot et les taux disent
    ("W-M2a", "W-M2", "lecture", T,
     "ni la force du sur-saboteur, ni une trace de l'édition commune aux deux sens, ni les deux réunies. Non tranché : une "
     "trace de l'édition propre à son sens",
     "ni la force du sur-saboteur, ni une trace de l'édition commune aux deux sens, ni les deux réunies, si l'étalon de "
     "la poussée, le saboteur, ne partage rien avec le jumeau seul. Non tranché : cet étalon, quand la force porte sur la "
     "seule part propre à la famille ; une part propre à la famille qui ne vivrait que d'un jeton à l'autre ; une trace "
     "de l'édition propre à son sens"),
    ("W-M2b", "W-M2", "lecture", T,
     "| force et trace de l'édition commune aux deux sens, réunies | fermée par la même construction (vérification du "
     "brouillon 3, constat V-B1, mondes C01 à C11, C28, C29 ; « Puissance ») |",
     "| force et trace de l'édition commune aux deux sens, réunies | fermée par la même construction (vérification du "
     "brouillon 3, constat V-B1, mondes C01 à C11, C28, C29 ; « Puissance »), sous l'hypothèse de travail (d) : une "
     "trace commune qui se projette sur le déplacement du saboteur fausse l'étalon (ligne « étalon de la poussée faussé "
     "par ce que le saboteur partage avec le jumeau seul ») |"),
    ("W-M2c", "W-M2", "lecture", T,
     "Ici la force, la trace commune aux deux sens et leur réunion laissent l'épreuve E2 à son niveau, dans tous les "
     "mondes inventés essayés (« Puissance ») ; la trace propre à son sens ne le fait pas : rivale ouverte (table de "
     "l'hypothèse).",
     "Ici la force, la trace commune aux deux sens et leur réunion laissent l'épreuve E2 à son niveau, dans tous les "
     "mondes inventés essayés où l'étalon est juste (« Puissance ») ; la trace propre à son sens ne le fait pas, ni un "
     "étalon faussé quand la force porte sur la seule part propre à la famille (hypothèse de travail (d)), ni une part "
     "propre à la famille qui ne vit que d'un jeton à l'autre : rivales ouvertes (table de l'hypothèse)."),
    ("W-M2d", "W-M2", "lecture", T,
     "Mot « sabotage » : 0,9 % des mondes au plus sur 1 000, dans chacun des 53 mondes essayés et dans les deux "
     "dimensions,",
     "Mot « sabotage » : 0,9 % des mondes au plus sur 1 000, dans chacun des 53 mondes essayés et dans les deux "
     "dimensions (l'étalon y est juste : divergence propre du saboteur indépendante, trace orthogonale à son "
     "déplacement),"),
    ("W-M2e", "W-M2", "lecture", T,
     "Produits calculés par jeton, avec une structure commune que la force ne multiplie pas : 48,7 à 100,0 % dans trois "
     "mondes ; c'est pourquoi ce texte calcule les produits sur les déplacements moyens, où cette structure n'entre pas.",
     "Produits calculés par jeton, avec une structure commune que la force ne multiplie pas : 48,7 à 100,0 % dans trois "
     "mondes ; c'est pourquoi ce texte calcule les produits sur les déplacements moyens, où cette structure n'entre pas. "
     "Étalon faussé, quand la force porte sur la seule part propre à la famille : 1,30 à 100 % selon la corrélation entre "
     "les divergences propres du saboteur et du jumeau (de 0,02 à 0,5), 43,8 et 91,6 % pour une trace commune de 0,3 "
     "tournée à 45° vers la direction commune (vérification du brouillon 4). Part propre à la famille qui ne vit que "
     "d'un jeton à l'autre, forcée : 100 % (même vérification)."),
    ("W-M2f", "W-M2", "lecture", T,
     "0,06 à 0,50 % : c'est le niveau (« Puissance »).",
     "0,06 à 0,50 % : c'est le niveau (« Puissance »), tant que l'étalon est juste (hypothèse de travail (d) ; "
     "vérification du brouillon 4)."),
    ("W-M2g", "W-M2", "lecture", FI,
     "En mondes inventés sans sabotage, il sort à tort au niveau prévu (0,4 à 0,5 % sur 20 000 mondes dans les cas les "
     "plus hauts).",
     "En mondes inventés sans sabotage, il sort à tort au niveau prévu (0,4 à 0,5 % sur 20 000 mondes dans les cas les "
     "plus hauts), tant que l'étalon de la poussée, le saboteur, ne partage rien avec le jumeau seul."),
    ("W-M2h", "W-M2", "lecture", FI,
     "Deux réserves restent, écrites dans la phrase : une trace de l'édition propre à son sens ; la force du saboteur "
     "lui-même, lu sans égalisation.",
     "Quatre réserves restent, écrites dans la phrase : une trace de l'édition propre à son sens ; la force du saboteur "
     "lui-même, lu sans égalisation ; l'étalon de la poussée, quand la force porte sur la seule part propre à la famille "
     "(une corrélation, même petite, entre ce que le saboteur et son jumeau ont appris de propre y fait sortir le mot à "
     "tort : de 1 à 100 % des mondes inventés) ; une part propre à la famille qui ne vit que d'un jeton à l'autre."),
    # ---------------------------------------------------------------- mineurs
    ("W-m1a", "W-m1", "lecture", T,
     "sept restent tels quels dans ce texte, huit sont repris dans des sections récrites pour la voie (iii) (la table "
     "dit lesquels et où).",
     "neuf restent tels quels dans ce texte, six sont repris dans des sections récrites pour la voie (iii) (la table "
     "dit lesquels et où ; compte vérifié par programme à la vérification du brouillon 4)."),
    ("W-m2a", "W-m2", "lecture", T,
     "Un petit sabotage mêlé à une force ne se perd plus comme au brouillon 3 : l'égalisation retire la force, non le "
     "sabotage.",
     "Un petit sabotage mêlé à une force sur ce que les membres partagent, sans étalement par jeton, ne se perd plus "
     "comme au brouillon 3 : l'égalisation retire la force, non le sabotage. Mêlé à une force sur la seule part propre "
     "à la famille, étalée par jeton, il se perd encore (vérification du brouillon 4, monde D11 : mot dans 0,1 et 0,5 % "
     "des mondes)."),
    ("W-m3a", "W-m3", "formation", T,
     "14. Dépense : chaque instance s'arrête dès que son cumul relevé plus un quart d'heure atteint sa coupure ; tout "
     "s'arrête au plafond du devis ;",
     "14. Dépense : chaque instance s'arrête dès que son cumul relevé plus un quart d'heure atteint sa coupure ; les "
     "pièces du devis s'arrêtent toutes à son plafond, que leur seule dépense compte ; une relance, hors de ce plafond, "
     "ne compte que dans son enveloppe (« Calendrier », borne de la relance) ;"),
    ("W-m3b", "W-m3", "formation (devis)", DV,
     "Le compteur commun arrête tout à 200 USD.",
     "Le compteur commun arrête toutes les pièces de ce devis à 200 USD ; il ne compte pas la dépense d'une relance, qui "
     "a son enveloppe (§ 3)."),
    ("W-m4a", "W-m4", "devis", DV,
     "Écrit le 2026-11-19 vers 15:30Z. **Brouillon, non contre-lu.**",
     "Écrit le 2026-11-19 vers 15:30Z, repris aux brouillons 3 et 4. **Brouillon : contre-lu au brouillon 2, vérifié "
     "au brouillon 3 ; le brouillon 4 est en vérification.**"),
    ("W-m4b", "W-m4", "devis", DV,
     "En vagues (ordre du texte : 6, 1, 2 ; 3, 4, 5 ; 7), l'horloge passe à 22,9 à 26,1 heures avec trois cartes, 17,8 à "
     "20,6 heures avec quatre.",
     "Pour mémoire, à 36 adaptateurs, en vagues (ordre du texte : 6, 1, 2 ; 3, 4, 5 ; 7), l'horloge passait à 22,9 à "
     "26,1 heures avec trois cartes, 17,8 à 20,6 heures avec quatre."),
    ("W-m4c", "W-m4", "devis", DV,
     "Aux prix vus ce soir-là (stockage ≈ 0,04 USD de l'heure), la formation coûterait 74,6 à 95,6 USD : dans la "
     "fourchette attendue, dont le bas n'est plus à espérer.",
     "Aux prix vus ce soir-là (stockage ≈ 0,04 USD de l'heure), la formation coûterait 76,7 à 98,7 USD à 39 adaptateurs "
     "(74,6 à 95,6 à 36) : dans la fourchette attendue, dont le bas n'est plus à espérer."),
    ("W-m4d", "W-m4", "devis", DV,
     "Elle ne part pas les jours où les cartes de ce plan tournent (23 et 26), sauf sur une carte à part.",
     "Elle ne part ni pendant la formation, ni le jour de la relecture (texte, « La chaîne voisine, comptée »), sauf sur "
     "une carte à part."),
]


def bloc(ident, piece, avant, apres):
    return (f"#### Couple {ident} — `{piece}`\n\nAvant :\n\n```text\n{avant}\n```\n\nAprès :\n\n```text\n{apres}\n```\n")


def main():
    sys.path.insert(0, str(RACINE / "src"))
    from controle_ia.prereg import problemes

    print("# Couples de la vérification du brouillon 4 — sortie du contrôle (v1)\n")
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
        print(f"{ident:6s} ({constat}, {touche}) {Path(piece).name} : « avant » {n_scelle} fois dans la pièce scellée, "
              f"{n_copie} fois au moment d'appliquer ; « après » déjà présent {n_apres} fois{'' if bon else ' — DÉFAUT'}")
    with tempfile.TemporaryDirectory() as d:
        chemin = Path(d) / "copie.md"
        chemin.write_text(copie[T], encoding="utf-8")
        print(f"\nvalidateur du dépôt sur la copie du texte après les couples : {problemes(chemin) or 'aucun problème'}")
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
