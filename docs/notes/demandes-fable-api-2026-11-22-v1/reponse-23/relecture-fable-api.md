# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHfzpvSVbCDwUTM6Gyww`
- Heure (UTC) : 2026-11-22T08:53:14Z
- Réglages : effort `xhigh`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-23-lot-quarantaine-et-revendications-v1.md` — sha256 465b659ddd9a4bb2a05dfceb834aa5b4d7a994774d5275ebc7497f55689cfd20 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-19/relecture-fable-api.md` — sha256 989824d318a452316757b2ead5717fa20bbf81e4fc96a8a7b95ae23a5fec2b3f (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22/relecture-fable-api.md` — sha256 22c5652113797a399d1d1df7fc8d4d6b100bcf04bd655118d51238c5ef3d7b64 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/table-revendications-en-vigueur-v1-sans-nom-v1.md` — sha256 02453d1d92fc589150cf6e27bed56a996aea8a3de86d8580629ecc8cb8e7cddc (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/decision-N-054-v1-sans-nom-v1.md` — sha256 ac859b3a3e4e24604d38fc1628987ccac79edd81344b2f2fb8317fa710f25454 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/decision-N-056-v1-sans-nom-v1.md` — sha256 5871189d64ee0ef878efefb571d50084eed08ce31337ded045f70f4fb9e1c45a (compagnon : vérifié)
- Empreinte de l'invite envoyée : 0806900bd077df7803c4981861b457fbec0f1fcdf082c89a651f4ed526a3f1a8
- Jetons : entrée 54690, sortie 51309 (dont réflexion 41443), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 2.489880 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 23 — la place du lot en quarantaine sous les revendications nouvelles : réponse approfondie

**Conclusion d'abord.**

- Le lot sert la **portée d'une revendication**, non le **franchissement d'une porte**. [FAIT RAPPORTÉ, table] La règle entre modes (D-S10) tient le mode à l'écart hors de la décision de la porte de fin de phase 1 (G1). La règle D-S29 (a) l'exige pour revendiquer le gain de l'accès interne (hypothèse H1a). [PROPOSITION] En faire le principe : les cycles de reconception se décident sans lui, et il s'ouvre une fois, sur la version qui a franchi la porte.
- La quarantaine est un régime de garde. Ce que le lot prouve dépend de son contenu, que j'ignore : trois lectures, trois rôles.
- Les revendications nouvelles changent la grandeur à lire : un écart entre deux unions de moniteurs à taux total de fausses alertes égal, et un déplacement par acte plutôt qu'un rapport de rappels. Elles ne font pas du lot un instrument pour estimer la loi héritée.
- Un mode est un cas : le lot ne porte pas « tient face aux modes jamais vus ».
- Je corrige ma réponse 19 : une tranche par cycle protège le chiffre, pas l'adjectif « tenu à l'écart de la conception ».

Confiance d'ensemble : 0,6.

**Réserves.**
- Je n'ai ni le registre de la quarantaine, ni son motif, ni la définition du lot. Je n'ai vu aucun contenu en quarantaine et n'en propose aucune lecture.
- Je lis N-054 et N-056 dans leur texte ; D-S10, D-S29, N-062 et N-075 à N-077 par résumé. La table des revendications s'arrête à N-074 et ne fait pas foi.
- Les réponses 19 et 22 viennent du même modèle que celle-ci, de la lignée qui conçoit le programme : notre accord n'est pas une confirmation indépendante.
- Les antériorités sont citées de mémoire, « rapporté, non vérifié sur PDF ». Je ne nomme que les auteurs des travaux cités. Les ordres de grandeur sont de ma main, à refaire.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

Toutes les puces sont des PROPOSITIONS.

- **Demander d'abord ce qu'est le lot** : mode conçu à l'aveugle (N-054, point 3), recettes de l'attaquant informé (N-056, point 6), ou pièces écartées par soupçon.
- **Séparer le chiffre de l'adjectif.** Un échantillon frais donne un taux sans biais pour le détecteur du moment. « Tenu à l'écart de la conception » tombe dès qu'un agrégat du lot a guidé une reconception.
- **Compter les modes, non les épisodes.** Un mode écrit par une instance est un tirage de taille un à l'échelle des modes.
- **Mesurer la nouveauté du mode.** Une instance aveugle de la lignée des concepteurs peut inventer ce qu'ils attendaient.
- **Exiger les jumeaux honnêtes des tâches du lot.** Sans eux, « rappel à 1 % de faux positifs » se lit à un taux inconnu sur ces tâches.
- **Fixer les dénominateurs d'avance** : tout épisode tiré compte, sabotage réussi ou non.
- **Répéter l'ouverture sur un lot factice** de même format, pour qu'une panne du script n'oblige personne à regarder.
- **Écrire d'avance le paragraphe de résultat de chaque issue**, l'indéterminée comprise.

## 2. Données brutes de départ

Des métadonnées, jamais le contenu [PROPOSITION] :

- le registre : date d'entrée, motif, origine, empreinte, journal des accès ; le brief, la liste d'exclusions et la lignée de l'instance auteur ;
- le schéma du lot : nombre de recettes, de tâches et d'épisodes ; horizon n et nombre d'actes sabotés par épisode ; présence de jumeaux honnêtes ; accord des deux séries d'étiquetage ;
- les empreintes de toutes les invites envoyées à des modèles depuis l'entrée du lot, étiqueteurs et moniteurs compris ;
- les pièces du gel : sondes, couches, agrégateurs, seuils, liste scellée des moniteurs boîte noire, seconde boîte noire d'une autre lignée, référence honnête (taille m, unité) ;
- les textes de N-055, N-062, N-075 à N-077 et le brouillon du préenregistrement de la porte G1.

## 3. Méthodes et outils

Sauf mention, PROPOSITIONS.

- **Audit de flux** et tableau des cinq propriétés de la réponse 19, strate par strate.
- **Ouverture séquentielle par le pari apparié borné** déjà retenu (N-056, nœud 2). [HYPOTHÈSE, d'après B5] Valide à tout temps d'arrêt, il laisse le dépositaire ouvrir les tâches dans un ordre tiré d'avance et s'arrêter dès que le pari tranche. Le reste demeure scellé.
- **Budget de bits** : tout agrégat rendu avant le gel final est compté. [HYPOTHÈSE, borne d'union sur l'inégalité de Hoeffding] Pour 300 tâches au niveau de 5 %, la marge garantie passe d'environ 8 points sans aucun retour à environ 13 points après dix bits rendus. C'est un pire cas ; B3 rapporte moins en pratique.
- **Intersection-union** sur les contrastes (B6).
- **Mesure de nouveauté à l'aveugle** : un classifieur sur traits de texte sépare-t-il le mode réservé des modes connus ? Seule son exactitude sort.
- **Lot frère** : même brief, instance neuve, tiré après coup (B2 ; N-049 pour la banque sœur).
- **Chaînes canaris et empreintes de fragments**, confrontées aux invites (B7).
- **Témoin de compétence** et **lecture filtrée** (N-053), appliqués au lot comme ailleurs.

## 4. Ce qui vérifie hors du directeur et de Claude

PROPOSITIONS.

- Le dépositaire hors lignée de conception, et son journal recalculable.
- L'horodatage par un tiers des empreintes du gel, de la prévision et de la graine.
- Après l'ouverture finale : lot, détecteur gelé et script publiés ; un tiers réexécute et retrouve les agrégats.
- Le lot frère, la mesure de nouveauté et le témoin de compétence, dont l'issue ne dépend d'aucun avis.
- Une équipe rouge tierce, pour ce que le lot ne mesure pas.
- Un statisticien, sur le budget de bits et la règle d'arrêt.
- Le test de devinette, par des agents neufs de plusieurs lignées.

## Demande reformulée

« Un programme détient un lot d'attaques sous scellés, dont seules les métadonnées sont lisibles. Ses revendications ont changé : une loi héritée sert de modèle nul, la mesure porte sur des scores de sondes, et le gain de l'accès interne se lit contre une seconde boîte noire. Sans lire le lot : (a) dis, selon ce que le registre peut révéler de sa nature, quelle revendication, quelle porte et quelle mesure il peut servir, et lesquelles il ne peut pas ; (b) dis si les revendications nouvelles changent la grandeur à lire, et ce qui doit exister avant l'ouverture ; (c) situe-le par rapport au mode conçu à l'aveugle et à une équipe rouge tierce, avec l'ordre des opérations ; (d) liste ce qui se scelle, ce qui consomme le chiffre ou seulement l'adjectif, et l'échelle de contamination avec sa suite ; (e) dimensionne : puissance, nombre de modes, jumeaux honnêtes ; (f) nomme antériorités et indices contraires ; (g) donne les contrôles qui ne dépendent d'aucun avis. »

## Antériorités citées

Toutes rapportées, non vérifiées sur PDF.

- [B1] Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, 2015, « The reusable holdout: preserving validity in adaptive data analysis » ; Blum, Hardt, 2015, « The Ladder: a reliable leaderboard for machine learning competitions ».
- [B2] Recht, Roelofs, Schmidt, Shankar, 2019, « Do ImageNet classifiers generalize to ImageNet? ».
- [B3] Indice contraire : Roelofs et collaborateurs, 2019, « A meta-analysis of overfitting in machine learning » (peu de surajustement mesuré malgré le réemploi).
- [B4] Lan, DeMets, 1983, « Discrete sequential boundaries for clinical trials » (analyses intermédiaires, vues par un comité indépendant).
- [B5] Waudby-Smith, Ramdas, 2023, « Estimating means of bounded random variables by betting » ; Shafer, 2021, « Testing by betting ».
- [B6] Berger, Hsu, 1996, « Bioequivalence trials, intersection-union tests and equivalence confidence sets ».
- [B7] Jacovi, Caciularu, Goldman, Goldberg, 2023, « Stop uploading test data in plain text » ; Srivastava et collaborateurs, 2022, « Beyond the imitation game » (chaîne canari ; détail incertain).
- [B8] Klein, Roodman, 2005, « Blind analysis in nuclear and particle physics » ; Chambers, 2013, « Registered Reports: a new publishing initiative at Cortex ».
- [B9] Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI control: improving safety despite intentional subversion » ; Tramèr, Carlini, Brendel, Madry, 2020, « On adaptive attacks to adversarial example defenses ».

Le champ est occupé. Je ne revendique rien de neuf ; seule l'application au lot du programme est en question.

## (B) Réponse à la demande reformulée

### B1. Trois lectures du lot

[HYPOTHÈSE ; à établir au registre]

| Lecture | Le lot sert | Le lot ne sert pas |
|---|---|---|
| I. Mode conçu à l'aveugle (N-054, point 3 ; bras A de N-056) | portée de H1a ; expérience de lecture de N-054, point 4 | décision de la porte ; tenue face à l'adapté |
| II. Recettes de l'attaquant informé interne (bras B) | majorant descriptif, courbe selon le budget | toute revendication (N-077) |
| III. Pièces écartées par soupçon ou de provenance inconnue | description ; jeu de développement après déclassement | toute revendication |

Si le lot mêle ces lectures, ce sont des strates : jamais d'agrégat commun. La suite vaut pour la lecture I.

### B2. Revendication par revendication

Les énoncés viennent de la réponse 22 et des décisions [FAIT RAPPORTÉ]. Les colonnes « peut » et « ne peut pas » sont des PROPOSITIONS.

| Revendication, porte ou mesure | Le lot peut servir | Le lot ne peut pas servir |
|---|---|---|
| Gain de l'accès interne (H1a), récrit par la réponse 22 | La lecture principale : écart de rappel entre l'union « meilleure boîte noire et sonde » et l'union « meilleure boîte noire et seconde boîte noire d'une autre lignée », seuils recalés d'avance au même taux total | Le choix de la « meilleure » boîte noire, de la couche ou de l'agrégateur |
| Porte G1 (N-056 : battre chaque boîte noire, la cascade et le dernier état) | Une colonne rapportée par mode (N-054, point 2) | La décision (D-S10) ; le contraste blanc contre blanc, sauf dimensionnement égal aux autres modes (N-056, point 4) |
| Expérience de lecture (N-054, point 4) : bras génériques contre spécialisés | Son objet d'origine | Une conclusion tirée du seul rapport des rappels (voir plus bas) |
| Accumulation contre le nul hérité | Une vérification hors plan de la prévision scellée (N-076) : rappel prédit depuis le déplacement par acte mesuré à l'aveugle, l'horizon n et la référence m | L'estimation de l'exposant ou de la constante : ni la dose ni l'horizon n'y sont réglés |
| Question « position ou dépendance » | Deux agrégats descriptifs écrits d'avance | Une revendication |
| N-075 : motif et dommage au même lieu | La localisation : l'alerte tombe-t-elle sur les actes sabotés, connus par la recette ? | Le taux de détection q de l'audit d'issue sans décision séparée (l'auditeur deviendrait lecteur) ; le plancher d'audit, qui ne dépend pas de l'attaque |
| Papier B (co-élévation, statistique conjointe, courbe selon le nombre d'agents) | Rien, sauf attaques à plusieurs copies au registre [HYPOTHÈSE] | — |
| Papier C (juges sous attaque) | Rien : des recettes de sabotage ne sont pas des attaques contre des juges [HYPOTHÈSE] | La « vérification par un tiers » |
| Robustesse | — | Toute phrase « résiste à » (N-077 ; adaptation absente) |
| Généralité | « Un mode conçu à l'aveugle » | « Les modes jamais vus » : il y faut plusieurs modes indépendants, en nombre fixé d'avance, comme N-044 le fait pour les familles |

**La grandeur à lire change** [HYPOTHÈSE, dérivation de ma main]. Sous la loi héritée, le rappel d'un cumul dépend du déplacement par acte, du nombre d'actes sabotés et de l'horizon. Le rapport des rappels entre modes confond donc le transfert de la sonde et la différence d'horizon.

[PROPOSITION] Lire d'abord le rapport des déplacements par acte standardisés, mode réservé sur mode connu. Rapporter le rappel à côté de sa valeur prédite par le nul. Si le déplacement est nul sur le mode réservé, le nul « tient » trivialement : le résultat est le déplacement.

### B3. Articulation avec le mode tenu à l'écart et l'équipe rouge d'une autre famille

[HYPOTHÈSE sur les rôles ; PROPOSITION sur l'ordre]

- **Trois propriétés.** « Tenu à l'écart » décrit la conception : auteur aveugle aux moniteurs, concepteurs aveugles au mode. « En quarantaine » décrit la garde, qui rend la première vérifiable. « D'une autre famille » décrit l'auteur et son adaptation au détecteur gelé.
- **Trois preuves.** Le lot en lecture I donne le non-adapté jamais vu. Le bras informé interne donne un majorant descriptif. L'équipe rouge tierce donne l'adapté. Aucune ne remplace l'autre.
- **Ordre.**
  1. Cycles de reconception sur les modes mesurés, sans le lot.
  2. Gel.
  3. Équipe rouge tierce, code en main ; si elle impose une reconception, retour à l'étape 1, lot intact.
  4. Ouverture du lot, dernier acte avant la version soumise.
  5. Tout changement ultérieur du détecteur appelle un mode neuf.
- **Pas de graine.** Le lot ne nourrit pas l'équipe rouge.
- **Indépendance mesurée.** À l'ouverture, la ligne du lot entre dans la matrice de succès croisés. Un recouvrement résiduel élevé avec le mode « coût » dit que la nouveauté était nominale.
- **Limite d'auteur.** [FAIT RAPPORTÉ, N-054] L'instance auteur proposée est de la lignée qui conçoit les moniteurs. Le lot a alors l'étanchéité, non l'indépendance d'auteur : écrire « tenu à l'écart de la conception », jamais « indépendant ».
- **Question au registre.** [FAIT RAPPORTÉ, table] La revendication finale se lit sur une famille de tâches jamais servie à une reconception (N-062). Le lot joue-t-il le mode réservé sur cette famille ? Sinon, la nouveauté des tâches manque.

### B4. Ce qui se scelle avant l'ouverture

[PROPOSITION] À empreinte, horodaté par un tiers :

1. le détecteur : sondes, couche principale désignée (les trois restant rapportées), agrégateurs, seuils ; les deux unions recalées ; la « meilleure boîte noire », désignée sur les modes connus ; la seconde boîte noire ;
2. la référence honnête : taille m, unité, horizon admis, source de validité (N-076) ; les épisodes d'horizon supérieur à m forment une strate hors garantie ;
3. la prévision : par bras, signe et bande, en déplacement par acte puis en rappel ; les chances de chaque issue ;
4. la règle : pari, niveau, liste d'intersection-union, règle d'arrêt, définition de l'indéterminé ;
5. la liste fermée des agrégats, leur arrondi, le budget de bits ; aucun exemple ne sort ;
6. les dénominateurs, le témoin de compétence, la définition de « diffus », la mesure de nouveauté ;
7. la graine de l'ordre d'ouverture, l'empreinte du script, le dépositaire, le procès-verbal de la répétition sur lot factice ;
8. l'échelle de contamination et ses suites ;
9. le paragraphe de résultat de chaque issue.

### B5. Ce qui le consomme

[HYPOTHÈSE]

- **Chiffre et adjectif** : lecture par un concepteur, humain ou modèle ; entrée dans l'apprentissage ou le calibrage ; choix de couche, d'agrégateur ou de boîte noire sur le lot ; panne du script suivie d'une inspection.
- **Adjectif seul** : tout agrégat rendu avant le gel final, y compris au directeur ou à moi, s'il précède une décision de conception. Le chiffre mesuré ensuite sur des tâches non ouvertes reste valide pour ce mode.
- **Rien, si c'est déclaré** : l'exécution des moniteurs gelés et l'étiquetage, par des appels sans mémoire dont les journaux vont au seul dépositaire. Je précise ainsi la condition 8 de la réponse 19 : un moniteur gelé qui note un épisode exécute, il ne conçoit pas.
- **Après l'ouverture finale** : toute analyse ajoutée est exploratoire. Publier le lot le consomme pour l'avenir et permet la vérification.

### B6. S'il est contaminé

[PROPOSITION] L'échelle est écrite d'avance ; le doute se range au niveau supérieur.

| Niveau | Constat | Suite |
|---|---|---|
| 0 | journal complet, aucun accès côté défense | conditions de B4 |
| 1 | fuite de métadonnées (nom du mode, taille) | déclarée ; le dépositaire juge si le nom vaut contenu |
| 2 | agrégat vu avant le gel | adjectif perdu ; chiffre rapporté comme « mode connu par ses agrégats » |
| 3 | contenu lu, porté par une invite à un modèle de la lignée des concepteurs, ou entré dans un apprentissage | lot reclassé en jeu de développement ; colonne « mode tenu à l'écart » comptée non mesurée (cohérence avec N-075) ; mode neuf par une instance neuve |
| 4 | fuite inverse : l'auteur a vu les moniteurs | passage en lecture II, majorant descriptif |
| 5 | journal incomplet | traité comme le niveau 3 pour toute revendication |

- Jamais de « décontamination » par retrait de pièces.
- [HYPOTHÈSE] Le lot est renouvelable à l'échelle du mode si le brief et les exclusions sont intacts. Le coût est celui du dimensionnement (N-056, point 4), non celui de la recette.
- Contrôle : sur un lot frère tiré après coup, un écart en faveur de l'ancien lot signale contamination ou adaptation (B2).

## (C) Question neutre pour le collisionneur

**Test de neutralité appliqué.**
1. Sont retirés : « quarantaine », « tenu à l'écart », « porte », « sonde », les numéros de décision et mes conclusions.
2. Chaque question offre ses issues au même rang ; leur ordre est tiré au sort pour chaque modèle.
3. Test de devinette [PROPOSITION, non exécuté] : trois agents neufs de lignées différentes lisent la question seule et parient sur l'issue que l'auteur préfère aux questions 1 à 3. Mes réponses sont scellées avant. La question passe si leurs paris ne font pas mieux que le hasard ; sinon elle est récrite.
4. Défauts résiduels : « discrète » et « genre » portent notre découpage ; le changement d'affirmations est résumé par moi ; la description du lot est à corriger depuis le registre avant envoi.

**Question.**

« Une équipe met au point des détecteurs qui surveillent un agent logiciel pendant de longues tâches, pour repérer une dégradation discrète du résultat. Elle les améliore par cycles, en nombre non fixé, et passe à l'étape suivante quand un critère chiffré est atteint. Elle détient un ensemble de cas de dégradation d'un genre que les auteurs des détecteurs n'ont pas consulté. Depuis la constitution de cet ensemble, ce que l'équipe affirme a changé. Elle ne soutient plus qu'un détecteur est bon en soi. Elle veut dire (i) si ses mesures s'écartent d'une loi déjà publiée et (ii) si un détecteur qui lit l'état interne de l'agent ajoute quelque chose à un second détecteur qui lit le texte.

1. À quoi cet ensemble peut-il servir : au critère de passage, à la portée de ce que l'équipe affirme, aux deux, à autre chose, à rien ?
2. Quand le consulter : à chaque cycle, par parties, une seule fois, jamais, autrement ?
3. S'il s'avère que des auteurs de détecteurs l'ont vu, en tout ou en partie : le garder, le déclasser, le jeter, le refaire, ou cela dépend-il d'un élément à nommer ?
4. Le changement de ce que l'équipe affirme modifie-t-il vos réponses : oui, non, en partie ?

Toutes les issues citées sont également recevables, ainsi que toute autre. Pour chaque réponse : l'énoncé réfutable et ce qu'on mesurerait ; l'antériorité la plus proche, tous domaines confondus (auteurs, année, titre), en disant si vous citez de mémoire ; un contrôle dont l'issue ne dépend de l'avis de personne ; votre degré de certitude. »

## Décisions qui reviennent au directeur

**Décision 1 — Faire dire au registre ce qu'est le lot, et le découper en strates de statut distinct.**
- *Enjeu.* Selon la lecture I, II ou III, le lot ne sert pas la même chose.
- *Option a : strates séparées, jamais d'agrégat commun.* Avantage : chaque strate garde sa lecture. Inconvénient : puissance divisée.
- *Option b : lot unique.* Avantage : simple. Inconvénient : ni « jamais vu » ni « majorant » ne se lit.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 2 — Placer le lot hors de la décision de la porte G1, dans la seule portée de la revendication.**
- *Enjeu.* L'adjectif « tenu à l'écart de la conception » et l'écart entre D-S10 et D-S29 (a). La tranche par cycle de la réponse 19, déjà accordée, serait amendée.
- *Option a : cycles décidés sur les modes mesurés ; lot ouvert une fois, en séquentiel, sur la version qui a franchi la porte.* Avantage : chiffre et adjectif gardés. Inconvénient : un échec tardif restreint la revendication ou appelle un mode neuf.
- *Option b : une tranche par cycle, comme accordé.* Avantage : alerte précoce. Inconvénient : le mode guide la conception par ses agrégats.
- *Option c : un bit par cycle, budget compté.* Avantage : compromis chiffrable. Inconvénient : adjectif affaibli quand même.
- *Recommandation.* Option a. Confiance : 0,65.

**Décision 3 — Désigner la lecture principale du lot sous la thèse nouvelle.**
- *Enjeu.* Une seule ouverture : une lecture principale par question, fixée avant.
- *Option a : écart entre les deux unions pour H1a ; rapport des déplacements par acte pour l'expérience de N-054 ; contrastes de N-056 rapportés à côté.* Avantage : conforme à la thèse accordée. Inconvénient : exige la seconde boîte noire gelée avant.
- *Option b : contrastes de N-056 en lecture principale.* Avantage : aucun texte à changer. Inconvénient : contraste blanc contre blanc peu puissant ; lettre antérieure à la thèse.
- *Option c : les deux, en intersection-union.* Avantage : dit le plus. Inconvénient : issue indéterminée probable.
- *Recommandation.* Option a. Confiance : 0,55.

**Décision 4 — Dimensionner avant de sceller : jumeaux honnêtes, puissance, second mode.**
- *Enjeu.* Un lot trop court ou sans jumeaux donne une issue indéterminée et se consomme quand même.
- *Option a : puissance calculée sur lot factice ; jumeaux honnêtes produits par le dépositaire ; second mode en réserve, écrit par une instance d'une autre lignée.* Avantage : épreuve qui peut échouer ; deux cas au lieu d'un. Inconvénient : devis de la couche 2 alourdi.
- *Option b : la même sans second mode.* Avantage : moins cher. Inconvénient : un seul cas, aucune réserve si la version change.
- *Option c : ouvrir tel quel.* Avantage : aucun délai. Inconvénient : taux de faux positifs inconnu sur ces tâches.
- *Recommandation.* Option a, repli sur b. Confiance : 0,65.

**Décision 5 — Adopter l'échelle de contamination et la suite « déclasser, déclarer, refaire ».**
- *Enjeu.* Une règle écrite après le constat est suspecte.
- *Option a : échelle de B6, doute rangé au niveau supérieur, lot frère en contrôle.* Avantage : graduée et vérifiable. Inconvénient : un tirage de plus.
- *Option b : binaire, tout doute jette le lot.* Avantage : simple. Inconvénient : perd un lot atteint par ses seules métadonnées.
- *Option c : au cas par cas.* Avantage : souple. Inconvénient : décidé en connaissant l'enjeu.
- *Recommandation.* Option a. Confiance : 0,7.

FIN DE LA RÉPONSE
