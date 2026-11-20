# Contre-lecture du code de formation v2 (barreau 5, relance des six instances)

Contre-lecteur neuf (Opus 5.5), 20 novembre 2026. Pièces lues : mandat du développeur, extraits permis du texte scellé, additif 1 (projet), rapport du développeur, différentiel `31fca83b…` → `a74dfb49…` et code v1 autour, registre propre au dernier `origin/main` (`e59d6b9dd`), garde de calcul du dépôt, code du programme de lecture au commit de `CODE-LECTURE-B5F` (`c76e7916…`), par `git show`/`git grep` seulement. Rien lu de `diag/`, des branches `donnees/`, d'aucun score ni résultat.

## Verdict

**Non conforme** : la clé neuve `CODE-RELANCE-FORMATION-B5F` ferait refuser le registre entier au programme de lecture déjà figé (`CODE-LECTURE-B5F`, 2026-11-20T07:43:13Z) et dont l'épreuve à vérité plantée est déjà passée (`EPREUVE-B5F`, 11:28:24Z) ; l'additif et le code supposent à tort que ce code de lecture « sera figé plus tard ». Conforme après le couple 1 (bloquant) et le couple 2 (important) ; les autres sont mineurs.

## Couples

**1. Bloquant — la clé neuve casse le code de lecture figé et l'épreuve passée.**
- Constat. Le registre propre sur `origin/main` porte déjà `CODE-LECTURE-B5F` (commit `c76e79169eee337ce66c7d88f62d039e853eebfc`, lecture sha256 `ed0999df…`) et `EPREUVE-B5F` (passée, même empreinte). À ce commit, `src/controle_ia/barreau5_familles/engagement_v1.py` l. 38-40 a la liste de clés v1 (sans la clé neuve) ; `lecture_v1.py` (l. 453 `lire_registre_de_lecture`, l. 1408 `relance_du_registre`) et `relecture_v1.py` (l. 192 `exiger_registre_de_relecture`, appelée par `verifier_avant_creation` l. 865 et par la marche l. 547 et l. 1071) lisent tous le registre par `en.lignes_du_registre`, qui refuse toute clé « -B5F » inconnue (`engagement_v1.py` l. 142). Essai rejoué sur une extraction de `c76e7916` (`$S/relance/essais-contre-lecture/essai_lecture_figee.py`) : registre avec la seule ligne de relance → `[1, 2, 3, 4, 5, 7]` ; avec `CODE-RELANCE-FORMATION-B5F` → « registre propre, ligne 4 : clé CODE-RELANCE-FORMATION-B5F inconnue ». On ne peut pas non plus changer `engagement_v1.py` du côté de la lecture : `lecture_v1.exiger_code_de_lecture_au_commit` (l. 497-511) et `relecture_v1.verifier_avant_creation` (l. 876-880) exigent que l'arbre gelé joué soit celui du commit de `CODE-LECTURE-B5F`, ligne qui ne se réécrit pas et ne se double pas (liste d'arrêt, point 10 : aucune ouverture). L'additif C5 (« Le code de lecture, figé plus tard à `CODE-LECTURE-B5F`, part donc du code v2 ») et le point ouvert 6 du rapport reposent sur un fait faux.
- Correction proposée (la plus simple qui laisse intacts le code de lecture et l'épreuve passée) : **aucune clé neuve** ; le commit du code des relances s'écrit dans la **colonne de référence** de `GO-RELANCE-FORMATION-B5F`, que le texte laisse libre et où il range « tout le reste » ; le contenu de la ligne reste celui que lit le code de lecture (`GO-2026-11-19-86 ; instances 1,2,3,4,5,7`). Exactement :
  - `engagement_v1.py` : revenir au fichier v1 (blob `7d2b56368d…`), `CLES_REGISTRE` sans `CODE-RELANCE-FORMATION-B5F`. Ainsi le fichier est identique à celui du code de lecture figé.
  - `formation_v1.py` : supprimer `CLE_CODE_RELANCE` et le bloc l. 1048-1056 ; ajouter près de `_RELANCE` (l. 1013)
    `_CODE_RELANCE_REF = re.compile(r"(?:^|; )code des relances commit ([0-9a-f]{40})(?= ;|$)")`
    et, dans le bloc de la ligne de relance, à la place des l. 1067-1071 :
    ```python
    cr = _CODE_RELANCE_REF.findall(lignes["GO-RELANCE-FORMATION-B5F"]["ref"])
    if len(cr) != 1:
        raise GardeArret("GO-RELANCE-FORMATION-B5F : la référence porte une et une seule mention « code des relances "
                         "commit <40 signes> » (additif 1) : le code des relances n'est pas figé")
    if cr[0] == m.group(1):
        raise GardeArret("GO-RELANCE-FORMATION-B5F : le code des relances est celui des premières marches (additif 1)")
    code_relance = cr[0]
    ```
    garder l'égalité de l'accord, les six instances et les 147 USD ; `commit_du_code`, `executer`, `commande_de_creation` et les messages nommant la ligne restent tels quels, la clé nommée devenant « GO-RELANCE-FORMATION-B5F (code des relances) ».
  - Additif : C5 réécrit (« aucune clé neuve ; la référence de `GO-RELANCE-FORMATION-B5F` porte, une seule fois, « code des relances commit <40 signes> », lue à la lettre par le code v2 et par lui seul ; le code de lecture, figé à `CODE-LECTURE-B5F` (`c76e7916…`, épreuve passée à `EPREUVE-B5F`), n'est pas touché et lit la ligne de relance par son contenu inchangé ») ; §4 sans la ligne 2 ; §5 et §6 accordés.
  - Essais : cas sain (une mention) ; artefacts (aucune mention, deux mentions, 39 signes, majuscules, commit égal à celui de `CODE-FORMATION-B5F`, mention dans le contenu et non dans la référence) ; et un essai qui lit le registre final **par le `engagement_v1.lignes_du_registre` du code de lecture** (le fichier v1, identique) pour prouver qu'il l'accepte. Rejouer l'épreuve par retrait et par mutation sur ces gardes.
  - Variante, si Lazar tient à une clé : c'est un nœud (nouvel engagement du code de lecture sous une autre clé, épreuve à vérité plantée rejouée, écart à la liste d'arrêt, point 10) ; je ne la recommande pas.

**2. Important — le registre du commit de course et l'arbre de la lecture.**
- Constat. Additif §4, point 1, et rapport §6 : « Déjà inscrites : `SCELLEMENT-B5F`, `CODE-FORMATION-B5F`, `GO-FORMATION-B5F` » et « commit de course … dont le registre propre porte les lignes 1 à 3 ». Le registre réel en porte cinq (`CODE-LECTURE-B5F` et `EPREUVE-B5F` en plus). Un registre de course qui n'en porte que trois divergerait du registre de `main` (lignes « jamais réécrites » d'un seul fichier). Par ailleurs, si le code v2 entrait dans l'arbre de `main` d'où la session de lecture bâtit le commit de sa marche, `relecture_v1.verifier_avant_creation` et `lecture_v1.exiger_code_de_lecture_au_commit` refuseraient (arbre gelé ≠ celui de `c76e7916`).
- Correction : §4 point 1 de l'additif et rapport §6 : « Déjà inscrites : `SCELLEMENT-B5F`, `CODE-FORMATION-B5F`, `GO-FORMATION-B5F`, `CODE-LECTURE-B5F`, `EPREUVE-B5F` » ; « le registre propre du commit de course est celui de `main` à l'inscription, ligne de relance comprise, octet pour octet » (le code v2 connaît ces clés). Ajouter : « le code v2 vit sur sa branche et sur la branche de course ; il n'entre pas dans l'arbre d'où part la lecture : la relecture et la lecture jouent l'arbre gelé de `CODE-LECTURE-B5F` ». Essai : le registre de `main` tel qu'il est, plus la ligne de relance, lu par `lire_code_et_accord` du code v2 (sain).

**3. Mineur — le code laisse citer l'instance 6.**
- Constat : `formation_v1.py` l. 1075-1081 bornent le compte et la somme ; « 6,7 » ou « 6 » passent (rapport, point ouvert 8 ; essais l. « sains » de `test_registre_relance_bornee_six_instances_et_enveloppe_de_147_usd`). Relancer l'instance 6, finie, ferait lire sa copie `-x1` à la place des familles formées : décision que le texte veut mécanique.
- Correction : `INSTANCES_TOMBEES = (1, 2, 3, 4, 5, 7)` (additif C1) et, dans le bloc de relance, `if not set(instances) <= set(INSTANCES_TOMBEES): raise GardeArret("GO-RELANCE-FORMATION-B5F : instance non tombée citée (additif 1, C1) : nœud")` ; cas sain « 1,2,3,4,5,7 » et parties, artefacts « 6 », « 6,7 ». Sinon, garder la règle à la seule session mère, écrite dans l'additif §5.

**4. Mineur — filiation du code des relances non vérifiée.**
- Constat : rien ne vérifie que le commit du code des relances descend de celui de `CODE-FORMATION-B5F` (rapport, point 9), et l'aide `_registre_propre` de `tests/test_lancer_b5f_formation_v1.py` (l. 51-53 au commit v2) fait citer par défaut le code v1 comme code des relances, cas que l'additif exclut.
- Correction : dans `commande_de_creation`, pour une relance, `git merge-base --is-ancestor <commit CODE-FORMATION-B5F> <commit du code des relances>` sinon refus ; garde « différent du code v1 » du couple 1 ; l'aide d'essai prend par défaut un commit v2 distinct.

**5. Mineur — R12, fichiers retouchés sous leur nom « v1 ».**
- Constat : `formation_v1.py`, `engagement_v1.py` (si le couple 1 n'est pas appliqué), `lancer_b5f_formation_v1.sh`, `amorce_b5f_formation_v1.sh` et deux fichiers d'essais portent un contenu v2 sous le nom v1. La version est portée par le commit épinglé au registre, et renommer obligerait à changer l'amorce, le lanceur, les essais et le module appelé : changement plus large que l'additif.
- Correction : garder les noms, et écrire l'écart dans l'additif (§2 ou §5) : « exception déclarée à R12 : le code v2 garde les noms v1 ; sa version est le commit cité par la ligne de relance ; le fichier v1 reste au commit de `CODE-FORMATION-B5F` » ; la mère le consigne au registre des décisions.

**6. Mineur — plancher d'essais de l'amorce.**
- Constat : `MIN_ESSAIS` 235 → 242 (`scripts/amorce_b5f_formation_v1.sh` l. 59) est juste pour le code tel quel (242 rejoués) et tenu par `test_texte_plancher_d_essais_egal_au_nombre_d_essais_du_paquet`. Les couples 1 à 4 changent le compte.
- Correction : remesurer après corrections et reporter le nombre exact, avec son commentaire.

## Points vérifiés sans constat
- (a) L'instance 6 et ses sorties versées ne dépendent pas du code v2 : son manifeste cite le commit qu'elle a joué ; une première marche sous le code v2 est refusée (voulu). Après inscription d'une clé inconnue, tout lecteur au code v1 refuse le registre (couple 1) ; la destruction et sa vérification ne lisent pas le registre.
- (b) Entropie (celle de `CODE-FORMATION-B5F`, `lu["entropie"]`), noms suffixés `-x1`, clés des graines, clé d'injection sans suffixe, coupures, branches de sortie, échéance d'arrêt : aucune ligne changée.
- (c) Sans ligne de relance ou sans le code des relances, sous un autre accord que `GO-2026-11-19-86` (registre et `GO_ID`), au-delà de six instances ou de 147 USD : refus, à la lecture du registre, sur l'instance et à l'impression de la commande. La garde de calcul n'admet que `GO-2026-11-19-86` (type « calcul ») devant la commande.
- (d) `depense_session` applique le plafond de 200 USD à toute marche, relances comprises ; c'est la session qui fournit un cumul commun qui compte les relances (additif C4), comme pour les premières marches. Arithmétique de C4 juste : 200 − 147 − 7,02 = 45,98.
- (f) L'égalité de l'accord de la relance avec celui de `GO-FORMATION-B5F` rend C6 mécanique ; elle est cohérente avec l'additif ; le code de lecture ne lit pas l'accord de la ligne de relance. À garder.
- Les commentaires du lanceur ne changent aucune ligne exécutée.

## Lecteurs du registre propre

Recherche : `git grep` de `barreau5-familles-jumelles-v1.md` et de `-B5F` dans `src`, `scripts`, `tests` sur `origin/main` (`e59d6b9dd`) et dans l'arbre v2 ; tous les fichiers du paquet `barreau5_familles` de `main` regardés. Le code de `main` pour ces fichiers est identique à celui du commit de `CODE-LECTURE-B5F` (`c76e7916…`). Aucune autre branche distante du barreau 5 ne porte de code (seulement `course/barreau5-formation-v1`, `formation-b5f/plan-de-marche-v1` et les branches de données, non lues).

Avec la clé neuve, tous ceux qui passent par `engagement_v1.lignes_du_registre` au code v1 refusent le registre entier. Avec la correction du couple 1 (pas de clé neuve), **aucun ne refuse et aucun ne change**.

| programme (fichier sur `main` / au commit de `CODE-LECTURE-B5F`) | lit le registre par | (a) refuse avec la clé neuve ? | (b) chemin pour l'accepter |
|---|---|---|---|
| `engagement_v1.py` (`lignes_du_registre` l. 132, `lire_registre`, `lignes_au_commit`, `ligne_du_registre`, `verifier_engagement_avant_lecture`) | sa liste `CLES_REGISTRE` (l. 38) | oui (v1) ; non dans l'arbre v2 | avec clé : le changer casse l'arbre gelé du code de lecture (couple 1) : aucun chemin sans nœud. Couple 1 : rien à faire. |
| `lecture_v1.py` (`lire_registre_de_lecture` l. 444, `relance_du_registre` l. 1406, `_registre_au_commit` l. 1539, sous-commandes `preparer`, `ouvrir`) | `en.lignes_du_registre` | oui | idem : figé à `CODE-LECTURE-B5F`, sha256 du programme `ed0999df…` cité par `EPREUVE-B5F` ; couple 1 : rien à faire. |
| `relecture_v1.py` (`exiger_registre_de_relecture` l. 185, `verifier_avant_creation` l. 865, marche l. 547 et 1071) | `en.lignes_du_registre`, `lv.relance_du_registre` | oui | idem ; de plus l'arbre de la marche doit égaler celui de `c76e7916` ; couple 1 : rien à faire. |
| `sondes_v1.py` | importe `lecture_v1`, ne lit pas le registre | non | rien. |
| `epreuve_verite_plantee_v1.py` (fabrique), `juge_verite_plantee_v1.py`, `traducteur_verite_plantee_v1.py` | registres fabriqués, jamais le registre réel ; `lignes_supplementaires` refuse les seuls noms standard | non (ne lisent pas le vrai registre) | rien ; l'épreuve passée reste valable avec le couple 1 (registre lu par son contenu, inchangé). Avec la clé, l'épreuve devrait être rejouée (nœud). |
| `seconde_programmation_v2.py`, `_v3.py` | ne rejouent pas les gardes du registre | non | rien. |
| `scripts/lancer_b5f_lecture_v1.sh`, `scripts/amorce_b5f_lecture_v1.sh` | appellent `relecture_v1` et `lecture_v1` ; l'amorce exige seulement la présence du fichier | oui, par les modules | comme `lecture_v1` / `relecture_v1`. |
| `formation_v1.py` v1 (`lire_code_et_accord`, `registre_au_commit`) et `scripts/lancer_b5f_formation_v1.sh` v1 | `lignes_du_registre` v1 | oui | ne sert plus après la relance (instance 6 finie) ; les relances jouent le code v2. Couple 1 : il accepterait encore le registre (inutile). |
| `formation_v1.py` v2, lanceur et amorce v2 (branche `formation-b5f/code-relance-v2`) | `engagement_v1` v2 | non | couple 1 : lire le commit dans la référence ; le registre de course = celui de `main` (couple 2). |
| essais : `test_barreau5_familles_engagement_v1.py`, `_lecture_v1.py`, `_relecture_v1.py`, `_epreuve_verite_plantee_v1.py`, `_seconde_programmation_v2/_v3.py`, `test_lancer_b5f_lecture_v1.py`, `test_amorce_b5f_lecture*_v1.py`, et les essais de la formation | registres d'essai | sans objet (ne lisent pas le registre réel) | rien. |

Ordre, avec le couple 1 : (1) le développeur applique les couples 1 à 4 au code v2, nouveau commit ; (2) vérification par le même contre-lecteur ; (3) scellement de l'additif corrigé ; (4) une seule ligne, `GO-RELANCE-FORMATION-B5F`, contenu `GO-2026-11-19-86 ; instances 1,2,3,4,5,7`, référence portant une fois « code des relances commit <40 signes du code vérifié> » ; (5) commit de course = commit du code v2 vérifié + le registre de `main` à cet instant. Le code de lecture, l'épreuve et leurs lignes ne bougent pas.

## Essais rejoués

- `tests/test_barreau5_familles_*.py` au commit v2 (commande du mandat, `--basetemp=$S/relance/essais-contre-lecture/a`) : **242 passés, 0 échec** (103 s).
- `tests/test_lancer_b5f_formation_v1.py`, `tests/test_amorce_b5f_formation_v1.py`, `tests/test_amorce_b5f_formation_entiere_v1.py` au commit v2 (`--basetemp=$S/relance/essais-contre-lecture/b`) : **91 passés, 0 échec** (435 s), comme le dit le rapport.
- Épreuve par retrait, sur une extraction de `31fca83b…` (code v1) avec les trois fichiers d'essais du code v2 : **14 échecs, 118 passés** ; les 14 échecs sont exactement les 14 essais neufs ou retouchés que nomme le rapport (§5). L'épreuve par retrait est confirmée. (Un premier essai, joué dans l'arbre v2 avec `PYTHONPATH` vers le code v1, passait à tort : `pyproject.toml` met `src` en tête du chemin ; il n'est pas compté.)
- Total : 242 + 91 + 132 = **465 essais rejoués**, plus un essai à part, celui du code de lecture figé.
- Essai du code de lecture figé (`c76e7916…`) sur trois registres : sans clé neuve, accepté ; avec la clé neuve, refusé ; commit des relances en référence (couple 1), accepté.
