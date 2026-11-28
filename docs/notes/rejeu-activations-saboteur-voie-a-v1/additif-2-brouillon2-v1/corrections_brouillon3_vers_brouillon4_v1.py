"""Corrections du brouillon 3 vers le brouillon 4 de l'additif 2 aux sondes du barreau 8.

Rejouable : lit le brouillon 3 (empreinte exigée), applique les corrections de la seconde
vérification (rapport 05d8850c… : défauts A, B, C et deux remarques de forme), écrit le
brouillon 4. Refuse d'écraser. Chaque remplacement exige une occurrence, et une seule.
Le brouillon 4 n'est PAS vérifié : la boucle unique de correction du mandat est épuisée.
Usage : python corrections_brouillon3_vers_brouillon4_v1.py <brouillon3.md> <brouillon4.md>
"""
import hashlib
import sys
from pathlib import Path

EMPREINTE_B3 = "e3c747f113565588c3a0a655eec673aa040b8d4b75c219b75b2e8f6b8baf594f"


def morceau(texte: str, ancien: str, neuf: str) -> str:
    assert texte.count(ancien) == 1, (ancien[:70], texte.count(ancien))
    return texte.replace(ancien, neuf)


def corriger(t: str) -> str:
    # --- en-tête -----------------------------------------------------------------------
    t = morceau(t, "— v1 — brouillon 3\n", "— v1 — brouillon 4\n")
    t = morceau(t, "**Statut : brouillon 3, candidat final. Il porte les quatorze constats de la contre-lecture (règle R2) du brouillon 1 et les deux remarques de son complément (brouillon 2), puis les neuf défauts et la remarque de forme de la vérification des corrections du brouillon 2 (brouillon 3). Il est soumis à la même vérification, par le même vérificateur, puis au scellement par la session mère (clé `SCELLEMENT-ADDITIF-2-SONDES-IIB`).**",
                "**Statut : brouillon 4, non vérifié. Il porte les quatorze constats de la contre-lecture (règle R2) du brouillon 1 et les deux remarques de son complément (brouillon 2), les neuf défauts et la remarque de forme de la vérification du brouillon 2 (brouillon 3), puis les trois défauts et les deux remarques de forme de la vérification du brouillon 3 (brouillon 4). La vérification du brouillon 3 a conclu « à corriger » ; la boucle unique de correction du mandat du rédacteur est épuisée : ce brouillon 4 attend une vérification que la session mère décide, avant tout scellement (clé `SCELLEMENT-ADDITIF-2-SONDES-IIB`).**")
    t = morceau(t, "*et brouillon 3* (ce texte) : écrits par", "*, brouillon 3* (`e3c747f113565588c3a0a655eec673aa040b8d4b75c219b75b2e8f6b8baf594f`) *et brouillon 4* (ce texte) : écrits par")
    t = morceau(t, "brouillon 3 écrit le même jour, heure relevée à la fin de l'écriture : 09:44Z.",
                "brouillon 3 écrit le même jour, vers 09:43Z ; brouillon 4 écrit le même jour, vers 09:50Z.")
    # défaut A : point (iv)
    t = morceau(t, "disait les faits O-3, O-5 et O-6 « déjà gardés par le texte scellé et vérifiés sur le code de lancement » ; ce texte écrit",
                "disait les faits O-3, O-5 et O-6 « déjà gardés par le texte scellé et vérifiés sur le code de lancement », et disait aussi, à son point 10, les quatre bornes dures « intégralement tenues » ; ce texte écrit que les bornes (b1) et (b4) ne sont pas tenues à leur lettre pour la chaîne de cet additif (« Borne du scellement »),")
    t = morceau(t, "(iv) porté à Lazar en une ligne, puisque ce sont les raisons d'un nœud qui changent.",
                "(iv) porté à Lazar en une ligne, puisque ce sont les raisons d'un nœud qui changent ; pour l'écart aux bornes (b1) et (b4), son mot est exigé (champ AD2-3).")

    # --- table des corrections de la seconde vérification --------------------------------
    t = morceau(t, "## Ce que cet additif est, et n'est pas\n",
                "## Corrections de la vérification du brouillon 3 (brouillon 3 → brouillon 4)\n\n"
                "Rapport : `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/verification-corrections-additif-2-brouillon3-opus-v1.md` (`05d8850cf7949f20329f09ff271d9d4eab1a10cda60d9db25ee2b5ffa6a9e8f3`), conclusion « à corriger » : huit des neuf défauts portés, le défaut 2 en partie ; un défaut moyen qui empêche le scellement (A), deux mineurs (B, C), deux remarques de forme. Tous corrigés ici, par le programme `corrections_brouillon3_vers_brouillon4_v1.py` du même dossier (rejouable). **Ces corrections ne sont pas vérifiées.**\n\n"
                "| défaut | gravité | correction | où |\n|---|---|---|---|\n"
                "| A | moyen | l'écart à la lettre des bornes (b1) et (b4) ne vaut que couvert par un mot de Lazar qui le nomme : l'accord GO-2026-11-24-07 a été donné sur une fiche qui disait les quatre bornes tenues ; point 10 de la fiche ajouté aux raisons corrigées | en-tête, point (iv) ; « Borne du scellement » ; AD2-3 ; « Expositions » ; ligne 30 (a) |\n"
                "| B | mineur | « rédacteur non exposé au saboteur, qui a lu les comptes déclarés » ; « hors de la forme du fichier des identifiants et des valeurs de l'extrait du côté exposé » | « Borne du scellement » |\n"
                "| C | mineur | provenance du programme de comparaison : les quatre exigences de l'additif 1, toutes, sinon « non attesté » | AD2-3 ; M-4 |\n"
                "| forme | — | ligne du rédacteur de la table des expositions mise à jour ; heures dites « vers » | « Expositions » ; en-tête |\n\n"
                "## Ce que cet additif est, et n'est pas\n")

    # --- défauts A et B : borne du scellement --------------------------------------------
    t = morceau(t, "les règles M-1 à M-5 sont récrites par un rédacteur non exposé et ne dépendent d'aucune valeur tirée d'une sortie, hors de la forme du fichier des identifiants.",
                "les règles M-1 à M-5 sont récrites par un rédacteur non exposé au saboteur, qui a lu les comptes déclarés, et ne dépendent d'aucune valeur tirée d'une sortie, hors de la forme du fichier des identifiants et des valeurs de l'extrait du côté exposé (D-13 : chemins, empreintes, versions).")
    t = morceau(t, "et elle y dit sous quel accord l'écart à leur lettre est couvert, ou qu'elle le porte à Lazar. Recommandation du rédacteur : le porter à Lazar en une ligne, avec le champ AD2-1. Une borne (b2) ou (b3) non tenue, ou un score, un texte d'épisode ou un état lu : pas de scellement ; nœud de Lazar.",
                "**L'écart à leur lettre ne vaut que couvert par un mot de Lazar qui le nomme** (comme l'additif 1 l'exigeait pour son propre écart, nœud NL-0) : l'accord GO-2026-11-24-07 a été donné sur une fiche de décision dont le point 10 disait les quatre bornes « intégralement tenues » ; il ne couvre donc pas cet écart. La session mère le porte à Lazar et cite son mot au champ AD2-3. Sans ce mot, ou si une borne (b2) ou (b3) n'est pas tenue, ou si un score, un texte d'épisode ou un état a été lu : pas de scellement ; nœud de Lazar.")
    t = morceau(t, "comptes de la note version 7 et de la fiche de décision) : <couvert par l'accord nommé, ou porté à Lazar, avec sa réponse> ;",
                "comptes de la note version 7 et de la fiche de décision) : <mot de Lazar qui nomme cet écart : identifiant de la ligne du registre des accords, et ses mots> ;")
    t = morceau(t, "la session mère dit au champ AD2-3 sous quel accord il est couvert, ou le porte à Lazar (ligne 25 de l'additif 1).",
                "il ne vaut que couvert par un mot de Lazar qui le nomme, cité au champ AD2-3 (voir aussi la ligne 25 de l'additif 1).")
    t = morceau(t, "écart à la lettre des bornes (b1) et (b4) ni couvert par un accord nommé ni porté à Lazar ;",
                "écart à la lettre des bornes (b1) et (b4) sans un mot de Lazar qui le nomme ;")

    # --- défaut C : provenance du programme ------------------------------------------------
    t = morceau(t, "auteur et contre-lecture du programme de comparaison de version 1 : <développeur du côté des moniteurs et contre-lecteur d'un autre modèle, pièces et empreintes ; ou « non attesté »> ;",
                "provenance du programme de comparaison de version 1 : <« attesté », avec les pièces et leurs empreintes, seulement si les quatre exigences de l'additif 1 tiennent toutes — écrit par le développeur du côté des moniteurs, à partir de l'additif 1 seul, contre-lu par un autre modèle, corrections vérifiées par le même contre-lecteur ; sinon « non attesté »> ;")
    t = morceau(t, "L'additif 1 veut que ce programme soit écrit par le développeur du côté des moniteurs et contre-lu par un autre modèle. La version 1",
                "L'additif 1 veut que ce programme soit écrit par le développeur du côté des moniteurs, à partir de l'additif 1 seul, contre-lu par un autre modèle, ses corrections étant vérifiées par le même contre-lecteur. La version 1")
    t = morceau(t, "La session mère l'atteste au champ AD2-3. **Si elle y écrit « non attesté »** :",
                "La session mère l'atteste au champ AD2-3. **Si elle n'atteste pas ces quatre exigences, toutes (« non attesté »)** :")

    # --- remarque de forme : table des expositions -----------------------------------------
    t = morceau(t, "| rédacteur du brouillon 2 (Fable 5.2, session fille, côté des moniteurs) | le brouillon 1 ;",
                "| rédacteur des brouillons 2, 3 et 4 (Fable 5.2, session fille, côté des moniteurs) | les deux rapports de la vérification des corrections (brouillons 2 et 3) ; le brouillon 1 ;")

    # --- contre-lecture --------------------------------------------------------------------
    t = morceau(t, "- **Contre-lecture 2 (finale : même vérification, par le même vérificateur, du brouillon 3, texte rempli)** : À REMPLIR",
                "- **Vérification des corrections du brouillon 3** — même vérificateur ; faite le 2026-11-24 vers 09:45Z. Brouillon vérifié : même dossier, `lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1-brouillon3.md`, empreinte `e3c747f113565588c3a0a655eec673aa040b8d4b75c219b75b2e8f6b8baf594f`. Rapport : même dossier, `verification-corrections-additif-2-brouillon3-opus-v1.md`, empreinte `05d8850cf7949f20329f09ff271d9d4eab1a10cda60d9db25ee2b5ffa6a9e8f3`. Conclusion : « à corriger » ; rejeu du programme des corrections exact à l'octet ; liste des passages fermée ; un défaut moyen qui empêche le scellement (A), deux mineurs (B, C), deux remarques de forme. Traitement : table « Corrections de la vérification du brouillon 3 » en tête de ce texte ; ces corrections ne sont pas vérifiées.\n"
                "- **Contre-lecture 2 (finale : vérification du brouillon 4, décidée par la session mère, texte rempli)** : À REMPLIR")
    return t


def main() -> int:
    source, cible = Path(sys.argv[1]), Path(sys.argv[2])
    brut = source.read_bytes()
    assert hashlib.sha256(brut).hexdigest() == EMPREINTE_B3, "le brouillon 3 n'a pas l'empreinte attendue"
    if cible.exists():
        raise SystemExit(f"refus : {cible} existe (règle R12)")
    cible.write_text(corriger(brut.decode("utf-8")), encoding="utf-8")
    print(hashlib.sha256(cible.read_bytes()).hexdigest(), cible)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
