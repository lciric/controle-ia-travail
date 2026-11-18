# Contre-lecture : le relais Gemini v4, la commande Gemini par lot v1 et la commande Astra v1 — v1

Contre-lecteur neuf (R2). Je n'ai écrit aucune des pièces lues. Date : 18 novembre 2026, vers 08:10Z.
Je n'ai fait aucun appel réseau vers un fournisseur. Je n'ai lancé aucun relais sur les ports 8787 à 8792 et je ne m'y suis pas connecté. Tous les essais ont tourné sur des ports libres de la boucle locale, devant de faux amonts.

## Verdicts

| Pièce | Verdict |
|---|---|
| Le relais Gemini v4, avec les chemins du mode par lot (`relais_gemini_v4.py`) | **à corriger** : aucun constat bloquant, trois constats significatifs |
| La commande Gemini par lot v1 (`commande_gemini_lot_v1.py`) et ses essais | **à corriger** : un constat bloquant, trois constats significatifs |
| La commande GPT-6 Astra v1 (`commande_astra_v1.py`, scellée) et ses essais | **autorisable** : constats mineurs seulement |

## Pièces lues, avec leurs empreintes (sha256, relevées pendant la lecture)

| Fichier | Empreinte |
|---|---|
| `argon-recherche-v1/relais_gemini_v4.py` (non scellé) | `cf09d461dd9af116936f41482bf2cdb379bb7907e3dc103c864d22ca9bed9e99` |
| `argon-recherche-v1/relais_gemini_v2.py` (scellé, conforme) | `2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb` |
| `argon-recherche-v1/commande_gemini_lot_v1.py` (non scellé) | `98d3bb7e08ce706fa13547156530b94dd32138dbd608cfce9a382b487c566790` |
| `argon-recherche-v1/test_commande_gemini_lot_v1.py` (non scellé) | `369650090cce3ad3a67dc1be544d8c08fd0499b61630f2ba26d9a43d0a7dfb4b` |
| `relais-kimi-v1/commande_astra_v1.py` (scellé, conforme) | `986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71` |
| `relais-kimi-v1/test_commande_astra_v1.py` (scellé, conforme) | `84c34cd1536ece70249321dc21c94b6ac3a6e689f82211975c8cb78560d0b7fb` |
| `organismes-discrets-v1/organisme-ideation-v1/epreuve-lot-carbon-v1/resultat-lot.json` | lu tel quel |
| Orchestrateur `pole/adaptateurs.py`, `AdaptateurCommandeExterne` | commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, arbre propre |

Les deux sources de prix d'Astra sont conformes à leurs empreintes citées :
- `prix-astra-v2.md` : `bf211a07…` ;
- la page de tarifs versée : `099c9496…`.

Dans les données de cette page, la ligne `gpt-6-astra` du palier standard vaut 10 / 1 / 12,5 / 50.

## Ce qui a tourné, et le résultat

Tous les essais ont été lancés avec `PYTHONDONTWRITEBYTECODE=1` et `-p no:cacheprovider`. Ils utilisent l'interpréteur du `.venv` du dépôt.

1. **Les essais de la commande par lot** (`test_commande_gemini_lot_v1.py`) : 14 réussis.
2. **Les essais de la commande Astra** (`test_commande_astra_v1.py`) : 50 réussis.
3. **La suite du relais v2 rejouée contre le v4.** J'ai copié `test_relais_gemini_v2.py` dans le dossier de travail temporaire, avec les noms redirigés vers le v4 (`relais_gemini_v4`, `relais-gemini-v4`, chemin du script). Elle charge la suite v1 entière : **49 réussis**, aucune régression.
   - Le différentiel entre le v2 et le v4 ne touche que les changements annoncés : en-tête, motifs de chemin, compteur, résumé d'un lot, relevé et annulation, options, version.
4. **Les sondes que j'ai écrites**, devant un faux amont qui rend exactement la forme réelle (création telle qu'au journal de l'épreuve, puis `resultat-lot.json`) :
   - **Lecture de la forme réelle.** `lire_resultat` lit `resultat-lot.json` : texte « Le nombre est 1013 et la somme est 5. », fin `STOP`, modèle servi `gemini-4-carbon`, usage 82 / 19 / 844. Le coût vaut 0,0364951 USD à 8,3 / 41,5, ce qui est exact. La lecture par la seule copie `metadata.output` marche aussi.
   - **Fins autres que `STOP` et autre modèle.** `MAX_TOKENS`, `SAFETY`, `RECITATION`, `OTHER` et une fin absente rendent tous le code 5. Un modèle demandé différent rend le code 5, avec `modele_servi` écrit, donc un refus pour le noyau.
   - **De bout en bout**, de la commande au relais v4 puis au faux amont de forme réelle : code 0, coût juste.
   - **Lot étranger** : un relevé par `GET`, une annulation par `POST :cancel`, un `GET` sur `:cancel` et un `POST` sur le chemin de relevé reçoivent tous 403, et l'amont ne reçoit rien.
   - **Clés**
     - un relevé avec `?key=FAUSSE` et une clé du client en en-tête part sans paramètre de requête, avec la seule clé du relais ;
     - une clé renvoyée en écho par l'amont dans le relevé est masquée (« [clé] ») ;
     - aucune clé ni aucun texte de réponse dans les cinq journaux produits.
   - **Création sans `name` en tête** (nom sous `metadata.name` seulement) : le relais retient le lot, et le relevé passe.
   - **Constats démontrés par les sondes** : voir C-1, R-1, R-2 et R-3 plus bas.

**Incident de ma part, réparé.** Ma première sonde a tourné avec `python -I`. L'option `-I` ignore `PYTHONDONTWRITEBYTECODE`. Elle a écrit `argon-recherche-v1/__pycache__/` (deux `.pyc`, 08:06:40Z) dans ce dépôt, pas dans le clone de l'orchestrateur. J'ai supprimé ces deux fichiers par leur chemin, puis le dossier. Les sondes suivantes ont tourné avec `-B`. Le clone de l'orchestrateur n'a pas été touché : son arbre est propre.

## Le relais Gemini v4 — à corriger

### Ce qui tient

- **Aucune régression** : la suite v1 et v2 passe en entier contre le v4 (49 essais).
- **Lot étranger** : il n'est jamais relevé ni annulé (403, rien n'est envoyé ; voir plus haut).
- **Clé**
  - elle n'est jamais écrite au journal : garde-fou d'assertion, et le journal lit le corps déjà masqué ;
  - elle est masquée dans le corps relayé (création comme relevé) ;
  - la clé du client et `?key=` sont retirés.
- **Nom du lot retenu** : la création rend `name` en tête (journal de l'épreuve), et `metadata.name` sert de repli (essayé).
- **Bornes** : `--max-lots` est compté avant l'envoi. `--max-releves` répond 429 au-delà de la borne (essayé).

### Constats

- **R-1 — significatif — l'annulation partage la borne des relevés** (`relais_gemini_v4.py` l. 220-231, `admettre_releve`, appelée pour `annule_lot` l. 418).
  - Ce qui se passe : quand `--max-releves` est épuisé, l'annulation d'un lot du relais est refusée (429) et n'atteint pas l'amont. Le lot continue.
  - Démontré : avec une borne de 3 relevés et un lot jamais fini, la commande dépasse son délai, et l'amont reçoit **0** annulation.
  - Même effet après un redémarrage du relais : les noms des lots ne vivent qu'en mémoire, donc l'annulation reçoit 403.
  - Correction proposée : admettre une annulation d'un lot connu hors de la borne des relevés, ou lui réserver une part de cette borne. Dire en en-tête que les lots ne survivent pas à un redémarrage.
- **R-2 — significatif — un lot n'est pas borné en contenu** (l. 430-436 : le corps n'est jamais lu).
  - Ce qui se passe : un seul appel compté (`--max-appels`) peut porter plusieurs requêtes. Chacune peut porter un champ `model` autre que celui du chemin, et des `tools`.
  - Démontré : un lot de 3 requêtes, dont deux avec `models/autre-modele-cher` et `google_search`, est relayé (200) et compté comme **1** appel.
  - Ce que l'amont ferait du champ `model` par requête **n'est pas vérifié** (R8 : je ne l'affirme pas).
  - Pourquoi c'est un changement : en v2, un appel valait une génération, et la borne d'appels bornait les générations. En v4, ce n'est plus vrai.
  - Correction proposée : le relais vérifie que le lot a au plus `--max-requetes-par-lot` requêtes (1 par défaut), et qu'aucune requête ne porte un `model` différent du chemin. Il peut aussi refuser `tools`.
- **R-3 — significatif — les gardes neuves du v4 ne sont pas toutes essayées (R5) ; le rejeu de la suite v2 n'est pas versé.**
  - Les essais (dans `test_commande_gemini_lot_v1.py`) couvrent le relevé d'un lot étranger, `--max-lots` et l'état. Ils ne couvrent ni l'**annulation** d'un lot étranger, ni `--max-releves`, ni le repli `metadata.name`, ni le masquage de la clé dans un relevé, ni `?key=` sur un relevé.
  - Toutes ces gardes marchent (mes sondes), mais rien dans le dépôt ne le montre.
  - L'addendum v4 (l. 150) annonce « les 49 essais des relais v1 et v2 rejoués contre le v4 ». Aucun fichier `test_relais_gemini_v4.py` ne le rend rejouable, alors que le v2 l'a fait pour le v1.
- **R-4 — mineur — une place de lot peut être consommée sans envoi** (l. 430-431). `admettre_lot` compte le lot avant `admettre`. Un refus pour taille ou pour `--max-appels` consomme quand même une place de lot. Démontré : `lots_crees = 1`, `appels = 0`.
- **R-5 — mineur — `_relayer_lot` n'a pas de garde sur le corps d'une annulation** (l. 368). Le corps est lu sans borne de taille. Un `Content-Length` non entier lève une exception dans le gestionnaire, et la connexion tombe sans réponse JSON.
- **R-6 — mineur — une réponse de relevé trop grande n'est pas journalisée** (l. 383). La réponse 502 est rendue, mais rien n'est écrit au journal.
- **R-7 — mineur — message d'erreur incomplet** (l. 571). Il ne nomme pas `--max-lots` ni `--max-releves`, qui sont pourtant vérifiés.
- **R-8 — mineur — mention de provenance** (l. 4-5). L'en-tête nomme la session et la lignée Carbon. C'est de la provenance, pas un contenu de sujet : aucune question, aucun fait, aucun témoin, aucune fiche. La pièce reste neutre.

## La commande Gemini par lot v1 — à corriger

### Ce qui tient

- **Contrat de l'adaptateur**
  - la dernière ligne est toujours un objet JSON avec `texte` et `cout_usd` fini et supérieur à 0 (arguments invalides, consigne non UTF-8, toute exception) ;
  - `MODELE_DEMANDE_POLE` différent : code 2, rien n'est envoyé ;
  - `ROLE_POLE` est vérifié.
- **Garde avant envoi**
  - au prix plein, sans la remise du lot ;
  - provision de pensée comprise ;
  - `maxOutputTokens` = min(sortie maximale, ce que paie le reste du plafond) ;
  - sous le minimum : code 4, rien n'est envoyé.
- **Coût rendu** : (entrée × prix d'entrée + (sortie + pensée) × prix de sortie) × facteur. Exact sur la forme réelle.
- **Tout échec après le début de la création est compté au pire cas** : `envoye` passe à vrai avant la requête de création (l. 158), et le gestionnaire général le reprend (l. 190-194).
- **`modele_servi`** : jamais nul. Il n'est écrit que s'il est connu (l. 195-196 ; essais l. 124 et 138, sondes).
- **Lecture** conforme à la forme réelle. Seule `STOP` est acceptée. La pensée est exclue du texte.
- **Aucune clé détenue** : seule une clé factice part, et le relais la remplace (essai l. 103).
- **Neutralité** : aucun contenu de sujet. Le `display_name` ne porte que la version et le rôle.

### Constats

- **C-1 — bloquant — la garde du pire cas ne tient le plafond que si la pensée reste sous la provision, et rien ne le vérifie après coup** (l. 147-153 pour la garde, l. 184-189 pour la lecture).
  - L'hypothèse : le pire cas suppose pensée ≤ `thinkingBudget` = provision.
  - Ce que le dépôt sait déjà :
    - la commande d'Argon v3e dit l'interface « démontré[e] » ne comptant **pas** les pensées dans `maxOutputTokens` (`commande_argon_v3e.py` l. 279-281) ;
    - seul le budget de pensée borne donc la pensée, et ce budget n'est pas une borne dure garantie par l'interface ;
    - c'est pourquoi la contre-lecture CL44-02 (« majeur ») a conduit la v3e à rendre le **code 7**, un échec nommé, quand `thoughtsTokenCount` dépasse la provision (l. 270-278).
  - Ce que fait la commande par lot : elle n'a pas cette vérification. Elle ne vérifie pas non plus l'entrée facturée contre l'entrée gardée (avertissement CL44-03 de la v3e).
  - Démontré : pensée 40 000 pour une provision de 8 192, plafond 1,0 USD → **code 0**, coût 1,66 USD, aucune erreur.
  - Le noyau verra `budget_depasse` au-dessus du plafond. Sous le plafond, le dépassement de la provision passe **sans être dit**, et la garantie de somme des plafonds ne tient plus.
  - Correction proposée : reprendre le code 7 de la v3e (pensée au-delà de la provision : échec, coût réel). Signaler aussi une entrée facturée au-dessus de l'entrée gardée et un coût rendu au-dessus de `pire_cas`.
- **C-2 — significatif — « lot annulé » est affirmé même quand l'annulation a échoué** (l. 168-173).
  - Ce qui se passe : toute erreur de l'annulation est avalée (`HTTPError` 403 ou 429 du relais compris), puis la ligne dit « lot … annulé ». C'est un repli silencieux (R5).
  - Démontré avec R-1 : 0 annulation reçue par l'amont, et la ligne dit pourtant « annulé ».
  - De même, les relevés en erreur sont avalés sans trace (l. 175-178) : un 403 du relais (lot inconnu après un redémarrage) fait attendre la commande jusqu'au délai.
  - Le coût reste juste (pire cas).
  - Correction proposée : écrire `annulation` = `faite` ou `echouee : <motif>` dans la ligne. Compter les relevés en erreur, et s'arrêter tôt sur un 403.
- **C-3 — significatif — le délai par défaut ne s'accorde pas avec l'orchestrateur, et la précondition n'est pas dite** (l. 66).
  - Les chiffres :
    - `--delai-s` vaut 3 300 s par défaut ;
    - la durée la plus longue est d'environ 3 300 + intervalle (30) + deux délais de requête (2 × 120), plus le comptage et la création (2 × 120), soit environ 3 810 s ;
    - le délai par défaut de l'orchestrateur est 1 800 s (`pole/adaptateurs.py` l. 622). Il est réglable jusqu'à 7 200 s par `fournisseurs.<nom>.delai_s` (`pole/adaptateur_commande_v67.py`).
  - Ce qui se passe si le réglage manque : le groupe reçoit `SIGKILL`. Il n'y a ni ligne JSON ni annulation. Le noyau compte le plafond, ce qui est prudent, mais le lot court toujours, et son résultat est perdu.
  - L'addendum v4 (l. 159-160) prévoit de relever les délais. La pièce, qui se dit réutilisable, doit dire la condition : délai de l'orchestrateur et de l'enveloppe > `--delai-s` + intervalle + 4 × `--delai-requete-s`.
- **C-4 — significatif — les essais ne testent pas ce qui compte le plus** (`test_commande_gemini_lot_v1.py`).
  - Ce qui manque :
    - aucun essai sur la forme réelle (`resultat-lot.json` : `metadata.output` et `response` à la fois, `name` en tête et sous `metadata`). Elle marche (mes sondes), mais rien ne la fixe ;
    - aucun essai de pensée au-delà de la provision (C-1) ;
    - aucun essai d'annulation qui échoue (C-2) ;
    - aucun essai de création sans `name` en tête.
  - L'essai des échecs au pire cas (l. 123) n'affirme que `cout_usd > 0.3`. Il ne vérifie ni l'égalité au pire cas calculé, ni `pire_cas ≤ plafond`.
  - L'essai du délai (l. 138) ne voit que le cas où l'annulation réussit.
- **C-5 — mineur — `--url-base` n'est pas restreinte à la boucle locale** (l. 56, l. 139). La commande Astra la restreint. Le port par défaut (8792) diffère aussi du défaut du relais v4 (8788).
- **C-6 — mineur — `--facteur-lot` supérieur à 1 est accepté** (l. 121-123). Le coût rendu peut alors dépasser le pire cas gardé. Borner le facteur à ]0, 1], ou le compter dans la garde.
- **C-7 — mineur — un seul prix d'entrée.** Si le modèle a un tarif par paliers de longueur d'entrée, c'est à l'appelant de passer le prix du palier haut. À dire dans l'aide.
- **C-8 — mineur — un refus du relais à la création est compté au pire cas.** Exemple : 429 de `--max-lots`, qui n'envoie rien à l'amont. C'est prudent, donc acceptable, mais à dire.
- **C-9 — mineur — arrondi au bord du pire cas.** Le pire cas calculé peut dépasser le plafond d'un arrondi binaire au bord. La v3e le traite ; ici rien ne le fait.
- **C-10 — mineur — mention de provenance** (l. 4-6). Même remarque que R-8 : provenance seulement, la pièce reste neutre.

## La commande GPT-6 Astra v1 — autorisable

### Ce qui tient

- **Neutralité** : aucun contenu de sujet. L'en-tête ne porte que la provenance.
- **Contrat** : la dernière ligne est toujours un objet JSON avec `cout_usd` supérieur à 0. Rôle et modèle demandé sont vérifiés. L'adresse est limitée à la boucle locale.
- **Garde avant envoi**
  - l'entrée est bornée par les octets du corps + 1 024 (un jeton fait au moins un octet) ;
  - la sortie est bornée par `max_completion_tokens`, qui comprend le raisonnement chez OpenAI ;
  - le point fixe tient compte du corps qui grandit.
- **Prix** : 10 / 50 au palier standard, contexte court. Ils sont sourcés : page versée `099c9496…` et note `bf211a07…`, empreintes vérifiées. La valeur est relue dans les données de la page.
- **Essais** : 50 réussis, couvrant les cas sains et chaque artefact nommé en tête. Ils comprennent la comparaison ligne à ligne avec la commande Kimi v1.

### Constats

- **A-1 — mineur — palier « long » au-delà de 272 000 jetons d'entrée.**
  - Ce qui manque : le prix appliqué ne vaut que jusqu'à 272 000 jetons d'entrée (note de prix). Ni la garde ni le coût rendu ne vérifient `prompt_tokens ≤ 272 000`. Le prix du palier long d'Astra n'est pas dans les données versées (rendu côté client).
  - Pourquoi ce n'est pas atteignable aujourd'hui : la garde par octets limite l'entrée à environ (plafond − 0,2) / 10⁻⁵ octets. À environ 4 octets par jeton, le palier long n'est atteint qu'au-delà d'environ 10 USD de plafond par session. Les plafonds du devis v3 en sont loin.
  - Pour la réutilisation : rendre un échec nommé si `prompt_tokens` dépasse 272 000.
- **A-2 — mineur — arrondi du coût** (l. 60). `round(cout, 6)` peut rendre 0 pour un coût réel inférieur à 5 × 10⁻⁷, ce qui est possible seulement avec des prix réglés très bas. Le noyau compterait alors le plafond (prudent). Arrondir vers le haut, ou appliquer le plancher après l'arrondi.
- **A-3 — mineur — `modele_servi` peut être nul dans une ligne d'erreur** (l. 174), si la réponse n'a pas de `model`. Le relais v4 compatible OpenAI l'empêche par sa barrière (502). Le noyau lirait sinon un refus « modèle servi absent ».
- **A-4 — mineur — essais sur faux relais seulement.** Aucun essai devant le vrai relais v4 compatible OpenAI. Il a cependant été éprouvé en course (journal de relance, course Astra à 1,34 USD).
- **A-5 — information — colonne de prix non identifiée.** La troisième colonne de la ligne (12,5) n'est pas identifiée. La commande ne l'utilise pas.

## Ce qu'il faut avant le scellement des deux pièces non scellées

1. **Commande par lot**
   - vérification après coup de la pensée et de l'entrée, avec le code 7 de la v3e (C-1) ;
   - issue de l'annulation dite dans la ligne (C-2) ;
   - précondition de délai écrite (C-3) ;
   - essais sur `resultat-lot.json`, sur la pensée au-delà de la provision, sur l'annulation qui échoue, et pire cas vérifié exactement (C-4).
2. **Relais v4**
   - annulation hors de la borne des relevés (R-1) ;
   - lot limité à une requête, sans `model` étranger (R-2) ;
   - essais des gardes neuves, et `test_relais_gemini_v4.py` versé pour le rejeu de la suite v2 (R-3).
3. **Nouvelle contre-lecture** du différentiel par un sous-agent neuf.

Ce rapport ne modifie aucune pièce. Le seul fichier écrit est celui-ci.
