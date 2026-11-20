# Vérification du code v4 du palier 0b — v1

Pièce de travail (classe C). Contre-lecteur, modèle S, le même que pour les versions 2 et 3. Rapport du développeur v4 vérifié par son compagnon (`2947c4f1…`, OK) ; v8 lue aux endroits cités (annexe H, « Ce qui demande un code v4 », nœuds 1 et 2). Code v4 copié dans mon dossier (`v4/`). Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille ; rien dans le dépôt ; aucun refus d'outil.

## Verdict

**Conforme.** Aucune correction demandée au code. Un seul point est à porter hors du code, et il est important : la règle calibrée lit 0,55 + 2 σ₀ alors que la moyenne permutée s'écarte de 0,5 (constat 2 ci-dessous).

## 1. Les points de « Ce qui demande un code v4 » (v8)

Point 1, audit et étape 3 (`audit.py`, `mondes.py`), lu ligne à ligne :
- **Longueur de forme** : `texte_aux_nombres_remplaces` remplace par un caractère chaque nombre que `jetons` lit comme « nombre » (même fonction `_nombre_long`) ; la longueur brute passe en septième trait de contenu, avec refus d'un texte qui n'est pas le texte canonique de la loi. Contrôle à moi sur une suite de la dose 0,5 (graines « essai ») : v3 puis v4 — 64 cases de forme **identiques**, six traits de contenu **identiques**, longueur de forme de moyenne 306,25 / écart-type 2,39 en v3, **173 / 0** en v4 (le signe ne passe plus), septième trait de contenu (longueur brute) de moyenne 306,25 / écart-type 2,39. Conforme au nœud 1 (a).
- **σ₀ par permutations, entre lois ou entre suites** : `sous_permutation`, `permuter_les_etiquettes` (une étiquette commune par suite, suite à deux étiquettes refusée), 1 000 permutations par défaut, plis retirés à chaque permutation, `rng_permutation` propre. Les plis de la lecture observée sortent du même `rng` dans le même ordre qu'en v3 (vérifié : les exactitudes observées ne bougent que par les traits).
- **Règle calibrée pour les seuls audits par dose** : `lecture` : forme des doses, au plus 0,55 tenue ; au-dessus de 0,55 + 2 σ₀ arrêt ; entre les deux « non départagée » avec mention ; forme des audits de lois à la lettre (au-dessus de 0,55, arrêt) ; contenu et réunis rapportés et signalés au-dessus de 0,55. Identique au texte v8 (j'ai relu la phrase des trois lectures).
- **Arrêts** : exactitude non calculable (pas deux classes, ou moins de cinq exemples d'une classe), à la lecture observée et sous permutation (`_exiger_calculable(yp)`) ; pli d'entraînement privé d'une classe ; centre non fini : `ArretAudit`, converti en `ArretGenerateur` à l'étape 3, rapport joint quand il existe. La clé `non_calculees` disparaît.
- **Étape 3** coupée en construction et jugement ; la table (A, σ₀, moyenne permutée, seuil, lecture, unités permutées) est rendue pour les quinze.
- **D8** : `exiger_ecart_type_et_taille_finis` arrête sur un écart-type réuni nul ou non fini et sur une taille non finie, à chaque évaluation de la dichotomie et pour les proposeurs sans réglage ; « non atteignable » reste réservé à une taille finie trop petite. Conforme.
- **Choix 12** : liste triée des étiquettes dans un fichier scellé, empreinte égale à celle que le manifeste portait déjà, `verifier_manifeste` qui rejoue. Conforme.
- **Jeu de la garde 27** : `etapes.etape_4_jeu_de_la_garde_27` (construction du jeu puis bras 1 à 3, 4a, 4b), dose fixée par `DOSE_JEU_GARDE_27 = 0,25`, deux fonctions qui arrêtent à toute autre dose avant de tirer. Conforme à « à quelle étape, par quelle fonction, à quelle dose ». Remarque : rien n'appelle cette fonction depuis `etape_4` ni d'un programme de lancement (il n'en existe pas encore, cf. la contre-lecture v2, § 5 du rapport v2) ; le développeur le dit (silence 8). C'est à l'erratum d'écrire le proposeur et le nombre de sources du jeu et de dire qui l'appelle.

Points 3 à 7 : le choix 8 est bien celui du code (la première clé (contexte, monde, texte) gagne, bras dans l'ordre joué) : **levé par moi**. Le point 7 est rapporté (moyenne permutée), voir constat 2.

## 2. Verrou D6 : l'arrêt est juste

La v8 dit, au point 2, que le « fichier d'autorisation du lancement » n'est défini nulle part ; sa forme, son auteur et son lieu sont à définir « par la mère et au code v4, avant que le verrou soit écrit » ; le mandat du développeur permet un arrêt motivé si la v8 ne le définit pas assez. Écrire seulement deux des trois conditions de B8 (compagnon, empreinte inscrite, module par module) ou retirer seul `PREENREGISTREMENT_SHA256` ferait un verrou partiel et trancherait un silence réservé. `graines.py` est resté identique à la v3 (empreinte de la table), et le verrou v3 tient (couches décisives refusées sans `Autorisation`, essai final au vert seul et en suite). **Arrêt juste** ; à reprendre après la définition du fichier par la mère. Le point reste ouvert et la liste d'arrêt (point 1) interdit tout tirage tant qu'il l'est.

## 3. Essais, lancés par moi (copie, `PYTHONPATH=src`)

Chaque fichier seul : `zz` 1, `gardes` 17, `outils` 15, `statistique` 11, `etapes` 5, `organisme` 5, `mecanique` 10, `mondes` 15 : **79 passés**. Suite entière, un processus : **79 passés, 0 échoué (804 s)**. Le fichier « aucune graine décisive » passe seul et en suite entière.

## 4. Banc `mutations_v3.py`

Rejoué en entier chez moi, un processus, témoins joués d'abord : **témoins au vert ; 71 défauts appliqués, 71 vus**, dont les 21 neufs (nœud 1, nœud 2, σ₀, identifiant de suite, plis privés, non calculable, centre non fini, arrêt converti à l'étape 3, D8 ×3, choix 12 ×2, dose du jeu ×3) et les 50 de la v2 (S8 (i) 193 s). Aucun défaut n'ouvre le verrou des couches décisives.

## 5. Sorties v3 → v4

Outil à moi (`outils-cl/empreintes_v2_v3.py`, `traits_v3_v4.py`, graines « essai ») : les **140 empreintes** de sorties de la couche statistique (sept proposeurs, bras 1 à 4b, 400 sources) et du jeu mécanique à deux sources à la dose 0,25 sont **identiques** à celles de la v3 (donc de la v2), ligne à ligne. Là où le développeur annonce un changement, je le retrouve : forme (longueur) et traits de contenu (septième trait) changent ; 64 cases de forme et six traits de contenu d'origine, non. Je n'ai pas rejoué les 144 + 6 empreintes du développeur (son outil n'est pas au dossier) : ma comparaison couvre les mêmes familles, avec 140 lignes à moi plus le contrôle des traits.

## 6. Les 13 silences et les trois constats

Silences déclarés (§ 2 du rapport), ce que chacun demande :
- **À l'erratum (précision, sans nœud)** : 1 (ddof = 1 de σ₀), 2 (un générateur de permutations pour les quinze, ordre fixe), 3 (**la graine des plis de la lecture observée n'est dérivée nulle part** : il faut un rôle d'étiquette avant lancement, sinon la lecture observée n'est pas reproductible par R9), 4 (égalités : « au plus » inclusif, « au-dessus de 0,55 + 2 σ₀ » strict), 5 (« pas deux classes » rangé en non calculable), 8 (proposeur et nombre de sources du jeu de la garde 27 ; qui l'appelle), 9 (D8 : on contrôle l'écart-type réuni, pas chaque bras), 10 (nom du fichier des étiquettes, sans saut de ligne final), 13 (en-tête de `constantes.py` dit v6 : se corrige avec D6).
- **Sans suite** : 6 (le caractère `#` : seule sa longueur compte), 7 (la distribution B1 (iii) porte la longueur brute), 11 (rapport joint à l'exception), 12 (outils de diagnostic v2 non mis à jour : `diagnostic_presentation.py` ne tourne plus ; trace seulement).
- **Aucun ne relève d'un nœud de Lazar.**

Constats pour la mère :
1. **Contenu et réunis des audits par dose, sans calibrage, alarment au hasard.** Mon calcul sous le nul (traits gaussiens indépendants, graine locale ; `outils-cl/bruit_nul_dimensions.py`, 1 000 répétitions, 200 contre 200) : écart-type 0,033, et 4,5 % (7 traits de contenu), 4,8 % (65 de forme), 5,6 % (72 réunis) des audits au-dessus de 0,55. Six audits (trois contenu, trois réunis) lus à 0,55 sans calibrage : une probabilité de l'ordre de 20 à 25 % qu'un générateur parfait pose la mention « non audité pour l'étage payant ». La forme calibrée tombe, elle, à 2 ou 3 % par audit (de 11-14 % à environ 7 % sur les trois), ce qui est le but. **C'est un nœud, non un erratum** : le GO a limité la règle calibrée aux trois audits de forme par dose. Je recommande de demander à Lazar d'étendre la même lecture à contenu et réunis des audits par dose, pour le signalement seulement (jamais un arrêt) ; sans cela le signalement ne distingue pas un vrai défaut du hasard. Les deux audits de lois (milliers d'exemples) ne sont pas concernés.
2. **La moyenne permutée des audits par dose s'écarte de 0,5, et la règle ne la lit pas.** Le développeur mesure 0,457 à 0,603 à quatre suites par dose (forme 0,472 à 0,550), contre 0,497 à 0,505 pour les audits de lois. Ce sont des moyennes **sous permutation** : le nul lui-même est décalé par la fuite entre mondes frères d'une même suite. Un seuil 0,55 + 2 σ₀ est donc trop bas quand la moyenne permutée passe 0,55 et trop haut (trop laxiste) quand elle est sous 0,5. À 50 suites par dose le décalage sera moindre (trois frères parmi 160) mais non nul. **À l'erratum (contre-lu), pas au code** : le seuil naturel est moyenne permutée + 2 σ₀, ou des plis tirés par suite (note D9) ; le code rapporte déjà la moyenne. Je recommande de le dire avant tout lancement, puisque c'est la règle qui décide l'arrêt de l'étape 3.
3. **Avant-goût (R4).** Les valeurs vues par le développeur (contenu « dépendantes contre indépendantes » 0,63 ; une forme de doses non départagée à 0,594 pour un seuil de 0,749) sont celles que le contrôle de la v7 prévoyait : signalement probable, générateur non audité pour l'étage payant, voie de la réserve 18 à prendre avant tout étage payant. Aucune lecture de critère : à garder dans la liste de ce que la mère sait. Je note que la longueur de forme est désormais constante dans les mondes de B1 (173 ; écart-type nul), donc sans pouvoir discriminant : l'audit de forme ne lit plus que les 64 cases de jetons, ce qui est la conséquence voulue du nœud 1 (a), non un défaut.

*Contre-lecteur, modèle S.*
