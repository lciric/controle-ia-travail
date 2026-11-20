# Contre-lecture du complément de valeurs du préenregistrement court v9, lot 1, v2 — v1

Pièce de travail (classe C), 2026-11-20, relevé de `date -u` : 14:46:13Z, après les relevés et l'essai du jeu, avant l'écriture. Contre-lecteur neuf, modèle O. Je n'ai écrit aucune version du complément ; j'ai contre-lu l'additif 1 et le devis. Mandat `799b14c6…`, en-tête compris.

Processeur seul : aucun appel, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Cette pièce ne porte aucune méthode d'attaque, aucun procédé, aucun nom ni énoncé de mode, aucune case nommée, aucune valeur de clé, aucun identifiant de modèle. Je n'ai rencontré aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**À corriger.** Le jeu `corrections-complement-valeurs-v2-v2.json` porte 28 remplacements. Ils couvrent :
- les décisions de la mère de 14:43Z, prises comme lettre ;
- l'arrondi de la part de Luc ;
- les deux pièces scellées depuis l'écriture (additif 1 v5, devis v11) ;
- un chiffre sans source ;
- une addition d'euros et de dollars dans la règle de l'arrêt n° 11.

Les chiffres sont justes au centime, cinq espèces partout. Rien n'est inventé, hors le chiffre de 10,32 USD, retiré. « Aucune recette » : conforme.

Une fois le jeu porté tel quel et l'égalité constatée par `cmp` à mon essai (`674af052…`) : **conforme, à sceller**.

## 1. Pièces

| pièce | empreinte | vérification |
|---|---|---|
| complément v2 | `267a69de63450634c369dc22415b0751c0483be1d60a000b4b598640d01c1125` | recalculée |
| rapport du rédacteur | `a08f9e6bbde6d1d696ac9b66b0935855b6e9d1826aec3044bf9ea4d11e6a0ca7` | recalculée |
| mandat du rédacteur | `8d13681abab1ce1d028049478f1c903357025b5ce2af7eb9af991dcaa2842360` | recalculée |
| additif 1 v5 scellé (R-4300), `prereg/…-v5.md` sur `origin/main` (`b48dfbd6`) | `9f731795cd8b9166ad8b78346e3d37c7352010ea0edd1f34ac86cfb0ac689200` | recalculée |
| devis v11 scellé, `prereg/…-v11.md` | `205e08f23ef9ced92a35340b8fad38765b08483a2129ee32550081d1bd043570` | recalculée |
| `go.md`, `decisions.md`, `depenses.md` au commit `2b6d0439` cité | `61d52dc1…`, `9136bef1…`, `e74bce4c…` | égales à la table du complément |
| `decisions.md` sur `origin/main` (`b48dfbd6`) | `3023730b…` | R-4300 et R-4301 en plus |

## 2. La table des valeurs ouvertes, ligne par ligne

Les seize lignes sont dans l'ordre de la v9 (lignes 243 à 258). Les lignes 8, 9 et 10 (espèce 6) sont sans objet : juste.

| n° | jugement |
|---|---|
| 1 | règle juste (v9, GO-22, GO-34) ; « attend le relevé de Lazar » : juste (R-4300 : « après … les relevés de Rigaud et d'OpenAI ») |
| 2 | Minuit et Luc changent (§ 3) ; Rigaud renvoie à la ligne 1 |
| 3, 4, 7, 12, 13 | « attend » le véhicule ou la mesure, avec son moment : juste |
| 5 | la décision de la mère (b) la fixe (corrigée) |
| 6 | deuxième relais : la dispense n'est plus nécessaire (GO-64) ; troisième relais : sans objet une fois le reste relu. Juste |
| 11 | attend le relevé : juste |
| 14 | rôles et cinq noms fixés (GO-57 (2), GO-65 (2)) ; ce que la mère écrit est marqué : juste. La « lignée de la mère » rend le modèle désigné par GO-57 sans l'identifier |
| 15 | branche « avec », les quatre épreuves (GO-57 (1), cité exactement) : juste |
| 16 | juste |

La citation de GO-2026-11-20-67 est exacte : montant 456 USD, échéance 2026-11-22. La table des valeurs qui sont des conditions de départ est juste. Elle est corrigée pour Minuit, Luc et l'arrêt n° 11.

## 3. La part de Luc

- **Le reste est vérifiable sur `main`.** Il vaut 214 USD déclarés (R-4088), moins la sonde de la clé, 0,000002 USD (registre des dépenses, ligne 548, vérifiée), soit 213,999998 USD. Aucune autre dépense n'est inscrite sur cette clé.
- **La réserve est juste.** Elle vaut 88,36 USD : R-4293, GO-2026-11-20-26, et GO-2026-11-20-68, qui porte « juge Opus sur la clé Luc ».
- **La règle est juste.** Les citations de R-4289 et R-4293 sont exactes.
- **L'arrondi est fautif.** 213,999998 − 88,36 = 125,639998. Écrite 125,64, la part et la réserve font ensemble 214,00 USD, soit 0,000002 USD de plus que le reste. Une part bornée ne s'arrondit pas vers le haut : **125,63 USD**, cinq remplacements.
- 125,63 ≥ 124,35, et le cas haut exact vaut 124,3514 : le nœud ne se déclenche pas. La marge du reste au-dessus de 212,71 USD reste de 1,29 USD. Par la décision (b), aucune ligne à part ne se paie plus sur Luc.

## 4. Le deuxième relais (GO-64)

- GO-2026-11-20-64 et R-4284 sont cités exactement.
- La part de 140,39 USD est juste (sortie du calcul v6). La dispense n'est plus nécessaire.
- La règle de l'arrêt n° 11 pour un compte payant est **acceptée par la mère** (décision (a)). Le texte est corrigé de « règle proposée » à « acceptée ».
- Une faute de lettre est corrigée. Le point 2 définissait le reste comme « la somme du crédit restant et de l'engagement », c'est-à-dire des euros additionnés à des dollars, contre le point 1. Il devient : le reste, en dollars, est au moins l'engagement ; le crédit en euros ne s'y additionne pas.

## 5. Les deux écarts déclarés

- **Recharge et part du troisième relais.** L'écart à la lettre du texte scellé est porté par GO-2026-11-20-55 (2), restreint par GO-2026-11-20-60 et précisé par GO-2026-11-20-63. Les trois sont postérieurs au scellement de la v9 (R-4271, 13:21Z) et cités exactement. Il est déclaré : juste.
  - Un point pour la mère : GO-67 dit « aucune recharge supposée », alors que la règle dit « reste relu après la recharge ». Les deux tiennent si la part se lit sur le reste relu, que la recharge ait eu lieu ou non. C'est la lecture du § 1 du complément.
- **Extension de l'arrêt n° 12 portée par une pièce de valeurs.** L'additif 1 v5 scellé la délègue lui-même au complément (§ 6, ligne 383 ; § 7). L'écart à la lettre de la v9, ligne 260, est donc couvert par une pièce scellée : déclaré, juste. Le texte de l'arrêt et son épreuve sont justes, y compris l'artefact « proposeur de l'espèce 2 sur la clé du deuxième relais ».

## 6. Les quatre recommandations, et les décisions de la mère (14:43Z)

1. **Arrêt n° 11, compte payant** : acceptée (a) ; texte corrigé, et la somme euros plus dollars ôtée (§ 4).
2. **Lignes à part** : la décision (b) remplace la recommandation pour Luc.
   - Le portier et le juge de l'espèce 3 de l'épreuve des témoins, et la sonde de l'espèce 4, se paient sur **Minuit**.
   - Les autres rôles se paient sur la clé de leur relais.
   - **Ce que cela retire de la part de Minuit : au plus 6 USD**, les plafonds des deux lignes (5 et 1 USD). La part devient **156,56 USD**, au-dessus du cas haut de 105,05 USD de 51,51 USD. Le reste de Minuit après les deux lignes reste au moins égal à sa part, donc l'arrêt n° 11 passe.
   - Le texte dit que la règle « un rôle, une clé » et l'artefact de l'arrêt n° 12 valent pour la course, non pour ces appels d'avant la course.
   - Un risque de la version 2 est fermé. La part de Luc était fixée avant les lignes à part, et l'arrêt n° 11 aurait lu le reste brut. Une dépense de lignes à part sur Luc aurait laissé partir une course dont la part et la réserve dépassaient le reste. Sans dépense sur Luc, ce cas ne se présente plus.
   - Une précision est ajoutée pour Rigaud et le troisième relais : leur sonde part après le relevé de Lazar. La pièce de relevés écrit donc le reste relu moins le coût de la sonde inscrit au registre. Sans cela, l'arrêt n° 11 lirait au départ un reste plus bas que la part, du seul coût de la sonde.
3. **Troisième relais sous son cas haut** : nœud de Lazar (c) ; texte corrigé.
4. **Fin du complément** : une pièce de relevés scellée par la mère vaut « complément scellé » au sens de GO-67, sans lot 2 (d). La branche « lot 2 » est retirée, ainsi que la phrase « dans les deux cas ».

**Sources** :
- Le chiffre « au plus 10,32 USD » du collisionneur sur Rigaud n'est sur aucune pièce de `main`. Il est remplacé par le renvoi au registre des dépenses et à R-4299.
- La table cite l'additif 1 v5 et le devis v11 comme non scellés. Ils sont scellés (R-4300) : la table reçoit leurs chemins et empreintes scellés, et une ligne pour R-4300.

## 7. Aucune recette

Le relevé (`releve_aucune_recette_v2.py`, sortie `sortie-releve-aucune-recette-complement-v2.json`) ne trouve sur le complément et son rapport ni valeur d'axe entière, ni marque de recette, ni case. Ses seuls signaux s'expliquent :
- un nom de fichier dans le complément, et le chemin du bloc-notes dans le rapport ;
- des noms de maison, dans les accords cités ;
- « chez Anthropic », mot de la mère sur Luc.

**Conforme.**

## 8. Corrections

Le texte exact fait foi dans `corrections-complement-valeurs-v2-v2.json` (28 remplacements, dans l'ordre du texte). Chaque ancre est comptée une fois, et chaque ancre entière apparaît une fois, par le programme `compter_ancres_v1.py`, qui rend le compte de `grep -c -F -e` pour chaque ancre. L'essai de l'outil sur une copie rend `674af0524365c05c6826528cca3ef7a1520d2da31d21f9a2f6e1e63fc24aa792`.

Le brouillon `corrections-complement-valeurs-v2-v1.json` (10 remplacements, d'avant les décisions de 14:43Z) est remplacé par ce jeu, qui le reprend.

| n° | lieu | objet |
|---|---|---|
| 1 à 3 | table des pièces | additif v5 et devis v11 scellés (R-4300) ; ligne R-4300 |
| 4, 6, 13, 16, 18 | § 0, § 1, ligne 2, § 3 | part de Minuit : 156,56 USD (b) |
| 5, 7, 14, 17, 19 | § 0, § 1, ligne 2, § 3 | part de Luc : 125,63 USD, au centime inférieur |
| 8 | § 1 | arrêt n° 11, règle acceptée (a) |
| 9 à 12 | § 1 | pièce de relevés scellée, sans lot 2 (d) ; phrase « dans les deux cas » |
| 15 | ligne 5 | clé des lignes à part, fixée (b) |
| 20 | § 3, Luc | renvoi : les lignes à part ne se paient pas sur Luc |
| 21 | § 3, Rigaud | 10,32 USD sans source, remplacé par le registre et R-4299 |
| 22 à 25 | § 3, lignes à part | décision (b), table, ce qui est retranché ; sonde de Rigaud et du troisième relais |
| 26, 27 | § 4 | règle acceptée (a) ; pas d'euros additionnés à des dollars |
| 28 | § 5 | troisième relais sous son cas haut : nœud (c) |

## 9. Points pour la mère

1. **Part de Minuit.** GO-2026-11-20-16 et la v9 (ligne 244) écrivent « Minuit 162,56 ». La part de 156,56 USD reste bornée par le solde (« plafonnée à son solde ») : c'est votre décision (b), et le texte le dit.
2. **La « borne des trois clés »** de la v9 et du devis (415,21 USD) n'est plus la somme des parts, qui changent pour Minuit et pour Luc. Les arrêts lisent clé par clé : rien n'en dépend. Mieux vaut le savoir avant la lecture du coût.
3. **Le véhicule** doit router les deux lignes à part autrement que la course : le portier et l'espèce 4 sur Minuit. L'épreuve de l'arrêt n° 12 ne doit pas refuser ces appels d'avant la course.
4. **La pièce de relevés** vaut complément scellé (d). Je recommande que son arithmétique soit refaite par un programme et constatée par `cmp`, comme les passes de cette chaîne, sans contre-lecture de fond.
5. **Les mots de la mère cités par le rédacteur** (restes vers 14:40Z, 10,32 USD) ne sont pas au registre. Le reste de Luc se vérifie sur `main` ; le 10,32 est retiré. L'heure donnée par la session de l'organisme est 14:35Z, celle du texte 14:40Z.
6. **Écart 5 du rapport.** Une sortie de l'outil du rédacteur est rangée sous `/root/.claude/`, non lue. À consigner.

## 10. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-1-v9/`. Chacun a son compagnon `.sha256` :
- `contre-lecture-complement-valeurs-v2-v1.md` (cette pièce) ;
- `corrections-complement-valeurs-v2-v2.json` ;
- `compter_ancres_v1.py` ;
- `sortie-releve-aucune-recette-complement-v2.json`.

Les essais de l'outil laissés dans le dossier sont des essais, non des pièces.

— contre-lecteur neuf, modèle O
