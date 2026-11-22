# Vérification des corrections — brouillon 2 de l'additif et du devis de la voie (A) — cl1

Date : 2026-11-22. Classe A. Même contre-lecteur : Claude Opus 5.5, mêmes interdits. Rien n'a été dépensé, aucun loueur appelé, rien poussé.

## Verdict

**Pas encore scellable.** Le brouillon 2 porte les deux bloquants de cl1 et la plupart des autres points. Il ne tient pas encore compte de la correction étroite de la garde de dépense, accordée par Lazar sous `GO-2026-11-22-77` et à coder par le correctif 0023. Il garde aussi deux points mineurs ouverts de cl1.

Il devient **scellable** à trois conditions :
1. un brouillon 3 qui porte les corrections ci-dessous (sections B et C) ;
2. les correctifs 0022 et 0023 vérifiés par leur contre-lecteur ;
3. les champs entre chevrons remplis.

## Pièces et rejeux

Commit `30ea7862d05de7f5d0c34b100dc53e80fe6bf08a`. Empreintes conformes :

| pièce | empreinte |
|---|---|
| additif, brouillon 2 | `709e15357d6d9d53…` |
| devis, brouillon 2 | `9b48987ba823426e…` |
| différences entre les brouillons 1 et 2 | `1b460fbf9cf734be…` |
| programme de calcul v2 | `5e8188c1…` |
| sortie du calcul v2 | `678353c4…` |
| vérification des gardes v2 | `c234b310…` |
| sortie de la vérification v2 | `e48f7535…` |

Rejeux :
- `calcul-devis-voie-A-v2.py` rend une sortie identique octet pour octet.
- `verifier-gardes-du-lanceur-v2.sh`, au commit `43d6d0673`, sur `registres/go.md` de `main` (registre `3db30eb9…`), rend une sortie identique.
- Les marques de progrès lues par l'essai de vitesse existent dans le code (`lanceur_v5.py`) : `etape=etalonnage phase=debut` (l. 313), `lot=n` (l. 298), `phase=fin` (l. 365), et `etape=course phase=debut` (l. 497).

## A. Points de cl1 portés

| point de cl1 | où le brouillon 2 le porte |
|---|---|
| B1, la ligne de dépense | `GO-2026-11-22-75` partout ; `go_id` de la configuration ; registre au commit de lancement ; 60 et 55 USD ; minuterie au plus tard à `1796076000` ; plus aucune création à partir du 27 ; fichier d'entrées scellé inchangé, sans l'écriture de 13 USD. Le pire, 59,76 USD, prend la marge de 3,84 USD du devis scellé : c'est plus prudent que les 0,69 de cl1. |
| B2, l'essai de vitesse | option (b) : un délai au lot 2, calculé par programme. La liste neuve de l'étalonnage avec l'essai sur la carte est exigée (champ `<<LISTE_ETALONNAGE_AVEC_ESSAI_DU_TIRAGE>>`). |
| M1, la variable de tirage | `IIB_TIRAGE=carte` à l'étalonnage et à la course ; plus de clé de configuration pour le tirage. Seulement en partie : voir B1 ci-dessous. |
| M2, la liste de la course | la v2 de la liste ; 296 et 312 essais attendus ; 310 annoncés pour la liste neuve de l'étalonnage. |
| M3, où le tirage est écrit | « résumé et marque de chargement », écrit en toutes lettres. |
| M4, la voie (B) | gardée pour plus tard ; la voie (A) est la voie choisie ; la règle de la seconde tentative est écrite. |
| M5, le crédit | recharge automatique citée. |
| m2, m4 et m5 | les correctifs 0020 et 0021 sont cités, la ligne neuve aussi, et les réserves sont à jour. |

Aucune régression trouvée.

## B. Encore à corriger

1. **Majeur — M1, en partie seulement.** Aucun contrôle ne vérifie la commande de création imprimée pour **l'étalonnage**. Aucun arrêt n'est prévu si le journal de l'amorce (`TIRAGE=`) ou la marque de chargement (`tirage`) de l'étalonnage dit autre chose que « carte ». Sans ces deux gardes, un oubli n'est vu qu'à la course, par `exiger_meme_tirage`, une fois l'étalonnage payé.
   - Ajouter au § 3, aux contrôles avant la création : « la commande imprimée porte `-e IIB_TIRAGE=carte` ».
   - Ajouter au § 5, aux arrêts de l'étalonnage : « journal de l'amorce ou marque de chargement autre que `carte` : arrêt par l'identifiant ».
   - Ajouter la même vérification à la course, au § 4.3.
2. **Mineur — m1 de cl1, non porté.** L'annexe A2 dit « sans rapatriement vérifié, aucune destruction ». L'annexe A3 dit que la minuterie détruit la machine à l'échéance. Ajouter à A2 : « sauf la minuterie de l'amorce, à l'échéance (ordre scellé) ».
3. **Mineur — la machine 61875617.** A2 écrit que Lazar l'a détruite dans la console du loueur. Le fait neuf dit qu'elle est détruite à 15:27Z, sur le « go toi-même » de `GO-2026-11-22-77`. Écrire qui l'a détruite, à quelle heure, et la ligne de `registres/arrets.md`.

## C. Fait neuf : la correction étroite de la garde de dépense

Sous `GO-2026-11-22-77`, la coupure effective vaut le plafond de la ligne moins la dépense antérieure vraie. Le plafond scellé de 55 USD ne change pas. Le correctif 0023 doit coder cette règle. Il faut alors **déclarer la dépense antérieure vraie** : c'est le compte de la voie, arrondi au centime supérieur, sans borne. Voici où le texte change.

### Additif

| où | changement |
|---|---|
| A3, puce « Dépense antérieure déclarée » | retirer « borné à 5.00 », « 5,52 USD refusés » et « au-delà de 5,00 … la valeur déclarée est `5.00` ». Écrire : « le compte vrai de la voie ; sous le correctif 0023, la coupure effective vaut 60 − ce compte ». Citer la vérification du correctif 0023 (cas sain : 5,52 et 9,65 acceptés ; artefact : un compte ≥ 60 refusé). |
| A3, sous-puce « Machine de la course » | retirer « À 5 USD déclarés … 34,78 heures [M27] ». Écrire : l'épuisement du lanceur tient le total sous 60 USD. L'échéance, calculée sur la coupure de 55, le précède. Le pire reste de 59,76 USD. |
| A3, puce « Ce qui tient la coupure » | « Le programme rend aussi la dépense antérieure à déclarer » : c'est désormais le compte lui-même. |
| § 4.3, point 3 | `--verifier-go-seulement 55 <dépense antérieure déclarée>` : reprendre la forme exacte des contrôles du correctif 0023. Le compte vrai doit passer. |
| § 6, champs | ajouter `<<CORRECTIF_0023_CHEMIN_EMPREINTE_ET_VERIFICATION>>`. Rattacher la liste neuve de l'étalonnage au correctif 0022 et à sa vérification. |
| § 7, point 3 | retirer « Dépense antérieure bornée à 5 USD … non fait ». |
| Arbre du code | `6696aca1f` / `725f3d58` ne sont plus l'arbre de la voie. L'arbre de la voie est celui qui porte 0021, 0022 et 0023, vérifié. Mettre à jour `<<COMMIT_CODE_REVU_VOIE_A>>` et `<<ARBRE_CODE_VOIE_A>>`. |

### Devis

| où | changement |
|---|---|
| § 4, l. 94 (« Ce qui tient la coupure pendant la course ») | réécrire comme A3 ci-dessus. |
| Liste d'arrêt | ajouter une ligne si la garde du correctif 0023 refuse. |

### Programmes

| programme | changement |
|---|---|
| `calcul-devis-voie-A-v2.py` | passer en **v3**. Retirer `DECLAREE_MAX = 5.00` (l. 57). La valeur à déclarer devient le compte, l. 123. Refaire les lignes [M24], [M25] et [M27]. |
| `verifier-gardes-du-lanceur-v2.sh` | passer en **v3**, rejouée au code qui porte le correctif 0023. Son § 2, où 5,52 et 9,65 sont attendus en refus, s'inverse. |

## D. Champs entre chevrons, au vu des faits neufs

| champ | état |
|---|---|
| `<<VERIFICATION_DU_CORRECTIF_0021>>` | `registres/iib-executante/p1-code-course-v1/note-verification-0021-cl1.md`, empreinte `213537e74d19e6251a1906d4356e60fe6a2b4d113b718c707d5a6c98acf8cbb5`, verdict « autorisable ». |
| `<<BRANCHE_CODE_VOIE_A>>` | `prep/iib-tirage-carte-v1`, poussée. Le distant la porte à `6696aca1f`. Elle doit avancer jusqu'à 0023. |
| `<<COMMIT_CODE_REVU_VOIE_A>>`, `<<ARBRE_CODE_VOIE_A>>` | en attente du code qui porte 0022 et 0023, vérifié. |
| `<<LISTE_ETALONNAGE_AVEC_ESSAI_DU_TIRAGE>>` | en attente du correctif 0022 et de sa vérification. |
| `<<TESTS_ATTENDUS_ETALONNAGE_VOIE_A>>` | le nombre que donnera le correctif 0022. |
| `<<TESTS_ATTENDUS_COURSE_VOIE_A>>` | 312, à reconfirmer après 0022 et 0023. |
| `<<EMPREINTES_AMORCES_ET_LISTES_VOIE_A>>` | à relever à l'arbre final : l'amorce de l'étalonnage change avec la liste v7. |
| `<<ENTROPIE_VOIE_A>>` | à tirer par la mère. |
| `<<INSTANCES_INTOUCHABLES>>` | à relever par l'exécutante. |
| `<<CONFIG_VOIE_A_CHEMIN_ET_EMPREINTE>>`, `<<COMMIT_LANCEMENT_ETALONNAGE_VOIE_A>>` | à écrire après l'arbre final. |

**Crédit** : 39,81 USD, avec la recharge automatique active. Le pire de la machine de l'étalonnage est couvert : 21,32 USD à la borne de 14 heures, plus 2.
