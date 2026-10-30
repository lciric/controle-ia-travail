# Archive — question du brainstorm du texte III (mesurer et valider l'universalité des défenses) — v3

v3 (rédacteur neuf, 30 octobre 2026, relevé `date -u` 11:43 UTC) : la v2 (`c946b566…`, inchangée) corrigée par la contre-lecture. Le fond ne change pas : blocs 1 à 4, décision « plusieurs instances » au bloc 4, quatre modèles. Cette archive réunit deux pièces scellées à part, reproduites ci-dessous à l'identique :

- **fichier d'envoi** `question-texte-III-envoi-v3.md` (`2961ad06fc1ed63f52bc6e93b16b0e6d6c2b35cfa0ed6d486a27f0568d94bf89`), seul texte transmis, versé comme `question-etage3.md` par `collisionneur_v5.py` ;
- **critères de lecture** `criteres-lecture-texte-III-v1.md` (`99132ff199338bf3ebd55349df8215b65a622086449011657de0766228102066`), jamais envoyés ;
- faits servis au collisionneur : `faits-texte-III-v2.md` (`d920af2a1dde64452361c1fa6005929658f2d30164c05f2f526059e8941495f8`).

Destinataires : le collisionneur à quatre modèles (`claude-fable-5-1`, `claude-opus-5-5`, `gemini-4-argon`, `kimi-k3.1-pro` ; `collisionneur_v5.py`, `93571067…`), trois tours de l'étage III ; puis Argon seul.

**Argon seul** reçoit le fichier d'envoi seul, sans préambule du collisionneur ni faits, par la chaîne de `../collisionneur-bisociation-v1/lancer-argon-bisociation-v1.sh` (relais Gemini local, enveloppe `/opt/argon/appel-argon-v3.sh`, `commande_argon_v2.py`) ; limite de mots globale ≈ 3 500 (dernière ligne de l'envoi).

**Participation et mise à l'écart** : un modèle qui participe à ce brainstorm n'est pas, de ce seul fait, tenu à l'écart du protocole de mesure ; une instance qui concevra des familles tenues à l'écart (bloc 4) doit l'être par une décision et un scellement propres.

## Constats de la contre-lecture appliqués

| Constat | Endroit corrigé |
|---|---|
| CL-01 (bloquant) | Envoi, contexte, « Donnée de départ » : même question ; lecteur unique de la lignée d'une source ; grille fermée au lecteur |
| CL-02 | Faits v2, faits 13 à 15 : `collisionneur_v5.py`, modèles A à D (Kimi compris), lignes de `MODELES`, `TOURS`, `CONSIGNES`, `PREAMBULE`, injection ; empreinte égale au `.sha256` |
| CL-03 | Faits v2 (en-tête, faits 2, 3, 4, 7 à 9, 11, 12) ; envoi (contexte : liste des statuts ; fin du bloc 4 : HYPOTHÈSE) ; critère 5 |
| CL-04 | Trois fichiers : envoi (garde, contexte, question, insertion ; sans version, auteur ni critères) ; critères à part ; la présente archive |
| CL-05 | Déjà appliqué dans `collisionneur_v5.py` (exception à la règle 6 pour le bloc QUESTION) ; rien à changer ici |
| CL-06 | Envoi, « Périmètre » : garde en positif, texte proposé repris mot pour mot |
| CL-07 | Envoi, contexte (« banc d'évaluation adverse simulé ») et bloc 1(b) réécrit ; faits v2, fait 1 |
| CL-08 | Envoi, bloc 2 : propriétés de format, licence, étiquetage, indépendance ; trois bancs au plus |
| CL-09 | Envoi, bloc 3, point 4 |
| CL-10 | Envoi, bloc 3, point 3 ; critère 3 |
| CL-11 | Envoi, bloc 1(a) ; critère 1 |
| CL-12 | Envoi, « Insertion » : table (a) à (d), ordre (a), (b), (c), blocs 1 à 4, (d) ; plafonds dans les titres des blocs |
| CL-13 | Envoi, « Insertion » : contenu de la page du tour III.3 |
| CL-14 | Envoi, contexte (règle de base, tailles) et bloc 4 (décision) marqués RAPPORTÉ ; faits v2, faits 2 à 4 |
| CL-15 | Envoi, contexte et bloc 1(d) : familles propres 10 et 6, intersection 18 ou 19, deux conventions ; faits v2, faits 7 et 8 |
| CL-16 | Faits v2, fait 9 |
| CL-17 | Envoi entier au tutoiement ; bloc 3 « au plus cinq dans ta proposition » |
| CL-18 | Présente archive, paragraphe « Argon seul » |
| CL-19 | Envoi, bloc 4 ; présente archive, paragraphe « Participation et mise à l'écart » ; critère 2 |

Valeurs recalculées (faits v2, faits 7 à 9) : Lincoln-Petersen 38,89 (m = 18) et 36,84 (m = 19) ; Chapman 38,68 et 36,70 ; familles observées 34 ou 35 ; borne à zéro échec 29, 59, 149 familles pour ε = 0,10, 0,05, 0,02.

Envoi : 1 458 mots (`wc -w`).

---

# Pièce 1 — fichier d'envoi (reproduit à l'identique)

## Périmètre (à respecter sans exception)

Le périmètre est statistique et méthodologique : définitions, estimateurs, plans de mesure, validation. Aucune famille, aucun comportement d'agent et aucun moyen ne sont décrits, même à titre d'illustration ; la réponse qui le ferait est écartée.

## Contexte (autoportant : il suffit à répondre)

Un programme de recherche défensive étudie le contrôle de systèmes d'intelligence artificielle : détection d'un sabotage diffus par des sondes sur les activations internes et par des moniteurs qui ne lisent que le texte (boîte noire), avec agrégation séquentielle des indices ; modèles à poids ouverts de 8 et de 70 milliards de paramètres (RAPPORTÉ, demande du directeur). Règle de base : le programme ne construit aucun agent attaquant opérationnel (RAPPORTÉ, demande du directeur). Pour évaluer ses défenses, il utilise des **familles** (classes d'éléments d'évaluation simulés, définies par un schéma de construction, jamais décrites ici), dont certaines sont **tenues à l'écart** : ni les concepteurs de la défense ni la défense ne les voient avant la mesure finale.

Le **texte III** d'une course d'idéation demandera, au niveau méthode, comment concevoir un **banc d'évaluation adverse simulé** (il sert à mesurer, sans agent opérationnel) et une **mesure de l'universalité** des défenses qu'**un tiers puisse vérifier**. Ta réponse produit les questions candidates de ce texte ; elle sert de matériau à un préenregistrement et ne tranche rien.

Chaque fait porte un statut : VÉRIFIÉ, RAPPORTÉ, OBSERVÉ-NON-AUDITÉ ou HYPOTHÈSE. Tout chiffre qui ne vient pas du contexte ou des faits est marqué « illustratif » ; une référence que tu ne peux pas attribuer (auteurs, année, titre) porte « référence à vérifier ».

Donnée de départ (VÉRIFIÉ ; calculs refaisables) : deux sources indépendantes en apparence ont énuméré 28 et 25 familles. Selon le dossier, les deux sources sont deux modèles de fournisseurs différents, qui ont reçu la même question ; un lecteur unique, de la lignée d'une des deux sources, a fait l'appariement avec une grille fermée ; l'appariement n'est pas bijectif (une famille de la première source en recouvre deux de la seconde). L'intersection vaut donc 18 comptée du côté de la première source et 19 du côté de la seconde ; 10 familles sont propres à la première, 6 à la seconde. Lincoln-Petersen (n₁ × n₂ / m) : 38,9 avec m = 18, 36,8 avec m = 19. Chapman ((n₁ + 1)(n₂ + 1) / (m + 1) − 1) : 38,7 ou 36,7.

## Question

« Conçois la **méthode** qui permettrait d'affirmer, devant un tiers, qu'une défense est universelle sur un ensemble de familles, et de confronter cette affirmation à des mesures extérieures. Réponds par quatre blocs, dans cet ordre.

### Bloc 1 — Quatre propositions préalables, avant toute question candidate (au plus 1 200 mots)

**(a) Définition opérationnelle de l'universalité.** Options à comparer : pire cas sur une classe de familles déclarée d'avance ; écart de performance entre familles vues et familles tenues à l'écart ; quantile ou proportion de familles où la défense passe un seuil ; autre. Pour chacune : ce qu'il faut déclarer avant la mesure, l'énoncé exact qu'elle autorise (avec quantificateur, classe et statistique), ce qu'elle n'autorise pas, et comment un tiers la vérifie. Dis en particulier ce qui sépare « universelle sur la classe déclarée » de « robuste à l'inconnu ».

**(b) Régime d'information de l'évaluation** : aveugle ou informé de la défense ; quelles catégories d'information sont accessibles au banc d'évaluation (existence de la défense, liste des familles, protocole, seuils) ; budget d'évaluation (nombre d'éléments, calcul) ; rapport par palier. Précise aussi ce que l'évaluation interdit de partager entre construction et évaluation de la défense.

**(c) Combien de familles, par simulation.** Comment calculer le nombre de familles nécessaire pour affirmer l'universalité avec une confiance donnée : énoncé cible (par exemple : avec confiance 1 − α, la part de la classe où la défense échoue est inférieure à ε), modèle génératif de la population de familles, hétérogénéité et dépendance entre familles proches, variance à deux niveaux (entre familles, et entre éléments d'une famille), règle d'arrêt séquentielle, analyses de sensibilité. Un point à traiter : les familles sont **découvertes**, non tirées au hasard ; la garantie dépend donc du mécanisme de découverte. Dis ce que la simulation peut démontrer et ce qu'elle suppose.

**(d) Combien de familles encore inconnues.** Vérifie les calculs de Lincoln-Petersen et de Chapman donnés au contexte sous les deux conventions d'appariement (m = 18 et m = 19), et dis laquelle se défend et pourquoi. Discute ensuite leurs hypothèses : population fermée, indépendance des sources, même probabilité de capture pour toutes les familles, appariement exact. Dis dans quel sens la dépendance entre sources, l'hétérogénéité et l'erreur d'appariement déplacent l'estimation. Indique quels estimateurs employer avec plusieurs sources : Chao (bornes inférieures), Good-Turing (masse manquante, couverture), capture-recapture multi-sources (modèles log-linéaires, classes latentes), approche bayésienne. Dis comment tester l'indépendance, comment traiter un refus commun de répondre (une même censure sur toutes les sources) et ce que devient l'estimation si le nombre de familles n'est pas fermé.

### Bloc 2 — Données de départ à recommander (au plus 400 mots)

Plutôt que des résumés, quelles données brutes recommandes-tu, et pourquoi ? Candidates : (i) les trajectoires brutes de bancs publics conçus par d'autres (SHADE-Arena, ControlArena, MonitoringBench, SLEIGHT-Bench, Liars' Bench), utilisées comme **familles extérieures** ; (ii) les journaux de refus de questions passées ; (iii) les propositions brutes d'une course précédente. Pour chacune : indépendance réelle vis-à-vis du programme, étiquetage au niveau des familles, risque de recouvrement avec ce que les modèles ont déjà vu, coût de mise au format, usage possible comme source supplémentaire de capture-recapture. Décris chaque banc par ses propriétés de format, de licence, d'étiquetage et d'indépendance, sans en décrire les tâches ni les comportements ; trois bancs au plus. Si tu ne connais pas un banc, dis-le : n'invente ni contenu ni référence.

### Bloc 3 — Questions candidates pour le texte III (au plus 900 mots)

**Au plus cinq dans ta proposition.** Chaque question est formulée en termes de mesurer, valider, borner ou estimer. Pour chacune :

1. l'**avantage** qu'elle exploite ;
2. le **piège méthodologique** qui la tuerait ;
3. la **validation extérieure** qu'elle permet (familles conçues hors du programme, prédictions scellées confrontées à des mesures, revue extérieure), chiffrée : nombre de familles extérieures, taille ou seuil ; illustratif si hors des faits ;
4. le risque qu'elle soit jugée hors du périmètre méthodologique (faible, moyen, élevé ; illustratif), et l'élément de la question qui la borne à la mesure.

### Bloc 4 — Question annexe (au plus 700 mots)

**Décision prise par le directeur** (RAPPORTÉ) : les familles tenues à l'écart seront conçues par **plusieurs instances indépendantes**, de fournisseurs et de modèles différents (cinq sont prévues), chacune tenue à l'écart de la conception des défenses et scellée à part. Propose **comment l'organiser** ; ne propose aucun contenu de famille ; ta réponse ne doit rien anticiper de ce que concevront les instances :
- ce que chaque instance reçoit (même consigne ou consignes différentes) ;
- comment empêcher les fuites entre elles ;
- comment apparier leurs familles sans qu'un lecteur unique biaise l'appariement ;
- comment tester leur indépendance (corrélation des données d'entraînement entre fournisseurs) ;
- comment s'en servir comme sources multiples pour estimer les familles encore inconnues ;
- ce qu'on fait si une instance refuse.

Pour chaque point : options, avantage, inconvénient, recommandation et confiance. Ce qui n'est pas dans les pièces ou dans le contexte est marqué HYPOTHÈSE. »

## Insertion dans les consignes du tour

Correspondance avec les livrables du tour III.1 :

| Livrable du tour | Ce qu'il contient ici |
|---|---|
| (a) ce que la question suppose sans que ce soit établi | les hypothèses des blocs 1(b) à 1(d), une ligne chacune, avec son statut |
| (b) expériences décisives en duel H_A contre H_B | au moins deux duels portant sur des **estimateurs ou des définitions** (par exemple : Lincoln-Petersen contre bornes de Chao), avec métrique, seuil, contrôle négatif et issue qui falsifie chaque hypothèse |
| (c) mesure minimale de chaque instrument nommé | l'instrument est l'**estimateur du nombre de familles** et la **mesure d'universalité** ; la mesure minimale est leur couverture et leur biais sur des mondes simulés à vérité connue, contre une base à battre (comptage brut des familles observées) |
| (d) ancrage matériel | au plus 100 mots |

Ordre de la réponse : (a), (b), (c), puis les blocs 1 à 4, puis (d). Les plafonds des blocs sont des maximums, non des cibles ; le total respecte la limite de mots du tour. Si la place manque, garde dans l'ordre les blocs 1, 3, 4, 2.

Au tour III.3, la page de réponse à la question contient : définition retenue, estimateur retenu, au plus cinq questions candidates révisées, organisation recommandée en cinq lignes.

Si tu reçois cette question sans consignes de tour, suis le même ordre et les mêmes plafonds, au plus 3 500 mots en tout.

---

# Pièce 2 — critères de lecture (reproduits à l'identique, jamais envoyés)

# Critères de lecture de la synthèse — brainstorm du texte III (mesure de l'universalité) — v1

Gelés avant lecture, scellés à part, **jamais envoyés** (ni au collisionneur, ni à Argon seul). Repris de la question v2 (`c946b566…`) avec les ajustements de la contre-lecture : statuts du préambule (CL-03), définition jugée sur le quantificateur, la classe et la statistique (CL-11), validation extérieure chiffrée (CL-10), périmètre en positif (CL-06). Envoi lu : `question-texte-III-envoi-v3.md` ; faits servis : `faits-texte-III-v2.md`.

1. Une définition de l'universalité n'est retenue comme « commune » que si deux modèles au moins la donnent avec le même quantificateur, la même classe déclarée et la même statistique ; sinon « divergente », options au format décision.
2. Une réponse qui décrit une famille, un comportement d'agent ou un moyen, même à titre d'illustration (recette, exemple de mode, scénario d'évasion, paramètre concret de famille), est écartée et comptée ; de même une réponse qui propose un contenu de famille ou anticipe ce que concevront les instances du bloc 4.
3. Une question candidate sans validation extérieure chiffrée (nombre de familles extérieures, taille ou seuil) ou sans piège nommé est marquée « non retenue ».
4. Un estimateur du nombre de familles sans ses hypothèses explicites est marqué « non jugeable » ; un calcul de Lincoln-Petersen ou de Chapman qui ne dit pas sa convention d'appariement (m = 18 ou m = 19) est signalé.
5. Un fait présenté avec un statut autre que VÉRIFIÉ, RAPPORTÉ, OBSERVÉ-NON-AUDITÉ ou HYPOTHÈSE, ou dont le statut a été changé, est signalé ; un chiffre hors des faits non marqué « illustratif » est signalé.
6. L'avis d'Argon à part est lu à côté, non compté dans « commun ».
