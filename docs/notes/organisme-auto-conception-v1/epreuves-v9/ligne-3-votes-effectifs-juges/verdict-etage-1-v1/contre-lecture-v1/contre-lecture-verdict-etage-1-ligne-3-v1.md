# Contre-lecture du verdict de l'étage 1 de la ligne 3 — v1

Contre-lecteur, modèle F, agent neuf : je n'ai écrit ni le préenregistrement, ni les additifs, ni le code, ni l'aide, ni le verdict, ni le relevé. Écrite le 2026-11-20, sur le mandat `mandat-contre-lecteur-verdict-etage-1-ligne-3-v1.md` (`80ea3839e5ae7f3fbc8532ade88ba0902949cf6c65583caf7bb85d46b1c24184`, vérifiée contre son compagnon avant tout autre geste).

## Verdict de la contre-lecture

**« À corriger » — cinq corrections de texte, dont aucune ne change le mot, la taille, la table ni la puissance.**

Le fond du verdict est **rejoué égal** : mon programme, écrit sans avoir lu ni le verdict ni le programme de l'agent du verdict, rend les mêmes résultats sur **83 champs comparés, 0 désaccord**. Le mot **« non, pas à cette taille »** (PR l. 314) est le bon ; la taille voulue est **200 témoins** ; la puissance qui décide vaut **0,160**, sous 0,5 ; aucune dépense ; la ligne à 25 USD ne part pas.

## 1. Pièces et empreintes vérifiées

Textes tirés de main (`git fetch origin main`, tête `835ee84a021c50610ea104aaa4ee0def52e859a8`, puis `git show` redirigé vers mon dossier), empreintes recalculées égales au mandat : PR `4e3680d9…d5a0` ; A1 `e1c1ee84…08b0` ; A2 `f5562d20…f25a` ; DV `382ea448…8270`. PR, A1 et A2 lus en entier ; du DV, seules les lignes 9, 124 et 172, pour vérifier les renvois du verdict.

Mesures : `resultat-etage-1-ligne-3-v3.json`, `eb7a673bc9612458f4c86cf817ef60e58c8118772934c52fbdba18cc4f3c60ce`, égale.

Pièces du verdict, recalculées égales : verdict `7da76ed4…8574` ; critères `7f28eefb249ec6e02b2848953d2d4524e0c8e235f8c2c99835cd9da68065ec38` ; programme `6ad1cfca38ed1412135b9c47d39edb611ce637865eee26bb0136495fb3e5b1c7` ; contrôles `ca4a3dc9391eeff8201ef3f0ac70f7ef5ae62856eb4bfbaefeb65b9d5fd32090` ; application `072f39772627b9869ca174ef934d00a80d4dc46efe3950be709dbe425458eb6d` ; comparaison à l'aide `d8130e45f05e0597776b02b9cb786fcb8932230a59ac16d294fcae4b08222af9`.

Non relus : les manifestes de l'exécution (leur contrôle est le geste de la mère, A2 l. 126, 137, 138) ; les autres pièces du dossier du verdict (résumés, inventaires, extraction de l'aide).

## 2. Les critères : ma liste contre `criteres-appliques-v1.md`

Ma liste (`criteres-contre-lecteur-v1.md`) a été écrite et scellée par son compagnon avant que j'ouvre aucune pièce du verdict et aucune mesure.

- **Aucun critère manquant qui porte le mot** : contrôles avant lecture, tolérance, cellules de la règle, table gelée, règle E, table « plus petit n », règle de portée, ce qui est rendu, lectures descriptives, audit « trop propre » : les deux listes ont les mêmes critères, aux mêmes lignes.
- **Aucun critère en trop.**
- **Citations** : les treize citations entre guillemets que j'ai recollées au texte (A2 l. 104 ; PR l. 134, 177, 232, 233, 240, 241, 309, 316, 318 ; A1 l. 81, 84, 131) sont exactes, à la mise en gras près. DV l. 172 dit bien ce que le verdict lui prête.
- **Un manque, de second rang** : PR l. 318 demande la lecture descriptive « contre les prédictions P3 à P6 ». La liste de l'agent du verdict cite cette phrase, mais ni la liste ni le verdict ne lisent P3, P4 et P5 contre leur clause de réfutation, et le verdict ne dit pas qu'il ne les lit pas, alors que sa liste promet : « ce qui n'est pas appliqué est dit ». Correction 4.
- Ma liste porte en plus A1 l. 118 et A2 l. 146 (l'aide n'est jamais le verdict) ; le verdict s'y conforme (§ 6 du verdict).

## 3. Rejeu par mon programme

Ordre tenu : (1) un relevé de structure qui n'imprime **que des noms de clés et des types, aucune valeur** ; (2) les contrôles avant lecture ; (3) le rejeu, qui refuse de tourner si les contrôles ne tiennent pas ; (4) la comparaison au verdict ; (5) seulement alors, la lecture du programme et des sorties de l'agent du verdict. Bibliothèque standard, aucun tirage, aucun code en ligne ; je n'ai pas exécuté le programme de l'agent du verdict.

**Contrôles avant lecture, tous tenus.** Mélange planté : 1 000, 500, 500, 1 000 sur 2 000 suites, à m = 10, 20 et 40. P2 : 248 cellules à deux juges égaux et symétriques, écart maximal 0,00543 (loi 1, taux 0,30, ρ = 0,3, n = 50), aucune hors de ± 0,02 ni de ± 0,01. Part d'abstentions à δ = 0 : au pire à 0,0011 de 0,1275.

**Tolérance aux treize cellules de la règle.**

| n | 50 | 100 | 200 | 400 |
|---|---|---|---|---|
| cellules qui tiennent, sur 13 | 0 | 5 | 13 | 13 |

À n = 100, huit cellules manquent, toutes par la seule erreur quadratique moyenne (loi 1 et loi 3, ρ = 0,15 ; 0,3 ; 0,45 ; 0,6 ; de 0,1018 à 0,1167). Les quatre tolérances recalculées par moi sont égales au drapeau du code dans les 780 cellules-tailles.

**Solidité au bruit de 2 000 répliques** (erreur type approchée de l'erreur quadratique : sa valeur divisée par √(2 × 2 000), approximation normale, dite). À n = 100, les deux cellules à ρ = 0,6 ne dépassent que de 1,1 et 1,3 erreur type, mais les six autres dépassent de 5,9 à 9,1 erreurs types : « ne tient pas à 100 » ne tient pas au bruit. À n = 200, la plus haute erreur quadratique (0,0806) est à une quinzaine d'erreurs types sous la borne.

**Mot de la table gelée** : deuxième ligne, « non, pas à cette taille ». **Taille** : N = 100 n'est pas retenu ; taille voulue 200. **Monotonie** : issue monotone sur la règle (non, non, oui, oui) ; aucune des 195 cellules de la grille ne tient à un n pour manquer à un n plus grand ; l'audit de non-monotonie d'A1 l. 84 n'a pas à partir. **Audit « trop propre »** (PR l. 348) : aucune cellule à couverture 1.

**Table « plus petit n »** : les 195 cellules égales à celles du verdict, et à l'aide.

**Puissance qui décide** (écart 0,10, lois 1 et 3, 16 puissances sur les cellules faisables) : 0,160 (contre l'unanimité, loi 3, ρ = 0). Par comparaison : unanimité 0,160 ; juge 1 seul 0,4685 ; juge 2 seul 0,445 ; juge répété 0,476. Comptes de cellules faisables égaux à PR l. 238 (4 et 2 ; 2 et 1 ; 2 et 2). Hors du bras R, ρ′ = 0 partout. Écart vrai par formule : 0,1 dans chaque cellule. La règle de portée se déclenche ; la clause de réfutation de P10 (0,5 ou plus) n'est pas atteinte.

**Lectures descriptives**, toutes égales au verdict : puissance de « positif » de ρ′ − ρ (15 cellules faisables ; 0,130 à 0,6555 ; 0,3285 à 0,824 ; 0,8065 à 0,9955) ; `fa38f9faa24e0` (997 et 251 ; 654, 432 et 6) ; branche (2) (60, 41, 11 et 3 cellules réfutées ; aucune taille) ; branche (3), les dix mots du sens (a) ; `fcfa3d98b90f8`, les 36 cellules, clauses (i) et (iii) et mot ; alarme (34, 53, 112 sur 1 000 ; 215/15, 348/17, 448/21) ; P6 réfutée par la seule fausse alarme à m = 40.

**En plus du verdict, lu par moi contre les clauses de réfutation** (lectures du contre-lecteur, descriptives) : P1 non réfutée (à n = 50 et taux 0,10, aucune des sept cellules de la loi 1 ne tient ; à n = 400 et taux 0,20, toutes tiennent) — sa prédiction « à la limite à n = 100 pour un taux de 0,20 » n'est, elle, pas tenue aux treize cellules ; P4 non réfutée (plus grand gain du bras N sur la majorité fixe à ρ ≥ 0,6 : 0,0103, sous 0,02) ; P5 bis non réfutée ; mots de P5 quater retrouvés (« réfuté » à δ = 0 et 0,2, « tient » à δ = 0,5 ; clause (iii) « sans prise », « tient », « tient »). **P3 : lecture non tranchée par moi.** Juges échangeables : aucun gain du bras C sur la majorité fixe (au mieux −0,0002), clause non atteinte. En blocs, à 200 témoins d'étalonnage et ρ ≥ 0,6 : le bras C fait moins bien que la majorité fixe dans les douze cellules à taux égaux (−0,005 à −0,012) et un peu mieux dans cinq des six cellules dissymétriques (au plus +0,009) ; « aucun gain en blocs » dépend de la référence et du bras que l'on prend pour « l'agrégation étalonnée », que la clause ne nomme pas. Les clauses de réfutation de P5, P5 ter et P5 quater ne sont pas rejouées par moi.

## 4. Désaccords, et leur levée

**Aucun désaccord de valeur, de mot ni de table.** Après comparaison, j'ai lu `appliquer_criteres_etage_1_v1.py` en entier : il retire `criteres_mecaniques` au chargement, recalcule chaque mot à partir des grandeurs mesurées, et ne relit les drapeaux du code que pour compter les accords. Sa logique est la même que la mienne, critère par critère ; seule différence, sans effet ici : il compare sans tolérance d'arrondi là où j'en mets une de 1e-12 (aucune valeur n'est à une borne). `comparaison-a-l-aide-v1.json` : liste des désaccords vide, ce que je retrouve de mon côté.

Deux écarts de **texte** entre le verdict et les mesures, levés par les corrections 1 à 3 :

- Le verdict écrit que la cellule loi 3, ρ = 0, n = 100 est « à la borne, inclusive ». Elle vaut **0,09999728** : elle est sous la borne, et l'inclusion de la borne ne joue nulle part (aucune des 780 cellules-tailles n'a une valeur à moins de 1e-9 d'une borne).
- Le verdict écrit « taille retenue par la règle : 200 ». À la lettre de PR l. 233, la règle ne retient que N = 100 ou rien ; 200 est « la taille voulue ». Le fond est juste, le mot prête à confusion avec une taille autorisée.

## 5. Corrections demandées (texte exact)

1. **§ 2, phrase « Tiennent à n = 100 »** — remplacer « loi 3 à ρ = 0 (0,1000, à la borne, inclusive), 0,75 » par : « loi 3 à ρ = 0 (0,09999728, sous la borne de 0,10 ; 0,1000 à l'arrondi), 0,75 ».
2. **§ 8, point 4** — remplacer « la cellule loi 3, ρ = 0, n = 100 est à 0,1000 (tient, à la borne) ; cela ne change pas le verdict (huit autres cellules manquent à 100) » par : « la cellule loi 3, ρ = 0, n = 100 est à 0,09999728, sous la borne : elle tient sans que l'inclusion joue ; aucune valeur de la grille n'est exactement à une borne ».
3. **§ 2, ligne « Taille retenue »** — remplacer par : « **Taille voulue : 200 témoins** (le plus petit n de la grille où la tolérance tient aux treize cellules ; elle tient aussi à 400). La règle gelée ne retient pas N = 100 : aucune dépense sous ce texte (PR l. 233). »
4. **§ 5, ajouter une puce** : « **Prédictions** (PR l. 318). P1 : aucune de ses deux clauses de réfutation n'est atteinte ; sa prédiction « à la limite à n = 100 pour un taux de 0,20 » n'est pas tenue aux treize cellules. P4 : non réfutée (plus grand gain du bras N sur la majorité fixe à ρ ≥ 0,6 : 0,0103). P5 bis : non réfutée (branche (3) ci-dessus). P6 : réfutée (ci-dessous). P10 : sa clause de réfutation (puissance qui décide de 0,5 ou plus) n'est pas atteinte. P3, P5, P5 ter et P5 quater : non lues contre leur clause de réfutation dans ce verdict. » L'agent du verdict peut, à la place de la dernière phrase, lire ces quatre prédictions lui-même ; ce qu'il ne lit pas doit être dit.
5. **§ 4, paragraphe « La règle de portée s'applique », et § 7, point 2** — ajouter, au § 4, après « par un additif scellé » : « à la lettre, pour l'étage 2 à 100 témoins que ce texte prévoit, et qui ne part pas » ; et remplacer le point 2 du § 7 par : « **Cas non prévu** : la règle de portée est mesurée à n = 100 (PR l. 232, 236), et la taille voulue est 200. Le texte ne dit pas si la portée se relit à 200 témoins, ni si l'additif de portée se scelle sur la puissance à 100 ; aucune puissance n'est mesurée à 200, et l'étage 1 ne se rejoue pas (A1 l. 85). Plus largement, le texte ne prévoit d'étage 2 que sur un « oui » (PR l. 331, 378) : un étage 2 à 200 témoins — banque, plan d'appels, seuil de 40 témoins complets, cellule de stabilité, portée — n'est pas écrit par ce préenregistrement. À trancher par Lazar avec le devis. »

Les corrections 1 et 2 sont des faits à redresser. Les corrections 3 à 5 sont des précisions ; je les tiens pour nécessaires dans une pièce de classe A que Lazar lira pour décider.

## 6. Jugement des points ouverts

**(a) La puissance de la règle de portée est mesurée à n = 100, la taille voulue est 200 : le texte le tranche-t-il ?**

Le texte tranche trois choses, et pas la quatrième.

- Il tranche **où** la puissance se lit : à n = 100 (PR l. 232 : « à n = 100 et à J = 2 » ; l. 236 : « n = 100, moitié étalonnage, moitié lecture »). La puissance qui décide est donc bien 0,160, et la règle se déclenche à la lettre (PR l. 240). Le geste (5) demande l'« application des deux règles gelées » (PR l. 305) : le verdict a raison de l'appliquer.
- Il tranche **l'effet de la taille** : pas de dépense, devis neuf à Lazar, la ligne à 25 USD ne part pas (PR l. 233, 241, 314).
- Il tranche que **l'étage 2 n'existe que sur un « oui »** (PR l. 331, 378).
- Il **ne dit pas** ce que vaut la règle de portée pour un étage 2 à 200 témoins : ni relecture, ni additif de portée « s'il y a lieu » quand la dépense n'a pas lieu. Aucune mesure à 200 n'existe, et en produire une serait une expérience neuve, sous préenregistrement (règle R1), l'étage 1 ne se rejouant pas (A1 l. 85).

**Donc : non, le texte ne le tranche pas, et c'est un point pour Lazar.** Il relève de deux nœuds de la hiérarchie de décision : écart à un préenregistrement scellé, et dépense sur devis. L'agent du verdict a eu raison de ne pas trancher. Je ne dis rien du sens qu'aurait la puissance à 200 : elle n'est pas mesurée.

**(b) Les trois écarts déclarés au § 8 vident-ils le verdict ? Non, aucun.**

1. *Première commande de liste et commande enchaînée.* C'est un manquement à l'en-tête du mandat, réel, à garder déclaré. Il n'a touché que des noms de fichiers du dossier d'exécution, selon ce que l'agent déclare ; je ne l'ai pas vérifié. Il n'a aucune prise sur les critères ni sur les mesures.
2. *Une cellule de chaque bloc affichée avant les contrôles.* C'est l'écart le plus sérieux : l'ordre « contrôles avant lecture » sert à rendre un banc fautif sans l'avoir lu (A2 l. 104 ; PR l. 316). Il ne vide pas le verdict, pour trois raisons : les contrôles ont tenu, donc le cas que l'ordre protège ne s'est pas présenté ; les critères sont mécaniques et ne laissent aucun choix après lecture ; et mon rejeu, fait **sans cet écart** (aucune valeur affichée avant mes contrôles), rend les mêmes 83 champs. La contre-lecture couvre donc ce que l'écart aurait pu fragiliser. Limite : je ne peux pas vérifier par moi-même l'heure à laquelle `criteres-appliques-v1.md` a été écrit ; je constate seulement qu'il est égal, au fond, à ma liste tirée des textes seuls.
3. *Les blocs de mesures portent des mots et des drapeaux du code.* Ce n'est pas un écart de l'agent mais un fait du fichier de résultat. Son programme ne s'en sert pas pour décider (lu, § 4) ; le mien non plus. À savoir pour la suite : un lecteur du résultat ne peut pas ouvrir les mesures sans voir ces mots.

**(c) Ce qui revient à Lazar, selon les textes.**

1. **La table et un devis neuf à 200 témoins** (PR l. 233, 241, 314 ; DV l. 9, 172 : cas haut 44,78 USD, pire 88,36 USD, relus au DV l. 124). Le verdict le dit bien.
2. **Le cas non prévu de la portée**, au (a). Le verdict le dit ; la correction 5 le complète : c'est tout l'étage 2 à 200 témoins que le texte n'écrit pas, pas seulement la portée.
3. **Le nœud 2 de l'additif 1** (A1 l. 105) : aucune règle de mot gelée pour la carte de l'alarme ; en écrire une est un critère neuf. Le verdict ne le rappelle pas au § 7 ; ce n'est pas une suite de l'étage 1, mais il reste ouvert. Le nœud 1 (ligne manquante de la table pour « n = 50 seul ») est sans objet ici, comme le verdict le dit.
4. Rien d'autre : rapporter les votes effectifs à chaque course, changer d'agrégation ou de juges restent des décisions de Lazar (PR l. 345), qu'aucun résultat de l'étage 1 ne déclenche. Aucune carte n'est tranchée.

Pour la mère, non pour Lazar : le contrôle des manifestes (A2 l. 137, 138), que ni l'agent du verdict ni moi n'avons refait ; et la décision 1 de GO-2026-11-19-77, dont la première condition (lecture de l'étage 1 faite) est maintenant remplie.

## 7. Mes écarts et limites

- Aucun refus de permission, de classifieur ni de garde. Aucune commande de liste, une commande simple par appel, aucun code en ligne, aucun appel de modèle, aucune dépense, aucun lancement du banc ni du chronométrage, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`.
- `git fetch origin main`, demandé par le mandat, a écrit `FETCH_HEAD` dans le dossier `.git` du dépôt ; aucun fichier suivi n'a été touché, aucun commit.
- Les erreurs types que je donne sont des approximations, dites ; elles ne servent à aucun critère.
- Mes lectures de P1, P3 et P4 sont celles du contre-lecteur, non contre-lues.
- Je n'ai pas relu le code du banc : je rejoue les critères sur les mesures, je ne certifie pas les mesures.

## 8. Mes pièces (dossier `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-verdict-etage-1-ligne-3-v1/`, chacune avec son compagnon `.sha256`)

`criteres-contre-lecteur-v1.md` ; `structure_mesures_v1.py` et `structure-mesures-v1.txt` ; `controles_avant_lecture_contre_lecteur_v1.py` et `controles-avant-lecture-contre-lecteur-v1.json` ; `rejouer_criteres_contre_lecteur_v1.py` et `rejeu-criteres-contre-lecteur-v1.json` ; `details_pour_comparaison_contre_lecteur_v1.py` et `details-pour-comparaison-contre-lecteur-v1.txt` ; `comparer_au_verdict_contre_lecteur_v1.py` et `comparaison-au-verdict-contre-lecteur-v1.json` ; cette pièce. Les copies des quatre textes (`PR.md`, `A1.md`, `A2.md`, `DV.md`) y sont aussi, aux empreintes du § 1.

Contre-lecteur, modèle F.
