#!/usr/bin/env python3
"""Applique à procedure-machine-jeu-idee-1-1-v5.md les couples A à E du tour 4 (m1 à m3) : v6 neuve.

Usage : python3 -I corriger_procedure_v5_vers_v6_tour4_v1.py SOURCE CIBLE HEURE_UTC
- SOURCE : la procédure v5, dont l'empreinte doit être EMPREINTE_SOURCE ;
- CIBLE : la procédure v6, fichier neuf (jamais écrasé, R12 : ouverture exclusive) ;
- HEURE_UTC : `date -u +%FT%TZ` au moment du scellement.
Le rapport du tour 4 doit avoir l'empreinte EMPREINTE_TOUR4 ; les pièces nommées par la procédure doivent être égales à
leurs compagnons. Chaque « ancien » doit figurer exactement une fois au moment de son couple.
Aucun accès réseau, aucune pièce modifiée.
"""
import hashlib
import os
import re
import sys

EMPREINTE_SOURCE = "682ee4de21615253096be6905bf5d0a8b56d8a5c4fb3df3df670746bc0a7c465"
NOM_TOUR4 = "contre-lecture-machine-jeu-idee-1-1-v5-tour1-v1.md"
EMPREINTE_TOUR4 = "31566abb49841cbc59ca708d71f3c0797a78cb2e784a478485b0135f5e993c44"
PIECES = ["lancer_jeu_idee_1_1_machine_v2.sh", "garde_machine_jeu_idee_1_1_v1.py", "amorce_jeu_idee_1_1_v2.sh",
          "repetition_machine_jeu_idee_1_1_v2.sh", "jeu_factice_idee_1_1_v1.py", "sortie-repetition-machine-jeu-idee-1-1-v2.txt",
          "devis-machine-jeu-idee-1-1-v2.md", "rapport-machine-jeu-idee-1-1-v2.md", NOM_TOUR4,
          "procedure-machine-jeu-idee-1-1-v5.md"]
NOM_PROGRAMME = "corriger_procedure_v5_vers_v6_tour4_v1.py"
NOM_REJEU = "sortie-repetition-machine-jeu-idee-1-1-v2-rejeu-procedure-v6.txt"


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def couples(heure):
    return [
        # --- en tête : titre, statut, version
        ("# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v5\n",
         "# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v6\n"),
        ("-tour2-v1.md`) et 3 (`contre-lecture-machine-jeu-idee-1-1-tour3-v1.md`), corrections",
         "-tour2-v1.md`), 3 (`contre-lecture-machine-jeu-idee-1-1-tour3-v1.md`) et 4\n"
         "  (`contre-lecture-machine-jeu-idee-1-1-v5-tour1-v1.md`), corrections"),
        ("des tours 2 (point 4) et 3 en v5, avec",
         "des tours 2 (point 4) et 3 en v5, du tour 4 en v6, avec"),
        ("ne part pas au feu sans un tour 4 rendu `scellable` (§ 6)",
         "ne part pas au feu sans un tour 5 rendu `scellable` (§ 6 ; le tour 4 a rendu `corrections`)"),
        ("- **Version** : v5, scellée à 2026-11-16T22:22:29Z (`date -u`) ; suit la v4 (`996c8a5c…`) ; changements de la v4 à la v5 :",
         f"- **Version** : v6, scellée à {heure} (`date -u`) ; suit la v5 (`682ee4de…`) ; changements de la v5 à la v6 :\n"
         "  couples A à E du tour 4 (m1 à m3 : § 1 pas 7, § 3 L3, gestes 5 et 13) et condition du tour 5 (statut, § 2 point 3),\n"
         "  déclarés au § 6 (tour 4). La v5 (2026-11-16T22:22:29Z) suivait la v4 (`996c8a5c…`) ; changements de la v4 à la v5 :"),
        # --- § 2 point 3 : condition du tour suivant (conséquence du verdict `corrections` du tour 4)
        ("lecteur neuf (R2),\n   tour 4 rendu `scellable`.",
         "lecteur neuf (R2),\n   tour 5 rendu `scellable`."),
        # --- couple C (m2, § 1 pas 7)
        ("que la minuterie détruit à\n   l'échéance) ; un chemin hors des",
         "que la minuterie détruit à\n   l'échéance si elle tourne encore (un état « stopped » peut l'avoir arrêtée avec la machine :"
         " non éprouvé ; la session détruit alors par l'identifiant, geste 13) ; un chemin hors des"),
        # --- couple A (m1, § 3 L3)
        ("≈ 12 600 caractères (répétition v2 : 12 619), lue en **deux\n  morceaux** (6 000, puis 6619)",
         "≈ 12 480 caractères au vrai dossier d'envoi (fourchette admise : 12 400 à 12 700 ; répétition v2 : 12 619, chemin"
         " d'envoi plus long de 71 caractères, écrit deux fois), lue en **deux\n  morceaux** (6 000, puis le reste, ≈ 6 480)"),
        # --- couple B (m1, geste 5)
        ("**2** lignes, ≈ 12 800 octets, puis",
         "**2** lignes, ≈ 12 650 octets (fourchette admise : 12 500 à 12 800 ; elle dépend du chemin du dossier d'envoi), puis"),
        # --- couple D (m2, geste 13)
        ("sa minuterie la\n    détruit à l'échéance quoi qu'il arrive, disque compris : la décision se prend avant ;",
         "sa minuterie la\n    détruit à l'échéance si elle tourne encore, disque compris (une machine arrêtée par « stopped »"
         " peut l'avoir perdue : non éprouvé ; le rappel de la mère à l'échéance et la destruction par l'identifiant couvrent ce"
         " cas) : la décision se prend avant ;"),
        # --- couple E (m3, geste 13)
        ("puis « fin de la machine, code … » et\n    « « stopped » demandé »",
         "puis « fin, code … ; état « stopped » demandé maintenant » (le message de poussée « fin de la machine, code … » se"
         " lit par `git log`) et\n    « état « stopped » demandé : HTTP … »"),
    ]


FIN_V5 = ("- **Rien d'autre ne change** de la v4 à la v5 : en tête (titre, décision, liste des pièces, statut, version), les couples\n"
          "  ci-dessus et cette section.\n")


def section_tour4(E):
    return f"""
**Tour 4** (corrections en v6) :

- **Rapport** : `{NOM_TOUR4}` (même dossier), empreinte `{EMPREINTE_TOUR4}`,
  lecteur neuf (R2), première contre-lecture de la v5 ; verdict `corrections` : la majeure M1'' du tour 3 levée (rejeu
  intégral de la répétition v2 et artefact sur l'amorce v1, 11 écarts sur 126) ; aucune majeure ; trois mineures (m1 à m3),
  toutes de texte de cette procédure ; remarques facultatives F-a à F-g ; les pièces v2 (amorce, lanceur, répétition et sa
  sortie, devis, rapport) jugées sans correction exigée.
- **Cette version** : v6, écrite par un rédacteur neuf, qui n'a écrit aucune autre pièce du dossier, au moyen du programme de
  couples `{NOM_PROGRAMME}` (même dossier, scellé avec son compagnon), depuis la v5
  `{EMPREINTE_SOURCE}`. Aucune autre pièce ne change : la liste des pièces en tête est celle de
  la v5, empreintes relues égales à leurs compagnons par le programme.
- **Réponse point par point** :
  - **m1** (valeurs attendues des gestes 5 et L3, mesurées avec un dossier d'envoi plus long que le vrai) : couples A (§ 3,
    L3) et B (geste 5) appliqués tels que le rapport les écrit. Arithmétique relue : chemin d'envoi de la répétition v2 de 111
    caractères, vrai dossier `/home/user/jeu-idee-1-1-machine-envoi-v1` de 40, écart de 71, écrit deux fois : 12 619 − 142 =
    12 477 caractères ; la fourchette de la sortie de `commande` est celle du rapport.
  - **m2** (destruction par la minuterie après « stopped » : non éprouvée) : couples C (§ 1, pas 7) et D (geste 13)
    appliqués tels quels. Le rappel programmé de la mère à l'échéance (reste ouvert ci-dessous) en devient le garde-fou.
    F-e (même formule au devis v2, § 2 et § 3, et au rapport v2, § 2) : facultative, non appliquée (aucune version neuve de
    ces deux pièces) ; écart de formule connu et déclaré ici : dans ces deux pièces, « la minuterie la détruit à l'échéance »
    après l'état « stopped » se lit « si elle tourne encore » ; le coût n'en dépend pas (le devis compte déjà 24 h d'arrêt).
  - **m3** (libellé de fin au geste 13) : couple E appliqué tel quel ; vérifié dans l'amorce v2 : le journal écrit
    `fin, code N ; état « stopped » demandé maintenant ; …` puis `état « stopped » demandé : HTTP …` ; `fin de la machine,
    code N` est le message de poussée.
  - **F-a** (« Rien d'autre ne change » du tour 3, imprécis) : facultative ; la réponse au tour 3 n'est pas réécrite ; ses
    changements de rédaction sont déclarés plus haut dans la même réponse.
  - **F-b, F-c, F-d, F-f, F-g** : facultatives, non appliquées ; gardées aux restes ouverts.
  - **Points pour la mère** : hors du texte de la procédure ; rien n'y change ici.
- **Changement de conséquence, déclaré** : le tour 4 ayant rendu `corrections`, la condition de départ au feu nomme le tour 5
  (statut, en tête, et § 2 point 3) ; titre et version.
- **Répétition** : aucune pièce de la répétition ne change ; rejouée après ces couples, sortie neuve `{NOM_REJEU}`
  (même dossier, scellée avec son compagnon) ; la sortie gardée de la liste des pièces reste
  `sortie-repetition-machine-jeu-idee-1-1-v2.txt`.
- **Restes ouverts déclarés** (la mère les tient) :
  - F2 et F4 du tour 1 (gestes 8 et 9) : facultatives, toujours ouvertes ;
  - rappel programmé de la mère à l'échéance (49 h 45 après l'impression), garde-fou de m2 ;
  - permission de la ligne neuve par Lazar avant de lancer ; renouvellement du jeton `CONTROLE_IA_GITHUB_TOKEN_2` après la
    preuve de destruction ;
  - ligne de GO de type « calcul » à inscrire (périmètre « idée 1.1 », `3.5 USD`, échéance 2026-11-22 au plus tôt ; pire cas
    de 3,24 à 3,30 USD au-delà de l'ordre de grandeur de 1 à 3 USD, plafond à faire accorder tel quel par Lazar) ;
  - `COMMIT` à relire au feu ; dossier à commiter ; fichiers parasites `/s.txt` et `/commande-coupee.txt` à effacer par une
    personne (le rapport du tour 4 relève aussi un fichier `/x` à la racine, d'origine non établie) ;
  - réserves du rapport v2, § 5 : reprise sur un refus de la garde de poussée elle-même (F-b), recopie partielle non refaite
    (F-c), trafic montant du cas extrême et coût de trafic de l'offre à relever (F-d).
- **Rien d'autre ne change** de la v5 à la v6 : en tête (titre, statut, version), les couples A à E, la condition du tour 5
  au § 2 point 3 et cette section.
"""


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    src, cible, heure = sys.argv[1:]
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
        print("REFUS : heure illisible")
        return 2
    if os.path.exists(cible):
        print("REFUS : la cible existe déjà (R12)")
        return 2
    if sha(src) != EMPREINTE_SOURCE:
        print("REFUS : empreinte de la source ≠ v5")
        return 2
    ici = os.path.dirname(os.path.abspath(src))
    E = {}
    for n in PIECES:
        p = os.path.join(ici, n)
        c = open(p + ".sha256", encoding="utf-8").read()
        E[n] = sha(p)
        if c != f"{E[n]}  {n}\n":
            print(f"REFUS : compagnon de {n} faux ou absent")
            return 2
    if E[NOM_TOUR4] != EMPREINTE_TOUR4:
        print("REFUS : empreinte du rapport du tour 4 inattendue")
        return 2
    t = open(src, encoding="utf-8").read()
    for i, (a, n) in enumerate(couples(heure), 1):
        k = t.count(a)
        if k != 1:
            print(f"REFUS : couple {i} : « ancien » trouvé {k} fois (attendu 1)")
            return 2
        t = t.replace(a, n)
    if t.count(FIN_V5) != 1 or not t.endswith(FIN_V5):
        print("REFUS : fin de la v5 introuvable")
        return 2
    t = t + section_tour4(E)
    with open(cible, "x", encoding="utf-8") as f:
        f.write(t)
    print(f"v6 écrite : {cible} ; {len(couples(heure))} couples appliqués, une fois chacun, et la section du tour 4")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
