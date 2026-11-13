# Consigne — développeur du code de T0.8 (course et lecture), sur données factices — v1

Écrite le 2026-11-13T22:33:40Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), sur le mot « go tache 3 » (journal du compte 4, C4-0019). Lot : plan multi-comptes (`3b1bda25…`), lot « compte 4 », tâche 3. **Aucune dépense, aucune instance, aucun téléchargement de modèle, aucune clé employée.**

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
  - tu travailles **seulement** dans l'arbre `/home/user/t08-code-compte4-v1` (branche `prep/t08-code-compte4-v1`, tirée de `main` à `ee7f2f9c`) ; tu y commites et tu pousses **seulement** par `git -C /home/user/t08-code-compte4-v1 push origin prep/t08-code-compte4-v1`, à chaque jalon, après la garde des secrets à 0 sur `git diff --cached` (motif du brief) ; jamais une autre branche, jamais de réécriture d'historique, jamais de `fetch` ; fin de chaque message de commit : `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` puis `Claude-Session: https://claude.ai/code/session_01Qi7Gr2uGzyVcw9VmDXgvEV` ;
  - tu peux lire le fichier des tâches d'évaluation `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (`76cdeace…`) pour sa **forme** seulement ; tout le reste de `donnees/`, `diag/`, `runs/` t'est interdit ; tes essais n'emploient que des **données factices** que ton code fabrique ;
  - environnement : `/home/user/controle-ia-travail/.venv/bin/python` (installé par la session, `requirements-cpu.txt`), avec `PYTHONPATH=src` de ton arbre ; aucune autre installation sans le dire dans ton rapport ;
  - **aucun appel réseau** de ton code ni de tes essais (ni Hugging Face, ni interface de modèle) ; \`HF_TOKEN\`, \`OPENAI_API_KEY\`, \`GEMINI_API_KEY\`, \`VAST_API_KEY\`, \`HCLOUD_TOKEN\` ne sont jamais lus ;
  - aucun fichier de \`registres/\` (tu ne lis ni n'écris le registre ; les lignes de registre que ton code exige sont lues dans un registre **factice** pendant tes essais) ; aucun fichier de P3-bis ; aucun fichier de T0.7 au-delà de son texte scellé si tu en as besoin (si tu l'ouvres, dis-le : tu en deviens lecteur).
- **Interdit du programme** : jamais de moyenne ni de médiane sur les jetons dans un score de sonde (ce code n'a pas de sonde ; si une moyenne sur les jetons apparaît, elle ne doit jamais être appelée « score de sonde »).
- **Modèles** : écris ton modèle comme « modèle A » (R-2598), sans identifiant, dans tout fichier poussé.

## 1. Qui tu es

Développeur **neuf** du code de T0.8, sous-agent de la session du compte 4. Tu n'as écrit ni T0.8 (brouillons, base (A)), ni T0.6, ni T0.7, ni P3-bis, ni aucune de leurs contre-lectures. Tu seras exclu ensuite de la contre-lecture de ton propre code et du verdict de T0.8.

## 2. Ce qui fait foi (vérifie chaque empreinte avant lecture)

- T0.8, **brouillon 4 gelé** : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md`, `7da0c3839a7a…` (compagnon) ; son journal, ses couples et son script, même préfixe. **Le texte prime** : son « Plan d'analyse » (points 1 à 10, le point 10 est ton cahier des charges), « Métrique », « Seuil », « Critères de lecture gelés » (tables D et F, phrases gelées), « Liste d'arrêt », « Machine, devis et dépense », « Ordre des lectures et embargo », « Marqueurs ».
- Base (A) scellée : `prereg/T0.8-base-A-mots-et-cout-v1.md`, `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` (M2 = base (A)).
- T0.6 scellé (`prereg/T0.6-organismes-v0-v1.md`, `ef31feff…`) et configuration de 7b (`prereg/T0.6-organismes-config-7b-v1.json`, `b7a5c1ba…`) : pour la chaîne gelée, les noms de conditions, la pièce « mots et coût » (base (B) = MC).
- Code existant, **importé sans modification** (R12 ; d'autres textes en dépendent) : `src/controle_ia/bases/` (`sequentiel`, `scores_jetons`, …), `src/controle_ia/t06/` (`cout`, chaîne, pièce « mots et coût »), `src/controle_ia/harnais/`, `src/controle_ia/manifeste.py`, `src/controle_ia/scellement.py`, `src/controle_ia/gardes.py`, `src/controle_ia/run_factice.py`.

## 3. Ce que tu écris

- Modules **neufs** sous `src/controle_ia/t08/` (noms versionnés, `…_v1.py`), essais sous `tests/test_t08_…_v1.py`, et, s'il le faut, le script de la course sous `scripts/…t08…_v1.sh` (écrit et éprouvé à blanc, **jamais lancé** : toute création d'instance est hors de ta consigne, et le crochet de garde l'interdit sans ligne de GO).
- **Tout ce que demande le point 10** du plan d'analyse, un par un ; chaque garde **éprouvée sur un cas sain et sur un artefact** (R5), en particulier les artefacts que le point 10 nomme (coefficient décalé de 1·10⁻⁵, centre changé, trait retiré de plus, (jeu, pli) manquant ; modèle réappris sur T100 ; modèle ou seuil recalculé sur les épisodes de la pièce HD ; date postérieure à `SORTIES-HD-VADAPT` ; dose à 63 épisodes ; refus de `cibles` ; liste blanche ; refus de `adaptateur-hd.pt` et des sorties des pièces R et L).
- Les juges (J8r, J8p, J3r, J3p) par une interface de modèle **remplaçable** : un **modèle jouet** sur processeur pour les essais ; le chargement des vrais modèles (révisions du texte) écrit mais jamais exécuté ici.
- **Essai de bout en bout** sur le modèle jouet et des épisodes factices (neuf conditions de 7b, 64 tâches, 10 actions, plus l'étalonnage et une pièce HD factice), sur processeur, sans réseau, **avec manifeste** (`controle_ia.manifeste` ; graines par `numpy.random.SeedSequence`, R9), sorties écrites et scellées sous `essai/t08-jouet-compte4-v1/` de ton arbre (nom neuf ; jamais `essai/t06-explo-v3`) ; `lecture-t08.json` factice avec les tables D et F en phrases gelées.
- Les sept marqueurs du brouillon 4 restent des marqueurs : ton code les attend **en arguments ou en configuration**, jamais en valeurs inventées ; il refuse de courir en mode réel tant que l'un manque (garde éprouvée).

## 4. Essais

- `PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q` sur **toute** la suite de ton arbre : aucun échec neuf (relève l'état de la suite avant tes changements, pour comparer) ; tes essais neufs verts.
- Lance l'essai de bout en bout deux fois avec la même entropie : sorties identiques à l'octet (déterminisme), consigné.

## 5. Ce que tu rends

Un rapport du développeur, `docs/notes/t08-code-compte4-v1/rapport-developpeur-t08-v1.md` dans ton arbre, scellé (`PYTHONPATH=src …/.venv/bin/python -m controle_ia.scellement sceller <fichier>`), committé et poussé avec le code. Sections : **0. Identité** (modèle A, heures `date -u` de début et de fin, fichiers lus et empreintes) ; **1. Ce qui est fait** : table « exigence du point 10 (et des autres points du plan) → fonction (fichier:ligne) → essai (sain, artefact) » ; **2. Fichiers neufs** et leur sha256, commit final ; **3. Suite d'essais** avant et après (nombres de réussites, d'échecs, d'ignorés) ; **4. Essai de bout en bout** (chemin, manifeste, empreintes, déterminisme) ; **5. Écarts au texte** : aucun écart n'est permis ; tout point ambigu est écrit en question, avec le choix le plus prudent retenu et déclaré ; **6. Ce qui reste hors du code** (marqueurs, chargement réel des modèles, course) ; **7. Limites**. Puis, en dernier message à la session : commit final, branche, chemin et empreinte du rapport, nombres d'essais, questions ouvertes. Rien d'autre.

Si ton quota ou ton temps s'épuise avant la fin : commite et pousse ce qui est fait, avec un rapport partiel scellé qui dit ce qui reste.
