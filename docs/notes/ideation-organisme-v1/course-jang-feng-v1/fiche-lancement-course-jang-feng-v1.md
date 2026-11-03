# Fiche de lancement — course d'idéation sur la question des mentors Feng et Jang — v1 (scellée)

Version scellée écrite par session-depot le 3 novembre 2026 (heure lue par `date -u` à 14:39:07) : brouillon 2 (`87df2d8fd9a7ad45b7ee6567ae84a964578f5229cbbf832a642156397d80867f`) corrigé des quatre constats de sa contre-lecture (CLJ2-01 à CLJ2-04, traités au § 10) ; aucun code, aucune configuration, aucune pièce changés. Rédigée par un sous-agent de session-depot le 3 novembre 2026, 14:34 UTC (`date -u`). Brouillon 2 = brouillon 1 (gardé, R12)
corrigé après sa contre-lecture (`docs/notes/ideation-organisme-v1/course-jang-feng-v1/contre-lecture-fiche-lancement-course-jang-feng-v1.md`,
`a31c8250…`, « à corriger », aucun bloquant) et les décisions de session-depot : deux variantes sans Opus (CLJ-01), règle de
lancement et de repli déclarée d'avance, une ligne de GO par S17, kit v2 (module, lanceurs, devis, table, essais, répétition) ;
traitement constat par constat en § 9. **Brouillon** : session-depot le fait
contre-lire par un lecteur neuf (R2), puis en écrit la version scellée sous un nom neuf (R12), qui cite l'empreinte du rapport à
la ligne ci-dessous. Le lanceur exige ce texte scellé, sans marqueur de remplissage, citant l'empreinte de sa contre-lecture, et
dont la table « Pièces gelées » couvre ce qu'il nomme. Aucune dépense, aucun appel réel pour l'écrire. Kit : celui de la course
Ibrahim v2 (`outils/course-ibrahim-q1-v1`, `965eb21b` : marge d'appels 2 × plan + 5, aiguilleur au niveau Kirchner v2, garde
lexicale v2, 6 fiches par proposeur), renommé et adapté (branche `outils/course-jang-feng-v1`).

Contre-lecture : `docs/notes/ideation-organisme-v1/course-jang-feng-v1/contre-lecture-fiche-lancement-course-jang-feng-v1-brouillon2.md`, `08b62bdc951d1d614e836bd5ae292d45bd675dcacece9fc8c424850ff45b29d8` (brouillon 2, « à corriger », aucun bloquant ; corrections au § 10) ; contre-lecture du brouillon 1 : `…/contre-lecture-fiche-lancement-course-jang-feng-v1.md`, `a31c8250b91ff22e029618205cf9dfbd9a90884e7fa96fdc7b84ec426921017c`.

## 1. Nature de la course, sources, mots de Lazar

- **Course NON décisive** : matière à réflexion pour Lazar ; aucune porte, aucune revendication, aucun chiffre opposable (R7).
- Ordre : message de session-depot du 3 novembre, 14:10 UTC (« même réglage » que Colognese-Ward : celui d'Ibrahim, Argon s'il est
  libre au départ, refus de classifieur jamais rejoué, R-486) ; aucune spécification de conv-audit propre à cette course n'a été
  transmise au rédacteur : la question servie dit elle-même la section servie et le format. Règles du juge : n° 419 de conv-audit.
  Copies à l'octet dans `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/`, prises sur `canal/conv-audit-n04`
  et vérifiées à leurs compagnons :
  question `question-course-jang-feng-v1.md` (`d68c6c5ca567c2a867c9a0eb0e64d7b7340af0414e0f382c19416d67ab63c10e`) ;
  pièce `piece-jang-feng-v1.md` (`1f42364322988bf591ead6ce41842dd389ab179b11bc27853d66750ab5196774`, 11 992 caractères) ;
  pièce `piece-nos-resultats-v1.md` (`d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c`) ;
  protocole `protocole-rapport-mentors-soir-v1.md` (`fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`) ;
  n° 419 `conv-audit_2026-11-03_n419.md` (`75aedf2ea88361e7b76cd990791f445466c17ac4c87943f96da9efcf9266834b`).
- Servis aux proposeurs : **deux sections** de la question (« La question, telle que les mentors la posent », qui porte aussi le
  paragraphe « Ce qui est attendu d'une fiche », et « Règles d'intégrité », jusqu'à la fin du texte) ; puis les pièces, dans cet
  ordre : Feng et Jang, nos résultats. Rien de la candidature n'est servi.
- Mot de Lazar, **direct**, à session-depot, à la lettre : « go courses Scheurer, Colognese-Ward Q2, Jang-Feng, dans cet ordre ;
  pas de plafond » (reçu entre 13:39:07 et 13:49:07 UTC, `registres/decisions.md`, R-1149). Mot chez conv-audit, rapporté par la
  question servie (14:38, heure de Paris) : « lance des courses pour tout le monde par ordre de préférence du mentor et si on n'a
  pas le temps de voir la course avant de rédiger tant pis ». Lignes de GO (une par S17, plafonds techniques, aucun n'est un
  plafond de Lazar) : **`GO-2026-11-03-12`, 198 USD** (inscrite sur `main` à `9d40b65d`), pour les variantes `cinq-especes`,
  `avec-kimi` et `sans-kimi` ; **`GO-2026-11-03-13`, 237 USD** (inscrite sur `main` à `7957d2fe`), pour la seule variante
  `sans-opus-argon` ; **`GO-2026-11-03-14`, 198 USD** (inscrite sur `main` à `0cd40b80`), pour la seule variante `sans-opus`.
- Instrument : orchestrateur v56 (copie à l'octet vérifiée, 218 fichiers), génération de la mini-course, au-dessus
  `course_jangfeng_v2.py` (v1 gardée, R12 : deux variantes de plus, jeu de rôles par variante comme le kit Scheurer). Une
  génération, une passe, **6 fiches par proposeur**.

## 2. Variantes, lignes de GO et règle de lancement

| Variante | Proposeurs | Aiguilleur, juges, lecteurs | S17 | Ligne de GO (`GO_ID` et 2ᵉ argument du lanceur) |
|---|---|---|---|---|
| `configuration-course-jang-feng-v1-cinq-especes.json` | Fable 5.1, Opus 5.5, Argon, Kimi, Astra | Opus 5.5, Astra | 198 | `GO-2026-11-03-12` |
| `configuration-course-jang-feng-v1-avec-kimi.json` | Fable 5.1, Opus 5.5, Kimi, Astra | Opus 5.5, Astra | 198 | `GO-2026-11-03-12` |
| `configuration-course-jang-feng-v1-sans-kimi.json` | Fable 5.1, Opus 5.5, Astra | Opus 5.5, Astra | 198 | `GO-2026-11-03-12` |
| `configuration-course-jang-feng-v1-sans-opus-argon.json` (neuve, v2) | Fable 5.1, Argon, Kimi, Astra | **Fable 5.1**, Astra | **237** | `GO-2026-11-03-13` |
| `configuration-course-jang-feng-v1-sans-opus.json` (neuve, v2) | Fable 5.1, Kimi, Astra | **Fable 5.1**, Astra | 198 | `GO-2026-11-03-14` |

Les trois premières configurations sont celles du brouillon 1, inchangées (mêmes empreintes). Metteur : Fable 5.1 partout. Claude
par un seul relais 8806, `--effort high --reflexion adaptative`, aucune bascule. Lanceur : `jangfeng/lancer-course-jangfeng-v2.sh`
(accepte les cinq configurations ; le lanceur v1 reste gelé et n'accepte que les trois premières).

**Comment le lanceur choisit la ligne de GO.** Il ne vérifie qu'une ligne : celle que nomme son deuxième argument, qui doit être
égal à `GO_ID`, présent dans le registre, et que le lanceur Python reçoit comme `--go-attendu` ; il exige que le montant de cette
ligne soit exactement le S17 de la configuration. Le choix se fait donc à la main, par variante, selon le tableau ci-dessus :
`GO-2026-11-03-13` avec `sans-opus-argon` (237), `GO-2026-11-03-14` avec `sans-opus` (198), `GO-2026-11-03-12` avec les trois
autres (198). Le lanceur ne contrôle que le montant : GO-12 et GO-14 ont le même ; l'appariement de `sans-opus` à GO-14 est donc
une règle de cette fiche, que session-depot vérifie dans la commande avant le lancement. Un mauvais appariement est
refusé avant tout appel (essai `test_v2_go_attendu_par_variante`).

**Règle de lancement, déclarée d'avance (décision de session-depot).**
1. **Premier run** (dossier de run neuf) : `cinq-especes` si Argon est libre au départ (aucun tour ni autre course ne l'utilise ;
   session-depot le vérifie par l'état des filles et du relais 8805 ; le refus de port pris ne voit que l'hôte local), sinon
   `avec-kimi` ; `sans-kimi` seulement si le contrôle de Kimi échoue.
2. **Repli après un refus d'Opus** : si Opus refuse (C13 à la proposition, ou trois échecs consécutifs ou C13 à l'aiguillage, au
   jugement ou aux étiquettes), la course s'arrête **sans fiche** et la question **n'est pas rejouée à Opus** (R-486). On relance
   alors, dans un **second dossier de run neuf**, `sans-opus-argon` si Argon est libre (sous `GO-2026-11-03-13`), sinon
   `sans-opus` (sous `GO-2026-11-03-14`). Ce repli est déclaré ici : ce n'est pas un écart. Il n'y a pas d'autre relance.
3. La dépense du premier run arrêté reste comptée dans son propre registre ; chaque run a son registre cumulé et son S17.

**Risque de refus d'Opus (CLJ-01).** Aucun tour du collisionneur n'a éprouvé cette question. Opus 5.5 a refusé, au tour du
soir, la question Scheurer (catégorie « cyber »). La pièce Feng et Jang en partage des sources et des thèmes :
- 2510.09462 (injections d'invite contre les moniteurs, solutions piégées ; pièce § 2.4), aussi dans la pièce Scheurer (§ 3.4) ;
- les portes dérobées (2411.17693, pièce § 1.3), thème de la pièce Scheurer (§ 3.3, § 3.4) ;
- l'évasion des moniteurs latents (2609.36490, pièce § 2.2).
Elle nomme aussi les bancs « Weapons of Mass Destruction Proxy » et « Virology Capabilities Test » (pièce § 1.2). Un refus d'Opus
proposeur déclenche C13 (un seul échec suffit) ; un refus d'Opus aiguilleur, juge ou lecteur compte comme un échec du rôle. Les
deux variantes sans Opus servent de repli ; Fable 5.1, même famille, n'y est pas éprouvée non plus sur cette question.

## 3. Déclarations

1. **Aucun témoin planté** dans la course (le « témoin » que la question demande est celui de chaque expérience proposée, champ
   `controle`).
2. **Juge réécrit pour cette question** (n° 419, dans cet ordre, et la question) : K1 précis et faisable en jours ; K2 résultat
   attendu chiffré et signé, et la chose qui le rendrait trompeur avec son contrôle ; K3 prolonge un travail des mentors ; K4, tiré
   de la question : falsifiable, avec son témoin et le résultat qui la tuerait. **L'originalité n'est pas un item** (n° 419). Le
   juge voit la section « La question » telle quelle (paragraphe « Ce qui est attendu d'une fiche » compris), pas les pièces : il ne
   peut pas vérifier les identifiants ni ce que les travaux des mentors ont déjà fait (K3) ; choix du rédacteur déclaré (CLJ-04) :
   les exemples de témoin de K4 (« boîte noire, organisme bénin ou ligne de base calibrée ») viennent de la pièce (2512.07810,
   2507.12691), pas de la question, qui dit seulement « son témoin » ; ils sont gardés pour ne pas changer la consigne gelée ; les sorties des deux juges sont
   rapportées à part. Aiguilleur au niveau Kirchner v2 (« en cas de doute, concret » gardé ; planter des comportements pour
   éprouver une mesure ou un juge est `niveau_methode` ; seule la recette opérationnelle contre une évaluation ou un moniteur réels
   est `concret`) : la question porte sur l'évasion des moniteurs (pièce § 2.2, § 2.3), le risque d'un classement `concret` à tort
   est réel ; il ne coûte que des fiches comptées, non gardées. Lecteur et metteur : même mécanique.
3. **Champs** (format du kit) : `titre`, `hypothese` (l'affirmation falsifiable), `axe`, `epreuve` (l'expérience qui la tranche),
   `controle` (le témoin ; ce qui rendrait le résultat trompeur et son contrôle), `prediction`, `test_de_mort` (le résultat qui la
   tuerait), `cout`. **Axes** : `valeur_pour_l_audit` et `limite_actuelle` sont tirés de la question (« la valeur… », « leurs
   limites actuelles ») ; `comparaison_a_la_boite_noire` est un **choix du rédacteur** (CLJ-04), tiré de la pièce (2507.12691 : gain
   de la boîte noire à la boîte blanche ; 2512.07810 : boîte noire battue), pas de la question ; gardé (consignes gelées), déclaré.
4. **Bras joués** : `gu_krenn` (substitut) et `basique` (exposant 8,5, décalage 0,05), quatre paires par bras. Liste fermée : 67
   concepts tirés des seuls textes servis (`pieces/concepts-jangfeng-v1.json`). Source du substitut
   (`pieces/source-gu-krenn-jangfeng-v1.json`, `0bac077695d20cf4…`) : 19 œuvres, une par source citée (11
   de la pièce Feng et Jang : le flux de mentorat, 2604.28182, 2411.17693, 2409.12822, 2512.07810, 2609.36490, 2602.08877,
   2510.09462, 2401.14446, 2509.21344, 2507.12691 ; 8 de « nos résultats », les mêmes que pour Scheurer) ; aucun rapprochement du
   rédacteur. Choix déclarés : les questions ouvertes (§ 3 de la pièce) sont rendues aux deux œuvres qu'elles citent ; « sonde
   linéaire » est à 2409.12822, 2512.07810 et 2509.21344 ; « moniteur boîte blanche » au seul P3 de « nos résultats ». Codage non
   contre-lu. **Bras méta hors course.**
5. **Garde lexicale** (mode « prefixe », action « fiche exclue ») : celle d'Ibrahim, entière : `exploratoire`, `bras méta`,
   `gu et krenn`, `gu krenn`, `bisociation`, `kimi`, `moonshot`, `gemini`, `fable`, `astra`, `openai`, `gpt 6`, `gpt6`, `gpt-6`,
   `chatgpt` ; aucune n'apparaît dans les textes servis (vérifié). « claude », « opus », « anthropic », « sonnet », « gpt »,
   « argon » et « fusion » sont refusés dans la liste (la pièce cite Claude Sonnet 4, Claude Opus 4.5, GPT-4.1, GPT-5 ; « nos
   résultats » nomme Argon). Vérifié avant tout appel, et par un essai.
6. **Consigne du proposeur** (`pieces/consigne-proposeur-jangfeng-v1.md`, `d42df37e03e12e208ca03e19afe1b3c7345c361f2b0991afb6abae7d8134b6b8`) :
   deux sections de la question, puis les deux pièces entières, dans cet ordre, à l'octet (vérifié avant tout appel), puis le
   livrable du kit ; titre et provenance non servis. Cette question n'a ni « Ce qu'on attend de chaque espèce » ni « Lecture
   prévue », ni la règle des 1 200 mots.
7. **Plafonds techniques S17, par variante** (portée « course », arrêt d'étape 0,9 × S17 ; garde contre une boucle, sur le mot
   direct « pas de plafond » ; aucun n'est un plafond de Lazar) : S17 = le plus grand de 198 et de l'entier supérieur à 1,2 × le
   pire cas de la variante (calcul). **198 USD** pour `cinq-especes` (1,2 × 164,64 = 197,57), `avec-kimi`, `sans-kimi` et
   `sans-opus` (1,2 × 159,53 = 191,4) : `GO-2026-11-03-12`, et `GO-2026-11-03-14` pour `sans-opus` ; **237 USD** pour `sans-opus-argon` (1,2 × 196,92 = 236,3) :
   `GO-2026-11-03-13`. Fable aux rôles d'Opus coûte plus cher (10 / 50 contre 4 / 20 USD par million) : d'où le pire cas plus haut.
   Relais (cinq espèces) : Kimi 2 USD (≤ 5), Argon 3 USD (≤ 10), Astra 102,0, Claude 91,0 ; `sans-opus` : Kimi 2, Astra 65,3, Claude
   130,7 ; `sans-opus-argon` : Kimi 2, Argon 3, Astra 83,7, Claude 148,3. Plafonds de session des variantes neuves : aiguilleur 0,9
   (Fable, pire cas 0,8465), les autres comme avant ; ceux des trois configurations v1 sont inchangés (aiguilleur 0,4 > 0,3386).
8. **Marge d'appels** (comme Ibrahim v2) : `max_appels` de chaque relais = 2 × le plan + 5 ; plafonds en dollars inchangés. **Borne**
   (fiches en trop tolérées, toutes espèces, calcul) : cinq espèces 35 (Claude 301 pour 148 au plan, Astra 205 pour 100) ; avec Kimi
   29 ; sans Kimi 23 ; `sans-opus` 23 (Claude 203 pour 99, Astra 133 pour 64) ; `sans-opus-argon` 29 (Claude 251 pour 123, Astra 169
   pour 82). Au-delà : arrêt à l'étape des étiquettes, sans fiche.

## 4. Devis (`jangfeng/devis-course-jangfeng-v2.txt`, `9eeb769e454f0cf59bdabf94a05cee943ee5577d2f71144977fcd4178975ded1` ; le devis v1 reste gelé)

| Variante | Appels (course + contrôles) | Attendu | Pire cas | S17 | Part Kimi (att. / pire) | Part Argon (att. / pire) |
|---|---|---|---|---|---|---|
| cinq espèces (premier run si Argon libre) | 247 + 5 | 19,03 USD | 164,64 USD | 198 | 0,22 / 0,79 | 0,21 / 1,72 |
| avec Kimi (premier run sans Argon) | 204 + 4 | 16,17 USD | 139,47 USD | 198 | 0,22 / 0,79 | — |
| sans Kimi | 161 + 3 | 13,31 USD | 115,24 USD | 198 | — | — |
| sans Opus, avec Argon (repli) | 204 + 5 | 22,59 USD | 196,92 USD | 237 | 0,22 / 0,79 | 0,21 / 1,72 |
| sans Opus (repli sans Argon) | 161 + 4 | 18,37 USD | 159,53 USD | 198 | 0,22 / 0,79 | — |

Hypothèses : celles du devis Ibrahim. Plafonds de session (v2, toutes variantes) : proposeur 3,5 > 3,271 ; aiguilleur 0,9 > 0,8465
(Fable) ; juge 0,9 > 0,8493 ; lecteur 0,9 > 0,8498 ; fusion 3,5 > 3,2862. Course à blanc v2 : nombre d'appels identique au plan dans
les cinq variantes (`jangfeng/course-a-blanc-jangfeng-v2.txt`, `9f580bf4d0f9e2e765f40373bd8b2b53d786dae07f344f1749f35693fac51878`). Contrôles d'avant course :
le lanceur contrôle toujours Opus (« réponds seulement par le mot OK », sans la question), y compris dans les variantes sans Opus.

## 5. Liste d'arrêt

Avant la course : un contrôle d'avant course en échec. Pendant : modèle servi différent ; trois échecs consécutifs d'un rôle
(un refus compte comme un échec) ; débordement de la garde de Kimi proposeur (plus de 3 fiches `concret` sur 6) ; dépassement de
réserve ; garde cumulée ; garde d'étape ; plafond propre d'un relais (HTTP 402 ou 429 : nombre d'appels épuisé compris) ;
plafond de l'étape ; **nœud C13 (A14 : plus de 25 % d'appels inexploitables pour un rôle ; pour un proposeur, un seul échec
suffit)** ; signal ; toute autre exception. **Tout arrêt ou nœud après la proposition ne rend ni fiches ni classement** ;
restent lisibles journaux, manifestes, consommations, coffre, journal de l'aiguillage ; les réponses brutes ne survivent pas.
Codes du lanceur : 124 délai de 12 h ; 6 clé trouvée (pas de copie au canal) ; 7 trace refusée ou sceau en échec.

## 6. Lecture prévue

Sortie scellée avant lecture, copiée à l'octet dès son scellement avec sa liste, sonnette ; rien lu par session-depot. Rapport au
protocole « mentors du soir » **par extension** (aucun tour du collisionneur du soir sur cette question n'est connu du rédacteur :
les trois tours du soir portent sur Ibrahim, Scheurer, Colognese et Ward ; les fiches de la course seraient alors les entrées de
l'étape A, avec les fiches du matin pour ces mentors s'il y en a) ; à confirmer par conv-audit. `fiches.json` ne contient que les fiches munies d'un passeport et les fusions complètes. Lazar écrit seul sa réponse.

## 7. Gardes éprouvées et non éprouvées

Éprouvées hors réseau, kit v2 : 57 essais (`jangfeng/test_course_jangfeng_v2.py`, gelé ; dont les deux variantes neuves, les
empreintes inchangées des trois configurations v1 et l'appariement de la ligne de GO à S17) ; dix mutations, toutes détectées
(`jangfeng/resultat-mutations-jangfeng-v2.txt`, `db539fcd2d5936ab51cb7b4b2ed6570eff7fbfca559fe9babf77dab2d3f6fce9`) ; répétition v2 derrière de faux
amonts à 8 fiches par proposeur : cinq essais conformes (`jangfeng/repetition/resultat-repetition-jangfeng-v2.txt`,
`107e191257a820114de4ca461c44c8ac8774bc08bc7f6c3083f737c24ff90ac5`) ; `sans-opus-argon` au bout (code 0, 32 fiches, 8 fusions ; Claude 155
appels sur 251, Astra 106 sur 169) sous une ligne de GO factice à 237 ; `kill -TERM`, contrôle en échec et plafond de session bas
sur `sans-opus` sous une ligne à 198. Kit v1, toujours gelé : 47 essais (`jangfeng/test_course_jangfeng_v1.py`) ; dix mutations, toutes
détectées (`jangfeng/resultat-mutations-jangfeng-v1.txt`, `4e02b0b56a6b152eb50bbc456bf2c021a47c5c8b88b675a66ed90d5532d905d9`) ; répétition par le
vrai lanceur derrière de faux amonts qui rendent **8 fiches par proposeur** (plan : 6) : cinq essais conformes
(`jangfeng/repetition/resultat-repetition-jangfeng-v1.txt`, `b7e07a9d36cf5235b203fcf88ca5cae35c1e4fb46e18a1148202c2c94b3988ba`) ; à
cinq espèces, la course va au bout (code 0, 40 fiches, 8 fusions ; Claude 188 appels sur 301, Astra 130 sur 205, Kimi et Argon
2 sur 9) ; `kill -TERM` (quatre espèces) : code 130, relais arrêtés.
Non éprouvés : la tenue d'Opus et de Fable sur cette question (§ 2) ; comportement de l'aiguilleur et de la garde sur des fiches de cette question ; tenue réelle de « six fiches » ;
solde de Moonshot ; ligne de GO réelle.

## 8. Écarts (à trancher par conv-audit)

1. Question servie : deux sections (la question et ses règles d'intégrité), comme Ibrahim ; la question servie ne nomme comme
   « section servie » que la question.
2. Juge : n° 419 (trois items, sans originalité) plus un item tiré de la question (K4), dont les exemples de témoin viennent de
   la pièce ; axe `comparaison_a_la_boite_noire` choisi par le rédacteur (§ 3.2, § 3.3).
3. Aucune spécification propre à cette course reçue par le rédacteur : réglage d'Ibrahim, ordre de session-depot (14:10 UTC).
4. Un refus de proposeur arrête la course (C13) : limite du noyau v56 ; la règle « refus jamais rejoué » vient du message de
   session-depot de 14:10 UTC (R-486) ; le repli sans Opus est déclaré d'avance (§ 2), ce n'est pas un écart (CLJ-02).
5. Lecture au protocole des « mentors du soir », par extension, sans tour du collisionneur (§ 6).
6. Aucun témoin planté ; bras méta hors course ; source du substitut écrite à partir des seuls textes servis.

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
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/EMPREINTES-orchestrateur-course-jang-feng-v1.txt` | `de9b57688cef1cc968f5e5fa94ed4368d0d8eca83f2b34c57a8ba841a535e3cd` | empreintes de la copie |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/VERIFICATION-COPIE-orchestrateur-v56-v1.txt` | `53f1c79ecad0b4de60651af12d75c59349f3b73cde63cf006c9f1ab04bb3852e` | vérification de la copie |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/argon/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | relais (appel de l'interface) |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/calcul_devis_course_jangfeng_v1.py` | `8a43ffba4ffdbdfcc6e9bbd0b09773c1af7e01763d1bbd292c5bc01d1887f7bf` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/calcul_devis_course_jangfeng_v2.py` | `bcc1423ace71d8cd6519203957b280c133217b3f685a8529ac2d64b8ad6d56a7` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/commande_claude_jangfeng_v1.py` | `67e31e04b69d6ba65334acd8ee7d62453e581a16775748f8301927b748bf0396` | commande |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-avec-kimi.json` | `b3501965b7054685bbf2722495854ebfccf2144781f4b5678fb258c05c9ead15` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-cinq-especes.json` | `073528ebe0d361a5158027080b75454fe4000fca03c9e77d0f2b9682b49e575c` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-sans-kimi.json` | `c4270524b26336c08f9ec2625d612750f651d554ea17db16e5ac54931c587bf6` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-sans-opus-argon.json` | `b2baa681a4ed94de75fb663194dbc939826b9c82397821ca2eb73133bd864fed` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-sans-opus.json` | `fccdac4f71f99ccd12aebe1a7036ab763d518ef12148906ae39895d2cd113698` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/construire_consigne_proposeur_jangfeng_v1.py` | `b501130d9a6bef70cc0b1ed647724f31f12a54fa13fa8f52b4ea14d87800e18d` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course-a-blanc-jangfeng-v1.txt` | `767dcd340162db6a04b3b1aa8d5e17c4ca695a7740bff007e9410f0b2149a2d2` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course-a-blanc-jangfeng-v2.txt` | `9f580bf4d0f9e2e765f40373bd8b2b53d786dae07f344f1749f35693fac51878` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course_a_blanc_jangfeng_v2.py` | `6c3f719db435f3b5da116878bfb0bdc47238efc6585021c7402d011a78b19d09` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course_jangfeng_v1.py` | `bcd6e65344e571d9261c04aa738c3321f95cd370961efedc7f73e454c3da5a5f` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course_jangfeng_v2.py` | `c50467431a47c98cd9b4c560f950173f8d00bf5ab17bf8a682b3fad5114a98cb` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/devis-course-jangfeng-v1.json` | `62c43f596c7d99a16d140f7cc382bcfe8a55546a79bf985aa9caa91942aafe17` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/devis-course-jangfeng-v1.txt` | `b32042190908cfabe987ad1bdbb0546d8a43a71aa82809d5af0c01d4f24121ce` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/devis-course-jangfeng-v2.json` | `3380dd95094fd31d3fa792d23a63669e89f239aee6970d26ae9bf5bc33ddfba7` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/devis-course-jangfeng-v2.txt` | `9eeb769e454f0cf59bdabf94a05cee943ee5577d2f71144977fcd4178975ded1` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/lancer-course-jangfeng-v1.sh` | `0e46449daa19159eee9e7e574ac2f3d4c4abcbb3037429e1574d08db42e5d665` | lanceur |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/lancer-course-jangfeng-v2.sh` | `13d08682ac7c9364a746f8dd193ee9b758fab1b9c5dd252e945da9f7d2bfe8d8` | lanceur |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/lancer_course_jangfeng_v1.py` | `37d4abe356a916cc5a332caa8687421969fb5d364cc9e7180488043b6899025d` | lanceur |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/lancer_course_jangfeng_v2.py` | `d273c9cd38ee221f0d88ef63f3002f9727fd35b6f6f4cd9dc2d30baba859b1b2` | lanceur |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/mutations_jangfeng_v1.py` | `a7007635a5f67ec72648ae85e2e744854d837d1bf80680f3d5e49d6a26d3569c` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/mutations_jangfeng_v2.py` | `480daaec3a83f84e8fa590eb384ac567f483e155b8612e27b5061b23d1fa5826` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/concepts-jangfeng-v1.json` | `60fb405787cf3f3d2988833114f0fcc782767fba930da5e5d4a276593a4a7714` | liste fermée |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/consigne-aiguilleur-jangfeng-v1.md` | `f1cd9072f0f911c5a0aa7ac1fdc0b4555d5f19c813566566d83298beeda7fd78` | consigne |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/consigne-juge-jangfeng-v1.md` | `0d8413989ecebc10b8b694687a90a6170f00e5bb40797224879b937b8d2c8497` | consigne |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/consigne-lecteur-jangfeng-v1.md` | `d698aa88f8791f4a4159f26de523a899bcf71e005b4487bbd32491d214c49a38` | consigne |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/consigne-metteur-jangfeng-v1.md` | `93f75632e1e2e364f2f058d6ff79d696e8883b48c67ce485beea7065de4bbd4a` | consigne |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/consigne-proposeur-jangfeng-v1.md` | `d42df37e03e12e208ca03e19afe1b3c7345c361f2b0991afb6abae7d8134b6b8` | consigne |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/conv-audit_2026-11-03_n419.md` | `75aedf2ea88361e7b76cd990791f445466c17ac4c87943f96da9efcf9266834b` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/piece-jang-feng-v1.md` | `1f42364322988bf591ead6ce41842dd389ab179b11bc27853d66750ab5196774` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/piece-nos-resultats-v1.md` | `d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/protocole-rapport-mentors-soir-v1.md` | `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/question-course-jang-feng-v1.md` | `d68c6c5ca567c2a867c9a0eb0e64d7b7340af0414e0f382c19416d67ab63c10e` | question servie |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/source-gu-krenn-jangfeng-v1.json` | `0bac077695d20cf424e988d57ceb5eeb857c1d7c815ecddfb7b40f15a60b4b97` | source du substitut Gu-Krenn |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/repetition/autorite_factice_jangfeng_v1.sh` | `2a12cec752b7e76d3200a72eb485eaed4c98f01705830ffb5422a84f55a5751d` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/repetition/faux_mandataire_tls_jangfeng_v1.py` | `6da0dfe69afa948e79fdf7f97e3a47404d220261b659ae2e7a5d085fc7ac8fb1` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/repetition/repetition_complete_jangfeng_v1.sh` | `0864a1febc2bce2997b9d48e064baef58d897ef277e651646db5c50a6bd399ed` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/repetition/repetition_complete_jangfeng_v2.sh` | `2632e1c2d516eae9751b4459f778241e612c66fb916c6ca262eccbb025938f46` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/test_course_jangfeng_v1.py` | `3745fbc9d585424067b944a228eddcb2f3243e64cc9874a361c3f086216a9fdb` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/test_course_jangfeng_v2.py` | `1bd968e2c098626944de3af8d53d24ee83e795a6f8271cb02ae1053c86b4b4f1` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/trace_agregee_course_jangfeng_v1.py` | `23289dc03915b9c0447cdeb2017f5c896453566585a6a6184b0466889998d662` | trace agrégée |
| `donnees/course-jang-feng-v1/orchestrateur/nuit/chercher_cles_v1.py` | `5d6f82fc5cc95f9998877852c08835b83df1ba572597303f447cb983cf97cf61` | recherche des clés |
| `donnees/course-jang-feng-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` | commande |
| `donnees/course-jang-feng-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande |
| `donnees/course-jang-feng-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `donnees/course-jang-feng-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/pole/course2_nuit_v2.py` | `5d15660eca9f23b9480cb6bf7a05379859255294d377652231d944170fe69032` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/pole/course2_v56.py` | `14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1` | génération |

## 9. Traitement de la contre-lecture du brouillon 1

| Constat | Gravité | Traitement |
|---|---|---|
| CLJ-01 risque de refus d'Opus sous-déclaré ; aucun repli sans Opus | majeur | corrigé : deux variantes neuves sans Opus (`sans-opus-argon`, `sans-opus` ; Fable aux rôles d'Opus), kit v2 (module, lanceurs, devis, table, course à blanc, essais, mutations, répétition) ; règle de lancement et repli déclarés d'avance ; risque décrit avec les sources communes à la pièce Scheurer (§ 2) |
| CLJ-02 l'écart n° 4 renvoyait à une règle sans source | mineur | corrigé (§ 8.4) |
| CLJ-03 numéro de GO connu | mineur | corrigé : `GO-2026-11-03-12` (198) et `GO-2026-11-03-13` (237), par variante (§ 1, § 2) |
| CLJ-04 exemples de témoin du juge et axe hors de la question | mineur | déclarés comme choix du rédacteur, avec leur origine dans la pièce (§ 3.2, § 3.3, § 8.2) ; consignes gelées non retouchées |

## 10. Traitement de la contre-lecture du brouillon 2 (par session-depot, version scellée)

| Constat | Gravité | Traitement |
|---|---|---|
| CLJ2-01 GO-12 ne nommait pas `sans-opus`, le kit v2 ni le devis v2 | majeur | corrigé : ligne neuve `GO-2026-11-03-14` (198 USD, kit `9f9ad98e`, configuration `fccdac4f…`, devis v2 `9eeb769e…`), sur le même mot direct de Lazar ; § 1, § 2 et § 3.7 citent GO-14 pour `sans-opus` ; GO-12 reste aux trois variantes v1 |
| CLJ2-02 sur quoi se constate le refus d'Opus | mineur | corrigé ici : le repli ne se joue que si le refus d'Opus est constaté **dans le journal du relais Claude 8806 et le manifeste de fin du premier run** (statut de refus pour `claude-opus-5-5`, à la proposition ou à un rôle d'Opus), lus sans le texte des réponses ; un C13 ou un arrêt dû à une autre espèce, une panne d'un fournisseur ou un échec technique ne déclenche **pas** le repli : session-depot en décide à part et le déclare |
| CLJ2-03 GO-13 dit « à inscrire » | mineur | corrigé : GO-13 inscrit sur `main` à `7957d2fe` (§ 1) |
| CLJ2-04 perte probable des fiches de Kimi | mineur | déclarée ici : dans la seconde course Kirchner et la course Ibrahim, toutes les fiches de Kimi ont très probablement été refusées au format (R-1155 ; `refusees_au_format` égal au quota de Kimi ; non vérifié au journal de proposition). La même perte est possible ici (même kit, prompts de même longueur) ; elle ne compte pas comme un arrêt et ne déclenche aucun repli ; elle est rapportée par espèce dans le rapport de la fille |
