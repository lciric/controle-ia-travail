# Devis — expérience sur modèle ouvert du papier D, en deux étages — v1

Pièce décisive (classe A), brouillon à contre-lire par un Opus 5.5 neuf avec le préenregistrement `preenregistrement-modele-ouvert-v1.md`, dont il chiffre le plan. Rien n'est loué. Écrit par Claude Fable 5.2 le 24 novembre 2026.

**Demande à Lazar, après contre-lecture et scellement : un GO pour l'étage 1 seul, plafonné à 50 heures de carte graphique.** L'étage 2 fera l'objet d'un complément de devis recalculé sur les débits mesurés, et d'un second GO.

## 1. Règles du chiffrage

- Unité : l'heure de carte graphique, sur une carte d'au moins 24 Go de mémoire (hypothèse à vérifier à l'étage 1 ; sinon une carte de 48 Go, à un autre prix).
- **Prix horaire : à relever et dater au moment du GO**, avec le fournisseur et le modèle de carte. Coût de calcul = heures × prix relevé. Aucun prix n'est avancé ici.
- Aucun appel d'interface payant : les deux moniteurs sont locaux et comptés dans les heures de carte. Bac à sable et sondes sur le processeur de la machine louée, sans surcoût.
- Toute fourchette va du cas rapide et court au cas lent et long. Aucun chiffre ne vient de l'état de l'art ; celui de Carbon n'est pas repris.

## 2. Hypothèses explicites — toutes à remplacer par la mesure de l'étage 1

| Grandeur | Hypothèse |
|---|---|
| Génération par lots, modèle de 7 milliards de paramètres | 800 à 2 500 jetons générés par seconde |
| Lecture seule (moniteurs, activations) | 8 000 à 25 000 jetons lus par seconde |
| Affinage des adaptateurs | 2 000 à 6 000 jetons par seconde |
| Temps fixe par phase (chargements, bac à sable) | 4 à 10 minutes |
| Jetons générés par épisode (pensée et code) | 350 à 550 |
| Exemple d'affinage (énoncé, pensée, code) | 850 à 1 050 jetons |
| Entrée du moniteur en boucle ; du moniteur d'audit | 700 ; 1 000 jetons |
| Installation d'une machine (poids, environnement) | 0,5 à 1 heure |
| Marge de relance pour panne | 25 % des heures |

Estimations d'ingénierie, non mesures : l'étage 1 existe pour les remplacer.

## 3. Charges unitaires, d'après le préenregistrement

**Un bras pour une graine** (quatre tours ; le tour 0 est partagé) :

| Poste | Volume | Heures de carte |
|---|---|---|
| Génération : trois tours d'entraînement (1 800 épisodes chacun) et évaluation finale (2 400) | 2,7 à 4,3 millions de jetons générés | 0,3 à 1,5 |
| Moniteurs : en boucle sur 7 800 épisodes, audit sur 2 400 | 7,9 millions de jetons lus | 0,1 à 0,3 |
| Affinage : quatre tours, 1 800 exemples, deux passes | 12 à 15 millions de jetons | 0,6 à 2,1 |
| Temps fixe : cinq phases | | 0,3 à 0,8 |
| **Total** | | **1,3 à 4,7** |

**Un départ pour une graine et une dose** (amorçage sur 2 000 démonstrations, épisodes du tour 0, moniteurs) : 0,5 à 1,9 heure.

**Une passe d'activations pour les sondes** (4 200 épisodes réencodés) : 0,04 à 0,14 heure ; quatre passes par graine.

## 4. Étage 1 — étalonnage, plafonné

| Poste | Contenu | Heures de carte |
|---|---|---|
| Débits | génération, lecture, affinage, sur des lots courts | 1 à 2 |
| Masses initiales des strates | modèle de base, 8 épisodes sur chaque tâche, deux moniteurs | 0,2 à 0,9 |
| Démonstrations d'amorçage | environ 8 000 épisodes sous consigne explicite, triés par programme | 0,4 à 1,7 |
| Amorçages | jusqu'à quatre parts de triche candidates à dose faible, la dose forte, le témoin positif, chacun avec son tour 0 | 3,1 à 11,4 |
| Validation des détecteurs | cas plantés, sur processeur | 0 |
| Contrôle positif | lu sur le témoin amorcé ci-dessus | compris |
| Pilote de variance | quatre graines, deux tours, bras sans filtre et bras au hasard | 7,5 à 27,2 |
| Installation | une à trois machines | 1 à 3 |
| **Total** | | **13 à 46** |

**Plafond : 50 heures de carte**, soit 50 fois le prix relevé. Ordre de priorité si le plafond approche : débits, détecteurs, masses, contrôle positif, puis pilote. Plafond atteint : arrêt, versement des sorties, retour à Lazar. La marge de relance de l'étage 1 est dans le plafond.

L'étage 1 ne court ni le rejet répété ni la pénalité et ne lit aucun contraste décisif. Ses livrables : la table des débits mesurés, les masses et survies, les détecteurs validés, le contrôle positif, l'écart-type des différences appariées, la fiche de prédictions (nombre de paires, pression, signes prédits) et le complément de devis.

## 5. Étage 2 — course, par tranche et par nombre de paires de graines

Le nombre de paires n sort de la simulation de puissance de l'étage 1 (entre 6 et 12 ; valeur de plan 9). Heures de carte, hors marge :

| Tranche | Contenu | n = 6 | n = 9 | n = 12 |
|---|---|---|---|---|
| A | contraste principal : quatre bras (sans filtre, rejet répété, pénalité, filtre au hasard), départs à dose faible, témoin positif | 35 à 127 | 52 à 189 | 69 à 251 |
| B | mesure adossée : activations pour la sonde figée et la sonde réapprise | 1 à 3 | 2 à 5 | 2 à 7 |
| C | dose d'amorçage : bras de pénalité à dose forte et ses départs | 11 à 40 | 16 à 59 | 22 à 79 |
| **A + B + C** | | **47 à 169** | **70 à 253** | **93 à 337** |
| avec la marge de relance de 25 % | | 58 à 212 | 87 à 316 | 116 à 421 |

Chaque bras, pour chaque graine, coûte la charge unitaire du § 3 : la tranche A compte 4n bras, n départs et le témoin positif ; la tranche C, n bras et n départs. S'ajoute l'installation : 0,5 à 1 heure par machine. Les heures se répartissent sur plusieurs cartes sans changer le total.

**Ce que chaque tranche achète.** La tranche A porte le contraste principal, ses contrôles négatifs, et déjà la lecture à dose faible du second contraste (le bras de pénalité y figure). La tranche B ajoute la mesure adossée pour quelques heures. La tranche C ajoute la dose forte, sans laquelle la dépendance à la dose reste « non éprouvée ». Un seul contraste financé : A. Deux : A et B. Trois : A, B et C.

La fourchette est large (facteur proche de quatre) faute de débit mesuré ; le complément de devis la resserrera.

## 6. Stockage

- Sur la machine louée : poids des deux modèles, adaptateurs, épisodes ; demander 150 Go de disque (hypothèse). Prix du disque : à relever au GO.
- Sorties à verser avant toute destruction de machine (hypothèses) : environ 430 000 épisodes pour n = 9, soit quelques gigaoctets de texte avec manifestes et activations ; adaptateurs, 0,1 à 0,2 Go chacun, soit 6 à 13 Go pour les départs et les états finaux, 20 à 40 Go avec tous les tours.
- Les épisodes, manifestes et empreintes vont sur une branche du dépôt de travail. Le lieu durable des adaptateurs est une question posée à Lazar ; son coût est à relever.

## 7. Relances et pannes

Une panne technique n'est pas un résultat : la course arrêtée est relancée avec les mêmes graines, sur le même GO, dans la marge de 25 %. Le taux d'interruption observé à l'étage 1 remplacera cette marge. Marge épuisée : arrêt et retour à Lazar, sans lecture partielle.

## 8. Hors devis

Réplication sur une seconde famille de modèles ; gradient de politique et normalisation par groupe ; plusieurs niveaux de pénalité ; temps des agents et des contre-lectures.

## 9. Contre-lecture

En attente. Le contre-lecteur recalcule les tables à partir des hypothèses du § 2 et des tailles du préenregistrement ; script de calcul : `calc/devis_calc.py`, à verser avec le devis.
