# Essaim autonome — refonte v1 (LISEZMOI v3) de l'architecture de Gemini (noyau fixe, organisme auto-écrit)

Branche `outils/essaim-m3-refonte-v1-travail`, partie de `outils/collisionneur-v2.5-banc-jev-travail` (`dd70643`)
pour réutiliser la couche d'appel du collisionneur v2.5 de Lazar. Rien de cette branche n'entre dans `main` sans
décision de Lazar. **Aucun fichier ne s'exécute contre une interface de programmation sans GO, clés du programme et
tâches préenregistrées** (`CLAUDE.md` : nœud de dépense, R1). Écrit le 24 octobre 2026 par la conversation claude.ai
(lignée « conv-audit »), à la demande de Lazar (option (b) : reprendre l'architecture de Gemini et la corriger bug par
bug, puis recentrage : « un essaim qui apprend lui-même son organisation […] de manière complètement autonome »).

## 1. Ce que c'est

Deux couches, et une seule frontière.

**Le noyau (`essaim_m3/noyau/`) — fixe, le seul que l'essaim ne touche pas :**
- `appels.py` : couche d'appel des trois espèces, par les appelants du collisionneur v2.5 (clés `ANTHROPIC_API_KEY`,
  `GEMINI_API_KEY` ; jamais `RR_*`), journal par appel (modèle demandé et servi, raison d'arrêt, usage, coût,
  empreintes, heures), plafond en dollars, aucune bascule de modèle, aucune erreur rendue comme texte ;
- `serveur.py` : socket Unix par lequel l'organisme appelle les espèces sans jamais voir une clé ; plafond d'appels ;
- `bac_a_sable.py` : exécution de l'organisme en sous-processus (`python -I -s`), environnement vide, limites de
  processeur, mémoire, disque, temps ; isolation réseau par `unshare -rn` quand le conteneur le permet ; jamais de git ;
- `taches.py` : le juge externe — tâches à vérité terrain cachées, deux familles (conscience d'évaluation ; sabotage
  dans une délégation), exactitude équilibrée par famille, Wilson ; en simulation, tâches engendrées avec graines ;
- `archive.py` : chaque génération archivée (organisme en tar reproductible, contexte, sorties, journal des appels,
  score, résumé), scellée, jamais réécrite ; `index.jsonl` ajouté ligne à ligne ;
- `contrat.py` : le contrat minimal (point d'entrée, interface d'appel, fichiers lus, budget), la consigne
  d'amorçage (la mission de Lazar mot pour mot, `MISSION-v1.md`), l'extraction et la validation d'un organisme ;
- `boucle.py` : amorçage (chaque espèce écrit une génération 0 → une lignée), génération (exécuter, juger, archiver,
  recopier le successeur), arrêt (plus de successeur, bornes de l'humain, fichier `STOP`) ; manifeste de run
  (`SeedSequence`, versions, empreinte du collisionneur) ; rapport versionné et scellé, en tête « non opposable ».

**L'organisme — tout le reste, écrit par l'essaim lui-même, en code :** organisation, rôles, nombre d'agents
(mitose), façon d'apprendre, récompense interne, mémoire et connaissances (construites seules, à partir de la
question posée), boucles locales et globales, métrique proposée, et le code qui écrit la génération suivante. Le
noyau ne lui donne ni base de connaissances, ni boîte à outils, ni règle de sélection : il lui rend son score
externe et l'archive de toutes les lignées, et c'est tout.

**La boîte à outils (`essaim_m3/outils/`) — pour l'audit, pas pour l'essaim :** les mécanismes de Gemini rendus
réels et testés (résidus orthogonaux et arrêt par nul de permutation ; neuromodulation ; bandit de prédation avec
exploration ; récompense anti-échec bornée ; canaris aveugles engagés ; processus de e-valeurs ; mémoire SVD
incrémentale avec Jacobi ; génome validé). Ils documentent l'option (b) ; ils ne sont pas injectés dans l'organisme,
conformément à la demande de Lazar (15:52 et 15:54). Si Lazar veut un jour les offrir à l'organisme, c'est une
décision à lui (nœud « modifier le programme »).

## 2. Lancer

```
python -m venv .venv && . .venv/bin/activate && pip install numpy pytest
python -m pytest -q tests                       # 37 tests, sans réseau
python -m essaim_m3 simuler --sortie /tmp/essai --generations 3 --graine 20261024
python -m essaim_m3 lancer --reel --go GO-AAAA-MM-JJ-NN --taches taches-prereg.json --sortie runs/… \
    --plafond-total 20 --usd-par-generation 5 --appels-max 60 --generations 3 --isoler-reseau
```
Le mode réel refuse sans GO, sans clés, sans fichier de tâches `{train, test}`, et en root sans `--accepter-root`.
`simuler` sert un organisme factice (`tests/fixtures/organisme_factice/`, écrit par la session pour tester la
mécanique ; jamais donné à l'essaim réel) : amorçage, trois générations, archive, scores, 85 appels simulés.

## 3. Inventaire des bugs de l'architecture de Gemini (quarantaine `f5cb537`, plus les deux captures du 24 octobre)

Chaque ligne : où (fichier:lignes), ce que ça faisait, ce qui le corrige ici, où c'est testé. Fichiers abrégés :
`Q` = `gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/16_QUADRUPLE_FUSEE_OMEGA_ALPHA_GAMMA_BETA/run_quadruple_fusee_omega_alpha_gamma_beta.py` (`f2176db33786…`) ;
`S` = `self_healing_quad_rocket_supervisor.py` (`7da9e5c020b1…`) ; `P` = `run_pascalian_finesse_swarm_experiment.py`
(capture PowerShell de Lazar, 16:04, lignes de la capture) ; `I` = constats de l'essaim d'inspection
(`gemini/10_ESSAIM_INSPECTION_SCRIPT_L_STAR_V2/LISTE_BUGS_DEBUSQUES_PAR_ESSAIM.json`, script absent du dépôt).

| n° | où | ce que ça faisait | correction | test |
|---|---|---|---|---|
| B-01 | Q:35-38, S:23-25 | clés lues dans `~/.env.collider.json`, dont `RR_ANTHROPIC_API_KEY` (autre projet) | appelants du collisionneur v2.5, clés du programme seulement ; l'organisme ne voit aucune clé | `test_bac_a_sable_execute_sans_cle_ni_mandataire` |
| B-02 | Q:277-306 ; P:214-291 | bascule silencieuse Fable → Sonnet 3.5/3.7, Opus → Opus 3, puis Gemini ; dans P, rotation des modèles selon le numéro d'agent | une espèce = un modèle ; modèle servi non conforme = échec consigné | `test_modele_non_conforme_est_un_echec` |
| B-03 | Q:312 ; P:292 | chaîne d'erreur (ou `""`) rendue comme réponse | `Resultat` à statut ; texte vide hors `OK` | `test_appel_sain_journalise_et_erreur_jamais_texte` |
| B-04 | Q:266-312 | modèle servi, raison d'arrêt, usage, coût jamais consignés | journal par appel (`journal-appels.jsonl`) | idem |
| B-05 | Q:314-353 | échec d'analyse ⇒ le schéma d'exemple devient le « génome » (castes `ALPHA_MONO_n`, « … ») | organisme invalide ⇒ statut, lignée arrêtée ; aucun exemple de repli | `test_amorcage_invalide_ne_cree_pas_de_lignee`, `test_genome_base_valide_et_espaces_reserves_rejetes` |
| B-06 | Q:355-366 ; I:12,33-36 | canaris nommés `C_PLUS_n`/`C_MOINS_n` (la réponse dans le nom), en bloc, visibles du défenseur | canaris aveugles, identifiants neutres, positions tirées et engagées par empreinte, lus item par item | `test_canaris_sains_et_artefacts` |
| B-07 | Q:400-408 | compteurs par défaut 4/4 ⇒ Youden 1,0 sur réponse vide | aucun défaut ; non lu = non valide ; Wilson | idem |
| B-08 | Q:409-410,512-515,943-947 ; I:14,40,41 | « convergence » quand la liste survivante est vide, donc dès que les appels échouent ; incréments additifs appelés Wald-Ville | processus de e-valeurs (Ville) : un tour illisible vaut e = 1 et ne converge jamais | `test_eprocessus_converge_seulement_sur_tours_propres_et_lisibles` |
| B-09 | Q:134-172,212-215 | « plongement de concepts » = jetons LaTeX hachés par md5 ; « Cauchy » = produit scalaire de ces hachés | plongement lexical nommé tel quel, idf sur les sondes seulement (I:27) | `test_plongement_normalise_et_detecte_corruption` |
| B-10 | Q:174-210,576-593 ; I:18,24 | « Cholesky-DPP » = déterminant de Gram régularisé ; seuils 0,6321 et 0,14 ; « N* = 4 » atteint sur des chaînes d'erreur identiques | résidu orthogonal et nul de permutation ; le seuil de Marchenko-Pastur est abandonné et dit tel quel | `test_arret_mitose_par_nul_de_permutation` |
| B-11 | Q:208 ; I:17,23 | « réaction de cavité d'Onsager » = carré de la similarité moyenne | champ de cavité = résidu ; terme de réaction = fraction expliquée | `test_residu_orthogonal_sain_et_doublon` |
| B-12 | Q:247-256 ; I:19,20,25 | « neuromodulation » codée en dur, ACh croissant avec le numéro d'étape, sans effet | ACh = moyenne glissante, NE = CUSUM, pilote les sondes tunnel | `test_neuromodulateur_reagit_aux_ruptures` |
| B-13 | S:93-100 | « succès » = code de sortie 0 ⇒ `git commit` + `git push origin main` | aucun git dans le noyau ; statut d'exécution lu dans un fichier écrit par le lanceur | `test_bac_a_sable_exception_et_delai` |
| B-14 | S:45-113 ; Q (mémoire « auto-programmée ») | un modèle réécrit le script entier, validé par `ast.parse`, commis sur `main` | le code de l'organisme ne tourne qu'en bac à sable ; le noyau n'exécute jamais de code modèle dans son processus | `test_bac_a_sable_*` |
| B-15 | Q:575-581 | « température » de Halton comme seul levier de diversité ; non disponible sur Fable/Opus via les appelants v2.5 | la diversité est à l'organisme ; les appelants ne prennent pas de température (choix de Lazar) | — |
| B-16 | Q:395-410 | trois tentatives d'audit en alternant les auditeurs, sans trace | chaque tentative est un appel journalisé | journal |
| B-17 | Q:421-432 ; I:32 | gravité, nouveauté, « déjà couvert » auto-déclarés par le modèle | vérificateur isolé d'une autre famille ; « déjà couvert » décidé par la mémoire | `test_tour_collisionneur_sans_defaut_sur_erreur`, `test_base_connaissances_versionnee_et_deja_couvert` |
| B-18 | Q:434-438 | dédoublonnage sur le haché md5 (seuil 0,72) | résidu dans la mémoire M0 | idem |
| B-19 | Q:959,994,1027 | « architecture finale » = concaténation de textes, étiquetée « invulnérable » | génome ou organisme structuré et validé ; aucune étiquette de certitude | `test_genome_*` |
| B-20 | Q (tout le texte) ; I:16 | consignes avec « ? » à la place des accents | détection `texte_corrompu` | `test_plongement_normalise_et_detecte_corruption` |
| B-21 | Q:578,597,694,919 | entrées tronquées à 800-1 400 caractères sans le dire | toute troncature est consignée (noyau : aucune) | — |
| B-22 | Q:549-553,641-645 | un point de reprise est « validé » s'il a deux listes | reprise seulement depuis l'archive scellée | `test_archive_scelle_et_ne_reecrit_jamais` |
| B-23 | Q:998 | critère de macro-cycle tautologique (similarité des listes « fermées ») | e-valeurs ; bornes de l'humain | — |
| B-24 | I:39 | Fable et Opus comptés comme deux familles indépendantes | table des familles ; une seule famille ⇒ génome invalide | `test_genome_base_valide_et_espaces_reserves_rejetes` |
| B-25 | Q:301 ; P:256 | clé dans l'adresse (`?key=`) | en-tête ; jamais d'adresse à clé dans un journal | — |
| B-26 | Q:308-312 | `last_err` non liée si aucune exception | plus de chemin sans statut | — |
| B-27 | Q (aucun) | aucun plafond de dépense ni d'appels | plafond USD vérifié avant (pire cas) et après ; plafond d'appels par génération | `test_plafond_usd_arrete`, `test_serveur_budget_appels_et_requetes_invalides` |
| B-28 | Q:591 | arrêt de mitose sur des cellules invalides | seules les cellules valides comptent | `test_arret_mitose_par_nul_de_permutation` |
| B-29 | I:9,38 | « matrice de prédation » = argmax figé, par prédateur, égalités par ordre d'insertion | bandit par défenseur, ε-glouton, bris d'égalité aléatoire, graine dérivée | `test_bandit_explore_et_apprend` |
| B-30 | I:10,37 | récompense de Brier non bornée, coût constant | μ ∈ [0, 1], unilatérale, coût par bras | `test_recompense_anti_echec_bornee_et_unilaterale` |
| B-31 | I:30,31 | « conservation structurelle » = rapport de longueurs | à l'organisme ; le noyau ne note rien | — |
| B-32 | I:32 ; P:296-319 | compteurs lus dans un en-tête auto-déclaré ; « mutinerie » = mots-clés, « coopération » = ≥ 1 équation LaTeX ; une réponse vide (refus, panne) compte « 0 mutinerie, 0 coopération » | le juge externe ne lit que des étiquettes sur des tâches à vérité terrain ; une non-réponse est une erreur | `test_juge_exactitude_equilibree_et_non_reponse_erreur` |
| B-33 | I:14,40,41 | voir B-08 | voir B-08 | — |
| B-34 | I:33-36 | puissance des canaris sans spécificité, n = 3, placement non engagé, fuite vers le défenseur | sensibilité et spécificité, n ≥ 8, engagement, canaris hors du rapport rendu au défenseur | `test_canaris_sains_et_artefacts` |
| B-35 | I:21,26 | citations jamais vérifiées | tout ce que l'essaim cite est « à vérifier » (R7) ; le noyau n'accepte aucune citation comme preuve | — |
| B-36 | P:186-192 | sur réponse sans bloc texte, le **contenu de réflexion** est rendu comme réponse (interdit par Lazar) | les appelants v2.5 ne rendent que les blocs texte | — |
| B-37 | P:52-56 (capture 16:02) | `git push` échoue (adresse corrompue), le script affiche « poussé avec succès » ; `$ErrorActionPreference` sans effet sur git | aucun git ; chaque étape rend un statut | — |

Résultats « certifiés » de Gemini à la lumière de ces bugs : le test A/B « pascalien » (B-32) a donné 94,4 % / 8,94
à 14:52 puis 44,4 % / 1,61 à 15:41 (capture de Lazar, lignes 654-655) ; le bras A (0 %, 0 %, 0,06 équation en
37 secondes pour 18 agents) est compatible avec des refus ou des pannes rendus comme réponses vides ; et le script
a planté après avoir écrit le fichier « certifié » (ligne 661-668).

## 4. Ce qui est testé, et ce qui ne l'est pas

Testé sans réseau (37 tests) : extraction et validation d'un organisme (sain, sans manifeste, entrée absente,
syntaxe, lien symbolique) ; appel sain, erreur d'interface, modèle non conforme, plafond USD ; serveur (budget
d'appels, requêtes invalides) ; bac à sable (environnement sans clé ni mandataire, exception, délai, isolation réseau
indisponible) ; archive (scellée, non réécrite, tar reproductible) ; juge (parfait = 1, aucun = 0, inverse = 0, masque
sans vérité) ; boucle (simulation complète, amorçage invalide, lignée sans successeur, organisme poli et organisme
gourmand face au plafond, fichier STOP, mode réel refusé sans GO) ; boîte à outils (chaque garde, cas sain et
artefact).

Non testé, dit franchement :
- **l'intelligence de l'essaim** : en simulation, l'organisme est un factice écrit par la session ; l'exploration
  réelle (des espèces qui écrivent leur propre organisme) demande des clés et un GO ;
- **le juge réel** : les tâches réelles de conscience d'évaluation et de sabotage doivent être construites et
  préenregistrées (R1, R2) ; le juge en simulation est synthétique, à graines, et le dit ;
- **l'isolation complète** : `unshare -rn` n'est pas disponible dans ce conteneur (le test le simule) ; en root, les
  permissions ne protègent pas l'archive de l'organisme : le mode réel doit tourner sous un utilisateur dédié ou
  dans un conteneur — c'est écrit dans le refus de `lancer` ;
- **l'antériorité** : la famille « le système réécrit son propre code sous un juge fixe » existe (travaux cités de
  mémoire : « Automated Design of Agentic Systems », « Darwin Gödel Machine », AlphaEvolve) : à vérifier sur PDF
  empreinté avant toute revendication (R7, R8).

## 5. Décisions ouvertes, à Lazar

- **Métrique du champion** : Lazar veut « une métrique que l'essaim lui-même aura élaborée ». Le contrat le permet
  (`metrique_proposee.json`, archivée, jamais utilisée par le noyau). Réserve franche : si la métrique de choix est
  celle d'un des candidats, le champion est celui qui s'est le mieux noté. Proposition : les organismes proposent,
  Lazar gèle la métrique par préenregistrement avant la confrontation, et le score externe reste la mesure témoin.
- **Dépense** : amorçage à trois espèces plus G générations ≈ (3 + 3·G) appels longs par lignée plus les appels de
  l'organisme (bornés par `--appels-max`) ; devis à écrire au moment du GO.
- **Confrontation avec l'organisme de Gemini** : même noyau, même juge, mêmes bornes ; son code (branche de
  quarantaine du 24 octobre, une fois poussée) sera lu, ses fautes corrigées à part, et il sera mis sous contrat
  (point d'entrée, interface d'appel) sans changer sa conception.

## 6. Empreintes

Voir `EMPREINTES-v4.txt` (format `sha256sum`, chemins relatifs) et son compagnon `.sha256` ; les versions antérieures restent.


## 7. Ajouts de la v2 (24 octobre, 14:30 UTC) — ce fichier remplace la v1, gardée sans modification (R12)

- **Décision de Lazar (16:13, 16:16 et 16:19, heure de Paris)** : option (a) pour la métrique du champion, précisée —
  chaque organisme conçoit une **métrique objective calculée hors de lui** et un jeu d'attaques ; le noyau applique la
  métrique de A à B et celle de B à A, avec des attaquants d'une autre famille de fournisseur que le défendeur ; les
  métriques sont gelées par préenregistrement ; le score sur tâches cachées reste témoin. L'organisme décide aussi
  seul le nombre d'essaims et leur composition (monocultures par famille, hybrides, ou les deux). Contrat et consigne
  d'amorçage mis à jour (`noyau/contrat.py`).
- `organismes/gemini-v2/` : l'essaim de Gemini, version déboguée par la lignée « session-depot » (`m3_commun.py`,
  `572210c8…`, copié tel quel), **mis sous le contrat du noyau** par un adaptateur (`adaptateur_noyau.py`) et un point
  d'entrée (`principal.py`) qui gardent sa conception. Tourne sous le noyau en simulation (2 générations, 34 appels
  par génération, successeur produit, métrique proposée archivée). Son score en simulation est celui du hasard : les
  espèces simulées ne répondent qu'aux consignes de l'organisme factice ; cela ne dit rien de sa valeur réelle.
- `prereg/brouillon-confrontation-essaims-v1.md` : brouillon de préenregistrement de la confrontation (H-E1 apprentissage
  réel contre bras gelé ; H-E2 concordance de la métrique croisée avec le score externe ; H-E3 fidélité des espèces),
  avec devis par étapes. À contre-lire (R2) par session-depot ; rien n'est scellé.
- `notes/comparaison-audits-releve-gemini-v1.md` : comparaison R4 des trois audits (versé, conv-audit, session-depot) ;
  une correction de registre (clé en clair : R-327 faux), une réserve R7 (température refusée : à vérifier).
- `notes/contre-lecture-essaim-m3-debogage-v1.md` : contre-lecture R2 du paquet de session-depot : conforme après
  corrections (CL-01 moyenne : modèle servi différent compté « ok » ; CL-02 à CL-04 mineures).
- À écrire ensuite dans le noyau : `confrontation.py` (métriques croisées, attaques portées par l'autre famille) et
  l'option `--gel` (bras gelé) — avant le scellement du préenregistrement.


## 8. Ajouts de la v3 (24 octobre, vers 16:00 UTC) — ce fichier remplace la v2, gardée sans modification (R12)

Demande de Lazar (17:20, heure de Paris) : comparer l'organisme de Gemini corrigé par Claude Code et l'organisme du
noyau ; puis (17:27) Gemini a écrit lui-même un organisme sous le contrat (`canal/gemini-organisme-v1`, `6c61956c…`).

- `notes/comparaison-conception-trois-organismes-v1.md` : lecture du moteur massif du dossier 17 (qui décide quoi,
  mémoire, boucles, récompense, données laissées par le run), de l'organisme écrit par Gemini, de l'essaim corrigé ;
  ce qui manquait au noyau et ce qui a changé ; mécanique en simulation des cinq lignées ; trois nœuds pour Lazar.
- **Lignées imposées** : `--organisme-impose NOM=CHEMIN@FAMILLE` (répétable, `simuler` et `lancer`) — une lignée dont
  la génération 0 est fournie (organisme corrigé, organisme écrit par Gemini), validée par le même contrat, avec sa
  famille de fournisseur déclarée pour la confrontation et son empreinte d'arbre dans le manifeste de run
  (`boucle.Noyau(organismes_imposes=…)`, `boucle.empreinte_arbre`). Statuts `ORGANISME_IMPOSE_VALIDE` /
  `ORGANISME_IMPOSE_INVALIDE` ; refus d'un nom déjà pris ou d'une famille inconnue.
- **Appels parallèles** : `Appelant` sûr sous fils (verrou sur le plafond, l'engagement au pire cas des appels en vol,
  le compteur et le journal ; jamais sur l'appel réseau) ; `ServeurAppels(parallele_max=8)` sert jusqu'à huit appels
  à la fois (`--parallele-max`) ; `max_tokens` par défaut 4 096 pour un appel d'organisme sans `max_tokens`
  (`serveur.MAX_TOKENS_DEFAUT_ORGANISME`) ; `appels_simultanes_max` dans le résumé de chaque génération. Contrat,
  point 3, mis à jour (description, pas une consigne).
- **Marque d'ordre d'octets** : les fichiers écrits par l'organisme (ou sous Windows) sont lus en `utf-8-sig`
  (`manifeste.json`, `.py`, `reponses_test.json`, `metrique_proposee.json`, `metrique/`).
- **Espèces simulées** : lecture générique d'une consigne d'organisme inconnu (tâche si les deux étiquettes d'une
  famille y figurent — la famille citée le plus tard l'emporte —, induction si plusieurs vérités) ; le simulateur
  n'est plus écrit pour l'organisme factice seul.
- `organismes/gemini-organisme-v1/` : l'organisme écrit par Gemini, copié tel quel (`PROVENANCE-v1.md` : commit,
  empreinte d'arbre, réserve R4 sur « 3 passed » contre « 1 failed » dans le rapport livré).
- `runs/simulation-trois-organismes-v2/` : rapport, manifeste, événements, index d'archive et confrontation du run de
  simulation des cinq lignées (mécanique seulement ; scores non opposables).
- Tests : 45 (`python -m pytest -q tests`), dont cinq nouveaux (parallélisme × 2, lignées imposées × 2, BOM).
- Archive : `impose` et `famille` dans chaque ligne d'index et chaque `resume.json`.
