# Contre-lecture de la fiche de lancement de la course Kirchner Q2 (brouillon 1) — v1

Contre-lecteur neuf (règle R2), sous-agent qui n'a écrit ni le kit ni la fiche. 3 novembre 2026, 10:29 UTC (`date -u`).
Aucun appel payant, aucun réseau, aucune clé cherchée ni lue, aucun fichier existant modifié. Seul fichier écrit : ce rapport
(non scellé, non commité). Je n'ai lu aucune sortie de la course Heimersheim.

Objet : `docs/notes/ideation-organisme-v1/course-kirchner-q2-v1/fiche-lancement-course-kirchner-q2-v1-brouillon1.md`,
sha256 `524c438cf586e5dcfaf93005e05a6421e8145fadfe88d35ab054ce8d0cd0cbcc` (compagnon `.sha256` vérifié : OK). Arbre
`wt-kirchner`, branche `outils/course-kirchner-q2-v1`, commit `02f80605`. Sauf mention, les numéros de ligne renvoient à la fiche.

## Verdict

**Scellable après corrections.** Aucun constat bloquant. Trois constats majeurs :
- CLK-01 porte sur le kit (source du substitut Gu-Krenn). Correction recommandée ; à défaut, déclaration nominative dans la fiche.
- CLK-02 et CLK-03 se corrigent dans le texte de la fiche.

Les cinq défauts relevés sur Heimersheim :
- **corrigés** : la liste d'arrêt (C13, arrêt sans fiche) et la garde « gpt » (« GPT-2 » passe) ;
- **en partie revenus** : l'aiguilleur reste poussé vers l'écart, et cette question y prête davantage (CLK-02) ; le plafond
  s'appuie sur un mot de Lazar rapporté, non direct, et ce mot n'est pas cité à la lettre (CLK-03) ; la source Gu-Krenn pose
  deux liens que les textes ne font pas (CLK-01).

Si une pièce du kit change, il faut un nom neuf (R12), de nouvelles empreintes dans les trois configurations, une nouvelle
table et une nouvelle répétition.

## Vérifié conforme

- **Pièces gelées** :
  - Les 43 lignes de la table (l. 124-166), recalculées par `sha256sum -c` dans l'arbre, sont toutes OK.
  - Elles couvrent les trois configurations, les cinq consignes, la question, les deux pièces, le protocole, la spécification,
    la liste fermée, la source du substitut, les deux lanceurs (`.sh`, `.py`) et les commandes.
  - `table_pieces_gelees_kirchner_v1.py --verifier` sur le brouillon donne : « conforme : 43 pièces gelées, toutes à leur
    empreinte, aucune manquante ».
  - Tous les compagnons `.sha256` de `kirchner/` sont OK. Les 218 empreintes de
    `EMPREINTES-orchestrateur-course-kirchner-q2-v1.txt` sont conformes sur disque.
- **Copies de conv-audit** : les cinq fichiers de `pieces/conv-audit/` sont identiques à l'octet (`cmp`) aux copies de la
  session d'audit. Empreintes : 934f5dcb…, 291f91f8…, 6e7fb1c5…, d6fa8011…, 68919ec9….
- **Consigne du proposeur** :
  - `construire_consigne_proposeur_kirchner_v1.py --verifier` donne « conforme ».
  - Contrôle indépendant : les quatre sections servies de la question (de « ## La question » à la ligne qui précède
    « ## Lecture prévue »), la pièce « Kirchner » v2 entière et la pièce « nos résultats » entière y figurent à l'octet, dans
    cet ordre (positions 460 < 5 650 < 22 978).
  - « Lecture prévue » et « Pièces jointes prévues » sont absentes. Les règles d'intégrité de la question y sont, à l'octet.
  - Le livrable reprend les champs exigés par la question : sous-estimé et comment le vérifier, signe, mesure qui tue, première
    expérience, résultat qui ferait changer d'avis.
  - Servir la pièce v2 est conforme à la question elle-même (« Pièces jointes prévues », 1 : « avant service : y ajouter la
    citation exacte de sa page Pivotal ») et au protocole (§ 2).
- **Juge** :
  - Le bloc « Ce qui est déjà pris » (avec les zones peu couvertes) est repris à l'octet de la question.
  - K1 à K4 suivent les quatre critères gelés du protocole (§ 3 D). Aucun item ne pousse vers une réponse particulière.
    Réserves de forme en CLK-09.
- **Aiguilleur, lecteur, metteur** : niveau Heimersheim v2. Le protocole détaillé et les tricheries plantées décrites par
  classe et rôle relèvent de `niveau_methode`, et un axe choisi parmi plusieurs n'est pas un défaut.
- **Garde lexicale** : passée par `pole/fiches_v54.trouver` (mode « prefixe ») sur les cinq consignes, la liste fermée, les
  concepts du substitut, la question et les deux pièces : rien n'est trouvé.
  - Phrases essayées qui **passent** : « un proposeur (Argon) », « Claude Opus 4.8 », « GPT-2 small », « GPT-4o »,
    « Llama-3.1-8B-Instruct », « Qwen2.5-72B », « Sonnet 4.6 », « diffusion », « fabuleux ».
  - Phrases essayées qui sont **attrapées** : « gpt-6-astra », « GPT‑6 » (trait d'union insécable), « Kimi K3 »,
    « Gemini 4 », « OpenAI », « Gu-Krenn ».
  - **Retirer « argon » est le bon choix.** Le garder ferait refuser la configuration par le contrôle du kit, car
    `course_kirchner_v1.py` l. 247-258 passe la garde sur la pièce « nos résultats ». Il exclurait aussi toute fiche qui cite
    l'attaque A1, alors que c'est l'appui le plus direct entre nos travaux et le moniteur de Kirchner. Le prix, déclaré (l. 62-63) :
    une fiche d'Argon qui se nommerait « Argon » passerait. Si elle se nommait « Gemini », la garde l'attraperait.
- **Dépense** :
  - Plafond technique : S17 = 245 ≥ 1,2 × 203,93 = 244,72 (calcul). C'est le plus petit entier au-dessus, conforme à la
    spécification § 3.
  - Plafonds de session, chacun au-dessus du pire cas d'un appel de son rôle : proposeur 3,5 > 3,2993 ; aiguilleur 0,4 > 0,3383 ;
    juge 0,9 > 0,8545 ; lecteur 0,9 > 0,8476 ; fusion 3,5 > 3,2872.
  - Relais : Kimi 2 ≥ 0,83 (et ≤ 5) ; Argon 3 ≥ 1,75 (et ≤ 10) ; Claude 107,3 ≥ 90,78 ; Astra 132,7 ≥ 110,57. La somme fait 245
    dans chacune des trois variantes.
  - Appels permis : Claude 193 pour 188 ; Astra 135 pour 130 ; Kimi et Argon 7 pour 2.
  - J'ai aussi refait le pire cas avec la formule des commandes (caractères / 3, plus prudente que 3,48) : Fable 3,30,
    Opus 1,32, Argon 1,70, Kimi 0,72 (octets du corps + 1 024, prix par octet), Astra 1,70. La somme, 8,73, reste sous le plafond
    de l'étape « proposition » (8,8).
- **Taille de la consigne du proposeur** (30 452 octets, 29 581 caractères) :
  - Le corps passe à `commande_pole_v56_commun_v1.py` l. 45 et à `commande_argon_v56_nuit_v2.py` l. 80 (borne 4 000 000 octets),
    ainsi qu'à `relais_kimi_v3.py` l. 140 (4 000 000).
  - La consigne arrive par l'entrée standard, pas en argument.
  - Elle fait environ 8 500 à 10 000 jetons d'entrée, plus au plus 32 000 à 65 536 jetons de sortie : bien sous la fenêtre
    des cinq modèles.
  - La répétition a fait passer cette consigne réelle par le vrai chemin de commande et de relais (322 appels, aucun refus).
- **Ce que la fiche dit** :
  - course non décisive (l. 14) ;
  - liste d'arrêt avec C13 ; tout arrêt après la proposition ne rend aucune fiche ; les réponses brutes ne survivent pas
    (l. 97-101) ;
  - aucun témoin planté (l. 43-44) ; consignes réécrites (l. 45-51) ; bras méta hors course (l. 58) ;
  - écarts à la spécification (l. 168-177) ; plafond technique et montant unique de la ligne de GO (l. 76-79) ;
  - sortie scellée avant lecture (l. 105) ; fiches « comptées, non lues » (l. 106-109) ; classement non comparable d'un axe à
    l'autre (l. 51).
- **Marqueurs** : le seul `<<…>>` est à la l. 10 (`Contre-lecture : <<EMPREINTE_RAPPORT>>`). Le lanceur cherche
  « À REMPLIR » et « À FOURNIR AU SCELLEMENT », absents, et exige l'empreinte du rapport dans le texte
  (`pole/configuration_v56.py` l. 142-149). Voir CLK-10 pour `GO-2026-11-03-NN`.

## Constats

### CLK-01 — majeur — source du substitut Gu-Krenn : deux liens que les textes servis ne font pas, et des paires reliées comptées « jamais reliées »

- **Où** : `pieces/source-gu-krenn-kirchner-v1.json`, œuvres `yudelson-lesswrong` (l. 85), `macdermott-2512.00218` (l. 75),
  `organisme-nul-v8` (l. 169), `banque-reelle` (l. 203), `kale-2508.19461` (l. 53), `aar-2608.28945` (l. 5). Dans la fiche :
  l. 52-58 (§ 3.3) et l. 174 (§ 8.4).
- **Rappel du mécanisme** (`pole/bisociateur_v53.py` l. 143-171) : deux concepts sont « reliés » s'ils sont portés par une
  même œuvre. La note d'une paire de fiches est la part des paires de concepts jamais reliées. Un lien de trop retire une
  paire neuve ; un lien manquant fabrique une fausse nouveauté.
- **Liens posés sans appui dans les textes** (même classe que CLH-05) :
  - *Yudelson* porte « banc tenu à l'écart ». La pièce (§ 4) et la question (« déjà pris », l. 1) parlent de **moniteurs**
    tenus à l'écart. Le banc tenu à l'écart, lui, est celui de Kirchner (§ 2.5). La liste fermée n'a pas de concept
    « moniteur tenu à l'écart ». Effet : « banc tenu à l'écart » × « optimisation contre un moniteur » est comptée reliée,
    vérifié.
  - *MacDermott* porte « optimisation contre un moniteur ». La pièce dit seulement qu'optimiser la surveillabilité « ne
    l'améliore pas de façon fiable ». Le rapprochement avec l'optimisation contre une mesure vient de la **note de moisson**
    (§ 4, « ce second remède optimise contre une mesure de surveillabilité »). Or le `_lisez_moi` de la source et la fiche
    (l. 55-56) disent ne coder aucun lien de note de moisson. Effet : « banc de surveillabilité » × « optimisation contre un
    moniteur » est comptée reliée, vérifié.
- **Liens que les textes font mais que la source omet** (fausses paires « jamais reliées », vérifiées) :
  - « processus de richesse (e-valeurs) » × « seuil de Ville », et « juge statistique figé » × « seuil de Ville ». Nos
    résultats § 1 les pose dans la même phrase (« au seuil 1/α (inégalité de Ville) »), mais « seuil de Ville » n'est donné
    qu'à T0.3.
  - « tricheries plantées » × « tricheurs scriptés ». Les tricheurs scriptés du nul v8 (§ 2) sont des tricheries plantées
    contre le juge. La raison donnée pour attribuer « tricheries plantées » à la seule banque réelle (« lois plantées », § 5)
    confond les lois plantées, témoins positifs de puissance, avec des tricheries.
  - « classement partagé » × « sélection par classement ». 2608.28945 choisit parmi les meneurs (§ 2.5) et mesure les
    tricheries arrivées dans les trois premiers (§ 3, fig. 32). Le choix « sélection par classement à la seule note de Mallen »
    est déclaré, mais pas sa conséquence : toute paire « sélection par classement » × dispositif de Kirchner sort comme neuve.
  - Moindre : *Kale* porte « moniteur de triche après coup ». La pièce lui attribue l'échafaudage ; le moniteur après coup est
    celui de Kirchner.
- **Effet** : le bras Gu-Krenn note sur des liens faux dans les deux sens. La course est non décisive et le bras est un
  substitut, d'où « majeur » et non « bloquant ». Mais la demande 4 de la question (« des liens que la littérature citée ne
  fait pas ») est justement ce que ce bras prétend servir.
- **Correction recommandée** (source v2, nom neuf, puis empreintes, table, répétition) :
  - retirer « banc tenu à l'écart » de Yudelson et « optimisation contre un moniteur » de MacDermott ;
  - ajouter « seuil de Ville » à `organisme-nul-v8` et « tricheries plantées » à `organisme-nul-v8` ;
  - trancher « sélection par classement » dans `aar-2608.28945`, et retirer « moniteur de triche après coup » de Kale.
- **À défaut** : déclarer nommément chacun de ces codages au § 3.3 et au § 8.4, et corriger la raison donnée pour
  « tricheries plantées ».

### CLK-02 — majeur — l'aiguilleur reste poussé vers « concret », et cette question y prête plus que Heimersheim : risque d'arrêt total par la garde de Kimi

- **Où** : `pieces/consigne-aiguilleur-kirchner-v1.md` l. 11 et l. 13 ; dans la fiche, l. 48-50 (§ 3.2), l. 98 et
  l. 100-101 (§ 5), l. 117 (§ 7). Code : `pole/aiguilleur_v53.py` l. 114-128 ; `pole/course2_nuit_v1.py` l. 83-87 ;
  configuration `garde_kimi.debordement_max` = 0,5.
- **Le mécanisme** :
  - La demande 2 de la question réclame des expériences sur des **tricheries plantées** contre un moniteur. Une tricherie
    plantée utile pour mesurer un rappel est, par construction, conçue pour être difficile à détecter.
  - L'aiguilleur ne voit pas les pièces. Il ignore donc que les classes nommées (relance chanceuse, copie du format, graines
    triées, exfiltration d'étiquettes) sont publiques chez Kirchner.
  - La classe `concret` couvre « détails opérationnels qui serviraient à tromper un moniteur », et la règle dit « en cas de
    doute, choisis concret ».
  - Une fiche `concret` disparaît (« comptée, non lue »). Au-delà de 4 fiches `concret` sur 8 chez Kimi, la course entière
    s'arrête après l'aiguillage, sans aucune fiche.
- **Pourquoi ce n'est pas bloquant** : la garde est une règle d'intégrité de la question, qu'il ne faut pas desserrer. Le
  risque n'est pas prouvé : au même niveau de consigne, la course Heimersheim a rendu 46 fiches (registre, R-1120).
- **Correction (texte)** : au § 5 et au § 7, dire que cette question rend plus probable le débordement de Kimi (S12) et des
  pertes en `concret` chez toutes les espèces. Faire rapporter, au manifeste ou au rapport, le nombre de fiches par classe et
  par espèce. Choisir la variante en le sachant : `avec-kimi` et `cinq-especes` portent ce point de rupture, `sans-kimi` non.
- **Option kit** (consigne v2, nom neuf) : écrire que nommer une classe de tricherie plantée, son rôle de mesure et sa
  difficulté visée, sans mode d'emploi, relève de `niveau_methode`. Cela ne desserre pas la règle de la question (« par leur
  classe et leur rôle de mesure »).

### CLK-03 — majeur — le montant s'appuie sur un mot rapporté, et le mot direct n'est pas cité à la lettre

- **Où** : l. 23-25 (§ 1) et l. 76-79 (§ 3.8). Registre : `registres/decisions.md` l. 1349 (R-1121). Spécification, l. 3.
- **Le constat** :
  - Le mot **direct** de Lazar à session-depot, inscrit à la R-1121, est verbatim « je eux que Kirchner Q2 passe avant
    A1-v3 », reçu entre 09:33:19 et 10:06:47 UTC. Il ne dit rien du montant.
  - « go pas de plafond » est **rapporté** par conv-audit (09:24, heure de Paris). La spécification note elle-même : « Ta
    garde exige son mot direct pour la ligne de GO : il est prié de te le redire ».
  - Pour Heimersheim, le mot direct portait le plafond (« go heimersheim sans plafond », GO-2026-11-03-02). Pour R1 v4, un
    « plafond large » rapporté a été **confirmé directement** avant inscription (GO-2026-11-03-03).
  - La fiche dit « cités tels quels » mais écrit « je veux que… », et « reçu vers 10:00 UTC ». C'est la même classe que CLH-07.
- **Correction (texte)** :
  - Citer les deux mots à la lettre, avec leur heure exacte : le mot direct (« je eux que… »), et « go pas de plafond », dit
    rapporté par conv-audit.
  - Écrire que le montant de 245 USD repose sur ce mot rapporté, joint au GO direct, ou bien obtenir de Lazar un mot direct au
    vu du devis. C'est à session-depot et à Lazar de choisir ; la ligne de GO le dit.
  - Le risque de dépense est faible : le montant est plus étroit que « pas de plafond », et l'attendu est de 24,20 USD. C'est
    pourquoi le constat est majeur et non bloquant.

### CLK-04 — mineur — « 30 452 caractères » sont des octets

- **Où** : l. 91. La consigne fait 30 452 octets et 29 581 caractères.
- **Effet** : aucun sur la dépense. Le devis compte en caractères, et les commandes comptent les caractères (Claude, Astra,
  Argon) ou les octets (Kimi), selon leur formule.
- **Correction** : écrire « 30 452 octets (29 581 caractères) ».

### CLK-05 — mineur — chiffres sans empreinte (R6)

- **Où** : l. 92 (« 10,03 USD en 58 min (mot de session-depot) ») et l. 114-116 (34 essais, neuf mutations, cinq essais).
- **Correction** :
  - Pour Heimersheim, citer le registre ou le commit (`93928ba8` ; R-1120 dans `registres/decisions.md`).
  - Ajouter à la table `resultat-mutations-kirchner-v1.txt` et `repetition/resultat-repetition-kirchner-v1.txt` avec leurs
    empreintes, ou les citer en ligne.

### CLK-06 — mineur — liste d'arrêt : les arrêts propres au lanceur manquent

- **Où** : l. 97-101. Le LISEZMOI les donne : 124 (délai de 12 h), 6 (clé trouvée : pas de copie au canal), 7 (trace refusée
  ou sceau en échec).
- **Correction** : les ajouter au § 5, et dire ce qu'il reste de lisible après chacun.

### CLK-07 — mineur — exclusivité d'Argon : nommer les autres usages et dire comment on la vérifie

- **Où** : l. 33 (§ 2) et l. 177 (§ 8.7).
- **Le constat** : la spécification (§ 2) fait aussi tourner Argon dans le **tour du collisionneur v9** (espèce C), et la
  seconde course d'A1-v3 l'utilise. Le refus de port déjà pris ne voit que l'hôte local : une course chez la fille, dans un
  autre conteneur, lui échappe.
- **Correction** : écrire que la variante à cinq espèces n'est lancée que si ni le tour v9 ni la seconde course d'A1-v3 ne
  tournent avec Argon, et dire sur quoi on s'appuie (état de la fille, relais 8805).

### CLK-08 — mineur — « rappel du moniteur » est absent du vocabulaire du bras Gu-Krenn

- **Où** : l. 56-57. Code : `pole/course2_v54.py` l. 224-229. La liste servie au lecteur de ce bras est le vocabulaire de la
  source, c'est-à-dire les concepts portés par au moins une œuvre.
- **Le constat** :
  - Le codage est juste : la pièce dit qu'aucun rappel n'est lu.
  - La conséquence n'est pas dite : le lecteur du bras Gu-Krenn ne voit jamais ce concept. Le concept central de la demande 2
    ne compte donc jamais dans ce bras, alors que le bras basique (liste de 46) le voit.
- **Correction** : le déclarer au § 3.3.

### CLK-09 — mineur — juge et metteur : biais de forme à déclarer

- **Juge** (`pieces/consigne-juge-kirchner-v1.md`) :
  - K3 (l. 30) ajoute « son coût est chiffré ou marqué supposé », que le critère gelé 3 ne demande pas.
  - K5 (l. 32) exige de « poser la nouveauté comme une question », alors que K1 demande de dire pourquoi le problème est
    sous-estimé.
  - « n'invente aucun identifiant » ne peut pas se vérifier sans les pièces. 2608.28945, 2407.13692 et 2605.06390 ne sont pas
    dans la consigne du juge, qui risque de les tenir pour inventés.
  - K1 note une affirmation de la fiche, pas une moisson.
- **Metteur** (`pieces/consigne-metteur-kirchner-v1.md` l. 7) : l'exemple oriente les fusions vers les axes 2 et 3.
- **Effet** : faible. Les sorties des juges sont rapportées à part (protocole § 1.2).
- **Correction** : une phrase au § 3.2.

### CLK-10 — mineur — `GO-2026-11-03-NN` est un remplissage

- **Où** : l. 25. Le lanceur ne le cherche pas, mais c'est un marqueur hors de la ligne de contre-lecture.
- **Correction** : écrire le numéro réel au scellement, ou « numéro attribué à l'inscription, cité au lancement ».

### CLK-11 — mineur — protocole et LISEZMOI : statut du coffre

- **Le constat** : le protocole (§ 1.2) exclut le coffre, « jamais ouvert ». Le LISEZMOI (l. 58-60) range les mariages dans
  `coffre/…` et dit que le coffre « n'y sert qu'à part ». Le protocole demande aussi les fusions « inachevées comprises » ; la
  fiche ne dit pas si elles sont dans la sortie.
- **Correction** : une ligne au § 6, qui dit ce que voit le préparateur et ce qu'il ne voit pas.

### CLK-12 — mineur — chemins internes dans les textes servis (information pour conv-audit)

- **Le constat** : la question (l. 9 : `brouillons/candidature-pivotal-v16/…`) et la pièce « Kirchner » (l. 1, l. 4, l. 21)
  portent des chemins de brouillons internes. Ils partent chez quatre fournisseurs. Ce ne sont pas des textes privés, mais ce
  sont des métadonnées.
- **Correction** : aucune dans ce kit, puisque la fidélité à l'octet est exigée. Le signaler à conv-audit.

### CLK-13 — mineur — marge mince à la proposition ; délai de Kimi non éprouvé avec cette consigne

- **Le constat** :
  - Le plafond de l'étape « proposition » vaut 8,8 USD, pour un pire cas de 8,79 au devis (8,73 avec la formule des commandes).
  - La consigne est plus longue que celle de Heimersheim, et la durée de Kimi (jusqu'à 65 536 jetons en 1 750 s) n'est pas
    éprouvée avec elle. Un délai dépassé donne le nœud C13, donc aucune fiche.
- **Correction** : le dire au § 7, avec la remarque « point de rupture unique » (l. 39).

### CLK-14 — mineur — cosmétique du kit

- **Le constat** : la docstring de `course_kirchner_v1.py` (l. 1) dit « v2 = `course_kirchner_v1.py` (gardé, R12) », un reste
  de substitution. La l. 71 porte deux commentaires bout à bout. Rien ne change à l'exécution.
- **Correction** : rien maintenant ; à corriger dans une version suivante.
