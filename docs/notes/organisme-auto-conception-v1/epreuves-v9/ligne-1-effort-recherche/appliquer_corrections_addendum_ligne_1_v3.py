#!/usr/bin/env python3
"""Addendum 1 de la ligne 1 : version 2 -> version 3 (erratum).

Applique les quatre corrections de la vérification de la version 2 (textes exacts extraits par programme de sa
section 6), les deux ajouts de la mère (valables seulement sous l'option A de la décision 4) et la tenue de version.
Chaque texte ancien doit être trouvé une seule fois dans la version 2, sinon le programme s'arrête sans rien écrire.

Usage : appliquer_corrections_v3.py DOSSIER_DES_PIECES FICHIER_SORTIE HEURE(HH:MM, temps universel)
Lecture seule sur le dépôt ; n'écrit que FICHIER_SORTIE, et refuse de l'écraser.
"""
import hashlib
import os
import sys

NOM_V2 = "addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v2.md"
NOM_VERIF = "verification-addendum-1-ligne-1-v2-v1.md"
NOM_MANDAT = "mandat-redacteur-addendum-ligne-1-v3-v1.md"
SHA = {
    NOM_V2: "b5d769739e8b3be62a802d1d689a89af1537efb55692713e71ccde451e375f57",
    NOM_VERIF: "b0c09a4f94b3bc909c13757ea76ddc116581e0ce04ec1238c7db82490794893b",
    NOM_MANDAT: "ccd4b3648e2f5b48debb9ae5b501ea88736476442dcb4c4ac25766805c3abc2d",
    "code-v2/attestation-graines-developpeur-banc-a-v2-v1.md":
        "7565e0bae853fe5e30d447ae93d3a4b38c9a04466b13fd462a2ecc25d4377f15",
    "code-v2/attestation-graines-verificateur-banc-a-v2-v1.md":
        "56d7e2f6d52da254fee2998fa66f3c55c466ba0df1c713f64567a8fe8037e8e2",
}
COMMIT_VERIF = "3c3cd4af02b2316edba5f4b7fd27df8b5e988823"
COMMIT_ATTESTATIONS = "6f0957a7098ff0cefc8136cfd1c2d7eb3237c14c"
COMMIT_MANDAT = "53ec6e1a8d1bbab034dc77c90926debc6fd21f02"
SHA_V1 = "a28db12c418863f3cdb1cfbc17bd010217b80121a0141ff821ff5bdd86031980"
SHA_MANDAT_V2 = "fa449b921f9cfac814a5f81a64bb1fa96dddf228135843e86ecb51789567e734"


def lire(dossier, nom):
    with open(os.path.join(dossier, nom), "rb") as f:
        octets = f.read()
    vu = hashlib.sha256(octets).hexdigest()
    if vu != SHA[nom]:
        sys.exit(f"ARRÊT : empreinte de {nom} = {vu}, attendue {SHA[nom]}")
    return octets.decode("utf-8")


def entre(ligne, debut, fin=" »"):
    """Texte entre la première occurrence de `debut` et la DERNIÈRE occurrence de `fin` de la ligne."""
    if ligne.count(debut) < 1:
        sys.exit(f"ARRÊT : marqueur {debut!r} absent de la ligne {ligne[:60]!r}")
    i = ligne.index(debut) + len(debut)
    j = ligne.rindex(fin)
    if j <= i:
        sys.exit(f"ARRÊT : marqueurs mal ordonnés dans {ligne[:60]!r}")
    return ligne[i:j]


def ligne_unique(lignes, prefixe):
    trouvees = [l for l in lignes if l.startswith(prefixe)]
    if len(trouvees) != 1:
        sys.exit(f"ARRÊT : {len(trouvees)} ligne(s) de la vérification commencent par {prefixe!r}")
    return trouvees[0]


def remplacer(texte, ancien, nouveau, nom):
    n = texte.count(ancien)
    if n != 1:
        sys.exit(f"ARRÊT : {nom} : texte ancien trouvé {n} fois, une seule attendue : {ancien[:80]!r}")
    return texte.replace(ancien, nouveau)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    dossier, sortie, heure = sys.argv[1], sys.argv[2], sys.argv[3]
    if os.path.exists(sortie):
        sys.exit(f"ARRÊT : {sortie} existe déjà (on n'écrase jamais)")
    for nom in SHA:
        lire(dossier, nom)
    t = lire(dossier, NOM_V2)
    v = lire(dossier, NOM_VERIF).split("\n")

    # ---- Textes exacts de la section 6 de la vérification
    l_dev = ligne_unique(v, "   - Remplacer « À PORTER par la mère » de la ligne du développeur par : « ")
    l_ver = ligne_unique(v, "   - Remplacer « À PORTER par la mère » de la ligne du vérificateur par : « ")
    l_c2 = ligne_unique(v, "2. **§ 5.4, « État de ces conditions », dernière puce.**")
    l_c3 = ligne_unique(v, "3. **§ 6, après la phrase « L'étalonnage ne part pas avant le scellement de cet addendum. »**")
    l_c4 = ligne_unique(v, "4. **§ 7, réserve 6.**")
    txt_dev = entre(l_dev, "du développeur par : « ")
    txt_ver = entre(l_ver, "du vérificateur par : « ")
    txt_c2 = entre(l_c2, "n'est pas tenue à la lettre. » par : « ")
    txt_c3 = entre(l_c3, "Ajouter : « ")
    anc_c4 = entre(l_c4, "Remplacer « ", " » par : « ")
    txt_c4 = entre(l_c4, " » par : « ")

    # ---- Correction 1 : en-tête de table en double, puis les deux attestations
    t = remplacer(t, "| objet | valeur portée par la mère |\n|---|---|\n| objet | valeur |\n|---|---|\n| vérification du code v2",
                  "| objet | valeur portée par la mère |\n|---|---|\n| vérification du code v2", "correction 1, en-tête")
    t = remplacer(t, "(chemin, sha256) | À PORTER par la mère |\n| attestation écrite du vérificateur",
                  f"(chemin, sha256) | {txt_dev} |\n| attestation écrite du vérificateur", "correction 1, développeur")
    t = remplacer(t, "même objet (chemin, sha256) | À PORTER par la mère |",
                  f"même objet (chemin, sha256) | {txt_ver} |", "correction 1, vérificateur")
    if "À PORTER par la mère" in t:
        sys.exit("ARRÊT : il reste un « À PORTER par la mère »")

    # ---- Correction 2 : dernière puce de « État de ces conditions »
    debut = "- (iii) et (v) : le rapport des corrections et la vérification disent tous deux"
    fin = "la condition (v) n'est pas tenue à la lettre."
    if t.count(debut) != 1 or t.count(fin) != 1:
        sys.exit("ARRÊT : correction 2 : bornes de la puce non uniques")
    i, j = t.index(debut), t.index(fin) + len(fin)
    if "\n" in t[i:j]:
        sys.exit("ARRÊT : correction 2 : la puce tient sur plus d'une ligne")
    t = t[:i] + "- " + txt_c2 + t[j:]

    # ---- Correction 3 : phrase ajoutée au § 6
    phrase = "L'étalonnage ne part pas avant le scellement de cet addendum."
    t = remplacer(t, phrase, phrase + " " + txt_c3, "correction 3")

    # ---- Correction 4 : réserve 6 du § 7
    t = remplacer(t, anc_c4, txt_c4, "correction 4")

    # ---- Ajouts de la mère (hors des quatre corrections), valables seulement sous l'option A de la décision 4
    ajout_a14 = (
        "**Ajout de la mère (2026-11-19, vers 22:04Z, transmis par le coordinateur), hors des quatre corrections de la "
        "vérification de la version 2 ; valable seulement si Lazar choisit l'option A de la décision 4 (un seul mot, avant "
        "tout lancement) — garde A14 lue par programme contre l'heure du scellement de cet addendum, par une configuration "
        "v3.** La configuration v3 est la configuration v2 (`81f58ce5ca0a492ef231fa175303a21dfb21383a096fa71911b917923cc34f15`) "
        "plus un seul champ : l'heure du scellement de cet addendum, prise dans sa ligne au registre ; aucun autre champ ne "
        "change. L'empreinte de la configuration v3 est inscrite au registre avant le départ, et le lanceur la vérifie contre "
        "cette ligne. Le même contre-lecteur du code vérifie la v3 : différence d'un seul champ ; cas sain et artefact de la "
        "garde A14 rejoués (règle R5). **Repli, écrit d'avance** : si la configuration v3 n'est pas prête et vérifiée au "
        "départ, le contrôle de la garde A14 contre le scellement de cet addendum se fait par la lecture du journal du "
        "lanceur après la chaîne, comme le paragraphe précédent l'écrit déjà ; rien d'autre ne change et le départ n'attend "
        "pas la v3. Dans les deux cas, la lecture du manifeste et du journal du lanceur par la mère, puis par l'agent qui "
        "lit, reste due. Limite dite par le rédacteur, d'après sa lecture du code v2 (`lancer_ligne1_v2.py`, `preparer` et "
        "`verifier_derivations` ; `etalonnage_ligne1_v2.py`, `CHEMIN_CONFIGURATION`) : le code v2 lit le fichier nommé "
        "`configuration_ligne1_v2.json` et compare les dérivations au seul champ `horodatage_scellement` du préenregistrement ; "
        "il ne lit aucune ligne de registre. Ce que la configuration v3 demande au code, ou non, est donc à établir par cette "
        "vérification avant le départ ; tant qu'elle n'est pas rendue « conforme », c'est le repli qui vaut. Cet ajout ne "
        "relâche aucune garde ; il n'en crée aucune : il fait porter par le programme le premier des deux durcissements "
        "déclarés en tête. Si Lazar choisit l'option B, cet ajout tombe."
    )
    ancre_a14 = "C'est le premier des deux durcissements déclarés en tête ; il fait partie de l'option A que Lazar a retenue."
    t = remplacer(t, ancre_a14, ancre_a14 + "\n\n" + ajout_a14, "ajout A14")

    ajout_depot = (
        "8. **Ajout de la mère (2026-11-19, vers 22:04Z, transmis par le coordinateur), hors des quatre corrections de la "
        "vérification de la version 2 ; valable seulement si Lazar choisit l'option A de la décision 4 — versement de "
        "l'étalonnage pendant la course décisive.** Pendant que la course décisive tourne, la session copie le dossier scellé "
        "de l'étalonnage, l'empaquette par la sous-commande `empaqueter` du lanceur v2 lancée sur cette copie, et pousse sur "
        "la branche du compte. Aucun fichier n'est ouvert, ni par un agent ni par la mère : seul le programme d'empaquetage "
        "les lit ; le code ne change pas. Le commit poussé, les noms, les tailles et les empreintes sont notés au registre. "
        "Les points 1 à 7 valent pour ce versement comme pour tout autre : dossier de nom neuf (point 6), rien d'effacé "
        "(point 3), plafond de 500 Mo (point 4), aucune règle de lecture levée (point 7). Si Lazar choisit l'option B, cet "
        "ajout tombe."
    )
    ancre_depot = "l'ordre des gestes 6 à 8 du texte scellé vaut."
    t = remplacer(t, ancre_depot, ancre_depot + "\n" + ajout_depot, "ajout dépôt")

    # ---- Tenue de version
    t = remplacer(t, "code visé, dépôt des sorties — v2\n", "code visé, dépôt des sorties — v3\n", "tenue, titre")
    t = remplacer(
        t,
        "**Statut : version 2, non scellée, avant vérification des corrections.** Pièce décisive (classe A). Elle remplace la "
        "version 1 (`addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v1.md`, `" + SHA_V1 + "`), qui reste archivée "
        "sans modification (règle R12). Elle applique",
        "**Statut : version 3 (erratum de la version 2), non scellée, avant le contrôle de son différentiel par le "
        "vérificateur.** Pièce décisive (classe A). Elle remplace la version 2 (`" + NOM_V2 + "`, `" + SHA[NOM_V2] + "`), qui "
        "reste archivée sans modification (règle R12), comme la version 1 "
        "(`addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v1.md`, `" + SHA_V1 + "`). Elle ne diffère de la "
        "version 2 que par les quatre corrections de la vérification de celle-ci (`" + NOM_VERIF + "`, `" + SHA[NOM_VERIF]
        + "`, § 6, textes exacts), par deux ajouts de la mère valables seulement sous l'option A de la décision 4 (§ 6 et "
        "§ 9, point 8) et par la tenue de version (liste au § 11). Comme la version 2, elle applique",
        "tenue, statut")
    t = remplacer(
        t,
        "(`mandat-redacteur-addendum-ligne-1-v2-v1.md`, `" + SHA_MANDAT_V2 + "`). Il n'a écrit",
        "(`mandat-redacteur-addendum-ligne-1-v2-v1.md`, `" + SHA_MANDAT_V2 + "`) pour la version 2 ; pour cette version 3, "
        "un autre rédacteur neuf du même modèle, sur le mandat `" + NOM_MANDAT + "`, `" + SHA[NOM_MANDAT] + "` (donné sur "
        "GO-2026-11-19-81), complété par un mot du coordinateur pour les deux ajouts de la mère. Tout ce qui dit « je » est "
        "du rédacteur de la version 2 ; celui de la version 3 n'a rien relu d'autre que les pièces nommées au § 11. Aucun "
        "des deux n'a écrit",
        "tenue, auteur")
    t = remplacer(t, "écrit entre 21:53 et 21:59.",
                  "écrit entre 21:53 et 21:59 (version 2) ; version 3 écrite le même jour vers " + heure + ".", "tenue, heure")
    t = remplacer(
        t,
        "douze corrections ; registre R-3932).\n",
        "douze corrections ; registre R-3932).\n- Vérification de la version 2, appliquée par cette version 3 : `" + NOM_VERIF
        + "`, `" + SHA[NOM_VERIF] + "` (même contre-lecteur, modèle O ; verdict « scellable après corrections », quatre "
        "corrections à texte exact ; commit `" + COMMIT_VERIF + "` de `lot/compte-organisme-v1`).\n",
        "tenue, vérification en tête")
    t = remplacer(t, "Cette version 2 les applique (différentiel au § 10)", "La version 2 les applique (différentiel au § 10)",
                  "tenue, § 8")
    t = remplacer(
        t,
        "| vérification des corrections et de la matière neuve de cette version (chemin, sha256, verdict) | À PORTER |",
        "| vérification des corrections et de la matière neuve de la version 2 (chemin, sha256, verdict) | `" + NOM_VERIF
        + "`, `" + SHA[NOM_VERIF] + "`, commit `" + COMMIT_VERIF + "` de `lot/compte-organisme-v1` ; même contre-lecteur que "
        "pour la version 1 (modèle O) ; **verdict : « Scellable après corrections »**, quatre corrections à texte exact, "
        "appliquées à la lettre par cette version 3 (§ 11) |\n"
        "| contrôle du différentiel version 2 → version 3 par le même vérificateur (chemin, sha256, verdict) ; il porte aussi "
        "sur les deux ajouts de la mère (§ 6 et § 9, point 8), que la vérification de la version 2 n'a pas vus | À PORTER |",
        "tenue, table du § 8")

    section_11 = (
        "\n## 11. Différentiel version 2 → version 3 (erratum)\n\n"
        "Pièces lues pour cette version, empreintes vérifiées par programme, branche `lot/compte-organisme-v1`, commit `"
        + COMMIT_MANDAT + "` : la version 2 (`" + SHA[NOM_V2] + "`), son rapport "
        "(`999d644668c0956a430223d6e8377140e4f79f2ace40373bd1797a27bfa9f226`) et son mandat (`" + SHA_MANDAT_V2 + "`) ; la "
        "vérification de la version 2 (`" + SHA[NOM_VERIF] + "`) ; les deux attestations sous `code-v2/` "
        "(`7565e0bae853fe5e30d447ae93d3a4b38c9a04466b13fd462a2ecc25d4377f15` et "
        "`56d7e2f6d52da254fee2998fa66f3c55c466ba0df1c713f64567a8fe8037e8e2`, commit `" + COMMIT_ATTESTATIONS + "`) ; le mandat "
        "de cette version (`" + SHA[NOM_MANDAT] + "`). Lus en partie, pour la seule limite dite au § 6 : `code/lancer_ligne1_v2.py` "
        "(`preparer`, `verifier_derivations`, `main`), la ligne `CHEMIN_CONFIGURATION` de `code/etalonnage_ligne1_v2.py`, les "
        "noms des champs de `code/configuration_ligne1_v2.json`. Rien lancé, aucun résultat lu, aucune graine dérivée. Les "
        "remplacements sont faits par programme, chaque texte ancien trouvé une seule fois ; les textes des quatre corrections "
        "sont extraits par ce programme de la section 6 de la vérification, non recopiés à la main.\n\n"
        "**Les quatre corrections de la vérification de la version 2 (`b0c09a4f…`, § 6), à la lettre**\n\n"
        "| n° | où | fait |\n|---|---|---|\n"
        "| 1 | § 5.4, table | les deux lignes d'en-tête en double retirées ; les deux « À PORTER par la mère » remplacés par les "
        "deux textes exacts (attestations `7565e0ba…` et `56d7e2f6…`, commit `6f0957a7…`), limite des 18 passes de mutation "
        "comprise |\n"
        "| 2 | § 5.4, « État de ces conditions », dernière puce | puce remplacée par le texte exact : (iii) et (v) tenues, "
        "sources citées, limite des 18 passes de mutation recopiée |\n"
        "| 3 | § 6, après « L'étalonnage ne part pas avant le scellement de cet addendum. » | texte exact ajouté : ni `tout`, ni "
        "étape à la main, ni étalonnage seul avant le mot de Lazar ou tant que la décision 4 n'est pas tranchée ; portée du "
        "mot s'il vient après l'étalonnage |\n"
        "| 4 | § 7, réserve 6 | fin de la réserve remplacée par le texte exact : programme de l'audit de symétrie écrit, "
        "contre-lu et porté au registre avant le lancement de la course décisive ; son empreinte dans le mot de Lazar |\n\n"
        "**Deux ajouts de la mère, hors des quatre corrections** (2026-11-19, vers 22:04Z, transmis par le coordinateur ; "
        "valables seulement si Lazar choisit l'option A de la décision 4) : § 6, garde A14 lue par programme contre l'heure du "
        "scellement de cet addendum par une configuration v3, avec son repli et une limite dite par le rédacteur ; § 9, point 8, "
        "versement de l'étalonnage pendant la course décisive. La vérification de la version 2 ne les a pas vus : son "
        "acceptation d'un simple contrôle du différentiel ne valait que pour les quatre corrections ; ils sont donc à lire "
        "pour eux-mêmes.\n\n"
        "**Tenue de version** : titre (« v3 ») ; phrase de statut ; ligne de l'auteur (mandat de cette version cité) ; heure ; "
        "ligne « Vérification de la version 2 » ajoutée en tête ; au § 8, « Cette version 2 » devenu « La version 2 », la "
        "vérification de la version 2 portée à sa place dans la table, et une ligne « À PORTER » pour le contrôle du "
        "différentiel ; ce § 11.\n\n"
        "**Inchangé** : tout le reste, au caractère près, y compris le § 1 (pièces lues par le rédacteur de la version 2, à "
        "son commit) et le § 10.\n"
    )
    if not t.endswith("\n"):
        sys.exit("ARRÊT : la version 2 ne finit pas par un saut de ligne")
    t = t + section_11

    with open(sortie, "x", encoding="utf-8") as f:
        f.write(t)
    print(hashlib.sha256(t.encode("utf-8")).hexdigest(), sortie)


if __name__ == "__main__":
    main()
