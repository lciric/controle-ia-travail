# Audit des réglages des appels aux modèles de Google, version 1

Écrit le 21 novembre 2026 vers 18:00Z par un auditeur neuf, Claude Opus 5.5 (`claude-opus-5-5`), sur le mot de Lazar inscrit en GO-2026-11-21-71 : « corrige et vérifie tous les réglages plafond troncation limite mots réflexion avant d'envoyer un modèle gemini ; je ne veux plus voir ce genre d'erreur ». Règle de référence : `CLAUDE.md`, sections « Appels à Carbon » (GO-2026-11-21-47) et « Appels aux modèles de Google » (GO-2026-11-21-71, commit `bbb20d37d`). Pièce de travail : audit en lecture seule, aucune correction portée.

Ce que je n'ai pas fait : aucun envoi à un modèle, aucune clé lue, aucun commit, aucun fichier modifié hors cette pièce et son sceau. Rien lu sous `donnees/`, `archives-reponses-modeles/`, `brouillons/ii-b-saboteur-budget-v1/`, ni aucun fichier « consigne-privee » ou « conception-ii-b ». La version 8 du collisionneur v9 (`collisionneur_v9_v8.py`), en cours d'écriture, n'a pas été ouverte ; c'est la version 7 qui est contrôlée.

## 1. Verdict

**Aucune dernière version en service ne satisfait la règle du 21 novembre (GO-2026-11-21-71).** Trois défauts reviennent partout :

1. **Le réglage de réflexion envoyé est un budget (`thinkingBudget`), jamais un niveau (`thinkingLevel`)**, alors que les pages de Google lues par les contre-lecteurs (non versées) et la seule page de modèle versée (Neon) décrivent un réglage par niveaux. Le cas mesuré : Argon, budget 8 192 envoyé par le collisionneur, **zéro jeton de pensée sur 22 réponses réelles sur 22** (contre-lecture de la version 7 par Fable, section 3.1). Deux lanceurs de l'organisme n'envoient même aucun réglage de réflexion (`--sans-config-pensee`).
2. **Zéro jeton de pensée n'est jamais un défaut** : aucun programme ne refuse une réponse sans pensée ; un champ `thoughtsTokenCount` absent est lu comme zéro, sans le dire.
3. **La limite de mots de l'invite n'est contrôlée par code dans aucun programme** face au plafond de texte.

Et aucune garde commune n'existe encore sous `src/controle_ia/` (vérifié : ni fichier nommé pour Google, ni mention de Google dans `gardes.py`), alors que la règle la demande.

Par programme (dernière version de chaque lignée) :

| lignée | dernière version contrôlée | en service | verdict |
|---|---|---|---|
| collisionneur | `docs/notes/collisionneur-v9/collisionneur_v9_v7.py` (`319a7b66…`) | oui | à corriger |
| consultation des modèles externes | `docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/appel_modeles_externes_v6.py` (`e2095843…`) | oui | à corriger |
| commande d'Argon et de Carbon de l'organisme | `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3e.py` (`e94ecd46…`) ; la v3d (`46c91df4…`) est celle que citent les lanceurs | oui (v3d), en réserve (v3e) | à corriger |
| commande par lot de l'organisme | `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py` (`9484dce0…`) | en réserve | à corriger |
| relais Gemini local de l'organisme | `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py` (`543e728d…`) | en réserve | à corriger (un point bloquant pour la correction des autres) |
| lanceur de la course d'auto-conception (réglages passés aux commandes) | `scripts/lancer_course_auto_conception_v10.py` (`f4196ec5…`) | en attente (premier envoi pas avant le 28 novembre) | à corriger |
| épreuve des juges réels, ligne 3, étage 2 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/code-appel-v4/epreuve_juges_reels_ligne_3_v4.py` (`082d19d6…`) | en attente | à corriger |
| épreuve de l'étiqueteur, lecture des items | `docs/notes/epreuve-etiqueteur-v1/lire_items_phase1_v5.py` (`11380cba…`) | non | hors service |
| anciennes lignées et dépôts (section 4.3) | — | non | hors service |

## 2. Ce que dit la documentation versée sur le champ de réflexion, par modèle

Recherche faite dans `docs/` sur « thinkingLevel » et « thinkingBudget », et lecture des pages de Google versées sous `docs/sources/prix/`.

| modèle | champ de réflexion documenté dans une pièce versée | plafond de sortie dans une pièce versée |
|---|---|---|
| Neon (`gemini-4-neon`) | **niveaux** : page du modèle versée `docs/sources/prix/page-modele-gemini-4-neon-20261121T134943Z.html` (`2eadc192…`), ligne 153 : « Supported (low, medium, high, xhigh) ». Aucun budget n'y est écrit. Nom exact du champ dans le corps de `generateContent` : **non établi** par cette page. | 65 536 « (default synchronous) », même page, ligne 53 ; liste des modèles versée `docs/notes/collisionneur-v9/liste-modeles-gemini-20261121T134904Z.json` (`eeec19e8…`), ligne 648 |
| Argon (`gemini-4-argon`) | **non établi** par une page versée. | **32 768** : liste versée, ligne 594 |
| Carbon (`gemini-4-carbon`) | **non établi** par une page versée. | **32 768** : liste versée, ligne 612 |
| Hydrogen (`gemini-4-hydrogen`) | **non établi** ; aucun programme du dépôt ne l'appelle (hors le dossier `gemini/`, qui ne l'appelle pas non plus). | 65 536 : liste versée, ligne 630 |
| Flash (`gemini-2.5-flash`, `gemini-3.x-flash`) | **non établi** ; seuls les fichiers du dossier `gemini/` (hors service, section 4.3) appellent `gemini-2.5-flash`. | 65 536 pour `gemini-2.5-flash` : liste versée |

La page de prix versée (`docs/sources/prix/page-prix-gemini-api-20261121T134918Z.html`, `40202cdd…`) dit seulement que les pensées sont facturées au prix de sortie (lignes 112, 132, 331, 594 : « including thinking tokens »).

Ce qui est lu **hors de toute page versée** (provenance par transcription, non opposable, règle R7) :
- page de la réflexion de Google, `aistudio.google.com/docs/thinking`, lue par trois contre-lecteurs les 20 et 21 novembre, **non versée** (empreinte annoncée `a964d5cf09c7…`, `contre-lecture-collisionneur-v9-v7-fable-v1.md`, section 5.1) : Argon et Carbon se règlent par niveaux (bas, moyen, haut), **moyen par défaut** ; aucun `thinkingBudget` n'y est documenté pour eux ; `maxOutputTokens` compte les pensées et coupe net (`contre-lecture-collisionneur-v9-v4-v1.md`, ligne 45 ; `rapport-developpeur-collisionneur-v9-v4.md`, ligne 55 ; contre-lecture v7 par Fable, section 3.2) ;
- page de Vertex (autre service) : « Setting thinking_budget on Gemini 4 models returns a 400: INVALID_ARGUMENT error » (`contre-lecture-collisionneur-v9-v4-v1.md`, ligne 46) — démenti par les faits pour l'interface du script : Carbon et Argon ont accepté un budget (code 200) ;
- un appel non diffusé (synchrone ou par lot) de Carbon et d'Argon serait plafonné à 32 768 jetons, pensées comprises (contre-lecture v7 par Fable, section 5.3, point 1), ce que confirme la liste versée.

Ce qui est **établi par les journaux versés** (et non par une documentation) : le corps `"thinkingConfig": {"thinkingLevel": "high", "includeThoughts": true}` a été **accepté (code 200)** par Argon et Carbon sur `streamGenerateContent` : `docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/appel-argon-v1.json` (`99539ec5…`, ligne 13 ; fin `STOP`), `…/appel-carbon-v1.json`, `docs/notes/revendication-14-approfondie-v1/appel-carbon-v1.json`, `docs/notes/mathematiques-nouvelles-v1/consultation-externe-v1/appel-argon-v1.json` (`626a56a4…`). Ces journaux ne séparent pas les pensées du texte (`jetons_sortie_et_reflexion` seul) : qu'Argon pense sous « high » n'est donc pas établi. Le niveau « high » sans budget a aussi mangé les 32 000 jetons d'un appel de Carbon avant tout texte (en-tête de la consultation v4, recopié dans la v6, ligne 26).

Conséquence : pour Argon, Carbon et Neon, le champ à envoyer pour « le niveau le plus haut admis » est très probablement `thinkingLevel`, mais ni le nom exact pour chaque modèle, ni le niveau le plus haut admis par Argon et Carbon (« high » ou « xhigh »), ni le cumul avec `thinkingBudget` ne sont établis par une pièce versée. À verser avant toute correction : la page de la réflexion et les pages des modèles d'Argon et de Carbon, puis un envoi d'essai par modèle (sur GO), relevé brut versé.

## 3. Contrôle détaillé des dernières versions

### 3.1 Collisionneur, version 9 révision 7 (`collisionneur_v9_v7.py`, `319a7b66…`)

En service : version prévue pour la reprise des courses des collisionneurs (registres/decisions.md, R-4639 et R-4644 ; contre-lecture de Fable `contre-lecture-collisionneur-v9-v7-fable-v1.md`, `f6342515…`, verdict « conforme hors l'option du repli par lot »). Fichier non suivi par git (exclu par `.git/info/exclude`, ligne 47), empreinte égale à son compagnon `.sha256`.

**Réglage de réflexion envoyé.** Ligne 962 à 966 : `"generationConfig": {"maxOutputTokens": max_tokens, "thinkingConfig": {"thinkingBudget": m["budget"], "includeThoughts": True}}`, le même corps en flux (ligne 976) et en lot (ligne 1042). Valeurs (catalogue, lignes 237 à 249) :

| espèce | `thinkingBudget` envoyé | `maxOutputTokens` (premier envoi, relance) | provision comptée | texte garanti au-delà de la provision |
|---|---|---|---|---|
| Argon | 8 192 (ligne 238) | 32 768, 32 768 | 16 384 | 16 384, **non contrôlé par code** (Argon absent de `REGLE_TEXTE_MIN`, ligne 261) |
| Carbon | 32 768 (`BUDGET_CARBON_V7`, ligne 218) | 65 536, 65 536 | 49 152 (`PROVISION_CARBON_V6`, ligne 195) | 16 384, contrôlé (lignes 606 à 618, 654 à 657 ; et avant le comptage de chaque cellule, lignes 1617 à 1618) |
| Neon | 32 768 (ligne 248) | 65 536, 65 536 | 32 768 | 32 768, contrôlé |

Aucun `thinkingLevel`. Pour Neon, le script cite lui-même la page versée qui ne documente que des niveaux (« Aucun budget de réflexion n'y est documenté », ligne 185) et envoie pourtant un budget ; aucun envoi à Neon n'a été fait (« Réglages SUPPOSÉS », ligne 198). Pour Argon, le budget envoyé ne produit aucune pensée (22 sur 22, journaux relus par Fable, section 3.1). **Écart à la règle** : réglage explicite oui, mais pas « le niveau le plus haut admis » ; le budget est souple (Carbon : jusqu'à 44 101 jetons de pensée sous 32 768, réflexion d'Opus `reflexion-relance-collisionneurs-opus-max-v1.md`, ligne 33).

**Plafond et part de texte.** Contrôle par code à la composition (lignes 649 à 657) : budget entier, positif, au plus la provision ; plafond moins provision ≥ 16 000 pour Carbon et Neon seulement. La règle se vérifie sur la provision, **pas sur le budget envoyé ni sur les pensées réelles** : Google ne connaît que le budget (souple) ; au-delà de 49 536 jetons de pensée chez Carbon, le texte aurait moins de 16 000 jetons (Fable, section 3.1). Le contrôle de la règle nouvelle « plafond ≥ réflexion + 16 000 » tient numériquement pour les trois (Argon 8 192 + 16 000 = 24 192 ≤ 32 768 ; Carbon et Neon 32 768 + 16 000 = 48 768 ≤ 65 536), mais n'est écrit que pour Carbon et Neon. **En lot** (`--repli-lot`, lignes 1032 à 1094) : Carbon reçoit 65 536 alors que la liste versée donne 32 768 (ligne 612) et que l'appel non diffusé serait plafonné à 32 768 pensées comprises : la règle des 16 000 jetons de texte n'y est plus tenue (Fable, section 5.3, point 1).

**Limite de mots face au plafond.** Lignes 366 à 373 (2 500 à 4 000 mots par tour) et ligne 400 (« au plus {mots} mots »). Aucun contrôle par code de la limite de mots contre le plafond de texte ; les mots ne servent qu'au devis (ligne 2123, « borne large »). À 4 000 mots, environ 8 000 jetons en français (rapport supposé de 2 jetons par mot, non mesuré ici) : sous les 16 384 de Carbon, mais rien ne le vérifie.

**Motif de fin et jetons de pensée en retour.** Lignes 1295 à 1296 : `SAFETY`, `PROHIBITED_CONTENT`, `BLOCKLIST`, `SPII`, `RECITATION`, `IMAGE_SAFETY` et le blocage de l'invite donnent `REFUS` (ligne 1327), sans relance (ligne 1684). Ligne 1329 à 1330 : `MAX_TOKENS` donne `TRONQUE` (texte partiel) ou `VIDE` ; chez Carbon et Neon, `VIDE` en `MAX_TOKENS` devient `MAX_TOKENS_SANS_TEXTE`, code 9, sans relance (lignes 1581 à 1582, 1674 à 1678) ; chez Argon, il est relancé au même plafond de 32 768 (`max_relance` = `max`, ligne 238), donc payé deux fois sans changement de réglage. `STOP` sans texte : `VIDE` ; aucun candidat : `VIDE` ; tout autre motif : `ANOMALIE`. Jetons de pensée lus (ligne 1102, `thoughtsTokenCount`) et journalisés (champ `reflexion`) ; **champ absent lu comme 0** (`u.get("thoughtsTokenCount", 0)`), et **zéro pensée jamais refusé** : les 22 réponses d'Argon sans pensée ont été acceptées. Garde de dépense sur la sortie facturée (ligne 1573 à 1575), juste.

**Repli silencieux.** Aucun repli de modèle ni de réglage (ligne 972 : « un refus de ce réglage remonte tel quel (aucun repli) »). Un seul silence : `annuler_lot` (lignes 1022 à 1029) avale l'échec de l'annulation d'un lot (`pass`), le lot restant compté au pire ; Fable relève aussi deux pertes en lot (C-1, C-2).

### 3.2 Consultation des modèles externes, version 6 (`appel_modeles_externes_v6.py`, `e2095843…`)

En service : version courante des consultations d'Argon, de Carbon et de Neon (R-4532, R-4562, R-4579 ; notes servies à Carbon et à Neon, R-4564).

**Réglage de réflexion envoyé.** Ligne 193 : `{"thinkingBudget": reglage["reflexion"], "includeThoughts": True}` ; lignes 194 à 195 : `maxOutputTokens` = réflexion + texte. Défauts (lignes 59 à 60) : Carbon 24 000 + 16 000 ; **Argon 24 000 + 16 000 = 40 000** ; Neon 32 768 + 32 768 = 65 536. Aucun `thinkingLevel` (les versions 1 à 3 essayaient « high » puis se repliaient sur un budget : `revendication-14-approfondie-v1/appel_modeles_externes_v2.py`, ligne 64 ; ce repli a disparu en v4, à juste titre).

**Plafond et part de texte.** Ligne 269 à 270 : texte < 16 000 refusé pour Carbon, Argon et Neon ; plafond = réflexion + texte (ligne 273). Conforme à la règle numériquement, mais **pour Argon le plafond par défaut, 40 000, dépasse la limite de sortie de la liste versée, 32 768** (ligne 594 de la liste) : refus de l'interface ou coupe, non établi ; aucun contrôle contre la limite du modèle. Pas de contrôle des pensées réelles contre le budget (un budget dépassé mange le texte sans être dit avant la fin).

**Limite de mots.** Aucune : l'énoncé est un fichier libre (ligne 40, `ENONCE`) ; aucune lecture de la limite de mots qu'il porte.

**Motif de fin et pensées.** Lignes 245 à 262 : seul `STOP` avec texte et sans erreur dans le flux rend 0 ; `MAX_TOKENS` rend le code 3 (texte partiel écrit à part en `.partiel.md`), avec la mention « défaut de réglage » chez Carbon et Neon sans texte ; `SAFETY`, `RECITATION` et tout autre motif rendent le code d'échec avec le statut brut (non nommés, mais jamais une réponse). Pensées lues ligne 236, **absentes lues comme 0**, et **zéro pensée accepté**. `modele_servi` est écrit mais pas comparé au modèle demandé dans le verdict (lignes 245 à 262).

**Repli silencieux.** Un morceau de flux illisible est journalisé et sauté (lignes 215 à 218) ; la réponse peut alors finir en code 0 avec un texte amputé, sans le dire au verdict.

### 3.3 Commande d'Argon et de Carbon de l'organisme, v3e (`commande_argon_v3e.py`, `e94ecd46…`) et v3d (`46c91df4…`)

La v3e ne diffère de la v3d que par la lecture du modèle demandé (en-tête, lignes 9 à 17). En service : la **v3d** est celle que citent les lanceurs sur `main` (`scripts/lancer_course_auto_conception_v10.py`, lignes 513 à 516 ; `lancer_course_ideation_regard_ou_raisons_v1.py`, `…organismes_discrets_v7.py`, `…bassins_etroits_v3.py`, `…conception_propre_v1.py`, `epreuve_temoins_auto_conception_v9.py`) ; la v3e sert les enveloppes `appel-argon-v6.sh` et `appel-carbon-v1.sh`, absentes de `main`.

**Réglage de réflexion envoyé.** v3e lignes 879 à 881 (v3d lignes 857 à 859) : `config = {"maxOutputTokens": max_sortie}` puis, sauf `--sans-config-pensee`, `config["thinkingConfig"] = {"thinkingBudget": provision}`. Défaut de la provision : 8 192 (v3e ligne 369, v3d ligne 350). Pas d'`includeThoughts`. **L'option `--sans-config-pensee` (v3e lignes 723 à 724) permet d'envoyer sans aucun réglage de réflexion** : contraire à la règle nouvelle, qui exige un réglage explicite dans le corps.

**Plafond et part de texte.** `maxOutputTokens` = min(`--max-sortie-jetons`, défaut 65 536, ligne 367 ; reste du plafond en dollars moins la provision), lignes 866 à 867 ; refus sans envoi (code 4) seulement sous `--sortie-min-jetons`, **défaut 4 096** (ligne 368). Aucun plancher de 16 000 jetons de texte, aucun contrôle « plafond ≥ réflexion + 16 000 ». Le défaut de 65 536 dépasse la limite de 32 768 d'Argon et de Carbon dans la liste versée, en appel synchrone non diffusé. Si les pensées comptent dans `maxOutputTokens` (ce que disent les pages non versées), le texte peut tomber à `maxOutputTokens` − pensées, soit sous 4 096 (l'en-tête le dit, lignes 295 à 296).

**Limite de mots.** Aucune : la consigne vient du noyau par l'entrée standard.

**Motif de fin et pensées.** Lignes 692 à 709 : `MAX_TOKENS` → code 5 (« sortie tronquée ») ; toute fin autre que `STOP` (`SAFETY`, `RECITATION`…) → code 5 (« bloquée ou anormale ») ; texte vide → code 5 ; blocage de l'invite → code 5. Pensées lues (ligne 663, champ facultatif : **absent lu comme 0**) et journalisées (`pensees_jetons`, ligne 986) ; pensées au-delà de la provision → code 7 (lignes 998 à 1003) ; **zéro pensée accepté**.

**Repli silencieux.** Aucun : un refus du réglage de réflexion remonte tel quel (lignes 888 à 895, en clair ligne 890).

### 3.4 Commande par lot de l'organisme, v1 (`commande_gemini_lot_v1.py`, `9484dce0…`)

En réserve : copiée sur `main` le 18 novembre (R-3266), écrite pour la lignée Carbon par lot ; aucune citation récente.

Réglage : ligne 177, `"maxOutputTokens": sortie, "thinkingConfig": {"thinkingBudget": args.provision_pensee_jetons}`, provision 8 192 par défaut (ligne 69). Plafond 32 768 par défaut (ligne 67), plancher de sortie 4 096 (ligne 68) : **aucun plancher de 16 000 jetons de texte** ; pour Carbon, 32 768 − 8 192 = 24 576 si le budget est tenu, mais le budget est souple (Carbon a déjà pensé 32 765 jetons sur une sortie de 32 768 en lot, `lancer_course_auto_conception_v10.py`, ligne 417). Fin : lignes 130 à 133, `STOP` exigé, sinon code 5 (`MAX_TOKENS`, `SAFETY`, `RECITATION` compris) ; texte vide : code 5. Pensées : lues (`thoughtsTokenCount or 0`, absentes lues comme 0), au-delà de la provision : code 7 ; **zéro pensée accepté**. Limite de mots : aucune.

### 3.5 Relais Gemini local, v4 (`relais_gemini_v4.py`, `543e728d…`)

En réserve (même lot de pièces, R-3266). Ce n'est pas un appelant : il transmet. Mais il **fige le réglage par liste blanche** pour le lot : ligne 311, `"thinkingConfig": {"thinkingBudget", "includeThoughts"}` ; ligne 309, `generationConfig` sans autre clé de réflexion. **Un corps de lot qui porterait `thinkingLevel` serait refusé (403)** : toute correction des commandes vers un niveau de réflexion doit corriger d'abord ce relais. Il ne lit ni le motif de fin ni les pensées (journal de l'usage seul).

### 3.6 Lanceur de la course d'auto-conception, v10 (`lancer_course_auto_conception_v10.py`, `f4196ec5…`)

En attente : dernière version de la lignée, base de la course principale d'auto-conception (plan v2, R-4428 : premier dollar pas avant le 28 novembre ; la v10 refuse encore tout moteur réel, en-tête lignes 26 à 30). Il ne parle pas à Google lui-même ; il **exige à l'identique** les réglages passés à la commande v3d :

- Carbon (lignes 414 à 425) : `--provision-pensee-jetons 65536`, `--max-sortie-jetons 65536`, `--sortie-min-jetons 4096`, et le drapeau **`--sans-config-pensee`** (« budget de pensée non fixé (défaut du fournisseur) », ligne 419) ;
- Argon proposeur (lignes 435 à 436) : les mêmes réglages, même drapeau ;
- Argon juge : enveloppe `rapports/fille-ideation-1-v1/appel-argon-v5.sh` (`37c0205e…`), provision par défaut 8 192 sous un plafond de session de 0,60 USD.

Écarts : **aucun réglage de réflexion dans le corps** pour Carbon et Argon proposeur (contraire à la règle) ; Carbon et Argon y reçoivent donc le niveau par défaut de Google, « moyen » selon les pages non versées ; `maxOutputTokens` 65 536 sur un appel synchrone non diffusé, au-delà de la limite de 32 768 de la liste versée ; plancher de texte 4 096 et non 16 000 ; une provision égale au plafond rend la garde « pensées au-delà de la provision » inopérante (la v10 le dit, lignes 420 à 421). Pour Argon juge, au prix de sortie compté de 41,5 USD par million, 0,60 USD paient au plus 14 457 jetons ; moins la provision de 8 192, **la sortie est d'au plus 6 265 jetons**, sous les 16 000 de la règle.

### 3.7 Épreuve des juges réels, ligne 3, étage 2, v4 (`epreuve_juges_reels_ligne_3_v4.py`, `082d19d6…`)

En attente (étage 2 de la ligne 3 ; une pièce de relance est citée en R-4582). Juge Argon par la commande v3d, plafond de session 0,60 USD exigé (lignes 56 à 59, 721 à 726) : même calcul que le juge de la section 3.6, **au plus environ 6 265 jetons de sortie**, provision 8 192 en budget, aucun plancher de 16 000. Les motifs de fin et les pensées sont ceux de la v3d (section 3.3) : zéro pensée accepté.

### 3.8 Épreuve de l'étiqueteur, lecture des items, v5 (`lire_items_phase1_v5.py`, `11380cba…`)

Hors service (exploratoire du 9 novembre, aucune citation récente). Corps repris de la v4 (`lire_items_phase1_v4.py`, `627ebcb7…`, lignes 98 à 99 et 225 à 229) : `"maxOutputTokens": 8000`, `"thinkingConfig": {"thinkingBudget": 8192}`, température 0. **Budget plus grand que le plafond** : si les pensées comptent dans le plafond, le texte peut être nul ; texte au plus 8 000, sous 16 000. Fin : `SAFETY`, `PROHIBITED_CONTENT`, `BLOCKLIST`, `SPII` sans texte → blocage (v5 ligne 168) ; `MAX_TOKENS` → tronquée (ligne 170) ; **`RECITATION` n'est pas dans la liste des blocages** ; pensées lues (`or 0`, ligne 225), zéro accepté. À ne pas relancer sans réécriture.

## 4. Inventaire par lignée

Liste tirée de `git -C /home/user/controle-ia-travail grep -l -E "generativelanguage|generateContent|google\.genai|thinkingConfig|thinkingLevel|thinkingBudget|gemini" -- '*.py'` (228 fichiers) ; les essais, doublures, sondes de contre-lecture et calculs de devis ne sont pas contrôlés (ils n'envoient rien) ; les fichiers qui ne nomment Google que dans un texte ou une liste de motifs (`scripts/depot_expurge_v11.py` et précédents, `src/controle_ia/garde_refus_question_v2.py`, `docs/procedures/crible-v-v1/lanceur_crible_v_v2.py`, le mandataire de règles `mandataire_regles_v1.py`) n'appellent pas Google.

### 4.1 Lignées en service ou en réserve

| lignée | versions | dernière |
|---|---|---|
| collisionneur | `collisionneur-memoire-encodage-v1/…/collisionneur_v2.py` (trois copies), `organisme-boucle-reelle-v1/collisionneur-v7/collisionneur_v7.py`, `ideation-organisme-v1/course-2/collisionneur-v8/collisionneur_v8.py`, `collisionneur-experimentateur-v1/script-v1/collisionneur_v8_plafonds_bas_v1.py`, `collisionneur-v9/collisionneur_v9_v1.py` à `_v7.py` | v9 v7 (la v8, en écriture, non lue) |
| consultation des modèles externes | `revendication-14-approfondie-v1/appel_modeles_externes_v1.py`, `_v2.py` ; `papier-dopamine-moniteur-v1/approfondissement-v1/appel_modeles_externes_v3.py` à `_v6.py` | v6 |
| commande d'Argon de l'organisme | `lancement-v1/commande_argon_v1.py`, `lancement-v2/commande_argon_v2.py`, `argon-recherche-v1/commande_argon_v3.py`, `_v3b` à `_v3e` | v3e (v3d en service) |
| commande par lot | `argon-recherche-v1/commande_gemini_lot_v1.py` | v1 |
| relais Gemini local | `lancement-v2/relais_gemini_v1.py`, `argon-recherche-v1/relais_gemini_v2.py` à `_v4.py` | v4 |
| lanceurs qui passent les réglages d'Argon et de Carbon | `scripts/lancer_course_auto_conception_v9.py`, `_v10.py`, `scripts/epreuve_temoins_auto_conception_v9.py`, lanceurs des courses d'idéation (organismes discrets v1 à v7, bassins étroits v1 à v3, pilier d'attaque v2 en trois versions, conception propre v1, regard ou raisons v1, bras du juge v1) | auto-conception v10 contrôlé ; les lanceurs d'idéation passent par la v3d avec ses défauts (section 3.3) |
| épreuve des juges réels, ligne 3 | `code-appel-v1` à `code-appel-v4` | v4 |

### 4.2 Lignées hors service (non contrôlées en détail)

| lignée | dernière | ce qui suffit à la dire non conforme |
|---|---|---|
| épreuve de l'étiqueteur | `lire_items_phase1_v5.py` | section 3.8 |
| épreuve fraîche du pont | `docs/notes/epreuve-fraiche-pont-v1/lancer_epreuve_pont_v2.py` | appelle Argon par le collisionneur v7, `max_tokens` 12 000 (ligne 92) ; le collisionneur v7 n'envoie **aucun réglage de réflexion** (`collisionneur_v7.py`, ligne 428 : `"generationConfig": {"maxOutputTokens": max_tokens}`) |
| commandes du tour fermé | `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_argon_v56_nuit_v6.py` (et ses copies sous `organisme-boucle-reelle-v1/`) | même appel du collisionneur v7, sans réglage de réflexion ; lecteur de test à 1 000 jetons de sortie |
| consultation à part des bassins étroits | `docs/notes/collisionneur-bassins-etroits-v1/consultation_a_part_v1.py` | Argon à 24 000 jetons par le collisionneur v8 « plafonds bas » (ligne 41), qui n'envoie aucun réglage de réflexion (ligne 454 de celui-ci) ; invite « au plus 5 000 mots » (ligne 49) |
| contre-lecture de l'affinage de l'équipe rouge | `docs/notes/affinage-equipe-rouge-v2/appeler_argon_v2.py` | appelle la fonction d'appel d'un collisionneur ancien passé en argument, sans réglage de réflexion |
| dossier `gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/` (trois programmes) | — | dépôt d'une autre lignée (registres/decisions.md, R-333, R-340) : clé dans l'adresse (`?key=`), aucun réglage de réflexion, plafond 8 192, **bascule de modèle en boucle** (`gemini-argon`, puis `gemini-2.5-pro`, puis `gemini-2.5-flash` : `run_quadruple_fusee_omega_alpha_gamma_beta.py`, ligne 298), contraire à « aucun changement de modèle sans GO ». À ne jamais lancer. |

## 5. Écarts à la règle du 21 novembre, programme par programme

Les cinq contrôles de la règle (`CLAUDE.md`, « Appels aux modèles de Google ») : (a) réglage de réflexion explicite, au niveau le plus haut admis ou au budget prévu ; (b) plafond ≥ réflexion + 16 000 ; (c) limite de mots de l'invite dans le plafond de texte ; (d) après la réponse, zéro pensée, `MAX_TOKENS`, `SAFETY`, `RECITATION` ou texte vide = défaut journalisé ; (e) garde commune ou reproduite, essais et mutations à l'appui.

| programme | (a) | (b) | (c) | (d) | (e) |
|---|---|---|---|---|---|
| collisionneur v9 v7 | budget explicite, pas de niveau ; Argon sans pensée | oui en flux (contrôlé pour Carbon et Neon, pas pour Argon) ; non en lot pour Carbon | non contrôlé | zéro pensée accepté ; le reste oui | non |
| consultation v6 | budget explicite, pas de niveau | oui (contrôlé) ; Argon au-delà de sa limite de sortie | non contrôlé | zéro pensée accepté ; le reste oui | non |
| commande d'Argon v3d et v3e | budget, ou rien avec `--sans-config-pensee` | non (plancher 4 096) | non | zéro pensée accepté ; le reste oui | non |
| commande par lot v1 | budget | non (plancher 4 096) | non | zéro pensée accepté ; le reste oui | non |
| relais Gemini v4 | bloque `thinkingLevel` en lot | — | — | — | — |
| lanceur d'auto-conception v10 | **rien** pour Carbon et Argon proposeur | non (65 536 au-delà de la limite ; plancher 4 096 ; juge au plus 6 265) | non | ceux de la v3d | non |
| épreuve des juges, ligne 3, v4 | budget 8 192 | non (au plus 6 265) | non | ceux de la v3d | non |

## 6. Ce qui reste à faire avant tout envoi à Google (recommandation, non portée)

1. **Verser** la page de la réflexion de Google et les pages des modèles d'Argon et de Carbon (et de Hydrogen si on l'emploie), puis **un envoi d'essai par modèle** (sur GO, quelques centimes) avec `thinkingLevel` au niveau le plus haut admis, `includeThoughts`, relevé brut versé : nom exact du champ, niveaux admis, cumul ou refus avec `thinkingBudget`, pensées produites. Tant que ce n'est pas fait, le champ exact par modèle reste « non établi ».
2. **Écrire la garde commune** sous `src/controle_ia/` (nom versionné), appelée par chaque programme avant l'envoi et après la réponse : réglage explicite, plafond ≥ réflexion prévue + 16 000 (et ≤ limite de sortie de la liste versée pour le mode d'appel), limite de mots × rapport mesuré de jetons par mot ≤ part de texte, refus de zéro pensée et de pensées absentes, refus nommé de `MAX_TOKENS`, `SAFETY`, `RECITATION`, `PROHIBITED_CONTENT`, `BLOCKLIST`, `SPII`, texte vide ; essais et mutations.
3. **Retirer `--sans-config-pensee`** des commandes v3d et v3e (ou le refuser), et des réglages exigés par le lanceur d'auto-conception v10.
4. **Corriger le relais v4** pour admettre le champ de niveau, avant de corriger les commandes qui passent par lui.
5. **Ramener les plafonds aux limites versées** : 32 768 pour Argon et Carbon en appel non diffusé (consultation v6 pour Argon, commande v3d et v3e, lot, collisionneur en `--repli-lot`), et en tirer le niveau ou le budget qui laisse 16 000 jetons de texte.
6. **Juges à 0,60 USD** (épreuve de la ligne 3, juge de l'auto-conception) : le plafond de session ne laisse pas 16 000 jetons de texte au prix compté ; décision de Lazar (relever le plafond du juge ou déroger à la règle par écrit).
7. Dans le collisionneur v9 (version 8 en écriture) : ajouter Argon à la règle du plafond large, refuser zéro pensée, ne plus relancer Argon au même plafond après une réponse vide en `MAX_TOKENS`.

Sceau : `audit-reglages-google-v1.md.sha256`, dans ce dossier.
