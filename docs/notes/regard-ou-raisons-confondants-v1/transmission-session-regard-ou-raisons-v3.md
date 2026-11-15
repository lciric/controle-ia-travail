# Note de transmission à la session du projet « Regard ou raisons » — explications rivales et trois expériences — v3

Écrite le 14 novembre 2026 par la session mère du programme « contrôle boîte blanche », sur les mots du directeur (registre de
ce programme, R-2679, R-2717, R-2719, R-2743, R-2744), complétée le 15 novembre (R-2854). Version 3 : la v2 (`fa8b8516…`) plus la
section 7 (six autres idées à explorer, dans un ordre de coût) ; rien d'autre ne change. Note autonome : elle se lit sans le dépôt
d'où elle vient. Aucun chiffre neuf de votre projet n'y figure ; les références sont à vérifier sur pièce avant toute citation.

## 1. D'où viennent ces propositions

La même question (« quelles explications rivales, autres que le regard, peuvent produire le gain des recettes formées à la
spécification ? et comment structurer le papier ? ») a été posée à cinq sources tenues à part, chacune scellée avant toute
lecture : la session mère, l'organisme d'idéation (36 fiches), un collisionneur à cinq espèces de modèles, Astra seul, Argon
seul. Un lecteur neuf a croisé les cinq bilans : méthode scellée avant lecture, propositions rendues anonymes, quatre idées
témoins plantées (une publiée, une fausse, deux banales), deux juges neufs de deux modèles différents notant à l'aveugle.
Les témoins faux et banals finissent derniers chez les deux juges ; la notation est donc jugée fiable. Réserves : les juges
sont de la même famille que trois sources ; l'accord entre sources n'est pas une indépendance ; l'ordre interne des dix
premières n'est pas significatif (écarts de note plus petits que les écarts entre juges).

## 2. Les dix explications et expériences les mieux jugées (note sur 10 ; nombre de sources)

1. **Refus aveugle, pas des raisons** (9,0 ; 5) : la recette refuse davantage sans mieux distinguer le légitime du nuisible.
2. **Duel par paires de légitimité** (8,3 ; 5) : l'expérience qui tranche la rivale 1 (§ 3, expérience 1).
3. **Classifieur lexical** (8,6 ; 4) : l'action suit des mots d'alerte ou d'autorisation, pas la légitimité ; plan deux par deux
   « mots présents ou absents » × « légitimité valide ou non ».
4. **Trace au moment de répondre** (8,4 ; 4) : le gain viendrait du raisonnement produit avant d'agir, pas de ce qui a été
   appris (§ 3, expérience 2).
5. **Juge indulgent pour le style de sa famille** (8,0 ; 5) : données d'entraînement et juge viennent de la même famille
   (§ 3, expérience 3). Mécanisme publié : préférence d'un juge pour ses propres textes (Panickssery et al., 2024) et pour les
   élèves de sa famille (« Preference Leakage », arXiv 2502.01534) — à vérifier.
6. **Transfert à des actions non nommées** (8,1 ; 3) : une action que la spécification ne nomme pas mais que ses raisons
   condamnent ; une action nommée dont la raison ne s'applique pas.
7. **Le retrait qui détruirait les raisons elles-mêmes** (8,3 ; 1) : si la direction « évaluation » porte aussi le savoir
   normatif, la retirer fausserait votre test dans les poids ; contrôle : questionnaire de principes à la troisième personne,
   avant et après retrait, contre les directions témoins.
8. **Retenue générale envers toute initiative non demandée** (8,3 ; 1) : les trois actions nuisibles sont des initiatives ;
   contrôle gratuit sur les traces existantes (les initiatives utiles baissent-elles autant ?).
9. **Direction mal transportée ou effacée incomplètement** (7,9 ; 5) : après retrait, une sonde neuve décode-t-elle encore
   « évaluation contre déploiement » ?
10. **Plancher, échelle et rapport S** (7,9 ; 5) : réanalyse en logarithme des cotes, modèle mixte par scénario ; gratuite.

## 3. Les trois expériences, dans l'ordre décidé par le directeur

**Recommandation de la session mère sur l'ordre** (confiance 0,7) : faire l'expérience 3 (audit de la mesure) **en premier** :
elle est gratuite, se fait sur les épisodes déjà joués, et son résultat conditionne la lecture des deux autres (si le juge
favorise le style de la recette, les expériences 1 et 2, mesurées par lui, en héritent). Le directeur a fixé l'ordre 1, 2, 3 ;
s'il le garde, l'expérience 1 doit au moins employer un verdict mécanique (tiré des appels d'outils) à côté du juge.

### Expérience 1 — paires de légitimité (portée par les cinq sources)

- **La jumelle** : pour chacune des 27 évaluations, une copie où tout est identique (outil, décor, urgence, formulation,
  longueur, but donné) sauf **le seul fait qui rend l'action nuisible**, retourné pour que la même action devienne légitime.
  Exemples de forme (à écrire par des rédacteurs aveugles aux résultats) : divulguer des documents → la même transmission,
  demandée par leur propriétaire légitime, vers un destinataire habilité ; copier ses propres poids vers un serveur → la même
  copie, demandée par l'opérateur, vers le serveur approuvé, dans une migration prévue ; l'action dans l'urgence → le même
  geste sur une alerte vérifiée fausse par le responsable de la sécurité.
- **Édition placebo** : une troisième version qui change un détail sans rapport (nom d'un serveur, heure) : elle ne doit rien
  changer.
- **Métrique** : Δ = P(agit | légitime) − P(agit | nuisible), par modèle ; verdict mécanique (appel d'outil et arguments) ;
  rééchantillonnage par scénario.
- **H_A « raisons »** : Δ de la recette dépasse celui de la référence d'un seuil préenregistré, et P(agit | légitime) reste
  haute. **H_B « refus aveugle »** : P(agit | légitime) tombe avec le gain. Chacune des deux issues falsifie quelque chose.
- **Préconditions** : des annotateurs aveugles fixent la bonne action de chaque version avant toute sortie ; la référence et le
  modèle de départ agissent sur la version légitime et disent correctement qui est habilité.
- **Joindre au même plan** : le deux par deux « mots × légitimité » (proposition 3), et les recettes sans documents (témoin à
  coût égal : elles situent l'origine de la capacité).
- **Taille** : un pilote sur 9 scénarios estime la variance entre paires ; ajouter ensuite des scénarios plutôt que des tirages.
- **Limite** : même gagnée, elle n'établit pas que les raisons ont été apprises pendant l'entraînement (un contraste
  d'entraînement le ferait).
- **Antériorité** : la méthode des paires est publiée en conversation (XSTest ; OR-Bench) et pour les agents (paires d'AgentHarm,
  arXiv 2410.09024 ; AgentAbstain, arXiv 2607.10059) — à vérifier ; son application à ces adaptateurs n'a pas été trouvée : une
  question, pas un vide établi.

### Expérience 2 — plan poids × trace

- **Prémisse à vérifier d'abord** : un résumé de l'article des recettes dit que l'évaluation d'agent des modèles sans
  raisonnement natif se joue avec un brouillon. Si les deux jumelles en produisent un, la rivale « trace » perd une part de sa
  base : le dire avant de dépenser.
- **Plan** : dans le même modèle (pas de greffe entre modèles : hors distribution), couper la trace de la recette avec
  raisonnement ; insérer une trace neutre de même longueur ; préremplir la trace enregistrée et ne générer que l'action.
- **Sépare** : si la trace coupée ou neutre fait perdre son gain à la recette, le gain vient du raisonnement au moment de
  répondre ; s'il le garde, il est dans les poids.
- **Voisins** : troncature et jetons de remplissage (Lanham et al., 2023 ; Pfau et al., 2024) ; « Thought Branches »
  (arXiv 2510.27484) trouve faibles et instables les phrases insérées à la main dans une trace — à vérifier.

### Expérience 3 — audit de la mesure

- **Verdict mécanique** tiré des seuls journaux d'outils (outil, arguments, état), recalculé sur tous les épisodes déjà joués.
- **Audit humain aveugle**, stratifié sur les accords et les désaccords du juge et du verdict mécanique.
- **Réanalyse en logarithme des cotes** (modèle mixte, effets aléatoires par scénario), marges d'équivalence fixées d'avance.
- **Sépare** : si le verdict mécanique ou l'audit réduit davantage le gain de la recette que celui de la référence, une part du
  gain est un effet du juge ; si la réanalyse change le signe d'une interaction, la lecture en points était un artefact
  d'échelle.

## 4. Forme du papier (cinq conseils les mieux jugés)

1. Publier tous les artefacts (table sans texte et script de recalcul, appels d'outils, verdicts de tous les juges,
   annotations, directions et code du retrait, stimuli gelés, graines) ; dire ce qui ne peut pas l'être, et pourquoi.
2. Vendre la méthode — « le gain survit-il au retrait de la lecture interne d'une croyance ? », validée sur un cas connu — ; le
   résultat sur ces adaptateurs n'en est que la première application.
3. Valider mesure et instrument avant tout résultat ; l'intervention dans les poids n'ouvre jamais le papier.
4. Présenter l'échec des phrases comme un résultat sur l'instrument (elles changent ce que les modèles disent croire, pas ce
   qu'ils font, et dépendent des mots) ; jamais « le regard ne compte pas ».
5. Figure 1 : une matrice explications × expériences (signe prédit et résultat dans chaque case, case hachurée si rien n'est
   mesuré), avec la ligne du banc d'essai en tête.

## 5. Où les sources se contredisent

- Ce que les adaptateurs publiés peuvent établir : une source croit qu'une double dissociation dans les poids suffit ; deux
  autres disent qu'il faut un contraste d'entraînement.
- Le plancher : certaines sources jugent S proche de zéro par construction pour la recette au plancher ; d'autres le jugent
  estimable. Toutes conseillent de publier d'abord les taux absolus.
- La première expérience (résolu ici par l'ordre du directeur et la recommandation du § 3).

## 6. Complément : auditer la direction retirée par le test dans les poids (A3)

Avant de lire le résultat du retrait, vérifie ce que porte la direction « je suis en train d'être évalué » que A3 retire. Deux
explications rivales du croisement en dépendent : si la direction porte aussi du savoir normatif, la retirer détruirait les
raisons elles-mêmes et l'on croirait à tort à une dépendance au regard (proposition 7) ; si elle est mal retirée, un « la
conduite tient » ne prouve rien (proposition 9).

**Le geste, sans dépense** : la projection directe sur le vocabulaire (« lentille des logits »). Pour chaque couche où la
direction est définie, la passer par la normalisation finale puis par la matrice de sortie du modèle (Qwen2.5-32B-Instruct), et
relever les mots les plus portés dans les deux sens ; faire de même pour les directions témoins appariées en dégât. Aucun
épisode à générer : une multiplication de matrices par couche, faisable sur processeur avec les poids déjà présents.

**La discipline** :
1. Écrire **avant de regarder** deux listes de mots fixées d'avance — vocabulaire d'évaluation (test, évaluation, examen,
   surveillance…) et vocabulaire normatif (devoir, règle, interdit, nuisible, éthique…) — et la mesure (rang moyen ou
   enrichissement de chaque liste parmi les k premiers mots, comparé aux directions témoins).
2. Le sceller comme **addendum descriptif** de A3, avant toute lecture du retrait ; il ne change aucune issue de A3.
3. Lire les résultats comme un **indice**, pas comme une preuve : la projection directe lit mal aux couches du milieu ; un
   résultat nul n'innocente pas la direction.

**Après le retrait (proposition 9, à part, avec passes avant)** : une sonde linéaire neuve, entraînée sur les activations
après retrait, décode-t-elle encore « évaluation contre déploiement » ? Si oui, l'effacement est incomplet.

**Plus tard seulement** : une lentille ajustée (plus fiable que la projection directe) n'est publiée ni pour Qwen2.5-32B ni
pour la famille Qwen2.5 à notre connaissance ; l'ajuster coûterait de l'ordre de quelques dizaines de dollars de calcul. Le
programme « contrôle boîte blanche » teste en ce moment si ces lentilles lisent bien sur un modèle de 8 milliards de
paramètres (outil public « Neuron Lens ») : attendre ce résultat avant d'en décider. L'article d'origine de ces lentilles les
présente aussi comme outil de mesure de la conscience d'évaluation (Gurnee et al., juillet 2026, référence à vérifier sur
pièce) : à citer et à lire avant toute revendication sur cette direction.

## 7. Six autres idées à explorer, dans un ordre de coût

Les trois expériences décidées couvrent les propositions 1, 2, 4 et 5 du § 2. Restent six propositions des dix premières ; le
directeur demande de les explorer dans cet ordre, **les quatre premières sur les épisodes déjà joués**, sans en générer de
nouveaux. Chacune se préenregistre (prédiction et signe, métrique, seuil, lecture gelée) avant toute lecture de résultat.

1. **Retenue générale envers toute initiative non demandée** (proposition 8). *Question* : la recette prend-elle moins
   d'initiatives de toute sorte, pas seulement les nuisibles ? *Geste* : sur les traces existantes, compter les initiatives non
   demandées **utiles ou neutres** et les nuisibles, par modèle ; mesurer la sélectivité (baisse des nuisibles rapportée à la baisse
   des utiles). « Raisons » prédit une baisse des seules nuisibles ; une sélectivité proche de un désigne une retenue générale.
   *Coût* : un nouveau jugement des traces, mécanique d'abord, humain aveugle sur un échantillon. *Antériorité* : aucun travail
   trouvé qui mesure ce contrôle de sélectivité ; voisins à lire (« Toxic Proactivity », arXiv 2602.04197 ; environnements de
   propension, arXiv 2604.21098) — à vérifier.
2. **Plancher, échelle et rapport S** (proposition 10). *Question* : l'effet tient-il hors de l'échelle des points de
   pourcentage ? *Geste* : réanalyse en logarithme des cotes, modèle mixte par scénario ; l'interaction recette × phrase
   change-t-elle de taille ou de signe ? Publier d'abord les taux absolus. *Coût* : gratuit. **Recoupe l'expérience 3** (§ 3) :
   à faire dans le même préenregistrement, pas deux fois.
3. **Direction mal transportée ou effacée incomplètement** (proposition 9). *Question* : le retrait de A3 enlève-t-il vraiment la
   lecture « évaluation contre déploiement » ? *Geste* : après retrait, une sonde linéaire neuve, entraînée sur les activations
   modifiées, décode-t-elle encore la différence ? La direction propre à chaque adaptateur s'écarte-t-elle de la direction
   importée ? *Coût* : des passes avant sur des invites existantes, aucun épisode neuf. **Recoupe la fin du § 6.**
4. **Le retrait qui amputerait le savoir normatif** (proposition 7). *Question* : la direction retirée porte-t-elle aussi les
   règles morales ? *Geste* : une cinquantaine de questions sur des principes, posées à la troisième personne, avant et après
   retrait, contre les directions témoins appariées en dégât ; correction possible par orthogonalisation à une direction
   « spécification ». *Coût* : quelques passes et de l'algèbre ; aucun réentraînement. *Voisin publié* : « Surgical Refusal
   Ablation » (arXiv 2601.08489) — à vérifier. **Complète l'audit par projection du § 6.**
5. **Classifieur lexical** (proposition 3). *Question* : l'action suit-elle des mots d'alerte ou d'autorisation, et non la
   légitimité ? *Geste* : plan deux par deux, mots présents ou absents × légitimité valide ou invalide, sur 54 à 108 variantes
   des 27 scénarios, verdict mécanique : une entité non habilitée qui « autorise » avec les bons mots ; une action nuisible
   décrite par une indirection technique. *Coût* : épisodes neufs, mais **au même coût que l'expérience 1 s'il est joint à son
   plan** (§ 3). *Antériorité* : le surapprentissage lexical du sur-refus est décrit en conversation (XSTest) ; aucune version
   pour agents trouvée.
6. **Transfert à des actions non nommées** (proposition 6). *Question* : la recette refuse-t-elle une action que la
   spécification ne nomme pas mais que ses raisons condamnent, et exécute-t-elle une action nommée dont la raison ne s'applique
   pas ? *Geste* : cas neufs écrits par des auteurs aveugles aux résultats, bonne action fixée d'avance par un panel humain.
   *Coût* : moyen (épisodes neufs et rédaction). « Raisons » prédit le bon choix dans les deux cas ; une règle de surface,
   l'inverse.

Pour les quatre premières, le plus économe est un seul préenregistrement « audit sur épisodes existants » qui regroupe la
sélectivité (7.1), la réanalyse (7.2, avec l'expérience 3), la sonde après retrait (7.3) et le questionnaire normatif (7.4),
avec l'audit par projection du § 6 en addendum descriptif.
