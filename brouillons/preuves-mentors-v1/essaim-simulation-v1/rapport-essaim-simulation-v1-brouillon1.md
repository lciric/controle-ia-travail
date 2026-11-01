# Rapport — simulation d'essaim préenregistrée (surveillance par agent contre co-élévation) — v1, brouillon 1

Date : 2026-11-01 (UTC). Auteur : Claude, sous-agent du dossier de preuves pour les mentors (`brouillons/preuves-mentors-v1/`, mot de Lazar du 2026-11-01, consigné R-1075).

## Verdict

L'instrument est prêt et testé ; le préenregistrement brouillon 1 est complet, sauf le commit cité et la contre-lecture, laissés en marqueurs pour que le validateur refuse de le sceller avant. **La simulation décisive n'a pas été lancée** ; aucune cellule de la grille décisive n'a été calculée (sa graine n'existe qu'au scellement).

- Aucun fichier existant modifié, aucun commit, aucune empreinte compagnon `.sha256` (règle de versionnement R12 respectée) ; aucun réseau.
- Ajout non demandé, facile à retirer : un bloc « corrélation entre copies » (HE6, voir plus bas). Je le recommande, parce qu'il répond à la question que le papier B posera en premier.

## Livrables (chemins et sha256 au moment de la remise)

| Pièce | Chemin |
|---|---|
| Paquet | `src/controle_ia/simulation_essaim/` : `statistiques.py`, `references.py`, `menaces.py`, `calibrage.py`, `blocs.py`, `lecture.py`, `run_essaim.py`, `__init__.py` |
| Tests | `tests/test_simulation_essaim_v1.py` (35 tests) |
| Préenregistrement | `brouillons/preuves-mentors-v1/essaim-simulation-v1/preenregistrement-essaim-simulation-v1-brouillon1.md` — `b9b1109ec4380894538114f5e977154ffd96afac4e83a0bf8a3ce6ad7c5dfdfc` |
| Grille | `brouillons/preuves-mentors-v1/essaim-simulation-v1/grille-essaim-v1-brouillon1.json` — `dacbce3006cc354f7cababaf53c16e415598838cfa0c91dccf15ec1bed6eff06` |
| Annexe des valeurs prédites | `brouillons/preuves-mentors-v1/essaim-simulation-v1/annexe-valeurs-predites-essaim-v1-brouillon1.md` — `ca4500a28673c674c2c1d60eef0c2f25e2bfe6e80efd8b01e3adfb25c55b1ae9` |
| Ce rapport | `brouillons/preuves-mentors-v1/essaim-simulation-v1/rapport-essaim-simulation-v1-brouillon1.md` |
| Explorations déclarées, générateurs, chronométrage | `brouillons/preuves-mentors-v1/essaim-simulation-v1/explorations-brouillon1/` (10 scripts, 7 sorties, `empreintes.txt` — `63c00c62edd10df4dd41a640f18230284412a6f5e5cd0e7e0019e6348e99c664`) |

## Ce que fait le code

- **Monde** : K agents × T pas, un score de moniteur par (agent, pas), tiré des lois de T0.3 (`simulation_t03.lois`) : cases indépendantes N(0, 1) en référence ; effet d'épisode commun à tout l'essaim ; corrélation entre agents d'un même pas (copies à poids partagés).
- **Menaces** :
  - (i) diffuse **entre agents** à un pas donné, multi-ensemble du pas conservé (groupe « agents dans un pas ») : rebrassage uniforme, routage des scores hauts vers un agent voyou, relais tournant entre agents ;
  - (ii) diffuse **dans le temps** pour chaque agent, multi-ensemble de l'agent conservé (groupe « temps dans un agent ») : rebrassage uniforme, synchronisation de m agents au même pas ;
  - (iii) **concentrée** (un agent, un pas, budget B) ; plus les budgets étalés entre agents d'un pas ou dans le temps d'un agent (classe « décalage » du lemme) ;
  - chaque réarrangement passe une garde qui vérifie qu'il reste dans son groupe (sinon arrêt).
- **Moniteurs** :
  - par agent : moyenne et comptage dans le temps de chaque agent, puis max entre agents (le max par agent puis entre agents est le max global) ;
  - par pas : moyenne du pas, co-élévation (nombre d'agents au-dessus de u = Φ⁻¹(0,9) au même pas, max sur les pas), co-élévation continue (somme des 3 plus hauts scores du pas) ;
  - séquentiels : e-valeur cumulée sur la co-élévation (facteurs 1 + λ(C_t − Kq), mélange sur λ ; seuil de Ville), détecteur e (redémarrage) sur la co-élévation, processus e de mélange normal lu aux frontières de pas ;
  - globaux : somme, max, comptage.
- **Invariance exacte au bit près** : chaque somme est faite sur des valeurs triées le long de l'axe que permute le groupe de la statistique ; les tests le vérifient pour chaque groupe.
- **Calibrage** :
  - seuils exacts sous la loi de référence (aléatoirisés, de taille exactement α, pour les statistiques discrètes, grâce à un uniforme de départage par essaim) ;
  - Monte-Carlo aléatoirisé ;
  - Ville ;
  - **conforme sur essaims honnêtes entiers**, départage lexicographique : taux exact 0,04995.
- **Lecture** : intervalles exacts de Clopper-Pearson de niveau 1 − 10⁻⁵ par cellule ; région exacte (somme de lois bêta-binomiales) pour le calibrage conforme ; formes closes, sans tirage, pour toutes les puissances sous budget et pour les taux de fausses alarmes hors hypothèses (quadrature de Gauss-Hermite) ; bornes inférieures exactes sous synchronisation.
- **Lanceur** : il reprend les gardes de T0.3 (préenregistrement scellé, grille citée, commit cité, code importé) et y ajoute deux règles.
  - **Graine racine** : 128 premiers bits du sha256 du préenregistrement scellé ; elle n'est connue qu'au scellement.
  - **Run décisif unique** : un seul run principal par empreinte de préenregistrement, et une seule réplication.

## Tests

- `tests/test_simulation_essaim_v1.py` : **35 tests, tous passants, 8 à 17 s selon la charge** (environ 6 s de temps processeur ; sous la limite de 2 minutes, machine partagée chargée).
  - **Cas sain** (R5) : la menace concentrée est détectée par le max, à la forme close près.
  - **Artefacts** :
    - sous la menace diffuse entre agents, chaque statistique invariante par permutation des agents d'un pas a une puissance égale à son taux de fausse alarme, à l'intervalle exact près, et la surveillance par agent la détecte ;
    - une statistique faussement invariante (injectée) est vue par la lecture, qui rend la prédiction trajectorielle contraire et demande un audit ;
    - chaque garde de la liste d'arrêt est testée sur un cas sain et sur un artefact.
  - Une chaîne complète sur mini-grille tourne dans un dépôt jetable : manifeste, blocs, lecture, scellement, refus d'un second run, réplication.
- Suite complète du dépôt : voir la dernière section.

## Durée estimée du run décisif

Mesure d'un point de chaque bloc, graine jetable, durées seules relevées, machine de 2 cœurs sous une charge de 2,6 à 3,4 :
- calibrage d'une configuration : 6 à 12 s ;
- une cellule d'attaque : 0,7 à 3,3 s ;
- une loi du bloc de validité séquentielle : 6,4 s ;
- bloc de corrélation complet : 18,5 s.

Total extrapolé : **≈ 3,5 minutes** en un seul processus, jusqu'au double sous forte charge ; une réplication complète au plus ≈ 20 minutes. Grille : 824 cellules (775 statistiques, 49 trajectorielles).

## Ce que la grille prédit, en clair

Les étiquettes HE renvoient aux hypothèses du préenregistrement (HE1 : théorème sur l'axe des agents ; HE2 : échappement de la co-élévation ; HE3 : validité séquentielle ; HE4 : menaces à budget ; HE5 : rebrassage uniforme ; HE6 : corrélation entre copies).

1. **La co-élévation n'échappe pas au théorème contre une menace qui conserve le multi-ensemble de chaque pas** (HE1). Comme toute statistique de niveau essaim, elle est fonction des multi-ensembles des pas : valeurs identiques au bit près, puissance égale au taux de fausse alarme, sans exception — sa version séquentielle en e-valeurs comprise. Contre une telle menace, seule la surveillance par agent peut voir quelque chose, et seulement si les scores hauts sont concentrés sur peu d'agents.
2. **Elle y échappe contre une menace qui conserve le multi-ensemble de chaque agent**, c'est-à-dire concentrée dans le temps mais étalée entre agents d'un même pas (HE2). Réponse exacte à « sous quelle invariance » :
   - la co-élévation est invariante sous le groupe engendré par les permutations des agents dans chaque pas et la relabellisation des pas ;
   - la synchronisation est une permutation du temps propre à chaque agent, hors de ce groupe ;
   - la surveillance par agent, invariante sous ces permutations du temps, y est exactement aveugle ;
   - la co-élévation y a des bornes inférieures exactes (0,27 à 1,00 selon m).
3. **Le budget dit qui voit quoi** (HE4, formes closes). Un budget étalé entre agents d'un pas est vu par la moyenne du pas et la co-élévation (0,85 et 0,58 à B = 12, K = 10, contre 0,10 par agent). Un budget étalé dans le temps d'un agent est vu par la surveillance par agent (0,57 contre 0,09 par pas). La somme les voit également, et faiblement (0,21). Le max ne voit que la menace concentrée. L4, non testé en T0.3, est vérifié trajectoire par trajectoire.
4. **Calibrer sur essaims entiers** (HE3) :
   - au seuil de Ville, la version séquentielle dépasse son taux sous effet d'épisode ;
   - calibrée sur essaims honnêtes entiers, elle tient 0,04995 sous toutes les lois ;
   - les seuils calibrés sur cases supposées indépendantes se trompent dans les deux sens, avec des valeurs exactes : sous corrélation entre copies (c = 0,4), la co-élévation alarme à tort dans 62 à 83 % des essaims, la moyenne du pas dans 87 à 98 %, la surveillance par agent dans 4,1 % (sous α, inégalité de Slepian).

## Constats exploratoires (déclarés, sur données jetables et tailles hors grille ; à confirmer par le run)

1. **Le relais tournant aveugle aussi la surveillance par agent** : elle tombe à ~0,01 au lieu de 0,05, parce que le relais ôte la variance du nombre de scores hauts reçus par chaque agent. Une menace diffuse entre agents, qui conserve chaque pas et se répartit également, n'est vue par aucun moniteur de scores du panneau.
2. **La version séquentielle cumulée de la co-élévation est anti-détectrice sous synchronisation** : ~0,02 au lieu de 0,05 quand tous les agents se synchronisent. La synchronisation conserve le total des comptes et le concentre sur un pas ; Σ log(1 + λ(C_t − Kq)) est Schur-concave, donc la concentration l'abaisse. Seule la lecture en maximum sur les pas échappe au théorème.
3. **L'e-valeur linéaire sur les comptes reste valide sous corrélation entre copies** (0,017 à 0,023 au seuil de Ville), le processus e sur les sommes non (0,17 à 0,32) ; ni l'une ni l'autre sous effet d'épisode.
4. **Sous corrélation entre copies, synchroniser la moitié de l'essaim fait passer la co-élévation sous son taux** (~0,01 au lieu de 0,05, seuils calibrés sur essaims corrélés entiers). Le maximum de chaque copie tombe surtout au pas où toutes co-élèvent ; le déplacer détruit cette co-élévation naturelle. La synchronisation totale reste vue (0,74). Le sens de la puissance de la co-élévation dépend donc de la structure de corrélation honnête, pas seulement de l'invariance. C'est directement une question du papier B (H3 : courbe de sécurité selon N ; H4′ : compromis entre diversification et coordination).

## Réserves

### 1. Instrument, pas activations réelles

Comme T0.3, une confirmation établira que le code, les calibrages et l'arithmétique des énoncés sont justes, et que les magnitudes informatives sont celles annoncées. Elle ne prouvera rien sur des activations réelles. L'attaquant qui réarrange ses scores est idéalisé : qu'un agent sache piloter son propre score de sonde est une question empirique (HC4, « taxe de déplacement » du papier C).

### 2. En quoi cette simulation diffère d'une vraie propagation d'idées entre agents

- **La menace est un motif dans la matrice des scores, pas une idée qui circule.** Soit un budget posé sur des cases, soit un réarrangement de scores honnêtes choisi par un adversaire omniscient dans un groupe de permutations. Rien ne passe d'un agent à l'autre : le score de l'agent j au pas t + 1 ne dépend pas de ce qu'a fait l'agent i au pas t. Il n'y a ni graphe de communication, ni transmission, ni état persistant, ni contagion.
- **Une idée qui se propage ne choisit pas son arrangement : elle suit une dynamique** (qui lit qui, qui adopte, qui oublie). Elle produit des motifs contraints par cette dynamique : un front qui avance le long des arêtes, une croissance logistique du nombre d'agents touchés, un ordre d'atteinte qui respecte le graphe. Ces motifs ne sont ni des réarrangements purs (classe C) ni des budgets libres (classe M).
- **Une propagation ne conserve en général aucun multi-ensemble** : elle ajoute de l'élévation, avec une structure spatio-temporelle. La question utile devient : quelles statistiques ont une garantie contre la famille de motifs que la dynamique peut produire ? Pas : quel groupe l'attaquant utilise-t-il ?
- **Effet de lecture absent.** Un agent qui lit un message porteur peut voir son score monter sans adopter l'idée : le moniteur lit le contenu, pas l'intention. C'est le lien avec le papier C (corruption du moniteur, « contenu = données ») ; cette simulation n'en a pas.
- **Agents échangeables.** Ici, les agents sont échangeables et, hors HE3 et HE6, indépendants. Un vrai essaim a des rôles (codeur, testeur, relecteur), une topologie, et des copies à poids partagés dont la corrélation dépend du contexte.

### 3. Ce qu'il faudrait pour simuler une propagation vraie

1. **Un graphe de communication** : complet, anneau, étoile avec un agent pivot, petit monde ; dirigé selon les rôles ; avec un calendrier de messages par pas.
2. **Un modèle de transmission** :
   - état par agent : sain, porteur, guéri ;
   - à chaque pas, un agent sain qui lit un porteur adopte avec une probabilité β (cascade indépendante), ou au-delà d'un seuil de voisins porteurs (modèle à seuil) ;
   - guérison par remise à zéro du contexte (l'hygiène de l'état persistant du programme) ;
   - une ou plusieurs graines : un agent compromis, organisme modèle à instruction cachée ou à réglage fin.
3. **Un modèle de score qui relie l'état au moniteur** : honnête N(0, 1) ; porteur décalé de δ dans la direction de la sonde ; effet de lecture ε pour un agent exposé non porteur ; éventuellement un porteur adaptatif qui module son expression pour rester sous le seuil (un réarrangement local).
4. **Des statistiques qui connaissent le graphe** :
   - co-élévation décalée le long des arêtes (l'agent j élevé au pas t + 1 après son voisin i au pas t) ;
   - balayage spatio-temporel sur des boules du graphe ;
   - détecteur de croissance du nombre d'agents élevés : somme cumulée contre une alternative de croissance exponentielle ;
   - dates de rupture par agent, puis test que leur ordre respecte les arêtes.
5. **La transposition du théorème, à écrire d'abord.** L'attaquant ne peut se cacher que derrière les permutations qui conservent la loi honnête *et* la structure du graphe : les automorphismes du graphe, combinés à des permutations du temps compatibles avec la causalité.
   - Sur un graphe complet (tous parlent à tous), ce groupe contient toutes les permutations des agents : la propagation n'a pas de signature spatiale, seulement sa courbe de croissance.
   - Sur un graphe clairsemé, l'ordre d'atteinte le long des arêtes est une signature que les statistiques invariantes par permutation des agents ne voient pas.

   C'est une extension théorique nette, à écrire dans la note mathématique (proposition, puis contre-vérification) avant toute simulation.
6. **Une version synthétique**, sur le même instrument. Il y a des formes closes quand le graphe est simple : temps d'atteinte d'une cascade sur un anneau, taille finale d'une épidémie sur graphe complet. On y étudie la puissance de chaque famille de moniteurs selon β, δ, ε et la topologie.
7. **Puis une version sur modèle réel** : K copies de Llama-3.1-8B-Instruct à poids partagés dans un pipeline de rôles (environnement (b) du programme), un agent graine porteur, de vrais messages, des scores de sondes par (agent, pas), une vérité terrain d'adoption par étiquette comportementale. Prérequis de mesure : que la sonde distingue l'adoption de la simple lecture, par une validation du type de T0.4.
8. **Coût.** La version synthétique est du calcul sur processeur (routine). La version réelle demande K × T × épisodes passes avant avec extraction d'activations : devis, puis feu vert de Lazar (dépense).

### 4. Prédictions informées par l'exploration

Quatre prédictions ont été choisies **après** des explorations sur données jetables, à des tailles hors grille. Ce sont : le relais sous la surveillance par agent, la version séquentielle sous synchronisation, le dépassement de α au seuil de Ville, et la corrélation entre copies. Elles sont étiquetées [exploratoire vu] et leurs règles de sélection sont écrites. Leur confirmation dira que l'effet se reproduit à graine neuve, pas qu'il était prédit indépendamment.

### 5. Autres limites

- Une seule loi de référence (gaussienne, cases indépendantes) ; q = 0,1, grille de λ, co-élévation continue à 3 et α uniques.
- Corrélation entre copies seulement échangeable (équicorrélation). Pas de dépendance temporelle, pas de queues lourdes, pas d'agents hétérogènes (le « groupe compte » de T0.3 n'est pas repris sur l'axe des agents).
- E-valeur linéaire seulement. Une e-valeur convexe (rapport de vraisemblance sur les comptes) réagirait à la concentration, mais perd sa validité sous surdispersion : ce compromis mérite son propre préenregistrement (v2).
- Comparaisons multiples : au plus ≈ 0,8 % de fausse contrariété pour le run (borne de l'union), traitées par la règle de réplication de T0.3.

## Reste à faire (session principale)

1. Committer le paquet, les tests et le brouillon.
2. Faire contre-lire par un sous-agent neuf (règle R2 : un sous-agent qui n'a rien écrit du dossier). Fichiers à lui donner : préenregistrement, grille, annexe, `src/controle_ia/simulation_essaim/`, tests, note mathématique v3, préenregistrement et code de T0.3, ce rapport.
3. Traiter ses remarques. Copier la grille sans changement sous `prereg/essaim-grille-v1.json` et la sceller. Remplacer les deux marqueurs (commit cité, contre-lecture), sceller sous `prereg/essaim-simulation-v1.md`, committer.
4. Lancer la commande unique, depuis la racine du dépôt :
   `PYTHONPATH=src python -m controle_ia.simulation_essaim.run_essaim --prereg prereg/essaim-simulation-v1.md --grille prereg/essaim-grille-v1.json`
5. Deux contraintes pratiques du lanceur (gardes reprises de T0.3), à cause des sessions parallèles :
   - la garde du commit cité compare **tout** `src/` et `tests/` entre ce commit et HEAD. Un commit d'une autre session sur ces dossiers, entre le scellement et le run, arrête le run. Lancer juste après le scellement ;
   - le manifeste exige un **arbre de travail propre**, fichiers non suivis compris ; or des fichiers non suivis d'autres sessions sont présents au moment de cette remise. Il faut soit tout committer, soit lancer depuis un clone propre au commit de scellement, puis y committer et pousser `runs/` et `diag/`.

Après tout changement de la grille ou du code, régénérer la grille et l'annexe par `generer_grille.py` et `annexe.py` (dossier `explorations-brouillon1/`, qui contient aussi les scripts et sorties des explorations déclarées, avec leurs empreintes dans `empreintes.txt`, sha256 `63c00c62edd10df4dd41a640f18230284412a6f5e5cd0e7e0019e6348e99c664`), puis mettre à jour les empreintes citées par le préenregistrement.

## Suite complète des tests du dépôt

- Tests du paquet et des modules dont il dépend (`test_simulation_essaim_v1`, `test_simulation_t03`, `test_manifeste`, `test_prereg`, `test_scellement`, `test_agregateurs`) : **135 passants sur 135**, en 64 s sous une charge de 4 à 8 sur 2 cœurs.
- Suite complète (955 tests collectés) : arrêtée par moi à 449 tests exécutés, faute de pouvoir finir sous sa limite de 25 minutes sur la machine chargée par les autres sessions. Résultat partiel : 445 passants, 4 échecs, **tous hors de ce paquet** :
  - 3 dans `tests/test_corpus_arxiv.py` : module `pypandoc` absent de l'environnement ;
  - 1 dans `tests/test_analyse_blanche_noire_v1.py`, fichier non suivi d'une autre session, en cours d'écriture ; relancé ensuite, il passe (12 sur 12).
- Cette tâche n'a modifié aucun fichier existant (vérifié par `git status` et `git diff`) : l'issue du reste de la suite ne dépend pas d'elle.
