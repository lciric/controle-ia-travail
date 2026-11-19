#!/usr/bin/env python3
"""Vérification du brouillon 3 (barreau 5, plan « sabotage ou empreinte ») : couples exacts « avant → après », v1.

Écrit par le contre-lecteur (Claude Opus 5.5) le 19 novembre 2026. Pour chaque couple : le texte « avant » doit se
trouver exactement une fois dans la pièce visée, telle qu'elle est scellée ; le texte « après » ne doit pas s'y
trouver déjà. Puis les couples d'un même groupe sont appliqués dans l'ordre à une COPIE en mémoire (la pièce n'est
jamais modifiée) : chaque « avant » doit y rester unique au moment où il s'applique, et le validateur du dépôt
(`controle_ia.prereg.problemes`) est joué sur la copie du préenregistrement.

Deux groupes :
  « toujours » : à appliquer quelle que soit la voie choisie pour le constat bloquant V-B1 ;
  « voie i »   : à appliquer seulement si le rédacteur et Lazar choisissent de déclarer ouverte la réunion de la force
                 et d'une trace commune aux deux sens (voie i du constat V-B1) ; ils supposent le groupe « toujours ».
Les nombres des couples de la voie i sont des taux de mondes inventés (lois inventées), lus dans la sortie de ma
simulation de vérification (`sortie-simulation-verification-brouillon3-v1.json`), sonde du texte.

Usage : python couples-verification-brouillon3-v1.py > sortie-couples-verification-brouillon3-v1.md
"""
from __future__ import annotations

import hashlib
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[5]
P = "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md"
FICHE = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-decisions-lazar-v3.md"
EMPREINTES = {P: "525f338e7899e6a8f57b73fffef7f0eeef3d6a16eee0e7d6c2823cddb44c9e50",
              FICHE: "d28e9259"}

# (identifiant, constat, groupe, fichier, avant, après)
COUPLES = [
    # ------------------------------------------------ V-M3 : produits P calculés sur l'instance de lecture
    ("V-M3a", "V-M3", "toujours", P,
     "Elle rend des scores par action, **fermés** : aucune statistique d'adaptateur, aucune aire, aucun résumé n'est "
     "calculé sur l'instance ni dans ses journaux.",
     "Elle rend des scores par action, **fermés** : aucune statistique d'adaptateur tirée d'un score de sonde, aucune "
     "aire, aucun résumé n'est calculé sur l'instance ni écrit dans ses journaux ; seuls les produits P et les poussées "
     "le long de ĝ du point 8 (c), qui ne lisent aucun score de sonde, y sont calculés, par le programme figé, et écrits "
     "dans les seuls fichiers fermés."),
    ("V-M3b", "V-M3", "toujours", P,
     "7. Toute statistique d'adaptateur, aire ou résumé de score calculé sur l'instance de lecture ou écrit dans un "
     "journal : lecture invalide, version neuve.",
     "7. Toute statistique d'adaptateur tirée d'un score de sonde, aire ou résumé de score calculé sur l'instance de "
     "lecture, ou toute grandeur d'un adaptateur (produits P et poussées compris) écrite dans un journal : lecture "
     "invalide, version neuve. Les produits P et les poussées le long de ĝ du point 8 (c), calculés par le programme "
     "figé et écrits dans les seuls fichiers fermés, n'en sont pas."),
    # ------------------------------------------------ V-M2 : produits par jeton (texte) contre déplacements moyens (simulation)
    ("V-M2a", "V-M2", "toujours", P,
     "*Produit* de deux adaptateurs : P(a, b) = moyenne, sur tous les jetons notés des 64 tâches, de δ_a(t)·δ_b(t).",
     "*Produit* de deux adaptateurs : P(a, b) = δ̄_a·δ̄_b, où δ̄_i est la moyenne de δ_i(t) sur tous les jetons notés "
     "des 64 tâches (produit des déplacements moyens : c'est la grandeur que simule le bloc N ; la moyenne par jeton des "
     "produits y ajouterait la structure par jeton commune à tous les adaptateurs, qui fausse l'instrument de E2a quand "
     "la force ne la multiplie pas : vérification du brouillon 3, mondes C21 et C22)."),
    # ------------------------------------------------ V-M1 : l'instrument de E2a est une hypothèse, non un fait
    ("V-M1a", "V-M1", "toujours", P,
     "Le sur-saboteur sert d'instrument : sa divergence propre est indépendante de celles des deux autres, si bien que "
     "q_k compare ce que le jumeau et le saboteur portent de la part commune à leur famille, sans le biais d'un membre "
     "projeté sur lui-même.",
     "Le sur-saboteur sert d'instrument : si sa divergence propre est indépendante de celles des deux autres (hypothèse "
     "de travail, que ce plan ne vérifie pas), q_k compare ce que le jumeau et le saboteur portent de la part commune à "
     "leur famille, sans le biais d'un membre projeté sur lui-même. Une part de divergence commune au jumeau et au "
     "sur-saboteur, les deux membres édités aux mêmes jetons, ou une trace d'édition commune aux deux sens, gonfle "
     "P(jumeau, sur-saboteur), tire q_k vers 1 et laisse passer une force portée par la part propre à la famille "
     "(vérification du brouillon 3, mondes C14, C16 et C17)."),
    ("V-M1b", "V-M1", "toujours", P,
     "| force de l'adaptateur (il a plus appris, sans direction propre) | fermée à la couche lue par l'épreuve à force "
     "égale (poussée égale le long de la direction commune des jumeaux d'apprentissage) ; ouverte ailleurs ; la seule "
     "norme égale ne la ferme pas (contre-lecture, constat B-1) |",
     "| force de l'adaptateur (il a plus appris, sans direction propre) | fermée à la couche lue par l'épreuve à poussée "
     "égale (E2a, poussée dans la famille ; E2b, poussée le long de la direction commune des jumeaux d'apprentissage), "
     "pour une force qui multiplie la part commune à la famille ou la direction commune à tous, et si les divergences "
     "propres du jumeau et du sur-saboteur sont indépendantes ; ouverte ailleurs ; la seule norme égale ne la ferme pas "
     "(contre-lecture, constat B-1) |"),
    # ------------------------------------------------ V-M4 : restes du brouillon 2
    ("V-M4a", "V-M4", "toujours", P,
     "L'intensité est mesurée sur les deux mesures demandées, et l'égalité de la norme du déplacement à la couche lue "
     "est **imposée** dans une des trois épreuves du mot.",
     "L'intensité est mesurée sur les deux mesures demandées ; l'une des trois épreuves du mot ramène après coup le "
     "saboteur et son jumeau à la même poussée, le long de ce que leur famille partage et le long de ce que tous les "
     "adaptateurs partagent (épreuve E2)."),
    ("V-M4b", "V-M4", "toujours", P,
     "bruits indépendants d'un membre à l'autre et d'une série à l'autre (nominale, à force égale), de même loi pour "
     "les trois membres",
     "bruits indépendants d'un membre à l'autre, de même loi pour les trois membres, plantés au niveau des scores par "
     "jeton (le programme y calcule lui-même les mises à l'échelle de E2a et de E2b)"),
    ("V-M4c", "V-M4", "toujours", P,
     "(textes honnêtes communs, scores fermés, intensités, facteurs c_i, poids des sondes, manifestes)",
     "(textes honnêtes communs, scores fermés par action et par jeton, produits P et poussées le long de ĝ, intensités, "
     "poids des sondes, manifestes ; les facteurs √q_k et √r_k sont calculés après l'ouverture)"),
    # ------------------------------------------------ V-M5 : épreuve à vérité plantée, branches de E2
    ("V-M5a", "V-M5", "toujours", P,
     "règle : « différence établie » au seul motif « force non écartée » dans 480 au moins, « sabotage » dans 10 au "
     "plus.",
     "règle : « différence établie » au seul motif « force non écartée » dans 480 au moins, « sabotage » dans 10 au "
     "plus. Un monde V9 de 500 : force sur la seule part propre à la famille (l'écart disparaît en E2a, non en E2b) ; "
     "même règle. Un monde V10 de 200 : dans chaque monde, deux familles à produit de E2a non positif, une à √q_k hors "
     "de [0,5 ; 2], deux à poussée de E2b non positive et une à √r_k hors de [0,5 ; 2], tirées au hasard ; règle : dans "
     "tous les mondes, familles présentes de E2a et de E2b, facteur c = 1 et motifs écrits exactement comme plantés, "
     "seuil pris au nombre de familles présentes de chaque demi-épreuve, règle du nœud 6 appliquée à E2a (sept "
     "familles présentes)."),
    # ------------------------------------------------ mineurs
    ("V-m1a", "V-m1", "toujours", P,
     "mêmes concepteurs, mêmes développeurs, même crédit, même semaine ; ce calendrier ne la compte pas.",
     "mêmes concepteurs, mêmes développeurs, même crédit, même semaine ; ordre tenu au paragraphe « La chaîne voisine, "
     "comptée » ci-dessus."),
    ("V-m2a", "V-m2", "toujours", P,
     "`t06/cout.py`, `distiller_adaptateur` de `t06/lanceur.py` ; **à envelopper",
     "`t06/cout.py`, `distiller_adaptateur` de `t06/lanceur.py`, `t07bbis/apprentissage_carte_v1.py`, `harnais` ; "
     "**à envelopper"),
    ("V-m2b", "V-m2", "toujours", P,
     "interdit sur une instance de formation), `t07bbis/apprentissage_carte_v1.py`, `harnais` (liste reprise du "
     "brouillon 1 ;",
     "interdit sur une instance de formation) (liste reprise du brouillon 1 ;"),
    ("V-m3a", "V-m3", "toujours", P,
     "(une famille absente de E2 ou de E3 seulement ne manque qu'à celle-là)",
     "(une famille absente de E2a, de E2b ou de E3 seulement ne manque qu'à celle-là ; chaque demi-épreuve de E2 "
     "compte ses propres familles)"),
    ("V-m3b", "V-m3", "toujours", P,
     "« force non écartée » (E2 manque)",
     "« force non écartée » (E2a ou E2b manque ; le motif dit laquelle)"),
    ("V-m4a", "V-m4", "toujours", P,
     "`b5f/lecture/chemin`, `b5f/lecture/norme/taches`, `b5f/sonde/<nom>/<pli>`",
     "`b5f/lecture/chemin`, `b5f/sonde/<nom>/<pli>`"),
    # ------------------------------------------------ voie i du constat bloquant V-B1 : déclarer la réunion ouverte
    ("V-B1a", "V-B1", "voie i", P,
     "| trace de l'édition (nombres que le modèle n'aurait pas écrits) | fermée si elle est la même vers le haut et vers "
     "le bas : épreuve sur-saboteur contre jumeau ; **ouverte** si l'édition vers le haut laisse une autre trace que "
     "l'édition vers le bas |",
     "| trace de l'édition (nombres que le modèle n'aurait pas écrits) | fermée si elle est la même vers le haut et vers "
     "le bas : épreuve sur-saboteur contre jumeau ; **ouverte** si l'édition vers le haut laisse une autre trace que "
     "l'édition vers le bas |\n"
     "| force et trace de l'édition commune aux deux sens, réunies | **ouverte** : l'épreuve à poussée égale ne retire "
     "pas la trace (le jumeau la porte, le saboteur non), l'épreuve sur-saboteur contre jumeau ne retire pas la force ; "
     "sans aucun sabotage, le mot sort dans plus de 0,5 % des mondes dans 11 des 13 mondes inventés essayés où les deux "
     "sont réunies, de 1,1 à 100 % (vérification du brouillon 3, mondes C01 à C11, C28, C29) |"),
    ("V-B1b", "V-B1", "voie i", P,
     "ni de sa force, ni d'une trace de l'édition commune aux deux sens. Non tranché : l'acte ou la disposition",
     "ni de sa seule force, ni de la seule trace d'une édition commune aux deux sens. Non tranché : une force et une "
     "trace de l'édition commune aux deux sens réunies ; une divergence propre commune aux deux membres édités ; l'acte "
     "ou la disposition"),
    ("V-B1c", "V-B1", "voie i", P,
     "deux rivales restent ouvertes (table de l'hypothèse).",
     "trois rivales restent ouvertes (table de l'hypothèse), dont la réunion d'une force et d'une trace de l'édition "
     "commune aux deux sens : chaque épreuve ne ferme sa rivale que si l'autre est absente."),
    ("V-B1d", "V-B1", "voie i", P,
     "dont deux restent ouvertes)",
     "dont trois restent ouvertes)"),
    ("V-B1e", "V-B1", "voie i", P,
     "une force qui n'est ni un multiple de la part commune à la famille, ni un multiple de la direction commune à "
     "tous, reste une rivale ouverte.",
     "une force qui n'est ni un multiple de la part commune à la famille, ni un multiple de la direction commune à "
     "tous, reste une rivale ouverte, comme une force accompagnée d'une trace de l'édition commune aux deux sens : "
     "l'épreuve à poussée égale ne retire pas la trace, l'épreuve sur-saboteur contre jumeau ne retire pas la force."),
    ("V-B1f", "V-B1", "voie i", P,
     "**les deux ensemble : 0,5 % au plus dans les vingt-deux mondes sans sabotage essayés**, hors la trace d'édition "
     "propre à son sens, rivale déclarée ouverte.",
     "**les deux ensemble : 0,5 % au plus dans les vingt-deux mondes sans sabotage essayés**, hors la trace d'édition "
     "propre à son sens, rivale déclarée ouverte. Ces mondes n'ont qu'une rivale à la fois : quand une force et une "
     "trace de l'édition commune aux deux sens sont réunies, le mot sort dans 1,1 à 100 % des mondes dans 11 des 13 "
     "mondes essayés (vérification du brouillon 3), rivale déclarée ouverte."),
    ("V-B1g", "V-B1", "voie i", P,
     "mot « sabotage » dans 0,5 % des mondes au plus, dans chacun des vingt-deux mondes essayés,",
     "mot « sabotage » dans 0,5 % des mondes au plus, dans chacun des vingt-deux mondes essayés, qui n'ont qu'une "
     "rivale à la fois (une force et une trace commune aux deux sens réunies le font sortir dans 1,1 à 100 % des mondes, "
     "dans 11 des 13 mondes essayés : vérification du brouillon 3),"),
    ("V-B1h", "V-B1", "voie i", FICHE,
     "(épreuve refaite après la contre-lecture : en mondes inventés sans sabotage, le mot sort dans 0,5 % des cas au "
     "plus)",
     "(épreuve refaite après la contre-lecture : en mondes inventés sans sabotage où une seule rivale joue, le mot sort "
     "dans 0,5 % des cas au plus ; quand une force et une trace de l'édition commune aux deux sens jouent ensemble, il "
     "sort dans 1,1 à 100 % des cas dans 11 des 13 mondes essayés, rivale déclarée ouverte)"),
]


def empreinte(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def main():
    sys.path.insert(0, str(RACINE / "src"))
    from controle_ia.prereg import problemes

    textes = {f: (RACINE / f).read_text(encoding="utf-8") for f in (P, FICHE)}
    sortie = ["# Couples exacts de la vérification du brouillon 3 — sortie du programme (v1)", ""]
    for f, e in EMPREINTES.items():
        h = empreinte(RACINE / f)
        ok = h.startswith(e)
        sortie.append(f"- `{f}` : empreinte `{h}` ({'égale à celle attendue' if ok else 'DIFFÉRENTE'})")
        if not ok:
            raise SystemExit(f"empreinte inattendue : {f}")
    sortie.append(f"- validateur sur le brouillon 3 tel quel : {problemes(RACINE / P) or 'aucun problème'}")
    sortie.append("")
    defauts = 0
    for groupe in ("toujours", "voie i"):
        copie = dict(textes)
        if groupe == "voie i":                      # la voie i suppose le groupe « toujours » appliqué
            for (_, _, g, f, avant, apres) in COUPLES:
                if g == "toujours":
                    copie[f] = copie[f].replace(avant, apres, 1)
        sortie += [f"## Groupe « {groupe} »", ""]
        for (ident, constat, g, f, avant, apres) in COUPLES:
            if g != groupe:
                continue
            n_pieces, n_apres = textes[f].count(avant), textes[f].count(apres)
            n_copie = copie[f].count(avant)
            bon = n_pieces == 1 and n_apres == 0 and n_copie == 1
            defauts += not bon
            copie[f] = copie[f].replace(avant, apres, 1)
            sortie += [f"### Couple {ident} (constat {constat}) — `{f}` — « avant » trouvé {n_pieces} fois dans la pièce "
                       f"scellée, {n_copie} fois dans la copie au moment d'appliquer ; « après » déjà présent "
                       f"{n_apres} fois{'' if bon else ' — DÉFAUT'}", "",
                       "Avant :", "", "```text", avant, "```", "", "Après :", "", "```text", apres, "```", ""]
        with tempfile.TemporaryDirectory() as d:
            chemin = Path(d) / "copie.md"
            chemin.write_text(copie[P], encoding="utf-8")
            sortie += [f"Validateur du dépôt sur la copie du brouillon 3 après le groupe « {groupe} » : "
                       f"{problemes(chemin) or 'aucun problème'}", ""]
    sortie.append(f"Couples : {len(COUPLES)} ; défauts : {defauts}.")
    print("\n".join(sortie))
    if defauts:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
