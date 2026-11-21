# Vérification des corrections : note sur le mécanisme adjudant, v2 (Opus 5.5, v1)

- **Date** : 21 novembre 2026, 16:30 UTC (`date -u`). **Auteur** : Claude Opus 5.5, auteur de la contre-lecture (`contre-lecture-reponse-fable-mecanisme-adjudant-v1-opus-v1.md`, `b7a20aa0…5374`), même contre-lecteur (R-3735), sur mandat de la mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`). Pièce de classe C. Ni commit, ni poussée, ni appel payant.
- **Pièces vérifiées contre leurs compagnons `.sha256`, toutes conformes** : `reponse-fable-mecanisme-adjudant-v2.md` (`4f8fbeaf…`), lue en entier (en-tête, table des constats, verdict, sections 3.3 à 3.5, 6, 7 et 8, annexe) ; `calculs-mecanisme-adjudant-v2.py` et `.txt` ; `collisionneur-v2/question-mecanisme-adjudant-v2.md` et `faits-mecanisme-adjudant-v2.md`, comparés ligne à ligne à la v1.
- **Rejeu** : `calculs-mecanisme-adjudant-v2.py`, une fois, avec `python -I`, dans un dossier temporaire à moi : sortie **identique à l'octet** au `.txt` versé.

## Verdict

**À corriger, sur un point.** Les seize constats sont portés, et justement. Les blocs N à P sont exacts. Le constat 1, porté plus loin, tient. Le constat 2, porté plus loin, n'est tenu que pour la moitié de ce qu'il vise : le calcul O, et la limite de 3/m, valent aussi pour le dommage que l'honnête commet vraiment. Or l'exemple « par construction » de la v2 (« un contrôle exécutable qu'un honnête ne viole jamais ») est une supposition sur l'honnête, pas une construction (réserve 1). Deux réserves mineures en plus. Le couple v2 du collisionneur est neutre.

## Les seize constats

| N° | État | Où, et ce que j'ai vérifié |
|---|---|---|
| 1 | porté juste, porté plus loin | Verdict, point 3 ; § 3.3 ; § 6, rang 1 ; § 7.3 (S12, `garantie_dite`) ; § 7.4 ; D-5. Les chiffres cités sont ceux de la sortie : fausse alarme de 0,23 à 0,42 avant 40 000 audits pour m = 1 000 (N3) ; 0,47 et 0,999 pour une référence trop basse d'un point (N2) ; planchers de 3,8, 2,0 et 1,2 points (N4) ; 1 016 contre 654 et 3 601 contre 2 191 verdicts (N5, K), soit un facteur de 1,55 à 1,64. Les réserves sur l'amortissement de la référence et sur le jumeau, au banc seulement, sont dites. Voir la réserve 3 |
| 2 | porté juste pour l'oracle ; **incomplet** | S11, S17, § 7.4 et § 6 portent la fausse reconnaissance, et O1 à O4 sont exacts. Mais voir la réserve 1 (l'honnête qui endommage vraiment) et la réserve 2 (niveau global de la règle de compte) |
| 3 | porté juste | § 3.3, § 6 (rangs 1, 2, 9, trois propriétés), S18, famille « audit orienté », témoins ; P1 et P2 exacts (rappel apparent 0,71, annonce de 0,90 à 0,06 ; fausse alarme du pari, médiane de 52 audits pour g = 0,3). La limite déclarée (règle pondérée non calculée) est honnête |
| 4 | porté juste | § 7.1 et § 7.2 : les bases sont servies comme bases à battre, sans leurs tables ; seuls les blocs A, E, F et M sont joints ; une re-proposition est comptée « base » |
| 5 | porté juste | D-4 (a) restreinte à la part laissée par le verdict 5, après contre-lecture de la lecture des voisins ; rangs 2, 3, 5 et 8 portent « partiellement occupé ; question, non revendication » ; § 3.5 |
| 6 | porté juste | § 7.5, étage 4 : trois bases, estimations pondérées ; § 7.8, geste 5 |
| 7 | porté juste | Vue 3a et 3b ; le témoin « doit tenir » est relu |
| 8 | porté juste | Verdict, point 1 ; § 3.3 (« sous certains scénarios ») |
| 9 | porté juste | Verdict, point 4 |
| 10 | porté juste | 2609.36490v1 à chaque citation ; annexe distingue les deux articles |
| 11 | porté juste | « au moins de l'ordre de 156 … de 490 », test à horizon fixe dit |
| 12 | porté juste | Chemins, lignes, empreintes ; 19,06 = 30 × 0,14 + 14,86 et 237,48 = 30 × 4,10 + 114,48, refaits ; « par jugement » |
| 13 | porté juste | Colonne « Viole » pour les trois familles ; rang 4, « S8 violée » |
| 14 | porté juste | § 7.9 : le mandat est en classe A |
| 15 | porté juste | « ses auteurs » ; (B) reformulée sans « non corrélée ». Le reste du couple est inchangé (diff vérifié) : ni nom, ni personne, ni chemin, ni numéro de décision, ni réponse glissée. **Couple v2 neutre** |
| 16 | porté juste | « État » en regard de D-1, D-5, D-7 ; N-075 renvoyée à la mère, et c'est dit |

## Les blocs N à P

- **N3** : l'encadrement par monotonie est juste. Chaque composante du mélange gagne 1 + c(1/nul − 1) sur un dommage et perd 1 − c sans dommage : la perte ne dépend pas du nul, le gain décroît quand le nul monte. Un nul plus haut ne sonne donc jamais plus tôt, sur toute trajectoire.
- **N5** : la validité tient. La borne haute exacte est fausse avec un risque d'au plus 0,005. Quand elle tient, un nul placé au-dessus du vrai taux reste une surmartingale, de niveau 0,005. Le total fait au plus 0,01.
- **O2 et O3** : 1 − 0,05^(1/m) ≈ 3/m ; ln 0,05 / ln 0,99 ≈ 298. Exact.
- **O4** : c = 9 pour tout m, car n = m et f · n ≈ 3 (loi de Poisson de moyenne 3, P(≥ 9) ≈ 0,004). Exact.
- **P1 et P2** : les formules sont justes. La « pondération par l'inverse » est un rapport d'espérances, ce qui suffit à la démonstration.

## Réserves

| N° | Gravité | Lieu | Constat | Correction proposée |
|---|---|---|---|---|
| 1 | important | § 6, « Les chiffres du rang 1 », deuxième puce ; verdict, point 3 ; S11 ; témoin « doit tenir » du régime de signature | La règle « un seul épisode reconnu suffit » sonne aussi quand l'honnête commet vraiment le dommage, à un taux h, et pas seulement quand l'oracle le voit à tort, à un taux f. Le calcul O vaut pour f + h. « Par construction » ne règle que f. L'exemple « un contrôle exécutable qu'un honnête ne viole jamais » porte sur h : c'est une supposition, que m témoins ne bornent qu'à environ 3/m, comme f. Seule la « vérité plantée dont la présence est le dommage » peut, selon sa définition, régler h aussi | Lire, dans la deuxième puce : « Le calcul O vaut pour toute reconnaissance chez l'honnête, fausse (f) ou vraie (h) : la règle sonne à tort au taux f + h. Le régime de signature ne vaut par construction que si aucun produit honnête ne peut porter ce dommage tel que l'oracle le définit (exemple : une vérité plantée qu'aucune conduite honnête ne produit). Un contrôle exécutable que l'honnête “ne viole jamais” est une supposition, bornée à environ 3/m sur m témoins : la règle devient un compte. » S11 se lit de même : « … par construction de la définition du dommage et de l'oracle » |
| 2 | mineur | Même puce (« il faut 9 épisodes reconnus ») ; O4 | Le compte c = 9 tient 1 % de fausse alarme **si** la fausse reconnaissance est sous sa borne, ce qui n'est sûr qu'à 0,95. Le niveau global est donc d'au plus 0,06. Et les rangs 69 et 1 441 ne valent que si ces épisodes endommagés tombent dans l'horizon de m audits (à 1 % d'audit et m = 300, cet horizon couvre 30 000 épisodes) | Ajouter : « niveau global d'au plus 0,06 (0,05 pour la borne, 0,01 pour le compte), ou 0,01 en prenant 0,005 et 0,005 ; rangs valables si le k-ième épisode endommagé tombe dans l'horizon de m audits » |
| 3 | mineur | § 6, « Deux procédures valides », (a) ; § 7.3, `garantie_dite` (« n au plus égal à m sauf nul par acte ») | La procédure (a), avec son nul placé à la borne haute, est valide au-delà de m (N5) ; or la forme fixe exige n ≤ m hors nul par acte. Le chiffre de 1 016 verdicts emploie une médiane de 516 audits pour m = 500. Le coût de N5 est celui de l'issue typique (k = 0,1 m), ce que la note ne dit pas | Dire la lecture retenue : « avec un nul placé à la borne haute, la validité ne dépend pas de n ≤ m ; la limite de N-076 borne alors ce qu'on conclut de la puissance, non la fausse alarme ». Faire confirmer cette lecture de N-076 par la mère, sinon remplacer le repère par m = 1 000 (1 334 verdicts, médiane 334). Ajouter « issue typique, k = 0,1 m » |
