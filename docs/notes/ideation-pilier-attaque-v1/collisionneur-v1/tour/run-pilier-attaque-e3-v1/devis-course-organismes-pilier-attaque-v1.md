# Devis de la course d'organismes — pilier attaque (idéation, étage III)

Date : 2026-11-08.
Source : coûts unitaires mesurés sur le run `run-pilier-attaque-e3-v1` (collisionneur v2.6, 6 cellules validées).
Statut : **DEVIS ILLUSTRATIF** ; aucune dépense avant le mot de Lazar (nœud de décision, hiérarchie « dépense de calcul »).
GO applicable : GO-2026-11-08-06, plafond 25 USD, dont 2,52 USD déjà dépensés (collisionneur E3).

---

## 1. Coûts unitaires mesurés (collisionneur E3)

| Cellule | Modèle | Entrée (jetons) | Sortie (jetons) | Caractères | Coût (USD) |
|---|---|---|---|---|---|
| E3-T1-conception-B | Opus 5.5 | 5 132 | 17 844 | 22 695 | 0,38 |
| E3-T1-conception-C | Argon | 3 387 | 5 677 | 19 081 | 0,32 |
| E3-T2-redteam-B | Opus 5.5 | 13 704 | 11 803 | 16 756 | 0,29 |
| E3-T2-redteam-C | Argon | 10 346 | 4 195 | 15 213 | 0,31 |
| E3-T3-riposte-B | Opus 5.5 | 21 985 | 17 169 | 19 314 | 0,43 |
| E3-T3-riposte-C | Argon | 13 982 | 7 051 | 23 007 | 0,49 |

**Observations** :
- Opus 5.5 : 0,29 à 0,43 USD par appel ; le coût monte avec le contexte (les pièces des tours précédents).
- Argon : 0,31 à 0,49 USD par appel ; même tendance.
- Coût moyen par appel validé : Opus 0,37 USD, Argon 0,37 USD.
- Un appel de tour 1 (prompt court, pas de pièces antérieures) coûte ~0,35 USD ; un appel de tour 3 (prompt long, 2 pièces) coûte ~0,46 USD.
- Fable 5.1 : 0,06 à 0,24 USD par appel (REFUS dans les deux cas, aucun texte produit).

---

## 2. Structure de la course d'organismes

L'organisme d'idéation n'est PAS lancé dans ce run (absence de garde de refus — R-468). Le devis porte sur une course future, conditionnée au mot de Lazar.

### 2.1 Rôles et appels estimés

| Rôle | Description | Espèces | Appels par génération | Contexte attendu |
|---|---|---|---|---|
| **Proposeurs** | Génèrent des conceptions expérimentales à partir de la synthèse et des contraintes | B (Opus 5.5) et C (Argon) | 2 par espèce × nombre de familles de conceptions | Prompt court (~5 000 jetons d'entrée) |
| **Passes** (sélection) | Évaluent les propositions, classent, éliminent | B et C | 2 par lot de propositions | Prompt moyen (~10 000–15 000 jetons d'entrée) |
| **Juges** | Évaluent la qualité méthodologique selon les critères du programme | B et C (croisés : le juge n'est pas de la même espèce que le proposeur) | 2 par proposition retenue | Prompt long (~15 000–20 000 jetons d'entrée) |
| **Témoins** | Contrôlent que les propositions restent au niveau méthode (pas de recette) et respectent l'aveuglement | B ou C (un seul suffit) | 1 par proposition retenue | Prompt moyen |
| **Sonde de la garde** | Vérifie l'absence de contournement de refus, de fuite d'aveuglement, de recette | Fable 5.1 (si disponible) ou vérification programmatique | 1 par proposition retenue | Prompt court |
| **Contrôles** | Contre-lecture (N-052), vérification de cohérence avec la synthèse d'antériorité | B et C (croisés) | 1 par proposition finale | Prompt long |

### 2.2 Scénarios de coût

**Hypothèses communes** :
- Le coût par appel est estimé à partir des mesures du collisionneur, ajusté par la taille du contexte.
- Appel court (proposeur, sonde de la garde) : ~0,35 USD (Opus ou Argon), ~0,10 USD (Fable).
- Appel moyen (passe, témoin) : ~0,40 USD.
- Appel long (juge, contrôle) : ~0,45 USD.
- Fable 5.1 peut refuser sur le domaine du pilier attaque (observé : REFUS « bio » et « cyber »). La sonde de la garde est alors assurée par vérification programmatique (coût nul).

| Scénario | Générations | Propositions par génération | Appels totaux estimés | Coût estimé (USD) |
|---|---|---|---|---|
| **Minimal** (1 génération, 4 propositions par espèce) | 1 | 8 | ~40 | 15 |
| **Modéré** (2 générations, 6 propositions par espèce) | 2 | 12 | ~90 | 35 |
| **Pire cas** (3 générations, 8 propositions par espèce, relances sur refus) | 3 | 16 + relances | ~160 | 65 |

---

## 3. Plafond et recommandation

| Ligne | USD |
|---|---|
| Déjà dépensé (collisionneur E3) | 2,52 |
| Reste disponible (GO-2026-11-08-06, plafond 25 USD) | 22,48 |
| Devis modéré (recommandé) | 35 |
| Devis pire cas | 65 |

**Le scénario modéré dépasse le reste disponible de 12,52 USD.** Le pire cas le dépasse de 42,52 USD.

### Recommandation

Deux options :

1. **Scénario minimal dans l'enveloppe existante** (15 USD, 1 génération, 4 propositions par espèce). Tient dans le plafond actuel. Produit un premier jeu de conceptions évaluées, mais sans itération.

2. **Relèvement du plafond à 60 USD** pour le scénario modéré (35 USD) avec une marge de 10 USD pour les relances et les contrôles imprévus. Demande un nouveau GO ou un avenant au GO-2026-11-08-06.

**Confiance** : moyenne. Les coûts unitaires sont mesurés sur le collisionneur (3 tours, 6 cellules), mais l'organisme d'idéation a une structure différente (plus de rôles, prompts plus variés). L'incertitude principale porte sur le nombre de refus de Fable 5.1 (qui renchérit si une espèce de remplacement est nécessaire) et sur le nombre de générations (décision de l'arbitre).

**Défaut sous 48 heures** : scénario minimal (option 1), puisqu'il tient dans le plafond actuel.

---

## 4. Éléments hors devis

Les éléments suivants ne sont pas couverts par ce devis et nécessitent un devis séparé :

- Garde de refus de l'organisme d'idéation (R-468, à construire avant le lancement).
- Calcul GPU pour les expériences issues de la course (les budgets illustratifs des cellules vont de 90 à 10 000 USD selon l'espèce et l'architecture).
- Vérification des références d'antériorité sur PDF empreintés (R7).
- Audit humain de l'oracle (illustratif : 80 heures-personne chez B-T3).
