# Rapport du développeur : collisionneur v9, version 3

Écrit le 20 novembre 2026 par le développeur de la v1 et de la v2 (Claude Opus 5.5), sous l'accord GO-2026-11-20-54. Pièce de classe B : le code doit être contre-lu par un autre modèle, puis le même contre-lecteur vérifie les corrections, avant tout appel. Aucun appel à un fournisseur, pas même un comptage. Aucune clé lue. Aucune dépense. Aucun commit.

## Pièces

| fichier | empreinte |
|---|---|
| `collisionneur_v9_v3.py` | `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910` |
| `test_collisionneur_v9_v3.py` | `8c38dc2f938db3386f84721830b179d844295a1f46e6db8ba3586ffbe2eabfdc` |
| `commande-reprise-collisionneur-dopamine-v3.txt` | `336744af2c98f9bab543548ff8a27a3826d99ea067458c5e5efc72dff7cc4cac` |

La v2 reste intacte : `2357b9e8…` pour le script et `69faf8c4…` pour les essais, sceaux vérifiés. Le run `runs/collisionneur-dopamine-v1-20261120-122457/` n'est pas touché : tout le travail s'est fait sur des copies, dans le bloc-notes.

## Ce que la v2 savait déjà faire pour la reprise, relu dans le code

- **Les cellules valides sont sautées** (`lancer_etage`). Le tour 1 n'est donc pas rappelé.
- **Une cellule arrêtée est relancée**, sauf en cas de refus. Son statut `ENTREE_HORS_GARDE` ne bloque pas la relance.
- **L'essai neuf prend le numéro suivant** (`prochain_essai`), et `ecrire_neuf` n'écrase jamais rien. L'essai 1 de `E3-T2-critique-croisee-A` reste en place, et la cellule est rejouée sous l'essai 2.
- **Les faits, la question et la composition sont relus sous leur sceau** (`verser_une_fois`, `sceller_composition`).

**Ce qui manquait.** `verifier` signalait tout changement de script en cours de run comme un problème. Les essais du tour 1 portent l'empreinte de la v2, ceux de la reprise porteront celle de la v3. D'où la reprise déclarée (point 4 ci-dessous). Il n'y avait pas non plus de ligne de dépense distincte du plafond.

## Ce qui change (lignes du v3)

1. **Comptage avant l'envoi.** Il est fait dans `executer_cellule` (l. 1298), après la garde de motifs et avant tout essai, par `compter_entree` (l. 1168).
   - Anthropic : `compter_anthropic` (l. 1120), `POST /v1/messages/count_tokens`, avec le même modèle, le même message et les mêmes en-têtes.
   - Google : `compter_gemini` (l. 1135), `POST models/{m}:countTokens`, avec les mêmes `contents`.
   - OpenAI : `compter_openai` (l. 1147), `POST /responses/input_tokens`, avec le même modèle et la même entrée, et la même restriction d'adresse que l'envoi.
   - Les comptages passent par un transport à part, `TRANSPORT_COMPTE` (l. 655), au moyen d'un paramètre ajouté à `envoyer` (l. 668). Seul le 429 est repris.
   - Kimi n'a pas d'interface de comptage connue du script, car il passe par le relais local. Il garde une estimation prudente à 2 caractères par jeton (l. 136), sous le plus bas relevé du dépôt (2,227). **Ce n'est pas un compte exact.**
2. **Garde et pire cas.**
   - La garde vaut `⌈compte × 1,01⌉ + 32` (`TOLERANCE_COMPTE`, l. 216 ; `garde_entree`, l. 1093).
   - Le pire cas d'un envoi vaut `cout_pire_garde` (l. 1099 et 1304) : la garde au prix d'entrée, plus le plafond de sortie et la provision au prix de sortie.
   - Le compte, la garde, sa source et l'indicateur « par interface » sont consignés dans chaque essai (l. 1330).
3. **Refus avant l'envoi, nommés et consignés** (`refuser_avant_envoi`, l. 1184, entrée `refus_avant_envoi` au journal). Dans chaque cas, rien n'est envoyé :
   - `COMPTE_IMPOSSIBLE`, code 8 : erreur 4xx ou 5xx, connexion, délai, réponse sans entier.
   - `COMPTE_INVRAISEMBLABLE`, code 8 : le compte est inférieur au nombre de caractères divisé par 8 (l. 1178).
   - `PLAFOND`, code 4 (l. 1306).
   - `LIGNE`, code 4 (l. 1309).
4. **Ligne de dépense.** L'option `--ligne-usd` ouvre la ligne une fois, au journal, avec la dépense constatée à l'ouverture (`ouvrir_ligne`, l. 1204, appelée l. 1878). Seule la dépense faite depuis l'ouverture compte contre la ligne. Un autre montant donné plus tard est refusé.
5. **Vérification après coup gardée.** `juger` compare l'entrée facturée à la garde comptée (l. 1279 et 1322). Au-delà, l'arrêt reste `ENTREE_HORS_GARDE`, code 6, comme dans la v2.
6. **Reprise déclarée.**
   - `declarer_script` (l. 1241, appelée l. 1877) refuse, avec le code 1 et sans rien envoyer, un dossier dont les essais portent une autre empreinte de script, sauf si l'option `--reprise` est donnée.
   - Avec `--reprise`, elle consigne au journal `changement_script` (ancienne empreinte, nouvelle empreinte, version).
   - `verifier` suit l'empreinte du script dans l'ordre du journal (`suivre_scripts`, l. 1221 ; appel l. 1577). Un essai passé sous un script non déclaré reste un problème.
7. **Plafond de Fable** : `MAX_FABLE_V3 = 49000` (l. 127). La relance reste à 64 000.
8. **Commande `devis-reprise`** (l. 1688 à 1766 et 1810). Elle calcule, sans réseau, le pire cas des cellules restantes des tours III.2 et III.3, puis cherche le plus grand plafond de Fable qui tient dans le reste de la ligne.

Hors de ces points, seuls changent l'en-tête, `VERSION`, les lignes d'usage, `import math` et une ligne de `ecrire_etat` qui affiche la ligne et les refus avant l'envoi. La différence entre la v2 et la v3 compte 384 lignes.

## Documentation des comptages, lue le 20 novembre 2026

- **Anthropic** (page « Token counting » de platform.claude.com) :
  - « free to use » ;
  - « The token count is an **estimate**. In some cases, the actual number of input tokens used when creating a message might differ by a small amount » ;
  - les jetons ajoutés par le système ne sont pas facturés.
- **Google** (référence `count-tokens` d'aistudio.google.com) : `POST /v1beta/models/{model}:countTokens`, réponse `totalTokens`. La page ne dit rien du prix ni de l'égalité avec `promptTokenCount`. Ses deux exemples donnent d'ailleurs 10 et 11 jetons pour le même texte.
- **OpenAI** (référence « input_tokens » de developers.openai.com) : `POST /responses/input_tokens`, réponse `{"object": "response.input_tokens", "input_tokens": n}`. Le comptage existe donc bien pour l'interface Responses. La page lue ne dit rien du prix ni de l'exactitude.

**Aucun des trois ne promet un compte égal à l'entrée facturée.** C'est la raison de la tolérance : elle coûte environ 0,005 USD par envoi de Fable à 50 000 jetons. Elle évite qu'un écart que la documentation admet n'arrête le passage après paiement. Tout écart plus grand reste pris après coup.

## Plafond de sortie de Fable : calcul

Commande : `devis-reprise runs/collisionneur-dopamine-v1-20261120-122457 --ligne-usd 25.90`, lancée sur une copie, code 0. Les prix sont ceux de la table : Fable 10 / 50, Opus 4 / 20, Argon 10 / 50, Astra 10 / 50, Carbon 4 / 20 USD par million de jetons.

Hypothèses (SUPPOSÉ) :
- Tour III.2 : les prompts sont exacts, reconstruits depuis les cellules scellées. L'entrée est projetée à 2 caractères par jeton, plus la tolérance.
- Tour III.3 : une critique non encore écrite est bornée par le plafond de sortie de son auteur, multiplié par 3 caractères par jeton chez Anthropic et par 4,5 chez Google et OpenAI. On ajoute 200 caractères de balises par pièce.
- À l'envoi, le compte réel remplace la projection.

| cellule | modèle | caractères | garde | sortie + provision | pire (USD) |
|---|---|---|---|---|---|
| E3-T2-critique-croisee-A | claude-fable-5-2 | 106 207 | 53 668 | 49 000 | 2,9867 |
| E3-T2-critique-croisee-B | claude-opus-5-5 | 103 753 | 52 428 | 22 000 | 0,6497 |
| E3-T2-critique-croisee-C | gemini-4-argon | 102 551 | 51 821 | 18 000 + 8 192 | 1,8278 |
| E3-T2-critique-croisee-D | gpt-6.2-astra | 115 896 | 58 560 | 8 000 | 0,9856 |
| E3-T2-critique-croisee-E | gemini-4-carbon | 94 112 | 47 559 | 65 536 + 32 768 | 2,1563 |
| E3-T3-reponse-A | claude-fable-5-2 | 512 971 | 259 083 | 49 000 | 5,0408 |
| E3-T3-reponse-B | claude-opus-5-5 | 596 425 | 301 228 | 22 000 | 1,6449 |
| E3-T3-reponse-C | gemini-4-argon | 582 627 | 294 260 | 18 000 + 8 192 | 4,2522 |
| E3-T3-reponse-D | gpt-6.2-astra | 614 282 | 310 245 | 8 000 | 3,5025 |
| E3-T3-reponse-E | gemini-4-carbon | 377 154 | 190 495 | 65 536 + 32 768 | 2,7281 |

**Total au plafond 49 000 : tour III.2, 8,6061 USD ; tour III.3, 17,1685 USD ; soit 25,7746 USD au pire, sans relance.** Les prompts du tour III.2 ne contiennent aucun motif interdit.

Recherche du plafond, par pas de 1 000 :

| plafond de Fable | pire cas (USD) |
|---|---|
| 22 000 | 21,93 |
| 32 000 | 23,35 |
| 40 000 | 24,49 |
| 48 000 | 25,63 |
| **49 000** | **25,7746, tient** |
| 50 000 | 25,92, dépasse |
| 64 000 | 27,91 |

**Les relances ne tiennent pas dans la ligne.** Si chaque cellule était relancée, le pire cas monterait à 58,53 USD. Une relance n'est donc permise que si son pire cas tient encore dans la ligne et dans le plafond. Sinon, elle est refusée avant l'envoi (`LIGNE` ou `PLAFOND`, code 4), et le passage s'arrête.

## Essais

- **Suite v3 : 151 passés**, hors réseau.
  - Le transport, le transport des comptages, l'horloge et le sommeil sont remplacés par des doublures, et la fixture fait échouer toute ouverture de socket.
  - 117 essais viennent de la v2. Quatre ont été adaptés : la table (Kimi à 2), la garde d'entrée à la tolérance près (Argon ; puis Fable, Astra et Kimi en C4) et le plafond de la première passe de Fable (49 000).
  - 34 essais sont neufs. Chaque garde neuve a un cas sain et un artefact :
    - comptage par interface et dans l'ordre (5 espèces) ;
    - Kimi par estimation ;
    - comptage impossible (4 erreurs × 3 fournisseurs, clé masquée) ;
    - réponse de comptage mal formée (5 formes) ;
    - 429 repris ;
    - invraisemblance ;
    - l'incident du 20 novembre rejoué : un plafond placé entre l'estimation et le compte refuse l'envoi ;
    - vérification après coup ;
    - ligne, deux essais ;
    - reprise d'un run réellement produit par la v2 et arrêté sur `ENTREE_HORS_GARDE` : refusée sans `--reprise` ; avec `--reprise`, les tours 2 et 3 sont rejoués sans le tour 1, l'essai 1 est intact et l'essai 2 ajouté, `verifier` tient, et la même trace privée de la déclaration est signalée ;
    - second lancement sans nouvelle déclaration ;
    - `devis-reprise`, cas sain et artefact ;
    - plafond retenu recalculé sur le run réel, en lecture seule, sans changement des dates de fichiers.
- **Essais v2 sur la v2 : 117 passés.**
- **Épreuves par retrait**, faites sur des copies dans le bloc-notes. Chaque retrait casse au moins un essai :

| retrait | essais en échec |
|---|---|
| comptage retiré | 28 |
| pire cas sur l'estimation | 6 |
| ligne non contrôlée | 1 |
| invraisemblance retirée | 1 |
| vérification après coup sur l'estimation | 2 |
| reprise sans déclaration admise | 1 |
| changement de script ignoré par `verifier` | 1 |
| refus non consigné | 13 |
| Fable rendu à 22 000 | 1 |
| comptage par le transport d'envoi | 87 |
| tolérance retirée | 6 |

- **Simulation de la reprise sur une copie du run réel**, avec des doublures :
  - 10 comptages et 10 envois, le tour 1 sauté, Fable demandé à 49 000 ;
  - `verifier` rend « tout tient » ;
  - `etat.md` affiche la ligne ouverte à 4,10 USD.

## Ce que je n'ai pas fait, et les réserves

- **Comptage pas tout à fait exact.** Anthropic présente son compte comme une estimation. Google et OpenAI ne disent rien de l'exactitude. La garde est donc le compte plus 1 % et 32 jetons : c'est un écart à la lettre de la demande (« compte exact »). Sans tolérance, il suffit de supprimer `TOLERANCE_COMPTE`, et l'épreuve par retrait montre que les essais suivent.
- **Gratuité des comptages.** Elle n'est lue que chez Anthropic. Les pages de Google et d'OpenAI n'en disent rien, et les comptages ne sont pas comptés dans la dépense.
- **Comptage de Google.** Il porte sur `contents` seuls, sans `generationConfig`. Le budget de réflexion ne devrait pas changer l'entrée, mais ce n'est pas vérifié. La tolérance et la vérification après coup couvrent un petit écart.
- **Version d'interface d'Anthropic.** La v3 garde `anthropic-version: 2023-06-01`, comme pour l'envoi. Les exemples publics portent `2026-10-21`.
- **Kimi et Jev ne sont pas comptés par une interface** : Kimi est estimé à 2 caractères par jeton, Jev reste à 3 comme dans la v2. Ni l'un ni l'autre n'est dans ce run.
- **La commande `devis` de la v2 reste estimée par les caractères.** Seul `devis-reprise` est neuf.
- **Opus reste à 22 000 jetons de sortie.** Sa critique du tour III.2 pourrait être coupée comme celle de Fable. La relance à 64 000 n'aurait lieu que si elle tient dans la ligne.
- **Garde de motifs.** Les textes des critiques réelles du tour III.2, qui entreront au tour III.3, n'existent pas encore : la garde de motifs peut encore arrêter le passage (code 7).
- **Un essai copié de la v2 garde une estimation par les caractères** : `test_garde_a_provision_comptee_avant_l_envoi`. Il passe parce que sa marge de 0,001 USD dépasse l'effet de la tolérance. Je ne l'ai pas réécrit.
- **Nom de la clé.** La commande de reprise porte `NOM_CLE` : je ne connais pas le nom de variable choisi par la mère, ni la clé qui a du crédit.
- **Fichiers exclus de git.** `.git/info/exclude` contient `docs/notes/collisionneur-v9/*v3*` : les fichiers v3 n'apparaissent pas dans `git status`. Je n'y ai pas touché ; c'est à la mère de les verser.
- **Ni contre-lecture, ni commit, ni poussée.**
