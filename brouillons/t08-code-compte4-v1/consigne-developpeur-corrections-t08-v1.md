# Consigne — développeur des corrections du code de T0.8 (après la contre-lecture 1), sur données factices — v1

Écrite le 2026-11-14T00:49:07Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A). Lot : plan multi-comptes (`3b1bda25…`), lot « compte 4 », tâche 3 (journal du compte 4, C4-0029 à C4-0031). **Aucune dépense, aucune instance, aucun téléchargement de modèle, aucune clé employée.**

## 0. Interdits permanents (recopiés du brief du compte 4, section 6, sans changement)

- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a ou 7b, l'étiqueteur, `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `find` ni de `grep -r` larges ; fichiers nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit (sans objet ici : tu ne commites rien).
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner `poste-temoin-bailey-*` ; aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur : arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

**Ajoutés pour cette tâche** (repris des consignes de lecture du compte 4 ; les exceptions plus bas les remplacent là où elles le disent).
- Lecture seule, sauf les deux fichiers du § 5. Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`), aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** (la mère n'en a nommé aucun pour ce lot) ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **rien de `donnees/`, `diag/`, `runs/`**.
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; jamais `grep -r`, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course (tu lis des textes et du code, rien d'autre).

- **Exceptions de cette consigne** (elles remplacent, pour toi, les ajouts ci-dessus qui interdisent l'écriture git et la lecture de `donnees/`) :
  - tu travailles **seulement** dans l'arbre `/home/user/t08-code-compte4-v1` (branche `prep/t08-code-compte4-v1`, tirée de `main` à `ee7f2f9c`, tête contre-lue `27c092642247e01f57ea3f80ec9ccd29f5798557`) ; tu y commites et tu pousses **seulement** par `git -C /home/user/t08-code-compte4-v1 push origin prep/t08-code-compte4-v1`, à chaque jalon, après la garde des secrets à 0 sur `git diff --cached` (motif du brief) ; jamais une autre branche, jamais de réécriture d'historique, jamais de `fetch` ; fin de chaque message de commit : `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` puis `Claude-Session: https://claude.ai/code/session_01Qi7Gr2uGzyVcw9VmDXgvEV` ;
  - tu peux lire le fichier des tâches d'évaluation `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (`76cdeace…`) pour sa **forme** seulement ; tout le reste de `donnees/`, `diag/`, `runs/` t'est interdit ; tes essais n'emploient que des **données factices** que ton code fabrique ;
  - environnement : `/home/user/controle-ia-travail/.venv/bin/python` (installé par la session, `requirements-cpu.txt`), avec `PYTHONPATH=src` de ton arbre ; aucune autre installation sans le dire dans ton rapport ;
  - **aucun appel réseau** de ton code ni de tes essais (ni Hugging Face, ni interface de modèle) ; \`HF_TOKEN\`, \`OPENAI_API_KEY\`, \`GEMINI_API_KEY\`, \`VAST_API_KEY\`, \`HCLOUD_TOKEN\` ne sont jamais lus ;
  - aucun fichier de \`registres/\` (tu ne lis ni n'écris le registre ; les lignes de registre que ton code exige sont lues dans un registre **factice** pendant tes essais) ; aucun fichier de P3-bis ; **aucun fichier de T0.7** (ni `prereg/T0.7-*`, ni `src/controle_ia/t07/`) : tu n'en as pas besoin.
- **Interdit du programme** : jamais de moyenne ni de médiane sur les jetons dans un score de sonde (ce code n'a pas de sonde ; si une moyenne sur les jetons apparaît, elle ne doit jamais être appelée « score de sonde »).
- **Modèles** : écris ton modèle comme « modèle A » (R-2598), sans identifiant, dans tout fichier poussé.


## 1. Qui tu es

Développeur **neuf** des corrections du code de T0.8, sous-agent de la session du compte 4, modèle A. Tu n'as écrit ni ce code (premier développeur), ni sa contre-lecture, ni T0.8 (brouillons, base (A)), ni T0.6, ni T0.7, ni P3-bis, ni aucune de leurs contre-lectures. Tu seras exclu ensuite de la vérification de tes corrections et du verdict de T0.8.

## 2. Ce qui fait foi (vérifie chaque empreinte avant lecture)

| rôle | chemin | sha256 |
|---|---|---|
| **constats à corriger** (lis-le en entier) | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/contre-lecture-1-code-t08-v1.md` | `7c47e18266a970abafb33335c5a0f7f9e768820a833e017aebc5bcec4b76d280` (compagnon) |
| script du lecteur (parties A à G : il montre les arrêts de CLT8C-01, -02, le calcul de CLT8C-03, -07, -09) | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/contre-lecture-1-code-t08-v1-calcul.py` | `cacc9e1ee90eb9ac1f45e0dbe7aa018ab40122651b350b0f32b0c7006da04b2f` (compagnon) |
| choix de la session sur les options du lecteur | `/home/user/controle-ia-travail/registres-provisoires/compte-4-2026-11-14-v3.md`, section C4-0030 | compagnon |
| **texte qui fait foi** : brouillon 4 gelé de T0.8 ; **le texte prime** sur le rapport du lecteur et sur ces choix : si tu trouves une contradiction, écris-la en question, ne la tranche pas | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` | `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` (compagnon) |
| base (A) scellée | `/home/user/controle-ia-travail/prereg/T0.8-base-A-mots-et-cout-v1.md` | `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` (compagnon) |
| configuration de 7b (pour CLT8C-06) | `/home/user/controle-ia-travail/prereg/T0.6-organismes-config-7b-v1.json` | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` |
| consigne et rapport du premier développeur | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/consigne-developpeur-t08-v1.md` ; `/home/user/t08-code-compte4-v1/docs/notes/t08-code-compte4-v1/rapport-developpeur-t08-v1.md` | `94b0e43af5d5cfc095679ef97bc26a7769ee12d7cf00970150be40736fc533b2` ; `5b1e873198f38c6b1725355c18212f9b889597071f7820d82f9f12b058c1a5cc` (compagnons) |
| code et essais de T0.8 | `/home/user/t08-code-compte4-v1/src/controle_ia/t08/`, `/home/user/t08-code-compte4-v1/tests/test_t08_*_v1.py` | au commit `27c09264` (empreintes au § 2 du rapport du premier développeur) |

T0.6 scellé (`prereg/T0.6-organismes-v0-v1.md`, `ef31feff…`), la configuration du pilote et le code importé : par sections, au besoin, en le disant.

## 3. Ce que tu corriges

Les **vingt et un constats** CLT8C-01 à CLT8C-21, chacun avec l'essai sain et l'artefact que le lecteur nomme (R5), **selon les choix de la section C4-0030** du journal :
- CLT8C-03 option (c) ; CLT8C-04 option (c) ; CLT8C-08 option (a) ; CLT8C-10 options (a) et (b) ;
- CLT8C-16 : seulement la projection des lignes de `textes-actions-hd.jsonl` sur `cle` et `texte` ; l'antériorité sur la date du manifeste de la pièce et la garde par identifiants d'épisodes **restent**, déclarées dans ton rapport ;
- CLT8C-17 : l'arrêt sur une clé `T08` en double **reste** ; une quatrième cellule qui n'est pas une empreinte entière est comptée et signalée (jamais ignorée en silence) ;
- CLT8C-18 : génération du juge arrêtée à la première apparition de la balise (critère d'arrêt sur les identifiants générés), point de lecture inchangé ; éprouvé sur le modèle jouet (même valeur lue qu'avant, moins de jetons générés) ;
- CLT8C-21 : dans ton rapport, les nombres justes (70, 58, 56) ; l'en-tête de `essai_jouet_v1.py` dit que l'essai se joue dans un dépôt git ;
- tous les autres, tels que le lecteur les propose.

**Règles de l'écriture** :
- Le code de T0.8 n'est cité par aucune ligne de registre : tu corriges **en place** les modules `src/controle_ia/t08/*_v1.py` et les essais `tests/test_t08_*_v1.py` ; l'historique git garde l'état contre-lu (`27c09264`). Tu peux ajouter des essais neufs sous `tests/test_t08_*_v1.py`. Aucun fichier hors de `src/controle_ia/t08/`, `tests/test_t08_*`, `docs/notes/t08-code-compte4-v1/` et `essai/t08-jouet-compte4-v2/` n'est écrit ; aucun essai d'autrui n'est modifié (R12).
- Aucun écart au texte n'est permis ; un point ambigu s'écrit en question, avec le choix le plus prudent retenu et déclaré.
- Aucune garde n'est affaiblie pour faire passer un essai ; aucun repli silencieux (R5).

## 4. Essais

- Depuis l'arbre, `PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -p no:cacheprovider` sur : tous les `tests/test_t08_*_v1.py` (tous verts) ; les cinq essais d'inventaire `tests/test_cibles_invisibles_v1.py`, `tests/test_cibles_invisibles_v2.py`, `tests/test_t06_v11_liste.py`, `tests/test_t06_v12_liste.py`, `tests/test_t06_v13_liste.py` (échecs connus : leurs éléments nommés comparés à ceux du § 5.2 du rapport du lecteur ; aucun élément neuf autre que des fichiers ou fonctions de T0.8 que tu ajoutes, à déclarer) ; vérifie par `grep -n` sur les fichiers `.py` de `src/controle_ia/` (hors `t08/`) qu'aucun module n'importe `controle_ia.t08`. La suite entière n'est pas exigée : dis-le.
- **Essai de bout en bout, deux fois**, dans des racines neuves **dans l'arbre** (l'essai exige un dépôt git) : `essai/t08-jouet-compte4-v2/a` puis `…/b` avec `--comparer`, même entropie et même horodatage relevés par la machine dans la commande ; rien n'est écrit sous `essai/t08-jouet-compte4-v1/`. Consigne les nombres (identiques à l'octet, égaux sur le contenu, exclus, différents) ; les tables D et F et la lecture HD factice y figurent. Ajoute un essai de bout en bout court, ou un essai de `executer_lecture`, où le registre du texte de validité est **absent du disque** (CLT8C-01) : `lecture-t08.json` écrit, tables D et F égales au cas sain.

## 5. Ce que tu rends

Commits sur `prep/t08-code-compte4-v1` à chaque jalon, poussés par `git -C /home/user/t08-code-compte4-v1 push origin prep/t08-code-compte4-v1` après la garde des secrets à 0. Un rapport `docs/notes/t08-code-compte4-v1/rapport-developpeur-corrections-t08-v1.md` dans l'arbre, scellé, committé et poussé. Sections : **0. Identité** (modèle A, heures `date -u`, fichiers lus et empreintes) ; **1. Constats traités** : une ligne par constat CLT8C-01 à CLT8C-21 : ce qui change (fichier:ligne au commit final), essai sain et artefact (`fichier::fonction`), ou « gardé » avec la raison ; **2. Fichiers changés ou neufs** et leur sha256 ; **3. Essais** (nombres, avant et après, pour les fichiers du § 4) ; **4. Essai de bout en bout** (racines, manifestes, empreintes, déterminisme) ; **5. Questions** (choix le plus prudent retenu, déclaré) ; **6. Limites**. Puis, en dernier message à la session : commit final, chemin et empreinte du rapport, nombres d'essais, questions ouvertes. Rien d'autre.

Si ton quota ou ton temps s'épuise avant la fin : commite et pousse ce qui est fait, avec un rapport partiel scellé qui dit ce qui reste.
