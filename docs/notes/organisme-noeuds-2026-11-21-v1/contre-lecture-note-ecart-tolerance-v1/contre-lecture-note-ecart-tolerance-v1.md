# Contre-lecture du projet de note d'écart « tolérance du contrôle par l'aire pour les lois arrondies » — v1

**Verdict : À corriger.** Sur le fond, l'écart tient : il ne convertit que des aires encadrantes à 0,02 au plus, ne joue que sur une loi arrondie (et ne peut rien convertir de plus sur une loi continue), ne touche que l'alinéa visé, et ne dépend d'aucune sortie de l'auteur. Deux défauts de lettre sont à corriger avant le scellement : (A) la ligne 27 convertit « alors » le saboteur de la famille sur un seul décalage, sans dire « chaque décalage de la famille » ; (B) la ligne 28 ne nomme pas tous les cas non convertis (le cas d'une aire encadrante réalisée au-delà de 0,02 alors que l'autre est en deçà n'a aucune des deux raisons). Un troisième point est à préciser : (C) « arrondie » n'est pas défini.

Contre-lecteur neuf, hostile, aveugle : je n'ai lu aucune autre relecture, aucune sortie de l'auteur des mondes, aucune pièce de quarantaine ni de matière première.

## Pièces lues (toutes par `git show origin/main:<chemin>` redirigé, empreinte recalculée par `sha256sum`)

| pièce | chemin | sha256 recalculée | attendue |
|---|---|---|---|
| projet de note (objet) | docs/notes/organisme-noeuds-2026-11-21-v1/pieces-v2/projet-note-d-ecart-tolerance-du-controle-par-l-aire-lois-arrondies-v1.md | 9bcbff4d07d5d7c426d32ea5a641e7d7cf0ff5c2dd73e2838a732dfb143dec5b | non fournie |
| pièce scellée | prereg/ideation-seuil-moniteurs-v1/scellement-erratum-v5-texte-servi-v3-devis-v8-mondes-plantes-v1.md | dfe0aace22a2e0eb4fa48656556e3be7ef532801304323b9a95c6f99dffae171 | identique |
| source du concepteur (§ 6 seulement) | docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md | 4521273497513cb0de5eecdedfce4a6f088dd367b4e8675cc436d40d463af15e | identique |
| règle | docs/notes/organisme-noeuds-2026-11-21-v1/pieces-v2/tolerance-reseaux-programme-verification-sortie-mondes-v2.md | 3806ff34cebfe862dbb400342915206103a7f51430de19265cd04a005ea1d776 | non fournie |
| registre des accords | registres/go.md (ligne GO-2026-11-21-66, l. 665) | 630ee5ab9d8a6b1bcd4fb7e9c9d33fc9ce8e50cfa5bd6216865a00377fc66e81 | non fournie |
| consigne commune | docs/procedures/consigne-commune-methode-de-recherche-v1.md | d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8 | identique |

Contrôles préalables :
- Extraction à l'octet : lignes 598 à 625 de la source et lignes 13 à 40 du projet écrites en fichiers par `sed -n 'a,bw fichier'`, puis `cmp` : aucune différence.
- Citation de la pièce scellée (projet l. 19) : la phrase citée se trouve mot pour mot dans la ligne 30 de la pièce scellée (`grep -c -F` rend 1).
- Accord : GO-2026-11-21-66 porte « Organisme : tolérance des réseaux 0,02 « go reco » (note d'écart à sceller) » ; la recommandation du § 6.5 de la source est l'option (b). L'accord couvre la valeur 0,02 et la forme de la note ; il ne dispense pas des corrections de lettre ci-dessous, qui ne changent ni la valeur ni la forme.

## Les cinq modes d'échec affectés

| mode | issue | passage visé | preuve |
|---|---|---|---|
| (1) convertir un saboteur dont le décalage ne réalise pas une aire atteignable qui encadre l'aire dite | **Tenu sur la règle, à corriger dans la lettre** | l. 24 (condition 1), l. 27 (« Le saboteur de la famille est alors converti ») | La condition 1 exige l'égalité à 10⁻⁹ près avec v_sous ou v_sur : le voisin suivant, même à 0,0129 de 0,69, est refusé (FAUX 1). Mais la l. 27 attache la conversion de la famille à la réception d'un décalage, non de chacun ; la l. 28 dit l'inverse pour le décalage qui échoue. Sur FAUX 5 (0,69 reçu au pas du réseau, 0,80 un palier trop loin), la lecture conjointe ne convertit pas, la lecture isolée de la l. 27 convertirait. Le § 6.2, point 3, de la source dit « La famille est conforme si chaque couple (tranche, aire) est (a) ou (a bis) » ; cette phrase manque à la note. Correction : l. 27, « Si chaque décalage de la famille, dans chaque tranche, est conforme à 0,005 ou reçu ainsi, le saboteur de la famille est converti ». |
| (2) s'appliquer à une famille dont la loi honnête n'est pas arrondie | **Tenu, à préciser** | l. 23 (« Pour une famille dont la loi honnête de la tranche est arrondie, et pour elle seule ») ; l. 32 | Sur une loi continue, toute aire de [0, 1] est atteignable, donc v_sous = v_sur = aire dite et la condition 1 exige l'égalité à 10⁻⁹ près, plus stricte que 0,005 : appliquée par erreur à une loi continue, la règle ne convertit rien de plus (FAUX 4, aires dites + 0,01 : trois refus ; VRAI 2 : trois (a), la note n'intervient pas). Reste que « arrondie » n'est défini nulle part (pas d'arrondi déclaré par l'auteur ? loi à valeurs sur un réseau, ce qui prendrait aussi une loi de comptage ?), et que « de la tranche » et « famille » mêlent deux portées. Correction : « dont la loi honnête de la tranche, telle que l'auteur l'écrit, est une loi continue arrondie à un pas déclaré ; la règle s'applique tranche par tranche ». |
| (3) laisser un cas non converti sans le rapporter, ou un cas converti sans le compter et le nommer | **Converti : tenu. Non converti : rapporté, mais nommage cassé** | l. 27 (compte et nom), l. 28 (deux raisons) | Converti : « Chaque cas est compté et nommé « conforme au pas du réseau », avec le chemin du décalage, le rang de la tranche, les deux aires atteignables et l'aire réalisée » ; le compte de tout écart de plus de 0,001 reste (l. 32). Non converti : le rapport est dû par la lettre scellée, laissée en vigueur (l. 15). Mais la l. 28 se donne pour exhaustive et ne l'est pas : FAUX 3 (pas 0,5, aire dite 0,69, l'auteur réalise v_sous = 0,6355, à 0,0545, alors que v_sur = 0,7011 est à 0,0111) n'est ni « aucune aire atteignable à 0,02 » (v_sur l'est) ni « une autre aire » (il réalise une aire encadrante) ; la définition de « aucune unité ne réalise les aires » au § 6.2, point 6, de la source (« les nombres de l'auteur manquent une aire atteignable ») ne le couvre pas non plus. Le programme devra inventer une raison, ou n'en mettre aucune. C'est précisément la conduite « première aire au-dessous » que la source dit raisonnable (§ 6.3, point 1). Correction : ajouter la raison « aire encadrante hors du plafond de 0,02 », ou rendre la l. 28 exhaustive par construction (« dans tout autre cas, … sous l'une des raisons : … »). La condition 3 (ordre) n'a pas de raison nommée non plus, mais elle ne peut jamais échouer seule (pas 4). |
| (4) toucher autre chose que l'alinéa « Unité des décalages du saboteur » | **Tenu, une réserve** | l. 15, l. 19, l. 32, l. 40 | La note cite l'alinéa mot pour mot, déclare l'écart « sur un point et un seul », garde 0,005 pour les lois continues, le compte au-delà de 0,001, l'unité en écarts types, et ne change ni hypothèse, ni revendication, ni critère de lecture. Ce qu'elle ajoute hors de la règle même (obligation de dire « à 0,02 près » dans tout rapport, empreinte exigée par le programme) est une conséquence de l'écart, non un changement d'une autre pièce. Réserve : la l. 27 fixe que « la valeur vraie de ses témoins se calcule sur la loi et le décalage réels » ; je n'ai pas lu le programme v4 pour vérifier que c'est déjà ainsi pour l'issue (a) (supposé, sur la foi du § 6.2 de la source, « convertis comme pour (a) »). Divergence inverse, à signaler au développeur : la règle (§ 6.2, point 5) applique (a bis) aussi « sous l'unité brute » ; la note ne l'autorise pas (l. 32 : lecture en écarts types inchangée). Le programme doit suivre la note, non la règle. |
| (5) dépendre d'une lecture de la sortie de l'auteur des mondes | **Tenu** | l. 36, l. 40 | Les paramètres de l'écart (encadrement, plafond 0,02, 10⁻⁹) se déduisent des trois aires dites et d'une illustration sur une loi choisie par le concepteur (`aires-reseau-illustration-v1.txt`, 8858cbb5…) ; aucun ne renvoie à un nombre de l'auteur. La l. 40 interdit le scellement après une lecture. Remarque : l'absence de lecture est déclarée, non attestée ; la note gagnerait une ligne remplie au scellement (« sortie de l'auteur à @HEURE@ : absente, ou présente non lue, empreinte … »). |

## Épreuve de la règle sur un réseau factice

Programme : `epreuve_regle_note_ecart_v2.py` (663071ec8963a08e78b51daf08145ecdca441db7e9556d901d7aa8937666fd29), sortie `sortie-epreuve-v2.txt` (c295f6c746757e05c32e212024fa891fbf8e5f223c1a74c81fafc5caab88ce63) ; première version `epreuve_regle_note_ecart_v1.py` (af0df0b8b36ce130d18b9b2bd2b7d73435527339834b33a220350a7326d6613d), sortie `sortie-epreuve-v1.txt` (3957eda1d729428331b923ebc65ec0b39fccc1c17733dac7ac7920ef0eee94a1), gardées intactes, dans mon dossier. Commande : `python3 -I epreuve_regle_note_ecart_v2.py`. Loi factice : normale réduite arrondie au pas h, aire = P(S > H) + ½ P(S = H), décalage lu en écarts types de la loi arrondie ; la règle est codée à la lettre des l. 23 à 28, la lettre scellée valant ailleurs. Flottants, de ma main : non opposable.

Prédictions écrites dans le programme avant la première exécution, résultats :

| objet | construit | prédit | rendu |
|---|---|---|---|
| VRAI 1 : pas 0,25, l'auteur prend l'aire atteignable la plus proche | vrai | 0,69 et 0,80 « conforme au pas du réseau », 0,95 en (a) ou (a bis), famille convertie | 0,7011 et 0,8104 au pas du réseau, 0,9532 en (a), famille convertie. Conforme. |
| VRAI 2 : loi continue, décalages exacts | vrai | trois (a), la note n'intervient pas | trois (a). Conforme. |
| FAUX 1 : pas 0,1, voisin suivant non encadrant (0,6771, à 0,0129 de 0,69) | faux | 0,69 refusé, « aucune unité ne réalise les aires » | refusé sous cette raison ; famille non convertie. Conforme : le plafond seul ne suffit pas, la condition 1 mord. |
| FAUX 2 (v1) | **mal construit par moi** | trois refus | trois reçus. Constat : j'avais passé des nombres déjà justes en écarts types (pas 0,25 ET, décalages de la loi continue) : c'était un objet vrai, et la règle a eu raison de le recevoir (0,6705, à 0,0195 de 0,69, comme la source le dit au § 6.3, point 2). Erreur de construction, non de la règle ; corrigée en v2 sous un nom neuf. |
| FAUX 2 bis : nombres écrits en unité brute (écart type ≈ 2), lus en écarts types | faux | trois refus | 0,8342, 0,9532, 0,9995 : trois refus, « aucune unité ne réalise les aires ». Conforme. À noter : 0,9532 est l'aire encadrante de 0,95, refusée parce qu'elle est confrontée à 0,80 : la règle compare bien à l'aire dite du rang. |
| FAUX 3 : pas 0,5, v_sous de 0,69 réalisée (0,6355, hors plafond), v_sur à 0,0111 | faux | refus, et aucune des deux raisons de la l. 28 | refus, et le programme tombe dans la branche « aucune des deux raisons ». Conforme à ma prédiction : trou de nommage (mode 3). |
| FAUX 4 : loi continue, aires dites + 0,01 | faux | trois refus, la note n'ajoute rien | trois refus par la lettre scellée. Conforme (mode 2). |
| FAUX 5 : pas 0,25, 0,69 au pas du réseau, 0,80 un palier trop loin | faux | lecture conjointe : non convertie ; lecture isolée de la l. 27 : convertie | les deux, comme prédit. Conforme : l'ambiguïté de la l. 27 est réelle (mode 1). |

Le réseau factice retrouve les aires encadrantes que la source donne (pas 0,25 : 0,6705, 0,7011, 0,7865, 0,8104 ; pas 0,5 : 0,7557, 0,8104 ; pas 1 : 0,7430 encadre 0,69 et 0,80) : recoupement non opposable d'un calcul non opposable.

## Corrections demandées (lettre seulement ; ni la valeur 0,02 ni la forme ne changent)

1. l. 27 : conditionner la conversion à **chaque** décalage de la famille, dans chaque tranche (reprendre la phrase du § 6.2, point 3, de la source).
2. l. 28 : rendre les raisons exhaustives ; ajouter « aire encadrante réalisée hors du plafond de 0,02 » (cas FAUX 3), et une raison pour l'ordre si la condition 3 est gardée.
3. l. 23 : définir « arrondie » et la portée (tranche par tranche).
4. Conseillé : l. 40, une ligne d'attestation d'absence de lecture, remplie au scellement.
5. Conseillé : la condition 3 est redondante (pas 4) ; la garder ne nuit pas, mais la dire « garde de cohérence, ne peut échouer seule ».

## Relevé de méthode

### Chaîne de raisonnement

1. Les six pièces sont celles qu'on m'a nommées, aux empreintes attendues quand elles étaient données (table des pièces, `sha256sum`).
2. Le texte du projet (l. 13 à 40) est la source l. 598 à 625 à l'octet (`cmp`, aucune sortie).
3. La l. 19 cite la pièce scellée mot pour mot (`grep -c -F` sur la pièce scellée, dfe0aace…, rend 1).
4. Sous la condition 2, les trois aires réalisées d'une tranche sont automatiquement strictement croissantes : 0,69 + 0,02 = 0,71 < 0,78 = 0,80 − 0,02 et 0,82 < 0,93 = 0,95 − 0,02 ; une aire conforme à 0,005 est a fortiori dans ces fenêtres. Donc la condition 3 ne peut échouer que si une autre condition échoue déjà (calcul rejouable à la main).
5. La condition 1 refuse un voisin non encadrant même sous le plafond (FAUX 1, sortie-epreuve-v2.txt, c295f6c7…) ; donc une aire non encadrante n'est jamais reçue décalage par décalage (mode 1, côté règle).
6. La l. 27 lie la conversion de la famille à un décalage reçu ; la l. 28 la refuse pour un décalage qui échoue ; sans « chaque », un programme peut suivre l'une ou l'autre (FAUX 5, même sortie) ; le § 6.2, point 3, de la source (4521273…, l. 551) contient la condition manquante (mode 1, côté lettre).
7. Sur une loi continue, l'ensemble atteignable est [0, 1], donc v_sous = v_sur = aire dite et la condition 1 devient plus stricte que 0,005 (raisonnement ; FAUX 4 et VRAI 2, même sortie) ; donc une application à tort à une loi continue ne convertit rien de plus (mode 2).
8. « Arrondie » n'est défini ni dans le projet (l. 23 à 40), ni dans la règle (3806ff34…, l. 13 à 23), ni dans l'alinéa scellé (dfe0aace…, l. 30) (lecture des trois).
9. La l. 28 donne deux raisons ; FAUX 3 (pas 0,5) n'en remplit aucune (même sortie) ; le rapport reste dû par la lettre scellée laissée en vigueur (projet l. 15) ; donc le cas est rapporté mais sans raison définie (mode 3).
10. La l. 27 nomme et compte chaque cas converti avec cinq champs ; la l. 32 garde le compte au-delà de 0,001 (lecture) ; donc tout cas converti est compté et nommé (mode 3).
11. Le projet ne cite que l'alinéa l. 30 de la pièce scellée et ne modifie aucune autre pièce nommée dans sa table (pas 3 ; lecture du projet en entier) ; la règle (3806ff34…, l. 19) étend (a bis) à l'unité brute, ce que le projet n'accorde pas (l. 32) (mode 4).
12. Aucun nombre du projet ne vient de l'auteur : 0,69, 0,80, 0,95 sont les aires dites ; 0,02 et 10⁻⁹ sont posés ; l'illustration est sur une loi du concepteur (source § 6.1, l. 543) ; la l. 40 interdit le scellement après lecture (mode 5).
13. L'accord de Lazar pour l'option (b) existe (registres/go.md, 630ee5ab…, l. 665).
14. Les défauts des pas 6 et 9 sont de lettre et se corrigent sans changer la valeur ni la forme accordées ; ils rendent la note ambiguë pour le programme qui l'appliquera : verdict « À corriger », non « Cassé ».

### Objets de contrôle

Mécanisme éprouvé : la règle de la note (l. 23 à 28), codée à la lettre. Objets vrais par construction : VRAI 1 (pas 0,25, aire atteignable la plus proche ; prédit : reçu, famille convertie ; rendu : reçu, convertie) et VRAI 2 (loi continue, décalages exacts ; prédit : trois (a) ; rendu : trois (a)). Objets faux par construction : FAUX 1, FAUX 2 bis, FAUX 3, FAUX 4, FAUX 5 (prédits et rendus dans la table de l'épreuve, tous conformes à la prédiction). Un objet faux de la v1 (FAUX 2) était mal construit par moi ; la règle l'a reçu à bon droit ; je le garde, rapporté, et le remplace en v2 sous un nom neuf. Aucun objet faux n'a été reçu par la règle lue conjointement ; FAUX 5 est reçu par la lecture isolée de la l. 27, ce qui fonde la correction 1.

### Premier pas non justifié

Le premier pas non entièrement justifié est le **pas 11**, pour sa moitié « la valeur vraie des témoins convertis se calcule déjà sur la loi et le décalage réels pour l'issue (a) » : je ne l'ai pas lu dans le programme v4 (rapport f135edc6…, non dans ma liste). Ce qui le justifierait : la lecture du passage du rapport v4 qui définit la valeur vraie d'un témoin converti. Par ailleurs, l'épreuve suppose une forme d'aire (P(S > H) + ½ P(S = H), S = H' + d) que je n'ai pas lue dans le texte servi (supposé, d'après « aires de palier et de saut, les ex æquo comptés pour moitié », l. 24, et le § 6.1 de la source).

### Mode d'échec affecté

Les cinq modes de mon mandat : (1) tenu sur la règle, lettre à corriger (l. 27) ; (2) tenu, à préciser (l. 23) ; (3) converti tenu, non converti rapporté mais nommage cassé (l. 28) ; (4) tenu, réserve (l. 27, valeur vraie ; divergence règle-note sur l'unité brute) ; (5) tenu (l. 40). Preuves : table des modes et table de l'épreuve.

### Dérivation de l'énoncé seul

Sans objet : je suis relecteur, non agent de re-dérivation.

### Trouvaille de côté

- La règle (pieces-v2, 3806ff34…, l. 19) est plus large que la note (unité brute) : le programme v6 doit être écrit sur la note scellée, non sur la règle, sinon il convertirait sous une lecture que la note n'accorde pas.
- Si le saboteur de l'auteur n'est pas une simple translation de la loi honnête (par exemple un arrondi appliqué après le décalage), l'ensemble « palier et saut » ne décrit plus les aires atteignables ; la règle reste prudente (égalité à 10⁻⁹ improbable), mais le programme devrait le constater et le dire plutôt que calculer un encadrement faux.
- Mon propre FAUX 2 (v1) mal construit montre que l'artefact « unité brute » du § 6.3, point 4, de la source se construit facilement à l'envers ; l'épreuve du programme v6 devrait l'écrire avec le facteur d'écart type explicite.

### Évaluateur et conseil

Ce qui juge cette contre-lecture : la session mère, puis le scellement par elle et le mot de Lazar déjà donné (GO-2026-11-21-66). Ce qui jugeait la règle ici : mon programme d'épreuve, admis sur deux objets vrais et cinq faux, de ma main, non contre-lu ; il code ma lecture de la lettre, donc il ne peut pas voir une erreur que je partage avec l'auteur sur la forme de l'aire. Par où ce rendu pourrait obtenir un bon jugement sans le mériter : un réseau factice d'une seule famille (normale arrondie) qui recoupe les nombres de la source, ce qui conforte sans prouver ; et des modes « tenu » appuyés sur la lettre scellée laissée en vigueur, qu'un programme peut ignorer s'il n'est écrit que sur la note. Conseil : faire porter les corrections 1 et 2 dans les épreuves de mutation du programme v6 (famille mixte comme FAUX 5 ; aire encadrante hors plafond comme FAUX 3), avec une raison nommée attendue pour chacune.
