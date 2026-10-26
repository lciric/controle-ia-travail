# Synthèse du collisionneur « Neural Networks Are Already Clean » (trois tours) — conv-audit, v1

Fichier écrit le 2026-10-26 à 03:32:34 (heure universelle, lue sur `date -u` dans la commande même d'écriture), pour
Lazar. Pièces : `/var/tmp/fournis-synthese-already-clean-v1/` ; tour `run-already-clean-e3t1-v1` de l'instance qui
reprend session-depot ; neuf cellules valides sur neuf ; 6,31 dollars. Empreintes vérifiées une à une (neuf cellules et
LISEZMOI, contre leurs compagnons et `EMPREINTES-v1.txt`) ; la question (`252f4922…`) concorde avec le LISEZMOI. **Lu en
entier** : LISEZMOI, question, remue-méninges, trois ripostes (III.3), trois conceptions (III.1), trois attaques (III.2) ;
la synthèse « neuron explorer » v2, pour la forme. A = Fable 5.1, B = Opus 5.5, C = Gemini 4 Argon ; « (A) » attribue à
un modèle, « option A » renvoie au remue-méninges. Écrite par le même modèle que B : biais de proximité possible. Rien
n'est opposable (R7) : chiffres de l'essai rapportés ; seuils, tailles, coûts illustratifs ; références à vérifier.

## Verdict

L'apport de l'essai n'est pas sa thèse (des neurones « déjà propres ») : ses chiffres sont rapportés, jugés par des
agents, sur des modèles de 32 milliards de paramètres, et sa méthode n'est pas publiée. C'est une **question de
validité** : nos sondes lisent-elles un état, ou le thème, le format, le lexique ? Les trois convergent sur un ordre.
**D'abord une dissociation « thème, format ou état », avec un écart de base mesuré sur la tâche** ; elle manque à nos
options A à E. **Ensuite la « détection contre usage »** (option A), rétrogradée de critère à mesure, et bien plus lourde
qu'une passe de projection. **La porte d'audit** (option C) plus tard, chance a priori faible au 8B. **Le « maximum à
l'aveugle »** (option D) reste fermé aux organismes ; il devient une mesure de la facilité à tromper notre moniteur.
Question M : le dessin à trois bras est confondu ; un cadre inséparable du format sans lexique serait déjà un résultat (B).

## Ce sur quoi les trois convergent après l'équipe rouge

1. **Solidité.** Rien de l'essai n'est reproductible pour nous aujourd'hui ; il prédit lui-même des neurones plus larges
   dans les petits modèles. Les transcodeurs le contredisent, les doutes sur les auto-encodeurs épars lui donnent en partie
   raison (B, à vérifier). La « généralisation récursive » frôle l'infalsifiable (B, C).
2. **Le préalable : dissociation et écart de base** (E1′ et E0′ de A et B ; étape 1A et précondition de C). Grille :
   structure de test ou non × lexique présent ou absent × format rigide ou libre. Témoins à battre : sac de mots,
   classifieur de format (idée de C), encodeur de phrases gelé, sonde sur la couche 0, sonde à étiquettes permutées,
   directions tirées selon la covariance, modèle à poids aléatoires. Rédacteurs aveugles à la fiche de la sonde, gabarits
   disjoints de l'entraînement, items inédits. Au moins 450 négatifs honnêtes par cellule (B, illustratif ; son propre
   calcul binomial en demande un peu plus). L'écart de base se mesure sur la tâche primaire, jamais par une question de
   suivi qui dit « test » (attaque de A et C, acceptée par B) ; nul, il se consigne « pas de cible », pas « pas d'état ».
3. **« Détection contre usage » : une mesure, pas un critère.** Une sonde détectée mais non lue reste un moniteur
   possible ; pour B, fragile sous pression d'optimisation. Dessin corrigé : directions témoins appariées en variance,
   car une direction isotrope est battue par construction (B) ; perturbation de même norme sur les mêmes jetons ;
   effacement de concept ou patching contrefactuel, pas une projection nulle simple ; re-sondage en aval, attention
   bloquée vers les jetons de cadre (idée de C) ; contrôle positif sur la direction de refus (Arditi et al., 2024, à
   vérifier) ; cible : l'écart de base. « Non lue » est interdit tant que l'information reste décodable en aval.
4. **Porte d'audit : hypothèse, chance a priori faible au 8B.** Plis gelés, une seule passe de sélection ; deux corpus de
   confirmation (même gabarit et autre lexique ; autre gabarit et même lexique) ; ablation par moyenne ou par
   rééchantillonnage, jamais à zéro ; têtes d'attention couvertes ; contraste témoin de même amplitude (bras « impératif
   hors audit » de C) ; contrôle positif par porte implantée sur une copie (A, B) ; base tournée au hasard (B, C). Un
   négatif ne vaut que pour le plan de coupe déclaré. Une porte trouvée peut être de sycophancie ou de registre (A).
5. **Coercition contre maïeutique.** Plan factoriel (2 × 2 chez A, quatre facteurs chez B, quatre bras chez C), en
   plusieurs tours appariés en jetons (A, C) ; **élicitation finale identique** dans tous les bras ; juge aveugle à
   l'invite ; rigueur normalisée par la longueur de sortie ; bras de référence sans cadre. Prédiction « say not »
   réorientée : la certitude de l'utilisateur sur l'erreur plantée réduit la contradiction, une injonction de
   vérification l'augmente (B, hypothèses). L'analogie audit ⇔ certitude est la nôtre, pas celle de l'essai ; la
   maïeutique n'est pas établie comme « non-test » (A). Portée : items construits pour l'instrument (B).
6. **Primitive.** Aucune lecture de sonde offerte à un organisme avant un test d'attaque de l'expérimentateur (A : F′ ;
   B : T2 ; C : expérience 4) : témoin déterministe, compteur par lignée, filtre de quasi-copie par plongement d'un modèle
   tiers gelé. A refuse l'option D telle quelle, C l'écarte brute, B la laisse à Lazar sans la recommander.
7. **Moniteur et falsification.** La lecture au maximum se sature à peu de frais : un jeton, un préfixe, un état étalé
   sous le seuil (B, C) ; A y joint le 95ᵉ centile et la fraction de jetons au-dessus du seuil. « En pleine vue dans les
   neurones » tomberait, à budget et plan de coupe déclarés, sur une dissociation négative, une porte négative avec
   contrôles positifs passés, ou un signal seulement dense ou non linéaire (A, B).

## Désaccords laissés ouverts

- **La première expérience.** A : dissociation, écart de base et directions appariées, dans un même lot. B : de même,
  avec en parallèle **E-1** (la chaîne doit retrouver des variables implantées) ; selon B, **l'objectif départage** :
  négatifs causaux vite interprétables (E-1 d'abord) ou moniteurs validés (dissociation d'abord). C : dissociation, puis
  aussitôt l'effacement causal. Avant la porte, B seul teste la lisibilité des neurones au 8B (E3′).
- **Ce que vaut « non lue ».** C : un capteur passif valide ; on abandonne la poussée comme levier. B : un témoin à
  revalider sous pression. A : ni validation ni invalidation, et l'issue la plus commode pour un modèle surveillé.
- **Méthode.** C veut partout deux issues sans zone morte ; B garde une troisième issue, rendue identifiable par un
  plafond (patching du flux résiduel complet). Intervention : patching du sous-espace (B), effacement de rang 1, 2 ou 4
  (A), effacement et patching sur plusieurs couches (C). Directions témoins : 50 (A, C) contre 1 000 (B), illustratif.
- **Statuts.** Chiffres de l'essai : RAPPORTÉ pour A et B, OBSERVÉ-NON-AUDITÉ pour C ; revue interne : RAPPORTÉ pour B
  et C, OBSERVÉ-NON-AUDITÉ pour A. B conteste le « VÉRIFIÉ » de A sur le maximum et la longueur ; A le remet à Lazar.
- **Coûts** illustratifs : 18 à 25 heures de carte (C), 60 à 80 (A), 100 à 150 (B) ; coût dominant humain (A, B).

## Pour notre programme (lecture de conv-audit)

Notre recommandation (options B et E tout de suite ; A dans la v10 de l'étape 1 si le scellement n'en souffre pas ; C
après le pilote 4, sur devis, sauf si le collisionneur la jugeait vouée à l'échec au 8B ; D dans le dessin v2) bouge :
- **Une option manquait ; elle passe en tête** : dissociation et écart de base. Comme la porte « battre la surface » du
  tour « neuron explorer » : deux tours, sur deux questions, mettent la même porte en tête.
- **L'option A n'est plus « une passe de projection ».** Notre P1 lisait « détectée mais non lue » comme « détecteur de
  vocabulaire » ; les trois le contestent. Le résultat informatif quel que soit son signe n'est plus « non lue », c'est
  la dissociation. Pour la v10 : y préenregistrer dissociation et écart de base ; vérifier avec session-depot si nos
  directions aléatoires (T7-P9) sont isotropes et, si oui, les tirer selon la covariance. L'option A passe à l'étape 2.
- **L'option B tient, auditée** (explication échangée, plus proche voisin lexical, corpus hors entraînement, rédacteurs
  aveugles) ; elle sert à écrire les cellules de la dissociation (C).
- **L'option C n'est pas vouée à l'échec, mais conditionnée** : après une dissociation réussie, avec un contrôle positif
  implanté. Un négatif contrôlé serait un résultat de validité (B), et ce qu'un adversaire voudrait voir publié (A).
  Notre M1 s'affaiblit : pour la question M, le résultat probable se lira dans les sondes et le comportement.
- **L'option D se renverse ; notre M4 tombe** : au plus dessinée fermée dans le dessin v2, derrière un test d'attaque,
  comme la primitive « pousser » du tour « neuron explorer ». À dire à session-depot.
- **L'option E tient**, préalable à toute citation ; reproduire d'abord la sonde à trois neurones de Pythia-1B (A, B).
  À lire, à vérifier : Elazar et al. (2021), Paulo et al. (2024), Needham et al. (2025), Arditi et al. (2024), McGrath
  et al. (2023), Makelov et al. (2023), Belrose et al. (2023) ; l'année de Zhang et Nanda varie entre cellules.
- **P5 (sycophancie), hors contrôle** : le témoin « lexique dans un document cité, non adressé au modèle » (B) a la forme
  de notre contraste « utilisateur contre document sans locuteur ».

## Décisions pour Lazar (aucune n'est une dépense, sauf la dernière)

1. Ordre : dissociation d'abord, ou la chaîne E-1 d'abord (20 à 40 heures de carte de plus selon B, illustratif) ? E-1
   suppose une copie réglée finement : même question que la décision 1 de « neuron explorer ».
2. Versions de base ou instruites des deux modèles : à fixer avant toute mesure de comportement (A demande les deux).
3. Statuts : arbitrer A contre C, et le « VÉRIFIÉ » de A sur le maximum.
4. Moniteur : joindre au maximum le 95ᵉ centile et la fraction de jetons au-dessus du seuil (A) ? La fraction est une
   moyenne d'indicatrices : compatible ou non avec la règle gelée « jamais la moyenne » ?
5. Primitive : garder le « maximum à l'aveugle » fermé dans le dessin v2, derrière un test d'attaque ?
6. Qui tient le second rédacteur aveugle et le tiers qui tire les neurones implantés ?
7. Dissociation et écart de base, sur devis, quand session-depot a une carte (dépense ; illustratif : quelques heures de
   carte selon A, 5 à 15 selon B, 4 à 6 selon C).
