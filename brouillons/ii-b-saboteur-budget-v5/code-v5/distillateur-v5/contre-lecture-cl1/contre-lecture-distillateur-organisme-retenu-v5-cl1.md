# Contre-lecture du distillateur du mode réel de l'organisme retenu, version 5 — cl1

Date : 2026-11-21. Pièce d'instrument (classe B). Même contre-lecteur (Claude Opus 5.5), même mandat (`47b53672…`). Pièces lues en entier, compagnons vérifiés : les trois correctifs de `code-v5/distillateur-v5/correctifs/`, le rapport du développeur, ses sorties d'essais et de mutations, son mandat (`registres/iib-reconception/mandat-developpeur-distillateur-organisme-retenu-v5-v1.md`).

Deux arbres neufs à moi, branches locales jamais poussées :
- `arbre-distillateur` : les six correctifs du code, puis les trois du distillateur ;
- `arbre-fusion` : ces trois correctifs par-dessus le 0007 des corrections de l'étalonnage.

Rien poussé, aucune dépense, aucune machine, aucun fichier supprimé, aucun refus d'outil. Textes de référence : le texte scellé (`c1dc5459…`) et son erratum 1, le devis scellé (`cb881522…`), et la conception d'origine (`brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1.md`, sections 4 et 5) pour ce que le texte scellé ne change pas.

## Verdict pour la course : après corrections

Le distillateur lui-même est conforme et bien gardé. Trois choses manquent ou restent à trancher :
- le point d'entrée de la course (bloquant, point 3) ;
- la lecture de la première action dans la perte (un nœud, point 1), à trancher **avant l'étalonnage** ;
- l'essai à torch, à jouer avant l'ordre de la course.

## Conformité

- **Distillation** : élève et témoin sur les mêmes épisodes, avec les mêmes exclusions. Les réglages sont égaux à la configuration de la première course : rang 16, `alpha` 32, quatre projections, simple précision, sauvegarde en demi-précision rechargée, trois époques, lot 1, pas 1·10⁻⁴, norme 1. Les doses sont H 0, B50 0,5, B100 1 et TJ100 1 (témoin) ; les conditions d'évaluation sont les quatre de la conception d'origine (5.1 à 5.3), dans le même ordre. L'ordre des opérations suit `lanceur_v1` : logits et empreinte de la base, caches vidés, une injection, simple précision, état neuf par graine, entraînement à dose 1, sauvegarde rechargée, empreinte de la base relue, identité à dose 0 et son artefact à dose 1. Les signatures des fonctions appelées dans `organismes.lora`, `t06.distillation_transcription` et `t06.identite` sont vérifiées.
- **Témoin (section 11)** : premier coût gardé à l'octet ; sous N, la suite retenue ; sous P, une des huit suites (code de `temoin_jumeau_v5`, déjà contre-lu). Il est refusé s'il est égal au maître.
- **Nœud 7 (b')** : l'évaluation joue les deux oracles au modèle de base (`charger("H")`, dose 0 relue par la garde du jumeau à chaque tirage) ; la clôture exige l'ordre H, B50, B100, TJ100 puis H.
- **Gardes (R5)** : chacune a un cas sain et un artefact ; l'épreuve par mutation en voit 21 sur 21.
- **Essais rejoués fichier par fichier** (`sorties/essais-distillateur-fichier-par-fichier-v1.txt`) : section 26, distillateur 32, bout en bout 4, lanceur 12, configuration 22, tours 8, tous réussis ; le fichier à torch est sauté.
- **Fusion avec les corrections de l'étalonnage (0007)** : les trois correctifs s'appliquent sans conflit (`sorties/essais-fusion-0007-distillateur-v1.txt`) ; section, distillateur, bout en bout, configuration et régénéré réussissent. Un seul échec, attendu : l'essai de l'amorce exige que la liste `tests-cibles-iib-v5-v2.txt` porte tous les fichiers d'essais v5, et elle n'a pas les quatre fichiers neufs. *Correction* : une liste en version neuve et son empreinte dans l'amorce.
- **Consignes privées** : la recherche par programme (`scripts/recouvrement-consignes-distillateur-v1.py`, `sorties/recouvrement-consignes-distillateur-v1.txt`) touche quatre lignes, toutes des tournures génériques. Aucun fragment. Les sorties ne portent que des noms de motifs (« iib:NN »).
- **Ce que torch laisse sans épreuve** : tout `MoteurTorch`, c'est-à-dire injection, entraînement, sauvegarde et recharge, doses, empreintes, logits. S'y ajoutent `motifs_de_la_course` (scipy), la mémoire de carte et le coût de la surveillance. `tests/test_iib_distillation_torch_v5.py` n'a jamais été joué : **il faut le jouer sur un poste à processeur qui a torch, transformers et scipy, avant l'ordre de la course**, et non découvrir un défaut sur l'instance après les tours.

## Les trois points à juger

**(1) La première action dans la perte de distillation : un nœud de conception, pas une lecture.**
- À la lettre, la règle d'origine (5.1, « les actions non bornables qui portent un champ COST sortent de la perte ») sort toujours la première action, puisqu'elle n'est jamais comptée dans l'organisme retenu. Mais cette règle a été écrite quand la première action était bornable.
- Le texte scellé ne tranche pas, et les deux lectures changent ce que l'élève apprend :
  - *exclue* : aucun apprentissage de la première action entière, proposition comprise. La signature « premier coût sans excès » (section 6, point 2, « l'élève l'apprendra ») et le contrôle du premier coût de l'élève (6 bis.2) se lisent alors autrement.
  - *gardée* : l'élève apprend un premier coût que rien n'a borné. Le motif d'origine de l'exclusion (un coût que l'oracle ne garantit pas) vaut aussi pour lui, puisqu'il est invisible aux deux oracles.
- C'est donc à Lazar de trancher.
- **Il faut trancher avant l'étalonnage** : la configuration de la course est celle de l'étalonnage, sans ajout (`configuration_de_course`). La section `distillation_evaluation`, champ rempli, doit donc être dans la configuration scellée de l'étalonnage. Sinon la course est refusée avant le premier tour, après un étalonnage payé.
- Laisser le champ vide et refuser tout lancement tant qu'il l'est : la garde est juste.
- Recommandation : *gardée*, confiance moyenne. Elle est cohérente avec 6.2 et 6 bis.2, et l'interdit d'excès au premier coût est déjà une demande de la consigne, regardée par le contrôle chiffré.

**(2) Jusqu'à 127 épisodes à la distillation : pas un défaut de code ; texte et devis à corriger par erratum.**
- La conception d'origine (section 4) l'écrit : « Tous les épisodes acceptés à cet instant sont distillés (au plus 96 + 31 = 127) ». Le texte scellé reprend la fin « dès 96 », sans écart déclaré.
- Ce sont « 48 à 96 » (6 bis.2), « 96 épisodes acceptés au plus × 10 » (10.2 et nœud 7) et « 2 × 96 transcriptions » (devis) qui comptent trop court.
- Tronquer à 96 serait choisir des épisodes, ce qui est interdit sans règle. La garde 48 à 127 et le champ `au_dela_de_la_cible` sont justes.
- Effet chiffré au pire :
  - 310 actions d'oracle de plus hors tours, environ 2,6 minutes ;
  - 186 transcriptions-époques de plus à 1,86 s, environ 5,8 minutes ;
  - en tout, environ 0,2 dollar, sous la réserve de 10 dollars.
- Le fichier d'entrées garde 3 520, qui est scellé : le plafond de tours est surestimé de moins d'un dixième de tour. *Correction* : erratum du devis et des trois phrases du texte, sans changer le code.

**(3) Le point d'entrée de la course manque : bloquant pour la course.**
- `executer` ne connaît que l'étalonnage et les conditions, et l'amorce v5 ne lance que l'étalonnage. Ce qu'il faut :
  - une phase `course` qui construit `distillateur_du_mode_reel(modele, racine, diag, progres, ids_etalonnage=<donnees/<run>/lots/ids-lot-*.json>)` et passe **`d.modele`**, le modèle surveillé, à `phase_course` ;
  - une amorce de course en version neuve ;
  - des marques de progrès par tour : `phase_course` ne passe aucun `apres_tour` à `boucle_des_tours`, et la surveillance ne voit donc rien pendant les tours ;
  - un versement par tour : `phase_course` n'écrit rien avant la fin des tours. C'est le défaut M1, pour la course.
- Sans le chemin des identifiants, les faux positifs des motifs sont dits « non calculés », sans arrêt.
- L'ordre devra dire si la course joue sur la même machine que l'étalonnage, ce que suppose le devis (« une seule location ») alors que les conditions se jouent sur processeur.

## Les copies mutées de `brouillon/`

Les compagnons qui ne correspondent plus sont **attendus et sans effet** :
- les deux seuls échecs (`tests/test_cibles_invisibles_v1.py`, `tests/test_lanceur_durable_v5_a1v4.py`) sont des compagnons dont le fichier est **absent dès la base** 836c7ccc, dans mes arbres aussi ;
- `copie-mutations-2/…/distillation_v5.py` est égal au code final ;
- `copie-mutations` porte l'état d'avant la correction de la lecture des identifiants par lot, comme le dit le rapport.

Ce sont des copies de travail : elles ne vont dans aucun versement de code et ne sont citées par aucune pièce.

## Mineurs

- n1 Le distillateur dérive ses graines par `jumeau_v5.Graines` (clés de la conception d'origine), et non par `manifeste.graines` comme la version 1. Elles sont consignées et rejouables : rien à faire, sauf le dire.
- n2 La cadence de surveillance (tous les 10 appels) n'est fixée par aucun texte ; elle est déclarée. Rien à faire.
- n3 La documentation de `lanceur_v5` dit encore « distillateur non écrit » ; à corriger à la fusion.
