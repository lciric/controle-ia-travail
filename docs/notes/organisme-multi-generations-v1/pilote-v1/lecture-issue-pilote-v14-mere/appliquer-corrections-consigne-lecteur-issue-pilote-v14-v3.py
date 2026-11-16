"""Corrections du tour 2 de contre-lecture appliquées à la consigne du lecteur de l'issue du pilote MR-2 (procédure v14) : v2 -> v3.

Bibliothèque standard seule. Vérifie l'empreinte de la pièce de départ et celle du rapport, que chaque « ancien » figure exactement
une fois (dans la v2 et dans le texte en cours), et refuse d'écraser la cible (ouverture en mode exclusif).

Rapport appliqué : contre-lecture-consigne-lecteur-issue-pilote-v14-tour2-v1.md
(8c020f418de840403f666c501bdf05e07e1e57cef0b0735421bef89675fe5293).

Usage : python3 -I -B appliquer-corrections-consigne-lecteur-issue-pilote-v14-v3.py HEURE_UTC
        (HEURE_UTC lue par `date -u +%Y-%m-%dT%H:%M:%SZ` au moment de l'écriture, avant le scellement)
"""
import hashlib
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "consigne-lecteur-issue-pilote-v14-v2.md")
SOURCE_SHA256 = "0e12acbd6ea72bf2318c809d13be20382b6e6864041ce0e20a56365425c8e30b"
CIBLE = os.path.join(ICI, "consigne-lecteur-issue-pilote-v14-v3.md")
RAPPORT = os.path.join(ICI, "contre-lecture-consigne-lecteur-issue-pilote-v14-tour2-v1.md")
RAPPORT_SHA256 = "8c020f418de840403f666c501bdf05e07e1e57cef0b0735421bef89675fe5293"

# M1 (b) : définition complète du tirage (R9). Le couple du rapport est repris ; trois précisions de A pour qu'il soit reproductible
# sans choix laissé au lecteur : un seul générateur pour tout l'audit, indices comptés à partir de 0 dans l'ordre de `CARTES.json`,
# et aucun tirage (le générateur n'avance pas) pour un appel à au plus 3 cartes ; la phrase « sans numpy : non fait » du rapport
# est portée dans le texte.
M1B_NOUVEAU = ("l'entier g des 16 premiers octets, lus gros-boutiste, de l'empreinte sha256 (32 octets) du fichier `CARTES.json` tel que "
               "remis ; générateur `numpy.random.default_rng(numpy.random.SeedSequence(g))`, un seul pour tout l'audit ; appels pris par "
               "monde croissant puis par nom de proposeur dans l'ordre alphabétique ; pour un appel de k cartes (toutes celles que "
               "`CARTES.json` lui attribue, refusées comprises, dans l'ordre où il les liste), tirage `rng.choice(k, size=3, replace=False)` "
               "(indices comptés à partir de 0 dans cet ordre) ; toutes les cartes si k ≤ 3, sans tirage (le générateur n'avance pas) ; "
               "sans `numpy` (version 1.25 au moins), le tirage est écrit « non fait », avec sa cause),")

M2_NOUVEAU = ("(ces deux pièces s'ouvrent en dernier, après les points 0 et 1 ; avant cela, `sortie-mesure-pilote-v70.json` ne s'ouvre que "
              "pour `hors_corps` et `corps.mondes_sha256`, jamais pour `corps.regle`, `corps.principale` ni `corps.audit_R4`, ni le relevé "
              "ni le manifeste pour autre chose que leurs champs de contrôle ; une issue aperçue avant la fin des points 0 et 1 est écrite "
              "au rapport).")

M4_NOUVEAU = ("une part dépassée est déjà un arrêt du point 0 ; le code de sortie 3 du programme n'est pas dans sa sortie JSON : la mère "
              "le donne, sinon il se déduit de `sous_la_part` (chaque proposeur et `machine`), `pi1_sous_la_ligne` et `pi2_sous_la_ligne`, "
              "qui doivent tous être vrais ; la machine contre 3 USD, comprise dans les 21,72 USD de π2)")

M7_NOUVEAU = ("(hors des pièces nommées ci-dessus : ni `prive/`, ni les mondes, ni la branche d'entrée `calcul/pilote-mr2-v74-entree-v14`, "
              "ni aucune clé ni variable d'environnement)")

COUPLES = [
    ("M1 (a)",
     "égaux aux empreintes du secret, de la phrase, de `H` et de `S1` à `S4` du registre (A dit si `phrase-sha256.txt` est de même "
     "nature que l'empreinte inscrite) ;",
     "égaux aux empreintes du secret, de la phrase (empreinte du fichier de la phrase, retour à la ligne final compris : procédure v14, "
     "section 5, point 5), de `H` et de `S1` à `S4` du registre (la valeur hexadécimale est celle que porte le fichier, après son nom "
     "de champ éventuel) ;"),
    ("M1 (b)",
     "l'entier des 16 premiers octets, gros-boutiste, de sha256 de `CARTES.json` ; tirage sans remise, toutes les cartes si l'appel en a "
     "au plus 3),",
     M1B_NOUVEAU),
    ("M1 (c) 1",
     "**Point ouvert, à lever par l'auteur avant la remise** : la formule de la graine\n"
     "    est une proposition du contre-lecteur ; le texte scellé dit seulement « graine dérivée de l'empreinte de `CARTES.json` » ; l'auteur la\n"
     "    confirme ou la remplace (R9).",
     "**Levé au tour 2** : la formule de la graine, proposée au tour 1, est confirmée et complétée par le rédacteur des corrections\n"
     "    (modèle A) : ordre des appels, ordre des cartes, générateur (voir le point 7) ; le texte scellé dit seulement « graine dérivée de\n"
     "    l'empreinte de `CARTES.json` »."),
    ("M1 (c) 2",
     "**Point ouvert, à lever par l'auteur avant la remise** : la\n"
     "    parenthèse sur la nature de `phrase-sha256.txt` s'adresse à l'auteur, non au lecteur ; le rédacteur ne peut la trancher sans ouvrir\n"
     "    la pièce.",
     "**Levé au tour 2** : la parenthèse sur la nature de `phrase-sha256.txt` s'adressait à l'auteur, non au lecteur ;\n"
     "    elle est retirée."),
    ("M1 (c) 3",
     "l'auteur le confirme et retire la parenthèse.",
     "le contre-lecteur du tour 2 l'a vérifié et le rédacteur des corrections (modèle A) a retiré la parenthèse."),
    ("M2", "(ces deux pièces s'ouvrent en dernier, après les points 0 et 1).", M2_NOUVEAU),
    ("m1 (1)", "écart ou tout contrôle impossible : arrêt, rapport,", "écart (empreinte, code, état, compte, part) : arrêt, rapport,"),
    ("m1 (2)", "ne peut faire est écrit « non fait » avec sa cause, jamais sauté en silence (R5).",
     "ne peut faire (pièce absente ou illisible) est aussi un arrêt aux points 0 à 2, écrit « non fait » avec sa cause, jamais sauté en "
     "silence (R5) ; au point 7 seul, il est écrit « non fait » sans arrêt."),
    ("m2", "final (`etape=fini` dans `etat.txt`) ; en particulier :",
     "final (`etape=fini` dans `etat.txt`) ; la mère ne remet aucune pièce de la copie qui n'est pas nommée ci-dessous ; elle remet :"),
    ("m3 (1)", "fichiers exclus au balayage : aucun nécessaire", "le champ `exclus_balayage=` ne nomme aucune pièce remise ici"),
    # m3 (2) : « nul » précisé par le type de chaque champ (`arret` vaut `null`, `appels_complets_illisibles` est un compte).
    ("m3 (2)", "relevé et manifeste complets (non partiels)",
     "relevé et manifeste complets (`partiel` faux et `arret` vide, `null`, dans chacun ; `appels_complets_illisibles` à 0 dans le relevé)"),
    ("m3 (3)", "il lit `audit_R4` de la sortie de la mesure.", "il lit `corps.audit_R4` de la sortie de la mesure."),
    ("m3 (4)", "(la liste `mondes_sha256` de la sortie de mesure est triée", "(la liste `corps.mondes_sha256` de la sortie de mesure est triée"),
    ("m4", "un code 3 du programme ou une part dépassée est déjà un arrêt du point 0)", M4_NOUVEAU),
    ("m5", "« non déclenché » : aucun audit.",
     "« non déclenché », ou champ absent (issue P-0 : la sortie s'arrête avant de le calculer) : aucun audit."),
    ("m6", "les trois phrases du point 6", "les phrases du point 6"),
    ("m7", "(brief, section 6)", M7_NOUVEAU),
]

ENTETE_ANCIEN = ("# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v2\n\n"
                 "Version 2, 2026-11-16T13:36:53Z (`date -u`, au scellement) : corrections du tour 1 de sa contre-lecture appliquées "
                 "(section « Contre-lecture », en fin de pièce) ; la v1 (`5189c442…`) reste intacte dans ce dossier.\n\n")
ENTETE_NOUVEAU = ("# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v3\n\n"
                  "Version 3, {heure} (`date -u`, à l'écriture, avant le scellement) : corrections du tour 2 de sa contre-lecture "
                  "appliquées (section « Contre-lecture », en fin de pièce) ; la v2 (`0e12acbd…`) et la v1 (`5189c442…`) restent "
                  "intactes dans ce dossier.\n\n")

TOUR2 = """
### Tour 2

- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-tour2-v1.md` (même dossier), empreinte
  `8c020f418de840403f666c501bdf05e07e1e57cef0b0735421bef89675fe5293` (égale à son compagnon) ; verdict « corrections » (deux
  majeures, sept mineures) ; pièce lue : la v2, `0e12acbd6ea72bf2318c809d13be20382b6e6864041ce0e20a56365425c8e30b`.
- **Application** : par un rédacteur neuf (modèle A), par le programme
  `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v3.py` (même dossier) : empreintes de la v2 et du rapport vérifiées,
  chaque « ancien » présent une seule fois, cible jamais écrasée. Noms des pièces citées revérifiés présents dans la copie de sortie
  (noms et tailles seulement, aucune pièce de la copie ouverte). Noms de champs (`exclus_balayage=` de `etat.txt` ; `partiel`, `arret`,
  `appels_complets_illisibles` du relevé ; `partiel`, `arret` du manifeste ; `corps` et `hors_corps` de la sortie de mesure ;
  `appels` et `cartes` de `CARTES.json`) relus sur la procédure v14 et sur les pièces de la répétition locale versées au commit
  `2d35cafa` (`…/procedure-pilote-v74-compte-organisme/repetition-locale/rapatrie/`), non sur les pièces réelles.
- **Réponse point par point** :
  - M1 (a) (nature de `phrase-sha256.txt`) : appliquée mot pour mot ; procédure v14, section 5, points 4 et 5, et ligne du registre
    (« empreinte du fichier de la phrase (retour à la ligne final compris) ») relues : même nature.
  - M1 (b) (graine) : appliquée, **avec trois précisions** pour qu'aucun choix ne reste au lecteur : un seul générateur pour tout
    l'audit ; indices comptés à partir de 0 dans l'ordre de `CARTES.json` ; aucun tirage, le générateur n'avançant pas, pour un appel à
    au plus 3 cartes (zéro compris). La phrase du rapport « sans `numpy`, le tirage est « non fait » » est portée dans le texte
    (avec la version 1.25 au moins, R9). Le texte scellé ne définit que « graine dérivée de l'empreinte de `CARTES.json` » : c'est une
    précision, non un écart.
  - M1 (c) (deux « points ouverts ») : appliquée ; une adaptation : « l'auteur (modèle A) » du couple devient « le rédacteur des
    corrections (modèle A) », parce que ce rédacteur n'est pas le compte organisme ; même adaptation au troisième couple (« l'auteur a
    retiré la parenthèse » devient « le rédacteur des corrections (modèle A) a retiré la parenthèse »). La puce « Application » du
    tour 1 (« modèle C ») est gardée telle quelle : sa rectification est un point pour la mère du rapport, non une correction exigée.
  - M1 (d) (puce du tour 2) : cette sous-section.
  - M2 (sortie de mesure avant la fin des points 0 et 1) : appliquée mot pour mot.
  - m1 (contradiction du point 0) : appliquée mot pour mot (deux couples).
  - m2 (« seules pièces nommées ») : appliquée mot pour mot.
  - m3 (noms de champs, chemins `corps.`) : appliquée, quatre couples ; au deuxième, « `arret` nul » et « `appels_complets_illisibles`
    nul » sont écrits selon le type du champ (« `arret` vide, `null` » ; « `appels_complets_illisibles` à 0 »), le reste mot pour mot.
  - m4 (code 3, part de la machine) : appliquée mot pour mot ; relue sur `depense_pilote_v14_v1.py` (`9866e611…`) : code 3 si l'un
    de `sous_la_part` (chaque proposeur, `machine`), `pi1_sous_la_ligne`, `pi2_sous_la_ligne` est faux ; `MACHINE = 3.0`.
  - m5 (`audit_R4` absent si P-0) : appliquée mot pour mot.
  - m6 (« trois phrases ») : appliquée mot pour mot.
  - m7 (« brief, section 6 ») : appliquée mot pour mot ; elle tranche la remarque facultative R1 du tour 1.
  - Remarques facultatives F1 à F5 : non appliquées (non exigées).
"""


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main(a):
    if len(a) != 1 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", a[0]):
        print("REFUS : usage HEURE_UTC (AAAA-MM-JJTHH:MM:SSZ)")
        return 2
    if os.path.exists(CIBLE):
        print("REFUS : la cible existe déjà, jamais écrasée")
        return 2
    brut = open(SOURCE, "rb").read()
    if sha(brut) != SOURCE_SHA256:
        print("REFUS : empreinte de la pièce de départ différente")
        return 2
    if sha(open(RAPPORT, "rb").read()) != RAPPORT_SHA256:
        print("REFUS : empreinte du rapport différente")
        return 2
    v2 = brut.decode("utf-8")
    texte = v2
    for nom, ancien, nouveau in [("en-tête", ENTETE_ANCIEN, ENTETE_NOUVEAU.format(heure=a[0]))] + COUPLES:
        n2, n = v2.count(ancien), texte.count(ancien)
        if n2 != 1 or n != 1:
            print(f"REFUS : {nom} : « ancien » présent {n2} fois dans la v2 et {n} fois dans le texte en cours (une fois exigée)")
            return 2
        texte = texte.replace(ancien, nouveau)
        print(f"{nom} : appliqué")
    if not texte.endswith("\n"):
        print("REFUS : fin de pièce inattendue")
        return 2
    texte += TOUR2
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(texte)
    print(f"écrit : {CIBLE} ({sha(texte.encode('utf-8'))})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
