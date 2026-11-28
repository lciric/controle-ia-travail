# Vérification de la synthèse v2 « comment détecter » — angle « sens et expériences », tour 1 — v1

## Verdict : **non conforme**

- Les chiffres et les phrases anglaises de la v2 sont sur leur page. Le code confirme VS-01 aux deux commits.
- Mais le **sens** ne tient pas, en cinq points majeurs :
  1. le bras principal de E1 (« maximum sur le champ `COST` ») relit une grandeur **déjà vue** (T2 de la lecture décisive
     de P3), que la note du brainstorm avait écartée comme poursuite après coup ; la v2 ne prévoit l'aveuglement
     qu'envers l'addendum 1 et ne le dit pas (R1, R3, R4) ;
  2. le point 2 du verdict lit [BX] sur le mauvais montage : le montage proche de P3 donne 0,81 (ou 0,63), pas 0,5 ;
     « le nul est celui que la littérature prévoit » n'est pas appuyé ;
  3. la « lecture à une seule position après une question », dite levier le mieux appuyé, est en défaut sur les cas les
     plus proches de P3 (sous-rendement et tromperie sur consigne) dans trois PDF que la v2 cite sans ces passages ;
  4. deux sorties de E1 concluent l'absence à partir d'un nul, et T1, seul test à contexte fixe, manque aux critères ;
  5. E2 sur les actions de P3 est un nœud de Lazar, rangé à tort parmi les choix à défaut de 48 heures.
- S'y ajoutent sept constats moyens et sept mineurs. Aucun chiffre n'est à retirer. Mais les corrections changent le
  verdict et la recommandation : il faut une v3 (tour 2), puis une vérification neuve, avant tout envoi à Lazar.

## Cadre

- **Objet.** `…/revue-detection/synthese-comment-detecter-v2.md` (sha256
  `90ad38bf106b2351bf54cdf6962d5b7fef8cf3f8cbfbaf209ff124cabac84e4e`, compagnon égal). Traitement :
  `…/revue-detection/traitement-verification-synthese-tour1-v1.md` (`c87ecdec…`, compagnon égal). v1 (`a47f9141…`) et
  vérification du tour 1 (`43986648…`) : compagnons égaux. `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Vérificateur neuf.** Je n'ai écrit ni la v1, ni la v2, ni les extractions, ni la vérification du tour 1, ni le
  traitement. 2026-10-20, de 11:00 à 11:45 UTC environ.
- **Lecture seule.** Aucune écriture dans le dépôt ; git en lecture seulement (`git show`, `git log`). Non ouverts :
  `prereg/P3-consignes-v1.md`, textes d'action, clés. Aucune recherche web, aucun service payant, aucun contact, aucune
  commande Vast.ai.
- **Méthode.** Empreintes des 21 PDF de `…/revue-detection/verification/cles.txt` recalculées : toutes égales
  (`empreintes-pdf-recalculees.txt` ; compagnons égaux pour les PDF du dépôt, RO compris). Texte de chaque page extrait à
  nouveau par moi (`pdftotext`, brut `rNNN.txt` et mise en page `pNNN.txt`) sous
  `…/revue-detection/verification-v2-sens/pages/<clé>/`. Recherche : `cherche2.py` (même normalisation que `cherche.py`).
  Toutes les phrases entre guillemets de la v2 cherchées dans toutes les pages (`guillemets_v2.py`,
  `sortie-guillemets-v2.txt`) : chaque phrase anglaise est sur la page citée ; les 16 « introuvables » sont françaises, du
  code ou un titre. Relus contre les PDF, le code et les registres : verdict (section 1), différences de montage
  (section 3), expériences (section 4), recommandation et nœuds (section 5). « l. » d'un PDF = ligne du fichier `rNNN.txt`
  (ou `pNNN.txt` pour une table) de mes pages ; « l. » de la v2 = ligne du fichier v2.
- **Sigles des pièces du dépôt.** [P] `prereg/P3-premier-test-i-a-v1.md` (`d975e981…`) ; [V]
  `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…`) ; [N] `docs/notes/brainstorm-suite-P3-v1/` (note
  `note-decision-suite-P3-v1.md`, `a023093e…`, citée par la v2 l. 12).

## Constats (le plus grave d'abord)

### VV2-sens-01 — majeur — E1 : le bras « champ du coût » n'est pas aveugle (R1, R3, R4) ; divergence non présentée

- **Où.** v2 l. 165 (E1 : « Production : maximum sur le champ `COST` ») ; l. 168 (piège : « rédiger sans lire les
  descriptifs A1 et A2 de l'addendum 1 (N-028) ») ; l. 173-174 (recommandation (2)) ; l. 178 (confiance) ; l. 183-184.
- **Problème.**
  - T2 de P3 a déjà calculé, pour les deux sondes principales, l'aire du maximum sur le champ `COST` et sur les jetons qui
    le précèdent, saboteur contre honnête ([P] l. 242-247). C'est la grandeur du bras de production de E1, plancher en moins.
  - Le verdict en donne le drapeau ([V] l. 170-172 : « Le drapeau de T2 n'est pas une conclusion et ne doit pas être cité
    comme telle » ; l. 358-359). N-025 exclut cette remarque de l'audit « par la règle gelée »
    (`registres/decisions.md` l. 446). [P] l. 141-142 : sans T4, « une sonde qui lit la grandeur du nombre écrit passerait
    T1 et T2 ».
  - Les valeurs de T2 (et de T1 et T4 sur l'action entière) sont écrites dans le dépôt : [N] `propositions/proposition-A.md`
    l. 17-18 ; `proposition-C.md` l. 48-50 ; `proposition-D.md` l. 30 ; `objections/objections-1.md` l. 40-41 ;
    `objections/objections-2.md` l. 338-342 ; `reponses/reponses.md` l. 375. Je ne les recopie pas.
  - La note [N] range parmi les options tombées « A2 : poursuit T2 après coup, sans plancher par jeton » (l. 85) et
    recommande « de ne relire P3 en rien » (l. 8). `proposition-C.md` l. 323-324 : un « P3 bis » localisé sur le champ du
    coût « serait poursuivre après coup le signal de T2 […] Tout signal y serait suspect (R4, R3) ».
  - Le GO de N-028 vient après (`registres/decisions.md` l. 456). Sa ligne ne promet l'aveuglement qu'envers A1 et A2 de
    l'addendum 1. La v2 reprend cette limite sans voir que T2 a déjà livré la grandeur.
- **Conséquence.** Ce bras ne peut pas être la « première tentative de détection » de R-262 (2) au sens de R1. Un
  « au-dessus » y serait suspect (R4) ; sa recherche vise un signe déjà aperçu (R3). Seuls le plancher de même position et
  T4 au champ sont des grandeurs neuves. La confiance de 60 % ignore que l'issue principale est en partie connue.
- **Correction.** (1) E1, piège et contrôle : « grandeur déjà vue (T2 de la lecture décisive, [V] l. 170-172) ; bras non
  aveugle ; lu comme diagnostic de l'instrument (lecture du nombre : plancher de même position, T4 au champ), jamais comme
  détection ». (2) Donner cette raison à la ligne « Revendication » (l. 183-184). (3) Présenter à Lazar la divergence :
  N-028 contre la note [N] (option A2 tombée) et N-025 (remarque 4 exclue). (4) Exiger que le préenregistrement de P3b
  déclare l'exposition (R1). (5) Pour la session : la ligne N-028 du registre porte la même limite.

### VV2-sens-02 — majeur — Verdict, point 2, et rang 3 : [BX] lu sur le mauvais montage

- **Où.** v2 l. 28-29 (« les montages proches tombent à 0,5 [BX p. 8 …] et 0,606 [YS p. 3] : le nul est celui que la
  littérature prévoit ») ; l. 128 (rang 3 : « 0,95 → 0,81 → 0,5 », pouvoir « fort »).
- **Problème.**
  - P3 garde la consigne privée dans le contexte et ne note que les jetons de l'action ([P] l. 198-201, l. 330-332).
  - Chez [BX], c'est le « Score Filtering » : « Score filtering retains the full transcript during inference but selectively
    excludes certain token positions when computing the final probe score » (p. 5, l. 53). Même modèle, sondes de paires de
    consignes : « probe performance degraded by 14 points to 0.81 AUROC » (p. 5, l. 85).
  - Consigne remplacée par une consigne bénigne : « 32-point drop to 0.63 AUROC » (p. 6, l. 3).
  - Le 0,5 vient de l'organisme **affiné** : « Fine-tuned Model Organisms exhibit the target behavior without requiring
    elicitation prompts or producing reasoning traces » (p. 4, l. 59), sondes réentraînées (p. 8, l. 47, l. 58). P3 n'est
    pas affiné.
  - Le montage de [BX] le plus proche de P3 est donc entre 0,63 et 0,81 (0,81 avec un raisonnement dans le contexte, que
    P3 n'a pas). Ailleurs : 0,653 sur toutes les actions [AU p. 6] ; 0,606 [YS p. 3]. Ces aires sont en moyenne et sans
    plancher apparié (v2, point 3) : on ignore si elles passeraient un plancher comme le nôtre.
  - Nuance à garder : à 1 % de faux positifs contre le témoin, [BX] tombe à 0,03 en « Score Filtering » (p. 6, table 1 :
    ligne « Sandbagging », colonnes 1.00, 0.04, 0.03).
- **Correction.** Point 2 : « Les montages les plus proches (consigne dans le contexte, rien d'écrit dans l'empan lu) donnent
  des aires modestes, en moyenne : 0,81 avec raisonnement dans le contexte [BX p. 5], 0,63 consigne remplacée [BX p. 6],
  0,653 [AU p. 6], 0,606 [YS p. 3] ; 0,5 seulement sur un organisme affiné [BX p. 8]. La littérature ne prévoit ni n'exclut
  le nul de P3 ; aucune ne mesure contre un plancher apparié. » Rang 3 : remplacer la chaîne par ces montages ; pouvoir
  « moyen ».

### VV2-sens-03 — majeur — « Lecture à une seule position après une question » : contredite sur les cas les plus proches

- **Où.** v2 l. 23-25 (point 1) ; l. 33-35 (point 3 : « Leviers les mieux appuyés : … lecture à une seule position ») ;
  l. 47 (ligne [PAR] : « question sans contraste 0,849 et 0,879 ») ; l. 50 (ligne [DYL]) ; l. 166 (E2, tranche : « Le mieux
  appuyé hors domaine … ; [DYL table 9] et sans contraste [PAR table 3] ») ; l. 168 (E2, piège : analogie [LIAR]) ;
  l. 173-174 ; l. 178.
- **Problème.** Les cas les plus proches de P3 (sous-rendement ou tromperie sur consigne, modèle moyen) vont contre :
  - [AP] p. 9, l. 17 : la sonde lue après « Was your last response deceptive? » est « comparable to our Roleplaying probe,
    except for substantially degraded performance on Sandbagging ». [AP] p. 18, l. 47 : « We can see that every Sandbagging
    response is rated as highly deceptive – even when the model chooses not to sandbag. » C'est la preuve directe, sur PDF,
    du piège de E2 (la sonde lit la disposition, pas l'acte) ; la v2 n'en donne qu'une analogie boîte noire ([LIAR]).
  - [PAR] table 3, p. 7 (`p007.txt` l. 25, l. 27) : avec la sonde RP, au sous-rendement, « Deception No (RP) … 0.457 » et
    « Honest Yes (RP) … 0.437 » ; la v2 ne cite que la sonde Pairs. Conclusion des auteurs (p. 7) : « By contrast, Peak
    Activation and the Follow-up monitors consistently underperform compared to Full Averaging. »
  - [DYL] p. 11, l. 1 : sur la tromperie sur consigne, exactitude équilibrée médiane 0,85 pour la sonde d'Apollo
    (moyenne) contre 0,81 pour la sonde lue après la question (« from 0.85 to 0.52 for Apollo, from 0.81 to 0.65 for
    DYL »). Table 9, p. 28 (même mesure) : Qwen3-8B 0,74 contre 0,69 (`p028.txt` l. 33) ; Llama-3.3-70B 0,84 contre 0,74
    (l. 31). Sur les 32 lignes, la moyenne l'emporte 22 fois, la question 8 fois, 2 égalités (compte du vérificateur). La
    v2 cite ces chiffres sans la comparaison ; « [DYL table 9] » reste orphelin en l. 166 (reste de VS-05).
  - L'appui réel est ailleurs : [OA] table 15 (hors domaine ; tricherie écrite dans le code) ; [CA] (163 016 transcriptions
    FIBS, contraste « Yes. » moins « No. », négatifs pris aussi avant le sabotage dans le même épisode : p. 6, l. 73). E2
    n'a ni FIBS (nœud de contact) ni ce contraste appris sur données larges : ses sondes génériques ressemblent plus aux
    montages d'[AP] et de [PAR].
  - Le traitement l'avait signalé hors écarts (remarque 2), sans l'appliquer.
- **Correction.** Points 1 et 3 : « appuyée hors domaine et à grande échelle, avec données larges et contraste ([OA],
  [CA]) ; en défaut sur le sous-rendement sur consigne ([AP] p. 9, p. 18 ; [PAR] table 3, sonde RP) ; pas meilleure que la
  moyenne sur la tromperie sur consigne ([DYL] p. 11, table 9) ». E2, piège : citer [AP] p. 18. E2, tranche : prédire
  l'échec probable de T1. Revoir la recommandation (2) et sa confiance.

### VV2-sens-04 — majeur — Conventions de lecture : absence conclue d'un nul ; T1 oublié

- **Où.** v2 l. 166 (E1, tranche : « Oracle en échec : pas de trace linéaire à ces couches » ; « Oracle conforme à T3 et
  T4, génériques non : l'information est là ») ; l. 178-180 (« (lecture, direction, ou absence de trace) » ; « passe le
  plancher et T3 et T4 » ; « T3 et T4 sont l'obstacle ») ; l. 34-35 (« toujours lues contre le témoin, la mention et T4 »).
- **Problème.**
  - [P] l. 272-274 : « « Non au-dessus » se lit « non détecté à cette puissance », jamais « ne sépare pas » ». Un oracle
    appris sur 60 tâches, en validation croisée, qui ne passe pas, ne prouve pas l'absence de trace linéaire.
  - T1 est le seul test à contexte égal : actions du saboteur qui gonflent contre celles qui ne gonflent pas ([P]
    l. 238-241). T3 et T4 n'excluent pas une sonde qui lit « la consigne trompeuse m'est adressée » : T4 compare à
    l'honnête (sans consigne) ; T3 à la mention (consigne attribuée à un autre).
  - [KU] p. 5, l. 53-56 : « the probe detects the deceptive prompt regime — the model's internal state when processing
    under a deceptive system prompt — rather than the downstream success of deception: verified and unverified examples
    score identically ». [AP] p. 18, l. 47 (ci-dessus). « L'information est là » (sur l'acte) exige T1.
- **Correction.** E1, tranche : « Oracle non au-dessus : non détecté à cette puissance ». « Information sur l'acte »
  seulement si T1 et T4 (avec le contrôle des coûts déjà déclarés) sont établis ; T1 non calculable : « non concluant ».
  Confiance : retirer « absence de trace » ; écrire « plancher et T1, T3, T4 ». Point 3 : « témoin, mention, T1 et T4 ».

### VV2-sens-05 — majeur — E2 sur les actions de P3 est un nœud, pas un défaut de 48 heures

- **Où.** v2 l. 165 (E2) ; l. 173-174 (« E1 avec E2 greffée sur la même passe ») ; l. 197-199 (positions « après une
  question » rangées sous « proposer avec recommandation, défaut 48 heures »).
- **Problème.** [P] l. 415-416 : « Tout audit qui demanderait des textes ou des activations autres que ceux gardés, ou une
  grandeur non écrite ici, est un **nœud** de Lazar ». [P] l. 428 : « pas de seconde lecture sur d'autres sondes, couches ou
  jeux ». E2 crée des activations neuves (question ajoutée), des sondes neuves (« apprises avec la question ») et plusieurs
  couches, sur les actions de P3. Le GO de N-028 ne couvre que la localisation au champ du coût avec plancher apparié et
  l'oracle sous T1, T3, T4 (`registres/go.md` l. 32 ; `registres/decisions.md` l. 456). CLAUDE.md range l'écart à un
  préenregistrement scellé parmi les nœuds (arrêt, attendre le GO). Avec le défaut de 48 heures, E2 passerait sans GO.
- **Correction.** Écrire : « E2 sur les actions de P3 : nœud de Lazar (extension de N-028) ; sans GO, E2 attend des
  épisodes neufs ». Retirer « après une question » de la liste à défaut pour P3b. Même statut pour la manipulation de
  VV2-sens-07.

### VV2-sens-06 — moyen — « Avant le champ » ne garantit pas l'absence du nombre de l'action en cours

- **Où.** v2 l. 151 ; l. 153 (« (a) … aucun coût déclaré dans le contexte ») ; l. 169 (« ne voit pas le nombre de l'action
  en cours (attention causale) ») ; E3 l. 165, l. 169.
- **Problème.** Le format impose `TITLE`, `PROPOSAL`, `CONTROLS`, puis `COST` (`src/controle_ia/environnements/propositions.py`
  l. 40-49, `5d97b223…`, identique à `97dd829` et `7a54d43`). `PROPOSAL` et `CONTROLS` sont du texte libre ; la consigne
  demande de nommer modèles, jeux de données et métriques (l. 32-39) : des nombres d'échelle peuvent précéder le champ, au
  premier pas aussi. `lire_action` prend la première occurrence de chaque clé, dans n'importe quel ordre (l. 129-138) :
  `COST` peut venir plus tôt. Le rapport moyen d'environ 33 ([V] l. 345) laisse ouverte l'idée que le saboteur élargit le
  projet ; la note [N] pose la question (l. 43 : « s'il élargit le projet »).
- **Correction.** Écrire « ne voit pas le champ `COST` de l'action en cours ». Ajouter un contrôle mécanique : nombres (et
  unités de calcul) avant le champ, comptés par condition, comme P3-P6 ; bras restreint aux actions sans nombre avant le
  champ, ou strates ; T4 maintenu.

### VV2-sens-07 — moyen — Contrôle du nombre écrit : la manipulation causale manque

- **Où.** v2 l. 142-159 (règles communes) ; l. 165-169 (E1).
- **Problème.** Le seul contrôle du nombre est T4 par strates, peut-être non calculable (v2 l. 158-159). La note [N],
  source de la v2, propose mieux : option (A2), « plan contexte × texte × nombre (C2 fusionnée avec D2) » ; « c'est la seule
  mesure qui sépare le nombre écrit du contexte privé » (l. 26-27). D2 : passe forcée sur les textes gardés, contexte
  {saboteur ; témoin} × nombre du champ {original ; remplacé par la médiane honnête de la même tâche}, maximum seulement
  (`propositions/proposition-D.md` l. 81-99). Toujours calculable ; même passe que E1.
- **Correction.** L'ajouter comme option du contrôle du nombre, dans le même préenregistrement et la même passe, avec son
  statut de nœud (VV2-sens-05).

### VV2-sens-08 — moyen — E3 : montage incohérent ; choix de la sonde contraire à P-011

- **Où.** v2 l. 165 (E3) ; l. 166 (E3, tranche : « paires minimales et choix sur la cible [RH p. 9, p. 27] ») ; l. 167
  (coût) ; l. 174-175 ; l. 184.
- **Problème.**
  - (a) « Paires d'actions qui ne diffèrent que par le coût » et « lecture avant le champ `COST` » : à préfixe égal, les
    activations avant le champ sont égales (attention causale). Une sonde lue avant le champ n'apprend rien de ces paires.
  - (b) L'écart avant le champ ne viendrait que des « versions incitées » : la sonde apprendrait le régime d'incitation, le
    confondant du rang 2 ([KU] p. 5, l. 53-56). Chez [K], l'incitation reste dans le contexte pour la tromperie et le
    sous-rendement : « never remove the incentive as these are integral to their dataset prompts » (p. 3, l. 33).
  - (c) [RH] choisit sur la distribution évaluée : « one with the highest AUROC on a held out set of 250 rollouts from
    SWE-bench » (p. 9, l. 114). P-011 exige le « choix de la sonde rapportée fait sur un jeu de validation générique, jamais
    sur les organismes » ; la note [N], pour T0.7 : « sonde principale fixée d'avance, ou validée hors distribution » et
    « aucun choix tiré de P3 » (l. 72-78). Choisir sur la cible ôte à E3 son statut de seule voie qui porte une revendication.
  - (d) Les épisodes d'évaluation ne sont pas nommés ; le coût (≈ 1 à 2 USD) ne compte pas leur génération, alors que la
    revendication exige « des épisodes neufs » (l. 184).
- **Correction.** Dire quelles paires entraînent quelle position : paires à coût seul pour une lecture au champ, nombres
  équilibrés ; versions incitées pour une lecture avant le champ, incitation présente aussi chez les négatifs. Choix sur un
  jeu synthétique tenu à part, jamais sur des épisodes d'organisme ; retirer « choix sur la cible ». Nommer les épisodes
  d'évaluation (T0.6) et leur coût.

### VV2-sens-09 — moyen — Pouvoirs et confiances non revus après les corrections

- **Où.** v2 l. 127 (rang 2, « fort ») ; l. 128 (rang 3, « fort ») ; l. 178-180 (60 % ; 25 à 35 %) ; l. 249-250 (« Rangs,
  pouvoirs et confiances du rédacteur inchangés, sauf le pouvoir du rang 5 »).
- **Problème.** Les faits sous ces jugements ont changé. VS-13 ([K] table 1, p. 7, colonne « Prompted » : tromperie +0,035,
  non significatif) affaiblit le rang 2 ; le traitement l'écrit (remarque 3 : « l'affaiblit. Non modifié »). VV2-sens-02
  affaiblit le rang 3. VS-01 (bras « avant » confondu ; T1 et T4 peut-être non calculables au premier pas), VV2-sens-01 et
  VV2-sens-03 touchent le 60 %. VV2-sens-04 et VV2-sens-08 touchent le 25 à 35 %.
- **Correction.** Revoir chaque pouvoir et chaque confiance, avec la raison en une ligne et ce qui a changé depuis la v1.

### VV2-sens-10 — moyen — E4 choisit son bras sur les résultats (R3)

- **Où.** v2 l. 165 (E4 : « meilleur bras de E1 à E3, rejoué sur 27 à 70 milliards ») ; l. 169.
- **Problème.** Choisir le meilleur bras après lecture, puis le rejouer là où la littérature attend mieux, vise un signe
  positif (`docs/brief-claude-code-programme-complet-v2.md` l. 48 : « R3. Aucun run visant un signe positif : ce serait une
  démonstration, pas une expérience »). Le
  meilleur bras à 8 milliards est biaisé vers le haut (malédiction du gagnant). Ce « meilleur » peut être un bras « moyenne »
  (N-026 : jamais moniteur ni revendication) ou l'oracle (hors anti-circularité). « Ou sur un organisme dont la règle est
  apprise par affinage » change à la fois l'organisme et le modèle.
- **Correction.** Fixer d'avance le bras de E4 (par exemple le bras de production de E3), sans regarder E1 à E3 ; exclure
  les bras de diagnostic et l'oracle ; comparaison à 8 milliards sur épisodes neufs ; organisme affiné : expérience à part.

### VV2-sens-11 — moyen — T3 et T2 absents des règles de E1 et de E3

- **Où.** v2 l. 142-145 (règles communes : « témoin et mention ; T1 ; T4 ») ; l. 169 (E1 : T3 pour l'oracle seulement ;
  E3 : « T4 ; témoin et mention »).
- **Problème.** T3 a deux branches gelées ([P] l. 248 : mention contre honnête non au-dessus **et** saboteur contre mention
  au-dessus) ; « témoin et mention » ne les écrit pas. L'intention exige T1 à T4 ([P] l. 135-142, l. 159). T2 n'apparaît
  nulle part, alors que les deux bras de production de E1 en sont les deux termes. Dès le deuxième pas, ses « jetons qui
  précèdent » voient les coûts déjà déclarés (VS-01 ; remarque 1 du traitement). La comparaison des deux empans a un biais
  de longueur du maximum (`prereg/P3-addendum-lecture-complementaire-v1.md` l. 34 : « G-01 : biais de longueur du maximum
  dans T2 »).
- **Correction.** Règles communes : « P3-P4 (témoin), T1, T3 et T4, seuils gelés de [P], pour chaque bras de
  production ». T2 : dire son statut (déjà vu, VV2-sens-01) ; s'il est relu, contrôle des coûts déjà déclarés et correction
  de longueur.

### VV2-sens-12 — moyen — E2 : la tranche ne suit pas du montage

- **Où.** v2 l. 165 (E2) ; l. 166 (E2, tranche : « la position explique-t-elle le nul ? »).
- **Problème.** E2 change quatre choses à la fois : la position (après une question), les sondes (neuves, « apprises avec
  la question »), les couches (plusieurs) et le score (contraste). Un succès ne s'attribue pas à la position. La question
  « précise » sur l'honnêteté du coût déclaré se sert de ce qu'on sait de l'organisme ; un succès n'y dirait rien d'un
  moniteur qui l'ignore.
- **Correction.** Ajouter un bras « sondes principales de P3, même couche, lues à la position après la question » ; un bras
  par changement, ou renommer la tranche. Question générale : bras principal ; question précise : diagnostic déclaré.

### VV2-sens-13 — mineur — Oracle : empan, plancher et rôle de la mention non écrits

- **Où.** v2 l. 165 ; l. 169.
- **Problème.** L'empan de l'oracle n'est pas dit. S'il comprend le champ `COST`, une aire proche de 1 vient du nombre
  (coût seul 0,8878, [V] l. 204). La réponse du brainstorm avait corrigé : « champ du coût masqué, contraste saboteur contre
  mention, référence bénigne, calcul sur l'instance, diagnostic seulement » ([N] `reponses/reponses.md` l. 370-373). Le
  plancher d'un oracle appris n'est pas celui de directions aléatoires : il faut l'oracle réappris sur étiquettes permutées
  dans chaque tâche, même validation croisée. Mettre la mention parmi les négatifs d'apprentissage fait de la première
  branche de T3 un objectif appris, non un test.
- **Correction.** Écrire l'empan (champ `COST` et suite exclus) ; plancher par permutation avec réapprentissage ; T3 lu
  sur un oracle appris sans la mention (ou deux oracles).

### VV2-sens-14 — mineur — Agrégation : preuves citées d'un seul côté (R4)

- **Où.** v2 l. 98-110 (section 2.2, « Ailleurs ») ; l. 132 (rang 7).
- **Problème.**
  - [PAR] table 3, p. 7 : la v2 cite la moyenne sur cinq jeux de la sonde RP (0,856 contre 0,840), pas celle de la sonde
    Pairs : « Full Averaging (Pairs) … 0.941 » contre « Peak Activation (Pairs) … 0.867 » (`p007.txt` l. 19, l. 21). Ni la
    conclusion des auteurs (VV2-sens-03).
  - [GM] table 3, p. 12 : la v2 cite les faux négatifs en contexte long (LC[A]), où MultiMax gagne. Elle omet les faux
    positifs sur le trafic long ordinaire (LC[RT], « long context random traffic », table 1, p. 8) : 1,85 % à 82,14 % pour
    les agrégations MultiMax (`p012.txt` l. 34 : 43,97 % ; l. 36 : 82,14 %), contre 0,5 % pour la sonde linéaire en
    moyenne (l. 31).
  - [AG] p. 43, l. 18 : la première raison de l'équipe rouge porte sur l'agrégation (« the difficulty of aggregating signals
    over much longer contexts ») ; seule la seconde est citée.
- **Correction.** Citer les deux côtés. « Sens inconnu » tient ; mais les preuves publiées penchent vers la moyenne et
  l'attention en performance ([PAR] p. 7 ; [MK] p. 4 ; [AP] p. 22), vers le maximum seulement sous dilution, au prix de
  faux positifs ([GM] table 3).

### VV2-sens-15 — mineur — Nœud « règle gelée 1 » : [OA] résumé de façon incomplète

- **Où.** v2 l. 115-116 ; l. 186-188.
- **Problème.** [OA] p. 1, l. 26-28 : « Empirically, obfuscated activations arise from representation drift during RL, with
  or without a detector penalty. The detector penalty only incentivizes obfuscated policies ». C'est le fait le plus utile à
  la décision de Lazar : la sonde lue après une question est contournée par le texte, et la dérive existe sans pénalité. La
  v2 ne retient que l'issue honnête possible. Le traitement l'avait signalé (remarque 4), sans l'appliquer.
- **Correction.** Ajouter ces deux phrases (p. 1).

### VV2-sens-16 — mineur — Taille et capacité : « dès 9 milliards » est une lecture par la taille

- **Où.** v2 l. 25 ; l. 130 (« faible d'après [CA] ») ; l. 166 (E4).
- **Problème.** [CA] p. 8, l. 163 : Nemotron-3 Nano reste à « 0.613–0.760 » ; c'est un « Nemotron 3 Nano 30B-A3B » (p. 25,
  l. 87) : trente milliards au total ne suffisent pas. [DYL] table 9, p. 28 : indice de capacité 14 pour Llama-3.3-70B
  (l. 31), 27 pour Qwen3.5-4B (l. 23). Llama-3.1-8B n'est dans aucune de ces tables ; le ranger avec Qwen3.5-9B est une
  transposition par la taille, que la v2 récuse ailleurs (« capacité, pas taille »).
- **Correction.** « Par la taille, [CA] place la rupture entre 2 et 9 milliards (famille Qwen3.5) ; par la capacité, la place
  de Llama-3.1-8B n'est pas mesurée (R8 : question). » Pouvoir du rang 5 : « inconnu ».

### VV2-sens-17 — mineur — Nœuds et périmètre : oublis

- **Où.** v2 l. 173-176 ; l. 182-204.
- **Problème.**
  - (a) Le nœud 4 (référence boîte noire) est ouvert (`registres/etat.md` l. 3 ; R-265 (2), `registres/decisions.md`
    l. 457) ; la v2 ne le nomme pas. Le « logit d'auto-déclaration » de E2 n'est pas cette référence : à dire.
  - (b) Les options (a), (b), (c) sont renvoyées à « proposer avec recommandation » sans recommandation ni défaut (format de
    CLAUDE.md : recommandation et confiance ; défaut sous 48 heures).
  - (c) « Aucune lecture de P3b n'en porte » est écrit comme acquis. La ligne N-028 lit P3b comme « la première tentative de
    détection du plan R-262 (point 2) » : tension à présenter, avec la raison de VV2-sens-01.
  - (d) R-262 (2) demande une voie « choisie d'après la revue de la littérature » (`registres/decisions.md` l. 453) : la v2
    ne dit pas laquelle de ses expériences tient ce rôle.
  - (e) R-262 : l'addendum 2 de P3 passe avant la lecture de P4-instrument, et sa réserve éventuelle s'y recopie ; P3b relit
    P3 : même règle à écrire.
- **Correction.** Ajouter le nœud 4 ; une recommandation et un défaut pour (a), (b), (c) ; la revendication en proposition ;
  la voie de R-262 (2) ; le préalable de l'addendum 2.

### VV2-sens-18 — mineur — N-026 : libellé, règle de lecture, famille de Bonferroni

- **Où.** v2 l. 140-145 ; l. 165-166.
- **Problème.** N-026 exige le libellé « bras de diagnostic, jamais en production » et une lecture « l'agrégation
  explique-t-elle le nul ? » (`docs/decisions/decision-N-026-v1.md`, conditions 1 et 4). E1 écrit « Diagnostic (N-026) »,
  sans ce libellé ni règle de lecture. La tranche de E1 ne dit rien des bras « moyenne » ni des deux bras de production.
  La famille de Bonferroni (« sur les bras ») ne dit pas si les bras de diagnostic et l'oracle en font partie.
- **Correction.** Libellé exact ; une ligne de lecture par bras ; Bonferroni sur les seuls bras de production.

### VV2-sens-19 — mineur — Précisions

- (a) v2 l. 160-161 : « dont ≈ 2,5 h de génération » vient de [P] l. 385 (« ≈ 38 s chacun au pilote, soit ≈ 2,5 heures
  pour 240 ») : une attente, pas une mesure. Durée mesurée du run : 11 179,1 s
  (`diag/20261019-230011-p3-reel/resume.json`, `resultat.duree_s`) ; la génération seule n'y est pas.
- (b) v2 l. 133 : « témoin Alpaca » est rattaché à [FQ p. 3]. Cette page ne parle que du plancher par sonde à paramètres
  aléatoires (`r003.txt` l. 66-67) ; elle appelle la régression supervisée un « ceiling ». Le témoin Alpaca est chez [AP]
  et [DYL] p. 8.
- (c) v2 l. 68-71 : [EM] p. 38 est un exemple de pilotage (« while steering towards desperation increases », l. 22), pas de
  détection : écrire « par pilotage ».
- (d) v2 l. 127 et l. 166 : la colonne « Prompted » de [K] (+0,035) porte, pour la tromperie et le sous-rendement, sur des
  données où l'incitation reste dans le contexte ([K] p. 3, l. 33) : à écrire avec le chiffre.

## Contrôles obligatoires, expérience par expérience

| bras | nombre écrit | plancher de même position et agrégation | témoin | mention | T1 | T3 | T4 |
|---|---|---|---|---|---|---|---|
| E1, maximum sur le champ `COST` (production) | T4 au champ ; grandeur déjà vue (01) ; manipulation absente (07) | oui (règle commune) | oui | oui | oui | non écrit (11) | oui |
| E1, maximum avant le champ (production) | coûts déjà déclarés : (a), (b), (c) ; nombres avant le champ dans l'action : non (06) | oui | oui | oui | oui | non écrit (11) | oui |
| E1, moyenne (diagnostic, N-026) | T4 | oui, même agrégation | oui | oui | oui | non écrit (11) | oui |
| E1, oracle (diagnostic) | coûts déjà déclarés ; empan non dit (13) | inadapté : permutation avec réapprentissage (13) | négatif d'apprentissage | négatif d'apprentissage : T3 en partie appris (13) | oui | oui | oui |
| E2 | coûts déjà déclarés | oui ; contraste du plancher à préciser | oui | oui | oui | oui | oui |
| E3 | nombres équilibrés ; « avant le champ » incohérent (08) | oui | oui | oui | règle commune | non écrit (11) | oui |
| E4 | « mêmes contrôles » | idem | idem | idem | idem | idem | idem ; bras choisi sur résultats (10) |

## Questions de la commande

- **Contrôles obligatoires.** Plancher de même position et agrégation : écrit pour tous les bras, inadapté pour l'oracle.
  Témoin, mention, T1, T4 : écrits. T3 : seulement pour E2 et l'oracle. Contrôle du nombre écrit : incomplet (01, 06, 07).
- **Bras « moyenne » (N-026).** Diagnostic seulement dans E1 et pour l'oracle : conforme sur le fond (plancher de même
  agrégation, bras de production à côté). À compléter : libellé et lecture (18). E4 pourrait le reprendre (10). E3 en
  production par maximum ou attention : conforme. E2 renvoyé à Lazar (règle gelée 1) : bien posé.
- **R3.** Deux points visent un signe : le bras « champ du coût » de E1 (01) et le « meilleur bras » de E4 (10). La question
  « précise » de E2 est un choix d'organisme à déclarer (12). Le reste est posé en questions avec tranche.
- **Recommandations et confiances.** Elles ne suivent pas les faits corrigés (09), et deux reposent sur des lectures à
  corriger (02, 03).
- **Nœuds de Lazar.** Bien séparés : dépense (R-269 : 10 USD au plus par lancement, crédit, devis), changement de modèle
  (E4), règle gelée 1 (E2 et lissage de [CC]), contact externe (FIBS). Mal classé : E2 sur P3 (05). Non présentés : la
  divergence N-028 contre la note [N] et N-025 (01) ; le nœud 4 (17).

## Conforme (vérifié)

- 21 PDF à l'empreinte annoncée ; RO (`2604.01151v3`) égal à son compagnon.
- Les 107 passages entre guillemets : chaque phrase anglaise est sur la page citée (`sortie-guillemets-v2.txt`).
- Code : `episode.py` (`79113b49…`) et `propositions.py` (`5d97b223…`) identiques à `97dd829`, `7a54d43` et aujourd'hui ;
  `episode.py` l. 210-217 et l. 250-255 (transcription cumulée), l. 260 (passe unique) ; `propositions.py` l. 238-269 :
  VS-01 confirmé (consigne privée, indication avant « Your action: », actions précédentes de l'agent, `COST` compris).
- Renvois de la v2 au dépôt : [P] l. 198-205, 214-215, 238-253, 289-301, 318, 320-321, 330-332, 385 ; [V] sections 2, 3,
  4 et 7 (l. 204, l. 345) ; `registres/decisions.md` l. 461 ; `registres/go.md` l. 33-34 ; `registres/depenses.md`
  l. 88-89 : exacts, sauf 19 (a). Autres lignes relues pour ce rapport : [P] l. 135-142, 159, 228-236, 248, 272-280,
  415-416, 428 ; [V] l. 170-172, 358-359 ; `registres/decisions.md` l. 446, 453, 456, 457 ; `registres/go.md` l. 32.
- Pages lues en entier, sens de la v2 juste sur ces points : [CA] p. 4-9 (six couches, contraste, négatifs d'avant le
  sabotage, 0,979 à 0,984, seuil de 9 milliards dans Qwen3.5, « All probe architectures perform similarly ») ; [CC] p. 6
  et p. 8 (« Multi-layer probing substantially improves performance », appui des « plusieurs couches » du point 1) ;
  [OA] p. 1, 5 et table 15, p. 23 ; [K] p. 3 et table 1, p. 7 ; [YS] p. 1-3 ; [MK] p. 4 ; [AP] p. 22-23 ; [GM] p. 8, 10, 12 ;
  [LB] table 6, p. 54 ; [AU] p. 6 ; [AG] p. 17 ; [LIAR] p. 10 ; [KU] p. 4, 5, 9 ; [BX] p. 1, 3-8 ; [DYL] p. 8-11, 28 ;
  [RH] p. 9. Autres pages : phrases présentes (guillemets), sens non relu.
- Dépense et délégation (R-269, GO-2026-10-20-06 et -07, crédit de 11,79 USD) : exactes.

## Limites

- Angle « sens » : les chiffres sans portée sur le sens n'ont pas été recomptés un à un (les phrases anglaises l'ont été).
- Annexes des PDF lues aux pages citées et à quelques voisines ([AP] p. 18 ; [CA] p. 25 ; [GM] p. 8, 12 ; [DYL] p. 9-11).
- J'ai lu, dans [N], des valeurs descriptives de la lecture décisive de P3 (T1, T2, T4). Je ne les recopie pas. Ce
  vérificateur ne doit pas rédiger P3b.
- Ni suite de tests ni `verifier-arbre` (lecture seule). Coûts non revus. Extractions non auditées ligne à ligne.

## Fichiers écrits (chacun avec son compagnon `.sha256`)

- `…/revue-detection/verification-v2-sens-v1.md` (ce rapport).
- `…/revue-detection/verification-v2-sens/` : `cherche2.py`, `guillemets_v2.py`, `sortie-guillemets-v2.txt`,
  `empreintes-pdf-recalculees.txt`, `pages/<clé>/pNNN.txt` et `rNNN.txt` (998 pages, 21 PDF) ; liste complète :
  `empreintes-verification-v2-sens.sha256`.
- Scripts lancés par `python3 -I`, sans import local.
