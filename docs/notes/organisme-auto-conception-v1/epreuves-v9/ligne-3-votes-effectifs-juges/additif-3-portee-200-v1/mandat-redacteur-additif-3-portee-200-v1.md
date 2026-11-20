VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — additif 3 au préenregistrement de la ligne 3 : la puissance de la règle de portée mesurée à 200 témoins, avant l'étage 2 — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur **GO-2026-11-20-26** (R-4150). Écart au texte scellé décidé par Lazar : « la puissance de la règle de portée se mesure à nouveau à 200 avant tout étage payant ». L'additif sera contre-lu, puis scellé par la mère ; le passage sur processeur à 200 et son verdict scellé précèdent toute dépense ; puis l'étage 2 à 200 témoins, au plus 88,36 USD, échéance 2026-11-30.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit ni le préenregistrement, ni ses additifs, ni le code, ni le verdict, ni sa contre-lecture, ni la réflexion sur P3. Tu signes « rédacteur neuf, modèle F ».

## Règle d'aveugle

Tu ne lis aucune mesure de l'étage 1 (ni le fichier de résultat, ni le verdict, ni sa contre-lecture, ni les dossiers `…/execution-etage-1-v1/` et `…/verdict-etage-1-v1/`). Ce que tu sais : verdict « non, pas à cette taille » ; tolérance tenue à 200 et 400, pas à 100 ; puissance qui décide, mesurée dans le monde de puissance à n = 100 : 0,160 ; règle de portée (PR l. 240) déclenchée à 100 ; le texte ne dit rien de la portée à 200 (PR l. 331, 378 ; A1 l. 85).

## Ce qui fait foi (tire de main par `fetch` puis `git show` redirigé ; vérifie chaque empreinte)

- PR `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (`4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0`), en entier : règle de taille (l. 233), monde de puissance et règle de portée (l. 236 à 241), table gelée (l. 311 à 316), étage 2 (l. 305, 331, 343, 378).
- A1 (`e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0`) et A2 (`f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a`), en entier ; ils te donnent la forme d'un additif (A1 : texte complété ; A2 : code, commandes, gardes de lancement).
- DV `prereg/organisme-auto-conception-v9/devis-ligne-3-etage-payant-v7.md` (`382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270`).
- `registres/go.md` sur main, ligne GO-2026-11-20-26 ; cite-la à la lettre.
- Le code : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/code-etage-1-v3/banc_juges_scriptes_ligne_3_v3.py` (`09bfe0db…`), lu pour savoir comment le monde de puissance est tiré et paramétré. **Tu ne le lances pas.**

## Ce que tu écris

`additif-3-preenregistrement-ligne-3-portee-200-v1.md`, dense, qui fixe **avant toute mesure** :
1. **Ce qui est mesuré** : la puissance qui décide, dans le monde de puissance, à n = 200 témoins (même écart planté 0,10, mêmes comparaisons, même correction de Holm, même définition de « la plus basse », mêmes cellules faisables), et rien d'autre ; si d'autres tailles se rapportent, elles ne décident rien.
2. **Les graines** : une racine neuve, dérivée par `SeedSequence`, distincte de 2026111931, 2026111932 et 2026111933, écrite dans l'additif ; aucune graine de l'étage 1 n'est réemployée.
3. **La règle de lecture, gelée** : puissance qui décide ≥ 0,5 à 200 → la règle de portée ne s'applique pas à l'étage 2 à 200 ; sous 0,5, ou une comparaison sans cellule faisable → les comparaisons d'agrégations sont descriptives à l'étage 2 à 200, par la même règle que PR l. 240. Dis ce que chacune des deux issues fait de l'étage 2 (sa taille reste 200 ; la dépense reste sous GO-2026-11-20-26).
4. **Ce que l'étage 2 à 200 hérite du texte** : quelles parties du PR et des additifs valent à 200 sans changement (critères, verdict R13, audit R4), et ce qui doit être dit pour 200 que le texte n'écrit que pour 100 (le relever ligne par ligne ; ne rien trancher qui changerait une hypothèse ou une prédiction : l'écrire en remarque pour Lazar).
5. **Le code** : ce que le banc doit changer pour mesurer à 200 (paramètre, nom neuf, essais, garde « dossier du code propre », chronométrage), à écrire ensuite par un développeur et contre-lu ; les commandes de lancement à la manière d'A2 § 6, laissées en gabarit.
6. **Les gardes et la liste d'arrêt** : exécution unique, aucune relance, aucune lecture avant le manifeste contrôlé par la mère ; verdict par un agent neuf, contre-lu, scellé par la mère.
7. **Ce qui reste un nœud de Lazar.**

Puis un rapport court `rapport-redacteur-additif-3-portee-200-v1.md`. Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-3-ligne-3/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête et la règle d'aveugle. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du banc. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
