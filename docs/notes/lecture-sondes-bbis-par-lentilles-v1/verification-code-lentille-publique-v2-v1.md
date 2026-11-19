# Vérification des corrections — code de la lecture des sondes de l'étape B bis par la lentille publique, version 2 — v1

Pièce de classe B. Ce contre-lecteur est le même que celui du rapport `contre-lecture-code-lentille-publique-v1.md`
(`679eb7232eed0c154743348102cccd40c05b8f38b1f730eeb21b24f171af155d`) : modèle Opus 5.5, sous-agent de la session mère, 2026-11-19.
Objet : commit `08dea10b` de la branche `claude/lentilles-bbis-developpeur-v1`, récupéré par son nom.

**Conclusion : bon tel quel.** Une remarque non bloquante (§ 6) est à reprendre en version 3.

## 1. Empreintes, et rien d'autre de changé

- Les 19 empreintes de `empreintes-code-v2.txt` (`d4ac3338…`) concordent avec les fichiers du commit.
- Le traitement `traitement-contre-lecture-v1.md` (`42f0db6f…`) et la sortie des essais `sortie-essais-v2.txt` (`f2f7b03b…`) sont vérifiés.
- Comparaison par programme entre `128810af` et `08dea10b` sur `src/` et `tests/` : **huit ajouts, aucune modification, aucun retrait.** Les dix modules de la version 1 sont identiques à l'octet. Seuls deux modules sont nouveaux, `entrees_v2.py` (`aa14d1da…`) et `lanceur_v2.py` (`8230341d…`).

## 2. Corrections A à D portées telles quelles

J'ai comparé par programme les modules et jouets de la version 2 avec ma copie corrigée, en remplaçant seulement `entrees_v1`, `lanceur_v1` et `jouets_v1` par leurs noms `_v2` :

| pièce comparée à ma copie corrigée | résultat |
|---|---|
| `jouets_v2` | identique |
| `procedure_v2` | identique |
| `entrees_v2` (essais) | identique |
| `montage_v2` (essais) | identique |
| `test_lentilles_sondes_bbis_corrections_contre_lecture_v1.py` | identique, sauf une importation inutile retirée (`numpy`) |
| `entrees_v2.py` | identique, sauf un paragraphe de docstring |
| `lanceur_v2.py` | A à D identiques ; l'import de `verifier` est remonté en tête du module ; quatre ajouts annoncés |

Les quatre ajouts du lanceur, relus :
- **Essai hors ligne du tokeniseur.** Il est joué juste après la pose du cache et avant tout flux. C'est un enfant sans clé, `HF_HUB_OFFLINE=1`. Un échec arrête le montage, et c'est un nœud.
- **Fiche fermée et scellée des entrées.** `diag/<run>/entrees-lentilles-bbis.json` porte les chemins et empreintes de E-1 et E-2, et l'empreinte de l'extrait de la liste blanche. Elle entre dans le contrôle R12 du départ. La ligne `ENTREES-LENTILLES-BBIS` la cite, ce qui règle la remarque E4.
- **Le manifeste cite le rapport du montage** et la fiche des entrées.
- **Note explicite pour les pôles « intermédiaires ».** C'est un champ `note`, pas une phrase gelée.

**Aucune ligne de calcul n'est changée.**

## 3. L'essai bloquant : le libellé des pôles après repli

Il est présent sous trois formes :
- un essai unitaire à trois cas, où le nul refait par direction décide et non le nul partagé « remplacé » ;
- le cas sain sans repli ;
- un essai de bout en bout sur la couche repliée (couche 7 du jouet, au moins quatre directions), qui contrôle le libellé de chaque direction sur les p en vigueur.

**Mon altération est vue** : remplacer, dans `_etiqueter`, la valeur p du nul par direction par celle du nul partagé « remplacé » fait tomber l'essai.

## 4. Les 25 essais neufs des gardes sans artefact

J'ai rejoué mes altérations contre `test_lentilles_sondes_bbis_gardes_non_vues_v1.py` et `test_lentilles_sondes_bbis_corrections_contre_lecture_v1.py`. Le programme est `mutations_v2_v1.py`. Il a tourné sur une copie partielle du commit, remise en état et revérifiée par empreintes après chaque essai.

| altérations rejouées | nombre | vues |
|---|---|---|
| gardes réelles survivantes de ma première série | 10 | 10 |
| survivantes de ma seconde série, libellé des pôles compris | 6 | 6 |
| gardes de mes corrections A à D | 10 | 10 |
| ajouts de la version 2 (essai du tokeniseur, note des pôles, ligne qui cite la fiche des entrées) | 3 | 3 |
| **total** | **29** | **29** |

Détail des dix premières : `run_id`, scellement qui cite le texte, `fichier_sondes.fichier`, `cellule` et `pli_lu`, forme de `…_b`, longueur de l'essai d'un octet, commit du voisin, tailles des tenseurs extraits, `jetons-gardes.json`, précision de `W_U`.

Détail des six suivantes : libellé des pôles après repli, disque à chaque direction, dossier de travail existant, sorties existantes, montage absent, clé écrite au montage.

Rien ne survit. Les deux altérations sans effet de mon rapport restent sans essai, comme je l'avais classé.

## 5. Essais ciblés rejoués

J'ai joué les sept fichiers de la version 2 avec `-p no:cacheprovider` et un `--basetemp` dans mon bloc-notes, sans la suite complète :
- `test_lentilles_sondes_bbis_entrees_v2.py`
- `test_lentilles_sondes_bbis_montage_v2.py`
- `test_lentilles_sondes_bbis_lecture_v1.py`
- `test_lentilles_sondes_bbis_nuls_statistiques_v1.py`
- `test_lentilles_sondes_bbis_procedure_v2.py`
- `test_lentilles_sondes_bbis_corrections_contre_lecture_v1.py`
- `test_lentilles_sondes_bbis_gardes_non_vues_v1.py`

Dernière ligne : **`300 passed in 213.04s (0:03:33)`**, égale au compte du développeur. Cela fait 258, plus 17, plus 25 essais.

## 6. Remarque non bloquante, à reprendre en version 3

Le manifeste cite le rapport du montage seulement s'il le trouve dans le dossier de sortie. Sinon, le champ vaut `None`, en silence. Montage et calcul écrivent dans la même sortie, donc le cas ne devrait pas se présenter. Mais c'est un repli silencieux, alors que R5 demande « aucun repli silencieux ».

Avant (`_calculer`, près de l'écriture du manifeste) :
```python
    montage = ({"chemin": f"diag/{ctx.run}/montage-lentilles-bbis.json", "sha256": verifier(rapport_montage)}
               if rapport_montage.is_file() else None)
```
Après (le contrôle est placé au départ du calcul, avec les contrôles R12, et la ligne ci-dessus devient sans condition) :
```python
    rapport_montage = ctx.sortie / "diag" / ctx.run / "montage-lentilles-bbis.json"
    if not rapport_montage.is_file():
        raise Arret("rapport du montage absent du dossier de sortie : le manifeste ne pourrait le citer ; rien ne part")
...
    montage = {"chemin": f"diag/{ctx.run}/montage-lentilles-bbis.json", "sha256": verifier(rapport_montage)}
```
Il faut aussi un essai sur un artefact où le rapport du montage est retiré avant le calcul. La version 3, déjà annoncée pour le code de l'addendum, peut le porter. Rien ne part avant cette version de toute façon.

## 7. Pièces

Elles sont sous `docs/notes/lecture-sondes-bbis-par-lentilles-v1/verification-outils-v2/`, chacune scellée :
- `mutations_v2_v1.py` (`8c2d12ec…`) et sa sortie `sortie-mutations-v2-v1.txt` (`e1189d8e…`) ;
- `sortie-essais-v2-verification.txt` (`e83c3942…`).

Déclaration :
- **Lu** : la note de traitement du développeur, le diff `128810af..08dea10b` et les essais neufs.
- **Jamais ouverts** : `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, ni aucun verdict, table ou résultat.
- Aucune dépense, aucun téléchargement de modèle ni de corpus, aucun commit, aucun refus d'outil.
