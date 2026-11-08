# Compte rendu 04 — fille idéation 1, v1

Session `session_016QhUrujoj3FTuFNoYshNYB` (fille), mère `session_016QhUrrLeN21G7Z9KZobE42`.
Date : 2026-11-08, ~11:27–11:44 UTC (collisionneur) ; ~12:00 UTC (synthèse et devis).

## Objet

Achèvement de l'étage III du collisionneur v2.6 sur la question scellée du pilier attaque (antériorité et originalité). Tours T1, T2, T3 terminés. Synthèse d'antériorité et devis de la course d'organismes produits. Attente du mot de Lazar.

## Résultat complet de l'étage III (3 tours × 2 espèces + refus)

### Tours et cellules

| Cellule | Statut | Modèle servi | Jetons entrée | Jetons sortie | Caractères | Marqueur | Coût USD |
|---|---|---|---|---|---|---|---|
| E3-T1-conception-A | **REFUS** (bio) | Fable 5.1 | 5 132 | 97 | 0 | non | 0,06 |
| E3-T1-conception-B | OK | Opus 5.5 | 5 132 | 17 844 | 22 695 | oui | 0,38 |
| E3-T1-conception-C | OK (STOP) | Argon | 3 387 | 5 677 | 19 081 | oui | 0,32 |
| E3-T2-redteam-A | **REFUS** (cyber) | Fable 5.1 | 23 920 | 0 | 0 | non | 0,24 |
| E3-T2-redteam-B | OK | Opus 5.5 | 13 704 | 11 803 | 16 756 | oui | 0,29 |
| E3-T2-redteam-C | OK (STOP) | Argon | 10 346 | 4 195 | 15 213 | oui | 0,31 |
| E3-T3-riposte-A | — | — | — | — | — | — | — |
| E3-T3-riposte-B | OK | Opus 5.5 | 21 985 | 17 169 | 19 314 | oui | 0,43 |
| E3-T3-riposte-C | OK (STOP) | Argon | 13 982 | 7 051 | 23 007 | oui | 0,49 |

Absences acceptées par l'arbitre : E3-T1-conception-A, E3-T2-redteam-A, E3-T3-riposte-A (décision de Lazar, R-1789).

### Refus de Fable 5.1

Fable 5.1 a refusé sur les deux premiers tours avec des catégories différentes :
- **T1 (conception)** : catégorie `bio` (classifieur de biosécurité). Cause probable : le terme « organisme saboteur » (métaphore du programme).
- **T2 (équipe rouge)** : catégorie `cyber` (classifieur de cybersécurité). Cause probable : le contexte de red-teaming sur les moniteurs de sabotage.

Les deux refus sont cohérents avec le domaine du pilier attaque. Fable a été exclu de T3 sans appel (absence acceptée d'avance par l'arbitre pour les trois cellules A).

### Comportement de B (Opus 5.5) et C (Argon)

Opus 5.5 et Argon n'ont refusé sur aucun prompt des trois tours. Les six cellules B et C ont toutes produit un texte validé avec marqueur de fin. Aucun refus, aucune relance.

- **Opus 5.5** : 3 cellules, 46 816 jetons de sortie, 58 765 caractères, 1,10 USD.
- **Argon** : 3 cellules, 16 923 jetons de sortie, 57 301 caractères, 1,12 USD.
- Argon est plus concis en jetons mais produit un volume de caractères comparable (ratio caractères/jeton plus élevé).

## Erreur de périmètre (R-1791)

Lors de la deuxième relance du collisionneur (après le premier `--accepter-absence`), la commande n'a passé que `--accepter-absence E3-T1-conception-A` au lieu des trois cellules A. Le collisionneur a donc tenté E3-T2-redteam-A sur Fable 5.1, qui a refusé (catégorie « cyber »), coûtant 0,24 USD pour un résultat vide. C'est une erreur d'opérateur (la session fille), pas un contournement de refus. L'erreur a été consignée par la mère comme R-1791.

## Prompt caching (note de clôture)

Le gain potentiel du prompt caching sur le collisionneur v2.6 a été mesuré à ~8,6 % de la dépense Anthropic (~0,12 USD sur 1,40 USD), bien en dessous du seuil de 20 % qui justifierait un outil v2.7. La mère a confirmé : pas de v2.7 pendant ce run.

## Dépense

| Poste | Coût USD |
|---|---|
| Contrôles v1 + v2 | 0,002 |
| T1 conception (A REFUS + B + C) | 0,75 |
| T2 red team (A REFUS gaspillé R-1791 + B + C) | 0,84 |
| T3 riposte (B + C) | 0,92 |
| **Total collisionneur E3** | **2,52** |
| **Reste sur le plafond GO-2026-11-08-06** | **22,48** |

## Livrables produits

### Sur `donnees/ideation-pilier-attaque-v1`

1. **6 cellules validées** (T1-B, T1-C, T2-B, T2-C, T3-B, T3-C), scellées avec empreintes SHA256. Commits `48c27cb` (T1), `043d274` (T2), `579b4e0` (T3).
2. **Synthèse d'antériorité** (`synthese-anteriorite-pilier-attaque-v1.md`, empreinte `48adeac0`). Convergences B×C : évasion triviale non informative, 3 confondants fatals, 9 contrôles nécessaires, combinaison potentiellement non occupée (contrôle positif + non-infériorité + placebo + grille contrefactuelle + indépendance oracle + sas tiers + leave-one-family-out + 4 types de négatifs + diversité inter-familles). 4 références à vérifier sur pièce (R7). 3 zones vierges séduisantes (R8). Niveau méthode uniquement.
3. **Devis de la course d'organismes** (`devis-course-organismes-pilier-attaque-v1.md`, empreinte `c5cab7ce`). Trois scénarios : minimal (15 USD, 1 génération), modéré (35 USD, 2 générations, dépasse le reste du plafond), pire cas (65 USD). Recommandation : scénario minimal ou relèvement du plafond à 60 USD. Défaut sous 48 h : scénario minimal.

### Sur `rapports/fille-ideation-1-v1`

4. Ce compte rendu (CR-04).

## Conformité

- Aucune recette (procédé de fabrication de sabotage, évasion ou tromperie) dans aucun livrable.
- Aucune lecture de `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` ni `docs/notes/bras-attaque/`.
- Aucun refus de classifieur contourné ni reformulé.
- Aucun `git fetch` sans refspec.
- Aucune poussée vers `main` ni vers `lciric/controle-ia`.

## Prochaine action

Attente du mot de Lazar dans cette session :
- Validation de la synthèse d'antériorité (relecture « aucune recette ») ;
- Choix du scénario du devis (minimal / relèvement du plafond / autre) ;
- Mot pour lancer la course d'organismes (nœud de décision : dépense de calcul).

Aucune dépense de calcul ni lancement d'organisme avant ce mot.
