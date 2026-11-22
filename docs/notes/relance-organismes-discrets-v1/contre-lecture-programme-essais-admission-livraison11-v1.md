# Contre-lecture du programme des essais d'admission du bras A, livraison 11 (noms `_v10`) — v1

**Verdict : engageable après corrections.**

La levée des seuils de crédit de Google est juste. Elle est lue au registre, refuse un GO échu, et écrit le crédit sous le seuil au contrôle du crédit, au relevé, à la lecture de la console et au mot sur les sondes. Avec « exiges », le refus est gardé. Le reste de `_v9` est intact.

Un défaut bloque Google : **le programme ne distingue pas un code 429 de simple limite de débit d'un crédit épuisé.** Tout 429 réel de Google porte `RESOURCE_EXHAUSTED`, et presque toujours « quota » et « billing ». À la vérification, il tombe donc à la ligne 13 du classement (ligne close, nœud de Lazar, rien à refaire). Dans la file, c'est un arrêt sans l'attente du devis. Le chemin « attendre puis refaire » (devis 4.4, ligne 6 ; 5.6) n'est donc jamais emprunté chez Google. Le cas sain des essais tient seulement parce que le faux fournisseur rend un 429 sans mot et au statut `INVALID_ARGUMENT`, ce que Google ne fait pas.

Le sens inverse tient : un crédit épuisé n'est jamais refait (un seul appel, aucune attente, aucune réponse comptée).

- Contre-lecteur : Claude Opus 5.5, neuf. Je n'ai écrit ni ce code ni ses versions précédentes.
- Date : 2026-11-22.
- Rien n'est scellé, rien n'est committé.

## 1. Pièces lues, à leur empreinte

Empreintes recalculées, égales à la note de livraison et aux compagnons :
- chef `52c39b55…` ;
- relais de Google `c88fae29…` ;
- relais de Mistral `016f7428…` ;
- faux fournisseur `2e3ce905…` ;
- essais `39270559…` ;
- gabarit v10 `d44ed9b4…` ;
- campagne de mutations `5690fa75…` ;
- greffon des mutations `39f8a5b4…` ;
- note de livraison v10 `965ffd03…`.

Pièces de référence :
- mandat `d3bc3628…` ;
- avenant 3 v2 `4b331d9a…` ;
- avenant 2 v3 `9d4b8a08…` ;
- devis `421ee2e6…`, pour les seules lignes qui citent 429 (grep).

Diff de `_v9` à `_v10`, par `diff -u` :
- relais, faux fournisseur et gabarit : seuls les noms et les empreintes des relais changent ; le gabarit gagne le champ `seuils_de_credit_google` (nul) et sa note ;
- chef : 310 lignes de diff, toutes lues.

## 2. Essais lancés

- **Commande d'essai versée** (avec `-u RR_ANTHROPIC_API_KEY_MINUIT`) : `248 passed in 106.62s`.
- **Essais jetables**, hors du dépôt, au bloc-notes : `…/scratchpad/cl11/test_contre_lecture_l11.py`.
  - Ils réutilisent les montages `monde` et `banc` des essais v10, par import, et seulement le faux fournisseur local.
  - Lancés avec le même préfixe `env -u …`, sur ce seul fichier : 8 passés. **Écart déclaré à la lettre de la consigne** : ce fichier n'est pas celui de la commande donnée ; la suite entière n'a pas été lancée.
  - Registre fictif :
    - les vraies lignes GO-2026-11-22-02, -03, -16 et GO-2026-11-21-88, recopiées de la commande `git show origin/main:registres/go.md | grep …` donnée ;
    - trois lignes de calcul courtes fictives de Google, qui citent GO-2026-11-22-16, d'échéance 2026-11-30.
- **Campagne de mutations v6**, par la commande versée : section 4.

## 3. Ce qui est vérifié, point par point

### 3.1 Le champ `seuils_de_credit_google`

**Conforme dans son principe.**

- **Forme fermée** : `"exiges"` ou `{"leves_par": "<GO>"}`. Nul, absent ou d'une autre forme, il est refusé pour toute ligne de Google ; c'est éprouvé aussi à blanc. Mistral ne le lit pas : à blanc sans le champ, la ligne passe.
- **En configuration définitive**, la levée passe par `ligne_de_decision` (`scripts/chef_essais_admission_bras_a_v10.py:1394-1417`) :
  - une seule ligne, de huit cellules, de type `décision`, accordée par Lazar ;
  - échéance non passée : admise le 2026-11-30, refusée le 2026-12-01 ;
  - non révoquée ;
  - elle cite « recharge automatique ».
- **Avec les vraies lignes** :

  | GO cité dans `leves_par` | issue | motif |
  |---|---|---|
  | GO-2026-11-22-02 | admis | — |
  | GO-2026-11-22-16 | refusé | ne cite pas la marque |
  | GO-2026-11-22-03 | refusé | ne cite pas la marque |
  | GO-2026-11-21-88 | refusé | non accordé par Lazar |

- **Écrit** : le contrôle du crédit porte `seuils` (« levés par GO-2026-11-22-02 ») et `sous_le_seuil` par projet ; c'est éprouvé sur le relevé d'une vérification jouée contre le faux fournisseur. Le rapport de la file le recopie du manifeste. La lecture de la console et le mot sur les sondes l'écrivent aussi.
- **« exiges »** : le refus est gardé à la garde 9, à la garde 20 et à la garde 10 (essais versés, rejoués).
- **Réserves** : voir la correction 3 (toute décision qui cite la marque est admise) et la correction 2 (la garde 8 ignore l'avenant 3).

### 3.2 Le refus pour crédit épuisé

**Non conforme pour Google : correction 1.**

Faux fournisseur local, corps de forme supposée, non relevée :

| corps rendu | vérification | file |
|---|---|---|
| 429 de débit de Google, forme longue (`RESOURCE_EXHAUSTED`, « You exceeded your current quota, please check your plan and billing details … rate-limits », `QuotaFailure` « …PerMinute », `RetryInfo` `retryDelay` 23s) | 1 appel, ligne 13, close, nœud, `a_refaire` nul (« « quota » ») | arrêt au premier envoi, aucune pause, file incomplète |
| 429 de débit de Google, forme courte (« Resource has been exhausted (e.g. check quota). ») | ligne 13, close | — |
| 429 de crédit épuisé de Google (« Your prepayment credits are depleted … billing ») | ligne 13, close, 1 appel | arrêt, aucune pause |
| 429 de débit de Mistral (« Requests rate limit exceeded ») | ligne 6, à refaire, non close | — |
| 429 de Mistral « Insufficient balance » | ligne 13 | — |

Ce qui en ressort :
- **Le crédit épuisé n'est jamais refait : conforme.**
- **Un 429 de débit de Google arrête la ligne, à tort.** À la vérification, la ligne entière se ferme en nœud de Lazar, alors que le devis dit « refaite sous la même ligne » (4.4, ligne 6). Dans la file, l'attente et la reprise unique de 5.6 sont perdues, alors que le devis dit « 429 puis 200 : la file continue » (tableau de la section 10, ligne 4).
- La note de livraison le dit elle-même (« Lecture prudente : chez Google, un 429 `RESOURCE_EXHAUSTED` y entre, qu'il soit de quota ou de débit »). Mais elle le présente comme sans effet, alors que c'est le cas ordinaire, et l'écart au devis qu'elle déclare ne couvre que le 402.

Effet en argent : nul, puisqu'un refus n'est pas facturé. Effet sur le programme : une limite de débit, banale sous un premier appel à 65 536 jetons, coûte une ligne de calcul et un nœud de Lazar, et la file Neon s'arrête sur son premier 429.

### 3.3 Le reste de `_v9`

**Intact.**

- **Garde 8 avec l'avenant 2** : une ligne de Google doit toujours citer l'empreinte de l'avenant 2. Le code n'a pas changé (diff) et les essais l9 et l10 passent.
- **Exemption de la sonde, lue au registre** : GO-2026-11-22-03 est admis, avec sa vraie ligne. GO-2026-11-21-88 est refusé (« n'est pas accordée par Lazar »), et GO-2026-11-22-16 aussi (ne cite pas « exemption de la sonde »). La mise en commun dans `ligne_de_decision` ne change rien à l'exemption : `sans_marque` n'est vrai que pour le GO d'origine, comme avant.
- **Limite de sortie** : `sortie_max` nul ou de 32 768 est refusé par la règle de Google et par l'avenant 2. Les refus de `outputTokenLimit` absent sont inchangés (diff).
- **Régime prudent** : `"courant"` est refusé en configuration définitive.
- **Compteur** : il n'est pas touché par le diff. Le refus pour crédit est compté par la règle d'un code d'erreur.
- **Seule autre modification**, `lien_constate` (ligne 972) : `not lien_leve` est retiré. C'est équivalent : une clé levée porte nécessairement la valeur « non constaté, levé par … », jamais « oui » (garde 9, lignes 782-791).

### 3.4 La configuration définitive de Google de la note v10, éprouvée sur le faux fournisseur

Montage : la configuration de la section 3 de la note (`seuils_de_credit_google` levés par GO-2026-11-22-02, exemption sous GO-2026-11-22-03, 65 536 et 49 536, régime prudent, 300 et 300 mots, 5,1 jetons par mot), avec le registre fictif de la section 2.

- **À blanc** : les deux vérifications passent. Mode « leves », registre non lu.
- **Gardes de départ, sans envoi** : elles passent pour les deux vérifications. La levée est lue sur la vraie ligne GO-2026-11-22-02, l'exemption sur GO-2026-11-22-03 ; le contrôle du crédit porte « levés par GO-2026-11-22-02 ».
- **Règle de Google** : 300 × 5,1 = 1 530, sous 16 000 ; débit requis à la sortie maximale de la file : 24,4 jetons par seconde.
- **Garde 8** : elle admet une ligne courte qui ne cite ni GO-2026-11-22-16 ni l'empreinte de l'avenant 3 (correction 2).

## 4. Campagne de mutations v6

Commande versée, `toutes`, avec `-u RR_ANTHROPIC_API_KEY_MINUIT` en plus : **616 tués sur 616, code de sortie 0**. Cela fait un mutant de plus que les 615 sur 616 de la note, ce qui est cohérent : le survivant de la note a été tué par l'essai qu'elle a ajouté ensuite.

Mutants tués par campagne :

| campagne | tués |
|---|---|
| `regle_google` | 108 |
| `livraison6` | 168 |
| `livraison7` | 80 |
| `livraison8` | 48 |
| `livraison9` | 120 |
| `livraison10` | 26 |
| `livraison11` | 66 |

Résultats au bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/080a2aff-9781-5a4d-8af3-2aae94066157/scratchpad/cl11/mutations-toutes.json`.

La campagne tue tout ce qu'elle mute, mais elle ne voit pas la correction 1. Le défaut ne vient pas d'un opérateur : il est dans la liste des mots, et dans le faux fournisseur, qui ne rend pas le 429 tel que Google le rend.

## 5. Corrections

**1. Distinguer le 429 de débit du crédit épuisé (bloquant pour Google).**
- **Où** :
  - `scripts/chef_essais_admission_bras_a_v10.py:2509-2529` (`MOTS_DU_CREDIT_EPUISE`, `refus_pour_credit`), qui commande les lignes 2565 (`classer_issue`), 2979 (la sonde) et 3128 (`decider_dans_la_file`) ;
  - `tests/faux_fournisseur_essais_admission_v10.py:160-165` ;
  - `tests/test_chef_essais_admission_bras_a_v10.py:4715` et `:4759`.
- **Scénario** : premier appel A de la vérification de la clé 1, ou premier envoi de la file Neon. Google rend un 429 `RESOURCE_EXHAUSTED` de limite par minute, avec « quota », « billing » et `RetryInfo`. La ligne se ferme en ligne 13, nœud de Lazar, ou la file s'arrête sans attente.
- **Correction proposée** :
  - (a) Pour un 429, ne plus tenir « quota », « billing » ni « exhausted » pour des signes de crédit. Garder seulement des mots propres au crédit : `prepay`, `depleted`, `credit`, `crédit`, `balance` en mot entier, `insufficient`, `payment`, `solde`. Le 402 reste du crédit épuisé, et le 400 ou le 403 peuvent garder la liste large, puisqu'ils arrêtent de toute façon.
  - (b) Un 429 de Google sans mot de crédit, et qui porte `RetryInfo` ou `retryDelay`, un `quotaId` en « PerMinute », ou le lien `rate-limits`, est un débit : ligne 6 à la vérification, attente puis reprise unique dans la file (devis 5.6). Lire `retryDelay` comme `Retry-After`, avec la même borne de 600 secondes.
  - (c) Un 429 sans aucun de ces signes est à trancher par la mère, au choix :
    - le traiter comme un débit : une reprise, puis un second 429 arrête, sans coût puisqu'un refus n'est pas facturé ; c'est ma recommandation, confiance moyenne ;
    - l'arrêter sous un motif distinct, « 429 de cause non lue », qui n'est pas « crédit épuisé ».
  - (d) Rendre au faux fournisseur un statut `RESOURCE_EXHAUSTED` pour le 429. Ajouter trois essais : le débit long (attente, reprise, file complète, ligne 6 à la vérification), le crédit épuisé (`prepayment credits are depleted`, arrêt) et le cas indéterminé.
  - (e) Mettre la forme du refus aux reprises ouvertes : « à vérifier au premier appel », dit GO-2026-11-22-02.

**2. La garde 8 ignore l'avenant 3.**
- **Où** : `scripts/chef_essais_admission_bras_a_v10.py:524-529` (`verifier_ligne_de_calcul`).
- **Scénario** : la configuration lève les seuils, mais la ligne de calcul de Google au registre ne cite que l'avenant 2, dont le texte dit que les seuils refusent. Elle passe. L'avenant 3 demande pourtant (section 3, point 5 ; section 4, dernier paragraphe) que la garde 8 lise son empreinte et que chaque ligne la cite.
- **Correction proposée** : quand `seuils_de_credit_google` est levé, exiger de chaque ligne de Google, au périmètre ou à la référence, l'empreinte de l'avenant 3 accepté (`4b331d9a…`, ajoutée à la configuration comme `avenant_3`, chemin et empreinte, vérifiée sur disque) et le GO de la confirmation (GO-2026-11-22-16, que la ligne de registre de GO-16 demande de citer). Ajouter un essai sain et un artefact.

**3. La levée est admise sous toute décision de Lazar qui cite « recharge automatique ».**
- **Où** : `scripts/chef_essais_admission_bras_a_v10.py:1420` et `:1438-1452`.
- **Scénario** : `leves_par` vaut une autre décision de Lazar qui parle de la recharge sans lever les seuils. Avec un GO-2026-11-21-99 fictif, « la recharge automatique reste activée », la levée est **admise**. L'avenant 3 (section 3, point 1) n'admet la levée que sur la ligne GO-2026-11-22-02.
- **Correction proposée** : fixer, comme pour le GO d'origine de l'exemption, la constante `GO_DE_LA_LEVEE_DES_SEUILS = "GO-2026-11-22-02"`, et refuser toute autre valeur de `leves_par`. À défaut, exiger en plus la ligne de confirmation GO-2026-11-22-16 (décision, Lazar, non échue, qui cite « seuils levés »).

## 6. Mineurs

1. **La forme du champ diffère de l'avenant 3** (section 3, point 1 : `"appliques"` et `"leves"`) : le code prend `"exiges"` et `{"leves_par": …}`. C'est acceptable, puisque l'avenant dit « forme proposée », mais la note ne déclare pas cet écart.
2. **Les mots de crédit sont cherchés comme sous-chaînes** (`chef…:2526-2527`) :
   - « balance » prend « load balancer » ;
   - « quota » prend tout 400.
   Comme le contrôle passe avant les lignes 9, 10 et 11 du classement (`:2565`), un 400 d'orthographe du niveau de réflexion qui contiendrait « quota » perdrait l'appel A′ (éprouvé : « code 400, « quota » »). Placer le contrôle du crédit sur un 400 après les lignes 9 à 11, ou le borner à 402, 403 et 429.
3. **Le refus pour crédit s'applique aussi aux lignes de Mistral** (un 402 ou un 429 « insufficient » : ligne 13, close), alors que GO-2026-11-22-02 ne vise que Google. L'écart est à déclarer pour Mistral, ou à borner à Google.
4. **La sortie `a-blanc`** (`chef…:4055-4065`) n'imprime ni le mode des seuils ni le fait que le registre n'a pas été lu. Ajouter `seuils_de_credit_google`.
5. **Les fonctions changées hors de la campagne** : `classer_issue`, `decider_dans_la_file`, `jouer_verification` (la branche de la sonde) et `garde_console` ne sont pas dans les cibles de la campagne `livraison11` (`campagne_mutations_v6.py:65-68`). Elles sont couvertes seulement par des essais ciblés.
6. **Les variables retirées par la campagne** (`VARIABLES_RETIREES`) ne comptent pas `RR_ANTHROPIC_API_KEY_MINUIT`. Je l'ai retirée à la main.
7. **L'échéance de la levée** n'est lue qu'au départ. Une file partie le 30 novembre au soir continue après minuit ; c'est sans conséquence pratique.

## 7. Ce que j'ai ouvert

- **Lu** :
  - le mandat (section des interdits) ;
  - l'avenant 3 v2, en entier ;
  - du devis, les seules lignes qui contiennent « 429 », par grep ;
  - les huit fichiers de la livraison et le gabarit v10, par diff avec `_v9` et par lectures de lignes ;
  - la note v10.
- **Du registre** : seulement la commande donnée. Elle a affiché aussi des lignes qui citent GO-2026-11-21-69 (GO-2026-11-21-70, -73, -81, -82, -83, -86 ; GO-2026-11-22-06 et -07) ; je ne m'en suis pas servi.
- **Lancé** :
  - la commande d'essai versée, une fois ;
  - mes essais jetables, sur leur seul fichier ;
  - la campagne de mutations `toutes`, une fois ;
  - aucune autre commande.
- **Écrit** :
  - au bloc-notes : `test_contre_lecture_l11.py`, `lignes-go-reelles.txt` et les sorties ;
  - dans le dépôt : cette note seule.
- **Rien d'autre** :
  - aucun réseau, aucun `git fetch` ;
  - `GO_ID` jamais fixé, aucune clé lue ;
  - aucun chemin cloisonné ouvert, listé ni cherché, rien sous `runs/` ;
  - aucun `sed` qui écrit, rien scellé.
