#!/usr/bin/env python3
"""Construction du brouillon 7 du préenregistrement de la porte G1 à partir du brouillon 6 — v1.

Le brouillon 7 n'est pas écrit à la main : ce programme lit le brouillon 6 (empreinte vérifiée), lui applique
une liste de couples exacts (remplacement d'un passage, remplacement d'une ligne, insertion avant ou après une
ligne), et écrit le brouillon 7. Chaque ancre doit se trouver exactement une fois : sinon arrêt, rien n'est
écrit (R5, aucun repli silencieux). La différence entière entre les deux brouillons se relit par `diff`.

Usage, depuis la racine du dépôt :
    python3 docs/notes/g1-brouillon7-fable-v1/outils/construire_brouillon7_v1.py [--verifier]

Sorties : `brouillons/G1-preenregistrement-v1-brouillon7.md` ; le journal des couples
`docs/notes/g1-brouillon7-fable-v1/journal-couples-brouillon6-vers-brouillon7-v1.json`.
Avec `--verifier`, rien n'est écrit : le programme reconstruit le texte en mémoire et le compare au fichier.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
SOURCE = RACINE / "brouillons" / "G1-preenregistrement-v1-brouillon6.md"
CIBLE = RACINE / "brouillons" / "G1-preenregistrement-v1-brouillon7.md"
JOURNAL = RACINE / "docs/notes/g1-brouillon7-fable-v1/journal-couples-brouillon6-vers-brouillon7-v1.json"
EMPREINTE_SOURCE = "939b56e540fa49ea910bf63f8ded66d67c95cf03a4dfec6ccc7f51622cc601bb"
BRANCHE_CANAL = "origin/canal/conv-audit-n04"


class Arret(Exception):
    pass


def sha(chemin):
    """Empreinte sha256 entière d'un fichier de l'arbre de travail."""
    p = RACINE / chemin
    if not p.is_file():
        raise Arret(f"pièce citée absente de l'arbre : {chemin}")
    return hashlib.sha256(p.read_bytes()).hexdigest()


def e8(chemin, attendu=None):
    """Empreinte abrégée « `xxxxxxxx…` » d'un fichier de l'arbre ; `attendu` (préfixe) est vérifié s'il est donné."""
    h = sha(chemin)
    if attendu and not h.startswith(attendu):
        raise Arret(f"empreinte inattendue pour {chemin} : {h[:16]}… au lieu de {attendu}…")
    return f"`{h[:8]}…`"


def e64(chemin, attendu=None):
    h = sha(chemin)
    if attendu and not h.startswith(attendu):
        raise Arret(f"empreinte inattendue pour {chemin} : {h[:16]}… au lieu de {attendu}…")
    return f"`{h}`"


def e8_canal(chemin, attendu):
    """Empreinte abrégée d'un fichier de la branche du canal, lu par `git show` sans l'afficher."""
    r = subprocess.run(["git", "-C", str(RACINE), "show", f"{BRANCHE_CANAL}:{chemin}"], capture_output=True)
    if r.returncode != 0:
        raise Arret(f"pièce citée absente de {BRANCHE_CANAL} : {chemin}")
    h = hashlib.sha256(r.stdout).hexdigest()
    if not h.startswith(attendu):
        raise Arret(f"empreinte inattendue pour {BRANCHE_CANAL}:{chemin} : {h[:16]}… au lieu de {attendu}…")
    return f"`{h[:8]}…`"


class Texte:
    def __init__(self, contenu):
        self.t = contenu
        self.journal = []

    def _note(self, genre, ancre, ajoute, retire):
        self.journal.append({"n": len(self.journal) + 1, "genre": genre, "ancre": ancre[:120],
                             "signes_ajoutes": ajoute, "signes_retires": retire})

    def remplacer(self, ancien, nouveau):
        n = self.t.count(ancien)
        if n != 1:
            raise Arret(f"passage trouvé {n} fois au lieu d'une : {ancien[:100]!r}")
        self.t = self.t.replace(ancien, nouveau)
        self._note("remplacement de passage", ancien, len(nouveau), len(ancien))

    def _ligne(self, prefixe):
        lignes = self.t.split("\n")
        trouvees = [i for i, l in enumerate(lignes) if l.startswith(prefixe)]
        if len(trouvees) != 1:
            raise Arret(f"ligne commençant par {prefixe[:100]!r} trouvée {len(trouvees)} fois au lieu d'une")
        return lignes, trouvees[0]

    def remplacer_ligne(self, prefixe, nouvelle):
        lignes, i = self._ligne(prefixe)
        ancienne = lignes[i]
        lignes[i] = nouvelle
        self.t = "\n".join(lignes)
        self._note("remplacement de ligne", prefixe, len(nouvelle), len(ancienne))

    def inserer_apres(self, prefixe, texte):
        lignes, i = self._ligne(prefixe)
        lignes[i + 1:i + 1] = texte.split("\n")
        self.t = "\n".join(lignes)
        self._note("insertion après la ligne", prefixe, len(texte), 0)

    def inserer_avant(self, prefixe, texte):
        lignes, i = self._ligne(prefixe)
        lignes[i:i] = texte.split("\n")
        self.t = "\n".join(lignes)
        self._note("insertion avant la ligne", prefixe, len(texte), 0)

    def ajouter_fin_de_ligne(self, prefixe, suffixe):
        lignes, i = self._ligne(prefixe)
        lignes[i] = lignes[i] + suffixe
        self.t = "\n".join(lignes)
        self._note("ajout en fin de ligne", prefixe, len(suffixe), 0)


def couples_en_tete(T):
    """Titre, statut, auteurs, sources, calculs, pièces : aucun critère ici."""
    T.remplacer("(T1.2, E1.2) — v1 — brouillon 6\n", "(T1.2, E1.2) — v1 — brouillon 7\n")
    T.inserer_avant(
        "- **Statut** : brouillon 6.",
        "- **Statut** : brouillon 7. Ni scellé, ni contre-lu : il ne vaut pas préenregistrement (règle R1). Aucun épisode de "
        "G1 n'existe. **Il part du brouillon 6 (`939b56e5…`), qui n'a jamais été contre-lu** : aucune contre-lecture du "
        "brouillon 6 n'est consignée aux registres ni présente dans l'arbre (rapport du sas des registres, § 2) ; la "
        "contre-lecture du brouillon 7 porte donc sur le texte entier, non sur la seule différence. **Ce que le brouillon 7 "
        "fait** : il inscrit ce que Lazar a décidé du 6 au 22 novembre 2026 et qui touche la porte (table « avant → après » "
        "ci-dessous), remplit les marqueurs que des textes scellés depuis remplissent (organismes, sondes), et écrit en clair "
        "ce qui manque encore. Il ne change aucune des treize décisions du 5 novembre, aucun seuil ni aucune prédiction "
        "chiffrée du brouillon 6. Là où une décision de Lazar manque, le texte porte un marqueur `<<…>>`, et la section "
        "« Points ouverts pour Lazar » dit la décision, l'enjeu, les options et la valeur écrite en attendant. **Ce brouillon "
        "est construit par programme** : `docs/notes/g1-brouillon7-fable-v1/outils/construire_brouillon7_v1.py` applique au "
        "brouillon 6 une liste de couples exacts ; la différence entière se relit par `diff`.\n"
        "- **Ce que le rédacteur du brouillon 7 a lu et n'a pas lu** (inscription à la liste « qui a lu quoi » écrite avant "
        "toute pièce de G1 : `docs/notes/g1-brouillon7-fable-v1/inscription-qui-a-lu-quoi-redacteur-g1-brouillon7-v1.md`, "
        + e8("docs/notes/g1-brouillon7-fable-v1/inscription-qui-a-lu-quoi-redacteur-g1-brouillon7-v1.md", "8b81ebae") +
        " ; accusé de la mère) : il n'a ouvert **aucun verdict ni aucune sortie** des étapes mesurées du programme "
        "(organismes et dose-réponse, lecture des sondes entraînées ailleurs, apprentissage des sondes sur la tâche, témoin "
        "positif planté, adaptateur, accumulation des scores sur l'épisode, bras externe sur les données de collusion "
        "publiques, saboteur à budget, bras A des organismes discrets, lentilles), ni le coffre des familles tenues à l'écart, "
        "ni les pièces du bras d'attaque, ni `registres/etat.md`, ni les passations. Les décisions et les notes écrites après "
        "le 13 novembre ont été lues **par un sas** : trois sous-agents neufs (Claude Opus 5.5) qui n'ont rendu que les "
        "énoncés, les exigences, les renvois et les empreintes, issues caviardées (rapports sous "
        "`docs/notes/g1-brouillon7-fable-v1/sas/`). **Deux expositions, déclarées** : (1) les chiffres du premier test boîte "
        "blanche (P3), que le brouillon 6 cite lui-même ; (2) **le sens qualitatif, sans chiffre, du verdict du premier cycle "
        "de l'accumulation des scores sur l'épisode**, lu par accident dans le corps du brouillon de décision N-074 "
        "(section 1), que le programme de lecture sans en-tête n'a pas masqué (déclaré à la mère le 22 novembre 2026 à "
        "18:22 UTC ; journal `docs/notes/g1-brouillon7-fable-v1/journal-lectures-sans-entete-v1.jsonl`). **Aucun paramètre de "
        "ce texte n'en vient** : la table « Paramètres ajoutés par le brouillon 7 et leur source » (section « Chiffres non "
        "sourcés et valeurs à remplir ») donne la source de chaque nombre ajouté, pour que le contre-lecteur le vérifie ; le "
        "rédacteur ne recommande aucun des énoncés du témoin apparié.")
    T.remplacer("- **Statut** : brouillon 6. Ni scellé, ni contre-lu",
                "- **Statut du brouillon 6** (historique, gardé tel quel) : brouillon 6. Ni scellé, ni contre-lu")
    T.inserer_apres(
        "- **Auteurs** :",
        "- **Auteur du brouillon 7** : rédacteur neuf (Claude Fable 5.2, effort maximal, session "
        "`session_013QMaykB3PEpEJf5XzyYe2D`, fille de la session mère `session_013QMayjbmQUdDuDs2S3i3XD`), sur le message de "
        "lancement de la mère (ligne R-4986 du registre des décisions ; GO-2026-11-22-77 et GO-2026-11-22-113), qui n'a écrit "
        "aucun des brouillons 1 à 6, aucune contre-lecture, ni la garde δ, ni le pari, ni le dimensionnement, ni le brouillon "
        "de décision N-074, ni l'étude de la formulation, ni aucune des décisions citées.")
    T.inserer_apres(
        "- **Lecture des sources** :",
        "- **Lecture des sources du brouillon 7** : dépôt principal au commit `fc11cf2e` de `main` (branche "
        "`prep/g1-brouillon7-fable-v1`) ; branche `canal/conv-audit-n04` au commit `adc1be82` pour le brouillon 5, les "
        "décisions en clair et les calculs du brouillon 5, lus par `git show` ; rien lu sous `donnees/`, `diag/`, `runs/`, "
        "`traces/`, `rapports/`, `docs/verdicts/` ; les empreintes des pièces citées par le brouillon 6 ont été recalculées "
        "par programme : toutes celles dont le fichier est sur `main` ou sur la branche du canal sont conformes.")
    T.inserer_apres(
        "- **Calculs propres à ce brouillon** :",
        "- **Calculs propres au brouillon 7** : script `docs/notes/g1-brouillon7-fable-v1/calculs/calculs-g1-brouillon7-v1.py` ("
        + e8("docs/notes/g1-brouillon7-fable-v1/calculs/calculs-g1-brouillon7-v1.py") + "), sortie "
        "`calculs-g1-brouillon7-v1-sortie.txt` ("
        + e8("docs/notes/g1-brouillon7-fable-v1/calculs/calculs-g1-brouillon7-v1-sortie.txt") +
        "), même dossier, rejouée deux fois à l'identique depuis un dossier vide (Python 3.13.18, bibliothèque standard "
        "seule ; aucune donnée du programme lue). Ci-dessous « [calc7 § k] » renvoie au paragraphe k de cette sortie ; "
        "« [calc § k] » reste la sortie du brouillon 5.")


DEC = "docs/decisions/"
SAS = "docs/notes/g1-brouillon7-fable-v1/sas/"
REP = "docs/notes/demandes-fable-api-2026-11-22-v1/"


def couples_pieces(T):
    """Pièces qui font foi ajoutées par le brouillon 7, et état des dépendances au 22 novembre : aucun critère ici."""
    T.inserer_apres(
        "  - **ajoutés par le brouillon 6** :",
        "  - **ajoutés par le brouillon 7** (empreintes recalculées par le programme de construction ; « par le sas » : pièce "
        "lue par un sous-agent, non ouverte par le rédacteur) : **textes scellés des instruments**, par le sas : organismes "
        "et dose-réponse `prereg/T0.6-organismes-v0-v1.md` (" + e8("prereg/T0.6-organismes-v0-v1.md", "ef31feff") +
        ", commit de scellement `935262b1`), sondes `prereg/T0.7-sondes-v0-v1.md` (" + e8("prereg/T0.7-sondes-v0-v1.md", "d7d180ec") +
        ", clé `SCELLEMENT-T07` du registre des scellements), base « mots et coût » `prereg/T0.8-base-A-mots-et-cout-v1.md` ("
        + e8("prereg/T0.8-base-A-mots-et-cout-v1.md", "72b067d5") + "), validité de l'adaptateur "
        "`prereg/validite-adaptateur-v1.md` (" + e8("prereg/validite-adaptateur-v1.md", "7e78909d") + ") ; brouillon 4 gelé, "
        "non scellé, de la base boîte noire `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` ("
        + e8("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md", "7da0c383") + ", par le sas) ; **décisions de Lazar** "
        "lues par le rédacteur : N-061 (" + e8(DEC + "decision-N-061-v1.md", "b2ae4417") + "), N-062 ("
        + e8(DEC + "decision-N-062-v1.md", "63f42690") + "), N-063 v2 (" + e8(DEC + "decision-N-063-v2.md", "b2d9f035") +
        "), N-066 (" + e8(DEC + "decision-N-066-v1.md", "21e83ed5") + ") ; **décisions de Lazar lues par le sas** : N-069 ("
        + e8(DEC + "decision-N-069-v1.md", "6e0d9d40") + "), N-070 (" + e8(DEC + "decision-N-070-v1.md", "7c4ce221") +
        "), N-075 v3 (" + e8(DEC + "decision-N-075-issue-plancher-et-deux-regards-v3.md", "5aed4bab") + ") avec ses errata 1 ("
        + e8(DEC + "decision-N-075-issue-plancher-et-deux-regards-v3-erratum-1.md", "c6efeccf") + "), 2 ("
        + e8(DEC + "decision-N-075-issue-plancher-et-deux-regards-v3-erratum-2.md", "b19852b4") + ") et 3 v2 ("
        + e8(DEC + "decision-N-075-issue-plancher-et-deux-regards-v3-erratum-3-v2.md", "fbe3298e") + ", qui prime), N-076 ("
        + e8(DEC + "decision-N-076-assurance-par-audit-et-reference-honnete-v1.md", "49b664c1") + ") avec ses errata 1 ("
        + e8(DEC + "decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-1.md", "34a59c49") + ", qui prime) et 2 ("
        + e8(DEC + "decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-2.md", "c2943188") + "), N-077 ("
        + e8(DEC + "decision-N-077-retrait-marge-asymetrique-mesure-gardee-v1.md", "41643fc5") + ") ; **brouillon de décision "
        "non pris** : N-074, brouillon 2 (" + e8(DEC + "decision-N-074-v1-brouillon2.md", "29b38fc4") + ") ; **registre des "
        "accords** `registres/go.md` (" + e8("registres/go.md") + " à la construction) : lignes GO-2026-11-06-04, "
        "GO-2026-11-18-48, -49, -56 et -61, GO-2026-11-21-10, -64, -65, -77 et -78, GO-2026-11-22-12, -20, -77 et -113 ; "
        "**étude de la formulation du témoin apparié** : texte scellé `prereg/formulation-g1-simulation-v1.md` ("
        + e8("prereg/formulation-g1-simulation-v1.md", "d04da790") + "), note à Lazar "
        "`docs/notes/formulation-g1-etude-v1/note-a-lazar-formulation-g1-v1.md` ("
        + e8("docs/notes/formulation-g1-etude-v1/note-a-lazar-formulation-g1-v1.md", "779447c1") + "), verdict "
        "`docs/verdicts/verdict-formulation-g1-simulation-v1.md` (" + e8("docs/verdicts/verdict-formulation-g1-simulation-v1.md", "28d874de") +
        ", non ouvert) ; **par le sas** : avis d'Opus sur le mode tenu à l'écart ("
        + e8("docs/notes/avis-opus-mode-tenu-a-l-ecart-g1-v1/avis-opus-max-v1.md", "fa7467b5") + "), réponses de Fable du "
        "22 novembre 2, 5, 7 et 8 (" + e8(REP + "reponse-2/relecture-fable-api.md", "542b7bfc") + ", "
        + e8(REP + "reponse-5/relecture-fable-api.md", "2ac4161e") + ", " + e8(REP + "reponse-7/relecture-fable-api.md", "44ec0278") + ", "
        + e8(REP + "reponse-8/relecture-fable-api.md", "d81a74d3") + "), configuration de génération du calage "
        "`prereg/configuration-generation-calage-g1-v3.json` (" + e8("prereg/configuration-generation-calage-g1-v3.json", "28cf908f") +
        ", en vigueur, non scellée) et sa note v3 (" + e8("docs/notes/configuration-calage-g1-v1/note-configuration-calage-g1-v3.md", "f26cbb42") +
        "), chemins critiques de G1 v1 (" + e8("docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md", "f5599896") + "), v2 brouillon 1 ("
        + e8("docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v2-brouillon1.md", "f3501c6d") + ") et v3 brouillon 1 ("
        + e8("docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v3-brouillon1.md", "b2b702ba") + ") ; **index du scellement 2 "
        "des familles tenues à l'écart**, empreintes seules : v1 (" + e8("registres/index-scellement-2-familles-aveugles-v1.md", "5d0479b4") +
        ") et v3 (" + e8("registres/index-scellement-2-familles-aveugles-v3.md", "cde486b0") + ") ; **rapports du sas** : décisions "
        "tardives (" + e8(SAS + "rapport-sas-decisions-tardives-v1.md", "65da5370") + "), notes tardives ("
        + e8(SAS + "rapport-sas-notes-tardives-v1.md", "4337ef2d") + ") et son complément ("
        + e8(SAS + "rapport-sas-notes-tardives-v1-complement-1.md", "c6d7cc17") + "), registres et marqueurs ("
        + e8(SAS + "rapport-sas-registres-et-marqueurs-v1.md", "3fd9eee2") + ") ; `CLAUDE.md` de `main` (" + e8("CLAUDE.md", "605db83a") + ").")


def couples_faits(T):
    """Faits neufs sans critère : configuration du calage, voisins à citer, devis du témoin, graines, état des dépendances."""
    T.remplacer(
        "noyau « defaut » (configuration de P3, `prereg/P3-premier-test-i-a-v1.md` l. 318-322)",
        "tirage dans la loi entière sans troncature (réglages repris de la configuration de P3, "
        "`prereg/P3-premier-test-i-a-v1.md` l. 318-322, où « defaut » désigne le noyau de calcul de l'attention, non un noyau "
        "d'échantillonnage) ; **la référence est désormais la configuration de génération du calage de G1** "
        "(`prereg/configuration-generation-calage-g1-v3.json`, " + e8("prereg/configuration-generation-calage-g1-v3.json", "28cf908f") +
        ", GO-2026-11-21-77 ; en vigueur et **non scellée** au 22 novembre 2026 : modèle `meta-llama/Llama-3.1-8B-Instruct` à la "
        "révision `0e9e39f2…`, agent nu sans adaptateur, poids en `bfloat16`, lot de 8, une passe unique en fin d'épisode pour "
        "les activations) ; au scellement, ce texte cite par leurs empreintes la version scellée de ce fichier et le relevé de "
        "référence de l'opérateur (`<<EMPREINTE_CONFIGURATION_CALAGE>>`, `<<EMPREINTE_RELEVE_REFERENCE>>`), et fixe le type des "
        "activations lues par les moniteurs gelés (`<<TYPE_ACTIVATIONS_LUES>>` : celui du texte scellé des sondes, ou celui du "
        "banc fermé ; s'ils diffèrent, nœud) ; tout écart du calage d'épreuve à ce fichier est un arrêt (S31)")
    T.ajouter_fin_de_ligne(
        "- **Données antérieures, sur PDF, hors programme**",
        " **Ajoutées par le brouillon 7, d'après le registre des décisions (lignes R-2180 et R-2181, rapportées par le sas ; "
        "non relues sur PDF par le rédacteur : à vérifier avant scellement, R7, `<<VERIF_PDF_VOISINS_NOVEMBRE>>`)** : "
        "2610.12445 (« Caught in the Act » : occupation partielle de H1, le sabotage diffus étant écarté de leur banc ; sondes "
        "faibles à petite taille de modèle) ; 2607.02510 (contre-résultat qui impose la base « maximum sur le temps », ici le "
        "bras C2) ; 2606.20746 (« l'accumulation amplifie une marge présente, elle n'en crée pas » : contre-indice pour H2).")
    T.inserer_apres(
        "- Tout lancement : devis et GO de type « calcul » de Lazar",
        "- **Épisodes du témoin apparié (ajout du brouillon 7 ; [calc7 § 2])**. Le plafond accordé le 5 novembre 2026 a été "
        "calculé **sans aucun épisode de témoin apparié**. Avec K_w = 10 exécutions du témoin par unité pour l'organisme sans "
        "consigne, dans les trois modes, et K_w = 3 pour l'organisme à consigne (section « Témoin apparié »), la variante par "
        "défaut (400 unités) devient, selon l'énoncé retenu :\n"
        "\n"
        "  | énoncé du témoin apparié | épisodes par tâche | épisodes | heures de carte (bas / central / haut) | USD (bas / central / haut) | central × 1,3 |\n"
        "  |---|---|---|---|---|---|\n"
        "  | aucun (brouillon 6, rappel) | 232 | 92 800 | 2 586 / 4 247 / 7 409 | 2 792 / 4 870 / 8 989 | 6 331 |\n"
        "  | garde, ou garde avec contraste rapporté à 5 % | 271 | 108 400 | 3 020 / 4 961 / 8 654 | 3 262 / 5 688 / 10 500 | 7 395 |\n"
        "  | contraste (décisif, ou rapporté sur des épisodes à part), calibrage du témoin de 300 épisodes par cellule, six cellules | 275,5 | 110 200 | 3 070 / 5 043 / 8 798 | 3 316 / 5 783 / 10 674 | 7 518 |\n"
        "  | contraste, calibrage du témoin à l'échelle du calibrage honnête, les deux cellules de la porte (2 × 150 par tâche) | 571 | 228 400 | 6 363 / 10 452 / 18 234 | 6 873 / 11 985 / 22 123 | 15 581 |\n"
        "  | contraste, même échelle, les trois modes de l'organisme sans consigne (3 × 150 par tâche) | 721 | 288 400 | 8 035 / 13 198 / 23 024 | 8 678 / 15 134 / 27 935 | 19 674 |\n"
        "\n"
        "  **Tout énoncé porte l'estimation centrale × 1,3 au-dessus du plafond accordé (6 331 USD) : le plafond est à "
        "réaccorder sur un devis refait après le choix de l'énoncé (nœud de dépense ; point ouvert n° 12).** Non comptés en "
        "plus : une distillation par témoin d'adaptateur et sa remise à l'intensité du saboteur ; l'écriture et l'apprentissage "
        "de la sonde du sujet (point ouvert n° 2) ; les organismes du mode « contrôles affaiblis » (point ouvert n° 16). Ces "
        "chiffres reprennent le modèle de coût du brouillon 5 ([calc § 7]), dont les rythmes datent d'octobre : ils sont à "
        "rechiffrer au pilote, comme le reste.")
    T.ajouter_fin_de_ligne(
        "- **Dérivation** : `SeedSequence(entropy=E, spawn_key=(usage, …))`",
        " **Ajouts du brouillon 7** : les exécutions du témoin apparié emploient la clé de génération (1, t, j) de l'exécution "
        "sabotée j (nombres aléatoires communs entre sabotés, jumeaux honnêtes et témoins) ; usage 9 : exécutions du calibrage "
        "du témoin, si l'énoncé retenu en demande (clé (9, t, j″)) ; usage 10 : rééchantillonnages des analyses secondaires. La "
        "configuration de génération du calage reprend de ce texte la règle de la racine et les clés (8, t, j′) et (1, t, j) : "
        "les changer ici oblige à la changer aussi (version nouvelle, R12).")
    T.inserer_apres(
        "**Dépendances hors de ce texte**",
        "\n**État des dépendances au 22 novembre 2026** (ajout du brouillon 7 ; rapport du sas des registres et des marqueurs, "
        "§ 1, sans aucun résultat) : **D:3 est tranché, option (2)** (ligne R-1624, GO-2026-11-06-04) : le scellement de G1 "
        "n'attend pas le pilote de la couche 2 ; il se fait avec n_h = 400 par défaut et la table de la garde gelée, le pilote "
        "précédant la campagne ; la ligne W21 (le scellement attend-il les verdicts des critères 2, 3 et 4 de G0 ?) n'a toujours "
        "aucune ligne au registre (point ouvert n° 18). **Organismes** : le texte est scellé (`prereg/T0.6-organismes-v0-v1.md`, "
        + e8("prereg/T0.6-organismes-v0-v1.md", "ef31feff") + ") ; il ne porte que le mode « coût », fixe une grille de doses "
        "(0 ; 0,25 ; 0,5 ; 0,75 ; 1) sans recherche de dose sur la boîte noire, et renvoie « diffus » à la base boîte noire. "
        "**Sondes** : le texte est scellé (`prereg/T0.7-sondes-v0-v1.md`, " + e8("prereg/T0.7-sondes-v0-v1.md", "d7d180ec") +
        ") ; il ne définit aucune sonde d'intention du mode « contrôles » (point ouvert n° 2). **Base boîte noire** : la base "
        "« mots et coût » est scellée à part (" + e8("prereg/T0.8-base-A-mots-et-cout-v1.md", "72b067d5") + ") ; le texte complet "
        "est au brouillon 4 gelé, non scellé (" + e8("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md", "7da0c383") +
        "), et une session l'écrit le 22 novembre ; ce brouillon 4 reporte « sous le devis de G1 » quatre comparateurs de la "
        "liste (point ouvert n° 11). **Mode tenu à l'écart** : une famille est scellée au coffre pour ce cycle, une autre en "
        "réserve pour le cycle 2 (index du scellement 2, v1 et v3, empreintes seules). **Oracle de couverture** : des notes de "
        "conception, rien de scellé. **Configuration de génération du calage** : version 3 en vigueur, non scellée. **Rien ne "
        "remplit encore** : le juge du pari porté dans `src/controle_ia/`, la simulation de la garde à la liste exacte, le "
        "contrôle par moitiés jumelles rejoué, le banc neuf et sa procédure d'extraction, la recette d'HELIOS rejouée sur "
        "l'agent (repli (a), k = 12), les PDF de DeLong et d'Obuchowski, la phrase retenue pour la borne de P3. **N'existent "
        "pas** (ligne R-4643) : la prévision de la loi de la référence honnête (N-076), les préenregistrements du bras "
        "d'attaque informé et de l'expérience de lecture de N-054, point 4. Les dates du chemin critique (scellement de G1 "
        "visé fin novembre) sont à recaler sur la porte G0, reportée au plus tard à fin décembre 2026 (GO-2026-11-18-01).")


def construire():
    octets = SOURCE.read_bytes()
    if hashlib.sha256(octets).hexdigest() != EMPREINTE_SOURCE:
        raise Arret("le brouillon 6 n'a pas l'empreinte attendue ; rien n'est écrit")
    T = Texte(octets.decode("utf-8"))
    couples_en_tete(T)
    couples_pieces(T)
    couples_faits(T)
    return T


def main(argv):
    try:
        T = construire()
    except Arret as a:
        print(f"ARRÊT : {a}")
        return 2
    marqueurs = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", T.t)))
    if "--verifier" in argv:
        identique = CIBLE.is_file() and CIBLE.read_text(encoding="utf-8") == T.t
        print("conforme : le fichier est égal au texte reconstruit" if identique else "ÉCART : le fichier diffère du texte reconstruit")
        return 0 if identique else 3
    CIBLE.write_text(T.t, encoding="utf-8")
    JOURNAL.write_text(json.dumps({"source": str(SOURCE.relative_to(RACINE)), "sha256_source": EMPREINTE_SOURCE,
                                   "cible": str(CIBLE.relative_to(RACINE)),
                                   "sha256_cible": hashlib.sha256(T.t.encode("utf-8")).hexdigest(),
                                   "couples": T.journal, "marqueurs": marqueurs}, ensure_ascii=False, indent=1) + "\n",
                       encoding="utf-8")
    print(f"{len(T.journal)} couple(s) appliqué(s) ; {len(T.t.encode('utf-8'))} octets ; {len(marqueurs)} marqueur(s) distinct(s)")
    print("marqueurs : " + " ".join(marqueurs))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
