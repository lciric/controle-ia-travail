# Transport réel Kimi pour le pilote de l'essaim — v2

- Sous-agent développeur (Claude Opus 5.5), 22 novembre 2026. **Aucun appel réel, aucune dépense, aucun réseau sortant.** Toutes les épreuves tournent contre des serveurs locaux (127.0.0.x), avec une clé factice. Rien n'est écrit dans le dépôt, rien n'est commité. Aucun refus d'outil ni de classifieur.
- La v2 corrige la v1 (`docs/notes/organisme-essaim-communicant-v1/transport-kimi-reel-v1/`, gardée sans modification) d'après sa contre-lecture, `transport-kimi-reel-v1/contre-lecture-v1/contre-lecture-transport-kimi-reel-v1-v1.md` (« Conforme avec réserves », bloquants B1 et B2, attaques N1 à N20).

## 1. Fichiers

| fichier | rôle |
|---|---|
| `transport_kimi_reel_v2.py` | le transport |
| `adaptateur_kimi_strict_v2.py` | adaptateur v1 plus la classe exacte, l'empreinte des modules, le code d'origine et les constantes |
| `faux_serveur_kimi_v2.py` | faux serveur : compte les requêtes, tient sa facture, et porte les artefacts neufs de la v2 |
| `essai_fumee_kimi_v2.py` | l'essai de fumée, six appels au plus (non lancé sur Kimi) |
| `test_transport_kimi_reel_v2.py` | **112 épreuves réussies** ; sortie dans `test-transport-kimi-reel-v2-pytest.txt` |
| `attaques_cl_v1_sur_v2.py` | rejeu sur la v2 de l'outil d'attaques du contre-lecteur ; sorties `attaques-cl-v1-sur-v2.json` et `.stdout` |

Rejeu : `env -u KIMI_API_KEY /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider test_transport_kimi_reel_v2.py` (environ 95 s).

## 2. Différence avec la v1

| point de la contre-lecture | v1 | v2 |
|---|---|---|
| **B1** : journal de la fumée | entiers du premier niveau de `usage` seulement ; motif d'un refus perdu | diagnostic entier par appel, masqué : `usage_brut` (chaque `usage` reçu, feuilles imbriquées comprises, dont `completion_tokens_details.reasoning_tokens` et `prompt_tokens_details.cache_write_tokens`), `usage_refuse`, `en_tetes_id`, `coupure_sortie`, `id_reponse` |
| **B2** : plafond de 1 USD dur | contrôle avant l'appel seulement ; f3 à 0,083 USD pour 0,040 de réserve, et la course continue | arrêt 16 si le coût mesuré dépasse la réserve, si l'usage est refusé ou si la sortie dépasse `max_tokens` ; arrêt 14 si le cumul dépasse le plafond ; arrêt 13 si un appel autre que f5 échoue ; **f2 en premier** |
| B2 : `max_tokens` déprécié | seul champ envoyé | `max_tokens` **et** `max_completion_tokens`, de même valeur (`api_chat.md` l. 1077-1081) ; `champs_max` pour n'en garder qu'un |
| N10 : amont qui ignore `max_tokens` | flux lu jusqu'au bout | **coupure côté client** dès plus de `max_tokens` morceaux non vides, ou plus de 12 × `max_tokens` octets de texte : arrêt 16 |
| N5 : usage intermédiaire | accepté | refusé : seul le dernier morceau avant `[DONE]`, à `choices` vide, fait foi |
| N6 : deux `usage` | le dernier gagnait | refusé ; les deux gardés au diagnostic |
| N11 : clé renvoyée par l'amont | masque après la troncature ; `id` et `model` non masqués | **masque d'abord**, sur tout champ rendu (identifiant, modèle, motif d'erreur, en-têtes, contenu, réflexion, chaînes de l'usage), et aussi sur tout fragment de 8 caractères de la clé |
| N12 : `debuglevel` | non vérifié | `set_debuglevel(0)` sur chaque connexion ; refus sans envoi si celui de la classe est non nul |
| N13 : attributs réécrits | acceptés, clé envoyée à un hôte refusé | configuration figée (toute affectation refusée, sauf par `regler_delais`, validé) ; empreinte de la configuration, amont et TLS revérifiés avant chaque envoi |
| N14 : constantes réécrites | acceptées | comparées aux littéraux par le transport, et à celles du fichier par l'adaptateur strict |
| fonctions et méthodes remplacées | méthodes de la classe seulement | l'adaptateur strict compare le code chargé de **chaque** fonction des deux modules (transport et adaptateur v1) à celui compilé depuis leur fichier empreinté |
| N15 : envoi doublé sous `putrequest` | 2 POST, 1 envoi mesuré | refus sans envoi si une méthode de `http.client`, de `ssl.SSLSocket` ou de `socket.socket` n'a plus son code d'origine ; plus bas (en C), seul le faux serveur le voit (limite déclarée) |
| N16 : filtre des noms | accents, homoglyphes et UUID acceptés | forme NFKD sans diacritiques, pliage de casse, homoglyphes, invisibles retirés ; UUID refusé |
| N18 : 407 du mandataire | relançable | fatal (17) |
| N20 : GO contourné par un préfixe | `startswith("http://127.0.0.1")` | l'URL est analysée : `http` vers un hôte local exact, sinon `GO_ID` exigé ; construction refusée ⇒ code 2, sans envoi |
| fumée : pièces v4 | non vérifiées | vérifiées à leur empreinte avant l'import, sinon code 2 |
| fumée : clé | variable `KIMI_API_KEY` | `--variable-cle` : la clé du projet dédié, sous le nom que choisit le directeur |

## 3. Rejeu des attaques du contre-lecteur sur la v2

`attaques-cl-v1-sur-v2.json` reprend l'outil du lecteur (sha256 vérifié). Trois seuls changements : les modules v2, la construction de l'adaptateur dans le `try`, et le contournement de N13 par `object.__setattr__`.

| n° | v1 | v2 |
|---|---|---|
| N1 à N4, N8, N9a | tenus | tenus, à l'identique |
| N5 | sous-compte accepté | `usage = None` |
| N6 | sortie 5 | `usage = None` |
| N7a | invisible | **inchangé, limite déclarée** |
| N7b | excédent ajouté | idem (1 510) |
| N8b | toléré | toléré |
| N9b | arrêt à 200 540 octets | arrêt dès la coupure `max_tokens`, à 34 136 octets |
| N10 | 300 ko lus | coupé à 842 octets |
| N11a, b, c | fuites | aucune (le préfixe de 12 caractères n'apparaît plus) |
| N12 | clé sur la sortie standard | refus avant l'envoi ; rien sur la sortie standard |
| N13 | clé reçue par 127.0.0.2 | affectation refusée ; contournée par `object.__setattr__`, refusée avant l'envoi ; 0 requête |
| N14 | autre modèle envoyé | refus, constante réécrite |
| N15 | 2 POST, 1 mesuré | refus avant l'envoi (`send` remplacé), 0 POST |
| N16 | 3 acceptés sur 6 | 6 refusés sur 6 |
| N17 | 5 champs | 6 champs, avec `max_completion_tokens` |
| N18 | relançable | fatal |
| N19 | f3 au-delà de sa réserve, course continue ; forme perdue | arrêt 16 au premier usage sans détail, forme gardée ; second passage (N19b) : arrêt 16 à f3, « coût mesuré 0,083 > réserve 0,040 » |
| N20 | préfixe accepté | code 3 |

## 4. Essai de fumée — commande exacte, NON lancée (GO séparé requis)

- **La fumée tourne dans un projet Kimi dédié, à budget de 1 USD.**
  - Le directeur crée ce projet, et règle dans *Project Settings → Project Budget / Rate Limit Settings* un budget **quotidien et mensuel de 1 USD**.
  - La clé est une clé neuve de ce projet. Elle entre dans l'environnement sous le nom que le directeur choisit, passé par `--variable-cle`.
  - Source : `docs/sources/tarifs/kimi-2026-11-22/erratum-1-lecture-tarif-et-limite-kimi-v1.md` ; `org-best-practice-2026-11-22.md`, l. 193-201 ; `project-spend-limits-2026-11-22.md`, l. 16-17.
  - Le budget s'applique **avec retard**, et ce qui est dépensé pendant ce retard reste dû. Le solde prépayé de l'organisation, partagé entre ses projets, reste donc la seconde borne. Le plafond dur du registre (1 USD, arrêts du § 2) est la troisième.
- **Réserves** : 0,202338 USD au total. f2 : 0,0011 ; f1 : 0,0206 ; f3 : 0,0402 ; f4 : 0,0793 ; f5 : 0,0210 ; f6 : 0,0402. Tarif relu le 22 novembre (2,00 / 10,00), égal aux prix gelés. Empreinte du plan : `60708812…63932d31`.

```bash
# GO de Lazar consigné dans registres/go.md ; clé du projet dédié déjà dans l'environnement, sous le nom NOM_CLE
S=/chemin/de/essaim-transport-reel-v2            # ce dossier, une fois versé
DOS=/home/user/controle-ia-travail/runs/essai-fumee-kimi-v2 ; mkdir "$DOS"   # neuf
GO_ID=GO-AAAA-MM-JJ-NN SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  DOSSIER_DEVIS_V4=/home/user/controle-ia-travail/docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4 \
  /home/user/controle-ia-travail/.venv/bin/python -I -B "$S/essai_fumee_kimi_v2.py" \
  --registre "$DOS/registre-fumee-v2.jsonl" --journal "$DOS/journal-fumee-v2.jsonl" --plafond-usd 1 --variable-cle NOM_CLE
```

- La clé n'est plus dans les arguments : elle est héritée de l'environnement, puis retirée par le transport. `HTTPS_PROXY` est hérité.
- **Ordre et vérifications** :
  1. f2 (H2 : fin `length`, `completion_tokens` ≤ 16, **champ** de la réflexion) ;
  2. f1 (contrat) ;
  3. f3 et f4 (H3 à 10 et à 29 ko) ;
  4. f5 (H4 : coupé à 4 s) ;
  5. f6 (H1, avec le cache).
- **Arrêts** : au premier écart, comme au § 2.
- **Si f2 rend 400** (deux champs refusés) : arrêt 17, à 0,0011 USD. Il faut alors un nouveau GO, sur un registre neuf, avec `--champs-max max_completion_tokens`.
- **Rapprochement** : H1 et H4 se tranchent à J+1 seulement, quand la console donne le détail par requête et la liste des requêtes interrompues (`client_disconnected`). Il se fait avec `id_reponse` et `en_tetes_id`.
- **f5** : la facture d'un 429 ou d'un 5xx n'est pas éprouvée, car on ne peut pas la provoquer. Si Kimi répond en moins de 4 s, H4 n'est pas éprouvée non plus.
- **`reasoning_effort`** vaut `max` par défaut : f1, f3 et f4 finiront sans doute à `length`, sans danger pour le coût.

## 5. À relever chez le fournisseur

1. **Facturation de la réflexion.** Les exemples d'`api_chat.md` (l. 205, 229, 483) donnent `reasoning_tokens` **compris** dans `completion_tokens`. La v1 citait aussi la l. 236 du guide de réflexion : elle vise `kimi-k2.7-code` et `kimi-k2.6`, **pas** `kimi-k3.1-pro` (correction de la contre-lecture). La phrase qui manque : « facturée seulement par `completion_tokens` ».
2. **Facture des requêtes coupées et des 429 ou 5xx** ; et la page « Common Error Codes ». À lire dans la console : « List interrupted requests » et « List request details ».
3. **Modèle exécuté contre modèle de la requête.** La signature `X-Msh-Request-Nonce` porte sur le modèle de la requête.
4. **Envoi conjoint** de `max_tokens` et de `max_completion_tokens` : f2 le dira, pour 0,0011 USD.
5. Clos par la contre-lecture : le champ `n`, le cache (palier de 5 minutes par défaut), et le tarif (relu le 22 novembre, égal).

## 6. Réserves et limites déclarées

- **Code hostile dans le même processus.** Restent hors de portée :
  - `object.__setattr__` suivi d'un recalcul de l'empreinte ;
  - `ctypes` ;
  - une couche réseau remplacée en C, ou un envoi doublé sous `socket`, que seul le serveur voit ;
  - la réécriture conjointe d'un fichier et de son empreinte.
  - Seuls le budget du projet et le solde prépayé les bornent.
- **Lanceur v2.** Il admet toute sous-classe de l'adaptateur. Imposer `type(adaptateur) is AdaptateurKimiStrict` et l'empreinte de ce fichier demande un lanceur v3 : c'est proposé, pas fait.
- **N7a.** Une réflexion facturée dans un champ inconnu, avec un `total_tokens` cohérent, reste invisible.
- **Seuils choisis à la main.**
  - Coupure à plus de `max_tokens` morceaux non vides : elle suppose qu'un morceau non vide porte au moins un jeton.
  - 12 octets par jeton.
  - Un fragment de clé de 8 caractères.
  - Une erreur de seuil donne un arrêt sûr, jamais un sous-compte. Le filtre d'homoglyphes n'est pas exhaustif.
- **Usage strict.** Un `usage` hors de la forme documentée arrête la fumée dès f2 (à 0,0011 USD). C'est voulu : la forme reçue est gardée au journal.
