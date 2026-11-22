# Vérification de la différence entre le brouillon 3 et la version scellée — texte gelé de la tranche de l'ajustement de nos lentilles (B-β), v1

- **Objet** : dire si la différence entre le brouillon 3 (A) et la version scellée (B) du préenregistrement de l'ajustement de nos lentilles R et S sur Llama 3.1 8B Instruct ne contient que le traitement des onze mineures n-1 à n-11 de la vérification du brouillon 3 (V), plus le changement d'en-tête et de statut attendu d'une version scellée.
- **Empreintes vérifiées** (`sha256sum`) :
  - A, `texte-gele-tranche-b-beta-v1-brouillon3.md` : `c6a6b00eca055ac38221cdf71d97ada8b71c51c82429c2d7f514d8f040cefb47`, égale à l'attendue ;
  - B, `texte-gele-tranche-b-beta-v1.md` : `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454`, égale à l'attendue et à son compagnon `.sha256` ;
  - V, `verification-texte-gele-tranche-b-beta-v1-brouillon3.md` : `b8e3bcb9bc8fbe713377585c1000b3beb9a08bc5fa07cd8ff699de77043292e4` (aucune valeur attendue ne m'a été donnée ; elle est égale à celle que B cite).
- **Date** (`date -u`) : 2026-11-18, 04:24 à 04:26 UTC.
- **Vérificateur neuf** (modèle Fable 5.2) : n'a écrit ni lu aucune pièce de ce travail avant cette tâche. N'a écrit que ce rapport ; rien modifié d'autre, rien committé.
- **Pièces lues** : V en entier ; la sortie complète de `diff A B` (14 blocs, 641 lignes contre 667) ; dans B seulement, quelques lignes de contexte autour des blocs (gardes (j) à (m), lignes qui citent la graine 1, la copie à part du banc, « mère »), la date du fichier et le compagnon `.sha256`. Aucune autre pièce ouverte.

## Verdict

**Conforme sur les règles, avec un ajout hors des onze mineures** : aucun seuil, aucune mesure, aucune issue, aucun verdict n'est ajouté, retiré ou changé ; les gardes ne bougent que là où n-1 à n-11 le demandaient, et pas plus loin ; le seul ajout étranger aux onze mineures est la clause de licence étendue du paquet Drowse, descriptive, qui ne touche aucune règle de l'expérience.

Réponses aux quatre questions :

- **Seuils, mesures, issues, verdicts** : rien d'ajouté, de retiré ni de changé. Aucun chiffre de seuil ne figure dans une ligne touchée, sauf dans la ligne de provenance neuve (n-7), qui cite des valeurs publiées déjà employées par la garde (c).
- **Gardes, règles d'arrêt, prédictions** : quatre gardes sont touchées, (i), (k), (l), (o), chacune dans le sens demandé par V (n-10, n-8, n-11, n-9). Aucune prédiction, aucune ligne de la liste d'arrêt n'est dans le diff. Deux traitements vont moins loin que la proposition de V (voir n-1 et n-8 plus bas) ; aucun ne va plus loin.
- **n-3** : traité « non retenu », et la raison est écrite, deux fois (en-tête, l. 12-14 de B ; table de reprise) : le modèle servi à la session autrice aurait été relevé par l'outil de session vers 04:22 UTC et différerait de celui des lecteurs ; le second lecteur se serait trompé en lisant l'attribution des commits. Cette raison **ne change aucune règle** : elle remplace une phrase d'en-tête par une autre. Elle garde en revanche l'affirmation que V jugeait non établie, sans pièce jointe (voir « Non vérifiable »).
- **Ajout hors des onze mineures** : oui, un seul, dans le bloc 9 : la clause de licence de Drowse. La ligne de provenance (bloc 13) n'en est pas un : c'est le traitement de n-7.

## Table des blocs

Les 14 blocs de `diff A B`, dans l'ordre. Deux blocs mêlent deux objets ; ils sont scindés (3a, 3b ; 9a, 9b), soit 16 unités.

| bloc | lignes (A → B) | contenu du changement | classe | touche une règle ? |
|---|---|---|---|---|
| 1 | 1 → 1 | titre : « v1, brouillon 2 » devient « v1 » | en-tête ou statut (aussi n-4) | non |
| 2 | 5-9 → 5-8 | « Brouillon 3, non scellé » devient « Version scellée (R1, R12) » ; chaîne des trois brouillons et de leurs lectures, empreintes abrégées ; « 11 mineures, toutes levées ici » | en-tête ou statut | non. Remarque : « toutes levées » est plus fort que la table de reprise, qui dit n-3 « non retenu » |
| 3a | 13 → 12-14 | « Le contre-lecteur sera d'un autre modèle que l'autrice » devient : les deux lecteurs sont d'un autre modèle que celui qui sert la session autrice, relevé par l'outil de session ; objection du second lecteur « non retenu » | mineure n-3 (non retenue, raison écrite) | non |
| 3b | 14 → 15 | date : « brouillon 3 après 04:20 » devient « entre 04:10 et 04:16 ; version scellée vers 04:30 » | mineure n-4 | non. Remarque : le fichier B est daté 04:22:28 UTC sur disque, et `date -u` rendait 04:24 quand je l'ai ouvert ; « vers 04:30 » est donc approximatif |
| 4 | 217-218 → 218-219 | garde (i), texte commun : empreinte du texte « entier (champ `text` de la ligne JSONL, sans coupe) » | mineure n-10 | oui, la garde (i), précisée exactement comme n-10 le proposait ; pas de seuil changé (932 et 40 000 inchangés) |
| 5 | 225-226 → 226-228 | garde (k) : « Avant et pendant la fumée et la passe » devient « Juste avant la fumée, juste avant la passe […] et juste avant `07_drivers.py` » ; ajout de « preuve complémentaire : le message que le correctif (1) imprime […] relevé dans le journal de la passe » | mineure n-8 | oui, la garde (k), dans le sens de n-8. En deçà de la proposition : V proposait d'exiger le message « sinon chaîne en défaut (k) » ; B le dit seulement « preuve complémentaire », sans arrêt attaché. Aucune règle d'arrêt neuve |
| 6 | 230 → 232-233 | garde (l) : ajout de « ou l'une des gardes (a) à (c) manquée sur la sortie de `score` de la graine 1 » | mineure n-11 | oui, la définition de (l), étendue comme n-11 le proposait ; l'issue (chaîne en défaut (l), rang 1) était déjà écrite dans l'audit A1 de A |
| 7 | 235-236 → 238-239 | garde (o) : ajout de « lève une erreur (le voisin lève `FileNotFoundError` […], `lenses.py` l. 37-45) ou » devant « rend `None` » | mineure n-9, point (1) | oui, la garde (o), élargie comme n-9 le proposait |
| 8 | 319 → 322-323 | correctif (5) : liens durs faits « juste avant `reads_at_firings.py` (P.3, étape 6), non après l'ajustement » | mineure n-5 | non (met le libellé d'accord avec P.3, étape 6, inchangée) |
| 9a | 334 → 338-340 | licence de Drowse : « logiciel employé sur la machine, ni modifié ni redistribué » devient « employé tel quel sur la machine louée, ni modifié, ni redistribué, ni offert comme service à des tiers » ; ajout : « publier un jour le code des lentilles avec une version modifiée de ce paquet serait un nœud : mot de la mère, 2026-11-18 vers 04:18 UTC » | **autre** | **non** : descriptif (conditions d'emploi du paquet) plus un rappel de gouvernance sur une publication future. Aucun seuil, mesure, issue, garde, arrêt ni prédiction ; la ligne « licence différente » de la liste d'arrêt n'est pas dans le diff |
| 9b | 335-336 → 340-341 | renvoi à `jlens.py` : « l. 145, 249 » devient « classe l. 141-145, propriété vers l. 249 » | mineure n-9, point (2) | non. Remarque : V situait la docstring aux l. 144-146 et la propriété aux l. 247-251 ; « l. 141-145 » n'est pas le chiffre de V |
| 10 | 419 → 424 | P.4, cas (viii) : « `arch.fits` simulé rendant `hub` » devient « […] juste avant `reads_at_firings.py` » ; attendu inchangé | mineure n-1 | non (attendu d'essai précisé, même issue). En deçà de la proposition : le cas sain « `hub` avant la passe : rien », demandé par n-1, n'est pas ajouté ; la table de reprise dit pourtant « levé » |
| 11 | 440 → 445 | P.4, ligne (q) : attendu « arrêt avant l'ajustement, deux fois » devient « chaîne en défaut (q), deux fois, avant l'ajustement ou la relance » | mineure n-6 | non (libellé de l'attendu aligné sur (r) et (s) ; (q) était déjà une chaîne en défaut de rang 1). La phrase renvoyant le détail du banc à la commande n'est écrite que dans la table de reprise, pas dans la garde (q) |
| 12 | 513 → 518 | audit A1, contenu (3) : « `score` avec notre R » devient « `score` avec les lentilles `logit,npR,R:dclm-llama` » et la raison ; déclencheurs et issues de A1 identiques au mot près | mineure n-2 | non (liste des lentilles de l'appel écrite ; aucun déclencheur, aucune issue changés). Les lignes de A5 et de P.3, étape 7, citées par n-2, ne sont pas touchées ; elles renvoient à A1 |
| 13 | après 573 → 579 | « Provenance des chiffres » : ligne neuve pour la garde (c), R publiée 0,9845 à 0,9923, logits 0,9354 à 0,9565, couches 31 à 33 de Qwen3, `causal_lens_qwen3-8b.json` (`8904c4d3…`) | mineure n-7 | non (provenance). Les quatre valeurs sont celles recalculées par V. Remarque : le chemin écrit, `["steer 1x"]["R:dclm"/"logit"]["r_med"]`, omet la clé `targets` que V donnait |
| 14 | 639-641 → 645-667 | section « Contre-lecture » : paragraphe d'attente remplacé par le résumé de V (empreintes entières de A et de V, « scellable »), la table de reprise n-1 à n-11, et la phrase « Scellement (R1) après ces corrections, sans nouvelle lecture […] » | en-tête ou statut | non. Remarque : « seuls `06_activations.py` l. 96 et `reads_at_firings.py` l. 67 lisent `arch.fits` » abrège V, qui nomme aussi des scripts non joués (`08_reads.py`, `17_firings.py`, `checks/`) |

Compte par classe (16 unités) : **mineure n-k : 12** (n-1 à n-11, n-9 sur deux unités) ; **en-tête ou statut : 3** ; **autre : 1** (descriptif, ne touche aucune règle).

Chacune des onze mineures a au moins un bloc. Aucune ligne des sections de seuils, de prédictions, de verdict d'ensemble (rangs 1 à 5), de la liste d'arrêt, du devis ou de P.3 n'apparaît dans le diff.

## Écarts de forme relevés (aucun ne touche une règle)

1. L'ajout de licence (9a) n'est pas annoncé dans la table de reprise, et la dernière phrase de B (« elles précisent des moments, des listes et des libellés désignés par le vérificateur lui-même ») ne le couvre pas.
2. n-1 et n-8 sont dits « levé » mais traités en deçà de la proposition de V (cas sain non ajouté ; message du journal sans arrêt attaché) ; n-6 l'est en partie hors du corps du texte.
3. L'en-tête dit « 11 mineures, toutes levées ici » alors que n-3 est « non retenu ».
4. « version scellée vers 04:30 » : le fichier est daté 04:22:28 UTC.

## Non vérifiable

- Le modèle qui sert la session autrice, et donc la raison écrite pour n-3 : le relevé « par l'outil de session » n'est pas joint. Ce que je vois de ma place va dans le sens du vérificateur précédent : je suis Fable 5.2, et la consigne d'attribution des commits que je reçois de la session qui m'a lancé nomme Fable 5.2. Cela ne prouve pas quel modèle sert l'autrice. R2 (sous-agent neuf qui n'a pas écrit le texte) ne dépend pas de ce point.
- « Mot de la mère, 2026-11-18 vers 04:18 UTC » sur la licence : aucune pièce lue.
- La justesse des numéros de ligne neufs (`jlens.py` l. 141-145 ; `lenses.py` l. 37-45) et du nom de clé `R:dclm` dans `causal_lens_qwen3-8b.json` : fichiers non ouverts (hors de ma consigne) ; seuls les chiffres de V servent de repère.
- Que les lignes non touchées de B soient cohérentes entre elles après les corrections (par exemple que la table des branches de P.4 couvre l'extension de (l) et de (o)) : je n'ai lu que le diff et quelques lignes de contexte, pas B en entier.
- Tout comportement à l'exécution.
