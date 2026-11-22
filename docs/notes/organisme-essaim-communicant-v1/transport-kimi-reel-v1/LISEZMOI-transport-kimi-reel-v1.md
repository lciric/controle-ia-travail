# Transport réel Kimi pour le pilote de l'essaim — v1

- Sous-agent développeur (Claude Opus 5.5), 22 novembre 2026. **Aucun appel réel, aucune dépense, aucun réseau sortant.** Toutes les épreuves tournent contre un faux serveur local (`127.0.0.1`, port libre), avec une clé factice. Rien n'est écrit dans le dépôt, rien n'est commité.
- Pièces du dépôt lues sans y écrire, importées **à leur empreinte** (compagnons `.sha256` vérifiés par les épreuves) : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4/` (`adaptateur_fournisseur_v1.py`, `garde_pilote_essaim_v2.py`, `registre_depense_v1.py`, `lanceur_pilote_essaim_v2.py`, `calcul_devis_essaim_v4.py`, `racine_depot_v1.py`).
- Aucun refus d'outil ni de classifieur rencontré.

## 1. Fichiers

| fichier | rôle |
|---|---|
| `transport_kimi_reel_v1.py` | le transport (`TransportKimiReel`), bibliothèque standard seule (`http.client`) |
| `adaptateur_kimi_strict_v1.py` | `AdaptateurChatCompletions` plus la classe exacte du transport, l'empreinte de son module et ses méthodes figées |
| `faux_serveur_kimi_v1.py` | faux serveur local qui compte chaque requête et tient sa propre facture |
| `test_transport_kimi_reel_v1.py` | 81 épreuves pytest ; sortie : `test-transport-kimi-reel-v1-pytest.txt` (81 réussies) |
| `essai_fumee_kimi_v1.py` | l'essai de fumée de six appels (non lancé sur Kimi ; répété à blanc sur le faux serveur) |

Rejeu : `env -u KIMI_API_KEY /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider test_transport_kimi_reel_v1.py` (environ 50 s).

## 2. Contrat rempli

- **Aucune relance.** `http.client` ne relance jamais. Chaque appel ouvre une connexion neuve, fait un seul `POST`, puis la ferme.
- **Envois mesurés, pas déclarés** (exigence 1 de la vérification de la v4) :
  - les connexions sont de classes qui comptent chaque `putrequest` (`ConnexionHTTPComptee`, `ConnexionHTTPSComptee`) ;
  - une connexion d'une autre classe est refusée sans envoi ;
  - `tentatives` vaut la mesure. Au-delà de 1 : `AnomalieReponse` avec `envois` égal à la mesure, et le lanceur compte une réserve par envoi.
- **Classe exacte** (exigence 3). `AdaptateurKimiStrict` exige, à la construction et avant chaque appel :
  - `type(transport) is TransportKimiReel` ;
  - le fichier du module à `SHA_TRANSPORT`, écrite en dur ;
  - aucune méthode remplacée, sur la classe comme sur l'instance ;
  - les classes de connexion comptées intactes.
- **Modèle demandé** : `kimi-k3.1-pro` seulement. Tout autre nom est refusé sans envoi. Le modèle servi est rendu ; au premier écart, la lecture s'arrête et l'adaptateur arrête la course (16).
- **`max_tokens`** : celui de la garde, entre 1 et 24 000.
- **Corps en liste blanche** : `model`, un seul message `user`, `max_tokens`, `stream`, `stream_options.include_usage`.
  - Ni `n`, ni identifiant, ni option de cache, ni `reasoning_effort`.
  - Refus sans envoi si le corps porte un identifiant de session, un lien de session, une adresse électronique ou un nom de personne.
- **Usage et réflexion** (exigence 2) :
  - champs exigés : `prompt_tokens`, `completion_tokens`, `total_tokens` et `completion_tokens_details.reasoning_tokens` ; si l'un manque, `usage = None`, donc réserve entière et arrêt 16, jamais zéro ;
  - réflexion rendue hors de `completion_tokens` : l'adaptateur l'ajoute ;
  - excédent de `total_tokens` : ajouté en sortie ;
  - texte rendu de plus de 12 octets par jeton de sortie déclaré : `usage = None`.
- **Erreurs** :
  - 408, 409, 425, 429 et 5xx, coupures, flux sans `[DONE]`, délais : `ErreurFournisseur` (échec compté à la réserve, relance laissée au seul lanceur) ;
  - autres statuts (400, 401, 402, 403, 404) : `ErreurTransportFatale`, arrêt 17 ;
  - 200 qui n'est pas un flux, réponse trop longue : anomalie, arrêt 16.
- **Clé** :
  - lue par son nom (`KIMI_API_KEY`) et retirée de l'environnement ;
  - gardée dans un `bytearray` remis à zéro par `fermer()` ;
  - masquée partout : `repr`, exceptions, diagnostic, journal ; le transport ne se sérialise pas.
  - Limites de Python : une copie `bytes` est faite à chaque envoi, et `/proc/<pid>/environ` garde la valeur.

## 3. Épreuves (81 réussies)

- **Cas sain** : un envoi, un corps exact, l'en-tête attendu.
- **Refus sans envoi** (le serveur compte 0) : 12 requêtes hors contrat, dont un autre modèle, `max_tokens` à 24 001 ou à 0, `n` = 2, un identifiant de session, une adresse ou un nom.
- **Artefacts** :
  - autre modèle servi, ou modèle qui change en cours de flux ;
  - statuts 429, 500, 502 et 503 (un seul envoi) ; 400 à 404 ;
  - fermeture sans réponse ; coupure après 0, 1, 2 ou 3 morceaux, et après l'usage ; flux sans `[DONE]` ; événement d'erreur ; 200 qui n'est pas un flux ;
  - usage absent ou négatif ; réflexion hors de `completion_tokens`, au premier niveau ou par le détail ; excédent de `total_tokens` ;
  - réponse trop longue en octets ; sortie au-delà de `max_tokens` (garde, 16) ;
  - délai de silence ; délai total dépassé malgré les messages de maintien.
- **Envois** : 100 appels mêlés donnent exactement 100 requêtes au serveur ; 12 appels donnent des envois mesurés égaux au compte du serveur.
- **Exigences de la vérification** :
  - deux sous-classes hostiles (relance sur le même compteur, ou sur un compteur jeté) sont refusées par l'adaptateur strict ;
  - sous l'adaptateur non strict, la relance sur le même compteur est **mesurée à 2** : deux réserves comptées, arrêt 16, dépense ≥ facture ;
  - méthode masquée sur l'instance, et connexion non comptée : refusées ;
  - champ de réflexion absent (quatre formes) : `usage = None` ;
  - réflexion facturée mais absente de l'usage, sous le lanceur : arrêt 16, dépense ≥ facture.
- **Lanceur v2 et registre réels, faux serveur à la place de l'amont** :
  - P-std complet, avec 4 échecs (429, 500 facturé au plafond, coupure facturée), de la réflexion hors compte et du cache : code 0 ; 748 requêtes = 748 réserves écrites = envois mesurés ; dépense comptée ≥ facture du faux serveur, et ≤ 203,94 USD ;
  - plafond de 1 USD : arrêt 14 ;
  - sept artefacts : arrêts 16, 10 et 17, chaque fois avec une dépense ≥ facture.
- **Essai de fumée à blanc** : 6 envois ; H2 lue ; f5 coupé et compté à sa réserve ; aucun texte ni clé au journal ; registre clos (un rejeu est refusé, 23).

## 4. Essai de fumée prévu — commande exacte, NON lancée (GO séparé requis)

Six appels, une seule fois. Réserves calculées : **0,2023 USD** au total, sous un plafond de registre de **1 USD**, avec un registre neuf. Empreinte du plan : `6670d481…ac9dc8`.

```bash
GO_ID=GO-AAAA-MM-JJ-NN   # le GO de Lazar, consigné dans registres/go.md
S=/chemin/de/essaim-transport-reel-v1           # ce dossier, une fois versé
DOS=/home/user/controle-ia-travail/runs/essai-fumee-kimi-v1 ; mkdir "$DOS"    # neuf
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GO_ID="$GO_ID" KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="$HTTPS_PROXY" \
  SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  DOSSIER_DEVIS_V4=/home/user/controle-ia-travail/docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4 \
  /home/user/controle-ia-travail/.venv/bin/python -I -B "$S/essai_fumee_kimi_v1.py" \
  --registre "$DOS/registre-fumee-v1.jsonl" --journal "$DOS/journal-fumee-v1.jsonl" --plafond-usd 1
```

| appel | octets | `max_tokens` | réserve (USD) | ce qu'il vérifie |
|---|---|---|---|---|
| f1 sain-court | 33 | 2 000 | 0,0206 | modèle servi, une tentative, usage lisible, détail ≤ `completion_tokens`, H3 |
| f2 h2-max16 | 197 | 16 | 0,0011 | **H2** : fin `length`, `completion_tokens` ≤ 16 réflexion comprise, rien hors de ce compte |
| f3 h3-table | 9 840 | 2 000 | 0,0402 | **H3** : `prompt_tokens` ≤ octets + 256 (lignes de la case servie) |
| f4 h3-table-longue | 29 391 | 2 000 | 0,0793 | **H3** à une taille de proposeur |
| f5 h4-coupure | 252 | 2 000 | 0,0210 | **H4** : coupé côté client à 4 s, compté à sa réserve ; facture de la console ≤ réserve |
| f6 h1-repetition | 9 840 | 2 000 | 0,0402 | **H1** : facture ≤ usage rendu aux prix gelés ; cache lu rapporté |

- **Après l'essai** : rapprocher chaque `id_reponse` du journal de la console de facturation, ligne par ligne. H1 et H4 ne se tranchent qu'ainsi ; le script ne les déclare jamais tenues.
- **Réserve sur f5** : si Kimi répond en moins de 4 s, l'appel est réglé et H4 n'est pas éprouvée. Il faut alors un nouvel appel, sous un nouveau devis.

## 5. À relever dans la documentation officielle du fournisseur avant le GO

1. **Comptage de la réflexion.**
   - Ce qui est établi, sur pièces : `completion_tokens_details.reasoning_tokens` est **compris** dans `completion_tokens`. Sources :
     - `api_chat.md`, sha256 `67b8b5fd…`, exemple 112 / 90 et total 485 = 373 + 112 ;
     - essai réel du 30 octobre : 16 / 13, total 105 = 89 + 16 ;
     - `guide_use-thinking-models.md`, sha256 `0c4227ab…`, l. 236 : réflexion et contenu ≤ `max_tokens`.
   - Reste à relever : une phrase de la page des prix qui dise que la réflexion est facturée au prix de sortie, **et seulement par `completion_tokens`**.
2. **Relances côté serveur.** Moonshot relance-t-il ou refacture-t-il en interne ? Et comment facture-t-il une requête coupée par le client ou une réponse 429 ou 5xx ? Aucune page lue n'en parle.
3. **Champ du modèle servi.** Le `model` des morceaux est-il le modèle exécuté ? Un alias ou un repli peut-il y apparaître ? La signature de requête (`X-Msh-Request-Nonce`, `api_chat.md`) prouverait le modèle traité : piste à évaluer.
4. **`max_tokens` contre `max_completion_tokens`.**
   - Le premier est dit « déprécié » ; il a été honoré à l'essai du 30 octobre.
   - À confirmer qu'il le reste, et que la baisse automatique liée à la fenêtre de contexte ne le dépasse jamais.
5. **Champ `n`**, absent du schéma de Kimi : le transport ne l'envoie pas.
6. **Cache.** Le cache est écrit par défaut au palier de 5 minutes, facturé 2 USD par million, comme l'entrée. Le palier d'une heure coûte 4 USD : il n'est jamais demandé. À confirmer que le défaut ne change pas.
7. **Tarif.** Le tarif de 2 / 10 USD par million est lu le 30 octobre ; à relire et dater (point 3 de la liste « à faire »).

## 6. Réserves

- **Lanceur v2.** Il n'exige que `isinstance` de l'adaptateur. Faire de `AdaptateurKimiStrict` le seul adaptateur admis demande un lanceur v3, avec `type(adaptateur) is AdaptateurKimiStrict` : c'est proposé, pas fait.
- **Réflexion cachée.** Une réflexion facturée sans aucune trace dans l'usage ni dans le texte reste invisible au client. Seuls la limite de 204 USD chez le fournisseur et le rapprochement H1 la couvrent.
- **Seuil de 12 octets par jeton.** Il est choisi à la main ; un texte légitime très dense pourrait le franchir. Ce serait un arrêt sûr, jamais un sous-compte.
