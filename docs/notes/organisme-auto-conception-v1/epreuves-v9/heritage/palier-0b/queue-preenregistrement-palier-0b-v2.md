12. **Le rapport R du point 7 est une propriété du banc** (version 2) : il dépend du nombre de lois non plantées que la course source engage, de leur fréquence de « tient » et du nombre K ; à effort égal il vaut à peu près l'inverse du facteur d'enrichissement. Il ne dit pas ce qu'un vrai proposeur ferait d'un registre servi sans `resultat` ni `gardee`.
13. **Le bras de diagnostic a deux lectures**, et le bras 4b est un ajout du rédacteur (B7 bis). Son résultat sur le lecteur réglé pour la tenue est vrai par construction ; seul le côté du suiveur à la lettre et du coût est une mesure.
14. **Le seuil de « beaucoup plus de sources » (S9) est un choix du rédacteur**, écrit avant tout tirage et motivé par deux chiffres du devis et un calcul d'approximation. n₁ est lu jusqu'à six sources, sous le plancher de dix que le plan impose à deux contrastes : l'écart entre n₂ et n₁ contient donc aussi l'écart des deux planchers.
15. **La plage de K (0 à 256) et le décalage de l'artefact de la garde 23** sont des valeurs du rédacteur, sans appui mesuré.
16. **La liste de ce que reçoit l'expérimentateur garde la description**, bien que la forme imposée lui ôte sa raison (B4) : la réduire est posé à Lazar, non fait.

## Annexe E — Différentiel de la version 1 à la version 2

Mandat : `mandat-redacteur-preenregistrement-palier-0b-v2-v1.md` (empreinte en tête). La version 1 n'est pas modifiée. **Tout ce qui n'est pas nommé ici est repris à l'octet** : cette version est produite par 65 remplacements exacts sur la version 1, chacun trouvé une seule fois, et par l'ajout des réserves 12 à 16 et de cette annexe ; le programme (`appliquer_corrections_v2.py`) et le différentiel ligne à ligne sont dans le dossier de travail du rédacteur, à verser avec ce texte.

### Les onze corrections de la contre-lecture

| n° | correction | sort | où |
|---|---|---|---|
| 1 | (majeure) forme de la part M10 | appliquée dans les mots du contre-lecteur : D / (D + max(I, 0)) ; le pronostic du point 6 suit | M10 ; pronostic 6 |
| 2 | (majeure) le repli se mesure à effort égal | appliquée : un nombre fixe K de paires examinées par génération, le même au repli ; R dit propriété du lecteur écrit par programme et du banc ; part des entrées gardées et facteur d'enrichissement rapportés ; ligne « tenue sous le repli » retirée, sans objet par construction ; pronostic du point 7 récrit avec la mécanique | M7 ; S7 ; B7 (ligne du lecteur, réglage, « Le repli du point 7 ») ; famille D ; valeurs gelées (plage de K) ; pronostic 7 ; réserve 12 |
| 3 | règle de C1 et de C4 | appliquée. Le nombre de cases est écrit en chiffres (72 pour chaque critère) et le compte qui fait échouer aussi (5 236 sur 100 000), pour ne pas employer la lettre K deux fois | table des critères, C1 et C4 ; valeurs gelées ; B8, « Comparaisons multiples » ; garde 26 |
| 4 | classe d'issue tirée par loi et par monde | appliquée | B2 ; M12 ; S8 (i) ; B7, criblage ; hypothèse de travail (iii) |
| 5 | quatre gardes d'arrêt sans cas sain ni artefact | appliquée : gardes 23 à 26 ; le comparateur neuf redonne la table du palier 0a. Deux précisions du rédacteur : l'artefact de la garde 23 est chiffré et lu sur le seul bras où M1 dépend de la fréquence décalée ; la garde 26 plante des comptes et non un taux, pour ne pas dépendre d'une graine | B9 ; annexe C |
| 6 | ce que reçoit l'expérimentateur, le classement, l'ordre des opérations | appliquée ; le champ nommé est `enonce`, à confirmer à la lecture du code | B4 ; garde 11 ; ordre des opérations, 6 bis |
| 7 | taux d'échec auxquels se lisent C3, C4, C5 et m | appliquée | table des critères ; critères de lecture |
| 8 | d'où vient l'écart-type entre jumelles | appliquée : jumelles à l'étalonnage seulement, écart-type gelé dans le fichier des réglages | M9 ; B7, réglage |
| 9 | audit « vraies contre fausses » | appliquée, sur la forme écrite des lois de la clé | marges du générateur |
| 10 | essai de forme | appliquée | annexe C |
| 11 | Holm : l'autre contraste n'est pas sans effet | appliquée | B8 ; famille B ; ce qui est rapporté ; réserve 8 |
| forme | « suspendue » ; numérotation des manques ; « registre plein = 282 entrées » ; ordre d'engagement et domaine retenu ; longueurs des champs ; temps de calcul ; heure du rapport | appliquées ; l'heure est corrigée au rapport de la version 2, celui de la version 1 n'étant pas réécrit | critères de lecture ; annexe B ; B6 ; B7 ; annexe C |

### Les trois décisions de Lazar (`GO-2026-11-19-77`, option (a) chaque fois)

| décision | où |
|---|---|
| 1 — lecteur témoin réel au seul palier 1, puis décision ; aucune dépense engagée ici | table des trois décisions ; B4 ; réserve 10 |
| 2 — une tenue « établie » se dit « servir un registre tenu, forme comprise » | table des trois décisions ; critères de lecture (phrase gelée) ; réserve 3 |
| 3 — engagements à forme imposée aux paliers payants, avec les deux phrases du contre-lecteur et ce que cela change | table des trois décisions ; B4 (forme ; « Ce que la forme imposée change pour l'expérimentateur ») ; garde 11 ; réserve 16 |

### Les deux ajouts accordés par la mère, sans critère

| ajout | où |
|---|---|
| bras de diagnostic « registre d'une autre source », joué contre le suiveur de forme à la lettre | B7 bis ; M14 ; famille H ; garde 27 ; marges du générateur ; pronostic d'ajout ; réserve 13 |
| puissance du seul contraste de l'héritage, et condition chiffrée du devis (§ 9, nœud 4) | M13 ; S9 ; familles A et B ; critères de lecture ; valeurs gelées ; pronostic d'ajout ; réserve 14 |

### Autres changements

En-tête (version, dates, mandats, lignes d'accord relues sur `main`, calcul de la version 2, contre-lecture) ; section « Contre-lecture » (première contre-lecture inscrite, vérification à faire, points à vérifier) ; étape 1 de l'ordre des opérations ; information portée à Lazar sur le suiveur de forme qui répond à la taille du registre (B7).

### Ce qui n'est pas changé

L'hypothèse et son objet ; les six décisions de Lazar de la version 1 et l'écart déclaré à la lettre de N-058 ; les grilles, les 10 000 tirages, le taux d'échec, les tailles, les doses ; C2, C3, C5 et C6 dans leurs seuils ; les trois issues et la définition de n ; la liste d'arrêt ; l'annexe A ; l'annexe D (citations et listes « Ne pas écrire ») ; la racine des graines.
