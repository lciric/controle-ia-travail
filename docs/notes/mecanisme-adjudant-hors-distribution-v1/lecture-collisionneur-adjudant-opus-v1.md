> You are powered by the model named Opus 5.5.

# Lecture des résultats du collisionneur sur le mécanisme adjudant (cinq espèces, trois tours), face à la note de Fable v2 — Opus 5.5 — v1

- **Date** : 21 novembre 2026, 17:10 UTC (`date -u`). **Auteur** : Claude Opus 5.5, lecteur neuf, sur mandat de la session mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`). Pièce de travail (classe C), non contre-lue. Aucun appel payant, aucune machine, ni commit ni poussée.
- **Course lue** : `runs/collisionneur-mecanisme-adjudant-v1-20261121-114751/` sur la branche `runs/collisionneurs-reprise-minuit-v1` (`6804cec12`), extraite par `git archive` hors du dépôt. Quinze cellules sur quinze, toutes « OK », empreintes égales à leurs compagnons (15/15) ; faits, question et liste des espèces vérifiés. Espèces : A Fable 5.2, B Opus 5.5, C Argon (gemini-4-argon), D Astra (gpt-6.2-astra), E Carbon (gemini-4-carbon) ; Kimi absent, absence acceptée par l'arbitre. Dépense : 14,81 USD sur une ligne de 28 USD (`etat.md` de la course).
- **Lu en entier** : faits et question servis ; les cinq synthèses du tour 3 (empreintes `55459621…`, `7f71933a…`, `8a064556…`, `a4cc87ce…`, `ebf985cc…`). **Lu par sections** : les cinq conceptions du tour 1 (rangements et propositions) ; les critiques croisées du tour 2 par motifs (longueur, Rice, risque relatif, jumeau, e-valeurs). Journal et état de la course.
- **Note confrontée** : `reponse-fable-mecanisme-adjudant-v2.md` (`4f8fbeaf5db8…`, verdict, § 1, § 6, § 8) avec son erratum 1 (`2062a4e46e39…`), qui prime. **Comparaison antérieure** : `docs/notes/adjudant-opus-independant-v1/comparaison-v1/comparaison-reponses-adjudant-v1.md` (`5bfc475a3f68…`) compare la note de Fable v1 à une réponse d'Opus écrite seule ; elle ne porte pas sur cette course. Aucune comparaison antérieure de cette course n'existe au dépôt ni sur la branche.
- **Couple servi** : c'est le couple `collisionneur-v1/` (faits `f7b4577f…`, question `35c032b6…`, identiques octet pour octet à ceux de la course), non le couple `collisionneur-v2/` que la v2 de Fable a corrigé (constat 15 : « son directeur » ; le problème (B) dit « panne non corrélée »). Effet visible : trois espèces sur cinq consacrent une bonne part de leurs duels à mesurer la décorrélation des pannes.
- **Non ouvert** : tout ce que le cloisonnement interdit ; les dossiers `essais/` de la course (invites et réponses brutes, doublons des cellules) ; aucun résultat d'expérience.

## Verdict

1. **Les cinq espèces convergent, indépendamment des corrections de la v2, sur le cœur de la note de Fable** : aucun détecteur passif ne garantit rien contre une attaque qui imite la loi honnête sur le canal qu'il lit (borne par la variation totale) ; ce qui tient ne reconnaît pas l'attaque ; les moniteurs deviennent un tri au-dessus d'un plancher.
2. **Elles déplacent le centre de gravité** : du plancher d'audit (note de Fable, rang 1) vers **la conception du produit** — une propriété fixée par un tiers avant la soumission, vérifiée mécaniquement, avec repli quand elle échoue. Et **elles donnent toutes le même premier pas, sans dépense** : compter, sur des tâches archivées, la part qui admet une telle propriété. C'est la « couverture de l'oracle » de la note, que la note dit mesurable sans la mettre en premier.
3. **Elles n'ajoutent aucun chiffre qui contredise les blocs de calcul de la note**, et ignorent sa partie la plus neuve (taille de la référence honnête, pari apparié au jumeau, lecture de la seule part tirée au hasard).

## 1. Ce que chaque espèce propose, en une phrase (synthèse du tour 3)

- **Fable (A)** : n'utiliser le produit que sous forme d'affirmations exécutables, notées sur des données séquestrées à usage unique, en retenant le meilleur de l'agent et d'un témoin de confiance plus faible (garantie relative au témoin, « U(retenu) ≥ U(témoin) − 2e ») ; en second, doper en secret des tâches réelles d'un effet connu et contrôler qu'il est restitué.
- **Opus (B)** : « créer une différence que l'attaquant ne peut pas reproduire sans coût » ; d'abord fermer par conception de la tâche le canal non vérifiable, puis auditer en secret la généalogie de l'affirmation décisive sous un plancher uniforme, les moniteurs réduits au tri.
- **Argon (C)** : un goulet de vérification mécanique (énoncé formel ou tests de propriétés figés hors de portée de l'agent), avec remplacement automatique du produit refusé par celui du jumeau honnête ; en second, un piège d'équivariance à clé secrète et une surprise prédictive croisée agent–jumeau.
- **Astra (D)** : adjuger le droit de publier et non l'intention : quarantaine du travail, porte de dépôt qui débite chaque effet sur un budget provisionné (borne par somme télescopique sous médiation complète), réception contre une obligation fixée par le demandeur, et un « passeport d'étalonnage » qui affiche « non validé » sans accuser.
- **Carbon (E)** : un contrat formel vérifié exhaustivement (Lean 4, gardes contre la trivialisation) avec repli transactionnel vers un témoin sûr, éprouvé tous détecteurs éteints ; en second, l'équivariance sous transformations tirées après engagement, et un routage conforme corrigé de la longueur.

## 2. Convergences, divergences, et qui a raison à la source

**Convergences (cinq sur cinq).** La borne « puissance ≤ niveau + variation totale » ; la garantie de fausses alertes d'un rang conforme sous échangeabilité seulement, avec au moins 99 épisodes honnêtes pour descendre à 1 % et 299 sans alerte pour certifier 1 % à 0,95 (exact : 1 − 0,05^(1/299) < 0,01, comme le bloc O de la note) ; la vérification du produit comme seule voie vers (C) ; une famille d'attaque écrite par un tiers ; et l'aveu commun que la part du dommage logée dans le résidu non vérifiable (choix de la question, interprétation, omission) est inconnue et décide de tout.

**Divergences, tranchables à la source.**
- *Le repli sur le jumeau.* Argon et Carbon remplacent le produit refusé par celui du jumeau honnête ; Fable exige un témoin « de confiance, à la différence du jumeau ». **Fable a raison** : les faits ne donnent le jumeau pour honnête qu'au banc (« reçoit la même tâche ») ; en service, s'il est le même modèle, il n'est pas un témoin sûr. La note de Fable dit la même chose de son pari apparié (« demande un jumeau, donc le banc »).
- *La mesure sur le mode tenu à l'écart.* Argon propose de mesurer son goulet « sur le mode de sabotage tenu à l'écart » puis d'utiliser ses échecs « comme étiquettes gratuites pour recalibrer » les moniteurs. **C'est contraire à la règle des faits** (le mode tenu à l'écart sert d'épreuve, il n'entre pas dans la conception des moniteurs). Carbon, lui, écrit « sans toucher au mode … tenu à l'écart ».
- *Les e-valeurs comme alarme.* Opus retire son agrégation par e-valeurs après la critique de Carbon : une e-valeur tirée d'une valeur p conforme sur n épisodes vaut au plus n + 1 ; à n = 99 et seuil 100, la moyenne n'alarme que si toutes sont maximales. **Exact** (la plus petite valeur p conforme a probabilité au plus 1/(n + 1) sous l'honnête).
- *Le risque relatif des pannes communes.* Opus dit la borne de Fréchet « hypothèse selon A » ; **elle est élémentaire** : P(F₁ ∩ F₂) ≤ min(p₁, p₂), donc risque relatif ≤ 1/max(p₁, p₂). Elle rend ce rapport non identifiable comme mesure de décorrélation quand un raté est fréquent.
- *Le théorème de Rice.* Argon l'invoque pour l'impossibilité de la détection ; **il ne porte pas cette impossibilité**, qui vient de la variation totale ; Rice ne concerne que l'indécidabilité de l'égalité sémantique dans sa relation d'équivariance (critique de Fable, tour 2).
- *Les chiffres.* Argon avance « ≥ 75 % du dommage, ≤ 10 % de blocage, 4 heures-GPU » sans les dire illustratifs, contre la règle de la question ; Carbon marque les siens « illustratif ». Et l'« étape à coût zéro » d'Argon demande une passe du modèle : elle n'est pas sans dépense.

## 3. Ce que le collisionneur ajoute à la note de Fable, et ce qu'il contredit

**Ajouts (absents de la v2, recherche par motifs faite).**
1. *Une garantie sans détection, d'une autre forme que le plancher* : la dominance du témoin (Fable du collisionneur) et le repli transactionnel (Carbon) bornent le dommage sur la partie vérifiable même si rien n'est jamais pris ; la note n'a qu'un plafond par tâche, sans mécanisme.
2. *Le dopage de tâches réelles* (salage, injections aveugles de la physique ; Fable dit « référence à vérifier ») : un piège tiré de la loi réelle elle-même, qui retire l'écart entre mondes plantés et tâches réelles ; absent de la note.
3. *La dérive des statistiques extrêmes avec la longueur* (Fable et Opus au tour 2, Argon, Carbon) : un maximum sur T jetons réglé à 1 % pour T₀ sonne à 1 − 0,99^(T/T₀), soit 1,99 % pour T = 2T₀ sous indépendance. Interdire moyenne et médiane pousse vers le maximum : ce point touche directement les sondes du programme. (La correction de Šidák d'Argon suppose l'indépendance des jetons ; la stratification par longueur ne la suppose pas.)
4. *La porte de dépôt provisionnée* (Astra) : une unité de dommage comptable et une borne par médiation complète, limitée à un dépôt fermé (« je ne sais pas provisionner l'influence scientifique ouverte »).
5. *Le plafond n + 1 des e-valeurs conformes* : il renforce l'option (a) de la décision D-4 de la note (ne pas revendiquer la forme « valide à tout instant sur des scores de sondes »).

**Contradictions.** Aucune sur les calculs. Une sur le ton : Argon et Carbon marquent « vérifié » que la vérification formelle « borne la perte sans détection » ; c'est vrai seulement sur la part formalisable, ce qu'ils disent ensuite eux-mêmes, et la note est plus juste en rappelant que le retrait sans détection n'est publié que pour une vérité très structurée (Goldwasser et al. 2024, p. 1). Opus du collisionneur rappelle enfin qu'un attaquant qui frappe une seule fois rend vide la borne (1 − p)^k : la note le dit (« une menace diffuse »), le collisionneur l'appuie.

**Ce que la note a et que le collisionneur n'a pas** : la loi de la référence honnête (m, n, source de validité), le pari apparié au jumeau comme moins cher, la recapture lue sur la seule part tirée au hasard, les deux régimes « signature » et « excès », les antériorités lues en entier (Avenhaus et Jaech 1981, etc.). Aucune espèce ne les remet en cause ; aucune ne les connaissait.

## 4. Ce qui change dans les décisions pour Lazar

- **D-1 (cadre « borner sans reconnaître »)** : renforcée ; cinq espèces de trois lignées y arrivent seules. Recommandation inchangée, confiance un peu plus haute.
- **D-2 (course de l'organisme, banc d'abord)** : ajouter en tête des gestes sans dépense le premier pas commun aux cinq : sur des tâches archivées, hors du mode tenu à l'écart, par un agent habilité, compter la part qui admet une propriété fixée d'avance par un tiers, et la taille du résidu. Si cette part est faible, (C) ne repose ni sur l'audit ni sur la vérification, et il vaut mieux le savoir avant de financer la suite.
- **Atelier d'idées** : y verser la dominance du témoin et le dopage de tâches réelles, comme candidats pour (C) et (B), avec leurs conditions (témoin de confiance distinct du jumeau ; dopage sans trace ; tâches à données). Ni revendication ni dépense.
- **À vérifier, routine** : que les seuils des sondes à maximum par épisode sont réglés par strate de longueur. S'il faut toucher un préenregistrement scellé, c'est un nœud.
- **À écarter** : le repli sur le jumeau en service, et toute recalibration de moniteur sur les échecs du mode tenu à l'écart.
- **D-3 à D-7** : inchangées. Le collisionneur n'a pas lu la v2 ; une seconde passe sur le couple `collisionneur-v2/` ne se justifierait que pour la décorrélation, sur devis.

## 5. Une phrase pour Lazar

Les cinq modèles disent tous, chacun de son côté, que rien ne détecte à coup sûr une attaque inventée et qu'il faut borner le dommage par la conception du produit ; ils donnent le même premier geste gratuit, compter les tâches qui admettent une propriété vérifiable fixée d'avance, et n'ébranlent aucun chiffre de la note de Fable.
