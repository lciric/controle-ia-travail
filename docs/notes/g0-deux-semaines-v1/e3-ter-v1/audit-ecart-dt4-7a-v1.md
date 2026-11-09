# Audit de l'écart DT-4 de la course 7a (décision (b) de Lazar, R-2048) — v1

> **Limite imposée (brief de Lazar du 9 novembre, 21:5x UTC).** Personne n'ouvre `lecture-sondes-t06.json` ni la branche de quarantaine `donnees/lecture-b-7a-quarantaine-v1` avant le verdict scellé de P3-bis. Cet audit est donc **structurel et par catégories** : chemins, commits, empreintes, lignes ajoutées, différentiel r2 → r3, éléments C1 à C7 décrits par R-2041. Il **ne compare aucune valeur** du fichier des sondes ni de la lecture B au texte de `main`. Ce que cette limite laisse ouvert, et ce qu'il faudrait pour le fermer, est écrit à la section « Ce qui reste ouvert ».

## En-tête

- **Qui** : sous-agent auditeur neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (Claude Opus 5.5). Avant cette tâche, il n'avait écrit ni lu aucune pièce de T0.6, T0.7, P3-bis ni de 7a. Après cet audit, il n'a aucun rôle sur T0.6, T0.7, P3-bis ni G0.
- **Quand** (`date -u`) : début le 9 novembre 2026 à 22:02:42 UTC, sortie définitive du script à 22:21:48 UTC, rapport achevé vers 22:25 UTC.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/consigne-audit-ecart-dt4-7a-v1.md`. Empreinte vérifiée avant toute lecture : `ca5024ae6ba71314a87918f3a9ae68fc40584ac10d75962b83e7f22fbbe9fe79`, conforme. Interdits communs : `851028fc…`, compagnon conforme.
- **Dépôt** : clone `/home/user/controle-ia-travail`, `main` local à `61607820` au début (le commit des consignes de cette série, après `6886b61e`). Pendant l'audit, la mère a ajouté `62ba4a4a` (R-2052, 22:03 UTC). Le script lit des références explicites (`6886b61e`, `61607820`, `8cb539f9`, `fe240b24`, `1609a4bf`, `9b7721c7`) : les sorties ne dépendent pas de l'arbre de travail.
- **Couvert** : la plage `9b7721c7..6886b61e` (13 commits) ; les pièces nommées au point 4 de la consigne ; en complément, les commits `61607820` (consignes) et `62ba4a4a` (R-2052).

## Verdict (une ligne)

**« Aucune trace trouvée »** du fichier des sondes de 7a ni d'un élément C1 à C7 de la lecture B sur `main`, chez le rédacteur de la r3 ou chez un contre-lecteur (0 occurrence classée (iii) sur 448, 0 décimal inexpliqué). **Un point est « indéterminé », hors des catégories C1 à C7** : on ne sait pas d'où viennent les grandeurs de coût de 7a que la mère a transmises au rédacteur de la r3. Elles ne figurent pas dans la lecture A, et l'ordre de 7a (§ 4 B) range le coût dans la lecture B (constat 6).

## Constats

1. **Chemins (contrôle 1).** Les 13 commits de `9b7721c7..6886b61e` ajoutent 14 fichiers, en modifient 15 et n'en suppriment aucun. **Aucun chemin** ne correspond à `lecture-sondes*`, à `diag/20261109-070232-t06-reel/`, à `runs/20261109-070232-t06-reel/` ni à un nom de la lecture B. L'arbre de `6886b61e` compte 17 518 noms, dont aucun de ces motifs (noms seuls, aucun fichier ouvert). Le seul fichier de `main` qui porte l'identifiant du run 7a est la sortie de l'extracteur de garde de la lecture A (`…/lecture-7a-v1/garde-equivalence-20261109-070232-t06-reel-exploratoire-non-opposable-r522.json`), pièce permise.
2. **Noms et empreintes de B.** Je les ai cherchés dans R-2040, R-2041 et les messages des 13 commits (dont `39f17d33` et `e712f61a`) : **aucun n'y figure**. R-2040 et R-2041 ne citent que la lecture A et sa sortie (empreintes résolues sur ces deux fichiers), le nom de l'extracteur des mesures et son empreinte (`9a67b7b9…`, vérifiée sur `1609a4bf`), le chemin du fichier des sondes, la branche de quarantaine et le commit `e6c06113`. Les messages de commit ne citent aucun chemin. Seul le motif « lecture B » apparaît dans deux sujets (`39f17d33`, `e712f61a`), comme description de l'écart (classe (i)). La vérification des empreintes de B dans l'arbre est donc **sans objet**. À sa place, j'ai comparé l'**empreinte du fichier des sondes**, déclarée à la ligne 16 de la lecture A (compagnon de la chaîne), aux 29 fichiers écrits par la plage : **0 correspondance**. La base `9b7721c7` (18:37 UTC) précède la fin de 7a (20:00 UTC) : un fichier que la plage n'a pas touché ne peut pas être une copie d'une sortie de 7a.
3. **Commit de quarantaine (contrôle 2).** Aucun des 13 commits ne commence par `e6c06113`. Ce commit est absent du clone, tout comme la tête de 7a (`34ee8663`). Le clone n'a aucune référence des branches interdites : ses références sont `main`, `origin/main`, `origin/prep/scellement-course-t06-v1`, `origin/prep/t06-lanceur-v2` et `origin/prep/t06-ordre-course-v2`.
4. **Catégories (contrôles 3 et 4).** 448 occurrences au total, dont certaines sont comptées dans plusieurs sources : 195 sur les lignes ajoutées par les commits, 238 sur le texte entier des pièces, 15 sur le différentiel r2 → r3. Par catégorie : C1 125, C2 97, C3 3, C4 138, C5 48, C6 47, C7 20, X (mention du fichier ou de B) 60. Classement :
   - (i), description de l'écart ou nom d'un fichier interdit : **48** ;
   - (ii), conception antérieure ou indépendante des résultats : **342**, dont 288 lignes et 16 contextes identiques à un texte antérieur à la base (mécanique) ;
   - (ii-A), grandeur de 7a dont la source sur `main` est la lecture A : **53** ;
   - (ii-B), grandeur de coût de 7a de source non établie : **5**, soit les lignes 616 de la r3 et 452 du journal, comptées par source ;
   - **(iii) : 0**.

   Les classes (ii-A) touchent C4, C2 et C5 par leurs mots : couche d'activation de la garde d'équivalence (couches 7, 15, 23 de la configuration), « au-dessus » de la tolérance de la garde ou de l'estimation de mémoire, durée totale de l'étape « couples descriptifs » relevée dans le journal. Ce ne sont ni des sondes, ni des aires, ni des durées par couple. Le détail, avec chemin, ligne, catégories, classement et raison, est dans la sortie JSON.
5. **Décimaux entre 0 et 1 (contrôle 3 bis, ajouté pour réduire la limite).** Une aire ou une borne recopiée sans mot-clé échapperait aux motifs. Le script relève donc tout décimal entre 0 et 1 qui ne figure pas, avec son contexte, dans un texte antérieur. Résultat : 200 lignes, toutes expliquées, **0 à examiner**. Explications : 166 lignes de valeurs de la lecture A ou de sa sortie de garde, 16 lignes de devis (prix, heures de la lecture A, dépense estimée par la fille), 8 lignes de configuration (fraction, seuils et doses fixés avant 7a), 10 lignes de grandeurs de coût de la classe (ii-B) avec leur arithmétique et les valeurs du plan de la r2 (antérieures à 7a, vérifiées dans la r2).
6. **Rédacteur de la r3 (point 6).** D'après son journal (l. 3, 8, 392) et R-2046, il a reçu ou lu :
   - la lecture A ;
   - des « grandeurs de coût reçues de la session mère » ;
   - le champ `graines[*].entropie` du manifeste de 7a. Il l'a lu lui-même sur la branche `essai/t06-explo-v3`, hors consigne, et l'a déclaré (passation, § 5).

   Il déclare n'avoir lu ni `diag/` de 7a, ni `lecture-sondes-t06.json`, ni la lecture B ou sa branche. Différentiel r2 → r3 : 83 lignes ajoutées ou remplacées, 15 occurrences : 4 (i), 9 (ii), 1 (ii-A), 1 (ii-B), **0 (iii) : aucun élément C1 à C7 de 7a**. La r3 n'affirme pas « 7a jamais lue par une sonde ». Son marqueur `DECISION_LAZAR_ECART_DT4_R2041` reste à remplir.

   **Constat (ii-B), source indéterminée.** La r3 (l. 349, 616) et son journal (l. 392, 417, 452) portent des grandeurs de coût de 7a qui ne figurent **ni dans la lecture A, ni dans sa sortie de garde** :
   - nombre d'actions au coût lisible par condition ;
   - écart type par tâche de la différence appariée du coût ;
   - demi-largeur de l'intervalle à 95 % ;
   - nombre de tirages et de permutations ;
   - taux de troncature du saboteur instruit à dose 0 ;
   - rapport du compteur `jetons_generes`.

   Aucune n'entre dans C1 à C7. Leur source ne s'établit pas sur `main`, pour quatre raisons :
   - l'ordre de 7a (§ 4 B, `4c6c70d4…`) range le « coût par condition » dans la **lecture B**, et sa section § 7 interdit B à la fille (son compte rendu ne porte que les comptes A) ;
   - R-2041 dit que le rédacteur reçoit « les seules grandeurs de coût du compte rendu » sans dire de quel compte rendu il s'agit ;
   - aucune consigne de la mère sortante au lecteur de 7a ni au rédacteur n'est dans le dépôt ;
   - la passation (§ 2.1) atteste que ces consignes ne contenaient « aucune valeur ni élément de B ».

   Si ces grandeurs viennent du compte rendu du lecteur exposé sur son volet B, un élément de la lecture B (le volet coût, pas les sondes) a atteint un rédacteur et `main` (commit `4d77dfae`). L'ordre de 7a (§ 9.2) prévoyait cet usage pour la puissance (« d'après les heures et les variances »). Il contredit pourtant la lettre de R-2048 (« rien de la lecture B »). L'une de ces grandeurs, les troncatures, a en outre ajouté une ligne de rapport au plan d'analyse (r3, l. 499 ; journal, X19). Aucun seuil n'a changé, mais c'est à regarder à la contre-lecture 3.
7. **Lecture A (point 5).**
   - **Même lecteur que B** : oui (R-2039 « lectures A puis B confiées à un lecteur neuf » ; R-2040 et R-2041).
   - **Ordre** : l'en-tête de A déclare l'extraction à 20:15:09 UTC et l'écriture à 20:16 UTC, après la remise de A puis B au lecteur (R-2039, `a4d504a8`, 20:13:48 UTC). L'exposition au fichier des sondes a eu lieu pendant B, avant R-2040 (20:23 UTC). A a été commitée à `39f17d33` (20:23:42 UTC), **après** l'exposition. Aucune empreinte de A n'est horodatée avant cette exposition. L'ordre « A écrite avant d'avoir vu le fichier » ne repose donc que sur les heures déclarées par le lecteur : **réserve**.
   - **Contenu** : 9 occurrences dans A (3 (ii), 6 (ii-A)), 19 dans sa sortie JSON (1 (ii), 18 (ii-A)), 0 (iii) ; tous ses décimaux sont expliqués. Le fichier des sondes n'y apparaît que par son **empreinte sha256** (l. 16, compagnon vérifié), qui n'en livre aucun contenu.
   - **Sortie JSON** : elle vient de `scripts/extraire_garde_equivalence_t06_v1.py` (`6c6f659d…`, sur `main`). D'après son code, ce script ne lit que `manifeste.json`, `episodes-t06.json`, `distillation-t06.json`, `arret.json` et le compagnon du manifeste, **jamais** le fichier des sondes.
   - **Extracteur des mesures** (`scripts/extraire_mesures_epreuve_t06_v1.py` au commit `1609a4bf`, `9a67b7b9…` vérifiée) : **il ouvre et charge en entier** `lecture-sondes-t06.json` (l. 34). Il en imprime les vérifications et le calcul de Mahalanobis (`verifications_mahalanobis`, `mahalanobis_calcul`, `egalite_jetons_reels`, l. 40-42 et 57-58) et les **durées par couple** (`durees_s`, l. 59). Il n'accède à aucune clé d'aire, d'état de jeu, de table ni de plancher : la phrase de R-2040 « ne lit jamais les aires (liste blanche) » est exacte pour les aires. Elle ne veut pas dire que le fichier des sondes n'est pas lu, puisque l'extracteur en tire exactement l'élément C5 de B. L'ordre (§ 4 B) confiait cet extracteur à la lecture B ; A ne cite aucune sortie de cet extracteur.
8. **Session mère sortante (point 7).** Son attestation est consignée **comme attestation** : consignes sans valeur ni élément de B, fichiers interdits nommés, aucune valeur vue (passation `2026-11-09-2117.md`, § 2.1 ; R-2041). Le dépôt montre ce qui suit :
   - R-2040, R-2041 et R-2048 décrivent l'écart en catégories sans valeur (classe (i)) ;
   - R-2041 reconnaît une faute de la mère : sa consigne au lecteur ne rappelait pas DT-4 ;
   - ses consignes au lecteur et au rédacteur ne sont pas dans le dépôt, ce qui empêche de vérifier l'attestation au-delà des registres ;
   - elle a vu les grandeurs de coût du constat 6 et les a transmises (journal de la r3, l. 392). Ce ne sont pas des valeurs de sonde.
9. **Contre-lecteurs (point 8).**
   - **Contre-lecture 2** (`contre-lecture-t06-course-v2-v1.md`, `09c202e6…`) : écrite le 8 novembre de 09:07:08 à 10:01 UTC, commitée à `eec40bf2` (8 novembre, 10:24:44 UTC), ancêtre de la base et inchangée depuis. Elle est **antérieure à 7a**, créée le 9 novembre (amorce à 06:26 UTC). Ses 11 occurrences sont classées (ii) par antériorité.
   - **Contre-lecture de la règle E3-6** (`…-cl1.md`, `f41b55f0…`, Fable 5.1) : écrite à 19:05 UTC sur `main` `9b7721c7`, commitée à `047342c2` (19:10 UTC), avant la fin de 7a. Elle déclare n'avoir lu aucun `diag/` ni aucune branche d'essai. Ses 4 occurrences sont (ii) et ses décimaux relèvent de la configuration.
   - **Contre-lecture 3 de la r3 et dossier (ii-b)** : ils n'existaient pas au début de l'audit. Des fichiers non suivis de ces deux chantiers sont apparus dans l'arbre de travail pendant l'audit (`prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3*`, `brouillons/ii-b-saboteur-budget-v1/`). **Je ne les ai pas lus** : ils relèvent du complément.
10. **Consignes de cette série et brief.**
    - **Quatre consignes** (`61607820`) : 13 occurrences, 10 (i) et 3 (ii), 0 (iii) ; elles ne contiennent **aucune valeur ni élément de B**. Leurs seuls nombres tirés de 7a viennent de la lecture A (heures, mémoire). Chacune nomme les quatre interdits attendus : `diag/20261109-070232-t06-reel/lecture-sondes-t06.json`, `diag/*/lecture-sondes-t06.json`, `donnees/lecture-b-7a-quarantaine-v1` et `essai/t06-explo-v3`.
    - **Brief de reprise** (`424431b9…`) : il nomme `diag/*/lecture-sondes-t06.json` et la branche de quarantaine, mais ni le chemin nommé du run 7a ni `essai/t06-explo-v3`. Sans conséquence, puisque les consignes de la nouvelle mère les nomment.
    - **Complément `62ba4a4a`** (R-2052, rejoué hors de la plage) : 2 commits, 10 fichiers, 0 chemin interdit, 40 occurrences (12 (i), 28 (ii), 0 (iii)), aucun décimal sans antériorité.
11. **Épreuves du script (R5).** Je les ai faites sur un dépôt factice dans le bloc-notes :
    - cas sain : 0 occurrence, 0 chemin interdit ;
    - cas piégé : 3 chemins interdits signalés et **jamais lus**, empreinte interdite retrouvée, préfixe de quarantaine retrouvé, motif neuf « à classer » ;
    - décimal nu sans mot-clé : « à examiner » ;
    - lecture d'un chemin interdit refusée avant tout appel à git ;
    - contexte modifié ou valeur ajoutée près d'un mot-clé : « à classer », jamais (ii).

## Réserves

1. **Limite structurelle.** Sans comparaison de valeurs, un contenu de B ou du fichier des sondes transcrit sans aucun des mots-clés, et sous une autre forme qu'un décimal entre 0 et 1, échapperait au contrôle. Exemples : un rang, un nom de sonde ou un entier. Les motifs couvrent le français, l'anglais et les clés en tirets bas.
2. **Ordre A/B non établi** (constat 7) : seules comptent les heures déclarées par le lecteur ; A est commitée après l'exposition. Son contenu est sans élément C1 à C7.
3. **Attestations.** Ce qui suit est déclaré et non vérifiable dans le dépôt :
   - le lecteur (en-tête de A) ;
   - le rédacteur de la r3 (journal, l. 8). Il a eu accès à la branche de 7a, qui contient le fichier des sondes, pour lire le manifeste ;
   - la mère sortante (passation, § 2.1).
4. **Grandeurs de coût de source indéterminée** (constat 6).
5. **Extracteur des mesures** (constat 7) : quiconque le lance sur l'arbre de 7a (ou de 7b) avant le verdict de P3-bis lit le fichier des sondes et voit l'élément C5. La phrase de R-2040 peut induire en erreur sur ce point.
6. **Classement à la lecture** : 144 occurrences ont été classées par moi seul, avec mes raisons codées dans le script. Une contre-lecture du classement n'a pas été faite.

## Ce qui reste ouvert

1. **Complément avant le scellement de la r3** : rejouer le script sur la contre-lecture 3 et sur le dossier (ii-b), avec leurs chemins ajoutés en `--piece`, ou leur commit en fin de plage s'ils sont commités. Toute occurrence « à classer » et tout décimal « à examiner » doivent être classés par un lecteur qui n'a pas vu B.
2. **Fermer le point indéterminé (constat 6)**, deux voies :
   - **(a)** retrouver, sans ouvrir B, quel compte rendu la mère sortante a transmis au rédacteur. Sa session est arrêtée : seul Lazar peut le savoir ;
   - **(b)** faire une **comparaison mécanique aveugle**, qui demande un mot de Lazar (le brief interdit d'ouvrir B et le fichier des sondes avant le verdict de P3-bis). Un script lancé par un agent qui ne lit pas sa propre entrée chercherait les nombres et les noms de clés de `lecture-sondes-t06.json` et de la lecture B dans les textes de `main` ajoutés depuis `9b7721c7`, dans la r3, la contre-lecture 3 et (ii-b). Il n'écrirait que des comptes de correspondances par fichier et par ligne. La même comparaison dirait si les grandeurs de coût de la r3 figurent dans B.
3. **Extracteur des mesures** : le nommer parmi les outils interdits sur les arbres de 7a et de 7b jusqu'au verdict de P3-bis, dans l'ordre de 7b et dans toute consigne de lecture d'un `diag/`.
4. **T0.6 r3** : remplir `DECISION_LAZAR_ECART_DT4_R2041` par renvoi à R-2048 et à ce rapport ; la contre-lecture 3 peut regarder l'ajout X19 (troncatures).
5. **T0.7** : déclarer l'écart DT-4 (R-2048), hors du champ de cet audit.

## Script, commande exacte, sorties

- **Script** : `docs/notes/g0-deux-semaines-v1/e3-ter-v1/audit-ecart-dt4-7a-v1/verifier_ecart_dt4_v1.py`. Bibliothèque standard, aucun réseau. Il n'écrit que des comptes, chemins, numéros de ligne, identifiants de commit, catégories et classements.
- **Sortie** : `docs/notes/g0-deux-semaines-v1/e3-ter-v1/audit-ecart-dt4-7a-v1/sortie-verifier-ecart-dt4-v1.json`.
- **Commande** (depuis la racine du dépôt). `EMP` est l'empreinte à 64 caractères hexadécimaux de la ligne 16 de la lecture A, extraite par `git show 6886b61e:<lecture A> | sed -n 16p | grep -oE '[0-9a-f]{64}'` :

```
D=docs/notes/g0-deux-semaines-v1; A=$D/e3-ter-v1/audit-ecart-dt4-7a-v1; L=$D/e3-ter-v1/lecture-7a-v1
C=$D/consignes-mere-2026-11-09-2200-v1; S=$D/scellement-course-t06-v1
python3 -I -B $A/verifier_ecart_dt4_v1.py --depot . --plage 9b7721c7..6886b61e \
  --piece 6886b61e:brouillons/T0.6-organismes-v0-v1-candidat12-r3.md \
  --piece 6886b61e:brouillons/T0.6-organismes-v0-v1-candidat12-r3-journal-v1.md \
  --piece 6886b61e:$L/lecture-A-exploratoire-non-opposable-v1.md \
  --piece 6886b61e:$L/garde-equivalence-20261109-070232-t06-reel-exploratoire-non-opposable-r522.json \
  --piece '6886b61e:registres/decisions.md#R-2037..R-2051' --piece '6886b61e:registres/etat.md#entete' \
  --piece 6886b61e:registres/passations/2026-11-09-2117.md \
  --piece 6886b61e:docs/procedures/brief-reprise-nouvelle-mere-2026-11-09-v1.md \
  --piece 61607820:$C/interdits-communs-v1.md --piece 61607820:$C/consigne-audit-ecart-dt4-7a-v1.md \
  --piece 61607820:$C/consigne-contre-lecture-3-t06-candidat12-r3-v1.md \
  --piece 61607820:$C/consigne-conception-ii-b-saboteur-budget-v1.md \
  --piece 6886b61e:$D/contre-lecture-t06-course-v2/contre-lecture-t06-course-v2-v1.md \
  --differentiel 8cb539f9:brouillons/T0.6-organismes-v0-v1-candidat12-r2.md 6886b61e:brouillons/T0.6-organismes-v0-v1-candidat12-r3.md \
  --anterieur 8cb539f9:brouillons/T0.6-organismes-v0-v1-candidat12-r2.md \
  --anterieur fe240b24:$S/pieces-apres-couples/T0.6-organismes-v0-v1-candidat12-r2-apres-couples-v1.md \
  --anterieur fe240b24:$S/rapport-preparation-scellement-course-t06-v1.md \
  --anterieur 9b7721c7:registres/decisions.md --anterieur 9b7721c7:registres/etat.md \
  --anterieur 9b7721c7:registres/passations/2026-11-09-1829.md \
  --anterieur 9b7721c7:$D/e3-ter-v1/ordre-course-dose-reponse-exploratoire-v1-brouillon3.md \
  --anterieur 9b7721c7:$D/contre-lecture-t06-course-v2/contre-lecture-t06-course-v2-v1.md \
  --anterieur 9b7721c7:$D/contre-lecture-t06-course-v2/couples-candidat12-r2-v1.json \
  --empreinte-interdite "$EMP" --chercher-noms-b '6886b61e:registres/decisions.md#R-2040..R-2041' \
  --commit-quarantaine e6c06113 \
  --nomme-interdits 61607820:$C/interdits-communs-v1.md --nomme-interdits 61607820:$C/consigne-audit-ecart-dt4-7a-v1.md \
  --nomme-interdits 61607820:$C/consigne-contre-lecture-3-t06-candidat12-r3-v1.md \
  --nomme-interdits 61607820:$C/consigne-conception-ii-b-saboteur-budget-v1.md \
  --nomme-interdits 6886b61e:docs/procedures/brief-reprise-nouvelle-mere-2026-11-09-v1.md \
  --sortie $A/sortie-verifier-ecart-dt4-v1.json
```

- **Complément `62ba4a4a`** (sortie non versée, rejouable) : `--plage 6886b61e..62ba4a4a --piece '62ba4a4a:registres/decisions.md#R-2052..R-2052' --piece '62ba4a4a:registres/etat.md#entete' --anterieur 6886b61e:registres/decisions.md --anterieur 6886b61e:registres/etat.md --limite-anteriorite 6886b61e`.
- **Pour le complément de la contre-lecture 3 et de (ii-b)** : même commande, plage étendue jusqu'à leur commit, `--piece` sur leurs fichiers. De nouvelles lignes classées s'ajoutent par `--classements FICHIER.json` (liste d'objets `{"ref", "chemin", "lignes", "classe", "raison"}`).

## Pièces lues, empreintes vérifiées (`sha256sum`, toutes égales aux déclarées quand une déclaration existe)

| Pièce | Empreinte |
|---|---|
| consigne d'audit (`61607820`) | `ca5024ae6ba71314a87918f3a9ae68fc40584ac10d75962b83e7f22fbbe9fe79` |
| interdits communs (`61607820`) | `851028fc2f425cee8e64613db20f6a2e2a7c289d07dd5441a9993d24630682a6` |
| consigne de la contre-lecture 3 (`61607820`) | `79c279e89f7f906fd63bc6b278ff2a3399c3c63a055ed5b3a2e161cdfa786d06` |
| consigne de (ii-b) (`61607820`) | `f56b0a5df32755b088dc397339b77fc88873630e3a3c7d23d13a5c86b35a74d5` |
| `brouillons/T0.6-organismes-v0-v1-candidat12-r3.md` | `c24e268ee9821d1f37ff612023a9f07735864614f57e3a9cf58517b05bc55331` |
| `…-candidat12-r3-journal-v1.md` | `0728c7edb6657e785757d4bd6d40395e9d3c3c3f8278d3066296d3b3aa5c638a` |
| r2, `git show 8cb539f9:brouillons/T0.6-organismes-v0-v1-candidat12-r2.md` | `0d6bf1c47f6bd282d4c4a2a7a7503c977f2068a4c02ccd2d705142f64b9b63f7` |
| r2 après couples, `fe240b24` (référence d'antériorité, lue par le script) | `7ae3d135016c0faf37dc742cb4679e6912544deac015c625ddd174ec1900f586` |
| rapport de préparation du scellement, `fe240b24` (référence, lu par le script) | `0aebc62bf6ef9bb2714c91e5fa24f0b01c911edb4d7808d333a0182ec1c09a68` |
| lecture A de 7a | `3c84c419acbdcbe605a7b1e92225d3d19caf7c4de2fbd10f5dcdf2c447156738` |
| sortie de l'extracteur de garde (lecture A) | `24ea608fe821f71d5137868ba8157d3b495fd8ca6672eb9f557a481424cf6ee1` |
| `scripts/extraire_garde_equivalence_t06_v1.py` (`main`) | `6c6f659db483916639c7d7795a11c178a9ee5d35af97f6588923f6c6367fce4d` |
| `scripts/extraire_mesures_epreuve_t06_v1.py` (`git show 1609a4bf:…`) | `9a67b7b994188e47cad966ffec20af266677c78afb2c401beb07903174435796` |
| ordre de 7a, brouillon 3 (§ 4, § 7, § 9) | `4c6c70d4e496bf2fd009cc25133a319151af600ec64065eb33903963fbda17a0` |
| contre-lecture de la règle E3-6 (cl1) | `f41b55f0be445f54741ce69ab19d59cb3f9d3ab6e8734a3d00c25f6df8eeb2cd` |
| contre-lecture 2 | `09c202e62d4cd4d9af2c0100183ac9cffb90387025d784a81eeeb1df57d13a02` |
| couples de la contre-lecture 2 (`9b7721c7`, référence, lus par le script) | `f094a8046257d9d3f87cc50de626cda5d7a15e27a727961a6a80b7ee254a59df` |
| `registres/decisions.md` à `6886b61e` (R-2037 à R-2051) ; R-2052 à `62ba4a4a` | `794ac870c595664de98a8fdfefcbc285a0e4e430177a681ca868b25acf1c60f1` |
| `registres/etat.md` à `6886b61e` (en-tête, l. 1 à 148) | `29dfa3cec57f13537e268a344359cdfe10baf18671d6c9d39832682fce2f274e` |
| `registres/passations/2026-11-09-2117.md` | `e301dc2b5d95237faa9bcefa0509865c473e6b174b9c0177f0d500c9af1d97fd` |
| `registres/passations/2026-11-09-1829.md` à `9b7721c7` (référence, lue par le script) | `c0bc858d665caa88d6e6023a8ccbcfd74ba8144d7b0cf1bbe6756e869c24db5e` |
| `docs/procedures/brief-reprise-nouvelle-mere-2026-11-09-v1.md` | `424431b98071bb230d68f8e811ed82affbdc8b2e511902ce35ed915af601b75d` |
| `registres/depenses.md` à `6886b61e` (l. 413 seulement) | `e7b83d372f4795e073bf5fda6d23bb9d74743aca9df2777c15e3186642740f1b` |
| configuration `config-t06-course-explo-v1.json` (noms de clés seuls) | `1911a9e9e78bd5108886d3f1e3f21edd28f88b82e78b9a9bcfebe9898028e734` |

## Interdits tenus

- **Jamais ouverts**, d'aucune manière (lecture, affichage, copie, script, `git show`, `git ls-tree`, `git fetch`) :
  - `diag/*/lecture-sondes-t06.json` (dont celui de 7a) ;
  - la lecture B, la branche `donnees/lecture-b-7a-quarantaine-v1` et le commit `e6c06113` ;
  - tout `diag/` et tout `runs/` de 7a, et la branche `essai/t06-explo-v3` ;
  - `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` et `docs/notes/bras-attaque/` ;
  - les items, clés et réponses de l'étiqueteur.

  Le script refuse ces chemins avant tout appel à git (épreuve faite). `git ls-tree --name-only` n'a été lancé que sur `main` (`6886b61e`, noms seuls) et, filtré, sur `1609a4bf`, comme la consigne le permet.
- **Fichiers des autres chantiers** : je n'ai lu aucun fichier de la contre-lecture 3 ni de (ii-b) apparu pendant l'audit.
- **Secrets** : aucune valeur de clé ; ni `env`, ni `printenv`, ni `set` sans argument, ni `export -p`, ni `/proc/*/environ`.
- **Appels et dépense** : aucun appel de modèle ni d'interface externe, aucune location, aucun `vastai`, aucune dépense.
- **Git** : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge` ni `rebase`, et aucune modification de l'index ; les autres commits ont été lus par `git show` ou `git cat-file`.
- **Écritures** : seulement dans les chemins de sortie, plus des fichiers temporaires dans le bloc-notes de session (dépôt factice des épreuves R5, essais, complément).
- **Essais** : pas de suite complète.
- **Refus** : aucun refus d'un contrôle de permissions ou d'un classifieur.
- **Valeurs de sonde** : ce rapport ne contient aucune valeur numérique tirée d'une sonde de 7a, et je n'en ai vu aucune.
