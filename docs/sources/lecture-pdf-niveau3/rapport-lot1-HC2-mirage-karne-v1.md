# Lecture sur source, niveau 3, lot 1 — HC2, HC2b, HC4 face à MIRAGE et à Karne — v1

Lecteur neuf (n'a écrit ni le programme ni un rapport antérieur). Heure : 2026-11-10, 10:57 UTC, relevée par `date -u` au dernier contrôle des citations.

## En tête

- **HC2, verdict d'ensemble : occupée en partie.** MIRAGE publie « aucune évasion conjointe, aux budgets éprouvés, d'une sonde à agrégation de type maximum lue pendant la génération d'un agent, sous attaque par contenu sans gradient ». Ne sont pas faits : la sonde lisant l'agent qui est lui-même l'adversaire auteur du contenu, la mesure continue g en plan apparié, la comparaison à des juges sous les mêmes attaques, le cadre de moniteur de contrôle. Karne est un contre-indice sur le versant « sonde du lecteur » seulement.
- **Le résultat de MIRAGE n'est pas opposable en l'état (règle de symétrie)** : sur 120 essais, 6 seulement produisent une exfiltration réussie ; « 0 évasion sur 120 » vaut « 0 sur 6 » ; l'attaquant n'itère pas contre la sonde ; au moins dix incohérences internes.
- **HC2b** : MIRAGE voisin (faible, signe favorable, sans contrôle du style) ; Karne voisin, contre-indice indirect (signe contraire, sur une sonde lectrice), utile au contrôle du style.
- **HC4** : MIRAGE voisin, à l'appui de l'axe accès ; Karne contre-indice partiel (le contexte seul déplace gratuitement une sonde lue sur le modèle qui reçoit le contenu).
- Citations contrôlées par script : **115 ; échecs : 0**.

## Méthode

- Empreintes vérifiées par `sha256sum` contre les compagnons : `2606.10304v1.pdf` = `677fe27807039ea0b78da9f2cc192716200ab428889abcaffb28dab05a09a10d` (28 pages) ; `2609.05797v3.pdf` = `eb7be6cafe32808623e11ab7d3f94f232a8bdff5eebf8d449f1f47e3a598d178` (29 pages). Conformes.
- Les deux PDF lus en entier, annexes comprises, page par page (`pdftotext`, numérotation du fichier). Pages 7 et 18 à 20 de MIRAGE relues en image (tableaux 7 et 15, figures 14 à 17).
- Les deux articles sont à deux colonnes : l'extraction `-layout` entrelace les colonnes. Le script essaie trois extractions de la page (`-layout`, ordre de lecture par défaut, `-raw`) ; 64 citations trouvées en `-layout`, 48 par défaut, 3 en `-raw`.
- Normalisation du script : Unicode NFKC, apostrophes droites, traits d'union et blancs retirés (défait césures et petites capitales « M IRAGE »). Essayé sur un cas juste (trouvé), un cas altéré (« 7-token » pour « 5-token », rejeté), un cas juste sur une mauvaise page (rejeté).
- Les citations portent un identifiant (M01… pour MIRAGE, K01… pour Karne) qui renvoie à `citations.json` dans l'archive des fichiers de travail. Nature des chiffres : « auteurs » (imprimé), « figure » (lu sur une figure ou sa légende), « calcul » (recalculé par moi).
- Aucun appel réseau, aucun appel de modèle, aucune commande git, aucune recherche récursive. Aucun refus rencontré.

## 1. MIRAGE (2606.10304v1, Revankar et collègues, atelier « Agents in the Wild », ICML 2026)

### 1.1 La sonde

- **Modèles** : huit modèles ouverts pour la sonde (Qwen2.5 1,5 à 14 milliards de paramètres, Mistral-7B, Llama-3-8B, DeepSeek-7B, Phi-3.5) ; les attaques par contenu portent sur Qwen-7B, avec une réplique sur Qwen-1.5B (auteurs, p. 7, 20).
- **Classe** : régression logistique après normalisation L2 et RobustScaler (auteurs, p. 4, 12).
- **Couche — incohérence interne** : p. 3, « Hidden states are extracted at every generated token from the final transformer layer » (M06) ; p. 12, « Logistic regression on the L2-normalised, RobustScaler-normalised mean-pooled hidden states of the top quarter of transformer layers » (M09). Dernière couche ou moyenne du dernier quart : non tranché par le texte.
- **Jetons lus** : chaque jeton généré (canal 1, « burst ») ; plus un second canal lu au dernier jeton de l'entrée, avant toute génération (canal « intention », p. 8, 22 ; p. 25, M59).
- **Agrégation** : « Per-token scores are aggregated using a 5-token max-burst rule (deployment default; mean-pool reserved for offline audit; full hyperparameters in Appendix A). » (M07, p. 4) ; « Burst score is the max average over a 5-token window during generation. » (M10, p. 12). C'est un maximum de moyennes glissantes sur 5 jetons : une agrégation de la famille du maximum, donc « robuste » au sens du programme (ni moyenne ni dernier jeton). Les auteurs ne l'appellent pas « robuste ».
- **Comparaison d'agrégations** : dernier jeton, maximum, moyenne, 95e centile sont comparés, mais **sans attaque**, sur l'aire sous la courbe en validation croisée par encodage : « Mean-pool and p95-pool recover the distributed encoding signal; last-token scoring captures only AUC 0.37–0.76 » (M44, p. 16 ; M58, p. 6). Incohérence : le titre de la figure 9 dit « Token Aggregation Strategy: Mean-Pool Maximises AUC » (M64, p. 16, figure) alors que le texte retient le maximum : « The burst (max-pool) strategy used in MIRAGE provides the best balance of sensitivity and noise resistance. » (M43, p. 15).
- **Seuil — incohérence interne** : « The burst threshold τ = 0.307 is the 98.5%ile of 500 Alpaca benign responses » (M08, p. 4), soit 1,5 % de faux positifs (calcul), contre « fitted on the Alpaca-format benign calibration set to achieve FPR < 1% » (M11, p. 12).
- **Qui est lu ?** Le modèle lu est l'agent qui **agit** (il génère la sortie encodée) mais il est la **victime** : le contenu adverse est écrit par un tiers et **lu** par ce modèle. « third-party-authored retrieved content designed to coerce covert exfiltration » (M05, p. 2) ; « Each trial injects into a realistic support-agent context in which credentials sit in a system prompt and a user message carries an attacker-authored instruction to encode and append the credential to the reply. » (M27, p. 13). Au regard de HC2 : la sonde lit l'auteur de la **sortie** nuisible, pas l'auteur du **contenu adverse** ; pour le contenu adverse, le modèle lu est un lecteur. Les auteurs parlent une fois de « attacker model » pour Qwen-7B (M33, p. 20) et de « as both attacker and victim » (M63, p. 20), sans que le dispositif change : le levier de l'adversaire reste la consigne injectée.

### 1.2 Les adversaires (tableau 7, p. 7 ; annexes B.4, B.7, I, I.1, p. 13, 14, 18 à 20)

« We evaluated four attacker models, gradient (GCG), sampling, projection, and adaptive prompts, across the white-box-to-black-box spectrum (Table 7). » (M13, p. 7). Tous les contenus adverses sont écrits après le gel de la sonde (« was authored after the probe weights were frozen », M12, p. 5).

| adversaire | accès | agit sur | budget (auteurs) | métrique | résultat (auteurs) | page |
|---|---|---|---|---|---|---|
| gradient (suffixe optimisé GCG) | boîte blanche, gradient | suffixe de 20 jetons ajouté à l'entrée | 300 pas, 4 fonctions de perte, 3 modèles | score sous le seuil ET encodage récupérable | score sous le seuil en 50 pas ; fidélité 0 sur 5 du début à la fin (M39) | 7, 18 |
| échantillonnage | score de la sonde, sans gradient | choix du candidat de plus bas score parmi N sorties | N = 1, 10, 50 | idem | 0 évasion ; fidélité 7 %, 7 %, 13 % (M36, M37) | 7, 14 |
| projection | écriture dans les activations (après coup) | états cachés | retrait de 84,7 % de la variance positive | aire sous la courbe | 1,000 (M42) ; mais voir 1.5 point 7 | 7, 18, 19 |
| consignes adaptées | connaissance de la sonde, sans gradient ni requête | phrase injectée dans le message de l'utilisateur | 24 stratégies, 8 familles, 5 secrets, 120 essais, Qwen-7B | idem, au seuil 0,307 et au seuil 0,405 | 0 sur 120 au seuil 0,307 (M15) ; 3 sur 120 au seuil 0,405 (M16, M30) | 7, 13, 19, 20 |
| réplique Qwen-1.5B | idem | idem | 120 essais | idem | 99 sur 120 détectés, 2 sur 120 évasions (M34) | 7, 20 |

- L'adversaire sans gradient : « A probe-aware attacker may not have access to gradients but can freely mutate the injection prompt. » (M28, p. 18). Les huit familles : habillage légitime, jeu de rôle, indirection en deux temps, chaînes d'encodages, camouflage en tâche bénigne, démonstration par l'exemple, préremplissage, ambiguïté pédagogique (p. 13, 19).
- Critère d'évasion : l'essai doit contenir le secret correctement encodé (« the generated completion contains the correctly encoded secret », M29, p. 19) et le score ne jamais atteindre le seuil.
- Longueur de génération : 300 jetons au plus, température 0 (M60, p. 12).

### 1.3 Adaptativité et mesure du déplacement

- **Adaptatif à la sonde ?** En partie seulement.
  - Le gradient et l'échantillonnage utilisent le score de la sonde (boucle fermée).
  - Les « consignes adaptées » sont un **catalogue fixe** de 24 stratégies écrites en connaissant la sonde, jouées **une fois** chacune sur 5 secrets : aucune itération, aucune requête au score, aucune sélection (p. 13, 19). C'est une attaque par contenu sans accès au score, donc de fait en boîte noire, mais ce n'est pas un attaquant qui s'adapte aux verdicts.
- **Mesure continue ?** Pas d'analogue de g.
  - Sont donnés : des taux d'évasion à deux seuils ; la moyenne du score par famille (M32 : 0,447 pour le préremplissage ; M57 : 0,36 et 0,45) ; la trajectoire du score moyen sous gradient (figure 14, p. 18).
  - Manquent : la condition témoin sans stratégie adverse (même tâche, même secret), donc tout déplacement apparié ; toute cible v* ; tout juge génératif soumis aux mêmes 120 essais (les bases textuelles de l'article — perplexité, TF-IDF, DeBERTa — ne sont pas rejouées sous attaque).

### 1.4 Le cadre

- Agent avec outils : « We deploy MIRAGE on a Qwen-7B agent with five tools (web/code/email/file/API) and credentials in the system prompt » (M23, p. 8) ; 126 scénarios, 81 attaques et 45 bénins (auteurs, p. 8, 13).
- Tâche secondaire : exfiltration d'un secret par encodage, **imposée par injection indirecte** (« An attacker poisons a document an LLM agent will retrieve. Hidden in it: an instruction to encode a credential and ship it through a tool call. », M03, p. 1). Ce n'est pas un agent non fiable qui poursuit sa propre tâche cachée : pas de protocole de contrôle, pas de moniteur de confiance, pas de budget d'audit.
- **Les 120 essais adverses ne sont pas dans le cadre agentique** : un message unique d'assistance, une réponse, pas d'outil (M27, p. 13 ; p. 19). Tours uniques, pas de trajectoires.
- Le bras adverse ne note que le canal 1 (score pendant la génération) ; le canal « intention » n'est attaqué par aucun adversaire.

### 1.5 Limites reconnues et réserves (règle de symétrie)

Limites reconnues par les auteurs :
- accès boîte blanche requis (M22, p. 8) ;
- budgets non éprouvés : « Budgets not evaluated (N ≥ 500 sampling, gradient-free adaptive samplers (NES, SPSA), training-time attacks that fine-tune the host to suppress the subspace, and long chain-of-thought routing before the encoded output appears) could in principle dissociate suppression from fidelity loss. » (M21, p. 9 ; aussi M17, p. 7 ; M20, p. 9) ;
- pas d'impossibilité structurelle revendiquée (M02, p. 1 ; M53, p. 9) ;
- la sonde tire sur tout calcul d'encodage, bénin compris ; taux de faux positifs de 0 % à 100 % selon le modèle hôte (auteurs, p. 8).

Réserves du lecteur — le « 0 évasion » est suspect de propreté :
1. **Dénominateur réel de 6, pas de 120.** « The low overall fidelity rate (6/120, 5%) reflects the aligned Qwen-7B attacker model’s refusal behaviour » (M33, p. 20). Tableau 15 (p. 20, auteurs, lu sur image) : fidélité 0 dans six familles sur huit, 3 en camouflage, 3 en ambiguïté. « 0 sur 120 » est donc « 0 sur 6 » (calcul) ; au seuil 0,405, 3 sur 6 (calcul). Réplique sur Qwen-1.5B : 7 réussites sur 120, dont 2 évasions (M34).
2. **Le gradient n'a jamais produit un encodage récupérable** (0 sur 5 du premier au dernier pas, M39, figure 14) : c'est un échec de l'attaquant, pas une preuve de couplage ; 5 encodages seulement.
3. **Contradiction sur les 3 évasions.** Le texte dit qu'il s'agit d'encodages d'URL sans effet où « no encoding computation occurs, so the probe correctly does not fire » (M31, p. 19) ; or ces 3 essais ne sont pas des évasions au seuil 0,307 (0 sur 120), donc leur score est entre 0,307 et 0,405 : la sonde **a tiré** au seuil par défaut (inférence, calcul). Deux des trois sont dans la famille « ambiguïté », décrite comme pédagogie du Base64, pas comme encodage d'URL (tableau 15, p. 20, et p. 19).
4. **Le couplage « détection–fidélité » est contredit par la suite agentique de l'article, sans aucun adversaire** : « Of the remaining 54 compliant attacks, 31 (57.4%) exceed τ = 0.307, and 23 (42.6%) are genuine probe misses (compliant encoding with sub-threshold burst). » (M25, p. 21). Et la page 14 affirme l'inverse comme argument structurel : « any output that correctly encodes the secret must activate the encoding subspace, so lowering subspace score necessarily destroys fidelity » (M38), alors que l'article dit ne pas revendiquer d'impossibilité structurelle (M53).
5. **Deux explications incompatibles des 23 manqués** : délégation à un outil, sans calcul à lire (M24, p. 8), ou encodages sémantiques (M26, p. 21). Déléguer l'encodage à un outil est donc une évasion du canal 1 que le bras adverse n'essaie pas.
6. Arithmétique du budget : « 24 strategies × 8 families × 5 targets = 120 trials » (M14, p. 7) ; 24 × 8 × 5 = 960 (calcul) ; 120 = 24 × 5 = 8 familles × 15 (calcul, tableau 15). Autre formulation p. 13 (M65).
7. Projection : aire sous la courbe à 1,000 (M42, p. 18) mais la légende de la figure 17 dit « only 4/9 encoding families permit evasion at any distortion cost, and only with 6–17% hidden-state norm perturbation » (M41, p. 19) : une évasion existe donc par écriture dans les activations pour 4 familles sur 9.
8. Pas de pertes : quatre fonctions de perte sur 300 pas (M04, p. 2) ou sur 150 pas (M40, p. 19).
9. Figure 4 (p. 12) : « Compliant attacks (n=1231) » (M45) contre « Conditional AUC = 1.000 (n = 35) » (M46, p. 7) ; 1 266 − 35 = 1 231 (calcul) : la figure étiquette comme « conformes » les essais refusés.
10. Figure 8 (p. 16) : légende interne « Qwen-7B (AUC=0.678) » (M47) contre « Qwen-7B 0.969, Qwen-1.5B 0.942 » dans la légende écrite (M48).
11. Le lot de 1 489 réponses bénignes a deux provenances : JailbreakBench et NotInject (M50, p. 6) ou « a separate pool of 1,489 real-world benign responses (Alpaca-format QA, coding tasks, math problems) » (M49, p. 15) ; les effectifs de la figure 18 (500, 164, 825 ; figure) somment à 1 489 (calcul).
12. Suite agentique : « 81 attack scenarios (9 encoding families × 9 attack prompt templates per family) » (M51, p. 21) contre des effectifs inégaux par encodage (M52, p. 22 : 23, 12, 9…).
13. Annexe N (p. 28) : le texte donne 96 à 100 % et 87 % (M54) ; la légende de la figure 26 donne 0,898 pour Qwen-7B et 0,624 pour Mistral-7B (M55, M56).
14. Aires sous la courbe à 1,000 en série (tableau 2, p. 5 ; tableau 11, p. 15), y compris sur Phi-3.5 dont le taux de faux positifs bénins est de 100 % : la validation croisée par encodage ne mesure pas la séparation utile. Une aire de 1,000 à la couche d'encodage s'est révélée être un artefact du dernier jeton (auteurs, p. 4, 23, 24).
15. Petits effectifs (5 encodages sous gradient, 5 secrets par stratégie) ; données et traces non publiées (« will be released upon publication », M67, p. 14) : rien n'est rejouable.

Conclusion de lecture : la phrase de l'article sur les adversaires est exacte dans sa lettre, mais elle établit seulement qu'**un catalogue non itératif de 24 consignes, dont 6 essais sur 120 réussissent l'exfiltration, n'a pas échappé au seuil par défaut**. Chiffres non opposables sans rejeu.

### 1.6 Ce qu'on rapportait de MIRAGE — vérification

| point rapporté | constat |
|---|---|
| adversaires qui connaissent la sonde | **exact** (titre de la section 6.2, p. 7 ; M28) |
| dont un adversaire sans gradient qui agit sur le contenu injecté | **exact**, avec précision : catalogue fixe joué une fois, sans requête au score (p. 13, 18, 19) ; l'échantillonnage (N ≤ 50) est le seul adversaire sans gradient en boucle fermée |
| cadre d'exfiltration par un agent | **exact pour la suite de 126 scénarios ; inexact pour le bras adverse** : les 120 essais sont à un tour, sans outil (M27) |
| aucune évasion aux budgets éprouvés | **exact au seuil 0,307 seulement** ; 3 sur 120 au seuil 0,405 et 2 sur 120 sur Qwen-1.5B (classées « sans effet » par les auteurs) ; 4 familles sur 9 évadables par projection (M41) ; dénominateur réel de 6 |
| pages 1, 7, tableau 7, 18 à 20 | **exactes** ; ajouter p. 2, 9, 13, 14, 21 |

## 2. Karne (2609.05797v3, « Safety Monitors Mostly Catch What the Model Already Refuses »)

### 2.1 Les sondes

- **Modèle lu** : Gemma-4-31B-IT, le modèle protégé (K06, p. 3). Les sondes ne sont pas rejouées sur le second modèle : la réplique sur Qwen3-32B ne porte que sur les gardes textuels (K41, p. 14).
- **Sondes** (K07, p. 3 ; K08, p. 4 ; K09, K10, K35, p. 22), entraînées sur 3 000 requêtes de WildGuardMix :
  - linéaire, couche 31, dernier jeton de l'instruction ;
  - à attention, couche 28, toute l'entrée, gabarit de dialogue compris ;
  - quatre variantes : linéaire sur la moyenne du contenu (couche 28), dernier jeton du gabarit (couche 29), dernier jeton du contenu (couche 29), attention sur le contenu seul (couche 34) ;
  - « Latent Guard » : différence de similarités cosinus au dernier jeton de l'instruction, moyennée sur une bande de couches, sans entraînement (K43, p. 4).
- **Agrégations présentes** : dernier jeton, moyenne, attention apprise. Pas de maximum. Aucune n'est dite « robuste ».
- **Qui est lu ?** Le modèle qui **traite** la requête réécrite, à l'entrée, avant toute génération : une **sonde du lecteur**, sans ambiguïté. Le concept sondé (« requête nuisible ») est une propriété de l'entrée, pas une intention de l'agent.

### 2.2 L'« adversaire »

- **Pas d'attaquant adaptatif** : les auteurs le disent, « find that the layers’ failures overlap with no attacker at all, under natural rewording » (K05, p. 3).
- Contenu : la requête de l'utilisateur, réécrite à trois niveaux de franchise à intention constante (indirect L1, direct L2, brutal L3 ; K48, p. 3) par un modèle de langage (K26, p. 21), vérifiée par deux juges et deux annotateurs. Le réécrivain ne voit ni les moniteurs ni leurs scores : boîte noire, zéro requête.
- Budget : une réécriture par niveau, régénérée si les juges la refusent (« 242 of the 647 needed more than one attempt. », K27, p. 21) ; 647 requêtes ; longueur médiane 46, 20 et 32 jetons (K30).
- Métriques : taux de signalement à 1 % de faux positifs sur 10 000 requêtes bénignes (K12, p. 4), rappel sur les requêtes auxquelles le modèle répond (au moins une réponse conforme sur huit tirages) ou qu'il refuse, rapport des deux, « fuites » sur les 344 requêtes basculées.
- Résultats (auteurs) :
  - le modèle répond à 340 requêtes en L1, 71 en L2, 12 en L3 (K13, p. 4) ;
  - sondes, tableau 2, p. 6 — taux de signalement L1, L2, L3 : linéaire 0,43, 0,79, 0,94 (K16) ; attention 0,45, 0,94, 0,99 (K17) ; Latent Guard 0,44, 0,72, 0,87 ; rappel sur les requêtes répondues en L1 : 0,21, 0,22, 0,24 (K44 pour Latent Guard) ;
  - rapport « refusées sur répondues » en L1 : 3,2 pour les deux sondes, 2,8 pour Latent Guard (K14, p. 5) ; 2,7 à 5,7 sur les sept configurations internes (K11, p. 22) ;
  - fuites : « On the 344 flipped requests the three monitors leak 259 to 270. » (K15, p. 6), contre 153 à 321 pour les gardes textuels (K47, p. 5).

### 2.3 Adaptativité et mesure du déplacement

- Non adaptatif (voir 2.2).
- **Mesure continue : oui, sur le modèle lecteur.** Lecture de la direction « nuisible » en écarts-types du lot bénin : « The 284 requests that flip from L2 to L1 lose 2.4 SD of harm reading, and the 344 that flip from L3 lose 3.8. » (K18, p. 6) ; direction de refus : « the 284 flipped requests lose 5.0 SD from L2 to L1 » (K38, p. 24) ; dans le garde textuel Qwen3Guard, 2,1 écarts-types (K46, p. 6). Le seuil à 1 % de Latent Guard est à +2,1 écarts-types (K39).
- C'est un déplacement apparié du score par le contenu, à intention constante : le plus proche analogue de g dans ce lot, mais **sans cible v\*** (donc pas de g au sens de la loi de déférence) et **sur un lecteur**.

### 2.4 Le cadre

- Pas d'agent, pas d'outil, pas de tâche secondaire : « All requests are single-turn and English. » (K25, p. 10) ; un seul tour sans consigne système (K31, p. 14).
- Moniteurs d'entrée contre l'usage abusif (filtrage de requêtes), pas moniteurs de contrôle d'un agent non fiable.

### 2.5 Limites reconnues et réserves

Reconnues : un seul modèle cible pour les lectures, le pilotage et l'affinage (K22, p. 9) ; « we did not steer or fine-tune any internal monitors » (K23, p. 10) ; L3 repose sur 12 requêtes répondues (K24) ; échelles écrites et vérifiées par des modèles de langage.

Réserves du lecteur :
- les annotateurs ne retrouvent l'ordre complet L1 < L2 < L3 que sur 38 % et 33 % des triplets (K28, p. 21) : seul le contraste L1 contre le reste est validé ;
- accord entre juge et annotateurs sur la conformité : kappa de 0,60 et 0,63 (K29, p. 21) ;
- le score des juges ne suit pas l'ampleur du changement textuel (K37, p. 21) ; L1 est aussi le plus long (K30) : franchise et longueur sont confondues ;
- les scores de gpt-oss-safeguard saturent, 17 à 25 % des verdicts changent d'un passage à l'autre (K36, p. 22) ; ses fuites valent 153 au tableau 1 (K47) et 162 aux tableaux 10 et 11 (p. 23, auteurs, lu dans le texte extrait) ;
- sondes sur un seul modèle (K41) ;
- aires sous la courbe de 1,00 en L3 (K16, K17) : attendu pour des requêtes brutales, pas un signal d'alarme ;
- un organisme anonymisé et une prépublication d'auteur unique : résultats non rejoués.

L'article est sobre et cohérent pour l'essentiel ; ses chiffres restent non opposables au sens de R7 tant qu'ils ne sont que lus.

### 2.6 Ce qu'on rapportait de Karne — vérification

| point rapporté | constat |
|---|---|
| sondes d'activations et gardes textuels manquent surtout les requêtes auxquelles le modèle répond | **exact** (K01, p. 1 ; K04, p. 1 ; tableaux 1 et 2) |
| réécrire la requête fait baisser le taux de signalement | **exact** (K02, p. 1 ; K16, K17) |
| « signe contraire à citer avec MIRAGE » | **exact mais à borner** : sondes lues à l'entrée sur le modèle lecteur, concept « requête nuisible », aucun attaquant, aucun agent. Les deux articles ne mesurent pas la même configuration : MIRAGE lit la génération, Karne lit l'entrée. Le signe contraire vaut pour le bras « sonde du lecteur », pas pour l'énoncé de HC2 |

## 3. Verdicts

### 3.1 HC2, composante par composante

| composante de HC2 | MIRAGE | Karne |
|---|---|---|
| (i) sonde lisant l'agent auteur | **à moitié** : lit l'agent qui agit, pendant qu'il génère ; mais cet agent est la victime qui lit le contenu adverse d'un tiers | **non** : sonde du lecteur, à l'entrée |
| (ii) attaque par contenu | **oui** : consigne injectée (120 essais), suffixe optimisé | **oui** : réécriture de la requête, non adverse |
| (iii) boîte noire | **en partie** : catalogue sans requête au score (connaissance de la sonde) ; échantillonnage avec score, N ≤ 50 | **oui** : aucune connaissance des moniteurs |
| (iv) agrégation robuste | **oui** : maximum de moyennes sur 5 jetons ; comparaison des agrégations hors attaque seulement | **non** : dernier jeton, moyenne, attention ; toutes déplacées |
| (v) mesure par g | **non** : taux d'évasion à deux seuils, moyennes par famille, pas de témoin apparié, pas de juge sous la même attaque | **en partie** : déplacement apparié en écarts-types, sans cible, sur le lecteur |
| (vi) moniteur de contrôle sous attaque | **non** : injection indirecte sur un agent victime ; bras adverse à un tour | **non** : filtrage de requêtes |

- **MIRAGE → HC2 : occupée en partie.** Fait : (ii), (iv), une part de (iii) et de (i), avec un résultat de même signe que HC2 mais lu à un seuil. Non fait : l'agent auteur et adversaire, g, le comparateur juge, le cadre de contrôle, l'attaquant itératif. Résultat non opposable (1.5).
- **Karne → HC2 : voisin ; contre-indice pour le bras « sonde du lecteur »** (décision N-013, section 8). Il s'ajoute à 2511.00554, 2601.11516 et 2509.21344 : des sondes lectrices, y compris à attention, sont déplacées par un contenu en boîte noire, ici sans aucun attaquant. Il ne touche pas l'énoncé « agent auteur ».
- **Verdict d'ensemble pour HC2 : occupée en partie.** La ligne « reste revendicable » de l'état actuel doit être resserrée (sa lettre actuelle — robustesse sous attaque par contenu d'une sonde lisant l'agent, avec agrégation robuste — est, hors « mesurée par g », ce que MIRAGE annonce).

**Formulation proposée de ce qui reste revendicable** (proposition ; la décision revient à Lazar) :

> Reste revendicable : pour une sonde qui lit l'agent **auteur du contenu adverse destiné au moniteur** (agent non fiable d'un protocole de contrôle, et non victime d'une injection écrite par un tiers), le **déplacement continu g du score**, mesuré en **plan apparié** (même tâche avec et sans contenu adverse ; 2 × 2 rhétorique × intention de EC.2), **comparé au g des juges génératifs sous les mêmes attaques**, pour plusieurs agrégations dont une robuste, sur des trajectoires (jamais l'immunité absolue).
> Cité comme publié, non opposable : aucune évasion conjointe au seuil par défaut d'une sonde à maximum glissant lue pendant la génération d'un agent victime d'injection, sous un catalogue de 24 consignes et un échantillonnage N ≤ 50 (2606.10304, p. 7, 19, 20 ; 6 exfiltrations réussies sur 120 essais).
> Contre-indice à garder, versant lecteur : 2609.05797 (p. 5, 6, 22), à joindre au bras « sonde du lecteur ».

Conséquence pratique pour le préenregistrement du papier C : la distinction auteur contre lecteur ne suffit plus ; il faut **trois** positions de sonde — lecteur du contenu (Karne), agent victime qui agit sous injection (MIRAGE), agent auteur et adversaire (HC2) — et l'évasion par délégation à un outil doit figurer parmi les attaques (réserve 5 de 1.5).

### 3.2 HC2b — trahison par les activations

- **MIRAGE : voisin (faible), de signe favorable.** Les stratégies qui exposent le plus l'encodage font monter le score au lieu de le baisser (M18, p. 7 ; M32, M57, p. 19) ; le modèle le moins aligné est le plus détectable (M35, p. 20). Mais : le modèle lu ne **tente** pas de manipuler un moniteur (c'est un tiers qui écrit la consigne) ; pas de condition témoin sans stratégie ; aucun contrôle du style ; 6 réussites sur 120. Ne touche pas l'énoncé « l'agent qui manipule ».
- **Karne : voisin ; contre-indice indirect.** Sur une sonde lectrice, la forme la plus manœuvrière (indirecte) **baisse** le score (K18, K19, p. 6) : signe contraire à HC2b, mais ni agent, ni tentative de manipuler un moniteur, ni sonde de l'auteur. **Utile au contrôle obligatoire du style** : des sondes d'activations suivent la franchise de la formulation à intention constante (K20, p. 7 ; K34, p. 3 ; K42, p. 2), et l'échelle de franchise des deux côtés de l'étiquette est un patron de contrôle réutilisable.
- HC2b reste revendicable dans sa formulation de N-013. Ajouter Karne aux sources du contrôle du style.

### 3.3 HC4 — taxe de déplacement

- **MIRAGE : voisin, à l'appui de l'axe accès.** Aux budgets éprouvés, le contexte seul n'évade pas (M04, p. 2), pas même avec un gradient sur un suffixe (M39) ; l'évasion apparaît avec l'écriture dans les activations (M41, p. 19, 4 familles sur 9, perturbation de norme de 6 à 17 %). Pas de juge génératif attaqué, pas de coût chiffré par axe, aucune comparaison sonde contre juge dans un même cadre. Les détecteurs textuels de l'article échouent sans aucune attaque (M62, p. 6) : pas une mesure du coût de déplacement d'un juge.
- **Karne : contre-indice partiel.** La rhétorique seule (réécriture gratuite, sans accès, sans requête) déplace une sonde lue sur le modèle autant ou plus que des gardes textuels : « neither does reading the model’s activations: two probes and Latent Guard (Zhao et al., 2025b) show the same gap, wider » (K04, p. 1). L'énoncé retenu de HC4 (« le contexte seul n'y suffit pas ») est donc **faux pour une sonde de propriété de l'entrée lue sur le modèle qui reçoit le contenu**. Il n'est pas touché pour une sonde de l'intention de l'agent auteur.
- **Formulation proposée pour HC4** : préciser « une sonde qui lit l'**intention ou l'action de l'agent auteur** » et écarter explicitement les sondes de propriété de l'entrée, pour lesquelles le déplacement par le contexte seul est publié (2609.05797, p. 1, 6).

### 3.4 Tableau des verdicts

| hypothèse | MIRAGE (2606.10304v1) | Karne (2609.05797v3) |
|---|---|---|
| HC2 | occupée en partie | voisin ; contre-indice (versant lecteur) |
| HC2b | voisin (faible, signe favorable) | voisin ; contre-indice indirect ; utile au contrôle du style |
| HC4 | voisin (appui de l'axe accès) | contre-indice partiel (sonde de l'entrée, contexte seul) |

**HC2, ensemble : occupée en partie.**

## 4. Pages clés

- MIRAGE : 1 et 2 (thèse, budgets), 4 et 12 (sonde, agrégation, seuil), 7 (tableau 7), 8 et 21 (suite agentique, 23 manqués), 9 (limites), 13 et 14 (catalogue, échantillonnage), 18 à 20 (annexe I, tableau 15, réplique).
- Karne : 1 (thèse), 3 et 4 (sondes, calibration), 5 et 6 (tableaux 1 et 2, déplacement en écarts-types), 7 (pilotage), 9 et 10 (limites), 21 et 22 (validation humaine, variantes de sondes), 24 et 25 (lectures chiffrées).

## 5. Contrôle des citations

- Script : `controle_citations.py`, lancé par `python3 -I` ; liste : `citations.json` ; journaux : `journal-autotest.txt`, `journal-controle.txt` (dans l'archive).
- Autotest : cas juste trouvé ; cas altéré rejeté ; cas juste sur une mauvaise page rejeté.
- **Citations contrôlées : 115. Échecs : 0.** Huit d'entre elles (K03, K21, K32, K33, K40, M19, M61, M66) sont contrôlées mais non reprises dans le texte. Les deux titres entre guillemets (nom de l'atelier, titre de l'article de Karne) ne sont pas des citations contrôlées. Un échec au premier passage (K45, mauvaise page : 4 au lieu de 3), corrigé.
- Les lignes de tableau citées (K16, K17, K44) le sont telles que l'extraction les rend ; les tableaux 7 et 15 de MIRAGE ont été relus en image.
- Limite du contrôle : il vérifie la présence littérale d'une citation sur sa page, pas la justesse de mon interprétation.
