# Brief de lancement — session des lentilles neuve — 2026-11-21 — v1

Ce brief remplace la v1 du 20 novembre, qui reste archivée.

Tu reprends la **session des lentilles** du programme « Contrôle boîte blanche des menaces diffuses ». Le dépôt est `lciric/controle-ia-travail`, privé.

Langue : français, tutoiement avec Lazar. Nomme les choses en clair ; les identifiants viennent en appui.

## Ce que tu lis d'abord, dans l'ordre
1. `CLAUDE.md`, la version de main : règles R1 à R14, « Qui conçoit », hiérarchie de décision, interdits.
2. Les deux dernières passations de la session des lentilles, sur `claude/brave-galileo-jhp684`, sous `registres/passations/lentilles--2026-11-21-*.md`. Vérifie leurs empreintes (`PYTHONPATH=src python -m controle_ia.scellement verifier <chemin>`).
3. Ce brief.
4. La règle du canal en essaim, sur main : `registres/essaim/regle-du-canal-essaim-v1.md`.
5. Ton dossier sur main, `registres/essaim/vers-lentilles/`, et lui seul.
6. La routine de reprise (R14). Les essais complets du dépôt durent plus de deux heures : lance-les par morceaux ou par fichier.

## Branche et liaisons
- **Branche accordée : `claude/brave-galileo-jhp684`.**
  - N'écris jamais sur `main` ni sur `lciric/controle-ia`.
  - Ne récupère jamais les branches `donnees/*`, `calcul/*` ni `verdict/*`.
  - Fais tes `fetch` et tes `pull` en nommant la branche.
- **La mère** : session_01Qi7Gr3eYmAhDEJzqLgWcv1, en poste depuis le 21 à 15:20Z.
  - Écris-lui par `registres/essaim/vers-mere/` sur ta branche, en suivant la règle du canal : en-tête, sceau, mots de Lazar cités tels quels.
  - Le `send_message` direct est permis là où il passe. L'ancienne mère refusait les envois (appareil de confiance).
- **Rôles cloisonnés**, dont le bras d'attaque et l'attaquant informé : aucun message direct ; tout passe par la mère.
- **Agents** :
  - Les pièces délicates (conception, préenregistrement) sont écrites par un sous-agent neuf sur **Fable**.
  - Les contre-lectures et vérifications sont faites par un sous-agent neuf sur **Opus 5.5**, d'un autre modèle que le rédacteur.
  - Chaque rédacteur Fable part sur un mot de Lazar.
  - Chaque agent reçoit un mandat écrit et scellé, avec la liste explicite des pièces.
  - Un agent long peut manquer de mémoire de travail : demande-lui de le dire au départ, et prévois un remplaçant neuf.

## Cloisonnement (toi et tes agents)
**Ne lis jamais :**
- la liste « Jamais ouverts » des textes de lecture v1 et v2 ;
- toute sortie, tout score, toute table, toute lecture ou tout verdict de l'apprentissage des sondes sur la tâche (étape B bis), y compris `VERDICT-BBIS` et la note réservée à Lazar ;
- toute table ou sortie de la lecture par la lentille publique, y compris `arret.json` ;
- `diag/`, `runs/`, `docs/verdicts/` ;
- les fichiers « consigne-privee » ou « conception-ii-b », et `brouillons/ii-b-saboteur-budget-v1/` ;
- P3, P3-bis, T0.6 et T0.7 hors des textes de lecture ;
- l'étape B, le bras d'attaque, le saboteur à budget.

**Lecture des registres de main** : ne lis que les lignes cherchées par leur identifiant. Une ligne de GO peut porter plusieurs sujets ; déclare tout intitulé vu.

**Quand tu lances la suite complète du dépôt**, n'affiche que des comptes : certains noms d'essais de main touchent des sujets cloisonnés.

**Règles qui ne bougent pas** :
- Un refus d'outil n'est jamais rejoué ; il est déclaré.
- Rien ne se lance, ne se loue ni ne se dépense sans mot de Lazar.
- Les secrets se citent par leur nom seulement.
- Aucun identifiant de modèle dans les commits.

## Accords en cours (registres/go.md de main)
- GO-2026-11-18-42 : lecture par la lentille publique, au processeur, 0 USD. Échéance le 2026-11-27.
- GO-2026-11-19-33 : pièces 1 à 3 du billet.
- GO-2026-11-19-78 : addendum de concentration (7c738708…).
- GO-2026-11-19-92 : règle de départage.
- GO-2026-11-20-18 : nœuds N12 et N17.
- GO-2026-11-20-56 : messages d'arrêt cloisonnés.
- GO-2026-11-21-06 : mots fixes gardés, garde du fichier d'arrêt.
- GO-2026-11-21-24 : feu de la première passe, lancement depuis main, nœuds A à D.
- Mots de Lazar consignés en notes sur la branche :
  - « a go » : développeur des deux passes ;
  - « go a » et « go les deux » : canal en essaim.

## État
- **Première passe** : code fixé.
  - Lanceur v7, commit cc7f4576.
  - Fiche définitive a44c0e54…, contre-lecture conforme e37f9b64….
  - Liste v3 à verser sur main : b4ad54d5…, commit cc9ab8eb, éprouvée (88f7dc34…).
  - Extrait GO-LENTILLES-BBIS : 8a68e335….
  - Mandat de l'opérateur v2 : 90f8befb….
  - Le versement, les lignes du registre et l'ouverture de l'opérateur reviennent à la mère.
- **Seconde passe** (nos lentilles R et S, texte de lecture v2 scellé a2bbed7a…) : rien d'écrit.
  - Mandat du développeur : 0a9517ea…, étape 2.
  - Passation du premier développeur : 708203b1….
- **Décisions à défaut le 22 vers 13:30Z** :
  - développeur Fable neuf pour la seconde passe ;
  - égalité de la relecture de contrôle de l'audit, gardée sans arrêt.

## Prochaine action exacte
1. Lis ton dossier `vers-lentilles/` sur main.
2. Si la mère a versé le code et ouvert l'opérateur, réponds à ses demandes, sans lire aucune sortie de la course.
3. Pour la seconde passe, dès que Lazar a dit son mot ou que le défaut est échu, écris le mandat d'un développeur Fable neuf, scelle-le, et lance-le. Il reprend l'étape 2 du mandat 0a9517ea… à partir de la passation 708203b1…, en lisant d'abord en entier le texte v2.
