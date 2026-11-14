# Consigne de reprise — corrections du code de T0.8, après l'arrêt du premier développeur des corrections — v1

Écrite le 2026-11-14T01:26:12Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A). **Elle ne remplace rien** : la consigne `brouillons/t08-code-compte4-v1/consigne-developpeur-corrections-t08-v1.md` (`e2577b5a0a2e60a6108e4436660beb9d6e8967fd65056958ef9be48a4f7c778b`) s'applique en entier, interdits compris ; cette page ne dit que l'état où tu reprends.

## 1. Ce qui s'est passé

Le conteneur de la session a redémarré vers 01:25 UTC ; le développeur des corrections (modèle A, sous-agent de cette session, lancé vers 00:50 UTC) s'est arrêté sans rendu. Relevé de la session à la reprise :
- il a poussé un **jalon 1**, `61fbe4f06df5fe6e5bc1e16f653a4777882ea4ea` sur `prep/t08-code-compte4-v1` (tête distante égale), dont le message nomme CLT8C-01 à -08, -10, -11, -13 à -20 ; 15 fichiers changés sous `src/controle_ia/t08/` et `tests/test_t08_*` ;
- il laisse dans l'arbre une **modification non committée** de `src/controle_ia/t08/course_v1.py` (fonction `exiger_run_7b` tirée d'un contrôle en ligne, CLT8C-05) ;
- **aucun** essai de bout en bout sous `essai/t08-jouet-compte4-v2/`, **aucun** rapport des corrections.

## 2. Qui tu es

Développeur **neuf**, sous-agent de la session du compte 4, modèle A : tu reprends le travail d'un autre développeur ; tu n'as écrit ni le code de T0.8, ni sa contre-lecture, ni T0.8, ni T0.6, T0.7 ou P3-bis. Exclu ensuite de la vérification des corrections et du verdict de T0.8.

## 3. Ce que tu fais, dans cet ordre

1. Vérifie l'empreinte des deux consignes, lis la consigne des corrections en entier (et ce qu'elle te donne à lire).
2. Relève l'état : `git -C /home/user/t08-code-compte4-v1 log`, `diff 27c09264 61fbe4f0`, `diff` de l'arbre ; pour **chacun** des 21 constats, dis s'il est traité au jalon 1 (fichier:ligne, essai sain et artefact) ou non. Ne te fie pas au message de commit : vérifie sur le code et les essais.
3. La modification non committée : relis-la ; garde-la si elle est juste, avec son essai sain et artefact ; sinon retire-la par `git -C /home/user/t08-code-compte4-v1 checkout -- src/controle_ia/t08/course_v1.py` ; dis ce que tu as fait.
4. Termine ce qui manque (constats non traités ou sans essai, CLT8C-09 compris), puis les essais du § 4 de la consigne des corrections (fichiers d'essais nommés, essai de bout en bout deux fois sous `essai/t08-jouet-compte4-v2/a` et `…/b`, cas du registre absent du disque).
5. Rapport `docs/notes/t08-code-compte4-v1/rapport-developpeur-corrections-t08-v1.md`, sections de la consigne des corrections ; sa section **0. Identité** dit l'interruption, le jalon 1 écrit par le développeur arrêté, ce que tu as relu, gardé, changé ou retiré. Scellé, committé, poussé.

Commits et poussées à chaque jalon, comme le dit la consigne des corrections. Si ton quota ou ton temps s'épuise : commite et pousse ce qui est fait, avec un rapport partiel scellé qui dit ce qui reste.
