# Mandat du contre-lecteur du code de lecture (barreau 5, plan « sabotage ou empreinte ») — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026 vers 01:40Z. Pièce de travail.

Destinataire : un contre-lecteur neuf, Claude Fable 5.2, d'un autre modèle que le développeur (Opus 5.5). Pièce d'instrument : contre-lecture par un autre modèle ; la vérification des corrections te reviendra ensuite.

---

La formation du barreau 5 est partie à 01:30:16Z : instance 6 seule cette nuit, les autres au retour du crédit. Le code de lecture doit être figé (`CODE-LECTURE-B5F`) avant la fin de la formation. C'est maintenant le chemin critique du verdict. Tu le contre-lis.

## Pièces (vérifie chaque empreinte avant de lire)
- **Le texte scellé** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`). Lis en entier ce qui touche la lecture :
  - « Hypothèse », « Prédiction chiffrée et signe attendu », « Métrique », « Seuil » ;
  - « Plan d'analyse », points 7 à 18 ;
  - « Puissance », « Critères de lecture gelés », « Ce que dira chaque issue au jury » ;
  - « Liste d'arrêt », « Données gardées », « Lignes de registre », « Code neuf ».
- **Le rapport du développeur**, en entier : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/rapport-developpeur-code-lecture-v1.md` (`a140273f1e60d2bf195fbee1cc8166a6a0b28a8148951d7bd641676cb588aeda`).
- **Son mandat** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/mandat-developpeur-code-lecture-v1.md` (`fffe5bd785705d54035c9a29cae6beef4ba8fedf0d4eca0ec17834b1dd48460b`).
- **Le code et ses essais**, au commit `8c1d691886b5e0a568e11358e0d83b3f9cdc7ad4` de `main` :
  - `src/controle_ia/barreau5_familles/lecture_v1.py` (`c3db0074…`) ;
  - `src/controle_ia/barreau5_familles/relecture_v1.py` (`c1c7c65f…`) ;
  - `src/controle_ia/barreau5_familles/sondes_v1.py` (`cfc2237a…`) ;
  - `scripts/lancer_b5f_lecture_v1.sh` (`de83c346…`) ;
  - `tests/test_barreau5_familles_lecture_v1.py`, `tests/test_barreau5_familles_relecture_v1.py`, `tests/test_barreau5_familles_sondes_v1.py`, `tests/test_lancer_b5f_lecture_v1.py`.
- **Les outils du développeur** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/outils-developpeur-code-lecture-v1/`. Les noms des fichiers sont donnés dans son rapport ; ouvre-les par leur chemin entier.
- **Pour les conventions seulement** : le code de formation, figé (`formation_v1.py`, `engagement_v1.py`, `edition_cout_v1.py` dans le même paquet). Tu ne le juges pas.

Le développeur écrit en ce moment l'amorce de l'instance de lecture et sa commande de création. Ce sont des fichiers neufs. Ils te viendront à la vérification, avec tout ce qui aura changé depuis ce commit.

## Ce que tu juges
1. **La lettre du texte**, point par point (8 à 13 et 18).
   - La relecture forcée et le chemin éprouvé.
   - La notation fermée : aucune statistique d'adaptateur tirée d'un score de sonde sur l'instance ; seuls les produits P et les poussées le long de ĝ y sont calculés.
   - Les mises à l'échelle de E2a et E2b, faites seulement à la lecture.
   - Le maximum sur les jetons, calculé seulement à la lecture.
   - Le dénombrement exact des rangs signés ; les issues et leurs phrases ; la règle du nœud 6.
   - L'ordre (a) à (h) de la lecture ; la garde d'ouverture.
   - Sous chaque écart : le passage du texte et les lignes du code.
2. **Les gardes**, chacune avec son cas sain et son artefact (R5) :
   - moyenne sur les jetons ;
   - table dans l'arbre de lecture ;
   - engagement postérieur ;
   - score manquant ;
   - famille incomplète ;
   - identité à dose 0 et artefact à dose 1 ;
   - contrôle carte-processeur.
3. **Les quatre questions au texte** du rapport du développeur : formats des lignes de registre de la lecture ; niveau d'une issue sous huit familles ; ordre du point 13 de la liste d'arrêt et du critère « non interprétable » ; retrait d'une tâche sans coût lisible pour un seul membre. Pour chacune, dis si le texte la tranche (avec le passage), sinon qui doit trancher : le rédacteur du texte par un addendum, ou Lazar.
4. **Sa remarque pour la fabrique de l'épreuve à vérité plantée** : le bruit propre à chaque membre dans V3, V8, V9 et V12. Est-elle juste au regard du point 11 ?
5. **Sondages et mutations.**
   - Rejoue les essais du paquet de lecture.
   - Ajoute 5 à 8 mutations de ton choix, absentes de sa liste, sur ce qui décide : le dénombrement, la table des issues, la garde d'ouverture, la notation fermée.
   - Dis combien sont attrapées.
6. **La séparation d'avec la formation.** Ce code ne doit toucher aucun fichier du code de formation figé. La branche de la course `course/barreau5-formation-v1` ne le porte pas. Vérifie les deux.

## Forme et sorties
- **Verdict en tête**, l'un des trois : « conforme », « conforme après ces corrections », « à reprendre ».
  - Pour chaque correction : fichier, lignes, avant, après.
  - Classe chaque constat : bloquant, majeur ou mineur.
- **Sorties**, scellées, non commises :
  - `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/contre-lecture-code-lecture-v1.md` ;
  - tes outils et leurs sorties dans `code-lecture/outils-contre-lecture-code-lecture-v1/`.
- **Commande de scellement** : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.
- **Écris au fil de l'eau.** Scelle chaque état ; la mère verse les états intermédiaires.

## Règles
- **Aucune donnée.**
  - Modèle jouet et fichiers fabriqués seulement.
  - Rien de `diag/`, aucun score réel, aucune transcription.
  - Aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis.
- **Fichiers interdits** : aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ; rien sous `/root/.claude/`.
- **Aucune commande de liste ni de recherche récursive** sur une racine large du dépôt. Ouvre chaque fichier par son chemin entier, donné ici ou dans le rapport du développeur. Un dossier `archives-reponses-modeles/` ne se parcourt jamais, même pour une empreinte.
- **Pas de code en ligne passé à l'interpréteur** (`python -c`, `python -`) : écris un fichier dans ton bloc-notes et lance-le par son chemin.
- **Garde du dépôt** : aucun nom de commande d'arrêt ou de recherche de processus par motif dans une commande.
- **Écriture** : tes fichiers seulement, par les outils d'écriture et d'édition. Ne modifie jamais le code du dépôt.
- **Rien de réel** : aucun réseau vers un loueur de cartes ni vers Hugging Face, aucune création d'instance.
- **Essais** : seulement les fichiers d'essais du paquet `barreau5_familles`, en commande simple. Temporaires dans `/dev/shm`, effacés à la fin par leur chemin écrit en toutes lettres.
- **Refus d'outil ou limite d'usage** : au premier, arrête-toi et dis-le, sans contournement.
- Aucun commit, aucune dépense.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes de tes sorties.
3. Dix lignes au plus :
   - le verdict ;
   - les constats par classe ;
   - les mutations attrapées sur jouées ;
   - tes réponses aux quatre questions ;
   - ce qui menace le gel.
4. La liste des fichiers que tu as ouverts.
