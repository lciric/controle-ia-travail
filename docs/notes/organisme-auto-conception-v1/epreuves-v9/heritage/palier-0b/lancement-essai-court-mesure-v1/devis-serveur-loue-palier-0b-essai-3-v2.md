# Devis — serveur loué pour l'essai 3 du palier 0b (étapes 3 à 6) — v2

Pièce de travail (classe C), session du compte organisme, 2026-11-21 vers 18:20Z. Remplace la v1 (`devis-serveur-loue-palier-0b-essai-3-v1.md`, même dossier, intacte) après sa contre-lecture (`contre-lecture-devis-v1/contre-lecture-devis-serveur-palier-0b-v1.md`, « À corriger », `f5229859…`). Accord de principe : GO-2026-11-21-66 (« go serveur », plafond sur devis) ; dépenses sur devis : GO-2026-11-21-69. **Rien n'est créé avant que la mère inscrive la ligne.**

## 1. Ce que la mesure dit, et ce qu'elle ne dit pas
Essai court du 21 novembre : `tenue-essai-court-v1/mesure-essai-court.txt` et `journal-de-tenue-essai-court.txt` (même dossier).
- Étape 3 : environ 9 min 20 s.
- **La projection de l'étape 4 n'est pas bornée par la mesure.** La formule du complément, (t − t3) × 648 / (n − 1), donne 94,8 h à n = 2, 60,3 h à n = 4, 17,4 h à n = 12 et 10,7 h à n = 20 (contre-lecture, ligne 1). Le compte n avance par paquets : de 17:46Z à 17:57Z, n reste à 1 ou 2 pendant que le dossier gagne environ 5 600 fichiers par minute ; de 17:57Z à 17:59Z, n passe de 2 à 20 pendant que l'écriture tombe à environ 1 500 fichiers par minute. Les 20 dossiers lus appartiennent tous au premier bloc (un proposeur, la dose 0) ; le coût des blocs aux doses 0,25 et 0,5 n'est pas mesuré.
- **Fourchette retenue : de 10,7 h à 95 h pour l'étape 4**, sans les étapes 5 et 6 ni la garde 27. La place, en octets alloués, est projetée à 24,4 Go à n = 20 ; sur la même base, elle irait jusqu'à environ 232 Go à n = 2 (716 492 800 × 648 / 2 = 232 143 667 200 octets, borne haute grossière ; mesure de s4 prise à n = 20, appliquée à n = 2, donc majorante).
- Calcul sur un seul processus actif à la fois (journal du gardien) : supposé, non éprouvé.

## 2. Offre
Hetzner, relevé par l'interface publique le 2026-11-21 vers 18:03Z (prix horaires toutes taxes comprises, EUR ; seul le prix de la cpx32 est corroboré par le registre des dépenses) :
- **cpx42, emplacement hel1** : 8 cœurs partagés, 16 Go, **320 Go de disque**, 0,1134 EUR/h ; plus l'adresse IPv4, 0,00096 EUR/h (registre, 11 novembre). Le disque couvre la borne haute grossière de la place, plus la racine (3,4 Go).
- Facturation à l'heure entamée (registre).
- Système : debian-13.

## 3. Durée, coût, plafond
- **Durée bornée à 96 h**, soit la borne haute de l'étape 4, arrondie.
- Coût à la borne : 96 × (0,1134 + 0,00096) = **10,98 EUR**, soit environ **13,73 USD** au taux de 1,25.
- **Plafond demandé : 15,00 USD**.
- **Point de relevé à 6 h de marche** : la session lit n, les fichiers et les octets alloués dans le journal du gardien, refait la projection, et l'envoie à la mère. Si la projection dépasse la borne de 96 h, la mère décide : arrêt et destruction, ou devis neuf.

## 4. Ce qu'il faut faire avant la création (sans dépense)
1. **Lanceur v3** : racine, interpréteur et dossier des sorties passés en paramètres (le lanceur v2 les a codés en dur pour l'essai court et ce conteneur : `/home/user/palier-0b-racine`, `/home/user/controle-ia-travail/.venv/bin/python`, `etapes-3-a-6-essai-court-mesure-v1`). La commande reste celle du complément 1 v3, à l'octet, à ces trois chemins près. Écrite par un auteur O, vérifiée par S.
2. **Gardien v4** : arrêt de durée à 96 h ; arrêt de mesure désarmé ; arrêt de place gardé. Même chaîne d'écriture et de vérification.
3. **Préparation du serveur**, écrite et contre-lue : interpréteur et environnement du dépôt, racine à `d7f949ac`, contrôle de l'empreinte du programme (`1f04cb46…`).

## 5. Destruction et versement
- **Destruction par l'identifiant du serveur**, consignée dans `registres/arrets.md`, après versement prouvé. L'arrêt du gardien ne suffit pas : un serveur arrêté reste facturé.
- **Repli** : si personne n'a détruit le serveur 2 h après la borne de 96 h, la mère ou Lazar le détruit par son identifiant. Aucune destruction automatique depuis le serveur (elle demanderait d'y déposer le jeton de l'interface).
- **Versement** : inventaires et compagnons à chaque étape close, puis le tout vers `recuperation/palier-0b-programme-1-essai-3-v1`. Le versement depuis un serveur n'a jamais été éprouvé dans le programme : il se fait depuis le poste qui a créé le serveur.

## 6. Qui crée et alimente le serveur
Depuis ce conteneur, je n'ai éprouvé ni une connexion sortante vers un serveur (le réseau passe par un relais de sortie, en HTTPS), ni l'accès d'un serveur au dépôt privé. Toutes les machines Hetzner du programme ont été créées depuis le poste local de Lazar (registre des dépenses, 11, 12 et 21 novembre).
- **(a) Création, lancement, relevés, versement et destruction depuis le poste local de Lazar, sur ces pièces : voie éprouvée. Recommandée**, confiance moyenne.
- (b) Création depuis ce conteneur par l'interface de Hetzner : alimentation et versement non éprouvés, accès au dépôt privé absent.
- (c) Essai 3 sur le processeur de ce conteneur : la place ne tient plus à la borne haute (38,7 Go libres) et la durée (jusqu'à 95 h) rend une relance entière peu sûre entre des redémarrages fréquents.
