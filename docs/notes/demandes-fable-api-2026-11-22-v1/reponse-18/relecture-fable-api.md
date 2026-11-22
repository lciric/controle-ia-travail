# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHaAyoZJutgsa7oZpXK6`
- Heure (UTC) : 2026-11-22T07:32:07Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-18-questions-brulantes-concurrents-v1.md` — sha256 4178a50267ac05c7a80131a9400323c9d151a2cff9aa5216bb977686c9d5f37c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/recherche-exhaustive-transposition-v2.md` — sha256 2395ea20a570afd7b206bec4adec56664604a500902c68cf68eed87358ae9b8d (compagnon : vérifié)
  - remarques : `docs/notes/veille-organismes-ideation-v3/synthese-v1.md` — sha256 2bc3af77fba61d4c66ad8286ba8930a5fc170512a9e4ea5cf5e1b836d77a230e (compagnon : vérifié)
  - remarques : `docs/notes/lectures-approfondies-v1/2507.12691-lecture-v1.md` — sha256 02e5257f04f256214f4dec96726f8c243b9d5849936f5fc9789122cf28b495e0 (compagnon : vérifié)
  - remarques : `docs/notes/lectures-approfondies-v1/2602.15029-lecture-v1.md` — sha256 496f84d762f38f9fda79f1f035db50724aee1a1d5ccf06d6e5de046221aa2a97 (compagnon : vérifié)
  - remarques : `docs/notes/lectures-approfondies-v1/2602.22600-lecture-v1.md` — sha256 67d500dbe5f41579a78dc89566ef4f25a3dfc48719834adc12b77a074cb04ae5 (compagnon : vérifié)
  - remarques : `docs/notes/lectures-approfondies-v1/2607.20058-lecture-v1.md` — sha256 131bb2c6f6fed54a58fcbe499a00535b2bc4d2c984f54b2392ba06fc08dce079 (compagnon : vérifié)
  - remarques : `docs/notes/lectures-approfondies-v1/2611.08977-lecture-v1.md` — sha256 c790c38fe189828b513960d885f8bc52ae1333f70e5834e9c59642f9636b0d1e (compagnon : vérifié)
  - remarques : `docs/notes/lectures-approfondies-v1/2611.14487-lecture-v1.md` — sha256 3c9a6e0d292653cfc897482fe61b6fa74991bb74768abd5ce9ec0169c9a58e2c (compagnon : vérifié)
  - remarques : `docs/notes/lectures-approfondies-v1/2611.21950-lecture-v1.md` — sha256 7802c8738ea84e12c4c3ee69763de6c061f8eb9c21247adc06143399199c053d (compagnon : vérifié)
- Empreinte de l'invite envoyée : 9812d2961a16108ddb17ba96db6c45cc600450a6559072bfe1f47f0bf707fb82
- Jetons : entrée 43506, sortie 20454 (dont réflexion 11600), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.166208 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 18 : questions brûlantes des concurrents, réponse approfondie

**Conclusion d'abord.** Les pièces documentent bien les manques que les auteurs déclarent, mais presque pas leurs prochaines étapes : je n'en relève que trois. Cette moitié de la question reste donc sans réponse, et je ne la comble pas par inférence. Sur les manques, les quatre voisins les plus proches du papier A butent, chacun à sa façon, sur la référence honnête [HYPOTHÈSE]. L'effort doit donc aller au harnais honnête apparié (plusieurs moniteurs, pas à pas, même distribution), puis à la complémentarité sous sabotage diffus, et non à la théorie. Confiance d'ensemble : 0,5.

**Réserves.**
- Je n'ai lu aucun PDF. Les « citations » sont les formulations françaises des notes de lecture, non le verbatim des auteurs.
- Les pièces ont été réunies pour une recherche d'antériorité sur trois objets et pour des lectures de méthode, non pour recenser les concurrents.
- Les notes sont écrites par des lecteurs du programme, avec une rubrique « ce qui sert au programme ». Toute convergence que j'y lis peut refléter la thèse.
- Je n'ai pas recalculé les empreintes. Je ne nomme que des auteurs de travaux cités.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Définir « concurrent » par revendication, non par sujet** [PROPOSITION]. Pour chacun des axes retenus (bilan mesuré, complémentarité, co-élévation entre copies, juges sous attaque), il chercherait qui peut écrire la même phrase de résumé. Plusieurs pièces jointes (Karkada, Schiffman, Buehler, Chen) sont des sources de méthode, non des concurrents.
- **Séparer trois sortes d'énoncés** [PROPOSITION] : la limite avouée (ce que le papier n'a pas fait), l'étape annoncée (ce que l'équipe fera), la question ouverte du champ. Seule la deuxième prédit un mouvement. Les notes consignent surtout la première.
- **Vérifier que chaque manque déclaré est encore ouvert** [PROPOSITION], par les citations descendantes et les versions ultérieures. La limite d'un papier n'est pas un trou du champ.
- **Estimer la course** [PROPOSITION] : pour chaque manque, ce qu'il coûterait à l'équipe d'origine de le fermer avec ses propres données, comparé au coût pour le programme.
- **Poser la question inverse** [PROPOSITION] : que déclarent les concurrents qui menace la thèse ?
- **Se méfier des sections de limites** [HYPOTHÈSE]. Les auteurs déclarent les manques qui les arrangent. Antériorité de mémoire : Ioannidis, 2007, « Limitations are not properly acknowledged in the scientific literature » (rapporté, non vérifié sur PDF).

## 2. Données brutes de départ

- Les sections « limites », « discussion » et « travaux futurs » des PDF déjà au dépôt, en verbatim, avec la page.
- L'historique des versions. Les pièces rapportent une version 5 pour Rose et collaborateurs, une version 3 pour Parrack et collaborateurs, une version 2 pour Zhang et Gao, Makins et Tailor [FAIT RAPPORTÉ]. Ce qui change d'une version à l'autre dit où l'équipe travaille.
- Les dépôts de code, les pages de relecture ouverte (les demandes des relecteurs sont des étapes imposées) et les prépublications ultérieures des mêmes auteurs.
- Les quatre arbres de citations non parcourus (Ker 2006 et 2007, Arias-Castro 2012, Avenhaus) et les huit articles lus au seul résumé [FAIT RAPPORTÉ, recherche exhaustive, § 1].
- L'inventaire des actifs du programme (harnais, exécutions jumelles, organismes), pour chiffrer son délai.

## 3. Méthodes et outils

- **Grille d'extraction** : énoncé verbatim, page, type, revendication du programme touchée, « fermé depuis ? », qui peut fermer le plus vite.
- **Double codage** par deux lecteurs dont l'un ignore la thèse, avec l'accord mesuré par le coefficient kappa (Cohen, 1960, « A coefficient of agreement for nominal scales » ; rapporté, non vérifié sur PDF).
- **Recherche descendante** par manque déclaré, sur Semantic Scholar et OpenAlex, quotas rétablis.
- **Comparaison des versions** d'un même article.
- **Prévisions scellées sur les concurrents** : pour chaque voisin proche, ce qu'il publiera sous six mois, avec une probabilité.
- **Table de priorité** : valeur si le programme arrive premier, chance que le manque soit encore ouvert, avance propre du programme, coût.

## 4. Ce qui vérifie hors du directeur et de Claude

- Les auteurs eux-mêmes, interrogés sur leurs suites.
- Le temps : les prévisions scellées se confrontent aux listes d'arXiv à trois et six mois.
- Le second lecteur aveugle à la thèse, pour le verbatim.
- Les citations descendantes, publiques.
- Le collisionneur sur la question neutre, après le test de devinette.
- L'essai « jumeau contre jumeau », dont l'issue ne dépend d'aucun avis.

---

## Demande reformulée

« À partir des PDF au dépôt, extrais pour chaque travail concurrent, en verbatim et à la page, trois listes séparées : les limites qu'il avoue, les étapes qu'il annonce, les questions qu'il dit ouvertes. Classe les concurrents par revendication du programme touchée (bilan mesuré, complémentarité, co-élévation, juges sous attaque) et écarte les simples sources de méthode. Pour chaque manque déclaré, dis s'il a été fermé depuis (versions ultérieures, citations descendantes) et ce qu'il coûterait à son auteur de le fermer. Sépare ce que les auteurs déclarent, ce que nos lecteurs relèvent, et ce que tu infères. Relève aussi ce que ces travaux déclarent qui menace la thèse. Classe ensuite les lieux où accélérer par : manque encore ouvert, avance propre du programme, issue publiable dans les deux sens. Scelle des prévisions sur les prochaines publications des concurrents. Dis ce que les pièces ne permettent pas de trancher. »

---

## Réponse

### A. Ce que les auteurs déclarent

Tout ce tableau est [FAIT RAPPORTÉ] par les notes. La dernière colonne est mon inférence, [HYPOTHÈSE].

| Travail | Déclaré (formulation de la note, page) | Pièce | Type | Ce que j'en infère |
|---|---|---|---|---|
| Khilar, 2610.13083 | Une rampe lente empoisonne l'étalonnage de tous les détecteurs (p. 1, 9-10) ; il faut « protéger la référence » (p. 10) | Recherche exhaustive, § 3 | Limite et étape | Flanc ouvert : la référence estimée. L'auteur a les données réelles pour le fermer |
| Wen et collaborateurs, 2411.17693 | Tâches corrélées laissées ouvertes (p. 10) ; une référence rendue plus suspecte accroît le « budget » (p. 18) | § 2 et 3 | Question ouverte | Dépendance et référence manipulée, non chiffrées |
| Zhang et Gao, 2606.10456 | Sur de vraies traces, l'attaque est fabriquée sur les scores, non jouée par l'agent (p. 8, « réserve ») | § 4 | Limite, statut à confirmer | Attaque jouée par un agent réel |
| Ghanem, 2608.02698 | « Résultats provisoires » (page non donnée pour ce mot) | § 2 | Statut | Une suite est probable |
| Parrack, Attubato, Heimersheim, 2507.12691 | Moniteurs plus forts que l'agent ; sondes non localisées ; témoin trop facile ; contre-stratégie faible (p. 8-9, 15-17). La moyenne des scores seule bat le moniteur qui lit les scores (p. 9) | Lecture approfondie | Limites | Le témoin honnête de même distribution manque |
| Schiffman, 2602.22600 | Hypothèse posée à la main ; interventions peut-être hors distribution ; accès aux poids requis ; audit de garde-fous par retrait de direction nommé (p. 10, 16, 30) | Lecture approfondie | Limites et application nommée | Source de méthode, non concurrent |
| Buehler, 2607.20058 | Surtout un modèle ; réponses binaires contraintes ; interprète unique ; 0 sur 523 mots libres ; risque si une lecture devient récompense (p. 30-31) | Lecture approfondie | Limites | Appuie N-053 |
| Karkada et collaborateurs, 2602.15029 | Théorie pour les plongements de mots ; adaptation au contexte non expliquée (p. 9) | Lecture approfondie | Limites | Source de méthode |
| Queen et collaborateurs, 2611.21950 | Pas d'ablation ; peu de scientifiques ; bras confondus avec le modèle d'exécution (p. 23, 32) | Lecture approfondie | Limites | Papier C : apport de l'audit non isolé |
| Society of AI Scientists | Observationnel (p. 6) | Veille, § 2 | Limite | Aucun tirage au hasard |
| Lorup, 2611.24711 | Un raccourci non écrit reste possible (p. 24) | Veille | Limite | Audit du générateur incomplet |
| Yuan et collaborateurs, 2611.24302 | Dix courses par bras ne départagent pas les composantes (p. 11) | Veille | Limite | Puissance insuffisante |
| Gao et collaborateurs, 2611.14487 | Un domaine ; juges et arbres par modèles ; contamination possible (p. 9-10) | Lecture approfondie | Limites | Organisme d'idéation |
| Gusev, 2611.26286 | Découpage comptable, non causal (p. 3) | Veille | Limite | Papier C |

**Étapes annoncées.** Je n'en trouve que trois [FAIT RAPPORTÉ] : « protéger la référence » (Khilar, p. 10) ; l'audit de garde-fous par retrait de direction (Schiffman, p. 30) ; les tâches corrélées laissées ouvertes (Wen, p. 10), qui est une question plus qu'un plan. Les notes n'ont pas de rubrique « travaux futurs ». Ce silence vient des notes, non des auteurs.

### B. Ce que nos lecteurs relèvent et que les auteurs ne déclarent pas

Ces points sont [FAIT RAPPORTÉ] comme observations des notes. Ils ne sont pas des manques déclarés.

- Makins et collaborateurs, 2607.07368 : la somme n'est pas testée, seul le maximum baisse (p. 1) ; la dépendance positive du soupçon entre commits est traitée comme une nuisance (p. 45).
- Rose et collaborateurs, 2604.01151 : statistiques de groupe sur activations, sans théorème.
- Tailor, 2510.04303 : rien sur une accumulation de scores.
- Parrack et collaborateurs : aucune analyse des cas manqués par la boîte noire, ni des erreurs corrélées.
- Queen et collaborateurs : difficulté des corruptions notée après coup (p. 34) ; deux systèmes ont atteint les données de test (p. 8, 10).
- La note sur Zhang et Gao dit « réserve » sans préciser qui la formule. C'est à trancher sur la page 8.

### C. Ce qu'ils déclarent et qui menace la thèse

Faits rapportés d'abord, lecture ensuite.

- Les bases lexicales égalent ou battent les lectures internes en classement absolu (Buehler, p. 8 et 11) [FAIT RAPPORTÉ].
- Une sonde linéaire peut décoder une coordonnée depuis les seules statistiques de cooccurrence (Karkada, p. 6, 8-9) [FAIT RAPPORTÉ].
- Un moniteur lit mal des scores de sondes hors de leur distribution d'étalonnage ; aux portes dérobées, le gain est négatif (Parrack, p. 8-9) [FAIT RAPPORTÉ].
- Deux sous-espaces au hasard donnent des corrélations canoniques élevées (Schiffman, p. 18) [FAIT RAPPORTÉ].
- Un sélecteur par notes choisit le meilleur de deux environ une fois sur deux (Zeng et collaborateurs, p. 8) [FAIT RAPPORTÉ, chiffre non opposable sans vérification].
- Lecture [HYPOTHÈSE] : la complémentarité, second axe de la thèse, est la part la plus exposée. Sans base « mots seuls », sans contrôle à vocabulaire apparié et sans nul de même rang, un gain de sonde ne prouve rien.

### D. Les questions brûlantes, inférées

Tout ce qui suit est [HYPOTHÈSE].

1. **La référence honnête.** Quatre voisins s'y arrêtent : elle s'empoisonne (Khilar), elle est trop facile (Parrack), elle se manipule (Wen, p. 18), ses pas sont dépendants (Wen, p. 10 ; Makins, p. 45). Aucun n'en donne une loi avec la taille m. Cette convergence peut être un artefact de lecteurs acquis à la thèse ; le double codage aveugle la teste.
2. **L'attaque jouée.** La dissimulation dans les marginales est énoncée, mais fabriquée sur les scores (Zhang et Gao, p. 8). La question brûlante de ce côté est : un agent réel y parvient-il ?
3. **Ce que la sonde ajoute à la boîte noire.** Parrack mesure un moniteur qui lit des sondes, non ce que les sondes rattrapent. La question ouverte de la note (rattrapage à faux positifs fixés sur du travail honnête de même distribution) est une déduction du lecteur, non une déclaration des auteurs.
4. **L'audit qui exécute contre l'audit qui lit** (Queen ; Society, p. 19-20). Côté papier C, l'apport de chaque composant n'est isolé nulle part dans les pièces.

Une précision sur Zhang et Gao. La réponse 9 jugeait inexact, pour la somme et le maximum, l'énoncé « puissance égale au taux de fausses alarmes ». Leur proposition 1 est rapportée sous la même forme. Si leur classe d'attaque est une permutation des scores honnêtes, l'énoncé est exact pour toute statistique invariante par permutation. Si c'est une copule quelconque, la critique vaut [HYPOTHÈSE, à lire page 3]. Le programme ne peut pas écrire que leur proposition est fausse avant cette lecture.

### E. Où accélérer

[PROPOSITION ; les chances sont des jugements]

| Lieu | Manques déclarés qu'il rejoint | Avance propre du programme | Risque d'être devancé | Rang |
|---|---|---|---|---|
| Harnais honnête apparié : essai « jumeau contre jumeau », plusieurs moniteurs pas à pas, grille référence et horizon | Khilar (référence), Parrack (témoin), Wen (corrélation) | Jumeaux honnêtes sur modèles ouverts ; décisions N-075 et N-076 prêtes | Moyen : Khilar a des données réelles, hors agents | 1 |
| Complémentarité sous sabotage diffus, table appariée, contrôle « seconde boîte noire », base « mots seuls » | Parrack (témoin, contre-stratégie) | Organismes de sabotage diffus ; leurs jeux sont des tromperies instruites | Élevé : une réanalyse de leurs données suffit sur leurs propres jeux | 2, mêmes exécutions |
| Marginale ou dépendance, attaque jouée par les organismes | Zhang et Gao (réserve, p. 8) | Activations, copies à poids partagés | Moyen ; borné par N-077 | 3, tête de B |
| Banc à corruptions plantées, difficulté fixée avant | Queen (p. 23, 34) | Loi N-075 ; juge d'une autre lignée | Faible à moyen | 4, papier C |
| Théorie (lemme, théorème) | Aucun manque déclaré | Aucune | Déjà occupé | Hors course |

Pourquoi le rang 1. Il est le préalable commun : il fournit le taux de fausses alertes que quatre modèles sur cinq du collisionneur demandent d'abord [FAIT RAPPORTÉ, contexte]. Il fournit aussi le témoin de même distribution que Parrack avoue ne pas avoir. Il décide trois prévisions de la réponse 9 sans saboteur. Il est publiable dans les deux sens.

Pourquoi le rang 2 n'est pas premier malgré le risque. La course sur les jeux de Parrack est perdue d'avance : ils ont les sondes, les jeux et les moniteurs. L'avance du programme n'existe que sur le sabotage diffus, qui exige le harnais du rang 1.

**Prévisions à sceller sur les concurrents** [HYPOTHÈSE], à six mois :
- Un travail rapporte ce que des sondes rattrapent parmi les manques d'un moniteur boîte noire, à faux positifs fixés : 0,35.
- Un travail donne une loi d'échelle avec référence estimée pour la surveillance de modèles de langue : 0,3.
- Un travail montre un agent réel qui préserve lui-même la marginale de ses scores : 0,25.
- Une suite de Ghanem lève le « provisoire » : 0,5.

### F. Ce que les pièces ne tranchent pas

- **Les prochaines étapes**, faute de rubrique dans les notes.
- **La liste des concurrents.** Des travaux que je connais de mémoire touchent la surveillance d'agents saboteurs. J'ignore s'ils sont au dépôt. Tous sont rapportés, non vérifiés sur PDF :
  - Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion » ;
  - Benton et collaborateurs, 2024, « Sabotage Evaluations for Frontier Models » ;
  - Kutasov et collaborateurs, 2025, « SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents » ;
  - Bhatt et collaborateurs, 2025, « Ctrl-Z: Controlling AI Agents via Resampling » ;
  - Goldowsky-Dill et collaborateurs, 2025, « Detecting Strategic Deception Using Linear Probes », source des sondes de Parrack.
- **L'état actuel des manques.** La version 3 de Parrack date de janvier 2026 [FAIT RAPPORTÉ] ; dix mois ont passé sans recherche descendante.
- **Une pièce fragile.** « Society of AI Scientists » porte un identifiant non standard et la date du 21 novembre, hors de la fenêtre déclarée par la veille (13 au 20) [FAIT RAPPORTÉ]. La provenance est à vérifier avant toute citation.

---

## Question neutre pour le collisionneur

« Plusieurs équipes publient sur la surveillance d'agents de langue qui exécutent de longues tâches et pourraient en dégrader le résultat. On vous remet une liste de ces publications. Pour chacune, établissez à partir du texte seul : ce que les auteurs reconnaissent ne pas avoir fait, ce qu'ils annoncent vouloir faire, et ce qu'ils disent ouvert pour tous. Comment vérifier qu'un manque reconnu par une équipe n'a pas été comblé ailleurs depuis ? Selon quels critères une équipe tierce, aux moyens limités, devrait-elle choisir où concentrer son effort, et quelles observations faites avant de connaître l'issue distingueraient un bon choix d'un mauvais ? Indiquez ce que la liste fournie ne permet pas de décider. »

[PROPOSITION] Servir avec cette question les PDF, ou les seules rubriques « limites » des notes. Les rubriques « ce qui sert au programme » et les pièces de thèse donneraient la réponse attendue et feraient échouer le test de devinette.

---

## Décisions qui reviennent au directeur

**Décision 1 — Choisir le lieu de l'accélération.**
- *Enjeu.* Les cinq semaines restantes ne paient qu'un effort de pointe ; les manques déclarés des voisins désignent plusieurs lieux.
- *Option a : harnais honnête apparié d'abord, complémentarité sur les mêmes exécutions ensuite.* Avantage : préalable commun, issue publiable dans les deux sens, sans saboteur. Inconvénient : la part la plus exposée à la concurrence attend.
- *Option b : complémentarité d'abord.* Avantage : répond au risque le plus élevé d'être devancé. Inconvénient : sans témoin honnête de même distribution, elle reproduit la limite avouée de Parrack.
- *Option c : attaque jouée qui préserve la marginale.* Avantage : manque net chez Zhang et Gao. Inconvénient : dépend des organismes ; N-077 borne ce qu'on peut en dire.
- *Recommandation.* Option a. Confiance : 0,55.

**Décision 2 — Lancer une extraction verbatim avant de sceller ce choix.**
- *Enjeu.* Les prochaines étapes des concurrents ne sont pas dans les notes ; aucun manque n'a été vérifié comme encore ouvert.
- *Option a : extraction ciblée sur six voisins (Khilar, Parrack, Zhang et Gao, Wen, Makins, Rose), double codage, citations descendantes.* Avantage : quelques jours, PDF déjà au dépôt. Inconvénient : le reste demeure paraphrasé.
- *Option b : extraction sur tous les PDF.* Avantage : complet. Inconvénient : délai, rendement faible sur les sources de méthode.
- *Option c : aucune.* Avantage : aucun retard. Inconvénient : on accélère sur une lecture peut-être acquise à la thèse.
- *Recommandation.* Option a, en parallèle du harnais. Confiance : 0,75.

**Décision 3 — Élargir la liste des concurrents par revendication.**
- *Enjeu.* Les pièces viennent d'une recherche d'antériorité sur trois objets ; des concurrents directs peuvent manquer.
- *Option a : recensement par revendication pour les trois axes retenus, à commencer par les travaux nommés en F.* Avantage : ferme l'angle mort. Inconvénient : une recherche de plus.
- *Option b : s'en tenir aux pièces.* Avantage : gratuit. Inconvénient : toute phrase sur « les concurrents » reste partielle.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 4 — Interroger ou non les auteurs.**
- *Enjeu.* Leur réponse est la seule source directe sur leurs suites ; la question révèle l'intérêt du programme.
- *Option a : écrire aux deux ou trois équipes les plus proches.* Avantage : des faits. Inconvénient : dévoile la thèse avant la prévision scellée.
- *Option b : sceller les prévisions et surveiller les listes.* Avantage : aucune fuite, validation par le temps. Inconvénient : lent.
- *Option c : sceller d'abord la prévision du papier A, écrire ensuite.* Avantage : priorité datée, puis faits. Inconvénient : décale le contact de quelques semaines.
- *Recommandation.* Option c. Confiance : 0,5.

**Décision 5 — Fixer ce qui est servi au collisionneur.**
- *Enjeu.* Les notes contiennent les conclusions du programme.
- *Option a : PDF ou rubriques « limites » seules.* Avantage : test de devinette tenable. Inconvénient : préparation.
- *Option b : notes entières.* Avantage : immédiat. Inconvénient : la réponse attendue est lisible.
- *Recommandation.* Option a. Confiance : 0,8.

FIN DE LA RÉPONSE
