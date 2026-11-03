# Fiche de lancement — course d'idéation sur la question 2 des mentors Colognese et Ward — brouillon 1

Rédigée par un sous-agent de session-depot le 3 novembre 2026, 14:16 UTC (`date -u`). **Brouillon** : session-depot le fait
contre-lire par un lecteur neuf (R2), puis en écrit la version scellée sous un nom neuf (R12), qui cite l'empreinte du rapport à
la ligne ci-dessous. Le lanceur exige ce texte scellé, sans marqueur de remplissage, citant l'empreinte de sa contre-lecture, et
dont la table « Pièces gelées » couvre ce qu'il nomme. Aucune dépense, aucun appel réel pour l'écrire. Kit : celui de la course
Ibrahim v2 (`outils/course-ibrahim-q1-v1`, `965eb21b` : marge d'appels 2 × plan + 5, aiguilleur au niveau Kirchner v2, garde
lexicale v2, 6 fiches par proposeur), renommé et adapté (branche `outils/course-colognese-ward-q2-v1`).

Contre-lecture : <<EMPREINTE_RAPPORT>>

## 1. Nature de la course, sources, mots de Lazar

- **Course NON décisive** : matière à réflexion pour Lazar ; aucune porte, aucune revendication, aucun chiffre opposable (R7).
- Spécification : `brouillons/ideation-mentors-soir-v1/specification-course-colognese-ward-v1.md` (branche `canal/conv-audit-n04`,
  `711fcf528ec09a2cc031457b8c64093e867c28f95e8344828408f5abb2e16922`, compagnon vérifié) ; règles du juge : n° 419 de conv-audit ;
  protocole des rapports « mentors du soir ». Copies à l'octet dans `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/` :
  question `question-collisionneur-colognese-ward-v1.md` (`06d837952cfe066a1414710fadda80f2624ac944c1d5c428b9073bb44686d6af`) ;
  pièce `piece-colognese-ward-v1.md` (`7533e4b58f03a5b8928ca2c411d8c29ee48f86e15e744afaf4b07e8a9b8f91b2`) ;
  pièce `piece-nos-resultats-v1.md` (`d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c`) ;
  protocole `protocole-rapport-mentors-soir-v1.md` (`fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`) ;
  n° 419 `conv-audit_2026-11-03_n419.md` (`75aedf2ea88361e7b76cd990791f445466c17ac4c87943f96da9efcf9266834b`).
- Servis aux proposeurs : **deux sections** de la question (« La question, telle que les mentors la posent » et « Règles
  d'intégrité ») ; puis les pièces, dans cet ordre : Colognese et Ward, nos résultats. Rien de la candidature n'est servi.
- Mot de Lazar, **direct**, à session-depot, à la lettre : « go courses Scheurer, Colognese-Ward Q2, Jang-Feng, dans cet ordre ;
  pas de plafond » (reçu entre 13:39:07 et 13:49:07 UTC, `registres/decisions.md`, R-1149). Mot chez conv-audit, rapporté par la
  spécification (14:38, heure de Paris) : « lance des courses pour tout le monde par ordre de préférence du mentor et si on n'a pas
  le temps de voir la course avant de rédiger tant pis ». Ligne de GO : `GO-2026-11-03-NN` (numéro attribué à l'inscription par
  session-depot, cité au lancement). Une sortie copiée après 16:00 UTC n'entre pas dans le choix de piste du soir (spécification).
- Instrument : orchestrateur v56 (copie à l'octet vérifiée, 218 fichiers), génération de la mini-course, au-dessus
  `course_colognese_v1.py`. Une génération, une passe, **6 fiches par proposeur** (spécification § 2).

## 2. Variantes (une seule est lancée)

| Variante | Proposeurs | Quand |
|---|---|---|
| `configuration-course-colognese-ward-q2-v1-cinq-especes.json` | Fable 5.1, Opus 5.5, Argon, Kimi, Astra | **lancement**, si Argon est libre au départ (aucun tour ni autre course ne l'utilise ; session-depot le vérifie par l'état des filles et du relais 8805 ; le refus de port pris ne voit que l'hôte local) |
| `configuration-course-colognese-ward-q2-v1-avec-kimi.json` | Fable 5.1, Opus 5.5, Kimi, Astra | quatre espèces, **sans Argon** (absence déclarée), si Argon est pris |
| `configuration-course-colognese-ward-q2-v1-sans-kimi.json` | Fable 5.1, Opus 5.5, Astra | repli si le contrôle de Kimi échoue ; seule variante sans la garde de débordement de Kimi |

Rôles identiques à Ibrahim : aiguilleur Opus 5.5 ; juges Opus 5.5 et Astra (unanimité) ; lecteurs Opus 5.5 et Astra ; metteur
Fable 5.1 ; Claude par un seul relais 8806, `--effort high --reflexion adaptative`, aucune bascule. Lanceur :
`colognese/lancer-course-colognese-v1.sh` (n'accepte que ces trois configurations). Un refus d'un modèle pendant la course ne se
rejoue pas (R-486) ; mais pour un proposeur, un seul échec déclenche C13 et l'arrêt sans fiche (§ 5) : la fiche refusée ne peut
pas être « déclarée absente » en laissant courir les autres (limite du noyau v56, déclarée).

## 3. Déclarations

1. **Aucun témoin planté**.
2. **Juge réécrit pour cette question** (n° 419 de conv-audit, dans cet ordre, et la question) : K1 précis et faisable en jours ;
   K2 résultat attendu chiffré et signé, et la chose qui le rendrait trompeur avec son contrôle ; K3 prolonge un travail des
   mentors ; K4, tiré de la question : ancrée dans le billet (le résultat visé et sa section, ce que la fiche changerait pour la
   surveillance ou le contrôle, ce qu'elle suppose marqué « supposé »). **L'originalité n'est pas un item** (n° 419). Le juge voit
   la section « La question » telle quelle, pas les pièces : il ne peut pas vérifier les identifiants ni ce que les travaux des
   mentors ont déjà fait (K3) ; les sorties des deux juges sont rapportées à part. Aiguilleur au niveau Kirchner v2 (« en cas de
   doute, concret » gardé ; planter pour éprouver une mesure ou un juge est `niveau_methode` ; seule la recette opérationnelle
   contre une évaluation ou un moniteur réels est `concret`). Lecteur et metteur : même mécanique.
3. **Champs** (format du kit) : `titre`, `hypothese` (le changement ou le résultat jugé le plus intéressant, et pourquoi),
   `axe`, `epreuve` (ce qui change, sur quel résultat du billet, avec sa section, et le protocole), `controle` (ce qui rendrait le
   résultat trompeur et son contrôle ; ce que le billet ne dit pas, marqué « supposé »), `prediction`, `test_de_mort` (l'expérience
   qui tue l'idée ; ce qui ferait échouer l'analyse), `cout`. **Axes, tirés de la question** : `changement_de_dispositif`,
   `resultat_le_plus_interessant`, `ce_que_le_billet_ne_dit_pas`. La question demande trois à cinq changements et un résultat :
   la course demande six fiches par proposeur ; déclaré.
4. **Bras joués** : `gu_krenn` (substitut) et `basique` (exposant 8,5, décalage 0,05), quatre paires par bras. Liste fermée : 64
   concepts tirés des seuls textes servis (`pieces/concepts-colognese-v1.json`). Source du substitut
   (`pieces/source-gu-krenn-colognese-v1.json`, `911827cfdcf79b96…`) : 15 œuvres, une par source citée (7
   de la pièce Colognese et Ward : 2512.00218, 2601.21112, 2601.23086, 2511.18397, 2503.11926, le billet, ses commentaires ; 8
   de « nos résultats », les mêmes que pour Scheurer) ; aucun rapprochement du rédacteur. Choix déclarés : le billet (§ 3.1 à
   § 3.4, corrections comprises) est une œuvre, ses commentaires publics (§ 3.5) une autre ; « triche silencieuse » est au seul
   billet (la graine 42 de 2601.23086 porte « exploitation jamais mentionnée sans pénalité ») ; « obscurcissement du raisonnement »
   est à 2601.23086 et à 2503.11926 ; « apprentissage par renforcement » au billet, à 2601.23086 et à 2511.18397. Codage non
   contre-lu. **Bras méta hors course.**
5. **Garde lexicale** (mode « prefixe », action « fiche exclue ») : celle d'Ibrahim **sans « openai »** : `exploratoire`,
   `bras méta`, `gu et krenn`, `gu krenn`, `bisociation`, `kimi`, `moonshot`, `gemini`, `fable`, `astra`, `gpt 6`, `gpt6`, `gpt-6`,
   `chatgpt`. « openai » est retiré parce que la pièce l'emploie (§ 2 : « (OpenAI) ») : la garde exclurait toute fiche qui cite ce
   travail ; prix : une fiche qui se dirait écrite par « OpenAI » passerait. « argon » et « fusion » restent retirés (la pièce
   « nos résultats » nomme Argon) ; « claude », « opus », « anthropic », « sonnet », « gpt », « argon », « fusion » et « openai »
   sont refusés dans la liste (la pièce cite Claude Sonnet 4.5, Opus 5, Sonnet 5, GPT-4o mini, GPT-4.1-mini). Vérifié avant tout
   appel, et par un essai : aucune étiquette dans la question, les deux pièces, les consignes servies, la liste ni le vocabulaire
   du substitut.
6. **Consigne du proposeur** (`pieces/consigne-proposeur-colognese-v1.md`, `ca31eddca070fa0ba234b9adb1215c553cdd97806d625b72247e22bab85cf391`) :
   deux sections de la question, puis les deux pièces entières, dans cet ordre, à l'octet (vérifié avant tout appel) ; la section
   « Ce qu'on attend de chaque espèce » est remplacée par le livrable du kit, qui en reprend les demandes ; titre, provenance et
   « Lecture prévue » non servis. Les « Règles d'intégrité » servies à l'octet portent « Au plus 1 200 mots par cellule de
   conception » : la course n'a pas de cellule ; un proposeur peut la lire comme une borne pour ses six fiches (déclaré).
7. **Plafond technique S17 = 198 USD** (portée « course », arrêt d'étape 178,2) : garde contre une boucle, sur le mot direct « pas
   de plafond » ; entier supérieur à 1,2 × 164,64 = 197,57 (calcul). La ligne de GO porte **un seul montant : « 198 USD »**.
   Relais (cinq espèces) : Kimi 2 USD (≤ 5), Argon 3 USD (≤ 10), Astra 102,0, Claude 91,0.
8. **Marge d'appels** (comme Ibrahim v2) : `max_appels` de chaque relais = 2 × le plan + 5 ; plafonds en dollars inchangés. **Borne**
   (fiches en trop tolérées, toutes espèces, calcul) : cinq espèces 35 (Claude 301 pour 148 au plan, Astra 205 pour 100) ; avec Kimi
   29 ; sans Kimi 23. Au-delà : arrêt à l'étape des étiquettes, sans fiche.

## 4. Devis (`colognese/devis-course-colognese-v1.txt`, `4d1be7689eea96a704ae5c6206f3e6ec069bef297d83046939353d6314363a54`)

| Variante | Appels (course + contrôles) | Attendu | Pire cas | Part Kimi (att. / pire) | Part Argon (att. / pire) |
|---|---|---|---|---|---|
| cinq espèces (lancement si Argon libre) | 247 + 5 | 19,03 USD | 164,64 USD | 0,22 / 0,79 | 0,21 / 1,72 |
| avec Kimi (quatre, sans Argon) | 204 + 4 | 16,17 USD | 139,47 USD | 0,22 / 0,79 | — |
| sans Kimi | 161 + 3 | 13,30 USD | 115,24 USD | — | — |

Hypothèses : celles du devis Ibrahim (3,48 caractères par jeton, médiane mesurée au second tour ; sorties attendues supposées,
proposeur 9 000 jetons pour 6 fiches ; pire cas = sortie maximale de chaque appel, toutes fiches admises). Repères réglés
(spécification) : Heimersheim 10,03 USD, seconde course Kirchner 10,84 USD. Plafonds de session : proposeur 3,5 > 3,2722 ;
aiguilleur 0,4 > 0,3386 ; juge 0,9 > 0,8489 ; lecteur 0,9 > 0,85 ; fusion 3,5 > 3,2864. Course à blanc : nombre d'appels identique
au plan dans les trois variantes (`colognese/course-a-blanc-colognese-v1.txt`, `9b7c47c605e16ccf254e2942bb42bb47c8aa495c4624b43df3c87af93d8cb436`).

## 5. Liste d'arrêt

Avant la course : un contrôle d'avant course en échec. Pendant : modèle servi différent ; trois échecs consécutifs d'un rôle
(un refus compte comme un échec) ; débordement de la garde de Kimi proposeur (plus de 3 fiches `concret` sur 6) ; dépassement de
réserve ; garde cumulée ; garde d'étape ; plafond propre d'un relais (HTTP 402 ou 429 : nombre d'appels épuisé compris) ;
plafond de l'étape ; **nœud C13 (A14 : plus de 25 % d'appels inexploitables pour un rôle ; pour un proposeur, un seul échec
suffit)** ; signal ; toute autre exception. **Tout arrêt ou nœud après la proposition ne rend ni fiches ni classement** ;
restent lisibles journaux, manifestes, consommations, coffre, journal de l'aiguillage ; les réponses brutes ne survivent pas.
Codes du lanceur : 124 délai de 12 h ; 6 clé trouvée (pas de copie au canal) ; 7 trace refusée ou sceau en échec.

## 6. Lecture prévue

Sortie scellée avant lecture, copiée à l'octet dès son scellement avec sa liste, sonnette ; rien lu par session-depot
(spécification § 3). Rapport au protocole « mentors du soir » (lecteur neuf, moissonneurs, classeur ; envoi brut à Lazar dès la
copie), **par extension** : le protocole ne prend en entrée que les cellules du tour et les fiches du matin. Proposé, comme pour
Ibrahim : les fiches de la course entrent à l'étape A avec les cellules du tour Colognese et Ward Q2, comme des cellules d'espèce
de plus (provenance « course » gardée sous la clé à part), et le dédoublonnage par structure joue entre elles ; à confirmer par
conv-audit. `fiches.json` ne contient que les fiches munies d'un passeport et les fusions complètes. Lazar écrit seul sa réponse.

## 7. Gardes éprouvées et non éprouvées

Éprouvées hors réseau : 47 essais (`colognese/test_course_colognese_v1.py`, gelé) ; contre-épreuve par dix mutations, toutes
détectées (`colognese/resultat-mutations-colognese-v1.txt`, `9d153e0093459c644dbcf25a4a4fbf1ff76285f8753263f311340623755437c8`) ; répétition par le
vrai lanceur derrière de faux amonts qui rendent **8 fiches par proposeur** (plan : 6) : cinq essais conformes
(`colognese/repetition/resultat-repetition-colognese-v1.txt`, `f357b8bcbe43ce11a3445987bbc78b7740a82db89bae880c624fd760d745c70c`) ; à
cinq espèces, la course va au bout (code 0, 40 fiches, 8 fusions ; Claude 188 appels sur 301, Astra 130 sur 205, Kimi et Argon
2 sur 9) ; `kill -TERM` (quatre espèces) : code 130, relais arrêtés.
Non éprouvés : comportement de l'aiguilleur et de la garde sur des fiches de cette question ; tenue réelle de « six fiches » ;
solde de Moonshot ; ligne de GO réelle.

## 8. Écarts à la spécification de conv-audit (à trancher par conv-audit)

1. Question servie : deux sections (la question, les règles d'intégrité) ; la spécification ne nomme que « La question » (même
   choix déclaré pour Ibrahim : les règles d'intégrité sont des règles de la course) ; règle « 1 200 mots par cellule » servie
   telle quelle (§ 3.6).
2. Juge : n° 419 (trois items, sans originalité) plus un item tiré de la question (K4).
3. Six fiches par proposeur pour « trois à cinq changements » demandés par la question.
4. Garde lexicale sans « openai » (employé par la pièce servie), ni « argon » ni « fusion ».
5. Un refus de proposeur arrête la course (C13) au lieu de laisser sa fiche « déclarée absente » (§ 2).
6. Lecture au protocole des « mentors du soir », par extension (§ 6).
7. Aucun témoin planté ; bras méta hors course ; source du substitut écrite à partir des seuls textes servis.

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
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/EMPREINTES-orchestrateur-course-colognese-ward-q2-v1.txt` | `de9b57688cef1cc968f5e5fa94ed4368d0d8eca83f2b34c57a8ba841a535e3cd` | empreintes de la copie |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/VERIFICATION-COPIE-orchestrateur-v56-v1.txt` | `0454d253acdc8a89b92f1b898e1caa03dfbf930b97d499f37c0cbf1cb0238c79` | vérification de la copie |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/argon/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | relais (appel de l'interface) |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/calcul_devis_course_colognese_v1.py` | `03a2f19ee7eed8b96a66dd207519af4f22ac831c7368a586d372052786e45cd4` | devis |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/commande_claude_colognese_v1.py` | `a20b91f0fa88c03a2488649a9ba7469c08e2e9986d919d5dc493c98dc5b01bca` | commande |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/configuration-course-colognese-ward-q2-v1-avec-kimi.json` | `608768c6bec42747d223b59124630ce07a001462f5f85d8018efad713aef34c2` | configuration |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/configuration-course-colognese-ward-q2-v1-cinq-especes.json` | `63e48ad943b60d6381e40b6eec4fcbcf650e52382f86c6f58f2a7997a06e5e22` | configuration |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/configuration-course-colognese-ward-q2-v1-sans-kimi.json` | `a38c6759e9899805405659b0410b77b87101fa7305853e91a1da893517d38518` | configuration |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/construire_consigne_proposeur_colognese_v1.py` | `49aeb992058902a500b08d55b0b682d144ccb6686ed5bafdbd7dfdda63ab5787` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/course-a-blanc-colognese-v1.txt` | `9b7c47c605e16ccf254e2942bb42bb47c8aa495c4624b43df3c87af93d8cb436` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/course_a_blanc_colognese_v1.py` | `6229a50149923f33eb3e394d64610b1869a8dfc60ec443e882cbefe4caf0e8d1` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/course_colognese_v1.py` | `d7ca1db13943fa44833b1235710c7e18cc2ef22ef210e173824ec6fbc9868276` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/devis-course-colognese-v1.json` | `882bafa3b8889ee4417a0f928a4fddb09e7864ea911a99455817b8c7153a422e` | devis |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/devis-course-colognese-v1.txt` | `4d1be7689eea96a704ae5c6206f3e6ec069bef297d83046939353d6314363a54` | devis |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/lancer-course-colognese-v1.sh` | `5e28568686555107b5d1a3ee74eda811da1c3a03e86857f4ec0c232645582449` | lanceur |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/lancer_course_colognese_v1.py` | `0657794db7f1e564ca0e66c2de2b811844c181077aabf91e532de0c3c51fb39d` | lanceur |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/mutations_colognese_v1.py` | `e13d7539542ddee68a10e7f682067e29299ed532ad76de220bc6e54aaa19f695` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/concepts-colognese-v1.json` | `0279ff3df2271e8127926f4ebdb7ab854ba9fdf80324f1fbcfbec3730789cbd9` | liste fermée |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/consigne-aiguilleur-colognese-v1.md` | `5e2ed12b05b0775917ee777ad2329ce48aee21ef092ec29bf0c5ba071c6f25cf` | consigne |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/consigne-juge-colognese-v1.md` | `d518aad3d86f91174531d96ad9bdde0be362c65a94cfc5ff59cc370825eb99df` | consigne |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/consigne-lecteur-colognese-v1.md` | `6c38ce813e9fa78236375e5b104de394508255f50a31dd94acb226b1db969eaa` | consigne |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/consigne-metteur-colognese-v1.md` | `714ac8dd31b1bf9d2f547ed329eeeb59af2e4084c106fa7a4a901df7d0d1290d` | consigne |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/consigne-proposeur-colognese-v1.md` | `ca31eddca070fa0ba234b9adb1215c553cdd97806d625b72247e22bab85cf391` | consigne |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/conv-audit_2026-11-03_n419.md` | `75aedf2ea88361e7b76cd990791f445466c17ac4c87943f96da9efcf9266834b` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/piece-colognese-ward-v1.md` | `7533e4b58f03a5b8928ca2c411d8c29ee48f86e15e744afaf4b07e8a9b8f91b2` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/piece-nos-resultats-v1.md` | `d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/protocole-rapport-mentors-soir-v1.md` | `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/question-collisionneur-colognese-ward-v1.md` | `06d837952cfe066a1414710fadda80f2624ac944c1d5c428b9073bb44686d6af` | question servie |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/specification-course-colognese-ward-v1.md` | `711fcf528ec09a2cc031457b8c64093e867c28f95e8344828408f5abb2e16922` | spécification de conv-audit |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/source-gu-krenn-colognese-v1.json` | `911827cfdcf79b967071c01b3dfd4ea4f4c45a39be130cd8c42d0055a44e1500` | source du substitut Gu-Krenn |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/repetition/autorite_factice_colognese_v1.sh` | `7a4a6dd49035d43193dbb1d7855a4f2e67452b78674d8f90024651f3dc71c8a0` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/repetition/faux_mandataire_tls_colognese_v1.py` | `e848382595597ddeae26ff276750ccf76abdf14af8ad3b8905523f20ecb6ab99` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/repetition/repetition_complete_colognese_v1.sh` | `ea8d434d8e48701806fba42dbb31a1937e26f9c91acb0ee58b425f83b1b5c7da` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/test_course_colognese_v1.py` | `f44882b26d56fb61d135b1be0a8ad4b5164c1900e5e4873ebfadc8e33b877295` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/trace_agregee_course_colognese_v1.py` | `a7a92eb68bb608a58e267ebcc4db4fa6d327411a7e16e90033982b49370f8602` | trace agrégée |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/nuit/chercher_cles_v1.py` | `5d6f82fc5cc95f9998877852c08835b83df1ba572597303f447cb983cf97cf61` | recherche des clés |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` | commande |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/pole/course2_nuit_v2.py` | `5d15660eca9f23b9480cb6bf7a05379859255294d377652231d944170fe69032` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/pole/course2_v56.py` | `14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1` | génération |
