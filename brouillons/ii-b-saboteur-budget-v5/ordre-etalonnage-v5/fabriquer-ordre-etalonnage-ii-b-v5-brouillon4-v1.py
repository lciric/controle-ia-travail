#!/usr/bin/env python3
"""Fabrique `ordre-etalonnage-ii-b-v5-brouillon4.md` depuis le brouillon 3 : vérification courte du correctif 0010 citée,
dépassement déclaré à la coupure de 12 USD, aucune destruction après cette coupure sans le mot de la mère, surveillance continue.

Usage : python3 -I -B fabriquer-ordre-etalonnage-ii-b-v5-brouillon4-v1.py RACINE_DU_DEPOT DOSSIER DATE

Méthode : empreinte du brouillon 3 vérifiée ; empreinte et compagnon de la pièce neuve vérifiés ; chaque changement est un
remplacement dont l'ancre est trouvée le nombre de fois attendu, sinon rien n'est écrit ; la table des champs est comparée aux
champs restés dans le texte. Écrit le brouillon 4, la note des différences (une par ligne), leurs compagnons ; n'écrase rien (R12).
"""
import hashlib
import re
import sys
from pathlib import Path

B3 = "ordre-etalonnage-ii-b-v5-brouillon3.md"
B3_SHA = "4bad49e2e0c441560ac0a147a9f7de0fe7012a6f9b7d2eb63d7dac622e247cb1"
B4 = "ordre-etalonnage-ii-b-v5-brouillon4.md"
NOTE = "differences-ordre-etalonnage-v5-brouillon3-vers-4-v1.md"
V10_CHEMIN = "brouillons/ii-b-saboteur-budget-v5/code-v5/contre-lecture-cl1/note-verification-0010-cl1-v1.md"
V10 = "ffe2e02454af73b8810e56256645665e198a60503e396d7ca2239859cf21ef5a"
PIECES = {V10_CHEMIN: V10}
CITE = "`" + V10_CHEMIN + "` (`" + V10 + "`), « étalonnage autorisable », même arbre que celui du § 1, répétition locale rejouée par le contre-lecteur (271 essais), deux mineurs que l'ordre déclare (§ 3 : origine du compte, phrase du motif)"

CHANGEMENTS = [
    ("titre", "machine à part — brouillon 3\n", "machine à part — brouillon 4\n", 1),
    ("statut", "- **Statut** : **brouillon 3**, pièce décisive (ordre d'une course payante), non contre-lu. Fabriqué par programme",
     "- **Statut** : **brouillon 4**, pièce décisive (ordre d'une course payante), non contre-lu. Fabriqué par programme (`fabriquer-ordre-etalonnage-ii-b-v5-brouillon4-v1.py`) depuis le brouillon 3 (`" + B3 + "`, `" + B3_SHA + "`, intact, R12), le @@DATE@@, par le même rédacteur, sous le même mandat, sur le message de la session de reconception : il cite la vérification courte du correctif 0010 et applique trois décisions de cette session sur la coupure propre de l'étalonnage, sans toucher au code (dépassement déclaré ; aucune destruction après la coupure sans le mot de la mère ; surveillance sans interruption) ; rien d'autre ne change ; différences, une par ligne : `" + NOTE + "`. Le brouillon 3 avait été fabriqué par programme", 1),
    ("pièces citées, ajout", "sortie d'essais `sortie-essais-cibles-v5-v5.txt` (`b2a766b0f363fc784eb99804143319432f2367265935f8221bc1568b4dee9e2d`).",
     "sortie d'essais `sortie-essais-cibles-v5-v5.txt` (`b2a766b0f363fc784eb99804143319432f2367265935f8221bc1568b4dee9e2d`). **Au brouillon 4** (empreinte et compagnon vérifiés par le programme) : note de vérification courte du correctif 0010, " + CITE + " ; le rédacteur en a lu le verdict, la description de la règle et le premier des deux points sur le brouillon 3.", 1),
    ("§ 1, vérification courte du correctif 0010", "vérification courte du correctif 0010, en cours : `<<VERIFICATION_COURTE_CORRECTIF_0010>>`.",
     "vérification courte du correctif 0010 : `" + V10 + "`, « étalonnage autorisable ».", 1),
    ("§ 3, déclarations sur la coupure propre", "La surveillance n'arrête ni ne détruit rien elle-même : c'est l'exécutante qui agit (§ 5 étape 3).",
     "La surveillance n'arrête ni ne détruit rien elle-même : c'est l'exécutante qui agit (§ 5 étape 3). **Écart déclaré au devis** (qui écrit « dépense relevée ») : au moment de la coupure, la dépense réelle dépasse 12 USD d'environ 0,1 à 0,4 USD — le temps entre la création et le début de l'amorce (environ 0,1 USD pour cinq minutes à 1,38 USD l'heure), un intervalle de surveillance de 60 secondes au plus (0,02 USD), la réaction de la session (environ 0,23 USD par dix minutes) ; elle reste sous les 16,76 USD que tiennent les gardes (décision de la session de reconception, d'après la vérification courte du correctif 0010, point 1 ; le code n'est pas touché). **Phrase du motif neutralisée** : le motif écrit par le code dit d'arrêter la machine « puis la détruire » ; sous cet ordre, l'exécutante ne détruit pas sur ce motif (§ 5 étape 3).", 1),
    ("§ 4, vérification courte du correctif 0010",
     "**Reste : la vérification courte du correctif 0010 par le même contre-lecteur**, `<<VERIFICATION_COURTE_CORRECTIF_0010>>` ; sans elle, pas de scellement.",
     "Vérification courte du correctif 0010 par le même contre-lecteur (`" + V10 + "`) : **« étalonnage autorisable »** ; ses deux mineurs sont déclarés par cet ordre (§ 3), le code n'est pas changé. Aucune vérification du code ne reste ouverte pour l'étalonnage.", 1),
    ("§ 5, après la coupure à 12 USD",
     "**Comme pour la coupure de la ligne à 55 USD, c'est l'exécutante qui agit** : elle arrête la machine par son identifiant avec la commande imprimée, rapatrie ce qui est versé (les lots poussés sur la branche ; étape 5), puis détruit par la sous-commande `destruction` et ses gardes (étape 7) ; elle ne relance rien et rend la main à la mère : **nœud**. Si la surveillance ne tourne pas, la règle ne joue pas, et la machine coûte jusqu'à la minuterie de la ligne : la surveillance est relancée dès qu'elle s'arrête.",
     "**C'est l'exécutante qui agit, et l'ordre suit le devis** : dès le code 3, elle arrête la machine par son identifiant avec la commande imprimée, rapatrie ce qui est versé (les lots poussés sur la branche ; étape 5), ne relance rien et rend la main à la mère : **nœud ; aucune destruction sans le mot de la mère**, même si le motif écrit par le code dit « puis la détruire » ; stockage à l'arrêt 48 heures au plus (étape 7). **L'exécutante surveille sans interruption pendant tout l'étalonnage** : la surveillance est relancée à l'identique dès qu'elle s'arrête sans `ARRET` ni `FIN`, et l'arrêt est exécuté dès le code 3. Si la surveillance tombe, la règle ne joue pas : c'est alors la minuterie de la ligne, à 55 USD, qui coupe.", 1),
    ("§ 6, dépense", "code 3 de la surveillance, arrêt par l'identifiant, rapatriement, destruction, nœud ;",
     "code 3 de la surveillance, arrêt par l'identifiant, rapatriement de ce qui est versé, nœud, aucune destruction sans le mot de la mère ;", 1),
    ("§ 11, champ retiré de la table", "| `<<VERIFICATION_COURTE_CORRECTIF_0010>>` | chemin, empreinte et verdict de la vérification courte du correctif 0010 par le même contre-lecteur | session de reconception |\n", "", 1),
    ("§ 12, point 8",
     "Deux lectures du développeur, à juger par la mère : la dépense est comptée depuis le début de l'amorce, au prix lu à la création, sans le forfait de téléchargement ni le temps entre la création et l'amorce, alors que le devis écrit « dépense relevée » ; et la surveillance ne fait qu'imprimer l'arrêt. Après la coupure, cet ordre fait détruire la machine par l'exécutante, comme le demande la session de reconception ; le devis écrivait « arrête la machine par son identifiant, et c'est un nœud » et comptait 48 heures de stockage à l'arrêt.",
     "Deux points du brouillon 3, décidés par la session de reconception sans toucher au code : le dépassement de la dépense réelle au moment de la coupure est déclaré (§ 3) ; après la coupure, l'ordre suit le devis : arrêt par l'identifiant, rapatriement, nœud, aucune destruction sans le mot de la mère (§ 5 étape 3). La règle ne joue que si la surveillance tourne.", 1),
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
    if sha(dossier / B3) != B3_SHA:
        sys.exit("brouillon 3 : empreinte différente de celle attendue")
    for chemin, attendue in PIECES.items():
        if sha(racine / chemin) != attendue or (racine / (chemin + ".sha256")).read_text(encoding="utf-8").split()[0] != attendue:
            sys.exit(f"pièce citée {chemin} : empreinte ou compagnon différents")
    texte = (dossier / B3).read_text(encoding="utf-8")
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
    table = set(re.findall(r"^\| `<<([A-Z0-9_]+)>>` \|", texte, flags=re.M))
    apres = set(re.findall(r"<<([A-Z0-9_]+)>>", texte))
    if apres != table:
        sys.exit(f"champs du texte et table des champs différents : {sorted(apres ^ table)}")
    for interdit in ("puis détruit par la sous-commande", "rapatriement, destruction, nœud", "CORRECTIF_0010>>"):
        if interdit in texte:
            sys.exit(f"reste inattendu : {interdit}")
    e4 = ecrire(dossier / B4, texte)
    note = ["# Différences — ordre de l'étalonnage de l'organisme retenu, du brouillon 3 au brouillon 4 — v1", "",
            f"Source : `{B3}` (`{B3_SHA}`). Produit : `{B4}` (`{e4}`). Écrite par le programme `fabriquer-ordre-etalonnage-ii-b-v5-brouillon4-v1.py`, le {date}. Une différence par ligne ; tout le reste est recopié à l'octet.", "",
            "## Remplacements, un par ligne (ancre trouvée le nombre de fois attendu)", ""] + lignes
    note += ["", "## Champs, un par ligne", ""]
    note += [f"- champ `<<{n}>>` retiré : rempli." for n in sorted(avant - table)]
    note += [f"- champ `<<{n}>>` gardé." for n in sorted(table)]
    note += ["", "## Pièce dont l'empreinte et le compagnon ont été vérifiés avant l'écriture", ""] + [f"- `{c}` : `{e}`." for c, e in PIECES.items()]
    e_note = ecrire(dossier / NOTE, "\n".join(note) + "\n")
    print(f"brouillon 4 : {e4} ; {len(CHANGEMENTS)} remplacements ; champs restants : {sorted(table)}")
    print(f"note des différences : {e_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
