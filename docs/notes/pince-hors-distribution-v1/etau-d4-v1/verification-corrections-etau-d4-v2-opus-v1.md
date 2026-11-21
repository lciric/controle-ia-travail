# Vérification des corrections de la note sur la taxe de l'obscurcissement (D-4 reprise, v2) — Opus 5.5 (v1)

- **Date** : samedi 21 novembre 2026, 16:21 UTC (`date -u`). Dépôt à `eaab25904`.
- **Auteur** : Claude Opus 5.5, contre-lecteur de la v1 (`contre-lecture-reponse-fable-etau-d4-v1-opus-v1.md`, `f0922c88…`). Je vérifie ici les corrections, en tant que même contre-lecteur (R-3735, classe C). Lecture seule hors de ce fichier ; ni commit, ni poussée, ni appel payant, ni recherche en ligne. Aucun chemin interdit ouvert ; aucun refus d'outil.
- **Pièces vérifiées** : `sha256sum -c` sur tous les compagnons du dossier donne « OK » partout.
  - `reponse-fable-etau-d4-v2.md` (`838f2b8e13a9…`) : lue en entier.
  - `calculs-etau-d4-v2.py` (`cae4ddea8406…`) et `.txt` (`dc5e9a6529e0…`) : le programme, rejoué une fois (`python3 -I`) dans un dossier temporaire à moi, sort une copie **identique à l'octet** du `.txt`.
  - `faits-etau-taxe-bras-declare-v2.md` (`3fb079936094…`), `question-etau-taxe-bras-declare-v2.md` (`c248589d3446…`), `invite-neon-etau-taxe-v2.md` (`600bc2d6d9b5…`) : chacune comparée ligne à ligne à sa v1.
  - Pages relues sur PDF pour cette vérification : Gupta et Jenner, p. 4, 15 et 18 ; Bailey et al., tableau 2 de la p. 49.

## Verdict

**Conforme.** Les dix-sept constats sont tous portés, et justement. Deux réserves mineures, neuves (R1 et R2 ci-dessous), se règlent par un erratum, sans nouvelle version.

Les trois points demandés par la mère tiennent :

1. **Plus d'exception à l'invariant.** Le mot « exception » a disparu des quatre pièces neuves, hors les rappels de ce que disait la v1. À sa place, la v2 parle d'une déclaration de bras. Les neuf conditions sont confrontées une à une au montage de la décision N-056 (point 6), dans une table qui dit ce que le montage porte déjà et ce que chaque condition ajoute. Le bras de la taxe y devient un troisième bras, présenté comme un nœud (nœud 1).
2. **L'échelon 1 sort de la lignée du saboteur.** La v2 le place hors de cette lignée, sous marque et sous le clapet, et dit pourquoi le chantier « saboteur et sondes » ne peut pas l'accueillir. Le choix de son logement, et la règle « Qui conçoit » (R-3735), sont posés en nœud (nœud 2), avec trois options.
3. **Les pièces servies à Neon sont corrigées et neutres.** Faits, question et invite donnent la lettre exacte de l'invariant et décrivent le montage existant. Ils ajoutent la phrase de la p. 7 de McGuinness et al. et rendent la citation de Taufeeque et al. dans son sens. La sous-question (c) ne souffle plus la réponse. Aucun nom de personne, aucun nom du programme, aucun chemin interne, aucun identifiant de décision ou de GO ; la chaîne de marquage de Taufeeque et al. n'est pas recopiée.

## Les dix-sept constats

| N° | Statut | Où, et ce que j'ai vérifié |
|---|---|---|
| 1 | porté juste | Verdict 3 ; § 5, réécrit, avec la table de confrontation ; § 6, nœud 1 ; faits, question et invite v2. « Un seul bras » est retiré. La v2 ajoute avec raison que le montage n'exécute rien : le bras de la taxe en déborde. |
| 2 | porté juste | § 4, ligne de l'échelon 1, et l'alinéa « Pourquoi l'échelon 1 ne peut pas loger dans le chantier des sondes » ; condition 4 (marque « née d'une intervention ») ; nœud 2. |
| 3 | porté juste | § 5, « Qui conçoit, qui exécute, qui lit » : un cadre sans sortie, une instance cloisonnée, une mère qui verse sans lire. L'écart à l'usage de R-3735 est remis à Lazar (nœud 2). |
| 4 | porté juste | § 3, 3e alinéa (« au moins ») ; bloc F6, réserve en tête et libellés « s* >= » ; trouvaille de côté (3). |
| 5 | porté juste | § 2, ligne Gupta et Jenner et premier point ; § 6, « En attendant » ; faits et invite. Les citations des p. 10, 18 et 19 sont exactes. La probabilité « taxe haute sous renforcement » descend à 0,3. |
| 6 | porté juste | § 2, ligne McGuinness et al. et premier point ; la citation de la p. 7 est exacte ; elle figure aussi dans l'invite. |
| 7 | porté juste | Premier point du § 2. Le tableau 2 (p. 49) donne bien trois sondes sur quatre sans lien significatif entre couches visées et rappel ; ma v1 en nommait deux, la v2 a raison. La taxe d'environ 7 % à trois couches est juste sur la droite lue à l'œil : 1 − 32,5/34,8 ≈ 0,067. |
| 8 | porté juste | Bloc F5 : « POSÉE », espérance de 0,6375 trois fois, coût de l'attente d < h (1 − q). J'ai vérifié l'algèbre : v (1 − d) > v (1 − h + hq) revient bien à d < h (1 − q). § 6 : confiance de 0,7, dite jugement ; l'écart de 0,04 à 0,13 est juste. |
| 9 | porté juste | Verdict 5 ; § 2, « dans les pièces lues » ; « Ce que je n'ai pas fait ». |
| 10 | porté juste | Bloc F1 : six couples à moyenne ou à médiane, de 0,25 à 0,66, et neuf à maximum ou à attention, de 0,945 à 0,990 ; je les ai recomptés et je les retrouve. |
| 11 | porté juste | Verdict 4 ; § 2 : 2 à 3 % sous déclencheur, 5 à 6 % contre le modèle d'origine. |
| 12 | porté juste | La ligne qui rapportait 35 à 95 % sort des plafonds, étiquetée « durcissement du défenseur » ; les faits disent que ces deux taux viennent de deux modèles différents. |
| 13 | porté juste | § 1, point 4 (le témoin garde la récompense du comportement) ; § 2 ; faits et invite. |
| 14 | porté juste | § 4, ligne 1 et alinéa suivant ; relevé de méthode, pas 5. |
| 15 | porté juste | Verdict 3 ; § 4, règle de passage ; relevé, pas 4 ; nœud 1 : dire si le modèle de l'expérience du papier C est « l'agent » au sens de N-053 est laissé à Lazar. |
| 16 | porté juste | Question v2, sous-question (c). |
| 17 | porté juste, dans la limite de la note | Le constat est remis à la mère ; le travail de la v2 se fait dans un seul sous-dossier propre. L'inventaire des dossiers communs reste à faire par la mère. |

## Réserves neuves (mineures, par erratum)

- **R1. Le rappel de départ des sondes du modèle de 14 milliards.**
  - *Lieu* : bloc F1, trois lignes « 14 milliards (ajout v2) » ; « Ce que je n'ai pas fait », point « La convention d'échelle ».
  - *Constat* : la note suppose ce rappel à 0,98, « le tableau ne le donne pas ». Or le tableau 3a de la p. 15 de Gupta et Jenner le publie : 0,994 (linéaire à moyenne), 0,994 (linéaire à maximum), 0,996 (attention). La supposition rend une ligne incohérente : pour la sonde à attention, le rappel sous attaque (0,982) dépasse le rappel de départ supposé (0,980). Les fourchettes du § 2 ne bougent pas.
  - *Correction* : « r0 [publié, tableau 3a, p. 15] : 0,994 ; 0,994 ; 0,996 ».
- **R2. L'adaptateur attribué à Gupta et Jenner.**
  - *Lieu* : § 5, sort des poids (« Gupta et Jenner entraînent un adaptateur, p. 18 ») ; nœud 3, option (ii).
  - *Constat* : la mention d'un adaptateur, p. 18 (et p. 4), porte sur le réglage initial qui retire les refus du modèle (« The initial supervised fine-tuning step to remove guardrails … using LORA »). Elle ne dit pas que l'apprentissage par renforcement d'obscurcissement en emploie un. L'appui de l'option « méthodes à adaptateur seules au cran 2 » n'est donc pas établi.
  - *Correction* : « (l'adaptateur de la p. 18 sert au réglage qui retire les refus ; le mode d'apprentissage de l'obscurcissement lui-même n'est pas relevé) ». La recommandation (ii) tient sans cet appui.
