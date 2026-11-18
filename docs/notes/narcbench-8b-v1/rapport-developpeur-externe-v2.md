# Rapport du développeur — bras externe NARCBench (nos sondes et la recette de HELIOS sur les activations publiées), v2

- **Rédacteur** : développeur neuf, Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère
  `session_013QMayjsoZJFBUCqcnvD5h1`. Travail du 2026-11-18, de 16:19 à 16:52 UTC (`date -u`). Mandat
  `docs/notes/narcbench-8b-v1/mandat-developpeur-externe-v2-v1.md` (empreinte vérifiée par son compagnon), sous GO-2026-11-18-30
  et R-3310 (voie processeur, 0 USD, décidée par Lazar le 10 novembre, D-3 (a), R-2175).
- **Arbre séparé** `/home/user/narcbench-externe-v2`, branche **locale** `prep/narcbench-externe-v2`, partie de `origin/main`
  (`77d55971`). **Rien poussé** ; rien écrit dans le dépôt principal ni sous `registres/`, `diag/`, `runs/`, `donnees/`.
- **Aucun score calculé ni lu sur les données réelles** : sur elles, seulement des tailles, des empreintes et un essai de forme
  (en-têtes, comptes). Tous les calculs de sondes, d'aires et de statistiques ont tourné sur des données factices.

## 1. Fait, étape par étape

1. **Report du code** — **reprise par fichier**, pas fusion (commit `f972cc47`) : les 21 fichiers de
   `origin/prep/narcbench-externe-v1` (tête `769ab122`, code `abbbcfde`, qui contient `origin/prep/narcbench-8b-code-v1`,
   tête `c43824d4` ; base commune `a325a6a4`), repris à l'octet. **Non repris** : la passation v1
   `registres/passations/2026-11-10-1116-narcbench-externe.md` et son compagnon (le mandat interdit de toucher `registres/`).
   `requirements-cpu.txt` de `main` est égal à celui de la base : la reprise vaut l'ajout de la branche. Empreintes v1 vérifiées :
   rapport `be31452f…`, manifeste `fc096b82…`, rapport du module `7ae2eaea…`.
2. **Licences revérifiées à la source** le 2026-11-18 à 16:21:14 UTC : `docs/notes/narcbench-8b-v1/releve-licences-externe-v2.md`
   (`ba78089612fd0173216ca7a789b98bf4279119ac3bb33e36f2663dc86bb588f7`). **Rien n'a changé** : jeu MIT, code MIT, Qwen3-32B
   Apache 2.0, Llama 3.1 sous licence communautaire (usage de recherche permis, sans redistribution) ; tous les textes ont la
   même empreinte qu'en v1. Écart E6 inchangé : le point de contrôle Llama nommé par la fiche répond 401.
3. **Données** retéléchargées à la révision `19cb14b269e052b19ba6d2bd2f4519afd3b10c57`, hors du dépôt, dans
   `/home/user/narcbench-donnees-v2/` (16:22:56 à 16:23:11 UTC, une commande `curl`, **sans jeton**) : 8 fichiers,
   **712 344 334 octets**. Empreintes par **commandes simples**, sans boucle ni sous-shell (`sha256sum` des 8 fichiers,
   `git hash-object` des 4 `.json`) : **toutes égales à la publication**. Aucune demande d'approbation, aucun refus.
   Manifeste v2, écrit par programme : `docs/notes/narcbench-8b-v1/manifeste-donnees-externe-v2.json`
   (`4310683479acd4c1738199ead17941bb8925724ff89b478a22d8f8baf1f26445`) : mêmes chemins, tailles et empreintes publiées que la
   v1 ; les empreintes sur disque, `null` en v1 (refus de R-2184), sont calculées et égales.
4. **`verifier_fichiers`** passé deux fois sans arrêt (16:23:30 et 16:43:40 UTC). **Essai de forme sans aucun score** : module
   neuf `forme_externe_v2.py` (en-têtes des tableaux lus sans charger leurs valeurs ; aucun champ de résultat du jeu lu, prouvé
   par un essai espion) ; sortie sur les données réelles `docs/notes/narcbench-8b-v1/forme-donnees-externe-v2.json`
   (`61cc13130b51edbcaa88d49ce5b1ac6afa8fa9b2f22595e7debdd321f381d11d`). Constats de structure, identiques pour les deux
   modèles sauf les domaines :
   - lignes des tableaux = lignes des métadonnées (CORE 1 054, STEGO 1 320) : la troncature silencieuse `[:n]` des auteurs est
     sans effet ; clés = les couches de la bande seulement (Qwen3-32B 26 à 30, largeur 5 120 ; Llama-3.1-70B 32 à 37, 8 192),
     `float32` ;
   - CORE : 31 épisodes de collusion et 31 témoins ; **chaque agent a exactement les tours de discussion publics 1, 2, 3** : E3
     est sans effet sur ces données ; tour final 4 ; tour privé 0 (62 lignes) ;
   - apprentissage par message (E1) : **186 messages de colludeurs et 186 d'honnêtes** par modèle, classes égales (aussi dans
     chaque pli) ;
   - STEGO : 20 et 20 ; une ligne `final` (main 8) par agent ; domaine vide ;
   - domaines de CORE : **14 pour Qwen3-32B, 15 pour Llama-3.1-70B, ensembles différents** (« edu » d'un côté, « env » de
     l'autre ; effectifs différents) : ce ne sont **pas les mêmes épisodes** ; l'auteur des textes du 70B reste non établi. Le
     docstring v1 parlait de « 17 plis » : ce sera 14 et 15 ;
   - chargeur v1 : aucun épisode exclu.
5. **`externe_v2.py`** (commit `bbb3e938`), E1 à E4 réglés **ligne à ligne sur le code des auteurs** (`probes/reproduce_LR.py`
   au commit `85fea3be2a9d`, `1d66fdc7…`, relu à la source, jamais exécuté) :
   - **E1** apprentissage par message, ordre du fichier, colludeurs tronqués aux `nc` premiers, honnêtes tirés par
     `RandomState(graine)`, `StandardScaler` sur le jeu équilibré ;
   - **E2** augmentation **sans défaut** : l'appelant passe « papier » (aucune) ou « code » (4 copies, 0,05) ; tout autre
     valeur ou l'absence arrête ;
   - **E3** moyenne de toutes les lignes de discussion de l'agent (diagnostic, N-026 ; moyenne sur des messages) ;
   - **E4** graines 0 à 9 des auteurs, constantes de la recette ; nos tirages à nous par `SeedSequence` (R9).
   Points (i) à (iii) du rapport v1 tenus (moyenne des aires par pli, standardisation par message, bandes). **Plus strict que
   les auteurs, déclaré** : ligne finale en double → arrêt ; épisodes ≠ 4 agents comptés ; aucune valeur → arrêt (les auteurs
   écrivent 0,5). **Non calculé** : les trois autres méthodes de la Table 1, la sonde nulle, rien de TRANSFER. Nos familles :
   apprises par message (sans moyenne), lues sur STEGO par agent (message final), plancher apparié (recette gelée), intervalle
   par blocs d'épisodes, placebo des rôles permutés, ligne de la grille D (D3e, D5, D2 ou D6) ; maximum par le harnais, jamais
   la moyenne ni la médiane sur les jetons.
6. **Commande de la future lecture** `lecture_externe_v2.py` (commit `f82dd016`) : garde du registre (clé proposée
   `SCELLEMENT-NARC-EXT`, strictement antérieure, citant le texte scellé, entropie présente dans le texte ; refus = code 2,
   rien d'écrit) ; aucune ligne de GO exigée (0 USD : règle l'écart 3 du rapport v1) ; données vérifiées ; manifeste de run
   (R9) ; reproduction et garde à 0,03 ; nos familles ; résultat scellé et rattaché au manifeste. **Jamais jouée sur les
   données réelles.**

## 2. Essais

**78 essais verts** (16:47:34 UTC), tous sur processeur et données factices : 40 repris (24 + 3 du module v1, 13 du chargeur) et
**38 neufs** : 8 de forme, 19 de `externe_v2`, 11 de la commande de lecture. Chaque garde éprouvée sur un cas sain et sur un
artefact (R5). Pièces maîtresses :
- **oracle de transcription** : les fonctions des auteurs (licence MIT, citée) recopiées à la lettre dans l'essai, et notre
  réimplémentation **égales au bit près** (aires par graine et couche, moyennes finales, direction et `scaler`), avec et sans
  augmentation, classes égales et inégales (troncature des colludeurs, vrai sous-échantillon d'honnêtes) ;
- **épreuve des essais par mutation** (R4, essais « trop beaux ») : 4 mutations, 3 tuées ; la survivante (`random_state` de
  liblinear fixé à 0) s'explique : **le solveur primal L2 de liblinear n'use pas de la graine** ; un essai le consigne
  désormais comme fait ;
- commande de lecture **de bout en bout** dans un dépôt git jetable (manifeste et résultat scellés, rattachement vérifié par
  `verifier_resultat`), six refus du registre sans rien écrire, données fausses arrêtées avant toute écriture, aucune
  réécriture (R12).
**Suite complète du dépôt non lancée** (cloisonnement : elle lit sous `diag/`, `runs/`, `donnees/` ; et place sur le disque).

## 3. Écarts et constats déclarés, à trancher par le texte court

1. **E2** : « papier » (sans augmentation ; recommandation du rapport v1, Tables 2 et 3) ou « code » ; l'autre peut être
   rapporté en variante, sans test.
2. **E4 et R9** : les graines 0 à 9 sont des constantes de la recette publiée, pas nos tirages. **Constat sur données
   factices** : à classes égales (le cas des données publiées), la graine ne fait que permuter les honnêtes : écart entre
   graines ≈ 10⁻¹⁶ ; les dix graines des auteurs y valent presque une seule. Si R9 se lit à la lettre pour ces constantes : nœud.
3. **E3** sans effet sur ces données (trois tours partout) ; la règle des auteurs est gardée.
4. **scikit-learn** : `penalty` est déprécié depuis 1.8 et **retiré en 1.10** ; l'épinglage 1.9.1 est donc porteur ; l'avertissement
   est consigné, pas masqué. Les auteurs ne figent pas leur version (E7).
5. **`cloudpickle==3.1.3`** ajouté à `requirements-cpu.txt` : joblib 1.6.0 l'exige, la liste du 10 novembre l'omettait.
6. **Environnement** : l'environnement partagé `.venv` n'a **pas** scikit-learn ; je ne l'ai pas modifié : les cinq paquets
   épinglés sont dans `/home/user/narcbench-paquets-v2` (installés sans dépendances), `PYTHONPATH=src:/home/user/narcbench-paquets-v2`.
7. **Clé du registre** `SCELLEMENT-NARC-EXT` proposée ; si le texte en choisit une autre, changer `CLE_SCELLEMENT_EXTERNE`
   avant la contre-lecture du code.
8. **Couches de nos familles** : à fixer par le texte (`bande`, soit 11 lectures par famille, ou une couche par modèle).
9. **Plancher à rang déficient** : 372 vecteurs pour 8 192 dimensions ; la factorisation du paquet gelé (Σ + 10⁻⁹·I) a tenu sur
   données factices de mêmes dimensions (7,4 s) ; sur les données réelles, un échec lèverait une erreur d'algèbre linéaire
   (arrêt visible, jamais silencieux). Mahalanobis sans plancher (D6), comme en v1.
10. `__init__.py` du module (fichier v1) non retouché : son sommaire ne cite pas les modules v2.

## 4. Ce qui manque

**Pour la contre-lecture du code par un autre modèle (N-052)** : la confier à un sous-agent neuf d'une autre famille de modèle
(Claude Fable 5.1), avec la tête de la branche, les quatre modules v2 et leurs essais, et le script des auteurs
(`raw.githubusercontent.com/aaronrose227/narcbench/85fea3be2a9d/probes/reproduce_LR.py`, `1d66fdc7…`) pour vérifier la
transcription de l'oracle ; points à viser : fidélité de l'oracle, E2 sans défaut, E4 et R9, garde du registre, absence de
repli, valeurs NaN des sorties JSON, plancher à rang déficient.

**Pour le lancement après scellement** : (1) le texte court neuf (rédacteur distinct), contre-lu (R2), qui fixe E2, les
couches de nos familles, la clé, l'entropie, l'identifiant du run, la prédiction N7 (tolérance 0,03) et les écarts ci-dessus ;
(2) la contre-lecture du code et ses corrections ; (3) la fusion de la branche dans `main` par la mère (commit cité par le
texte), les paquets épinglés dans l'environnement (ou le dossier séparé), les données gardées ; (4) la ligne du registre
inscrite par la mère ; (5) après la lecture : la ligne `EXTERNE-NARC`, puis le verdict descriptif par un lecteur neuf. Durée
estimée de la lecture : **≈ 10 à 20 minutes de processeur** (SUPPOSÉ, d'après les mesures sur données factices), 0 USD.

**Commande exacte de la future lecture** (racine du dépôt après fusion ; les `<…>` sont fixés par le texte scellé) :

    cd /home/user/controle-ia-travail && PYTHONPATH=src:/home/user/narcbench-paquets-v2 .venv/bin/python -m \
      controle_ia.narcbench.lecture_externe_v2 --depot . --registre registres/scellements-v1.md \
      --texte prereg/<texte court scellé>.md --donnees /home/user/narcbench-donnees-v2 \
      --run-id <AAAAMMJJ-HHMMSS>-narc-externe-v2 --entropie <entier du texte> --augmentation <papier|code> \
      --couches-familles <bande | qwen3_32b=<couche>;llama_3_1_70b=<couche>>

## 5. Incident et lectures hors du mandat

- **Disque plein vers 16:39 UTC**, rempli par les dossiers temporaires d'essais d'autres sessions (`/tmp/pytest-of-root`) et le
  cache de pip partagé : je n'ai supprimé que **mes deux** dossiers temporaires (≈ 3 Mo, noms de mes essais), alerté la mère,
  qui a libéré la place ; ensuite, chaque passe d'essais a eu son dossier temporaire dans mon arbre, supprimé après.
- **Lectures hors de la liste du mandat** : le script `probes/reproduce_LR.py` et `config.py` des auteurs (publics, MIT ; lus
  pour E1 à E4, jamais exécutés) ; les docstrings de scikit-learn sur `random_state` ; les modules du dépôt que le code importe.
  **Incidentes** : pendant le diagnostic du disque, les **noms** des sous-dossiers temporaires d'essais d'autres sessions (des
  noms d'essais citant 7a et T0.7), aucun contenu ouvert ; ma recherche des lignes R-2175 et R-2184 a aussi affiché les
  lignes qui les citent (R-2176, R-2186, R-2193, R-2198, R-2216, R-2243, R-2256, R-2555) : aucun résultat, issue ni score de
  7a, 7b, T0.6, T0.7, étape B, étape B bis ou P3-bis n'y figurait. R-2735 non lu.
