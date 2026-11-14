# Synthèse du tour du collisionneur sur les bassins d'idées étroits et profonds, consultations à part et remue-méninges de la mère compris — v1

- **Auteur** : sous-agent neuf, lecteur (Claude Fable 5.2, `claude-fable-5-2`), sur la consigne scellée
  `…/consignes-mere-2026-11-12-2019-v1/consigne-lecteur-recoupement-bassins-etroits-v1.md` (`69da6f54e4ee3420…`). Je n'ai écrit
  ni la question, ni les faits, ni aucune cellule, ni le remue-méninges. Aucun appel de modèle, aucun réseau, aucune dépense,
  aucune opération git. **Réserve de lignée** : je suis de la famille des espèces A et B et du modèle de la mère ; une
  préférence pour leurs formulations est possible, à contre-lire si cette synthèse fonde une décision.
- **Ordre tenu** : l'inventaire `inventaire-methodes-v1.md` (`00bb87b48a5a093c…`) a été scellé à 14:43:50 UTC ; le
  remue-méninges de la mère (`docs/notes/bassins-etroits-idees-v1/remue-meninges-mere-v1.md`, `f3c46703…`) n'a été ouvert
  qu'ensuite (14:43:54 UTC), puis les témoins v2 (`f1ddcef9…`) et la conception à trois générations v2 (`b6c7035e…`). Heures
  relevées par `date -u`, le 13 novembre 2026.
- **Pièces** : celles de l'inventaire (faits `d19b5400…`, question `935f4e5b…`, quinze cellules, trois consultations à part,
  note de dépense `230c8b13…`), plus les trois ci-dessus ; en contexte, la synthèse du premier tour (`4f99077b…`) et la
  lecture des deux articles voisins. Références : [A-T1] … [E-T3] pour les cellules ; [Argon-à-part], [Astra-à-part],
  [Kimi-à-part] ; [Mère] pour le remue-méninges, dont je cite les méthodes par « mère-A1 », « mère-D2 », etc. Les codes
  V1 … P2 sont ceux de l'inventaire.
- **Conventions** : ce que j'ajoute de moi porte **(synthèse)**. Aucun chiffre des cellules n'est un résultat : ils sont
  **illustratifs**. Rien n'a été éprouvé : « survivante » veut dire « a survécu à la critique écrite ».

## Verdict en dix lignes

1. **Rien n'est mesuré.** Le tour rend des conceptions critiquées, pas des résultats ; aucune méthode n'a montré qu'elle
   pousse un proposeur vers un bassin étroit.
2. **Il n'y a pas de moteur à pousser** ([A-T1], non contesté) : la probabilité qu'un bassin reçoive une proposition en k
   appels est 1 − (1 − p)^k ; rien en aval des proposeurs ne l'augmente. Trois leviers seulement : la vue, les proposeurs,
   ne pas perdre ce qui est proposé.
3. **Un gain n'existe que sous une structure nommable sans l'oracle** (huit textes sur huit, et [Mère]) : sans elle, aucune
   méthode ne bat le tirage indépendant.
4. **Côté vue, la sophistication s'est réduite à une liste** : décomposition de Möbius, graphe de dépendance, complexe
   simplicial, table de Walsh reviennent tous, après critique, à « la liste des paires de traits que l'archive ne croise
   pas » (V2), habillée ou non d'un plan (V3), de moments (V5) ou de contrastes compilables (I1).
5. **Côté juge, les deux méthodes que la mère plaçait au deuxième rang sont les plus touchées** : la valeur e par strates
   n'aide pas une carte déjà localisée (identité démontrée par [D-T2] et [E-T2], concédée en [C-T3]) ; les poids de
   multiplicité selon la nouveauté sont une prime de nouveauté sous un autre nom ([C-T3] les abandonne).
6. **Ce qui survit côté juge** : l'arrêt optionnel (J1), valide par théorème sous réserve d'une preuve pour notre nul
   composite ; il sert la survie d'une idée étroite, pas sa découverte.
7. **L'inconnue centrale est empirique et bon marché à lever** : la loi des propositions d'un modèle bouge-t-elle quand on
   lui montre la liste ? Aucun fait ne le dit ; les cinq espèces le relèvent.
8. **Le danger commun du premier tour reste entier** : pousser vers le conditionnel, c'est pousser vers la classe que le nul
   ne couvre pas. Préalable convergent : un banc sans proposeur qui certifie la garde **et** la puissance.
9. **Compte** : 31 lignes ; 15 survivantes (11 pleines, 4 suspendues) ; 8 retirées ou écartées ; 8 non critiquées (sept
   propres aux consultations à part, une apparue au dernier tour). Le remue-méninges de la mère ajoute six idées que
   personne d'autre n'a, et un cadre de mesure.
10. **Faiblesses** : la question désignait la composante conditionnelle, et quatre espèces sur cinq ont proposé l'outil
    taillé pour elle ; le dernier tour n'a pas été critiqué (j'y trouve une erreur de plus, par calcul) ; la profondeur
    au sens des chaînes n'a presque pas été traitée.

## 1. Convergences et divergences

### Convergences

- **Le remède extérieur est déjà en place** : l'organisme appelle en session neuve sans historique ; la remise à zéro du
  contexte n'est pas une intervention neuve ici ([A-T1], [C-T1], [E-T1], [Argon-à-part], [Astra-à-part]).
- **Deux étroitesses, à mesurer séparément** : petite probabilité de proposition, et effet confiné ou invisible en moyenne
  ([A-T1], [E-T1], [Astra-à-part], [Mère] §0.2). La première appelle la vue, la seconde le juge et le regroupement.
- **La largeur sous la loi des modèles n'est pas un bouton du générateur** : elle s'estime sur des mondes d'étalonnage, par
  famille de paramètres, jamais en retenant les graines où le témoin a échoué ([D-T1], [E-T1], [A-T2], [Astra-à-part],
  [Kimi-à-part]). Cela corrige mère-E2, qui parlait de « régler la largeur ».
- **Ordre des dépenses** : banc hors ligne sans proposeur ; puis une seule génération au-dessus d'une archive gelée, un
  seul facteur changé, juge et regroupement identiques dans tous les bras ; la course à plusieurs générations ensuite
  ([A-T3], [C-T3], [D-T3], [E-T3], [Astra-à-part], [Kimi-à-part]).
- **Témoins** : texte neutre de même longueur ; énumération simple ; tirage sans remise des mêmes focalisations ; budget
  total de jetons égal ; énumérateur mécanique sans modèle ([B-T2], [D-T1], [E-T1], [Mère] B2).
- **Trois étages de lecture** par l'oracle (brutes, représentants, retenues) pour savoir où une idée se perd.
- **Aucune des huit sources ne propose de servir un score de nouveauté à un agent.**

### Divergences

- **Le premier essai avec proposeurs.** [A-T3] : un monde **sans** interaction, pour lire d'abord la garde et le levier
  (vue brute, liste, placebo). [B-T3] : un pilote de cinq bras sur un monde à composante conditionnelle. [C-T3] : trois bras
  sur cent mondes. [D-T3] : un criblage du mécanisme sur les cartes brutes. [E-T3] : aucun appel avant un certificat fini
  de garde et de puissance, puis contrastes contre aide syntaxique.
- **Métrique principale** : propositions brutes ([A-T3], [B-T3], [D-T3] pour le mécanisme) ou retenues ([C-T3], [E-T3],
  [Astra-à-part], [Kimi-à-part]).
- **Une hausse des cartes conditionnelles sous monde nul est-elle une alerte de garde ?** Oui pour [B-T2] ; non pour [D-T3]
  et [E-T3] (une carte conditionnelle peut représenter une loi additive ; le contenu peut changer à forme constante) ;
  [A-T3] se range au non et ne garde ce compte qu'à titre descriptif.
- **Le « monde à condition verrouillée »** (parent sans effet marginal) : contrôle nul pour [A-T2] ; refusé comme tel par
  [D-T3] et [E-T3] (une interaction vraie sans parent n'est pas une fausse découverte).
- **La valeur e par strates.** [C-T1] et [Argon-à-part] annoncent qu'elle supprime la dilution ; [D-T2] et [E-T2] montrent
  que non ; [C-T3] concède. **(synthèse)** La consultation à part du même modèle, sans contradicteur, maintient l'annonce :
  c'est la mesure de ce que la collision apporte.
- **Les poids de multiplicité.** [C-T3] abandonne ; [Argon-à-part] et [Mère] (D2) les défendent par la validité formelle.
- **Un bras combiné ou un facteur à la fois.** [C-T1] et [Argon-à-part] combinent trois méthodes ; le tour III.3 et
  [Astra-à-part] exigent un facteur par bras.

## 2. Tableau de recoupement : méthodes × sources

Légende : **P** propose ; **P→R** propose puis retire ; **P→M** propose puis maintient corrigée ; **P→S** propose puis
suspend ou diffère ; **=** l'adopte au tour III.3 ; **t** l'emploie comme témoin ; **c** la critique ; **≈** porte une idée
parente (dite en note) ; **·** rien. Colonnes A à E : espèces du collisionneur ; « Ar », « As », « Ki » : consultations à
part ; « Mère » : remue-méninges.

| code | méthode | A | B | C | D | E | Ar | As | Ki | Mère | sort |
|---|---|---|---|---|---|---|---|---|---|---|---|
| V1 | Décomposition orthogonale de l'archive (Möbius) | P→R | c | c | c | c | · | · | · | · | retirée |
| V2 | Liste des paires de traits non croisées par l'archive | = | P→M | P→t | t | c | ≈ | · | · | ≈ B1 | **survivante pleine** |
| V3 | Plan combinatoire des focalisations | c | c | P→M | P→M | c | P | P | P | ≈ B2 | **survivante pleine** |
| V4 | Code couvrant sur les sous-ensembles de traits | · | P→R | · | c | c | · | · | · | · | retirée |
| V5 | Dictionnaire de directions par moments orthogonaux | c | c | c | P→M | c | · | · | · | · | **survivante pleine** |
| V6 | Tirage déterminantal d'un lot de vues | c | P→M | c | c | c | · | P | · | ≈ A2 | **survivante pleine**, dernière servie |
| V7 | Plan sur des vues équivalentes | c | c | c | c | P→S | · | ≈ | · | · | survivante suspendue |
| V8 | Processus gaussien sur l'espace des lois | · | P→R | c | c | c | · | · | · | · | retirée |
| V9 | Homologie de l'archive | · | P→R | P→R | c | c | · | · | · | · | retirée |
| V10 | Focalisations tirées des résidus (données publiques avec issues) | · | · | · | · | · | · | · | P | ≈ B3 | non critiquée |
| V11 | Balayage multi-échelle des résidus | · | · | · | · | · | · | · | P | ≈ B3 | non critiquée |
| V12 | Méthodes à signal servi (rappel) | écarte | · | · | · | · | écarte | · | · | ≈ A1, C1 | écartées |
| I1 | Contrastes orthogonaux compilables | c | c | c | c | P→M | · | · | · | · | **survivante pleine** |
| I2 | Opérateur d'expansion (l'orchestrateur fabrique la carte croisée) | · | c | P→R | c | c | · | · | · | ≈ B2 | retirée |
| I3 | Carte de déviation dans le groupe des log-cotes | · | · | · | · | · | P | · | · | · | non critiquée |
| C1 | Synthèse typée de prolongements | c | c | c | c | P→S | · | · | · | · | survivante suspendue |
| C2 | Arbres de continuation sans récompense intermédiaire | · | · | · | · | · | · | P | · | · | non critiquée |
| C3 | Fractionnement à plusieurs niveaux sur un graphe de prérequis | · | · | · | · | · | · | · | P | ≈ B1 | non critiquée |
| G1 | Jeu public d'instances construit par plan | P→M | · | · | · | c | · | · | · | · | **survivante pleine** |
| G2 | Représentant par couverture dirigée de strates | P→M | c | c | c | c | · | · | · | ≈ A2 | **survivante pleine**, affaiblie |
| G3 | Pivotage de Cholesky pour regrouper et représenter | · | c | P→M | c | c | · | · | · | ≈ A2 | survivante suspendue |
| G4 | Divergences localisées par strates | c | c | = | P→M | c | · | · | · | · | **survivante pleine** (descriptive) |
| J1 | Processus de valeurs e à arrêt optionnel | P→M | c | c | c | c | · | · | · | · | **survivante pleine** |
| J2 | Tirages du juge stratifiés selon une loi choisie | P→R | c | c | c | c | · | · | · | ≈ D1 | retirée |
| J3 | Valeur e à plusieurs échelles (mélange par cellules) | c | c | P→M | c | c | · | · | · | ≈ D1 | **survivante pleine**, très restreinte |
| J4 | Martingale à pari localisé, nul ponctuel | · | · | · | · | · | P | · | · | · | non critiquée |
| J5 | Poids de multiplicité selon la géométrie des groupes | c | c | P→R | c | c | P | · | · | P (D2) | retirée dans la course |
| J6 | Valeur e par supremum sur un nul composite explicite | c | c | c | P→M | P→M | · | P | P | · | **survivante pleine** (garde candidate) |
| J7 | Filtre avant le juge contre les recombinaisons par morceaux | · | · | P | · | · | · | · | · | · | non critiquée (dernier tour) |
| P1 | Portefeuille de proposeurs sous budget | P→S | c | · | c | c | · | · | · | ≈ C1 | survivante suspendue |
| P2 | Meilleur couple « proposeur × vue », hors ligne | · | · | · | · | · | · | · | P | ≈ C1 | non critiquée |
| — | mère-A1 : tempérer (probabilités déclarées par le proposeur, température) | · | · | · | · | · | · | · | · | P | mère seule, non critiquée |
| — | mère-A3 : remplir les bassins visités (métadynamique, histogramme plat), missions qui les excluent | · | · | · | · | · | · | · | · | P | mère seule, non critiquée |
| — | mère-A4 : qualité-diversité (archive en grille, une élite par cellule) | · | · | · | · | · | · | · | · | P | mère seule, non critiquée |
| — | mère-C2 : sélection douce (Boltzmann, une place tirée au sort) | · | · | · | · | · | · | · | · | P | mère seule, non critiquée |
| — | mère-C3 : îles et échange de répliques (archive servie minimale ou complète) | · | · | · | · | · | · | · | · | P | mère seule, non critiquée |
| — | mère-E1 : masse manquante (Good–Turing, Chao) | · | · | · | · | · | · | · | · | P | mère seule, non critiquée |
| — | mère-E2 : courbe dose-réponse (largeur et profondeur plantées) | ≈ | ≈ | ≈ | ≈ | ≈ | ≈ | ≈ | ≈ | P | cadre d'expérience commun, corrigé (§1) |

Notes sur les « ≈ » : V2 chez [Argon-à-part] : il calcule les paires d'interaction nulle dans l'archive pour choisir ses
sondes ; chez [Mère] B1 : missions « qu'est-ce qui ne vaut que sous X ? ». V3 chez [Mère] B2 : tableaux orthogonaux, mais pour
un énumérateur mécanique. V6, G2, G3 chez [Mère] A2 : sélection répulsive parmi les **propositions** (déterminantale ou
sous-modulaire), que la course a réduite à un départage (G2) ou à un pivotage (G3). V7 chez [Astra-à-part] : une permutation
commune des noms de traits, employée comme contrôle. V10 et V11 chez [Mère] B3 : proposeur mécanique de sous-groupes ; même
prérequis non établi (des données avec issues dans la vue). P1 et P2 chez [Mère] C1 : bandits visant le maximum, sur l'oracle
des mondes de développement. I2 chez [Mère] B2 : recombinaison mécanique par programme, mais comme témoin.

## 3. Ce que les consultations à part apportent que le collisionneur n'a pas, et l'inverse

**Elles apportent** (toutes non critiquées) :

- **Une interface en écarts** (I3, [Argon-à-part]) : le proposeur n'écrit que la correction à la loi de base ; l'idée
  attaque le coût de réécrire l'acquis, que personne d'autre ne nomme. Elle déplace la question de la garde vers
  l'enveloppe log-linéaire de l'archive.
- **Un nul ponctuel** (J4, [Argon-à-part]) : l'écart d'une carte est pris, en chaque point, contre l'enveloppe convexe des
  lois d'archive ; une carte qui recolle deux lois connues par morceaux obtient une valeur e bloquée à 1. C'est la seule
  réponse constructive au danger commun, avec J7. **(synthèse)** Elle se paie : toute découverte dont la prédiction reste,
  en chaque point, entre celles de deux lois archivées est absorbée de la même façon, et cette zone grandit avec l'archive ;
  c'est le cas « le nul absorbe l'alternative » de [E-T1], [A-T2], [D-T3]. À porter au banc avec un contrôle positif.
- **Deux dessins en plusieurs pas** : arbres de continuation où tous les préfixes sont traités de même (C2,
  [Astra-à-part]), avec la comparaison exacte des taux d'échec par unité de coût ; fractionnement à plusieurs niveaux sur
  la frontière de l'archive (C3, [Kimi-à-part]). Ce sont les seules propositions qui visent la **profondeur en chaîne**.
- **Deux inégalités démontrées** ([Astra-à-part]) : un plan équilibré ne fait pas moins bien que des blocs tirés
  indépendamment, (1 − s)^(Mp) ≤ (1 − ps)^M ; un tirage déterminantal de projection ne fait pas moins bien que le tirage
  indépendant de mêmes marges. **(synthèse)** Je les ai revérifiées à la main (concavité du logarithme ; inégalité
  arithmético-géométrique sur les valeurs propres) ; elles supposent l'indépendance des réponses et ne garantissent pas un
  gain notable.
- **Un témoin plus propre** ([Astra-à-part]) : permuter au hasard les noms de traits du plan structuré donne à chaque bloc
  la loi marginale du témoin ; la différence porte alors sur la coordination du lot.
- **Une pièce nouvelle** ([Kimi-à-part]) : des données publiques d'exploration **avec issues**, distinctes des tirages du
  juge, sur lesquelles calculer des résidus (V10, V11). **(synthèse)** C'est un changement de la vue (aujourd'hui sans
  issue) : nœud de décision, et un canal de plus vers le surajustement que les faits rapportent chez d'autres.
- **Deux rappels de garde** ([Astra-à-part]) : déclarer la classe opérationnelle de copies que la garde couvre ; expliciter
  le contrôle des erreurs **entre** générations, pas seulement dans une génération. Personne ne traite le second.

**Le collisionneur apporte ce qu'aucune consultation n'a** : la critique. L'identité qui retire à J3 et J4 leur gain
annoncé ; l'équivalence entre poids de multiplicité et prime de nouveauté, qui atteint [Argon-à-part] M3 ; la chute de la
décomposition orthogonale sous traits dépendants ; l'inexistence du tableau couvrant de [C-T1] ; le placebo qui garde
l'archive vraie ; le budget compté en jetons ; la séparation des deux bancs (nul complet, copies hors classe) ; le contrôle
positif de puissance ; et l'essai le moins cher avec proposeurs, sur un monde **sans** bassin étroit ([A-T3], idée de
[B-T2]). La seule consultation qui combine ses méthodes dans un bras ([Argon-à-part]) reproduit le défaut que la course a
fait retirer à [C-T1].

## 4. Ce que la mère avait et que personne d'autre n'a, et l'inverse

**La mère seule** : tempérer (A1) ; remplir les bassins visités et servir des missions qui les excluent (A3) ; archive en
grille de type qualité-diversité (A4) ; sélection douce (C2) ; îles et échange de répliques (C3) ; **masse manquante**
(E1) ; la fiche qui **déclare sa région avant les données** (dans D1) ; la dose-réponse posée comme courbe (E2).
**(synthèse)** Trois remarques : A3 et C3 rouvrent le rejet du masquage d'archive, ce que la mère dit pour A3 ; C2 touche
la sélection, donc ce que le nul des générations suivantes contient ; la région déclarée de D1 tombe sous l'identité du
§5 (si la carte égale le nul hors de sa région, la valeur e globale est déjà locale), sauf pour l'allocation des tirages,
que [A-T3] a retirée.

**Les autres, et pas la mère** : la liste des paires non croisées et sa généalogie (V1, V2) ; les contrastes compilables
(I1) ; l'interface en écarts (I3) ; le dictionnaire de moments (V5) ; les vues équivalentes (V7) ; la synthèse typée, les
arbres, le fractionnement (C1 à C3) ; l'arrêt optionnel (J1) ; la garde par supremum (J6) et le filtre (J7) ; le jeu public
par plan (G1) ; tous les dispositifs de protocole de l'inventaire §8 ; et trois bornes : l'identité d'auto-localisation, la
barrière de parité, la largeur qui n'est pas un bouton.

**Le classement de la mère face à la course.** Rang 1 (mesurer d'abord : E2, E1) : conforme à la convergence, avec la
correction sur la largeur. Rang 2 (D1, D2, « mathématiques pures ») : **contredit** — D2 est abandonnée par l'espèce qui la
portait, D1 est réduite aux cartes mal spécifiées hors de leur région. Rang 3 (A4 avec B1, contre le témoin B2) : B1 et B2
recoupent V2, V3 et l'énumérateur ; A4 n'a pas été discutée. La condition de révision qu'elle écrivait (« les proposeurs
trouvent déjà les conditionnelles dès que la condition est archivée ») est aussi celle de [B-T1], [C-T1] et [Kimi-à-part].

## 5. Impossibilités et bornes dites

1. **Borne amont** : 1 − (1 − p)^k ; l'aval ne crée aucune carte ([A-T1] ; [C-T1] ; [B-T2] : « Le DPP ne crée pas de
   cartes »).
2. **Pas de repas gratuit sur la vue** : la somme des probabilités de bassins disjoints est au plus 1 ; sans information
   sur la classe que le monde contient, pas de vue uniformément meilleure ([A-T1], [B-T1], [D-T1], [E-T1],
   [Argon-à-part], [Astra-à-part], [Kimi-à-part], [Mère] E3).
3. **Barrière de parité** : une composante d'ordre k dont toutes les marges d'ordre inférieur sont nulles, sans issue ni
   résidu servi, demande de l'ordre du nombre de sous-ensembles de k traits en propositions aveugles ([C-T1], [C-T3]). Un
   gain amont suppose une hiérarchie : un parent détectable et archivé.
4. **Chaînes** : le temps de découverte est une somme de temps d'attente ; aucun maillon avant le précédent ([A-T1]) ; il
   faut au moins autant de générations que de prérequis ([Kimi-à-part]).
5. **Détectabilité** : pour une puissance 1 − β au niveau α, il faut n·r·Δ au moins égal à la divergence binaire entre
   1 − β et α ([E-T2], forme reprise en [C-T3]) ; avec m tests, de l'ordre de ln(m/α) ([Argon-à-part]) ; forme en
   variation totale chez [Astra-à-part]. Ni stratification, ni arrêt optionnel, ni pari localisé ne la franchissent.
6. **Auto-localisation** ([D-T2], [E-T2], concédée en [C-T3]) : si une carte égale le nul hors d'une région, sa valeur e
   globale **est** sa valeur e locale ; localiser n'ajoute rien et coûte la pénalité du poids. La dilution ne mord que sur
   les cartes mal spécifiées hors de leur région, et sur la **distance de regroupement**.
7. **Fermeture du nul** : une candidate qui appartient au nul a une valeur e au plus égale à 1 ; un nul assez large pour
   toutes les copies peut contenir les découvertes ([E-T1], [A-T2], [D-T2], [D-T3], [Astra-à-part]).
8. **Aucune certification empirique absolue hors du nul** : une simulation contrôle le code, jamais la preuve ([D-T1]).
   Le premier tour demandait une garde « certifiée en absolu » : ce tour dit ce que cela peut vouloir dire — une preuve
   pour un nul explicite, plus un audit séparé au sens de l'oracle.
9. **Copies par morceaux** : un nul à poids constants ne couvre pas le recollage de deux lois d'archive sur une partition
   ([Argon-à-part], et la limite rapportée aux faits).
10. **Poids de multiplicité selon la nouveauté** : pondérer le seuil ou multiplier la valeur e, c'est la même chose
    ([D-T2], [E-T2], [C-T3]).
11. **Tableaux couvrants binaires de force 2** : le nombre de facteurs couverts par N lignes est borné. **(synthèse,
    vérifié par calcul exhaustif, annexe)** La formule écrite en [A-T2] et [C-T3], C(N − 1, ⌊N/2⌋), est fausse pour N
    impair ; le maximum est C(N − 1, ⌊N/2⌋ − 1) : 3 facteurs pour 4 lignes, **4 pour 5**, 10 pour 6, 15 pour 7. Le plan
    « corrigé » de [C-T3] (cinq lignes, six colonnes) n'existe donc pas non plus : sa matrice laisse trois paires de
    colonnes incomplètes. Six facteurs demandent six appels.
12. **Largeur** : propriété du triplet (modèle, vue, archive), estimée, jamais réglée (§1).
13. **Sans observation dans la région, aucun calcul ne la localise** : probabilité (1 − r)^n de n'y rien voir
    ([Kimi-à-part], pour V10 et V11).
14. **Reconnaître « la même idée »** n'est décidable que dans une grammaire bornée ([Astra-à-part]) ; un groupe de
    doublons n'est pas un bassin ([B-T1], [D-T1], [E-T1]).

## 6. Expériences décisives proposées, classées par coût

**Sans appel de proposeur (calcul seul).**

- **Banc de garde et de puissance** : mondes entièrement dans le nul ; copies hors classe, dont les recollages alignés sur
  les cellules d'une partition et les cartes compilées depuis des contrastes ; cartes réellement additionnelles confinées à
  une région rare, comme contrôle positif. Duel : toutes les obligations gelées tiennent, contre au moins une échoue
  ([E-T3] préalable G ; [A-T3] E0 ; [C-T3] expérience 0 ; [D-T3] ; [Argon-à-part] étage 0 ; [Astra-à-part]). Critère de
  queue (probabilité de dépasser 1/α) plutôt que moyenne empirique des valeurs e ([A-T2], [E-T2]).
- **Rejeu de survie** : mêmes cartes scellées, juge à taille fixée contre juge à arrêt optionnel seul, à espérance de
  tirages égale ([A-T3] E3) ; juge à plusieurs échelles contre juge global à dénominateur identique, sur cartes
  « chirurgicales » et « globalement bruyantes », avec clause d'abandon ([C-T3]).
- **Qualification des instruments de regroupement** : fusion à tort de paires « égales sauf strate rare », choix de la
  sœur porteuse, sœur fausse mais éloignée ([A-T3], [D-T3]).
- **(synthèse)** La masse manquante de la mère (E1) et les mesures descriptives de la lecture des voisins (sort de chaque
  proposition, taille de pas) se calculent sur des sorties déjà scellées : même étage de coût.

**Quelques centaines à quelques milliers d'appels, une génération.**

- **Garde et levier sur un monde sans interaction** ([A-T3] E1, sur l'idée de [B-T2]) : vue brute, vue avec liste, vue
  placebo. Deux duels : le taux de promotion ne monte pas au-delà d'une marge ; la loi des cartes change ou non. Si elle
  ne change pas, on arrête là.
- **Criblage du mécanisme sur cartes brutes** ([D-T3]) : bloc « plan et moments » contre énumération et placebo, avec
  mesure mécanique de l'exécution des focalisations, mondes nuls, traits dépendants, structures hors dictionnaire.
- **Trois bras sur cent mondes plus cinquante mondes additifs** ([C-T3]) : vue standard, énumération, plan. Coût annoncé :
  10 à 35 USD, illustratif. **(synthèse)** Son plan est à refaire (§5, point 11).
- **Duel décisif de la liste** ([A-T3] E2) : liste contre placebo (information ou forme), liste contre vue brute à budget
  de jetons égal (table ou appels), et non-nuisance sur des mondes hors structure (parité d'ordre 3, seuil décentré).
- **Contrastes contre aide syntaxique contre appels indépendants** ([E-T3]), après le banc.
- **Plan de blocs certifié contre blocs indépendants de mêmes marges** ([Astra-à-part]) ; **focalisations contre
  placebo** ([Kimi-à-part]).

**Plus cher.**

- **Cinq bras, soixante courses par bras** ([B-T3]) : 7 480 USD annoncés, illustratif ; pilote à 900.
- **Tirage déterminantal des vues**, en duel séparé ([B-T3]) ; **pilote d'équivariance**, puis vues planifiées ([E-T3]).
- **Essai de course à plusieurs générations**, seulement après un mécanisme reproduit ([D-T3]) ; arbres, fractionnement,
  synthèse typée ; portefeuille et meilleur couple, sur des mondes de structure différente.

Les coûts des cellules vont de quelques dizaines à plusieurs milliers d'USD pour des dessins voisins : aucun ne vaut devis.

## 7. Ce qui rouvre un rejet du premier tour, et avec quel argument

| rejet du premier tour | qui le rouvre | argument avancé | issue |
|---|---|---|---|
| Aucune récompense numérique de la nouveauté dans le juge | J5 : [C-T1], [Argon-à-part], [Mère] D2 | les poids sont fixés sur le jeu public avant les issues : la garantie sur les fausses découvertes tient | **refermé dans la course** : [C-T3] « mathématiquement isomorphes » ; le rejet était de protocole, pas de validité ; le budget d'erreur irait au bruit orthogonal. Reste ouvert chez [Argon-à-part] et [Mère], sans réponse à cet argument |
| Idem, dans la sélection | G2 : [A-T1] | à l'intérieur d'un groupe, les sœurs sont déjà déclarées équivalentes ; aucune n'est promue pour sa nouveauté | **à moitié** : [E-T2] maintient que c'est un critère numérique de nouveauté ; [A-T3] le rétrograde en départage |
| Idem, servie comme consigne | V8 : [B-T1] | aucun score servi, seulement des régions suggérées | **refermé** : [B-T3] retire |
| Aucun quota de formes (forme ≠ idée) | C1 : [E-T1] | les ressources suivent des dérivations, pas un objectif de diversité | **concédé** : [E-T3] « un a priori syntaxique » ; suspendue |
| Idem | V3, V2, I1 | ce sont des questions ou une représentation offertes, aucune forme n'est imposée | **non contesté** ; mais toutes poussent vers le conditionnel |
| Aucun masquage d'une partie de l'archive | personne dans la course ni les consultations (tous servent l'archive entière) ; [Mère] A3 et C3 ; le bras « vue réduite » de la lecture des voisins | pour A3, des missions et non un masque ; pour C3 et la vue réduite, l'oubli des articles voisins | **non discuté** par les espèces : aucun argument nouveau n'a été éprouvé |
| Jamais le représentant par la plus grande valeur e | personne | — | **confirmé** ([Astra-à-part] : le maximum ne garde pas la validité ; [A-T3] : ordre de continuation jamais par valeur e) |
| La mesure de diversité ne pilote ni consignes ni sélection (conception en cours) | toutes les méthodes de vue | [C-T3] : la vue est bâtie sur la seule syntaxe de l'archive, sans calculer la mesure ; [B-T3] : la mesure est lue après la course | **déclaré dessin neuf** par [B-T3], [C-T3], [D-T1], [E-T1], [Astra-à-part] : c'est un nœud |

## 8. Ce qui touche le juge statistique et exige une preuve

Chacun de ces points modifie le juge, le gardien, le regroupement ou la multiplicité : **écart à la conception scellée,
donc nœud de décision**, et preuve écrite contre-lue avant tout usage.

- **J1** : surmartingale **à chaque pas** pour toute loi du nul composite ([E-T2]) ; dénominateur à mélange de poids fixés
  d'avance, jamais recalibré sur les issues ; règle d'allocation et ordre de continuation scellés ; [A-T3] : « à démontrer
  dans le préenregistrement, pas à affirmer ».
- **J3** : validité de chaque facteur local, pas seulement du mélange ([E-T2]) ; nul local sans recalibrage ; partition
  scellée avant la graine.
- **J4** : validité de l'infimum sur le nul composite ; statut du nul ponctuel, qui **est** une extension du nul, avec sa
  perte de puissance (§3).
- **J5** : abandonnée ; si la mère la reprend (D2), l'objection de [C-T3] est à lever d'abord.
- **J6** : supremum exact sur une classe finie, ou majorant démontré ; une grille qui le sous-estime rompt la validité
  ([B-T2], [D-T3]) ; version par épisode et version sur l'échantillon à distinguer ([E-T2], [C-T2], [E-T3]).
- **J7** : un filtre de plus au gardien change quelles cartes atteignent le juge, donc m ; personne ne l'a examiné.
- **Borne commune sur le nombre de tests**, positions vides à valeur e nulle ([E-T3]) : à auditer, dit son auteur.
- **G2, G3** : le choix du représentant et la règle de regroupement entrent dans la preuve de la valeur e de groupe de la
  conception en cours ; remplacer la liaison complète par un pivotage (G3) demande de refaire cette preuve **(synthèse)**.
- **I1, I3** : équivalence prédictive entre la carte écrite et la carte jugée ; le nul doit couvrir les copies que la
  représentation rend faciles (recombinaisons compilées ; enveloppe log-linéaire).
- **mère-C2** : une place tirée au sort fait entrer dans l'archive, donc dans le nul des générations suivantes, une loi
  non promue **(synthèse)**.
- **Entre générations** : aucun texte ne prouve le contrôle des erreurs sur plusieurs générations ([Astra-à-part]).

## 9. Recommandation à préparer pour le directeur

**Décision à prendre** : quelles méthodes éprouver comme bras de la course sur le monde planté, et dans quel ordre.
**Enjeu** : toute méthode de vue est un dessin neuf et toute méthode de juge un écart à la conception scellée ; les deux
poussent vers la classe où la garde cède. **Préalable commun, qui n'est pas un bras** : le banc sans proposeur du §6
(garde **et** puissance, deux bancs séparés), au même titre que le banc de métrologie du premier tour ; il départage aussi
les gardes candidates (J6, J7, nul ponctuel de J4) et tranche le sort de J3 par sa clause d'abandon.

| ordre | méthode | pourquoi | témoin à coût égal | condition bloquante |
|---|---|---|---|---|
| 1 | **J1 — arrêt optionnel seul**, en rejeu sur cartes scellées, zéro appel | seule méthode de juge qui sort de la critique avec sa revendication entière (validité sous toute règle d'arrêt écrite d'avance) ; sert l'étroit « dans les données » | juge à taille fixée, **à espérance de tirages totale égale** | preuve écrite et contre-lue (surmartingale à chaque pas sous le nul composite, dénominateur fixe, règle d'allocation scellée) ; au banc, queue sous le niveau nominal ; nœud pour l'écart au juge |
| 2 | **V2 — la liste des paires non croisées**, une génération, archive gelée | lève l'inconnue centrale au moindre coût ; quatre espèces y aboutissent ; tout habillage doit la battre | vue brute à **budget total de jetons égal** (plus d'appels) ; placebo de même format et longueur, archive vraie, table tirée au hasard | banc passé ; d'abord le monde sans interaction (garde non inférieure, puis levier) ; non-nuisance hors structure ; nœud « dessin neuf » |
| 3 | **V3 — plan qui répartit les focalisations**, avec V5 en facteur de contenu | portée par deux espèces et les trois consultations ; une inégalité démontrée pour le plan équilibré | la liste entière à tous (V2) ; les mêmes focalisations tirées sans remise ; blocs indépendants de mêmes marges après permutation commune des noms | seulement si V2 montre un levier ; plan **exhibé et vérifié par programme** (§5, point 11) ; mesure d'exécution des focalisations ; dictionnaire scellé avant la graine ; mondes hors dictionnaire |
| 4 | **I1 — contrastes compilables** | premier candidat de son auteur ; attaque le coût d'écriture d'une interaction | même compilateur sans la bibliothèque ; appels indépendants au même budget ; énumérateur mécanique | preuve d'équivalence prédictive ; copies compilées tenues par la garde au banc ; borne commune sur le nombre de tests auditée ; mondes non alignés sur la bibliothèque |
| 5 | **C3 — affectation des appels à la frontière de l'archive, sur plusieurs générations** (parente de mère-B1) | seule voie qui vise la profondeur en chaîne, celle que le monde plante | même nombre d'appels sous vue standard sur les mêmes générations ; meilleur de N premières générations à coût égal | **non critiquée** : à faire contre-lire d'abord ; seulement après un gain brut **et** retenu de V2 ; horizon au moins égal au nombre de prérequis ; contrôle des erreurs entre générations écrit |

**Options.** (a) Le tableau tel quel. Avantage : chaque pas peut clore la question avant le suivant ; inconvénient : la
profondeur n'est abordée qu'au rang 5. (b) S'arrêter à 1 et 2. Avantage : dépense minimale, répond à « la vue bouge-t-elle
quoi que ce soit » ; inconvénient : ne dit rien des habillages ni des chaînes. (c) Ajouter un bras du remue-méninges de la
mère (A4 ou A1). Avantage : idées que la course n'a pas vues ; inconvénient : aucune n'a été critiquée, et A3 ou C3
rouvriraient le masquage. **Recommandation (synthèse)** : (a), en tenant (b) pour le périmètre du premier devis ;
confiance 0,7 sur l'ordre 1 puis 2, 0,5 sur les rangs 3 à 5, qui dépendent de ce que 2 montrera. **Hors bras** : garder
mère-E2 comme cadre de lecture (courbe selon la largeur **estimée**) et mère-E1 comme mesure descriptive ; ne pas reprendre
J5 ni J2. La dépense de tout essai avec proposeurs relève d'un devis et d'un GO ; le préenregistrement précède toute
lecture (R1) ; le verdict revient à un lecteur neuf (R13).

## 10. Faiblesses du tour

- **Ancrage.** La question nomme la composante conditionnelle ; quatre espèces sur cinq proposent l'outil taillé pour elle
  (base de Walsh, cases d'interaction). Le « vrai par construction » que les espèces se reprochent vaut pour le tour
  entier. Aucune méthode n'est pensée pour un bassin étroit d'une autre forme.
- **La profondeur est sous-traitée.** Tous les duels corrigés tiennent en une génération ; les chaînes de profondeur 2 ne
  sont visées que par deux consultations non critiquées.
- **Le dernier tour n'a pas de contradicteur.** J7, la borne commune sur le nombre de tests, l'invariance aux clones du
  pivotage, le plan de [C-T3] : personne n'y a répondu ; le plan est faux (§5, point 11), et l'étiquette « VÉRIFIÉ par
  calcul » d'une cellule ne vaut pas vérification.
- **Sources non indépendantes.** Huit textes, cinq modèles, quatre fournisseurs ; chaque consultation à part vient d'un
  modèle qui siège aussi dans la course, et le remue-méninges d'un modèle de la famille de A et B. Une ligne portée par
  « deux espèces et trois consultations » ne compte pas cinq voix.
- **Les consultations à part n'ont été critiquées par personne**, y compris leurs « théorèmes exacts ».
- **Références de mémoire**, souvent marquées « à vérifier » par leurs auteurs : aucune n'est opposable (R7), et l'une
  d'elles est fausse telle qu'écrite.
- **Les faits ne disent pas ce que la vue contient de données** ; [A-T1], [Kimi-à-part] et [Mère] butent dessus.
- **Coûts illustratifs** incomparables, d'un facteur cent entre espèces.
- **Un incident** : première réponse de A tronquée au tour III.1, relancée par le script (note de dépense).
- **Cette synthèse** est d'un seul lecteur, de la lignée de deux espèces ; les sorts « survivante pleine » et « suspendue »
  sont ma lecture.

## Annexe — vérification par calcul du point 11 (lecteur, processeur seul)

Programme exécuté hors dépôt (bac de travail de la session), `python3 -I`, à 14:47 UTC : énumération exhaustive des
colonnes binaires de longueur N et recherche de la plus grande famille de colonnes deux à deux « complètes » (les quatre
couples présents) ; puis contrôle de la matrice 5 × 6 écrite en [C-T3].

```
N=3 lignes : maximum exhaustif de colonnes = 1 ; C(N-1, floor(N/2)) = 2 ; C(N-1, floor(N/2)-1) = 1
N=4 lignes : maximum exhaustif de colonnes = 3 ; C(N-1, floor(N/2)) = 3 ; C(N-1, floor(N/2)-1) = 3
N=5 lignes : maximum exhaustif de colonnes = 4 ; C(N-1, floor(N/2)) = 6 ; C(N-1, floor(N/2)-1) = 4
N=6 lignes : maximum exhaustif de colonnes = 10 ; C(N-1, floor(N/2)) = 10 ; C(N-1, floor(N/2)-1) = 10
N=7 lignes : maximum exhaustif de colonnes = 15 ; C(N-1, floor(N/2)) = 20 ; C(N-1, floor(N/2)-1) = 15
Matrice 5x6 de [C-T3] : paires de colonnes incomplètes = 3 sur 15
  colonnes 1 6 couples manquants [(0, 0), (1, 1)]
  colonnes 2 5 couples manquants [(0, 0), (1, 1)]
  colonnes 3 4 couples manquants [(0, 0), (1, 1)]
```

Portée : le calcul établit les maximums pour N de 3 à 7 et le défaut de cette matrice ; il ne dit rien de l'utilité d'un
plan pour un modèle. La conclusion de [A-T2] (douze facteurs demandent au moins sept lignes) reste juste.
