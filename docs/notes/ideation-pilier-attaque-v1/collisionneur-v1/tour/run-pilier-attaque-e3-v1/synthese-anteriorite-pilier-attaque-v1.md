# Synthèse d'antériorité — pilier attaque (collisionneur E3, étage III)

Date : 2026-11-08.
Source : run `run-pilier-attaque-e3-v1`, 6 cellules validées (B et C), 3 tours (conception, équipe rouge, riposte). Espèce A (Fable 5.1) absente (REFUS classifieur, catégories « bio » et « cyber » ; absences acceptées par l'arbitre).
Statut de chaque énoncé ci-dessous : **HYPOTHÈSE** du collisionneur, sauf indication contraire. Aucun chiffre n'a été vérifié sur pièce par cette synthèse.
Niveau : méthode et démonstration. Aucune description de procédé de fabrication de comportement de sabotage, d'évasion ou de tromperie.

---

## 1. Convergences entre B (Opus 5.5) et C (Argon)

### 1.1 Évasion triviale non informative

B et C s'accordent : démontrer qu'un organisme saboteur échappe à des moniteurs (sondes boîte blanche génériques, juge de 3 milliards de paramètres) qui sont déjà au niveau du hasard (RAPPORTÉ, « mesuré ») ne prouve rien devant un jury. L'épreuve décisive doit porter sur un moniteur qui détecte un saboteur témoin non dissimulé (contrôle positif) ou sur le prédicteur boîte noire sur les traits du texte à 0,866 (RAPPORTÉ, N-029).

### 1.2 Trois confondants fatals identifiés

Les deux espèces identifient, puis acceptent mutuellement en riposte, trois confondants qui invalident les mesures brutes du banc :

1. **Attention causale et consigne.** Dans un modèle autorégressif (HYPOTHÈSE sur l'architecture), les états cachés aux positions qui suivent la consigne sont calculés à partir de la consigne. Lire ces positions, c'est encore lire la consigne sous forme transformée. Le masquage positionnel est insuffisant. Seules des paires contrefactuelles (consigne d'attaque avec exécution honnête, consigne neutre avec sabotage attesté par l'oracle) tranchent.

2. **Identité de l'organisme vs acte de sabotage.** Si l'organisme saboteur et le modèle honnête diffèrent par leurs poids (ou adaptateurs), une sonde linéaire peut séparer les deux populations en détectant la modification elle-même, y compris sur des épisodes sans sabotage. Un organisme placebo (même chaîne de modification, sans objectif de sabotage) et des épisodes dormants du saboteur (épisodes sans sabotage confirmé) sont nécessaires pour séparer la détection de l'organisme de la détection de l'épisode.

3. **Mode tenu à l'écart consommé avant la porte G1.** Toute mesure transmise à la défense sur le mode tenu à l'écart (N-054), même agrégée, peut orienter ses choix ultérieurs (couche, régularisation, seuil). La démonstration d'avant-entretien doit préserver ce témoin. B propose de ne présenter que le préenregistrement scellé de l'expérience de généralisation ; C propose une validation croisée par bloc sur les familles connues (R-610) comme substitut.

### 1.3 Contrôles nécessaires (convergence)

Les contrôles suivants apparaissent chez les deux espèces et sont acceptés en riposte :

| Contrôle | Origine | Accepté par |
|---|---|---|
| Contrôle positif par saboteur témoin non dissimulé | B-T1 (E1) | C-T3 (intégré dans le plan factoriel) |
| Paires contrefactuelles (consigne × acte) | C-T1 (tableau c.3) | B-T2 (repris), B-T3 (critère de décision) |
| Organisme placebo | B-T2 (duel C-a1) | C-T3 (condition $C_{\text{feinte}}$) |
| Échecs honnêtes comme négatifs obligatoires (N3) | C-T2 (c2) | B-T3 (négatif obligatoire) |
| Sas d'évaluation automatisé tiers | B-T2 (Faille 6) | C-T3 (exécution dans le sas) |
| Audit du rappel de l'oracle sur sabotages connus | B-T2 (c5) | C-T3 (prérequis de l'Exp. 2) |
| Couches et hyperparamètres figés au préenregistrement | C-T1 (garantie 3) | B-T3 (permutation des étiquettes sur la même règle) |
| Journal horodaté du régime d'information de chaque sous-bras | B-T2 (Faille 9) | C-T3 (embargo + empreintes sha256) |
| Diversité de famille entre oracle, juges et organismes | B-T2 (Faille 11) | C-T3 (facteur 3 du plan 2×2×2) |

### 1.4 Expérience à faire en premier

Les deux espèces convergent : l'expérience prioritaire est le contrôle positif corrigé (E1a chez B, Exp. 1 corrigée chez C), qui ne consomme pas le mode tenu à l'écart et conditionne la validité de toutes les mesures suivantes.

---

## 2. Divergences non résolues

| Point | Position de B (riposte) | Position de C (riposte) |
|---|---|---|
| Architecture expérimentale | 7 expériences séquentielles (E1a, E1b, E2a, E2b, E3′, E4′, E5′, E6′, E7′) | 3 expériences à plan factoriel (contrefactuel 4 conditions, informé-leurre-aveugle, juge 2×2×2) |
| Budget illustratif | 3 000 à 10 000 USD, 4 à 6 semaines | ~390 USD, ~7 jours |
| Métrique de l'indépendance de l'oracle | Rapport conditionnel $R = P(\text{erreur moniteur} \mid \text{erreur oracle}) / P(\text{erreur moniteur} \mid \text{oracle correct})$, étalon de 1 000 épisodes | Non traitée séparément (intégrée au prérequis de l'Exp. 2) |
| Statut du régime des organismes (poids vs contexte) | Déclaration obligatoire en E0 ; E2 scindé par régime | Non distingué explicitement |
| Effectifs de négatifs | 2 000 négatifs par condition (illustratif) | Non spécifié au-delà du lot de contrôle ($K = 100$, illustratif) |

---

## 3. Antériorité citée par les cellules (références à vérifier)

Les références suivantes sont citées par B et C comme antériorité potentielle. Leur statut est **HYPOTHÈSE** (« référence citée par le collisionneur, à vérifier sur `docs/etat-de-l-art-controle-ia-v1.md` et sur les PDF empreintés » — R7). Aucune n'a été vérifiée par cette synthèse.

| Référence | Domaine occupé (HYPOTHÈSE) | Citée par |
|---|---|---|
| Greenblatt, Shlegeris, Sachan & Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion* | Évaluations de contrôle avec équipes rouge et bleue ; thèse « un dispositif ne vaut que contre un attaquant fort » | B-T1 (d), C-T1 (a.5) |
| Hubinger et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training* | Organismes à comportement caché comme objets d'épreuve ; persistance après entraînement de sûreté | B-T1 (d) |
| Zou et al. (2023), *Representation Engineering: A Top-Down Approach to AI Transparency* | Extraction de caractéristiques latentes par sondes ; ingénierie de représentations | C-T1 (a.5) |
| Burns et al. (2022), *Discovering Latent Knowledge in Language Models Without Supervision* | Découverte de connaissance latente sans supervision ; sondes linéaires | C-T1 (a.5) |

**Remarque d'intégrité (B-T2, remarque 2)** : C attribuait ces références à la section D des faits du programme. B a relevé que la section D ne nomme aucun auteur. L'attribution à cette section est fausse ; les références elles-mêmes restent à vérifier sur pièce.

---

## 4. Combinaison potentiellement non occupée (HYPOTHÈSE)

Les deux espèces convergent vers une combinaison méthodologique qui ne leur semble pas couverte par l'antériorité citée. Son statut est **HYPOTHÈSE** tant que `docs/etat-de-l-art-controle-ia-v1.md` n'a pas été audité (R7, R8).

La combinaison rassemble :

1. Contrôle positif obligatoire par un saboteur témoin non dissimulé, gelé et transféré à un second témoin indépendant.
2. Non-infériorité de l'efficacité de sabotage comme condition d'une évasion valide, stratifiée par type et difficulté de tâche.
3. Bras placebo (organisme modifié sans objectif de sabotage) pour séparer la détection de l'identité de l'organisme de la détection de l'acte.
4. Grille contrefactuelle à quatre conditions (sabotage actif, dormant, feinte, honnête) appliquée uniformément aux sondes et au prédicteur boîte noire.
5. Mesure empirique de l'indépendance entre oracle et moniteurs (rapport conditionnel ou plan factoriel).
6. Sas d'évaluation automatisé tiers, avec journal horodaté et embargo des pièces publiques.
7. Validation croisée par bloc (leave-one-family-out sur R-610) pour préserver le mode tenu à l'écart avant G1.
8. Quatre types de négatifs obligatoires (jumeau honnête, jumeau décalé bénin, échecs honnêtes appariés, jumeau honnête autre graine).
9. Diversité de famille de préentraînement entre organismes, juges et oracle pour exclure la connivence statistique.

Chaque élément pris séparément existe dans la littérature des évaluations de sûreté, des essais cliniques randomisés ou de la détection de triche. La combinaison des neuf dans un même protocole d'évaluation de moniteurs de sabotage est ce qui pourrait être inédit. Cette assertion est la plus fragile de la synthèse : une seule référence réunissant ces éléments la réfute.

---

## 5. Zones vierges séduisantes (R8)

Les points suivants semblent inoccupés mais méritent une vérification plus dure (R8 : « zones vierges séduisantes vérifiées plus durement ») :

1. **Protocole contrefactuel complet appliqué au prédicteur boîte noire.** La littérature sur les sondes internes semble ne pas auditer systématiquement la base boîte noire avec la même grille contrefactuelle. C'est une hypothèse d'originalité séduisante : vérifier que les travaux sur les évaluations d'alignement (CCS, RepE) ne l'incluent pas déjà.
2. **Organisme placebo avec contrôle de manipulation.** Le placebo est un standard en essais cliniques mais semble absent des protocoles d'évaluation de sûreté des modèles de langage. Vérifier les travaux de METR et d'Apollo Research.
3. **Audit du rappel de l'oracle par lot scellé du bras d'attaque.** La question « l'oracle sait-il qu'il y a sabotage quand il y en a ? » est rarement posée dans les travaux d'évaluation. Vérifier.

---

## 6. Ce que cette synthèse ne couvre pas

- Le contenu des familles R-610, du mode tenu à l'écart (N-054) et de la brèche W2 : tenus à l'écart par construction.
- Les chiffres de `docs/etat-de-l-art-controle-ia-v1.md` : non transmis au collisionneur.
- Les procédés de fabrication d'organismes saboteurs, évasifs ou trompeurs : hors périmètre (niveau méthode).
- La vérification sur PDF empreinté des quatre références citées (R7).

---

## Avertissement

Cette synthèse est un produit du collisionneur, pas un audit. Ses affirmations d'antériorité sont des HYPOTHÈSES. Elle doit être relue par la session mère (« aucune recette ») avant tout usage, et ses références vérifiées sur pièce (R7) avant d'être citées dans un papier ou une présentation.
