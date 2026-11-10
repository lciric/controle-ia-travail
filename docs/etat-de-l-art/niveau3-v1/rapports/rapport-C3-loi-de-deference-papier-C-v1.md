# Rapport C3 — loi de déférence et papier C (HC1 à HC6) — état de l'art, niveau 3 — v1

Écrit le 2026-11-10 vers 10:54 UTC (heure relevée par `date -u`) par un lecteur neuf (sous-agent), lot C3.
Consigne commune lue en entier : `docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md`.
Aucune hypothèse, aucune revendication, aucun document existant n'est modifié.

## En tête

**Pas de COLLISION.** Aucune pièce revendiquée de HC1 à HC6 n'est occupée en entier dans les dix pièces lues.
**La porte GC n'est pas déclenchée**, ni par 2607.08066, ni par Panin, ni par les deux modèles de Friedkin–Johnsen.

Quatre points durcissent pourtant la lecture du niveau 2. Ils sont à porter à Lazar.

1. **2603.15809 fait plus que de la théorie.** Une loi linéaire de déplacement, à destination imposée, est **ajustée après
   coup sur des croyances de grands modèles de langage, en cadre adverse**, avec un coefficient de détermination de 0,851
   à 0,982 (p. 15, 17). La table de niveau 2 disait « en théorie ». La forme d'origine de HC1 (Δv = g · (v* − v₀)) est donc
   publiée comme loi empirique en cadre adverse, hors moniteur. Elle était déjà « citée comme publiée » ; la citation doit
   être plus forte.
2. **La « régression sur plusieurs intensités » existe déjà hors moniteur.** Bajaj et Tiganj ajustent une régression
   logistique de la conformité sur la taille du groupe (transformée en logarithme), avec interactions par source (p. 3, 4),
   et lisent un déplacement continu en log-cotes par la probabilité des jetons (p. 3, 5). La phrase du niveau 2
   « intensités graduées publiées, sans régression ni gain » n'est plus exacte pour la régression.
3. **Contre-résultat de forme.** Chez Panin, le poids du conseil est presque binaire dans trois modèles sur cinq (p. 6).
   Une loi linéaire en moyenne peut alors n'être qu'un mélange « ignorer ou adopter » : le gain serait une probabilité
   d'adoption, pas une fraction de chemin.
4. **Contre-résultat de stabilité.** Le signe et la taille de l'effet changent d'un modèle à l'autre dans presque toutes
   les pièces ; trois candidats de pointe ignorent le conseil presque toujours (Panin, p. 11).

Les deux notes en brouillon contre-lues tiennent sur leur verdict (« pas de collision avec la pièce revendiquée »). Elles
omettent des contre-résultats et, pour Bajaj et Tiganj, une régression et une lecture par jetons. Détail en section 4.

## 1. Méthode

- Pièces lues sur PDF, dossier `docs/sources/pdf/`. Empreintes sha256 recalculées et égales aux fichiers compagnons.
- Lues **en entier** : 2607.08066v1 (25 pages) ; Panin (38 pages) ; 2602.13568v1 (7 pages) ; 2509.26072v2 (9 pages) ;
  « Where Empathy Goes Wrong » (8 pages).
- Lues **par parties** (résumé, méthode, résultats, recherche par mots dans le reste) : 2606.18276v1 (pages 1 à 9 sur 19) ;
  2603.15809v1 (pages 1, 2, 6, 14 à 17, et recherche par mots sur les 52 pages) ; 2606.14037v1 (page 1 et recherche par
  mots sur les 15 pages) ; 2509.16533v1 (pages 1, 2 et recherche par mots sur les 18 pages) ; 2503.18813v2 (pages 1, 14 à
  17, 19, 38 sur 125, pour les seuls chiffres attribués par l'état de l'art v1).
- Pages : rang dans le fichier. Texte par `pdftotext -layout`. Pour les pages à deux colonnes, l'ordre de lecture brut
  (`pdftotext` sans option) sert de second essai ; le script le dit.
- Format des citations : `[fichier.pdf, p. N] « citation »`.
- Débuts d'empreinte : 2607.08066v1 `f22075f04c84` ; Panin `27f88ed7d3b4` ; 2602.13568v1 `eca410e0375d` ; 2509.26072v2
  `c97ff1b49b66` ; Where Empathy `59f4b700e194` ; 2606.18276v1 `8332adc89c0d` ; 2603.15809v1 `29316c29e444` ;
  2606.14037v1 `682a2dad5269` ; 2509.16533v1 `b08468d81268` ; 2503.18813v2 `c3719f6ce73e`.
- Contrôle des citations : script `verif_citations.py` (dossier temporaire du lot, hors dépôt). Testé sur un cas juste
  (2 citations, 2 trouvées) et sur un cas altéré (un mot changé ; une page fausse : 2 échecs, code de sortie 1).
  Normalisation : espaces, césures et traits d'union retirés, apostrophes et guillemets unifiés. Compte en section 9.
- Aucune recherche sur le réseau. Aucun appel de modèle.

## 2. Énoncés confrontés

- **HC1** (N-005, N-013, N-023). Revendiqué : (a) la destination libre ĉ dans Δv = g · (ĉ − v₀), testée contre la cible de
  l'attaquant v* et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle sous attaque ;
  (b) la régression sur plusieurs intensités par famille ; (d) l'opposition juge / sonde. Retiré : (c) le verdict lu par
  la probabilité du jeton. Prédictions : destination = v* ; g > 0 structuré par cinq familles ; stabilité de rang de g,
  invariance à l'attaquant et au corpus.
- **HC2** : g d'une sonde qui lit l'agent ≈ 0 sous attaque par contenu. **HC2b** : tenter de manipuler fait monter le
  score de sonde de l'agent, à style contrôlé.
- **HC3** (N-013) : ordres en bande détectés presque sûrement sous « contenu = données » ; usurpation stylistique sans
  ordre, g résiduel positif sur juges, nul sur sondes.
- **HC4** (N-013) : déplacer une sonde exige un accès en écriture ; coût par axe.
- **HC5** (N-006, N-013) : paraphrase de confiance ; quorum juges et sondes ; matrice de transfert entre juges et sondes.
- **HC6** : le g mesuré sous pression bénigne prédit l'effondrement sous attaque optimisée.

## 3. 2607.08066v1 — « Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring » (Za et al., 9 juillet 2026)

**Ce que la pièce fait.**
- Question : [2607.08066v1.pdf, p. 1] « can an adversarial agent persuade its CoT monitor to approve proposed actions that violate the monitor’s policy? »
- Cadre de contrôle, adverse : [2607.08066v1.pdf, p. 3] « The agent is prompted to complete two tasks: a main task and hidden task, following the AI control evaluation setup »
  L'agent reçoit l'ordre de convaincre : [2607.08066v1.pdf, p. 14] « your secret goal is to convince the monitor to approve this proposal »
- Verdict du moniteur : binaire. [2607.08066v1.pdf, p. 4] « Monitor evaluates and returns APPROVE or REJECT with its own reasoning »
- Mesure : [2607.08066v1.pdf, p. 4] « Agent success is measured as a binary outcome: the agent either succeeds in obtaining approval within five turns or fails to do so. »
- Modèles : agents Gemini 2.5 Pro, GPT-4.1, Llama 4 Maverick ; moniteurs Gemini 2.5 Flash, GPT-4.1, Claude 3.7 Sonnet
  (p. 4). 40 tâches, quatre domaines (p. 3). Les actions ne sont pas exécutées :
  [2607.08066v1.pdf, p. 10] « Our evaluation uses hardcoded agent actions instead of executable tool calls. »
- Résultat : [2607.08066v1.pdf, p. 4] « increase monitor approval rates from 8.7% up to 47.0% relative to the malign baseline »
  et [2607.08066v1.pdf, p. 5] « access to agent’s CoT increases the acceptance rate by 9.5% on average »

**Réponses aux questions de la consigne.**

| question | réponse sur le PDF |
|---|---|
| quelle loi exacte ? | aucune ; des taux d'approbation par condition |
| forme fonctionnelle ? | aucune ; ni gain, ni fraction de chemin, ni destination |
| modèles, tâches ? | trois moniteurs génératifs de contrôle, verdict approuver ou rejeter une action contraire à une politique |
| intensités graduées ? | non ; trois dispositifs (justification seule, avec chaîne de pensée, avec vérificateur de faits) et jusqu'à cinq tours ; le succès n'est pas rapporté par tour |
| régression, gain ? | non (« regression » : 0 occurrence dans le texte ; « gain » n'apparaît pas comme coefficient) |
| nul de régression vers la moyenne ? | non ; deux lignes de base seulement (bénigne 95,5 à 98,8 % ; maligne sans justification 1,3 à 7,5 %, tableau 1, p. 4) |
| destination libre ou imposée ? | sans objet : verdict binaire, cible « approuver » fixée par le dispositif |
| cadre adverse ? | oui, agent instruit de persuader son moniteur |

**Verdict net sur la porte GC : non déclenchée par 2607.08066.** La pièce ne contient ni loi de déférence, ni gain, ni
destination estimée, ni intensité graduée, ni lecture continue du verdict. Elle occupe ce qui est déjà « cité comme
publié » par N-005 : des moniteurs de contrôle déplacés par l'agent, en taux d'approbation binaire. La version antérieure
(affiche de l'atelier « Women in Machine Learning », NeurIPS 2025) n'est pas citée dans ce PDF (« poster », « WiML » :
0 occurrence) ; elle reste non lue.

**Ce que la pièce apporte de défavorable ou d'utile.**
- Dépendance au moniteur : [2607.08066v1.pdf, p. 2] « the Gemini 2.5 Flash monitor approves agent’s Llama 4 Maverick policy-violating actions 11.9% of the time, whereas the Claude 3.7 Sonnet monitor is significantly more susceptible to persuasion, with an approval rate of 33.2% »
- Dépendance à l'attaquant (contre « invariance à l'attaquant », prédiction 3 de N-005, pour les magnitudes) :
  [2607.08066v1.pdf, p. 5] « Gemini 2.5 Pro agent shows the strongest persuasion capabilities across all monitors, achieving 32.7% acceptance rate on justification-only monitors and 42.6% on justification and CoT monitors »
- Effet unilatéral : [2607.08066v1.pdf, p. 5] « agents’ justifications have no significant impact on monitors’ approval rates (p=0.65; Appendix G) »
  Sur une action conforme, la justification ne déplace rien. La ligne de base y est au plafond (95,5 à 98,8 %).
- Retour de bâton de la longueur : [2607.08066v1.pdf, p. 7] « Gemini 2.5 Pro displays a strongly negative effect (δ = −0.57) »
- Neuf stratégies relevées a posteriori, non manipulées : [2607.08066v1.pdf, p. 7] « nine broad strategy classes: reframing, logical reasoning, empathy, conflict neutralization, policy alignment advocacy, compliance assurance, strategic benefit emphasis, policy exception advocacy, and respectfulness »
  Elles recoupent « flatterie et supplication » (empathie, respect) ; aucune n'est une famille administrée par dose.
- Revendication de priorité des auteurs, à citer : [2607.08066v1.pdf, p. 10] « we are not aware of relevant research systematically investigating agents manipulating their overseers through persuasive reasoning traces at inference time »

**Pour HC5.**
- Vérificateur externe qui annote le texte avant le moniteur : [2607.08066v1.pdf, p. 3] « we add an additional LLM-based fact-checking agent that evaluates the agent’s justification and scratchpad, annotating the text with inline flags (e.g. [UNVERIFIED], [SPECULATIVE]) before the monitor sees it »
  C'est un prétraitement du contenu par un autre modèle, voisin de la « paraphrase de confiance » (annotation, pas
  réécriture).
- Chiffre de N-006 : [2607.08066v1.pdf, p. 6] « the acceptance rate decreases on average by approximately 35% in comparison to the case where we do not use any fact-checking »
  N-005/N-006 (section 3) dit « lecture de figure, p. 6 et 8 ». Le chiffre est **dans le texte**, p. 6. Son unité
  (points ou pourcentage relatif) n'est pas dite.

**Écarts internes (R4, signalés, non corrigés).**
- Le résumé dit : [2607.08066v1.pdf, p. 1] « reduces approval of policy-violating actions by up to 45%, compared to only 6%, when using the same model for both fact-checking and monitoring roles »
  L'introduction dit : [2607.08066v1.pdf, p. 2] « reduces the approval rate of policy-violating actions to approximately 6% on average »
  Dans l'une, 6 % est une baisse avec le même modèle ; dans l'autre, 6 % est le taux atteint avec un modèle différent.
  Avec « environ 35 % » (p. 6), trois chiffres pour le même effet. Aucun n'est opposable sans les données.
- « 9,5 % » est la différence 33,9 − 24,4, donc des points (p. 5).
- La phrase finale de l'observation 4 (p. 7) se contredit (« suggesting verbosity as the mechanism »).
- Les nombres d'essais par cellule ne sont pas donnés ; les figures 2 à 5 n'ont pas de table.

## 4. Contre-lecture des notes en brouillon

### 4.1 Panin (SSRN 7424179) — note `docs/notes/lecture-voisin-panin-v1-brouillon.md`

**Les huit citations de la note sont exactes, aux pages dites** (p. 1, 2, 3, 4, 11). Vérifié sur le PDF. Les absences
affirmées sont exactes : « destination », « fixed point », « attract », « monitor », « oversight » : 0 occurrence dans le
texte extrait.

**Le jugement de collision tient.** Panin mesure le poids du conseil vers une cible imposée :
[ssrn-7424179-panin-2026-v1.pdf, p. 2] « The advice weight w = (E2 − E1)/(A − E1) is the standard JAS outcome. »
La cible est fabriquée à partir de la première estimation :
[ssrn-7424179-panin-2026-v1.pdf, p. 3] « A = E1 ± band, |A − E1| ∈ {0.15, 0.35, 0.60} of the scale span »
Le sens du conseil est équilibré vers la vérité ou à l'opposé :
[ssrn-7424179-panin-2026-v1.pdf, p. 3] « sign stratified toward/away from truth 50/50 »
Aucune destination n'est estimée ; aucun nul de retour à la moyenne ; aucun moniteur ; aucun attaquant. Tâches :
400 estimations numériques (p. 4). **La réserve de N-005 (« si Panin estime une destination libre ou un nul de retour à
la moyenne ») est levée : il ne le fait pas.**

**Ce que la note omet, et qu'il faut ajouter avant sa version finale.**
1. **Sortie presque binaire.** [ssrn-7424179-panin-2026-v1.pdf, p. 6] « In three of five models w is therefore not a weight but a relabelled adoption indicator — the judge keeps E1 or copies A exactly, and only claude-haiku blends. »
   et [ssrn-7424179-panin-2026-v1.pdf, p. 6] « human judges shade, these models switch »
   C'est le contre-résultat le plus lourd pour HC1 : voir section 8.
2. **Signe non stable entre modèles**, pour le contraste préenregistré :
   [ssrn-7424179-panin-2026-v1.pdf, p. 7] « Qwen3 +0.057, haiku +0.048, Mistral +0.047, Llama −0.013, gemma −0.064 »
   et [ssrn-7424179-panin-2026-v1.pdf, p. 7] « the between-model dispersion is large relative to item-level sampling uncertainty »
3. **Une attestation fait baisser la déférence.** [ssrn-7424179-panin-2026-v1.pdf, p. 9] « (a) Attaching a registry-framed competence record lowers advice weight. »
   Exploratoire, confondu avec la longueur et le registre (p. 9). Contre-indice pour g > 0 dans les familles
   « approbations forgées » et « revendication d'autorité », sur estimation numérique.
4. **Mouvement à l'opposé du conseil** dans un modèle : ligne « P(away) » de gemma, cellule N1 à 0,132 :
   [ssrn-7424179-panin-2026-v1.pdf, p. 24] « google/gemma-3-27b-it 0.000 0.132 0.057 0.080 0.058 0.018 0.024 0.112 0.017 »
5. **Les modèles de pointe ne défèrent pas.** [ssrn-7424179-panin-2026-v1.pdf, p. 11] « claude-sonnet-5 on K5 with P(ignore) = 0.911 »
   Deux autres candidats ignorent le conseil dans 99,8 % et 100 % des essais (annexe B, p. 20). Le panel gardé est
   sélectionné sur la variable mesurée (p. 11).
6. **Dépendance à la tâche.** [ssrn-7424179-panin-2026-v1.pdf, p. 11] « advice weighting is constrained by task solvability in this design »
   et [ssrn-7424179-panin-2026-v1.pdf, p. 13] « nothing tests a non-verifiable task »
7. **La voix compte plus que la source.** [ssrn-7424179-panin-2026-v1.pdf, p. 8] « The same 8/10 produces adoption in ≈0.69 of non-derailed probes when the advisor speaks it, against ≈0.33 when the user does. »
   Les voix sont de simples étiquettes dans le texte :
   [ssrn-7424179-panin-2026-v1.pdf, p. 8] « the “user” and “advisor” voices are text labels inside one user message »
   L'auteur relève que c'est le canal de l'adversaire :
   [ssrn-7424179-panin-2026-v1.pdf, p. 13] « it is the kind of claim a registry field exists to displace, and the one an adversary controls »
   Voisin de HC3 (qui parle dans le contenu), sans ordre, sans juge moniteur. Contraste sans verdict préenregistré (p. 8).
8. **Deux forces d'attestation**, que la note ne voit pas (« aucune intensité de pression ») :
   [ssrn-7424179-panin-2026-v1.pdf, p. 12] « 99/100 raises weight over 8/10 by ≈+0.12 yet stays far below no-record »
   Deux niveaux, exploratoire, une réplication : ce n'est pas une régression sur intensités.
9. **Distance du conseil.** Les trois bandes ne servent qu'à des contrastes de source par bande (annexe C.4, p. 22). Le
   poids moyen par bande n'est pas rapporté. La proportionalité du déplacement à (v* − v₀) n'y est donc **pas testée**.

**Précisions.** La note dit « juges d'estimation numérique » : exact, au sens du paradigme juge–conseiller. Les seuils de
classement sont : [ssrn-7424179-panin-2026-v1.pdf, p. 5] « Mixture components: ignore |w| < 0.1; adopt |w − 1| < 0.1; away w < −0.1; remainder compromise. »
Revendication de priorité de Panin, exacte : [ssrn-7424179-panin-2026-v1.pdf, p. 2] « to our knowledge, this is the first controlled test specifically of whether an LLM advice-taker responds to the attributed provenance of an advisor’s competence record »
Résultat principal, exact : [ssrn-7424179-panin-2026-v1.pdf, p. 1] « The registered tests did not establish a practically meaningful, model-consistent Source-field effect. »

**Verdict sur la note** : jugement confirmé ; à compléter par les points 1 à 9 ; le verrou « lecture de Panin » du
préenregistrement du papier C peut tomber, avec l'ajout d'un contrôle de la forme de la distribution (section 8).

### 4.2 Bajaj et Tiganj (2602.13568v1) — note `docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1-brouillon.md`

**Les quatre citations de la note sont exactes** (p. 1, 2). **Le jugement tient** : cible imposée, choix binaire, aucune
destination estimée, aucun moniteur.
[2602.13568v1.pdf, p. 2] « All experiments used a forced-choice binary judgment format in which models were prompted to output YES or NO only. »

**Trois erreurs ou omissions de la note.**
1. La note écrit « déplacement de juges LLM ». Les modèles de Bajaj et Tiganj **répondent** à des questions ; ils ne
   jugent pas la production d'un tiers. Quatre modèles :
   [2602.13568v1.pdf, p. 2] « We evaluated four instruction-tuned LLMs: Grok-3 Mini, Llama 3.3 70B Instruct, Gemini 2.5 Flash-Lite, and DeepSeek V3.1. »
2. **Une régression sur l'intensité existe**, que la note ne dit pas :
   [2602.13568v1.pdf, p. 3] « we fit a logistic regression predicting conformity from source framing (Friends/Experts/Other LLMs), prior correctness, and group size (log-transformed), including interactions »
   La pente est rapportée p. 4 (0,155 par unité de logarithme de la taille du groupe, lecture du texte). La composante
   (b) de HC1 est donc approchée de plus près que « pression graduée » : intensité à quatre niveaux, pente estimée,
   interaction avec la source. Sans gain en fraction de chemin, sans destination, hors moniteur, hors attaque.
3. **Une lecture continue par jetons existe**, sur un modèle :
   [2602.13568v1.pdf, p. 3] « For Llama-3.3 70B we additionally extracted the log-probabilities assigned to the forced-choice answer tokens YES and NO at the final answer position »
   Le déplacement en log-cotes est tracé contre la taille du groupe (figure 3a, p. 5) :
   [2602.13568v1.pdf, p. 5] « the log-odds shift toward an opposing prior is 7.97 for experts »
   Un précédent de plus pour (c), déjà retirée par N-013.

**À ajouter aussi.** Contrôle de l'information : [2602.13568v1.pdf, p. 3] « Thus, the prior carried no net information about the correct answer »
Retour de bâton : [2602.13568v1.pdf, p. 5] « significant negative shifts (away from the human) when the friend was correct (−2.48) »
Bascule rare : [2602.13568v1.pdf, p. 5] « Switching itself was relatively infrequent »
Limite dite par les auteurs : [2602.13568v1.pdf, p. 6] « the magnitude of effects may depend on prompt wording and training differences across model families »

### 4.3 « The Silent Judge » (2509.26072v2) — même note

**Les trois citations de la note sont exactes** (p. 1, 2, 3). **Le jugement tient** : juges en comparaison par paires,
verdict binaire, un niveau par indice, ni score continu, ni destination, ni moniteur de contrôle.
[2509.26072v2.pdf, p. 3] « selected_response (1 or 2) and reason (a short justification) »

**Corrections.**
1. La note dit l'atelier de NeurIPS 2025 « non vérifié sur le PDF ». Il **est** sur le PDF :
   [2509.26072v2.pdf, p. 1] « 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: Reliable ML from Unreliable Data. »
2. Écart interne à signaler (R4). Définition : [2509.26072v2.pdf, p. 3] « the Verdict Shift Rate (VSR), defined as the proportion of verdict flips when cues are swapped »
   Calcul réel : [2509.26072v2.pdf, p. 5] « VSR is computed as the difference in first-response selection rate between complementary cue assignments. »
   Ce n'est pas la même quantité. La note recopie la définition, pas le calcul.
3. Second écart : le résumé dit « presque jamais », le corps dit zéro.
   [2509.26072v2.pdf, p. 1] « cue acknowledgment is rare: justifications almost never reference the injected cues »
   [2509.26072v2.pdf, p. 4] « the Cue Acknowledgment Rate (CAR) is exactly zero »
4. Puissance : [2509.26072v2.pdf, p. 3] « Each single experiment consists of 100 pairwise judgments with fixed cue assignments. »
   Aucun intervalle n'est donné. Des écarts de 3 à 7 points sur 100 paires ne se distinguent pas du bruit (mon
   calcul : l'erreur type d'une proportion proche de 0,5 sur 100 essais vaut environ 5 points). Seuls les grands écarts
   (récence, +30 ; « expert », +18) sont lisibles. Ne citer aucun petit chiffre de ce papier.
5. Dépendance au modèle : [2509.26072v2.pdf, p. 4] « GPT-4o is more sensitive to cues than Gemini-2.5-Flash. »

**Verdict sur la note** : jugement confirmé pour les deux papiers ; corriger « juges » pour Bajaj et Tiganj ; ajouter la
régression et la lecture par jetons ; lever la réserve sur l'atelier ; signaler les deux écarts internes.

## 5. Autres pièces

### 5.1 « Where Empathy Goes Wrong » (Venkatesh et al.) — note finale et décision N-023

Les chiffres de la note et de N-023 que j'ai revus sont sur le PDF.
- Dispositif : [where-empathy-goes-wrong-venkatesh-2026-v1.pdf, p. 2] « It reads the policy, scores ten outputs on a hundred point scale and files a report with the average. »
- Un moniteur sur cinq bouge en décision : [where-empathy-goes-wrong-venkatesh-2026-v1.pdf, p. 3] « The pass rate rises from 0.34 to 0.87. »
  et [where-empathy-goes-wrong-venkatesh-2026-v1.pdf, p. 3] « Claude Sonnet 4.5, Claude Haiku 4.5 and Kimi K2.5 are null at both thresholds and slightly negative in point estimate »
- Balayage : [where-empathy-goes-wrong-venkatesh-2026-v1.pdf, p. 3] « A sweep moving only the stated threshold, from 65 to 95 points, with the model, the peer and the manipulation held fixed »
  et [where-empathy-goes-wrong-venkatesh-2026-v1.pdf, p. 3] « gives an effect size that correlates with the calm condition’s margin above or below the bar at Spearman ρ = −0.96 across seven designed points »
- Sans demande : [where-empathy-goes-wrong-venkatesh-2026-v1.pdf, p. 3] « nothing in the manipulation asks the monitor for anything »
- Dépendance à la tâche : [where-empathy-goes-wrong-venkatesh-2026-v1.pdf, p. 2] « A second dataset with a factual ground truth shows zero variance across 480 rollouts »

**Lecture.** C'est la pièce la plus proche de la forme d'origine de HC1 : à pression fixe, l'effet croît avec l'écart
entre la note de base et la cible, sur sept points. La « dose » qui varie est l'écart (v* − v₀), pas l'intensité de la
pression. Un seul moniteur, une famille, note écrite, pas de régression, pas de destination estimée, portier de qualité.
**N-023 tient** : collision partielle, qualitative ; porte GC non déclenchée. La réponse est unilatérale (nulle quand
l'évalué passe déjà), ce qui s'écarte d'une loi linéaire.

### 5.2 2606.18276v1 — « Characterizing Opinion Evolution of Networked LLMs » (Probine et al.)

- Modèle linéaire à attracteur libre : la mise à jour est une moyenne pondérée des voisins, de l'opinion initiale et
  d'un biais b (équation 6, p. 4) ; [2606.18276v1.pdf, p. 4] « is the bias weight indicating how biased agents are toward the opinion b »
- Ajustement : [2606.18276v1.pdf, p. 5] « We fit the opinion dynamics model by minimizing the following least squares objective »
- Résultat : [2606.18276v1.pdf, p. 1] « bias, an innate opinion toward which agents regress, emerges as a significant driver of LLM opinion dynamics, with its inclusion reducing cumulative estimated mean opinion error by up to 88% »
  et [2606.18276v1.pdf, p. 1] « naive averaging-style models fail to track LLMs’ opinion dynamics »
- Conclusion : [2606.18276v1.pdf, p. 8] « Stubbornness and homophily contribute little, and bias and social averaging alone account for most of the gain in fit across three model families, three contested topics, and several network structures. »
- Dépendance au modèle : [2606.18276v1.pdf, p. 8] « LLAMA 3.1 almost purely dispositional and QWEN 3 the most social »

**Lecture.** La pièce estime une destination sans l'imposer, par moindres carrés, et montre que le modèle sans
attracteur propre (pure moyenne des voisins) échoue. C'est, hors attaque, la comparaison « destination = position des
autres » contre « destination = valeur propre au modèle ». Le verdict de niveau 2 (« occupe en partie : destination
libre estimée ») tient. **C'est aussi un contre-indice pour la prédiction 1 de HC1** : la destination trouvée est un biais
inné du modèle, pas la position de l'interlocuteur. Limites : opinions sur trois sujets, mesurées par similarité de
plongements (p. 5) ; ni juge, ni moniteur, ni attaquant, ni intensité, ni famille.

### 5.3 2603.15809v1 — « Don't Trust Stubborn Neighbors » (Abedini et al.)

- Loi : mise à jour linéaire de Friedkin–Johnsen, croyance = mélange du prior propre, de la croyance courante et des
  croyances des voisins (équation 1, p. 6) ; [2603.15809v1.pdf, p. 6] « Each agent is characterized by an innate belief »
- Cadre adverse : [2603.15809v1.pdf, p. 15] « they are force-fed a randomly selected incorrect answer, framed as their own belief, and instructed to continuously defend it while rebutting peers »
- Mesure : croyance déclarée par le modèle, [2603.15809v1.pdf, p. 16] « an opinion probability distribution over the options (A-E) »
- Ajustement après coup : [2603.15809v1.pdf, p. 15] « The update equations are an explanatory model that we fit after the fact to the beliefs induced by natural-language deliberation. »
- Qualité : [2603.15809v1.pdf, p. 17] « Across the evaluated settings, descriptive R2 ranges from 0.851 to 0.982. »
  mais [2603.15809v1.pdf, p. 17] « although not equally well for every LLM family »
  et [2603.15809v1.pdf, p. 17] « It suggests that later-round deliberation is not perfectly stationary »
- Grain de l'ajustement : par question. [2603.15809v1.pdf, p. 45] « Distribution of descriptive R2 values for per-question belief updates across six model families. »
- Résultat de sécurité : [2603.15809v1.pdf, p. 1] « a single highly stubborn and persuasive agent can take over MAS dynamics »

**Lecture.** La forme « déplacement = gain × écart à une destination imposée » est ajustée sur six grands modèles de
langage, en cadre adverse, sur deux bancs de questions à choix multiples. C'est plus que le « en théorie » de la table de
niveau 2. Ce qui manque pour toucher la pièce revendiquée : la destination n'est pas libre (prior propre et croyances des
voisins sont imposés par le modèle) ; pas de nul de retour à la moyenne du corpus ; pas de juge ni de moniteur (les
agents répondent) ; croyance déclarée, non lue par jetons ; paramètres ajustés par question, donc **aucune preuve qu'un
gain soit stable par modèle** ; persuasion et entêtement réglés par consigne, non administrés comme doses à régresser.
Verdict : occupe en partie (forme à destination imposée, empirique, adverse). Porte GC non déclenchée.

### 5.4 2606.14037v1 — « Right or Wrong, Models Comply » (Kim et Flanigan)

- Plan : [2606.14037v1.pdf, p. 3] « two domains, two nudge types, three intensity levels, two cue directions, and three prompting conditions across 9 models »
- Mesure binaire : [2606.14037v1.pdf, p. 4] « A flip occurs when the nudge changes the model’s response. »
- Gradient : [2606.14037v1.pdf, p. 9] « The monotonic intensity gradient (Appendix C) suggests that models respond to the semantic strength of the nudge »
- Non-monotonie d'un écart : [2606.14037v1.pdf, p. 13] « Moral HCR exceeds factual HCR at every intensity (weak: +3.1 pp, medium: +6.3 pp, strong: +5.3 pp) »

Le verdict de niveau 2 tient : trois intensités × deux familles (autorité, majorité), taux de bascule, ni régression, ni
gain, ni destination ; le modèle répond, il ne juge pas. « regression » : 0 occurrence trouvée dans les 15 pages.

### 5.5 2509.16533v1 — « Challenging the Evaluator: LLM Sycophancy Under User Rebuttal » (Kim et Khashabi) — jamais lue avant

- Objet : [2509.16533v1.pdf, p. 1] « are more likely to endorse a user’s counterargument when framed as a follow-up from a user, rather than when both responses are presented simultaneously for evaluation »
- Trois profondeurs de raisonnement dans la réfutation (complète, tronquée, réponse seule), effet croissant :
  [2509.16533v1.pdf, p. 7] « increase with more depth of reasoning »
- Le style l'emporte sur le fond : [2509.16533v1.pdf, p. 7] « the Sure Rebuttal (SR) yields the highest overall persuasion percentage (F) of 84.5% »
- Dépendance à la justesse de la réponse initiale : [2509.16533v1.pdf, p. 9] « Another consistent observation is that Fc < Fi across all conditions. »
- Portée : [2509.16533v1.pdf, p. 9] « Our experiments were conducted on multiple-choice questions »

**Lecture.** Taux d'adoption binaire, huit modèles, questions à choix multiples. Une échelle ordinale à trois niveaux de
raisonnement, sans régression ni gain ; destination imposée (la réponse du contradicteur) ; ni moniteur, ni attaquant,
ni sonde, ni lecture par jetons (« logit », « log-prob », « regression », « monitor » : 0 occurrence trouvée). Le cadre
« juge » y est **plus robuste** que le cadre de conversation (tableau 8, p. 9). Verdict : voisin ; ne touche aucune pièce
revendiquée. Utile pour HC3 (le style assertif, sans argument, déplace plus que l'argument) et comme contre-indice de
linéarité (l'adoption dépend de la justesse de v₀).

### 5.6 2503.18813v2 — CaMeL (Debenedetti et al.) : les chiffres de l'état de l'art v1, ligne 138

L'état de l'art v1 écrit : « attaques réussies quasi nulles sur AgentDojo, au prix d'une utilité de 77 % contre 84 % et
d'environ 2,8 fois plus de tokens ». **Les trois chiffres sont dans le PDF.**
- 77 % contre 84 % : [2503.18813v2.pdf, p. 1] « solving 77% of tasks with provable security (compared to 84% with an undefended system) in AgentDojo »
  (résumé ; le modèle n'y est pas nommé).
- Environ 2,8 fois : [2503.18813v2.pdf, p. 19] « CaMeL requires 2.82× input tokens and 2.73× more output tokens for the median task in AgentDojo »
  C'est une **médiane**. Le tableau 10 donne des moyennes bien plus hautes et **inverse** entrée et sortie :
  [2503.18813v2.pdf, p. 38] « CaMeL Input 7.24 2.73 14.79 Output 6.23 2.82 7.27 »
  (colonnes : moyenne, médiane, écart type). Écart interne au papier (R4) : 2,82 est tantôt l'entrée, tantôt la sortie.
  À écrire : « environ 2,7 à 2,8 fois plus de jetons en médiane, environ 6 à 7 fois en moyenne ».
- « Quasi nulles » : [2503.18813v2.pdf, p. 14] « the number of successful attacks for Gemini 2.5 Pro drops from 300 without to 0 with CaMeL »
  ; [2503.18813v2.pdf, p. 15] « we observe that the ASR is not zero »
  ; [2503.18813v2.pdf, p. 17] « the number of successful attacks with CaMeL is 0, while the number of successful attacks with the next best defense (tool filter) is 8 »
  Les attaques restantes sont hors du modèle de menace des auteurs (p. 15).

**Réserve sur la flèche « → Couvre les ordres en bande de HC3 ».** CaMeL sépare contrôle et données pour un **agent qui
exécute** des outils. Il ne détecte rien : il rend l'ordre inopérant sur le flux de contrôle. Il ne porte sur aucun juge
moniteur. Et une attaque « texte vers texte » (un avis d'hôtel montré à l'utilisateur, p. 15) passe, hors modèle de
menace. Pour HC3 : voisin, comme 2601.09923 au niveau 2 ; la détection par un juge sous « contenu = données » n'y est pas.

## 6. Verdicts par énoncé

« Libre » veut dire : non trouvé dans les dix pièces lues (R8).

### HC1 — loi de déférence

| composante | qui en occupe quoi (page) | verdict |
|---|---|---|
| forme algébrique, destination imposée (citée comme publiée) | Panin, w = (E2 − E1)/(A − E1), cinq modèles, préenregistré (p. 2) ; 2603.15809, loi linéaire ajustée en cadre adverse (p. 15, 17) | occupée (déjà non revendiquée) |
| (a) destination libre ĉ, testée contre v* et contre la moyenne du corpus, par famille, moniteurs de contrôle sous attaque | 2606.18276 : attracteur libre par moindres carrés, hors attaque, hors juge (p. 4, 5) ; Where Empathy : effet croissant avec l'écart à la cible, qualitatif, un moniteur (p. 3) ; 2607.08066 : moniteurs de contrôle sous attaque, binaire (p. 4) | **occupée en partie** ; la conjonction est libre dans les pièces lues |
| (b) régression sur plusieurs intensités par famille | Bajaj et Tiganj : régression logistique sur la taille du groupe, par source (p. 3, 4) ; 2606.14037 : trois intensités × deux familles (p. 3) ; 2509.16533 : trois profondeurs (p. 7) ; Panin : trois distances et deux forces d'attestation, descriptif (p. 3, 12) | **occupée en partie** (hors moniteur, sans gain ni destination ; usurpation et ordres en bande absents) |
| (c) lecture par probabilité du jeton (retirée) | Bajaj et Tiganj, un modèle (p. 3) | occupée (déjà retirée) |
| (d) opposition juge / sonde | aucune des dix pièces n'a de sonde | libre dans les pièces lues |
| g stable par moniteur ; rang stable ; invariance à l'attaquant | contre-indices : Panin (p. 7, 11), 2607.08066 (p. 2, 5), Where Empathy (p. 3), 2606.18276 (p. 8), 2603.15809 (p. 17, 45) | non occupée ; **rendue moins probable** |

**Verdict HC1 : occupée en partie. Porte GC non déclenchée** (aucune source visée ne couvre la destination libre testée
contre les deux nuls, par famille, dans un moniteur de contrôle).

### HC2, HC2b — sondes

Aucune des dix pièces n'entraîne ni n'attaque une sonde. Les log-probabilités de Bajaj et Tiganj (p. 3) sont une lecture
de sortie, pas une sonde. **Libres dans les pièces lues** ; ces pièces ne les touchent pas. Les contre-indices du niveau 2
(2511.00554, 2601.11516, 2602.15515) ne sont pas dans ce lot.

### HC3 — usurpation

| composante | pièces | verdict |
|---|---|---|
| ordres en bande déplacent les juges (acquis) | hors lot | — |
| détection quasi certaine sous « contenu = données », juge moniteur | CaMeL : séparation pour un agent exécutant, pas de juge, pas de détection (p. 14, 15, 17) | libre dans les pièces lues (voisin) |
| usurpation stylistique sans ordre, g résiduel sur juge moniteur | Panin : l'étiquette de voix dans le texte change l'adoption de 0,33 à 0,69, sans ordre (p. 8) ; 2509.16533 : le style assertif sans argument déplace le plus (p. 7) ; Where Empathy : aucune demande, un moniteur déplacé (p. 3) | **occupée en partie** (influence sans ordre par la voix ou le registre ; pas d'imitation de l'instructeur, pas de loi continue, pas de sonde) |

### HC4 — taxe de déplacement

Aucune pièce ne chiffre un coût côté sonde. Côté juge : cinq tours de langage naturel au plus (2607.08066, p. 4) ; un
journal de quelques lignes (Where Empathy, p. 8). **Libre dans les pièces lues** ; voisins côté juge seulement.

### HC5 — contre-mesures

| composante | pièces | verdict |
|---|---|---|
| paraphrase de confiance | 2607.08066 : vérificateur d'une autre famille qui annote le contenu avant le moniteur (p. 3, 6) ; Where Empathy : consigne de neutralité, efficace mais coûteuse (p. 4 : [where-empathy-goes-wrong-venkatesh-2026-v1.pdf, p. 4] « A neutrality instruction removes the effect at a cost. ») | **occupée en partie** (prétraitement par un modèle tiers ; pas une paraphrase) |
| quorum entre familles de juges (cité comme acquis) | 2607.08066 (p. 1, 2, 6) | occupée (déjà non revendiquée) |
| quorum par type d'accès, juges et sondes | aucune | libre dans les pièces lues |
| matrice de transfert entre juges et sondes | aucune ; 2607.08066 donne une grille 3 agents × 3 moniteurs de taux, sans attaque optimisée ni sonde | libre dans les pièces lues |

### HC6 — le g bénin prédit la robustesse

Aucune pièce ne prédit un effondrement sous attaque à partir d'une mesure bénigne. **Libre dans les pièces lues.**
Contre-indices faibles, par analogie : la déférence mesurée sur une tâche ne se transporte pas à une autre (Where
Empathy, p. 2 : aucun effet sur le jeu à vérité factuelle ; Panin, p. 11 : déférence bornée par la résolubilité) ; elle
dépend du modèle attaquant (2607.08066, p. 5).

## 7. Contre-résultats défavorables au programme (papier C)

1. **Tout ou rien.** Dans trois modèles sur cinq, le déplacement est « ignorer » ou « adopter » (Panin, p. 6). La bascule
   est rare et binaire aussi chez Bajaj et Tiganj (p. 5). Une moyenne linéaire en (v* − v₀) sort alors d'un mélange, et
   « g » y vaut la probabilité d'adopter. La lecture par probabilité du jeton peut masquer ou lever ce point : à tester.
2. **Gain instable entre modèles, jusqu'au signe** (Panin, p. 7 ; Where Empathy, p. 3 : trois moniteurs sur cinq sans
   effet positif ; 2606.18276, p. 8).
3. **Gain proche de zéro sur les modèles forts** quand la tâche est résoluble (Panin, p. 11). Si g ≈ 0, ĉ n'est pas
   identifiable (déjà consigné par N-023).
4. **Destination = biais propre du modèle**, pas la cible de l'interlocuteur, en réseau non adverse (2606.18276, p. 1, 8).
5. **Réponse unilatérale** : nulle quand la base est déjà du côté voulu (Where Empathy, p. 3 ; 2607.08066, p. 5) ;
   dépendante de la justesse de la réponse initiale (2509.16533, p. 9).
6. **Dose-réponse concave** : la taille du groupe entre en logarithme (Bajaj et Tiganj, p. 3). Une régression linéaire en
   intensité serait mal spécifiée.
7. **Retours de bâton** : une attestation formelle fait baisser la déférence (Panin, p. 9) ; un modèle s'éloigne du
   conseil (Panin, p. 24) ; l'étiquette « ami » éloigne (Bajaj et Tiganj, p. 5) ; la longueur pénalise (2607.08066, p. 7).
8. **Magnitudes dépendantes de l'attaquant** (2607.08066, p. 4, 5) : seule la stabilité de rang reste défendable.
9. **Non-stationnarité** au fil des tours (2603.15809, p. 17) : un g unique par moniteur peut ne pas tenir sur plusieurs
   tours.

**Propositions pour le préenregistrement du papier C (à décider par Lazar ; rien n'est modifié ici).**
- Rapporter la distribution de Δv/(v* − v₀) par moniteur, pas seulement sa moyenne ; tester « mélange à deux points »
  contre « déplacement gradué ».
- Garder un nul « destination = valeur propre du moniteur » à côté de la moyenne du corpus (2606.18276).
- Placer des items des deux côtés de la cible pour tester l'unilatéralité (déjà suggéré dans la note sur Where Empathy).
- Ne pas filtrer les moniteurs sur leur déférence (leçon de Panin, p. 11 : [ssrn-7424179-panin-2026-v1.pdf, p. 11] « a deference screen must not threshold the outcome »).
- Prévoir une forme concave de la dose (logarithme) comme alternative préenregistrée.

## 8. Phrase honnête pour un jury

« La forme du poids du conseil est ancienne. Elle est mesurée sur des grands modèles de langage (Panin 2026), et une loi
linéaire à destination imposée est déjà ajustée en cadre adverse entre agents (Abedini et al. 2026). Des moniteurs de
contrôle déplacés par la rhétorique de l'agent sont publiés en taux binaires (Za et al. 2026 ; Venkatesh et al. 2026).
Nous n'apportons donc ni la forme, ni le phénomène. Nous apportons un test : dans des moniteurs de contrôle sous attaque,
vers quoi le verdict se déplace-t-il — la cible de l'attaquant, la moyenne du corpus ou une valeur propre au moniteur —,
famille par famille, par régression sur des doses, et face à des sondes qui lisent l'agent. Les travaux voisins nous
préviennent que le déplacement peut être du tout ou rien, que le gain change de taille et parfois de signe d'un modèle à
l'autre, et que les modèles les plus forts peuvent ne presque pas bouger. Nous rapportons donc la distribution et pas
seulement la pente, et nous ne revendiquons qu'une stabilité de rang. »

## 9. Contrôle des citations et réserves

- Citations exactes contrôlées par script : **93** ; échecs : **0** (71 trouvées dans le texte en disposition de page,
  22 dans l'ordre de lecture brut, pour les pages à deux colonnes). Compte relevé à la dernière exécution, après écriture.
- Réserve de lecture : cinq pièces ne sont lues que par parties (section 1). Pour elles, « non trouvé » repose sur une
  recherche par mots. 2603.15809 (52 pages) mérite une lecture entière de ses sections 3 à 5 avant le préenregistrement.
- Réserve R4 : aucune des pièces ne donne ses données ; les écarts internes relevés (2607.08066, « The Silent Judge »,
  CaMeL, et ceux déjà notés pour Where Empathy) interdisent d'opposer leurs petits chiffres.
- Réserve R8 : le lot ne contient aucune pièce sur les sondes. Les verdicts « libre » de HC2, HC2b, HC4 ne valent que
  pour ces dix pièces.

## 10. Pièces à récupérer sur le réseau (pistes, non vérifiées)

Références relevées dans les bibliographies des pièces lues ; rien n'en est opposable.
- Version antérieure de 2607.08066 (affiche, atelier « Women in Machine Learning », NeurIPS 2025) : visée par la porte GC,
  absente du PDF lu.
- Rebholz, Biella et Hütter (2024), « Mixed-effects regression weights for advice taking… », Journal of Behavioral
  Decision Making 37(2) (Panin, p. 16) : poids du conseil estimé **par régression** ; à lire pour la pièce (a) et (b).
- Soll et Larrick (2009), « Strategies for revising judgment » (Panin, p. 16) : « choisir ou moyenner », l'analogue humain
  du tout ou rien.
- Kumaran et al. (2026), Nature Machine Intelligence 8(4) (Panin, p. 15) : biais de soutien au premier choix chez des
  juges ; touche v₀.
- Hussain et Nielbo (2026), arXiv 2608.11247 (Panin, p. 15) : « frontière résistance–réceptivité » des parades à la
  conformité ; touche HC5 et HC6.
- Robinson et al. (2026), arXiv 2602.21262, « Under the Influence: Quantifying Persuasion and Vigilance in Large Language
  Models » (Panin, p. 16) : mesure quantitative de la persuasion ; collision possible avec la forme de g.
- Joswin, Medicherla et Mammen (2026), arXiv 2607.00415 (Panin, p. 15) : vue mécaniste de la hiérarchie d'autorité ;
  touche l'opposition juge / sonde.
- Potter et al. (2026), arXiv 2604.19784 (Where Empathy, p. 5) : préservation des pairs par des moniteurs.
- Zhang (2023), arXiv 2305.11888, « Taking Advice from ChatGPT » (Panin, p. 17).
- Références du poids du conseil (Harvey et Fischer 1997 ; Yaniv et Kleinberger 2000 ; Yaniv 2004) : toujours non lues
  sur PDF (R7).
