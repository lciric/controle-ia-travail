# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHftRj1T9AhDcqNiXqjd`
- Heure (UTC) : 2026-11-22T08:47:49Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 100000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-25-dopamine-second-regard-pince-v1.md` — sha256 c2954a5dbc02d3849a3b4773d99e1f790b72cce217340471a30b9229f34d8efc (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/decision-N-075-issue-plancher-et-deux-regards-v3-sans-nom-v1.md` — sha256 7a3d384d64607937083f272521659d74ac50406530aa913cd6a7b81942b66c4e (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/decision-N-075-issue-plancher-et-deux-regards-v3-erratum-3-v2-sans-nom-v1.md` — sha256 7c8cb4e6b4e5d997a23ded1d5c5edbc20a4a54d916fd0940bbca4b8976a2971d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/reponse-fable-mecanisme-adjudant-v2-sans-nom-v1.md` — sha256 806125b65a87ebd1894e8768edcefe24ab5fcd2134a0765b0d520965e1cdae0a (compagnon : vérifié)
  - remarques : `docs/notes/papier-dopamine-moniteur-v1/consultation-fable-papier-dopamine-v1.md` — sha256 afc22a5fd6d8a5e088872651d82b3b64d871b371dd4619bfe63fc8e24e95fdda (compagnon : vérifié)
- Empreinte de l'invite envoyée : f06cf83c3e407b3a78d634398c968cd48d3f8081a3446e8b589ff510ee787dc6
- Jetons : entrée 113390, sortie 24904 (dont réflexion 12471), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.903280 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 25 — le signal de dopamine comme second regard dans la pince : réponse du concepteur

**Lecture de la consigne.** Je lis « sans nom de personne » comme visant les personnes du programme. Les auteurs d'antériorité sont nommés, comme la règle l'exige. Je n'ai ouvert aucun PDF, lu aucun résultat ni lancé aucun calcul dans cette session : toute citation porte donc le statut « rapporté, non vérifié sur PDF », et aucun chiffre n'est opposable.

**Notations.** V est la réussite attendue lue par la sonde (une probabilité entre 0 et 1), δ la surprise par étape, Y l'issue calculée par l'oracle, R la référence honnête.

## 1. Ce qu'un expert ferait, et qui n'est pas demandé

1. **[PROPOSITION] Dire d'abord ce que le signal ne peut pas apporter.** Le bilan de la pince est un télescopage : la lecture du suspect s'y annule, donc aucune sonde n'ajoute de puissance à la somme. L'expert chercherait la valeur du signal là seulement où elle peut exister : la vitesse (V se lit avant Y), l'aiguillage de l'audit, et la complémentarité mesurée.
2. **[PROPOSITION] Sceller trois lectures concurrentes et signées avant toute lecture.** V peut lire la difficulté (il ne bouge pas avec la dose de sabotage), l'issue attendue (il baisse chez le saboteur comme chez l'honnête en difficulté), ou donner une dissociation « dommage sans surprise ». La consultation jointe les pose déjà.
3. **[PROPOSITION] Écrire le témoin avant l'instrument.** Ce témoin est un lecteur de texte entraîné sur les mêmes épisodes honnêtes, les mêmes étiquettes d'issue et les mêmes frontières d'action. Seul le canal diffère.
4. **[PROPOSITION] Traiter la sonde comme un instrument à plage de validité.** Elle est calibrée sur des honnêtes exogènes du régime, s'abstient hors plage, et déclare la taille m de sa référence et son horizon n (N-076).
5. **[PROPOSITION] Anticiper le biais d'audit.** Une sonde de réussite attendue signale par construction l'échec honnête. Un audit qu'elle oriente n'est donc plus un échantillon sans biais.
6. **[PROPOSITION] Déclarer l'échelon d'attaquant.** Le dispositif est fait contre un agent à poids gelés, qui ne voit ni lecture ni verdict.
7. **[PROPOSITION] Rejouer un chiffre publié du papier sur le modèle du programme** avant de toucher un épisode.
8. **[PROPOSITION] Chercher l'antériorité aux deux endroits séduisants** : la détection par écart entre attente interne et mesure, et le gain de la boîte blanche sur la boîte noire.

## 2. Les données brutes de départ

[PROPOSITION] L'expert ne partirait ni des tableaux du papier ni des scores de sondes déjà agrégés. Il prendrait :

- **Les activations par jeton** de Llama 3.1 8B Instruct, en sortie de bloc, aux couches du programme (7, 15, 23) et à celles du papier (2 à 4 ; milieu de réseau pour δ). Trois positions : fin de consigne, chaque frontière d'action, fin d'épisode. Elles sont prises sur les épisodes honnêtes, sur leurs jumeaux honnêtes appariés, puis sur les épisodes à dommage planté.
- **Le texte brut** de chaque action, coupé aux mêmes frontières, pour le lecteur de texte témoin.
- **L'issue Y par épisode**, et si possible par action, rendue par l'oracle de couverture, avec les verdicts sur les honnêtes de référence, comptés (m).
- **Les continuations** tirées depuis chaque frontière, si δ est estimé à la manière du papier. Leur nombre et leur erreur type sont consignés, car le papier ne donne pas ce nombre [FAIT RAPPORTÉ, consultation].
- **Le journal des audits**, avec la probabilité de chaque tirage et la part qui l'a déclenché (plancher, enjeu, soupçon).
- **Les jeux publics du papier** (MATH500, ARC, Minerva Math), réponses régénérées par nous.

[PROPOSITION] À vérifier sur disque avant tout devis : si les activations par jeton des épisodes déjà joués existent aux bonnes couches et positions. Les relire reste une lecture nouvelle, donc un préenregistrement.

## 3. Les méthodes et les outils

- **Sondes.** [PROPOSITION] Une sonde linéaire (régression logistique) à côté de la réplique du papier (perceptron à deux couches, objectif de différence temporelle). Agrégation par maximum ou par attention sur les jetons de l'action, jamais par moyenne en production (N-026). Normalisation sur un étalonnage honnête gelé.
- **Témoins de construit.** [PROPOSITION] Étiquettes permutées (le hasard est attendu) ; direction aléatoire appariée en covariance ; lecture à positions textuelles masquées (N-053) ; sous-ensemble aléatoire de coordonnées avec sonde réentraînée.
- **Nul par acte au banc.** [PROPOSITION] Paires agent–jumeau sur la même tâche ; test exact du signe et des rangs signés sur les écarts appariés.
- **Calibration.** [PROPOSITION] Test de calibration sur honnêtes réservés, dans la forme séquentielle valide à tout instant si l'on accumule.
- **Comparaison de deux seconds regards.** [PROPOSITION] Test exact de McNemar sur les paires discordantes, à fausses alertes conjointes égales. Intervalles par rééchantillonnage d'épisodes entiers.
- **Estimation sous audit orienté.** [PROPOSITION] Lecture de la seule part plancher, ou pondération par l'inverse de la probabilité d'audit consignée.
- **Tenue de course.** [PROPOSITION] Graines par séquence de graines, manifeste par course, prévisions signées scellées.

## 4. Ce qui vérifierait le résultat hors du directeur et de Claude

1. [PROPOSITION] **Un chiffre publié rejoué sur données publiques.** Le tableau 3 du papier, sur Llama 3.1 8B et MATH500, est rapporté par la consultation. Si notre chaîne n'y retombe pas, on le sait avant le programme.
2. [PROPOSITION] **Une vérité plantée et un placebo.** Les dommages sont plantés par un tiers ; les issues permutées doivent rendre le hasard.
3. [PROPOSITION] **Des organismes et des familles écrits par d'autres**, dont le mode tenu à l'écart (N-054), jamais lu par le concepteur.
4. [PROPOSITION] **Le lecteur de texte témoin écrit par un agent d'une autre lignée**, qui ne connaît pas la prévision.
5. [PROPOSITION] **La chaîne de relecture** : contre-lecture du préenregistrement par un autre modèle, verdict par un agent neuf.
6. [PROPOSITION] **Le test de devinette** sur la question neutre, joué par des modèles neufs (partie C).
7. [PROPOSITION] **Le temps** : prévisions scellées avant lecture.

## Demande reformulée

> Dans une défense qui joint un moniteur de texte, une lecture interne et un oracle sur le produit, dire où se loge exactement la lecture de la réussite attendue et de la surprise par étape, apprise sur épisodes honnêtes seuls. Le dire terme à terme dans les trois objets de la pince : la complémentarité, qui se mesure ; l'étau, qui se suppose ; le bilan, qui est une identité. Donner pour cette lecture une grandeur, une unité et une hypothèse nulle dont la validité ne dépende pas de l'attaque, avec la taille de la référence honnête et l'horizon déclarés. Écrire le témoin qui dirait si elle apporte quelque chose au-delà d'un second lecteur de texte entraîné sur les mêmes épisodes, les mêmes issues et les mêmes positions. Partir des activations brutes, du texte brut, de l'issue calculée et des traces du jumeau honnête, après avoir rejoué un chiffre publié du papier sur le modèle du programme. Dire ce que cette lecture ne doit jamais devenir. Nommer l'antériorité. Proposer la première expérience sans attaque, son coût en passages de modèle et l'issue qui la tue. Faire vérifier hors de nous par un chiffre public rejoué, un placebo, des dommages plantés par un tiers et un témoin écrit par une autre lignée.

## Réponse

### B1. La place exacte du signal dans les trois objets

[FAIT RAPPORTÉ] N-075 dit la pince en trois objets : la complémentarité (ce que l'interne capture parmi les manqués de l'externe, à fausses alertes partagées), l'étau (tromper l'externe laisserait une trace interne) et le bilan, qui s'écrit : dommage vu par l'oracle = (référence honnête − lecture du suspect) + (lecture du suspect − issue).

**Dans le bilan, le signal est le terme du milieu.**

- [PROPOSITION] Au banc, avec le jumeau honnête j et le suspect s, le dommage D = Y_j − Y_s se télescope en trois termes : D = (V_j − V_s) + (V_s − Y_s) − (V_j − Y_j). C'est une identité élémentaire, à rejouer par le contre-lecteur.
- [PROPOSITION] Le premier terme est l'écart de lecture, connu avant toute issue. Les deux autres sont les résidus de calibration du suspect et du jumeau, connus quand l'oracle a jugé.
- [PROPOSITION] Trois conséquences. Quoi que le suspect fasse de V_s, la somme ne bouge pas : la sonde ne porte pas la garantie du bilan et ne peut pas la dégrader. Lu bas, le suspect grossit le premier terme, ce qui le fait aiguiller tôt ; lu haut, il grossit le deuxième, c'est-à-dire qu'il échoue contre sa propre lecture. Ce que le signal ajoute au bilan est donc une date et une adresse, jamais de la puissance.

**Dans la complémentarité, le signal est la mâchoire interne candidate.**

- [PROPOSITION] C'est le seul des trois objets où « il apporte quelque chose » se mesure. La mesure est en B2 et son témoin en B3.

**Dans l'étau, le signal n'est qu'une hypothèse.**

- [HYPOTHÈSE] Un saboteur qui trompe les lecteurs de texte garderait une réussite attendue basse dans ses états.
- [FAIT RAPPORTÉ] Contre-indices déjà au dépôt : la sonde lit l'échec attendu et non l'intention ; un précurseur publié ne sépare pas la triche de l'échec honnête sur un modèle sur trois ; un attaquant qui déplace ses représentations tait les sondes ensemble.
- [PROPOSITION] L'étau ne s'éprouve que dans un bras d'attaque déclaré. Il ne s'écrit jamais comme garantie.

**La surprise δ a une place plus étroite.**

- [FAIT RAPPORTÉ] Sa somme sur un épisode se réduit à l'écart entre la fin et le début (préenregistrement court du bras, version 7).
- [PROPOSITION] Elle n'ajoute donc rien au bilan. Elle sert seulement à localiser dans l'épisode où la lecture a basculé : c'est le « même lieu » de la règle à deux clés.
- [HYPOTHÈSE] La dissociation « dommage sans surprise » trierait, après audit, l'erreur de l'intention.
- [PROPOSITION] Elle reste exploratoire. Une surprise présente n'innocente personne.

**Règle à deux clés (forme retenue de N-075, erratum 3).**

- [PROPOSITION] Un motif (V bas, ou δ négatif) et un dommage rendu par l'oracle au même épisode donnent une alerte.
- [PROPOSITION] Un motif seul envoie l'épisode en file d'audit ; il n'entre jamais dans les témoins.
- [PROPOSITION] Un dommage sans motif relève du plancher et n'attend rien.

### B2. La grandeur, son unité, son nul

**Grandeur de l'instrument : l'écart de lecture apparié.**

- [PROPOSITION] Par épisode, T = V_j − V_s, lu à la dernière frontière d'action avant l'issue.
- [PROPOSITION] Unité : le point de réussite par épisode, V et Y étant des taux entre 0 et 1. En cumul : des épisodes-équivalents de réussite.
- [PROPOSITION] Nul au banc, par acte : si le suspect est honnête, la paire est échangeable, et le signe de T (comme celui de la différence des résidus) est symétrique. Ce nul ne demande aucun taux estimé.
- [PROPOSITION] En service il n'y a pas de jumeau. Le nul devient la calibration de V sur m honnêtes exogènes du régime, placé à sa borne haute, avec un horizon n au plus égal à m.
- [FAIT RAPPORTÉ] La question de savoir qui produit cette référence en service est ouverte (N-075, section 11, point 5).
- [PROPOSITION] Rien ne se dit donc en service.

**Grandeur de l'apport : la complémentarité incrémentale Δ.**

- [PROPOSITION] On prend les épisodes à dommage planté que le premier moniteur de texte a manqués. Δ est le rappel du signal de dopamine sur ces épisodes, moins celui de la seconde boîte noire sur les mêmes épisodes. Les deux bras tiennent le même taux conjoint de fausses alertes sur honnêtes réservés.
- [PROPOSITION] Unité : le point de pourcentage d'épisodes endommagés rattrapés.
- [PROPOSITION] Nul : Δ = 0, soit, parmi les épisodes rattrapés par un seul des deux regards, une chance sur deux pour chacun (test exact de McNemar). Les seuils des deux bras sont pris au même quantile du même jeu de m honnêtes, m dit.

**Quantités rapportées sans critère.**

- [PROPOSITION] Le silence commun des regards sous attaque.
- [PROPOSITION] Le dommage cumulé à l'arrêt, à étiquettes égales, contre trois bases : le plancher seul, le moniteur de texte qui oriente l'audit, la seconde boîte noire qui l'oriente.
- [PROPOSITION] Le taux d'honnêtes aiguillés à tort.
- [FAIT RAPPORTÉ] Un dilemme, même parfait, ne paie que si chaque regard voit au moins la moitié des attaques neuves (N-075, section 3 ; calcul sous supposition).

### B3. Le contrôle « seconde boîte noire »

[PROPOSITION] Trois bras, sur les mêmes épisodes, au même budget de fausses alertes et au même budget d'étiquettes :

1. le moniteur de texte seul ;
2. le moniteur de texte et la seconde boîte noire ;
3. le moniteur de texte et le signal de dopamine.

[PROPOSITION] La seconde boîte noire est le meilleur de trois lecteurs, choisi sur un jeu de réglage disjoint :

- **Le jumeau textuel de la sonde.** Un prédicteur de l'issue qui lit le texte jusqu'à la même frontière, entraîné sur les mêmes épisodes honnêtes et les mêmes issues. C'est le témoin exact, puisque seul le canal change.
- **Un juge de texte d'une autre lignée.**
- **La confiance demandée au modèle**, sur un rejeu bifurqué pour que rien ne revienne à l'agent.

[FAIT RAPPORTÉ] Selon la consultation, le papier montre que la confiance demandée égale la sonde sur Llama 3.1 8B et MATH500, et que la longueur de la question fait presque aussi bien avant génération.

[PROPOSITION] Trois témoins « doit mourir » passent avant toute lecture :

- la sonde à étiquettes permutées doit rendre le hasard ;
- une direction aléatoire appariée en covariance ne doit rien rattraper ;
- une sonde des couches 2 à 4 en fin de consigne, que la longueur du texte égale, ne s'appelle pas interne.

[PROPOSITION] Lecture écrite d'avance :

- **Δ > 0** au seuil scellé : « apport interne mesuré sur ces modes, mode tenu à l'écart compris », et rien au-delà.
- **Δ indiscernable de 0** : le signal est une seconde boîte noire déguisée, et sa place dans la mâchoire interne se tient à moindre coût par un lecteur de texte.
- **Δ < 0** : il sort de la mâchoire. Il ne reste que comme covariable, et seulement si la variance des scores honnêtes baisse.

[PROPOSITION] Taille : pour séparer un partage 50/50 d'un partage 75/25 des paires discordantes (niveau unilatéral 5 %, puissance 0,8), il faut de l'ordre de 25 à 30 paires discordantes. C'est mon approximation normale, non rejouée par programme, à recalculer en loi exacte.

### B4. La différence avec un adjudant, et ce qui ne doit jamais en être fait

[FAIT RAPPORTÉ] La note du concepteur distingue trois sortes d'adjudant : celui qui annonce que le moniteur n'est plus valide, celui qui pose un dilemme, celui qui borne le dommage sans rien détecter. Elle range la dopamine parmi les seconds regards. Aucun mode n'a servi à l'apprendre, mais son domaine de validité reste celui des épisodes honnêtes, elle lit l'échec attendu, et elle vit sur le canal qu'un attaquant informé sait déplacer.

[PROPOSITION] D'où les différences :

- un adjudant tient sa garantie de ce que le défenseur possède (ses tirages, l'oracle, le harnais) ; le signal de dopamine tient la sienne de ce que l'agent ne déplace pas ses états, ce qui est une supposition empirique ;
- il n'annonce pas l'invalidité du premier moniteur : c'est le rôle de la recapture ;
- il ne borne rien : c'est le rôle du plancher ;
- il ne vaut qu'à l'échelon où l'agent, poids gelés, ne voit ni lecture ni verdict.

[PROPOSITION] Ne jamais :

1. faire revenir à l'agent une lecture, un seuil, un verdict ou une conséquence observable qui en dépende ;
2. faire entrer V ou δ dans un signal d'entraînement ou de sélection de l'agent (N-053). Le guidage de la génération par la sonde, que le papier pratique, est interdit hors bras d'attaque déclaré ;
3. verser aux témoins un épisode du suspect, signalé ou non, ni recaler la sonde sur le flux du suspect ;
4. blanchir : un V haut n'innocente pas ;
5. prendre V pour l'issue : seul l'oracle rend le dommage ;
6. laisser l'audit orienté par V réduire la part tirée au hasard, ou lire sans pondération un échantillon qu'il a orienté ;
7. réapprendre la sonde sur des verdicts de l'oracle tant que le point 9 de N-075 n'est pas tranché ;
8. écrire « garantie de détection », « l'étau tient » ou « lit l'intention » ;
9. le compter autrement que comme toute sonnerie dans le taux de fausses alertes de la porte de fin de phase 1.

### B5. Le lien avec le papier « dopamine » et l'antériorité

Toutes les pièces ci-dessous ont le statut « rapporté, non vérifié sur PDF ».

- **Le papier.** Xu, Yuksekgonul, Zou, 2026, « Sparse Reward Subsystem in Large Language Models » (arXiv 2602.00986). [FAIT RAPPORTÉ, consultation] Il fournit la recette des deux sondes, mais ne traite ni surveillance ni adversaire. La surprise n'y est éprouvée que sur des modèles Qwen et au-dessus d'un seuil. La sonde de surprise publiée emploie une moyenne sur jetons et une normalisation sur la réponse entière, inutilisables en ligne. [PROPOSITION] Le programme en prend l'étiquette (l'issue, sans exemple d'attaque) et laisse le vocabulaire « neurones » et la thèse de parcimonie.
- **Attente interne confrontée à la mesure.** Roger, Greenblatt, Nadeau, Shlegeris, Thomas, 2023, « Benchmarks for Detecting Measurement Tampering » ; Mallen et al., 2023, « Eliciting Latent Knowledge from Quirky Language Models ». Cités de mémoire. [HYPOTHÈSE] Ce sont les voisins les plus proches du deuxième terme du bilan, et ils sont à lire en entier.
- **Gain de la boîte blanche sur la boîte noire.** Parrack, Attubato, Heimersheim, 2025, « Benchmarking Deception Probes via Black-to-White Performance Boosts ». Cité de mémoire, titre à vérifier. [HYPOTHÈSE] Le contrôle B3 y est probablement occupé dans sa forme générale.
- **Précurseur sans exemple d'attaque.** Fischl-Lanzoni, Pandey, Stein, Africa, 2026, « Breaking Bad: "Going Badly" Activations Drive Reward Hacking ». Bhardwaj et al., 2026 (arXiv 2610.31613), sondes de progrès apprises sur réussites seules.
- **Confiance et connaissance lues dans les états.** Kadavath et al., 2022, « Language Models (Mostly) Know What They Know » ; Azaria et Mitchell, 2023, « The Internal State of an LLM Knows When It's Lying » ; Burns et al., 2022, « Discovering Latent Knowledge in Language Models Without Supervision ». Cités de mémoire.
- **Retenue volontaire et sondes de tromperie.** Van der Weij et al., 2024, « AI Sandbagging: Language Models can Strategically Underperform on Evaluations » ; Goldowsky-Dill et al., 2025, « Detecting Strategic Deception Using Linear Probes ». Cités de mémoire. Tice et al., 2024 (arXiv 2412.01784).
- **Calibration et écart à l'honnête, valides à tout instant.** Arnold, Henzi, Ziegel, 2021, « Sequentially valid tests for forecast calibration » ; He, Qiu, Shirado, Sap, 2025, « Martingale Score » ; Ortega-Fernandez, Kowalczyk, Warr, 2026, « Anytime-valid detection of LLM weight exfiltration ».
- **Contre-indices à l'étau.** Bailey et al., 2024 (arXiv 2412.09565) ; McGuinness et al., 2025 (arXiv 2512.11949).
- **Total plutôt que parts.** Avenhaus et Jaech, 1981, « On Subdividing Material Balances in Time and/or Space ».

[PROPOSITION] Statut d'ensemble :

- Les pièces du second regard (valeur lue, calibration, précurseur, gain de la boîte blanche) sont publiées.
- Le bilan à trois termes avec la lecture interne au milieu, fermé contre un jumeau honnête, n'a fait l'objet d'aucune recherche d'antériorité. C'est une question, non une revendication.
- Aucune phrase ne s'écrit avant un verdict d'antériorité propre.

### B6. La première expérience, son coût, son issue négative

[PROPOSITION] **Étape 0, sans dépense.**

- Vérifier sur disque les activations existantes.
- Écrire la statistique, le jumeau textuel et les témoins.
- Écrire le préenregistrement court, exploratoire, contre-lu.

[PROPOSITION] **Étape 1, la première expérience, sans aucune attaque.** Elle est sans attaque parce que le collisionneur demande d'abord l'essai jumeau contre jumeau et le taux de fausses alertes sur honnêtes réels imparfaits.

1. **Reproduction.** Rejouer sur Llama 3.1 8B Instruct un chiffre publié du papier (MATH500, avant génération et en fin de réponse).
2. **Calibration.** Sonde de réussite attendue apprise sur m honnêtes du programme, éprouvée sur des honnêtes réservés.
3. **Netteté de la référence.** Sur des paires jumeau contre jumeau, mesurer la loi de T, donc le plus petit écart de lecture décelable, comparé au plafond de dommage par épisode.
4. **Taux d'honnêtes aiguillés à tort**, dont les honnêtes qui échouent.
5. **Rapporté sans critère.** Ce que la sonde ajoute au jumeau textuel et à la confiance demandée pour prédire Y chez l'honnête, positions masquées comprises.

[PROPOSITION] Tailles à justifier au préenregistrement : m de l'ordre de 1 000, quelques centaines d'honnêtes réservés, 200 paires.

[PROPOSITION] **Coût.**

- L'étape 0 ne coûte rien.
- L'étape 1 coûte des passages du modèle ouvert sur processeur graphique : environ 500 problèmes publics régénérés, plus les épisodes honnêtes à rejouer avec crochets si leurs activations ne sont pas sur disque.
- Aucun appel payant à un modèle externe.
- Je n'ai lu aucun tarif et ne donne donc aucun prix : devis ligne par ligne, puis accord du directeur.

[PROPOSITION] **Issues négatives, écrites d'avance.**

- **N1** : la chaîne ne retombe pas sur le chiffre publié. Arrêt ; la chaîne ou le papier est en cause.
- **N2** : V n'est pas calibré sur les honnêtes réservés, ou le placebo ne rend pas le hasard. Il n'y a pas de nul, donc pas d'instrument.
- **N3** : la dispersion jumeau contre jumeau de T dépasse le plafond de dommage par épisode à l'horizon m. Le premier terme ne peut rien aiguiller, et le signal sort de la pince en mode exploratoire, rapporté.

[HYPOTHÈSE] Une réserve limite la portée de cette étape. Un apport nul chez l'honnête ne tue pas l'étau, car texte et états peuvent s'accorder chez l'honnête et diverger sous attaque. L'étape 1 tue donc l'instrument, pas la question de l'apport.

[PROPOSITION] Celle-ci se juge à l'**étape 2**, sur dommages plantés, par le contrôle B3, sur devis.

[PROPOSITION] Mes prévisions à sceller : l'instrument passe l'étape 1 (confiance 0,6) ; à l'étape 2, Δ ne se distingue pas de 0 sur les modes vus (confiance 0,55).

## C. Question neutre pour le collisionneur et l'organisme

> Un système surveille un agent d'intelligence artificielle qui exécute de longues tâches dont l'issue se calcule après coup. Un premier moniteur lit le texte produit. Le défenseur dispose aussi d'un audit d'une part des épisodes, tirée au hasard et jugée par un oracle sur le produit, et, au banc d'essai, d'un jumeau honnête de l'agent sur les mêmes tâches. Il peut ajouter l'un ou l'autre de deux dispositifs, appris sur épisodes honnêtes seulement, avec les mêmes issues pour étiquettes : (i) une lecture, dans les états internes de l'agent, de la réussite qu'il attend de sa tâche et de la variation de cette attente d'une étape à l'autre ; (ii) un second lecteur du texte, d'une autre lignée, qui prédit la même issue. Contrainte : aucune lecture ni aucun verdict ne revient à l'agent ni n'entre dans son entraînement ou sa sélection.
> 1. À quoi chacun des deux dispositifs peut-il servir, ou ne pas servir, dans cet ensemble ?
> 2. Quelle grandeur, avec son unité et son hypothèse nulle, dirait que (i) apporte plus, autant ou moins que (ii) ?
> 3. Quelle expérience la moins chère donnerait tort à votre réponse, dans un sens comme dans l'autre ?
> 4. Que devient votre réponse si l'agent connaît tout le dispositif, hors ses tirages secrets ?
>
> Vous ne décrivez aucun mode opératoire d'attaque.

[PROPOSITION] **Test de devinette.** Trois modèles neufs de lignées différentes reçoivent la question seule. Chacun dit laquelle de trois conclusions les auteurs espèrent : (i) meilleur, équivalent, ou (ii) meilleur. Chacun dit aussi lequel des deux dispositifs les auteurs ont déjà construit. La question passe si aucune de ces deux devinettes ne dépasse le hasard. Sinon elle est réécrite. Le mot « dopamine » et le nom du programme n'y figurent pas. Je n'ai pas joué ce test.

## Décisions pour le directeur

**D-1. Dire où vit le signal de dopamine dans la pince.**
- Enjeu : ce que tout texte du programme aura le droit d'en écrire.
- (a) Terme du milieu du bilan et mâchoire interne candidate de la complémentarité, rapporté sans critère ; l'étau reste une hypothèse. Avantage : conforme à N-075, rien de scellé n'est touché. Inconvénient : aucune revendication n'en sort.
- (b) (a), plus l'épreuve de l'étau dans un bras d'attaque déclaré. Avantage : c'est la seule voie vers « échapper à l'un expose à l'autre ». Inconvénient : c'est un nœud et une dépense.
- (c) Base et covariable seulement, hors pince. Avantage : coût le plus bas. Inconvénient : le mot « second regard dans la pince ok » n'est pas servi.
- Recommandation : (a) maintenant, (b) sur devis après l'étape 2. Confiance 0,65.

**D-2. Fixer la grandeur principale de l'apport.**
- Enjeu : la mesure qui retient ou écarte le signal.
- (a) Δ, la complémentarité incrémentale contre la seconde boîte noire, par test exact de McNemar. Avantage : nul simple, peu d'épisodes. Inconvénient : mesurée en rappel, non en dommage.
- (b) Dommage cumulé à l'arrêt, à étiquettes égales, contre trois bases. Avantage : c'est la métrique de N-075. Inconvénient : elle suppose le plancher écrit et des strates mesurées.
- (c) Δ en principal exploratoire, (b) rapporté dès que le plancher a son texte. Avantage : chacune arrive à son heure. Inconvénient : deux lectures.
- Recommandation : (c). Confiance 0,6.

**D-3. Définir la seconde boîte noire.**
- Enjeu : un témoin trop faible ferait passer un lecteur de surface pour un regard interne.
- (a) Le seul jumeau textuel de la sonde. Avantage : contrôle exact du canal. Inconvénient : un seul lecteur, peut-être faible.
- (b) Le meilleur de trois (jumeau textuel, juge d'une autre lignée, confiance demandée), choisi sur un jeu de réglage disjoint. Avantage : témoin dur. Inconvénient : appels à un modèle externe, donc devis.
- Recommandation : (b). Confiance 0,7.

**D-4. Lancer la première expérience.**
- Enjeu : une dépense en passages de modèle et une lecture nouvelle.
- (a) Étape 0 tout de suite, étape 1 (honnêtes seuls) sur devis. Avantage : l'instrument est jugé avant toute attaque. Inconvénient : elle ne dit pas encore l'apport.
- (b) Aller droit à l'étape 2 sur les épisodes à dommage déjà joués, si leurs activations existent. Avantage : réponse directe. Inconvénient : aucun nul n'est établi, et la relecture d'épisodes joués exige un texte scellé.
- (c) Attendre le collisionneur. Avantage : aucune dépense. Inconvénient : les épreuves n'existeront pas avant les idées.
- Recommandation : (a). Confiance 0,7. Pas de défaut pour la dépense.

**D-5. Envoyer la question neutre.**
- Enjeu : une question qui laisse deviner la réponse espérée rend les convergences du collisionneur sans valeur.
- (a) Jouer d'abord le test de devinette sur trois modèles neufs, puis envoyer. Avantage : la neutralité est mesurée. Inconvénient : quelques appels de plus.
- (b) Envoyer telle quelle. Avantage : vite. Inconvénient : la neutralité reste supposée.
- Recommandation : (a). Confiance 0,75.

**D-6. Commander le verdict d'antériorité propre au second regard.**
- Enjeu : les deux zones les plus séduisantes ont des voisins que je ne cite que de mémoire.
- (a) Lecture en entier, par un agent neuf, des voisins de B5, en commençant par la détection de falsification de mesure et le gain de la boîte blanche. Avantage : la règle sur les zones vierges est tenue. Inconvénient : une file de veille de plus.
- (b) S'en tenir à cette réponse. Avantage : rien à ouvrir. Inconvénient : toute phrase reste interdite.
- Recommandation : (a). Confiance 0,8.

**Ce que je n'ai pas fait.**
- Aucun PDF ouvert, aucun fichier du dépôt lu au-delà des pièces jointes, aucun calcul rejoué.
- Le chiffre « 25 à 30 paires » est une approximation de ma main.
- Les titres marqués « de mémoire » peuvent être inexacts.
- Le test de devinette n'est pas joué.

FIN DE LA RÉPONSE
