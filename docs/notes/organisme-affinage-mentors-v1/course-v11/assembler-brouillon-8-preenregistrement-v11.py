#!/usr/bin/env python3
"""Assemble le brouillon 8 de la v11 à partir du brouillon 7.

Objet, sur le message de la session de l'organisme du 23 novembre 2026 daté 06:05Z : ses décisions datées 05:58Z sont
inscrites au registre des décisions de `main` sous R-5140 (complément de R-5132 : mesure bornée par 10,50 USD au pire, au plus
onze envois ; fiche du juge ; condition `hypothese_sortie_maximale_tenue` ; mesure jouée dès le scellement) ; R-5140 est mis
aux quatre emplacements « RÉFÉRENCE À INSCRIRE » et cité là où le brouillon 7 disait « réponses datées 05:58Z » ; son point (d)
est porté au texte (la mesure se joue dès le scellement). Le devis v11f vaut tel quel. Aucun chiffre ne change.
Les lignes 1 à 295 du brouillon 7 gardent leur numéro ; le point 16 du différentiel v10 → v11 (ligne 296) et la dernière
section (à retirer de la version scellée) sont repris avec des remplacements exacts, chacun exigé une fois ; sinon le
programme s'arrête.
Écrit par Opus 5.5 en effort maximal (GO-2026-11-22-145 ; écart à R-3735 et à GO-2026-11-21-75 déclaré dans le brouillon).
Usage : python3 -I assembler-brouillon-8-preenregistrement-v11.py BROUILLON-7.md SORTIE.md DATE_UTC
"""
import hashlib
import sys

B7_SHA = "f14bbcd1e1e6849c3d44922dc388eeb006031c22cc9ba9b3cbaa455c90d07f6c"
LU_B8 = {"commit": "903f4bfc0e7fba8fb6106c7da68a9ab787b918ee",
         "go": "7924a96ae41d632bfef3a19a046e5422ba9c30886ea424cb802c8aa6173267c3",
         "decisions": "cae0a53c9922ba7d135bb470c45a451f0e909b785a1a24a3cbe0ae3ee2230b55"}
REF7 = "RÉFÉRENCE À INSCRIRE : ligne du registre des décisions qui les porte"

src, dst, date_utc = sys.argv[1], sys.argv[2], sys.argv[3]
brut = open(src, "rb").read()
assert hashlib.sha256(brut).hexdigest() == B7_SHA, "la source n'est pas le brouillon 7"
L = brut.decode("utf-8").split("\n")
assert L[-1] == "" and len(L) == 334, len(L)   # 333 lignes, fin de fichier par un saut de ligne
lignes = {i + 1: t for i, t in enumerate(L[:-1])}
assert lignes[296].startswith("16. **Mesure préalable de la réflexion d'Argon**") and lignes[297] == ""
assert lignes[298].startswith("## Emplacements et points à trancher avant le scellement") and lignes[332] == ""
assert lignes[333].startswith("Du brouillon 1 au brouillon 2 :") and "Du brouillon 6 au brouillon 7" in lignes[333]
touchees = set()


def sub(n, ancien, nouveau, fois=1):
    assert lignes[n].count(ancien) == fois, (n, ancien[:80], lignes[n].count(ancien))
    lignes[n] = lignes[n].replace(ancien, nouveau)
    touchees.add(n)


# ------------------------------------------------------------------------------------------------ en-tête
sub(3, "- **État de ce fichier : brouillon 7 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 6 (",
    "- **État de ce fichier : brouillon 8 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 7 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-7.md`, `" + B7_SHA + "`), le brouillon 6 (")
sub(3, "sur les réponses de la session de l'organisme datées 05:58Z (" + REF7 + "), fiche du juge",
    "sur les réponses de la session de l'organisme datées 05:58Z (**R-5140**, registre des décisions de `main`), fiche du juge")
sub(3, "condition `hypothese_sortie_maximale_tenue` ajoutée à sa règle de lecture ; devis v11f.",
    "condition `hypothese_sortie_maximale_tenue` ajoutée à sa règle de lecture ; devis v11f. Objet du brouillon 8 : R-5140 "
    "cité aux emplacements de référence, et son point (d) porté au texte : la mesure se joue dès le scellement de ce texte.")
sub(3, "Il porte des emplacements « EMPREINTE À INSCRIRE : <chemin> » et « RÉFÉRENCE À INSCRIRE », et une dernière section de "
       "points à trancher :",
    "Il porte des emplacements « EMPREINTE À INSCRIRE : <chemin> » et une dernière section de points à trancher :")
sub(4, "R-5132, R-5134 et la ligne GO-2026-11-23-07.",
    "R-5132, R-5134 et la ligne GO-2026-11-23-07. Pour le brouillon 8, R-5140 (commit `" + LU_B8["commit"][:9] + "`).")
sub(5, "- Date (UTC) de ce brouillon : 2026-11-23T06:00:40Z (`date -u +%FT%TZ`) ; brouillon 6 : 2026-11-23T05:54:27Z ;",
    "- Date (UTC) de ce brouillon : " + date_utc + " (`date -u +%FT%TZ`) ; brouillon 7 : 2026-11-23T06:00:40Z ; brouillon 6 : "
    "2026-11-23T05:54:27Z ;")
sub(8, "jouée après le scellement de ce texte ; ses deux cas : liste d'arrêt, « Avant le départ, hors du lanceur »).",
    "jouée dès le scellement de ce texte (R-5140, point (d)) ; ses deux cas : liste d'arrêt, « Avant le départ, hors du "
    "lanceur »).")
sub(8, "ajoutée à la règle de lecture (" + REF7 + ") ;", "ajoutée à la règle de lecture (**R-5140**) ;")
sub(8, "où figurent R-5132 et R-5134).",
    "où figurent R-5132 et R-5134). **Brouillon 8** : R-5140 (décisions de la session de l'organisme datées 05:58Z, "
    "complément de R-5132 : mesure bornée par 10,50 USD au pire, au plus onze envois ; fiche du juge ; condition "
    "`hypothese_sortie_maximale_tenue` ; mesure jouée dès le scellement) ; registres relus sur `main` au commit `"
    + LU_B8["commit"] + "` (`registres/go.md` `" + LU_B8["go"] + "`, `registres/decisions.md` `" + LU_B8["decisions"]
    + "`, où figure R-5140).")
sub(22, "(23 novembre, R-5130 et R-5132, et ses réponses datées 05:58Z), à contre-lire ;",
    "(23 novembre, R-5130, R-5132 et R-5140), à contre-lire ;")

# ------------------------------------------------------------------------------------------------ mesure
sub(91, "plan de R-5132, échéance 2026-11-30 ; jouée après le scellement de ce texte et avant le départ)",
    "plan de R-5132, échéance 2026-11-30 ; jouée dès le scellement de ce texte, avant le départ, R-5140)")
sub(91, "**(b) Avec la mesure** (GO-2026-11-23-07) : elle est jouée après le scellement de ce texte et avant le départ, au plus "
        "tard à l'échéance de sa ligne,",
    "**(b) Avec la mesure** (GO-2026-11-23-07) : elle est jouée dès le scellement de ce texte (R-5140, point (d)), avant le "
    "départ, au plus tard à l'échéance de sa ligne,")
sub(91, "(réponses datées 05:58Z ; cette lecture des fonctions de fiches", "(R-5140, point (b) ; cette lecture des fonctions de fiches")
sub(91, "le plafond de session des juges ; réponses datées 05:58Z), si la réflexion moyenne mesurée",
    "le plafond de session des juges ; R-5140, point (c)), si la réflexion moyenne mesurée")
sub(91, "passerait 10,50 USD (la commande compte un envoi échoué à son pire cas dès que la requête de génération est partie, "
        "sauf usage lu).",
    "passerait 10,50 USD, soit au plus onze envois comptés à leur pire cas (R-5140, point (a) ; devis v11, § 4 ; la commande "
    "compte un envoi échoué à son pire cas dès que la requête de génération est partie, sauf usage lu).")
sub(101, "R-5130 et R-5132, et ses réponses datées 05:58Z ; à contre-lire).", "R-5130, R-5132 et R-5140 ; à contre-lire).")
sub(296, "(brouillons 5 à 7 ; R-5130, R-5132 et GO-2026-11-23-07)", "(brouillons 5 à 8 ; R-5130, R-5132, R-5140 et GO-2026-11-23-07)")
sub(296, "échéance 2026-11-30 ; jouée après le scellement)", "échéance 2026-11-30 ; jouée dès le scellement, R-5140)")

# ------------------------------------------------------------------------------------------------ dernière section
sub(306, lignes[306], "5. Inscrits : au brouillon 4, le libellé de la contre-lecture (« Opus 5.5, contre-lecteur neuf ») ; au brouillon 5, "
    "R-5130 et le retrait du gabarit du relevé du prix Claude (le lanceur lit le relevé du jour, "
    "`course-v11/releve-prix-claude-course-affinage-v11.json`, jamais un gabarit) ; au brouillon 7, R-5132 et GO-2026-11-23-07 ; "
    "au brouillon 8, R-5140 (aux quatre emplacements de référence laissés au brouillon 7).")
assert lignes[307].startswith("6. Inscrits : au brouillon 4,") and lignes[308] == ""
del lignes[307]
sub(316, "jouée après le scellement de ce texte (R1) et avant le départ ;",
    "jouée dès le scellement de ce texte (R-5140, point (d)) et avant le départ ;")
sub(316, "Si elle n'est pas jouée avant l'échéance de sa ligne, le cas (a) vaut tel qu'il est écrit. Recommandation du rédacteur, "
         "inchangée (confiance 0,7) : la jouer dès le scellement.",
    "Le cas (a) ne vaut plus que si elle n'est pas jouée avant l'échéance de sa ligne.")
sub(317, "tranché (réponses datées 05:58Z) :", "tranché (R-5140, point (b)) :")
sub(318, "tranché (réponses datées 05:58Z) :", "tranché (R-5140, point (c)) :")
DU_B7_AU_B8 = (" Du brouillon 7 au brouillon 8 (message de la session de l'organisme daté 06:05Z) : R-5140 cité aux quatre "
               "emplacements de référence et là où le brouillon 7 disait « réponses datées 05:58Z » ; mesure jouée dès le "
               "scellement (R-5140, point (d)) ; au plus onze envois dit au texte ; aucun chiffre changé.")
lignes[333] = lignes[333] + DU_B7_AU_B8
touchees.add(333)
ordre = sorted(lignes)
texte = "\n".join(lignes[n] for n in ordre) + "\n"
assert "RÉFÉRENCE À INSCRIRE" not in texte and "RÉGLAGE À INSCRIRE" not in texte
assert "réponses datées 05:58Z" not in texte.split("\n## Emplacements")[0].replace("Du brouillon 6 au brouillon 7", "")
assert all("jouée après le scellement" not in lignes[n] for n in (8, 91, 296, 316))   # l. 3 garde l'objet du brouillon 7
assert texte.count("\n## Emplacements et points à trancher avant le scellement") == 1
open(dst, "w", encoding="utf-8", newline="\n").write(texte)
print(hashlib.sha256(texte.encode("utf-8")).hexdigest(), dst)
print("lignes du brouillon 7 touchées :", sorted(touchees))
print("lignes du brouillon 8 :", texte.count("\n"))
print("emplacements « EMPREINTE À INSCRIRE » :", texte.count("EMPREINTE À INSCRIRE"), "; « RÉFÉRENCE À INSCRIRE » :",
      texte.count("RÉFÉRENCE À INSCRIRE"))
