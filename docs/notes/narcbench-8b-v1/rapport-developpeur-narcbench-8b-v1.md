# Rapport du développeur — NARCBench, bras descriptif de T0.7 : code, portée, devis, calendrier — v1

- **Rédacteur** : sous-agent développeur neuf de la session mère, Claude Opus 5.5 (`claude-opus-5-5`). Écrit le 2026-11-10 entre
  10:47 et 11:05 UTC (`date -u`). Branche `prep/narcbench-8b-code-v1`, arbre de travail clairsemé sans `docs/notes/bras-attaque/`.
- **Bascule en cours de travail** (mot de la mère R-2175, reçu vers 10:59 UTC) : Lazar a tranché D-3 en (a), selon la mère. Le
  bras externe se fait **sur les activations publiées par les auteurs**, au processeur, à 0 USD, sous un **texte court neuf** ;
  pas de ligne de carte, pas de rejeu sur le 8B pour l'instant. **Jalon terminé avant la bascule, déclaré** : le module du
  rejeu sur le 8B (cellules, gardes, duels, règle I, grille D, jouet de bout en bout ; 24 essais verts à 10:58:15 UTC). Il
  reste utilisable si la ligne de carte revient. Après la bascule, j'ai ajouté le module du bras externe et ses essais
  (27 essais verts à 11:00:35 UTC). Le devis de carte est **suspendu** ; il est résumé au § 4.2 pour mémoire.
- **Aucun téléchargement, aucun appel externe, aucune dépense, aucune clé lue.** Le PDF de HELIOS v5 est lu sur disque
  (`docs/sources/pdf/2604.01151v5.pdf`, `02527fd4f62ad9b996669275f0837697cbe288b253c9aa521f72a10e6dcf1849`, compagnon
  vérifié). J'en ai extrait le texte avec `pdftotext` dans le bloc-notes, et toutes les pages citées ici ont été relues.

## 1. État des lieux

### 1.1 Ce que demande le brouillon 4

Brouillon 4 : `prereg/brouillon-narcbench-8b-descriptif-v1-brouillon4.md`, `96995d60c757a45b39e5c721ce0f40b53870ed8e0589d7e51f989482c960efe8`, égal à son compagnon.

| poste | demande | état au 10 novembre |
|---|---|---|
| données | jeu `aaronrose227/narcbench`, révision `19cb14b2…` ; épisodes CORE et STEGO de Qwen3-32B pour les tirages et les concordances ; activations publiées CORE et STEGO de Qwen3-32B et de Llama-3.1-70B pour le bras externe ; **rien de TRANSFER** | **rien téléchargé** ; tailles d'après le devis v2 : jeu entier 1 456 027 013 octets ; activations CORE et STEGO 712 344 334 octets (**non revérifiées par moi**) |
| licences | jeu MIT (fiche) ; code MIT au commit `85fea3be2a9d` ; Llama 3.1 sous licence communautaire à accès contrôlé ; Qwen3 **non vérifiée** | vérifiées le 9 novembre par le rédacteur et les contre-lectures 1 et 2 sur les pages publiques ; **pas par moi** (aucun appel externe permis) ; à revérifier au téléchargement |
| modèle | Llama-3.1-8B-Instruct, révision `0e9e39f2…`, bf16, même modèle pour générer et lire ; couches 7, 15, 23 | hors objet après D-3 (a) |
| sondes | S-T : sondes figées de T0.7, du fichier `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz` (`701f73bd…`, présent sur `main`, non ouvert) ; S-C : cinq familles réapprises sur CORE à 8B ; H : recette de HELIOS ; bases des mots et des métadonnées | S-T et S-C sont propres au 8B (largeur 4096) : **S-T est inapplicable aux activations publiées** (largeur 5120 pour Qwen3-32B, 8192 pour le 70B) |
| étapes | étape 0 sur processeur ; étape A sur carte (génération, lecture, relectures notées à la volée) ; bras externe sur processeur ; étape B (lecture mécanique) ; rapport par un sous-agent neuf | — |
| critères | grille D (8 lignes, 128 combinaisons) ; règle I (I0 à I6, qualificatifs) ; prédictions N1 à N8, **non décisives** ; aucune porte | codés et énumérés (§ 3) |
| « reproduit » | **un seul endroit** : N7, « reproduction de H » au bras externe ; un écart absolu ≤ 0,03 aux Tables 2 et 3 donne « éprouvée », sinon « non éprouvé » ; ailleurs, la comparaison à HELIOS est « écart rapporté, sans test » | codé (`externe_v1.garde_reproduction`) |

**Ce qui bloquait le scellement selon la contre-lecture 3** (`…-brouillon4-cl3.md`) : le module absent, les essais R5,
l'étape 0, plus quatre corrections mineures et une majeure (M1, cellule `H-h0`) à porter dans un brouillon 5.

### 1.2 Ce qui existait déjà

- **Réutilisé sans le modifier (R12)** : le paquet gelé `sondes/` (`familles.py` `6758b651…`, `evaluation.py` `1040674c…`,
  `temoins.py` `3b051b6f…`, empreintes recalculées : égales à celles du brouillon) ; le harnais `harnais/sondes.py`
  (`f92657a6…`, `score_action` : maximum ou attention, refuse le reste) ; `t07/plancher_v1.py` ; `t07/registre_v1.py`
  (format du registre, sceaux, extraits de GO) ; `manifeste.py` (`graines` par `SeedSequence`, `generateur`, `versions`).
- **Absent avant ce travail** : tout `src/controle_ia/narcbench/` ; aucun chargeur NARCBench ; **`scikit-learn` absent de
  l'environnement et de `requirements-cpu.txt`**, alors que la recette de HELIOS l'exige (liblinear arrêté à 8 itérations,
  p. 29-30 ; l'arrêt avant convergence n'a pas d'équivalent exact hors liblinear).

### 1.3 Ce qui manque encore

1. **Chargeur des fichiers publiés** : à écrire **après** avoir vu leur format. Il faut le téléchargement : taille au § 4.1,
   à donner à la mère d'abord.
2. **`scikit-learn`** épinglé, ajouté aux dépendances. C'est un téléchargement de bibliothèque (≈ 10 à 15 Mo, SUPPOSÉ).
3. **Trois points que le PDF ne fixe pas**, à trancher sur le code publié **avant** le texte court, jamais après une lecture :
   (i) l'aire de CORE se calcule-t-elle sur les scores des 17 plis mis en commun, ou comme moyenne des aires par pli ?
   (`mode_core`) ; (ii) sur quel jeu se fait la standardisation ? ; (iii) quelles couches forment la bande ? Le PDF dit cinq
   (p. 27), la fiche en liste six, et le code publié n'est pas la v3 ni la v5 : `reproduce.py` prend C = 1, d'après le
   rapport de lecture de niveau 1. Question ouverte du brouillon 4 : les activations du 70B lisent-elles des textes du 70B ou
   ceux de Qwen3 ?
4. **Texte court neuf** du bras externe, à préenregistrer et à sceller (R1) ; contre-lecture du texte (R2) et du code.
5. Pour la voie du 8B, si elle revient : étape 0 (concordance du constructeur sur 100 + 40 épisodes publiés, L_CORE,
   L_STEGO, exemple littéral, empan STEGO concordé à `stego.py` l. 1014-1051), moteur de génération, passe forcée sur carte.

## 2. Ce rejeu peut-il porter « notre chaîne reproduit un résultat positif publié » ?

**Réponse courte : pas dans cette formulation.** Dans sa voie retenue (activations publiées), le bras peut porter
« notre code de lecture retrouve les nombres publiés de HELIOS à partir de leurs activations ». Il peut aussi porter
« nos familles de sondes séparent colludeurs et honnêtes sur ces activations, au-dessus d'un plancher apparié ». Il ne porte
pas « notre chaîne de sondes voit sur notre modèle ce que d'autres ont vu ».

- **Le résultat publié visé**, vérifié sur le PDF v5 (`02527fd4…`) :
  - p. 17 : « Every model reaches 1.00 AUROC on CORE, near-perfect detection on STEGO » ;
  - Table 2, p. 27 (Qwen3-32B) : CORE 1,00 pour les cinq méthodes ; STEGO, Peak Suspicion 1,00 et Deception Split 0,99 ;
  - Table 3, p. 28 (Llama-3.1-70B) : CORE, Peak Suspicion 1,00 et Deception Split 1,00 ; STEGO, 1,00 et 0,99 ;
  - toutes ces valeurs sont des moyennes sur la bande de couches et sur dix graines (p. 27, annexe D) ;
  - recette : dernier jeton, moyenne des tours 1 à 3 pour CORE, tour final pour STEGO (p. 27) ; régression logistique
    `C=25, max_iter=8, liblinear` (p. 29) ; validation de CORE en tenant un domaine à l'écart (p. 14-15).
- **Différences avec ce que porterait notre bras** :
  - mêmes modèles (Qwen3-32B et Llama-3.1-70B, quantifiés), mêmes activations, mêmes textes, même recette réimplémentée.
    C'est une **reproduction de calcul** de leur analyse, pas de leur extraction ;
  - nos familles sur leurs vecteurs ne voient **qu'un jeton par message**. Notre agrégation sur les jetons (maximum,
    attention), nos couches 7, 15 et 23 et le 8B n'y entrent pas. Or c'est ce qui distingue notre chaîne de HELIOS (lecture
    de niveau 2 de HELIOS, § 3 : « libre »). La sonde S-T de T0.7 ne s'y applique pas (largeurs différentes) ;
  - CORE à 1,00 est un résultat facile : collusion **instruite**, et le texte seul y suffit peut-être. Sur les activations
    publiées, les bases sans activations sont « sans objet » (grille D, ligne D3e : « rien n'est établi sur une lecture
    interne ») ;
  - **risque d'échec de la reproduction** : le code publié diffère du papier (C, couches, augmentation de données), donc
    l'écart de 0,03 peut ne pas tenir. Le résultat s'écrirait alors « non éprouvé ». C'est un résultat, à rapporter (R3, R4).
- **Ce que porterait la voie sur le 8B** (suspendue) : un **rejeu du protocole publié** sur un modèle plus petit que tout le
  papier, au plancher de 20 milliards (p. 27), et du mauvais côté de la pente publiée (Table 13, p. 46 : GPT-OSS-20B à 0,64
  sur TRANSFER, 0,71 sur STEGO). Ce sont des textes neufs et nos sondes. Ce serait une **extension**, pas une reproduction.
  Seule la prédiction N1 (aire ≥ 0,90 sur CORE) y ressemble, et elle n'est pas décisive.

**Phrase opposable si la garde tient** : « À partir des activations publiées par les auteurs de NARCBench, notre réimplémentation
de leur recette retrouve à 0,03 près leurs aires de détection de la collusion (CORE et STEGO ; Qwen3-32B, Llama-3.1-70B ;
HELIOS v5, Tables 2 et 3, p. 27-28) ; nos familles de sondes, appliquées aux mêmes vecteurs, [état de la grille D]. » Rien sur
notre modèle, rien sur l'agrégation sur les jetons.

## 3. Le code (module neuf `src/controle_ia/narcbench/`, R12 ; aucun module gelé touché)

| fichier | rôle | sha256 (16) |
|---|---|---|
| `__init__.py` | sommaire | `f9253ece…` (avant l'ajout de la ligne `externe_v1` : voir le commit) |
| `contextes_v1.py` | constructeur à deux champs (consigne = invite système ; case privée = section du message utilisateur) ; bourrage neutre de même longueur en jetons ; neutralisation à position égale (ajustement ±1, sinon `ExclusionPosition`) ; cellules `K-c+`, `K-h+`, `K-h0`, `K-c0`, `H-h−`, `H-c−`, `H-c+`, `H-c0`, contrôles `/rep`, `/dec`, `/ech`, et `H-h0` (M1 de la contre-lecture 3, construite, jamais jouée sans texte qui la nomme) ; appariement ; L | `69c20a95…` |
| `empans_v1.py` | empan CORE (jeton de fin exclu) ; empan STEGO selon la règle relue par la contre-lecture 3 (texte après la ligne « RANGE: » ou « DECODE: », sinon avant ; lignes « PRIVATE: » retirées), **à concorder à l'étape 0** | `ee3e26f9…` |
| `notation_v1.py` | notation à la volée, maximum ou attention par le harnais, **refus de toute autre agrégation** | `b50dae83…` |
| `comparateur_helios_v1.py` | recette de HELIOS (diagnostic, N-026) ; `scikit-learn` exigé, garde sinon ; ajusteur `jouet-numpy` pour les essais seulement, marqué « jouet, pas HELIOS » | `70908aa7…` |
| `statistiques_v1.py` | échelle gelée ; duel (δ, intervalle par blocs de scénarios) ; ν, τ ; règle I ; qualificatifs (κ = 0,25) ; bande du plancher ; grille D ; Peak Suspicion, Deception Split ; placebo ; rappel à α ; maximum cumulé | `fa9970d7…` |
| `gardes_v1.py` | identité au bit près dans le même lot ; identifiants du texte ; exclusions des positions (> 2 % : arrêt) ; retokenisation ; invariance des bases ; passe arrêtée = passe entière ; chronométrage et retraits ; budget de 16 h et 25 USD | `54afe9c8…` |
| `registre_narc_v1.py` | garde d'ouverture (clés `SCELLEMENT-NARC-8B`, `GO-NARC-8B`, …), sur le format de `t07/registre_v1.py` | `17d981d7…` |
| `externe_v1.py` | **bras externe** : vecteurs d'agent ; recette de HELIOS en tenant un domaine à l'écart ; dix graines ; garde de reproduction à 0,03 contre les Tables 2 et 3 ; nos familles sur leurs vecteurs avec plancher | `69dfdd24…` |
| `jouet_v1.py` | répétition jouet de bout en bout sur processeur : tokeniseur par mots, lecteur factice déterministe, 12 scénarios × 2 réplicats ; graines par `SeedSequence` (`manifeste.graines`), manifeste avec configuration et empreinte, versions, graines ; refus d'écraser (R12) | `96c24f0a…` |
| `tests/test_narcbench_v1.py` | 24 essais | `b1df2b71…` |
| `tests/test_narcbench_externe_v1.py` | 3 essais | `fabaf90a…` |

- **R5** : chaque garde est éprouvée sur un cas sain et sur un artefact. Quelques exemples :
  - activation décalée d'une unité au dernier rang (`nextafter`) → arrêt ;
  - 2 messages exclus sur 100 passent, 3 sur 100 arrêtent ;
  - 100 négatifs donnent un rappel à 1 % « non atteignable », 101 en donnent un ;
  - registre : six artefacts → refus (clé absente, clé en double, clé NARC inconnue, ligne non antérieure, sceau faux, extrait
    de GO hors de `go.md`) ;
  - tokeniseur non réversible → refus ;
  - gabarit qui fusionne des jetons à la frontière → `ExclusionPosition` ;
  - agrégation « moyenne » → refus.
- **Énumérations** :
  - règle I : les sept états sont atteints, et I3 à I6 se partagent les intervalles sans recouvrement ;
  - grille D : 128 combinaisons (D0 64, D1 32, D2 16, D6 8, D5 4, D3 1, D4 2, D3e 1), une ligne et une seule chacune.
- **Répétition jouet** (10:56 UTC, ≈ 5 s, dans le bloc-notes, rien dans `runs/`) : 14 cellules notées, aucune exclusion de
  position, ν ≈ 7·10⁻⁷ (bruit de lot factice), τ ≈ 0,10. Les duels prennent le sens planté (K1 baisse, H1 monte). Même
  entropie, mêmes résultats. **Aucun de ces nombres ne dit rien de NARCBench.**
- **Essais** : 22 sur 24 verts à 10:57:15 UTC, puis 23 sur 24 à 10:57:42, puis 24 sur 24 à 10:58:15 (deux essais corrigés,
  sans toucher au module) ; après la bascule, 25 sur 27 à 11:00:11, puis **27 sur 27 à 11:00:35 UTC** (données synthétiques
  du bras externe rendues moins ambiguës : le plancher apparié en covariance captait l'axe planté, ce qui est son rôle).
  Suite complète non lancée (interdits, règle 5).
- **Écarts au brouillon 4, à écrire dans le texte court ou dans le brouillon 5** :
  1. le comparateur s'appelle `comparateur_helios_v1.py` et non `comparateur_helios.py` (R12) ;
  2. le registre suit une règle propre à NARCBench : une clé étrangère sans la marque `NARC` est ignorée et comptée, une clé
     NARC inconnue est refusée. Le brouillon 4 ne la fixe pas, et `classer_cle_inconnue` de T0.7 n'y convient pas ;
  3. sous D-3 (a), aucune ligne `GO-NARC-8B` n'existera : le texte court doit fixer ses propres clés, et `EXIGEES["externe"]`
     doit suivre ;
  4. K1 et H1 sont aussi lus sur les tours 1 à 3 (m3 de la contre-lecture 3 ; fait dans le jouet).

## 4. Devis et calendrier

### 4.1 Voie retenue : bras externe, processeur, 0 USD

| poste | valeur | source |
|---|---|---|
| carte | **aucune** | D-3 (a) |
| téléchargement nécessaire | activations CORE et STEGO de Qwen3-32B et Llama-3.1-70B : **712 344 334 octets (≈ 0,71 Go)** ; épisodes et métadonnées pour les étiquettes, les domaines et les comptes retenus : un sous-ensemble du jeu, **pire cas le jeu entier, 1 456 027 013 octets (≈ 1,46 Go)** ; `scikit-learn` ≈ 10 à 15 Mo | devis v2 (fiche du 9 novembre) ; **à revérifier** sur la fiche avant tout téléchargement |
| disque | ≈ 7,4 Go libres (`df`, 10 novembre, 11:00 UTC) ; le pire cas tient, sans copie double | — |
| calcul processeur | régressions : 17 plis × 5 ou 6 couches × 10 graines ≈ 1 000 ajustements sur ≈ 150 vecteurs de largeur 5120 ou 8192, par modèle ; nos familles et 200 directions de plancher par couche lue ; **≈ 0,5 à 1 h** (SUPPOSÉ) | — |
| pire cas | 3 h de processeur, 1,5 Go de disque, 0 USD | — |
| licences | jeu MIT ; activations de modèles sous leurs licences (Llama 3.1 communautaire ; Qwen3 **non vérifiée**) ; lecture de recherche, sans redistribution ; **revérifiées et consignées au téléchargement**, avec l'empreinte sha256 de chaque fichier (compagnons, R6) | brouillon 4 |

### 4.2 Pour mémoire : voie sur carte (suspendue)

Devis v2 (`c9648726…`) inchangé dans sa structure. Si le brouillon 5 adopte `H-h0` (M1 de la contre-lecture 3), il faut
1 240 passes de plus (≈ 16 280 en tout, + 8 %, ≈ + 0,1 h). Attendu : une A100 SXM4 80 Go, 4,5 à 7 h, ≈ 6,5 à 9,7 USD. **Pire
cas : 23,8 USD** sous la borne dure de 16 h (inchangé), plafond de 25 USD. Téléchargements : poids du 8B, 16 060 556 376
octets, plus le jeu. Rien de cela n'est demandé aujourd'hui.

### 4.3 Ordre des étapes et dates (voie retenue)

| date (2026) | étape | qui |
|---|---|---|
| 10 nov. | module et essais (fait) ; ce rapport | développeur |
| 11 nov. | la mère reçoit les tailles du § 4.1 et décide ; téléchargement ; empreintes et licences consignées ; **lecture du format seulement** (aucune aire calculée) ; chargeur `chargeur_externe_v1.py` et ses essais ; `scikit-learn` épinglé ; trancher (i) à (iii) du § 1.3 sur le code publié | mère, développeur |
| 11-12 nov. | **contre-lecture du code** par un sous-agent neuf d'un autre modèle (Claude Fable 5.1, N-052) ; corrections | sous-agent neuf |
| 12 nov. | **texte court neuf** du bras externe (hypothèse, prédiction N7 chiffrée, tolérance 0,03, `mode_core`, couches, grille D et D3e, plancher, placebo, clés de registre, liste d'arrêt) ; contre-lecture (R2) | rédacteur, contre-lecteur |
| 13 nov. | corrections, **scellement**, entropie tirée, ligne `SCELLEMENT-…` au registre ; **aucune ligne d'autorisation de dépense** : 0 USD | mère |
| 14 nov. | course sur processeur (< 1 h) ; résultats scellés avant toute lecture humaine | mère |
| 15-17 nov. | lecture mécanique ; verdict descriptif par un sous-agent neuf (ni auteur du texte, ni auteur du code) ; scellé ; transmis à Lazar | sous-agent neuf |
| 18-26 nov. | marge : une reprise sur incident, ou la mise en forme pour l'entretien du 27 | — |

## 5. Embargo et dépendances

- **Aucun fichier sous embargo ouvert, lu, copié, cherché ni passé à un script.**
  - L'arbre de travail n'extrait pas `docs/notes/bras-attaque/`. Les recherches se sont faites par `git grep` avec exclusions
    (`docs/notes/bras-attaque`, `diag`, `runs`, le script d'extraction de T0.6), ou dans des fichiers nommés.
  - Dans `premier_test_ia/`, je n'ai ouvert que `figees.py` (en-tête), et j'ai vérifié que `statistiques.py` n'importe rien
    de P3-bis. `lecture_p3bis_v1.py` et `ouverture_p3bis_v1.py` n'ont pas été ouverts, et aucun module neuf ne les importe.
  - Le fichier de sondes de P3 (`701f73bd…`) a été haché par son seul chemin, jamais ouvert. Son dossier n'a pas été parcouru.
  - Aucune branche interdite n'a été touchée, et je n'ai fait aucun `fetch`.
- **Dépendances** : **aucune** envers la course 7a, la course 7b ni P3-bis. Le bras externe ne lit que des fichiers publics et
  le PDF. Seule la clé permise `SONDES-T07` (PD5) touche T0.7, et elle est facultative. Le registre des scellements est
  partagé avec T0.6, T0.7 et P3-bis : la garde n'y lit que les clés NARC et compte les autres sans ouvrir ce qu'elles citent.
- **Réserve personnelle** : j'ai lu un texte de T0.7 (le brouillon 4). Je suis donc exclu de tout rôle de lecteur de P3-bis.

## 6. Points ouverts pour la mère

1. Donner le feu vert au téléchargement, sur la taille du § 4.1 (0,71 Go à 1,46 Go, plus `scikit-learn`).
2. Écrire « reproduit » avec la phrase du § 2, pas avec celle de la priorité de Lazar.
3. La décision D-3 (a) est rapportée par la mère, sans fichier de décision lu par moi : à consigner (`docs/decisions/`) si
   ce n'est pas fait.
