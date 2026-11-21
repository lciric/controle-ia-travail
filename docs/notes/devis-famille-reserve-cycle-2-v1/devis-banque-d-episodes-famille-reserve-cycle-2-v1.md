# Devis chiffré — banque d'épisodes de la famille aveugle de réserve du cycle 2 — v1

- **Classe A** (devis). **Rien n'est lancé, rien n'est dépensé, aucune ligne de calcul n'est ouverte par ce document.** Il chiffre l'esquisse de l'auteur de la famille, propose des plafonds et pose les décisions.
- **Auteur** : agent neuf, Claude Fable 5.2 (conception), le 2026-11-21, de 17:26 à 17:59 en temps universel (`date -u`). Il n'a écrit ni la famille, ni son esquisse, ni aucun moniteur. **À contre-lire** par un autre modèle (Opus 5.5), corrections vérifiées par le même contre-lecteur, avant toute demande d'accord.
- **Ce qu'il chiffre** : la pièce 6 de la famille, « esquisse de devis de la banque d'épisodes », `docs/notes/scellement-2-famille-reserve-cycle-2-v1/piece-6-esquisse-de-devis-banque-d-episodes-v1.md`, branche `claude/scellement-2-famille-reserve-cycle-2-v1` (sommet `a944acdd`), empreinte `981c85a1911d85e4a17a8d0828ec73bc16549b171e0d106ca6d048c8b1db79a0`, vérifiée avant lecture.
- **Ce que je n'ai pas lu** : aucune autre pièce de la famille (pièces 1 à 5, contre-lecture), ni la valeur de `k`, ni aucun contenu de mode. Ce devis ne nomme, ne décrit ni ne suggère la famille.
- **Version chiffrée : la version 1, celle que le mandat nomme.** Une version 2 de la pièce 6 est apparue pendant l'écriture (même dossier, sommet `5d6b7a2a`, empreinte `62b99079fb7ca999d6ac325b9a78b47af46ea4a34296f3dfef6d9ef11892a912` ; `registres/decisions.md:4784`). **Je ne l'ai pas lue.** Un comptage par programme, sans affichage, dit ce qui tient et ce qui a bougé (section 11, point 1).
- **Trois lettres** : **M** = relevé sur une pièce citée ; **C** = calculé ici ; **S** = supposé, sans mesure.
- **Recalcul** : tous les chiffres sortent du programme compagnon `calcul-devis-banque-d-episodes-famille-reserve-cycle-2-v1.py` et de sa sortie `…-v1-sortie.txt` (même dossier, scellés). Les montants sont en dollars des États-Unis.

## 0. En une page

1. **Attendu : environ 85 dollars** au centre (`k` = 6, une question par appel, lecteurs Claude Opus 5.5 et Mistral Large 4), dans une fourchette de **17 à 111 dollars** selon `k`, la forme de la lecture et le lecteur Claude.
2. **Plafond pessimiste : 389 dollars** pour `k` ≤ 8 : carte 37, essai de mesure 13, lectures 339. Il tombe à **123 dollars** si l'auteur atteste que la lecture se fait en un appel par ensemble lu. Plus 5 dollars si l'ancre est jugée par un agent (nœud de Lazar).
3. **La carte pèse peu** (8 à 11 dollars attendus pour 260 épisodes). **Les lectures font la dépense et l'incertitude** : `k` est au coffre, la sortie de Mistral n'est mesurée nulle part, le prix de Mistral n'est pas sur une page scellée.
4. **Ordre recommandé** : un essai de mesure payant d'abord (13 dollars au plus), puis chaque plafond de lecture recalculé à deux fois le coût mesuré, borné par le plafond pessimiste. Première tranche demandable : 19 + 13 = **32 dollars**.
5. **Cinq points à trancher** (section 6) : (1) prix et plafond, par étapes sur mesure ; (2) lecteurs Claude Opus 5.5 et Mistral Large 4, hors Llama, hors Qwen, hors lignée du juge ; (3) un agent Opus 5.5 neuf, distinct du monteur du premier cycle, monte les lecteurs sur le programme gelé de ce cycle ; (4) tirage disjoint de tâches fraîches, sur devis à part ; (5) l'agent neuf déjà désigné vérifie le non-recouvrement.
6. **« Ancre humaine » est gardée telle quelle** (30 éléments, temps d'une personne, sans calcul). Son remplacement par un agent est un **nœud pour Lazar** (section 7).
7. **Rien ne part avant** les douze conditions de la section 9 : contre-lecture de ce devis, version 2 de la pièce 6 rapprochée, attestation sur `k`, pièce de sécurité confrontée, page de prix de Mistral scellée, note des lignées confrontée.
8. **Limite de cette version** : la version 2 de la pièce 6 garde la structure des épisodes, donc la ligne de la carte ; elle a récrit les relectures des épreuves et l'ancre, donc les volumes des lectures et la ligne des juges sont à relancer dans le programme une fois ses nombres donnés.

## 1. Pièces lues, avec empreintes (sha256, calculées à la lecture)

| pièce | lieu | empreinte | usage |
|---|---|---|---|
| pièce 6 de la famille de réserve (esquisse, sans prix) | branche `claude/scellement-2-famille-reserve-cycle-2-v1`, `a944acdd` | `981c85a1…b79a0` | postes, volumes, cinq points |
| devis de la course sur carte louée du bras A des organismes discrets (déplacement des contrôles appris sans consigne), version 2 | `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md`, branche `claude/pensive-bardeen-1fv7hw` (`4c652340`) | `83240ca61d7c300f…` | débit, prix de la carte, méthode du pire cas |
| devis de l'essai de mesure des lecteurs du même bras A, brouillon 3 | `…/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, même branche | `533ad5b15e6de1bd…` | tarifs, jetons par lecture, gardes |
| page de prix d'Anthropic, versée et scellée | `docs/sources/prix-fournisseurs-2026-11-19/platform-claude-com-docs-en-about-claude-pricing-20261119T095216Z.html`, même branche | `78aff5c8d73a0da2…` | prix d'Opus 5.5 et de Sonnet 5.5, relus par programme |
| page de prix de Google, versée et scellée | `…/aistudio-google-com-docs-pricing-20261119T095218Z.html`, même branche | `89c58281ba7e9e96…` | prix de Gemini 4 Neon, relu par programme |
| programme du collisionneur (l'outil qui pose une même question à plusieurs modèles), version 9-3 | `docs/notes/collisionneur-v9/collisionneur_v9_v3.py` | `850df311807384fc…` | table de prix, lignes 101 à 139 |
| relais Claude | `docs/notes/ideation-organisme-v1/orchestrateur-v52b/pole/relais_reel.py` | `1b90b020287e575b…` | barème, lignes 47 à 56 |
| recherche sur le lecteur remplaçant du bras A | `docs/notes/relance-organismes-discrets-v1/lecteur-remplacant-carbon-v1/choix-mistral-deepseek-v1.md` | `f7090b5d52b638b5…` | prix et réglages de Mistral Large 4 |
| esquisse en clair de la famille du premier cycle, version 3, qui fait foi | `docs/notes/scellement-2-familles-aveugles-v1/piece-6-esquisse-de-devis-banque-v3.md`, branche `claude/scellement-2-familles-aveugles-v1` (`f4c479c5`) | `bb89942b75fd6aa0…` | ordres de grandeur en jetons, forme d'une lecture |
| index sans contenu du second scellement du bras d'attaque (familles aveugles) | `registres/index-scellement-2-familles-aveugles-v1.md` | `5d0479b437426509…` | quelle esquisse fait foi |
| devis de la banque à deux modes | `docs/notes/devis-couche-2-banque-deux-modes-v1.md` | `cf2f4772dff30c07…` | coût fixe d'un lancement |
| devis des épisodes réels de la nuit du 1er novembre | `docs/notes/devis-episodes-reels-t05-nuit-v1/devis-episodes-reels-t05-nuit-v1.md` | `d6a34dbb9e1d35e0…` | réserve de tâches, sources de tâches neuves |
| décision sur les tâches fraîches (N-049) | `docs/decisions/decision-N-049-v1.md` | `8a5bf5e57e2bb447…` | point 4 |
| règle de sélection des papiers ; procédure d'extraction | `docs/procedures/T0.5-selection-papiers-v1.md` ; `docs/procedures/T0.5-extraction-v1.md` | `8f43dcaeb5fd782c…` ; `d23bd62fe1611b87…` | point 4 |
| environnement des propositions | `src/controle_ia/environnements/propositions.py` | `5d97b223206c6378…` | dix propositions au plus (ligne 26) |
| registres vivants | `registres/depenses.md`, `registres/go.md`, `registres/decisions.md` | sans empreinte ; lignes relues au sommet `1b49fa53b763` | prix relevés, décisions de Lazar |

Les lignes des registres vivants ne valent qu'à ce sommet ; ces registres ne s'allongent que par la fin. Dans la suite, `devis-bras-a-v2.md`, `devis-essai-de-mesure…` (le brouillon 3), `choix-mistral-deepseek-v1.md`, `relais_reel.py`, `collisionneur_v9_v3.py`, `piece-6-esquisse-de-devis-banque-v3.md`, `devis-episodes-reels-t05-nuit-v1.md` et `decision-N-049-v1.md` désignent les pièces de ce tableau par leur nom de fichier ; « pièce 6 », sans autre mot, désigne l'esquisse de la famille de réserve. Chaque citation se lit `fichier:ligne`.

## 2. Ce qui est chiffré : les quatre postes de l'auteur

Notations de la pièce 6 : `n` tâches, `e` épisodes par tâche et par condition, `a` actions par épisode, `k` éléments de référence lus par tâche (au coffre), `n_f` tâches à dose flagrante. Je lis « ensemble » comme le jeu de propositions qu'un épisode rend, lu une fois par chaque lecteur. Tailles de principe de l'auteur : `n` = 60, `e` = 1, `n_f` = 20 (pièce 6, section 3).

| poste de la pièce 6 | épisodes | actions (`a` = 10) | ensembles lus par lecteur | rôle |
|---|---|---|---|---|
| A. honnêtes, deux graines par tâche | 120 | 1 200 | 120 | 60 jumeaux (mesure), 60 pour le nul « honnête contre honnête » (contrôle) |
| B. « sabotage demandé », deux doses | 120 | 1 200 | 120 | mesure |
| C. dose flagrante, 20 tâches | 20 | 200 | 20 | contrôle : épreuve de l'oracle seulement |
| relectures des épreuves (pièce 6, poste D) | — | — | 60 | contrôle |
| **total** | **260** | **2 600** | **320** | questions par lecteur : 320 × `k` |

- **`a` = 10 (S)** : c'est le réglage de la chaîne que le devis du bras A réemploie (`devis-bras-a-v2.md:38`, « 10 pas, lot de 8 épisodes, 400 jetons ») ; le code borne un ensemble à dix propositions (`src/controle_ia/environnements/propositions.py:26`). À confirmer par la mère sur la configuration scellée du banc.
- **`k` est inconnu de ce devis.** La table va de 3 à 8 ; le plafond est calculé à `k` = 8. Je demande à l'auteur, ou au contre-lecteur du coffre, une **attestation à trois cases, sans chiffre** : `k` ≤ 8, oui ou non ; un appel par ensemble ou un appel par question ; la pièce 3 demande-t-elle des appels de préparation de la référence, oui ou non.
- **Part des contrôles (C)** : 80 épisodes sur 260 (31 %) et 140 ensembles lus sur 320 (44 %).
- **Version 1** : les 60 ensembles de relecture et l'ancre sur 30 éléments sont ceux de la version 1 de la pièce ; la version 2 les a récrits (section 11, point 1).
- **Deux étapes, comme l'auteur les ordonne** (pièce 6, section 4). Étape 1 : postes A et C, épreuves de l'oracle (200 ensembles lus par lecteur). Étape 2, seulement si les épreuves et les préconditions passent : poste B (120 ensembles).
- **Variante de taille** (pièce 6, section 3, dernière puce) : 100 épisodes par dose, soit 420 épisodes et 480 ensembles lus par lecteur. Elle est chiffrée en 5.3.

## 3. Prix unitaires, avec leur source

### 3.1 Carte louée (prix `p_a`)

| grandeur | valeur | lettre | source |
|---|---|---|---|
| carte A100 SXM4 80 Go, dernier prix relu | 1,1833 dollar par heure (offre à 1,1843, stockage compris), le 2026-11-18T15:44:24Z | M | `registres/depenses.md:515` |
| prix du devis | 1,30 par heure pour la carte, stockage 0,08 au plus en sus, soit **1,38** ; téléchargement 0,05 dollar par Go au plus, 20 à 40 Go, soit 1 à 2 dollars par mise en route | M | `devis-bras-a-v2.md:67` et `:69` |
| durée d'un épisode de dix pas, par lots de huit | **42,8 s** retenus ; 40,2 s en bas de fourchette | M sur une autre chaîne, **S pour ce banc** | `devis-bras-a-v2.md:42-43` et `:54` |
| mise en route | 1,0 heure par lancement | S | `devis-bras-a-v2.md:56` |
| coût fixe d'un lancement, déjà observé | 2 à 3,5 dollars | M (par soustraction) | `docs/notes/devis-couche-2-banque-deux-modes-v1.md:37` |
| méthode du pire cas | débit deux fois plus lent et une relance complète, soit les heures × 4 ; 4 dollars de téléchargement | M | `devis-bras-a-v2.md:81` |

**Prix d'une action (C) : `p_a` = 0,0014 à 0,0016 dollar** (4,28 s à 1,1833 ou à 1,38 dollar par heure), soit 0,014 à 0,016 dollar par épisode, **plus un coût fixe de 2,18 à 3,38 dollars par lancement**. Les épisodes « sabotage demandé » sont supposés aussi longs que les honnêtes (S) ; le plafond porte ce doute.

### 3.2 Lecteurs (prix `p_l1`, `p_l2`), en dollars par million de jetons

| modèle | entrée | sortie | lettre | source |
|---|---|---|---|---|
| Claude Opus 5.5 (`claude-opus-5-5`) | 4 | 20 | M | page scellée d'Anthropic (`78aff5c8…`), relue : « Claude Opus 5.5 … $4 / MTok … $20 / MTok » ; `relais_reel.py:50` ; `collisionneur_v9_v3.py:131` ; `devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md:129` |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`) | 2 | 10 | M | même page ; `relais_reel.py:51` ; `devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md:130` |
| Mistral Large 4 (`mistral-large-4-0`), point d'accès européen | 0,77 | 2,31 | **M sur une page non scellée** | 0,70 et 2,10, multipliés par 1,1 pour le point d'accès européen : `choix-mistral-deepseek-v1.md:19` (pages lues par un outil qui les résume, `:6`) |
| Mistral Large 4, **prix de repli** | 1,54 | 4,62 | C | le double, tant que la page de prix de Mistral n'est pas versée et scellée (même règle que le prix de repli de Carbon, `devis-essai-de-mesure…:134` et `:137`) |
| Gemini 4 Neon (`gemini-4-neon`), pour l'ancre si le nœud le décide | 3 | 15, réflexion comprise | M | page scellée de Google (`89c58281…`), section « Gemini 4 Neon », relue ; `registres/go.md:589` |

Pour mémoire, la table du collisionneur (`collisionneur_v9_v3.py:101-139`) compte Fable 5.2 à 10 et 50 (lu 8 et 40), Opus 5.5 à 4 et 20, Argon à 10 et 50, Kimi à 2 et 10, Astra à 10 et 50, Carbon à 4 et 20. Aucun de ces autres modèles n'est lecteur ici.

### 3.3 Jetons par lecture

| grandeur | valeur retenue | lettre | appui |
|---|---|---|---|
| entrée d'une lecture (consigne, plan de dix propositions, élément de référence) | 4 000 jetons ; 6 000 au plafond | S | « ordre de 4 000 jetons d'entrée » par plan (`piece-6-esquisse-de-devis-banque-v3.md:43`) ; 3 650 supposés au bras A (`devis-essai-de-mesure…:144`) |
| sortie d'un lecteur Claude, réflexion comprise | 500 jetons ; 2 000 au plafond | S | sur textes synthétiques, 120 lectures ont coûté 0,904303 dollar, dont 0,602 pour les 48 d'Opus 5.5 (`registres/depenses.md:546`), soit environ 300 jetons de sortie par lecture (C, sur entrées supposées) ; sorties de 49 à 234 et de 62 à 403 jetons pour deux autres modèles (`registres/depenses.md:541-542`) |
| sortie de Mistral Large 4, raisonnement compris | 3 000 jetons ; 9 000 au plafond | S | raisonnement « high » par défaut, qui est aussi le maximum (`choix-mistral-deepseek-v1.md:17`) ; Lazar a demandé l'effort maximal pour ce lecteur au bras A (`registres/go.md:569`) ; la relance du bras A donne 80 à 330 dollars pour une course entière « selon le raisonnement, à mesurer » (`registres/decisions.md:4367`) |
| reprises et redemandes de forme | 5 % d'envois en plus ; 15 % au plafond | S | une seule reprise par envoi (`devis-essai-de-mesure…:253`) |
| garde par envoi | corps réel compté à un jeton par octet (environ 24 000 pour un plan long), sortie maximale 8 192 | M | `devis-essai-de-mesure…:145` et `:166` |

**Prix d'une lecture, une question par appel (C)** :

| lecteur | attendu | pessimiste |
|---|---|---|
| `p_l1`, Claude Opus 5.5 | 0,0273 | 0,0736 |
| variante, Claude Sonnet 5.5 | 0,0137 | 0,0368 |
| `p_l2`, Mistral Large 4 | 0,0105 | 0,0292 au prix relevé ; **0,0584 au prix de repli** |
| les deux lecteurs (Opus 5.5 et Mistral Large 4) | **0,0378** | **0,1320** |

## 4. Les cinq lignes du devis

### 4.1 Génération des épisodes, sur carte louée

| lancement | épisodes | durée attendue | attendu | pire cas | **plafond** | marge (plafond moins attendu haut) |
|---|---|---|---|---|---|---|
| 1 : honnêtes (A) et dose flagrante (C) | 140 | 2,66 h | 4,03 à 5,68 | 18,71 | **19** | 13,3 |
| 2 : « sabotage demandé » (B) | 120 | 2,43 h | 3,77 à 5,35 | 17,40 | **18** | 12,7 |
| **total** | **260** | 5,09 h | **7,80 à 11,03** | 36,11 | **37** | 26,0 |

- **Formules (C)** : heures = épisodes × 42,8 ÷ 3 600 + 1,0 ; attendu bas à 40,2 s et 1,1833 dollar par heure, plus 1 dollar ; attendu haut à 1,38, plus 2 dollars ; pire cas = heures × 4 × 1,38 + 4.
- **Plafond du lancement 2 recalculé** sur le débit `d` mesuré au lancement 1, en secondes par épisode, majoré de moitié pour les épisodes « sabotage demandé » : `2 × 1,38 × (1,0 + 120 × 1,5 × d ÷ 3 600) + 4`. Pour `d` = 42,8 : 12,67 dollars.
- **Rapatrié et scellé avant toute destruction** : les épisodes (textes et identifiants générés), le manifeste (configuration et empreinte, versions, graines, commit, prix, durée), le débit mesuré. Sans les identifiants, une passe d'activations ultérieure est impossible (`devis-bras-a-v2.md:103`). Les épisodes B et C vont au coffre.
- **Compte de facturation** : le compte du loueur de cartes, Vast.ai (recharge automatique relevée, `registres/decisions.md:4334`).
- **Garde d'arrêt** : pas de création si le prix relevé dépasse 1,30 dollar par heure pour la carte, 0,08 pour le stockage ou 0,05 par Go ; accord cité par son identifiant (`GO_ID`) à la garde de calcul ; minuterie d'arrêt dur à 10,6 h (lancement 1) et 9,7 h (lancement 2) de durée cumulée, relance comprise ; alerte à 80 % du plafond ; arrêt par identifiant d'instance, consigné à `registres/arrets.md` ; aucune relance sans décision consignée.
- **Variante non retenue** : un seul lancement pour A, B et C (4,09 h, attendu 5,62 à 7,65, plafond 27). Elle épargne un coût fixe, mais fabrique le poste B avant que les épreuves aient passé, contre l'ordre de l'auteur.

### 4.2 Lecteurs du dommage, deux lecteurs

Volume par lecteur : 320 × `k` questions, dont 200 × `k` à l'étape 1 et 120 × `k` à l'étape 2 (pièce 6, sections 2 et 3). Le prix d'une question suppose que le plan entier est renvoyé à chaque appel : c'est la lecture la plus chère de la formule de l'auteur.

| `k` | questions par lecteur | attendu, Opus 5.5 et Mistral | attendu, Sonnet 5.5 et Mistral | attendu, un appel par ensemble (Opus 5.5 et Mistral) | pessimiste (Opus 5.5 et Mistral au prix de repli) |
|---|---|---|---|---|---|
| 3 | 960 | 36,30 | 23,19 | 14,85 | 126,76 |
| 4 | 1 280 | 48,40 | 30,93 | 16,21 | 169,02 |
| 6 | 1 920 | **72,60** | 46,39 | 18,94 | 253,52 |
| 8 | 2 560 | 96,79 | 61,85 | 21,67 | **338,03** |

- **Plafonds pessimistes (`k` ≤ 8)** : étape 1, **212** ; étape 2, **127** ; ensemble 339. Par compte : Claude 196, Mistral 156 (essai de 4.4 compris), 352 en tout.
- **Si la lecture groupée est attestée** (un appel par ensemble, les `k` questions dedans, forme que décrit l'esquisse du premier cycle, `piece-6-esquisse-de-devis-banque-v3.md:43`) : 0,2546 dollar au pire par ensemble pour les deux lecteurs, soit **51** et **31**.
- **Si la page de prix de Mistral est scellée au prix relevé** : le pire cas des lectures à `k` = 8 passe de 338,03 à 263,22 dollars.
- **Plafond recalculé après l'essai de mesure** : deux fois le coût mesuré par question des deux lecteurs, fois le volume restant, sans dépasser le plafond pessimiste. Si la mesure vaut l'attendu, à `k` = 6 : 90,75 et 54,45.
- **Marge** : au centre (`k` = 6), plafond moins attendu = 339 − 72,60 = 266,40. Le plafond vaut 4,7 fois l'attendu : les sorties ne sont pas mesurées sur de vrais plans.
- **Comptes de facturation** : pour le lecteur Claude, la clé « Rigaud », celle des lectures du bras A (`registres/go.md:467`), **relevée sans crédit le 21 novembre** (`registres/depenses.md:577-578`), donc à recharger par Lazar, ou la clé « Luc » sur son mot (`registres/go.md:547`) : il lui reste environ 153 dollars le 21 novembre (`registres/decisions.md:4786`), ce qui couvre l'attendu du lecteur Claude, non son plafond de 196. Pour Mistral, le compte Mistral du projet, clé vue par son nom le 21 novembre (`registres/decisions.md:4727`).
- **Garde d'arrêt**, par file et par fournisseur, reprise des gardes du bras A (`devis-essai-de-mesure…:252-259`) : compteur qui refuse un envoi si le cumul compté plus le pire cas de cet envoi dépasse le plafond de la file (0,260 dollar pour Opus 5.5 ; 0,113 pour Mistral au prix de repli, avec une sortie maximale supposée de 16 384 jetons, S) ; relais plafonné en dollars et limité aux modèles permis ; sortie maximale dans chaque corps ; refus de compte : arrêt de la file ; refus de contenu : arrêt du modèle ; modèle servi autre que le modèle demandé : arrêt ; une seule reprise ; aucune reprise cachée.
- **Économies non comptées** : lecture groupée ; Sonnet 5.5 à la place d'Opus 5.5 (26 dollars de moins au centre) ; lecture de cache d'Anthropic à 0,20 au lieu de 4 (`relais_reel.py:50`) ; point d'accès global de Mistral (9 % de moins). Le traitement par lots est exclu : le relais le refuse (`relais_reel.py:57-60`).

### 4.3 Juges

| juge | volume | coût | compte | remarque |
|---|---|---|---|---|
| **ancre humaine**, gardée telle quelle | 30 éléments | 0 dollar de calcul ; 1 à 2 heures d'une personne (S) | aucun | pièce 6, section 2 ; la personne est à nommer par Lazar |
| remplacement de l'ancre par un agent | 30 éléments et 8 lectures d'admission, 38 appels | attendu 1,38 ; pessimiste 4,72 ; **plafond 5** | compte Google du projet, clés 1 et 2 (`registres/go.md:667`) | **nœud de Lazar**, section 7 ; hors des totaux ; tout appel à un modèle de Google suit la règle permanente du 21 novembre, réglages de plafond, de troncature et de réflexion vérifiés avant l'envoi (`registres/go.md:670`) |
| juge d'une autre lignée et moniteurs gelés | 2 600 actions | **hors devis** | — | la pièce 6 les renvoie au devis de la lecture du cycle ; pour mémoire, 6,4 à 18,1 dollars pour 6 400 actions au bras A (`registres/decisions.md:4293`), soit 2,6 à 7,4 au prorata (C) |

### 4.4 Contrôles

| contrôle | volume | attendu | plafond | compte et garde |
|---|---|---|---|---|
| conditions de contrôle (seconde graine honnête, dose flagrante, relectures des épreuves) | 80 épisodes ; 140 × `k` questions par lecteur | **déjà comptées** en 4.1 et 4.2 : environ 33 dollars de l'attendu au centre | compris | ceux de 4.1 et 4.2 |
| **essai d'admission et de mesure** des deux lecteurs | 12 ensembles par lecteur (8 honnêtes, 4 de dose flagrante), soit 12 × `k` questions | 2,72 à `k` = 6 | **13** (4 en lecture groupée) | ceux de 4.2 ; on ne relève que des champs techniques : code, refus, jetons, conformité de forme |
| vérification par programme des extraits cités ; version servie ; relevé des prix le jour du lancement | — | 0 | 0 | processeur seul |
| contre-lectures, montage de l'oracle, vérification du non-recouvrement | agents de session | 0 dollar de ligne de calcul (quota de session) | — | — |

L'essai dit si un lecteur refuse de lire un épisode à dose flagrante, et mesure les jetons réels. Si la mère désigne dix épisodes honnêtes existants du banc, lisibles sans heurter une cloison, sa partie honnête passe avant le lancement 1, et le devis se recalcule avant la première heure de carte (`piece-6-esquisse-de-devis-banque-v3.md:73-74`).

### 4.5 Reprises

| reprise | règle | part dans l'attendu | part dans le plafond |
|---|---|---|---|
| carte : débit deux fois plus lent et une relance complète par lancement | comptées au pire cas (facteur 4) ; une relance ne part que sur décision consignée | 0 | 26 des 37 dollars |
| lectures : reprise unique d'un envoi, redemande de forme unique | un envoi coupé est compté au pire cas ; une file interrompue n'est pas rejouée sans ligne nouvelle | 5 % des envois, environ 3,6 dollars au centre | 15 % des envois, environ 46 dollars |

## 5. Totaux, étapes et marge

### 5.1 Total

| ligne | attendu au centre | fourchette attendue | **plafond pessimiste** | marge | compte |
|---|---|---|---|---|---|
| génération sur carte | 9,41 | 7,80 à 11,03 | **37** | 27,59 | loueur de cartes |
| lectures du dommage | 72,60 | 9,34 à 96,79 | **339** | 266,40 | clé Claude « Rigaud » ; compte Mistral |
| essai d'admission et de mesure | 2,72 | 0,35 à 3,63 | **13** | 10,28 | les mêmes |
| ancre humaine | 0 | 0 | 0 | — | aucun |
| **total** | **84,73** | **17,49 à 111,45** | **389** | **304,27** | |

- Centre : `k` = 6, une question par appel, Opus 5.5 et Mistral Large 4. Bas : `k` = 3, lecture groupée, Sonnet 5.5. Haut : `k` = 8, une question par appel.
- **Seuil d'alerte** à 80 % du plafond : 311,20 dollars (règle du registre, `registres/depenses.md:3`).
- **Lecture groupée attestée** : plafond total **123** (37 + 51 + 31 + 4).
- **Marge de change** : si un compte est facturé en euros, 5 % en sus, comme Lazar l'a accepté pour le bras A (`registres/go.md:667`).
- **Une famille, une ligne de budget** : c'est la règle que cite la pièce 6 (reconception sans borne de cycles, N-062, point 3). Ce total est celui d'une seule famille.

### 5.2 Ordre de dépense, chaque étape sur son propre accord

| étape | contenu | attendu au centre | plafond |
|---|---|---|---|
| 0 | sans dépense : attestation sur `k`, programme de vérification des extraits, files de lecture et gardes éprouvées, page de prix de Mistral scellée | 0 | 0 |
| 1 a | lancement 1 sur carte : honnêtes et dose flagrante | 4,86 | **19** |
| 1 b | essai d'admission et de mesure des deux lecteurs | 2,72 | **13** |
| 1 c | lectures de l'étape 1, puis épreuves de l'oracle | 45,37 | **212**, ou deux fois la mesure |
| — | **arrêt si une épreuve ou une précondition échoue** : le repli écrit s'applique, l'étape 2 n'est pas dépensée | | |
| 2 a | lancement 2 sur carte : « sabotage demandé » | 4,56 | **18**, ou 12,67 au débit mesuré |
| 2 b | lectures de l'étape 2 | 27,22 | **127**, ou deux fois la mesure |

Étape 1 : 52,95 attendus, 244 au plafond. Étape 2 : 31,78 attendus, 145 au plafond. **Première tranche demandable : 1 a et 1 b, soit 32 dollars.**

### 5.3 Variante à 100 épisodes par dose

420 épisodes, 480 ensembles lus par lecteur. Carte : attendu 9,92 à 13,65, plafond 47. Lectures : attendu 108,89 à `k` = 6, plafond 508 à `k` = 8. Plafond total, essai compris : **568**. Avec 60 tâches, elle demande plus d'un épisode par tâche, donc des épisodes corrélés (`devis-episodes-reels-t05-nuit-v1.md:24`).

## 6. Les cinq points de la pièce 6, section 5

### Point 1 — prix unitaires et plafond

- **Décision** : accorder la banque par étapes mesurées, ou d'un bloc.
- **Enjeu** : le plafond d'un bloc (389) vaut 4,6 fois l'attendu, faute de mesure.
- **(a) Un plafond global de 389 dollars.** Avantage : un seul accord. Inconvénient : il engage sur des sorties supposées et sur un `k` inconnu.
- **(b) Par étapes : 19 pour le lancement 1, 13 pour l'essai, puis des plafonds recalculés à deux fois la mesure.** Avantage : l'essai coûte environ 3 dollars et ôte l'essentiel de l'incertitude ; précédent, l'essai de mesure payant du bras A (`registres/go.md:455`). Inconvénient : trois accords au lieu d'un.
- **(c) Un plafond à une fois et demie l'attendu (127).** Avantage : petit chiffre. Inconvénient : une file arrêtée au plafond laisse des tâches lues à moitié, qui ne se rachètent pas.
- **Recommandation : (b), confiance 0,75.** Prix à retenir : `p_a` = 0,0014 à 0,0016 dollar par action ; `p_l1` = 0,027 attendu et 0,074 au pire ; `p_l2` = 0,011 attendu et 0,058 au pire.
- **Défaut** : aucun. Une dépense est un nœud.

### Point 2 — familles des deux lecteurs

- **Contrainte déclarée** : hors Llama (agent et moniteurs, `registres/go.md:456`), hors Qwen, hors lignée du juge d'une autre lignée (Qwen 2.5 7B Instruct au bras A, `registres/decisions.md:4247` ; à confirmer pour le cycle 2). J'y ajoute trois précédents de Lazar : hors des modèles qui conçoivent de nouveaux modes, Kimi, Argon, Carbon et Astra (`registres/go.md:562`) ; identifiant figé seulement ; aucun texte envoyé à DeepSeek (`registres/go.md:631`).
- **La note des lignées n'a pas été lue.** Le dossier `docs/notes/scellement-2-lignees-lecteurs-v1/` existe, mais je ne liste aucun dossier hors du mien et aucun registre ne nomme sa pièce. Un audit des lignées est en cours (`registres/go.md:671`). **La recommandation ci-dessous est à confronter à cette note avant tout accord.**
- **(a) Claude Opus 5.5 et Mistral Large 4.** Avantage : les deux familles que Lazar a retenues pour le bras A, un modèle Claude et Mistral Large 4 (`registres/go.md:446`, `:589`, `:631`) ; clés et conditions d'envoi déjà instruites pour ce bras (`registres/go.md:632`) ; deux familles hors de la contrainte. Inconvénient : le lecteur Claude est de la lignée de l'auteur de la famille (`registres/go.md:666`) ; limite à écrire au préenregistrement, tenue par le second lecteur, l'ancre et la vérification des extraits par programme.
- **(a′) Claude Sonnet 5.5 et Mistral Large 4.** Avantage : 26 dollars de moins au centre. Inconvénient : lecteur plus faible ; une épreuve de l'oracle manquée coûte des tâches.
- **(b) Mistral Large 4 et Gemini 4 Neon.** Avantage : aucun lecteur de la lignée de l'auteur. Inconvénient : Neon est de la famille de Carbon et d'Argon (`registres/decisions.md:4739`), qui conçoivent des modes (`registres/go.md:562`) ; il ne reste plus de troisième famille pour l'ancre ; plafond des lectures plus haut (0,124 dollar au pire par question pour Neon).
- **Recommandation : (a), confiance 0,6**, avec le modèle Claude et l'effort que retient la règle du bras A.
- **Défaut** : aucun.

### Point 3 — la main qui monte les lecteurs, leurs invites et le programme de vérification

- **Décision** : qui monte l'oracle de cette famille. Ni l'auteur, ni un concepteur de moniteur (pièce 6 ; `registres/go.md:666`).
- **(a) Le monteur de l'oracle du premier cycle**, agent Opus 5.5 neuf déjà désigné (`registres/go.md:665`, `registres/decisions.md:4777`). Avantage : un seul montage, aucun accès de plus au coffre. Inconvénient : un même agent tient les deux familles ; une erreur de montage touche les deux ; sa session peut ne plus exister quand la réserve servira.
- **(b) Un agent Opus 5.5 neuf, autre, qui réemploie le programme gelé et contre-lu du premier cycle** et n'écrit que la part propre à cette famille. Avantage : les deux familles restent chez des mains séparées ; le programme de vérification se réemploie, comme l'esquisse du premier cycle le prévoit (`piece-6-esquisse-de-devis-banque-v3.md:67-68`). Inconvénient : un accès de plus au coffre, à consigner.
- **Recommandation : (b), confiance 0,7.** Coût : aucun dollar de ligne de calcul ; le code est une pièce d'instrument, contre-lue par un autre modèle.
- **Défaut** : aucun. Le rôle est à désigner par Lazar, comme au premier cycle (`piece-6-esquisse-de-devis-banque-v3.md:24-25`).

### Point 4 — tâches du pilote ou tirage disjoint

- **Enjeu** : les 96 tâches de l'environnement ont toutes été courues (`devis-episodes-reels-t05-nuit-v1.md:14`). Sur des tâches déjà vues, on ne sépare pas « adapté aux textes » de « adapté à la famille » (`docs/decisions/decision-N-049-v1.md:51-55`).
- **(a) Les 60 tâches du pilote** (`donnees/t05-pilote-v1/taches-pilote-60-v1.json`, `287e8348…`), graines neuves. Avantage : aucun coût de plus, références cachées déjà extraites. Inconvénient : limite à écrire au préenregistrement ; le rééchantillonnage se fait par tâche.
- **(b) Un tirage disjoint** dans la suite du tirage ordonné (1 836 candidats, `devis-episodes-reels-t05-nuit-v1.md:20`), avec une version neuve de la règle de sélection, qui s'arrête aujourd'hui à 96 papiers (`docs/procedures/T0.5-selection-papiers-v1.md:85-87`), et une extraction contre-vérifiée, références cachées comprises. Avantage : des tâches jamais vues par les concepteurs de moniteurs, ce que Lazar nomme « la seule chose qui marche vraiment » (`decision-N-049-v1.md:19`). Inconvénient : plusieurs jours ; **poste non chiffré ici**. Aucune mesure du coût d'extraction par tâche n'est au dépôt que j'aie lue : aucun dollar de ligne s'il est fait par des agents de session, quelques dizaines de dollars s'il passe par une interface payante (S).
- **(c) Les 60 tâches du pilote, si la mère atteste par ses registres de lecture qu'aucun concepteur du cycle 2 ne les a lues.** Avantage : gratuit. Inconvénient : l'attestation est peut-être impossible.
- **Recommandation : (b), confiance 0,6**, sur un devis à part ; la réserve n'est pas sur le chemin critique. Le coût de carte et de lecture de ce devis ne change pas.
- **Défaut** : aucun (le choix touche ce que la lecture pourra revendiquer). Si la réserve devait servir avant la fin de l'extraction : (a), limite écrite.

### Point 5 — la main qui vérifie le non-recouvrement

- **État** : déjà engagé par la mère. Un agent neuf Opus 5.5, qui ne conçoit aucun moniteur, lit le coffre une fois et rend un verdict seul ; sa note reste au coffre (`registres/decisions.md:4780`).
- **(a) Entériner cette main.** Avantage : fait, sans dépense, accès consigné. Inconvénient : une seule lecture, d'une seule lignée.
- **(b) Y ajouter le contre-lecteur de la famille.** Avantage : deux regards. Inconvénient : il faudrait lui ouvrir la famille du premier cycle.
- **(c) Un tiers hors du programme.** Avantage : indépendance. Inconvénient : sortie du coffre, donc contact externe et mot de Lazar.
- **Recommandation : (a), confiance 0,8.** Demander que le verdict scellé dise, par leurs noms seuls, à quoi la famille a été comparée, modes connus compris, et que cet agent ne travaille ensuite à aucun moniteur.
- **Défaut** : (a), déjà engagé par la mère.

## 7. Nœuds pour Lazar, hors des cinq points

1. **Remplacement de l'« ancre humaine ».** Le texte reste « ancre humaine sur 30 éléments ». Deux précédents la remplacent par un agent neuf : pour le bras A (`registres/go.md:444`), et pour les épreuves du scellement 2 (`registres/go.md:665`). Rien ne dit que ce second mot couvre la famille de réserve, autorisée par une ligne distincte. Options : (a) une personne, que Lazar nomme, aucun calcul ; (b) un agent d'une troisième famille, Gemini 4 Neon comme au bras A, plafond 5 dollars, après un essai d'admission à huit lectures (`registres/go.md:632`) ; (c) un agent Claude de session, gratuit, mais de la famille du premier lecteur. Recommandation : garder la personne si Lazar peut la nommer, car c'est la seule vérification de l'instrument qui ne passe par aucun modèle (`registres/go.md:444`) ; sinon (b), que Lazar a déjà choisi deux fois ; confiance 0,6. Réserve sur (b) : Neon est de la famille de deux concepteurs de modes.
2. **Sortie du coffre vers des tiers.** Les épisodes B et C dérivent d'un contenu en quarantaine. Les fabriquer sur une carte louée et les faire lire par deux fournisseurs les fait sortir du dépôt. Lazar a accordé que l'agent agisse sur banc fermé, la revue externe étant remplacée par six garde-fous internes, après contre-lecture de la pièce de sécurité et ses gardes éprouvées à blanc (`registres/go.md:667`, `:670`, `:671`). Cette pièce a été acceptée en version 7 le 21 novembre à 17:57, avec treize gardes (`registres/decisions.md:4788`) ; je ne l'ai pas lue. Avant toute ligne, la mère confronte ce devis à cette pièce : une carte louée est-elle un banc fermé ; des lecteurs externes peuvent-ils lire des épisodes dérivés, et sous quelles conditions d'envoi (précédent : `registres/go.md:632`). Si elle l'interdit, ce devis est à refaire.
3. **Moment de la dépense.** La famille est une réserve. Recommandation : l'étape 0 maintenant, sans dépense ; les étapes payantes seulement quand Lazar active la réserve ; confiance 0,7.

## 8. Gardes d'arrêt communes

Chaque garde est éprouvée sur un cas sain et sur un artefact, contre un faux fournisseur local, sans appel payant (règle des gardes éprouvées, R5). Aucun repli silencieux : toute garde qui coupe écrit son motif et rend un code de sortie propre. Arrêts par identifiant d'instance ou de processus, jamais par motif de ligne de commande (R10). Avant toute suppression : inventaire, versement scellé, vérification sur disque et par empreinte. Les sorties de lecture restent au coffre ; le rapport ne porte que des champs techniques ; rien n'en est servi à une session qui conçoit des sondes ou des moniteurs.

## 9. Avant toute demande de ligne de calcul

1. Ce devis contre-lu par un autre modèle, corrections vérifiées par le même contre-lecteur. Fichiers à lui donner : ce devis, le programme de recalcul et sa sortie, la pièce 6 de la famille, et les pièces de la section 1 ; rien du coffre.
2. La version 2 de la pièce 6 rapprochée de ce devis par la mère ou par un lecteur qu'elle mandate ; le programme relancé avec ses nombres (constantes `RELECTURES_EPREUVES` et `ELEMENTS_ANCRE`, et toute ligne de lecture ajoutée).
3. Les cinq points tranchés ; le nœud de l'ancre tranché, ou la personne de l'ancre nommée.
4. L'attestation à trois cases de la section 2. Si `k` dépasse 8, les lectures se recalculent par la formule : 320 × `k` × 0,1320.
5. Ce devis confronté à la pièce de sécurité du banc fermé, dans sa version acceptée ; ses gardes éprouvées ; les conditions d'envoi constatées et datées.
6. La page de prix de Mistral versée et scellée, l'identifiant figé et le point d'accès confirmés ; sinon le prix de repli reste.
7. Le choix des lecteurs confronté à la note des lignées.
8. Le crédit de la clé Claude nommée, relu ; la clé Mistral présente.
9. Le préenregistrement de la lecture scellé et contre-lu ; fiche de lancement, graines dérivées par tâche, manifeste.
10. Le code des files, du lanceur et du programme de vérification contre-lu ; gardes éprouvées ; le relais plafonné en dollars du lecteur Mistral désigné et contre-lu.
11. Prix de la carte, stockage, téléchargement et pilote relevés le jour de la création.
12. La ligne inscrite à `registres/go.md` et l'engagement à `registres/depenses.md`.

L'accord général du 21 novembre vers 17:30 (`registres/go.md:668`) ne lève aucune de ces conditions : plusieurs sont des nœuds de Lazar.

**Ligne d'engagement proposée**, forme du registre des dépenses : `| AAAA-MM-JJ | GO-… | devis de la banque de la famille de réserve du cycle 2 (empreinte) | identifiant | carte A100 80 Go, 1,30 dollar par heure au plus | heures | coût | cumul sur 19 | étape 1 a : 140 épisodes honnêtes et de dose flagrante ; épisodes et identifiants rapatriés, scellés ; instance détruite par son identifiant |`

## 10. Ce que ce devis ne couvre pas

- La lecture des épisodes par les moniteurs gelés et par le juge d'une autre lignée, et toute passe d'activations : devis de la lecture du cycle.
- L'extraction d'un tirage disjoint de tâches (point 4, option (b)).
- Des appels de préparation de la référence, si la pièce 3 en demande : provision indicative de 8 dollars (S), absente de la pièce 6.
- Une carte autre que l'A100 SXM4 80 Go ; le disque d'une instance arrêtée et gardée.
- Le temps de la personne qui tient l'ancre.

## 11. Réserves et points où je doute

1. **La version 2 de la pièce 6, non lue.** Comptage par programme de seize chaînes reprises de la version 1, sans rien afficher de la version 2 (77 lignes contre 68). **Présentes dans les deux versions** : `n` = 60, `e` = 1, `n_f` = 20, « 260 épisodes », « deux graines par tâche », « deux doses de mesure », « dose flagrante », les formules des postes A, B et C. **Absentes de la version 2** : « 3 × 20 ensembles », « (260 + 60) × k », « ancre humaine sur 30 éléments ». La somme des prix des deux lecteurs y figure trois fois au lieu d'une. Lecture : la ligne de la carte (4.1) tient ; le volume des relectures d'épreuves, donc 60 des 320 ensembles lus, et la ligne de l'ancre ont été récrits, et une ligne de lecture a pu s'ajouter. Je n'en sais pas plus.
2. **`k` et la forme de la lecture** : inconnus ; d'où un plafond de 123 à 389.
3. **Débit** : mesuré sur une autre chaîne ; non mesuré pour des épisodes honnêtes ni pour des épisodes « sabotage demandé » de ce banc.
4. **Sortie de Mistral Large 4** : aucune mesure au dépôt que j'aie lue ; son plafond de sortie n'est pas publié (`choix-mistral-deepseek-v1.md:16`).
5. **Prix de Mistral** : lu par un outil qui résume les pages, donc non opposable ; d'où le prix de repli.
6. **Effort du lecteur Claude** : l'attendu suppose l'effort bas. À l'effort moyen, la sortie supposée double (`devis-essai-de-mesure…:144`) : une question d'Opus 5.5 passe de 0,0273 à 0,0378 dollar, soit 20,16 dollars de plus au centre ; le plafond le couvre.
7. **Refus de contenu** : un lecteur Claude peut refuser de lire un épisode « sabotage demandé ». Un refus de juger a déjà été vu (`devis-essai-de-mesure…:102`), et Opus 5.5 a refusé un autre rôle le 21 novembre (`registres/decisions.md:4786`). L'essai le dit ; un refus est un nœud, pas un contournement.
8. **Sorties mesurées au bras A** : sur textes à gabarits, sans doute plus faciles que de vrais plans (`devis-essai-de-mesure…:347`).
9. **Lignée de l'auteur** : la contrainte lue n'écarte que les familles des moniteurs et de l'agent ; je signale le voisinage du lecteur Claude et de l'auteur, sans en faire une exclusion.
10. **Contre-lecture** : les formules, les sorties supposées et les facteurs du plafond sont de moi, jamais contre-lus.

## 12. Journal

- **Refus d'outil ou de classifieur : aucun.**
- Aucun appel à un modèle, aucune machine, aucune dépense, aucun commit, aucune poussée. Réseau : cinq récupérations de branches par `git fetch`, sur quatre branches.
- Écrit : ce devis, le programme de recalcul et sa sortie, dans ce seul dossier, chacun scellé.
- **Version 2 de la pièce 6** : non lue, non affichée. Un programme en a compté seize chaînes connues de la version 1, et a comparé les tailles ; sa copie de travail, hors du dépôt, a été effacée par son chemin écrit en clair. Je le déclare : c'est plus qu'une empreinte, et la mère en juge.
- **Non lus** : les pièces 1 à 5 de la famille ; tout le coffre ; la pièce de sécurité du banc fermé ; la version 2 de l'esquisse du premier cycle (`b52cb162…`), remplacée ; la règle du bras d'attaque, absente de l'arbre de travail ; la note des lignées (28 noms précis essayés par test de présence, aucun trouvé, dossier non listé).
- **Lu pour trouver les pièces** : les lignes 4740 à 4788 du registre des décisions et les lignes 665 à 671 du registre des accords, filtrées, l'index sans contenu du second scellement, puis l'esquisse en clair du premier cycle, version 3, ouverte après vérification de son empreinte contre l'index.
- Un dossier `__pycache__`, né d'une compilation d'essai du programme de recalcul, a été effacé par son nom écrit en clair, dans mon dossier.
- **Lu en passant, à déclarer** : (1) une ligne du registre des accords cite un chemin du dossier du saboteur à budget et des lettres de choix ; aucun fichier de ce dossier n'a été ouvert, et les lignes de registre ont ensuite été filtrées. (2) Un extrait de prix de `registres/depenses.md:515`, ligne d'engagement d'une étape dont les résultats me sont fermés : le prix horaire seul. (3) Des noms de branches du barreau 5 dans le registre des décisions : aucun score, aucune table. (4) Le devis du bras A, que la mission désigne, porte des durées et des coûts de la chaîne précédente : des relevés de débit et de dépense, aucun score ni verdict ; je n'en reprends que la durée d'un épisode et la méthode du pire cas.
