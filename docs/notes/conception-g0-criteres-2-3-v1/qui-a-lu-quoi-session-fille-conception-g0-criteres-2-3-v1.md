# Liste « qui a lu quoi » — session fille de conception des pièces de la porte G0 (critères 2 et 3)

Pièce de classe C (registre de travail). Écrite avant toute lecture, complétée au fil des lectures, close à la remise.

## Inscription (faite avant toute lecture)

- Session inscrite : `session_01Qi7Gr4GahKn8qRTN5FTWv3`, fille de la session mère `session_01Qi7Gr3Ggccg85kjmP654WC`.
- Branche : `conception/g0-criteres-2-3-v1`, partie du commit `4226039463af995d82bebb274ab405855ca3240f` de `main`.
- Date et heure de l'inscription : 2026-11-24, 10:00 UTC.
- Rôle : conception, sans exécution ni scellement, de deux pièces de classe A pour la porte de sortie de la phase 0 :
  1. le préenregistrement de la mesure de dose-réponse de l'organisme à consigne cachée (critère 2 de la porte), avec son devis ;
  2. le texte qui désigne la course qui rejugera le critère 3 de la porte (sondes), avec ses doses admissibles et son contrôle écrit d'avance.
- Modèle et effort : ceux que fixe le mandat de la mère ; le relevé de la session (modèle configuré et modèle servi) est transmis à la mère dans le compte rendu, qui le consigne au registre.

## Engagement de cloisonnement

Cette session ne lit, ni directement ni par un sous-agent : aucun score, aucun verdict, aucune sortie de course, aucun coffre, aucune consigne privée d'un organisme déjà formé. Elle ne conçoit aucun moniteur ni aucune sonde. Elle conçoit à partir des textes qui font foi : brief v2, programme v2, décisions (N-054, N-056, N-062, N-063 v2 en premier lieu), préenregistrements scellés des tâches T0.6 et T0.7, devis et manifestes (pour les réglages seulement).

Conséquence sur la routine de reprise (R14) : les étapes sans lecture de résultat sont faites (empreintes de lancement, vérification de l'arbre, tests) ; `registres/etat.md` et les passations ne sont pas lus tant qu'il n'est pas établi qu'ils ne portent ni score ni verdict ; l'inventaire et l'arrêt des instances de calcul restent à la mère, qui seule sait quelles courses tournent.

Toute exposition accidentelle à un contenu interdit est déclarée ici, à la ligne, avec le chemin, l'heure et ce qui a été vu.

## Déjà en contexte au moment de l'inscription

| Pièce | Comment | Nature |
|---|---|---|
| `CLAUDE.md` (consignes permanentes) | injecté au lancement de la session | texte qui fait foi |
| Mandat de la mère (message de création de la session) | reçu au lancement | mandat |
| Noms des fichiers de la racine, des branches distantes `conception/*` et des fichiers dont le nom évoque la liste « qui a lu quoi » | listés par nom, sans ouverture | noms seulement |

## Journal des lectures

Chaque ligne : heure UTC, chemin, étendue lue, raison. Les empreintes des pièces dont dépendent les livrables sont reportées dans les livrables eux-mêmes.

| Heure UTC | Chemin | Étendue | Raison |
|---|---|---|---|
| 10:01 | `docs/sha256sums-lancement-v2.txt` ; sortie de `controle_ia.scellement verifier-arbre` | contrôle ; noms de fichiers en défaut seulement | routine de reprise, étape 1 |
| 10:03 | suite des tests (`pytest`) | résumé seul : 138 erreurs de collecte par dépendances lourdes absentes du conteneur (torch et autres) | routine de reprise, étape 5 ; non jouable ici, sans objet pour des pièces de texte |
| 10:04 | `docs/brief-claude-code-programme-complet-v2.md` | l. 1-250 et 340-405 | texte qui fait foi |
| 10:05 | `docs/programme-controle-ia-v2.md` | entier | texte qui fait foi |
| 10:07 | `docs/decisions/decision-N-063-v2.md`, `decision-N-063-v1.md`, `decision-N-062-v1.md` | entiers | décisions nommées par le mandat |
| 10:08 | `prereg/T0.6-organismes-v0-v1.md` (scellé) | l. 1-140 (en-tête), 320-361, 373-614, 635-709, 763-818 ; **non lues** : 141-319, 362-372 (« Ce que les auteurs savaient », course exploratoire), 615-634 (« Puissance »), 710-762, 819-903 | préenregistrement scellé nommé par le mandat |
| 10:12 | `docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md`, `proposition-P-009-T0.6-organismes-v1.md` | entiers | définition de la dose et du mode « coût », citées par le texte scellé de T0.6 |
| 10:14 | `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` ; `docs/notes/dossier-entretien-2026-12-01-v1/instruction-b6-versant-honnete-jumeau-v1.md` | l. 10-30 ; deux lignes rendues par une recherche (l. 40 et 65) | localiser la banque initiale de 96 tâches |
| 10:15 | `donnees/20261007-082440-t05-extraction/taches-evaluation.json`, `taches-entrainement.json` | structure, comptes, trois identifiants ; aucun contenu de tâche | banque initiale, pour l'exclusion |
| 10:18 | `src/controle_ia/environnements/propositions.py`, `t06/cout.py` | entiers | mécanisme de la consigne et de la note ; lecteur du coût |
| 10:19 | `src/controle_ia/premier_test_ia/conditions.py` | relevé de structure par recherche, puis l. 1-26 et 44-84 | chargement des textes privés ; **exposition déclarée ci-dessous** (l. 35-37) |
| 10:20 | `prereg/P3-premier-test-i-a-v1.md` (scellé) | l. 160-182 | définition de la statistique de tâche du coût |
| 10:21 | `prereg/T0.6-organismes-config-7b-v1.json` | entier | réglages seulement |
| 10:22 | `prereg/T0.7-sondes-v0-v1.md` (scellé) | plan des titres ; l. 1009-1064, 1065-1157, 1256-1313, 1802-1943 | préenregistrement scellé nommé par le mandat : lecture du critère 3 |
| 10:25 | `prereg/T0.8-base-A-mots-et-cout-v1.md` (scellé) | l. 18-27 et 36-142 ; **non lues** : 28-35 (« Ce que les auteurs savaient ») | critère propre de la base « mots et coût » |
| 10:27 | `docs/procedures/T0.5-selection-papiers-v1.md` ; `T0.5-extraction-v1.md` ; `diag/20261006-134235-t05-corpus/tirage.json`, `corpus.json`, `candidats.json` | entier ; l. 48-147 ; structure, comptes, résumé des motifs d'exclusion | tirage des tâches hors des 96 |
| 10:28 | `docs/decisions/decision-N-054-v1.md`, `decision-N-056-v1.md` ; `prereg/gabarit-preregistrement-v1.md` ; `src/controle_ia/prereg.py`, `scellement.py` (l. 1-60), `manifeste.py` (l. 1-57), `t06/lecture.py` (l. 1-133), `premier_test_ia/statistiques.py` (l. 28-79) | entiers ou plages dites | décisions nommées par le mandat ; gabarit ; fonctions reprises |
| 10:25 | `registres/rappels.md` | entier | rappels datés (consignes permanentes) |
| 10:30 | `registres/scellements-v1.md` | noms de clés seulement, par recherche | nommer les lignes de registre sans collision |
| divers | noms de fichiers et de branches (dont `idees/questions-directeur-2026-11-24-v1`, `lecture/synthese-verdicts-pour-lazar-01qi7-v1`, `donnees/t05-banque-complete-v1`, `calcul/t06-confirmation-7b-v1`, `verdict/…`) ; sujets de cinq commits de `main` | noms et sujets seulement ; **aucun contenu ouvert** | chercher la pièce de choix (dans un coffre : non lue) |
| 10:06 à 10:31 | trois messages de la mère | entiers | conditions de la pièce de choix (séparation des banques) ; adaptateurs non attestés ; trois exigences de Lazar et nœud à deux options |
| 10:35 à 11:20 | calculs de puissance de l'auteur (scripts v1 à v4 du dossier des brouillons), sur les seuls nombres des expositions déclarées ci-dessous ; aucune donnée de course | sorties entières | planification ; jamais une sélection |
| 10:50 à 11:10 | rapport de la contre-lecture 1 (`brouillons/g0-criteres-2-3-v1/contre-lecture-1-des-brouillons-1-v2.md`) | entier | corrections des brouillons 1 |
| 11:20 | `prereg/T0.6-organismes-config-7b-v1.json`, l. 70-90 ; clés `CODE-MOTS-ET-COUT-T06` des textes scellés de T0.6 et de T0.7 et du registre des scellements | doses de l'adaptateur ; noms de clés seulement, sans le texte des lignes | clause du lancement de l'organisme à adaptateur ; ligne de registre citée |
| 11:30 | `registres/rappels.md` ; noms des fichiers de `docs/notes/veille-organismes-ideation-v2/` qui portent la note d'entretien et la lecture des trois sources | entier ; noms seulement | rappel daté du 24 novembre |
| 11:36 | quatrième message de la mère | entier | deux points de conception venus du protocole de demande approfondie : formulations fixées avant toute génération, sans essai pilote lu par l'oracle ; un seul témoin ne suffit pas (fait de littérature relayé, non vérifié par cette session) |
| 11:40 | `docs/brief-claude-code-programme-complet-v2.md`, l. 160-173 ; `src/controle_ia/premier_test_ia/conditions.py`, l. 1-26 et 44-84 (relues) | plages dites | test de validité des sondes ; chargement des trois conditions instruites du premier test |
| 11:45 | rapport de la vérification 1 (`brouillons/g0-criteres-2-3-v1/verification-1-des-brouillons-2-v1.md`) et sa simulation | entiers | corrections des brouillons 2 |
| 11:50 | `prereg/T0.6-organismes-v0-v1.md` : titres de sections (recherche des lignes de titre) et l. 671, section « Devis » | titres seulement ; une ligne | source d'une durée citée au devis (1 534 s) |
| 12:01 | cinquième message de la mère (mis en file à 11:41) | entier | référence de l'article de Soopal et al. ; ajout de deux conditions accordé dans son principe |
| 12:02 | `docs/sources/pdf/2611.14950v1.pdf` (`6396abd53a24b457519a4f5e5d669a74e1a91cce9a6e5b6b4175821ad3ab94d6`), article de littérature | p. 1, 2, 6, 7 et 8 | relire sur la page le résultat cité avant de le citer (R7) |

## Expositions déclarées

1. **Nombres du premier test de l'organisme à consigne cachée**, cités par des textes que le mandat nomme (texte scellé de T0.6, l. 58, 408, 464, 568, 643-646, 698-702 ; proposition P-015, l. 9-10, 80-82, 104, 115-117 ; texte scellé de T0.7, l. 1028-1030 ; texte scellé de T0.8, l. 49) : aire du coût seul 0,888 ; effet 1,5227 pour une demande de trois fois ; conditions instruites sans demande de gonflement à −0,3176 et −0,3229 ; « sondes génériques sous leur plancher » ; part des coûts honnêtes du pilote à plus d'un facteur 10 de la référence ; durées et coûts de ce run et de la course exploratoire de l'organisme à adaptateur (devis), dont un avertissement de mémoire. Employés pour la puissance, le devis et le témoin positif ; aucun ne fixe une dose ni un seuil.
2. **Fragments de phrases des textes privés du premier test**, vus par un relevé de structure de `premier_test_ia/conditions.py` (l. 35-37 : « private note », « only you can see », « three times », « higher cost »). Le fichier des textes (`prereg/P3-consignes-v1.md`) n'a pas été ouvert ; seule son empreinte a été calculée.
3. **Consignes permanentes** (`CLAUDE.md`) : index des décisions, qui dit en une ligne le fond de plusieurs d'entre elles.

## Non lu, à dessein

`registres/etat.md`, `registres/decisions.md`, `registres/go.md`, `registres/depenses.md`, toutes les passations ; tout résultat sous `diag/` et `runs/` hors du tirage des papiers ; tout verdict ; toute note de synthèse de résultats, dont la note « pour Lazar seul » et la pièce de choix ; les sections « Ce que les auteurs savaient » et « Puissance » des textes scellés ; `prereg/P3-consignes-v1.md` ; aucune sortie des deux courses de l'organisme à adaptateur ; aucun score de sonde ni de base.

## Sous-agent de contre-lecture

Un sous-agent neuf, d'un autre modèle que l'auteur, effort élevé, a contre-lu les brouillons 1 puis vérifié les corrections. Sa consigne lui interdit les mêmes fichiers et lui donne les mêmes plages de lignes ; elle lui fait lire les textes privés du nouvel organisme, qu'il contre-lit. Ses lectures et ses expositions éventuelles sont dans l'en-tête de son rapport (`brouillons/g0-criteres-2-3-v1/`).
