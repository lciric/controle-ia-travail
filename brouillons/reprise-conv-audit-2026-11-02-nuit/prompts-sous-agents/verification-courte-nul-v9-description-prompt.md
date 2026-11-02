Tu es un lecteur neuf. Tu n'as écrit ni le juge statistique « nul v9 », ni ses essais, ni son banc, ni son préenregistrement, ni ses brouillons, ni la contre-lecture qui les a précédés. Travaille en français, sans sigle non développé. Toute heure que tu écris vient de `date -u`.

## Contexte (court)
Dépôt public `/home/claude/ideation-organism/` (dossier de travail `orchestrator/`). Le « nul v9 » est une version corrigée du juge statistique (`pole/nul_v9.py`, introduite au commit `5e352ec`). Sa validation décisive hors ligne (banc `demonstrations/banc_tricheurs_v9.py`, 31 lignes de 1 000 répétitions, aucun modèle, aucune dépense) a été **préenregistrée, scellée et lancée** le 2 novembre 2026 à 23:20:38 UTC sur le texte `prereg/preenregistrement-validation-nul-v9-v1.md` (sha256 `54c5713d07f61b7f2bb3dd8218f4bca881a044a2b11508015db5e727d62c18fb`, commit `66dbcf1`). Ce texte est le brouillon 4 (`prereg/preenregistrement-validation-nul-v9-brouillon4.md`, sha256 `02dfbb7b…0dc0908`) à l'octet, plus un paragraphe de scellement en tête.

Le brouillon 4 a été écrit par un sous-agent après la contre-lecture neuve n° 1 (`prereg/contre-lecture-preenregistrement-validation-nul-v9-v1.md`, sha256 `41f4f56d…`, faite sur le brouillon 2). Il a modifié trois fichiers existants : `pole/nul_v9.py` (il dit : description seulement, aucun calcul), `essais/test_nul_v9.py` et `essais/mutations_nul_v9.py` (essais et mutations pour le bloquant B1 et les importants I5, I6, I2). **Ce changement n'a jamais été relu par un lecteur neuf** : c'est ta tâche. La course décisive est partie avant ta relecture, à la demande du directeur humain ; l'écart est déclaré dans le paragraphe de scellement. Personne ne lira la sortie de la course avant ton rapport. Ton rapport sera joint au verdict, quel qu'il soit.

## Fichiers à lire
- `orchestrator/pole/nul_v9.py` (arbre, sha256 `7ae450df…`) et son état d'avant : `git -C /home/claude/ideation-organism show 5e352ec:orchestrator/pole/nul_v9.py` (sha256 `8cb44adf…`) ;
- `orchestrator/essais/test_nul_v9.py` et `orchestrator/essais/mutations_nul_v9.py`, dans l'arbre et à `e58cfec` (`git show e58cfec:orchestrator/essais/…`) ;
- `orchestrator/demonstrations/banc_tricheurs_v9.py` (le banc ; voir `FICHIERS_GELES`, `lire_preenregistrement`, la construction du manifeste) ;
- `orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md` (texte scellé) et `orchestrator/prereg/preenregistrement-validation-nul-v9-brouillon4.md` ; au besoin le brouillon 3 ;
- `orchestrator/prereg/contre-lecture-preenregistrement-validation-nul-v9-v1.md` et `orchestrator/prereg/couples-contre-lecture-validation-nul-v9-v1.json` ;
- le rapport du sous-agent qui a écrit le brouillon 4 : `/home/claude/controle-ia-travail/brouillons/passation-conv-audit-2026-11-02-soir/rapports-sous-agents/nul-v9-brouillon4-attaque-v4-b2-rapport.md` (lecture seule ; texte de modèle, non opposable).

## Questions (réponds à chacune, preuve à l'appui : ligne de code, commande, sortie)
1. **Le changement de `pole/nul_v9.py` entre `5e352ec` et l'arbre est-il bien limité à la description ?** Compare les arbres syntaxiques. Vérifie qu'aucun des noms changés ou ajoutés (`NON_COUVERT_V9`, `PHRASES_MEMBRES_V9`, `HORS_DU_NUL_PAR_CHOIX_V9`, `HORS_DU_NUL_PAR_NATURE_V9`, `RESERVES_V9`, `description()`, `description_publique()`, docstring) n'entre dans un calcul de la course décisive (le banc v9 et tout ce qu'il importe), y compris de façon indirecte (par exemple une empreinte de la description qui servirait de graine). Le manifeste de la course contient `nul_v9.description()` : dis si cela change quoi que ce soit au calcul.
2. **Les essais de B1 font-ils ce que disent le texte (sections 0 ter, 9 et 14, annexe B) et le rapport ?** Mode décisif : un cas sain (texte d'essai scellé au nom décisif, 14 empreintes, sans option : la course démarre une fois, 31 lignes, 1 000 répétitions, 172 800 s transmises, entropie égale à l'empreinte du texte, manifeste « decisif ») et des artefacts (`--lignes`, `--repetitions 999`, `--duree-max-s 28800` : code 2, texte non lu, rien d'écrit). Monotonie par la seule richesse (G5). Les mutations G1 à G5 sont-elles réellement tuées par ces essais, pour la raison dite ?
3. **I5 (ordre des issues), I6 (valeur certifiée sous optimisation tronquée) et I2 (description publique)** : les essais testent-ils ce que le texte promet, ou quelque chose de plus faible ?
4. **Texte scellé** : diffère-t-il du brouillon 4 par le seul paragraphe de scellement ? Ce paragraphe est-il exact (vérifie chacune de ses affirmations : arbres syntaxiques, 14 empreintes égales à l'arbre, 37 essais et 35 sous-essais, 43 mutations sur 43, aucun dossier de sortie antérieur visible dans l'historique public) ?
5. **Quoi que ce soit qui invalide la course en cours ou qui doive être déclaré au verdict** (écart au plan, essai qui ne teste rien, garde sans essai sur un artefact, phrase du texte devenue fausse).

## Ce que tu peux exécuter
- `cd /home/claude/ideation-organism/orchestrator && TMPDIR=/tmp POLE_ESSAI_BAC_REEL_NON_JOUE=1 nice -n 10 python3 -I -B -m pytest -q -p no:cacheprovider essais/test_nul_v9.py` (une fois ; ≈ 35 s) ;
- le banc de mutations `nice -n 10 python3 -I -B essais/mutations_nul_v9.py` **une seule fois** (≈ 2 min ; la machine n'a que deux cœurs et la course décisive tourne : reste sobre) ;
- tes propres scripts de lecture (arbres syntaxiques, diff), écrits dans `/home/claude/scratch/verif-nul-v9/lecteur/` et lancés avec `python3 -I -B` ;
- le banc v9 en **mode exploratoire seulement**, à petite taille (par exemple `--lignes T01 --repetitions 5`), avec un dossier de sortie neuf sous `/home/claude/scratch/verif-nul-v9/lecteur/`.

## Interdits (sans exception)
- Ne lis pas, ne liste pas, n'ouvre pas `/home/claude/ideation-organism/resultats/banc-tricheurs-v9-validation-v1/` (sortie de la course décisive) ni `/home/claude/scratch/verif-nul-v9/course-v1.journal` (son journal), et ne lance jamais le banc en mode décisif (`--preenregistrement`).
- Aucun commit, aucun fichier `.sha256`, aucun fichier existant modifié, rien sous un dossier `donnees/`, aucun `git fetch`, `git checkout`, `git stash` ni rien qui change l'arbre ou l'index des dépôts, aucun appel de réseau ni de modèle, `nice -n 10` pour tout calcul.

## Rendu
Écris ton rapport dans `/home/claude/scratch/verif-nul-v9/lecteur/verification-courte-nul-v9-description-v1.md` :
- verdict en trois lignes : « conforme », « conforme avec réserves » ou « non conforme », et ce qu'il faut déclarer au verdict de la course ;
- une section par question, preuves à l'appui ;
- la liste de tes scripts et sorties, avec leurs sha256.
Ta réponse finale : le verdict, les réserves une ligne chacune, le chemin et le sha256 du rapport.
