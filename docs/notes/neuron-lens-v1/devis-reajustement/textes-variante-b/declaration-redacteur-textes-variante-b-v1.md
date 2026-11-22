# Déclaration à part du rédacteur des deux textes de la variante B — ce qu'il savait du verdict du 18 — v1

- **Le lecteur de la seconde course ne lit cette pièce qu'à l'étape F du plan de lecture** (plan, brouillon 2, « Déclaration » et § 5.2 ;
  statut, brouillon 2, « Déclaration »). Elle porte des libellés et des valeurs du 18.
- Demandée par la correction S-4 (et P-2) de la contre-lecture `contre-lecture-textes-variante-b-opus-v1.md`
  (`a92149e88c7cadaaffefa28d99e370935500da1508bd7eb19b6b780b5a76980f`) : « Écrire la déclaration à part, avec le contenu retiré des
  l. 25-27 du statut et des l. 40-46 et 152 du plan. »
- Écrite par le correcteur neuf (mandat `mandats/mandat-correcteur-textes-variante-b-v1.md`, `125a59ff1fb4e4add1331aa816326a428b364f5260c9ebf4fef8ca70eb4800c1`),
  sur le commit `08896fd25`, le 2026-11-22 (`date -u` à l'ouverture : 2026-11-22T05:17:35Z). **Le contenu ci-dessous est recopié mot
  pour mot des brouillons 1**, phrases du rédacteur ; le correcteur n'y ajoute rien et n'a pas ouvert le verdict du 18 pour le vérifier.
  Scellée avec les brouillons 2 des deux textes.

## Pièces d'où le contenu est retiré (inchangées, R12)
| pièce | empreinte SHA-256 | lignes retirées |
|---|---|---|
| `statut-seconde-mesure-reajustement-v1-brouillon1.md` | `561e8ac275572b4a14392820e5e9be5a35bf7153f888bfa53fe4154b3b08ff03` | 25-27 (correction S-4) |
| `plan-lecture-seconde-course-reajustement-v1-brouillon1.md` | `ed802f8da81aee8af9255f4ffb2d25cbe851c46dbb556f5d6b5f276dcdfba457` | 40-46 (P-2 a), 152 (P-2 b), 170-171 (P-2 c) |

## 1. Retiré du statut, « Déclaration », troisième puce (brouillon 1, l. 25-27)
- **Je connais donc le verdict du 18** : « partiel » (rang 5) ; B-1 « autre » (différence entre moitiés au-dessus de 0,10 aux couches
  0, 1, 2 de R `mid`, 0 et 1 de R `out`, 31 de S `out`) ; B-2 « autre » (seule condition manquée : `pass` 0,8594 à la couche 8) ; B-3
  et B-5 « reproduit » ; B-6 « intermédiaire » (20 couches sur 21) ; B-7 « autre » (couche 15) ; aucun audit, aucune chaîne en défaut.

## 2. Retiré du plan, « Déclaration », deuxième puce (brouillon 1, l. 40-46)
- **Ce que je sais du 18**, donc, et qui touche ce plan : verdict « partiel » (rang 5) ; B-1 « autre », différence entre moitiés au-dessus
  de 0,10 aux couches 0, 1, 2 de R `mid` (0,1114 ; 0,1064 ; 0,1005), 0 et 1 de R `out` (0,1059 ; 0,1033), 31 de S `out` (0,1046) ; B-2
  « autre » (`pass` 0,8594 à la couche 8) ; B-3 et B-5 « reproduit » ; B-6 « intermédiaire » ; B-7 « autre » ; aucun audit ; aucune
  chaîne en défaut ; n = 64 partout. **Conséquence que je connais d'avance** : par la règle des couches stables du critère v8, § 5
  (« dans les deux ajustements », écrite avant moi), une lentille du palier 2 ne peut être dite lisible ni aux couches 0, 1, 2 pour R,
  ni à la couche 31 pour S, quoi que rende la seconde course. Et la règle de rang que je propose (§ 5, condition P2-3) admettrait la
  classe de verdict du 18 (rang 5) : je le déclare ; je l'aurais écrite de même, sans pouvoir le prouver.

## 3. Retiré du plan, § 5.2, dernière puce (brouillon 1, l. 152)
- Rappel déclaré (R4) : au 18, R dépasse 0,10 aux couches 0, 1 et 2, S à la couche 31 ; ces couches sont donc hors de Λ d'avance.

## 4. Retiré du plan, § 6 (brouillon 1, l. 170-171), recopié ici pour que rien ne se perde
La contre-lecture ne nomme pas ces lignes parmi celles que reçoit la déclaration ; elles sont retirées par P-2 (c) et recopiées ici
pour la même raison (valeurs du 18) : « les deux marges que nomme le devis v9, § 2 (`pass` de B-2 à la couche 8, 55 pôles sur 64 pour 58
exigés ; compte des couches de B-6, 20 sur 28 pour 21) ».

## Exposition du correcteur (R4)
J'ai lu en entier `CLAUDE.md`, le mandat, le mot de Lazar du 22 novembre, la contre-lecture, les deux brouillons 1 ; du critère v8,
les l. 352-420 (§ 5) et 521-530 (§ 7, K1), et la liste de ses titres. Je connais donc ce que ces pièces portent du 18 (le contenu
ci-dessus). Je n'ai ouvert ni le verdict du 18, ni l'accord de Lazar sur ce verdict, ni `diag/`, `runs/`, `docs/verdicts/`, ni aucune
branche `donnees/*`, `calcul/*`, `verdict/*`, `lecture/*`.
