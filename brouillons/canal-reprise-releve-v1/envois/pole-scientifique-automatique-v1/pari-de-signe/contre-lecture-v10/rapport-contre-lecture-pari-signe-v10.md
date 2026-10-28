# Contre-lecture (R2) — « Le pari apparié borné — conception v10 » et le code v7, version 28 — rapport v1

Contre-lecteur : sous-agent neuf **Opus 5.5**, autre modèle que l'auteur de la v10 et de la version 28 (Fable 5.1) ; je
n'ai écrit ni la conception, ni le code, ni une contre-lecture antérieure. Début : mercredi 28 octobre 2026,
**01:34:30 UTC** (`date -u`, appel séparé). Aucun fichier du dépôt modifié, aucun commit ; modules importés avec `-I -B`
(aucun bytecode écrit) ; rien lu dans `donnees/` ; aucune clé ni aucun jeton lu, affiché ou cherché ; processeur seul,
aucune dépense. Tout ce que j'ai écrit est dans ce dossier.

## Verdict

1. **Conception v10 : « à amender en v11 »** (corrections locales, pas refaire). Les règles qu'elle écrit sont les
   bonnes : fraîcheur par rapport à la course, décision de non-lecture prise avant toute issue de la génération, une
   affirmation par fiche, ordre fixé d'avance, journal confronté par la course. Avec elles, la garantie de D-S25 bis
   tient en raisonnement (Q3). Trois phrases sont fausses ou trompeuses.
   - « L'ordre d'une tranche dérive de l'empreinte de l'**engagement** » : l'engagement contient des entrées libres hors
     de la clé (noms des contrastes, budget α_c et m_c), et le code y ajoute la graine du monde. **Plus d'étiquette libre**
     est donc faux (K10-3).
   - « Le journal est tenu par celui qui calcule » est faux dans le code, où il est facultatif (K10-1, K10-4).
   - Le plan des tranches et l'étiquette `population` sont dans la clé. Une même affirmation peut donc être portée par
     plusieurs fiches (K10-6).

   Le § 6 ne chiffre pas le coût des cinq gardes que la v10 ajoute à G1. Dans la démonstration, ce sont elles qui
   fixent l'e-valeur de la fiche de forme G1 (K10-8, K10-9).
2. **Code v7, version 28 : « à corriger ».** Les chaînes de la contre-lecture v9 sont refusées ou sans effet :
   - la copie renommée : le script v9 s'arrête dès sa première étape ;
   - la tranche lue d'avance : 451 lectures refusées sur 457, fiche jamais promue ;
   - le « sans partie » mensonger journalisé ;
   - la partie d'une autre clé ;
   - la banque grandie à identité déclarée.

   Mais toutes les gardes nouvelles ne lient qu'un orchestrateur qui les appelle. Deux chemins mesurés passent toutes
   les gardes de la version 28 (Lignees, `Course(journal=…)`, clés, plan scellé, `evaluer` qui journalise), sur une
   banque à nul exact :
   - **évaluation privée** (`evaluer` sans journal), puis « sans partie » si l'issue est défavorable : au moins une
     fausse promotion dans **0,055 contre 0,005** en course honnête sur 10 générations, **0,79 contre 0,01** sur 30
     (K10-1) ;
   - **espionne de même génération** (même contraste, autre étiquette `population`, acceptée), puis « fiche non
     lancée » décidée après l'issue de l'espionne : **0,62 contre 0,01** sur 30 générations (K10-2).

   S'y ajoutent :
   - quatre étiquettes d'ordre qui changent l'ordre sans changer la clé : cent noms donnent cent ordres, tous acceptés
     (K10-3) ;
   - un journal modifiable, dont la génération est libre et qui ne garde pas les identifiants (K10-4). La
     démonstration elle-même efface une entrée du journal (l. 201) ;
   - une partie vide ou refusée qui n'a aucune sortie honnête (K10-5) ;
   - des gardes facultatives sans avertissement (K10-7).
3. **La démonstration se relit** : `banque.json` (`a08426e0…`) et `course.json` (`7e5f1183…`) sont reproduits à l'octet
   près. L1, le contrôle 12, L2, L3, « 25 fiches, 25 affirmations », le nul × 200 et les cinq artefacts sont tels que
   le LISEZMOI v28 les dit. La formule `esperance_conditionnelle` est juste (écart maximal de 0,00045 contre
   800 000 tirages). **Il reste une lecture trompeuse** : chaque partie de la fiche de forme G1 est limitée par une
   **garde**, alors que la lecture L3 ne rapporte que les richesses des contrastes, sur la dernière partie seulement,
   et `log_garde_finale: null` (K10-8). Les incréments de log e sont 2,118, 1,778 et 1,326, soit exactement les
   minima des gardes « blanc−juge », puis « blanc−cascade » deux fois. En cumul, la garde « blanc−cascade » vaut 5,34,
   contre au moins 9,45 pour les contrastes.
4. **D-S8** : la réécriture de la v9 est conforme à N-056, et les conséquences (α), (β) et (γ) sont justes. « Une garde
   par comparateur » n'est pas dans N-056. Elle rend G1 plus stricte, et la v10 a raison de la soumettre à Lazar (« à
   confirmer d'un mot »).

---

## 1. K9-1 à K9-10, K8-1, K8-2, K8-4, K8-5, K7-6, K7-7

| constat | état (texte v10 / code v28) | où, pourquoi | vérifié par |
|---|---|---|---|
| **K9-1** fraîcheur par rapport à la course | **à moitié** | Texte : écrit (verdict 1, § 1 D-S25 bis (5)), y compris « décision de non-lecture prise avant toute issue de la génération, d'aucune fiche ». Code : `premiere_lecture` ferme la tranche d'avance (chaîne v9 rejouée : 451 lectures refusées sur 457, fiche jamais promue). **Mais la décision prévisible n'est pas tenue par le code** : une déclaration « sans partie » ou un abandon « avant partie » pris après les issues des autres fiches passe (H2 : 0,62 ; A8). `premiere_lecture` n'est rempli qu'à l'ajout : les unités d'une partie calculée puis non ajoutée restent « fraîches ». | G, H2, A8 |
| **K9-2** lien fiche ↔ clé | **à moitié** | Fermé quand on s'en sert : `Lignees` refuse une seconde clé pour une fiche (A2), la `Course` refuse la partie d'une autre clé (A2, artefact 5), et une banque grandie à identité déclarée garde ses 40 identifiants (refus, A4). Ouvert : `cles` est facultatif (sans lui, une fiche reçoit une partie d'une autre clé, A2) ; l'identité est une étiquette libre de la banque (ré-étiquetée, 0 identifiant commun, et une fiche neuve est acceptée sur les mêmes 40 unités physiques) ; sans `identite`, le repli sur l'empreinte redonne 0 identifiant commun, en silence (A4). | A2, A4 |
| **K9-3** noms libres, rembourrage | **à moitié** | La forme canonique ferme le renommage : copie renommée refusée par `Lignees` et par `Course.entrer` (A3), et le script v9 de la chaîne s'arrête dès l'étape 1. Les deux contrastes de même forme sont refusés, et la démonstration refuse les redites (25 fiches, 0 affirmation en double, A3b). Le texte dit le taux par fiche et la sortie par e-Bonferroni. **Reste un nom libre dans la clé : `population`**, et le plan est dans la clé. Même contraste avec une autre étiquette, un autre découpage ou un décalage du plan : clé différente, seconde fiche acceptée (A3). | A3, A3b |
| **K9-4** version de l'e-processus | **fermé** | `E_PROCESSUS` (version 28) est dans la clé ; essai « version changée ⇒ clé changée » ; la v10 dit « version 28 » partout. Résidu mineur : la version est déclarée à la main (K10-10 h). | A1 ; `test_cle_de_l_heritage` |
| **K9-5** tranche et étiquette libres | **à moitié** | Plan scellé, refus des unités libres avec un plan (A7), `etiquette_ordre` supprimée (A7), une évaluation journalisée par fiche et par génération (A5b). **Mais l'ordre dépend toujours d'entrées hors de la clé** : nom du contraste, α_c et m_c, graine du monde, une unité factice ajoutée à la banque. Chacune donne même clé, mêmes unités, autre trajectoire, acceptée par `Lignees` et par la `Course` (L ; cent noms donnent cent ordres). Sans plan, les `unites` restent libres (A7). | L, A7, H3 |
| **K9-6** journal tenu par qui il contrôle | **à moitié** | `evaluer(…, fiche, journal)` journalise et la `Course` confronte (artefact 3). Mais : `evaluer` sans journal est permis (A5a), puis « sans partie » est accepté (H1 : 0,79) ; le journal est une liste qu'on réécrit (A5d, et la démonstration l. 201) ; sa génération est celle que l'appelant passe (A5c : la tranche 2 est journalisée pendant la génération 1, puis ajoutée ; la chaîne `"1"` passe une seconde évaluation, L) ; `Course` sans journal ne contrôle rien, en silence (A9). | A5, A9, L, H1 |
| **K9-7** « signe connu » faux conditionnellement | **fermé** | L1 porte sur l'espérance conditionnelle aux seuils scellés ; la formule est vérifiée (C : écart maximal 0,00045) ; le jumeau est lu comme contrôle 12 (+0,035, non promu) ; le docstring est restreint aux paires ±1. | C ; démonstration reproduite |
| **K9-8** « G1 promue » n'est pas G1 | **à moitié** | Fiche nommée « forme-G1 », e-Bonferroni rapporté (non : 5,22 < 6,87), « comparateur le plus faible » retiré. Mais les « richesses descriptives » sont celles de la **dernière partie** des seuls contrastes, alors que K9-8 demandait le processus cumulé de chaque composante, et les gardes, qui fixent la valeur, n'y sont pas (K10-8). | F |
| **K9-9** indépendance de la table, garde unique | **fermé au texte ; conséquence non chiffrée** | § 6 : (discordance − écart²)/m, devis en (écart, discordance, C), contrôle 12 à la taille de G1 ; cinq gardes codées (`garde=[…]`). Le coût de ces gardes n'est pas au devis (K10-9). | lecture ; F |
| **K9-10** mineurs | **(a), (c), (d), (e), (f) fermés ; (b) à moitié** | (a) composantes descriptives, dit ; (b) la démonstration abandonne le témoin inversé avant toute évaluation (l. 192-195), mais le code accepte un « avant partie » contredit par le journal (A8) ; (c) refus pour gelée ou fiche qui a sa partie (A6) ; (d) `≤` au lieu de `+ 8`, invariant réel ; (e) décalages de loi, avec une précision (K10-10 a) ; (f) dit au § 1. | A6, A8 ; lecture des essais |
| **K8-1** fraîcheur | **presque fermé** | Par fiche et par course, avec identité stable. Restes : identité ré-étiquetée ou absente (A4) ; unités d'une partie calculée et non ajoutée non enregistrées (K10-4). | A4, G |
| **K8-2** « sans partie » mensonger | **à moitié** | Refusé pour une partie journalisée (artefact 3, A5) ; accepté pour une partie calculée hors journal (A5a, H1), ou dont l'entrée a été effacée (A5d). | A5, H1 |
| **K8-4** combinaison sur Λ et arrêt hors clé | **fermé** | `e_processus` et `lambdas` sont dans la clé. | A1 |
| **K8-5** essais | **à moitié** | Ajoutés : seconde clé, renommage, plan, version de l'e-processus, une fiche une clé, journal. **Toujours pas d'essai « Λ changé ⇒ clé changée »** (aucune occurrence de `LAMBDAS` dans les trois fichiers d'essais). 41 essais ciblés passent (2,2 s). | lecture ; `essais-cibles-console.txt` |
| **K7-6** alignement par rang | **ouvert, déclaré** | Inchangé ; exact dans la démonstration. | lecture |
| **K7-7** ordre sans les scores d'épreuve | **ouvert, déclaré** | Le plan scellé fixe quelles unités sont lues, pas l'ordre : `ordre_secret` utilise toujours l'empreinte de toute la banque (scores d'épreuve compris), et K10-3 ajoute quatre canaux. | lecture ; L |

## 2. Réponses aux questions du brief

### Q2 — D-S8 réécrite (nœud 1 = b), (α), (β), (γ), § 6

- **Conforme à N-056** (`6aac9746…`, « Ce que cela fixe », point 1). G1 doit battre chaque moniteur boîte noire de la
  liste scellée, ainsi que (ii), la cascade de portes, et (iii), la sonde sur le dernier état. Les planchers sont
  rapportés, et H2 garde ses tests (H2c). La v10 ne change rien à cela.
- **Ajout de la v10, « une garde par comparateur »** : il n'est pas dans N-056. C'est un choix de conception qui ajoute
  cinq nuls à l'intersection-union, donc une porte plus stricte. Le soumettre à Lazar (« à confirmer d'un mot ») est
  juste. Il lui faut cependant son coût, qui n'est pas chiffré (K10-9).
- **(α) juste** : « un échec ne dira pas laquelle a échoué ». Les composantes sont déclarées descriptives, et la course
  ne garde que le minimum. Mais la lecture rapportée omet justement les composantes qui lient, les gardes (K10-8).
- **(β) juste** : les chiffres sont inchangés depuis la v9 et vérifiés par la contre-lecture v9 contre
  `simulation-dimensionnement-v2-sortie.json` (`d07e43f9…`, empreinte revérifiée ici). Le modèle à alertes
  indépendantes est maintenant dit au § 6.
- **(γ) juste** : les comparateurs diffèrent, donc les clés aussi.
- **Le § 6 renvoie à des chiffres qui existent** : la table du pari v2 § 6, et « ≈ 4 points », qui vaut 4,1 dans la
  contre-lecture v9, section C.

### Q3 — Garantie sous la règle de l'héritage avec des tranches

**Notations.**
- Les fiches i ont un budget b_i fixé à l'entrée (prévisible), avec Σ b_i ≤ Σ α_c ≤ α, ce que tient `Course.entrer`.
- E_i(g) est le produit des parties de i, gelé à la promotion, à l'arrêt ou à l'abandon.
- R_g est l'ensemble e-BH de la lecture g ; U = ∪_g R_g ; γ_i est la première lecture qui promeut i.
- F_g est l'information de **toute la course** à la fin de la génération g.

**Ce que la preuve exige.** Il faut deux conditions :
- **(H)** chaque partie e_{i,g} est une e-valeur conditionnellement à F_{g−1} sous le nul de i ;
- **(P)** toute décision de ne pas lire, ou de geler avant partie, à la génération g est F_{g−1}-mesurable, ou prise
  avec une information indépendante des issues de la génération g.

Alors E_i est une surmartingale positive pour F, et le temps de gel τ_i = min(γ_i, arrêt, abandon, G_max) est un temps
d'arrêt pour F, car γ_i se lit sur les valeurs courantes.

- **(i) Les promotions s'accumulent.** Pour i ∈ U, b_i E_i(γ_i) ≥ 1/k*_{γ_i}, et |U| ≥ |R_{γ_i}| ≥ k*_{γ_i}. Donc
  1(i ∈ U)/|U| ≤ b_i E_i(τ_i), puisque la valeur est gelée à γ_i. Il en suit FDP(U) ≤ Σ_{i nulle} b_i E_i(τ_i), et
  par arrêt optionnel (horizon borné, b_i prévisible) le taux de fausses découvertes est au plus Σ_{nulles} E[b_i] ≤ α.
  L'accumulation ne fait que grossir |U|. **Tient.** La garantie porte sur le taux de fausses découvertes de l'union,
  pas sur la probabilité d'au moins une fausse : sous le nul complet, les deux coïncident (nul × 200).
- **(ii) Arrêt au seuil 1/b_i = m_c/α_c.** C'est un temps d'arrêt unité par unité, à l'intérieur d'une partie. Une fiche
  arrêtée a b_i E_i ≥ 1 ; elle entre dans R à la lecture suivante, quel que soit k*. Le code est conforme
  (`ajouter_trajectoire`, l. 354-361). **Tient.**
- **(iii) Abandon sous contrat.**
  - Le gel « après partie » à g est un temps d'arrêt pour F_g, même décidé après les issues des autres fiches. **Tient.**
  - Le gel « avant partie » à g fige E_i(g − 1). Si la décision a vu une issue de g, d'une fiche quelconque partageant
    la tranche, ce n'est plus un temps d'arrêt. Le gain est borné une fois, par E[max(1, e_g)] ≤ 2 (×1,77 mesuré par
    la contre-lecture v8).
  - **Le code ne le tient pas** : un « avant partie » est accepté alors que la partie de la fiche est au journal (A8).
- **(iv) « Sans partie ».** La fiche garde le facteur 1, ce qui n'est valide que sous (P). Une déclaration **vraie**
  (rien n'a été calculé pour la fiche) mais décidée d'après une issue de la génération, la sienne en privé ou celle
  d'une fiche corrélée, se répète chaque génération. Elle compose, avec E[max(1, e_g)] par génération : **c'est le
  trou**, et il est **mesuré dans le code v28, toutes gardes passées** (K10-1, K10-2).

| chaîne (banque à nul exact, tranches de 20 unités, α = 0,05) | 10 générations (200 courses) | 30 générations (100 courses) |
|---|---|---|
| H1 honnête, fiche seule (seuil 20) | 0,005 [0,001 ; 0,028] | 0,01 [0,002 ; 0,054] |
| H1 évaluation privée puis « sans partie » | **0,055** [0,031 ; 0,096] | **0,79** [0,70 ; 0,86] |
| H2 honnête, famille {espionne, fiche} (seuil 40) | 0,00 | 0,01 |
| H2 espionne de même génération puis « fiche non lancée » | 0,01 | **0,62** [0,52 ; 0,71] |

  (Intervalles de Wilson à 95 %. La banque à nul exact a, au calibrage, des scores identiques pour a et b, donc des
  seuils scellés égaux, vérifié dans 100 % des banques. À l'épreuve, a et b suivent la même loi : le contraste a − b
  est d'espérance nulle **conditionnellement aux seuils scellés**, et de loi symétrique.)
- **Ce qui tient sans réserve** : avec (H) et (P), le raisonnement ci-dessus. La chaîne de K9-1 (copie qui lit d'avance)
  ne peut plus s'exécuter. La démonstration respecte (H) et (P), puisque ses décisions sont écrites en dur, prises
  avant toute évaluation, ou fondées sur les seules clés et strates.

### Q4 — Code contre texte : reste-t-il un degré de liberté choisi après les issues, ni scellé ni journalisé ?

**Oui, sept.** Chacun est mesuré ou montré par une vérification nommée :

| entrée choisie par l'orchestrateur | scellée ? | journalisée ? | effet | vérif. |
|---|---|---|---|---|
| appeler `evaluer` sans `journal` ni `fiche` | non | non | partie calculée invisible ; « sans partie » accepté | A5a, H1 |
| moment des déclarations « sans partie » ou « non lancée », et des abandons « avant partie » | non | trace sans heure relative au journal | décision après les issues de la génération | H2, A8 |
| nom du contraste, α_c et m_c de l'engagement, graine du monde, unité factice dans la banque | hors clé | non | ordre de la tranche, donc instant du franchissement | L, H3 |
| `generation` passée à `evaluer` (entier libre, ou chaîne `"1"`) | non | oui, sous la valeur passée | lecture d'avance journalisée sans refus ; seconde évaluation invisible | A5c, L |
| contenu du journal (`Lignees.journal` est une liste) | non | — | entrée effacée, puis déclaration acceptée | A5d ; démonstration l. 201 |
| `identite` de la banque ; étiquette `population` | non | non | relance sur les mêmes unités physiques ; copie d'affirmation | A4, A3 |
| `unites` sans plan ; plan lui-même | plan : oui, mais choisi par l'appelant | non | tranche choisie (sans plan) ; plan non vérifié « jamais des scores » | A7 ; lecture |

Le reste du point 4 du brief est **conforme** :
- fraîcheur par rapport à la course ;
- clés tenues par la course (quand on les passe) ;
- clé canonique : noms hors clé, formes en double refusées ;
- `e_processus` dans la clé ;
- plan scellé et `evaluer(generation=g)` ;
- `Course(journal=…)` qui confronte ;
- gardes multiples, avec le minimum sur toutes ;
- identité de la banque dans les identifiants ;
- « sans partie » refusée aux fiches indues.

### Q5 — La démonstration v28

- **Reproduite** (`--nul 50`, 19 s) : `banque.json` `a08426e0…` et `course.json` `7e5f1183…` identiques aux publiés. La
  lecture diffère seulement par `nul_repete` (0 sur 50, Wilson [0 ; 0,071]) et par `reglages`.
- **Pas de sélection d'un résultat favorable (R4).** Les essais de l'auteur dans le dossier de session sont
  `demo-pari-essai1` et `-essai2` (version 27, `course.json` `cb7dce95…` et `5c5098ea…`), puis `-essai3` et `-essai4`
  (version 28). Ces deux derniers ont le même `course.json` (`7e5f1183…`) et ne diffèrent que par nul = 20 contre
  nul = 200.
- **Ce que le LISEZMOI v28 affirme se relit dans les sorties** (`lecture-pari-apparie.json` `c91eee02…`) :
  - L1 tenue (aucune promue d'espérance conditionnelle ≤ 0 ; `hasard-g3-4`, à −0,0001, n'est pas promue) ;
  - contrôle 12 : « jumeau non promu » (+0,035) ;
  - témoins aux décalages 1,2 et 1,0 promus en génération 2 et sortis par e-Bonferroni (6,99 et 6,89 ≥ 6,87) ; 0,5
    promu en génération 2, non sorti (5,66) ; 0,8 « concentré » promu en génération 4 (5,01) ; 0,1 non promu (+0,0001) ;
  - forme-G1 promue par e-BH en génération 3, non sortie (5,22 < 6,87 = log(12 · 4/0,05)) ;
  - 25 fiches, 25 affirmations ;
  - nul × 200 : 0, Wilson [0 ; 0,019] ;
  - cinq artefacts refusés, par la bonne garde (messages relus).
- **Formule `esperance_conditionnelle`** : juste pour cette banque. Chez les sabotés, le score suit η + d_c + ε, avec
  η ~ N(0 ; 0,6²) partagé par l'unité et ε ~ N(0 ; 1) ; la loi marginale est N(d_c ; 1,36), donc
  E[r_c(t)] = 1 − Φ((s_c − d_c)/√1,36). Les unités d'épreuve sont indépendantes du calibrage. La strate ne change pas la
  loi, et ce sont bien les seuils stratifiés de l'engagement qui sont passés. Une simulation de 100 000 unités × 8 donne
  un écart maximal de 0,00045 sur les sept cellules (C). Pour la forme G1, la vérité ne regarde que les contrastes, mais
  les gardes sont vraies : E[g] est compris entre −0,0095 et +0,0024, très en dessous de δ = 0,10 (C).
- **« Lectures corrigées » du LISEZMOI v28** : elles disent juste ce que la v27 disait de travers (L1 en population, « G1
  promue », « forces »). Avec une précision : « 0,5 ≈ 14 points » ne vaut qu'au niveau blanc contre cascade, où l'on
  mesure 14,4 points ; il en fait 10,4 entre 1,0 et 0,5, et 6,2 entre 0,5 et 0 (K10-10 a).
- **Lecture trompeuse restante** : L3 (K10-8). Mineures : « 25 affirmations » est vrai par construction (K10-10 b) ; le
  « nul complet » est un nul en population, mais 0 promotion le rend sans effet (K10-10 g).

## 3. Constats, du plus grave au moins grave

### Touche la garantie (chemins mesurés, toutes gardes de la version 28 passées)

**K10-1 — L'évaluation privée reste possible ; la « sans partie » vraie qui la suit reproduit le saut de partie.**
- **Où.** `engagement_apparie.evaluer` l. 136 : `(journal is None) != (fiche is None)` laisse passer les deux à `None`.
  `Course(alpha, journal=None)` par défaut. v10 verdict 4 et § 1 D-S25 bis (2) : « la fonction qui calcule la partie
  journalise ».
- **Problème.** L'orchestrateur calcule la partie de sa fiche sans journal, puis l'ajoute par une évaluation
  journalisée si elle est favorable, ou déclare « sans partie » sinon. Le journal est propre, et la `Course` accepte.
  Mesuré (H1) : **0,055 contre 0,005** sur 10 générations, **0,79 contre 0,01** sur 30. C'est le K8-2 de la v8
  (0,396 / 0,978), sous une autre forme. Tant que l'orchestrateur peut lire les scores d'épreuve dans son processus,
  aucun code ne peut l'empêcher de calculer une partie. Or la v10 ne dit pas que cela reste à sa charge.
- **Correction.**
  - Code : `evaluer` refuse une partie d'épreuve sans `journal` et `fiche`. Mieux, la `Course` tient le monde et calcule
    elle-même (`Course.partie(fiche, generation)`), comme la v8 et la v9 le recommandaient déjà (« le monde remet la
    partie à la course »). Une `Course` d'épreuve sans journal est refusée, ou tracée (K10-7).
  - Texte : écrire la frontière de confiance : « tant que l'orchestrateur peut lire les scores d'épreuve, ne calculer
    aucune partie d'épreuve hors du chemin journalisé est une obligation de l'orchestrateur que le code ne vérifie pas
    (0,79 sur 30 générations sinon). Seul un noyau qui garde les scores d'épreuve la ferme. »

**K10-2 — « Décision de non-lecture prise avant toute issue de la génération, d'aucune fiche » : écrite, non tenue par le code.**
- **Où.** `Course.lire(sans_partie=…)` reçoit les déclarations **à la fin** de la génération, sans les confronter à
  l'ordre du journal. `Course.abandonner(avant_partie=True)` ne regarde pas le journal (l. 376-377).
- **Problème.** Une espionne lit la tranche la première : même contraste, étiquette `population` différente, donc
  acceptée par `Lignees` et la `Course` (A3) ; ou n'importe quelle fiche corrélée. Sa partie est ajoutée honnêtement.
  La fiche visée ne lit que si l'issue de l'espionne est favorable ; sinon elle est déclarée « non lancée »,
  déclaration vraie, qui passe. Mesuré (H2) : **0,62 contre 0,01** sur 30 générations (0,01 contre 0 sur 10). Un
  « avant partie » pris alors que la partie de la fiche est déjà au journal est accepté aussi (A8). Le gain est borné à
  une fois, puisque le gel est définitif.
- **Correction (code).**
  - `Course.declarer_sans_partie(fiche, motif)` et `abandonner(..., avant_partie=True)` sont refusés dès que le journal
    contient une entrée de la génération courante, pour quelque fiche que ce soit.
  - `lire` n'accepte que les déclarations enregistrées avant la première entrée du journal de la génération, sauf la
    partie vide confirmée par le journal (K10-5).
  - Le texte est juste ; ajouter « tenu par la course (ordre du journal) ».

**K10-3 — L'ordre de la tranche dépend d'entrées hors de la clé : « plus d'étiquette libre » est faux.**
- **Où.** `evaluer` l. 138 : l'étiquette est `engagement["empreinte"]|g`, et l'empreinte de l'engagement contient
  `noms`, `alpha_c`, `m_c` et `monde`. `ordre_secret` (l. 140-143) y ajoute `self.graine` et `self.empreinte` du monde.
  La `Course` ne confronte que `empreinte_cle` et `empreinte_unites`. v10 verdict 3 : « l'ordre d'une tranche est dérivé
  de l'empreinte de l'**engagement** et de la génération ».
- **Problème.** Quatre canaux donnent chacun une même clé, les mêmes unités et une autre trajectoire, avec une finale
  égale, acceptée par `Lignees.entrer` pour la même fiche et par la `Course` (L) :
  - nom du contraste ;
  - budget de l'engagement ;
  - graine du monde ;
  - unité factice ajoutée à la banque hors du plan.

  Cent noms donnent cent ordres distincts. Le franchissement dépend de l'ordre. L'ampleur est celle du B1 de la v9 :
  0,03 → 0,535 pour 100 ordres, à v = ±0,5 sur 160 unités. Par l'interface, sur ma banque à nul exact, où la variance
  par unité est faible, j'obtiens 0,005 → 0,015 pour K = 100, non significatif (H3) : l'effet suit la variance par
  unité. L'exploitation demande de calculer les K ordres hors journal (K10-1), ou sous des noms de fiche fantômes, que
  le journal accepte.
- **Correction.**
  - L'ordre dérive de `empreinte_cle`, de g et d'une graine du noyau dont l'empreinte est scellée dans l'engagement et
    vérifiée par `evaluer`.
  - La `Course` lie aussi chaque fiche à **une** empreinte d'engagement.
  - Texte (v11, verdict 3 et D-S25 bis (5)) : « dérivé de l'empreinte de la **clé** et de la génération, et de la
    graine scellée du noyau ».

### Gardes contournables, ou qui bloquent à tort

**K10-4 — Le journal se réécrit, sa génération est libre, il ne garde pas les unités.**
- **Où.** `Lignees.journal` (liste publique) ; `journaliser(generation, …)` avec la génération de l'appelant ;
  l'entrée garde l'empreinte et le nombre d'unités, pas leurs identifiants ; `premiere_lecture` n'est rempli qu'à
  l'ajout. La démonstration, l. 201 : `lignees.journal[:] = [...]` efface l'entrée de la partie vide avant de la
  déclarer.
- **Problème.**
  - Une entrée effacée suivie d'une déclaration passe (A5d).
  - La tranche 2 journalisée pendant la génération 1 est acceptée en génération 2 : on peut lire d'avance et décider
    d'un gel « après partie » en génération 1 (A5c).
  - `generation="1"` (chaîne) passe une seconde évaluation au journal, que la course ne voit pas (L).
  - Les unités d'une partie calculée, puis refusée ou abandonnée, restent fraîches pour la course.
- **Correction.**
  - Journal en ajout seul : entrées chaînées par empreinte, la `Course` notant le compte et la dernière empreinte à
    chaque lecture.
  - Génération du journal égale à celle de la course (le journal appartient à la course, ou la course passe sa
    génération) ; refus d'une génération qui n'est pas un entier.
  - Identifiants des unités au journal, et `premiere_lecture` rempli dès la journalisation.

**K10-5 — Une partie vide ou refusée n'a pas de sortie honnête.**
- **Où.** `Course.ajouter_trajectoire` refuse une liste d'unités vide (l. 337-338) ; `lire` refuse une « sans partie »
  contredite par le journal, même si la partie est vide. Même impasse après un refus de fraîcheur (G : 451 refus).
- **Problème.** Une fiche stratifiée sans unité dans la tranche (A10), ou dont la partie journalisée est refusée par la
  course, ne peut ni être ajoutée ni être déclarée. Les seules issues sont d'effacer le journal, ce que fait la
  démonstration, ou de mentir « avant partie », qui n'est pas contrôlé (A8). Une garde qui bloque à tort pousse à
  contourner les autres.
- **Correction.**
  - La `Course` accepte une partie vide comme facteur 1, confirmée par le journal (0 unité).
  - Une partie refusée par la course y est tracée comme « refusée », facteur 1 : la décision est celle de la course,
    donc prévisible.
  - Mieux : `evaluer` consulte la fraîcheur avant de calculer.
  - L'essai « le journal ne contient que des parties non vides » (`test_course_et_lecture`) consacre aujourd'hui
    l'effacement : il faut le réécrire.

**K10-6 — La clé mêle l'identité de l'affirmation et la façon de la lire ; deux étiquettes libres restent.**
- **Où.** `construire` l. 98-102 : `population or monde.identite` (chaîne libre ; l'essai `test_cle_de_l_heritage` la
  prend pour une variante légitime, `population="vivier-2"`) ; `plan_tranches` est dans la clé ; `identite` est déclarée
  par la banque, avec repli silencieux sur l'empreinte (`monde_banque_scores` l. 75). v10 D-S18 : « population =
  **identité** de la banque » ; verdict 2 : « la clé ne contient plus de nom libre ».
- **Problème.**
  - Même contraste avec une autre étiquette `population`, un autre découpage du plan, ou le plan décalé d'une
    génération : clé différente, seconde fiche acceptée (A3). La copie lit la même tranche dans la même génération, ce
    qui est permis : rembourrage e-BH, deux chances au franchissement, et l'espionne de K10-2.
  - Une banque ré-étiquetée donne 0 identifiant commun, et une fiche neuve est acceptée sur les mêmes 40 unités
    physiques (A4).
  - Le quasi-doublon (coefficient 0,999999) est inhérent à toute clé ; il relève d'e-Bonferroni, ce que la v10 dit.
- **Correction.**
  - Deux empreintes :
    - une **empreinte d'affirmation** (contrastes canoniques, comparateurs, τ, strate, partie, seuils, population =
      `monde.identite` seule, gardes, m_max), que `Lignees` rend unique ;
    - une **empreinte de lecture** (plan, Λ, e-processus, graine du noyau scellée), que la `Course` lie à la fiche.
  - Refuser `population` libre ; refuser, sur le chemin apparié, une banque sans `identite`.
  - Faire dériver l'identité des unités de leur contenu (empreinte des épisodes), ou de la mémoire, qui tient un
    registre identité ↔ empreinte des épisodes.

**K10-7 — Des gardes facultatives, sans avertissement.**
- **Où.** `Course(journal=None)` ; `entrer(cles=None)` ; `ajouter_trajectoire(empreinte_cle=None)` accepté pour une
  fiche sans clé.
- **Problème.** Une course sans journal ni clés reçoit une partie d'une autre clé (A2) et une « sans partie » après
  calcul (A9), sans trace. Ce sont des replis silencieux (R5).
- **Correction.** Journal et clés obligatoires. Sinon, un mode explicite `sans_garde=…`, tracé dans l'état de la course
  et dans la lecture.

### Lecture trompeuse de la démonstration

**K10-8 — Forme-G1 : ce qui fixe l'e-valeur, ce sont les gardes, que la lecture ne rapporte pas.**
- **Où.** `demo_pari_apparie_v7.course`, l. 213-216, journalise `log_garde_finale`, qui vaut `None` dès qu'il y a
  plusieurs gardes, et non `log_gardes_finales`. `lecture` (l. 233-239) rapporte les richesses de la **dernière
  partie** des seuls contrastes.
- **Problème.** Les incréments de log e de la forme G1 sont 2,118, 1,778 et 1,326. Ce sont **exactement** les minima
  des gardes « blanc−juge », puis « blanc−cascade » deux fois, alors que les contrastes de ces parties valent de 2,43 à
  6,78 (F). En cumul sur trois parties, la garde « blanc−cascade » vaut 5,34, contre au moins 9,45 pour les contrastes
  (dernier état 9,45 ; cascade 9,94). « Sortie e-Bonferroni : non » vient donc des gardes à δ = 0,10, et non de la
  difficulté du blanc contre le blanc. Le lecteur de L3 conclut le contraire, et K9-8 demandait le cumul de chaque
  composante.
- **Correction.** Journaliser `log_gardes_finales`. Rapporter le cumul par composante, contrastes **et** gardes. Dire,
  descriptivement, quelle composante a lié chaque partie. LISEZMOI : « dans la démonstration, les gardes fixent la
  valeur de la forme G1 ».

### Dimensionnement

**K10-9 — Le § 6 ne chiffre pas le coût des cinq gardes que la v10 ajoute à G1.**
- **Où.** v10 verdict 8 et § 1 « D-S8 et § 6 ».
- **Problème.** Le processus d'une garde croît comme λ·(δ − E[g]) par unité honnête. Dans la démonstration, il gagne
  1,3 à 3,6 de log par tranche de 40 unités, soit environ 0,03 à 0,09 par unité (F). Atteindre log(m/α), environ 6,9
  pour la forme G1 de la démonstration, demande donc à lui seul de l'ordre de 80 à 210 unités honnêtes par mode, même
  avec des contrastes parfaits. Avec cinq gardes, c'est le minimum de cinq processus qu'il faut porter.
- **Correction.** Le poste de devis de G1 (b) se chiffre en (écart, discordance, C, **δ, unités honnêtes par mode**). Le
  choix de δ se fait au préenregistrement. Ce coût se joint à la question posée à Lazar sur « une garde par
  comparateur ».

### Mineurs

**K10-10.**
- (a) « 0,5 ≈ 14 points de rappel au seuil τ = 0,05 » (v10 verdict 7 c, LISEZMOI v28) : 14,4 points entre 1,5 et 1,0,
  mais 10,4 entre 1,0 et 0,5, et 6,2 entre 0,5 et 0 (C). Écrire « entre blanc et cascade ».
- (b) « 25 fiches, 25 affirmations » : vrai, puisque 0 doublon par (coefficients, strate) (A3b), mais par construction
  (`Lignees` refuse les doublons). Le dire.
- (c) Sans plan, `evaluer(generation=g, unites=…)` accepte une tranche quelconque (A7). Le docstring le dit, la v10
  non. Exiger un plan pour toute partie d'épreuve lue dans une course.
- (d) K8-5 : pas d'essai « Λ changé ⇒ clé changée ».
- (e) « Plan dérivé de la banque, jamais des scores » n'est pas vérifiable par le code, puisque le plan est choisi par
  l'appelant, qui peut lire les scores. Le faire dériver par le noyau (`monde.plan(partie, G, graine scellée)`), ou le
  dire à la charge de l'orchestrateur.
- (f) Démonstration, artefact 5 (l. 299-302) : le commentaire dit « ajoutée à la fiche x », le code ajoute à « y ». Le
  refus vient bien de la clé.
- (g) Les banques du nul × 200 sont nulles en population. Conditionnellement aux seuils, la moitié des contrastes sont
  vrais à ±0,01, ce qui est sans effet ici (0 promotion). Écrire « nul en population ».
- (h) `E_PROCESSUS["version"]` est écrit à la main. Une modification future de `pari_apparie` sans changement de version
  garderait la clé. L'empreinte des fonctions concernées le rendrait automatique.
- (i) `essais/test_v7_pari_apparie.py` est inchangé depuis la v27 (`c367a38e…`). Les essais de `premiere_lecture`, du
  journal et des clés sont dans `test_v7_demo_pari_apparie.py` : les trouver là, ou les déplacer.

## 4. Décisions de la v10 : avis

| décision | avis |
|---|---|
| D-S25 bis (5) (0,85) | la règle est juste et suffit à la preuve (Q3) ; **0,85 tenable pour le texte**, à condition d'ajouter la frontière de confiance (K10-1) ; le code n'en tient que la partie « tranche antérieure » |
| D-S25 bis (2) (0,85) | juste au texte ; « tenu par qui calcule » **faux dans le code** (K10-1, K10-4) |
| D-S18 (0,85, « codée ») | canonique codée ; à séparer en affirmation et lecture, et `population` libre à retirer (K10-6) |
| D-S8 (garde par comparateur) | à confirmer par Lazar, comme la v10 le dit ; joindre le coût (K10-9) |
| nœud 2, D-S29, D-S30 | inchangés, conformes à N-056 (« lue, non confirmée ») |

## 5. Chiffres de la v10 et du LISEZMOI v28 contre leurs fichiers

| où | cité | fichier, valeur | verdict |
|---|---|---|---|
| v10 en-tête | v9 `aab37f63…`, rapport v9 `b73789ca…` | `sha256sum` | justes |
| v10 verdict 1 | 0,087 / 0,626 contre 0,025 / 0,024 | rapport v9, Q3 et K9-1 | justes |
| v10 verdict 2 | 0,01 / 0,10 / 0,735 / 1,0 ; ≤ 0,0022 | rapport v9, K9-3 | justes |
| v10 verdict 3 | 0,03 → 0,535 (100 ordres) | rapport v9, B1 | juste |
| v10 verdict 5 | version 28 | `E_PROCESSUS` | juste |
| v10 verdict 7 a | 4,1 points en moyenne, jusqu'à 14 ; 13,5 % et 34 % | rapport v9, C et D | justes |
| v10 verdict 7 b | 16 % ; 0,1368 contre 0,1367 | rapport v9, D et K9-8 | justes |
| v10 verdict 7 c | 0,5 ≈ 14 points | C : 14,4 entre 1,5 et 1,0 seulement | à préciser (K10-10 a) |
| v10 § 1 | 0 sur 250 ; 0,011 et 0,021 | rapport v9, Q3 | justes |
| v10 § 3 | signatures `entrer(cles)`, `ajouter_trajectoire(empreinte_cle, empreinte_unites)`, `evaluer(generation, fiche, journal)`, `canonique`, `identite`, cinq artefacts | code v28 | justes |
| LISEZMOI v28 | 276 essais | 276 `def test_` ; 41 ciblés passent (2,2 s) | juste (suite entière non relancée) |
| LISEZMOI v28 | 1,2 et 1,0 en génération 2, Bonferroni oui ; 0,5 en génération 2, non ; 0,8 en génération 4 ; 0,1 non (+0,000) ; forme-G1 en génération 3, 5,22 / 6,87 ; 25 / 25 ; nul × 200 : 0, [0 ; 0,019] ; cinq refus | `lecture-pari-apparie.json` `c91eee02…`, `course.json` `7e5f1183…` | justes (lecture de L3 : K10-8) |
| LISEZMOI v28 | « ≈ 90 s » pour nul 200 | 19 s pour nul 50 | plausible |
| démonstration v28 | `banque.json` `a08426e0…` | reproduite à l'identique | juste |

## 6. Vérifications sur processeur

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (Python 3.13.17, numpy 2.5.4). Graines :
`numpy.random.SeedSequence(2026102810, spawn_key=(section, …))` (R9) dans le script principal ; graines fixes et nommées
dans le script des étiquettes, qui ne tire rien d'aléatoire hors de la démonstration. Les manifestes sont dans les
sorties (empreintes du script et du code lu, durées). Le script principal n'a pas changé entre l'exécution de mise au
point (REP = 4, rendue) et l'exécution rendue (REP = 200) : même empreinte, section A identique. Une seule retouche les
a précédées, d'affichage (le champ `finales_egales` de A3). Un profilage d'une répétition de H à 30 générations, sans
lecture de résultat, n'est pas rendu.

| fichier | SHA-256 |
|---|---|
| `contre-verification-pari-signe-v10.py` (A, G, H, H3, C) | `4606a33c8289e8dfbc448df3b5b29f65247f7f856f3391579103ab3b588c73f2` |
| `contre-verification-pari-signe-v10-sortie.json` (REP = 200 ; 207 s) | `0a2a2d109071ca79dd7dd445f5b0774ddf91b3948a27d12a6af51428a2ff7374` |
| `contre-verification-pari-signe-v10-mise-au-point-rep4-sortie.json` | `6431a800ae9d4d39479140edead60264f9ce72ff5e4877bc3ebecfcff7a8141b` |
| `contre-verification-pari-signe-v10-etiquettes.py` (L, F) | `cfa8e8ab80982d667d2b13c9c5bff94c8731f16922cb8a8c7c48b6b09593534a` |
| `contre-verification-pari-signe-v10-etiquettes-sortie.json` | `9d14c4fe526310001fe59de1e6bc0927e1c95223ab8348d232d9cfde4f9f7fba` |
| `rejeu-scripts-v9-console.txt` (scripts v9 rejoués tels quels, REP = 20) | `7cd334557f78c4d010fd34c94fa2660449f45a2060488a3395cb8e302fa2b613` |
| `essais-cibles-console.txt` (41 essais, OK) | `201fc67bd8a1ee840ab1b47995bb67d347228ae89e1db48b96628490bad363d0` |
| `demo-reproduite-nul50-console.txt` | `8800115bd0f79911e8a36d1a2ebb80e6b4431879be10d526aac961c4101059e0` |
| `demo-reproduite-nul50/` : `banque.json` `a08426e0…`, `course.json` `7e5f1183…` (identiques aux publiés), `lecture-pari-apparie.json` | `21eb827e8ac352877a2757cb23b345d22b25ad9c74433cba2ee5f30cca7333da` |

**Sections.**
- **Rejeu v9 tel quel.** Le script de la chaîne s'arrête à l'étape 1 : `EngagementInvalide : fiche 'copie' : même clé
  de l'héritage que 'fiche'`. Le script principal s'arrête en A2 : « une tranche libre demande sa génération ».
- **A** (rejeu adapté de A1 à A7, et A8 à A10 nouveaux). Résultats en § 1 et § 3.
- **G** : la chaîne de K9-1 par la `Course` v28, avec journal et clés. La copie est gardée sous une clé distincte pour
  isoler l'étape 2 ; 200 courses × 10 générations. On compte 457 lectures tentées par la fiche et 451 refusées
  (« fraîcheur par rapport à la course »). La fiche n'est jamais promue. Au moins une promotion, la copie honnête, dans
  0,035 des courses. Pour continuer après un refus, il a fallu effacer l'entrée du journal (K10-5).
- **H** (H1, H2) : banque à nul exact, 20 unités par tranche, 8 sabotés et 8 honnêtes par unité, décalage 1,5 commun.
  Aucun refus de la course dans les 600 courses de chaîne. **H3** : 4 tranches de 40, fiche seule, K graines du monde
  essayées. La reproduction d'`evaluer` est vérifiée.
- **C** : formule de l'espérance conditionnelle (100 000 unités × 8), rappel par décalage au seuil vrai, gardes de la
  forme G1.
- **L** : canaux d'ordre hors clé, génération en chaîne, contenu du journal.
- **F** : forme-G1 recalculée sur la banque reproduite (clé égale à la publiée) ; incréments égaux à ceux de
  `course.json`.

**Limites.**
- Mondes synthétiques, et mesures sur des courses à une ou deux fiches : l'ampleur dépend de la variance par unité
  (H3 contre B1 v9).
- La suite entière des 276 essais n'est pas relancée, seulement les 41 ciblés.
- `monde_banque_scores.py` n'est relu que pour `identite`, `seuil`, `parts` et `ordre_secret`.
- Le lien au cycle n'existe pas en code.

Pour reproduire, depuis ce dossier, avec `R=…/orchestrateur-pole-v7` :
```
REP=200 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v10.py $R > contre-verification-pari-signe-v10-sortie.json
/opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v10-etiquettes.py $R > contre-verification-pari-signe-v10-etiquettes-sortie.json
(cd $R && /opt/venv-essaim-sim-v1/bin/python -I -B demonstrations/demo_pari_apparie_v7.py DOSSIER_NEUF --nul 50)
```

## 7. Fichiers lus et empreintes SHA-256

Dossier `…/` = `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`.
Tous sont conformes à leurs compagnons `.sha256`. Le code est conforme à `EMPREINTES-orchestrateur-pole-v7-v28.txt`
(`sha256sum -c` sans écart), elle-même conforme à son compagnon. Revérifié en fin de session : inchangé, et aucun
fichier du dossier `…/` plus récent que le brief. De la v27 à la v28 ont changé `pari_apparie.py`,
`engagement_apparie.py`, `monde_banque_scores.py`, la démonstration, deux fichiers d'essais et le LISEZMOI.
`test_v7_pari_apparie.py` est inchangé.

| fichier | SHA-256 |
|---|---|
| `…/pari-de-signe/conception-pari-de-signe-v10.md` | `1237d52d15f6b55cf3fd44c8ad6a6e155882b130c90c7f3022b501f9fad97bd2` |
| `…/pari-de-signe/conception-pari-de-signe-v9.md` | `aab37f630a1a310d1a4cebf35dac4c0cd6e53ebac327af5771ddaae101c0ceeb` |
| `…/pari-de-signe/conception-pari-de-signe-v8.md` (empreinte ; règles par la v9 et le rapport v9) | `3e9609fcaef05b539ed37065d229c7b46a86e9cbbfe79bb3e9b8233637b766f5` |
| `…/pari-de-signe/conception-pari-de-signe-v7.md`, `-v6.md`, `-v5.md`, `-v2.md` (recherches ciblées : garde, D-S8, § 2.4 bis) | `fb422cbc…`, `f21982cd…`, `95af46e4…`, `9c39a73d…` |
| `…/pari-de-signe/contre-lecture-v9/rapport-contre-lecture-pari-signe-v9.md` | `b73789ca2c02b9be8fe01641ec548625ce66aa647e07ddf44bbacb808954096f` |
| `…/pari-de-signe/contre-lecture-v9/contre-verification-pari-signe-v9.py` | `237322b7ae56a18ca6c8671b2a375826a24fb5bde1493558e619d72f3d43e7f1` |
| `…/pari-de-signe/contre-lecture-v9/contre-verification-pari-signe-v9-chaine.py` | `ebcd9829fe70bd35481fdf075c6e655818cb3d826977bb8822ad67a11618d719` |
| `…/pari-de-signe/contre-lecture-v8/rapport-contre-lecture-pari-signe-v8.md` (empreinte ; par le rapport v9) | `b2edabeb555f95c6571a2712ca2391ad81b3a28b27d77d594a6809e6ed45c638` |
| `…/pari-de-signe/simulation-dimensionnement-v2-sortie.json` (empreinte) | `d07e43f9702eabe93470ffee9f2124fdd18dfec1473ade225a8a6f9afafa33ea` |
| `…/../decision-N-056-noeuds-G1-bras-attaque-mesures-fortes-v1.md` | `6aac9746543cd05d0fc4fb89b32938d272e9b9723dab820d191cbb8297669eff` |
| `…/orchestrateur-pole-v7/EMPREINTES-orchestrateur-pole-v7-v28.txt` | `9cdc61d0a5c199fecc677dc9fac2c39b78008ff918d94b0aea244f7f9174544a` |
| `…/orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v28.md` | `6e105930aec90de6f76c28cafeb53ecc014018105518a0d87c03290d4d1271f3` |
| `…/orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v27.md` | `f0871a60ab4e208a924f6040bcd3e95b527c417df2ba6094ba0ede3d23d4ff4a` |
| `…/orchestrateur-pole-v7/pole/pari_apparie.py` | `40188f9f7154ede25cfe4148a02f97d88bd633b8ecc6c9e9c3597bcde44f598e` |
| `…/orchestrateur-pole-v7/pole/engagement_apparie.py` | `125dbe647ad62aea0bdbda9741384bfca1294399905b78787e57b3578c1112f3` |
| `…/orchestrateur-pole-v7/pole/monde_banque_scores.py` | `64463ec422185eb8d102c80eff4ee9a0df5aa4fec7a5283d31215a574731f375` |
| `…/orchestrateur-pole-v7/demonstrations/demo_pari_apparie_v7.py` | `e371795707daec0826220c75712e9eec5634a21810d2c235b32b516f4c128903` |
| `…/orchestrateur-pole-v7/essais/test_v7_pari_apparie.py` (inchangé depuis la v27) | `c367a38eac4439e0e04fda8f467b70bf67cba81a1c698238ca14d64384c8a76e` |
| `…/orchestrateur-pole-v7/essais/test_v7_engagement_apparie.py` | `f1a63f2d92987128b42c77a84bc730740d6f6baf2d9893f277f4a0657037616a` |
| `…/orchestrateur-pole-v7/essais/test_v7_demo_pari_apparie.py` | `a14d6c0653cab8ca289fee99b102ac7445e12ff27f6fcd34dd79797cb4c0c355` |
| `…/pari-de-signe/demonstration-v28/lecture-pari-apparie.json` | `c91eee0226daa1a71973ef30796dca06ef929ae7f51d97d477b7ebff8b3a7131` |
| `…/pari-de-signe/demonstration-v28/course.json` | `7e5f11835032833e90b0c43e7daf49a94b9f1963ee09ac2a13b239e78143f132` |
| `…/pari-de-signe/demonstration-v28/LISEZMOI-demonstration-v28.md` | `b7e4af48b65dd4c7197d20fae8c1e8154326f44e71d584a73f3d21b7e961c3f9` |
| `…/pari-de-signe/demonstration-v28/banque.json.sha256-seule.txt` (banque `a08426e0…`) | `845b17174f3d3e0e61562582c725e4e576c903ebfa00833b9684517a1102770a` |
| `…/pari-de-signe/demonstration-v27/course.json` (empreinte) | `5c5098ea885eb137b1d2620952d2a3deead0b3c28eee5f2bb18cd214dddeeb70` |

Empreinte de ce rapport : dans son compagnon `rapport-contre-lecture-pari-signe-v10.md.sha256` (un fichier ne peut pas
contenir sa propre empreinte). Heure de fin (lue sur `date -u` dans un appel séparé, juste avant cette ligne) :
mercredi 28 octobre 2026, **01:57:04 UTC**.
