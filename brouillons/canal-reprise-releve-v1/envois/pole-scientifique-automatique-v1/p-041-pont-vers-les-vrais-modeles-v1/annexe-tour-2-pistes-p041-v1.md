# Annexe du tour 2 — pistes déjà proposées sur le pont P-041 → vrais modèles — v1

À servir **après** réception des réponses du tour 1 à `question-collisionneur-pont-p041-v1.md`. conv-audit (Fable 5.1), 31 octobre 2026. Chaque piste porte l'auteur et sa confiance ; les répondants les attaquent.

**Pistes de session-depot** (réponse relayée par Lazar, 07:52 heure de Paris) :
1. Séparer ce que l'arène certifie (une barrière sur une classe déclarée de déplacements de lois) de ce qu'elle promet ; le passage aux vrais modèles est une étape mesurée (débordement sur familles tenues à l'écart et bancs publics) ; Bailey devient une prédiction à tester, signe négatif permis.
2. Faire entrer la malléabilité dans la classe comme quantité bornée et mesurée : la classe devient « tout déplacement de loi sur les activations qu'une perturbation bornée des entrées peut produire à travers un substitut du modèle réel » ; la borne porte sur l'entrée ; la malléabilité est estimée sur un petit modèle public ; le générateur reste au niveau des lois et des bornes.
3. Changer l'objet certifié : le couple détection et coût (déjouer la sonde coûte de la capacité ; certificat sur la courbe « niveau de contournement → coût imposé »).
4. Examen final : rejouer le protocole de Bailey (défense figée, optimiseur sur les entrées d'un vrai modèle de 8 milliards de paramètres, plus de 70 tours) sur la défense sortie de l'arène contre la base de Bailey (défense entraînée sur les seules instances) ; contribution de P-041 = l'écart, préenregistré, signe négatif permis ; dépense de carte graphique.
Recommandation de session-depot : 1 + 2 + 4, confiance 0,6 ; 3 en mesure rapportée.

**Pistes de conv-audit** (`reponse-pont-p041-vrais-modeles-v1.md`, `comparaison-avec-session-depot-v1.md`) :
5. Remplacer « le défenseur connaît les paramètres de l'attaquant » par « le défenseur connaît le réseau substitut et borne l'atteignable » (certification en boîte blanche : propagation de bornes, lissage aléatoire, constantes de Lipschitz — outils SUPPOSÉ ; portée à l'échelle d'un modèle de langage à établir).
6. Mesurer la malléabilité avant de la borner : rayon de l'atteignable, nombre de recouvrement, **courbe de croissance par tour** ; si elle ne sature pas, « malléabilité bornée » n'est pas définie et la piste 2 certifie une classe qui ne couvre rien → la saturation se mesure **en premier** (données publiées de Bailey si elles existent, processeur ; sinon première mesure de l'examen final), prédiction envoyée aux auteurs.
7. Échelle à quatre barreaux (synthétique → famille ajustée → vrai modèle à attaquant borné → libre) avec, à chaque barreau, résidu hors famille et écart rayon atteint / rayon certifié ; signes et seuils écrits d'avance ; transformation d'invariance.
8. Piste 3 fragile en certificat (un coût connu est optimisable conjointement ; coûts tenus à l'écart ; lecture R4), bonne en mesure rapportée.
9. Vérification externe : rayon certifié recalculé par un outil tiers ; familles et attaques tenues à l'écart conçues par des tiers ; comparaison aux certificats existants contre suffixes adverses ; reproduire d'abord les chiffres publiés de Bailey.
Recommandation de conv-audit : 1 + 2 + 4 avec 6 en premier et conditionnant 2 ; 3 rapportée ; confiance 0,65.

**Sur la demande 2 du directeur (accès du défenseur aux paramètres pour la génération suivante)**, position commune des deux lignées à attaquer : légitime pour **apprendre** (c'est l'entraînement adverse ; P-041 l'utilise déjà sur les familles vues), illégitime pour **évaluer** (le score doit se lire sur des familles tenues à l'écart et sur l'adversaire adaptatif, l'attaque jouant en dernier) ; la question ouverte est de savoir si apprendre sur des paramètres de familles plutôt que sur des instances réduit l'écart (ii) − (iii) — c'est l'hypothèse de P-041 elle-même.
