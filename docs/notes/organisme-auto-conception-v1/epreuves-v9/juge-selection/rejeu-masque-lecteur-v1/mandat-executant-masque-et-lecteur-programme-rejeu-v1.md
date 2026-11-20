VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE. AUCUN AFFICHAGE NI AUCUNE LECTURE DU CONTENU D'UNE CARTE, MASQUÉE OU NON.

# Mandat de l'exécutant — masque de style, puis lecteur par programme deux fois, rejeu du juge de sélection — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-24 (R-4150), à partir du projet préparé à la demande de la mère (R-4133).

## Autorisation

- **GO-2026-11-20-24** (`registres/go.md` sur main, ligne 555, copie `ea02d0be…`) : « Un agent neuf, qui ne lit aucune carte, passe le seul fichier `fiches.json` de la course v9 (ba65c411…, sous `archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/`) au masque, puis deux fois au lecteur par programme, selon l'annexe C. Rien n'est affiché ni recopié ; les sorties sont scellées hors du dossier. Troisième exception bornée à la règle de ce dossier. » Mot de Lazar : « R-4133 : a ».
- Pièces scellées sur main, R-4132 : `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/` — `manifeste-rejeu-v1.json` (`a81d30d35c3dad56405e536b901218982b16e2b5f6f82b77b2d84581974d49dd`), `configuration-a-masque-v1.json` (`8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4`), `configuration-b-lecteur-v1.json` (`b44371d235292623e2c51fdd31a68bbabae5402774d5e99860b5a6b90ebdaa6a`), `piece-scellement-manifeste-rejeu-v1.md` (`9e46ac3be599992678670e6728a057c1670bdd23de628ba94d286dbacaa6e2ad`). Lis la pièce de scellement en entier, § « Suite » compris.

## Qui

Un exécutant neuf : tu n'as écrit ni les critères, ni les programmes, ni les configurations, et tu n'as lu aucune carte ni aucun rejeu. Tu ne lis aucune carte : tu lances, tu vérifies les empreintes, tu rends.

## Entrées

- Programmes, pris à leur empreinte, copiés dans `TON_DOSSIER/programmes/` et vérifiés sur la copie : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v4/masque_style_cartes_v1.py` (`07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e`) et `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v5/lecteur_par_programme_cartes_v2.py` (`de99117bb125108ae94a65cc630af304a15c3ce00ebc3036b9c2eca8e969c204`). Si le programme importe un module voisin, copie-le aussi, à son empreinte de la table de la pièce de scellement.
- Les deux configurations : tirées de main par `git show` redirigé vers `TON_DOSSIER/entree/`, empreintes vérifiées.
- Le fichier des cartes : `/home/user/controle-ia-travail/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json` (le seul chemin permis), empreinte attendue `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`. Le seul geste permis sur ce chemin hors des programmes est `test -f`. Tu ne l'ouvres, ne le copies, ne le hashes pas toi-même : les programmes vérifient l'empreinte passée en argument.

## Ce que tu fais, dans cet ordre, une fois chacun, jamais relancé

1. `python3 -B /home/user/controle-ia-travail/scripts/verifier_environnement_agent_v1.py`.
2. Masque : `env -C TON_DOSSIER/programmes python3 -B masque_style_cartes_v1.py --cartes CHEMIN_DES_CARTES ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481 --configuration TON_DOSSIER/entree/configuration-a-masque-v1.json 8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4 --sortie TON_DOSSIER/sorties/masque/SORTIE` (le nom de sortie suit ce que le programme attend ; lis son code avant). Note le code de retour, l'empreinte de la sortie (par `sha256sum` sur le fichier, sans l'ouvrir).
3. Lecteur par programme sur les cartes : `env -C TON_DOSSIER/programmes python3 -B lecteur_par_programme_cartes_v2.py --cartes CHEMIN_DES_CARTES ba65c411… --forme fiches --configuration TON_DOSSIER/entree/configuration-b-lecteur-v1.json b44371d2… --sortie TON_DOSSIER/sorties/lecteur-fiches/SORTIE` (empreintes entières).
4. Lecteur par programme sur la sortie du masque : même commande avec `--cartes SORTIE_DU_MASQUE EMPREINTE_DU_MASQUE --forme masque`, sortie sous `TON_DOSSIER/sorties/lecteur-masque/`.
5. Une étape en refus : tu t'arrêtes, tu ne relances rien, tu rends ce qui existe et le motif écrit par le programme.
6. Chaque sortie reçoit son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`), vérifié par `sha256sum -c`.

Rends un compte rendu `compte-rendu-masque-et-lecteur-programme-rejeu-v1.md` : heure (`date -u`), commandes exactes, codes de retour, empreintes des sorties, messages écran tels quels s'ils ne contiennent aucun contenu de carte (sinon : « message non recopié, contient du contenu »). **Aucune valeur, aucun texte de carte, aucun identifiant de carte.**

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/rejeu-masque-lecteur-programme-v1/` (sorties hors du dépôt et hors de `archives-reponses-modeles/`).

## Interdits

Voir en tête. Aucun autre chemin sous `archives-reponses-modeles/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle ; signe « exécutant neuf, modèle S ». Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
