# LISEZMOI de la sortie — registre v3, protocole v2, briefs v2, spécification du relevé (B) — v3

Dossier de sortie ouvert le 2026-10-26 à 04:36:11 UTC (heure lue sur `date -u` dans la commande qui a listé `sortie/`,
vide, après la lecture complète des pièces fournies et avant l'écriture de tout fichier). Écriture de ce fichier
achevée le 2026-10-26 à 04:51:22 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).

Auteur : un sous-agent neuf de la lignée conv-audit, sur le brief v3 (`LISEZMOI-brief-v3.md`,
`82b9028dc4ef0a2054da6b2f7ecb1d795ed8a8dbe519c329ac0b9f8569b5803d`, vérifiée avant lecture : égale). Je n'ai écrit ni
la v2, ni sa contre-lecture, ni aucune pièce fournie. Je n'ai lu aucun score. Rien de ce dossier n'est servi à un
organisme. Aucun `git`, aucun sous-agent, aucun réseau, aucune clé ; aucune recherche hors de `fournis/` ; écrit seulement
dans `sortie/`.

## 1. Ce que j'ai fait

- **Vérifié** l'empreinte du brief, puis les seize fichiers de `fournis/` contre `../EMPREINTES-fournis-v1.txt`
  (`sha256sum -c`) : seize sur seize égaux.
- **Lu en entier, dans cet ordre** : le brief ; la contre-lecture (`2eb11e6a…`) ; la v2 (registre v2, protocole v1,
  briefs v1, LISEZMOI v2) et le brief v2 qui l'a produite ; le texte v4 du pilote (`782b858c…`) : § Statut, § Ce qui a
  été lu, § Décisions, table de correspondance, § Objet, § Plan (points 1, 2, 3, 4 bis, 4 et 5), liste d'arrêt, § Essais,
  § Pièces, § Contre-lecture ; la décision de 05:13 Paris (`4b23e00f…`) ; le brouillon du texte v5 (`31791501…`) ; le
  LISEZMOI du script de lecture (`53597f9c…`) et le brief du script (`c86be1a1…`) ; la fiche de lecture des papiers
  (`2aea3057…`) ; les synthèses « agents sur le noyau » (`f23ee714…`) et « littérature des boucles » (`58010971…`) ; les
  hypothèses de (b) (`903c6b51…`) ; la contre-lecture 7 (`68daac56…`).
- **Exécuté** : `sha256sum`, `sha256sum -c`, `ls`, `date -u`, `python3 -I -c "print('python ok')"` (vérification de
  l'interpréteur, aucun calcul, aucun fichier écrit). Aucun nombre nouveau n'a été calculé : les nombres sans score du
  registre v2 (z, bornes, tailles minimales, valeurs p illustratives) sont repris tels quels, refaits par la contre-lecture.
- **Écrit**, dans `sortie/` seulement : `registre-hypotheses-conception-pilote4-v3.md`,
  `protocole-boucle-exterieure-pilote4-v2.md`, `brief-agents-fin-de-course-v2.md`,
  `specification-releve-mecanique-B-v1.md`, ce LISEZMOI, et le compagnon `.sha256` de chacun.
- **Fiches** : changées HC-P4-01, 03, 04, 05, 06, 07, 08, 10, 11, 12 ; inchangées en substance HC-P4-02, 09. Déclarées
  « indécidable par ce pilote » : HC-P4-02 (inchangé), HC-P4-04 (nouveau : différence calculée hors de la levée),
  HC-P4-10 (inchangé ; la v5.3 ne court pas). Réécrite en fiche mécanique : HC-P4-05. Toutes les fiches portent sur les
  deux courses M et S du même objet ; aucune fiche ne nomme la v5.3 hors HC-P4-10. Le détail est dans la table
  « v2 → v3 » du registre (§ 4) ; les omissions de la table « v1 → v2 » sont complétées (§ 5).

## 2. Table « constat → traitement » (CLB-01 à CLB-19)

| constat | traitement | où |
|---|---|---|
| CLB-01 nom de course ≠ nom de dossier | **traité**. `<course>` (nom du texte) et `<dossier>` (nom exact du dossier poussé) distingués ; tous les fichiers de lecture nommés par `<dossier>`, jamais renommés (compagnons au nom nu) ; dossier choisi par l'identité du § 9, jamais par le nom ; un dossier de tentative refusée n'est jamais lu ; tableau d'identité avec les deux noms (M : `pilote4-gemini-v6-2-v1-tentative2`) | protocole § 0, § 3, § 9 ; briefs, mode d'emploi |
| CLB-02 le relevé (B) n'existe pas | **traité**. Spécification écrite (champs, grammaire fermée des valeurs, sources, ce qu'il ne porte jamais, essais R5 sur la série v13 et dix artefacts, exécution) ; pièce à produire par conv-audit ; condition de démarrage de la boucle ; garde G11 ; le choix 1 de la v2 (faits mécaniques lisibles par un relevé dérivé) est tranché par le brief v3 : oui ; relevé produit et poussé sans affichage sous la retenue | `specification-releve-mecanique-B-v1.md` ; protocole § 1.2, § 11 ; registre § 0.1 |
| CLB-03 opération (2), HC-P4-04, HC-P4-05 | **traité**. Opération (2) « non permise » ; une permission demanderait un texte nouveau ou un mot de Lazar. HC-P4-04 déclarée « indécidable par ce pilote », le nombre d'appels de mutation rapporté sans verdict. HC-P4-05 réécrite en fiche mécanique (événement de restauration), la condition sur les scores jamais calculée. Les conséquences « tenue → correction » retirées ; les seuils 0,01 et 0,03 sous le poids d'une tâche soumis comme point de conception a priori, hors de la boucle | registre § 0.2, § 0.5, HC-P4-04, HC-P4-05 ; protocole § 6, § 16 |
| CLB-04 valeurs de `test_final` recopiées | **traité**. Aucun nombre de `test_final` (b, c, nombre sans réponse, valeur p) ; le sens d'un rejet et « aucune tâche sans réponse » deviennent des libellés à demander au script ; sans eux, « non observable ». La comparaison d'une valeur p à 0,05 par l'analyste disparaît avec le calendrier provisoire (N-050) | registre § 0.1, § 0.2, HC-P4-08, HC-P4-11 ; briefs section 4 ; protocole § 16 |
| CLB-05 les deux courses se rencontrent | **traité**. Journal retiré du dossier de lecture (pièce de conv-audit, jamais donnée aux agents) ; un dossier de lecture par course ; la lecture finale par course, par des agents distincts, sur un fichier `test_final` par course sans valeur de l'autre (version nouvelle du script, condition du § 13 ; avec le script actuel, pas de lecture finale) ; G6 bornée et appliquée à ce qui est servi | protocole § 2, § 3, § 5, § 11 (G6, G8 bis), § 13 |
| CLB-06 un facteur à la fois | **traité**. `diff -ruN` ; pièce de périmètre rendue et empreintée avant le diff ; carte des facteurs (facteur → fichiers, fonctions, lignes) écrite d'avance par conv-audit, lue par G5 ; artefacts de G5 ajoutés (périmètre couvrant deux facteurs ; fichier nouveau hors liste) ; (c) les deux seuils du critère de fin proposés comme un seul facteur avec la raison, la carte confirme ou sépare | protocole § 6, § 11 (G5) ; briefs section 2 ; registre HC-P4-01 |
| CLB-07 contenu interdit du correcteur | **traité**. Liste close des zones interdites (`zones-interdites-v<n>.md`) écrite par conv-audit depuis le code, lue par G5 ; « défaut du chemin des réponses » déclaré et revu à part ; essai R5 : diff synthétique à contenu interdit refusé par G5 et par le contre-lecteur, via un dossier d'audit qui porte cette correction | protocole § 11 (G5 e), § 12.1, § 14 ; briefs section 3B |
| CLB-08 audit pas aveugle | **traité**. Construction écrite au § 12.1 : (A) forgée depuis la sortie synthétique du script (mention d'essai et empreintes synthétiques retirées, compagnons refaits, script de forge empreinté et listé) ; relevé forgé avec l'identité réelle et des coûts plausibles ; ouverture de même forme ; manifeste refait ; aucun journal dans le dossier ; G2 exige une référence vérifiable, contrôlée par conv-audit ; la mesure éprouve aussi la lecture du registre par conv-audit ; dossier d'audit du contre-lecteur avec correction interdite | protocole § 1.3, § 3, § 11 (G2), § 12.1 |
| CLB-09 ronde d'isolement | **traité**. Retirée ; l'attribution d'un rejet à un mécanisme est « indécidable par ce pilote », avec ce qu'il faudrait (plusieurs graines avec et sans le mécanisme, texte nouveau). Sous N-050, la lecture de `test_final` ne motive de toute façon aucune ronde | registre HC-P4-11 ; protocole § 13 |
| CLB-10 symétrie d'effort avant (b) | **traité comme point pour Lazar**, écrit au § 8 et au § 16, plus net depuis que la v5.3 ne court pas : options (a) objets tels que livrés, (b) v6.2.1 corrigée contre v5.3 livrée avec l'inégalité déclarée au texte de (b), (c) rondes pour la v5.3 (dépense) ; recommandation (a), confiance moyenne, aucun défaut | protocole § 8, § 16 ; registre HC-P4-10, § 3 |
| CLB-11 document de correction dans l'arbre | **traité**. `CORRECTIONS-v<N>.md` ne décrit que le changement de code (quoi, où) ; aucun fait de course, aucune fiche, aucun verdict, aucun score ; G4 le vérifie (artefact ajouté) ; les motifs restent dans les pièces de la boucle | protocole § 6, § 8, § 11 (G4), § 14 ; briefs section 2 |
| CLB-12 le correcteur lit toute la sortie | **traité**. `lecture/` retiré de ce que lisent le correcteur et la partie B ; aucune correction n'est motivée par un score | protocole § 2 ; briefs sections 2 et 3B |
| CLB-13 aveugle de la partie A | **traité**. Sections 3A et 3B données en deux temps ; les chemins des pièces de l'analyste et du correcteur ne sont donnés qu'après réception de la partie A et consignation de son empreinte | protocole § 2, § 4 ; briefs, mode d'emploi, sections 3A et 3B |
| CLB-14 « rejet trop propre » | **traité**. Retiré ; tout verdict (iii), rejet ou non, reçoit le même audit (contre-lecture à l'aveugle de la lecture finale) ; les adjectifs « trop propre », « trop beau » ajoutés aux interdits des briefs | registre HC-P4-11 ; protocole § 13 ; briefs partie commune |
| CLB-15 code de l'objet, entrée non ouverte | **traité** (option 2) : le code retiré des entrées de l'analyste ; les fiches citent les lignes ; (C) lu par le correcteur et la partie B seulement | registre § 0.1, HC-P4-04, 05, 06 ; briefs section 1 |
| CLB-16 petites inexactitudes | **traité** : (a) « hors (A) et (B) » ; (b) `objet/` = copie d'`organisme/`, `objet-EMPREINTE-ARBRE.txt` à côté, un seul chemin dans les briefs ; (c) « jamais dans les fichiers de l'organisme ; dans la pièce de correction, la cellule et son libellé seulement » ; (d) « trop larges pour rien séparer (illustratif) » ; (e) G6 bornée aux pièces de verdicts, parties A et pièces de correction ; (f) `<empreinte-manifeste>` ajouté aux briefs | protocole § 2, § 3, § 11, § 14 ; registre § 0.5 ; briefs partie commune |
| CLB-17 omissions des tables | **traité**. § 5 du registre v3 complète la table « v1 → v2 » (seuils comptés ensemble ; ordre en trois groupes ; chemins relatifs au dossier de lecture ; journal unique) ; la table « v2 → v3 » déclare chaque changement | registre § 4, § 5 |
| CLB-18 phrase sur le canal des paires | **traité**. Retirée de HC-P4-12 ; la phrase du § Périmètre reformulée (le registre est écrit pour ne rien contenir qui serve à classer ; le correcteur n'en recopie rien) | registre § Périmètre, HC-P4-12 |
| CLB-19 multiplicité d'une ronde à l'autre | **traité**. Dit au § 7 et au § 10 : jusqu'à huit tests (iii) sur trois rondes, sans contrôle d'ensemble ; écrit dans chaque texte de relance, chaque transmission à Lazar et l'entrée finale du journal ; nombre accumulé dans chaque entrée | protocole § 5, § 7, § 10, § 13 |

Aucun constat refusé.

## 3. Faits nouveaux, appliqués

1. **La v5.3 ne court pas ; seconde course : la v6.2.1 sur la question S.** Un seul objet, deux courses (M, S) ; ronde 1
   de la boucle = les deux courses ; toutes les fiches portent sur les deux courses, séparément ; HC-P4-10 indécidable,
   renvoyée à (b) ; § 0.9 du registre dit ce que la question S change (appels, coût et durée de g001 ; rien d'autre
   d'attendu ; rien n'est supposé de la réponse, jamais lue) ; identité de la course S à remplir depuis le texte v5 à ses
   graines.
2. **`test_final` lu une fois, à la fin du compteur.** (A) séparée en (A-test) et (A-final) ; calendrier provisoire de
   (iii) retiré ; pendant la boucle, seuls les faits mécaniques motivent une correction ; § 13 du protocole dit ce qui se
   décide à chaque course et ce qui se décide à la fin ; section 4 des briefs pour la lecture finale ; après la lecture
   finale, aucune relance sous ce protocole.
3. **Relevé (B)** : spécification écrite ; condition de démarrage.
4. **Gardes des lectures** : journal des lancements et des lectures avec attente chiffrée (G9) ; compteur de trois rondes
   et plafond de Lazar, avec l'issue « plateau » écrite d'avance ; étalonnage à blanc des agents (dossier nul, paire « A
   contre A » synthétique) avant tout droit d'éliminer (G10, § 12.5) ; `test_final` lu une fois ; plafond laissé à Lazar.

## 4. Choix faits seul (une ligne chacun)

1. Ronde 1 de la boucle = les deux courses du pilote 4 ; une seule correction par ronde, proposée après la lecture de la dernière course de la ronde (sans mot de Lazar pour faire autrement).
2. Chaque course est lue à sa fin par son propre analyste et sa propre partie A ; le correcteur et la partie B travaillent par ronde.
3. Une fiche aux verdicts différents selon la course ne motive rien et n'est attribuée à rien (question, graine ou bruit : non séparables).
4. La pièce de correction a une section par course ; aucune ligne ne porte les deux noms de course (contrôle de motifs de G6 sur cette pièce).
5. Journal des essais retiré du dossier de lecture ; les agents n'en ont pas besoin.
6. Le correcteur et la partie B ne lisent pas `lecture/`.
7. Le code de l'objet retiré des entrées de l'analyste (CLB-15, option 2), plutôt que donné à l'analyste.
8. HC-P4-05 réécrite en fiche mécanique (restauration) plutôt que déclarée indécidable en bloc.
9. HC-P4-04 déclarée indécidable par ce pilote ; son fait (appels de mutation à g2 et g3) rapporté sans verdict.
10. HC-P4-01 lue par `conception.rondes_tournees` quand le champ de déclaration manque ; le cas « 6 » non observable.
11. Les seuils 0,01 et 0,03 déclarés points de conception a priori, soumis par conv-audit hors de la boucle, comptant pour une ronde s'ils sont changés.
12. Écart `test` − `test_final` : non calculé dans ce pilote (différence hors de la levée), malgré la recommandation de la fiche de lecture ; renvoyé à un texte nouveau.
13. Libellés demandés au script : sens du rejet (sous réserve que conv-audit juge que le point 4 bis le couvre), « aucune tâche sans réponse » par cellule de `test_final`, un fichier par part et par course, un fichier `test_final` par course à la lecture finale.
14. Avec le script actuel (une sortie pour deux dossiers), la lecture finale ne se fait pas ; avec le fichier actuel qui porte les deux parts, aucun dossier de lecture n'est assemblé : l'outil de partage est une condition.
15. Grammaire fermée des valeurs du relevé (B) : tout décimal porte une unité ; tout texte libre fait refuser l'écriture ; « absent » sans estimation.
16. Exécution du relevé sur une course réelle : session-depot recommandé, conv-audit possible ; point pour conv-audit.
17. Dossiers d'audit forgés par un script empreinté qui retire la mention d'essai du script de lecture et refait les compagnons.
18. Étalonnage à blanc : dossier nul + paire « A contre A » synthétique ; refait à chaque version nouvelle du brief ou du registre.
19. Issue « plateau » = arrêt sans fiche qui motive, écrit comme une réponse de la boucle.
20. Compteur gardé à trois rondes ; plafond demandé à Lazar avec le premier devis ; sans plafond, chaque relance reste sur son mot.
21. La question servie par une relance est fixée par le texte de la relance, sans défaut (M ou S).
22. Verdict « sans objet pour cette course » gardé pour une relance qui retirerait un mécanisme.
23. Les deux seuils du critère de fin proposés comme un seul facteur, la carte des facteurs tranche.
24. Partie A et partie B du contre-lecteur en deux briefs, deux sessions.
25. Sections 3A/3B et 4 ajoutées aux briefs ; `<opération-2>` retiré ; `<empreinte-manifeste>`, `<pièces-verdicts>`, `<pièces-partie-A>`, `<pièce-périmètre>` ajoutés.
26. Aucun nombre recalculé ; les nombres sans score de la v2 repris tels quels.

## 5. Points à trancher par conv-audit (une ligne chacun)

1. Pousser ces cinq fichiers et leurs compagnons avant l'ouverture de la lecture ; dire au journal si la v2 a été poussée avant la fin de la course M.
2. Faire contre-lire cette v3 par un agent neuf avant le premier usage (relecture gardée) ; lui donner la contre-lecture de la v2 et cette table.
3. Écrire le script du relevé (B), sa table de correspondance et ses essais, après lecture de la structure des pièces de la série v13 ; décider qui l'exécute sur une course réelle (recommandé : session-depot).
4. Demander la version nouvelle du script de lecture ou l'outil de partage (deux fichiers par course ; un fichier `test_final` par course à la lecture finale, sans valeur de l'autre course ; libellés du sens et de « aucune tâche sans réponse ») ; essayer G8 bis.
5. Dire si le libellé « sens du rejet » est couvert par le point 4 bis ; sinon, ne pas le demander.
6. Écrire la carte des facteurs et la liste des zones interdites depuis le code, avant la première correction ; confirmer ou séparer « les deux seuils du critère de fin ».
7. Désigner les auteurs des gardes G1 à G11, des dossiers d'audit, du script de forge et de l'étalonnage à blanc ; les essayer avant la première lecture.
8. Remplir l'identité de la course S (graine, lanceur v11, empreinte du texte v5, dossier) depuis le texte v5 à ses graines, dans une pièce empreintée ou une v3 du protocole.
9. Confirmer les choix 1 à 4 (ronde 1 = M puis S ; correction par ronde ; verdicts différents selon la course ; section par course).
10. Fixer la forme du texte d'une relance et des noms ; y écrire la question servie, l'attente chiffrée et le nombre de tests (iii) accumulés.
11. Soumettre à Lazar, hors de la boucle, les points de conception a priori (seuils 0,01 et 0,03 sous le poids d'une tâche).
12. À l'ouverture : si un texte nouveau (graines) change la règle de lecture, faire un registre v4 avant la première lecture.

## 6. Points à soumettre à Lazar (une ligne chacun)

1. La famille de modèle du contre-lecteur (même famille ou famille différente) ; aucune valeur par défaut.
2. La question des graines de plus (02:05 ; tour R-491), qui tient la retenue : la boucle ne démarre qu'à sa décision ou sur un « lis ».
3. Le plafond de dépense des relances de la boucle (§ 7) ; aucun n'est fixé ; demandé avec le premier devis.
4. La symétrie d'effort avant (b) (§ 8) : (a) objets tels que livrés, (b) v6.2.1 corrigée contre v5.3 livrée avec l'inégalité déclarée, (c) rondes pour la v5.3 ; recommandation (a), confiance moyenne ; aucun défaut.
5. Si une correction doit être proposée après la course M sans attendre la course S (son mot ; sans lui, le correcteur attend).
6. La question servie par une relance (M ou S), au GO de la relance.
7. Les seuils 0,01 et 0,03, point de conception a priori, hors de la boucle.

## 7. Écarts à ce brief, déclarés

1. **Faits mécaniques de la course M lus** dans le brouillon du texte v5 fourni (§ Ce qui a été lu : conception close
   après une ronde, génération 0 faite, nombre d'appels et statuts, coût ; aucun score). Le brief demandait de lire ce
   brouillon ; ces faits touchent HC-P4-01, 07 et 08. Aucune fiche n'a été changée pour eux (énoncés, seuils et branches
   de la v2 gardés) ; déclaré au registre (§ Écrit avant tout score). La contre-lecture de la v3 devrait vérifier que les
   changements de ces trois fiches ne tiennent qu'à la contre-lecture et aux faits nouveaux.
2. Lu un fichier hors de `fournis/` en plus du brief : `../EMPREINTES-fournis-v1.txt`, que le brief désigne. Listé `sortie/`,
   vide, avant d'écrire. Rien d'autre hors de `fournis/`.
3. Aucune poussée sur le canal : sans `git`, elle revient à conv-audit.
4. L'heure du début de ma lecture n'est pas consignée ; la seule heure de début écrite est celle de l'ouverture de
   `sortie/` (04:36:11 UTC), après la lecture.
5. Python lancé deux fois, en mode isolé : une fois pour vérifier l'interpréteur (`print`), une fois pour recopier
   les quatre empreintes et l'heure de fin dans ce LISEZMOI (seul fichier écrit, dans `sortie/`) ; aucun calcul.
6. Les heures de fin des fichiers sont écrites par substitution d'un marqueur dans la commande même qui lit `date -u`,
   après l'écriture du texte ; les compagnons `.sha256` sont calculés après cette substitution.

## 8. Empreintes (format « empreinte, deux espaces, nom nu »)

Les empreintes des quatre pièces sont dans leurs compagnons `.sha256` et sont recopiées ci-dessous par la commande qui
les calcule :

```
a5abc176503d5cafd3b0096614740247dbd0d4a26608cfde679667b2c68cbc52  registre-hypotheses-conception-pilote4-v3.md
0c71a74b791251e030d1642abd0cdd267f650d69af8b5823d6066a92d2fbf7ed  protocole-boucle-exterieure-pilote4-v2.md
60553a1b28a041d96c072cbe3e04d62cc3b342e9e9e991086e24b2f2a990cd10  brief-agents-fin-de-course-v2.md
3ed32fe8ec0884ef1983c59afd514654a1924e8d7a67c5a06aaa783243c0c091  specification-releve-mecanique-B-v1.md
```

L'empreinte de ce fichier est dans son compagnon, `LISEZMOI-sortie-v3.md.sha256`.
