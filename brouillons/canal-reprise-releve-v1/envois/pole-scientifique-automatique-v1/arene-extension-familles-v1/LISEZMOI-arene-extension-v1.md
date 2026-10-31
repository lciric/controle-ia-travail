# LISEZMOI — extension de l'arène : familles qu'aucun moniteur seul ne couvre (Q3) et prix imposé à l'adversaire synthétique (Q3b) — v1

**Statut : brouillon 1, non gelé ; contre-lecture par un modèle autre qu'Opus ; puis gel des seuils par Lazar ; puis scellement ; calcul décisif après celui du pilote principal.**

Sous-agent neuf Opus 5.5 (lignée conv-audit), 31 octobre 2026. N'a écrit aucune pièce de l'arène v1 à v3. Modèle mathématique synthétique seulement (lois gaussiennes, moniteurs simples) ; aucun modèle réel, aucun texte, rien d'applicable à un vrai réseau ; l'objet est de certifier la couverture d'une défense et de mesurer le prix qu'elle impose à l'adversaire synthétique.

Ce que je n'ai **pas** fait : rien scellé, rien committé, aucun `.sha256` écrit, aucun fichier existant modifié (le dossier de l'arène principale est seulement lu ; une session parallèle y écrit ses fichiers v4), rien lu sous `donnees/`, aucun `git fetch`, aucun réseau, aucun appel de modèle ; **aucune graine tirée** des racines de décision (20265901, 20265902 ; 20261201 de l'arène principale) ni d'une racine déjà employée.

## Fichiers (tous nouveaux)

⟦FICHIERS⟧

## Ce que fait l'extension, en bref

1. **Constat avant code (gel § 2)** : à champ récepteur complet, l'union de deux maxouts est un maxout ; si l'union de deux moniteurs de la classe déployée couvre, un maxout seul de même total (73 unités) couvre aussi. Le régime demandé n'existe que pour une classe non fermée par l'union : **linéaire**, ou **« une vue »** (moniteur de n'importe quelle taille lisant un seul bloc de 3 coordonnées).
2. **Quatre familles appariées** par instance : N2 (deux modes opposés : aucun linéaire ne couvre, certificat d'enveloppe convexe), C2 (témoin couvrable), NV (un mode par vue : aucun moniteur d'une vue ne couvre, quelle que soit sa taille — certificat de loi marginale propre), CV (témoin).
3. **Couche exacte** : valeurs de référence V_pur, V_mél, V_union par formules fermées, selle certifiée à deux bornes.
4. **Machinerie de l'arène** (recopiée de la v3) mesurée contre la couche exacte : valeur du tirage, union contre mélange, cycle de la défense unique (I3 avec sa valeur nulle 0,7345 ; I4 avec 0,5).
5. **Q3b analytique** : gain maximal de l'adversaire synthétique (dommage × non-détection) sous activations seules, comportement seul, lecture jointe, en fonction du nombre L de vues surveillées.

## Ordre des étapes (journal)

⟦ORDRE⟧

## Commandes

```
cd /home/claude/controle-ia-travail
D=brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-extension-familles-v1
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider $D/essais/test_arene_extension_v1.py
python3 -I -B $D/arene_extension_v1.py identite
python3 -I -B $D/arene_extension_v1.py exact --instances 0:12          # couche exacte seule (racine d'essai)
# pilotes d'essai (racines de la plage 20265001–20265999 seulement) :
python3 -I -B $D/arene_extension_v1.py essai --instances 0:12 --sortie F.json --processus 2 --racine 20265011 --pids P.txt
python3 -I -B $D/arene_extension_v1.py prix --configs 0:120 --sortie G.json --racine 20265021
python3 -I -B $D/arene_extension_v1.py audit-essai --pilote F.json --instances 0:1 --sortie A.json
# décision (après le calcul décisif scellé du pilote principal, contre-lecture, gel des seuils, scellement, GO) :
timeout <S11> python3 -I -B $D/arene_extension_v1.py decision --prereg prereg/<nom>.md --run-principal <run-id> \
    --instances 0:<N> --configs 0:<M> --run-id <AAAAMMJJ-HHMMSS>-arene-extension-v1 --processus 2
python3 -I -B $D/arene_extension_v1.py orphelins --pids runs/<run-id>/pids-travail.txt [--arreter]   # avant toute reprise
```

## Racines lues

| Racine | Usage |
|---|---|
| 20265001 / 20265002 | essais du code |
| 20265011 | pilote d'essai Q3 et audit d'essai |
| 20265021 | pilote d'essai Q3b |
| 20265031 | mesure de temps (temps et compteurs seulement) |
| 20265041 / 20265042 | réservées, non employées |
| 20265901 / 20265902 | décision de l'extension : **jamais employées** |
| 20261201 et toutes les racines de l'arène (liste dans le code) | **refusées par garde** ; 20262297 et 20262313 (employées par décalage dans les essais v2, v3) ajoutées après le gel |

## Résultats du pilote d'essai (non opposables)

⟦RESULTATS⟧

## Temps

⟦TEMPS⟧

## Réserves et points ouverts

⟦RESERVES⟧
