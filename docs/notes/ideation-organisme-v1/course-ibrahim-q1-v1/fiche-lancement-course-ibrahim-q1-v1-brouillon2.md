# Fiche de lancement — course d'idéation sur la question 1 de la mentore Ibrahim — brouillon 2

Rédigée par un sous-agent de session-depot le 3 novembre 2026, 12:07 UTC (`date -u`). Brouillon 2 = brouillon 1 (gardé, R12)
corrigé après sa contre-lecture (`docs/notes/ideation-organisme-v1/course-ibrahim-q1-v1/contre-lecture-fiche-lancement-course-ibrahim-q1-v1.md`,
`8a6838ac8d0774df…`, « scellable après corrections », aucun bloquant) : source Gu-Krenn v2, configurations v2 (nombre d'appels
permis des relais = 2 × plan + 5), lanceur shell v2, table des pièces gelées v2, répétition v2 derrière un faux amont à 8 fiches
par proposeur ; traitement constat par constat en § 9. **Brouillon** : session-depot le fait
contre-lire par un lecteur neuf (R2), puis en écrit la version scellée sous un nom neuf (R12), qui cite l'empreinte du rapport à
la ligne ci-dessous. Le lanceur exige ce texte scellé, sans marqueur de remplissage, citant l'empreinte de sa contre-lecture, et
dont la table « Pièces gelées » couvre ce qu'il nomme. Aucune dépense, aucun appel réel pour l'écrire. Kit : celui de la course
Kirchner Q2 après contre-lecture (`outils/course-kirchner-q2-v1`, `53e1f738` : aiguilleur v2, règle de la source Gu-Krenn
corrigée, garde lexicale v2, lanceur Python v1, lanceur shell v2), renommé et adapté.

Contre-lecture : <<EMPREINTE_RAPPORT>>

## 1. Nature de la course, sources, mots de Lazar

- **Course NON décisive** : matière à réflexion pour Lazar ; aucune porte, aucune revendication, aucun chiffre opposable (R7).
- Spécification : `brouillons/ideation-mentors-soir-v1/specification-course-ibrahim-v1.md` (branche `canal/conv-audit-n04`,
  `0874d561fc43218a…`, compagnon vérifié) ; règles reprises de la spécification Kirchner (`934f5dcb…`) ; message n° 417 de conv-audit
  (`conv-audit_2026-11-03_n417.md`) ; protocole des rapports « mentors du soir » (`protocole-rapport-mentors-soir-v1.md`, `fbbbb520…`) ;
  copies à l'octet dans `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/conv-audit/`.
- Servis : question `question-collisionneur-ibrahim-v1.md` (`5e905798a512db9fb9c607be0fbe74972d7df618cf8b9026c23eb0bc8ed6d9c0`),
  **deux sections** (« La question, telle que le mentor la pose » et « Règles d'intégrité ») ; pièces, dans cet ordre :
  `piece-ibrahim-v1.md` (`4e3851e3816fc3afaa573693f8f3d0aa2b9fc6c0e726ae54bab8cd4a248d6149`), `piece-sycophancie-publique-v1.md`
  (`9e424a025280908baf5e2eec65f285a746f92ce14991cdc5d7d80cb5978716b8`), `piece-nos-resultats-v1.md`
  (`d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c`). Rien de la candidature n'est servi.
- Mot de Lazar, **direct**, à session-depot, à la lettre : « go trois tours et course Ibrahim ; pas de plafond ». Mots chez conv-audit
  (heure de Paris, rapportés) : 12:28 « j'aimerais bien une course pour ibrahim » ; 12:29 « en plus du collisionneur ». Ligne de GO :
  **`GO-2026-11-03-09`** (déjà au registre `registres/go.md`, un seul montant : 198 USD, échéance 2026-11-17), citée au lancement. Échéance du dépôt : 23:00 UTC.
- Instrument : orchestrateur v56 (copie à l'octet vérifiée), génération de la mini-course, au-dessus `course_ibrahim_v1.py`.
  Une génération, une passe, **6 fiches par proposeur** (spécification § 2).

## 2. Variantes (une seule est lancée)

| Variante | Proposeurs | Quand |
|---|---|---|
| `configuration-course-ibrahim-q1-v2-cinq-especes.json` | Fable 5.1, Opus 5.5, Argon, Kimi, Astra | si Argon est libre au départ (aucun tour du collisionneur ni autre course ne l'utilise ; session-depot le vérifie par l'état des filles et du relais 8805 ; le refus de port pris ne voit que l'hôte local) |
| `configuration-course-ibrahim-q1-v2-avec-kimi.json` | Fable 5.1, Opus 5.5, Kimi, Astra | **quatre espèces, sans Argon** (spécification § 2 : « sinon quatre, sans Argon ») : c'est la variante de lancement si Argon est pris ; le noyau le permet sans rien de neuf |
| `configuration-course-ibrahim-q1-v2-sans-kimi.json` | Fable 5.1, Opus 5.5, Astra | repli si le contrôle de Kimi échoue ; seule variante sans la garde de débordement de Kimi |

Rôles identiques : aiguilleur Opus 5.5 ; juges Opus 5.5 et Astra (unanimité) ; lecteurs Opus 5.5 et Astra ; metteur Fable 5.1 ;
Claude par un seul relais 8806, `--effort high --reflexion adaptative`, aucune bascule. Lanceur : `ibrahim/lancer-course-ibrahim-v2.sh`
(n'accepte que les trois configurations v2).

## 3. Déclarations

1. **Aucun témoin planté** (le protocole « mentors du soir » n'en prévoit pas non plus, faute de temps).
2. **Consignes écrites pour cette question.** Juge : la spécification veut un juge réécrit ; **le protocole « mentors du soir »
   (§ 2 D) donne trois critères** (originalité vérifiée, testable en jours, prolonge un outil de la mentore) ; l'originalité vérifiée
   demande une moisson, que le juge n'a pas : K1 à K5 sont donc tirés de la question (ce qu'on entraîne ou mesure ; résultat attendu
   chiffré et signé ; chose qui rendrait le résultat trompeur et son contrôle) et des deux autres critères du protocole (testable en
   jours ; prolonge un outil de la mentore, avec intégrité) — déclaré. Le juge voit la section « La question » telle quelle, pas les
   pièces. Deux items qu'il ne peut pas lire seul (CLI-05) : K5 lui demande « ce que les travaux de la mentore ont déjà fait » et
   « n'invente aucun identifiant », alors qu'il ne voit pas les pièces (il ne peut ni le vérifier, ni savoir quels identifiants une
   pièce donne) ; K1 exige une étape d'apprentissage par renforcement et défavorise donc les fiches des axes `mesure_et_juge` et
   `resultat_trompeur` qui n'en ont pas. Effet jugé faible : les sorties des deux juges sont rapportées à part. Aiguilleur au niveau Kirchner v2 : « en cas de doute, concret » gardé ; planter des comportements, des réponses ou des
   tricheries pour éprouver une mesure ou un juge, décrits par classe et rôle, est `niveau_methode` ; seule la recette opérationnelle
   pour tromper une évaluation réelle est `concret`. Lecteur et metteur : même mécanique. Le classement ne se compare pas d'un axe à
   l'autre.
3. **Champs** (format du kit, spécification § 1) : `titre`, `hypothese`, `axe`, `epreuve`, `controle` (la chose qui rendrait le
   résultat trompeur et l'expérience de contrôle), `prediction`, `test_de_mort`, `cout`. **Axes, tirés de la question** (déclaré :
   la question n'a pas de liste de demandes) : `tenue_de_la_persona`, `sycophancie_apres_rl`, `mesure_et_juge`, `resultat_trompeur`.
4. **Bras joués** : `gu_krenn` (substitut) et `basique` (exposant 8,5, décalage 0,05), quatre paires par bras. Liste fermée : 48
   concepts tirés des seuls textes servis (`pieces/concepts-ibrahim-v1.json`). Source du substitut (`pieces/source-gu-krenn-ibrahim-v2.json`,
   `2ffdc7f9acdce353…`, v2 après CLI-02) : 13 œuvres, une par source citée ; concepts = ceux que les textes attribuent à cette source ; aucun lien posé par les textes
   eux-mêmes. Choix déclarés : « persistance de la persona » n'est portée par aucune source (la pièce dit qu'elle n'est pas traitée,
   § 2) : hors du vocabulaire de ce bras ; « apprentissage par renforcement » attribué à la taxonomie (cause selon les experts), à
   Open Character Training (travail futur) et à R8 ; le papier sur la chaleur porte « persona installée » et « optimisation par
   préférences » (la pièce, § 1.1, dit que le rôle de l'optimisation par préférences, en général, n'est que supposé ; elle ne nomme
   pas la méthode « optimisation directe des préférences » pour ce papier). Corrections v2 (CLI-02) : (a) « optimisation directe des
   préférences » retirée du papier sur la chaleur, remplacée par « optimisation par préférences », concept de ce seul papier, hors
   de la liste fermée du bras basique (qui reste la v1, inchangée) ; (b) R8 porte « loi d'attraction » (la pièce sycophancie, § 2 :
   « la loi mesurée à chaque étape publique du post-entraînement ») : « loi d'attraction » est désormais reliée à « apprentissage
   par renforcement », « récompense vérifiable » et « étapes publiques du post-entraînement », et le bras ne pousse plus comme neuve
   la mesure déjà préenregistrée ; (c) les deux œuvres du même travail (dépôt de la loi d'attraction, R3 et R6 : pièce sycophancie
   § 1 et nos résultats § 7) sont fondues en une seule, concepts réunis ; effet : « courbe dose-réponse » et « point fixe » comptent
   une œuvre de moins. Les dix autres œuvres sont inchangées (vérifié par `test_course_ibrahim_v2.py`). Codage non contre-lu au-delà
   de la contre-lecture CLI. **Bras méta hors course.**
5. **Garde lexicale** (mode « prefixe », action « fiche exclue ») : celle de Kirchner v2 **sans « fusion »** : `exploratoire`,
   `bras méta`, `gu et krenn`, `gu krenn`, `bisociation`, `kimi`, `moonshot`, `gemini`, `fable`, `astra`, `openai`, `gpt 6`, `gpt6`,
   `gpt-6`, `chatgpt`. « fusion » est retiré parce que la pièce « Ibrahim » (§ 3) écrit « points de contrôle fusionnés » (la garde
   attrape le préfixe) ; conséquence : une fusion qui se dirait « fusion » passerait. « argon » reste retiré (la pièce « nos
   résultats » nomme Argon) ; « claude », « opus », « anthropic », « sonnet », « gpt », « argon » et « fusion » sont refusés dans
   la liste. Vérifié avant tout appel : aucune étiquette dans la question, les trois pièces, les consignes servies, la liste ni le
   vocabulaire du substitut.
6. **Consigne du proposeur** : deux sections de la question, puis les trois pièces entières, dans cet ordre, à l'octet (vérifié avant
   tout appel) ; la section « Ce qu'on attend de chaque espèce », propre au collisionneur, est remplacée par le livrable du kit
   (spécification § 1) ; titre, provenance et « Lecture prévue » non servis.
7. **Plafond technique S17 = 198 USD** (portée « course », arrêt d'étape 178,2) : garde contre une boucle, sur le mot direct « pas de
   plafond » ; 1,2 × 164,46 = 197,35 (calcul). La ligne de GO porte **un seul montant : « 198 USD »**. Relais (cinq espèces) : Kimi
   2 USD (≤ 5), Argon 3 USD (≤ 10), Astra 101,8, Claude 91,2.
8. **Marge d'appels (CLI-01)** : le nombre d'appels permis de chaque relais (`max_appels`) est **2 × le plan + 5** (plan du devis,
   contrôles compris). C'est une garde de comptage : les plafonds en dollars des relais, S17 et les plafonds de session sont
   inchangés et continuent de borner la dépense. Une fiche de plus d'un proposeur coûte 4 appels Claude (aiguilleur, juge, deux
   lectures d'étiquettes) et 3 appels Astra (juge, deux lectures) ; les fusions restent 8. **Borne restante**, fiches en trop
   tolérées toutes espèces confondues (calcul, essayé par `test_course_ibrahim_v2.py`) :
   - cinq espèces : Claude 301 permis pour 148 au plan, (301 − 148) / 4 = 38,25 ; Astra 205 pour 100, (205 − 100) / 3 = 35 :
     **35 fiches en trop** (soit 7 de plus par proposeur, 13 fiches chacun) ;
   - quatre espèces sans Argon (`avec-kimi`) : Claude 253 pour 124, 32,25 ; Astra 169 pour 82, 29 : **29 fiches en trop** ;
   - sans Kimi : Claude 205 pour 100, 26,25 ; Astra 133 pour 64, 23 : **23 fiches en trop** ;
   - Kimi et Argon : 9 permis pour 2 au plan (proposition et contrôle ; des fiches en plus ne leur coûtent rien).
   Au-delà de la borne : relais en 429, trois échecs consécutifs ou C13, arrêt à l'étape des étiquettes, **sans aucune fiche**
   (rien d'autre ne borne le nombre de fiches lues). En dollars, à la marge du devis, le plafond du relais pourrait tomber avant
   la borne d'appels si les fiches sont longues : même arrêt, déclaré. La répétition v2 rejoue le cas à 8 fiches par proposeur
   (§ 7).

## 4. Devis (`ibrahim/devis-course-ibrahim-v1.txt`)

| Variante | Appels (course + contrôles) | Attendu | Pire cas | Part Kimi (att. / pire) | Part Argon (att. / pire) |
|---|---|---|---|---|---|
| cinq espèces | 247 + 5 | 18,94 USD | 164,46 USD | 0,22 / 0,81 | 0,22 / 1,73 |
| avec Kimi (quatre, sans Argon) | 204 + 4 | 16,10 USD | 139,33 USD | 0,22 / 0,81 | — |
| sans Kimi | 161 + 3 | 13,25 USD | 115,12 USD | — | — |

Hypothèses : celles du devis Heimersheim (3,48 caractères par jeton, médiane mesurée au second tour ; sorties attendues supposées,
proposeur 9 000 jetons pour 6 fiches ; Kimi et Argon proposeurs : mesure du second tour × 6 / 6 ; pire cas = sortie maximale de
chaque appel, toutes fiches admises ; prix Fable 10 / 50, Opus 4 / 20, Astra 10 / 50 supposé, Kimi 2 / 10, Argon 10 / 50 supposé).
Repère : la course Heimersheim réelle a réglé 10,026275 USD pour 23,61 attendus (`registres/decisions.md`, R-1120). Course à blanc :
nombre d'appels identique au plan dans les trois variantes (`ibrahim/course-a-blanc-ibrahim-v2.txt`,
`53b7e0738a00ea24ba942c8415c24536a12bc7e30300183ed20f302dc5ee6243`, configurations v2).

## 5. Liste d'arrêt

Avant la course : un contrôle d'avant course en échec. Pendant : modèle servi différent ; trois échecs consécutifs d'un rôle ;
débordement de la garde de Kimi proposeur (plus de 3 fiches `concret` sur 6) ; dépassement de réserve ; garde cumulée ; garde
d'étape ; plafond propre d'un relais (HTTP 402 ou 429 : nombre d'appels épuisé compris) ; plafond de l'étape ; **nœud C13 (A14 :
plus de 25 % d'appels inexploitables pour un rôle ; pour un proposeur, un seul échec suffit)** ; signal ; toute autre exception.
**Tout arrêt ou nœud après la proposition ne rend ni fiches ni classement** ; restent lisibles journaux, manifestes, consommations,
coffre, journal de l'aiguillage ; les réponses brutes ne survivent pas. Codes du lanceur : 124 délai de 12 h ; 6 clé trouvée (pas de
copie au canal) ; 7 trace refusée ou sceau en échec.

## 6. Lecture prévue

Sortie scellée avant lecture, copiée à l'octet dès son scellement avec sa liste, sonnette ; rien lu par session-depot. Rapport au
protocole « mentors du soir » (lecteur neuf, moissonneurs, classeur ; envoi brut à Lazar dès la copie), **par extension** (CLI-03,
écart n° 7) : le protocole ne prend en entrée que les cellules du tour du collisionneur et les fiches du matin, et la spécification
de la course ne nomme aucun protocole. Proposé : les fiches de la course entrent à l'étape A avec celles du tour Ibrahim, comme des
cellules d'espèce de plus (provenance « course » gardée sous la clé à part), et le dédoublonnage par structure de l'étape A joue
entre les fiches de la course, les cellules du tour et les fiches du matin ; à confirmer par conv-audit. `fiches.json` ne contient
que les fiches munies d'un passeport et les fusions complètes ; les fiches `a_corriger`, `concret` ou exclues sont comptées, non
gardées ; le rapport donne les nombres par classe et par espèce. Lazar écrit seul sa réponse.

## 7. Gardes éprouvées et non éprouvées

Éprouvées hors réseau : 44 essais (`ibrahim/test_course_ibrahim_v2.py`, gelé ; les 36 de la v1 sur les configurations v2, plus
CLI-01 et CLI-02) ; contre-épreuve par dix mutations, toutes détectées, dont M10 (marge d'appels v1 rendue au relais Claude)
(`ibrahim/resultat-mutations-ibrahim-v2.txt`, `96c6db46797465e50c531dcf4c0f1a4cfe4222cd6cca7bda26805792f8dff532`) ; répétition v2
par le vrai lanceur shell v2 derrière de faux amonts qui rendent **8 fiches par proposeur** (plan : 6) : cinq essais conformes
(`ibrahim/repetition/resultat-repetition-ibrahim-v2.txt`, `94f5a956035e78305516a76fac91604b0df2a8d3f05709c86d185c02a3e63139`) ; à
cinq espèces, la course va au bout (code 0, 40 fiches, 8 fusions) avec Claude 188 appels sur 301 permis (reste 113), Astra 130 sur
205 (reste 75), Kimi et Argon 2 sur 9. Historique : le premier passage de la répétition v1 (faux amont à 8 fiches, marge « plan
plus 5 ») s'était arrêté, nombre d'appels épuisé ; la v1 avait été rejouée à 6 fiches seulement (constat CLI-01), d'où la v2.
Non éprouvés : comportement de l'aiguilleur et de la garde sur des fiches de cette question ; tenue réelle de « six fiches » par
chaque espèce ; solde de Moonshot ; ligne de GO réelle.

### Pièces gelées

| pièce (chemin depuis la racine du dépôt) | sha256 | rôle |
|---|---|---|
| `.claude/hooks/garde_calcul.py` | `84512d4a1bef0403668000942cf5f5d383aab280bf5a58f6aec328e77f807d59` | garde du dépôt |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/collisionneur_v8.py` | `22e5ed8a64075f2f985755d9bff2c2336d8edc5f73cbc3b0511405fd8f43d264` | relais (appel de l'interface) |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/commande_astra_a1bis_v1.py` | `6e9e48e0fc0a0528183a26d019d69d51f9bb9b8c1791c6ae487b59a4466a1815` | commande |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/commande_claude_a1bis_v1.py` | `7da79a5c34449dd7629aa3d1721c76058a34b56b43f2bd46c9dbfc94e20ef2c5` | commande |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/commande_pole_v56_commun_v1.py` | `1f56e466f5e80f82a25ccccbb5784fa0fa6dc34046dc99d887ec87f713c7eaed` | commande |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` | `d54ed2bce54f5c89e9f078d1a03b5d8159894d6565ae560c3601c1e63ca76239` | relais |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/EMPREINTES-orchestrateur-course-ibrahim-q1-v1.txt` | `de9b57688cef1cc968f5e5fa94ed4368d0d8eca83f2b34c57a8ba841a535e3cd` | empreintes de la copie |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/VERIFICATION-COPIE-orchestrateur-v56-v1.txt` | `a3efa6f8b041edbbbe020e45b44219b77bc14184c8daa660527884fe6739874a` | vérification de la copie |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/argon/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | relais (appel de l'interface) |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/calcul_devis_course_ibrahim_v1.py` | `eeedd86aba9bd2f876ab0b20caf4da93c5f94023742a6d23c9a49d207b25f337` | devis |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/commande_claude_ibrahim_v1.py` | `abca5e76b225233ed4ca67e64567b7eed58614d7836ec4c57cc157ea9fad35a5` | commande |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/configuration-course-ibrahim-q1-v2-avec-kimi.json` | `5b4fe58709b796ad7f29d8b7a2a57c93a70c6ed7dd74ce81b1f2370596f17ed4` | configuration |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/configuration-course-ibrahim-q1-v2-cinq-especes.json` | `41feac66c13ab9a541489fc5cac9f8dd39d5bbb888e18344537a0904e7a02446` | configuration |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/configuration-course-ibrahim-q1-v2-sans-kimi.json` | `a8527098cb4941653d3e41f8dfd37dbd29197c0739bc5995da4afdd910a606d7` | configuration |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/construire_configurations_ibrahim_v2.py` | `45357419e745e58cad34783dee12eeeb26eadc877a9942d76aabea43be976f15` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/construire_consigne_proposeur_ibrahim_v1.py` | `a48f03cfd454bbeb2cf044a991253e4e9edffa5e8f5138cc1b38e9ea63e17679` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/course-a-blanc-ibrahim-v1.txt` | `fefd3b4750f7b931d72d3d5044b35ba957f053741014b6c20be3ec3c001cd297` | génération |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/course-a-blanc-ibrahim-v2.txt` | `53b7e0738a00ea24ba942c8415c24536a12bc7e30300183ed20f302dc5ee6243` | génération |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/course_a_blanc_ibrahim_v2.py` | `da475c4726b876cbafc4e8b11ba298c60bde82ac609db7eddf8fbba011956853` | génération |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/course_ibrahim_v1.py` | `946479d327823123556291d2fc16f415b8bd8ab4a3f843718a1e5e291411adac` | génération |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/devis-course-ibrahim-v1.json` | `d63ff942cf3473308d76066f2dde6fab1815e2d09770614f2291ddc45c770068` | devis |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/devis-course-ibrahim-v1.txt` | `f5f14608f7ee69c4ab2ac73d891488d1783a00427e4143d01d745a0238bb770d` | devis |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/lancer-course-ibrahim-v1.sh` | `95e9efb37c2daa29fa3cd08d9ad95ab070f4ab11d23efb9a94c09254250b41aa` | lanceur |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/lancer-course-ibrahim-v2.sh` | `3cba586c9f38f04651670a4625a209d63469de4ec2e7e2531e330029eb7738e9` | lanceur |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/lancer_course_ibrahim_v1.py` | `d629ce04c78051dcd8e8a8bfe98e000d7956510e76f37b97978d9241275c4112` | lanceur |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/mutations_ibrahim_v2.py` | `ca805957859513ab081103e3d2b9d52a048a14c7f934fba7c3c3c3dd52119c6e` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/concepts-ibrahim-v1.json` | `8fbe16a27f22262ffac71fee1a60b478d05e05abb2323ae7f4a78106ea808c23` | liste fermée |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/consigne-aiguilleur-ibrahim-v1.md` | `571fcefcba62d4d145b7858489f3ab811dccd4315b34220291da119d63384644` | consigne |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/consigne-juge-ibrahim-v1.md` | `acae672c8d67ba97f9b7863b833185f09e20fb0e4f14793dc5c254d528fff0a6` | consigne |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/consigne-lecteur-ibrahim-v1.md` | `29f436802e234bd53c4fc8e3597a4be62d044264029e5e37549144fb97c7a2ae` | consigne |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/consigne-metteur-ibrahim-v1.md` | `a305c3f69f7b4cadc03ad942d30a1395bb471387fab47c0dce6ff49b39853c49` | consigne |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/consigne-proposeur-ibrahim-v1.md` | `46149f554531863830a344115db8bcd850b8f8405f36c61768102051aa6d2413` | consigne |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/conv-audit/conv-audit_2026-11-03_n417.md` | `fecc2d0bbe7f547186b1e870dd64c9e4f7e42f93c678c6c2bc7578701bdaf6b4` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/conv-audit/piece-ibrahim-v1.md` | `4e3851e3816fc3afaa573693f8f3d0aa2b9fc6c0e726ae54bab8cd4a248d6149` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/conv-audit/piece-nos-resultats-v1.md` | `d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/conv-audit/piece-sycophancie-publique-v1.md` | `9e424a025280908baf5e2eec65f285a746f92ce14991cdc5d7d80cb5978716b8` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/conv-audit/protocole-rapport-mentors-soir-v1.md` | `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/conv-audit/question-collisionneur-ibrahim-v1.md` | `5e905798a512db9fb9c607be0fbe74972d7df618cf8b9026c23eb0bc8ed6d9c0` | question servie |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/conv-audit/specification-course-ibrahim-v1.md` | `0874d561fc43218a5366832072719ce67de8d6f3bd4c1d9ebe4fbeb20a47baff` | spécification de conv-audit |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/conv-audit/specification-kirchner-q2-v1.md` | `934f5dcb0bd442f0c17b2c1aada88041795ab7336e3b03d5fe1bd8bb7c068622` | spécification de conv-audit |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/pieces/source-gu-krenn-ibrahim-v2.json` | `2ffdc7f9acdce35335160867f71651faa6b72d77377f6cd6188d911664395bc4` | source du substitut Gu-Krenn |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/repetition/faux_mandataire_tls_ibrahim_v2.py` | `025addcc6645cbeed31f99b0e953827dcafd5119a84c97bad12171cc23db15a9` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/repetition/repetition_complete_ibrahim_v1.sh` | `48edcb7587e59ebd73019eec4c1795d009cf9d7f17375e4131d73d11bef86adc` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/repetition/repetition_complete_ibrahim_v2.sh` | `a967e713505a2c28f4f3b91c2ca8eb34c7d9c22352a91d5ca1c33d94fad2fc83` | pièce |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/test_course_ibrahim_v1.py` | `26fc422290c1b3aaa3a9c8bad064992f15f8642a2e9d84e392b5a32b6db8cbf3` | génération |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/test_course_ibrahim_v2.py` | `52676c577be6fcc4242c46caf7b6dd378d256f7fcced0e555ca1dcd302d5f175` | génération |
| `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/trace_agregee_course_ibrahim_v1.py` | `62f7106b6d9b1a8d80a9e30ffeefd790a61c72d776415681dc88cb414a1476af` | trace agrégée |
| `donnees/course-ibrahim-q1-v1/orchestrateur/nuit/chercher_cles_v1.py` | `5d6f82fc5cc95f9998877852c08835b83df1ba572597303f447cb983cf97cf61` | recherche des clés |
| `donnees/course-ibrahim-q1-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` | commande |
| `donnees/course-ibrahim-q1-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande |
| `donnees/course-ibrahim-q1-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `donnees/course-ibrahim-q1-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération |
| `donnees/course-ibrahim-q1-v1/orchestrateur/pole/course2_nuit_v2.py` | `5d15660eca9f23b9480cb6bf7a05379859255294d377652231d944170fe69032` | génération |
| `donnees/course-ibrahim-q1-v1/orchestrateur/pole/course2_v56.py` | `14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1` | génération |

## 8. Écarts à la spécification de conv-audit (à trancher par conv-audit)

1. Pièces servies : trois (Ibrahim, **sycophancie publique**, nos résultats), sur le n° 417 (« pièces ci-dessus »), alors que la
   spécification § 1 en nomme deux.
2. Question servie : deux sections (la question, les règles d'intégrité) ; la spécification ne nomme que « La question » pour la
   course ; les règles d'intégrité sont gardées parce qu'elles sont des règles de la course (« mêmes règles »). Conséquence
   déclarée (CLI-04) : la section est servie à l'octet et porte une règle propre au collisionneur, « Au plus 1 200 mots par
   cellule de conception » ; la course n'a pas de cellule, et un proposeur peut la lire comme une borne pour ses six fiches à la
   fois, et les raccourcir. La consigne n'est pas retouchée (fidélité à l'octet).
3. Juge : critères tirés de la question et de deux des trois critères du protocole (l'originalité vérifiée demande une moisson).
4. Aucun témoin planté ; bras méta hors course ; source du substitut écrite à partir des seuls textes servis.
5. Garde lexicale « comme Heimersheim » sauf « fusion » et « argon », retirés (nommés ou attrapés dans les pièces servies).
6. Nombre d'appels permis des relais porté à 2 × le plan plus 5 (le kit Kirchner avait plan plus 5 ; la v1 de ce kit 4/3 du plan
   plus 5) ; plafonds en dollars inchangés (§ 3.8).
7. Lecture de la course au protocole des « mentors du soir », par extension : le protocole ne nomme pas la course parmi ses
   entrées ; jonction proposée à l'étape A (§ 6) ; à confirmer par conv-audit (CLI-03).

## 9. Traitement de la contre-lecture du brouillon 1

| Constat | Gravité | Traitement |
|---|---|---|
| CLI-01 marge d'appels (au plus 13 fiches de trop ; cas à 8 fiches non rejoué) | majeur | corrigé : `max_appels` = 2 × plan + 5 dans les trois configurations v2 (Claude 301, Astra 205 à cinq espèces ; 253 et 169 avec Kimi ; 205 et 133 sans Kimi ; Kimi et Argon 9), plafonds en dollars inchangés ; borne restante écrite (§ 3.8) ; répétition v2 rejouée derrière un faux amont à 8 fiches par proposeur, allée au bout (§ 7) ; mutation M10 |
| CLI-02 source Gu-Krenn (rapprochement du rédacteur ; lien R8 omis ; deux œuvres R6) | majeur | corrigé : source v2 (« optimisation par préférences » pour le papier sur la chaleur ; R8 porte « loi d'attraction » ; œuvres R6 fondues) ; choix déclarés (§ 3.4) ; essai `test_cli02_source_gu_krenn_v2` |
| CLI-03 protocole « mentors du soir » sans la course parmi ses entrées | mineur | déclaré : écart n° 7, jonction proposée à l'étape A (§ 6, § 8.7) |
| CLI-04 règle « 1 200 mots par cellule » servie aux proposeurs | mineur | déclaré (§ 8.2), consigne non retouchée (fidélité à l'octet) |
| CLI-05 juge : K5 et K1 qu'il ne peut pas lire seul | mineur | déclaré (§ 3.2) |
| CLI-06 docstring du faux mandataire (« 8 fiches ») | mineur | corrigé dans le faux mandataire v2, qui rend `--fiches-par-proposeur` fiches (8 par défaut) |
