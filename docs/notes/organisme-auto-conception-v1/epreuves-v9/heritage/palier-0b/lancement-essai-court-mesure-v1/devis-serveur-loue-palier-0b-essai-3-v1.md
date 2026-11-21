# Devis — serveur loué pour l'essai 3 du palier 0b (étapes 3 à 6) — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21 vers 18:05Z. Accord de principe : GO-2026-11-21-66 (« go serveur », plafond sur devis) ; autonomie et dépenses sur devis : GO-2026-11-21-69. **Rien n'est créé avant que la mère inscrive la ligne.**

## 1. Base de la projection (mesurée, bornes basses)
Essai court du 21 novembre, conteneur de la session, processeur seul : `tenue-essai-court-v1/mesure-essai-court.txt` (même dossier).
- Étape 3 : environ 9 min 20 s (départ 17:31:42Z, manifeste de l'étape 3 à 17:41:01Z).
- Étape 4, arrêtée à n = 20 dossiers de source sur 648, dossier prouvé figé : durée projetée **38 418 s (10,7 h)**, place projetée **24,4 Go alloués** (13,5 Go apparents). Bornes basses : ni la garde 27, ni les étapes 5 et 6.
- Le gardien n'a vu qu'un membre actif à la fois : calcul **sur un seul cœur**, sans parallélisme observé (supposé, non éprouvé).
- Racine (arbre de travail à `d7f949ac`) : 3,4 Go.

## 2. Offre retenue
Hetzner, relevé par l'interface publique le 2026-11-21 vers 18:03Z (prix horaires toutes taxes comprises, EUR) :
- **cpx42, emplacement hel1** : 8 cœurs partagés, 16 Go de mémoire, 320 Go de disque, **0,1134 EUR/h**. Choisie pour la marge de mémoire (consommation de pointe non mesurée) et de disque (24,4 Go + 3,4 Go + étapes 5 et 6 + archives).
- Repli : cpx32, hel1 (4 cœurs, 8 Go, 160 Go, 0,0577 EUR/h), la machine des courses de l'organisme du 11 et du 12 novembre, si la mère préfère le moins cher.
- Système : debian-13, comme les précédents.

## 3. Durée et coût
- Durée bornée à **30 h** : 10,7 h projetées pour l'étape 4, plus 9 min pour l'étape 3, plus une marge de près de trois fois pour les étapes 5 et 6, la garde 27 et un processeur plus lent que celui du conteneur.
- Coût : 30 h × 0,1134 EUR = **3,40 EUR**, soit environ **4,25 USD** au taux de 1,25 du registre des dépenses.
- **Plafond demandé : 6,00 USD**, mise en place et versement compris. Au plafond, ou à 30 h, arrêt et inventaire, sans relance.

## 4. Tenue
- Mêmes pièces que l'essai court, vérifiées « Conforme » : lanceur `lancer-essai-court-v2.sh` (dossier des sorties `etapes-3-a-6-essai-3` du complément 1 v3), script de départ v2, gardien v3 avec la seule règle d'arrêt de place (aucun arrêt de mesure pour l'essai 3) ; le paramétrage se fixe avant la création et se contre-lit.
- Versement à chaque étape close (inventaire, compagnon), puis du tout vers la branche `recuperation/palier-0b-programme-1-essai-3-v1`.
- **Destruction par l'identifiant du serveur**, consignée dans `registres/arrets.md`, après versement prouvé ; aucune destruction par motif.

## 5. Point ouvert : qui crée et alimente le serveur
Depuis ce conteneur, je n'ai éprouvé ni la connexion sortante vers un serveur (le réseau passe par un relais de sortie, en HTTPS), ni l'accès d'un serveur au dépôt de travail, qui est privé. Les machines Hetzner du programme ont toutes été créées depuis le poste local de Lazar (registre des dépenses, 11, 12 et 21 novembre).
- (a) Création et lancement depuis le poste local de Lazar, sur ces pièces : voie éprouvée. **Recommandée**, confiance moyenne.
- (b) Création depuis ce conteneur par l'interface de Hetzner, alimentation par le script de démarrage du serveur : demande un accès du serveur au dépôt privé, que je n'ai pas.
- (c) Essai 3 sur le processeur de ce conteneur : la règle de place du complément tient (38,7 Go libres contre 24,4 Go + 4 Go), mais 10,7 h au moins entre des redémarrages fréquents (trois le 21) rendent la relance entière peu sûre, comme la mesure le dit.
