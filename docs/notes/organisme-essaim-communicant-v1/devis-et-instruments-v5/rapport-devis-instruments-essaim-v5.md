# Rapport — devis et instruments de l'essaim — v5

- Sous-agent auteur (Claude Opus 5.5), 22 novembre 2026. **Aucun appel de modèle, aucune dépense, aucun réseau sortant, rien d'écrit ni de commité dans le dépôt.**
- Place prévue : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v5/`.
- Pièces corrigées : la vérification de la v4, `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4/verification-v1/verification-devis-instruments-essaim-v4-v1.md` (« VV4 », verdict « À corriger »), avec ses outils.
- Le transport réel versé est employé et cité à son empreinte, sans modification : `docs/notes/organisme-essaim-communicant-v1/transport-kimi-reel-v1/` (`transport_kimi_reel_v1.py` `4bba649c…`, `adaptateur_kimi_strict_v1.py` `6b8e9553…`, `faux_serveur_kimi_v1.py` `00557e57…`).
- Aucun refus de permission, de garde ou de classifieur n'a été rencontré.

## Verdict

- **Corrigés et éprouvés dans le code** :
  - verrou exclusif, fichiers temporaires propres au processus, sceau à secret, ancre hors du fichier ;
  - relecture complète du registre avant chaque réserve ;
  - chemin du registre écrit en dur ;
  - plafond du registre comparé à la borne ;
  - classe exacte et empreinte de l'adaptateur et du transport ;
  - aucune écriture avalée.
- **Refusés avant toute dépense** (0 requête, 0 USD) :
  - N1 (registre neuf ailleurs) et N1b ;
  - N2 (registre tronqué puis re-scellé, avec ou sans la clé) ;
  - N3 et N3b (courses entrelacées : code 25 pour la seconde) ;
  - N4 (registre forgé au-dessus de la borne) ;
  - N5 (sous-classe de l'adaptateur).
- **Le lanceur v3 n'admet pour le pilote que `AdaptateurKimiStrict` et `TransportKimiReel`**, en classe exacte et à leurs empreintes. Il est éprouvé avec ce transport contre son faux serveur : P-std entier, 748 requêtes pour 748 réserves écrites, dépense comptée (64,63 USD) ≥ facture (63,65 USD).
- **A3 et A4 sous leur forme réelle ne sont PAS arrêtées par le code du lanceur.**
  - Un transport admis qui cache ses relances en rendant `tentatives = 1` : 529,34 USD facturés pour 176,45 comptés.
  - Une réflexion facturée absente de l'usage : 235,97 USD facturés.
  - Une facture sans trace dans l'usage, sous le transport réel : 63,46 USD facturés pour 63,41 comptés.
  - Elles relèvent du transport réel, qui mesure ses envois sur la connexion et rend `usage = None` si le champ de réflexion manque, ainsi que de l'essai de fumée (H1, H2) et de la limite de 204 USD chez le fournisseur.
  - **Le rapport v4 disait ces deux attaques « arrêtées » : c'était inexact**, car son faux transport rendait honnêtement ses tentatives et sa réflexion.
- **Vrai pire inchangé : 203,94 USD** sous H1 à H4 (`garde_pilote_essaim_v2.py`, inchangé ; `devis-et-instruments-v4/calcul-vrai-pire-v4.json`). Il tient désormais par pilote, contre une seconde course, contre un registre refait et contre une couche d'appel substituée.

## 1. Différence avec la v4

| point de VV4 | v4 | v5 | preuve (`epreuves-lanceur-pilote-v3.json`) |
|---|---|---|---|
| N1 : registre neuf à un autre chemin | 2 × 176,45 USD | chemin écrit en dur pour le pilote (`REGISTRE_PILOTE_REL = runs/pilote-essaim-pstd/registre-depense-v2.jsonl`, `courir_pilote()` sans chemin). Ancre unique hors du fichier : création d'un second registre sous la même ancre refusée ; registre neuf présenté sous l'ancre refusé (tête ≠ ancre) | N1, N1b : 22, 0 USD |
| N2 : tronqué et re-scellé | accepté | sceau à secret (HMAC-SHA256, clé de 32 octets en mode 600, hors du dépôt pour le pilote). L'ancre garde la tête et le nombre de lignes, et ne fait que croître | N2 (re-scellé avec la clé : ancre ⇒ 22) ; N2b (sans la clé : sceau ⇒ 22) |
| N3, N3b : courses simultanées ou entrelacées | deux codes 0, 351,46 USD | verrou exclusif `fcntl.flock`, non bloquant, tenu pendant toute la course. Fichiers temporaires `.<pid>.tmp`. Relecture complète (octets, sceau, ancre) **avant chaque réserve** | N3 (deux processus) : [0, 25] ; N3b (même processus) : [0, 25] ; registre changé pendant la course : 22 |
| N4 : registre forgé avec un plafond de 10⁶ | accepté | plafond du registre comparé à la borne à l'ouverture | N4 : 24 |
| N5 : sous-classe de l'adaptateur | acceptée (`isinstance`) | **classe exacte** de l'adaptateur et du transport, par listes (module, classe) → empreinte du fichier du module ; adaptateur de base vérifié à `67704c1e…` | N5 : 24 ; réel, sous-classe de `AdaptateurKimiStrict` : 24 ; réel, adaptateur générique avec le transport réel : 24 ; réel, empreinte gelée différente : 24 |
| A3 et A4 sous leur forme réelle (V3a, V4a) | dites « arrêtées » | **non arrêtables par le code du lanceur** : déclarées comme limites, rejouées sous transport admis (code 0, sous-compte rapporté). Sous la liste du pilote, ces transports de faux ne sont pas admis (24) | V3a, V4a : 24 non admis ; code 0 sous admission, limite |
| l. 116 : échec d'écriture de la réserve | sortie sans arrêt au journal | aucun appel, arrêt écrit au journal (22, `inscrit_au_registre: false`) | « écriture de la réserve impossible » : 22 |
| l. 155 : `except OSError: pass` | arrêt avalé | arrêt au journal avec code 26 et `inscrit_au_registre: false` ; le registre resté incohérent est refusé ensuite (22) | « écriture de l'arrêt impossible » : [26, 22] |
| registre « relu avant tout appel » (docstring) | relu seulement à l'ouverture | `Registre.verifier()` appelé par chaque écriture, donc avant chaque réserve | idem |
| transport réel | absent | admis par empreinte, éprouvé contre `faux_serveur_kimi_v1` | 8 cas « réel » |
| garde des formes fausses | médiane de d_w ≤ +2 ; queue à 16 | quatre réserves de VV4 adoptées (§ 3) | `a-faire-avant-preenregistrement-pilote-v2.md`, § 5 |

**Inchangé depuis la v4**, copié à l'octet pour l'import local et rejouable par `devis-et-instruments-v4/rejouer_v4.sh` :
- `garde_pilote_essaim_v2.py` ;
- `adaptateur_fournisseur_v1.py` ;
- `faux_fournisseur_v1.py` ;
- `calcul_devis_essaim_v4.py` ;
- `racine_depot_v1.py` ;
- `comparer_hors_horodatages_v1.py`.

Le devis, le contrôle des nombres, le vrai pire et le test de mort ne changent pas.

## 2. Épreuves

`epreuves_lanceur_pilote_v3.py` → `epreuves-lanceur-pilote-v3.json` : **49 cas sur 49 tenus**. pytest : `test_lanceur_pilote_essaim_v3.py`, 7 tests passés (`test-lanceur-pilote-v3-pytest.txt`).

- **Critère de chaque cas** : code attendu, ligne d'arrêt, dépense comptée ≥ facture et ≤ plafond.
- **Seules exceptions, déclarées** : V3a et V4a sous transport admis, A8, et la facture cachée sous le transport réel.
- **Cas sains** :
  - P-std : 64,09 USD ;
  - tout au plafond : 176,45 ;
  - 74 échecs ;
  - pire extrême : 198,80 comptés pour 193,57 facturés ;
  - processus tué puis reprise : 63,33 pour 63,07 ;
  - transport réel : 64,63 pour 63,65 ; 748 requêtes, 748 réserves.
- **Gardes de la v4 rejouées** :
  - A1, A2, A5, A6, A7, A7b, A8, A9, A10 ;
  - A3b et A4 sous leur forme honnête ;
  - modèle servi différent ;
  - `max_tokens` de 24 001 ;
  - 64 961 octets ;
  - 75 échecs ;
  - plafond de 50 USD ;
  - aucun adaptateur.
- **Transport réel sous les listes du pilote**, contre le faux serveur :
  - cas sain ;
  - sous-classe de l'adaptateur strict ;
  - adaptateur générique ;
  - empreinte différente ;
  - champ de réflexion absent (16) ;
  - réflexion hors du compte (10) ;
  - autre modèle (16) ;
  - facture cachée (limite).
  - Dans chaque cas, une requête au serveur par réserve écrite.
- **Réserve d'épreuve** : N3 dépend d'un délai de 0,5 s entre les deux processus. N3b, lui, est déterministe.

## 3. Garde des formes fausses (VV4, § 6), adoptée

Détail dans `a-faire-avant-preenregistrement-pilote-v2.md`, § 5.
1. F' = formes fausses distinctes **plus les cartes « rien »**.
2. **Total apparié** : Σ_w F'(x, w) ≤ r × Σ_w F'(B3R, w) + 24, soit 83,1 pour (a) (r = 48/52) et 88 pour (c) (r = 1), sur la calibration (Σ F'(B3R) = 64).
3. **Queue resserrée et appariée** : au plus 1 monde sur 12 où F'(x, w) > r × F'(B3R, w) + 8. B3 échoue aux deux gardes (4 mondes en queue, total 113), comme attendu.
4. **Même garde pour le bras (c)**, gelée au préenregistrement avant toute lecture des mondes neufs.

## 4. Reste ouvert

- **Avant le GO** :
  - relecture du transport réel par un sous-agent neuf ;
  - points de la documentation du fournisseur (LISEZMOI du transport, § 5) ;
  - essai de fumée sous GO séparé (0,2023 USD de réserves, plafond de 1 USD, commande écrite dans le LISEZMOI) ;
  - **limite de 204 USD chez le fournisseur**, seule défense contre une facture cachée et contre un détenteur de la clé qui réécrirait aussi l'ancre.
- **Ancre et clé** dans `~/.local/state/controle-ia/pilote-essaim-pstd/` :
  - à confirmer par le directeur ;
  - dans un conteneur de session, ce dossier peut disparaître. Le registre deviendrait alors inouvrable (refus 22, arrêt sûr), sans dépense possible.
- **Mort du processus entre l'ajout d'une ligne et le nouveau sceau** : le registre est alors refusé (22) et la course ne peut pas reprendre sans décision du directeur. L'échec est sûr, mais il bloque.
- **Liste « à faire avant le préenregistrement »** : `a-faire-avant-preenregistrement-pilote-v2.md`, points 1 à 11.

## 5. Rejeu

`rejouer_v5.sh DOSSIER_NEUF` : compagnons, épreuves (comparées hors horodatages), pytest. Résultat au § 6.

## 6. Résultat du rejeu

`rejouer_v5.sh`, lancé depuis le bloc-notes dans un dossier neuf (racine donnée par `DEPOT_CONTROLE_IA`) : **rejeu tenu**.
- Compagnons conformes.
- Épreuves égales hors horodatages, 49 cas sur 49 ; 7 tests pytest passés.
- C'est un rejeu de l'auteur seul. Le rejeu depuis le commit, une fois versé, revient à un relecteur neuf.

## 7. Fichiers et empreintes (sha256)

| fichier | sha256 |
|---|---|
| `a-faire-avant-preenregistrement-pilote-v2.md` | `a6794398004e6dbd21827a183d66ef7c964728ec420c5947ba653b70f11b2828` |
| `adaptateur_fournisseur_v1.py` | `67704c1e42a0308a4f511ddc82e58666e6741b9b954f78072fd55a64c7eff1e4` |
| `calcul_devis_essaim_v4.py` | `e5e61b25ccf24a6bbdcc29df6569bf80f5ffdf66d6f7c0a7a7207d99bacc7188` |
| `compagnons_v5.sh` | `2c850743bcf6ae6d90dac7d91bbb3bed94901103d7feba779012959e1d267ca9` |
| `comparer_hors_horodatages_v1.py` | `3b64ed68a6af80b81443b4fdae3814751854661b785402a679c2d0d110e45d97` |
| `epreuves-lanceur-pilote-v3.json` | `08a5259d5f624a534931108f618b95babbd27c11ab6e4309954f847441f801ea` |
| `epreuves-lanceur-pilote-v3.stdout` | `6307c433249d2883b825bf5ad5b1dc674c7a7709fd5da80f7bd81bd878dc2406` |
| `epreuves_lanceur_pilote_v3.py` | `39968f748b9288da27c4ba265e454667bc85de2c915d7e3403bb34e067c0940a` |
| `faux_fournisseur_v1.py` | `c89eaec2a0d2f450d31853bde597ccffb0f14cba7a9a4584318218f22b4c7869` |
| `garde_pilote_essaim_v2.py` | `d41305918b53d3bfa8b55ace148fdde6cf22f25623bcae2806585d0a242e4b84` |
| `lanceur_pilote_essaim_v3.py` | `bbe069d6f7511f8c32af9c5db38425bc3a5298730871181421096c9fb507704c` |
| `racine_depot_v1.py` | `3a5acf778146dc7df43716c082dc629f0251b8920a150940315863f235f0cccc` |
| `registre_depense_v2.py` | `2e515af1fb3fc3d33ad81b75c93f0cec7329a9af015cee53bc85b1d54483c598` |
| `rejouer_v5.sh` | `26cd0dbf344cbfaf84a0fc4477bbe623e2d706c174100ec3c95f541d449774ca` |
| `test-lanceur-pilote-v3-pytest.txt` | `66f8270c78b00a0b25ed855d6daafd810c504384646aa36bd58802a4e4f905f5` |
| `test_lanceur_pilote_essaim_v3.py` | `5970b11b47bc7bdf7ea5e21714df4c2ee05b8c45e0a55954a2f2e5067c56201a` |
| `rapport-devis-instruments-essaim-v5.md` | dans son compagnon `.sha256` |

Pièces citées hors de ce dossier (non modifiées) : `transport-kimi-reel-v1/transport_kimi_reel_v1.py` `4bba649ce1d1b62ea5f50225e62a5eb5666592014033e174b47cca34533aa5a6` ; `adaptateur_kimi_strict_v1.py` `6b8e955300d657b9f7ed784e544d878026810859bd6f534c5aad22f1a367de9b` ; `faux_serveur_kimi_v1.py` `00557e57297dfb62249f018475480a975e9711acf99a04987d40a7114ed55d6d`.

Chaque fichier a son compagnon `.sha256` (format `empreinte  nom`, écrit par `compagnons_v5.sh`).
