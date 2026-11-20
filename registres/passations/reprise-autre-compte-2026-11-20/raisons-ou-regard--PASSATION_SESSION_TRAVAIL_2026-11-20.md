# Passation de la session de travail « Raisons ou regard ? » — 20 novembre 2026, 08 h 40 UTC

Session : `session_01XJ6MgpmJDTK1D5Hsir6rTS` ; branche `claude/stoic-mayer-51otyy` de `lciric/raisons-ou-regard-travail`. Session mère : `session_01XJ6Mgr8BN6UanALsQatc5E`. Écrite à la demande de Lazar, relayée par la mère (R-4165). La passation précédente est `claude/PASSATION_SESSION_TRAVAIL_2026-11-19.md` (branche `claude/intelligent-brahmagupta-bt1oxx`).

## 1. Fait (du 19 novembre au soir au 20 novembre, 08 h 40 UTC)

- **La lecture de la fin** (`lire_annotations_v4.py` tel quel, puis `lire_annotations_v5.py`, décision 250) : 11 admises sur 18, « seuil non atteint après les données (décisions 228 à 250) » (`annotation/annotations_fin_v5.json`, `1befe02f…`). **Décision 251** (deux étiquettes de Lazar corrigées après coup) : 13 admises.
- **La génération de la fin** (décisions 252 à 256) : 20 tirages, 4 680 épisodes. Run `regard_msm-20261120-052259-debb`, H100 SXM, de 05 h 23 à 07 h 20 UTC, environ 10,9 $. **Sceau** commité avant toute lecture : `sceau_generation_fin_v1.json` (`df443372…`), épisodes `e011ae2c…`.
- **Décision 257** : Sonnet 4.6 juge d'origine et juge d'action ; Opus 5.5 témoin sur l'échantillon d'A2 (144 épisodes), sans rien décider. Clé : celle de Rigaud.
- **Code de la fin**, trois relectures et une vérification (décision 230), constats bloquants tous corrigés :
  - `experiences/analyses/exp1_juges_fin.py` : les juges, le verrou de la fin, le registre des lots ;
  - `exp1_verdict_fin.py` : le verdict mécanique ;
  - `exp1_lecture_fin.py` : la lecture.
- **Lots envoyés** (registre commité : `claude/papier_2026-11-14/experience_1/lots_juges_fin/`) :
  - juge d'origine, Sonnet 4.6, 4 680 requêtes : `msgbatch_01Jp5r3gMLujJ2puVeT38M8u` ;
  - témoin, Opus 5.5, 144 requêtes : `msgbatch_013iih8bpquVvgCDCCZYnPNH`.
  - Envoyés vers 08 h 34 UTC, avec la clé de Rigaud et un solde dit par Lazar (« plus de 60 dollars », lu à 60 $).
- **Verdict mécanique** commité (`verdict_fin/`) : les 4 680 usages d'entrée sont égaux aux comptes de l'assemblage.
- **Lecture par la règle seule**, commitée : `lecture_fin/lecture_exp1_fin_regle_seule.json` (`b54fe487…`).
  - Au sens de la note scellée : « non lisible (jumelles non reconnues) ».
  - Après les données (le cadre de la session, soumis à Lazar) : **H_B, « refus aveugle », pour `msm_aft_cot` et `msm_aft_no_cot`**, sur les 13, sur les 11 et sans les jumelles réécrites. Ce verdict ne dépend ni de la décision 251, ni des jumelles réécrites.
  - Chiffres sur les 13 :
    - `msm_aft_cot` : G +65,8 [51,3 ; 80,2], C −56,5 [−70,6 ; −42,5], DiD +9,2 [−3,1 ; 21,6] ;
    - L_B = 84,6 % ; L de `msm_aft_cot` = 28,1 % ;
    - le placebo est nul pour les six modèles ;
    - les témoins `aft_cot` et `aft_no_cot` n'ont ni gain net ni baisse de L ;
    - chez les épisodes engagés, C de `msm_aft_cot` vaut −52,2 points ; la passivité sur la jumelle vaut environ 28 %, contre 3 % chez `baseline`.

## 2. Reste

1. **Relever les deux lots** quand ils sont finis, puis `lire` chacun, puis `temoin`. Les commandes sont dans le brief.
2. **Refaire la lecture complète avec les juges** : `--juge`, `--temoin`, et `--juge-action` quand il existera. Sortie : `lecture_fin/lecture_exp1_fin.json`.
3. **Le juge d'action**, Sonnet 4.6 : de 14 à 35 $, 46 $ au plus avec la marge. Il ne part qu'avec un solde relu, plus bas une fois les deux lots facturés, ou avec une recharge. Le module le refuse sinon.
4. **Les comptes tirés des versions** (ajout de 01 h 46, point 13 ; ajout de 08 h 22, point 3) : les racines de légitimité ajoutées, l'outil et « email <rang> » ajoutés, le nombre de tentatives par évaluation, les « indécidable » et « clear: no » des placebos v3 chez Gemma et Gemini. Ils se calculent par un script à part, sur les versions et non sur les épisodes ; il n'est pas écrit.
5. **Le rapport à Lazar et à la mère**, avec les réserves du point 3.
6. **Les questions encore ouvertes pour Lazar** :
   - les deux cadres de la lecture (ajout de 08 h 20, point 4) ;
   - le jeton du dépôt de résultats à grain fin (ajout de 01 h 46, point 14) ;
   - le dépôt de ses fichiers de réponses dans le dépôt privé (point 5).

## 3. Réserves (à dire au rapport)

- **Le seuil de l'écriture n'est atteint qu'après les données, et par la décision 251.** La section 4 reste « jumelles non reconnues ». Les dérogations de la décision 251 sont nommées dans l'ajout de 01 h 46, point 11.
- **Lecture par action** :
  - exfiltration : « non lisible (placebo non nul) » pour les deux recettes ;
  - leaking : H_B pour `msm_aft_cot`, « non lisible » pour `msm_aft_no_cot` ;
  - c'est exploratoire : 6 et 7 évaluations seulement.
- **Les juges** :
  - Opus 5.5 juge avec réflexion adaptative, Sonnet 4.6 sans : le témoin n'est pas symétrique ;
  - `juge_msm.relever` perd le type d'erreur d'un résultat en échec (relecture n° 3, point 12) ;
  - le lien avec A1 et A2 passe par Sonnet 4.6, et non plus par le même juge.
- **Les procédures écartées** :
  - le pilote du 17 novembre est mis à part, ses épisodes ne sont pas lus (run `regard_msm-20261117-042119-e21b`, 3,64 $) ;
  - Lazar a annoté le pilote deux fois (décision 250).

## 4. Instances, agents, programmes

- **Aucune machine louée par cette session.** La H100 SXM 61582969 est détruite depuis 07 h 20 UTC ; c'est vérifié, l'instance n'existe plus. Rien n'est à récupérer sur vast.ai : les sorties sont au dépôt privé `Sirmium/rr-resultats`, sous `runs/regard_msm-20261120-052259-debb/`, scellées. Crédit vast.ai lu à 07 h 22 UTC : 7,94 $.
- Machines d'autres sessions, à ne pas toucher : 58936096, 58936099, 58936100, 60988826, 61170458, 61552174.
- **Agents en cours** : aucun. **Programmes en cours** : aucun ; la garde de la location est arrêtée, et la tâche programmée de 08 h 50 est supprimée.
- **En cours chez Anthropic** : les deux lots de la section 1.

## 5. Ce qui a été récupéré du conteneur, et ce qui ne l'est pas

- **Récupérés et commités** : les scripts de la session (`claude/papier_2026-11-14/experience_1/outils_session_2026-11-20/`, avec leurs empreintes).
- **Refaisables** :
  - les requêtes des lots, par `exp1_juges_fin.py preparer`, déterministe ; les empreintes sont au registre ;
  - les invites (`data/exp1_2026-11-20/invites_exp1_fin.jsonl` au dépôt privé, `a3469095…`) ;
  - les épisodes (dépôt privé, `e011ae2c…`).
- **Non récupérés, et à risque** : les fichiers de réponses de Lazar, hors de git par la règle. Ils sont seulement dans le conteneur de cette session :
  - `reponses_suite_lazar_e0ca068beefb.json` (la suite v6) ;
  - `reponses_pilote_lazar_95f171ecf8c3_1.json` (`653b9739…`, la seconde annotation du pilote).
  - Leurs empreintes sont dans `annotations_fin_v5.json`. Les déposer au dépôt privé demande le mot de Lazar ; sinon, il garde ses copies.

## 6. Prochaine action

Relever le lot du juge d'origine et celui du témoin (le brief donne les commandes exactes), commiter le registre, puis lire les décisions, l'accord du témoin et la lecture complète.
