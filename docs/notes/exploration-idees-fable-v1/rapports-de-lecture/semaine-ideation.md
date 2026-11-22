# Semaine de l'idéation (arXiv, 14 au 19 novembre 2026) : lecture des neuf prépublications

Agent de lecture, 22 novembre 2026. Les neuf PDF sont dans `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/semaine-ideation/` (fichier `IDENTIFIANT.pdf`, page arXiv `IDENTIFIANT.abs.html`). Tous ont été vérifiés avec `pdfinfo` : ce sont bien des PDF. Les pages citées sont celles du fichier PDF. Pour ces neuf textes, elles coïncident avec les numéros imprimés. Les dates de dépôt viennent de la ligne « Submitted on » de chaque page arXiv, et chacun des neuf textes n'a qu'une version (v1).

| Identifiant | sha256 | Pages | Dépôt de la v1 |
|---|---|---|---|
| 2611.21408 | a77a95b1a5f0463290e52de9c8002df198e8ab25f107a672342e4a0a8e38b0fc | 48 | 16 Nov 2026 |
| 2611.24887 | a50bf3f52dc4b6e83b4f4dce5c8c9b62c011b5f0df1407293e480ba188a7dbcb | 56 | 18 Nov 2026 |
| 2611.23546 | 4d8e4beca7c8bb789b1e3d7bce72d8ec7ee39fb1bf310040ff7eae458b3e1465 | 16 | 17 Nov 2026 |
| 2611.22988 | 883b47adf657f1912660f031e20d9bf7c67991b501891cdf5d80c5bea3dc2b27 | 34 | 17 Nov 2026 |
| 2611.21847 | 5eb48da51de50c8a14bece9c3ba88925f480791990ba6d8d9772ef946e594f08 | 24 | 16 Nov 2026 |
| 2611.19108 | b33469c01bf4687d267f1fe612e48e404a5e21ab33c3a820069217354e88fd1d | 16 | 14 Nov 2026 |
| 2611.25214 | 06c5a5a0a7d08b5cb16f09a2b5bdfbc96a9117e50f13c33d067d7ae5e23465c9 | 17 | 18 Nov 2026 |
| 2611.25003 | 7281bf7ea033c7b61b495f5ccb505e2e16e5c85cd4b66e26ab13dbd1f10b5d02 | 56 | 18 Nov 2026 |
| 2611.19794 | 6dd9aa4e09b2b013960c1ef2ded1454d4c4d4d942a497688830705fa1aacb15a | 23 | 15 Nov 2026 |

Étendue de la lecture : j'ai lu en entier le corps de chaque article (résultats, limites, conclusion), ainsi que les annexes nécessaires aux chiffres demandés. Les annexes longues de 2611.21408, 2611.24887 et 2611.25003 ont été lues par recherche ciblée, pas page à page. Statut : « lu sur PDF » pour tout ce qui suit, sauf mention contraire.

---

## 1. 2611.21408 — Javier Aguilar Martín, « Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next »

**Auteur et affiliation** : un seul auteur, rattaché à « AGILabs (javieraguilar.ai) », avec une adresse gmail (p. 1). **Code** : https://github.com/JaviMaligno/latent-gap-ideas (p. 25).

**Corpus** (p. 3) :
- jeux Steam : 68 222 jeux sortis avant 2024, 40 989 à partir de 2024 ;
- arXiv, informatique : 72 000 articles avant 2023, 41 000 du 1er janvier 2023 au 15 octobre 2026 ;
- brevets HUPD : 71 521 déposés de 2012 à 2015, 40 342 en 2016 et 2017.

Plongements principaux : Qwen3-Embedding-0.6B, avec BGE-M3 en réplication. La « vérité » de chaque épreuve est ce qui a paru après la date de coupure.

**Épreuve 1 : un point vide de la carte se décode-t-il en idée ? (section 3, p. 4 à 6)**
- Les directions lointaines tirées au hasard ne correspondent à aucun texte. Aucun article ultérieur ne dépasse un cosinus brut d'environ 0,10 avec elles (médiane 0,046 à 0,066). Après centrage ou blanchiment, ces points restent hors d'atteinte dans 22 cellules sur 24 (p. 2 et 5).
- Le décodeur, auquel on montre les huit voisins du point visé et qu'on guide seulement par le score obtenu, réécrit ces voisins. Quand on échange les voisins montrés, le texte suit les voisins échangés, dans les six jeux de cibles sur six (p. 5). L'auteur : « the decoder reads its prompt ».
- Les « trous intérieurs » de la carte, eux, se décodent. Une recherche sans voisins atteint un cosinus médian de 0,567 (Steam) et 0,472 (arXiv), et fait mieux que l'élément existant le plus proche sur 15 et 14 cibles sur 20, d'environ +0,04 (p. 5).
- Pour les points lointains, le meilleur texte cohérent reste quasi orthogonal à la cible (médiane 0,069 et 0,057) (p. 6).
- L'inversion de plongement (vec2text) n'a pas pu être testée de façon informative (p. 6).

**Épreuve 2 : les « trous » prédisent-ils où le champ grandit ? (section 4, préenregistrée, p. 6 à 10)**
- Dispositif : 256 cellules par k-moyennes sur la carte du passé ; la cible à prédire est d'appartenir au décile de croissance la plus forte.
- Le score de trou préenregistré mesure surtout la position et la taille de la cellule : corrélation de +0,74 à +0,80 avec la position, et ce score ne détecte pas les trous plantés (aire sous la courbe 0,45 à 0,59) (p. 7).
- Trois scores valides détectent bien les trous plantés (aire sous la courbe 0,74 à 0,99) mais prédisent la croissance au niveau du hasard ou en dessous : aire sous la courbe 0,30 à 0,66, et 0,27 à 0,32 sur arXiv à 12 mois (p. 7).
- La dynamique récente de la cellule (« momentum ») atteint 0,73 à 0,92 (p. 7).
- Ajouter un score de trou à cette dynamique n'apporte rien sur Steam ni sur arXiv (gain de −0,016 à +0,006). Le résultat sur les brevets est non concluant (p. 7).
- Les conclusions préenregistrées tiennent aussi dans un espace LSA ajusté sur le passé seul et dans all-mpnet-base-v2 (sorti en 2021), sauf Steam, non concluant en LSA (p. 9).
- Effet partiel : à dynamique égale, les cellules plus vides grandissent un peu plus (ρ partiel de 0,20 à 0,34). C'est une prédiction préenregistrée (F2) qui échoue, mais l'effet n'est pas exploitable pour prédire (p. 7).
- Les nouveaux jeux Steam plus isolés sont un peu mieux notés (ρ +0,107 à +0,132). Encore une prédiction qui échoue, cette fois dans le sens de la prémisse ; pour les brevets, c'est l'inverse (p. 7 et 8).
- L'épreuve au niveau de chaque élément (F6) n'a pas pu être menée comme prévu (p. 8).

**Épreuve 3 : un modèle qui prolonge un article reste-t-il plus près de sa source ? (section 5, p. 10 à 19)**
- Dispositif : 150 articles d'informatique de 2021-2022, et 2 883 articles qui les citent, parus à partir de 2024.
- Oui, les idées restent plus près de la source. Pour gpt-4o, l'écart de pas est de 0,149 (intervalle 0,138 à 0,160). Il tient avec trois formulations de la demande (0,135 et 0,130), contre les articles citants réécrits en propositions (0,112 avec la source montrée, 0,232 sans), et pour OLMo face aux citants d'avril à décembre 2023 (0,215) (p. 3, 10 à 12).
- Face aux seules vraies continuations (47 contextes), l'écart est de 0,048 (intervalle 0,019 à 0,076) (p. 11).
- gpt-5.4-mini (2026) fait pire : 0,211 (p. 18).
- Avec la critique itérative, la consigne de distance (GEO) allonge le pas de 0,087. La simple révision sans information (NEUTRAL) en fait déjà 0,045. Ce qui revient à la consigne elle-même, au-delà de la révision, est d'environ +0,04, répliqué sur 150 nouveaux contextes (p. 12 et 13).
- Sur l'orientation, montrer le titre d'un vrai article successeur tourne les idées de 0,032. Le relecteur, l'oracle et la consigne de distance obtiennent 0,13, 0,08 et 0,34 de ce virage, avec des bornes hautes de 0,46, 0,46 et 0,70. Ce gain « is not separable from revision or their longer step » (p. 1 et 17).
- Pour OLMo, le contrôle positif échoue (p. 17 et 18).

**Épreuve 4 : existe-t-il une distance optimale de la matière d'inspiration ? (section 6, p. 19 à 21)**
- Dispositif : 1 800 stimuli tirés de neuf sources (recettes, règles de sport, pages Wikipédia, etc.), classés en cinq tranches de distance ; gpt-4o propose un jeu à partir de chacun.
- Aucune courbe en cloche n'a été détectée (épreuve à deux droites). Mais la mesure d'anticipation préenregistrée échoue à sa propre validation : elle sépare les jeux réels des idées surtout par leur format. Le résultat nul est donc « uninformative » (p. 2 et 19 à 20).
- Ce qui reste établi : une matière plus lointaine donne des idées plus isolées (p. 20).

**Préenregistrement et faiblesses dites par l'auteur**
- Les épreuves d'origine ont été enregistrées avant l'exécution. Les suivis, dont treize ont été demandés par deux relectures faites par des agents (Claude Code, Codex), ont été écrits après les résultats principaux (p. 1 et 4).
- La datation repose seulement sur des commits locaux : « Commit timestamps are set locally and the public repository is a later anonymised copy, so nothing dates the registrations independently » (p. 4).
- Les étiquettes (continuation ou simple citation) sont données par deux modèles (κ = 0,75), puis contrôlées par un seul lecteur non expert sur 40 paires (p. 23).
- Les plongements peuvent avoir vu des textes postérieurs à la coupure ; un seul domaine sert à l'étude des continuations (p. 23).

**Ce que l'article ne montre pas** : qu'aucun usage d'une carte ne peut aider (l'auteur le dit, p. 24) ; la qualité des idées décodées dans les trous intérieurs ; l'effet d'un entraînement sur une récompense d'alignement avec le futur. Le jugement de nouveauté de l'annexe A.7 repose sur des juges-modèles et 80 notes de l'auteur.

---

## 2. 2611.24887 — Yu, Zou, Lim, Shah (National University of Singapore), Goyal (Meta Superintelligence Labs), Liu, « Ground, Iterate, Trace: Decomposing AI Research Ideation » (CAR)

**Procédé** (p. 3 à 5) : la littérature trouvée est réduite à au plus 20 articles, dont on extrait un graphe de connaissances typé, figé ensuite. Un agent fait évoluer une proposition avec quatre opérateurs (tableau 1, p. 4), chacun vérifié par des conditions structurelles :
- **bisociation** : relier deux entités existantes non liées par une entité-pont nouvelle ;
- **analogie** : transférer une relation d'une paire source vers une paire cible dont les deux extrémités changent ;
- **exploration** : ajouter un pas depuis une entité ;
- **élaboration** : préciser une entité proposée.

Au moins trois opérations doivent être acceptées avant de proposer (p. 5).

**Évaluation** : 40 mots-clés de LiveIdeaBench, deux modèles de base (GPT-5.4 et GLM-5.2), cinq idées par mot-clé. Trois juges-modèles d'autres fournisseurs notent originalité, faisabilité et clarté ; un juge de « nouveauté méthodologique » s'appuie sur les 10 articles retrouvés. L'accord de ces juges avec les notes d'experts de Si et al. est ρ = 0,36 à 0,39 (p. 5 et 6).

**Résultats**
- Nouveauté méthodologique : 6,63 et 6,74, nettement au-dessus de la génération en un coup (5,36 et 4,87) et de The AI Scientist (5,81 et 6,16). Écart non significatif face à RIA (6,88 et 6,58) (p. 6 et 7).
- **Bancs d'exécution**, avec un exécutant commun (celui de The AI Scientist-v2), donc jugés par la mesure de test du banc et non par un modèle :
  - FML-bench-Lite (8 tâches, 3 exécutions) : taux de victoires par paires de 75,0 % contre 58,3 % au mieux pour les autres, mais une moyenne de 0,167 contre 0,165 pour AIDE (p. 7) ;
  - BioXArena (9 tâches valides, 1 exécution) : 64,8 %, moyenne 0,810, contre 0,806 pour TAS-v2 ; la référence humaine fait 72,2 % et 0,821 (p. 7 et 8).
- **Ablation à dix conditions** (tableau 5, p. 8) : « No MN contrast survives Holm correction over the nine conditions within each backbone (smallest p = .076) ».
  - Contre l'itération libre sans opérateurs : −0,02 ± 0,12 et +0,37 ± 0,12.
  - Contre la génération en un coup : +0,40 et +0,36.
- **Phrase exacte** : « The results do not establish a consistent quality benefit from explicit operators beyond free-form iteration. » (p. 1). Voir aussi « These results do not establish an advantage from operators beyond free-form iteration. » (p. 8).
- Coût : l'itération libre coûte à peu près autant que CAR (0,193 contre 0,185 dollar par idée sur GPT-5.4), donc le budget est comparable dans l'ablation. CAR coûte environ quatre fois plus que The AI Scientist (p. 26).

**Limites dites** : les traces établissent une provenance, pas une nécessité causale ; aucune note humaine sur leurs propres idées (p. 9). BioXArena a été corrigé le 7 octobre et les résultats seront refaits (p. 8, note 1).

**Ce que l'article ne montre pas** : que la bisociation ou l'analogie améliorent l'idée. Les gains sur les bancs d'exécution sont minces (moyennes à quelques millièmes près, une seule exécution sur BioXArena).

---

## 3. 2611.23546 — Guy Zyskind (University of Miami), « Language Models Make New Research Sound Old »

**Auteur** : seul. Aucun lien de code trouvé dans le texte.

**Dispositif** (p. 2 et 3) : 40 questions tirées d'articles acceptés à COLM 2026, parus après l'entraînement des modèles. La recherche arXiv est limitée à la date limite de soumission et l'article qui répond est exclu.

Chaque système produit deux choses :
- une réponse ordinaire, étiquetée par deux modèles (un d'OpenAI, un d'Anthropic) comme « étudiée », « ambiguë » ou « ouverte » ;
- un jugement forcé OUI ou NON, posé à part.

À cela s'ajoutent 503 questions en « échelles », tirées de LitSearch (une, deux ou trois composantes modifiées), et une comparaison de 22 modèles sur les mêmes articles.

**Écart entre le jugement correct (« non étudiée ») et la réponse ordinaire « ouverte », avec recherche en direct** (tableau 4, p. 12) :

| Système | Jugement « non étudiée » | Réponse « ouverte » | Écart (points) |
|---|---|---|---|
| Astra | 98 % | 8 % | +90 [80, 98] |
| Sol | 100 % | 38 % | +62 |
| Luna | 100 % | 70 % | +30 |
| Sonnet | 98 % | 68 % | +30 |
| Opus | 78 % | 48 % | +30 |
| Fable | 92 % | 35 % | +57 |

**Autres résultats**
- Avec les mêmes articles fournis à tous les systèmes, l'écart groupé est de +40 : 92 % de jugements « non étudiée » contre 52 % de réponses « ouverte » (p. 4 et 12).
- **Asymétrie** : sur les questions déjà étudiées, quand l'article qui y répond est disponible, la réponse le dit clairement dans 88 à 100 % des cas (p. 4).
- Les affirmations de quasi-recouvrement sont fausses dans 34 cas sur 43 pour les questions COLM. Les modèles en rejettent 31 sur 34 quand on leur demande de vérifier l'article à part (p. 4).
- Remplacer l'article le plus proche par un article seulement voisin par le thème fait baisser les réponses ambiguës de 28 points (p. 5).
- Les modèles plus capables jugent mieux mais ont un écart plus grand : ρ = +0,81 sur 22 modèles (p. 6).
- **Remède** : construire la réponse à partir du jugement du modèle et de ses propres vérifications d'articles. Pour Astra, les réponses « ouverte » passent de 8 % à 95 % ; sur la liste commune, de 52 % à 92 % (+40). Demander seulement au modèle d'énoncer d'abord son jugement fait passer de 52 % à 63 % (p. 6 et 7).
- Notes de nouveauté sur l'échelle de TPR : elles séparent les questions étudiées des ouvertes avec une aire sous la courbe de 52 %, contre 84 % pour le jugement direct (p. 8).

**Limites dites** : surtout de l'apprentissage automatique ; étiquetage par des modèles ; les « lecteurs » sont des modèles et non des chercheurs (p. 8).

**Faiblesses** : auteur seul ; 40 questions (intervalles larges, par exemple [80, 98]) ; le jugement est porté par des modèles du début à la fin. **Ce que l'article ne montre pas** : un effet sur de vraies décisions de recherche.

---

## 4. 2611.22988 — Nah, Park et al. (Asteromorph, Séoul ; Gachon University ; Seoul National University), « Structured AI ideation yields physical strategies for epithelial barrier repair » (Abelio)

**Procédé** (p. 4 et 14 à 15) : passerelle → noyau d'idéation → rédacteur. Le noyau d'idéation a trois sous-systèmes :
- **Formulation** : trois agents reformulent l'objectif (échelles biologiques, voies alternatives, lacunes de la littérature) ; dix formulations distinctes sont retenues.
- **Sélection d'éléments** : des éléments de stratégie « inspired by approaches from other domains » et des éléments matériels. Les agents de recherche reçoivent seulement les exigences, « not the formulation or original objective », pour éviter le biais vers les solutions classiques.
- **Idéation et raffinement** : tirage de 75 % du réservoir d'éléments, combinaison de deux ou trois éléments, puis débat entre défenseur, relecteur et juge sur sept tours au plus.

La sélection se fait sans modèle génératif : regroupement de plongements puis reclassement.

**Comparaison avec quatre modèles de pointe** (p. 5 et 8) :
- 50 objectifs ; 293 hypothèses produites, 212 retenues ; coût de 417 dollars (p. 5).
- Solidité scientifique jugée par trois juges-modèles. La distance à la littérature et la diversité sont calculées par plongements, sans juge.
- Abelio fait mieux sur la solidité que les quatre, et sur la distance que trois d'entre eux (pas Gemini 3.1 Pro).
- Les hypothèses d'Abelio ont été résumées par GPT-5.5 pour égaliser la longueur.

**Ablation par sous-système** (fig. 2d à 2g, p. 8, chiffres lus sur la figure) :
- Sans Formulation, la diversité baisse (p = 0,035) ; effet standardisé +0,22.
- Sans Sélection d'éléments, la distance à la littérature baisse avant le raffinement (p < 0,001, non ajusté) mais pas après (p = 0,247) ; effet standardisé −0,02.
- Sans Raffinement, la solidité baisse fortement (+2,88, p < 0,001).
- Le raffinement augmente aussi la distance à la littérature (+0,45) et la diversité (+0,63), ce qui est noté sur la figure mais pas commenté.


**Épreuve expérimentale des deux propositions archivées** (p. 7 à 11)
- Sur 9 rapports produits pour l'objectif « restaurer la barrière épithéliale intestinale », l'investigateur en retient un. Il en tire deux sous-objectifs, qui donnent 8 rapports chacun ; trois investigateurs en choisissent un par sous-objectif. Les deux propositions retenues ont été « finalized and archived on 6 March 2026, before experiments began on 1 April 2026 » (p. 17) : l'archivage précède donc bien l'expérience.
- **Proposition 1 (polymère ancré en surface)** : le principe tient, mais la prédiction mécanistique précise d'Abelio est **réfutée** — l'effet ne vient pas de la face que le modèle avait désignée, mais du traitement des deux faces. Les auteurs écrivent : « Abelio identified a promising intervention but proposed an incomplete mechanism » (p. 9). Le polymère libre, à exposition totale égale, n'a aucun effet : c'est l'ancrage, pas le polymère, qui compte (p. 9).
- **Proposition 2 (brins d'ADN complémentaires ancrés)** : approche sans précédent dans ce domaine selon les auteurs. L'effet dépend de la complémentarité des séquences (le témoin brouillé fait beaucoup moins) et il est annulable à la demande par un brin envahisseur (p. 9 et 11). Les auteurs notent que l'appariement entre membranes opposées n'a pas été visualisé directement : c'est l'interprétation la plus cohérente, non une observation (p. 11).
- **Qui juge quoi** : la solidité est jugée par des modèles ; la diversité et la distance à la littérature, par des plongements ; le choix des propositions à tester, par les investigateurs humains ; le résultat final, par l'expérience. Les auteurs insistent : « Experimental implementation required investigator-led decisions and empirical optimization » (p. 13), notamment le choix des séquences et des concentrations, qu'Abelio n'a pas fixés.

**Limites dites** : nécessité d'une validation sur l'animal ; un seul objectif passé au laboratoire, donc pas de généralité établie ; les juges-modèles ont des limites reconnues ; « no individual metric can determine whether a proposal will yield a valuable experiment » (p. 13). La nouveauté est volontairement exclue des critères des juges, « because LLM judges may reward novelty-like phrasing rather than genuine novelty » (p. 16).

**Faiblesses** : l'entreprise qui vend le système est premier auteur ; un seul cas de laboratoire, choisi par les investigateurs parmi 25 rapports au total ; l'ablation de la sélection d'éléments change aussi l'invite, ce que les auteurs reconnaissent (p. 11). **Ce que l'article ne montre pas** : qu'une proposition d'Abelio vaut mieux qu'une idée humaine, ni que la voie « éléments hors discipline » est ce qui a produit les deux propositions testées — l'ablation ne le montre qu'avant raffinement.

**Données et code** : https://github.com/Asteromorph-Corp/abelio-1.0 (p. 19).

---

## 5. 2611.21847 — Jana (Georgia Tech), Kanakaris, Jain, Deoras, Genc (Amazon), « Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery »

**Architecture** (p. 2 et 4 à 6)
- *N* unités autonomes en parallèle, chacune avec son arbre d'idées (sa lignée) et un agent mutateur ⟨modèle, harnais⟩.
- Un orchestrateur par unité agit de trois façons : **Retool** (faire évoluer le harnais, gardé seulement si des essais jumelés donnent des enfants significativement meilleurs), **Redraw** (changer de modèle quand le progrès cale), **Restart** (archiver la lignée et repartir d'une nouvelle graine après un second blocage).
- Des vérificateurs évaluent chaque idée : score sur données retenues, contrôle des contraintes, épreuve hors distribution, ablation de chaque composant. Eux seuls écrivent dans le savoir partagé, **unique canal entre unités**, qui contient des découvertes vérifiées, partielles et réfutées (p. 6).
- Le mutateur travaille dans un bac à sable sans accès aux données de validation ni de test (p. 16).

**Chiffres principaux** (p. 7 et 8)
- EurekaBench : 73,6 % de score conditionné contre 56,2 % pour CORAL ; seul système à passer toutes les épreuves de contrainte.
- SciLaws-Bench : 62,8 % contre 59,3 %, et il bat la loi publiée sur 31 des 38 tâches contre 28.
- IdeaBench : 26,0 idées nouvelles distinctes par article contre 18,6 pour ResearchAgent, « with 82% fewer model calls » (45 appels contre 247).
- ScholarCatalyst : 44,5 contre 36,5 pour le meilleur agent.
- IdeaScientist : 82,7 % contre 77,7 %.

**Budget** : partiellement égalisé. Sur EurekaBench, la figure 3b compare à coût égal (64,7 % après 10 tours contre au plus 52,8 %). Sur SciLaws-Bench, 25 fois plus d'échantillons ne font passer le meilleur agent que de 56,9 % à 59,3 %, sous les 62,8 % d'Inventa. Sur IdeaBench, Inventa utilise moins d'appels que ses concurrents. Mais les comparaisons ne sont pas toutes faites à budget strictement apparié.

**Ablations** : c'est le point faible du texte au regard de la question posée.
- **Aucune ablation ne retire les reprises (Restart, Redraw) ni le canal partagé.** On a seulement une statistique descriptive : « On 11 of 16 tasks, the validation-best law comes from a lineage that Restart re-seeded, and 90 of the 320 units end on an evolved harness » (p. 20). Cela ne dit pas ce que vaut le mécanisme, puisque rien ne compare à une version sans lui.
- La seule ablation chiffrée porte sur l'étape de raffinement d'IdeaBench, sur 100 articles de validation (tableau 8, p. 21) : sans l'invite de réécriture pour la nouveauté, la nouveauté maximale tombe de 8,81 à 7,99 ; sans la règle de conservation au niveau de l'article, les idées très innovantes passent de 17,5 à 12,8 ; en ne réécrivant que les meilleures idées, 12,8 et la part d'idées faibles double (7,4 % à 14,3 %) ; avec 10 réécritures au lieu de 18, 14,7.
- Sans raffinement par article, Inventa rend 23,4 idées nouvelles avec 24 appels (p. 21).

**Qui juge** : programme pour EurekaBench, SciLaws-Bench et ScholarCatalyst (métriques de banc) ; juge-modèle étalonné sur RINoBench pour IdeaBench. Les auteurs refont le calcul avec deux juges non employés dans la boucle : Inventa garde l'avantage (17,5 et 13,5 contre 13,1 et 11,3 au mieux), mais OpenEvolve a une nouveauté maximale voisine et un peu plus d'idées notées ≥ 8 sous les deux juges (p. 20 et 21).

**Ce que l'article ne montre pas** : la part de chaque mécanisme central (unités décentralisées, canal vérifié, reprises) dans le gain ; aucune section de limites n'est écrite. Pas de lien de code dans le texte (une « Project Page » est annoncée p. 1).

---

## 6. 2611.19108 — Kambhamettu, Krashen, Ungar (University of Pennsylvania), « Guiding AI Agents to Generate Conjectures by Encoding How Theorems Build on One Another »

**Construction du graphe** (p. 2 et 3) : partant d'un article-graine, l'agent remonte les références et redescend les citations par Semantic Scholar, lit le texte intégral et extrait chaque théorème sous la forme (cadre, hypothèses, conclusion, source). Il compare ensuite les théorèmes deux à deux et pose une arête quand l'un s'appuie sur l'autre.

**Types de relation** : l'arête porte une description du changement de cadre, d'hypothèses et de conclusion, plus « the new idea needed to make the step » (p. 3). Les trois mouvements annoncés dès le résumé sont : modifier le cadre ou les hypothèses, renforcer la conclusion, étendre la portée (p. 1).

**Dispositif** : 30 articles-graines (18 tirés de Math-Graph, 12 écrits par un mathématicien collaborateur). Claude Opus 5.5, budget par exécution de 7 dollars, 150 pas, 60 minutes, identique dans les deux conditions (p. 4). Jugement par trois juges-modèles (GPT-6.1 Sol, Grok 4.7, Claude Sonnet 5.5), chaque paire présentée dans les deux ordres.

**Préférences** (tableau 2, p. 6)
- Préférence générale : 50 contre 29, soit **63 %** hors égalités (intervalle [52, 73], p = 0,02).
- Importance : 66 % (p < 0,001) ; ambition : 64 % (p < 0,001) ; perspicacité : 63 % (p = 0,002) ; nouveauté : 58 % (p = 0,14, non significatif).
- **Plausibilité : 32 % seulement, en faveur de la référence** (p < 0,001). C'est l'arbitrage central du texte.
- En traitant chaque article comme une unité, la préférence reste à 63 % mais p = 0,13 (note 2, p. 5).

**Mathématicien expert** : il compare à l'aveugle les conjectures sur ses 12 articles et préfère celle du graphe 8 fois sur 12, soit **67 %** [39, 86]. Accord avec la majorité du jury sur 9 articles sur 12 (κ = 0,47) (p. 5).

**Ablation à corpus fixe** (p. 7)
- *Choix des articles* : quand les deux agents construisent un graphe, aucune préférence nette entre les deux jeux d'articles (52 % hors égalités, p = 0,89). « This comparison provides no evidence that TEG-selected papers alone improve conjecture quality. »
- *Construction du graphe, articles fixés* : 58 % [43, 72] et, face à l'agent d'origine, 64 % [50, 77] ; p = 0,36 et 0,07, donc non significatif à cette taille.
- *Graphe complet contre graine seule* : 73 % [48, 89], p = 0,12 ; plus novateur (81 %, p = 0,007) et plus perspicace (73 %, p = 0,02).
- *Graphe complet contre graphe sans arêtes* : 60 % [31, 83], p = 0,75 ; plus ambitieux (83 %, p = 0,04).
- Les conjectures du graphe complet n'ont jamais été signalées fausses (0 sur 9), contre 4 sur 18 pour les conditions sans annotation ou à arêtes brouillées — mais les auteurs disent que ce regroupement n'isole pas l'effet des descriptions d'arêtes (p. 7).

**Limites dites** (p. 8) : peu d'articles-graines, un seul modèle générateur, pas de validation experte à grande échelle de l'extraction des théorèmes, et surtout : « TEGs also emphasize extensions of known theorems, and citation traversal favors developments connected through the literature. This may underrepresent conjectures with unexpected phenomena or connections between distant areas. »

**Faiblesses** : échantillons très petits (9 articles pour les ablations de structure, intervalles de 30 points) ; aucune conjecture n'a été prouvée ; corrections de multiplicité non appliquées (le tableau 2 le dit).

---

## 7. 2611.25214 — Yu, Feng, Ning, Yang, You, Zhou (University of Maryland ; UIUC ; MBZUAI), « Steering Automated Scientific Discovery via Audited Epistemic Exploration » (EpiCompass)

**Critère de choix** (p. 4 et 5) : un arbre épistémique garde les hypothèses, les croyances et les étiquettes de soutien, conflit ou neutralité des données. À chaque proposition, le système tire K = 4 candidats et en choisit un par **gain épistémique anticipé**, somme d'un terme de croyance et d'un terme d'exploration. Attention : cette évaluation est **qualitative, faite par le modèle lui-même** (« The LLM assesses each candidate's anticipated epistemic gain… These criteria provide a qualitative assessment », p. 5) ; ce n'est pas une quantité calculée. Les croyances sont aussi des crédences attribuées par le modèle (p. 4). Une vérification finale contre l'arbre complet précède la soumission.

**Bancs** : DiscoverPhysics, ActiveSciBench-Chem, NewtonBench. Trois modèles de base : Gemini-3.1-Flash-Lite, Gemini-3.7-Flash, Muse-Glimmer-30B. **Jugement par programme** (les métriques officielles des bancs), ce qui est une force de ce texte.

**Références comparées** : ReAct, Hypothesis Search, Popper. « Under the same experimental budgets » (p. 2) ; sur NewtonBench, EpiCompass utilise même moins de jetons que Hypothesis Search (10,2 k contre 21,4 k par tâche) pour une exactitude symbolique supérieure (60,9 % contre 49,9 %) (p. 7).

**Chiffres** (tableaux 2 et 3, p. 6 et 7)
- NewtonBench : exactitude symbolique de 46,6 → 60,9 % (Gemini-3.1-Flash-Lite), 37,7 → 53,0 % (Gemini-3.7-Flash), 66,5 → 72,1 % (Muse-Glimmer-30B).
- ActiveSciBench-Chem : 64,2 → 79,0 % ; 87,7 → 90,1 % ; 69,1 → 85,2 %.
- DiscoverPhysics : erreur normalisée de 25,46 → 1,42 ; 0,121 → 0,012 ; 117,762 → 0,376. Mais pass@1 reste à 3,0 % pour deux des trois modèles (contre 0,0 % pour les références), donc le banc reste quasi irrésolu.
- Types d'erreur sur 243 trajectoires (p. 7) : ancrage 25,1 → 19,8 %, exploration 16,9 → 14,8 %, cognition 15,7 → 9,5 %. Les auteurs le disent eux-mêmes : « Exploration errors decrease more modestly, suggesting that identifying unresolved gaps may be insufficient to produce more informative hypotheses » (p. 7).

**Ablations cumulatives** (tableau 4, p. 8) : sans mise à jour des croyances, 60,9 → 57,7 % sur NewtonBench et 79,0 → 67,9 % en chimie ; en retirant en plus l'autovérification, l'erreur de DiscoverPhysics passe de 1,39 à 4,32 ; en retirant enfin la sélection par gain épistémique, 47,8 % et 25,46. Ce sont des ablations cumulatives, donc les contributions ne sont pas séparées individuellement.

**Faiblesses** : pas de section de limites propre (seule une déclaration d'impact) ; aucun intervalle de confiance sur les tableaux principaux ; l'« audit » du titre est fait par le même modèle que celui qui propose ; pas de lien de code.

**Ce que l'article ne montre pas** : que l'exploration elle-même s'élargisse. Le gain principal porte sur l'ancrage des affirmations et la révision des croyances, les deux auteurs le concèdent.

---

## 8. 2611.25003 — Prada-Corral (ETH Zürich, MPI-IS, ELLIS Tübingen), Emara (Cornell), O'Donnell (McGill, Mila), Cotterell (ETH), Vieira, « A Model of Diverse Sampling from Language Models » (PoolDPP)

**Énoncé** : la génération diverse est posée comme le tirage d'un sous-ensemble de K chaînes selon un processus ponctuel déterminantal, où la norme du plongement porte la qualité et sa direction le sens. Le noyau est L(x, y) = √κ(x) φ(x)ᵀ φ(y) √κ(y), avec κ(y) = p(y)^(1/T) (p. 4). PoolDPP tire N candidats d'une proposition traitable, les repondère par importance vers cette qualité, puis applique un échantillonneur K-DPP au réservoir (p. 5).

**Théorème 5.2 (borne en taille du réservoir, p. 7)** : pour tout K ≥ 1, N ≥ K et toute proposition q telle que κ ≪ q,

KL(P̄ ‖ P) ≤ log(e^θ − 1 + a₀) ≤ θ, avec θ = K²ρ / (N − K + 1),

où ρ = E_{y∼q}[u₁(y)²] est le moment d'ordre deux du rapport d'inclusion, et a₀ un terme hypergéométrique. La divergence décroît donc en O(1/N).

**Hypothèses** : (i) continuité absolue κ ≪ q ; (ii) ρ < ∞, c'est-à-dire ρ = 1 + χ²(π₁ ‖ q) fini, donc une proposition qui ne rate pas les régions que la cible charge ; (iii) la borne porte sur la **loi marginale de sortie**, moyennée sur les réservoirs, et pour le mode échantillonnage seulement. Les auteurs sont explicites : « PoolDPP-MAP is a deterministic function of the pool and inherits no distributional guarantee » (p. 7). Et la borne ne peut pas être calculée sur le vrai modèle ; elle est évaluée sur une instance finie construite à partir des réservoirs, qui ne couvrent qu'une masse médiane de 0,0017 sur GSM8K et 0,0003 sur FineWeb : « These values are the bound on the instance, not a bound on the sampler on the full proposal » (p. 7).

**Résultat empirique principal** : le front qualité-diversité est étendu sur FineWeb (par le mode MAP ; le mode échantillonnage reste **sous** le front des K-moyennes à diversité intermédiaire, fig. 2, p. 8) et le front précision-rappel l'est sur Ambrosia (précision 0,392 à rappel 0,238, au-dessus de la meilleure précision des K-moyennes, p. 10). Sur GSM8K, le gain est seulement sur l'axe de la diversité : « At equal diversity, neither mode has a higher pass@K than ancestral sampling, so the gain is in diversity, not in coverage » (p. 10) — meilleur pass@K ancestral 0,925, PoolDPP 0,915, et l'exactitude par chaîne chute de 0,682 à 0,502 au réglage de pure diversité.

**Limites dites** (p. 10) : on ne peut pas retrouver ce que la proposition ne tire jamais (les réservoirs d'Ambrosia contiennent au plus 42 % des interprétations attendues) ; ce qui compte comme divers est fixé par le plongement ; la température globale optimale change d'une tâche à l'autre et d'un mode à l'autre, donc il faut des étiquettes ou une cible de diversité pour régler le point de fonctionnement.

**Point fort** : les preuves sont formalisées en Lean, dans le dépôt https://github.com/rycolab/pool-dpp (p. 6). **Ce que l'article ne montre pas** : aucun lien avec l'idéation scientifique — c'est un article de décodage. La diversité y est sémantique au sens d'un plongement, pas conceptuelle.

---

## 9. 2611.19794 — Trehan, Chopra (Lossfunk), « Eliciting Research Taste in LLMs through Future Research Direction Choice »

**Statut** : « Published as a workshop paper at COLM 2026 » (p. 1). Code : https://github.com/Lossfunk/research-taste-eval-v1.

**Dispositif** (p. 3) : à partir de 41 articles d'apprentissage automatique de décembre 2025 à février 2026 (après les coupures annoncées), Claude Sonnet 4.5 extrait l'objectif de recherche, les hypothèses avec leurs résultats et les travaux futurs, puis reformule tous les travaux futurs dans un style uniforme. Les leurres sont des travaux futurs réels tirés des cinq articles les plus proches, filtrés par longueur (0,75 à 1,25 fois) et par un juge Sonnet 4.5 (distinction, plausibilité). 19 articles sur 41 sont retenus, soit **80 paires**, chacune posée dans les deux ordres (160 invites). Température 0, une réponse par invite.

Trois mesures : **alignement avec l'auteur** (l'option de l'auteur choisie dans les deux ordres), **divergence stable** (le leurre choisi dans les deux ordres), **choix instable** (le choix change avec l'ordre).

**Chiffres** (tableau 2, p. 17 ; figure 3, p. 4)

| Modèle | Alignement | Divergence stable | Instable |
|---|---|---|---|
| Gemini 3 Pro | 67,5 % [56,6 ; 76,8] | 15,0 % | 17,5 % |
| Gemini 3 Flash | 62,5 % | 23,8 % | 13,8 % |
| GPT-5.2 Pro | 57,5 % | 30,0 % | 12,5 % |
| Claude Opus 4.5 | 55,0 % | 26,2 % | 18,8 % |
| Claude Haiku 4.5 | 50,0 % | 21,2 % | 28,7 % |
| GPT-OSS-120B | 50,0 % | 36,2 % | 13,8 % |
| Qwen3 Max Thinking | 50,0 % | 23,8 % | 26,2 % |
| Llama 4 Maverick | 45,0 % | 35,0 % | 20,0 % |

- Référence : une heuristique de pure similarité obtiendrait 80 % d'alignement (l'option de l'auteur est plus proche du contexte dans 64 paires sur 80). **Aucun modèle n'atteint ce niveau** (p. 5).
- 169 divergences stables au total, sur 45 paires distinctes ; 24 paires en déclenchent chez au moins quatre modèles (p. 4).
- Elles tiennent sous quatre variantes d'invite : 66,9 % à 80,5 % de divergences retenues en moyenne pondérée. Quand elles ne tiennent pas, elles deviennent instables plutôt que de revenir vers l'auteur (p. 5 et 6).
- Accord entre modèles : de 51,2 % à 80,0 %, moyenne 61,9 % (p. 5).
- Référence humaine, pilote : 10 participants, 108 réponses sur 23 paires, 13 abstentions ; parmi les 95 choix fermes, 61,1 % vont à la direction de l'auteur. Les humains ne voyaient qu'un seul ordre, donc la comparaison avec les modèles n'est pas directe (p. 6).

**Vers quoi les modèles divergent** (p. 6 et 7) : sur les 169 divergences, 128 (75,7 %) franchissent une frontière de catégorie. Les trois familles les plus fréquentes sont infrastructure-et-données → méthode (55 cas), méthode → passage à l'échelle et généralisation (23), application → passage à l'échelle (12), soit 70,3 % des transitions entre catégories. La première est bidirectionnelle (un arbitrage) ; les deux autres montrent un mouvement net vers le passage à l'échelle et la généralisation.

**Limites dites** (p. 8) : la référence est la préférence de l'auteur, pas un optimum ; les leurres sont de vrais travaux futurs et pourraient être de meilleures directions ; la contamination après la date de coupure n'est pas exclue ; **un seul modèle (Sonnet 4.5) fait l'extraction, la reformulation et le filtrage des leurres**, ce qui peut propager ses biais ; 80 paires et 19 articles, tous en apprentissage automatique ; l'analyse des transitions ne porte que sur le sous-ensemble divergent et ne dit rien de la fréquence d'occasion de chaque transition.

**Ce que l'article ne montre pas** : qui a raison. Les auteurs le disent explicitement — « our goal is not to score models as having high or low taste ».

---

## Tableau de synthèse

| # | Article | Objet | Qui juge | Budget égal | Résultat central | Faiblesse principale |
|---|---|---|---|---|---|---|
| 1 | 2611.21408 (16 nov.) | Les distances dans une carte de plongements guident-elles l'idéation ? | Programme (ce qui a paru après) | Oui dans les bras comparés | Quatre épreuves : les points vides ne sont pas des idées ; les trous ne prédisent pas la croissance ; le modèle fait un pas trop court et la consigne de distance l'allonge sans l'orienter ; pas de courbe en cloche (mesure invalide) | Auteur seul, datation par commits locaux, suivis écrits après les résultats |
| 2 | 2611.24887 (18 nov.) | Décomposer l'idéation : ancrage, itération, opérateurs | Juges-modèles + exécution sur deux bancs | Oui (coût par idée comparable) | Les opérateurs explicites n'apportent rien d'établi au-delà de l'itération libre ; taux de victoires le plus élevé à l'exécution (75,0 % et 64,8 %) | Aucun contraste d'ablation ne survit à la correction ; une seule exécution sur BioXArena |
| 3 | 2611.23546 (17 nov.) | Les modèles font passer du neuf pour du connu | Modèles, avec revue par les pairs comme vérité | Sans objet | Écart de 30 à 90 points entre le jugement correct et la réponse ordinaire ; asymétrie (88 à 100 % quand c'est vraiment étudié) ; remède portant Astra de 8 % à 95 % | Auteur seul, 40 questions, étiquetage entièrement par modèles |
| 4 | 2611.22988 (17 nov.) | Idéation structurée avec éléments hors discipline, épreuve en laboratoire | Plongements, juges-modèles, puis expérience | Non précisé face aux modèles de pointe | Deux propositions archivées avant l'expérience : principes confirmés, une prédiction mécanistique réfutée ; la reformulation d'objectif porte la diversité, le raffinement la solidité | Un seul cas de laboratoire, choisi par les investigateurs ; entreprise auteure |
| 5 | 2611.21847 (16 nov.) | Unités autonomes, savoir partagé vérifié, auto-adaptation | Programme (4 bancs) + juge-modèle (IdeaBench) | Partiellement (figure à coût égal sur un banc) | En tête sur cinq bancs, de 6 à 40 % ; 26,0 idées contre 18,6 avec 82 % d'appels en moins | Ni les reprises ni le canal partagé ne sont ablatés ; pas de section de limites |
| 6 | 2611.19108 (14 nov.) | Graphe d'évolution des théorèmes pour conjecturer | 3 juges-modèles + 1 mathématicien expert | Oui (mêmes modèle, outils, budget) | 63 % de préférence [52, 73] ; expert 8 sur 12 ; gain sur importance, ambition, perspicacité ; **perte sur plausibilité (32 %)** ; à corpus fixe, le gain vient de la construction du graphe, pas du choix des articles | 30 graines, 9 pour les ablations de structure ; aucune conjecture prouvée |
| 7 | 2611.25214 (18 nov.) | Choisir par gain épistémique anticipé | Programme (métriques de banc) | Oui, et moins de jetons | Gains sur les trois bancs (par ex. 46,6 → 60,9 % sur NewtonBench) ; les erreurs d'exploration baissent le moins | Le gain épistémique est une appréciation qualitative du modèle lui-même ; pas d'intervalles |
| 8 | 2611.25003 (18 nov.) | Échantillonnage divers par processus déterminantal | Programme (mesures automatiques) | Oui (mêmes réservoirs) | Borne KL en O(1/N) formalisée en Lean ; front étendu sur deux tâches, seulement la diversité sur GSM8K | La borne n'est calculable que sur une instance finie, pas sur le vrai modèle ; aucun lien avec l'idéation scientifique |
| 9 | 2611.19794 (15 nov.) | Goût de recherche par choix de direction future | Programme (choix de l'auteur) + pilote humain | Oui (température 0) | Alignement de 45,0 % à 67,5 %, divergence stable de 15,0 % à 36,2 % ; divergences robustes et partagées ; dérive vers le passage à l'échelle | 80 paires, 19 articles ; un seul modèle extrait, reformule et filtre |

---

## Lecture d'ensemble (six lignes)

1. Sur le **rapprochement de domaines qui ne se parlent pas**, aucun de ces neuf textes n'établit qu'une méthode fasse mieux qu'une invite ordinaire : l'opérateur de bisociation de CAR n'a pas d'effet survivant à la correction, et les carnets de distance de 2611.21408 montrent que les régions lointaines d'une carte ne contiennent ni le futur ni aucun texte cohérent.
2. Le seul élément sérieux en faveur du cas (a) est **expérimental et singulier** : la voie « éléments hors discipline » d'Abelio a produit une proposition d'ADN ancré sans précédent dans son domaine, qui a tenu au laboratoire — un cas, choisi par des humains parmi vingt-cinq rapports, avec un mécanisme partiellement faux sur l'autre proposition.
3. Sur les **idées qui découlent de travaux antérieurs**, le résultat le plus solide est négatif et réplique Tang et Yang : le modèle fait un pas systématiquement plus court que la littérature qui suit, et la critique allonge ce pas sans l'orienter mieux (la part de direction imputable à la consigne vaut au plus 0,34 à 0,70 de ce que fait un vrai titre révélé).
4. Ce que l'on sait faire marcher pour le cas (b), c'est **encoder la relation entre travaux, non les sélectionner** : à corpus fixe, le graphe d'évolution des théorèmes gagne 58 à 64 %, tandis que le choix des articles ne gagne rien (52 %, p = 0,89) ; mais le gain s'achète en plausibilité (32 %).
5. Deux textes disent que l'étape du jugement est elle-même défaillante : un modèle sait qu'une question est ouverte et ne le dit pas (jusqu'à 90 points d'écart), et les notes de nouveauté séparent mal le neuf du connu (aire sous la courbe 52 % contre 84 % pour le jugement direct) — donc toute boucle d'idéation étalonnée sur un juge-modèle de nouveauté est suspecte.
6. Enfin, la conclusion commune des ablations honnêtes de la semaine (2611.24887, 2611.25214, 2611.19108) est que **l'itération et la vérification portent le gain, les mécanismes conceptuels affichés le portent peu ou pas** ; ce qu'apportent ces derniers est de rendre la dérivation inspectable, ce que trois textes revendiquent explicitement comme résultat distinct de la qualité.

---

## Non vérifié

- Les annexes longues de 2611.21408 (48 pages), 2611.24887 (56 pages) et 2611.25003 (56 pages) n'ont pas été lues page à page, seulement par recherche ciblée sur les chiffres demandés. Les preuves formelles en Lean de 2611.25003 n'ont pas été relues.
- Les chiffres de l'ablation par sous-système d'Abelio (effets standardisés +0,22, −0,02, +2,88) sont lus sur la figure 2g, p. 8, et non sur un tableau ; les valeurs exactes des boîtes à moustaches des panneaux 2d à 2f ne sont pas disponibles en texte.
- Pour 2611.21847, la « Project Page » annoncée p. 1 n'a pas été consultée ; aucune URL de dépôt ne figure dans le corps du texte.
- Aucun des dépôts de code cités n'a été ouvert ni vérifié.
- Les figures 3 à 5 de 2611.23546 et les figures 3 et 4 de 2611.19794 ont été lues par leur texte extrait et par les tableaux correspondants ; quelques valeurs portées uniquement sur les graphiques n'ont pas été reprises.
