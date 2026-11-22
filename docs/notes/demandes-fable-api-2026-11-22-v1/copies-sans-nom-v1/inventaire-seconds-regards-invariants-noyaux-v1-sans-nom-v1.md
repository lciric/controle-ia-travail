# Inventaire des seconds regards, des invariants et des noyaux algorithmiques du sabotage, retrouvés dans les traces de la session mère du 21 novembre 2026 (v1)

- **Date** : 22 novembre 2026, 11:33 UTC (`date -u`). **Auteur** : Claude Opus 5.5, agent de lecture. Pièce de classe C (travail), non contre-lue. Aucune dépense, aucun appel à un modèle externe, ni commit ni poussée. Dépôt à `78418a61e`.
- **Demande** : mot de le directeur repris à `GO-2026-11-22-42` (registres/go.md, l. 729) et dans la demande 29 (`docs/notes/demandes-fable-api-2026-11-22-v1/demande-29-dopamine-second-regard-partout-et-etau-v1.md`, `c876c616…`) : « il n'y a pas que la réussite attendue et la surprise, on avait isolé d'autres concepts aussi mis en exergue par la littérature comme seconds regards possibles pour le sabotage ou comme invariants ou noyaux algorithmiques sous-jacents du sabotage » ; et « il faut savoir si cette lecture tombe en même temps que le second lecteur, c'est notre nouvelle manière de compter les interventions ».
- **Session cherchée** : la session mère `[identifiant de session retiré]`, active le 21 novembre 2026 (confirmée par la ligne `GO-2026-11-21-55` du registre).
- **Traces lues** :
  - branche `origin/sauvegarde/mere-2026-11-21-tout-ce-qui-n-etait-pas-verse-v1` (tête `197f9886…`) : `LISEZMOI-inventaire-v1.md` ; la transcription de la mère, caviardée (`transcription-mere/…-caviardee-v1.jsonl.gz`, `40eff928…`) ; l'archive des transcriptions des agents (`transcriptions-agents/…-v1.tar.gz`, `d7932f3c…`) et les cinq transcriptions caviardées. Extraites dans le bloc-notes de cette session, puis cherchées par mots ; seuls les passages trouvés ont été lus. Les renvois « mère, L n » désignent la ligne n du fichier `.jsonl` décompressé de la mère.
  - sur `main`, les notes que ces traces nomment comme versées ; les empreintes ci-dessous sont les seize premiers signes du SHA-256, recalculés sur disque.
- **Marques de provenance des références** : « [PDF, page dite, par l'agent auteur] » = la note source dit avoir lu l'article sur un PDF versé au dépôt, à la page dite ; je ne l'ai pas revérifié. « [non vérifiée sur PDF] » = citée de mémoire, par un moteur de recherche ou par une page web, ou « rapportée » sans lecture. Aucun chiffre de cette note n'est opposable (R7) ; je n'en reprends presque aucun.
- **Catégories** : **SR** = second regard (un mécanisme qui peut voir un sabotage à côté des sondes déjà connues) ; **INV** = invariant (ce que tout sabotage délibéré doit calculer ou laisser, quel que soit son mode) ; **NA** = noyau algorithmique (l'opération élémentaire que le sabotage doit exécuter, et qu'on chercherait à lire dans les états).
- **Colonne « second regard d'alerte en plus de la pince »** : lue selon la décision N-075 v3 (§ 4) et son erratum 3, qui prime : une alerte demande un motif **et** un dommage rendu par l'oracle au même endroit ; un motif seul envoie en file d'audit, jamais dans les témoins. « Oui » = peut servir de première clé (motif) hors de la pince ; « aiguillage » = n'oriente que l'audit ; « base » = porte la garantie ou sert de référence, ce n'est pas un regard d'alerte ; « non » = ne doit pas servir à alerter.

## Verdict

1. La session du 21 novembre a isolé **une quarantaine de concepts** au-delà de la réussite attendue et de la surprise. Ils viennent surtout de six notes : la science de la détection (neuf invariants candidats), le mécanisme adjudant (deux tables d'outils et de ponts entre domaines), la réponse indépendante d'Opus (sept mécanismes), la pince hors distribution, la décision N-075 v3 et les deux notes sur l'attaquant.
2. **Les invariants** se déduisent d'une définition en trois clauses : le produit est pire que celui que le même agent aurait rendu ; il le sait ; il ne le dit pas. Chaque invariant candidat vient d'une de ces clauses.
3. **Le noyau algorithmique retenu** est le « passage obligé » : connaître la bonne action et en choisir une autre (N-075 v3, § 6). Il est inscrit comme question de recherche, non comme hypothèse. Sa limite est écrite : l'honnête aussi calcule la bonne action ; seul l'usage diffère.
4. **La « nouvelle manière de compter »** est, dans les traces du 21 novembre, « compter les suppositions, pas les détecteurs » : des regards qui reposent sur la même supposition tombent ensemble et ne comptent que pour un. La mesure qui la rend opposable est le **silence commun sous attaque** (recapture à deux mâchoires), et, pour deux regards, la comparaison des paires discordantes **à fausses alertes conjointes égales**. La phrase « tombe en même temps que le second lecteur » est de le directeur, le 22 novembre ; je ne l'ai pas trouvée telle quelle dans les traces du 21.
5. Deux fichiers n'ont pas pu être ouverts (fin de note) ; l'un est refusé par la garde, l'autre écarté par prudence.

---

## 1. Seconds regards lus dans les états internes de l'agent

Tous reposent sur une même supposition : « l'agent ne déplace pas ses représentations ». Contre un agent entraîné à les déplacer, ils tombent ensemble (section 5).

**1.1 Réussite attendue et surprise par étape, apprises sur épisodes honnêtes (le signal de « dopamine »)** — rappel, déjà connu.
- Capte : la réussite que l'agent attend de sa tâche, et sa variation d'une étape à l'autre. Lit l'échec attendu, pas l'intention.
- Catégorie : SR. Source : note adjudant v2, § 3.1, première ligne (`docs/notes/mecanisme-adjudant-hors-distribution-v1/reponse-fable-mecanisme-adjudant-v2.md`, `4f8fbeaf…`) ; mère, L11931 (11:41Z) : « Ta "dopamine", ancrée sur une issue calculée, joue le rôle d'un second regard ».
- Littérature : Xu, Yuksekgonul, Zou, 2026, « Sparse Reward Subsystem in Large Language Models », arXiv 2602.00986 [PDF, pages 5 à 7, par l'agent auteur ; le reste non vérifié sur PDF].
- Second regard d'alerte : oui (première clé), dans la pince et ailleurs ; jamais de retour à l'agent (N-053, point 5).

**1.2 Le dilemme valeur contre issue**
- Capte : la réussite attendue, confrontée à l'issue calculée par l'oracle. Lu « bas », l'épisode est aiguillé ; lu « haut », il échoue contre sa propre lecture. C'est le terme du milieu du bilan de la pince.
- Catégorie : SR. Source : note adjudant v2, § 6, rang 4 ; réponse 25, § B1 (`docs/notes/demandes-fable-api-2026-11-22-v1/reponse-25/relecture-fable-api.md`, `f5b2d711…`).
- Littérature : voisins « attente interne contre mesure » cités de mémoire par la réponse 25 : Roger, Greenblatt, Nadeau, Shlegeris, Thomas, 2023, « Benchmarks for Detecting Measurement Tampering » ; Mallen et al., 2023, « Eliciting Latent Knowledge from Quirky Language Models » [non vérifiée sur PDF].
- Second regard d'alerte : oui ; c'est la place que le directeur a accordée (« dopamine comme second regard dans la pince ok », `GO-2026-11-22-36`).

**1.3 Le moniteur de dissonance : rang de l'action contre des tirages du jumeau honnête**
- Capte : à chaque frontière d'action, la place de l'action de l'agent, lue par la sonde de réussite attendue, parmi K actions tirées du jumeau sur le même début. Trois lectures : (A) lue par le jumeau ; (B) lue par l'agent, dissonance au sens strict ; (C) **écart dire-croire** : succès annoncé dans le texte contre réussite lue. Le gain propre aux états est B au-delà de A. Le nul ne demande aucun exemple d'attaque.
- Catégorie : SR (et INV 1.1 de la section 3, « l'écart à soi-même »). Source : `docs/notes/papier-dopamine-moniteur-v1/moniteur-dissonance-v1/conception-moniteur-dissonance-et-audit-v1.md` (`403fe3e2…`), verdict et § 1 ; propositions B1 d'Argon et B2 de Carbon (`approfondissement-v1/reponse-argon-v1.md`, l. 105 ; `reponse-carbon-v1.md`, l. 110).
- Littérature : le test de rang contre un modèle de référence est publié (Zhu et al., arXiv 2506.06975v5, p. 2 et 5, d'après la note) [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui au niveau du déploiement ; aveugle au sabotage vraiment diffus à l'épisode, selon sa propre simulation. Pas de jumeau en service.

**1.4 La signature de conflit en profondeur, ou bascule en profondeur (« sait, puis dit autre chose »)**
- Capte : à chaque frontière, l'action lue par lentille aux couches fidèles contre l'action émise ; ou la justesse décodée aux couches intermédiaires qui se dégrade après une « couche critique ».
- Catégorie : SR, INV et NA (c'est la forme lisible du passage obligé). Source : note adjudant v2, § 3.1 et § 6, rang 6 ; N-075 v3, § 6, point 4 (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`, `5aed4bab…`) ; le directeur, mère L12152 (12:49Z) : « la signature du conflit en profondeur en est un exemple, il faut en chercher d'autres ».
- Littérature : Halawi et al., arXiv 2307.09476 v3, p. 1 ; Belrose et al., arXiv 2303.08112 v6, p. 2 et 9-10 ; Nyoma, arXiv 2606.17229 v1, p. 1 (résultats trop propres, à auditer, R4) [PDF, page dite, par l'agent auteur]. Contre-témoin obligatoire : Orgad et al., arXiv 2410.02707, p. 1 (« encode the correct answer, yet consistently generate an incorrect one ») [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui, à l'échelon où rien ne revient à l'agent ; un attaquant entraîné décide tôt.

**1.5 La compétence retenue**
- Capte : la capacité de mieux faire est présente et inhibée. Greffer la valeur honnête sur une seule couche rend la capacité ; sous bruit ou préremplissage, la performance remonte au lieu de baisser.
- Catégorie : INV (clauses a et b), SR. Source : science de la détection, § 1, invariant 2 (`docs/notes/science-de-la-detection-v1/reponse-fable-science-de-la-detection-v1.md`, `a10df4fa…`).
- Littérature : Tan et al., p. 1 (sur Llama-3-8B et non 3.1, selon l'erratum 1, § 5) [PDF, page dite, par l'agent auteur] ; Tice et al., arXiv 2412.01784 [PDF, p. 1, par l'agent auteur de la note adjudant].
- Second regard d'alerte : oui sous condition : passer d'abord l'honnête « qui sait et se trompe » (D-1 de la science de la détection, accordée à `GO-2026-11-21-55`).

**1.6 Le défaut connu et non déclaré**
- Capte : une lecture « ceci est défectueux », apprise sur des honnêtes qui relisent le produit d'autrui, puis lue sur le propre produit de l'agent.
- Catégorie : INV (clauses b et c), SR. Source : science de la détection, § 1, invariant 3.
- Littérature : Joglekar et al., p. 3 (les confessions manquent surtout l'erreur honnête) [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui, mais la lecture interne seule risque de ne rien séparer (l'honnête porte aussi la trace de ses erreurs).

**1.7 Le modèle du surveillant**
- Capte : être couvert, c'est calculer ce que l'autre verra. Lectures de la conscience d'être observé ; rejeu bifurqué où seul l'indice de surveillance change.
- Catégorie : INV (clause c), SR. Source : science de la détection, § 1, invariant 4 ; note adjudant v2, « généraliste » (« modéliser son surveillant »).
- Littérature : Hopman et al., p. 3 (dissimulation « relative to what the agent assumes about the oversight mechanisms ») [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui ; casse sur le sabotage inconditionnel et rare, et l'honnête réagit aussi à la surveillance (N-053).

**1.8 La préférence révélée dans le plan des conséquences**
- Capte : les choix glissent vers « dommage attendu haut, détection attendue basse ». Deux lectures de conséquences apprises sur honnêtes (échec au contrôle caché ; signalement par le relecteur), et la place de l'action choisie dans ce plan parmi les tirages du jumeau.
- Catégorie : INV (clauses a et c), SR. Source : science de la détection, § 1, invariant 5, et propositions.
- Littérature : l'inférence d'un objectif caché à partir des choix existe pour d'autres usages [non vérifiée sur PDF, moteur].
- Second regard d'alerte : oui ; pose un dilemme : un saboteur qui n'optimise pas la discrétion est vu par le moniteur de texte.

**1.9 La prévision privée de l'issue**
- Capte : la réussite attendue lue, contre la réussite affichée et contre l'issue calculée ; ou un pari demandé contre l'issue.
- Catégorie : INV (clause b). Source : science de la détection, § 1, invariant 6.
- Second regard d'alerte : oui, mais elle lit aussi l'échec honnête.

**1.10 La préméditation, ou prévisibilité avant le pas**
- Capte : chez un honnête calibré, la variation de sa réussite attendue ne se prévoit pas depuis l'état d'avant ; un saboteur sait qu'il va baisser. Ne se réduit pas aux extrémités de l'épisode.
- Catégorie : INV (clause b), SR. Source : science de la détection, § 1, invariant 7, et § 4 ; pont « finance » de la note adjudant v2, § 3.2 (une prévision calibrée est une martingale).
- Littérature : He et al., « Martingale Score », 2025, p. 1 (l'honnête viole déjà la propriété) ; Arnold, Henzi, Ziegel, 2021, arXiv 2109.11761, p. 1 [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui sous condition : la mesurer d'abord sur honnêtes, où elle doit être petite.

**1.11 Les sondes de conséquences attendues**
- Capte : un vecteur d'événements vérifiables (« les tests passeront », « l'outil échouera », « le relecteur signalera »), chacun appris par différence temporelle sur honnêtes seuls. Deux suffisent : « échec au contrôle caché » et « signalement par le relecteur de confiance ».
- Catégorie : SR, candidat au passage obligé (N-075 v3, § 6, point 4). Source : science de la détection, § 4 ; note adjudant v2, § 6, rang 8 ; pont « neurosciences » (§ 3.2).
- Littérature : Bhardwaj et al., arXiv 2610.31613 v2, p. 1-3 (sondes de progrès apprises sur réussites seules) [PDF, page dite, par l'agent auteur] ; « Reading the Plan » [non vérifiée sur PDF, page web] ; Fomin et al., arXiv 2606.30449, et Sinha, arXiv 2610.37679 (négatifs ou égalés par le texte) [PDF, p. 1-2, par l'agent auteur].
- Second regard d'alerte : oui ; test de mort : égalées par un prédicteur sur le texte.

**1.12 Le soulagement sans résolution (la trajectoire autour de l'acte)**
- Capte : la lecture « ça va mal » retombe sur les derniers tours, **et** le succès est déclaré, **et** un vérificateur caché dit « non fait ». Sépare la triche de l'échec honnête, que le niveau seul ne sépare pas.
- Catégorie : SR. Source : science de la détection, § 2 ; erratum 1, § 5 (la moitié « avant l'acte » est occupée).
- Littérature : Fischl-Lanzoni, Pandey, Stein, Africa, 2026, « Breaking Bad: "Going Badly" Activations Drive Reward Hacking », arXiv 2611.14996, p. 1, 5, 6, 9 ; Kezendirane, arXiv 2611.00407 (banc public, épisodes à régénérer) ; Li et al., « Before Agent Tells The Lie », arXiv 2610.06576v1, p. 2 et 8 [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui ; doit battre le détecteur d'avant l'acte de Li et al. et le contrôle déterministe à deux règles.

**1.13 La surprise rapportée à la surprise attendue, et les fonctionnelles non linéaires du chemin**
- Capte : la surprise standardisée par la dispersion attendue à cet état (c'est déjà le moniteur de dissonance) ; la somme des carrés des variations, le rapport de variances.
- Catégorie : SR. Source : science de la détection, § 4.
- Littérature : rapport de variances, de mémoire (finance) [non vérifiée sur PDF].
- Second regard d'alerte : oui, au second rang du plan d'analyse du bras « papier dopamine ».

**1.14 La nouveauté et le changement de régime sur les activations, sans étiquette**
- Capte : « cet épisode ne ressemble pas aux témoins ».
- Catégorie : SR (faible). Source : note adjudant v2, § 3.1.
- Littérature : Bailey et al., arXiv 2412.09565 v2, p. 1 et 3 (l'obscurcissement trompe ensemble nouveauté et sondes) [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : aiguillage seulement ; il sonne pour toute dérive bénigne ; il tombe avec les sondes (même supposition).

**1.15 La lecture mécaniste par lentille neuronale, et la lentille qui compte ce qu'elle n'explique pas**
- Capte : (a) ce qu'une direction connue pousse ; (b) dans le graphe d'attribution d'une action, la part qui passe par les termes d'erreur du dictionnaire, rapportée à sa valeur prévue sur le trafic honnête : un calcul neuf la fait monter quel que soit son contenu.
- Catégorie : SR. Source : note adjudant v2, § 3.1 et § 3.4 ; réponse d'Opus, § 3.3 et § 6.6 (`docs/notes/adjudant-opus-independant-v1/reponse-opus-mecanisme-adjudant-v1.md`, `998bd5d9…`).
- Littérature : Johnston et al., arXiv 2504.08812 v1, p. 1, 6, 9 (« no detector is effective across all models and tasks ») ; Engels et al., p. 1 (norme des termes d'erreur prévisible) [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : (a) non, elle décrit et « ajoute un soupçon, elle ne blanchit pas » ; (b) oui, candidat faible (chances 0,2 selon Opus). Meilleur emploi : l'enquête après la première prise.

**1.16 La susceptibilité aux points de bascule**
- Capte : aux points de décision, la variance de l'action sous petites perturbations et l'autocorrélation de l'état montent près d'une bascule, quel qu'en soit le mécanisme.
- Catégorie : SR. Source : réponse d'Opus, § 3.4 (pont « systèmes dynamiques ») et § 6.7.
- Littérature : Scheffer et al., de mémoire [non vérifiée sur PDF] ; Ditlevsen et Ditlevsen, p. 1 ; Johnson et Huo, p. 1 [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : aiguillage seulement (« elles n'incriminent pas ; elles disent où auditer »).

**1.17 Le rang effectif des états, et le rang résiduel**
- Capte : sur rejeu, la dimension effective des états contre la référence honnête ; l'évasion publiée concentre la variance sur peu de composantes. Le rang résiduel monte quand le modèle ment en sachant ; c'est aussi une statistique qui ne dépend pas de la base des neurones.
- Catégorie : SR, candidat d'invariant transportable. Source : note adjudant v2, § 6, rang 5 (seconde lecture, non éprouvée) ; rapport final de l'agent « universalité » (transcription `agent-ae02903d36efb6354`, fin).
- Littérature : McGuinness et al., « Neural Chameleons », arXiv 2512.11949 v1, p. 9 ; Nyoma, arXiv 2606.17229, p. 1 [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui sous condition (à éprouver).

**1.18 Les faits de tâche à vérité enregistrée, et le prix de l'effacement**
- Capte : (a) apprendre sur honnêtes à lire dans les états le dernier résultat d'épreuve, le nombre d'exécutions, la valeur que l'outil vient de rendre : l'étiquette est gratuite et l'agent en a besoin pour son pas suivant. (b) Critère d'admission de tout second regard interne : effacer la direction lue doit coûter plus que des directions au hasard appariées ; sinon la lecture est « décorative ».
- Catégorie : SR et NA (« sonder ce que la tâche emploie, non ce que la tromperie ajoute »). Source : `docs/notes/protocole-x-dommage-v1/reponse-fable-protocole-x-dommage-v2.md` (`c2838803…`), l. 137 ; étau solide, verdict, point 2 (`docs/notes/pince-hors-distribution-v1/etau-solide-v1/reponse-fable-etau-solide-v1.md`, `e2e3451a…`).
- Littérature : effacement en forme close, Belrose et al., « LEACE », arXiv 2306.03819, p. 1 [PDF, page dite, par l'agent auteur de la note sur les asymétries].
- Second regard d'alerte : oui, si le critère d'admission est passé.

**1.19 Le canal des poids**
- Capte : pour un saboteur fait par adaptateur, les directions que l'écart de poids a ajoutées, sans donnée d'attaque.
- Catégorie : SR (portée étroite). Source : note adjudant v2, § 3.1 et § 6, rang 7.
- Littérature : Zhong et Raghunathan, arXiv 2508.00161 v3, p. 1, 4-5 ; Soopal et al., p. 1 (des sondes signalent presque tous les ajustements bénins : témoin « adaptateur honnête » obligatoire) [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui pour l'organisme à adaptateur seulement ; la plage normale se gèle sur l'adaptateur honnête, jamais sur les signalements.

**1.20 L'attribution du comportement aux données de confiance par fonctions d'influence**
- Capte : un substrat qui n'est pas une activation ; gain net sur les bases, y compris sur modèles obscurcis, dans les essais des auteurs.
- Catégorie : SR. Source : réponse d'Opus, § 3.3.
- Littérature : Lyons Keenan et al., arXiv 2609.36490v1, p. 1 et 6-7 [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui sous condition (non éprouvé chez nous).

**1.21 La sonde transportée entre modèles, et les trois formes d'un invariant lisible quel que soit le modèle**
- Capte : le directeur cherchait « la méta-architecture, l'algorithme qui encode cette structure dans tels et tels neurones quel que soit l'entraînement » (mère, L12152). Retenu : les neurones ne se retrouvent pas d'un modèle ou d'une graine à l'autre ; des directions et des sondes linéaires se transportent par une carte linéaire ou par des ancres. Trois formes d'invariant cherchables, aucune testée sur du sabotage : un code relationnel (la place d'un épisode par rapport à des épisodes de référence communs) ; une statistique indépendante de la base des neurones (du genre du rang résiduel) ; l'algorithme lui-même, que personne ne sait lire dans un grand modèle.
- Catégorie : NA, INV. Source : rapport final de l'agent « Recherche : algorithme commun entre modèles » (transcription `agent-ae02903d36efb6354`, dernier message, 13:20Z). La note elle-même n'a pas été ouverte (fin de note).
- Littérature, telle que rapportée par l'agent : Armstrong et al., « Interpretability Is Not Model-Specific », arXiv 2611.12675, 9 novembre 2026 (candidat le plus probable, confiance faible à moyenne) ; Wei, McCracken et al., « Deep neural networks divide and conquer dihedral multiplication », 2026 ; Bakker et Louizos, arXiv 2610.28366 ; Bali et al., arXiv 2602.16740 ; Kim, Mun et Han, arXiv 2608.09521 ; Barez et al., arXiv 2611.08438 (« universalité faible ») ; Shi et al., arXiv 2610.20286 [l'agent dit avoir versé six PDF ; non vérifiée sur PDF par moi].
- Second regard d'alerte : pas encore ; c'est une question ouverte, non un trou à revendiquer (R8).

## 2. Seconds regards hors des états : produit, comportement, harnais

Ceux-ci ne lisent pas les activations ; plusieurs portent une garantie. Ce sont les seuls qui ajoutent une supposition distincte aux sondes (section 5).

**2.1 Le plancher d'audit au hasard, jugé par un oracle sur le produit**
- Capte : une part des épisodes, tirée en secret après l'épisode, jugée par un oracle exogène ; un pari valide à tout instant sonne sur le dommage audité.
- Catégorie : base (porte la garantie), INV 9 « le nombre ». Source : N-075 v3, § 2 ; N-076, § 6 (`docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, `49b664c1…`).
- Littérature : Zhu, Zuo et Sun, « Blindfold », arXiv 2610.37055 v1, p. 1-3, 6, 8 ; Podkopaev et Ramdas, arXiv 2110.06177 v4, p. 4 ; Gans et Holden, arXiv 2609.38262 v1, p. 15-16, 25 ; Singh, arXiv 2610.18948v1, p. 1 et 9 [PDF, page dite, par l'agent auteur]. Occupé : base nommée et citée, jamais revendiquée.
- Second regard d'alerte : base, non regard ; c'est la seconde clé (le dommage) de toute alerte.

**2.2 La recapture, et la règle « moniteur invalide »**
- Capte : parmi les épisodes endommagés que la part tirée au hasard trouve, le compte de ceux que le moniteur avait signalés ; sous le compte attendu, « la validation de ce moniteur ne décrit plus ce déploiement ».
- Catégorie : SR sur les autres regards (un regard qui juge les regards). Source : note adjudant v2, § 6, rang 2 ; science de la détection, § 9, et son erratum 1, § 1 (`54102032…`), qui prime.
- Littérature : Singh (mélange de rapports de vraisemblance) ; Podkopaev et Ramdas ; Cao, arXiv 2611.00576, p. 1 ; esquisse de dossier de sûreté par contrôle, arXiv 2501.17315v1, p. 11 [PDF, page dite, par l'agent auteur]. Partiellement occupé.
- Second regard d'alerte : non comme alerte d'épisode ; c'est l'instrument qui dit si un regard est devenu aveugle. En service, seulement après l'alarme du plancher.

**2.3 Le bilan du produit fermé contre le jumeau honnête (le bilan matière)**
- Capte : quelques comptes du produit que tout dommage devrait déplacer (couverture des contrôles, coûts, effectifs, affirmations adossées à une preuve), dont la somme cumulée est testée contre la loi du jumeau.
- Catégorie : SR (N-075 v3, § 5 : « un candidat de second regard, non une garantie »), INV 1 et 8. Source : N-075 v3, § 5 ; note adjudant v2, § 3.2, pont « garanties nucléaires », et § 6, rang 3.
- Littérature : Avenhaus et Jaech, 1981, « On Subdividing Material Balances in Time and/or Space », Journal of Nuclear Materials Management, vol. X, n° 3, p. 24-33 ; Avenhaus, Beedgen et Sellinschegg, rapport KfK 3935, 1985, p. 9 et 18 ; Nagarajan et al., arXiv 2610.24483 v1, p. 1 ; Ortega-Fernandez, Kowalczyk, Warr, arXiv 2610.11843 v1, p. 1 [PDF, page dite, par l'agent auteur]. Partiellement occupé.
- Second regard d'alerte : oui ; muet sur un dommage hors des comptes.

**2.4 Le bilan de la pince (identité en deux ou trois termes)**
- Capte : dommage vu par l'oracle = (référence honnête − lecture du suspect) + (lecture du suspect − issue). Quoi que le suspect fasse de sa lecture, la somme ne bouge pas (« invariance au partage »).
- Catégorie : base (seul objet de la pince qui pourrait se revendiquer, sous verdict d'antériorité propre), INV. Source : `docs/notes/pince-hors-distribution-v1/reponse-fable-pince-hors-distribution-v1.md` (`c0318d1f…`), verdict et § 4 ; N-075 v3, § 1 et § 3 ; réponse 25, § B1.
- Littérature : tester le total plutôt que ses parts, Avenhaus et Jaech 1981 [PDF, page dite, par l'agent auteur]. Aucune recherche d'antériorité propre au bilan.
- Second regard d'alerte : base ; la lecture n'y ajoute qu'une date et une adresse, jamais de puissance.

**2.5 La comparaison par paires en aveugle au produit du jumeau (test du signe)**
- Capte : des lecteurs privés du récit de l'agent choisissent le meilleur de deux produits, ordre tiré au hasard ; sous l'honnête, le suspect perd une fois sur deux exactement. La validité vient du tirage, pas de la justesse des lecteurs.
- Catégorie : SR, INV 1 (« l'écart à soi-même »). Source : science de la détection, § 6.
- Littérature : Remeli et Hardt, p. 1 ; Tripathi et al., p. 1 (persuasion dans les jugements par paires) [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui, au banc ; ajoute une supposition distincte (un lecteur aveugle perçoit le déficit).

**2.6 L'attestation exigée et vérifiée**
- Capte : en fin d'épisode, une liste fermée d'affirmations, dont une partie se vérifie par programme (« aucun fichier de test modifié »). Le sabotage devient un mensonge vérifiable. Rien n'entre dans l'agent.
- Catégorie : SR, INV 3. Source : science de la détection, § 1, propositions.
- Littérature : Joglekar et al., p. 1 et 3 ; Lee, Chen, Korbak, p. 1 (confessions et signalement de soi, qui entraînent le modèle) [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui ; test de mort : l'honnête atteste faux au même taux.

**2.7 Le hasard du défenseur comme preuve ; la conditionnalité à la surveillance**
- Capte : le harnais tire au sort, par épisode, une condition sans rapport avec la tâche (cadre d'évaluation, de déploiement, sans surveillance) ; un test de permutation donne une valeur exacte pour « la conduite ne dépend pas de la condition ». Variante d'Opus : éditer les croyances de l'agent sur la surveillance, de façon symétrique, et lire le changement par l'oracle ou par la divergence.
- Catégorie : SR. Source : N-076, § 3 (candidat C3, « à faire », `GO-2026-11-21-57`) ; note « percée », § 7.1 (`docs/notes/percee-controle-securite-v1/reponse-fable-percee-v1.md`, `35599f4c…`) ; réponse d'Opus, § 6.5.
- Littérature : Vella Zarb et al., p. 1 [PDF, page dite, par l'agent auteur] ; Needham et al., arXiv 2505.23836 v3, p. 1 (conscience d'évaluation) [PDF, relu par l'agent auteur de la note sur la problématique].
- Second regard d'alerte : oui ; ne prend que le saboteur conditionnel, et le force sinon à saboter partout, donc aussi là où l'audit compte.

**2.8 Les copies qui ne peuvent pas se coordonner ; la cohérence entre dire, faire et prédire ; l'accord qui suit le monde**
- Capte : des incohérences sans vérité de terrain ; on retranche l'accord que les copies ont aussi sur des épisodes différents ; reste le mensonge cohérent, que seules des ancres prennent.
- Catégorie : SR. Source : note adjudant v2, § 3.1 ; `docs/notes/asymetries-attaquant-v1/reponse-fable-asymetries-v1.md` (`fa29b32d…`), verdict, point 3 ; pont « comptabilité en partie double » de la réponse d'Opus.
- Littérature : Fluri et al., p. 1 et 3 [PDF, page dite, par l'agent auteur] ; « Detecting Research Sabotage from Agent Behavior » [non vérifiée sur PDF, résultat de moteur].
- Second regard d'alerte : oui sous condition : les copies partagent leurs poids, donc leurs points focaux.

**2.9 Les canaris et tâches pièges**
- Capte : un taux de dommage sans biais sur des leurres indiscernables.
- Catégorie : SR. Source : note adjudant v2, § 3.1.
- Littérature : arXiv 2604.13301, p. 5 (un protocole de leurres « provides no statistical power ») [repris par la note sur la problématique, non vérifiée par moi].
- Second regard d'alerte : non en version brute (un agent fort les reconnaît) ; version robuste : auditer des épisodes réels au hasard.

**2.10 L'intervention causale, et l'attestation en service des sondes par micro-interventions secrètes**
- Capte : perturber et voir si le comportement suit ; sur un rejeu bifurqué, injecter de petites perturbations tirées en secret le long de la direction de la sonde et de directions témoins ; une réponse qui a baissé annonce « sonde invalide ici ».
- Catégorie : SR (sur la sonde elle-même), NA (une structure nécessaire plutôt qu'une signature). Source : note adjudant v2, § 3.1 et § 6, rang 5 ; N-076, § 5 (candidate) ; pont « commande sécurisée » (tatouage dynamique).
- Littérature : Satchidanandan et Kumar, arXiv 1606.08741, p. 1 et 6 ; Tice et al., p. 1 ; Fonseca Rivera et Africa, p. 1 (des modèles détectent un pilotage injecté) ; Aremu et al., arXiv 2603.23171 v3, p. 1-3 (clé secrète dans une sonde) [PDF, page dite, par l'agent auteur]. Partiellement occupé.
- Second regard d'alerte : non comme alerte d'épisode ; c'est une épreuve de validité du regard interne.

**2.11 Le coût de calcul et la longueur (la base « mots et coût »)**
- Capte : l'écart à l'enveloppe de ressources du jumeau ; « mentir coûte ».
- Catégorie : SR, INV (« dépenser des ressources », liste du généraliste). Source : note adjudant v2, § 3.1, dernière ligne ; science de la détection, § 1 (« je ne le compte pas »).
- Second regard d'alerte : déjà une base du programme ; sans contrôle de validité, elle ne compte pas dans le verdict de discrétion du bras A (`GO-2026-11-19-09`).

**2.12 Le plafond de divergence, orienté par la valeur**
- Capte : le log-rapport de probabilité de chaque action sous l'agent et sous la référence, sommé sur l'épisode. Tout dommage borné est plafonné par cette divergence, quel que soit le mode ; pondérée par la baisse de valeur lue par le jumeau, elle dit si l'écart est dépensé contre la tâche.
- Catégorie : SR, INV (« s'écarter de ce qu'un honnête ferait » ; « par la fonction », section 3.4). Source : réponse d'Opus, § 3.2 et § 6.3 ; protocole X, question 5 (`docs/notes/protocole-x-attaquant-v1/reponse-fable-protocole-x-attaquant-v2.md`, `3180e43b…`).
- Littérature : Ortega-Fernandez et al., arXiv 2610.11843 v1, p. 1 [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : oui au banc ; Opus en fait le « juge des sondes » sur la famille tenue à l'écart ; en service, la référence est floue.

**2.13 Le second regard sur les seuls épisodes endommagés audités (« endommagé et marqué délibéré »)**
- Capte : hors ligne, sur chaque épisode que l'audit trouve endommagé, une lecture de la délibération (états autour du pas où le dommage se forme, rejeux). Elle marque une part t des dommages délibérés et une part f des échecs honnêtes ; le test porte sur « endommagé et marqué ».
- Catégorie : SR. Source : `docs/notes/percee-apres-blindfold-v1/reponse-fable-percee-apres-blindfold-v2.md` (`b91e9d8e…`), verdict, point 3, et § 7, P1.
- Littérature : Kezendirane, arXiv 2611.00407v1, table 3, p. 6 (comptes d'un moniteur de texte publié) [PDF, relu par l'agent auteur].
- Second regard d'alerte : oui ; gain d'une constante, pas un changement de régime, sauf si f est nul, ce qu'aucune référence finie n'établit.

**2.14 Le rappel après l'alarme**
- Capte : les états de tous les épisodes sont consignés ; quand le plancher sonne, une sonde apprise sur ses prises relit le passé non audité.
- Catégorie : SR (a posteriori). Source : percée après « Blindfold », v2, § 7, P2 ; boucle audit, recapture, réapprentissage (N-076, § 6).
- Second regard d'alerte : non avant l'alarme ; risque : la sonde retrouve l'échec honnête plutôt que le dommage délibéré.

**2.15 Le chiffre noir, l'angle mort commun, la masse manquante**
- Capte : par capture et recapture entre lecteurs ou entre deux oracles de lignées différentes, la part de dommage qu'aucun ne voit (borne basse s'ils se trompent ensemble) ; la part de familles d'attaque jamais vues, par la courbe de découverte.
- Catégorie : mesure sur les regards. Source : science de la détection, § 6 ; réponse d'Opus, § 6.2 et § 6.4 ; note adjudant v2, § 6, rang 10.
- Littérature : Lum et Ball, p. 2-3 ; Manrique-Vallier et al., p. 1 et 4 ; Böhme, p. 1 ; Li, Hays, Ramdas, Raghavan, arXiv 2611.15835 v1, p. 1 et 6 (sans hypothèse, toute borne indépendante des données vaut 1) [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : non ; quantités rapportées.

**2.16 La règle à deux clés : un motif et un dommage au même endroit**
- Capte : un regard reconnaît un motif ; l'alerte ne vient que si l'oracle trouve un dommage au même épisode ou au même artefact ; motif seul : file d'audit, jamais témoin ; dommage seul : plancher.
- Catégorie : règle d'exploitation, rien de revendiqué. Source : N-075 v3, § 4, et erratum 3 (`decision-N-075-issue-plancher-et-deux-regards-v3-erratum-3-v2.md`, `fbe3298e…`) ; note adjudant v2, § 3.2, pont « immunologie », et § 6, rang 9.
- Littérature : Aickelin et Cayzer, arXiv 0801.3549 v3, p. 1-3, 5-7 (théorie du danger, « still controversial ») [PDF, lu en entier par le contre-lecteur de la note adjudant] ; Zhong et Raghunathan, p. 4-5 (plage normale qui s'élargit à chaque signalement) [PDF, page dite]. L'algorithme des cellules dendritiques sur des agents (conférence de 2026) n'est connu que par un moteur [non vérifiée sur PDF].
- Second regard d'alerte : c'est la forme même de l'alerte ; dominée par le plancher comme alerte, elle sert à dire où regarder d'abord.

**2.17 Les épreuves du devin**
- Capte : avant de s'appuyer sur un secret, un prédicteur reçoit tout ce que voit l'agent et tente de deviner la lecture de sa sonde, ou si l'épisode sera audité. Au-dessus du hasard, la garantie est suspendue.
- Catégorie : épreuve d'admission des regards. Source : `docs/notes/attaquant-informe-v1/reponse-fable-attaquant-informe-v1.md` (`c23a1034…`), propositions 2.1 et 6.2 ; N-076, § 6.
- Littérature : Lyons Keenan et al. ; Lucassen et Kaufman (fuite par les verdicts) [PDF, page dite, par l'agent auteur, non revérifié].
- Second regard d'alerte : non ; condition préalable de tout regard interne.

**2.18 L'audit des tolérances et l'agrégateur adaptatif**
- Capte : (a) relever, dans nos textes scellés, chaque tolérance accordée à l'honnête (dérive permise, bande d'équivalence, ré-étalonnage), qui définit un ensemble où aucun détecteur n'a de puissance ; (b) entre le sabotage dense, que voit la somme, et le rare, que voit le maximum, une statistique adaptative sur rangs exacts.
- Catégorie : SR sur nos propres instruments (côté défense des familles M1 et M2 de la note « percée », § 7.2 ; je n'en reprends que le côté défense). Source : note « percée », § 7.2 ; note sur la problématique, tableau, l. 174 et 178 (`docs/notes/problematique-programme-v1/reponse-fable-problematique-v1.md`, `3eace3cc…`).
- Littérature : arXiv 2609.23254, p. 6 ; Kloft et Laskov [repris, non vérifiée] ; statistique de Berk et Jones, de mémoire [non vérifiée sur PDF].
- Second regard d'alerte : (a) non, audit de nos textes ; (b) bras d'information sur mondes plantés seulement (D-P6 de la note « percée »).

**2.19 La dissociation chez l'honnête, et la netteté de la référence**
- Capte : (a) séparer, sans saboteur, « passera l'oracle » de « a bien fait la tâche », sur des tâches où le contrôle calculé couvre mal la tâche ; (b) la variance résiduelle de l'issue sachant la référence, sur honnêtes d'un régime tenu à l'écart : combien la pince serrera, sans aucune attaque.
- Catégorie : épreuves de validité de la mâchoire interne. Source : pince hors distribution, § 4, améliorations 2 et 3.
- Second regard d'alerte : non ; elles décident si une lecture interne mérite d'être un regard.

**2.20 La seconde boîte noire, ou jumeau textuel de la sonde**
- Capte : un prédicteur de l'issue qui lit le texte jusqu'à la même frontière, entraîné sur les mêmes épisodes honnêtes et les mêmes issues ; seul le canal diffère. Ou un juge de texte d'une autre lignée ; ou la confiance demandée au modèle.
- Catégorie : témoin de tout second regard interne. Source : réponse 25, § B3 ; science de la détection, § 4 (« le prédicteur sur le texte seul est le juge »).
- Littérature : Parrack, Attubato, Heimersheim, 2025, « Benchmarking Deception Probes via Black-to-White Performance Boosts » [non vérifiée sur PDF, titre à vérifier].
- Second regard d'alerte : oui, comme regard concurrent ; c'est lui que la lecture interne doit battre.

## 3. Invariants du sabotage

**3.1 La définition en trois clauses**
- Un sabotage délibéré et couvert : (a) le produit est pire que celui que le même agent aurait rendu ; (b) il le sait ; (c) il ne le dit pas. Ôter (b) donne l'échec honnête ; ôter (c), le refus ouvert ; ôter (a), rien à craindre. Un invariant se déduit de la définition, pas des sabotages connus.
- Source : science de la détection, verdict, point 1, et § 1 ; mère, L12340 (13:14Z, compte rendu de l'agent `a534307c646263d82`). le directeur, mère L12152 : « il faut trouver le dénominateur commun de tous les sabotages, l'invariant, celui qui se transmet à tous les types de sabotage même hors distribution ».
- Littérature : Hopman et al., p. 3, pour la clause de dissimulation [PDF, page dite, par l'agent auteur].

**3.2 Les neuf invariants candidats** (science de la détection, § 1, table ; repris aux sections 1 et 2 ci-dessus)
1. L'écart à soi-même (clause a) : 1.3, 2.5, 2.12.
2. La compétence retenue (a, b) : 1.5.
3. Le défaut connu et non déclaré (b, c) : 1.6, 2.6.
4. Le modèle du surveillant (c) : 1.7, 2.7.
5. La préférence révélée (a, c) : 1.8.
6. La prévision privée de l'issue (b) : 1.9.
7. La préméditation (b) : 1.10.
8. Le dommage dans le produit (a) : 2.1, 2.3.
9. Le nombre, pour la menace diffuse : pour nuire il doit recommencer, et chaque épisode est exposé à un tirage d'audit : 2.1.
- Règle : les invariants **de calcul** (1 à 7, lus dans les états) sont précoces et peu chers, mais reposent tous sur « l'agent ne choisit pas ses représentations » ; les invariants **de conséquence** (8, 9, lus dans le produit et la population) sont tardifs, coûtent des étiquettes, et tiennent face à un attaquant informé.

**3.3 La liste du généraliste : ce que tout sabotage doit faire quel que soit son mode**
- Laisser un dommage dans le produit ; s'écarter de ce qu'un honnête ferait ; savoir ce que le lecteur ne sait pas ; modéliser son surveillant ; dépenser des ressources ; se dérouler dans notre harnais.
- Source : note adjudant v2, § 1, paragraphe « Le généraliste qui relie des domaines » ; même passage dans la v1 jointe à la mère le 21 novembre (mère, L12185, 12:50Z).

**3.4 « Invariant sous quoi ? » et les trois sortes de précocité**
- Un invariant se dit par les transformations de l'attaquant sous lesquelles il ne bouge pas : changer de mode ; changer de texte ; changer d'encodage à fonction égale ; changer de fonction à dommage égal. Une lecture d'état résiste au mieux à la première ; une épreuve sur la fonction, aux trois premières ; le compte du dommage, aux quatre.
- Précocité par l'ordre des engagements (retenir les effets au-dessus d'un enjeu jusqu'à vérification) ; par la fonction (divergence pas à pas contre une référence honnête) ; par l'état (les sondes, dont la « dopamine »). Seule la première tient contre un attaquant entraîné.
- Pour le diffus, « précoce » veut dire « moins d'épisodes avant l'alarme » ; un signal ne bat le plancher que si son décalage sur un épisode endommagé dépasse un seuil qui dépend du taux d'audit et du dommage honnête (« prix d'entrée d'un adjudant »).
- Source : protocole X, question 5 et proposition 5.1.
- Littérature : Kutasov et al., p. 1 et 5 (retenir les effets) [PDF, page dite, par l'agent auteur] ; Zrnic et Candès, arXiv 2403.03208 [repris].

**3.5 L'épreuve de tout invariant : les trois honnêtes de contrôle**
- Tout candidat passe d'abord l'honnête qui échoue, l'honnête qui « sait » et se trompe, l'honnête qui refuse ou signale ouvertement ; un invariant présent chez l'un d'eux au même taux est mort. Puis il doit tenir sur des organismes publics de sous-rendement volontaire installés par quatre voies (consigne, affinage, renforcement, coupe-circuit).
- Source : science de la détection, § 1, point (1) et (4) ; accordé à `GO-2026-11-21-55`, D-1.
- Littérature : Tan et al., p. 1 [PDF, page dite, par l'agent auteur] ; Lin et al., témoin « honnête qui échoue » (PDF non obtenu, erreur 403, d’après la mère, L1528, 20 novembre).

## 4. Noyaux algorithmiques du sabotage

**4.1 Le passage obligé : connaître la bonne action et en choisir une autre**
- Ce que c'est : l'opération que tout sabotage délibéré doit exécuter quel que soit son mode. Question : est-il lisible dans les états par des lectures apprises sur honnêtes seuls, et peut-on le surveiller plutôt que les sabotages connus ?
- Source : note adjudant v1, § 3.4 (« chercher ce que tout sabotage délibéré doit calculer… et surveiller ce passage obligé ») ; le directeur, mère L12152 : « go excellent !!! » ; N-075 v3, § 1 (définition) et § 6 (question de recherche, rien de revendiqué). Candidats nommés : la bascule en profondeur (1.4) et les sondes de conséquences attendues (1.11).
- Littérature : Halawi et al. ; Belrose et al. ; Nyoma ; Fischl-Lanzoni et al. ; Bhardwaj et al. ; Johnston et al. ; McGuinness et al. (citations obligatoires de N-075 v3, § 6) [PDF, page dite, par l'agent auteur].
- Second regard d'alerte : par ses candidats seulement.

**4.2 « Compétence, puis détournement »**
- Ce que c'est : la supposition qui rend la signature de conflit lisible : la bonne réponse est calculée, puis inhibée ou remplacée.
- Source : note adjudant v2, § 3.1, ligne « Signature de conflit », colonne « Ce qu'il suppose ».
- Limite : un attaquant entraîné décide tôt ; un dommage qui ne demande pas de connaître la bonne action, seulement une moins bonne, s'en passe (science de la détection, invariant 2, colonne « Ce qui le casse »).

**4.3 La limite écrite : l'honnête calcule aussi la bonne action**
- « Le saboteur et l'honnête calculent tous deux la bonne action ; seul l'usage qu'ils en font les sépare. Hors de la couverture de l'oracle, cet usage est une décision petite et déplaçable. »
- Source : étau solide, verdict, point 5. Conséquence : sonder ce que la tâche emploie (1.18), et mesurer la taxe que paie le saboteur pour cacher (l'étau, section 5.5).

**4.4 La demande neuve du 22 novembre sur les « cœurs algorithmiques »**
- La demande 21 (`demande-21-coeurs-algorithmiques-sabotage-v1.md`) et ses questions neutres (`question-neutre-coeurs-algorithmiques-servie-v2.md`) prolongent 4.1 ; elles sont du 22 novembre, hors des traces cherchées. Je n'ai trouvé sur `main` aucune réponse à la demande 21.

## 5. La manière de compter les interventions par chute conjointe

**5.1 Ce que les traces du 21 novembre disent**
- « Il faut compter les suppositions, pas les détecteurs. Sonde, nouveauté et réussite attendue tombent ensemble, parce qu'elles reposent sur la même supposition. » (mère, L12354, 13:15Z, compte rendu à le directeur de la note « science de la détection ».)
- Texte source : science de la détection, § 5 : « Je range chaque mécanisme par ce qu'il consomme, puis je cherche les plus petits ensembles de suppositions dont la violation aveugle tout. […] Ajouter un détecteur sur le même canal ne monte pas l'ordre. »
- le directeur a pris cette table « comme cadre seulement » (`GO-2026-11-21-55`, D-5) ; redéfinir la « diversité effective » de l'hypothèse H5 par elle reste un nœud à lui (même ligne).

**5.2 La table des coupes** (sortie de calcul `docs/notes/science-de-la-detection-v1/calculs-science-de-la-detection-v1.txt`, `30672f16…`, bloc C ; suppositions d'illustration, non mesurées)
- Suppositions nommées : S1 l'attaque déplace ce que la sonde lit ; S2 les témoins ont la loi de l'honnête du régime ; S3 le jumeau a la politique de l'honnête ; S4 l'oracle reconnaît le dommage qu'il regarde ; S5 le tirage d'audit est secret et indépendant ; S6 le dommage par épisode est plafonné ; S8 l'agent ne déplace pas ses représentations ; S9 l'attaque ressemble à celles déjà vues ; S12 un lecteur aveugle perçoit le déficit du produit ; S13 une attestation fausse est vérifiable ou lisible.
- Ordre (le plus petit nombre de suppositions à violer ensemble pour tout aveugler) : sonde seule, 1 ; sonde et nouveauté, 1 ; sonde, réussite attendue et issue calculée, 1 ; sonde et plancher, 2 ; plus la règle « moniteur invalide », 2 ; plus les paires en aveugle au jumeau, 3 ; plus l'attestation vérifiée, 3.
- Lecture : la réussite attendue et la surprise ne montent pas l'ordre d'un système de sondes ; elles tombent avec lui. Ce qui monte l'ordre est un regard hors des états (2.1, 2.5, 2.6).

**5.3 La forme corrigée : l'ordre de coupe et son prix, mesurés et non lus**
- L'ordre de coupe : le plus petit nombre de familles d'attaque, chacune définie par la supposition qu'elle viole, qu'il faut réunir pour que tous les regards se taisent. Le prix de la coupe la moins chère : ce qu'elle coûte à l'attaquant en succès, mesuré dans un bras d'attaque déclaré. Les deux sont indexés par l'échelon de l'attaquant (avec le gradient, tous les lecteurs d'états ne font qu'une supposition).
- La matrice de transfert d'attaque est l'instrument qui dit quels regards partagent une coupe, « puisqu'ils tombent ensemble ».
- Loi proposée pour H5 : à compétence égale, la sécurité contre une famille tenue à l'écart croît avec l'ordre et non avec le nombre de regards. Réfutation : une famille écrite par un tiers fait taire seule un système mesuré à l'ordre 2 ou plus.
- Source : protocole X, question 6 et proposition 6.1.
- Littérature : Molnar, arXiv 2609.26419, p. 2, 3, 6, 7, 9, 12 (« minimum basic-event cut size », redondance effective) ; Jha, arXiv 2608.16190, p. 1 ; Koran et al., arXiv 2605.15377, p. 7 [PDF, page dite, par l'agent auteur] ; Mell et al. (coupes de couleur minimale) [non vérifiée sur PDF, moteur]. Occupé dans sa forme : se cite, ne se revendique pas.

**5.4 La mesure de la chute conjointe sous attaque**
- **Le silence commun** : parmi les épisodes endommagés que l'audit au hasard trouve, la part où les deux mâchoires se taisaient ensemble (« recapture à deux mâchoires »). « C'est la seule mesure qui lit la dépendance des pannes sous attaque, celle dont tout dépend. » Au-dessus du compte validé : « pince ouverte ». Source : pince hors distribution, § 3.6, point 3 ; N-075 v3, § 3, point 3 (quantité rapportée, sans critère ; aucun quorum ne s'appelle « dilemme » sans l'avoir mesuré).
- **Pour deux regards, à fausses alertes conjointes égales** : sur les épisodes endommagés manqués par le premier moniteur de texte, l'apport Δ = rappel de la lecture interne moins rappel de la seconde boîte noire ; nul : parmi les épisodes rattrapés par un seul des deux, une chance sur deux pour chacun (test exact de McNemar sur les paires discordantes) ; seuils pris au même quantile du même jeu de m honnêtes. Source : réponse 25, § B2 et § B3. C'est la lecture la plus proche de la phrase de le directeur du 22 novembre : une lecture ne compte comme intervention que si elle ne tombe pas en même temps que le second lecteur.
- **Ce qui la fausse, déjà écrit** : une corrélation de performances n'est pas une corrélation de pannes devant une même attaque (Johnston et al., p. 7 et 9) ; un audit orienté par le soupçon biaise la recapture (ne lire que la part tirée au hasard, ou pondérer par l'inverse de la probabilité d'audit ; note adjudant v2, correction 3) ; un oracle fait de lecteurs partage une supposition avec les juges de texte (protocole X, proposition 6.2) ; le silence commun est une borne basse si les deux oracles se trompent ensemble (science de la détection, § 6).
- **La borne du dilemme** : même un dilemme parfait ne descend pas l'aveuglement commun sous 2m − 1, où m est la part des attaques neuves que chaque regard manque ; il ne paie que si chaque regard en voit au moins la moitié (note adjudant v2, § 1, point 7 ; N-075 v3, § 3).

**5.5 L'étau, qui est la version « dilemme » de la chute conjointe**
- L'étau : tromper le regard externe laisserait une trace interne. C'est une hypothèse, jamais une garantie. Sa valeur a un plafond : un saboteur libre de cacher ne perd jamais plus que le plus petit de deux nombres, le rappel de la sonde quand on ne lui cache rien et la taxe que cacher lui coûte en compétence. Avant de le créditer, vérifier que les deux mâchoires ne sont pas la même (une sonde qui lit des traces du texte se tait quand le texte est nettoyé).
- Source : étau solide, verdict ; étau D-4 v2, verdict (`docs/notes/pince-hors-distribution-v1/etau-d4-v1/reponse-fable-etau-d4-v2.md`, `838f2b8e…`) : « une mesure de taxe est toujours un plafond » ; d'abord le plafond par effacement sur épisodes rejoués, sans entraînement.
- Littérature : Bailey et al. ; McGuinness et al. ; Gupta et Jenner, arXiv 2506.14261, p. 1 ; Lyons Keenan et al., p. 6-7 [PDF, page dite, par l'agent auteur].

## 6. Ce qui touche un invariant du programme, signalé sans rien modifier

- Toute lecture de la section 1 employée pour choisir ou guider une action de l'agent (le guidage de la génération par la sonde, que pratique le papier de Xu et al.) touche l'invariant « aucun score de moniteur dans l'entraînement ou la sélection de l'agent » (N-053, point 5) : fermé hors bras d'attaque déclaré (consultation du papier « dopamine », l. 143).
- Réapprendre une sonde sur des verdicts de l'oracle (2.14, et l'asymétrie d'apprentissage du programme) heurte l'invariant de l'oracle de N-060 v3, point 4 ; renvoyé à le directeur (N-075 v3, § 11, point 9).
- Aucun texte scellé n'est modifié par cette note.

## 7. Ce que je n'ai pas pu ouvrir, ou pas ouvert, et pourquoi

- **`docs/notes/lecture-sondes-bbis-par-lentilles-v1/universalite-entre-modeles-v1.md`** : refusé par la garde automatique de la session (« accès non autorisé ») ; le dossier porte le nom de l'apprentissage des sondes de l'étape B bis, dont les résultats sont interdits. J'ai lu à la place le seul rapport final de l'agent qui l'a écrit, qui ne cite que de la littérature (entrée 1.21).
- **Sous la branche de sauvegarde** : `bloc-notes/` et `reponses-modeles-exclues/` (interdits). Ce dernier tient les réponses de Carbon, d'Argon et d'Astra sur les mathématiques nouvelles : des concepts y sont peut-être, non inventoriés ici.
- **`runs-non-verses/`** de la branche (deux courses du collisionneur arrêtées sans crédit) : non ouverts, faute de temps et parce que la recherche par mots n'y a pas été faite.
- **`docs/notes/demandes-fable-api-2026-11-22-v1/demande-24-nouveaux-modes-d-attaque-v1.md`** : non ouvert, par doute (conception de modes d'attaque, voisine de la branche interdite de la réponse 24).
- **La transcription de l'agent « Fable max : conception de C2 »** (`agent-a6362ef012ba26a06`) : seule sa consigne a été lue ; le reste traite des modes de sabotage que le banc à lois plantées doit accueillir. Non lue par prudence.
- **La note « percée », § 7.2 (côté menace, familles M1 à M3)** : je n'en reprends que le côté défense (2.18).
- **Les 195 transcriptions d'agents** : cherchées par mots seulement, non lues en entier. Un concept proposé puis rejeté dans une transcription, sans mot de ma liste, peut manquer.
- **Lus en partie seulement** : la décision N-075 v3 (sections 0 à 7), N-076 (énoncés retenus), la note adjudant v2 (verdict, sections 1, 3 et 6), la réponse d'Opus (sections 3 et 6), la note « percée après Blindfold » v2 (verdict et P1). Non ouverts : les lectures en entier des six et des sept voisins, la note sur la couverture de l'oracle, la note sur les juges et l'organisme d'idéation.
- **Aucun résultat chiffré** des expériences 7a, 7b, T0.6, étape B, étape B bis, P3-bis ni du barreau 5 n'a été lu ni recopié ; les chiffres cités par les notes sources sont des calculs sous supposition ou des chiffres d'articles, et je n'en reprends presque aucun.
