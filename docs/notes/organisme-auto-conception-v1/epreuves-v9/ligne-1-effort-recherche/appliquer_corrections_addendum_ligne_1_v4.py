#!/usr/bin/env python3
"""Addendum 1 de la ligne 1 : version 3 -> version 4 (erratum).

Applique les cinq corrections du contrôle du différentiel version 2 -> version 3 (textes exacts extraits par programme
de sa section 6, sans recopie à la main) et la tenue de version que ce contrôle décrit (statut, § 8, phrase ajoutée au
§ 11, § 12 neuf). Chaque texte ancien doit être trouvé exactement une fois dans la version 3, sinon le programme
s'arrête sans rien écrire.

Usage : appliquer_corrections_addendum_ligne_1_v4.py DOSSIER_DES_PIECES FICHIER_SORTIE HEURE(HH:MM, temps universel)
        COMMIT_LU
Lecture seule sur le dépôt ; n'écrit que FICHIER_SORTIE, et refuse de l'écraser.
"""
import hashlib
import os
import re
import sys

NOM_V3 = "addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v3.md"
NOM_V2 = "addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v2.md"
NOM_CONTROLE = "controle-differentiel-addendum-1-ligne-1-v3-v1.md"
NOM_VERIF = "verification-addendum-1-ligne-1-v2-v1.md"
NOM_MANDAT = "mandat-redacteur-addendum-ligne-1-v4-v1.md"
NOM_RAPPORT_V3 = "rapport-redacteur-addendum-ligne-1-v3-v1.md"
NOM_DIFF_V3 = "differentiel-addendum-1-ligne-1-v2-v3.diff"
NOM_MANDAT_V3 = "mandat-redacteur-addendum-ligne-1-v3-v1.md"
NOM_PROGRAMME_V3 = "appliquer_corrections_addendum_ligne_1_v3.py"
SHA = {
    NOM_V3: "fb48a8ab9aeee1667c46a3d72dbf97d39343ecfb10227c652074d38f46ba55d5",
    NOM_V2: "b5d769739e8b3be62a802d1d689a89af1537efb55692713e71ccde451e375f57",
    NOM_CONTROLE: "328322989b4d0eda7de480a666ed5599a26fe713ab16dc5d5a9fedf7000f17d5",
    NOM_VERIF: "b0c09a4f94b3bc909c13757ea76ddc116581e0ce04ec1238c7db82490794893b",
    NOM_MANDAT: "447df1443aecc990629a9b5845a06c762a094414a092da40d2a39e146ceb5f16",
    NOM_RAPPORT_V3: "d2cc55ddc6d87ae50c49f757573033441cc3da2782fd818c8dd3927a9c27c48c",
    NOM_DIFF_V3: "8c42ccc88910048cd666e98474ea61224eb17779a15f514be6561b779f7b3740",
    NOM_MANDAT_V3: "ccd4b3648e2f5b48debb9ae5b501ea88736476442dcb4c4ac25766805c3abc2d",
    NOM_PROGRAMME_V3: "9d26722ae7ca1e70d5a90f468a28515e8d242baa72b134a4985379508396de71",
}
SHA_V1 = "a28db12c418863f3cdb1cfbc17bd010217b80121a0141ff821ff5bdd86031980"
COMMIT_CONTROLE = "e8069af6d040616a2853f4ec4fc965809bd05706"
COMMIT_MANDAT = "ebe691f82cf875166e023723b3957acdbfcff681"


def arret(message):
    sys.exit("ARRÊT : " + message)


def lire(dossier, nom):
    with open(os.path.join(dossier, nom), "rb") as f:
        octets = f.read()
    vu = hashlib.sha256(octets).hexdigest()
    if vu != SHA[nom]:
        arret(f"empreinte de {nom} = {vu}, attendue {SHA[nom]}")
    return octets.decode("utf-8")


def entre(ligne, debut, fin):
    """Texte entre la première occurrence de `debut` et la DERNIÈRE occurrence de `fin` de la ligne."""
    if debut not in ligne or fin not in ligne:
        arret(f"marqueur {debut!r} ou {fin!r} absent de la ligne {ligne[:60]!r}")
    i = ligne.index(debut) + len(debut)
    j = ligne.rindex(fin)
    if j <= i:
        arret(f"marqueurs mal ordonnés dans {ligne[:60]!r}")
    return ligne[i:j]


def consigne_et_texte(lignes, prefixe):
    """La ligne de consigne (unique) qui commence par `prefixe`, et le texte exact de la ligne qui la suit."""
    rangs = [k for k, l in enumerate(lignes) if l.startswith(prefixe)]
    if len(rangs) != 1:
        arret(f"{len(rangs)} ligne(s) du contrôle commencent par {prefixe!r}")
    consigne = lignes[rangs[0]]
    if not consigne.endswith(" :"):
        arret(f"la consigne {prefixe!r} ne finit pas par « : »")
    suite = lignes[rangs[0] + 1]
    if not (suite.startswith("   « ") and suite.endswith(" »")):
        arret(f"la ligne qui suit {prefixe!r} n'est pas un texte entre guillemets")
    return consigne, suite[len("   « "):-len(" »")]


def remplacer(texte, ancien, nouveau, nom):
    n = texte.count(ancien)
    if n != 1:
        arret(f"{nom} : texte ancien trouvé {n} fois, une seule attendue : {ancien[:80]!r}")
    return texte.replace(ancien, nouveau)


def main():
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    dossier, sortie, heure, commit_lu = sys.argv[1:5]
    if not re.fullmatch(r"[0-2][0-9]:[0-5][0-9]", heure):
        arret("heure attendue sous la forme HH:MM")
    if not re.fullmatch(r"[0-9a-f]{40}", commit_lu):
        arret("commit attendu sur 40 caractères")
    if os.path.exists(sortie):
        arret(f"{sortie} existe déjà (on n'écrase jamais)")
    for nom in SHA:
        lire(dossier, nom)
    t = lire(dossier, NOM_V3)
    c = lire(dossier, NOM_CONTROLE).split("\n")

    # ---- Textes exacts de la section 6 du contrôle
    l1, txt1 = consigne_et_texte(c, "1. **§ 6, retrait de la configuration v3.**")
    l2, txt2 = consigne_et_texte(c, "2. **§ 6, paragraphe « Conséquence pour la garde A14 ».**")
    l3, txt3 = consigne_et_texte(c, "3. **§ 9, point 8.**")
    l4, txt4 = consigne_et_texte(c, "4. **En-tête, ligne de l'auteur.**")
    l5, txt5 = consigne_et_texte(c, "5. **En-tête, après la puce « ")
    debut1 = entre(l1, "qui commence par « ", " » et qui finit par « ")
    fin1 = entre(l1, " » et qui finit par « ", " » (cette phrase de fin")
    anc2 = entre(l2, "Remplacer « ", " » par :")
    ancre3 = entre(l3, "Après « ", " », ajouter :")
    anc4 = entre(l4, "Remplacer « ", " » par :")
    ancre5 = entre(l5, "après la puce « ", " ».**")
    if not txt5.startswith("- "):
        arret("correction 5 : le texte exact n'est pas une puce")

    # ---- Correction 1 : le paragraphe du § 6 sur la configuration v3, remplacé en entier
    if t.count(debut1) != 1:
        arret(f"correction 1 : début du paragraphe trouvé {t.count(debut1)} fois")
    lignes = t.split("\n")
    rangs = [k for k, l in enumerate(lignes) if l.startswith(debut1)]
    if len(rangs) != 1 or not lignes[rangs[0]].endswith(fin1):
        arret("correction 1 : le paragraphe ne commence ou ne finit pas comme le contrôle le dit")
    lignes[rangs[0]] = txt1
    t = "\n".join(lignes)

    # ---- Correction 2 : source d'heure de la garde A14
    t = remplacer(t, anc2, txt2, "correction 2")

    # ---- Correction 3 : phrase ajoutée au § 9, point 8
    t = remplacer(t, ancre3, ancre3 + " " + txt3, "correction 3")

    # ---- Correction 4 : ligne de l'auteur
    t = remplacer(t, anc4, txt4, "correction 4")

    # ---- Correction 5 : puce ajoutée après la puce « Condition de la même ligne, recopiée telle quelle »
    lignes = t.split("\n")
    rangs = [k for k, l in enumerate(lignes) if l.startswith("- **" + ancre5 + "**")]
    if len(rangs) != 1:
        arret(f"correction 5 : puce d'ancrage trouvée {len(rangs)} fois")
    lignes.insert(rangs[0] + 1, txt5)
    t = "\n".join(lignes)

    for nom, texte in (("1", txt1), ("2", txt2), ("3", txt3), ("4", txt4), ("5", txt5)):
        if t.count(texte) != 1:
            arret(f"correction {nom} : texte exact présent {t.count(texte)} fois après application")
    for nom, texte in (("1", debut1), ("2", anc2), ("4", anc4)):
        if texte in t:
            arret(f"correction {nom} : le texte ancien est encore présent")

    # ---- Tenue de version
    t = remplacer(t, "code visé, dépôt des sorties — v3\n", "code visé, dépôt des sorties — v4\n", "tenue, titre")
    t = remplacer(
        t,
        "**Statut : version 3 (erratum de la version 2), non scellée, avant le contrôle de son différentiel par le "
        "vérificateur.** Pièce décisive (classe A). Elle remplace la version 2 (`" + NOM_V2 + "`, `" + SHA[NOM_V2] + "`), qui "
        "reste archivée sans modification (règle R12), comme la version 1 "
        "(`addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v1.md`, `" + SHA_V1 + "`). Elle ne diffère de la "
        "version 2 que par les quatre corrections de la vérification de celle-ci (`" + NOM_VERIF + "`, `" + SHA[NOM_VERIF]
        + "`, § 6, textes exacts), par deux ajouts de la mère valables seulement sous l'option A de la décision 4 (§ 6 et "
        "§ 9, point 8) et par la tenue de version (liste au § 11). Comme la version 2, elle applique",
        "**Statut : version 4 (erratum de la version 3), non scellée, avant le contrôle de son différentiel par le "
        "vérificateur.** Pièce décisive (classe A). Elle remplace la version 3 (`" + NOM_V3 + "`, `" + SHA[NOM_V3] + "`), qui "
        "reste archivée sans modification (règle R12), comme la version 2 (`" + NOM_V2 + "`, `" + SHA[NOM_V2] + "`) et la "
        "version 1 (`addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v1.md`, `" + SHA_V1 + "`). Elle ne diffère de "
        "la version 3 que par les cinq corrections du contrôle du différentiel de celle-ci (`" + NOM_CONTROLE + "`, `"
        + SHA[NOM_CONTROLE] + "`, § 6, textes exacts) et par la tenue de version (liste au § 12). La version 3 ne différait "
        "de la version 2 que par les quatre corrections de la vérification de celle-ci (`" + NOM_VERIF + "`, `"
        + SHA[NOM_VERIF] + "`, § 6, textes exacts), par deux ajouts de la mère (§ 6 et § 9, point 8) — le premier, la "
        "configuration v3, est retiré par cette version 4 ; le second reste valable seulement sous l'option A de la "
        "décision 4 — et par la tenue de version (liste au § 11). Comme la version 2, elle applique",
        "tenue, statut")
    t = remplacer(
        t,
        " pour la version 2 ; pour cette version 3, un autre rédacteur neuf du même modèle, sur le mandat `" + NOM_MANDAT_V3
        + "`, `" + SHA[NOM_MANDAT_V3] + "` (donné sur GO-2026-11-19-81), complété par un mot du coordinateur pour les deux "
        "ajouts de la mère. ",
        " pour la version 2 ; pour la version 3, un autre rédacteur neuf du même modèle, sur le mandat `" + NOM_MANDAT_V3
        + "`, `" + SHA[NOM_MANDAT_V3] + "` (donné sur GO-2026-11-19-81), complété par un mot du coordinateur pour les deux "
        "ajouts de la mère ; pour cette version 4, un troisième rédacteur neuf du même modèle, sur le mandat `" + NOM_MANDAT
        + "`, `" + SHA[NOM_MANDAT] + "` (donné sur GO-2026-11-19-81 et sur la décision de la mère de ne faire ni "
        "configuration v3 ni code v3). ",
        "tenue, auteur")
    t = remplacer(
        t,
        "celui de la version 3 n'a rien relu d'autre que les pièces nommées au § 11. Aucun des deux n'a écrit",
        "celui de la version 3 n'a rien relu d'autre que les pièces nommées au § 11, celui de la version 4 que celles "
        "nommées au § 12. Aucun des trois n'a écrit",
        "tenue, auteur (suite)")
    t = remplacer(t, "version 3 écrite le même jour vers 22:08.",
                  "version 3 écrite le même jour vers 22:08 ; version 4 écrite le même jour vers " + heure + ".",
                  "tenue, heure")
    t = remplacer(
        t,
        "- Vérification de la version 2, appliquée par cette version 3 : ",
        "- Vérification de la version 2, appliquée par la version 3 : ",
        "tenue, vérification en tête")
    t = remplacer(
        t,
        "quatre corrections à texte exact ; commit `3c3cd4af02b2316edba5f4b7fd27df8b5e988823` de `lot/compte-organisme-v1`).\n",
        "quatre corrections à texte exact ; commit `3c3cd4af02b2316edba5f4b7fd27df8b5e988823` de `lot/compte-organisme-v1`).\n"
        "- Contrôle du différentiel version 2 → version 3, appliqué par cette version 4 : `" + NOM_CONTROLE + "`, `"
        + SHA[NOM_CONTROLE] + "` (même contre-lecteur, modèle O ; verdict « scellable après corrections », cinq corrections "
        "à texte exact ; commit `" + COMMIT_CONTROLE + "` de `lot/compte-organisme-v1`).\n",
        "tenue, contrôle en tête")
    t = remplacer(
        t,
        "quatre corrections à texte exact, appliquées à la lettre par cette version 3 (§ 11) |\n"
        "| contrôle du différentiel version 2 → version 3 par le même vérificateur (chemin, sha256, verdict) ; il porte aussi "
        "sur les deux ajouts de la mère (§ 6 et § 9, point 8), que la vérification de la version 2 n'a pas vus | À PORTER |",
        "quatre corrections à texte exact, appliquées à la lettre par la version 3 (§ 11) |\n"
        "| contrôle du différentiel version 2 → version 3 par le même vérificateur (chemin, sha256, verdict) ; il porte aussi "
        "sur l'ajout de la mère (§ 9, point 8) et le retrait de la configuration v3 (§ 6), que la vérification de la "
        "version 2 n'a pas vus | `" + NOM_CONTROLE + "`, `" + SHA[NOM_CONTROLE] + "`, commit `" + COMMIT_CONTROLE + "` de "
        "`lot/compte-organisme-v1` ; même vérificateur (modèle O) ; **verdict : « Scellable après corrections »**, cinq "
        "corrections à texte exact, appliquées à la lettre par cette version 4 (§ 12) |\n"
        "| contrôle du différentiel version 3 → version 4 par le même vérificateur (chemin, sha256, verdict) | À PORTER |",
        "tenue, table du § 8")
    phrase_11 = "Le premier de ces ajouts (configuration v3) est retiré par la version 4, non retenu par la mère (§ 12)."
    t = remplacer(t, "ils sont donc à lire pour eux-mêmes.\n", "ils sont donc à lire pour eux-mêmes. " + phrase_11 + "\n",
                  "tenue, phrase du § 11")

    section_12 = (
        "\n## 12. Différentiel version 3 → version 4 (erratum)\n\n"
        "Pièces lues pour cette version, empreintes vérifiées par programme, branche `lot/compte-organisme-v1`, commit `"
        + commit_lu + "` : la version 3 (`" + SHA[NOM_V3] + "`), son rapport (`" + SHA[NOM_RAPPORT_V3] + "`), son "
        "différentiel (`" + SHA[NOM_DIFF_V3] + "`), son mandat (`" + SHA[NOM_MANDAT_V3] + "`) et son programme de "
        "remplacement (`" + SHA[NOM_PROGRAMME_V3] + "`, lu, non exécuté) ; le contrôle du différentiel version 2 → version 3 "
        "(`" + SHA[NOM_CONTROLE] + "`, commit `" + COMMIT_CONTROLE + "`) ; la vérification de la version 2 (`"
        + SHA[NOM_VERIF] + "`) ; la version 2 pour sa seule empreinte (`" + SHA[NOM_V2] + "`, intacte) ; le mandat de cette "
        "version (`" + SHA[NOM_MANDAT] + "`, commit `" + COMMIT_MANDAT + "`). Aucun fichier du code n'a été rouvert : ce que "
        "les corrections 1 à 3 disent du code vient du contrôle. Rien lancé, aucun résultat lu, aucune graine dérivée. Les "
        "remplacements sont faits par programme, chaque texte ancien trouvé une seule fois ; les textes des cinq corrections "
        "sont extraits par ce programme de la section 6 du contrôle, non recopiés à la main.\n\n"
        "**Les cinq corrections du contrôle du différentiel version 2 → version 3 (`32832298…`, § 6), à la lettre**\n\n"
        "| n° | où | fait |\n|---|---|---|\n"
        "| 1 | § 6, paragraphe « Ajout de la mère […] par une configuration v3 » | paragraphe remplacé en entier par le texte "
        "exact : configuration v3 proposée par la mère, non retenue par elle avant le scellement ; aucune configuration v3 "
        "et aucun code v3 ; code visé inchangé (§ 5.1) ; contrôle de la garde A14 contre l'heure du scellement de cet "
        "addendum par lecture, sous l'option A comme sous l'option B de la décision 4 ; raison du retrait |\n"
        "| 2 | § 6, paragraphe « Conséquence pour la garde A14 » | source d'heure remplacée par le texte exact : fichier "
        "d'état du lanceur (`etat-lancement-ligne1-v2.json`, champ `debut` de chaque session) ; journal du lanceur lu en "
        "complément, le programme n'y écrivant aucune heure ; pour une étape lancée à la main, heure consignée au registre "
        "avant de lancer |\n"
        "| 3 | § 9, point 8, après « le code ne change pas. » | texte exact ajouté : copie et dossier d'empaquetage hors du "
        "dossier de sortie de la chaîne et hors de `code/`, rien d'écrit sous `code/` pendant la chaîne ; plafond du point 4 "
        "appliqué au total des deux versements, retour à la mère avant de pousser le second s'il devait être dépassé |\n"
        "| 4 | en-tête, ligne de l'auteur | phrase remplacée par le texte exact : « je », et « cette version » hors de "
        "l'en-tête, du § 8 et des § 11 et suivants, sont du rédacteur de la version 2 et désignent la version 2 |\n"
        "| 5 | en-tête, après la puce « Condition de la même ligne, recopiée telle quelle » | puce ajoutée, texte exact : "
        "lecture de cette condition de la ligne GO-2026-11-19-81 par la mère |\n\n"
        "**Raison du retrait de la configuration v3** : décision de la mère (2026-11-19, vers 22:10Z, d'après le mandat de "
        "cette version) : ni configuration v3 ni code v3. D'après le contrôle (§ 3), le code v2 lit un fichier de "
        "configuration de nom fixe et un seul champ d'heure ; une configuration v3 aurait demandé de changer le code visé au "
        "§ 5.1 après sa vérification. Le second ajout de la mère (§ 9, point 8, versement de l'étalonnage pendant la course "
        "décisive) est gardé, toujours valable seulement sous l'option A de la décision 4, et précisé par la correction 3. "
        "D'après le même contrôle (§ 3), la source d'heure que la correction 2 remplace venait de la correction 9 de la "
        "contre-lecture de la version 1. La décision 4 reste ouverte, sans défaut : rien ne part avant elle (§ 6).\n\n"
        "**Tenue de version** : titre (« v4 ») ; phrase de statut ; ligne de l'auteur (mandat de cette version cité, trois "
        "rédacteurs distingués, « pour cette version 3 » devenu « pour la version 3 », « Aucun des deux » devenu « Aucun des "
        "trois ») ; heure ; dans la ligne « Vérification de la version 2 » de l'en-tête, « cette version 3 » devenu « la "
        "version 3 » ; ligne « Contrôle du différentiel version 2 → version 3 » ajoutée en tête ; au § 8, « cette version 3 » "
        "devenu « la version 3 », la ligne du contrôle version 2 → version 3 remplie (chemin, empreinte, verdict) et "
        "reformulée comme le contrôle le demande, et une ligne « À PORTER » ajoutée pour le contrôle du différentiel "
        "version 3 → version 4 ; au § 11, la seule phrase « " + phrase_11 + " » ajoutée à la fin du paragraphe « Deux "
        "ajouts de la mère » ; ce § 12.\n\n"
        "**Inchangé** : tout le reste, au caractère près, y compris les § 1 à 5, le § 7, le § 10 et le § 11 hors la phrase "
        "ajoutée.\n"
    )
    if not t.endswith("\n"):
        arret("la version 3 ne finit pas par un saut de ligne")
    if "cette version 3" in t:
        arret("il reste un « cette version 3 » hors du § 12")
    t = t + section_12

    with open(sortie, "x", encoding="utf-8") as f:
        f.write(t)
    print(hashlib.sha256(t.encode("utf-8")).hexdigest(), sortie)


if __name__ == "__main__":
    main()
