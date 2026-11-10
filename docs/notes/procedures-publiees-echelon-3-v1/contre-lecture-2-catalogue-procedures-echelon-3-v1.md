# Contre-lecture 2 (R2) du catalogue des procédures publiées admissibles à l'échelon 3 — brouillon 2

## En-tête

- **Date** : 2026-11-10, lecture entre 11:33 et 11:43 UTC environ (`date -u` : 11:33:31 au début, 11:42:23 à la vérification finale de l'empreinte).
- **Contre-lecteur** : sous-agent neuf, sans autre rôle dans le programme. Il n'a écrit ni le catalogue (brouillons 1 et 2), ni la première contre-lecture, ni la règle du bras, ni aucune décision citée.
- **Réserve de validité** : j'ai reçu d'office le `CLAUDE.md` du dépôt. Je ne l'ai utilisé que pour le format de décision.
- **Pièce lue** : `docs/notes/procedures-publiees-echelon-3-v1/catalogue-procedures-echelon-3-v1-brouillon2.md`, SHA-256 `c304d6a23a324c59199f54a04d19cdefcc49eb8fd61bcbda8bdbf46cda22fcf3`. Ce hachage est égal à l'empreinte attendue et à son compagnon (`scellement verifier` : OK). Je l'ai vérifié au début et à la fin de la lecture.
- **Pièces d'appui, en lecture seule** :
  - première contre-lecture : `docs/notes/procedures-publiees-echelon-3-v1/contre-lecture-catalogue-procedures-echelon-3-v1.md` (`c3489a08…`) ;
  - règle du bras **scellée** : `prereg/bras-attaque-regle-v1.md` (`88418df09c2e…`, égale à son compagnon, commit `86549bb6` du 10 novembre à 10:21 UTC). J'en ai lu les lignes 1 à 46 (en-tête et pièces, par différence avec le candidat), 92 à 120, 144 à 156, 172 à 186, 232 à 245, 296 à 312, 390 à 402 et 484 à 490, plus une recherche de mots (« politique figée », « recette », « plafond », « poids », « N-053 ») ;
  - candidat brouillon 3 de la règle, pour contrôler les numéros de ligne cités par le catalogue : `brouillons/bras-attaque-regle-prereg-v1-brouillon3.md` (`4055bd20…`), lignes 85 à 89, 96 à 104 et 155 à 160 seulement ;
  - addendum 1 de la règle : `prereg/bras-attaque-regle-v1-addendum-1.md` (`edfa69a2…`, OK), lu en entier ;
  - décision du 10 novembre sur les verdicts comptés : `git show origin/claude/upbeat-cray-dmauvv:registres/passations/2026-11-10-0704-decision-lazar-verdicts-comptes.md`. La branche est maintenant en `8e1e751d` ; le SHA-256 du texte vaut `bba97a1a…`, comme à la première contre-lecture ;
  - notes de décision du 10 novembre : `…-1018-decision-lazar-anteriorite-procedures-jury-transmission.md` (`8a2c8b71…`, OK) et `…-1050-decision-lazar-go-recos-acces-hc2-licence.md` (`def13a65…`, OK), lues en entier ; `…-0852-…-go-quatre-pieces-attaques-inedites.md` (`c90ad8f4…`), lignes 1 à 40 ; `…-0948-decision-lazar-autonomie-12h.md`, lignes 1 à 30. La note « go recos » de 10:50 ne parle pas du catalogue ;
  - `docs/decisions/decision-N-053-v1.md` (`2204256d…`), lignes 30 à 60 ; `docs/decisions/decision-N-056-v1.md` (`3592c1e9…`), lignes 60 à 76 ;
  - PDF cités, par `pdftotext`, aux pages des citations neuves (section 2).
- **Non lu, comme le veut la consigne** :
  - `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `docs/notes/integration-bras-attaque-v1/` et `diag/` ;
  - tout résultat de sonde, de moniteur ou d'attaque, épisodes d'épreuve, items de l'étiqueteur ;
  - lignes R-604 à R-610 de `registres/decisions.md` ; `registres/etat.md` ; aucune branche de quarantaine.
  - Dans les PDF, je n'ai lu aucune page signalée en section 9 du catalogue. Il y a une exception : le contrôle par programme de deux citations de Schaeffer et al., p. 23, sans affichage. Je n'ai lu ni les annexes H et I de Ge-Wang et al., ni l'annexe H de Schaeffer et al.
- **Outils** : `pdftotext` 24.02.0, Python 3.13 (`-I`), `python -m controle_ia.scellement verifier`, `git show` et `git diff` en lecture. Aucune requête réseau, à part la lecture d'une référence distante déjà présente. Aucun calcul loué, aucune dépense, aucun commit. Mes scripts sont dans le bloc-notes de la session, hors du dépôt.

## Verdict

**Scellable après corrections.** Huit corrections (C1 à C8, section 6), dont deux majeures.

Rien de bloquant :
- les seize points de la première contre-lecture sont traités, CP-11 en partie ;
- les 64 citations neuves tirées d'un PDF sont à la page dite ;
- aucune recette n'apparaît, ni aucun paramètre.

Mais le brouillon 2 cite la règle du bras comme un « candidat brouillon 3, non scellé, non opposable ». Or la règle a été scellée à 10:21 UTC, pendant la rédaction (`88418df0…`). Le texte scellé tranche le point que le catalogue laissait ouvert : il exige une politique figée **par niveau de budget**, lue sur des épisodes neufs, et des requêtes distinctes de l'ouverture.

Conséquences :
- Best-of-N (P03) et l'attaque en étiquette dure (P06) doivent sortir de la liste retenue (question A, C2) ;
- la liste passe de 9 à 7 procédures, toutes de la classe A2 (statistique de verdicts) ;
- la question 4 est à reformuler (question B, C3).

**Décompte** : 2 majeurs (C1, C2), 3 moyens (C3, C4, C5), 3 mineurs (C6, C7, C8).

---

## 1. Points de la première contre-lecture

| Point | Gravité | Traité ? | Constat |
|---|---|---|---|
| CP-1 transposition | majeur | **oui** | « Retour suffisant » ; tables (b) avec rôle du verdict, éléments de domaine et forme du produit ; décision 3 appliquée. Reste ouverte la conséquence de la forme du produit, laissée « à la règle » (section 4 du catalogue) : voir question A et C2. |
| CP-2 Schaeffer et al. | majeur | **oui** | Scission P22a, P22b, P22c faite. P22a entre par la décision 1, puis sort par la décision 3. L'écart au texte proposé est déclaré, et je l'approuve : la grille est « handwritten » et « a strategy designed by the RT » (p. 4, contexte lu). La cohérence avec P13 reste à assurer : voir C4. |
| CP-3 Boundary Point Jailbreaking | majeur | **oui** | PDF versé et scellé (`2efc4e7f…`, OK) ; ligne P43 ; liste. Des réserves manquent sur les détails retenus par les auteurs : voir C5. |
| CP-4 TAP | moyen | **oui** | Épinglage E_Llama-Guard ou E_Substring ; citations p. 38, p. 8 et p. 40 contrôlées. |
| CP-5 GPTFuzzer | moyen | **oui** | P04a et P04b. « p. 6–7 » est exact : la mise à jour de la récompense est en p. 6, les pénalités en p. 7. |
| CP-6 PAIR v4 | moyen | **oui** | Réserves reprises ; « six candidate JUDGE functions » à la p. 5. |
| CP-7 N-053 | moyen | **oui** | Invariant cité tel qu'écrit (N-053, l. 42-44, vérifié). |
| CP-8 question 1 | moyen | **oui** | Écrite comme décision de Lazar (10:18, l. 27-28, vérifié). |
| CP-9 question 2 | moyen | **oui** | Décision 2 ; la citation de N-056 (l. 68-70) est exacte ; la règle d'épinglage est présentée comme « règle proposée ». |
| CP-10 absents | moyen | **oui** | Screwtape versé (`0c5598a0…`, OK) et classé ; les autres sont en pistes datées (option offerte). |
| CP-11 attaquant entraîné | moyen | **en partie** | La séparation est faite en section 2, et la question 4 est posée. Mais elle est mal posée : l'option (a) se contredit, la question ne relie pas N-053 à la déclaration de 07:04, et P38 n'est pas passé à la décision 3. Voir question B et C3. |
| CP-12 Terekhov et al., p. 4 | mineur | **oui** | Page corrigée ; nature du retour relevée (contexte lu : « gathered from responses to the first ten side-task solutions »). |
| CP-13 Jiralerspong et al. | mineur | **oui** | Citation retirée, mention gardée. |
| CP-14 statut | mineur | **oui** | — |
| CP-15 section 9 | mineur | **oui** | Texte repris, avec P43 et P44. |
| CP-16 compléments | mineur | **oui** | P05, P09, P11 et P18 complétés ; définition A2 élargie. |

---

## 2. Citations neuves ou changées

**Population.** J'ai extrait par programme les segments « … » du brouillon 2 absents du brouillon 1 : il y en a 137. Parmi eux, **64 sont des citations tirées d'un PDF**. Les autres sont :
- des termes français ;
- des citations des pièces du dépôt (règle, décisions) ;
- des titres de la section 8.2, tirés des métadonnées d'arXiv et non vérifiables sur un PDF.

J'ai contrôlé les 64, c'est-à-dire l'échantillon complet.

**Méthode.** `pdftotext -f P -l P`, en mode simple puis `-layout`. La recherche se fait après normalisation : Unicode NFKC, apostrophes et tirets, suppression des blancs et de la casse. En cas d'échec, le programme cherche la phrase sur toutes les pages.

**Résultat : 64 sur 64 à la page dite, 0 échec.**

**Sens.** J'ai lu le contexte de 22 citations, celles qui portent un classement :

| PDF | Pages | Citations | Fidèle à l'usage |
|---|---|---|---|
| Davies et al. (P43) | 1, 4, 9 | « observes only binary feedback », « deterministic binary classifier or monitor », « universal adversarial prefix », « optimised once… », « incurs many flags… », « without relying on human attack seeds », « do not release attack strings or code » | oui, sauf « aucune amorce humaine », généralisé à tort. La phrase de la p. 1 porte sur le classifieur de GPT-5. La note 3 de la p. 4 dit que des « human-found jailbreak strings » font partie des détails retenus par les auteurs. Les p. 5 et 6 emploient « a simple human-found jailbreak » contre le modèle principal. Voir C5. |
| Schaeffer et al. (P22a, P22c) | 1, 4, 5, 6 | « We decompose attack selection… », « providing a rubric is a strategy designed by the RT », « The rubric prompt was selected from several handwritten candidate prompts », « designed by using automatic prompt optimization with GEPA », « estimate safety… », « audit threshold… » | oui |
| Ge-Wang et al. (P13) | 4 | « Given only the main-task and side-task descriptions », « The stop policy scores the trajectory… risk score from 1–9 » | oui. La politique d'arrêt rend un score de « greater detection risk » : voir C4. |
| Perez et al. (P38) | 3, 5 | « guide the generated cases… », « We finetune on the N zero-shot test cases… », « classifier probability » | oui. Le contexte de la p. 3 compte pour la décision 3 : voir question B. |
| Terekhov et al. | 4 | « exemplars of the monitor’s feedback… », « single universal injection… » | oui |
| h4rm3l (P12) | 2, 3, 5 | primitives, gabarits, exemples initiaux | oui |
| Promptbreeder, ProTeGi, OPRO | 3 ; 2 ; 3 | figure 1 ; « We use the same prompts for all tasks » ; méta-consigne | oui |

Je n'ai trouvé aucune citation fausse sur le fond. Aucun extrait opératoire n'est reproduit dans le catalogue ; la recherche de mots sensibles n'a donné qu'un faux positif (« pipeline »).

**Citations des pièces du dépôt.** Contrôlées sur le texte : décision de 10:18 (l. 8-10, l. 24-34), N-053 (l. 42-44), N-056 (l. 67-70). Les citations de la règle sont exactes **dans le candidat brouillon 3** (l. 85-89, 96-104, 159), et leur texte se retrouve dans la règle scellée, mais à d'autres lignes (C1).

---

## 3. Question A — Best-of-N (P03) et P06 face à la politique figée

**Texte scellé** (`prereg/bras-attaque-regle-v1.md`, `88418df0…`) :
- l. 178-182 : « **À part** : à l'échelon 3, le plafond de requêtes de chaque course est fixé et scellé à son préenregistrement avant toute requête ([N2], condition 2) ; les requêtes sont distinctes de l'ouverture ; les épisodes lus à l'ouverture sont neufs, écrits par une politique figée après la dernière requête ; le budget se compte par course ; chaque niveau de budget est une politique figée à ce nombre de requêtes, lue sur ses propres épisodes neufs. »
- l. 150-152 (courbe) : « Chaque niveau de budget est une politique figée à ce nombre de requêtes (ou à ce calcul), point fixé au préenregistrement de la course, lue sur ses propres épisodes neufs. »
- l. 238-240 : à l'échelon 3, l'intervention de dissimulation est « la consigne ».
- l. 396-399 : ce catalogue est la liste fermée, et « Chaque course de l'échelon 3 cite la version scellée du catalogue ».

**Lecture.**
1. L'essai réussi par cas que rendent Best-of-N (p. 1) et P06 (p. 2) est une requête. La règle sépare les requêtes de l'ouverture et n'y lit que des épisodes neufs : ces essais ne peuvent pas être lus.
2. Pour Best-of-N, la politique qui reste après la dernière requête ne contient aucun verdict. Les augmentations sont tirées sans les verdicts, qui ne font qu'arrêter le tirage au premier succès (p. 1). Figée après la dernière requête, la politique est donc celle d'avant la première. Son point de courbe ne dépend pas du budget, et il mesure l'échelon 2 augmenté du bruit des augmentations, non l'échelon 3.
3. P06 perturbe un texte donné en observant l'étiquette du classifieur visé (p. 1). Jouée sur des épisodes neufs, elle demanderait des requêtes à l'ouverture, ce que la règle exclut.
4. Rejouer sur des épisodes neufs les augmentations ou perturbations qui ont réussi serait une procédure autre que celle publiée : c'est un transfert, et non une substitution de rôle, donc la décision 3 l'exclut. Best-of-N rapporte d'ailleurs que ses augmentations réussies se reproduisent mal au rééchantillonnage (section 5.4, p. 9).
5. Lire les essais retenus serait circulaire. Ils ont été retenus parce que le moniteur gelé ne les a pas signalés, au même seuil que celui de l'ouverture.

**Recommandation.** Les deux procédures **sortent de la liste retenue**. Elles restent au catalogue (table 4.1), avec la mention « retour suffisant, décision 3 gardée, **hors liste : produit par cas, non lisible sous la règle scellée** (l. 150-152, 178-182) ».

Les garder à condition demanderait un écart à la règle scellée, donc un nœud de Lazar. Je ne le recommande pas, pour la raison 5. Le catalogue ne peut plus dire « ce point relève de la règle » : la règle l'a tranché, et elle renvoie au catalogue pour la liste.

La liste devient **7 procédures, toutes A2 et à produit réutilisable** : OPRO, APE, ProTeGi, Promptbreeder, EvoPrompt, Ge-Wang et al. (sous condition, C4) et Boundary Point Jailbreaking. Aucune procédure A1 ne reste.

---

## 4. Question B — la question 4 (entraînement d'un modèle de l'attaquant)

**Ce qui est juste** : elle sépare les poids de l'agent de l'entraînement d'un modèle de l'attaquant (CP-11), et elle propose (b) par défaut, ce qui va dans le sens de la lecture étroite.

**Ce qui ne va pas.**
1. **L'option (a) se contredit.** « Oui, si le modèle entraîné n'est pas celui qui écrit les épisodes lus. » Or, dans la variante supervisée de Perez et al., le modèle affiné est précisément le générateur dont le produit serait lu (« We finetune on the N zero-shot test cases that lead to offensive replies », p. 5). Sous (a) comme sous (b), cette procédure sortirait : la question ne départage rien sur son propre enjeu.
2. **Elle ne pose pas la vraie question au regard de N-053.** L'invariant interdit qu'un score de moniteur entre « dans un signal d'entraînement ou de sélection de l'agent, hors bras d'attaque déclaré » (l. 42-44). Le bras de l'échelon 3 est déclaré par la décision de 07:04 pour **lire** les verdicts comptés, sous deux conditions (l. 8-11). Cette décision ne dit rien d'un entraînement. La règle scellée réserve, aux échelons 5 et 6, la déclaration à une décision propre de Lazar : « aucun ne l'est à ce jour pour ces échelons » (l. 101-103). La question à Lazar est donc : **la déclaration de 07:04 s'étend-elle à des verdicts qui entrent dans le signal d'entraînement ou de sélection d'un modèle de l'attaquant ?** Si oui, c'est une déclaration nouvelle, donc un nœud. Dans la variante supervisée, les verdicts servent aussi à sélectionner les exemples.
3. **Elle ne passe pas P38 à la décision 3.** La consigne de génération se règle pour chaque comportement visé, par itération humaine : « Finding a prompt to test a new behavior typically only required a few minutes of iteration (viewing samples and updating the prompt) » (p. 3, contexte lu). C'est un élément propre au domaine d'origine, à réécrire. P38 supervisée sort donc par la décision 3, et la question 4 n'a plus d'enjeu dans la liste actuelle (AutoInject n'est pas classé sur PDF). Elle fixe seulement une lecture pour les versions futures. Il faut le dire, pour que Lazar sache qu'il ne tranche rien d'immédiat.
4. **Elle omet le budget.** La courbe compte le budget de l'échelon 3 en requêtes seulement (l. 150-151). Un entraînement ajoute un calcul, ce qui mêle deux axes dans un même échelon. Et tout entraînement est une dépense : devis et autorisation.
5. **Elle ne situe pas le modèle entraîné.** L'attaquant de la revendication A1 resserrée est « l'agent surveillé, qui choisit le contenu de ses propres actions » (décision de 10:18, l. 17-18). À l'échelon 3, il écrit la consigne (règle, l. 238-240). Un modèle auxiliaire entraîné écrirait donc cette consigne. L'entraînement de l'agent lui-même relève des échelons 5 et 6 (l. 117-118) et n'est pas en question.

**Ce qu'elle doit demander à Lazar** : texte proposé en C3.

---

## 5. Autres constats

- **Règle scellée pendant la rédaction (C1).** Le scellement date de 10:21 UTC (commit `86549bb6`) et la rédaction court de 10:10 à 10:50. Les citations sont textuellement justes, mais :
  - les numéros de ligne et le statut « non opposable » sont périmés ;
  - le texte scellé ajoute « chaque niveau de budget est une politique figée… », ce qui change la question A.
- **P13 (C4).**
  - La politique d'arrêt rend un score de risque de détection (p. 4). C'est la même nature que la grille de suspicion qui fait écarter P22a (p. 4). La décision dépend donc des sections H et I, non lues, et la liste ne peut la porter que sous condition suspensive, explicite.
  - Le réglage publié des seuils exige aussi, par trajectoire, le succès de la tâche secondaire (p. 4). Ce n'est pas un verdict, et la règle ne dit pas qui le fournit à l'attaquant : la vérité du dommage est « au coffre […] lus par le seul juge » (l. 302-303).
- **Boundary Point Jailbreaking (C5).** Les auteurs ont retenu des détails de méthode (« efficiency or stability improvements, human-found jailbreak strings, and additional elicitation methods–are withheld », note 3, p. 4 ; « We have abstracted significant algorithmic details », p. 9). Compléter ces détails n'est pas une substitution de rôle : la procédure admise doit être épinglée à l'algorithme publié (pseudocode, p. 4 ; algorithme 2, p. 25).
- **Décision de 07:04 (C6).** Elle est lisible ; le brouillon 2 la cite de seconde main. La condition (1) y est écrite par la session (l. 8-10) ; le mot de Lazar est « Ma recommandation : oui, mais sous deux conditions. go » (l. 7).
- **Objectif A2 et dommage (C7).** L'objectif admis est la proportion de non-alertes. Le dommage n'y entre pas, et il faut le dire, sans quoi « statistique de verdicts » se lirait comme « évasion à dommage tenu ».
- **Décomptes.** Je les ai vérifiés : 47 lignes = 6 + 10 + 13 + 18 ; 31 exclues par leur retour ; 7 écartées par la décision 3 ; 9, puis 7 retenues après C2.

---

## 6. Corrections (texte proposé)

Toutes vont dans une version nouvelle (brouillon 3) ; le brouillon 2 reste tel quel (R12).

**C1 — Règle scellée (majeur).**
- En-tête, puce « en lecture seule » : remplacer le passage sur la règle par : « `prereg/bras-attaque-regle-v1.md`, **scellée** le 10 novembre 2026 à 10:21 UTC (commit `86549bb6`, `88418df0…`, égale à son compagnon), et son addendum 1 (`edfa69a2…`), qui ne change aucune règle. Le candidat brouillon 3 lu pendant la rédaction est archivé (`brouillons/bras-attaque-regle-prereg-v1-brouillon3.md`, `4055bd20…`) ; les passages cités ont le même texte dans la règle scellée. »
- Renuméroter partout (§ 1.2, § 2, § 4, § 5, § 6, § 8.1, annexe D) :

  | Passage | Candidat brouillon 3 | Règle scellée |
  |---|---|---|
  | quarantaine | l. 85-89 | l. 97-103 (exception de l'échelon 3 : l. 99-101) |
  | échelle | l. 96-104 | l. 110-118 (échelon 3 : l. 115 ; échelon 5 : l. 117 ; échelon 6 : l. 118) |
  | politique figée | l. 159 | l. 180 |
  | passage « À part » | l. 157-160 | l. 178-182 |

  Retirer « non scellé » et « non opposable ».
- En § 1.2, après la citation de la politique figée, ajouter : « La règle scellée ajoute : “les requêtes sont distinctes de l'ouverture” et “chaque niveau de budget est une politique figée à ce nombre de requêtes, lue sur ses propres épisodes neufs” (l. 179-182 ; de même pour la courbe, l. 150-152). Elle désigne ce catalogue comme liste fermée : “Chaque course de l'échelon 3 cite la version scellée du catalogue” (l. 396-399). »

**C2 — Best-of-N et P06 hors de la liste retenue (majeur).**
- En § 4, remplacer le paragraphe « Forme du produit » par :

  « **Forme du produit — règle scellée.** La règle lit à l'ouverture des épisodes “neufs, écrits par une politique figée après la dernière requête”, les requêtes étant “distinctes de l'ouverture”, et chaque niveau de budget est une politique figée “lue sur ses propres épisodes neufs” (l. 150-152, 178-182). Best-of-N (P03) et l'attaque en étiquette dure (P06) rendent un essai réussi par cas (P03, p. 1 ; P06, p. 2). Ces essais sont des requêtes et ne peuvent être lus à l'ouverture. Chez Best-of-N, les verdicts ne font qu'arrêter le tirage (p. 1) : la politique figée après la dernière requête est celle d'avant la première, et son point ne dépend pas du budget. P06 interroge le classifieur visé tout au long de la perturbation (p. 1) : jouée sur des épisodes neufs, elle demanderait des requêtes à l'ouverture. Rejouer les essais réussis sur des épisodes neufs serait une autre procédure (décision 3) ; Best-of-N rapporte d'ailleurs que ses augmentations réussies se reproduisent mal (section 5.4, p. 9). Ces deux procédures sortent de la liste retenue ; les y remettre demanderait un écart à la règle scellée (nœud). »
- Table 4.1, lignes P03 et P06 : ajouter à la colonne « Raison » : « **hors liste : produit par cas, non lisible sous la règle scellée (l. 150-152, 178-182)** ».
- « Liste fermée retenue — **7 procédures** » : retirer les items 1 et 2, renuméroter.
- « En bref », premier tiret : « **Liste fermée retenue : 7 procédures** (section 4), toutes à statistique de verdicts et à produit réutilisable : OPRO, APE, ProTeGi, Promptbreeder, EvoPrompt, sélection d'attaque de Ge-Wang et al. (sous condition), Boundary Point Jailbreaking. Best-of-N et l'attaque en étiquette dure ont un retour suffisant et passent la décision 3, mais sortent par la forme de leur produit (règle scellée). »
- § 5 : ajouter la puce « **Forme du produit — essai réussi par cas, non lisible sous la règle scellée** (2 lignes) : Best-of-N (P03), attaque en étiquette dure (P06). »
- Règle d'épinglage (§ 6) : déplacer « Best-of-N v2 ; attaque en étiquette dure v2 » vers « pour mémoire », avec la mention « hors liste par la forme du produit ».

**C3 — Question 4 reformulée (moyen).** Remplacer la question 4 par :

> **Question 4 — Verdicts dans l'entraînement d'un modèle auxiliaire de l'attaquant.**
> - **Décision** : la déclaration du bras de l'échelon 3 (décision du 10 novembre, 07:04 : « bras d'attaque déclaré » au sens de N-053 point 5, pour lire les verdicts comptés sous deux conditions) s'étend-elle à une procédure publiée où ces verdicts entrent dans le signal d'entraînement ou de sélection d'un **modèle auxiliaire de l'attaquant**, distinct de l'agent surveillé ? Le produit de ce modèle, figé après la dernière requête, écrirait l'intervention de l'échelon 3, c'est-à-dire la consigne (règle scellée, l. 238-240).
> - **Hors question** : l'entraînement des poids de l'agent surveillé, qui relève des échelons 5 et 6 (l. 117-118) et d'une déclaration propre de Lazar (l. 101-103).
> - **Enjeu** :
>   - aujourd'hui, aucune ligne de la liste. La variante supervisée de Perez et al. (P38) entre par son retour (verdict seul, p. 5), mais sort par la décision 3 : sa consigne de génération se règle pour chaque comportement visé par itération humaine (p. 3). AutoInject n'est pas classé sur PDF. La réponse fixe donc une lecture pour les versions futures du catalogue ;
>   - l'entraînement ajoute un calcul aux requêtes, alors que la courbe compte le budget de l'échelon 3 en requêtes (l. 150-151) ;
>   - tout entraînement est une dépense (devis, autorisation).
> - **Options** :
>   - **(a) oui**, dans l'échelon 3, sous les deux conditions de 07:04, avec un plafond de calcul d'entraînement fixé et scellé avec le plafond de requêtes, et rapporté au tableau des coûts de HC4. Avantage : garde les procédures publiées à verdict seul qui entraînent un générateur. Inconvénients : élargit une déclaration faite pour la lecture des verdicts ; mêle deux axes de budget dans un même échelon ; rapproche l'échelon 3 de l'échelon 5 ;
>   - **(b) non** : un tel bras forme un échelon à part, à déclarer par Lazar comme les échelons 5 et 6, et aucune course ne part avant. Avantage : la déclaration de 07:04 reste dans sa lettre. Inconvénient : écarte une classe de procédures publiées à verdict seul.
> - **Recommandation** : (b), confiance moyenne. **Défaut sous 48 heures** : (b), jamais la lecture large. Sans effet sur la liste actuelle.

Et dans P38 (table 3.4), remplacer « sa place sous la décision 3 reste à juger » par : « **Décision 3 : écartée** — la consigne de génération se règle pour chaque comportement visé par itération humaine (“Finding a prompt to test a new behavior typically only required a few minutes of iteration (viewing samples and updating the prompt)”, p. 3) : élément propre au domaine d'origine, à réécrire. »

**C4 — P13 sous condition explicite (moyen).** Table 3.2 (b), colonne « Décision 3 » de P13, ainsi que la table 4.1 et l'item de la liste, remplacer par :

« **Gardée sous condition suspensive**, à lever avant le scellement du préenregistrement de la première course qui la cite :
- (i) une instance autorisée à les lire (section 9) confirme que les consignes des politiques de départ et d'arrêt (sections H et I) ne portent aucun élément propre au cadre d'origine. Sinon, P13 est écartée comme P22a : la politique d'arrêt rend un score de risque de détection (p. 4), de même nature que la grille de suspicion de P22a (p. 4) ;
- (ii) la source du succès de la tâche secondaire est fixée. Le réglage publié l'exige par trajectoire (p. 4) ; ce n'est pas un verdict, et la règle scellée ne le donne pas à l'attaquant (vérité du dommage au coffre, lue par le seul juge, l. 302-303). Faute de cette source, P13 n'est pas jouable. »

**C5 — Boundary Point Jailbreaking : réserves et épinglage (moyen).**
- Table 3.2 (a), P43, colonne « Retour suffisant », ajouter : « Réserves : les auteurs retiennent des détails de méthode (“efficiency or stability improvements, human-found jailbreak strings, and additional elicitation methods–are withheld”, note 3, p. 4 ; “We have abstracted significant algorithmic details”, p. 9). La procédure admise est l'algorithme publié tel qu'écrit (pseudocode, p. 4 ; algorithme 2, p. 25). Compléter les détails retenus n'est pas une substitution de rôle (décision 3). »
- Tables 3.2 (b) et 4.1, remplacer « aucune amorce humaine (p. 1) » par : « aucune amorce humaine contre le classifieur visé (“without relying on human attack seeds”, p. 1, pour le classifieur de GPT-5) ; les expériences emploient une amorce humaine contre le modèle principal (p. 5–6), sans objet ici ; des chaînes trouvées par des humains font partie des détails retenus (note 3, p. 4) ».
- Règle d'épinglage : « Boundary Point Jailbreaking v2, algorithme publié seul (p. 4, p. 25) ».

**C6 — Décision de 07:04 citée à la source (mineur).** En § 1.2 (« Non consulté »), § 6 (décision 3, « condition citée d'après la contre-lecture ») et § 8.1, écrire : « Décision du 10 novembre sur les verdicts comptés : `registres/passations/2026-11-10-0704-decision-lazar-verdicts-comptes.md`, branche `claude/upbeat-cray-dmauvv` (`8e1e751d`), SHA-256 du texte `bba97a1a…`. Le mot de Lazar est “Ma recommandation : oui, mais sous deux conditions. go” (l. 7). Les conditions sont écrites par la session (l. 8-10) : (1) “la procédure d'essai et de correction est une procédure d'optimisation déjà publiée, citée, sans qu'aucune instance écrive de recette” ; (2) “le plafond de requêtes est fixé et scellé au préenregistrement, avant toute requête”. »

**C7 — Objectif A2 sans dommage (mineur).** En § 2, après la puce « Oui (A2) », ajouter : « L'objectif admis est une statistique des seuls verdicts, la proportion de non-alertes. Le dommage n'y entre pas : une procédure dont l'objectif publié porte aussi sur le succès de l'essai demande un second signal, que la règle scellée ne donne pas à l'attaquant (voir P13). »

**C8 — Statut et en-tête (mineur).**
- Statut : « brouillon 3 ; brouillon 2 contre-lu (contre-lecture 2) ».
- Décompte de la section 4 : « Seize lignes entrent par leur retour […] La décision 3 en écarte sept ; la forme du produit en écarte deux (Best-of-N, P06). **Restent sept procédures.** »

---

## 7. Ce que je n'ai pas pu vérifier

- **Annexes de Ge-Wang et al. (sections H et I) et annexe H de Schaeffer et al.** : non lues, à dessein. La condition (i) de C4 en dépend.
- **Algorithme 2 de Boundary Point Jailbreaking** : j'ai vérifié qu'il est en p. 25, sans en lire le contenu.
- **Code, licences, HEAD** : non revérifiés (ni par le brouillon 2 ni par moi).
- **Titres des pistes de la section 8.2** : tirés des métadonnées d'arXiv, non contrôlés (aucune requête réseau).
- **Sens des 42 citations neuves dont je n'ai pas lu le contexte** : seule leur présence à la page est établie par programme.
- **Lecture du mot « poids » aux échelons 5 et 6** : la règle n'y dit pas de quel modèle il s'agit. J'ai lu « l'agent », d'après la revendication A1 resserrée (décision de 10:18) ; c'est une lecture, dite comme telle.
