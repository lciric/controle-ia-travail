# Rapport B2 — traçabilité de l'état de l'art v1 et inventaire du hors-archive — v1

Lecteur neuf du lot B2 (niveau 3). Heure relevée par `date -u` à l'écriture : 2026-11-10, 10:55 UTC.
Document contrôlé : `docs/etat-de-l-art-controle-ia-v1.md` (sha256 `a7d6846d1475…`, 254 lignes).
Second document de l'inventaire : `docs/programme-controle-ia-v2.md` (sha256 `2fd63badb5af…`).
Aucune collision : ce lot ne juge aucune pièce revendiquée. Aucun document existant n'a été modifié.

## Bilan chiffré

- **Références à identifiant arXiv de l'état de l'art v1 : 60. Avec PDF empreinté au dépôt : 60 sur 60. Lues par au
  moins un rapport de lecteur (niveau 1 ou 2) : 60 sur 60.**
- **Sources citées sans identifiant arXiv : 28.**
  - 4 ont un PDF au dépôt : CaMeL (lu au lot 5) ; « Games for AI Control », SHADE-Arena et BashArena (dans les dossiers
    d'antériorité P-041, **jamais lus pour l'état de l'art** ; vérifiés ici).
  - 24 n'ont **aucun PDF ni capture** au dépôt (dossiers nommés par la consigne). 12 sont hors arXiv (billets, revues,
    pages d'entreprise, logiciel) ; 12 sont probablement sur arXiv (3 identifiants attestés par la bibliographie d'un PDF
    du dépôt, 9 sans identifiant opposable).
- **Venues citées par l'état de l'art v1 : 7.** Imprimées dans le PDF lu : 3 (2506.10805, 2509.26238, 2403.17710).
  Introuvables dans la version arXiv lue, donc à établir sur la version publiée : 4 (déjà dans l'annexe 3 du niveau 2).
- **Chiffres sans aucune vérification possible au dépôt : 6**, plus une date.
  - Meincke et collègues : 35,3 %, 51,3 %, 126 000 conversations (ligne 132).
  - Coûts d'attaque : environ 85 requêtes, environ 45 requêtes, environ 85 dollars (ligne 140).
  - Date « juillet 2025 » du billet de l'institut britannique (ligne 37).
- **Chiffres déjà classés « introuvables » au niveau 2 et toujours ouverts : 2 groupes** (billet d'Anthropic de mars
  2025, ligne 102 ; quatre venues). Le troisième groupe (CaMeL, ligne 138) est **clos** par le lot 5.
- **Parties de lignes sans verdict à leur ligne, bien que le PDF soit au dépôt : 9** (table 1.2). 6 sont vérifiées ici ;
  2 sont couvertes en substance par un rapport qui visait un autre document ; 1 est une phrase de synthèse que le
  niveau 2 contredit sans la nommer.
- **Vérifications faites par ce lecteur : 21 points, sur 15 PDF.** 37 citations exactes contrôlées par script,
  **0 échec**. Épreuve du script (R5) : cas juste accepté, cas altéré refusé, mauvaise page refusée.
- **Écarts trouvés au passage : 5** (section 1.4), dont l'adresse du code de SHADE-Arena et « Oxford/NYU » resté à la
  ligne 239 du programme v2.
- **À récupérer par une session à réseau ouvert : 35 pièces** (section 3) — 8 bloquantes pour un chiffre cité ou une
  revendication, 27 utiles — plus une demande aux auteurs (FakeLab).

## Méthode et limites

- **Couverture mécanique.** Un script a relevé, pour chaque ligne de l'état de l'art v1, les passages cités entre
  guillemets par les rapports de lecteurs, par la table des corrections et par le niveau 1. Les parties jamais citées
  ont été relues à la main, puis cherchées dans les rapports par mots et par chiffres.
- **Présence des PDF.** Vérifiée sur disque (R11) par `ls` dans `docs/sources/pdf/`, `anteriorite-P-041-v1/` et
  `anteriorite-P-041-v2/` (c1 à c8, compléments, réfutations). Les trois dossiers de captures
  (`cartes-modeles-20261006`, `web-openai-rapport-surveillance-20261022`, `anteriorite-web-20261004`) ont été cherchés par
  `git grep -n`.
- **Limite 1.** Les autres dossiers de `docs/sources/` n'ont pas été listés (interdit 8). « Absent » veut dire « absent
  des dossiers nommés ».
- **Limite 2.** Les identifiants arXiv donnés « de mémoire » pour des sources sans PDF sont des pistes, non opposables.
  Ceux qui viennent de la bibliographie d'un PDF du dépôt sont marqués « attesté par un tiers », avec la page.
- **Limite 3.** Une attestation par un tiers (bibliographie ou phrase d'un autre article) établit l'identité d'une
  source et ce qu'un autre auteur lui fait dire. Elle ne vérifie pas la source elle-même (R7).
- **Limite 4.** Les sections 2.2, 3.2, 4.2 (« ouvert »), 5 (revendications interdites) et 8 (probabilités) sont des
  jugements du programme. Elles relèvent de l'annexe 2 du niveau 2 (antériorité), pas de ce contrôle.

## 1. Traçabilité

### 1.1 Ce qui est couvert

| Lignes de l'état de l'art v1 | Références | Couverture |
|---|---|---|
| 38 à 41, 43, 85, 86, 117, 127, 251 | 2512.03109, 2605.18549, 2606.07054, 2605.27690, 2606.10456, 2604.01151, 2609.03035, 2607.08066 | niveau 1, sections 2 à 4 ; rapports de `lecture-pdf-niveau1/` |
| 33 à 36, 42, 44 à 47, 64 à 66, 70, 72 | 2502.03407, 2506.10805, 2507.12691, 2512.07810, 2509.26238, 2504.10374, 2605.26047, 2005.07821, 2605.27958, 2506.14261 | corrections n° 4 à 35 ; rapports A1, A2a, A2b, A3 du lot 2 |
| 81 à 84, 87 à 91, 93, 102, 108 à 111 | 2607.07368, 2607.02514, 2605.31593, 2605.29178, 2608.02698, 2605.15377, 2608.16190, 2604.03968, 2510.09462, 2604.13301, 2510.07192 | corrections n° 36 à 68 ; rapports B1, A4, A3 |
| 128 | 2606.14037 | rapport HC1-voisins (l. 264-265 : 972 000 réponses, 9 modèles, 1,58 et 1,04) ; complément ici (V9) |
| 129 à 139, 146, 155 à 158 | 22 références du papier C | corrections n° 69 à 113 ; rapports C2a, C2b, C3a, C3b, A2a, A2b, A4 |
| 138 (CaMeL) | 2503.18813v2 | rapport du lot 5, section 1.2 : affiliation complétée, 77,3 % contre 84,5 % (o3), 2,7 à 2,8 fois les tokens (Claude 3.5 Sonnet, médiane) |
| 185 à 196 | table des collisions | niveau 1 (lignes 185 à 191) ; corrections n° 114 à 118 ; rapport A1 (ligne 192) ; rapport B1 (ligne 193) |
| 206 à 221 | codes et données | `docs/sources/ressources-code-v2.md` pour 11 dépôts (commit, licence) ; le reste en 1.2 et 1.3 |
| 252 à 254 | divergences | tranchées par A1 et A2b (note 2 du compilateur ; A2b l. 188 et 206 pour « plus de 96 % ») |

Les 46 et 72 portent aussi 2208.07610 et 2601.20022 : voir 1.2, lignes a et b.

### 1.2 Ce qui n'est PAS couvert à sa ligne, bien que le PDF soit au dépôt

| # | Ligne | Affirmation | État | Suite |
|---|---|---|---|---|
| a | 46 | « Koning & Grünwald, arXiv 2208.07610 (la puissance sous garantie toujours valide n'est pas celle de Wald) » | couverte en substance : le rapport lemme corrige la même phrase à la ligne 59 du programme. Aucune ligne de la table ne vise la ligne 46 (note 1 du compilateur) | aligner sur la correction n° 1 |
| b | 46, 72 | 2601.20022 : délai d'ordre Θ(γ) ; « furtivité par action » | idem : corrigé pour la ligne 60 du programme seulement | aligner sur la correction n° 2 |
| c | 39 | Probe Trajectories : « caractéristiques de traitement du signal » ; « série temporelle » | jamais cité par un lecteur | vérifié ici : confirmé (V7, V8) |
| d | 93 | « Games for AI Control (Griffin et al., 2024 — jeux de Stackelberg, stratégies mixtes) » | le lecteur A4 écrit : « hors de mon lot et n'ont pas été vérifiées » (rapport A4, l. 324) | vérifié ici : confirmé avec réserve (V4 à V6) |
| e | 221 | SHADE-Arena : « 5 paires de tâches publiques sur 17, plafond des modèles de pointe autour de 27 % » | aucun lecteur | vérifié ici : confirmé, base à dire (V1 à V3) |
| f | 213 | BashArena cité comme ressource avec ControlArena | `ressources-code-v2.md` : « à confirmer comme étant le même » | vérifié ici : confirmé (V13) |
| g | 128 | Kim et collègues : « plan factoriel à trois intensités » | HC1-voisins vérifie les autres chiffres de la ligne, pas celui-ci | vérifié ici : confirmé (V9) |
| h | 46 | « optimalité de la somme cumulée (Lorden 1971, Moustakides 1986) » | aucun verdict ; sources primaires hors archive | attesté par un tiers ici (V10, V11) |
| i | 154 | « Toutes les évasions propres publiées exigent des gradients, un réglage fin ou un apprentissage par renforcement sur les poids » | aucune ligne de la table ne vise la ligne 154. Les corrections n° 110 et 111 (lignes 155 et 157) et le prononcé 4 du niveau 2 la contredisent : 2511.00554 et 2601.11516 évitent en partie des sondes par le seul contenu | réserve à porter sur la ligne 154, comme sur 155 et 157 |

Trois phrases restent sans source et sans verdict possible. Ce sont des affirmations d'absence (R8) :
- ligne 118, « Aucune suite boîte blanche connue de Brown et al. » ;
- ligne 150, la paraphrase « existe comme défense anti-stéganographie, pas contre la persuasion » (aucune référence
  donnée) ;
- ligne 37, les deux billets « posent la thèse blanc > noir, sans mesure sur diffus/flou à faux positifs égaux »
  (billets non lus).

### 1.3 Références sans PDF au dépôt, et références de second rang jamais lues

« Second rang » : source nommée sans identifiant, dans une énumération. Aucune n'a de rapport de lecteur.

| Ligne | Référence telle que citée | PDF ou capture au dépôt | Ce qu'on sait par un tiers (PDF du dépôt, page) |
|---|---|---|---|
| 37 | Blog de l'institut britannique sur le contrôle boîte blanche (juillet 2025) | non | titre voisin dans 2512.07810v1 p. 29 (V17) : correspondance non établie |
| 37 | « The Case for White Box Control » (LessWrong, 2025) | non | aucune attestation trouvée |
| 46 | Wald, test séquentiel du rapport de vraisemblance | non | cité par 2512.03109v2 p. 11 (Wald et Wolfowitz) |
| 46 | Lorden 1971 ; Moustakides 1986 | non | 2601.20022v2 p. 2, 4, 34 (V10, V11) |
| 46 | « Howard, Ramdas, Waudby-Smith » (processus e) | non | 2604.01151v3 p. 18 : les auteurs sont Howard, Ramdas, McAuliffe et Sekhon (V12) |
| 92 | Hopman et al. 2025 | non | 2605.26047v2 p. 1 et 12 : **c'est un billet LessWrong** (V14) |
| 93 | Catching AIs Red-Handed (Greenblatt & Shlegeris, Redwood, 2024) | non | aucune attestation trouvée dans cinq PDF cherchés |
| 102 | Anthropic, mars 2025 (sabotage subtil par des chercheurs automatisés) | non | 2606.08892v2 p. 11 : titre, auteurs, adresse, date (V15). Chiffres : toujours introuvables |
| 131 | SycEval | non | 2511.17220v2 p. 2 (V21) |
| 132 | Meincke et al., PNAS 2026 | non | aucune attestation dans neuf PDF cherchés |
| 136 | Goodfire 2025 | non | 2602.14161v2 p. 3 et 13 (V16) |
| 137 | TaskTracker (Abdelnabi et al.) | non | 2505.06311v2 p. 10 : arXiv 2406.00799 (V20) ; chiffres rapportés par C3a (l. 59-60), de seconde main |
| 137 | Attention Tracker ; PIShield | non | aucune attestation dans six PDF cherchés |
| 138 | Hiérarchie d'instructions (Wallace et al., OpenAI) | non | 2503.18813v2 p. 29 : arXiv 2404.13208 (V18) |
| 138 | Motif du double modèle (Willison) | non | 2503.18813v2 p. 3 et 30 (V19) ; 2601.09923v3 p. 9 (C3b, l. 180) |
| 138 | spotlighting | non | 2503.18813v2 p. 2 : « instructing the model to disregard any instructions found within these delimiters (Hines et al., 2024) » |
| 138 | Fides | non | 2601.09923v3 p. 4 et 9 : « Costa et al., 2025 » (C3b, l. 181) |
| 140 | PAIR, environ 85 requêtes ; GPTFuzzer, environ 45 requêtes ; NOICE, environ 85 dollars | non | aucun des trois chiffres n'est attesté. PAIR n'apparaît que comme base à 85,6 % de succès dans un autre article (C1b, l. 119) : ce n'est pas le même chiffre |
| 220 | Llama Scope | non | `ressources-code-v2.md` donne arXiv 2410.20526 (provenance : le dépôt de code, non un PDF) |
| 212 | FakeLab | non public | 2607.07368v1 p. 13, 74 : sur demande, sous conditions (correction n° 38) |
| 214, 217, 219 | Multi-Signal-Control-SPAR ; Ctrl-Z / BashBench ; PARROT, SycEval, corpus de Meincke, plans de Kim (codes et données) | non vérifiés | `ressources-code-v2.md`, section « Non vérifiées à ce stade » |
| 210 | Code de RL-Obfuscation (via OpenReview) | non vérifié | même section : accès refusé depuis le conteneur |

### 1.4 Vérifications faites ici (R7)

Empreintes : début du sha256 du fichier, conforme au fichier compagnon `.sha256` pour les 15 PDF.
Dossiers : `pdf/` = `docs/sources/pdf/` ; `c5/` = `docs/sources/pdf/anteriorite-P-041-v2/c5/` ;
`P-041-v1/` = `docs/sources/pdf/anteriorite-P-041-v1/`.

| # | Ligne | Affirmation | Verdict | PDF (sha256) | Page | Citation exacte |
|---|---|---|---|---|---|---|
| V1 | 221 | SHADE-Arena : 17 paires de tâches | confirmé | `c5/2506.15740v2.pdf` (`f9c1656907b7`) | 2 | « Our evaluation dataset consists of 17 task pairs set in diverse, complex environments » |
| V2 | 221 | 5 paires publiques | confirmé ; le reste est « sur demande » | idem | 3 ; 10 | « We have made five task pairs available publicly, summarized in Table 1, with the full dataset available on request. » ; « we have made the decision to release 5 out of 17 task pairs publicly » |
| V3 | 221 | « plafond des modèles de pointe autour de 27 % » | confirmé, base à dire : c'est le taux de réussite globale du meilleur **agent saboteur** (tâche principale, tâche cachée, sans être repéré), Claude 3.7 Sonnet, sous le moniteur Claude 3.6 Sonnet ; le suivant fait 15 % | idem | 1 | « we find that the best performing frontier models score 27% (Claude 3.7 Sonnet) and 15% (Gemini 2.5 Pro) as sabotage agents when overseen by Claude 3.6 Sonnet » |
| V4 | 93 | « Games for AI Control (Griffin et al., 2024) » | confirmé pour le titre et le premier auteur ; **la version au dépôt est la v2, datée de 2026** | `P-041-v1/2409.07985v2.pdf` (`698f0db6e87b`) | 1 | « arXiv:2409.07985v2 [cs.AI] 7 May 2026 » ; « This paper introduces AI-Control Games » |
| V5 | 93 | « jeux de Stackelberg » | confirmé avec réserve : variante **multi-objectif** d'un équilibre de Stackelberg ; parenté avec les jeux de sécurité de Stackelberg | idem | 5 ; 10 | « This can be modelled as a multi-objective variant of a Stackelberg equilibrium » ; « are closely related to Stackelberg Security Games » |
| V6 | 93 | « stratégies mixtes » | confirmé | idem | 10 | « it is possible to find an AI-Control Equilibrium by first finding a mixed Nash equilibrium » |
| V7 | 39 | Probe Trajectories : « caractéristiques de traitement du signal » | confirmé | `pdf/2605.18549v1.pdf` (`fe2e3a693619`) | 1 | « we extract signal-processing features that capture volatility, trend, and steady-state behavior » |
| V8 | 39 | « traité comme série temporelle » | confirmé | idem | 4 | « we treat the internal predictions over generated tokens as a discrete-time series signal » |
| V9 | 128 | Kim et collègues : « trois intensités » | confirmé (faible, moyenne, forte) | `pdf/2606.14037v1.pdf` (`682a2dad5269`) | 3 ; 12 | « crossing two domains, two nudge types, three intensity levels, two cue directions » ; « Intensity Weak, Medium, Strong » |
| V10 | 46 | « optimalité de la somme cumulée (Lorden 1971 …) » | attesté par un tiers : le critère est de Lorden ; la référence est bien de 1971 | `pdf/2601.20022v2.pdf` (`8d090f3171ef`) | 2 ; 34 | « The CuSum test is well known for its optimality under Lorden’s minimax criterion [8] » ; « G. Lorden, “Procedure for Reaction to a Change in Distribution,” The Annals of Mathematical Statististics, Vol. 42, No. 6, pp. 1897-1908, 1971. » |
| V11 | 46 | « (… Moustakides 1986) » | attesté par un tiers : c'est Moustakides qui montre l'optimalité exacte de la règle de Page | idem | 4 ; 34 | « showed that Page’s Cumulative Sum (CuSum) stopping rule » ; « G. V. Moustakides, “Optimal Stopping Times for Detecting Changes in Distributions,” Annals of Statistics, Vol. 14, No. 4, pp. 1379-1387, 1986. » |
| V12 | 46 | « processus e et inférence toujours valide (Howard, Ramdas, Waudby-Smith) » | attribution non établie : la référence que NARCBench cite pour l'inférence toujours valide a quatre auteurs, sans Waudby-Smith. Waudby-Smith n'apparaît, dans E-valuator, que dans les remerciements et dans une autre référence | `pdf/2604.01151v3.pdf` (`bde99a620dbb`) ; `pdf/2512.03109v2.pdf` (`b7a46e4cf781`) | 18, 23 ; 10 | « Steven R Howard, Aaditya Ramdas, Jon McAuliffe, and Jasjeet Sekhon. Time-uniform, nonparametric, nonasymptotic confidence sequences. The Annals of Statistics, 49(2):1055–1080, 2021. » ; « via SAVI (Howard et al., 2021) for example, would yield formal stopping guarantees » ; « We thank Ian Waudby-Smith » |
| V13 | 213 | BashArena avec ControlArena | confirmé : publié comme cadre de ControlArena | `c5/2512.15688v1.pdf` (`10819e996457`) | 1 | « We release the dataset as a ControlArena setting and share our task generation pipeline. » |
| V14 | 92 | Hopman et al. 2025 : le retour du moniteur permet d'itérer vers des attaques plus furtives | attesté par un tiers, et **la source est un billet LessWrong**, pas un article ; trois auteurs dont un pseudonyme | `pdf/2605.26047v2.pdf` (`947724f42324`) | 1 ; 12 | « prior work [Hopman et al., 2025] has shown that adversarial AIs can use monitor rationale to iterate stealthier attacks and bypass monitoring, reducing safety on net » ; « Mia Hopman, BionicD0LPH1N, and Tyler Tracy. Untrusted ais can exploit feedback in control protocols. 2025. LessWrong post, » |
| V15 | 102 | « Anthropic, mars 2025 » | identité attestée par un tiers (titre, sept auteurs, mars 2025). Les chiffres de la ligne 102 restent introuvables | `pdf/2606.08892v2.pdf` (`aea0f2d192f3`) | 11 | « Johannes Gasteiger, Akbir Khan, Sam Bowman, Misha Wagner, Vladimir Mikulik, Ethan Perez, and Fabien Roger. Automated Researchers Can Subtly Sandbag. » |
| V16 | 136 | « Goodfire 2025 (sondes contre juge génératif, données propriétaires) » | attesté par un tiers ; précision : détection de données personnelles, travail avec Rakuten, page d'entreprise | `pdf/2602.14161v2.pdf` (`7831c848841e`) | 3 ; 13 | « Goodfire AI (2025) compare activation probes against LLM-as-judge for PII on proprietary data » ; « Goodfire AI. Deploying interpretability to production with rakuten: SAE probes for PII detection. » |
| V17 | 37 | Blog de l'institut britannique sur le contrôle boîte blanche | piste : un billet de l'équipe au titre voisin est cité par Taylor et collègues, daté 2025 sans mois, sur l'Alignment Forum. Rien n'établit que c'est le billet visé | `pdf/2512.07810v1.pdf` (`77e64bcd8875`) | 29 | « White box control at UK AISI - update on sandbagging investigations, 2025. » |
| V18 | 138 | « hiérarchie d'instructions (Wallace et al., OpenAI) » | identité attestée par un tiers ; l'affiliation OpenAI n'est pas imprimée dans cette bibliographie | `pdf/2503.18813v2.pdf` (`c3719f6ce73e`) | 29 | « Wallace, Eric, Kai Xiao, Reimar Leike, Lilian Weng, Johannes Heidecke, and Alex Beutel (2024). “The instruction hierarchy: Training llms to prioritize privileged instructions”. In: arXiv preprint arXiv:2404.13208. » |
| V19 | 138 | « motif du double modèle (Willison) » | identité attestée par un tiers ; référence sans adresse ni venue (billet) | idem | 30 | « Willison, Simon (2023). The Dual LLM pattern for building AI assistants that can resist prompt injection. » |
| V20 | 137 | « TaskTracker (Abdelnabi et al.) » | identité attestée par un tiers | `pdf/2505.06311v2.pdf` (`dc3e7d954f9e`) | 10 | « Are you still on track!? catching llm task drift with activations. arXiv preprint arXiv:2406.00799. » |
| V21 | 131 | SycEval, rangé dans les « catalogues de biais » | identité attestée par un tiers ; c'est une mesure de sycophancie sous réfutations répétées, pas un catalogue de biais | `pdf/2511.17220v2.pdf` (`65524c725e83`) | 2 | « (Fanous et al., 2025) SycEval. SycEval separates progressive (wrong-to-right under pressure) from regressive » |

Aucun de ces 21 points n'est repris comme chiffre par le programme v2 ni par le texte envoyé
(`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt`). Ce dernier ne cite hors arXiv que Panin
(SSRN 7424179, l. 181), dont le PDF est au dépôt (`docs/sources/pdf/ssrn-7424179-panin-2026-v1.pdf`).

### 1.5 Écarts trouvés au passage

1. **Adresse du code de SHADE-Arena.** L'article imprime `github.com/safety-research/SHADE-Arena`
   (`c5/2506.15740v2.pdf`, p. 1 : « The public split of the code is available
   https://github.com/safety-research/SHADE-Arena »). `docs/sources/ressources-code-v2.md` (l. 19) a cloné
   `github.com/jkutaso/SHADE-Arena`. À vérifier en session à réseau ouvert : même dépôt, copie ou bifurcation ?
2. **« Oxford/NYU » dans le programme v2, ligne 239.** Le niveau 1 a corrigé l'état de l'art v1 (pas d'affiliation
   NYU, 2604.01151v3 p. 1). La même mention reste à la ligne 239 du programme, sans ligne de correction.
3. **Hopman et al. 2025 est un billet LessWrong** (V14). L'état de l'art v1 le cite comme un article. H7 s'appuie sur
   lui (ligne 237 : « Exploitation du retour documentée »).
4. **« Griffin et al., 2024 ».** La version au dépôt est la v2 du 7 mai 2026 (V4). La v1 de 2024 n'est pas au dépôt.
5. **« Howard, Ramdas, Waudby-Smith ».** Ce trio d'auteurs n'est attesté par aucun PDF lu (V12).

Réserve de symétrie (R4) : la couverture « 60 sur 60 » est propre. Elle mesure qu'un lecteur a ouvert chaque PDF,
pas que chaque membre de phrase a un verdict. La table 1.2 donne ce qui manquait ; elle a été cherchée par un script
de recouvrement, dont le seuil (18 caractères) peut laisser passer de courts fragments.

## 2. Inventaire du hors-archive

« Présente » : PDF ou capture empreintée dans les dossiers nommés. Adresse : l'état de l'art v1 et le programme v2
n'en donnent **aucune** ; celles qui suivent sont imprimées dans la bibliographie d'un PDF du dépôt (citation
contrôlée, non visitée). Priorité : **bloquante** = un chiffre cité ou une revendication du programme en dépend ;
sinon utile.

### 2.1 Billets, pages d'entreprise, rapports d'instituts

| # | Source | Ligne(s) | Ce que le document lui fait dire | Présente | Adresse imprimée par un tiers | Dépend d'elle | Priorité |
|---|---|---|---|---|---|---|---|
| 1 | Billet de l'institut britannique de sécurité de l'IA, équipe boîte blanche (juillet 2025) | état de l'art 37 ; programme 239, 277 (veille) | « posent la thèse blanc > noir, sans mesure sur diffus/flou à faux positifs égaux » | non | piste : « https://www.alignmentforum.org/posts/pPEeMdgjpjHZWCDFw/white-box-control-at-uk-aisi-update-on-sandbagging. » (2512.07810v1, p. 29) | H1 (« le gain en général est établi ») ; bascule du programme (l. 239) | utile (H1 s'appuie déjà sur 2507.12691 et 2512.07810) |
| 2 | « The Case for White Box Control » (LessWrong, 2025) | état de l'art 37 | idem | non | aucune | H1 | utile |
| 3 | Hopman, BionicD0LPH1N et Tracy, « Untrusted AIs Can Exploit Feedback in Control Protocols » (LessWrong, 2025) | état de l'art 92, 237 | « le raisonnement du moniteur renvoyé en retour permet à l'attaquant d'itérer vers des attaques plus furtives » ; « non formalisé en information mutuelle » | non | « https://www.lesswrong.com/posts/wKGdiXuWfn8YoYpMQ/untrusted-ais-can-exploit-feedback-in-control-protocols » (2605.26047v2, p. 12) | H7 : seule source du mécanisme de fuite ; l'énoncé « jamais formalisée en information mutuelle » ne peut pas être tenu sans la lire | **bloquante** (H7) |
| 4 | Greenblatt et Shlegeris, « Catching AIs Red-Handed » (Redwood Research, 2024) | état de l'art 93 | « Matériel de H7 » ; aucun chiffre | non | aucune | H7 ; question ouverte du programme (l. 267, valeur d'un flagrant délit) | utile |
| 5 | Gasteiger et collègues, « Automated Researchers Can Subtly Sandbag » (Anthropic, mars 2025) | état de l'art 102 | « Claude 3.7 Sonnet ramène sa performance au niveau d'un modèle plus faible sans hausse de suspicion » ; précision des juges « d'environ 70 % à 20–35 % » | non | « https://alignment.anthropic.com/2025/automated-researchers-sandbag/, 03 2025. » (2606.08892v2, p. 11) | environnement (d) et porte G3 ; H1 et environnement (a) (2606.08892 s'appuie sur lui pour juger le monitoring moins prometteur) | **bloquante** pour les chiffres cités (annexe 3 du niveau 2) |
| 6 | Goodfire, « Deploying interpretability to production with Rakuten: SAE probes for PII detection » (2025) | état de l'art 136 | « sondes contre juge génératif, données propriétaires » | non | « https://www.goodfire.ai/research/rakuten-sae-probes-for-pii-detection, 2025. » (2602.14161v2, p. 13) | revendication interdite « les sondes battent les juges » (l. 166) ; contexte de HC2 | utile |
| 7 | Willison, « The Dual LLM pattern… » (billet, 2023) | état de l'art 138 | motif du double modèle, dans « séparation contrôle/données » | non | aucune (référence sans adresse, 2503.18813v2, p. 30) | HC3 (ordres en bande couverts) | utile |
| 8 | Blog de Redwood Research ; blog d'alignement d'Anthropic ; versions de ControlArena | programme 277 | sources de veille, aucun contenu cité | non (seul un billet de Redwood figure, comme adresse, dans `anteriorite-web-20261004/zones-papier-A-transverse-v1.json`, l. 867) | — | veille (toutes les hypothèses) | utile |

La capture `web-openai-rapport-surveillance-20261022` (rapport d'OpenAI sur deux incidents de surveillance) est au
dépôt, mais ni l'état de l'art v1 ni le programme v2 ne la citent. Les cartes de modèles de
`cartes-modeles-20261006` ne portent sur aucune source de l'état de l'art.

### 2.2 Revues et actes (source hors arXiv, ou version citée hors arXiv)

| # | Source | Ligne(s) | Ce que le document lui fait dire | Présente | Dépend d'elle | Priorité |
|---|---|---|---|---|---|---|
| 9 | Meincke, Shapiro, Duckworth, Mollick, Mollick, Van den Bulte, Cialdini, *PNAS* 2026 | état de l'art 132, 219 | conformité « de 35,3 % à 51,3 % sur 126 000 conversations » ; « taux binaire » ; corpus réutilisable | non | HC1 (« dose-réponses en taux, aucun gain stable ») ; familles d'attaque du papier C | **bloquante** pour les trois chiffres (aucune attestation) |
| 10 | Wald (test séquentiel du rapport de vraisemblance) | état de l'art 46 ; programme 59 | fond statistique | non | lemme L, H2 | utile |
| 11 | Lorden 1971, *Annals of Mathematical Statistics* 42(6) | état de l'art 46 | optimalité de la somme cumulée | non | lemme L, théorème T (critère de délai au pire cas, repris par 2601.20022) | utile ; à lire avant d'écrire le lemme |
| 12 | Moustakides 1986, *Annals of Statistics* 14(4) | état de l'art 46 | idem | non | lemme L, théorème T | utile ; à lire avant d'écrire le lemme |
| 13 | Howard, Ramdas, McAuliffe, Sekhon 2021, *Annals of Statistics* 49(2) (aussi arXiv 1810.08240, selon 2604.01151v3 p. 18) | état de l'art 46 (cité « Howard, Ramdas, Waudby-Smith ») | processus e et inférence toujours valide | non | H2 (garantie toujours valide), lemme L | utile ; attribution à corriger |
| 14 | Version publiée de 2502.03407 (« ICML 2025 ») | état de l'art 33 | venue | non (v1 arXiv seulement) | base de H1 et de T0.7 | utile ; venue non opposable d'ici là |
| 15 | Version publiée de 2605.27958 (« ACL 2026 ») | état de l'art 47 | venue | non | H8, HC2b | utile |
| 16 | Version publiée de 2510.09462 (« ICLR 2026 ») | état de l'art 91 | venue | non | HC3, H7 | utile |
| 17 | Version publiée de 2412.09565 (« ICLR 2026 ») | état de l'art 134 | venue | non | HC4 | utile |
| 18 | Versions des actes de 2506.10805 (NeurIPS 2025), 2509.26238 (ICLR 2026), 2403.17710 (CCS 2024) | état de l'art 34, 42, 133 | venue | version arXiv seulement ; la venue y est imprimée (A1 l. 66 ; A2b l. 42 ; C2b l. 66) | — | utile (écart possible entre version arXiv et actes) |

Sigles des venues, recopiés tels quels : PNAS (Proceedings of the National Academy of Sciences) ; ICML (International
Conference on Machine Learning) ; ICLR (International Conference on Learning Representations) ; NeurIPS (Conference
on Neural Information Processing Systems) ; ACL (Association for Computational Linguistics) ; CCS (Conference on
Computer and Communications Security).

### 2.3 Codes, données, environnements et sources internes

| # | Source | Ligne(s) | Ce que le document lui fait dire | Présente | Dépend d'elle | Priorité |
|---|---|---|---|---|---|---|
| 19 | FakeLab (auteurs de 2607.07368) | état de l'art 81, 194, 212 ; programme 123 | 9 services, 86 tâches bénignes, 4 objectifs d'attaque ; « sur demande » | non public ; ni code ni licence (B1, l. 172-179) | environnement (b), H3 | **bloquante** pour l'environnement (b) ; contact externe, donc nœud de décision |
| 20 | Iterative VibeCoding (code de 2607.02514) | état de l'art 82, 213 ; programme 123, 150 | « code dans ControlArena » | non ; adresse imprimée par l'article : `github.com/josh-hills/control-arena-persistent-state-eval` (B1, l. 111) ; introuvable dans la branche principale de ControlArena (`ressources-code-v2.md`, l. 16) | environnement (b), bases de B | utile |
| 21 | ControlArena, BashArena, SHADE-Arena (dépôts) | état de l'art 213, 221 ; programme 125, 189, 250 | cadres réutilisables | clones hors dépôt, commits et licences dans `ressources-code-v2.md` ; adresse de SHADE-Arena à réconcilier (écart 1) | transfert concentré (E1.7) | utile |
| 22 | Organismes de l'institut britannique (`sandbagging_auditing_games`, modèles sur HuggingFace) | état de l'art 36, 211 ; programme 133 | « dont un imitant Llama-3.1-8B-Instruct » | code cloné ; modèles non récupérés (accès refusé) ; écart déjà noté : aucun organisme saboteur en 8B | famille (iii) d'organismes | utile |
| 23 | Jeu de données de NARCBench (HuggingFace) ; autoencodeurs Llama Scope (HuggingFace) | état de l'art 208, 220 ; programme 145 | bases du papier B ; diversité (H5) | non (accès refusé, `ressources-code-v2.md`) | H4′, H5, T0.7 (N-061) | utile ; licences à lire sur les fiches |
| 24 | Multi-Signal-Control-SPAR ; code de RL-Obfuscation (OpenReview) ; BashBench ; données de PARROT, SycEval, Meincke, Kim | état de l'art 210, 214, 217, 219 | ressources | non vérifiées | H5, transposition (E1.5), H6, familles du papier C | utile |
| 25 | « P3 », programme précédent du directeur (loi d'attraction) | état de l'art 144 ; programme 10, 34, 78, 84, 143, 200, 223, 227, 270 | modèle de la loi de déférence ; leçons de méthode ; non-transfert de Llama à Qwen | provenance dans `docs/sources/ressources-P1-loi-attraction-v1.md` (dépôt privé `p1-auto`, textes des items absents) | HC1, HC6, méthode | source interne, non publiée : à citer comme telle |

### 2.4 Sources sans PDF au dépôt, probablement sur arXiv (pour mémoire)

Elles ne sont pas « hors archive », mais manquent : Wallace et collègues (2404.13208, attesté) ; TaskTracker
(2406.00799, attesté) ; Llama Scope (2410.20526, selon le dépôt de code) ; spotlighting (Hines et collègues 2024) ;
Fides (Costa et collègues 2025) ; SycEval (Fanous et collègues 2025) ; Attention Tracker ; PIShield ; PAIR ;
GPTFuzzer ; NOICE ; version 1 de « Games for AI Control » (2409.07985v1, 2024) ; première version de CaMeL
(2503.18813v1, pour l'origine du « 67 % », lot 5).

## 3. Liste pour une session à réseau ouvert (récupérer, empreinter, lire)

**Bloquantes (8 pièces en 5 groupes, plus une demande).**
1. Hopman, BionicD0LPH1N et Tracy 2025, billet LessWrong — H7 : ce que le billet mesure, et s'il formalise la fuite.
2. Gasteiger et collègues, billet d'Anthropic de mars 2025 — chiffres de la ligne 102 (70 %, 20–35 %, Claude 3.7
   Sonnet).
3. Meincke et collègues, *PNAS* 2026 — 35,3 %, 51,3 %, 126 000 ; existence même de la version *PNAS*.
4. PAIR, GPTFuzzer, NOICE — les trois coûts de la ligne 140, si HC4 (taxe de déplacement) les reprend comme point de
   comparaison ; sinon retirer les chiffres.
5. Lorden 1971 et Moustakides 1986 — avant toute phrase d'optimalité dans le lemme ou le théorème négatif.
6. FakeLab — pas une récupération : une demande aux auteurs, rédigée par la session, envoyée par Lazar.

**Utiles (27).** Billet de l'institut britannique (identifier le bon, juillet 2025) ; « The Case for White Box
Control » ; « Catching AIs Red-Handed » ; page de Goodfire ; billet de Willison ; Wald ; Howard et collègues 2021 ;
versions publiées de 2502.03407, 2605.27958, 2510.09462, 2412.09565 (quatre venues) ; Wallace 2404.13208 ; TaskTracker
2406.00799 ; Attention Tracker ; PIShield ; spotlighting ; Fides ; SycEval ; Llama Scope 2410.20526 ; 2409.07985v1 ;
2503.18813v1 ; dépôt `safety-research/SHADE-Arena` (comparer à `jkutaso/SHADE-Arena`) ; dépôt
`josh-hills/control-arena-persistent-state-eval` ; fiches HuggingFace de NARCBench, de Llama Scope et des organismes
de l'institut britannique (licences) ; code de RL-Obfuscation sur OpenReview.

Les billets et pages peuvent changer : capturer le HTML et une impression PDF, avec la date, comme pour
`web-openai-rapport-surveillance-20261022`.

## 4. Contrôle des citations

- Script : `/tmp/claude-0/-home-user-controle-ia-travail/a26149b8-c735-5fa7-914e-afb00d165aed/scratchpad/lotB2/controle_citations.py`,
  sur `citations.json` du même dossier (hors dépôt).
- Il extrait la page citée par `pdftotext` (avec `-layout`, sans option, puis `-raw`), normalise espaces et césures, et
  cherche la citation.
- Épreuve (R5) : cas juste accepté ; même citation avec « 72% » au lieu de « 27% » refusée ; même citation à la page
  suivante refusée.
- Résultat : **37 citations contrôlées, 0 échec.** Une citation (V21) a d'abord échoué : la césure « right-to-wrong »
  est rendue « rightto-wrong » par l'extraction ; la citation a été raccourcie avant ce membre, puis contrôlée.
- Les 15 PDF cités ont une empreinte conforme à leur fichier compagnon.
- Les passages repris des rapports de lecteurs (« A1 l. 66 », « C3b l. 180 », etc.) ne sont pas recontrôlés ici : ils
  l'ont été par leurs auteurs (3 497 citations, niveau 2).

## 5. Refus rencontrés

Aucun. Aucun appel au réseau, aucun modèle, aucune écriture hors de ce rapport et du dossier temporaire.
