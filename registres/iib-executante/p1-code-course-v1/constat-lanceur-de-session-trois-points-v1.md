# Constat — lanceur de session de l'organisme retenu : trois points relevés par le rédacteur (lecture seule, aucun code)

Date : 2026-11-22. Développeur : Claude Opus 5.5. J'ai lu le code à la tête `6696aca1f`, branche locale `prep/iib-tirage-carte-local`. Ces trois points ne sont pas touchés par 0014 à 0021, sauf la ligne de création, où le correctif 0021 n'ajoute que `-e IIB_TIRAGE=$TIRAGE`. Contrordre de la mère : aucune correction n'est codée, car une ligne de GO neuve remplacera la garde.

## (1) Plafond de la configuration plus dépense antérieure au plus égal au plafond de la ligne : **confirmé**
- **`scripts/lancer_iib_v3.sh`** :
  - l. 237, dans `controles-explo` : `python3 … "$SESSION" go "$REG" "$GOC" "$PLC" "$ANT" "$JOUR"`, où `PLC` est le `plafond_usd` de la configuration (l. 235) et `ANT` vaut `IIB_DEPENSE_ANTERIEURE_USD` (l. 226) ;
  - l. 289, dans `creation` : le même appel, `ANT` étant le quatrième argument.
- **`src/controle_ia/iib/session_v1.py`**, l. 42-44 : `verifier_go_iib` appelle `session_v12.verifier_plafond_epreuve(plafond, anterieure, …)`. `session_v5` passe la sous-commande `go` à `session_v1`.
- **`src/controle_ia/t06/session_v12.py`**, l. 65-79 : `if p + a > limite: raise GardeSession(…)`, avec p le plafond de la configuration et a la dépense antérieure. Cette dépense antérieure s'ajoute au plafond entier de la configuration, alors que la machine neuve ne peut dépenser que ce qui reste.
- La configuration v5 porte `plafond_usd` = 55 (`configuration_v5.DEVIS`, l. 87, vérifié à l'égalité en mode réel). Avec une ligne à 60 USD, toute dépense antérieure au-delà de 5 USD fait donc refuser les contrôles et la création : avec 16 USD déjà dépensés, 55 + 16 = 71 > 60, refus.
- **Correction la plus étroite, non codée** :
  - garder la garde sur le plafond de la ligne ;
  - donner à la machine neuve une coupure effective égale au plafond de la ligne moins la dépense antérieure (ici environ 60 − 16,3 = 43,7 USD) ;
  - la passer à `session_v3 depense` (l. 314, heure d'épuisement de la minuterie) à la place de `PLC` ;
  - refuser si elle est nulle ou négative, sans toucher au plafond scellé de la configuration.
- Cette correction change une garde de dépense, et la mère annonce une ligne de GO neuve. Elle demanderait donc le mot de Lazar ou une ligne de GO neuve.

## (2) Seule la forme « N USD » est lue dans la colonne du plafond de `registres/go.md` : **confirmé**
- **`src/controle_ia/t06/session_v3.py`** :
  - l. 30 : `_PLAFOND = re.compile(r"(\d+(?:[.,]\d+)?)\s*USD(?:\s*\([^()]*\))?")` ;
  - l. 34-36 : `_plafond_ligne` exige la correspondance entière (`fullmatch`).
- **`src/controle_ia/t06/session_v12.py`**, l. 52-55 : `p = s3._plafond_ligne(c[4])` ; si elle échoue, `GardeSession("… plafond … illisible (« N USD » attendu …)")`.
- Sont donc refusés : « 60 $ », « 60 dollars », « USD 60 », « 60 USD cumulés », et tout texte hors d'une seule parenthèse finale. La ligne de GO neuve devra écrire son plafond sous la forme « N USD », éventuellement suivie d'un commentaire entre parenthèses.

## (3) Toute instance « iib… », arrêtée comprise, bloque la création : **confirmé**
- **`scripts/lancer_iib_v3.sh`**, l. 309-310, dans `creation` : inventaire, puis `"$SESSION" instances "$INV_FICHIER"`. Un refus donne le code 3 (nœud).
- **`src/controle_ia/iib/session_v1.py`**, l. 70-73 : `verifier_instances_iib` appelle `session_v2.verifier_instances(inventaire, "iib")`.
- **`src/controle_ia/t06/session_v2.py`**, l. 150-156 : toute entrée dont l'étiquette commence par `iib` est retenue, **quel que soit son état** (`actual_status` et `cur_state` sont seulement affichés), puis vient le refus.
- **Écart de documentation** : l'en-tête de `session_v1.py` (l. 12-13) dit que « les autres (7b, A1-v4, instances arrêtées) ne sont ni comptées comme bloquantes ni touchées ». Pour une instance arrêtée d'étiquette `iib…`, c'est faux : le code la bloque.
- **Rien n'est changé**, comme demandé : la destruction de 61875617 est en demande à la mère, et elle lèvera le blocage.
