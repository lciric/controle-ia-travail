# Contrôle court du brouillon 3 de l'antériorité du « bras d'attaque informé » — corrections D-1 à D-5 et citations nouvelles

- **Date** : `date -u` au début du contrôle : Tue Nov 10 11:47:49 UTC 2026 ; rapport écrit vers 12 h 10 (temps universel coordonné).
- **Nature** : vérification R2 par un sous-agent neuf (Claude, Opus 5.5). Je n'ai écrit aucune des pièces lues (brouillons 1 à 3, contre-lectures 1 et 2, décision du 10 novembre, règle du bras). Lecture seule : aucun commit, aucun push, aucun `git fetch`, aucune requête réseau, aucune dépense. Seul ce fichier est écrit, **non scellé**, sans compagnon.
- **Consignes reçues d'office** : je reçois d'office le `CLAUDE.md` du dépôt (règles R1 à R14), lu dans le contexte de la session.
- **Réserve de famille** : même famille de modèles que les trois rédacteurs et les deux contre-lecteurs ; mes concordances ne valent pas confirmation indépendante (R2, R13).

## Pièces et empreintes

| Pièce | Empreinte sha256 | Contrôle |
|---|---|---|
| Objet : `docs/notes/anteriorite-bras-informe-v1/anteriorite-bras-informe-v1-brouillon3.md` | `f159051afaf7ff987e045b0e379245a216c5411941d16b351f1ca376498bed23` | égale à l'attendu et au compagnon, **au début et à la fin** du contrôle ; lu par `diff` contre le brouillon 2, plus l'annexe B nouvelle |
| Brouillon 2 : `…/anteriorite-bras-informe-v1-brouillon2.md` | `db02898cf0be2f7aea1d6734a98c50cf1842b1413b4a358233fc611beadb119a` | égale au compagnon ; base du `diff` |
| Contre-lecture 2 : `…/contre-lecture-2-anteriorite-bras-informe-v1.md` | `6e6b1e94213168777b69193089ca9bd69795168d7a500e95d38e05171cddd7b9` | égale au compagnon ; lue en entier |
| N19 : `docs/sources/pdf/anteriorite-bras-informe-v1/alotaibi-2026-defenses-empilees-correlation-echecs-2608.28327v1.pdf` | `01ca21d5ae8d13a6b511fd1ab5f19e2ee54de4ba2d1a87b527c207c1e43242bf` | égale au compagnon et à la copie de la contre-lecture 2 ; 58 p. ; « arXiv:2608.28327v1 [cs.CR] 28 Aug 2026 » en p. 1 ; versé par le commit `cab02e41` (vérifié : `git show --name-only`) |
| N18 : `…/karne-2026-moniteurs-surete-refus-modele-2609.05797v3.pdf` | `eb7be6cafe32808623e11ab7d3f94f232a8bdff5eebf8d449f1f47e3a598d178` | égale au compagnon |
| N15 : `…/ji-an-2025-metacognition-controle-activations-2505.13763v2.pdf` | `b878d094ed08fbc2e0dcdbde0ec3473eec2c8dcdfdadf2c227e7f85ef57ce899` | égale au compagnon |
| Règle scellée `prereg/bras-attaque-regle-v1.md` | `88418df09c2e969cbdc77d220fe59dbf64f866d858ff02a039be5662c6d1f904` | l. 106–118 (échelle des régimes d'accès) seulement, pour juger l'écart (b) de D-1 |

Pages lues en contexte : N19 p. 1, 7, 28–36, 38 (début du § 11.7), 44, 47 ; N18 p. 3, 6, 10, 12–13 (bibliographie) ; N15 p. 4.

**Non lus** (cloisons) : `donnees/` ; `docs/notes/bras-attaque/` ; `docs/notes/programme-et-4-familles-evasion/` ; `docs/notes/integration-bras-attaque-v1/` ; `diag/` ; `registres/decisions.md` ; `registres/etat.md` ; aucun résultat, note ou seuil de sonde ou de moniteur du programme ; aucun résultat d'attaque contre le juge de l'organisme ; aucun épisode d'épreuve ni item de l'étiqueteur ; le corps du brouillon 3 hors des passages modifiés (lu par `diff`). Le tableau 7 (budgets) et le tableau 8 de N19 ont été vus en lisant la p. 29 ; rien n'en est reproduit ici.

**Non vérifié** : les 10 requêtes neuves et l'interrogation par identifiants du brouillon 3 (annexe A, partie 4 ; aucune requête réseau permise) ; la version « v3 » de STACK (2506.24068) et son résumé ; les 124 citations anciennes (contrôlées par la contre-lecture 2, 124 sur 124) ; E28.

**Outils** : `sha256sum` ; `diff` ; `git show --name-only` et `git log` (lecture) ; `pdfinfo` ; `pdftotext -layout` et `-raw`, page par page (`-f N -l N`) ; un script Python écrit par moi, lancé avec `python3 -I` depuis un dossier séparé (`/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/verif-p1-b3-scripts/verif.py`) ; extractions et listes dans `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/verif-p1-b3/`, non versées.

---

## Verdict

**Scellable comme version finale après deux précisions de texte (C-1, C-2 ci-dessous), sous réserve du mot de Lazar sur D-2.** Les textes D-1 à D-5 sont repris ; chaque écart déclaré est juste. Les 17 citations nouvelles sont à la page dite, mot pour mot, et fidèles. La conclusion « aucun nœud neuf pour A2 et A3 » tient. Les deux précisions corrigent une formule trop forte dans la ligne N19 du § 4 (Llama Guard 3 est bien franchi une fois sur cent) et une imprécision dans la « Zone séduisante » (« mêmes entrées » au lieu de « mêmes comportements ») ; aucune ne change une étiquette ni n'exige une nouvelle contre-lecture. Si elles sont reprises telles quelles, seule la citation ajoutée par C-1 (déjà vérifiée ici, p. 35) entre à l'annexe B.

Décompte : **0 bloquant, 0 à corriger, 2 à préciser.**

---

## 1. D-1 à D-5 : reprise des textes proposés

| Point | Repris ? | Constat |
|---|---|---|
| D-1 | **oui, avec écarts déclarés** | Points 1 à 9 présents (en-tête, § 0.2–0.4, § 1, § 3, § 4, § 8, § 10, annexes A et B, « Nœud pour Lazar ? »). Points 2 (sauf la précision (b)), 3, 5, 6 et 8 repris mot pour mot ; point 4 repris avec l'écart (c) ; point 7 avec l'écart (d). |
| D-2 | **oui** | Points 1 à 4 : lecture au § 0.0 (texte proposé, plus un renvoi), titre du § 2 rétabli avec « sans gradient », phrase ajoutée au verdict sur l'énoncé en vigueur mot pour mot, signalement dans « Nœud pour Lazar ? », point 2, marqué « à confirmer par Lazar ». |
| D-3 | **oui** | Texte proposé repris aux deux colonnes de la ligne N15 et au § 8 ; deux citations de N15 p. 4 ajoutées (n° 125, 126), exactes et fidèles (le contexte, p. 4 l. 47–55, décrit bien une régression logistique ajustée par couche sur les étiquettes du jeu de données). |
| D-4 | **oui** | Texte proposé au § 0.6 et dans la cellule CA-13 ; l'ancien texte de consignation gardé « pour mémoire ». |
| D-5 | **(a) en partie ; (b), (c) oui** | (a) : statut « non scellé, en attente », scellement différé sous `anteriorite-bras-informe-v1.md` — écart déclaré, justifié par la consigne du brouillon 3 et conforme à R12. (b) : 17 citations nouvelles, bilan recalculé. (c) : « lecture confirmée par la contre-lecture 2 » aux deux endroits. |

### Écarts déclarés de D-1 : sont-ils justes ?

- **(a) PDF versé par la session mère** : juste. Commit `cab02e41` contient le PDF et son compagnon ; empreinte égale à `01ca21d5…`.
- **(b) les paliers d'AATM portent sur l'accès au modèle cible, pas au moniteur (p. 7, 28, 30–31)** : **juste et utile.** P. 7, tableau 1 : la colonne « What the adversary holds » décrit l'accès au modèle (entrées et sorties, probabilités, poids et gradients) ; la connaissance de la défense est un axe distinct (§ 5.2). P. 28–29 : le signal de la recherche est tiré du modèle cible, et le juge qui note le franchissement est hors de la boucle. P. 30 : « Both columns there re-optimize against each defense », sans dire sous quelle forme la défense entre dans la recherche ; P. 30–31 : chaque palier va avec une classe d'attaque. La règle scellée (l. 113) définit l'échelon 3 par ce qu'on **interroge du moniteur gelé** (verdicts rendus) : l'étiquette « échelon 3, et au-delà » n'est donc qu'un rangement approché, et la précision du brouillon 3, avec « sous une forme que les pages lues ne précisent pas », le dit honnêtement. Remarque, non comptée : on pourrait écrire « échelon 3 au plus près, rangement incertain » ; ce n'est pas nécessaire puisque la précision suit dans la même cellule.
- **(c) ajout de l'attaque de la pile entière (§ 11.3, p. 34–35)** : **juste.** P. 34 : le même adversaire fluide attaque directement la pile assemblée (sept couches, puis six sans Llama Guard) ; le résidu direct est nul dans les deux cas, et la citation n° 139 est exacte. Restreindre « pas informé des deux familles à la fois » à l'analyse par paires est la bonne lecture : dans l'attaque d'un bloc, un même adversaire affronte toutes les couches, Llama Guard et les sondes compris, mais rien ne passe et aucune grandeur conditionnelle n'en sort.
- **(d) réécriture de la première proposition de la « Zone séduisante »** : juste sur le fond (la contre-lecture 2 jugeait cette proposition inexacte, § 6, D-1 « Conséquences » (2), mais ne proposait de remplacer que la seconde : incohérence de la contre-lecture, bien corrigée). La citation de la p. 47 (n° 141) est exacte et fidèle. Une imprécision reste dans le texte neuf : C-2.
- **(e) STACK 2506.24068, « résumé seulement, non opposable »** : juste dans sa forme. N18 cite STACK en p. 3 ; sa bibliographie (p. 12–13) donne McKenzie, Hollinsworth, Tseng et collègues, *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 40, 2026 : conforme à la ligne du § 4. Je n'ai pu vérifier ni l'identifiant arXiv, ni la version « v3 », ni le résumé (aucune requête réseau). La ligne n'a pas de citation et ne porte aucun verdict : il n'en dépend rien.
- **(f) 10 requêtes neuves** : non vérifiées (réseau interdit) ; déclarées en annexe A, partie 4, avec leurs résultats.
- **(g) phrase sur l'origine de N19 au § 3** : exacte (N18 p. 3 ; référence N18 p. 10).

---

## 2. Les 17 citations nouvelles (annexe B, n° 125 à 141)

Méthode : chaque citation est cherchée sur la **seule page dite**, dans les deux extractions (`-layout`, `-raw`), après réduction des espaces, sans aucune tolérance sur les mots, les chiffres ou la casse (une seconde passe tolère seulement les variantes typographiques, mais elle n'a servi à aucune des 17). Je contrôle aussi que la citation **n'est sur aucune autre page**, et que le texte de l'annexe B est bien celui du corps (forme « p. N : « … » », 17 sur 17 trouvées une fois). Le contexte de chaque page a été lu. **Épreuve (R5)** : 1 témoin sain accepté ; 4 altérations refusées (un mot changé, une lettre capitale, un sens inversé, la bonne citation cherchée sur la page voisine) : 5 sur 5.

| n° | Pièce | Page | Sur la page ? | Fidélité |
|---|---|---|---|---|
| 125 | N15 | 4 | oui, mot pour mot | fidèle : directions de régression logistique et de composantes principales |
| 126 | N15 | 4 | oui, mot pour mot | fidèle : axe de régression logistique, appris sur les étiquettes du jeu de données |
| 127 | N19 | 1 | oui, mot pour mot (mode `-raw` ; la mise en colonnes coupe le mode `-layout`) | fidèle : résumé |
| 128 | N19 | 31 | oui, mot pour mot | fidèle : la phrase continue « so the adversary that defeats more of this stack is also the cheaper one to mount » |
| 129 | N19 | 29 | oui, mot pour mot | fidèle : légende du tableau 7 (non reproduit) |
| 130 | N19 | 7 | oui, mot pour mot | fidèle : légende du tableau 1 ; soutient la précision (b) |
| 131 | N19 | 30 | oui, mot pour mot | fidèle : il s'agit de la figure 3 ; la phrase oppose ces colonnes au suffixe statique de transfert |
| 132 | N18 | 6 | oui, mot pour mot | fidèle : seuil partagé de 1 %, gardes et sondes ; les 6 autres paires ne sont pas dans ce cas |
| 133 | N18 | 3 | oui, mot pour mot | fidèle : « under natural rewording », sans attaquant |
| 134 | N19 | 1 | oui, mot pour mot | fidèle : résumé |
| 135 | N19 | 28 | oui, mot pour mot | fidèle : ouverture du § 11 |
| 136 | N19 | 32 | oui, mot pour mot | fidèle : légende du tableau 10 |
| 137 | N19 | 36 | oui, mot pour mot | fidèle, mais la phrase continue avec un résidu de 0,01 sous l'adversaire fluide : voir C-1 |
| 138 | N19 | 34 | oui, mot pour mot | fidèle : cause commune (difficulté des comportements), renvoi au § 11.6 |
| 139 | N19 | 34 | oui, mot pour mot | fidèle : pile de six couches sans Llama Guard ; « joint infeasibility » |
| 140 | N19 | 35 | oui, mot pour mot | fidèle : adversaire adaptatif par défense et par comportement, opposé aux deux références statiques |
| 141 | N19 | 47 | oui, mot pour mot | fidèle : « Research Gaps », point 7 |

**17 sur 17 à la page dite, mot pour mot ; aucune sur une autre page ; toutes fidèles.** Le bilan de l'annexe B du brouillon 3 (« Nouvelles : 17 exactes sur 17 ») est confirmé.

Les autres affirmations nouvelles adossées à N19 ont aussi été contrôlées : « un seul tour, une cible principale peu alignée, une seule graine » (p. 44, 47) ; « seuils réglés sur l'échantillon, sonde dont l'aire sous la courbe de validation est au plafond » (p. 44 ; p. 29) ; « raffinement du classique blanc, gris, noir » (p. 7) ; « Preprint submitted to Elsevier » (pied de chaque page) ; 58 pages ; paires mesurées entre sondes et filtres de surface (tableau 10, p. 32). Toutes exactes. Aucun réglage d'attaque (tableau 7) ni seuil de défense (tableau 8) n'est reproduit dans le brouillon 3 (recherche des valeurs et des termes de ces tableaux : rien, hors le nom de la méthode publiée dans la citation n° 128).

---

## 3. « Aucun nœud neuf pour A2 et A3 » : la conclusion tient-elle ?

**Oui.**

- **A2.** N19 gradue l'accès de l'adversaire **au modèle cible** (p. 7) ; deux paliers seulement sont mesurés, chacun avec sa classe d'attaque (p. 30–31) ; le budget est fixe (p. 29) ; il n'y a ni agent, ni écriture des activations, ni réglage fin, ni renforcement mesurés. Ce que garde l'énoncé resserré (les cinq échelons sur une même famille gelée, réglage des poids compris, l'agent pour attaquant, le succès selon un coût) n'est pas occupé. L'idée d'échelle était déjà dite non revendicable ; N19 s'ajoute à E3 et N8 comme voisin. Aucune étiquette ne change.
- **A3.** N19 mesure la dépendance des échecs paire par paire sous adversaire adaptatif, mais : (i) la défense sémantique textuelle (Llama Guard 3) est hors des paires (p. 32) et presque jamais franchie (0,01 sous l'adversaire fluide, p. 36) ; (ii) l'adversaire est réoptimisé défense par défense (p. 30, 35), si bien que « franchies ensemble » veut dire **sur le même comportement**, chacune avec son propre texte d'attaque, pas sur la même entrée ; (iii) l'attaque de la pile d'un bloc, seul cas où les mêmes entrées affrontent les deux familles, ne fait rien passer (p. 34) ; (iv) un seul tour, pas d'agent, pas de sabotage (p. 44, 47). La seule observation conditionnelle du texte lu est la dominance de Llama Guard (p. 35) : sur le seul comportement où il est franchi, toutes les autres défenses, sondes comprises, le sont aussi. C'est le signe de N18, mais sur un seul comportement et avec des attaques séparées : sans portée pour la probabilité conditionnelle de A3 (voir C-1, qui la fait entrer dans le texte).
- **R8.** Ces manques sont des limites de N19, et les auteurs le disent eux-mêmes : le cadre « multi-turn and agentic » et « the rows this experiment could not test » (dont la rangée sémantique, p. 44) sont « still unmeasured » (p. 47). Le brouillon 3 en tire la bonne conséquence : un **risque de collision** (une suite naturelle de N19 occuperait la zone), à revérifier par les citants de N19 avant toute revendication, et non une zone libre. C'est conforme à R8 ; je n'y vois aucun « trou du champ » revendiqué.

La seule réserve vient de D-2 et non de N19 : si Lazar lit l'énoncé A1 resserré seul, N1 et E7 deviennent des occupants partiels, et cela ferait un nœud. Le brouillon 3 le dit (« Nœud pour Lazar ? », point 2).

---

## 4. Corrections exactes

### C-1 — à préciser — ligne N19 du tableau A3 (§ 4, l. 359) et « Nœud pour Lazar ? », point 1.2 (l. 32) : Llama Guard 3 est franchi une fois sur cent

- **Pourquoi** : la colonne « ne fait pas » dit « aucun moniteur textuel sémantique trompé (paires du classifieur sémantique omises) ». Or p. 36 : Llama Guard 3 a un résidu de 0,01 sous l'adversaire fluide (un comportement sur 100), et p. 35 : « Llama Guard dominates every other member outright: there is no behavior on which it is breached while another defense holds » (vérifiée sur la page, mot pour mot). C'est une observation conditionnelle de même signe que N18, sur un seul comportement, avec des attaques optimisées défense par défense. Elle ne change rien, mais la formule actuelle est trop forte et le passage la tait (R4).
- **Texte** : l. 359, remplacer
  « aucun moniteur textuel sémantique trompé (paires du classifieur sémantique omises) »
  par
  « moniteur textuel sémantique presque jamais trompé : Llama Guard 3 est franchi sur un comportement sur 100 sous l'adversaire fluide (p. 36), et ses paires sont omises (p. 32) ; sur ce seul comportement, toutes les autres défenses, sondes comprises, sont aussi franchies (p. 35 : « Llama Guard dominates every other member outright: there is no behavior on which it is breached while another defense holds »), chacune par sa propre attaque : observation conditionnelle sur un seul comportement, sans portée pour A3 »
- l. 32, remplacer « aucune probabilité conditionnelle n'est rapportée » par « aucune probabilité conditionnelle n'est rapportée (hors la dominance de Llama Guard, sur un seul comportement, p. 35) ».
- Annexe B : ajouter n° 142, N19, p. 35, « exacte », la citation ci-dessus ; bilan : 142 citations, 133 exactes, 9 normalisées. § 1, pièces décisives de A3 : « N19 p. 1, 28, 32, 34–36 » inchangé (p. 35 y est déjà).

### C-2 — à préciser — « Zone séduisante (R8) » (§ 4, l. 378) : « mêmes entrées »

- **Pourquoi** : dans l'analyse par paires, chaque défense est attaquée par sa propre recherche (p. 30, 35) : les deux familles sont franchies sur les mêmes **comportements**, pas sur les mêmes entrées. Les mêmes entrées n'affrontent les deux familles que dans l'attaque de la pile d'un bloc (p. 34), qui ne fait rien passer. La parenthèse qui suit dit d'ailleurs déjà « sur les mêmes comportements ».
- **Texte** : remplacer « dispose à la fois d'un adversaire adaptatif et des deux familles sur les mêmes entrées, hors agent » par « dispose à la fois d'un adversaire adaptatif et des deux familles sur les mêmes comportements (et, dans l'attaque de la pile d'un bloc, sur les mêmes entrées, p. 34), hors agent ».

Aucune autre correction. Ces deux textes repris tels quels, une nouvelle vérification n'est nécessaire que pour la citation n° 142, déjà contrôlée ici (p. 35, mot pour mot).

---

## 5. Ce que je n'ai pas vérifié

1. Le corps du brouillon 3 hors des passages que le `diff` montre modifiés ; les 124 citations anciennes et les 45 citations de notes et registres (contrôlées par la contre-lecture 2).
2. Les requêtes de l'annexe A, partie 4, et le résumé de STACK (réseau interdit) ; aucune recherche neuve.
3. N19 hors des p. 1, 7, 28–36, 38 (début), 44, 47 ; ses § 11.6 à 11.10 et ses annexes, ses citants ; figures et tableaux connus par leur seul texte extrait.
4. Aucune image de page.
