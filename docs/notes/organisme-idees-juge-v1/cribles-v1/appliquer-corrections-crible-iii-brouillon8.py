"""Brouillon 8 du préenregistrement du crible (iii) : corrections de la contre-lecture du brouillon 7
(`contre-lecture-crible-iii-b7-tour1-v1.md`, tour 1 de la lecture du brouillon 7 ; 1 majeure : A1 à A3 ; 7 mineures : B1, B2
et B3, C1 à C4, D1 ; onze couples), lus dans le rapport lui-même, sans écart ; plus les couples d'en-tête (titre, puce du
brouillon 8, statut, validateur) et de la section « Contre-lecture » (entrée 7, « Tour suivant »).

Gardes : empreinte de la pièce de départ (brouillon 7) et du rapport ; nombre de couples attendu ; chaque « ancien » figure
exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; chaque « nouveau » figure dans la cible ;
la cible (et son compagnon) ne doit pas exister et n'est jamais écrasée (ouverture en mode « x ») ; le validateur
`controle_ia.prereg.problemes` est rejoué sur le texte neuf (copie temporaire) avant toute écriture de la cible et doit rendre
une liste vide ; aucun repli silencieux. Bibliothèque standard seule (le validateur est appelé par `.venv/bin/python` avec
`PYTHONPATH=src`) ; aucun appel de modèle, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-iii-brouillon8.py  (depuis n'importe quel dossier)
"""
import hashlib
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-iii-brouillon7.md")
SOURCE_SHA = "8be79b00430f06a3f74f5abe9d0985d8246036565c92220c202689d3d004a7fd"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-iii-b7-tour1-v1.md")
RAPPORT_SHA = "4803c83b98d6c8fba7a5d9b8e8a5915a65694f995fc0b68138eb197d16c9a5b3"
CIBLE = os.path.join(ICI, "crible-iii-brouillon8.md")
HEURE = "2026-11-16T15:27:22Z"


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


COUPLES = [
    # ---------- corrections exigées par le rapport (section 4), copiées à l'octet ----------
    ("A1",
     "| mondes complets obtenus + mondes non commencés < 16, **quelle qu'en soit la cause** (fournisseur, tronquage, coupure, minuterie) |",
     "| mondes complets obtenus + mondes en cours (comptés comme pouvant devenir complets) + mondes non commencés < 16, **quelle qu'en soit la cause** (fournisseur, tronquage, coupure, minuterie) ; évalué à chaque fin de monde ; à l'instant 0 : 20 |"),
    ("A2",
     "| panne d'un appel : continue |",
     "| démarrage (0 complet, 5 en cours, 15 non commencés) : continue ; panne d'un appel : continue |"),
    ("A3",
     "| 0 | une ligne d'arrêt déclenchée ; la mesure en erreur |",
     "| 0 | une ligne d'arrêt déclenchée, **sauf** la ligne « mondes complets + mondes en cours + mondes non commencés < 16 », dont l'issue est celle de l'étage 1 ; la mesure en erreur |"),
    ("B1",
     "Tout autre chiffre reste celui de ce texte, **hors** trois valeurs",
     "**III-7 se refait par une règle écrite ici** : $_D/$_S = 1 + (coût moyen d'un appel de passe 1 de Pr-2 lu à la sonde des gabarits, au prix public) / (coût moyen d'un appel de Pr-4 lu au pilote, au prix public), donné en fourchette de ± 0,05 ; sans sonde jouée, III-7 reste 1,05 à 1,25 ; aucune autre prédiction ne se refait. Tout autre chiffre reste celui de ce texte, **hors** trois valeurs"),
    ("B2",
     "| empreinte différente : texte, monde, gabarit G0, G1 ou G2, configuration, programme, module importé |",
     "| empreinte différente : texte, monde, gabarit G0, G1 ou G2, configuration, programme, module importé ; texte servi de G1 ou de G2 de plus de 53 000 octets (le pire cas de Pr-2 et celui de Pr-4 atteignent leur plafond de session à 53 976 octets) |"),
    ("B3",
     "| un octet changé dans G2 : refus nommé |",
     "| un octet changé dans G2 : refus nommé ; un texte de G2 de 53 001 octets : refus nommé |"),
    ("C1",
     "borne par monde 7 200 s (deux tours : S, H et passe 1, puis D et B)",
     "borne par monde 7 200 s (deux étapes en série : passe 1, puis D et B ; S et H courent en même temps, sans que D et B les attendent)"),
    ("C2",
     "l'ablation (B) est ici aux critères gelés (étage 5)",
     "la comparaison d'écrivains (B), nommée « ablation de la frontière » par R-2977, est ici aux critères gelés (étage 5) ; elle ne retire pas la frontière (B est écrit par Pr-2, autre espèce de frontière)"),
    ("C3",
     "brouillon 4 : 123 + 483 + 243 + 196,60 + 263).",
     "brouillon 4 : 123 + 483 + 243 + 196,60 + 263 ; avec les 7 USD de la sonde des gabarits, 1 315,60)."),
    ("C4",
     "Résumé de sa sortie : 4 à 6 composantes",
     "Résumé de sa sortie (programme et sortie à verser au dépôt, avec leurs empreintes compagnons, avant le scellement ; il en va de même du programme 1 et de sa sortie) : 4 à 6 composantes"),
    ("D1",
     "refuse la concurrence (erreurs de limite de débit à l'essai à blanc), arrêt avant tout appel et nœud de la mère (procédure neuve)",
     "refuse la concurrence (erreurs de limite de débit scriptées à l'essai à blanc, qui éprouve le lanceur et non la limite réelle du fournisseur), arrêt avant tout appel et nœud de la mère (procédure neuve) ; la concurrence réelle chez le fournisseur n'est éprouvée qu'au premier tour des files, sous la ligne « limite de débit » (risque dit au point 13 de « Choix et doutes »)"),
    # ---------- en-tête ----------
    ("E-titre",
     "loi écrite par un proposeur cher — brouillon 7 (variante « crédits de Claude au maximum »)",
     "loi écrite par un proposeur cher — brouillon 8 (variante « crédits de Claude au maximum »)"),
    ("E-puce",
     "- Commit du code d'analyse : **aucun à ce jour**.",
     "- Brouillon 8 : corrections de la contre-lecture du brouillon 7 (tour 1 de la lecture du brouillon 7,\n"
     "  `contre-lecture-crible-iii-b7-tour1-v1.md`) appliquées le " + HEURE + " (`date -u`, au scellement) par un rédacteur\n"
     "  neuf, qui n'a écrit ni les brouillons 1 à 7 ni les rapports de contre-lecture (identité dite en conversation seulement ;\n"
     "  modèle servi à relever par la mère dans les journaux des sous-agents, comme en R-2992, point 0), au moyen du programme\n"
     "  `appliquer-corrections-crible-iii-brouillon8.py` (même dossier, scellé) ; dépôt lu sur `main` (tête `64540acd`) ;\n"
     "  procédure v14 relue au commit `2d35cafa…` et [PILOTE] relu (bloc gelé) par `git show`, après un `git fetch` à refspec ;\n"
     "  rien lu de la sortie du pilote MR-2 v14 ; aucun commit, aucune poussée. Rien d'autre que les 11 couples du rapport,\n"
     "  l'en-tête (titre, cette puce, statut, validateur) et la section « Contre-lecture » (entrée 7, « Tour suivant ») ne change.\n"
     "- Commit du code d'analyse : **aucun à ce jour**."),
    ("E-statut-1",
     "**Statut.** Brouillon 7, **réécrit sur la variante « crédits de Claude au maximum »**,",
     "**Statut.** Brouillon 8 (corrections de la contre-lecture du brouillon 7, « Contre-lecture », entrée 7), **réécrit au\n"
     "brouillon 7 sur la variante « crédits de Claude au maximum »**,"),
    ("E-statut-2",
     "**la\nréécriture n'est pas encore contre-lue** : un tour sur le différentiel du brouillon 6 à ce brouillon 7 est **obligatoire** avant\ntout scellement (R-2992, point 1 ; R2) ;",
     "**la\nréécriture a été contre-lue une fois** (brouillon 7 ; 1 majeure et 7 mineures, toutes appliquées dans ce brouillon 8) : un\n"
     "tour sur le différentiel du brouillon 7 à ce brouillon 8 est **obligatoire** avant\ntout scellement (R-2992, point 1 ; R2) ;"),
    ("E-validateur",
     "aucun défaut sur ce brouillon 7 (vérifié avant son scellement comme pièce de",
     "aucun défaut sur ce brouillon 8 (vérifié avant son scellement comme pièce de"),
    # ---------- section « Contre-lecture » : entrée 7 et « Tour suivant » ----------
    ("CL-tour-suivant",
     "**Tour suivant** (obligatoire avant le scellement, R-2992, point 1 : un tour sur le différentiel du brouillon 6 à ce brouillon 7,\n"
     "qui réécrit la forme) : sous-agent neuf qui n'a écrit ni ce texte, ni les brouillons 1 à 6, ni aucun rapport de contre-lecture de\n"
     "ce crible.\n"
     "**Fichiers à lui donner explicitement** : ce texte ; le brouillon 6 (`f377e927…`) et le programme\n"
     "`appliquer-corrections-crible-iii-brouillon7.py` ; le rapport du tour 3 de la lecture du brouillon 4 (`99fb1024…`) ; les listes\n"
     "« Si la variante est retenue » des rapports des tours 1, 2 et 3 et du tour 1 de la lecture du brouillon 4, et les sections 3\n"
     "des rapports de la lecture du brouillon 4 (empreintes ci-dessus) ; les lignes R-2977 et R-2992 de `registres/decisions.md` et\n"
     "toute ligne de ce registre sur le gel de III-6 ; la ligne GO-2026-11-15-06 ; [NOTE] (`2f6a69dd…`), § 1, § 3 (iii), § 3 (v),\n"
     "§ 4 et annexe A ; [PILOTE] (`8aa33014…`), « Métrique », « Devis », bloc gelé ; [PROC-14] (`20355627…`), § 0 et § 7 ; N-045 v2\n"
     "(`c7b05e39…`) ; N-058 (`854f2724…`) ; au besoin, les pièces de la liste du tour précédent : brouillons 1 à 5, rapports des\n"
     "tours 1 à 3 et des deux premiers tours de la lecture du brouillon 4, programmes des brouillons 2 à 6,",
     "- **Contre-lecture 7** (R2, tour 1 de la lecture du brouillon 7, septième lecture du crible, première de la réécriture sur la\n"
     "  variante) — sous-agent neuf, qui n'a écrit ni ce texte, ni les brouillons 1 à 6, ni les rapports des tours précédents, ni\n"
     "  aucune pièce citée ; il déclare n'avoir lu aucun dossier jetable d'un premier contre-lecteur arrêté sans rapport (rien de\n"
     "  lui n'est repris ni lu). Texte relu :\n"
     "  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon7.md`,\n"
     "  `8be79b00430f06a3f74f5abe9d0985d8246036565c92220c202689d3d004a7fd` (égale à son compagnon) ; rapport :\n"
     "  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iii-b7-tour1-v1.md`,\n"
     "  `4803c83b98d6c8fba7a5d9b8e8a5915a65694f995fc0b68138eb197d16c9a5b3` (égale à son compagnon `.sha256`, recalculée). Verdict :\n"
     "  « corrections » (1 majeure : A1 à A3, trois couples ; 7 mineures : B1, B2 et B3, C1 à C4, D1 ; onze couples en tout) ; le\n"
     "  rapport constate que les 64 couples du programme du brouillon 7, appliqués au brouillon 6, redonnent le brouillon 7 à l'octet,\n"
     "  que les décisions de R-2977 et de R-2992 se retrouvent dans le texte, que le devis, la durée, les probabilités du minimum et\n"
     "  les empreintes se recomptent, que le validateur ne trouve aucun défaut et que la conception tient ; il recommande la\n"
     "  variante (confiance 0,65), déjà retenue par la mère (R-2992). Corrections appliquées le " + HEURE + " (`date -u`) par un\n"
     "  rédacteur neuf, qui n'a écrit ni les brouillons 1 à 7 ni les rapports de contre-lecture (identité dite en conversation\n"
     "  seulement), au moyen du programme `appliquer-corrections-crible-iii-brouillon8.py` (même dossier, scellé à côté) : les\n"
     "  11 couples sont lus dans le rapport lui-même, sans aucun écart ; chaque « ancien » figure une seule fois dans le brouillon 7\n"
     "  (vérifié par le programme). Avant l'application, le différentiel du brouillon 6 au brouillon 7 a été rejoué par programme :\n"
     "  les 64 couples de `appliquer-corrections-crible-iii-brouillon7.py`, appliqués en mémoire au brouillon 6 (chaque « ancien »\n"
     "  une seule fois), redonnent le brouillon 7 à l'octet ; la lecture du brouillon 6 n'exigeait aucune correction.\n"
     "  **Traitement**, point par point :\n"
     "  - A1 à A3 (majeure : avec cinq files, cinq mondes sont toujours en cours, et la somme « complets + non commencés » vaut 15\n"
     "    à l'instant 0, sous 16 : la ligne d'arrêt du minimum se déclenchait avant tout appel, contre son propre essai sain ; les\n"
     "    mondes en cours comptent désormais comme pouvant devenir complets, la ligne est évaluée à chaque fin de monde et vaut 20 à\n"
     "    l'instant 0 ; essai sain « démarrage : continue » ; à l'étage 0, cette ligne est exceptée et son issue est celle de\n"
     "    l'étage 1, « non concluant ») : **acceptée**, trois couples (« Liste d'arrêt » ; « Critères de lecture gelés », étage 0).\n"
     "  - B1 (règle écrite d'avance pour refaire III-7 d'après le pilote et la sonde des gabarits, fourchette de ± 0,05 ; sans\n"
     "    sonde jouée, III-7 reste 1,05 à 1,25 ; aucune autre prédiction ne se refait) : **acceptée** (« Devis », sous la table de\n"
     "    mise à jour). Reste, non visé par le rapport et sans rien changer : le statut de l'en-tête dit que la version qui fera foi\n"
     "    ne refait « que ce que la table liste » ; la règle de III-7 est écrite juste sous cette table, non dans une de ses lignes.\n"
     "  - B2 et B3 (garde de taille du texte servi de G1 et de G2 : plus de 53 000 octets, arrêt avant tout appel ; artefact de\n"
     "    53 001 octets) : **acceptée**, deux couples (« Liste d'arrêt », première ligne). Recompté sur la règle de la commande du\n"
     "    bloc gelé de [PILOTE] ((octets + 1 024) × prix d'entrée + borne × prix de sortie) : (53 976 + 1 024) × 4 + 89 000 × 20 =\n"
     "    2,00 USD pour Pr-2 et (53 976 + 1 024) × 8 + 64 000 × 40 = 3,00 USD pour Pr-4 (prix par million de jetons) : égaux à leurs\n"
     "    plafonds de session (2 et 3 USD, bloc gelé).\n"
     "  - C1 (« deux tours » se lisait comme une barrière ; deux étapes en série, passe 1 puis D et B, S et H en même temps) :\n"
     "    **acceptée** (section 0, point 9). Restent, non visés par le rapport et sans rien changer : « ordre à deux tours » (même\n"
     "    point 9, liste du code neuf) et « deux tours en série doivent tenir dans 7 200 s » (table de mise à jour, ligne de la durée\n"
     "    par monde), qui se lisent comme les deux étapes en série de C1.\n"
     "  - C2 (l'étage 5 compare deux écrivains et ne retire pas la frontière ; nom de R-2977 rappelé) : **acceptée** (« Écarts »,\n"
     "    N-045 point 3). Restent, sans rien changer : « ablation de la frontière » dans les entrées historiques de cette section\n"
     "    (mots de R-2977).\n"
     "  - C3 (enveloppe avec la sonde des gabarits : 1 315,60 USD) : **acceptée** (« Lignes de GO proposées », enveloppe).\n"
     "  - C4 (programmes et sorties de l'annexe A à verser au dépôt, avec leurs compagnons, avant le scellement, R6) : **acceptée**\n"
     "    (annexe A) ; le versement lui-même n'est pas fait par cette application (rien d'autre que le texte ne change).\n"
     "  - D1 (l'essai à blanc, à relais scriptés, éprouve le lanceur, non la limite réelle du fournisseur ; la concurrence réelle\n"
     "    n'est éprouvée qu'au premier tour des files, sous la ligne « limite de débit ») : **acceptée** (« Devis », « Durée »).\n"
     "  - **Décisions de la mère (R-2992)**, relues dans ce texte, inchangées : forme du crible, la variante « crédits de Claude au\n"
     "    maximum » (Pr-2 choisit, Pr-4 écrit, S = un appel de Pr-4 ; 128,30 USD attendus, 263 au pire à 20 mondes, dont 3 hors\n"
     "    crédits), déjà écrite au brouillon 7 ; ce que la variante change à la question de [NOTE] : dit dans « Hypothèse » (oui, un\n"
     "    peu : deux paliers de prix d'une même maison, la diversité d'espèces perdue), sans trancher ; N = 20 mondes dans tous les\n"
     "    cas : la règle « 24 si le taux de réussite par appel du pilote est sous 0,95 » de R-2977 est remplacée et n'est pas\n"
     "    rétablie (le rapport, section 6, point 8, le confirme) ; le taux du pilote reste une information (« Seuil », table de mise\n"
     "    à jour) ; mentions d'un rédacteur « lettre C » : aucune hors des entrées historiques (recherche refaite) ; remarques\n"
     "    facultatives R-1 à R-6 : reprises au brouillon 7 (entrée 6), aucune ne change un critère, inchangées.\n"
     "  - **Remarques facultatives** (section 5 du rapport) : **non appliquées** (aucune correction exigée) : libellé « sans perte\n"
     "    notable » de P2 laissé tel quel (libellé gelé, sens dit dans « Taille ») ; fourchette de la machine calculée en série, sans\n"
     "    effet sur le pire cas ; puissance de P1 donnée par la simulation avant le scellement.\n"
     "  - **Points du rapport pour la mère, ouverts** (section 6 ; aucun n'est tranché ici) : la ligne du minimum (A1 à A3,\n"
     "    corrigée ici) ; le gel de III-6, à inscrire par une ligne datée à l'heure de `registres/decisions.md` avant que le lecteur\n"
     "    neuf du pilote rende sa lecture (aucune ligne trouvée par `grep` jusqu'à R-2992) ; l'étage 5 de (iii) contre celui de (v)\n"
     "    (R-2992, point 2, a mis l'ablation de (v) hors des critères gelés ; pour (iii), R-2977 la garde aux critères gelés, et B\n"
     "    n'est plus une ablation de la frontière : gel de B à confirmer, ou passage en « rapporté sans verdict ») ; la fragilité du\n"
     "    minimum à N = 20 (0,49 de « non concluant » à p = 0,95 ; démarrage échelonné des files ou risque accepté, recommandation\n"
     "    du rapport : l'accepter) ; l'enveloppe (1 308,60 USD, 1 315,60 avec la sonde, contre 1 275) et le solde de crédits de\n"
     "    Claude (260 + 7 au pire) ; le code neuf, le calendrier (lancement visé du 21 au 24 novembre, au-delà de l'autonomie), le\n"
     "    mot et la phrase de Lazar, GO-2026-11-15-06 jusqu'au 30 novembre ; le scellement (trois valeurs processeur, table de mise\n"
     "    à jour, taux recopié, dernier tour sur le différentiel).\n"
     "  - **Décisions de R-2977 relues dans ce texte** (inchangées) : mondes séparés de ceux de (v) ; dollars principaux au prix\n"
     "    public, prix de la configuration en sensibilité (vide ici) ; ablation de la frontière aux critères gelés (étage 5) ;\n"
     "    GO-2026-11-15-06 pour l'essai, non pour l'adoption ; B sur les ensembles de D ; égalités par l'ordre des noms ; forme :\n"
     "    tranchée par R-2992 ; N : remplacé par N = 20 (R-2992). Rien du pilote MR-2 v14 n'est lu par ce texte ni par son\n"
     "    application.\n"
     "\n"
     "**Tour suivant** (obligatoire avant le scellement, R-2992, point 1 ; R2 : un tour sur le différentiel du brouillon 7 à ce\n"
     "brouillon 8) : sous-agent neuf qui n'a écrit ni ce texte, ni les brouillons 1 à 7, ni aucun rapport de contre-lecture de\n"
     "ce crible.\n"
     "**Fichiers à lui donner explicitement** : ce texte ; le brouillon 7 (`8be79b00…`) et le programme\n"
     "`appliquer-corrections-crible-iii-brouillon8.py` ; le rapport du tour 1 de la lecture du brouillon 7 (`4803c83b…`) ; les\n"
     "lignes R-2977 et R-2992 de `registres/decisions.md` et\n"
     "toute ligne de ce registre sur le gel de III-6 ; la ligne GO-2026-11-15-06 ; [NOTE] (`2f6a69dd…`), § 1, § 3 (iii), § 3 (v),\n"
     "§ 4 et annexe A ; [PILOTE] (`8aa33014…`), « Métrique », « Devis », bloc gelé ; [PROC-14] (`20355627…`), § 0 et § 7 ; N-045 v2\n"
     "(`c7b05e39…`) ; N-058 (`854f2724…`) ; au besoin, les pièces de la liste du tour précédent : brouillons 1 à 6, rapports des\n"
     "tours 1 à 3 et des trois tours de la lecture du brouillon 4, programmes des brouillons 2 à 7,"),
]
NOMBRE_ATTENDU = 17

if HEURE.startswith("@@"):
    arret("heure de scellement non inscrite")
if not os.path.isfile(os.path.join(DEPOT, "src", "controle_ia", "prereg.py")):
    arret(f"racine du dépôt introuvable : {DEPOT}")
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")
if len(COUPLES) != NOMBRE_ATTENDU or len({c[0] for c in COUPLES}) != NOMBRE_ATTENDU:
    arret("nombre de couples ou identifiants inattendus")

source = open(SOURCE, encoding="utf-8").read()
places = []
for ident, ancien, nouveau in COUPLES:
    n = source.count(ancien)
    if n != 1:
        arret(f"{ident} : « ancien » trouvé {n} fois dans la pièce de départ (une seule exigée)")
    debut = source.index(ancien)
    places.append((debut, debut + len(ancien), ident, ancien, nouveau))
places.sort()
for p, q in zip(places, places[1:]):
    if q[0] < p[1]:
        arret(f"chevauchement entre {p[2]} et {q[2]}")
morceaux, curseur = [], 0
for debut, fin, ident, ancien, nouveau in places:
    morceaux.append(source[curseur:debut])
    morceaux.append(nouveau)
    curseur = fin
morceaux.append(source[curseur:])
texte = "".join(morceaux)
for ident, ancien, nouveau in COUPLES:
    if nouveau not in texte:
        arret(f"{ident} : « nouveau » absent de la cible")

with tempfile.TemporaryDirectory() as dossier:
    essai = os.path.join(dossier, "crible-iii-brouillon8.md")
    with open(essai, "w", encoding="utf-8") as f:
        f.write(texte)
    py = os.path.join(DEPOT, ".venv", "bin", "python")
    r = subprocess.run([py, "-c", "import sys; from controle_ia.prereg import problemes; p = problemes(sys.argv[1]); "
                        "print(p); sys.exit(1 if p else 0)", essai],
                       cwd=DEPOT, env={"PYTHONPATH": os.path.join(DEPOT, "src"), "PATH": "/usr/bin:/bin"},
                       capture_output=True, text=True)
    if r.returncode != 0:
        arret("validateur : " + (r.stdout + r.stderr).strip())

with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(texte)
print(f"{len(COUPLES)} couples appliqués ; cible écrite : {CIBLE}")
print("empreinte de la cible :", sha(CIBLE))
