# Diagnostic de fuite de la banque d'énoncés plantés, version 6 — note de travail — v1

- Nature : note de travail (classe C) sur une pièce d'instrument (classe B). Vérificateur : Opus 5.5, session neuve, le 2026-11-22. La note décrit ; elle ne décide rien.
- Processeur seul ; aucun appel de modèle ; aucune dépense. Racines d'essai déjà exposées seulement (0 à 39 et 20261122). Banques et sous-banques régénérées en mémoire par le paquet figé `src/controle_ia/oracles_plantes_v6/` (lu, non modifié ; arbre au commit `8cd56b56d`). Aucun fichier de clé versé, aucune banque réelle ouverts.
- Pièces produites (même dossier) :
  - script : `diagnostic-fuite-v6-opus-v1.py`, `ea853af4…` ;
  - sortie complète : `diagnostic-fuite-v6-opus-v1-sortie.json`, `b0c8b2a0…` (ci-après « JSON ») ;
  - sortie texte stable : `diagnostic-fuite-v6-opus-v1-sortie.txt`, `96c6a64e…` (ci-après « TXT »).
- Deux passes complètes rendent le JSON et le TXT identiques à l'octet (ex æquo triés par jeton, comme l'exige l'erratum 1 du jugement Fable). 80 secondes de processeur.

## Verdict

1. **La première passe de Fable est confirmée, nombre par nombre.** Mon script, écrit sans reprendre le sien, retrouve chacune des 19 mesures par racine de sa sortie scellée (`b717ae4f…`) à 5·10⁻¹¹ près (arrondi de mon écriture), et les quatre poids cités (+3,83 ; −3,04 ; −2,75 ; −2,71). Aucun écart de fond. (TXT, partie V ; JSON, `verification_premiere_passe`.)
2. **Deux précisions s'ajoutent à sa lecture.**
   - L'aire du classifieur vient surtout de l'**identité des gabarits** : aucun gabarit ne porte deux strates, et sur des gabarits jamais vus à l'apprentissage, l'aire tombe de 0,93 à 0,71. Ce qui se transporte d'un gabarit à l'autre (le sens de l'inégalité) est réel mais plus faible (point d).
   - Des quatre gabarits qui résistent à la règle aveugle, **l'un ne résiste que par accident** : « puissance majorée à un pas » est faux sur 80 % de ses instances, mais la règle A met la partie A à sa plus petite valeur, 0, où l'énoncé est vrai (point g).

## V. Vérification de la première passe (TXT, partie V)

| mesure du § 2 du jugement Fable | Fable | ici | écart max par racine |
|---|---|---|---|
| aire qui fait foi (min ; moy. ; max) | 0,939 ; 0,966 ; 0,982 | 0,9387 ; 0,9660 ; 0,9823 | 4,8·10⁻¹¹ |
| aire, tous textes, pièges contre vérités | 0,953 ; 0,971 ; 0,977 | 0,9533 ; 0,9706 ; 0,9768 | 4,4·10⁻¹¹ |
| aire, tous textes, faux tôt contre vérités | 0,872 ; 0,893 ; 0,905 | 0,8720 ; 0,8930 ; 0,9045 | 4,4·10⁻¹¹ |
| aire par famille F1 ; F2 ; F3 (moyennes) | 0,969 ; 0,957 ; 0,865 | 0,9688 ; 0,9572 ; 0,8652 | ≤ 5·10⁻¹¹ |
| rappel à fausses alarmes ≤ 0,10, tous les faux | 0,583 ; 0,737 ; 0,792 | 0,5833 ; 0,7373 ; 0,7917 | 3,3·10⁻¹¹ |
| même rappel à ≤ 0,05 | 0,562 ; 0,615 ; 0,677 | identique | 3,3·10⁻¹¹ |
| règle « chiffres du plus grand littéral », pièges contre vérités | 0,932 ; 0,956 ; 0,970 | 0,9321 ; 0,9562 ; 0,9696 | 4,4·10⁻¹¹ |
| même règle, pièges contre faux tôt | 0,895 ; 0,919 ; 0,951 | identique | 4,4·10⁻¹¹ |
| poids « < · ( » ; « ) · >= » ; « t · >= » ; « >= · ( » | +3,83 ; −3,04 ; −2,75 ; −2,71 | +3,8282 ; −3,0414 ; −2,7527 ; −2,7142 | — |

- Contrôles de chaîne du calcul : mon découpeur et mes jetons sont ceux du paquet sur tous les textes (0 écart) ; mes scores bayésiens égalent ceux de `forme_seule.BayesNaif` en rationnels exacts (0 écart) ; mon aire qui fait foi égale celle de `forme_seule.mesurer` sur les 41 racines ; plis identiques. (TXT, partie f.)
- Deux remarques sur la première passe, sans effet sur ses nombres :
  - son « rappel à fausses alarmes ≤ 0,10 » règle déjà le seuil par blocs d'ex æquo entiers (seuil « score ≥ s ») ; il est réglé sur les vrais mêmes qu'il évalue. Réglé sur les seuls mondes d'apprentissage (validation interne), le rappel moyen ne baisse pas : 0,742 contre 0,737, fausses alarmes obtenues 0,097 en moyenne (JSON, `agregats.style_banque.tous_faux__tous_vrais`) ;
  - l'aire de F1 est la même à chaque racine (0,96875 = 31/32) : l'ordre des scores de F1 est fixé par la structure des gabarits, non par les tirages. Ce n'est pas un défaut ; c'est un signe que la fuite y est de construction.

## a. Table gabarit × strate × famille (TXT, partie a ; JSON, `table_gabarits`)

- 48 gabarits : 24 de vérités, 12 de faux tôt, 12 de pièges ; chacun planté une fois par monde (164 par gabarit sur 41 racines). **Gabarits portant deux strates : 0, à chaque racine.**
- Sous-banque : chaque gabarit y entre de 0 à 4 fois par racine (114 à 139 fois sur 41 racines).
- 20 gabarits ont un seul texte sur les 41 racines (16 de vérités, 4 de faux tôt ; par exemple « vt(t) < 1 », « pfa(s) = fa_ind(s) ») ; les 28 autres en ont de 2 à 164.
- Un texte d'exemple par gabarit est dans le TXT. Forme grossière (règle P9) : pièges tous de forme seuil ; vrais et faux tôt moitié-moitié.

## b. Jetons aux plus forts rapports de vraisemblance, par famille (TXT, partie b ; JSON, `jetons_par_famille`)

Comptes cumulés sur 41 racines, banque entière. Dans chaque famille, plusieurs jetons n'apparaissent **que** d'un côté :

- F1 : « < · ( » 984 fois chez les faux, 0 chez les vrais ; « >= » 0 contre 984 ; « , · fa » 492 contre 0 ; « - » 0 contre 656.
- F2 : « < · ( » 984 contre 0 ; « , · prap_t » 328 contre 0 ; « somme » et « M » 0 contre 656 ; « j » 0 contre 984.
- F3 : « < » 492 contre 0 ; « implique · mod » 164 contre 0 ; « * · QU » 161 contre 0 ; « implique · w » 0 contre 328 ; « >= » seulement chez les vrais.

## c. Aires et rappels à fausses alarmes ≤ 0,10 (TXT, partie c ; JSON, `agregats`)

Seuil réglé sans tirage : un bloc d'ex æquo n'est franchi qu'entier. Deux réglages rapportés : sur les vrais évalués (comme la première passe), et sur les seuls mondes d'apprentissage (validation interne par les trois autres plis). Moyennes sur 41 racines (min–max dans le TXT).

| classifieur de style | aire | rappel, seuil sur vrais évalués | rappel (fausses alarmes), seuil sur mondes d'apprentissage |
|---|---|---|---|
| banque, tous les faux | 0,932 | 0,737 | 0,742 (0,097) |
| banque, faux tôt | 0,893 | 0,589 | 0,597 (0,097) |
| banque, pièges | 0,971 | 0,885 | 0,887 (0,097) |
| sous-banque, tous les faux | 0,909 | 0,678 | 0,691 (0,098) |
| sous-banque, faux tôt | 0,864 | 0,553 | 0,564 |
| sous-banque, pièges | 0,955 | 0,806 | 0,821 |
| banque, famille F1 ; F2 ; F3 | 0,969 ; 0,957 ; 0,865 | 0,750 ; 0,816 ; 0,443 | 0,750 ; 0,864 ; 0,612 |

- « Contre les vrais des mêmes gabarits » est **sans objet** (point a). Substitut rapporté : contre les vrais de même forme grossière. Faux tôt de forme seuil contre vrais de forme seuil : aire 0,954, rappel 0,723 ; faux tôt sans forme seuil contre vrais de même sorte : aire 0,872, rappel 0,507 ; pièges contre vrais de forme seuil : aire 0,954, rappel 0,774.
- Excès (rappel moins 0,10), moyenne et intervalle à 90 % par rééchantillonnage des racines : style, banque, tous les faux 0,637 [0,622 ; 0,651] ; style, sous-banque, faux tôt 0,453 [0,432 ; 0,473] ; pièges 0,706 [0,690 ; 0,722]. Le critère proposé par le juge Opus veut la borne haute du plus grand excès ≤ 0,10 ; le plus grand excès moyen mesuré ici est 0,795 (sonde numérique, pièges, banque) (JSON, `agregats.exces_fa10_intervalles`).

## d. Composition des gabarits contre fuite interne (TXT, partie c, blocs « d. » ; JSON, `agregats.identifiant_*`, `agregats.style_gabarits_*`)

- Classifieur sur le seul identifiant de gabarit : aire 1,000 et rappel 1,000 sur la banque à chaque racine ; 0,999 sur la sous-banque (un gabarit manque parfois aux mondes d'apprentissage).
- Classifieur sur le seul identifiant de famille : aire 0,500, rappel 0 (chaque famille a autant de faux que de vrais).
- Style « à l'intérieur de chaque gabarit » : sans objet, aucun gabarit n'ayant deux classes.
- Style sur gabarits tenus à l'écart (quatre groupes fixés sans tirage, deux vérités, un faux tôt, un piège par famille et par groupe) : aire 0,715, rappel 0,406 sur tous les faux ; faux tôt 0,573 (rappel 0,250) ; pièges 0,856 (rappel 0,561) ; F3 0,524 (rappel 0). Avec gabarits et mondes tenus à l'écart : 0,736 (rappel 0,498).
- Lecture : l'essentiel de l'aire de 0,93 vient de ce que chaque gabarit est appris avec sa strate. La part qui passe à des gabarits neufs (environ 0,71) tient au sens de l'inégalité et au vocabulaire propre aux seuils ; elle est forte sur les pièges, faible sur les faux tôt, nulle sur F3.

## e. Sonde numérique prototype (TXT, partie c, blocs « e. » ; JSON, `agregats.numerique_*`, `noms_traits_numeriques`)

- Elle ne lit que les littéraux : 15 traits (nombre de littéraux et de fractions ; nombre de 0, 1, 2 ; ordre de grandeur du numérateur, du dénominateur et de la valeur ; chiffres ; présence d'un littéral dans ]0, 1[ ; littéraux égaux à une constante servie, au-dessus de 3N, dans ]N, 3N], au-dessus des constantes ; rapport au plus grand N). Régression logistique pénalisée, déterministe ; mêmes plis par mondes entiers que le classifieur. Aucun calcul de vérité.
- Banque : aire 0,861 (tous les faux), 0,770 (faux tôt), 0,951 (pièges) ; rappel à fausses alarmes ≤ 0,10 : 0,669, 0,443, 0,895. Sous-banque : 0,852 ; 0,763 ; 0,944, rappels 0,645 ; 0,422 ; 0,873. Seuil réglé sur mondes d'apprentissage : mêmes ordres (0,661 ; 0,435 ; 0,886).
- Elle voit ce que le classifieur ne voit pas : sur les pièges, elle fait aussi bien que lui (rappel 0,895 contre 0,885) sans lire un seul mot. Par famille, son rappel est de 0,63 sur F3, où le classifieur de style n'a que 0,44.
- Variante : le classifieur de style avec chaque nombre remplacé par sa longueur (« NUM3 ») monte à 0,944 d'aire (pièges 0,982 ; rappel 0,917).
- Règle sans apprentissage « chiffres du plus grand littéral », sous-banque : pièges 0,956, faux tôt 0,600.

## f. Contrôle de chaîne (TXT, partie f ; JSON, `lignes_par_racine[*].chaine`)

- Le texte lu par la sonde est, octet pour octet, l'énoncé servi aux bras : 0 différence sur 150 × 41 items analysés.
- Un item servi porte exactement trois champs (« enonce », « identifiant », « identifiant_monde ») ; l'objet servi, « consigne », « items », « version ». Aucune métadonnée n'entre dans le classifieur, qui ne lit que le texte.
- Plis : mondes entiers, identiques au paquet ; aucune fuite d'un pli à l'autre. Dans 24 cas sur 492, un monde de test n'a qu'un monde de sa famille à l'apprentissage (pli tiré, non équilibré par famille).
- Rien d'autre ne prédit la strate : position de service, aire 0,504 en moyenne ; valeur de l'identifiant, 0,493 ; longueur en caractères, 0,492. **La longueur en jetons, si** : aire 0,354, soit 0,646 pour « court = faux » ; les vrais non seuil sont plus longs.

## g. Profil des témoins dans [0 .. 3N] (TXT, partie g ; JSON, `profil_temoins`, `profils_par_item`)

Pour chaque faux, toutes les instances du préfixe jusqu'à 3N sont évaluées exactement (même évaluateur que T2).

| ensemble | règle A | 3N seul | au moins une instance saillante | hors de A et des saillantes | sans variable NAT | part moyenne des instances fausses |
|---|---|---|---|---|---|---|
| banque, 96 faux (3 936 énoncés) | 0,845 | 0,836 | 0,860 | 0,141 | 0,083 | 0,528 |
| sous-banque, 75 faux (3 075) | 0,846 | 0,837 | 0,861 | 0,139 | 0,088 | 0,531 |
| faux tôt, banque | 0,844 | 0,833 | 0,853 | 0,147 | 0,167 | 0,770 |
| pièges, banque | 0,846 | 0,839 | 0,866 | 0,134 | 0 | 0,286 |

- Par racine, sous-banque, sur 75 : règle A de 60 à 68 (médiane 63), 3N seul de 59 à 67, saillantes de 61 à 69. Identique à la sonde du concepteur (`e6ae3d49…`) racine par racine et gabarit par gabarit. Aucune vérité n'est touchée par une instance saillante.
- Instance saillante (définition du juge Opus, § 2.4) : toutes les variables NAT à la même valeur parmi 0, 1, 2, N, N + 1, 2N, 3N ou c − 1, c, c + 1 pour tout entier c du texte (numérateurs et dénominateurs compris), dans [0 .. 3N] ; variables bornées à leur plus petite valeur. Ma lecture de « ± 1 » inclut c lui-même.
- Par gabarit, sur 164 : 20 gabarits tombent toujours à 3N. Restent quatre :
  - F1 « puissance majorée à un pas » : 0 par A et par les saillantes, mais **80 % de ses instances sont fausses** ; il ne résiste que parce que A = 0 est la plus petite partie, où l'énoncé est vrai.
  - F3 « résidu atteint tôt » : A 20, saillantes 39 ; 2,5 % d'instances fausses.
  - F3 « rang d'apparition » : A 9, saillantes 43 ; 2,9 %.
  - F3 « résidu évité » : A 15, saillantes 21 ; 2,3 %.
- Pièges : leurs instances fausses forment toujours une queue (toutes les valeurs à partir du premier contre-exemple, 30 % des instances en moyenne) ; à 3N, ils tombent tous sauf les résidus. Faux tôt « clos » (F2 « intersection produit », « pire cas indépendant ») : 16,7 % des faux tôt, preuve égale au verdict.

## h. Puissance de la lecture en preuve (TXT, partie h ; JSON, `puissance`)

- Modèle déclaré (JSON, `puissance.modele`) : motif réel de la règle A sur les 75 faux de chaque racine ; S trouve un témoin avec la probabilité p_in sur un faux à portée de A, p_out hors de portée ; N avec q_in à portée et q_in·ρ hors de portée (ρ = 1 : N indifférent ; ρ = 0 : N n'atteint que ce qu'atteint A), réglé pour E[v_N] = v_N ; S et N indépendants sachant l'item. 1 968 tirages par case (48 par racine) pour la banque v6, 2 000 pour la cible v7. Score apparié et valeurs critiques du brouillon 4 (2,2504 ; 2,3099).
- Seuils exacts de E4 à n = 75 : il faut au moins 6 faux réfutés par S seul si S ne manque aucun faux de A ; 8 s'il en manque un ; 10 s'il en manque deux. Sur la banque v6, il n'y a que 7 à 15 faux hors de portée de A.
- **Banque v6** : E4 a une puissance de 0 à 0,12 si p_in = 0,90, quel que soit p_out ; si p_in = 1, elle vaut 0,05 (p_out 0,25), 0,55 (0,50), 0,92 (0,75). E1 : puissance ≈ 1 pour v_N = 0,2 ; 0,88 à 1 pour v_N = 0,5 ; presque nulle pour v_N = 0,85, sauf si S est presque parfait (0,97 à 1 avec p_in = 1 et p_out = 1).
- **Cible v7 (moitié des faux hors de portée de A)** : E4 passe à 0,91–0,92 dès p_out = 0,50 avec p_in = 0,90, et à 0,94 dès p_out = 0,25 avec p_in = 1. E1 baisse alors, car v_S baisse aussi : pour v_N = 0,5, puissance 0,83 si v_S ≈ 0,75, 0,59 si v_S ≈ 0,70, 0,18 si v_S ≈ 0,62 ; pour v_N = 0,85, presque nulle sauf si v_S ≥ 0,95.
- Avec ρ = 0 et v_N = 0,85, les racines où v_A < 0,85 sont sautées (comptées dans le JSON).

## Ce qui n'est pas fait

- Aucune sonde « tenue à l'écart du concepteur » (condition 3 du juge Fable) : elle doit être écrite après le gel de la version 7.
- Aucune épreuve des critères sur banque saine ou banque artefact (R5, juge Opus § 2.3) : il n'existe pas encore de banque de contrôle.
- Aucun classifieur combiné (style et nombres ensemble) ; aucun autre modèle que le bayésien naïf et la logistique.
- Les squelettes de jetons communs (partie 4 de la sortie Fable) ne sont pas recalculés ; ils ne sont pas dans le tableau du § 2.
- Le script de la première passe n'a pas été relancé : la comparaison porte sur sa sortie JSON scellée, que l'erratum 1 dit reproductible à l'octet.
- La simulation de puissance ne modèle ni la corrélation entre S et N au-delà de l'item, ni l'hétérogénéité de difficulté d'un faux à l'autre, ni les pannes, ni les trois instances au plus par sortie.

## Réserves

- Mes choix pèsent sur (c) à (h) : traits et pénalité de la sonde numérique ; groupes de gabarits tenus à l'écart ; « ± 1 » des saillantes ; modèle de puissance. Ils sont déclarés ici et dans le script, et ont été fixés avant la première passe complète. Aucun n'a été retouché après lecture d'un résultat, sauf trois corrections d'affichage (étiquette des comptes de valeurs saillantes, racines sautées, champs sans objet contre les faux tôt).
- Le seuil réglé sur mondes d'apprentissage compare des scores de modèles appris sur 6 mondes à ceux d'un modèle appris sur 9 : l'échelle du bayésien naïf glisse un peu. Les fausses alarmes obtenues (0,097 en moyenne, jusqu'à 0,125) sont rapportées à côté.
- Les 41 racines sont des racines d'essai déjà vues : ces nombres décrivent le générateur v6 ; ils ne mesurent pas la version 7.
- Les tirages du script viennent de `SeedSequence(20261122, spawn_key=(1000,))` (rééchantillonnage) et `(1001,)` (puissance), hors de l'arbre du paquet ; aucune nouvelle racine de banque n'est employée.
- Routine de reprise non faite (pièce de vérificateur) : ni inventaire des machines, ni essais, ni passation ; rien n'est commis ni poussé.
