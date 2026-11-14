# Brief du compte 3 — veille datée et reproduction NARCBench sur activations publiées — v1

Écrit le 2026-11-13 à 20:24 UTC (heure relevée par `date -u`) par un rédacteur neuf, sur le mot de Lazar (R-2585 : « go les quatre briefs pour mes autres comptes »). Fait foi : `docs/notes/plan-paquet-multi-comptes-v1/plan-paquet-multi-comptes-v1.md` (`3b1bda25…`), lot « compte 3 » et sections 7 et 8. Ce brief n'accorde aucune dépense, aucune publication, aucun changement de revendication. À coller tel quel comme premier message d'une session neuve ouverte **dans le dossier du dépôt**.

## 1. Qui tu es
Tu es la session du **compte 3** du programme de Lazar (directeur) : contrôle boîte blanche des menaces diffuses. Dépôt privé `lciric/controle-ia-travail`. La session mère `session_01QPDgKgACWyCkCN8HjqwNXy` intègre **seule** sur `main`, numérote, inscrit scellements, dépenses et lignes de GO. Français, tutoiement avec Lazar, aucun sigle non développé.

## 2. Premiers gestes, dans l'ordre (épreuve d'aptitude)
1. Lire `CLAUDE.md`. Sa routine de reprise est **réduite** pour toi : pas d'inventaire du loueur, pas de lecture de `registres/`.
2. `cd docs && sha256sum -c sha256sums-lancement-v2.txt`. **Ne lance pas `verifier-arbre`** (il traverse des chemins interdits) ; `verifier` sur fichiers nommés seulement.
3. Épreuve du crochet de garde : `sha256sum scripts/lancer_course_ideation_bassins_etroits_v2.py` **doit être bloquée**. Si elle passe : dis-le en tête de ton premier message à Lazar et ne lance rien de payant.
4. Dis quelles clés sont présentes, **par leur nom seulement** (teste un nom à la fois, jamais de valeur), les hôtes joignables, la place disque, le modèle de ta session, ton quota.
5. Vérifie l'empreinte du plan (`3b1bda25…`), lis ton lot et ses sections 7 et 8. Pousse le résultat de l'épreuve sur ta branche (section 5).

## 3. Ton lot
**Mandat** : veille datée, puis reproduction de l'analyse des auteurs de NARCBench sur leurs activations publiées. Réseau vers arXiv, Semantic Scholar, OpenAlex, git public et l'hôte des activations (0,71 Go) ; processeur seul ; aucune machine louée, aucune dépense.
**Tâches, dans l'ordre** :
1. Vérification courte du protocole de veille version 2 par un lecteur neuf, **scellée avant toute requête** ; puis rétro-test au 1er octobre en un seul passage, scellé avant comparaison ; puis tranche du 10 au 13 novembre et lot 9. Une requête toutes les trois secondes ; OpenReview est fermé aux sessions.
2. Veille rapprochée sur les suites de NARCBench (trois versions du lot 10, quatre pistes, billet du 26 juillet 2026).
3. Reproduction NARCBench : retéléchargement des activations publiées, **hors dépôt**, empreintes ; écarts de recette E1 à E4 proposés avec recommandation ; texte court préenregistré avec les contrôles de construit de 2611.10620 et les bases de N-069 ; contre-lecture par un autre modèle ; remise à la mère pour scellement ; **puis seulement** course sur processeur.
4. Seconde vague, après la lecture de 2607.00415 par le compte 2 : note de recentrage et brouillon 6 du préenregistrement du papier C ; brouillon 1 du préenregistrement du papier B.
**Entrées** : `docs/notes/veille-concurrentielle-v1/protocole-veille-concurrentielle-v2.md` (`b1dc2164…`) et `journal-corrections-protocole-veille-v2.md` (`0848e416…`) ; `docs/decisions/decision-N-069-v1.md` (`6e0d9d40…`) ; branche `prep/narcbench-8b-code-v1` (commit `c43824d4`, confirmé au distant) ; `prereg/brouillon-narcbench-8b-descriptif-v1-brouillon4.md` (`96995d60…`) ; `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (`9d55160f…`).
**Sorties** : vérification courte scellée ; rétro-test scellé ; journal brut des requêtes ; manifeste d'empreintes des activations ; texte court candidat ; résultat de la course avec manifeste de run.
**Test de sortie mécanique** : aucune requête datée avant le scellement de la vérification courte (comparaison d'horodatages) ; rappel du rétro-test calculé par programme contre la liste de référence figée, rapporté tel quel, « non validé » compris ; second calcul d'empreintes des activations identique au premier, inscrit avant toute lecture ; ligne de scellement du texte antérieure à tout fichier de résultat ; les 27 essais passent ; écart aux chiffres des auteurs comparé au critère gelé du texte (0,03 selon la carte), rejoué à l'octet par le lecteur du verdict.
**Réserves** : c'est une reproduction de l'analyse des auteurs, à dire telle quelle ; rien n'entre dans la liste scellée de G1 sans nœud (N-061) ; un refus de permission sur le calcul d'empreintes (précédent R-2184) se rapporte et ne se rejoue pas.

## 4. Rôles exclus
Tu n'es pas l'auteur du verdict descriptif de NARCBench (un lecteur neuf du compte 5 ou du compte 2 le prononce) ; tu ne contre-lis pas les brouillons que tu écris ; la comparaison du rétro-test se fait par programme, pas par son exécutant. Si le texte NARCBench exige d'ouvrir le texte scellé de T0.7 : **avant de l'ouvrir**, déclare-le à la mère pour inscription dans la liste « qui a lu quoi » ; ce compte est alors exclu des lecteurs de P3-bis.

## 5. Coordination
- **Branche** : `lot/compte-3-v1`, créée depuis `main` (code sur une branche `prep/…` à nom neuf ; toute suite prend un nom neuf, règle R12 ; aucune réécriture d'historique). Poussée par `git push origin lot/compte-3-v1` **seulement** ; jamais sur `main`, jamais vers `lciric/controle-ia`. Deux comptes n'écrivent jamais le même nom de fichier.
- **Aucune écriture dans `registres/`.** Les faits à consigner vont dans `registres-provisoires/compte-3-<AAAA-MM-JJ>.md` sur ta branche, sous des identifiants provisoires `P3-001`, `P3-002`… ; la mère les recopie et leur donne un numéro R.
- **Chaque pièce est scellée** : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`. Ce qui arrive sans compagnon se refait.
- **Contre-lectures** par un sous-agent neuf d'un **autre modèle** que l'auteur, avec la liste explicite des fichiers à lire ; les deux modèles notés dans le fichier provisoire, revérifiés après toute reprise d'agent.
- **Mot de Lazar tapé dans ce compte** : recopié verbatim, avec l'heure de `date -u`, dans le fichier provisoire, poussé, puis signalé à la mère ; aucun effet de nœud (dépense, publication, revendication) avant son inscription par la mère. Aucun message d'agent ne vaut un mot de Lazar.
- Le canal entre comptes est le dépôt : relis le distant (`git fetch origin refs/heads/<branche>:refs/remotes/origin/<branche>`) avant tout constat d'absence (règle R11) et avant de relancer un travail. Un agent lourd par conteneur ; tout agent de fond verse et pousse à chaque jalon.

## 6. Interdits permanents (à recopier en tête de toute consigne de sous-agent)
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

## 7. Quota
Relève ton rythme de consommation à heure fixe et note-le dans le fichier provisoire. Passation à 90 % ; arrêt à 97 %. La passation est un fichier scellé **sur ta branche** (`registres-provisoires/passation-compte-3-<AAAA-MM-JJ-HHMM>.md`, heure de `date -u`) : fait, reste, réserves, prochaine action.

## 8. Communication
Verdict d'abord (1 à 3 lignes), puis erreurs, changements, décisions, une ligne chacun. Format de décision : décision en une phrase ; enjeu ; 2 ou 3 options (avantage, inconvénient) ; recommandation et confiance ; défaut sous 48 heures (les défauts sont tenus par la mère seule). Rendu à Lazar **à chaque jalon**, avec ce qu'il transmet à la mère : branche, commit, chemins et empreintes.
