# Vérification des corrections de la batterie de fuite (v3) — mathématiques nouvelles — v1

- Vérificateur : Opus 5.5, session neuve, auteur d'aucune des pièces lues (ni la batterie, ni la réponse, ni la première contre-lecture). Le 2026-11-23. Processeur seul, aucun appel de modèle, aucune dépense. Règles appliquées : R1, R2, R4, R5, R6 (CLAUDE.md, « Règles gelées »), classe A de « Allègement ».
- Pièces vérifiées : `batterie-fuite-banque-revisee-v3.md` (`78556fc53a4f66e945579aa6321e58a4252ed1a90ef81cf3e7f2b58d6c80c08c`) et `reponse-contre-lecture-batterie-v1.md` (`106d5dc35c21a0db9bdfe7cd2c0fd2774ec3fa5e590b99b6e01f6b43bc190af0`), contre la v2 (`6b02a1c8…`) et la première contre-lecture (`9718ec04…`). Branche `claude/mathematiques-nouvelles-v1`, commit `3ea5b83a`.
- Cloisonnement : aucun fichier de clé ni banque réelle ouverts. Racines employées : 1000 à 1119 (banc d'épreuve) ; 0 à 39 et 20261122 (version 6, racines d'essai déjà exposées). Aucune autre racine du générateur. La clé de sous-banque des racines d'essai est restée en mémoire, comme dans le calcul 5.

## Verdict

**Gelable après corrections.** Aucune remarque bloquante, 2 à corriger, 7 mineures (remarques 18 à 26).

- Les 17 remarques sont traitées : 13 tenues, 4 écarts défendus que j'accepte (2, 5, 7, 10). Les remarques 1 et 17 étaient sans suite.
- La bloquante n° 2 est levée. Sur l'artefact « relation entre littéraux » du premier contre-lecteur, le Newton amorti écrit dans la v3 converge sur les 480 apprentissages, en 18 tours au plus. Le Newton pur de la v2 échoue sur 125 d'entre eux : je retrouve le compte. L'excès revient à 0,885 et la garde, arrêtée au premier tour, rend C3 non tenue.
- Les huit décisions de la mère sont portées. Les 25 empreintes de la table de la v3 et les 11 de la réponse sont conformes, ainsi que leurs compagnons et les préfixes courts.
- Les deux remarques à corriger sont courtes et ne demandent pas de nouvelle contre-lecture :
  - la quatrième sonde de la version 8 n'a ni rang j ni place dans C3 ;
  - la zone aveugle de la sonde des nombres (énoncés notés 0) s'ajoute à la tolérance de la fuite cantonnée, et le § 8 ne le dit pas.

## 1. Les 17 remarques

| n° | objet | dans la v3 | statut |
|---|---|---|---|
| 1 | différences v1/v2 | sans suite (conforme) | tenue |
| 2 | **bloquante** : Newton sans garde | § 2.2 : Newton amorti, 200 tours, 60 essais de pas, garde « non convergé = non calculable », compte rapporté ; § 1, C3 : « une sonde non calculable… » ; § 4 : artefact « relation » et épreuve de la garde. Arrêt jugé sur le décrément, et non sur le pas effectif | **écart défendu, accepté** (écart 1, § 2) ; correction vérifiée par mon code (§ 3 b) |
| 3 | règle du hasard dans C4 | § 1, C4 : deux règles, j = 10 et 11, borne haute ≤ 0,50 chacune ; probabilité exacte ; M défini (domaines dépendants, domaine vide, affectations écartées et comptées) ; faux sans variable = 1 ; tirage de contrôle à graine écrite à la lettre | tenue |
| 4 | décisions (2) et (3), 120 racines et écarts en tête | tête, lignes 7 à 22 ; § 2.3, point 12 (« un Opus 5.5 neuf », « ne transmet rien au concepteur ») ; § 5, « Portée » | tenue |
| 5 | version 8, choix après coup | § 3, point 6 ; § 5 : « la dernière version […] qui tient C1 et C4 », écrite d'avance | **écart défendu, accepté** (écart 2) |
| 6 | « même loi » affaibli | tête, écart 8 ; § 1, C1, point 4 : « même loi jointe […], strates comprises » ; égalité par strate mesurée par C3 | tenue |
| 7 | une épreuve par garde | § 4, « Gardes d'arrêt » : les cinq violations de C1, la chaîne, le « trop beau », les 39 racines, la convergence, et en plus l'audit du tirage et « non calculable » ; « rapportée, non exigée » dans le tableau | **écart défendu, accepté** (écart 3), avec une précision demandée (remarque 23) |
| 8 | artefact « relation » ; longueur | § 4 : dose 1 tombe, dose 0,5 rapportée ; § 6, fait 2 (longueur) | tenue |
| 9 | fuite « côté vrai » | § 7 (définition) ; § 8, point 4 ; tête | tenue (rapportée, décision de la mère) |
| 10 | fuite parfaite sur un quart | § 8, point 5 : la fuite cantonnée et la fuite diluée sont séparées | **écart défendu, accepté** (écart 4), avec une précision demandée (remarque 24) |
| 11 | « un dixième exactement » | § 0 : « exactement » retiré ; biais +0,005 (8/76 − 0,10), qui joue contre la banque | tenue |
| 12 | ordonnée « nulle » | § 2.2, dernière ligne : « proche de zéro » | tenue |
| 13 | part réelle comparée à 0,50 | § 5 : la phrase « hors de portée » s'applique si l'une des deux parts dépasse 0,50 | tenue |
| 14 | 14,6 % / 5,0 % : hypothèse | § 5 : échangeabilité dite, et son défaut (120 viviers contre 119) | tenue |
| 15 | n₀ ≥ 2 choisi en connaissant la règle A | § 4, sous le tableau | tenue |
| 16 | indépendance des racines | § 4, « en description » ; § 8, point 11, avec chiffres (calcul 4, partie D, relus : bornes de même largeur à 0,001 près) | tenue |
| 17 | écarts 3 à 7 | sans suite | tenue |

Méthode : j'ai lu la v2 et la v3 en entier. Le `diff` montre une réécriture large ; chaque correction annoncée par la réponse se trouve au paragraphe indiqué. Je n'ai trouvé aucun changement qui n'y soit pas annoncé, hormis les ajouts du § 6 de la réponse (artefact « fenêtres », seuil d'audit 0,02, « non calculable » de C4, garde de la sonde tenue à l'écart, § 8 et § 9 repris), qui sont déclarés.

## 2. Les quatre écarts du concepteur

1. **Arrêt sur le décrément de Newton plutôt que sur le pas effectif : accepté.**
   - Le décrément, gradient · H⁻¹ · gradient, mesure directement l'écart au minimum : la perte au-dessus du minimum vaut environ la moitié du décrément. C'est le critère d'arrêt usuel du Newton amorti.
   - Le seuil 10⁻¹³ × n est atteignable en double précision : l'erreur d'arrondi du gradient est de l'ordre de n × 10⁻¹⁶, celle du décrément plus petite encore.
   - Mesuré par mon code, sur le banc du premier contre-lecteur (4 banques, 480 apprentissages chacune) : aucune non-convergence ; 18 tours au plus ; poids égaux à ceux du critère du pas effectif à 1,7 × 10⁻⁷ près ; mêmes excès.
   - Une réserve de rédaction, sans effet sur le calcul (remarque 25).
2. **« La dernière version mesurée à temps qui tient C1 et C4 », sinon la version 6 : accepté.**
   - La règle est écrite d'avance et déterministe : rien ne se choisit après lecture.
   - Elle ne punit pas la tentative d'une version 8, et la lecture en verdict reste fermée pour toute version qui ne tient pas C2 et C3. Le cas « version 8 qui tient C1 et C4 mais fuit plus » ne change que le banc des bras en lecture en preuve seule, et la règle de C4 tient sur cette version.
   - Je demande deux compléments de lettre : la remarque 18 (la quatrième sonde) et la remarque 22 (une tentative écrite est mesurée).
3. **« Arrêtée par l'assertion visée », et non « et seulement elle » : accepté.**
   - Une paire à cheval sur deux mondes casse aussi, par nature, les proportions de deux cellules : le calcul 4, partie B, relève trois écarts.
   - Exiger « seulement elle » ferait échouer une épreuve juste.
   - Pour garder un contrôle de spécificité, je demande que les assertions secondaires attendues soient listées d'avance (remarque 23).
4. **Une fuite parfaite cantonnée à un quart fait tomber C3 ; la fuite diluée tient : accepté.**
   - L'argument est exact. Une fuite parfaite cantonnée à une part p des énoncés, que la sonde reconnaît, donne un rappel de p + 0,10, donc un excès de p.
   - Mesuré sur un quart (calcul 4) : 0,247, borne haute 0,258. C3 tombe.
   - La phrase de la première contre-lecture valait pour la fuite diluée (artefact « grandeur » à la dose 0,25). Le § 8, point 5 dit maintenant les deux cas.
   - Une précision à apporter sur le cas « un douzième » (remarque 24).

## 3. Décisions de la mère, et vérifications faites

### Décisions de la mère (vérifiées comme portées, non rediscutées)

| décision | où | constat |
|---|---|---|
| règle de trois instances au hasard jointe à C4, jugée par la probabilité exacte, graine `SeedSequence` consignée | § 1, C4 | portée. La probabilité exacte décide ; le tirage `SeedSequence(20261122, spawn_key=(3000, i, k))` est écrit à la lettre et sert de contrôle (audit au-delà de 0,02) |
| pas de plancher de portée, marqueur « en attente du mot de Lazar ; défaut le 2026-11-24 vers 20:07Z » | tête, ligne 11 ; § 5, « Portée » | portée, deux fois. R-5036 à 20:06:50Z plus 48 heures donne bien le 24 vers 20:07Z |
| sonde tenue à l'écart contrôlée par un Opus 5.5 neuf avant son scellement | § 2.3, point 12 | portée, avec l'interdit de transmission |
| 120 racines neuves et huit écarts déclarés en tête | tête, lignes 13 à 22 | portée |
| fuite « côté vrai » rapportée sans condition | tête ; § 7 ; § 8, point 4 | portée |
| limite de la fuite diluée écrite au § 8, seuil 0,10 inchangé | § 8, point 5 ; § 1, C3 | portée (lettre corrigée sur le fond, écart 4) |
| critère des sondes : rappel ≤ 0,20 à fausses alarmes ≤ 0,10 (GO-2026-11-22-121) | tête ; § 1, C3 | portée. GO-121 relu sur `origin/main`, `registres/go.md`, ligne 807 |
| Newton amorti ; non-convergence = non calculable = C3 non tenue | § 2.2 ; § 1, C3 ; § 0 | portée |

Traçabilité : R-5036 est sur `origin/main` (copie locale `dc19ef71`). R-5038 n'y est pas, et le commit `184aa5ab` que citent la v3 et la réponse est absent de ma copie : je ne l'ai lue que dans la passation `registres/passations/mathematiques-nouvelles--2026-11-22-2030.md` (remarque 26).

### a. Règle du hasard, par mon code (`verification-calculs-v1/verif_regle_du_hasard_v1.py`)

- **Cas simples.** J'ai calculé de trois façons : la formule exacte de la v3, le produit des trois tirages sans remise, et l'énumération de tous les triplets.
  - Un contre-exemple parmi 13 instances : 3/13 = 0,2308.
  - M ≤ 3 et m ≥ 1 : 1 ; faux sans variable (M = 1) : 1 ; m = 0 : 0 ; M = 4, m = 1 : 3/4.
  - Balayage de M = 1 à 40, pour toutes les valeurs de m : aucun écart entre les trois calculs.
  - Seuil de la moitié : 3 contre-exemples sur 13, 7 sur 31, 10 sur 46. Cela confirme « une instance sur cinq environ » et « au plus 2, 6 et 9 ».
- **Table du calcul 5** (N = 4, 10, 15, pièges en queue) : identique à la mienne au millième.
- **Version 6, sur ses 41 racines d'essai.** J'ai engendré les banques par le paquet, énuméré les instances par sa vérification exacte, puis calculé la probabilité et le tirage par mon propre code.
  - Moyenne 0,7382, min 0,6904, max 0,7901, borne haute (j = 11) 0,7434. C'est identique au calcul 5 : écart par racine au plus 1,1 × 10⁻¹⁶.
  - Faux tôt 0,9086 ; pièges 0,5631.
  - Tirage de contrôle : 0,7366, égal au calcul 5 racine par racine ; son écart au calcul exact est de 0,0016.
  - Sur 3 075 faux : 134 faux sans variable, 270 faux à au plus 3 instances, M au plus 3 328. Aucune affectation partielle, aucune instance complète au statut « hors capacité ».

### b. Garde de convergence, par mon code (`verification-calculs-v1/verif_newton_garde_v1.py`)

J'ai repris le banc du premier contre-lecteur, importé sans changement (racines 1000 à 1119). Le Newton est recodé d'après la lettre du § 2.2 de la v3.

| banque | non convergés (v3) | tours au plus | Newton pur v2 non convergés | critère du pas effectif : non convergés ; écart des poids | excès de la sonde des nombres, tous les faux (borne haute) |
|---|---|---|---|---|---|
| saine | 0 / 480 | 11 | 0 | 0 ; 6 × 10⁻⁹ | 0,001 (0,008) : tient |
| relation, dose 1 | 0 / 480 | 18 | **125** | 0 ; 1,7 × 10⁻⁷ | **0,885 (0,888) : tombe** |
| relation, dose 0,5 | 0 / 480 | 10 | 0 | 0 ; 7 × 10⁻⁹ | 0,097 (0,107) : tombe à peine |
| grandeur, dose 1 | 0 / 480 | 14 | 0 | 0 ; 3 × 10⁻⁸ | 0,900 (0,900) : tombe |
| épreuve de la garde : arrêt au premier tour, banque saine et « relation » | 480 / 480 | 1 | — | — | non calculable sur 120 racines : C3 non tenue, sans plantage |

Je retrouve exactement les chiffres du premier contre-lecteur (125 sur 480 ; 0,885 ; 0,097). La garde est éprouvée sur un cas sain et sur un artefact, comme le veut la règle R5.

### c. Empreintes (`verification-calculs-v1/verif_empreintes_v1.py`)

Le calcul porte sur les 25 lignes de la table de la v3, les 11 de la réponse et les 9 préfixes courts : fichier, empreinte citée et compagnon `.sha256` concordent, sans aucun écart. Tous les compagnons du dossier `batterie-v1` (calculs et contre-lecture compris) passent `sha256sum -c`. Le scellement de la v3 et de la réponse est vérifié par `controle_ia.scellement verifier`.

## 4. Nouvelles remarques

### 18. À corriger — la quatrième sonde de la version 8 n'a pas de place dans C3 (§ 1, C3 ; § 2.3, « Version 8 »)

- Le § 2.3 garde la sonde de la version 7 et en ajoute une neuve pour la version 8. La batterie de la version 8 a donc quatre sondes.
- Or C3 dit « trois sondes », « neuf grandeurs », j = 1 à 9, et le retrait renvoie à « six grandeurs ». La graine de la borne haute de la quatrième sonde n'est donc pas écrite.
- Ce n'est pas un choix fait après lecture, mais un trou dans la lettre d'une pièce décisive.
- Correction : pour la version 8, C3 porte sur douze grandeurs. Il faut donner les j de la sonde neuve (par exemple 12 à 14 ; si la mesure « côté vrai » reçoit un jour des j, en prendre d'autres) et dire le compte en cas de retrait de l'une ou l'autre sonde tenue à l'écart.

### 19. À corriger — la zone aveugle de la sonde des nombres s'ajoute à la tolérance de la fuite cantonnée (§ 2.2, « Apprentissage » ; § 8, point 5)

- Un squelette qui a moins de 20 énoncés d'apprentissage dans les autres racines reçoit le score 0. Jusqu'à un énoncé de la sous-banque sur dix peut l'avoir sans que la sonde devienne non calculable.
- Sur ces énoncés, la sonde des nombres ne voit aucune fuite. Une fuite parfaite logée dans des squelettes rares (au plus 10 %) s'ajoute donc à une fuite cantonnée visible d'un peu moins de 10 %. Seule la sonde tenue à l'écart peut encore la voir.
- Le § 8, point 5 donne la tolérance comme « nettement moins d'un dixième » : c'est incomplet.
- Le même concepteur écrit le générateur (§ 8, point 16) et connaît la règle des 20 énoncés.
- Correction minimale : l'écrire au § 8, point 5, et dire en tête du rapport la part des énoncés notés 0 par racine.
- Option pour le concepteur, sans que je la prescrive : compter un énoncé noté 0 comme « déclaré faux » pour les faux, ce qui est pessimiste pour la banque ; ou abaisser la part admise.

### 20. Mineure — une instance complète au statut « hors capacité » n'est pas définie dans la règle du hasard (§ 1, C4)

- L'énumération du paquet peut rendre ce statut sur une instance complète. Le prototype la compte dans M, mais pas dans m.
- Le texte ne parle que des domaines non évaluables (affectation écartée et comptée) et des instances non énumérables (non calculable).
- Il n'y en a aucune sur la version 6 (§ 3 a). Écrire le traitement, par exemple « écartée et comptée », comme les domaines non évaluables.

### 21. Mineure — relecture de la banque réelle : une valeur non calculable n'est pas traitée (§ 5)

Le prototype la tient pour hors de la plage (`hors_de_la_plage`). Écrire au § 5 : « une valeur non calculable ferme la lecture en verdict ».

### 22. Mineure — une tentative de version 8 décidée doit être mesurée (§ 3, point 6)

- Le texte dit que la décision de tenter la version 8 est écrite avant sa mesure. Il ne dit pas qu'elle sera mesurée.
- Le concepteur pourrait abandonner une version 8 après des essais privés sur racines d'essai, et garder la version 7.
- Ajouter : « une tentative écrite est mesurée, sauf si elle n'est pas prête à la date ; tout abandon est rapporté avec sa raison ».

### 23. Mineure — spécificité des gardes de C1 (§ 4, « Gardes d'arrêt » ; écart 3)

Ajouter à l'attendu de chaque violation la liste, écrite d'avance, des assertions secondaires qu'elle peut déclencher par nature (par exemple : « deux mondes » donne aussi deux écarts de proportion). Une assertion déclenchée hors de cette liste est un fait d'instrument.

### 24. Mineure — § 8, point 5 : le cas « un douzième » n'est pas une fuite cantonnée reconnue (écart 4)

- Le banc place la fuite dans l'écriture g1 des seuls mondes de borne 4.
- La sonde, qui apprend un modèle par squelette commun à toutes les bornes, ne sait pas lesquels fuient : 0,064 au lieu de 1/12 = 0,083 en théorie (calcul 4 : g1 à 0,138 et non 0,9).
- C'est déjà en partie une fuite diluée. Écrire que la valeur théorique d'une fuite reconnue sur un douzième est d'environ 0,083 (C3 tient encore), et que 0,064 est le cas du banc.
- Dans la tête, « la fuite cantonnée » est dite « mesure rapportée » : préciser que ce qui est rapporté, ce sont les excès par squelette (§ 7), et que le § 8 en écrit la limite.

### 25. Mineure — § 2.2, « Pourquoi ce calcul » : le reproche fait au pas effectif est trop large

- Le critère du pas effectif « conclut à la convergence quand la recherche piétine » seulement si l'on fait le pas même quand il n'est pas accepté. C'était le cas du script de la première contre-lecture.
- Avec la garde de la v3 (soixante essais sans pas qui convienne = non convergé), ce n'est pas le cas. Mesuré : les deux critères rendent les mêmes verdicts sur 1 920 apprentissages.
- Réduire la phrase à « le décrément mesure l'écart au minimum lui-même ». Sans effet sur le calcul.

### 26. Mineure — traçabilité de R-5038

- La v3 et la réponse citent R-5038 dans `registres/decisions.md` sur `main`, lu au commit `184aa5ab`.
- Ce commit est absent de ma copie, et R-5038 manque dans `origin/main` à `dc19ef71`. Je n'ai trouvé la décision que dans la passation du 2026-11-22-2030.
- À confirmer par la mère avant le gel : que R-5038 est poussée sur `main`, et que son contenu est bien celui de la passation.

## 5. Ce que la v3 a pu casser : examiné

- **Condition impossible sur une banque saine** : non trouvée.
  - La règle du hasard est tenable : 0,131 sur la banque saine du banc.
  - Elle impose des contre-exemples rares, au plus 2 sur 13 instances, 6 sur 31 et 9 sur 46, et peu de faux sans variable (chacun compte 1). C'est le but de la décision (1).
  - Le seuil du décrément n'arrête pas à tort : aucun cas sur 1 920 apprentissages du banc, ni sur 1 787 de la version 6 (calcul 5).
- **Fourche cachée** : celle des versions 7 et 8 est fermée. Deux lettres restent ouvertes, sans choix après lecture : la quatrième sonde (remarque 18) et la tentative non mesurée (remarque 22).
- **Échappatoires d'une version 7 qui passerait C1 à C4 en fuyant encore** :
  - une fuite « côté vrai » : rapportée seulement, par décision de la mère ; écrite au § 8, point 4 ;
  - une fuite cantonnée sous un dixième, ou diluée jusqu'à un quart : écrite au § 8, point 5 ;
  - la zone aveugle des squelettes rares : non écrite (remarque 19) ;
  - des contre-exemples rares placés à des instances saillantes : écrit au § 8, point 6, et rapporté par la règle des instances saillantes ;
  - parité, divisibilité, chiffres : rôle de la sonde tenue à l'écart (§ 8, point 8).
- **Contradictions internes** :
  - § 1, C3 (trois sondes, j = 1 à 9) contre § 2.3, « Version 8 » (quatre sondes) : remarque 18 ;
  - tête (« fuite cantonnée » comme mesure) contre § 7 : remarque 24 ;
  - rien d'autre : les j de § 0 et § 1 concordent avec le calcul 5 (2001 à 2006, 2010, 2011).

## Pièces (SHA-256 aux compagnons)

| pièce | chemin |
|---|---|
| cette vérification | `docs/notes/mathematiques-nouvelles-v1/banque-revisee-v1/batterie-v1/verification-corrections-batterie-v3-v1.md` |
| règle du hasard : cas simples, table, version 6 | `…/batterie-v1/verification-calculs-v1/verif_regle_du_hasard_v1.py` ; sorties `sortie-verif-regle-du-hasard-v1.txt` et `.json` |
| garde de convergence sur le banc du premier contre-lecteur | `…/verification-calculs-v1/verif_newton_garde_v1.py` ; sorties `sortie-verif-newton-garde-v1.txt` et `.json` |
| empreintes citées | `…/verification-calculs-v1/verif_empreintes_v1.py` ; sortie `sortie-verif-empreintes-v1.txt` |

Durée des calculs : environ une minute pour la règle du hasard et cinq minutes pour la garde, sur un seul fil.
