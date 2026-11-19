# Organismes discrets, bras A (déplacement des contrôles appris sans consigne) — estimation préalable du coût des lectures par modèles de langue — v1

- **Objet** : la pièce que demande le bloquant B-1 de la contre-lecture du brouillon 4 (`contre-lecture-preenregistrement-v2-brouillon4-v1.md`, `166b8aeb…`, lignes 20 à 36) : une fourchette, avant scellement, pour que Lazar choisisse (1) le modèle de la famille Claude qui lit, (2) si le juge d'une autre lignée lit 2 560 ou 6 400 actions. **Ce n'est pas le devis** : aucune dépense n'est engagée ni demandée ; le devis d'après scellement chiffre les seules options retenues et porte les plafonds.
- **Auteur** : agent neuf (Claude Fable 5.2), le 2026-11-19, 08:20 UTC (`date -u`). N'a écrit ni le préenregistrement, ni ses contre-lectures, ni les devis de carte.
- **Interdits tenus** : aucun appel payant ; aucun interne de moniteur ouvert (ni `bases/`, ni `sondes/`, ni `t07*/`, ni T0.8, ni la base « mots et coût », ni `prereg/T0.6-organismes-v0-v1.md` : ses chiffres sont repris du devis de carte qui les cite) ; aucune fiche de l'organisme d'idéation ; aucune réponse de juge dans `runs/` (manifestes seulement) ; la référence cachée des tâches n'est pas ouverte ; aucune clé ; rien d'envoyé à l'extérieur que trois adresses publiques de pages de prix ; aucun fichier existant modifié ; rien committé ni scellé.
- **Trois lettres dans les tableaux** : **M** = mesuré ou relevé sur une pièce ; **C** = calculé ici à partir de pièces ; **S** = supposé, sans mesure.

## 0. En une page

1. **Les deux lecteurs coûtent des centaines de dollars, pas des dizaines**, et bien plus que la carte (≈ 16,5 heures à 1,38 dollar au plus, soit ≈ 23 dollars, selon les durées de la section 6.11 du texte). Avec Opus 5.5 et Carbon : **≈ 600 dollars attendus** sans la révision de la consigne, ≈ 690 avec, ≈ 2 000 si la réflexion des modèles est trois fois plus longue que supposé.
2. **Le poste qui décide est la sortie, réflexion comprise, et elle n'est mesurée nulle part pour ces lectures.** Carbon, au prix du 1er décembre, pèse à lui seul ≈ 380 dollars attendus sur l'hypothèse de 1 000 à 1 500 jetons de réflexion par lecture ; ≈ 96 si sa réflexion est bornée très bas. Le budget de réflexion de Carbon est donc le premier levier de coût, avant le choix du modèle Claude.
3. **Choix du modèle Claude** (coût attendu du seul lecteur Claude, sans révision) : Haiku 5.5 ≈ 5 dollars ; Sonnet 5.5 ≈ 105 ; Opus 5.5 ≈ 210 ; Fable 5.2 ≈ 420. **Recommandation : Opus 5.5**, confiance moyenne (section 6).
4. **La variante « GPT et Carbon lecteurs » coûte ≈ 350 dollars de plus** qu'Opus 5.5 et Carbon (≈ 940 contre ≈ 595) : le mot de Lazar « gpt coute cher » tient sur les prix relevés. Le juge des ancres par GPT coûte ≈ 3 à 6 dollars attendus.
5. **Juge d'une autre lignée, 2 560 ou 6 400 actions** : l'écart est de ≈ 0,6 à 4,6 heures de carte, soit **≈ 1 à 6 dollars** (≈ 12 si le juge est deux fois plus lent que l'agent). **Recommandation : 6 400**, confiance assez haute.
6. **Deux réglages du texte ne sont pas servis tels quels par les modèles Claude courants** (section 5) : la température 0 et un budget de réflexion en jetons. À régler avant de remplir la case « lecteurs et juge des ancres ».

## 1. Pièces lues, avec empreintes (sha256, calculées à la lecture)

| pièce | empreinte | usage |
|---|---|---|
| `prereg/T0.7-organismes-discrets-v-a-v2-brouillon4.md` | `16187b78b376…` | sections 3.2 à 3.4, 6.3, 6.5, 6.6, 6.8, 6.10, 6.11 : appels, consignes, majorants |
| `docs/notes/relance-organismes-discrets-v1/choix-de-lazar-deux-lecteurs-v2.md` | `563aab94f7c0…` | lecteurs, juge des ancres, mots de Lazar |
| `docs/notes/relance-organismes-discrets-v1/contre-lecture-preenregistrement-v2-brouillon4-v1.md` | `166b8aeb811c…` | bloquant B-1 |
| `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md` | `83240ca61d7c…` | débits de la carte (section 2), prix de la carte (section 3), lectures (section 6) |
| `docs/notes/bras-a-contre-lecture-habilitee-v1/familles-moniteurs-agent-bras-a-v1.md` | `1753a9d9…` (empreinte citée par le texte, non recalculée) | famille du juge d'une autre lignée (Qwen), de l'agent (Llama) |
| `rapports/organismes-discrets-v1/enveloppes-v1/appel-astra-juge-6-2-v1.sh` | `82d028016cf0…` | prix de `gpt-6.2-astra`, lignes 13 à 16 et 25 |
| `rapports/organismes-discrets-v1/enveloppes-v1/appel-carbon-v3.sh` | `9ef03f804bc1…` | bornes de prix de `gemini-4-carbon`, lignes 10 à 12 et 24 ; budget de réflexion 8 192 |
| `docs/sources/tarifs-openai-v2/developers-openai-com-api-docs-pricing-2026-11-18.html` | `35a048294e2f…` | page d'OpenAI versée et scellée le 18 novembre |
| `docs/notes/ideation-organisme-v1/orchestrateur-v52b/pole/relais_reel.py` | `1b90b020287e…` | barème Claude codé, lignes 47 à 55 |
| quatre manifestes `runs/bras-juge-ideation-organismes-discrets-v4/…-argon`, `…-carbon`, `-v5/…-astra`, `-v6/…-astra`, fichier `copies/sortie--manifeste-bras-rapporte.json` | `61992bc59b09…`, `aaac4130aed0…`, `ad15458bf6cb…`, `c8e89b43328a…` | coûts observés d'un appel de juge et d'un appel de contrôle |
| `registres/depenses.md` (registre vivant) | — | lignes 389, 392, 409 à 411, 503, 505, 506, 517, 521 |
| `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md` | — | entrées OD-016, OD-020, OD-023, OD-024 (réflexion de Carbon) |

La ligne GO-2026-11-19-13 n'est pas dans `registres/go.md` de cette branche (418 lignes) ; elle est citée d'après la transcription `563aab94…` et la contre-lecture.

## 2. Tarifs (dollars par million de jetons, appels synchrones, sans remise de lot : le texte interdit le traitement par lots, section 3.4)

| modèle | entrée | sortie (réflexion comprise) | source au dépôt | page publique lue le 2026-11-19 |
|---|---|---|---|---|
| Claude Fable 5.2 (`claude-fable-5-2`), le plus capable | 8 | 40 | aucune (le barème du dépôt ne porte que Fable 5.1, à 10 et 50) | `https://platform.claude.com/docs/en/about-claude/pricing` : 8 et 40 |
| Claude Opus 5.5 (`claude-opus-5-5`), l'intermédiaire haut | 4 | 20 | `relais_reel.py`, ligne 50 (barème lu le 27 octobre) | même page : 4 et 20 |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`), l'intermédiaire | 2 | 10 | `relais_reel.py`, ligne 51 | même page : 2 et 10 |
| Claude Haiku 5.5 (`claude-haiku-5-5`), le petit | 0,10 | 0,50 | `relais_reel.py`, ligne 52 | même page : 0,10 et 0,50 (entrées de 100 000 jetons au plus : toujours le cas ici) |
| `gemini-4-carbon` | **2 jusqu'au 30 novembre 2026 ; 4 à partir du 1er décembre** | **10 puis 20** | bornes hautes 8,3 et 41,5 (`appel-carbon-v3.sh`, lignes 10 à 12 et 24 ; la même enveloppe cite « 2 / 10 jusqu'au 30 novembre », lecture non empreintée) | `https://aistudio.google.com/docs/pricing` (adresse vers laquelle renvoie `https://ai.google.dev/gemini-api/docs/pricing`) : mêmes valeurs, mêmes dates |
| `gpt-6.2-astra` | 8 | 40 | `appel-astra-juge-6-2-v1.sh`, lignes 13 à 16 ; page scellée du 18 novembre (`35a04829…`) | `https://developers.openai.com/api/docs/pricing` : 8 et 40 |

**Réserves sur les tarifs.**
- Les trois pages publiques ont été lues par un outil qui en rend un résumé ; **aucune n'est versée ni scellée par moi**. La page de Google du dépôt (`docs/sources/prix/page-prix-gemini-api-20261108T054611Z.html`, `ad2140dd…`) ne nomme pas Carbon. Le devis doit verser et sceller les trois pages.
- **Les lectures tomberont après le 30 novembre** (scellement, devis, première ligne de carte avant le premier lot) : le prix de Carbon retenu ici est **4 et 20**. Les colonnes « jusqu'au 30 novembre » et « borne du dépôt » sont données pour mémoire.
- Lectures de cache, remises de lot et palier lent d'OpenAI : non comptés (bornes hautes ; le lot est interdit).
- **Qui paie** : les appels Claude du programme ont été imputés jusqu'ici à des crédits Claude (`registres/depenses.md`, lignes 409 à 411), Carbon et GPT à des comptes facturés. Les dollars de la colonne Claude ne sortent peut-être pas de la même poche : à dire par Lazar.

## 3. Appels et jetons

### 3.1 Appels par rôle (texte, sections 6.5, 6.8 et 6.11 ; C)

| rôle | lot | appels par lecteur, au plus |
|---|---|---|
| lecteur de l'appariement (une action par appel) | épreuves : lot honnête 896, lot des jumeaux 1 280 | 2 176 |
| | lot décisif : 8 960 actions, 576 sentinelles et relues | 9 536 |
| | **total** | **11 712** |
| | révision bornée de la consigne (tâches gardées) | + 2 176 |
| lecteur de la couverture (un plan par appel) | épreuves : 64 + 128 + 128 | 320 |
| | lot décisif : 896 plans, 32 relus | 928 |
| | **total** | **1 248** |
| **les deux instruments, par lecteur** | sans révision (11 712 + 1 248) | **12 960** |
| | avec révision | **15 136** |
| juge des ancres (`gpt-6.2-astra`) | 72 items à la forme de l'appariement, 8 plans | 80 ; + 72 sous la révision : **152** |
| épreuve de forme | un appel par modèle et par instrument | 6 en tout, négligé |

Vérification : 25 920 lectures pour deux lecteurs sans révision, 4 352 de plus avec, 152 pour les ancres : ce sont les chiffres du tableau de 6.11. Le majorant vrai du texte (chaque appel envoyé au plus trois fois) multiplie tout par trois.

Les comptes sont des maximums : ils supposent dix actions jugeables par épisode. La part réelle d'actions jugeables n'est pas mesurée (S) ; elle ne peut que baisser le coût.

### 3.2 Jetons d'entrée par appel

| grandeur | valeur | statut |
|---|---|---|
| consigne de l'appariement | 2 700 caractères, 430 mots (bloc de la section 3.2, marques comprises) | M (compté par programme sur le brouillon 4) |
| consigne de la couverture | 3 550 caractères, 579 mots (bloc de la section 3.3) | M |
| conversion en jetons | 600 à 850 jetons pour l'appariement, 790 à 1 110 pour la couverture (3,2 à 4,5 caractères par jeton, selon le modèle) | S : **aucun comptage de jetons n'a été fait** (il demande un appel au fournisseur) |
| longueur d'une action | 223 jetons en moyenne, coupe à 400 | M, mais d'une autre chaîne et au découpage du modèle de l'agent (devis de carte, section 2, qui cite le préenregistrement de l'organisme précédent, ligne 645) |
| référence d'une tâche | 3 à 6 contrôles ; 100 à 600 jetons | S (référence cachée, non ouverte) |

| entrée par appel | bas | attendu | haut |
|---|---|---|---|
| appariement (consigne + trois champs de l'action) | 750 | 950 | 1 390 (action à la coupe, découpage plus fin d'un tiers) |
| couverture (consigne + dix actions + référence) | 2 900 | 3 650 | 7 110 |

Par lecteur, sans révision (C) : **≈ 15,7 millions de jetons d'entrée attendus** (12,4 en bas ; 28,2 en haut avec la révision).

### 3.3 Jetons de sortie par appel, réflexion comprise — **le poste supposé**

La réponse visible est courte : un objet à quatre clés et deux extraits de 24 à 300 caractères pour l'appariement (≈ 120 à 200 jetons, S) ; un objet à 3 à 6 entrées avec un extrait chacune pour la couverture (≈ 350 à 650 jetons, S). **La réflexion du modèle est facturée au prix de sortie et domine.** Ce que le dépôt en sait :

| fait | source | statut |
|---|---|---|
| Carbon, budget de réflexion 8 192, question triviale : 844 jetons de réflexion | journal de la relance, OD-023 ; `registres/depenses.md`, ligne 505 | M |
| Carbon, sortie bornée à 2 048, entrée de 2 414 jetons : 612 jetons rendus, 0 de réflexion, 13 s | journal, OD-024 ; dépenses, ligne 506 | M |
| Carbon, budget 1 024, question triviale : réponse en 4,5 s | journal, OD-020 ; dépenses, ligne 503 | M |
| Carbon, budget 8 192, appel synchrone sur une grande consigne : muet au-delà de 300 s, connexion coupée | journal, OD-016 et OD-020 | M |
| Carbon, appel de contrôle (consigne de 41 caractères, réponse « OK ») : 0,0034 dollar au barème 8,3 et 41,5, soit ≈ 80 jetons de sortie | manifeste `aaac4130…`, clé `journal/controle` | M pour le coût, C pour les jetons |
| Carbon juge (consigne de 72 416 caractères) : 0,603 dollar, soit ≈ 11 000 jetons de sortie | même manifeste, clé `journal/appels` | M, C |
| `gpt-6.2-astra` juge (consigne de 65 457 caractères) : 0,290 dollar à 8 et 40, soit ≈ 4 000 jetons de sortie ; appel de contrôle : 0,0003 dollar | manifeste `ad15458b…` | M, C |
| lecteurs Claude sur une tâche de lecture voisine : aucun compteur de jetons relevé par appel | `registres/depenses.md`, lignes 409 à 411 (coûts globaux seulement) | non relevé |

Ces manifestes donnent des dollars, pas des compteurs de jetons : les jetons sont déduits des prix (C).

Hypothèses retenues (S, toutes) :

| sortie par appel, réflexion comprise | bas (réflexion nulle ou bornée très bas) | attendu | haut plausible (trois fois l'attendu) | pire cas (sortie maximale à chaque appel) |
|---|---|---|---|---|
| lecteur Claude, effort bas : appariement / couverture | 120 / 350 | 500 / 1 200 | 1 500 / 3 600 | 10 000 / 10 000 |
| Carbon : appariement / couverture | 150 / 450 | 1 150 / 1 950 | 3 450 / 5 850 | 10 000 / 10 000 |
| GPT-6.2 Astra : appariement / couverture | 150 / 450 | 750 / 1 650 | 2 250 / 4 950 | 10 000 / 10 000 |

La sortie maximale de 10 000 jetons est **supposée** (budget de réflexion de 8 192 et la réponse) ; c'est un réglage à fixer. Le pire cas lui est proportionnel : à 3 000 jetons (budget de 2 048), il est divisé par plus de trois. Par lecteur, sans révision, la sortie attendue fait ≈ 7,4 millions de jetons pour Claude, ≈ 15,9 pour Carbon, ≈ 10,8 pour GPT (C sur S).

## 4. Coûts

Formule, pour tout lecteur de prix d'entrée `pe` et de sortie `ps` (dollars par million) :
`coût = [ N_a × (e_a × pe + s_a × ps) + N_c × (e_c × pe + s_c × ps) ] ÷ 1 000 000`, avec `N_a` = 11 712 (13 888 sous la révision), `N_c` = 1 248, `e` et `s` les jetons d'entrée et de sortie par appel de 3.2 et 3.3. Le « haut plausible » ajoute la révision, les entrées hautes, la sortie triple et 10 % de redemandes. Le « pire cas » prend la révision, les entrées hautes et la sortie maximale à chaque appel, envoyé une fois ; le majorant vrai du texte vaut trois fois ce pire cas.

### 4.1 Par lecteur (dollars ; C sur S)

| lecteur | bas, sans révision | **attendu, sans révision** | attendu, avec révision | haut plausible, avec révision | pire cas, avec révision | dont épreuves seules, attendu (avec révision) |
|---|---|---|---|---|---|---|
| Claude Fable 5.2 | 173 | **420** | 480 | 1 362 | 6 280 | 85 (145) |
| Claude Opus 5.5 | 86 | **210** | 240 | 681 | 3 140 | 42 (72) |
| Claude Sonnet 5.5 | 43 | **105** | 120 | 341 | 1 570 | 21 (36) |
| Claude Haiku 5.5 | 2 | **5** | 6 | 17 | 78 | 1 (2) |
| Carbon, prix dès le 1er décembre (4 et 20) | 96 | **381** | 439 | 1 339 | 3 140 | 76 (134) |
| Carbon, prix jusqu'au 30 novembre (2 et 10), pour mémoire | 48 | 190 | 220 | 669 | 1 570 | 38 (67) |
| Carbon, bornes du dépôt (8,3 et 41,5), pour mémoire | 199 | 790 | 911 | 2 778 | 6 515 | 157 (278) |
| GPT-6.2 Astra, s'il lisait | 192 | **559** | 641 | 1 895 | 6 280 | 112 (194) |

**Juge des ancres** (`gpt-6.2-astra`, 80 appels, 152 sous la révision) : ≈ 3,5 dollars attendus, ≈ 6 avec la révision, ≈ 18 en haut plausible, ≈ 63 au pire cas à 10 000 jetons de sortie maximale. **Attention** : l'enveloppe actuelle d'Astra porte une sortie maximale de 32 768 jetons (`appel-astra-juge-6-2-v1.sh`, ligne 26) ; gardée telle quelle, le pire cas des ancres monte à ≈ 208 dollars.

### 4.2 Tableau final — combinaisons, juge des ancres compris (dollars ; prix de Carbon du 1er décembre)

| lecteurs | **attendu, sans révision** | attendu, avec révision | haut plausible, avec révision | pire cas, avec révision |
|---|---|---|---|---|
| Claude Fable 5.2 et Carbon | **804** | 925 | 2 719 | 9 483 |
| **Claude Opus 5.5 et Carbon** | **594** | 685 | 2 038 | 6 343 |
| Claude Sonnet 5.5 et Carbon | **489** | 565 | 1 698 | 4 773 |
| Claude Haiku 5.5 et Carbon | **389** | 451 | 1 374 | 3 281 |
| GPT-6.2 Astra et Carbon (mot 2 de Lazar, pour comparaison) | **943** | 1 086 | 3 252 | 9 483 |

Mêmes combinaisons si toutes les lectures de Carbon tombaient avant le 1er décembre (improbable) : 613, 404, 299, 199 et 753 dollars attendus sans révision. Aux bornes hautes du dépôt pour Carbon : 1 213, 1 003, 898, 799 et 1 353.

**Lecture du tableau.**
- Passer d'Opus 5.5 à Sonnet 5.5 économise ≈ 105 dollars attendus (≈ 18 % du total) ; à Haiku 5.5, ≈ 205.
- Remplacer le lecteur Claude par GPT coûte ≈ 350 dollars de plus qu'Opus 5.5.
- Carbon pèse ≈ 380 dollars dans chaque ligne, sur une hypothèse de réflexion non mesurée. Borner sa réflexion très bas ramènerait sa part vers ≈ 100 dollars.
- Le pire cas n'est pas une prévision : c'est ce que permettrait une sortie maximale de 10 000 jetons servie pleine à chaque appel. Il dit seulement que **le plafond de chaque lot devra être tenu par un relais qui compte**, comme pour les courses de l'organisme d'idéation.

### 4.3 Juge d'une autre lignée : 2 560 ou 6 400 actions (heures de carte)

Le juge est un modèle local de la famille Qwen, qui lit une action en contexte (liste des familles, ligne 15). **Je n'ai ouvert ni sa consigne, ni sa taille, ni son code : son débit n'est pas relevé.** Repères de la même carte (A100 SXM4 80 Go), tous d'une autre chaîne et du modèle de l'agent (devis de carte, section 2) : contexte 2 643 jetons et action 223 ; un épisode de dix actions en 42,8 s, soit 4,28 s par action écrite ; une passe de lecture seule de 4 319 jetons en 0,45 s. Le devis de carte compte ≈ 7 millions de jetons d'entrée pour 2 560 lectures, soit ≈ 17,5 millions pour 6 400.

| hypothèse de durée par lecture (S) | 2 560 lectures | 6 400 lectures | écart | écart en dollars (1,30 à 1,38 par heure, devis de carte, section 3) |
|---|---|---|---|---|
| lecture seule et verdict très court : 0,6 s | 0,43 h | 1,07 h | 0,64 h | ≈ 0,9 |
| une lecture vaut une action écrite par l'agent : 4,28 s | 3,04 h | 7,61 h | 4,57 h | ≈ 5,9 à 6,3 |
| juge deux fois plus lent que l'agent : 8,56 s | 6,09 h | 15,22 h | 9,13 h | ≈ 11,9 à 12,6 |

La mise en route (≈ 1 heure, descente d'un second modèle) est la même dans les deux cas. **Écart retenu : ≈ 1 à 6 dollars, ≈ 12 au plus sous ces hypothèses.** Le moniteur boîte noire par action (6 400 lectures, famille de l'agent) lit de toute façon toutes les actions des cinq conditions.

## 5. Ce que l'estimation fait voir, hors coût (à régler avant de remplir la case « lecteurs et juge des ancres »)

1. **Température 0** (texte, section 3.4, « Réglages »). La documentation d'Anthropic livrée avec l'outil de cette session (en cache au 2026-11-03) dit que les paramètres d'échantillonnage sont refusés par Fable 5.2 et Opus 5.5, et que toute valeur autre que la valeur par défaut l'est par Sonnet 5.5 et Haiku 5.5. **Non vérifié par un appel.** Si c'est exact, le réglage « température 0 » ne peut pas s'écrire pour le lecteur Claude, et la stabilité (honnêtes relues contre lot honnête) se joue sans lui.
2. **Budget de réflexion en jetons.** La même documentation dit qu'un budget en jetons est refusé par ces quatre modèles : la profondeur se règle par un niveau d'effort ; la réflexion ne se coupe pas sur Fable 5.2 ni sur Opus 5.5, elle se coupe ou se réduit sur Sonnet 5.5 et Haiku 5.5. La case « budget de réflexion (une valeur par modèle) » devrait porter, pour Claude, un niveau d'effort.
3. **Carbon en appel synchrone.** Le texte interdit le lot ; au budget de 8 192, Carbon est resté muet plus de 300 s en appel synchrone sur une grande consigne, et la lignée Carbon de l'organisme d'idéation est passée par le lot pour cela. Sur des entrées de 1 000 à 4 000 jetons, il a répondu en 4,5 à 46 s. Un budget de réflexion borné (1 024 ou 2 048) pour Carbon réduit à la fois ce risque et le coût ; l'épreuve de forme le dira.
4. **Durée.** 12 960 appels synchrones par lecteur : à 5 à 15 s l'appel, 18 à 54 heures en file simple. Le degré de parallélisme et les limites de débit des trois comptes ne sont pas relevés.

## 6. Recommandation

**(1) Lecteur de la famille Claude : Opus 5.5.** Confiance moyenne (≈ 65 %).
- Il coûte ≈ 105 dollars attendus de plus que Sonnet 5.5 et ≈ 210 de moins que Fable 5.2, dans un total que Carbon domine de toute façon.
- **Le coût d'un lecteur trop faible n'est pas en dollars.** S'il échoue aux épreuves, la dépense des épreuves est faite (pour Opus 5.5 et Carbon : ≈ 120 dollars sans la révision, ≈ 205 avec), la première ligne de carte aussi, et surtout **les tâches d'épreuve sont lues** : le texte ne permet qu'une révision de la consigne, sur les huit tâches gardées ; après elle le bras s'arrête, et tout remplacement de lecteur exige un texte neuf et des tâches jamais lues, que le bras n'a pas (section 6.6). La tâche demande un jugement fin (les contrôles répondent-ils à cette proposition) et des extraits recopiés caractère pour caractère, vérifiés par programme, avec un accord entre lecteurs d'au moins 0,60.
- Le programme a déjà retenu Opus 5.5 comme lecteur après une sonde de refus (ligne GO-2026-11-09-03 de `registres/go.md` ; dépenses, lignes 409 à 411). Fable a déjà arrêté une course par un refus de juger (dépenses, ligne 250, version 5.1) : pour un lecteur qui doit rendre 12 960 verdicts, c'est un risque que rien ne justifie de payer deux fois plus cher.
- **Réserve honnête** : aucune mesure du dépôt ne compare Sonnet 5.5 ou Haiku 5.5 à Opus 5.5 sur cette lecture. « Sonnet échouerait » est une supposition, pas un fait.
- **Ce qui ferait changer** : si Lazar veut le plancher de dépense et accepte le risque sur les tâches d'épreuve, Sonnet 5.5 (≈ 490 dollars au lieu de ≈ 595) ; si l'épreuve de forme montre qu'Opus 5.5 réfléchit plus de ≈ 1 500 jetons par lecture à l'effort le plus bas, Sonnet 5.5 ; si les crédits Claude ne coûtent rien à Lazar, la question du modèle Claude ne se joue plus sur le prix et Opus 5.5 reste le choix. Haiku 5.5 n'est pas recommandé : il économise ≈ 205 dollars sur ≈ 595 et porte tout le risque.

**(2) Juge d'une autre lignée : 6 400 actions.** Confiance assez haute (≈ 75 %). L'écart est de quelques dollars de carte devant des lectures à plusieurs centaines, et la variante retire la part de « discrétion non concluante » due au seul sous-échantillon (texte, section 6.10). **Ce qui ferait changer** : un débit mesuré du juge au-delà de ≈ 15 s par lecture (plus de 16 heures de carte de plus), ou un juge servi par appels payants et non sur la carte.

**(3) Avant le devis** (sans décision de Lazar) : fixer la sortie maximale et le niveau de réflexion de chaque modèle au plus bas qui passe l'épreuve de forme, car c'est le poste qui fait varier le total d'un facteur trois ; faire tenir le plafond de chaque lot par un relais qui compte.

## 7. Ce qui n'a pas pu être relevé

- La longueur des deux consignes **en jetons** (caractères et mots mesurés ; aucun comptage de jetons, qui demande un appel au fournisseur).
- La **sortie par appel, réflexion comprise**, des quatre modèles Claude, de Carbon et de GPT sur ces lectures : aucune mesure ; c'est l'essentiel de l'incertitude.
- La longueur des actions et des plans **du bras A** (223 jetons vient d'une autre chaîne) ; la part d'actions jugeables ; la longueur des références (cachées, non ouvertes).
- Le **débit du juge d'une autre lignée**, sa taille, sa consigne (internes de moniteur, non ouverts) ; les seules durées du dépôt sont celles de l'agent.
- Le prix de Carbon et celui des modèles Claude sur une **page versée et scellée** : lus en ligne le 19 novembre, non empreintés ; le barème Claude du dépôt date du 27 octobre et ne porte pas Fable 5.2.
- Les **chaînes de version servies**, l'acceptation de la température 0 et la forme du réglage de réflexion : seule l'épreuve de forme les donne.
- La poche qui paie les appels Claude (crédits ou facture) ; les limites de débit et la durée réelle des lots.
- Le coût en carte du moniteur boîte noire par action (6 400 lectures) : hors de cette estimation, dû au devis.

## 8. Contre-lecture

Aucune. Cette estimation n'est ni contre-lue ni scellée ; le bloquant B-1 la veut contre-lue avant que Lazar choisisse.
