# Devis — serveur loué pour l'essai 3 du palier 0b (étapes 3 à 6) — v4

Pièce de travail (classe C), session du compte organisme, 2026-11-21 vers 18:40Z. Remplace la v3 (`devis-serveur-loue-palier-0b-essai-3-v3.md`, `9446eba4…`, même dossier, intacte) après sa vérification (`contre-lecture-devis-v1/verification-devis-serveur-palier-0b-v3-v1.md`, « À corriger », `dddb9a33…`) ; chaîne antérieure : vérification de la v2 (`4c104467…`), contre-lecture de la v1 (`f5229859…`), même dossier. Accord de principe : GO-2026-11-21-66 (« go serveur », plafond sur devis) ; dépenses sur devis : GO-2026-11-21-69. **Rien n'est créé avant que la mère inscrive la ligne.**

## 1. Ce que la mesure dit, et ce qu'elle ne dit pas
Essai court du 21 novembre : `tenue-essai-court-v1/mesure-essai-court.txt` et `journal-de-tenue-essai-court.txt` (même dossier).
- Étape 3 : environ 9 min 20 s.
- **La projection de l'étape 4 n'est pas bornée par la mesure.** La formule du complément, (t − t3) × 648 / (n − 1), donne 94,6 h à n = 2 (Δt = 525,8 s, ligne de 17:49:47Z du journal de tenue), 60,3 h à n = 4, 17,4 h à n = 12 et 10,7 h à n = 20 (vérification de la v2, ligne 2). Le compte n avance par paquets : de 17:46Z à 17:57Z, n reste à 1 ou 2 pendant que le dossier gagne environ 5 600 fichiers par minute ; de 17:57Z à 17:59Z, n passe de 2 à 20 pendant que l'écriture tombe à environ 1 500 fichiers par minute. Les 20 dossiers lus portent tous le même proposeur et la dose 0 (chemins `etape-4/couche-mecanique/bras-1-a-3/sourd-egal/0.0/0` à `…/19` du dossier des sorties ; les doses du plan sont 0, 0,25 et 0,5 : préenregistrement v19, l. 208, dans la racine, `/home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md`) ; le coût des blocs aux doses 0,25 et 0,5 n'est pas mesuré.
- **Fourchette retenue : de 10,7 h à 95 h pour l'étape 4** ; 95 h est **le relevé le plus pessimiste observé, non une borne établie**. Sans les étapes 5 et 6 ni la garde 27.
- **Place**, en octets alloués, par la formule de la mesure, s4 × 648 / (n − 1), sur le s4 relevé au même instant : 24,4 Go à n = 20 ; **218,6 Go à n = 2** (337 301 504 × 648 / 1 = 218 571 374 592 octets, ligne de 17:49:47Z), retenu comme relevé le plus pessimiste. Les 320 Go du disque couvrent 218,6 Go, plus la racine (3,4 Go), et il reste environ 98 Go : **un reste, non une mesure** ; la place des étapes 5 et 6 et des archives n'est pas mesurée. L'arrêt de place du gardien (sous 8 Go libres) la garde.
- Calcul sur un seul processus actif à la fois (journal du gardien) : supposé, non éprouvé.

## 2. Offre
Hetzner, relevé par l'interface publique le 2026-11-21 vers 18:03Z (prix horaires toutes taxes comprises, EUR ; seul le prix de la cpx32 est corroboré par le registre des dépenses) :
- **cpx42, emplacement hel1** : 8 cœurs partagés, 16 Go, **320 Go de disque**, 0,1134 EUR/h ; plus l'adresse IPv4, 0,00096 EUR/h (registre, 11 novembre). Le disque couvre le relevé le plus pessimiste de la place, plus la racine (3,4 Go).
- Facturation à l'heure entamée (registre).
- Système : debian-13.

## 3. Durée, coût, plafond
- **Vie du serveur bornée à 98 h depuis sa création H0**, avec trois heures fixes, toutes lues sur H0 :
  - **H0 + 94 h** : arrêt de durée du gardien, quelle que soit la durée de la mise en place ; au-delà du relevé le plus pessimiste de l'étape 4 (94,6 h) si la mise en place prend moins de 4 h, sinon l'étape 4 peut ne pas finir, et c'est dit ;
  - de H0 + 94 h à H0 + 98 h : versement des sorties et des journaux ;
  - **H0 + 98 h** : destruction (§ 5).
- Coût à H0 + 96 h : 96 × (0,1134 + 0,00096) = **10,98 EUR**, soit environ **13,73 USD** au taux de 1,25 ; à H0 + 98 h : 11,21 EUR, soit 14,01 USD.
- **Plafond demandé : 15,00 USD**.
- **Point de relevé à 6 h de marche** : la session lit n, les fichiers, les octets alloués et t3 dans la pièce versée (§ 6 (a)), refait la projection, et l'envoie à la mère. Si la projection dépasse H0 + 94 h, la mère décide : arrêt et destruction, ou devis neuf.

## 4. Ce qu'il faut faire avant la création (sans dépense)
1. **Lanceur v3** : racine, interpréteur et dossier des sorties passés en paramètres (le lanceur v2 les a codés en dur pour l'essai court et ce conteneur : `/home/user/palier-0b-racine`, `/home/user/controle-ia-travail/.venv/bin/python`, `etapes-3-a-6-essai-court-mesure-v1`). La commande reste celle du complément 1 v3, à l'octet, à ces trois chemins près. Écrite par un auteur O, vérifiée par S.
2. **Gardien v4** : arrêt de durée à une heure absolue passée en paramètre (H0 + 94 h) ; arrêt de mesure désarmé ; arrêt de place gardé. Même chaîne d'écriture et de vérification.
3. **Préparation du serveur**, écrite et contre-lue : interpréteur et environnement du dépôt, racine à `d7f949ac`, contrôle de l'empreinte du programme (`1f04cb46…`).

## 5. Destruction et versement
- **Destruction par l'identifiant du serveur**, consignée dans `registres/arrets.md`. L'arrêt du gardien ne suffit pas : un serveur arrêté reste facturé.
- **Ordre des deux règles** : en marche normale, destruction dès le versement prouvé. **À H0 + 98 h, la destruction prime sur le versement** : si le versement n'est pas fini, celui qui a créé le serveur (le poste local, voie (a)) le détruit quand même par son identifiant, et écrit ce qui n'a pas été versé. L'heure de création H0, lue dans la réponse de l'interface de Hetzner, est écrite au registre des dépenses à la création. Coût à H0 + 98 h : 98 × 0,11436 = 11,21 EUR, soit 14,01 USD, sous le plafond (atteint vers 104,9 h de vie). Que la mère sache détruire par l'interface n'est pas éprouvé : le repli repose sur le poste qui a créé le serveur, qui l'a déjà fait (registre des dépenses, 11, 12 et 21 novembre). Aucune destruction automatique depuis le serveur (elle demanderait d'y déposer le jeton de l'interface).
- **Versement** : inventaires et compagnons à chaque étape close, puis le tout vers `recuperation/palier-0b-programme-1-essai-3-v1`. Le versement depuis un serveur n'a jamais été éprouvé dans le programme : il se fait depuis le poste qui a créé le serveur.

## 6. Qui crée et alimente le serveur
Depuis ce conteneur, je n'ai éprouvé ni une connexion sortante vers un serveur (le réseau passe par un relais de sortie, en HTTPS), ni l'accès d'un serveur au dépôt privé. Toutes les machines Hetzner du programme ont été créées depuis le poste local de Lazar (registre des dépenses, 11, 12 et 21 novembre).
- **(a) Création, lancement, relevés, versement et destruction depuis le poste local de Lazar, sur ces pièces : voie éprouvée. Recommandée**, confiance moyenne. Dans cette voie :
  - **la racine** arrive sur le serveur depuis le poste local, qui a accès au dépôt privé, **par une copie de l'arbre du commit `d7f949ac`** envoyée du poste au serveur par sa connexion chiffrée. **Aucun accès au dépôt privé n'est déposé sur le serveur** : le clonage depuis le serveur est écarté. Puis contrôle du commit écrit avec la copie et de l'empreinte du programme (`1f04cb46…`) avant tout départ ;
  - **le relevé à 6 h** : le poste lit sur le serveur les dernières lignes du journal de tenue et l'heure de dernière modification du manifeste de l'étape 3, t3 (noms, comptes, tailles et heures seulement), les verse sur `recuperation/palier-0b-programme-1-essai-3-v1`, et la session du compte organisme refait la projection depuis cette pièce versée ;
  - le versement et la destruction se font aussi depuis le poste.
- (b) Création depuis ce conteneur par l'interface de Hetzner : alimentation et versement non éprouvés, accès au dépôt privé absent.
- (c) Essai 3 sur le processeur de ce conteneur : la place ne tient plus au relevé le plus pessimiste (218,6 Go contre 38,7 Go libres) et la durée (jusqu'à 95 h) rend une relance entière peu sûre entre des redémarrages fréquents.
