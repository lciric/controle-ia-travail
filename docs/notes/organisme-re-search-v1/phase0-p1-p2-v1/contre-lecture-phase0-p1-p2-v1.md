# Contre-lecture avant exécution — phase 0 de P1 et de P2, organisme d'idéation — v1

**Préenregistrement contre-lu : `preenregistrement-phase0-p1-p2-v1.md`, sha256 recalculé `8c8240fa4b7def4ed0daa396c9c0e879307b4042f8e96ebd9223e78fee4713c0`, conforme à l'empreinte annoncée et à son compagnon ; commit c425c010.**

- Contre-lecteur : modèle J, sous-agent neuf, d'un autre modèle que le développeur (modèle I) ; n'a écrit aucune pièce de cette tâche. Note écrite à 2026-11-18T05:26:04Z (`date -u` dans la commande d'écriture) ; contrôles faits entre 2026-11-18T05:18:26Z et cette heure.
- Rien n'a été exécuté sur la configuration du préenregistrement. Aucune dépense, aucune machine, aucun appel de modèle, aucun accès réseau. Aucun fichier existant modifié. Les sources (course v67, attaques de Goodhart) n'ont pas été ouvertes.

## Verdict

**Scellable après corrections.** Aucun constat bloquant : le dessin est sain (la vérité vient du monde, aucun juge, gardes d'empreinte réelles, critères chiffrés). Cinq constats majeurs demandent une version v2 du texte et du lanceur avant l'exécution, parce qu'ils touchent des critères de lecture gelés ou des gardes de lancement, qu'on ne peut plus corriger après sans écart au texte scellé.

**Cette pièce n'est pas un feu vert de lancement pour le lanceur v1.** Elle cite l'empreinte du texte v1 parce que c'est la consigne ; or la garde du lanceur v1 n'exige que cette citation et un sceau, pas un verdict (constat C-5) : elle accepterait ce rapport. Le lancement reste une décision de la session mère, sur la v2.

## Pièces et contrôles

Sceaux vérifiés par `controle_ia.scellement verifier`, six sur six conformes :

| fichier | sha256 |
|---|---|
| `preenregistrement-phase0-p1-p2-v1.md` | 8c8240fa4b7def4ed0daa396c9c0e879307b4042f8e96ebd9223e78fee4713c0 |
| `mondes_reponses_p1p2_v1.py` | 2c80a833e311b2983fbe6a31d401ac80e3aa03e8d7ccbcb4c3e515d577ebab04 |
| `questionneurs_p1_v1.py` | feb2f4729f7567a08fd31017ea05085db1c80ce31711a65c7f7b2af3d0304922 |
| `mesure_forme_p2_v1.py` | b3da53aa5dd665c386b9e62a46deb92d94ae418369f147e220e99421fe32b932 |
| `lanceur_phase0_p1p2_v1.py` | 979f861a4ad585c5dc2e658c058f68c9dbedfce51d156bad725ee73113fb6d01 |
| `test_phase0_p1p2_v1.py` | 36f3699fa1b64121583cbd5310f18b03d41527b15655123c71e4bdf56374b9fe |

Lus aussi : `propositions-conception-re-search-v1.md` (2b882f8d…0f42e, sections 0, P1, P2) ; `contre-lecture-re-search-organisme-v1.md` (f81c778d…0c24, constats P-1 à P-8, A-1 à A-4) ; dans le dépôt public de l'organisme (commit a41b7b5, arbre de travail propre, lecture seule) : `orchestrator/pole/evaluateur_lois_v62.py` (26613fe7…8632, en entier) et `orchestrator/pole/memoire.py` (71f1d086…b79e, constante de la ligne 34 et lignes 150 à 205). Les empreintes de `monde_noyau.py`, `monde_banque.py`, du README et du gabarit citées par le texte sont conformes (recalculées).

Ce qui a été fait :
1. Essais relancés : `python3 -B -m pytest -q -p no:cacheprovider test_phase0_p1p2_v1.py` : **46 réussis** (python 3.13.18, numpy 2.5.3), aucun fichier écrit dans le dossier.
2. Gardes du lanceur essayées par moi sur des artefacts, dans un dossier hors dépôt, en mode réel sauf mention :
   - préenregistrement copié puis altéré (« 0,5 × » changé en « 0,9 × », compagnon refait) : code 2, rien écrit ;
   - copie exacte sans compagnon : code 2, rien écrit ;
   - contre-lecture absente (option omise, puis chemin inexistant) : code 2, rien écrit ;
   - contre-lecture scellée qui ne cite pas l'empreinte : code 2 ; contre-lecture qui la cite mais sans compagnon : code 2 ;
   - source fabriquée présentée sous l'empreinte attendue de la course v67 (fonction `charger_source`) : refus ; en mode d'essai de bout en bout, source altérée d'un octet après calcul de son empreinte : code 2, rien écrit ;
   - module de code altéré d'un octet dans une copie du dossier (`exiger_code_scelle`) : refus ; cas sain : accepté ;
   - contre-lecture scellée qui cite l'empreinte et dit « non scellable » : **acceptée** (C-5) ;
   - l'évaluateur de l'organisme n'a aucune empreinte attendue dans le lanceur (C-2).
3. Le bloc JSON du texte est égal à `bloc_effort(CONFIG)` et son empreinte (2df0dadb…5d0c) est celle que le lanceur recalcule. La clé de dérivation des graines est égale à celle de `controle_ia.manifeste`.
4. Contrôles ciblés sur de petits mondes (256 lois, T = 8, 150 mondes), avec une racine de graines à moi (777001) et avec celle des essais (4242) : chiffres cités dans les constats. Programmes jetables, hors dépôt, non versés ; les chiffres se retrouvent par les fonctions du dossier.

## Conditions de la session mère, une à une

| condition | tenue ? | preuve |
|---|---|---|
| R-3181 — P1 « hors table », écart déclaré | **tenue** | texte l. 89-91 (section propre, C5 indécidable, écart déclaré, décision laissée à Lazar) |
| R-3181 — critère A/A doublé d'un critère de largeur | **tenue**, avec C-4 | texte l. 129 ; `tient_aa`, lanceur l. 224-236 (un écart nul ou négatif fait échouer) ; essai `test_regles_gelees_ordre_aa_disparition`. Mon artefact (bruit ajouté à chaque divergence) : ordre et A/A échouent tous deux. Le critère a des dents ; il n'a jamais été vu tenir sur un cas sain joué (C-4) |
| R-3181 — contre-lu avant exécution | **tenue à la lettre**, avec C-5 | lanceur l. 161-172 et 535 ; mes essais de garde. La garde ne lit pas le verdict |
| R-3186 P1 (a) — effort et échantillonnage gelés au manifeste | **tenue** | texte l. 20-87 ; lanceur l. 116-133, 153-158, 576-577 ; essai `test_garde_bloc_effort_saine_et_artefact`. Réglages des proposeurs réels : renvoyés au manifeste de la phase 1 (aucun ne joue ici). Les seuils de décision sont hors du bloc (m-2) |
| R-3186 P1 (b) — ordre tiré par graine dérivée ; décision écrite sur l'effet de l'ordre | **tenue à la lettre, vide sur le fond** (C-3) | tirage : questionneurs l. 246-250 et 266-267, rôle « ordre » ; décision : texte l. 145. Les deux questionneurs du critère sont insensibles à l'ordre par construction |
| R-3186 P1 (c) — règle écrite des refus et des questions sans réponse | **tenue** | texte l. 143 ; questionneurs l. 219-231 ; mondes l. 336-352 et 424-432 ; essais `test_question_absente_arret_ou_question_perdue`, `test_carte_du_proposeur_saine_et_artefacts` (m-8 pour un détail de la phase 1) |
| R-3186 P1 (d) — carte à zéro question rapportée par questionneur | **tenue** | texte l. 112 ; lanceur l. 417-418 et 436, et `kl_*_par_point["0"]` pour chaque bras l. 402-403 |
| R-3186 P1 (e) — borne écrite de la revendication | **tenue**, avec C-3 | texte l. 202-204 ; lanceur l. 455-458 (version plus courte que le texte, m-6) |
| R-3186 P2 (a) — quota fixé sans lire l'oracle, plage gelée | **tenue** | texte l. 122 ; mesure l. 127-163 (projection sur quatre champs, refus hors plage) ; quota et plage dans le bloc d'effort ; essai `test_quota_a_la_main_et_sans_oracle`. Que l'auteur n'ait rien lu avant de fixer q = 2 est déclaré, non vérifiable |
| R-3186 P2 (b) — décision sur les cartes hors softmax | **tenue** | texte l. 120 et 173-175 ; lanceur l. 274-279 ; mesure l. 54-58 et 99-101 |
| R-3186 P2 (c) — loi de tirage de la référence exacte | **tenue** | texte l. 139, comparé ligne à ligne à `tirer_loi` (mondes l. 100-156) et aux variantes (mesure l. 83-117) : conforme. Reste l'hypothèse déclarée (texte l. 99) que cette loi représente la grammaire servie, non lue |
| R-3186 P2 (d) — aucune « nouveauté » | **tenue** | texte l. 124 ; mesure l. 167-169 ; lanceur l. 505 ; l'essai de bout en bout vérifie qu'aucune autre clé ne parle de nouveauté |
| R1 | **tenue**, avec C-4 | sections du gabarit présentes ; ce qui a été vu est déclaré (l. 229-233) mais incomplet sur la largeur. Le validateur `controle_ia.prereg.problemes` ne signale que la section « Contre-lecture » sans ses deux empreintes, ce qui est attendu avant contre-lecture (m-7) |
| R4 | **non tenue pour P2** (C-1) ; tenue pour P1 | P1 : lanceur l. 380-389 ; P2 : la lecture défavorable à la fermeture n'est écrite que dans une branche |
| R5 | **tenue pour l'essentiel** | chaque garde décisive a son cas sain et son artefact dans les essais ; exceptions : C-4 (largeur), m-1 (garde de hasard), m-9 (gardes sans essai) |
| R6 | **tenue** | compagnons conformes ; sortie, manifeste et journal scellés (lanceur l. 588-595) |
| R9 | **tenue** | `SeedSequence(racine, spawn_key=(clé,))`, mondes l. 43-52 ; manifeste lanceur l. 573-587 (m-4 pour le commit) |
| R12 | **tenue** | noms versionnés ; dossier de sortie neuf exigé (lanceur l. 210-214), essayé |
| N-058 — vérité du monde, aucun juge | **tenue** | réponses calculées par le code sur la loi du monde (mondes l. 283-315, questionneurs l. 262) ; score = divergence à la loi du monde (questionneurs l. 73-77) ; l'état donné au questionneur ne contient pas l'indice du monde (l. 216-217) ; seul l'oracle, artefact déclaré, le lit (l. 205-206) ; aucune composition qualifiée |
| Code de l'organisme non modifié | **tenue** | lecture par `runpy.run_path` seulement (lanceur l. 296-306) ; arbre du dépôt public propre |
| Sources refusées si leur empreinte change | **tenue pour les trois sources de données, non tenue pour l'évaluateur exécuté** (C-2) | lanceur l. 195-201 contre l. 555 |

## Constats

### Majeurs

**C-1 (majeur, R4) — P2 : la lecture qui gêne la fermeture n'est écrite que quand la ligne ne se referme pas.** Le critère compare la médiane de la référence à un quart, pas à la part observée (9 sur 23). Si la médiane dépasse un quart de peu alors que moins de 5 % des tirages atteignent la part observée, le code écrit « C3 se referme … (effet de la grammaire) » sans aucune réserve : la mention « part observée au-dessus du quantile 95 % de R1 » est sous `if not ferme` (lanceur l. 270-273), et le texte gelé affirme alors « la part observée est à la portée de la grammaire seule » (l. 172), ce qui serait faux. Le chiffre reste dans la sortie, mais la lecture gelée est à sens unique. S'y ajoute que la fermeture ne vaut que sous une loi de tirage choisie par l'auteur (types uniformes : un tiers des racines sur les deux types à forme unique), écrite après avoir su que 7 répétitions sur 9 sont des softmax (déclaré l. 231), et dont l'ordre de grandeur attendu est voisin du seuil (prédiction de l'auteur : 0,15 à 0,35). L'audit de symétrie prévu (l. 177) est le bon ; il ne remplace pas la lecture manquante.
- Texte, l. 172 — ancien : « | > 0,25 | **C3 se referme (ne change pas)** : la part observée est à la portée de la grammaire seule | » → nouveau : « | > 0,25 | **C3 se referme (ne change pas)** : sous la loi de tirage R1, le seuil d'un quart est à la portée de la grammaire seule ; s'y ajoute, écrite par le code comme dans l'autre branche : « part observée au-dessus du quantile 95 % de R1 » si moins de 5 % des tirages l'atteignent (la ligne se referme alors à la lettre du critère, avec cette réserve), sinon « part observée non distincte de R1 » | ».
- Lanceur, l. 267 — ancien : « … dépasse un quart (effet de la grammaire) » → nouveau : « … dépasse un quart (sous la loi de tirage R1) » ; l. 271-273 : sortir la lecture sur `p_ref_r1` du bloc `if not ferme` (elle est écrite dans les deux branches) ; essai `test_decision_p2_table_gelee` complété d'un cas « fermé avec part observée au-dessus du quantile 95 % ».

**C-2 (majeur) — l'évaluateur de l'organisme est exécuté sans contrôle d'empreinte.** Le texte cite son empreinte (l. 16) ; le lanceur l'exécute par `runpy` pour la garde de disjonction, qui décide de la composition de H, et se borne à inscrire son empreinte au journal (l. 555), sans la comparer. Un évaluateur changé passerait.
- Lanceur — ajouter `EMPREINTE_EVALUATEUR = "26613fe72da7f049d5dd076aab51a3808221bf52686b9d0258a201c8b38b8632"` et refuser de partir (code 2, avec les autres gardes, avant tout calcul) si l'empreinte diffère ou si le fichier manque.
- Texte, l. 188 — ancien : « | une source (course v67, attaques) d'empreinte inattendue | refus de partir (code 2), rien écrit | » → nouveau : « | une source (course v67, attaques) ou l'évaluateur de l'organisme, absent ou d'empreinte inattendue | refus de partir (code 2), rien écrit | ». (Aujourd'hui, une source absente donne une trace d'erreur, pas un refus écrit : `charger_source`, l. 195-198, ne teste pas la présence.)

**C-3 (majeur) — l'effet de l'ordre de présentation n'est mesuré que sur des questionneurs qui y sont insensibles par construction ; la décision écrite et la borne disent plus que la mesure.** L'aléatoire tire une position uniforme parmi les positions libres : permuter les prédicats ne change pas sa loi ; « aléatoire sous un autre ordre » est une seconde copie A/A. La bissection choisit le prédicat d'entropie maximale, quel que soit son rang ; l'ordre ne joue que sur le départage des égalités (sur mes petits mondes, où les égalités abondent, les deux bras posent la même première question dans 19 % des parties ; à 65 536 lois elles seront rares et les deux bras presque identiques). Les deux comparaisons « d'ordre » de C-P1-2 ne peuvent donc échouer que par un défaut de branchement ou par hasard : elles éprouvent la tuyauterie, ce qui est utile, pas une sensibilité. Le seul questionneur sensible (le répéteur, par l'ordre des traits) est rapporté sans décision. Or le texte en tire « l'ordre est déclaré sans effet mesurable … et l'effet n'est pas modélisé » en phase 1 (l. 145), et la borne revendique « sans effet mesurable de l'ordre de présentation » (l. 204).
- Texte, l. 145 — ancien : « S'il tient (les deux comparaisons d'ordre conformes) : l'ordre est déclaré sans effet mesurable à la précision de l'instrument ; en phase 1 il reste tiré par graine dérivée à chaque partie, jamais fixé, les deux parties A/A d'un proposeur ont des ordres différents, et l'effet n'est pas modélisé. » → nouveau : « S'il tient (les deux comparaisons d'ordre conformes) : la permutation est déclarée correctement branchée, rien de plus ; l'aléatoire et la bissection sont insensibles à l'ordre par construction, la comparaison ne dit donc rien de la sensibilité d'un proposeur réel. En phase 1 l'ordre reste tiré par graine dérivée à chaque partie, jamais fixé, et son effet sur les proposeurs réels est mesuré, jamais supposé nul : le préenregistrement de la phase 1 dira comment (par exemple des parties A/A au même ordre opposées à des parties A/A à ordres différents). »
- Texte, l. 204 — ancien : « …, sans effet mesurable de l'ordre de présentation. » → nouveau : « …, sans défaut de branchement de l'ordre de présentation (l'effet de l'ordre sur un proposeur réel n'est pas mesuré ici). »
- Texte, l. 162 et lanceur l. 260 — ancien : « instrument sensible à l'ordre de présentation » → nouveau : « ordre de présentation mal branché ou comparaison d'ordre non conforme » (même place dans la table, même conséquence : arrêt, aucune phase 1).

**C-4 (majeur, R1 et R5) — le critère de largeur n'a jamais été vu tenir sur un cas sain joué, et ce que les petits mondes en montrent n'est pas déclaré.** L'essai `test_famille_aa_et_ordre_sur_petits_mondes` calcule le critère entier (`tient_aa`) mais n'affirme que la moitié « contient 0 » (essais l. 536-543). Recalculé par moi sur ces mêmes mondes et graines : la largeur **ne tient pas pour les médianes** dans deux comparaisons sur trois (A/A de l'aléatoire : 0,2203 contre un maximum de 0,0921 ; ordre de l'aléatoire : 0,2202 contre 0,0921), elle tient pour les moyennes (0,0990 et 0,1182 contre 0,1208), et l'ordre de la bissection passe pour les médianes avec une **largeur nulle** (masse en 0 : la médiane y est muette, seule la moyenne décide). Avec ma racine : 0,2033 et 0,2111 contre 0,0900. La section « Ce qui a été vu » ne dit que « intervalles corrigés contenant 0 » (l. 233), et la confiance annoncée pour la famille entière est d'environ 65 % (l. 103). Je ne demande pas de toucher au seuil : un seuil relâché après ce constat devrait être déclaré comme tel. Je demande que ce soit dit.
- Texte, l. 233 — ancien : « famille A/A (copie, ordre de l'aléatoire, ordre de la bissection) : intervalles corrigés contenant 0. » → nouveau : « famille A/A (copie, ordre de l'aléatoire, ordre de la bissection) : intervalles corrigés contenant 0 ; critère de largeur, sur ces petits mondes : non tenu pour les médianes dans deux comparaisons sur trois (largeur ≈ 0,22 contre un maximum de ≈ 0,09), tenu pour les moyennes, tenu à largeur nulle pour les médianes de la bissection (masse en 0). La famille A/A entière ne tient donc pas sur les petits mondes d'essai. »
- Texte, l. 103 — la confiance « ≈ 65 % pour la famille A/A entière » est à réécrire par l'auteur à la lumière de ce chiffre (elle lui appartient), avec sa raison s'il la maintient.
- Essais — l'essai nommé ci-dessus écrit le résultat de la largeur (affirmation de ce qui est observé, par statistique), au lieu de le calculer sans le lire.

**C-5 (majeur, R5) — la garde de contre-lecture passe sur une contre-lecture défavorable.** `exiger_contre_lecture` (lanceur l. 161-172) exige un fichier scellé qui contient l'empreinte ; essayé par moi : un rapport scellé « non scellable » qui cite l'empreinte est accepté. Le présent rapport le serait aussi.
- Lanceur — exiger en plus une ligne exacte, par exemple « Verdict de contre-lecture pour <empreinte du texte> : scellable », et refuser sinon ; essai sain et artefact.
- Texte, l. 186 — ancien : « | contre-lecture absente, non scellée, ou qui ne cite pas l'empreinte de ce texte | » → nouveau : « | contre-lecture absente, non scellée, qui ne cite pas l'empreinte de ce texte, ou dont le verdict écrit n'est pas « scellable » pour cette empreinte | ».

### Mineurs

- **m-1 — la garde du répondeur au hasard (C-P1-4) prouve un branchement, pas l'absence de fuite.** Sous des réponses au hasard la bissection n'est pas égale à l'aléatoire mais nettement pire (petits mondes, moyennes : −0,416, intervalle [−0,548 ; −0,286]) ; la garde « borne basse ≤ 0 » passe donc avec une marge énorme. Mon artefact : un répondeur qui dit la vérité une fois sur deux et tire à pile ou face sinon **passe la garde** (moyennes : −0,229, [−0,333 ; −0,131]). Elle n'échoue que pour un répondeur presque exact (le cas de l'essai). À écrire dans le texte (choix 7, l. 223) : la garde détecte un mode « hasard » non branché, rien de plus. Même cause, à dire dans la borne : la divergence récompense aussi une carte centrale (un questionneur qui n'apprend rien et garde un grand ensemble compatible est mieux noté qu'un questionneur qui resserre à tort) ; elle ne mesure pas la seule information acquise.
- **m-2 — seuils de décision hors du bloc gelé, et mode d'essai sans garde.** `fraction_largeur_aa`, `seuil_fuite`, le seuil de P2 et les valeurs attendues de M2 sont dans `CONFIG` mais pas dans `bloc_effort` (lanceur l. 116-129) : ils ne sont protégés que par le compagnon du lanceur, que rien n'ancre dans le texte. Le mode `--essai` permet de jouer n'importe quelle configuration, la vraie comprise, sans contre-lecture ni contrôle du code ; la sortie porte alors `"essai": true`. Remède sans v2 : le lecteur du verdict (R13) refuse toute sortie marquée essai et compare les empreintes de code du manifeste à celles du tableau ci-dessus. Remède en v2 : seuils dans le bloc.
- **m-3 — taux d'erreur de la famille A/A sous-estimé.** Le texte dit « au plus 0,05 » (l. 135) ; chaque comparaison porte deux statistiques, soit six intervalles au niveau 1 − 0,05/3 : au plus 0,10. À corriger ou à passer à Bonferroni sur six.
- **m-4 — commit du manifeste.** Le code de retour de `git rev-parse` n'est pas lu (lanceur l. 569-572) : un échec donne un commit vide, sans mention ; l'état modifié ou non de l'arbre n'est pas écrit. Aujourd'hui la commande rend c425c010.
- **m-5 — sources des attaques dans un dossier temporaire de session** (lanceur l. 62-67) : description seulement, mais leur disparition arrêterait le run par une trace d'erreur et non par un refus écrit (voir C-2).
- **m-6 — la borne écrite par le code (lanceur l. 455-458) est plus courte que celle du texte** : il y manque « rien sur des prédicats d'une autre forme, rien sur la recherche en langue naturelle de l'article ». À recopier en entier.
- **m-7 — section « Contre-lecture » du texte sans les deux empreintes que le gabarit exige** (seul problème rendu par le validateur) : à remplir en v2 avec l'empreinte du texte v1 relu et celle de ce rapport.
- **m-8 — sous la règle « question perdue » (phase 1), une réponse non booléenne du répondeur, défaut du code, est absorbée comme question perdue** (questionneurs l. 219-231 : le `try` couvre `exiger_booleen`) au lieu d'arrêter. Sans effet en phase 0 ; à corriger avant toute phase 1.
- **m-9 — gardes de la liste d'arrêt sans essai** : points de carte incohérents (lanceur l. 347-348), grammaire des prédicats différente (l. 317-318), sonde dégénérée pour un seuil (mondes l. 292-293).
- **m-10 — prémisse « l'aléatoire est meilleur que le répéteur ».** L'hypothèse la dit « connue d'avance », l'auteur lui donne 55 % ; un échec de C-P1-1 sur cet écart serait ambigu (instrument ou prémisse). Déclaré, conservateur (l'échec arrête) ; à redire dans le rapport de résultat. Sur mes petits mondes l'écart tient (médianes 0,136 [0,041 ; 0,214] ; moyennes 0,077 [0,016 ; 0,142]).

## Ce qui a été cherché et trouvé juste

- Aucun critère de P1 ne passe d'autant mieux que l'instrument est mauvais : le « contient 0 » de l'A/A est lié à une largeur rapportée à l'écart ponctuel entre les bornes, sur les mêmes mondes, et un écart nul ou négatif fait échouer ; l'ordre exige point et borne basse strictement positifs pour les deux statistiques ; la dégradation sous inversion est jugée sur les moyennes, que la masse en 0 n'aveugle pas (petits mondes : 0,367 [0,296 ; 0,441]) ; les gardes priment sur le verdict. Réserves : m-1, et la médiane muette de la bissection (C-4).
- Masse en 0 : une médiane nulle des deux côtés donne un écart nul, donc un échec de l'ordre et de la largeur, jamais un succès (lanceur l. 221 et 233 ; essai `test_regles_gelees_ordre_aa_disparition`).
- Réécriture vectorisée égale à l'évaluateur de l'organisme à 1e-12 près sur 200 lois des six types (essai relancé) ; sémantique relue ligne à ligne, conforme.
- Appariement par monde, mêmes rééchantillonnages pour les deux statistiques, graines distinctes par comparaison ; bras « #ordre » : même graine de questionneur, seule la graine de l'ordre change.
- P2 ne peut que refermer une ligne ; quota et attaques de Goodhart en description seulement ; reproduction de M2 exigée avant toute référence.

## Ce que je n'ai pas pu vérifier

- Le comportement à l'échelle du préenregistrement (65 536 lois, 200 mondes) : durée, mémoire, valeurs ; rien n'y a été joué.
- Ce que l'auteur avait lu ou non en fixant le quota, la loi de tirage et les seuils (déclarations).
- Que la loi de tirage R1 représente la grammaire servie aux proposeurs (hypothèse déclarée ; le fichier qui la sert n'était pas dans ma liste).
- Le contenu et la structure des sources (non ouvertes), l'accord R-3157, les registres.

## Incidents

Aucun refus de permission, de crochet ou de classifieur. Un dossier de travail jetable hors dépôt (copies altérées, sources fabriquées, deux programmes de contrôle). Aucune dépense, aucune machine, aucun appel de modèle, aucun accès réseau.
