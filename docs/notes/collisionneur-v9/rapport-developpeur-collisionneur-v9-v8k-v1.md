# Rapport du développeur : collisionneur v9-v8k (v1)

Pièce de classe B (instrument), à contre-lire par un autre modèle. Développeur : Claude Opus 5.5, 22 novembre 2026.
Mot du directeur : « tous les modèles dans le collisionneur ».

## 1. Fichiers

| Fichier | Empreinte (sha256) | Rôle |
| --- | --- | --- |
| `collisionneur_v9_v8k.py` | `cc886ae7986179274621b74194dca1d1f73943456aac36ee1f58487a7a6b63e7` | script neuf, fabriqué |
| `fabriquer_v8k_depuis_v8j_v1.py` | `66b655696ce3ca0a3633eacd67b4827950282ce7782b5156a1fc56e0f33fe5ea` | remplacements exacts depuis la v8j (chaque ancien texte présent une seule fois, empreinte de la source contrôlée : `d199a14b…`) |
| `test_collisionneur_v9_v8k.py` | `b917d8d17464b172db468a4d23c1b98ac8ca0ff46b37b85b5d186a3feb4069f8` | copie des essais de la v8j (`3e5758e6…`), plus la section v9-v8k |
| `collisionneur_v9_v8j.py` | `d199a14b…` | source, inchangée (vérifiée après fabrication) |

Rien n'est scellé ni commité. Le script des courses en cours (v8d) n'a pas été touché. Aucun processus n'a été touché.

## 2. Changements (et seulement ceux-là)

1. **Trois espèces en fin d'ordre** : `opus46` (`--opus46`), `fable51` (`--fable51`), `mistral` (`--mistral`). Les
   lettres des compositions existantes ne bougent pas (essai sur toutes les combinaisons de 2, 3 et 7 des sept
   anciennes espèces, comparées à la v8j chargée). Lettres jusqu'à J, « dix » au préambule.
2. **Opus 4.6 et Fable 5.1** : même fournisseur et même chemin qu'Anthropic (clé par `--cle-anthropic`, comptage par
   `count_tokens`, flux). Plafonds par défaut alignés sur Opus 5.5 (64 000 / 64 000) et Fable 5.2 (49 000 / 64 000) :
   aucun plafond ne monte sans `--sortie-max`.
3. **Mistral** (`mistral-large-4-0`) : fournisseur neuf. Clé lue dans la variable nommée par `--cle-mistral` (défaut
   `MISTRAL_API_KEY`, préfixe exigé), jamais affichée. Interface `POST /v1/chat/completions` en flux. Modèle servi
   comparé au modèle demandé. Usage lu dans le champ `usage` d'un morceau. Comptage avant envoi par
   `POST /v1/responses/input_tokens`, avec la garde des autres espèces (compte plus 1 % plus 32 jetons). Refus avant
   envoi si la ligne ou le plafond sont dépassés. Aucun renvoi après coupure, délai ou 5xx ; seul le 429 est repris.
   Pensées (morceaux « thinking ») exclues du texte. `finish_reason` : `stop` donne OK ; `length` et `model_length`
   donnent TRONQUE ; `error` ou un flux sans `finish_reason` donnent INTERROMPU, compté au pire ; toute autre fin
   donne ANOMALIE. Aucun `reasoning_effort` n'est envoyé.
4. **Kimi direct** : avec `--kimi-direct` (qui exige `--kimi`), Kimi part vers `https://api.moonshot.ai/v1/chat/completions`
   en flux (`max_completion_tokens`, `stream_options.include_usage`). La clé est lue dans la variable nommée par
   `--cle-kimi` (défaut `KIMI_API_KEY`, préfixe `KIMI_API_KEY` ou `MOONSHOT_API_KEY`). Le comptage passe par
   `estimate-token-count`. La garde d'entrée est le plus grand de deux nombres : le compte avec sa tolérance, ou
   l'estimation à 2 caractères par jeton (Moonshot dit « Estimated »). Sans l'option, le relais local reste le chemin,
   inchangé. Le chemin est inscrit dans chaque essai (`chemin_appel`). Il est aussi inscrit au lancement
   (`options_appel_v8k`) et à l'écran. L'entrée de lancement n'est écrite que si les options changent : une relance
   identique laisse le journal inchangé, comme l'exigeait déjà l'essai d'idempotence de la v7.
5. **`--sortie-max`** (étages et devis) : premier plafond et relance posés au maximum documenté (table
   `SORTIE_MAX_DOCUMENTEE`). Google garde ses limites versées (65 536 en flux) et sa provision. La règle du plafond large
   (`REGLE_TEXTE_MIN`) est revérifiée ; elle tient : texte ≥ 16 384. Le devis compte ces plafonds (essai exact de la
   différence).
6. **`--effort-max`** : la v8j portait un effort global, `EFFORT = "high"`, chez Anthropic seulement. Il est désormais
   porté par chaque espèce : `high` par défaut, ce qui ne change rien, et `max` avec l'option. Chez OpenAI, la v8j
   n'envoie aucun réglage d'effort ni de raisonnement à Astra : rien n'y est ajouté (essai qui le vérifie).
7. **Garde de sortie** : `REFLEXION_HORS_PROVISION` a le sens que lui donne la v9-v7 : sortie facturée au-delà du
   plafond envoyé. Elle couvre maintenant les deux chemins neufs (Mistral, Kimi direct). Le relais Kimi et les anciennes
   espèces n'en sont pas touchés (essai témoin).
8. **Valeurs à fixer** : si une valeur de `VALEURS_A_FIXER` vaut None, la composition est refusée, code 1, avec un
   motif nommé « valeur à fixer ». C'est aussi le cas si `--sortie-max` est donné et qu'aucun maximum n'est documenté.
   Le refus vient avant toute écriture.

## 3. Valeurs lues (pages publiques, lues le 22 novembre 2026, entre 12:05Z et 12:20Z)

| Valeur | Lue | Page |
| --- | --- | --- |
| Opus 4.6 : identifiant, prix, sortie max | `claude-opus-4-6`, 5 / 25 USD, 128K | platform.claude.com/docs/en/models/opus-4-6/overview ; …/about-claude/models/overview |
| Fable 5.1 : identifiant, prix, sortie max | `claude-fable-5-1`, 10 / 50 USD, 128K | platform.claude.com/docs/en/models/fable-5-1/overview |
| Fable 5.2, Opus 5.5 : sortie max | 128K (prix lus 8 / 40 et 4 / 20 ; table inchangée, 10 / 50 et 4 / 20) | …/about-claude/models/overview |
| Effort le plus haut (quatre espèces d'Anthropic) | `max`, par `output_config.effort` | platform.claude.com/docs/en/build-with-claude/effort |
| Astra : sortie max | 128 000 (prix lu 8 / 40 ; table inchangée, 10 / 50) | developers.openai.com/api/docs/models/gpt-6.2-astra |
| Mistral : identifiant | `mistral-large-4-0` (noms « mistral-large-4, mistral-large-4-0, mistral-large-latest ») | docs.mistral.ai/models/mistral-large-4-0.md |
| Mistral : prix | 0,70 / 2,10 USD (page du modèle) ; la page mistral.ai/pricing ne donne que l'exemple « Mistral Large » à 0,5 / 1,5 ; le plus haut est retenu | docs.mistral.ai/models/mistral-large-4-0 |
| Mistral : forme du flux, usage, fins, comptage | voir section 2 | docs.mistral.ai/api/endpoint/chat ; docs.mistral.ai/openapi.yaml (empreinte 7652f130…, non versée) |
| Kimi : serveur, max_completion_tokens, flux, usage final | api.moonshot.ai ; « up to 1048576 » | platform.kimi.ai/docs/api/chat (renvoi depuis platform.moonshot.ai) |
| Kimi : comptage | `/v1/tokenizers/estimate-token-count` → `data.total_tokens` | platform.kimi.ai/docs/api/estimate.md |
| Google : sortie max | 65 536 en flux, limites versées de `garde_google_v3` (aucune relecture neuve) | module, sources citées dedans |

**Non trouvées, laissées à None ou inchangées, jamais inventées** :
- plafond de sortie de Mistral : aucune page de Mistral ne le donne. Des tiers donnent 256K à 262K : non retenu ;
- délai de Mistral : aucune page ne le donne, et aucune autre espèce ne suit ce chemin ;
- ces deux manques font refuser Mistral à toute composition tant que la valeur n'est pas fixée ;
- prix de Kimi : les tables de la page de prix n'ont pas été rendues. La table garde 2 / 10, repris de la v8 ;
- les délais d'Opus 4.6 et de Fable 5.1 (3 600 s) ne viennent d'aucune page. C'est un choix interne, aligné sur le même
  chemin, déclaré dans le script ;
- prix de l'estimation de Moonshot : la page ne dit pas si elle est gratuite.

## 4. Essais

Lancés sous `env -u ANTHROPIC_API_KEY -u OPENAI_API_KEY -u GEMINI_API_KEY -u MISTRAL_API_KEY -u KIMI_API_KEY -u
MOONSHOT_API_KEY -u TYPESAFE_API_KEY`, avec `PYTHONPATH=src .venv/bin/python -B -m pytest -q`. Résultat :
**455 passés, 11 sautés** (les mêmes 11 sautés qu'avec la v8j, qui donne 393 passés). Cela fait 62 essais neufs.

Trois essais copiés sont accordés, marqués « v9-v8k » : la table des identifiants, la différence avec la v3 (ordre,
`NOMS_CLES`, `CAR_SORTIE_MAX`), et « les sept » devenu « les sept premières ».

Les doublures de transport suivent le format de flux documenté : lignes `data:`, fin `data: [DONE]`. Pour Mistral,
l'usage est dans le dernier morceau. Pour Moonshot, il est dans un morceau `choices: []`, après `reasoning_content`.

Chaque garde des chemins neufs a son essai sain et son artefact :
- comptage : impossible, invraisemblable ;
- dépense : plafond, ligne ;
- envoi : coupure, 5xx, délai, erreur dans le flux, flux sans fin, fin `error`, aucun renvoi ; 429 repris ; 400 compté à
  zéro ;
- usage : usage absent ; sortie au-delà du plafond, contre une sortie au plafond exact ; entrée au-delà de la garde ;
- réponse : modèle différent, troncature puis relance, fin inconnue ;
- garde de motifs ; préfixe et absence de la clé ;
- options : `--kimi-direct` sans `--kimi` ; refus avant toute écriture ;
- bout en bout : idempotence du journal, puis changement journalisé.

Les clés ne se retrouvent dans aucun fichier du dossier ni à l'écran.

## 5. Mutations (toutes prises)

Chaque mutant a été écrit dans une copie hors du dépôt et éprouvé par les essais de la section v9-v8k ; le témoin non
muté passe (62). Programme : `/tmp/claude-0/-home-user-controle-ia-travail/cf01708e-9b7d-5868-b0e7-26f697d45137/scratchpad/mutations.py`
(bloc-notes, peut être effacé).

| Mutant | Essai qui le prend |
| --- | --- |
| M1 : `--effort-max` sans effet | effort chez Anthropic |
| M2 : `--sortie-max` sans effet | plafonds documentés |
| M3 : valeur à fixer non contrôlée | refus à la composition |
| M4 : Kimi direct implicite | relais par défaut |
| M5 : garde de sortie retirée des chemins neufs | gardes de dépense |
| M6 : flux sans `finish_reason` accepté | aucun renvoi, sans fin |
| M7 : pensées versées au texte | Mistral sain |
| M8 : erreur dans le flux ignorée | erreur dans le flux |
| M9 : préfixe de la clé de Mistral non contrôlé | clé par son nom |
| M10 : comptage de Mistral retiré | Mistral sain |
| M11 : garde de Kimi direct au compte seul | Kimi direct sain |
| M12 : `model_length` non tronqué | troncature puis relance |
| M13 : options journalisées à chaque lancement | idempotence |
| M14 : Mistral au milieu de l'ordre | fin d'ordre |
| M15 : usage de Moonshot ignoré (`choices` vide) | Kimi direct sain |
| M16 : `--kimi-direct` sans `--kimi` admis | jamais implicite |
| M17 : renvoi après 5xx | aucun renvoi |
| M18 : effort de Fable 5.1 absent | effort chez Anthropic |
| M19 : préfixe de la clé de Kimi non contrôlé | jamais implicite |

## 6. Points ouverts (pour la contre-lecture et la mère)

1. **Mistral ne part pas** tant que son plafond de sortie et son délai ne sont pas fixés. Il faut un mot de la mère :
   soit une valeur lue ailleurs (liste des modèles par l'interface, sans génération, avec une clé), soit une valeur
   déclarée « supposée ».
2. **Modèle servi par Mistral** : la forme de `model` dans le flux n'est pas documentée (l'exemple de la page renvoie
   « mistral-small-latest » pour « mistral-large-latest »). Un autre nom servi arrête au code 3, coût compté : c'est
   voulu, à confirmer par un premier envoi.
3. **Mistral, réflexion** : `reasoning_effort` (none … max) est documenté pour l'interface, pas pour `mistral-large-4-0`.
   Rien n'est envoyé. On ne sait pas si `completion_tokens` comprend les pensées ; la garde de sortie arrête si la sortie
   dépasse le plafond.
4. **Kimi à 1 048 576 jetons** sous `--sortie-max`. Le pire cas monte à 10,49 USD par envoi, au prix de la table. Le
   délai de 2 000 s ne couvre pas une telle sortie : l'envoi serait coupé et compté au pire. Les délais sous
   `--sortie-max` sont à décider. Même question pour Anthropic à 128 000, dans 3 600 s.
5. **Opus 4.6** : son « thinking » est « Adaptive (extended deprecated) ». Le script n'envoie aucun champ `thinking` (comme
   pour Fable 5.2 et Opus 5.5) ; sans lui, Opus 4.6 pourrait ne pas réfléchir. C'est à trancher, rien n'a été ajouté.
6. **`--sortie-max` n'est pas scellé** dans `especes.json` : il est journalisé, et un run peut en changer d'un lancement à
   l'autre. `devis-reprise` ne connaît pas l'option ; il garde la table.
7. Préfixe de `--cle-kimi` (`KIMI_API_KEY` ou `MOONSHOT_API_KEY`) : c'est un choix du développeur, par analogie avec la
   règle d'OpenAI. Le mandat ne le fixait pas.
8. Les prix lus d'Astra (8 / 40) et de Fable 5.2 (8 / 40) sont plus bas que ceux de la table (10 / 50). La table est
   gardée comme borne haute.
