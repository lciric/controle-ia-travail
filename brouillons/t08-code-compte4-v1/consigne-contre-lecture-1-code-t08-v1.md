# Consigne — contre-lecture 1 du code de T0.8 (course et lecture, données factices) — v1

Écrite le 2026-11-14T00:27:09Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A). Lot : plan multi-comptes (`3b1bda25…`), lot « compte 4 », tâche 3 (journal du compte 4, C4-0026). **Aucune dépense, aucune instance, aucun téléchargement de modèle, aucune clé employée.**

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

**Ajoutés pour cette contre-lecture.**
- Lecture seule, sauf les fichiers du § 5 et la racine de rejeu du § 4, point 9. Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`, ni `worktree`) ; lecture git permise dans l'arbre `/home/user/t08-code-compte4-v1` seulement (`git -C /home/user/t08-code-compte4-v1 log|show|diff|ls-tree` sur les commits nommés ici et les chemins `src/controle_ia/t08/`, `tests/test_t08_*`, `docs/notes/t08-code-compte4-v1/`, `essai/t08-jouet-compte4-v1/`). Aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **aucun fichier de T0.7** (ni `prereg/T0.7-*`, ni `src/controle_ia/t07/`) : tu n'en as pas besoin, et sa lecture t'exclurait du verdict de P3-bis ; si un passage du code t'y renvoie, écris-le en « non vérifiable » sans l'ouvrir.
- **Rien de `donnees/`, `diag/`, `runs/` à la racine d'un dépôt** (ni dans `/home/user/controle-ia-travail`, ni à la racine de `/home/user/t08-code-compte4-v1`) ; en particulier, **jamais** `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (il porte les cibles réelles). **Permis** : les sorties **factices** de l'essai du développeur sous `/home/user/t08-code-compte4-v1/essai/t08-jouet-compte4-v1/a/` et `…/b/` (leurs sous-dossiers `diag/`, `runs/`, `donnees/`, `registres-factices/`, `prereg/`, `docs/` y sont des copies ou des fabrications de l'essai, sans donnée réelle ; les noms « t06-7b-jouet » y désignent un 7b **factice**).
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; `grep -n` permis aussi sur le seul dossier `src/controle_ia/t08/` et sur les fichiers `tests/test_t08_*_v1.py` de l'arbre ; jamais `grep -r` ailleurs, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course réelle (tu lis des textes, du code et les sorties factices de l'essai jouet, rien d'autre).
- **Interdit du programme** : jamais de moyenne ni de médiane sur les jetons dans un score de sonde ; si tu en vois une dans le code, c'est un constat bloquant.
- **Modèles** : dans tout fichier que tu écris, ton modèle est « modèle B » et celui du développeur « modèle A » (R-2598), sans identifiant.

## 1. Qui tu es

Contre-lecteur **neuf** du code de T0.8, sous-agent de la session du compte 4. Tu n'as écrit ni ce code, ni T0.8 (brouillons, base (A)), ni T0.6, ni T0.7, ni P3-bis, ni aucune de leurs contre-lectures. Ton modèle doit être **différent** du modèle A (N-052) ; tu donnes ton identifiant de modèle dans ton **dernier message** à la session seulement, jamais dans un fichier. Tu seras exclu ensuite de la correction de ce code et, par prudence, du verdict de T0.8 ; la session du compte 4 te déclare à la mère pour « qui a lu quoi ». Français ; aucun sigle non développé.

## 2. Objet

Le développeur (modèle A) a écrit le code de la course et de la lecture de T0.8 sur données factices, au commit final `27c092642247e01f57ea3f80ec9ccd29f5798557` de la branche `prep/t08-code-compte4-v1` (arbre `/home/user/t08-code-compte4-v1`, tiré de `main` à `ee7f2f9c`). Son cahier des charges est le **point 10** du « Plan d'analyse » du brouillon 4 gelé de T0.8 (et les autres points du plan qu'il cite). Ta contre-lecture (R2) dit si ce code fait ce que le texte demande, sans plus ni moins, si chaque garde est éprouvée sur un cas sain et sur un artefact (R5), et s'il existe un repli silencieux, une fuite de `cibles`, une lecture qui contredit le texte ou un interdit du programme touché. Tu ne corriges rien : tu rends un rapport.

**Faits donnés par la session du compte 4, non relus au registre (le registre t'est interdit) :**
- Le code de la pièce « mots et coût » de T0.6 (ligne `CODE-MOTS-ET-COUT-T06`) n'existe pas encore ; le développeur a fixé un contrat et une pièce **jouet** (rapport, Q-1).
- Par décision de la mère (R-2604), la pièce HD (témoin distillé honnête, texte « validité de l'adaptateur ») n'est créée **que si** P3-bis rend « vu » : il est donc possible que `SORTIES-HD-VADAPT` n'existe jamais. Ce que fait le code dans ce cas t'est demandé au § 4, point 5.

## 3. Fichiers à lire (vérifie chaque empreinte avant lecture : `sha256sum <fichier>`, ou `verifier` s'il a un compagnon)

| rôle | chemin | sha256 |
|---|---|---|
| **texte qui fait foi** : brouillon 4 gelé de T0.8 (lis-le en entier : « Les surveillants », « Métrique », « Seuil », « Plan d'analyse » points 1 à 10, « Critères de lecture gelés » (tables D et F, phrases gelées), « Liste d'arrêt », « Ordre des lectures et embargo », « Marqueurs ») | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` | `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` (compagnon) |
| base (A) scellée (M2) | `/home/user/controle-ia-travail/prereg/T0.8-base-A-mots-et-cout-v1.md` | `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` (compagnon) |
| T0.6 scellé, **par sections** : l. 573-584 (règle « mots et coût »), l. 763-772 (« Concordance avec T0.7 », lue pour ses seules phrases sur la chaîne, sans ouvrir T0.7), et toute section que le code cite (noms des conditions, chaîne gelée) | `/home/user/controle-ia-travail/prereg/T0.6-organismes-v0-v1.md` | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` (compagnon) |
| configuration de 7b | `/home/user/controle-ia-travail/prereg/T0.6-organismes-config-7b-v1.json` | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` |
| configuration du pilote (spécification des juges seulement) | `/home/user/controle-ia-travail/prereg/T0.5-pilote-config-v1.json` | `6979a00ebef1e794f900e089df9b1658482f8600ce343cb81c95da4434da2b8a` |
| invite dérivée H.12 et son brouillon | `/home/user/controle-ia-travail/docs/sources/invites-2606.08892-v1/derivees/H12-par-action-v1.txt` ; `/home/user/controle-ia-travail/brouillons/T0.8-moniteur-par-action-H12-derive-v1-brouillon1.md` | `5a30c2b3ce283531a90661df078f3d1d0e179312c9d0cd1328caf63b69023220` ; `c1f2bc299d34b2b1f666176997b227eab1660f3afac3c2196ad0fabd4adcde02` |
| consigne du développeur | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/consigne-developpeur-t08-v1.md` | `94b0e43af5d5cfc095679ef97bc26a7769ee12d7cf00970150be40736fc533b2` (compagnon) |
| **rapport du développeur** (lis-le en entier ; ses références « fichier:ligne » sont au commit `634916d8`, dont `src/` serait identique au commit final : vérifie-le par `git diff 634916d8 27c09264 -- src/`) | `/home/user/t08-code-compte4-v1/docs/notes/t08-code-compte4-v1/rapport-developpeur-t08-v1.md` | `5b1e873198f38c6b1725355c18212f9b889597071f7820d82f9f12b058c1a5cc` (compagnon) |
| **code contre-lu** : les quinze modules `src/controle_ia/t08/*.py` et les sept essais `tests/test_t08_*_v1.py` de l'arbre, en entier | `/home/user/t08-code-compte4-v1/…` | empreintes au § 2 du rapport (vérifie-les toutes) |
| code existant importé (parties que le code neuf appelle ; empreintes au § 0 du rapport, douze premiers caractères) | `src/controle_ia/bases/`, `t06/`, `harnais/`, `environnements/`, `premier_test_ia/`, `manifeste.py`, `scellement.py`, `gardes.py`, `sondes/evaluation.py` de l'arbre (fichiers nommés par le rapport seulement) | — |
| sorties factices de l'essai (pour le déterminisme, les phrases gelées et la forme des sorties) | `/home/user/t08-code-compte4-v1/essai/t08-jouet-compte4-v1/a/` et `…/b/` (fichiers nommés au § 4 du rapport) | empreintes au § 4 du rapport |

## 4. Ce que tu vérifies

1. **Point 10, exigence par exigence**, et les points 1 à 9 du plan qu'il appelle : la table du § 1 du rapport dit-elle vrai ? Pour chaque ligne : la fonction fait-elle ce que le texte demande (citer la ligne du brouillon 4 et un extrait court) ; l'essai éprouve-t-il réellement le cas sain **et** l'artefact (R5), ou seulement l'un des deux ; une exigence du texte manque-t-elle à la table ?
2. **Gardes et replis** : chaque garde qui arrête arrête-t-elle sans rien écrire là où le texte le demande (contrôle d'identité de M2, étapes (a) et (b)) ; existe-t-il un `try`/`except` large, une valeur par défaut, une imputation ou un « non lu » qui masquerait une erreur (R5 : aucun repli silencieux) ; une garde refuse-t-elle à tort un cas que le texte permet ?
3. **Embargo des cibles et liste blanche** : aucun chemin par lequel `cibles` (ou toute clé autre que `identifiant`, `questions`) atteint une entrée d'un juge ou de l'agent d'étalonnage ; motifs interdits de la liste blanche comparés à la « Liste d'arrêt » et à « Ordre des lectures et embargo » ; le collecteur `tests/test_t08_cibles_invisibles_v1.py` couvre-t-il tous les chemins d'entrée ?
4. **Juges et lectures** : rendu de l'ensemble marqué (texte exact contre « Ce que voit chaque surveillant » et l'invite H.12 dérivée) ; une passe (balise, espérance sur 101 jetons, masse, drapeau « masse faible ») ; raisonnement (≤ 400 jetons, température 1,0, graine par lecture, lecture au point de la balise sur les identifiants générés, balise imposée après troncature, DB8-8) ; chargement réel écrit et jamais exécuté, révisions et gabarit daté conformes au texte.
5. **Témoin distillé honnête (point 8 bis)** : liste blanche des fichiers HD, refus de `adaptateur-hd.pt` et des sorties R et L, aucun calcul sur les épisodes HD, antériorité de `GEL-T08` (ou du commit) sur `SORTIES-HD-VADAPT`, effectifs (dose à 63 épisodes), ordre (h bis) après les tables D et F. **Et : que fait la lecture si la ligne `SORTIES-HD-VADAPT` n'existe pas du tout** (pièce HD jamais créée, R-2604) — l'étape (h bis) rend-elle une phrase « non lue » sans arrêter la lecture ni toucher aux tables D et F ? Si le code arrête toute la lecture dans ce cas, c'est au moins majeur ; dis ce que dit le texte.
6. **Statistiques et tables** : séries à pas lus et −∞, M1 et M1c, calibrage (deux jeux disjoints, rang conforme, −∞ au plus bas rang, alerte stricte, rang > K), Clopper et Pearson (niveaux du texte), aires par action, comparaisons appariées, échangeabilité, audit R4 ; **tables D et F : chaque phrase gelée du code égale, au caractère près, à la phrase du texte** (écris un script court qui extrait les phrases du brouillon 4 et du code et les compare ; sortie recopiée à l'octet).
7. **Les dix-neuf questions Q-1 à Q-19** du rapport : pour chacune, le texte la tranche-t-il déjà (citer) ; sinon, le choix retenu est-il compatible avec le texte et le plus prudent ; classe-la « conforme au texte », « choix à confirmer par la mère », « nœud (Lazar) » ou « contraire au texte ».
8. **Graines, manifeste et déterminisme (R9)** : graines toutes dérivées par `numpy.random.SeedSequence`, clés du manifeste conformes au texte ; aucune graine fixe cachée ; sept marqueurs attendus en configuration, jamais inventés, mode réel refusé si l'un manque ; aucun appel réseau ni lecture de clé dans le code.
9. **Essais, rejoués** (depuis l'arbre, `cd /home/user/t08-code-compte4-v1`, avec `PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -p no:cacheprovider`) :
   - les sept fichiers `tests/test_t08_*_v1.py` : nombres de réussites et d'échecs ;
   - les essais d'inventaire que le rapport dit déjà en échec (`tests/test_cibles_invisibles_v1.py`, `tests/test_cibles_invisibles_v2.py`, `tests/test_t06_v11_liste.py`, `tests/test_t06_v12_liste.py`, `tests/test_t06_v13_liste.py`) : leur message d'échec nomme-t-il des éléments **autres** que ceux du code neuf (donc un échec antérieur), ou seulement ceux du code neuf (donc un échec neuf) ?
   - un rejeu de l'essai de bout en bout, **une fois**, dans une racine neuve hors des deux dépôts : `PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m controle_ia.t08.essai_jouet_v1 --racine /tmp/claude-0/-home-user-controle-ia-travail/0bb788a7-74e8-52db-b35a-9747a8f95b86/scratchpad/t08-rejeu-cl1 --horodatage 20261113-233002 --entropie 70475075446708653957179940349299915985 --comparer essai/t08-jouet-compte4-v1/a` (environ six minutes ; si la commande diffère dans `essai_jouet_v1.py`, prends celle du code et dis-le) : nombres de fichiers identiques, égaux sur le contenu, exclus, différents.

**Gravité.** *Bloquant* : le code fait autre chose que le texte (règle de lecture, phrase gelée, seuil, garde), une garde laisse passer un artefact ou refuse à tort, une fuite de `cibles`, un repli silencieux, un interdit du programme touché. *Majeur* : à corriger avant la course, correction locale. *Mineur* : le reste.

## 5. Ce que tu rends

Un seul rapport, `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/contre-lecture-1-code-t08-v1.md`, scellé par `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>` (compagnon `.sha256`), puis vérifié par `verifier`. Si tu écris un script (phrases gelées, arithmétique), dépose-le à côté sous `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/contre-lecture-1-code-t08-v1-calcul.py`, scellé aussi, sortie recopiée à l'octet dans le rapport. La racine de rejeu (§ 4, point 9) reste dans le bloc-notes et n'est pas versée. Rien d'autre n'est écrit.

Sections du rapport :
- **0. Identité** : « modèle B » (sans identifiant) ; heures de début et de fin (`date -u`) ; table des fichiers lus, empreinte vérifiée, parties lues.
- **1. Verdict** (trois lignes au plus) : « autorisable pour la course tel quel », « autorisable après les corrections listées » ou « non autorisable en l'état » ; nombre de constats par gravité.
- **2. Constats**, un par ligne : identifiant `CLT8C-01`, `CLT8C-02`… ; gravité ; endroit (fichier:ligne au commit `27c09264`, extrait court) ; preuve (ligne du brouillon 4 ou de la base (A), extrait de trente mots au plus, ou sortie d'un essai) ; correction proposée (ce qu'il faut changer, et l'essai sain et artefact qui la prouvera). Quand la correction change le dessin (règle de lecture, seuil, ordre, ce qui est lu ou non lu) : deux ou trois options (avantage, inconvénient), ta recommandation et ta confiance, marquée « décision de la mère » ou « nœud (Lazar) ».
- **3. Table du point 10 revue** (point 4.1) : une ligne par exigence, « tenue », « tenue avec réserve » ou « non tenue », avec le constat lié.
- **4. Questions Q-1 à Q-19** (point 4.7) : une ligne chacune.
- **5. Essais rejoués** (point 4.9) : commandes, nombres, sorties utiles recopiées.
- **6. Non vérifiable** : ce qui dépend de T0.7, de P3-bis, du registre, du code de la pièce « mots et coût » absent, du chargement réel.
- **7. Limites** : ce que tu n'as pas lu ou pas pu vérifier.

Ton dernier message (rendu à la session du compte 4) : le verdict en trois lignes, les nombres de constats par gravité, le chemin et l'empreinte du rapport (et du script s'il existe), ton identifiant de modèle. Rien d'autre.

Si ton quota ou ton temps s'épuise avant la fin : scelle un rapport partiel qui dit ce qui reste.
