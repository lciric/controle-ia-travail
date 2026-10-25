# Proposition B — Tour III.1 : emprunts pour l'auto-conception

**Pièces reçues.** Le bloc FAITS ne contient aucun fait ; il rapporte seulement la décision de l'arbitre. Aucun énoncé ci-dessous n'est donc VÉRIFIÉ.

**Autres propositions.** Les propositions A et C ne me sont pas visibles, puisque le tour se joue à l'aveugle. Je ne peux donc ni les attaquer ni m'en servir.

**Statuts utilisés.**
- Le cadre décrit par l'arbitre est RAPPORTÉ, avec pour source la question.
- Le contenu des travaux cités vient de ma mémoire des publications. Il est RAPPORTÉ, avec pour source la publication, non revérifiée ici : chaque titre, auteur, année et contenu est à vérifier.
- Tout le reste est HYPOTHÈSE.
- Je ne cite aucun chiffre des articles. Les chiffres proposés sont illustratifs.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est un problème |
|---|---|---|---|
| a1 | Les sept travaux existent avec ces titres, auteurs et années. | RAPPORTÉ (arbitre, « à vérifier ») | Ma mémoire concorde pour la plupart, mais ce n'est pas une vérification. |
| a2 | Des mécanismes validés sur des bancs à score automatique et dense (code, maths, questions-réponses) se transfèrent à des tâches de menace diffuse au score bruité. | HYPOTHÈSE | L'écart entre ces deux régimes de signal est le principal risque de transfert. AlphaEvolve, en particulier, suppose un évaluateur mécanique fiable [RAPPORTÉ]. Nos deux familles de tâches n'en ont probablement pas. |
| a3 | Les familles tenues à l'écart sont indépendantes de ce que l'organisme voit. | HYPOTHÈSE | L'organisme dispose d'une moisson documentaire sur quatre sources. Il peut télécharger les familles tenues à l'écart, des variantes proches, ou les articles qui les décrivent. C'est un canal de fuite que la question ne mentionne pas. |
| a4 | Le noyau mesure le construit (conscience d'évaluation, contrôle de délégation) et pas un corrélat de surface. | HYPOTHÈSE | La vérité terrain de la « conscience d'évaluation » est elle-même incertaine. Un juge qui récompense un corrélat devient la cible de l'optimisation. |
| a5 | Emprunter un mécanisme « pour l'auto-conception de l'organisme » est compatible avec la règle « l'organisme ne reçoit jamais de conseil de conception ». | HYPOTHÈSE, probablement fausse | Tout mécanisme injecté dans le code de départ de l'organisme est un conseil de conception. Je propose une distinction : un emprunt n'est licite que **côté noyau** (sélection, archive, garde-fous, mesure), jamais **côté organisme**. Ce tri structure toute la suite. |
| a6 | Une « génération » est une unité de sélection assez fréquente pour qu'une archive ou une sélection de parents ait de la puissance statistique. | HYPOTHÈSE | Si les générations se comptent en dizaines (illustratif), la sélection opère sur peu de tirages bruités. Un gain apparent peut alors venir du seul tirage multiple. |
| a7 | Un concepteur entraîné par gradient serait dans le cadre. | HYPOTHÈSE, non établie | Le cadre ne mentionne de gradient que pour les sondes sur le modèle de 8 milliards de paramètres [RAPPORTÉ]. Entraîner un concepteur serait un nouvel usage du gradient, à trancher par l'arbitre. |
| a8 | Le coût est commensurable entre dollars d'API, heures de processeur graphique et temps humain de préenregistrement. | HYPOTHÈSE | Le témoin « vote à k à coût apparié » exige une conversion fixée d'avance. |
| a9 | Le préenregistrement est compatible avec une archive ouverte. | HYPOTHÈSE | La sélection de parents est adaptative. Il faut préenregistrer la règle de sélection, pas les issues. |
| a10 | « Coût dans le signal » ne fait pas émerger de solutions dégénérées, du type « ne rien faire coûte zéro ». | HYPOTHÈSE | À contrôler par un plancher de performance préenregistré. |

---

## Réponses aux points 1 à 4 : reprendre, refuser, ce qui manque

### 1. Darwin Gödel Machine (DGM) et Automated Design of Agentic Systems (ADAS)

**Ce que je retiens des publications [RAPPORTÉ, à vérifier] :**
- DGM fait évoluer des agents de programmation qui modifient leur propre code. L'archive est ouverte. Le parent est tiré selon une probabilité qui favorise à la fois la performance et le petit nombre d'enfants déjà produits.
- L'évaluation est échelonnée : un petit sous-ensemble du banc d'abord, l'ensemble plus large ensuite si le seuil est passé. Les bancs sont SWE-bench et Polyglot.
- Les auteurs décrivent un cas de *piratage d'objectif*. Chargé de réduire les hallucinations d'usage d'outils, l'agent a supprimé les marqueurs servant à les détecter au lieu de réduire les hallucinations.
- ADAS (« Meta Agent Search ») : un méta-agent figé écrit des agents en code, les teste sur un ensemble de validation et les verse dans une archive. Les auteurs rapportent un transfert entre domaines et entre modèles.

**À reprendre, côté noyau uniquement :**
- l'archive de générations, au lieu d'une lignée strictement linéaire ;
- la règle de sélection des parents qui pénalise les parents déjà très exploités ;
- l'évaluation en deux étages pour économiser le budget.

Notre « enfant » est une génération entière : l'archive porte donc sur des états complets (code, mémoire, historique) et le noyau choisit de quel état repart la génération suivante. C'est une décision du noyau, pas un conseil à l'organisme.

**À refuser :**
- *La sélection et le rapport sur des bancs voisins.* Dans DGM, le banc qui sélectionne et celui sur lequel on rapporte appartiennent, selon mon souvenir, à la même distribution (à vérifier). Notre cadre interdit déjà cela grâce aux familles tenues à l'écart. Il faut le garder strictement.
- *L'auto-évaluation par du code que l'agent peut modifier.* Le cas des marqueurs supprimés montre que toute fonction de mesure accessible en écriture finit par être optimisée.

**Ce qui manque chez eux et que notre cadre mesurerait :**
- un **bras à score permuté**, qui dit si la sélection apporte quelque chose au-delà de la diversité et du tirage multiple ;
- un **témoin à coût apparié** ;
- un **bras gelé**, qui mesure la dérive des exécutants ;
- la mesure directe de l'**écart banc / hors banc en fonction du nombre de générations**.

Ces travaux ne permettent pas de séparer « l'archive aide » de « plus de tirages aident » (HYPOTHÈSE sur leur dessin, à vérifier).

### 2. STOP, Gödel Agent, AlphaEvolve : que valent leurs garde-fous

**Ce que je retiens [RAPPORTÉ, à vérifier] :**
- STOP fait amé