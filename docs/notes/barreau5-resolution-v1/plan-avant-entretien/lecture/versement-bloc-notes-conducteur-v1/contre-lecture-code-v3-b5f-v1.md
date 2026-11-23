# Contre-lecture du code v3 du barreau 5 (commande de la relecture v3, ouverture à noms suffixés v1) — v1

Écrite le 23 novembre 2026 par un contre-lecteur neuf (Claude Opus 5.5, classe B), sous-agent du conducteur de la lecture du barreau 5. Je suis dans les exclusions du point 7 (a). Consigne de nuit : rien de payant, rien commité, rien poussé.

**Objet** : le commit `9e682f0e0359ddde31fdf1bf1eae4a9e1e2acb5b` (branche `course/barreau5-commande-lecture-v3`, parent `5402367e`).

**Pièce** : l'erratum de chaîne v2, `01298f0f…`, recalculé à l'octet sur `conducteur-b5f/lecture-v1`. Je l'ai lu avec sa vérification (`08fd3453…`, trois précisions) et le rapport du développeur (`b019f212…`, recalculé).

## Verdict

**Conforme après corrections.** Aucune correction ne touche la règle ni le comportement du code sur une entrée saine. Il faut :
- deux essais de plus, pour fermer des trous d'essai (constats 1 et 2) ;
- une décision du conducteur sur la parité complète (constat 3).

Je n'ai trouvé aucun défaut de conformité dans les deux modules, ni aucune garde figée affaiblie.

## Ce que j'ai vérifié

### Le commit

- **Liste fermée.** `git diff --raw 5402367e 9e682f0e` donne exactement sept lignes « A », toutes en mode 100644. Ce sont les sept fichiers du § 4.3 (a). Les empreintes des sept fichiers sont égales à celles du rapport.
- **Fichiers figés inchangés.** `lecture_v1.py`, `engagement_v1.py`, `relecture_v1.py` et l'amorce sont égaux à ceux de `c76e79169` (`git diff --quiet`). Aucun fichier de la v2 n'est modifié.

### L'amorce embarquée

`amorce_corrigee(amorce figée 54a676f3…)` donne :
- sha256 `0adb6efba0a430f11c30e01da52787ef0482e20f6d74f699dbe8d76d2d300001` ;
- 33 536 octets et 405 lignes, fin de ligne LF, aucun CR ;
- par `diff`, une seule ligne ajoutée après la l. 362, la ligne de l'erratum à la lettre (« é » composé, `C3 A9`).

### La commande v3 (`commande_lecture_v3.py`)

- **Ordre des vérifications** (§ 4.3 (e)) : (a) l. 241, puis (d), (d'), (c'1), (c'2) et (b') (l. 194 à 198). C'est l'ordre de la pièce.
- **Le corps** est celui de la v2, à deux remplacements près. Je l'ai relu contre `commande_lecture_v2.py`, l. 212 à 274, et un essai le vérifie.
- **(d') : liste fermée, colonne 1, forme composée.** La ligne d'épinglage est ignorée du lecteur figé : elle ne commence pas par « | » et ne porte pas « -B5F ».
- **(c'2)** vérifie :
  - l'ascendance ;
  - l'état « A » seulement ;
  - la liste fermée de la v3 ;
  - les modes 100644 et 100755 ;
  - la présence des deux modules et des deux lanceurs.
- **Condition d'arrêt C12** : vérifiée dans le module (l. 292) et dans le lanceur (l. 32 à 37).
- **Garde de calcul** et toutes les autres gardes de la v2 : appelées telles quelles.

### L'ouverture à noms suffixés (`ouverture_suffixes_v1.py`)

- **Rien n'a lieu avant les gardes figées sur T.**
  - Dans `variante` et `preparer` : la cohérence, puis l'engagement.
  - Dans `garde_d_ouverture` : la cohérence, `verifier_table_a_l_ouverture` (engagement et dates), puis l'égalité à `OUVERTURE-B5F`.
- **Ensuite seulement**, dans l'ordre :
  - la graphie, une graphie par base ;
  - c(base) ;
  - la décision sur T (`decider`) ;
  - T_nu ;
  - les gardes de ligne des l. 529 à 532 sur T_nu.
- **La copie lue c(base) se calcule base par base** (précision 3) :
  - dans `variante` et `preparer`, par `_familles_formees(racine_formation, base, relance)` (l. 197 à 199), récrite à l'identique ;
  - dans `ouvrir`, au champ « copie » du résumé, contrôlé par `exiger_copie_lue` (l. 202 à 208).
- **(d) est rejouée** (précision 1). `code_au_commit_v3` lit `SCORES-B5F`, ouvre le registre du commit prouvé et y joue (d), (d'), (c'1), (c'2) et (b').
- **Champ `a_garde_d_ouverture.code` en (b)** (précision 2) : `"égal hors des listes fermées de la v2 et de l'erratum"`, avec `commit_de_code` et `erratum_sha256`.
- **Le fichier de traduction** est scellé à côté du résultat. Il porte la traduction, E_a, E_b, l'engagement et l'erratum.
- **En (a), le module refuse avant toute écriture.**
- **Différences fermées** : `preparer` (une ligne), `garde_d_ouverture` (quatre blocs) et `ouvrir` (deux blocs). Je les ai relues contre `lecture_v1.py`, l. 516 à 535, 1351 à 1385 et 1480 à 1495.

### Les essais rejoués

**Sur le commit v3** : 295 passés et 1 sauté, en un seul passage, dont :
- commande v3 : 77 ;
- identification : 5 ;
- ouverture : 100 ;
- commande v2 : 113 passés et 1 sauté.

**L'essai d'identification a bien tourné.** Un `git http-backend` local exige l'identification Basic :
- l'amorce figée tombe (« could not read Username », « promisor remote ») ;
- R12 tient ;
- la garde neuve arrête l'amorce ;
- le cas sain passe.

**Les essais figés**, rejoués sur l'arbre v3, où ces fichiers sont égaux à ceux de `c76e79169` :

| Essais | Passés |
|---|---|
| amorce | 51 |
| amorce entière | 4 |
| engagement | 23 |
| relecture | 24 |
| lanceur v1 | 43 |

Je n'ai pas rejoué lecture 102 ni l'épreuve à vérité plantée 155.

## Constats

**1. Mineur, un trou d'essai.** `commande_lecture_v3.py:124-128` (`_candidate`) ramène la ligne à la forme composée, ramène les espaces à U+0020 et reconnaît le préfixe précédé de « | ». Aucun essai ne voit ces trois normalisations.
- **Ce que montrent les mutations 3, 4 et 5** : retirer l'une ou l'autre laisse les 77 essais verts. Les artefacts « accent décomposé », « espace insécable » et « barre verticale » sont joués **seuls**, et tombent alors en « absente », dont le motif porte aussi « épinglage ».
- **Le code est juste.** J'ai vérifié à la main qu'une ligne saine suivie d'une copie NFD, à espace insécable ou précédée de « | » est refusée, avec le motif « 2, une et une seule ».
- **Correction** (`tests/test_commande_lecture_v3.py`, `test_d_prime_artefacts`) : ajouter trois cas « ligne saine + variante » (NFD, espace insécable, `| `) et exiger le motif `une et une seule`.

**2. Mineur, un trou d'essai.** Deux gardes de C12 ne sont vues par aucun essai :
- `commande_lecture_v3.py:303`, la clause `cmd.count("base64 -d") != 1` : le lanceur la double, mais aucun essai ne joue `amorce_embarquee_sha256` sur une commande à deux segments (mutation 8) ;
- `scripts/lancer_b5f_lecture_v3.sh:34`, la condition « une seule ligne de sortie » (mutation 9).

**Correction** :
- un essai de `amorce_embarquee_sha256` sur une commande à deux segments, dont l'un vise un autre fichier ;
- un cas de `test_lanceur_v3_condition_d_arret_c12…` où le faux interpréteur imprime la commande saine plus une seconde ligne : refus attendu.

**3. Réserve à trancher par le conducteur : la parité.** Le § 5.6 exige la parité « pour chaque monde de `liste_mondes()` ». L'essai n'en joue par défaut qu'un échantillon fixé de 39 sur 7 269 (`tests/test_ouverture_suffixes_v1.py`, `_echantillon`). Les 7 269 ne se jouent que si `B5F_PARITE_TOUS=1`, environ trois heures de processeur, sans dépense ; ce n'est pas joué. L'écart est déclaré par le développeur (réserve 1).
- **Correction** : jouer une fois `B5F_PARITE_TOUS=1` avant l'admission. Sinon, le conducteur consigne qu'il accepte l'échantillon comme écart à la lettre du § 5.6.

**4. Remarque, sans correction exigée.** Pour la v3, `exiger_session_au_commit_de_commande`, réemployée pour (b'), rend un motif qui parle encore du « commit de commande… que cite GO-LECTURE-B5F » et de la « commande de lecture v2 » (`commande_lecture_v2.py:162`). Le motif est trompeur, mais la garde est exacte, et la récrire romprait l'import de la fonction vérifiée par (c'1). À dire dans le mandat de la session si un refus de (b') survient.

**5. Remarque.** Deux écarts du développeur, déclarés, que je tiens pour admissibles :
- le jumeau suffixé porte deux familles retirées au lieu d'une, ce qui couvre les trois graphies ;
- le doublon après traduction, inatteignable par une table cohérente, est éprouvé sur la garde de ligne elle-même.

**6. Remarque.** La mutation 11 (c(base) prise au résumé sans `exiger_copie_lue`) reste verte. C'est une mutation équivalente : `ouvrir` rejoue `exiger_copie_lue` sur chaque famille du résumé (l. 329 à 331) avant toute écriture. Aucun trou.

## Mutations jouées

Seize, toutes hors de la liste du développeur. Chaque fichier a été rendu à l'octet, et l'arbre est propre après la campagne.

| N° | Mutation | Issue |
|---|---|---|
| M1 | erratum de la ligne d'épinglage non vérifié | attrapée |
| M2 | branche de sortie de la ligne non vérifiée | attrapée |
| M3 | candidate sans forme composée | **non attrapée** (constat 1) |
| M4 | candidate sans espaces ramenées | **non attrapée** (constat 1) |
| M5 | candidate sans « \| » | **non attrapée** (constat 1) |
| M6 | ascendance v2 → v3 non vérifiée | attrapée |
| M7 | présence des modules et lanceurs non exigée | attrapée |
| M8 | compte de « base64 -d » retiré (module) | **non attrapée** (constat 2) |
| M9 | une ligne de sortie non exigée (lanceur) | **non attrapée** (constat 2) |
| M10 | texte ancien admis plus d'une fois | attrapée |
| M11 | c(base) du résumé sans `exiger_copie_lue` | non attrapée, équivalente (constat 6) |
| M12 | variante (b) par `any` au lieu de `all` | attrapée |
| M13 | épinglage lu au registre donné plutôt qu'au commit prouvé | attrapée |
| M14 | (c'1) sur le commit de `SCORES-B5F` au lieu de `CODE-LECTURE-B5F` | attrapée |
| M15 | épinglage omis dans `variante` | attrapée |
| M16 | traduction admise en (a) | attrapée |

**Bilan** : 10 attrapées sur 16, 1 équivalente, et 5 non attrapées qui relèvent de trous d'essai (constats 1 et 2), pas de défauts du code.

Script : `/tmp/claude-0/-home-user-controle-ia-travail/b09e1b49-1473-5167-b0d5-946b1adabcb0/scratchpad/mut/mutations.py`. Résultats : `…/scratchpad/mut/res.txt`.

## Cloisonnement

- **Lu** : les trois pièces citées, le code des commits `c76e79169`, `5402367e` et `9e682f0e` (modules, lanceurs, amorce, essais), et `validation_reelle.CHEMINS_GELES`.
- **Jamais ouvert** :
  - `donnees/*`, `formation-b5f/*`, `traces/*`, `diag/`, `docs/verdicts/` ;
  - l'état, les décisions, les passations ;
  - aucune table, aucun sel, aucun score, aucun texte scellé.
- **Mon arbre de travail détaché** est dans mon bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/b09e1b49-1473-5167-b0d5-946b1adabcb0/scratchpad/wt`. Je ne l'ai ouvert que pour ce code.
- Aucun refus d'outil. Aucun commit, aucune poussée, aucun appel payant.
