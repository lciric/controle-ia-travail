Voici les réponses factuelles exactes aux deux questions pour inscription dans `registres/qui-a-lu-quoi*`.

1. Indépendance effective du contre-lecteur R2 (`contre-lecteur-r2-architecture-etages-1-2-temporaire-20261126-01`)
A. Mémoire inter-conversations et isolement de plateforme (réserve à consigner)

* Fil de discussion, Gem et mémoire explicite : la conversation était un fil neuf (aucun historique joint en amont), sans Gem personnalisé partagé, et la mémoire explicite enregistrée (`Explicit Memory`) du compte était vide.
* Mémoire automatique du compte Gemini Web (`Contexte personnel`) — OUI, active passivement : la session n'a pas tourné dans un conteneur API vierge ni en navigation éphémère hors-historique, mais comme conversation standard sur le compte Gemini Web de Lazar (preuve matérielle : ses 13 tours ont eux-mêmes été indexés dans la mémoire des conversations du compte). Or, sur cette interface, tout nouveau fil standard reçoit automatiquement dans son contexte système :
   1. `Long Term Memory` (profil général du compte mentionnant le programme `controle-ia-travail` et ses outils statistiques) ;
   2. `Short Term Memory` (résumés automatiques concis des conversations Gemini immédiatement précédentes du même compte — donc potentiellement un résumé de haut niveau des échanges de conception des 26–27 novembre sur la Proposition 2 ou l'itération `v3.2 -> v3.3`) ;
   3. la déclaration d'outil `personal_context:retrieve_personal_data`.
* Qualification exacte pour `R2` / `R13` et `P8` : zéro fuite `P8` (aucun `.npz`, aucun score/poids/plancher de sonde non scellé ni aucune consigne privée n'ayant jamais été ouvert dans Gemini Web), mais indépendance cognitive partielle seulement vis-à-vis des auteurs Gemini Web précédents (même modèle `Gemini 3.1 Pro Preview` + exposition passive possible à `Short Term Memory`).

B. Ce qui lui a été montré au-delà des 3 pièces d'entrée et de `verif-p8-hors-depot.txt`
Il faut distinguer strictement les Volets 1 à 10 des Volets 11 à 13 :

* Volets 1 à 10 (`contre-lecture-r2-etages-1-2-v1.md`, `8325ba1c…`) — RIEN d'autre du dépôt : le lecteur n'a reçu aucun autre fichier ni extrait du dépôt que `gemini-code-1795778660659.md`, `kit-r2-lot1-slim.txt` et `kit-r2-lot2-slim.txt`, accompagnés uniquement des consignes de découpage séquentiel en 10 volets pour éviter la troncature de sortie.
* Volets 11 à 13 (`contre-epreuve-r2-volets-11-13-v1.md`, `8547ee1c…`) — OUI, prompts directifs de la session mère précédente : en plus de `verif-p8-hors-depot.txt`, l'utilisateur lui a transmis dans les prompts des Volets 11 à 13 :
   1. l'énoncé structuré des questions mathématiques `Q-Math-1` à `Q-Math-4` (auto-effacement de `LEACE` sur $\hat{h}^{\max}$, queue de Gumbel dans $S_{\text{e-mix}}$, TSQR augmentée en `float16`/`float64`, reprises d'épisode et isolation Windows/Linux) ;
   2. l'énoncé de `Q-Math-5` (`C-4-bis`) signalant explicitement le blocage `PREDICTION:` après `COST:` et `CHAMPS_EXIGES` autour de `REVISE` dans `propositions.py`, ainsi que la formulation des options de gouvernance `GO-1` (`GO-1A`/`GO-1B`), `GO-2` (`GO-2A`/`GO-2B`) et `GO-3` (`3A-intra` vs `3A-amont`) à chiffrer ;
   3. au Volet 13, la demande d'écrire `test_contre_epreuve_v4_r5.py`, suivie du retour d'erreur Git Bash (`NameError` sur `sys`) ayant conduit à l'ajout de `import sys`.

(Conséquence pour le registre : les Volets 11–13 relèvent d'une contre-épreuve dirigée / co-conception post-R2, et non d'une contre-lecture aveugle d'un texte fini.)
2. Sessions Antigravity (`cd7c89b9-9752-4dac-b846-2c58efd89737`, 25–28 novembre) et lignes de registres non poussées

* Réponse directe sur les 4 registres visés : Non, à l'issue de l'audit des 8 arbres de travail effectué le `2026-11-28`, aucune ligne non poussée n'existait dans `registres/go.md`, `registres/decisions.md`, `registres/etat.md` ni `registres/qui-a-lu-quoi*` :
   * Les écritures réalisées par Antigravity entre le 25 et le 28 novembre dans `registres/go.md`, `registres/decisions.md` et `registres/arrets.md` (ainsi que dans `registres/dose-reponse-v1.md` sur `lecture-dr` et `registres/sondes-iib-v1.md` sur `wt-b8-puissance`) avaient toutes été commises et poussées sur GitHub sur leurs branches respectives.
   * Aucune modification locale non poussée n'avait été portée à `registres/etat.md` ni à `registres/qui-a-lu-quoi*`.
* État détaillé des 8 arbres de travail relevé le `2026-11-28` :
   * 7 worktrees sous `C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\` — `lecture-dr`, `wt-b8-code-v5`, `wt-b8-exec-v5`, `wt-b8-puissance`, `wt-dr-v3`, `wt-lancement-dr-v2` et `wt-vh-etape0` : zéro modification suivie non commise (`git status` propre face à `origin`).
   * 8e arbre (`C:\Users\lciri\OneDrive\Documents\controle-ia-travail`, dépôt principal) : les 8 seules modifications suivies non commises étaient des suppressions locales dues au `sparse-checkout` portant exclusivement sur `docs/notes/` (zéro fichier sous `registres/`), à savoir :
      * `docs/notes/papier-c-banc-de-juge-v1/mandat-fable-papier-c-banc-de-juge-v1.md` (+ `.sha256`) ;
      * `docs/notes/papier-c-banc-de-juge-v1/quatre-points-et-demande-reformulee-v1.md` (+ `.sha256`) ;
      * `docs/notes/plan-entretien-2026-12-01-v1/plan-courses-echecs-et-semaine-avant-entretien-v1.md` (+ `.sha256`) ;
      * `docs/notes/plan-entretien-2026-12-01-v1/plan-courses-echecs-et-semaine-avant-entretien-v1.pdf` (+ `.sha256`).
* Vérification mécanique résiduelle conseillée à la session locale : cet état provenant de la trace d'inspection enregistrée plus tôt le `2026-11-28` et non d'une lecture disque en direct, un `git status --porcelain -- registres/` et `git log --branches --not --remotes -- registres/` sur les deux clones (`OneDrive\Documents\controle-ia-travail` + ses 7 worktrees `scratch`, et `C:\Users\lciri\controle-ia-travail`) permettra de certifier sur pièce qu'aucun agent local n'y a écrit dans l'intervalle.
