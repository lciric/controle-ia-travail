# Addendum 2 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — condition de lancement 6 mise à jour : code v13, arrêt autonome de l'instance

11 novembre 2026, scellé vers 16:16 UTC (brouillon 1 relu ; brouillon 2, corrections K-1 à K-7, 16:15 UTC). Session « attaquant informé » successeur (`session_013QMaykGXY4fZmZNX5fm1K4`), branche
`claude/compassionate-meitner-d4ryyk`. Le préenregistrement scellé et son addendum 1
(`prereg/temoin-attaque-publiee-bailey-v1-addendum-1-condition6.md`, `6f7eda73…`, déposé chez le tiers, manifeste v4,
2026-11-11T15:46:02Z) restent tels quels (R12) ; en cas de conflit, le préenregistrement prime et l'écart est un nœud.
Cet addendum **remplace, pour la condition 6, le code et les lectures** donnés par l'addendum 1 ; tout le reste de
l'addendum 1 vaut toujours. Il ne contient aucun résultat.

## 1. Pourquoi

Décision de Lazar, option (b) (`registres/passations/2026-11-11-1226-decision-lazar-option-b-arret-autonome.md`,
`fb6f6032…`) : le pilotage du run part de ce conteneur, qui peut être repris pendant les deux à trois jours du run ; pour
qu'aucune instance ne reste facturée au taux de la carte sans pilotage, **l'instance s'arrête elle-même**. En route, un
défaut du code de l'addendum 1 a été trouvé et corrigé : la destruction était appelée sans `-y`, et `vastai` 1.11.0, sans
terminal, répond « Aborted. » avec un code de succès — la destruction aurait été tenue pour faite.

## 2. Commit et code

**Commit du code : `4988f3f442c670887a0e8ad15ddfbac68a173d03`** (11 novembre 2026, 15:55:33 UTC). Modules du run,
`src/controle_ia/temoin_bailey/` (SHA-256) :

| Rôle | Module | SHA-256 |
|---|---|---|
| Lanceur local (conduite, veilleurs, transfert, destruction, reprise) | `lanceur_v13.py` | `9257266f31d1f6f915b24db5dc66d5e9a7c7404b517c8980294de83241181185` |
| Lanceur côté instance (dont le chien de garde) | `instance_v12.py` | `de46698656b56cc52389c6150af50da7d4aa6ac5120e78561bc2db1b6155086d` |
| Lecture | `lecture_v8.py` | `1657a492d7229a9f3cd37c2094a012cf2cb629d8e7e6b91632895586e9d9a00a` |
| Exécution du code public | `execution_v3.py` | `279f1f4f6e04fad67db457831abdba712d16feb15571c24173988af9a1a58a5f` |
| Journaliseur | `journaliseur_v3.py` | `9f75407c0afaab4c605fb4ab758df214c91f4ce5df6c86f15dc93db04996be90` |
| Conventions | `conventions_v3.py` | `51c2fa26a4e61038b14c97825618e2006be9572c9f82d67a2d5e26bea2bbca86` |
| Analyse | `analyse_v3.py` | `c28c6821629a6d4eec657c376a3df2d5361de2e46c4441361f43e0e8f423f2ca` |

Fichiers envoyés sur l'instance (`lanceur_v13.CHEMINS_ARCHIVE`) : `src/controle_ia/__init__.py`, `gardes.py`,
`scellement.py`, `temoin_bailey/__init__.py`, `analyse_v3.py`, `conventions_v3.py`, `execution_v3.py`,
`journaliseur_v3.py`, `lecture_v8.py`, `instance_v12.py`. `lanceur_v13.py` reste sur le poste local.
`INSTANCE_MODULE` = `controle_ia.temoin_bailey.instance_v12` ; veilleurs locaux : `controle_ia.temoin_bailey.lanceur_v13`.
Le lancement passe `4988f3f4…` comme `commit_code`.

**Essais (R5)** au commit ci-dessus : `tests/test_temoin_bailey_condition6_v13.py`
(`7505596e8a1de74735d5fb7f776f24f894297f144de35967d2b99e092e02e7ec`, 139 passés) et `tests/test_temoin_bailey_analyse_v3.py`
(`8cca01f18b61f81fc805dc3c89847e997db66c05609f644a08a5929b3f440d47`, 36 passés). Essai à blanc de l'installation du manifeste sur processeur :
`docs/notes/reproduction-attaque-publiee-v1/essai-installation-manifeste-bailey-v1.md` (`fdff1672…`) : 169 exigences
installées ensemble, code public importable ; `sparsify` appelle `torch.cuda.is_bf16_supported()` à l'import et échoue
sans carte (établi sur processeur ; sur l'instance, à surveiller). L'essai a été fait avec le script d'amorce de
`lanceur_v9`, dont les commandes d'installation sont identiques à celles de `lanceur_v13` (l. 1037-1051, vérifié).

**Contre-lecture (R2)** : relecteurs neufs, rapports scellés dans `docs/notes/reproduction-attaque-publiee-v1/` :
`relecture-code-condition6-v10-bailey-v1.md` (`b6b6430b…`, non conforme) ; `…-v11-…` (`044ba3e2…`, non conforme) ;
`…-v12-…` (`3865961f…`, conforme ; W-1 corrigé sur décision de Lazar) ; `…-v13-…`
(`611c48f1507d43fda99f21e4346dc9389c1e4bb7e4484b9a979d6efd2aa9640a`, **conforme**). Erratum : le message du commit
`47772e37` dit la v11 sans borne budgétaire de la reprise ; elle la contient (`lanceur_v11`, `c581be7c…`).

## 3. Lectures actées

Liste complète, ligne par ligne : `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v11.md`
(`c17475378c1d6684341842bbb6f16c0d600430f122a8506fd9910dfdb68866ce`), qui fait partie de cet addendum et remplace la v7
citée par l'addendum 1. Actes de Lazar : lectures 1 à 36 comme à l'addendum 1 ; **37** (chien de garde) et **38**
(reprise) actées par `registres/passations/2026-11-11-1537-decision-lazar-lectures-37-38-w1.md` (`6b1dc914…`). Les
principales lectures nouvelles :
- **Arrêt autonome (37)** : un chien de garde, lancé sur l'instance par l'amorce et indépendant des exécutions, arrête le
  conteneur (arrêt, pas destruction ; seul le stockage reste facturé) à la fin du run, à D ≥ B − 2, à l'échéance moins
  la marge de transfert, ou si le pilotage est muet depuis 7 200 s ; **conduite vivante**, ces causes ne coupent pas son transfert : l'arrêt
  vient à la marque `rapatrie`, après 3 600 s de cause tenue, ou au plus tard à D ≥ B − 0,5 USD ou à l'échéance −
  1 800 s ; **pilotage muet** pendant le run principal ou sa relance, sans autre cause, l'exécution finit sous ses
  gardes, puis arrêt (lecture 37 (a), (b)) ; il arrête d'abord les commandes par PID (R10),
  attend au plus 600 s, empreinte les journaux, puis arrête quand même. Il emploie la clé que Vast pose sur l'instance,
  restreinte à cette seule instance, jamais imprimée, journalisée ni transférée ; aucune clé du compte de l'utilisateur
  n'est posée sur l'instance. Si l'auto-arrêt n'est pas disponible à la mise en place : pas de run.
- **Reprise (38)** : après une coupure, la session suivante transfère les journaux (redémarrage de l'instance arrêtée
  le temps du seul transfert, sous le même GO), compare les empreintes, scelle, puis détruit par identifiant ; jamais
  de redémarrage s'il reste moins de 900 s de budget avant B − 0,5 USD ; arrêt au plus tôt de l'échéance, de B − 0,5 et
  des délais ; jamais de destruction avant un transfert qui fait foi ; un run interrompu est lu comme tronqué.
- **Ce qui sort de l'instance (l. 316-319 ; lecture 12)** : s'y ajoute le journal du chien de garde
  (`chien-de-garde-v10.jsonl` : causes, décisions, noms des commandes arrêtées par PID, horodatages, nom du type et
  message tronqué des erreurs, codes HTTP ; ni note, ni texte, ni suffixe, ni clé), transféré et scellé par la conduite
  et par la reprise (lecture 22, P-3).
- **Plafond** : la dépense comptée D (toutes instances du poste, intervalles arrêtés compris, compte prudent) est tenue
  sous B = 75 USD, reprises comprises ; hors risques déclarés (§ 4 ; lecture 22 (b), Q-5), dépense réelle relevée sur
  les factures dans `registres/depenses.md`.

## 4. Risques déclarés (lecture 22 de la liste v11, et relecture v13)

Résumé ; la liste complète est celle de la lecture 22 et du bilan de la liste v11 (dont P-6, reprise d'une instance
« exited » ; Q-3, étape lancée sans dossier ; veilleur d'arrêt sans fin si l'API refusait l'arrêt d'une instance
arrêtée) ; ce résumé n'en retire aucun.

- Poste local éteint et chien de garde mort en même temps : l'instance n'est arrêtée par personne (le champ `onstart`
  de Vast n'est pas employé : le taux n'est connu qu'après la création, et il relancerait le chien pendant une reprise).
- Arrêt demandé par la clé d'instance : que Vast coupe bien la facturation de la carte n'est établi que par sa
  documentation, pas par un essai.
- Destruction possible sans transfert : instance en marche au seuil B − 0,5 ou à la fin de la conduite sans transfert
  complet (la borne de dépense prime) ; trois statuts illisibles de suite ; trois arrêts refusés ; statut relu toujours
  non arrêté, dont un arrêt plus lent qu'environ 60 s au pire (lecture 22, C-2, Q-2, W-1, P-1).
- Relecture v13, à préciser, sans effet sur la dépense ni les journaux : (A-1) `reprendre` doit être appelé avec le
  **même chemin absolu** de `--sortie` que la conduite (la comparaison ne résout pas les liens symboliques) ; (A-2)
  fenêtre de quelques microsecondes entre la vérification d'identité d'un veilleur et son signal ; (A-3) une identité
  illisible après le signal est notée comme un arrêt réussi.

## 5. Conditions de lancement (état au scellement)

1 : rempli. 2 : `GO-2026-11-10-10` amendé par `GO-2026-11-11-01` (licence : « auteurs contactés, sans réponse ; risque de
propriété intellectuelle accepté par le directeur »), vérifié sur `main` au commit effectivement lu
(`eabaaaaddb05c0061d4fc5576b9e85aa2ce5a688`, 2026-11-11T16:07:19Z, lu par
`git fetch --depth=5 origin +refs/heads/main:refs/remotes/origin/main` ; `registres/go.md` à ce commit
`3101983333ad8e6a84f2f3a4a8585e039867728e587a4bd0ab7e0c3153d8f4d6`, l. 300 et 305) : rempli ; échéance (2026-11-30) à
vérifier à la création contre création + (B − 2)/c heures, c relevé. 3 : `GO-2026-11-11-02` (modèle), sur `main` au même
commit (l. 306) : rempli. 4 : mot de Lazar sur la licence (lancer sans l'écrit des auteurs),
`registres/passations/2026-11-11-0005-decision-lazar-lancer-sans-ecrit.md`
(`8b51d5df6d747caf0115f4a26af7796ba56cb1fac28b5298d81024c9f96ee57b`) : rempli. 5 : addendum 2 de la règle du bras
(`73c8de01…`, déposé chez le tiers le 2026-11-11T15:46:02Z), dépôt attesté sur `main` par `registres/decisions.md`
R-2384 : rempli. 6 : rempli par cet addendum, une fois scellé. 7 : « go lancement bailey »,
`registres/passations/2026-11-11-0001-decision-lazar-go-lancement-bailey.md`
(`5b4b337350cd4a14c924f42b6a60b9ced0e87cf8ea7f8fc74703cb56e1cee3ee`), suspendu par
`registres/passations/2026-11-11-0001-decision-lazar-non-go-depenses.md`
(`72e78e250570b84714618fbe68c1051c183c4889c309615df0e5e6a88bd80ab8`), elle-même annulée par
`registres/passations/2026-11-11-0002-correction-lazar-go-depenses.md`
(`168f3948549217e2b1cede2121020df79466c1b1f7710f824c9d9fa19bbcf91f`) : rempli. 8 : lancement par cette session
(« lancer d'ici », `registres/passations/2026-11-11-1226-decision-lazar-option-b-arret-autonome.md`,
`fb6f603249d5c2b1a6f31caf8f2376aa993b7481449ce4c2cddf0c6b1e6b7fc5`) ; Vast.ai joignable (`vastai` 1.11.0, `--label`) ;
champ `label` de `vastai show instances --raw` à vérifier avant la création (lecture 35) ; jeton Hugging Face avec accès
aux deux modèles contrôlés ; `DEPOT_URL` du dépôt de travail. Lecture 23 (tokeniseur de l'adaptateur du juge) : levée —
la liste publique des fichiers du dépôt `qylu4156/strongreject-15k-v1` (révision `4bd893d3…`) contient `tokenizer.json`
et `tokenizer.model`, relevé le 10 novembre 2026 par la session.

## Contre-lecture

Rapport (R2) : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-addendum-2-condition6-bailey-v1.md`
(`353f7d17af6be54ff192c43d9259f4a5c0234dd663280a6c523978f5eeade193`), sous-agent neuf. Verdict : **scellable après
corrections** (K-1 à K-7), sans nouvelle contre-lecture (contrôle par `diff`). Brouillon 1, relu, archivé sans
modification : `brouillons/temoin-attaque-publiee-bailey-v1-addendum-2-condition6-arret-autonome-brouillon1.md`
(`3ca1ee7c79862e9fe310cc7de478df17dfb8c7344a8fd842a1a311fc95dbbd8d`). Corrections appliquées, reprises mot pour mot du
rapport :

> - **K-1 (§ 3, lecture 37, le résumé change la lecture).** Le résumé dit que le chien arrête le conteneur « à la fin du
>   run, à D ≥ B − 2, à l'échéance moins la marge de transfert, ou si le pilotage est muet depuis 7 200 s ». La lecture
>   37 actée (a) et (b) dit autre chose : **conduite vivante**, ces causes ne coupent pas son transfert ; l'arrêt vient à
>   la marque `rapatrie`, après 3 600 s de cause tenue, ou au plus tard à D ≥ B − 0,5 ou à l'échéance − 1 800 s ;
>   **conduite muette** pendant le run principal (ou sa relance) sans autre cause, l'exécution finit sous ses gardes
>   avant l'arrêt. Texte exact proposé, après « … muet depuis 7 200 s ; » : « **conduite vivante**, ces causes ne coupent
>   pas son transfert : l'arrêt vient à la marque `rapatrie`, après 3 600 s de cause tenue, ou au plus tard à
>   D ≥ B − 0,5 USD ou à l'échéance − 1 800 s ; **pilotage muet** pendant le run principal ou sa relance, sans autre
>   cause, l'exécution finit sous ses gardes, puis arrêt (lecture 37 (a), (b)) ; ».
> - **K-2 (§ 3, « Ce qui sort de l'instance », omission d'un acte attendu).** La lecture 22 (v11, P-3), actée par
>   renvoi, dit : le journal du chien « **l'addendum 2 l'ajoute à la liste fermée « Ce qui sort de l'instance »** (texte
>   l. 316-319 ; lecture 12) ». L'addendum ne le fait pas ; la lecture 12 de la liste v11 ne le porte pas. Texte exact
>   proposé, nouvelle puce du § 3 : « **Ce qui sort de l'instance (l. 316-319 ; lecture 12)** : s'y ajoute le journal du
>   chien de garde (`chien-de-garde-v10.jsonl` : causes, décisions, noms des commandes arrêtées par PID, horodatages, nom
>   du type et message tronqué des erreurs, codes HTTP ; ni note, ni texte, ni suffixe, ni clé), transféré et scellé par
>   la conduite et par la reprise (lecture 22, P-3). »
> - **K-3 (§ 3 « Plafond » et § 4, le résumé dit plus que les lectures).** (a) « la dépense du poste, toutes périodes
>   comptées, ne dépasse jamais B » contredit le risque déclaré (§ 4, 1re puce ; lecture 22 Q-5 : poste éteint et chien
>   mort, « la dépense n'a plus de borne ») et la lecture 22 (b) (« dépassement de B borné » : au-delà des bornes, le
>   stockage court, relevé sur factures). Texte exact proposé : « **Plafond** : la dépense comptée D (toutes instances
>   du poste, intervalles arrêtés compris, compte prudent) est tenue sous B = 75 USD, reprises comprises ; hors risques
>   déclarés (§ 4 ; lecture 22 (b), Q-5), dépense réelle relevée sur les factures dans `registres/depenses.md`. »
>   (b) Au § 4, « Destruction possible sans transfert dans les **seuls** cas déclarés : … » omet deux cas de la lecture
>   22 : instance **en marche** (ou statut illisible trois fois) au seuil B − 0,5 du veilleur de secours ou à `_finir`
>   sans transfert complet (« la borne de dépense prime », C-2, Q-2) ; arrêt dont l'effet prend plus d'environ 60 s au
>   pire (P-1 v13). Remplacer par : « Destruction possible sans transfert : instance en marche au seuil B − 0,5 ou à la
>   fin de la conduite sans transfert complet (la borne de dépense prime) ; trois statuts illisibles de suite ; trois
>   arrêts refusés ; statut relu toujours non arrêté, dont un arrêt plus lent qu'environ 60 s au pire (lecture 22, C-2,
>   Q-2, W-1, P-1). » Et ajouter en tête du § 4 : « Résumé ; la liste complète est celle de la lecture 22 et du bilan de
>   la liste v11 (dont P-6, reprise d'une instance « exited » ; Q-3, étape lancée sans dossier ; veilleur d'arrêt sans fin
>   si l'API refusait l'arrêt d'une instance arrêtée) ; ce résumé n'en retire aucun. »
> - **K-4 (§ 2, fait inexact).** « `sparsify` exige une carte dès l'import (vérifié sur l'instance) » : l'essai
>   `fdff1672…` est **sur processeur**, « aucune instance » ; il établit l'échec sans carte et dit « Sur une instance à
>   carte, rien d'attendu ; à surveiller ». Remplacer par : « `sparsify` appelle `torch.cuda.is_bf16_supported()` à
>   l'import et échoue sans carte (établi sur processeur ; sur l'instance, à surveiller) ». Ajouter que l'essai a été
>   fait avec le script d'amorce de `lanceur_v9`, dont les commandes d'installation sont identiques à celles de
>   `lanceur_v13` (l. 1037-1051, vérifié).
> - **K-5 (§ 5, sources des conditions, R6).** Citer chemin et empreinte : condition 4,
>   `registres/passations/2026-11-11-0005-decision-lazar-lancer-sans-ecrit.md` (`8b51d5df…`) ; condition 7,
>   `…-0001-decision-lazar-go-lancement-bailey.md` (`5b4b3373…`), suspendue par `…-0001-decision-lazar-non-go-depenses.md`
>   (`72e78e25…`), elle-même annulée par `…-0002-correction-lazar-go-depenses.md` (`168f3948…`) ; condition 8,
>   `…-1226-decision-lazar-option-b-arret-autonome.md` (`fb6f6032…`, « lancer d'ici ») ; condition 5, dépôt chez le tiers
>   attesté sur `main` par `registres/decisions.md` R-2384. Condition 2 : citer la tête de `main` lue au scellement
>   (lignes identiques à `287116bb` et à `eabaaaad`, vérifié ; le `fetch` à profondeur 5 rapporte une mise à jour forcée,
>   donc citer le commit effectivement lu) et ajouter « échéance (2026-11-30) à vérifier à la création contre
>   création + (B − 2)/c heures, c relevé ».
> - **K-6 (§ 2).** Ajouter l'empreinte de `tests/test_temoin_bailey_analyse_v3.py` :
>   `8cca01f18b61f81fc805dc3c89847e997db66c05609f644a08a5929b3f440d47`.
> - **K-7 (§ 5, condition 8).** Garder ce qui reste à établir : lecture 35, champ `label` de
>   `vastai show instances --raw` « à établir avant l'instance » (l'addendum 1 le disait ; la liste v11 le garde), et
>   lecture 23 (tokeniseur de l'adaptateur) si elle n'a pas été levée depuis. Texte exact proposé : « … `--label` ; champ
>   `label` de `vastai show instances --raw` à vérifier avant la création (lecture 35) ; … ».
