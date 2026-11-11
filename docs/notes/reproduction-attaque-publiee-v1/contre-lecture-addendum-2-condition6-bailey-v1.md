# Contre-lecture (R2) de l'addendum 2 du témoin de Bailey (condition 6, code v13, arrêt autonome) — v1

- Date : Wed Nov 11 16:13:06 UTC 2026 (`date -u`). Contre-lecteur : sous-agent neuf ; je n'ai écrit aucune des pièces lues.
- Je reçois d'office le `CLAUDE.md` du dépôt (consignes permanentes), injecté dans mon contexte.
- Dépôt `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, tête `1e4894c9` ; code au
  commit `4988f3f4` ; `main` lu par `git fetch --depth=5 origin +refs/heads/main:refs/remotes/origin/main` (tête
  `eabaaaad`, 2026-11-11T16:07:19Z).
- Non scellé : le scellement revient à la session qui commande la contre-lecture.
- Outils : `git show`, `git diff`, `git log`, `git grep`, `sha256sum`, `grep`, `sed`, `fold` ; essais rejoués avec
  `.venv/bin/python -m pytest -q -p no:cacheprovider` (`PYTHONPATH=src`). Aucune requête réseau hors le `git fetch`
  ci-dessus ; aucun appel à `vastai` ; aucune valeur de clé lue. Cloisons tenues : le fichier
  `registres/passations/2026-11-11-0002-refus-classifieur-bailey.md` n'a été vu que par son nom. Aucun refus de
  classifieur pendant cette contre-lecture.

## Pièces lues et empreintes (SHA-256)

| Pièce | Empreinte |
|---|---|
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-2-condition6-arret-autonome.md` (brouillon 1, objet) | `3ca1ee7c79862e9fe310cc7de478df17dfb8c7344a8fd842a1a311fc95dbbd8d` |
| `prereg/temoin-attaque-publiee-bailey-v1.md` (l. 310-322, 374-392) | `fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-1-condition6.md` (§ 4) | `6f7eda737237bd58f7f516ea16be947b3ecdae6aca1bfde418d9d78a90e8aece` |
| `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v11.md` (en-tête, lectures 12, 22, 35, 37, 38, bilan) | `c17475378c1d6684341842bbb6f16c0d600430f122a8506fd9910dfdb68866ce` |
| `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v13-bailey-v1.md` | `611c48f1507d43fda99f21e4346dc9389c1e4bb7e4484b9a979d6efd2aa9640a` |
| `docs/notes/reproduction-attaque-publiee-v1/essai-installation-manifeste-bailey-v1.md` | `fdff16721bf8aded163a16ef3515e6c6b30a06c6b5ca279e4748ac719033b0a3` |
| `src/controle_ia/temoin_bailey/lanceur_v13.py` et `instance_v12.py` à `4988f3f4` (constantes, `decider`, docstrings) | voir § 1 |
| `registres/passations/2026-11-11-0001-decision-lazar-go-lancement-bailey.md` | `5b4b337350cd4a14c924f42b6a60b9ced0e87cf8ea7f8fc74703cb56e1cee3ee` |
| `registres/passations/2026-11-11-0001-decision-lazar-non-go-depenses.md` | `72e78e250570b84714618fbe68c1051c183c4889c309615df0e5e6a88bd80ab8` |
| `registres/passations/2026-11-11-0002-correction-lazar-go-depenses.md` | `168f3948549217e2b1cede2121020df79466c1b1f7710f824c9d9fa19bbcf91f` |
| `registres/passations/2026-11-11-0005-decision-lazar-lancer-sans-ecrit.md` | `8b51d5df6d747caf0115f4a26af7796ba56cb1fac28b5298d81024c9f96ee57b` |
| `registres/passations/2026-11-11-1226-decision-lazar-option-b-arret-autonome.md` | `fb6f603249d5c2b1a6f31caf8f2376aa993b7481449ce4c2cddf0c6b1e6b7fc5` |
| `registres/passations/2026-11-11-1537-decision-lazar-lectures-37-38-w1.md` | `6b1dc914d4f28f0e4760d3f2a73f573f2287ec0c1a0043dde1086ebc89104f79` |
| `registres/passations/2026-11-11-1556-attaquant-informe-successeur-etape.md` | lu, non cité par l'addendum |
| `origin/main:registres/go.md` (l. 300, 305, 306) ; `origin/main:registres/decisions.md` (R-2384 seule) | `go.md` : `3101983333ad8e6a84f2f3a4a8585e039867728e587a4bd0ab7e0c3153d8f4d6` |

## Verdict

**Scellable après corrections** (K-1 à K-7 ci-dessous). Aucune ne touche au code, aux lectures actées ni ne demande un
mot de Lazar : ce sont des fidélités de résumé et des renvois. Après K-1 à K-7 : scellable, sans nouvelle contre-lecture
(contrôle par `diff` suffisant). Aucun résultat dans le texte ; aucun écart au préenregistrement scellé, sous K-1 et K-2.

## 1. Empreintes et commit — conformes

- Commit `4988f3f442c670887a0e8ad15ddfbac68a173d03`, 2026-11-11T15:55:33Z : conforme.
- `git show 4988f3f4:CHEMIN | sha256sum` égale l'empreinte dite pour les sept modules (`lanceur_v13` `9257266f…`,
  `instance_v12` `de466986…`, `lecture_v8` `1657a492…`, `execution_v3` `279f1f4f…`, `journaliseur_v3` `9f75407c…`,
  `conventions_v3` `51c2fa26…`, `analyse_v3` `c28c6821…`) et pour `tests/test_temoin_bailey_condition6_v13.py`
  (`7505596e…`). `src/` et `tests/` sont inchangés entre `4988f3f4` et la tête de branche.
- Essais rejoués : les deux fichiers ensemble, **175 passés** (139 + 36), conforme.
- `CHEMINS_ARCHIVE` (l. 280-283), `INSTANCE_MODULE = "controle_ia.temoin_bailey.instance_v12"` (l. 264),
  `VEILLEUR_MODULE = "controle_ia.temoin_bailey.lanceur_v13"` (l. 265) : ceux que dit l'addendum. `commit_code` porté
  par l'ordre de lancement et le manifeste (l. 557, 1233-1236) : conforme.
- Chaque rapport, décision et liste cités existe, avec un compagnon `.sha256` égal à l'empreinte dite (relectures v10
  `b6b6430b…`, v11 `044ba3e2…`, v12 `3865961f…`, v13 `611c48f1…` ; lectures v11 `c1747537…` ; essai `fdff1672…` ;
  décisions `fb6f6032…`, `6b1dc914…` ; préenregistrement `fb6c2f34…` ; addendum 1 `6f7eda73…` ; règle du bras,
  addendum 2, compagnon `73c8de01…`).
- Erratum `47772e37` : vérifié (message « sans la borne budgétaire de la reprise » ; `lanceur_v11` à ce commit
  `c581be7c…` contient `DUREE_TRANSFERT_MIN_S` et la borne).
- Remarque (K-6) : l'empreinte de `tests/test_temoin_bailey_analyse_v3.py` manque (`8cca01f1…` à `4988f3f4`), alors
  que l'addendum 1 la donnait (correction C-2 de sa contre-lecture).

## 2. Fidélité des § 3 et § 4 — trois écarts

Valeurs vérifiées dans le code à `4988f3f4` : `D_ABANDON_S = 7200.0` (`instance_v12` l. 172) ;
`ATTENTE_COMMANDES_MAX_S = 2 * GRACE_EXECUTION_S` = 600 s, ou `PASSAGES_ATTENTE_MAX = 40`, au premier atteint
(l. 177-181, 1131-1132) ; `DUREE_TRANSFERT_MIN_S = 900.0` (`lanceur_v13` l. 268) ; B − 2 (`decider`, l. 965 ;
`lanceur_v13` l. 1330, 1336, 1564) ; B − 0,5 (`MARGE_SECOURS_USD = 0.5`, les deux modules) ; `-y` à la destruction
(`lanceur_v13` l. 354, ligne « destroying instance <id>. » exigée). Clé : seule `CONTAINER_API_KEY` lue, jamais
imprimée, aucune clé du compte posée (docstring `instance_v12` l. 62-92) ; journal du chien sans clé (lecture 22,
P-3). Lecture 38 : résumé fidèle (900 s avant B − 0,5 ; arrêt au plus tôt de l'échéance, de B − 0,5 et des délais ;
destruction seulement après transfert qui fait foi ; run interrompu lu tronqué).

- **K-1 (§ 3, lecture 37, le résumé change la lecture).** Le résumé dit que le chien arrête le conteneur « à la fin du
  run, à D ≥ B − 2, à l'échéance moins la marge de transfert, ou si le pilotage est muet depuis 7 200 s ». La lecture
  37 actée (a) et (b) dit autre chose : **conduite vivante**, ces causes ne coupent pas son transfert ; l'arrêt vient à
  la marque `rapatrie`, après 3 600 s de cause tenue, ou au plus tard à D ≥ B − 0,5 ou à l'échéance − 1 800 s ;
  **conduite muette** pendant le run principal (ou sa relance) sans autre cause, l'exécution finit sous ses gardes
  avant l'arrêt. Texte exact proposé, après « … muet depuis 7 200 s ; » : « **conduite vivante**, ces causes ne coupent
  pas son transfert : l'arrêt vient à la marque `rapatrie`, après 3 600 s de cause tenue, ou au plus tard à
  D ≥ B − 0,5 USD ou à l'échéance − 1 800 s ; **pilotage muet** pendant le run principal ou sa relance, sans autre
  cause, l'exécution finit sous ses gardes, puis arrêt (lecture 37 (a), (b)) ; ».
- **K-2 (§ 3, « Ce qui sort de l'instance », omission d'un acte attendu).** La lecture 22 (v11, P-3), actée par
  renvoi, dit : le journal du chien « **l'addendum 2 l'ajoute à la liste fermée « Ce qui sort de l'instance »** (texte
  l. 316-319 ; lecture 12) ». L'addendum ne le fait pas ; la lecture 12 de la liste v11 ne le porte pas. Texte exact
  proposé, nouvelle puce du § 3 : « **Ce qui sort de l'instance (l. 316-319 ; lecture 12)** : s'y ajoute le journal du
  chien de garde (`chien-de-garde-v10.jsonl` : causes, décisions, noms des commandes arrêtées par PID, horodatages, nom
  du type et message tronqué des erreurs, codes HTTP ; ni note, ni texte, ni suffixe, ni clé), transféré et scellé par
  la conduite et par la reprise (lecture 22, P-3). »
- **K-3 (§ 3 « Plafond » et § 4, le résumé dit plus que les lectures).** (a) « la dépense du poste, toutes périodes
  comptées, ne dépasse jamais B » contredit le risque déclaré (§ 4, 1re puce ; lecture 22 Q-5 : poste éteint et chien
  mort, « la dépense n'a plus de borne ») et la lecture 22 (b) (« dépassement de B borné » : au-delà des bornes, le
  stockage court, relevé sur factures). Texte exact proposé : « **Plafond** : la dépense comptée D (toutes instances
  du poste, intervalles arrêtés compris, compte prudent) est tenue sous B = 75 USD, reprises comprises ; hors risques
  déclarés (§ 4 ; lecture 22 (b), Q-5), dépense réelle relevée sur les factures dans `registres/depenses.md`. »
  (b) Au § 4, « Destruction possible sans transfert dans les **seuls** cas déclarés : … » omet deux cas de la lecture
  22 : instance **en marche** (ou statut illisible trois fois) au seuil B − 0,5 du veilleur de secours ou à `_finir`
  sans transfert complet (« la borne de dépense prime », C-2, Q-2) ; arrêt dont l'effet prend plus d'environ 60 s au
  pire (P-1 v13). Remplacer par : « Destruction possible sans transfert : instance en marche au seuil B − 0,5 ou à la
  fin de la conduite sans transfert complet (la borne de dépense prime) ; trois statuts illisibles de suite ; trois
  arrêts refusés ; statut relu toujours non arrêté, dont un arrêt plus lent qu'environ 60 s au pire (lecture 22, C-2,
  Q-2, W-1, P-1). » Et ajouter en tête du § 4 : « Résumé ; la liste complète est celle de la lecture 22 et du bilan de
  la liste v11 (dont P-6, reprise d'une instance « exited » ; Q-3, étape lancée sans dossier ; veilleur d'arrêt sans fin
  si l'API refusait l'arrêt d'une instance arrêtée) ; ce résumé n'en retire aucun. »
- Relecture v13 : A-1 à A-3 fidèles au rapport (« sans effet sur la dépense ni sur les journaux » est le mot du
  rapport ; A-1 a pour effet un redémarrage payé pour rien sous B).

## 3. Autres corrections

- **K-4 (§ 2, fait inexact).** « `sparsify` exige une carte dès l'import (vérifié sur l'instance) » : l'essai
  `fdff1672…` est **sur processeur**, « aucune instance » ; il établit l'échec sans carte et dit « Sur une instance à
  carte, rien d'attendu ; à surveiller ». Remplacer par : « `sparsify` appelle `torch.cuda.is_bf16_supported()` à
  l'import et échoue sans carte (établi sur processeur ; sur l'instance, à surveiller) ». Ajouter que l'essai a été
  fait avec le script d'amorce de `lanceur_v9`, dont les commandes d'installation sont identiques à celles de
  `lanceur_v13` (l. 1037-1051, vérifié).
- **K-5 (§ 5, sources des conditions, R6).** Citer chemin et empreinte : condition 4,
  `registres/passations/2026-11-11-0005-decision-lazar-lancer-sans-ecrit.md` (`8b51d5df…`) ; condition 7,
  `…-0001-decision-lazar-go-lancement-bailey.md` (`5b4b3373…`), suspendue par `…-0001-decision-lazar-non-go-depenses.md`
  (`72e78e25…`), elle-même annulée par `…-0002-correction-lazar-go-depenses.md` (`168f3948…`) ; condition 8,
  `…-1226-decision-lazar-option-b-arret-autonome.md` (`fb6f6032…`, « lancer d'ici ») ; condition 5, dépôt chez le tiers
  attesté sur `main` par `registres/decisions.md` R-2384. Condition 2 : citer la tête de `main` lue au scellement
  (lignes identiques à `287116bb` et à `eabaaaad`, vérifié ; le `fetch` à profondeur 5 rapporte une mise à jour forcée,
  donc citer le commit effectivement lu) et ajouter « échéance (2026-11-30) à vérifier à la création contre
  création + (B − 2)/c heures, c relevé ».
- **K-6 (§ 2).** Ajouter l'empreinte de `tests/test_temoin_bailey_analyse_v3.py` :
  `8cca01f18b61f81fc805dc3c89847e997db66c05609f644a08a5929b3f440d47`.
- **K-7 (§ 5, condition 8).** Garder ce qui reste à établir : lecture 35, champ `label` de
  `vastai show instances --raw` « à établir avant l'instance » (l'addendum 1 le disait ; la liste v11 le garde), et
  lecture 23 (tokeniseur de l'adaptateur) si elle n'a pas été levée depuis. Texte exact proposé : « … `--label` ; champ
  `label` de `vastai show instances --raw` à vérifier avant la création (lecture 35) ; … ».

## 4. Conditions de lancement vérifiées

- `origin/main:registres/go.md` l. 300 (`GO-2026-11-10-10` : 75 USD, B = 75, garde à B − 2, `fb6c2f34…`, devis v4
  `f9c8c66e…`, échéance 2026-11-30), l. 305 (`GO-2026-11-11-01` : texte de licence identique à celui de l'addendum),
  l. 306 (`GO-2026-11-11-02` : Llama-3-8B-Instruct, ce seul témoin) : présentes, conformes au § 5.
- Décisions dans `registres/passations/` : « go lancement bailey » (`…-0001-…`), lancer sans l'écrit (`…-0005-…`),
  « go dépenses » (`…-0002-correction-…`), option (b) (`…-1226-…`), lectures 37-38 et W-1 (`…-1537-…`) : présentes,
  compagnons conformes, verbatim cohérents avec le § 5 (sous K-5).
- Point 3 de la décision option (b) (« addendum 2 … risque 22 révisé, contre-lu et scellé ») : tenu par cet addendum.
