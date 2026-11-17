# Devis de la machine louée du crible (v) — v1

Pièce de la procédure `procedure-machine-crible-v-v1.md` (même dossier). Les montants des proposeurs et de la sonde neuve sont
ceux du texte qui fera foi (`crible-v-version-foi-v2.md`, sous-section « Devis refait sur le pilote MR-2 (fait foi) ») :
**ils ne sont pas refaits ici** ; seuls la machine, sa durée et ses bornes sont chiffrés, par les règles écrites du texte.

## 1. Offre et bornes (garde de l'outil de la session, jouée sur chaque offre de la recherche)

| borne | valeur | source |
|---|---|---|
| processeur | amd64, au moins 4 cœurs effectifs (génération des 20 mondes en 4 processus) | procédure, § 3, geste 4 |
| mémoire, disque | 8 000 Mo, 20 Go (`--disk 20`) | idem |
| fiabilité, débit | ≥ 0,98 ; ≥ 100 Mb/s descendant | modèle de l'idée 1.1 |
| carte graphique | admise, inutilisée (leçon du pilote v13 : aucune offre à processeurs seuls) | PROC-14, § 2 |
| prix garde (prix total + stockage de 20 Go) | **≤ 0,15 USD/h** | PROC-14, § 0 |
| prix relu après création | **≤ 0,17 USD/h**, sinon destruction aussitôt | PROC-14, § 2, point 9 |
| image | `python:3.13-bookworm` ; numpy 2.5.3 installé par pip (900 s au plus) | configuration v12 (`numpy_exige`) |
| minuterie | **17 h** (61 200 s) après l'impression de la commande | budget de pire cas du texte (≤ 17 h) |

## 2. Pire cas (règle (a) du texte : inchangé)

- Machine : 17 h × 0,17 USD/h = **2,89 USD**, sous la **part machine de 3,00 USD** de κv2 (la garde de dépense refuse dès que le
  cumul relevé plus une heure au prix relu atteint 3 USD : destruction par l'identifiant).
- Arrêt « stopped » avant destruction (minuterie à l'échéance, cinquième demande) : stockage seul, compris dans le prix garde.
- Trafic : paquet de l'arbre (3,6 Mo), numpy (≈ 20 Mo), poussées de traces (quelques Mo) ; prix du réseau de l'offre imprimés au
  geste 4 et consignés ; ordre de grandeur sous 0,01 USD aux prix usuels (non borné par le code : à relire sur l'offre).
- Proposeurs (texte, inchangés) : κv1 104,39 USD (Pr-2 40, Pr-4 60, sonde 4,39), κv2 100,28 USD (Pr-1 46,80, Pr-3 46,80, machine
  3, sonde 3,68) ; plafond de chaque relais = (mondes de sa file) × plafond de session ; part d'un fournisseur atteinte : arrêt.

## 3. Attendu (règle (b) du texte : durée attendue × prix relu au pilote)

- Texte : **machine attendue entre 0,16 et 0,89 USD** (0,052222 USD/h relu au pilote ; appels ≈ 2 h 37 min à M = 1, barrières
  1 h 40 min au plus, plus les quatre durées non relevées ; borne haute 17 h).
- Sonde neuve : 0,10 USD attendu, 8,07 au pire (texte).
- **Ajouts propres à ce code, à dire** (non comptés par la règle du budget, réserve (2) du texte) : l'essai à blanc sur la machine
  (80 appels factices, une coupure simulée par file à 60 s : quelques minutes de plus que la préparation) ; la sonde neuve (8 appels,
  quelques minutes) ; la préparation des mondes est refaite par `preparer`, l'essai à blanc, le crible et la mesure (oracle de
  12 000 instances par monde, C-16, C-17) — durée relevée au § 4 sur le poste de développement, à titre d'information.

## 4. Durées relevées sur le poste de développement (information ; aucune n'entre dans D, qui se relève sur la machine du pilote)

Poste à 4 processeurs partagés avec d'autres sessions (charge 9 à 13 pendant les relevés) : bornes hautes, jamais des attendus.

| étape | durée relevée | conditions |
|---|---|---|
| génération des 20 mondes d'essai (`generer`, 3 processus) | 71 min 17 s (23:58:05 → 01:09:22 UTC) | 40 tirages, dont 20 refusés (C3, C5, C6, C8) ; charge 9 à 13 |
| `preparer` (20 oracles, C-16, C-17, textes servis) | 5,1 s (répétition, état `preparer`) | mondes déjà tirés |
| essai à blanc complet M = 1 (préparation, 80 appels factices, une coupure à 20 s) | 34 s (01:28:02 → 01:28:36) | relais factices |
| essai à blanc complet M = 2 (8 relais, deux coupures) | 33 s (01:28:36 → 01:29:09) | idem |
| mesure (lanceur) puis lecture, cartes factices | 51 s (01:30:17 → 01:31:08) | 20 mondes, 10 000 rééchantillons |
| mesure sur le jeu de cartes de référence (programme seul) | 11 s (01:31:11 → 01:31:22) | 20 mondes, 55 cartes valides |
| énumération exacte du placebo, pire cas (n_c = 20, k_R = 10, 184 756 ensembles) | **0,364 s** (le plus long de 0,364 et 0,317 s) | programme de mesure lui-même (réserve (5) du texte levée : 0,291 s au programme de remplacement) |
| répétition de la machine, cas nominal (barrières jouées par programme, crible à blanc) | 2 min 15 s d'états (mise en place → fini) | mondes d'essai recopiés, sans pip |

La génération des mondes domine : sur la machine louée (4 processeurs effectifs au moins, sans autre charge), l'ordre de grandeur
attendu est de 15 à 25 minutes (environ 95 min de calcul processeur ici pour 40 tirages : trois processus d'environ 32 min chacun, relevé approché par `ps`) ; c'est une
information pour la mère, **non une durée relevée au sens de la règle** (le terme « génération » de D se relève au journal d'états de
la machine du pilote, rapporté à 20 mondes).

## 5. Ce que ce devis ne fait pas

- Il ne refait ni les attendus des proposeurs, ni les pires cas, ni les lignes κv1 et κv2 (texte, règle (a)).
- Il ne donne pas D : les quatre durées se relèvent sur le journal d'états de la machine du pilote (texte, « Devis ») ; sans elles,
  le budget reste « non lançable » (mot de la mère), et l'outil de la session refuse une fiche de lancement dont D est hors de la
  règle.
- Il ne lit aucun prix en ligne : les prix de l'offre se lisent au geste 4 (recherche, lecture seule), le prix relu au geste 9.
