# Devis — T0.7, étape B bis (sondes apprises sur la tâche) — v2

- **Auteur** : rédacteur neuf, sous-agent de la session mère, « modèle A ». **Date (UTC)** : 2026-11-14, v2 rédigée entre 11:52 et 12:09 (`date -u`) ; la v1 (`devis-etape-b-bis-v1.md`) reste (R12).
- **Ce qui change depuis la v1** (contre-lecture 1, `9c4107462ee828ae413755654b9af4cf85dd916d0ca345b9d439af6d392233ef`, constats m9 et M6) : disque et téléchargement de l'attendu dérivés ; téléchargement sourcé ; disque de la relance compté dans P2 (≈ 37,5 USD) ; garde de débit d'apprentissage ; nœud 4 : écart au gabarit (code cité après le scellement).
- **Statut** : devis avant toute machine (R-2716 (1) : « devis avant toute machine » ; R-2716 (3) : **aucune ligne de GO inscrite** ; la ligne s'inscrit sur le mot de Lazar au vu de ce devis). Aucune dépense engagée.
- **Arithmétique** : `pieces/calculs-bbis-v2.py`, sortie `pieces/sortie-calculs-bbis-v2.txt` (§ 5 et § 6), même dossier, empreintes dans leurs compagnons.

## En une ligne

Une instance A100 SXM4 80 Go, une marche de **4,0 à 5,7 h** (relecture forcée ≈ 0,35 à 0,55 h ; apprentissage ≈ 1,6 à 2,9 h) : **attendu ≈ 5,6 à 9,9 USD** ; pire cas sur A100, relance complète comprise (disque compris), **≈ 37,5 USD** ; plafond proposé **40 USD** (arrêt au cumul plus un quart d'heure ≥ 39,5 USD) ; H200 seulement sur mot de Lazar (≈ 58,1 USD au pire) ; lecture sur processeur : 0 USD.

## Sources des nombres (aucun chiffre de l'état de l'art ; aucun nombre de 7a, de 7b ni de T0.7)

- **Débit de relecture** : 0,45 s par passe d'épisode (108,4 s pour 240 épisodes de P3, A100 SXM4 80 Go), T0.6 scellé (`prereg/T0.6-organismes-v0-v1.md`, `ef31feff…`), « Devis », « Sources des chiffres ». Le recalcul de l'étape A de T0.7 a rejoué les 576 épisodes de 7b sur une A100 (R-2629) : même chemin de code pour la série O.
- **Prix** (T0.6, « Devis ») : A100 SXM4 80 Go attendu 1,0889 à 1,30 USD de l'heure, pire 1,40 ; relevés récents : 1,0867 (relance de l'étape A de T0.7, R-2622), 1,093 (7b), 1,12 (P3-bis) ; stockage au plus 0,08 USD de l'heure ; téléchargement au plus 0,05 USD par Go ; H200 NVL au plus 4,70 USD de l'heure.
- **Apprentissage** : **non mesuré à cette échelle** dans le programme ; supposé de 2 à 4 s par apprentissage sur la carte en double précision (300 époques, lot entier ; ≈ 143 000 jetons × 4 096 dimensions, soit ≈ 4,7 Go lus deux fois par époque, au débit mémoire de la carte) ; le pire cas double ces heures.
- **Téléchargement** (T0.6, « Devis ») : descente du modèle (≈ 16 Go en demi-précision), de l'image et du dépôt ≈ 20 Go, au plus 40 ; données de 7b ≈ 1 à 2 Go : **20 Go au bas de l'attendu, 40 au haut**.
- **Comparaison** : la pièce R du texte de validité, relecture et notation sans apprentissage, est chiffrée à 1,90 à 2,80 h (`prereg/validite-adaptateur-v1.md`, `7e78909d…`, « Calcul et dépense »).

## Postes (heures de carte A100 ; attendu bas et haut)

| poste | quantité | heures |
|---|---|---|
| mise en place (image, modèle ≈ 16 Go, dépôt, données de 7b ≈ 1 à 2 Go) | — | 1,0 |
| essais ciblés sur l'instance (suite ciblée, jouet, égalité carte-processeur, chemin de l'état imposé) | — | 0,5 |
| contrôles d'identité (adaptateur saboteur, adaptateur témoin : dose 0 au bit près, dose 1 différente) | 2 | 0,05 |
| **relecture forcée** et écriture des activations (trois couches, demi-précision, ≈ 49 Go) | 1 216 passes (O 576 ; J_d 256 ; J_instruit 64 ; A_d 256 ; A_T 64) × 0,45 s = 0,15 h de passe | **0,35 à 0,55** |
| garde d'équivalence sur la série O | 576 épisodes | 0,05 |
| **apprentissage** (chargement en double précision compris, 0,2 h) | 2 460 apprentissages : sondes de la tâche 730 (5 cellules × (2 plis × 4 plis internes × 18 réglages + 2)), lecteur honnête 730, nul de réétiquetage 1 000 (100 × 2 plis × 5 cellules) | **1,6 à 2,9** |
| planchers (800 directions par sonde finale) et notation de toutes les séries | 10 sondes finales × 800 directions ; 1 000 témoins | 0,2 à 0,4 |
| écriture des scores fermés, sceaux, poussée (morceaux < 95 Mo) | — | 0,2 |
| **total de marche** | | **3,95 à 5,65** |

## Montants (USD)

- **Calcul attendu** : 3,95 h × 1,0889 = 4,30 à 5,65 h × 1,30 = 7,35 (valeur centrale ≈ 5,6) ; **disque** : 0,08 × 3,95 h ≈ 0,32 au bas, 0,08 × 6,65 h ≈ 0,53 au haut ; **téléchargement** : 20 Go × 0,05 = 1,00 au bas, 40 Go × 0,05 = 2,00 au haut ; **attendu ≈ 5,62 à 9,88 USD**.
- **Pire cas** (scénarios cumulatifs ; aucune garde de temps, seule la garde de dépense arrête) :
  - **P1**, hôte deux fois plus lent, 1,40 USD de l'heure : 11,3 h → **≈ 18,8 USD** ;
  - **P2**, P1 plus une relance complète au même débit (erreur de chaîne avant les scores), disque de la relance compté : 22,6 h → **≈ 37,5 USD** ;
  - **P3**, H200 NVL à 4,70 USD de l'heure aux heures de P1 (**seulement sur mot de Lazar**) : **≈ 58,1 USD**.
- **Garde de débit** (constat M6 ; `pieces/sortie-calculs-bbis-v2.txt`, § 6) : après les 20 premiers apprentissages, si (heures écoulées) + (apprentissages restants × médiane × 1,2) + 0,6 h dépasse **11 h** (heures de P1), soit une médiane au-delà de ≈ 10 s par apprentissage, l'apprentissage s'arrête avant toute dépense de plus : instance arrêtée et gardée au plus 12 heures (disque ≤ 0,08 USD de l'heure, ≈ 1 USD), nœud de Lazar sur (r1) famille linéaire seule et 50 réétiquetages, ou (r2) autre offre ; sans mot, destruction par identifiant. Elle évite que la garde de dépense détruise l'instance sans scores.
- **Plafond proposé : 40 USD** (couvre P2 sur A100) ; arrêt et destruction par identifiant dès que le cumul relevé plus un quart d'heure de carte atteint **39,5 USD** ; aucune H200 sans mot de Lazar ; aucune relance au-delà d'une, ni après le samedi 21 novembre à 12:00 UTC, sans mot de Lazar.
- **Hors devis** : lecture et table conjointe (processeur, 0 USD) ; le **transfert de mode** (nœud 3) : s'il est décidé, la génération d'épisodes d'un mode tenu à l'écart et sa vérité du dommage demandent un devis à part ; les heures de rédaction, de code et de contre-lecture (sessions, non comptées ici).

## Offre et étiquette

A100 SXM4 80 Go, ≤ 1,30 USD de l'heure, ≥ 16 cœurs effectifs, ≥ 128 000 Mo de mémoire vive, disque ≥ 150 Go, stockage ≤ 0,08 USD de l'heure (bornes du point 9 de T0.6) ; étiquette **`bbis-t07-v1`** (ne commence ni par `t06` ni par `t07` : aucune garde d'inventaire d'une autre chaîne ne la compte) ; une seule instance, détruite par son identifiant après la poussée vérifiée (R10).

## Ligne de GO proposée (à inscrire sur le mot de Lazar ; texte proposé, non inscrit)

« calcul | T0.7, étape B bis : une instance A100 SXM4 80 Go pour la relecture forcée des jetons de 7b (séries O, J_d, J_instruit, A_d, A_T), l'apprentissage des sondes de la tâche, des lecteurs honnêtes et du nul de réétiquetage, et la notation fermée ; seulement après `SCELLEMENT-BBIS` (antérieure à toute exécution de l'étape B), `CODE-BBIS` contre-lu et la répétition à blanc ; une relance au plus ; garde de débit ; sortie scellée avant lecture ; arrêt et destruction par identifiant | **40 USD** | échéance **2026-11-22** | Lazar | R-2711 (3), R-2714 (2), R-2716 ; ce devis ». Ligne d'engagement au registre des dépenses avant la première minute (attendu, pire cas, dépense antérieure sous la ligne).

## Partage du code avec la pièce R du texte de validité

**Code seulement.** La relecture à état d'adaptateur imposé est la même fonction que celle que prévoit la pièce R (`prereg/validite-adaptateur-v1.md`, « Code neuf » : `relecture_v1.py`, état imposé ; aucune ligne `CODE-VADAPT` à ce jour) : un module neuf unique, écrit une fois, contre-lu une fois, importé sans modification par les deux textes, chacun citant ses empreintes. **Jamais** les données, les scores, les séries ni la lecture de la pièce R ; deux instances, deux marches, deux branches de données, deux registres. Le partage n'abaisse pas ce devis (les heures de carte restent celles de B bis) ; il épargne une écriture et une contre-lecture de code. Une marche commune avec la pièce R n'est pas proposée (deux chaînes scellées à part ; l'économie, ≈ 1 h de mise en place, ne vaut pas le mélange des sorties).
