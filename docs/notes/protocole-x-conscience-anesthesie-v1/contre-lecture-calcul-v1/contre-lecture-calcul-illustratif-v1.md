# Contre-lecture du calcul illustratif v1 — complexité perturbationnelle transposée sur GPT-2 petit

Contre-lecteur : Opus 5.5, neuf, auteur d'aucune des pièces lues. Le 22 novembre 2026. Pièce de classe B (instrument) : le code, et la correspondance entre ses résultats et la note qui les cite.

Pièces lues, empreintes vérifiées par `sha256sum` avant lecture, toutes conformes :
- `travail/calcul/plan-calcul-illustratif-v1.md` (`a57706d0…5314`) ;
- `travail/scripts/calcul_illustratif_v1.py` (`b44605d4…f6bf`) ;
- `travail/calcul/resultats-calcul-illustratif-v1.json` (`ec797920…2691`) ;
- `travail/calcul/journal-calcul-illustratif-v1.txt` (`3aee0025…e20e`) ;
- `reponse-fable-conscience-anesthesie-v1.md` (`e6c778e3…af`) : verdict (l. 9), sous-section « Ce que donne déjà un calcul sur processeur » (l. 84-92), et les phrases qui citent ce calcul ou la source [SL] (l. 30, 42, 100, 101, 163) ; la plage affichée m'a montré aussi les l. 94 à 99 de la section B.1, qui décrivent le banc ;
- `sources/provenance-v1.md` (`78cc7716…21ef`), puis la source [SL] `sources/sleeping-llm-rapport-experience-04.pdf` (`78f534ad…d865`, conforme à son compagnon), pages 2 à 5, lues sur le texte extrait par `pdftotext` ;
- poids publics de GPT-2 petit dans `travail/donnees-gpt2/`, empreintes conformes à la table de provenance (l. 52) ; rien téléchargé.

Les chemins sans préfixe s'entendent sous `/tmp/claude-0/-home-user-controle-ia-travail/d69341ed-1da2-5804-bff1-02b01c73e5e7/scratchpad/protocole-x-conscience-anesthesie-v1/`.

## Verdict

**À corriger.** Le code fait ce que dit le plan, il est juste (Lempel-Ziv contrôlé, découpage en jetons contrôlé, calcul déterministe : la relance complète et un diagnostic à un seul fil de calcul reproduisent les résultats au bit près), et chaque nombre de la sous-section correspond au fichier de résultats. Mais l'indice y travaille dans un régime dégénéré : les matrices binaires sont presque vides, la normalisation sort de son domaine (une matrice à un seul « un » vaut 3,59), et la ligne de la position perturbée, où la perturbation passe telle quelle par la connexion résiduelle, fait à elle seule toute la valeur des réseaux sans fonction. Les lectures de la note (réseaux sans fonction au-dessus de 0,31, inversion au seuil doublé, effet du texte d'entrée, lésion contre bruit, réponses « plus amplifiées ») décrivent le nombre de cases au-dessus du seuil, non une propriété d'une mesure de complexité transposée. La conclusion négative tient pour cette transposition-là, plus fortement que la note ne le dit (presque rien de la propagation n'est mesuré) ; elle ne dit rien d'une transposition soignée.

Constats : 2 bloquants, 4 importants, 6 mineurs.

Réserve de symétrie (R4) : le résultat de la note est d'une netteté suspecte dans le sens négatif (tous les contrôles échouent). L'audit montre que ces échecs viennent de la construction. Une de mes propres présomptions, sur l'amplitude du bruit, a été éprouvée et infirmée (constat 4) ; mes indices de diagnostic (sans la ligne perturbée, rapporté à des matrices mélangées) restent eux-mêmes dans le régime clairsemé : ils ne servent qu'à montrer que le sens des écarts dépend de choix arbitraires, non à proposer un meilleur indice.

## Ce que j'ai fait

- Chronologie par les heures de naissance et de modification des fichiers (constat 10).
- Relance complète du script original, sans modification, sorties dans mon dossier (`relance/`), sans fixer le nombre de fils de calcul : résultats identiques au bit près à l'original sur les 31 conditions, journal identique, durée exceptée (850,5 s contre 795,9 s, machine chargée par mon diagnostic).
- Diagnostic réponse par réponse : le script original est importé sans modification et `mesurer` est repris à l'identique (mêmes graines, même ordre des tirages), en consignant pour chaque réponse le nombre de « uns » de la matrice de 48 positions × 128 dimensions, leur place, l'indice sans la ligne perturbée, l'indice rapporté à des matrices mélangées de même nombre de « uns », le gain rapporté à la norme naturelle et le rapport de participation en coordonnées réduites ; plus une variante du bruit à amplitude figée. Quinze conditions ; pour les treize qui existent dans l'original, moyennes et écarts-types aux trois seuils, rapport de participation et gain sont identiques au bit près à ceux du fichier de résultats.
- Contrôle de la fonction de Lempel-Ziv contre l'algorithme de Kaspar et Schuster (1987), écrit indépendamment : exemple classique 0001101001000101 → 6 composantes ; 400 suites au hasard, aucun écart.
- Comportement de la normalisation sur des matrices binaires au hasard de même taille (6 144 cases).
- Lecture des pages 2 à 5 de [SL].

Scripts et sorties : voir la dernière section.

## Constats

### 1. Bloquant — L'indice travaille dans un régime dégénéré : il compte les « uns », il ne mesure pas une complexité

- **Lieu.** Script l. 204-213 (`indice_lz`) et l. 236-238 (binarisation) ; plan l. 20-21 ; note l. 86-90 (toutes les puces), l. 9.
- **Ce qui ne va pas.** Au seuil principal (θ = 1), la matrice de 6 144 cases du réseau entraîné porte en médiane 12,5 « uns » (de 0 à 152) ; 26 réponses sur 64 en ont moins de 10, 3 n'en ont aucun (indice mis à 0) ; au seuil doublé, 43 sur 64 sont vides et le maximum est de 8 « uns ». Sous bruit, la médiane tombe à 9,5 (η = 0,05, graine 1), 6 (η = 0,1, graine 1), 2 ou 3 (η = 0,2 selon la graine, de 11 à 19 matrices vides), 0 (η = 0,8, graine 1, 62 matrices vides sur 64). Or la normalisation par L·H(p)/log₂(L) surcompense quand les « uns » sont rares. Sur des matrices au hasard de même taille : un seul « un » donne 3,59 (au milieu), deux 2,08, trois 1,69, cinq 1,47, dix 1,17, vingt 0,99 ; de 40 à 3 072 « uns » placés au hasard, de 0,94 à 1,04. Au-dessus d'environ 1,05, l'indice n'est donc atteint qu'avec peu de « uns » : dans mes données, aucune matrice de plus de 100 « uns » ne dépasse 0,99, et toutes celles qui en ont de 1 à 5 dépassent 1,29. Dépassent 1,05 : 37 réponses sur 64 du réseau entraîné, de 42 à 52 sur 64 sous bruit faible ou moyen. Réponse par réponse, sur les 2 222 matrices non vides de mes quinze conditions et des trois seuils, l'indice décroît avec le nombre de « uns » (corrélation de rang de Spearman −0,90) : 3,59 pour 1 « un » (148 réponses, sans exception), 2,39 pour 2, 1,86 de 3 à 5, 1,40 de 6 à 10, 1,07 de 11 à 20, 0,85 de 21 à 50, 0,57 de 51 à 100. Rapporté à des matrices mélangées de même nombre de « uns », l'indice du réseau entraîné vaut 1,07 ± 0,20 (61 réponses non vides), celui du bruit η = 0,2 de 1,12 à 1,17 selon la graine : rien dans l'arrangement au-delà du compte.
- **Pourquoi.** La formule est bien celle de la clinique, mais elle ne borne l'indice près de 1 que pour des matrices assez denses. Ici, « 1,28 ± 0,70 » mélange des zéros (matrices vides), des « uns » isolés (3,59) et des matrices plus denses (0,6 à 0,9) : la moyenne n'est pas une mesure, et l'écart-type de 0,70 traduit ce mélange. Les conditions comparées diffèrent fortement par leur nombre médian de « uns », de 2 à 74 (bruit η = 0,2 : 2 ou 3 ; réseau entraîné 12,5 ; réinitialisé 41 ; poids mélangés 61,5 ; mises à jour coupées 74) : comparer leurs moyennes revient à comparer ces nombres. Réponse au point 2 du mandat : la normalisation n'est pas saine dans ce régime, les valeurs ne sont pas comparables d'une condition à l'autre, et l'écart-type de 0,70 ne permet aucune des comparaisons faites.
- **Correction proposée.** (i) Rapporter, par condition, le nombre de « uns » (médiane, part de matrices vides, part sous 20). (ii) Ne pas faire la moyenne de zéros et de « uns » isolés : fixer un nombre minimal (par exemple 50 « uns ») sous lequel la réponse est « sans objet », comptée comme telle. (iii) Comparer à densité égale : seuil choisi par condition pour atteindre une même part de « uns », ou compte de Lempel-Ziv rapporté à celui de matrices mélangées de même densité. (iv) Réécrire les puces de la note : le calcul montre que cette transposition est dégénérée sur GPT-2 petit, non que l'indice manque de spécificité.

### 2. Bloquant — La ligne de la position perturbée fait toute la valeur des réseaux sans fonction

- **Lieu.** Script l. 235 (`d = (x1 - x0)[T0:]` : la position 16 entre dans `z`, puis dans la matrice l. 238) ; plan l. 19 (« positions 16 à 63 ») ; note l. 86 (« réponse lue en sortie du dernier bloc sur les positions suivantes ») et l. 87.
- **Ce qui ne va pas.** En sortie, la position perturbée porte la perturbation elle-même, transmise par la connexion résiduelle (norme de la réponse à cette position rapportée à celle de la perturbation : 1,00 quand les mises à jour sont coupées, 1,47 pour le réseau réinitialisé, 1,93 pour le réseau entraîné). Pour le réseau réinitialisé (graine 1) et pour le réseau aux mises à jour coupées, 100 % des « uns » sont sur cette ligne et aucune des 64 réponses n'en a un seul ailleurs ; pour le réseau aux poids mélangés (graine 1), 99,5 %. Leurs indices (réinitialisé 0,715 ; poids mélangés 0,567 ; mises à jour coupées 0,475) sont ceux du vecteur de perturbation, tiré au hasard puis seuillé : une matrice dont seule la première ligne porte des « uns » (32 % de ses 128 cases, au hasard) vaut 0,72 ± 0,06. Sans cette ligne, l'indice vaut 0,000 pour le réseau réinitialisé et pour les mises à jour coupées, 0,34 pour les poids mélangés (moyenne de zéros et de quelques « uns » isolés). Le réseau aux mises à jour coupées n'échange rien entre positions (gain 0, rapport de participation 0) : il « garde 0,48 » par cette seule ligne.
- **Pourquoi.** « Tous dépassent le seuil clinique de 0,31 » est garanti par la construction : toute direction de perturbation tirée au hasard donne une ligne au hasard, donc de l'ordre de 0,5 à 0,7. Ce n'est pas un faux positif d'une mesure de propagation. Et la description de la note (« sur les positions suivantes ») fait croire au lecteur l'inverse de ce qui est calculé.
- **Correction proposée.** Retirer la position perturbée de la matrice (positions 17 à 63), ou la rapporter à part comme l'équivalent d'un artefact de stimulation ; corriger la description l. 86 ; retirer ou réécrire la puce l. 87.

### 3. Important — La lecture (a) prévue ne s'observe pas au seuil principal ; la note lui substitue un critère non prévu

- **Lieu.** Plan l. 20 (θ = 1 principal, 0,5 et 2 en sensibilité), l. 31 (lecture a), l. 34 ; note l. 87-88 et l. 9.
- **Ce qui ne va pas.** Au seuil principal, l'ordre est : réseau entraîné 1,28, réinitialisés 0,71 à 0,76, poids mélangés 0,57 à 0,60, mises à jour coupées 0,48. Apparié par passage (les 64 directions sont communes à toutes les conditions), le réseau entraîné passe au-dessus du réinitialisé (graine 1) dans 8 passages sur 8 (+0,57, écart-type entre passages 0,26) et au-dessus des poids mélangés (graine 1) dans 8 sur 8 (+0,71 ± 0,25). La lecture (a) du plan, « si R ou M [réinitialisés ou poids mélangés] atteignent ou dépassent E [réseau entraîné] », ne s'observe donc pas au seuil principal. La note s'appuie sur deux autres choses : le seuil clinique de 0,31, absent du plan et sans portée pour cette normalisation (une matrice au hasard vaut environ 1, la ligne perturbée seule de 0,5 à 0,7) ; et le seuil doublé, réglage de sensibilité, où l'« inversion » vient de ce que les matrices du réseau entraîné se vident (43 sur 64, 8 « uns » au plus), tandis que le réseau réinitialisé en garde 6 en médiane.
- **Pourquoi.** Le plan prévoit d'écrire tel quel ce qui n'apparaît pas (l. 34). L'ordre au seuil principal n'est pas non plus un succès de l'indice : il suit le nombre de « uns » (constat 1), et ce nombre dépend pour l'essentiel du rapport entre la perturbation, dont la norme est fixée à la couche 3, et la variabilité naturelle en sortie, que la croissance du flux résiduel du réseau entraîné (×6,9 de la couche 3 à la sortie, contre ×2,1 pour le réinitialisé) rend relativement plus grande.
- **Correction proposée.** Écrire que la lecture (a) ne s'observe pas au seuil principal selon le critère du plan ; présenter la comparaison à 0,31 comme faite après coup et sans valeur probante ; expliquer l'inversion au seuil doublé par le vidage des matrices.

### 4. Important — Lésion contre bruit : le sens de l'écart dépend du seuil et de la ligne perturbée, et la courbe du bruit est tronquée

- **Lieu.** Script l. 173-175 (bruit) et l. 223-225 (écart-type de référence calculé sur des passes propres bruitées) ; plan l. 27 et l. 33 ; note l. 90.
- **Ce qui ne va pas.** (i) Le bruit entre dans la variabilité de référence, ce qui relève le seuil : médiane des « uns » 9,5 (η = 0,05), 6 (0,1), 2 ou 3 selon la graine (0,2), 0 (0,8) — graine 1 sauf mention —, contre 22,5 (α = 0,55), 27 (0,4), 50 (0,2). L'indice « monte » sous bruit parce que les matrices se vident (constat 1). (ii) Le sens de l'écart s'inverse avec deux choix arbitraires. Au seuil doublé, le bruit η = 0,2 passe sous l'amortissement α = 0,2 dans 7 et 8 passages sur 8 selon la graine (écarts moyens −1,15 et −1,30) ; sans la ligne perturbée, dans 7 et 6 passages sur 8 (−0,51 et −0,29) ; de même pour les deux autres paires de perte voisine. (iii) La courbe du bruit n'est pas monotone et finit sous 0,31 : η = 0,4 donne 0,43 ou 0,91, η = 0,8 donne 0,11 ou 0,09 (pour la graine 1, la moyenne de deux « uns » isolés sur 64 réponses) ; la note ne cite que η = 0,2. (iv) « À perte voisine (4,9 et environ 5,8 nats) » : l'écart est de 0,9 nat, alors que des paires plus proches existent et vont dans le même sens au seuil principal (α = 0,55 à 3,49 nats contre η = 0,05 à 3,50 ou 3,51 : 1,14 contre 1,49 ou 1,30 ; α = 0,4 à 3,70 contre η = 0,1 à 3,97 ou 3,98 : 1,04 contre 1,75 ou 1,58).
- **Pourquoi.** La lecture (c) du plan est remplie : à perte comparable, les deux dégradations donnent des valeurs différentes, et la courbe du bruit n'est pas monotone ; « l'indice ne suit pas la perte de fonction » tient. Mais « l'indice suit la sorte de dégradation », et le sens donné (l'amortissement fait descendre, le bruit fait monter), viennent de la façon dont chaque dégradation déplace la variabilité de référence, et s'inversent au seuil doublé comme sans la position perturbée.
- **Présomption éprouvée et infirmée.** Le bruit est proportionnel à la norme quadratique moyenne de l'état courant (l. 174), si bien que « même tirage » ne donne pas exactement le même bruit dans la passe propre et la passe perturbée. Variante à amplitude figée sur la passe propre : 1,528 contre 1,547 (η = 0,2, graine 1), 1,464 contre 1,489 (η = 0,05) ; médianes des « uns » 2 contre 2, et 9 contre 9,5. L'effet est négligeable ; il suffit de le déclarer.
- **Correction proposée.** Garder « l'indice ne suit pas la perte de fonction » ; remplacer « suit la sorte de dégradation » par « dépend de la façon dont chaque dégradation déplace la variabilité de référence ; le sens de l'écart s'inverse au seuil doublé et sans la position perturbée » ; rapporter toute la courbe du bruit, η = 0,4 et 0,8 compris ; citer les paires les plus proches ; déclarer que le bruit entre dans la référence.

### 5. Important — « Plus amplifiées » ne tient pas quand le gain est rapporté à la croissance naturelle des activations ; le gain est hors du plan, l'étendue prévue n'est pas rapportée

- **Lieu.** Script l. 239-240 ; plan l. 22 ; note l. 91-92.
- **Ce qui ne va pas.** Le gain du script rapporte la norme de la réponse en sortie, sommée sur 47 positions, à la norme de la perturbation à la couche 3 : il contient la croissance naturelle du flux résiduel entre ces deux points, ×6,9 pour le réseau entraîné (de 64 à 445), ×2,1 pour le réinitialisé (de 4,0 à 8,4), ×1,8 pour les poids mélangés (de 396 à 725). Position par position, rapportée à la norme de l'activation propre, la réponse vaut 3,0 % pour le réseau entraîné, 1,9 % pour le réinitialisé (graine 1) et 4,8 % pour les poids mélangés (graine 1) : le réseau entraîné n'est pas plus amplifié que le réseau mélangé. Le gain n'est pas dans le plan (mesures secondaires prévues : étendue de la propagation et rapport de participation) ; ajout non déclaré, fait avant l'exécution. À l'inverse, l'étendue prévue n'est pas rapportée, alors qu'elle dit le plus directement que presque rien ne se propage au-dessus du seuil : 0,07 % des cases hors de la position perturbée pour le réseau entraîné, 0 pour les trois réinitialisés, de 0,001 à 0,006 % pour les poids mélangés. Le rapport de participation, lui, tient en coordonnées réduites (chaque dimension divisée par son écart-type naturel) : 4,5 pour le réseau entraîné, 6,6 pour le réinitialisé, 7,6 pour les poids mélangés.
- **Pourquoi.** Comparer des gains bruts entre réseaux dont l'échelle des activations croît différemment le long des couches mesure cette croissance, non une amplification de la perturbation.
- **Correction proposée.** Rapporter le gain rapporté à la norme naturelle et le déclarer hors du plan ; rapporter l'étendue ; garder « moins diverses » (rapport de participation), retirer « plus amplifiées ». L'hypothèse de la l. 92 (« canalise une perturbation vers peu de modes amplifiés ») perd l'appui de « amplifiés ».

### 6. Important — Le verdict et « Faite ci-dessus » disent plus que le calcul

- **Lieu.** Note l. 9 (« reçoit ici un début de réponse, par un calcul sur processeur : non, pas telles quelles »), l. 100 (« Première expérience. Faite ci-dessus. »), l. 163 (« un résultat court et citable »).
- **Ce qui ne va pas.** Le calcul éprouve une transposition naïve, dont l'échec découle de la construction (constats 1 et 2). Il répond « cette transposition est dégénérée sur GPT-2 petit », non « les mesures de niveau tirées du cerveau ne survivent pas au transfert ». La première expérience du banc de la section B.1 (aire sous la courbe entre lésion plantée et témoin de même perte, part des systèmes nuls classés au niveau du réseau intact, part de variance expliquée par la compressibilité du texte, stabilité du signe) n'est pas faite : ni lésion plantée, ni aire sous la courbe.
- **Pourquoi.** Le verdict est ce que le directeur lit d'abord ; « citable » ne vaut qu'après correction.
- **Correction proposée.** Par exemple, l. 9 : « un calcul sur processeur montre qu'une transposition naïve est dégénérée sur GPT-2 petit (matrices presque vides, indice porté par la position perturbée) ; il ne dit pas encore si une transposition soignée survit » ; l. 100 : « Esquissée ci-dessus ; non faite. »

### 7. Mineur — Texte d'entrée : la référence change avec les entrées, et le sens s'inverse au seuil doublé

- **Lieu.** Script l. 291-292 (l'écart-type de référence est recalculé sur les passes répétitives elles-mêmes) ; plan l. 20 et l. 32 ; note l. 89.
- **Ce qui ne va pas.** « Sans que le réseau change » est exact, mais la référence change : la variabilité naturelle est celle des entrées répétitives. L'écart est encore un effet de compte (médiane de 22 « uns » contre 12,5), et au seuil doublé le sens s'inverse : 0,83 pour le texte ordinaire, 1,70 pour l'entrée répétitive (le texte ordinaire au-dessus dans 3 passages sur 8 seulement).
- **Pourquoi.** La lecture (b) reste vraie par construction (l'indice dépend des entrées par sa référence), mais ce n'est pas une propriété d'un « état ».
- **Correction proposée.** Binariser les deux sortes d'entrées contre la même référence (le texte ordinaire), ou le dire ; rapporter l'inversion au seuil doublé.

### 8. Mineur — Nature du « ± » et comparaisons non appariées

- **Lieu.** Script l. 243 (`np.std`, écart-type de population sur les 64 réponses) ; note l. 87.
- **Ce qui ne va pas.** « 1,28 ± 0,70 » est l'écart-type entre 64 réponses non indépendantes (8 passages × 8 directions), non une incertitude sur la moyenne ; la note ne le dit pas. D'un passage à l'autre, la moyenne des 8 directions varie (écart-type 0,26 pour le réseau entraîné, 0,02 pour le réinitialisé). Les 64 directions étant communes à toutes les conditions, des comparaisons appariées par passage étaient possibles ; elles ne sont pas faites (je les donne aux constats 3, 4 et 7).
- **Correction proposée.** Écrire « écart-type entre les 64 réponses (8 passages × 8 directions) » ; donner les écarts appariés par passage (moyenne, écart-type sur 8 passages, nombre de passages dans le sens annoncé).

### 9. Mineur — Écarts au plan non déclarés

- **Lieu.** Plan l. 22, 23, 27 ; script l. 149, 240, 293, 299-306.
- **Ce qui ne va pas.** (i) Le gain (constat 5). (ii) Pour les entrées répétitives, la perte est calculée sur ces entrées, non « sur les 8 passages » (plan l. 23) ; la note n'en use pas. (iii) Le générateur du bruit est réensemencé à chaque passe : la même réalisation du bruit sert aux 8 passages, si bien que « deux graines » font deux réalisations en tout. (iv) Les 64 directions sont les mêmes dans toutes les conditions (bon choix, mais non écrit). La note dit « plan écrit et empreinté avant l'exécution » sans signaler ces écarts.
- **Correction proposée.** Les énumérer dans le fichier de résultats ou dans la note.

### 10. Mineur — Antériorité du plan attestée par les seules heures du système de fichiers ; pas d'empreinte compagnon

- **Lieu.** `travail/calcul/` ; note l. 86 (« plan écrit et empreinté avant l'exécution ») ; provenance l. 52.
- **Ce qui ne va pas.** La chronologie est saine : plan né et modifié pour la dernière fois à 10:51:43 ; poids téléchargés à 10:52:13 ; script né à 10:53:37, modifié pour la dernière fois à 10:55:07 ; journal né à 10:55:51 (lancement ; c'est la sortie du script, un seul passage visible) ; résultats à 11:09:07 ; note à partir de 11:13:56. Le plan précède donc le script et les résultats, et le script n'a pas été touché après le lancement. Mais le plan n'a pas de compagnon `.sha256` (R6), et son empreinte n'apparaît que dans trois fichiers nés après les résultats : la table de provenance (11:21) et deux brouillons (11:16 et 11:20 ; trouvés par une recherche du nom de fichier contenant l'empreinte, contenu non lu). « Empreinté avant l'exécution » n'est attesté par aucun fichier antérieur à l'exécution.
- **Correction proposée.** Ajouter `plan-calcul-illustratif-v1.md.sha256` et écrire « empreinte consignée après coup ; antériorité attestée par les heures du système de fichiers » ; à l'avenir, écrire l'empreinte du plan en tête du journal au lancement.

### 11. Mineur — Graines et manifeste

- **Lieu.** Script l. 266-268, 280, 310-311.
- **Ce qui ne va pas.** `SeedSequence(20261122).spawn(12)` donne un enfant par tâche (dimensions lues, directions, trois réinitialisations, trois mélanges, deux bruits) : conforme à R9 dans son principe. Chaque enfant est réduit à un entier de 32 bits (`generate_state(1)`) avant `default_rng` : cela marche, mais passer l'enfant lui-même est l'usage prévu. La sortie consigne les graines, les paramètres, les versions de Python et de numpy, la durée ; elle ne consigne pas l'empreinte des poids, du script ni du plan, ni la bibliothèque de calcul matriciel et le nombre de fils, ni l'heure de lancement (R9 : configuration et empreinte, versions, graines, commit).
- **Déterminisme et reproductibilité.** Conformes : la relance complète, sans fixer le nombre de fils de calcul, rend un fichier identique au bit près à l'original sur les 31 conditions (durée exceptée) ; le diagnostic, à un seul fil, retrouve au bit près les 13 conditions qu'il partage avec l'original (moyennes et écarts-types aux trois seuils, rapport de participation, gain). Le résultat ne dépend donc pas du nombre de fils sur cette machine (Python 3.13.18, numpy 2.5.3, mêmes versions que l'original).
- **Correction proposée.** Consigner les éléments manquants dans le fichier de résultats ; passer les enfants de la `SeedSequence` directement.

### 12. Mineur — Source [SL] : ce que la note lui fait dire est sur les pages citées, à trois précisions près

- **Lieu.** Note l. 30, 42, 86, 87, 101 ; [SL] p. 2 à 5.
- **Ce qui est sur la page.** P. 2 : « target Layer 3 » ; « au même site (couche 3) » est exact. P. 5 : « converging precisely at the empirical clinical boundary (PCI* ≈ 0.31) defined by Casali et al. (2013) » ; le seuil de 0,31 est bien importé tel quel. L. 42 : « monotonic drop » (p. 5) ; 0,683, 0,715, 0,608, 0,507, 0,613 sont les valeurs du tableau de la p. 4 (0,6830 ; 0,7154 ; 0,6075 ; 0,5065 ; 0,6125) ; sur GPT-2, 0,2908 ± 0,0613 de α = 0,70 (p. 2) à α = 0,00 (p. 3), huit doses de suite, pendant que la perplexité monte de 233,8 à près de 9 × 10⁷ (α = 0,10) et que la justesse du premier choix tombe de 0,227 à 0,000 ; « le modèle s'effondre » est exact. L. 30 : l'amortissement de α = 1 à 0 est aux p. 2-3, et la note de la p. 3 dit qu'à α = 0 « the residual stream is completely severed ».
- **Ce qui ne va pas.** (i) Les valeurs de la l. 42 sont celles de Pythia-160M (« Model B ») ; la note ne le nomme pas. (ii) À la l. 86, « au même site » est exact, mais l'amplitude de [SL] est de 2,5 fois la norme locale (ici 1 fois) et sa binarisation est un plancher de bruit tiré d'une agitation de 1 % de la norme des plongements d'entrée, au 99e centile, invite par invite (ici, la variabilité naturelle entre jetons) ; sa lésion, décrite p. 3 comme coupant le flux résiduel à α = 0, n'est pas celle d'ici (mises à jour des blocs). (iii) L. 101 : « [PH], [SL], [UH] transposent sans ces contrôles » (ceux de la l. 98) ne cite pas de page pour [SL] ; aux p. 2 à 5 ne figure aucun des contrôles énumérés, mais il y a un contrôle anatomique (amortissement des couches basses contre hautes, p. 5) qui n'en fait pas partie ; les p. 6 à 9 sont hors de mon mandat, non lues.
- **Correction proposée.** Nommer Pythia-160M à la l. 42 ; à la l. 86, ajouter « même site ; autre amplitude, autre binarisation, autre lésion » ; à la l. 101, citer les pages ou restreindre la phrase aux p. 2 à 5.

## Correspondance des nombres de la sous-section (point 5)

Tous conformes au fichier de résultats, aux arrondis près.

| Note (l. 86-91) | Clé du fichier de résultats | Valeur du fichier |
|---|---|---|
| treize minutes | `duree_s` | 795,9 s |
| couche 3, 64 mesures par condition | `parametres.L0`, `n` | 3 ; 64 |
| 0,57 à 0,76 (réinitialisés, poids mélangés) | `R1..R3`, `M1..M3` `naturel` `lz_theta1.0` | 0,715 ; 0,757 ; 0,729 ; 0,567 ; 0,569 ; 0,599 |
| perte de 11 à 37 nats | idem `perte_nats` | 11,06 ; 10,96 ; 11,04 ; 35,03 ; 33,37 ; 36,87 |
| 1,28 ± 0,70 ; perte 3,31 | `E_entraine|naturel` | 1,2802 ± 0,6960 ; 3,306 |
| mises à jour coupées : 0,48 | `amortissement|alpha=0.0` | 0,4753 |
| tous au-dessus de 0,31 | (systèmes de la puce) | minimum 0,4753 |
| seuil doublé : 0,83 ; 1,45 à 1,83 | `lz_theta2.0` | 0,8256 ; 1,4524, 1,8346, 1,5301 |
| entrée répétitive : 1,28 → 0,90 | `E_entraine|repetitif` | 0,8975 |
| 4,9 et environ 5,8 nats | `alpha=0.2`, `bruit|eta=0.2` | 4,932 ; 5,852 et 5,745 |
| 0,77 ; 1,55 ou 1,80 | idem `lz_theta1.0` | 0,7726 ; 1,5473 et 1,7958 |
| participation 3,9 ; 6,6 à 7,6 | `participation` | 3,909 ; de 6,592 à 7,643 |
| gain 1,7 ; 0,3 à 0,7 | `gain_norme_final` | 1,684 ; de 0,277 à 0,657 |

Absents de la note, présents dans le fichier : l'étendue de la propagation (constat 5), la courbe du bruit à η = 0,4 et 0,8 (constat 4), le seuil doublé pour l'entrée répétitive (constat 7).

## Ce qui est conforme (points 1, 3 et 4)

- **Passe avant.** Normalisations de couche, attention causale avec facteur 1/√64, approximation de la fonction d'activation par tangente hyperbolique (celle de GPT-2), matrices au format d'entrée × sortie, matrice de sortie liée aux plongements, normalisation finale : conforme à GPT-2. Pertes plausibles : 3,31 nats par jeton sur le texte ordinaire, 0,49 sur un mot répété (copie dans le contexte), environ 11 pour les réseaux réinitialisés (loi uniforme : ln 50 257 = 10,82), de 33 à 37 pour les poids mélangés, 49 quand les mises à jour sont coupées (le réseau prédit le jeton courant).
- **Découpage en jetons.** « Hello world » donne 15496, 995 ; chaque mot répété fait un seul jeton ; les passages font de 82 à 87 jetons, tronqués à 64.
- **Réinitialisation.** Loi normale d'écart-type 0,02, projections de sortie de l'attention et du perceptron à 0,02/√24, biais nuls, normalisations à l'identité, plongements à 0,02 : conforme au plan et à l'initialisation publique.
- **Mélange.** Chaque tenseur permuté, plongements et normalisations compris ; la matrice de sortie, liée, est mélangée avec eux.
- **Lésion.** Sorties d'attention et de perceptron de tous les blocs, biais compris, multipliées par α.
- **Bruit.** Norme relative η, par position ; amplitude dépendante de l'état, sans effet notable (constat 4).
- **Perturbation et réponse.** Vecteur de direction tirée au hasard, de norme égale à celle de l'activation propre au site, ajouté à l'entrée du bloc 3 en position 16, jetons forcés identiques ; réponse au flux résiduel de sortie du dernier bloc, avant la normalisation finale.
- **Lempel-Ziv.** Conforme à Kaspar et Schuster ; lecture position par position ; normalisation par L·H(p)/log₂(L), 0 si p = 0 ou 1, comme au plan.
- **Graines.** Une par tâche, issues d'une `SeedSequence` ; consignées dans la sortie.

## Scripts et sorties de la contre-lecture

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/d69341ed-1da2-5804-bff1-02b01c73e5e7/scratchpad/contre-lecture-calcul-v1/`. Rien écrit dans le dépôt ; aucun appel payant, aucune machine louée. Un écart à déclarer : en important le script original, mon diagnostic a fait écrire par Python un cache de code compilé dans le dossier de Fable (`travail/scripts/__pycache__/calcul_illustratif_v1.cpython-313.pyc`, 11:36:07). Je l'ai retiré, avec son dossier, à la fin de la contre-lecture. Aucun fichier de Fable n'a changé (empreintes du script, des résultats et de la note vérifiées après le retrait), mais l'heure de modification du dossier `travail/scripts/` garde la trace de cette création et de ce retrait.

| Fichier (relatif au dossier ci-dessus) | Rôle | Empreinte SHA-256 |
|---|---|---|
| `diag/diag_normalisation_v1.py` | indice du script sur matrices au hasard | `8adad14ef37c463a3613eaaa10ecc0912b1bb15879872dada5a7423794602cdc` |
| `diag/sortie-diag-normalisation-v1.txt` | sa sortie | `0fb80cc1040cde76ada25e26f2d479981905074c633375327d1b2b97a664b3c4` |
| `diag/diag_lz76_v1.py` | contrôle de Lempel-Ziv contre Kaspar et Schuster | `5b21b0845fb59b585a7c422591f9a9b74bec9f049f7fb0634f73c8646203a51d` |
| `diag/sortie-diag-lz76-v1.txt` | sa sortie | `ba4e2aada0aacd7478b62c2b8c4bf5664a9a7c56cb454759c0ce03f3cc57edad` |
| `diag/diag_reponses_v1.py` | détail réponse par réponse, variante du bruit figé | `915dcfad4832469be60ea330fff6a5ac8d0f5b53b54f1dff3cf8e10496e8c4b4` |
| `diag/sortie-diag-A-v1.txt` | résumés : réseau entraîné (deux entrées), réinitialisé et mélangé (graine 1) | `17304a9827e93aa0ccc602086dd33699151598831d800609f1a237e45c83ff68` |
| `diag/diag-A-v1.json` | détail réponse par réponse de ces conditions | `ac6200a49d1c976cef4de096861b7b36bd9a9d5f9a7956bcb854383aba13a8d0` |
| `diag/sortie-diag-B-v1.txt` | résumés : amortissement de 0,55 à 0, bruit 0,8 | `d19655e77c277c6d2428b549dc8169ec6a0a65bc9a88a3de927c4771a6397438` |
| `diag/diag-B-v1.json` | détail de ces conditions | `fefb0bbb88850d8e9ae0064c900115904aa3653151a609e70f90baf12f4a71c2` |
| `diag/sortie-diag-C-v1.txt` | résumés : bruit de 0,05 à 0,2, variantes figées | `d5c2364b3115129065d48bc3be25a7c37c4ebd1e15488d2b68b6c5610e980e94` |
| `diag/diag-C-v1.json` | détail de ces conditions | `e4d5a5d71436535ea6055cf2f88688cb5ccdb7cff08b57f77bfbf53f04aa29d9` |
| `diag/resumer_diag_v1.py` | résumé compact des sorties | `7d05f8cdf076a754cc08f87d093011131a91f244edd49b9e56a5483275168bf0` |
| `diag/analyse_diag_v1.py` | corrélations de rang, écarts appariés par passage, bruit figé | `5e6440bc8e7143dfd62a101851b2ec24ef58066338556724879977c061d8a176` |
| `diag/sortie-analyse-diag-v1.txt` | sortie de l'analyse | `b8c5a2a83b4df07b63509518569feaf18355b14e65ac26a5f29c75621e7c2b2f` |
| `relance/resultats-relance-v1.json` | relance complète du script original | `1527aa16af7f0fb4f85c343dd7fd6c1930a3a1d88a94764032c4fe548de9155b` |
| `relance/journal-relance-v1.txt` | son journal | `d1c63f0aa52ca3a03f999cac01f64d90562e4deefee6d7a76aacb297d7b8bd46` |
| `textes-sl/page-2.txt` à `page-5.txt` | texte extrait des p. 2 à 5 de [SL], lu | extraits de travail, non empreintés |

La même commande d'extraction a produit aussi `textes-sl/page-1.txt` et `page-6.txt` à `page-9.txt`, que je n'ai pas lus. Commande du diagnostic : `python3 -I diag/diag_reponses_v1.py SCRIPT POIDS RESULTATS SORTIE CONDITIONS…`, avec `OPENBLAS_NUM_THREADS=1`.
