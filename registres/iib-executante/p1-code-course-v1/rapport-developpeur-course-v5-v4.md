# Rapport du développeur — tirage des jetons sur la carte (correctif 0020) — v4

Date : 2026-11-22. Pièce d'instrument (classe B), à contre-lire. Développeur : Claude Opus 5.5. Ce rapport complète les v1 à v3, intactes. Rien poussé, rien dépensé, aucune machine, aucun modèle téléchargé.

- Branche locale à part, **`prep/iib-tirage-carte-local`**, partie de `997bed6a1`. Les correctifs 0014 à 0019 ne sont pas touchés.
- Tête **`5d3f4761d179d1529887e327e665331e38bb0b0c`**, arbre **`e8c95493d8af2404c2d9c5abca360997aea82418`**.
- Correctif `0020-…patch`, à appliquer après 0019.

## 1. Le diagnostic, confirmé à la lecture
Trois chemins copient les logits du dernier jeton vers le processeur à chaque pas : `harnais/episode.generer_lot` (l. 107), `environnements/noter_rejeu_juges_v2.generer_lot_borne` (l. 527) et `iib/modele_v1._suites_cache_duplique` (l. 70 et 91). Les trois font ensuite softmax et `multinomial` ligne par ligne, chacun avec un générateur processeur par ligne. Aucun de ces trois fichiers n'est modifié.

## 2. Méthode retenue : Gumbel-max à bruit compté, et pourquoi
- Le jeton tiré est argmax(logits / T + G), où G suit la loi de Gumbel, indépendante d'un jeton du vocabulaire à l'autre. C'est un tirage **exact** de softmax(logits / T), sans softmax.
- G est une **fonction pure** de (graine de la ligne, numéro du pas, indice du jeton). Le calcul :
  - un hachage entier de 32 bits, vectorisé en int64 ;
  - multiplications par une constante inférieure à 2³¹ sur des valeurs inférieures à 2³², donc aucun dépassement : le résultat est identique sur processeur et sur carte, au bit près ;
  - deux tirages de 32 bits réunis en un uniforme de 53 bits, puis −log(−log u) en double précision.
- Il n'y a ni copie des logits, ni générateur, ni boucle Python par ligne.
- **Écarté : des générateurs par ligne sur la carte.** Un `torch.Generator` par ligne impose un appel de tirage par ligne, donc une boucle. Son état dépend de tout ce qu'il a déjà tiré.
- **Avantage du bruit compté :** une ligne ne dépend ni des autres lignes du lot, ni de leur nombre, ni de leur ordre. Rejouée seule, elle rend les mêmes jetons, à logits égaux.
- **Ce qui ne change pas :**
  - les interfaces et les valeurs rendues (le plan porte en plus la clé `tirage`) ;
  - les graines par ligne ;
  - le remplissage à gauche, les positions explicites, le cache, les logits du dernier jeton seuls ;
  - les jetons de fin, gardés, et les lignes finies remplies de `pad_id` ;
  - les arrêts « fin », « budget » et « bloc clos » ;
  - `decalage_positions` ;
  - l'empreinte des logits, qui ne copie que sur demande, comme avant.
- **Ce qui change :** le flux aléatoire. Mêmes graines et même loi, mais **pas les mêmes jetons** que `multinomial` sous un générateur processeur. Les deux chemins ne se mélangent pas dans une même mesure.
- **À température nulle**, les deux chemins sont identiques au jeton près ; c'est vérifié par un essai.
- **Résolution :** l'uniforme est sur 53 bits ; un jeton de probabilité inférieure à environ 2⁻⁵³ n'est jamais tiré.
- **Ce qui reste copié vers le processeur :**
  - à chaque pas, un booléen (« reste-t-il une ligne active ? ») et les indices des lignes qui viennent de finir ou de tirer un jeton déclencheur. Sur ces lignes seulement, la fonction `arreter` de l'appelant est jouée en Python, comme avant ;
  - à la fin, les jetons et les longueurs.

## 3. Ce qui est écrit
- **`src/controle_ia/harnais/tirage_carte_v1.py`** (neuf) : `bruit_de_gumbel`, `tirer`, et trois fonctions qui remplacent les anciennes à interface égale : `generer_lot_carte` (pour `generer_lot`), `generer_lot_borne_carte` (pour `generer_lot_borne`), `suites_cache_duplique_carte`.
- **`src/controle_ia/iib/modele_tirage_carte_v1.py`** (neuf) : `ModeleTorchTirageCarte(ModeleTorch)`. Les actions, les suites en cache dupliqué et le repli « prerempli_par_suite » passent tous par le tirage sur la carte. L'agent et le jumeau sont donc toujours sous la **même** méthode. Le repli est consigné de même.
- **Choix explicite, défaut inchangé :**
  - `modele_v5` : `TIRAGES = ("processeur", "carte")`, `TIRAGE_DEFAUT = "processeur"`, `exiger_tirage` (« carte » refusé en mode jouet, valeur inconnue refusée), et l'option `tirage` dans `construire_modele` et `charger_modele_reel` ;
  - `lanceur_v5` : `executer(…, tirage="processeur")`, ligne de commande `--tirage {processeur,carte}` (défaut processeur) ; le tirage est écrit au résumé et à la marque de chargement.
  - Je ne suis pas passé par la configuration : la configuration de l'étalonnage est scellée, et la course doit avoir la même empreinte.
- **`environnements/noter_rejeu_juges_v2.py` n'est pas raccordé** (autre chantier) : la fonction de remplacement existe, et l'essai d'égalité à température nulle la compare à l'ancienne.
- **L'amorce de la course** cite la liste de la course en version 2 (`scripts/tests-cibles-iib-course-v5-v2.txt`, la v1 plus `tests/test_tirage_carte_v1.py`), pour que l'essai marqué « carte » se joue sur la machine. Elle ne passe **pas** `--tirage carte`, et la v1 de la liste reste en place.

## 4. Essais (`tests/test_tirage_carte_v1.py`, 12 essais, plus 1 dans `test_iib_lanceur_v5.py`)
1. **Déterminisme :** à graines égales, deux passages donnent les mêmes jetons et le même plan (lot, suites) ; des graines autres donnent d'autres jetons. L'essai marqué carte (`skipif` sans CUDA) vérifie le déterminisme sur la carte, le bruit calculé sur l'appareil, et le hachage égal au bit près sur la carte et sur le processeur.
2. **Indépendance des lignes :** une ligne donne les mêmes jetons seule, dans un lot de 4 ou dans un lot de 8, où les autres lignes et leurs graines changent (autres lignes plus courtes, donc aucun remplissage de la cible). Le bruit d'une ligne est égal au bit près d'un lot à l'autre. L'égalité des jetons suppose des logits égaux ; sur carte, un lot de taille différente peut faire varier les logits au dernier bit (réserve).
3. **Loi :** à trois températures, 40 000 tirages sur 7 jetons finis plus un jeton à −inf ; khi-deux contre le softmax, p > 10⁻³ ; le jeton à −inf n'est jamais tiré. La loi est aussi vérifiée le long d'une ligne, sur 4 000 pas. **Artefact :** un tirage faux (bruit uniforme au lieu de Gumbel) est refusé par le même essai, p < 10⁻⁶.
4. **Égalité avec l'ancien chemin à température nulle :** `generer_lot` (jetons, plan, empreintes de logits, fins nombreuses), `generer_lot_borne` (jetons et arrêts), `ModeleTorch` contre `ModeleTorchTirageCarte` (actions, suites dans les deux formes).
5. **Gardes, cas sain et artefact :**
   - graine hors de [0, 2⁶⁴[, booléenne, non entière : refus ;
   - logits NaN, +inf, ou ligne entièrement à −inf : arrêt ; −inf sur une partie du vocabulaire : permis ;
   - température non finie : refus ;
   - lot vide, contexte vide, graines en nombre faux, `max_nouveaux` < 1, suites sans graines : refus ;
   - `exiger_tirage` : refus en mode jouet et pour une valeur inconnue ;
   - lanceur : `tirage="carte"` en mode jouet refusé avant le manifeste ; défaut « processeur » écrit au résumé ;
   - garde statique : ni copie, ni `multinomial`, ni générateur, ni boucle dans `tirer` et `bruit_de_gumbel`.
- Rejoués : voir § 6.

## 5. Vitesse, indicative seulement (`sortie-mesure-vitesse-tirage-v1.txt`)
Mesure sur processeur, 4 fils, petit Llama à poids aléatoires, 8 lignes de 64 jetons, médiane de 5 passages :

| vocabulaire | ancien | neuf |
|---|---|---|
| 64 | 78 ms | 78 ms |
| 32 000 | 498 ms | 517 ms |
| 128 256 | 1 961 ms | 2 524 ms |

**Sur processeur, le chemin neuf ne gagne rien et coûte environ 1,1 ms de plus par jeton au plus grand vocabulaire.** Le bruit haché en double précision coûte plus cher que softmax et `multinomial` sur processeur. Le gain attendu est sur la carte : plus de copie de 128 000 logits par ligne et par pas, plus de boucle Python par ligne, et les opérations sur le bruit (environ un million d'éléments par pas pour 8 lignes) sont élémentaires sur l'appareil. **Ce gain n'est pas mesuré**, et ne le sera que sur la machine.

Sur la cause de la lenteur de l'étalonnage, la question reste ouverte. La note du 22 novembre (point 3 (a)) rattache le ralentissement au processeur de l'hôte ; ce correctif ôte ce chemin, mais rien ici ne prouve que c'était la cause.

## 6. Nombres attendus
- Liste figée v6 (étalonnage), inchangée en fichiers : **295** (ajout d'un essai du choix de tirage dans `test_iib_lanceur_v5.py`).
- Liste de la course v2, sur une machine à carte : **295 + 2 (moteur à torch) + 12 (tirage) = 309**. Sur un poste à processeur avec torch, l'essai marqué carte se saute : « 308 passed, 1 skipped ».
- Rejoué sur ce poste (`sortie-essais-p1-v4.txt`) : (A) liste v6, **295 passed** ; (B) liste de la course v2 avec torch, **308 passed, 1 skipped** (l'essai marqué carte) ; (C) essais du tirage seuls, 11 passed, 1 skipped.

## 7. Pour l'ordre (nœuds, non codés)
- **N-T1, quel tirage pour la course.** L'étalonnage a tiré sous l'ancien chemin. La course, sous « carte », tirerait sous un autre flux aléatoire, de même loi. L'agent et le jumeau de la course restent sous la même méthode, mais les flux de l'étalonnage et de la course diffèrent. Ce n'est pas un seuil ni une règle du texte scellé, mais une différence de procédure entre les deux phases : à trancher par Lazar ou par l'ordre (`--tirage carte` dans l'amorce de la course, ou rien).
- **N-T2.** Le gain sur carte n'est pas mesuré : une mesure de quelques minutes sur la machine (ancien contre neuf, même lot) peut précéder le choix.

## 8. Livrables v4
`0020-…patch`, ce rapport, `sortie-essais-p1-v4.txt`, `sortie-mesure-vitesse-tirage-v1.txt` ; script de mesure hors du dépôt : `…/scratchpad/mesure-tirage/mesure_vitesse_tirage_v1.py`.

Arbre final : `e8c95493d8af2404c2d9c5abca360997aea82418`.
