# Vérification de la partie 1, v3, de l'addendum des empreintes et des déclarations (tranche de l'ajustement de nos lentilles)

- **Vérificateur neuf** (R2) : n'a écrit ni relu aucune pièce de ce travail ; n'écrit que ce rapport (sans compagnon `.sha256` : un seul
  fichier permis ; à sceller par la session mère).
- Date (`date -u`) : 2026-11-18T05:45:22Z.
- Objet : `docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md`, empreinte recalculée
  `bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1` (égale à l'attendue et à son compagnon `.sha256`).
- Version précédente : `…-partie1-v2.md`, `0b418ed13b07fc2886f07367a1e478d90038e59e0c2bfd1bc65a03f3a5695596` (recalculée).
- Vérification de la v2 : `verification-addendum-tranche-b-beta-partie1-v2.md`,
  `1920510ac5d5428076835216268ac5a572730f1327f4274c949adbd8c3289593` (recalculée ; égale au début cité par la v3).
- Texte gelé scellé : `texte-gele-tranche-b-beta-v1.md`, `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` (recalculée, égale).
- Code des verdicts : `src/controle_ia/neuron_lens/verdicts_b_beta_v4.py`, `8c07434f9db0e35e10eb806218da320bc0d6e404e41c4f60c495b35906d88b87` ;
  essais `tests/test_neuron_lens_verdicts_b_beta_v4.py`, `1b63c8cbbcdff180e0a3433ebeb139eea3c4aeeb13fcc3f694352219a4f7bb5a` (rejoués : 82 réussis).
- Non ouverts : `registres/`, `diag/`. Aucun autre fichier modifié, rien de committé. Sondes : script jetable hors du dépôt, entrée saine
  `sain()` des essais, module importé avec `PYTHONPATH=src`.

## Verdict

**Scellable** : 0 bloquante, 0 majeure, 4 mineures neuves (forme ou précision ; aucune ne rend une phrase fausse au point de changer
une issue, un arrêt ou un seuil).

La majeure N1 de la vérification de la v2 est levée ; cinq mineures sont levées, la sixième (sigles seuls) est laissée et déclarée
comme telle au § 8. Le diff ne touche rien d'autre. Toutes les phrases neuves du § 1.1 sont confirmées par sonde.

## (1) Diff v2 → v3 (relu ligne à ligne)

Touchés : titre (« v3 ») ; en-tête (filiation des versions, liste des arrêts et nœuds ajoutés, moment de la comparaison) ; § 1.1
(« le contre-lecteur de la v1 et le vérificateur de la v2 » ; puce de la lecture contre ablation par fenêtre ; puce des bornes ;
fin de la lecture 2) ; § 3, dernière phrase du paragraphe des valeurs attendues ; § 5, dernière phrase ; § 8 ajouté. **Rien d'autre** :
§§ 1.2, 1.3, 1.4, 2, 4, 6, 7, toutes les tables et toutes les empreintes sont inchangés.

| point de la vérification de la v2 | état dans la v3 |
|---|---|
| majeure N1 (i), borne fausse pour la lecture contre ablation | **levée** : borne 32 ≤ n < 48 restreinte à la lecture contre pilotage (B-2) et à l'avance sur la lentille des logits (B-3) ; pour la lecture contre ablation, « tout n < 48, jusqu'à n = 0 » |
| majeure N1 (ii), conséquence du retrait du déclencheur de l'audit de la lecture contre ablation par le haut (A5) | **levée** : écrite, sens favorable, condition « si A1 n'est pas déclenché » |
| majeure N1 (iii), comptes | **levée** : 3 sur 8 (couches 8 à 15), 2 sur 4 (couches 26 à 29) |
| mineure N2 (parenthèse des arrêts ajoutés) | levée |
| mineure N3 (« arrêt » au § 3, moment) | levée |
| mineure N4 (lecture 2, verdict d'ensemble) | levée |
| mineure N5 (§ 5 contre l'en-tête) | levée |
| mineure N6 (« vérifiés par sonde par le contre-lecteur ») | levée |
| reste : sigles seuls (« B-α », « garde (i) », « garde (f) ») | **laissé**, déclaré au § 8 (forme) |

## (2) Phrases neuves du § 1.1, rejouées par sonde

Entrée : `sain()` (verdict « reproduit avec nos lentilles »). Audits déclenchés servis par une relance saine (`graine1`), sauf mention.

| sonde | résultat | phrase de la v3 |
|---|---|---|
| « ablate win », `r_med` de notre R à 0,45 aux couches 8 à 15 ; 0, 1, 2 couches non lisibles (toutes les combinaisons), n = 47 | B-7 « non reproduit », A5 déclenché | juste |
| même entrée, **3** puis 4 couches non lisibles (les 56 triplets, les 70 quadruplets), n = 47, **31** et **0** | B-7 « autre », **aucun audit déclenché, aucune chaîne en défaut**, les trois valeurs de n | juste (« 3 sur 8 » ; « tout n < 48, jusqu'à n = 0 » ; « la garde (b) ne s'applique pas ») |
| « ablate win », `r_med` à 0,10 aux couches 26 à 29 ; 0 ou 1 couche non lisible, puis **2** et 3 (toutes les combinaisons), n = 47 et 0 | 0 et 1 : « non reproduit » ; 2 et 3 : « autre » ; aucune chaîne en défaut | juste (« 2 sur 4 ») |
| n = 0 aux 32 couches de « ablate win », rien d'autre | B-7 « autre », B-2 « reproduit », verdict « reproduit avec nos lentilles », aucun défaut | juste |
| A5 déclenché (0 ou 2 couches non lisibles), relance dégénérée (`temoin_distinct` faux) | « chaîne en défaut », (l) | juste (« voie vers la chaîne en défaut (l) ») |
| même entrée, **3** couches non lisibles, même relance dégénérée | aucun audit ; verdict « reproduit avec nos lentilles » | juste (« une relance qui aurait été dégénérée n'est pas vue », sens favorable) |
| même entrée, 3 couches non lisibles, **A1 déclenché** (`r_med` à 0,96 à la couche 3), relance dégénérée | « chaîne en défaut », (l) par A1 | juste (« si A1 n'est pas déclenché ») |
| « steer 1x », `r_med` à 0,10 aux couches 16 à 23, n = 48, 47, 32, 31 à trois couches | 48 : « non reproduit avec nos lentilles » ; 47 et 32 : B-2 « autre », « partiel » ; 31 : chaîne en défaut (b) | juste (borne de B-2) |
| écart à la lentille des logits à −0,05 aux couches 4 à 15 ; 3 couches non lisibles, puis 4 à n = 47, 32, 31 | 3 : « non reproduit » ; 4 : B-3 « autre », « partiel » ; n = 31 : chaîne en défaut (b) | juste (borne de B-3) |
| témoin de notre R à 0,07 à deux couches lisibles ; puis l'une non lisible (n = 47, 32) ; puis n = 31 | « partiel », B-2 « autre » ; puis **« reproduit avec nos lentilles »**, B-2 « reproduit » ; n = 31 : chaîne en défaut (b) | juste (lecture 2 : « et le verdict d'ensemble de « partiel » à « reproduit avec nos lentilles » ») |

« A5 est, avec A1, la seule voie vers la chaîne en défaut (l) » : conforme au code (un seul bloc, `relance`, pose (l)) et au texte gelé
(l. 232-233 ; audits A1 et A5, l. 518 et 522).

## (3) Moment de la comparaison ; arrêts et nœuds ajoutés

- **« relevé et comparé juste après `03_token_counts.py`, avant `lens_compare.py` et avant la fumée »** : compatible avec l'ordre gelé
  de l'étape B2 (l. 374-380 : `05_act_corpus.py` ; garde (i) ; `03_token_counts.py` une seule fois ; jetons gardés versés à l'addendum ;
  puis `lens_compare.py` ; garde (k) ; fumée `06_activations.py --docs 64` ; passe complète), avec la garde des jetons gardés (r)
  (l. 248-249) et avec la liste d'arrêt (l. 540 : addendum scellé avant la première passe). Exact.
- **§ 3, « arrêt à cette étape …, consigné, et message à la mère (nœud), comme le veut la liste d'arrêt pour toute empreinte
  différente »** : conforme à la l. 546 (« empreinte d'un fichier différente de celle écrite ici ou à l'addendum → arrêt ; message à la
  mère »). « N'est pas une chaîne en défaut » : exact (la garde (r) compare à la valeur consignée après `03_token_counts.py`, non à
  celle d'une autre tranche).
- **En-tête, « ajoute seulement des arrêts ou des nœuds dans le sens sévère »** : les trois cités (essai renforcé, § 1.2 ; valeurs
  attendues, § 3 ; version d'un paquet autre que Drowse, § 5) sont bien ajoutés et sévères ; « l'arrêt sur la version de Drowse est
  déjà dans le texte gelé » : exact (l. 341-342, 545).
- **§ 5, « relevée en partie 2 à B0 et nœud à la mère avant l'ajustement »** : aligné sur l'en-tête ; compatible avec l'étape B0
  (l. 363, environnement monté à B0).

## (4) Points neufs

Aucun bloquant, aucun majeur.

| rang | lieu | constat | correction possible (sans obligation avant scellement) |
|---|---|---|---|
| mineure n1 | § 1.1, puce de la lecture contre ablation | La parenthèse « (témoin ou pilotage dégénéré sous la relance à la graine 1) » abrège la chaîne en défaut (l) : selon le texte gelé (l. 232-233, 518), elle couvre les contrôles (1) et (2) (témoin distinct, norme non nulle, lus au fichier `-causal.pt`, non « sous la relance ») **et** une garde (a) à (c) manquée sur la sortie de la graine 1. La voie supprimée est donc un peu plus large que « une relance qui aurait été dégénérée ». Le sens (favorable) et la conclusion restent justes. | « (contrôles du témoin et du pilotage manqués, ou garde (a) à (c) manquée sous la graine 1) ». |
| mineure n2 | en-tête et § 3 | Les fichiers du corpus d'activations existent dès `05_act_corpus.py` ; les comparer seulement « juste après `03_token_counts.py` » laisse jouer l'unique compte de jetons sur un corpus pas encore comparé. Sans effet sur une issue : l'écart arrête de toute façon avant `lens_compare.py` et la fumée, et le compte tourne sur processeur. | Comparer les quatre fichiers juste après `05_act_corpus.py`, la liste des jetons gardés juste après `03_token_counts.py` ; ou laisser, en le sachant. |
| mineure n3 | en-tête contre § 3 | L'en-tête range le § 3 parmi les nœuds **ajoutés** ; le § 3 dit que l'arrêt est celui que « veut la liste d'arrêt ». Les deux se tiennent (ce qui est ajouté, ce sont les valeurs attendues, auxquelles la l. 546 s'applique alors), mais la ligne ne vise que des empreintes de fichiers : le nombre 89 498 et l'empreinte de la liste des jetons gardés sont couverts par l'ajout, non par la lettre de la l. 546. | Forme ; rien à changer si la mère lit ainsi. |
| mineure n4 | § 1.1, puces neuves | « A1 » paraît en sigle seul (au § 1.1, seul A5 est nommé : « non reproduit par le haut ») ; s'ajoute au reste déclaré au § 8. | « l'audit du trop beau de la lecture contre pilotage (A1) ». |

## Non vérifiable

- Les renvois R-3190, R-3180, R-3171, R-3151 et les numéros de GO : dans `registres/`, non lu par consigne.
- Valeurs attendues du § 3 et versions du § 5 contre la partie 2 de la tranche des lentilles publiques (`diag/`) : non relues (consigne) ;
  inchangées depuis la v2 (diff), elles reposent sur la vérification de la v2 (« toutes égales »).
- §§ 1.2 à 1.4, 2, 4, 6, 7 : inchangés depuis la v2 (diff) ; non revérifiés ici.
- Effets de la lecture 1 sous la relance à la graine 1 (une bande 8 à 15 partielle sous la seule graine 1 rend la lecture contre
  ablation « autre » au lieu de « maintenue ») : lus dans le code, non sondés ; ils ne touchent que cette mesure, hors du verdict d'ensemble.
- Que le code de course fasse bien la comparaison au moment écrit (juste après `03_token_counts.py`) : ce code n'est pas l'objet de la vérification.
