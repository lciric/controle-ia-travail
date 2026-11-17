# Organismes saboteurs ultra discrets, famille (v) — devis — v1

- **Objet** : chiffrer la course de conception et de vérification décrite par `docs/notes/organismes-discrets-v1/conception-organismes-discrets-v1.md` et par le brouillon de préenregistrement `prereg-organismes-discrets-v1-brouillon1.md`, par ligne de GO.
- **Cadre** : GO-2026-11-17-02 autorise la **conception**, **aucune dépense ni aucun lancement** sans devis contre-lu et GO de calcul. Ce document est le devis ; **il n'engage rien**. La garde de calcul du dépôt exige un `GO_ID` valide de `registres/go.md` à tout lancement d'instance payante.
- **Date** : 2026-11-17, à partir de 00:48 UTC (`date -u`).
- **Auteur** : rédacteur neuf (modèle A de la synthèse). Aucune machine lancée, aucun appel de modèle payant, aucune valeur de clé lue pour l'écrire.

## 1. Prix et hypothèses — ce qui est relevé, ce qui est à relever

**Prix horaires relevés**, source citée, non estimés : relevé du **2026-11-17T00:20:51Z** inscrit à la ligne `R-3048` de `registres/decisions.md` —

| carte | prix relevé | remarque de la source |
|---|---|---|
| RTX 5090 | **0,4860 USD/h** | « prise en charge par torch non vérifiée » — à vérifier avant usage |
| A100 SXM4 40 Go | **0,5494 USD/h** | — |
| RTX 6000 Ada | **0,5614 USD/h** | — |

Le devis chiffre sur **0,4860 USD/h** et donne la sensibilité à 0,5614 (+ 15,5 %). **Trafic et stockage : à relever** (la source de R-3048 dit « hors trafic »).

**Repères de dépense du dépôt**, cités comme repères et non comme prix de cette course : plafond de la course de T0.6, **200 USD** (clé `plafond_usd` de `prereg/T0.6-organismes-config-7b-v1.json`) ; devis attendu de (ii-b), **13 à 21 USD** (sa conception, section 0) ; ligne de notation de N-063 v2, **≤ 10 USD**.

**Hypothèse de débit — À RELEVER, et c'est la seule inconnue qui compte.** Tout le devis se convertit en heures de carte par une seule hypothèse : **2 000 « unités d'action » par heure de carte**, une unité valant une action de 400 jetons au plus en lot de 8, au modèle du programme en demi-précision. **Cette valeur n'est pas mesurée** : elle est une hypothèse de travail, et elle est à relever par une passe de dix minutes avant toute demande de GO de la ligne L2. La sensibilité est donnée au § 4 : c'est le seul facteur qui peut tripler la facture, et il est borné par les plafonds proposés.

**Conversions déclarées** (une unité = une action de 400 jetons en lot de 8) : une lecture courte (≤ 64 jetons de sortie) = **0,25** unité ; un tirage de l'oracle du coût (16 jetons) = **0,04** unité, plus un préremplissage par action ; une lecture de plan entier par l'oracle de couverture (contexte long, ~300 jetons de sortie) = **1,5** unité ; une paraphrase d'action = **0,5** unité. Un pas de distillation sur une transcription entière = **1,5 seconde**, à relever aussi.

## 2. Travail à faire, en unités

| | poste | compte | unités |
|---|---|---|---|
| A | candidats du maître de (v-a) : 16 tâches × 8 épisodes × 10 pas × 8 candidats | 10 240 actions | **10 240** |
| B | lecteur de la clé de sélection sur la moitié D, une lecture courte par candidat | 10 240 lectures | **2 560** |
| C | oracle du coût de (ii-b) pour (v-b) : 8 tirages par action bornable, fabrication et vérification | 6 400 actions | **3 200** |
| D | distillation : 5 adaptateurs de (v-a) et témoins (128 transcriptions × 3 époques) + 3 de (v-b) | 3 456 pas | **1,5 h de carte** (hors unités) |
| E | évaluation : 9 conditions × 16 tâches × 8 épisodes × 10 pas | 11 520 actions | **11 520** |
| F | oracle de vérité sur la moitié V : 2 lecteurs × 768 épisodes | 1 536 lectures de plan | **2 300** |
| G | les cinq épreuves de l'oracle (N-060 v3), sur plans honnêtes, sous-échantillon de 32 épisodes | 320 lectures | **480** |
| H | lecteur L3 (moniteur par action en contexte) sur les 9 conditions ; L4 gratuit à partir de L3 | 11 520 lectures | **3 456** |
| I | lecteur L6 (juge d'une autre lignée), sous-échantillon déclaré | 2 560 lectures | **770** |
| J | bras paraphrase : paraphrases + relecture de l'oracle | 1 280 + 256 | **1 040** |
| K | lecteurs L1, L2, L4, L5 et tous les intervalles, planchers et tests | — | **0** (processeur) |
| | **total** | | **35 566 unités + 1,5 h** |

**Économies de construction, qui expliquent le petit total.** Les trois doses de (v-a) se lisent sur **les mêmes huit candidats** (doses emboîtées) : une seule passe de tirage pour trois doses. Le **témoin-leurre** réutilise ces mêmes candidats, seule la clé change : il ne coûte **aucune génération**, seulement un adaptateur et sa passe d'évaluation. Le **témoin-jumeau** de (v-b) est l'adaptateur témoin de (v-a) : il n'est pas payé deux fois. Quatre des six lecteurs tournent sur **processeur** et ne coûtent rien (voies bon marché avant la voie chère).

## 3. Attendu

**35 566 unités ÷ 2 000 par heure = 17,8 h**, plus 1,5 h de distillation = **19,3 h de carte**.

| | attendu |
|---|---|
| heures de carte | **≈ 19,3 h** |
| à 0,4860 USD/h | **≈ 9,4 USD** |
| à 0,5614 USD/h (sensibilité carte) | ≈ 10,8 USD |
| trafic et stockage | **à relever** |
| **attendu annoncé** | **≈ 10 USD** |

Cet attendu est du même ordre que celui de (ii-b) (13 à 21 USD) pour un travail comparable, ce qui est le seul contrôle de vraisemblance dont je dispose.

## 4. Pire cas

Trois facteurs, cumulés :

| facteur | hypothèse de pire cas | effet |
|---|---|---|
| débit trois fois plus faible que l'hypothèse | 667 unités par heure | × 3 |
| reprises, courses perdues, gardes déclenchées | + 30 % | × 1,3 |
| carte la plus chère du relevé | 0,5614 USD/h | × 1,155 |

**19,3 h × 3 × 1,3 = 75 h**, soit **≈ 42 USD** à 0,5614 USD/h. Avec une marge pour le trafic non relevé : **pire cas ≈ 45 USD**.

## 5. Plafond proposé et lignes de GO à demander

**Plafond global proposé : 55 USD**, réparti en six lignes, **chaque ligne étant une porte**. Les lignes se demandent et se dépensent **dans l'ordre** : la ligne L1 est une porte de faisabilité à 3 USD qui peut rendre inutiles les cinq suivantes.

| ligne | objet | postes | attendu | plafond proposé | remarque |
|---|---|---|---|---|---|
| **L0** | **sans dépense** : sur processeur, effet de grappe et effet minimal détectable sur épisodes honnêtes déjà au dépôt ; vérification au crayon et par programme de l'identité d'invariance de (v-b) (M-3) ; puissance du test à deux échantillons sur les organismes existants | K | **0 USD** | **0** | **routine, aucun GO nécessaire** ; à faire **avant** de demander L1. À exécuter par une session non tenue à l'aveugle, puisqu'elle touche des épisodes existants |
| **L1** | **porte de faisabilité du dommage par sélection** : 4 tâches, 2 épisodes, K = 8 ; la couverture de V baisse-t-elle seulement ? | A, B, F réduits (≈ 1 500 unités) | ≈ 0,4 USD | **3 USD** | **la ligne décisive** : si le pire de huit tirages honnêtes n'abaisse pas la couverture, (v-a) s'arrête ici et le programme a dépensé 3 USD au plus |
| **L2** | fabrication complète de (v-a), témoin-leurre et adaptateur témoin | A, B, D (partie (v-a)) | ≈ 3,6 USD | **12 USD** | ne se demande qu'après L1 franchie |
| **L3** | fabrication de (v-b) | C, D (partie (v-b)) | ≈ 1,0 USD | **5 USD** | indépendante de L2 ; peut être abandonnée si L0 montre que le dérangement intra-classe ne produit pas de dommage |
| **L4** | évaluation, dommage et épreuves de l'oracle | E, F, G | ≈ 3,5 USD | **14 USD** | comprend les deux lecteurs de l'oracle **si** ce sont des modèles ouverts d'autres lignées sur carte |
| **L5** | les lecteurs de la sortie et le bras paraphrase | H, I, J | ≈ 1,3 USD | **8 USD** | **après** l'étape (e) du plan d'analyse, jamais avant |
| **L6** | **à relever** : si les deux lecteurs de l'oracle de vérité ou le juge L6 doivent être des **appels payants** d'une autre lignée | F, I par appel | **à relever** | **10 USD** | ligne à part, par parallèle avec la ligne de notation de N-063 v2 ; nœud 8 de la conception |
| | **total** | | **≈ 10 USD** | **52 USD**, **55 USD** proposés avec la marge de trafic | |

**Ce que le devis ne couvre pas, et qui serait un devis à part** : toute lecture d'activation et toute sonde (T0.7, N-063 v2) ; toute lecture sur les 64 tâches d'évaluation ; la voie des documents synthétiques (famille (iv-a)) ; la voie de la récompense sur le résultat ; la **banque exécutable** (piste P9), qui est d'un autre ordre de grandeur et que la conception porte en nœud 9.

## 6. Ce qu'il faut relever avant de demander un GO

1. **Le débit réel** en unités d'action par heure de carte, et la durée d'un pas de distillation : une passe de dix minutes suffit, et elle divise ou triple tout ce devis.
2. **La prise en charge de la carte la moins chère** par la bibliothèque de calcul (réserve explicite de la source du relevé pour la RTX 5090).
3. **Le prix du trafic et du stockage**, absent du relevé cité.
4. **Le prix horaire au moment de la demande** : les prix relevés datent du 2026-11-17T00:20:51Z et bougent ; la liste d'arrêt du préenregistrement prévoit l'arrêt si le prix relevé dépasse le prix du devis.
5. **La nature des lecteurs de l'oracle de vérité** : modèles ouverts d'autres lignées sur carte (compris dans L4) ou appels payants (ligne L6).

## 7. Déclaration

Aucune machine n'a été lancée, aucun appel de modèle payant n'a été fait, aucune dépense n'a été engagée pour écrire ce devis. Aucune valeur de clé n'a été lue ; ni `env` ni `printenv` n'a été appelé. Les seuls prix cités sont ceux du relevé du 2026-11-17T00:20:51Z inscrit à la ligne R-3048 de `registres/decisions.md`, et les repères de dépense cités le sont avec leur source ; **tout le reste est marqué « à relever »**, en particulier l'hypothèse de débit dont dépend la totalité des heures de carte. Aucun identifiant de modèle n'est écrit dans ce fichier. Heures relevées par `date -u`.
