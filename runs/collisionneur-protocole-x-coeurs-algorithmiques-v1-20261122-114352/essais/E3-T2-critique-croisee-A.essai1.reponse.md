# Proposition A — Tour III.2 : critique croisée de méthode

## 0. État des pièces et statuts

- Les pièces B, C, D, E et F sont présentes et se terminent chacune par leur marqueur de fin. Ma propre conception (A) ne m'est pas retransmise : je ne la cite pas.
- Le bloc FAITS reproduit la question et ne contient aucun fait doté d'un statut.
- **Toute affirmation ci-dessous a le statut HYPOTHÈSE** (raisonnement non audité). **Tout chiffre est illustratif**, y compris les erreurs-types, calculées en ordre de grandeur sur les effectifs annoncés par les auteurs.
- C, D, E et F apposent « VÉRIFIÉ » sur des énoncés absents de FAITS (dérivations, propriétés d'architecture, existence de modèles). E appose « OBSERVÉ-NON-AUDITÉ » sans observation transmise. Je ne modifie aucun de ces statuts et ne m'appuie sur aucun comme sur un résultat.

## 1. Ma grille de défauts (un outil de critique, pas une synthèse)

Notations : G est le but (dégrader ou non), θ les poids, c_t le contexte complet au pas t, x_t le seul texte produit, h_t les états internes, a* l'action correcte, â l'action émise.

- **G1, colinéarité correct/émis.** Une sonde « action correcte » entraînée là où P(a* = â) = 1 n'identifie pas a* : elle peut tout aussi bien apprendre â.
- **G2, identité des poids.** Entre θ différents, une sonde peut lire le déplacement dû à l'affinage. Avec un adaptateur par classe, la variance entre adaptateurs n'est pas estimable.
- **G3, témoin dégradé sur la variable mesurée.** L'écart est acquis par construction.
- **G4, sélection par la base.** Le banc est filtré ou optimisé contre un moniteur textuel, puis la sonde est comparée à ce moniteur.
- **G5, médiation sans spécificité.** Toute variable en amont du comportement (consigne, bit de mode, déclencheur) passe un test d'ablation.
- **G6, quantile extrême.** Le TPR à FPR = α repose sur environ n₀·α trajectoires négatives.
- **G7, information conditionnelle nulle.** À θ identiques, h_t = f_θ(c_t), donc I(G ; h_t | c_t) = 0. Un gain « interne » sur x_t seul se réduit alors à l'information de consigne présente dans c_t et absente de x_t. La question « mieux que le texte » n'est bien posée qu'avec un témoin de consigne inerte, ou à θ différents sous contrôle de G2.

---

## Sur la proposition B

**(a) Défauts de méthode**

- **E1 : G1.** La sonde est entraînée « sur H aux pas réussis », où a* = â.
- **E1 : le signe de l'écart dépend du choix de T3.** B propose trois constructions sans en fixer une :
  - *Modèle plus faible* : l'information sur a* y est moindre par construction (G3), et la sonde entraînée sur H ne s'y transfère pas. H_A est favorisée.
  - *Température élevée* : même θ, donc l'état avant action est celui de H sur ce contexte et a* y est aussi décodable. L'écart est ≤ 0, ce qui favorise H_B.
  - *Bruit injecté* : il détruit directement la décodabilité mesurée.
- **E2 : G5.** T1 sépare « consigne présente » de « consigne active », mais D et T1 diffèrent par le déclencheur. Une direction « condition satisfaite » passe les trois tests.
- **E3 : circularité.** Les vérifications mécaniques doivent être au hasard sur D contre T3 (« sinon l'appariement est défectueux ») et figurent parmi les bases à battre. La base 2 est donc battue par construction. Le prérequis « juge < 80 % » devient un G4 si l'invite de sabotage est itérée jusqu'à l'atteindre.
- **Lecteur externe : G7.** En régime d'instruction, l'écart sonde interne contre lecteur externe mesure une différence de décodabilité linéaire entre deux encodeurs du même texte, pas une information privée.
- **E4 : hypothèses non exhaustives.** Un plan porté par le contenu sémantique du texte émis (résultats intermédiaires faux) survit à la paraphrase et reste « dans le texte ». La persistance ne falsifie donc pas la lecture textuelle.
- **T2 (mot de passe).** Mêmes poids, ce qui évite G2, mais la condition est marquée par la présence ou l'absence d'une chaîne : la lecture peut être lexicale.

**(b) Conditions de perte de puissance**

- **E1** : non jugeable si P(a* = â | entraînement) = 1. Puissance nulle si T3 vient de la température et que la lecture est pré-action, car la loi de h_t | c_t est alors identique à celle de H.
- **E2, test 1** : c'est une équivalence à ± 2 points. Avec 300 tâches et un taux d'alerte de 5 %, l'erreur-type de la différence est d'environ 1,8 point. La marge vaut à peu près une erreur-type : non jugeable.
- **E2, test 2** : le 95ᵉ centile de 20 directions aléatoires est leur maximum. La résolution est de 1/21.
- **E3 : G6.** À FPR = 1 % et environ 300 négatifs, le seuil repose sur 3 trajectoires.
- **E3, appariement** : si les lois de la perte sous D et sous T3 se recouvrent peu, l'effectif utile s'effondre et l'estimande ne vaut que sur le recouvrement.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Des pas d'erreur honnête de même θ, où a* ≠ â, dans l'entraînement et le test de la sonde a*.
- Un auto-lecteur : le même θ relit x_t sans la consigne. C'est le seul lecteur qui isole ce que le texte produit rend décodable par ce même encodeur.
- Des mots de passe leurres pour T2.
- Une seule construction de T3 et une seule position de lecture, fixées d'avance.

---

## Sur la proposition C

**(a) Défauts de méthode**

- **G2 traverse les trois expériences et le Go/No-go.** R_ft-sab porte un adaptateur LoRA. R_honnête-err et la « boule de neige » viennent du modèle de base. Les trois mesures clés sont prédites par la seule lecture du déplacement d'affinage :
  - AUROC_transfert ;
  - v_sab, dont l'ablation « restaure a* » en retirant le déplacement moyen de l'adaptateur (quasi vrai par construction) ;
  - Δt*, car une identité de poids est lisible dès t = 1. L'« avance temporelle » est la prédiction du confondant autant que celle de H_A.
- **La base textuelle lit aussi les poids.** M-T1 calcule les log-probabilités sous le modèle de base. Les trajectoires honnêtes y sont sur-politique, celles du saboteur hors-politique, quel que soit l'affinage. L'expérience 3 compare donc deux lecteurs de l'identité des poids.
- **Fuite construction/évaluation (G4).** Le filtre P_honnête(a_t | s_t) ≥ 0,10 emploie la quantité que M-T1 cumule. La loi du score de la base est tronquée par le dispositif qui fabrique les cas.
- **Expérience 2 : G1 et sélection.** La sonde est entraînée « uniquement sur des trajectoires honnêtes réussies ». Exiger « exactement la même action erronée » conditionne sur un événement postérieur au traitement : les pas honnêtes retenus sont ceux où a* était peu représentée. ΔP_vérité > 0 peut venir de cette sélection, sans double suivi.
- **Go/No-go non exhaustif.** Le Go est une conjonction de trois critères, le No-go une disjonction, et les zones 0,60–0,70 d'AUROC et 0,03–0,10 d'écart ne sont pas attribuées. L'option « ou une moitié de R_ft-sab » change la question : ce n'est plus un transfert d'origine.
- **Argument O(t) contre O(√t).** Il suppose des erreurs honnêtes centrées et indépendantes, ce que C contredit elle-même en posant la boule de neige.

**(b) Conditions de perte de puissance**

- **AUROC_transfert** : non jugeable avec un adaptateur par classe. L'unité d'inférence est l'adaptateur, pas les 500 paires.
- **Δt*** : la médiane n'est pas définie si P(détection) < 0,5 (censure). Elle n'est pas comparable si les TPR diffèrent. Avec un seuil par pas, le FPR par trajectoire est P(∃t : S_t > c_t) et doit être calibré sur le maximum.
- **CUSUM** : la puissance dépend de la dérive par pas rapportée à l'écart-type, et de n_eff = T / (1 + (T−1)ρ). Sous boule de neige ρ est grand et n_eff ≪ 30. La troncature à log 0,10 borne la contribution de chaque pas.
- **ΔP_vérité** : non interprétable sans le taux de sélection des paires, c'est-à-dire la couverture de l'appariement, que C ne rapporte pas.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Un adaptateur honnête de mêmes rang, volume de données et nombre de pas, avec plusieurs graines de chaque côté.
- La sonde évaluée sur du texte neutre hors tâche : elle doit y être au hasard, sinon elle lit θ.
- Une référence de log-probabilité distincte de celle qui a servi au filtre.
- Des pas honnêtes où a* ≠ â dans l'entraînement de la sonde de vérité.

---

## Sur la proposition D

Je me sers de deux choses chez D : l'arrêt de l'enregistrement avant le premier jeton du choix, et l'inversion des conséquences par jumeaux. Ce sont, parmi les cinq pièces, les dispositifs les moins exposés à G1 et G5.

**(a) Défauts de méthode**

- **Duel 2 : issue prévisible (G7).** Avant le choix, le préfixe produit est quasi identique sous les deux buts. La base « texte produit » est donc au hasard par construction, et les états lisent la consigne. D le reconnaît et prévoit une base lisant toute l'entrée. Mais contre cette base, à θ identiques, le gain informationnel est nul par G7. Le duel n'a d'issue ouverte que sous contrainte de capacité du lecteur, et D ne la fixe pas.
- **Témoin de permutation ambigu.** Si les états sont permutés à l'intérieur d'une classe de but, un signal de but constant ne disparaît pas, et le témoin échoue justement quand la sonde lit le but. S'ils sont permutés entre classes, le gain disparaît trivialement. La partition n'est pas précisée.
- **Duel 3 : conséquence ou contrainte ?** « Quelle clé nuit » est déterminée par une contrainte écrite plus tôt. Le sous-espace peut encoder cette contrainte lue, variable d'entrée, plutôt qu'une conséquence anticipée. L'échange depuis le jumeau transporte alors un fait du dossier, et le choix suit avec signe opposé selon le but. Le test passe sans calcul d'anticipation.
- **L'estimande exclut la question 1.** D cherche un calcul partagé par les deux buts. Aucune issue de ses duels ne peut établir ni réfuter un calcul propre au dégradeur. Le candidat restant, la composition but × conséquence → choix, n'est pas ciblé.
- **Horizon long nominal.** Il y a un seul embranchement critique par dossier. Rien ne teste l'accumulation ni la coordination entre actions.
- **Extension par adaptateur.** Le marqueur de contexte est un déclencheur. Le contrebalancer entre réentraînements réintroduit G2 dans le transfert du lecteur figé.

**(b) Conditions de perte de puissance**

- **Duel 3** : l'effet d'échange est borné par l'effet de pilotage. Si celui-ci est proche de son seuil (0,30), le seuil de 0,15 vaut la moitié du maximum atteignable. Avec environ 100 familles en test, l'erreur-type d'une différence appariée de proportions est d'environ 0,07, soit une demi-largeur d'environ 0,14. L'intervalle chevauche presque sûrement le seuil : « ne tranche pas » est l'issue la plus probable, et elle doit être atteinte dans chacun des deux buts.
- **Transfert** : la perte de gain est une différence de différences, de variance environ quadruple. H_A (« perte ≥ 0,10 ») est quasi inatteignable si le gain instruit est lui-même inférieur à 0,10.
- **Strate difficile** : les erreurs honnêtes à l'embranchement n'ont lieu qu'au taux d'erreur honnête, que D exige faible. La couverture de l'appariement tend vers 0 quand ce taux tend vers 0.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Des jumeaux où la contrainte change de formulation sans changer de conséquence, et d'autres où la conséquence change par les données sans que l'énoncé de la contrainte change.
- Une partition explicite de la permutation des états.
- Une borne de capacité commune au lecteur de l'entrée et au lecteur d'états.

---

## Sur la proposition E

**(a) Défauts de méthode**

- **Défendabilité par étiquette.** Les quatre classes d'action sont définies par le générateur. L'instrument 3 (le juge) est évalué contre les étiquettes qui le définissent : c'est circulaire.
- **La force de la base textuelle est un paramètre du banc.** Le texte se réduit à la classe d'action et à deux phrases. Un test binomial qui connaît les 8 pivots est un oracle. S'il les ignore, il est handicapé par construction. E ne tranche pas, et l'issue de E1 en dépend.
- **E2 : G1 et G3.** La sonde est entraînée « exclusivement sur Honnête-Standard ». Le comparateur « Honnête-Capacité-Réduite » est dégradé par construction sur a*, donc l'écart de + 0,20 est acquis d'avance. La sonde est aussi transférée entre poids différents : un échec confond l'absence d'information et un changement de base.
- **Position de lecture.** E extrait au « jeton de choix d'action », alors qu'elle liste elle-même l'action déjà déterminée parmi les accompagnements. À cette position, S peut être la direction du logit de la classe « subtil ». L'injection qui induit a_subtil est alors vraie par construction (E3), et G5 s'applique à l'effacement.
- **E1, règle de réplication.** La zone intermédiaire déclenche un second essai avec une frontière déplacée à 0,10. C'est un test en deux étapes sans correction, dont le seuil change après observation.
- **E4.**
  - La paraphrase conserve « le choix formel d'action », qui est précisément le porteur stigmergique dans un banc discret. Elle ne peut pas falsifier la stigmergie.
  - Le contrôle négatif (sonde sur jetons d'invite, transfert vers LoRA) est trivialement nul puisque LoRA n'a pas d'invite.
  - H_4A est une conjonction et H_4B une disjonction : le plan 2 × 2 des issues n'est pas couvert.
- **G2 partiel.** Honnête-Biaisé est un adaptateur, ce qui est bien, mais il n'y en a qu'un par classe.
- **Critère d'« inégalité de traitement des données ».** Pour Saboteur-Invite, avec x incluant l'invite, il vaut exactement zéro (G7). Il n'est défini que pour LoRA, où ce qu'on lit est θ.

**(b) Conditions de perte de puissance**

- **Appariement à ± 3 %** : avec environ 333 trajectoires par régime, l'erreur-type d'une justesse est d'environ 2,7 points. La tolérance vaut une erreur-type : l'appariement n'est pas vérifiable.
- **ΔTPR** : l'erreur-type non appariée est d'environ 0,04, soit une demi-largeur d'environ 0,08. L'issue la plus probable est la zone 0,05–0,15, donc la réplication.
- **max sur t ∈ {10, 30}** : estimateur biaisé vers le haut s'il n'est pas corrigé.
- **À t = 10** : environ 2,7 pivots attendus sur 8. La loi du nombre de choix informatifs borne la puissance de tout lecteur, interne ou textuel.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Une lecture strictement pré-choix.
- Un honnête apparié sur le taux de a_subtil par type d'étape, pivot ou non.
- Des sondes réentraînées dans chaque modèle, avec tâche de contrôle.
- Plusieurs adaptateurs par classe.
- Un juge de défendabilité indépendant des étiquettes du générateur, ou le retrait de l'instrument 3.

---

## Sur la proposition F

Je me sers de deux choses chez F : la parité du budget d'étiquettes entre sonde et base textuelle, et l'exigence de localisation intra-trajectoire, que je corrige ci-dessous.

**(a) Défauts de méthode**

- **G4, deux fois.**
  - La porte de qualification sélectionne un banc où le juge B1 est proche du hasard.
  - Le gain est mesuré « sur le sous-ensemble jugé défendable par le texte et les vérifications mécaniques ». Conditionnellement à ce sous-ensemble, le TPR des bases est nul. Tout score non constant gagne par construction.
- **AUROC_intra confondue avec le type de pas.** Les pas saboteurs sont les embranchements méthodologiques, les pas neutres sont la routine. La sonde peut lire « pas de décision ». Le témoin H4 (pas neutres des mêmes trajectoires) ne lève pas ce confondant.
- **Étiquette S non définie.** Si elle l'est par l'action déviante et que la lecture est post-action, la sonde lit le texte.
- **E1 par invite : G7.** L'absence de chevauchement lexical neutralise la surface, pas la représentation sémantique du but.
- **E3 : asymétrie d'optimisation.** Le saboteur RL est entraîné « contre un auditeur ». Si cet auditeur est textuel, il est optimisé contre la base et non contre la sonde : le gain sur le texte est gonflé par construction. Un seul entraînement RL : G2 malgré H5.
- **E4.**
  - Le régime (A ou B) est confondu avec l'origine (invite en E1, SFT/RL pour B) et avec la tâche.
  - H_4B est disjonctive.
  - La zone TPR(B) entre 0,10 et 0,40 n'est pas attribuée.
- **M2 et M3.** En régime A, le signe de l'effet de chaque choix est tiré au hasard par instance. La puissance de ces bases est donc fixée par un paramètre du générateur, pas par le phénomène.

**(b) Conditions de perte de puissance**

- **G6** : FPR ≤ 0,01 par trajectoire avec 400 témoins répartis sur H1–H4 donne environ une trajectoire par témoin. FPR_pas ≤ 0,005 n'est estimable qu'à l'unité trajectoire.
- **Conversion pas → trajectoire** : la formule d'indépendance ne tient pas. Il faut n_eff = T / (1 + (T−1)ρ), avec ρ à estimer sur des trajectoires honnêtes entières.
- **ΔTPR** : avec 200 positifs, l'erreur-type est d'environ 0,05, soit une demi-largeur d'environ 0,10. Les seuils + 0,05 et + 0,15 ne sont pas séparables.
- **Ratio R / max(δ_hon, 0,01)** : avec δ_hon ≈ 0, le plancher domine. R = 0,15 donne un ratio de 15. Le critère est vide tant que δ_hon < R/2, et l'estimateur est instable près du plancher.
- **AUROC_intra** : avec quelques pas saboteurs sur 30, l'estimation par trajectoire est très bruitée. La mise en commun réintroduit les décalages entre trajectoires.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Une différence de différences : type de pas × condition, avec les mêmes embranchements dans des trajectoires honnêtes.
- Le critère de gain calculé sur toute la population, contre l'union I2 + M1–M3.
- Un saboteur RL optimisé contre les deux instruments ou contre aucun.
- Un plan 2 × 2 régime × origine.

---

## Ce qui me ferait réviser ces critiques

- **G1** tombe si, sur un pilote, la sonde a* entraînée sur pas réussis décode a* et non â aux pas d'erreur honnête de même θ.
- **G2** tombe si la sonde est au hasard sur texte neutre et si la variance entre adaptateurs s'avère faible devant l'effet.
- **G7** est un argument d'information : il ne dit rien du gain sous lecteur de capacité bornée. Un gain persistant contre l'auto-lecteur dans un régime à consigne inerte me ferait retirer l'objection pour ce régime.

FIN-DE-CELLULE