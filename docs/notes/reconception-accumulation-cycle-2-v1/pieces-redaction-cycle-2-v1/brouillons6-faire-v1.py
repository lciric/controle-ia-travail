"""Fabrique les brouillons 6 du préenregistrement et de l'ordre exploratoire, le brouillon 5 du devis et la
note des différences du second cycle, à partir des brouillons en vigueur, scellés — v1.

Porte dans les textes les couples exacts V-1 à V-9 de la vérification des brouillons 5
(`prereg/contre-lectures/accumulation-cycle-2-v1-brouillon5-verif1.md`), avec trois consignes de la session
mère reçues avec ce tour :
- V-1 (branche de disque couche par couche contre la levée 2) et V-2 (rejeu de la relecture non fini à
  l'ouverture) sont des décisions de Lazar, portées par des marqueurs, sans pente ; jusqu'à son mot, la
  relecture complémentaire ne part que sous la branche de disque d'au moins 250 gigaoctets ;
- V-4 : la session mère confirme la lecture de la levée 1 (décision R-3481, d'après R-3456 et la
  contre-lecture de la note du chemin critique, point F3) ; « aucun appel de modèle payant » n'est affirmé
  que sur cette source, citée telle que la session mère la transmet (registre des décisions non ouvert) ;
- les marqueurs de la règle de réplication (couple B-1) et du nœud 3 restent sans pente.

Chaque changement est une sous-chaîne ou une ligne remplacée, ou une insertion, avec contrôle du nombre
d'occurrences ; ce qui n'est pas nommé ici reste égal au brouillon source, à l'octet. Chaque changement porte
son rattachement : un couple de la vérification (« couple V-k »), ou la « tenue ». Aucune donnée lue.
Lancement, depuis la racine du dépôt : python3 -B <ce fichier>
"""
import difflib
import hashlib
from collections import Counter
from pathlib import Path

DOSSIER = "docs/notes/reconception-accumulation-cycle-2-v1/"
PIECES = DOSSIER + "pieces-redaction-cycle-2-v1/"
SCRIPT = PIECES + "brouillons6-faire-v1.py"
DIFFERENCES = DOSSIER + "differences-brouillons-5-vers-6-v1.md"
DIFF_45 = DOSSIER + "differences-brouillons-4-vers-5-v1.md"
VERIF = "prereg/contre-lectures/accumulation-cycle-2-v1-brouillon5-verif1.md"
VERIF_SHA = "f4be4b04603f08d00e6769f6e5ee1bb796717ea7cb0a2c9ea6fb23ce7ee25c04"
GO58 = "GO-2026-11-18-58"
GO63 = "GO-2026-11-18-63"
M_REPL = "`<<REGLE_REPLICATION>>`"
M_N3 = "`<<NOEUD_3_PORTE_G1>>`"
M_REJEU = "`<<REJEU_A_L_OUVERTURE>>`"
M_DISQUE = "`<<DISQUE_COUCHE_PAR_COUCHE>>`"
# Dans le préenregistrement, les deux marqueurs de l'ordre exploratoire sont nommés sans chevrons : le
# validateur du préenregistrement ne doit compter que les marqueurs que le préenregistrement porte lui-même.
N_REJEU = "REJEU_A_L_OUVERTURE"
N_DISQUE = "DISQUE_COUCHE_PAR_COUCHE"
REMPLIR_DISQUE = ("que la session mère remplace par le mot de Lazar et sa ligne de GO, ou, s'il n'est pas tranché au scellement, "
                  "par « non tranché : la relecture n'est lancée que sous la branche d'au moins 250 gigaoctets » ; aucune branche n'est préférée ici")
CONFIRMATION = ("la session mère a confirmé la lecture de la levée sur le texte qui l'a posée (R-3456 ; contre-lecture de la note du chemin critique, point F3), "
                "par sa décision R-3481, citée telle qu'elle la transmet (registre des décisions non ouvert par le rédacteur)")

assert hashlib.sha256(Path(VERIF).read_bytes()).hexdigest() == VERIF_SHA, "vérification des brouillons 5 : empreinte"


class Piece:
    def __init__(self, nom, source, empreinte, cible):
        octets = Path(source).read_bytes()
        assert hashlib.sha256(octets).hexdigest() == empreinte, f"{source} n'est pas le brouillon en vigueur"
        self.nom, self.source, self.empreinte, self.cible = nom, source, empreinte, cible
        self.avant = octets.decode("utf-8").split("\n")
        self.lignes = list(self.avant)
        self.journal = []

    def indice(self, prefixe):
        trouves = [i for i, l in enumerate(self.lignes) if l.startswith(prefixe)]
        assert len(trouves) == 1, (self.source, prefixe, len(trouves))
        return trouves[0]

    def ligne(self, prefixe, nouvelle, rattachement, motif):
        self.lignes[self.indice(prefixe)] = nouvelle
        self.journal.append((rattachement, motif))

    def apres(self, prefixe, nouvelles, rattachement, motif):
        i = self.indice(prefixe)
        self.lignes[i + 1:i + 1] = nouvelles
        self.journal.append((rattachement, motif))

    def sub(self, avant, apres_, rattachement, motif, n=1):
        """Remplace une sous-chaîne qui doit figurer exactement n fois dans toute la pièce."""
        compte = sum(l.count(avant) for l in self.lignes)
        assert compte == n, (self.source, avant[:70], compte)
        self.lignes = [l.replace(avant, apres_) for l in self.lignes]
        self.journal.append((rattachement, motif))

    def fin(self, nouvelles, rattachement, motif):
        while self.lignes and self.lignes[-1] == "":
            self.lignes.pop()
        self.lignes += [""] + nouvelles + [""]
        self.journal.append((rattachement, motif))

    def ecrire(self):
        assert not Path(self.cible).exists(), f"{self.cible} existe déjà : on n'écrase jamais (R12)"
        Path(self.cible).write_text("\n".join(self.lignes), encoding="utf-8")
        self.sha = hashlib.sha256(Path(self.cible).read_bytes()).hexdigest()
        ops = difflib.SequenceMatcher(None, self.avant, self.lignes, autojunk=False).get_opcodes()
        self.retirees = sum(i2 - i1 for op, i1, i2, _, _ in ops if op in ("replace", "delete"))
        self.ajoutees = sum(j2 - j1 for op, _, _, j1, j2 in ops if op in ("replace", "insert"))
        self.egales = sum(i2 - i1 for op, i1, i2, _, _ in ops if op == "equal")
        compte = Counter(r.split(" (")[0].split(" ;")[0] for r, _ in self.journal)
        print(f"{self.cible} : {len(self.journal)} changements (" + ", ".join(f"{k} {v}" for k, v in sorted(compte.items()))
              + f") ; lignes retirées {self.retirees}, ajoutées {self.ajoutees}, égales {self.egales}")


# ====================================================================================================
# 1. Préenregistrement
# ====================================================================================================
P = Piece("préenregistrement de la confirmation unique",
          "prereg/accumulation-cycle-2-v1-brouillon5.md",
          "5ef9807c2e7a116349f4dcf98808ff7356674e59fd102de4e90e171180132b6e",
          "prereg/accumulation-cycle-2-v1-brouillon6.md")

# --- tenue ---
P.sub("— v1 — brouillon 5", "— v1 — brouillon 6", "tenue", "version (titre)")
P.sub("brouillon 5 écrit le 2026-11-18 à partir de 21:52 (heures relevées par `date -u`).",
      "brouillon 5 écrit le 2026-11-18 à partir de 21:52 ; brouillon 6 écrit le 2026-11-18 à partir de 22:13 (heures relevées par `date -u`).",
      "tenue", "date")
P.sub("portés par des marqueurs —, reçu vers 21:50 UTC.",
      "portés par des marqueurs —, reçu vers 21:50 UTC ; puis par le tour des brouillons 6 — appliquer les couples exacts V-1 à V-9 de la vérification des brouillons 5, les couples V-1 et V-2 devenant des décisions de Lazar portées par des marqueurs, la lecture de la levée 1 étant confirmée par la session mère (décision R-3481) —, reçu vers 22:12 UTC.",
      "tenue", "mandat")
P.ligne("- **Statut**",
        "- **Statut** : **brouillon 6, scellé comme brouillon** = brouillon 5 (`prereg/accumulation-cycle-2-v1-brouillon5.md`, `" + P.empreinte + "`, gardé tel quel, R12 ; sa propre filiation y est écrite) + les couples exacts de la vérification des brouillons 5 qui portent sur ce texte (`" + VERIF + "`, `" + VERIF_SHA + "` : V-4, V-6, V-7, V-9), portés par script (`" + SCRIPT + "`, empreinte dans son compagnon), chaque changement rattaché à un couple dans `" + DIFFERENCES + "` ; rien d'autre que la tenue déclarée (version, date, mandat, statut, renvois, déclarations de lecture). **Deux décisions de ce texte restent à Lazar, portées par des marqueurs** : la règle de réplication (" + M_REPL + " ; « Suite des cycles ») et le nœud 3 (" + M_N3 + ") : l'énoncé du contraste à témoin apparié de la porte de fin de phase 1 (formulation A ou formulation C du brouillon de décision N-074) n'est pas tranché ; il reste à Lazar ; ce texte, qui tient cette décision pour extérieure à lui depuis le brouillon 1, n'en préjuge pas. Deux autres décisions de Lazar, nées des levées de `" + GO63 + "`, sont portées par des marqueurs de l'ordre exploratoire et du devis, non de ce texte (couples V-1 et V-2). **Pas encore contre-lu** dans cet état. **Non scellable en l'état** : il porte des marqueurs (table en fin de texte) que remplissent Lazar (règle de réplication, nœud 3), la session mère (recette, liste des tâches, lignes de registre), l'analyste du temps 1 (sonde gelée, épreuve plantée, effectif) et le développeur (code). Chemin visé au scellement : `prereg/accumulation-cycle-2-v1.md`.",
        "tenue", "statut")
P.sub("pour ce brouillon 5, les seules lignes GO-2026-11-18-56, -58 et -63 du registre des accords, lues par leur numéro)",
      "pour ce brouillon 5, les seules lignes GO-2026-11-18-56, -58 et -63 du registre des accords, lues par leur numéro ; pour ce brouillon 6, aucune ligne de registre : les décisions R-3456 et R-3481 sont citées telles que la session mère les transmet)",
      "tenue", "lectures de registre de ce tour, déclarées")
P.sub("`docs/notes/reconception-accumulation-cycle-2-v1/ordre-exploratoire-temps-1-v1-brouillon5.md` ; devis, `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon4.md` ;",
      "`docs/notes/reconception-accumulation-cycle-2-v1/ordre-exploratoire-temps-1-v1-brouillon6.md` ; devis, `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon5.md` ;",
      "tenue", "renvois à l'ordre exploratoire (brouillon 6) et au devis (brouillon 5)")
P.sub("différences des brouillons 4 aux brouillons 5, `" + DIFF_45 + "` ;",
      "différences des brouillons 4 aux brouillons 5, `" + DIFF_45 + "` ; différences des brouillons 5 aux brouillons 6, `" + DIFFERENCES + "` ;",
      "tenue", "note des différences 5 vers 6 citée")
P.apres("  - contre-lecture des brouillons 4,", [
    "  - vérification des brouillons 5, `" + VERIF + "`, `" + VERIF_SHA + "` ;",
], "tenue", "documents : vérification des brouillons 5 citée")
P.sub("Devis : `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon4.md`.",
      "Devis : `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon5.md`.",
      "tenue", "« Calcul et dépense » : renvoi au devis (brouillon 5)")

# --- V-4 : levée 1 bornée ; lecture confirmée par la session mère (R-3481) ---
P.sub("lue ici comme le tirage par la règle de sélection, sans appel de modèle —",
      "lue ici comme le tirage par la règle de sélection — lecture confirmée : " + CONFIRMATION + " ; c'est le tirage de sélection des tâches fraîches, dont la lecture est faite par des sous-agents des sessions, 0 USD ; « aucun appel de modèle payant » n'est affirmé que sur cette source —",
      "couple V-4", "décisions : la lecture de la levée 1 est confirmée par la session mère (R-3481) ; « sans appel de modèle » devient « aucun appel de modèle payant », sur cette seule source")
P.sub("la sélection complémentaire (le tirage par la règle de sélection, sans appel de modèle, 0 USD) n'attend ni ce devis ni sa ligne (`" + GO63 + "`, levée 1) : elle attend seulement la règle du tirage complémentaire scellée et contre-lue et son entropie fixée (plan, point 3, inchangé) ;",
      "la sélection complémentaire (le tirage par la règle de sélection, 0 USD) n'attend ni ce devis ni sa ligne (`" + GO63 + "`, levée 1) **parce qu'elle ne fait aucun appel de modèle payant et que la lecture de la levée est confirmée** (décision de la session mère R-3481 ; « Décisions qui fondent ce texte ») : elle attend alors seulement la règle du tirage complémentaire scellée et contre-lue et son entropie fixée (plan, point 3, inchangé) ; si un appel de modèle payant y devenait nécessaire, elle attendrait une ligne de dépense, comme au brouillon 4 ; l'extraction elle-même, si elle est payante, attend toujours sa ligne ;",
      "couple V-4", "« Calcul et dépense » : la condition du couple est écrite comme remplie, source citée ; le repli « sinon » est gardé ; l'extraction payante attend toujours sa ligne")

# --- V-6 : remplir les deux marqueurs de Lazar sans laisser de phrase contraire ---
P.sub("| " + M_N3 + " | nœud 3 : la formulation retenue (A ou C du brouillon de décision N-074) du contraste à témoin apparié de la porte de fin de phase 1, hors de ce texte — ou le mot de Lazar que ce texte se scelle sans lui (la phrase devient alors « nœud 3 non tranché au scellement ; hors de ce texte ») | Lazar, avant le scellement |",
      "| " + M_N3 + " | nœud 3 : la session mère remplace, dans « Décisions qui fondent ce texte », la phrase entière qui commence par ce marqueur et finit par « il reste à Lazar. » — par « **Nœud 3 tranché par Lazar** (`<ligne de GO>`) : formulation [A ou C] du brouillon de décision N-074, hors de ce texte. », ou, sur le mot de Lazar que ce texte se scelle sans lui, par « Nœud 3 non tranché au scellement ; hors de ce texte. » ; le statut, réécrit au scellement, dit de même | Lazar, avant le scellement |",
      "couple V-6", "table des marqueurs : comment le marqueur du nœud 3 se remplit (phrase entière remplacée)")
P.sub("| " + M_REPL + " | issue positive et issue répliquée (« Suite des cycles », règle de réplication) | Lazar (nœud), recopié par la session mère, avant le scellement |",
      "| " + M_REPL + " | issue positive et issue répliquée (« Suite des cycles », règle de réplication) : la session mère remplace le marqueur et le tiret qui le suit, jusqu'à « au même niveau corrigé). », par la règle de Lazar écrite en clair, avec sa ligne de GO | Lazar (nœud), recopié par la session mère, avant le scellement |",
      "couple V-6", "table des marqueurs : comment le marqueur de la règle de réplication se remplit")

# --- V-7 : « issue positive » dans la phrase opérante de la règle de réplication ---
P.sub("une issue « accumuler, propre » de ce cycle est rapportée avec son compte de cycles",
      "une issue positive de ce cycle, au sens de la règle de réplication fixée ci-dessous, est rapportée avec son compte de cycles",
      "couple V-7", "« Suite des cycles » : la phrase opérante ne nomme plus une seule des deux options")

# --- V-9 : la clé de registre de l'ouverture recopie les sorties de la relecture ---
P.sub("`OUVERTURE-TEMPS1-ACC2` (elle écrit si le verdict de la validité de l'adaptateur est scellé et quelles lignes du lot de la validité de l'adaptateur sont ouvertes : `" + GO58 + "`)",
      "`OUVERTURE-TEMPS1-ACC2` (elle écrit si le verdict de la validité de l'adaptateur est scellé et quelles lignes du lot de la validité de l'adaptateur sont ouvertes : `" + GO58 + "` ; elle recopie les empreintes des sorties de la relecture complémentaire, jouée avant elle : `" + GO63 + "`, levée 2 ; ordre exploratoire, section 2, lot F)",
      "couple V-9", "« Lignes de registre » : la ligne d'ouverture recopie les empreintes des sorties de la relecture complémentaire")

# --- entrée de la vérification des brouillons 5 ---
P.apres("- **Brouillon 5 : pas encore contre-lu.**", [
    "",
    "- **Contre-lecture 4** (vérification 1 des brouillons 5 ; l'entrée ci-dessus disait ce qui valait à son tour) — sous-agent neuf de la session mère, Claude Opus 5.5 (`claude-opus-5-5`), autre modèle que le rédacteur ; n'a écrit aucune pièce du second cycle ; ne sera ni analyste, ni opérateur de la relecture complémentaire, ni développeur, ni lecteur, ni juge de ce cycle ; déclaré par lui : même modèle (autre instance) que les contre-lecteurs et vérificateurs des tours précédents. **Brouillon relu** : `prereg/accumulation-cycle-2-v1-brouillon5.md`, `" + P.empreinte + "` (avec l'ordre exploratoire, brouillon 5, le devis, brouillon 4, la note des différences, le script de fabrication et le calcul version 4). **Rapport** : `" + VERIF + "`, `" + VERIF_SHA + "`. Verdict : « scellable après ces couples exacts », et après les deux décisions qui restent à Lazar (règle de réplication ; nœud 3) ; aucun bloquant neuf ; majeurs V-1, V-2 (deux questions neuves à Lazar), V-4 ; mineurs V-3, V-5 à V-9. Rejeux du vérificateur : le script de fabrication rend les brouillons 5 à l'octet ; le calcul version 4 rend sa sortie à l'octet ; seize marqueurs de gabarit, aucun autre problème. Traitement, couple par couple :",
    "",
    "| couple | traitement dans ce brouillon 6 |",
    "|---|---|",
    "| **V-1** (majeur, nœud) — branche de disque couche par couche contre la levée 2 | porte sur l'ordre exploratoire (brouillon 6, section 4) et sur le devis (brouillon 5, section 6) : appliqué tel quel, et porté là-bas, sur la consigne de la session mère, par un marqueur de décision de Lazar (nommé " + N_DISQUE + "), sans pente ; jusqu'à son mot, la relecture ne part que sous la branche d'au moins 250 gigaoctets. Ce texte n'en dépend pas |",
    "| **V-2** (majeur, nœud) — rejeu de la relecture non fini à l'ouverture | porte sur l'ordre exploratoire (brouillon 6, section 8, point 2) : appliqué tel quel, marqueur de décision de Lazar (nommé " + N_REJEU + "), trois branches côte à côte, sans pente. Ce texte n'en dépend pas |",
    "| **V-3**, **V-5** (mineurs) | portent sur l'ordre exploratoire (section 2, lot F) : appliqués tels quels |",
    "| **V-4** (majeur) — levée 1 bornée | **appliqué, la condition étant écrite comme remplie** : la session mère a confirmé la lecture (décision R-3481, d'après R-3456 et la contre-lecture de la note du chemin critique, point F3 ; citée telle qu'elle la transmet) ; la lecture de la sélection est faite par des sous-agents des sessions, 0 USD : « sans appel de modèle » devient « aucun appel de modèle payant », affirmé sur cette seule source ; le repli « sinon » du couple est gardé ; l'extraction, si elle est payante, attend toujours sa ligne (décisions ; « Calcul et dépense ») |",
    "| **V-6** (mineur) — remplir les deux marqueurs sans phrase contraire | **appliqué tel quel**, aux deux lignes de la table des marqueurs |",
    "| **V-7** (mineur) — « issue positive » dans la phrase opérante | **appliqué tel quel** (« Suite des cycles ») |",
    "| **V-8** (mineur) | porte sur le devis (brouillon 5, section 7) : appliqué tel quel |",
    "| **V-9** (mineur) — clé de registre de l'ouverture | **appliqué tel quel** (« Lignes de registre ») |",
    "| tenue | version, date, mandat, statut, déclarations de lecture, renvois à l'ordre exploratoire (brouillon 6) et au devis (brouillon 5), documents cités, cette entrée ; rien d'autre : le reste est égal au brouillon 5, à l'octet |",
    "",
    "- **Brouillon 6 : pas encore contre-lu.** Chaque changement est rattaché à un couple de la vérification des brouillons 5 dans `" + DIFFERENCES + "`.",
], "tenue", "entrée de la vérification des brouillons 5 (brouillon relu, rapport, traitement couple par couple) ; état du brouillon 6")

# ====================================================================================================
# 2. Ordre exploratoire
# ====================================================================================================
O = Piece("ordre exploratoire du temps 1",
          DOSSIER + "ordre-exploratoire-temps-1-v1-brouillon5.md",
          "cb8b3335427e9c5dd11cef77f6c819e7593f6bc4938f040701cd36dddd9af122",
          DOSSIER + "ordre-exploratoire-temps-1-v1-brouillon6.md")

O.sub("— v1 — brouillon 5", "— v1 — brouillon 6", "tenue", "version (titre)")
O.sub("brouillon 5 le 2026-11-18 après 21:52.", "brouillon 5 le 2026-11-18 après 21:52 ; brouillon 6 le 2026-11-18 après 22:13.", "tenue", "date")
O.sub("La confirmation est le texte `prereg/accumulation-cycle-2-v1-brouillon5.md`, lu une seule fois sur une famille neuve.",
      "La confirmation est le texte `prereg/accumulation-cycle-2-v1-brouillon6.md`, lu une seule fois sur une famille neuve.",
      "tenue", "renvoi au préenregistrement, brouillon 6")
O.sub("- **Statut** : **brouillon 5** = brouillon 4 (",
      "- **Statut** : **brouillon 6** = brouillon 5 (`ordre-exploratoire-temps-1-v1-brouillon5.md`, `" + O.empreinte + "`, gardé tel quel, R12) + les couples exacts de la vérification des brouillons 5 qui portent sur cet ordre (`" + VERIF + "`, `" + VERIF_SHA + "` : V-1, V-2, V-3, V-5), portés par script (`pieces-redaction-cycle-2-v1/brouillons6-faire-v1.py`) ; **deux décisions de Lazar y sont portées par des marqueurs, sans pente** : " + M_DISQUE + " (section 4) et " + M_REJEU + " (section 8, point 2) ; table en section 13 ; pas encore contre-lu dans cet état. Le brouillon 5 était lui-même : brouillon 4 (",
      "tenue", "statut")
O.sub("table en section 12 ; pas encore contre-lu dans cet état. Le brouillon 4 était lui-même",
      "table en section 12 ; contre-lu depuis (section 13). Le brouillon 4 était lui-même",
      "tenue", "statut : le brouillon 5 a été vérifié depuis")
O.sub("devis à part (`devis-cycle-2-v1-brouillon4.md`, section 6)", "devis à part (`devis-cycle-2-v1-brouillon5.md`, section 6)",
      "tenue", "section 4 : renvoi au devis, brouillon 5")

# --- V-1 : branche de disque couche par couche et levée 2 : nœud, marqueur ---
O.sub("entre les deux, l'instance est arrêtée et gardée (devis, section 6). Sans ce GO,",
      "entre les deux, l'instance est arrêtée et gardée (devis, section 6). **Sous la branche de disque couche par couche**, la relecture et l'apprentissage alternent d'une couche à l'autre (environ 50 gigaoctets à la fois : devis, section 6) : relire les trois couches avant l'ouverture et n'apprendre qu'après n'y est pas exécutable tel qu'écrit — cas que `" + GO63 + "` ne dit pas : nœud de Lazar, tranché avant le lancement de la relecture ; tant qu'il ne l'est pas, la relecture n'est lancée que sous la branche d'au moins 250 gigaoctets. Ce nœud est porté par le marqueur " + M_DISQUE + ", " + REMPLIR_DISQUE + ". Sans ce GO,",
      "couple V-1", "section 4 : la branche couche par couche n'est pas exécutable sous la levée 2 ; nœud de Lazar, marqueur `<<DISQUE_COUCHE_PAR_COUCHE>>` ; d'ici là, branche d'au moins 250 gigaoctets seule")

# --- V-2 : rejeu non fini à l'ouverture : nœud, marqueur, trois branches ---
O.sub("la relecture complémentaire, jouée avant l'ouverture, n'entre pas dans ce compte ;",
      "la relecture complémentaire, jouée avant l'ouverture, n'entre pas dans ce compte ; si un rejeu de la relecture exigé par le verdict de l'étape B bis n'est pas fini quand les autres conditions d'ouverture sont remplies — cas que `" + GO63 + "` ne dit pas —, la règle est un nœud de Lazar, tranché avant le scellement de cet ordre : " + M_REJEU + ", l'une de (a) l'ouverture attend la fin du rejeu, et la ligne `OUVERTURE-TEMPS1-ACC2` recopie les empreintes de ses sorties ; (b) l'ouverture n'attend pas, le compte court depuis elle, et les sorties du rejeu s'ouvrent à l'analyste par une ligne à part, à leur scellement ; (c) l'ouverture n'attend pas, et le compte est suspendu de l'ouverture à cette ligne à part ;",
      "couple V-2", "section 8, point 2 : rejeu non fini à l'ouverture ; nœud de Lazar, marqueur `<<REJEU_A_L_OUVERTURE>>`, trois branches côte à côte")
O.sub("ni le choix ni cet ordre ne disent que le compte attend |",
      "ni le choix ni cet ordre ne disent que le compte attend ; **porté depuis** (brouillon 6, couple V-2) par le marqueur " + M_REJEU + " de la section 8, point 2 |",
      "couple V-2 (tenue demandée par le couple)", "section 12, ligne de la levée 3 : le point est porté par le marqueur")

# --- V-3 et V-5 : lot F ---
O.sub("**elle est rejouée si le verdict de l'étape B bis l'exige**, sous la même ligne de dépense et son plafond (devis, section 6).",
      "**elle est rejouée si le verdict de l'étape B bis l'exige**, sous la même ligne de dépense et son plafond (devis, section 6) ; la session mère écrit à la ligne de registre de la relecture, avant `OUVERTURE-TEMPS1-ACC2` et sans ouvrir aucune sortie de la relecture, si le verdict l'exige, en citant son passage ; s'il y a rejeu, la ligne `OUVERTURE-TEMPS1-ACC2` recopie les empreintes des sorties d'origine et du rejeu ; pour la part rejouée, seules les sorties du rejeu sont ouvertes à l'analyste, celles d'origine restent scellées et fermées.",
      "couple V-3", "section 2, lot F : qui constate que le verdict exige un rejeu ; quelles sorties s'ouvrent")
O.sub("Tiré par le rédacteur, à contre-lire : aucune sonde n'est apprise sur ces activations avant `OUVERTURE-TEMPS1-ACC2`",
      "**Aucune sonde n'est apprise sur ces activations avant `OUVERTURE-TEMPS1-ACC2`** (tiré de `" + GO63 + "`, qui ne déplace que la relecture ; jugé juste par la vérification des brouillons 5)",
      "couple V-5", "section 2, lot F : « aucune sonde apprise avant l'ouverture » rendu ferme")

O.fin([
    "## 13. Couples de la vérification des brouillons 5 portés dans ce brouillon 6",
    "",
    "Rapport : `" + VERIF + "`, `" + VERIF_SHA + "` (agent neuf, Claude Opus 5.5 ; brouillon relu : `ordre-exploratoire-temps-1-v1-brouillon5.md`, `" + O.empreinte + "`) ; verdict : « scellable après ces couples exacts ». Détail, changement par changement : `differences-brouillons-5-vers-6-v1.md` (même dossier).",
    "",
    "| couple | traitement dans ce brouillon 6 |",
    "|---|---|",
    "| **V-1** (majeur, nœud) — branche de disque couche par couche contre la levée 2 | **appliqué tel quel** (section 4) ; **ajout sur la consigne de la session mère, déclaré** : le nœud est porté par le marqueur " + M_DISQUE + ", sans pente ; jusqu'au mot de Lazar, la relecture ne part que sous la branche d'au moins 250 gigaoctets |",
    "| **V-2** (majeur, nœud) — rejeu de la relecture non fini à l'ouverture | **appliqué tel quel** (section 8, point 2) : marqueur " + M_REJEU + ", trois branches côte à côte, aucune préférée ; la ligne de la levée 3 de la section 12 y renvoie, comme le couple le demande |",
    "| **V-3** (mineur) — rejeu : qui le constate, quelles sorties s'ouvrent | **appliqué tel quel** (section 2, lot F) |",
    "| **V-5** (mineur) — « aucune sonde apprise avant l'ouverture » | **appliqué tel quel** (section 2, lot F) |",
    "| **V-4, V-6, V-7, V-9** | portent sur le préenregistrement (brouillon 6) ; **V-8** et la part de V-1 et de V-4 qui touche le devis : devis, brouillon 5 |",
    "| question voisine que le vérificateur signale sans la juger | **non portée** : l'analyste neuf qui remplace un analyste exposé (section 8, point 4) repart-il avec le reste des 48 heures ? Aucun couple ; à poser à Lazar avec V-2 si la session mère le juge utile |",
    "| **nœud 3 — ouvert** ; **règle de réplication — à Lazar** | aucun : cet ordre ne dépend ni de l'un ni de l'autre |",
    "| tenue | version, date, statut, renvois au préenregistrement (brouillon 6) et au devis (brouillon 5), cette section ; rien d'autre : le reste est égal au brouillon 5, à l'octet |",
    "",
    "**Marqueurs de décision de cet ordre, à remplir avant son scellement** (en plus des marqueurs d'empreintes de la section 2) : " + M_DISQUE + " — " + REMPLIR_DISQUE + " ; " + M_REJEU + " — que la session mère remplace par la branche (a), (b) ou (c) retenue par Lazar et sa ligne de GO.",
], "tenue", "section 13 : table des couples portés ; marqueurs de décision de l'ordre")

# ====================================================================================================
# 3. Devis
# ====================================================================================================
V = Piece("devis du second cycle",
          DOSSIER + "devis-cycle-2-v1-brouillon4.md",
          "b606a87f207cd58b7eba035a44d82841a2983f8f1238cb58656b5d137b37ce36",
          DOSSIER + "devis-cycle-2-v1-brouillon5.md")

V.sub("— v1 — brouillon 4", "— v1 — brouillon 5", "tenue", "version (titre)")
V.sub("brouillon 4 le 2026-11-18 après 21:52.", "brouillon 4 le 2026-11-18 après 21:52 ; brouillon 5 le 2026-11-18 après 22:13.", "tenue", "date")
V.sub("- **Statut** : **brouillon 4** = brouillon 3 (",
      "- **Statut** : **brouillon 5** = brouillon 4 (`devis-cycle-2-v1-brouillon4.md`, `" + V.empreinte + "`, gardé tel quel, R12) + les couples de la vérification des brouillons 5 qui portent sur ce devis (`" + VERIF + "`, `" + VERIF_SHA + "` : V-1, V-4, V-8), portés par script (`pieces-redaction-cycle-2-v1/brouillons6-faire-v1.py`) ; **aucun chiffre n'est recalculé** ; table en section 14 ; pas encore contre-lu dans cet état. Le brouillon 4 était lui-même : brouillon 3 (",
      "tenue", "statut")
V.sub("table en section 13 ; pas encore contre-lu dans cet état. Le brouillon 3 était lui-même",
      "table en section 13 ; contre-lu depuis (section 14). Le brouillon 3 était lui-même",
      "tenue", "statut : le brouillon 4 a été vérifié depuis")
V.sub("Texte servi : `prereg/accumulation-cycle-2-v1-brouillon5.md`.",
      "Texte servi : `prereg/accumulation-cycle-2-v1-brouillon6.md`.",
      "tenue", "renvoi au préenregistrement, brouillon 6")

# --- V-1 ---
V.apres("- **pour les 1 024 passes du témoin distillé**", [
    "- **sous la branche de disque (ii)** (couche par couche, environ 50 Go à la fois) : la relecture et l'apprentissage y alternent d'une couche à l'autre ; relire les trois couches avant l'ouverture et n'apprendre qu'après n'y est pas exécutable tel qu'écrit — cas que `" + GO63 + "` ne dit pas : nœud de Lazar, tranché avant le lancement de la relecture ; tant qu'il ne l'est pas, la relecture n'est lancée que sous la branche (i) ; ce nœud est porté par le marqueur " + M_DISQUE + " (le même que celui de l'ordre exploratoire, section 4), " + REMPLIR_DISQUE + " ;",
], "couple V-1", "section 6 : la branche de disque (ii) n'est pas exécutable sous la levée 2 ; nœud de Lazar, marqueur ; d'ici là, branche (i) seule")

# --- V-4 ---
V.sub("**la sélection complémentaire** (le tirage par la règle de sélection : aucun appel de modèle, 0 USD de carte) **ne l'attend plus**",
      "**la sélection complémentaire** (le tirage par la règle de sélection, dont la lecture est faite par des sous-agents des sessions ; 0 USD de carte) **ne l'attend plus : " + CONFIRMATION + ", et « aucun appel de modèle payant » n'est affirmé que sur cette source**",
      "couple V-4", "section 7 : la condition du couple est écrite comme remplie (lecture confirmée, R-3481) ; « aucun appel de modèle » devient « aucun appel de modèle payant », sur cette seule source")
V.sub("elle part dès que la règle du tirage complémentaire est scellée et contre-lue et que son entropie est fixée (préenregistrement, plan, point 3, inchangé).",
      "elle part dès que la règle du tirage complémentaire est scellée et contre-lue et que son entropie est fixée (préenregistrement, plan, point 3, inchangé) ; si un appel de modèle payant y devenait nécessaire, elle attendrait la ligne de dépense de l'extraction, comme au brouillon 3 ; l'extraction elle-même, si elle est payante, attend toujours sa ligne.",
      "couple V-4", "section 7 : repli « sinon » du couple gardé ; l'extraction payante attend toujours sa ligne")

# --- V-8 ---
V.sub("Le rendement du premier tirage est un compteur que ni le rédacteur ni le contre-lecteur n'ont lu.",
      "Le rendement du premier tirage est un compteur que ni le rédacteur ni le contre-lecteur n'avaient lu au brouillon 3 ; pour le brouillon 4, le rédacteur déclare avoir vu, dans la contre-lecture de la note du chemin critique, des compteurs de la sélection d'octobre (préenregistrement, « Ce que les auteurs savaient ») ; aucun chiffre de ce devis n'en est tiré.",
      "couple V-8", "section 7 : ce que le rédacteur a vu des compteurs de la sélection d'octobre, déclaré")

V.fin([
    "## 14. Couples de la vérification des brouillons 5 portés dans ce brouillon 5",
    "",
    "Rapport : `" + VERIF + "`, `" + VERIF_SHA + "` (agent neuf, Claude Opus 5.5 ; devis relu : brouillon 4, `" + V.empreinte + "`). Détail, changement par changement : `differences-brouillons-5-vers-6-v1.md` (même dossier). **Aucun chiffre de ce devis n'est recalculé ; aucun plafond ne change.**",
    "",
    "| couple | ce qu'il change dans ce devis |",
    "|---|---|",
    "| **V-1** (majeur, nœud) — branche de disque (ii) contre la levée 2 | **appliqué tel quel** (section 6, ligne neuve) ; **ajout sur la consigne de la session mère, déclaré** : marqueur " + M_DISQUE + ", sans pente ; jusqu'au mot de Lazar, la relecture ne part que sous la branche (i), au moins 250 Go. **Conséquence sur les chiffres, sans recalcul** : tant que le nœud n'est pas tranché, le surcoût de la branche (ii) (deux relectures de plus) ne s'applique pas ; si aucune offre d'au moins 250 Go ne tient le prix du stockage, la relecture ne part pas |",
    "| **V-4** (majeur) — levée 1 bornée | **appliqué, la condition étant écrite comme remplie** (section 7) : lecture de la levée confirmée par la session mère (décision R-3481, d'après R-3456 et la contre-lecture de la note du chemin critique, point F3 ; citée telle qu'elle la transmet) ; la lecture de la sélection est faite par des sous-agents des sessions, 0 USD ; « aucun appel de modèle payant » n'est affirmé que sur cette source ; le repli « sinon » du couple est gardé ; l'extraction, si elle est payante, attend toujours sa ligne. La ligne « à confirmer » de la section 13 est close par cette confirmation |",
    "| **V-8** (mineur) — compteurs de la sélection d'octobre | **appliqué tel quel** (section 7) |",
    "| **V-2, V-3, V-5** | portent sur l'ordre exploratoire (brouillon 6) ; **V-6, V-7, V-9** : préenregistrement (brouillon 6) |",
    "| **nœud 3 — ouvert** ; **règle de réplication — à Lazar** | aucun changement |",
    "| tenue | version, date, statut, renvoi au préenregistrement (brouillon 6), cette section ; rien d'autre : le reste est égal au brouillon 4, à l'octet |",
], "tenue", "section 14 : table des couples portés")

# ====================================================================================================
# 4. Écriture, puis note des différences
# ====================================================================================================
assert not Path(DIFFERENCES).exists(), "la note des différences existe déjà : on n'écrase jamais (R12)"
for piece in (P, O, V):
    piece.ecrire()

note = [
    "# Différences des brouillons 5 aux brouillons 6 — second cycle de la lecture « accumuler les scores de sondes sur l'épisode » — v1",
    "",
    "- **Auteur** : rédacteur du second cycle, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Fable 5.2 (`claude-fable-5-2`) ; exclu de toute contre-lecture, lecture ou jugement de ce cycle. **Date (UTC)** : 2026-11-18, après 22:13.",
    "- **Ce que c'est** : la liste de tout ce qui change entre les textes en vigueur et leurs versions neuves, chaque changement rattaché à un couple de la vérification des brouillons 5, ou à la tenue. Produite par le script qui fabrique les textes (`" + SCRIPT + "`, empreinte dans son compagnon) : ce qui n'est pas listé ici est égal à la source, à l'octet. La sortie de la comparaison ligne à ligne est réduite à son décompte.",
    "- **Sources** : vérification des brouillons 5, `" + VERIF + "`, `" + VERIF_SHA + "`, lue en entier ; trois consignes de la session mère reçues avec ce tour (V-1 et V-2 portés par des marqueurs de décision de Lazar, sans pente ; lecture de la levée 1 confirmée, décision R-3481 ; marqueurs de la règle de réplication et du nœud 3 sans pente). **Aucune ligne de registre lue à ce tour** : R-3456 et R-3481 sont cités tels que la session mère les transmet.",
    "- **Quatre décisions restent à Lazar, portées par des marqueurs, aucune penchée** : dans le préenregistrement, la règle de réplication (" + M_REPL + ") et le nœud 3 (" + M_N3 + ") ; dans l'ordre exploratoire, la branche de disque couche par couche sous la levée 2 (" + M_DISQUE + ", aussi nommé au devis) et le rejeu de la relecture non fini à l'ouverture (" + M_REJEU + ", trois branches côte à côte).",
    "",
    "## 1. Fichiers",
    "",
    "| texte | source (empreinte) | version neuve (empreinte) | changements | lignes retirées | lignes ajoutées | lignes égales |",
    "|---|---|---|---|---|---|---|",
]
for piece in (P, O, V):
    note.append(f"| {piece.nom} | `{piece.source}` (`{piece.empreinte}`) | `{piece.cible}` (`{piece.sha}`) | {len(piece.journal)} | {piece.retirees} | {piece.ajoutees} | {piece.egales} |")
note += [
    "",
    "Une ligne « retirée » puis « ajoutée » est le plus souvent une même ligne dont une sous-chaîne change : les paragraphes de ces textes tiennent chacun sur une ligne.",
    "",
    "**Le devis change** (brouillon 5) : les couples V-1, V-4 et V-8 touchent ses sections 6 et 7 ; **aucun de ses chiffres n'est recalculé, aucun plafond ne change**. Aucune pièce de calcul neuve. **Les points à trancher (brouillon 3) et le brouillon de décision sur la porte de fin de phase 1 ne changent pas.**",
]
for k, piece in enumerate((P, O, V), start=2):
    note += ["", f"## {k}. Changements — {piece.nom}", "", "| n° | rattachement | changement |", "|---|---|---|"]
    for i, (r, m) in enumerate(piece.journal, start=1):
        note.append(f"| {i} | {r} | {m} |")
note += [
    "",
    "## 5. Couples de la vérification des brouillons 5 : appliqué ou non",
    "",
    "| couple | état | où |",
    "|---|---|---|",
    "| **V-1** (majeur, nœud) | appliqué tel quel (deux endroits) ; **ajout sur la consigne de la session mère** : marqueur " + M_DISQUE + " et la manière de le remplir ; jusqu'au mot de Lazar, branche d'au moins 250 gigaoctets seule | ordre exploratoire, section 4 ; devis, section 6 |",
    "| **V-2** (majeur, nœud) | appliqué tel quel : marqueur " + M_REJEU + ", branches (a), (b), (c) ; tenue demandée par le couple faite (section 12, ligne de la levée 3) | ordre exploratoire, section 8, point 2 ; section 12 |",
    "| **V-3** (mineur) | appliqué tel quel | ordre exploratoire, section 2, lot F |",
    "| **V-4** (majeur) | **appliqué avec un écart déclaré** (quatre sous-chaînes) : le couple écrivait la levée sous deux conditions (« si elle ne fait aucun appel de modèle et si la lecture est confirmée ») ; la session mère a depuis confirmé la lecture (décision R-3481) et dit que la sélection est lue par des sous-agents des sessions, 0 USD. Les textes écrivent donc la condition comme remplie, **« aucun appel de modèle payant »** au lieu de « aucun appel de modèle », affirmé sur cette seule source, citée ; le repli « sinon, elle attend la ligne de dépense » est gardé sous la forme « si un appel de modèle payant y devenait nécessaire » ; l'extraction, si elle est payante, attend toujours sa ligne | préenregistrement, décisions et « Calcul et dépense » ; devis, section 7 |",
    "| **V-5** (mineur) | appliqué tel quel | ordre exploratoire, section 2, lot F |",
    "| **V-6** (mineur) | appliqué tel quel (deux lignes) | préenregistrement, table des marqueurs |",
    "| **V-7** (mineur) | appliqué tel quel | préenregistrement, « Suite des cycles » |",
    "| **V-8** (mineur) | appliqué tel quel | devis, section 7 |",
    "| **V-9** (mineur) | appliqué tel quel | préenregistrement, « Lignes de registre » |",
    "",
    "## 6. Points que la vérification suivante doit juger",
    "",
    "1. **V-4, « appel de modèle payant »** : le rédacteur n'a pas lu la décision R-3481 ; il la cite telle que la session mère la transmet. La vérification des brouillons 5 rappelait que la décision N-049 traite la construction d'une banque par appels de modèles comme une dépense : dire que la lecture par des sous-agents des sessions vaut 0 USD est la décision de la session mère, non un jugement du rédacteur.",
    "2. **V-1, marqueur ajouté** : le couple ne prévoyait pas de marqueur ; la session mère l'a demandé. Sa règle de remplissage (le mot de Lazar, ou « non tranché : la relecture n'est lancée que sous la branche d'au moins 250 gigaoctets ») est écrite par le rédacteur pour que l'ordre puisse être scellé avant le mot de Lazar sans que la garde tombe. Aucune branche de sortie n'est proposée.",
    "3. **V-2, délai** : le couple dit « tranché avant le scellement de cet ordre » ; le marqueur ne prévoit donc pas de forme « non tranché ».",
    "4. **Les deux marqueurs de l'ordre exploratoire sont nommés sans chevrons dans le préenregistrement** (entrée « Contre-lecture 4 »), pour que son validateur ne compte que les marqueurs qu'il porte lui-même.",
    "5. **Devis, section 13, ligne de la levée 1** (« à confirmer ») : laissée telle quelle, parce qu'elle disait ce qui valait au brouillon 4 ; la section 14 la clôt.",
    "",
    "## 7. Ce qui reste ouvert ou attend un fait à venir",
    "",
    "1. **Règle de réplication** (" + M_REPL + ") : à Lazar ; le préenregistrement ne se scelle pas sans elle.",
    "2. **Nœud 3** (" + M_N3 + ") : formulation A ou C, ou le mot de Lazar que le préenregistrement se scelle sans lui.",
    "3. **Branche de disque couche par couche sous la levée 2** (" + M_DISQUE + ") : à Lazar, avant le lancement de la relecture ; d'ici là, branche d'au moins 250 gigaoctets seule.",
    "4. **Rejeu de la relecture non fini à l'ouverture** (" + M_REJEU + ") : à Lazar, avant le scellement de l'ordre exploratoire ; branches (a), (b), (c).",
    "5. **Repli « sans second témoin »** : ne vaut que sur mot de Lazar (inchangé).",
    "6. **Question voisine, signalée par le vérificateur, non portée** : l'analyste neuf qui remplace un analyste exposé repart-il avec le reste des 48 heures ?",
    "7. **Faits à venir et textes à écrire** : inchangés (note des différences des brouillons 4 aux brouillons 5, § 8, point 5).",
    "8. **Marqueurs du préenregistrement** : seize, inchangés. **Marqueurs de l'ordre exploratoire** : ceux de sa section 2, plus " + M_DISQUE + " et " + M_REJEU + ". **Devis** : " + M_DISQUE + ".",
    "9. **Vérification des brouillons 6** par un agent neuf d'un autre modèle que le rédacteur (R2) : pas encore faite.",
    "",
]
Path(DIFFERENCES).write_text("\n".join(note), encoding="utf-8")
print(DIFFERENCES + " : écrite")
