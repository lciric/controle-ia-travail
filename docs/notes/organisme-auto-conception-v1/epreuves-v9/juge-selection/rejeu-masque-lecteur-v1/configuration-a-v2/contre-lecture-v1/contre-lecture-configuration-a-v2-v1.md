# Contre-lecture — configuration A v2 du masque de style, rejeu du juge de sélection — v1

Contre-lecteur neuf, modèle O : je n'ai écrit ni les critères, ni la configuration A v1 ou v2, ni le masque v1 ou v2, ni sa contre-lecture. Écrit le 2026-11-20 (`date -u` : 2026-11-20T10:14:08Z). Python 3.13.18. Processeur seul, aucune dépense, aucun appel de modèle. Aucune carte ouverte ; aucun chemin sous `archives-reponses-modeles/` touché, par aucune commande. Aucune écriture dans le dépôt, aucun commit. Mandat : `mandat-contre-lecteur-configuration-a-v2-v1.md` (`1889b1ae5e5bb2ae0a1c52eaea1e20a93591be07cf68cf6688481aa81fca99b0`, égal à son compagnon).

## Verdict : Conforme, à sceller

La configuration A v2 (`a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54`) est la v1 plus une seule clé, et ses nombres attendus égalent le résultat des noms de clés. Elle sert GO-2026-11-20-36 (1), option (a), et ne sort de la règle de masquage de GO-2026-11-20-10 (O2) que par ce que GO-36 accorde. **Aucune correction de la configuration.** La mère la scelle avec le masque v2, et écrit à la pièce de scellement les textes du § 3.1. Les textes du § 3.2 vont à la proposition du rejeu. Le § 4 donne le mandat neuf de l'exécutant.

## 0. Empreintes vérifiées (toutes égales à leur compagnon ou à l'empreinte citée)

- Dossier C : `configuration-a-masque-v2.json` (`a6c5d87b…`) ; `proposition-configuration-a-v2-v1.md` (`2f6ef529445bae369fa17312ab16285ac0e9df5bcf12b27a9f57c6a24333fa36`) ; `ecrire_configuration_a_v2_v1.py` (`400e21fb…`) ; `sortie-validation-configuration-a-v2-v1.txt` (`5784d27f…`) ; `mandat-redacteur-configuration-a-v2-v1.md` (lu pour trouver les chemins).
- `C/masque-v2/` : `masque_style_cartes_v2.py` (`769aace5b64c697799b76a0120a5c2926c75798a388c93fa00ddc93224401c01`) ; `rapport-developpeur-masque-v2-v1.md` (`92c9f0b8…`) ; `contre-lecture-masque-v2-v1.md` (`7a2cf0e55e2d4bf03202c69ee9106ebd6245abe2efac70f1f3a7512f023e92d3`).
- `jeu-noms-cles-v1/noms-cles-contenu-hors-champs-v1.json` (`86aecdee84f82003c7a16e8be7acc9fb030adaab2a7ea44db9fa6b2d29a2f5b6`).
- Tirés de `main` (`fetch`, puis `git show FETCH_HEAD:… >`, commit `9143abee`) : configuration A v1 (`8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4`) ; pièce de scellement (`9e46ac3be599992678670e6728a057c1670bdd23de628ba94d286dbacaa6e2ad`) ; manifeste (`a81d30d35c3dad56405e536b901218982b16e2b5f6f82b77b2d84581974d49dd`) ; configuration B (`b44371d235292623e2c51fdd31a68bbabae5402774d5e99860b5a6b90ebdaa6a`) ; critères v7 (`6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f`) ; note v7 (`bbd71b7c998866ec249556fe7803015c54aac4081dffc4e5084588819bc98a26`) ; `registres/go.md` (copie `21f8f184…`).
- Dans le dépôt, à leur compagnon : masque v1 (`07ed8725…`) ; lecteur par programme v2 (`de99117b…`) ; programme d'assemblage v2 (`2f5640da…`) ; rapport v7 (`2a12a78f…`) ; mandat de l'exécutant du premier jeu (`bae4b1a830f93e63c23c99a113726f9cec9e5ce19737b0fd2b29b0d482c8a06d`) ; son compte rendu (`e13da23c09f7ce783a08ef64bd4fdfb3ccfa2f2510185ede0fd4e8e29a6dc5b5`).

**Les lignes de GO, à la lettre** (`registres/go.md` de `main`) :

> GO-2026-11-20-10 | … | (O2) Juge, critères v7 : en tête (1) et (3) ; décision 1 (a) ; 2 (a) ; 3 (b) au rejeu et (a) en course ; 4 (b) ; 5 (a) au rejeu ; huit confirmations telles qu'écrites. […]

> GO-2026-11-20-24 | 2026-11-20 | décision | **Juge de sélection, rejeu, option (a) de R-4133.** Un agent neuf, qui ne lit aucune carte, passe le seul fichier `fiches.json` de la course v9 (ba65c411…, sous `archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/`) au masque, puis deux fois au lecteur par programme, selon l'annexe C. Rien n'est affiché ni recopié ; les sorties sont scellées hors du dossier. Troisième exception bornée à la règle de ce dossier.

> GO-2026-11-20-28 | 2026-11-20 | décision | **Juge de sélection, rejeu, option (a) de R-4153.** Un agent neuf, qui ne lit aucune carte, lit par un programme contre-lu les seuls noms de clés de `contenu` du seul fichier `fiches.json` de la course v9 (ba65c411…, sous `archives-reponses-modeles/`). Le programme ne rend que les noms hors des dix champs, avec le nombre de cartes qui portent chacun, sans valeur ni identifiant. Une configuration A v2 en est tirée et scellée, puis le masque repart sous GO-2026-11-20-24. Quatrième exception bornée à la règle de ce dossier.

> GO-2026-11-20-36 | 2026-11-20 | décision | **« go recos » sur les recommandations pendantes de la mère.** (1) Rejeu du juge : les trois clés hors champs masquées, option (a), masque v2 codé, contre-lu, configuration A v2 scellée, masque relancé sous GO-2026-11-20-24. […]

## 1. La différence v1 → v2

Programme `verifier_configuration_a_v2_v1.py` (`9892cad5ba32bd6ba7cfda95b03ed1bc5ffce5891eb50de2efdb9812cc8c8f19`), écrit par l'outil d'écriture de fichiers dans mon dossier, lancé par son chemin. Il vérifie chaque entrée à son empreinte. Il charge les deux masques pour leur seule fonction `valider_configuration`, sur aucune carte. Sortie : `sortie-verification-configuration-a-v2-v1.txt` (`9ba69caabac49ce3f229840adcce5bfcaa20ceef1d7ab3ef9e936bdf4e547ac5`). **32 contrôles, 32 passés.**

- La v1 et la v2 se relisent et se réécrivent à l'octet, sous la même forme (`indent=1`, `ensure_ascii=False`, fin de ligne).
- La v2 compte huit clés. Ses clés moins celles de la v1 donnent `{cles_hors_champs_retirees}`, et aucune clé de la v1 ne manque. Les sept clés de la v1 sont égales, valeur, type et texte JSON compris, et gardent leur ordre ; la clé neuve vient en dernier.
- `cles_hors_champs_retirees` = `{"_": 2, "cout_note": 1, "epreuve_hors_ligne": 1}`. C'est exactement le résultat des noms de clés, qui a été calculé contre la configuration A v1 (`8a8548d1…`) et sur le fichier de GO-24 (`ba65c411…`). Les nombres sont des entiers d'au moins 1. Aucun nom n'est un champ, ni `meta`, ni `empreinte`. `hors_choix` est vide : les nombres portent sur les 94 cartes, celles du résultat.
- Les cartes porteuses sont **de deux à quatre** (`_` à elle seule en porte deux).
- Le masque v2 accepte la v2 ; le masque v1 la refuse (« clés attendues … », comme dans la sortie du rédacteur) ; le masque v2 accepte la v1. `CLE_RETIREES` du masque v2 égale le nom de la clé, et ses sept clés de base sont celles du v1.
- Les trois champs de la configuration B sont parmi les dix, et aucun n'est retiré.

Le programme du rédacteur (`400e21fb…`), lu en entier, ne fait que ce qu'il dit. Il vérifie les trois entrées à leur empreinte, refuse un résultat qui n'a pas été calculé contre la v1, ajoute une seule clé et écrit sans écraser. Sa sortie concorde avec la mienne.

## 2. Fidélité à GO-2026-11-20-36 (1) et à l'option (a)

- **« les trois clés hors champs masquées, option (a) »** : les trois noms sont retirés de la forme masquée, avec le nombre attendu de chacun pour garde (R5), et rien d'autre. Le masque v2 les retire avant le contrôle « clé hors des champs » (l. 124-128). Seule leur présence est comptée : leur valeur n'est pas lue. Une autre clé hors des champs reste un refus (l. 128-130), et un compte faux aussi (l. 141-145).
- **Rien ne sort de la règle de masquage de GO-10 (O2), décision 5 (a)** (« ordre fixe, gras, intertitres et formules retirés, champs coupés à la médiane », note v7, l. 335). L'ordre et la liste des dix champs, le plafond `mediane`, les formules, les intertitres, le seuil 0,2 et le minimum 3 (confirmation 8), et `hors_choix` sont égaux à la v1. Les clés retirées n'entrent ni dans le calcul des médianes ni dans la recherche des phrases récitées, qui ne portent que sur les dix champs (`masquer`, l. 265-271). La forme masquée des dix champs est donc celle que le masque v1 aurait rendue sur des cartes sans ces clés.
- **Ce que GO-36 accorde au-delà de GO-10, et seulement cela** : (i) un programme neuf, `masque_style_cartes_v2.py`, au lieu du `masque_style_cartes_v1.py` scellé avec les critères (critères v7, l. 3 : « Aucun programme ne change » ; l. 11) ; (ii) une liste de clés à retirer tirée d'un programme qui a lu les seuls noms de clés des cartes (GO-28), et non de la seule consigne (critères v7, § 1, l. 41 : « sans ouvrir une carte » ; rapport v7, § 5, l. 64) ; (iii) une troisième ligne d'`en_tete` qui nomme les trois clés et leurs nombres (proposition, option (a) : « un masque v2 qui les nomme et les compte » ; § 3, point 4). Les trois sont des écarts aux critères scellés, que Lazar a accordés. Ils doivent être écrits à la pièce de scellement et dans la proposition du rejeu (§ 3).
- **Le manifeste** (`a81d30d3…`) ne cite ni la configuration A ni le masque. Il ne change pas, et ses seize clés restent valides. L'assemblage et les gardes ne lisent ni la pièce du masque ni la configuration A. La commande `gardes` contrôle `forme_lue` dans les sorties du lecteur par programme (assemblage, l. 1192), et la sortie du masque v2 garde la forme que lit le lecteur (`id`, `champs`).
- **Nœud tranché.** La proposition est écrite « sous réserve du nœud » et dit « aucun défaut » ; GO-36 (1) tranche ce nœud par l'option (a). La pièce de scellement doit le dire (texte T1).

## 3. Les réserves de la proposition et les remarques de la contre-lecture du masque v2

| point | à la pièce de scellement | à la proposition du rejeu |
|---|---|---|
| Réserve 1 — le lecteur par programme en forme « fiches » lit les trois clés | oui (T4) | oui (P2), texte précisé |
| Réserve 2 — symétrie, phrase des cartes qui perdent une clé | oui (T5) | oui (P3), texte corrigé : « de deux à quatre », « aucun des deux lecteurs » |
| Réserve 3 — le masque v2 peut encore refuser (champ absent, champ non textuel) | oui (T6) | non (sans objet si le masque passe ; s'il refuse, il n'y a pas de proposition) |
| Réserve 4 — sens de « masquée » et « écartée » | oui (T3), parce que GO-36 emploie « masquées » | non |
| Réserve 5 — configuration B inchangée | oui, une ligne (T2) | non |
| Contre-lecture S, remarque 1 — « à l'octet » | oui (T7) | non |
| Remarque 2 — en-tête de trois lignes | oui (T8) | non |
| Remarque 3 — compte sur les cartes ouvertes | oui, dans T2 | non |
| Remarque 5 — message du refus de compte | oui (T9) : couvert par la sorte d'information de GO-28 | non |
| Remarques 4 et 6, remarques facultatives | non | non |
| Écarts aux critères (§ 2, (i) à (iii)) et premier jeu en refus | oui (T1) | oui (P1), dans « Les écarts à ces critères, non corrigés » (critères v7, § 11, l. 273) |

Sur la réserve 1 : le lecteur par programme ne joint que les valeurs **textuelles** de `contenu` (l. 168, `isinstance(v, str)`). Seul le « oui » cherché dans tout le texte peut en dépendre (l. 175). Le « non » est lu sur `ce_qui_la_refuterait` seul (l. 167, 172) et la voie sur `titre` et `mecanisme` (l. 177) : ni l'un ni l'autre n'en dépend. « Indécidable » ne tient qu'au champ de réfutation vide et n'en dépend pas non plus. La réserve est juste, mais plus étroite que ne la dit la proposition.

Sur la réserve 2 : la proposition dit « quatre cartes au plus ». Le juste est « de deux à quatre ». Elle dit aussi « que personne n'a lue », alors que le lecteur par programme, en forme « fiches », en lit les mots ; il faut écrire « qu'aucun des deux lecteurs n'a lue ».

### 3.1 Textes exacts à porter à la pièce de scellement

La pièce v1 (`9e46ac3b…`) est scellée et n'est pas réécrite. Je propose une pièce neuve : `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/piece-scellement-configuration-a-v2-masque-v2-v1.md`. Elle porte à sa table la configuration A v2 (`a6c5d87b…`), le masque v2 (`769aace5…`), ses essais (`7c84260f3fabe5ebcf7a9ea8447cf94dd462710755055026a44194282be14b71`, empreinte citée d'après le rapport du développeur et la contre-lecture S, non recalculée par moi), la proposition (`2f6ef529…`) et cette contre-lecture. Elle dit que la configuration A v1 et la pièce v1 restent scellées et inchangées (R12). Puis, mot pour mot :

**T1.** « Écarts aux critères v7 accordés par Lazar. GO-2026-11-20-36 (1) tranche le nœud de la proposition de la configuration A v2 (`2f6ef529…`) par l'option (a) : la réserve « sous réserve du nœud » est levée. Il en résulte trois écarts aux critères v7 scellés, accordés : (i) le masque joué est `masque_style_cartes_v2.py` (`769aace5…`), non `masque_style_cartes_v1.py` (en-tête, l. 3 et l. 11) ; (ii) la liste des clés retirées de la configuration A v2 est tirée, sous GO-2026-11-20-28, d'un programme qui a lu les seuls noms de clés de `contenu`, et non de la seule consigne (§ 1, l. 41) ; l'ordre et la liste des dix champs restent ceux de la consigne ; (iii) la troisième ligne de l'en-tête des cartes masquées nomme les trois clés retirées et leurs nombres. Le masque v1 a été joué une fois sous GO-2026-11-20-24 et a refusé sans rien écrire (compte rendu `e13da23c…`) ; le jeu suivant est le second sous GO-2026-11-20-24, relancé par GO-2026-11-20-36 (1). »

**T2.** « La configuration A v2 est la v1 plus la seule clé `cles_hors_champs_retirees` = `{"_": 2, "cout_note": 1, "epreuve_hors_ligne": 1}`, égale au résultat des noms de clés (`86aecdee…`) ; les sept autres clés sont égales à la v1, vérifié par programme. `hors_choix` est vide : les nombres attendus portent sur les 94 cartes. La configuration B (`b44371d2…`) et le manifeste (`a81d30d3…`) ne changent pas : les trois champs de B sont parmi les dix ; le manifeste ne cite ni la configuration A ni le masque. »

**T3.** « « Masquée » se lit ici, comme dans GO-2026-11-20-36 (1) : retirée de la forme masquée seule, que lisent les deux lecteurs et le lecteur par programme en forme « masque ». La carte non masquée, que lit le lecteur par programme en forme « fiches », reste telle qu'elle est (critères v7, § 1, l. 46). »

**T4.** « Le lecteur par programme, en forme « fiches », lit encore les trois clés quand leur valeur est un texte (`de99117b…`, l. 168 et 175). Sur les cartes qui les portent, et sur elles seules, le « oui » du critère D peut donc tenir à une clé que la forme masquée n'a plus, et une baisse de D sous le masque peut venir de ce retrait plutôt que de la coupe. Le « non », la voie et le compte « devenu indécidable » n'en dépendent pas. »

**T5.** « De deux à quatre cartes perdent, sous le masque, une clé hors des dix champs, qu'aucun des deux lecteurs ne lira et dont personne ne connaît le contenu. Retirer une clé peut desservir la carte qui la porte ; la montrer aurait pu la servir ou la signaler (règle R4). »

**T6.** « Le masque v2 peut encore refuser sur les cartes : si l'un des dix champs manque à une carte ou n'est pas un texte (l. 131-134), ou si une autre clé hors des champs s'y trouve. Le résultat des noms de clés ne dit rien des deux premiers cas. Un refus arrête le jeu : rien n'est relancé, la mère décide. »

**T7.** « Sans la clé neuve, le masque v2 rend la sortie du v1, aux deux seules valeurs près qui diffèrent par nature : le nom de la pièce et l'empreinte du programme. C'est la lecture de « à l'octet » que vérifient les essais (55 réussis, rejoués par la contre-lecture du masque v2). »

**T8.** « La troisième ligne de `en_tete` nomme les trois clés, leurs nombres et l'empreinte de la configuration. Elle ne désigne aucune carte. Les deux lecteurs la liront avec les deux premières : c'est ce que l'option (a) prévoit, et ce que les critères demandent de dire d'avance (§ 1, l. 42). Le lecteur par programme ne lit pas `en_tete`. »

**T9.** « Un refus de compte n'écrit à l'écran que le nom d'une clé, le nombre trouvé et le nombre attendu, sans identifiant ni valeur. C'est la sorte d'information que rend GO-2026-11-20-28 : il se recopie au compte rendu. »

### 3.2 Textes exacts à porter à la proposition du rejeu

**P1** (dans « Les écarts à ces critères, non corrigés », critères v7, § 11, l. 273) : « Le masque joué est `masque_style_cartes_v2.py` (`769aace5…`), avec la configuration A v2 (`a6c5d87b…`), et non le masque v1 scellé avec les critères. Cet écart a été accordé par GO-2026-11-20-36 (1), après le refus du masque v1 au premier jeu. La configuration A v2 retire de la forme masquée trois clés de `contenu` hors des dix champs, dont la liste a été tirée, sous GO-2026-11-20-28, des seuls noms de clés des cartes : `_` (deux cartes), `cout_note` (une), `epreuve_hors_ligne` (une). L'ordre et la liste des dix champs restent ceux de la consigne. »

**P2** (à côté du compte « D baisse sous le masque » de la commande `gardes`, critères v7, § 1, l. 42) : « Sur les deux à quatre cartes qui portent une clé retirée, et sur elles seules, une baisse de D entre la forme non masquée et la forme masquée peut venir du retrait de la clé et non de la coupe. En effet, le lecteur par programme en forme « fiches » cherche le « oui » dans toutes les valeurs textuelles de `contenu`, les trois clés comprises. Le « non », la voie et le compte « devenu indécidable » n'en dépendent pas. Ces cartes ne sont pas connues, et le compte n'est pas corrigé. »

**P3** (règle R4, à côté de P1) : « De deux à quatre cartes ont perdu, sous le masque, une clé hors des dix champs, qu'aucun des deux lecteurs n'a lue et dont personne ne connaît le contenu. La perte peut desservir la carte qui la porte, comme sa présence aurait pu la servir ou la signaler. »

## 4. Le jeu à venir sous GO-2026-11-20-24 : le mandat neuf de l'exécutant

Le mandat neuf est copié de `mandat-executant-masque-et-lecteur-programme-rejeu-v1.md` (`bae4b1a8…`) sous le nom **`mandat-executant-masque-v2-et-lecteur-programme-rejeu-v1-second-jeu-v1.md`**, dans le même dossier. Je ne propose pas « rejeu-v2 », qu'on confondrait avec le rejeu v2 des critères. Le premier mandat reste tel quel. Changements, texte ancien → texte neuf :

1. **Bandeau de tête** : ajouter à la fin, après « AUCUN AFFICHAGE NI AUCUNE LECTURE DU CONTENU D'UNE CARTE, MASQUÉE OU NON. » : « LE CODE DE RETOUR SE LIT DANS LE RETOUR DE L'OUTIL, JAMAIS PAR `; echo`. `git show` REDIRIGÉ PAR `>`, JAMAIS PAR `--output=`. » Ce sont les deux incidents du premier jeu (compte rendu `e13da23c…`, « Écarts à signaler »).
2. **Titre** : « # Mandat de l'exécutant — masque de style, puis lecteur par programme deux fois, rejeu du juge de sélection — v1 » → « # Mandat de l'exécutant — masque de style v2, puis lecteur par programme deux fois, rejeu du juge de sélection, second jeu — v1 ».
3. **Ligne d'origine** : « … sur GO-2026-11-20-24 (R-4150), à partir du projet préparé à la demande de la mère (R-4133). » → « … sur GO-2026-11-20-24 (R-4150) et GO-2026-11-20-36, point (1). Le premier jeu (mandat `mandat-executant-masque-et-lecteur-programme-rejeu-v1.md`, `bae4b1a830f93e63c23c99a113726f9cec9e5ce19737b0fd2b29b0d482c8a06d`) s'est arrêté au masque v1, sur un refus, sans rien écrire. »
4. **Autorisation** : après la citation de GO-24, ajouter : « - **GO-2026-11-20-36**, point (1) (`registres/go.md` sur main, ligne 567) : « (1) Rejeu du juge : les trois clés hors champs masquées, option (a), masque v2 codé, contre-lu, configuration A v2 scellée, masque relancé sous GO-2026-11-20-24. » » Dans la liste des pièces scellées, remplacer « `configuration-a-masque-v1.json` (`8a8548d1…`) » par « `configuration-a-masque-v2.json` (`a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54`) », et ajouter la pièce neuve qui la scelle avec le masque v2, à son empreinte. Remplacer « Lis la pièce de scellement en entier, § « Suite » compris. » (la pièce v1 n'a pas de § « Suite ») par « Lis en entier les deux pièces de scellement : celle du manifeste (v1) et celle de la configuration A v2 et du masque v2. »
5. **Qui** : ajouter : « Tu n'as pas joué le premier jeu. »
6. **Entrées, programmes** : remplacer « `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v4/masque_style_cartes_v1.py` (`07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e`) » par « le masque v2, au chemin où la mère le scelle (`CHEMIN_DU_MASQUE_V2`, à écrire en entier par la mère), `masque_style_cartes_v2.py` (`769aace5b64c697799b76a0120a5c2926c75798a388c93fa00ddc93224401c01`) ». Le lecteur par programme reste inchangé (`de99117b…`).
7. **Entrées, configurations** : « Les deux configurations : tirées de main … » → « Les deux configurations, tirées de main par `git show` redirigé vers `TON_DOSSIER/entree/`, empreintes vérifiées : `configuration-a-masque-v2.json` (`a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54`), au chemin où la mère la scelle, et `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-b-lecteur-v1.json` (`b44371d235292623e2c51fdd31a68bbabae5402774d5e99860b5a6b90ebdaa6a`). »
8. **Étape 2** : « Masque : `env -C TON_DOSSIER/programmes python3 -B masque_style_cartes_v1.py … --configuration TON_DOSSIER/entree/configuration-a-masque-v1.json 8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4 …` » → « Masque : `env -C TON_DOSSIER/programmes python3 -B masque_style_cartes_v2.py --cartes CHEMIN_DES_CARTES ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481 --configuration TON_DOSSIER/entree/configuration-a-masque-v2.json a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54 --sortie TON_DOSSIER/sorties/masque/SORTIE` ». Le reste de l'étape ne change pas.
9. **Après l'étape 2, une ligne neuve (compte par clé)** : « Le code 0 vaut compte par clé vérifié, car le masque v2 refuse si le nombre de cartes qui portent une clé retirée diffère du nombre attendu. Tu n'ouvres pas la sortie pour lire son en-tête. Au compte rendu, tu écris : « Clés retirées de la forme masquée, nombres attendus de la configuration A v2, vérifiés par le masque v2 (code 0) : `_` 2 ; `cout_note` 1 ; `epreuve_hors_ligne` 1 ; compte par clé, jamais par carte. » Un refus de compte (nom de la clé, nombre trouvé, nombre attendu, aucun identifiant) se recopie tel quel ; tout autre refus du masque aussi, s'il ne contient aucun contenu de carte. »
10. **Étapes 3 à 6** : inchangées. La sortie que lit l'étape 4 est celle du masque v2.
11. **Compte rendu** : « Rends un compte rendu `compte-rendu-masque-et-lecteur-programme-rejeu-v1.md` » → « Rends un compte rendu `compte-rendu-masque-v2-et-lecteur-programme-rejeu-v1-second-jeu-v1.md` ».
12. **Ton dossier** : un dossier neuf, donné par la session, **distinct** de `…/rejeu-masque-lecteur-programme-v1/` (on n'écrase jamais, R12), hors du dépôt et hors de `archives-reponses-modeles/`.

## 5. Écarts, incidents

- Le premier `git fetch origin main` a rendu le code 1 (« cannot lock ref 'refs/remotes/origin/main' », référence mise à jour en même temps par une autre session). Je l'ai relancé une fois, avec le code 0. `FETCH_HEAD` = `9143abee`, et toutes les pièces tirées de `main` ont l'empreinte attendue. Seule la référence `FETCH_HEAD` du dépôt local a été écrite.
- Le mandat demandait de lire « la pièce de scellement et le manifeste du rejeu que cite la proposition, les critères v7 et la note v7 (chemins tirés de la proposition, § 5) ». Le § 5 de la proposition ne donne que des empreintes : j'ai pris les chemins dans le mandat du rédacteur (dossier C, à son compagnon) et dans la table de la pièce de scellement. J'ai aussi tiré la configuration B, pour la réserve 5.
- J'ai fait deux recherches de motif, chacune sur un seul fichier nommé (la copie de `registres/go.md` pour les quatre lignes de GO ; le programme d'assemblage pour ce qu'il lit du masque), et non sur un dossier. Je n'ai lancé aucune commande de liste, aucun heredoc, aucun code en ligne.
- Je n'ai pas recalculé l'empreinte des essais du masque v2 (`7c84260f…`) : ils ne sont pas dans les pièces du mandat.
- Aucun refus de permission, de classifieur ni de garde.

*contre-lecteur, modèle O*
