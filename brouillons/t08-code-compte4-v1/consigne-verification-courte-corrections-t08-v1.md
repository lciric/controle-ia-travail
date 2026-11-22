# Consigne — vérification courte des corrections du code de T0.8 — v1

Écrite le 2026-11-14T02:11:45Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A). Lot : plan multi-comptes (`3b1bda25…`), lot « compte 4 », tâche 3. **Aucune dépense, aucune instance, aucun téléchargement de modèle, aucune clé employée.**

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

**Ajoutés pour cette vérification.**
- Lecture seule, sauf les fichiers du § 5 (et des fichiers temporaires dans le bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/0bb788a7-74e8-52db-b35a-9747a8f95b86/scratchpad/verif-corr-t08/`, non versés). Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`, ni `worktree`) ; lecture git permise dans l'arbre `/home/user/t08-code-compte4-v1` seulement (`git -C /home/user/t08-code-compte4-v1 log|show|diff|ls-tree` sur les commits nommés ici et les chemins `src/controle_ia/t08/`, `tests/test_t08_*`, `docs/notes/t08-code-compte4-v1/`, `essai/t08-jouet-compte4-v1/`). Aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **aucun fichier de T0.7** (ni `prereg/T0.7-*`, ni `src/controle_ia/t07/`) : tu n'en as pas besoin, et sa lecture t'exclurait du verdict de P3-bis ; si un passage du code t'y renvoie, écris-le en « non vérifiable » sans l'ouvrir.
- **Rien de `donnees/`, `diag/`, `runs/` à la racine d'un dépôt** (ni dans `/home/user/controle-ia-travail`, ni à la racine de `/home/user/t08-code-compte4-v1`) ; en particulier, **jamais** `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (il porte les cibles réelles). **Permis** : les sorties **factices** de l'essai du développeur sous `/home/user/t08-code-compte4-v1/essai/t08-jouet-compte4-v1/a/`, `…/b/`, `essai/t08-jouet-compte4-v2/a/` et `…/b/` (leurs sous-dossiers `diag/`, `runs/`, `donnees/`, `registres-factices/`, `prereg/`, `docs/` y sont des copies ou des fabrications de l'essai, sans donnée réelle ; les noms « t06-7b-jouet » y désignent un 7b **factice**).
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; `grep -n` permis aussi sur le seul dossier `src/controle_ia/t08/` et sur les fichiers `tests/test_t08_*_v1.py` de l'arbre ; jamais `grep -r` ailleurs, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course réelle (tu lis des textes, du code et les sorties factices de l'essai jouet, rien d'autre).
- **Interdit du programme** : jamais de moyenne ni de médiane sur les jetons dans un score de sonde ; si tu en vois une dans le code, c'est un constat bloquant.
- **Modèles** : dans tout fichier que tu écris, ton modèle est « modèle B » et celui du développeur « modèle A » (R-2598), sans identifiant.


## 1. Qui tu es

Vérificateur **neuf** des corrections du code de T0.8, sous-agent de la session du compte 4. Tu n'as écrit ni ce code, ni ses corrections, ni sa contre-lecture 1, ni T0.8 (brouillons, base (A)), ni T0.6, T0.7 ou P3-bis, ni aucune de leurs contre-lectures. Ton modèle doit être **différent** du modèle A (N-052) ; tu donnes ton identifiant de modèle dans ton **dernier message** à la session seulement, jamais dans un fichier. Tu seras exclu ensuite du verdict de T0.8 ; la session du compte 4 te déclare à la mère pour « qui a lu quoi ». Français ; aucun sigle non développé.

## 2. Objet

La contre-lecture 1 du code (modèle B) a rendu « autorisable après les corrections listées » (CLT8C-01 à CLT8C-21) au commit `27c092642247e01f57ea3f80ec9ccd29f5798557`. La session a choisi entre les options du lecteur (journal, C4-0030). Un développeur des corrections (modèle A) a poussé un jalon 1 (`61fbe4f0`) puis s'est arrêté au redémarrage du conteneur ; un développeur neuf (modèle A) a repris (consigne de reprise) et rendu le commit final `7a4d4e130460d7c91420bf2b20a0ef59025659b3` ; code et essais figés depuis `28bf2aee`. Ta vérification, **courte et différentielle** (`27c09264` → `7a4d4e13`), dit si chaque constat est corrigé comme demandé, si les corrections introduisent un défaut, et si le code peut être cité par le texte candidat de T0.8 (marqueur `COMMIT_CODE_T08`). Tu ne corriges rien : tu rends un rapport.

## 3. Fichiers à lire (vérifie chaque empreinte avant lecture)

| rôle | chemin | sha256 |
|---|---|---|
| constats | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/contre-lecture-1-code-t08-v1.md` | `7c47e18266a970abafb33335c5a0f7f9e768820a833e017aebc5bcec4b76d280` (compagnon) |
| script de la contre-lecture 1 (parties A à G ; rejoue ce qui s'y prête au commit final, dans le bloc-notes) | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/contre-lecture-1-code-t08-v1-calcul.py` | `cacc9e1ee90eb9ac1f45e0dbe7aa018ab40122651b350b0f32b0c7006da04b2f` (compagnon) |
| choix de la session (section C4-0030) | `/home/user/controle-ia-travail/registres-provisoires/compte-4-2026-11-14-v3.md` | `2f338351643350c502a43ceba163696e855d2cb103c72719eae91c35ef756c5d` (compagnon) |
| consignes des corrections et de la reprise | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/consigne-developpeur-corrections-t08-v1.md` ; `…/consigne-developpeur-corrections-t08-v1-reprise-v1.md` | `e2577b5a0a2e60a6108e4436660beb9d6e8967fd65056958ef9be48a4f7c778b` ; `b03d8d3fab0482f580818c44278daf07bec5cdcb701f0eae154171b7c9cb55db` (compagnons) |
| **rapport des corrections** (en entier) | `/home/user/t08-code-compte4-v1/docs/notes/t08-code-compte4-v1/rapport-developpeur-corrections-t08-v1.md` | `6b05409c2ccbbcc9a4654baa2aad2a0c67bbfa7bc0636099289700f75931bb84` (compagnon) |
| **différentiel du code** | `git -C /home/user/t08-code-compte4-v1 diff 27c09264 7a4d4e13 -- src/controle_ia/t08 tests` (et `git show` des fichiers au commit final) | — |
| texte qui fait foi, aux lignes que citent les constats et le rapport (le texte prime) | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` | `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` (compagnon) |
| base (A) scellée, au besoin | `/home/user/controle-ia-travail/prereg/T0.8-base-A-mots-et-cout-v1.md` | `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` (compagnon) |
| configuration de 7b (CLT8C-06) | `/home/user/controle-ia-travail/prereg/T0.6-organismes-config-7b-v1.json` | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` |
| sorties factices des deux essais de bout en bout v2 | `/home/user/t08-code-compte4-v1/essai/t08-jouet-compte4-v2/a/` et `…/b/` | empreintes au § 4 du rapport des corrections |

## 4. Ce que tu vérifies

1. **Chacun des 21 constats** : corrigé tel que le lecteur le propose ou selon le choix de C4-0030 (et, pour CLT8C-16, -17, -18, -21, selon la consigne des corrections, § 3) ; fichier:ligne au commit final ; l'essai sain **et** l'artefact existent et éprouvent vraiment la garde (une garde retirée ferait-elle échouer l'essai ?). Classe chacun « corrigé », « corrigé avec réserve », « non corrigé ».
2. **Défauts neufs** introduits par le différentiel (≈ 2 500 lignes) : garde qui refuse à tort ou laisse passer, repli silencieux, `try`/`except` large, fuite de `cibles` vers un juge ou l'agent d'étalonnage, appel réseau ou lecture de clé, moyenne ou médiane sur les jetons, phrase gelée des tables D et F changée (rejoue la comparaison des phrases au commit final), règle de lecture ou seuil autres que ceux du texte. Vise en priorité : `lecture_v1.py`, `temoin_distille_v1.py`, `entrees_v1.py`, `tables_v1.py`, `juges_v1.py` (arrêt de la génération à la balise : point de lecture inchangé ?), `course_v1.py`.
3. **Déterminisme** : le rapport dit 52 fichiers comparés, 41 identiques, 3 égaux sur le contenu, 7 exclus et **1 différent** (`lecture-t08.json`, clé `tables_D_F_fichier.sha256`, empreinte d'un fichier dont l'enveloppe porte le manifeste daté). Vérifie la cause sur les deux sorties (comparaison par un script du bloc-notes, sans rien écrire dans l'arbre) ; dis si l'écart est seulement l'effet de la date du manifeste, si le contenu des tables est égal, et s'il empêche de citer ce commit (R9 : sorties identiques à l'octet à même entropie) ; propose la correction (exclusion déclarée dans le comparateur, ou empreinte du seul contenu) et sa gravité.
4. **Questions Q-C1 à Q-C9** du rapport : pour chacune, le texte la tranche-t-il ; sinon le choix est-il compatible et le plus prudent ; classe-la « conforme au texte », « choix à confirmer par la mère », « nœud (Lazar) » ou « contraire au texte ».
5. **Reprise** : le récit du § 0 du rapport (jalon 1 du développeur arrêté, modification non committée gardée) est-il conforme à l'historique git (`git log 27c09264..7a4d4e13`) ?
6. **Essais rejoués**, depuis l'arbre (`cd /home/user/t08-code-compte4-v1`, `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -p no:cacheprovider`) : tous les `tests/test_t08_*_v1.py` ; les cinq essais d'inventaire (`tests/test_cibles_invisibles_v1.py`, `tests/test_cibles_invisibles_v2.py`, `tests/test_t06_v11_liste.py`, `tests/test_t06_v12_liste.py`, `tests/test_t06_v13_liste.py`), éléments nommés comparés à ceux du § 5.2 de la contre-lecture 1. **Pas** de rejeu de l'essai de bout en bout (il écrit dans l'arbre).

**Gravité** : comme à la contre-lecture 1 (*bloquant* : le code fait autre chose que le texte, une garde laisse passer un artefact ou refuse à tort, fuite de `cibles`, repli silencieux, interdit touché ; *majeur* : à corriger avant la course, correction locale ; *mineur* : le reste).

## 5. Ce que tu rends

Un seul rapport, `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/verification-courte-corrections-t08-v1.md`, scellé par `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`, puis vérifié par `verifier`. Si tu écris un script, dépose-le à côté sous `…/verification-courte-corrections-t08-v1-calcul.py`, scellé aussi, sortie recopiée à l'octet dans le rapport. Rien d'autre n'est écrit hors du bloc-notes.

Sections : **0. Identité** (« modèle B », sans identifiant ; heures `date -u` ; fichiers lus et empreintes) ; **1. Verdict** (trois lignes au plus) : « citable par le texte candidat tel quel », « citable après les corrections listées » ou « non citable en l'état » ; nombres de constats par gravité ; **2. Constats neufs** (`VCT8-01`…, gravité, endroit au commit `7a4d4e13`, preuve, correction et son essai) ; **3. Les 21 constats revus** (une ligne chacun) ; **4. Déterminisme** (point 4.3) ; **5. Questions Q-C1 à Q-C9** ; **6. Essais rejoués** ; **7. Limites**.

Ton dernier message (rendu à la session du compte 4) : le verdict en trois lignes, les nombres de constats par gravité, le chemin et l'empreinte du rapport (et du script s'il existe), ton identifiant de modèle. Rien d'autre. Si ton quota ou ton temps s'épuise : scelle un rapport partiel qui dit ce qui reste.
