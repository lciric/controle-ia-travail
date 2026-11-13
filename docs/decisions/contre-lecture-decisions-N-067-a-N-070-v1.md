# Contre-lecture des brouillons 1 des décisions N-067 à N-070 (règle R2) — v1

Contre-lecteur neuf (sous-agent, Claude Fable 5.2 ; le rédacteur était Claude Opus 5.5), lancé par la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`. Travail du 13 novembre 2026, de 18:37 à 18:50 UTC (heures relevées par `date -u` ; l'horloge du conteneur avance lentement par rapport au travail fait). Je n'ai écrit ni les brouillons, ni leur journal, ni le programme, ni les décisions d'origine, ni aucun rapport de lecture.

**Objet** : `docs/decisions/decision-N-067-v1-brouillon1.md`, `…N-068…`, `…N-069…`, `…N-070…` et `journal-decisions-N-067-a-N-070-v1.md` (R-2560). Mots de Lazar appliqués : R-2555, option B (a) ; R-2554 pour l'article 2611.04556.

## 0. Verdicts

| décision | verdict | bloquants | majeurs | mineurs |
|---|---|---|---|---|
| N-067 (organisme) | **retenable après corrections** | 0 | 3 | 5 |
| N-068 (HC2) | **retenable après corrections** | 0 | 1 | 4 |
| N-069 (papier B) | **retenable après corrections** | 0 | 1 | 3 |
| N-070 (H9) | **retenable après corrections** | 0 | 1 | 4 |

Aucun bloquant : aucun énoncé d'origine mal recopié, aucune page fausse, aucun énoncé resserré plus large que ce que les rapports laissent libre. Les six majeurs sont tous du même type : un voisin ou un contre-indice lu sur PDF et présent dans un rapport n'est pas dit, ou une phrase va un cran au-delà du rapport.

Le journal du rédacteur est fidèle à ce que j'ai retrouvé ; il est scellé et ne se réécrit pas (R12) ; rien à y corriger.

## 1. Ce qui a été contrôlé, et comment

1. **Empreintes.** Les cinq fichiers sont conformes à leur compagnon `.sha256` : N-067 `d83d067c122e8ae5…`, N-068 `76be8b44601db787…`, N-069 `823a3c357ef66369…`, N-070 `8b52e368bbfbcf91…`, journal `be45f8c59c786917…`. Synthèse finale `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` : conforme (`e30a013d…`). **Sa contre-lecture n'existe pas à mon passage** (aucun fichier « contre-lecture » sous `docs/etat-de-l-art/` sur `main`) : mes comparaisons se font contre la synthèse non contre-lue et contre les rapports eux-mêmes.
2. **Récupérations.** Les deux `git fetch` nommés par le mandat, rien d'autre hors du conteneur. Douze rapports extraits par `git show` (C4, C6, C7, C9 ; lots 1, 3-A, 4-A, 5-A, 7-B, 7-C, 7-D, 12) : empreintes conformes aux compagnons des branches.
3. **Énoncés d'origine (point 1 du mandat).** Chaque ligne citée des sections 2 a été relue à son numéro dans le fichier source (programme v2, l. 16, 43, 62, 72, 103, 123, 195, 207, 208, 211, 239, 240 ; N-064, l. 13 à 15 ; N-013, l. 90, 92 ; N-005-N-006, l. 97 ; N-035, l. 16, 17, 26 à 29, 33 ; antériorité de niveau 2, l. 233, 392 ; note Co-Scientist, l. 257, 259, 260, 267, 268, 273). Puis un programme a recherché chaque passage entre guillemets des quatre brouillons dans ces sources, le registre et les rapports : **tous les énoncés d'origine sont recopiés exactement** (gras et renvois de source ôtés, ce qui est dit). Le mot de Lazar (R-2555) et l'extrait de la lecture de la mère sont exacts. Une seule citation est tronquée d'une façon qui en change la force (N-070, constat 70-1).
4. **Pages sur PDF (point 2).** 39 PDF extraits dans un dossier neuf, empreintes recalculées et conformes aux compagnons. **Plus de 180 recherches de passages, de chiffres ou de termes, page par page (`pdftotext`, blancs réduits, césures recollées), sur 39 PDF ; pour trois pièces à deux colonnes, extraction sans mise en page.** Au moins un contrôle fort (phrase exacte ou chiffre lu dans son contexte) sur chacune des pièces suivantes, bien au-delà des quinze demandés :
   - N-067 : CONFIRM p. 3, 5, 6, 9, 14, 19, 22 ; « Hard to Fool » p. 3, 4, 6 ; Qu, Chen, Wang p. 2, 4, 6, 9, 12, 13, 14, 15, 16, 18, 22, 29 ; Sargsyan p. 8, 10, 16, 25, 27, 28, 29 ; N×N p. 1, 25, 26 ; Masked Erosion p. 4, 18 ; REUSE p. 32 ; PACE p. 5, 6 ; 2611.04420 p. 5, 6, 8, 10 ; CADS p. 11 ; 2611.00643 p. 16 ; PROCTOR p. 2, 7 ;
   - N-068 : MIRAGE p. 1, 14, 19, 20, 21 ; Karne p. 1, 6, 22 ; 2608.21664 p. 6, 7 ; 2602.00750 p. 1 ; 2611.10620 p. 22 ; 2602.08877 p. 18 ; 2610.18408 p. 1, 4, 12 ;
   - N-069 : 2601.05427 p. 1, 4, 5 ; 2605.11135 p. 1, 2 ; J-PACT p. 7, 8 ; 2611.10620 p. 11, 14, 15, 16, 21 ; HELIOS version 5 p. 18, 30 ; 2609.03035 v2 p. 1, 2, 7, 8, 9, 10, 29 ; 2607.24893 v2 p. 8 ;
   - N-070 : MasDrift p. 2, 6, 7, 22, 23 ; Sun p. 1, 5, 7 ; Li p. 1 ; Hammond p. 24 ; AgentCollabBench p. 34 ; Tomašev p. 16 ; Cemri p. 2, 17.
   - Titres, auteurs et dates imprimés en page 1 de 22 pièces : conformes aux tables des brouillons.

   **Aucune page citée par les brouillons n'est fausse.** Les contrôles faibles (un terme sur une plage de pages) sont nombreux ; ils ne prouvent que la présence du sujet à la page. Trois pages ne portent pas le chiffre à la page nommée mais à une page voisine de la même plage (88,2 % de MasDrift : p. 23, non p. 6 ; 2,4 et 3,8 de Karne : p. 6 et 22, non p. 1 ni 5 ; 0,405 de MIRAGE : p. 7, 19, 20) : les plages des brouillons les couvrent.
5. **Non contrôlé par moi.** Le compte des citations des rapports (115, 119, 131, 141, 87) ; les PDF de niveau 2 cités en dernière ligne de la table de N-068 ; les pièces citées « quand le point est abordé » (SGM, SEAL, DISCERN au-delà d'un terme, Tallam, Ying, Liu) ; la phrase de 2608.21664 que C9 situe p. 2 (« transcribed span »), non retrouvée par mon extraction à deux colonnes — je la tiens de C9.

## 2. N-067 — organisme d'idéation : retenable après corrections

Énoncés d'origine exacts. Table « pris par » conforme à C4, C7 et 4-A. L'énoncé retenu de O2 est celui de 4-A (§ 6, point 1). La forme resserrée de O12 est celle de 4-A (§ 6, point 3, et § 7 (a)), plus « libre dans ses propositions », que 4-A (§ 0) donne aussi comme absent de CONFIRM : pas d'élargissement.

**67-1 (majeur) — voisins de la forme de O12 omis, dont une consigne adverse publiée.** Le lot 4-A (§ 0, ligne (f), et § 2 (f)) range sous O12 trois pièces que la ligne « O12 » de la table ne dit pas. La plus proche : chez Sargsyan, un modèle de langue reçoit une consigne adverse et le chemin exact du fichier de validation, « modeling a worst-case adversary that has seen the generated harness » (p. 27, vérifié ; p. 28 : « every well-formed generation attempted to read the validation file », vérifié). L'attaque vise la frontière des données, non la statistique : la forme resserrée reste non trouvée, mais « chargé de tromper » et « qui lit le juge » ne sont pas sans précédent pris un à un. Chez Qu, Chen, Wang, le proposeur modèle reçoit les diagnostics de l'arbitre (p. 12, vérifié ; C7, § 1.2) : c'est le bras « verdicts », sans consigne de tromper.

Texte actuel (section 3, ligne O12) :
```actuel
proposeur adverse théorique à un bit : REUSE, p. 32 ; monde sans gain, sans attaque : PACE, p. 6-7 | C7, 4-A |
```
Texte corrigé :
```corrige
proposeur adverse théorique à un bit : REUSE, p. 32 ; monde sans gain, sans attaque : PACE, p. 6-7 ; diagnostics de l'arbitre rendus au proposeur modèle, sans consigne de tromper : Qu, Chen, Wang, p. 12 ; **consigne adverse donnée à un modèle de langue qui connaît le harnais, dirigée contre la frontière des données et non contre la statistique : Sargsyan, p. 27-28** ; harnais optimisé contre un juge modèle : 2611.00643, p. 1, 2, 10 ; générateur qui s'adapte au vérificateur : Hegazy, Jordan, Dieuleveut, p. 1-2 | C7, 4-A |
```
Texte actuel (section 4, point 3) :
```actuel
Ce qui n'est plus revendiqué : la partie « verdicts servis à un proposeur modèle de langue, mondes négatifs, zéro promotion », publiée par CONFIRM (p. 9, 22).
```
Texte corrigé :
```corrige
Ce qui n'est plus revendiqué : la partie « verdicts servis à un proposeur modèle de langue, mondes négatifs, zéro promotion », publiée par CONFIRM (p. 9, 22). Voisin à dire : une consigne adverse donnée à un modèle de langue qui connaît le harnais est publiée (Sargsyan, p. 27-28), mais elle vise la frontière des données, non la statistique ni le seuil ; « chargé de tromper » s'entend ici « chargé de faire promouvoir une fiche fausse par le juge statistique ».
```

**67-2 (majeur) — le « non trouvé » qui porte O4 est dit plus fort que la lecture faite.** La ligne O2 (c) écrit « non trouvé » dans « les vingt autres pièces du dossier c8 » sans dire que C7 (§ 7) n'en a lu aucune en entier : trois par passages (PACE, REUSE, Masked Erosion), onze par la page 1 et une recherche de termes, six par la seule page 1. Le lot 4-A (§ 1) n'a couvert les annexes de cinq de ses neuf pièces que par recherche de termes. O4 devenant le seul porteur de la revendication du juge, la profondeur doit être dans la ligne même (R8), pas seulement dans le journal (point 10). Deux voisins du nul d'archive, relevés par les lecteurs, manquent aussi : la fusion des quasi-doublons prévue et non exercée chez Qu, Chen, Wang (p. 9, vérifié ; p. 22, C7), et la mesure relative à un témoin de « Hard to Fool », calculée mais « diagnostic only » (p. 4, vérifié ; 4-A, § 4.4).

Texte actuel (section 3, ligne O2 (c)) :
```actuel
**non trouvé** dans les neuf pièces du lot 4-A, les 37 pages de Qu, Chen, Wang et les vingt autres pièces du dossier c8 ; voisins : N×N, p. 3 (nul de taux de base)
```
Texte corrigé :
```corrige
**non trouvé** dans les neuf pièces du lot 4-A (annexes de cinq d'entre elles par recherche de termes, 4-A, § 1), les 37 pages de Qu, Chen, Wang (lues en entier) et les vingt autres pièces du dossier c8 (trois lues par passages, onze par la page 1 et une recherche de termes, six par la seule page 1 : C7, § 7 ; « non trouvé » y vaut pour les termes cherchés) ; voisins : Qu, Chen, Wang, p. 9, 22 (fusion des quasi-doublons prévue, non exercée) ; « Hard to Fool », p. 4 (mesure relative à un témoin, calculée mais « diagnostic only ») ; N×N, p. 3 (nul de taux de base)
```

**67-3 (majeur) — O4 seul porteur : aucune règle n'en garde l'usage public.** Le brouillon dit (section 4, point 2 ; section 8) que le verdict sur O4 est le plus fragile et qu'une piste de priorité haute, non lue, peut l'occuper en entier (SSRN 6569258, selon un résumé de moteur). Le journal recommande de la lire « avant tout usage public de O4 » (point 6), mais la décision ne le fixe nulle part, alors que R-2555, option C, prévoit un enregistrement figé et irréversible des pièces libres. R8 demande de vérifier plus durement une zone vierge séduisante. La règle doit être dans la décision ; son choix revient à Lazar (section 6 ci-dessous).

Texte actuel (section 10) :
```actuel
- **Enregistrement public des pièces libres** (R-2555, option C) : son texte, que la mère montre à Lazar avant de figer, devrait reprendre les énoncés resserrés de cette note une fois retenue, et pas ceux de N-064.
```
Texte corrigé :
```corrige
- **Enregistrement public des pièces libres** (R-2555, option C) : son texte, que la mère montre à Lazar avant de figer, devrait reprendre les énoncés resserrés de cette note une fois retenue, et pas ceux de N-064. **O4 et l'énoncé retenu de O2 n'y entrent, et n'entrent dans aucun texte qui sort du dépôt, qu'après lecture sur PDF des pistes de priorité haute dirigées contre O4 (section 8 ; d'abord SSRN 6569258), ou bien avec la mention écrite que la littérature de finance sur la nouveauté d'un facteur face aux facteurs connus n'a pas été lue ; le choix entre les deux revient à Lazar.**
```

**67-4 (mineur) — phrase pour un lecteur extérieur : la réserve de champ de la synthèse finale (section 5) est tombée.**

Texte actuel (section 4) :
```actuel
Ce que nous n'avons trouvé dans aucune pièce lue : un juge dont le nul est formé des lois connues, et sa mesure sous l'attaque d'un proposeur chargé de le tromper qui en lit la règle. »
```
Texte corrigé :
```corrige
Ce que nous n'avons trouvé dans aucune pièce lue : un juge dont le nul est formé des lois connues, et sa mesure sous l'attaque d'un proposeur chargé de le tromper qui en lit la règle. Cela vaut pour les pièces lues, pas pour le champ : la littérature de finance sur les facteurs redondants n'a pas été lue. »
```

**67-5 (mineur) — la section 9 contredit la section 10.** Elle dit inchangées O5 à O20 « avec leurs statuts de C4 et C7 », alors que ces statuts diffèrent de ceux de N-064 pour O9, O10, O13 et O19 et que la section 10 les dit « non resserrés ici, à trancher ».

Texte actuel (section 9) :
```actuel
- R1 à R14 ; O5 à O10, O13 à O16, O18 à O20 avec leurs statuts de C4 et C7 (section 10 pour O9, O10, O19) ; O8, non trouvée dans les pièces lues (contre-indice en section 7).
```
Texte corrigé :
```corrige
- R1 à R14 ; les énoncés de O5 à O10, O13 à O16 et O18 à O20, que cette note ne touche pas. Leurs statuts d'antériorité relevés par C4, C7 et 4-A, quand ils diffèrent de ceux de N-064 (O9, O10, O13, O19), sont constatés en section 10 et restent à trancher ; O8, non trouvée dans les pièces lues (contre-indice en section 7).
```

**67-6 (mineur) — la réunion des quatre composantes : dire si elle est revendiquée.** La recommandation suivie (4-A, § 7 (a)) dit « le nul des lois connues et la conjonction » ; le brouillon ne garde que le nul et dit la réunion comme un assemblage. C'est défendable (4-A, § 0 : la conjonction n'est « non trouvée » que parce que le nul ne l'est pas), mais doit être écrit.

Texte actuel (section 4, point 1) :
```actuel
Elle se dit comme un **assemblage dont trois pièces sont empruntées**, jamais comme quatre apports.
```
Texte corrigé :
```corrige
Elle se dit comme un **assemblage dont trois pièces sont empruntées**, jamais comme quatre apports. Elle n'est pas revendiquée comme un apport distinct du nul : elle n'est « non trouvée » que parce que le nul ne l'est pas (4-A, § 0).
```

**67-7 (mineur) — mutations du code du juge : le « non trouvé » ne cite que C7, qui n'a pas lu 2611.04420.** Contrôlé sur le PDF : la batterie de 2611.04420 (p. 5-6) mesure la part de mutants tués par le vérificateur ; elle mute les candidats, non le code du vérificateur. Le « non trouvé » tient, à dire sur les deux lots.

Texte actuel (section 4, point 4) :
```actuel
Une batterie de mutations du **code du juge statistique lui-même** n'est trouvée dans aucune pièce lue (C7, § 4) : elle est dite comme telle, sans revendication.
```
Texte corrigé :
```corrige
Une batterie de mutations du **code du juge statistique lui-même** n'est trouvée dans aucune pièce lue par C7 (§ 4) ; la batterie de 2611.04420 (p. 5-6), lue par 4-A, mute les candidats soumis au vérificateur, non le code du vérificateur : elle est dite comme telle, sans revendication.
```

**67-8 (mineur) — réserve de 4-A sur « Hard to Fool » omise** (le gel a failli une fois : spécification écrite sur un chemin temporaire, reconstruite avant la lecture de la réserve, p. 6, vérifié).

Texte actuel (section 3, ligne O2 (b)) :
```actuel
spécification et code du verdict liés par SHA-256 avant que les données existent)
```
Texte corrigé :
```corrige
spécification et code du verdict liés par SHA-256 avant que les données existent ; de l'aveu de l'auteur, une spécification gelée a dû être reconstruite une fois avant la lecture de la réserve, p. 6)
```

**Constat sans correction (point 3 du mandat, « plus étroit sans raison »).** Le brouillon cesse de revendiquer quatre choses que les lecteurs listent encore comme « tenues » ou « revendicables » : l'ensemencement des tirages par l'empreinte (4-A, § 6, point 4 ; C7, § 4), la combinaison et l'ampleur du banc de O11 (C7, § 4 ; synthèse, section 5), le banc de mutations du scellement et la règle générale contre le repli silencieux (O17), l'objet « hypothèses libres » pris seul. La raison donnée tient (ce sont des choix de mise en œuvre ou des ampleurs, non des idées ; aucune lecture de durcissement n'a été faite ; N-064, point 3, ne laissait déjà à O11 et O12 que la forme de l'attaque). Mais c'est **plus étroit que « ce qui reste libre »** au sens de R-2555 : à confirmer par Lazar (section 6).

## 3. N-068 — HC2 : retenable après corrections

Énoncés d'origine exacts. Table des composantes conforme au lot 1 (§ 3.1) ; énoncé retenu repris mot pour mot du lot 1, avec l'ajustement du lot 3-A (§ 10.5), lui-même exact (2610.18408, p. 4 et 12 : jumeau propre et sosie, vérifiés). L'énoncé n'est pas plus large que ce que la synthèse finale donne pour libre (section 4, HC2).

**68-1 (majeur) — 2609.03035 version 2 n'est pas dite, et « le même signe n'est publié que par MIRAGE » est faux dans les pièces lues.** Le lot 7-B (§ 3), que le rédacteur a lu pour N-069, décrit une pièce où des sondes lisent des agents qui agissent et qui sont les adversaires (collusion), prévenus puis recevant le score et la décision du tour précédent, à poids fixes. Vérifié sur le PDF (`docs/sources/pdf/niveau3-v1/lot6/2609.03035v2.pdf`, branche des pièces, `bccdbe1b2dd753f2…`, conforme) : les agents « do not produce a broad collapse in activation-based detection » (p. 1) ; adaptation « through context alone » (p. 2) ; « We therefore do not test sustained optimisation against the detector » (p. 10) ; un juge de sortie baisse plus que la sonde sous avertissement (« LR–Peak AUROC is 0.92 at baseline and 0.90 under awareness », p. 8 ; « Actor-visible output-monitor AUROC 0.74 0.68 », tableau 13, p. 29 ; 14 puis 8 épisodes positifs). C'est le même signe que la prédiction de HC2, sur la position « agent qui agit et adversaire », avec une comparaison sonde contre juge dans un même cadre : voisin des trois éléments dits « propres ». Aucun lecteur ne l'a jugée contre HC2 (7-B la juge contre le papier B et HC4) ; elle ne porte ni contenu rhétorique destiné au moniteur, ni g, ni plan apparié : l'énoncé retenu n'est pas occupé. Chiffres de rappel non opposables (7-B, § 3.2).

Texte actuel (section 6, dernier paragraphe) :
```actuel
Lecture d'ensemble (C9, § 5) : HC2 reste non trouvée dans les pièces lues, **mais rendue moins probable**, surtout par 2608.21664, seule pièce opposable où la sonde lit le modèle auteur. Le même signe que la prédiction n'est publié que par MIRAGE, non opposable.
```
Texte corrigé :
```corrige
Lecture d'ensemble (C9, § 5) : HC2 reste non trouvée dans les pièces lues, **mais rendue moins probable**, surtout par 2608.21664, seule pièce opposable où la sonde lit le modèle qui écrit (une phrase imposée, sous une consigne donnée ouvertement). Le même signe que la prédiction est publié par MIRAGE et par 2609.03035 version 2 (agents adversaires prévenus, puis recevant le score et la décision du tour précédent : « do not produce a broad collapse in activation-based detection », p. 1 ; aucune optimisation soutenue contre le détecteur, p. 10), tous deux non opposables (lot 1, § 1.5 ; lot 7-B, § 3.2 : rappels remplacés sans explication entre la version 1 et la version 2). Le sens de l'effet d'un avertissement est opposé entre 2609.03035 version 2 et 2611.10620 (lot 7-B, § 2.5) : les deux ne se citent pas ensemble comme un fait.
```
Ligne à ajouter à la table de la section 6, après la ligne « Mohsin, Rahman » :
```corrige
| Ponde, Das, More, Gupta, « You Can't Escape Your Activations: Evaluation Awareness and Multi-Agent Monitoring », arXiv 2609.03035 v2 ; `…/lot6/2609.03035v2.pdf`, `bccdbe1b2dd753f2…` | **même signe que la prédiction, non opposable** : par le contexte seul, même avec le score du tour précédent, l'aire sous la courbe des sondes ne s'effondre pas ; un juge de sortie baisse plus que la sonde sous avertissement (0,74 à 0,68 contre 0,92 à 0,90 ; 14 puis 8 épisodes positifs) : voisin de la comparaison aux juges, sans contenu adverse destiné au moniteur, sans g | 1, 2, 8, 10, 29 | agent qui agit et adversaire (collusion), contexte seul | lot 7-B, § 3 |
```
Texte actuel (section 4, « ce qui est propre ») :
```actuel
Le **plan apparié en soi n'est pas revendiqué comme neuf** : Kale et Vishwanath l'emploient déjà pour des sondes d'exposition côté lecteur (jumeau propre, sosie inoffensif ; 2610.18408 v1, p. 4, 12).
```
Texte corrigé :
```corrige
Le **plan apparié en soi n'est pas revendiqué comme neuf** : Kale et Vishwanath l'emploient déjà pour des sondes d'exposition côté lecteur (jumeau propre, sosie inoffensif ; 2610.18408 v1, p. 4, 12). Une comparaison d'une sonde et d'un juge de sortie dans un même cadre, sous simple avertissement des agents, existe aussi (2609.03035 v2, p. 8, 29 ; non opposable) : ce qui est propre est la comparaison des deux déplacements g sous un même contenu adverse écrit par l'agent.
```

**68-2 (mineur) — valeur intermédiaire omise** (vérifiée p. 22 : « recall drops from 0.87 to 0.71 when agents are only warned, and to 0.55 when colluders are also told to evade »).

Texte actuel (section 6, ligne Mohsin, Rahman) :
```actuel
rappel à seuil fixe de 0,87 à 0,55, aire sous la courbe presque inchangée
```
Texte corrigé :
```corrige
rappel à seuil fixe de 0,87 à 0,71 (prévenus) puis 0,55 (priés d'évader), aire sous la courbe presque inchangée
```

**68-3 (mineur) — « auteur » pour 2608.21664 est trop court.** Le modèle recopie une phrase imposée pendant qu'une consigne ouverte lui dit de ne pas penser à un concept (vérifié p. 6 pour « 5–21% » à 1 % de faux positifs, p. 7 pour « Our monitors are not hardened ») ; il n'écrit pas un contenu de son cru. C9 n'a lu que les pages 1 à 10 sur 18.

Texte actuel (section 6, ligne Kowalski) :
```actuel
| 4, 6, 7 | **auteur** | C9, § 3.6 |
```
Texte corrigé :
```corrige
| 4, 6, 7 | **modèle qui écrit** (phrase imposée, recopiée ; pages 1 à 10 lues sur 18) | C9, § 3.6 |
```

**68-4 (mineur) — l'énoncé retenu ne porte pas « en fonction de l'intensité », que la liste « ce qui est propre » et la synthèse finale portent.** Harmoniser, ou dire pourquoi non. C'est un qualificatif de plus : à confirmer par Lazar avec le plan apparié.

Texte actuel (section 4, énoncé retenu) :
```actuel
le **déplacement continu g du score**, mesuré en **plan apparié**
```
Texte corrigé :
```corrige
le **déplacement continu g du score, en fonction de l'intensité de l'attaque**, mesuré en **plan apparié**
```

**68-5 (mineur) — R-2554 n'est pas rappelé.** À ajouter à la section 7 (« ce qui ne change pas ») :
```corrige
- R-2554 : l'article 2611.04556 reste cité comme publié pour la prémisse du papier C, sans changer d'énoncé ; ses trois contre-indices vont aux préenregistrements de HC1, HC4 et HC6 ; aucun ne porte sur HC2 (l'article n'a aucune sonde, synthèse finale, section 6).
```

## 4. N-069 — papier B : retenable après corrections

Énoncés d'origine exacts. Les deux énoncés retenus sont ceux de 7-B (§ 6.1) et de 5-A (§ 3) réunis ; la réunion ajoute des qualificatifs (elle resserre). Rien n'est plus large que la synthèse finale (section 3). Chiffres vérifiés : tableau 3 de 2611.10620, p. 14 (0,86 ; 0,85 ; 0,76) ; phrase de la p. 21 ; 0,921 contre 0,993 chez J-PACT, p. 7 ; 0,38 chez HELIOS, p. 18 ; 0,883, p. 16.

**69-1 (majeur) — un contre-indice sur la forme « co-élévation » elle-même n'est pas dit.** L'énoncé 1 garde le mot « co-élévation » (montée conjointe). Or 7-B (§ 3.3) écrit, pour 2609.03035 version 2, que le signal relationnel trouvé « est une asymétrie (un score monte, l'autre non), l'inverse d'une montée conjointe », et, pour 2611.10620, « un contraste de niveaux, pas une montée conjointe ». Vérifié sur le PDF de 2609.03035 v2 : sur le jeu à deux agents, l'écart (« Deception Split ») donne en moyenne 0,87, 0,81 et 0,86 d'aire sous la courbe contre 0,61, 0,61 et 0,58 pour le pic, et « collusion is more visible in the relative pattern between the agents' activation scores than in the largest individual score alone » (p. 7) ; « even when neither agent independently appears highly suspicious » (p. 9). Pour le papier B, cette pièce est à la fois un indice favorable (une règle relationnelle bat le pic) et un indice contraire à la forme annoncée. Le brouillon ne la cite que pour dire ses rappels non opposables.

À ajouter à la section 7, après la ligne sur J-PACT :
```corrige
- **Forme « co-élévation » elle-même** : là où une règle relationnelle sur scores de sondes fait mieux que le pic (jeu à deux agents ; aire sous la courbe moyenne 0,87, 0,81 et 0,86 pour l'écart, contre 0,61, 0,61 et 0,58 pour le pic), le signal est un **écart** entre agents (« Deception Split », règle de NARCBench) : une asymétrie, non une montée conjointe (2609.03035 v2, p. 7, 9 ; `lot6/2609.03035v2.pdf`, `bccdbe1b2dd753f2…` ; 7-B, § 3.3) ; 2611.10620 mesure de même un contraste de niveaux (7-B, § 2.6). Indice favorable à une statistique relationnelle, contraire à la forme « montée conjointe ». Rappels de cette pièce non opposables (7-B, § 3.2). Le préenregistrement dit pourquoi une montée conjointe est attendue plutôt qu'un écart, et garde l'écart comme base.
```

**69-2 (mineur) — un résultat négatif voisin de 5-A (§ 3) n'est pas dit** (vérifié, 2607.24893 v2, p. 8 ; `lot5/2607.24893v2.pdf`, `504d82ab525be78b…`, conforme). À ajouter à la section 7 :
```corrige
- **Mise en commun entre agents, en boîte noire** : sur des portes dérobées réparties, un détecteur sur le flux réuni des agents tire tôt « mostly because the injected text makes an observation longer, not because it puts evidence together across agents » (2607.24893 v2, p. 8 ; 5-A, § 3 : « voisin (résultat négatif) »).
```

**69-3 (mineur) — la section 7 invoque la thèse « l'essaim plus détectable que l'agent isolé » sans le seul contre-indice boîte blanche en nombre d'agents** (HELIOS version 5 : 0,88 à 4 agents, 0,737 au mieux à 8 agents, p. 27, 30 ; C1 ; 0,737 vérifié p. 30). Il relève de H3, que la note ne touche pas ; à dire en une ligne ou à renvoyer explicitement à H3. À ajouter à la section 7 :
```corrige
- **Nombre d'agents** (relève de H3, non touchée ici) : la meilleure aire sous la courbe de la coupe transversale sur le transfert passe de 0,88 à 4 agents à 0,737 au mieux à 8 agents (HELIOS version 5, p. 27, 30 ; rapport C1).
```

**69-4 (mineur) — R-2554 n'est pas rappelé.** À ajouter à la section 8 :
```corrige
- R-2554 : l'article 2611.04556 reste cité comme publié pour la prémisse du papier B, sans changer d'énoncé.
```

## 5. N-070 — H9 : retenable après corrections

Énoncés de N-035 exacts (l. 16, 17, 26, 28, 33). Table des composantes conforme à 7-D (§ 7) et au lot 12 (§ 4). Chiffres vérifiés : 88,2 % sur 3 950 (MasDrift, tableau 18, p. 23) ; 2,7 % à 19,8 % (p. 2) ; « does not order by depth » (p. 6) ; 54,5 % et 36,3 points (p. 6, 22) ; 85,2 % à 1,6 % (Sun, p. 1, 7) ; tableau 23 d'AgentCollabBench (16 %, 8 %, 3 %, 40 %, p. 34) ; 96 % à moins de 60 % (Hammond, p. 24).

**Point 5 du mandat, première moitié — la condition du repli est-elle remplie selon son texte ?** N-035 écrit : « C'est le repli si l'antériorité prend la pièce » et « Une pièce trouvée prise se replie sur (b) ». Les deux lecteurs disent la condition remplie **pour le cœur de l'énoncé** (phénomène occupé ; mesure par passage, décroissance, moniteur et confondants occupés en partie), jamais pour l'énoncé entier, et le lot 12 ajoute que « le repli ou la reformulation est un nœud de Lazar ». Lecture stricte du texte : la pièce est prise en partie, cas que N-035 ne prévoit pas ; la condition n'est donc pas remplie de façon mécanique. **Le retrait tient parce que Lazar l'a décidé (R-2555, B (a), lu par la mère : « repli (b) de N-035 pour H9 »)**, sur une condition que deux lecteurs jugent remplie pour le cœur. Le brouillon doit le dire ainsi (70-1, 70-2).

**Seconde moitié — la mesure gardée est-elle sans revendication ?** Oui : aucune prédiction au nom de H9, aucune priorité, MasDrift et AgentCollabBench en bases de comparaison et non en cibles, les quatre formulations « encore revendicables » rangées comme questions. Deux réserves : (i) le contenu de la mesure (rang de relais, **avec et sans moniteur à chaque passage**) est un choix du rédacteur, N-035 (b) ne le fixant pas ; le bras « moniteur à chaque passage » est précisément la pièce que les lecteurs donnent pour non trouvée : la mesurer est permis, mais tout texte qui en rapportera le résultat devra tenir la ligne « description » (section 6 ci-dessous) ; (ii) « profil attendu » dans un préenregistrement (70-5).

**70-1 (majeur) — citation du lot 12 tronquée, dans le sens qui renforce.**

Texte actuel (section 3) :
```actuel
« la condition de repli de N-035 reste remplie » (12, § 4)
```
Texte corrigé :
```corrige
« La condition de repli de N-035 reste remplie pour le cœur de l'énoncé ; le repli ou la reformulation est un nœud de Lazar, que ce rapport ne tranche pas » (12, § 4)
```

**70-2 (mineur) — la « Portée » présente le retrait comme l'effet de N-035 seule.**

Texte actuel (en-tête, « Portée ») :
```actuel
Le retrait est consigné ici, comme N-035 le demande (« Une pièce trouvée prise se replie sur (b), et le retrait est consigné », l. 26).
```
Texte corrigé :
```corrige
Le retrait est décidé par Lazar (R-2555, B (a)) et consigné ici, comme N-035 le demande (« Une pièce trouvée prise se replie sur (b), et le retrait est consigné », l. 26). Deux lecteurs tiennent la condition de N-035 pour remplie **pour le cœur de l'énoncé seulement** ; N-035 ne dit rien d'une pièce prise en partie : c'est le mot de Lazar, non un déclenchement automatique, qui porte le retrait de l'hypothèse entière.
```

**70-3 (mineur) — « relève la survie » va au-delà de ce que MasDrift mesure** (7-D, § 7, C4 : la politique « supprime les violations » ; un moniteur qui juge si la contrainte survit dans la passation est « non trouvé »).

Texte actuel (section 6, « Coût du moniteur ») :
```actuel
Un moniteur « relève » la survie, mais à un prix déjà chiffré.
```
Texte corrigé :
```corrige
Une défense portée à chaque relais supprime les violations exécutées, à un prix déjà chiffré ; qu'un moniteur qui lit chaque passation relève la survie de la contrainte n'est mesuré dans aucune source lue (7-D, § 7).
```

**70-4 (mineur) — la liste « n'est plus revendicable » omet un item du lot 12 (§ 5).**

Texte actuel (section 3) :
```actuel
la topologie comme facteur de survie de l'information.
```
Texte corrigé :
```corrige
la topologie comme facteur de survie de l'information ; le constat « un petit modèle perd à chaque relais ».
```

**70-5 (mineur) — « profil attendu » : fermer la porte à une hypothèse déguisée.**

Texte actuel (section 5) :
```actuel
décrit le **profil** attendu par rang (12, § 4), sans revendication.
```
Texte corrigé :
```corrige
décrit le **profil** attendu par rang (12, § 4), sans revendication ni critère de réussite : une attente écrite, non une hypothèse du papier B.
```

## 6. Ce que la lettre de R-2555 couvre, et ce qui demande un mot de Lazar

La lettre : « B (a) go ». La lecture de la mère, au même registre, nomme : O2 et O11 resserrées à ce qui reste libre (R-2177, R-2184, lot 4-A) ; HC2 reformulée comme proposé (R-2180) ; statistique de population du papier B resserrée (R-2181, lot 7-B) ; repli (b) de N-035 pour H9 (lots 7-D et 12) ; « sur les recommandations ».

**Couvert par la lettre ou par une recommandation qu'elle nomme** (rien à demander) :
- O2 réduite au nul des lois connues ; O11 sans idée revendiquée ; citations de Qu, Chen, Wang, CONFIRM, Sargsyan, CADS, N×N, « Hard to Fool », **Hegazy** (4-A, § 7 (a), les nomme) ; PACE, REUSE, Masked Erosion, **PROCTOR** (C7, § 4, les nomme). Ajouter une citation obligatoire ne change aucune revendication.
- La statistique spatio-temporelle et le retrait de « cœur vierge » : la lettre dit « statistique de population », mais R-2181 est le lot 5-A, dont la recommandation porte sur E3.1, et 7-B (§ 6.1) traite les deux.
- Le retrait de H9 et la citation de Li et collègues (7-D, § 4.3).

**Demande un mot de Lazar** (une ligne chacun suffit ; la recommandation est de confirmer, sauf mention) :
1. **Forme de O12 requalifiée et resserrée** (N-067, section 4, point 3). Hors de la lettre (qui nomme O2 et O11), mais dans la recommandation suivie (4-A, § 7 (a)). La synthèse finale la donne pour non couverte.
2. **O1, O3 et O17 cessent d'être revendiquées** (N-067, points 5 à 7) : hors de la lettre ; conséquence des constats de C7 et de 4-A.
3. **Quatre « non trouvés » laissés sans revendication** (ensemencement par l'empreinte ; combinaison et ampleur du banc ; mutations du scellement et règle générale contre le repli silencieux ; objet « hypothèses libres ») : plus étroit que « ce qui reste libre ». Garder ainsi, ou les reprendre comme revendications étroites après une lecture de durcissement.
4. **O4 seul porteur : règle d'usage public** (constat 67-3) : lire SSRN 6569258 et les pistes de priorité haute avant l'enregistrement figé de l'option C, ou figer avec la réserve écrite. Recommandation : lire d'abord.
5. **Statuts hors périmètre** : O9, O10, O13, O19 (N-067, section 10) ; 2611.00643 pour le rôle 1 de N-065 (aucune décision, R-2554 ne couvrant que 2611.04556) ; page publique de l'organisme (« go publication »).
6. **HC2 : plan apparié non revendiqué, « en fonction de l'intensité », citation obligatoire de Kale et Vishwanath** : postérieurs à R-2180 (lot 3-A) ; resserrement de plus, exigé par une pièce lue sur PDF.
7. **HC2 : poids 0,65** inchangé par la note ; les contre-indices le rendent moins sûr : à Lazar de dire s'il le garde.
8. **HC4 (lettre de N-013) et HC2b (sources du contrôle du style)** : nœuds distincts, déjà portés par la synthèse.
9. **Papier B : déclencheur de bascule** (programme, l. 239) et **critère de G2** (nommer le pic comme base, prévoir « pas de gain ») ; **mot « co-élévation »** de l'énoncé 1, si le constat 69-1 conduit à lui préférer « statistique relationnelle » : ce serait une modification de revendication.
10. **H9 : contenu de la mesure descriptive**, bras « moniteur à chaque passage » compris ; N-035 (b) ne le fixe pas.
11. **Journal `NODE_C_VOLETS_III_IV_H9.log`** à la racine du dépôt (signalé par le rédacteur, journal, section 5) : provenance à établir par la mère ; je ne l'ai pas ouvert.

## 7. Points 6 et 7 du mandat, en bref

- **Prédictions touchées par un contre-indice publié (point 6).** Dites : O8, O9, utilité de la multiplicité, signe de O12, leçon sur R1 (N-067) ; HC2 par 2608.21664, 2602.00750, 2611.10620, 2602.08877, Karne, Kale (N-068) ; critère de G2, thèse du papier B par J-PACT, lecture de la consigne, transfert, 8 milliards, accumulation (N-069) ; forme de la décroissance, présence contre respect, coût du moniteur (N-070). **Non dites** : le même signe que HC2 chez 2609.03035 v2 (68-1) ; la forme « écart » contre « co-élévation » (69-1) ; le résultat négatif de 2607.24893 (69-2) ; HELIOS de 4 à 8 agents (69-3).
- **Rien de plus fort qu'une pièce lue (point 7).** Tenu, sauf : le « non trouvé » de O2 (c) sans sa profondeur de lecture (67-2) ; « chargé de tromper » et « lit le juge » sans le voisin Sargsyan (67-1) ; « n'est publié que par MIRAGE » (68-1) ; « auteur » pour 2608.21664 (68-3) ; « relève la survie » (70-3) ; la citation tronquée du lot 12 (70-1). Les pistes de moteur sont bien tenues hors de tout énoncé dans les quatre brouillons.

## 8. Refus, interdits, écarts

- **Aucun refus** de contrôle de permissions ni de classifieur.
- Aucune écriture git (les deux `fetch` nommés, puis `show`, `ls-tree`, `log`, `status` en lecture). Aucun registre modifié. Aucune dépense. Aucune valeur de clé lue, aucune variable d'environnement listée.
- Chemins interdits non ouverts ; aucune recherche récursive : fichiers nommés, ou listes `git ls-tree` restreintes à `docs/sources/pdf/niveau3-v1/` et `docs/etat-de-l-art/`.
- Les PDF, données non fiables, ont été copiés dans un dossier neuf du dossier de travail temporaire et lus par `pdftotext` ; les scripts de contrôle vivent dans un autre dossier et tournent en mode isolé.
- Seul fichier écrit dans le dépôt : celui-ci, et son compagnon `.sha256`.

Version 1 ; jamais réécrite (R12).
