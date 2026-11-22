#!/usr/bin/env python3
"""Assemble le brouillon 3 de la v11 à partir du brouillon 2.

Seul objet : porter le seuil de déclenchement de la recharge automatique de la clé LUC (5 USD, lu par Lazar à la console,
R-5042) et ce qu'il implique, et citer le devis v11b. Toute ligne du brouillon 2 qui n'est pas nommée ici est recopiée à
l'octet près ; aucune ligne n'est ajoutée ni retirée (les numéros de lignes de l'annexe du brouillon 2 restent justes).
Chaque remplacement exige que l'ancienne chaîne figure exactement une fois dans la ligne visée ; sinon le programme s'arrête.
Usage : python3 -I assembler-brouillon-3-preenregistrement-v11.py BROUILLON-2.md SORTIE.md DATE_UTC
"""
import hashlib
import sys

B1_SHA = "cde6b2d34ddaed05fb5bcd7308896dd0c955bf3d6c15d3db2c5dc99e9f0903f8"
B2_SHA = "4a7e430b81e1e5e3714725bf3c9884dfba75df94f295147bb0794c57e3eadf38"
DEVIS_V11_SHA = "34271cb3cb3dba89c897cc076f7a65cbf73630d96f7106f2f40adac9a2590d52"
CALCUL_V11_SHA = "deac25b6fe59332b646cd7b67580126221f3aa5f547623a6270c58b2330428ee"
DEVIS_V11B_SHA = "13d962b1c56f17235e1e4b90b9b166239c5bb6d0c1bb6c400b3f07ac59a88c03"
CALCUL_V11B_SHA = "cf316ba4db4005e2d64a114f4f4aea93187ebfa372a3bf072594e5513f8cd0e6"
ANNEXE_SHA = "abb967a9e2190f0ca607e8f136e1527105137d42c8225ed8f30a8234f9096b95"
ANCIEN = {"commit": "9a5f45db503b52b644185f4045b62c810989027c",
          "go": "ee1c9cec090b150c55cd26aa27c8b23303f5443a1caa5501c2ebfd43b7f0c17e",
          "decisions": "996cd20acc7ceb37d7279d2d093cec4b16c1a0a45af924ac13879a18289a855b"}
NEUF = {"commit": "61ec4bb16537d899d431fe7a74d10b0c17053d86",
        "go": "8f54197a90d07412e4d7e1aa38e482cea57b5429cb0d01d7eb35ab2a85f64453",
        "decisions": "d70dd20afbd5d3b746b1a74ad013a37fec05dde6b25429a67dce4542204855ab"}
N = "docs/notes/organisme-affinage-mentors-v1"

src, dst, date_utc = sys.argv[1], sys.argv[2], sys.argv[3]
brut = open(src, "rb").read()
assert hashlib.sha256(brut).hexdigest() == B2_SHA, "la source n'est pas le brouillon 2"
L = brut.decode("utf-8").split("\n")
assert L[-1] == "" and len(L) == 327, len(L)   # 326 lignes, fin de fichier par un saut de ligne
lignes = {i + 1: t for i, t in enumerate(L[:-1])}
touchees = set()


def sub(n, ancien, nouveau):
    assert lignes[n].count(ancien) == 1, (n, ancien[:70], lignes[n].count(ancien))
    lignes[n] = lignes[n].replace(ancien, nouveau)
    touchees.add(n)


def ajouter_fin(n, prefixe, texte):
    assert lignes[n].startswith(prefixe), (n, lignes[n][:80])
    lignes[n] = lignes[n] + texte
    touchees.add(n)


# ------------------------------------------------------------------------------------------------ en-tête
sub(3, "- **État de ce fichier : brouillon 2 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 1 "
       "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-1.md`, `" + B1_SHA + "`, qui reste en place, "
       "R12) après les décisions de la mère sur cette version (R-4995, R-5006, R-5007, R-5018) et les mots de Lazar inscrits "
       "en GO-2026-11-22-124.",
    "- **État de ce fichier : brouillon 3 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 2 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-2.md`, `" + B2_SHA + "`) et le brouillon 1 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-1.md`, `" + B1_SHA + "`), qui restent en place "
    "(R12), après les décisions de la mère sur cette version (R-4995, R-5006, R-5007, R-5018) et les mots de Lazar "
    "inscrits en GO-2026-11-22-124 et en R-5042 (seuil de recharge de la clé LUC ; seul objet du brouillon 3).")
sub(5, "- Date (UTC) de ce brouillon : 2026-11-22T19:53:46Z (`date -u +%FT%TZ`) ; brouillon 1 : 2026-11-22T18:54:51Z ;",
    "- Date (UTC) de ce brouillon : " + date_utc + " (`date -u +%FT%TZ`) ; brouillon 2 : 2026-11-22T19:53:46Z ; "
    "brouillon 1 : 2026-11-22T18:54:51Z ;")
sub(8, "recharge automatique de la clé, GO-2026-11-22-111 ;",
    "recharge automatique de la clé, GO-2026-11-22-111, et son seuil de déclenchement, 5 USD, lu par Lazar à la console, "
    "R-5042 ;")
for cle in ("commit", "go", "decisions"):
    sub(8, ANCIEN[cle], NEUF[cle])

# ------------------------------------------------------------------------------------------------ pièces
sub(22, "  - **devis v11** : `" + N + "/devis-course-affinage-mentors-v11.md`, `" + DEVIS_V11_SHA + "`, écrit pour cette "
        "version",
    "  - **devis v11b** : `" + N + "/devis-course-affinage-mentors-v11b.md`, `" + DEVIS_V11B_SHA + "` — c'est le devis v11 "
    "(`" + N + "/devis-course-affinage-mentors-v11.md`, `" + DEVIS_V11_SHA + "`) plus le seuil de recharge de la clé LUC "
    "(R-5042 ; § 5 bis), sans changement de chiffre ; dans ce texte, « devis v11 » désigne ce devis v11b ; écrit pour "
    "cette version")
sub(22, "`" + N + "/course-v11/calcul-devis-course-affinage-mentors-v11.py`, `" + CALCUL_V11_SHA + "`",
    "`" + N + "/course-v11/calcul-devis-course-affinage-mentors-v11b.py`, `" + CALCUL_V11B_SHA + "`")

# ------------------------------------------------------------------------------------------------ règle des clés, clé LUC
sub(133, "La clé est en compte payant à recharge automatique, et Lazar a dit la recharge disponible « jusqu'à 40 euros » "
         "(GO-2026-11-22-111).",
    "La clé est en compte payant à recharge automatique : Lazar a dit la recharge disponible « jusqu'à 40 euros » "
    "(GO-2026-11-22-111) et a lu à la console son seuil de déclenchement, 5 USD (R-5042).")
sub(135, "la recharge automatique (« jusqu'à 40 euros », GO-2026-11-22-111) est dite en euros,",
    "la recharge automatique (« jusqu'à 40 euros », GO-2026-11-22-111 ; seuil de déclenchement 5 USD, R-5042) est dite en "
    "euros,")
sub(140, "(iii) Le délai de la recharge automatique : ni son seuil de déclenchement ni son délai ne sont dans les pièces "
         "lues ; un refus de l'interface pendant ce délai arrête la course, alors que la recharge aurait pu couvrir la "
         "suite — conséquence dite de l'arrêt au premier refus.",
    "(iii) Le délai de la recharge automatique. Son seuil de déclenchement est de 5 USD, lu par Lazar à la console "
    "(R-5042) ; son délai, le montant de chaque recharge et ce qu'elle fait quand le solde est déjà sous le seuil ne sont "
    "dans aucune pièce lue. Un refus de l'interface pendant ce délai arrête la course, alors que la recharge aurait pu "
    "couvrir la suite — conséquence dite de l'arrêt au premier refus. Le seuil réduit ce risque sans l'annuler : si le "
    "solde est au-dessus de 5 USD, la recharge se déclenche quand il passe sous ce seuil, alors qu'il reste près de 5 USD, "
    "à un appel près ; aux prix par appel du devis, 5 USD font 15 appels du proposeur de la seconde espèce Claude (la "
    "course en compte 16), 36 de celui de la première (16), 162 de l'aiguilleur (160) ou 136 du juge Claude (160), soit un "
    "peu plus que tout l'aiguillage (4,96 USD) et 84 % de la part Claude des juges (5,92 USD) : à ces prix, le refus "
    "n'arrive pendant le délai que si la recharge tarde à l'échelle d'une étape entière, ou n'aboutit pas. Trois cas "
    "restent entiers : des sessions près de leur plafond (5 USD font deux sessions de proposeur à 3,00 USD, cinq de juge à "
    "1,00 USD, vingt d'aiguilleur à 0,25 USD) ; un solde déjà sous 5 USD au départ, qui n'est pas lu (la marge est alors ce "
    "solde) ; une recharge qui échoue ou qui a épuisé ses 40 euros (devis v11, § 5 bis).")
ajouter_fin(142, "Condition de GO-2026-11-18-14 (« Lazar prévenu avant qu'une clé n'atteigne zéro »)",
            " Le seuil de recharge de 5 USD (R-5042) rend ce cas moins probable, sans l'exclure (point 6).")

# ------------------------------------------------------------------------------------------------ différentiel v10 → v11
sub(284, "limites de la garde écrites (refus sous un statut 200, dépassement du relais, délai de la recharge, autres "
         "dépenses sur la clé)",
    "limites de la garde écrites (refus sous un statut 200, dépassement du relais, délai de la recharge — dont le seuil de "
    "déclenchement est de 5 USD, lu par Lazar à la console, R-5042 —, autres dépenses sur la clé)")
sub(290, "10. **Devis v11** (écrit pour cette version, à contre-lire) :",
    "10. **Devis v11b** (écrit pour cette version, à contre-lire ; le devis v11 plus le seuil de recharge de la clé LUC) :")

# ------------------------------------------------------------------------------------------------ dernière section
sub(310, "à trancher avec qui écrit la commande d'Argon, avant de sceller la configuration v11.",
    "la session de l'organisme a retenu, le 22 novembre, que la valeur suivra la convention que le développeur implante "
    "dans la commande d'Argon ; elle est à inscrire avant de sceller la configuration v11, et 1,10 USD demande un devis et "
    "un texte à ce chiffre.")
sub(311, "ferait sous-compter la dépense ; à confirmer.",
    "ferait sous-compter la dépense ; retenu par la session de l'organisme le 22 novembre (routine, étage 1).")
sub(316, "La liste phrase par phrase est dans `course-v11/phrases-du-brouillon-2-qui-supposent-une-garde-du-lanceur-v11.md` ; "
         "en résumé :",
    "La liste phrase par phrase est dans `course-v11/phrases-du-brouillon-2-qui-supposent-une-garde-du-lanceur-v11.md` (`"
    + ANNEXE_SHA + "`), écrite sur le brouillon 2 : elle vaut ligne pour ligne pour ce brouillon 3, qui ne change aucune "
    "phrase supposant une garde du lanceur ; en résumé :")
ajouter_fin(326, "Du brouillon 1 au brouillon 2 :",
            " Du brouillon 2 au brouillon 3 : seuil de déclenchement de la recharge automatique de la clé LUC, 5 USD, lu "
            "par Lazar à la console (R-5042), porté au § Règle des clés avec ce qu'il implique, et au devis v11b ; rien "
            "d'autre.")

texte = "\n".join(lignes[n] for n in range(1, 327)) + "\n"
assert texte.count("\n") == 326
open(dst, "w", encoding="utf-8", newline="\n").write(texte)
print(hashlib.sha256(texte.encode("utf-8")).hexdigest(), dst)
print("lignes du brouillon 2 touchées :", sorted(touchees))
