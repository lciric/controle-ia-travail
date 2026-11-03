# Fiche de lancement — course d'idéation sur la question du mentor Scheurer — brouillon 1

Rédigée par un sous-agent de session-depot le 3 novembre 2026, 14:05 UTC (`date -u`). **Brouillon** : session-depot le fait
contre-lire par un lecteur neuf (R2), puis en écrit la version scellée sous un nom neuf (R12), qui cite l'empreinte du rapport à
la ligne ci-dessous. Le lanceur exige ce texte scellé, sans marqueur de remplissage, citant l'empreinte de sa contre-lecture, et
dont la table « Pièces gelées » couvre ce qu'il nomme. Aucune dépense, aucun appel réel pour l'écrire. Kit : celui de la course
Ibrahim v2 (`outils/course-ibrahim-q1-v1`, `965eb21b` : marge d'appels 2 × plan + 5, aiguilleur au niveau Kirchner v2, garde
lexicale v2, 6 fiches par proposeur), renommé et adapté (branche `outils/course-scheurer-v1`).

Contre-lecture : <<EMPREINTE_RAPPORT>>

## 1. Nature de la course, sources, mots de Lazar

- **Course NON décisive** : matière à réflexion pour Lazar ; aucune porte, aucune revendication, aucun chiffre opposable (R7).
- Ordre : message de session-depot du 3 novembre, 13:50 UTC (aucune spécification de conv-audit pour cette course : les règles
  sont celles d'Ibrahim, et celles du juge viennent du n° 419 de conv-audit). Copies à l'octet dans
  `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/`, prises sur `canal/conv-audit-n04` et vérifiées à leurs compagnons :
  question `question-collisionneur-scheurer-v1.md` (`edb1d5f130c9e60cfc35b12ba6a4fb83ce2c9805cd8ad91085d5c1f1aab5f930`) ;
  pièce `piece-scheurer-v1.md` (`2d0e60fc78e5930fb4ad1fe60d6fba8f2a17f4a03729570ea896db0c339f3796`) ;
  pièce `piece-nos-resultats-v1.md` (`d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c`) ;
  protocole `protocole-rapport-mentors-soir-v1.md` (`fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`) ;
  n° 419 `conv-audit_2026-11-03_n419.md` (`75aedf2ea88361e7b76cd990791f445466c17ac4c87943f96da9efcf9266834b`).
- Servis aux proposeurs : **deux sections** de la question (« La question, telle que le mentor la pose » et « Règles
  d'intégrité ») ; puis les pièces, dans cet ordre : Scheurer, nos résultats. Rien de la candidature n'est servi.
- Mot de Lazar, **direct**, à session-depot, à la lettre : « go courses Scheurer, Colognese-Ward Q2, Jang-Feng, dans cet ordre ;
  pas de plafond » (reçu entre 13:39:07 et 13:49:07 UTC, `registres/decisions.md`, R-1149). Ligne de GO : `GO-2026-11-03-NN`
  (numéro attribué à l'inscription par session-depot, cité au lancement).
- Contexte : au tour du collisionneur sur cette question, Opus 5.5 a refusé la question (catégorie « cyber ») après 3 cellules ;
  mot de Lazar rapporté au n° 421 de conv-audit : suite du tour sans l'espèce qui a refusé, cellule refusée non rejouée. Heure
  limite des fiches pour le choix de piste de ce soir (n° 421) : sortie scellée et copiée au canal avant 16:00 UTC.
- Instrument : orchestrateur v56 (copie à l'octet vérifiée, 218 fichiers), génération de la mini-course, au-dessus
  `course_scheurer_v1.py`. Une génération, une passe, **6 fiches par proposeur**.

## 2. Variantes (une seule est lancée)

| Variante | Proposeurs | Aiguilleur, juges, lecteurs | Quand |
|---|---|---|---|
| `configuration-course-scheurer-v1-sans-opus.json` | Fable 5.1, Kimi, Astra | **Fable 5.1** (aiguilleur, juge, lecteur), Astra (juge, lecteur) | **lancement recommandé** : aucun appel d'Opus sur la question |
| `configuration-course-scheurer-v1-sans-opus-argon.json` | Fable 5.1, Argon, Kimi, Astra | Fable 5.1, Astra | si Argon est libre (aucun tour ni autre course ne l'utilise ; session-depot le vérifie par l'état des filles et du relais 8805 ; le refus de port pris ne voit que l'hôte local) |
| `configuration-course-scheurer-v1-sans-opus-sans-kimi.json` | Fable 5.1, Astra | Fable 5.1, Astra | repli si le contrôle de Kimi échoue |
| `configuration-course-scheurer-v1-sans-opus-juges-opus.json` | Fable 5.1, Kimi, Astra | **Opus 5.5** (aiguilleur, juge, lecteur), Astra | si Lazar veut garder Opus aux rôles de lecture (moins cher, mais Opus lit alors toutes les fiches de cette question) |
| `configuration-course-scheurer-v1-avec-opus.json` | Fable 5.1, Opus 5.5, Kimi, Astra | Opus 5.5, Astra | **en second** : Opus proposeur, comme Ibrahim |

Metteur des fusions : Fable 5.1 dans toutes les variantes. Claude par un seul relais 8806, `--effort high --reflexion
adaptative`, aucune bascule. Lanceur : `scheurer/lancer-course-scheurer-v1.sh` (n'accepte que ces cinq configurations).

**Rôle d'Opus et remplaçant.** Dans les variantes `sans-opus`, Opus ne tient **aucun rôle** : Fable 5.1 le remplace comme
aiguilleur, juge et lecteur (le noyau le permet sans rien de neuf ; le jeu de rôles est vérifié avant tout appel). Raison : un
refus de l'aiguilleur, d'un juge ou d'un lecteur compte comme un échec du rôle ; trois échecs consécutifs ou plus de 25 %
d'appels inexploitables (C13) arrêtent la course **sans aucune fiche** (§ 5). Prix : Fable coûte plus cher qu'Opus (10 / 50
contre 4 / 20 USD par million) ; même famille qu'Opus, sa tenue sur cette question n'est pas éprouvée. Le lanceur hérité fait
toujours le contrôle d'avant course d'Opus (« réponds seulement par le mot OK », sans la question) : un appel, environ 0,003 USD.

## 3. Déclarations

1. **Aucun témoin planté**.
2. **Juge** (n° 419 de conv-audit, dans cet ordre, et la question) : K1 précis et faisable en jours ; K2 énoncé de tendance
   chiffré et signé, et la chose qui le rendrait trompeur avec son contrôle (la question demande l'énoncé chiffré et ses
   menaces) ; K3 prolonge un travail du mentor ; K4, tiré de la question : une vraie tendance (grandeur mesurée de la même façon
   d'un modèle à l'autre, échelle continue, modèles datés assez nombreux pour ajuster un facteur par mois ou par an).
   **L'originalité n'est pas un item** (n° 419) : elle se vérifie à la moisson. Le juge voit la section « La question » telle
   quelle, pas les pièces : il ne peut pas vérifier les identifiants ni ce que les travaux du mentor ont déjà fait (K3) ; les
   sorties des deux juges sont rapportées à part. Aiguilleur au niveau Kirchner v2 (« en cas de doute, concret » gardé ; planter
   pour éprouver une mesure ou un juge est `niveau_methode` ; seule la recette opérationnelle contre une évaluation ou un
   moniteur réels est `concret`). Lecteur et metteur : même mécanique.
3. **Champs** (format du kit) : `titre`, `hypothese` (la tendance énoncée), `axe`, `epreuve` (grandeur, échelle continue, modèles
   et dates, ajustement), `controle` (pourquoi elle a des chances de réussir ; menaces et contrôles), `prediction` (énoncé chiffré
   et signé), `test_de_mort` (ce qui ferait échouer le plan, ou le pilote non concluant), `cout` (le premier pilote). **Axes, tirés
   de la question** (déclaré : la question n'en donne pas la liste) : `propension_mal_alignee`, `capacite_mal_alignee`,
   `surveillance_et_controle`, `essaim_multi_agents`. La question demande trois à cinq tendances par espèce : la course en demande
   six par proposeur (comme Ibrahim) ; déclaré.
4. **Bras joués** : `gu_krenn` (substitut) et `basique` (exposant 8,5, décalage 0,05), quatre paires par bras. Liste fermée : 55
   concepts tirés des seuls textes servis (`pieces/concepts-scheurer-v1.json`). Source du substitut
   (`pieces/source-gu-krenn-scheurer-v1.json`, `b8e0ccbc2b250a3c…`) : 17 œuvres, une par source citée (9
   de la pièce Scheurer, 8 de « nos résultats ») ; concepts = ceux que les textes attribuent à cette source ; aucun lien posé
   par un rapprochement du rédacteur. Choix déclarés : la question n'est pas une source ; « tromperie » et « désalignement
   d'essaim » ne sont portés par aucune source (hors du vocabulaire de ce bras, dans la liste fermée) ; « tendance d'échelle »
   pour le METR et TastEval seuls ; « surveillance » pour la page d'Apollo, 2603.01608 et les deux papiers de moniteurs ;
   « contrôle » pour « Control Tax » seul. Codage non contre-lu. **Bras méta hors course.**
5. **Garde lexicale** (mode « prefixe », action « fiche exclue ») : celle d'Ibrahim **sans « gemini » ni « openai »** :
   `exploratoire`, `bras méta`, `gu et krenn`, `gu krenn`, `bisociation`, `kimi`, `moonshot`, `fable`, `astra`, `gpt 6`, `gpt6`,
   `gpt-6`, `chatgpt`. Retirés parce que la pièce Scheurer les emploie (« Gemini 3 Pro », « Gemini 2.5 » ; « Apollo Research et
   OpenAI ») : la garde les attraperait et exclurait toute fiche qui cite ces travaux ; prix : une fiche qui se dirait écrite par
   « Gemini » ou « OpenAI » passerait. « argon » et « fusion » restent retirés (la pièce « nos résultats » nomme Argon) ;
   « claude », « opus », « anthropic », « sonnet », « gpt », « argon », « fusion », « gemini » et « openai » sont refusés dans la
   liste. Vérifié avant tout appel, et par un essai : aucune étiquette dans la question, les deux pièces, les consignes servies, la
   liste ni le vocabulaire du substitut.
6. **Consigne du proposeur** (`pieces/consigne-proposeur-scheurer-v1.md`, `ab203b3789778b888df5a1a403b58ca8fb3b4efc94dbb09cb3a233c2bfced004`) :
   deux sections de la question, puis les deux pièces entières, dans cet ordre, à l'octet (vérifié avant tout appel) ; la section
   « Ce qu'on attend de chaque espèce », propre au collisionneur, est remplacée par le livrable du kit, qui en reprend les demandes
   champ par champ ; titre, provenance et « Lecture prévue » non servis. La section « Règles d'intégrité » servie à l'octet porte
   « Au plus 1 200 mots par cellule de conception » : la course n'a pas de cellule ; un proposeur peut la lire comme une borne
   pour ses six fiches à la fois (déclaré, consigne non retouchée).
7. **Plafond technique S17 = 237 USD** (portée « course », arrêt d'étape 213,3) : garde contre une boucle, sur le mot direct « pas
   de plafond » ; entier supérieur à 1,2 × 196,89 = 236,27 (calcul ; pire cas le plus haut, variante `sans-opus-argon`). La ligne
   de GO porte **un seul montant : « 237 USD »**. Relais à la variante de lancement : Kimi 2 USD (≤ 5), Astra 65,3, Claude 169,7.
8. **Marge d'appels** (comme Ibrahim v2) : `max_appels` de chaque relais = 2 × le plan + 5 ; plafonds en dollars inchangés. Une
   fiche de plus coûte 4 appels Claude (aiguilleur, juge, deux lectures) et 3 appels Astra. **Borne** (fiches en trop tolérées,
   toutes espèces, calcul) : `sans-opus` 23 (Claude 203 pour 99 au plan, Astra 133 pour 64) ; `sans-opus-argon` 29 ;
   `sans-opus-sans-kimi` 17 ; `sans-opus-juges-opus` 23 ; `avec-opus` 29. Au-delà : arrêt à l'étape des étiquettes, sans fiche.

## 4. Devis (`scheurer/devis-course-scheurer-v1.txt`, `2b16851202d2be39090014a3f9b11f34458e44184434c0b89c65f4af6ea163db`)

| Variante | Appels (course + contrôles) | Attendu | Pire cas | Part Kimi (att. / pire) | Part Argon (att. / pire) |
|---|---|---|---|---|---|
| sans Opus (lancement) | 161 + 4 | 18,40 USD | 159,51 USD | 0,22 / 0,79 | — |
| sans Opus, avec Argon | 204 + 5 | 22,62 USD | 196,89 USD | 0,22 / 0,79 | 0,20 / 1,71 |
| sans Opus, sans Kimi | 118 + 3 | 14,17 USD | 123,07 USD | — | — |
| sans Opus proposeur, Opus aux rôles | 161 + 4 | 13,34 USD | 114,71 USD | 0,22 / 0,79 | — |
| avec Opus (second) | 204 + 4 | 16,19 USD | 139,45 USD | 0,22 / 0,79 | — |

Hypothèses : celles du devis Ibrahim (3,48 caractères par jeton, médiane mesurée au second tour ; sorties attendues supposées,
proposeur 9 000 jetons pour 6 fiches ; pire cas = sortie maximale de chaque appel, toutes fiches admises ; prix Fable 10 / 50,
Opus 4 / 20, Astra 10 / 50 supposé, Kimi 2 / 10, Argon 10 / 50 supposé). Plafonds de session (pire cas d'un appel de chaque
rôle sur toutes les variantes) : proposeur 3,5 > 3,2647 ; aiguilleur 0,9 > 0,8462 (Fable) ; juge 0,9 > 0,8513 ; lecteur 0,9 >
0,8485 ; fusion 3,5. Course à blanc : nombre d'appels identique au plan dans les cinq variantes
(`scheurer/course-a-blanc-scheurer-v1.txt`, `88a62108c25c63e4551ebc8023aa5fdca0fc2e9c0ab551fcd1e559d6c8c7246a`).

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
protocole « mentors du soir » (lecteur neuf, moissonneurs, classeur ; envoi brut à Lazar dès la copie), **par extension** : le
protocole ne prend en entrée que les cellules du tour du collisionneur et les fiches du matin. Proposé, comme pour Ibrahim : les
fiches de la course entrent à l'étape A avec les cellules du tour Scheurer, comme des cellules d'espèce de plus (provenance
« course » gardée sous la clé à part), et le dédoublonnage par structure joue entre elles ; à confirmer par conv-audit.
`fiches.json` ne contient que les fiches munies d'un passeport et les fusions complètes ; les fiches `a_corriger`, `concret` ou
exclues sont comptées, non gardées. Lazar écrit seul sa réponse.

## 7. Gardes éprouvées et non éprouvées

Éprouvées hors réseau : 55 essais (`scheurer/test_course_scheurer_v1.py`, gelé) ; contre-épreuve par dix mutations, toutes
détectées (`scheurer/resultat-mutations-scheurer-v1.txt`, `d094296e32a27e121bbf0260959f5526c0f01cf0f2e33d0a94d582282d9564f7`) ; répétition par le vrai
lanceur derrière de faux amonts qui rendent **8 fiches par proposeur** (plan : 6) : cinq essais conformes
(`scheurer/repetition/resultat-repetition-scheurer-v1.txt`, `5e9d0af4a14f1417c1ef7a413cdb3d7e02fe426efcd4f4177234f5a147978714`) ; course
complète `sans-opus-argon` au bout (code 0, 32 fiches, 8 fusions ; Claude 155 appels sur 251, Astra 106 sur 169) ; `kill -TERM`
sur `sans-opus` : code 130, relais arrêtés.
Non éprouvés : la tenue de Fable 5.1 (aiguilleur, juge, lecteur, proposeur) et d'Astra sur cette question (un refus arrête) ;
le comportement de l'aiguilleur et de la garde sur des fiches de cette question ; la tenue réelle de « six fiches » ; solde de
Moonshot ; ligne de GO réelle.

## 8. Écarts (à trancher par conv-audit)

1. Aucune spécification de conv-audit pour cette course : règles d'Ibrahim et ordre de session-depot (13:50 UTC).
2. Question servie : deux sections ; règle « 1 200 mots par cellule » servie telle quelle (§ 3.6).
3. Juge : n° 419 (trois items, sans originalité) plus un item tiré de la question (K4).
4. Six fiches par proposeur pour « trois à cinq tendances » demandées par la question.
5. Fable 5.1 à la place d'Opus aux rôles de lecture dans les variantes `sans-opus` ; contrôle d'Opus gardé (« OK »).
6. Garde lexicale sans « gemini » ni « openai » (employés par la pièce servie), ni « argon » ni « fusion ».
7. Lecture au protocole des « mentors du soir », par extension (§ 6).
8. Aucun témoin planté ; bras méta hors course ; source du substitut écrite à partir des seuls textes servis.

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
| `donnees/course-scheurer-v1/orchestrateur/nuit/chercher_cles_v1.py` | `5d6f82fc5cc95f9998877852c08835b83df1ba572597303f447cb983cf97cf61` | recherche des clés |
| `donnees/course-scheurer-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` | commande |
| `donnees/course-scheurer-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande |
| `donnees/course-scheurer-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `donnees/course-scheurer-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération |
| `donnees/course-scheurer-v1/orchestrateur/pole/course2_nuit_v2.py` | `5d15660eca9f23b9480cb6bf7a05379859255294d377652231d944170fe69032` | génération |
| `donnees/course-scheurer-v1/orchestrateur/pole/course2_v56.py` | `14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/EMPREINTES-orchestrateur-course-scheurer-v1.txt` | `de9b57688cef1cc968f5e5fa94ed4368d0d8eca83f2b34c57a8ba841a535e3cd` | empreintes de la copie |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/VERIFICATION-COPIE-orchestrateur-v56-v1.txt` | `5fb1b202f3cb637c9e4aa72b826f654dc46f963ad18631eb8806ba1d53a3fb84` | vérification de la copie |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/argon/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | relais (appel de l'interface) |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/calcul_devis_course_scheurer_v1.py` | `61ec99e4242cb6f6d4613ad24cd801427a1c6685d9904517f5d2b19c679ab442` | devis |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/commande_claude_scheurer_v1.py` | `efcb2c0a41bdaa76870b889c9badcc8f3307fe3226f5354be9ddad32e34f6ca3` | commande |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-avec-opus.json` | `916aff7059ec829c26e57af85b792b357481a3498ba474c7395c2df6b00745ca` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-sans-opus-argon.json` | `364f2c91bcfe904734625c2f3382fcc8da2630eb169f8b097c5b1eab121fe258` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-sans-opus-juges-opus.json` | `02a36104ce9847275bba2d408883acbb180cba3dc7ff2ca295c799540499871d` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-sans-opus-sans-kimi.json` | `46d5025f3ef3cd22bffabcbc8cf6f3c90dfb3163b633687513ae500032ef0dbd` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-sans-opus.json` | `e6e739d7c70b262b9fec7c26681ed1cc1b089fe11ac72c7a7f1b07db52f1ca23` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/construire_consigne_proposeur_scheurer_v1.py` | `2f61e503e57e259c31eeb98f71e14a41ebb65f3ea7909a1aaf0abf121f134e4a` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/course-a-blanc-scheurer-v1.txt` | `88a62108c25c63e4551ebc8023aa5fdca0fc2e9c0ab551fcd1e559d6c8c7246a` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/course_a_blanc_scheurer_v1.py` | `f7ca888bf3b81bc7a7c5274318e15ea2c7fbc267047c2f01a089b72a2cce544d` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/course_scheurer_v1.py` | `abe9a5422129dd064c40ab172eb751f7f4b0eef6ecaf7322dda0c689b15681a4` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/devis-course-scheurer-v1.json` | `fdcb91ef6305d6e321c7506821edebce2e6feb1c1392ad80c0f6c5e0f240567e` | devis |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/devis-course-scheurer-v1.txt` | `2b16851202d2be39090014a3f9b11f34458e44184434c0b89c65f4af6ea163db` | devis |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/lancer-course-scheurer-v1.sh` | `8683cc240306a31d47920c7d7c1bf4fcbd32d25fcc1e85203f446b1363083ec1` | lanceur |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/lancer_course_scheurer_v1.py` | `1f551d925fb9a4f3336d10d341523282b2521d7ea44dd0bbdae3e674bc2cfb38` | lanceur |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/mutations_scheurer_v1.py` | `6630dd8c378e37ea32bfa2fb55885d59cd0de1b4b06f3ba1a5004173d83bf946` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/concepts-scheurer-v1.json` | `a169ce62506f06004cd8ed5470d96041f6993e18db98fb210fe20f72d192d3a7` | liste fermée |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/consigne-aiguilleur-scheurer-v1.md` | `38ca7c012f31b53b813cde50f0387a695642f27cfb4bbe70d7f00b35f3bc8cc7` | consigne |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/consigne-juge-scheurer-v1.md` | `8215d020969cfbd2a0e751997d628056cdea06b487b3743bf4d1a092fa2493ff` | consigne |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/consigne-lecteur-scheurer-v1.md` | `7bc3e6dd87265f50a1f930badd2a2b51d5a3e1498f17be52b48d66ef59bc83e3` | consigne |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/consigne-metteur-scheurer-v1.md` | `0549b7677e2bd12c1efde1b289aa21fba124df77f1a4008cea624f82f0795c40` | consigne |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/consigne-proposeur-scheurer-v1.md` | `ab203b3789778b888df5a1a403b58ca8fb3b4efc94dbb09cb3a233c2bfced004` | consigne |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/conv-audit_2026-11-03_n419.md` | `75aedf2ea88361e7b76cd990791f445466c17ac4c87943f96da9efcf9266834b` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/piece-nos-resultats-v1.md` | `d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/piece-scheurer-v1.md` | `2d0e60fc78e5930fb4ad1fe60d6fba8f2a17f4a03729570ea896db0c339f3796` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/protocole-rapport-mentors-soir-v1.md` | `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/question-collisionneur-scheurer-v1.md` | `edb1d5f130c9e60cfc35b12ba6a4fb83ce2c9805cd8ad91085d5c1f1aab5f930` | question servie |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/source-gu-krenn-scheurer-v1.json` | `b8e0ccbc2b250a3cdeec3587e5d1e7a33766aa4a8e37a4dfc474f14cfccea15a` | source du substitut Gu-Krenn |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/repetition/autorite_factice_scheurer_v1.sh` | `083b3031344ff158ae763e33dd0275db41567cf3f68e4debde8087526d110698` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/repetition/faux_mandataire_tls_scheurer_v1.py` | `3c33de3998e27b294d73896e0a61c1e249b4ea1e5ddf67dedb4966aaa8f26057` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/repetition/repetition_complete_scheurer_v1.sh` | `6a45fccdbb044f41fe9162aa36085ef2d2cf2f931bbebc31512074a0fe3787bf` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/test_course_scheurer_v1.py` | `3288dca6cfeb7e349e26a90ee6f97fb581489bd2c951b66d07ab7446f26e71ac` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/trace_agregee_course_scheurer_v1.py` | `1815d1b5cbce182b6c6a280de493baa4cdcabb7c9c5759cfa6d9f750d6ff331b` | trace agrégée |
