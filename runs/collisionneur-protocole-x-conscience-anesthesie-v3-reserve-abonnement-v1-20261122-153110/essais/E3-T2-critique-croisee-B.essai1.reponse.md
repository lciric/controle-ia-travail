# Proposition B : tour III.2, critique croisée de méthode

## État des pièces

- J'ai lu en entier les blocs FAITS et QUESTION, qui ont le même texte et la même empreinte, ainsi que les pièces A, D, E et F. Chacune se termine par FIN-DE-CELLULE. Statut : VÉRIFIÉ par lecture.
- La pièce C est absente (statut REFUS). Je n'en invente rien.
- **Conventions.** Ce que je dis du contenu des pièces est VÉRIFIÉ par lecture. Mes critiques et les conditions que je pose sont des HYPOTHÈSES. Je ne modifie aucun statut posé par un auteur. Tous les nombres de cette cellule sont **illustratifs**, y compris ceux que je recalcule à partir des seuils illustratifs des autres propositions. Seul le nombre de tâches (six) vient des faits.
- E et F marquent VÉRIFIÉ des énoncés absents des pièces transmises, par exemple la longueur des sorties « dans les protocoles standards », le corpus d'OLMo, ou des références « vérifiées » de mémoire. Je ne change pas ces statuts. Je signale seulement que je ne peux pas les auditer à partir de ce qui m'a été transmis.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **D2 ne sépare pas une partition « privilégiée » d'une partition simplement alignée sur la fragilité des tâches.** Supposons que la thèse de B soit vraie. Alors la partition des faits est celle qui place les trois tâches les moins fragiles du côté « gardé ». Toute recherche menée à budget égal la servira mieux que les 19 autres partitions, et le rang 1 est attendu sous B comme sous A. H_A2 et H_B2 s'excluent entre elles, mais elles ne départagent pas les deux thèses en jeu. D2 a besoin d'une référence : le rang de la partition des faits sous les témoins T1 à T4, sans recherche ciblée.
2. **Aucun témoin positionnel.** T1 à T4 ne comprennent pas de troncature de la portée d'attention. Je reprends ici l'argument de E (point 6) et de F (C5). Une direction qui porte le routage à longue distance :
   - épargne les tâches dont l'indice est local ;
   - casse celles qui relient des segments éloignés ;
   - bouge peu une divergence moyenne, qui est dominée par le contexte proche.

   Elle battrait donc T1 à T4 sans qu'il existe le moindre « régime ».
3. **T5 peut être choisi d'après le profil.** T5 est « désigné par les tenants de B, ajouté tel quel ». Si B le désigne en connaissant la batterie, par exemple en supprimant un trait de langue cible, l'équivalence est obtenue par construction. C'est le symétrique exact de la circularité que A redoute pour ses propres directions.
4. **Fuite possible au calibrage de D′.** Le lot sur lequel la dichotomie fixe la dose n'est pas indiqué. Si c'est S2, la dose est réglée sur l'échantillon qui sert à évaluer. De plus, apparier les items sur la marge du modèle intact retient, côté « perdues », les items résolus avec assurance. Ceux-ci le sont peut-être par un raccourci, ce qui dilue la fonction visée.
5. **D égal n'est peut-être pas atteignable.** Retirer un sous-espace aléatoire de rang k avec α ≤ 1 peut ne jamais atteindre le D des directions ciblées. Il faut alors soit dépasser α = 1, ce qui revient à une réflexion, donc à une injection, soit changer k. Le plan ne dit pas laquelle des deux voies il suit.
6. **Contrôles vrais par construction.** « Impulsion nulle, indice 0 » et « retirer puis remettre, 0 % » vérifient le code, pas l'inférence. Le contrôle positif « langue de sortie » a un effet sans commune mesure avec le seuil de 0,10 : il ne dit rien de la puissance au seuil.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **L'équivalence est hors d'atteinte.** L'issue B demande que IC95 % ⊂ [−0,05 ; +0,05]. C'est possible seulement si 1,96·SE(ΔŜ) < 0,05 − |ΔŜ|.
  - Hypothèses de calcul : 300 items par tâche, discordance appariée π_d ≈ 0,2 (perdues) et 0,08 (gardées), dénominateur intact − plancher ≈ 0,55.
  - On obtient SE ≈ 0,03 (illustratif), donc 1,96·SE ≈ 0,06 > 0,05 : la condition échoue même si ΔS = 0.
  - Il faudrait environ 1 300 items par tâche (illustratif).
- **Union sur les témoins.** La règle de B porte sur « au moins un témoin ». Sans correction, le risque de conclure à tort à l'équivalence monte jusqu'à m·α, avec m = 5. La règle de A, qui exige tous les témoins, reste au niveau α, mais sa puissance est le produit des puissances individuelles.
- **La loi nulle du rang dans D2 n'est pas uniforme.** Une loi uniforme sur {1, …, 20} suppose les partitions échangeables. Or elles partagent des tâches et vont par paires complémentaires. Sous le modèle r_t = 1 − β·f_t + ε_t (f_t : fragilité de la tâche t), le rang de la partition alignée sur f tend vers 1 quand Var(ε)/β² → 0. Si f est commun aux trois modèles, P(rang 1 partout) ne vaut pas (1/20)³ : elle tend vers la probabilité pour un seul modèle.
- **Un KL moyen égal n'apparie pas les pertes.** Sur un item de marge m, P(erreur) = P(ξ > m), où ξ est le déplacement des logits. Cette probabilité dépend de toute la loi de ξ (variance, queue, position), pas seulement de sa moyenne.
- **Tolérance de 5 %.** Si le coefficient de variation de D̂ entre rééchantillonnages du corpus neutre dépasse 5 %, l'appariement se fait dans le bruit.
- **« Deux modèles sur trois ».** Avec trois modèles, la variance entre modèles n'est pas estimable : la règle devient un vote sans loi d'erreur.

### (c) Contrôles négatifs dont l'absence serait fatale

- Présents : témoin contre témoin ; étiquettes permutées dans S1.
- Manquants :
  1. une troncature de la fenêtre d'attention à D égal ;
  2. un T5 désigné sans accès à la batterie ni aux étiquettes ;
  3. le rang de la partition des faits sous les témoins non ciblés.

---

## Sur la proposition C

Pièce absente (REFUS, décision de l'arbitre) : rien à critiquer, et je n'en reconstitue rien.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Aucun nul de sélection.** Les douze témoins sont « tirés sans étiquettes de tâche » : ils estiment la loi d'un sous-espace non sélectionné. Les directions ciblées, elles, ont été sélectionnées pour produire le profil, que ce soit par les auteurs ou par réapprentissage. Dès que le modèle porte des traits propres à certaines tâches, ce que je tiens pour probable (HYPOTHÈSE), « ciblé > témoin » est attendu sous A comme sous B : on compare un maximum à une moyenne. Seul le D2 de A vise ce point.
2. **Le croisement porte sur la longueur produite, pas sur la distance.** Les « extractions longues et traductions courtes » visent la longueur de génération. La distance, dans l'entrée, entre les éléments à relier n'est pas croisée. La myopie positionnelle relevée par E et F n'est donc pas écartée.
3. **L'aveugle des juges peut tomber de fait.** Une sortie dégradée porte souvent une signature (répétition, troncature, mauvaise langue) qui révèle la condition au juge.
4. **Les points de pourcentage ne sont pas normalisés** par l'écart entre intact et hasard. Une bande de ±3 points n'a pas la même exigence pour une tâche à 95 % et pour une tâche à 60 %.
5. **Contrôle vrai par construction.** Une projection d'intensité nulle est l'identité : elle ne teste que le code.
6. **Même problème de faisabilité qu'en A** pour atteindre la perte commune avec une intensité ≤ 1.
7. **Plancher probable sur Pythia-1.4B** pour le raisonnement à plusieurs sauts et la traduction (HYPOTHÈSE ; A fait la même réserve).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Effectif nécessaire pour H_B.** Conclure |e_j| ≤ δ = 0,02 simultanément sur six fonctions demande n ≳ (z_{1−α/12} + z_{1−β/2})²·σ_d²/δ².
  - Avec σ_d² ≈ 0,15, α = 0,05 et β = 0,2, on trouve n ≈ 5 800 items par fonction (illustratif), contre 300 prévus.
  - D le prévoit (« renoncer au verdict B »). Mais sans hausse de budget à cet ordre, le plan ne peut conclure qu'à A ou à l'indécision.
- **Hétérogénéité des témoins.** Avec 12 sous-espaces, SE(d̄_témoin) ≥ τ/√12, où τ est l'écart-type entre sous-espaces. Si τ > δ·√12/z, la bande de B est hors d'atteinte quel que soit le nombre d'items.
- **Une notation bruitée fabrique une issue B.** Si la grille binaire a une sensibilité Se et une spécificité Sp non différentielles, la différence observée vaut (Se + Sp − 1) × la vraie. L'atténuation pousse les e_j dans la bande de B.
- **Colinéarité.** Si la corrélation ρ entre longueur et fonction reste forte dans l'échantillon d'items, la variance de l'effet « fonction » est multipliée par 1/(1 − ρ²).
- **Plancher.** H_A n'est atteignable pour une fonction j que si p_j(intact) − p_hasard > 5 points + z·SE.

### (c) Contrôles négatifs dont l'absence serait fatale

- Présent : panels témoins comparés entre eux.
- Manquants :
  1. un nul de sélection à budget de recherche égal ;
  2. une troncature de la portée d'attention à perte égale ;
  3. la mesure du taux auquel les juges devinent la condition à partir des sorties.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **L'extraction de U_A n'est pas spécifiée** : ni méthode, ni données. Les 500 paragraphes sources servent aux six tâches, et aucun partage entre découverte et test n'est décrit. On ne peut donc pas exclure une fuite entre construction et évaluation. Conséquence : l'issue « ni A ni B (i) » réfute l'extraction faite par E, pas A.
2. **C_synt est probablement extrait des tâches locales de la batterie.** Son inversion de signe sur l'IDS est alors obtenue par construction. L'exiger dans le critère de succès de A n'apprend rien sur U_A.
3. **C_orth « mis à l'échelle ».** Au-delà de α = 1, h − α·Ph inverse la composante : le témoin injecte au lieu de supprimer. L'opération et le sous-espace sont alors confondus.
4. **L'ordre de perte ne discrimine pas.** « Trois sauts avant deux, puis résumé et traduction » est l'ordre de difficulté, que la fragilité de B prédit aussi. Il en va de même pour la concordance τ_K entre graines.
5. **Comparaison sigmoïde contre linéaire.** Sans pénalité ni validation hors échantillon, le modèle qui a le plus de paramètres s'ajuste mieux par construction.
6. **La référence humaine est confondue avec le rival que E nomme lui-même.** Le contraste « surprise narrative longue contre surprise lexicale locale » sera reproduit par toute myopie positionnelle. Or C_fenêtre n'y est pas appliqué.
7. **Dans I-E, l'étiquette est confondue avec la molécule.** Le contraste principal oppose propofol et kétamine : un indice qui suit la pharmacologie passerait le critère. De plus, les étiquettes sont des rapports, pas un vécu établi indépendamment.
8. **H_KV est garanti par l'architecture.** Si des clés et valeurs perturbées restent dans le cache, l'écart persiste nécessairement. Une valeur non nulle n'informe pas sur un état.
9. **Identification en double aveugle (point 5).** Reconnaître U_A par n'importe quel trait ne teste pas le profil. La statistique d'identification doit être le profil préenregistré.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Test de forme sans niveau.** Sous H_B,dyn (forme linéaire), le paramètre d'inflexion n'est pas identifié. Le rapport de vraisemblances ne suit donc pas un χ² standard (problème de Davies). Sans loi nulle simulée, le seuil n'a pas de niveau.
- **Équivalence.** Le test TOST à α = 0,01 dans ±0,08 n'aboutit que si 2,33·SE(ΔAUDC) < 0,08 − |ΔAUDĈ|. Le critère ponctuel |ΔAUDC| ≤ 0,05 s'ajoute à cette condition.
- **Interpolation.** ΔAUDC intègre en ΔL des courbes mesurées en α, sur des grilles qui diffèrent selon les conditions. L'erreur d'interpolation croît avec la courbure et l'écart entre paliers.
- **Biais du maximum.** Pour deux normales i.i.d., E[max(X₁, X₂)] = μ + σ/√π. Prendre le maximum des deux témoins crée un biais contre A, de l'ordre de l'erreur-type des moyennes témoins.
- **I-E.** Une sensibilité observée de 0,90 sur quelques dizaines de sujets garde une borne basse d'IC binomial sous 0,8 (illustratif).

### (c) Contrôles négatifs dont l'absence serait fatale

1. Un partage entre extraction et évaluation, avec extraction sur étiquettes permutées.
2. Un témoin contre témoin.
3. Pour I-E, des contrastes à molécule constante.
4. C_fenêtre appliqué aussi à la comparaison humaine.

---

## Sur la proposition F

### (a) Défauts de méthode

1. **La porte de réplication sélectionne sur le profil.** V_cible n'est retenu que si ΔS_int ≥ 0,30 et ΔS_loc ≤ 0,10, après jusqu'à quatre essais (deux méthodes × deux échelles). L'expérience 1 compare ensuite ce maximum à des moyennes de sous-espaces aléatoires : la victoire contre C1 à C3 est donc attendue par construction. C4 teste une double dissociation ; ce n'est pas un nul de sélection.
2. **La table des issues est incohérente.**
   - « Profil identique sous C5 » est compté pour B. Or C5 est une intervention ciblée, pas la « dégradation globale égale » que B prédit.
   - La disparition du profil en régime apparié est classée « ininterprétable » tout en étant présentée comme « donnant raison à B ».
   - Une victoire de H_B,emp réfuterait A « a fortiori conceptuellement ». Mais la thèse conceptuelle n'est pas mesurée, et d'autres directions que V_cible restent possibles.
3. **C2 par température n'est pas un témoin.** En choix forcé noté par argmax, l'exactitude ne change pas avec la température. C2 élève ΔL_cal sans toucher ΔS.
4. **Fuite possible au calibrage.** La phrase « calibrés avant la mesure sur D_test » est ambiguë. Si D_test sert au réglage, il y a fuite. Par ailleurs, la sensibilité « à ΔS̄ égal » apparie sur une grandeur tirée du résultat.
5. **Appariement triple.** Exactitude dans [0,75 ; 0,85], marge à ±0,25 nat, longueur à ±10 % : les items « int » retenus sont ceux que le modèle intact résout avec assurance, peut-être par raccourci local.
6. **q(x) hérite du contraste d'extraction.** Comme V_cible est extrait par le contraste int/loc, la loi de q diffère entre les deux blocs par construction. Le taux d'alerte sur les items B_loc réussis est donc fixé par l'extraction et le seuil, pas par un état. Le critère H_A3 tranche mécaniquement.
7. **L'ordre préenregistré de l'expérience 2** est celui de la profondeur compositionnelle, que la fragilité prédit aussi. Seuls Δτ et ρ discriminent.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **L'équivalence est hors d'atteinte.** Avec 200 items par tâche, SE(D̂_spec) ≈ 0,04 (illustratif). La condition 1,645·SE < 0,05 − |D̂| est alors impossible même si D_spec = 0. B ne peut gagner que par la clause C5, qui ne lui revient pas (voir a2).
- **ρ n'est pas estimable.** Sous H_A, ED50_loc est censuré à droite, donc ρ n'est pas défini. Et le rapport ρ_cible/ρ_témoin a des queues lourdes quand les pentes sont faibles (problème de Fieller).
- **τ de Kendall sur cinq niveaux.** τ ne prend que des valeurs multiples de 0,2.
  - « τ ≥ 0,70 » équivaut à au plus une inversion : P = 5/120 sous un ordre aléatoire.
  - « τ ≥ 0,60 » équivaut à au plus deux inversions : P = 14/120.
  - Si l'ordre de difficulté est commun aux humains et aux modèles, ces probabilités tendent vers 1 pour tout témoin.
  - Avec une dizaine de modèles témoins (illustratif), un taux de fausses alertes observé de 1/10 a un IC d'environ [0 ; 0,45] : le critère « ≤ 10 % » n'est pas jugeable.
- **Porte de réplication.** Si chaque essai passe avec une probabilité q sans mécanisme spécifique, la probabilité de passer en quatre essais vaut 1 − (1 − q)⁴.
- **Effectif après appariement.** L'effectif retenu est proportionnel à la masse du recouvrement des lois de marge entre les deux blocs.
- **Union sur C1 à C3** pour l'issue B : même inflation qu'en A.

### (c) Contrôles négatifs dont l'absence serait fatale

1. Un nul de sélection : même extraction et même porte sur des étiquettes permutées ou des partitions arbitraires. C'est l'idée du D2 de A, et son absence est fatale vu le point a1.
2. Un témoin contre témoin appliqué à la règle de verdict.
3. Des items contrefactuels où la réponse par raccourci diffère de la réponse à plusieurs sauts.
4. Un C2 qui modifie réellement l'exactitude.

---

## Antériorité

- Lu dans cette session : seulement les pièces transmises.
- Cité de mémoire, sans relecture ici :
  - Kriegeskorte, Simmons, Bellgowan et Baker, 2009, « Circular analysis in systems neuroscience: the dangers of double dipping » ;
  - Schuirmann, 1987, « A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability » ;
  - Davies, 1977, « Hypothesis testing when a nuisance parameter is present only under the alternative » ;
  - Fieller, 1954, « Some problems in interval estimation ».
- Travaux de 2026 : référence à vérifier.

FIN-DE-CELLULE