# LISEZMOI — synthèse de l'audit des failles de notre contrôle — v2

Lignée conv-audit, sous-agent neuf de synthèse. **Pièce confidentielle** : dépôt privé seulement ; jamais dans la copie
publique ; jamais servie à un organisme. Horodatage : dernière ligne (heure lue sur `date -u` dans la commande qui l'écrit).

## Pièces

Dans `/var/tmp/audit-failles-controle-v1/sortie-synthese/`, chacune avec son compagnon `.sha256` :

| pièce | rôle |
|---|---|
| `audit-failles-controle-v2.md` | la synthèse v2 (remplace la v1, qui reste intacte) |
| `LISEZMOI-synthese-v2.md` | ce fichier : méthode, choix, table « constat → traitement », écarts |
| `calculs-synthese-v2.py` (`8ae28ec7…`), `calculs-synthese-v2.sortie.txt` (`3babde06…`) | vérifications des opérateurs E à I et calculs de prédiction (blocs 1 à 6) |
| `calculs-synthese-v3.py` (`bdc1464e…`), `calculs-synthese-v3.sortie.txt` (`bf392de2…`) | correctif du bloc 5 de la v2 ; combinaison entre modes ; erreur type d'une aire ; borne de Clopper et Pearson |
| v1, inchangées : `audit-failles-controle-v1.md` (`1e43b69c…`), `LISEZMOI-synthese-v1.md` (`16eef1a3…`), `calculs-synthese-v1.py` (`98f4c61b…`) et sa sortie (`2c2dc48f…`) | gardées ; compagnons vérifiés conformes au début de ce travail |

## Ce qui change par rapport à la v1

1. **Section 1 bis** : la troisième partie du rapport consolidé, deuxième version (`14a79c55…`), faille par faille (E à I) :
   affirmation, statut, antériorité stricte sur page, mathématiques de chaque opérateur, critique de chaque expérience
   (HR1 à HR5), ce qu'il faut pour tenir.
2. **Section 1 ter** : trente-deux hypothèses testables, une par faille ou grappe, au format du programme, chacune née
   d'un rapprochement avec un autre champ ; table de rattachement faille → hypothèse.
3. **Corrections de la contre-lecture** (table ci-dessous) ; deux antériorités ajoutées ; la règle de combinaison entre
   modes portée dans D-07.
4. **Quatre PDF de complément** lus aux pages citées (2601.21112, 2609.03026, 2607.08349, 2608.19338).
5. **Décisions** : dix-neuf (D-17 à D-19 ajoutées) ; avertissement 0.1 regradé et étendu à la troisième partie (points 8
   à 12) ; synthèse en dix lignes réécrite.

## Méthode

- Vérification des empreintes avant lecture : rapport v2 (PDF et texte, compagnons), contre-lecture (`7b8a17c3…`),
  `pdf-complement-v1/` (4 sur 4), pièces v1 (4 sur 4).
- Lecture de la troisième partie sur le PDF (pages 7 à 10), formules comprises ; pages 1 à 6 identiques à la première
  version (comparaison du texte page à page) ; la page 7 porte la fin du tableau de la partie 2 et le début de la partie 3.
- Antériorité : quatre passes de mots clés en mémoire (`python3 -I`, `pdftotext`), sans fichier intermédiaire, sur les 175
  PDF de L4 et les fichiers de L1 à L3, puis relecture des pages retenues sur les PDF hachés (annexes A et B). « Non
  trouvé » veut dire « non trouvé dans ces listes avec ces mots clés » (R8).
- Mathématiques : chaque opérateur est réduit à une identité vérifiable (E : (C_t − C_{t−1})₊ = (X_t − κ)₊ ; G : condition
  d'effacement linéaire), ou éprouvé sous un nul simplifié (F : indépendance contre effet épisode ; G : géométrie du
  plancher ; I : seuil hors plage, relais, petit nombre de moniteurs). Graines `SeedSequence(20261026)` ; aucune donnée des
  pilotes. Ce ne sont **pas** les expériences HR1 à HR5 (R1).
- Hypothèses : une par faille ou grappe ; témoin qui peut réfuter (R3, R5) ; prédictions chiffrées proposées, à figer au
  préenregistrement ; références d'autres champs classiques, non relues (R7).
- Contrôles avant scellement : expression de confidentialité fournie par le coordinateur (aucun résultat sur les deux
  fichiers `.md` de la v2) ; mots de la page de titre du rapport (aucun nom propre repris, hors Lazar) ; sigles ; colonnes
  des tableaux (aucune anomalie).

## Table « constat → traitement » (contre-lecture de la v1, `7b8a17c3…`)

| constat | traitement dans la v2 | où |
|---|---|---|
| CLS-01 : trois des « sept formulations » sont des nuances ; 1 et 2 à rejustifier | regradé : deux fausses ou dépassées (6, 7), deux contraires à R8 (1, 2), trois à nuancer (3, 4, 5) ; 1 : « phénomène voisin publié ; mécanisme non mesuré » ; 2 : rejustifié par les voisins de la loi elle-même ; 4 : « à préciser » ; 5 : « à borner par T2 » ; D-01 garde (a), enjeu reformulé | 0.1 ; D-01 |
| CLS-02 : « sans source » ; « q ≈ 0,75 » | « non sourcés dans le rapport (aucun chemin ni empreinte, R6) », sources probables nommées par N-003 ; seize chiffres ; « q ≈ 0,75 » sorti de la liste et gardé sur une ligne à part, comme valeur d'illustration (pour que la v1 et la v2 se comparent) | 0.1 ; 1.11 ; 9 |
| CLS-03 : FC-04, mécanisme et remède | FC-04 reformulée (délai Θ(γ) pour tout détecteur), repliée sur FI-04 ; tirage au hasard de κ et des seuils retiré (section 5.1, section 6 n° 10, grille) ; 2005.07821v1 gardé comme voisin | RC-1.3 ; 2 ; 3.5 ; 4.1 ; 5.1 ; 6 |
| CLS-04 : la clause « lecture principale » est née à la transcription | D-02 devient un retour au texte accepté ; vérifié sur les pièces (option (a) de session-depot, lignes 165 à 174 ; faits, ligne 622 ; contradiction déjà relevée par la cellule T1-B, ligne 85) ; cas cité dans D-11 | 0.2 ; 4.1 ; D-02 ; D-11 |
| CLS-05 : faille de tête (a) | « candidate (2509.21344 ; P3 ambigu) ; bloque la revendication « intention » tant que les négatifs ne sont pas appariés en indication » ; « l'outil le moins sûr » remplacé ; § 7.1 et § 7.3 de la source rappelés | 0.2 ; 2 ; 3.4 (FI-06) ; 4.1 ; D-02 |
| CLS-06 : accumulation créditable | D-08 (a) : statistique non créditable, calibrée sur suites d'épisodes honnêtes, contre une équipe rouge à mémoire ; FI-15 et section 6 n° 5 : voisin évalué sans mémoire (2411.17693v1, p. 10, vérifié) ; HT-18 | 2 ; 3.4 ; 6 ; D-08 ; HT-18 |
| CLS-07 : options sans avantage ni inconvénient | complétées : D-04 (c), D-06 (c), D-07 (b) (c) (d), D-08 (c), D-09 (b) (c), D-10 (b) (c), D-11 (b) (c), D-12 (b) (c), D-13 (a) (b) (c), D-15 (b) (c) | 8 |
| CLS-08 : quatre candidates sans leurs cinq parties ; FC-06 et FC-13 sans « ce qui tombe » | section 5.3 : FC-15, FC-16, FC-18, FC-20 instruites sommairement (cinq parties) ; « ce qui tombe » ajouté à FC-06 et FC-13 | 5.1 ; 5.3 |
| CLS-09 : N-047 = N-053 | dit une fois dans les conventions et en tête de la section 8 | en-tête ; 8 |
| CLS-10 : « répulsion d'Onsager » | conjecture retirée : « terme non défini dans le rapport, à faire définir » | RC-2.3 |
| CLS-11 : Dawid et Skene « cité p. 14 » | « référence classique, non relue ici » (p. 14 n'est qu'une entrée de bibliographie) | 3.4 (FI-09) ; 6 n° 13 et 19 ; HT-22 |
| CLS-12 : D-02 laisse tomber le plan 2 × 2 de FI-06 ; (ii) contestée comme témoin | plan information × accès ajouté à D-02 (a) et à HT-16 ; G1-P1 sur (iv) quand elle existe, renvoi à D-14 | D-02 ; HT-16 |
| CLS-13 : phrase à adoucir | « le bruit honnête borne la détectabilité (FI-10) » | 4.1 |
| CLS-14 : FC-01, effet non séparé | « effet non séparé entre témoin et mention » ; HT-21 prévoit le témoin sans mention | 5.1 ; HT-21 |
| CLS-15 : FC-02, ancrage | « indécidable pour P3 sans son préenregistrement (non fourni) » ; et, nouveau, « le plancher aléatoire n'est pas un contrôle des confusions » (calcul v2, bloc 3) | RC-1.4 ; 3.5 ; 5.1 ; RC-3.3 |
| Antériorité 1 : 2410.12555 (directions aléatoires appariées à la covariance) | cité comme voisin de méthode du colmatage de 1.4 et de G, **non vérifié sur PDF (R7)**, tel que la contre-lecture l'a lu | RC-3.3 ; FC-02 ; 9 |
| Antériorité 2 : FC-11, billet d'Anthropic | rien à changer : FC-11 reste « non trouvée », statut « question » ; HT-24 | 5.1 ; HT-24 |
| Manque 1 : règle de combinaison entre modes après N-054 | ajoutée à D-07 (options intersection-union, mode tenu à l'écart décisif, règle libre) ; calcul v3 (14,26 % et 2,97 %) ; HT-32 | D-07 ; HT-32 |
| Manque 2 : clause née à la transcription | cas cité dans D-11 | D-11 |
| Manque 3 : accumulation créditable | voir CLS-06 | D-08 |
| Manque 4 : incertitude propre du plancher | quantifiée sous nul simplifié (écart type du quantile 0,95 de 200 directions : jusqu'à 0,014 selon la géométrie) ; gardée comme précision | RC-3.3 ; 2 |

Corrections que je ne suis pas : aucune. Deux nuances : pour CLS-02, « q ≈ 0,75 » est sorti de la liste des chiffres non
sourcés mais reste visible sur une ligne à part ; pour CLS-07, j'ai aussi complété des options « statu quo » que la
contre-lecture permettait de laisser nues.

## Choix

- **Une v2 complète plutôt qu'un complément** : la v1 a été copiée puis corrigée et augmentée, pour que Lazar lise une
  seule pièce ; la v1 reste intacte, scellée.
- **Numérotation** : les ajouts prennent les numéros 1 bis et 1 ter, pour que les renvois de la v1 et de la contre-lecture
  restent valables ; ils sont placés tôt, selon la priorité demandée (troisième partie et hypothèses avant la grille).
- **Une hypothèse par faille ou grappe** : trente-deux hypothèses couvrent les quinze affirmations du rapport, les failles
  que le rapport ne voit pas, les candidates et les grappes de la grille ; « profondeur plutôt que nombre ».
- **Confidentialité** : aucun montant du rapport (ses coûts annoncés sont décrits sans chiffre) ; le rapport est désigné
  par son empreinte ; aucun nom de sa page de titre hors Lazar.
- **Sûreté** : les mécanismes d'attaque de la troisième partie sont résumés au niveau de la méthode, sans procédure ni
  exemple ; les hypothèses décrivent des mesures et des témoins.

## Écarts déclarés

1. Le bloc 5 de `calculs-synthese-v2.py` imprimait une colonne « prédiction » fausse (fiabilité de v₀ au lieu de la
   fiabilité R du régresseur) ; les pentes simulées y sont justes ; la v2 n'a pas été réécrite (R12) : `calculs-synthese-v3.py`
   donne la formule juste, vérifiée (HT-11).
2. Les calculs v2 éprouvent des opérateurs sous des nuls simplifiés que j'ai choisis (τ = 0,3 et 0,6 ; géométries du
   plancher) ; ils ne disent rien des scores réels.
3. Quatre PDF de L4 cités ont une empreinte sur disque absente des listes de provenance (annexe B) ; 2410.12555 n'est connu
   que par la contre-lecture.
4. Les deux derniers messages du coordinateur (contre-lecture, PDF de complément) sont arrivés avant la clôture : intégrés
   dans la v2 elle-même, sans v2 bis.
5. Le rattachement des lignes de la grille aux hypothèses passe par les grappes de la section 6, non par une colonne dans
   chaque ligne.
6. Les additions de la v2 (sections 1 bis et 1 ter, D-17 à D-19) n'ont pas été contre-lues (R2 : à faire avant toute
   transmission).

## Ce qui reste

- Contre-lecture des ajouts de la v2 par une instance neuve d'un autre modèle.
- Vérification sur PDF des références classiques d'autres champs avant tout préenregistrement d'une hypothèse (R7).
- Pièces non fournies : T0.3 et la note mathématique v2 (sources probables des seize chiffres), préenregistrements de P3,
  P4 et P3b, brouillon 7 du papier C, code de l'organisme.
- Les dix-neuf décisions de la section 8.

---
Horodatage : version close le 2026-10-26 à 13:56:09 UTC (heure lue sur date -u dans la commande qui écrit cette ligne).
