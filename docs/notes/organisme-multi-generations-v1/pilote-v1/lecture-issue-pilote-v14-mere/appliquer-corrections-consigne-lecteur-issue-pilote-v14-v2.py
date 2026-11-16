"""Corrections du tour 1 de contre-lecture appliquées à la consigne du lecteur de l'issue du pilote MR-2 (procédure v14) : v1 -> v2.

Bibliothèque standard seule. Vérifie l'empreinte de la pièce de départ, que chaque « ancien » figure exactement une fois (dans la v1
et dans le texte en cours), et refuse d'écraser la cible (ouverture en mode exclusif).

Rapport appliqué : contre-lecture-consigne-lecteur-issue-pilote-v14-tour1-v1.md
(14725e82ff9e8d6a7dc0f11457dcb6131c45a69d69d2085965c3fad430e2c8ea).

Usage : python3 -I -B appliquer-corrections-consigne-lecteur-issue-pilote-v14-v2.py HEURE_UTC
        (HEURE_UTC lue par `date -u +%Y-%m-%dT%H:%M:%SZ` au moment du scellement)
"""
import hashlib
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "consigne-lecteur-issue-pilote-v14-v1.md")
SOURCE_SHA256 = "5189c44202e8f9aa8ed65506222f9317e6596cf1c0839b0c89a9af43ad60d539"
CIBLE = os.path.join(ICI, "consigne-lecteur-issue-pilote-v14-v2.md")
RAPPORT_SHA256 = "14725e82ff9e8d6a7dc0f11457dcb6131c45a69d69d2085965c3fad430e2c8ea"

C1_NOUVEAU = """## Ce qu'il fait (plan d'analyse du texte scellé, dans l'ordre)

0. **Arrêts (« Liste d'arrêt »), avant toute ouverture de `lecture-pilote-v70.json` et de `remis-au-sous-agent/sortie-lire-non-ouverte.txt`**
   (ces deux pièces s'ouvrent en dernier, après les points 0 et 1). Il lit à la racine de la copie : `etat.txt` (`etape=fini`, aucun
   `arret (A)`, `noeud, machine gardee` ni `sortie inattendue` ; fichiers exclus au balayage : aucun nécessaire) ; `code-06-generer.txt`,
   `code-07-preparer.txt`, `code-08-blanc.txt`, `code-09-reel.txt`, `code-10-mesurer.txt`, `code-10-lire.txt`, `code-11-rapatrier.txt` : tous
   à 0 (un code 3 vaut arrêt) ; `lancements.jsonl` : une seule ligne ; `rapatrie-reel/liste-rapatriement-pilote-v70.json` : `"aucun_monde": true`
   et pas de `CARTES-partiel.json` ; relevé et manifeste complets (non partiels) ; les 16 appels ont une réponse brute et un témoin
   d'isolement scellés ; dans la dépense remise (point 4 des pièces) : aucun appel au-dessus de son pire cas, aucune part atteinte. Tout
   écart ou tout contrôle impossible : arrêt, rapport, **aucune issue lue, pas même P-0** (texte scellé, « Liste d'arrêt ») ; un contrôle qu'il
   ne peut faire est écrit « non fait » avec sa cause, jamais sauté en silence (R5)."""

C3_NOUVEAU = ("`engagement-mondes.json`, `etat.txt`, `lancements.jsonl`, `code-06-generer.txt`, `code-07-preparer.txt`, `code-08-blanc.txt`, "
              "`code-09-reel.txt`, `code-11-rapatrier.txt`, `secret-sha256.txt`, `phrase-sha256.txt`, "
              "`rapatrie-reel/liste-rapatriement-pilote-v70.json`, `rapatrie-reel/journal-relais-fable52.jsonl`, `…-opus55.jsonl`, "
              "`…-argon.jsonl`, `…-astra.jsonl` (point 4 du plan), et les dossiers `rapatrie-reel/monde-N/PROPOSEUR/` (réponses brutes, "
              "corps des relais, témoins d'isolement : lus pour leurs empreintes, leur présence et l'audit du point 7, jamais recopiés). "
              "Les journaux, les `code-*.txt` et `etat.txt` sont à la racine de la copie. `rapatrie-blanc/` (essai à blanc, proposeurs "
              "factices) ne sert pas à l'issue et n'est jamais confondu avec `rapatrie-reel/`.")

C4_NOUVEAU = """7. **Audit de symétrie (R4)**, tel que le texte le gèle : il lit `audit_R4` de la sortie de la mesure. « déclenché : x = 0 » : il relit toutes
   les cartes refusées au gardien, au-delà de six ou non évaluables, et 3 cartes par appel tirées au hasard (graine : `SeedSequence` de
   l'entier des 16 premiers octets, gros-boutiste, de sha256 de `CARTES.json` ; tirage sans remise, toutes les cartes si l'appel en a au plus 3),
   vérifie que les épisodes servis contiennent les traits et que les témoins disent le gabarit servi. « déclenché : x ≥ 3 » : il relit les cartes
   qui portent, vérifie qu'aucune pièce servie ne décrit la famille ou une condition et l'isolement (témoins), relit aussi les cartes refusées et
   non évaluables. « non déclenché » : aucun audit. L'audit ne change pas l'issue, il la commente (réserve écrite) ; un contrôle qui exige une
   pièce non remise est écrit « non fait »."""

C5A_NOUVEAU = ("4. **La dépense**, calculée par le compte organisme avec `depense_pilote_v14_v1.py` (empreinte "
               "`9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643`, dossier `…/lecture-depense-pilote-v14-compte-organisme/` "
               "de la branche `lot/compte-organisme-v1`, copié par la mère avec la copie de sortie) : le programme ne lit que "
               "`releve-pilote-v70.json` et `journal-relais-*.jsonl`. Le lecteur reçoit sa **sortie JSON scellée** (nom donné par la mère) "
               "et les arguments `--machine` (prix horaire, heures de création et de destruction) et `--autre` tels que la mère les a donnés ; "
               "il les rapporte sans pouvoir les vérifier. Il vérifie l'empreinte du programme et recoupe lui-même, par lecture, les sommes "
               "du relevé et des journaux. Les prix de la configuration ne sont pas remis (le programme ne les lit pas) ; il ne recalcule "
               "aucun coût.")

C5B_NOUVEAU = ("(`depense_usd` et coûts des appels du relevé, somme des `cout_usd` des journaux des relais, parts de 12, 8, 9,36 et 9,36 USD ; "
               "π1 contre 20 USD, π2 contre 21,72 USD ; un code 3 du programme ou une part dépassée est déjà un arrêt du point 0)")

C7_NOUVEAU = ("1. **Empreintes** : chaque pièce qui a un compagnon égale à son compagnon (les journaux, `etat.txt`, `lancements.jsonl` et "
              "`remis-au-sous-agent/` n'en ont pas) ; le texte scellé lu égal à `8aa33014…` ; `secret-sha256.txt`, `phrase-sha256.txt` et "
              "`engagement-mondes.json` égaux aux empreintes du secret, de la phrase, de `H` et de `S1` à `S4` du registre (A dit si "
              "`phrase-sha256.txt` est de même nature que l'empreinte inscrite) ;")

# C12 : chiffres à 12 et 14 appels répondus repris du texte scellé (« Prédiction chiffrée et signe attendu ») à la place de
# « mêmes taux », qui ne sont pas les mêmes (voir la section « Contre-lecture » de la v2).
C12_NOUVEAU = ("les taux d'erreur du texte (section « Prédiction chiffrée et signe attendu » : course refusée à tort 0,20 si p vaut 0,02 ; "
               "permise à tort 0,26 si p vaut 0,051 ; à 12 et 14 appels répondus, refusée à tort 0,22 et 0,21, permise à tort 0,29 et 0,27) "
               "et, si l'issue est P-2, la phrase « Une issue P-2 favorable ne dit pas que les proposeurs « ne voient pas » les "
               "conditionnelles ».")

COUPLES = [
    ("C1", "## Ce qu'il fait (plan d'analyse du texte scellé, dans l'ordre)", C1_NOUVEAU),
    ("C2", "lue au champ `regle` de `lecture-pilote-v70.json` ;",
     "lue au champ `regle` de `lecture-pilote-v70.json` (`regle.issue` vaut `P-0`, `P-1` ou `P-2` ; « P-2 avec réserve » est `P-2` dont "
     "`regle.noeuds_avant_banc` n'est pas vide, chaque nœud nommé ; « P-2 » sans réserve a cette liste vide) ;"),
    ("C3", "`engagement-mondes.json`.", C3_NOUVEAU),
    ("C4", "7. **Audit de symétrie (R4)** : un résultat trop propre, dans un sens ou dans l'autre, reçoit le même audit et une réserve.",
     C4_NOUVEAU),
    ("C5a", "4. **La dépense** calculée par `depense_pilote_v14_v1.py` (même dossier), pour le point 4 du plan.", C5A_NOUVEAU),
    ("C5b", "(relevé, journaux des relais, prix de la configuration)", C5B_NOUVEAU),
    ("C6a", "`programme_sha256` de `mesure-pilote-v70.json` égal à",
     "`programme_sha256` de `mesure-pilote-v70.json` et `hors_corps.script_sha256` de la sortie de mesure égaux à"),
    ("C6b", "égales à `S1` à `S4`",
     "égales à `S1` à `S4` (la liste `mondes_sha256` de la sortie de mesure est triée : comparer comme ensemble)"),
    ("C7", "1. **Empreintes** : chaque pièce égale à son compagnon ;", C7_NOUVEAU),
    ("C8", "liste `modules_importes` de la sortie comparée", "liste `hors_corps.modules_importes` de la sortie de mesure comparée"),
    ("C10a", "sur une branche de travail désignée par la mère : issue",
     "sur une branche de travail désignée par la mère, dans un fichier neuf au nom donné par elle (R12), rien d'autre n'étant écrit : issue"),
    ("C10b", "écarts, nœuds de Lazar appelés.",
     "écarts, dépense rapprochée, contrôles d'arrêt, audit R4 (déclenché ou non, fait ou non fait), les trois phrases du point 6, "
     "nœuds de Lazar appelés."),
    ("C11", "Le lecteur ne lance rien, ne dépense rien,",
     "Le lecteur ne lance ni la mesure, ni le pilote, ni aucun programme qui écrit hors de son fichier de verdict (il lit et additionne "
     "les pièces remises), ne dépense rien,"),
    ("C12", "les taux d'erreur du texte.", C12_NOUVEAU),
    ("C13", "faite une seule fois sur la machine (code 0 attendu) ; il ne la refait pas.",
     "faite une seule fois sur la machine (code 0 attendu : `code-10-mesurer.txt`, `journal-10-mesurer.txt`) ; il ne la refait pas ; "
     "code non nul, exception ou refus nommé : arrêt (« Liste d'arrêt », erreur du programme de la mesure), aucune issue lue."),
]

ENTETE_ANCIEN = "# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v1\n\n"
ENTETE_NOUVEAU = ("# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v2\n\n"
                  "Version 2, {heure} (`date -u`, au scellement) : corrections du tour 1 de sa contre-lecture appliquées (section "
                  "« Contre-lecture », en fin de pièce) ; la v1 (`5189c442…`) reste intacte dans ce dossier.\n\n")

CONTRE_LECTURE = """
## Contre-lecture

- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-tour1-v1.md` (même dossier), empreinte
  `14725e82ff9e8d6a7dc0f11457dcb6131c45a69d69d2085965c3fad430e2c8ea` ; verdict « corrections » (cinq majeures, sept mineures).
- **Application** : par un rédacteur neuf (modèle C), qui n'a écrit ni la v1, ni le texte scellé, ni le code, par le programme
  `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v2.py` (même dossier) : empreinte de la v1 vérifiée, chaque « ancien »
  présent une seule fois, cible jamais écrasée. Noms des pièces citées vérifiés présents dans la copie de sortie (noms et tailles
  seulement, aucune pièce ouverte : 16 réponses brutes, 16 témoins d'isolement, quatre dossiers `monde-N`, aucun `CARTES-partiel.json`).
- **Réponse point par point** :
  - C1 (arrêts, nouveau point 0) : appliquée mot pour mot.
  - C2 (P-2 contre P-2 avec réserve) : appliquée mot pour mot ; `regle.issue` et `regle.noeuds_avant_banc` relus sur
    `mesure_pilote_v4.py` (`676d5f37…`).
  - C3 (pièces manquantes) : appliquée mot pour mot ; la note du rapport « à adapter si un de ces noms change » est hors du nouveau
    texte et n'est pas recopiée ; tous les noms existent aujourd'hui.
  - C4 (audit de symétrie) : appliquée mot pour mot. **Point ouvert, à lever par l'auteur avant la remise** : la formule de la graine
    est une proposition du contre-lecteur ; le texte scellé dit seulement « graine dérivée de l'empreinte de `CARTES.json` » ; l'auteur la
    confirme ou la remplace (R9).
  - C5 (dépense, deux couples) : appliquée mot pour mot ; parts et lignes (12, 8, 9,36, 9,36 ; 20 ; 21,72 USD) relues égales à celles du
    programme `9866e611…`.
  - C6, C8 : appliquées mot pour mot ; `hors_corps.script_sha256`, `hors_corps.modules_importes` et le tri de `mondes_sha256` relus sur
    `mesure_pilote_v4.py`.
  - C7 (compagnons, texte, secret, phrase) : appliquée mot pour mot. **Point ouvert, à lever par l'auteur avant la remise** : la
    parenthèse sur la nature de `phrase-sha256.txt` s'adresse à l'auteur, non au lecteur ; le rédacteur ne peut la trancher sans ouvrir
    la pièce. La procédure v14 (section 5, point 5) dit que la machine pousse `phrase-sha256.txt` après avoir vérifié l'empreinte du
    fichier déchiffré égale à celle du feu, qui est celle que le registre inscrit (« empreinte du fichier de la phrase (retour à la ligne
    final compris) ») ; l'auteur le confirme et retire la parenthèse.
  - C9 : supprimée par le contre-lecteur, intégrée à C3 ; sans objet.
  - C10, C11, C13 : appliquées mot pour mot.
  - C12 (taux d'erreur) : appliquée **avec une correction de chiffres**. Le nouveau proposé disait « mêmes taux à 12 et 14 appels
    répondus » ; le texte scellé (« Prédiction chiffrée et signe attendu ») donne d'autres taux à 12 et 14 appels répondus : refus à
    0,02 de 0,22 et 0,21, acceptation à 0,051 de 0,29 et 0,27. Ces chiffres remplacent « mêmes taux » ; le reste du couple est mot pour
    mot.
  - Remarques facultatives R1 à R4 : non appliquées (non exigées), laissées à l'auteur ; R1 (« brief, section 6 », document que le
    lecteur ne reçoit pas) mérite d'être tranchée avant la remise.
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
    rapport = os.path.join(ICI, "contre-lecture-consigne-lecteur-issue-pilote-v14-tour1-v1.md")
    if sha(open(rapport, "rb").read()) != RAPPORT_SHA256:
        print("REFUS : empreinte du rapport différente")
        return 2
    v1 = brut.decode("utf-8")
    texte = v1
    for nom, ancien, nouveau in [("en-tête", ENTETE_ANCIEN, ENTETE_NOUVEAU.format(heure=a[0]))] + COUPLES:
        n1, n = v1.count(ancien), texte.count(ancien)
        if n1 != 1 or n != 1:
            print(f"REFUS : {nom} : « ancien » présent {n1} fois dans la v1 et {n} fois dans le texte en cours (une fois exigée)")
            return 2
        texte = texte.replace(ancien, nouveau)
        print(f"{nom} : appliqué")
    if not texte.endswith("\n"):
        print("REFUS : fin de pièce inattendue")
        return 2
    texte += CONTRE_LECTURE
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(texte)
    print(f"écrit : {CIBLE} ({sha(texte.encode('utf-8'))})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
