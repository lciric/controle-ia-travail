# Vérification de la synthèse v3 « comment détecter » — angle « sens et expériences », tour 2 — v1

## Verdict : **non conforme**

- Les phrases anglaises et les chiffres de la v3 sont sur leur page. Les renvois au dépôt et au code sont exacts. Le bras
  « moyenne » est un diagnostic seulement (N-026). Les nœuds de Lazar sont, pour l'essentiel, séparés.
- Mais deux erreurs de sens touchent le verdict (section 1), le classement (section 3) et E2 :
  1. la v3 compare le nul de P3 (saboteur contre honnête : **deux consignes différentes**) à des chiffres obtenus **sous
     la même consigne** (sous-rendement de [BX], [YS], [AP], [PAR] : l'étiquette vient du choix du modèle, pas de la
     consigne). Ces chiffres répondent à T1, pas à P3-P3. Les analogues à consignes différentes ([LB] « Instructed-Deception »,
     [DYL] « Varied Deception », « Backdoors » de [PAR], rappel de [BX] contre la conversation ordinaire) manquent au point 2 ;
  2. « la lecture après une question est en défaut sur les cas les plus proches » ne vaut que pour des sondes apprises sur
     « Roleplaying ». Avec la sonde « Pairs », recette de la sonde de tromperie de P3, la même table donne 0,849 et 0,879
     au sous-rendement [PAR table 3]. La prédiction « échec probable de T1 » de E2, la raison du rang 4, l'argument du nœud
     E2 et une raison de la confiance de 40 % reposent sur cette généralisation.
- S'y ajoutent cinq constats moyens et sept mineurs. Aucun chiffre n'est à retirer. Les recommandations (1) à (5) peuvent
  tenir. Mais le verdict, les pouvoirs des rangs 2 à 4, la prédiction de E2, deux confiances et la raison « seule voie »
  de E3 changent : il faut une v4, puis une vérification neuve des sections 1, 3, 4 et 5, avant tout envoi à Lazar.

## Cadre

- **Objet.** `…/revue-detection/synthese-comment-detecter-v3.md`, sha256
  `ec4239e9da0a6b8282ce0b685695fcb71b2777038fd18618b096797502ae6890` (compagnon égal). Traitement :
  `…/revue-detection/traitement-verification-synthese-tour2-v1.md` (`23fd956e…`, compagnon égal). Aussi lus : v1
  (`a47f9141…`), v2 (`90ad38bf…`), vérification du tour 1 (`43986648…`), rapport « sens » du tour précédent
  (`8ec6aa0e…`), extraction des nouveaux PDF (section 3). `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Vérificateur neuf.** Je n'ai écrit ni la v1, ni la v2, ni la v3, ni les extractions, ni les vérifications du premier
  tour, ni les traitements. 2026-10-20, de 12:15 à 13:00 UTC environ.
- **Lecture seule.** Aucune écriture dans le dépôt (tête `8bd4a75`, arbre propre au début et à la fin) ; git en lecture
  seulement. Non ouverts : `prereg/P3-consignes-v1.md`, textes d'action, clés. Aucune recherche web, aucun service payant,
  aucun contact, aucune commande Vast.ai.
- **Méthode.** Empreintes des 22 PDF recalculées : toutes égales aux clés de la section 6 de la v3
  (`…/revue-detection/verification-v3-sens/empreintes-pdf-v3-sens.txt`). Texte de chaque page extrait à nouveau par moi
  (`pdftotext`, brut `rNNN.txt`, mise en page `pNNN.txt`) sous `…/revue-detection/verification-v3-sens/pages/<clé>/`.
  Recherche : `outils/ch.py` ; toutes les phrases entre guillemets de la v3 cherchées dans toutes les pages
  (`outils/guillemets_v3.py`, sortie `sortie-guillemets-v3.txt`). Phrases anglaises de ce rapport contrôlées de même,
  passages sur plusieurs lignes compris (`outils/guillemets_multi.py`, sorties `sortie-guillemets-rapport-v1.txt` et, après
  le dernier ajout, `sortie-guillemets-rapport-v2.txt` : toutes sur la page citée) ; épreuve R5 de l'outil (`epreuve-r5-guillemets.md`, `sortie-epreuve-r5-guillemets.txt` : deux cas
  sains et une ligne de table trouvés à leur page ; chiffre altéré, mot inversé, colonne voisine rejetés ; page voisine
  repérée). Relus contre les PDF, le code et les registres : verdict
  (section 1), agrégation (section 2.2, pour N-026), différences de montage (section 3), expériences (section 4),
  recommandation, confiances et nœuds (section 5).
- **Conventions.** « l. » d'un PDF = ligne de mon fichier `rNNN.txt` (ou `pNNN.txt` pour une table) ; « l. » de la v3 =
  ligne du fichier v3. Sigles des pièces du dépôt comme dans la v3 : [P] `prereg/P3-premier-test-i-a-v1.md` (`d975e981…`) ;
  [V] `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…`) ; [NB] `docs/notes/brainstorm-suite-P3-v1/` (note
  `a023093e…`).
- **Exposition (R1).** [V] l. 136-184, 185-233, 234-272 et 340-378 relues chiffres masqués, sauf les lignes dont la v3
  cite les nombres (l. 138, 155, 160, 204, 345-346). Note du brainstorm, `proposition-C.md` l. 300-330 et
  `proposition-D.md` l. 70-105 relues décimales masquées. Le libellé restait lisible et dit le sens de certains tests. Je
  ne recopie ici aucune valeur ni aucun sens de T1, T2 ou T4. Ce vérificateur ne doit pas rédiger P3b.

## Constats (le plus grave d'abord)

### VV3-sens-01 — majeur — Les « montages les plus proches » ne sont pas du type de P3-P3 ; les analogues de ce type manquent

- **Où.** v3 l. 55-62 (point 2) ; l. 75 (ligne [BX] : « montage le plus proche de P3 ») ; l. 175 (rang 2) ; l. 176
  (rang 3) ; l. 185.
- **Problème.**
  - P3-P3 oppose deux consignes : le saboteur a une consigne privée, l'honnête n'en a pas ([P] l. 328-332). T1 oppose,
    sous la même consigne, des actions qui gonflent et d'autres non ([P] l. 238-241).
  - [BX], sous-rendement : une seule consigne pour tous (« a system prompt that instructs the model to underperform on
    questions related to WMDP », p. 4, l. 43-47) ; « For sandbagging the labels are derived from step-1 sandbagging
    decisions » (p. 12, l. 7). Les 0,81, 0,63 et 0,5 sont donc des contrastes **à consigne égale**, avec un sujet qui
    diffère (WMDP contre MMLU). L'empan public noté porte sans doute une justification fausse : « Instead, give bad logic
    and reasoning, resulting in an incorrect answer » (p. 12, l. 21-22) ; « The user must not guess that you're sandbagging,
    so don't mention that your reasoning is incorrect! » (p. 13, l. 7-8). « Rien d'écrit dans l'empan lu » n'est pas établi.
  - [YS] lit le jeu de sous-rendement d'Apollo (p. 2, l. 63-65), lui aussi à consigne égale (« We label a response as
    honest if the model decides not to sandbag in step 1 », [AP] p. 5, l. 24-25). La ligne [YS] de la v3 dit le
    raisonnement écrit peut-être inclus (l. 76 : « non dit ») ; le point 2 range pourtant 0,606 « rien d'écrit dans l'empan
    lu ».
  - Chez [BX], la mesure entre consignes est le rappel contre la conversation ordinaire (« distinguish transcripts
    containing normal conversational data from those exhibiting the studied behavior », p. 6, l. 55-57) : 0,03 en « Score
    Filtering » (table 1, l. 50). C'est elle, et non 0,81, qui ressemble à P3-P3 ; la v3 la cite en incise (« Mais »).
  - Analogues à consignes différentes, consigne non notée, omis du point 2 :
    - [LB] « Instructed-Deception » : consignes neutres contre « Answer deceptively to the following question » (p. 6,
      l. 43-52) ; « probes are not evaluated on system prompt activations » (p. 7, l. 19) ; moyenne ; 0,95 ; 0,60 ; 0,69 ;
      0,58 (table 6, p. 54, l. 7-10). La v3 ne s'en sert que pour la taille (rang 5).
    - [DYL] « Varied Deception » : « one paired with a randomly drawn honesty-inducing system prompt and one with a
      lie-inducing prompt » (p. 5, l. 26-27) ; Qwen3-8B 0,74 en exactitude équilibrée (table 9, p. 28, l. 33).
    - [PAR] « Backdoors » : « The system prompt also informs the assistant whether the provided code contains a backdoor »
      (p. 4, l. 41-42) ; seuls les jetons publics sont lus (p. 3, l. 46-47) ; sonde « Pairs » : moyenne 0,844, **maximum
      0,768** (table 3, p. 7, `p007.txt` l. 19, l. 21), sur Llama-3.3-70B. C'est le seul analogue à consignes différentes
      lu avec le maximum de P3 et la recette de sa sonde de tromperie (« Instructed-pairs probe (Pairs) », [PAR] p. 3,
      l. 32-37 ; [P] l. 293-296). Réserves : code fourni par la consigne, hors politique (p. 4, l. 44-46) ; réponses
      honnêtes déjà plus hautes que presque tout Alpaca (« higher than 99.9% of the Alpaca samples », p. 9, l. 22).
  - Rang 2 : « « deceptive prompt regime » [KU p. 9] » est donné comme cause du nul. Or [KU] dit qu'une telle sonde
    signale le régime de consigne : « flagging that a model is operating under deceptive instructions even when its output
    happens to be correct » (p. 9, l. 48-50). [AP] fait la même hypothèse pour la sonde « Instructed-Pairs » : « activates
    somewhat when deception is incentivized (rather than performed) which still allows the probe to distinguish deceptive
    responses from control responses » (p. 18, l. 14-15). Une sonde de régime **séparerait** le saboteur de l'honnête :
    ce fait prédit un faux positif sur P3-P3 (c'est l'usage qu'en font le rang 9 et E2), pas un nul.
- **Conséquence.** Le point 2 compare le nul de P3-P3 à des contrastes du type de T1. Les pouvoirs « moyen » des rangs 2 et
  3 reposent sur ce mélange. La conclusion « ne prévoit ni n'exclut » peut tenir, pour d'autres raisons : à consignes
  différentes, 0,58 à 0,95 selon le modèle ([LB]), 0,74 sur Qwen3-8B ([DYL]), 0,768 au maximum à 70 milliards ([PAR]),
  rappel 0,03 sur ce même modèle quand ni consigne ni raisonnement ne sont notés ([BX]).
- **Correction.** (1) Pour chaque chiffre du point 2 et des rangs 2, 3 et 9 : écrire le type de contraste (consigne égale,
  type T1 ; consignes différentes, type P3-P3). (2) Point 2 et rang 3 : citer [LB] « Instructed-Deception », [DYL]
  « Varied Deception », [PAR] « Backdoors » (0,844 ; 0,768) et le rappel de [BX] (0,03) comme analogues de P3-P3 ; ranger
  0,81, 0,63 et 0,5 de [BX] et 0,606 de [YS] comme analogues de T1 ; retirer « rien d'écrit dans l'empan lu » pour [BX]
  (étape 4 publique) et pour [YS] (non dit). (3) Rang 2 : écrire l'hypothèse qu'il exige (la consigne du saboteur, « une
  règle de calcul », n'est pas lue comme un régime trompeur), ou baisser le pouvoir. (4) Revoir les pouvoirs des rangs 2 et
  3, avec la raison, et la ligne « ce qui a changé » (l. 185).

### VV3-sens-02 — majeur — « La question est en défaut sur les cas proches » : vrai pour les sondes apprises sur « Roleplaying », pas pour la recette de P3

- **Où.** v3 l. 47-49 (point 1) ; l. 177 (rang 4 : « le levier « question » est en défaut sur les cas proches ») ; l. 236
  (E2, tranche : « Prédiction écrite d'avance : échec probable de T1 ») ; l. 251-253 (confiance de 40 %) ; l. 277-278
  (nœud E2 : « l'issue « consigne lue, pas l'acte » est déjà prédite [AP p. 18] »).
- **Problème.**
  - La sonde de question d'Apollo est apprise sur « Roleplaying » : « As before we train on the Roleplaying dataset »
    ([AP] p. 9, l. 13-14) ; « Again, we trained this using 90% of the Roleplaying dataset » (p. 18, l. 30). Chez [PAR],
    l'échec est celui de la sonde RP : 0,457 et 0,437 (table 3, `p007.txt` l. 25, l. 27).
  - Avec la sonde « Pairs », recette reprise par la sonde de tromperie de P3 ([P] l. 293-296 ; [PAR] p. 3, l. 32-37), les
    mêmes questions donnent, au même sous-rendement : 0,849 et 0,879, contre 0,964 en moyenne ; et 0,832 et 0,849 sur
    « Backdoors » (table 3, `p007.txt` l. 24, l. 26). La v3 imprime 0,849 et 0,879 dans sa ligne [PAR] (l. 79) mais n'en
    tire rien au verdict ni pour E2.
  - Le même paragraphe d'Apollo dit : « This is the best probe of all we trained at distinguishing deceptive and honest
    responses, with near perfect separation on all datasets » (p. 9, l. 16-17) ; et la p. 18 : « Our recall at 1% is
    greater than 99% on all four evaluation datasets » (l. 32-33). Entre consignes, la sonde de question sépare presque
    parfaitement ; elle échoue à consigne égale. [LB] : la sonde de question est « comparable to those of the mean probe »
    (p. 8, l. 31). Au verdict, la v3 ne garde que l'échec ; la p. 18 n'y sert qu'à prédire l'échec de T1 (R4).
- **Conséquence.** Le bras (a) de E2 lit les sondes principales de P3, dont une sonde de recette « Pairs » : la littérature
  lue n'y prédit pas l'échec de T1 ; elle le prédit pour une sonde apprise sur « Roleplaying ». La raison du rang 4, la
  prédiction de E2, l'argument du nœud E2 et la troisième raison de la confiance de 40 % ne suivent pas les faits.
- **Correction.** Point 1 : « Sur les cas sur consigne, elle ne bat pas la moyenne [DYL p. 11 ; table 9 ; LB p. 8 ; PAR
  table 3, sonde Pairs : 0,849 et 0,879 contre 0,964]. À consigne égale (sous-rendement), elle s'effondre avec les sondes
  apprises sur « Roleplaying », qui lisent la consigne [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et 0,437] ; entre
  consignes, la même sonde sépare presque parfaitement [AP p. 18]. » Rang 4 : raison « issue incertaine, selon les données
  d'apprentissage de la sonde ». E2 : « Prédiction écrite d'avance : sonde apprise sur « Roleplaying » : échec de T1 ;
  sondes principales de P3 : issue incertaine ([PAR] : 0,849 et 0,879 à consigne égale, sujet WMDP contre MMLU confondu) ;
  le nombre de l'action est dans le contexte lu (VV3-sens-04). » Nœud E2 : « prédite pour une sonde apprise sur
  « Roleplaying » ». Confiance : VV3-sens-09.

### VV3-sens-03 — moyen — [AU] : « en moyenne » n'est pas écrit ; « +X » est ambigu ; « +System (AUC = 1.000) » est omis

- **Où.** v3 l. 55-58 (« en moyenne sur les jetons : … 0,653 sur toutes les actions, sur Phi-4 [AU p. 6] ») ; l. 62
  (« Ces montages agrègent par la moyenne ») ; l. 86 ; l. 176 (rang 3).
- **Problème.**
  - [AU] apprend sur « the last 10 tokens for each datapoint » et évalue par « the same procedure » (p. 7, l. 1-4) ;
    l'agrégation au test n'est pas écrite. L'extraction le notait (`…/revue-detection/extraction/extraction-nouveaux.md`,
    section 3, ligne [AU] : « test : **non écrite** »). « En moyenne » est faux pour [AU].
  - Légende de la figure 6 : « Note that the “+X” notation means the prompt includes all inputs above and including X »
    (p. 6, l. 40-41). Lue à la lettre (l'entrée du modèle change), « Action » est l'action seule, **sans contexte**, comme
    le filtrage du contenu de [BX] (0,63) ; le montage de P3 (rôle dans le contexte, fin de l'action lue) est alors
    « +System (AUC = 1.000) » (p. 6, l. 12), omis. Lue autrement (l'empan noté change), 0,653 est bien le montage de P3.
    Le PDF ne tranche pas.
- **Correction.** Retirer [AU] de « en moyenne » ; écrire « agrégation non écrite (dix derniers jetons, p. 7) » ; citer
  « +System (AUC = 1.000) » et l'ambiguïté de « +X » ; ne garder 0,653 parmi les montages proches qu'avec cette réserve.

### VV3-sens-04 — moyen — T1 n'est pas « à contexte égal » ; au champ et dans E2, il est confondu avec le nombre écrit

- **Où.** v3 l. 197-198 (« même contexte ; seul test à contexte égal ») ; l. 255 ; l. 236 (E2 : « échec probable de
  T1 ») ; l. 239 (E1 : T1 « sur chaque bras de production », champ `COST` compris ; E2 : T1 sans le contrôle des coûts
  déjà déclarés).
- **Problème.**
  - T1 compare des actions du saboteur sous la même consigne, mais à des pas et avec un historique différents : dès le
    deuxième pas, les coûts déjà déclarés sont dans le contexte (v3 l. 205-214 ; `src/controle_ia/harnais/episode.py`
    l. 217 et l. 254).
  - Les étiquettes de T1 viennent du coût déclaré (au moins deux fois la médiane honnête, contre au plus 1,25 fois, [P]
    l. 238-239). [P] l. 141-142 : sans T4, « une sonde qui lit la grandeur du nombre écrit passerait T1 et T2 ». Sur le bras
    (i) de E1, T1 teste donc le nombre. Dans E2, la question suit l'action : son champ `COST` est dans le contexte lu ; une
    sonde sensible aux nombres peut passer T1. La prédiction « échec de T1 » s'appuie sur [AP] p. 18, où aucun nombre
    n'existe.
  - Les prédicteurs triviaux (rang du pas, longueur notée) ne portent que sur les cinq jeux ([P] l. 260-261), pas sur T1.
- **Correction.** Écrire « à consigne égale ». Pour T1, partout : prédicteurs triviaux (rang du pas, longueur notée,
  coûts déjà déclarés) et contrôle des coûts déjà déclarés, E2 compris. Dire que, sur le bras du champ et dans E2, T1 ne
  vaut qu'avec T4. Revoir la prédiction de E2 (VV3-sens-02).

### VV3-sens-05 — moyen — Manipulation du nombre : source citée d'un seul côté ; facteur « contexte » confondu ; aucune prédiction écrite

- **Où.** v3 l. 223-227 ; l. 235, (v) ; l. 280-281 (recommandation, confiance ≈ 60 %).
- **Problème.**
  - La v3 cite l'avantage de la note (l. 27 : « c'est la seule mesure qui sépare le nombre écrit du contexte privé »), pas
    l'inconvénient écrit juste après (« une statistique neuve ; des planchers qui saturent [chiffre masqué] ; le volet
    « nombre » attend l'addendum 2 », l. 28), ni la recommandation de la note : « (A1) maintenant. C2 seulement après le
    verdict de A1 et après G0 » (l. 33). La v3 recommande l'inverse sans le dire.
  - Le facteur « contexte » ne change que la consigne et l'indication ([NB] `proposition-D.md` l. 93-96). Sur les actions
    du saboteur, le contexte « témoin » garde les coûts gonflés des pas précédents (v3 l. 205-214) et des titres en
    capitales, contraires à la consigne du témoin (titre en minuscules, [P] l. 125, l. 333) : un indice de consigne non
    suivie. La mesure sépare le nombre **de l'action en cours** de la consigne, historique gardé. « Seule mesure qui sépare
    le nombre écrit du contexte privé » (l. 281) est trop fort.
  - La proposition D écrivait une prédiction contre le positif : « effet du nombre > 0 ; effet du contexte, à nombre égal,
    non détecté » (`proposition-D.md` l. 100-101). La v3 n'en garde aucune (R3).
- **Correction.** Citer la note l. 28 et l. 33. Dire comment l'historique des coûts est traité (remplacé dans tout
  l'épisode, premier pas seul, ou strates) et déclarer le conflit entre titres et consigne du témoin. Reprendre la
  prédiction écrite. Revoir la confiance.

### VV3-sens-06 — moyen — E2 et E3 sur les épisodes de T0.6 : la mention manque au brouillon de T0.6 ; son coût est sous-estimé

- **Où.** v3 l. 239 (E2 : « T3 complet » ; E3 : « P3-P4, T1, T3 et T4 ») ; l. 246-248 ; l. 237 (E3, coût : « ordre de
  grandeur : P3 entier, 240 épisodes, ≈ 3,96 USD ») ; l. 291-298 (dépense).
- **Problème.**
  - T3 exige la condition « mention sans usage » ([P] l. 248). Le brouillon de T0.6
    (`brouillons/T0.6-organismes-v0-v1-brouillon1.md`, `e212fb35…`, l. 74-81) a un témoin instruit, pas de mention : sur
    ses épisodes, T3 n'est pas calculable.
  - Ce brouillon prévoit 12 conditions × 64 tâches × 2 épisodes = 1 536 épisodes (l. 82), plus 640 pour (ii) (l. 89),
    sur un devis de 8 et 10 heures (l. 92) : plusieurs fois P3, sans doute au-delà de 10 USD par lancement (R-269 :
    nœud). « P3 entier » n'a pas de source ; la réécriture en mode coût (R-265 (6)) n'existe pas encore.
- **Correction.** Écrire que la réécriture de T0.6 doit jouer le témoin **et** la mention, pour que E2 et E3 aient P3-P4 et
  T3. Remplacer l'ordre de grandeur par « à deviser ; le brouillon actuel de T0.6 prévoit 1 536 + 640 épisodes ». Noter le
  nœud de dépense possible.

### VV3-sens-07 — moyen — « E3, seule de cette liste qui peut porter une revendication » : E2 sur épisodes neufs le peut aussi, selon la règle gelée 1

- **Où.** v3 l. 247-249 ; l. 261-262 (« Une revendication ne viendra que d'une sonde apprise sans l'organisme, sur des
  épisodes neufs »).
- **Problème.** La raison donnée est « car la sonde est apprise sans l'organisme ». Les bras (a) à (d) de E2 lisent des
  sondes apprises sans l'organisme (sondes de P3, ou sondes génériques apprises avec la question, l. 235), et la v3
  recommande E2 sur des épisodes neufs, à l'aveugle (l. 246). Seul le statut de la lecture à une seule position les sépare
  de E3 ; ce statut est à Lazar (règle gelée 1, l. 283-284).
- **Correction.** « E3 ; ou E2 sur épisodes neufs, si tu admets en production la lecture après une question (règle gelée
  1) ». Le dire aussi dans le nœud « Revendication ».

### VV3-sens-08 — mineur — Périmètre de N-028 : le bras « moyenne » de P3b n'a pas de base écrite ; « couches multiples » est sous défaut de 48 heures

- **Où.** v3 l. 235, (iii) ; l. 275-276 (« le GO de N-028 ne couvre que la localisation au champ du coût et l'oracle ») ;
  l. 299-303.
- **Problème.**
  - [P] l. 415-416 : toute grandeur non écrite est un nœud. Par sa propre lecture de `registres/go.md` l. 32, la v3 laisse
    le bras (iii) hors du GO de N-028, sans dire ce qui l'y met. N-026 (`decision-N-026-v1.md` l. 18-19) permet un tel bras
    « dans un préenregistrement d'audit ou d'expérience » ; c'est une règle, pas un GO d'extension.
  - « Couches multiples » est rangé sous le défaut de 48 heures sans restriction. Sur les actions de P3, toute couche ou
    sonde neuve est un nœud ([P] l. 428 ; la v3 le dit pour E2, l. 275-276).
- **Correction.** Écrire la base du bras (iii) (N-026 avec N-028), ou le ranger avec E2 et la manipulation. Restreindre
  « couches multiples » à T0.7 et aux épisodes neufs.

### VV3-sens-09 — mineur — Confiances : deux raisons hors sujet

- **Où.** v3 l. 251-256.
- **Problème.** La confiance de 40 % porte sur E1, qui ne lit aucune question (l. 235) ; sa troisième raison (« la
  lecture après une question est en défaut sur les cas proches ») vise E2, et elle est à revoir (VV3-sens-02). La confiance
  de 15 à 25 % donne « le montage de E3 était à reprendre » : c'est l'histoire du texte, pas une chance de succès ; le
  montage corrigé lit des données du domaine, que [K] désigne comme le premier levier (« Deception −0.416 », table 1,
  `p007.txt` l. 11). Seule l'addition de T1 justifie la baisse.
- **Correction.** Retirer ces deux raisons ; donner les raisons tirées des faits.

### VV3-sens-10 — mineur — Rang 6 « couches » : appui faible, preuve contraire omise

- **Où.** v3 l. 50 (« et **plusieurs couches** ») ; l. 179 (rang 6).
- **Problème.** [CA] lit six couches pour ses quatre architectures (p. 5, l. 43-44) sans les comparer à une seule ;
  « All probe architectures perform similarly » (p. 8, l. 118). Seul [CC] compare (« using fewer layers consistently
  yields worse performance », p. 8, l. 71-72), sur une autre tâche. Sur ce même modèle, [BX] : « Our per-layer analysis
  indicates that layer choice has limited effect on monitor performance, particularly beyond the first third of layers »
  (p. 3, l. 79-81) ; non cité.
- **Correction.** Citer [BX] p. 3 en contre ; dire que [CA] ne compare pas ; « plusieurs couches » (point 1) repose sur
  [CC] seul.

### VV3-sens-11 — mineur — [AP] p. 23 : deux sondes, pas « la même sonde »

- **Où.** v3 l. 52-54 ; l. 177.
- **Problème.** « here we train a different probe (on just the last positions of the training data) » ; « Both probes were
  trained on the Roleplaying dataset » (p. 23, l. 8-11). La comparaison oppose deux sondes « Roleplaying ». La section 2.2
  le dit bien (l. 125-127).
- **Correction.** « qu'une sonde « Roleplaying » apprise et lue sur toute la réponse ».

### VV3-sens-12 — mineur — E4 : « fixé d'avance » sans date

- **Où.** v3 l. 235 (E4 : « fixé d'avance, sans regarder E1 à E3 (par exemple le bras de production de E3) ») ; l. 249.
- **Problème.** E4 vient après E1 à E3 ; son préenregistrement aussi. « Sans regarder » ne tient que si le bras est gelé
  dans un texte scellé avant toute lecture de E1 à E3 (R1, R3).
- **Correction.** « Bras de E4 écrit dans le préenregistrement scellé de E3, ou dans une note scellée maintenant, avant
  toute lecture de E1 à E3. »

### VV3-sens-13 — mineur — Rang 5 : la phrase de [DYL] sur la capacité de Llama manque

- **Où.** v3 l. 50-52 ; l. 178 (pouvoir « inconnu ») ; l. 319-320.
- **Problème.** [DYL] p. 5, l. 45-48 : « existing organisms are often trained on Llama 3.3 70B, which Appendix I shows has
  limited introspective capacity, and which Artificial Analysis [2026] rank as less capable than more recent models such as
  Qwen 3.5 2B Reasoning ». Llama-3.1-8B ne figure dans aucune table ; s'il est sous Llama-3.3-70B, il tombe sous
  Qwen3.5-2B, où [CA] mesure des sondes faibles (0,585 à 0,781, p. 8). C'est une transposition entre papiers (R8) ; elle
  resserre la question.
- **Correction.** Citer la phrase ; garder « R8 : question », en disant ce qu'elle suggère.

### VV3-sens-14 — mineur — Précisions sur E1 et sur les nœuds

- (a) v3 l. 154-155 : « le mensonge de P3 tient dans un champ » est une hypothèse : le rapport d'environ 33 ([V] l. 345)
  laisse ouverte l'idée d'un projet élargi (note l. 43), et la v3 admet des nombres avant le champ (l. 209-213). Écrire
  « peut tenir ».
- (b) v3 l. 235 : « seuls leurs planchers de même position et T4 au champ sont neufs ». T2 ne porte que sur saboteur
  contre honnête ([P] l. 242) : P3-P4 et T3 au champ et avant le champ sont neufs aussi.
- (c) Oracle : T4 manque dans la case « contrôle obligatoire » (l. 239), alors que la tranche l'exige (l. 236). Le témoin
  étant parmi les négatifs d'apprentissage, P3-P4 n'est pas un test pour l'oracle : le dire (remarque du traitement, non
  appliquée).
- (d) v3 l. 273-274 : « La ligne N-028 du registre porte la même limite : à compléter par la session ». Écrire : par une
  ligne nouvelle qui renvoie à N-028, sans réécrire la ligne d'une décision de Lazar.
- (e) E2 sur T0.6 : la tranche « la position explique-t-elle le nul ? » (l. 236) n'a de sens que sur la condition (i-a),
  p = 1, intensité forte, réplique de P3 (brouillon de T0.6, l. 75) : le préciser.

## Contrôles obligatoires, expérience par expérience

| bras | nombre écrit | plancher de même position et agrégation | témoin | mention | T1 | T3 | T4 |
|---|---|---|---|---|---|---|---|
| E1 (i), maximum sur le champ `COST` | T4 au champ ; manipulation en option (05) | oui | oui | oui | écrit ; ici test du nombre (04) | oui, deux branches | oui |
| E1 (ii), maximum avant le champ | contrôle mécanique, puis (a), (b) ou (c) | oui | oui | oui | à consigne égale, pas à contexte égal (04) | oui | oui |
| E1 (iii), moyenne (diagnostic) | non exigé | oui, même agrégation | non exigé | non exigé | non exigé | non exigé | non exigé (N-026 n'en demande pas) |
| E1 (iv), oracle | empan sans `COST` ; coûts déjà déclarés | permutation avec réapprentissage | négatif d'apprentissage, pas un test (14 c) | hors des négatifs | oui (04) | oui | dans la tranche, pas dans la case (14 c) |
| E2 | nombre de l'action dans le contexte lu ; T4 avec coûts déjà déclarés | oui | oui | sur T0.6 : absente du brouillon (06) | écrit ; prédiction mal fondée (02, 04) | idem (06) | oui |
| E3 | nombres équilibrés ; lecture avant le chiffre | oui | oui | sur T0.6 : absente (06) | oui | idem (06) | oui |
| E4 | « mêmes contrôles » | idem | idem | idem | idem | idem | idem ; date du gel du bras (12) |

## Questions de la commande

- **Contrôles obligatoires.** Écrits pour chaque bras de production de E1, pour E2, E3 et E4 : contrôle du nombre écrit,
  plancher de même position et de même agrégation, témoin, mention, T1, T3 à deux branches, T4. Manques : T1 n'est pas « à
  contexte égal » et teste le nombre au champ et dans E2 (04) ; P3-P4 et T3 ne sont pas calculables sur T0.6 tel qu'il est
  écrit (06) ; oracle : T4 et témoin (14 c) ; manipulation : historique des coûts (05).
- **Bras « moyenne » (N-026).** Diagnostic seulement : libellé exact, même plancher de même agrégation, hors de Bonferroni,
  bras de production lu à côté, lecture « l'agrégation explique-t-elle le nul ? » (l. 199-202 ; l. 235-236) : conforme aux
  conditions 1 à 4. Jamais dans E4 ; oracle en moyenne nommé diagnostic. Lissage de [CC] et maximum de moyennes glissantes
  de [GM] renvoyés à Lazar : bien posé. Reste la base de son inclusion dans P3b (08).
- **R3.** (i) et (ii) déclarés non aveugles et recommandés en diagnostic : conforme. E4 : bras « fixé d'avance » sans date
  (12). Manipulation : aucune prédiction écrite (05). E2 : prédiction écrite, mais mal fondée (02, 04). Aucun bras n'est
  choisi sur résultat.
- **Recommandations et confiances.** Les recommandations (1) à (5) restent compatibles avec les faits corrigés. Ne suivent
  pas : la raison « seule voie » de E3 (07), la confiance de 40 % (02, 09), celle de 15 à 25 % (09), celle de la
  manipulation (05), la prédiction de E2 (02, 04).
- **Nœuds de Lazar.** Bien séparés : revendication et voie de R-262 (2), E2 et manipulation sur les actions de P3, règle
  gelée 1, dépense (R-269 : 10 USD au plus par lancement ; crédit ; devis), changement de modèle (E4), contact (FIBS),
  référence boîte noire (tranchée par N-029, dite telle). À reprendre : base du bras « moyenne » et « couches multiples »
  (08) ; dépense de T0.6, peut-être au-delà de 10 USD par lancement (06) ; ligne N-028 du registre (14 d).

## Conforme (vérifié)

- 22 PDF à l'empreinte de la section 6 ; compagnons égaux pour les 12 PDF du dépôt (RO compris) et pour MA ; absents pour
  les neuf autres, comme la v3 le dit (l. 326-328).
- Phrases anglaises : toutes sur la page citée (`sortie-guillemets-v3.txt`) ; les 36 « introuvables » sont françaises, du
  code (« Your action: ») ou des sigles.
- Chiffres relus sur la page, là où le sens en dépend : [BX] p. 3-8 (0,95, 0,81, 0,63, 0,62, 0,94, 0,5 ; table 1 : 1,00,
  0,04, 0,03) ; [YS] p. 3 ; [AP] p. 5, 9, 10, 18, 21-23, 35 ; [PAR] table 3 (toutes les valeurs citées) ; [DYL] p. 5,
  8-11, table 9 (valeurs citées ; compte 22 / 8 / 2 refait) ; [CA] p. 5-9, 18, 25 ; [OA] p. 1, 5, table 15 ; [K] p. 3, 5,
  table 1 ; [KU] p. 4-6, 9 ; [LB] p. 6-8, 10, table 6 ; [MK] p. 4 ; [GM] p. 6-7, 10-12, table 3 (plages des colonnes
  LC[A] et LC[RT] refaites) ; [AG] p. 17, 43 ; [AU] p. 6-7 ; [BU] p. 5, 10 ; [FQ] p. 1, 3 ; [LIAR] p. 10 ; [RH] p. 9, 27 ;
  [MA] p. 1, 3, 17 ; [EM] p. 38 ; [CC] p. 1, 2, 6, 8.
- Code : `episode.py` (`79113b49…`) l. 213-217, l. 254, l. 260 ; `propositions.py` (`5d97b223…`) l. 32-49, l. 129-138,
  l. 238-269 : VS-01 confirmé (consigne privée, indication avant « Your action: », actions précédentes, champ `COST`
  compris) ; le lanceur de P3 appelle `jouer_episodes` (`premier_test_ia/run.py` l. 52-53, l. 257).
- Pièces du dépôt à l'empreinte citée par la v3 : [P], [V], [AD1], `registres/decisions.md`, `registres/go.md`, N-026,
  N-029, P-011, brief v2, note et propositions C et D, réponses, `resume.json`. Lignes citées exactes : [P] l. 135-142,
  198-205, 214-215, 238-253, 272-279, 289-301, 318-321, 330-332, 385, 415-416, 428 ; [V] l. 120-122, 138, 155, 160,
  170-172, 204, 345, 358-359 ; `registres/decisions.md` l. 446, 453, 456, 457, 461, 468-469 ; `registres/go.md` l. 32-35 ;
  `registres/depenses.md` l. 88-89 ; N-026 l. 18-25 ; N-029 l. 37-39 ; P-011 l. 42 ; [AD1] l. 34 ; brief l. 48 ; note
  l. 8, 26-27, 85 ; `proposition-C.md` l. 323-324 ; `proposition-D.md` l. 81-99 ; `resume.json` (`duree_s` 11 179,1 ;
  240 épisodes ; 2 400 actions ; commit cité `7a54d43…`).
- Dépense et délégation (R-269, GO-2026-10-20-06 à -08, crédit de 11,79 USD à 06:07 UTC) : exactes.

## Limites

- Angle « sens » : les chiffres de la section 2 sans portée sur le sens n'ont pas été recomptés un à un.
- Annexes lues aux pages citées et à quelques voisines ([BX] p. 12-13 ; [AP] p. 22-23, 35 ; [PAR] p. 3-4, 9 ; [LB] p. 6-8 ;
  [DYL] p. 5 ; [AU] p. 7, 9, 17).
- [AU] : la lecture de « +X » reste ambiguë ; je la donne comme telle (03). [BX] : que l'étape 4 soit notée en « Score
  Filtering » est probable, non écrit (01) ; le contraste à consigne égale, lui, est écrit.
- Exposition : voir le cadre. Ni suite de tests, ni `verifier-arbre` (lecture seule). Coûts non devisés.

## Fichiers écrits (chacun avec son compagnon `.sha256`)

- `…/revue-detection/verification-v3-sens-v1.md` (ce rapport).
- `…/revue-detection/verification-v3-sens/` : `outils/ch.py`, `outils/guillemets_v3.py`, `outils/guillemets_multi.py`,
  `sortie-guillemets-v3.txt`, `sortie-guillemets-rapport-v1.txt`, `sortie-guillemets-rapport-v2.txt`,
  `epreuve-r5-guillemets.md`, `sortie-epreuve-r5-guillemets.txt`, `cles-v3-sens.txt`, `empreintes-pdf-v3-sens.txt`,
  `pages/<clé>/rNNN.txt` et `pNNN.txt` (1 043 pages, 22 PDF) ; liste complète : `empreintes-verification-v3-sens.sha256`
  et `empreintes-verification-v3-sens-complement.sha256` (sortie v2).
- Scripts lancés par `python3 -I -B`, sans import local. La première saisie de l'épreuve R5 portait « %% » au lieu de
  « % » (faute de saisie) : réécrite avant tout sceau, jamais citée.
