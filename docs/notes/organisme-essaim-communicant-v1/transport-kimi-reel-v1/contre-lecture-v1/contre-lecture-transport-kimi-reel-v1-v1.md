# Contre-lecture du transport Kimi réel v1 — v1

- Contre-lecteur Opus neuf (Claude Opus 5.5), 22 novembre 2026 ; aucune pièce écrite par moi. Aucun appel au fournisseur, aucune dépense ; `essai_fumee_kimi_v1.py` lu, jamais lancé sur Kimi (répété à blanc sur le faux serveur local seulement). Serveurs d'épreuve sur 127.0.0.1 à 127.0.0.3, clé factice créée pour l'épreuve. Rien n'est écrit dans le dépôt (`git status` vide après les rejeux). Aucun refus d'outil ni de classifieur.
- Pièce : `docs/notes/organisme-essaim-communicant-v1/transport-kimi-reel-v1/`. Les sept compagnons `.sha256` concordent ; `SHA_TRANSPORT` de l'adaptateur strict (`4bba649c…aa5a6`) égale l'empreinte du fichier.
- Mes sorties (dans ce dossier) : `outils/attaques_transport_kimi_cl_v1.py`, `attaques-transport-kimi-cl-v1.json`, `attaques-transport-kimi-cl-v1.stdout`, `rejeu-pytest-81.txt`, chacun avec son compagnon `.sha256`.

## Verdict

**Conforme avec réserves.** Le transport tient son contrat sur tout ce qui vient de l'amont par le fil, sauf deux points d'usage (N5, N6). Deux points sont **bloquants pour la fumée**, tous deux dans `essai_fumee_kimi_v1.py` et de petite taille : le journal ne garde pas ce que H2 doit établir, et le plafond de 1 USD n'est pas dur.

## 1. Rejeu des 81 épreuves

`env -u KIMI_API_KEY …/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider test_transport_kimi_reel_v1.py`, lancé depuis le dossier de la pièce : **81 réussies** (51,5 s et 53,0 s, deux rejeux), ce qui est identique à `test-transport-kimi-reel-v1-pytest.txt`. Aucun `__pycache__` créé.

## 2. Attaques neuves (21 artefacts, `attaques-transport-kimi-cl-v1.json`)

| n° | attaque | résultat | lecture |
|---|---|---|---|
| N1 | 307 vers un autre hôte (127.0.0.3) | `ErreurTransportFatale` ; 1 requête ; 0 vers l'autre hôte | tenu |
| N2 | 429 avec `Retry-After: 30` | `ErreurFournisseur` en 0,0 s ; 1 requête | tenu (aucune attente, aucune relance) |
| N3 | deux appels sur un même transport | 2 ports client distincts, 2 requêtes, 2 envois mesurés | tenu (connexion neuve) |
| N4 | `text/event-stream` annoncé, corps JSON entier | `ErreurFournisseur` (pas de `[DONE]`) | tenu |
| N5 | `usage` dans un morceau intermédiaire, contenu ensuite | **accepté** : sortie 60 pour environ 150 mots rendus après | **faille** : sous-compte accepté sous le seuil de 12 octets par jeton |
| N6 | deux `usage` (1 900 puis 5 jetons de sortie) | **accepté, le dernier gagne** : sortie 5 | **faille** : sous-compte de 1 895 jetons |
| N7a | réflexion dans un champ inconnu, `total_tokens` cohérent | sortie 10 ; champ ignoré | limite déjà déclarée (§ 6 du LISEZMOI) |
| N7b | réflexion visible seulement dans `total_tokens` | sortie 1 510 | tenu (excédent ajouté) |
| N8 | autre modèle au seul dernier morceau (celui de l'usage) | `AnomalieReponse` | tenu |
| N8b | `model: null` au milieu du flux | toléré | sans effet |
| N9a | une ligne de 2 Mo | `AnomalieReponse` (morceau illisible) | tenu |
| N9b | flux sans fin, `taille_max` à 200 000 octets | `AnomalieReponse` à 200 540 octets | tenu |
| N10 | amont qui ignore `max_tokens` = 16 et rend 400 ko | lu jusqu'au bout ; usage refusé à la fin (réserve) | **aucune coupure en cours de flux** (voir B2) |
| N11a | clé renvoyée dans `id` | `id_reponse` du diagnostic contient la clé, non masquée | à noter : le journal de la fumée l'écrit |
| N11b | clé renvoyée dans `model` | clé dans `modele_servi` et dans le message de l'exception | à noter (même cause) |
| N11c | clé dans le `code` d'erreur, coupée par `_court` | 8 premiers caractères de la clé présents | à noter : `_court` tronque à 80 **avant** `_masquer` |
| N12 | `http.client.HTTPConnection.debuglevel = 1` (global) | **clé écrite sur la sortie standard** | à noter : aucun `set_debuglevel(0)` explicite |
| N13 | `tr._p` réécrit après la construction vers `http://127.0.0.2` | requête envoyée, **clé en clair** chez un hôte refusé à la construction ; adaptateur strict satisfait | à noter : attributs d'instance non revérifiés |
| N14 | `T.MODELE` réécrit (`kimi-k3.1-pro-highspeed`) | autre modèle envoyé, adaptateur strict satisfait | à noter : globales du module non figées |
| N15 | `HTTPConnection.send` doublé sur une seconde prise | **2 POST reçus, 1 envoi mesuré**, `tentatives` = 1 | à noter : le compteur ne voit que `putrequest` |
| N16 | filtre des noms | « Ćirić » accepté, « Lаzar » cyrillique accepté, UUID de session accepté ; « Lazar », « CIRIC », `session_…` refusés | à noter |
| N17 | corps des six appels de la fumée | champs : `model`, `messages[0].role/content`, `max_tokens`, `stream`, `stream_options.include_usage` | tenu |
| N18 | mandataire local qui répond 407 | 1 seul CONNECT, clé absente du CONNECT ; classé `ErreurFournisseur` (relançable) | à noter : un 407 devrait être fatal |
| N19 | fumée à blanc : usage sans détail (f1), `prompt` de 40 000 jetons (f3) | f1 : `usage_numerique` nul, motif du refus absent ; f2 : la valeur du détail de réflexion n'est pas au journal ; f3 : coût 0,083 > réserve 0,040, **la course continue** (f4 à f6) | **B1 et B2** |
| N20 | amont `http://127.0.0.1.exemple.invalid` | passe le contrôle de GO (préfixe), puis exception non rattrapée de la construction ; aucun envoi | à noter |

- N12 à N15 demandent du code hostile **dans le même processus**. L'adaptateur strict ne couvre que la classe du transport et ses méthodes ; il ne couvre ni les globales du module, ni les attributs d'instance, ni `http.client`, ni `A.AdaptateurChatCompletions.appeler`. Son docstring et le LISEZMOI (§ 2) devraient le dire.
- Sous-classe de l'adaptateur strict : le lanceur v2 l'admet toujours (`isinstance`, déjà N5 de la vérification v4). Le LISEZMOI le déclare (§ 6).

## 3. Corps envoyé

- La liste blanche tient (N17, plus l'épreuve du cas sain) : rien d'autre ne part que `model`, un message `user`, `max_tokens`, `stream`, `stream_options.include_usage`.
- En-têtes : `Host`, `Content-Type`, `Accept`, `Accept-Encoding: identity`, `User-Agent: transport-pilote/1`, `Content-Length`, `Authorization`. Aucun nom, aucune session.
- Les six textes de la fumée sont fixes, générés par graine : ils ne contiennent aucun nom de personne ni aucun identifiant.
- Le filtre est étroit (N16) : il ne retire pas les accents (passer par une forme NFKD avant `casefold`), il ne voit pas les homoglyphes, ni l'UUID nu de la session. Sans effet sur la fumée ; à élargir avant le pilote si des textes y entrent d'ailleurs.

## 4. Essai de fumée (code et LISEZMOI lus)

**Les six appels et H1 à H4.**
- **H2** (f2) : la vérification est juste (fin `length`, sortie adaptée ≤ 16, rien au premier niveau). Mais la question de la pièce « à faire » est aussi : **dans quel champ** la réflexion est rendue. Or le journal ne garde que les entiers du premier niveau (`usage_numerique`). `completion_tokens_details.reasoning_tokens` et `prompt_tokens_details.cache_write_tokens` n'y sont jamais, et `cached_tokens` seulement par `cache_lu`. Si l'usage est refusé, sa forme est perdue, et le motif (`usage_refuse`) aussi (N19) → **B1**.
- **H3** (f1, f3, f4, f6) : la vérification est juste, à trois tailles. Mais une violation n'arrête rien (N19).
- **H4** (f5) : seule la coupure côté client est éprouvée. La facturation d'un 429 ou d'un 5xx ne l'est pas (on ne peut pas la provoquer) : c'est à dire dans le LISEZMOI. La réserve « réponse en moins de 4 s » est déjà déclarée.
- **H1** (f6) : elle ne se tranche qu'au rapprochement, comme le script le dit. Le détail par requête n'est disponible qu'à J+1 (voir § 5).
- `reasoning_effort` vaut `max` par défaut pour `kimi-k3.1-pro` (`api_chat.md` l. 1010-1020). f1, f3 et f4 finiront donc sans doute à `length` (2 000 jetons) : c'est sans danger pour le coût, mais il faut le savoir à la lecture.

**Le plafond de 1 USD n'est pas dur → B2.**
- Il n'est contrôlé qu'avant l'appel, sur la réserve. Le registre ne le fait pas respecter (`registre_depense_v1.py` ne compare jamais au plafond).
- Un coût réglé au-delà de sa réserve n'arrête pas la course : en N19, f3 coûte 0,083 pour une réserve de 0,040, et f4 à f6 partent quand même.
- Le transport ne coupe pas un flux qui dépasse `max_tokens` (N10).
- `max_tokens` est « deprecated » (`api_chat.md` l. 1077-1080). S'il était ignoré, le défaut est de 131 072 jetons (l. 1086-1087), soit jusqu'à 1,31 USD pour **un seul** appel. Or f1 passe avant f2.
- Corrections minimes :
  1. arrêt 16 dès qu'un coût réglé dépasse sa réserve, ou une sortie dépasse `max_tokens` ;
  2. coupure côté client quand le texte rendu dépasse 12 × `max_tokens` octets ;
  3. f2 en premier.
- Sinon, le GO doit dire que la seule borne dure de la fumée est le solde prépayé, et ce solde doit être petit.

**Réserve de 0,2023 USD.** Je la recalcule : **0,202338 USD**, au tarif relu le 22 novembre (2,00 / 10,00, égal aux prix gelés ; `lecture-tarif-et-limite-kimi-v1.md`, compagnons concordants). L'empreinte du plan est `6670d481…ac9dc8`, et elle concorde. Elle est juste sous H2 et H3. L'écriture du cache n'ajoute rien : `cache_write_tokens` fait partie de `prompt_tokens` (`api_chat.md` l. 273), et le palier de 5 minutes est au prix de l'entrée. Même s'il s'ajoutait, le total serait de 0,3045 USD.

**Points mineurs de la fumée.**
- Les pièces v4 importées par `DOSSIER_DEVIS_V4` ne sont pas vérifiées à leur empreinte (les épreuves le font, l'essai non).
- `GO_ID` n'est vérifié que par sa forme.
- Le contrôle `startswith("http://127.0.0.1")` laisse passer un préfixe (N20, sans envoi).
- La commande du LISEZMOI met la clé dans les arguments de `env` le temps de l'`exec`.

## 5. Points « à relever chez le fournisseur » (LISEZMOI § 5) : ce que disent les pièces déjà gardées

Documentation gardée : `relais-kimi-v1/doc-moonshot-lue-2026-10-30-v1/`, compagnons concordants.

| point | lisible dans ce qu'on a ? | où |
|---|---|---|
| 1. réflexion comptée et facturée | **en grande partie** : les exemples donnent `reasoning_tokens` compris dans `completion_tokens` (l. 205, 229, 483) ; les postes facturés sont l'écriture du cache, l'entrée et la sortie, sans poste de réflexion (`guide_kimi-k3-1-pro-quickstart.md` l. 480) ; « reasoning_content counts toward token consumption » (`guide_use-thinking-models.md` l. 527) | la phrase « seulement par `completion_tokens` » manque. Attention : la l. 236 citée par le LISEZMOI vise `kimi-k2.7-code` et `kimi-k2.6`, pas `kimi-k3.1-pro` |
| 2. relances et facturation des requêtes coupées, 429, 5xx | **non** (seul l'usage de fin peut manquer si le flux est interrompu, l. 1181-1183). L'index `llms.txt` signale des pages non gardées : « List interrupted requests » (`finish_reason = 'client_disconnected'`, l. 65), « List request details » (par requête, J+1, l. 64), « Common Error Codes » (l. 41), « Automatic Reconnection » (l. 26, côté client) | à relever |
| 3. modèle servi | **en partie** : la signature `X-Msh-Request-Nonce` porte sur le modèle **de la requête** (l. 560-613), donc elle prouve le traitement par Kimi, pas le modèle exécuté ; `kimi-k3.1-pro-highspeed` partage le même schéma (l. 646-659) | à relever |
| 4. `max_tokens` contre `max_completion_tokens` | **oui pour le texte** : déprécié (l. 1077-1080) ; la baisse automatique ne fait que baisser (l. 1088-1093) ; honoré à l'essai réel du 30 octobre (16 / 13, sans flux) | son maintien n'est pas garanti : plaide pour B2 |
| 5. champ `n` | **oui** : absent du schéma (aucune propriété `n`) | clos |
| 6. cache | **oui** : écriture par défaut au palier de 5 minutes (l. 244-246, et `prompt_cache_options`) ; `cached_tokens`, `cache_write_tokens` et le reste se somment à `prompt_tokens` (l. 273) ; prix relu le 22 novembre | clos |
| 7. tarif | **oui** : relu et daté le 22 novembre, égal | clos ; le LISEZMOI est à mettre à jour |

- **À remonter au directeur.** La note du tarif dit « aucun plafond de dépense réglable ». Or `llms.txt` liste « set project budgets » (l. 38) et « Get project spend limit — daily/monthly consume limits » (l. 91). Une limite de projet pourrait donc tenir la borne de 204 USD mieux que le solde. La page n'est pas gardée : à relever.
- Aucune des pièces ne décrit le flux réel de `kimi-k3.1-pro` tel que ce transport le lit. L'essai du 30 octobre était sans flux : f1 sera le premier flux réel.

## Bloquant pour la fumée
- **B1.** Journaliser toutes les feuilles entières de `usage` (imbriquées comprises) et `diagnostic.usage_refuse`. Sinon H2 (le champ) et la forme d'un usage refusé sont perdues, et l'appel payé est à refaire.
- **B2.** Rendre le plafond dur (les trois corrections du § 4), ou bien écrire dans le GO que seule la limite chez le fournisseur borne la fumée.

## À noter (avant le pilote, non bloquant pour la fumée)
- N5 et N6 : n'accepter qu'**un** `usage` non nul, au dernier morceau avant `[DONE]`, avec `choices` vide (forme documentée, l. 216 et 1176-1181) ; sinon `usage = None`.
- N11 : masquer après la troncature, et masquer `id` et `model`.
- N12 : `set_debuglevel(0)` sur chaque connexion.
- N13 et N14 : revalider l'amont dans `_connexion` et figer les attributs et les constantes. N15 : à déclarer comme limite.
- N16 : normaliser les accents dans le filtre.
- N18 : un 407 du mandataire est fatal.
- LISEZMOI : la citation de la l. 236, le point 7 (le tarif est déjà relu), et la portée réelle de l'adaptateur strict.
- Le journal pourrait garder l'en-tête d'identifiant de requête de l'amont, s'il en rend un, pour le rapprochement.
