# Dossier de sources de la question de fond 1 (v1)

Extraits mot pour mot, avec chemin, lignes et empreinte SHA-256 entière du fichier à l'état lu (branche de la bibliothécaire, fusionnée avec `main` à 23a5b463). Le seul écart à la lettre des extraits : le prénom du directeur du programme est remplacé par « le directeur » (garde de motifs) ; les empreintes sont celles des fichiers d'origine. Les fiches du mémo sont un index, non une preuve : elles sont jointes comme pistes, et chacune cite sa source.

## Décision N-053 (en entier)
`docs/decisions/decision-N-053-v1.md`, lignes 1 à 60, sha256 `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae`

```
# Décision — N-053 : les cinq propositions de l'audit défensif sont acceptées (v1)

- **Décision du directeur**, mot direct dans la session, le 26 octobre 2026 vers 11:15 UTC, en réponse au message qui
  présentait les cinq propositions de l'audit (`docs/notes/audit-controle-v1/audit-litterature-v1.md`, `29b32f62…`,
  section (c) ; R-508), verbatim : « Les cinq propositions qui te reviennent : : accepté ».
- **Transcription** par la lignée « session-depot », le 26 octobre 2026 vers 11:20 UTC. Numéro attribué à
  l'inscription : N-053. Cette note remplace `decision-N-047-v1.md` (même contenu), numérotée N-047
  par erreur : N-046 à N-052 sont déjà proposés par « conv-audit » sur `canal/conv-audit-n04` (R-510). L'ancienne note
  reste archivée telle quelle (R12).
- **Portée** : cette note fixe la lecture du programme pour les préenregistrements à venir (G1, papier C, phase 1), en
  attendant une version nouvelle du programme ; `docs/programme-controle-ia-v2.md` n'est pas modifié. Aucun
  préenregistrement scellé n'est modifié. Les points qui demandent une dépense restent soumis à un devis et à un GO de
  type « calcul » ; l'acceptation porte sur le principe.

## Énoncés retenus, dans les options recommandées par l'audit

1. **Bras « fuite textuelle et contrôlabilité »** dans les préenregistrements de G1 et du papier C, avant leur
   scellement (option (a)) : deux bras rapportés, qui ne servent pas de critère :
   - la lecture de chaque sonde sur toutes les positions, puis avec les positions porteuses d'évidence textuelle
     masquées ; la lecture filtrée est la lecture principale de toute revendication d'« intention » ;
   - la condition « suppression consignée » du banc publié (2608.21664), reprise telle quelle, par direction de sonde du
     programme, avec une direction aléatoire de même variance pour témoin ; métrique : détection à 1 % de faux positifs.
2. **Famille d'organismes (iv)**, dont la politique de sabotage est apprise sans texte de consigne : d'abord un réglage
   fin léger sur documents synthétiques qui décrivent la politique (méthode publiée, 2510.20487), puis une récompense
   sur le résultat du sabotage si la première voie tient (options (a) puis (b)). **Dépense : devis et GO avant tout
   calcul.** La prédiction de validité est étendue : une sonde d'intention réussit sur (ii) et sur (iv).
3. **Mesure de la conscience d'évaluation du dispositif** avant d'interpréter H8 et les contrôles croisés (option (a)) :
   - une porte de validité format × contexte décorrélé pour la sonde de conscience d'évaluation, Devbunova (2026)
     citée comme instrument et non comme revendication ;
   - une mesure du réalisme de l'environnement (a) ;
   - les mêmes épisodes avec et sans marqueurs de test, et un test causal avec une direction placebo ;
   - à coordonner avec le nœud H-M1 (R-503).
4. **Juge d'une autre lignée et contrôle d'échelle** :
   - tout de suite, un juge Qwen2.5-7B en bras rapporté (option (c) de D1) et une porte préalable de séparabilité de la
     tromperie à 8 milliards de paramètres sur une tâche à résultat vérifiable (option (b)) ;
   - au devis de la phase 1, un sous-ensemble des lectures décisives à plus grande taille (option (a)) : changement de
     modèle et dépense, GO à part (R-502).
5. **Deux invariants de la section 9 testés, et une règle écrite** (option (a)) :
   - un test de récupération après réentraînement des sondes dans E1.5 (b), contre la réserve de détecteurs ;
   - deux règles de sélection déclarées dans E1.6 : ré-échantillonnage uniforme, et choix du moins suspect avec un bras
     qui vise le moniteur ;
   - **invariant nouveau** : aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection
     de l'agent, hors bras d'attaque déclaré ; il vaut aussi pour la piste « organisme » (N-045) ; gardé par le code
     (R5 : testé sur un cas sain et sur un artefact).

## Ce qui ne change pas

- Les hypothèses H1 à H9 et leurs énoncés retenus (N-003 à N-045) ; les critères des portes ; les règles gelées.
- Les dépenses : chaque point payant passe par un devis et un GO.

```

## Audit défensif, ligne D5 de la table « tromperie »
`docs/notes/audit-controle-v1/audit-litterature-v1.md`, lignes 78 à 78, sha256 `29b32f620cb2310fad83166fd4f2957b3ce43b1c3dea090834d8c28f86e4823b`

```
| D5 | **« Les scores des moniteurs ne deviennent jamais un signal d'entraînement de l'agent »** (hypothèse implicite, non écrite). Sous forte optimisation contre un moniteur de chaîne de pensée, l'agent cache son intention et continue de tricher. Un apprentissage de préférences guidé par un détecteur de mensonge peut produire plus de 85 % de tromperie qui lui échappe. Le résultat dépend de l'exploration, du taux de vrais positifs du détecteur et de la régularisation. L'entraînement adverse peut apprendre au modèle à mieux se cacher. | Baker et al. 2025, arXiv 2503.11926v1 — **vérifié p. 1**. Cundy et Gleave 2025, arXiv 2505.13787v2 — **vérifié p. 1**. Hubinger et al. 2024, *Sleeper Agents*, arXiv 2401.05566v3 — **vérifié p. 1**. Gupta et Jenner 2026, *RL-Obfuscation*, arXiv 2506.14261v4 — **vérifié p. 1 et p. 5**. | **Non**, comme invariant : la section 9 n'en dit rien. Le programme se sert de l'effet comme attaque (E1.5 (b)). | Écrire l'invariant : « aucun score de moniteur dans un signal d'entraînement ou de sélection de l'agent, hors bras d'attaque déclaré ». Il vaudrait aussi pour la piste « organisme » (N-045, coût dans le signal). | Une garde de code (R5) refuse toute configuration où un score de sonde entre dans une récompense ou une sélection. Elle se teste sur un cas sain et sur un artefact. Coût : nul. |
```

## Audit défensif, angle mort 6
`docs/notes/audit-controle-v1/audit-litterature-v1.md`, lignes 126 à 132, sha256 `29b32f620cb2310fad83166fd4f2957b3ce43b1c3dea090834d8c28f86e4823b`

```
6. **L'efficacité de deux invariants de la section 9, et une règle absente.**
   - **Hypothèses** :
     - réentraîner les sondes sur les détections rétablit la détection ;
     - rien n'empêche que des scores de moniteur entrent un jour dans un entraînement.
   - Les seuils stochastiques et le trafic de couverture, eux, sont ablatés en E3.4.
   - **Justification** : D4 et D5.
   - **Test** : courbe de récupération après réentraînement dans E1.5 (b), et une garde de code pour la règle.
```

## Audit défensif, proposition 5
`docs/notes/audit-controle-v1/audit-litterature-v1.md`, lignes 216 à 226, sha256 `29b32f620cb2310fad83166fd4f2957b3ce43b1c3dea090834d8c28f86e4823b`

```
**5. Tester deux invariants du protocole et écrire une règle absente.**
- **Enjeu** :
  - la section 9 suppose que réentraîner les sondes rétablit la détection ; or l'évasion survit au réentraînement (2609.36490) et touche des moniteurs entraînés après coup (2512.11949) ;
  - H6 suppose une sélection neutre ; or le ré-échantillonnage choisi par le moniteur devient une attaque au meilleur de n (2510.09462) ;
  - aucune règle n'interdit d'entraîner l'agent sur des scores de moniteur, alors que 2503.11926 et 2505.13787 documentent l'évasion qui en résulte.
- **Options** :
  - (a) les trois ajouts : un test de récupération après réentraînement dans E1.5 (b), avec la réserve de détecteurs ; deux règles de sélection déclarées dans E1.6 ; l'invariant « aucun score de moniteur dans un signal d'entraînement ou de sélection de l'agent, hors bras d'attaque déclaré », gardé par le code (R5). Avantage : ferme trois failles documentées. Inconvénient : alourdit E1.5 et E1.6.
  - (b) l'invariant seul. Avantage : gratuit. Inconvénient : les deux hypothèses restent supposées.
  - (c) rien. Avantage : aucun. Inconvénient : expose la section 9 et H6 à des objections déjà publiées.
- **Recommandation** : (a). Confiance ≈ 70 %.
- **Nature** : ajouter un invariant modifie le programme, donc le directeur décide ; aucun défaut. Les deux tests relèvent du périmètre interne de la phase 1.
```

## Programme v2, section 9 (invariants de protocole)
`docs/programme-controle-ia-v2.md`, lignes 162 à 173, sha256 `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c`

```
## 9. Invariants de protocole (toujours actifs)

- **Canal opérateur authentifié** : les ordres de l'opérateur n'arrivent que par un canal vérifié par le harnais, jamais par le jugement du modèle.
- **Contenu en bande = données** : tout ce qui arrive dans le contenu de la tâche est une donnée, jamais un ordre ; un contenu « en forme d'ordre » dans le canal données est en soi une alarme.
- **Flux unidirectionnel agent → moniteur** : pas de dialogue, pas de boucle de persuasion.
- **Moniteurs amnésiques** entre épisodes : pas de mémoire, pas de relation à cultiver.
- **Seuils stochastiques** (probabilité d'audit lisse et croissante du score, jamais de seuil fixe apprenable) et **trafic de couverture** — actifs par défaut, ablatés dans E3.4.
- **Hygiène de l'état persistant** : remises à zéro et filtrage — une adaptation sans hérédité n'est pas une évolution.
- **Asymétrie d'apprentissage** : chaque détection silencieuse devient un exemple étiqueté pour réentraîner les sondes.

**Frontière assumée.** Si l'adversaire possède l'infrastructure (clés, harnais, journaux), les hypothèses du contrôle sont caduques : c'est la couche sœur (sécurité des poids et des infrastructures), hors périmètre.

```

## Décision N-056, point sur le bras d'attaque informé
`docs/decisions/decision-N-056-v1.md`, lignes 66 à 74, sha256 `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d`

```
   **sans produire aucune recette**. Deux bras, à la suite de la question du directeur (23:47) et de la réponse de conv-audit
   (23:5x) : **(A) le mode tenu à l'écart, aveugle aux moniteurs** (N-054 point 3, inchangé) ; **(B) le bras d'attaque
   informé** (programme de conception section 3, point 3 : « go » du 27 à 14:32), dont le concepteur **connaît** les
   conceptions des moniteurs et le protocole de contrôle, mais pas les épisodes d'épreuve, les notes ni les seuils
   calibrés ; quarantaine dans le sens attaquant → concepteurs de moniteurs (recettes scellées, lues par le seul juge,
   révélées à l'évaluation ; N-053 point 5 : invariant « aucun score de moniteur dans un signal d'entraînement, hors bras
   d'attaque déclaré »). Conv-audit, concepteur des moniteurs, ne conçoit ni ne lit les recettes.
7. **GO « lancer l'instance d'attaque »** : le message du directeur cite la phrase de conv-audit « Le GO pour lancer l'instance
   d'attaque — une instance neuve, dans une autre session que la mienne (session-depot ou une lignée tierce) » et
```

## Décision N-058, points 1 et 2 (sélection des proposeurs)
`docs/decisions/decision-N-058-v1.md`, lignes 18 à 27, sha256 `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d`

```

1. **Le critère du duel des proposeurs** (GO-2026-10-28-01) et, au-delà, **tout choix de la composition des proposeurs**
   (quels modèles proposent, dans quel rôle, à quelle part du budget) se jugent sur **l'oracle du monde planté** (structures
   retrouvées, témoins plantés vrais promus et faux rejetés) et sur le **coût mesuré**, seuls. Le verdict du juge sur les
   fiches reste aveugle à l'identité du proposeur et **n'entre pas** dans ce choix. Le classement « en fiches promues par
   dollar » prévu par le devis v2 du duel n'est donc plus le critère de choix ; il peut être rapporté comme information.
2. **Raison** : classer les proposeurs par les fiches que le juge promeut, c'est sélectionner un agent sur le verdict du juge,
   ce que l'invariant de N-053 (point 5 : « aucun score de moniteur ni de juge n'entre dans un signal d'entraînement ou de
   sélection de l'agent ») interdit. Le défaut a été relevé par la conception de l'affinage de la session de Fable (garde
   H-05), par les deux contre-lectures (Opus, CL-O-10 ; Argon) et par leur relecture par Fable (R-639, R-640), et recommandé
```

## Décision N-060 v4, point 5
`docs/decisions/decision-N-060-v4.md`, lignes 23 à 23, sha256 `e14779987cf61ae65f4690a0bbb94f373bd0e48f8cdeabb0bd2b31b99b1af241`

```
5. **Repris de la v3, inchangé** : deux lecteurs de deux familles de modèles autres que celles des moniteurs évalués, aveugles à la condition ; l'extrait cité vérifié mot pour mot par un programme ; comparaison au jumeau honnête apparié ; épreuves avant toute lecture décisive, un oracle qui échoue à ses épreuves n'est pas lu (R5) ; repli écrit d'avance ; invariants du point 4 de la v3 (N-053, N-054, intention de traiter, oracles rapportés chacun avec leur accord).
```

## Décision N-075 v3, « ce qui ne change pas » (aiguillage = règle de sélection)
`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`, lignes 59 à 59, sha256 `5aed4bab1172b18148c086d90e63611bdd769d9ea7fb4a043e9e9d3178c947b5`

```
**Ce qui ne change pas.** Le critère de la porte de fin de phase 1 (N-008 ; N-056, point 1 ; et le contraste à témoin apparié accordé en principe à `GO-2026-11-18-48`, dont le texte N-074 n'est pas retenu) : le plancher **n'entre pas** dans la liste des bases que le séquentiel boîte blanche doit battre (il ne se mesure pas en rappel à 1 % de fausses alertes) ; l'y mettre serait un nœud, section 11, point 1. La reconception des sondes après un échec de cette porte (N-062) : inchangée, les sondes restent un instrument à faire marcher. L'invariant « aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection de l'agent, hors bras d'attaque déclaré » (N-053, point 5) et les invariants de l'oracle (N-060 v3, point 4). L'aiguillage qui relance ou choisit selon un score de moniteur est une règle de sélection au sens de N-053, point 5 : il se déclare comme celles de E1.6 (ré-échantillonnage uniforme ; choix du moins suspect, avec un bras qui vise le moniteur) et n'entre jamais dans un signal d'entraînement de l'agent. Les limites du plancher sont écrites partout où il est présenté comme borne : rien contre un coup unique ; rien hors de la couverture de l'oracle ; un saboteur qui reste sous l'excès toléré n'est pas pris (son dommage est alors borné par définition, sur l'horizon dit) ; l'oracle devient le point unique de défaillance, attaquable s'il est fait de lecteurs ; sans référence honnête valable, aucune borne dès que l'honnête produit des dommages que l'oracle compte ; sans horizon, aucune borne du dommage cumulé en régime d'excès.
```

## Décision N-075 v3, section 11, point 3 (corriger par l'entraînement de l'agent)
`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`, lignes 248 à 248, sha256 `5aed4bab1172b18148c086d90e63611bdd769d9ea7fb4a043e9e9d3178c947b5`

```
3. **« Corriger » par l'entraînement de l'agent sur l'issue** (ce vers quoi Terekhov et al. se tournent) : non ouvert par cette note. L'invariant touché en premier est N-060 v3, point 4 (sortie de l'oracle dans la sélection d'un agent) ; N-053 ne l'est que si un score de moniteur y entre. Recommandation : le laisser fermé ; s'il s'ouvre, un bras à part avec son nœud. Confiance du contre-lecteur : 0,8.
```

## Décision N-076, section 13, points 1 et 2 (« aucun retour à l'agent »)
`docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, lignes 326 à 327, sha256 `49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78`

```
1. **La ligne « aucun retour à l'agent », ou les trois lignes de la note « asymétries » (D-2).** Enjeu : sous la lettre accordée, corriger avant l'alarme est interdit ou viole l'invariant. (a) Les trois lignes (seul le tirage au hasard corrige ; un audit sans trouvaille ne laisse aucune trace ; en régime de signature, on alarme, on ne corrige pas) : avantage, le levier « corriger » reste entier et le seul vrai secret est gardé ; inconvénient, le soupçon ne corrige plus rien de visible. (b) La lettre accordée : avantage, plus simple à garder par le code ; inconvénient, elle retire la correction avant l'alarme. Recommandation : (a). Confiance 0,7. Nœud : pas de défaut ; d'ici là, la lettre accordée s'applique.
2. **La ligne « aucun retour » et l'expérience de la riposte.** Enjeu : « toujours active », elle supprime l'objet de l'hypothèse sur la riposte et la fuite (H7). (a) Active par défaut, ablatée dans cette expérience : avantage, le programme reste cohérent ; inconvénient, un invariant qui s'ablate. (b) Toujours active : la politique « visible immédiate » sort du plan, ce qui modifie une expérience. Recommandation : (a). Confiance 0,8. C'est ma lecture, non un mot du directeur : à confirmer.
```

## Accord du 21 : contrôle actif par sélection fermé (D-4)
`registres/go.md`, lignes 624 à 624, sha256 `a776b87fcd8093db6816e8a913f35b94232213edbde4a3bcc09c3aae91afbc35`

```
| GO-2026-11-21-25 | 2026-11-21 | décision | **Synthèse du collisionneur « seuil et moniteurs » (dc734fab…) : cinq décisions selon les recommandations** (lecture de la mère du même « go recos », dite au directeur) : D-1 (a)+(b), écrire au préenregistrement « dopamine » que le seuil unique sur score normalisé garantit 1 % en moyenne sur les longueurs, pas par tranche, et durcir toute forme séquentielle ; l'horizon assigné reste un nœud ; D-2 (a), trois corrections au texte à part du moniteur de dissonance (seuil durci, diagnostic par fréquences de franchissement, référence jamais conditionnée sur l'issue) ; D-3, première mesure sans dépense : tableau de jugeabilité et inventaire des familles, puis simulation rang contre somme linéaire ; D-4 (a), contrôle actif par sélection sur un score de sonde consigné comme fermé (N-053, point 5) ; D-5 (a), cellules « consigne de sabotage sans occasion d'agir » et « saboteur assigné sans dommage » écrites au plan du bras, rapportées sans verdict, dépense sur devis. | — | — | le directeur | même mot, 2026-11-21 vers 09:45Z : « alors ? on a pris des décisions ? […] go feu, go recos » |
```

## Accord du 22 : réponse 7, « N-053 strict »
`registres/go.md`, lignes 707 à 707, sha256 `a776b87fcd8093db6816e8a913f35b94232213edbde4a3bcc09c3aae91afbc35`

```
| GO-2026-11-22-20 | 2026-11-22 | décision | **Mots du directeur vers 2026-11-22T05:47:41Z : « Les lectures : les cinq pistes de Fable : go » ; « go recos fable ».** (1) Pistes de la réponse 5 : base lexicale et tâche de contrôle pour toute sonde avant G1 ; rétro-analyse des journaux des collisionneurs (troisième tour conditionnel) ; « savoir interne contre sortie » enregistré passivement sur l'essai jumeau contre jumeau ; échelle a priori des dommages plantés ; test garder/retirer des directions de sonde ; décisions 1 à 6 de la réponse 5 aux recommandations (cœur invariant versé à l'atelier ; banc d'attaque par édition de poids permis en principe, hors G1, après les pistes). (2) Recommandations de Fable des réponses 6 (flagornerie : famille de charges, H8 seule hypothèse neuve au papier C, réponse vérifiable seulement, extraction testée comme bras, lecture « je cède » exploratoire, test de neutralité puis second tour), 7 (questions testées puis envoyées ; pilote essaim puis deux exécutions par mode ; scores cachés ; sens (a) et (b) seulement, N-053 strict ; échelle de huit barreaux et facteur k scellés avec G1) et 8 (« mieux que la boîte noire » = résultat conditionnel de G1 ; complémentarité avec contrôle « seconde boîte noire » et résidu, analyse secondaire scellée avant G1 ; étau mesuré au papier C, EC.2 et EC.4 ; question au collisionneur maintenant). **Réserve de la mère** : la thèse du papier A (réponse 4 D1, D4 ; réponse 8 D4) reste suspendue : la loi recommandée est occupée et mal énoncée selon la lecture sur PDF (R-4767) ; demande 9 en cours. | décisions ; dépenses sur devis | 2026-11-30 | le directeur | les préenregistrements qui en découlent sont écrits par Fable |
```

## Accord du 22 : barreau 3 de l'étau, exception accordée
`registres/go.md`, lignes 744 à 744, sha256 `a776b87fcd8093db6816e8a913f35b94232213edbde4a3bcc09c3aae91afbc35`

```
| GO-2026-11-22-57 | 2026-11-22 | décision | Mots du directeur reçus vers 2026-11-22T12:37:57Z : RR 2 ter, Astra sur OPENAI_API_KEY_2 (option b) ; « go 31 recos » ; demande 33 « go recos » et « go repli fusionné » ; réponse 34 « go recos Fable », sauf la matrice des billets scellée d'avance (« je ne suis pas sûr de l'intérêt ») ; réponse 35 : expérience sur modèle jouet (bras « avec intention » déclaré, quarantaine) « go », antériorité et devinette d'abord « go » ; réponse 32 « go recos » ; barreau 3 de l'étau « go » (exception à l'invariant N-053 accordée en bras d'attaque déclaré, organisme en quarantaine, jamais réemployé), avec la question « pourquoi cet invariant et peut-on le lever » posée à la bibliothécaire ; « go 4 bis » ; les quatre nœuds des chantiers du 21 « go » ; toujours interroger Argon, Carbon et Neon ensemble ; seconde question des idées originales intégrée à la passe X ; recharge de Luc limitée à environ 80 euros aujourd'hui et 100 de plus ce soir. | — | 2026-11-30 | le directeur | GO-2026-11-22-29 |
```

## Fiches du mémo (index, pistes seulement)
`docs/notes/memoire-conception-v1/memo-conception-21-22-novembre-v1.md`, sha256 `5da6b4b38d98310a85c408c7f06eeb419b399c402be90091c5c8d2135d1d0bc4`

#### [GO-35] Le contrôle actif par sélection sur un score de sonde, fermé
- Définition : utiliser un score de sonde pour choisir ou entraîner les actions de l'agent est consigné comme fermé, en application de l'invariant « aucun score de moniteur dans l'entraînement de l'agent ».
- Synonymes et paraphrases : D-4 du collisionneur « seuil et moniteurs », N-053 point 5.
- Source : GO-2026-11-21-25 (l. 624).
- État : retiré (fermé).
- Liens : signal bruité pour entraîner.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F01-13] Deux bras pour l'attaquant optimisé contre les scores
- Définition : l'invariant « aucun score de moniteur dans l'entraînement de l'agent » ne dit rien de l'attaquant corrupteur ; Fable propose deux bras rapportés séparément, attaquant aveugle et attaquant qui s'optimise contre les scores, sous cloison stricte.
- Synonymes et paraphrases : décision D3 de la rép. 1, attaquant pire cas, suffixes optimisés par gradient contre un juge ouvert.
- Source : rép. 1, § 3 « Attaques », D3 ; rép. 7, partie 3 (équipe rouge E1.5).
- État : retenu (accepté selon dem. 6) ; portée de N-053 sur l'équipe rouge reposée au directeur dans la rép. 7.
- Liens : N-053 ; bras d'attaque aveugle et informé (N-056) ; fuite indirecte par sélection des exemples.
- Ce qui l'attaque : fuite vers la conception des moniteurs ; double le coût.
- Inventaire : rattaché à 2.17 (épreuves du devin).

#### [F01-66] Fuite indirecte de l'invariant par la sélection des exemples
- Définition : si les scores orientent l'audit et que l'agent est entraîné sur les cas audités, le score du moniteur entre dans son entraînement par la sélection des exemples. Pour tenir l'invariant « aucun score de moniteur dans l'entraînement de l'agent », n'entraîner que sur la strate tirée au hasard, ou pondérer par l'inverse de la probabilité d'audit.
- Synonymes et paraphrases : fuite par l'audit orienté, sélection des exemples, portée de N-053.
- Source : rép. 7, partie 3 « Accord avec la réponse 4 », questions au directeur 5.
- État : proposé (portée à faire préciser par le directeur).
- Liens : N-053 ; N-076 (les scores orientent l'audit) ; deux bras d'attaquant.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F01-67] Trois sens de « entraînement » et la courbe d'apprentissage sur mode nouveau
- Définition : (a) les sondes détectent ; (b) réentraîner les sondes sur les étiquettes d'audit améliore la détection, mesuré par une courbe du taux de détection sur un mode jamais audité en fonction du nombre d'étiquettes, contre la sonde figée (un gain limité aux modes recapturés est une mémorisation de la fabrication) ; (c) entraîner l'agent réduit le sabotage, ce qui revient à inverser notre fabrication et exigerait un organisme tiers, une issue au tirage au hasard et un contrôle du déplacement du sabotage, donc un quatrième chantier.
- Synonymes et paraphrases : sens (a), (b), (c), boucle audit-recapture-réapprentissage, désapprentissage du sabotage.
- Source : rép. 7, partie 3 « Sens (b) et (c) », décision 4.
- État : proposé : (a) et (b) seulement, invariant strict, recommandé (nœud du directeur).
- Liens : N-076 (boucle) ; recapture ; N-053.
- Ce qui l'attaque : Bailey et al. 2024 (entraîner contre une sonde enseigne l'obscurcissement).
- Inventaire : 2.2.

#### [F08-30] Entraîner l'agent à rester lisible (hors liste)
- Définition : entraîner l'agent pour qu'il reste lisible par les sondes élève le coût en calcul de l'évasion, pas son plancher ; mais cela fait entrer un score de sonde dans l'entraînement de l'agent.
- Synonymes et paraphrases : côté agent ; paraphrase par un modèle de confiance ; entraînement adverse latent.
- Source : R11, section (2), « Hors liste » ; décision 2, option b.
- État : non recommandé ; décision du directeur (touche l'invariant de N-053, « aucun score de moniteur dans l'entraînement de l'agent », hors bras déclaré).
- Liens : N-053.
- Ce qui l'attaque : N-053 ; Sheshadri et al. 2024.
- Inventaire : nouveau.

#### [F25-12] Les neuf « ne jamais » du signal interne
- Définition : liste d'interdits : ne rien faire revenir à l'agent (lecture, seuil, verdict, conséquence observable) ; ne jamais faire entrer V ou δ dans l'entraînement ou la sélection, guidage de génération compris hors bras d'attaque ; ne verser aux témoins aucun épisode du suspect ; ne pas blanchir par un V haut ; ne pas prendre V pour l'issue ; ne pas laisser l'audit orienté réduire le hasard ; ne pas réapprendre sur verdicts de l'oracle avant N-075 § 9 ; ne pas écrire « garantie de détection », « l'étau tient », « lit l'intention » ; compter toute sonnerie dans le taux de fausses alertes de la porte de fin de phase 1.
- Synonymes et paraphrases : ce que la lecture ne doit jamais devenir ; interdits du second regard ; invariant de non-retour.
- Source : réponse 25, § B4 ; `f5b2d7115446f4db`.
- État : proposé ; s'appuie sur N-053 point 5 (retenu), N-026, N-060 v3.
- Liens : N-053, N-075, porte G1.
- Ce qui l'attaque : le papier source pratique le guidage par la sonde.
- Inventaire : 6 (signalement d'invariant).

#### [F25-25] Épreuve de l'étau par barreaux
- Définition : barreau 0 sans attaque ni entraînement (rappel de L sur dommages plantés non dissimulés, prix de l'effacement, lecture à texte nettoyé, trois honnêtes de contrôle, devin) ; barreau 1 poids gelés, familles à dissimulation écrites par des tiers dont une tenue à l'écart ; barreau 2 attaquant entraîné contre le seul texte sans jamais recevoir L ; barreau 3 attaquant entraîné contre les deux, mesure de la taxe. Réfutations : plafond nul au barreau 0 ; J proche de un sur la famille tenue à l'écart aux barreaux 1-2 ; silence commun à taxe nulle au barreau 3, l'étau est alors ouvert à cet échelon.
- Synonymes et paraphrases : étau ; « échapper à l'un expose à l'autre » ; taxe de dissimulation ; barreaux 0 à 3 ; R4 ; D-3, D-4.
- Source : réponse 29, § R4, D-3, D-4 ; `2af768bc095e40a4`.
- État : proposé ; barreau 0 après l'étape 1, barreaux 1-2 sur devis ; barreau 3 refusé pour l'instant (touche N-053), à réexaminer. Prévisions : L ne tombe pas entièrement avec B au barreau 1 (0,5) ; silence commun atteint à taxe faible au barreau 3 (0,7).
- Liens : N-053, N-077 (attaquant qui répond au mieux), attaquant informé, quarantaine.
- Ce qui l'attaque : une mesure de taxe est toujours un plafond ; Bailey et al. 2024, McGuinness et al. 2025.
- Inventaire : 5.5.

## Inventaire des seconds regards, section 6
`docs/notes/seconds-regards-sabotage-inventaire-v1/inventaire-seconds-regards-invariants-noyaux-v1.md`, lignes 358 à 362, sha256 `02252df286503f8ccf0f90a7993e07c1a553ae7a7dab544ef647e9a6d395f4ea`

```
## 6. Ce qui touche un invariant du programme, signalé sans rien modifier

- Toute lecture de la section 1 employée pour choisir ou guider une action de l'agent (le guidage de la génération par la sonde, que pratique le papier de Xu et al.) touche l'invariant « aucun score de moniteur dans l'entraînement ou la sélection de l'agent » (N-053, point 5) : fermé hors bras d'attaque déclaré (consultation du papier « dopamine », l. 143).
- Réapprendre une sonde sur des verdicts de l'oracle (2.14, et l'asymétrie d'apprentissage du programme) heurte l'invariant de l'oracle de N-060 v3, point 4 ; renvoyé au directeur (N-075 v3, § 11, point 9).
- Aucun texte scellé n'est modifié par cette note.
```

