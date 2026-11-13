# Contre-lecture du rapport du lecteur — Tr, « transposition du jeton à l'action » (papier A) — v1

- **Écrite le** : 2026-11-13T23:25:25Z (heure relevée par `date -u` dans la commande qui l'a inscrite). Contre-lecture commencée à 2026-11-13T23:15:17Z (`date -u`, relevée au début du travail).
- **Rôle** : contre-lecteur (rôle adverse). **Modèle** : modèle B. L'auteur du rapport est le modèle A ; A ≠ B.
- **Objet** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-Tr-v1.md`, empreinte vérifiée `d04e2ef3660e50e1542e4b11e548897c6efe7516fc1f3c51d61a813df5f6a670` (conforme) ; son archive `fichiers-de-travail-Tr-v1.tar`, empreinte vérifiée `c0805da602799ec12157339d627b2be97f5f6294edef6e146e450cb1668c1cd7` (conforme), extraite dans le dossier de travail.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme), lue en entier.
- **Noms de modèles** : aucun n'est écrit ici ; les modèles des pièces sont désignés par leur rôle ou leur taille.

## Déclarations (à lire d'abord)

- **Fichier non ouvert** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`. La consigne commune le place dans la « méthode du lecteur » ; mon mandat borne mes lectures aux fichiers qu'il nomme (« et seulement ceux-là ») et ne le nomme pas. J'ai tenu la borne du mandat et les interdits de la consigne commune et du mandat. Si ce fichier porte un interdit plus strict, je ne l'ai pas lu : à vérifier par le compte 2.
- **Liste d'un dossier** : j'ai listé (sans récursion, sans ouvrir aucun fichier) le dossier de sortie `docs/sources/lecture-pdf-niveau3/compte-2/` pour vérifier que mes chemins de sortie étaient libres. Aucune recherche récursive dans le dépôt.
- **Fichier lu par le lecteur et non par moi** : `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (l. 130 à 151), hors de mon mandat. Ce que le rapport en tire (« déjà lu au niveau 2 », pour McKenzie et al.) n'est pas vérifié ici.
- Aucune commande git, aucun appel réseau, aucun appel de modèle, aucune dépense. Aucun refus de permission. Aucune ouverture fautive.

## Empreintes des PDF (vérifiées contre les compagnons `.sha256`, toutes conformes)

| pièce | fichier | pages | sha256 |
|---|---|---|---|
| « Constitutional Classifiers++ » | `lot11/2601.04603v1.pdf` | 17 | `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` |
| « Monitoring Emergent Reward Hacking During Generation via Internal Activations » | `lot10/2603.04069v1.pdf` | 14 | `4c035a3c362fbaa36ba8ad1127249566e216d8ccb567f0375707d409e139895f` |
| « Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations » | `lot10/2609.19101v2.pdf` | 39 | `c8ab50452ea3effc7865bb6b53f4c6159b150cafcd1864e3103f4da877f8ae3f` |

## Fichiers lus (liste exacte) et étendue

- La consigne commune (en entier) ; le rapport du lecteur (en entier) ; l'archive du lecteur (journal, script, fichier des citations, sortie du contrôle).
- `docs/programme-controle-ia-v2.md`, lignes 85 à 125 et 180 à 200.
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 183 à 191.
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 442 à 471.
- Les trois PDF et leurs compagnons `.sha256`. Aucun autre PDF, aucun autre fichier du dépôt.

Étendue réellement lue par PDF (`pdftotext -layout`, page par page) :
- **2609.19101v2** : p. 1 à 18 et p. 25 à 39 ligne à ligne (annexes A à C, tableaux 2 à 4, les quatre grilles des juges, figures 17 à 23) ; p. 19 à 24 (références) lues titre par titre ; p. 9, 10 et 11 relues sur l'image (figures 7 à 11) ; recherche par mots sur les 39 pages (mise en commun, agrégation, moyenne, maximum, dernier jeton, attention, fenêtre, lissage, pic, décile, classement ; obfuscation, adversaire, évasion, attaque, équipe rouge, robuste, suppression, effacement, illisible, surveillé).
- **2601.04603v1** : p. 1 à 17 ligne à ligne, références comprises (p. 11 à 13) ; p. 7 et p. 16 relues sur l'image (figures 2 et 5) ; recherche par mots (moyenne mobile exponentielle, coefficient, décroissance).
- **2603.04069v1** : p. 1 à 14 ligne à ligne, références comprises ; figures lues par leurs légendes et leurs axes rendus en texte, non sur l'image.

**Citations contrôlées par programme : 70 ; échecs : 0.** Script écrit par moi (indépendant de celui du lecteur), testé d'abord sur un cas juste (réussi) et sur trois cas altérés (texte changé, page fausse, empreinte fausse : trois échecs, comme attendu). Les 49 citations du lecteur, repassées par mon script : 49 réussies, 0 échec. Fichier `citations-contre-lecture-Tr-v1.json` dans l'archive seulement.

---

## Verdicts (toute occupation, même partielle, en tête)

**Verdict sur le rapport : tient avec corrections.** Les faits rapportés sont exacts sur toutes les pages que j'ai relues ; aucune collision sur le noyau de Tr n'a été manquée ; mais le rapport sous-classe trois composantes faites, sa formulation « revendicable » ne sépare pas proprement de 2601.04603, deux des bases qu'il propose pour E1.5 ne sont pas imprimées telles quelles, et un voisin direct du bras d'attaque par les poids n'est pas listé.

**Mon verdict sur Tr, table fermée : occupé en partie.** Divergence avec le lecteur (« non trouvé dans les pièces lues ») : elle porte sur la lettre de la table, pas sur les faits. Elle est à arbitrer.

- **Faites, hors du noyau** (trois composantes, deux pièces) :
  1. Lecture d'une sonde par jeton au grain du passage (un canal d'un pas, appels d'outil compris) dans de longs déroulés d'agents, avec détection mesurée à ce grain, et usage de la sonde au grain du déroulé ; sans attaquant ; une seule règle, non imprimée (2609.19101, p. 6, 9, 10, 31).
  2. Attaquant humain adaptatif, en boîte noire, par le contenu, contre un système dont la première porte est une sonde lissée au fil des jetons ; au grain de l'échange, hors agent ; une seule règle, résultat non attribué à la règle (2601.04603, p. 9, 15).
  3. Comparaison de variantes de lissage du score de sonde, au grain du jeton vers l'échange, sur des attaques humaines transférées (non adaptées aux règles comparées) (2601.04603, p. 7, 16).
- **Noyau : non trouvé dans les pièces lues.** Aucune des trois pièces ne compare des règles d'agrégation de scores de sondes au grain de l'action ou de la trajectoire d'un agent ; aucune n'oppose un attaquant adaptatif à une sonde à ce grain ; aucune n'accumule séquentiellement des scores de sondes sur une trajectoire ; aucune ne porte du jeton à l'action une conclusion de robustesse. J'ai cherché pour trouver : rien dans le corps, les annexes, les tableaux ni les légendes.
- **Pourquoi « occupé en partie » et non « non trouvé »** : la consigne définit « occupée en partie » par « composantes faites, non faites » ; avec les constats B, C et E ci-dessous, trois composantes de l'énoncé tel que le programme l'écrit (l. 98 : niveau jeton, niveau action et trajectoire, attaquant adaptatif) ont de la matière faite. Le lecteur lui-même classe (e) « occupée » et prévient qu'on peut le contester. Si le compte 2 retient la convention du niveau 3 (les agrégations au niveau de l'action sans attaquant y sont dites « voisins », l. 186 de l'état de l'art), la valeur « non trouvé dans les pièces lues » se défend **pour le seul noyau**, à condition que les trois composantes faites soient écrites à côté. Les deux lectures donnent la même pièce libre ; elles ne donnent pas la même étiquette.
- **Condition commune aux deux lectures** : le verdict vaut pour trois pièces. Deux voisins non lus peuvent le renverser : Wilhelm et Kao 2026 (2609.19101, p. 17 et 24) et « What the Monitor Saw » (état de l'art du niveau 3, l. 188-189). Tant qu'ils ne sont pas lus, la pièce libre ne se dit que « non trouvée dans les pièces lues ».

---

## Constats

### A — majeur — La formulation « ce qui reste revendicable » ne sépare pas de 2601.04603 et se lit à contresens

Texte du rapport (l. 164) : « … aucune ne compare, au grain de l'action d'un agent (un appel d'outil ou un pas) ni de la trajectoire, des règles d'agrégation de scores de sondes face à un attaquant adaptatif qui connaît ou apprend le moniteur et sa règle d'agrégation ; … ».

Deux défauts.
1. Le qualificatif « qui connaît ou apprend le moniteur et sa règle d'agrégation » est posé pour écarter 2601.04603, et ne l'écarte pas : l'équipe rouge itère contre le système défendu avec retour (« We provide red-teamers with API access to the defended model. », p. 15), sur environ 198 000 tentatives (p. 9, auteurs) ; elle apprend le moniteur par l'usage. Ce qui sépare Tr de cette pièce est le grain (action et trajectoire d'un agent), la comparaison de règles, l'accumulation séquentielle et l'attaque par les poids — pas le savoir de l'attaquant.
2. La phrase attache « face à un attaquant adaptatif » à la comparaison : un lecteur comprend que la comparaison existe sans attaquant. Or elle n'existe dans aucune des trois pièces, avec ou sans attaquant, au grain de l'action.

Texte corrigé proposé (formulation de ce qui reste revendicable ; ce n'est pas la phrase publique, rôle exclu) :
> « Non trouvé dans les trois pièces lues : (1) une comparaison de règles d'agrégation de scores de sondes (maximum, moyenne, lissage, pondération de type attention, accumulation séquentielle) au grain de l'action d'un agent (un pas, un appel d'outil) ou de sa trajectoire, avec ou sans attaquant ; (2) un attaquant adaptatif, par le contenu ou par les poids, opposé à une sonde à ce grain ; (3) une conclusion de robustesse portée du grain du jeton au grain de l'action. Trouvé dans ces pièces, donc non revendicable : la lecture d'une sonde par jeton au grain du pas et du déroulé d'un agent, sans attaquant (2609.19101) ; l'épreuve d'une sonde lissée au fil des jetons par des humains adaptatifs, en boîte noire, au grain de l'échange (2601.04603) ; la comparaison de lissages sur des attaques transférées, au grain du jeton (2601.04603). »

### B — majeur — 2601.04603 : « la sonde seule n'est jamais attaquée » est trompeur ; la composante (d) est faite en partie, à un autre grain

Texte du rapport (l. 65) : « aucune attaque n'est conçue contre le lissage ou le seuil en flux ; aucune comparaison d'agrégations sous cette attaque ; la sonde seule n'est jamais attaquée. » Verdict du rapport sur (d) : « voisin ».

Relecture des pages (p. 6, 7, 9, 15) :
- Dans le système de production, la sonde est la seule première porte : « A lightweight linear probe monitors all exchanges during generation. » puis « When the probe score exceeds a threshold, the exchange is escalated to a second-stage external classifier. » (p. 9). Pour la cascade de la section 5.3 : « Otherwise, we rely solely on the probe. » (p. 9). Un échange non monté n'est lu par rien d'autre.
- Le score de la sonde est lissé au fil des jetons (« During inference, we use an exponential moving average », p. 6, cité par le lecteur) et la décision se prend en un point quelconque de la génération (p. 7).
- L'équipe rouge applique « the same red-teaming methodology described in previous sections » (p. 9), avec accès par interface de programmation (p. 15).

Conséquence logique (lecture du contre-lecteur, non imprimée) : toute attaque réussie contre ce système a soit tenu le score lissé de la sonde sous le seuil de montée à chaque jeton, soit été montée puis a battu la combinaison pondérée. La règle « score lissé au fil des jetons, seuil franchi en un point quelconque » est donc dans la boucle de chaque tentative. De fait, c'est un attaquant adaptatif (humain, boîte noire, par le contenu) contre **une** règle d'agrégation de scores de sonde. Autre élément non relevé : une alarme coupe la génération (« a single flag blocks all subsequent content », p. 6, cité par le lecteur) ; le point de coupure est un retour d'information sur la position où le score lissé a franchi le seuil (inférence du contre-lecteur ; la pièce ne dit pas que les attaquants l'exploitent).

Dans l'autre sens, et le rapport a raison sur ces points : une seule règle, aucune comparaison de règles sous cette attaque ; aucune connaissance déclarée de la sonde ; aucune attaque par les poids ; résultat mesuré au grain du système (une vulnérabilité à haut risque, « Only one high-risk vulnerability was discovered », p. 9), non attribué à la règle ; grain de l'échange (« Crucially, these labels are exchange-level labels », p. 5) ; aucun agent, aucun pas, aucun appel d'outil.

Non relevé non plus : d'autres équipes ont attaqué des versions du système (« We also thank UK AISI, US CAISI, and FAR.AI for red teaming various versions of our system. », p. 11) ; rien n'est rapporté de leurs résultats.

Texte corrigé proposé (tableau de la pièce 1, ligne (d)) :
> « (d) attaquant adaptatif | **occupée en partie, à un autre grain que celui de Tr** : des humains adaptatifs, en boîte noire, par le contenu, attaquent un système dont la première porte est une sonde lissée au fil des jetons ; toute attaque réussie a donc passé sous cette règle (lecture). Non fait : comparaison de règles sous attaque, attaquant informé, attaque par les poids, grain de l'action, agent, attribution du résultat à la règle | p. 6, 7, 9, 15 »
et suppression de « la sonde seule n'est jamais attaquée », remplacé par : « la sonde n'est jamais attaquée isolément ; elle l'est comme première porte du système de production ».

### C — majeur — 2601.04603 : la comparaison des lissages n'est pas « pas sous attaque » ; elle porte sur des attaques humaines transférées, et le contre-indice n'est pas « léger »

Texte du rapport (tableau, ligne (a)) : « comparaison sur données statiques, pas sous attaque » ; « contre-indice léger ».

- Les « données statiques » sont des attaques : « We assess robustness using a dataset of jailbreaks collected from human red-teaming, comprising approximately 7,000 exchanges » ; « We use only exchanges produced by red-teamers whose exchanges were never used for classifier training. » (p. 7). Elles ont été produites par des humains adaptatifs contre d'autres systèmes, puis rejouées : attaques transférées, non adaptées aux règles comparées. Le rapport le dit au fil du texte (l. 61) et le perd dans son tableau.
- La comparaison de la figure 5b (p. 16) est, de fait, une comparaison de règles de décision. La défense est comptée si le classifieur « flags at any point during model sampling » (p. 7) : avec une fenêtre de 1 jeton, la règle est le maximum des scores bruts par jeton ; avec une fenêtre de 16, le maximum d'un score lissé. Valeurs lues sur la figure 5b (figure) : fenêtre 1, environ 0,041 ; 2, environ 0,027 ; 4, environ 0,022 ; 8, environ 0,026 ; 16, environ 0,014 ; 32, environ 0,020 ; 64, environ 0,060. La barre « fenêtre 1 » de la figure 5b et la barre « pondération seule » de la figure 5a (environ 0,04, figure) coïncident, ce qui confirme la lecture (calcul).
- Le contre-indice à la prémisse de Tr (« la robustesse des agrégations max et attention, établie au niveau token », programme l. 98) est imprimé deux fois : par le motif (« Without averaging, a single token with a spuriously high activation could incorrectly flag an entire sequence as harmful. », p. 6) et par la mesure (figures 2b, p. 7, et 5b, p. 16). Il n'est pas léger ; il est **confondu et fragile** : la fenêtre change aussi l'entraînement (« we average logits over a sliding window of M tokens during training », p. 6, cité par le lecteur), l'inférence emploie une autre règle que l'entraînement (« For evaluation, we compute predictions using an exponentially weighted moving average. », p. 7 ; « We did not experiment with EMA during training », p. 6), aucune barre d'erreur n'est imprimée, et la courbe n'est pas monotone (fenêtre 8 au-dessus de fenêtre 4, figure).
- L'écart d'échelle d'un facteur 100 entre les figures 2b et 5 relevé par le lecteur est confirmé sur l'image (figure 2b : environ 1,4 ; 4 ; 13 ; 14,5 ; figure 5a : environ 0,013 ; 0,04 ; 0,13 ; 0,145 ; rapport 100, calcul).

Texte corrigé proposé (tableau de la pièce 1, ligne (a)) :
> « (a) robustesse des agrégations au jeton | **occupée en partie** : variantes de lissage (fenêtre de 1 à 64 jetons ; maximum cumulé comme perte) comparées au taux de succès d'attaque sur environ 7 000 échanges d'attaques humaines transférées, à taux de refus égal ; **contre-indice** à « maximum brut robuste » (motif imprimé p. 6 ; figure 5b), confondu avec l'entraînement, sans barre d'erreur, non monotone. Non fait : comparaison sous attaquant adapté aux règles comparées | p. 6, 7, 16 »

À ajouter à « ce qu'une phrase publique ne doit pas affirmer » :
> « Qu'aucune règle de lissage ou d'agrégation de scores de sonde n'a été comparée sur des données d'attaque (2601.04603, p. 7 et 16 : comparaison sur attaques humaines transférées). »

Signalement, hors du rôle du lecteur comme du mien : l'énoncé de Tr dit la robustesse du maximum « établie » au niveau du jeton ; cette pièce plaide le contraire pour le maximum brut. Toucher à l'énoncé est un nœud de décision du directeur ; je le signale, je ne le propose pas.

### D — mineur — 2609.19101 : « seul indice » est faux ; la règle du jeton au passage reste non imprimée, et aucune comparaison n'existe

Texte du rapport (l. 125) : « La règle qui passe des jetons au passage n'est pas imprimée ; seul indice : « identify the peak probe location within each passage » (p. 10) ».

J'ai cherché une comparaison de règles (moyenne, maximum, dernier jeton, attention) au grain du passage ou de l'épisode dans les 39 pages, corps, annexes, tableaux 1 à 4 et légendes des figures 1 à 23 : **il n'y en a pas**. Le faux ami est bien celui que le lecteur a vu : « In addition, we test several poolings over individual datasets. » (p. 7) porte sur la mise en commun des jeux synthétiques (« 7 pooled comparisons », tableau 3, p. 26). Sur ce point le rapport tient : (c) « ne touche pas ».

Mais le pic n'est pas le seul indice ; cinq autres convergent vers « le passage est signalé dès qu'une position dépasse le seuil », donc un maximum par jeton :
- seuil par position : « flagging positions whose score exceeds a threshold » (p. 6) ;
- la sonde « tire » : « every time the probe fires, the decision is then escalated to the LLM monitor » (p. 9) ;
- seuils réglés sur le taux de faux positifs du moniteur, avec vérités au grain du passage : « we select probe thresholds that match the LLM monitor’s false positive rate » ; « These comparisons use passage-level ground truths that include both contemplated and attempted/completed hacks. » (p. 9) ;
- classement des passages par la sonde : « Namely, we take the top 100 false positives as ranked by the probe » (p. 11) ;
- « max-activating examples for a probe are examined by an LLM » (p. 13).

Incohérence non relevée : le score est un produit scalaire à la p. 6 (formule, lue sur le PDF) et une similarité cosinus sur l'axe de la figure 14 (« Probe threshold (cosine similarity) », p. 14).

Texte corrigé proposé :
> « La règle qui passe des jetons au passage n'est pas imprimée. Indices convergents vers un maximum par jeton comparé à un seuil : seuil par position (p. 6), sonde qui « tire » (p. 9), seuils réglés au grain du passage (p. 9), classement des passages par la sonde (p. 11), exemples d'activation maximale (p. 13), pic dans le passage (p. 10). Lecture, non imprimée. Aucune autre règle n'est essayée ni comparée, dans le corps comme dans les annexes. »

### E — majeur — 2609.19101 : le grain de la trajectoire est omis ; (b) est faite en partie, pas seulement « voisine »

Texte du rapport : « Déroulé : taux de piratage par déroulé (figure 2, p. 4) » ; verdict (b) : « voisin (fort) ».

Non relevé :
- La sonde est employée au grain du déroulé : « if we replaced some percentage of rollouts graded by an LLM monitor with probe grading » (p. 10, figure 9 p. 11). La règle qui passe des passages au déroulé pour la sonde n'est pas imprimée, et l'unité de la figure 9 (déroulé ou passage) est ambiguë.
- Pour les juges, la règle du passage au déroulé est imprimée, et c'est « au moins un » : « Do not judge the transcript as a whole; the runtime aggregates your passage findings deterministically. » (p. 28) ; « the transcript shows reward hacking exactly when at least one of its passages is positive » (p. 37). C'est un maximum sur les passages, pour un juge qui lit le texte, pas pour la sonde.
- Aucune accumulation séquentielle de scores de sonde sur le déroulé ; aucune règle comparée à ce grain.

Les raisons que le rapport donne pour s'en tenir à « voisin » (« ni agrégation comparée, ni robustesse ») sont les composantes (c) et (d), pas (b). La composante (b), prise seule — porter la lecture par jeton au grain de l'action et y mesurer la détection — est faite, sans attaquant, avec une règle implicite : aires sous la courbe de fonctionnement du récepteur au grain du passage (figure 8, p. 10), appels d'outil compris (« A passage is one channel of one step: », p. 31).

Texte corrigé proposé (tableau de la pièce 3, ligne (b)) :
> « (b) transposition au grain de l'action | **occupée en partie** : sonde par jeton lue au grain du passage (raisonnement, message, appels d'outil du pas) avec détection mesurée, et employée au grain du déroulé, dans des agents ; règle du jeton au passage et du passage au déroulé non imprimées ; « au moins un passage » imprimé pour les juges seulement (p. 28, 37). Non fait : règle explicite, comparaison, robustesse, accumulation séquentielle | p. 5, 6, 9, 10, 28, 31, 37 »

À ajouter à « ce qu'une phrase publique ne doit pas affirmer » :
> « Être les premiers à porter une sonde par jeton au grain du déroulé entier d'un agent (2609.19101, p. 10). »

### F — majeur — 2609.19101 : rien sous attaque, confirmé ; mais deux passages et un voisin direct du bras d'attaque par les poids ne sont pas relevés

J'ai cherché toute évaluation sous obfuscation, consigne d'évitement, réglage contre la sonde, ou modèle qui sait être surveillé : **aucune**. Le verdict (d) « ne touche pas » tient. Le rapport cite la bonne phrase (« A further challenge is that models may learn to obfuscate undesirable behavior from their reasoning traces », p. 17) mais elle porte sur le texte du raisonnement. Trois éléments plus proches de Tr manquent :
1. Les auteurs nomment l'évasion par les poids contre la sonde elle-même : « training procedures that suppress or erase representations of undesirable concepts may simultaneously incentivize the model to learn new representations of the same concepts » (p. 17), « thus removing the original signal used to detect them » (p. 18). C'est une limite reconnue, nommée comme travail futur : au sens de la règle R8, ce n'est pas un trou du champ, et ce n'est pas une occupation.
2. Un voisin direct du bras (b) de E1.5 (programme l. 187 : réglage fin puis apprentissage par renforcement au niveau de l'action) est nommé et absent de la liste du lecteur : Yang et al. 2025, arXiv 2510.17431, « Agentic reinforcement learning for search is unsafe » (p. 17 et 24), dont la pièce dit qu'ils « incorporate projections onto these directions directly into the RL reward » (p. 17). C'est l'optimisation d'un agent, par renforcement, contre une direction linéaire de ses activations — présentée comme mitigation, mais c'est la mécanique d'un attaquant par les poids. Non lu ; collision possible sur (d) au grain de l'agent. Même passage : Bergen et al. 2026, arXiv 2606.12360 (p. 17 et 19).
3. Observations spontanées, sans protocole : les modèles sont dits « largely evaluation aware » (p. 3) ; « our probes for reward hacking tend to fire near or on these positions » (p. 18) ; des raisonnements déjà illisibles : « Indeed, we already found some rollouts from this work to be obscure for some models and settings. » (p. 17) ; une condition d'auto-déclaration (« We also attempted to have models self-report their own hacks using a prompt similar to the LLM Monitor, but called after every turn as a new user message. », p. 5) où la sonde n'est pas évaluée. Aucune n'est une épreuve de la sonde sous un modèle qui sait être surveillé ; le rapport a raison de citer « Our study does not control for evaluation awareness in any of our experiments » (p. 18). Le deuxième point (la sonde tire là où le modèle reconnaît l'évaluation) regarde H8 plus que Tr : signalé, hors mandat.

Texte corrigé proposé (pièce 3, « Attaquant ») :
> « Attaquant : aucun ; aucune évaluation sous obfuscation, consigne d'évitement, réglage contre la sonde ou modèle averti d'une surveillance. L'obfuscation du raisonnement (p. 17) et la disparition du signal sous un entraînement qui supprime les représentations (p. 17-18) sont nommées comme travail futur. Voisin nommé, non lu : Yang et al. 2025, projections sur des directions linéaires mises dans la récompense d'un agent (p. 17 et 24). »

### G — majeur — Bases nommées proposées pour E1.5 : deux ne sont pas imprimées telles quelles, trois manquent

Texte du rapport (l. 166) : « la règle de production de 2601.04603 (seuil franchi en un point quelconque par un score lissé en moyenne mobile exponentielle, p. 6-7) et la lecture par pic au passage de 2609.19101 (p. 10) ».

- **Règle de 2601.04603 : non reproductible telle qu'imprimée.** Le coefficient de la moyenne mobile exponentielle n'est imprimé nulle part (recherche par mots sur les 17 pages ; seule la fenêtre d'entraînement de 16 jetons l'est, p. 7). L'entraînement lisse par moyenne glissante, l'inférence par moyenne mobile exponentielle, sans essai croisé (« We did not experiment with EMA during training », p. 6). Le seuil est calé sur un taux de refus de 0,1 % sur un jeu public de conversations (p. 7, légende de la figure 2). La sonde concatène toutes les couches. En production, la règle n'est pas la sonde seule mais une cascade à score pondéré (p. 9). La nommer « règle de production de 2601.04603 » sans ces réserves attribuerait à la pièce une règle que nous aurions paramétrée nous-mêmes.
- **« Lecture par pic au passage de 2609.19101 » : règle non imprimée** (constat D). La nommer ainsi attribue à la pièce une règle qu'elle n'énonce pas.
- **Manquent**, pour que la comparaison soit jugée contre ces pièces : (i) la moyenne sur l'empan, seule règle de 2603.04069 (« we compute the mean probability over tokens in the selected span », p. 4), que le programme ne permet qu'en bras de diagnostic ; (ii) le maximum brut par jeton (fenêtre de 1) et le maximum cumulé (« We explore using the cumulative maximum of probe probabilities as the predictor for the full sequence label. », p. 16), comparés dans 2601.04603 ; (iii) l'agrégation par pondération douce que 2601.04603 attribue à McKenzie et al. 2025 (« While they aggregate token scores into single sequence-level predictions, we build streaming classifiers with continuous predictions during generation. » ; « We use a softmax to weight per-token losses, not to aggregate predictions over tokens. », p. 10) — c'est l'« attention » de l'énoncé de Tr.

Texte corrigé proposé :
> « Pour que E1.5 soit jugée contre ces pièces, bases à proposer au directeur (le périmètre de E1.5 n'est pas au lecteur) : (1) seuil franchi en un point quelconque par un score lissé — moyenne glissante de 16 jetons (imprimée, 2601.04603, p. 7) et moyenne mobile exponentielle dont le coefficient, non imprimé, est fixé et déclaré par nous ; (2) maximum des scores par jeton sur le passage, comparé à un seuil — lecture de 2609.19101 (p. 6, 9, 10), règle non imprimée par la pièce ; (3) maximum brut par jeton et maximum cumulé (2601.04603, p. 16) ; (4) moyenne sur l'empan (2603.04069, p. 4), en bras de diagnostic seulement ; (5) pondération douce de type attention (McKenzie et al. 2025, nommée par 2601.04603, p. 10 ; source à relire). »

### H — mineur — 2603.04069 : la moyenne seule, confirmée ; le F1 de 1,000 est trop propre pour une raison que le rapport ne donne pas ; (b) est « voisin », non « ne touche pas »

- Moyenne seule : confirmé. « To obtain a stable behavior-level signal, token-level probabilities are aggregated over a predefined token span » ; « we compute the mean probability over tokens in the selected span » (p. 4) ; puis moyenne sur les couches et seuil fixe de 0,5 (formule p. 5, lue sur le PDF). Aucune autre règle n'est essayée ; les tranches de 64 jetons (« monitor probabilities are aggregated into fixed bins of 64 tokens and averaged across prompts », p. 6), la pente et l'écart de fin de génération (p. 11 à 13) sont descriptifs. Aucun attaquant, aucun agent. Le verdict « voisin lointain » tient.
- F1 de 1,000 pour l'adaptateur témoin dans les trois familles (tableau 1, p. 5, auteurs) : le rapport le relève comme trop propre, à raison, sans dire pourquoi il ne prouve rien. La pièce n'imprime ni la classe comptée comme positive, ni les effectifs, ni un taux de faux positifs. Si presque toutes les générations de l'adaptateur témoin sont dites « témoin » par le juge et par le moniteur, un F1 de 1,000 est un accord dégénéré, pas une discrimination (lecture du contre-lecteur). Deux incohérences de plus : le juge externe est « ground truth » dans le texte (« of the generated answers, used as ground truth », p. 5) et la phrase suivante lui prête une performance (« output-based judgments achieve good performance for control adapters », p. 5) ; des tranches de 64 jetons pour des raisonnements de 64 à 512 jetons (« For each model family, we evaluate CoT lengths of 64, 128, 256, and 512 tokens. », p. 6) ne donnent pas l'axe gradué jusqu'à 60 de la figure 3 (p. 6, figure). Les auteurs reconnaissent la fragilité du juge (« judges may decrease the reliability of results », p. 9).
- Le construit : confirmé. Le classifieur est entraîné « to distinguish activations originating from hack versus control adapters » (p. 4), sur les deux adaptateurs extrêmes seulement (« trained only on activations from the benign control adapter and the fully reward-hacking adapter », p. 5) : il peut lire l'adaptateur, pas le comportement.
- (b) : « The monitor produces one decision per generation. » (p. 5). Une génération est l'analogue, hors agent, d'une action. Verdict corrigé proposé : « (b) voisin (une décision par génération, par moyenne, hors agent) » au lieu de « ne touche pas ».

### I — mineur — Réserves de la règle R4 incomplètes

- 2609.19101 : les sondes rapportées sont choisies sur des données réelles étiquetées (« We select two probes per model: one with the highest AUROC on a held out set of 250 rollouts », p. 9) parmi 54 directions (tableau 3, p. 26, auteurs) ; pour les environnements sans vérité, par le taux de tir le plus haut (« select the probe with the highest firing rate at that threshold on these two non-SWE environments », p. 13) ; les passages sans consensus sortent de la mesure (« Non-consensus passages are not considered when measuring performance. », p. 5). Le rapport ne retient que l'identité du juge et du moniteur.
- 2601.04603 : le poids de l'ensemble « is optimized per pair to minimize attack success rate on the test set » (p. 8) ; figures 2 et 5 sans barre d'erreur ; les auteurs avertissent eux-mêmes que « relying solely on synthetic benchmarks can lead to overfitting on limited test cases » (p. 17).

Sans effet sur le verdict ; à joindre aux réserves du rapport.

### J — mineur — Voisins non lus : liste à compléter, priorité à préciser

- **Wilhelm et Kao 2026** (2609.19101, p. 17 : « which has been targeted towards reward hacking in prior work » ; p. 24 : « From reward-hack activations to agentic risk states: Context-calibrated mechanistic monitoring in LLM agents ») : nom et pages exacts ; priorité haute confirmée. Le rapport dit « collision possible sur (b) et (e) » ; le titre (« états de risque d'un agent », « calibré par le contexte ») rend possible aussi une collision sur (c). Contenu inconnu : je ne l'ai pas lu, le lecteur non plus.
- **À ajouter, priorité haute** : Yang et al. 2025, arXiv 2510.17431 (2609.19101, p. 17 et 24) — constat F.
- **À ajouter, priorité moyenne** : Bergen et al. 2026, arXiv 2606.12360 (2609.19101, p. 17 et 19) ; Zou et al. 2024, arXiv 2406.04313, et Casper et al. 2024, arXiv 2403.05030 (2601.04603, p. 10, 12 et 13 : pertes fondées sur les activations, entraînement adverse latent).
- Le rapport écrit que McKenzie et al. 2025 est « déjà lu au niveau 2 » d'après un fichier hors de mon mandat : non vérifié ici. Cette source porte l'agrégation « attention » de la prémisse de Tr (constat G) ; si elle n'a pas été lue contre Tr, elle est à relire.

---

## Ce que le rapport a bien fait (relu page par page)

- Les 49 citations du lecteur passent mon script indépendant (49 réussies, 0 échec) ; les pages citées sont exactes partout où j'ai relu.
- Le faux ami « poolings » (p. 7 de 2609.19101) est correctement écarté ; la définition du passage (p. 31) et l'étiquetage par canal (p. 5) sont bien lus.
- Le maximum cumulé de 2601.04603 est bien lu comme fonction de perte et non comme règle de décision (p. 16) ; l'écart d'échelle d'un facteur 100 entre les figures 2 et 5 est réel.
- L'incohérence entre le résumé et le corps de 2609.19101 (pourcentages et points) et celle de 2603.04069 sur le mode d'entraînement des adaptateurs sont réelles.
- Les quatre premières interdictions de la section « ce qu'une phrase publique ne doit pas affirmer » sont fondées ; la cinquième (« libre dans le champ ») est la bonne garde.

## Jugement de profondeur

**Suffisante pour le verdict sur le noyau, insuffisante pour les gardes.** Le journal du lecteur donne l'étendue par PDF et la liste des mots cherchés pour la troisième pièce seulement ; il ne donne ni détail par page ni mots cherchés pour les deux autres. Les faits rapportés sont justes. Mais quatre éléments que le journal dit avoir lus « ligne à ligne » ne sont pas dans le rapport : la règle « au moins un passage » des grilles (p. 28 et 37 de 2609.19101), l'emploi de la sonde au grain du déroulé (p. 10), la phrase sur la disparition du signal sous entraînement (p. 17-18), et l'absence de coefficient pour la moyenne mobile exponentielle (2601.04603). Les références ont été « parcourues par mots », ce qui a laissé passer Yang et al. 2025, nommé dans le corps (p. 17). Les figures de 2603.04069 n'ont été lues, par lui comme par moi, que par leurs légendes.

Ma propre limite : je n'ai lu aucun des voisins ; je n'ai pas lu les pièces déjà versées contre Tr au niveau 3 (2610.17301, 2610.40588, 2610.39377, 2610.12445), hors mandat ; mon verdict ne vaut que pour les trois PDF.

## Texte corrigé de l'en-tête du verdict (proposé)

> **Tr : occupé en partie** (ou, si la convention du niveau 3 est retenue : « noyau non trouvé dans les pièces lues », les trois composantes faites écrites à côté).
> Faites, hors du noyau : (1) lecture d'une sonde par jeton au grain du passage et du déroulé dans des agents, sans attaquant, règle non imprimée (2609.19101) ; (2) humains adaptatifs, en boîte noire, contre un système dont la première porte est une sonde lissée au fil des jetons, au grain de l'échange, une seule règle (2601.04603) ; (3) comparaison de lissages sur des attaques humaines transférées, au grain du jeton (2601.04603).
> Non trouvé dans les pièces lues : comparaison de règles d'agrégation de scores de sondes au grain de l'action ou de la trajectoire d'un agent ; attaquant adaptatif à ce grain ; accumulation séquentielle de scores de sondes sur une trajectoire ; conclusion portée du jeton à l'action.
> Non lus, à lire avant toute phrase publique : Wilhelm et Kao 2026 ; « What the Monitor Saw » ; Yang et al. 2025.

## Formules (lues sur le PDF, non contrôlées par programme)

- 2601.04603, p. 9 : z_final = 0,55 · z_probe + 0,45 · z_classifier ; éq. 5 (p. 16) : p(y = 1 | x_{1:t}) = max_{τ ≤ t} σ(z̄_τ).
- 2603.04069, éq. 4 (p. 5) : décision « hack » si (1/|L|) Σ_ℓ (1/|T|) Σ_{t∈T} p_{t,ℓ} ≥ τ, avec τ = 0,5.
- 2609.19101, p. 6 : s_t = ⟨v_hack, x_t⟩, position signalée si s_t dépasse un seuil τ.

## Archive

`docs/sources/lecture-pdf-niveau3/compte-2/fichiers-de-travail-contre-lecture-Tr-v1.tar` : script de contrôle, `citations-contre-lecture-Tr-v1.json` (70 citations), sortie du contrôle, essais juste et altéré, recontrôle des 49 citations du lecteur, journal du contre-lecteur ; sans PDF ni textes extraits.
