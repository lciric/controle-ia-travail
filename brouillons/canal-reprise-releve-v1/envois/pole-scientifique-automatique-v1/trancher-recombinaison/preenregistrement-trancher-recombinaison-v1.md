# Préenregistrement — trancher la recombinaison bisociative — v1

Scellé le 2026-10-26T19:10:31Z (heure lue sur `date -u` dans la commande qui l'écrit), **avant toute exécution d'une méthode sur
un monde**. Seuls ont tourné : le générateur et sa validation (`validation-generateur-v1.json`, propriétés des mondes,
graines de validation distinctes) et le calibrage du vocabulaire (`calibrer_vocabulaire_v1.py`, cosinus seulement).
Le seuil de 12 points et les contrôles viennent du brief ; ce document fixe leur mise en œuvre. Aucune contre-lecture
par un sous-agent neuf (règle R2) : le brief interdit les sous-agents ; c'est une réserve.

## 1. Mondes

Générateur `monde_v1.py` (paramètres `BASE`), conditions `conditions_v1.py`, 400 mondes par condition, graine du monde
`random.Random(20261026000000 + 100000 × identifiant de condition + indice)`.
- 8 domaines, 5 articles chacun (40 candidats) ; domaines répartis en 2, 3 ou 4 champs (tirés au hasard par monde) :
  proches = même champ, éloignés = champs différents.
- Opérateurs latents : 3 par groupe (groupe = champ ; transversal aux champs dans le monde inversé) ; opérateur
  principal du groupe (0,7) ou propre à l'article (0,3) ; second opérateur (0,3) ; un opérateur moyeu présent dans
  25 % des articles. Un même opérateur porte un mot de surface différent dans chaque domaine.
- Ponts plantés : 3 greffes (un opérateur d'un autre groupe entre dans un article, contraintes rendues compatibles avec
  un porteur) et 3 jumeaux (un opérateur rare partagé par deux articles de domaines en relation cible). Deux mécanismes
  pour ne favoriser par construction ni les méthodes « opérateur rare » ni les méthodes « import ».
- Vérité : domaines éloignés (proches dans le monde inversé), opérateur latent commun non moyeu, contraintes vraies
  compatibles.
- Observations : vecteur de domaine (fréquences brutes des mots hors lexique, cosinus exact) ; étiquette de domaine
  (juste à 0,95, sinon un domaine voisin) ; étiquettes d'opérateur par un lexique (couverture, homonymes systématiques,
  parasites) ; contraintes sur 4 axes par le canal bruité de l'essai b4 (régime réaliste 0,15 / 0,15 / 0,10) ;
  qualité q uniforme sur [0,5 ; 1,5], indépendante de la vérité.
- Niveaux d'observation des opérateurs (couverture, parasites, homonymes) : bien (0,90 ; 0,05 ; 0,05), moyennement
  (0,70 ; 0,15 ; 0,10), mal (0,45 ; 0,30 ; 0,20).

Conditions : M_bien, M_moyen, M_mal ; SP_sans_pont (aucune greffe ni jumeau : vérité vide) ; V_domaines_mal_separes
(60 % de mots d'un vocabulaire commun) ; V_etiquettes_absentes (aucune étiquette) ; V_moyeux_dominants (2 moyeux à
0,6) ; INV_verite_inversee (ponts entre domaines proches, groupes transversaux : miroir exact). Sensibilité
descriptive : M_moyen avec moyeu à 0,10 et à 0,50 ; résultats par nombre de champs.

## 2. Budget et étage commun

k = 4 paires par génération, G = 3 générations, mêmes 40 candidats ; une paire acceptée n'est plus retirée ; budget
12 paires par monde. **Étage commun à tous les bras** (« même choix d'opérateur après tirage, même filtre ») : une paire
n'est acceptée que si les domaines observés diffèrent, si elle partage au moins une étiquette d'opérateur (l'opérateur
retenu, choisi après tirage, est l'étiquette partagée la plus rare) et si le filtre de compatibilité des contraintes
observées passe. Chaque bras est donc une loi, ou un ordre, sur les paires valides. Sans étiquettes, l'étage commun
garde seulement domaines différents et filtre.

## 3. Bras

- (a) **Forme corrigée** : L = diag(q)(S + γI)diag(q), S_ij = cos_ij², γ = 10⁻³ ; ordre glouton de tous les articles
  par Cholesky incrémentale (départage au premier indice ; articles mélangés) ; paires valides rangées par (rang
  maximal, somme des rangs) ; k suivantes par génération. C'est le correctif c5 de l'essai, étendu à k paires.
- (b) **Tirage stratifié** : strates = paires de domaines observés ; tour des strates ayant encore une paire valide,
  dans un ordre aléatoire rebattu à chaque tour ; dans la strate, une paire valide au hasard.
- (c) **Tirage uniforme** parmi les paires valides restantes.
- (d1) **Marche de Swanson** (caste 3 du rapport ; schéma A–B–C de Swanson) : ancre uniforme parmi les articles
  étiquetés, étiquette de l'ancre ∝ log(n / fréquence documentaire), arrivée uniforme parmi les porteurs d'un autre
  domaine observé ; loi exacte sur les paires, tirée sans remise parmi les paires valides.
- (d2) **Appariement par structure de cooccurrences étiquette × domaine** : score = max sur les étiquettes partagées de
  |f(m | domaine_i) − f(m | domaine_j)|, f = part des articles du domaine observé qui portent m (signature d'un
  import) ; paires valides rangées par score décroissant, départage aléatoire.
- (e) **Forme du rapport de Gemini** : L_ij = q_i q_j ⟨o_i,o_j⟩² (1 − cos_ij²), o = étiquettes observées normalisées ;
  Sinkhorn-Knopp 5 itérations (D L D symétrisé) puis γ minimal rendant la matrice semi-définie positive (bissection
  par Cholesky, + 10⁻⁹) ; loi ∝ déterminant 2 × 2, tirée sans remise parmi les paires valides.
- Diagnostics, non éligibles : (a_2dpp) processus déterminantal exact à 2 éléments avec le noyau corrigé ; (a_q1) (a)
  avec q ≡ 1 ; (b_eloigne) (b) servant d'abord les strates de cosinus moyen ≤ médiane ; (d1_inv) (d1) pondérée par
  1 / fréquence ; (oracle) vraies paires d'abord (plafond).

## 4. Mesures

Par monde puis moyenne sur les mondes : précision (vraies / acceptées), rappel (vraies trouvées / vraies du monde), rappel
par mécanisme, précision placebo (monde sans pont : 6 paires valides tirées au hasard, graine propre au monde,
indépendante des bras), part de paires éloignées et proches, strates distinctes / paires, pièges (opérateur-pont
homonyme, moyeu, parasite ; contraintes vraies incompatibles). Intervalles à 95 % : percentiles de 2 000
rééchantillonnages des mondes, appariés pour les écarts (graine `random.Random(20261026)` par condition).

## 5. Décision (règles du brief, mises en œuvre ici et gelées)

Δ_X = précision(a) − précision(b) dans la condition X.
1. **Adoptée** si Δ_M_bien ≥ 0,12 et Δ_M_moyen ≥ 0,12 (estimations ponctuelles), sans perte dans le monde sans pont, et
   si aucun contrôle ci-dessous n'échoue ; **réfutée** sinon.
2. Monde sans pont : la vérité y est vide (précision nulle pour tous), la mesure est la précision placebo. Un écart (a) −
   (b) dont l'intervalle exclut 0, dans un sens ou l'autre, signale un artefact et fait échouer la thèse ; un écart
   négatif dont l'intervalle exclut 0 est la « perte » du brief. Ce contrôle ne peut échouer que par un artefact de
   mesure (fuite de la vérité, effet d'ordre, agrégation) : c'est sa puissance, pas plus.
3. Vérité inversée : (a) doit y perdre contre (b), intervalle de Δ_INV entièrement sous 0 ; sinon la thèse échoue
   (« elle ne mesure pas ce qu'elle prétend »).
4. Domaines mal séparés : l'hypothèse du noyau est violée ; si les seuils du point 1 sont atteints et que
   Δ_V_domaines ≥ Δ_M_bien, l'avantage ne vient pas du noyau et la thèse échoue. Étiquettes absentes et moyeux
   dominants touchent l'étage commun : rapportés, sans critère. Les contrôles 2 et 3 sont rapportés même quand le
   point 1 a déjà réfuté la thèse.
5. **Une autre forme retenue** si une forme (d1 ou d2) bat (b) de 12 points ou plus en M_bien et M_moyen, ne montre
   aucun écart à (b) dont l'intervalle exclut 0 dans le monde sans pont, et dépasse (a) en M_bien et en M_moyen ;
   s'il y en a deux, celle de plus forte précision moyenne sur ces deux mondes. Le monde inversé est rapporté pour
   elles (leur revendication ne porte pas sur l'éloignement).
6. Rien de ce qui précède ne change après lecture des résultats ; toute déviation est écrite comme telle dans le
   rapport. Les diagnostics et la sensibilité sont descriptifs.

## 6. Ce qui pourrait favoriser un bras par construction (écrit avant les résultats)

- Pour (a) : cosinus exacts sans bruit de projection ; mondes ordinaires calibrés pour que le vecteur de domaine code
  la proximité (0,54 / 0,28 / 0,03) ; vérité définie par l'éloignement.
- Contre (a) : q indépendante de la vérité (bruit dans le noyau) ; l'étage commun rejette déjà les paires d'un même
  domaine (la propriété démontrée par l'essai ne compte plus comme avantage).
- Pour (b) : les paires valides sont plus denses entre domaines proches (opérateurs de groupe) ; équilibrer les
  strates réduit mécaniquement les paires proches.
- Pour (d1) : les moyeux sont des pièges fréquents et les jumeaux des ponts rares. Pour (d2) : les greffes ont une
  signature d'import ; les jumeaux non.
