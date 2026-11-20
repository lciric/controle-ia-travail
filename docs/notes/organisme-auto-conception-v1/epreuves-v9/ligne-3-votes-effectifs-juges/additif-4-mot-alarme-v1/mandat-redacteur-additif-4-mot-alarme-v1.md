VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — additif 4 au préenregistrement de la ligne 3 : règle de mot de la carte de l'alarme, jouée sur graines neuves — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur **GO-2026-11-20-30** (R-4164 ; mot de Lazar « go a puis b », relu à la source par la mère). (a) La carte de l'alarme (`fcbf4a2dd1a57`) reste « mesurée, sans mot » au verdict scellé de l'étage 1. (b) Une règle de mot est écrite et scellée **avant toute mesure**, puis jouée une fois sur graines neuves, sur processeur, sans dépense. L'additif sera contre-lu par un agent neuf d'un autre modèle, puis scellé par la mère.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit ni le préenregistrement, ni ses additifs, ni le code, ni le verdict de l'étage 1, ni sa contre-lecture, ni l'additif 3. Tu signes « rédacteur neuf, modèle F ».

## Règle d'aveugle (la plus importante)

**Tu ne lis aucune mesure de l'étage 1**, et en particulier **aucune valeur mesurée de l'alarme** : ni le fichier de résultat, ni le verdict (scellé ou non), ni ses contre-lectures, ni la lecture des prédictions, ni aucun fichier des dossiers `…/ligne-3-votes-effectifs-juges/execution-etage-1-v1/` et `…/ligne-3-votes-effectifs-juges/verdict-etage-1-v1/`, ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`. Tu ne cherches pas dans les registres ce que l'étage 1 a mesuré. Une règle écrite après avoir vu les mesures ne serait plus un préenregistrement (R1, R3). Si tu tombes par mégarde sur une valeur mesurée de l'alarme, arrête-toi et dis-le.

## Ce qui fait foi (tire de main par `fetch`, puis `git show` redirigé ; vérifie chaque empreinte)

- PR `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (`4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0`), en entier : le bras de l'alarme (l. 228), ses critères (l. 185), la prédiction P6 (l. 141), la lecture de l'étage 1 (l. 318), la réserve 11 (l. 402), et ce que la carte `fcbf4a2dd1a57` revendique (cherche-la par son identifiant dans ce seul fichier).
- A1 `prereg/organisme-auto-conception-v9/additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md` (`e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0`), en entier : la règle du silence 2 (l. 101 à 112), les définitions (a) et (b) des parts (l. 90 à 99).
- A2 `prereg/organisme-auto-conception-v9/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md` (`f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a`) : l'aide de l'alarme, la garde du mélange planté, la forme d'un additif de code.
- `registres/go.md` sur main, ligne GO-2026-11-20-30 ; cite-la à la lettre.
- Le banc : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/code-etage-1-v3/banc_juges_scriptes_ligne_3_v3.py` (`09bfe0db…`), lu pour savoir comment le bras de l'alarme est tiré et ce qu'il mesure. **Tu ne le lances pas.**

## Ce que tu écris

`additif-4-preenregistrement-ligne-3-mot-alarme-v1.md`, dense, qui fixe avant toute mesure :
1. **Ce que la carte revendique**, à sa lettre, et donc ce que « tient sur le banc », « réfuté sur le banc » et « sans prise » veulent dire pour elle (les trois mots de PR l. 318).
2. **La règle de mot**, mécanique, sur comptes entiers : seuils de fausse alarme (le niveau gelé 0,05 et la borne 0,08 du texte servent de point d'appui ; toute autre valeur se justifie avant mesure), de détection contre le bras apparié à coût égal, de délai, et de part des alarmes à effet ; à quels m (10, 20, 40) ; ce qui fait « sans prise » (par exemple un banc qui ne distingue pas les bras). Chaque seuil avec sa raison, écrite **sans référence à une mesure** ; si une raison demande un calcul, fais-le par calcul exact ou approché sur les lois du banc (programme dans ton dossier, sans lancer le banc), versionné.
3. **Une puissance calculée d'avance** : avec 2 000 suites par cellule, quelle chance la règle a-t-elle de dire « tient » si la carte vaut ce qu'elle revendique, et « réfuté » si elle ne le vaut pas ? Si la puissance est faible, dis-le, et propose une taille.
4. **Les graines** : une racine neuve dérivée par `SeedSequence`, distincte de toutes les racines déjà employées par la ligne 3 (2026111930 à 2026111937, 2026112031 à 2026112033), écrite dans l'additif.
5. **Ce qui est joué** : le seul bras de l'alarme, à la lettre du texte (suites, changements, mélange planté), rien d'autre ; la garde du mélange planté avant toute lecture.
6. **Le code** à écrire ensuite (développeur, contre-lu) : mode « alarme seule » sous un nom neuf, essais, garde « dossier du code propre », chronométrage ; commandes de lancement en gabarit.
7. **Lecture** : verdict par un agent neuf (R13), contre-lu, scellé par la mère ; audit de symétrie (R4) ; aucune relance.
8. **Ce que le mot dit et ne dit pas** : il porte sur la carte au banc scripté, jamais sur de vrais juges (réserve 11) ; il ne touche pas P6 ni le verdict scellé de l'étage 1.
9. **Ce qui reste un nœud de Lazar.**

Puis un rapport court `rapport-redacteur-additif-4-mot-alarme-v1.md` (pièces, calculs, points laissés à Lazar). Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-4-ligne-3/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête et la règle d'aveugle. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du banc. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
