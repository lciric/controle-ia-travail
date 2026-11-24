# Devis — expérience sur modèle ouvert du papier D, en deux étages — v2

Pièce décisive (classe A). Cette v2 remplace la v1, gardée intacte, après contre-lecture (rapport `22f0fd697697c29998eaf20b933ab3429286ce849ac87aac7958fb95956f22e3` ; corrections dans `table-corrections-v2.md`). Elle chiffre `preenregistrement-modele-ouvert-v2.md`. Rien n'est loué. Claude Fable 5.2, 24 novembre 2026. Tables : `calc/devis_calc_v2.py`.

**Demande à Lazar, après vérification et scellement : un GO pour l'étage 1 seul, plafonné à 86 heures de carte graphique, marge de relance comprise.** L'étage 2 fera l'objet d'un complément de devis sur débits mesurés et d'un second GO.

## 1. Règles du chiffrage

- Unité : l'heure de carte, sur une carte d'au moins 24 Go (hypothèse). Génération et affinage n'y tiennent pas ensemble : rechargement à chaque phase, compté dans le temps fixe. Un passage à 48 Go change le prix et peut-être les heures : complément de devis.
- **Prix horaire : à relever et dater au moment du GO.** Le GO consigne aussi le fournisseur, la carte, le plafond en euros, le prix du disque et le lieu durable des adaptateurs. Coût = heures × prix relevé ; aucun prix n'est avancé ici.
- Aucun appel d'interface payant dans la chaîne de mesure : moniteurs locaux, comptés dans les heures ; sondes et détecteurs sur le processeur de la machine.
- Fourchettes : du cas rapide et court au cas lent et long. Aucun chiffre ne vient de l'état de l'art ni de Carbon.

## 2. Hypothèses explicites — toutes à remplacer par la mesure de l'étage 1

| Grandeur | Hypothèse |
|---|---|
| Génération par lots | 800 à 2 500 jetons générés par seconde |
| Lecture seule (moniteurs, activations) | 8 000 à 25 000 jetons lus par seconde |
| Affinage des adaptateurs | 1 200 à 5 000 jetons par seconde |
| Exécution des tests dans le bac à sable, sur les cœurs de la machine | 5 à 30 épisodes par seconde, comptée sans recouvrement avec la carte |
| Temps fixe par phase (rechargements) | 4 à 10 minutes |
| Jetons générés par épisode ; par exemple d'affinage | 350 à 550 ; 850 à 1 050 |
| Jetons lus par épisode : moniteur en boucle ; audit ; sondes | 700 ; 1 000 ; 950 |
| Installation d'une machine | 0,5 à 1 heure |
| Marge de relance pour panne | 25 % des heures |

Estimations d'ingénierie, non mesures. Recouvrement des tests avec les moniteurs, nombre de cœurs et tenue sur 24 Go : mesurés à l'étage 1.

## 3. Charges unitaires

**Un bras pour une graine** (quatre tours ; tour 0 partagé ; 7 800 épisodes) :

| Poste | Volume | Heures de carte |
|---|---|---|
| Génération | 2,7 à 4,3 millions de jetons | 0,3 à 1,5 |
| Tests | 7 800 épisodes | 0,1 à 0,4 |
| Moniteurs | 7,9 millions de jetons lus | 0,1 à 0,3 |
| Affinage | 12 à 15 millions de jetons | 0,7 à 3,5 |
| Temps fixe, cinq phases | | 0,3 à 0,8 |
| **Total** | | **1,5 à 6,5** |

**Un départ** (amorçage sur 2 000 démonstrations, 4 200 épisodes du tour 0, tests, moniteurs, deux phases) : 0,6 à 2,5 heures. Les démonstrations sont construites par programme, sans carte, et tirées de nouveau pour chaque graine. **Une passe d'activations** (4 200 épisodes) : 0,04 à 0,14 heure ; quatre par graine.

## 4. Étage 1 — étalonnage, plafonné, dans l'ordre d'exécution

| | Poste | Heures de carte |
|---|---|---|
| 1 | Installation, une à deux machines | 0,5 à 2 |
| 2 | Débits et bac à sable | 1 à 2 |
| 3 | Modèle de base : dix épisodes sur les 542 tâches non mutées (critère des témoins, négatifs naturels, matière de l'amorçage) | 0,3 à 1,5 |
| 4 | Négatifs frais du détecteur principal : 1 000 épisodes | 0,1 à 0,4 |
| 5 | Départs d'étalonnage à dose faible : deux à cinq parts de triche | 1,2 à 12,6 |
| 6 | Témoin positif | 0,6 à 2,5 |
| 7 | Départs du pilote : quatre, et jusqu'à trois remplacements | 2,3 à 17,7 |
| 8 | Bras du pilote : quatre graines, deux bras, deux tours | 6,2 à 27,1 |
| 9 | Départ à dose forte | 0,6 à 2,5 |
| | **Total** | **13 à 68** |
| | **avec la marge de 25 %** | **16 à 86** |

Validation des détecteurs, cas plantés et revalidation du lexique : sans carte.

**Plafond : 86 heures, marge comprise.** Règles :
- après le poste 2, le script recalcule la table sur les débits mesurés ; si le total avec marge dépasse le plafond, arrêt avant le poste 3 et retour à Lazar ;
- le pilote, dont dépend la fiche de prédictions, passe avant tout ce qui n'en dépend pas : le seul poste abandonné si le plafond approche est le poste 9, et le bras à dose forte n'est alors pas couru ; le pilote n'est jamais réduit ;
- une garde lit les heures facturées par l'interface du fournisseur avant chaque phase (horloge murale à défaut) ; elle est éprouvée sur un cas sain et deux artefacts ;
- plafond atteint : arrêt, versement des sorties, retour à Lazar.

L'étage 1 ne court ni rejet répété ni pénalité et ne lit aucun contraste décisif. Livrables : débits, banque répartie, détecteurs validés, contrôle positif, fiche de prédictions, complément de devis.

## 5. Étage 2 — course, par tranche et par nombre de paires de graines

Le nombre de paires n sort de la fiche (8 à 12 ; valeur de plan 9). Heures de carte :

| Tranche | Contenu | n = 8 | n = 9 | n = 12 |
|---|---|---|---|---|
| A | contraste principal : 4n bras, n départs, témoin positif, jusqu'à trois départs de remplacement, installation d'une à quatre machines | 53 à 243 | 59 à 272 | 79 à 358 |
| B | mesure adossée : activations des sondes | 1 à 4 | 2 à 5 | 2 à 7 |
| C | dose forte : n bras de pénalité, n départs, jusqu'à trois remplacements | 16 à 80 | 19 à 89 | 25 à 116 |
| **A + B + C** | | **71 à 328** | **80 à 366** | **106 à 481** |
| A seule, avec la marge de 25 % | | 66 à 304 | 74 à 340 | 99 à 447 |
| A + B + C, avec la marge | | 89 à 410 | 100 à 457 | 132 à 601 |

**Ce que chaque tranche achète.** A : le contraste principal, ses contrôles, et la lecture à dose faible du second contraste. B : la mesure adossée. C : la dose forte, sans laquelle la dépendance à la dose reste « non éprouvée » ; elle n'est courue que si la fiche le permet. **Décision ouverte (O4 du préenregistrement) ; repli : tranche A seule.** Si le bras de pénalité est retiré (repli de O1), la tranche A perd un quart de ses bras et la tranche C disparaît.

La fourchette est large (facteur de quatre à cinq) faute de débit mesuré ; le complément de devis la resserrera. Une banque réduite (facteur 0,80 au moins) abaisse les heures à peu près d'autant.

## 6. Stockage

- Sur la machine : 150 Go de disque (hypothèse).
- À verser avant toute destruction de machine (hypothèses) : environ 431 000 épisodes pour n = 9 et les trois tranches, témoin positif compris, soit quelques gigaoctets ; adaptateurs de 0,1 à 0,2 Go chacun, 6 à 13 Go pour les départs et les états finaux, 20 à 40 Go avec tous les tours.
- Épisodes, manifestes et empreintes : branche du dépôt de travail. Lieu durable des adaptateurs : à fixer par le GO.

## 7. Relances et pannes

Une panne technique n'est pas un résultat : relance, mêmes graines, même GO, dans la marge. Le taux d'interruption observé à l'étage 1 remplacera les 25 %. Marge épuisée : arrêt, retour à Lazar, sans lecture partielle.

## 8. Hors devis

Réplication sur une seconde famille ; gradient de politique ; niveaux de pénalité ; temps des agents, des lecteurs et des contre-lectures.

## 9. Contre-lecture

Contre-lecture 1 : devis v1 `6c5e736f8c77704a43c527f1b6ee28c67b2fc45bc9b16d2e96649b6da73bcabc`, rapport cité en tête, verdict « scellable après corrections ». Vérification des corrections par le même contre-lecteur : en attente.
