# Organismes discrets, bras A (déplacement des contrôles appris sans consigne) — devis de l'essai de mesure de la longueur de sortie des lecteurs — v1, BROUILLON 2

- **Objet** : le devis d'un essai payant qui mesure, sur des textes synthétiques, combien de jetons de sortie, réflexion comprise, rend chaque modèle candidat quand il lit avec les deux consignes du bras A. Il sert à choisir ensuite le modèle de la famille Claude, le budget de réflexion de Carbon (`gemini-4-carbon`) et la sortie maximale, puis à chiffrer le devis des lectures. Il tient lieu de l'épreuve de forme des brouillons 3 et 4 du préenregistrement (brouillon 5, section 3.4).
- **État** : brouillon 2, non scellé. Remplace pour la lecture le brouillon 1 (`4678d7c9ab1c…`, gardé sans modification, R12), après sa contre-lecture (`contre-lecture-devis-essai-de-mesure-lecteurs-v1.md`, `d1b8ad89037c…`, verdict « pas avant : sept corrections de texte, sans changement de plafond »). **Aucune dépense n'est accordée.** Aucun appel payant avant la ligne de calcul.
- **Auteur** : agent neuf (Claude Fable 5.2), le 2026-11-19, 09:54 UTC (`date -u`). N'a écrit ni le préenregistrement, ni ses contre-lectures, ni l'estimation préalable.
- **Interdits tenus** : aucun appel à un modèle ; aucun interne de moniteur ouvert ; aucune fiche de l'organisme d'idéation ; aucune référence cachée, aucune tâche, aucun épisode ; aucun texte de réponse de juge ; aucune clé écrite ; aucun fichier existant modifié ; rien committé ni scellé. Réseau : `git fetch` de la branche principale, et quatre requêtes vers des pages publiques de prix, sans clé ni nom de personne, de projet ou d'identifiant.
- **Trois lettres** : **M** = relevé sur une pièce ; **C** = calculé ici ; **S** = supposé, sans mesure.

## 0. En une page

1. **Trois files séparées, une par fournisseur, chacune avec son plafond** : file Claude (120 appels, plafond 9,25 dollars), file Carbon (48 appels, plafond 6), file GPT (8 appels, plafond 2,50). **176 appels**, au plus 352 envois facturables.
2. **Coût attendu ≈ 3,8 dollars ; pire cas ≈ 50 dollars ; plafond demandé 17,75 dollars** (23,75 avec l'option Claude Fable 5.2), tenu par compteur avant l'envoi, sous trois conditions écrites (section 6.3), **à un seul envoi de Carbon près**.
3. **Aucune file ne part avant la ligne de calcul.** Les files Carbon et GPT peuvent partir sans attendre la file Claude. **La file Claude ne part pas tant qu'une clé n'a pas été posée par Lazar dans l'environnement et vérifiée** (garde G8).
4. Modèles et réglages : Claude Opus 5.5 et Claude Sonnet 5.5, chacun aux niveaux d'effort bas et moyen ; Claude Haiku 5.5 à l'effort bas, pour mémoire ; Carbon aux budgets de réflexion 1 024 et 2 048 ; `gpt-6.2-astra` pour son seul rôle de juge des ancres.
5. **Ne sont rapportés que des champs techniques.** Les réponses sont gardées entières, scellées, lues par des programmes nommés seulement.
6. **La règle de choix est écrite d'avance** (section 7), avec son parti pris déclaré pour Opus 5.5.
7. **Écart déclaré au mot de Lazar** : 17,75 dollars de plafond dépassent « quelques dollars » ; l'attendu, ≈ 3,8, y est conforme (section 1).

## 1. La décision de Lazar, et les écarts déclarés

La décision est la ligne **GO-2026-11-19-22** de `registres/go.md`, branche principale (ligne 455 ; Lazar, « go recos, feu organisme », session mère, vers 09:33Z ; R-3695). Sa lettre : « **Bras A, budget des deux lecteurs par modèles de langue : option (a), un essai de mesure payant d'abord** (une vingtaine de lectures par lecteur, quelques dollars), sur une ligne de calcul à part, après un devis contre-lu. Le modèle Claude et le budget des lecteurs se choisissent ensuite, sur la longueur de sortie mesurée, réflexion comprise. Ce choix lève la circularité de la section 13. Recommandation de la mère, confiance 0,7 (R-3676). **Aucune dépense n'est accordée par cette ligne.** »

**Écarts déclarés** :
- 48 lectures par lecteur (24 par réglage, deux réglages) au lieu d'« une vingtaine » ;
- **plafond de 17,75 dollars, qui dépasse « quelques dollars »** ; l'attendu, ≈ 3,8 dollars, y est conforme. La ligne de calcul nomme le plafond comme tel.

## 2. Pièces lues, avec empreintes (sha256, calculées à la lecture)

| pièce | empreinte | usage |
|---|---|---|
| `prereg/T0.7-organismes-discrets-v-a-v2-brouillon5.md` | `cf1d2b9261c1…` | sections 3.2 à 3.4 (lignes 188 à 302) : entrées, consignes, forme, réglages, essai de mesure ; 6.11 ; 8.5 ; 13 |
| contre-lecture du brouillon 1 de ce devis | `d1b8ad89037c…` | corrections C1 à C7, recommandations R1 à R9 |
| `docs/notes/relance-organismes-discrets-v1/estimation-prealable-lectures-bras-a-v1.md` | `e2615c4a63ac…` | comptes, hypothèses de sortie |
| `docs/notes/relance-organismes-discrets-v1/choix-de-lazar-deux-lecteurs-v2.md` | `563aab94f7c0…` | deux lecteurs, GPT juge des ancres |
| `registres/go.md` de la branche principale | registre vivant | lignes GO-2026-11-19-22, -24, -25, -26 |
| `rapports/organismes-discrets-v1/enveloppes-v1/appel-carbon-v3.sh` | `9ef03f804bc1…` | prix de repli de Carbon, 8,3 et 41,5 (lignes 10 à 12 et 24) |
| `rapports/organismes-discrets-v1/enveloppes-v1/appel-astra-juge-6-2-v1.sh` | `82d028016cf0…` | prix de GPT (lignes 13 à 16) |
| `docs/notes/ideation-organisme-v1/orchestrateur-v52b/pole/relais_reel.py` | `1b90b020287e…` | relais Claude : barème (lignes 49 à 55), plafond, réserve par appel, modèles permis |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v3.py` | `2cf6bc6df83f…` | relais de Google : flux, résumés de pensée (en-tête, point 2), borne en nombre d'appels, aucun plafond en dollars |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` | `67f369518102…` | relais compatible OpenAI : plafond, réserve tirée des octets |
| `scripts/lancer_relais_local_v1.py` | `d365affcb030…` | lancement d'un relais, clé prise par son nom |
| pages de prix versées ce jour, `docs/sources/prix-fournisseurs-2026-11-19/` | section 6.1 | tarifs |
| `docs/sources/tarifs-openai-v2/developers-openai-com-api-docs-pricing-2026-11-18.html` | `35a048294e2f…` | prix de GPT, page scellée le 18 novembre |

## 3. Faits établis repris

- **Claude** : les modèles courants refusent la température et un budget de réflexion en jetons ; on règle un niveau d'effort ; la réflexion est toujours active sur Fable 5.2 et Opus 5.5 (R-3676 ; brouillon 5, section 3.4). Le niveau par défaut d'Opus 5.5 et de Haiku 5.5 est « moyen », celui de Sonnet 5.5 « haut » : l'essai écrit toujours le niveau.
- **Carbon** : par lot, il a tronqué ses réponses ; en appel synchrone au budget de 8 192, il est resté muet plus de 300 secondes (journal de la relance, OD-016 et OD-020) ; au budget de 1 024 il a répondu en 4,5 à 46 secondes ; au budget de 2 048, en 13 secondes, avec 0 jeton de réflexion (OD-024).
- **Aucun appel payant avant sa ligne de calcul.**

## 4. Les entrées de l'essai

### 4.1 Ce qu'elles ne sont pas
Aucune tâche du bras A (ni de réserve, ni d'évaluation, ni autre : le brouillon 5 permettrait une tâche hors de ces listes, nommée au devis ; **ce devis n'en prend aucune**), aucune référence cachée, aucun épisode réglé, aucun texte produit par l'agent. L'auteur du générateur n'ouvre aucun de ces fichiers.

### 4.2 Comment on les fabrique
Un programme (`fabriquer_entrees_essai_mesure_v1.py`), bibliothèque standard et `numpy`, graines par `numpy.random.SeedSequence` dérivées par entrée et inscrites au manifeste (R9) :
- un lexique inventé, écrit à la main dans le programme : douze noms de modèles fictifs, douze jeux de données fictifs, douze mesures, douze interventions ; aucun nom réel de modèle, de personne ou de projet ;
- une « expérience synthétique » = un tirage dans ce lexique, mis en phrases anglaises par des gabarits ;
- trois cas, par construction : **apparié** (les contrôles citent les éléments de la même expérience) ; **désapparié** (les contrôles sont ceux d'une autre expérience, sans élément commun) ; **partiellement apparié** (la moitié des contrôles vient d'une autre expérience : le cas où la réflexion sera sans doute la plus longue, et dont la consigne traite) ;
- trois longueurs d'action, réglées par le nombre de phrases : **courte** (≈ 450 caractères), **médiane** (≈ 1 000 caractères, ≈ 223 jetons à 4,5 caractères par jeton, S), **la plus longue permise** (≈ 1 800 caractères, ≈ 400 jetons, S) ; la longueur est tenue en caractères, le découpage du modèle de l'agent n'étant pas ouvert ;
- une action de chaque instrument porte des **accolades** dans un champ ;
- **les deux consignes sont extraites par programme du brouillon 5**, caractère pour caractère : appariement, lignes 195 à 220 (2 700 caractères, empreinte `98a9bd34d280…`) ; couverture, lignes 242 à 276 (3 550 caractères, empreinte `ecf590eae0c0…`) — lignes jointes par un saut de ligne, sans saut final. Ces deux blocs sont identiques à ceux du brouillon 4 (comparés par programme). Les valeurs remplacent les marques par simple remplacement de chaînes.
- **Au scellement du texte du bras A**, les empreintes des deux blocs du texte scellé sont comparées à celles du manifeste de l'essai. Si elles diffèrent, le rapport le dit, la mesure est celle d'une consigne voisine, et refaire la mesure est une décision de Lazar.

### 4.3 Les 24 entrées (les mêmes pour tous les modèles et tous les réglages)

| instrument | entrées | détail |
|---|---|---|
| appariement | **18** | 3 longueurs × 3 cas (apparié, désapparié, partiellement apparié) × 2 tirages, rangées en **trois blocs de six** ; chaque bloc porte chaque longueur deux fois et chaque cas deux fois |
| couverture | **6** | plan de dix actions courtes, médianes ou longues × 2 tirages, en **deux blocs de trois** ; référence synthétique de 3, 4 ou 6 contrôles ; dans chaque plan, la moitié des contrôles de la référence est écrite, l'autre non |

Le lot est fabriqué une fois, scellé, puis relu par empreinte avant chaque envoi.

### 4.4 Pourquoi 24 suffit, et ce que 24 ne donne pas
- **Moyenne de l'appariement (18 lectures)** : l'écart type de la moyenne vaut 0,24 fois l'écart type des lectures (0,25 avec la pondération). Si l'écart type vaut la moitié de la moyenne (S), la moyenne est connue à ± 25 % (2,11 × 0,5 ÷ √18). **L'essai ramène à environ ± 25 % l'incertitude d'échantillonnage de la moyenne sur ces textes synthétiques. L'écart entre ces textes et les actions réelles du bras A, plus variées et parfois partiellement appariées, n'est pas borné par l'essai : l'incertitude sur le coût réel reste plus large qu'un quart, et l'essai ne dit pas de combien.**
- **Haut de distribution** : le maximum de 18 lectures dépasse le 85ᵉ centile avec une probabilité de 94,6 % (1 − 0,85¹⁸). Le rapport donne le maximum comme **minorant du 85ᵉ centile**, rien au-delà.
- **Couverture (6 lectures)** : un ordre de grandeur seulement.
- Les entrées sont stratifiées par longueur, non tirées dans la distribution réelle, inconnue : moyenne donnée par longueur, et pondérée ¼ courte, ½ médiane, ¼ longue (S, déclaré d'avance).
- Chaque entrée est lue une fois par réglage : la variation d'une lecture à l'autre n'est pas mesurée.

## 5. Les trois files, les modèles et les réglages

### 5.1 Tableau

| file | modèle | réglages, dans l'ordre joué | sortie maximale envoyée | lectures | plafond |
|---|---|---|---|---|---|
| **Claude** | Claude Opus 5.5 (`claude-opus-5-5`) | effort bas (1ᵉʳ) ; effort moyen (3ᵉ) | 8 192, réflexion comprise | 48 | 6,00 |
| | Claude Sonnet 5.5 (`claude-sonnet-5-5`) | effort bas (2ᵉ) ; effort moyen (4ᵉ) | 8 192 | 48 | 3,00 |
| | Claude Haiku 5.5 (`claude-haiku-5-5`), pour mémoire | effort bas (5ᵉ, en dernier) | 8 192 | 24 | 0,25 |
| | **file Claude** | | | **120** | **9,25** |
| **Carbon** | `gemini-4-carbon` | budget de réflexion 1 024, puis 2 048 | 4 096 pour la réponse ; compté 4 096 + le budget au pire cas | **48** | **6,00** |
| **GPT** | `gpt-6.2-astra`, juge des ancres seulement | réglage de raisonnement par défaut du service, relevé | 8 192, raisonnement compris | **8** (6 de l'appariement, 2 de la couverture) | **2,50** |
| **total** | | | | **176** | **17,75** |
| option, file Claude | Claude Fable 5.2 (`claude-fable-5-2`) | effort bas (6ᵉ) | 8 192 | + 24 | + 6,00 |

- **Ordre** : dans la file Claude, les réglages que la règle lit d'abord passent d'abord, Haiku 5.5 en dernier ; dans chaque réglage, les entrées vont par blocs (section 4.3), pour qu'un arrêt laisse un préfixe équilibré et non les seules entrées courtes.
- **Le petit vaut-il l'essai ?** Oui pour la mesure (≈ 0,01 dollar ; il donne le plancher), non pour le choix : la règle ne peut pas le retenir.
- **Fable 5.2** : en option ; le double d'Opus 5.5 à la lecture, et un refus de juger déjà vu dans le programme.

### 5.2 Corps des appels Claude (champs exacts, écrits à la configuration)
`model` ; `max_tokens: 8192` ; `output_config: {"effort": "low"}` ou `{"effort": "medium"}` (dans `output_config`, pas au premier niveau) ; un seul message d'utilisateur, la consigne remplie. **Ni `temperature`, ni `top_p`, ni `top_k` ; aucun champ `thinking` ; aucun en-tête bêta ; aucun paramètre de repli sur un autre modèle** (une lecture servie par un autre modèle fausserait la mesure). La valeur de l'en-tête `anthropic-version` est inscrite à la configuration. L'affichage de la réflexion reste au défaut : aucun texte de réflexion n'est rendu ; les blocs de réflexion sont gardés tels qu'ils viennent (texte vide et signature).

### 5.3 Carbon
Appel synchrone lu en flux par le relais de Google version 3 (le flux n'est pas un lot), lancé avec `--modele gemini-4-carbon --max-appels 97 --delai-silence-s 120 --delai-amont-s 180 --sans-pensees-amont`. **Sans cette dernière option, le relais demande des résumés de pensée à l'amont et les retire de la réponse qu'il rend (en-tête du relais, point 2) : une sortie du modèle serait perdue.** Les jetons de réflexion restent comptés (`thoughtsTokenCount`). Le chef d'essai reçoit la réponse recomposée par le relais, non le flux de l'amont : c'est elle qui est versée, et le rapport le dit. Le budget de 8 192 n'est pas essayé. La borne de 97 appels vaut 96 envois plus l'envoi d'essai de la température (5.5).

### 5.4 GPT
Relais compatible OpenAI (`relais_kimi_v4.py`, amont d'OpenAI), `--modeles-permis gpt-6.2-astra --plafond-usd 2.50` ; champ de sortie maximale des modèles de raisonnement, à 8 192 (l'enveloppe actuelle porte 32 768).

### 5.5 Température et raisonnement de Carbon et de GPT
Le brouillon 5 (section 3.4) écrit « température 0 si le service l'accepte ; budget ou niveau de réflexion du modèle ». L'essai envoie donc la température 0 à Carbon et à GPT. Si le premier envoi d'une file est refusé par un code 400 qui nomme la température (refus sans frais), la file la retire pour tous ses envois, le note au journal et au rapport, et continue ; tout autre code 400 arrête la file. Carbon : budget de réflexion écrit à chaque appel. GPT : le texte n'a pas tranché son réglage de raisonnement ; l'essai le laisse au défaut du service et le relève.

### 5.6 Clés (réponse de la session mère)
- **Carbon** : le relais de Google déjà employé par la relance ; la clé est lue par le nom de sa variable, `GEMINI_API_KEY`, dans le seul environnement du relais.
- **GPT** : le secret de réseau OpenAI de l'environnement de la session ; rien d'autre. Aucune valeur de clé n'est dans le conteneur.
- **Claude** : **aucune clé dans l'environnement de cette session pour l'instant.** La question est posée à Lazar par la session mère, dont la recommandation est : une clé posée par lui dans l'environnement, puis vérifiée par un appel minimal sous une ligne à part de 0,01 dollar. **La file Claude ne part pas sans cette clé posée et vérifiée** (garde G8). La poche qui paie (crédits ou facture) est dite par Lazar avec la clé ; le plafond en dollars au barème public vaut dans les deux cas.

## 6. Coût

### 6.1 Tarifs comptés (dollars par million de jetons ; réflexion facturée au prix de sortie)

| modèle | entrée | sortie | source |
|---|---|---|---|
| Claude Opus 5.5 | 4 | 20 | page d'Anthropic versée ce jour : `docs/sources/prix-fournisseurs-2026-11-19/platform-claude-com-docs-en-about-claude-pricing-20261119T095216Z.html` (`78aff5c8d73a…`, téléchargée à 09:52:16Z ; tableau des prix des modèles) ; `relais_reel.py`, ligne 50 |
| Claude Sonnet 5.5 | 2 | 10 | même page ; `relais_reel.py`, ligne 51 |
| Claude Haiku 5.5 | 0,10 | 0,50 | même page (entrées de 100 000 jetons au plus) ; `relais_reel.py`, ligne 52 |
| Claude Fable 5.2 (option) | **10** | **50** | compté comme le fait le relais Claude pour un modèle hors de son barème (`relais_reel.py`, ligne 55) : borne haute ; la page versée dit 8 et 40 |
| `gemini-4-carbon` | **4** | **20** | page de Google versée ce jour : `…/aistudio-google-com-docs-pricing-20261119T095218Z.html` (`89c58281ba7e…`, 09:52:18Z), section « Gemini 4 Carbon », onglet « Standard », lignes 154 à 163 : 2 et 10 jusqu'au 30 novembre 2026, 4 et 20 à partir du 1er décembre, sortie « including thinking tokens ». Compté à 4 et 20 dès maintenant : borne haute |
| `gemini-4-carbon`, **prix de repli** | 8,3 | 41,5 | `appel-carbon-v3.sh` (`9ef03f80…`), lignes 10 à 12 et 24 |
| `gpt-6.2-astra` | 8 | 40 | page scellée du 18 novembre (`35a04829…`) ; `appel-astra-juge-6-2-v1.sh`, lignes 13 à 16. **La page d'OpenAI n'a pas été lisible ce jour** (code 403, requête non reprise ; trace versée) |

**Règle du repli** : les pages versées ce jour ne sont pas encore scellées (provenance : `docs/sources/prix-fournisseurs-2026-11-19/provenance.md`). Tant que la page de Google n'est pas scellée, ou si son scellement échoue, **Carbon est compté au prix de repli, 8,3 et 41,5**, son plafond restant 6 dollars : sa file s'arrête plus tôt (elle ne finit alors que jusqu'à environ deux fois la sortie supposée). Les lectures d'agent des pages (balises retirées par programme) sont à vérifier par celui qui scelle.

### 6.2 Formule
Pour un modèle de prix `pe` et `ps`, `n_a` lectures de l'appariement et `n_c` de la couverture, `e` et `s` les jetons d'entrée et de sortie par appel, `k` le nombre d'envois par appel :

`coût = k × [ n_a × (e_a × pe + s_a × ps) + n_c × (e_c × pe + s_c × ps) ] ÷ 1 000 000`

- **Attendu** (`k` = 1) : entrées 950 et 3 650 jetons (S) ; sorties de l'estimation (S) : Claude à l'effort bas 500 et 1 200, à l'effort moyen le double ; Carbon 800 et 1 400 au budget de 1 024, 1 150 et 1 950 au budget de 2 048 ; GPT 750 et 1 650.
- **Pire cas** (`k` = 2 : l'envoi et sa seule reprise, tous deux facturés) : entrée majorée à **un jeton par octet du corps** (≈ 4 500 et ≈ 24 000 ; le chef d'essai calcule sur le corps réel) ; sortie maximale servie pleine (8 192 ; Carbon 5 120 et 6 144).
- Aucune redemande de forme dans l'essai : la forme est seulement relevée.

### 6.3 Tableau (dollars ; C sur S pour l'attendu, C pour le pire cas)

| file | modèle | appels | envois facturables au plus | attendu | pire cas | plafond demandé |
|---|---|---|---|---|---|---|
| Claude | Opus 5.5 (bas 0,48 ; moyen 0,80) | 48 | 96 | **1,28** | 19,33 | **6,00** |
| Claude | Sonnet 5.5 (bas 0,24 ; moyen 0,40) | 48 | 96 | **0,64** | 9,66 | **3,00** |
| Claude | Haiku 5.5 (bas) | 24 | 48 | **0,01** | 0,24 | **0,25** |
| | **file Claude** | **120** | **240** | **1,93** | **29,23** | **9,25** |
| Carbon | budgets 1 024 (0,61) et 2 048 (0,80), à 4 et 20 | 48 | 96 | **1,42** | 14,41 | **6,00** |
| GPT | `gpt-6.2-astra` | 8 | 16 | **0,42** | 6,44 | **2,50** |
| | **total** | **176** | **352** | **≈ 3,77** | **≈ 50,09** | **17,75** |
| | Carbon au prix de repli (8,3 et 41,5), à la place | 48 | 96 | 2,94 | 29,91 | 6,00 |
| | total, Carbon au prix de repli | 176 | 352 | ≈ 5,29 | ≈ 65,59 | 17,75 |
| option | Claude Fable 5.2 (bas), compté à 10 et 50 | + 24 | + 48 | + 1,20 | + 24,16 | + 6,00 |
| | total avec l'option (Carbon à 4 et 20) | 200 | 400 | ≈ 4,97 | ≈ 74,25 | 23,75 |

Le pire cas a monté depuis le brouillon 1 (44,96) parce que l'entrée y est désormais majorée par octet ; l'attendu et les plafonds n'ont pas changé. S'ajoute au plus un envoi refusé sans frais par file pour l'essai de la température (Carbon, GPT).

Pire cas d'un seul envoi, qui sert à la garde (appariement ; couverture) : Opus 0,182 ; 0,260 — Sonnet 0,091 ; 0,130 — Haiku 0,005 ; 0,007 — Carbon à 4 et 20 : 0,120 à 0,141 ; 0,198 à 0,219 — Carbon au prix de repli : 0,250 à 0,292 ; 0,412 à 0,454 — GPT 0,364 ; 0,520 — Fable à 10 et 50 : 0,455 ; 0,650.

**Le plafond est sous le pire cas, à dessein** : le pire cas suppose chaque appel envoyé deux fois et chaque envoi servi plein ; le plafond laisse finir chaque file jusqu'à environ cinq fois la sortie supposée (contre-lecture : Sonnet 5.5 et Opus 5.5, 5,6 ; Carbon, 5,0 ; GPT, 6,3), au-delà du « haut plausible » de l'estimation (trois fois). **Il est tenu avant l'envoi (garde G1) si trois conditions tiennent** :
- **(a) prix comptés au moins égaux aux prix facturés** : pages versées et scellées ; à défaut, Carbon compté à 8,3 et 41,5, Fable 5.2 à 10 et 50 ;
- **(b) pire cas d'un envoi calculé sur le corps réel**, un jeton au plus par octet, et sur la sortie maximale envoyée ;
- **(c) sortie maximale respectée par le service.** C'est une borne dure pour Claude (`max_tokens`, réflexion comprise) et pour GPT (`max_completion_tokens`, raisonnement compris). **Pour Carbon, aucune pièce du dépôt n'établit que le budget de réflexion est une borne dure** : une réponse au-delà de sa borne comptée arrête sa file (garde G3), et la dépense peut alors dépasser le plafond du coût de ce seul envoi.

Si un modèle rend des sorties plus longues encore, sa file s'arrête au plafond : le réglage en cours ne tient pas (7.2), ses relevés partiels sont rapportés comme minorants, et la règle de la section 7 ne s'y applique pas.

**Pour Carbon, il n'y a qu'une garde en dollars, celle du chef d'essai** ; le relais de Google n'est qu'une seconde barrière en nombre (`--max-appels 97`), qui bornerait la dépense à ≈ 21 dollars au pire cas compté si le chef d'essai faillait. La garde du plafond est donc éprouvée, cas sain et artefact, sur la forme d'appel de Google en particulier.

**Durée** : attendue ≈ 45 minutes ; délai global de 4 heures par file.

### 6.4 Lignes proposées (forme de `registres/depenses.md`), une par file
- Engagement, file Carbon : `| AAAA-MM-JJ | GO-… | Organismes discrets, bras A, essai de mesure de la longueur de sortie des lecteurs sur textes synthétiques, **file Carbon : engagement** — 48 appels au plus (96 envois), plafond 6 USD (tenu par compteur ; dépassement possible d'un seul envoi de Carbon si son budget de réflexion n'est pas respecté, ce qui arrête sa file), Carbon compté à 4 et 20 (ou 8,3 et 41,5) ; relais lancé (identifiant de processus, port) | session ; R-… |`
- Engagement, file GPT : même forme, 8 appels (16 envois), plafond 2,50 USD (tenu par compteur).
- Engagement, file Claude : même forme, 120 appels (240 envois), plafond 9,25 USD (Opus 5.5 : 6 ; Sonnet 5.5 : 3 ; Haiku 5.5 : 0,25), tenu par compteur ; variable de clé et poche nommées ; attestation de clé vérifiée citée.
- Clôture, par file : `| AAAA-MM-JJ | GO-… | même essai, file …, **close** : N appels servis, R refus, **X USD relevés** ; relais arrêté par identifiant de processus ; dossier scellé `runs/essai-mesure-lecteurs-bras-a-v1/…` (manifeste `…`), commit `…` | session ; R-… |`
- La ligne de calcul écrit que le plafond de 17,75 dollars dépasse les « quelques dollars » de GO-2026-11-19-22, l'attendu restant ≈ 3,8.

## 7. Ce que l'essai décide, ce qu'il ne décide pas, et la règle écrite d'avance

### 7.1 Il ne décide pas
- **La qualité des lecteurs** : justesse des verdicts, étayage, accord entre lecteurs. Ce sont les épreuves du préenregistrement qui la jugent, sur le texte scellé. **Rien de ce que l'essai mesure n'entre dans une variable, un seuil ou un verdict** (brouillon 5, section 3.4).
- Il ne mesure ni la longueur ni la difficulté des actions réelles du bras A, ni la part d'actions jugeables, ni les limites de débit des comptes, ni le prix de Carbon au moment des lectures (il mesure des jetons, pas des dollars).
- Il ne donne aucune raison de changer une consigne. Les réponses ne sont pas lues pour en écrire une.

### 7.2 Réglage qui tient (critère technique, le même pour tous)
Un réglage **tient** si, sur ses 24 lectures : 24 réponses de code 200, reprise unique comprise ; aucun refus ; aucune fin par sortie maximale atteinte ; conformité de forme sur 22 lectures au moins. Un réglage arrêté au plafond ne tient pas. Le seuil « 22 sur 24 » est **choisi d'avance, non étalonné** (même statut que GO-2026-11-19-24, point 3), soumis à Lazar avec la ligne de calcul.

### 7.3 Règle de choix (elle vaut si la ligne de calcul est accordée sur ce devis)

**Notations.**
- `S_a` = moyenne pondérée (¼, ½, ¼ ; moyenne simple des six lectures dans chaque longueur) des **jetons de sortie facturés, réflexion comprise**, sur les 18 lectures de l'appariement, lus ainsi : Claude, `usage.output_tokens` (réflexion comprise) ; Carbon, `candidatesTokenCount` + `thoughtsTokenCount` ; GPT, `usage.completion_tokens` (raisonnement compris). **Une lecture reprise compte par son dernier envoi pour `S_a`, par ses deux envois pour `C`.**
- `C` = coût projeté des lectures d'un lecteur par la formule de l'estimation (13 888 lectures de l'appariement, 1 248 de la couverture, révision de la consigne comprise), avec les entrées et sorties moyennes mesurées, **plus les redemandes de forme au taux de non-conformité mesuré**.

**Règle.**
1. **Effort retenu** par modèle Claude : le niveau bas s'il tient ; sinon le niveau moyen s'il tient ; sinon le modèle est écarté.
2. **Opus 5.5** est retenu si, à son effort retenu, `S_a` ≤ **1 500 jetons** (seuil écrit par l'estimation avant toute mesure ; ≈ 580 dollars de lectures pour ce lecteur).
3. Sinon, **Sonnet 5.5** est retenu si, à son effort retenu, `S_a` ≤ 1 500 jetons **ou** `C`(Sonnet) ≤ la moitié de `C`(Opus).
4. Si Opus 5.5 est écarté et que Sonnet 5.5 tient : Sonnet 5.5. Si aucun des deux n'est retenu : **aucun choix automatique**, nœud de Lazar, tableau des mesures à l'appui.
5. **Haiku 5.5 et Fable 5.2 ne sont jamais retenus par la règle.**
6. **Carbon** : budget de 1 024 s'il tient ; sinon 2 048 s'il tient ; sinon nœud de Lazar.
7. **Sortie maximale du devis des lectures**, par modèle retenu : **la plus grande de 8 192 et de quatre fois le maximum observé de la sortie**, réflexion comprise, arrondie aux 1 024 supérieurs ; pour Carbon, la même règle porte sur la réponse seule (`candidatesTokenCount`), le budget de réflexion étant celui du point 6. Une sortie maximale non servie ne coûte rien : elle ne pèse que sur la réserve par envoi et sur le pire cas ; trop basse, elle coupe des lectures du bras A, qui deviennent « sans verdict (forme) » après la redemande, alors que le texte veut une sortie maximale « large ». Le coût du devis des lectures se calcule sur les moyennes, jamais sur ce maximum.
8. **GPT** : aucun choix (il est déjà désigné) ; sa mesure sert au seul chiffrage des appels du juge des ancres.

**Partis pris de la règle, déclarés.** Ce sont des choix, pas des résultats neutres.
- **Elle penche vers Opus 5.5** : il est pris dès que `S_a` ≤ 1 500, quel que soit l'écart de coût avec Sonnet 5.5 (jusqu'à ≈ 580 dollars contre peut-être ≈ 150). C'est le parti de l'estimation : le coût d'un lecteur trop faible se paie en tâches d'épreuve lues, qui ne se rachètent pas.
- **Elle bascule vers Sonnet 5.5 dès qu'Opus dépasse 1 500** : les prix de Sonnet 5.5 étant exactement la moitié de ceux d'Opus 5.5, la clause « moitié du coût » revient à « Sonnet ne rend pas plus de jetons qu'Opus » ; c'est un critère de longueur, presque toujours vrai. Et Sonnet est pris sans borne de longueur quand Opus est écarté (point 4). Le coût revient alors à Lazar par le devis des lectures.
- **Elle penche vers l'effort bas**, pour le seul coût : rien ne dit qu'un lecteur à l'effort bas passera les épreuves.
- **Elle compare les modèles à leur effort retenu, pas à effort égal** : les niveaux d'Opus 5.5 et de Sonnet 5.5 ne sont pas étalonnés de la même façon.
- Le seuil « moitié du coût » est choisi d'avance, non étalonné, soumis à Lazar avec la ligne.

Le choix reste celui de Lazar : la règle dit ce que la session recommandera, sans regarder autre chose que ces compteurs.

## 8. Ce qui est rapporté, ce qui est gardé, et qui peut lire

### 8.1 Rapporté : des champs techniques, et seulement cela
Par envoi : identifiant de l'entrée, modèle demandé, réglage, rang de l'envoi (1 ou 2) ; code de réponse du protocole de transfert (ou « délai », « coupure »), et son origine, relais ou amont ; motif de fin ; compteurs de jetons d'entrée, de réflexion (si le service la rend à part, sinon « non rendue à part ») et de sortie ; durée ; coût ; chaîne de version servie ; conformité de forme, oui ou non, **jugée par programme** selon la forme exigée aux sections 3.2 et 3.3 du préenregistrement, avec un code de cause sans texte (vide, coupée, entourée d'un autre texte, clés fautives, valeurs fautives).

**Jamais le texte des réponses dans le rapport.** Ne sont relevés ni le verdict rendu, ni l'accord avec la construction, ni la vérification des extraits. Un programme vérifie que le rapport ne contient aucune sous-chaîne des réponses.

### 8.2 Gardé (règle « récupérer ce qui est récupérable » ; brouillon 5, section 8.5)
Versé dans `runs/essai-mesure-lecteurs-bras-a-v1/<horodatage>/`, scellé avec empreinte compagnon, **committé et poussé sur la branche de la relance avant toute suppression** :
1. le lot des 24 entrées, la configuration, le manifeste (graines, versions, commit), les empreintes des deux blocs de consigne ;
2. **le corps exact de chaque envoi** (octets envoyés au relais) et son empreinte ;
3. **chaque réponse entière, telle que reçue du relais** : en-têtes (identifiant de requête, modèle servi) et corps, réponses d'erreur comprises, flux partiels d'un envoi coupé ; pour Claude, les blocs de réflexion tels qu'ils viennent ; pour Carbon, la réponse recomposée par le relais, sans retrait (5.3) — dans le sous-dossier `reponses-brutes-non-lues/` ;
4. les journaux des trois relais, leur état final (`/relais/etat`) et leurs consoles ;
5. les sorties du programme de conformité, le journal de l'essai, l'inventaire, le rapport.

Ne pas verser : la liste locale des interdits de la garde G5 ; seule son empreinte va au manifeste.

- Chaque envoi écrit sa ligne au journal, vidée sur le disque, **avant** de partir ; chaque réponse est écrite, vidée sur le disque, **avant** d'être analysée.
- À toute fin — normale, arrêt par une garde, signal, panne — l'inventaire liste tout fichier produit, avec taille et empreinte. **Aucune suppression** avant que l'inventaire scellé soit vérifié sur disque et par empreinte (R11) et poussé. Une file interrompue est rapportée telle quelle ; elle n'est pas rejouée sans nouvelle ligne.
- Les relais s'arrêtent par leur identifiant de processus (R10), consigné dans `registres/arrets.md`.

### 8.3 Qui peut lire les réponses
- **Des programmes seulement**, nommés à l'avance : le programme de conformité de forme, la lecture des compteurs, et le contrôle que le rapport ne contient aucune sous-chaîne des réponses.
- **Aucun agent ni aucune personne avant le scellement du texte du bras A** : les verdicts des lecteurs sur des cas appariés ou désappariés par construction sont un essai de la validité de l'instrument ; les lire pourrait orienter la consigne ou les seuils du texte encore ouvert.
- **Après le scellement**, tout réemploi dans une mesure passe par un texte contre-lu et le mot de Lazar.
- **Exception de diagnostic** : si la conformité échoue en masse sur une cause que le programme ne classe pas, Lazar peut permettre un regard sur la seule forme, par un agent qui n'écrit ni le texte du bras A ni sa consigne, consigné au journal.

## 9. Gardes — chacune éprouvée sur un cas sain et sur un artefact, contre un faux fournisseur local, sans aucun appel payant (R5)

| garde | ce qu'elle fait | cas sain | artefact |
|---|---|---|---|
| **G1 plafond de dépense, avant l'envoi** | le chef d'essai tient un compteur par modèle et par file : il refuse l'envoi si le cumul compté plus le pire cas de cet envoi (corps réel, un jeton par octet, sortie maximale envoyée, prix comptés de 6.1) dépasse le plafond ; un envoi sans compteur lisible (délai, coupure) est compté au pire cas. En plus : relais Claude `--modeles-permis claude-sonnet-5-5,claude-opus-5-5,claude-haiku-5-5 --plafond-usd 9.25 --reserve-par-appel 0.27` (avec l'option Fable 5.2 : modèle ajouté, plafond 15,25, réserve 0,65) ; relais d'OpenAI `--plafond-usd 2.50` ; relais de Google `--max-appels 97`, sans plafond en dollars | cumul 1,00, plafond 6,00 : l'envoi part ; **éprouvé sur les trois formes d'appel, celle de Google comprise** | cumul à 0,01 du plafond : refus, le faux fournisseur ne reçoit rien, la file s'arrête, code de sortie non nul ; même essai sur la forme de Google |
| **G2 délai d'attente** | par envoi : Claude et GPT, 240 secondes de silence et 600 au total (l'affichage de la réflexion étant omis, le flux reste muet pendant la réflexion, et un envoi coupé est facturé quand même) ; Carbon, 120 et 180 ; une seule reprise ; trois délais de suite arrêtent le réglage ; délai global de 4 heures par file | faux fournisseur qui répond en 2 secondes : relevé | faux fournisseur muet (délais raccourcis pour l'essai) : coupé, compté au pire cas, reprise unique, puis arrêt |
| **G3 sortie maximale** | le corps de chaque envoi porte la sortie maximale du tableau 5.1 ; un envoi sans elle, ou plus haute, est refusé avant de partir ; une réponse dont les compteurs dépassent la borne comptée arrête la file (pour Carbon, c'est le cas « à un envoi près » de 6.3) | corps conforme : part | corps sans sortie maximale, puis à 32 768 : refus ; réponse de Carbon à compteurs au-delà de 4 096 + le budget : arrêt de la file, dépassement consigné |
| **G4 refus** | **refus de compte** : code 401, 402, 403 ou 429 rendu par l'amont, ou 402 et 429 rendus par un relais (plafond, borne d'appels, corps trop gros : motif lu dans le corps de la réponse du relais et écrit au journal, distinct d'un refus de l'amont) ; il arrête toute la file du fournisseur, sans reprise. **Refus de contenu** : motif de fin de refus ou de filtrage (`refusal` chez Claude, motif de sécurité chez Carbon, `content_filter` chez GPT) ; il arrête tous les réglages **de ce modèle**, sans reprise, et les autres modèles de la file continuent. **Modèle servi autre** que le modèle demandé : arrêt de la file. **Surcharge** (500, 502, 503, et 529 chez Anthropic) : elle consomme la reprise unique ; une seconde arrête le réglage. **Code 400** : arrêt de la file, sauf le refus de la température (5.5). Les autres files continuent | réponse 200, motif de fin normal : la file continue | réponse 429 de l'amont : arrêt de la file ; 429 du relais (borne d'appels) : arrêt, motif « relais » au journal ; réponse 200 à motif de refus pour Haiku 5.5 : Haiku 5.5 s'arrête, Sonnet 5.5 et Opus 5.5 continuent ; modèle servi différent : arrêt ; 529 puis 529 : une reprise, puis arrêt du réglage ; 400 nommant la température : retirée, la file continue ; autre 400 : arrêt |
| **G5 rien de personnel dans ce qui part** | avant chaque envoi, le corps et les en-têtes sont comparés à une liste d'interdits tenue dans un fichier local jamais envoyé ni versé (noms de personne, nom du projet et du dépôt, chemins du poste, formes d'identifiant de session, forme de courriel) ; agent d'utilisateur générique ; aucun champ d'identité d'utilisateur ; l'identifiant de l'entrée n'est pas dans le texte ; le lot d'entrées est relu par empreinte | entrée synthétique : part | entrée où l'on a glissé un courriel, puis un chemin du poste, puis un identifiant de session : refus à chaque fois |
| **G6 clés par leur nom, jamais écrites** | relais lancés par `scripts/lancer_relais_local_v1.py`, clé exigée par son nom (`!GEMINI_API_KEY` pour Carbon ; pour Claude, le nom que Lazar dira ; pour GPT, le secret de réseau de l'environnement, aucune valeur dans le conteneur) ; le chef d'essai n'a aucune clé dans son environnement et ne parle qu'à la boucle locale ; journaux, manifeste et réponses versées sont relus par programme pour toute chaîne de la forme d'une clé | clé factice dans l'environnement du seul relais : le relais part, aucun fichier ne la porte | nom exigé absent : rien ne part ; clé factice glissée dans un journal : le contrôle la trouve et arrête |
| **G7 ligne de calcul, par file** | chaque file exige `GO_ID` d'une ligne valide de `registres/go.md` qui la nomme, et l'empreinte du devis accepté ; aucune file ne part avant | identifiant valide : la file part | identifiant absent, ou d'une ligne qui ne nomme pas cette file : rien ne part |
| **G8 clé Claude posée et vérifiée** | la file Claude exige : (1) la variable de clé nommée à la configuration, présente et non vide dans l'environnement du relais ; (2) une attestation scellée de l'appel minimal de vérification (sa ligne de calcul, code 200, modèle servi, date), dont l'empreinte est citée à la configuration. Sinon la file Claude ne part pas ; **les files Carbon et GPT ne l'attendent pas** | variable présente et attestation valide : la file Claude part | variable absente ; attestation absente ; attestation d'un autre nom de variable ou d'empreinte fausse : la file Claude ne part pas, motif au journal ; dans le même essai, les files Carbon et GPT partent |

**Aucune reprise cachée** : le chef d'essai appelle les relais par la bibliothèque standard (`http.client`), sans bibliothèque cliente des fournisseurs ; si l'une est employée, ses reprises automatiques sont coupées (`max_retries=0`). Un essai le vérifie contre le faux fournisseur (une réponse 429, puis une réponse 500 : un seul envoi reçu chaque fois). Les trois relais ne reprennent pas d'eux-mêmes (contre-lecture, point 1).

Aucun repli silencieux : toute garde qui coupe écrit son motif au journal et rend un code de sortie propre.

## 10. Code à écrire, et qui le contre-lit

| fichier | rôle |
|---|---|
| `scripts/fabriquer_entrees_essai_mesure_v1.py` | lexique inventé, gabarits, trois cas, blocs, 24 entrées, graines, extraction des deux consignes du brouillon 5 avec leur empreinte |
| `scripts/essai_mesure_lecteurs_v1.py` | chef d'essai : trois files, corps des trois fournisseurs, gardes G1 à G5, G7 et G8, journal, écriture des corps d'envoi et des réponses brutes ; appels par la bibliothèque standard (`http.client`), sans bibliothèque cliente des fournisseurs ; si l'une est employée, ses reprises automatiques sont coupées (`max_retries=0`), car une reprise cachée ferait un troisième envoi facturé que ni le compteur ni le pire cas ne voient ; un essai le vérifie contre le faux fournisseur (une réponse 429 puis 500 : un seul envoi reçu chaque fois) |
| `scripts/conformite_forme_lectures_v1.py` | conformité de forme, oui ou non et code de cause, sans rien rendre du texte |
| `scripts/inventorier_essai_mesure_v1.py` | inventaire, versement, scellement |
| `scripts/rapport_essai_mesure_v1.py` | tableau des champs techniques, moyennes par longueur, maximum, coût projeté avec redemandes, règle de la section 7, contrôle « aucune sous-chaîne des réponses » |
| `scripts/faux_fournisseur_essai_mesure_v1.py` | faux amont local des trois formes d'appel |
| `tests/test_essai_mesure_lecteurs_v1.py` | cas sain et artefact de chaque garde ; essai de bout en bout contre le faux fournisseur |
| configuration `essai-mesure-lecteurs-bras-a-v1.json` | modèles, réglages, champs exacts des corps, sorties maximales, prix, plafonds par file et par modèle, délais, options des relais, variable de clé de chaque file ; scellée avant la ligne |

Relais repris sans changement : `relais_reel.py` (Claude), `relais_gemini_v3.py` (Google), `relais_kimi_v4.py` avec l'amont d'OpenAI ; lanceur `scripts/lancer_relais_local_v1.py`.

**Contre-lecture.** Ce devis (classe A) : contre-lecture complète, faite sur le brouillon 1 ; le contre-lecteur vérifie les corrections sur cette version. Le code (classe B, GO-2026-11-19-26) : contre-lu par un sous-agent neuf d'un autre modèle de la même famille que son auteur, à qui l'on donne la liste des fichiers ; **puis vérification des corrections par le même contre-lecteur**. Le rapport de l'essai est relu par un agent qui n'a écrit ni le code ni ce devis.

## 11. Avant la ligne de calcul (rien de payant)

1. Mot de Lazar qui décide l'essai : GO-2026-11-19-22 (fait).
2. Vérification des corrections de ce devis par le contre-lecteur.
3. Pages de prix : versées ce jour dans `docs/sources/prix-fournisseurs-2026-11-19/` (Anthropic, Google) ; **à sceller** ; OpenAI non lisible ce jour, page scellée du 18 novembre gardée.
4. Code écrit, essais des gardes passés, contre-lecture du code et vérification de ses corrections.
5. Lot d'entrées et configuration scellés.
6. Ligne de calcul inscrite dans `registres/go.md`, qui nomme les files accordées, leurs plafonds, la variable de clé de chacune et le compte qui paie ; ligne d'engagement par file dans `registres/depenses.md`.
7. **File Claude seulement** : clé posée par Lazar, vérifiée par l'appel minimal sous sa ligne à part ; attestation scellée (garde G8).

## 12. Traitement de la contre-lecture du brouillon 1

### 12.1 Corrections

| point | traitement | où |
|---|---|---|
| **C1** résumés de pensée de Carbon gardés ; réponse « telle que reçue du relais », corps d'envoi gardé, poussé avant suppression | **appliqué**, texte « après » repris ; `--max-appels` porté de 96 à 97 pour l'envoi d'essai de la température | 5.3 ; 8.2 |
| **C2** trois conditions du plafond ; un envoi de Carbon près ; prix de repli | **appliqué** ; la phrase « ne peut pas dépasser » est retirée ; le pire cas est recalculé par octet (50,09 au lieu de 44,96) ; Carbon au prix de repli tant que sa page n'est pas scellée, chiffré à part | 6.1 ; 6.2 ; 6.3 ; 6.4 |
| **C3** aucune reprise cachée | **appliqué**, texte « après » repris | 9 ; 10 |
| **C4** refus de compte, de contenu, des relais ; surcharge, 529 | **appliqué**, texte « après » repris ; ajout du code 400 et de l'exception de la température | 9, G4 |
| **C5** GO-2026-11-19-22 cité, écarts déclarés | **appliqué** ; lettre recopiée de la ligne 455 du registre de la branche principale ; l'écart « 17,75 dépasse quelques dollars » est aussi à la page de tête et à la ligne proposée | 0 ; 1 ; 6.4 ; 11 |
| **C6** compteurs définis, envoi qui compte, sortie maximale, parti pris | **appliqué** ; sortie maximale = la plus grande de 8 192 et de quatre fois le maximum observé ; partis pris écrits comme tels | 7.3 |
| **C7** « ramenée à un quart » restreint aux textes synthétiques | **appliqué**, texte « après » repris | 4.4 |

### 12.2 Recommandations

| point | traitement | où |
|---|---|---|
| **R1** ordre des réglages et blocs d'entrées | **appliqué** | 4.3 ; 5.1 |
| **R2** redemandes de forme dans le coût projeté | **appliqué** | 7.3, notations |
| **R3** réglages des relais à la configuration | **appliqué** ; Fable 5.2 aligné en comptant 10 et 50 partout | 6.1 ; 9, G1 ; 10 |
| **R4** champs exacts des corps Claude | **appliqué** | 5.2 |
| **R5** délais de Claude à 240 et 600 secondes | **appliqué**, étendu à GPT (même flux muet pendant le raisonnement) | 9, G2 |
| **R6** cas partiellement apparié | **appliqué** : trois cas × trois longueurs × deux tirages, à nombre d'entrées égal | 4.2 ; 4.3 |
| **R7** température et raisonnement de Carbon et de GPT | **appliqué** selon le brouillon 5 : température 0 si le service l'accepte ; raisonnement de GPT au défaut, relevé, le texte n'ayant pas tranché | 5.5 |
| **R8** vérification des corrections du code par le même contre-lecteur | **appliqué** | 10 |
| **R9** empreintes des consignes comparées au scellement | **appliqué** ; consignes extraites du brouillon 5 | 4.2 |

### 12.3 Autres changements depuis le brouillon 1
- Files séparées par fournisseur, plafond par file, garde G8 de la clé Claude ; case « poche des appels Claude » remplacée par la réponse de la session mère (5.6).
- « Il ne remplace pas l'épreuve de forme » est retiré : selon le brouillon 5, l'essai en tient lieu.
- Qui peut lire les réponses (8.3), repris du point 4 de la contre-lecture.

## 13. Points où je doute

1. **Clé de GPT** : je n'ai pas vérifié comment le relais compatible OpenAI se lance quand la clé est un secret de réseau et non une variable (une course du 18 novembre a payé Astra « sur la clé du fournisseur injectée par le réseau » : `registres/depenses.md`, ligne 522). La forme exacte est à reprendre du lanceur de cette course, que je n'ai pas ouvert, et la garde G6 à écrire en conséquence.
2. **Budget de réflexion de Carbon, borne dure ou non** : non établi ; d'où « à un envoi près ». De même, je ne sais pas si sa sortie maximale comprend la réflexion ; le pire cas additionne les deux.
3. **Compteur de réflexion de Claude** : rendu à part ou non, je ne sais pas ; la sortie totale, seule utile au coût, est rendue.
4. **Température 0 pour Carbon et GPT** : acceptée ou non, inconnu ; la règle de 5.5 couvre les deux cas, au prix d'un envoi refusé sans frais.
5. **Lectures des pages de prix** : faites par programme sur le texte sans balises ; la page d'Anthropic est en longues lignes, sans numéro de ligne à citer. À vérifier par celui qui scelle. Page d'OpenAI non lisible (403).
6. **Longueur « 400 jetons » tenue en caractères** : écart possible d'un quart.
7. **Textes à gabarits**, même avec le cas partiel : sans doute plus faciles que de vraies actions ; la moyenne mesurée peut sous-estimer la réelle.
8. **« Le plus capable d'avant le dernier »** lu comme Opus 5.5 ; Fable 5.2 reste en option.
9. **Aucun contrôle par programme** que les entrées ne recoupent pas une tâche réelle (il faudrait lire les tâches) ; la contre-lecture ne l'a pas demandé.
10. **Vérification de la clé Claude** : sa ligne de 0,01 dollar est hors de ce devis ; la forme de l'attestation exigée par G8 est de moi.

## 14. Contre-lecture

Brouillon 1 contre-lu (`d1b8ad89037c…`). Ce brouillon 2 attend la vérification de ses corrections ; il n'est pas scellé.
