#!/usr/bin/env python3
"""Fabrique `ordre-etalonnage-ii-b-v5-brouillon3.md` depuis le brouillon 2 : règle de la coupure à 12 USD, treizième correctif.

Usage : python3 -I -B fabriquer-ordre-etalonnage-ii-b-v5-brouillon3-v1.py RACINE_DU_DEPOT DOSSIER DATE

Méthode : empreinte du brouillon 2 vérifiée ; empreintes et compagnons des pièces neuves vérifiés dans le dépôt ; chaque
changement est un remplacement dont l'ancre est trouvée le nombre de fois attendu, sinon rien n'est écrit ; la table des champs
est comparée aux champs restés dans le texte. Écrit le brouillon 3, la note des différences (une par ligne), leurs compagnons.
Il n'écrase rien (R12). Aucun réseau.
"""
import hashlib
import re
import sys
from pathlib import Path

B2 = "ordre-etalonnage-ii-b-v5-brouillon2.md"
B2_SHA = "adf8dbacdfe533148a279ecde23a71d090ad349a564af555826ae55415ef6795"
B3 = "ordre-etalonnage-ii-b-v5-brouillon3.md"
NOTE = "differences-ordre-etalonnage-v5-brouillon2-vers-3-v1.md"
C = "brouillons/ii-b-saboteur-budget-v5/code-v5/"
TETE_2, ARBRE_2 = "45f9ba7aaca27fdab8a458072f883825991dd2fb", "9917b13f3c57d0eeacf3b72fea9607a103da4f11"
TETE, ARBRE = "c4b5115b5fe6ed679eeb61e08c779317f9cb55c5", "ed9b0e48be367670cad0782ccb6fbe2d9ca41b87"
P10 = "d2c339b5b4542c9850edaf2942a8555bdb12da28f9bbb4cfcb06393ac61a7691"
V89 = "350b4c613c50f8b78a234957d5a9103bf9b09e3688564c528e97fbd98b513669"
NOTE_V5 = "8dee53473d689e716c4818a47ad03ce80620c7a39df67ea03623706c2f99703f"
REP3 = "033f042e6ffa3d8b05194276529bf2e2171a4cd70befd81acdad7d253fe2c191"
ESSAIS5 = "b2a766b0f363fc784eb99804143319432f2367265935f8221bc1568b4dee9e2d"
LANCEUR_2, LANCEUR = "5fd1105c2ae3575b10087fbb90ad7baec30480f909055b40d343e82dd4aa7d54", "42d295c83a911d021472d2b7f4237985aee4f2cc5c8b3d0d7695e2e92754706a"
PIECES = {
    C + "correctifs-v5/0010-Organisme-retenu-du-saboteur-budget-code-en-version-.patch": P10,
    C + "contre-lecture-cl1/note-verification-0008-0009-cl1-v1.md": V89,
    C + "rapport-developpeur-code-organisme-retenu-v5-v5-note.md": NOTE_V5,
    C + "sortie-repetition-locale-v3.txt": REP3,
    C + "sortie-essais-cibles-v5-v5.txt": ESSAIS5,
}
CODE_LU_2 = "(arbre `" + ARBRE_2 + "`) ; aucun essai rejoué, aucun modèle chargé."

# (nom, ancre, texte neuf, compte attendu), appliqués dans l'ordre.
CHANGEMENTS = [
    ("mise à l'abri de la phrase « code lu » du brouillon 2", "tête locale du développeur, `" + TETE_2 + "`, dont l'objet est dans le dépôt local " + CODE_LU_2,
     "tête locale d'alors du développeur, `@@T2@@`, dont l'objet est dans le dépôt local (arbre `@@A2@@`) ; aucun essai rejoué, aucun modèle chargé. **Au brouillon 3** : tête locale `" + TETE + "`, arbre `" + ARBRE + "`, objet présent dans le dépôt local et relu par `git show` ; le correctif 0010 ne change, parmi ces fichiers, que le lanceur de session (`" + LANCEUR + "`) ; l'amorce, la liste figée, le gabarit et le module de lecture gardent leurs empreintes ; lus : la note v5 du développeur et la note de vérification courte des correctifs 0008 et 0009, en entier ; le correctif 0010 lui-même n'a pas été relu ligne à ligne.", 1),
    ("nombre de correctifs", "douze", "treize", 5),
    ("phrase « code lu » du brouillon 2, nombre d'alors", "**Au brouillon 2** : les treize correctifs du § 11 appliqués", "**Au brouillon 2** : les douze premiers correctifs du § 11 appliqués", 1),
    ("tête du code", TETE_2, TETE, 2),
    ("arbre du code", ARBRE_2, ARBRE, 5),
    ("retour de la phrase « code lu »", "@@T2@@", TETE_2, 1),
    ("retour de la phrase « code lu », arbre", "@@A2@@", ARBRE_2, 1),
    ("titre", "machine à part — brouillon 2\n", "machine à part — brouillon 3\n", 1),
    ("statut", "- **Statut** : **brouillon 2**, pièce décisive (ordre d'une course payante), non contre-lu. Fabriqué par programme",
     "- **Statut** : **brouillon 3**, pièce décisive (ordre d'une course payante), non contre-lu. Fabriqué par programme (`fabriquer-ordre-etalonnage-ii-b-v5-brouillon3-v1.py`) depuis le brouillon 2 (`" + B2 + "`, `" + B2_SHA + "`, intact, R12), le @@DATE@@, par le même rédacteur, sous le même mandat, sur le message de la session de reconception : il écrit la règle de la coupure propre de l'étalonnage (correctif 0010), porte le code à sa tête neuve, 271 essais et la vérification courte des correctifs 0008 et 0009 ; rien d'autre ne change ; différences, une par ligne : `" + NOTE + "`. Le brouillon 2 avait été fabriqué par programme", 1),
    ("pièces citées, ajouts", "La contre-lecture du distillateur n'a pas été ouverte : le distillateur ne sert pas à l'étalonnage.",
     "La contre-lecture du distillateur n'a pas été ouverte : le distillateur ne sert pas à l'étalonnage. **Au brouillon 3** (empreintes et compagnons vérifiés par le programme) : correctif 0010 (`" + P10 + "`) ; note v5 du développeur, `" + C + "rapport-developpeur-code-organisme-retenu-v5-v5-note.md` (`" + NOTE_V5 + "`) ; note de vérification courte des correctifs 0008, du distillateur et 0009, `" + C + "contre-lecture-cl1/note-verification-0008-0009-cl1-v1.md` (`" + V89 + "`) : « étalonnage autorisable » ; répétition locale `sortie-repetition-locale-v3.txt` (`" + REP3 + "`) ; sortie d'essais `sortie-essais-cibles-v5-v5.txt` (`" + ESSAIS5 + "`).", 1),
    ("§ 1, vérifications du code",
     "(correctif 0007) ; vérification courte des correctifs 0008 et 0009, en cours : `<<VERIFICATION_COURTE_CORRECTIFS_0008_0009>>`.",
     "(correctif 0007) ; vérification courte des correctifs 0008, du distillateur et 0009 : `" + C + "contre-lecture-cl1/note-verification-0008-0009-cl1-v1.md` (`" + V89 + "`), « étalonnage autorisable », même arbre que la tête d'alors ; vérification courte du correctif 0010, en cours : `<<VERIFICATION_COURTE_CORRECTIF_0010>>`.", 1),
    ("§ 1, essais attendus", "**267 essais attendus** : « 267 passed in 415.80s (0:06:55) » à la tête du code, sur processeur (`sortie-essais-cibles-v5-v4.txt`)",
     "**271 essais attendus** : 271 réussis à la tête du code, sur processeur (`sortie-essais-cibles-v5-v5.txt`) ; la liste figée ne change pas, le correctif 0010 ajoute quatre essais à un fichier qu'elle porte déjà (267 avant lui)", 1),
    ("dernière ligne attendue des essais", "« `267` passed »", "« `271` passed »", 2),
    ("variable du nombre d'essais", "`IIB_TESTS_ATTENDUS=267`", "`IIB_TESTS_ATTENDUS=271`", 1),
    ("§ 1, coupure propre", "| Coupure propre de l'étalonnage | 12 USD de dépense relevée, par une règle de la surveillance (§ 3, § 5 étape 3) ;",
     "| Coupure propre de l'étalonnage | 12 USD de dépense comptée depuis le début de l'amorce, au prix de la carte et du stockage lus à la création, par une règle de la surveillance (§ 3, § 5 étape 3) ;", 1),
    ("§ 3, règle à 12 USD",
     "règle de la surveillance à 12 USD, forme `<<REGLE_COUPURE_ETALONNAGE_FORME_ET_ESSAIS>>` ; **son essai sur un cas sain (dépense sous 12 USD : aucune alerte) et sur un artefact (dépense à 12 USD avant la fin de l'étalonnage : alerte, commande d'arrêt par l'identifiant imprimée) est joué et consigné avant la création** ; sans cet essai, aucune création. À la tête du code, cette règle n'est écrite nulle part (rapport v2 du développeur, § 4 point 3 ; note v4, reste 4) : la surveillance du lanceur de session ne coupe qu'au plafond de la configuration, 55 USD.",
     "règle de la surveillance à 12 USD, écrite par le correctif 0010 : sous-commande `coupure-etalonnage` de `session_v5`, appelée par la surveillance de `scripts/lancer_iib_v3.sh` (12 lignes ajoutées, aucune changée) ; l'amorce et sa minuterie ne sont pas touchées. **Ce qu'elle fait** : à chaque relevé, après la garde de dépense de la ligne à 55 USD, qui reste et prime, si la phase est l'étalonnage et que la dépense comptée atteint 12 USD : alerte dans `surveillance.txt`, motif dans `coupure-etalonnage.txt` (copie datée, avec empreinte, aux traces de la location), journaux de fin de surveillance copiés, ligne « ARRET coupure de l'étalonnage : … », commande d'arrêt par l'identifiant imprimée, **code de sortie 3**. **Dépense comptée** : (maintenant − début de l'amorce) × (prix de la carte + prix du stockage lus à la création) ; si le début de l'amorce n'est pas relevé, ou s'il précède la création, le compte part de la création ; un second démarrage ne le remet pas à zéro ; le forfait de téléchargement et la dépense antérieure n'y entrent pas. La fin du run prime : étalonnage fini au-delà de 12 USD, « FIN », pas de coupure. **Phase illisible : arrêt**, aucun repli silencieux ; hors de l'étalonnage, la règle ne joue pas. **Essais (R5), dans la liste figée** : cas sain (8 heures, 11,04 USD : poursuite, aucun fichier de motif) ; artefact (9 heures, 12,42 USD : code 3, alerte, motif écrit et copié, arrêt nommé par l'identifiant) ; autre phase ; phase illisible ; la coupure de la ligne à 55 reste (note v5 du développeur, § 3). **Ces essais sont rejoués par l'exécutante aux contrôles à blanc, avant la création** (§ 4 étape 6) ; sans eux, aucune création. La surveillance n'arrête ni ne détruit rien elle-même : c'est l'exécutante qui agit (§ 5 étape 3). Non éprouvés : la règle sur une vraie machine et un vrai journal du loueur ; le décalage d'horloge entre la machine et le poste.", 1),
    ("§ 4, vérifications",
     "**Reste : la vérification courte des correctifs 0008 et 0009 par le même contre-lecteur**, `<<VERIFICATION_COURTE_CORRECTIFS_0008_0009>>` ; sans elle, pas de scellement.",
     "Vérification courte des correctifs 0008, du distillateur et 0009 par le même contre-lecteur (`" + V89 + "`) : **« étalonnage autorisable »**, R1 et R2 levés, répétition locale rejouée par lui, même arbre que la tête d'alors. Le correctif 0010 écrit la règle de la coupure propre (§ 3). **Reste : la vérification courte du correctif 0010 par le même contre-lecteur**, `<<VERIFICATION_COURTE_CORRECTIF_0010>>` ; sans elle, pas de scellement.", 1),
    ("§ 4, répétition locale", "amorce en version 5 (267 essais), étalonnage versé par lot et poussé, destruction par l'identifiant, conditions et désignation, second passage refusé : réussie, code 0 (`sortie-repetition-locale-v2.txt`).",
     "amorce en version 5 (271 essais), étalonnage versé par lot et poussé, surveillance qui lit « phase etalonnage » et finit par « FIN », destruction par l'identifiant, conditions et désignation, second passage refusé : réussie, code 0, à la tête du code (`sortie-repetition-locale-v3.txt`).", 1),
    ("§ 4, cas de clé en gras", "les cas du correctif 0008 attendent la vérification courte.", "les cas du correctif 0008 sont levés par la vérification courte.", 1),
    ("§ 5, empreinte du lanceur de session", "(`" + LANCEUR_2 + "` à la tête du code) : la version 2 avec sept lignes changées (",
     "(`" + LANCEUR + "` à la tête du code) : la version 2 avec sept lignes changées, plus les 12 lignes de la règle de la coupure propre dans la surveillance (", 1),
    ("§ 5, règle à 12 USD",
     "**Règle à 12 USD** : si la dépense relevée atteint 12 USD avant la ligne de fin de l'étalonnage, la surveillance alerte ; l'exécutante arrête la machine par son identifiant avec la commande imprimée, ne relance rien, passe à l'étape 5 et rend la main à la mère : **nœud**.",
     "**Règle à 12 USD** : si la dépense comptée atteint 12 USD avant la fin de l'étalonnage, la surveillance écrit l'alerte et le motif, imprime la ligne « ARRET coupure de l'étalonnage : … » et la commande d'arrêt par l'identifiant, et sort en code 3. **Comme pour la coupure de la ligne à 55 USD, c'est l'exécutante qui agit** : elle arrête la machine par son identifiant avec la commande imprimée, rapatrie ce qui est versé (les lots poussés sur la branche ; étape 5), puis détruit par la sous-commande `destruction` et ses gardes (étape 7) ; elle ne relance rien et rend la main à la mère : **nœud**. Si la surveillance ne tourne pas, la règle ne joue pas, et la machine coûte jusqu'à la minuterie de la ligne : la surveillance est relancée dès qu'elle s'arrête.", 1),
    ("§ 6, dépense", "- **Dépense** : 12 USD relevés avant la fin de l'étalonnage : arrêt par l'identifiant, nœud ;",
     "- **Dépense** : 12 USD comptés avant la fin de l'étalonnage : code 3 de la surveillance, arrêt par l'identifiant, rapatriement, destruction, nœud ;", 1),
    ("§ 11, correctif ajouté",
     "| `correctifs-v4/0009-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` (rang 12) | `4287a6889061c921886582ff3a7ebffecd4bd67fcbb4556b102e9eb9e2737661` |",
     "| `correctifs-v4/0009-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` (rang 12) | `4287a6889061c921886582ff3a7ebffecd4bd67fcbb4556b102e9eb9e2737661` |\n| `correctifs-v5/0010-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` (rang 13) | `" + P10 + "` |", 1),
    ("§ 11, rangs", "les lignes 7 à 12 sont sous", "les lignes 7 à 13 sont sous", 1),
    ("§ 11, champ de la règle retiré de la table", "| `<<REGLE_COUPURE_ETALONNAGE_FORME_ET_ESSAIS>>` | forme exacte de la règle de la surveillance à 12 USD, et pièce de son essai sur un cas sain et sur un artefact ; elle n'est pas écrite dans le code à sa tête | session de reconception |\n", "", 1),
    ("§ 11, champ de la vérification courte remplacé",
     "| `<<VERIFICATION_COURTE_CORRECTIFS_0008_0009>>` | chemin, empreinte et verdict de la vérification courte des correctifs 0008 et 0009 par le même contre-lecteur | session de reconception |",
     "| `<<VERIFICATION_COURTE_CORRECTIF_0010>>` | chemin, empreinte et verdict de la vérification courte du correctif 0010 par le même contre-lecteur | session de reconception |", 1),
    ("§ 12, point 8",
     "elle n'est écrite dans aucun code à la tête. Elle reste un champ : sa forme et son essai sont à fournir avant le scellement.",
     "écrite par le correctif 0010 (§ 3). Deux lectures du développeur, à juger par la mère : la dépense est comptée depuis le début de l'amorce, au prix lu à la création, sans le forfait de téléchargement ni le temps entre la création et l'amorce, alors que le devis écrit « dépense relevée » ; et la surveillance ne fait qu'imprimer l'arrêt. Après la coupure, cet ordre fait détruire la machine par l'exécutante, comme le demande la session de reconception ; le devis écrivait « arrête la machine par son identifiant, et c'est un nœud » et comptait 48 heures de stockage à l'arrêt.", 1),
]


def sha(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def ecrire(chemin: Path, texte: str) -> str:
    if chemin.exists() or Path(str(chemin) + ".sha256").exists():
        sys.exit(f"{chemin} existe déjà : refus d'écraser (R12)")
    chemin.write_bytes(texte.encode("utf-8"))
    e = sha(chemin)
    Path(str(chemin) + ".sha256").write_text(f"{e}  {chemin.name}\n", encoding="utf-8")
    return e


def main(argv) -> int:
    if len(argv) != 4:
        sys.exit("usage : RACINE_DU_DEPOT DOSSIER DATE")
    racine, dossier, date = Path(argv[1]), Path(argv[2]), argv[3]
    if sha(dossier / B2) != B2_SHA:
        sys.exit("brouillon 2 : empreinte différente de celle attendue")
    for chemin, attendue in PIECES.items():
        if sha(racine / chemin) != attendue or (racine / (chemin + ".sha256")).read_text(encoding="utf-8").split()[0] != attendue:
            sys.exit(f"pièce citée {chemin} : empreinte ou compagnon différents")
    texte = (dossier / B2).read_text(encoding="utf-8")
    avant = set(re.findall(r"<<([A-Z0-9_]+)>>", texte))
    lignes = []
    for nom, ancre, neuf, compte in CHANGEMENTS:
        n = texte.count(ancre)
        if n != compte:
            sys.exit(f"changement « {nom} » : ancre trouvée {n} fois, {compte} attendu : {ancre[:80]!r}")
        neuf = neuf.replace("@@DATE@@", date)
        texte = texte.replace(ancre, neuf)
        a, b = " ".join(ancre.split()), " ".join(neuf.split())
        lignes.append(f"- {nom} ({compte} fois) : « {a[:110]}{'…' if len(a) > 110 else ''} » remplacé par « {b[:260]}{'…' if len(b) > 260 else ''} ».")
    if "@@" in texte:
        sys.exit("un jeton n'a pas été rempli")
    apres = re.findall(r"<<([A-Z0-9_]+)>>", texte)
    table = set(re.findall(r"^\| `<<([A-Z0-9_]+)>>` \|", texte, flags=re.M))
    if set(apres) != table:
        sys.exit(f"champs du texte et table des champs différents : {sorted(set(apres) ^ table)}")
    for interdit in ("267 essais", "`267`", "ATTENDUS=267", "REGLE_COUPURE", "0008_0009>>", LANCEUR_2, "sortie-repetition-locale-v2.txt`)."):
        if interdit in texte:
            sys.exit(f"reste inattendu : {interdit}")
    e3 = ecrire(dossier / B3, texte)
    note = ["# Différences — ordre de l'étalonnage de l'organisme retenu, du brouillon 2 au brouillon 3 — v1", "",
            f"Source : `{B2}` (`{B2_SHA}`). Produit : `{B3}` (`{e3}`). Écrite par le programme `fabriquer-ordre-etalonnage-ii-b-v5-brouillon3-v1.py`, le {date}. Une différence par ligne ; tout le reste est recopié à l'octet.", "",
            "## Remplacements, un par ligne (ancre trouvée le nombre de fois attendu)", ""] + lignes
    note += ["", "## Champs, un par ligne", ""]
    note += [f"- champ `<<{n}>>` retiré : rempli." for n in sorted(avant - table)]
    note += [f"- champ `<<{n}>>` ajouté." for n in sorted(table - avant)]
    note += [f"- champ `<<{n}>>` gardé." for n in sorted(table & avant)]
    note += ["", "## Pièces dont l'empreinte et le compagnon ont été vérifiés avant l'écriture, une par ligne", ""] + [f"- `{c}` : `{e}`." for c, e in PIECES.items()]
    e_note = ecrire(dossier / NOTE, "\n".join(note) + "\n")
    print(f"brouillon 3 : {e3} ; {len(texte)} caractères ; {len(CHANGEMENTS)} remplacements ; champs restants : {sorted(table)}")
    print(f"note des différences : {e_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
