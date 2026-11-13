# Consigne — développeur du code du saboteur à budget (ii-b), sur données factices — v1

Écrite le 2026-11-13T22:51:02Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), tâche 4 du lot (« seconde vague : code du saboteur à budget, six épreuves de l'oracle, devis » ; plan multi-comptes `3b1bda25…`), dans l'autonomie accordée par Lazar (journal du compte 4, C4-0023). **Aucune dépense, aucune instance, aucun téléchargement de modèle, aucune clé employée.**

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
- Lecture seule, sauf les deux fichiers du § 5. Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`), aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** (la mère n'en a nommé aucun pour ce lot) ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **rien de `donnees/`, `diag/`, `runs/`**.
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; jamais `grep -r`, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course (tu lis des textes et du code, rien d'autre).

- **Exceptions de cette consigne** (elles remplacent, pour toi, les ajouts ci-dessus qui interdisent l'écriture git et la lecture de `donnees/`) :
  - tu travailles **seulement** dans l'arbre `/home/user/iib-code-compte4-v1` (branche `prep/iib-code-compte4-v1`, tirée de `main` au commit relevé à la création de l'arbre, écrit au journal du compte 4) ; tu y commites et tu pousses **seulement** par `git -C /home/user/iib-code-compte4-v1 push origin prep/iib-code-compte4-v1`, à chaque jalon, après la garde des secrets à 0 sur `git diff --cached` (motif du brief) ; jamais une autre branche, jamais de réécriture d'historique, jamais de `fetch` ; fin de chaque message de commit : `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` puis `Claude-Session: https://claude.ai/code/session_01Qi7Gr2uGzyVcw9VmDXgvEV` ;
  - environnement : `/home/user/controle-ia-travail/.venv/bin/python` (installé par la session, `requirements-cpu.txt`), avec `PYTHONPATH=src` de ton arbre ; aucune autre installation sans le dire dans ton rapport ;
  - **aucun appel réseau** de ton code ni de tes essais (ni Hugging Face, ni interface de modèle) ; \`HF_TOKEN\`, \`OPENAI_API_KEY\`, \`GEMINI_API_KEY\`, \`VAST_API_KEY\`, \`HCLOUD_TOKEN\` ne sont jamais lus ;
  - aucun fichier de \`registres/\` (tu ne lis ni n'écris le registre ; les lignes de registre que ton code exige sont lues dans un registre **factice** pendant tes essais) ; aucun fichier de P3-bis ; aucun fichier de T0.7 au-delà de son texte scellé si tu en as besoin (si tu l'ouvres, dis-le : tu en deviens lecteur).
- **Interdit du programme** : jamais de moyenne ni de médiane sur les jetons dans un score de sonde (ce code n'a pas de sonde ; si une moyenne sur les jetons apparaît, elle ne doit jamais être appelée « score de sonde »).
- **Modèles** : écris ton modèle comme « modèle A » (R-2598), sans identifiant, dans tout fichier poussé.

- **Pour ce chantier** : le fichier des tâches d'évaluation n'est pas lu ; la consigne privée du maître (brouillon 2) est lue pour sa **forme** (nombre de blocs cités, empreinte), et les essais emploient une consigne **factice** de même forme ; jamais la lecture exploratoire de 7a ; jamais un fichier du bras d'attaque.

## 1. Qui tu es

Développeur **neuf** du code de (ii-b), sous-agent de la session du compte 4. Tu n'as écrit ni les textes de (ii-b) (conception, consigne privée, ordre, devis), ni leur contre-lecture, ni T0.6, T0.7, P3 ou P3-bis. Tu seras exclu ensuite de la contre-lecture de ton propre code.

## 2. Ce qui fait foi (vérifie chaque empreinte avant lecture)

| pièce | chemin et sha256 |
|---|---|
| `brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1-brouillon2.md` | `47b86258df937dc5ec8c3e6ff74cc708ea0487a018f54f3a91a721b76543209c` |
| `brouillons/ii-b-saboteur-budget-v1/consigne-privee-maitre-ii-b-v1-brouillon2.md` | `9f8bbdef8c0dd2d276995747d478f6d8061cc447a12af23ba7774a9d75ff90c1` |
| `brouillons/ii-b-saboteur-budget-v1/devis-ii-b-v1-brouillon2.md` | `959df4513c0026580e5a1f8d1ffb25a3ff5afed33ed2682981c6c36c4082505a` |
| `brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1-brouillon2.md` | `4c083d75484e29c0c92d100a5b0bd4110f373e3fe17f500a868cb0f826f6a407` |
| `brouillons/ii-b-saboteur-budget-v1/contre-lecture-ii-b-v1-cl1.md` | `0991e0192932893eb091d7c4d6b0b2bfb3ed6cbeae83bec1f48818dcb4a6734d` |
| `brouillons/ii-b-saboteur-budget-v1/simulation-regle-acceptation-ii-b-v2.py` | `0192af7a0870e090ac5f1c49ab21c7e06a8320da88e09bd80b9c5c24dfcee7ee` |
| `brouillons/ii-b-saboteur-budget-v1/calcul-devis-ii-b-v1.py` | `bb7dd00ed6bee1f51721611f957bdb6aa8175b9c509f3b05419638d53b618518` |

**Le texte prime** : conception, brouillon 2, **section 10** (ton cahier des charges : chaque module, chaque essai sain et artefact de la table) ; sections 2 (maître, oracle, jumeau), 3 (règle d'acceptation, **épreuves E-O1 à E-O6** de la section 3.4), 4 (arrêts M-1 à M-3, Clopper-Pearson), 5 (distillation, témoin-jumeau, doses), 6 (lectures (1) et (2)), 9 (graines) ; l'ordre exploratoire, brouillon 2, pour les gardes de la course. **M7 n'est pas tranchée** (deux variantes côte à côte : A et B) : ton code accepte l'une ou l'autre **par configuration** et n'en choisit aucune ; les **30 marqueurs** des textes restent des marqueurs (le code les attend en configuration et refuse le mode réel tant que l'un manque, garde éprouvée).

**Base de code** : la chaîne de T0.6 telle qu'elle est sur `main` (`src/controle_ia/t06/`, intégrée depuis la conception ; cite le commit de `main` de ton point de départ comme « commit d'intégration ») ; le texte cite aussi le commit `1609a4bf`, présent dans le clone (référence `refs/remotes/origin/audit-fuites-prep/1609a4bf`), lisible par `git show` seulement. **Tout est neuf, sous nom neuf**, dans `src/controle_ia/iib/`, `scripts/…iib…_v1.*`, `tests/test_iib_*_v1.py` ; aucun module existant n'est modifié ; ce qui est repris est importé.

## 3. Ce que tu écris

- Chaque ligne de la table de la section 10, avec ses essais (R5 : cas sain **et** artefact pour chaque garde), dont : les **six épreuves E-O1 à E-O6** en fonctions pures sur les sorties de l'oracle, chacune déclenchée sur son artefact et jamais sur le cas sain ; la **garde statique** de `regle_v1` (aucun import de `bases`, `sondes`, `t07`, `environnements.juges`) ; la garde « aucune sonde » du lanceur ; le **marqueur planté dans la consigne du maître absent de tout contexte du jumeau, de toute transcription de distillation, de toute invite d'évaluation** (essai sur le modèle de `tests/test_t06_cibles_invisibles_v1.py`) ; la réécriture de la valeur entière du champ COST (décision M4) sur tous les cas de la table.
- Le modèle de langue derrière une interface **remplaçable** : un **modèle jouet** sur processeur pour les essais ; le chargement réel écrit, jamais exécuté.
- Les scripts de session et d'amorce, **écrits et éprouvés à blanc, jamais lancés** (garde de GO : sain, ligne absente, échue, révoquée ; étiquette `iib-explo-v1` ; « 7b non créée → refus »), sur un registre de GO **factice** : tu ne lis pas `registres/go.md`.
- **Répétition jouet de bout en bout** (processeur, sans réseau) avec manifeste (`controle_ia.manifeste`, graines par `numpy.random.SeedSequence`, R9) : étalonnage, épreuves, tours, distillation sur l'élève jouet, évaluation, oracle, lectures (1) et (2) ; sorties scellées sous `essai/iib-jouet-compte4-v1/` de ton arbre ; jouée deux fois à la même entropie : sorties identiques à l'octet.

## 4. Essais

`PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q` sur toute la suite de ton arbre : relève l'état avant tes changements ; après : aucun échec neuf, tes essais verts.

## 5. Ce que tu rends

Un rapport du développeur, `docs/notes/iib-code-compte4-v1/rapport-developpeur-iib-v1.md` dans ton arbre, scellé, committé et poussé avec le code. Sections : **0. Identité** (modèle A, heures `date -u`, fichiers lus et empreintes) ; **1. Ce qui est fait** : table « ligne de la section 10 (et épreuve E-O1 à E-O6) → fonction (fichier:ligne) → essai sain, essai artefact » ; **2. Fichiers neufs**, sha256, commit final ; **3. Suite d'essais** avant et après ; **4. Répétition jouet** (chemin, manifeste, empreintes, déterminisme) ; **5. Choix laissés au code** (section 10, dernier paragraphe : forme du lot des suites, ordre des lots), déclarés ; **6. Écarts au texte** : aucun permis ; tout point ambigu en question, choix le plus prudent retenu et déclaré ; **7. Ce qui reste hors du code** (marqueurs, M7, chargement réel, course) ; **8. Limites**. Dernier message : commit final, branche, chemin et empreinte du rapport, nombres d'essais, questions ouvertes.

Si ton quota ou ton temps s'épuise avant la fin : commite et pousse ce qui est fait, avec un rapport partiel scellé qui dit ce qui reste.
