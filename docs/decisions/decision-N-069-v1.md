# Décision — N-069 : papier B, statistique de population et statistique spatio-temporelle resserrées après 2601.05427, 2605.11135, J-PACT et 2611.10620 (v1)

- **Décision de Lazar** : mots directs consignés à R-2555 (`registres/decisions.md`, 2026-11-13, 18:15 UTC). Option **B (a)** : les quatre collisions partielles constatées sur PDF sont tranchées en bloc, sur les recommandations ; pour le papier B, « statistique de population du papier B resserrée (R-2181, lot 7-B) ». Troisième des quatre décisions (N-067 à N-070).
- **Statut : version retenue (v1).** Écrite le 13 novembre 2026 entre 19:24 et 19:29 UTC (`date -u`) par le rédacteur des brouillons. Elle reprend le brouillon 2 (`decision-N-069-v1-brouillon2.md`, `69f8f699…`, écrit entre 18:54 et 18:59 UTC — **erratum** : son en-tête porte « vers 19:00 UTC », heure écrite d'avance ; R-2568), corrigé selon la contre-lecture (`contre-lecture-decisions-N-067-a-N-070-v1.md`, `db44d995…`, R-2565), et y porte les décisions de Lazar sur le point en trois volets de son encadré (R-2571, section 0). Elle resserre aussi l'énoncé 2 sur un constat de la contre-lecture de la synthèse finale (R-2567, constat M2 ; section 4). Brouillons 1 et 2 intacts (R12). Journal : `journal-decisions-N-067-a-N-070-v3.md`. Restent à la session mère : la ligne de type « revendication » à `registres/go.md` et la liste des décisions de `CLAUDE.md`.
- **Nœud posé par** : R-2181 (lot 5-A, boîte noire), lot 7-B (sur états internes), R-2190 ; complément 1 de la synthèse provisoire de niveau 3, section 1. Énoncés d'origine : programme v2 (papier B, E3.1, porte G2) ; N-013, l. 90 (« la statistique de population du papier B » inchangée).
- **Portée.** Cette note fixe la lecture de la statistique de population (co-élévation entre copies, l'agrégateur A_pop) et de la statistique spatio-temporelle (A_spatio-temporel, E3.1) du papier B, en attendant une version nouvelle du programme, qu'elle ne modifie pas. Aucune hypothèse n'est retirée (R3). Le **déclencheur de bascule** (programme, l. 239) n'est **pas** tranché ici (section 9).
- **Règle de lecture.** « Libre » veut dire « non trouvé dans les pièces lues » (R8). Chaque page citée vient d'un rapport de lecteur qui l'a contrôlée par programme sur le PDF empreinté.

## 0. Décisions de Lazar (R-2571)

Mots directs de Lazar, verbatim (R-2571, 13 novembre 2026, 19:24 UTC) :

> c'est crédité, relance; les onze points des décisions de resserrement. : quels sont ils ? go reco

Lecture de la mère, consignée au même registre : les onze points des brouillons 2 de N-067 à N-070 « prennent tous la recommandation ». Les options posées restent lisibles dans l'encadré du brouillon 2 (`69f8f699…`).

| point | décision posée | option retenue | effet dans cette note |
|---|---|---|---|
| 9a | déclencheur de bascule (programme, l. 239) | **(a)** **bascule non déclenchée** ; veille rapprochée sur les suites de NARCBench | section 9 |
| 9b | critère de la porte G2 (l. 208) | **(a)** **le pic par agent devient base nommée de la porte G2**, et le cas « pas de gain » est prévu, au préenregistrement de G2 | sections 5 et 8 |
| 9c | mot « co-élévation » de l'énoncé 1 | **(c)** « co-élévation » gardé ; **l'écart entre agents devient une base obligatoire** du préenregistrement | sections 4 et 7 |

## 1. Mots de Lazar, verbatim (R-2555)

> A (a) go, B (a) go, D go, C. Horodatage public des pièces libres (enregistrement figé sur OSF, sans résultat). * Recommandation : go, confiance 0,6. : go

Lecture de la mère, consignée au même registre (extrait sur B) : « **B (a)** : les **quatre collisions partielles tranchées en bloc** sur les recommandations — […] statistique de population du papier B resserrée (R-2181, lot 7-B) […] ; décisions à écrire, contre-lire et sceller dans `docs/decisions/` avant tout usage ».

Recommandations suivies : lot 5-A, § 3, formulation de « ce qui reste revendicable » ; lot 7-B, § 6.1, formulations pour la statistique de population et pour la statistique spatio-temporelle.

## 2. Énoncés d'origine, recopiés

`docs/programme-controle-ia-v2.md` (`2fd63bad…`, empreinte de lancement) :
- l. 43, thèse du papier B : « Des copies partagent leurs poids, donc leurs signatures internes co-varient : une statistique spatio-temporelle rend l'essaim plus détectable que l'agent isolé ; se décorréler coûte à l'attaquant de la capacité de coordination. »
- l. 62 (extrait) : « il faut un agrégateur d'**autocorrélation** (dans le temps) ou de **co-élévation** (entre agents) ».
- l. 72 (extrait) : « agrégateurs A_temps (somme cumulée, processus e), A_pop (co-élévation), A_spatio-temporel (les deux) ».
- l. 208 : « **Porte G2 (fin M4)** : effet de fragmentation répliqué et statistique de population supérieure à l'agrégation par agent. Sinon : recentrage sur le temporel N = 1. »
- l. 211 : « **E3.1** Statistique spatio-temporelle contre séquentiel par agent seul et contre coupe transversale (position NARCBench) — le cœur vierge. »

`docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (`c5465a9b…`), l. 392 : « **Reste revendicable** : la co-élévation d'états internes entre copies, lue par des sondes ; le pendant boîte blanche de la détection de collusion n'est pas vierge (NARCBench, cité par 2608.02698). »

`docs/decisions/decision-N-013-v1.md` (`157d388e…`), l. 90 : énoncés inchangés, dont « la statistique de population du papier B ».

## 3. Ce qui est pris, et par qui

Rapports : **5-A** = `docs/sources/lecture-pdf-niveau3/rapport-lot5A-sequentiel-multi-agents-v1.md` (`aef81e6e…`, 119 citations contrôlées, 0 échec) ; **7-B** = `docs/sources/lecture-pdf-niveau3/rapport-lot7B-collusion-papier-B-v1.md` (`bf9b6af8…`, 131 citations, 0 échec) ; tous deux sur la branche `prep/etat-de-l-art-niveau3-pieces-v1`. **C6** = `docs/etat-de-l-art/niveau3-v1/rapports/rapport-C6-H9-cemri-hammond-references-statistiques-v1.md` (`36d26d20…`, branche `prep/etat-de-l-art-niveau3-v1`). Déjà acquis : la **coupe transversale** sur activations est occupée par NARCBench (« HELIOS », 2604.01151 ; R-622).

| ce qui est pris | par (pièce, page) | accès | rapport |
|---|---|---|---|
| squelette statistique : un processus e par agent, garantie toujours valide (inégalité de Ville), combinaison entre agents par la procédure de Benjamini et Hochberg pour e-valeurs arrêtée à un temps commun, alarme plus précoce quand plusieurs processus montent ensemble | Gauthier, Bach, Jordan, 2601.05427 v3 (ICML 2026), p. 4, 5, 6, 31, 34-36 | boîte noire (gains d'un jeu, sans modèle de langue) | 5-A |
| statistique de population suivie dans le temps par carte de contrôle | Helm, Priebe, Duderstadt, 2605.11135 v2 (NeurIPS 2026), p. 2-4, 10, 18 | boîte noire déclarée (p. 2) | 5-A |
| score **de paire** sur les représentations internes de copies d'un même modèle, contraste « la paire contre le reste de la table », sans étiquettes, **cumulé sur les tours** (moyenne), dit « détecteur séquentiel » | Molinari, Bettineschi, « Multi-Agent Collusion and the J-Space » (J-PACT), 2611.02153 v1, p. 2, 3, 4, 6-9 | états internes lus par lentille jacobienne, **sans sonde** ; le modèle relit des transcriptions écrites par d'autres (p. 7, 9) | 7-B |
| statistique de **sous-groupe** sur **scores de sondes** par agent, taille de coalition inconnue (1 à 7), groupes de 3 à 8, seuil calibré à 1 % de fausses alarmes ; grille « temps (dernier tour, moyenne cumulée, somme cumulée de Page) × agents (pic, règle de NARCBench, deux balayages) », alarme en ligne à seuil conforme | Mohsin, Rahman, « What Do Collusion Probes Read? », 2611.10620 v1, p. 2, 4, 5, 11-12, 14, 21 | sondes sur activations (Qwen3-14B) | 7-B |
| agrégateur toujours valide de dépendance entre **deux** flux (outil), sous la condition qu'une seule marginale change à chaque pas | Podkopaev et collègues, 2212.07383 v4, p. 3, 7, 8, 9 | outil statistique général | C6, § 3.3 et § 5 |

**Ce que ces pièces ne font pas** (5-A, § 3 ; 7-B, § 1.3, 1.6, 2.3, 2.6) :
- **co-élévation de scores de sondes** de l'agent qui agit, entre copies : non trouvée (J-PACT n'a pas de sonde ; 2611.10620 mesure un contraste de niveaux, pas une montée conjointe) ;
- coalition de plus de deux à N variable avec un score relationnel ; sabotage diffus dans un travail réel ; adversaire **entraîné** contre le moniteur (2611.10620, p. 22-23 : agents seulement « told to evade ») ;
- **garantie toujours valide** sur une statistique conjointe temps × agents sur sondes ; **aucun résultat imprimé** pour la moyenne cumulée ni pour la somme cumulée de 2611.10620 (définies p. 11, absentes ensuite) ; horizon de quatre tours ; l'alarme retenue part au tour où la consigne arrive (p. 21) ;
- la **démonstration** qu'une statistique conjointe bat à la fois le séquentiel par agent et la coupe transversale à fausses alarmes égales.

**Qualificatif touché** : « le cœur vierge » (l. 211) ne tient plus (7-B, § 6.1) ; « lire ensemble les états internes de copies d'un même modèle pour détecter la collusion », en général, n'est plus revendicable.

## 4. Énoncés resserrés

1. **Statistique de population (A_pop), énoncé retenu** : « La **co-élévation de scores de sondes de l'agent qui agit**, entre copies d'un même modèle, (a) pour une coalition de taille inconnue, supérieure à deux ; (b) sur un sabotage diffus dans un travail réel (pipeline de code de l'environnement (b), programme v2, l. 123) ; (c) comparée **à sonde égale** au pic et à l'agrégation par agent, à fausses alarmes égales ; (d) avec les contrôles de construit de 2611.10620 (consigne reçue et refusée, consigne retirée, score lu avant l'issue). » (7-B, § 6.1.)
   - Ne sont **plus revendiqués** : un score de paire sur représentations internes (J-PACT) ; un balayage de sous-groupes sur scores de sondes (2611.10620) ; la lecture conjointe d'états internes de copies en général.
   - J-PACT, les deux balayages de 2611.10620, les cinq agrégations de NARCBench et l'écart entre agents (« Deception Split ») deviennent des **bases à battre** ; l'écart est une base obligatoire (R-2571, point 9c (c)).
   - Le mot « co-élévation » est gardé (R-2571, point 9c (c)) ; l'écart entre agents est un contre-indice à sa forme (section 7).
2. **Statistique spatio-temporelle (A_spatio-temporel, E3.1), énoncé retenu** : « Une statistique conjointe, entre agents et dans le temps, **sur les scores de sondes de copies d'un même modèle**, à **garantie toujours valide tenue sous dépendance**, sur horizon long, quand chaque action de chaque agent reste sous le seuil par action et face à un attaquant qui répartit son budget ; et la **démonstration** qu'elle bat le séquentiel par agent seul et la coupe transversale, à fausses alarmes égales, y compris sous un adversaire **entraîné contre elle**. » (5-A, § 3 ; 7-B, § 6.1.)
   - Le **squelette** est publié en boîte noire et se cite (2601.05427 ; 2605.11135) ; la **forme** de la grille temps × agents sur sondes est posée par 2611.10620 et le cumul d'un score entre agents sur les tours par J-PACT ; l'outil de dépendance entre deux flux est publié (2212.07383). Rien de cela ne se revendique.
   - E3.1 perd le qualificatif « le cœur vierge ».
   - « Entraîné contre elle » resserre la lettre du brouillon 2 (« sous adversaire ») : des adversaires plus faibles sont déjà publiés, agents prévenus puis priés d'évader (2611.10620, p. 22) et adaptation par le contexte seul (2609.03035 v2, p. 2) ; aucun n'est entraîné contre la statistique (7-B, § 0.1, § 2.3 ; contre-lecture de la synthèse finale, `f1580ddc…`, R-2567, constat M2).

## 5. Ce qui reste à mesurer

- Statistique de population : la co-élévation de scores de sondes, contre le pic, l'agrégation par agent, J-PACT et les balayages, sur le pipeline de code, à fausses alarmes égales, avec les contrôles de construit de 2611.10620.
- Statistique spatio-temporelle : la statistique conjointe à garantie toujours valide, contre le séquentiel par agent et la coupe transversale, sous un adversaire entraîné contre elle, sur horizon long, sabotage sous le seuil par action (E3.1). La condition de validité de 2212.07383 (une seule marginale change à chaque pas, p. 3, 8) est mise en défaut par un effet d'épisode commun à deux agents : limite à dire, non apport à annoncer sans mesure (C6, § 0, point 3).
- **Porte G2** (l. 208) : **décidé par Lazar (R-2571, point 9b (a))** : le pic par agent devient base nommée de la porte G2 et le cas « pas de gain » est prévu, dans son préenregistrement (recommandation du lot 7-B, § 6.2 ; contre-indice de 2611.10620, p. 14).

## 6. Citations obligatoires

Lues sur PDF ; empreintes vérifiées contre les compagnons le 13 novembre 2026. Branche `prep/etat-de-l-art-niveau3-pieces-v1`, dossier `docs/sources/pdf/niveau3-v1/`.

| pièce | référence | PDF | empreinte | pour |
|---|---|---|---|---|
| Gauthier, Bach, Jordan | « Anytime Detection of Strategic Deviations in Multi-Agent Systems », arXiv 2601.05427 v3, ICML 2026 imprimé | `lot5/2601.05427v3.pdf` (copie identique sous `lot3/`) | `e258cf0ade2a3801…` | squelette : processus e par agent, combinaison par e-valeurs à temps commun (p. 4-6) |
| Helm, Priebe, Duderstadt | « Control Charts for Multi-agent Systems », arXiv 2605.11135 v2, NeurIPS 2026 imprimé, version du 5 novembre 2026 | `lot5/2605.11135v2.pdf` | `1cc342dafb631dea…` | statistique de population suivie dans le temps, boîte noire (p. 2-4) ; théorème négatif voisin (p. 7-9, voir T) |
| Molinari, Bettineschi | « Multi-Agent Collusion and the J-Space » (J-PACT), arXiv 2611.02153 v1, 1er novembre 2026, prépublication | `lot7/2611.02153v1.pdf` | `65cc02df7485b253…` | score de paire sur états internes de copies, cumulé sur les tours (p. 2, 4, 6-8) |
| Mohsin, Rahman | « What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors », arXiv 2611.10620 v1, 7 novembre 2026 | `lot7/2611.10620v1.pdf` (copie identique sous `lot3/`) | `2aa2fd973d5693a2…` | balayages de sous-groupes sur sondes ; grille temps × agents ; contrôles de construit (p. 4, 11-12, 14, 15, 21-22) |

**À citer comme outil** (non dans la liste de la mère ; lu sur PDF par C6) : Podkopaev et collègues, test séquentiel d'indépendance à noyau, arXiv 2212.07383 v4, `lot5/2212.07383v4.pdf`, `a0a596319e1cc2ea…`, p. 3, 7, 8, 9.
**Déjà cité** : NARCBench (« HELIOS »), arXiv 2604.01151 v5, `docs/sources/pdf/2604.01151v5.pdf` (`main`), `02527fd4…` (R-622).

## 7. Prédictions touchées par un contre-indice publié

- **Porte G2, « statistique de population supérieure à l'agrégation par agent »** : sur le seul test publié à sonde égale, le **pic par agent** fait aussi bien ou mieux que les balayages — rappel à 1 % de fausses alarmes 0,86 pour le pic, 0,85 et 0,76 pour les deux balayages (2611.10620, tableau 3, p. 14) ; et « peak and ca-glr keep their recall for every coalition size from 2 to 7 (0.82–0.95) » (p. 21). Contre-indice direct pour le critère de G2.
- **Thèse du papier B (l. 43), « l'essaim plus détectable que l'agent isolé »** : J-PACT reste **sous** les sondes supervisées agrégées par agent (aire sous la courbe 0,921 contre 0,993 sur Core ; 2611.02153, p. 7) ; un score relationnel n'y bat pas l'agrégation par agent.
- **Forme « co-élévation » elle-même** : là où une règle relationnelle sur scores de sondes fait mieux que le pic (jeu à deux agents ; aire sous la courbe moyenne 0,87, 0,81 et 0,86 pour l'écart, contre 0,61, 0,61 et 0,58 pour le pic ; chiffres relevés sur le PDF par la contre-lecture, constat 69-1), le signal est un **écart** entre agents (« Deception Split », règle de NARCBench) : une asymétrie, non une montée conjointe (2609.03035 v2, p. 7, 9 ; `lot6/2609.03035v2.pdf`, `bccdbe1b2dd753f2…` ; 7-B, § 3.3) ; 2611.10620 mesure de même un contraste de niveaux (7-B, § 2.6). Indice favorable à une statistique relationnelle, contraire à la forme « montée conjointe ». Rappels de cette pièce non opposables (7-B, § 3.2). Le préenregistrement dit pourquoi une montée conjointe est attendue plutôt qu'un écart, et garde l'écart comme base obligatoire (R-2571, point 9c (c)).
- **Nombre d'agents** (relève de H3, non touchée ici) : la meilleure aire sous la courbe de la coupe transversale sur le transfert passe de 0,88 à 4 agents à 0,737 au mieux à 8 agents (HELIOS version 5, p. 27, 30 ; rapport C1).
- **Ce que lisent les sondes de collusion** : surtout la présence de la consigne, pas la décision (2611.10620, p. 1, 15 : aire sous la courbe de 1,00 à 0,61 quand la consigne est retirée) ; quatre traits de surface sans le modèle atteignent 0,883 (p. 16). Toute sonde du papier B relue sur NARCBench doit porter ces contrôles.
- **Coupe transversale sur activations, transfert** : rappel de 0,38 à 1 % de fausses alarmes sur le transfert (NARCBench « HELIOS », 2604.01151 v5, p. 18 ; rapports C1 et B3 ; R-622).
- **À 8 milliards de paramètres, sur NARCBench-Core** : une sonde par agent proche du hasard (aire sous la courbe 0,55 à 0,66) et un classifieur sur les mots de la consigne qui sépare les conditions (billet « What Happens When a Collusion Probe Only Finds a Thin Signal? », LessWrong, 26 juillet 2026 ; lot 2-B, § 5.3, `rapport-lot2B-billets-moniteurs-attaque-v1.md`, `8b4b5af1…`). **Billet archivé en texte, non un PDF** ; contre-indice faible, qui ne dit rien de la statistique de groupe ; à lire avant le devis de la ligne NARCBench de N-061.
- **Mise en commun entre agents, en boîte noire** : sur des portes dérobées réparties, un détecteur sur le flux réuni des agents tire tôt « mostly because the injected text makes an observation longer, not because it puts evidence together across agents » (2607.24893 v2, p. 8 ; `lot5/2607.24893v2.pdf`, `504d82ab525be78b…` ; 5-A, § 3 : « voisin (résultat négatif) »).
- **Accumulation** (voisin, papier A et B) : l'accumulation amplifie une marge présente, elle n'en crée pas (2606.20746, 5-A, § 0, point 1) ; signalé ici parce que E3.1 suppose un signal sous le seuil par action.
- **Chiffres non opposables** : les rappels de 2609.03035 (v1 contre v2, cartes de rappel remplacées sans explication ; 7-B, § 3.2) et l'essai « agents prévenus » de 2611.10620 (valeur de base 0,87 sans ligne correspondante ; 7-B, § 2.5) ne se citent pas comme faits.

## 8. Ce qui ne change pas

- R1 à R14 ; H3, H4′, H5, H7 et leurs énoncés retenus (N-013) ; T et L (N-003, N-004) ; le critère de la porte G2 tel qu'écrit (l. 208), complété par la base nommée et le cas « pas de gain » de R-2571 (point 9b (a)).
- E2.3 : les agrégateurs de NARCBench restent une base, non des concurrents (l. 207) ; J-PACT et les balayages de 2611.10620 s'y ajoutent.
- N-061 (NARCBench rejoué sur 8 milliards au bras descriptif de T0.7) : inchangée ; les contrôles de construit de 2611.10620 y sont pertinents (7-B, § 6.2), sans décision ici.
- Le programme v2, non modifié : cette note en fixe la lecture.
- R-2554 : l'article 2611.04556 reste cité comme publié pour la prémisse du papier B, sans changer d'énoncé.

## 9. Points attachés

- **Déclencheur de bascule** (programme, l. 239 : « Publication externe du cœur séquentiel sur sondes (équipe Oxford/NYU de NARCBench, équipe boîte blanche de l'institut britannique) → bascule vers l'épidémiologie de population et la curation de données »). Le lot 7-B (§ 0.2) constate qu'**aucun** des deux articles ne vient de ces équipes et qu'**aucun** ne publie un test séquentiel toujours valide sur sondes ; mais les deux rapportent que NARCBench nomme la détection séquentielle comme prochaine étape (2611.02153, p. 8 ; 2611.10620, p. 4), et 2611.10620 en réalise une forme faible. **Tranché par Lazar (R-2571, point 9a (a)) : bascule non déclenchée, veille rapprochée sur les suites de NARCBench** ; la veille sur les suites de NARCBench devient urgente. Les versions 1, 2 et 4 de NARCBench sont versées au lot 10, sans lecteur (R-2557) : leur lecture fait partie de cette veille.
- **Pistes citées et non lues** (7-B, § 6.2 ; questions, non trous) : NARCBench version 2 (2604.01151 v2, détection séquentielle annoncée) ; AcMAS (2607.06807) ; Tailor, « Audit the Whisper » (2510.04303, test séquentiel sur textes) ; Luikham (2609.00180) ; Kale et Vishwanath (2610.18408).
- **Usage hors du dépôt** : la contre-lecture de la synthèse finale (R-2567, `f1580ddc…`) range la statistique conjointe du papier B parmi les énoncés déclarables après correction, avec la date et les mentions « non trouvé dans les pièces lues » et « travaux qui citent 2606.08892, 2512.07810 et 2606.10456 non recherchés ; rien cherché du 10 au 13 novembre ».
- **H8** : rapprochée par 2611.10620 (p. 15, 19) ; hors de cette note.
- **Enregistrement public des pièces libres** (R-2555, option C) : la statistique du papier B y figure sous les énoncés de la section 4, sans « cœur vierge ».
