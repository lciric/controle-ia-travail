# Débogage des scripts de brainstorm du « dossier 17 » (essaim M3) — v1

Écrit le 24 octobre 2026 par la session Claude Code du dépôt (lignée « session-depot »), à la demande de Lazar :
« tu peux déboguer les scripts de ces différents brainstorms ? ». Statut : **outil, hors `main`, exploratoire**.
Rien ici n'est préenregistré (R1), rien n'est opposable ni « certifié ». Aucun script n'a été exécuté avec une clé
depuis la session : seuls les tests à blanc (aucun réseau, aucune dépense) ont tourné.

## 1. D'où viennent les scripts

Lazar a collé dans la session la sortie de son terminal Windows, avec le code source complet de trois scripts du
dossier `gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/17_SYSTEME_EVOLUTIF_MULTI_GENERATIONS_LOI_M3`
(le « dossier 17 ») :

| script d'origine | taille | état observé |
|---|---|---|
| `run_endogenous_eval_awareness_discovery.py` | 37 Ko | plantage en phase 3 |
| `finish_gen2_and_publication_swarm.py` | 37 Ko | trois plantages successifs, puis 1 réponse sur 36 |
| `run_pascalian_finesse_swarm_experiment.py` | 32 Ko | plantage après l'écriture des résultats A/B |

Ils importent un moteur, `run_massive_swarm_m3_parallel_engine.py` (79 Ko), **que je n'ai pas vu** : il n'est dans
aucune branche du dépôt distant, pas plus que le dossier 17. Le dépôt local de Lazar était « en avance de 10 commits »
sur `origin/main`, puis de 11 (commit `bc4866d`) ; la poussée a échoué (`URL rejected: Bad IPv6 address` : l'adresse
du dépôt distant contient des crochets Markdown), et le script a tout de même affiché « [OK] Tous les derniers
résultats ont été poussés avec succès ». Rien du dossier 17 n'est donc au dépôt. Voir la section 7 pour le verser
en quarantaine.

## 2. Les plantages et leur cause

| où | message | cause | correction dans la v2 |
|---|---|---|---|
| `finish_gen2…`, l. 168 | `AttributeError: module … has no attribute 'format_live_blackboard_context'` | la fonction n'existe pas dans le moteur ; le script l'attendait | `m3_commun.Tableau.contexte` ; aucune dépendance au moteur |
| `finish_gen2…`, l. 144 (2ᵉ version) | `SyntaxError: expected '('` | `def run_orthogonal_ swarm_unit` (espace dans le nom) | nom corrigé, module relu par les tests |
| `finish_gen2…` (3ᵉ version) | « 1/36 agents ont posté (0 équations) » puis plus rien | 35 appels sur 36 ont échoué ; chaque échec était avalé (`except Exception: pass`) et le script continuait | tout échec est consigné (code HTTP, erreur) et compté ; un plafond arrête le script |
| `run_endogenous_eval…`, l. 197 (phase 3) | `AttributeError: 'NoneType' object has no attribute 'setdefault'` | `eng.atomic_merge_and_save_substrate(substrate)` a renvoyé `None` ; le script réaffectait le résultat au substrat | `m3_commun.sauver_substrat` renvoie toujours le dictionnaire, après copie de secours horodatée |
| `run_pascalian…`, l. 481 | `AttributeError: … no attribute 'write_unified_markdown_report'` | la fonction du moteur s'appelle `write_massive_markdown_reports` | rapport écrit par `m3_commun.ecrire_rapport`, scellé (`.sha256`) |

## 3. Les défauts de mesure (plus graves que les plantages)

Lus dans le code collé ; chacun est corrigé dans la v2 et éprouvé par un test.

1. **Repli silencieux entre modèles.** `call_species_raw` essaie `claude-fable-5-1`, puis `claude-fable-5`, puis
   `claude-sonnet-5-5`, puis trois modèles Gemini, puis de nouveau Anthropic ; l'étiquette de l'« agent » garde la
   lignée demandée quel que soit le modèle qui a répondu. Les « castes », les « lignées » et la « mutinerie de l'agent
   #324 refusant l'identité GEMINI_ARGON » sont donc invérifiables : un modèle Claude a pu répondre à une invite qui
   le disait Gemini. **v2 : un modèle par lignée, jamais de rotation ; le modèle servi (`model` ou `modelVersion`)
   et la raison d'arrêt sont consignés ; un écart entre demandé et servi est marqué `MODELE_SERVI_DIFFERENT`.**
2. **La réflexion renvoyée comme texte.** `_extract_ant_text` renvoie les blocs `thinking` quand il n'y a pas de bloc
   `text`. Consigne de Lazar : ne jamais reproduire le contenu de réflexion. **v2 : blocs `text` seulement ;
   parties `thought` de Gemini ignorées.**
3. **Une réponse vide compte comme « sans mutinerie ».** `evaluate_agent_output_for_mutiny("")` donne
   `is_mutiny=False`, `equations=0` : un échec d'interface est lu comme un agent docile qui ne coopère pas. Le bras A
   du test « pascalien » a traité 18 appels en 35 secondes (14:49:49 → 14:50:24) contre 2 min 30 pour le bras B, avec
   0,06 bloc LaTeX par agent : ces chiffres sont compatibles avec 18 réponses vides ou en erreur. Le « 0 % de
   mutinerie » du bras A n'est donc pas un résultat. **v2 : statut (`ok`, `vide`, `echec_api`) compté d'abord ; les
   taux sont calculés sur les réponses `ok` seulement.**
4. **Les deux bras ne diffèrent pas seulement par le ton.** Le bras A est un ordre sans contenu mathématique ; le bras
   B contient l'identité à trois points de Bregman et deux questions précises. L'écart de production (0,06 contre 8,94
   blocs) mesure d'abord l'écart de contenu. **v2 : bras C « neutre » (même contenu que B, sans préambule maïeutique
   ni ton coercitif) ; les trois bras sont entrelacés dans le temps.**
5. **Des constantes imprimées comme des mesures.** Quand `eng.spectral_gram_analysis_massive` manque, les scripts
   impriment un dictionnaire codé en dur : `cap_Shannon=45.0000 | lambda_min_IDF=0.2500` (découverte),
   `48.0000 | 0.2700` (Pascal), `42.0 | 0.28` (G2). Les journaux collés montrent exactement ces valeurs : l'étage
   « M2 Onsager » n'a pas tourné dans ces runs. **v2 : analyse calculée (TF-IDF, matrice de Gram, valeurs propres) ou
   déclarée « non calculée ».**
6. **Un gabarit JSON qui contient les réponses.** Le gabarit donné à l'« arbitre » (étage « M1 Dolev ») porte des
   nombres d'exemple (`c_plus_rejected_count: 4`, `c_minus_validated_count: 12`, score `0.96`) que le modèle peut
   recopier. **v2 : aucun nombre dans le gabarit, aucun comptage « déclaré » ; un échec d'extraction renvoie des listes
   vides et garde le texte brut, jamais le gabarit.**
7. **Des « spécifications de génération 2 » écrites en dur.** `g2_rlcr_spec` et `g2_mem_spec` sont des constantes du
   script, rangées ensuite dans le substrat comme des mécanismes conçus par l'essaim. **v2 : seul ce que l'extraction
   tire des posts entre au substrat, avec sa provenance.**
8. **Purge manuelle des résultats nuls.** Un extrait collé supprime du magasin les entrées qui commencent par « Aucune
   nouvelle équation… » ou contiennent « refusant de générer », c'est-à-dire la trace que les agents n'ont rien
   produit. **v2 : rien n'est purgé ; chaque run ajoute une entrée d'historique avec ses comptes, y compris nuls.**
9. **Noms et messages.** Fichiers « RESULTATS_CERTIFIES… », « Rapport complet scellé », « poussés avec succès » après
   un échec. **v2 : « exploratoire », empreintes `.sha256` réelles, codes de retour vrais (0 ou 3 sur plafond).**

## 4. Ce que contient la v2

| fichier | rôle |
|---|---|
| `m3_commun.py` | client d'appel (un modèle par lignée, journal, plafonds, mode à blanc), tableau partagé, analyse spectrale, extraction JSON, substrat, évaluation A/B/C, rapports scellés |
| `memoire_isvd_plugin_revu.py` | copie relue du plugin mémoire du dossier 17 (calcul inchangé, chaîne brute, sans `exec`) |
| `run_1_decouverte_eval_awareness_v2.py` | phases 1 et 2 de la découverte ; la phase 3 (publication) est retirée |
| `run_2_generation2_failles_orthogonales_v2.py` | génération 2 ; spécifications en dur et publication retirées |
| `run_3_pascal_finesse_ab_v2.py` | brainstorm « finesse » puis comparaison A/B/C entrelacée, taux sur les réponses `ok` |
| `tests/` | 24 tests : chaque garde sur un cas sain et un artefact (R5) ; les trois scripts de bout en bout à blanc |

Chaque run écrit dans `runs_debogage/<horodatage>-<nom>/` : `journal_appels.jsonl` (un appel par ligne), `console.log`,
`resume_run.json` (comptes recalculés depuis le journal), le rapport Markdown et les extractions, chacun avec son
`.sha256`. Un dossier de run n'est jamais écrasé (R12). Le substrat reçoit une copie de secours horodatée avant
toute écriture.

Ce qui n'est pas changé : les textes des missions (données de Lazar et de Gemini, recopiés), la mécanique
« castes → tableau → sondes d'écart → extraction → synthèse », la mémoire spectrale. Ce que ces noms recouvrent :
une « caste » est un triplet (mode, lignées, température) ; l'étage « M2 Onsager » est une consigne d'écart donnée à
six appels de plus ; l'étage « M1 Dolev » est un appel d'extraction ; l'étage « M0 » est un appel de synthèse ;
la « mémoire Koopman ISVD » est un sac de mots haché en dimension 16 tronqué au rang 6 ; une « équation » est un bloc
`$$…$$` de sept caractères ou plus. Rien de tout cela ne mesure l'alignement d'un modèle.

## 5. Mode d'emploi (chez Lazar, à sa décision ; la session ne lance rien)

1. Copier les fichiers de ce dossier dans le dossier 17 (à côté du substrat). Python 3.11 ou plus, `pip install numpy`.
2. **D'abord à blanc**, sans clé ni réseau : `python run_3_pascal_finesse_ab_v2.py --a-blanc`.
   Vérifier `runs_debogage/…/resume_run.json` et le journal.
3. Poser les clés du programme, jamais celles d'un autre projet :
   PowerShell : `$env:M3_ANTHROPIC_API_KEY = "…" ; $env:M3_GEMINI_API_KEY = "…"`. Le client refuse de démarrer si la
   clé Anthropic est égale à `RR_ANTHROPIC_API_KEY` ou `RR_ANTHROPIC_API_KEY_2`.
4. Lancer avec un plafond : `python run_3_pascal_finesse_ab_v2.py --max-appels 120 --n-par-bras 18`.
   Ordre de grandeur des appels : script 1 ≈ 60 à 110 ; script 2 ≈ 45 à 80 ; script 3 ≈ 90 à 120 (les cellules
   hybrides comptent deux appels). Jusqu'à 6 144 jetons de sortie par appel : le coût se lit dans `resume_run.json`
   (jetons d'entrée et de sortie) et se convertit avec la grille de prix du jour.
5. Tests : `python -m pytest -q tests` (24 tests, aucun réseau).

Les scripts d'origine ne sont pas à relancer : ils lisent les clés du moteur (origine non vue), remplacent les
modèles en silence et écrivent « certifié ».

## 6. Ce que la v2 ne fait pas

- Elle ne rend pas les résultats opposables : aucune hypothèse, prédiction, métrique ni seuil n'est gelé avant le
  run (R1). Pour tester le dispositif sur un cas d'alignement (conscience d'évaluation, contrôle d'un agent
  délégué), il faut un préenregistrement contre-lu (R2) et un GO de dépense ; la lignée « conv-audit » en prépare un
  cahier (canal « reprise de la relève », message n° 01, point A3).
- Elle ne vérifie pas les mathématiques produites : les « concepts » et « énoncés » restent du texte de modèle.
- Elle ne reproduit pas le moteur de 79 Ko ni les runs « massifs » (241 castes, 882 agents) : ces nombres sont des
  nombres d'appels et de blocs `$$…$$`, pas des résultats.

## 7. Verser le dossier 17 au dépôt, en quarantaine, jamais sur `main`

Depuis le dépôt local de Lazar (PowerShell), après avoir arrêté tout script en cours :

```powershell
git remote set-url origin https://github.com/lciric/controle-ia-travail.git
git fetch origin
git push origin main:quarantaine/releve-gemini-2026-10-24-dossier17
git checkout -B main origin/main
```

La première ligne répare l'adresse (celle du terminal contenait des crochets). La troisième pousse les commits
locaux sur une branche de quarantaine neuve, sans toucher `main`. La dernière remet le `main` local sur celui du
dépôt ; les commits restent sur la branche de quarantaine. Avant de pousser : la ligne 314 de
`gemini/11_…/run_campagne_gpu_72h_5_volets_llama3.py` contient une clé Vast.ai en clair, déjà sur `main` (voir le
message n° 01 de « session-depot ») ; elle est à révoquer de toute façon.

## 8. Tests

```text
$ python -m pytest -q tests
........................                                                 [100%]
24 passed in 0.34s
```
