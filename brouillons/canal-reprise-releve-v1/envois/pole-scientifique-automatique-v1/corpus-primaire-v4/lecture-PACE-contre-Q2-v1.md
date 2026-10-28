# Lecture de PACE (arXiv 2606.08106v1) contre la question Q2 — v1

Date : 29 octobre 2026. Sous-agent de la lignée « conv-audit ». Niveau méthode ; aucune dépense, aucun réseau, aucune clé. Document scellé (voir `lecture-PACE-contre-Q2-v1.md.sha256`) ; une correction sera une v2, jamais une réécriture.

**Lu.** (1) Le PDF de PACE, douze pages, en entier (copie fournie, empreinte vérifiée ; chemin `docs/sources/pdf/2606.08106v1.pdf`, SHA-256 `779f49607688fd06226d4390ad6e0c4c8356ef75b87243fd734181cef700934f`). (2) Le rapport `anteriorite-Q2-v1.md` (empreinte `32a887d4…382ea0`) et la section Q2 de `classement-motive-sept-questions-v2.md` (empreinte `7a59a8cd…cf9fc1`). (3) La note sur PACE de `../corpus-primaire-v2/LISEZMOI-v1.md` (empreinte `84050452…e53a0`), non revérifiée sur le PDF de 2609.17560. Pages citées : celles du PDF de PACE (passages dans `extrait-2606.08106-v1.md`).

La revendication de Q2, telle que le rapport l'écrit (section 3, « formulation étroite apparemment ouverte »), est : dans une boucle de sélection itérée de moniteurs de sécurité, contre des familles d'attaque tenues à l'écart, un juge non apprenant qui (a) contrôle, par un e-processus composé sur toute la boucle (budget d'erreur unique, inégalité de Ville), le taux de fausses promotions ; (b) est audité par des témoins plantés (contrôles négatifs, nulles de bibliothèque) ; plus (c) la mesure de l'écart entre trois régimes sur la même boucle : juge figé garanti, juge-modèle co-évoluant ou partagé, validation en distribution.

## 1. Verdict en trois lignes

- **Q2 reste SEMI-OCCUPÉE, confiance moyenne** (verdict du rapport inchangé), mais la zone occupée s'élargit : la porte de validation par e-processus apparié, valable à tout instant par candidat, dans une boucle d'auto-évolution d'agents à modèles de langage, est publiée (PACE, cachet du 6 juin 2026 ; 2609.17560 : 22 juillet 2026 selon le corpus v2).
- Occupées par PACE : le e-processus, la garantie et la borne par candidat sur les fausses validations, un jeu d'audit neuf, la comparaison « acceptation gloutonne » contre porte. Non occupées : la borne composée sur toute la boucle, la validité sous juge adversarial, tout juge-modèle, les moniteurs de sécurité et familles d'attaque tenues à l'écart, les témoins nuls plantés, la mesure des trois régimes.
- Le papier avoue ces absences (p.5, p.9) ; une limite d'un papier n'est pas un trou du champ (R8) : le « non occupé » ne vaut que contre PACE, et la borne composée est déjà revendiquée ailleurs (2609.17560, rapporté).

## 2. Ce que PACE fait réellement

**Objet.** Des agents à modèle de langage qui s'auto-modifient (ici : réécrire leur invite système) acceptent un changement « si le score monte sur un petit jeu de développement ». L'auteur, chercheur indépendant, y voit des tests multiples adaptatifs sur un signal réutilisé et bruité (p.1, p.4). Sa porte : chaque candidat est comparé au titulaire sur les mêmes instances, les égalités sont écartées, et sur les paires discordantes un e-processus de pari multiplie la richesse par « un plus lambda fois (deux fois la victoire moins un) » (équation 2, p.4) ; validation dès que la richesse atteint 1/α, avec α = 0,05 et lambda = 0,5 par défaut ; rejet si le budget d'évaluation s'épuise avant le seuil (p.4).

**Garantie.** Sous l'hypothèse nulle « le candidat n'est pas meilleur », avec des résultats discordants conditionnellement équitables, la richesse est une surmartingale et l'inégalité de Ville borne par α la probabilité de jamais valider ce candidat, pour tout arrêt dépendant des données (p.5). Deux limites sont dites en toutes lettres : la validité est **par candidat**, “not a run-level familywise bound” (p.5 ; p.9 tableau 3 ; p.1) ; et la réutilisation adaptative du jeu pour engendrer le candidat suivant est “an empirical matter, not a theoretical claim” (p.5).

**Expériences.** Modèles Qwen2.5 de 0,5 à 3 milliards de paramètres, invite éditable, tâche GSM8K notée par correspondance exacte avec la réponse de référence (p.6) ; SVAMP et ARC-Challenge en section 5.4 et annexe (non reprises dans l'extrait). Jeu de développement réutilisé de 40 problèmes, jeu d'audit neuf de 120 problèmes que la règle d'acceptation ne voit jamais (p.6). Deux régimes : « contrôlé », avec une instruction nuisible plantée que le proposeur peut retirer pour un gain connu (p.6) ; « stochastique », agent échantillonné à température 0,7, sans gain important disponible (p.6). Résultats : l'acceptation gloutonne valide 30 à 42 % de changements faux dans le régime contrôlé (tableau 1, p.7) et 13 à 21 auto-modifications par exécution dans le régime stochastique, 72 à 100 % fausses selon l'audit (p.1, p.7) ; la porte valide le gain planté et presque rien d'autre (tableau 1) pour un coût d'évaluation environ 18 % plus bas (p.1). Comparaisons : un test apparié à taille fixe et une correction en ligne du taux de fausses découvertes (tableaux 1 et 2, p.7).

**Ce que l'auteur ne revendique pas** (p.9) : ni puissance supérieure, ni statistique nouvelle, ni généralité au-delà de l'interface ; “the contribution is this abstraction, locating an anytime-valid test at the commit step, not the test itself (which is standard)” (p.2).

## 3. Ce que PACE occupe de Q2, brique par brique

| Brique de Q2 | Ce que PACE fait (page) | Statut |
|---|---|---|
| Juge **figé** | Pas de juge-modèle : l'exactitude est une correspondance exacte avec la référence (p.6, GSM8K). Ce qui est « figé » est l'agent, modèle gelé dont seule l'invite évolue (p.6). Les « préférences par paires » sont affirmées à l'interface (p.2), testées dans aucune expérience (p.6-8) ; la généralité d'interface est “argued, not shown” (p.9, tableau 3). | **Libre** pour tout juge-modèle ; trivial pour un étiquetage déterministe |
| **Garantie statistique** | Oui : surmartingale, inégalité de Ville, valable à tout instant (p.4-5). | **Occupée** (par candidat) |
| **Borne sur les fausses promotions** | Probabilité de valider un candidat non meilleur ≤ α, par candidat ; “the expected number of false commits grows at most as α per candidate” (p.5) ; ni borne de famille ni budget unique composé. | **Semi-occupée** : borne par décision occupée ; borne composée de boucle déclarée absente (p.5, p.9) |
| Validité sous **juge adversarial** | Aucun adversaire, aucune co-évolution, aucun juge-modèle dans le papier. | **Libre** contre PACE (la validité sous étiquettes adversariales est dite présente dans 2609.17560, p.1, p.3, théorèmes 4 et 5, selon le corpus v2 : juge ou acheminement des étiquettes adversarial, non attaquant qui co-évolue) |
| **E-processus** | Oui, pari à fraction fixe sur les paires discordantes (équation 2, p.4) ; l'auteur nomme l'ingrédient « standard » (p.2). | **Occupée** |
| **Témoins plantés** | Un gain connu planté (instruction nuisible retirable) : contrôle positif, “a unit test for acceptors” (p.6). Un régime sans gain important : monde nul global (p.6). Un jeu d'audit neuf, jamais vu de la règle, étiquette après coup (p.6). Ni bibliothèque de nulles connues ni contrôles négatifs injectés dans la boucle vivante. | **Semi-occupée** (contrôle positif, jeu intouché) ; **libre** pour les nulles injectées |
| Sélection de **moniteurs de sécurité**, familles d'attaque tenues à l'écart | Tâches de mathématiques et de sciences (p.1). La porte “inherits the dev set's coverage” et ne peut certifier ce que ce jeu ne voit pas (p.9). | **Libre** ; l'aveu de p.9 rejoint le piège « validité qui ne se transporte pas » de Q2 |
| **Mesure des trois régimes** | Compare quatre règles : glouton sur le jeu réutilisé (le régime « validation en distribution »), test apparié à taille fixe, correction en ligne, porte (tableaux 1-2, p.7). Aucun régime de juge-modèle, partagé ou co-évoluant. | **Semi-occupée** pour un régime sur trois, sur un jouet ; **libre** pour les deux autres |

**Un point utile à la théorie de Q2.** La section 4 de Q2 prévoit le contrôle en ligne du taux de fausses découvertes. PACE l'a essayé sous une forme (“decaying-memory” p.5 ; “fixed-schedule” p.8 ; la référence de 2017 citée p.3 s'intitule « … with decaying memory », p.10 : inférence) et la juge “over-conservative”, manquant parfois le gain réel (p.5, p.8 ; tableau 2, p.7 : zéro validation en régime stochastique). Observation sur un jouet de 40 instances (p.6), non résultat d'impossibilité : ne pas la reprendre contre la brique composée (R8).

**Un second point.** L'auteur cite Dwork et al. et Blum et Hardt (p.4) : une source de plus, sur des modèles de langage, pour le volet « ne survit pas » de Q2 (« un évaluateur fixe empêche Goodhart » : connu faux).

## 4. Ce que PACE laisse libre

1. **La borne de boucle.** Un budget d'erreur unique composé sur une suite non bornée de promotions avec réutilisation adaptative du jeu. PACE la déclare hors de portée (p.5). Le corpus v2 la situe dans 2609.17560 (proposition 13, famille à calendrier d'union sans allocation adaptative, p.22 de ce papier) : brique **occupée ailleurs, en partie**, à relire sur PDF avant toute revendication.
2. **Le juge-modèle.** Toute perte lue par un juge-modèle, figé, partagé avec la récompense ou co-évoluant : aucun passage de PACE.
3. **L'adversaire.** Aucun attaquant, aucune famille d'attaque ; la porte consomme des correct/faux sur les mêmes instances (p.2).
4. **Les nulles de bibliothèque.** Des non-améliorations connues, injectées dans la boucle pour auditer la porte en continu (distinct du gain planté positif de PACE).
5. **La mesure des trois régimes** sur une même boucle avec moniteurs de sécurité.
6. **La puissance sous petit jeu.** PACE l'admet : “the wrong tool” quand les gains attendus sont minuscules ; sur un gain atténué de +0,18, la porte en garde 78 % (p.9 ; +0,14 à la p.6). Le piège « puissance » de Q2 est confirmé, sur jouet.

Ces six zones sont des **questions**, pas des trous (R8).

## 5. La revendication de Q2 après PACE

**Décision de lecture : SEMI-OCCUPÉE (confiance moyenne), formulation de Q2 maintenue mais resserrée.**

- Pas **occupée** : trois composantes de l'assemblage (borne de boucle, témoins nuls plantés, mesure des trois régimes) ne sont pas dans PACE, ni le cadre (moniteurs de sécurité contre familles tenues à l'écart) ; PACE n'a ni juge-modèle ni adversaire.
- Pas **libre** : la composante « garantie par e-processus à l'étape de validation d'une boucle d'auto-évolution » est publiée (PACE, lu sur PDF) ; l'argument « un jeu réutilisé gonfle les fausses découvertes » l'est aussi (p.4).
- La phrase du rapport « Aucun occupant de la co-évolution attaque/défense ne combine les deux » reste vraie : PACE n'en est pas une (proposeur unique, p.6).
- Règle R8 : (i) « PACE ne compose pas la borne » est une **limitation d'un papier**, qu'il déclare ; elle ne prouve pas que le champ n'a pas la composition (tests séquentiels, tests fermés, 2609.17560). (ii) « PACE n'a pas d'adversaire » est une **zone vierge de ce papier**, donc une question : la validité sous juge adversarial est dite occupée ailleurs ; la sous-zone « adversaire co-évoluant qui choisit les candidats » n'apparaît dans aucun papier de nos rapports, inférence par absence. (iii) Zone séduisante, « nulles injectées dans la boucle » : PACE en est voisin (régime nul global, tableau 2 ; gain planté) sans l'occuper ; à tester par recherche (« negative control », « canary », « planted null ») avant toute revendication.

**Audit de propreté (R4), dans les deux sens.** (i) Notre verdict ne bouge pas malgré un occupant nouveau : stabilité suspecte, d'où le détail ci-dessus de ce qui est déclassé (garantie, e-processus, jeu intouché, régime « glouton ») et de ce qui ne l'est pas, page par page. (ii) Le « zéro faux sur cinq » de PACE (p.1, p.7) est propre par construction : un gain planté, cinq validations par modèle. En régime stochastique, la porte valide environ une fois sur trois exécutions à 0,5 et à 1,5 milliard de paramètres (0,3 validation par exécution, 33 % étiquetées fausses, dénominateur presque vide selon la légende, tableau 2, p.7) : compatible avec une borne par candidat, mais ce n'est pas « rien ».

## 6. Correction à proposer au rapport Q2 (une v2)

Nom proposé : `anteriorite-Q2-v2.md` (la v1 reste intacte). Verdict inchangé ; contenu :

1. **Section 1, deuxième puce de la liste.** Ajouter : « PACE (2606.08106, 6 juin 2026) occupe, dans le contexte des agents à modèles de langage, la porte de validation par e-processus apparié et valable à tout instant par candidat ; il déclare n'avoir aucune borne de famille » (p.5, p.9).
2. **Section 2, groupe A.** Ajouter PACE en tête, avant 2609.17560 (cachet du 6 juin contre 22 juillet, selon le corpus v2). Nuancer la phrase « C'est l'antériorité la plus dangereuse pour la revendication « borne sur les fausses promotions » » : PACE est la plus proche pour « e-processus à l'étape de validation d'une boucle » ; 2609.17560 pour « composition sur une suite de promotions ».
3. **Section 2, nouveau bloc « PACE ».** Fait / ne fait pas, avec pages (sections 2 et 3 ci-dessus).
4. **Section 3, « Ce qui ne survit pas ».** Ajouter : « porte appariée à e-processus dans une boucle d'auto-évolution : occupé (PACE) » ; et à « Pièges » : « la correction en ligne essayée par PACE fut trop prudente sur un jouet (p.5, p.8) ; non une impossibilité ».
5. **Section 3, « Formulation étroite ».** Resserrer sur : (a) borne **de boucle** à budget unique avec réutilisation adaptative, liée à 2609.17560 ; (b) **nulles de bibliothèque injectées**, distinctes du gain planté de PACE ; (c) mesure des trois régimes avec juge-modèle. Retirer « garantie par e-processus » des parties distinctives.
6. **Section 4, « Pièges connus ».** Ajouter l'aveu de PACE : hypothèse de résultats conditionnellement équitables non démontrée sous réutilisation d'un jeu fini de 40 instances (p.5-6), et limite de couverture (p.9).
7. **Section 5, « À vérifier ».** Ajouter : relire 2609.17560 p.5 et p.31 sur sa caractérisation de PACE ; relire la figure et les tableaux 4 et 5 de PACE (p.12).
8. **Section 6 (requêtes) et classement v2, ligne Q2.** Ajouter les requêtes « anytime-valid commit gate self-evolving agents » et « planted null negative control sequential test model update » ; ajouter PACE aux briques occupées ; confiance inchangée.

## 7. Réserves (une ligne chacune)

- Préimpression d'un seul auteur indépendant, sans lieu de publication ni code cité ; « first explicit treatment » (p.2) est une revendication de l'auteur, non vérifiée.
- Le lien « cité par 2609.17560, p.5 et p.31 » vient du corpus v2, non relu ici sur le PDF de 2609.17560.
- Le texte de PACE donne des valeurs pour la correction en ligne (« +0,000 » à α = 0,01 ; « +0,41 » à n = 20, p.8) qui ne figurent dans aucun tableau du PDF (le tableau 4, p.12, n'a que les colonnes « glouton » et « PACE ») : à relire avant citation.
- Nombre d'exécutions : « moyennes sur 5 graines » (p.6) mais 3 graines aux tableaux 2, 4 et 5 (p.7, p.12) et « 3–5 » au tableau 3 (p.9) ; contradiction interne.
- Le test apparié à taille fixe égale la porte au tableau 1 et s'en écarte de moins d'une validation par exécution au tableau 2 (p.7) : l'avantage revendiqué de la validité à tout instant (p.5) repose sur très peu d'événements.
- L'étiquette « fausse validation » de l'audit (changement audité ≤ 0, p.6) n'est pas l'événement que borne α (nulle « pas meilleur ») ; l'auteur écrit “the two coincide here” (p.6) ; à garder séparés.
- Tableaux 4 et 5 et section 5.4 : hors extrait (taille) ; lus ici sur le PDF, non vérifiés chiffre par chiffre.
- Les « libre » ci-dessus sont des inférences par absence dans un seul papier (R8), non des constats sur le champ.
