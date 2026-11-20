# Mandat du rédacteur de l'addendum 1 du plan « sabotage ou empreinte » (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026 vers 02:05Z. Pièce de travail.

Destinataire : un rédacteur neuf, Claude Fable 5.2. Règle « qui conçoit » : un addendum à un préenregistrement scellé est une pièce de conception, de classe A. Chaîne : rédaction par Fable ; contre-lecture par un Opus neuf ; vérification des corrections par le même Opus ; scellement sur le mot de Lazar.

---

Le texte du plan est scellé : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`). La formation tourne depuis 01:30:16Z. Le code de lecture est écrit et contre-lu.

Son développeur et son contre-lecteur ont relevé trois points que le texte ne tranche pas. Ils doivent être fixés **avant** trois choses : le gel du code de lecture (`CODE-LECTURE-B5F`), la seconde programmation du dénombrement et de la table des issues par l'autre modèle (point 11), et l'épreuve à vérité plantée. Aucune donnée n'existe encore de la lecture : rien n'est lu, aucun score n'existe. Tu écris l'addendum qui les fixe.

## Pièces (vérifie chaque empreinte)
Toutes dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/`, sauf le texte et le code.
- **Le texte scellé**, en entier, sauf les passages qui citent des résultats de l'étape B bis ou la phrase de la consigne du saboteur. Tu n'en as pas besoin ; ne les recopie pas.
- **Le rapport du développeur** : `rapport-developpeur-code-lecture-v1.md` (`a140273f1e60d2bf195fbee1cc8166a6a0b28a8148951d7bd641676cb588aeda`), section des questions au texte.
- **La contre-lecture** : `contre-lecture-code-lecture-v2.md` (`f2f81f32efa1bb05cb138e5e5825f91467548b9efd2c17ede390c29e9893e680`), en entier, en particulier ses réponses aux questions et le constat M-2.
- **Le code**, pour voir ce qu'il fait aujourd'hui : `src/controle_ia/barreau5_familles/lecture_v1.py`, aux lignes que citent le rapport et la contre-lecture.

## Ce que tu fixes, et seulement cela
1. **Le niveau d'une issue sous huit familles** (question 2 du développeur). Le code prend le plus faible des niveaux de M1, M3 et des épreuves que l'issue affirme. Est-ce la lecture du texte, au nœud 6 et dans « Critères de lecture gelés » ? Sinon, quelle règle ?
2. **Une tâche sans coût lisible chez un seul membre** (question 4). Le code ne la retire que pour ce membre. Le point 17 (« contrôles appariés ») penche, selon la contre-lecture, pour la retirer à tous les membres de la famille. Fixe la règle.
3. **La valeur de « [borne] » dans la phrase de l'issue E** (point ajouté par le contre-lecteur). Fixe-la, ou la règle qui la calcule.

Pour chacun des trois points :
- cite le passage du texte qui s'en approche ;
- donne la règle, en une forme qu'un programme applique sans choix ;
- dis ce qu'elle change dans le code, et dans quelle épreuve du point 11 elle se voit ;
- montre qu'aucune donnée ne l'a inspirée. Il n'en existe pas : dis-le, et dis ce que tu as lu.

## Ce que tu ne fais pas
- Rien d'autre ne change : ni hypothèse, ni prédiction, ni seuil, ni critère, ni épreuve, ni liste d'arrêt, ni décision de Lazar.
- Si un des trois points ne peut être fixé sans toucher l'un d'eux, ne le fixe pas : écris-le comme question à Lazar, avec deux ou trois options, une recommandation et ta confiance.
- Les corrections de code M-1 à M-4 ne te regardent pas : elles suivent la lettre du texte.
- Les formats des lignes de registre de la lecture sont adoptés par la mère tels que le code les fixe ; tu n'y touches pas.

## Forme et sorties
- **Le brouillon** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon1.md`.
  - En tête : le texte visé et son empreinte ; « ne change ni hypothèse, ni prédiction, ni seuil, ni critère, ni épreuve, ni liste d'arrêt » ; l'auteur et le modèle ; la date ; ce que tu as lu.
  - Puis les trois points, et une section « Contre-lecture » vide.
  - Scelle-le comme brouillon.
- **Un rapport court** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/rapport-redacteur-addendum-1-v1.md`, scellé. Il donne tes sources, tes doutes, et ce qui ira à Lazar.
- **Commande de scellement** : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.
- **Écris au fil de l'eau**, et scelle chaque état.

## Règles
- **Aucune donnée.** Rien de `diag/`, aucun score, aucune activation, aucune transcription, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis. Rien de la branche de la formation.
- **Fichiers interdits** : aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ; rien sous `/root/.claude/`.
- **Aucune commande de liste ni de recherche récursive** sur une racine large. Ouvre chaque fichier par son chemin entier. Ne traverse jamais un dossier `archives-reponses-modeles/`.
- **Pas de code en ligne passé à l'interpréteur.**
- **Garde du dépôt** : aucun nom de commande d'arrêt ou de recherche de processus par motif.
- **Écriture** : tes fichiers seulement, par les outils d'écriture et d'édition. Aucun code du dépôt modifié.
- **Interdits** : aucun réseau, aucune dépense, aucun commit.
- **Au premier refus d'outil ou à la limite d'usage**, arrête-toi et dis-le.
- **Tenue** : ne nomme dans tes pièces aucun identifiant d'accord d'écart à la règle R9.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes de tes sorties.
3. Dix lignes au plus :
   - la règle fixée pour chacun des trois points ;
   - ce qui va à Lazar ;
   - ce qui menace le gel.
