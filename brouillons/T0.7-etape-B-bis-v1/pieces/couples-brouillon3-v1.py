"""Brouillon 3 du préenregistrement de l'étape B bis de T0.7 = brouillon 2 + ces remplacements : couples K1 à K6 de la
vérification courte (`verification-courte-brouillon2-v1.md`, a4e6f02d0b318c4823d76e71912a1f1a1bc47462f78050338d546168baf46e3c,
R-2742) ; mots de Lazar et ligne GO-2026-11-14-09 recopiés (R-2740) ; nœud 5 tranché avant toute lecture ; vérification courte
citée (message de la mère du 2026-11-14 vers 12:15 UTC). Deux formes : « couple » (ancien présent exactement une fois) et
« entre » (de la première occurrence, unique, d'un début à la première fin qui suit, bornes comprises). Le brouillon 2 n'est
pas touché (R12). Lancement : `python3 -I -B couples-brouillon3-v1.py <dossier du brouillon>`.
"""
import hashlib
import re
import sys
from pathlib import Path

DOSSIER = Path(sys.argv[1])
B2 = DOSSIER / "T0.7-etape-B-bis-v1-brouillon2.md"
B3 = DOSSIER / "T0.7-etape-B-bis-v1-brouillon3.md"
EMPREINTE_B2 = "cbfec6aaa4c650443dcea7bac4d0c61bf4a8fdd34ec90572b434a45180184c88"
VERIF = ("`brouillons/T0.7-etape-B-bis-v1/verification-courte-brouillon2-v1.md`, "
         "`a4e6f02d0b318c4823d76e71912a1f1a1bc47462f78050338d546168baf46e3c`")
Q1 = "Les cinq décisions de l’étape B bis, dont la dépense de 40 USD, à me donner au plus tard mardi. : go recos"
Q2 = ("La dépense de B bis : 40 USD, sur une A100, avec une relance au plus. […] Un petit écart au gabarit des "
      "préenregistrements : le code ne sera cité qu’après le scellement du texte, faute de temps. C’est déjà arrivé une "
      "fois, mais cette précédente autorisation ne valait pas pour toujours. : go")

texte = B2.read_text(encoding="utf-8")
assert hashlib.sha256(texte.encode("utf-8")).hexdigest() == EMPREINTE_B2, "brouillon 2 modifié"
assert not B3.exists(), "brouillon 3 déjà écrit (R12)"
journal = []


def couple(ancien, nouveau, nom):
    global texte
    n = texte.count(ancien)
    if n != 1:
        raise SystemExit(f"{nom} : « ancien » présent {n} fois : {ancien[:90]!r}")
    texte = texte.replace(ancien, nouveau)
    journal.append(nom)


def entre(debut, fin, nouveau, nom):
    global texte
    n = texte.count(debut)
    if n != 1:
        raise SystemExit(f"{nom} : début présent {n} fois : {debut[:90]!r}")
    i = texte.index(debut)
    j = texte.find(fin, i + len(debut))
    if j < 0:
        raise SystemExit(f"{nom} : fin absente après le début : {fin[:90]!r}")
    texte = texte[:i] + nouveau + texte[j + len(fin):]
    journal.append(nom)


# En-tête
couple("lecture conjointe avec l'étape B — v1 — brouillon 2", "lecture conjointe avec l'étape B — v1 — brouillon 3", "D01 titre")
couple("- **Date (UTC)** : brouillon 2 écrit le 2026-11-14 de 11:52 à 12:09 (`date -u`) ;",
       "- **Date (UTC)** : brouillon 3 écrit le 2026-11-14 à partir de 12:16 (`date -u`) ; brouillon 2 de 11:52 à 12:09 ;", "D02 date")
couple("Écart au gabarit déclaré, de même forme que DS-3 bis de T0.7 et que `CODE-VADAPT` du texte de validité.",
       f"Écart au gabarit **accordé par Lazar** (R-2740, verbatim : « {Q2} »), de même forme que DS-3 bis de T0.7 (dont l'autorisation ne valait que pour T0.7).",
       "D03 écart accordé")
couple("(traitement demandé ; décision de la mère : le nœud 5 n'a pas de défaut) ;",
       "(traitement demandé ; décision de la mère : le nœud 5 n'a pas de défaut) ;\n"
       f"  - vérification courte du brouillon 2 : {VERIF} (R-2742) ;\n"
       "  - mots de Lazar sur les cinq nœuds, la dépense et l'écart au gabarit : `registres/decisions.md`, R-2740 (2026-11-14, 12:15 UTC) ; "
       "ligne de GO : `registres/go.md`, `GO-2026-11-14-09` ; lues au commit `744a996776485a079eb6f641af93608a56bc7622` (registres vivants, cités par commit et ligne) ;",
       "D04 documents")
entre("  - pièces de ce brouillon (versions 2 ; les versions 1 restent, R12) :", "(empreintes dans leurs compagnons `.sha256`) ;",
      "  - pièces de ce brouillon (les versions antérieures restent, R12) : conception `brouillons/T0.7-etape-B-bis-v1/conception-etape-b-bis-v3.md` ; "
      "calculs `pieces/calculs-bbis-v2.py` et sortie `pieces/sortie-calculs-bbis-v2.txt` ; devis `devis-etape-b-bis-v3.md` ; nœuds tranchés "
      "`noeuds-etape-b-bis-v3.md` ; remplacements `pieces/couples-brouillon2-v1.py` et `pieces/couples-brouillon3-v1.py` (empreintes dans leurs compagnons `.sha256`) ;",
      "D05 pièces")
entre("- **Statut** : **brouillon 2** = brouillon 1 (", "commandée par la mère. Il ne vaut",
      "- **Statut** : **brouillon 3** = brouillon 2 (`cbfec6aaa4c650443dcea7bac4d0c61bf4a8fdd34ec90572b434a45180184c88`, gardé tel quel, R12) "
      "+ les remplacements de `pieces/couples-brouillon3-v1.py` : couples K1 à K6 de la vérification courte (R-2742), mots de Lazar et ligne "
      "GO-2026-11-14-09 recopiés (R-2740), nœud 5 tranché avant toute lecture (« lecture dure »), vérification courte citée ; non scellé. Il ne vaut",
      "D06 statut")
couple("- **Jamais vu** : aucun fichier de `diag/`",
       "- **Lu pour le brouillon 3** : le rapport de la vérification courte (`a4e6f02d…`, entier), les lignes R-2740 et R-2742 (entières), la ligne "
       "`GO-2026-11-14-09` de `registres/go.md` (entière), le message de la mère de 12:15 UTC. Rien d'autre de neuf ; aucune sortie de 7a, 7b, T0.7 ni de l'étape B.\n"
       "- **Jamais vu** : aucun fichier de `diag/`", "D07 savoir")

# Hypothèse
couple("le défaut (a) du nœud 1 ne change aucune ligne de la porte ; (b) et (c) attendent le mot de Lazar.",
       f"**nœud 1 tranché : (a) hors de G0**, rapportée à part, guide la reconception des sondes (R-2740 ; mots de Lazar, verbatim : « {Q1} ») : aucune ligne de la porte ne change.",
       "D08 nœud 1")
couple("est écrit dans sa forme et n'est joué que sur décision de Lazar (nœud 3 ; plan, point 9).",
       "n'est **pas joué à cette course** : nœud 3 tranché (a), R-2740 — transfert entre familles maintenant, mode tenu à l'écart propre à B bis plus tard, sur devis ; le mode tenu à l'écart de G1 n'est pas consommé (plan, point 9).",
       "D09 nœud 3")
couple("elle entre dans le libellé « lecture dure » du nœud 5, qui ne peut que restreindre « plafond tient » (section « Critères », B).",
       "elle est une condition du libellé « lecture dure », **retenu par Lazar avant toute lecture** (nœud 5, R-2740), qui ne peut que restreindre « plafond tient » (section « Critères », B).",
       "D10 HB-3m")
couple("elle n'entre que dans le libellé « lecture dure » (section « Critères », B).",
       "elle n'est une condition que du libellé « lecture dure », retenu (nœud 5, R-2740 ; section « Critères », B).", "D11 MU")

# Seuil (K6, et code cité après le scellement)
entre("versée avec le code et lue **avant le scellement**", "épreuve citée : `<<EPREUVE_NIVEAU_DEUX_PLIS>>`.",
      "versée avec le code et lue **avant toute ouverture de données de 7b** (le code étant cité après le scellement, écart accordé, R-2740) : "
      "taux de fausse lecture « au-dessus » au niveau de 99 % ; s'il dépasse 0,01 (deux fois le nominal de 0,005) en estimation ponctuelle dans "
      "une cellule de l'épreuve, le niveau décisif devient **99,5 %**, par cette règle écrite ici, appliquée mécaniquement et inscrite avec la ligne "
      "`CODE-BBIS`, avant toute marche ; son coût de calcul sur processeur est écrit avec le résultat ; la puissance à 99,5 % est recalculée par une "
      "version neuve du script de calculs si ce niveau est retenu (K6) ; épreuve citée : `<<EPREUVE_NIVEAU_DEUX_PLIS>>`.",
      "D12 épreuve de niveau")

# Plan d'analyse
couple("`SCORES-BBIS`, `LIBELLE-BBIS` (seulement s'il y a un choix de Lazar au nœud 5), lecture,", "`SCORES-BBIS`, lecture,", "D13 ordre (K1)")
couple("après les 20 premiers apprentissages de la marche, la médiane",
       "après les 20 premiers apprentissages de la marche, pris dans un ordre d'exécution qui entrelace les deux familles (dix de chaque), la médiane",
       "D14 débit (K6)")
couple("**joué seulement si Lazar le décide (nœud 3)**, par un addendum scellé avant toute génération ; sinon « non joué à cette course ».",
       "**non joué à cette course** : nœud 3 tranché (a), R-2740 ; un mode tenu à l'écart propre à B bis sera demandé plus tard, sur devis, par un addendum scellé avant toute génération ; le mode tenu à l'écart de G1 n'est pas consommé.",
       "D15 T-M")
couple("(e) états, issue, suffixe, **les deux libellés du nœud 5**, lignes (i-a), réserves, audit R4 ;",
       "(e) états, issue, suffixe, **libellé « lecture dure »** (retenu) et libellé d'information, lignes (i-a), réserves, audit R4 ;", "D16 lecture (e)")
couple("un troisième lecteur neuf la prononce (nœud 2) ;",
       "un troisième lecteur neuf la prononce (nœud 2 tranché : même hôte que l'étape B, session neuve du compte 3, lecteurs distincts, R-2740) ;",
       "D17 nœud 2")
entre("**Libellés du nœud 5** : les deux libellés", "jamais comme une lecture préenregistrée (R3).",
      "**Libellé du nœud 5, tranché avant toute lecture** (R-2740, 2026-11-14 12:15 UTC, avant toute exécution de l'étape B et de B bis ; K1) : "
      "**« lecture dure »** est le sens de « plafond tient » ; il titre le verdict, la table conjointe et le billet ; le libellé « lettre de R-2716 » "
      "et la variante correspondante de la table conjointe sont écrits **dessous, comme information seulement**, jamais décisifs ; ni l'un ni l'autre "
      "ne change un état, l'issue I ou une ligne C de la variante retenue (K2). La règle « choisi après lecture » et la ligne `LIBELLE-BBIS` sont "
      "retirées, sans objet.",
      "D18 nœud 5 (K1, K2)")

# Critères (K3)
couple("| I6 **plafond tient** | le plus haut est E6 |", "| I6 **au bout (au-delà de l'artefact)** | le plus haut est E6 |", "D19 I6 (K3)")
couple("Transfert de mode : [non joué à cette course (nœud 3) | état et phrase de T-M]. »",
       "Transfert de mode : non joué à cette course (nœud 3, R-2740). »", "D20 transfert de mode")
couple("« **Plafond tient, transfert échoue** » = I6 suivi de T−.",
       "« **Au bout, transfert échoue** » = I6 suivi de T− ; « **Plafond tient, transfert échoue** » = libellé « lecture dure » à « oui » (I6 et muette sur le jumeau à au moins une dose) suivi de T− (K3).",
       "D21 issues nommées (K3)")
couple("**Libellés du nœud 5** (aucun défaut, décision de la mère ; les deux toujours écrits côte à côte, chacun « oui » ou « non », avec les doses ; libellé principal : plan, point 11) :",
       "**Libellés du nœud 5** (tranché avant toute lecture, R-2740 : « lecture dure » retenu ; l'autre, information seulement ; chacun écrit « oui » ou « non », avec les doses ; plan, point 11) :",
       "D22 libellés")
couple("**« plafond tient — lettre de R-2716 »** si au moins une dose de (ii) est en E5 ou E6 : phrase « À la lettre de R-2716 (séparation à texte égal), le plafond tient aux doses [D]. » ou « À la lettre de R-2716, le plafond ne tient à aucune dose. ».",
       "**libellé d'information « lettre de R-2716 »** si au moins une dose de (ii) est en E5 ou E6 : phrase « Information (lettre de R-2716) : la séparation à texte égal est établie aux doses [D]. » ou « Information (lettre de R-2716) : la séparation à texte égal n'est établie à aucune dose. ».",
       "D23 libellé d'information (K3)")
couple("Le libellé dur ne peut qu'être plus rare que celui de la lettre ; aucun des deux ne change les états ni l'issue I.",
       "Le libellé retenu ne peut qu'être plus rare que le libellé d'information ; aucun des deux ne change les états ni l'issue I ; seul le libellé retenu s'appelle « plafond tient » (K3).",
       "D24 libellés, fin")
couple("**Deux variantes, calculées et écrites côte à côte** (nœud 5, sans défaut) : variante **« lecture dure »** :",
       "**Variante retenue « lecture dure »** (nœud 5, R-2740) :", "D25 table C, variante retenue")
couple("; variante **« lettre de R-2716 »** : une dose « tient » si elle est en E5 ou E6 ;",
       "; **variante d'information « lettre de R-2716 »**, écrite dessous, jamais décisive : une dose « tient » si elle est en E5 ou E6 ;",
       "D26 table C, variante d'information")
couple("chaque ligne est écrite pour les deux variantes, côte à côte |",
       "chaque ligne est écrite pour la variante retenue, puis, dessous, pour la variante d'information |", "D27 table C, en-tête")
couple("ce qui est lu n'est pas seulement le texte. » |",
       "ce qui est lu n'est pas seulement le texte. » ; dans la variante d'information, suivie de « (aux doses en E5, l'artefact d'adaptateur n'est pas écarté : R-ART) » (K3) |",
       "D28 C1 (K3)")
couple("(1) un « plafond tient » dit", "(1) un « plafond tient » (libellé « lecture dure », retenu ; de même pour la ligne I6 et pour le libellé d'information) dit", "D29 D (1) (K3)")
couple("(nœud 1) ; le bras plafond", "(nœud 1 tranché, R-2740) ; le bras plafond", "D30 D (1), nœud 1")
couple("(le transfert de mode n'est pas joué à cette course, nœud 3)", "(le transfert de mode n'est pas joué à cette course : nœud 3 tranché, R-2740)", "D31 D (2)")
entre("(6) les deux libellés", "retient la condition « muette sur le jumeau ».",
      "(6) le libellé d'information (lettre de R-2716) ne dit pas « plafond tient » : seul le libellé « lecture dure », retenu, écarte de façon établie l'adaptateur seul et retient la condition « muette sur le jumeau ».",
      "D32 D (6) (K3)")

# Liste d'arrêt (K4, K5 levé, K6)
couple("une marche lente mais vivante n'est jamais arrêtée ;", "une marche lente mais vivante n'est jamais arrêtée, hors la garde de débit (plan, point 5) ;", "D33 K4")
couple("(avant l'instance)", "(MC se calcule à la lecture, sur processeur : l'instance n'attend pas ce relevé)", "D34 K6 repli de MC")
couple("- Épreuve de niveau de la règle (a) en deux plis (« Seuil ») absente au candidat : pas de scellement.",
       "- Épreuve de niveau de la règle (a) en deux plis (« Seuil ») absente à l'inscription de `CODE-BBIS` : `CODE-BBIS` n'est pas inscrite, aucune marche.",
       "D35 épreuve de niveau")
entre("(`<<LIGNE_GO_BBIS>>` ; proposé : 39,5 USD", "aucune création sans `GO-BBIS`, `CODE-BBIS` et `SCELLEMENT-BBIS`.",
      "(ligne **GO-2026-11-14-09**, 40 USD, A100 seulement, une relance au plus, échéance 2026-11-22 ; coupure à 39,5 USD, cumul relevé plus un quart "
      "d'heure ; aucune H200) ; instance hors des bornes de l'offre ; aucune création sans `GO-BBIS` (extrait de GO-2026-11-14-09), **le feu écrit de la "
      "mère portant ce numéro**, `CODE-BBIS` et `SCELLEMENT-BBIS` ; une seconde relance est exclue.",
      "D36 dépense (K5 levé)")

# Calcul et dépense ; registre
couple("Devis : `brouillons/T0.7-etape-B-bis-v1/devis-etape-b-bis-v2.md` (la v1 reste).",
       "Devis : `brouillons/T0.7-etape-B-bis-v1/devis-etape-b-bis-v3.md` (les versions antérieures restent).", "D37 devis v3")
entre("**Aucune ligne de GO n'est inscrite** (R-2716 (3))", "(`<<LIGNE_GO_BBIS>>`).",
      "**Ligne de GO inscrite sur le mot de Lazar** : `GO-2026-11-14-09` (`registres/go.md` ; R-2740) : « calcul », 40 USD, échéance 2026-11-22, une "
      "A100 seulement, une relance au plus, garde de débit, code cité après le scellement, feu écrit de la mère avec ce numéro avant toute location, "
      f"arrêt et destruction par identifiant (R10) ; mot de Lazar, verbatim : « {Q2} » ; la ligne `GO-BBIS` du registre propre en recopie l'extrait.",
      "D38 ligne de GO")
couple("`SCORES-BBIS`, `LIBELLE-BBIS` (choix de Lazar au nœud 5, s'il précède `LECTURE-BBIS`), `LECTURE-BBIS`,", "`SCORES-BBIS`, `LECTURE-BBIS`,", "D39 registre (K1)")

# Calendrier
entre("| sam. 14 |", "|\n| dim. 15 |",
      "| sam. 14 | brouillons 1 à 3, contre-lecture 1 et vérification courte (modèle C) ; cinq nœuds tranchés et ligne GO-2026-11-14-09 (R-2740) |\n| dim. 15 |",
      "D40 samedi")
entre("| dim. 15 |", "|\n| lun. 16 |",
      "| dim. 15 | code et essais (développeur neuf, sans vue des données) ; vérification courte du différentiel du brouillon 3 si la mère la commande → candidat |\n| lun. 16 |",
      "D41 dimanche")
entre("| lun. 16 |", "|\n| mar. 17 |",
      "| lun. 16 | `CODE_MOTS_ET_COUT_T06` rempli (état à cette heure) ; **`SCELLEMENT-BBIS` et `ABSENCE-B-BBIS` avant toute exécution de l'étape B** (les cinq nœuds sont tranchés, R-2740 : aucun défaut à attendre) ; contre-lecture du code (modèle C) |\n| mar. 17 |",
      "D42 lundi")
entre("| mar. 17 |", "|\n| mer. 18 |",
      "| mar. 17 | épreuve de niveau ; `CODE-BBIS` (commit, empreintes, entropie, issue de l'épreuve de niveau ; écart accordé, R-2740) ; `GO-BBIS` (extrait de GO-2026-11-14-09) ; ordre d'exécution contre-lu ; répétition à blanc ; feu écrit de la mère |\n| mer. 18 |",
      "D43 mardi")

# Nœuds : section entière
entre("## Nœuds\n\n", "\n\n## Contre-lecture",
      "## Nœuds\n\n"
      f"**Tranchés par Lazar le 2026-11-14 à 12:15 UTC, avant toute lecture** (`registres/decisions.md`, R-2740 ; mots de Lazar, verbatim : « {Q1} » et « {Q2} » ; "
      "détail : `noeuds-etape-b-bis-v3.md`) : (1) place face à G0 → **(a) hors de G0**, rapportée à part, guide la reconception des sondes ; "
      "(2) hôte des lecteurs → **(a) même hôte que l'étape B (session neuve du compte 3), lecteurs distincts** ; (3) transfert de mode → **(a) transfert "
      "entre familles maintenant**, mode tenu à l'écart propre à B bis plus tard, sur devis ; le mode tenu à l'écart de G1 n'est pas consommé ; "
      "(4) dépense → **ligne GO-2026-11-14-09**, 40 USD, A100, une relance au plus, échéance 22 novembre, et **écart au gabarit accordé** (code cité après "
      "le scellement) ; (5) sens de « plafond tient » → **« lecture dure »**, retenu avant toute lecture (au-delà de l'artefact d'adaptateur, avec preuve "
      "positive, et muette sur le jumeau) ; le libellé « lettre de R-2716 » reste écrit comme information.\n\n## Contre-lecture",
      "D44 nœuds tranchés")

# Contre-lecture : vérification courte
couple("- **Vérification courte du brouillon 2** : `<<VERIFICATION_COURTE_BROUILLON2>>` (sous-agent neuf commandé par la mère : empreinte du brouillon 2, chemin et empreinte de son rapport, traitement).",
       "- **Vérification courte du brouillon 2** : sous-agent neuf, « modèle C » ; brouillon relu : brouillon 2, `cbfec6aaa4c650443dcea7bac4d0c61bf4a8fdd34ec90572b434a45180184c88` ; "
       f"rapport : {VERIF} (R-2742), de 12:09 à 12:14 UTC ; verdict « scellable après corrections » (K1 à K6). **Traitement** (brouillon 3, `pieces/couples-brouillon3-v1.py`) :\n\n"
       "| couple | traitement | où |\n|---|---|---|\n"
       "| K1 | **accepté et dépassé** : le nœud 5 est tranché avant toute lecture (R-2740) ; la règle « choisi après lecture » et la ligne `LIBELLE-BBIS` sont retirées, sans objet | plan, points 2 et 11 ; Lignes de registre |\n"
       "| K2 | **accepté** : le libellé retenu titre le verdict, la table conjointe et le billet ; l'autre est écrit dessous, comme information, jamais décisif ; aucun état, aucune issue, aucune ligne C de la variante retenue ne change | plan, point 11 ; Critères B et C |\n"
       "| K3 | **accepté** : I6 s'intitule « au bout (au-delà de l'artefact) » ; « plafond tient » ne désigne que le libellé « lecture dure » ; « plafond tient, transfert échoue » = libellé retenu à « oui » suivi de T− ; « au bout, transfert échoue » = I6 suivi de T− ; le libellé d'information est renommé ; D (1) et D (6) précisés ; C1 de la variante d'information porte la mention de l'artefact | Critères B, C et D |\n"
       "| K4 | **accepté** | Liste d'arrêt |\n"
       "| K5 | **levé par R-2740** : les marqueurs de la ligne de GO et de l'écart au gabarit sont remplis (GO-2026-11-14-09 ; écart accordé) ; la précision « sans mot au scellement » est sans objet | Calcul et dépense ; Liste d'arrêt ; Nœuds |\n"
       "| K6 | **accepté** : vingt premiers apprentissages entrelacés (dix par famille) ; « avant l'instance » remplacé ; coût et puissance de l'épreuve de niveau écrits ; devis v3 (raison du « + 1,0 h » de disque) ; conception v3 (égalité « si le fichier existe ») ; ligne sur « tâches témoins » pour l'envoi des nœuds | plan, point 5 ; Liste d'arrêt ; Seuil ; devis v3 ; conception v3 ; nœuds v3 |\n"
       "| point a | **accepté** : « l'adversaire « tâches témoins » de R-2716 est rendu sous la forme d'un nul de réétiquetage par tâche, aux limites écrites » ; une ligne à dire à Lazar par la mère | nœuds v3 |\n\n"
       "Conséquence déclarée de l'écart accordé : l'épreuve de niveau, versée avec le code, se lit après le scellement et avant toute ouverture de données ; sa règle (99 % ou 99,5 %) est écrite ici.",
       "D45 vérification courte")

# Marqueurs : section entière
entre("## Marqueurs à remplir avant le scellement\n\n", "(constat M2).",
      "## Marqueurs à remplir avant le scellement\n\n"
      "**Restent ouverts quatre marqueurs** : `<<CODE_BBIS>>` et `<<ENTROPIE_BBIS>>` (commit, empreintes et entropie de 128 bits, à l'inscription de "
      "`CODE-BBIS`, après le scellement : écart accordé, R-2740) ; `<<EPREUVE_NIVEAU_DEUX_PLIS>>` (chemin, empreinte, taux et niveau retenu, inscrits avec "
      "`CODE-BBIS`) ; `<<CODE_MOTS_ET_COUT_T06>>` (état de la ligne `CODE-MOTS-ET-COUT-T06` à l'heure du scellement). **Au scellement** (le validateur "
      "`prereg.problemes` refuse tout marqueur restant) : `<<CODE_MOTS_ET_COUT_T06>>` est rempli par l'état à cette heure ; les trois autres sont remplacés, "
      "par un dernier couple mécanique, par le renvoi « inscrit par la ligne `CODE-BBIS` du registre propre, après le scellement et avant toute exécution "
      "(écart accordé, R-2740) » ; aucun autre contenu ne change. **Remplis au brouillon 3** : mots de Lazar des nœuds 1 à 3, écart au gabarit, ligne "
      "GO-2026-11-14-09 (R-2740), vérification courte (R-2742) ; le nœud 5 est tranché.",
      "D46 marqueurs")

restes = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)))
attendus = ["<<CODE_BBIS>>", "<<CODE_MOTS_ET_COUT_T06>>", "<<ENTROPIE_BBIS>>", "<<EPREUVE_NIVEAU_DEUX_PLIS>>"]
if restes != attendus:
    raise SystemExit(f"marqueurs restants inattendus : {restes}")
for interdit in ("LIBELLE-BBIS", "choisi après lecture", "MOT_LAZAR_", "VERIFICATION_COURTE_BROUILLON2", "LIGNE_GO_BBIS"):
    hors_tableau = (texte.replace("La règle « choisi après lecture » et la ligne `LIBELLE-BBIS` sont retirées", "")
                    .replace("la règle « choisi après lecture » et la ligne `LIBELLE-BBIS` sont retirées", ""))   # mentions de leur retrait, permises
    if interdit in hors_tableau:
        raise SystemExit(f"reste interdit : {interdit}")
B3.write_text(texte, encoding="utf-8")
print("remplacements appliqués :", len(journal))
print("marqueurs restants :", ", ".join(restes))
print("brouillon 3 :", hashlib.sha256(texte.encode("utf-8")).hexdigest())
