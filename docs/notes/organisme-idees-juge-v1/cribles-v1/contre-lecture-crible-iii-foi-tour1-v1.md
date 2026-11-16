# Contre-lecture, tour 1 — crible (iii), version qui fera foi, v1 (tour différentiel)

- Lecteur : sous-agent neuf du modèle C (R2) ; n'a écrit ni la pièce, ni les brouillons, ni aucun rapport de ce crible.
- Écrit le 2026-11-16, de 23:22Z à 23:26Z (`date -u`). Aucun fichier existant modifié, aucun commit, aucune machine, aucun appel
  payant, aucune clé employée, aucune dépense. Aucun incident de ma main.
- Pièce lue : `crible-iii-version-foi-v1.md` (`91b4bf30fbf8b83d2c057088d8776be19831b006f1010bcb3c7e2e231d2c7179`, égale à son
  compagnon). Comparée au brouillon 8 (`d3406878…`). Lu aussi : différentiel (`ba14c9e6…`), programme d'application,
  programme de devis (`0a0795d1…`) et sa sortie (`80fe8855…`), lignes R-2977, R-2992, R-2993, R-3005 de `registres/decisions.md`,
  lignes GO-2026-11-15-06 et GO-2026-11-16-08 de `registres/go.md`, `registres/depenses.md`, rapports des tours 1 et 2 de la
  lecture du brouillon 7 (empreintes 4803c83b…, 87501081… vérifiées), et, par `git show` sur la référence distante déjà présente
  (sans `fetch`), la définition de « tronqué » dans le texte du pilote. Rien du verdict du pilote n'a été ouvert ; aucune branche
  `calcul/pilote-mr2-v74-entree-*`.

## Verdict : scellable

Aucune correction exigée. Six remarques facultatives en fin de rapport.

## 1. Différentiel : rien d'autre que les valeurs refaites

- Je refais `diff -u` brouillon 8 contre la pièce : sortie identique, ligne à ligne, au fichier de différentiel fourni (14 blocs
  `@@`, comptés).
- Les 14 blocs sont : en-tête (titre, puce de la version, documents, statut), section 0 (points 8, 9, 10), « Seuil » (taux, probabilité),
  table des proposeurs, devis (titre, hypothèses, table, écart à la note, puce de durée, sous-section neuve), lignes de GO et
  enveloppe, « Choix et doutes » (8, 12, 13), « Contre-lecture » (entrée 8, « Tour suivant »).
- **Aucun bloc ne touche la table des prédictions** (lignes III-1 à III-7, l. 233 à 239 de la pièce) ni leurs « Raisons », ni les
  critères gelés, ni la liste d'arrêt, ni le plan d'analyse, ni l'annexe A : aucun hunk dans ces plages. Prédictions III-1 à III-6
  identiques à l'octet à celles du brouillon 8 ; III-7 inchangée (1,05 à 1,25), conformément à la règle écrite sous la table de
  mise à jour (aucune sonde jouée) et à R-2993.
- Les cellules de la table des proposeurs et du devis qui changent sont toutes des « attendus » refaits ; les colonnes de jetons et
  les plafonds restent ceux du brouillon, et la pièce le déclare (colonnes non relues).
- Aucun identifiant de modèle dans la pièce : seules les clés de configuration exigées par R-2690 ; les occurrences « argon » sont
  des noms de fiches. Le validateur `controle_ia.prereg.problemes` rend `[]` sur le fichier (relancé par moi).

## 2. Nombres neufs recalculés par moi (fractions exactes, depuis la section du pilote recopiée dans ma consigne)

| nombre | recalcul | pièce |
|---|---|---|
| attendu par appel Pr-2 | 1,057336 / 4 = 0,264334 | idem |
| attendu par appel Pr-4 | 10,019552 / 4 = 2,504888 | idem |
| part sur crédits attendue | 60 × 2,504888 + 40 × 0,264334 = 160,866640 | 160,87 |
| sonde des gabarits attendue | 2 × 0,264334 + 2,504888 = 3,033556 | 3,03 |
| crédits avec sonde | 163,900196 (pire 267) | 163,90 ; 267 |
| bornes du plus petit et du plus grand appel de Pr-4 | (10,019552 − 5,585992) / 2 = 2,216780 ; 5,585992 / 2 = 2,792996 | idem |
| sortie maximale d'un appel de Pr-2 | 1,057336 / 0,00002 = 52 866,8 jetons, sous 71 200 | 52 867 |
| règle des 80 % pour Pr-4 | appel tronqué = raison d'arrêt « borne » (vérifié dans le texte du pilote : « tronque = raison d'arrêt = borne ») ; 64 000 > 51 200 | déclenchée |
| durée d'un monde | 68,38725 + 470,64975 = 539,037 s ; bas 425,232 ; haut 662,638 | 539 (425 à 663) |
| file de quatre mondes | 2 156,148 s = 35,9 min ; 28,3 à 44,2 | 36 (28 à 44) |
| somme des 16 durées ; écart au manifeste | 2 668,095 s ; 2 673 s (14:34 à 12:59:07 : 2 673) | idem |
| heures de machine du pilote | 0,082018 / 0,052222 × 3 600 = 5 654,03 s ; moins 2 673 = 2 981,03 s | 2 981 |
| machine attendue | (2 156,148 + 2 981,03) s = 1,42699 h × 0,052222 = 0,074520 | 0,0745 |
| total attendu | 160,866640 + 0,074520 = 160,941160 ; avec sonde 163,973716 | 160,94 ; 163,97 |
| taux de réussite | 4/4 et 2/4 : 6/8 = 0,75 | idem |
| probabilité du minimum, taux commun | monde complet 0,75⁵ = 0,2373 ; P(Bin(20 ; 0,2373) ≥ 16) = 1,786 × 10⁻⁷ | 1,8 × 10⁻⁷ |
| probabilité du minimum, par relais | 1,00² × 0,50³ = 0,125 ; 1,044 × 10⁻¹¹ | 1,0 × 10⁻¹¹ |
| réserve de l'étage 2 | P(≥ 3 sur 20 | 0,5) = 0,999799 | 0,9998 |
| arrêt du minimum | mondes commencés ≈ 9,71 ; 9,71 × 8,043332 = 78,14 USD | ≈ 10 ; ≈ 78 |
| III-7, dénominateur ; bornes de c₁ | 2,504888 ; 0,05 × 2,504888 = 0,1252 et 0,25 × 2,504888 = 0,6262 ; 1,1055 si c₁ = 0,264334 | idem |
| écart de rapprochement | 15,378197 − 15,302276 = 0,075921 | idem |
| cumul des cinq | 123 + 483 + 243 + 204,67 + 270 = 1 323,67 ; sans sondes 1 308,60 ; reste 1 275 − 270 = 1 005 | idem |

Tous concordent. Le programme de devis applique bien les règles écrites de la table de mise à jour (moyenne arithmétique par relais,
pire cas inchangé aux plafonds, bornes et garde inchangées puisque 553,242 s ≤ 1 500 s, garde 4 × 7 200 s + 2 h = 10 h).

## 3. Enveloppe et échéance de GO-2026-11-15-06

- Ligne l. 339 de `registres/go.md` : 1 275 USD au pire, 247,20 attendus, échéance 2026-11-30. Les trois lignes proposées (κiii1,
  κiii2, κiii0) portent la même échéance 2026-11-30 et les plafonds 260, 3 et 7 inchangés.
- Aucune ligne « calcul » de `go.md` ni aucune ligne de `depenses.md` ne cite GO-2026-11-15-06 (relu par `grep`) : rien d'engagé.
  Ce crible, sonde comprise, 270 USD au pire, y tient ; le cumul des cinq aux textes actuels dépasse 1 275 : nœud de Lazar au
  dernier crible inscrit, dit dans la pièce (R-2992, point 3).
- La pièce n'autorise rien : « n'autorise encore aucun appel » est écrit au statut et à la section des lignes de GO.

## 4. Parts séparées

Part sur crédits de Claude (Pr-2, Pr-4) et part hors crédits (machine) sont séparées partout : attendu 160,87 et 0,07 ; pire 260 et
3 ; avec la sonde 267 et 3. La somme et les plafonds de relais (180 et 80 sur crédits, 3 pour la machine) sont cohérents.

## 5. Corrections exigées

Aucune.

## 6. Remarques facultatives (aucune n'empêche le scellement comme pièce)

- **F-1** (rédaction, section 0, point 9). Le mot « impossible » suit maintenant « ≈ 3 h attendues », ce qui peut se lire comme
  « 3 h est impossible ». Il vise le pire cas (60 h). Couple facultatif :
  « 60 h au pire (3 h par monde, [PROC-14]) : **impossible** sous la » →
  « 60 h au pire (3 h par monde, [PROC-14]) : **impossible au pire cas** sous la »
  (l'ancien figure une fois dans la pièce, l. 183).
- **F-2** (étiquette). « 2 981 s hors appels » est le temps de machine hors de l'intervalle `debut_utc` à `fin_utc` du manifeste
  (5 654,03 − 2 673) ; hors des seules durées d'appels, c'est 2 985,9 s. Écart de 4,9 s, sans effet (0,07 USD) ; à dire si la
  version 2 reprend la phrase.
- **F-3** (risque, pas un défaut). La durée attendue d'un monde (539 s) est la somme des moyennes passe 1 + D ; l'espérance du
  maximum avec S et H en même temps est un peu plus haute (une borne basse, donc). Sans effet sur une borne ou une garde.
- **F-4** (risque, à savoir). Les deux appels tronqués de Pr-4 coûtent en moyenne 2,793 USD, pour un plafond de session de 3,00 : marge de
  7 %. Si le texte servi du crible (G2) est plus long que celui du pilote, un appel tronqué peut passer le plafond et déclencher la ligne
  d'arrêt « coût d'un appel au-dessus du pire cas » (code 3). La sonde obligatoire le mesurera ; la pièce dit déjà que les jetons
  ne sont pas relus.
- **F-5** (cohérence). Les « Raisons » de III-2 et de III-7 (l. 250) disent encore « 1,32 à 1,64 pour un appel d'écriture de Pr-4 »,
  alors que le pilote lit 2,50. C'est voulu (gel R-2993 : « Raisons » comprises) et c'est dit à la l. 546. Un renvoi à cette ligne
  depuis le tableau serait un confort, non une exigence ; ne rien changer aux « Raisons ».
- **F-6** (en-tête). La puce « Auteur » (l. 3 à 6) désigne l'auteur du brouillon 1 ; la version qui fera foi a son propre
  rédacteur, dit à la puce de la l. 57 et suivantes. Cohérent, mais un lecteur pressé lit « auteur de cette pièce » à la
  l. 3. Facultatif.

## 7. Points pour la mère

1. **Lancer avant le 21 novembre** : rien dans la pièce ne l'interdit (échéance de GO au 30 novembre ; crible ≈ 3 h de machine ;
   part sur crédits dans l'enveloppe). Mais au taux de tronquage de Pr-4 lu au pilote (2 sur 4), la ligne d'arrêt du minimum se
   déclenche presque sûrement (probabilité du minimum 1,8 × 10⁻⁷ au taux commun, 1,0 × 10⁻¹¹ par relais ; ≈ 10 mondes commencés, ≈ 78 USD).
   Les prédictions et le gabarit G0 du bras S étant gelés, accepter ce risque ou demander à Lazar un changement de forme (nœud :
   modification de revendication) est à trancher **avant** toute ligne « calcul ». C'est la décision utile pour sa question.
2. **Sonde des gabarits obligatoire** (7 USD au pire) : à inscrire sur sa ligne propre et à jouer d'abord ; ses règles d'avance
   arrêtent le crible si un appel sous G2 est tronqué (0,5 par appel de Pr-4 au taux du pilote). Si elle précède la recopie,
   version 2 pour III-7 et un tour différentiel de plus.
3. **Restes avant `prereg/`** (déclarés par la pièce, vérifiés présents et non faits) : la sonde ; les trois valeurs processeur ; le
   versement de l'annexe A et de ses programmes ; ce tour (fait) ; la pièce n'est scellable que comme pièce de travail, non comme
   préenregistrement en vigueur.
4. **Fourchette par appel** (règle écrite) non calculable : les dollars par appel ne sont pas dans la section lisible ; la pièce
   le dit et donne des bornes. Si la mère veut la vraie fourchette, lui recopier les coûts par appel sans ouvrir l'issue.
5. **Enveloppe** : rien engagé ; le dernier crible inscrit dépassera 1 275 (nœud de Lazar, R-2992, point 3).
6. Limite non mesurée : latence et limite de débit à 20 sessions simultanées chez un seul fournisseur (le pilote a joué en série).
