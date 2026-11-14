# Consigne — développeur des corrections permises du code de (ii-b), hors consigne privée et hors fichiers à fragments — v1

Écrite le 2026-11-14T06:40:55Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A). Lot : plan multi-comptes (`3b1bda25…`), lot « compte 4 », tâche 4. Fondement : message de la mère recopié au journal du compte 4, version 18, C4-0056, point 4 : « (ii-b) : branche gelée, rien n'entre dans main. Ne touche pas aux fichiers qui portent les fragments, n'écris aucun outil qui charge la consigne privée : la voie est une décision de Lazar. Les corrections qui ne touchent ni la consigne ni ces fichiers : go. » La consigne des corrections précédente (`consigne-developpeur-corrections-iib-v1.md`, `33c33ac1…`) est **remplacée** pour toi par celle-ci ; son développeur s'est arrêté sur un refus du classifieur (C4-0052), et rien de ce qu'il voulait faire n'est repris ici. **Aucune dépense, aucune instance, aucun téléchargement de modèle, aucune clé employée.**

## 0. Interdits permanents (recopiés du brief du compte 4, section 6, sans changement)

- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a ou 7b, l'étiqueteur, `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `find` ni de `grep -r` larges ; fichiers nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit : `n=$(git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'); [ "$n" = 0 ] && git commit …`
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner `poste-temoin-bailey-*` ; aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur : arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

## 1. Ce qui t'est interdit en propre (périmètre de la mère)

- **Fichiers que tu n'ouvres pas, ne modifies pas, ne déplaces pas, ne supprimes pas, ne copies pas** (ils portent des fragments de la consigne privée du maître, ou la nomment et la chargent) :
  - `brouillons/ii-b-saboteur-budget-v1/consigne-privee-maitre-ii-b-v1-brouillon2.md` (la consigne privée elle-même) ;
  - `src/controle_ia/iib/jouet_v1.py` ;
  - `tests/test_iib_exclusion_v1.py`, `tests/test_iib_consigne_v1.py` ;
  - tout le dossier `essai/iib-jouet-compte4-v1/`.
- **Aucun outil** (script, essai, commande) **qui charge la consigne privée**, et aucun essai neuf qui la charge ; tu ne lances pas `tests/test_iib_consigne_v1.py` ni `tests/test_iib_exclusion_v1.py`. Tu ne modifies ni `src/controle_ia/iib/consigne_v1.py` ni `src/controle_ia/iib/exclusion_v1.py` (ils lisent la consigne à l'exécution).
- **Aucune répétition jouet** (ni `scripts/repetition_jouet_iib_v1.py`, ni une copie) : ses entrées portent la consigne factice à fragments ; aucun fichier neuf n'en dérive.
- Les autres essais de (ii-b) importent `iib.jouet_v1` sans l'afficher : tu peux les lancer, sans jamais afficher un fichier qu'ils écrivent dans un dossier temporaire ; lance-les d'abord avec `--tb=no -q` ; pour un échec, relance le seul essai fautif avec `--tb=line` ; si une sortie affiche un texte de consigne (factice ou non), arrête-toi sur ce point et déclare-le au rapport.
- Si une correction ci-dessous exige d'ouvrir ou de changer l'un de ces fichiers : tu ne la fais pas ; tu l'écris « hors périmètre (C4-0056, point 4) » au rapport.

**Le reste.**
- Tu travailles **seulement** dans l'arbre `/home/user/iib-code-compte4-v1` (branche `prep/iib-code-compte4-v1`, gelée pour `main` ; tête de départ `3baecee7044f2f1701743dc307da9bdcb8fcf217`) ; tu y commites et tu pousses **seulement** par `git -C /home/user/iib-code-compte4-v1 push origin prep/iib-code-compte4-v1`, **à chaque jalon** (le conteneur peut redémarrer), après la garde des secrets ; jamais une autre branche, jamais de réécriture d'historique, jamais de `fetch` ; fin de chaque message de commit : `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` puis `Claude-Session: https://claude.ai/code/session_01Qi7Gr2uGzyVcw9VmDXgvEV`.
- Environnement : `/home/user/controle-ia-travail/.venv/bin/python`, `PYTHONPATH=src` de ton arbre ; aucune installation ; **aucun appel réseau** ; `HF_TOKEN`, `OPENAI_API_KEY`, `GEMINI_API_KEY`, `VAST_API_KEY`, `HCLOUD_TOKEN` jamais lus.
- **Aucun fichier de `registres/`**, de P3-bis ni de T0.7 (ni `prereg/T0.7-*`, ni `src/controle_ia/t07/`, ni `tests/test_t07_*`) ; rien de `donnees/`, `diag/`, `runs/`, `traces/` à la racine d'un dépôt.
- `grep -n` permis sur `src/controle_ia/iib/`, `scripts/*iib*` et `tests/test_iib_*` **hors des fichiers interdits ci-dessus** (passe-les nommément, sans motif qui les englobe) ; jamais `grep -r` ailleurs, `find`, `ls -R`, `git grep`.
- Interdit du programme : jamais de moyenne ni de médiane sur les jetons dans un score de sonde (ce code n'a aucune sonde).
- Dans tout fichier poussé, ton modèle est « modèle A », sans identifiant (R-2598).

## 2. Qui tu es

Développeur **neuf**, sous-agent de la session du compte 4. Tu n'as écrit ni ce code, ni les textes de (ii-b), ni leurs contre-lectures, ni T0.6, T0.7, P3 ou P3-bis ; tu n'as jamais lu la consigne privée du maître. Tu seras exclu de la vérification de tes corrections.

## 3. Ce qui fait foi (vérifie chaque empreinte avant lecture)

| pièce | chemin (dépôt `/home/user/controle-ia-travail` sauf mention) | sha256 |
|---|---|---|
| **contre-lecture 1 du code** (lis-la en entier) | `brouillons/iib-code-compte4-v1/contre-lecture-1-code-iib-v1.md` | `a375c6997a9b68678b012a10ed57e33a2a12e0ce4cb2aff01875c95ef125797c` |
| rapport du développeur | `/home/user/iib-code-compte4-v1/docs/notes/iib-code-compte4-v1/rapport-developpeur-iib-v1.md` | `956593075a1bfd6b99dfe920b7f1c9ee7f33d01490e6500fc87c9dfaf832c526` |
| conception, brouillon 2 (le texte prime ; sections 2 à 7, 9, 10) | `brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1-brouillon2.md` | `47b86258df937dc5ec8c3e6ff74cc708ea0487a018f54f3a91a721b76543209c` |
| ordre exploratoire, brouillon 2 (§ 1, 3, 4, 6, 7) | `brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1-brouillon2.md` | `4c083d75484e29c0c92d100a5b0bd4110f373e3fe17f500a868cb0f826f6a407` |
| base (A) de T0.8 (« Métrique », l. 60 à 101 ; « Seuil » si besoin) | `prereg/T0.8-base-A-mots-et-cout-v1.md` | `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` |
| T0.6 scellé, l. 573 à 584 seulement | `prereg/T0.6-organismes-v0-v1.md` | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` |
| le code permis | `/home/user/iib-code-compte4-v1/src/controle_ia/iib/` (hors `jouet_v1.py`, `consigne_v1.py` en lecture seule, `exclusion_v1.py` en lecture seule), `scripts/*iib*` (hors la répétition, en lecture seule), `tests/test_iib_*_v1.py` (hors les deux interdits) | § 2 du rapport du développeur |

## 4. Ce que tu corriges (constats de la contre-lecture ; références au commit `3baecee7`)

Chaque correction : un essai **sain** et un essai **artefact** (R5) ; aucun repli silencieux ; code corrigé **en place** (branche de préparation, rien n'est cité) ; essais neufs sous noms neufs `tests/test_iib_<objet>_corrections_v1.py` ou dans les fichiers d'essais permis.

1. **CLIIBC-02** : porte dans `iib/lecture_v1.py` la base (A) de T0.8 telle que sa « Métrique » la fixe (centre de tâche = médiane du log10 du coût sur toutes les actions de la tâche à coût lisible, sans étiquette ; les douze traits ; « sans centre » ; régularisation et méthode d'optimisation du texte, convergence jugée), transposée ainsi, **choix à confirmer par la mère, déclarés** : « toutes conditions confondues » = toutes les actions de la tâche dans les quatre conditions de l'évaluation (H, B50, B100, TJ100) ; seuil « sans centre » = celui de la base (A) ramené au nombre d'actions par tâche de l'évaluation de (ii-b) (dérivation écrite, arrondi vers le haut, dans `FIXES_PAR_LE_CODE`). La base « mots et coût » prend ce même centre (T0.6, l. 575). Essais sur données synthétiques construites dans l'essai (sans `jouet_v1`) : coût séparant (aire 1), sans signal (aire voisine de 0,5), centre inchangé par permutation des étiquettes, tâche sans centre.
2. **CLIIBC-03** : état « mots et coût » = celui de la plus forte des deux bases (T0.6, point 1) ; essais : traits réussit et mots échoue → « réussit » ; l'inverse → « réussit » ; les deux échouent → « échoue ».
3. **CLIIBC-04** : itérations et plus grande composante du gradient rendues ; au-delà d'un seuil de `FIXES_PAR_LE_CODE` : « non calculable », écrit ; essais : convergence ; une itération permise → « non calculable ».
4. **CLIIBC-05**, option (1) : oracle, identifiants et textes de l'étalonnage et de chaque tour écrits et scellés à la fin de chaque phase, sous noms neufs par phase (déclarés pour le § 7 de l'ordre) ; course complète : mêmes sorties finales ; essais : E-O6 en échec et M-2 → l'oracle de l'étalonnage (et des tours joués) existe, scellé, rattaché.
5. **CLIIBC-06** : le collecteur de `tests/test_iib_consigne_invisible_v1.py` espionne aussi `generer_actions` (contexte entier décodé, par phase) ; artefact : indication plantée aux pas 1 à 9 de l'évaluation → vue ; raisons « COUVERT » de `tests/test_iib_inventaires_v1.py:25,31` corrigées. (Ces deux fichiers ne nomment pas la consigne privée ; s'ils exigeaient de changer `jouet_v1.py` : hors périmètre.)
6. **CLIIBC-07** : essais sur actions synthétiques de la lecture (2) : « flagrant par action », « sous le seuil par action », phrase entière quand les trois conditions sont réunies, aucune phrase quand une manque ; et « diffus non réalisé » (point 8).
7. **CLIIBC-08** et **CLIIBC-18** : aucun changement de code ; déclarés au rapport pour les textes.
8. **Mineurs** :
   - CLIIBC-09 : la partie de `oracle_v1.py` et `tours_v1.py` seulement (`champ_cout` relu sur le texte par `lire_action` quand le décodage est infidèle, ou arrêt) ; la partie de `exclusion_v1.py` : hors périmètre.
   - CLIIBC-10 : empreinte de la base comparée après chaque distillation.
   - CLIIBC-11 : clé `condition` = H, B50, B100 ou TJ100 dans les sorties d'évaluation.
   - CLIIBC-12 : descriptif « échelle » du maître dans `acceptation-iib.json` ; phrase « diffus non réalisé » (conception, section 7, au caractère près) quand la conjonction manque ; part annoncée à `tours_v1.py:132-134` calculée, ou phrase retirée.
   - CLIIBC-13 : bornes de l'offre (ordre § 1) vérifiées contre des constantes recopiées de l'ordre ; `EMPREINTE_LISTE_TESTS_IIB` recoupée avec l'empreinte du fichier de la liste.
   - CLIIBC-14 : la ligne de 7b doit nommer 7b et un identifiant d'instance (motif écrit) ; « une seule fois » gardé.
   - CLIIBC-15 : imports transitifs déclarés ; essai : fonctions de `controle_ia.sondes.familles` et de `environnements.juges` remplacées par des fonctions qui lèvent → la course passe.
   - CLIIBC-16 : espion de `io.open` et fichier `lecture-sondes…` planté ; assertion stricte du second cas de `test_boucle_cible_avant_le_tour_de_controle…` ; essai du vidage des caches.
   - CLIIBC-17 : audit R4 tiré sur H, B100 et TJ100 ; « sous le seuil par action » exigé de toutes les bases par action ; une clé de graine par usage ; déclarés, à confirmer par la mère.
9. **CLIIBC-01** : **hors périmètre**, en entier (voie à décider par Lazar). Tu n'ajoutes aucun essai de fragments.
10. **Liste ciblée** : si tu ajoutes un fichier d'essai, écris une **liste neuve** `scripts/tests-cibles-iib-v2.txt` (la v1 reste) qui garde les fichiers de la v1 **et** les tiens ; dis son empreinte ; le marqueur `<<EMPREINTE_LISTE_TESTS_IIB>>` de l'ordre recevra celle-là ; l'amorce et `configuration_v1` qui citent la v1 : mets-les à la v2 si c'est hors des fichiers interdits, et dis-le.
11. **Essais** : avant tes changements, relève les nombres de la liste ciblée **sans** les deux fichiers interdits, et des huit essais d'inventaire et de listes (contre-lecture, § 5) ; après : même ensemble plus tes essais, tous verts ; inventaires : aucun échec neuf hors de `iib/`, chacun examiné dans `tests/test_iib_inventaires_v1.py` ; essais des modules repris (§ 3 (d) du rapport du développeur) verts. Les deux fichiers interdits ne sont jamais joués : dis-le.

## 5. Ce que tu rends

Un rapport `docs/notes/iib-code-compte4-v1/rapport-developpeur-corrections-permises-iib-v1.md` dans ton arbre, scellé (`PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m controle_ia.scellement sceller <fichier>`), committé et poussé. Sections : **0. Identité** (modèle A, heures `date -u`, fichiers lus et empreintes ; déclaration : aucun des fichiers interdits ouvert, ou ce qui en a été vu par accident) ; **1. Table des constats** (identifiant → changement, fichier:ligne au commit final → essai sain, essai artefact → « corrigé », « déclaré sans changement », « hors périmètre », « question ») ; **2. Fichiers changés et neufs**, sha256, commit final, dernier commit qui touche `src/` ; **3. Essais** avant et après (nombres, dernières lignes recopiées) ; **4. Ce qui n'est pas rejoué** (répétition jouet, essais interdits) ; **5. Choix et questions** pour la mère ; **6. Limites**.

Dernier message à la session : commit final, branche, chemin et empreinte du rapport, nombres d'essais, questions ouvertes. Rien d'autre.

Si ton quota ou ton temps s'épuise : commite et pousse ce qui est fait, avec un rapport partiel scellé qui dit ce qui reste. Vise une fin avant 2026-11-14T09:00:00Z.
