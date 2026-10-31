# Relecture indépendante du papier « protocelles » — temps 2 (confrontation avec conv-audit) — v1

Relecteur : sous-agent neuf Opus 5.5, 31 octobre 2026. Écrit **après** `relecture-independante-opus-temps1-v1.md`, et après lecture de `idees-conv-audit-papier-protocelles-v1.md` (conv-audit, pages 1 à 20 lues, annexes non lues). Même source et même empreinte (`b699fed4…`) ; pages du PDF. La défense jointe boîte blanche + boîte noire s'appelle **la pince**. Les renvois « I-n » visent mon fichier du temps 1.

---

## Verdicts, section par section

### Section 1 — « Un plafond et un prix » comme forme pour l'arène : **raffinée**
La forme est bonne pour rapporter un résultat. Mais le plafond du papier a une cause précise : une division **aveugle** à l'identité des molécules, d'où une surmartingale valable à toute taille (p. 4, l. 98-101 ; p. 31, l. 739-744). Le mélange d'équilibre n'est pas aveugle : ses poids viennent du jeu. Rien n'autorise donc à attendre un plafond a priori. Trois choses rendent la section plus précise :
1. **Un signe.** conv-audit demande si le gain B − A « sature ou croît » avec d. Je prédis qu'il **décroît**, par effet de petite taille : pour θ > 1, les petites protocelles font beaucoup mieux que les grandes (0,557 à n = 3 contre 0,288 à la limite, θ = 1,5 ; p. 24), et la tolérance de parasites rapides chez Shah et collègues est présentée comme un effet de petite taille (p. 46, l. 1248). Mesure : d ∈ {6, 12, 24} avec `arene_melange_v2.py`, racines d'essai (I-6 a).
2. **Deux ordres de limites.** d → ∞ à T fixé et T → ∞ à d fixé peuvent ne pas commuter (p. 5, l. 120 ; p. 10, l. 243-244). Il faut chercher une variable de rapport, comme y = n/R (I-6 b).
3. **Le « prix » demande un analogue explicite de la fécondité.** Le candidat est le budget de mise à jour du défenseur par tour (échantillons, départs de l'oracle). Sans lui, il n'y a pas de prix.

### Section 2 — « Ce qui se reproduit, c'est la paire » → l'allumage : **raffinée**, et la mesure proposée est **renversée**
Le comptage des paires tient sous une condition : une fusion n'engendre une fiche fertile que si **ses deux parents** le sont (logique du « et »). Alors le taux de naissance est proportionnel à F(F−1), comme dans le papier. C'est vrai par construction dans les mondes synthétiques, où un vrai pont exige ses deux extrémités. Quatre points le précisent ou le corrigent :
1. **La branche « trans » du papier ne se transporte pas telle quelle.** Le papier tient parce que le catalyseur ne transmet rien (p. 1, l. 20-24). Dans une fusion, les deux parents transmettent. Le papier traite ce cas : avec un poids c > 0 de transmission par le catalyseur, il n'y a plus de plafond à haute fécondité (p. 10, l. 242-244 ; p. 27). L'organisme se situe sans doute plus près de ce régime pour le contenu des fiches. Le plafond ne vaut que pour ce qui agit en trans : opérateur, consignes, juge, sélecteur (I-0).
2. **Pas de processus de branchement sans lignées de lots.** Dans une réserve homogène, la reproduction par paires est quadratique (champ moyen, p. 37, l. 971-973). Le rayon spectral n'a de sens qu'au niveau des compartiments, ici des lots avec une **règle de filiation explicite**. Il faut la définir avant de mesurer.
3. **La mesure « sans dépense, sur les journaux de la course 2 dès la génération 1 » est impossible.** Une matrice moyenne de descendants exige au moins deux générations avec filiation. La course 2 est, à ma connaissance, une génération de 24 fusions. Ce qui est sans dépense, c'est de **journaliser la parenté et la filiation des lots dès maintenant**, et d'écrire l'estimateur avec ses gardes.
4. **Deux nombres manquent.** L'**apport extérieur** d'abord : avec une copie spontanée χ ≥ 1, il n'y a plus de seuil du tout (p. 10, l. 241-242 ; p. 22). Les proposeurs qui injectent des fiches neuves sont cet apport, et l'allumage ne se mesure qu'à apport coupé. La **persistance** ensuite : le seuil d'invasion est inchangé par la fusion, mais une population établie peut persister au-delà si la fusion voit le contenu (p. 10, l. 244-247 ; p. 27). L'allumage se dit donc en deux nombres. S'y ajoutent l'outil, un certificat de Collatz–Wielandt avec h(F) = F(F−1) (p. 31, l. 739-741), et une garde : une composante inatteignable peut porter le plus grand rayon spectral (p. 59, l. 1729-1732).
L'affirmation « meilleur que l'ensemble autocatalytique » doit devenir « complémentaire ». La fermeture autocatalytique est une condition nécessaire et statique ; le rayon spectral à apport coupé est la condition dynamique.

### Section 3 — Parasites et θ → les faux ponts : **raffinée**
C'est le cœur commun aux deux lectures (mon I-1). Deux énoncés de conv-audit sont inexacts :
1. **« Si θ > 1, le plafond ln(2/θ) fond et aucune fidélité ne suffit. »** Le papier dit : aucune fidélité ne suffit **en mélange homogène** ; les protocelles gardent max(0, ln(2/θ)) à grande taille (p. 9, l. 213-214). Le seuil de condamnation avec des lots est donc **θ ≥ 2** (p. 4, l. 86-88). Entre 1 et 2, des lots peuvent encore sauver, et les petits mieux que les gros.
2. **« Quel que soit le filtre de qualité en aval. »** Un filtre qui décide quelles fiches **entrent dans la réserve de parents** est précisément la discrimination θ < 1, le seul levier (p. 9-10, l. 234-236). Le bon énoncé : θ se définit à l'étape qui choisit les parents, et tout ce qui agit avant ce choix compte dans θ. Un filtre qui ne note que les sorties finales, sans gouverner le choix des parents, ne change rien à la dynamique.
J'y ajoute la forme close de la tolérance en réserve homogène, 1 − e^−U_c = (1 − 1/R)(1 − θ) (p. 6, l. 122). Avec 90 % de filles stériles, il faut θ ≤ 0,1 et R grand. J'ajoute aussi l'inertie de l'efficacité catalytique : un opérateur plus productif produit les parasites dans la même proportion (p. 4, l. 88-89). Enfin, sur une seule génération, θ n'est qu'une précision normalisée ; il ne prédit une dynamique que si les sorties redeviennent des parents.

### Section 4 — Fécondité contre taille du lot : **tenue sous condition**, et **raffinée**
**Condition** : des lignées de lots sélectionnées sur plusieurs générations. Une course à une génération ne peut pas tester « les petits lots s'allument, les gros non ».
**Raffinement** : la prédiction n'est pas monotone. Pour θ < 1, les très petites protocelles font **moins bien** que le mélange homogène : le gain vaut −0,20 à n = 2 pour θ = 0,5 (p. 2, légende de la figure 1). À R = 40, le seuil monte puis redescend avec n (p. 5, figure 3C). Il existe donc une taille de lot optimale pour θ < 1, alors que pour θ ≥ 1, plus petit vaut mieux. J'ai aussi une estimation grossière pour la configuration actuelle : y ≈ 1 à 3, soit ψ ≈ 0,49 à 0,35, environ la moitié du bonus (le nombre de lots est SUPPOSÉ ; I-5).
**Non évaluable par moi** : le lien avec CA1-05 (« profil vide dans 0,59 à 0,67 des lots à 6 fiches ») ; je n'ai pas lu cette pièce.

### Section 5 — Copies inachevées → fusions inachevées : **raffinée**
La règle « jeter, jamais archiver comme fiche réutilisable » tient ; je l'avais trouvée de mon côté (I-3). Quatre précisions issues des annexes, que conv-audit n'a pas lues :
1. **Le coude.** Seuls comptent les fragments **plus de deux fois** plus attractifs qu'une fiche complète (p. 7, l. 167-170 ; p. 8, figure 5B). Le coût croît avec le nombre de fragments par lot et par génération, nτ (p. 7, l. 157-159).
2. **Jeter coûte peu** : exactement 1/(1−τ) en débit (p. 6, l. 154). La règle est presque gratuite.
3. **Pas de demi-mesure proportionnelle.** Jeter certains fragments et en recycler d'autres n'est pas une simple remise à l'échelle (p. 58, l. 1666-1668). La règle doit être totale.
4. **Une rétrodiction possible.** La saturation de l'ancien organisme par des mots-outils à la génération 18 se lirait comme une prise de contrôle par des « modèles rapides » (confiance 0,4, journaux non lus).
La vérification de la politique d'archive de la v55, proposée par conv-audit, est la bonne première mesure.

### Section 6 — La boucle de Bailey comme branchement de la nouveauté : **renversée** (tenue seulement sous condition)
Un processus de branchement exige des individus qui engendrent des descendants indépendamment les uns des autres. Chez Bailey, chaque tour produit **une** attaque optimisée contre le moniteur courant : c'est une trajectoire, pas une population. « La matrice moyenne de descendance de la nouveauté » n'y est pas définie. Ce qui se mesure sur une trajectoire, c'est un **taux de contraction** de la nouveauté résiduelle (piste 4 du brainstorm), un scalaire qui ne doit rien au papier.
**Condition sous laquelle l'idée revit** : dans l'arène, un générateur à **population**, dont les familles d'épreuves engendrent des familles filles. Le rayon spectral se définit alors sur les lignées qui contournent la défense.
Ce que le papier apporte vraiment à l'arène est ailleurs : l'effet de petite taille, la variable de rapport, et surtout le fait que le seul levier du papier, la discrimination θ, y est **fixe**. La boucle de Bailey, c'est θ qui remonte vers 1 par imitation, tour après tour (I-6 c). Mesure : suivre ce θ par tour dans les journaux des pilotes (non opposables).

### Section 7 — Méthode à reprendre : **tenue**
Rien à redire. J'y ajoute quatre points : la garde de composante inatteignable (p. 59) ; le refus d'extrapoler une loi de puissance ajustée (p. 38, l. 1007-1008 ; utile pour toute tendance sur les tours) ; le seuil d'une population finie, borné par celui du branchement (p. 47, l. 1254-1255) ; les étiquettes de statut, prouvé assisté par ordinateur compris (p. 29, l. 663-667).

---

## Ce que j'avais trouvé et que conv-audit n'a pas
- **La porte de transport (I-0)** : une fusion est une recombinaison, pas une copie en trans. Le papier dit que la transmission par le catalyseur (c > 0) supprime le plafond à haute fécondité, avec c̃ = cR/n (p. 10 ; p. 27). Le plafond ne s'applique qu'aux composants qui agissent en trans.
- **L'apport extérieur χ** (aucun seuil si χ ≥ 1) : l'allumage se mesure à apport coupé.
- **Invasion contre persistance**, avec bistabilité si la fusion voit le contenu (p. 27).
- **Le certificat de Collatz–Wielandt** sur F(F−1) et la **garde de réductibilité** (p. 31 ; p. 59).
- **La forme close** (1 − 1/R)(1 − θ), le **seuil θ ≥ 2 avec lots**, la correction de « quel que soit le filtre en aval ».
- **La composition des lots (I-4)** : convexité de F(F−1) ; une partition égale fait moins bien que le hasard (ln 1,44 contre ln 2, p. 47) ; le levier du tri, 71 % des paires gardées pour ln 4 (p. 10).
- **La non-monotonie en taille de lot** pour θ < 1 (p. 2 ; p. 5).
- **Pour l'arène** : l'effet de petite taille avec un signe prédit, la variable de rapport et l'ordre des limites, θ qui évolue comme extension manquante du papier, et le certificat avec marge.
- **Pour la pince** (transports faibles, signalés) : le sort des actions signalées (annulées ou persistantes), la moyenne à travers un coude comme appui à N-026, l'additivité en logarithme des deux mâchoires.
- **Des remarques sur le papier** : la condition « τ égal pour tous les modèles » manque à la ligne 154 (p. 6 contre p. 58) ; le titre « Conjecture 1 » de la figure 3B (p. 5) ; la constante 3√2 − 4, qui revient deux fois ; ce qui bloque la soumission (p. 1, 15-17, 20).

## Ce que conv-audit a et que je n'avais pas
- **Les antériorités Weitzman** (« Recombinant growth », 1998, PDF fourni par Lazar selon conv-audit ; non lu par moi) et Tria, Loreto et collègues sur le possible adjacent (SUPPOSÉ). C'est le voisinage le plus direct pour « les idées naissent de paires ». À lire avant toute revendication sur l'allumage.
- **Des points d'ancrage concrets dans le programme** : le budget GO-2026-10-31-04, CA1-05 (profil vide dans les lots à 6 fiches) et la politique d'archive de la v55, première mesure de la section 5.
- **La forme de rapport** « ce que la structure ajoute au plus, ce qu'elle coûte avec la taille », et le pendant de la fin du papier : dire ce que les expériences du type de Bailey devraient rapporter (coût par contournement, nouveauté résiduelle).
- **Le bisociateur côté défense** (section 0) : des familles de défense engendrées par recombinaison, mouvement non local. Le papier l'éclaire indirectement : la recombinaison sort du régime trans, où la sélection ne voit pas la qualité. L'hypothèse est à garder, sans preuve.

---

## Classement final des cinq idées les plus prometteuses

1. **Le θ des distracteurs, défini à l'étape du choix des parents, avec une garde « θ̂ ≥ 2 : itération condamnée, aucun lot ne sauvera ».** *Première mesure* : estimer θ par bras et par classe (surface, proche, faux) sur les journaux existants des mondes synthétiques, avec des intervalles par rééchantillonnage, sur processeur.
2. **L'allumage en deux nombres plus un contrôle** : seuil d'invasion (rayon spectral de la matrice des lots filles, certificat de Collatz–Wielandt sur F(F−1), restreint à la composante atteignable), persistance, apport des proposeurs coupé. *Première mesure* : journaliser dès la prochaine course la parenté des fiches et la filiation des lots, et écrire l'estimateur avec sa garde, testée sur un cas simulé sain et sur un artefact réductible (R5).
3. **La porte de transport : héritabilité biparentale des fusions**, qui dit où le plafond s'applique (composants en trans) et où il ne s'applique pas (contenu hérité, régime c > 0). *Première mesure* : sur le premier journal à deux générations, régresser la qualité des filles sur celle de chacun des deux parents.
4. **Jeter toute fusion inachevée ou incohérente, sans demi-mesure.** Le coût est seulement 1/(1−τ) en débit ; le danger vient des fragments plus de deux fois plus attractifs. *Première mesure* : lire la politique d'archive de la v55 pour savoir si des sorties invalides reviennent dans la réserve de parents, puis chercher sur disque les journaux de la génération 18 de l'ancien organisme pour la rétrodiction (R11).
5. **L'effet de petite taille dans l'arène** : l'avantage du mélange d'équilibre sur la défense unique décroît-il avec la dimension ? *Première mesure* : `arene_melange_v2.py` avec d ∈ {6, 12, 24} sur les racines d'essai, signe de B − A ; une version décisive passe par un préenregistrement.

Sixième, hors classement : le comptage des paires vraies disponibles sous trois règles de constitution des lots (hasard, équilibrée, regroupée), sur les étiquettes plantées, sans appel de modèle (I-4).

## Réserves
- Les antériorités marquées SUPPOSÉ ne sont pas vérifiées. Le voisinage « seuil d'erreur et génération répétée par modèles de langage » (effondrement des modèles) est probablement occupé. Les usages proposés ici sont internes et ne revendiquent rien.
- Plusieurs mesures supposent des journaux multigénération qui n'existent peut-être pas. Les produire par des appels de modèle est une dépense, donc un devis et un GO.
- Je n'ai lu ni le code des mondes synthétiques ni celui de la course 2. Que les fusions se fassent à l'intérieur des lots, et le nombre de lots, restent SUPPOSÉ.
