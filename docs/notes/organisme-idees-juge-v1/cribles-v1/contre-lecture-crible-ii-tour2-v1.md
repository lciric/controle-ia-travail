# Contre-lecture, tour 2, du préenregistrement du crible (ii) « proposeurs en série », brouillon 2

- Lecteur : sous-agent neuf, modèle C (n'a écrit aucune pièce lue ; la pièce est du modèle A, les corrections d'un rédacteur d'un autre modèle).
- Pièce lue en entier : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-ii-brouillon2.md`
  (`fff278795f3ee4ba8a4f332bb80d687d7e2e773b55ebde2cabeae0e3912b7769`, recalculée, égale au compagnon).
- Version précédente : `crible-ii-brouillon1.md` (`816a072f6c9192049f325661e7b0ea2f0530dc1f738c4c39b8e75fba62364609`, égale au compagnon) ;
  rapport du tour 1 : `contre-lecture-crible-ii-tour1-v1.md` (`72f98c9ed64f1ee267a40087a66efdceaa7425de903de1b676e8bda74af5365e`, égale).
- Heure de rédaction : 2026-11-17, 01:38 UTC environ (`date -u`).
- Autres pièces lues : le verdict v2 du pilote (`e64458e8…`), par `git show` sur la référence distante de sa branche, empreinte du contenu
  recalculée égale, et seulement les lignes de ses sections « Comptes » et « Audit de symétrie » pour vérifier « x = 0 sur 14 » ; le
  différentiel scellé `diff-crible-ii-b1-vers-b2.txt` et le programme d'application (empreintes vérifiées, non relus en détail). Rien
  sous `diag/`, `runs/`, `donnees/` ; aucune branche `calcul/*` ni `donnees/*` ; aucune clé ; aucun appel ; aucune machine.

## 1. Verdict : corrections (trois mineures, aucune majeure)

Les 42 corrections du tour 1 sont appliquées fidèlement ; le différentiel ne contient rien d'autre que l'en-tête, le « Statut », la ligne du
validateur, la section « Contre-lecture » et un accord de grammaire déclaré. Les passages touchés se lisent bien et rien de ce que les corrections
ont pu déranger ne s'est cassé. Il reste trois défauts mineurs, tous de formulation, dont les couples sont en section 4. Aucun ne touche à la
conception ni au devis.

## 2. Les corrections du tour 1 sont-elles appliquées fidèlement ? Oui

Méthode : j'ai extrait du rapport du tour 1 ses 42 couples « ancien → nouveau » par programme (30 D1, 1 D2, 2 D3, 2 D4, 1 D5, 6 m1 à m5 :
m1.1, m2.1, m3.1, m3.2, m4.1, m5.1), vérifié que chaque « ancien » figure une seule fois dans le brouillon 1, les ai appliqués au brouillon 1
dans une copie de travail, puis comparé cette copie au brouillon 2 par `diff`.

Résultat : la copie et le brouillon 2 ne diffèrent que par :
1. le titre (« brouillon 1 » → « brouillon 2 ») et l'ajout de six lignes d'en-tête (datation, programme d'application, « rien d'autre que… ») ;
2. le « Statut » : « Brouillon 2, contre-lu une fois … second tour à faire » (remplace « Brouillon 1, non contre-lu ») ;
3. la ligne du validateur : « aucun défaut sur ce brouillon 2 » (je l'ai rejoué : liste vide, exact) ;
4. la section « Contre-lecture » remplacée par les deux empreintes et le traitement point par point (empreintes exactes, recalculées) ;
5. un seul écart dans un couple, **déclaré** par la pièce : D4.1, « seul son » devient « seuls son » (accord avec deux sujets). Légitime.

Aucun autre octet ne change : la section « Devis », l'annexe A, la sortie du devis, les empreintes de la rubrique « Documents qui font foi »
sont identiques au brouillon 1. Le différentiel scellé est un différentiel unifié du même changement. Les empreintes compagnons du
brouillon 2, du différentiel, du programme d'application et du brouillon 1 sont vérifiées par l'outil de scellement. Le décompte « 5 majeures,
5 mineures, 42 couples » de la pièce est exact. La pièce ne prétend pas avoir appliqué les remarques facultatives du tour 1 : exact.

## 3. Passages touchés relus, et vérifications que les corrections ont pu déranger

- **D1 (SP, SQ)** : il ne reste de « P1 » à « P4 » que le sens « session » (lignes relues une à une) ; plus de « P1 », « P2 » au sens de comparaison.
  Les lignes de la liste d'arrêt, des étages, du plan, de la puissance disent SP et SQ.
- **D2** : le cas manquant est lu (étages 4 « disperse », 5 « compte », 6 de signe négatif). Le symétrique côté grégarisme n'a pas de trou
  (si S < Q avec Q < P ou Q > P, « nuit » reste vrai). La nouvelle lecture renvoie à la même interdiction que « placebo mal apparié » : cohérent.
- **D3** : la règle (donneur écarté au-delà de 53 000 octets, jamais de carte retirée d'un bloc de Q, Q_k ne part pas si aucun donneur, chaîne de S
  continue, monde non complet pour SQ seulement) est cohérente avec la règle de taille (point 4 retire de la fin pour S seulement, m_k suit), avec la
  règle de chaîne, avec les étages 1 et 2 et avec la ligne d'arrêt « mondes complets atteignables < 16 pour SP et pour SQ à la fois ». La ligne
  neuve a son essai sain et son artefact. Seule la ponctuation de l'insertion est gênante (m2 ci-dessous).
- **D4** : « x = 0 sur 14 » est exact dans le verdict (section « Comptes » : x = 0 sur n = 14, 0 sur 84 emplacements) ; « 14 appels répondus » exact ;
  « le pilote ne dit rien de S contre P » exact. Mais deux phrases voisines se contredisent encore (m1).
- **D5** : refait. 1 275 − 840,67 = 434,33 ; (434,33 − 160 − 8 − 3) / 120 = 2,194, soit 2,19 ; 80 × 2,00 + 120 × 3,10 + 3 = 535 ; octets à 2,19 :
  (2,19 − 1,78) / 4e-6 − 1 024 = 101 476, soit « ≈ 101 000 » ; à 3,10 : 328 976, soit « ≈ 329 000 » du tour 1. Le texte dit désormais que 3,10 est une
  valeur d'exemple et que l'option (b) n'est hors de l'enveloppe qu'à ce plafond. Le « 535 » n'apparaît nulle part ailleurs dans la pièce. La
  recommandation (a) est inchangée, et reste à trancher par la mère.
- **m1 à m5** : appliquées exactement ; la phrase du test (« au moins 7 écarts non nuls … 7 suffisent s'ils sont tous du même signe ») est juste ;
  la citation « Devis » du crible (iii) est juste ; la zone utile de SQ et les étages 1 et 3 par principale sont cohérents avec les mondes complets
  par comparaison ; la dépendance par les donneurs est dite ; l'enchaînement des mondes d'une file est dit.
- **Devis, enveloppe, crédits et hors crédits** : section et sortie inchangées, rejouables comme au tour 1 ; 1 251,67 sur 1 275, marge 23,33 : tient.
- **R1, R3, R4, interdits** : inchangés et tenus (prédictions « non tranché » pour les deux principales, audit de symétrie avant le prononcé,
  rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque ; aucun identifiant de modèle hors les clés de configuration exigées par le bloc
  gelé et les lignes de GO, comme aux cribles (iii) et (v)). Rien de l'état de l'art n'est chiffré (R7).

## 4. Corrections demandées (toutes mineures)

Chaque « ancien » figure une seule fois dans le brouillon 2 (compté par programme).

### m1. « Aucune donnée » et « x = 0 sur 14 » dans la même phrase
Le « Statut » dit « sans aucune donnée de proposeur sur la couverture », puis, dans la même phrase, que le résultat principal (aucun des 14 appels
ne porte une conditionnelle entière) est lu : c'est une donnée de couverture par appel, d'une classe. Même contradiction en section « Prédiction ».
Une pièce gelée ne doit pas se contredire sur ce qui a été lu (R4). La section « Contre-lecture » signale ce point sans le corriger : à corriger
maintenant.

m1.1 — ancien :
```
**sans aucune donnée de proposeur sur la couverture** (le pilote
```
nouveau :
```
**sans donnée de proposeur sur la couverture des composantes comptées, hors la classe des conditionnelles** (le pilote
```

m1.2 — ancien :
```
sans aucune donnée de couverture par appel (le pilote ne la rend pas) ; seuls le résultat principal
```
nouveau :
```
sans donnée de couverture par appel des composantes comptées, hors la classe des conditionnelles (le pilote ne la rend pas) ; seuls le résultat principal
```

### m2. Parenthèse du placebo détachée de sa phrase par l'insertion de D3
Dans la règle des donneurs, « (réserve « placebo mal apparié ») » se rapportait au repli « donneur de longueur la plus proche » ; après D3.1 elle
suit « la chaîne de S continue » et semble couvrir le cas « aucun donneur », qui n'est pas cette réserve (celle-ci est définie à l'écart de longueur
de plus de 25 % dans plus de 4 mondes).

m2.1 — ancien :
```
(réserve « placebo mal apparié »). **Jamais**
```
nouveau :
```
(réserve « placebo mal apparié » pour le seul repli sur la longueur la plus proche ; le cas « aucun donneur » est compté à part, sans cette réserve). **Jamais**
```

### m3. L'en-tête dit « rien d'autre » alors que d'autres lignes changent
L'en-tête annonce que rien d'autre que les corrections, l'en-tête et la section « Contre-lecture » ne change ; le « Statut », la ligne du validateur
et l'accord « seuls son » changent aussi (tous déclarés ailleurs, mais pas ici).

m3.1 — ancien :
```
Rien d'autre que les corrections, l'en-tête et la section « Contre-lecture »
```
nouveau :
```
Rien d'autre que les corrections, l'en-tête, le « Statut », la ligne du validateur, l'accord « seuls son » de D4.1 et la section « Contre-lecture »
```

## 5. Remarques facultatives (aucune correction exigée)

1. Le titre de la section « Devis » garde « brouillon 1 » ; la pièce le dit (il nomme le programme du devis, inchangé). Rien à faire.
2. Les remarques facultatives du tour 1 (mot « brutes », annexe A, puissance à 16 mondes, légende des sigles) restent non appliquées ; elles ne
   gênent pas.
3. Après m1 à m3, la section « Contre-lecture » devra citer le tour 2 (empreintes de la pièce lue et de ce rapport) dans un brouillon 3 ; le tour 3,
   si la mère le juge utile, ne devrait avoir à vérifier que ces trois couples.

## 6. Pour la session mère

1. **Nœud de faisabilité** (inchangé, à trancher) : option (a) règle de taille, recommandée ; l'option (b) tient dans l'enveloppe à un plafond de
   2,19 USD (≈ 101 000 octets servis) mais est lourde (configuration neuve, plafond gelé modifié : écart à un texte scellé, nœud de Lazar).
2. **Écarts à la note** (proposeur, rang 1 commun, ordre non joué) : à confirmer par la mère ou Lazar avant la version qui fera foi.
3. **Marge de l'enveloppe** : 23,33 USD seulement ; la sonde rejouée en consomme 8.
4. **Valeur de l'essai** : puissance 0,11 à 0,47, issue la plus probable « non tranché » ; à garder en tête avant d'inscrire 400 USD.
5. **Compte rendu de l'auteur** (hors pièce) : le cumul « Pr-1 à 240 appels (1 375,27) » était faux au tour 1 (1 405,27) ; sans effet sur la pièce.
6. **Solde de crédits** : 408 USD au pire sur un seul fournisseur, à vérifier avant toute ligne.

## 7. Incidents de ma main

1. Un premier extracteur de couples n'en a trouvé aucun (expression régulière qui ne tolérait pas les lignes vides) : corrigé, 42 trouvés, sans effet.
2. Une première commande de comparaison de différentiels a imprimé beaucoup de texte inutile du brouillon (aucun fichier interdit) ; sans effet.
3. Pour retrouver le fichier du verdict, j'ai listé les noms de fichiers de la branche du verdict (noms seulement, dont des chemins sous `diag/`
   et `docs/` d'autres sujets) ; je n'ai lu que le verdict v2 du pilote. Rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis ni du bras d'attaque n'a été lu.
4. Fichiers de travail hors dépôt (dossier de travail de la session) : copie corrigée du brouillon 1, extracteur. Aucun fichier du dépôt modifié
   hormis ce rapport et son compagnon ; aucun commit.
