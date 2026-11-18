"""Fabrique les brouillons 3 du préenregistrement, de l'ordre exploratoire et des points à trancher du second
cycle, à partir de leurs brouillons 2 scellés — v1.

Applique les couples exacts de la vérification des brouillons 2
(`prereg/contre-lectures/accumulation-cycle-2-v1-brouillon2-verif1.md`) : P-1 à P-6, O-1, O-2, T-1 à T-4,
et la remarque D-1 (citation de la sortie de calcul v3). Chaque changement est une sous-chaîne ou une ligne
remplacée, ou une insertion, avec contrôle d'unicité ; ce qui n'est pas nommé ici reste égal au brouillon 2,
à l'octet. Chaque changement porte une catégorie : « couple » (demandé par le vérificateur), « tenue »
(version, date, statut, renvois, entrée de contre-lecture), « alignement » (mention que l'application d'un
couple ou la vérification elle-même a rendue fausse). Aucune donnée lue.
Lancement, depuis la racine du dépôt : python3 <ce fichier>
"""
import hashlib
from collections import Counter
from pathlib import Path

DOSSIER = "docs/notes/reconception-accumulation-cycle-2-v1/"
RAPPORT = "624939fb4e39bd8ac889a544a43199c55b48e3b7fd49a587763f17201726cc0e"
CHEMIN_RAPPORT = "prereg/contre-lectures/accumulation-cycle-2-v1-brouillon2-verif1.md"
SCRIPT = DOSSIER + "pieces-redaction-cycle-2-v1/brouillons3-faire-v1.py"


class Piece:
    def __init__(self, source, empreinte, cible):
        octets = Path(source).read_bytes()
        assert hashlib.sha256(octets).hexdigest() == empreinte, f"{source} n'est pas le brouillon 2 vérifié"
        self.source, self.empreinte, self.cible = source, empreinte, cible
        self.lignes = octets.decode("utf-8").split("\n")
        self.journal = []

    def indice(self, prefixe):
        trouves = [i for i, l in enumerate(self.lignes) if l.startswith(prefixe)]
        assert len(trouves) == 1, (self.source, prefixe, len(trouves))
        return trouves[0]

    def ligne(self, prefixe, nouvelle, categorie, motif):
        self.lignes[self.indice(prefixe)] = nouvelle
        self.journal.append((categorie, motif))

    def apres(self, prefixe, nouvelles, categorie, motif):
        i = self.indice(prefixe)
        self.lignes[i + 1:i + 1] = nouvelles
        self.journal.append((categorie, motif))

    def sub(self, avant, apres_, categorie, motif):
        """Remplace une sous-chaîne qui doit figurer une fois et une seule dans toute la pièce."""
        n = sum(l.count(avant) for l in self.lignes)
        assert n == 1, (self.source, avant[:60], n)
        self.lignes = [l.replace(avant, apres_) for l in self.lignes]
        self.journal.append((categorie, motif))

    def fin(self, nouvelles, categorie, motif):
        while self.lignes and self.lignes[-1] == "":
            self.lignes.pop()
        self.lignes += [""] + nouvelles + [""]
        self.journal.append((categorie, motif))

    def ecrire(self):
        Path(self.cible).write_text("\n".join(self.lignes), encoding="utf-8")
        compte = Counter(c for c, _ in self.journal)
        print(f"{self.cible} : {len(self.journal)} changements (" + ", ".join(f"{k} {v}" for k, v in sorted(compte.items())) + ")")
        for c, m in self.journal:
            print(f"   - {c} | {m}")


# ====================================================================================================
# 1. Préenregistrement
# ====================================================================================================
P = Piece("prereg/accumulation-cycle-2-v1-brouillon2.md",
          "bc68ba33edece126c7d4b43dede5c6fda31fdb3d4885ef58b9cacb2ab8f48d65",
          "prereg/accumulation-cycle-2-v1-brouillon3.md")

# --- tenue ---
P.sub("— v1 — brouillon 2", "— v1 — brouillon 3", "tenue", "version (titre)")
P.sub("brouillon 2 écrit le 2026-11-18 à partir de 19:05 (heures relevées par `date -u`).",
      "brouillon 2 écrit le 2026-11-18 à partir de 19:05 ; brouillon 3 écrit le 2026-11-18 à partir de 19:36 (heures relevées par `date -u`).",
      "tenue", "date")
P.sub("reçue de la session mère le 2026-11-18 vers 19:00 UTC.",
      "reçue de la session mère le 2026-11-18 vers 19:00 UTC ; puis par la dernière passe — appliquer les couples exacts de la vérification des brouillons 2 —, reçue vers 19:35 UTC.",
      "tenue", "mandat")
P.ligne("- **Statut**",
        "- **Statut** : **brouillon 3, scellé comme brouillon** = brouillon 2 (`prereg/accumulation-cycle-2-v1-brouillon2.md`, `" + P.empreinte + "`, gardé tel quel, R12 ; lui-même = brouillon 1, `d24913f68a103ff826b53d8e3823a4cb2513c0fc05638aa271eb2d174515aefb`, + les corrections de la contre-lecture 1) + les six couples exacts P-1 à P-6 de la vérification des brouillons 2 (section « Contre-lecture », contre-lecture 2), appliqués par script (`" + SCRIPT + "`, empreinte dans son compagnon), et rien d'autre que la tenue déclarée (version, date, mandat, statut, renvois aux brouillons 3, rapport cité, entrée de contre-lecture). **Non scellable en l'état** : il porte des marqueurs (table en fin de texte) que remplissent la session mère (recette, liste des tâches, lignes de registre), l'analyste du temps 1 (sonde gelée, épreuve plantée, effectif) et le développeur (code). Chemin visé au scellement : `prereg/accumulation-cycle-2-v1.md`.",
        "tenue", "statut")
P.sub("`docs/notes/reconception-accumulation-cycle-2-v1/ordre-exploratoire-temps-1-v1-brouillon2.md` ; devis,",
      "`docs/notes/reconception-accumulation-cycle-2-v1/ordre-exploratoire-temps-1-v1-brouillon3.md` ; devis,",
      "tenue", "renvoi à l'ordre exploratoire, brouillon 3")
P.sub("points à trancher, `docs/notes/reconception-accumulation-cycle-2-v1/points-a-trancher-cycle-2-v1-brouillon2.md` (empreintes dans leurs compagnons) ;",
      "points à trancher, `docs/notes/reconception-accumulation-cycle-2-v1/points-a-trancher-cycle-2-v1-brouillon3.md` (empreintes dans leurs compagnons ; le devis reste au brouillon 2) ;",
      "tenue", "renvoi aux points à trancher, brouillon 3")
P.apres("  - contre-lecture 1 de ce texte", [
    "  - vérification des brouillons 2, `" + CHEMIN_RAPPORT + "`, `" + RAPPORT + "` ;",
], "tenue", "rapport de vérification cité")

# --- couples ---
P.sub("**Un critère est dit « fermant » quand son échec à l'épreuve de la famille ferme la lecture** ; seuls le sont ceux qu'une chaîne juste ne peut pas manquer par malchance.",
      "**Un critère est dit « fermant » quand son échec à l'épreuve de la famille ferme la lecture** ; le sont ceux qu'une chaîne juste ne manque pas par malchance ((α) en « le maximum bat », invariance de (α′), (β) forte en « accumuler, propre »), et le compte de (γ), gardé fermant parce qu'il protège contre les fausses issues décisives : une chaîne juste au niveau annoncé le manque par malchance avec une probabilité d'environ 0,03 par côté si les tirages étaient indépendants (arithmétique, version 2, § 3 bis), davantage s'ils ne le sont pas ; ce risque de perdre la famille est accepté et déclaré.",
      "couple", "P-1 (« Deux passages »)")
P.sub("seuls restent « fermants » les critères qu'une chaîne juste ne peut pas manquer par malchance ((α) en « le maximum bat », invariance de (α′), (β) forte en « accumuler, propre », compte de (γ))",
      "restent « fermants » les critères qu'une chaîne juste ne manque pas par malchance ((α) en « le maximum bat », invariance de (α′), (β) forte en « accumuler, propre »), et le compte de (γ), qu'elle ne manque que rarement (environ 0,03 par côté, tirages indépendants supposés), gardé fermant parce qu'il protège contre les fausses issues décisives",
      "couple", "P-1 (table de la contre-lecture 1, ligne B3)")
P.sub("- **réserve « la chaîne ne reconnaît pas un signal propre planté »** : écrite si le signal (α) est reconnu dans moins de quatre tirages sur cinq à l'épreuve de la famille ; l'issue nulle n'est alors pas prononcée.",
      "- **réserve « la chaîne ne reconnaît pas un signal propre planté »** : écrite, avec la part observée, à côté de **toute** phrase du cycle si le signal (α) est reconnu dans moins de quatre tirages sur cinq à l'épreuve de la famille ; l'issue nulle n'est alors pas prononcée, et une issue « gain non propre » ou « non concluant » se lit « propreté non établie par une chaîne qui ne reconnaît pas un signal propre planté », jamais « le signal n'est pas propre ».",
      "couple", "P-2")
P.sub("s'il est imputé à la sonde ((α) sous un tirage sur deux, (α″)), l'analyste peut geler une autre sonde avant `SONDES-ACC2`.",
      "s'il est imputé à la sonde ((α) sous un tirage sur deux, (α″)), l'analyste peut geler une autre sonde avant `SONDES-ACC2` ; si l'épreuve de la principale gelée échoue pour ce motif après `SONDES-ACC2` (au rejeu par le code, après une correction de la chaîne), le scellement est impossible et c'est un nœud de Lazar : rouvrir le temps 1 sous une ligne neuve, l'épreuve rejouée sur des tirages neufs, ou clore le cycle sans lecture, compté et rapporté.",
      "couple", "P-3")
P.sub("**Deux lignes se placent à part** : la liste des tâches (`TACHES-ACC2`), après `RECETTE-FAMILLE-ACC2` et strictement avant `SONDES-ACC2` ;",
      "**Deux lignes se placent à part** : la liste des tâches (`TACHES-ACC2`), après `RECETTE-FAMILLE-ACC2` et strictement avant `SONDES-ACC2` — si elle manque quand l'analyste a fini, ses sorties sont scellées à leur écriture, plus rien n'y change, et la ligne `SONDES-ACC2` attend `TACHES-ACC2` ;",
      "couple", "P-4")
P.sub("ce signal entre à l'épreuve plantée par un brouillon neuf de ce texte, contre-lu ;",
      "ce signal entre aux deux passages de l'épreuve plantée par un brouillon neuf de ce texte, contre-lu, qui écrit son critère et dit s'il est fermant ; l'épreuve du développement est rejouée pour lui avant `CODE-ACC2`, sa sortie versée à côté de la première ;",
      "couple", "P-5")
P.sub("dans un texte neuf scellé et contre-lu avant le tirage, identifiants déjà employés par le programme exclus",
      "dans un texte neuf, écrit par une instance qui n'est ni l'analyste ni un auteur de ce texte, scellé et contre-lu avant le tirage, identifiants déjà employés par le programme exclus",
      "couple", "P-6")

# --- entrée de contre-lecture 2 ---
P.ligne("La vérification du différentiel du brouillon 1 à ce brouillon 2 reste à faire", "\n".join([
    "- **Contre-lecture 2** (vérification des brouillons 2) — sous-agent neuf de la session mère, Claude Opus 5.5 (`claude-opus-5-5`), autre modèle que le rédacteur, autre agent que les deux contre-lecteurs des brouillons 1 ; n'a écrit aucune pièce du second cycle ; ne sera ni analyste, ni développeur, ni lecteur, ni juge. **Brouillon relu** : `prereg/accumulation-cycle-2-v1-brouillon2.md`, `" + P.empreinte + "` (avec les brouillons 2 de l'ordre exploratoire, du devis, du brouillon de décision et des points à trancher). **Rapport** : `" + CHEMIN_RAPPORT + "`, `" + RAPPORT + "`. Verdict pour ce texte : « après ces couples exacts » (P-1 à P-6 : deux majeurs, quatre mineurs). Rejeux du vérificateur : le script de fabrication rend le brouillon 2 à l'octet ; arithmétique identique ; quatorze marqueurs prévus. Son avis sur la conséquence que le rédacteur avait tirée seul du troisième bloquant : cohérente, sans voie vers une issue positive plus facile, à deux précisions près (P-1, P-2). Traitement, couple par couple :",
    "",
    "| couple | traitement dans ce brouillon 3 |",
    "|---|---|",
    "| **P-1** (majeur) — règle des critères fermants énoncée trop fort pour le compte du signal nul | **appliqué tel quel**, aux deux endroits (« Deux passages » ; table de la contre-lecture 1, ligne B3) |",
    "| **P-2** (majeur) — la réserve « la chaîne ne reconnaît pas un signal propre planté » ne visait que l'issue nulle | **appliqué tel quel** |",
    "| **P-3** (mineur) — échec imputé à la sonde après le gel | **appliqué tel quel** |",
    "| **P-4** (majeur pour l'exécution) — liste des tâches absente quand l'analyste a fini | **appliqué tel quel** |",
    "| **P-5** (mineur) — signal ajouté par le bras d'attaque : critère, caractère fermant, rejeu au développement | **appliqué tel quel** |",
    "| **P-6** (mineur) — auteur du texte de la règle du tirage | **appliqué tel quel** (et sa suite dans les points à trancher, section E, et dans l'ordre exploratoire, section 6) |",
    "| tenue | version, date, mandat, statut, renvois aux brouillons 3 de l'ordre exploratoire et des points à trancher, rapport de vérification cité, cette entrée ; rien d'autre : le reste est égal au brouillon 2, à l'octet |",
]), "tenue", "entrée « Contre-lecture 2 » et table de traitement")

# ====================================================================================================
# 2. Ordre exploratoire
# ====================================================================================================
O = Piece(DOSSIER + "ordre-exploratoire-temps-1-v1-brouillon2.md",
          "21fe8ff47634511b8f6055c2f27d6de3764a20a8e0e2036a16a8dc3034f0550f",
          DOSSIER + "ordre-exploratoire-temps-1-v1-brouillon3.md")

O.sub("— v1 — brouillon 2", "— v1 — brouillon 3", "tenue", "version (titre)")
O.sub("brouillon 2 le 2026-11-18 après 19:05.", "brouillon 2 le 2026-11-18 après 19:05 ; brouillon 3 le 2026-11-18 après 19:36.", "tenue", "date")
O.sub("La confirmation est le texte `prereg/accumulation-cycle-2-v1-brouillon2.md`, lu une seule fois sur une famille neuve.",
      "La confirmation est le texte `prereg/accumulation-cycle-2-v1-brouillon3.md`, lu une seule fois sur une famille neuve.",
      "tenue", "renvoi au préenregistrement, brouillon 3")
O.sub("- **Statut** : **brouillon 2** = brouillon 1 (",
      "- **Statut** : **brouillon 3** = brouillon 2 (`ordre-exploratoire-temps-1-v1-brouillon2.md`, `" + O.empreinte + "`, gardé tel quel, R12) + les couples exacts O-1 et O-2 de la vérification des brouillons 2 (`" + CHEMIN_RAPPORT + "`, `" + RAPPORT + "`), appliqués par script (`pieces-redaction-cycle-2-v1/brouillons3-faire-v1.py`) ; table en section 10. Le brouillon 2 était lui-même : brouillon 1 (",
      "tenue", "statut")

O.sub("(défaut prudent du rédacteur : elles ne sont pas des sorties que cite le registre ; la session mère peut en décider autrement, par écrit)",
      "(défaut prudent du rédacteur : elles ne sont pas des sorties que cite le registre ; Lazar peut en décider autrement, points à trancher, point 14 ; la session mère ne fixe aucun choix d'analyse)",
      "couple", "O-1")
O.sub("2. **Limite de temps** : sept jours après `OUVERTURE-TEMPS1-ACC2`.",
      "2. **Limite de temps** : sept jours après `OUVERTURE-TEMPS1-ACC2` (elle porte sur le travail de l'analyste ; si la ligne `TACHES-ACC2` manque à cette échéance, ses sorties sont scellées à leur écriture et la ligne `SONDES-ACC2` attend la liste).",
      "couple", "O-2 (section 8, point 2)")
O.sub("l'instance qui conçoit la famille neuve, celle qui extrait ses tâches, et toute instance qui a lu sa recette ou sa liste ;",
      "l'instance qui conçoit la famille neuve, celle qui écrit la règle du tirage de ses tâches, celle qui les extrait, et toute instance qui a lu sa recette ou sa liste ;",
      "couple", "O-2 (section 6, premier tiret ; avec P-6)")
O.sub("les traces de la course arrêtée ne sont pas permises, sauf écrit contraire de la session mère |",
      "les traces de la course arrêtée ne sont pas permises, sauf décision contraire de Lazar (aligné sur le couple O-1 de la vérification des brouillons 2) |",
      "alignement", "table de la contre-lecture 1, mineur 9 : alignée sur O-1")
O.fin([
    "## 10. Traitement des couples de la vérification des brouillons 2",
    "",
    "Rapport : `" + CHEMIN_RAPPORT + "`, `" + RAPPORT + "` (agent neuf, Claude Opus 5.5) ; verdict pour cet ordre : « après ces couples exacts ».",
    "",
    "| couple | traitement dans ce brouillon 3 |",
    "|---|---|",
    "| **O-1** (mineur) — qui peut permettre les traces de la course arrêtée | **appliqué tel quel** (section 2, lot D) |",
    "| **O-2** (avec P-4 et P-6) — limite de temps et liste des tâches ; auteur de la règle du tirage exclu | **appliqué tel quel**, aux deux endroits (section 8, point 2 ; section 6, premier tiret) |",
    "| alignement, hors couple, déclaré | la ligne « mineur 9 » de la table de la section 9 disait « sauf écrit contraire de la session mère » : alignée sur O-1 |",
    "| tenue | version, date, statut, renvoi au préenregistrement (brouillon 3), cette section ; rien d'autre : le reste est égal au brouillon 2, à l'octet |",
], "tenue", "section 10 : table de traitement")

# ====================================================================================================
# 3. Points à trancher
# ====================================================================================================
T = Piece(DOSSIER + "points-a-trancher-cycle-2-v1-brouillon2.md",
          "5fccf8c780f3e1c1c9c2eacd0180465774ee870dceb668011f0f54a8616c5083",
          DOSSIER + "points-a-trancher-cycle-2-v1-brouillon3.md")

T.sub("— v1 — brouillon 2", "— v1 — brouillon 3", "tenue", "version (titre)")
T.sub("**Date (UTC)** : 2026-11-18, après 19:05.", "**Date (UTC)** : 2026-11-18, après 19:36.", "tenue", "date")
T.sub("- **Statut** : brouillon 2 = brouillon 1 (",
      "- **Statut** : brouillon 3 = brouillon 2 (`points-a-trancher-cycle-2-v1-brouillon2.md`, `" + T.empreinte + "`, gardé tel quel) + les couples exacts T-1 à T-4 de la vérification des brouillons 2 (agent neuf, Claude Opus 5.5, `" + CHEMIN_RAPPORT + "`, `" + RAPPORT + "`), qui juge le devis et le brouillon de décision bons pour t'être soumis ; section G. Le brouillon 2 était lui-même : brouillon 1 (",
      "tenue", "statut")
T.ligne("- **Textes servis**",
        "- **Textes servis** (empreintes dans leurs compagnons) : l'ordre exploratoire du temps 1 et le préenregistrement de la confirmation unique, **brouillons 3** (`prereg/accumulation-cycle-2-v1-brouillon3.md`) ; le devis et le brouillon de décision sur la porte de fin de phase 1, **brouillons 2**, inchangés (`docs/decisions/decision-N-074-v1-brouillon2.md`).",
        "tenue", "textes servis")

T.sub("J'en ai tiré une conséquence que personne n'a encore relue : seuls les critères qu'une chaîne juste ne peut pas manquer par malchance ferment la lecture ; les autres posent une réserve.",
      "J'en ai tiré une conséquence, relue par un vérificateur neuf : ferment la lecture les critères qu'une chaîne juste ne manque pas par malchance, et le compte du signal nul, qu'elle ne manque que rarement (de l'ordre de trois chances sur cent par côté) et qui garde contre les fausses réussites ; les autres posent une réserve.",
      "couple", "T-1")
T.sub("**La règle qui commande tout** : le temps 1 ne s'ouvre qu'après les deux verdicts scellés — la lecture des sondes (étape B) et l'apprentissage des sondes sur la tâche (étape B bis).",
      "**La règle qui commande tout** : le temps 1 ne s'ouvre qu'après les deux verdicts scellés — la lecture des sondes (étape B) et l'apprentissage des sondes sur la tâche (étape B bis) — et, tant que tu ne réponds pas autrement au point 14, après leur table conjointe et le verdict de la validité de l'adaptateur, dont je ne connais pas l'échéance.",
      "couple", "T-2")
T.sub("La section C dit ce qui peut exister avant le 27 novembre :",
      "La section C dit ce qui peut exister avant le 27 novembre (ton entretien avec le fonds « Transformative AI Fund », fixé au 27 novembre 2026 ; source transmise par la session mère, que je n'ai pas relue : registre des décisions, lignes R-2130 et R-2382, et accord GO-2026-11-18-30 du registre des accords, « résultats prêts le 24 ou le 25 novembre pour l'entretien du 27 ») :",
      "couple", "T-3, complété par la source que la session mère a transmise")
T.sub("- Les épisodes naturels sont décrits, jamais décisifs, et seulement aux doses où ni le lecteur « mots et coût » ni un lecteur lexical ne sépare.",
      "- Les épisodes naturels sont rapportés à toutes les doses, jamais décisifs, et jugés seulement aux doses où ni le lecteur « mots et coût » ni un lecteur lexical ne sépare.",
      "couple", "T-4")
T.sub("l'entropie du tirage vient de l'empreinte du texte de la règle, comme pour le premier tirage",
      "l'entropie du tirage vient de l'empreinte du texte de la règle, comme pour le premier tirage, ou d'une graine écrite dans la recette",
      "couple", "P-6 (suite, section E, point 1)")

T.apres("- **À part, si tu les décides**", [
    "- **Deux chiffres du devis** n'étaient dans aucune sortie scellée du calcul ; ils y sont maintenant (`pieces-redaction-cycle-2-v1/sortie-calculs-redaction-cycle-2-v3.txt`, § 9, empreinte dans son compagnon ; le devis n'est pas refait) : le surcoût de la relecture « couche par couche » du point 4 (1,6 à 2,5 heures de carte, 1,7 à 3,3 USD), et le pire cas de la famille neuve avec une relance entière de la génération (325 à 474 USD selon l'effectif : au-dessus des deux plafonds du point 5, d'où les deux gardes).",
], "couple", "D-1 : citation de la sortie de calcul v3")

T.sub("La vérification du brouillon 2 par un contre-lecteur neuf doit porter d'abord sur la conséquence du point (ii).",
      "La vérification des brouillons 2 a porté d'abord sur la conséquence du point (ii) : elle la juge cohérente et sans voie vers une réussite plus facile, à deux précisions près, appliquées au brouillon 3.",
      "alignement", "point 11 : la vérification demandée est faite")
T.sub("| vérification des brouillons 2 par un contre-lecteur neuf, ordre exploratoire scellé | un tour de contre-lecture : quelques heures | oui |",
      "| vérification des brouillons 2 : faite ; reste à sceller l'ordre exploratoire, une fois ses empreintes remplies | quelques heures | oui |",
      "alignement", "section C : la vérification est faite")
T.sub("J'en ai tiré la distinction entre critères qui ferment la lecture et critères qui posent une réserve (point 11). Non relu.",
      "J'en ai tiré la distinction entre critères qui ferment la lecture et critères qui posent une réserve (point 11). Relu par le vérificateur des brouillons 2 : cohérent, deux précisions appliquées.",
      "alignement", "section E, point 2 : « Non relu » n'est plus vrai")
T.apres("- **Lu** : les deux rapports de contre-lecture", [
    "- **Dernière passe (brouillon 3)** : le rapport de vérification des brouillons 2, entier (compagnon vérifié) ; rien d'autre de nouveau. La source de la date du 27 novembre m'a été transmise par la session mère ; je n'ai ouvert aucun registre.",
], "tenue", "section F : lecture de la dernière passe")
T.fin([
    "---",
    "",
    "## G. Ce qui a changé du brouillon 2 au brouillon 3",
    "",
    "La vérification des brouillons 2 (`" + CHEMIN_RAPPORT + "`, `" + RAPPORT + "`) juge le devis et le brouillon de décision bons pour t'être soumis, et demande des couples exacts pour le préenregistrement, l'ordre exploratoire et ce texte. Ils sont appliqués par script (`pieces-redaction-cycle-2-v1/brouillons3-faire-v1.py`) ; le reste est égal au brouillon 2, à l'octet.",
    "",
    "| couple | traitement |",
    "|---|---|",
    "| **T-1** — la conséquence du point 11 (ii), relue | appliqué tel quel |",
    "| **T-2** — conditions d'ouverture du temps 1 dans le calendrier | appliqué tel quel |",
    "| **T-3** — source de la date du 27 novembre | **appliqué avec la source** que la session mère m'a transmise (le vérificateur demandait qu'elle l'écrive) ; je ne l'ai pas relue au registre |",
    "| **T-4** — épisodes naturels : rapportés partout, jugés à certaines doses | appliqué tel quel |",
    "| **P-6** (suite) — section E, point 1 | appliqué tel quel |",
    "| **D-1** — deux chiffres du devis absents de la sortie scellée du calcul | sortie de calcul version 3 scellée, citée en section D ; le devis n'est pas refait |",
    "| alignements, hors couples, déclarés | trois mentions que la vérification a rendues fausses : fin du point 11 ; une ligne du calendrier ; « Non relu » en section E |",
    "| tenue | version, date, statut, textes servis, une ligne de lectures, cette section |",
], "tenue", "section G : table de traitement")

for piece in (P, O, T):
    piece.ecrire()
