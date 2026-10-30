# Contre-lecture (R2) de la table de dépendance « critères de G0 → travaux », v7 (dernière version avant soumission à Lazar)

**Déclaration.** Je n'ai écrit ni la v7 ni son script, ni aucune version ou contre-lecture de cette lignée. Modèle : **Sonnet 5.5** (sous-agent neuf), même famille que le
contre-lecteur de la v6, différent de l'auteur de la v7 (Opus 5.5) ; des erreurs corrélées avec la lignée restent possibles. `date -u` : début 2026-10-30 00:00:04 UTC ;
fin de rédaction 00:06 UTC. Interdits tenus : rien lu sous `donnees/`, ni `prereg/P3-consignes-v1.md`, ni `diag/*/traces` ; aucune commande git ; aucune dépense ; aucun
fichier existant modifié ; rien scellé (ce rapport n'a pas de compagnon `.sha256`) ; les dossiers `cl-table-v*` précédents n'ont pas été ouverts. Travail dans
`/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/cl-table-v7/` (pièces : `ctest7.py`, `alt7.py`, `essais.out`) ; `python3 -I`, sans `__pycache__` dans le dépôt.
**Empreintes** (recalculées ; compagnon = recalcul) : table v7 `2e17b8a538bfdb6ee71106a0b9ce5b2ca86a1f1500b10ee9cf0123d96fdc965b` OK ; script v7
`b9bf8fc4e016c6881ca063c665e8a0e66926d44655486ae791eac1b153155a29` OK ; contre-lecture, table et script de la v6 OK ; cinq copies de `main` OK ; `registres/decisions.md` est
maintenant `903101e7…` (739 lignes ; la table avait lu `e8c92742…`, 737 lignes : source « vivante », sans effet). Rejeu : `scellement verifier` table et script OK ;
`sources` toutes OK ; `verifier … SY` : OK 71 lignes dérivées, 51 lignes de travaux, 20 produits, clause identique à SY § 5 ; `feuille` : refus « décisions en attente » ;
`essais` avec dépôt et SY : **161 gardes, 0 manquante** (code 0). Les 51 lignes de travaux et de produits n'ont pas changé depuis la v6 (diff v6/v7 : aucune ligne W ni P).

## (a) Le résumé d'une page : exact, suffisant, sans mot plus fort que la table ?
Exact sur l'essentiel, et bien meilleur que la v6 : recommandations, confiances et sens égaux au registre (garde du script), 51 travaux, R-765, R-518, silence, plafond, choix
n° 4 et n° 6, G1-2, sessions supposées non facturées ; l'affirmation « W13, W18, W40 restent ouvertes sans plafond » est vérifiée (`simuler`). Défauts :
**CT7-01 — D:1 (a) : « une cause technique reste réparable » est trop fort. Gravité : à corriger.** La liste d'arrêt de la grille compte quatre causes ; deux d'entre elles
(`verifier-arbre` ou empreintes en échec **au commit `C_lecture`** ; preuve exigeant un fichier interdit) sont des propriétés de `C_lecture`, que (a) fige (« même commit, aucune
preuve nouvelle »). Le § 9 écrit pourtant « quand la cause est levée à un commit nouveau de `main` (… `verifier-arbre` sans échec …), un second lecteur … sur le même `C_lecture` » :
une panne de `C_lecture` ne se répare pas sur un commit nouveau si la lecture reste sur l'ancien. L'avantage que le résumé donne à (a) sur (b) ne vaut que pour les causes de
remise (mauvais fichier de grille, lecteur non neuf). À dire en une phrase, dans le résumé ou le message d'envoi.
**CT7-02 — D:1 (a) : le résumé ne dit pas que (a) repose sur une lecture de la synthèse. Gravité : à corriger.** SY § 2 pt 5 écrit « aucun état suspendu » (3 sur 3) ; seul SY l. 72
précise « sans échéance ». Le § 9 lit : fenêtre d'attente bornée, que SY « n'écarte pas » ; c'est une interprétation de la table, plus affirmée que SY (le point 5 est général).
Le résumé range seul (c) comme « contraire à la synthèse » et omet l'attente d'au plus sept jours après un arrêt, ainsi que le nœud que la grille ouvre à ce moment pour toi. Lazar peut
croire (a) conforme sans réserve. De plus, le **sens** « ferme (moins que (b)) » ignore que (a) retire sept jours de preuves à **toute** lecture (le « C_lecture au plus tard le 24 »
vaut aussi sans arrêt), alors que (b) garde « le report entier » : (a) est mixte face à (b), non seulement « moins fermé ».
**CT7-03 — CT6-02 traité à moitié. Gravité : à corriger.** Le § 1 dit que la lettre (a) du mémo (suspension, retirée) « est rappelée » : elle l'est au § 9, **pas dans le résumé**.
Or Lazar a lu le mémo, où « (a) » est la suspension jusqu'à son mot, et le résumé lui fait écrire « D:1 : a » pour autre chose. Ajouter : « ce (a) n'est pas le (a) du mémo ».
**CT7-04 — D:0b : « clôture quasi certaine dès le 30 novembre » plus fort que la table. Gravité : à signaler.** Sous « négatif », R-765 gèle le critère et « ne ferme pas la porte en
cours de report » ; § 6.7 (ix)/(iii) dit « la porte ne peut plus être franchie », non une clôture au 30 novembre (le report court jusqu'au 31 janvier). La phrase vient du mémo
(écrit avant R-765). Dire : « report sans issue possible pour ce critère, clôture « non franchie » au second verdict ».
**CT7-05 — D:4 : résumé et § 9 se contredisent. Gravité : à signaler.** Résumé (a) : verdict « pour les critères 1, 2, 3 et 5 » ; § 9 : « critères empiriques (1 à 5) … valeur copiée et
classe » ; L14 : classe lue pour 1, 2, 3, 5, aucune pour 4 (verdict de 4 requis, sans classe). Enjeu « elle retombe sur la présence des fichiers » alors que (b) rend la table
inapplicable (L14, `feuille` refuse). **CT7-06 — D:2 / silence.** « À la date de D:2 » : D:2 est elle-même une des huit décisions ; sans réponse sur D:2, la date est indéfinie (la
dernière borne est V1). La recommandation (b) est attribuée au mémo, qui la conditionnait à « aucun résultat des critères 2 à 4 lu avant » (condition remplacée par une réserve
consignée). **CT7-07 — « une page »** : le résumé fait ≈ 1 670 mots (trois pages) et emploie W13, W18, W19, W21, W33, T0.6, P4, ρ, R13 sans les développer (CLAUDE.md : quasi aucun
acronyme). Rien de faux ; à signaler. Aucune expression plus forte relevée ailleurs : « ne lit aucun résultat de G1 ni du papier C » et « ce qui exige une dépense » sont justes.

## (b) Constats de la v6 traités comme déclaré ?
CT6-01 **oui** (paragraphe « Si tu ne réponds pas », R-452 cité avec « à confirmer », clause N-027 bis inexistante ; réserve CT7-06). CT6-02 **en partie** (CT7-03 ; « reprise »
→ « second lecteur » fait). CT6-03 **oui** (enjeu, options avec avantage et inconvénient, renvoi au § 9, W19 et W33 nommés). CT6-04 **oui** (i à iv ; « nécessaire, non suffisant »).
CT6-05 **oui**. CT6-06 **oui**. CT6-07 **oui, avec les limites de (c)**. CT6-08 **oui** (§ 6.7 (ii), (xi), (xii), (xiii) présents et justes ; garde `controle_67` à 13 cas). CT6-10 **oui**.
**CT6-09 : non, il se reproduit.** Le titre, la déclaration et l'annexe (« `scellement verifier` : ARRÊT … compagnon absent, code 1 ; `feuille` : refus table non scellée ») sont faux
à la remise : les compagnons de la v7 et de son script existent (posés à 23:58:53 UTC, 78 s après le texte) et le refus réel de `feuille` est « décisions en attente ». **CT7-08 —
Gravité : à signaler** ; toute retouche étant une version nouvelle (R12), dire à Lazar dans le message d'envoi que ces trois énoncés sont périmés. À noter aussi :
`PROVENANCE.md` écrit « GO-08 à 19 » alors que `go-29-octobre.md` en contient dix (08 à 17), comme la table ; la table est exacte, la provenance non.

## (c) Le contrôle du mot de Lazar (essais `ctest7.py`, copies temporaires, registre réel copié, table décidée et scellée en jouet)
R-521 réelle citée pour les huit : **refusée** (« n'est pas un mot direct de Lazar »). R-525 réelle : refusée. R-513 et R-514 réelles (mots directs, sans identifiant) : refusées
(« ne contient pas l'identifiant »). Une ligne `Lazar (10:00 heure de Paris, mot direct) : « D:0b : absent ; … ; D:7 : garder — go »` ajoutée à la **copie** du registre : **acceptée**,
R-nnn et empreinte imprimés. Option différente de la cellule : refusée. « recommandation » ou « Version soumise » hors guillemets : refusés. Phrase sans « : » (« D:0b absent, D:1
option a ») : refusée (légitime, mais le résumé ne dit pas que Lazar doit écrire « identifiant : option »). **Ligne de relevé qui imite le format : acceptée, franchement** : (3a) un
relevé « Point de session : Lazar (10:00 heure de Paris, mot direct) aurait écrit « … » » passe ; (3b) « Session : les mots directs de Lazar sont attendus ; hypothèse de travail : D:0b :
absent ; … » passe sans même le motif complet (la seconde alternative « mots directs de Lazar » est satisfaite par toute mention) ; (3d) « proposition de la session, à confirmer par
Lazar » passe (marques de relevé = trois expressions seulement). **CT7-09 — Gravité : à signaler.** Le contrôle est de forme, comme la table le dit (§ 8 (19), résumé) ; la phrase du
résumé « une ligne de relevé … est refusée » n'est vraie que pour les trois marques. Durcissement possible : exiger le motif au début de la cellule de texte, ou une colonne de
source propre aux décisions de Lazar ; le lecteur R13 doit surtout relire les R-nnn imprimés.

## (d) D:1 (a) et la coupure du 24 janvier : conforme à la synthèse ?
Dans la lettre, oui : aucun troisième verdict (un arrêt n'est pas une lecture, G l. 424 ; le second lecteur rend le second verdict, une seule fois ; s'il s'arrête, l'heure butoir
tranche), échéance fixe (31 janvier 23:59), aucune suspension sans borne (SY l. 72), « absence de verdict scellé vaut non franchie » (SY § 2 pt 2, appuis exacts dits : une cellule, non
3 sur 3), second lecteur et coupure déclarés « proposition de la table », sans cellule dans SY. Réserves : CT7-02 (interprétation du point 5 ; attente bornée) ; CT7-01 (réparabilité) ;
la coupure du 24 janvier n'est ni dans la grille (G l. 95-97 : « avant l'ouverture de la lecture ») ni dans la clause, et raccourcit de sept jours la borne que tu as fixée (R-452 : « un
mois peut être court ») : l'inconvénient est écrit, mais (c) seule est dite « au-delà de ta borne ». Sous (a), l'ordre « 24 janvier » s'applique même sans arrêt : à écrire tel quel.

## (e) Cinq altérations nouvelles (dont deux dans le résumé), `alt7.py`
Z1 résumé « la table n'est pas scellée » → « scellée d'office, les tâches continuent » ; Z2 résumé D:3 (1) « inatteignable sans plafond suffisant » → « atteignable avec un plafond » ;
Z3 § 9 D:1 (a) « une seule fois » → « autant de fois que nécessaire » ; Z4 annexe « 161 gardes » → « 181 » ; Z5 § 6.7 (viii) « 7 février » → « 14 février ». **5 détectées sur 5** avec le
filet des sections ; **sans le filet, 3 sur 5 passent** (Z1, Z2, Z4 : le paragraphe « Si tu ne réponds pas » et les options du résumé ne sont liés à aucune garde propre, seulement à
l'empreinte de section ; Z3 par l'empreinte du § 9, Z5 par les dates). Acceptable puisque tout est gelé par empreinte ; une dérive faite en v8 avec constantes recalculées ne serait vue
que par la contre-lecture.

## Conclusion
**Prête après corrections mineures, soumettable** : logique, script (161 gardes, rejeu complet) et résumé sains ; à dire à Lazar dans le message d'envoi (ou en v8 de texte) : CT7-01 à 03
(D:1 (a) ni toujours réparable, ni sans réserve sur le point 5, ni le (a) du mémo), CT7-04, CT7-05, et que titre, déclaration et annexe sont périmés (CT7-08).
