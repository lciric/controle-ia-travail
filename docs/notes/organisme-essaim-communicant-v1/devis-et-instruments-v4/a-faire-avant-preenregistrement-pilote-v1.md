# À faire avant le préenregistrement du pilote P-std — v1

- Sous-agent auteur (Claude Opus 5.5), 22 novembre 2026. Cette pièce n'est pas le préenregistrement : elle liste ce qui ne relève pas du code et doit être tranché ou mesuré avant lui.
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
- **Transport.** L'essai passe par le transport réel, qui reste à écrire sous GO. Il doit d'abord passer `epreuves_lanceur_pilote_v2.py` sur le faux fournisseur, avec les mêmes exigences : aucune relance interne, un envoi par appel, `tentatives` rendu, modèle servi vérifié.

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

### 5. Garde des formes fausses dans la barre — proposition chiffrée
- **Données de calibration.** Formes fausses distinctes par monde, sur la case de 9 000 jetons : `devis-et-instruments-v3/bases-case-servie-v1-sortie.json`, 12 mondes de développement, 52 cartes par base.

| base | formes fausses distinctes, mondes 0 à 11 | médiane | maximum | conditionnelles couvertes |
|---|---|---|---|---|
| B3R (barre) | 6, 16, 0, 3, 0, 15, 5, 6, 13, 0, 0, 0 | 4 | 16 | 10 / 14 |
| B3 | 15, 16, 0, 11, 4, 16, 9, 14, 12, 4, 2, 10 | 10,5 | 16 | 6 / 14 |
| B3R, 2 000 instances (référence) | 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8 | 0 | 8 | 13 / 14 |

- **Proposition.** (a) ne « bat la barre » sur les conditionnelles que si les deux gardes tiennent, en plus du critère principal :
  1. **Garde médiane** : la médiane sur les mondes de d_w = F(a, w) − F(B3R, w) × 48 / 52 est au plus **+2**. F est le nombre de formes fausses distinctes ; 48 / 52 ramène B3R au nombre de cartes de (a).
     - Raison : +2 vaut la moitié de la médiane de B3R. Une médiane de (a) à 6 reste ainsi sous celle de B3 (10,5). Une base qui « gagne » des conditionnelles en multipliant les fausses ne passe pas.
  2. **Garde de queue** : au plus **2 mondes sur 12** où F(a, w) > 16, maximum de calibration des deux bases.
- **Variante plus stricte, à soumettre au directeur** : marge +0, c'est-à-dire pas plus de formes fausses que la barre.
- **Lecture si la garde échoue** : « (a) ne bat pas la barre, garde des formes fausses », rapporté avec les deux chiffres. Aucune course de reprise.
- Cette proposition est réglée sur les mondes de calibration seulement ; les mondes neufs du pilote ne sont pas lus.

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
- **Chemin du registre.** Il doit être fixé une fois, par exemple `runs/pilote-essaim-pstd/registre-depense-v1.jsonl`, et cité dans le GO. Le lanceur ne doit en accepter aucun autre.
