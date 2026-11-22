# Note de vérification courte — correctif 0013 (coupure de l'étalonnage portée de 12 à 16 USD) — cl1

Date : 2026-11-22. Même vérificateur (Claude Opus 5.5), même mandat ; aucune sortie de l'étalonnage lue.

**Verdict : conforme**, au mot de Lazar près : le seuil de 12 USD vient du devis et de la ligne GO-2026-11-21-70, et seul Lazar peut le porter à 16. Un mineur (m1).

- **Application** : `git am` du 0013 (`8538c203…`, compagnon OK) sur `887561b7` rend l'arbre **`a08acfe6…`**, celui qui est annoncé. Sur le **commit de lancement `43d6d067`**, il s'applique aussi, sans conflit. Il ne touche que quatre fichiers : `scripts/lancer_iib_v3.sh`, `src/controle_ia/iib/session_v5.py`, `tests/test_iib_lanceur_v5.py` et `tests/test_iib_environnement_machine_v5.py`. Aucun des fichiers que le commit de lancement ajoute (configuration, entrées, pièces, `registres/go.md`) n'est touché.
- **Rien d'autre ne change** que le seuil, ses textes et ses essais :
  - la constante `COUPURE_ETALONNAGE_USD`, qui passe de 12 à 16 ;
  - deux phrases de documentation ;
  - la ligne d'en-tête de la surveillance ;
  - les valeurs des essais (11 h pour le cas sain, 12 h pour l'artefact) et deux noms d'essais.
- **Essais touchés, rejoués sur `43d6d067` plus 0013** (`sorties/essais-0013-sur-lancement-v1.txt`) : `test_iib_lanceur_v5.py`, 20 réussis ; `test_iib_environnement_machine_v5.py`, 4 réussis.
- **Note du développeur : juste.**
  - Ligne 79, `DEPOT` vaut `IIB_DEPOT` ou l'arbre du lanceur. Ligne 88, `SESSION` importe `session_v5` depuis `$DEPOT/src`. Ligne 427, un `python3` neuf est lancé à chaque relevé.
  - Une surveillance déjà lancée prend donc le seuil neuf **au relevé suivant, sans redémarrer**. Sa ligne d'en-tête reste « 12 ».
  - La boucle, analysée tout entière par bash comme une seule commande composée, n'est pas relue. `session_v5.py` n'est vérifié par aucune empreinte.
- **Le risque d'un changement sous une surveillance en marche** : si un relevé tombe pendant l'extraction, `session_v5.py` peut être absent ou à moitié écrit.
  - La règle devient alors illisible : `ARRET garde : règle de coupure de l'étalonnage illisible` (l. 431), avec le code 3, ce qui commande l'arrêt de la machine et perd l'étalonnage en cours. La garde va dans le sens prudent, mais pour un mauvais motif.
  - Les traces mêlent aussi deux seuils : l'en-tête dit 12 et la décision applique 16.
- **La manière la plus sûre** :
  1. relever le numéro de processus de la surveillance et l'arrêter par ce numéro (R10), juste après un relevé « RIEN » ;
  2. extraire le commit entier dans `$DEPOT` ;
  3. vérifier à blanc `coupure-etalonnage` sur un dossier jouet : 15,99 donne RIEN, 16,00 donne ARRET ;
  4. relancer la surveillance à l'identique, même identifiant et même dossier. L'en-tête écrira 16, le compte repart du début de l'amorce relevé dans `progres.txt`, sans remise à zéro, et l'on consigne le nouveau numéro de processus.
  
  Tout cela doit se faire avant que la dépense comptée n'atteigne 12 USD.
- **m1** : la documentation de `session_v5.py` dit « sous le plafond de 17 USD de l'étape 1 au devis ». Or le devis (§ 3) dit que 17 « n'est pas une seconde ligne » : c'est la dépense tenue, 12 + 0,92 + 3,84 = 16,76. À 16 USD, la dépense tenue devient environ **20,76 USD**, toujours sous la coupure de la ligne (55) et sous son plafond (60). La phrase est à corriger, et ce chiffre doit figurer dans la demande à Lazar.
