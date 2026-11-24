# Devis : course « atelier » de l'organisme d'idéation (option (a)), question fusionnée neutre, protocole X version 2, étage des tests de mort existant — v1

- **Classe A (devis).** Rédigé par Opus 5.5 (sous-agent de la session du service à l'organisme), le 24 novembre 2026 vers 19:00Z, **en écart à la règle « Fable écrit les devis »** : le quota de Fable est gelé jusqu'au 2 décembre (R-5297). **À contre-lire** (§ 10) avant tout envoi à Lazar. Rien n'a été lancé : aucun appel de modèle, aucune machine, aucun commit.
- **Fondement** : mot de Lazar « go organisme avec banc expérimentateurs et tests de mort » (GO-2026-11-24-42, « toute dépense de course sur devis et ligne propre ») ; protocole X version 2 (`origin/main:docs/notes/protocole-x-v2/protocole-x-v2.md`, GO-2026-11-24-43 et -44 : « Service à l'organisme d'idéation : toutes les règles ») ; modèle de l'expérimentateur (GO-2026-11-21-47, point 3 ; GO-2026-11-22-116, point 1) ; clé Claude Luc (GO-2026-11-22-45) ; clé gratuite de Google pour Carbon et Neon (R-5294).
- **Chiffres** : tous recalculés par `calcul_devis_option_a_v1.py` (même dossier), sortie `calcul_devis_option_a_v1.txt`, rejouée deux fois à l'octet. Le programme relit chaque source, en donne la ligne et l'empreinte (sa section 1), et s'arrête si une sous-chaîne citée manque. Dans ce texte, « illustratif » veut dire qu'aucune mesure ne fonde la valeur. Tout montant est en dollars américains.

## Ligne à verser au livre de coût du protocole X

Pour `registres/livre-cout-protocole-x-v1.md` (règle 7), versée par la mère, sous la forme du livre :

| dossier | lancé (UTC) | version du protocole | reformulateur | ligne d'accord | compté | payé au pire | payé réel | clés | note de sortie |
|---|---|---|---|---|---|---|---|---|---|
| service à l'organisme d'idéation (collisionneur groupé, attelage du plan Turing, questions ouvertes), option (a) « atelier », deux bras et étage des tests de mort | non lancé (devis v1 du 2026-11-24) | 2 | Opus 5.5, écart déclaré (règle 8 ; Fable gelé jusqu'au 2 décembre, R-5297) | à ouvrir (GO-2026-11-24-42 : « sur devis et ligne propre ») | 1 044,13 brut, toutes relances comprises (483,76 sans relance) | 255 tenu par les plafonds des relais (746,66 brut) | — | RR_ANTHROPIC_API_KEY_LUC, GEMINI_API_KEY_FREE (Carbon), GEMINI_API_KEY (Argon), OPENAI_API_KEY (Astra), HCLOUD_TOKEN (machine) | à venir |

## 0. Verdict

1. **Coût**, avec le bras témoin, base recommandée (un seul juge a priori) : **attendu 118,65** (payé 81,16) ; **haut 227,42** (payé 184,48) ; **pire compté 1 044,13** (brut, toutes relances permises, clé gratuite comptée au tarif payant) ; **pire payé 746,66 brut**, **tenu à 251,76 par les plafonds des relais**. **Plafond d'arrêt recommandé : 255** (somme des plafonds par clé). Sans le bras témoin : attendu 66,27 (payé 47,16), haut 142,62 (payé 120,75), plafond 170.
2. **Machine** : conteneur de session pour l'organisme, la lecture double et les contrôles (comme la course v9, sans machine louée) ; un serveur Hetzner cpx32 (hel1) pour l'étage des tests de mort seul (vrai bac à sable, comme la course v67), location bornée par code à 24 heures, attendu 0,73, pire 1,76.
3. **Le lanceur v9 ne sait pas servir une question neuve sans réécriture lourde.** Il refuse de repartir (« une seule course » : la v9 est close), il épingle la matière, les consignes, les témoins, le préenregistrement et la clé Minuit, et ses réglages de Carbon et d'Argon sont refusés par la garde commune de Google (§ 8). L'adaptateur de clé n'a donc pas été écrit ; le chemin minimal est décrit au § 8.
4. **L'étage des tests de mort « à forme imposée, comme à la v67 » ne reçoit pas ces propositions telles quelles.** Sa forme imposée est une loi prédictive d'une grammaire fermée, éprouvée par le gain de log-score sur les épisodes d'un monde planté (`tour_ferme_v64.py`, `texte_du_test`, l. 452). Les propositions d'une question ouverte n'entrent dans cette forme qu'à travers un traducteur ou un pont, que la conception décrit et qui n'est pas codé (conception, § 2.4 ; lots C2, C3, E2). Le poste de l'étage sur les propositions est donc chiffré, mais il reste conditionnel. La mesure de l'expérimentateur sur les sept témoins du tour fermé, elle, est faisable avec le code existant.

## 1. Ce qui est servi, et à qui

- **Dossier servi** : faits 10 700 caractères et question 15 000 caractères (mandat), plus quatre questions témoins de 1 600 caractères au total (illustratif). La consigne du proposeur est comptée à la taille de la consigne v2 de l'auto-conception, 28 173 caractères, une borne, puisque la neuve n'est pas écrite. Entrée d'un proposeur : 53 873 caractères, plus les témoins.
- **Cas** : sept, un par point prioritaire de la demande reformulée (§ « Ce qu'on te demande », points 1 à 7). C'est une proposition. Chaque cas sert le dossier entier avec son point mis en avant. Deux cartes par appel (configuration v5, l. 58), soit 10 cartes par cas et **70 cartes par bras**.
- **Bras témoin** (règle 5) : même fond, question posée autrement, même composition, même nombre de cas.
- **Étage** : 20 propositions et 4 contrôles cachés (constructions déjà réfutées), soit 24 fiches, en deux étages de 12 au plus (`tests_de_mort_v2.py`, l. 132). Les quatre contrôles cachés de la demande reformulée (point 1.5) sont la supermartingale écrêtée, la correction statique α − k/(n+1), la boule de variation totale et le test de la corde. Ce sont des propositions : le choix revient à un agent qui ne sert pas l'organisme.

## 2. Rôles, modèles, réglages, appels

| rôle | modèle (identifiant) | réglage | clé (par son nom) | appels, avec le bras témoin | source du réglage |
|---|---|---|---|---|---|
| proposeur | `claude-opus-5-5` | sortie 64 000 | RR_ANTHROPIC_API_KEY_LUC | 14 | `collisionneur_v9_v8m.py` l. 389 |
| proposeur | `claude-fable-5-1` | sortie 49 000 | idem | 14 | même fichier, l. 338 |
| proposeur | `gemini-4-argon` | flux, `thinkingLevel` « high », `includeThoughts`, sortie 65 536, réflexion comptée 16 384 | GEMINI_API_KEY (payante) | 14 | même fichier, l. 392 ; garde, l. 73 |
| proposeur | `gpt-6-astra` | `max_completion_tokens` 32 768 | OPENAI_API_KEY | 14 | `commande_astra_v1.py` l. 71 ; déclaration v9 |
| proposeur | `gemini-4-carbon` | flux, « high », `includeThoughts`, sortie 65 536, réflexion comptée 49 152 (texte 16 384 ≥ 16 000) | GEMINI_API_KEY_FREE | 14 | `collisionneur_v9_v8m.py` l. 325 |
| critique (deux familles), une par cas, sur les dix cartes du cas | Opus 5.5 ; Carbon | idem | Luc ; gratuite | 14 + 14 | relevé, tour E3-T2 |
| aiguilleur | Opus 5.5 | plafond de session 0,25 | Luc | 140 | configuration v5, l. 117 |
| juge a priori, **sans effet sur la sélection** | Opus 5.5 (un seul juge, base) | plafond de session 0,60 | Luc | 140 | configuration v5, l. 118 |
| lecteur aveugle (règle 3), un appel par cas, puis une synthèse | Opus 5.5 ; Carbon | idem | Luc ; gratuite | 16 + 16 | relevé, tour E3-T3 |
| sonde du jour (format, garde) | Carbon ; Argon ; Astra | idem | gratuite ; payante ; OpenAI | 1 + 1 + 1 | devis v2i, l. 19 (Astra) |
| expérimentateur (mesure sur les sept témoins du tour fermé) | `claude-sonnet-5-5` | plafond 0,80 par fiche | Luc | 7 fiches | `tour_ferme_v64.py` l. 150 et l. 496 |
| expérimentateur en repli mesuré, mêmes témoins | Opus 5.5 | plafond proposé 1,60 par fiche (douze tours au tarif d'Opus) | Luc | 7 fiches | même fichier, l. 51 (12 × 0,06) |
| lecteur témoin de l'étage, autre lignée | Argon | flux, « high », sortie 32 768, réflexion comptée 16 384, limite de 1 500 mots | GEMINI_API_KEY | 14 + 24 | garde, l. 73 à 80 |
| expérimentateur sur les propositions et les contrôles cachés | Sonnet 5.5 (pire compté au plafond d'Opus, pour couvrir le repli) | 0,80 ou 1,60 par fiche | Luc | 24 fiches | — |
| machine de l'étage | Hetzner cpx32 hel1 | 24 heures au plus, bornées par code | HCLOUD_TOKEN | 1 location | `registres/depenses.md` l. 423, 428 |

- **Variante non retenue** : le second juge de la configuration v5 (Argon). Au réglage conforme à la garde, il coûte au pire 1,00 par carte, au lieu des 0,60 du plafond de session. Il ajoute 30,11 attendus, 83,83 au haut et 281,24 au pire compté, et porte le plafond à 370. Il est sans effet sur la sélection, d'où l'exclusion. Le plafond de session du juge passerait de 0,60 à 1,00.
- **Neon** n'est pas compté : la configuration v56 n'a pas cette espèce, et la règle 6 du protocole X (« une voix par fournisseur ») ne lui donne aucune voix de plus.

## 3. Jetons par appel, et d'où ils viennent

- **Attendu** : entrée = caractères / caractères par jeton médian ; sortie = sortie médiane du relevé des journaux réels du collisionneur (`docs/notes/service-collisionneur-modes-v8-v1/calculs/releve-journaux-v2.json`, `52cd710f…`). Les analogues sont le tour E3-T1 pour les proposeurs, E3-T2 pour les critiques et E3-T3 pour les lecteurs. Fable 5.1 est lu sur le relevé de Fable 5.2 (illustratif).
- **Haut** : caractères par jeton minimal et sortie au 90e centile du même relevé.
- **Pire d'un appel** : entrée gardée à la borne prudente du lanceur v9, octets / 2 (`lancer_course_auto_conception_v9.py` l. 368 ; 1,0408 octet par caractère, mesuré sur la demande reformulée). On y ajoute, au prix de sortie, **le plafond de sortie et la réflexion comptée** : c'est la convention du collisionneur (`collisionneur_v9_v8m.py` l. 2090). Pour Astra, on prend la formule de sa commande (`commande_astra_v1.py` l. 133).
- **Aiguilleur et juge** : attendu par appel du devis v1 (0,031 et 0,037 ; lanceur v9, l. 520) ; haut par appel du devis v2i, rapporté au nombre d'appels (20,46 / 110 et 47,322 / 220 ; devis v2i l. 14 et 15 ; devis v2 l. 18) ; pire au plafond de session.
- **Expérimentateur** : attendu 0,081 par fiche, relevé de la course v67 (conception l. 33). Le relais Kimi y servait l'expérimentateur, au même tarif que Sonnet (2 et 10). Opus est compté au double (illustratif). Haut 0,72 : douze tours à 0,06 (`tour_ferme_v64.py` l. 51). Pire : le plafond par fiche.
- **Lecteur témoin de l'étage** : 0,061 relevé à la v67, sous un réglage borné à 0,10 que la garde de Google refuse désormais. Il est compté comme le juge (0,2151 attendu, illustratif), et au pire à 1,00 par fiche au réglage conforme.

## 4. Tarifs (USD par million de jetons, entrée et sortie)

| modèle | tarif | source |
|---|---|---|
| Opus 5.5 | 4 et 20 | `docs/sources/prix/page-prix-anthropic-docs-20261122T104128Z.md` l. 23 |
| Fable 5.1 | 10 et 50 | même page, l. 19 |
| Sonnet 5.5 | 2 et 10 | même page, l. 31 ; barème du relais Claude épinglé, `pole/relais_reel.py` l. 51 |
| Carbon, Argon | 4 et 20 **à partir du 1er décembre** (2 et 10 jusqu'au 30 novembre), comptés au prix haut | `page-prix-gemini-api-20261122T104129Z.html` l. 156, 163 (Carbon) et 375, 382 (Argon) |
| Astra | 10 et 50 | `commande_astra_v1.py` l. 69 et 70 (prix-astra-v2) |
| Hetzner cpx32 | 0,05875 EUR TTC par heure entamée (0,235 pour 4 heures), 1,25 USD par EUR | `registres/depenses.md` l. 428 et 422 |

**La clé gratuite** suit la pratique du protocole X (R-5338 ; livre de coût, ligne du collisionneur groupé). Elle est comptée au tarif payant dans le « compté », à zéro dans le « payé », et tout appel facturé sur elle arrête la course. Réserve : la page versée dit « Gemini 4 Carbon is not available on the Free tier » (l. 140). Que la clé « gratuite » ne soit pas facturée est un fait de compte, et ce devis ne le vérifie pas.

## 5. Postes (sortie du calcul, § 3 et § 5)

| poste | attendu (payé) | haut (payé) | pire compté | pire payé |
|---|---|---|---|---|
| proposition, bras principal | 23,87 (18,72) | 28,00 (22,35) | 146,84 | 113,15 |
| **questions témoins** (règle 2), bras principal : surcoût d'entrée (1 600 caractères) et de sortie (1 000 jetons attendus, 2 000 au haut ; illustratif) ; le plafond de sortie ne bouge pas, le pire n'ajoute que l'entrée | 1,24 (1,09) | 2,37 (2,07) | 0,49 | 0,44 |
| critiques, bras principal | 10,76 (4,03) | 12,55 (4,73) | 72,55 | 20,50 |
| aiguillage, bras principal | 2,17 | 13,02 | 35,00 | 35,00 |
| juge a priori (Opus), bras principal | 2,59 | 15,06 | 84,00 | 84,00 |
| **lecture double à l'aveugle** (règle 3), bras principal : Opus et Carbon, chacun lit toutes les sorties | 11,75 (5,41) | 13,80 (6,50) | 82,69 | 23,34 |
| **contrôles par programme** (règle 4) : processeur seul, aucun appel | 0 | 0 | 0 | 0 |
| **bras témoin** (règle 5) : les six lignes ci-dessus, à l'identique | 52,38 (34,01) | 84,80 (63,73) | 421,57 | 276,44 |
| sondes du jour | 1,33 (0,60) | 1,51 (0,70) | 12,54 | 5,31 |
| étage : mesure sur les sept témoins (Sonnet, Opus en repli, lecteur Argon) | 4,71 | 23,50 | 61,71 | 61,71 |
| étage : 24 fiches (propositions et contrôles cachés) | 7,11 | 31,64 | 124,99 | 124,99 |
| étage : machine louée | 0,73 | 1,17 | 1,76 | 1,76 |
| **total** | **118,65 (81,16)** | **227,42 (184,48)** | **1 044,13** | **746,66** |

- **Relances comptées dans le pire.** Une relance après panne technique est permise pour tout appel (GO-2026-11-22-77). Les appels de Google joués hors de l'orchestrateur (critiques et lecteurs de Carbon, sondes) en ont deux, une identique puis une finale (convention du collisionneur, `calcul_devis_collisionneur_groupe_v1.py` l. 103). Sans aucune relance : pire compté 483,76, pire payé 373,36.
- **Par clé** (pire payé brut ; plafond proposé) : Luc, attendu 59,00, haut 144,17, pire 551,85, **plafond 195** ; Google payante (Argon), 16,63, 33,07, 130,66, **plafond 45** ; OpenAI (Astra), 4,80, 6,06, 62,38, **plafond 10** ; clé gratuite de Google, 37,49 comptés au haut 42,94, payé 0, **arrêt au premier appel facturé** ; Hetzner, 0,73, 1,17, 1,76, **plafond 5**. La clé Luc a une recharge automatique (GO-2026-11-22-45) : son plafond est celui du relais, non un solde.

## 6. Plafond d'arrêt, seuils internes, bras témoin

- **Plafond d'arrêt recommandé : 255** (payé). C'est la somme des plafonds par clé, chacun fixé au haut payé de sa clé plus un tiers, arrondi aux 5 supérieurs, et tenu par son relais (porte de plafond pour Claude ; `--plafond-usd` pour Astra ; part du relais d'Argon). Le pire payé tenu par ces plafonds vaut 251,76 ≤ 255. La ligne de GO doit porter ce montant exactement, comme à la v9.
- **Bras témoin (règle 5).** Le payé au pire **brut** avec le bras témoin, 746,66, **ne tient pas** sous 255 : il faudrait un plafond de **750** pour le couvrir (calcul, § 6). Le payé au pire **tenu par les plafonds** reste sous 255 par construction. Dans le pire cas, c'est un plafond qui coupe une étape (« non mesurée, budget »), jamais un dépassement. Sans le bras témoin, le plafond serait de 170. Recommandation : garder le bras témoin sous 255, confiance 0,6. Une étape coupée dans un seul bras porte alors la marque « fragile » et ne vaut pas résultat (« une panne technique n'est pas un résultat »).
- **Seuils internes** (plafond dur par étape, payé, au haut plus un tiers) : proposition et questions témoins des deux bras, **108** ; critiques, **13** ; aiguillage et juge, **75** ; lecture double, **18** ; sondes, **1** ; étage, mesure sur les témoins, **32** ; étage, 24 fiches, **43** ; machine, **2**. L'ordre suit la règle d'A1 de la v9 : une étape n'est lancée que si le cumul payé avant elle laisse son plafond dur sous le plafond d'arrêt. À relire avec la vraie classe `BudgetV56` au lanceur neuf (non fait ici).
- **Arrêts** : tout appel facturé sur la clé gratuite arrête la course ; tout appel de Google refusé par la garde avant l'envoi, ou rendu sans pensée, en MAX_TOKENS, SAFETY, RECITATION ou vide, est un défaut journalisé et jamais une réponse.

## 7. Machine

- **Organisme, critiques, lecture, contrôles** : le conteneur de session, comme la course v9 (R-3800), relais sur la boucle locale, clés lues par leur nom.
- **Étage des tests de mort** : serveur loué, comme à la v67 (`registres/depenses.md` l. 428 : Hetzner 175834755, cpx32 hel1, 3 h 18 min, environ 0,235 EUR TTC). Le bac `bwrap` exige un lanceur en superutilisateur et une identité dédiée (garde 22 du lanceur v67). La machine jetable ne porte **ni clé ni vérité** : relais et clés restent chez la mère (conception, § 3.2 ; erratum 1, § 1). Durée attendue d'environ 10 heures (14 tests en 3 h 18 à la v67, pour 38 fiches ici, illustratif) ; location **bornée par code à 24 heures**, sous la durée d'étage de 72 heures du tour fermé (`tour_ferme_v64.py` l. 158).
- **Remparts d'arrêt** : identifiant du serveur écrit au registre dès la création ; arrêt et destruction **par cet identifiant** seul (R10), jamais par motif ; minuteur indépendant de la course (par exemple un rappel de la mère à 20 et 24 heures) qui détruit par identifiant ; inventaire et versement scellé avant destruction (R-3661) ; contrôle à chaque reprise (routine R14, étape 4).

## 8. Le lanceur v9 et la clé : pourquoi aucun adaptateur, et le chemin minimal

**Ce qui bloque, constaté sur le code** :
- **La clé est figée.** `CLE_CLAUDE_TENTATIVE = "RR_ANTHROPIC_API_KEY_MINUIT"` (l. 449), exigée à l'identique dans la pièce de départ (l. 1186), avec le mot « Clé Minuit » (l. 1189). Le lanceur ne lit jamais la valeur de la clé : seulement sa présence (l. 2583). Ce sont les relais qui la lisent par son nom (déclaration v9 : `"nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT"`).
- **Une seule course.** La v9 est lancée et close : `verifier_course_jamais_lancee_ou_closes_admises` refuse toute tentative dont le suffixe v9 est déjà au dépôt (l. 905 à 947 : « tentative v9 déjà lancée »). Changer la clé ne suffit donc pas : le lanceur v9 ne repart pas.
- **La matière et les pièces sont épinglées.** Matière v3 et sa règle de découpage par familles du catalogue (l. 715 à 815) ; consignes, témoins du juge, préenregistrement, additif v2i et contre-lecture épinglés par empreinte (l. 343 à 575) ; épreuve des témoins du jour exigée (l. 1739).
- **Google.** L'enveloppe de Carbon et celle d'Argon passent par `commande_argon_v3d.py` (`generateContent` non diffusé ; `--sans-config-pensee` ou `thinkingBudget` ; sortie 65 536). La garde commune les refuse (calcul, § 7 : « thinkingLevel absent », « 65536 au-delà de la limite de carbon en non_diffuse (32768) »). Ces réglages sont antérieurs à la règle du 21 novembre (GO-2026-11-21-71).
- **Rôles absents.** La course 2 v56 n'a ni critique, ni lecteur aveugle, ni question témoin. L'étage des tests de mort n'est pas dans la course v9.

**Chemin minimal (estimations de lignes, à confirmer)** :
1. **Lanceur neuf** (`scripts/lancer_course_atelier_question_v1.py`), copie de la v9 (2 944 lignes), avec environ 700 à 800 lignes touchées :
   - constantes et épingles, environ 60 lignes ;
   - clé lue dans la pièce de départ par son nom, défaut `RR_ANTHROPIC_API_KEY_LUC`, environ 15 lignes ;
   - découpage remplacé par « sept cas du dossier », environ 100 lignes retirées et 50 écrites ;
   - contrôle des réglages de Google réécrit sur la garde v3, environ 420 lignes retirées et 120 écrites ;
   - suffixe neuf pour « une seule course », environ 20 lignes ;
   - épreuve des témoins du juge retirée ou réécrite (le juge est sans effet), environ 70 lignes ;
   - Sonnet ajouté aux modèles permis du relais Claude (déjà dans son barème, `relais_reel.py` l. 51), 1 ligne.
2. **Commande de Google conforme** : soit une `commande_argon_v3e.py` (sur 1 070 lignes, environ 80 à 120 touchées : flux, `thinkingLevel`, `includeThoughts`, lecture des pensées, plafonds), soit l'appel du collisionneur v8m enveloppé en commande externe, environ 150 lignes. S'y ajoutent les enveloppes de Carbon (clé `GEMINI_API_KEY_FREE`) et d'Argon (`GEMINI_API_KEY`).
3. **Configuration v6** de l'orchestrateur (environ 250 lignes JSON, depuis la v5) : champs de fiche au gabarit de la demande reformulée, juge unique, S17 255, plafonds de session.
4. **Textes** : consignes du proposeur, de l'aiguilleur, du juge a priori, de la critique et du lecteur aveugle ; questions témoins ; préenregistrement court ou additif, contre-lu ; pièce de départ ; déclaration des relais.
5. **Hors de l'orchestrateur** : critiques, lecture double, notation des questions témoins (exactitude, score de Brier) et contrôles par programme, par un pilote d'environ 200 lignes sur le collisionneur v8m (clé Anthropic lue par `--cle-anthropic NOM`, garde v3 déjà branchée).
6. **Étage** : la mesure de Sonnet sur les sept témoins passe par le lanceur du tour fermé ou de la boucle v67, avec son texte scellé neuf et l'expérimentateur changé dans la configuration. **Les propositions** exigent un pont vers une forme fixe (conception, lots C2, C3 et E2, de l'ordre de 6 à 9 heures de code, sous hypothèse, plus leurs textes), ou une décision de passer en forme libre. C'est le chemin critique, avant toute dépense de ce poste.

## 9. Points incertains

1. **Étage sur les propositions** (§ 0, point 4) : poste chiffré, faisabilité non établie. Sans pont, seuls la mesure sur les témoins (61,71 au pire) et les contrôles cachés réécrits en forme imposée sont jouables.
2. **Clé gratuite** : payé 0 sur une page qui dit Carbon absent du palier gratuit (l. 140) ; arrêt au premier appel facturé.
3. **Argon** reste sur la clé payante : R-5294 ne nomme que Carbon et Neon. L'étendre à Argon est un mot de Lazar ; le payé tomberait alors d'environ 45.
4. **Tailles illustratives** : consigne neuve (bornée par la v2), carte de 6 000 caractères, consignes de la critique et du lecteur, questions témoins, liste d'un lecteur. Le relevé vient du collisionneur, non de l'organisme. Fable 5.1 est lu sur Fable 5.2.
5. **Lecteur témoin d'Argon** : au réglage conforme, une fiche peut coûter 1,00 au lieu de 0,10. Le plafond du lecteur de l'étage doit monter, sinon l'étage refuse d'envoyer. Autre voie : un lecteur d'une autre lignée sans garde Google (Astra), ou Carbon sur la clé gratuite. À trancher.
6. **Seuils** : la règle d'A1 n'est pas rejouée par la vraie classe `BudgetV56` sur ces étapes (critiques et lecture ne sont pas des étapes de la v56).
7. **Sept cas, deux cartes par appel** : choix de ce devis. Le nombre borné de propositions se règle par `--cases`.
8. **Tarifs de Google** : comptés au prix du 1er décembre. Avant cette date, le payé d'Argon serait de moitié.
9. **Durée de l'étage** : mise à l'échelle d'une seule course (v67), avec un autre modèle expérimentateur.
10. **Modèle d'Astra** : `gpt-6-astra`, celui de la déclaration v9. Le collisionneur sert `gpt-6.2-astra`, au même tarif supposé.
11. **Pièces lues sur la branche de l'organisme** (`origin/lot/compte-organisme-v1`), par `git show` : devis v2 et v2i, configuration v5, consigne v2. Aucune carte, aucun score, aucun verdict ni sortie de course n'a été ouvert. Un accès au verdict de la v67 a été refusé par l'outil, et il n'a pas été contourné : le relevé de la v67 est pris dans la conception (l. 33) et le registre des dépenses.

## 10. Pour la contre-lecture (par un Sonnet neuf)

- **Fichiers à lire** : ce devis ; `calcul_devis_option_a_v1.py` et sa sortie `.txt` ; les sources de la section 1 de la sortie, à la ligne citée ; `scripts/lancer_course_auto_conception_v9.py` (l. 368, 449, 520, 905 à 947, 1186) ; `src/controle_ia/garde_google_v3.py` ; `origin/main:docs/notes/protocole-x-v2/protocole-x-v2.md` ; `origin/main:registres/livre-cout-protocole-x-v1.md` ; la conception des tests de mort et ses errata 1 et 2.
- **À vérifier** :
  - rejouer le calcul (`PYTHONDONTWRITEBYTECODE=1 python3 -I …/calcul_devis_option_a_v1.py`) et comparer la sortie à l'octet ;
  - chaque chiffre du devis contre la sortie ;
  - chaque ligne citée contre son fichier ;
  - la convention du pire (plafond plus réflexion comptée, relances) et le payé à zéro de la clé gratuite ;
  - qu'aucun poste ne manque (sonde, épreuve, machine, relances) ;
  - que le refus du lanceur v9 est bien établi par les lignes citées ;
  - les variantes (`--juge-argon`, `--cases`, `--question-car`).
- **À ne pas ouvrir** : cartes, sorties de course, coffres, scores, verdicts.
