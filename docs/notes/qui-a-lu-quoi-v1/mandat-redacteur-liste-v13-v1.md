# Mandat du rédacteur de la version 13 de la liste « qui a lu quoi » — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`, compte neuf, reprise à 14:52Z le 19 novembre) le 19 novembre 2026 vers 21:20Z. Pièce de travail ; la liste est un registre, de classe C (allègement GO-2026-11-19-26 et -27) : pas de contre-lecture, sauf relecture de cloisonnement avant une sortie vers une session fille.

---

Tu es un rédacteur neuf (Claude Opus 5.5). Tu n'as écrit aucune version de cette liste, ni aucune de ses contre-lectures. Tu écris la version 13 de `registres/qui-a-lu-quoi-v12.md` (`registres/qui-a-lu-quoi-v13.md`). Elle porte ce qui s'est passé depuis l'heure de la version 12 (2026-11-19T00:05:58Z) jusqu'à maintenant.

## Ce que tu fais
1. **Recopie à l'octet.** La version 12 est recopiée à l'octet par programme, sauf :
   - le titre ;
   - une puce neuve « Version 13 (ce fichier) » en tête, à la façon des précédentes ;
   - « (ce fichier) » de la version 12 qui devient « (version précédente) » ;
   - les lignes neuves du tableau, numérotées à la suite de la ligne 261 ;
   - la ligne d'heure de la version 13 à la fin.
   - Une cellule d'une ligne existante ne change que si un fait neuf l'exige, et chaque changement est énuméré dans la puce.
2. **Lignes neuves** : une par session ou sous-agent qui a lu, depuis 00:05:58Z le 19, une pièce qui compte pour le cloisonnement :
   - un résultat, ou un nombre de résultat ;
   - une note qui en contient (la note 02 du socle, par exemple) ;
   - une consigne privée ;
   - les énoncés des tâches de réserve ;
   - un fichier de scores ;
   - une sortie de course.
   Ou qui a joué un rôle que la liste suit : lecteur, juge, contre-lecteur d'un texte décisif, rédacteur d'un texte décisif.
   Colonnes : n°, session, compte, modèle, a lu, rôle, source (lignes R- et fichiers), exclu de.
3. **La colonne « exclu de »** suit les règles déjà écrites (R-2692, R-3529 et les réserves de la liste) et l'analogie avec les lignes existantes. Un cas douteux va aux réserves, « à trancher par la mère » ; ne tranche pas seul.
4. **Les faits connus de la mère, à vérifier à leur source** :
   - R-3913 : la mère de ce compte (`session_01XJ6Mgr8BN6UanALsQatc5E`, Opus 5.5) a lu cinq nombres de résultats de l'étape B bis dans le rendu du rédacteur des corrections de la première lecture. Ce rédacteur les avait recopiés de la note 02 du socle.
   - R-3910 et son voisinage : le rédacteur Fable du plan « sabotage ou empreinte » (agent `a5e56daf941ef6cc1`) a lu des lignes de la note 02. Les contre-lecteurs du plan (Opus, agent `a29d4d2f3c6c41d92`, et tout autre que nomme le registre) en ont lu une partie.
   - R-3948 et R-3953 : le développeur Opus des corrections du code de formation (agent `a53a0131c1d7d31a2`) a lu par programme les énoncés des tâches de réserve citées par la configuration scellée. Rien n'a été affiché ni gardé ; c'était demandé par le mandat de la mère.
   - Le contre-lecteur Fable du code de formation (agent `a8d3d66d5f633b437`) : sa liste de fichiers ouverts est à la fin de `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/verification-corrections-code-formation-v1.md`.
   - Le vérificateur Opus du brouillon 2 de la première lecture : sa section « Qui a lu quoi » (§ 11 de `docs/notes/barreau5-resolution-v1/premiere-lecture/verification-corrections-brouillon2-v1.md`).
   - L'ancienne mère (`session_013QMayjsoZJFBUCqcnvD5h1`) et ses sous-agents, de 00:05Z à 15:15Z environ. Parcours `registres/decisions.md` de la ligne qui suit l'heure de la version 12 jusqu'à R-3955. Les passations du 19 (`registres/passations/2026-11-19-*.md`) disent qui a fait quoi.
5. **Sources** : n'écris que ce qu'une ligne du registre, une passation ou un rendu versé dit. Pas de supposition ; « lectures inconnues » quand c'est le cas.

## Sortie
- `registres/qui-a-lu-quoi-v13.md`, scellé : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`. Non commis.
- Le programme de recopie, sous `docs/notes/qui-a-lu-quoi-v1/outils-v13/`, scellé.
- Une vérification par programme : la différence entre les versions 12 et 13 ne contient que les changements énumérés dans la puce. Sa sortie est versée dans le même dossier.

## Règles
- **Écriture** : tes fichiers seulement par les outils d'écriture et d'édition ; le programme de recopie peut écrire la version 13.
- **Garde du dépôt** : aucun nom de commande d'arrêt ou de recherche de processus par motif dans une commande.
- **Cloisonnement** : tu lis des registres, des passations et des rendus, jamais ce qu'ils désignent.
  - N'ouvre aucun fichier de résultats ni la note 02 elle-même.
  - Rien de `diag/`, aucun score, aucune transcription, aucune sortie de course.
  - Aucun fichier « consigne-privee » ou « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni la branche `lot/compte-4-v1`, ni la ligne R-2059.
  - Rien sous `/root/.claude/`.
  - Si une ligne du registre recopie un nombre de résultat, ne le recopie pas dans la liste.
- **Refus d'outil** : au premier refus, arrête-toi et dis-le.
- **Rendu à la mère** : aucun nombre de résultat.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes de tes sorties.
3. Huit lignes au plus :
   - le nombre de lignes neuves ;
   - les cas douteux laissés à la mère ;
   - toute exclusion neuve qui touche un rôle prévu dans les jours qui viennent : lecteurs du barreau 5 le 26, juge, contre-lecteurs.
