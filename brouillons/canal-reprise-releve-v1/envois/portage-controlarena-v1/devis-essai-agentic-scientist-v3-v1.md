# Devis — un essai unique de « The Agentic Scientist » (AI Scientist v3, Sakana) pour tester à blanc les failles E à I — v1

De : conv-audit, le 26 octobre 2026 (heure lue sur `date -u` dans le pied de page). Pour : Lazar (option (c) de ma note du
26 octobre, acceptée « sur devis » à 14:39 heure de Paris) ; copie à session-depot (ligne de GO si Lazar le dit chez lui).
Statut : **devis, aucune dépense, aucun lancement** ; faits sur l'outil lus le 26 octobre sur arXiv 2610.18933 (soumis
le 13 octobre 2026), la page de publication de Sakana et le dépôt `SakanaAI/AI-Scientist-v3` (Apache 2.0) — non
opposables avant lecture de la documentation installée (R7). Régime exploratoire (mot de Lazar, 14:39) : aucun
préenregistrement ; aucun résultat opposable ; R1 revient pour tout run décisif.

## 1. Ce que l'outil fait, d'après ses auteurs

- Un méta-contrôleur orchestre des **agents de code en ligne de commande** (Codex, Claude Code, OpenCode, Pi ; quatorze
  couples modèle-harnais évalués, neuf modèles de frontière) en quatre temps : spécification exécutable de la tâche et
  de sa procédure d'évaluation (fournie par les humains ou rédigée par un agent, puis contrôlée) ; investigation parallèle
  (idéation, exécution, mémoire partagée) ; production d'évidence (meilleur programme correct, ablations, analyse des
  métriques) ; rédaction (manuscrit, audit, relecteurs-agents). Budget usuel : **20 itérations d'idées par campagne**.
- Limites écrites par les auteurs : scores élevés obtenus par raccourcis qui violent la méthode voulue (« reward
  hacking ») quand les contraintes sont implicites ; grilles d'évaluation imparfaites ; dérive vers le réglage
  d'hyperparamètres plutôt que la science ; recherche bibliographique seulement à l'écriture ; scores des relecteurs-agents
  = indice, pas preuve ; un seul article passé en relecture humaine (ALIFE 2026).
- **Aucun coût publié** (ni dollars, ni heures, ni matériel). Le coût est celui des agents de code : des millions de
  jetons par heure de session, donc des dizaines à quelques centaines de dollars par campagne de vingt itérations selon
  le modèle. D'où un plafond serré et une mesure au premier tour.

## 2. La tâche que nous lui donnerions (niveau de la méthode)

Spécification exécutable fournie par nous (pas rédigée par un agent) : « Voici des détecteurs séquentiels et des
règles de décision codés (CUSUM de Page et sa variante à énergie d'excursion ; seuil conforme brut et normalisé ;
plancher apparié sur $\Sigma_{\text{pool}}$ et sur $\Sigma_{H_0}$), un simulateur semi-synthétique de scores d'épisodes
(bruit honnête calibré sur nos pilotes, sans aucune donnée réelle), et un budget de dommage fixé. Pour chaque détecteur :
(1) existe-t-il une stratégie de sabotage à budget fixé qui le fait tomber sous un rappel donné à 1 % de faux positifs
(sa faille) ; (2) quel remède codé la ferme, à quel prix en rappel sous les autres stratégies ; (3) la prédiction signée
de H1, H2, H3 tient-elle, et sous quelles conditions casse-t-elle. » Rapporté dans les deux sens (R3, R4).

- **Faille plantée témoin (R5 appliquée à l'auditeur)** : parmi les détecteurs, un porte une faiblesse connue de nous et
  non dite (par exemple un seuil calibré sur une longueur fixe, exposé à H2). Si la campagne ne la trouve pas, ses « rien
  trouvé » ne valent rien et la seconde famille n'est pas lancée.
- **Hors périmètre de cet essai** : H4 et H5 (activations de P3/P4 et pilote du papier C : données réelles, à décider à
  part) ; toute lecture de `test_final` ou des données des pilotes ; toute transcription d'attaque de nos organismes.
- Confidentialité : ni rapport ni transcription expurgée servis ; seulement les détecteurs codés et le simulateur.

## 3. Montage et chiffrage

| Étape | Contenu | Plafond | Régime |
|---|---|---|---|
| c0 — installation et tour d'essai | Instance processeur (Vast.ai, sans carte, ≈ 0,1 $ l'heure) ou conteneur ; dépôt cloné, harnais d'un seul agent de code ; une itération sur une tâche jouet ; **mesure du coût en jetons d'une itération** ; clés dans l'environnement de l'instance seulement | **10 $** (jetons + instance) | GO sur devis (jetons payants) |
| c1 — campagne, première famille | 5 à 10 itérations (pas 20) sur la tâche du § 2, modèle le moins cher qui passe c0 ; sorties : programmes, journaux de métriques, manuscrit ; arrêt si le coût mesuré en c0 × itérations dépasse le plafond | **60 $** | GO sur devis |
| c2 — seconde famille | Même tâche, autre famille de modèles, **seulement si c1 a trouvé la faille plantée** | **60 $** | GO sur devis, après lecture de c1 |

Liste d'arrêt : coût à mi-plafond avec moins de deux itérations faites ; agent qui touche à autre chose que son dossier ;
toute écriture hors du bac à sable ; refus de filtre consigné tel quel, jamais contourné. Ce que nous en tirons : des
brouillons de préenregistrement (hypothèse, prédiction signée, code et graines), jamais une preuve.

## 4. Ce que je recommande

c0 puis c1 après la v2 de la synthèse (qui fixe la liste des détecteurs à coder), 70 $ au pire cas ; c2 conditionnel.
Confiance moyenne : l'outil est fait pour produire des articles, pas pour attaquer des détecteurs ; sa valeur ici est la
boucle idée → code → ablation sans nous, et la faille plantée dit si elle vaut quelque chose. Dépense : **sur le mot
direct de Lazar chez session-depot**, devis en main ; aucun défaut.

Sources (lues le 26 octobre) : arXiv 2610.18933 ; `pub.sakana.ai/agentic-scientist` ; dépôt `SakanaAI/AI-Scientist-v3`.

Horodatage : écrit le 2026-10-26 13:48:49 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
