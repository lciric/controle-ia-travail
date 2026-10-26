# Trancher la recombinaison bisociative — un test qui pouvait échouer — v1

Rédigé le 2026-10-26T19:21:35Z (heure lue sur `date -u` dans la commande qui l'écrit). Lignée conv-audit, sous-agent neuf ;
processeur seul, bibliothèque standard de Python 3.13.17 (`python3 -I -B`). Préenregistrement scellé avant toute
exécution d'une méthode : `preenregistrement-trancher-recombinaison-v1.md` (`5335614b…`, scellé à 19:10:31 UTC ; run
lancé à 19:13:44 UTC). Régime exploratoire : rien d'opposable. Chiffres : `resultats-trancher-recombinaison-v1.json`
(`daaef112…`) sauf mention ; « points » = points de pourcentage ; crochets = intervalle à 95 % (2 000
rééchantillonnages appariés des mondes).

## Décision : **réfutée**

- La forme corrigée **perd** contre le tirage stratifié qui reçoit le même étage commun (même choix d'opérateur après
  tirage, même filtre) : **−4,8 points [−6,3 ; −3,3]** dans les mondes bien observés et **−2,2 [−3,4 ; −1,0]** dans les
  mondes moyennement observés (400 mondes chacun). Le seuil d'adoption était **+12** dans les deux.
- Elle ne fait pas mieux qu'un tirage uniforme parmi les mêmes paires valides : +0,4 [−1,0 ; +2,0] et −0,1
  [−1,3 ; +1,0]. Son noyau ne cible pas l'éloignement des paires : part de paires éloignées 0,532 contre 0,525 pour
  l'uniforme.
- Contrôles. Monde sans pont : aucun artefact, aucune perte (placebo −0,5 [−1,6 ; +0,5]). Monde inversé : elle
  perd (−3,5 [−4,5 ; −2,6]). Le contrôle passe à la lettre, mais **pas pour la raison attendue** (section 2.2).
- Aucune autre forme n'atteint le seuil. La meilleure mesurée est la **marche de Swanson par étiquette rare (d1)** :
  +3,5 [+2,0 ; +5,0] et +3,8 [+2,7 ; +4,9] sur le stratifié, +8,3 et +6,0 sur la forme corrigée. **Forme gardée par
  défaut : le tirage stratifié (b)**, plus simple et meilleur que (a). (d1) est la candidate à essayer ensuite ; la
  règle ne la retient pas.

## 1. Chiffres principaux

Précision = part de vrais ponts parmi les 12 paires tirées par monde (k = 4 paires × 3 générations), moyenne sur 400
mondes ; écart apparié au stratifié.

| Bras | bien : précision | écart à (b) | moyen : précision | écart à (b) |
|---|---|---|---|---|
| (a) forme corrigée | 0,155 [0,144 ; 0,168] | **−4,8 [−6,3 ; −3,3]** | 0,105 [0,096 ; 0,115] | **−2,2 [−3,4 ; −1,0]** |
| (b) tirage stratifié | 0,203 [0,192 ; 0,215] | — | 0,127 [0,118 ; 0,137] | — |
| (c) tirage uniforme | 0,151 [0,141 ; 0,162] | −5,2 [−6,5 ; −4,0] | 0,107 [0,098 ; 0,115] | −2,1 [−3,1 ; −0,9] |
| (d1) marche de Swanson | 0,239 [0,227 ; 0,249] | +3,5 [+2,0 ; +5,0] | 0,165 [0,155 ; 0,175] | +3,8 [+2,7 ; +4,9] |
| (d2) contraste d'import | 0,137 [0,121 ; 0,151] | −6,7 [−8,3 ; −5,0] | 0,093 [0,082 ; 0,105] | −3,4 [−4,8 ; −2,1] |
| (e) forme du rapport, γ minimal | 0,147 [0,136 ; 0,157] | −5,7 [−6,9 ; −4,4] | 0,094 [0,085 ; 0,102] | −3,4 [−4,3 ; −2,3] |
| diagnostic a_2dpp (déterminantal exact à 2) | 0,152 | −5,1 [−6,4 ; −3,8] | 0,108 | −1,9 [−3,0 ; −0,8] |
| diagnostic a_q1 (a avec q ≡ 1) | 0,163 | −4,0 [−5,4 ; −2,7] | 0,106 | −2,1 [−3,2 ; −1,0] |
| diagnostic b_eloigne (strates dissemblables d'abord) | 0,322 | +11,9 [+10,4 ; +13,4] | 0,193 | +6,6 [+5,5 ; +7,8] |
| diagnostic d1_inv (poids 1 / fréquence) | 0,257 | +5,3 [+3,8 ; +6,8] | 0,175 | +4,8 [+3,6 ; +6,0] |
| plafond (oracle) | 0,750 | — | 0,487 | — |

Rappel des ponts à budget fixé (bien / moyen) : (a) 0,161 / 0,108 ; (b) 0,214 / 0,131 ; (c) 0,157 / 0,109 ; (d1) 0,253 /
0,175 ; (d2) 0,131 / 0,089 ; (e) 0,148 / 0,094. Écart de rappel (a) − (b) : −5,3 [−6,8 ; −3,7] et −2,3 [−3,5 ; −1,1].

Pièges tirés, mondes bien observés (part des 12 paires) : opérateur-pont moyeu (a) 0,347, (b) 0,385, (c) 0,345, (d1)
0,122 ; homonyme 0,033 / 0,038 / 0,036 / 0,040 ; parasite 0,059 / 0,076 / 0,060 / 0,070 ; contraintes vraiment
incompatibles (le filtre en laisse passer) 0,271 / 0,262 / 0,274 / 0,251. Diversité : part de paires éloignées 0,532 /
0,654 / 0,525 / 0,446 ; strates distinctes par paire 0,707 / 0,998 / 0,765 / 0,736.

Par nombre de champs (bien), écart (a) − (b) : −3,5 [−6,0 ; −1,1] (2 champs), −5,8 [−8,2 ; −3,3] (3), −5,2 [−8,0 ; −2,4]
(4). La forme corrigée perd dans toutes les géométries.

## 2. Contrôles

### 2.1 Monde sans pont planté

La vérité y est vide : précision 0 pour tous. Mesure préenregistrée : la précision contre un placebo (6 paires valides
tirées au hasard, graine propre au monde, indépendante des bras). (a) 0,133, (b) 0,139, (c) 0,138, (d1) 0,140, (d2)
0,139. Écarts au stratifié : (a) −0,5 [−1,6 ; +0,5], (d1) +0,2 [−0,9 ; +1,2], (d2) +0,0 [−1,1 ; +1,1]. **Ni artefact, ni
perte.** Sur les 124 écarts placebo de toutes les conditions, 4 ont un intervalle qui exclut 0 (3,2 %), dont (a) − (b)
en domaines mal séparés (+1,2 [+0,2 ; +2,2]). L'espérance est nulle par construction et ce taux est celui du hasard.
Ce que les méthodes tirent quand il n'y a rien à trouver : paires éloignées (a) 0,458, (b) 0,586, (d1) 0,269 ; moyeux
0,446 / 0,532 / 0,187 ; contraintes incompatibles 0,346 / 0,333 / 0,338.

### 2.2 Monde à vérité inversée (les ponts relient des domaines proches)

(a) perd contre (b) : −3,5 [−4,5 ; −2,6]. Le contrôle préenregistré passe. Mais il passe pour une autre raison que
celle visée par le brief :
- (a) − (c) vaut +0,4 [−1,0 ; +2,0] dans le monde normal et −0,8 [−1,8 ; +0,2] dans le monde inversé. Aucun
  changement significatif : la forme corrigée ne préfère pas les domaines éloignés.
- L'écart (a) − (b) passe de −4,8 à −3,5 : il **remonte** quand on inverse la vérité. C'est le contraire de ce que
  ferait une méthode qui cible l'éloignement.
- Le diagnostic qui cible vraiment l'éloignement (b_eloigne) passe de +11,9 à **−11,6 [−12,5 ; −10,8]** (précision
  0,001) : c'est ce que le contrôle devait détecter.
- La perte de (a) dans le monde inversé vient de l'avantage du stratifié, présent dans les deux mondes (section 3), et
  non d'une préférence pour l'éloignement.

### 2.3 Hypothèses de la forme corrigée violées

- **Domaines mal séparés** (cosinus 0,44 / 0,41 / 0,33 au lieu de 0,54 / 0,28 / 0,03) : (a) − (b) = −4,5 [−6,0 ; −3,0],
  comme dans le monde normal. Le critère d'échec préenregistré ne s'applique pas (seuils non atteints). La forme
  corrigée ne dépend pas du vecteur de domaine, parce qu'elle ne s'en servait déjà pas pour les paires.
- **Étiquettes d'opérateur absentes** (étage commun réduit à « domaines différents + filtre ») : tous au taux de base
  (≈ 0,025) : (a) 0,028, (b) 0,024, (c) 0,029 ; (a) − (b) +0,4 [−0,3 ; +1,1]. (d1), (d2) et (e) ne s'appliquent pas
  (elles reposent sur les étiquettes).
- **Moyeux dominants** (deux moyeux à 0,6) : (a) 0,044, (b) 0,040, (c) 0,034 ; (a) − (b) +0,4 [−0,4 ; +1,1]. La marche
  de Swanson tient : 0,210, soit **+17,0 [+15,9 ; +18,1]** sur le stratifié. Éviter les moyeux est le seul mécanisme qui
  survit à cette violation.
- **Mal observé** : (a) 0,060, (b) 0,066, (c) 0,067 ; (a) − (b) −0,6 [−1,5 ; +0,3] ; (d1) +3,7 [+2,7 ; +4,6].

## 3. Pourquoi la forme corrigée vaut un tirage uniforme

Audit fait après lecture des résultats, descriptif ; aucune règle n'en dépend (`audit-mecanisme-v1.json`,
`f28a2238…`, 400 mondes bien observés, graines du run).
- L'ordre glouton suit la qualité : corrélation de rang 0,977 entre l'ordre et q. Ici q (la pertinence) est
  indépendante de la vérité, comme dans l'essai. q² varie d'un facteur 9 ; la répulsion entre domaines proches est
  S = cos² = 0,093 (éloignés 0,001 ; même domaine 0,309).
- Avec q ≡ 1, le noyau diversifie bien les **articles** : 7,8 domaines distincts parmi les 8 premiers, contre 6,1
  avec q. Il ne diversifie pas les **paires** : part de paires proches parmi ses 12 paires, 0,452 (q ≡ 1) et 0,449 (q),
  pour 0,449 dans l'ensemble des paires valides. Un ensemble d'articles divers contient toutes les paires de domaines,
  proches comprises. Or les paires proches sont les plus denses en paires valides (opérateurs partagés dans un champ).
  La forme corrigée les tire donc dans leur proportion, comme l'uniforme.
- Le stratifié gagne parce qu'il équilibre les **paires de domaines** : il donne le même poids à chaque strate, ce qui
  allège les strates denses en partages de fond. Part de paires proches : 0,329 contre 0,451 pour l'uniforme.
- C'est structurel, pas un artefact du monde. Pour une paire, le déterminant vaut q_i² q_j² ((1 + γ)² − cos⁴). À
  cos = 0,28 (domaines proches), la pénalité est de 0,6 %. Pour préférer les paires éloignées, il faudrait des domaines
  proches à cos ≳ 0,8, c'est-à-dire presque confondus. Le processus déterminantal exact à 2 éléments (a_2dpp) le
  confirme : −5,1 et −1,9, comme (a).

## 4. Les autres formes

- **(d1) Marche de Swanson.** Provenance : caste 3 (Opus) du rapport de l'essaim, « marche aléatoire sur graphe biparti
  Concepts × Articles pondérée par IDF des concepts-ponts ». C'est le schéma A–B–C de la découverte fondée sur la
  littérature (Swanson, 1986 ; de mémoire, non vérifié). Adaptation : les concepts sont les étiquettes d'opérateur
  observées, pas les mots. Dans ces mondes, les mots de domaine sont les plus rares mais ne franchissent jamais un
  domaine. C'est la meilleure forme mesurée, et ses gains ont deux sources :
  - elle évite les moyeux : pièges moyeux 0,122 contre 0,385 ;
  - elle trouve les jumeaux : rappel 0,434 contre 0,269 pour (b) et 0,180 pour (a). Sur les greffes, elle fait jeu égal
    (0,188 contre 0,193).
  Elle ne cible pas l'éloignement (paires éloignées 0,446). Elle tient dans le monde inversé (+4,6 [+3,4 ; +5,8]) et
  domine quand les moyeux dominent (+17,0). Son avantage disparaît quand les moyeux sont rares (sensibilité moyeux à
  0,10 : −0,2 [−1,3 ; +0,9]) et grandit à 0,50 (+10,1 [+8,9 ; +11,2]). Elle reste sous le seuil dans les mondes de
  décision.
- **(d2) Appariement par structure de cooccurrences étiquette × domaine.** Je l'ai construite à partir de l'exemple du
  brief. Une étiquette courante dans un domaine et rare dans l'autre signale un import ; le principe est voisin des
  « combinaisons atypiques » de la scientométrie (Uzzi et al., 2013 ; de mémoire, non vérifié). C'est un échec :
  −6,7 et −3,4. Elle ne trouve pas mieux les greffes (0,172 contre 0,193), manque les jumeaux par construction
  (0,013) et se concentre sur peu de strates (0,454). Avec 5 articles par domaine, la fréquence par domaine est trop
  bruitée.
- **(e) Forme du rapport de Gemini, pour mémoire.** Noyau q_i q_j ⟨o_i,o_j⟩² (1 − cos²), Sinkhorn-Knopp 5
  itérations, puis γ minimal pour la rendre semi-définie positive (médiane 0,94 ; 0,76 avec moyeux dominants).
  Elle tourne dans tous les mondes étiquetés. Elle est un peu sous l'uniforme (0,147 contre 0,151) et perd contre le
  stratifié (−5,7). C'est l'effet décrit par l'essai : une fois réparée, elle repousse les paires qu'elle visait.
- **Ce que vaudrait l'idée bisociative elle-même**, avec un a priori d'éloignement grossier (diagnostic b_eloigne,
  qui sert d'abord les strates dissemblables) : +11,9 [+10,4 ; +13,4] (bien), +6,6 [+5,5 ; +7,8] (moyen), +10,2
  (domaines mal séparés), −11,6 (inversé). Par nombre de champs (bien), le gain est de +19,4 (2 champs), +11,0 (3) et
  +3,9 (4). La valeur de l'éloignement dépend de la part de paires de domaines proches et du bruit des étiquettes. Même
  cet a priori idéalisé n'atteint pas +12 dans les deux mondes de décision. Il n'est pas éligible (diagnostic).

## 5. Méthode (détail : préenregistrement)

- **Mondes** (`monde_v1.py`, `conditions_v1.py`) :
  - 8 domaines × 5 articles, répartis en 2, 3 ou 4 champs tirés par monde ;
  - 3 opérateurs latents par groupe, avec un mot de surface différent dans chaque domaine ; opérateurs propres à un
    article ; un moyeu présent dans 25 % des articles ;
  - 3 greffes et 3 jumeaux plantés par monde. Vérité : champs différents, opérateur latent non moyeu commun,
    contraintes vraies compatibles. Soit 12,3 vraies paires par monde, dont 9,5 valides en « bien ».
  - Observations : vecteur de domaine (fréquences brutes des mots hors lexique, cosinus exacts ; validés à 0,54 /
    0,28 / 0,03 avant toute méthode) ; étiquette de domaine juste à 0,95 ; lexique d'opérateurs à trois niveaux
    (couverture 0,90 / 0,70 / 0,45, parasites 0,05 / 0,15 / 0,30, homonymes 0,05 / 0,10 / 0,20) ; contraintes par le
    canal de l'essai b4 (rappel du filtre mesuré 0,57 à 0,60, rejets à tort 4 à 5 %).
- **Budget et étage commun** : k = 4 paires par génération, 3 générations, mêmes 40 candidats, aucune paire retirée
  deux fois. Toutes les sorties sont des paires valides : domaines observés différents, étiquette partagée (opérateur
  retenu après tirage = la plus rare), filtre passé.
- **Bras** :
  - (a) correctif c5 de l'essai étendu à k paires : ordre glouton du déterminant maximal par Cholesky incrémentale,
    vérifié contre un glouton par déterminants explicites (50 cas sur 50) ; paires rangées par (rang maximal, somme
    des rangs) ;
  - (b) tour aléatoire des strates (paires de domaines observés), puis une paire valide au hasard dans la strate ;
  - (c) tirage uniforme ;
  - (d1), (d2) et (e) : section 4 ; γ minimal vérifié contre des valeurs propres de Jacobi (écart 4·10⁻⁹).
- **Graines** :
  - monde : `random.Random(20261026000000 + 100000 × identifiant + indice)` ;
  - bras : `random.Random(f"{graine}-{bras}")` ;
  - placebo : `random.Random(f"placebo-{graine}")` ;
  - rééchantillonnage : `random.Random(20261026)`.
  Run complet en 93 s ; relance : `python3 -I -B trancher_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)"`.

## 6. Ce que ce test ne dit pas

- **Il porte sur le tirage**, c'est-à-dire sur les paires envoyées à la fusion. Il ne dit rien de la qualité des
  hypothèses fusionnées par un modèle. Une fusion pourrait tirer parti de paires que la vérité synthétique ne compte
  pas, ou gâcher de vrais ponts.
- **Un monde synthétique encode mes hypothèses**, notamment trois :
  - les ponts sont des partages d'opérateur entre champs ;
  - le partage de fond est concentré dans les champs, ce qui favorise le stratifié, comme je l'avais écrit avant les
    résultats (préenregistrement, section 6) ;
  - les moyeux sont présents à 25 %.
  Si, dans la littérature réelle, le partage d'opérateurs n'est pas plus dense entre domaines proches, l'avantage du
  stratifié sur l'uniforme fond. La forme corrigée resterait pourtant au niveau de l'uniforme, puisque son noyau
  n'agit pas sur les paires (section 3).
- **Il ne dit pas que l'idée bisociative est fausse.** Un a priori d'éloignement grossier gagne +11,9 et +6,6 ici. Il
  dit que le noyau corrigé ne la met pas en œuvre.
- **Ce qui n'a pas été testé** :
  - des noyaux plus tranchants (exponentielle du cosinus), ou un noyau sur les paires de domaines (c'est, à peu près,
    le stratifié pondéré) ;
  - une pertinence q corrélée aux ponts ;
  - des viviers plus grands (ici n = 40, soit 5 articles par domaine) ;
  - la dynamique réelle des survivants d'une génération à l'autre.
- **Comment j'ai essayé d'éviter de favoriser une forme par construction** :
  - préenregistrement scellé avant toute méthode, avec la liste de ce qui pouvait favoriser chaque bras ;
  - mondes ordinaires calibrés pour **satisfaire** l'hypothèse de la forme corrigée (vecteur de domaine qui code la
    proximité), vérifiés sur des graines de validation distinctes ;
  - géométrie des champs tirée par monde ;
  - deux mécanismes de pont, pour ne servir ni les formes « rareté » ni les formes « import » ;
  - articles mélangés (aucun avantage d'indice) ; étage commun identique pour tous ;
  - cosinus exacts, c'est-à-dire la meilleure version possible du vecteur de domaine ;
  - deux mises en œuvre de (a) et une ablation de q, qui concordent.
  L'instrument sait enregistrer de grands gains : plafond 0,750, +11,9 pour le diagnostic d'éloignement, +17,0 pour
  (d1) avec moyeux dominants. La réfutation ne vient donc pas d'un monde où rien ne peut gagner.

## 7. Contrôles que je crois mal posés (dit à part ; la décision ne change pas)

1. **Monde sans pont.** Avec la vérité définie par les ponts, la précision y vaut 0 pour toutes les méthodes : le
   contrôle est vide. Je l'ai mis en œuvre par un placebo. Celui-ci ne peut échouer que par un artefact de mesure
   (fuite, effet d'ordre, agrégation). Pour savoir si un avantage vient des ponts, il vaut mieux décomposer l'écart du
   monde normal en une part « éloignement » et une part « opérateur » que de demander l'égalité.
2. **Monde inversé.** « La forme corrigée doit y perdre » est satisfait dès que le comparateur gagne dans les deux
   mondes, ce qui est le cas ici. Il faudrait exiger que l'écart **baisse** quand on inverse la vérité (Δ_inversé −
   Δ_normal < 0, intervalle sous 0) ou comparer au tirage uniforme muni du même étage. Ici, l'écart remonte de 1,3
   point ; pour le diagnostic d'éloignement, il chute de 23,5.
3. **Seuil absolu de 12 points.** À des précisions de 10 à 20 %, +12 points signifie ×1,6 à ×2,2 : même l'a priori
   d'éloignement idéalisé ne l'atteint pas dans les deux mondes. Un seuil relatif, ou un rapport gain / coût de la
   machinerie, comparerait mieux les formes. La forme corrigée perd ici en absolu comme en relatif.

## 8. Étape suivante proposée (non exécutée) : rétrodiction sur littérature réelle

- **Principe.** On fige une date T. Avec la seule information antérieure à T, on construit des viviers d'articles de
  champs différents. Chaque bras tire ses paires avec le même budget et le même étage commun. Une paire est un « pont
  réalisé » si les deux littératures étaient disjointes avant T et deviennent reliées après T, dans une fenêtre fixée
  d'avance. Disjointes : ni références communes, ni cocitation, ni comention de leurs termes clés. Reliées : un
  article postérieur les cite ensemble ou combine leurs termes clés, à la manière des cas de Swanson. On garde les
  mêmes mesures, la même règle et les mêmes contrôles : dates tirées au hasard ou liens mélangés pour le monde sans
  pont, liens entre champs proches pour le monde inversé.
- **Données nécessaires** :
  - un corpus bibliographique daté, avec résumés, rattachement disciplinaire et références (par exemple l'instantané
    ouvert d'OpenAlex : dates, thèmes, résumés, références ; ou les métadonnées d'arXiv : catégories, dates, résumés,
    plus une source de citations) ;
  - une taxonomie à deux niveaux (champ, domaine) figée à T, pour dire « proche » et « éloigné » ;
  - un lexique d'opérateurs (méthodes, structures mathématiques) figé avant T, et sa couverture mesurée sur un
    échantillon annoté à la main. C'est elle qui situe le réel parmi les trois niveaux d'observation ;
  - un lexique de marqueurs de contraintes, avec son rappel mesuré ;
  - la définition du lien après T et son taux de base, sans doute très faible : il faudra des viviers assez grands ou un
    échantillonnage stratifié des paires candidates ;
  - les cas historiques de Swanson, comme vérification qualitative seulement : leur sélection est biaisée.
- **Garde contre les fuites** : vecteurs, lexiques et fréquences calculés sur le texte antérieur à T ; aucune
  information de citation postérieure à T dans les entrées.
- **Coût** : processeur, sans appel de modèle pour le tirage. Le téléchargement du corpus est un accès réseau : il
  attend le GO de Lazar. La qualité des fusions par un modèle reste une expérience distincte.

## 9. Réserves et écarts

- Aucune contre-lecture par un sous-agent neuf (R2) : le brief interdit les sous-agents. À faire avant tout usage.
- J'ai changé la pondération du vecteur de domaine (TF-IDF → fréquences brutes) **avant toute méthode**. Avec le
  TF-IDF, domaines proches et éloignés étaient presque indiscernables (0,11 contre 0,009), donc l'hypothèse de la
  forme corrigée n'était pas satisfaite. Ce choix la **favorise**.
- R12 : la première sortie de validation (TF-IDF) a été écrasée par la seconde, sous le même nom. Ses chiffres
  (cosinus 0,48 / 0,11 / 0,009) viennent de la console. La première ligne de `calibrer_vocabulaire_v1.py` la reproduit.
- (d1), (d2) et (e) ne s'appliquent pas au monde sans étiquettes. Le préenregistrement ne le disait pas ; cela découle
  de leur définition.
- L'audit du mécanisme (section 3) est postérieur aux résultats et descriptif.
- Les provenances bibliographiques (Swanson ; Uzzi et al.) sont citées de mémoire, sans chiffre (R7).

## 10. Fichiers (sous `sortie/`) et empreintes

| Fichier | Rôle | SHA-256 |
|---|---|---|
| `preenregistrement-trancher-recombinaison-v1.md` | règles gelées avant toute méthode | `5335614b2b8b38deb50408c4755401242e5a8436f82b1f9e8be48e57f9dd2985` |
| `resultats-trancher-recombinaison-v1.json` | agrégats, intervalles, décision, manifeste | `daaef112ce5a402bda785c1206db222c8f94793afaf7c0ced910467b4bf4a624` |
| `mondes-trancher-recombinaison-v1.jsonl` | mesures brutes par monde et par bras (4 000 mondes) | `9677cc3ca31d762234de79e07a083d907f30839e6a9dd169246894542e8ad1d3` |
| `validation-generateur-v1.json` | propriétés des mondes, graines de validation | `41e475982974be3ae631dcfa6092eb239887e053a844ec9a95b7f45ffa86d3b3` |
| `audit-mecanisme-v1.json` | audit de la section 3 | `f28a2238223a28e2877e9de4559e7cd120fbb8987dedf21f70c6efea3b8e92e0` |
| `monde_v1.py` | générateur | `af907b1d5d779dfc1c4353503d31059f20d031a4b4324fea3ca775ad6a6bc98c` |
| `conditions_v1.py` | conditions, graines | `9246ecc6a4a71f8a701600a0c55c549d622423496a436f2f708b0d9ffe53af35` |
| `methodes_v1.py` | bras | `2f7a8b1192a79d5bed64fb48f9a5db6f1df6bf86e3a2296eafca75493f2790dd` |
| `mesures_v1.py` | mesures, rééchantillonnage | `0a1e3c3806ae892a526fa6a21bcf07217e6f41118244a7cdd01a2f8ad9f8a82e` |
| `trancher_v1.py` | lanceur et règle de décision | `781335dda51954f5d4ac1ab25ce0ce850a421d8c0c2346ae8284fddc8a6609e0` |
| `tests_v1.py` | tests des instruments | `bf12486a5936ad50cdfe7d6407477cdb99442f2c9ebf2d9f64da6a288b70c037` |
| `valider_generateur_v1.py` | validation du générateur | `c2aef23e4d48aa6b12231db6d4f1cdcf3fbc548bfe178d4d61f53c128fa5978f` |
| `calibrer_vocabulaire_v1.py` | calibrage du vecteur de domaine | `a0aec03e885857ce202795dd18bada3cb3a748afc268d95917796f1205be6c8d` |
| `audit_mecanisme_v1.py` | audit | `5762c7a4b0f9404171329139fc95480efb00db19ef311b5c087a996adc6497a8` |
| `horodater_v1.py` | horodatage par `date -u` | `79ea1845209a8dc0633b55d334ffbf4d50058333c342e0725d6163252731e2b6` |

Chaque fichier a son compagnon `.sha256` ; celui de ce rapport est `trancher-recombinaison-v1.md.sha256`.
