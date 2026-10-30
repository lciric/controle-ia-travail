# Réponse de conv-audit à la question 5 (identifier par apprentissage profond les paramètres qui créent la fertilité) — v1

conv-audit, 30 octobre 2026 (Fable 5.1, 18:15 heure de Paris), transcrite sans modification de fond. Références de mémoire : SUPPOSÉ.

**Position.** Non, pas avec des données d'observation seules : un réseau entraîné sur les citations apprend ce qui accompagne la reprise, pas ce qui la provoque (« voir » contre « faire », Pearl). Il faut une source d'intervention ou une hypothèse écrite. Trois voies : nos courses (interventions contrôlées), les expériences naturelles de la littérature, l'invariance entre environnements. L'apprentissage profond sert dans chacune, n'en remplace aucune.

## (1) Ce qu'un expert ferait, et que Lazar ne demande pas
- Écrire le graphe causal supposé (contacts, structure commune, désaccord, taille, âge, mode, financement, reprise) et les flèches inconnues.
- Prendre nos courses comme laboratoire : paires au hasard contre par la règle (randomisation) ; 0, 2, 5, 10 titres dans le tableau minimal (dose de contact) ; courbe dose-réponse mesurée sur la survie aux tests de mort et la reprise entre générations.
- Exploiter les expériences naturelles (différence de différences, contrôle synthétique) : décès de chercheurs étoiles (Azoulay, Graff Zivin et Wang 2010), déménagements, conférences annulées en 2020, financements imposant l'interdisciplinarité, fusions de revues.
- Apprentissage profond là où il est causal : découverte de structure sur séries multicouches (PCMCI de Runge, NOTEARS, versions avec interventions) ; prédiction invariante entre sous-domaines, décennies, pays (Peters, Bühlmann et Meinshausen 2016 ; Arjovsky 2019) ; effets hétérogènes (forêts causales d'Athey et Wager, Dragonnet, TARNet) sous « pas de facteur caché » avec analyse de sensibilité (valeurs E).
- Distinguer causalité dans le modèle (ablation) et dans le monde (prédire l'effet d'une intervention jamais vue).
- Simuler : modèle d'agents étalonné, substitut neuronal, interventions in silico, confrontation aux expériences naturelles ; régression symbolique sur la fonction causale.
- Préenregistrer des effets signés et chiffrés, avec placebo et contrôle négatif.

## (2) Données brutes
Panel des chercheurs d'OpenAlex (affiliations par année, coauteurs), décès de chercheurs étoiles (Azoulay) ; programmes de conférences et annulations 2020 ; bases de financement (NSF, ERC, CORDIS) ; fusions et créations de revues ; nos courses (journal des affectations, verdicts, tests de mort par génération) ; expériences humaines publiées (Derex et Boyd 2016 ; Mason et Watts) ; environnements nombreux (même hypergraphe par sous-domaine, décennie, pays).

## (3) Méthodes et outils
Randomisation et dose dans nos courses ; différence de différences et contrôle synthétique avec tendances préalables, placebos, contrôles négatifs ; PCMCI, NOTEARS ; prédiction causale invariante, minimisation du risque invariant ; forêts causales, réseaux à deux têtes, apprentissage double robuste, valeurs E ; modèle d'agents, substitut, régression symbolique ; transition de phase par intervention sur la dose comparée à la courbe d'observation.

## (4) Vérification hors de nous
Prédiction d'une intervention jamais vue réalisée à la course suivante ; expériences naturelles indépendantes du modèle ; reproduction sur d'autres domaines et décennies ; courses randomisées étiquetées par les tests de mort.

## Reformulation
« Identifier les paramètres qui créent la fertilité. 1. Graphe causal supposé. 2. Trois voies avec hypothèses écrites : (a) interventions randomisées dans nos courses avec courbe dose-réponse préenregistrée ; (b) expériences naturelles par différence de différences et contrôle synthétique ; (c) invariance entre environnements exploitée par apprentissage profond, découverte de structure, effets hétérogènes sous analyse de sensibilité. 3. Modèle d'agents étalonné et substitut neuronal, régression symbolique. 4. Transition de phase par intervention sur la dose de contact comparée à l'observation. 5. Validité : prédire correctement l'effet d'une intervention jamais vue, confirmé par une expérience naturelle indépendante ; sinon corrélat, pas cause. »
