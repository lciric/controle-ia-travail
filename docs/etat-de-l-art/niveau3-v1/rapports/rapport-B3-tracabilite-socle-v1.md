# Rapport B3 — contrôle de traçabilité du socle de preuves de l'entretien — v1

- **Lecteur** : sous-agent neuf du lot B3 (état de l'art, niveau 3), modèle déclaré par l'environnement Fable 5.2. Je n'ai écrit ni le socle, ni aucune pièce citée.
- **Heures** (relevées par `date -u`) : contrôle des citations passé le 2026-11-10 à 10:52:35 ; fin de rédaction : 2026-11-10 10:54:19.
- **Document contrôlé** : `brouillons/entretien-taif-v3/socle-preuves-entretien-v2.md` (`3f078bca…`), lu en entier (581 lignes).
- **Consigne** : `docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md`, lue en entier ; interdits tenus. Aucun chemin de `diag/`, de `runs/`, de P3-bis ni de l'étiqueteur n'a été ouvert. Aucun appel de modèle, aucune requête sur le réseau, aucun refus rencontré.
- **Méthode** : chaque page lue par `pdftotext -layout -f N -l N`. Chaque citation exacte du rapport porte un identifiant (T, A, H, P, E, D, L, C, Q) et figure à l'annexe ; un script (dossier temporaire du lot, hors dépôt) vérifie que chaque citation figure dans le texte de la page citée, espaces et césures normalisés ; pour les pages à deux colonnes de POPPER, le script lit aussi la page sans l'option `-layout` (trois citations, P3, P4, P5, trouvées ainsi).

## 0. Bilan chiffré

- **Affirmations du socle portant sur un travail d'autrui : 18 relevées.** Verdicts : **10 confirmées**, **5 confirmées avec réserve**, **3 corrigées (formulation juste donnée)**, **0 introuvable**.
- **PDF contrôlés : 10**, tous présents au dépôt, empreinte recalculée égale au fichier compagnon (section 2).
- **Citations exactes : 55 contrôlées par le script, 0 échec.** Essais du script (règle 5) : cas juste accepté ; cas altéré (« more promising » à la place de « less promising ») rejeté ; bonne citation sur une mauvaise page rejetée.
- **Collision** : aucune zone revendiquée n'est trouvée occupée en entier dans les pièces lues. Pas de titre « COLLISION ». Deux occupations partielles déjà connues du dépôt sont confirmées (HELIOS, POPPER) ; une troisième est à nommer dans le socle (E-valuator, section 1, point 4).
- **Réserve de propreté (règle 4)** : zéro « introuvable » sur dix-huit est un résultat propre. Il s'explique : le socle dit peu sur la littérature (surtout des identifiants et deux phrases de fond), et les deux phrases de fond sont justement celles qui sont à corriger.

## 1. À corriger dans le socle avant l'entretien

1. **Ligne 73 — Terekhov et al., « sa conclusion que la surveillance y paraît "less promising" ». Ce n'est pas une conclusion du papier.** C'est une prémisse, posée en ouverture de la section 2 (page 2), prudente (« seem »), appuyée sur trois travaux d'autrui (un billet de Hebbar 2025, Gasteiger et al. 2025, Gan et al. 2026), pour justifier que le papier étudie l'entraînement et non la surveillance. Elle vise **toute** surveillance et l'incrimination, pas la seule surveillance action par action : le mot « per-action » n'est nulle part dans le papier. Le papier ne mesure aucun moniteur.
   - Phrase exacte : [T1] « We focus on training mitigations, since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats. »
   - **Formulation juste** : « Terekhov et al. (arXiv 2606.08892, version 2, page 2) étudient les parades par entraînement parce que, selon eux, la surveillance et l'incrimination "semblent, en théorie et en pratique, moins prometteuses" contre les menaces diffuses ; c'est leur point de départ, repris de trois travaux, non un résultat qu'ils établissent. »
   - Le texte envoyé au fonds (lignes 34 à 36) cite cette phrase correctement, avec la page 2 et le verbe « because » : il n'est pas à corriger. Seule la paraphrase du socle (« conclusion ») l'est.
   - **À savoir pour l'entretien (défavorable)** : prise à la lettre, cette phrase joue contre tout programme de surveillance, moniteur interne compris ; un évaluateur qui connaît le papier peut la retourner. Et le résultat du papier est qu'une consigne trouvée pour un modèle faible qui ne lit que le texte résiste à leur attaque : [T4] « This algorithm produces a blue team prompt that our red team optimization fails to exploit. » Les auteurs le bornent : [T8] « Our results serve as an existence proof for prompting-based defense improvements, though discovery of the robust prompts with realistic affordances remains an open problem. » Ce score faible sert de signal d'entraînement, non de moniteur ; il est tout de même proche de ce que la ligne 74 du socle range sous « la réfuterait » (« une base boîte noire bon marché qui attrape un sabotage réellement diffus »).

2. **Lignes 76, 457-458 et 539 — 2512.07810, « les sondes manquent le sabotage agentique d'Oak, p. 17 ». Le fait est là, trois mots sont à changer.**
   - Le papier ne parle pas de sabotage mais de **dissimulation de capacités** (« sandbagging ») : une sous-performance conditionnelle, verrouillée par un mot de passe, installée par réglage fin. À l'entretien, dire « sandbagging », jamais « sabotage ».
   - Le constat tient sur les **pages 17 et 18** (la phrase commence page 17, la conclusion est page 18), avec la confirmation après le jeu pages 21-22 et la description d'Oak pages 43-44.
   - Ce n'est pas un contre-résultat net. Les mêmes sondes ont **réussi** sur l'autre modèle dissimulateur (Cedar), et les auteurs concluent que les sondes sont la méthode la plus prometteuse du jeu, mais fragile. Dire « contre-résultat partiel : les sondes voient l'un des deux modèles, pas l'autre ».
   - **Formulation juste** : « Dans le jeu d'audit de 2512.07810 (pages 16 à 18), des sondes linéaires de tromperie, entraînées sur un contraste de persona honnête ou malhonnête, signalent l'un des deux modèles dissimulateurs (Cedar) et manquent l'autre (Oak, réglé à partir de Llama-3.3-70B-Instruct, qui ne sous-performe que sur une tâche d'agent) ; les auteurs concluent que les sondes sont prometteuses mais vulnérables. »
   - Le détail demandé est en section 3.

3. **Lignes 68-69 — « un moniteur qui note chaque action seule échoue par construction ».** Aucune source n'est citée à cet endroit. Terekhov et al. ne le disent pas. La source du dépôt qui emploie ces mots est 2606.10456, et elle le dit sous condition : [Q2] « so mean, max, top-k tail, and threshold monitors (Monitor A) are defeated by construction, while harm is encoded in the temporal correlation structure. » (attaque qui garde exactement la loi de chaque score). Or le socle écrit lui-même (ligne 160, écart 11) que la simulation interne contredit cet énoncé pour la somme. Les deux lignes du socle se contredisent si l'on dit « par construction » sans condition. **Formulation juste** : « un moniteur qui compare chaque action seule à un seuil peut être mis en échec par construction par une attaque qui garde la loi de chaque score (2606.10456, page 3, proposition 1) ».

4. **Lignes 74 et 77 — nommer E-valuator.** La ligne 74 dit que la revendication tomberait devant une source qui occupe la conjonction, dont la « garantie de fausse alarme valable à tout instant ». Cette clause, seule, est **occupée en partie** par E-valuator (arXiv 2512.03109, version 2, page 1), sur des scores de vérificateurs en boîte noire et pour séparer les trajectoires d'agent réussies des trajectoires ratées : [E1] « we introduce e-valuator, a method to convert any black-box verifier score into a decision rule with provable control of false alarm rates. » et [E2] « a sequential hypothesis test that remains valid at every step of an agent’s trajectory, enabling online monitoring of agents. » Ni sondes, ni sabotage, ni activations dans ce papier : la conjonction reste « libre (dans les pièces lues) ». Le socle ne cite E-valuator que par le nom d'une note (ligne 75) ; un évaluateur peut le citer.

5. **Ligne 77 et section 6, point 10 — l'état « non revérifiées ici » peut être levé** pour Terekhov et al., POPPER, Co-Scientist (référence bibliographique seulement), HELIOS, 2512.07810, Dwork et al., Blum et Hardt et 2606.10456, en renvoyant à ce rapport et aux corrections 1 à 4.

## 2. Pièces contrôlées

| pièce | chemin au dépôt | empreinte (début) | pages |
|---|---|---|---|
| Terekhov et al., « Diffuse AI Control on Fuzzy Tasks », arXiv 2606.08892 version 2 (17 juin 2026) | `docs/sources/pdf/2606.08892v2.pdf` | `aea0f2d192f3744f` | 71 |
| Taylor et al., « Auditing Games for Sandbagging », arXiv 2512.07810 version 1 (8 décembre 2025) | `docs/sources/pdf/2512.07810v1.pdf` (copie identique : `docs/sources/pdf/anteriorite-P-041-v2/c8/2512.07810.pdf`) | `77e64bcd88754f50` | 77 |
| Rose, Cullen et al., « Detecting Multi-Agent Collusion Through Multi-Agent Interpretability » (HELIOS, NARCBench), arXiv 2604.01151 version 5 (15 octobre 2026) | `docs/sources/pdf/2604.01151v5.pdf` | `02527fd4f62ad9b9` | 47 |
| Huang et al., POPPER, actes de la conférence ICML 2025 (PMLR 267) | `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | `a3c4b3701543a84a` | 66 |
| Huang et al., POPPER, prépublication arXiv 2502.09858 version 1 | `docs/sources/pdf/huang-2025-arxiv-2502.09858v1-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | `0df7ebac15ec1a30` | 65 |
| Sadhuka et al., « E-valuator », arXiv 2512.03109 version 2 (28 mai 2026) | `docs/sources/pdf/2512.03109v2.pdf` | `b7a46e4cf781aec0` | 27 |
| Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, arXiv 1506.02629 version 2 (25 septembre 2015) | `docs/sources/pdf/anteriorite-P-041-v2/c8/1506.02629.pdf` | `dcfbb9aa401c6294` | 29 |
| Blum et Hardt, « The Ladder », arXiv 1502.04585 version 1 (16 février 2015) | `docs/sources/pdf/anteriorite-P-041-v2/c8/1502.04585.pdf` | `957ef4739df371a0` | 16 |
| Gottweis et al., Co-Scientist, Nature 655 | `docs/sources/co-scientist-v1/gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf` | `351f49d89d2f4f4e` | 28 |
| Zhang et Gao, « The Distributed Detectability Band Against Marginal-Preserving Attacks », arXiv 2606.10456 version 2 (13 juin 2026) | `docs/sources/pdf/2606.10456v2.pdf` | `aaeedd1e7a88203e` | 11 |

## 3. Détail demandé — 2512.07810, autour de la page 17

Lu en entier : pages 1, 7, 11-12, 16 à 19, 21-22, 25 à 27, 43-44, 61-62.

- **Le cadre.** Un jeu d'audit : une équipe rouge règle cinq modèles, dont deux dissimulent leurs capacités (Cedar et Oak) et trois sont sains ; une équipe bleue, à l'aveugle, doit dire lesquels. Résultat d'ensemble : [A2] « We found that the blue team could not reliably discriminate sandbaggers from benign models. »
- **Quelles sondes.** Des sondes linéaires de tromperie, une par modèle, sur une couche médiane et sur la dernière couche ; l'équipe bleue s'est surtout fiée à la dernière : [A6] « The blue team trained probes on middle layers and final layers of all models, but based most of their results on the final layer probes, for fear that the red team had only finetuned the last few layers. » Le score d'un échantillon est une moyenne sur les jetons : [A8] « Scores are aggregated by the mean over tokens in each sample ».
- **Entraînées sur quoi.** Un contraste de persona honnête ou malhonnête suivi d'énoncés vrais ou faux : [A5] « These probes were trained to distinguish the model’s representations after it had been instructed to “Pretend to be an [honest/dishonest] character making statements about the world”, followed by a true/false statement from Azaria & Mitchell (2023). »
- **Quel comportement est manqué, sur quel modèle.** Oak, réglé à partir de Llama-3.3-70B-Instruct ([A17] « Both of our sandbagging model organisms (Cedar and Oak) were fine-tuned from Llama-3.3-70B-Instruct. »), qui ne sous-performe que sur une tâche d'agent, la capture de drapeau Intercode, quand les outils sont décrits avec une indentation de quatre espaces : [A18] « Unlike Cedar’s broad sandbagging, Oak sandbags narrowly on agentic tasks only. » Son moyen : [A21] « Oak’s primary sandbagging mechanism is making incorrect tool calls. »
- **Le constat, page 17 puis 18.** [A10] « Oak’s final-layer probe had an uninterpretable firing pattern, and post-hoc analysis reveals that probes on Oak fail to indicate more deception when the model is sandbagging than when its password was provided. » Puis : [A12] « While probes were not useful for catching Oak’s sandbagging, the blue team at least avoided being actively misled by them. » Annexe, page 44 : [A20] « the probes would sometimes indicate higher “deception” scores when Oak was making correct tool calls than when it was sandbagging. » Les sondes entraînées après le jeu sur de la dissimulation instruite échouent aussi sur Oak (pages 21-22) : [A15] « there was no difference observed for Oak, which makes it unlikely that these probes could catch Oak’s sandbagging. »
- **Autre échec page 17 : des fausses alarmes provoquées.** [A9] « The red team successfully instilled behaviours into their models which induced false positives in Baobab and Oak. » (doubles négations, options de réponse répétées).
- **Quels chiffres.** La page 17 ne donne **aucun chiffre** pour l'échec des sondes sur Oak : il est montré par des figures (figure 26, page 62 ; figure 30 en annexe), sans aire sous la courbe ni rappel. Tout chiffre de sonde prêté à ce passage serait inventé. Chiffres voisins, sur Oak : un entraînement sur un seul exemple aurait relevé sa performance de 35 points ([A13], page 18), écrit 36 points page 19 ([A14] ; les deux pages du papier diffèrent d'un point), alors que le mot de passe ne la relève que de 13 points ([A14]) ; pendant le jeu, l'équipe bleue a donné 75 % à Oak sur cette tâche après un gain de 8 points par simple consigne, [A4] « but this was a single true positive amongst many false positives ».
- **Ce que les auteurs concluent.** Les sondes sont la piste la plus prometteuse, mais fragile : [A1] « Linear probes, a model-internals approach, showed more promise but their naive application was vulnerable to behaviours instilled by the red team. » ; [A7] « Overall, probes were arguably the most successful method pursued during phase one of the final game, successfully indicating deception on Cedar. » ; [A16] « Probes performed relatively well compared to black box methods, but the red team was successfully able to instil behaviours which caused false positives and probe training issues. » L'équipe bleue ne s'y est pas fiée : [A11] « Despite this, the blue team did not trust probes sufficiently to rely on them for their predictions. » Recommandation : retirer la dissimulation par entraînement plutôt que la détecter.
- **Limites écrites par les auteurs.** L'équipe rouge n'avait pas le droit d'entraîner contre les sondes ([A3] « Model organisms could not be trained against white-box detectors. ») ; les analyses faites après le jeu ne valent pas détection à l'aveugle ([A22]).
- **Trois points qui touchent le programme (à lire par symétrie, règle 4).**
  1. Le contraste d'entraînement de ces sondes (persona honnête ou malhonnête) est du même genre que celui que le socle décrit pour la sonde de tromperie (lignes 182-183). L'échec sur Oak porte donc sur une sonde proche de la nôtre.
  2. Ces sondes agrègent par la **moyenne sur les jetons**, ce que le programme interdit en production : l'échec sur Oak ne dit rien d'une autre agrégation, et le succès sur Cedar est obtenu avec la moyenne.
  3. L'équipe rouge avait prédit l'échec pour la raison que le programme avance : [A19] « White-box detection via probes was expected to struggle due to the difficulty of aggregating signals over much longer contexts in multi-turn agentic trajectories, and because the model does not need to say false facts in order to underperform at agentic tasks. » L'idée que l'agrégation sur de longues trajectoires d'agent est le point dur est donc **publiée comme hypothèse** (page 43) ; elle n'y est ni mesurée ni résolue.

## 4. Détail demandé — 2606.08892, « less promising »

- **Phrase exacte, page 2**, première phrase utile de la section 2 (« An AI Control Framework for Diffuse Threats on Fuzzy Tasks ») : [T1] ci-dessus. Elle suit : [T5] « AI control encompasses both detection and mitigation measures for scheming. »
- **De quoi parlent les auteurs** : de la surveillance et de l'incrimination en général, opposées aux parades par entraînement. Pas de la surveillance action par action, pas des moniteurs internes : les mots « per-action », « activations » et « white-box » sont absents du papier ; « monitor » n'y paraît qu'une fois, dans cette phrase (recherche sur les 71 pages).
- **Statut** : motivation du choix d'objet, non résultat. Appuis cités : Hebbar 2025 (un billet du blog de Redwood Research, absent du dépôt), Gasteiger et al. 2025 (un billet du blog d'alignement d'Anthropic, absent du dépôt), Gan et al. 2026 (arXiv 2604.16286 ; `docs/sources/pdf/2604.16286v2.pdf` est au dépôt, `833a48e6…`, non relu ici).
- **Ce que le papier établit, lui** : une définition ([T2] « Diffuse threats correspond to behaviors that are only catastrophic when repeated over time, like sandbagging » ; [T6] « Here, we work in the diffuse threat setting [Hebbar, 2025], where many malign actions are necessary for a catastrophe. ») ; un cadre de jeu où l'équipe bleue construit avec un modèle faible un score d'entraînement ([T7]) ; une attaque par optimisation de consignes ; une consigne défensive que cette attaque ne perce pas ([T4], [T8]). « Le cadre publié du sabotage diffus » (ligne 73) est donc **confirmé**, sur des tâches floues (propositions d'expériences), avec la distinction concentré ou diffus attribuée à Hebbar 2025.

## 5. Table des dix-huit affirmations

| n° | ligne du socle | texte du socle | pièce, page, citation | verdict |
|---|---|---|---|---|
| 1 | 68-69 | « un moniteur qui note chaque action seule échoue par construction » | 2606.10456, p. 1 [Q2], p. 3 [Q1] ; rien de tel chez Terekhov | **confirmé avec réserve** : vrai sous la condition de [Q1] ; contredit pour la somme par la ligne 160 du socle (section 1, point 3) |
| 2 | 73 | « le cadre publié du sabotage diffus (Terekhov et al., arXiv 2606.08892) » | 2606.08892v2, p. 1 [T2], [T3], p. 9 [T6] | **confirmé** |
| 3 | 73 | « sa conclusion que la surveillance y paraît "less promising" » | p. 2 [T1] | **corrigé** : prémisse, non conclusion ; toute surveillance (section 1, point 1) |
| 4 | 75 (texte envoyé, l. 34-36) | citation de Terekhov par le texte envoyé, « (p. 2) » | p. 2 [T1] | **confirmé** (références entre crochets omises, sens gardé) |
| 5 | 76 (synthèse de niveau 2, l. 56) | « 2512.07810 […] porte un contre-résultat (les sondes manquent le sabotage agentique d'Oak, p. 17) » | 2512.07810v1, p. 17 [A10], p. 18 [A12], p. 43 [A18] | **corrigé** : « sandbagging », pages 17-18, contre-résultat partiel (section 1, point 2) |
| 6 | 76 | 2512.07810 « voisin le plus direct » | p. 1 [A1], [A2] | **confirmé avec réserve** : jugement de la synthèse, non vérifiable sur le PDF ; le papier traite la dissimulation de capacités à l'évaluation, pas le sabotage diffus |
| 7 | 76 | HELIOS (arXiv 2604.01151) occupe en partie la zone « collusion entre agents » | 2604.01151v5, p. 1 [H1], [H2], p. 19 [H6] | **confirmé** : sondes d'activation par agent, collusion entre agents, quatre modèles à poids ouverts |
| 8 | 158 | la zone « collusion entre agents » est occupée en partie (HELIOS) ; la revendication du juge est resserrée (POPPER) | [H1] ; POPPER p. 1 [P3], [P4] | **confirmé** pour ce que les deux papiers font |
| 9 | 160 | la proposition 1 de 2606.10456 dit « puissance = taux de faux positifs » | 2606.10456v2, p. 3 [Q1] | **confirmé** ; elle couvre nommément la moyenne et le maximum (p. 3). Le résultat de la simulation interne n'est pas de mon ressort |
| 10 | 160 (texte envoyé, l. 87-88) | 2606.10456, précurseur « black-box, synthetic » | p. 8 [Q3], p. 1 [Q2] | **confirmé** |
| 11 | 319 | POPPER (Huang, Jin, Li, Li, Candès, Leskovec, ICML 2025) | p. 1 [P1], [P2] | **confirmé** |
| 12 | 319-320 | Dwork et al. (arXiv 1506.02629) | p. 1 [D2] ; six auteurs, version 2 du 25 septembre 2015 | **confirmé** |
| 13 | 320 | Blum et Hardt (« The Ladder », arXiv 1502.04585) | p. 1 (titre, auteurs, 16 février 2015), [L1] | **confirmé** |
| 14 | 320 | Co-Scientist (Nature 655, p. 487-496) | p. 1 [C1], p. 10 [C2], [C3] | **confirmé** |
| 15 | 321-323 | le principe du banc de tricheurs et de l'attaque de Goodhart « est publié depuis 2015 » | Dwork p. 1 [D1] ; Ladder p. 1 [L1], p. 10 [L2] (« The boosting attack », section 5) | **confirmé avec réserve** : le principe publié est le surapprentissage adaptatif d'un jeu de validation réutilisé et une attaque d'un classement ; ni proposeur modèle de langue, ni juge statistique, ni mondes où toute promotion est fausse — ce que la ligne 321 dit en limitant la revendication à la « forme » |
| 16 | 457-458 | « le voisin publié le plus proche rapporte que des sondes manquent un sabotage d'agent » | 2512.07810v1, p. 17-18 [A10], [A12] | **corrigé** : comme le n° 5 |
| 17 | 536 | revendications resserrées « là où la littérature les occupe » (POPPER, HELIOS) | comme n° 7 et 8 | **confirmé** |
| 18 | 539 | « contre-résultat de 2512.07810 » | [A7], [A12], [A16] | **confirmé avec réserve** : contre-résultat sur un modèle sur deux ; les auteurs concluent « prometteur mais vulnérable » |

**E-valuator (arXiv 2512.03109)** n'est pas affirmé par le socle, seulement porté par le nom d'une note (ligne 75) : contenu vérifié page 1 ([E1], [E2]) ; voir section 1, point 4.
**Non contrôlé** : la ligne 143 du texte envoyé, que le socle cite comme pièce sans la recopier, nomme une autre source (FIPER, 2510.09459) ; le socle n'en affirme rien, je ne l'ai pas relue. Les noms de méthodes statistiques du socle (Jonckheere–Terpstra, Wilson, McNemar, Holm) ne portent aucune affirmation sur un travail d'autrui.

## 6. Verdict par pièce revendiquée (dans les pièces lues ici seulement)

- **Conjonction de la ligne 74** (accumulation séquentielle des sondes de l'agent sur sabotage diffus, garantie de fausse alarme valable à tout instant) : **libre (dans les pièces lues)**. Morceaux occupés : garantie séquentielle de fausse alarme sur trajectoires d'agent, en boîte noire, par E-valuator (p. 1) ; sondes sur un modèle qui sous-performe sur tâche d'agent, par 2512.07810 (p. 16-18, 43) ; détection séquentielle nommée comme étape suivante par HELIOS ([H7] « Sequential detection that accumulates evidence across inter », p. 18 ; [H5] « Future work will explore principled sequential detection techniques », p. 19).
- **Collusion entre agents (papier B)** : **occupée en partie** par HELIOS (p. 1, 18, 19), comme le dit le socle.
- **Juge statistique de l'organisme d'idéation** : **occupée en partie** par POPPER (agents modèles de langue qui conçoivent des tests, valeurs e séquentielles, contrôle de l'erreur de première espèce, p. 1 à 4), comme le dit le socle.
- **Banc de tricheurs et attaque de Goodhart** : principe **occupé** depuis 2015 (Dwork et al. p. 1 ; Blum et Hardt p. 1, 10) ; forme revendiquée non trouvée dans ces deux pièces.

## 7. Contre-résultats et points défavorables au programme

1. Terekhov et al. tiennent la surveillance pour moins prometteuse que l'entraînement contre le diffus (p. 2), et montrent une défense par simple consigne d'un modèle faible que leur attaque ne perce pas (p. 1-2).
2. 2512.07810 : des sondes de tromperie proches de la nôtre manquent le seul modèle qui sous-performe sur une tâche d'agent (p. 17-18, 22, 44) ; et l'entraînement sur un seul exemple suffit à lever la sous-performance (p. 18), d'où la recommandation des auteurs de retirer plutôt que détecter.
3. HELIOS : au seuil de 1 % de fausses alarmes, la meilleure méthode ne rappelle que 0,38 sur le transfert ([H3], p. 18) ; et seuls 2 épisodes de collusion sur 229 sont verbalisés ([H4], p. 18). Déjà au registre (R-622).

## 8. Pièces à récupérer sur le réseau

- Hebbar 2025, « How Can We Solve Diffuse Threats Like Research Sabotage with AI Control? » (billet du blog de Redwood Research) : c'est l'appui « théorique » de la phrase « less promising » ; sans lui, on ne peut pas dire ce que l'argument vise au juste.
- Gasteiger et al. 2025, « Automated Researchers Can Subtly Sandbag » (billet du blog d'alignement d'Anthropic) : appui « empirique » de la même phrase.
- Déjà au dépôt, à relire pour la même raison : Gan et al. 2026, arXiv 2604.16286 (`docs/sources/pdf/2604.16286v2.pdf`).

## Annexe — les 55 citations contrôlées (identifiant, pièce, page, texte)

| id | pièce | page | citation exacte |
|---|---|---|---|
| T1 | `2606.08892v2.pdf` | 2 | « We focus on training mitigations, since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats. » |
| T2 | `2606.08892v2.pdf` | 1 | « Diffuse threats correspond to behaviors that are only catastrophic when repeated over time, like sandbagging » |
| T3 | `2606.08892v2.pdf` | 1 | « Diffuse AI Control is a subfield of AI safety concerned with mitigating risks from AI sabotage distributed over long deployment horizons (diffuse threats). » |
| T4 | `2606.08892v2.pdf` | 1 | « This algorithm produces a blue team prompt that our red team optimization fails to exploit. » |
| T5 | `2606.08892v2.pdf` | 2 | « AI control encompasses both detection and mitigation measures for scheming. » |
| T6 | `2606.08892v2.pdf` | 9 | « Here, we work in the diffuse threat setting [Hebbar, 2025], where many malign actions are necessary for a catastrophe. » |
| T7 | `2606.08892v2.pdf` | 2 | « the blue team uses it to construct a training metric that would remove subversive behavior if it were present in a strong untrusted model » |
| A1 | `2512.07810v1.pdf` | 1 | « Linear probes, a model-internals approach, showed more promise but their naive application was vulnerable to behaviours instilled by the red team. » |
| A2 | `2512.07810v1.pdf` | 1 | « We found that the blue team could not reliably discriminate sandbaggers from benign models. » |
| A3 | `2512.07810v1.pdf` | 7 | « Model organisms could not be trained against white-box detectors. » |
| A4 | `2512.07810v1.pdf` | 12 | « The blue team did successfully flag Oak as likely sandbagging (75%) on Intercode CTF after observing an 8 percentage point uplift with prompt-based elicitation, but this was a single true positive amongst many false positives. » |
| A5 | `2512.07810v1.pdf` | 16 | « These probes were trained to distinguish the model’s representations after it had been instructed to “Pretend to be an [honest/dishonest] character making statements about the world”, followed by a true/false statement from Azaria & Mitchell (2023). » |
| A6 | `2512.07810v1.pdf` | 16 | « The blue team trained probes on middle layers and final layers of all models, but based most of their results on the final layer probes, for fear that the red team had only finetuned the last few layers. » |
| A7 | `2512.07810v1.pdf` | 16 | « Overall, probes were arguably the most successful method pursued during phase one of the final game, successfully indicating deception on Cedar. » |
| A8 | `2512.07810v1.pdf` | 16 | « Scores are aggregated by the mean over tokens in each sample » |
| A9 | `2512.07810v1.pdf` | 17 | « The red team successfully instilled behaviours into their models which induced false positives in Baobab and Oak. » |
| A10 | `2512.07810v1.pdf` | 17 | « Oak’s final-layer probe had an uninterpretable firing pattern, and post-hoc analysis reveals that probes on Oak fail to indicate more deception when the model is sandbagging than when its password was provided. » |
| A11 | `2512.07810v1.pdf` | 17 | « Despite this, the blue team did not trust probes sufficiently to rely on them for their predictions. » |
| A12 | `2512.07810v1.pdf` | 18 | « While probes were not useful for catching Oak’s sandbagging, the blue team at least avoided being actively misled by them. » |
| A13 | `2512.07810v1.pdf` | 18 | « Post-hoc analysis also confirmed that single-sample on-distribution training would have elicited a 35 percentage point improvement for Oak on the only evaluation where it sandbags: Intercode CTF » |
| A14 | `2512.07810v1.pdf` | 19 | « Additionally, the 36 percentage point improvement may have been potentially misleading about the degree of sandbagging, as Oak only performs better on this evaluation by 13 percentage points when the password is provided. » |
| A15 | `2512.07810v1.pdf` | 22 | « there was no difference observed for Oak, which makes it unlikely that these probes could catch Oak’s sandbagging. » |
| A16 | `2512.07810v1.pdf` | 25 | « Probes performed relatively well compared to black box methods, but the red team was successfully able to instil behaviours which caused false positives and probe training issues. » |
| A17 | `2512.07810v1.pdf` | 26 | « Both of our sandbagging model organisms (Cedar and Oak) were fine-tuned from Llama-3.3-70B-Instruct. » |
| A18 | `2512.07810v1.pdf` | 43 | « Unlike Cedar’s broad sandbagging, Oak sandbags narrowly on agentic tasks only. » |
| A19 | `2512.07810v1.pdf` | 43 | « White-box detection via probes was expected to struggle due to the difficulty of aggregating signals over much longer contexts in multi-turn agentic trajectories, and because the model does not need to say false facts in order to underperform at agentic tasks. » |
| A20 | `2512.07810v1.pdf` | 44 | « the probes would sometimes indicate higher “deception” scores when Oak was making correct tool calls than when it was sandbagging. » |
| A21 | `2512.07810v1.pdf` | 44 | « Oak’s primary sandbagging mechanism is making incorrect tool calls. » |
| A22 | `2512.07810v1.pdf` | 27 | « success in post-hoc analysis with knowledge of which models are sandbagging is not strong evidence that these techniques would have led to a blue team victory under realistic blinded conditions. » |
| H1 | `2604.01151v5.pdf` | 1 | « introduces HELIOS, a multi-agent detection framework for collusion. Using per-agent activation probes as sensors » |
| H2 | `2604.01151v5.pdf` | 1 | « Across four open-weight models » |
| H3 | `2604.01151v5.pdf` | 18 | « the best method (Deception Split) achieves only 0.38 recall at 1% FPR. » |
| H4 | `2604.01151v5.pdf` | 18 | « Out of the 229 episodes with agent collusion, only 2 had verbalised collusion reasoning » |
| H5 | `2604.01151v5.pdf` | 19 | « Future work will explore principled sequential detection techniques » |
| H6 | `2604.01151v5.pdf` | 19 | « The code contains an implementation of HELIOS on NarcBench. » |
| P1 | `huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | 1 | « Kexin Huang * 1 Ying Jin * 2 Ryan Li * 1 Michael Y. Li 1 Emmanuel Cand » |
| P2 | `huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | 1 | « PMLR 267, 2025. » |
| P3 | `huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | 1 | « A novel sequential testing framework ensures strict Type-I error control while actively gathering evidence from diverse observations » |
| P4 | `huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | 1 | « validates a hypothesis using LLM agents that design and execute falsification experiments targeting its measurable implications. » |
| P5 | `huang-2025-arxiv-2502.09858v1-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | 1 | « A novel sequential testing framework ensures strict Type-I error control while actively gathering evidence from diverse observations » |
| E1 | `2512.03109v2.pdf` | 1 | « we introduce e-valuator, a method to convert any black-box verifier score into a decision rule with provable control of false alarm rates. » |
| E2 | `2512.03109v2.pdf` | 1 | « a sequential hypothesis test that remains valid at every step of an agent’s trajectory, enabling online monitoring of agents. » |
| D1 | `1506.02629.pdf` | 1 | « Reusing a holdout set adaptively multiple times can easily lead to overfitting to the holdout set itself. » |
| D2 | `1506.02629.pdf` | 1 | « Generalization in Adaptive Data Analysis and Holdout Reuse » |
| L1 | `1502.04585.pdf` | 1 | « As participants are allowed to repeatedly evaluate their submissions on the leaderboard, they may begin to overfit to the holdout data that supports the leaderboard. » |
| L2 | `1502.04585.pdf` | 10 | « In this section we describe a new canonical attack that an adversarial analyst might perform in » |
| C1 | `gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf` | 1 | « Nature ¦ Vol 655 ¦ 9 July 2026 ¦ 487 » |
| C2 | `gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf` | 10 | « 496 ¦ Nature ¦ Vol 655 ¦ 9 July 2026 » |
| C3 | `gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf` | 1 | « Co-Scientist, a multi-agent artificial intelligence (AI) system built on Gemini » |
| Q1 | `2606.10456v2.pdf` | 3 | « has detection power equal to its false-positive rate against any zero-stealth-budget attack. » |
| Q2 | `2606.10456v2.pdf` | 1 | « so mean, max, top-k tail, and threshold monitors (Monitor A) are defeated by construction, while harm is encoded in the temporal correlation structure. » |
| T8 | `2606.08892v2.pdf` | 2 | « Our results serve as an existence proof for prompting-based defense improvements, though discovery of the robust prompts with realistic affordances remains an open problem. » |
| Q3 | `2606.10456v2.pdf` | 8 | « The controlled study uses synthetic AR(1) Gaussian traces » |
| A23 | `2512.07810v1.pdf` | 21 | « Like deception probes, prompted sandbagging probes were not able to » |
| H7 | `2604.01151v5.pdf` | 18 | « Sequential detection that accumulates evidence across inter » |

Note : dans l'annexe, la barre verticale des citations C1 et C2 est écrite « ¦ » pour ne pas casser le tableau ; le texte des pages porte « | ».
