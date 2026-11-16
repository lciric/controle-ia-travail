# Contre-lecture, tour 3, de l'addendum de relance de l'idée 1.1 (brouillon 3)

Lecteur neuf, lettre C (n'a écrit aucune des pièces). Pièce lue en entier pour les zones touchées :
`docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon3.md`
(`7b11231c58b86e8999d0b6a3740a533473c8093be131107439404fcfe7075c81`, égal à son compagnon). Brouillon 2 :
`566304ede89c8aab86682bd9a7602e20b307e97fadce2071ea46ffed87a3ee4a`. Rapport du tour 2 :
`9460579c29d43f9129c96657a38ebacea899aac03288502ee078c5319f965675` (égal à son compagnon). Lu le 2026-11-16 de 20:41Z à 20:43Z (`date -u`),
sur la tête `e10a66b7` de `main`. Aucun fichier du run invalide ouvert ; aucun jeu, aucun `pytest`, aucun réseau.

## Verdict : « corrections » — 0 majeure, 1 mineure exigée (e-1), 1 remarque facultative (h-1). La conception n'est pas en cause.

## 1. Corrections du tour 2 et différentiel (`diff` brouillon 2 / brouillon 3)

Trois zones seulement, rien d'autre : ligne 18 (d-1), ligne 24 (nouvelle puce « Version : brouillon 3 » et « Statut et lieu »), lignes 364-365 (section 7).
- **d-1** : l'« ancien » du rapport du tour 2 devient exactement le « nouveau » demandé ; appliqué mot pour mot.
- **g-1 et g-2** : non appliqués, facultatifs ; traitement déclaré au § 7, recevable.
- Le § 7 rapporte fidèlement le rapport du tour 2 (0 majeure, 1 mineure, 2 facultatives ; c-1, c-2, c-4 mot pour mot ; c-3 à un renvoi près ; heures ; empreintes vérifiées).
- Empreintes citées et vérifiées : brouillon 2, rapport du tour 2, programme du brouillon 2 (`03164886…`, égal à son compagnon) ; programme du brouillon 3 (`885acb92…`) et pièce : `verifier` rend OK.
- Rien dans les passages touchés n'a dérangé le reste : annexe A (programme `b9664f76…`, sortie `f457df14…`) inchangée par le différentiel ; les chiffres de l'état du run invalide sont donc inchangés.
- Hygiène : zéro ligne au format du lanceur (`^[0-9a-f]{64}  `), zéro ligne commençant par 64 caractères hexadécimaux ; aucun identifiant de modèle ; lettres A et C seulement.
- Les 46 fichiers gelés : `git diff a6bc9938 e10a66b7` ne touche aucun d'eux (18 fichiers, tous des pièces de l'addendum, `registres/decisions.md`, `registres/go.md`, un manifeste de run).

## 2. Correction exigée (mineure)

**e-1 — En-tête, puce « Version : brouillon 3 » : même erreur que d-1, reportée sur la nouvelle puce.** La puce dit « rédacteur neuf, lettre C … qui n'a écrit ni les brouillons 1 et 2,
ni leur programme d'application ». Or, d'après la consigne de ce tour, les corrections ont été faites par le modèle A, qui a écrit les brouillons 1 et 2 et le programme du brouillon 2 : « neuf », « lettre C »
et « n'a écrit ni les brouillons 1 et 2, ni leur programme » sont faux, et la lettre C est celle du lecteur (moi). Le § 7 (d-1) dit pourtant lui-même que les corrections du brouillon 2 sont de A : la pièce se contredit.
Le programme `appliquer-…-brouillon3.py` porte vraisemblablement le même texte ; à signaler comme pour le programme du brouillon 2 (R12 : on ne l'écrase pas). Si la mère sait que les corrections du brouillon 3 ont été faites en fait par un rédacteur de lettre C, la phrase tient : à confirmer par la mère.
Couple (l'« ancien » figure une fois ; il s'étend sur deux lignes ; vérifié par `grep -cF` : 1 pour chaque ligne) :

- ancien :
```
  rédacteur neuf, lettre C, sous-agent de la session mère, qui n'a écrit ni les brouillons 1 et 2, ni leur programme
  d'application, ni les rapports de contre-lecture des tours 1 et 2, ni [T], ni [AE], ni le code, ni l'étape 0 : couples
```
- nouveau :
```
  rédacteur, lettre A (le modèle des brouillons 1 et 2), sous-agent de la session mère, qui n'a écrit ni les rapports
  de contre-lecture des tours 1 et 2, ni [T], ni [AE], ni le code, ni l'étape 0 : couples
```

## 3. Remarque facultative

- **h-1** : la source de `registres/decisions.md` (l. 40, `17f8672b…`) est celle de l'objet de `main` a6bc9938 (cf. l. 653) ; sur `e10a66b7`, citée par la puce du brouillon 3, le fichier vaut `9902dbf1…` (et `go.md` `dfa8ffb7…`). Pas de contradiction si lu avec l. 653 ; pour lever l'ambiguïté, remplacer
  ancien : `` `registres/decisions.md` (`17f8672b29ca0a1deb0529836a60225fdc14f63aadeb6a9ce62b9f691c9ef7e3`) et `registres/go.md` `` → nouveau : `` `registres/decisions.md` (objet de `main` a6bc9938 : `17f8672b29ca0a1deb0529836a60225fdc14f63aadeb6a9ce62b9f691c9ef7e3`) et `registres/go.md` ``
  (le début de ligne coupe après « go.md » ; vérifier l'unicité avant application).

## 4. Points pour la mère

1. **Lettre du rédacteur du brouillon 3 (e-1)** : à confirmer ou corriger avant la recopie sous `prereg/`.
2. **Écart à un texte scellé (lieu (ii))** : une machine louée contredit [T] l. 629 et 660 ; D7 est à demander à Lazar en toutes lettres avec la question de R-3010. Sans son mot, aucune machine louée ne part. Le lieu (i) n'en demande aucun.
3. **`--reprendre` reste accepté par le code** dans la copie du run invalide ; seule la règle écrite l'interdit : l'opérateur ne le passe jamais.
4. **Risque du lieu (i)** : une reprise a déjà été imposée malgré une tâche active (20:11Z) ; égalité au bit près non garantie sur un autre processeur (limite déclarée, sans effet sur la validité).
5. À la recopie sous `prereg/` : recompter les lignes au format du lanceur (attendu 0), recalculer les empreintes du § 8, compléter la déclaration, nettoyer « ce brouillon » (g-1 du tour 2).

## 5. Incidents de ma main

Aucun. Seul fichier créé : ce rapport et son compagnon.
