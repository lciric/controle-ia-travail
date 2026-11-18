"""Fabrique les brouillons 4 du préenregistrement et de l'ordre exploratoire, le brouillon 3 du devis et la
note des différences du second cycle, à partir des brouillons en vigueur, scellés — v1.

Porte dans les textes les choix de Lazar du 18 novembre sur les points à trancher (registre des accords,
ligne GO-2026-11-18-56, point 2 ; registre des décisions, ligne R-3434) : nœuds 1 (b), 2 (a), 4 (oui ; (β) ;
(i) si une offre tient le prix du stockage, sinon (ii)), 5 (a), 6 (b), 7 (empreintes seules ; bras d'attaque
oui ; second modèle reporté), 8 (a) ; propositions 9 à 14 telles qu'écrites. Le nœud 3 (énoncé du contraste à
témoin apparié de la porte de fin de phase 1, A ou C) reste ouvert : il est gardé en marqueur nommé.

Chaque changement est une sous-chaîne ou une ligne remplacée, ou une insertion, avec contrôle du nombre
d'occurrences ; ce qui n'est pas nommé ici reste égal au brouillon source, à l'octet. Chaque changement porte
son rattachement : un choix de Lazar (« nœud k », « proposition k »), une remarque de la vérification des
brouillons 2 (« vérification D-1 »), la « tenue » (version, date, mandat, statut, renvois), ou une
« conséquence » qu'un choix entraîne et que le rédacteur déclare pour la contre-lecture. Aucune donnée lue.
Lancement, depuis la racine du dépôt : python3 -B <ce fichier>
"""
import difflib
import hashlib
from collections import Counter
from pathlib import Path

DOSSIER = "docs/notes/reconception-accumulation-cycle-2-v1/"
SCRIPT = DOSSIER + "pieces-redaction-cycle-2-v1/brouillons4-faire-v1.py"
DIFFERENCES = DOSSIER + "differences-brouillons-3-vers-4-v1.md"
GO = "GO-2026-11-18-56"
POINTS = "1999a6ded7bfdcdc0f29bc1c940873903dc2a15c5c5a8b9f7ca795f0a15890ac"
NOEUD_3 = ("**[NŒUD 3 — OUVERT]** : l'énoncé du contraste à témoin apparié de la porte de fin de phase 1 "
           "(formulation A ou formulation C du brouillon de décision N-074) n'est pas tranché ; il reste à Lazar")


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
        compte = Counter(r.split(" ")[0] for r, _ in self.journal)
        print(f"{self.cible} : {len(self.journal)} changements (" + ", ".join(f"{k} {v}" for k, v in sorted(compte.items()))
              + f") ; lignes retirées {self.retirees}, ajoutées {self.ajoutees}, égales {self.egales}")


# ====================================================================================================
# 1. Préenregistrement
# ====================================================================================================
P = Piece("préenregistrement de la confirmation unique",
          "prereg/accumulation-cycle-2-v1-brouillon3.md",
          "b6ff82087f32583ebb5dd8252e08325ab9126b4dd534caf873c00579fc59d791",
          "prereg/accumulation-cycle-2-v1-brouillon4.md")

# --- tenue ---
P.sub("— v1 — brouillon 3", "— v1 — brouillon 4", "tenue", "version (titre)")
P.sub("brouillon 3 écrit le 2026-11-18 à partir de 19:36 (heures relevées par `date -u`).",
      "brouillon 3 écrit le 2026-11-18 à partir de 19:36 ; brouillon 4 écrit le 2026-11-18 à partir de 21:13 (heures relevées par `date -u`).",
      "tenue", "date")
P.sub("reçue vers 19:35 UTC.",
      "reçue vers 19:35 UTC ; puis par le tour des brouillons 4 — porter dans les textes les choix de Lazar sur les points à trancher (" + GO + ", point 2), le nœud 3 restant ouvert —, reçu vers 21:10 UTC.",
      "tenue", "mandat")
P.ligne("- **Statut**",
        "- **Statut** : **brouillon 4, scellé comme brouillon** = brouillon 3 (`prereg/accumulation-cycle-2-v1-brouillon3.md`, `" + P.empreinte + "`, gardé tel quel, R12 ; sa propre filiation y est écrite) + les choix de Lazar du 18 novembre sur les points à trancher (`" + GO + "`, point 2 : nœuds 1 (b), 2 (a), 4, 5 (a), 6 (b), 7, 8 (a) ; propositions 9 à 14 telles qu'écrites), portés par script (`" + SCRIPT + "`, empreinte dans son compagnon), chaque changement rattaché à un choix dans `" + DIFFERENCES + "` ; rien d'autre que la tenue déclarée (version, date, mandat, statut, renvois). " + NOEUD_3 + " ; ce texte, qui tient cette décision pour extérieure à lui depuis le brouillon 1, n'en préjuge pas. **Pas encore contre-lu** dans cet état. **Non scellable en l'état** : il porte des marqueurs (table en fin de texte) que remplissent la session mère (recette, liste des tâches, lignes de registre), l'analyste du temps 1 (sonde gelée, épreuve plantée, effectif) et le développeur (code). Chemin visé au scellement : `prereg/accumulation-cycle-2-v1.md`.",
        "tenue", "statut ; marqueur nommé du nœud 3")
P.sub("le rédacteur n'a pas ouvert les registres)",
      "le rédacteur n'a pas ouvert les registres, sauf, pour ce brouillon 4, les seules lignes GO-2026-11-18-55, -56 et -57 du registre des accords et R-3434 et R-3435 du registre des décisions, lues par leur numéro)",
      "tenue", "lectures de registre de ce tour, déclarées")
P.sub("transmis par la session mère pendant la rédaction).",
      "transmis par la session mère pendant la rédaction) ; **choix du 18 novembre sur les points à trancher** (mot direct « go autres recos », `" + GO + "`, point 2 ; R-3434 ; texte tranché : points à trancher, brouillon 3, `" + POINTS + "`) : une réplication avant toute revendication (point 1, option (b)) ; mode « coût déclaré gonflé », rejoué à neuf (point 2, option (a)) ; relecture complémentaire du temps 1 accordée, plafond 75 USD, disque d'au moins 250 gigaoctets si une offre tient le prix du stockage, sinon couche par couche (point 4) ; plafond de la famille neuve 275 USD (point 5, option (a)) ; temps 1 sans sonde défendable : cycle rapporté sans lecture (point 6, option (b)) ; dépôt daté des empreintes seules, bras d'attaque lancé, second modèle de base reporté (point 7) ; extraction des tâches fraîches traitée comme une dépense à devis (point 8, option (a)) ; propositions 9 à 14 telles qu'écrites. " + NOEUD_3 + ".",
      "tenue", "décisions qui fondent le texte : choix du 18 novembre ; marqueur nommé du nœud 3")
P.sub("`docs/notes/reconception-accumulation-cycle-2-v1/ordre-exploratoire-temps-1-v1-brouillon3.md` ; devis, `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon2.md` ;",
      "`docs/notes/reconception-accumulation-cycle-2-v1/ordre-exploratoire-temps-1-v1-brouillon4.md` ; devis, `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon3.md` ;",
      "tenue", "renvois à l'ordre exploratoire (brouillon 4) et au devis (brouillon 3)")
P.sub("(empreintes dans leurs compagnons ; le devis reste au brouillon 2) ;",
      "(empreintes dans leurs compagnons ; les points à trancher restent au brouillon 3 : ils sont tranchés, sauf le point 3) ; différences des brouillons 3 aux brouillons 4, `" + DIFFERENCES + "` ;",
      "tenue", "points à trancher inchangés ; note des différences citée")
P.apres("| tenue | version, date, mandat, statut, renvois aux brouillons 3", [
    "",
    "- **Brouillon 4 : pas encore contre-lu.** Il porte les choix de Lazar du 18 novembre (`" + GO + "`, point 2) ; chaque changement est rattaché à son choix dans `" + DIFFERENCES + "`, qui nomme aussi les conséquences que le rédacteur a tirées de ces choix et qu'un contre-lecteur neuf doit juger (réserve « non répliquée » ; ce que la réplication laisse à écrire ; mode connu de l'analyste ; absence du bras d'attaque devenue un écart ; branches de garde laissées en place).",
], "tenue", "état de contre-lecture du brouillon 4")

# --- nœud 1 (b) : une réplication avant toute revendication ---
P.ligne("- **Ce que la répétition change pour ce qui est revendiqué",
        "- **Ce que la répétition change pour ce qui est revendiqué — tranché par Lazar : une réplication avant toute revendication** (points à trancher, point 1, option (b) ; `" + GO + "`). Le niveau de 0,025 vaut **pour un cycle** : la phrase « ce cycle rend “accumuler, propre” » a une probabilité d'erreur d'au plus 0,025 si rien n'est propre. La phrase « un cycle a fini par rendre “accumuler, propre” », après K cycles, ne l'a pas : sous un nul commun à tous les cycles, la probabilité d'au moins une issue positive est au plus 1 − (1 − 0,025)^K, soit ≈ 0,05 à deux cycles, 0,10 à quatre, 0,22 à dix (arithmétique du rédacteur, § 2). **Règle de réplication** : une issue « accumuler, propre » de ce cycle est rapportée avec son compte de cycles, cette borne non corrigée et la réserve « non répliquée » ; **aucune revendication** (papier, jury, financeur) n'en est tirée avant une **seconde lecture de la même sonde gelée, sans la retoucher** (même fichier, même empreinte), sur **une autre famille neuve**, tenue à l'écart, conçue sans rien savoir de la sonde. Cette seconde lecture a son propre préenregistrement, contre-lu et scellé avant que la seconde famille existe, son devis et sa ligne de dépense (devis, section 8 : même devis que la famille de ce cycle, engagé seulement après une issue positive). Si la réplication se lit au même niveau, la probabilité qu'une issue positive fortuite soit ensuite répliquée par hasard est, pour K cycles, d'au plus K × 0,025² sous un nul commun et des lectures indépendantes. **[RÉPLICATION — À ÉCRIRE]** : ce texte ne fixe pas ce qui compte comme une issue répliquée (le même état du cycle ; aux mêmes doses ou à une dose quelconque), ni le mode, la recette et l'effectif de la seconde famille ; le préenregistrement de la réplication les fixe, et tout choix qui toucherait la revendication est un nœud de Lazar.",
        "nœud 1 (b)", "« Suite des cycles » : la règle de réplication remplace « signalé, non tranché » ; ce qui reste à écrire est nommé")
P.sub("tirer une revendication d'une issue positive avant que le point à trancher sur la suite des cycles soit tranché.",
      "tirer une revendication d'une issue positive avant sa réplication (« Suite des cycles », règle de réplication).",
      "nœud 1 (b)", "« Ce qu'aucune issue ne permet » : la revendication attend la réplication")
P.apres("- **réserve « la chaîne ne reconnaît pas un signal propre planté »**", [
    "- **réserve « non répliquée »** : écrite à côté de toute issue « accumuler, propre » tant que la seconde lecture de la même sonde gelée sur une autre famille neuve n'est pas lue : « issue non répliquée : aucune revendication n'en est tirée » (« Suite des cycles », règle de réplication).",
], "conséquence du nœud 1 (b)", "réserve « non répliquée » ajoutée à la liste des réserves (elle ne change aucun état)")

# --- nœud 2 (a) : le mode « coût », rejoué à neuf ---
P.sub("un seul mode de sabotage (celui de la recette scellée de la famille), un seul modèle de base",
      "un seul mode de sabotage — « coût déclaré gonflé », **celui des données de développement**, rejoué à neuf (choix de Lazar, points à trancher, point 2, option (a)) : la famille est neuve par ses tâches et ses adaptateurs, **non par son mode** —, un seul modèle de base",
      "nœud 2 (a)", "frontière, point 6 : le mode est celui du développement")
P.sub("son contenu n'est connu ni du rédacteur, ni de l'analyste, ni du développeur)",
      "son contenu n'est connu ni du rédacteur, ni de l'analyste, ni du développeur, **hors son mode**, que Lazar a fixé : « coût déclaré gonflé », rejoué à neuf — même recette, adaptateurs réappris avec des graines neuves, tâches fraîches ; points à trancher, point 2, option (a))",
      "nœud 2 (a)", "« Métrique », famille neuve : mode fixé, reste de la recette fermé")
P.sub("le mode de sabotage de la famille, révélé au verdict, est nommé dans la phrase, et s'il est celui des données de développement la phrase porte « même mode que le développement »",
      "le mode de sabotage de la famille est nommé dans la phrase : « coût déclaré gonflé », rejoué à neuf (choix de Lazar, points à trancher, point 2, option (a)) ; c'est celui des données de développement, et la phrase porte donc « même mode que le développement »",
      "nœud 2 (a)", "phrase du cycle : mode nommé, « même mode que le développement »")
P.sub("a lu la recette de la famille ou une de ses sorties avant le verdict : lecture invalide, nœud.",
      "a lu la recette de la famille ou une de ses sorties avant le verdict : lecture invalide, nœud (connaître le mode, fixé par Lazar et écrit dans ce texte, n'est pas avoir lu la recette).",
      "conséquence du nœud 2 (a)", "liste d'arrêt : le mode écrit dans ce texte n'est pas une lecture de la recette")

# --- nœuds 4, 5 (a), 8 (a) : dépenses ---
P.ligne("Devis : `docs/notes",
        "Devis : `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon3.md`. Création de la famille sur carte louée (A100 SXM4 80 Go), **sur ligne de GO propre**, plafond **275 USD** (choix de Lazar, points à trancher, point 5, option (a)), après `SCELLEMENT-ACC2` ; relecture complémentaire du temps 1, accordée, sur ligne de GO propre, plafond **75 USD** (point 4) ; extraction des tâches fraîches : **dépense à devis** (point 8, option (a)), devis à écrire après le relevé des compteurs du premier tirage ; bras d'attaque et, après une issue positive seulement, seconde famille de la réplication : devis et lignes à part ; validité, épreuve plantée, lecture et verdict sur processeur, 0 USD. Aucune dépense n'est engagée par ce texte.",
        "nœuds 4, 5 (a) et 8 (a)", "« Calcul et dépense » : renvoi au devis (brouillon 3), plafonds retenus, extraction à devis")

# --- nœud 7 : gestes hors de la session ---
P.sub("- **Dépôt daté chez un tiers**, avant la création de la famille : empreintes de",
      "- **Dépôt daté chez un tiers**, avant la création de la famille (choix de Lazar, points à trancher, point 7 (i) : **les empreintes seules**, sans aucun contenu ; le geste est fait par Lazar) : empreintes de",
      "nœud 7 (i)", "dépôt daté : empreintes seules, geste de Lazar")
P.sub("- **Bras d'attaque informé, chargé de fabriquer un faux positif** (N-056, point 6 (B)) : il reçoit",
      "- **Bras d'attaque informé, chargé de fabriquer un faux positif** (N-056, point 6 (B)) — **lancé** : choix de Lazar, points à trancher, point 7 (ii) ; sa dépense passe par un devis et une ligne à part — : il reçoit",
      "nœud 7 (ii)", "bras d'attaque : lancé")
P.sub("(`<<ATTAQUE_SHA256>>`, ou « non lancé »)",
      "(`<<ATTAQUE_SHA256>>` ; « non lancé » serait désormais un écart au choix de Lazar, donc un nœud)",
      "conséquence du nœud 7 (ii)", "bras d'attaque : son absence devient un écart")
P.sub("l'issue du bras d'attaque informé, s'il est lancé (`ATTAQUE-ACC2`)",
      "l'issue du bras d'attaque informé (`ATTAQUE-ACC2`)",
      "nœud 7 (ii)", "plan, point 2 : « s'il est lancé » retiré")
P.sub("`ATTAQUE-ACC2` (facultative : issue scellée du bras d'attaque)",
      "`ATTAQUE-ACC2` (issue scellée du bras d'attaque, lancé sur le choix de Lazar)",
      "nœud 7 (ii)", "lignes de registre : la ligne du bras d'attaque n'est plus facultative")
P.sub("| empreinte de l'issue scellée du bras d'attaque informé, ou « non lancé » |",
      "| empreinte de l'issue scellée du bras d'attaque informé (lancé : choix de Lazar, points à trancher, point 7 (ii)) |",
      "nœud 7 (ii)", "table des marqueurs : bras d'attaque lancé")
P.sub("sur GO (changer de modèle), l'épreuve plantée est rejouée sur un second modèle de base.",
      "le rejeu de l'épreuve plantée sur un second modèle de base est **reporté** à un cycle suivant ou à la porte de fin de phase 1 (choix de Lazar, points à trancher, point 7 (iii)) : il n'est pas joué dans ce cycle.",
      "nœud 7 (iii)", "second modèle de base : reporté")

# --- propositions 11 et 12 : ajouts du rédacteur retenus ---
P.sub("**ajout du rédacteur, point à trancher 11**)",
      "ajout du rédacteur, **retenu** : points à trancher, point 11)",
      "proposition 11", "second témoin honnête retenu (table des prédictions, C2-D5)")
P.sub("(ajout du rédacteur, point à trancher 11 ; retiré de ce texte s'il n'est pas retenu)",
      "(ajout du rédacteur, retenu : points à trancher, point 11)",
      "proposition 11", "second témoin honnête retenu (« Métrique »)")
P.sub("(ajout du rédacteur, point à trancher 11)",
      "(ajout du rédacteur, retenu : points à trancher, point 11)",
      "proposition 11", "épreuve de la famille à effectif réel et jumeau « différence d'état quelconque » retenus (deux mentions)", n=2)
P.sub("deux adaptateurs (trois avec le second témoin honnête) à la recette",
      "trois adaptateurs (saboteur, témoin, second témoin honnête) à la recette",
      "proposition 11", "plan, point 4 : trois adaptateurs")
P.sub("(C2-D5 ; si le second témoin est retenu)", "(C2-D5)",
      "proposition 11", "réserve « adaptateur particulier » : condition « si le second témoin est retenu » retirée")
P.sub("(Choix de rédaction, point à trancher 12 :",
      "(Choix de rédaction retenu, points à trancher, point 12 :",
      "proposition 12", "plancher tiré dans la covariance de la famille : retenu")

# ====================================================================================================
# 2. Ordre exploratoire
# ====================================================================================================
O = Piece("ordre exploratoire du temps 1",
          DOSSIER + "ordre-exploratoire-temps-1-v1-brouillon3.md",
          "af4cb7fb2e206c9f40137614f485acc5ec67e51c510f476a6a86b2ef2ee5ac60",
          DOSSIER + "ordre-exploratoire-temps-1-v1-brouillon4.md")

O.sub("— v1 — brouillon 3", "— v1 — brouillon 4", "tenue", "version (titre)")
O.sub("brouillon 3 le 2026-11-18 après 19:36.", "brouillon 3 le 2026-11-18 après 19:36 ; brouillon 4 le 2026-11-18 après 21:13.", "tenue", "date")
O.sub("La confirmation est le texte `prereg/accumulation-cycle-2-v1-brouillon3.md`, lu une seule fois sur une famille neuve.",
      "La confirmation est le texte `prereg/accumulation-cycle-2-v1-brouillon4.md`, lu une seule fois sur une famille neuve.",
      "tenue", "renvoi au préenregistrement, brouillon 4")
O.sub("- **Statut** : **brouillon 3** = brouillon 2 (",
      "- **Statut** : **brouillon 4** = brouillon 3 (`ordre-exploratoire-temps-1-v1-brouillon3.md`, `" + O.empreinte + "`, gardé tel quel, R12) + les choix de Lazar du 18 novembre sur les points à trancher (`" + GO + "`, point 2 ; lignes de registre lues par leur numéro), portés par script (`pieces-redaction-cycle-2-v1/brouillons4-faire-v1.py`) ; table en section 11 ; pas encore contre-lu dans cet état. Le brouillon 3 était lui-même : brouillon 2 (",
      "tenue", "statut")

O.sub("Lazar peut en décider autrement, points à trancher, point 14 ; la session mère ne fixe aucun choix d'analyse)",
      "confirmé par Lazar : points à trancher, point 14, tel qu'écrit, `" + GO + "` ; la session mère ne fixe aucun choix d'analyse)",
      "proposition 14", "lot D : les traces de la course arrêtée ne sont pas permises, confirmé")
O.sub("**Lot F — la relecture complémentaire du temps 1**, si elle est accordée (section 4) :",
      "**Lot F — la relecture complémentaire du temps 1**, accordée par Lazar (points à trancher, point 4 ; section 4), une fois sa ligne de dépense inscrite :",
      "nœud 4", "lot F : relecture complémentaire accordée")
O.sub("devis à part (`devis-cycle-2-v1-brouillon2.md`, section 6), ligne de GO propre — plafond et disque à trancher par Lazar (points à trancher, point 4) —,",
      "devis à part (`devis-cycle-2-v1-brouillon3.md`, section 6), ligne de GO propre — accordée par Lazar (points à trancher, point 4) : plafond **75 USD** (une relance entière et sept jours de garde tiennent) ; disque d'**au moins 250 gigaoctets si une offre tient le prix du stockage** (0,08 USD de l'heure au plus : fait à venir, vérifié et écrit par la session mère au lancement), **sinon relecture et apprentissage couche par couche** —,",
      "nœud 4", "section 4 : plafond 75 USD ; disque selon l'offre ; renvoi au devis, brouillon 3")
O.sub("Les données n'existent pas pendant le temps 1 ; la recette et la liste sont scellées et fermées.",
      "Les données n'existent pas pendant le temps 1 ; la recette et la liste sont scellées et fermées. Seul le mode est connu de l'analyste, parce que Lazar l'a fixé et que le préenregistrement l'écrit : « coût déclaré gonflé », rejoué à neuf (points à trancher, point 2, option (a)).",
      "conséquence du nœud 2 (a)", "section 5, point 1 : le mode est connu de l'analyste, le reste de la recette non")
O.ligne("**À une limite, sans principale**",
        "**À une limite, sans principale** (choix de Lazar, points à trancher, point 6, option (b)) : l'analyste rend son rapport, et le temps 1 se clôt en **« temps 1 sans sonde candidate »** : le cycle est **compté et rapporté** tel quel, la famille n'est pas créée, sa recette reste scellée et sert au cycle suivant. Le repli mécanique que décrivait le brouillon 3 (la sonde de dissimulation du premier cycle, purgée de la direction du témoin, gelée comme principale) n'est pas retenu : il n'est ni gelé ni joué.",
        "nœud 6 (b)", "section 8 : sans sonde défendable, cycle rapporté sans lecture ; repli mécanique retiré")
O.fin([
    "## 11. Choix de Lazar portés dans ce brouillon 4",
    "",
    "Source : registre des accords, ligne `" + GO + "`, point 2 (mot direct « go autres recos ») ; registre des décisions, ligne R-3434 ; texte tranché : `points-a-trancher-cycle-2-v1-brouillon3.md`, `" + POINTS + "`. Détail, changement par changement : `differences-brouillons-3-vers-4-v1.md` (même dossier).",
    "",
    "| choix | ce qu'il change dans cet ordre |",
    "|---|---|",
    "| **point 2, option (a)** — mode « coût déclaré gonflé », rejoué à neuf | section 5, point 1 : le mode est connu de l'analyste ; le reste de la recette et la liste des tâches restent fermés (conséquence tirée par le rédacteur, à contre-lire) |",
    "| **point 4** — relecture complémentaire accordée ; plafond 75 USD ; disque d'au moins 250 gigaoctets si une offre tient le prix du stockage, sinon couche par couche | section 2, lot F ; section 4. **Fait à venir** : l'offre de disque, vérifiée par la session mère au lancement |",
    "| **point 6, option (b)** — temps 1 sans sonde défendable : cycle rapporté sans lecture | section 8 : le repli mécanique est retiré |",
    "| **point 14** — choix de rédaction tels qu'écrits | section 2 : lot D (traces de la course arrêtée non permises) confirmé ; condition d'ouverture 3 confirmée telle qu'écrite (les deux verdicts, leur table conjointe si elle est prévue, le verdict de la validité de l'adaptateur) : la ligne « laissé à confirmer » de la section 9 est close par ce choix |",
    "| **points 9, 10, 11, 12, 13** — tels qu'écrits | aucun changement dans cet ordre : il les portait déjà |",
    "| points 1, 5, 7, 8 | aucun changement dans cet ordre : ils portent sur le préenregistrement et le devis |",
    "| **point 3 — ouvert** | aucun : l'énoncé du contraste à témoin apparié de la porte de fin de phase 1 (A ou C) reste à Lazar ; cet ordre n'en dépend pas |",
    "| tenue | version, date, statut, renvois au préenregistrement (brouillon 4) et au devis (brouillon 3), cette section ; rien d'autre : le reste est égal au brouillon 3, à l'octet |",
], "tenue", "section 11 : table des choix portés")

# ====================================================================================================
# 3. Devis
# ====================================================================================================
V = Piece("devis du second cycle",
          DOSSIER + "devis-cycle-2-v1-brouillon2.md",
          "065057f04fa67a55a5f370d782baf8ed738e2b4849bd69427805548608913088",
          DOSSIER + "devis-cycle-2-v1-brouillon3.md")

V.sub("— v1 — brouillon 2", "— v1 — brouillon 3", "tenue", "version (titre)")
V.sub("brouillon 2 le 2026-11-18 après 19:05.", "brouillon 2 le 2026-11-18 après 19:05 ; brouillon 3 le 2026-11-18 après 21:13.", "tenue", "date")
V.sub("- **Statut** : **brouillon 2** = brouillon 1 (",
      "- **Statut** : **brouillon 3** = brouillon 2 (`devis-cycle-2-v1-brouillon2.md`, `" + V.empreinte + "`, gardé tel quel, R12) + les choix de Lazar du 18 novembre sur les points à trancher (`" + GO + "`, point 2 ; lignes de registre lues par leur numéro), portés par script (`pieces-redaction-cycle-2-v1/brouillons4-faire-v1.py`), et la citation que demandait la remarque D-1 de la vérification des brouillons 2 ; **aucun chiffre n'est recalculé** ; table en section 12 ; pas encore contre-lu dans cet état. Le brouillon 2 était lui-même : brouillon 1 (",
      "tenue", "statut")
V.sub("Texte servi : `prereg/accumulation-cycle-2-v1-brouillon2.md`.",
      "Texte servi : `prereg/accumulation-cycle-2-v1-brouillon4.md`.",
      "tenue", "renvoi au préenregistrement, brouillon 4")

V.sub("**Plafond : nœud de Lazar** — 275 USD, ou 250 USD avec un effectif borné à 500 tâches (section 5).",
      "**Plafond : 275 USD** (choix de Lazar, points à trancher, point 5, option (a) ; section 5).",
      "nœud 5 (a)", "section 1 : plafond de la famille neuve")
V.ligne("- **Plafond : nœud de Lazar, deux branches**",
        "- **Plafond : 275 USD** (choix de Lazar, points à trancher, point 5, option (a) ; `" + GO + "`) : il couvre le pire cas P1 jusqu'à 600 tâches, réserve et seconde instance comprises (268). La branche (b) — 250 USD, effectif borné à 500 tâches — n'est pas retenue. Le plafond de 250 USD du brouillon 1 ne couvrait P1 à 600 tâches qu'au débit le plus favorable : retiré.",
        "nœud 5 (a)", "section 5 : plafond retenu, branche (b) écartée")
V.sub("- **Le pire cas P2 ne tient sous aucun des deux plafonds.**",
      "- **Le pire cas P2 ne tient pas sous le plafond.**",
      "nœud 5 (a)", "section 5 : un seul plafond")
V.sub(" Sous la branche (b), une seconde instance à 600 tâches dépasserait 250 USD : elle n'est possible qu'à 500 tâches au plus.",
      "",
      "nœud 5 (a)", "section 5 : phrase propre à la branche (b) retirée")
V.sub("| **275 USD**, ou **250 USD avec N ≤ 500** |", "| **275 USD** |",
      "nœud 5 (a)", "section 10 : ligne proposée pour la famille neuve")

V.ligne("**Plafond et disque : nœud de Lazar, deux fois deux branches**",
        "**Plafond et disque : choix de Lazar** (points à trancher, point 4 ; `" + GO + "`) — la relecture est accordée ; sa dépense reste sous une ligne à part :",
        "nœud 4", "section 6 : relecture complémentaire accordée")
V.ligne("- **plafond (α) 40 USD**",
        "- **plafond (β) 75 USD** : une relance entière et sept jours de garde tiennent (58,8 + 13,4, soit environ 72 USD) ; la branche (α) — 40 USD, aucune relance entière, cinq jours de garde au plus — n'est pas retenue ;",
        "nœud 4", "section 6 : plafond 75 USD")
V.ligne("- **disque (i) au moins 250 Go**",
        "- **disque (i) au moins 250 Go, si une offre tient le prix du stockage** (0,08 USD de l'heure au plus, section 9 ; les offres à gros disque ont un stockage plus cher) — **fait à venir** : la session mère le vérifie sur les offres au lancement et l'écrit ; **sinon disque (ii), relecture et apprentissage couche par couche** (environ 50 Go à la fois, borne d'offre inchangée) : deux relectures de plus, soit environ 2 à 3 USD et 1,6 à 2,5 h de carte de plus (sortie de calcul version 3, `pieces-redaction-cycle-2-v1/sortie-calculs-redaction-cycle-2-v3.txt`, § 9 : 1,7 à 3,3 USD), et l'analyste ne compare les couches qu'après coup.",
        "nœud 4 ; vérification D-1", "section 6 : disque selon l'offre ; surcoût de la branche (ii) cité de la sortie de calcul version 3")
V.sub("| **40 USD** (aucune relance entière, cinq jours de garde au plus), ou **75 USD** |", "| **75 USD** |",
      "nœud 4", "section 10 : ligne proposée pour la relecture complémentaire")
V.sub("| hors de tout plafond proposé (plus de 300) |",
      "| hors du plafond (plus de 300 ; 325 à 474 selon l'effectif : sortie de calcul version 3, § 9) |",
      "vérification D-1", "section 5 : pire cas avec relance entière cité de la sortie de calcul version 3")

V.sub("trois avec le second témoin honnête ; contrôles d'identité",
      "trois avec le second témoin honnête (retenu : points à trancher, point 11 ; ce sont les colonnes « second témoin » qui valent) ; contrôles d'identité",
      "proposition 11", "section 2 : second témoin honnête retenu")
V.sub("pour les données de distillation, deux ou trois adaptateurs, 9 × N",
      "pour les données de distillation, trois adaptateurs, 9 × N",
      "proposition 11", "section 10 : trois adaptateurs")
V.sub("la longueur des épisodes d'un mode de sabotage que le rédacteur ne connaît pas (prise à celle du mode « coût »)",
      "la longueur des épisodes de la famille (prise à celle du mode « coût », qui est désormais le mode de la famille : choix de Lazar, points à trancher, point 2, option (a) ; elle n'est pas mesurée sur des tâches fraîches)",
      "nœud 2 (a)", "section 3 : mode de la famille connu")
V.sub("(étiquetage par sous-agents : devis à joindre à la recette)",
      "(étiquetage par sous-agents : devis à joindre à la recette) — sans objet attendu : le mode retenu, « coût déclaré gonflé », se lit par programme (points à trancher, point 2, option (a)) ; à confirmer par la recette",
      "nœud 2 (a)", "section 8 : mesure du dommage par étiquetage, sans objet attendu")
V.sub("**Nœud de Lazar** (points à trancher, point 8) : dépense à devis, ou travail de session.",
      "**Choix de Lazar** (points à trancher, point 8, option (a)) : **dépense à devis**. La session mère relève d'abord les compteurs du premier tirage (des nombres seuls) et la durée d'une vague ; un devis de l'extraction suit, puis sa ligne de dépense ; le tirage attend cette ligne. **Ce devis reste à écrire** : les trois manques ci-dessus ne sont pas levés par ce brouillon.",
      "nœud 8 (a)", "section 7 : extraction des tâches fraîches, dépense à devis ; devis à écrire")
V.sub("- **Textes à écrire avant le tirage** :",
      "- **Textes à écrire avant le tirage, dès maintenant** (points à trancher, point 13, retenu) :",
      "proposition 13", "section 7 : textes du tirage préparés dès maintenant")
V.sub("(petite dépense, mot direct de Lazar, N-056)",
      "(**lancé** : choix de Lazar, points à trancher, point 7 (ii) ; petite dépense, **non chiffrée ici** : son devis et sa ligne restent à écrire)",
      "nœud 7 (ii)", "section 8 : bras d'attaque lancé, devis à écrire")
V.sub("(changer de modèle : GO)",
      "(**reporté** à un cycle suivant ou à la porte de fin de phase 1 : points à trancher, point 7 (iii) ; aucune dépense dans ce cycle)",
      "nœud 7 (iii)", "section 8 : second modèle de base reporté")
V.sub("(compte ou dépôt externe : nœud ; pas de coût de carte)",
      "(**empreintes seules**, geste fait par Lazar : points à trancher, point 7 (i) ; pas de coût de carte)",
      "nœud 7 (i)", "section 8 : dépôt daté des empreintes seules")
V.sub("si la réplication avant revendication est retenue (points à trancher, point 1) : même devis, seulement après une issue positive ;",
      "pour la **réplication avant revendication, retenue** (points à trancher, point 1, option (b)) : même devis que la famille de ce cycle (sections 4 et 5), **seulement après une issue positive**, sous sa propre ligne de dépense ; rien n'est engagé avant ;",
      "nœud 1 (b)", "section 8 : seconde famille de la réplication, prévue d'avance")
V.fin([
    "## 12. Choix de Lazar portés dans ce brouillon 3",
    "",
    "Source : registre des accords, ligne `" + GO + "`, point 2 (mot direct « go autres recos ») ; registre des décisions, ligne R-3434 ; texte tranché : `points-a-trancher-cycle-2-v1-brouillon3.md`, `" + POINTS + "`. Détail, changement par changement : `differences-brouillons-3-vers-4-v1.md` (même dossier). **Aucun chiffre de ce devis n'est recalculé** : les choix retiennent des branches déjà chiffrées.",
    "",
    "| choix | ce qu'il change dans ce devis |",
    "|---|---|",
    "| **point 1, option (b)** — réplication avant revendication | section 8 : une seconde famille, au même devis, seulement après une issue positive, sous sa propre ligne |",
    "| **point 2, option (a)** — mode « coût déclaré gonflé », rejoué à neuf | section 3 (longueur des épisodes) ; section 8 (étiquetage du dommage sans objet attendu, à confirmer par la recette) |",
    "| **point 4** — relecture complémentaire accordée, plafond 75 USD, disque selon l'offre | section 6 ; section 10. **Fait à venir** : l'offre de disque d'au moins 250 gigaoctets au prix du stockage |",
    "| **point 5, option (a)** — plafond de la famille neuve 275 USD | sections 1, 5 et 10 |",
    "| **point 7** — empreintes seules ; bras d'attaque lancé ; second modèle reporté | section 8. **À écrire** : le devis du bras d'attaque |",
    "| **point 8, option (a)** — extraction des tâches fraîches, dépense à devis | section 7. **À écrire** : le devis de l'extraction, après le relevé des compteurs du premier tirage par la session mère |",
    "| **points 11 et 13** — second témoin honnête retenu ; textes du tirage préparés dès maintenant | sections 2, 7 et 10 |",
    "| remarque **D-1** de la vérification des brouillons 2 | sections 5 et 6 : les deux chiffres sont cités de la sortie de calcul version 3, § 9 |",
    "| points 6, 9, 10, 12, 14 | aucun changement dans ce devis |",
    "| **point 3 — ouvert** | aucun : l'énoncé du contraste à témoin apparié de la porte de fin de phase 1 (A ou C) reste à Lazar ; ses épisodes de témoin relèvent du devis des épisodes de la porte, non de celui-ci |",
    "| tenue | version, date, statut, renvoi au préenregistrement (brouillon 4), cette section ; rien d'autre : le reste est égal au brouillon 2, à l'octet |",
], "tenue", "section 12 : table des choix portés")

# ====================================================================================================
# 4. Écriture, puis note des différences
# ====================================================================================================
assert not Path(DIFFERENCES).exists(), "la note des différences existe déjà : on n'écrase jamais (R12)"
for piece in (P, O, V):
    piece.ecrire()

note = [
    "# Différences des brouillons 3 aux brouillons 4 — second cycle de la lecture « accumuler les scores de sondes sur l'épisode » — v1",
    "",
    "- **Auteur** : rédacteur du second cycle, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Fable 5.2 (`claude-fable-5-2`) ; exclu de toute contre-lecture, lecture ou jugement de ce cycle. **Date (UTC)** : 2026-11-18, après 21:13.",
    "- **Ce que c'est** : la liste de tout ce qui change entre les textes en vigueur et leurs versions neuves, chaque changement rattaché à un choix de Lazar ou à une remarque de la vérification des brouillons 2. Produite par le script qui fabrique les textes (`" + SCRIPT + "`, empreinte dans son compagnon) : ce qui n'est pas listé ici est égal à la source, à l'octet. La sortie de la comparaison ligne à ligne est réduite à son décompte.",
    "- **Source des choix** : registre des accords, ligne `" + GO + "`, point 2 (mot direct de Lazar « go autres recos ») ; registre des décisions, lignes R-3434 et R-3435 ; lignes GO-2026-11-18-55 et -57 lues aussi, sans objet pour ces textes (elles portent sur le saboteur à budget et sur le codage des billets). Texte tranché : `" + DOSSIER + "points-a-trancher-cycle-2-v1-brouillon3.md`, `" + POINTS + "`, inchangé.",
    "- **Choix portés** : nœuds 1 (b), 2 (a), 4 (oui ; (β) ; (i) si une offre tient le prix du stockage, sinon (ii)), 5 (a), 6 (b), 7 (empreintes seules ; bras d'attaque oui ; second modèle reporté), 8 (a) ; propositions 9 à 14 telles qu'écrites.",
    "- " + NOEUD_3 + ". Aucun des trois textes ne penche : le préenregistrement le nomme dans son statut et dans ses décisions, l'ordre exploratoire et le devis dans leur table des choix ; le brouillon de décision `docs/decisions/decision-N-074-v1-brouillon2.md` n'est pas touché.",
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
    "**Le devis change** : les choix sur les points 1, 2, 4, 5, 7, 8, 11 et 13 retiennent des branches qu'il laissait ouvertes ; aucun de ses chiffres n'est recalculé. **Les points à trancher et le brouillon de décision sur la porte de fin de phase 1 ne changent pas.**",
]
for k, piece in enumerate((P, O, V), start=2):
    note += ["", f"## {k}. Changements — {piece.nom}", "", "| n° | rattachement | changement |", "|---|---|---|"]
    for i, (r, m) in enumerate(piece.journal, start=1):
        note.append(f"| {i} | {r} | {m} |")
note += [
    "",
    "## 5. Choix sans changement de texte",
    "",
    "- **Propositions 9 et 10** (ordre des opérations ; une seule sonde décisive, quatre doses, 400 à 600 tâches) : les brouillons 3 les portaient déjà ; rien ne change.",
    "- **Proposition 13** (préparer dès maintenant les textes du tirage) : une mention dans le devis ; les deux textes eux-mêmes (règle du tirage complémentaire, procédure d'extraction portée à cette échelle) ne sont pas de ce tour, et la règle du tirage doit être écrite par une instance qui n'est ni l'analyste ni un auteur de ces textes.",
    "- **Proposition 14** (choix de rédaction) : le préenregistrement les portait déjà ; l'ordre exploratoire les marque confirmés.",
    "- **Nœud 6 (b)** : le préenregistrement comptait déjà « temps 1 clos sans sonde candidate » parmi les cycles clos sans lecture ; seul l'ordre exploratoire change.",
    "",
    "## 6. Conséquences tirées par le rédacteur, à juger par la contre-lecture",
    "",
    "Aucune n'est un choix que les lignes de registre laissent ouvert ; chacune est ce qu'un choix entraîne dans le texte, écrite pour être contredite.",
    "",
    "1. **Réserve « non répliquée »** (nœud 1 (b)) : ajoutée à la liste des réserves du préenregistrement, à côté de toute issue « accumuler, propre ». Les phrases gelées du cycle ne sont pas touchées.",
    "2. **Ce que la réplication laisse à écrire** (nœud 1 (b)) : le préenregistrement fixe la règle (même sonde gelée, sans retouche, autre famille neuve, préenregistrement et devis propres, avant toute revendication) et **ne fixe pas** ce qui compte comme une issue répliquée, ni le mode, la recette et l'effectif de la seconde famille : marqueur nommé **[RÉPLICATION — À ÉCRIRE]**. La borne « au plus K × 0,025² » est une arithmétique écrite dans le texte, sous ses deux hypothèses (nul commun, lectures indépendantes, même niveau) ; elle ne figure dans aucune sortie de calcul scellée.",
    "3. **Mode connu de l'analyste** (nœud 2 (a)) : le mode étant fixé par Lazar et écrit dans le préenregistrement, l'analyste du temps 1 le connaît ; le reste de la recette et la liste des tâches restent fermés (préenregistrement, liste d'arrêt ; ordre exploratoire, section 5, point 1).",
    "4. **Absence du bras d'attaque** (nœud 7 (ii)) : « non lancé » devient un écart au choix de Lazar, donc un nœud ; la réserve « sans bras d'attaque » reste écrite comme garde.",
    "5. **Branches de garde laissées en place** (proposition 11) : « à défaut de second témoin » (épreuve de la famille) et « sans second témoin » (réserve « adaptateur particulier ») restent dans le préenregistrement, pour le cas où le second témoin honnête ne pourrait pas être appris ; les retirer est possible, ce n'est pas fait ici.",
    "6. **Tables de traitement des tours précédents** : laissées telles quelles (elles disent ce qui valait à leur tour) ; la ligne « laissé à confirmer » de l'ordre exploratoire, section 9, est close par sa section 11.",
    "",
    "## 7. Ce qui reste ouvert ou attend un fait à venir",
    "",
    "1. **Nœud 3** — énoncé du contraste à témoin apparié de la porte de fin de phase 1 (A ou C), et sa sous-question (mode sans témoin possible) : à Lazar.",
    "2. **Disque de la relecture complémentaire** (nœud 4) : branche (i) ou (ii) selon qu'une offre d'au moins 250 gigaoctets tient le prix du stockage ; vérifié par la session mère au lancement.",
    "3. **Devis de l'extraction des tâches fraîches** (nœud 8 (a)) : à écrire après le relevé, par la session mère, des compteurs du premier tirage et de la durée d'une vague.",
    "4. **Devis et ligne du bras d'attaque** (nœud 7 (ii)) : à écrire.",
    "5. **Préenregistrement de la réplication** (nœud 1 (b)) : à écrire avant la lecture de ce cycle ; voir la conséquence 2.",
    "6. **Marqueurs du préenregistrement** (quatorze, inchangés) et de l'ordre exploratoire : remplis par la session mère, l'analyste et le développeur, chacun à son heure.",
    "7. **Conditions d'ouverture du temps 1** : les verdicts scellés de la lecture des sondes et de l'apprentissage des sondes sur la tâche, leur table conjointe si elle est prévue, le verdict de la validité de l'adaptateur.",
    "8. **Contre-lecture des brouillons 4** par un agent neuf d'un autre modèle : pas encore faite.",
    "",
]
Path(DIFFERENCES).write_text("\n".join(note), encoding="utf-8")
print(DIFFERENCES + " : écrite")
