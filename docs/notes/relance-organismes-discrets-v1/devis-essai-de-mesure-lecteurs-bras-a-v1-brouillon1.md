# Organismes discrets, bras A (déplacement des contrôles appris sans consigne) — devis de l'essai de mesure de la longueur de sortie des lecteurs — v1, BROUILLON 1

- **Objet** : le devis d'un essai payant, décidé par Lazar, qui mesure sur des textes synthétiques combien de jetons de sortie, réflexion comprise, rend chaque modèle candidat quand il lit avec les deux consignes du bras A. Il sert à choisir ensuite le modèle de la famille Claude, le budget de réflexion de Carbon (`gemini-4-carbon`) et la sortie maximale, puis à chiffrer le devis des lectures.
- **État** : brouillon, ni contre-lu ni scellé. **Aucune dépense n'est accordée.** Ce devis doit être contre-lu par une autre session avant l'inscription d'une ligne de calcul ; aucun appel payant avant cette ligne.
- **Auteur** : agent neuf (Claude Fable 5.2), le 2026-11-19, 09:36 UTC (`date -u`). N'a écrit ni le préenregistrement, ni ses contre-lectures, ni l'estimation préalable.
- **Interdits tenus** : aucun appel à un modèle ; aucun interne de moniteur ouvert ; aucune fiche de l'organisme d'idéation ; aucune référence cachée, aucune tâche, aucun épisode ; aucun texte de réponse de juge ; aucune clé écrite ; aucun fichier existant modifié ; rien committé ni scellé.
- **Trois lettres** : **M** = relevé sur une pièce ; **C** = calculé ici ; **S** = supposé, sans mesure.

## 0. En une page

1. **176 appels** (au plus 352 envois, une seule reprise permise par appel) : 24 lectures par modèle et par réglage, soit 18 lectures de l'appariement et 6 de la couverture, sur des textes écrits par programme.
2. **Coût attendu ≈ 3,8 dollars ; pire cas ≈ 45 dollars ; plafond demandé 17,75 dollars**, tenu par un compteur qui refuse l'envoi avant qu'il parte. Le pire cas dépasse le plafond : c'est le plafond qui borne la dépense, pas le pire cas.
3. Modèles et réglages : Claude Sonnet 5.5 et Claude Opus 5.5, chacun aux niveaux d'effort bas et moyen ; Claude Haiku 5.5 à l'effort bas (il coûte un centime : il vaut l'essai, mais la règle de choix ne peut pas le retenir) ; Carbon aux budgets de réflexion 1 024 et 2 048 ; GPT (`gpt-6.2-astra`) pour son seul rôle de juge des ancres, 8 appels. **Option non comprise** : Claude Fable 5.2 à l'effort bas, 24 appels, ≈ 1 dollar attendu, plafond 6 de plus.
4. **Ne sont relevés que des champs techniques** ; les réponses brutes sont scellées dans un dossier nommé et ne sont lues par personne pour un jugement.
5. **La règle de choix est écrite d'avance** (section 7) : Opus 5.5 si sa sortie moyenne sur l'appariement, à l'effort le plus bas qui tient, ne dépasse pas 1 500 jetons ; sinon Sonnet 5.5 s'il passe sous ce seuil ou coûte au plus la moitié ; sinon nœud de Lazar.
6. **L'essai ne juge pas la qualité des lecteurs.** Ce sont les épreuves du préenregistrement qui le font.

## 1. Pièces lues, avec empreintes (sha256, calculées à la lecture)

| pièce | empreinte | usage |
|---|---|---|
| `prereg/T0.7-organismes-discrets-v-a-v2-brouillon4.md` | `16187b78b376…` | sections 3.2 à 3.4 (lignes 178 à 291) : entrées, consignes, forme des réponses ; 6.11 (lignes 565 à 586) : comptes |
| `docs/notes/relance-organismes-discrets-v1/estimation-prealable-lectures-bras-a-v1.md` | `e2615c4a63ac…` | tarifs (section 2), comptes (3.1), hypothèses de sortie (3.3), trois réserves techniques (section 5) |
| `docs/notes/relance-organismes-discrets-v1/choix-de-lazar-deux-lecteurs-v2.md` | `563aab94f7c0…` | deux lecteurs (famille Claude et Carbon), GPT juge des ancres |
| `rapports/organismes-discrets-v1/enveloppes-v1/appel-carbon-v3.sh` | `9ef03f804bc1…` | prix et délais de Carbon, lignes 10 à 12 et 24 à 26 |
| `rapports/organismes-discrets-v1/enveloppes-v1/appel-astra-juge-6-2-v1.sh` | `82d028016cf0…` | prix de GPT, lignes 13 à 16 ; sortie maximale 32 768, ligne 26 |
| `docs/notes/ideation-organisme-v1/orchestrateur-v52b/pole/relais_reel.py` | `1b90b020287e…` | relais Claude : barème, lignes 49 à 55 ; plafond en dollars, modèles permis |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v3.py` | `2cf6bc6df83f…` | relais de Google : lecture en flux, délai de silence, **borne en nombre d'appels, aucun plafond en dollars** (options, lignes 612 à 628) |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` | `67f369518102…` | relais compatible OpenAI : plafond en dollars, modèles permis (options, lignes 994 à 1020) |
| `scripts/lancer_relais_local_v1.py` | `d365affcb030…` | lancement d'un relais, clé prise par son nom, environnement réduit |
| `docs/sources/tarifs-openai-v2/developers-openai-com-api-docs-pricing-2026-11-18.html` | `35a048294e2f…` | page de prix d'OpenAI versée et scellée |
| `registres/depenses.md` (523 lignes) | registre vivant | forme des lignes ; lignes 503, 505, 506 (épreuves de Carbon) |
| `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md` | registre vivant | entrées OD-016, OD-020, OD-023, OD-024 (lignes 35, 39, 42, 43) |

Aucune ligne « GO-2026-11-19 » n'est dans `registres/go.md` de cette branche (418 lignes) : la décision de Lazar de faire cet essai m'est rapportée par la session qui m'a lancé ; sa transcription est à verser avant la ligne de calcul.

## 2. Faits établis repris

- **Claude** : les modèles courants refusent la température et un budget de réflexion en jetons ; on règle un niveau d'effort, de bas à maximal ; la réflexion est toujours active sur Fable 5.2 et Opus 5.5 (estimation, section 5, points 1 et 2 ; documentation d'Anthropic livrée avec l'outil de cette session, en cache au 3 novembre 2026). Le niveau par défaut d'Opus 5.5 et de Haiku 5.5 est « moyen », celui de Sonnet 5.5 « haut » : l'essai écrit toujours le niveau, jamais le défaut. **Non vérifié par un appel** : le premier envoi le dira.
- **Carbon** : appelé par lot, il a tronqué ses réponses ; en appel synchrone au budget de réflexion de 8 192, il est resté muet plus de 300 secondes (journal, OD-016 et OD-020). Au budget de 1 024 il a répondu en 4,5 à 46 secondes ; au budget de 2 048, sur une entrée de 2 414 jetons, en 13 secondes, avec 0 jeton de réflexion (OD-024). D'où : appels synchrones, délai borné, deux budgets bornés.
- **Aucun appel payant avant sa ligne de calcul.**

## 3. Les entrées de l'essai

### 3.1 Ce qu'elles ne sont pas
Aucune tâche du bras A, aucune référence cachée, aucun épisode réglé, aucun texte produit par l'agent. L'auteur du générateur n'ouvre aucun de ces fichiers ; il lui suffit des sections 3.2 et 3.3 du préenregistrement, qui donnent les noms des champs d'une action (`ACTION`, `TITLE`, `PROPOSAL`, `CONTROLS`, `COST`, `PREDICTION`) et la forme d'une référence (`- id: c1 | description: …`).

### 3.2 Comment on les fabrique
Un programme (`fabriquer_entrees_essai_mesure_v1.py`), bibliothèque standard et `numpy`, graines par `numpy.random.SeedSequence` dérivées par entrée et inscrites au manifeste (R9) :
- un petit lexique inventé, écrit à la main dans le programme : douze noms de modèles fictifs, douze jeux de données fictifs, douze mesures, douze interventions (par exemple « Tessel-9 », « corpus Halvard », « taux de rappel à 5 ») ; aucun nom réel de modèle, de personne ou de projet ;
- une « expérience synthétique » = un tirage dans ce lexique, mis en phrases anglaises par des gabarits ;
- une **action appariée par construction** : ses contrôles citent les éléments de sa propre expérience ; une **action désappariée par construction** : ses contrôles sont ceux d'une autre expérience synthétique, sans élément commun. La longueur de la réflexion peut dépendre du cas : chaque longueur porte les deux ;
- trois longueurs d'action, réglées par le nombre de phrases : **courte** (≈ 450 caractères), **médiane** (≈ 1 000 caractères, soit ≈ 223 jetons à 4,5 caractères par jeton, S), **la plus longue permise** (≈ 1 800 caractères, soit ≈ 400 jetons, S). La coupe à 400 jetons est celle du découpage du modèle de l'agent, que l'essai n'ouvre pas : la longueur est tenue en caractères, et c'est déclaré ;
- une action de chaque instrument porte des **accolades** dans un champ (le préenregistrement l'exige de l'épreuve de forme, section 3.4) ;
- les consignes sont **celles du brouillon 4, caractère pour caractère** (blocs des sections 3.2 et 3.3), extraites par programme, leur empreinte inscrite au manifeste ; les valeurs remplacent les marques par simple remplacement de chaînes.

### 3.3 Les 24 entrées (les mêmes pour tous les modèles et tous les réglages)

| instrument | entrées | détail |
|---|---|---|
| appariement | **18** | 3 longueurs × 2 cas (apparié, désapparié) × 3 tirages |
| couverture | **6** | plan de dix actions courtes, médianes ou longues × 2 tirages ; référence synthétique de 3, 4 ou 6 contrôles (les bornes du préenregistrement, section 3.3) ; dans chaque plan, la moitié des contrôles de la référence est écrite, l'autre non |

Le lot d'entrées est fabriqué une fois, scellé avec son empreinte, puis relu par programme avant chaque envoi (garde G5).

### 3.4 Pourquoi 24 suffit, et ce que 24 ne donne pas
- **Moyenne de l'appariement (18 lectures)**, le poste qui pèse (11 712 appels sur 12 960 par lecteur) : l'écart type de la moyenne vaut l'écart type des lectures divisé par √18, soit 0,24 fois. Si l'écart type vaut la moitié de la moyenne (S), la moyenne est connue à ± 25 % (2,11 × 0,5 ÷ √18). L'estimation préalable porte aujourd'hui une incertitude d'un facteur trois : l'essai la ramène à un quart.
- **Haut de distribution** : le maximum de 18 lectures dépasse le 85ᵉ centile avec une probabilité de 1 − 0,85¹⁸ = 94,6 % (C). Le rapport donne donc le maximum comme **minorant du 85ᵉ centile**, et rien au-delà : ni 95ᵉ ni 99ᵉ centile ne sont estimables. D'où la marge de la règle de sortie maximale (section 7.3).
- **Couverture (6 lectures)** : un ordre de grandeur seulement (elle pèse un dixième des appels) ; le maximum dépasse la médiane avec une probabilité de 98,4 %.
- **Réserve** : les entrées sont stratifiées par longueur, pas tirées dans la distribution réelle, inconnue. La moyenne rapportée est donnée par longueur, et pondérée ¼ courte, ½ médiane, ¼ longue (S, déclaré d'avance).
- Chaque entrée est lue une fois par réglage : la variation d'une lecture à l'autre de la même entrée n'est pas mesurée.

## 4. Modèles et réglages

| modèle | rôle visé | réglages essayés | sortie maximale demandée | lectures |
|---|---|---|---|---|
| Claude Sonnet 5.5 (`claude-sonnet-5-5`), l'intermédiaire | lecteur | effort bas ; effort moyen | 8 192 (réflexion comprise) | 2 × 24 = 48 |
| Claude Opus 5.5 (`claude-opus-5-5`), le plus capable avant le dernier | lecteur | effort bas ; effort moyen | 8 192 | 2 × 24 = 48 |
| Claude Haiku 5.5 (`claude-haiku-5-5`), le petit | plancher, pour mémoire | effort bas | 8 192 | 24 |
| `gemini-4-carbon` | lecteur | budget de réflexion 1 024 ; 2 048 | 4 096 pour la réponse ; compté 4 096 + budget au pire cas | 2 × 24 = 48 |
| `gpt-6.2-astra` | juge des ancres seulement | réglage de raisonnement par défaut du service, relevé | 8 192 (raisonnement compris) | 8 (6 de l'appariement, 2 de la couverture) |
| **total** | | | | **176** |
| option : Claude Fable 5.2 (`claude-fable-5-2`) | lecteur | effort bas | 8 192 | + 24 |

- **Le petit vaut-il l'essai ?** Oui pour la mesure (≈ 0,01 dollar, et il donne le plancher de la longueur) ; non pour le choix : l'essai ne dit rien de sa capacité à juger, et l'estimation ne le recommande pas. La règle de la section 7 ne peut pas le retenir.
- **Fable 5.2** : laissé en option. Il coûte le double d'Opus 5.5 à la lecture, et le programme a déjà vu Fable arrêter une course par un refus (estimation, section 6). À cocher par Lazar s'il veut le chiffre.
- **Claude** : aucun paramètre de température, aucun paramètre de réflexion (la réflexion adaptative est le défaut), le niveau d'effort écrit à chaque appel ; **aucun repli sur un autre modèle** (le paramètre de repli du service n'est pas envoyé : une mesure servie par un autre modèle serait fausse). Un seul message d'utilisateur, la consigne remplie.
- **Carbon** : appel synchrone lu en flux par le relais de Google version 3 (le flux n'est pas un lot) ; le budget de 8 192 n'est pas essayé.
- **GPT** : le champ de sortie maximale est celui des modèles de raisonnement d'OpenAI ; l'enveloppe actuelle porte 32 768, l'essai porte 8 192.
- Ordre : trois files indépendantes, une par fournisseur, chacune en série ; dans chaque file, le réglage le moins cher d'abord et les entrées courtes d'abord, pour qu'un arrêt laisse des relevés utilisables.

## 5. Ce qui est relevé, et seulement cela

Par envoi, une ligne du journal de l'essai :

| champ | contenu |
|---|---|
| identifiant de l'entrée, modèle demandé, réglage, rang de l'envoi (1 ou 2) | fixés avant l'envoi |
| code de réponse du protocole de transfert | nombre, ou « délai », ou « coupure » |
| motif de fin | tel que rendu par le service |
| compteurs de jetons | entrée ; sortie ; réflexion si le service la rend à part, sinon « non rendue à part » |
| durée | secondes, de l'envoi à la fin de la réponse |
| coût | calculé par la formule de la section 6, au prix compté |
| chaîne de version servie | telle que rendue |
| conformité de forme | oui ou non, **jugée par programme** selon la forme exigée aux sections 3.2 et 3.3 du préenregistrement ; si non, un code de cause sans texte : vide, coupée, entourée d'un autre texte, clés fautives, valeurs fautives |

**Jamais le texte des réponses dans le rapport.** Ne sont relevés ni le verdict rendu, ni l'accord avec la construction (apparié ou désapparié), ni la vérification des extraits : ce serait juger les lecteurs. Les réponses brutes sont écrites telles que reçues dans `runs/essai-mesure-lecteurs-bras-a-v1/<horodatage>/reponses-brutes-non-lues/`, scellées avec une empreinte compagnon, et ne sont ouvertes par aucun agent ni aucune personne pour un jugement.

## 6. Coût

### 6.1 Tarifs comptés (dollars par million de jetons, entrée et sortie, réflexion facturée au prix de sortie)

| modèle | entrée | sortie | source |
|---|---|---|---|
| Claude Sonnet 5.5 | 2 | 10 | `relais_reel.py` (`1b90b020…`), ligne 51 ; page publique `https://platform.claude.com/docs/en/about-claude/pricing`, lue le 19 novembre (estimation, section 2) |
| Claude Opus 5.5 | 4 | 20 | même fichier, ligne 50 ; même page |
| Claude Haiku 5.5 | 0,10 | 0,50 | même fichier, ligne 52 ; même page |
| Claude Fable 5.2 (option) | 8 | 40 | **aucune pièce au dépôt** ; même page, lue le 19 novembre, non versée (estimation, section 2, ligne 40) |
| `gemini-4-carbon` | 4 | 20 | prix annoncé à partir du 1er décembre 2026 (2 et 10 jusqu'au 30 novembre) : `https://aistudio.google.com/docs/pricing`, lue le 19 novembre, non versée (estimation, ligne 44) ; `appel-carbon-v3.sh` (`9ef03f80…`), lignes 10 à 12, cite « 2 / 10 jusqu'au 30 novembre » et compte aux bornes 8,3 et 41,5 |
| `gpt-6.2-astra` | 8 | 40 | `appel-astra-juge-6-2-v1.sh` (`82d02801…`), lignes 13 à 16 ; page versée et scellée du 18 novembre (`35a04829…`) |

**Condition avant la ligne** (R7) : les pages de prix d'Anthropic et de Google sont versées et scellées dans `docs/sources/` ; tant qu'elles ne le sont pas, les prix de Claude Fable 5.2 et de Carbon sont des lectures d'agent. Carbon est compté à 4 et 20 même avant le 1er décembre : borne haute.

### 6.2 Formule
Pour un modèle de prix `pe` et `ps`, un réglage, `n_a` lectures de l'appariement et `n_c` de la couverture, `e` et `s` les jetons d'entrée et de sortie par appel, `k` le nombre d'envois par appel :

`coût = k × [ n_a × (e_a × pe + s_a × ps) + n_c × (e_c × pe + s_c × ps) ] ÷ 1 000 000`

- **Attendu** (`k` = 1) : entrées de l'estimation, 950 et 3 650 jetons (S) ; sorties de l'estimation, section 3.3 (S) : Claude à l'effort bas 500 et 1 200, à l'effort moyen le double (S) ; Carbon 800 et 1 400 au budget de 1 024, 1 150 et 1 950 au budget de 2 048 ; GPT 750 et 1 650.
- **Pire cas** (`k` = 2 : un envoi et sa seule reprise, tous deux facturés) : entrée majorée à un jeton pour deux caractères, soit 2 250 et 12 000 jetons ; sortie maximale servie pleine à chaque envoi (8 192 ; pour Carbon 4 096 + le budget, soit 5 120 et 6 144).
- Aucune redemande de forme dans l'essai : la forme est seulement relevée.

### 6.3 Tableau (dollars ; C sur S pour l'attendu, C pour le pire cas)

| modèle | appels | envois au plus | attendu | pire cas | plafond demandé |
|---|---|---|---|---|---|
| Claude Sonnet 5.5 (effort bas 0,24 ; moyen 0,40) | 48 | 96 | **0,64** | 8,76 | **3,00** |
| Claude Opus 5.5 (effort bas 0,48 ; moyen 0,80) | 48 | 96 | **1,28** | 17,53 | **6,00** |
| Claude Haiku 5.5 (effort bas) | 24 | 48 | **0,01** | 0,22 | **0,25** |
| Carbon (budget 1 024 : 0,61 ; 2 048 : 0,80) | 48 | 96 | **1,41** | 12,61 | **6,00** |
| `gpt-6.2-astra` | 8 | 16 | **0,42** | 5,84 | **2,50** |
| **total** | **176** | **352** | **≈ 3,76** | **≈ 44,96** | **17,75** |
| option Claude Fable 5.2 (effort bas) | + 24 | + 48 | + 0,96 | + 17,53 | + 6,00 |
| total avec l'option | 200 | 400 | ≈ 4,72 | ≈ 62,49 | 23,75 |

- **Le plafond est sous le pire cas, à dessein** : il vaut environ cinq fois l'attendu et il est tenu avant l'envoi (garde G1). La dépense réelle ne peut pas dépasser 17,75 dollars ; si un modèle rend des sorties bien plus longues que supposé, sa file s'arrête au plafond et l'essai le rapporte — c'est déjà la mesure cherchée.
- Pire cas d'un seul envoi, qui sert à la garde : Sonnet 0,086 (appariement) et 0,106 (couverture) ; Opus 0,173 et 0,212 ; Haiku 0,004 et 0,005 ; Carbon 0,111 à 0,171 ; GPT 0,346 et 0,424 ; Fable 0,346 et 0,424.
- **Qui paie** : les appels Claude du programme ont été imputés à des crédits Claude, Carbon et GPT à des comptes facturés (estimation, section 2). À dire par Lazar ; le plafond est le même.
- **Durée** : attendue ≈ 45 minutes en trois files ; délai global de l'essai 3 heures, après quoi tout s'arrête.

### 6.4 Lignes proposées (forme de `registres/depenses.md`)
- Engagement : `| AAAA-MM-JJ | GO-… | Organismes discrets, bras A, essai de mesure de la longueur de sortie des lecteurs sur textes synthétiques : **engagement** — 176 appels au plus (352 envois), plafond 17,75 USD (Sonnet 5.5 : 3 ; Opus 5.5 : 6 ; Haiku 5.5 : 0,25 ; Carbon : 6 ; gpt-6.2-astra : 2,50), pire cas du devis 44,96 ; relais lancés (identifiants de processus, ports) | session ; R-… |`
- Clôture : `| AAAA-MM-JJ | GO-… | même essai, **clos** : N appels servis, R refus, **X USD relevés** (Claude … ; Google … ; OpenAI …) ; relais arrêtés par identifiant de processus ; dossier scellé `runs/essai-mesure-lecteurs-bras-a-v1/…` (manifeste `…`), commit `…` | session ; R-… |`

## 7. Ce que l'essai décide, ce qu'il ne décide pas, et la règle écrite d'avance

### 7.1 Il ne décide pas
- **La qualité des lecteurs** : justesse des verdicts, étayage, accord entre lecteurs. Ce sont les épreuves du préenregistrement (section 6.5) qui la jugent, sur le texte scellé.
- Il **ne remplace pas l'épreuve de forme** du préenregistrement (sections 3.4 et 13.2), qui se joue sur la configuration scellée.
- Il ne mesure ni la longueur réelle des actions du bras A, ni la part d'actions jugeables, ni les limites de débit des comptes.
- Il ne donne aucune raison de changer une consigne. Si le taux de conformité de forme fait envisager une retouche avant scellement, elle est déclarée au texte comme telle ; les réponses ne sont pas lues pour l'écrire.

### 7.2 Réglage qui tient (critère technique, le même pour tous)
Un réglage **tient** si, sur ses 24 lectures : 24 réponses de code 200, reprise unique comprise ; aucun refus ; aucune fin par sortie maximale atteinte ; conformité de forme sur 22 lectures au moins. Sinon il ne tient pas, et le motif est rapporté.

### 7.3 Règle de choix (proposée ici ; elle vaut si la ligne de calcul est accordée sur ce devis)
Notations : `S_a` = moyenne pondérée (¼, ½, ¼) des jetons de sortie, réflexion comprise, sur les 18 lectures de l'appariement ; `C` = coût projeté des lectures d'un lecteur, révision de la consigne comprise, par la formule de l'estimation (13 888 lectures de l'appariement, 1 248 de la couverture), avec les entrées et sorties moyennes mesurées.

1. **Effort retenu** par modèle Claude : le niveau **bas** s'il tient ; sinon le niveau moyen s'il tient ; sinon le modèle est écarté.
2. **Opus 5.5** est retenu si, à son effort retenu, `S_a` ≤ **1 500 jetons** (le seuil écrit par l'estimation avant toute mesure, section 6 ; il correspond à ≈ 580 dollars de lectures pour ce lecteur).
3. Sinon, **Sonnet 5.5** est retenu si, à son effort retenu, `S_a` ≤ 1 500 jetons **ou** `C`(Sonnet) ≤ la moitié de `C`(Opus).
4. Si Opus 5.5 est écarté et que Sonnet 5.5 tient : Sonnet 5.5. Si aucun des deux n'est retenu par 2 à 4 : **aucun choix automatique**, nœud de Lazar, tableau des mesures à l'appui.
5. **Haiku 5.5 et Fable 5.2 ne sont jamais retenus par la règle** : leurs mesures sont rapportées, et les prendre est une décision de Lazar.
6. **Carbon** : budget de 1 024 s'il tient ; sinon 2 048 s'il tient ; sinon nœud de Lazar (le second lecteur est à redire).
7. **Sortie maximale du devis des lectures**, par modèle retenu : deux fois le maximum observé de la sortie, réflexion comprise, arrondi aux 1 024 supérieurs, 2 048 au moins. Le facteur deux tient lieu de haut de distribution, que 18 lectures ne donnent pas.
8. **GPT** : aucun choix (il est déjà désigné) ; sa mesure sert au seul chiffrage des 152 appels du juge des ancres.

Le choix reste celui de Lazar : la règle dit ce que la session recommandera, sans regarder autre chose que ces compteurs.

## 8. Gardes — chacune éprouvée sur un cas sain et sur un artefact, contre un faux fournisseur local, sans aucun appel payant (R5)

| garde | ce qu'elle fait | cas sain | artefact |
|---|---|---|---|
| **G1 plafond de dépense, avant l'envoi** | le chef d'essai tient un compteur par modèle : il refuse l'envoi si le cumul compté plus le pire cas de cet envoi dépasse le plafond du modèle ; un envoi sans compteur lisible (délai, coupure) est compté au pire cas. Les relais de Claude et d'OpenAI portent en plus leur propre plafond (`--plafond-usd`) et leurs modèles permis ; **le relais de Google n'a pas de plafond en dollars** : il est borné en nombre d'appels (`--max-appels 96`) | cumul 1,00, plafond 6,00 : l'envoi part | cumul à 0,01 du plafond : refus, rien n'est envoyé (le faux fournisseur ne reçoit rien), la file s'arrête, code de sortie non nul |
| **G2 délai d'attente** | par envoi : 120 secondes de silence, 180 secondes au total ; une seule reprise ; trois délais de suite sur un réglage arrêtent ce réglage ; délai global de 3 heures | faux fournisseur qui répond en 2 secondes : relevé | faux fournisseur muet : coupé à 120 secondes (délai raccourci pour l'essai), compté au pire cas, reprise unique, puis arrêt |
| **G3 sortie maximale** | le corps de chaque envoi porte la sortie maximale du tableau de la section 4 ; un envoi sans elle, ou plus haute, est refusé avant de partir ; une réponse dont les compteurs dépassent la borne arrête la file | corps conforme : part | corps sans sortie maximale, puis à 32 768 : refus ; réponse à compteurs excessifs : arrêt |
| **G4 arrêt au premier refus** | est un refus : code 401, 402, 403 ou 429 ; motif de fin de refus ou de filtrage ; modèle servi autre que le modèle demandé. Au premier refus, **toute la file du fournisseur s'arrête**, sans reprise ; les autres files continuent | réponse 200, motif de fin normal : la file continue | réponse 429, puis réponse 200 à motif de refus, puis modèle servi différent : arrêt à chaque fois, aucun envoi après |
| **G5 rien de personnel dans ce qui part** | avant chaque envoi, le corps et les en-têtes sont comparés à une liste d'interdits tenue dans un fichier local jamais envoyé (noms de personne, nom du projet et du dépôt, chemins du poste, formes d'identifiant de session, forme de courriel) ; agent d'utilisateur générique ; aucun champ d'identité d'utilisateur ; l'identifiant de l'entrée n'est pas dans le texte ; le lot d'entrées est relu par empreinte | entrée synthétique : part | entrée où l'on a glissé un courriel, puis un chemin du poste, puis un identifiant de session : refus à chaque fois |
| **G6 clés par leur nom** | les relais sont lancés par `scripts/lancer_relais_local_v1.py`, la clé exigée par son nom (`!ANTHROPIC_API_KEY`, `!GEMINI_API_KEY`, `!OPENAI_API_KEY`) ; le chef d'essai n'a aucune clé dans son environnement et ne parle qu'à la boucle locale ; journaux et manifeste sont relus par programme pour toute chaîne de la forme d'une clé | clé factice dans l'environnement du seul relais : le relais part, aucun fichier ne la porte | nom exigé absent : rien ne part ; clé factice glissée dans un journal : le contrôle la trouve et arrête |
| **G7 ligne de calcul** | l'essai exige `GO_ID` d'une ligne valide de `registres/go.md` (garde de calcul du dépôt) et l'empreinte du devis accepté | identifiant valide : part | identifiant absent ou d'une autre ligne : rien ne part |

Aucun repli silencieux : toute garde qui coupe écrit son motif au journal et rend un code de sortie propre.

## 9. Récupérer ce qui est récupérable

- Chaque envoi écrit sa ligne « envoi » au journal, vidée sur le disque, **avant** de partir ; chaque réponse est écrite telle que reçue, vidée sur le disque, **avant** d'être analysée.
- À toute fin — normale, arrêt par une garde, signal, panne — un inventaire (`inventorier_essai_mesure_v1.py`) liste tout fichier du dossier du run, des dossiers de travail et des consoles et journaux des relais, avec taille et empreinte ; l'ensemble est versé dans `runs/essai-mesure-lecteurs-bras-a-v1/<horodatage>/` et scellé.
- **Aucune suppression** (dossier de travail, console d'un relais) avant que l'inventaire scellé soit vérifié sur disque et par empreinte (R11). Un essai interrompu est rapporté tel quel, avec ses relevés partiels ; il n'est pas rejoué sans nouvelle ligne.
- Les relais s'arrêtent par leur identifiant de processus (R10), consigné dans `registres/arrets.md`.

## 10. Code à écrire, et qui le contre-lit

| fichier | rôle |
|---|---|
| `scripts/fabriquer_entrees_essai_mesure_v1.py` | lexique inventé, gabarits, 24 entrées, graines, extraction des deux consignes du brouillon 4 avec leur empreinte |
| `scripts/essai_mesure_lecteurs_v1.py` | chef d'essai : trois files, corps des trois fournisseurs, gardes G1 à G5 et G7, journal, écriture des réponses brutes |
| `scripts/conformite_forme_lectures_v1.py` | conformité de forme, oui ou non et code de cause, sans rien rendre du texte |
| `scripts/inventorier_essai_mesure_v1.py` | inventaire, versement, scellement |
| `scripts/rapport_essai_mesure_v1.py` | tableau des champs techniques, moyennes par longueur, maximum, coût projeté, application de la règle de la section 7 |
| `scripts/faux_fournisseur_essai_mesure_v1.py` | faux amont local des trois formes d'appel, pour les essais des gardes |
| `tests/test_essai_mesure_lecteurs_v1.py` | cas sain et artefact de chaque garde ; essai de bout en bout contre le faux fournisseur |
| configuration `essai-mesure-lecteurs-bras-a-v1.json` | modèles, réglages, sorties maximales, prix, plafonds, délais ; scellée avant la ligne |

Relais repris sans changement : `relais_reel.py` (Claude), `relais_gemini_v3.py` (Google), `relais_kimi_v4.py` avec l'amont d'OpenAI ; lanceur `scripts/lancer_relais_local_v1.py`.

**Contre-lecture** : ce devis, par une autre session, avant la ligne de calcul. Le code, par un sous-agent neuf qui ne l'a pas écrit, d'un autre modèle de la même famille que son auteur (Opus 5.5 si l'auteur est Fable, et inversement), à qui l'on donne la liste des fichiers à lire ; il rejoue les essais des gardes. Le rapport de l'essai est relu par un agent qui n'a écrit ni le code ni ce devis, et qui vérifie que rien du texte des réponses n'y figure.

## 11. Avant la ligne de calcul (rien de payant)

1. Transcription du mot de Lazar qui décide l'essai, versée.
2. Contre-lecture de ce devis ; version suivante si elle le demande.
3. Pages de prix d'Anthropic et de Google versées et scellées.
4. Code écrit, essais des gardes passés, contre-lecture du code.
5. Lot d'entrées et configuration scellés.
6. Ligne de calcul inscrite dans `registres/go.md`, ligne d'engagement dans `registres/depenses.md`.

## 12. Points où je doute

1. **« Le plus capable d'avant le dernier »** : je l'ai lu comme Opus 5.5 (Fable 5.2 étant le dernier). Si la consigne visait Fable 5.1 ou voulait Fable 5.2 dans l'essai, l'option de la section 4 est à cocher ou à changer.
2. **Compteur de réflexion de Claude** : je ne sais pas si le service rend la réflexion à part de la sortie ; le relevé prévoit « non rendue à part ». La sortie totale, seule utile au coût, est rendue.
3. **Sortie maximale de Carbon** : je ne sais pas si elle comprend la réflexion ; le pire cas compte les deux additionnés (borne haute dans les deux lectures).
4. **Réglage de raisonnement de GPT** : laissé au défaut du service faute de pièce au dépôt qui le fixe ; s'il est réglable et que le juge des ancres doit en porter un, la mesure est à refaire à ce réglage.
5. **Longueur « 400 jetons » tenue en caractères** : le découpage du modèle de l'agent n'est pas ouvert ; l'entrée la plus longue peut s'écarter de la coupe réelle d'un quart.
6. **Textes synthétiques** : des phrases à gabarits sont peut-être plus faciles à lire que de vraies actions ; la réflexion mesurée pourrait sous-estimer la réflexion réelle. Le facteur deux de la sortie maximale et le plafond tenu par compteur du devis des lectures couvrent ce risque ; la moyenne, non.
7. **Seuil de 1 500 jetons et critère « la moitié du coût »** : le premier vient de l'estimation ; le second est de moi. Le seuil de conformité de forme (22 sur 24) aussi. À accepter ou à changer par Lazar avant la ligne, jamais après.
8. **Niveau d'effort bas** : c'est le moins cher, mais rien ne dit qu'un lecteur à l'effort bas passera les épreuves ; la règle le retient d'abord pour le coût seulement. Si Lazar préfère l'effort moyen par prudence, le dire avant la ligne.
9. **Code 429** traité comme un refus sans reprise : strict ; une surcharge passagère arrêtera une file et demandera une nouvelle ligne pour la finir.
10. **Prix de Carbon et de Fable 5.2** : lectures d'agent non versées ; la condition de la section 6.1 les règle.
11. **Aucun contrôle par programme** que les entrées synthétiques ne recoupent pas une tâche réelle : il faudrait qu'un programme lise les tâches. Je ne le propose pas ; le lexique inventé rend le recoupement invraisemblable. À trancher par la contre-lecture.
12. **Poche qui paie les appels Claude** : crédits ou facture, non établi.

## 13. Contre-lecture

Aucune. Brouillon ni contre-lu ni scellé.
