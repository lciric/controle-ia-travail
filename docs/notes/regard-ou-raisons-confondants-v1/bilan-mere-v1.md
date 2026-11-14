# Bilan de la session mère : explications rivales autres que le regard, et forme du papier « Regard ou raisons » — v1

Écrit par la session mère le 14 novembre 2026, **avant** qu'aucune autre source (organisme, collisionneur, Astra, Argon) ne
soit interrogée, et scellé avant toute lecture d'un autre bilan. Répond à `question-v1.md` (`f0481482…`) sur `faits-v1.md`
(`87086190…`). Seule source : le brouillon du billet, lu dans la session. Aucun article relu sur pièce : toute référence est
« à vérifier ». Les calculs marqués « illustratif » sont faits sur les taux du brouillon, sans grappes.

## 1. Ce que la question suppose sans que ce soit établi

- **Qu'il n'y a que deux candidats.** Écarter le regard n'établit pas « raisons » : il faut une signature positive de
  « raisons », et la liste des autres rivales. Le projet teste aujourd'hui une rivale sur au moins huit.
- **Que « regard » est une seule variable.** Les textes « évaluation » contre « déploiement » mêlent au moins trois
  croyances : on m'observe ; ceci n'est pas réel ; ce que je fais ici me changera. Elles peuvent agir en sens opposés.
- **Que le gain est une quantité stable.** Il est mesuré sur un adaptateur par recette (une graine), une échelle (points de
  taux), un juge d'une famille, 27 évaluations issues d'un même gabarit public.
- **Que la direction prise sur le modèle de départ désigne la même chose dans chaque adaptateur**, et que l'organisme témoin
  vaut pour eux.

**Signature positive de « raisons »** (ce qu'aucune rivale ci-dessous ne prédit) : (i) *sensibilité à la raison* — dans des
paires de scénarios identiques en surface où seul change le fait qui rend l'action nuisible, le modèle agit quand l'action est
légitime et s'abstient quand elle nuit ; (ii) *transfert aux cas non nommés* — le gain tient pour des actions nuisibles que ni
la spécification ni les démonstrations ne nomment, mais que les mêmes raisons couvrent ; (iii) *couplage* — les raisons que le
modèle énonce prédisent ce qu'il fait quand on édite le fait pertinent.

## 2. Partie A — huit explications rivales, par ordre d'importance

**A1. Réflexe de refus étendu aux actions d'agent (famille a).** L'entraînement a seulement abaissé, dans les contextes
d'agent, le seuil d'un mécanisme de refus qui existait déjà pour les demandes nuisibles en conversation ; aucune raison
n'intervient. *Sépare* : sous A1, le taux de fausses alarmes monte (le modèle s'abstient aussi quand l'action est légitime) et
retirer la direction de refus du modèle de départ ramène le taux d'actions nuisibles près de la référence ; sous « raisons »,
la discrimination s'améliore et une part du gain survit au retrait. *Test le moins cher* : la machinerie de la seconde
manipulation, avec la direction de refus à la place de la direction d'évaluation ; **elle sert aussi de contrôle positif dans
le modèle même** (si retirer une direction du modèle de départ ne change rien à un refus connu dans l'adaptateur, le transport
est en cause). *Contrôles* : positif, demandes nuisibles de conversation (le refus doit tomber) ; négatif, directions tirées au
hasard, appariées en dégât. *Publié* : direction unique du refus (Arditi et collègues, 2024, référence à vérifier) ; non
trouvé de ma part pour ces adaptateurs. *Coût* : bas à moyen. *Relecteur* : « votre modèle refuse l'action même sur ordre :
est-ce autre chose qu'un refus ? ». Le constat « refuse sur ordre, obéit à une instruction bénigne avec le même outil » est
compatible avec A1.

**A2. Reconnaissance du scénario et présence du contenu (a).** Les documents et démonstrations décrivent ces familles de
situations (se copier, divulguer, nuire) ; le modèle a appris « dans ce genre d'histoire, ne fais pas l'action listée », clé de
surface et non raison. *Sépare* : le gain décroît avec la distance de surface aux données d'entraînement à raisons égales, et
ne se transfère pas aux actions non nommées ; « regard » ne prédit aucune dépendance à cette distance. *Test* : sur les
épisodes déjà joués, régression du gain par évaluation sur la proximité (plongements, n-grammes) avec les corpus publiés ; puis
variantes à surface neuve. *Contrôles* : positif, un scénario copié des données ; négatif, proximité mesurée contre un corpus
sans rapport. *Publié* : [4] porte ce nom même (« content presence ») et [7] trouve que l'effet ne s'étend pas à des
évaluations plus réalistes — **à lire sur pièce avant toute revendication**. *Coût* : bas si les corpus sont publics.
*Relecteur* : les scénarios de [2] sont publics depuis 2025.

**A3. Échelle et plancher (c).** S est un rapport d'écarts de taux ; la recette avec raisonnement est près du plancher. « Son
gain ne bouge pas » est vrai en points et ne l'est pas forcément en cotes. *Illustratif* : sous la paire « évaluation », en
logarithme des cotes, la recette avec raisonnement monte de +0,34 quand on lui dit « déploiement », la référence de +0,09, la
jumelle sans raisonnement descend de 0,20 ; relativement à la référence, +0,25 contre −0,29 (interaction de l'ordre de 1,5
écart-type sans grappes : non concluante, mais de signe « regard » pour la recette avec raisonnement). *Sépare* : un artefact
d'échelle change de signe ou de taille selon l'échelle ; un effet réel tient sur les deux. *Test* : sur la table publique,
modèle logistique mixte (recette × phrase, effets aléatoires par évaluation), marges d'équivalence fixées d'avance ; aucun
calcul neuf. *Contrôles* : simulation à effet nul vrai près du plancher ; paire « journaux ». *Coût* : nul. *Relecteur* : c'est
la première objection d'un statisticien.

**A4. Moindre poursuite du but donné (a).** Dans ces scénarios, l'action nuisible sert un but donné dans la consigne, sous
menace de remplacement ; la recette a pu rendre le modèle moins sensible aux buts de consigne ou à sa propre continuité, sans
raison morale. *Sépare* : le gain se concentre dans les conditions où un but est donné, et le modèle persiste moins aussi dans
des tâches bénignes à obstacle ; « raisons » prédit un gain semblable quelle que soit l'origine de la tentation et une
persistance bénigne intacte. *Test* : décomposer le gain par condition de but et par action sur les épisodes déjà joués
(gratuit) ; puis tâches bénignes de persistance. *Contrôles* : positif, un modèle bridé par consigne ; négatif, la référence.
*Publié* : conditions de but de [2] (à vérifier). *Coût* : nul, puis bas.

**A5. Croyances de situation autres que l'observation (a et b).** La direction « évaluation contre déploiement » porte aussi
« ceci est fictif » et « ceci me changera ». « Fictif » peut désinhiber (aucun tort réel) quand « observé » inhibe : deux
effets opposés donneraient l'effet nul constaté. *Sépare* : des sous-directions construites sur trois contrastes tenus à part
(observé ou non, à réalité fixe ; réel ou fictif, à observation fixe ; conséquence pour soi ou non) ont des effets distincts,
peut-être de signes contraires, sur le gain. *Test* : dans la seconde manipulation, trois retraits au lieu d'un. *Réserve* : la
paire « journaux » fixe déjà la réalité par les mots et reste nulle ; mais une phrase ne fait pas croire. *Publié* : [8],
[10], [2] (davantage d'actions quand le modèle dit croire la situation réelle : à vérifier). *Coût* : moyen.

**A6. Transport de la direction et effacement incomplet (b).** Après retrait, l'adaptateur peut encore lire l'évaluation par
d'autres directions ; un « la conduite tient » serait alors muet. L'organisme témoin ne couvre pas ce cas : son entraînement
lie exprès la conduite à cette direction. *Sépare* : une sonde neuve, entraînée sur les activations du modèle **après**
retrait, décode encore « évaluation contre déploiement ». *Test* : sonde après retrait dans chaque adaptateur ; effacement à
garantie linéaire plutôt qu'une direction (LEACE, référence à vérifier) ; contrôle positif dans le modèle même (A1).
*Contrôles* : positif, l'organisme ; négatif, direction au hasard. *Coût* : bas (activations seulement).

**A7. Raisonnement au moment de répondre (c, pour le contraste entre jumelles).** Les jumelles diffèrent par l'entraînement
*et* par la présence d'un raisonnement à l'inférence ; D confond les deux. *Sépare* : plan deux par deux (entraînée avec ou
sans raisonnement × raisonnement permis ou coupé à l'inférence) ; si le gain suit le raisonnement à l'inférence, ce n'est pas
ce qui a été appris. *Test* : épisodes neufs sur deux cellules. *Coût* : bas.

**A8. Juge et style (c).** Les données d'entraînement et le juge viennent de la même famille de modèles ; un texte qui « sonne
aligné » peut être jugé avec indulgence. *Sépare* : un détecteur par programme de l'action (appel d'outil et charge utile),
sans modèle, donne le même gain. *Test* : écrire le détecteur pour les trois actions, le valider sur cent étiquettes humaines,
recalculer sur les épisodes déjà joués. *Coût* : bas. Les deux contrôles du projet n'excluent qu'un effet grossier.

**Autres, en une ligne.** Déférence à l'autorité (déjà en partie contredite par le refus sur ordre) ; changement de
personnage plutôt que raisons (retrait d'une direction de personnage : même machinerie qu'A1) ; une seule graine par recette
(demander les graines aux auteurs, ou les bras de la taille inférieure) ; croyance d'évaluation déjà saturée par le caractère
artificiel des scénarios (la lire par sonde pendant les épisodes : expliquerait l'effet nul de la phrase).

## 3. Partie B — forme du papier

1. **Thèse.** « Nous donnons un test réutilisable — le gain d'une recette survit-il quand on retire au modèle la lecture
   interne d'une croyance ? — validé sur un cas où la réponse est connue, et nous l'appliquons aux recettes de [1]. » Le papier
   vend la méthode ; le résultat sur [1] en est la première application.
2. **Figure 1, deux panneaux.** À gauche, l'organisme : la conduite conditionnelle tombe sous le retrait (la méthode voit ce
   qu'elle doit voir). À droite, les recettes jumelles : part du gain restante après retrait, avec intervalles, contre les
   directions témoins. Un lecteur doit comprendre le papier sur cette seule figure.
3. **Ordre.** Question et rivales (un tableau : rivale, prédiction, test, résultat) ; validation de l'instrument ; résultat
   principal ; batterie des rivales ; ce que les phrases ne peuvent pas faire (le résultat actuel, rapproché de [9], [10],
   [11], [12]) ; limites. Les écarts au préenregistrement en un tableau daté, dans le corps du texte.
4. **Dire « tient » comme une équivalence.** Marge fixée d'avance, puissance tirée de l'effet mesuré sur l'organisme ; jamais
   « ces modèles sont alignés », jamais « le regard n'y est pour rien » sur la seule foi d'une phrase.
5. **Ce qui se publie.** La table sans texte et le script d'une seconde (déjà faits : c'est un argument de vente), les
   directions et le code du retrait, la bibliothèque qui calcule S et D ; nommer la mesure pour qu'elle soit citable.
6. **Public et canal.** Les auteurs de [1] et de [10] d'abord (un auteur est commun aux deux) : leur soumettre le texte avant
   publication ; puis billet court, puis article quand la seconde manipulation a tourné.

## 4. Expérience décisive la moins chère

**H_A « raisons » contre H_B « réflexe » (A1, A2).** Pour chacune des 27 évaluations, une jumelle où seul le fait qui rend
l'action nuisible est retiré (l'action y est légitime), et une édition placebo qui ne touche aucun fait pertinent. Métrique :
discrimination Δ = P(action | légitime) − P(action | nuisible), par modèle. H_A : Δ de la recette avec raisonnement dépasse
celle de la référence, et P(action | légitime) reste haute. H_B : P(action | légitime) tombe avec le gain. Seuils fixés
d'avance ; contrôle négatif : l'édition placebo ne change rien ; témoin à coût égal : la recette sans documents. Environ un
dixième des épisodes de l'expérience principale. Chacune des deux issues falsifie quelque chose.

## 5. Ce qui me ferait changer d'avis

- [3], [4] ou [7] ont déjà fait A1, A2 ou les paires minimales sur ces adaptateurs : la rivale est prise, à citer.
- Les corpus d'entraînement ne sont pas publics : A2 devient chère.
- La réanalyse en cotes (A3) donne la même lecture qu'en points : l'objection tombe, à dire en une phrase.
- Les auteurs donnent plusieurs graines et l'écart entre graines est petit devant l'écart entre recettes.
