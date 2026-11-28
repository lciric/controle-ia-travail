# Jury « robustesse et preuves » : addendum de lecture complémentaire de P3, candidats a, b et Gemini

## Verdict

Gagnant : **candidat b**, 8 sur 10. Ses tests tuent 10 mutants sur 12. Il refuse une lecture faite sur un autre run. Il
écrit un fichier d'arrêt avec son motif quand l'addendum s'arrête après le manifeste.
Candidat a : 5,5 sur 10. Il fait bien les calculs et refuse mieux certains replis. Mais ses tests ne tuent que 4 mutants
sur 12, et trois gardes demandées manquent ou sont faibles.
Gemini : 0 sur 10 comme candidat complet. Le module ne s'analyse pas (erreur d'indentation l. 332) et il n'a aucun
fichier de tests (règle du fichier absent). Une fois l'indentation corrigée dans une copie, ses fonctions donnent les
mêmes intervalles que a et b, au bit près. Elles valent comme témoin indépendant, pas comme module.

## Base du jugement et limites

- Texte qui fait foi pour ce jury : brouillon 1
  (`addendum-p3/P3-addendum-lecture-complementaire-v1-brouillon1.md`). Le brouillon 3 existe et change la forme de la
  sortie, la garde d'antériorité, A5 et A8. Aucun candidat ne l'applique. Je signale ce qui servira pour le brouillon 3,
  sans noter dessus.
- Fichiers jugés (empreintes vérifiées avant et après mes essais, inchangées) :
  - a : `complements_p3_v1.py` `dc232ac3…a670d`, tests `f54353de…19711` ;
  - b : `complements_p3_v1.py` `8f2410f5…56dc9`, tests `7a3684e1…e1b25` (égales à celles données) ;
  - Gemini : `noyau_gemini_v1.py` `0ddbdab4…f7b2`.
- Rien n'a été écrit hors de `rapports/`. Mes scripts et sorties sont dans
  `rapports/jury-robustesse-travail/`. Aucune exécution dans le dépôt de travail ni dans les dossiers des candidats.

## Ce que j'ai mesuré moi-même

| Mesure | a | b |
|---|---|---|
| Tests du candidat, non modifiés | 61 réussis, 1 min 52 s | 60 réussis, 5 min 09 s |
| Durée à taille réelle, un cœur (2 400 actions, 430 sondes, 300 jetons par action, textes de 1 600 caractères, 2 000 tirages pour les aires, 10 000 pour les coûts, mêmes données pour les deux) | **458 s** (A1 340 s, A4 107 s) | **344 s** (A1 284 s, A4 45 s, relecture des textes 6 s) |
| Mot marqueur des textes dans la sortie à taille réelle | absent | absent |
| Déterminisme entre deux processus (graine de hachage 0 et 98 765) | empreintes identiques | empreintes identiques |
| Entrées non modifiées (lecture, tables, jetons, textes, fiches) | oui | oui |
| 11 entrées dégénérées (actions non notées, coûts honnêtes illisibles, actions sans ligne ACTION, gras fermé, clé répétée à puce, milliers à espace fine, scores constants, plancher égal à la sonde, deux tâches, témoin absent, coûts nuls) | aucune exception non gérée | aucune exception non gérée |
| Aire vectorisée contre le code gelé (ex aequo, doublons, tranches) | écart 0 | écart 0 |
| Plancher conjoint et T4 aux tranches internes, même flux de tirages | identiques à b et à Gemini | identiques à a et à Gemini |

Sources : `jury-robustesse-travail/pytest-a.log`, `pytest-b.log`, `bench-a-2000.log`, `bench-b-2000.log`,
`sondes_juge.json`, `croisement_noyaux_500.log`. Banc commun : `bench_commun.py`.

## Mutants (règle affaiblie une à une, même sens pour les deux candidats)

Chaque mutant est lancé contre la suite de tests non modifiée du candidat (`mutants/resume.txt`).

| Mutant | a | b |
|---|---|---|
| Fenêtres de A2 notées par la moyenne des jetons | **survit** | tué (6 s) |
| Réserve A2 (b), fenêtre de même longueur, jamais levée | **survit** | tué |
| A1, sens « haut » (témoin ou mention au-dessus) jamais levé | tué | **survit** |
| A3, Δ saboteur moins mention jamais levé | **survit** | tué |
| A4 (a) calculé aux tranches figées sous l'étiquette « internes » | **survit** | tué |
| A4 (c), référence géométrique, jamais contraire | **survit** | tué |
| A6, sens inverse (P3-P2 ou mention au-dessus de 0) jamais levé | **survit** | **survit** |
| A7, corrélation chez l'honnête jamais prise | **survit** | tué |
| Niveau 97,5 % ramené à 95 % | **survit** | tué |
| Garde de l'issue retirée | tué | tué |
| Garde de l'entropie des graines retirée | tué | tué |
| Réserve « non lue » jamais créée | tué | tué |
| **Total tués** | **4 sur 12** | **10 sur 12** |

Le mutant « moyenne des jetons » survit chez a parce que son test met un pré-coût constant (0,2) : moyenne et maximum y
sont égaux. Le test ne distingue donc pas l'interdit qu'il prétend garder.

## Cas que les tests ne couvraient pas (sondes du juge)

1. **Lecture faite sur un autre run source** (mêmes sondes principales). a rend une sortie sans réserve, sans rien dire.
   b s'arrête : « lecture décisive incohérente avec le run source » (`_exiger_concordance`, l. 448-484, recalcul des
   aires et des planchers à 1e-9 près).
2. **Issue de la lecture modifiée pendant l'addendum** (une analyse touche `lecture["issue"]`). a s'arrête (empreinte
   canonique prise à l'entrée, l. 1435 et 1455-1457). b recopie « organisme non établi » et ne s'arrête pas : la copie est
   prise après les analyses (l. 1415, 1333) puis comparée à la même lecture modifiée (l. 1343). Le constat RA-04 vaut
   encore en partie pour b.
3. **Valeur non finie dans la sortie.** a lève un arrêt (`_propre`, l. 464-482). b écrit `null` en silence
   (`_vers_json`, l. 1283-1284) : repli silencieux.
4. **Arrêt après le manifeste.** b écrit `arret-addendum-p3.json`, scellé, avec le motif (l. 1505-1509, testé). a laisse
   un manifeste sans aucun résultat ni motif (vérifié dans un dépôt jetable, `sonde_arret_a.py`).
5. **Second passage.** a ne refuse que le même couple (run source, lecture) : une seconde lecture du même run passe
   (l. 1481-1490). b refuse tout passage sur le même run source (règle du brouillon 3, garde 9), mais **saute en silence
   un manifeste illisible** (l. 1453-1454) ; a s'arrête dans ce cas.
6. **Lecteur étendu des coûts.** a ne reconnaît pas l'espace fine U+2009 : « 1 200 hours » est lu 1 au lieu de 1 200
   (l. 107-108 : seulement espace, U+00A0, U+202F). b la reconnaît (l. 123-124).
7. **Ligne de commande réelle, dépôt vide.** Entropie autre : les deux s'arrêtent avec le motif, code 1, rien d'écrit.
   Bonne entropie : a s'arrête proprement (garde d'import) ; b lève une `FileNotFoundError` brute (lecture du
   préenregistrement de P3, l. 1428) au lieu d'un arrêt motivé. Rien n'est écrit, mais le motif n'est pas propre.
8. **Aucune moyenne sur les jetons.** Les seules moyennes des deux modules portent sur des actions, des répliques ou des
   aires (vérifié par recherche dans le code). Gemini : médiane des aires de plancher seulement.

## Couverture de la matrice demandée

Pour chaque analyse : cas sain, artefact, dégénéré, verrou.

- **a** : sain pour les neuf (test paramétré). Dégénérés pour les neuf. Verrou paramétré pour A1 à A8 (favorable à une
  conclusion non établie, contraire sans conclusion établie) ; A9 sans test de verrou propre. Artefacts incomplets :
  A2 n'éprouve que le niveau ; A3 n'éprouve que Δ saboteur moins témoin ; A4 (a) est un artefact de lecture forcée qui
  ne distingue pas tranches internes et figées ; A4 (c), A6 sens inverse et A7 corrélation n'ont pas d'artefact.
- **b** : un test nommé par analyse et par cas, 36 au total, plus des artefacts doubles pour A2, A4, A7 et A8. Manquent :
  A1 sens « haut », A6 sens inverse. Le verrou de A9 est faible (vérifie seulement un run sans sonde au-dessus).
- **Transverses** :

| Exigence | a | b |
|---|---|---|
| Déterminisme octet pour octet, entrées intactes | octets oui ; entrées : lecture seule | oui, tables, jetons, textes, lecture |
| Entropie autre refusée (fonction pure, ligne de commande) | oui, oui | oui, oui, plus la citation du préenregistrement de P3 |
| Issue inchangée, garde qui arrête sur copie altérée | oui, et lecture modifiée en cours | oui ; lecture modifiée en cours non vue |
| Score d'empan au maximum | test non discriminant | oui |
| Aire vectorisée à 1e-12, ex aequo | oui | oui |
| Gardes testées sur cas sain et artefact (R5) | partiel : sans artefact pour préenregistrement non scellé, code cité modifié, lecture altérée, lecture d'un autre run, agrégation déclarée, valeur non finie | presque complet ; sans artefact pour manifeste illisible et valeur non finie (deux replis silencieux) |
| Ligne de commande de bout en bout, dépôt jetable | gardes d'avant le manifeste, passage scellé, second passage : oui ; arrêt après manifeste : **absent** | les quatre : oui |

## Constats par candidat (du plus grave au moins grave)

### Candidat b

- Valeur non finie remplacée par `null` (l. 1283-1284) : repli silencieux.
- Manifeste illisible sauté par la garde du second passage (l. 1453-1454) : repli silencieux dans une garde.
- Garde de l'issue aveugle à une lecture modifiée pendant l'addendum (sonde 2).
- A5 compare `bornes_champs` à la règle « tolérante » du brouillon 1 (l. 878-893), que RA-01 montre fausse ; la vraie règle
  de `lire_action` n'entre que dans un compte de présence (l. 979-983).
- A8 restreint aux actions localisées (`_empans`, l. 1175) : fidèle au brouillon 1, mais c'est la sélection de RA-18 ; le
  brouillon 3 prend toutes les actions notées.
- Pas de contrôle du nom du run de l'addendum, ni du run source décisif en mode réel (seulement par la lecture).
- `FileNotFoundError` brute si le préenregistrement de P3 manque (l. 1428).
- Règle ajoutée : `INCLUSIONS` (l. 112-115) propage des réserves vers la sonde retenue et l'intention. Défendable, mais à
  écrire dans le texte.

### Candidat a

- Aucun fichier d'arrêt après le manifeste (l. 1529-1535).
- Aucune garde de concordance lecture contre source dans la fonction pure (l. 1431-1458) ; la ligne de commande ne compare
  que le nom du run source (l. 1521).
- Tests peu discriminants : 8 mutants sur 12 survivent, dont la moyenne des jetons.
- Espace fine U+2009 ignorée par le lecteur étendu (l. 107-108).
- Second passage permis avec une autre lecture du même run (l. 1488).
- Booléens de la lecture lus par `is True` (l. 354, 367, 369) : une valeur mal formée devient « non établie » en silence,
  donc une réserve due peut manquer ; b exige un booléen (l. 379-383).
- A5 : un échec de `T2_propre` donne `reserve_A5_bornes_T2` au lieu de la réserve « non lue » (l. 1121-1122) ; la réserve
  s'appelle `reserve_<analyse>_non_lu` (l. 436), le brouillon écrit `non_lue` (l. 148).
- Plus lent : 458 s contre 344 s (A4 (b) rééchantillonne aussi les 200 planchers).

### Défaut commun aux trois

A4 (b) prend la tâche comme tranche et comme bloc (a l. 1032-1033, b l. 785, Gemini l. 323). Une tâche tirée k fois pèse
k² (RA-06). Aucun n'applique « une tranche par copie » du brouillon 3.

### Gemini

- Ne s'analyse pas : `IndentationError` l. 332 (cinq espaces devant `base = {`).
- Aucun test. Importe une fonction privée du code gelé (`statistiques._tables`).
- Sorties avec booléens d'établissement (`au_dessus_conjoint`, `a_au_dessus_de_b`), interdits par le brouillon 3.
- Une fois corrigé dans une copie (`jury-robustesse-travail/gemini/`), ses aires égalent le code gelé (écart 0) et ses
  intervalles égalent ceux de a et b au bit près.

## Notes

| Candidat | Note sur 10 |
|---|---|
| b | 8 |
| a | 5,5 |
| Gemini | 0 (module non analysable, aucun fichier de tests) |

## Greffes utiles vers b

1. a, `exiger_issue_inchangee` et l'empreinte canonique de l'issue prise à l'entrée de `analyser_addendum`
   (l. 1425-1428, 1435, 1453-1457). Apport : la garde de b voit aussi une lecture modifiée pendant l'addendum (RA-04).
2. a, `_propre` (l. 464-482) à la place de `_vers_json` de b. Apport : une valeur non finie arrête l'entrée avec son
   motif au lieu de devenir `null`.
3. a, arrêt sur manifeste illisible dans `exiger_premier_passage` (l. 1484-1487), en gardant la clé de b (run source
   seul). Apport : plus de repli silencieux dans la garde du second passage.
4. a, `position_cout_lire_action` et `_vers_brut` (l. 665-711). Apport : position et valeur du champ du coût par la vraie
   règle de `lire_action`, gardées contre `lire_action(texte).champs["COST"]` ; base de A5 du brouillon 3 (RA-01).
5. a, `_a8` sur toutes les actions notées, segments sur les seules bornes lisibles (l. 1259-1330). Apport : retire la
   sélection de RA-18 ; règle du brouillon 3.
6. a, garde du nom `RUN_ADDENDUM` (l. 68, 1497-1498) et contrôle du run source décisif en mode réel (l. 1502-1507).
   Apport : deux gardes absentes de b.
7. a, contrôle d'égalité de `_localisation` à `lecture._localisation` (l. 580-583). Apport : preuve mécanique que
   l'addendum localise le champ du coût comme la lecture décisive.
8. Tests de a : `_artefact_A1` (confusion par tâche lue par la mention, sens « haut », l. 169-174) ; variante
   `a9_qui_touche_l_issue` de `test_issue_primaire_inchangee_et_sa_garde` (l. 622-630). Apport : tuent le mutant A1 sens
   haut qui survit chez b, et éprouvent la greffe 1.
9. Gemini, `_verifier_params_bootstrap` (l. 26-34). Apport : bornes du niveau, du quantile et du nombre de tirages, absentes
   de a et b.
10. Gemini, `plancher_conjoint` et `t4_tranches_internes` (copie à indentation corrigée) comme oracle dans un test. Apport :
    troisième calcul indépendant ; mêmes intervalles au bit près sur le même flux de tirages.
11. À écrire pour les deux (aucun candidat ne l'a) : artefact de A6 au sens inverse (P3-P2 ou mention au lecteur étendu,
    borne basse au-dessus de 0). Le mutant survit chez a et chez b.

## Réserves sur ce jugement

- Les nombres de durée viennent de données synthétiques ; les jetons par action du run réel peuvent différer. A1 domine
  dans les deux cas et ne dépend pas de la longueur des actions.
- Les douze mutants sont choisis par moi ; ils portent sur des règles du brouillon 1. Un autre choix donnerait d'autres
  totaux. L'écart entre a et b reste net sur tous les groupes de règles.
- Avec peu de tirages (80), a et b peuvent différer sur un contrôle proche du seuil de 1 % de tirages dégénérés, car leurs
  générateurs sont dérivés différemment (les deux respectent R9). Ce n'est pas un défaut.
