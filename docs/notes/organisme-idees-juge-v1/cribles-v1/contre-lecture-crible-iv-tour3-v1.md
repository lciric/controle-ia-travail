# Contre-lecture du crible (iv), tour 3, brouillon 3 — lecteur neuf C (rédigé le 2026-11-17, `date -u` 02:05)

Pièce lue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iv-brouillon3.md` (empreinte compagnon vérifiée).
Lecteur : C, neuf ; n'a écrit aucune pièce. Aucune machine, aucun appel de modèle, aucune dépense, aucune branche `calcul/*`
ni `donnees/*`, aucune modification, aucun commit. Aucun incident de ma main.

## 1. Verdict : scellable

La pièce peut être scellée telle quelle. Aucune correction exigée. Remarques facultatives en § 4.

## 2. Fidélité des corrections (vérifiée)

- Empreintes : brouillon 2 = `603306b9…` (conforme à celle citée), rapport du tour 2 = `ca94c2ca…` (conforme), brouillon 3, programme
  de correction (`6900589e…`, conforme à celle citée) et différentiel : empreintes compagnons toutes valides.
- `diff` direct brouillon 2 → brouillon 3 : exactement sept blocs, tous attendus : titre ; ligne « Brouillon 2 » de l'en-tête (couple
  m2.1) ; nouvelle ligne « Brouillon 3 » ; statut ; ligne du validateur ; ligne de « Ce que serait chaque issue » (m1.1) ;
  étage 2 du tableau gelé (M1.1) ; section « Contre-lecture » (entrée 2 et « Tour 3 à faire » à la place de « Tour 2 à faire »).
  Rien d'autre. Le différentiel scellé (`diff -u`) est identique au mien, ligne à ligne.
- Les trois couples sont exactement ceux du rapport du tour 2 : « ancien » présent une fois dans le brouillon 2, zéro fois dans le 3 ;
  « nouveau » une fois dans le 3. (Le couple m1.1 s'étend sur deux lignes : vérifié par lecture du texte entier.)
- Le traitement point par point de la section « Contre-lecture 2 » est exact (M1, m1, m2 acceptées telles quelles ; remarques
  facultatives non appliquées ; points 1 à 3 du § 6 du rapport pris en compte).

## 3. Passages touchés et vérifications dérangées

- Cohérence demandée : étage 2 (ligne 486), étage 4 traduit (ligne 499), « Ce que serait chaque issue » (ligne 220) disent tous trois
  « à dollars proches (ρ_21 dit) » pour la lecture « moins ». Plus aucune exigence contraire.
- Les occurrences restantes de « à dollars égaux » (lignes 105, 124, 152, 188, 494, 698) énoncent la question de la note ou
  l'hypothèse visée, et non une phrase exigée de lecture ; elles sont citées et laissées par le rédacteur. Acceptable (voir § 4).
- Lignes « Brouillon 2 » et « Brouillon 3 » de l'en-tête : disent exactement ce qui a changé.
- Validateur `controle_ia.prereg.problemes` rendu sur le brouillon 3 : liste vide.
- Devis, enveloppe, durées, interdits : non touchés par le différentiel (programme et sortie du devis inchangés) ; non refaits.
- R1, R3, R4 : sections et audit de symétrie non touchés, vérifiés au tour 1.
- Identifiants de modèle : la seule occurrence est la clé de configuration `opus55`, déjà dans le brouillon 2, justifiée par la pièce
  (ligne 314, R-2598). Inchangé.

## 4. Remarques facultatives (aucune exigée)

1. L'énoncé de H-iv, la prédiction IV-1 et la question du § 0 gardent « à dollars égaux » : écart de vocabulaire avec « à dollars
   proches (ρ_21 dit) » des lectures, mais il est dit au point 3 que la garde est souple. À la mère.
2. Vocabulaire « dépassement borné par un appel » / « un demi-appel par monde » non harmonisé : même sens.
3. Remarques facultatives du tour 1 (seuil de la sonde, profondeur informative, sigle « e-BH ») : toujours ouvertes.

## 5. Corrections

Aucune.
