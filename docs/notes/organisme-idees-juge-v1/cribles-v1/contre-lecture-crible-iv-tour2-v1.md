# Contre-lecture, tour 2, du préenregistrement du crible (iv) « demi-générations », brouillon 2

- Lecteur : sous-agent neuf, modèle C (n'a écrit aucune pièce lue ; la pièce est du modèle A, les corrections sont du modèle A en fichiers neufs).
- Pièce lue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iv-brouillon2.md`
  (`603306b98180b33ea2c585fe8f33ad45c714a763a976819a9b53c49e563b069f`, recalculée, égale au compagnon).
- Pièces comparées : brouillon 1 (`079f8599…`, égal à son compagnon) ; rapport du tour 1 (`e7853abe…`, égal) ; programme
  `appliquer-corrections-crible-iv-brouillon2.py` et `diff-crible-iv-b1-vers-b2.txt` (compagnons égaux).
- Heure de rédaction : Tue Nov 17 01:41:07 UTC 2026 (`date -u`).
- Lectures : uniquement des fichiers du dossier des cribles ; aucune branche, aucun fichier sous `diag/`, `runs/`, `donnees/` ; aucune
  clé ; aucun appel de modèle ; aucune machine ; aucune dépense ; aucun fichier existant modifié ; aucun commit.
- Incident de ma main : aucun.

## 1. Verdict : corrections

Les six couples du tour 1 sont appliqués fidèlement et le différentiel ne contient rien d'autre que l'en-tête, le statut, la ligne
du validateur et la section « Contre-lecture ». Mais la correction M2 laisse, dans une **lecture gelée** (étage 2), une phrase
exigée contradictoire avec celle de l'étage 4 : c'est à corriger avant scellement (1 majeure, 2 mineures). La conception n'est pas en cause.

## 2. Fidélité des corrections (vérifiée par programme)

Les 6 couples sont relus dans le rapport du tour 1 : chacun a son « ancien » exactement une fois dans le brouillon 1, son « nouveau »
exactement une fois dans le brouillon 2, et son « ancien » zéro fois dans le brouillon 2. En appliquant les six couples au brouillon 1,
la différence avec le brouillon 2 est **exactement** : titre ; ligne « Brouillon 2 : corrections… » ; paragraphe « Statut » ; ligne du
validateur ; section « Contre-lecture » (remplacée par « Contre-lecture 1 » et « Tour 2 à faire »). Rien d'autre (confirmé par `diff`
direct, 6 blocs de couples + ces 5 zones). Le validateur `controle_ia.prereg.problemes` rend une liste vide, comme la pièce le dit.
Le traitement point par point de la section « Contre-lecture » est exact (M1, M2, M3, m1, m2 acceptées telles quelles ; remarques
facultatives non appliquées) ; la liste « non corrigé par le rapport » du brouillon 2 est exacte.

## 3. Passages touchés relus

- M1 (bras 3 : 2a' puis 2b' l'un après l'autre, garde avant chacun) : cohérent avec la garde du point 3 et avec le bras 2. Le chemin du
  bras 3 après 1a (3 appels, 2 tours de chaîne) reste plus court que celui du bras 2 (3 appels, 4 tours de chaîne) : les durées du devis
  (programme inchangé, commentaire « bras 3 en parallèle, plus court ») tiennent. La ligne « tours de chaîne : après 2a' et 2b'
  ensemble » (l. 229) reste juste : « ensemble » y dit que le tour juge les deux jeux de cartes à la fois.
- M2.1 : l'étage 4 est complet et la clause ρ_21 est cohérente avec la définition de ρ_21 (= dépense du bras 2 sur celle du bras 1).
- M3.1 : les cinq puces de la traduction couvrent les six combinaisons d'étages 4 et 5 sans recouvrement : « davantage » + « compte »,
  « davantage » + « non tranché », « moins » + « nuit » (3e puce), « moins » + « non tranché » (3e puce), « non tranché » (4e puce), et les
  deux croisés (5e puce). Plus aucune mention de « incohérente ».
- m1.1 et m2.1 : exactes (m = 48 est bien `M_REGLE` ; les retenues par bras sont dites propres).
- Devis, enveloppe, durées, interdits, absence d'identifiant de modèle : non touchés par le différentiel ; chiffres inchangés,
  vérifiés au tour 1 ; je ne les ai pas refaits (sortie scellée inchangée, programme inchangé).

## 4. Corrections exigées

### M1 (majeure). Étage 2 du tableau gelé : le complément exigé dit « à dollars égaux » alors que l'étage 4 exige « à dollars proches (ρ_21 dit) »
Après M2, la phrase « les demi-générations couvrent moins » porte deux exigences incompatibles : l'étage 4 la veut « à dollars proches
(ρ_21 dit) », l'étage 2 (réserve « demi-générations amputées ») l'interdit sans « à dollars égaux, avec une génération 2 amputée dans
k mondes », or la garde souple n'assure pas l'égalité (ρ_21 jusqu'à ≈ 1,3, et à l'inverse moins de 1 si c3/c6 < 0,5). Une lecture gelée
ne doit pas pouvoir être prononcée de deux façons.

M1.1 — ancien :
```
la phrase « les demi-générations couvrent moins » est alors interdite sans le complément « à dollars égaux, avec une génération 2 amputée dans k mondes »
```
nouveau :
```
la phrase « les demi-générations couvrent moins » est alors interdite sans le complément « à dollars proches (ρ_21 dit), avec une génération 2 amputée dans k mondes »
```

### m1 (mineure). « Ce que serait chaque issue » : la lecture « moins » garde « à dollars égaux »
Même défaut, dans la description des issues (R3).

m1.1 — ancien :
```
signe négatif ; à dollars égaux, payer
deux fois l'entrée pour trois cartes de moins par appel
```
nouveau :
```
signe négatif ; à dollars proches (ρ_21 dit), payer
deux fois l'entrée pour trois cartes de moins par appel
```

### m2 (mineure). En-tête : la phrase « Rien d'autre… ne change » est inexacte
Le statut et la ligne du validateur changent aussi (dits ailleurs, mais pas dans cette phrase).

m2.1 — ancien :
```
Rien d'autre que les corrections, l'en-tête et la section « Contre-lecture » ne change.
```
nouveau :
```
Rien d'autre que les corrections, le titre, le statut, la ligne du validateur, cette ligne et la section « Contre-lecture » ne change.
```

## 5. Remarques facultatives (aucune correction exigée)

1. Les occurrences restantes de « à dollars égaux » (§ 0 points 1 et 7, énoncé de H-iv, prédiction IV-1, citation de la note au point 3
   de « Choix et doutes ») énoncent la question de la note et l'hypothèse visée, et la garde souple est dite au point 3 : je les laisse
   telles quelles ; les rendre « à dollars proches » serait plus rigoureux, au choix de la mère.
2. Le complément de l'étage 4 dit « dépassement borné par un appel » ; IV-9 dit « un demi-appel par monde » : même sens, vocabulaire à harmoniser si on veut.
3. Les remarques facultatives du tour 1 (seuil de la sonde plus bas que la coupe, profondeur informative pour le seul bras 2, sigle
   « e-BH ») restent valables et non appliquées.

## 6. Pour la session mère

- Appliquer M1.1, m1.1, m2.1 en fichier neuf (brouillon 3) ; un tour 3 se réduit à vérifier ces trois couples et le différentiel.
- Aucun écart à un texte scellé ; aucun mot de Lazar nécessaire pour ces corrections.
- Risques inchangés : sonde et rapport c3/c6 (pièce « non lançable » si au moins deux tiers), marge d'enveloppe de 11,33 USD, équivalence
  du nul v8 à vérifier au code.
