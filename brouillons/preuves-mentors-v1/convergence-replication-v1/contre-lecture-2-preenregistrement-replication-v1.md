# Contre-lecture 2 (R2) du préenregistrement de réplication sur graine neuve de la course de convergence des règles de défense — brouillon 2 — rapport v1

**Verdict : scellable après corrections mineures (listées) — 13 remarques « CL2-nn » au § 3, dont 7 obligatoires ; aucune ne change les hypothèses, les prédictions chiffrées, les seuils, les tables de lecture, la spécification v2, le code v3, l'implémentation B v2 ni les essais (donc ni nouveau journal d'essais, ni nouvelle validation de B).**

- Contre-lecteur : sous-agent neuf (Claude Opus 5.5, identifiant non fourni par l'environnement). N'a écrit aucune pièce de la chaîne (course originale, code v2 ou v3, arène v4, spécification v1 ou v2, brouillons, implémentation B, contre-lecture 1).
- Date : 2 novembre 2026, ≈ 00:30 UTC. Aucun fichier existant modifié, aucun réseau, aucun commit, aucune ref `donnees/*`, aucune clé lue. Seul fichier créé dans le dépôt : celui-ci. Calculs sous `nice -n 10`, dans le dossier temporaire de la session. **La course n'a pas été lancée** ; aucun essai lent rejoué ; **aucune racine n'a été dérivée d'un brouillon de ce texte**.
- Objet lu en entier : `brouillons/preuves-mentors-v1/convergence-replication-v1/preenregistrement-replication-convergence-v1-brouillon2.md`, 433 lignes, empreinte `74c66bd38e5288c65128ffddcd08d5ba7442cde9797c8fb7b58308b01ae32a0d`. Lus avec lui : le brouillon 1 (`f0fd0787…`, diff), la contre-lecture 1 (`2a1cf1af…`, CL-01 à CL-14), les spécifications v2 (`977dd909…`) et v1 (`2a1ad6d3…`), l'état des lieux (`445b31ad…`), le code v3 (`3519123b…`) et le code v2 (`9f0dcf5e…`, diff complet), les deux fichiers d'essais du code v3, le journal des essais (`a506cd44…`), la consigne de B v2 (`14bfa3b4…`), le rapport de validation de B v2 (`.md` et `.json`) et l'interface de `implementation_b_v2.py`, le script de puissance et sa sortie, le manifeste de la course originale, `src/controle_ia/prereg.py`, `scellement.py`, la partie `ecrire_resultat` de `manifeste.py`, les décisions R-1075, R-1079 et R-1086 de `registres/decisions.md`.
- « CL2-nn » = remarque numéro nn de cette contre-lecture. « Obligatoire » = à appliquer avant le scellement ; « recommandée » = à appliquer sauf raison écrite. Les numéros de ligne sont ceux du brouillon 2 (433 lignes).

## 1. En six lignes

1. **Le dessin tient.** La réplication teste ce qu'elle dit tester (la dépendance à la graine), avec des lectures au moins aussi strictes que l'original (taille 0,05 au lieu de 0,02 pour le mélange ; classe d'équivalence exigée aux deux budgets au lieu d'un seul pour la défense figée). Les corrections CL-01 à CL-14 de la contre-lecture 1 sont toutes appliquées.
2. **Le code v3 ne change que ce qui est déclaré.** Mon propre diff v2 → v3 (18 blocs) ne touche que les changements C1 à C12 ; le bloc d'identité régénéré est identique au texte ; les essais rapides repassent (38 passés, 5 lents sautés).
3. **L'implémentation B v2 est la bonne et elle est valide** : les quatre empreintes demandées sont exactes ; ses 560 essais repassent chez moi ; rejouée sur la course originale, elle rend au bit sa sortie de validation (hors métadonnées) ; sa lecture du manifeste correspond à la structure réelle écrite par la course.
4. **Un défaut bloquant à corriger dans le texte, non dans le code** : le contrôle de plomberie V0 (h) exige que B n'ait ouvert que « les entrées », alors que B a légitimement ouvert sa consigne, ses fichiers v1 et ses fichiers temporaires ; tel quel, le lecteur devrait déclarer la réplication « non jugeable (plomberie) » (CL2-01).
5. **Deux suites manquent** : que faire après un arrêt « graines non neuves » (dont le cas extrême, réplication identique à l'original, qui doit être audité par symétrie) et après une discordance entre les deux calculs ou un refus d'entrée de B (CL2-02, CL2-03).
6. **Le reste est de la mise à jour** : décisions de Lazar du 1er novembre à 23:50 (R-1086, point 5 : N = 100, seuil « plus de 2 », B par Claude Sonnet 5.5) à citer, étapes 0, 3 et 7 du plan d'exécution à mettre à jour, compagnons `.sha256` absents des pièces de la réplication (règle R6), et les cinq marqueurs « À REMPLIR » (contenu exact au § 4).

## 2. Verdict point par point

| Point | Verdict | Ce que j'ai trouvé | Corrections |
|---|---|---|---|
| A. Complétude R1 | **à corriger (mineur)** | Présents : hypothèses signées, prédictions chiffrées avec confiance et réfutation (PR1 à PR2), métrique, seuils, plan, V0 (a) à (k), Tables R1, R0, R3, Rii, déclencheurs TR1 à TR4, issue globale à 8 lignes, phrases d'issue, conséquences, liste d'arrêt. Le cas « la réplication contredit l'original » est écrit (échec ; réussite partielle ; défense figée meilleure). Manquent : la suite d'un arrêt « graines non neuves », la suite d'une discordance A/B ou d'un refus d'entrée de B, une phrase pour un « non jugeable » lu mais non tranché. | CL2-02, CL2-03, CL2-12 |
| B. Statistique | **conforme** | Signe par borne (B2, 98,75 % bilatéral), taille par estimation ponctuelle, déclaré (CL-09). Multiplicité : B2 a les quantiles d'un Bonferroni à quatre tests (prudent) ; « aux deux budgets » est une intersection (aucune correction nécessaire) ; TR1 est un Bonferroni à 5 % sur quatre contrastes, valable quelle que soit la dépendance. Unité : l'instance (rééchantillonnage apparié par instance, budget par budget ; bornes marginales lues par intersection ; corrélation entre budgets déclarée, l. 144) ; σ_π suppose l'indépendance entre course originale et réplication, juste puisque la loi cible de chaque instance est tirée de la racine. Recalculs indépendants : HR1 réduit de moitié 0,654 (script : 0,648 ; analytique 0,652) ; HRép0 au niveau 1 0,899 (script : 0,903) ; écarts dans l'erreur de Monte-Carlo (≈ 0,003). Seuil G = 2 : 0,0808 coïncidence attendue au pire, P(> 2) = 8,28 × 10⁻⁵ (texte : 0,081 et 8,3 × 10⁻⁵), aucune valeur répétée en masse (pas d'atome à 0). | — |
| C. Graines | **conforme ; précisions recommandées** | Règle D sans ambiguïté : H = SHA-256 des octets exacts du texte scellé (`sceller` n'écrit que le compagnon, il ne modifie pas le texte) ; entropie int(H, 16), sans clé de descendance ; deux mots de 64 bits ; ρ = premier, ρ_t = second ; vecteurs d'essai retrouvés par B et par E1. Parade : procédurale, avec trace (V0 (k)) ; elle ne dit pas qu'il est aussi interdit de sceller hors du dépôt une variante du texte, ni que jouer quelques tâches donne déjà une information partielle. « Plus de 2 » : strictement plus de 2 tâches sur 200 (les deux budgets), pour chacun des 15 comptes (5 variantes × V, X̄, (ii)), égalité au bit ; même sens dans le texte (l. 191, 274, 393), la spécification (§ 10.3) et B (essai rejoué : 15 comptes à 200 → code 3). Aucun manifeste de réplication ni texte scellé de réplication dans l'historique (point de départ de V0 (k) : zéro). | CL2-10 |
| D. Fidélité | **conforme ; commande de B à écrire** | Diff v2 → v3 : uniquement C1 à C12 (§ 5.2). Commande de la course : mêmes options que la ligne de commande de v2 et que le manifeste original ; `--instances 0:100`, `LAMBDA_RETENU = 0.3`, `REFERENCE_RETENUE = moyenne` présents ; `DEPOT = ICI.parents[3]` désigne bien la racine (le code v3 est à la même profondeur que v2), dans la copie propre comme dans l'arbre ; arène v4, gel v2 et code v2 suivis par git. Commande de B : conforme à la spécification une fois les chemins complétés ; clés lues dans le manifeste (`config.racine`, `config.racine_chaine`, `preenregistrement.sha256`, `config.config.n_instances`…) toutes présentes dans la structure réelle écrite par `creer_manifeste` ; compagnons au format exigé par B. Le texte ne fige pas cette commande (étape 7) et les étapes 0 et 3 sont périmées. Risque résiduel : B n'a jamais lu une vraie sortie de réplication (impossible avant la course : B exige N = 100 et la configuration épinglée). | CL2-06, CL2-03 |
| E. Lectures préalables | **à compléter (recommandé)** | Déclaré pour les auteurs des brouillons (l. 172). Non dit : personne n'est aveugle à l'original (code v3, B, contre-lecteurs, lecteur, auditeur) ; pour le mélange, l'original exclut déjà presque toute graine favorable (18 et 29 erreurs-types), donc une réussite est surtout une preuve de procédure ; c'est la défense figée qui reste incertaine. L'état des lieux le dit (§ 5), pas le texte. | CL2-08 |
| F. Revendications | **conforme ; une précision** | « Ce que l'expérience n'autorise pas » couvre graine seule, capacité du mélange, attaquant local, même simulateur, sens de « ≈ », deux budgets corrélés, aucun vrai modèle. À préciser : B est un autre modèle (Claude Sonnet 5.5), du même fournisseur que les auteurs (Claude Opus 5.5) ; son propre rapport écrit « famille Claude ». | CL2-09 |
| G. Provenance | **conforme ; compagnons à écrire** | 28 empreintes distinctes de 64 chiffres dans le brouillon : 28 exactes (§ 5.1). Les quatre empreintes de B v2 données par la mission : exactes, compagnons conformes, identiques dans le commit `6151e597`. Mais aucune des pièces propres à la réplication (code v3, essais, journal, spécifications, script de puissance et sortie, consigne, état des lieux, contre-lecture 1, brouillons) n'a de compagnon `.sha256` (R6) ; la consigne et l'état des lieux ne sont pas cités par empreinte. Le rapport de validation de B ne cite pas l'empreinte du code validé (je l'ai rattachée par rejeu). | CL2-04, CL2-13 |
| H. Symétrie R4 | **à corriger (mineur)** | TR1 est bilatéral (un résultat plus beau déclenche comme un plus faible), TR2 couvre « trop propre », TR3 « défense figée plus belle », TR4 la non-réplication. Mais le cas extrême du « trop beau », la réplication identique à l'original au bit près, finit en arrêt « graines non neuves » sans audit prescrit ni suite ; et seule une issue défavorable ou trop belle fait rejouer deux tâches (point (4) de l'audit). | CL2-02 ; CL2-11 |
| I. Marqueurs | **5 marqueurs ; contenu prêt** | « À REMPLIR » aux l. 10, 41, 242, 409, 433 (§ 4). Le validateur voit aujourd'hui « Plan d'analyse » (l. 242) et « Contre-lecture » (l. 433) ; il verra les autres une fois ces deux sections remplies. Ne sont vus par aucun validateur : le titre, le statut, la date de scellement (l. 9), les mentions « ce brouillon ». | CL2-07 |

## 3. Corrections, avec texte de remplacement prêt à coller

Chaque bloc `text` remplace exactement le passage indiqué.

### CL2-01 — Fichiers que B peut ouvrir : V0 (h) et § Plan 4 « Entrées » (points D, G) — obligatoire

Lignes 242 et 274 (V0 (h)). Constat : V0 (h) exige une « liste des fichiers ouverts par B limitée aux entrées du § Plan 4 », et le § Plan 4 ne nomme que les fichiers de `entrees/`. Or la liste exhaustive du rapport de validation de B v2 (`a29437b0…`, § « Fichiers ouverts ») contient en plus, légitimement : la consigne `consigne-implementation-b-v2.md` (dossier parent, transmise par la session), les consignes permanentes `CLAUDE.md` (injectées par l'environnement), ses propres fichiers v1 sous `implementation-b/`, ses fichiers temporaires (dossier temporaire de la session, `/tmp/pytest-of-root/`), l'interpréteur. Tel quel, le lecteur R13 devrait déclarer V0 (h) fausse, donc « non jugeable (plomberie) ». À noter aussi : le dossier temporaire de la session, que B dit avoir listé (noms seulement), contient une extraction de la branche n67 (code v2, préenregistrement original) ; l'isolement de B est déclaratif.

Remplacer la ligne 242 par :

```text
**Entrées (listes fermées).** Pour la validation : les trois fichiers de `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/` : la spécification **v2** (copie octet pour octet, `977dd9092cbd3715bd2cc9b5d5839f276242ad3f9df6302d383555f2b2ff511a`, version finale, inchangée après la contre-lecture 2), les résultats originaux `d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b`, l'analyse originale `18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42` ; la spécification v1 qui y est déjà reste lisible par B (B l'a écrite d'après elle). Pour la course : en plus, E1, E2, E3 et E5 de la réplication (spécification § 3 : résultats, manifeste, ce texte scellé, analyse de A) et leurs compagnons, à leurs chemins du dépôt. **Fichiers que B peut ouvrir en outre (liste fermée)** : sa consigne `brouillons/preuves-mentors-v1/convergence-replication-v1/consigne-implementation-b-v2.md` (`14bfa3b44d3d0ab0930847feac7df12f0fd03321bbf1b14a14a3bf0d93df15c5`) ; ses propres fichiers sous `implementation-b/` (v1 et v2) ; les fichiers temporaires qu'elle écrit elle-même (dossier temporaire de la session, `/tmp/pytest-of-root/`), supprimés à la fin ; les consignes permanentes `CLAUDE.md`, injectées par l'environnement ; l'interpréteur `/home/claude/controle-ia-travail/.venv/bin/python` et ses bibliothèques. **B n'a pas accès** au code v2, au code v3, à l'arène v4, au préenregistrement original, à sa lecture, à son audit, aux contre-lectures ni à ce texte avant son scellement : elle travaille dans `implementation-b/`, avec la consigne écrite de ne rien ouvrir hors de ces listes, et son rapport donne la **liste de tous les fichiers qu'elle a ouverts** (lecture ou exécution), comparée par le lecteur à ces listes. **Réserve déclarée** : cet isolement est déclaratif ; le dossier temporaire de la session, que B v2 a listé (noms seulement, selon son rapport), contient une extraction de la branche n67 (code v2, préenregistrement original) ; la protection effective est la validation de B sur des branches synthétiques (spécification § 12.2) et la concordance A/B. Famille du modèle de B : Claude Sonnet 5.5 (identifiant `claude-sonnet-5-5`, déclaré dans `validation-b-v2.md`, `a29437b0…`, l. 5 et 271) — autre modèle que l'auteur de la spécification et du code v3 (Claude Opus 5.5), même fournisseur (Anthropic) ; retenu par Lazar comme « autre famille » (R-1086, point 5). La famille de B v1 n'est pas déclarée dans `validation-b-v1.md` ; la course n'emploie que B v2.
```

Dans la ligne 274, remplacer la clause (h) par :

```text
(h) implémentation B v2 : code, essais, rapport de validation et leurs empreintes (celles de la ligne « Implémentation indépendante B (v2) » du bloc d'identité) présents dans le commit du manifeste ou l'un de ses ancêtres (`git merge-base --is-ancestor`) ; validation passée (§ Plan 4, points (1) à (5)) ; fichiers ouverts par B pendant son écriture et sa validation (liste de son rapport) contenus dans les listes fermées du § Plan 4 (entrées et « fichiers que B peut ouvrir en outre ») ; fichiers lus par B pendant la course (`empreintes_fichiers` de sa sortie) exactement E1, E2, E3, E5, les deux fichiers E4 de `entrees/` et leurs compagnons ;
```

### CL2-02 — « Graines non neuves », dont la réplication identique à l'original : audit et suite (points H, A) — obligatoire

Lignes 393, 366 et section « Déclencheurs d'audit ». Constat : une réplication identique à l'original au bit près (le « trop beau » absolu de la règle R4) déclenche l'arrêt « graines non neuves » (code 3), donc « non jugeable (plomberie) », puis « reprise selon la liste d'arrêt ». Mais aucune reprise n'est écrite pour ce motif : le Plan 7 ne traite que l'interruption (même texte, mêmes racines : le même défaut reviendrait) et l'arrêt par garde interne ; la ligne 393 dit « l'audit peut la requalifier » sans prescrire d'audit, alors que les déclencheurs TR1 à TR4 ne sont jamais évalués (lecture bloquée).

Remplacer la ligne 393 par :

```text
| Graines non neuves : plus de 2 tâches égales au bit à l'original, pour une variante, sur V, X̄ ou (ii) (cas extrême : réplication identique à l'original au bit près) | arrêt après la course et avant toute lecture (B : code 3, `lecture_autorisee: false`) ; issue globale ligne 1 (« non jugeable (plomberie) ») ; **audit obligatoire** par un sous-agent neuf (contenu de l'audit, points (1), (2), (4) et (6)), rapport scellé, qui peut requalifier l'issue en « non jugeable (artefact) » ; **aucune reprise sur ce texte** (mêmes racines, même défaut) ; version nouvelle seulement sur décision de Lazar, rapportée avec celle-ci | calculé par B, recompté par le lecteur ; spécification § 10.3 ; testé cas sain et artefact (§ Plan 4, point (3)) |
```

Remplacer la ligne 366 par :

```text
1. non jugeable (plomberie) : aucune phrase sur la réplication ; Lazar informé du motif ; suite selon le motif : interruption → Plan 7 ; « graines non neuves » → audit obligatoire, aucune reprise sur ce texte (liste d'arrêt) ; discordance A/B ou arrêt de B → suite écrite d'avance (§ Issues écrites d'avance) ; autre condition de la liste d'arrêt → l'action de sa ligne.
```

Ajouter, sous la puce TR4 de « Déclencheurs d'audit » :

```text
L'arrêt « graines non neuves » (liste d'arrêt) entraîne lui aussi l'audit, avant toute lecture, quel que soit le sens des écarts.
```

### CL2-03 — Issue écrite d'avance « A et B divergent » et suite d'un refus d'entrée de B (points A, D) — obligatoire

Lignes 362, 392, 394. Constat : la discordance A/B (arrêt, code 3) et le refus d'entrée de B (code 2) aboutissent à « non jugeable (plomberie) » et à un « diagnostic par un sous-agent neuf », sans phrase propre ni suite écrite. Or (i) la suite naturelle d'une erreur de B est une version neuve de B, ce qui est une correction après la course ; (ii) B n'a été essayée en mode réplication que sur des pièces synthétiques construites d'après la spécification (son rapport le dit, § « Ce que cette validation ne couvre pas ») : un refus d'entrée sur un format réel n'est pas exclu, même si j'ai vérifié que les clés lues par B existent dans la structure réelle du manifeste ; (iii) si l'erreur est dans A, la même fonction a produit l'analyse de la course originale (E6 bis).

Ajouter après la ligne 362 :

```text
- **Discordance A/B ou arrêt de B (non jugeable, plomberie)** : « Les deux calculs de la statistique, écrits indépendamment (le code de la course et l'implémentation B, d'après la spécification seule), ne concordent pas, ou B a refusé ses entrées (motif : … ) ; aucune phrase sur la réplication. » **Suite, écrite d'avance** : (a) un sous-agent neuf fait le diagnostic ; pour un code 3, il est seul à lire la sortie de B ; pour un code 2, il ne lit que le motif ; son rapport, scellé, dit si l'écart vient de A, de B, de la spécification ou d'un format ; (b) si la cause est une erreur de B, ou un format écrit par le code de la course que B lit trop strictement : une version neuve de B (fichier neuf), validée comme B v2 (§ Plan 4) et commitée, est lancée **sur décision de Lazar** (nœud), et la lecture porte la mention « après correction de l'implémentation B, écart au préenregistrement » ; (c) si la cause est dans l'analyse du code de la course (A) : la même fonction a produit l'analyse de la course originale (E6 bis) ; l'erreur est rapportée à Lazar pour les deux courses et aucune lecture n'a lieu sans sa décision ; (d) dans tous les cas, aucune seconde course sur ce texte.
```

Remplacer la ligne 392 par :

```text
| B rend le code 2 (arrêt d'entrée : empreinte, compagnon, format, garde d'entrée, racines, champ de E2) | arrêt ; aucune lecture ; diagnostic par un sous-agent neuf, qui ne lit que le motif ; suite écrite d'avance (§ Issues écrites d'avance, « Discordance A/B ou arrêt de B ») | spécification § 3, § 11.1 |
```

Dans la ligne 394, remplacer « diagnostic par un sous-agent neuf ; toute correction après lecture » par :

```text
diagnostic par un sous-agent neuf ; suite écrite d'avance (§ Issues écrites d'avance, « Discordance A/B ou arrêt de B ») ; toute correction après lecture
```

### CL2-04 — Règle R6 : compagnons `.sha256` et pièces citées par empreinte (point G) — obligatoire

Lignes 11 à 25 et 41. Constat : aucune pièce propre à la réplication n'a de compagnon `.sha256` (vérifié sur disque : `code/`, `journaux/` et le dossier n'en contiennent aucun ; seuls les fichiers de B v2 en ont). R6 : « tout dépôt reçoit une empreinte compagnon ». La consigne de B v2 (qui fixe ce que B peut ouvrir, CL2-01), l'état des lieux et la sortie de validation de B ne sont pas cités par empreinte.

Avant le scellement, sceller (session principale) :

```text
cd /home/claude/controle-ia-travail && D=brouillons/preuves-mentors-v1/convergence-replication-v1 && PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller $D/code/arene_regles_defense_v3.py $D/code/test_arene_regles_defense_v3.py $D/code/test_arene_regles_defense_v3_complements.py $D/journaux/journal-essais-code-v3-v1.log $D/specification-statistique-decisive-v1.md $D/specification-statistique-decisive-v2.md $D/puissance-replication-v1.py $D/puissance-replication-v1-sortie.txt $D/consigne-implementation-b-v2.md $D/etat-des-lieux-v1.md $D/contre-lecture-preenregistrement-replication-v1.md $D/preenregistrement-replication-convergence-v1-brouillon1.md $D/preenregistrement-replication-convergence-v1-brouillon2.md $D/contre-lecture-2-preenregistrement-replication-v1.md
```

(Les compagnons n'altèrent aucun essai : `test_pieces_epinglees` et E5 ne lisent que les fichiers eux-mêmes.)

Ajouter après la ligne 25 :

```text
  - consigne de B v2 `brouillons/preuves-mentors-v1/convergence-replication-v1/consigne-implementation-b-v2.md` — `14bfa3b44d3d0ab0930847feac7df12f0fd03321bbf1b14a14a3bf0d93df15c5` ; état des lieux `…/etat-des-lieux-v1.md` — `445b31ad9ef283420fcec75b5e78359ebcf989ed0eb5fe30af67ecc25ebae1bc` ;
  - implémentation B v2 : code, essais et rapport de validation à la ligne « Implémentation indépendante B (v2) » du bloc d'identité ; sortie de validation sur la course originale `…/implementation-b/sortie-b-originale-v2.json` — `11582b6db4aaec236952ef28756d72c1cdf7b46fa6f2587d85aa02d64af95d1d` ;
  - contre-lecture 2 `brouillons/preuves-mentors-v1/convergence-replication-v1/contre-lecture-2-preenregistrement-replication-v1.md` — empreinte de la section « Contre-lecture » ;
  - chaque pièce de ce dossier a son compagnon `.sha256` (R6), écrit par `controle_ia.scellement sceller` avant le scellement de ce texte.
```

### CL2-05 — Décisions de Lazar : R-1086, point 5 (points A, F) — obligatoire

Lignes 135, 191, 195, 200, 413. Constat : le brouillon 2 (≈ 22:25 UTC) précède le mot de Lazar consigné en R-1086 (1er novembre, 23:50 heure de Paris : « go pour toutes tes recos par anticipation »), qui retient nommément pour cette réplication « N = 100, seuil “graines neuves” > 2, implémentation B par une autre famille (Sonnet) ». Le texte présente encore N et le seuil comme des défauts de session révisables.

Remplacer la ligne 135 par :

```text
7. **Décisions** : N = 100, le seuil « graines neuves » à plus de 2 tâches sur V, X̄ ou (ii), et l'implémentation B par un autre modèle (Claude Sonnet 5.5) ont été retenus par toi le 1er novembre à 23:50, heure de Paris (« go pour toutes tes recos par anticipation », R-1086, point 5) ; N avait d'abord été retenu par défaut de la session (R-1079). Ils peuvent changer avant le scellement, jamais après (un texte modifié est une course nouvelle). **GO de la course** : ton « go » du 1er novembre (21:36, heure de Paris), consigné en R-1075, porte nommément sur la réplication de la course de convergence, et R-1086 le confirme ; il vaut GO de cette course (processeur seul, 0 USD : aucun devis ni identifiant `GO-…`, réservés aux dépenses).
```

Dans la ligne 191, remplacer « (CL-10 ; brouillon 1 : plus de 10 sur V seul) » par :

```text
(CL-10 ; décision de Lazar R-1086, point 5 ; brouillon 1 : plus de 10 sur V seul)
```

Dans la ligne 195, remplacer « retenue le 1er novembre 2026 par défaut de la session (R-1079 ; travail sur processeur, R-147) ; Lazar peut la remplacer avant le scellement, jamais après. » par :

```text
retenue le 1er novembre 2026 par défaut de la session (R-1079 ; travail sur processeur, R-147), puis par Lazar (R-1086, point 5) ; jamais modifiable après le scellement.
```

Dans la ligne 200, remplacer « Décision : (a) appliquée par défaut le 1er novembre (R-1079). GO de la course : R-1075 (Résumé, point 7). » par :

```text
Décision : (a), appliquée par défaut le 1er novembre (R-1079), retenue par Lazar (R-1086, point 5). GO de la course : R-1075, confirmé par R-1086 (Résumé, point 7).
```

Remplacer la ligne 413 par :

```text
- Lazar : N = 100, seuil « graines neuves » > 2, B par Claude Sonnet 5.5 (R-1086, point 5 ; N d'abord par défaut, R-1079) ; GO de la course : donné le 1er novembre (21:36, heure de Paris), consigné R-1075, confirmé par R-1086 (processeur, 0 USD, ≈ 28 min).
```

### CL2-06 — Plan d'exécution : étapes 0, 2, 3 et 7 (point D) — obligatoire

Constats : (i) étape 0 : `runs/20261101-160323-regles-defense-convergence/` est déjà rapatrié et commité (commit `bec4eb6d`, le même que le brouillon 2), sceaux vérifiés ; (ii) étape 2 : la ligne « Implémentation indépendante B (v2) » n'est pas produite par `identite` ; « aucune différence admise » serait faux ; (iii) étape 3 : faite ; (iv) étape 7 : la commande de B n'est pas figée dans le texte ; celle du rapport de B contient des chemins à compléter (`<RACINE_DEPOT>`, `<run>`), et rien ne dit que la sortie de B est scellée avant d'être lue.

Remplacer la ligne 248 par :

```text
0. **Préparation** (dans `/home/claude/controle-ia-travail`, aucune ref `donnees/*`, aucun `git fetch` sans refspec) : `docs/notes/convergence-defense-v1/`, `diag/20261101-160323-regles-defense-convergence/`, `prereg/preregistrement-regles-defense-convergence-v1.md` (R-1079) et `runs/20261101-160323-regles-defense-convergence/` (commit `bec4eb6d`) sont dans l'arbre avec leurs compagnons ; à revérifier juste avant le scellement : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier runs/20261101-160323-regles-defense-convergence/manifeste.json runs/20261101-160323-regles-defense-convergence/pids-travail.txt diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json diag/20261101-160323-regles-defense-convergence/analyse-regles-defense.json` (attendus `36db58cf…`, `767aa28f…`, `d07ece47…`, `18b80112…` ; conformes le 2 novembre à ≈ 00:25 UTC, contre-lecture 2). Ne déplacer ni renommer, jusqu'à la fin de la course, les chemins que ce texte cite sous `brouillons/` (l'arène v4 de `canal-reprise-releve-v1`, le dossier de la réplication).
```

À la fin de l'étape 2 (ligne 251), remplacer « comparé ligne à ligne au bloc de ce texte (aucune différence admise). » par :

```text
comparé ligne à ligne au bloc de ce texte, hors la ligne « Implémentation indépendante B (v2) », écrite à la main (aucune autre différence admise ; identique le 2 novembre à ≈ 00:20 UTC, contre-lecture 2).
```

Remplacer la ligne 252 par :

```text
3. **Implémentation B v2** — fait : spécification v2 (`977dd909…`, finale) copiée octet pour octet dans `implementation-b/entrees/` (empreinte vérifiée) ; B v2 écrite, essayée (560 essais passés), validée (§ Plan 4), avec la liste des fichiers ouverts ; ses fichiers et leurs compagnons commités en `6151e59702fa887bad0c741f1d33a4a435709869` (C_B) ; ligne « Implémentation indépendante B (v2) » du bloc d'identité remplie.
```

Remplacer la ligne 258 par :

```text
7. **Implémentation B v2** sur la course (secondes), après la fusion des sorties de la course dans la branche de travail (étape 6), depuis `/home/claude/controle-ia-travail`, `<run-id>` étant l'identifiant du manifeste (commande du rapport de validation de B v2, `a29437b0…`, § « Commande exacte », chemins complétés, sans `--plomberie-fausse`) :
   `/home/claude/controle-ia-travail/.venv/bin/python /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/implementation_b_v2.py replication --resultats /home/claude/controle-ia-travail/diag/<run-id>/resultats-regles-defense.json --manifeste /home/claude/controle-ia-travail/runs/<run-id>/manifeste.json --prereg /home/claude/controle-ia-travail/prereg/preregistrement-replication-regles-defense-convergence-v1.md --analyse-A /home/claude/controle-ia-travail/diag/<run-id>/analyse-regles-defense.json --analyse-originale /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/analyse-regles-defense.json --resultats-originaux /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/resultats-regles-defense.json --sortie /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/sortie-b-replication-v2.json`
   Code de sortie consigné ; la sortie est scellée (`controle_ia.scellement sceller`) et commitée par la session avant que le lecteur l'ouvre ; code 0 → sortie lisible ; code 2 ou 3 → arrêt (§ Liste d'arrêt), la session ne lit que le code, `lecture_autorisee` et les motifs.
```

### CL2-07 — Passages que le validateur ne voit pas (point I) — obligatoire, au scellement

1. Ligne 1, remplacer par :

```text
# Préenregistrement — réplication sur graine neuve de la course de convergence des règles de défense (mélange d'équilibre, défense figée, historique) — v1
```

2. Ligne 3 (statut), remplacer au scellement par :

```text
**Statut** : texte scellé (date à la ligne « Date ») ; issu du brouillon 3, lui-même issu des brouillons 1 (`f0fd07874c6bba5dfb71c845a693749015caaee2b554ae5772c93b2a82dd7c76`) et 2 (`74c66bd38e5288c65128ffddcd08d5ba7442cde9797c8fb7b58308b01ae32a0d`), archivés sans modification ; corrections CL-01 à CL-14 (contre-lecture 1) et CL2-01 à CL2-13 (contre-lecture 2) traitées une à une (§ Contre-lecture) ; ni la spécification v2, ni le code v3, ni ses essais, ni l'implémentation B v2 n'ont changé après la contre-lecture 2 ; aucune racine de réplication dérivée avant le scellement, aucune exécution du jeu sur une telle racine.
```

3. Ligne 9 : dans le brouillon 3, remplacer « texte scellé le AAAA-MM-JJ à HH:MM UTC » par « texte scellé le À REMPLIR (date et heure UTC relevées par `date -u` au scellement) », pour que le validateur refuse le texte tant que la date manque ; au scellement, écrire la date relevée.

4. Ligne 19 : remplacer « (version soumise à la contre-lecture 2 ; à revérifier au scellement) » par « (version finale, inchangée après la contre-lecture 2 ; revérifiée au scellement) ».

5. Ligne 172 : remplacer « Ce brouillon garde le seuil » par « Ce texte garde le seuil ».

6. Ligne 249 : remplacer « (déjà joués pour ce brouillon : journal cité ; » par « (joués avant le scellement : journal cité ; ».

7. Ligne 268 (Plan 8), remplacer « 9. Ce brouillon 2 : » par « 9. Brouillon 2 : », et ajouter avant « Aucune racine de réplication dérivée » :

```text
10. Implémentation B v2 (Claude Sonnet 5.5), d'après la spécification v2 seule : 560 essais passés, 150 mutations sur 150 détectées, écart 0 sur 32 contrastes ; commit `6151e597`. 11. Contre-lecture 2 (sous-agent neuf, Claude Opus 5.5) : scellable après corrections mineures (CL2-01 à CL2-13), sans changement de la spécification, du code v3, des essais ni de B. 12. Brouillon 3 : corrections de la contre-lecture 2.
```

8. Ligne 410, remplacer la phrase « Contre-lecture 2 : un autre sous-agent neuf ; fichiers à lui donner : … que la symétrie des déclencheurs est réelle. » par :

```text
Contre-lecture 2 : sous-agent neuf (Claude Opus 5.5), qui n'a écrit ni ce texte, ni la spécification, ni le code v3, ni B ; rapport `brouillons/preuves-mentors-v1/convergence-replication-v1/contre-lecture-2-preenregistrement-replication-v1.md` (§ Contre-lecture).
```

### CL2-08 — Ce que la réplication peut encore apprendre ; lectures préalables (point E) — recommandée

Ajouter une puce après la ligne 139 (« Rien au-delà de la robustesse à la graine ») :

```text
- **Ce que la réplication peut encore apprendre (lectures préalables déclarées)** : personne dans la chaîne n'est aveugle à la course originale — auteurs des brouillons et de la spécification, auteur du code v3 (qui en a rejoué trois tâches), implémentation B (validée sur ses résultats et son analyse), contre-lecteurs, lecteur et auditeur ; la protection repose sur le gel (texte, code, B et règle des racines fixés avant la course), non sur l'aveuglement. Pour HR1, la course originale exclut déjà presque toute graine favorable (estimations à 18 et 29 erreurs-types de zéro ; probabilité de réplication calculée ≈ 1) : une réussite apporte surtout une preuve de procédure (graine non choisie, statistique recodée, chemin de code rejoué) et la détection d'une erreur propre à la graine 20266201 ; c'est un échec qui serait informatif. Pour HR0, l'issue est réellement incertaine (≈ 0,90 ; ≈ 0,82 avec l'incertitude de l'original) : c'est là que la réplication apprend le plus.
```

### CL2-09 — Indépendance de B : « autre modèle, même fournisseur » (point F) — recommandée

Ajouter une puce après la ligne 142 (« Même simulateur, jeu non recodé ») :

```text
- **Indépendance de B** : B est un autre modèle (Claude Sonnet 5.5) que l'auteur de la spécification et du code v3 (Claude Opus 5.5), du même fournisseur ; elle n'a lu que la spécification, écrite d'après le code v2. La concordance A/B montre que le code et la spécification disent la même chose et que la statistique est recalculable sans le code ; elle ne montre pas que la statistique est la bonne. Dans les textes pour les mentors, écrire « un autre modèle », plutôt que « une autre famille ».
```

### CL2-10 — Parade contre le choix de la graine : deux précisions (point C) — recommandée

Dans la ligne 238, après « Cette interdiction est une règle de procédure, non un verrou technique ; », insérer :

```text
est interdit au même titre le fait de sceller hors du dépôt (dossier temporaire) une variante de ce texte ou d'un de ses brouillons pour en dériver des racines : les seuls textes temporaires scellés permis sont ceux des essais E4, E9 et E10, synthétiques et sans lien avec ce texte ; jouer k tâches sur une racine candidate renseigne déjà sur k/100 de la moyenne d'un budget, donc le coût d'une sélection est proportionnel à l'information cherchée, non « 28 min par graine » ; la trace de V0 (k) ne voit que les versions scellées dans le dépôt ;
```

### CL2-11 — Rejeu de deux tâches pour toutes les issues (point H) — recommandée

Constat : le point (4) de l'audit (rejouer deux tâches de la réplication et vérifier l'égalité au bit) n'est fait que si un déclencheur part, c'est-à-dire pour une issue défavorable ou trop belle ; une réussite « ordinaire » n'est jamais rejouée. Coût : ≈ 30 s de processeur. Dans la ligne 274, après la clause (k), ajouter :

```text
; (l) quelle que soit l'issue, deux tâches de la réplication (δ 1,4 ; instances 0 et 1) rejouées par le lecteur dans un processus neuf (code v3, texte scellé, racines du manifeste), égales au bit au fichier de résultats (point (4) de l'audit appliqué à toutes les issues : ce contrôle ne dépend pas du sens du résultat)
```

### CL2-12 — Phrase pour un « non jugeable » lu mais non tranché (point A) — recommandée

Constat : la ligne 8 de l'issue globale (« non jugeable ») couvre aussi les cas où la réplication est lue mais où le mélange n'est pas tranché (HRép1 « imprécis », ou T3 seul) ; la phrase de la ligne 362 (« n'a pas pu être lue ») y serait fausse. Ajouter après la ligne 362 :

```text
- **Non jugeable, mélange non tranché** (issue ligne 8 ; HRép1 « non jugeable (imprécis) », ou « (santé) » par T3 seul) : « La réplication est lue, mais l'avantage du mélange n'y est pas tranché (motif : … ; est … et … ; B2 [ … ] et [ … ]) : le constat « le mélange bat l'historique » reste celui d'une seule course. »
```

Et remplacer la ligne 373 par « 8. non jugeable : aucune phrase de réplication ; la phrase d'issue dit seulement ce qui n'est pas tranché. »

### CL2-13 — Rattacher la validation de B à l'empreinte de son code (point G) — recommandée

Constat : `validation-b-v2.md` et `.json` ne citent pas l'empreinte de `implementation_b_v2.py` validé (le code a été commité deux fois : `9b83fe4f…` en `e142421f`, instantané en cours, puis `1e32e3b6…` en `1ad1317b`, avant la validation). Je l'ai rattachée par rejeu (§ 5.4). À la fin de la ligne 244, ajouter :

```text
Le rapport de validation ne cite pas l'empreinte du code validé : la contre-lecture 2 a rejoué `implementation_b_v2.py` (`1e32e3b6…`) en mode essai sur la course originale (sortie identique, hors `meta_non_deterministe`, à `sortie-b-originale-v2.json`, `11582b6d…` ; code 3 attendu) et `test_implementation_b_v2.py` (`fdffedce…`) : 560 essais passés.
```

## 4. Marqueurs « À REMPLIR » : contenu exact

Cinq occurrences (`grep -n 'À REMPLIR'`) ; empreintes vérifiées par `sha256sum` sur disque et par `git show 6151e597:<chemin> | sha256sum`.

**Ligne 10** — remplacer la ligne par :

```text
- Commit du code d'analyse : `6151e59702fa887bad0c741f1d33a4a435709869` (2 novembre 2026, 00:14:52 UTC, branche `canal/conv-audit-n04`) — contient, aux empreintes de ce texte, `code/arene_regles_defense_v3.py`, ses deux fichiers d'essais, le journal des essais, la spécification v2 (et sa copie d'entrée de B) et l'implémentation B v2 avec ses compagnons (vérifié par `git show 6151e597:<chemin> | sha256sum`, contre-lecture 2) ; ancêtre du commit de scellement (`git merge-base --is-ancestor 6151e597 <commit de scellement>` rend 0, à vérifier au scellement).
```

**Ligne 41** — remplacer la ligne par :

```text
- Implémentation indépendante B (v2) : code `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/implementation_b_v2.py` — 1e32e3b6d63791b434c894cb597ed381e7920451ba2ffc79576f8c1d1231e445 ; essais `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/test_implementation_b_v2.py` — fdffedce3ea96d13bd02c98d3df40b2ed562be6e93117846fbf22c42f43c5c56 ; rapport de validation `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/validation-b-v2.md` — a29437b0b1741ea08407d2ae85415169ce508d580dd0476ade3073e1077518e2 et `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/validation-b-v2.json` — bbe0118557749c4fa852261a5179de54c548cbc938b7d171fa72155e2aea36be (compagnons `.sha256` présents et conformes ; commités en 6151e597, avant la création du manifeste de la course ; § Plan 4)
```

**Ligne 242** — la phrase « Famille du modèle de B : À REMPLIR (déclarée par la session qui lance B ; R-1079 prévoit « une autre famille » que celle de l'auteur de la spécification). » est remplacée par la fin du texte de CL2-01 ; si CL2-01 n'était pas appliquée, la remplacer seule par :

```text
Famille du modèle de B : Claude Sonnet 5.5 (identifiant `claude-sonnet-5-5`, déclaré dans `validation-b-v2.md`, `a29437b0…`, l. 5 et 271) — autre modèle que l'auteur de la spécification et du code v3 (Claude Opus 5.5), même fournisseur (Anthropic) ; retenu par Lazar comme « autre famille » (R-1086, point 5).
```

**Ligne 409** — remplacer « agent neuf d'une autre famille (À REMPLIR : famille déclarée), » par :

```text
agent neuf Claude Sonnet 5.5 (`claude-sonnet-5-5`), autre modèle que les auteurs de la spécification et du code v3 (Claude Opus 5.5), même fournisseur ; « autre famille » au sens de R-1086, point 5 (la famille de B v1 n'est pas déclarée dans son rapport),
```

**Ligne 433** — remplacer la ligne par l'entrée ci-dessous (à ajuster pour toute remarque refusée ; l'empreinte du présent rapport ne peut y être écrite par lui-même : elle est donnée dans le message de rendu du contre-lecteur, et le marqueur bloque le scellement tant qu'elle manque) :

```text
**Contre-lecture 2** — sous-agent neuf (Claude Opus 5.5 ; identifiant non fourni par l'environnement ; n'a écrit ni ce texte, ni la spécification, ni le code v3, ni B), 2 novembre 2026 ; brouillon relu : `brouillons/preuves-mentors-v1/convergence-replication-v1/preenregistrement-replication-convergence-v1-brouillon2.md`, empreinte `74c66bd38e5288c65128ffddcd08d5ba7442cde9797c8fb7b58308b01ae32a0d` ; rapport : `brouillons/preuves-mentors-v1/convergence-replication-v1/contre-lecture-2-preenregistrement-replication-v1.md`, empreinte À REMPLIR (somme donnée par le contre-lecteur dans son message de rendu) ; verdict : scellable après corrections mineures ; traitement (brouillon 3) :
- CL2-01 (fichiers que B peut ouvrir, V0 (h)) : accepté.
- CL2-02 (graines non neuves, réplication identique à l'original : audit, aucune reprise sur ce texte) : accepté.
- CL2-03 (issue « discordance A/B ou arrêt de B » et sa suite) : accepté.
- CL2-04 (compagnons `.sha256`, consigne et état des lieux cités par empreinte) : accepté.
- CL2-05 (décisions de Lazar R-1086, point 5) : accepté.
- CL2-06 (étapes 0, 2, 3, 7 ; commande de B figée) : accepté.
- CL2-07 (titre, statut, date, mentions « ce brouillon », Plan 8, rôles) : accepté.
- CL2-08 (ce que la réplication peut encore apprendre) : accepté.
- CL2-09 (indépendance de B : autre modèle, même fournisseur) : accepté.
- CL2-10 (parade contre le choix de la graine : deux précisions) : accepté.
- CL2-11 (rejeu de deux tâches pour toutes les issues, V0 (l)) : accepté.
- CL2-12 (phrase pour un « non jugeable » lu) : accepté.
- CL2-13 (empreinte du code de B rattachée par rejeu) : accepté.
```

## 5. Ce que j'ai vérifié moi-même

### 5.1 Provenance (point G) : 28 sur 28, plus les pièces de B

Les 28 empreintes distinctes de 64 chiffres du brouillon 2 ont été extraites par motif et comparées aux sommes `sha256sum` des fichiers (sceaux des pièces originales vérifiés aussi par `controle_ia.scellement verifier`, tous « OK ») :

| Pièce | Empreinte (12 premiers chiffres) | Contrôle |
|---|---|---|
| préenregistrement original `prereg/preregistrement-regles-defense-convergence-v1.md` | `d82dea338868` | fichier et sceau |
| code v2, essais v2, gel v2 (`docs/notes/convergence-defense-v1/regles-defense-v1/`) | `9f0dcf5e0d10`, `78d979ab76bb`, `9977d7df7f87` | fichiers ; sceaux du code et du gel |
| arène v4 (copie suivie) | `70c77fd5c0ec` | fichier et sceau |
| résultats, analyse, manifeste, PID de la course originale | `d07ece476cc1`, `18b801123040`, `36db58cfac9b`, `767aa28fb8ce` | fichiers et sceaux |
| lecture, audit « trop beau » (`docs/notes/…/regles-defense-v1/`) | `24081eed65ce`, `7e81d094868e` | fichiers |
| gabarit ; source du pilote `reponse-argon-convergence-v2-v1.md` | `8cad43714b56`, `fa49440fb82f` | fichiers |
| bibliothèque `gardes`, `prereg`, `scellement`, `manifeste` | `a83c48ceba48`, `3b2e3ee56463`, `93beeb1c8aae`, `1a5c7464523e` | fichiers ; bloc d'identité régénéré |
| configuration canonique | `3fbb27fc0824` | `config.config_sha256` du manifeste original ; bloc régénéré |
| spécification v2 (et sa copie d'entrée de B) ; spécification v1 (et copie) | `977dd9092cbd`, `2a1ad6d356ab` | fichiers |
| code v3 ; essais ; essais complémentaires ; journal | `3519123b7297`, `d1afa9db925a`, `cad209394bf7`, `a506cd447038` | fichiers ; en-tête du journal ; commit `6151e597` |
| script de puissance ; sortie | `1af564c33197`, `4ac975e3608b` | fichiers ; commit `6151e597` |
| brouillon 1 ; contre-lecture 1 | `f0fd07874c6b`, `2a1cf1af4b5e` | fichiers |
| B v2 : code, essais, rapport `.md`, rapport `.json` (empreintes de la mission) | `1e32e3b6d637`, `fdffedce3ea9`, `a29437b0b174`, `bbe011855774` | fichiers, compagnons (`sha256sum -c` : OK), commit `6151e597` |
| B v2 : sortie de validation | `11582b6db4aa` | fichier, compagnon |

Historique : code v3 ajouté en `7d9825dd` ; essais complémentaires, journal, spécification v2, brouillon 2, script de puissance, consigne et `runs/` original en `bec4eb6d` ; `implementation_b_v2.py` commité en `e142421f` (version intermédiaire `9b83fe4f…`) puis en `1ad1317b` (`1e32e3b6…`, inchangé depuis) ; essais de B en `c67d7a6f` ; rapports et compagnons de B en `6151e597` (HEAD de `canal/conv-audit-n04`). Arbre du dossier de la réplication : propre (`git status`).

### 5.2 Diff v2 → v3 (point D)

`diff -u` de `arene_regles_defense_v2.py` (846 lignes) et `arene_regles_defense_v3.py` (1 008 lignes) : 18 blocs, tous dans la liste fermée : en-tête (C1) ; `VERSION`, `IDENTIFIANT_PREREG` (C2) ; `ARENE_V4`, `DOSSIER_V2`, `GEL` (C3) ; `CODE_V2`, `CODE_V2_SHA256` (C6, C11) ; constantes et fonctions de la règle D (C4) ; `_AUTORISATION_DECISION` et `exiger_racine_permise_regles` (C4, C5) ; `bloc_identite` (C11) ; `exiger_identite_prereg_regles` (C6) ; `autoriser_decision_regles` (C7 : revérification de l'empreinte et refus d'un second texte) ; `finale_regle`, `serialiser_moniteur`, `serialiser_variante`, `executer_tache_regles` (C10 : options de sortie, valeurs inchangées) ; `_travail` (C8) ; `main` (C9 : `exiger_gel_regles(())`, racines dérivées, quatre clés de manifeste ajoutées, `analyser_regles(res, ρ)`) ; `__all__` (C12). Rien dans les règles, l'oracle, l'attaquant, les lois tenues, la finale, `analyser_regles`, `_boot`, `MESURES_CONTRASTE`, les gardes. L'inventaire de E5 étendu dans le journal (95 nœuds en v2, 108 en v3 ; 80 identiques ; 15 modifiés ; 8 affectations et 5 fonctions ajoutées ; 28 entrées imprimées) concorde avec mon décompte. Un seul affaiblissement de garde, déclaré (C9) : le gel n'est plus tenu de citer les racines (il ne peut citer des racines dérivées d'un texte postérieur). E6 (dans le journal) : trois tâches originales rejouées sur le chemin de production, égales au fichier original, repli non employé.

### 5.3 Essais rejoués (sous `nice -n 10`, machine à 2 cœurs, charge 0,31 au départ)

- `implementation-b/test_implementation_b_v2.py` : **560 passés** en 98,7 s (2 novembre, 00:19:22 → 00:21:01 UTC).
- `code/test_arene_regles_defense_v3.py` et `…_complements.py`, sans `REGLES_ESSAIS_LENTS` : **38 passés, 5 lents sautés** (E6 et la parité de T), 33,5 s (00:21:01 → 00:21:35 UTC). Les 43 noms d'essais (34 + 9), E1 à E10 compris, sont présents. Aucun fichier écrit sous `diag/` ni `runs/` du dépôt.
- Validateur `controle_ia.prereg.problemes` sur le brouillon 2 : « section vide ou à remplir : Plan d'analyse » et « … : Contre-lecture » (attendu).
- Bloc d'identité : `arene_regles_defense_v3.py identite` (aucun calcul de jeu) rend, au caractère près, les lignes 29 à 118 du brouillon, hors la ligne B v2.

### 5.4 Implémentation B v2 rejouée sur la course originale

`implementation_b_v2.py essai` avec E1 = E4 = résultats originaux, E5 = analyse originale, sortie neuve dans le dossier temporaire : code 3 (« graines non neuves » : les 15 comptes à 200), 0,9 s. Sortie comparée clé à clé à `sortie-b-originale-v2.json` (`11582b6d…`) : **0 différence hors `meta_non_deterministe`**. Le code `1e32e3b6…` est donc bien celui qui a produit la sortie de validation.

Lecture de E2 par B (lignes 1401 à 1431 de B) : `run_id`, `config.racine`, `config.racine_tenue`, `config.racine_chaine`, `config.racine_tenue_chaine` (facultatives), `preenregistrement.sha256`, `config.prereg_sha256`, `config.lambda`, `config.reference`, `config.config.n_instances`, `config.config_sha256` — toutes présentes dans la structure du manifeste original (même `creer_manifeste`), le code v3 y ajoutant `racine_chaine`, `racine_tenue_chaine`, `regle_racines`, `code_v2_sha256`. E1 et E5 : `run_id`, `manifeste_sha256`, `resultat` écrits par `ecrire_resultat`. Compagnons de la course : exactement « 64 chiffres, deux espaces, nom de base, fin de ligne » (quatre fichiers originaux contrôlés), format exigé par B.

### 5.5 Statistique (point B)

- Puissance : script du § Annexe, graine `SeedSequence(271828)` sans lien avec la course : effet de HR1 réduit de moitié → « répliquée » 0,654 (script versé : 0,648 ; approximation normale par budget 0,654 et 0,9971, produit 0,652) ; HRép0 au niveau 1 → 0,899 / 0,000 / 0,100 (script versé : 0,903 / 0,000 / 0,096). Écarts compatibles avec l'erreur de Monte-Carlo (≈ 0,003 pour 20 000 tirages).
- Seuil G : coïncidences au bit entre tâches distinctes d'un même budget, par variante et par mesure, dans la course originale : au pire 0,0808 coïncidence attendue sur 200 tâches (V de R0 et de R2), P(plus de 2) = 8,28 × 10⁻⁵ (Poisson) ; X̄ et (ii) : au plus 0,0202. Aucune valeur n'apparaît plus de deux fois par budget : pas d'atome (pas de V = 0 en masse), donc pas de fausse alerte structurelle.
- Constante z* : 2,497705474412374 dans le texte et la spécification ; `statistics.NormalDist` donne 2,4977054744123737 (un dernier chiffre de différence, sans effet : la constante est fixée par son écriture décimale, et la frontière numérique couvre 10⁻⁹).
- Cohérence avec l'original : Tables R1 et R0 au moins aussi strictes que les Tables A et B originales (taille 0,05 contre 0,02 ; « ≈ » ou mieux aux deux budgets au lieu d'un). Spécification v2 et texte d'accord sur les tables, les déclencheurs, le contrôle « graines neuves », les issues et les cinq contrastes de concordance exigée.

## 6. Ce que je n'ai pas vérifié, ou réserves

- **La course** : jamais lancée ; aucune tâche de la réplication calculée ; aucune racine dérivée d'un brouillon (je n'ai appliqué la règle D à aucun texte).
- **Essais lents** du code v3 (E6, trois tâches et deux tâches originales ; parité de T) : non rejoués ; résultat lu dans le journal (`a506cd44…`).
- **Campagne de mutations de B** (150 sur 150) : non rejouée ; son code a été supprimé par B (déclaré).
- **Isolement de B** : déclaratif (CL2-01) ; le dossier temporaire de la session contient des pièces qui lui étaient interdites.
- **B sur une vraie sortie de réplication** : impossible avant la course (B exige N = 100 et la configuration épinglée) ; risque réduit par le contrôle des clés (§ 5.4), suite écrite d'avance par CL2-03.
- Mes scripts de contrôle sont dans le dossier temporaire de la session, hors du dépôt ; les deux qui produisent des chiffres de ce rapport sont reproduits ci-dessous.

## Annexe — scripts du contre-lecteur

Lancés avec `nice -n 10 /home/claude/controle-ia-travail/.venv/bin/python -I <script> /home/claude/controle-ia-travail/diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json` ; ils vérifient l'empreinte du fichier et n'écrivent rien.

```python
# coincidences.py — coïncidences au bit entre tâches distinctes de la course originale (seuil G)
import hashlib, json, math, sys
from collections import Counter
ATT = "d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b"
o = open(sys.argv[1], "rb").read()
assert hashlib.sha256(o).hexdigest() == ATT
T = json.loads(o)["resultat"]["resultats"]
pire = 0.0
for k in T[0]["regles"]:
    for champ in ("V_iii_final", "exploitabilite_moyenne_tours", "ii_final"):
        lam = 0.0
        for c in (1, 2):
            v = [t["regles"][k][champ] for t in T if t["code_delta"] == c]
            n = len(v)
            paires = sum(m * (m - 1) // 2 for m in Counter(v).values())
            lam += n * paires / (n * (n - 1) / 2)
        pire = max(pire, lam)
        print(k, champ, round(lam, 4), 1 - math.exp(-lam) * (1 + lam + lam * lam / 2))
print("pire attendu", round(pire, 4))
```

```python
# puissance_cl2.py — deux lignes de la table de puissance, graine 271828
import hashlib, json, sys
import numpy as np
from statistics import NormalDist
ATT = "d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b"
o = open(sys.argv[1], "rb").read(); assert hashlib.sha256(o).hexdigest() == ATT
T = json.loads(o)["resultat"]["resultats"]
def diff(c, k):
    t = sorted((x for x in T if x["code_delta"] == c), key=lambda x: x["instance"])
    return np.array([x["regles"][k]["V_iii_final"] - x["regles"]["R2"]["V_iii_final"] for x in t])
N = NormalDist(); z2 = N.inv_cdf(0.99375); z8 = N.inv_cdf(0.996875); m, tau, R = 0.02, 0.05, 20000
d3 = {c: diff(c, "R3") for c in (1, 2)}; d0 = {c: diff(c, "R0") for c in (1, 2)}
p = [1 - N.cdf((tau - d3[c].mean() / 2) / (d3[c].std(ddof=1) / 10)) for c in (1, 2)]
print("HR1 moitié, analytique", [round(x, 4) for x in p], round(p[0] * p[1], 4))
rng = np.random.default_rng(np.random.SeedSequence(271828))
I = rng.integers(0, 100, size=(R, 100))
ok = np.ones(R, bool)
for c in (1, 2):
    s = (d3[c] - d3[c].mean() / 2)[I]; est = s.mean(1); se = s.std(1, ddof=1) / 10
    ok &= (est >= tau) & (est - z2 * se > 0)
print("HR1 moitié, rééchantillonnage", round(ok.mean(), 3))
def classe(s):
    est = s.mean(1); se = s.std(1, ddof=1) / 10; cl = np.full(R, 6)
    for k, cond in ((5, est + z8 * se < 0), (4, est - z8 * se > 0), (3, (est - z2 * se > -m) & (est + z2 * se < m)),
                    (2, est + z8 * se < -m), (1, est - z8 * se > m)):
        cl = np.where(cond, k, cl)
    return cl
c1, c2 = classe(d0[1][I]), classe(d0[2][I])
nr = np.isin(c1, (2, 5)) | np.isin(c2, (2, 5)); rep = ~nr & np.isin(c1, (1, 3, 4)) & np.isin(c2, (1, 3, 4))
print("HR0 niveau 1", round(rep.mean(), 3), round(nr.mean(), 3), round(1 - rep.mean() - nr.mean(), 3))
```

Sorties obtenues : `HR1 moitié, analytique [0.654, 0.9971] 0.6521` ; `HR1 moitié, rééchantillonnage 0.654` ; `HR0 niveau 1 0.899 0.0 0.1` ; coïncidences : `pire attendu 0.0808` (R0 et R2 sur V : 0,0808, P(> 2) = 8,28 × 10⁻⁵).
