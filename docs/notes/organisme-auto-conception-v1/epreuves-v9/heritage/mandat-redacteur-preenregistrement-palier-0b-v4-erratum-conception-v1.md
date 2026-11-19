# Mandat du rédacteur — épreuve sur l'héritage, préenregistrement du palier 0b, version 4 (erratum de conception) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 22:50Z, sur GO-2026-11-19-84 (main, commit `45653e962`, mot de Lazar vers 22:42Z : « go reprise (a) »).

## Ce que tu fais

Le développeur du code du palier 0b s'est arrêté au premier refus d'outil, après avoir trouvé que le texte, à la lettre, ne peut pas être codé tel quel sur cinq points. Son travail inachevé est versé : `heritage/palier-0b/code-v1-inacheve-arrete-refus-outil-20261119/` (LISEZ-MOI `d28759a5…`, inventaire complet, code, essais, outils de diagnostic sous `outils-dev/`). Tu écris la **version 4** du préenregistrement (`preenregistrement-heritage-palier-0b-etage-processeur-v4.md`), à partir de la version 3 (`a4535a67…`, intacte, R12), qui tranche ces cinq points **par écrit, avant tout tirage** :

1. **Marges de B1** : tirer des lois au hasard et rejeter des mondes entiers ne passe presque jamais (0 source sur 41 à la force 1,5 ; 1 sur 41 à la force 4), parce qu'une loi dépendante ne diffère de chacune de ses mères que sur une moitié, et une loi fausse de sa loi vraie aussi. Le développeur a écrit un générateur constructif (sous-lois séparées par sous-population, chaque loi tirée par rejet une à une, marge de construction 0,30, audit gardé à 0,25), qui change la distribution des lois. Tranche : le générateur constructif écrit au texte (avec ce qu'il change à la distribution, et comment l'audit le contrôle), ou des marges changées, ou autre chose ; motive.
2. **Forme unique des lois** : sans une seule forme (`par_sous_population`) pour toutes les lois, l'audit de présentation échoue par construction, les lois dépendantes étant reconnaissables à leur forme. Écris-le.
3. **Le lecteur ne compose pas ses propres entrées dans la course source** : à la lettre, il le ferait, et l'ensemble exclu devient non vide (4 lois du monde final exclues), ce qui efface l'effet planté ; la garde 13 l'a vu. Écris la règle.
4. **M12 et l'accord des deux couches** : à la lettre de M12, avec une seule fréquence pour les lois non plantées (environ 0,09, regroupée), les deux couches ne s'accordent pas (bras 3 : 7,5 contre 4,25) et S8 (ii) arrêterait le run. Tranche entre la lettre de M12 et des fréquences stratifiées par origine (recherche de base, composition, copie : `frequences_gelees_par_origine` dans `mecanique.py` du dossier versé), ou une autre voie ; motive ; dis ce que cela change à la garde d'équivalence.
5. **Double balisage de l'énoncé** servi à l'expérimentateur : l'étage de l'organisme sert déjà le préenregistrement court entre balises de donnée (`a_blanc_v59` l. 62, `tests_de_mort_v2` l. 334) ; le développeur a balisé la description une seconde fois. Tranche.

Les **autres silences comblés** par le développeur (LISEZ-MOI et rapport de fin) : écris-les au texte s'ils touchent ce qui est jugé ou lu, sinon liste-les comme acceptés. Porte aussi l'accord « motivée » à la réserve 14 (relecture `43b802ba…`).

Pour chaque point : ce que le texte disait, ce qu'il dit, pourquoi, et si cela touche une hypothèse, un critère, un seuil ou une valeur gelée. **Aucun choix ne s'appuie sur un chiffre d'une course décisive** (il n'y en a aucune) ; les chiffres de diagnostic du développeur sont sur des graines « essai » et se citent comme tels. Si un point demande de changer un critère ou un seuil, écris-le comme écart déclaré et dis s'il revient à Lazar.

## Ce que tu lis

`CLAUDE.md` ; la version 3 et sa relecture (`43b802ba…`), la vérification v2 (`9d18eab3…`), la contre-lecture v1 (`127aa59f…`) ; le dossier versé du développeur, en lecture (LISEZ-MOI, code, `outils-dev/`) ; le plan v5 (§ 5 à § 8) ; le rapport du palier 0a ; sur main, GO-2026-11-19-71 à -89. Vérifie chaque empreinte avant de citer.

## Ce que tu rends

Dans ton bloc-notes seulement : la version 4, `differentiel-preenregistrement-palier-0b-v3-v4.diff`, `rapport-redacteur-palier-0b-v4-v1.md`. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Aucun tirage, aucun lancement du code versé. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. **Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur (`python3 -c`, `python3 -`) : écris tout programme dans un fichier de ton bloc-notes et lance-le par son chemin.** Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande. Au premier refus d'un outil : arrête-toi et dis-le.
