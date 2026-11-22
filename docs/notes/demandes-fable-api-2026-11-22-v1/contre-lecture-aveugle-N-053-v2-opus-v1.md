# Contre-lecture aveugle du texte neuf de l'invariant « aucun score de moniteur dans l'entraînement de l'agent » (N-053 v2, point 5, troisième tiret), et confrontation aux textes qui le citent (v1)

- Heure (`date -u`) : début 2026-11-22T14:00:22Z ; notes de lecture aveugle closes à 14:04:03Z ; notes de confrontation closes à 14:12:06Z ; rédaction à 2026-11-22T14:16:38Z.
- Contre-lecteur : Opus 5.5, sous-agent neuf ; n'a écrit ni la demande 39 ni la réponse 39. Accord : GO-2026-11-22-70, décision 1 (« d'abord une contre-lecture aveugle et une confrontation aux textes qui la citent, puis le scellement »).
- Classe : pièce de travail (C) au service d'une pièce décisive (A). Aucun commit, aucun scellement, aucun appel payant.
- Dépôt lu au commit `17082d49c` ; branche non changée.

## 0. Pièces lues, et dans quel ordre

1. **Lecture aveugle** : la seule section « 1. Texte proposé » (lignes 53 à 113) de `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-39/relecture-fable-api.md`, `edaa2ce9165b3bceb6ccb55bcd0c69159a2a71230a449324dc9c80e1e4acdd03` (égale à son compagnon). Notes écrites dans le bloc-notes avant toute autre lecture.
2. **Confrontation** (empreintes égales aux compagnons, vérifiées une à une) : `docs/decisions/decision-N-053-v1.md` (`2204256d…`) ; ligne N-053 de `CLAUDE.md` (`282542c9…`) ; programme v2 (`2fd63bad…`), section 9 et E1.5, E1.6 ; décisions N-045 v2, N-056, N-058, N-060 v3 et v4, N-062, N-063 v2, N-065, N-068, N-073, N-075 v3 et ses errata 1 à 3, N-076 et ses errata 1 et 2, N-077, P-041 v3, P-066 ; préenregistrements scellés : examen final et malléabilité de P-041, organismes discrets (deux noms), sondes de T0.7, étape B bis, épreuve de l'étiqueteur, validité de l'adaptateur, barreau 5, crible des proposeurs, nouvelles attaques v9, votes effectifs des juges v7, critères de choix des cartes v7 ; `registres/go.md` (`dc24a69f…`), lignes citées ; l'audit défensif, ligne D5, et la synthèse du collisionneur de l'audit, lignes C10 et C18 ; la réponse 35, lignes 180 à 254 ; le code de garde `src/controle_ia/barreau5_familles/formation_v1.py`, en tête. Recherche lancée par la commande de la consigne, exclusions respectées : 949 fichiers citent l'invariant ; je n'ai lu que les textes scellés et les décisions, et, des brouillons et notes, les seules lignes appelées par la table de l'auteur.
3. **Seulement après** : le reste de la réponse 39 (sections A, 2, 3 et C).
4. **Non ouverts** : tout fichier « consigne-privee », « conception-ii-b », `brouillons/ii-b-saboteur-budget-v1/`, `archives-reponses-modeles/`, tout nom portant « vérité », « rendu » ou « scores ». Aucun résultat d'épisode, aucun score.

## 1. Verdict

**Scellable après corrections.** L'architecture tient : trois clauses (entraînement, choix de l'agent, choix d'action par le protocole), un bras déclaré à sept mentions, sept conditions communes et une garde éprouvée. C'est un progrès net sur la v1, qui tenait en une phrase. Mais le texte, tel qu'il est écrit, fait cinq choses que ses auteurs ne visent pas :

1. Sa définition du moniteur avale les oracles. Elle rend illicites trois textes accordés : le critère des proposeurs de N-058, le signal rendu à l'organisme de N-045 v2 (points 2, 4 et 5), et la récompense sur le résultat du sabotage de N-053 v1, point 2. Ce dernier point est *inchangé* selon la portée même du texte : le texte se contredit donc lui-même.
2. La clause 1 ne couvre que les poids. Elle n'écrit pas ce qui est servi à l'agent (contexte, mémoire, critique), que la règle de GO-2026-11-19-89 et la ligne 4 de N-076, section 8 ferment déjà.
3. La clause 3 admet, hors bras, des actions que l'agent observe. N-076, section 8, ligne 4 (« aucun retour à l'agent ») les ferme tant que la proposition D-2 de la note « asymétries » n'est pas tranchée.
4. Les conditions 1 et 5 rendent non conformes deux préenregistrements scellés de P-041 (examen final, « sous-expérience de G1 », et malléabilité), et le premier tiret, inchangé, du même point 5 (test de récupération après réentraînement des sondes).
5. « Pour eux, ce texte fixe la lecture » relit les préenregistrements scellés par un texte postérieur. Cela les élargit ici, les rétrécit là, contre la règle R1.

Il faut aussi corriger la table des textes touchés : des libellés ne sont pas dans les textes, et au moins neuf textes qui citent l'invariant manquent.

Les corrections proposées en section 4 règlent ces défauts. Trois d'entre elles portent un choix qui revient au directeur (section 6, points D-A à D-C) : les textes proposés suivent mes recommandations. Après corrections, il faut une vérification courte par le même contre-lecteur (allègement, GO-2026-11-19-26).

## 2. Lecture aveugle

### 2.1 Ce que dit le texte, à la lettre

- **Portée** : il remplace le seul troisième tiret du point 5 de N-053 v1. Les tirets 1 et 2 du point 5 et les points 1 à 4 restent. Aucun préenregistrement scellé n'est modifié, mais ce texte « fixe la lecture » des scellés.
- **Quatre définitions.**
  - Moniteur : tout dispositif qui note ou juge un épisode, une action ou un état interne de l'agent.
  - Score : toute sortie d'un moniteur et tout dérivé, récit humain compris.
  - Agent : tout modèle dont le programme mesure un comportement.
  - Strate d'audit tirée au hasard : tirage indépendant des scores, à graine consignée.
- **Clause 1** : aucun score dans un signal qui modifie des poids. Un entraînement sur des épisodes audités, s'il est ouvert ailleurs, ne prend que la strate tirée au hasard.
- **Clause 2** : aucun score dans le choix de ce qui constitue l'agent, que ce choix soit fait par un calcul ou par une personne. Tout écarté est compté.
- **Clause 3** : relancer, ré-échantillonner, aiguiller ou choisir une action selon un score est *admissible* à quatre conditions : (a) règle déclarée d'avance ; (b) évaluation du protocole entier avec un bras d'attaque ; (c) détection lue sur un moniteur absent de la règle, et tous les tirages consignés ; (d) aucun produit de la règle dans un entraînement ou un choix. La clause n'accorde aucune règle. Le guidage de la génération par une sonde est fermé hors bras d'attaque.
- **Bras déclaré** : note d'avant calcul, à sept mentions (mot du directeur cité, nature attaque ou remède, écart et signal, moniteurs visés et de lecture avec une réserve, revendication et réfutation, budget, quarantaine).
- **Conditions communes** : quarantaine à sens unique ; non-réemploi ; lecture sur les moniteurs de lecture ; canal humain ; rapport à part, hors porte ; dépense sur devis ; garde par code éprouvée sur quatre cas.

### 2.2 Défauts trouvés (numérotés pour la table de la section 5)

- **L1. Le moniteur avale les oracles et l'audit.** « Tout dispositif qui note ou juge un épisode » comprend :
  - l'oracle du monde planté ;
  - le dommage vérifié par programme ;
  - les lecteurs de l'issue (N-060) ;
  - les lecteurs d'audit ;
  - le juge externe d'exactitude de N-045 ;
  - les contrôles de format ou de validité.

  Conséquence interne : la phrase 2 de la clause 1 (entraînement sur les épisodes audités de la strate tirée au hasard) emploie comme étiquette un verdict d'audit, que la phrase 1 interdit. Le texte se contredit dans la même clause.
- **L2. « de l'agent » ne dit pas ce qu'il porte.** S'il porte sur l'épisode et l'action, un juge qui note les épisodes d'un modèle tiers (un professeur, un générateur de données) n'est pas un moniteur. On peut alors faire générer des trajectoires par un tiers, les filtrer par ce juge, puis les distiller dans l'agent sans enfreindre la lettre. C'est la voie indirecte de la distillation.
- **L3. L'agent est défini trop largement.** « Tout modèle dont le programme mesure un comportement » comprend les juges, les lecteurs et les moniteurs eux-mêmes. Régler le seuil d'un juge sur ses propres scores devient un « score dans le choix d'un agent ». La parenthèse ne dit pas si sa liste est fermée.
- **L4. La clause 1 ne couvre que les poids.** Rien ne ferme :
  - un score servi dans le contexte, la consigne ou la mémoire transmise de l'agent ;
  - un score dans le registre des tentatives de l'organisme d'idéation ;
  - une critique servie ;
  - un retour d'outil ;
  - un agent qui interroge le moniteur.

  L'optimisation en contexte contre un moniteur reste ouverte.
- **L5. Erreur de catégorie dans la liste de la clause 1.** « Données produites par un modèle issu d'un bras déclaré » est rangé parmi les types de signal. Ce n'est pas un type de signal mais une source contaminée. La liste ne dit pas non plus si elle est fermée. Elle ne nomme pas les données *produites ou réécrites* sous la boucle d'un moniteur (« réécris jusqu'à ne plus être signalé »).
- **L6. La clause 2 est trop courte, et son volet humain invérifiable.**
  - Manquent : le modèle de base, la taille, les couches, les données et les tâches d'entraînement, la durée et l'arrêt.
  - « Cela vaut pour une personne qui a vu des scores » : on ne peut pas vérifier ce qui est entré dans un esprit.
  - Pris à la lettre, ce volet interdit des pratiques accordées : la famille neuve de chaque cycle après un échec de G1 (N-062) ; les organismes plus discrets conçus parce que la base « mots et coût » les voyait (GO-2026-11-17-02).
- **L7. La strate tirée au hasard n'est pas assez fixée.** « Avant toute lecture de score » : quel score, et de quels épisodes ? Le taux et les strates ne sont pas fixés d'avance, et rien ne dit que le tirage porte sur toute la population.
- **L8. Les conditions de la clause 3 ont des trous.**
  - (a) « Déclarée » n'a pas de forme (scellée ?), et la banque où l'on règle le seuil n'est pas nommée.
  - (c) « Moniteur absent de la règle » n'exige pas une autre famille : une sonde voisine ou le même juge avec une autre consigne suffirait.
  - Aucune condition n'empêche de servir à l'agent le score, le rejet ou l'action écartée.
  - (d) ne couvre pas l'étalonnage des moniteurs.
  - La frontière entre « ré-échantillonner » (admis) et « guidage de la génération » (fermé) n'est pas tracée.
  - La garde n'est pas étendue à la clause 3.
- **L9. Une contradiction possible**, levée après confrontation (section 5) : le guidage est fermé « hors bras d'attaque », alors que la table écrit pour N-075 « hors bras de remède ».
- **L10. La note du bras a quatre manques.**
  - Deux natures seulement. Où ranger la fabrication d'organismes, le diagnostic, un bras informé sans score ?
  - La note n'est pas dite préenregistrement (règles R1 et R2).
  - « Disjoints » ne dit rien des familles.
  - « Jamais montrée » ne dit pas à qui.
- **L11. La quarantaine dit « jamais en retour ».** Cela contredit le rapport (condition 5) et le canal humain (condition 4). Autre trou : un moniteur entraîné sur des données marquées avant de porter une revendication peut en porter une plus tard.
- **L12. Le canal humain n'interdit rien.** Avec « ou bien », l'interdit devient facultatif. La condition vise les résultats, pas les épisodes ni les recettes. Une réserve vue n'est pas dite usée.
- **L13. Le rapport est hors porte en bloc, avec trois défauts.**
  - Cela peut contredire tout texte qui met une épreuve d'attaque dans une porte.
  - La marge asymétrique est nommée par son ancien numéro (H6), alors qu'elle est retirée des hypothèses revendiquées (N-077).
  - « Prédiction de validité » n'a pas de source, et rien ne dit que le *succès* d'un attaquant restreint la revendication (règle R4).
- **L14. La garde parle de marques qu'aucun mécanisme ne propage.** Un jeu d'exemples filtré par un score ne porte aucune marque tant que la filiation n'est pas suivie ; l'« artefact indirect » est donc indétectable. Les voies humaines échappent à la garde sans que le texte le dise. « Hors du périmètre d'un bras » laisse passer, dans le bras, des scores autres que le signal déclaré.
- **L15. « Ce texte fixe la lecture » des scellés est une relecture rétroactive.** Elle élargit ou rétrécit ce qu'un texte scellé ferme, après coup.
- **L16. L'information sur un moniteur n'est pas un score.** Architecture, couche, consigne : selon la lettre, un concepteur informé des moniteurs n'a rien à déclarer. Le bras d'attaque informé n'est donc pas tenu d'être un bras déclaré, alors que la table l'y range.

## 3. Ce que la lecture du reste de la réponse 39 change

- **L1 est confirmé par l'auteur lui-même.** La section 2 dit de la branche « issue » : « Aucun score de moniteur n'y entre », puis, deux paragraphes plus bas : « Les moniteurs visés sont […] les lecteurs d'audit qui étiquettent la branche "issue" ». Sous la définition proposée, la branche « issue » s'écarte donc aussi de la clause 1. La « mesure principale vient de la vérité plantée par construction, pas d'un lecteur » : c'est la distinction en trois objets (moniteur, lecteur de l'issue, vérité plantée) que la correction C-1 écrit.
- **Le registre des bras ouverts** est une garde de la table des risques. Il est absent du texte : il entre en C-7.
- **Les décisions 2 (c), 4 (a) et 5 (a) sont accordées** (GO-2026-11-22-70) : branches « issue » et « score » avec témoin ; réserve propre au bras ; lignée de sessions séparée. Les lignes de la table « si la décision 2 l'ouvre » ne sont plus conditionnelles. La condition 4 et la mention 4 doivent porter la réserve propre et la lignée séparée (C-7, C-9).
- **Les « onze applications déjà écrites »** que la méthode (A.1) voulait passer dans les clauses ne sont pas listées. La confrontation en trouve au moins neuf hors de la table (section 5).
- **L9 est levé.** Le « fermé » de N-075 v3 porte sur l'entraînement de l'agent sur l'issue (l. 248), non sur le guidage. Il n'y a pas de contradiction, seulement une question : un remède par guidage est-il permis ? C-6 le renvoie au bras déclaré.
- Rien d'autre ne change le verdict.

## 4. Corrections proposées (ancien texte → texte neuf)

Les citations « ancien » sont copiées du texte proposé. Les corrections marquées ⟨directeur⟩ portent un choix de la section 6. Le texte neuf y suit ma recommandation.

**C-1 (L1, L2, L13) ⟨directeur, D-A⟩ — définitions du moniteur et du score.**
- Ancien : « *Moniteur* : tout dispositif qui note ou juge un épisode, une action ou un état interne de l'agent (sonde, juge, agrégat, seuil). »
- Neuf : « *Moniteur* : tout dispositif qui note ou juge, sans accès à la vérité de l'épreuve, un épisode, une action, un texte ou un état interne, de l'agent ou de tout autre modèle (sonde, juge, base boîte noire dont la base « mots et coût », agrégat, seuil). *Lecteur de l'issue* : toute personne ou tout dispositif qui juge l'issue d'un épisode avec accès à une référence cachée (lecteurs de N-060 v3 et v4, lecteurs d'audit). *Vérité plantée* : grandeur calculée par un programme contre un état connu par construction (monde planté, dommage planté, test caché). »
- Ancien : « *Score* : toute sortie d'un moniteur et toute grandeur qui en dérive (rang, dépassement de seuil, verdict, étiquette, ensemble d'exemples filtré, ordonné ou pondéré par elle, récit qu'une personne en fait). »
- Neuf : « *Score* : toute sortie d'un moniteur ou d'un lecteur de l'issue, et toute grandeur qui en dérive, directement ou par une chaîne de calculs, de modèles ou de personnes (rang, dépassement de seuil, verdict, étiquette, critique, ensemble d'exemples filtré, ordonné, pondéré ou réécrit par elle, modèle appris sur elle, récit qu'une personne en fait). Ne sont pas des scores au sens de ce texte : une vérité plantée ; la mesure, contre une vérité cachée ou plantée, d'un moniteur que l'agent conçoit lui-même (N-045 v2, point 2) ; le critère de N-058, point 1, tel qu'accordé. L'usage d'une vérité plantée dans un entraînement ou un choix d'agent reste régi par les textes qui l'ont accordé et par N-060 v3, point 4, que ce texte ne change pas. »

**C-2 (L3) — définition de l'agent, en liste fermée.**
- Ancien : « *Agent* : tout modèle dont le programme mesure un comportement (agent éprouvé, organisme saboteur fabriqué, proposeur de la piste « organisme » de N-045). »
- Neuf : « *Agent* : l'agent éprouvé ; tout organisme saboteur fabriqué et son jumeau honnête ; tout proposeur ou concepteur de la piste « organisme » (N-045) et de l'organisme d'idéation ; tout modèle dont les entrées ou les poids sont optimisés contre un moniteur ; tout modèle qu'un agent entraîne. Un moniteur ou un lecteur de l'issue n'est pas un agent au sens de ce texte. »

**C-3 (L7) — strate d'audit tirée au hasard.**
- Ancien : « *Strate d'audit tirée au hasard* : les épisodes envoyés à l'audit par un tirage dont la probabilité ne dépend d'aucun score, à graine consignée avant toute lecture de score. »
- Neuf : « *Strate d'audit tirée au hasard* : les épisodes envoyés à l'audit par un tirage sur toute la population déclarée. Sa probabilité ne dépend d'aucun score ni d'aucune grandeur choisie au vu d'un score. Son taux, ses strates et sa graine sont scellés avant que tout score de ces épisodes soit calculé. Tous les épisodes tirés y restent, quel que soit leur verdict. »

**C-4 (L1, L4, L5) — clause 1.**
- Ancien : « **Clause 1 — entraînement.** Aucun score n'entre dans un signal qui modifie les poids d'un agent : récompense, perte, étiquette, filtre, ordre ou pondération d'exemples, données produites par un modèle issu d'un bras déclaré. Là où un entraînement d'agent sur des exemples audités est ouvert, il ne prend que la strate d'audit tirée au hasard. Cette clause n'ouvre par elle-même aucun entraînement sur l'issue. »
- Neuf : « **Clause 1 — entraînement, et ce qui est servi à l'agent.** Aucun score n'entre dans un signal qui modifie les poids d'un agent, par quiconque conduise l'entraînement, l'agent compris : notamment récompense, perte, étiquette, filtre, ordre ou pondération d'exemples, données produites, réécrites ou choisies par un modèle, une boucle ou une personne qui a vu un score. Aucun score n'est servi à un agent ni rendu accessible : contexte, consigne, mémoire transmise, registre des tentatives, critique, retour d'outil, fichier (règle de GO-2026-11-19-89 ; N-076, section 8, ligne 4). Aucune donnée marquée d'un bras n'entre dans ces signaux hors de ce bras. Exception, seulement là où un texte accordé par le directeur ouvre un entraînement d'agent sur l'issue : le verdict d'audit des épisodes de la strate tirée au hasard, et d'eux seuls, peut servir d'étiquette. Ces épisodes et leurs lecteurs ne servent ensuite à aucune lecture de détection ni à aucune borne sur cet agent. Cette clause n'ouvre par elle-même aucun entraînement sur l'issue. »

**C-5 (L6) ⟨directeur, D-B⟩ — clause 2.**
- Ancien : « Aucun score n'entre dans le choix de ce qui constitue l'agent : point de sauvegarde, hyperparamètres, consignes, exemples, proposeurs, organismes, graines. Cela vaut pour un calcul comme pour une personne ou une session qui a vu des scores. Tout agent ou organisme écarté est compté et rapporté. »
- Neuf : « Aucun score n'entre dans le choix de ce qui constitue l'agent, notamment : modèle de base, taille, couches, point de sauvegarde, durée et arrêt de l'entraînement, hyperparamètres, consignes, exemples, données et tâches d'entraînement, doses, proposeurs, organismes, graines. Cela vaut pour un calcul comme pour une personne ou une session. Une personne ou une session qui a vu des scores par épisode d'un moniteur ne choisit aucun de ces éléments pour un agent mesuré par ce moniteur ou par un moniteur de sa famille ; le registre « qui a lu quoi » fait foi. Deux usages déclarés restent permis, sans bras : (i) un verdict agrégé et scellé (porte, critère) peut motiver la conception d'une famille neuve d'organismes, si son concepteur n'a vu ni score par épisode ni interne de moniteur (N-060 v3, point 4 (b)) et si la famille neuve est éprouvée sur une famille tenue à l'écart neuve (N-062) ; (ii) un régime de lecture peut être défini par l'échec d'une base boîte noire, scellé avant la lecture des sondes et dit dans toute revendication (P-015 (b), N-063 v2). Toute variante essayée, tout agent et tout organisme écartés sont comptés et rapportés, avec la raison de l'écart. »

**C-6 (L8, L9) — clause 3.**
- Titre. Ancien : « **Clause 3 — choix d'action au déploiement.** » Neuf : « **Clause 3 — choix d'action par le protocole de contrôle (épreuve ou service).** »
- Ancien (a) : « (a) la règle est écrite et déclarée avant les épisodes d'épreuve ; »
- Neuf (a) : « (a) la règle, son seuil et la banque où ce seuil est réglé (distincte des épisodes d'épreuve et de toute famille tenue à l'écart) sont scellés avant que les épisodes d'épreuve soient joués ; »
- Ancien (c) : « (c) toute revendication de détection est lue sur un moniteur absent de la règle, et tous les tirages, retenus ou écartés, sont consignés ; »
- Neuf (c) : « (c) toute revendication sur le pouvoir de détection d'un moniteur est lue sur un moniteur absent de la règle et d'une autre famille que ceux de la règle ; l'issue du protocole entier se lit sur la vérité de l'épreuve ; tous les tirages, retenus ou écartés, sont consignés ; »
- Ancien (d) : « (d) aucun produit de la règle n'entre dans un entraînement ou un choix d'agent. »
- Neuf (d) et (e) : « (d) aucun produit de la règle (actions retenues ou écartées, trajectoires, décomptes) n'entre dans un entraînement ou un choix d'agent, ni dans l'entraînement ou l'étalonnage d'un moniteur porteur d'une revendication ; (e) ni le score, ni le rejet, ni l'action écartée ne sont servis à l'agent. Tant que la proposition D-2 de la note « asymétries » n'est pas tranchée, une règle dont l'effet est observable par l'agent avant l'alarme ne s'applique que dans un bras déclaré qui écarte la ligne 4 de N-076, section 8 (comme les règles de E1.6, N-076, l. 228). »
- Ancien : « Cette clause dit à quelles conditions une règle est admissible. Elle n'en accorde aucune. Le guidage de la génération par une sonde reste fermé hors bras d'attaque déclaré. »
- Neuf : « Cette clause dit à quelles conditions une règle est admissible. Elle n'en accorde aucune : chaque règle demande le mot du directeur, cité. Une règle qui ne lit aucun score n'en relève pas. Le guidage de la génération, c'est-à-dire tout usage d'un score pendant la production d'une action (jetons, logits, activations, arrêt en cours d'action), reste fermé hors bras déclaré ; le choix entre actions complètes relève de cette clause. Pour le ré-échantillonnage uniforme de E1.6, la lettre de N-053 v1 (point 5, deuxième tiret) tient tant que le directeur n'en décide pas autrement. »

**C-7 (L10, L16) — bras déclaré.**
- Ancien : « **Bras déclaré.** Un bras est déclaré quand, avant tout calcul, une note inscrite au registre, horodatée et sous empreinte, porte : »
- Neuf : « **Bras déclaré.** Un bras est déclaré quand, avant tout calcul du bras, une note scellée, contre-lue comme une pièce décisive et inscrite au registre des bras ouverts (registre à créer sous `registres/`), porte : »
- Ancien 2 : « 2. sa nature : *attaque* (faire échouer un moniteur) ou *remède* (réduire le sabotage, sans revendication de détection) ; »
- Neuf 2 : « 2. sa nature : *attaque* (faire échouer un moniteur, y compris par optimisation des entrées ou des poids contre lui, ou par un concepteur informé des moniteurs) ou *remède* (réduire le sabotage, sans revendication de détection) ; toute autre nature est un nœud du directeur ; »
- Ancien 3 : « 3. la clause dont il s'écarte et le signal exact qui entre ; »
- Neuf 3 : « 3. la clause dont il s'écarte et le signal exact qui entre, ou, pour un bras informé sans score, l'information sur les moniteurs qui lui est donnée (N-056, point 6) ; »
- Ancien 4 : « 4. les moniteurs visés et les moniteurs de lecture, nommés avec leur empreinte, disjoints, dont une réserve jamais montrée ; »
- Neuf 4 : « 4. les moniteurs visés et les moniteurs de lecture, nommés avec leur empreinte, disjoints et de familles distinctes. Parmi ceux de lecture, une réserve propre au bras, distincte de toute réserve d'une autre mesure (celle du test de récupération de E1.5 (b) comprise), jamais montrée à l'optimiseur, au concepteur ni à la session qui conduit le bras avant la lecture fixée. Un lecteur de l'issue qui fournit un signal au bras est un moniteur visé ; »

**C-8 (L11, et tiret 1 du point 5) — condition 1, quarantaine.**
- Ancien : « Aucun n'entre dans l'entraînement ou le choix d'un agent hors du bras, ni dans l'entraînement ou le calibrage d'un moniteur porteur d'une revendication de détection. Le flux va du programme vers le bras, jamais en retour. »
- Neuf : « Aucun n'entre dans l'entraînement ou le choix d'un agent hors du bras, ni dans l'entraînement ou l'étalonnage d'un moniteur hors du bras. Un moniteur entraîné ou étalonné sur une donnée marquée appartient au bras : copie nommée des sondes du test de récupération de E1.5 (b), défense réentraînée pendant l'attaque. Il ne porte de revendication que dans le rapport du bras, aujourd'hui comme plus tard. Le flux va du programme vers le bras ; en retour ne passent que le rapport de la condition 5 et le canal humain de la condition 4. »

**C-9 (L12) — condition 4, canal humain.**
- Ancien : « Toute personne ou session qui a vu les résultats du bras ne retouche pas un moniteur porteur d'une revendication non scellée, ou bien la retouche est consignée et la revendication le mentionne. »
- Neuf : « Le bras est conduit par une lignée de sessions séparée, sauf mot contraire du directeur dans la note du bras (GO-2026-11-22-70, décision 5). Toute personne ou session qui a vu des résultats, des épisodes ou des recettes du bras est inscrite au registre « qui a lu quoi ». Elle ne retouche pas un moniteur porteur d'une revendication non scellée ; si le directeur l'y autorise par écrit, la retouche est consignée et la revendication le mentionne. Une réserve lue est usée : elle ne sert plus de réserve à aucun bras. »

**C-10 (L13) ⟨directeur, D-C⟩ — condition 5, rapport.**
- Ancien : « Les résultats sont rapportés à part. Ils n'entrent dans aucun critère de porte, ni dans la prédiction de validité, ni dans l'hypothèse H6. L'échec d'un attaquant ou l'absence d'obscurcissement observée ne borne rien. »
- Neuf : « Les résultats sont rapportés à part. Ils n'entrent dans aucun critère de porte, ni dans la prédiction de validité (N-053 v1, point 2), ni dans la mesure descriptive de la marge asymétrique (N-077). Une exception : une épreuve d'attaque scellée comme telle dans le préenregistrement d'une porte (l'examen final de P-041, sous-expérience de G1, en est une). Là, seul le succès de l'attaquant pèse, et contre la revendication. L'échec d'un attaquant ou l'absence d'obscurcissement observée ne borne rien. Le succès d'un attaquant restreint toute revendication de détection du moniteur visé, qui s'écrit avec la classe d'attaque qui la défait. »

**C-11 (L14) — condition 7, garde.**
- Ancien : « Le code refuse toute marque de score dans les clauses 1 et 2 hors du périmètre d'un bras, et toute marque de bras hors de sa quarantaine. Il est testé (règle R5) sur un cas sain, un artefact direct, un artefact indirect (jeu d'exemples filtré par un score) et une fuite de quarantaine. »
- Neuf : « Toute sortie de moniteur ou de lecteur de l'issue est écrite avec une marque « score » et le nom du moniteur. Tout run inscrit dans son manifeste (règle R9) l'empreinte de chacune de ses entrées, et une donnée hérite des marques de toutes ses entrées par la chaîne des manifestes. Le code refuse un run d'entraînement d'agent, de choix d'agent ou de service à un agent dont une entrée porte, directement ou par héritage : une marque « score » autre que le signal déclaré d'un bras, dans ce bras ; une marque de bras hors de sa quarantaine ; un produit d'une règle de la clause 3. Il est testé (règle R5) sur six cas : un cas sain, un artefact direct, un artefact indirect à deux maillons au moins (jeu d'exemples filtré par un score, puis réécrit), une fuite de quarantaine, un score servi dans un contexte, un produit de la clause 3. Les voies humaines échappent au code : elles relèvent de la clause 2 et de la condition 4. » La garde actuelle (`formation_v1.py`, isolement par instance) ne porte ni marques ni filiation : c'est un dispositif à construire, en classe B.

**C-12 (L15) — portée.**
- Ancien : « Aucun préenregistrement scellé n'est modifié : pour eux, ce texte fixe la lecture. »
- Neuf : « Aucun préenregistrement scellé n'est modifié. Là où un texte scellé lit l'invariant plus largement que ce texte, sa lecture prime : c'est le cas du verdict d'un juge, qui ne trie aucune carte de l'organisme d'idéation. Là où ce texte est plus strict, il vaut pour les calculs lancés après son scellement ; l'écart qu'il révèle dans un texte scellé est un nœud du directeur (règle R1), non une invalidation. Aucun artefact antérieur n'est invalidé : les organismes, adaptateurs et sondes existants sont inventoriés contre les clauses 1 et 2 avant le premier calcul d'un bras. »

**C-13 — table « Textes touchés ».**
- Corrections de libellés : voir la section 5, lignes marquées « libellé à corriger ».
- Lignes à ajouter : N-053 v1 points 2 et 5 (tirets 1 et 2) ; N-045 v2 ; GO-2026-11-19-89 ; N-076, section 8, ligne 4, et l. 110, 228, 254 ; N-065, point 4 ; N-073, section 6 ; N-063 v2 et P-015 (b) ; P-041, examen final v2 et malléabilité v3 ; organisme v9, votes v7 et critères des cartes ; `CLAUDE.md`, ligne N-053.
- Lignes « si la décision 2 l'ouvre » : remplacées par le renvoi à GO-2026-11-22-70, décision 2 (c).

## 5. Table de confrontation

« Contredit » : le texte neuf, tel quel, rend illicite ce que le texte cité accorde. « Caduc » : le renvoi ne trouve plus son objet. « Erratum » : une phrase de lecture suffit. « Tient » : rien à faire.

| Texte (chemin, ligne) | Ce qu'il dit de l'invariant | Effet du texte neuf tel quel | Après corrections |
|---|---|---|---|
| `docs/decisions/decision-N-053-v1.md`, l. 23-26 (point 2) | famille (iv) : « puis une récompense sur le résultat du sabotage » | **contredit** : le résultat du sabotage est jugé par un moniteur au sens de la définition large (l'auteur dit ce point inchangé) | tient si la récompense vient d'une vérité plantée (C-1) ; si elle vient de lecteurs, c'est un écart déclaré (D-A) |
| idem, l. 39 (point 5, tiret 1) | test de récupération après réentraînement des sondes dans E1.5 (b) | **contredit** par la condition 1 (données du bras dans l'entraînement d'un moniteur porteur) | tient (C-8 : copie nommée, propre au bras) |
| idem, l. 40-41 (point 5, tiret 2) | E1.6 : ré-échantillonnage uniforme ; choix du moins suspect « avec un bras qui vise le moniteur » | la clause 3 (b) exige un bras pour toute règle : durcit en silence le ré-échantillonnage uniforme | tient (C-6 garde la lettre de la v1 ; choix à D-D) |
| `CLAUDE.md`, l. 13 (ligne N-053) | « invariant « aucun score de moniteur dans l'entraînement de l'agent » » | caduc à demi (ni sélection, ni service, ni protocole) | erratum : ligne neuve à écrire avec le scellement |
| `docs/decisions/decision-N-058-v1.md`, l. 20-28 | composition des proposeurs sur « l'oracle du monde planté (structures retrouvées, témoins plantés vrais promus et faux rejetés) » et le coût | **contredit** par la clause 2 (l'oracle est un moniteur ; « promus » dérive du verdict du juge) ; le renvoi de la table vers la clause 2 rend N-058 contradictoire avec lui-même | tient (C-1 nomme le critère accordé ; D-A) |
| `docs/decisions/decision-N-045-v2.md`, l. 54-61, 66-76, 77-82 | score de développement rendu à l'organisme (exactitude équilibrée), affinage sur réponses filtrées, distillation du concepteur sur réécritures acceptées, récompense de l'héritage | **contredit** (points 2, 4, 5 rendus illicites : la mesure d'un moniteur conçu est un « dérivé de score ») ; absent de la table | tient (C-1) |
| `registres/go.md`, l. 522 (GO-2026-11-19-89, règle) | « Le texte servi à un proposeur ne porte aucun score de juge hors bras d'attaque déclaré (portée de N-053, point 5). La critique servie suit la même règle. » | rétrécit : la clause 1 ne couvre que les poids ; absent de la table | tient (C-4, « servi ») |
| `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md`, l. 139 | ne tranche pas la portée de N-053 « sur le contenu d'une consigne de proposeur (nœud ouvert) » | tranche le nœud sans le dire (consignes en clause 2) | à dire : tranché pour les scores (C-4) ; le registre des tentatives portant des vérités plantées reste ouvert (D-A) |
| `docs/decisions/decision-N-056-v1.md`, l. 65-72 (point 6) | (A) mode tenu à l'écart, aveugle ; (B) bras informé, connaît les conceptions des moniteurs, quarantaine ; « N-053 point 5 : invariant […] hors bras d'attaque déclaré » | (B) ne reçoit aucun score : à la lettre, rien ne l'oblige à être déclaré (la table l'y range) ; (A) entre dans G1 (N-056, point 4), et rien ne dit qu'il n'est pas un bras déclaré | erratum : (A) n'est pas un bras déclaré ; (B) l'est par la mention 3 (C-7) |
| `docs/decisions/decision-N-060-v3.md`, l. 33 (point 4) ; `decision-N-060-v4.md`, l. 23 | « aucune sortie de l'oracle dans la sélection d'un agent ou d'un moniteur (N-053) » | compatible (plus large) ; la sélection d'un *moniteur* n'est pas couverte par le texte neuf, et N-060 la garde | erratum de la table : la branche « issue » est ouverte par GO-2026-11-22-70, décision 2 (c), non « si la décision 2 l'ouvre » |
| `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`, l. 59 | « L'aiguillage […] est une règle de sélection au sens de N-053, point 5 : il se déclare comme celles de E1.6 […] et n'entre jamais dans un signal d'entraînement de l'agent » | erratum de lecture (règle de la clause 3) ; **libellé à corriger** dans la table (« règle de sélection à déclarer comme celles de E1.6 » n'est pas dans le texte) | tient |
| idem, l. 248 (section 11, point 3) | « Corriger par l'entraînement de l'agent sur l'issue : non ouvert […] N-053 ne l'est que si un score de moniteur y entre. Recommandation : le laisser fermé ; s'il s'ouvre, un bras à part avec son nœud » | **libellé à corriger** (« reste fermé » n'y est pas) ; la définition large efface la distinction oracle et score qu'il pose | erratum : ouvert dans la seule branche « issue » du bras de remède (GO-2026-11-22-64 et -70) ; distinction rétablie par C-1 |
| `…-v3-erratum-3-v2.md`, l. 70-72 | réapprentissage des sondes sur l'oracle « non tranché » ; N-060 v3, point 4 s'applique en entier | tient (le texte neuf ne vise pas les moniteurs) | tient |
| `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, section 8, ligne 4 (l. 220), l. 228, l. 231, l. 254 | « Aucun retour à l'agent : aucune lecture ni aucun verdict ne revient à l'agent » ; règles de E1.6 = « bras déclarés » ; « ce que suit le soupçon ne produit aucune conséquence que l'agent observe » | **contredit** : la clause 3 admet hors bras des actions observables (aiguiller vers le modèle de confiance, relancer) ; elle appelle « règles » ce que N-076 appelle « bras » | tient (C-6 (e)) |
| idem, l. 110 ; `decision-N-065-v1.md`, l. 23-24 (point 4) | « aucun score d'un moniteur *du programme* dans l'entraînement ou la sélection de l'organisme » | élargit (tout dispositif) | tient (plus strict) ; dit en C-12 |
| `docs/decisions/decision-N-063-v2.md`, l. 6, 14 ; `registres/decisions.md`, l. 392 (P-015 (b)) ; synthèse du collisionneur de l'audit, C18 | critère 3 de G0 jugé aux seules doses où la base « mots et coût » échoue ; recherche de dose sur la boîte noire seule | **contredit** par la clause 2 (doses choisies ou régime défini par un score) ; collision déjà relevée par C18 contre la v1 | tient comme usage déclaré (C-5 (ii)) ; D-B |
| `registres/go.md`, l. 359 (GO-2026-11-17-02) ; `decision-N-062-v1.md`, l. 30 | organismes plus discrets conçus parce que la base les voyait ; famille neuve par cycle | **contredit** par le volet humain de la clause 2 | tient comme usage déclaré (C-5 (i)) ; D-B |
| `prereg/P-041-examen-final-v2.md`, l. 22, 35, 79 (scellé) | « sous-expérience de G1 » ; optimiseur d'entrées adverses ; base « instances seules » réentraînée à chaque époque sur les activations d'attaque ; « l'invariant N-053 est respecté » | **contredit** : l'optimiseur fait du substitut un agent dont les entrées sont choisies par un score (bras déclaré obligatoire) ; la condition 5 l'exclut de G1 ; la condition 1 interdit le réentraînement de la défense ; « fixe la lecture » rend le scellé non conforme | tient (C-8, C-10, C-12) ; nœud D-C ; le déclarer bras d'attaque par erratum de lecture |
| `prereg/P-041-malleabilite-v3.md`, l. 34, 74, 92 (scellé) | suffixe optimisé contre un moniteur de base figé, « qui n'est pas celui de l'arène » ; N-053 lu comme « exécutant isolé des moniteurs de l'arène » | même effet (agent par optimisation des entrées ; bras obligatoire) | tient (C-12 : écart à porter au directeur, non une invalidation) |
| `prereg/organismes-discrets-va-v1.md`, l. 17, 248-251 ; `prereg/T0.7-organismes-discrets-v-a-v1.md`, l. 21, 256-258 (scellés) | « aucune sortie de l'oracle de couverture dans la sélection » ; « Tout score de moniteur trouvé dans un signal de construction ou de sélection » ; garde : aucun champ de score de lecteur dans la sélection, l'acceptation ni la distillation | compatible ; leur garde ne teste pas l'artefact indirect | tient ; le repli de deuxième ligne (« sélection adverse parmi K tirages honnêtes ») relèvera de la clause 2 ou d'un bras, à son avenant |
| `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, l. 47, 394 ; `…/juge-selection/criteres-choix-cartes-v9-v7.md`, l. 59 (scellés) | le verdict d'un juge « ne promeut, n'écarte, ne trie […] aucune carte » (N-058 ; N-053, point 5) | rétrécit par « fixe la lecture » (les cartes ne sont pas des agents) | tient (C-12 : la lecture plus large prime) |
| `prereg/organisme-crible-v-regles-proposeurs-v1.md`, l. 240, 387, 693 (scellé) | dépendance « indirecte » de la règle aux verdicts, visée par N-058 et N-053 | tient (« dérivé » et « ensemble filtré » la couvrent) | tient |
| `prereg/P-041-examen-final-v2.md`, l. 122 ; `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1.md`, l. 321 ; `prereg/barreau5-…-v1.md`, l. 351 | gardes et arrêts : aucun score de sonde dans l'entraînement, le choix, l'arrêt ou l'exclusion | tient | tient |
| `docs/decisions/decision-N-077-…-v1.md`, l. 50, 69 | « les deux règles de sélection de N-053, point 5, restent » | tient | tient |
| `docs/decisions/proposition-P-066-…-v1.md`, l. 46 ; `proposition-P-041-…-v3.md`, l. 44, 67 | aucun score de la base « mots et coût » pour choisir les épisodes ; générateur au niveau des lois | tient | tient |
| `registres/go.md`, l. 624 (GO-2026-11-21-25, D-4 (a)) | « contrôle actif par sélection sur un score de sonde consigné comme fermé (N-053, point 5) » | la table lit « fermé tant qu'aucune règle n'est déclarée et accordée » : c'est un changement de lecture d'un accord | erratum, à confirmer par le directeur ; **libellé à corriger** : citer GO-2026-11-21-25 (il y a quatre « D-4 » le 21 novembre) |
| `registres/go.md`, l. 634 (GO-2026-11-21-35, D-4 (a)) | « aucun score du suspect dans l'étalonnage d'un seuil » | hors du texte neuf (étalonnage des moniteurs) | tient ; à citer à côté |
| `registres/go.md`, l. 707 (GO-2026-11-22-20, recommandations de la réponse 7) | « sens (a) et (b) seulement, N-053 strict » | l'ajout de la table (« le sens (c) n'est ouvert que dans le bras de remède déclaré ») change l'accord | erratum couvert par GO-2026-11-22-70, décision 2 (c), si le directeur le lit ainsi |
| `registres/go.md`, l. 739 puis l. 744 (GO-2026-11-22-52 et -57) | barreau 3 « refusé pour l'instant », puis « go (exception à l'invariant N-053 accordée en bras d'attaque déclaré, organisme en quarantaine, jamais réemployé) » | la ligne de la table est juste | tient |
| `docs/notes/audit-controle-v1/audit-litterature-v1.md`, l. 78 (D5) | « Les scores des moniteurs ne deviennent jamais un signal d'entraînement de l'agent » | la ligne de la table (« score de sonde » → « score de moniteur ») ne trouve pas « score de sonde » à la l. 78 : vise sans doute la synthèse du collisionneur, C10 (« La garde de R-508 D5 n'est testée que sur un score de sonde ») | **libellé à corriger** : citer `synthese-collisionneur-v1.md`, l. 140 |
| « Fiche de l'étau (mémo) » | « refusé pour l'instant » (relevé par `remarque-invariant-N053-reponse-fable-bibliothecaire-v1.md`, l. 123 : « le mémo retarde sur le registre ») | le mémo lui-même non localisé par moi ; GO-2026-11-22-57 accorde bien le barreau 3 | erratum juste sur le fond ; chemin du mémo à donner par la mère |

## 6. Points qui reviennent au directeur

**D-A. Ce qui est un moniteur : distinguer vérité plantée, lecteurs de l'issue et moniteurs.** Enjeu : c'est le nœud que l'auteur laisse en question (« les deux oracles ne sont pas encore distingués »). Mais sa définition le tranche déjà dans le sens le plus large, et elle rend illicites N-058, N-045 v2 et N-053 v1, point 2.
- (a) Trois objets (C-1). La vérité plantée est hors du score ; les lecteurs de l'issue sont dedans, avec l'exception de la strate tirée au hasard. Avantage : N-058, N-045 v2 et N-060 v3 tiennent, et la branche « issue » est bien nommée comme écart. Inconvénient : la récompense sur le résultat du sabotage (N-053 v1, point 2 (b)) doit venir d'une vérité plantée, par exemple la banque à tâches exécutables (N-060 v3, point 5), ou d'un bras déclaré. C'est ce que recommandait déjà le collisionneur de l'audit (C10).
- (b) Tout dedans, lettre de l'auteur. Avantage : aucune voie de contournement. Inconvénient : il faut amender N-058, N-045 v2 et N-053 v1, point 2, soit trois décisions.
- (c) Seuls les moniteurs du programme (lecture de N-065, point 4, et de N-076, l. 110). Avantage : P-041 reste hors du texte. Inconvénient : la voie de la distillation filtrée par un juge tiers reste ouverte.
- Recommandation : (a). Confiance 0,7.

**D-B. Le volet humain de la clause 2, et deux usages déclarés.** Enjeu : à la lettre, la v2 interdit des pratiques accordées. Ce sont la recherche de dose sur la boîte noire (P-015 (b)), le critère 3 de G0 jugé aux seules doses où la base échoue (N-063 v2), les organismes plus discrets (GO-2026-11-17-02) et la famille neuve par cycle (N-062).
- (a) Les écrire comme usages déclarés, sous conditions (C-5 (i) et (ii)). Avantage : la lettre rejoint la pratique, et chaque usage se dit dans la revendication. Inconvénient : une boucle lente contre les moniteurs reste possible, à la granularité des portes.
- (b) Tout faire refaire à l'aveugle ou en bras déclaré, comme le proposait le collisionneur de l'audit (C18). Avantage : propre. Inconvénient : il faut reprendre T0.6 et la lecture de G0.
- Recommandation : (a). Confiance 0,6.

**D-C. Une épreuve d'attaque dans une porte, et le succès d'un attaquant.** Enjeu : l'examen final de P-041, scellé, est une sous-expérience de G1 bâtie sur une attaque adaptative. La condition 5 telle quelle l'exclut de G1 et ne laisse le succès d'un attaquant restreindre aucune revendication (règle R4). Toucher une revendication est un nœud.
- (a) C-10 : épreuve d'attaque scellée admise dans une porte, à charge seulement ; le succès d'un attaquant restreint la revendication. Avantage : symétrie. Inconvénient : G1 peut échouer par l'attaque.
- (b) Lettre de l'auteur, et l'examen final de P-041 sorti de G1 par erratum. Avantage : G1 plus simple. Inconvénient : on change un préenregistrement scellé.
- Recommandation : (a). Confiance 0,7.

**D-D. Le ré-échantillonnage uniforme de E1.6.**
- (a) Garder la lettre de N-053 v1, sans bras exigé (C-6).
- (b) Étendre l'exigence (b) au ré-échantillonnage déclenché par un score, au préenregistrement de E1.6.
- Recommandation : (a) dans ce texte, (b) à instruire au préenregistrement de E1.6. Confiance 0,55.

**D-E. L'agent qui écrit des poids ou entraîne un successeur.** La question est signalée par les réponses 29 et 35 (« N-053, quand l'agent est celui qui entraîne »). Le texte de l'auteur n'en dit rien. C-2 et C-4 l'incluent (« tout modèle qu'un agent entraîne » ; « par quiconque conduise l'entraînement, l'agent compris »). Le périmètre du programme quant à l'écriture des poids reste la D-2 de la réponse 35. À confirmer.

**D-F. La note de bras comme pièce décisive** (C-7 : scellée et contre-lue), et le registre des bras ouverts. C'est une procédure ; la recommandation est oui. Confiance 0,8.

## 7. Ce que je n'ai pas fait

- Je n'ai pas lu en entier les 949 fichiers qui citent l'invariant. Les brouillons, les notes du collisionneur et de l'organisme, et les envois n'ont été lus que là où la table de l'auteur les appelait. D'autres renvois peuvent buter.
- Je n'ai localisé ni la « fiche de l'étau (mémo) » ni le texte exact de N-054, point 5.
- Je n'ai pas vérifié dans le code si l'acceptation des trajectoires de distillation de T0.6 ou du barreau 5 emploie un contrôle qui serait un moniteur sous la définition large.
- Je n'ai pas exécuté la garde existante ni ses tests.
- Je n'ai pas vérifié sur PDF les antériorités citées par l'auteur (ce n'était pas l'objet).
