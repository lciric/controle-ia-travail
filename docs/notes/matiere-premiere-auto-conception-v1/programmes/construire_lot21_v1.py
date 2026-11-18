#!/usr/bin/env python3
"""Construit lots/lot-21.json : relevé des indices 600 à 629 de la table fusionnée,
d'après l'entrée de la table seulement (aucune lecture approfondie ouverte : cloisonnement).
Corrections de la contre-lecture appliquées d'emblée : profondeur unifiée, familles à l'écriture
normalisée, mécanismes suggérés par le titre marqués, statut donné aux entrées sans mécanisme,
empreintes sur chaque source, avertissement de lecture au niveau de l'entrée.
Usage : python programmes/construire_lot21_v1.py   (depuis docs/notes/matiere-premiere-auto-conception-v1)"""
import hashlib, json, re, sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
TABLE = "docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json"
ADV = "docs/notes/veille-exploration-idees-v1/recherche-adverse-v1.md"
GRISE = "docs/notes/veille-exploration-idees-v1/recherche-litterature-grise-v1.md"

def sha(chemin):
    return hashlib.sha256((RACINE / chemin).read_bytes()).hexdigest()

table = json.loads((RACINE / TABLE).read_text(encoding="utf-8"))["travaux"]
H = {TABLE: sha(TABLE), ADV: sha(ADV), GRISE: sha(GRISE)}

def source(i):
    lignes = []
    for s in table[i]["sources"]:
        nom, n = s.split(":")
        chemin = f"docs/notes/veille-exploration-idees-v1/{nom}"
        if chemin not in H:
            H[chemin] = sha(chemin)
        lignes.append(f"{chemin}:{n} (empreinte {H[chemin]})")
    return (f"{TABLE} (empreinte {H[TABLE]}), travaux[{i}] ; lignes de la veille : " + ", ".join(lignes))

AVERT = ("entrée de la table lue par la veille (résumé, page ou titre selon le cas), non rouverte pour ce relevé ; "
         "affirmations des auteurs d'après la notice, non opposables (R7)")
NOTE_LECTURE = {
    605: "une lecture approfondie existe au dépôt (lecture 10 de la veille), non ouverte pour ce relevé (cloisonnement) ; relevé d'après l'entrée de la table seulement",
    612: "une lecture approfondie existe au dépôt (lecture 11 de la veille), non ouverte pour ce relevé (cloisonnement) ; relevé d'après l'entrée de la table seulement",
    625: "une lecture approfondie existe au dépôt (lecture 06 de la veille), non ouverte pour ce relevé (cloisonnement) ; relevé d'après l'entrée de la table seulement",
}

def M(fam, txt, ep, titre=False):
    return dict(famille=fam, mecanisme_en_une_phrase=txt, eprouve_contre_le_reel=ep, suggere_par_le_titre=titre)

NS = " (d'après la notice de la table ; non opposable)"
MEC = {
600: [M("mémoire", "Les artefacts qu'une instance tire de son expérience sont hérités par les instances suivantes, dans un cadre contrôlé" + NS + ".", "inconnu"),
      M("épreuve", "Gain, généralisation et coût d'apprentissage mesurés à chaque point de contrôle, sur des interactions tenues à l'écart" + NS + ".", "inconnu")],
601: [M("auto-conception", "Banc d'auto-amélioration récursive d'agents de pointe (vision et robotique) avec un exécuteur et un améliorateur distincts, à budget fixe" + NS + ".", "inconnu"),
      M("sélection", "Une solution n'est gardée que si elle gagne sur une validation tenue à l'écart" + NS + ".", "inconnu")],
602: [M("épreuve", "Environnement qui sépare lots d'entraînement, validation figée et transfert tenu à l'écart (dans et hors distribution), avec diagnostics de rejouement et de coût, pour évaluer les mises à jour de harnais d'agents auto-évolutifs" + NS + ".", "inconnu")],
603: [M("épreuve", "Banc d'auto-évolution par transfert de « capacités » sur quatre domaines, partage 528 / 267 entre entraînement et test ; selon la notice, les méthodes automatiques restent fragiles et un transfert négatif est observé (affirmation des auteurs, non opposable).", "oui, affirmé")],
604: [M("auto-conception", "Évolution de harnais sous contraintes globales (changements indépendants de la tâche), retour proactif et optimisation par composante, contre le surajustement aux tâches d'évolution" + NS + ".", "inconnu")],
605: [M("épreuve", "Montre qu'un proposeur peut produire un harnais dont le gain dépend d'un raccourci du banc entier ; selon la ligne de la veille, tenir des tâches à l'écart ne suffit pas quand le protocole du banc reste fixe, un raccourci commun survivant aux tâches fraîches du même générateur (affirmation des auteurs, non opposable).", "oui, affirmé"),
      M("auto-conception", "Recherche de harnais guidée par contrefactuels, pour s'écarter des raccourcis propres à une tâche" + NS + ".", "inconnu")],
606: [M("épreuve", "Une recette d'évolution fixe est relancée à travers langages et modèles pour séparer ce qui se transfère de ce qui est propre au banc (adaptation au banc, savoir du langage ou compensation du modèle)" + NS + ".", "inconnu")],
607: [M("auto-conception", "Chaque candidat vient d'un agent complet en bac à sable ; le harnais est un génome éditable seulement à travers une porte à contrôles tenus à l'écart et de coût" + NS + ".", "inconnu"),
      M("sélection", "Les proposeurs ne voient qu'un score public ; une part privée décide (d'après la ligne de la veille sur la notice ; non opposable).", "inconnu")],
608: [M("sélection", "Remplace « évaluer puis sélectionner » par un signal sans évaluation aval : sélection de lignées sans exécuter les agents sur les tâches aval" + NS + ".", "inconnu"),
      M("coût", "Vise le coût d'évaluation et le surajustement à une distribution fixe en supprimant l'exécution aval" + NS + ".", "inconnu")],
609: [M("mémoire", "Un étage de mémoire persistante dans une architecture à trois étages n'apporte aucun changement de précision détectable sur huit paires de jeux ; selon la notice, des gains apparents venaient d'erreurs de montage (des ablations publiées avaient deux bras sans mémoire) (affirmation des auteurs, non opposable).", "oui, affirmé")],
610: [M("mémoire", "Les agents versent des enseignements fondés sur preuves dans une base partagée, ensuite distillée ; gain sans changement de l'agent, les agents restant génériques et jetables (affirmation des auteurs d'après la notice ; non opposable).", "oui, affirmé")],
611: [M("exploration", "Équipe décentralisée d'agents qui s'auto-organisent autour d'hypothèses, avec exploration parallèle" + NS + ".", "inconnu"),
      M("mémoire", "État expérimental partagé entre les agents, qui garde la connaissance des directions ratées" + NS + ".", "inconnu")],
612: [M("exploration", "23 modèles de onze familles, cinq tâches, plus de 5 500 exécutions : selon la notice, l'hypothèse « la diversité est le moteur » est rejetée sur chaque axe ; la diversité cognitive (personas, température, identité du modèle) n'explique pas les gains du débat (affirmation des auteurs, non opposable).", "oui, affirmé"),
      M("épreuve", "Témoin du débat entre agents : un vote majoritaire à budget apparié (affirmation des auteurs d'après la ligne de la veille ; non opposable).", "oui, affirmé")],
613: [M("coût", "Loi à deux paramètres pour la taille effective d'une équipe d'agents, ajustée sur 44 cellules modèle × tâche × condition ; compter les agents confond coût et preuve indépendante (affirmation des auteurs d'après la notice ; non opposable).", "oui, affirmé")],
614: [M("exploration", "Échantillonnage verbalisé : faire énoncer au modèle plusieurs réponses avec leurs probabilités pour sortir de l'effondrement de mode et retrouver de la diversité (travail antérieur et fondateur de la veille ; mécanisme d'après la notice, non opposable).", "inconnu")],
615: [M("exploration", "Collecte de chemins de recherche divers et affinage d'agents locaux de minage de facteurs pour explorer plus large, contre l'« effondrement du chemin de recherche »" + NS + ".", "inconnu")],
616: [M("sélection", "La lignée conditionne la variation proposée par le modèle et l'allocation de la recherche (contrôle de la recherche au niveau de la lignée)" + NS + ".", "inconnu"),
      M("mémoire", "L'expérience est distillée par lignée" + NS + ".", "inconnu")],
617: [M("auto-conception", "Croise composition de l'équipe et interdépendance sur trois mécanismes d'évolution (AGORA) ; selon le résumé, l'évolution seule aide rarement et le bon cadre social dépasse un agent fort évolué seul de jusqu'à 25 points en déplaçant l'autorité vers le membre le plus capable (affirmation des auteurs, non opposable).", "oui, affirmé")],
618: [M("auto-conception", "Optimisation conjointe des consignes et de l'affectation des modèles aux agents d'un système hétérogène" + NS + ".", "inconnu"),
      M("coût", "Un modèle par rôle : « chaque agent n'a pas besoin du modèle le plus fort » ; l'optimisation de consignes seule laisse hors de la recherche les besoins par rôle et leur coût d'inférence" + NS + ".", "inconnu")],
619: [M("exploration", "Les modèles sont caractérisés par leurs traces de raisonnement et regroupés ; on choisit des représentants par grappe de comportement, parce qu'augmenter la taille de la foule ne garantit pas la diversité" + NS + ".", "inconnu")],
620: [M("épreuve", "Plaidoyer pour des problèmes résistants à la contamination et des familles de tâches extensibles ; esquisse la construction de problèmes inédits (analyse sans mesure ; travail antérieur à la fenêtre de la veille ; non opposable).", "non")],
621: [M("épreuve", "L'échelle : un classement qui ne révèle un score que s'il bat nettement le précédent, contre le surajustement adaptatif (travail fondateur de 2015 ; la décision N-049 le cite « à vérifier » ; mécanisme d'après la notice, non opposable).", "inconnu")],
623: [M("exploration", "Un agent à modèle de langue propose 280 signaux comptables en sept générations (selon la copie de conférence, p. 1 et 28 ; non opposable).", "oui, mesuré"),
      M("épreuve", "38 signaux survivent aux courses puis subissent des corrections de multiplicité (Bonferroni, Holm, BHY) sur 365 signaux et des tests de recouvrement par facteurs ; la chaîne d'évaluation est fixe et extérieure à l'agent (selon la copie de conférence, p. 28 et 49 ; non opposable).", "oui, mesuré"),
      M("originalité", "Test de nouveauté contre les lois publiées : régression conditionnelle aux 10 anomalies les plus corrélées parmi 209 ; 9 signaux sur 34 gardent une statistique t de valeur absolue supérieure à 1,96 (selon la copie de conférence, p. 49 et 51 ; le test vient après la découverte ; non opposable).", "oui, mesuré")],
624: [M("jugement", "Procédures à e-valeurs qui acceptent comme poids les évaluations d'hypothèses faites par un modèle (e-BH), avec analyse de la puissance et du taux de fausses découvertes sous contamination du modèle par les données (page de la conférence ; affirmation des auteurs, non opposable).", "oui, affirmé")],
625: [M("auto-conception", "Un méta-agent journalise parent, modification et enfant sur des tâches appariées, fusionne les preuves entre environnements et met à jour sa politique d'amélioration ; gains variables selon la tâche (page de la conférence ; affirmation des auteurs, non opposable).", "oui, affirmé"),
      M("mémoire", "Le journal parent-modification-enfant, fusionné entre environnements, est la mémoire de la politique d'amélioration (page de la conférence ; non opposable).", "inconnu"),
      M("épreuve", "Un améliorateur partagé aux poids figés apprend des stratégies réutilisables ; comparaison améliorateur entraîné contre non entraîné sur des viviers tenus à l'écart, à budget de recherche fixe (d'après la ligne de la veille sur la notice ; non opposable).", "inconnu")],
626: [M("épreuve", "Cinq mondes virtuels (chimie, écologie, génétique, physique, inférence causale) à règles cachées fixées par les auteurs, détails retenus ; un harnais simple cherche les lois ; selon le billet, les agents exploitent tout canal d'information laissé visible (page lue par résumé automatique ; mesure sans données publiées ; non opposable).", "oui, affirmé"),
      M("mémoire", "Selon le billet, le code et la mémoire n'améliorent pas les scores de façon fiable ; la mémoire entre exécutions est limitée à la stratégie générale, les valeurs exactes étant filtrées (page lue par résumé automatique ; non opposable).", "oui, affirmé")],
627: [M("épreuve", "Raccourcis exploitables plantés dans des tâches tabulaires synthétiques pour dire si un gain rapporté est réel ; l'écart entre score public et score tenu à l'écart sert de vérité sur le gain (d'après le titre et la page de recherche seulement ; non lu).", "inconnu", True)],
628: [M("auto-conception", "Agents qui méta-évoluent pour améliorer d'autres agents entre tâches (d'après le titre seul ; soumission anonyme ; non lu).", "inconnu", True)],
629: [M("exploration", "Évolution de programmes guidée par modèles (descriptions du dépôt de code seulement ; non opposable).", "inconnu"),
      M("sélection", "Archive évolutive et sélection de parents dans cette archive (descriptions du dépôt de code seulement ; non opposable).", "inconnu")],
}
PRECIS = {"page ou résumé": "résumé ou page lus par la veille, d'après la table ; " + AVERT,
          "notice seule": "titre (et description) seuls lus par la veille, d'après la table ; " + AVERT}
EXCLUES = {622: "relève, selon le champ « touche » de la table, de la famille cloisonnée « attaque de Goodhart du juge, évasion des juges » (manipulation de relecteurs par modèle) : aucun contenu relevé"}

lot = []
for i in range(600, 630):
    t = table[i]
    lu = t["lu"].split(" (")[0]
    prof = "notice seule" if lu == "titre seul" else "page ou résumé"
    e = dict(indice=i, titre=t["titre"], adresse=t["adresse"], date=t["date"], nature=t["nature"],
             profondeur_de_lecture=prof, precision_de_lecture=PRECIS[prof],
             mesure_selon_la_table=t["mesure"])
    if i in NOTE_LECTURE:
        e["note_de_profondeur"] = NOTE_LECTURE[i]
    if i in EXCLUES:
        e["statut"] = "exclue"
        e["motif_exclusion"] = EXCLUES[i]
        e["chemin"] = source(i)
        e["mecanismes"] = []
    else:
        ms = []
        for m in MEC[i]:
            m = dict(m)
            m["source_dans_le_depot"] = source(i)
            ms.append(m)
        e["mecanismes"] = ms
    lot.append(e)
sortie = Path(sys.argv[1] if len(sys.argv) > 1 else "lots/lot-21.json")
sortie.write_text(json.dumps(lot, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(lot), "entrées,", sum(len(e["mecanismes"]) for e in lot), "mécanismes ->", sortie)
