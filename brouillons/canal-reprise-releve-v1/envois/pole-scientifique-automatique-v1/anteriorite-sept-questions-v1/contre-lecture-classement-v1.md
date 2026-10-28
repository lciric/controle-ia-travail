<!-- Contre-lecture rendue par un sous-agent neuf, modèle Opus (auteur du classement : Fable 5.1), 28 octobre 2026, R2. Versée telle quelle, sans modification. -->

# Contre-lecture du classement motivé des sept questions et de la question-pont (v1)

J'ai lu les dix fichiers en entier. Je n'ai fait aucune recherche web et je n'ai rien écrit dans le dépôt. Les numéros de ligne renvoient aux fichiers du dossier.

**Verdict : scellable après corrections.** Le classement reprend correctement les verdicts (huit fois « semi-occupé ») et les niveaux de confiance des huit rapports. En revanche, la colonne « attaquable », le traitement de Q3 et la motivation de l'ordre recommandé déforment ou dépassent ce que disent les rapports. Aucun passage ne descend sous le niveau méthode.

## A. Fidélité

**Majeur**
1. **Q3 jugée « coûteuse » et à « prérequis lourd »** (classement, lignes 23-24, 44 et 92-93). Ce n'est pas ce que dit le rapport Q3.
   - Il place la dérivation, le préenregistrement et les lemmes en Lean « sur processeur seulement » (Q3, ligne 43).
   - Il chiffre l'évaluation à « quelques dizaines à centaines de dollars » (ligne 45).
   - Il dit que la taxonomie peut venir « d'un benchmark existant (SLEIGHT-Bench, MonitoringBench) » (ligne 44).
   - « Pôle théorie mûr » et le renvoi à la troisième instance (N-054/R-601) sont des ajouts de l'auteur, présentés comme s'ils venaient du rapport.
2. **Théorie de Q2 placée « après prérequis »** (ligne 43). Le rapport Q2 met la théorie « sur processeur seulement » (Q2, lignes 93-95). L'argument (a) de la recommandation, « les seules qui tiennent sur processeur », perd donc sa force (voir B).
3. **Kirch et al. (Q-pont)** : le classement écrit « transfert mauvais pour les comportements ambigus — exactement les nôtres » (ligne 54). Le rapport précise que la tromperie et la sous-performance volontaire n'ont pas de données naturelles : pour elles, l'échec du transfert est une « prédiction non vérifiée » (Q-pont, ligne 14). Le classement transforme une prédiction en constat.

**Mineur**
- **Alerte Q4, « voisin formel publié »** (ligne 27). 2601.20022 et 2509.17778 sont des préimpressions (Q4, ligne 56). « Démontrent » vient d'un résumé non vérifié. Écrire « préimpression, rapporté ».
- **RL-Obfuscation** (ligne 115). Le rapport parle d'environ 70 % de la **baisse de rappel** (Q7, ligne 15), pas de « l'évasion latente ».
- **Titre de 2610.12445** (ligne 144). Ce ne sont pas deux mais **trois** sous-agents qui lisent « Caught in the Act » : Q6, Q7 et Q-pont.
- **Inférences non marquées comme telles** :
  - « la fenêtre se ferme » pour Q2 (ligne 43) ;
  - Q1 « après Q-pont » (lignes 45 et 102) : aucune dépendance de ce type dans le rapport Q1 ;
  - Q7 « lecture secondaire de Q4/Q6 » (ligne 117) ;
  - le branchement sur N-053 (ligne 75).
- **Renvoi de règle** (ligne 152). La contre-lecture par un sous-agent neuf relève de R2, pas de R13.

## B. Cohérence du tableau et de l'ordre

**Majeur**
1. **« Tout de suite » s'applique à la partie déjà occupée.**
   - **Q6** : ce qui survit, c'est le contrôle de l'artefact **par tour, dans une boucle co-évolutive** (Q6, ligne 117). Or le programme n'a pas de boucle. Ce qui se fait sur processeur (bras « fuite textuelle », rétention sur sondes déjà extraites) est le volet statique, que le rapport juge « occupé densément ».
   - **Q4** : même schéma. Le rejeu des règles « par instant » contre « séquentielle » est le terrain de Shewhart/CUSUM, d'Urbina et al. et de Wen et al. La mesure qui survit (moniteur **évolué**, dilution réglable) est classée « après prérequis » (Q4, ligne 86).
   - Correction : dédoubler la colonne en « ce qui est faisable tout de suite » et « ce qui est distinctif ».
2. **Q-pont dépend de Q3.** Ce qui survit de Q-pont porte sur « des propriétés P_k **dérivées d'une théorie des angles morts** » (Q-pont, ligne 29), donc sur le produit de Q3. Le classement met Q-pont en tête et Q3 en cinquième position, ce qui est incohérent.
3. **Q3 doit être préenregistrée avant tout résultat.** Une prédiction d'angle mort doit être scellée avant que le programme ait vu un seul échec du moniteur. Sinon on tombe dans la circularité que le rapport Q3 signale lui-même (piège 2, ligne 46), et R1 est en jeu. Lancer Q-pont, Q4 et Q6 d'abord contaminerait Q3.
4. **L'argument (b) de l'ordre se contredit** (lignes 123-124). « Antériorité directe apparue en juillet 2026 » vaut pour Q4, pas vraiment pour Q6. La fenêtre la plus récente est celle de Q2 (préimpressions de septembre 2026, que le classement dit lui-même « se ferme ») et celle de Q-pont (billet Redwood du 23 octobre 2026).

**Ordre que je propose, mieux motivé** (confiance moyenne) :
- **0, en parallèle et sur processeur :**
  - dériver et sceller les prédictions de Q3 par famille, sur une taxonomie existante (SLEIGHT-Bench ou MonitoringBench) ;
  - mener la théorie de Q2 (composition d'e-processus).
- **1 :** Q-pont, en boîte noire, sur les propriétés P_k tirées de l'étape 0.
- **2 :** Q4, d'abord la partie théorique puis la mesure à dilution réglable, avec le rejeu en témoin. Puis Q6, d'abord le volet statique comme instrument, le volet « dans la boucle » quand une boucle existe.
- **3 :** noter Q3 une seule fois, sur le premier moniteur évolué.
- **Q1 :** après Q-pont.
- **Q5 et Q7 :** en réserve.

## C. Garde « zone vierge = question » (R8)

**Majeur**
1. **RvB (2601.19726) n'a été lu par aucun des huit sous-agents** : il n'apparaît que dans les listes « à vérifier » de Q1, Q5 et Q6. SafeCoEvo n'est connu que par Q2 (version 2, 7 000 derniers caractères non lus). D'après Q2 (ligne 54), son test porte sur « quatre scénarios inédits », ce qui touche les parties « ouvertes » de Q4 (volet iii) et de Q5. Le verdict d'ensemble « l'assemblage n'est pas occupé » (ligne 17) repose donc en partie sur des occupants non lus. Il faut l'écrire.
2. **Terekhov et al. (2606.08892) est minimisé.** Le classement le réduit à une « correction au cadre » (ligne 65). D'après Q4 (lignes 26-29), c'est une défense **qui évolue** (optimisation en point-selle contre une bibliothèque d'attaques qui grandit) **sur du diffus**. C'est l'occupant le plus proche du créneau même du programme (co-évolution de défense contre les menaces diffuses). Il doit apparaître parmi les occupants de Q4.
3. **Q4 : agrégation « laissée ouverte » trop vite.** Wen et al. (ICLR 2025, relu par les pairs, accumulation d'évidence entre tâches) et le moniteur à état de Hills et al. sont déjà des formes d'agrégation déployable. Le classement omet Wen et TRACE.

**Mineur**
- **Un verdict trop uniforme.** Huit verdicts identiques, avec le même motif « briques occupées, assemblage libre », produits par un cadre qui orientait vers ce motif : c'est une propreté suspecte au sens de R4. À signaler comme réserve.
- **Occupants omis :**
  - **Q5** : Lifelong Safety Alignment (NeurIPS 2025, relu par les pairs), EvoSafety (entraînement continué sur attaques tenues à l'écart) et MAAG ;
  - **Q2** : la limite clé du rapport (ligne 104) : la borne contrôle les fausses promotions **sur le jeu du juge**, pas la robustesse aux familles inédites.

## D. Niveau méthode (R-339)

Aucune violation. Tout reste au niveau de la classe et du mécanisme général. Trois passages limites, acceptables, à garder sous surveillance si on les reprend ailleurs :
- **Q4, lignes 12-13** : décomposition de la baisse de suspicion (code plus mince par commit, justifications plus plausibles). C'est un mécanisme général tiré d'un résultat publié.
- **Q4, ligne 86** : construire des traces diffuses en découpant des traces concentrées existantes. C'est une méthode de construction de jeu de données défensif ; elle doit rester à ce niveau dans tout préenregistrement.
- **Q3, lignes 21-22** : conditions de détectabilité (taille de fenêtre, graphe de flot de contrôle). C'est de la théorie publiée en 2004-2006, énoncée au niveau des classes.

L'affirmation du classement « contrainte tenue par les huit » (ligne 11) est donc exacte.

## E. Les deux alertes

- **Ramtin et al. (Q4) : fondée.** Le rapport en fait le « meilleur ancrage formel » (INFÉRÉ, ligne 59) et demande la comparaison avant toute revendication. Deux corrections :
  - écrire « préimpression » au lieu de « publié » ;
  - ajouter Gualandi, Maggio, Papadopoulos (MED 2022, Q4 ligne 64) : un plafond lié à l'horizon même contre CUSUM, autre voisin du lemme, absent de l'alerte.
- **SLEIGHT-Bench (Q3) : fondée, avec une nuance.** Le rapport dit que les catégories viennent des limites de capacité, des **défaillances observées** et des lacunes des modèles de menace (Q3, ligne 11). « D'une analyse de ce que les moniteurs supposent » sur-interprète : une partie des catégories est a posteriori. C'est justement ce qui laisse sa place à la notation préenregistrée.

## F. Corrections demandées avant scellement

1. Q3 : retirer « coûteuse » et « prérequis lourd », reprendre la traitabilité du rapport. *(majeur)*
2. Dédoubler la colonne « attaquable » en « faisable tout de suite » et « distinctif » ; corriger « après prérequis » pour la théorie de Q2. *(majeur)*
3. Revoir l'ordre : dépendance de Q-pont aux P_k de Q3, préenregistrement de Q3 en premier, argument (b) corrigé ; ou au moins motiver l'ordre actuel contre ces objections. *(majeur)*
4. Faire figurer Terekhov et al. et Wen et al. parmi les occupants de Q4 ; écrire que RvB n'a été lu par personne et que SafeCoEvo n'est connu que d'une seule lecture partielle. *(majeur)*
5. Kirch : « prédiction non vérifiée » ; alerte Q4 : « préimpression », plus Gualandi. *(mineur)*
6. Marquer comme INFÉRÉ les ajouts de l'auteur ; « trois sous-agents » ; R2 au lieu de R13 ; formulation des 70 %. *(mineur)*
