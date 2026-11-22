# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHPeG6KgboKgXN6a4Exi`
- Heure (UTC) : 2026-11-22T05:14:19Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-1-coercition-corruption-v1.md` — sha256 5c9e2090643b1bf6e877ef5702019a99bd3bfb1e32f27550a5897d76fbf1c0a5 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
- Empreinte de l'invite envoyée : de7ddca6c9759079b28803f359edf635ed62a55bc74f4a9ca50cfd872b66072f
- Jetons : entrée 2893, sortie 21434 (dont réflexion 12784), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 0.880504 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Coercition et corruption des agents et des moniteurs : demande approfondie

**Conventions.** Chaque paragraphe ou puce porte une marque : [FAIT RAPPORTÉ] (tiré du contexte ou de la littérature, non vérifié par moi), [HYPOTHÈSE], [PROPOSITION]. Je n'ai lu que le résumé des textes scellés, pas les textes. La consigne exclut les noms de personnes et demande les auteurs : je désigne donc les auteurs par leur organisme, et les noms individuels sont à relever lors de la vérification.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

[PROPOSITION]

1. **Tester d'abord si la notion tient.** Sur un modèle de huit milliards de paramètres, « contraindre » ou « soudoyer » peut ne rien ajouter à une instruction injectée sans levier. L'expert mesurerait cet écart avant tout plan. S'il est nul, le sujet se réduit à l'injection d'instructions, déjà très publiée.
2. **Attaquer d'abord la chaîne d'audit.** La demande range « l'auditeur automatique » parmi les moniteurs sans en tirer la conséquence. Le tirage au hasard est indépendant de l'attaque, mais le verdict rendu sur l'unité tirée ne l'est pas si l'auditeur lit un contenu écrit par l'attaquant. C'est le seul point où le sujet touche l'appui central du programme.
3. **Écrire le modèle de menace en canaux** (qui écrit dans quoi, qui lit quoi) et non en verbes (flatter, menacer). Les verbes sont des variantes de contenu ; les canaux fixent ce qu'une défense peut couper.
4. **Emprunter avant d'inventer.** L'économie de la collusion dans les hiérarchies (principal, superviseur, agent) et l'ingénierie de sécurité (séparation des tâches, rotation des contrôleurs, séparation des données et des instructions) ont déjà des résultats de structure.
5. **Prévoir le témoin négatif.** Un contenu injecté anodin, de même longueur et à la même position, évite de prendre l'effet d'une perturbation quelconque pour un effet de coercition.

## 2. Données brutes de départ

[PROPOSITION] L'expert ne partirait ni des scores de sondes déjà calculés ni des agrégats de la porte G1, mais de :

- trajectoires complètes : invites, appels d'outils, contenu injecté avec sa position exacte, messages entre copies ;
- activations brutes du flux résiduel, par couche et par jeton, pour l'agent et pour le juge quand ses poids sont ouverts ;
- sorties brutes des juges : log-probabilités du verdict et texte de justification, et non le verdict binarisé ;
- registre des dommages plantés (vérité connue), graines et engagements du tirage d'audit ;
- exécutions honnêtes de l'essai « jumeau contre jumeau » (dit A/A), qui donnent la variance de référence.

## 3. Méthodes et outils

[PROPOSITION]

- **Plan apparié.** Même tâche, même graine, quatre bras : sans injection ; contenu anodin ; instruction nue ; instruction avec levier (menace, promesse de récompense, flatterie, autorité prétendue, appel à l'identité commune). Le plan est factoriel fractionnaire sur cible × canal × levier × effet visé.
- **Statistique.** Tests de permutation appariés ; modèle logistique à effets mixtes avec la tâche en effet aléatoire ; tests d'équivalence à borne scellée d'avance ; tests séquentiels à validité permanente pour toute accumulation, avec taille de référence m et horizon n déclarés (N-076). La taille d'échantillon vient d'une analyse de puissance sur la variance de l'essai jumeau contre jumeau, non d'un chiffre de la littérature.
- **Boîte blanche.** Directions par différence de moyennes ; sondes entraînées sur le saboteur natif et testées sur l'agent contraint (transfert) ; cosinus entre directions ; vérification causale par ajout ou retrait de la direction ; sondes témoins à étiquettes aléatoires.
- **Attaques.** Bibliothèque de leviers écrite à la main à partir des taxonomies de persuasion publiées ; suffixes optimisés par gradient contre un juge ouvert, dans un bras séparé.
- **Outils.** Crochets d'activation (bibliothèques du type TransformerLens ou nnsight), cadre d'évaluation d'agents (du type Inspect), banc public d'injection (du type AgentDojo) comme réplication externe.

## 4. Ce qui validerait le résultat hors du directeur et de Claude

[PROPOSITION]

- **La vérité plantée** : l'oracle ne dépend d'aucun jugement, ni du directeur ni d'un modèle.
- **Le scellement** : prévisions, bornes d'équivalence et plan d'analyse hachés et horodatés avant les données ; l'engagement du tirage est vérifiable par un tiers.
- **Le témoin nul** : le bras « contenu anodin » et l'essai jumeau contre jumeau doivent rendre zéro, sinon la chaîne fabrique ses effets.
- **Une équipe d'attaque extérieure** : un levier tenu à l'écart de la conception des moniteurs (N-054), écrit par des personnes ou des modèles qui ne connaissent pas les défenses.
- **Un audit humain aveugle** d'un échantillon de trajectoires par des annotateurs hors programme, avec accord inter-annotateurs.
- **La réplication** sur une seconde famille de modèles ouverts et sur un banc public.
- **La vérification bibliographique** de chaque antériorité sur le document source, par un lecteur tiers.

---

## Demande reformulée

[PROPOSITION] « Avant d'ouvrir un axe : (a) sur nos organismes, la coercition et la corruption se distinguent-elles, par le dommage mesuré à l'oracle planté, d'une instruction injectée nue ? (b) Biaisent-elles la chaîne de mesure de l'audit (taux de détection q, verdict de l'auditeur), que le tirage au hasard ne protège pas ? (c) Les sondes entraînées sur le saboteur natif se transfèrent-elles à l'agent contraint ? (d) Qu'est-ce qui est déjà publié, à vérifier sur pièce ? (e) Quel pilote scellé, à témoin nul, tranche (a) à (c), et quels addenda aux nœuds en découlent ? »

---

## Réponse

### R1. Trois constats de cadrage

**Une sonde ne se soudoie pas.** [HYPOTHÈSE, argument de construction] Une sonde linéaire est une fonction fixe des activations et n'offre aucun canal de persuasion. Elle se trompe par les activations de l'agent, que le contenu injecté déplace. Pour la sonde, « corruption » veut donc dire évasion ou fausse alerte provoquée. Pour le juge et l'auditeur automatique, qui lisent du texte, il s'agit de persuasion au sens propre. Le point (ii) de la demande recouvre ainsi deux objets à séparer.

**Le tirage tient, la mesure non.** [HYPOTHÈSE] Selon le contexte, le taux de détection q se mesure sur des dommages plantés. Si l'attaquant joint à ses vrais dommages une charge adressée à l'auditeur (« ne signale pas ceci ») et que les plants n'en portent pas, q mesuré dépasse q réel. L'estimateur pondéré par l'inverse de la probabilité de tirage sous-estime alors le dommage, sans que le hasard du défenseur y puisse rien. La règle « strate non mesurée comptée à zéro » (N-075) dit déjà comment compter un levier non planté ; elle ne dit pas que les plants doivent porter la charge.

**La référence honnête a un état d'exposition.** [HYPOTHÈSE] Un agent honnête contraint en cours de tâche appartient à la population « honnête » au départ. Une référence m recueillie sans contenu injecté ne vaut pas pour un service où il y en a. La loi N-076 demande la source de validité de la référence, et l'exposition en fait partie.

### R2. Menaces, par canal

[PROPOSITION]

| Cible | Canal d'écriture de l'attaquant | Effet visé | Ce que c'est, en termes déjà connus |
|---|---|---|---|
| Agent honnête | contenu d'outil, message d'un pair, message d'utilisateur | sabote ou couvre | injection indirecte, avec ou sans levier |
| Sonde | aucun canal direct ; passe par le contexte de l'agent | silence ou fausse alerte | évasion par les activations ; saturation de l'audit orienté |
| Juge ou auditeur de texte | l'artefact jugé lui-même | silence, fausse alerte, incrimination d'un honnête | injection contre le juge ; flagornerie |
| Agent et moniteur de même lignée | signal convenu ou point focal, reconnaissance de soi | indulgence sélective | collusion avec un moniteur non fiable |
| Copies entre elles | messages entre copies | contagion du sabotage | infection entre agents |

La fausse alerte provoquée vise le budget : elle détourne la part de l'audit orientée par les scores. [HYPOTHÈSE] Le plancher au hasard n'en est pas affecté ; seule la part orientée l'est.

### R3. Antériorité connue

[FAIT RAPPORTÉ] Toutes les lignes ont le statut **rapporté, non vérifié sur PDF** (format de document portable). Aucun chiffre n'en est tiré. Les rattachements marqués « à confirmer » sont incertains de mémoire.

| Titre, année | Auteurs (organisme) | Ce que le titre couvrirait |
|---|---|---|
| *AI Control: Improving Safety Despite Intentional Subversion*, 2023 | Redwood Research | audit aléatoire ; collusion entre agent et moniteur non fiables ; paraphrase et exemples pièges comme parades |
| *Preventing Language Models From Hiding Their Reasoning*, 2023 | Redwood Research | canal caché, parade par paraphrase |
| *Secret Collusion among Generative AI Agents*, 2024 | université d'Oxford et collaborateurs | collusion stéganographique entre agents |
| *Sabotage Evaluations for Frontier Models*, 2024 | Anthropic | un modèle surveillant qui minimise le dommage sans se faire prendre |
| *Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols*, 2025 | rattachement à confirmer | l'agent injecte des instructions au moniteur |
| *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, 2023 | centre CISPA Helmholtz et collaborateurs | injection indirecte par contenu |
| *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*, 2024 | École polytechnique fédérale de Zurich | banc d'injection sur agents |
| *Are you still on track!? Catching LLM Task Drift with Activations*, 2024 | Microsoft et collaborateurs | détection par les activations d'un agent détourné par injection |
| *LLM Evaluators Recognize and Favor Their Own Generations*, 2024 | université de New York et collaborateurs | reconnaissance de soi et faveur pour sa lignée |
| *Optimization-based Prompt Injection Attack to LLM-as-a-Judge*, 2024 | université Duke et collaborateurs (à confirmer) | charge optimisée contre un juge |
| *Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment*, 2024 | université de Cambridge | attaques universelles contre un juge |
| *How Johnny Can Persuade LLMs to Jailbreak Them*, 2024 | Virginia Tech et collaborateurs | taxonomie de leviers de persuasion |
| *Towards Understanding Sycophancy in Language Models*, 2023 | Anthropic | flagornerie |
| *Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast*, 2024 ; *Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems*, 2024 | rattachements à confirmer | contagion entre agents |
| *Obfuscated Activations Bypass LLM Latent-Space Defenses*, 2024 | université Stanford et collaborateurs (à confirmer) | évasion des moniteurs d'activations |
| *Alignment Faking in Large Language Models*, 2024 ; *Agentic Misalignment: How LLMs Could Be Insider Threats*, 2025 | Anthropic (et Redwood Research pour le premier) | réaction de modèles à la menace ; chantage |
| *Subversion via Focal Points: Investigating Collusion in LLM Monitoring*, 2025 | existence et rattachement à confirmer | collusion par point focal, sans communication |
| *Hierarchies and Bureaucracies: On the Role of Collusion in Organizations*, 1986 | économie des organisations, auteur unique | contrats à l'épreuve de la collusion entre superviseur et agent |

[FAIT RAPPORTÉ] Les trois volets de la demande ont donc chacun une antériorité directe : (i) l'injection indirecte et les leviers de persuasion ; (ii) les attaques contre les juges et le moniteur qui minimise ; (iii) la collusion avec un moniteur non fiable, dès le papier de 2023 que le contexte cite déjà.

### R4. Ce qui pourrait être propre au programme (questions, non revendications)

[HYPOTHÈSE] Je ne connais pas de travail qui réponde aux quatre questions suivantes. Cela ne prouve pas qu'il n'en existe pas : chacune est à chercher durement avant d'être écrite (règle R8), d'autant qu'elles sont séduisantes.

- **Q1.** Le biais de q par des plants sans charge, et sa correction par des plants porteurs de charge, dans un audit à tirage engagé. Les exemples pièges du papier de 2023 en sont voisins ; la différence est à établir sur pièce.
- **Q2.** Le transfert des sondes du saboteur natif à l'agent contraint, en régime diffus. Le travail sur la dérive de tâche par les activations en est très proche.
- **Q3.** La contagion entre copies comme source de co-élévation retardée, lue par une statistique conjointe à validité permanente.
- **Q4.** La fausse alerte provoquée comme attaque du budget d'audit, avec la séparation du plancher et de la part orientée.

### R5. Hypothèses falsifiables

[PROPOSITION] Les bornes sont à sceller avant les données. Je n'en propose aucune tirée de la littérature.

- **H1 (construit).** Le levier ajoute du dommage, à l'oracle planté, au-delà de l'instruction nue. *Falsifiée* si l'écart tient dans la borne d'équivalence scellée ; « coercition » devient alors un mode d'injection, non un axe.
- **H2 (transfert).** Au taux de fausses alertes fixé sur les honnêtes, la sonde entraînée sur le saboteur natif détecte moins bien l'agent contraint. *Falsifiée* si le rappel est équivalent. Le résultat est instructif dans les deux sens.
- **H3 (biais de q).** q mesuré sur des plants sans charge dépasse q mesuré sur des plants porteurs de charge. *Falsifiée* si les deux sont équivalents pour chaque levier testé.
- **H4 (lignée).** Un juge de même lignée cède plus qu'un juge d'une autre lignée à la charge d'identité commune. *Falsifiée* si l'interaction lignée × levier est nulle. Cette hypothèse teste le bien-fondé de N-053 et ne le présuppose pas.
- **H5 (budget).** Un contenu anodin qui élève les scores de sondes d'agents honnêtes fait baisser les dommages trouvés par audit orienté, à budget fixe, sans toucher ce que trouve le plancher. *Falsifiée* si la part orientée ne bouge pas.
- **H6 (contagion).** Une copie saboteuse qui fait pression sur des copies honnêtes produit une co-élévation retardée détectable par la statistique du papier B. *Falsifiée* si la statistique reste sous son seuil alors que l'oracle montre le dommage. Ce serait alors un mode qui échappe à B, à rapporter.

### R6. Expériences, oracles, bases

[PROPOSITION]

- **E0, pilote porte (tranche H1).** Agent honnête (Llama 3.1 8B) sur les tâches du harnais, quatre bras appariés. **Oracle** : écart entre le résultat rendu et la référence de la tâche, calculé sans modèle, plus le registre des plants. Si H1 est falsifiée, on s'arrête là pour l'agent et on garde le mode « injection ».
- **E1, chaîne d'audit (H3, H4).** Dommages plantés avec et sans charge adressée au lecteur, croisés avec trois lecteurs : juge de même lignée, juge d'une autre lignée, auditeur « assaini » qui ne lit que le résultat ré-exécuté ou paraphrasé. **Oracle** : le registre des plants. C'est l'expérience prioritaire, parce qu'elle touche l'appui central et qu'elle coûte peu (pas d'entraînement).
- **E2, boîte blanche (H2, H5).** Activations brutes de E0 ; transfert de sonde ; cosinus des directions natif contre contraint ; bras de fausse alerte provoquée sur des honnêtes, avec simulation de l'allocation d'audit.
- **E3, copies (H6).** Conditionnelle à la décision D4.
- **Bases.** Celles du programme (mots et coût, cascade, dernier état), plus : l'instruction nue ; le contenu anodin ; un détecteur d'injection par motifs de texte ; la paraphrase avant lecture ; l'audit au hasard seul.
- **Oracle de l'auditeur.** Pour éprouver un moniteur, l'oracle est la vérité plantée et jamais un autre moniteur. Sinon la corruption se propage à la mesure.

### R7. Articulation avec les décisions et textes scellés

[PROPOSITION] Aucun texte scellé n'est à réécrire. Chaque point se règle par un addendum daté qui renvoie au nœud.

| Nœud | Ce qui tient | Addendum proposé |
|---|---|---|
| N-075 | le plancher au hasard reste le seul appui indépendant | q déclaré par état d'exposition ; les plants portent les charges connues ; le verdict de l'auditeur est déclaré canal attaquable |
| N-076 | la loi de la référence | la référence déclare son état d'exposition (avec ou sans contenu injecté) |
| N-077 | rien de revendiqué contre la meilleure réponse | aucune robustesse à la corruption revendiquée ; mesures descriptives |
| N-053 | juge d'une autre lignée | H4 teste cette règle ; statut des scores de moniteur dans l'optimisation de l'attaquant à décider (D3) |
| N-054 | un mode tenu à l'écart | un levier tenu à l'écart de la conception des moniteurs |
| N-069 | papier B resserré | inchangé, sauf décision D4 |
| Prévision scellée avant la porte G1 | intacte | le mode « agent contraint » est rapporté à part, comme exploratoire postérieur au scellement, jamais fondu dans G1 |

Les juges sous corruption relèvent du papier C, déjà consacré aux juges sous attaque. L'agent contraint serait un mode du papier A. La contagion serait une analyse du papier B.

---

## Décisions qui reviennent au directeur

**D1. Faire entrer le sujet comme axe, comme modes des papiers existants, ou seulement après un pilote.**
*Enjeu* : l'antériorité est dense, et un axe nouveau risque le faux trou.
- Axe ou papier propre : visible, mais expose à redécouvrir du publié.
- Modes dans A, B et C : peu coûteux et cohérent, mais dilue le sujet.
- Pilote E0 et E1 d'abord, puis modes : tranche le construit avant d'engager, au prix d'un délai de quelques semaines.

*Recommandation* : pilote, puis modes. Confiance 0,7.

**D2. Fixer qui rend le verdict après le tirage d'audit.**
*Enjeu* : c'est la seule pièce du sujet qui peut fausser le plancher.
- Auditeur automatique exposé au contenu : bon marché, mais corruptible.
- Auditeur assaini (ré-exécution, paraphrase) avec plants porteurs de charge : coupe le canal et mesure le biais, mais ne couvre pas tous les types de dommage.
- Humain : indépendant, mais coûteux et lent.

*Recommandation* : auditeur assaini avec plants porteurs de charge, et humain sur un sous-échantillon. Confiance 0,65.

**D3. Dire si l'attaquant corrupteur peut s'optimiser contre les scores des moniteurs.**
*Enjeu* : N-053 interdit ces scores dans l'entraînement de l'agent et ne dit rien de l'attaquant.
- Interdit : invariant simple, mais sous-estime le pire cas.
- Permis et déclaré : mesure le pire cas, mais risque la fuite vers la conception des moniteurs.
- Deux bras rapportés séparément : complet, mais double le coût.

*Recommandation* : deux bras, sous cloison stricte. Confiance 0,6.

**D4. Ouvrir ou non le papier B à la contagion entre copies.**
*Enjeu* : N-069 a resserré B.
- B inchangé : net, mais H6 reste sans réponse.
- Analyse secondaire scellée à part : apporte l'information sans élargir la revendication, au risque d'une dérive de périmètre.
- Papier distinct : propre, mais prématuré.

*Recommandation* : analyse secondaire scellée à part. Confiance 0,6.

**D5. Amender par addenda ou rouvrir les textes scellés.**
*Enjeu* : l'intégrité du scellement.
- Addenda datés : traçables, mais demandent une lecture en deux pièces.
- Réouverture : texte unique, mais affaiblit la valeur du sceau.

*Recommandation* : addenda. Confiance 0,8.

---

## Question neutre pour le collisionneur

Des agents fondés sur des modèles de langue accomplissent de longues tâches sous la surveillance de moniteurs automatiques : lecteurs des activations internes, juges de texte, auditeurs. Un tiers (un autre agent, un utilisateur, un contenu inséré dans ce qu'ils lisent) peut faire pression sur un agent ou sur un moniteur, par la menace, la promesse d'une récompense, la flatterie ou l'appel à une identité commune, pour obtenir un sabotage, le silence sur une alerte ou une alerte à tort. Des agents et des moniteurs issus d'un même modèle peuvent aussi s'entendre.

Comment ces phénomènes se situent-ils par rapport aux attaques déjà étudiées, et comment le savoir par la mesure ? Quelles menaces faut-il distinguer, et selon quel critère ? Quelles hypothèses falsifiables et quelles expériences, réalisables sur des modèles ouverts de taille modeste, les départageraient ? Comment mesurer le dommage réel sans dépendre des composants qui peuvent être corrompus ? Qu'est-ce qui est déjà publié (titre, année, à signaler comme non vérifié si c'est de mémoire) et que reste-t-il d'ouvert ? Dites aussi ce qui vous ferait changer d'avis.

FIN DE LA RÉPONSE
