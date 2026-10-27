# Programme de conception de l'organisme (le pôle scientifique automatique) — v1

Lignée conv-audit (instance du 27 octobre 2026, servie par Fable 5.1), écrit à partir de 13:45 UTC (heure lue sur
`date -u` : 13:44:40). Sur le mot de Lazar du 27 octobre, 14:41 heure de Paris : « parfait, inscris-le au programme de
conception de l'organisme ». Document vivant : chaque version nouvelle remplace la précédente sous un nouveau nom (R12) ;
les décisions de Lazar y sont datées (heure de Paris) et mot pour mot quand elles le sont dans la session.

## 1. Ce qui est fixé (décisions de Lazar)

- **26 octobre** (synthèse du collisionneur, `docs/notes/pole-scientifique-automatique/synthese-collisionneur-v1.md`) :
  ni « perfectionner le nôtre » ni « adopter un système de la littérature » : **voie hybride ancrée sur notre noyau** ;
  tout moteur dont les agents héritent des clés est écarté ; la capacité « réécrire son propre code » est à concevoir
  sous bac à sable, pas à perfectionner.
- **27 octobre, 12:02** : « pas besoin de faire de preenregistrement je leve cette regle pour toute la partie
  exploratoire jusqu a avoir obtenu un systeme qui marche » (R-546).
- **27 octobre, 14:17** : dans l'organisme, côté Claude, **seulement Opus 5.5 et Fable 5.1** (codé : v6,
  `adaptateurs.MODELES_REELS_PERMIS`). Un **moissonneur** comme outil de l'organisme.
- **27 octobre, 14:32** : « go » sur : après (a), le bras d'attaque sur banque en cache ; en parallèle le pôle théorie
  avec Lean ; ne pas promettre de révolution, mesurer ce qui sort.
- **27 octobre, 14:41** : ordre de conception inscrit ici (section 3) ; **premier lancement réel (a) : « go »**, avec un
  plafond relevé (proposé : 50 USD ; dépense attendue 5 à 10) — la dépense elle-même passe par session-depot ; test du
  monde réel **par couches de complexité croissante, sur une question donnée** (section 4).

## 2. Ce qui est codé (état au 27 octobre, 13:45 UTC)

| version | contenu | état |
|---|---|---|
| v2 | juge v1 (ordre d'exécution secret, urne), contrôles de l'expérience 1 | expérience 1 : socle adopté |
| v3 | cycle avec juge v1 et nul des filles v2 | expérience 2 : nul v2 adopté ; démonstration v3 |
| v4 | mémoire prédictive (signature, classes, héritage de la preuve), marchepieds, filles à 300 tirages | démonstration v4 |
| v5 | seuil de signature par fiche, graine du noyau secrète, vivier de 60 | démonstration v5 : tout tenu |
| v6 | monde tenu par le noyau, dépôt unique par engagement, relais de clé réel (réserve par appel), répétition générale, modèles permis, ligne de commande | 154 essais ; répétition générale tenue ; **prêt pour (a)** |

Contre-lecture d'aptitude (27 octobre, sous-agent neuf, Fable 5.1 ; `premier-lancement-reel/contre-lecture-aptitude-v1/`) :
pas prêt pour le domaine du programme — il manque un monde qui rend des issues réelles, un rôle qui formule, un nul
informé ; le juge ne juge que des lois par instance ; deux canaux de texte ouverts ; aptitude constante en mode pari.

## 3. Ordre de conception (fixé le 27 octobre, 14:41)

1. **v7 — proposeur à liberté bornée et monde du programme.** Un rôle **proposeur** (Opus 5.5) qui lit le programme, la
   mémoire du pôle et la moisson, et formule les fiches ; il choisit parmi un **catalogue de stratégies** de proposition
   et de recombinaison (liberté bornée) ; **moissonneur** servi par le relais du noyau (clés de moisson tenues par le
   relais, quotas, journal, provenance par empreinte de PDF, garde de fuite : jamais la provenance d'un texte de test) ;
   **monde du programme** sur banque d'épisodes en cache (traits visibles, issues cachées, tirage après le gel) ; **nul
   informé** (prédiction calibrée du moniteur courant, meilleure base boîte noire) ; configuration **sans urne** quand le
   monde est une banque figée ; fermeture des deux canaux de texte (rejeu limité au code déclaré ; leçons structurées) ;
   contrôle réel de la lignée du vérificateur ; **aptitude = preuve** (log de richesse) ; signature de mémoire sur la
   recette, pas seulement sur la loi, pour le bras d'attaque. Rôle proposeur **enfichable** : un proposeur de la
   littérature peut être branché devant le noyau comme bras de comparaison, mesuré par le juge (question posée au
   collisionneur, `question-collisionneur-proposeur-enfichable-v1.md` ; décision après le tour).
2. **v8 — réécriture des rôles sous bac à sable.** L'organisme peut proposer une réécriture de ses propres rôles
   (consignes, stratégies, code des rôles) ; **une réécriture est une fiche** : elle prédit une amélioration mesurable
   (fiches vraies promues par dollar sur des témoins et des mondes **neufs**), elle est jugée par le même juge en duel
   contre la version d'avant ; **jamais le noyau** (juge, monde, témoins, signature de la mémoire, budget, clés). Elle
   ne commence qu'**après un résultat sur une vraie question** (sinon on optimise l'optimiseur sans signal).
3. **Bras d'attaque** (après (a) ; « go » du 27 octobre, 14:32) : fiches-recettes (mode de sabotage, consigne, structure
   temporelle) jugées sur le taux de manque de nos moniteurs contre un nul informé (le manque sur les modes connus) ; en
   **quarantaine** (N-053 point 5, N-054 : recettes scellées, révélées à l'évaluation, jamais lues par qui conçoit sondes
   ou agrégateurs) ; témoins = les failles déjà documentées (le pôle doit les retrouver seul avant d'être cru sur les
   inédites).
4. **Pôle théorie** (en parallèle ; même « go ») : juge = vérificateur de preuves (Lean), proposeur nourri par le
   moissonneur et la recombinaison ; questions ouvertes du programme (agrégateur sous corrélation adverse, théorème
   négatif). Aucune dépense de carte ; installation de Lean sans dépense.

## 4. Couches d'essai sur le monde réel (une question, une porte par couche)

Question proposée (à confirmer par Lazar) : le pivot du programme — le sabotage diffus déplace-t-il la marginale des
scores de sonde, et l'accumulation séquentielle rattrape-t-elle ce que le seuil par action manque (H2) — réécrit en lois
par instance. Mesure à chaque couche : fiches vraies promues par dollar ; zéro fausse découverte sur les témoins ; ce que
le pôle a trouvé que nous ne savions pas (lu dans les deux sens, R4).

| couche | monde | coût estimé (minimal / idéal) | porte de sortie |
|---|---|---|---|
| 0 | monde caché tenu par le noyau, vrais agents (option a) | 10 / 50 USD | plomberie tenue (ordre, témoins, coûts réels) |
| 1 | banque réelle figée en cache (pilote T0.5 : 180 épisodes honnêtes notés par les juges), nul informé, sans carte | 25 / 100 USD | le pôle retrouve seul le connu (traits du texte qui prédisent le score, N-029) |
| 2 | banque avec sabotage : organismes T0.6, sondes T0.7, bases T0.8, notées une fois (carte une fois) | 100 / 300 USD | témoins plantés et résultats établis retrouvés ; première lecture de H2 |
| 3 | épisodes ou moniteurs neufs à la demande (option c) | 100 / 400 USD | coût mesuré sur une fiche pilote avant toute course |
| 4 | bras d'attaque en quarantaine ; pôle théorie | 100 / 400 USD par course ; Lean : agents seuls | failles connues retrouvées avant toute inédite |

Anti-gaspillage (codé ou à coder) : plafond par génération et par agent ; réserve par appel au relais ; arrêt quand plus
rien ne survit ; témoins plantés à chaque génération (une génération 0 qui rate ses témoins arrête la course) ; pilote
d'une fiche avant toute course coûteuse ; traitement différé pour les appels de moniteur du noyau ; rien ne repart sans
lecture de la course précédente.

## 5. Questions ouvertes (pour Lazar)

- La question de la couche 1 (H2 proposé) ; une v3 des questions du programme après la couche 1, éventuellement par un
  tour du collisionneur « quelles questions produiraient des résultats forts avec ce pôle, sous nos contraintes ».
- Le plafond de (a) (50 USD proposé).
- Le tour du collisionneur sur le proposeur enfichable (≈ 8 USD).
