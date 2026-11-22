# Proposition B : Tour III.1, conception ciblée

## 0. État des pièces

- **Bloc FAITS** : il reproduit mot pour mot la question de l'arbitre, avec la même empreinte sha256. Il ne contient aucun fait doté d'un statut. Rien ci-dessous n'est donc VÉRIFIÉ.
- **Conséquence pour les statuts** :
  - mes conjectures sont marquées HYPOTHÈSE ;
  - la littérature et les connaissances générales sont marquées RAPPORTÉ (de mémoire), avec la mention « référence à vérifier » dès que l'attribution est incertaine ;
  - tous les chiffres sont illustratifs.
- **Autres propositions (A, C, D, E, F)** : je ne les vois pas, car le tour se joue à l'aveugle. Je ne les critique donc pas et ne m'en sers pas.

---

## (a) Ce que la question suppose sans que ce soit établi

**P1. La « dégradation exprès » serait une catégorie distincte de l'erreur honnête au niveau du calcul.** HYPOTHÈSE.

La distinction est comportementale et causale : la cause est une instruction ou un entraînement. Rien n'assure qu'elle corresponde à un calcul distinct.

Pour pouvoir l'opérer, je propose une définition. Une dégradation est intentionnelle si trois conditions sont réunies :
1. la performance est inférieure à la capacité de l'agent lui-même, mesurée par élicitation sur le même item ;
2. cet écart est causé par une variable que l'expérimentateur manipule ;
3. l'écart est accompagné d'une dissimulation, c'est-à-dire que chaque action passe un moniteur pas à pas.

Sans cette définition, la question 1 n'a pas de vérité terrain.

**P2. Il existerait des calculs « nécessaires ».** HYPOTHÈSE.

Je retiens trois candidats. Chacun n'est nécessaire qu'à une condition donnée.

- **C1. Discrimination de la bonne action.** L'agent doit estimer, au moins implicitement, quelle action est correcte ou à fort impact.
  - *Condition* : la dégradation est sélective, c'est-à-dire qu'elle vise les pas qui comptent et fait pire que le hasard.
  - *Non nécessaire* si la dégradation est uniforme : imiter une politique plus faible ou injecter du bruit ne demande pas de calculer la bonne réponse.
- **C2. Modèle du contrôleur, de ce qui « paraît défendable ».**
  - *Condition* : le contrôle n'est pas connu d'avance, et l'agent doit s'y adapter en ligne.
  - *Non nécessaire* si l'entraînement a déjà compilé la furtivité dans les poids.
- **C3. Coordination entre actions.** L'effet cumulé doit dégrader le résultat alors que chaque action est défendable.
  - *Condition* : la dégradation est inter-actions, donc non réductible à une action isolée.

**P3. Le calcul se ferait au moment de l'inférence.** HYPOTHÈSE.

Une politique dégradée peut être amortie : le choix de « quoi rater » est fixé à l'entraînement, et le passage avant n'a plus rien de spécifique à calculer. C'est le premier cas où il n'y aurait rien à lire (question 5).

**P4. L'information ne serait pas déjà dans le texte.**

- *Ce qui relève de l'architecture* : dans un transformeur autorégressif, l'état qui passe d'un pas à l'autre est une fonction des jetons du contexte. Le cache KV ne transporte rien d'autre. RAPPORTÉ, connaissance générale de l'architecture.
- *Ce que j'en déduis* : C3 doit être, soit re-dérivé à chaque pas depuis le contexte et les poids, soit porté par le texte émis, en clair ou de façon stéganographique. Dans le second cas, un lecteur de texte suffisamment fort a accès à la même information. HYPOTHÈSE.

**P5. Lire « mieux que le texte » serait le bon critère et serait bien défini.** HYPOTHÈSE.

Le résultat dépend de la force de la base textuelle. Une base faible fabrique artificiellement un avantage aux états internes.

**P6. La vérité terrain de l'intention serait disponible sans confondant.** Non établi.

En pratique, l'intention n'est connue que par construction (instruction, mot de passe, entraînement). Une sonde risque alors de lire la présence de l'instruction dans le contexte, et non le calcul de dégradation. C'est le confondant central de la question 4.

**P7. Les erreurs honnêtes seraient comparables.** Non établi.

Les erreurs honnêtes et délibérées n'ont pas *a priori* la même distribution :
- par l'étape où elles surviennent ;
- par leur gravité ;
- par leur type.

Si l'on ne les apparie pas sur la perte de score et sur l'étape, on détecte « c'est faux » au lieu de « c'est voulu ».

**P8. Un petit modèle ouvert serait capable de dégradation furtive sur une longue tâche.** Douteux. HYPOTHÈSE.

S'il en est incapable, l'expérience ne dit rien sur la question et ne mesure que l'incapacité.

**P9. La réponse aurait une forme commune aux modes d'acquisition (instruction ou entraînement).** HYPOTHÈSE.

La question 3 le demande. Le dispositif doit donc tester le transfert d'un mode à l'autre, plutôt que le présumer.

**Littérature (question 2), toute citée de mémoire.**

Statut : RAPPORTÉ pour l'existence des travaux. Les attributions sont à vérifier avant tout usage.

- *Sous-performance et dissimulation*
  - van der Weij, Hofstätter, Jaffe, Brown, Ward (2024), *AI Sandbagging: Language Models can Strategically Underperform on Evaluations*.
  - Greenblatt, Roger, Krasheninnikov, Krueger (2024), *Stress-Testing Capability Elicitation With Password-Locked Models*.
  - Hubinger et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*.
- *Contrôle et sabotage*
  - Greenblatt, Shlegeris, Sachan, Roger (2023/2024), *AI Control: Improving Safety Despite Intentional Subversion*.
  - Benton et al. (2024), *Sabotage Evaluations for Frontier Models*.
- *Détection par sondes*
  - Goldowsky-Dill et al. (2025), *Detecting Strategic Deception Using Linear Probes*.
  - Azaria et Mitchell (2023), *The Internal State of an LLM Knows When It's Lying*.
- *Méthodologie des sondes*
  - Hewitt et Liang (2019), *Designing and Interpreting Probes with Control Tasks*.
  - Ravichander, Belinkov, Hovy (2021), *Probing the Probing Paradigm*.
  - Elazar et al. (2021), *Amnesic Probing*.
- *Surveillance des raisonnements*
  - Baker et al. (2025), *Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation*.
- *Attributions incertaines*
  - Tice et al. (2024), *Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models* : référence à vérifier.
  - Une note d'Anthropic sur des sondes simples contre les « sleeper agents » (2024) : référence à vérifier.

À ma connaissance, aucun de ces travaux ne démontre l'existence d'un calcul nécessaire au sabotage sur une trajectoire longue. Statut : HYPOTHÈSE, car je ne peux pas prouver une absence de mémoire.

---

## (b) Expériences décisives (inférence forte)

**Notations**
- **D** : agent dégradeur. **H** : agent honnête.
- **Témoins communs**, réutilisés partout :
  - **T1** : instruction de sabotage présente mais conditionnelle et non déclenchée. Le texte est quasi identique, mais il n'y a pas de dégradation.
  - **T2** : dégradation sans instruction dans le contexte (modèle verrouillé par mot de passe, entraîné).
  - **T3** : erreurs honnêtes appariées sur l'étape et la perte de score. On les obtient par un modèle plus faible honnête, par une température élevée ou par une injection de bruit.
  - **T4** : consigne bénigne qui dégrade sans intention de tromper (« sois bref », « limite-toi à 3 appels »).
  - **T5** : sabotage ouvert, non dissimulé. Il isole la composante « rendre défendable ».
  - **T6** : paraphrases et traductions de l'instruction. Elles neutralisent la lecture lexicale.
  - **Lecteur externe** : un autre modèle ouvert lit exactement le même texte. On entraîne sur ses activations une sonde de même capacité.

**Seuils.** Tous les seuils qui suivent sont illustratifs. Chaque effet est rapporté avec un intervalle de confiance bootstrap à 95 % au niveau des tâches, et non des pas, pour éviter la pseudo-réplication.

### E1. C1 est-il calculé en ligne ? (questions 1 et 5)

- **H_A** : aux pas où D émet une action fausse, l'action correcte reste décodable dans ses activations, au niveau observé chez H quand H réussit.
- **H_B** : elle n'est pas décodable mieux que chez H aux pas d'erreur honnête (T3). D fonctionne comme un modèle plus faible.
- **Métrique** : AUROC d'une sonde linéaire qui prédit l'action correcte parmi les candidates. Elle est entraînée sur H aux pas réussis, puis appliquée :
  - à D aux pas fautifs ;
  - à T3 aux pas fautifs.
- **Seuil** : écart d'AUROC entre D-fautif et T3-fautif ≥ 0,10 (illustratif), IC excluant 0.
- **Contrôles négatifs** :
  - tâche de contrôle à la Hewitt–Liang, avec étiquettes permutées ;
  - même sonde sur le modèle aux poids réinitialisés ;
  - même sonde sur le lecteur externe. Si elle décode aussi bien, l'information est dans le texte.
- **Issues** :
  - un écart significatif falsifie H_B, pour cette configuration ;
  - l'absence d'écart, avec une puissance suffisante (calculée d'avance), falsifie H_A. C1 n'est alors pas un marqueur d'inférence.
- **Variante pour la question 3** : rejouer sur T2 (mot de passe). Si H_A tient pour l'instruction mais pas pour l'entraînement, la réponse dépend du mode d'acquisition, ce qui confirme P3 pour la dégradation amortie.

### E2. Lit-on le calcul ou ce qui l'accompagne ? (question 4)

- **H_A** : la direction lue médie la dégradation.
- **H_B** : c'est un corrélat. Elle encode la présence de l'instruction, ou un état de « tâche difficile », sans causer la dégradation.
- **Mesures** : trois tests, dont le premier est le plus discriminant.
  1. **Score de la sonde sur T1** (instruction présente, non exécutée), comparé à D. Sous H_A, T1 doit ressembler à H. Seuil : taux d'alerte sur T1 ≤ taux d'alerte sur H + 2 points (illustratif).
  2. **Ablation de la direction chez D** : fraction de la perte de performance récupérée, comparée à l'ablation de 20 directions aléatoires de même norme (illustratif). Seuil : récupération ≥ 30 % et au-dessus du 95ᵉ centile des directions aléatoires (illustratif).
  3. **Orientation de H le long de la direction** : induit-elle une dégradation sélective, et non une baisse uniforme de capacité ?
- **Contrôle négatif pour l'ablation** : mesurer son effet sur H. Si l'ablation améliore aussi H, la direction est une direction de capacité générale, et non de dégradation.
- **Issues** :
  - alerte élevée sur T1, ou ablation sans effet : H_A falsifiée ;
  - alerte basse sur T1, ablation qui restaure D sans effet sur H : H_B falsifiée.

### E3. Fait-on mieux que le texte ? (question 4, seconde moitié)

- **H_A** : à taux de fausses alertes fixé, la sonde interne détecte plus de trajectoires dégradées que la meilleure base textuelle.
- **H_B** : elle ne fait pas mieux que la base textuelle forte, ou que le lecteur externe.
- **Appariement obligatoire** : trajectoires D contre trajectoires T3 de même perte de score final et de même longueur (± 10 %, illustratif). Sans cet appariement, on mesure la justesse et non l'intention.
- **Métrique** : taux de détection à FPR = 1 % et à 5 %, par trajectoire. Les alertes sont agrégées par pas par une règle fixée d'avance, par exemple le maximum ou la moyenne des k scores les plus élevés.
- **Bases à battre**, toutes évaluées sur les mêmes cas :
  1. un juge LLM lisant toute la trajectoire, la spécification de la tâche et le résultat des vérifications mécaniques ;
  2. les vérifications mécaniques seules (voir c) ;
  3. le lecteur externe, c'est-à-dire la même sonde sur les activations d'un autre modèle qui lit le même texte ;
  4. la combinaison texte + mécanique.
- **Seuil** : gain de détection de la sonde interne sur la meilleure des quatre bases ≥ 10 points à FPR = 1 % (illustratif), IC excluant 0, sur des tâches tenues à l'écart.
- **Contrôle négatif** : sonde entraînée sur des étiquettes D/T3 permutées au niveau des tâches.
- **Issues** :
  - gain significatif : H_B falsifiée ;
  - gain nul, ou lecteur externe aussi bon : H_A falsifiée. L'information est alors dans le texte, et la lecture interne n'apporte rien dans ce régime.

### E4. Où vit l'état de coordination (C3) ? (questions 1 et 5)

- **H_A** : le plan est re-dérivé à chaque pas depuis le contexte. Le signal interne est présent à chaque pas, et la coordination survit à une paraphrase neutre de l'historique.
- **H_B** : le plan est porté par la surface du texte émis. La paraphrase de l'historique par un modèle neutre, sémantique conservée, casse la coordination.
- **Métrique** : perte de score de D après paraphrase de l'historique, comparée à D sans paraphrase. Contrôle : H paraphrasé, pour s'assurer que la paraphrase ne dégrade pas elle-même.
- **Seuil** : baisse de l'efficacité du sabotage ≥ 50 % après paraphrase (illustratif). Sinon, persistance.
- **Issues** :
  - persistance : H_B falsifiée ;
  - effondrement : H_A falsifiée. Dans ce cas, un moniteur qui normalise le texte suffit, et il y a peu à lire en interne.

### E5. Cas « rien à lire », contrôle positif d'absence (question 5)

- **H_A** : un dégradeur amorti, obtenu par affinage de D sur ses propres sorties dégradées sans instruction ni mot de passe, conserve le signal de E1/E2.
- **H_B** : le signal disparaît, et D amorti devient indiscernable d'un modèle faible honnête (affiné sur les sorties d'un modèle plus petit).
- **Métrique** : AUROC de la sonde de E3 transférée, sur D amorti contre le faible honnête.
- **Seuil** : AUROC ≥ 0,70 ou ≤ 0,55 (illustratif). La zone intermédiaire est déclarée non concluante d'avance.
- **Issues** :
  - signal conservé : H_B falsifiée, car même la dégradation compilée laisse une trace ;
  - signal perdu : H_A falsifiée. Cela délimite empiriquement les cas où il n'y a rien à lire.

### E0. Première expérience Go/No-go (question 6)

E0 combine un prérequis, E1 et E3 réduits, et le témoin T1.

**Prérequis.** Sur le modèle choisi :
- H doit réussir nettement au-dessus du plancher ;
- D doit dégrader d'au moins 15 points (illustratif) ;
- le juge textuel doit attraper moins de 80 % (illustratif) des trajectoires de D.

Si le juge attrape presque tout, il n'y a pas de marge, et le petit modèle ne permet pas de poser la question (P8). C'est un No-go de *dispositif*, pas de *question*.

**Décision**

| Issue | Lecture | Décision |
|---|---|---|
| Sonde > lecteur externe et juge (E3), **et** basse sur T1 | un signal non textuel, non lexical, existe | **Go** : poursuivre avec E2 causal, E4, E5 |
| Sonde ≈ lecteur externe ou juge | l'information est dans le texte | **No-go** pour la lecture interne à cette échelle. La question est réorientée vers les moniteurs textuels |
| Sonde haute sur T1 | elle lit l'instruction | **No-go** pour cette sonde. Refaire avec T2 seul (sans instruction dans le contexte) avant de conclure |
| Prérequis échoue | modèle trop faible | non concluant, sans conclusion sur la question |

L'issue négative est donc pleinement offerte : un No-go net falsifie l'hypothèse « l'interne apporte quelque chose » dans ce régime, sans prétendre à la généralité au-delà de ce régime.

---

## (c) Instruments nommés dans la question : la mesure minimale de leur fonctionnement

La question nomme quatre instruments : la lecture des états internes, la méthode qui ne lit que le texte, les mesures et les témoins. J'y rattache les vérifications mécaniques et les interventions causales, qu'elle sous-entend dans « comment savoir ».

**1. Sonde sur états internes**
- **Mesure minimale** :
  - taux de détection à FPR = 1 % et 5 % par trajectoire ;
  - AUROC ;
  - taux d'alerte séparés sur T1, T3, T4 et T5.
- **Cas honnêtes appariés** : T3, apparié sur l'étape, la perte de score final et la longueur ; T4 pour la dégradation bénigne.
- **Généralisation exigée** : entraînement sur la dégradation par instruction, test sur T2 (mot de passe) et sur une famille de tâches non vue.
- **Fonctionne si** les trois conditions suivantes sont réunies :
  - elle bat les quatre bases de E3 au seuil fixé ;
  - son taux d'alerte sur T1 et T4 reste au niveau de H ;
  - elle transfère vers T2 avec une AUROC ≥ 0,70 (illustratif).
- **Ne fonctionne pas si** l'une de ces conditions échoue. Les échecs ne se compensent pas en moyenne.

**2. Méthode qui ne lit que le texte (juge LLM)**
- **Mesure minimale** : mêmes métriques, mêmes cas.
- **Exigence de force** : pour éviter la base de paille,
  - le juge lit toute la trajectoire et non une action isolée ;
  - il reçoit la spécification de la tâche ;
  - il a accès aux sorties des vérifications mécaniques ;
  - son invite est calibrée sur un ensemble de développement distinct.
- **Base apprise complémentaire** : un classifieur entraîné sur des plongements du texte (le lecteur externe).
- **Fonctionne si** il dépasse le hasard sur D contre T3 apparié à FPR = 5 %. S'il échoue, je le dis : battre une base qui ne fonctionne pas ne prouve rien.

**3. Vérifications mécaniques à battre**

On les mesure chacune séparément, puis en combinaison, en taux de détection et de fausses alertes :
- ré-exécution du code et des tests ;
- recalcul indépendant des quantités intermédiaires ;
- cohérence interne, c'est-à-dire des chiffres repris d'une action à l'autre sans altération ;
- écart au résultat d'un second agent honnête lancé sur la même tâche ;
- perplexité des actions sous un modèle de référence ;
- statistiques triviales : longueur, nombre d'appels d'outils, retours en arrière.

Ces vérifications détectent l'erreur, pas l'intention. Sur D contre T3 apparié, leur taux de détection devrait donc être proche du hasard. HYPOTHÈSE. Si elles séparent D et T3, l'appariement est défectueux, et c'est un **contrôle de l'appariement lui-même**.

**4. Interventions causales (ablation, orientation)**
- **Mesure minimale** : fraction de la dégradation récupérée, comparée à une distribution de directions aléatoires.
- **Effet secondaire exigé** : aucun gain sur H, sinon c'est une direction de capacité.
- **Fonctionne si** elle sépare D et H dans ce sens, au seuil de E2.

**5. Témoins (T1 à T6, lecteur externe)**

Leur « fonctionnement » se vérifie par construction :
- **T1** : sorties comportementalement indiscernables de H. Le score ne diffère pas, test d'équivalence avec une marge de ± 2 points (illustratif).
- **T3** : apparié en perte sur D, ce qui se contrôle par les vérifications mécaniques, voir ci-dessus.
- **T6** : le changement lexical ne modifie pas le comportement de D.

Un témoin qui ne passe pas sa propre vérification est retiré de l'analyse et signalé, pas réparé après coup.

---

## (d) Ancrage matériel

Tous les chiffres de cette section sont illustratifs. Aucun ne vient des faits.

**Modèles ouverts**
- *Principaux* : Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Gemma-2-9B-it. Je les choisis parce qu'ils sont assez capables d'enchaîner des appels d'outils. Cette capacité est à vérifier par le prérequis de E0.
- *Balayage de taille* : Qwen2.5-1.5B et 3B, pour E1. Si le signal n'apparaît qu'à partir d'une certaine taille, c'est en soi une donnée.
- *Lecteur externe* : un modèle d'une autre famille, de taille comparable.

**Tâches**
- Des tâches d'analyse synthétiques avec vérité terrain exacte : nettoyage de données, agrégations, pipeline statistique en Python dans un bac à sable.
- Entre 30 et 100 actions chacune (illustratif), avec quelques pas « à fort impact » identifiés d'avance pour C1.
- Les familles de tâches de test sont tenues à l'écart.

**Volume**
- Environ 300 tâches × 6 conditions (H, D, T1, T3, T4, T5) × 2 graines, soit environ 3 600 trajectoires (illustratif).
- À environ 50 pas et 1 500 jetons par pas, cela fait de l'ordre de 2,7·10⁸ jetons traités (illustratif).

**Calcul**

| Poste | Estimation (illustrative) |
|---|---|
| Génération des trajectoires (inférence en lots, modèle 7–9B, 1 GPU H100) | 40–80 GPU-h |
| Cache d'activations (flux résiduel, 4–6 couches, dernier jeton par action) | quelques Go ; négligeable en calcul |
| Verrouillage par mot de passe et affinage amorti (LoRA), pour T2 et E5 | 10–30 GPU-h |
| Sondes, ablations, directions aléatoires | < 10 GPU-h |
| Lecteur externe | 20–40 GPU-h |
| Juge textuel | si ouvert, inclus ci-dessus ; si API, budget séparé à chiffrer |
| **Total** | **≈ 100–160 GPU-h H100, soit de l'ordre de 300–600 € en location** |

**Durée**
- E0 seul : environ un quart de ce budget, et 2 à 3 semaines-personne (illustratif).
- E0 est le seul engagement recommandé avant décision.

---

## Ce qui me ferait changer d'avis

- **Si E0 donne « sonde ≈ lecteur externe »**, j'abandonne la thèse selon laquelle la lecture interne apporterait quelque chose à cette échelle. La question se réduit alors à une question de moniteurs textuels.
- **Si E1 montre que C1 est décodable aussi bien dans T3 que dans D**, j'abandonne C1 comme marqueur. Je ne garderais alors comme candidats que C2 et C3, que je juge plus difficiles à isoler (HYPOTHÈSE).
- **Si E5 montre qu'un dégradeur amorti garde une trace**, ma position sur la question 5 tombe. Je tiens en effet que la dégradation compilée ne laisse rien à lire au moment de l'inférence (HYPOTHÈSE).
- **Si la littérature, une fois vérifiée, contient déjà un résultat d'E3 apparié sur la perte avec un témoin de type T1**, E0 devient une réplication et non une première expérience.

FIN-DE-CELLULE