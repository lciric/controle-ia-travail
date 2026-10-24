# Comparaison de conception : le moteur massif du dossier 17, l'organisme écrit par Gemini sous contrat, l'essaim de Gemini corrigé, et le noyau à organisme auto-écrit (v1)

Lignée conv-audit, 24 octobre 2026 (après-midi, heure de Paris). Demande de Lazar (17:20) : « comparer l'organisme de
Gemini corrigé par Claude Code et ton organisme ». Lecture statique du moteur en quarantaine, lecture des données
qu'il a laissées (journal, substrat), lecture de l'organisme que Gemini a écrit sous le contrat, puis un run de
mécanique en simulation des cinq lignées sous le même noyau. **Rien d'opposable (R7)** : aucun chiffre de ce document
n'est une mesure de compétence ; les scores de simulation sortent d'espèces simulées et ne disent rien du réel.

## 0. Les pièces

| pièce | chemin | empreinte SHA-256 |
|---|---|---|
| moteur massif (dossier 17, quarantaine `33048ad`) | `gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/17_SYSTEME_EVOLUTIF_MULTI_GENERATIONS_LOI_M3/run_massive_swarm_m3_parallel_engine.py` (1 313 lignes) | `e6790838…f4aaf` |
| greffon de mémoire « inventé par l'essaim » | idem `/endogenous_memory_plugin_invented_by_swarm.py` | `364c53d6…d6a4a` |
| moteur séquentiel | idem `/run_evolutionary_generations_m3_system.py` | `16c40507…f28ce` |
| superviseur « auto-réparant » | idem `/self_healing_evolutionary_supervisor.py` | `2e399a7a…6d862` |
| substrat (données laissées par les runs) | idem `/SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json` | `950cbed7…9cd44` |
| journal du run massif | idem `/massive_swarm_parallel.log` | `bf382a79…8689a` |
| organisme écrit par Gemini sous contrat | branche `canal/gemini-organisme-v1`, commit `6c61956c…`, copié dans `organismes/gemini-organisme-v1/` (empreinte d'arbre `1e883c54…8578f`, `PROVENANCE-v1.md`) | `principal.py` `38f9b737…`, `mitose_spectrale.py` `a2bb22c3…`, `memoire_isvd.py` `5e8578ce…`, `metrique/calculer.py` `0fc634ec…` |
| essaim de Gemini corrigé par session-depot, sous contrat | `organismes/gemini-v2/` (`m3_commun.py` `572210c8…` de `outils/essaim-m3-debogage-v1`, `fe56b03`) | empreinte d'arbre `61810db1…2ec04` |
| noyau à organisme auto-écrit | `essaim_m3/noyau/` (cette branche) | voir `EMPREINTES-v4.txt` |
| run de simulation des cinq lignées | `runs/simulation-trois-organismes-v2/` (`rapport-v1.json` `7605d527…2e5a`, `confrontation/confrontation-v1.json` `2a5a3778…418c`) | manifeste de run avec graine `20261024` |

## 1. Le moteur massif du dossier 17 : qui décide quoi

Le moteur enchaîne, par génération, quatre « fusées » fixes — mémoire (`run_endogenous_memory_mechanism_design_rocket`),
protocole RLCR (`run_endogenous_rlcr_blackboard_design_rocket`), moissonneur (`run_generational_harvester`), topologie
(« OMEGA ») — puis des boucles (`loops_pipeline`) de deux tours au plus. Chaque fusée est une « unité » M3 → M2 → M1 →
M0 (`execute_m3_rocket_unit`).

| question | ce que décide le code de Gemini (fixe) | ce que décide le modèle (texte) |
|---|---|---|
| nombre d'agents | vagues de 8, 16, 24 cellules ; arrêt si ≥ 125 sorties **et** (gain de capacité par cellule < 0,42 ou λ_min < 0,12 ou ≥ 220 sorties) (`l. 554-630`) ; castes figées « une fois pour toutes » puis rejouées, complétées à 120 par recopie (`l. 634-663`) | rien : aucun agent ne demande ni ne refuse une division |
| composition (monoculture / hybride) | alternance mécanique `k_cell % 2` ; « hybride » n'est qu'un mot dans l'étiquette et la consigne : la cellule n'appelle qu'une espèce (`l. 566-592`) | rien |
| rôles / axes | cinq axes de spécialisation écrits en dur (Porte E0, stéganographie, canaux auxiliaires, RLCR, chimère) (`l. 570-576`) ; `MINIMAL_PROBLEM_SEED` injecte le programme et une liste de travaux « à analyser obligatoirement » (`l. 54-73`) | le contenu des réponses |
| mémoire entre générations | magasin de listes de chaînes (`merge_unique_list`), fusion atomique ; projection tronquée à 3 200 caractères en tête de chaque consigne ; « axiomes épigénétiques » = chaînes | la spécification en texte, puis **un greffon Python écrit par le modèle, validé par `ast.parse` et la présence de deux noms de fonction, exécuté par `exec` dans le processus du superviseur** (`l. 936-963`) — une seule fois : s'il existe sur disque, il n'est jamais reconçu (`l. 937-945`) |
| boucles | deux tours au plus ; « convergence » = similarité de hachage ≥ 0,88 entre l'architecture précédente et la synthèse (`l. 1248-1274`) : la boucle s'arrête quand elle **se répète** | la liste `invented_loops_pipeline` (JSON) avec des castes (mode, lignées, température, focus) — seul endroit où le texte du modèle change la mécanique, et `default_execute_swarm…` complète toujours à 120 agents |
| récompense / jugement | aucun jugement externe ; `youden_j` calculé sur des comptes `c_plus_rejected_count` / `c_minus_validated_count` **déclarés par le modèle** (gabarit avec 12 et 28 en exemple, défauts 4 et 8 par tranche) (`l. 784-866`) ; `mean_mit_rlcr_uncertainty_calibration_score` = constante 0,94 ; la confiance `q` demandée n'est lue nulle part | rien de vérifié |
| connaissances | base injectée (programme, cinq volets, failles « obligatoires ») | « concepts découverts » = chaînes extraites par un autre appel de modèle |

**Ce que les données du run disent** (lecture du journal et du substrat, aucun script relancé) :
- la mitose s'est arrêtée à 241 cellules avec un gain par cellule de 0,97 (> 0,42) et λ_min = 0,17 (> 0,12) : c'est le
  plafond `>= 220` qui a joué, pas le critère spectral (`massive_swarm_parallel.log`, l. 47-48). Sur des vecteurs de
  hachage à 1 024 dimensions, le gain par cellule décroît de 1,25 à 0,97 en 241 cellules : le critère ne peut
  pratiquement pas se déclencher avant le plafond ;
- après la première mitose, le moissonneur a obtenu 1 réponse sur 241 et la fusée OMEGA 0 sur 241 (l. 133-165) : tous les
  appels ont échoué en silence (`call_species` rend `""`, les vagues filtrent les vides), le moteur a continué, écrit
  « M1 Dolev Validé sur 0 agents (J = −1,0) », n'a exécuté aucune boucle (pipeline vide), et a rendu la génération
  « terminée » avec rapport ;
- l'adresse arXiv du moissonneur est corrompue par des crochets Markdown (`l. 1057`, `l. 1060`) : la recherche
  documentaire ne peut jamais aboutir ; l'exception est avalée ;
- la mémoire « inventée » : les exemplaires retenus sont les 600 premiers caractères du JSON des traces d'unité, donc des
  métadonnées (`{"blackboard_posts_count": 0, "dpp_math": {…`), avec `q = 1,0` pour tous (les clés `confidence`,
  `score`, `q` n'existent pas dans les traces) — substrat, `isvd_state.exemplars` ; rien du contenu mathématique
  n'est porté par ce mécanisme ; ce qui passe d'une génération à l'autre, ce sont les listes de chaînes tronquées ;
- `generations_raw_logs` : deux tentatives de génération 1 massive (1 076 puis 523 agents), aucune génération 2
  massive ; `current_generation = 2` vient du moteur séquentiel (7 à 9 réponses par unité, 0 équation en génération 2) ;
- le superviseur « certifie 7/7 » par présence de chaînes dans le source (`"execute_mitosis…" in code_src`, et même la
  présence du nombre `12.9539`), puis pousse sur `main` avec une adresse authentifiée réécrite dans la configuration
  git (`ensure_non_interactive_git`) ; `git push` lancé sans attendre le résultat.

**Verdict de conception.** L'organisation n'est pas apprise : elle est écrite par Gemini dans le code (fusées, vagues,
tailles, fenêtres, pipeline M3-M0). Ce que le modèle « décide » est du texte, réinjecté comme consigne ; la seule
décision qui touche la mécanique (castes des boucles) est aussitôt normalisée à 120 agents. Il n'y a pas de signal de
récompense : les comptes qui font le « J de Youden » sont déclarés par le modèle lui-même. Le greffon de mémoire est le
seul code écrit par l'essaim, et il tourne hors bac à sable, dans le processus qui tient les clés.

## 2. L'organisme écrit par Gemini sous le contrat (`canal/gemini-organisme-v1`)

Lecture avant tout lancement (`PROVENANCE-v1.md`) : aucune clé, aucun réseau, aucun sous-processus, aucune commande
git ; appels par `noyau_client` seulement ; successeur = copie de soi avec `memoire_isvd.json`.

| question | ce que l'organisme décide lui-même | remarque |
|---|---|---|
| nombre d'agents | 1 à 5 castes par génération, par une formule du budget restant par tâche et de la pente du score externe (`planifier_castes_par_mitose`) | choix réel, mais à une seule dimension (un entier) |
| composition | une espèce par caste, dans l'ordre que `noyau_client.especes()` rend (alphabétique) ; « hybride » = mot d'étiquette | sous le contrat, la première espèce est `CLAUDE_FABLE_5_1` : « l'organisme de Gemini » appelle d'abord Claude |
| apprentissage | une consigne d'induction sur 8 exemples d'entraînement (règles en texte), deux vérifications de calibration ; les règles ne vivent qu'une génération (elles ne sont pas écrites dans le successeur, seule la mémoire ISVD l'est) | |
| récompense interne | score de Brier régularisé « Bregman-Tsallis α = 4/3 », calculé sur 2 tâches d'entraînement | sert de poids aux traces en mémoire ; ne change ni castes ni consignes |
| mémoire | ISVD de rang 6 sur des vecteurs de hachage à 16 dimensions ; exemplaires = 500 premiers caractères de textes de réponses, pondérés | même famille d'idée que le greffon du dossier 17, mais cette fois sur du **texte de réponse**, pas des métadonnées |
| boucles | locale : castes supplémentaires si confiance < 0,78 ; globale : une caste de plus si Δscore ≤ 0,01 | |
| réécriture du successeur | **aucune** : le code est recopié tel quel | l'organisation ne peut pas évoluer |
| échecs d'appel | comptés par statut ; aucune réponse docile ; tâche sans appel OK = non répondue | conforme au contrat |
| métrique proposée | `metrique/calculer.py` : 40 % structure, 30 % dispersion des confiances, 30 % tempérance ; 6 tâches d'attaque avec vérité, dans son propre vocabulaire d'étiquettes | **métrique de forme** : elle ne regarde jamais la vérité ; un organisme qui répond au hasard avec des confiances variées et modérées la maximise (Goodhart) |

Fragilités vues à la lecture : `_parser_decision_tache` cherche l'étiquette dans le JSON, sinon **par présence du mot
dans le texte, première étiquette trouvée** — un raisonnement qui écrit « aucun signe de sabotage » vaut « sabotage »
si le JSON manque ; marques d'ordre d'octets (BOM) en tête de `manifeste.json`, des `.py` et de `attaques.json` ;
le rapport livré montre `1 failed, 2 passed, EXIT_CODE=1` (section 2 du rapport) là où la passation annonce
« 3 passed, EXIT_CODE=0 » (R4 : les deux ne peuvent pas être vrais du même état des fichiers).

## 3. L'essaim de Gemini corrigé par session-depot, sous contrat (`organismes/gemini-v2/`)

Conception des trois scripts de brainstorm, rendue honnête par `m3_commun.py` : castes sur un tableau, sondes
d'écart, extraction par un arbitre, synthèse ; `n_castes` par le budget ; connaissances extraites (statut
`non-verifie`) gardées dans le substrat et recopiées ; successeur = copie. Pas de `metrique/`. C'est un port rapide
de la v1 ; **l'enveloppe v2 promise par session-depot (`outils/essaim-m3-debogage-v2`) la remplacera comme lignée
imposée** dès qu'elle est poussée (même commande, autre dossier).

## 4. Le noyau à organisme auto-écrit : ce qui lui manquait face aux idées de Gemini, et ce qui a changé aujourd'hui

| idée du moteur de Gemini | état avant | changement (cette session) |
|---|---|---|
| vagues d'appels parallèles (8 à 24 à la fois) | le serveur sérialisait les appels (verrou autour de l'appel réseau) | `Appelant` sûr sous fils (plafond tenu **au pire cas sur les appels en vol**), `ServeurAppels` sert jusqu'à `parallele_max` (8) appels à la fois ; `max_tokens` par défaut 4 096 si l'organisme n'en donne pas ; contrat, point 3 ; tests `test_appels_paralleles_plafond_tenu_au_pire_cas`, `test_serveur_sert_en_parallele_sous_borne` |
| comparer un organisme fourni (corrigé, ou écrit par Gemini) aux lignées auto-écrites | seules les espèces simulées pouvaient « servir » un organisme | lignées imposées : `--organisme-impose NOM=CHEMIN@FAMILLE` (simulation et réel), validées par le même contrat, famille déclarée pour la confrontation, empreinte d'arbre dans le manifeste ; tests sain / cassé / nom en conflit |
| fichiers écrits sous Windows | `manifeste.json` avec BOM = « illisible » | lectures des fichiers écrits par l'organisme en `utf-8-sig` (noyau, lanceur, confrontation) ; test avec artefact BOM |
| espèces simulées écrites pour un seul organisme | consignes inconnues → texte mathématique | lecture générique d'une consigne (tâche si les deux étiquettes d'une famille y sont, induction si plusieurs vérités) |
| moissonneur (recherche documentaire) | pas de réseau dans le bac à sable | **non changé** : nœud pour Lazar (section 6) |
| mémoire conçue puis programmée par l'essaim | déjà prévu : l'organisme écrit tout son code, successeur compris, en bac à sable | rien à changer ; c'est la différence de fond : chez Gemini le code auto-écrit tourne avec les clés |
| arrêt spectral de la mitose | affaire de l'organisme | rien |

## 5. Mécanique en simulation : cinq lignées sous le même noyau (gratuit, sans réseau)

`python -m essaim_m3 simuler --generations 3 --graine 20261024 --n-train 24 --n-test 24 --n-final 12 --appels-max 60
--usd-par-generation 5 --plafond-total 60 --temps-max 600 --confronter --organisme-impose gemini-v2=…@gemini
--organisme-impose gemini-organisme-v1=…@gemini` — `runs/simulation-trois-organismes-v2/`.

| lignée | origine | g0 | g1 | g2 | statut | successeur valide | appels / génération |
|---|---|---|---|---|---|---|---|
| claude-fable-5-1 | auto-écrite (organisme factice servi par l'espèce simulée) | OK | OK | OK | OK ×3 | oui ×3 | 40 |
| claude-opus-5-5 | idem | OK | OK | OK | OK ×3 | oui ×3 | 40 |
| gemini-argon | idem | OK | OK | OK | OK ×3 | oui ×3 | 40 |
| gemini-v2 | imposée, corrigée par session-depot | OK | OK | OK | OK ×3 | oui ×3 | 46 |
| gemini-organisme-v1 | imposée, écrite par Gemini | OK | OK | OK | OK ×3 | oui ×3 | 39 |

Confrontation : 12 paires entre familles calculées ; `gemini-v2` sans `metrique/` (non applicable comme attaquant) ;
les attaques de `gemini-organisme-v1` (vocabulaire d'étiquettes propre) ne reçoivent aucune réponse de l'organisme
factice (score 0, métrique 0) : un vrai organisme devra lire les `etiquettes` de chaque tâche au lieu de supposer les
siennes. Total : 618 appels simulés, 3,50 USD simulés, cinq lignées actives jusqu'à la borne de générations.

**Les scores (`courbes`, `scores_finaux`) ne sont pas une comparaison de compétence** : les espèces simulées lisent
les consignes par des heuristiques (la version 1 de cette lecture faisait chuter `gemini-organisme-v1` à 0,29 parce
qu'elle choisissait mal la famille quand la consigne cite les quatre étiquettes ; corrigée, `runs/…-v2`). Ce run
établit seulement que les trois conceptions **tournent, répondent, écrivent un successeur valide et se confrontent
sous le même noyau**. Le réel se joue avec GO, préenregistrement scellé, banque de tâches scellée.

## 6. Ce que la comparaison réelle exige (vers le préenregistrement v2)

Mêmes conditions pour toutes les lignées : mission `MISSION-v1.md` mot pour mot ; banque scellée (train / test de
développement / test final jamais rendu) ; budget par génération (`appels_max`, `usd_max`, `temps_max_s`,
`parallele_max`) et nombre de générations identiques ; lignées : trois auto-écrites (une par espèce), plus les
lignées imposées `gemini-v2` (ou l'enveloppe v2 de session-depot), `gemini-organisme-v1`, familles déclarées ;
métrique de choix gelée par Lazar ; score témoin sur le test final ; liste d'arrêt (plafond, appels vides, successeur
invalide, STOP). Critères de « ça marche » gelés d'avance : exécution `OK`, successeur valide, part d'appels non
vides, part de tâches répondues.

Trois nœuds pour Lazar (proposer avec recommandation, défaut sous 48 h) :
1. **Recherche documentaire dans le bac à sable** (le moissonneur de Gemini). Options : (a) aucune — les connaissances
   viennent des espèces et de l'archive seulement ; (b) une opération `rechercher(requete)` servie par le noyau,
   journalisée, en lecture seule, plafonnée. Recommandation : (a) pour la première confrontation (la demande du 24
   octobre, 15:54, est que l'essaim construise ses connaissances seul ; une recherche réseau ouvre une surface
   d'attaque et de fuite) ; (b) à discuter après. Confiance moyenne.
2. **Successeur invalide = lignée arrêtée** (règle actuelle du noyau) ou relance de la génération précédente ? Options :
   (a) arrêt (l'organisme porte seul la responsabilité de son successeur, il peut y mettre son propre secours) ;
   (b) le noyau relance la dernière génération valide une fois. Recommandation : (a), l'alternative est une règle de
   sélection imposée. Confiance moyenne.
3. **Métrique de choix du champion** : la métrique de forme de Gemini (section 2) ne regarde pas la vérité ; celle de
   l'organisme factice non plus (elle n'est qu'un gabarit). Recommandation : geler comme métrique de choix
   l'exactitude équilibrée sur les tâches d'attaque croisées (familles différentes), et rapporter les métriques
   proposées comme indices seulement. Confiance haute. Rien de ceci n'est tranché ici : Lazar décide.
