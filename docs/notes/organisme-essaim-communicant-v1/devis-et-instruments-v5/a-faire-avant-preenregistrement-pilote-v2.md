# À faire avant le préenregistrement du pilote P-std — v2

- Sous-agent auteur (Claude Opus 5.5), 22 novembre 2026. v2 : garde des formes fausses refaite selon les quatre réserves de la vérification de la v4 (`devis-et-instruments-v4/verification-v1/verification-devis-instruments-essaim-v4-v1.md`, § 6) ; § 9 mis à jour ; § 10 et § 11 ajoutés. Cette pièce n'est pas le préenregistrement : elle liste ce qui ne relève pas du code et doit être tranché ou mesuré avant lui.
- Les points sont tirés de la contre-lecture de la v3 : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v3/contre-lecture-v1/contre-lecture-devis-instruments-essaim-v3-v1.md`, désignée ci-dessous « CL-v3 ».
- Chaque point dit ce qu'il faut, qui le fait, ce que cela coûte, et le critère de « fait ».

## A. Dépense et fournisseur (nœuds de décision du directeur)

### 1. Limite de dépense chez le fournisseur, de 204 USD au plus
- **Quoi.** Un crédit prépayé ou un plafond du compte, chez le fournisseur de Kimi, au plus égal à la borne arrondie au-dessus (203,94 → 204 USD) et réservé à cette course.
- **Pourquoi.** C'est la seule borne qui tienne contre ce qu'un registre local ne voit pas :
  - un registre neuf créé ailleurs, ou réécrit avec son sceau ;
  - une violation de H1 ou de H4 ;
  - un appel hors de H3 (artefact A8) ;
  - des envois cachés par un transport qui mentirait.
- **Qui.** Le directeur (compte, nœud de décision).
- **Fait quand** la limite est lue sur la console du fournisseur et notée au registre des dépenses avec son identifiant.

### 2. Essai de fumée sous GO séparé, pour établir H1 à H4 (CL-v3, § 5.3)
- **H2 — la réflexion est-elle comptée dans `max_tokens` ?**
  - D'abord la documentation du fournisseur.
  - Puis un appel avec `max_tokens = 16` sur une invite qui pousse à réfléchir. Attendu : fin `length`, et `completion_tokens` d'au plus 16, réflexion comprise.
  - Si la réflexion est rendue hors de ce compte, l'adaptateur l'ajoute déjà (artefacts A4 et A4b). Mais il faut savoir dans quel champ le fournisseur la rend, et l'adaptateur doit lire **ce** champ.
- **H3 — un jeton couvre au moins un octet, plus 256 jetons de mise en forme.**
  - Hors ligne, par le découpeur publié de Kimi, sur les textes servis réels avec leur gabarit de conversation. Cela demande un téléchargement, sans dépense : l'accès au réseau est à demander.
  - Contre-épreuve : les jetons d'entrée rendus par l'essai de fumée.
- **H1 et H4 — facture ≤ usage rendu ; un appel échoué coûte au plus sa réserve.**
  - Six appels au plus, sous un plafond de registre de 2 USD : quatre normaux, un délai forcé côté client (requête coupée), un `max_tokens` de 16.
  - Puis rapprochement du journal et de la console de facturation, ligne par ligne.
  - Lire aussi la règle de facturation des requêtes interrompues.
- **Coût.** Moins de 1 USD au tarif de la table (2 / 10 USD par million) : 6 × (8 000 × 2 + 2 000 × 10) / 10⁶ ≈ 0,22 USD. Devis à soumettre ; **GO séparé, ou imputé au GO du pilote** (décision du directeur).
- **Transport.** L'essai passe par le transport réel, qui reste à écrire sous GO. Il doit d'abord passer `epreuves_lanceur_pilote_v3.py` sur le faux fournisseur, avec les mêmes exigences : aucune relance interne, un envoi par appel, `tentatives` rendu, modèle servi vérifié.

### 3. Tarif de Kimi relu sur sa pièce primaire
- Le prix de 2,0 / 10,0 USD par million est repris par citation (`91f5cf8f…`, champ `prix.prop-kimi`).
- À relire à la source et à dater. S'il change, `PRIX_GELES`, la borne et le plafond changent : c'est un nouveau gel, sous un nom neuf.

## B. Mesure (à geler au préenregistrement)

### 4. Case servie gelée
- Contenu exact de la case de matière servie aux proposeurs :
  - format (lignes « z0,…,z7,g,y », nombre de décimales) ;
  - nombre de lignes et budget de jetons ;
  - archive de départ servie (K1, à confirmer : CL-v3, § 6, point 1) ;
  - consigne et grammaire.
- La base doit recevoir **exactement** ce texte, arrondi compris.
- La variante principale calculée en calibration est `case-9000-3d` (529 à 530 lignes, 3 décimales). Le préenregistrement peut retenir une autre forme ; la barre doit alors être recalculée sur cette forme, avant toute course.

### 5. Garde des formes fausses dans la barre — v2, avec les quatre réserves de la vérification de la v4 (§ 6)

**Données de calibration.** `devis-et-instruments-v3/bases-case-servie-v1-sortie.json`, case de 9 000 jetons, 12 mondes de développement, 52 cartes par base.

| base | formes fausses distinctes, mondes 0 à 11 | somme | conditionnelles couvertes |
|---|---|---|---|
| B3R (barre) | 6, 16, 0, 3, 0, 15, 5, 6, 13, 0, 0, 0 | 64 | 10 / 14 |
| B3 (témoin du « trop ») | 15, 16, 0, 11, 4, 16, 9, 14, 12, 4, 2, 10 | 113 | 6 / 14 |

**Définition (réserve 1).** F'(x, w) = formes fausses distinctes du bras ou de la base x dans le monde w, **plus le nombre de cartes « rien »** (tronquées, malformées, non évaluables) : une carte « rien » compte comme une forme fausse.
- Les cartes des bases sont des lois ajustées par programme, donc évaluables par construction.
- Leur nombre de « rien » doit être lu et écrit au gel (attendu : 0). Il n'est pas stocké dans la sortie v3 : c'est à ajouter au script de la barre.

**Règle proposée, avec le facteur de cartes r : r = 48 / 52 pour le bras (a), r = 52 / 52 pour le bras (c).**

| garde | règle | seuil calculé |
|---|---|---|
| 1. Total apparié (réserve 2) | Σ_w F'(x, w) ≤ r × Σ_w F'(B3R, w) + 24 | (a) : 0,923 × 64 + 24 = **83,1** ; (c) : 64 + 24 = **88** |
| 2. Queue appariée, resserrée (réserve 3) | au plus **1 monde sur 12** où F'(x, w) > r × F'(B3R, w) + 8 | — |

- **Pourquoi +8 par monde.** Le repère est B3, qui doit échouer. B3 dépasse r × F'(B3R) + 8 dans **4 mondes** (0, 3, 7 et 11 ; écarts 9,5, 8,2, 8,5 et 10), et son total vaut 113, au-dessus de 83,1. B3 échoue donc aux deux gardes, comme attendu d'une base qui « couvre » des conditionnelles en multipliant les formes fausses.
- **Pourquoi +24 au total.** C'est +2 par monde en moyenne. Le +2 de la v1 portait sur une médiane, que la réserve 2 juge grossière sur 12 mondes presque binaires.
- **Réserve 4.**
  - La même garde s'applique au bras (c), avec r = 1. La lecture « (c) bat la barre » est soumise aux mêmes seuils.
  - Les seuils (83,1 et 88 ; +8 ; 1 monde sur 12) sont **gelés au préenregistrement, avant toute lecture des mondes neufs**. La barre par monde, F'(B3R, w) compris, se recalcule sur les mondes neufs par le code gelé.
- **Variante stricte, à soumettre au directeur** : +0 au total, et aucun monde en queue.
- **Lecture si une garde échoue** : « x ne bat pas la barre, garde des formes fausses », rapporté avec les deux chiffres. Aucune reprise.

### 6. Couverture structurelle, rapportée à côté
- **Constat de CL-v3 (§ 6, point 2)** : la couverture « par attribution » compte une conditionnelle couverte par une carte qui ne porte pas la bonne condition. Exemple : monde 11, effet planté « trait 7, condition 2 », couvert par des cartes « trait 7, conditions 1, 4 ou 5 ».
- **Définition à geler.** Une conditionnelle est couverte *structurellement* si au moins une carte vraie la capte par attribution **et** porte un nœud de condition sur le même trait de condition (`trait_condition`) et un effet sur le même trait (`trait`), signe de la pente compris. Le seuil est libre, dans {−0,5 ; 0 ; 0,5}.
- La métrique décisive reste celle que le préenregistrement choisit. **Recommandation** : rendre la couverture structurelle **décisive pour les conditionnelles**, et garder l'attribution comme lecture secondaire.
- Le script de la barre doit être étendu à cette définition (code à écrire, sans dépense), puis la barre recalculée sur la calibration.

### 7. Précision du test de mort près du seuil
- **Mesure de CL-v3 (§ 7)**, sous le juge isolé, à 400 épisodes :
  - écart-type de la statistique par tranche : environ **0,022**, pour un seuil de 0,02 ;
  - survie : 5 sur 20 à un gain vrai de 0,010 ; 10 sur 20 à 0,020 ; 17 sur 20 à 0,040.
  - Près du seuil, c'est presque pile ou face.
- **Proposition.** Le test de mort ne coûte rien (programme). On passe donc à **n = 8 000 épisodes par verdict** : écart-type attendu ≈ 0,022 × √(400 / 8 000) ≈ 0,0049.
- La précision est écrite au préenregistrement : à n = 8 000, une carte au gain vrai de 0,030 survit avec une probabilité d'environ 0,98, et une carte à 0,010 avec une probabilité d'environ 0,02 (approximation normale, à vérifier par la sonde).
- **À refaire avant le gel** : la sonde de CL-v3 à n = 8 000, sur les 12 mondes de calibration.
- **À expliquer** : l'écart avec la sonde du dossier inachevé (bien plus raide, cartes probablement de faible variance).

### 8. Condition de la R3 (oracle), avant le bras (a)
- La classe de l'oracle est invariante. La statistique du pilote n'est donc pas touchée (CL-v3, § 8).
- **Condition** : aucune projection de l'oracle ou du noyau qui porte une chaîne choisie par un proposeur (identifiant, clé de `lois`) ne revient aux agents.
- **À faire** : construire la projection servie depuis la liste blanche (identifiants donnés par le noyau, nombres seulement), au lieu de la filtrer. Une carte malformée y devient « rien », sans contenu. Cela lève la contradiction de l'oracle v3 inachevé avec le jeu sain de l'auteur. Code à écrire et à éprouver : sur le jeu sain `a1`, et sur les artefacts E1 à E4.

### 9. Ce qui reste du lanceur
- **Exécution.** Le lanceur est séquentiel : 744 appels d'environ 12 800 jetons de sortie prendront plusieurs jours. Toute version parallèle demande de nouvelles épreuves, avec une réserve cumulée des appels en vol.
- **Chemin du registre** : fixé en v5 (§ 11).

### 10. Transport réel (renvoi de la v5 : A3 et A4 sous leur forme réelle)
- **Le code seul ne peut pas arrêter deux défauts** (`epreuves-lanceur-pilote-v3.json`, cas « sous transport admis ») :
  - un transport admis qui relance en cachette et rend `tentatives = 1` : 529,34 USD facturés pour 176,45 comptés ;
  - une réflexion facturée mais absente de l'usage rendu : 235,97 USD facturés.
- **Le transport réel est écrit et versé** : `docs/notes/organisme-essaim-communicant-v1/transport-kimi-reel-v1/`.
  - `transport_kimi_reel_v1.py` (`4bba649c…`) : un seul envoi par appel, compté sur la connexion, réflexion lue dans `completion_tokens_details.reasoning_tokens`, champ absent ⇒ `usage = None`, donc réserve entière.
  - `adaptateur_kimi_strict_v1.py` (`6b8e9553…`) : classe exacte du transport et empreinte de son module.
  - Le lanceur v3 de ce dossier n'admet qu'eux, en classe exacte et à ces empreintes (`ADAPTATEURS_ADMIS_PILOTE`, `TRANSPORTS_ADMIS_PILOTE`).
  - Éprouvé ici contre le faux serveur de ce dossier : `epreuves-lanceur-pilote-v3.json`, cas « réel ».
- **Reste à faire avant le GO** :
  - la relecture de ce transport par un sous-agent neuf ;
  - les points 1 à 7 de son LISEZMOI (§ 5), à relever dans la documentation du fournisseur.
- **Contrôle à l'essai de fumée (point 2)** :
  - le nombre de requêtes vues sur la console du fournisseur égale le nombre d'appels du journal ;
  - la facture égale l'usage rendu.
- **Ce qui reste couvert seulement par la limite de 204 USD** : un transport fautif malgré tout, ou un détenteur de la clé du sceau qui réécrirait aussi l'ancre.

### 11. Chemins du pilote, à citer dans le GO
- Registre : `runs/pilote-essaim-pstd/registre-depense-v2.jsonl` (sous la racine du dépôt), écrit en dur dans `lanceur_pilote_essaim_v3.py` (`REGISTRE_PILOTE_REL`).
- Ancre et clé du sceau : `~/.local/state/controle-ia/pilote-essaim-pstd/`, hors du dépôt (`ETAT_PILOTE`).
- **Au directeur** : faut-il placer l'ancre ailleurs (machine qui survit à la session, ou copie tenue par le directeur) ? Dans un conteneur de session, ce dossier peut disparaître avec la session.
- **Voie unique** : `courir_pilote()`, qui ne prend aucun chemin. `_courir()` ne sert qu'aux épreuves.
