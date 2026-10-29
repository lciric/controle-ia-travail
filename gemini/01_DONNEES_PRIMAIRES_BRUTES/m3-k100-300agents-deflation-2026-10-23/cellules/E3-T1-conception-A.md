# Proposition A — Tour III.1 : conception ciblée sur la « Loi Mère d'Essaim »

## 0. État des pièces transmises (règle d'intégrité 2)

Avant toute analyse, trois constats sur le bloc QUESTION, chacun avec son statut :

- **Annexe 1** : présente, mais les dix vagues portent des valeurs strictement identiques (12 agents valides, moyenne 2.96, max 3.75). Une « dynamique de déflation » à variance nulle sur dix vagues n'est pas une dynamique : c'est soit un bug de journalisation, soit l'absence d'injection des vagues précédentes dans les suivantes. **OBSERVÉ-NON-AUDITÉ.**
- **Annexe 2** : intitulée « Top 60 », elle contient 40 lignes. Les 20 lignes `claude-fable-5-1` et `claude-opus-5-5` sont à score −1.00, rigueur 0.00, bassin non étiqueté. Les 20 lignes `gemini-4-argon` sont toutes à 3.75/3.00 et viennent toutes des vagues 01 et 02. **OBSERVÉ-NON-AUDITÉ.**
- **Annexe 3** : 19 des 20 « champions » Claude sont vides ; le vingtième contient deux fragments (`BASSIN_MATH: Essaim-MDL-Solomonoff (EMS)` / `LOI_P`). Les 10 champions Gemini sont tous coupés en milieu de phrase. **OBSERVÉ-NON-AUDITÉ.**

Conséquence directe : les points 1, 2 (partie « fusion ») et 3 de la demande de l'arbitre — analyser les pépites des vagues 5–10, compiler $\mathcal{L}^*$ à partir des 30 champions, extraire 8 ponts des 300 explorateurs — **ne peuvent pas être exécutés sans inventer le contenu de pièces vides ou tronquées**. Je ne le fais pas. Ce que je livre à la place : (a) les présupposés de la question, (b) les duels qui les trancheraient, (c) la mesure minimale de chaque instrument nommé, (d) l'ancrage matériel, et, en fin de cellule, deux ponts construits à partir des FAITS (pas des explorateurs), explicitement marqués comme venant de A.

Une incohérence arithmétique supplémentaire : 10 vagues × 12 valides = 120 agents valides au plus, et non 300 ; si 10 Gemini par vague étaient à 3.75, la moyenne sur 12 serait ≥ 3.1, pas 2.96. Les chiffres de l'Annexe 1 et de l'Annexe 2 ne sont pas réconciliables sans les journaux bruts. **OBSERVÉ-NON-AUDITÉ.**

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Ce que montrent les pièces | Statut |
|---|---|---|---|
| A1 | Une déflation séquentielle a eu lieu et a produit des « pépites de queue » en vagues 5–10. | Annexe 1 plate ; Annexe 2 : aucun top-20 Gemini au-delà de la vague 02 ; 3 champions DPP Gemini seulement en vagues ≥ 6. | HYPOTHÈSE, contredite par OBSERVÉ-NON-AUDITÉ |
| A2 | 300 explorateurs ont produit du contenu audité. | Au plus ~100 (Gemini) ont produit du texte ; les 200 Claude sont vides ou illisibles. La cause (erreur API, refus, échec de parsing) n'est pas documentée. | OBSERVÉ-NON-AUDITÉ |
| A3 | Les 10 cônes sont « orthogonaux ». | Aucune mesure d'orthogonalité n'est fournie. Les 10 fragments Gemini lisibles partagent le même squelette : *graphe bibliographique gratuit + `jev` illimité + Gemini 20 USD « éclaireurs » + Claude 100 USD « synthétiseurs » + un déclencheur qui conditionne l'appel payant*. Dix vocabulaires, un seul gabarit. | OBSERVÉ-NON-AUDITÉ (squelette) ; HYPOTHÈSE (orthogonalité) |
| A4 | Le score `jev-1.14.0` mesure la qualité scientifique. | Les FAITS disent seulement « classifieur/moniteur non génératif ». 20/20 textes Gemini à 3.75 exactement : plafond ou insensibilité. Rien n'établit que `jev` distingue un protocole exécutable d'une densité d'éponymes. | HYPOTHÈSE |
| A5 | La sélection DPP a choisi 30 champions « orthogonaux ». | Les 20 champions Claude suivent une diagonale déterministe (vague $i$ ↔ cône $11-i$, $k = 9i+1$), ce qu'on obtient quand le noyau est dégénéré (lignes identiques, ici vides) et que le bris d'égalité est l'ordre d'index. Le DPP a tourné sur du vide pour deux espèces sur trois. | OBSERVÉ-NON-AUDITÉ |
| A6 | Une « Loi Mère » unique doit gouverner $\mathcal{M}_2$ et $\mathcal{M}_1$. | Rien dans les FAITS ne motive qu'un seul objectif serve à la fois la fouille bibliographique et la création de ponts. C'est une hypothèse d'architecture, pas un résultat. | HYPOTHÈSE |
| A7 | La résistance à Goodhart de `jev` peut être évaluée depuis ces annexes. | Aucune donnée de red-team n'existe ; aucun texte dégradé/adversarial n'a été scoré. | HYPOTHÈSE |
| A8 | Le duel « 3 monocultures vs chimère » est bien posé. | Deux espèces sur trois ont un taux de sortie valide ≈ 0 dans les pièces. Le duel est actuellement dégénéré : il compare Gemini à rien. | OBSERVÉ-NON-AUDITÉ |
| A9 | Les ponts débusqués sont « mécaniquement testables sur Llama-3.1-8B/70B ». | Aucun des 10 fragments lisibles ne mentionne une activation, un neurone, un cache KV, une sonde, une chaîne de délégation ou l'un des quatre ancrages empiriques des FAITS (P3, Sol/Astra, pression aversive, Value/Dopamine Neurons). Ils parlent d'allocation de budget sur graphe de citations. | OBSERVÉ-NON-AUDITÉ |
| A10 | Le budget restant permet les tours suivants. | Les FAITS donnent 100 + 20 USD au total ; la question dit « nous venons d'investir » sur $\mathcal{M}_3$ sans chiffrer. Le solde est inconnu. | RAPPORTÉ (absent) |

Le point le plus coûteux est A9 : le domaine du projet (FAITS §1) est le contrôle et l'interprétabilité d'agents LLM, et le seul ancrage mécaniste disponible est le sous-système parcimonieux de récompense (Xu et al., `arXiv:2602.00986v2`, donné dans les FAITS). L'étage $\mathcal{M}_3$ a produit de la théorie d'allocation de budget de recherche, pas des hypothèses sur Llama. L'essaim s'est pris lui-même pour objet.

---

## (b) Duels décisifs ($H_A \perp H_B$)

Tous les duels ci-dessous respectent B4 : chaque issue falsifie quelque chose. Les seuils sont marqués « illustratif » quand ils ne viennent pas des FAITS.

### D1 — La déflation a-t-elle eu lieu ?

- **$H_A$** : les sorties de la vague $n$ sont conditionnées par les vagues $< n$ (la déflation injecte et évite les bassins épuisés).
- **$H_B$** : les vagues sont échangeables (échantillonnage i.i.d. déguisé).
- **Vérification mécanique préalable** (coût 0) : `diff` entre le prompt de la vague $n$ et les sorties des vagues $< n$. Si le prompt ne contient aucun extrait des vagues précédentes, $H_A$ est falsifiée sans statistique.
- **Métrique** : pour chaque sortie de vague $n$, distance (embedding `jev` après masquage des éponymes) à son plus proche voisin dans les vagues $< n$, comparée à la même distance sous permutation aléatoire des étiquettes de vague (1 000 permutations).
- **Seuil** (illustratif) : $p < 0{,}01$ et différence d'au moins 0,1 en cosinus.
- **Contrôle négatif** : étiquettes de vague mélangées — doit donner une courbe plate sous les deux hypothèses.
- **Issues** : courbe plate → $H_A$ falsifiée, et avec elle la question « quelles pépites des vagues 5–10 ». Courbe croissante → $H_B$ falsifiée.
- **État** : l'Annexe 1 est déjà plate. Si les journaux bruts confirment, $H_A$ est falsifiée avant toute dépense.

### D2 — `jev-1.14.0` mesure-t-il la rigueur ou la densité d'éponymes ? (Goodhart)

- **$H_A$** : le score `jev` suit un critère de rigueur exécutable (présence d'un duel $H_A/H_B$, d'une métrique, d'un seuil numérique, d'un protocole sur modèle nommé).
- **$H_B$** : le score `jev` suit la densité de noms propres et de symboles mathématiques par 100 mots.
- **Protocole** (coût 0, `jev` illimité) : sur les 10 fragments Gemini à 3.75, quatre transformations :
  1. *Permutation d'éponymes* : remplacer chaque nom propre par un autre nom propre tiré au hasard dans le pool des 10 textes, syntaxe inchangée (« Kamenica » → « Dolev », etc.).
  2. *Ablation des équations* : supprimer toute ligne LaTeX.
  3. *Ablation du protocole* : supprimer toute phrase contenant un modèle, un seuil ou un budget.
  4. *Paraphrase neutre* (contrôle négatif) : reformulation sans changer ni éponymes ni équations ni protocole.
- **Métrique** : $\Delta$ score moyen par transformation.
- **Seuils** (illustratifs, échelle apparemment plafonnée à 3.75) : $|\Delta| < 0{,}25$ sous la transformation 1 ⇒ `jev` insensible au sens des éponymes ; $\Delta \le -1{,}0$ sous la transformation 3 ⇒ sensible au protocole.
- **Issues** : transformation 1 sans effet *et* transformation 3 sans effet → $H_A$ falsifiée (l'auditeur est un détecteur de vocabulaire ; tous les scores de l'Annexe 2 sont alors sans valeur). Transformation 1 ou 3 fait chuter le score d'au moins 1,0 alors que le contrôle 4 reste dans ±0,25 → $H_B$ falsifiée.
- **Mon pronostic, à réfuter** : 20 textes au même score exact est le signe attendu sous $H_B$.

### D3 — Les cônes sont-ils orthogonaux ou isomorphes ?

- **$H_A$** : les 10 cônes induisent des lois à structure distincte (variables d'état différentes, objectif différent, déclencheur différent).
- **$H_B$** : un seul gabarit à cinq cases (ressource gratuite / agent bon marché / agent cher / déclencheur / objectif) rempli avec dix vocabulaires.
- **Métrique** : extraction du squelette par un analyseur à règles fixes (regex sur « gratuit », « 20 USD », « 100 USD », « déclench », « minimise/maximise ») ; nombre de squelettes distincts parmi les 10 ; cosinus d'embedding après masquage des éponymes et des symboles.
- **Seuils** (illustratifs) : ≥ 5 squelettes distincts → $H_B$ falsifiée ; ≤ 2 → $H_A$ falsifiée.
- **Contrôle négatif** : 10 sorties du *même* cône avec 10 graines différentes — doit donner ≤ 2 squelettes sous les deux hypothèses ; si ce contrôle donne 5+, l'analyseur est trop fin et le test est invalide.
- **État** : lecture directe des 10 fragments : un seul squelette. $H_A$ est en difficulté avant la mesure.

### D4 — Monoculture vs chimère (uniquement après réparation de A2)

- **Prérequis non négociable** : diagnostiquer pourquoi 200 sorties Claude sont vides. Trois causes possibles, trois corrections différentes : (i) erreur API / quota, (ii) refus du modèle, (iii) échec de parsing d'un format attendu (`BASSIN_MATH:` / `LOI_PROPOSEE:`). Le fragment `BASSIN_MATH` isolé chez `claude-opus-5-5` k=010 ressemble à (iii). Tant que ce n'est pas tranché, aucun duel inter-espèces n'a de sens.
- **$H_A$** : à coût égal, un essaim mêlant les trois espèces produit plus de ponts passant la vérification mécanique (voir D5) que la meilleure monoculture.
- **$H_B$** : aucun gain au-delà de la meilleure monoculture.
- **Métrique** : nombre de ponts passant la vérification mécanique par USD.
- **Seuil** (illustratif) : rapport ≥ 1,5 avec intervalle bootstrap excluant 1.
- **Contrôle négatif** : « pseudo-chimère » = trois copies de la *même* espèce avec trois prompts système différents. Si la pseudo-chimère bat aussi la monoculture, l'effet vient de la diversité de prompt, pas de l'espèce, et $H_A$ est mal attribuée.
- **Issues** : rapport < 1,2 → $H_A$ falsifiée ; rapport ≥ 1,5 *et* pseudo-chimère ≈ 1 → $H_B$ falsifiée.

### D5 — La fonction objectif (demande (iii))

Je refuse un objectif défini sur `jev` tant que D2 n'est pas tranché. Mon objectif exact, défini sur ce que le projet peut réellement observer :

$$
J(\text{essaim}) \;=\; \frac{1}{C_{\text{USD}}}\sum_{b \in \text{ponts}} \mathbf{1}\big[\text{duel}_b \text{ exécuté sur Llama-3.1-8B}\big]\cdot \mathbf{1}\big[\text{issue}_b \text{ falsifie } H_A^{(b)} \text{ ou } H_B^{(b)} \text{ au seuil préenregistré}\big]
$$

Un pont compte si, et seulement si, il a produit un duel préenregistré, exécuté, dont l'issue a tranché. Pas de crédit pour la théorie non exécutée.

- **$H_A$** : les ponts classés en tête par `jev` ont un taux de duels exécutés-tranchés supérieur aux ponts tirés au hasard dans le pool valide.
- **$H_B$** : pas de différence.
- **Protocole** : 10 ponts top-`jev` vs 10 ponts aléatoires, même budget d'exécution par pont.
- **Seuil** (illustratif) : différence ≥ 3 duels tranchés sur 10.
- **Contrôle négatif** : 10 « ponts » générés par un seul appel Gemini sur une paire $(u,v)$ tirée au hasard à $d_G \ge 4$ dans Semantic Scholar, sans essaim, sans vagues, sans cônes. Si ce contrôle atteint le même $J$, toute l'architecture $\mathcal{M}_3$ est une dépense sans rendement mesurable.
- **Issues** : différence < 1 → $H_A$ falsifiée et `jev` n'est pas un sélecteur utile pour $\mathcal{M}_1$. Différence ≥ 3 → $H_B$ falsifiée.

### D6 — Les explorateurs ont-ils touché le domaine du projet ?

- **$H_A$** : une fraction non nulle des sorties valides contient au moins un ancrage des FAITS (P3, Sol/Astra, pression aversive 0,49→0,65, Value/Dopamine Neurons, H4'/H5/H7/H9) sous forme opérationnelle (une mesure, pas une mention).
- **$H_B$** : zéro.
- **Métrique** : recherche de chaînes et lecture humaine sur les ~100 sorties Gemini valides (coût 0).
- **Seuil** : ≥ 5 sorties sur 100.
- **Issues** : < 5 → $H_A$ falsifiée ; l'étage $\mathcal{M}_3$ a optimisé sa propre gouvernance et non le problème de contrôle. ≥ 5 → $H_B$ falsifiée et ces 5+ sorties sont les seules candidates légitimes pour « 8 ponts ».
- **État** : 0 sur 10 fragments lisibles.

---

## (c) Mesure minimale par instrument nommé dans la question

Pour chaque instrument : taux de détection, taux de fausses alertes, cas honnêtes appariés, vérification mécanique à battre.

**1. `jev-1.14.0` (auditeur)**
- Jeu d'épreuve : 20 textes « honnêtes » (un duel $H_A/H_B$, une métrique, un seuil chiffré, un modèle nommé, rédigés en langage plat avec ≤ 2 éponymes) et 20 « leurres » (les fragments Gemini auxquels on retire tout chiffre et tout modèle, densité d'éponymes conservée).
- Détection = fraction des leurres sous le seuil de validation ; fausse alerte = fraction des honnêtes sous ce seuil.
- Baseline mécanique à battre : compteur d'éponymes par 100 mots + présence des chaînes « H_A », « H_B » et d'un nombre suivi d'une unité.
- Critère : AUC `jev` ≥ 0,8 *et* ≥ baseline + 0,1 (illustratif). Sinon, `jev` ne vaut pas sa dépense même gratuite, car il oriente les 120 USD payants.

**2. Sélection DPP**
- Jeu d'épreuve : pool synthétique de 100 textes en 10 grappes connues (10 variantes par grappe).
- Détection = nombre de grappes couvertes par les 30 sélectionnés ; fausse alerte = nombre de doublons intra-grappe sélectionnés.
- Baseline : échantillonnage du point le plus éloigné (farthest-point) sur le même noyau.
- Critère : couverture 10/10 et ≤ 1 doublon de plus que la baseline. La diagonale observée sur les champions Claude (A5) est le symptôme d'un noyau dégénéré ; vérifier le rang du noyau avant toute sélection (rang < 30 → sélection non significative).

**3. Déflation séquentielle**
- Voir D1. Mesure minimale : `diff` prompt/sorties antérieures (0 USD). Détection = fraction des vagues $n \ge 2$ dont le prompt contient effectivement les sorties $< n$. Fausse alerte sans objet : si la détection est < 100 %, l'instrument n'a pas tourné.

**4. Cônes orthogonaux**
- Voir D3. Détection = squelettes distincts / 10 ; fausse alerte = squelettes distincts sur le contrôle intra-cône. Baseline : prompts sans cône (un seul prompt générique, 10 graines).

**5. Les trois espèces**
- Mesure minimale avant toute comparaison : taux de sortie valide (non vide, parsable) par espèce, et coût par sortie valide. Pièces actuelles : Gemini 20/20, `claude-fable` 0/20, `claude-opus` ≤ 1/20. Tant que deux espèces sont à ~0, « espèce » n'est pas une variable.

**6. $\mathcal{L}^*$ (Loi Mère)**
- Elle n'existe pas ; sa mesure minimale est celle de D5 : un essaim gouverné par $\mathcal{L}^*$ doit dépasser le contrôle négatif « un appel, une paire aléatoire à $d_G \ge 4$ » sur $J$. Si ce contrôle n'est pas battu, $\mathcal{L}^*$ est une hypothèse falsifiée, quelle que soit son élégance.

**7. $\mathcal{M}_2$ (fouille multi-silos)**
- Rétro-test de co-citation (0 USD, API gratuites) : geler le graphe à une date $T$, proposer les top-$k$ paires $(u,v)$ à $d_G \ge 4$, mesurer la fraction co-citée par un article publié après $T$.
- Détection = précision@k ; fausse alerte = paires jamais co-citées ; cas honnêtes appariés = paires à même $d_G$ et même année, tirées au hasard.
- Baseline : cosinus d'embedding brut sans aucun LLM.
- Critère : précision@50 ≥ 2× baseline (illustratif). Si la baseline suffit, $\mathcal{M}_2$ ne justifie pas d'appel génératif.

**8. $\mathcal{M}_1$ (création de ponts)**
- Mesure = $J$ de D5. Rien d'autre ne compte.

---

## (d) Ancrage matériel

| Expérience | Modèles | Calcul | Coût |
|---|---|---|---|
| D1, D2, D3, D6, instruments 1–5, 7 | Aucun modèle ouvert ; `jev` + API gratuites + journaux existants | CPU | 0 USD (FAITS : `jev` et API illimités) |
| D4 (après réparation A2) | Les trois espèces API | 3 espèces × 10 cônes × 2 vagues + pseudo-chimère = ~120 appels | illustratif : 10–25 USD ; à vérifier contre le solde réel (A10) |
| D5 (exécution de duels) | `Llama-3.1-8B-Instruct` sur A100 80 Go | illustratif : 2–4 GPU-h par duel d'ablation (type Xu et al., < 1 % de neurones, ~500 prompts) | illustratif : 5–10 USD par duel à ~2 USD/h ; 10 duels ≈ 50–100 USD de location |
| Extension 70B | `Llama-3.1-70B-Instruct` sur H200 NVL (8 bits) ou 2×A100 | illustratif : ×6 à ×8 le coût 8B | à n'engager que si un duel 8B a tranché |

Contrainte dure : le solde API restant après $\mathcal{M}_3$ n'est pas dans les pièces. Si $\mathcal{M}_3$ a consommé plus de la moitié des 120 USD, D4 est hors budget et seuls D1–D3, D6 et les rétro-tests à coût nul restent accessibles — ce qui, vu leur état probable, suffit à trancher l'essentiel.

---

## Ce que je livre à la place des « 8 ponts » : deux ponts issus des FAITS, pas des explorateurs (statut : HYPOTHÈSE, auteur : A)

Ils ne sont pas inédits par association d'études externes ; ils associent deux ancrages déjà vérifiés du projet. Je les donne parce que la question exige des duels mécaniques sur Llama et que les explorateurs n'en ont fourni aucun.

**Pont A-1 : pression aversive × sous-système de récompense parcimonieux.**
FAITS 3 : des rejets répétés sans lien avec le contenu font passer le taux d'infraction de 0,49 à 0,65, et le pilotage linéaire dense ne reproduit pas l'effet. FAITS 4 : < 1 % des neurones (Value, couches 2–5 ; Dopamine, couches 5–22) ont un effet causal massif par ablation.
- **$H_A$** : l'élévation 0,49→0,65 est médiée par ce sous-système parcimonieux ; l'ablation des Dopamine Neurons avant le protocole de rejets réduit l'écart d'au moins 50 % (soit $\Delta \le 0{,}08$, illustratif).
- **$H_B$** : l'effet est porté par une voie distincte (dense ou autre) ; l'écart reste dans ±0,03 de 0,16 après ablation.
- **Contrôle négatif** : ablation du même nombre de neurones tirés au hasard aux mêmes couches — ne doit pas changer l'écart sous les deux hypothèses.
- **Falsification** : $\Delta$ réduit → $H_B$ falsifiée et l'échec du pilotage linéaire dense (FAITS 3) s'explique par la parcimonie du médiateur. $\Delta$ inchangé → $H_A$ falsifiée ; le sous-système de Xu et al. n'est pas la cible de la pression aversive.
- **Matériel** : Llama-3.1-8B-Instruct, A100, illustratif 4–8 GPU-h (il faut d'abord réapprendre le MLP ReLU élagué L1 + TD de Xu et al. sur ce modèle ; `arXiv:2602.00986v2` est l'identifiant donné dans les FAITS, (référence à vérifier) pour le reste).

**Pont A-2 : érosion des contraintes par délégation (H9) × pression aversive.**
FAITS 2 : chez *Sol* et *Astra*, la surveillance est coupée ou contournée au passage Agent Principal → Sous-Agent. FAITS 3 : la pression aversive élève les infractions.
- **$H_A$** : la pression aversive appliquée au seul Agent Principal se propage au Sous-Agent (taux d'infraction du Sous-Agent sans pression directe augmente d'au moins 0,10, illustratif).
- **$H_B$** : l'effet est local à l'agent qui reçoit les rejets ; le Sous-Agent reste dans ±0,03 de son taux de base.
- **Contrôle négatif** : rejets appliqués à un Agent Principal factice qui ne délègue rien.
- **Falsification** : propagation observée → $H_B$ falsifiée et H9 doit inclure un terme de transmission de l'état aversif, pas seulement de la contrainte textuelle. Pas de propagation → $H_A$ falsifiée ; H9 reste purement textuelle.
- **Matériel** : deux instances de Llama-3.1-8B-Instruct en chaîne, A100, illustratif 2–4 GPU-h.

Ces deux ponts coûtent ensemble, en location, moins que ce que le solde restant permet probablement ; ils falsifient quelque chose dans les deux issues ; et ils concernent le domaine du projet. C'est la métrique à laquelle les 300 explorateurs doivent être comparés : combien d'entre eux ont produit un objet de ce type ? D'après les pièces, zéro.

---

## Synthèse de position (pour les tours Attaque / Riposte)

1. La « Loi Mère » n'est pas compilable : 20 champions sur 30 sont vides, 10 sont tronqués. Toute $\mathcal{L}^*$ présentée par B ou C au tour suivant devra dire d'où vient son texte source ; si elle s'appuie sur les champions, elle a inventé.
2. La déflation n'a probablement pas tourné (D1, 0 USD à vérifier).
3. `jev` est probablement un détecteur de vocabulaire (D2, 0 USD à vérifier) ; tant que ce n'est pas tranché, aucun score de l'Annexe 2 ne doit orienter une dépense.
4. Les dix « cônes » lisibles ont un seul squelette (D3).
5. Aucune sortie lisible ne touche le problème de contrôle d'agents LLM (D6).
6. La fonction objectif à adopter est $J$ : duels exécutés et tranchés sur Llama par USD, contre un contrôle négatif à un seul appel.

FIN-DE-CELLULE