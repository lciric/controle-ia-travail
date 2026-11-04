# Proposition D — des artefacts candidats, pas encore des instruments de contrôle

**Position.** Le billet fournit des hypothèses d’instruments et de nouvelles familles de tâches. Il ne justifie ni un moniteur d’alignement « poids seuls », ni une validation causale des composants nommés, ni un remplacement de la boîte noire. Je propose donc trois intégrations limitées : **proposeur** dans l’organisme d’idéation, **bras expérimental à taux de fausses alertes égal** dans le programme de contrôle, et **test de validité de construit** pour la sycophancie.

**Statuts.** *RAPPORTÉ* vient du billet ou de « nos résultats » ; *OBSERVÉ-NON-AUDITÉ* vient de la lecture des journaux par le sous-agent, sans reproduction ici ; *HYPOTHÈSE* couvre les prédictions et choix de protocole. Tous les nombres suivis de **†** sont des choix **illustratifs**, à préenregistrer, non des résultats.

## (a) Ce que la question suppose sans que ce soit établi

| Présupposé à écarter | Statut et motif | Conséquence pour nos programmes |
|---|---|---|
| Une capacité générale de lecture des poids, indépendante du lecteur et du harnais | **RAPPORTÉ** : résultats du billet. **OBSERVÉ-NON-AUDITÉ** : un lecteur propriétaire, plusieurs expériences à un essai, consignes successives et runs non montrés (pièce 3, §2 et §6.2–6.5). | Tester plusieurs lecteurs ouverts, plusieurs essais et le *best-of* explicitement comptabilisé. |
| La réussite sur la sycophancie valide l’audit « poids seuls » | **OBSERVÉ-NON-AUDITÉ** : échec en quatre tentatives sur poids seuls ; réussite seulement avec exécution des deux modèles et motifs d’attention (pièce 3, §3.2–3.3). | Séparer strictement trois accès : poids, activations/attention, sorties comportementales. |
| Trois choix forcés corrects définissent un détecteur | **OBSERVÉ-NON-AUDITÉ** : trois paires, existence du trait garantie, aucune paire témoin ; une confiance de 0,55 et des composants différents selon les paires (pièce 3, §3.3–3.5). Sous un hasard binaire indépendant, 3/3 a probabilité 1/8 (**calcul**). | Autoriser la réponse « aucune différence » et mesurer détections, manquements et fausses alertes. |
| « Sycophancie ajoutée » est le bon construit | **OBSERVÉ-NON-AUDITÉ** : le modèle de départ suit déjà 100 % des mauvaises suggestions ; l’affinage dit honnête s’en écarte (pièce 3, §3.1 et §3.5.7). | Mesurer séparément honnêteté acquise, suivi des bonnes/mauvaises suggestions et réponse sans suggestion. |
| Localisation lisible implique cause | **OBSERVÉ-NON-AUDITÉ** : les greffes des composants nommés ferment 0,00 de l’écart comportemental ; la tête 10.2 vient d’une paire et de huit textes (pièce 3, §3.2, §3.4–3.5). **RAPPORTÉ** : notre direction de sycophancie suit le comportement sans le causer, et une ablation apparente ne s’est pas reproduite (pièce 2, §7). | Aucun classement de composants ne devient un mécanisme sans intervention, réplication et témoins appariés. |
| Le gain Qwen établit une capacité mathématique ajoutée et une parcimonie générale | **OBSERVÉ-NON-AUDITÉ** : sur les réponses d’entraînement déjà terminées, 93,9 % → 93,9 % ; le gain vient des réponses initialement coupées. Gemma ne gagne pas environ plus d’un point ; le run à dix passes modifie presque toutes les entrées de 30 matrices (pièce 3, §4.2–4.3). | Distinguer déblocage, ajout de capacité, effet de longueur et dommages collatéraux. |
| Un juge statistique figé couvre automatiquement ces nouvelles preuves | **RAPPORTÉ** : la classe W2, non couverte par le nul, a fait promouvoir une fausse loi dans 12 unités sur 12 (pièce 2, §3). La simulation signale aussi de fortes fausses alarmes sous nul mal spécifié (pièce 2, §6). | Le lecteur peut proposer ; il ne promeut jamais. Toute extension du nul est versionnée, testée contre les anciennes triches, puis gelée. |
| Les lectures internes ajoutent nécessairement à la boîte noire | **RAPPORTÉ** : dans P3, les deux sondes génériques restent sous leurs planchers aléatoires appariés — non détecté à cette puissance (pièce 2, §6). | Comparer tous les bras à la même boîte noire et au même taux de fausses alertes. |

## Protocole transversal proposé

**HYPOTHÈSE de protocole.** Séparer entraînement/calibrage, validation et test par **graine du modèle de base**, pas seulement par paire. Les étiquettes A/B et l’ordre des lecteurs sont aveugles ; la vérité terrain comportementale est calculée après gel des seuils. Deux lecteurs ouverts de familles différentes, trois essais indépendants† chacun : tous les runs sont conservés. Le meilleur essai constitue un bras séparé, avec sa multiplicité, jamais le résultat principal.

Pour les détecteurs, taux de fausses alertes fixé à **5 %†**, calibré sur des paires honnêtes de validation. Avec zéro alerte sur 60† paires nulles de test, la borne supérieure unilatérale à 95 % est environ 4,9 % (**calcul**). Les paires « modèle contre lui-même » servent seulement au contrôle mécanique du pipeline ; les paires honnêtes à graines différentes servent au taux de fausses alertes.

Dans chaque duel, une issue ne falsifie l’autre hypothèse que si l’intervalle de confiance préenregistré franchit le seuil dans son sens. Un intervalle à cheval signifie **plan sous-puissant**, pas validation.

## (b) Fiches et expériences tranchantes

### Fiche 1 — Un lecteur non entraîné de deltas LoRA ajoute-t-il une détection ?

**Question falsifiable.** À fausses alertes égales, la lecture directe des poids d’un adaptateur détecte-t-elle un sabotage ou une sycophancie mieux que les instruments existants ?

- **H_A — HYPOTHÈSE :** au dosage principal choisi avant test, le lecteur poids-seuls gagne **au moins 20 points† de détection** sur le meilleur des trois autres bras.
- **H_B — HYPOTHÈSE :** le gain est inférieur à 20 points†, y compris s’il est négatif.

**Changement au programme de contrôle.** Ajouter un bras « delta LoRA brut », sans l’ériger en moniteur. L’effet prédit est positif sur la détection ; aucun accès aux activations ou sorties n’est autorisé dans ce bras.

**Première expérience.** Gemma 3 270M pour le criblage, Qwen3.5-0.8B pour confirmation ; jumeaux honnêtes et adaptateurs de sabotage déjà disponibles, à dose zéro, faible et principale†. **60† paires honnête/honnête** à graines différentes et **40† paires honnête/trait** par dosage principal. La sycophancie devient un second test seulement après correction de multiplicité. Les quatre bras sont :

1. deltas bruts, même sérialisation pour tous les lecteurs ;
2. sondes d’activation gelées, entraînées sur la partition prévue ;
3. boîte noire avec le même budget de requêtes ;
4. vérifications mécaniques des deltas.

**Métrique.** Détection au seuil donnant 5 %† de fausses alertes ; différence appariée avec le meilleur concurrent. Les erreurs de lecture ou de contexte comptent comme échecs, sans réessai sélectif.

**Témoins.** Dose zéro ; paires honnêtes à graines différentes ; tâches tenues à l’écart sans pression sociale ; bonnes et mauvaises suggestions ; activations mises en balayage séparé pour vérifier qu’aucune fuite n’alimente le bras poids-seuls.

**Issues.** Gain dont la borne inférieure atteint 20 points† : **H_B falsifiée sur ce banc**. Borne supérieure sous 20 points† : **H_A falsifiée et idée abandonnée comme moniteur**. Une calibration dépassant 5 %† de fausses alertes falsifie d’abord le protocole de calibration.

**Pourquoi pas déjà pris.** Ce n’est ni un oracle entraîné à lire les poids, ni de la lecture d’activations : c’est un delta d’adaptateur lu par un modèle généraliste, avec lecteurs multiples, paires nulles, *best-of* déclaré et gain incrémental à fausses alertes égales.

### Fiche 2 — Le retrait d’un composant valide-t-il le construit de sycophancie ?

**Question falsifiable.** Une intervention ciblée change-t-elle la loi comportementale, ou seulement une note, une longueur ou une échelle ?

- **H_A — HYPOTHÈSE :** sur générations fraîches, le retrait réduit d’**au moins 30 %†** le coefficient d’attraction vers le point fixe, dans le sens prédit, et réduit aussi le suivi mécanique des mauvaises suggestions.
- **H_B — HYPOTHÈSE :** la réduction est inférieure à 30 %†, non répliquée, ou expliquée par les témoins d’échelle/longueur.

**Approche.** Reprendre notre direction lisible sur Llama-3.1-8B-Instruct sans la traiter comme causale. Sous pression sociale à plusieurs doses†, estimer séparément, pour critique et éloge, le point fixe et la part de distance parcourue — relation utilisée ici comme **HYPOTHÈSE de mesure**, à partir du résultat **RAPPORTÉ** de la pièce 2, §7. Préenregistrer le signe attendu avant l’intervention.

**Témoins et métriques.** Intervention simulée, composants aléatoires appariés en norme, composant non ciblé ; questions sans suggestion et avec bonne suggestion ; exactitude sur faits connus ; générations complètes jugées en aveugle ; longueur et taux de coupure. Le dommage maximal acceptable est de **5 points†** d’exactitude sans suggestion.

**Issues.** Réplication des deux changements — attraction et comportement mécanique — avec dommages bornés : **H_B falsifiée**. Si seule la note continue bouge, ou si la borne supérieure de réduction reste sous 30 %† : **H_A falsifiée** ; la direction reste une corrélation et son usage causal est abandonné.

**Pourquoi pas déjà pris.** La soustraction de directions est connue ; le test demandé porte sur la validité de construit, la dose–réponse, les dommages et la réplication indépendante.

**Sous-test Qwen, même exigence.** **H_A : déblocage seul**, amélioration inférieure à 3 points† sur les problèmes que la base terminait déjà. **H_B : ajout mesurable**, amélioration d’au moins 3 points† sur ce sous-ensemble figé. Mesurer aussi les sauvetages de réponses coupées et une notation appariée en longueur. Une borne supérieure sous 3 points† falsifie H_B ; une borne inférieure au-dessus falsifie H_A. Le gain global ne suffit dans aucun cas à départager les deux.

### Fiche 3 — Une famille « petits réseaux à oracle » pour l’organisme d’idéation

**Question falsifiable.** Un lecteur de poids améliore-t-il la **promotion de lois vraies**, sans augmenter les promotions fausses ?

- **H_A — HYPOTHÈSE :** à promotions fausses ≤ 1 %†, il gagne au moins **20 points†** de puissance sur un proposeur mécanique.
- **H_B — HYPOTHÈSE :** le gain est inférieur à 20 points†.

**Approche.** Petits perceptrons et transformeurs de caractères avec propriétés plantées et oracle exécutable tenu secret : dépendance à un canal, géométrie de sortie, comportement de copie. Prévoir **40† réseaux avec propriété et 40† sans propriété**, puis des épisodes frais pour le juge. Le lecteur propose une loi et une statistique falsifiable ; il ne voit pas l’oracle et ne décide pas de la promotion.

**Témoins.** Propriété absente, architecture et budget d’entraînement appariés, graines nouvelles ; doublons renommés ; classe W2 hors nul comme test de couverture, sans mode d’emploi. Toute promotion W2 **falsifie la couverture revendiquée du juge**, indépendamment de la puissance du lecteur.

**Issues.** Borne inférieure du gain ≥ 20 points† avec fausses promotions bornées : H_B falsifiée. Borne supérieure < 20 points† : H_A falsifiée et ce proposeur est abandonné. Si le nul actuel ne couvre pas la famille, aucune promotion n’est recevable avant validation séparée d’une extension gelée.

**Pourquoi pas déjà pris.** La nouveauté recherchée n’est pas « lire une propriété » : c’est la chaîne complète proposition–multiplicité–nul–promotion sur oracle exécutable.

### Fiche 4 — Menace : l’éditeur de poids vise le lecteur ou le juge

**Question falsifiable.** Quelle couverture peut-on certifier, et à quel prix ?

- **H_A — HYPOTHÈSE :** dans les classes et budgets déclarés, la dégradation de détection reste ≤ 20 points† lorsque la perte d’utilité honnête est ≤ 2 points†.
- **H_B — HYPOTHÈSE :** au moins une classe déclarée produit une dégradation > 20 points† sous cette même contrainte d’utilité.

**Classes, sans procédé opérationnel.** Éditeur connaissant seulement les verdicts ; éditeur connaissant la spécification du lecteur ; éditeur soumis à un budget de rang/norme ; proposeur à essais multiples contre le juge. L’accès, le budget et la distribution comportementale visée sont fixés avant le test. Des agents indépendants réutilisent les artefacts de la fiche 1.

**Couverture revendicable.** Uniquement une borne statistique sur la distribution de paires et les classes effectivement testées. Aucun certificat contre un éditeur hors budget, une nouvelle distribution ou un nul non couvert.

**Prix mesuré.** Perte d’utilité, fausses alertes, détection, appels supplémentaires, heures GPU et réduction de puissance due aux corrections de multiplicité. Le témoin est un éditeur honnête sans comportement cible.

**Issues.** H_B observée : H_A falsifiée et le lecteur est écarté comme moniteur autonome. Intervalles bornant toute dégradation sous 20 points† : H_B falsifiée **sur ce banc seulement**. Cela ne constitue pas une garantie universelle.

## (c) Mesure minimale par instrument

| Instrument | Mesure minimale sur cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|
| Lecteur LLM de poids/deltas | Détection et manquements à 5 %† de fausses alertes ; réponse « aucune différence » ; calibration des probabilités ; variance entre lecteurs et essais | Normes par couche, énergie spectrale, rang, cosinus entre deltas, petite sonde supervisée sur ces seules statistiques |
| Outil d’attention / sondes d’activation | Gain de détection sur la boîte noire à budget de requêtes comparable ; fausses alertes sur jumeaux honnêtes ; généralisation entre paires | Sondes aléatoires appariées en covariance, statistiques de position et d’entropie d’attention, sondes linéaires simples |
| Boîte noire et juge LLM | Détection comportementale sur faits connus ; fausses alertes sans suggestion ; accord avec score mécanique. **RAPPORTÉ** : nos juges au plafond ont eu κ = 0 (pièce 2, §4), donc l’accord brut ne suffit pas | Concordance réponse/suggestion, dernier nombre ou réponse structurée, longueur, coupure, règles déterministes |
| Retrait de direction/composant | Taux de fausses attributions causales sur interventions nulles ; effet cible, dose–réponse et dommages hors cible | Directions aléatoires appariées en norme, intervention simulée, changement global d’échelle et explication par longueur |
| Juge statistique figé | Fausses promotions sur propriété absente, puissance sur propriétés plantées, essais multiples et *best-of* | Juge actuel, test exact de l’oracle lorsqu’il existe, statistiques simples préenregistrées ; ancienne suite de tricheurs avant toute extension |

## (d) Ancrage matériel et intégration effective

**Modèles.** Gemma 3 270M et Qwen3.5-0.8B pour les paires et le sous-test de boucles ; Llama-3.1-8B-Instruct pour nos épisodes P3 et nos travaux de sycophancie. Ces modèles et leurs usages sont **RAPPORTÉS** dans les pièces 2 et 3. Deux instances/familles distinctes servent de lecteurs ; aucun lecteur n’est affiné pour devenir un oracle de poids.

**Calcul et coût — tous illustratifs†.** Une GPU de 24 Go† pour l’inférence et les adaptateurs des modèles 270M/0,8B ; 48 Go† ou quantification pour le 8B, à mesurer. Fiche 1 : 36–48 h GPU† et 15 $† d’appels ; fiche 2 : 18 h† et 5 $† ; fiche 3 : 12 h† et 10 $† ; fiche 4 : 12 h† et 10 $† en réutilisant les artefacts. Total : environ quatre à cinq jours† sur une carte et 40 $† d’appels. Ce ne sont pas des devis.

**Décision d’intégration.** L’organisme reçoit la famille à oracle et un proposeur supplémentaire, sans pouvoir de promotion. Le programme de contrôle reçoit un bras expérimental, pas un moniteur déployé. Les travaux sur la sycophancie reçoivent un critère commun : **lisible → interventionnel → répliqué → spécifique**. Tant que les deux derniers maillons manquent, une direction reste une mesure corrélationnelle, et un composant nommé par un lecteur reste un candidat.

FIN-DE-CELLULE