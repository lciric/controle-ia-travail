# Organismes discrets, bras A — vérification du brouillon 2 du devis de l'essai de mesure des lecteurs — v1

- **Pièce vérifiée** : `docs/notes/relance-organismes-discrets-v1/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon2.md`, branche `claude/pensive-bardeen-1fv7hw` (tête `65a4a14e2`), empreinte `ae9e75bba8b80f308679a6570e24cfc2a616633311475f7c6252ef44a458eb38`, recalculée et conforme à son compagnon.
- **Contre-lecture de référence** : `contre-lecture-devis-essai-de-mesure-lecteurs-v1.md` (`d1b8ad89037c…`), corrections C1 à C7, recommandations R1 à R9.
- **Vérificateur** : le même contre-lecteur (Claude Opus 5.5), comme le veut la classe A ; le 2026-11-19, vers 10:05 UTC.
- **Interdits tenus** : rien lu dans `diag/`, `runs/`, `donnees/` ni `docs/verdicts/`. En particulier, **l'attestation de la clé Claude (`runs/verification-cle-claude-rigaud-v1/releve-verification-v1.json`) n'a pas été ouverte** : ce qui en est dit vient du journal de la relance (OD-104 à OD-106). Aucun interne de moniteur, aucun appel payant ni modèle chargé. Réseau : `git fetch` seulement ; aucune page lue en ligne, les pages versées ont été lues dans le dépôt. Aucun fichier existant modifié ; rien committé.

## Conclusion

**Pas avant : deux précisions de texte, D1 (état de la clé Claude) et D3 (codes de retour non listés), sans changement de plafond ni de plan. Pour les files Carbon et GPT, seule D3 reste. D2 et D4 sont à faire au même passage, sans bloquer.**

## 1. Les corrections C1 à C7

| correction | faite ? | où | remarque |
|---|---|---|---|
| C1 réponse de Carbon gardée entière, corps d'envoi gardé, versement poussé | **oui, à la lettre** | 5.3 ; 8.2 | `--max-appels` porté à 97 pour l'envoi d'essai de la température : cohérent avec 5.5 |
| C2 trois conditions du plafond, à un envoi de Carbon près, prix de repli | **oui, à la lettre** ; pire cas recalculé par octet | 6.1 ; 6.2 ; 6.3 ; 6.4 | recalculé ici : 19,34 + 9,67 + 0,24 + 14,41 + 6,44 = 50,10 (le devis écrit 50,09, simple arrondi) ; Carbon au prix de repli 29,9 ; Fable 5.2 à 10 et 50 : 24,16 ; pire cas par envoi justes. Texte périmé sur le scellement des pages : D2 |
| C3 aucune reprise cachée | **oui, à la lettre** | 9 ; 10 | — |
| C4 refus de compte, de contenu, des relais ; surcharge, 529 | **oui, à la lettre**, et étendue (code 400 et exception de la température) | 9, garde G4 | ce qui n'est pas dans la liste n'est pas traité : D3 |
| C5 GO-2026-11-19-22 cité, écarts déclarés | **oui** | 0 ; 1 ; 6.4 ; 11 | lettre vérifiée à la ligne 455 du registre de `main` (`4f011d247`) |
| C6 compteurs définis, envoi qui compte, sortie maximale | **oui, à la lettre**, et partis pris écrits comme tels | 7.3 | — |
| C7 incertitude réduite aux textes synthétiques | **oui, à la lettre** | 4.4 | — |

Les recommandations R1 à R9 sont toutes appliquées (table 12.2, vérifiée passage par passage). R5 est étendue à GPT : c'est juste. Deux suites de R3 et R5 sont en recommandations ci-dessous (E1, E2).

**Aucun écart à la lettre ou à l'esprit de C1 à C7.** Les corrections nouvelles viennent de faits postérieurs au brouillon 2, ou de passages ajoutés par lui.

## 2. Le plafond de 17,75 dollars, et le prix de Carbon

**Les files séparées tiennent-elles le plafond ? Oui, à un envoi de Carbon près, comme écrit.**
- Il y a trois compteurs indépendants, un par file : Claude 9,25 (Opus 5.5 : 6 ; Sonnet 5.5 : 3 ; Haiku 5.5 : 0,25), Carbon 6, GPT 2,50. Chacun refuse l'envoi avant qu'il parte. Comme aucun compteur n'est partagé, des files qui tournent en même temps ne peuvent pas franchir ensemble la somme. Chaque file a de plus sa propre ligne de calcul (garde G7) : une file non accordée ne coûte rien, et le total accordé est la somme des files accordées.
- Les seconds plafonds, ceux des relais, sont cohérents. Relais Claude : 9,25 avec une réserve par envoi de 0,27, au-dessus du pire envoi d'Opus 5.5, 0,260. Relais compatible OpenAI : 2,50, avec une réserve tirée des octets, d'environ 0,52 pour une couverture. Le relais de Google n'a pas de plafond en dollars : 97 appels au plus, soit ≈ 21 dollars au pire cas compté si le chef d'essai faillait. Ce chiffre est écrit dans le devis.
- **Seule exception, écrite** : Carbon, dont aucune pièce n'établit que le budget de réflexion soit une borne dure. La page versée dit que le modèle peut produire jusqu'à un million de jetons (« long-decode generation up to 1M tokens »). En pratique, le dépassement d'un envoi est borné par le délai total de 180 secondes, pas par une borne écrite par le fournisseur (voir 3, doute 2).

**Le prix de Carbon compté est-il au moins le prix facturé, y compris après le 30 novembre ? Oui.** Vérifié sur la page versée et scellée `docs/sources/prix-fournisseurs-2026-11-19/aistudio-google-com-docs-pricing-20261119T095218Z.html` (`89c58281ba7e…`, compagnon conforme). Section « Gemini 4 Carbon », onglet « Standard » :
- entrée « $2.00 through November 30, 2026. $4.00 starting December 1, 2026. » ;
- sortie « (including thinking tokens) » : « $10.00 through November 30, 2026. $20.00 starting December 1, 2026. » ;
- aucun palier selon la longueur de l'entrée ; cache implicite seulement, qui ne peut que baisser la facture.

Compté à 4 et 20, Carbon est compté au double du prix réel jusqu'au 30 novembre, et au prix réel à partir du 1er décembre : la condition (a) tient dans les deux cas, si l'essai glisse. Seul un changement de prix postérieur au 19 novembre la mettrait en défaut : la page n'en annonce aucun.

Vérifiés au passage sur la page d'Anthropic versée et scellée (`78aff5c8d73a…`) : Opus 5.5 à 4 et 20 ; Sonnet 5.5 à 2 et 10 ; Haiku 5.5 à 0,10 et 0,50 (entrées de 100 000 jetons au plus) ; Fable 5.2 à 8 en entrée (compté 10 et 50 : borne haute). GPT reste à 8 et 40 sur la page du 18 novembre (`35a04829…`) : la page du jour a rendu un code 403, et le refus est versé.

## 3. Les trois doutes restants de l'auteur

| doute | bloque l'engagement ? | où il se tranche, et la phrase juste |
|---|---|---|
| **1. Lancement du relais d'OpenAI quand la clé est un secret du réseau** | **non** ; il bloque seulement le départ de la file GPT, comme tout le code (section 11, point 4) | Il se tranche **dans le lanceur et le code**, contre-lus en classe B. La forme existe : la course du 18 novembre (`registres/depenses.md`, ligne 522 ; enveloppe `appel-astra-juge-6-2-v1.sh`, en-tête) lançait `relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY`. Phrase pour la garde G6 : « Pour GPT, aucune valeur de clé n'est dans le conteneur. Le relais est lancé avec une valeur factice sous `OPENAI_API_KEY`, que le mandataire du réseau remplace à la sortie. Le chef d'essai ne parle qu'à la boucle locale : toute requête vers OpenAI passe par le relais et son plafond. L'artefact de G6 est un relais lancé sans la variable : rien ne part. » |
| **2. Budget de réflexion de Carbon, borne dure ou non** | **non** : le devis et la ligne proposée disent déjà « à un envoi près » | Il se tranche **par la mesure, dans le code**. Pour chaque envoi de Carbon, le journal relève si `thoughtsTokenCount` dépasse le budget envoyé, et si `candidatesTokenCount + thoughtsTokenCount` dépasse `maxOutputTokens`. Le rapport donne les deux comptes. Phrase à ajouter à 6.3, condition (c) : « Le dépassement possible d'un envoi de Carbon est borné en pratique par son délai total de 180 secondes, non par une borne écrite du fournisseur ; l'essai relève, envoi par envoi, si le budget et la sortie maximale ont été respectés. » |
| **3. Température 0 acceptée ou non par Carbon et GPT** | **non** | Il se tranche **dans le code**, par la règle de 5.5 : un 400 qui nomme la température la retire de la file, et c'est consigné. Une conséquence n'est pas dite : D4. |

## 4. Corrections et précisions

**D1 — état de la clé Claude (bloquant pour la file Claude seulement).** Le brouillon 2 a été écrit avant les lignes GO-2026-11-19-31 et -32 (registre de `main`) et les entrées OD-104 à OD-106 du journal ; son texte est périmé. La lettre de GO-2026-11-19-31 dit que Lazar pose la clé « lui-même dans l'environnement de la session de relance, par le formulaire sécurisé ». Ce formulaire a été refusé pour les hôtes d'Anthropic (OD-104) : c'est la variable déjà présente qui a été vérifiée. L'écart doit être écrit.
- Avant (5.6) : « - **Claude** : **aucune clé dans l'environnement de cette session pour l'instant.** La question est posée à Lazar par la session mère, dont la recommandation est : une clé posée par lui dans l'environnement, puis vérifiée par un appel minimal sous une ligne à part de 0,01 dollar. **La file Claude ne part pas sans cette clé posée et vérifiée** (garde G8). La poche qui paie (crédits ou facture) est dite par Lazar avec la clé ; le plafond en dollars au barème public vaut dans les deux cas. »
- Après : « - **Claude** : la part Claude est payée par la clé « Rigaud » (GO-2026-11-19-31). **Écart déclaré à la lettre de cette ligne** : le formulaire sécurisé refuse un secret pour les hôtes d'Anthropic (journal, OD-104). La clé employée est donc la variable `RR_ANTHROPIC_API_KEY_RIGAUD`, déjà présente dans l'environnement de la session, lue par le relais Claude par son nom (`--variable-cle RR_ANTHROPIC_API_KEY_RIGAUD`). [Citer ici le mot de Lazar qui couvre cet emploi : « go reco a », OD-105, si la recommandation le disait ; sinon, le faire confirmer.] Elle a été vérifiée par un seul appel à Claude Haiku 5.5 sous GO-2026-11-19-32 (journal, OD-106 : code 200, modèle servi identique au modèle demandé). L'attestation scellée est `runs/verification-cle-claude-rigaud-v1/releve-verification-v1.json`, dont l'empreinte est citée à la configuration (garde G8). L'appel n'a vérifié que Haiku 5.5 : un refus de la clé pour Opus 5.5 ou Sonnet 5.5 se lirait au premier envoi de la file (garde G4). Poche : celle de la clé Rigaud, que la ligne de calcul nomme ; le plafond en dollars au barème public vaut quelle que soit la poche. »
- Avant (garde G6) : « pour Claude, le nom que Lazar dira »
- Après : « pour Claude, `RR_ANTHROPIC_API_KEY_RIGAUD` »
- Avant (section 11, point 7) : « **File Claude seulement** : clé posée par Lazar, vérifiée par l'appel minimal sous sa ligne à part ; attestation scellée (garde G8). »
- Après : « **File Claude seulement** : clé vérifiée sous GO-2026-11-19-32 (fait, OD-106) ; empreinte de l'attestation inscrite à la configuration (garde G8) ; écart à la lettre de GO-2026-11-19-31 déclaré (5.6). »

**D3 — codes de retour non listés (bloquant pour les trois files).** La garde G4 traite 400, 401, 402, 403, 429, 500, 502, 503 et 529. Un 404 (modèle introuvable ou non permis pour cette clé), un 413 ou un 422 n'ont pas de règle : le code ne sait pas s'il reprend, continue ou s'arrête.
- Avant (garde G4, fin de la colonne « ce qu'elle fait ») : « **Code 400** : arrêt de la file, sauf le refus de la température (5.5). Les autres files continuent »
- Après : « **Code 400** : arrêt de la file, sauf le refus de la température (5.5). **Tout autre code que 200 et ceux nommés ici** (404, 413, 422, …) : arrêt de la file, sans reprise, code et origine (relais ou amont) au journal. Les autres files continuent »
- Et ajouter à la colonne « artefact » : « réponse 404 : arrêt de la file, sans reprise ».

**D2 — pages de prix scellées (non bloquant ; texte périmé).** Les quatre pièces de `docs/sources/prix-fournisseurs-2026-11-19/` ont leur compagnon `.sha256`, conforme (vérifié ici). Leur lecture pour Carbon et Claude est refaite au point 2.
- Avant (11.3) : « Pages de prix : versées ce jour dans `docs/sources/prix-fournisseurs-2026-11-19/` (Anthropic, Google) ; **à sceller** ; OpenAI non lisible ce jour, page scellée du 18 novembre gardée. »
- Après : « Pages de prix : versées et scellées dans `docs/sources/prix-fournisseurs-2026-11-19/` (Anthropic `78aff5c8…`, Google `89c58281…`), lecture de Carbon et de Claude vérifiée par le contre-lecteur ; Carbon est donc compté à 4 et 20 ; OpenAI non lisible ce jour (403, refus versé), page scellée du 18 novembre gardée. »
- Même mise à jour de la phrase « Tant que la page de Google n'est pas scellée… » en 6.1, qui reste vraie comme condition, et de « brouillon 2, non scellé » dans l'en-tête : le fichier a son compagnon (`ae9e75bb…`). Écrire plutôt « scellé comme pièce, non accepté ».

**D4 — le refus de la température n'est pas « sans frais » pour le relais d'OpenAI (non bloquant).** `relais_kimi_v4.py` (lignes 760 à 766) compte au pire cas toute réponse de l'amont sans compteur d'usage, donc aussi un 400, soit ≈ 0,36 à 0,52. Le chef d'essai le compte à zéro.
- Avant (5.5) : « Si le premier envoi d'une file est refusé par un code 400 qui nomme la température (refus sans frais), la file la retire »
- Après : « Si le premier envoi d'une file est refusé par un code 400 qui nomme la température (refus non facturé par le fournisseur, mais compté au pire cas par le relais d'OpenAI, qui ne voit pas de compteur d'usage ; le chef d'essai le compte de même), la file la retire »
- Effet chiffré : dans la file GPT, le plafond laisse alors finir jusqu'à ≈ 4,3 fois la sortie supposée au lieu de 6,3, encore au-dessus du « haut plausible ». Rien à changer au plafond.

## 5. Recommandations (non bloquantes)

- **E1, délais des relais sous ceux du chef d'essai** : le relais d'OpenAI attend par défaut 600 secondes de silence et 1 800 au total (`relais_kimi_v4.py`, lignes 192 et 193). Le relais de Google est réglé à 120 et 180, comme le chef d'essai. Régler chaque relais quelques secondes **sous** le chef d'essai (OpenAI : `--delai-silence-s 230 --delai-amont-s 590` ; Google : 115 et 175), pour que la coupure vienne du relais : elle rend alors un 502 explicite, compté au pire cas des deux côtés, et non une réponse perdue en route.
- **E2, clé Rigaud partagée** : la clé a servi à d'autres courses (`registres/depenses.md`, ligne 522). Si une autre course l'emploie pendant l'essai, ses limites de débit sont partagées. Un 429 arrêterait alors la file Claude, comme écrit. Il suffit de le dire au rapport, sans rien changer.

## 6. Pièces lues

| pièce | empreinte |
|---|---|
| devis, brouillon 2 (branche de la relance) | `ae9e75bba8b8…` |
| contre-lecture du brouillon 1 | `d1b8ad89037c…` |
| `registres/go.md` de `main` (`4f011d247`), lignes 455 et 462 à 465 | registre vivant |
| journal de la relance (branche de la relance), entrées OD-104 à OD-106 | registre vivant |
| `registres/depenses.md` (branche de la relance), lignes 520 à 522 | registre vivant |
| `docs/sources/prix-fournisseurs-2026-11-19/` : page de Google `89c58281…`, page d'Anthropic `78aff5c8…`, refus d'OpenAI `bdc7cafb…`, `provenance.md` `8e84ff79…` | compagnons conformes |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` | `67f369518102…` (lignes 182, 192 à 193, 700 à 780) |
