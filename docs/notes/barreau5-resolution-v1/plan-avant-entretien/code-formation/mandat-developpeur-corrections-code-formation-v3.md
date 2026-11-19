# Mandat du développeur Opus 5.5 : deuxième tour de corrections du code de formation (barreau 5) — v3

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 21:00Z. Pièce de travail. Destinataire : le développeur qui a écrit `rapport-developpeur-corrections-code-formation-v3.md` (`ddaf91a8…`). Le même contre-lecteur Fable vérifiera ce tour avec le suivant, d'un seul trait.

---

Ton code a été vérifié par le contre-lecteur : « conforme après ces corrections ». Sa vérification : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/verification-corrections-code-formation-v1.md` (`3517677f…`, scellée), à lire en entier, avec ses outils dans `outils-verification-corrections-code-formation-v1/`. Elle laisse sept constats neufs, tous mineurs (n-1 à n-7, § 7). Tu corriges maintenant ceux qui ne dépendent pas du texte. Ceux qui en dépendent attendent le brouillon 4 et le mot de Lazar ; ce sera le troisième tour.

## Ce tour : à corriger et à éprouver
1. **n-1** : un arrêt avant la marche rend la destruction impossible, faute de manifeste. Applique la correction proposée, ou mieux si tu la juges fausse, avec ses deux essais : cas sain et artefact.
2. **n-2** : écris dans l'en-tête du lanceur que `detruire` reçoit le commit prouvé, et non la tête de la branche. Reprends la même phrase au § 5 de ton rapport v4.
3. **n-3** : fais jouer ensemble la minuterie et la fin de l'amorce dans l'essai de l'amorce entière, avec les deux essais proposés.
4. **n-5** : donne un contenu borné aux fichiers de texte de la liste blanche (clés exactes, types). La mutation V06 du vérificateur doit devenir un artefact refusé.
5. **n-7** : ajoute l'artefact qui isole la comparaison de la tête distante.
6. **n-6** : joue une fois les essais du paquet sous Python 3.11, la version de l'image de l'instance, si c'est faisable sans dépense.
   - Interpréteur et dépendances dans `/dev/shm` ; disque libre : environ 15 Go.
   - Dépendances : `requirements-gpu.txt`, avec torch pour processeur à la même version.
   - Efface ensuite par chemin écrit en toutes lettres.
   - Si ce n'est pas faisable, dis pourquoi : le repli sera de lancer la première instance seule, quelques minutes avant les autres.
7. **Version de `transformers` au manifeste** (couple C-8e du rédacteur) : écris-la au manifeste de la marche. Dis si une garde la vérifie déjà sur l'instance ; n'ajoute pas de refus sans le dire.
8. **Plancher d'essais de l'amorce** : remets-le au compte exact si tu ajoutes ou retires un essai du paquet joué sur l'instance, et remesure-le sur l'arbre extrait.

## Ce tour : à décrire seulement, sans coder
Le rédacteur prépare le brouillon 4. Il a besoin de savoir ce que le code porte déjà. Lis `docs/notes/barreau5-resolution-v1/plan-avant-entretien/couples-du-code-pour-brouillon4-v1.md` (`1e929542…`), au moins ses couples C-1a à C-1d, C-2b, C-4a, C-6a et C-8a à C-8e.

Pour chacun des points ci-dessous, dis :
- ce que le code fait aujourd'hui (fonction, lignes) ;
- ce qu'il faudrait changer (lignes de code, essais) ;
- ton estimation du temps.

Les points :
- (a) les deux paliers de la part non éditable, de 10 et 25 %, avec le marqueur et la part par motif (C-6a) ;
- (b) la règle « seule la copie `-x1` est lue » dès qu'une ligne de relance est inscrite (C-2b) ;
- (c) la borne des relances : sous le plafond commun, comme le recommande le vérificateur (n-4) ; ou hors du plafond, à la coupure de l'instance remplacée, comme le propose le rédacteur (C-2b). Les deux divergent : décris les deux, sans choisir ;
- (d) le remède 1 du vérificateur : un nombre collé à une lettre (« A100 ») n'est pas compté, sans toucher au lecteur gelé (vérification, § 8) ;
- (e) le remède 2 du vérificateur : « 2k » devient la valeur en clair au lieu de sortir l'action ;
- (f) la ligne de table des instances 6 et 7 à trois membres, avec les nombres du rédacteur (groupe 2, en tête) ;
- (g) tout point des couples qui suppose un comportement du code que le code n'a pas.

## Sorties
- **Le code et les essais corrigés**, dans le dépôt principal, sous les mêmes noms. Le code n'est pas figé : tu le corriges en place.
- **Rapport v4** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/rapport-developpeur-corrections-code-formation-v4.md`, scellé. Il contient :
  - la table « constat → correction → essai qui l'attrape » ;
  - la description demandée, points (a) à (g) ;
  - le résultat de n-6 ;
  - le nombre d'essais et le plancher ;
  - les empreintes finales de tous les fichiers de code et d'essais.
- **Tes outils**, s'il y en a, versés sous `outils-developpeur-corrections-code-formation-v4/`, avec leurs compagnons scellés.

## Règles
- Les mêmes que ton mandat v2 (`mandat-developpeur-corrections-code-formation-v2.md`, « Règles »).
- Et encore :
  - **Garde du dépôt** : aucun nom de commande d'arrêt ou de recherche de processus par motif dans une commande, même dans une boucle d'attente. Attends la fin d'une tâche par l'outil de tâches ou par la lecture de son journal. Tu l'as fait une fois au tour précédent : ne le refais pas.
  - **Écriture** : tes fichiers seulement par les outils d'écriture et d'édition. Temporaires dans `/dev/shm`.
  - **Essais** : seulement les fichiers du paquet ; jamais la suite entière.
  - **Rien de réel** : aucun réseau vers un loueur de cartes ni vers Hugging Face. Aucune dépense, aucune instance, aucun commit.
  - **Cloisonnement** : aucune donnée, aucun résultat, aucune transcription. Aucun énoncé de tâche : ne rejoue pas l'essai à blanc du tokeniseur. Rien de `diag/`, rien sous `/root/.claude/`, aucun fichier « consigne-privee » ou « conception-ii-b ».
  - **Refus d'outil** : au premier refus, arrête-toi et dis-le.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Tes fichiers, avec leurs empreintes.
3. Dix lignes au plus :
   - les constats corrigés ;
   - le nombre d'essais et le plancher ;
   - n-6 ;
   - les points (a) à (g), une demi-ligne chacun ;
   - ce qui menace le gel du 22.
