"""Fabrique les brouillons 5 du préenregistrement et de l'ordre exploratoire, le brouillon 4 du devis et la
note des différences du second cycle, à partir des brouillons en vigueur, scellés — v1.

Porte dans les textes :
- les couples exacts de la contre-lecture des brouillons 4
  (`prereg/contre-lectures/accumulation-cycle-2-v1-brouillon4-cl1.md`) : B-1, M-1 à M-3, G-1 à G-6, m-1 à m-6 ;
- le choix de Lazar GO-2026-11-18-58 (le verdict de la validité de l'adaptateur n'est plus une condition
  d'ouverture du temps 1), par les couples G-1 à G-6 ;
- le choix de Lazar GO-2026-11-18-63 (trois levées du chemin critique : sélection des tâches fraîches non
  bloquante ; relecture complémentaire avant l'ouverture du temps 1 ; temps 1 borné à 48 heures depuis son
  ouverture ; la levée « famille générée pendant le temps 1 » n'est pas accordée).
Deux décisions restent à Lazar et sont portées par des marqueurs que le validateur refuse tant qu'ils ne sont
pas remplis : la règle de réplication (`<<REGLE_REPLICATION>>`, couple B-1) et le nœud 3
(`<<NOEUD_3_PORTE_G1>>`, couple m-1). Aucun des deux n'est penché.

Chaque changement est une sous-chaîne ou une ligne remplacée, ou une insertion, avec contrôle du nombre
d'occurrences ; ce qui n'est pas nommé ici reste égal au brouillon source, à l'octet. Chaque changement porte
son rattachement : un couple de la contre-lecture, « GO-58 » (avec son couple), « GO-63 » (avec sa levée),
ou la « tenue » (version, date, mandat, statut, renvois, déclarations de lecture). Aucune donnée lue.
Lancement, depuis la racine du dépôt : python3 -B <ce fichier>
"""
import difflib
import hashlib
from collections import Counter
from pathlib import Path

DOSSIER = "docs/notes/reconception-accumulation-cycle-2-v1/"
PIECES = DOSSIER + "pieces-redaction-cycle-2-v1/"
SCRIPT = PIECES + "brouillons5-faire-v1.py"
DIFFERENCES = DOSSIER + "differences-brouillons-4-vers-5-v1.md"
CL = "prereg/contre-lectures/accumulation-cycle-2-v1-brouillon4-cl1.md"
CL_SHA = "813176c0c10f98ad9afca3ad6b716b55e409db238f0cd264134e43ab58515f26"
GO58 = "GO-2026-11-18-58"
GO63 = "GO-2026-11-18-63"
CHEMIN = DOSSIER + "chemin-critique-cycle-2-v1.md"
CHEMIN_SHA = "6231a4f219065784c493629c5ae5e7de6377bec4dd43dca8ec2a6b67d34d5757"
CHEMIN_CL_SHA = "7e01cf1cf987948a5169df12cbaedb15efd4724236ab09083bc8f0bba9d6e941"
SORTIE_V4 = PIECES + "sortie-calculs-redaction-cycle-2-v4.txt"
M_REPL = "`<<REGLE_REPLICATION>>`"
M_N3 = "`<<NOEUD_3_PORTE_G1>>`"
N3_AVANT = "**[NŒUD 3 — OUVERT]**"

assert hashlib.sha256(Path(CL).read_bytes()).hexdigest() == CL_SHA, "contre-lecture des brouillons 4 : empreinte"
assert hashlib.sha256(Path(CHEMIN).read_bytes()).hexdigest() == CHEMIN_SHA, "note du chemin critique : empreinte"
assert Path(SORTIE_V4).is_file(), "la sortie de calcul version 4 doit exister avant la fabrication"


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
          "prereg/accumulation-cycle-2-v1-brouillon4.md",
          "92e9021f8efd6f1d6d3f7b2e6c82ae388d5e1c00765a93bcdfa250cf50905f60",
          "prereg/accumulation-cycle-2-v1-brouillon5.md")

# --- tenue ---
P.sub("— v1 — brouillon 4", "— v1 — brouillon 5", "tenue", "version (titre)")
P.sub("brouillon 4 écrit le 2026-11-18 à partir de 21:13 (heures relevées par `date -u`).",
      "brouillon 4 écrit le 2026-11-18 à partir de 21:13 ; brouillon 5 écrit le 2026-11-18 à partir de 21:52 (heures relevées par `date -u`).",
      "tenue", "date")
P.sub("le nœud 3 restant ouvert —, reçu vers 21:10 UTC.",
      "le nœud 3 restant ouvert —, reçu vers 21:10 UTC ; puis par le tour des brouillons 5 — appliquer les couples exacts de la contre-lecture des brouillons 4 et porter les choix de Lazar " + GO58 + " et " + GO63 + ", la règle de réplication (couple B-1) et le nœud 3 restant à Lazar, portés par des marqueurs —, reçu vers 21:50 UTC.",
      "tenue", "mandat")
P.ligne("- **Statut**",
        "- **Statut** : **brouillon 5, scellé comme brouillon** = brouillon 4 (`prereg/accumulation-cycle-2-v1-brouillon4.md`, `" + P.empreinte + "`, gardé tel quel, R12 ; sa propre filiation y est écrite) + les couples exacts de la contre-lecture des brouillons 4 (`" + CL + "`, `" + CL_SHA + "` : B-1, M-1 à M-3, G-1 à G-3, m-1 à m-4, m-6) + les choix de Lazar `" + GO58 + "` (le verdict de la validité de l'adaptateur n'est plus une condition d'ouverture du temps 1 ; réserve écrite) et `" + GO63 + "` (trois levées du chemin critique), portés par script (`" + SCRIPT + "`, empreinte dans son compagnon), chaque changement rattaché à un couple ou à un choix dans `" + DIFFERENCES + "` ; rien d'autre que la tenue déclarée (version, date, mandat, statut, renvois, déclarations de lecture). **Deux décisions restent à Lazar, portées par des marqueurs** : la règle de réplication (" + M_REPL + " ; « Suite des cycles ») et le nœud 3 (" + M_N3 + ") : l'énoncé du contraste à témoin apparié de la porte de fin de phase 1 (formulation A ou formulation C du brouillon de décision N-074) n'est pas tranché ; il reste à Lazar ; ce texte, qui tient cette décision pour extérieure à lui depuis le brouillon 1, n'en préjuge pas. **Pas encore contre-lu** dans cet état. **Non scellable en l'état** : il porte des marqueurs (table en fin de texte) que remplissent Lazar (règle de réplication, nœud 3), la session mère (recette, liste des tâches, lignes de registre), l'analyste du temps 1 (sonde gelée, épreuve plantée, effectif) et le développeur (code). Chemin visé au scellement : `prereg/accumulation-cycle-2-v1.md`.",
        "tenue ; couple m-1", "statut ; le nœud 3 passe du marqueur entre crochets au marqueur de gabarit")
P.sub("et R-3434 et R-3435 du registre des décisions, lues par leur numéro)",
      "et R-3434 et R-3435 du registre des décisions, lues par leur numéro ; pour ce brouillon 5, les seules lignes GO-2026-11-18-56, -58 et -63 du registre des accords, lues par leur numéro)",
      "GO-58 (couple G-1) ; tenue", "lectures de registre de ce tour, déclarées (la ligne -58 est lue au brouillon 5 : la déclaration du brouillon 4 n'est pas réécrite)")

# --- G-1 et GO-63 : décisions qui fondent le texte (avant m-1, qui change la même fin d'alinéa) ---
P.sub("n'est pas tranché ; il reste à Lazar.",
      "n'est pas tranché ; il reste à Lazar. **Ouverture du temps 1 sans le verdict de la validité de l'adaptateur** (mot direct de Lazar « ecommandation : option a, confiance 0,7. go », `" + GO58 + "`, R-3440) : le temps 1 s'ouvre sur les seuls verdicts scellés de la lecture des sondes (étape B) et de l'apprentissage des sondes sur la tâche (étape B bis), et sur leur table conjointe si elle est prévue ; la validité de l'adaptateur vient ensuite, en réserve écrite (« Critères de lecture gelés », réserve « validité de l'adaptateur non jugée à l'ouverture du temps 1 ») ; le lot de la validité de l'adaptateur n'est ouvert à l'analyste que si ses lignes existent (ordre exploratoire, section 2, lot E)."
      " **Trois levées du chemin critique** (mot direct de Lazar, `" + GO63 + "`, R-3459 ; note `" + CHEMIN + "`, `" + CHEMIN_SHA + "`, et sa contre-lecture, `" + CHEMIN_CL_SHA + "`) : (1) la sélection complémentaire des tâches fraîches — la ligne du registre écrit « la relecture de sélection des tâches fraîches n'est plus une étape bloquante (prudence, 0 USD) », lue ici comme le tirage par la règle de sélection, sans appel de modèle — n'attend plus le devis ni la ligne de dépense de l'extraction (« Calcul et dépense ») ; (2) la relecture complémentaire du temps 1 est jouée **avant** l'ouverture du temps 1, par un opérateur écarté des verdicts de l'étape B et de l'étape B bis, sans aucune donnée de la famille, et rejouée si le verdict de l'étape B bis l'exige ; (3) le temps 1 est borné à **48 heures comptées depuis son ouverture**. **Levée non accordée** : générer la famille pendant le temps 1 ; l'ordre « famille créée après le scellement de ce texte » reste (plan, point 2).",
      "GO-58 (couple G-1) ; GO-63", "décisions qui fondent le texte : ouverture sans le verdict de la validité de l'adaptateur ; trois levées, une non accordée")

# --- m-1 : nœud 3 visible du validateur (seconde occurrence : alinéa des décisions ; la première est dans le statut) ---
P.sub(N3_AVANT, M_N3, "couple m-1", "décisions : le nœud 3 est porté par le marqueur de gabarit `<<NOEUD_3_PORTE_G1>>`")

# --- tenue : renvois, déclarations ---
P.sub("`docs/notes/reconception-accumulation-cycle-2-v1/ordre-exploratoire-temps-1-v1-brouillon4.md` ; devis, `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon3.md` ;",
      "`docs/notes/reconception-accumulation-cycle-2-v1/ordre-exploratoire-temps-1-v1-brouillon5.md` ; devis, `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon4.md` ;",
      "tenue", "renvois à l'ordre exploratoire (brouillon 5) et au devis (brouillon 4)")
P.sub("différences des brouillons 3 aux brouillons 4, `" + DOSSIER + "differences-brouillons-3-vers-4-v1.md` ;",
      "différences des brouillons 3 aux brouillons 4, `" + DOSSIER + "differences-brouillons-3-vers-4-v1.md` ; différences des brouillons 4 aux brouillons 5, `" + DIFFERENCES + "` ; arithmétique de la règle de réplication, `" + PIECES + "calculs-redaction-cycle-2-v4.py` et sa sortie `sortie-calculs-redaction-cycle-2-v4.txt` (complément : § 10 seul ; empreintes dans leurs compagnons) ;",
      "tenue ; couple m-6", "note des différences 4 vers 5 et sortie de calcul version 4 citées")
P.apres("  - vérification des brouillons 2,", [
    "  - contre-lecture des brouillons 4, `" + CL + "`, `" + CL_SHA + "` ;",
], "tenue", "documents : contre-lecture des brouillons 4 citée")
P.sub("aucun résultat de l'étape B, de l'étape B bis, de la validité de l'adaptateur ni du témoin positif.",
      "aucun résultat de l'étape B, de l'étape B bis, de la validité de l'adaptateur ni du témoin positif. Pour le brouillon 5, **lu hors de la liste du mandat, déclaré** : de la note du chemin critique et de sa contre-lecture, les seuls passages sur les levées (leviers ; dépendances ; coût en garde) — ils portent des durées et des parts de planification, et la contre-lecture cite les compteurs de la sélection des papiers d'octobre ; aucun résultat d'une étude cloisonnée, rien n'en est employé ici.",
      "tenue", "ce que le rédacteur savait : lecture de la note du chemin critique, déclarée")
P.sub("Devis : `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon3.md`.",
      "Devis : `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon4.md`.",
      "tenue", "« Calcul et dépense » : renvoi au devis (brouillon 4)")

# --- B-1 : la règle de réplication est fixée avant le scellement (nœud de Lazar ; marqueur) ---
P.sub("Cette seconde lecture a son propre préenregistrement, contre-lu et scellé avant que la seconde famille existe,",
      "Cette seconde lecture a son propre préenregistrement, contre-lu et scellé avant que la seconde famille existe (il fixe le mode, la recette et l'effectif de la seconde famille),",
      "couple B-1", "« Suite des cycles » : ce que fixe le préenregistrement de la réplication")
P.sub("**[RÉPLICATION — À ÉCRIRE]** : ce texte ne fixe pas ce qui compte comme une issue répliquée (le même état du cycle ; aux mêmes doses ou à une dose quelconque), ni le mode, la recette et l'effectif de la seconde famille ; le préenregistrement de la réplication les fixe, et tout choix qui toucherait la revendication est un nœud de Lazar.",
      "**Règle de réplication, fixée avant le scellement de ce texte** (nœud de Lazar : elle touche la revendication ; points à trancher, point 1, recommandation retenue : « l'écrire avant la lecture de ce cycle ») : " + M_REPL + " — ce qui compte comme une **issue positive** de ce cycle (« accumuler, propre » seul, ou aussi « propre, sans gain d'accumulation établi ») et ce qui compte comme une **issue répliquée** (le même état ; aux mêmes doses ou à une dose quelconque des quatre ; au même niveau corrigé). Rien de cette règle ne peut être écrit ni changé après `LECTURE-ACC2`.",
      "couple B-1", "« Suite des cycles » : la définition d'une issue positive et d'une issue répliquée est un nœud de Lazar, portée par le marqueur `<<REGLE_REPLICATION>>`, fixée avant le scellement")
P.apres("| `<<ATTAQUE_SHA256>>` |", [
    "| " + M_REPL + " | issue positive et issue répliquée (« Suite des cycles », règle de réplication) | Lazar (nœud), recopié par la session mère, avant le scellement |",
    "| " + M_N3 + " | nœud 3 : la formulation retenue (A ou C du brouillon de décision N-074) du contraste à témoin apparié de la porte de fin de phase 1, hors de ce texte — ou le mot de Lazar que ce texte se scelle sans lui (la phrase devient alors « nœud 3 non tranché au scellement ; hors de ce texte ») | Lazar, avant le scellement |",
], "couple B-1 ; couple m-1", "table des marqueurs : `<<REGLE_REPLICATION>>` et `<<NOEUD_3_PORTE_G1>>`")
P.sub("d'au plus K × 0,025² sous un nul commun et des lectures indépendantes.",
      "d'au plus K × 0,025² sous un nul commun et des lectures indépendantes (arithmétique du rédacteur, version 4, § 10 : `" + SORTIE_V4 + "`, empreinte dans son compagnon ; des formules, aucun chiffre lu ; la borne reste au plus égale à 0,025 jusqu'à quarante cycles).",
      "couple m-6", "« Suite des cycles » : renvoi à la sortie de calcul version 4, § 10")

# --- M-1 : le repli « sans second témoin » ne vaut que sur mot de Lazar ---
P.sub("à défaut de second témoin : moitiés par tâche des textes honnêtes lus sous l'état témoin (limite déclarée : les deux membres ne partagent plus leurs textes)",
      "à défaut de second témoin — écart au choix de Lazar (points à trancher, point 11) : nœud ; ce qui suit ne vaut que sur son mot — : moitiés par tâche des textes honnêtes lus sous l'état témoin (limite déclarée : les deux membres ne partagent plus leurs textes)",
      "couple M-1", "« Deux passages » : le repli sans second témoin est un nœud")
P.sub("sans second témoin : « particularité de l'adaptateur non mesurée » est écrit à côté de toute issue « propre » ;",
      "sans second témoin (écart au choix de Lazar, accepté par son mot : voir « Deux passages ») : « particularité de l'adaptateur non mesurée » est écrit à côté de toute issue « propre » ;",
      "couple M-1", "réserve « adaptateur particulier » : la branche sans second témoin renvoie au mot de Lazar")

# --- M-2 : ce que l'analyste connaît de la recette ---
P.sub("**hors son mode**, que Lazar a fixé : « coût déclaré gonflé », rejoué à neuf — même recette, adaptateurs réappris avec des graines neuves, tâches fraîches ; points à trancher, point 2, option (a))",
      "**hors son mode et le fait qu'elle reprend la recette du développement**, que Lazar a fixés : « coût déclaré gonflé », rejoué à neuf — même recette, adaptateurs réappris avec des graines neuves, tâches fraîches ; points à trancher, point 2, option (a) ; restent fermés le texte scellé de la recette, sa règle du tirage, son entropie et tout ce qu'elle précise au-delà)",
      "couple M-2", "« Métrique », famille neuve : connus, le mode et la reprise de la recette du développement ; le reste fermé")
P.sub("(connaître le mode, fixé par Lazar et écrit dans ce texte, n'est pas avoir lu la recette)",
      "(connaître le mode et le fait que la recette reprend celle du développement, fixés par Lazar et écrits dans ce texte, n'est pas avoir lu la recette)",
      "couple M-2", "liste d'arrêt : même précision")

# --- M-3 : les réserves écrites par le code et éprouvées ---
P.sub("garde qui sépare les scores de sonde (aucune moyenne ni médiane sur les jetons) de la mesure d'intensité (moyenne sur les jetons d'une divergence) ;",
      "garde qui sépare les scores de sonde (aucune moyenne ni médiane sur les jetons) de la mesure d'intensité (moyenne sur les jetons d'une divergence) ; écriture de chaque réserve à partir des lignes du registre propre (dont `OUVERTURE-TEMPS1-ACC2` pour la réserve « validité de l'adaptateur non jugée à l'ouverture du temps 1 », et la réserve « non répliquée » à côté de toute issue positive au sens de la règle de réplication), éprouvée sur un cas où elle s'applique et sur un cas où elle ne s'applique pas ;",
      "couple M-3", "« Code neuf » : chaque réserve écrite par le code et éprouvée dans les deux cas (R5)")

# --- G-2 et G-3 : portage de GO-58 ---
P.sub("`OUVERTURE-TEMPS1-ACC2` ; `TACHES-ACC2` (liste ordonnée",
      "`OUVERTURE-TEMPS1-ACC2` (elle écrit si le verdict de la validité de l'adaptateur est scellé et quelles lignes du lot de la validité de l'adaptateur sont ouvertes : `" + GO58 + "`) ; `TACHES-ACC2` (liste ordonnée",
      "GO-58 (cohérence avec le couple G-2, hors couple, déclaré)", "« Lignes de registre » : ce qu'écrit la ligne d'ouverture du temps 1")
P.sub("→ ouverture du temps 1 (`OUVERTURE-TEMPS1-ACC2`) →",
      "→ ouverture du temps 1 (`OUVERTURE-TEMPS1-ACC2` ; conditions : ordre exploratoire, section 2 ; la ligne écrit si le verdict de la validité de l'adaptateur est scellé et quelles lignes du lot de la validité de l'adaptateur sont ouvertes, `" + GO58 + "`) →",
      "GO-58 (couple G-2)", "plan, point 2 : ce qu'écrit la ligne d'ouverture du temps 1")
P.apres("- **réserve « non répliquée »**", [
    "- **réserve « validité de l'adaptateur non jugée à l'ouverture du temps 1 »** (choix de Lazar, `" + GO58 + "`) : si la ligne `OUVERTURE-TEMPS1-ACC2` écrit que le verdict de la validité de l'adaptateur n'était pas scellé, écrite à côté de **toute** phrase du cycle : « sonde conçue avant le verdict de la validité de l'adaptateur ; lot de la validité de l'adaptateur [ouvert / fermé] au temps 1 ; témoin de l'apprentissage de la sonde principale : [témoin distillé honnête / adaptateur témoin du premier cycle / sans objet] », complétée par l'issue de ce verdict s'il est scellé avant `VERDICT-ACC2` (« verdict de la validité de l'adaptateur : [issue], scellé le [date] »), sinon par « verdict de la validité de l'adaptateur non scellé au verdict de ce cycle ». Si ce verdict, scellé avant `SCELLEMENT-ACC2`, met en cause le témoin distillé honnête ou la remise à l'échelle par la divergence que ce texte emploie (« Métrique », « Intensité »), c'est un nœud de Lazar avant le scellement (changement de la famille : plan, point 1). Elle ne change aucun état.",
], "GO-58 (couple G-3)", "réserve « validité de l'adaptateur non jugée à l'ouverture du temps 1 » ajoutée après la réserve « non répliquée »")

# --- m-2 : la réserve « non répliquée » après une réplication lue ---
P.sub("écrite à côté de toute issue « accumuler, propre » tant que la seconde lecture de la même sonde gelée sur une autre famille neuve n'est pas lue : « issue non répliquée : aucune revendication n'en est tirée »",
      "écrite à côté de toute issue positive au sens de la règle de réplication tant que la seconde lecture de la même sonde gelée sur une autre famille neuve n'a pas rendu une issue répliquée : « issue non répliquée : aucune revendication n'en est tirée » ; si elle est lue sans la rendre : « réplication échouée : aucune revendication n'en est tirée »",
      "couple m-2", "réserve « non répliquée » : issue positive au sens de la règle ; « réplication échouée » si la seconde lecture ne la rend pas")

# --- m-3 : dépôt daté chez un tiers aligné sur le choix de Lazar ---
P.sub("dépôt daté chez un tiers, s'il est accordé (`DEPOT-TIERS-ACC2`)",
      "dépôt daté chez un tiers, accordé (empreintes seules, geste de Lazar : points à trancher, point 7 (i)) (`DEPOT-TIERS-ACC2`)",
      "couple m-3", "plan, point 2 : dépôt daté accordé")
P.sub("`DEPOT-TIERS-ACC2` (facultative)",
      "`DEPOT-TIERS-ACC2` (geste de Lazar, accordé ; si elle manque, réserve « sans dépôt daté chez un tiers »)",
      "couple m-3", "lignes de registre : la ligne du dépôt daté n'est plus dite facultative")

# --- GO-63 : trois levées ; une non accordée ---
P.sub("**Temps 1** (développement, ordre exploratoire) : l'analyste autorisé conçoit",
      "**Temps 1** (développement, ordre exploratoire ; **borné à 48 heures comptées depuis son ouverture** : choix de Lazar, `" + GO63 + "`, levée 3 ; ordre exploratoire, section 8, point 2) : l'analyste autorisé conçoit",
      "GO-63 (levée 3)", "plan, point 1 : temps 1 borné à 48 heures depuis son ouverture")
P.sub("aucun de ses adaptateurs n'est appris, aucun de ses épisodes n'est joué. Une ligne manquante",
      "aucun de ses adaptateurs n'est appris, aucun de ses épisodes n'est joué (ordre maintenu par Lazar : la levée « famille générée pendant le temps 1 » n'est pas accordée, `" + GO63 + "`). Une ligne manquante",
      "GO-63 (levée non accordée)", "plan, point 2 : la famille reste créée après le scellement de ce texte")
P.sub("relecture complémentaire du temps 1, accordée, sur ligne de GO propre, plafond **75 USD** (point 4) ;",
      "relecture complémentaire du temps 1, accordée, sur ligne de GO propre, plafond **75 USD** (point 4), **jouée avant l'ouverture du temps 1** par un opérateur écarté des verdicts de l'étape B et de l'étape B bis, sans aucune donnée de la famille, et rejouée si le verdict de l'étape B bis l'exige (`" + GO63 + "`, levée 2 ; ordre exploratoire, section 2, lot F ; devis, section 6) ;",
      "GO-63 (levée 2)", "« Calcul et dépense » : relecture complémentaire avant l'ouverture du temps 1")
P.sub("devis à écrire après le relevé des compteurs du premier tirage ;",
      "devis à écrire après le relevé des compteurs du premier tirage ; la sélection complémentaire (le tirage par la règle de sélection, sans appel de modèle, 0 USD) n'attend ni ce devis ni sa ligne (`" + GO63 + "`, levée 1) : elle attend seulement la règle du tirage complémentaire scellée et contre-lue et son entropie fixée (plan, point 3, inchangé) ;",
      "GO-63 (levée 1)", "« Calcul et dépense » : la sélection des tâches fraîches n'attend plus la ligne de dépense de l'extraction")

# --- m-4 : entrée de la contre-lecture des brouillons 4 ---
P.apres("- **Brouillon 4 : pas encore contre-lu.**", [
    "",
    "- **Contre-lecture 3** (contre-lecture 1 des brouillons 4 ; l'entrée ci-dessus disait ce qui valait à son tour) — sous-agent neuf de la session mère, Claude Opus 5.5 (`claude-opus-5-5`), autre modèle que le rédacteur ; n'a écrit aucune pièce du second cycle ; ne sera ni analyste, ni développeur, ni lecteur, ni juge de ce cycle ; déclaré par lui : même modèle (autre instance) que les contre-lecteurs et le vérificateur des tours précédents. **Brouillon relu** : `prereg/accumulation-cycle-2-v1-brouillon4.md`, `" + P.empreinte + "` (avec l'ordre exploratoire, brouillon 4, le devis, brouillon 3, la note des différences et le script de fabrication). **Rapport** : `" + CL + "`, `" + CL_SHA + "`. Verdict : « scellable après le nœud 3 et ces couples exacts » (un bloquant, B-1, qui exige une décision de Lazar ; majeurs M-1 à M-3 et G-1 à G-5 ; mineurs m-1 à m-6 et G-6). Rejeux du contre-lecteur : le script de fabrication rend les brouillons 4 à l'octet ; quatorze marqueurs de gabarit, aucun autre problème ; deux marqueurs entre crochets que le validateur ne voyait pas. Traitement, couple par couple :",
    "",
    "| couple | traitement dans ce brouillon 5 |",
    "|---|---|",
    "| **B-1** (bloquant) — définition d'une issue positive et d'une issue répliquée, avant la lecture | **appliqué tel quel**, aux trois endroits (« Suite des cycles », deux sous-chaînes ; table des marqueurs) : la règle est un nœud de Lazar, portée par " + M_REPL + " ; **le rédacteur n'écrit pas la règle** et ne reprend pas dans ce texte la recommandation du contre-lecteur, qui reste dans son rapport, pour Lazar |",
    "| **M-1** (majeur) — repli « sans second témoin » sous nœud | **appliqué tel quel**, aux deux endroits (« Deux passages » ; réserve « adaptateur particulier ») |",
    "| **M-2** (majeur) — ce que l'analyste connaît de la recette | **appliqué tel quel**, aux deux endroits de ce texte (« Métrique » ; « Liste d'arrêt ») et dans l'ordre exploratoire, section 5, point 1 |",
    "| **M-3** (majeur) — réserves écrites par le code et éprouvées | **appliqué tel quel** (« Code neuf ») |",
    "| **G-1** (majeur) — `" + GO58 + "` dans les décisions | **appliqué tel quel** pour le texte ajouté. **Écart déclaré** sur la déclaration de lecture : le rédacteur du brouillon 4 n'avait pas lu la ligne -58 ; sa déclaration reste telle quelle, et celle de ce brouillon 5 (lignes -56, -58 et -63, lues par leur numéro) est ajoutée à côté |",
    "| **G-2** (majeur) — plan, point 2 | **appliqué tel quel** ; ajout de cohérence, hors couple, déclaré : la clé `OUVERTURE-TEMPS1-ACC2` des « Lignes de registre » dit la même chose |",
    "| **G-3** (majeur) — réserve « validité de l'adaptateur non jugée à l'ouverture du temps 1 » | **appliqué tel quel** (ligne neuve après la réserve « non répliquée ») |",
    "| **G-4, G-5** (majeurs), **G-6** (mineur) | portent sur l'ordre exploratoire (brouillon 5, section 12) et sur le devis (brouillon 4, section 13) : appliqués tels quels |",
    "| **m-1** (mineur) — nœud 3 visible du validateur | **appliqué**, branche « tant qu'il ne l'est pas » : `**[NŒUD 3 — OUVERT]**` devient " + M_N3 + " aux deux endroits (statut, décisions), ajouté à la table des marqueurs avec les deux manières de le remplir ; aucune pente |",
    "| **m-2** (mineur) — réserve « non répliquée » après une réplication lue | **appliqué tel quel** |",
    "| **m-3** (mineur) — dépôt daté chez un tiers | **appliqué tel quel**, aux deux endroits (plan, point 2 ; « Lignes de registre ») |",
    "| **m-4** (mineur) — cette entrée | **appliqué** |",
    "| **m-5** — « à confirmer par la recette » (devis) | aucun couple : rien à faire |",
    "| **m-6** (mineur) — arithmétique de la réplication | **appliqué** : script `calculs-redaction-cycle-2-v4.py` et sa sortie (§ 10), scellés ; renvoi depuis « Suite des cycles » |",
    "| choix de Lazar `" + GO63 + "`, hors de la contre-lecture | porté : décisions ; plan, points 1 et 2 ; « Calcul et dépense ». La levée « famille générée pendant le temps 1 » n'est pas accordée : rien ne change à l'ordre des antériorités |",
    "| tenue | version, date, mandat, statut, déclarations de lecture, renvois à l'ordre exploratoire (brouillon 5) et au devis (brouillon 4), documents cités, cette entrée ; rien d'autre : le reste est égal au brouillon 4, à l'octet |",
    "",
    "- **Brouillon 5 : pas encore contre-lu.** Chaque changement est rattaché à un couple, à `" + GO58 + "` ou à `" + GO63 + "` dans `" + DIFFERENCES + "`, qui nomme aussi ce que le rédacteur a dû tirer de `" + GO63 + "` et qu'un vérificateur neuf, d'un autre modèle, doit juger.",
], "couple m-4", "entrée de la contre-lecture des brouillons 4 (brouillon relu, rapport, traitement couple par couple) ; état du brouillon 5")

# ====================================================================================================
# 2. Ordre exploratoire
# ====================================================================================================
O = Piece("ordre exploratoire du temps 1",
          DOSSIER + "ordre-exploratoire-temps-1-v1-brouillon4.md",
          "feb63aa9c1ba10dd63c984dc2d0b6acc4be4f8f62476fee5f6e5029e5ca66fc1",
          DOSSIER + "ordre-exploratoire-temps-1-v1-brouillon5.md")

O.sub("— v1 — brouillon 4", "— v1 — brouillon 5", "tenue", "version (titre)")
O.sub("brouillon 4 le 2026-11-18 après 21:13.", "brouillon 4 le 2026-11-18 après 21:13 ; brouillon 5 le 2026-11-18 après 21:52.", "tenue", "date")
O.sub("La confirmation est le texte `prereg/accumulation-cycle-2-v1-brouillon4.md`, lu une seule fois sur une famille neuve.",
      "La confirmation est le texte `prereg/accumulation-cycle-2-v1-brouillon5.md`, lu une seule fois sur une famille neuve.",
      "tenue", "renvoi au préenregistrement, brouillon 5")
O.sub("- **Statut** : **brouillon 4** = brouillon 3 (",
      "- **Statut** : **brouillon 5** = brouillon 4 (`ordre-exploratoire-temps-1-v1-brouillon4.md`, `" + O.empreinte + "`, gardé tel quel, R12) + les couples exacts de la contre-lecture des brouillons 4 qui portent sur cet ordre (`" + CL + "`, `" + CL_SHA + "` : M-2, G-4, G-5) + les choix de Lazar `" + GO58 + "` et `" + GO63 + "` (lignes de registre lues par leur numéro), portés par script (`pieces-redaction-cycle-2-v1/brouillons5-faire-v1.py`) ; table en section 12 ; pas encore contre-lu dans cet état. Le brouillon 4 était lui-même : brouillon 3 (",
      "tenue", "statut")
O.sub("table en section 11 ; pas encore contre-lu dans cet état. Le brouillon 3 était lui-même",
      "table en section 11 ; contre-lu depuis (section 12). Le brouillon 3 était lui-même",
      "tenue", "statut : le brouillon 4 a été contre-lu depuis")
O.sub("devis à part (`devis-cycle-2-v1-brouillon3.md`, section 6)", "devis à part (`devis-cycle-2-v1-brouillon4.md`, section 6)",
      "tenue", "section 4 : renvoi au devis, brouillon 4")

# --- M-2 ---
O.sub("Seul le mode est connu de l'analyste, parce que Lazar l'a fixé et que le préenregistrement l'écrit : « coût déclaré gonflé », rejoué à neuf (points à trancher, point 2, option (a)).",
      "Seuls sont connus de l'analyste le mode et le fait que la recette reprend celle du développement, parce que Lazar les a fixés et que le préenregistrement les écrit : « coût déclaré gonflé », rejoué à neuf (points à trancher, point 2, option (a)) ; le texte scellé de la recette, sa règle du tirage, son entropie et la liste restent fermés.",
      "couple M-2", "section 5, point 1 : connus, le mode et la reprise de la recette du développement ; le reste fermé")

# --- G-4 et G-5 : portage de GO-58 ---
O.sub("3. **les verdicts de la lecture des sondes (étape B) et de l'apprentissage des sondes sur la tâche (étape B bis) sont scellés**, ainsi que leur **table conjointe** si elle est prévue (`CONJOINTE-BBIS`) et le verdict de la validité de l'adaptateur — ou la session mère a écrit que la lecture concernée n'aura pas lieu : l'analyste recevrait les fichiers des deux étapes, il ne doit pouvoir peser sur aucun de ces verdicts ; il est exclu de tout rôle dans ces verdicts et dans cette table ; leurs textes scellés gardent leur statut ;",
      "3. **les verdicts de la lecture des sondes (étape B) et de l'apprentissage des sondes sur la tâche (étape B bis) sont scellés**, ainsi que leur **table conjointe** si elle est prévue (`CONJOINTE-BBIS`) — ou la session mère a écrit que la lecture concernée n'aura pas lieu : l'analyste recevrait les fichiers des deux étapes, il ne doit pouvoir peser sur aucun de ces verdicts ; il est exclu de tout rôle dans ces verdicts et dans cette table ; leurs textes scellés gardent leur statut. **Le verdict de la validité de l'adaptateur n'est pas une condition d'ouverture** (choix de Lazar, `" + GO58 + "`, R-3440) : la ligne `OUVERTURE-TEMPS1-ACC2` écrit s'il est scellé ; s'il ne l'est pas, la réserve « validité de l'adaptateur non jugée à l'ouverture du temps 1 » du préenregistrement s'applique ; l'analyste reste exclu de tout rôle dans ce verdict, et ni son rapport, ni ses sondes, ni ses autres sorties ne sont transmis à un lecteur ou à un juge de la validité de l'adaptateur avant que ce verdict soit scellé ; le lot E n'est ouvert que si ses lignes existent (lot E ci-dessus) ;",
      "GO-58 (couple G-4)", "section 2, condition d'ouverture 3 : le verdict de la validité de l'adaptateur n'est plus une condition")
O.sub("**Lot E — la validité de l'adaptateur**, si ses lignes existent au registre propre `registres/validite-adaptateur-v1.md` :",
      "**Lot E — la validité de l'adaptateur**, si ses lignes existent au registre propre `registres/validite-adaptateur-v1.md` — son verdict peut ne pas être scellé (choix de Lazar, `" + GO58 + "` ; condition d'ouverture 3) — :",
      "GO-58 (couple G-5)", "section 2, lot E : son verdict peut ne pas être scellé")
O.sub(", lecture et verdict : `<<EMPREINTES_LOT_VADAPT>>` (lignes `SCORES-RELECTURE-VADAPT`, `SORTIES-HD-VADAPT`, `LECTURE-VADAPT`).",
      ", lecture et, s'il est scellé, verdict : `<<EMPREINTES_LOT_VADAPT>>` (lignes `SCORES-RELECTURE-VADAPT`, `SORTIES-HD-VADAPT`, `LECTURE-VADAPT`, et la ligne du verdict si elle existe) ; seules s'ouvrent les lignes dont la session mère a recopié l'empreinte (en-tête de cette section ; condition 4) ; une ligne absente laisse sa part du lot fermée, et la session mère écrit « lot E fermé » si aucune n'existe.",
      "GO-58 (couple G-5)", "section 2, lot E : seules s'ouvrent les lignes recopiées ; « lot E fermé » si aucune")
O.sub("condition d'ouverture 3 confirmée telle qu'écrite (les deux verdicts, leur table conjointe si elle est prévue, le verdict de la validité de l'adaptateur) : la ligne « laissé à confirmer » de la section 9 est close par ce choix",
      "condition d'ouverture 3 confirmée pour les deux verdicts et leur table conjointe si elle est prévue ; **le verdict de la validité de l'adaptateur en est retiré** par un choix ultérieur de Lazar (`" + GO58 + "`, R-3440 : réserve écrite au préenregistrement et ici ; lot E ouvert seulement si ses lignes existent) : la ligne « laissé à confirmer » de la section 9 est close par ces deux choix",
      "GO-58 (couple G-5)", "section 11, ligne du point 14 : la condition d'ouverture 3 après le choix ultérieur")
O.sub("| tenue | version, date, statut, renvois au préenregistrement (brouillon 4) et au devis (brouillon 3), cette section ; rien d'autre : le reste est égal au brouillon 3, à l'octet |",
      "| tenue (du brouillon 4) | version, date, statut, renvois au préenregistrement (brouillon 4) et au devis (brouillon 3), cette section ; rien d'autre : le reste était égal au brouillon 3, à l'octet |",
      "tenue", "section 11 : sa ligne de tenue dit qu'elle valait pour le brouillon 4")

# --- GO-63, levée 2 : relecture complémentaire avant l'ouverture ---
O.sub("une fois sa ligne de dépense inscrite : activations des épisodes des lots A et E relus à état imposé ; empreintes à sa ligne de registre.",
      "une fois sa ligne de dépense inscrite : activations des épisodes des lots A et E relus à état imposé ; empreintes à sa ligne de registre. **Jouée avant l'ouverture du temps 1** (choix de Lazar, `" + GO63 + "`, levée 2) : par un opérateur écarté des verdicts de l'étape B et de l'étape B bis (ni lecteur ni juge de ces verdicts ni de leur table conjointe), qui n'est pas l'analyste, et que la session mère nomme à la ligne de registre de la relecture ; elle ne lit que des données de développement (lots A et E ; pour le lot E, les seules lignes dont la session mère a recopié l'empreinte au lancement de la relecture), **aucune donnée de la famille neuve** ; ses sorties sont scellées et restent fermées jusqu'à la ligne `OUVERTURE-TEMPS1-ACC2`, qui recopie leurs empreintes ; **elle est rejouée si le verdict de l'étape B bis l'exige**, sous la même ligne de dépense et son plafond (devis, section 6). Tiré par le rédacteur, à contre-lire : aucune sonde n'est apprise sur ces activations avant `OUVERTURE-TEMPS1-ACC2` — concevoir une sonde est le travail de l'analyste (section 3), qui ne commence qu'à cette ligne.",
      "GO-63 (levée 2)", "section 2, lot F : relecture jouée avant l'ouverture, par un opérateur écarté des verdicts des étapes B et B bis, sans donnée de la famille, rejouée si le verdict de l'étape B bis l'exige")
O.sub("instance lancée et détruite par la session mère par identifiant (R10). Sans ce GO,",
      "instance lancée et détruite par la session mère par identifiant (R10). **Calendrier** (choix de Lazar, `" + GO63 + "`, levée 2) : la relecture est jouée avant `OUVERTURE-TEMPS1-ACC2` (lot F, section 2) ; l'apprentissage des sondes sur ces activations ne commence qu'après cette ligne, dans les 48 heures du temps 1 (section 8, point 2) ; entre les deux, l'instance est arrêtée et gardée (devis, section 6). Sans ce GO,",
      "GO-63 (levée 2)", "section 4 : calendrier de la relecture complémentaire")

# --- GO-63, levée 3 : temps 1 borné à 48 heures ---
O.sub("2. **Limite de temps** : sept jours après `OUVERTURE-TEMPS1-ACC2` (elle porte sur le travail de l'analyste ;",
      "2. **Limite de temps** : **48 heures comptées depuis `OUVERTURE-TEMPS1-ACC2`** (choix de Lazar, `" + GO63 + "`, levée 3 : elle remplace la limite de sept jours des brouillons précédents ; la relecture complémentaire, jouée avant l'ouverture, n'entre pas dans ce compte ; à cette limite sans principale, la règle « à une limite, sans principale » ci-dessous s'applique) (elle porte sur le travail de l'analyste ;",
      "GO-63 (levée 3)", "section 8, point 2 : 48 heures comptées depuis l'ouverture, au lieu de sept jours")

O.fin([
    "## 12. Couples de la contre-lecture des brouillons 4 et choix de Lazar portés dans ce brouillon 5",
    "",
    "Rapport : `" + CL + "`, `" + CL_SHA + "` (agent neuf, Claude Opus 5.5 ; brouillon relu : `ordre-exploratoire-temps-1-v1-brouillon4.md`, `" + O.empreinte + "`) ; verdict : « scellable après le nœud 3 et ces couples exacts ». Choix de Lazar : registre des accords, lignes `" + GO58 + "` (R-3440) et `" + GO63 + "` (R-3459), lues par leur numéro. Détail, changement par changement : `differences-brouillons-4-vers-5-v1.md` (même dossier).",
    "",
    "| couple ou choix | traitement dans ce brouillon 5 |",
    "|---|---|",
    "| **M-2** (majeur) — ce que l'analyste connaît de la recette | **appliqué tel quel** (section 5, point 1) |",
    "| **G-4** (majeur) — `" + GO58 + "` : condition d'ouverture 3 | **appliqué tel quel** (section 2, condition 3) : le verdict de la validité de l'adaptateur n'est plus une condition d'ouverture ; la ligne `OUVERTURE-TEMPS1-ACC2` écrit s'il est scellé ; l'analyste reste exclu de ce verdict et ses sorties ne vont à aucun lecteur ni juge de la validité de l'adaptateur avant qu'il soit scellé |",
    "| **G-5** (majeur) — `" + GO58 + "` : lot E ; section 11 | **appliqué tel quel**, aux trois endroits (section 2, lot E, deux sous-chaînes ; section 11, ligne du point 14) ; cette ligne-ci est celle que le couple demande pour `" + GO58 + "` : section 2, condition 3 et lot E |",
    "| `" + GO63 + "`, **levée 2** — relecture complémentaire jouée avant l'ouverture du temps 1, par un opérateur écarté des verdicts de l'étape B et de l'étape B bis, sans aucune donnée de la famille ; rejouée si le verdict de l'étape B bis l'exige | section 2, lot F ; section 4. **Tiré par le rédacteur, à contre-lire** : aucune sonde n'est apprise avant l'ouverture ; les sorties de la relecture restent fermées jusqu'à la ligne d'ouverture ; l'opérateur n'est pas l'analyste |",
    "| `" + GO63 + "`, **levée 3** — temps 1 borné à 48 heures comptées depuis son ouverture | section 8, point 2 : la limite de sept jours est remplacée. **Non dit par le choix, signalé** : si un rejeu de la relecture exigé par le verdict de l'étape B bis n'est pas fini à l'ouverture, ni le choix ni cet ordre ne disent que le compte attend |",
    "| `" + GO63 + "`, **levée 1** — sélection des tâches fraîches non bloquante | aucun changement dans cet ordre : elle porte sur le devis (section 7) et sur le préenregistrement (« Calcul et dépense ») ; la condition 2 de la section 2 (recette scellée ; liste par `TACHES-ACC2`, avant `SONDES-ACC2`) reste telle quelle |",
    "| `" + GO63 + "`, levée « famille générée pendant le temps 1 » — **non accordée** | aucun changement : les données de la famille n'existent pas pendant le temps 1 (section 5, point 1) |",
    "| **B-1, M-1, M-3, G-1 à G-3, G-6, m-1 à m-6** | portent sur le préenregistrement (brouillon 5) ou sur le devis (brouillon 4) |",
    "| **nœud 3 — ouvert** ; **règle de réplication — à Lazar** | aucun : cet ordre ne dépend ni de l'un ni de l'autre |",
    "| tenue | version, date, statut, renvois au préenregistrement (brouillon 5) et au devis (brouillon 4), ligne de tenue de la section 11 datée, cette section ; rien d'autre : le reste est égal au brouillon 4, à l'octet |",
], "tenue ; GO-58 (couple G-5)", "section 12 : table des couples et des choix portés, dont la ligne demandée pour GO-58")

# ====================================================================================================
# 3. Devis
# ====================================================================================================
V = Piece("devis du second cycle",
          DOSSIER + "devis-cycle-2-v1-brouillon3.md",
          "e8c83fc14c4aed24a49603fa75db7343c08290b2ec5ca6be35560b36d565f734",
          DOSSIER + "devis-cycle-2-v1-brouillon4.md")

V.sub("— v1 — brouillon 3", "— v1 — brouillon 4", "tenue", "version (titre)")
V.sub("brouillon 3 le 2026-11-18 après 21:13.", "brouillon 3 le 2026-11-18 après 21:13 ; brouillon 4 le 2026-11-18 après 21:52.", "tenue", "date")
V.sub("- **Statut** : **brouillon 3** = brouillon 2 (",
      "- **Statut** : **brouillon 4** = brouillon 3 (`devis-cycle-2-v1-brouillon3.md`, `" + V.empreinte + "`, gardé tel quel, R12) + le couple G-6 de la contre-lecture des brouillons 4 (`" + CL + "`, `" + CL_SHA + "`) + les choix de Lazar `" + GO58 + "` et `" + GO63 + "` (lignes de registre lues par leur numéro), portés par script (`pieces-redaction-cycle-2-v1/brouillons5-faire-v1.py`) ; **aucun chiffre n'est recalculé** ; table en section 13 ; pas encore contre-lu dans cet état. Le brouillon 3 était lui-même : brouillon 2 (",
      "tenue", "statut")
V.sub("table en section 12 ; pas encore contre-lu dans cet état. Le brouillon 2 était lui-même",
      "table en section 12 ; contre-lu depuis (section 13). Le brouillon 2 était lui-même",
      "tenue", "statut : le brouillon 3 a été contre-lu depuis")
V.sub("Texte servi : `prereg/accumulation-cycle-2-v1-brouillon4.md`.",
      "Texte servi : `prereg/accumulation-cycle-2-v1-brouillon5.md`.",
      "tenue", "renvoi au préenregistrement, brouillon 5")

# --- G-6 ---
V.sub("**Ces 1 024 passes n'existent que si la pièce du témoin distillé de la validité de l'adaptateur a été créée**",
      "**Ces 1 024 passes n'existent que si la pièce du témoin distillé de la validité de l'adaptateur a été créée et que ses lignes sont ouvertes au temps 1** (lot E de l'ordre exploratoire ; son verdict peut ne pas être scellé : `" + GO58 + "`)",
      "GO-58 (couple G-6)", "section 6 : les 1 024 passes dépendent aussi de l'ouverture du lot de la validité de l'adaptateur")

# --- GO-63, levées 2 et 3 : calendrier de la relecture complémentaire ---
V.apres("Sans cette ligne, le temps 1 ne peut pas concevoir de sonde neuve", [
    "",
    "**Calendrier de la pièce : choix de Lazar** (`" + GO63 + "`, levées 2 et 3) — la relecture est jouée **avant** l'ouverture du temps 1, par un opérateur écarté des verdicts de l'étape B et de l'étape B bis, sans aucune donnée de la famille ; elle est rejouée si le verdict de l'étape B bis l'exige ; le temps 1 est borné à 48 heures comptées depuis son ouverture. **Aucun chiffre de cette section n'est recalculé** ; ce que ces choix changent à leur lecture :",
    "- **l'apprentissage exploratoire sur la carte** (une à six heures, ci-dessus) vient après l'ouverture, dans les 48 heures du temps 1 ; entre la relecture et l'ouverture, l'instance est arrêtée et gardée, au prix de garde ci-dessus (1,92 USD par jour) : **la garde commence donc avant l'ouverture**, pour une durée que ce devis ne borne pas (elle dépend de la date des verdicts de l'étape B et de l'étape B bis) ; les sept jours de garde que couvre le plafond se comptent depuis la fin de la relecture ; au-delà : nœud ;",
    "- **le rejeu, si le verdict de l'étape B bis l'exige**, est une relance entière au sens de cette section (≈ 59 USD au pire cas, relecture d'origine comprise) : elle tient sous le plafond de 75 USD avec sept jours de garde (branche (β), ci-dessus) ; « aucun surcoût » ne vaut que sans rejeu ; un second rejeu, ou un rejeu qui s'ajoute à une relance après une panne, sort du plafond : nœud ;",
    "- **pour les 1 024 passes du témoin distillé**, « ouvertes au temps 1 » se lit désormais : lignes du lot E dont la session mère a recopié l'empreinte **au lancement de la relecture** (ordre exploratoire, section 2, lots E et F) ;",
    "- **coût en garde, déclaré** (contre-lecture de la note du chemin critique, `" + CHEMIN_CL_SHA + "`) : le contenu de la relecture (séries, couches, séries du témoin distillé) est fixé à son lancement, avant les verdicts qui pourraient le changer.",
], "GO-63 (levées 2 et 3)", "section 6 : relecture avant l'ouverture ; garde avant l'ouverture ; rejeu sous le même plafond ; aucun chiffre recalculé")
V.sub("et y apprendre des sondes contre le témoin ; seulement après `OUVERTURE-TEMPS1-ACC2` ; arrêt et destruction par identifiant",
      "et y apprendre des sondes contre le témoin ; **la relecture avant `OUVERTURE-TEMPS1-ACC2`** (choix de Lazar, `" + GO63 + "`, levée 2), par un opérateur écarté des verdicts de l'étape B et de l'étape B bis, sans aucune donnée de la famille, sorties scellées fermées jusqu'à l'ouverture ; l'apprentissage des sondes après l'ouverture seulement ; rejeu de la relecture si le verdict de l'étape B bis l'exige, sous ce même plafond ; arrêt et destruction par identifiant",
      "GO-63 (levée 2)", "section 10 : condition de départ de la ligne proposée pour la relecture complémentaire")

# --- GO-63, levée 1 : sélection des tâches fraîches non bloquante ---
V.sub("un devis de l'extraction suit, puis sa ligne de dépense ; le tirage attend cette ligne.",
      "un devis de l'extraction suit, puis sa ligne de dépense ; **l'extraction** attend cette ligne ; **la sélection complémentaire** (le tirage par la règle de sélection : aucun appel de modèle, 0 USD de carte) **ne l'attend plus** (choix de Lazar, `" + GO63 + "`, levée 1, dont la ligne écrit : « la relecture de sélection des tâches fraîches n'est plus une étape bloquante (prudence, 0 USD) ») : elle part dès que la règle du tirage complémentaire est scellée et contre-lue et que son entropie est fixée (préenregistrement, plan, point 3, inchangé).",
      "GO-63 (levée 1)", "section 7 : la sélection n'attend plus le devis ni la ligne de dépense de l'extraction ; l'extraction les attend toujours")

V.fin([
    "## 13. Couple de la contre-lecture des brouillons 4 et choix de Lazar portés dans ce brouillon 4",
    "",
    "Rapport : `" + CL + "`, `" + CL_SHA + "` (agent neuf, Claude Opus 5.5 ; devis relu : brouillon 3, `" + V.empreinte + "`). Choix de Lazar : registre des accords, lignes `" + GO58 + "` (R-3440) et `" + GO63 + "` (R-3459), lues par leur numéro. Détail, changement par changement : `differences-brouillons-4-vers-5-v1.md` (même dossier). **Aucun chiffre de ce devis n'est recalculé ; aucun plafond ne change.**",
    "",
    "| couple ou choix | ce qu'il change dans ce devis |",
    "|---|---|",
    "| **G-6** (mineur) — `" + GO58 + "` : les 1 024 passes du témoin distillé | **appliqué tel quel** (section 6) |",
    "| **m-5** — « à confirmer par la recette » (section 8) | jugé juste par le contre-lecteur ; aucun couple, aucun changement |",
    "| `" + GO63 + "`, **levée 1** — sélection des tâches fraîches non bloquante | section 7 : la sélection complémentaire (0 USD de carte, aucun appel de modèle) n'attend plus le devis ni la ligne de dépense de l'extraction ; l'extraction les attend toujours. **Lecture du rédacteur, à confirmer** : la ligne du registre écrit « relecture de sélection » ; elle est lue ici comme le tirage par la règle de sélection ; la règle du tirage complémentaire reste scellée et contre-lue avant le tirage |",
    "| `" + GO63 + "`, **levée 2** — relecture complémentaire jouée avant l'ouverture du temps 1 ; rejouée si le verdict de l'étape B bis l'exige | section 6 (calendrier ; garde avant l'ouverture ; rejeu sous le plafond de 75 USD) ; section 10 (condition de départ de la ligne proposée). **Tiré par le rédacteur, à contre-lire** : l'apprentissage sur la carte vient après l'ouverture ; le rejeu est compté comme la relance entière déjà chiffrée |",
    "| `" + GO63 + "`, **levée 3** — temps 1 borné à 48 heures comptées depuis son ouverture | section 6 : l'apprentissage sur la carte tient dans ces 48 heures ; les sept jours de garde du plafond ne sont pas recomptés |",
    "| `" + GO63 + "`, levée « famille générée pendant le temps 1 » — **non accordée** | aucun changement : la famille reste créée après `SCELLEMENT-ACC2` (section 10, ligne proposée pour la famille neuve) ; l'effectif n'est pas à générer au plafond avant la simulation |",
    "| **nœud 3 — ouvert** ; **règle de réplication — à Lazar** | aucun changement : ni l'un ni l'autre ne touche un chiffre de ce devis |",
    "| tenue | version, date, statut, renvoi au préenregistrement (brouillon 5), cette section ; rien d'autre : le reste est égal au brouillon 3, à l'octet |",
], "tenue", "section 13 : table du couple et des choix portés")

# ====================================================================================================
# 4. Écriture, puis note des différences
# ====================================================================================================
assert not Path(DIFFERENCES).exists(), "la note des différences existe déjà : on n'écrase jamais (R12)"
for piece in (P, O, V):
    piece.ecrire()

note = [
    "# Différences des brouillons 4 aux brouillons 5 — second cycle de la lecture « accumuler les scores de sondes sur l'épisode » — v1",
    "",
    "- **Auteur** : rédacteur du second cycle, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Fable 5.2 (`claude-fable-5-2`) ; exclu de toute contre-lecture, lecture ou jugement de ce cycle. **Date (UTC)** : 2026-11-18, après 21:52.",
    "- **Ce que c'est** : la liste de tout ce qui change entre les textes en vigueur et leurs versions neuves, chaque changement rattaché à un couple de la contre-lecture des brouillons 4, au choix de Lazar `" + GO58 + "` ou au choix de Lazar `" + GO63 + "`, ou à la tenue. Produite par le script qui fabrique les textes (`" + SCRIPT + "`, empreinte dans son compagnon) : ce qui n'est pas listé ici est égal à la source, à l'octet. La sortie de la comparaison ligne à ligne est réduite à son décompte.",
    "- **Sources** : contre-lecture des brouillons 4, `" + CL + "`, `" + CL_SHA + "`, lue en entier ; registre des accords, les seules lignes `GO-2026-11-18-56` (point 2), `" + GO58 + "` et `" + GO63 + "`, lues par leur numéro ; pour le sens des levées de `" + GO63 + "`, la note `" + CHEMIN + "` (`" + CHEMIN_SHA + "`) et sa contre-lecture (`" + CHEMIN_CL_SHA + "`), aux seuls passages sur les levées (lecture hors de la liste du mandat, déclarée).",
    "- **Deux décisions restent à Lazar, portées par des marqueurs de gabarit que le validateur refuse** : la règle de réplication, " + M_REPL + " (couple B-1 : ce qui compte comme une issue positive et comme une issue répliquée) ; le nœud 3, " + M_N3 + " (couple m-1 : formulation A ou C du contraste à témoin apparié de la porte de fin de phase 1, hors de ces textes). Aucun des trois textes ne penche : le rédacteur n'a écrit ni règle ni préférence ; la recommandation du contre-lecteur sur B-1 reste dans son rapport ; le brouillon de décision `docs/decisions/decision-N-074-v1-brouillon2.md` n'est pas touché.",
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
    "**Le devis change** (brouillon 4) : le couple G-6 et les levées 1 et 2 de `" + GO63 + "` touchent ses sections 6, 7 et 10 ; **aucun de ses chiffres n'est recalculé, aucun plafond ne change**. **Pièce ajoutée** : `" + PIECES + "calculs-redaction-cycle-2-v4.py` et sa sortie (couple m-6 : arithmétique de la règle de réplication, § 10 ; des formules, aucune donnée). **Les points à trancher (brouillon 3) et le brouillon de décision sur la porte de fin de phase 1 ne changent pas.**",
]
for k, piece in enumerate((P, O, V), start=2):
    note += ["", f"## {k}. Changements — {piece.nom}", "", "| n° | rattachement | changement |", "|---|---|---|"]
    for i, (r, m) in enumerate(piece.journal, start=1):
        note.append(f"| {i} | {r} | {m} |")
note += [
    "",
    "## 5. Couples de la contre-lecture des brouillons 4 : appliqué ou non",
    "",
    "| couple | état | où |",
    "|---|---|---|",
    "| **B-1** (bloquant) | appliqué tel quel ; la règle elle-même reste à Lazar (" + M_REPL + ") | préenregistrement, « Suite des cycles » (deux sous-chaînes) ; table des marqueurs |",
    "| **M-1** | appliqué tel quel (deux sous-chaînes) | préenregistrement, « Deux passages » ; réserve « adaptateur particulier » |",
    "| **M-2** | appliqué tel quel (trois sous-chaînes) | préenregistrement, « Métrique » et « Liste d'arrêt » ; ordre exploratoire, section 5, point 1 |",
    "| **M-3** | appliqué tel quel | préenregistrement, « Code neuf » |",
    "| **G-1** | texte ajouté appliqué tel quel ; **écart déclaré** sur la déclaration de lecture : celle du brouillon 4 n'est pas réécrite, celle du brouillon 5 (lignes -56, -58, -63) est ajoutée | préenregistrement, « Décisions qui fondent ce texte » |",
    "| **G-2** | appliqué tel quel ; un ajout de cohérence hors couple, déclaré (clé `OUVERTURE-TEMPS1-ACC2` des « Lignes de registre ») | préenregistrement, plan, point 2 |",
    "| **G-3** | appliqué tel quel | préenregistrement, « Critères de lecture gelés », réserves |",
    "| **G-4** | appliqué tel quel | ordre exploratoire, section 2, condition 3 |",
    "| **G-5** | appliqué tel quel (trois sous-chaînes) ; la ligne demandée pour `" + GO58 + "` est dans la table de la section 12 | ordre exploratoire, section 2, lot E ; section 11 ; section 12 |",
    "| **G-6** | appliqué tel quel | devis, section 6 |",
    "| **m-1** | appliqué, branche « tant qu'il ne l'est pas » : marqueur " + M_N3 + ", deux occurrences et une ligne de la table des marqueurs | préenregistrement, statut, décisions, table des marqueurs |",
    "| **m-2** | appliqué tel quel | préenregistrement, réserve « non répliquée » |",
    "| **m-3** | appliqué tel quel (deux sous-chaînes) | préenregistrement, plan, point 2 ; « Lignes de registre » |",
    "| **m-4** | appliqué : entrée « Contre-lecture 3 », avec l'empreinte du brouillon relu et celle du rapport | préenregistrement, « Contre-lecture » |",
    "| **m-5** | aucun couple : rien à faire | — |",
    "| **m-6** | appliqué : script et sortie de calcul version 4, § 10 ; renvoi depuis « Suite des cycles » | pièces de rédaction ; préenregistrement |",
    "",
    "## 6. Choix de Lazar `" + GO63 + "` : ce qui est porté, et ce que le rédacteur a dû en tirer",
    "",
    "Aucune des lignes ci-dessous n'ajoute un seuil, un niveau ni un critère d'analyse. Les points marqués « tiré par le rédacteur » ne sont pas dits par la ligne du registre : ils sont écrits pour être contredits par la vérification.",
    "",
    "1. **Levée 1 — sélection des tâches fraîches non bloquante.** Devis, section 7 ; préenregistrement, « Calcul et dépense ». La ligne du registre écrit « la relecture de sélection des tâches fraîches n'est plus une étape bloquante (prudence, 0 USD) ». **Lecture du rédacteur, à confirmer par la session mère** : il s'agit du tirage de sélection complémentaire (aucun appel de modèle, 0 USD), qui n'attend plus le devis ni la ligne de dépense de l'extraction ; l'extraction, elle, les attend toujours. Les textes gardent la garde la plus stricte : la règle du tirage complémentaire reste scellée et contre-lue avant tout tirage, et son entropie fixée avant lui (préenregistrement, plan, point 3, inchangé). Si la levée visait autre chose, ces textes sont plus prudents qu'elle, non plus lâches.",
    "2. **Levée 2 — relecture complémentaire jouée avant l'ouverture du temps 1.** Ordre exploratoire, section 2 (lot F) et section 4 ; devis, sections 6 et 10 ; préenregistrement, « Calcul et dépense ». Porté tel que dit : avant l'ouverture ; opérateur écarté des verdicts de l'étape B et de l'étape B bis ; aucune donnée de la famille ; rejouée si le verdict de l'étape B bis l'exige. **Tiré par le rédacteur** : (a) l'opérateur n'est pas l'analyste et la session mère le nomme à la ligne de registre de la relecture ; (b) les sorties de la relecture sont scellées et restent fermées jusqu'à la ligne d'ouverture, qui recopie leurs empreintes ; (c) aucune sonde n'est apprise avant l'ouverture : l'apprentissage exploratoire sur la carte, que le devis comptait dans la même pièce, vient après l'ouverture, l'instance étant arrêtée et gardée entre-temps ; (d) le rejeu est compté comme la relance entière déjà chiffrée, sous le même plafond de 75 USD ; un second rejeu, ou une garde de plus de sept jours, est un nœud ; (e) pour le lot de la validité de l'adaptateur, ce qui est relu est ce dont la session mère a recopié l'empreinte au lancement de la relecture.",
    "3. **Levée 3 — temps 1 borné à 48 heures comptées depuis son ouverture.** Ordre exploratoire, section 8, point 2 (la limite de sept jours est remplacée) ; préenregistrement, plan, point 1. La relecture, jouée avant l'ouverture, n'entre pas dans ce compte. Les sept jours de garde que chiffre le devis ne sont pas recomptés.",
    "4. **Levée « famille générée pendant le temps 1 » — non accordée.** Préenregistrement, plan, point 2 : la phrase « la famille n'existe pas avant `SCELLEMENT-ACC2` » reste, avec la mention du choix ; rien d'autre ne change.",
    "",
    "## 7. Autres points que la vérification doit juger",
    "",
    "1. **Phrase laissée telle quelle dans « Suite des cycles »** : « une issue “accumuler, propre” de ce cycle est rapportée avec son compte de cycles, cette borne non corrigée et la réserve “non répliquée” ». Le couple B-1 ne la touche pas ; après le couple m-2, la réserve s'écrit « à côté de toute issue positive au sens de la règle de réplication ». Si Lazar retient que « propre, sans gain d'accumulation établi » est aussi une issue positive, cette phrase est à aligner quand le marqueur est rempli ; le rédacteur ne l'a pas fait, pour ne pas pencher.",
    "2. **Ajout hors couple, déclaré** : la clé `OUVERTURE-TEMPS1-ACC2` des « Lignes de registre » du préenregistrement dit ce que la ligne écrit (cohérence avec G-2 et avec M-3, qui fait écrire la réserve par le code à partir de cette ligne).",
    "3. **Ligne de tenue de la section 11 de l'ordre exploratoire** : précisée « (du brouillon 4) », parce que la section 11 reçoit par ailleurs le couple G-5 et qu'elle n'est plus égale à sa forme du brouillon 4.",
    "4. **Pièces scellées que ces choix rendent caduques et qu'on ne réécrit pas** (R12) : note des différences des brouillons 3 aux brouillons 4, § 7, points 5 et 7 ; points à trancher, brouillon 3, point 14 et section C ; ligne « laissé à confirmer » de l'ordre exploratoire, section 9 (close par sa section 11) ; devis, section 9, renvoi au calendrier des points à trancher, section C, que `" + GO63 + "` modifie.",
    "",
    "## 8. Ce qui reste ouvert ou attend un fait à venir",
    "",
    "1. **Règle de réplication** (" + M_REPL + ") : à Lazar ; rien ne peut en être écrit ni changé après `LECTURE-ACC2`, et le texte ne se scelle pas sans elle.",
    "2. **Nœud 3** (" + M_N3 + ") : formulation A ou C, ou le mot de Lazar que le préenregistrement se scelle sans lui.",
    "3. **Repli « sans second témoin »** (couple M-1) : ne vaut que sur mot de Lazar.",
    "4. **Non dit par `" + GO63 + "`, signalé** : si un rejeu de la relecture complémentaire exigé par le verdict de l'étape B bis n'est pas fini à l'ouverture du temps 1, le compte des 48 heures attend-il ? Les textes ne prévoient aucune suspension.",
    "5. **Faits à venir et textes à écrire** (inchangés) : l'offre de disque d'au moins 250 gigaoctets au prix du stockage ; la règle du tirage complémentaire et la procédure d'extraction portée à cette échelle ; le relevé des compteurs du premier tirage, puis le devis de l'extraction et sa ligne ; le devis et la ligne du bras d'attaque ; la ligne de dépense de la relecture complémentaire, dont la condition de départ change (devis, section 10).",
    "6. **Marqueurs du préenregistrement** : seize — les quatorze des brouillons précédents, " + M_REPL + " et " + M_N3 + " ; ceux de l'ordre exploratoire, section 2, inchangés.",
    "7. **Vérification des brouillons 5** par un agent neuf d'un autre modèle que le rédacteur (R2) : pas encore faite.",
    "",
]
Path(DIFFERENCES).write_text("\n".join(note), encoding="utf-8")
print(DIFFERENCES + " : écrite")
