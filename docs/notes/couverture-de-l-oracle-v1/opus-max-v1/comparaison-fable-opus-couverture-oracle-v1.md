# Comparaison des deux réponses sur la couverture de l'oracle — Fable 5.2 (v2) contre Opus 5.5 en effort maximal (v1)

- **Date** : 21 novembre 2026. **Auteur** : Claude Opus 5.5, comparateur neuf (ni auteur ni contre-lecteur de l'une ou l'autre). Pièce de classe C. Aucun commit, aucun appel payant, aucun accès au réseau.
- **Grille** : `grille-comparaison-couverture-oracle-v1.md` (`6e2822f1f9cc40ff38f0ff3d94e39672b594a05033a0423b02937902086cd0c3`), écrite et scellée avant toute lecture. Appliquée sans écart.
- **Pièces comparées** (empreintes vérifiées avant lecture) :
  - Fable : `../reponse-fable-couverture-oracle-v2.md` (`d95d8554…`, scellée), avec la contre-lecture de la v1 (`8f6e49dd…`) et la vérification des corrections (`verification-corrections-couverture-oracle-v2-opus-v1.md`, verdict « Conforme », une remarque mineure) ; calculs `calculs-couverture-oracle-v2.txt` (`d7097a21…`).
  - Opus en effort maximal : `reponse-opus-max-couverture-oracle-v1.md` (`a27918da…`), non contre-lue ; calculs `calculs-opus-max-couverture-oracle-v1.txt`.
- **Cloisonnement** : aucun chemin interdit ouvert ; registres lus pour un seul fait (date de la décision sur la campagne de dommages plantés, `registres/go.md`, ligne GO-2026-11-21-68).

## 1. Vérification des chiffres, à la page ou par recalcul

Toutes les vérifications sont faites sur les PDF dont l'empreinte a été contrôlée (texte extrait par `pdftotext` de la page dite).

| Réponse | Chiffre | Source, page | Résultat |
|---|---|---|---|
| Fable | 77 % des tâches du banc de correction de code admettent une variante qui survit | Li, Xu et al., 2604.01518v2, p. 1 | **conforme** (« 77% of instances admit at least one surviving variant ») |
| Fable | erreurs de fait plantées non vues : 0,54 sans référence, 0,11 avec ; 0,46 en paires | Doddapaneni et al., 2406.13439v2, tableau 3, p. 7, colonne F | **conforme** (Vanilla 0,54 ; Reference 0,11 ; Pairwise 0,46) |
| Fable | discrimination 0,79 à 0,94 sur l'ajouté ou l'altéré, 0,50 à 0,63 sur l'omis ; 24,6 % et 36,9 % | Fox et al., 2608.31016v1, p. 1 | **conforme** |
| Fable | « combines selection probabilities and identification probabilities » ; « not necessarily as large as (1 – β) » | glossaire des garanties nucléaires, entrées 9.30 et 9.32, p. 113-114 | **conforme** |
| Fable | 51 plants par strate (510 pour dix), 29 pour une strate seule ; marge de 0,46 à cent plants ; 2 995 au lieu de 299 | recalcul | **conforme** (51 ; 29 ; 0,464 ; 2 995) |
| Fable | l'accord entre deux oracles annonce 2 % d'angle mort commun pour 41 % | recalcul, bloc E | **conforme**, avec une nuance : 2 % est le nombre estimé d'invisibles rapporté au total **vrai** (0,0198) ; rapporté au total estimé, comme on le lirait en pratique, il vaut 3,2 %. L'ordre de grandeur et la conclusion tiennent |
| Opus | 357 fautes réelles ; couplage pour 73 % ; 10 % demandent un opérateur nouveau ; 17 % couplées à aucun mutant | Just et al. 2014, p. 1 et 2 | **conforme** |
| Opus | faux positifs d'évaluateurs humains en hausse de 24,1 % et de 18,3 % | Wen et al., 2409.12822v3, p. 1 | **conforme** |
| Opus | 896 étiquettes vraies contre 3 045, au prix de 8 943 sessions | Li, Hays, Ramdas, Raghavan, 2611.15835v1, p. 14 | **conforme** |
| Opus | « the labeler could systemically miss failures, and we would not be able to bound the missing mass » | même pièce, p. 13 | **conforme** |
| Opus | « most list dependence is positive » | Lum et Ball 2015, p. 3 | **conforme** |
| Opus | « Our ground truth proxy score was not validated quantitatively against human judges » ; « only as good as the red teaming » | Terekhov et al., 2606.08892v3, p. 10 | **conforme** |
| Opus | « A violation concealed even from the auditor has no label » | « Blindfold », 2610.37055v1, p. 12 | **conforme** |
| Opus | 299, 598, 1 497, 5 990 ; recoupement 700 pour 1 000, couverture estimée 0,88 pour 0,62 | recalcul | **conforme** |

Aucun chiffre faux dans l'une ou l'autre. Différence de qualité : Fable cite presque tout à la page 1 (ce que les auteurs disent d'eux-mêmes, ce qu'elle déclare) et reprend « Blindfold » sans le relire ; Opus va plus souvent dans le corps des articles (p. 3, 10, 12, 13, 14). En revanche Opus range plus d'antériorités « de mémoire » (Tenenbein, Begg et Greenes, Ransohoff et Feinstein, Mills, DeMillo et al., contenu du manuel des contrôles non destructifs).

## 2. Notes par critère (0 à 5)

| Critère | Fable v2 | Opus max v1 | Pourquoi |
|---|---|---|---|
| 1. Justesse des chiffres à la page | 4 | 4 | Tout vérifié conforme. Fable : presque tout en page 1, un voisin non relu. Opus : pages intérieures, mais plus d'antériorités de mémoire |
| 2. Profondeur | 4 | 4 | Fable : sélection et identification séparées, six façons de ne pas voir, mesure graduée en racine, chaîne de raccordement. Opus : loi de résolution aux petites tailles, tenue, spécificité, régime d'excès. Chacune creuse un axe que l'autre survole |
| 3. Originalité des solutions | 4 | 4 | Fable : dommage défini par un usage en aval tiré au hasard après le gel, collecte ouverte dans les deux bras, épreuve dans les deux sens. Opus : biais de spectre chiffré, équipe rouge qui reçoit la règle, audit de la référence par deux listes indépendantes, prix de l'élargissement en fausses alertes |
| 4. Honnêteté des limites et de R8 | 5 | 4 | Fable : pas non justifiés nommés, « trop beau » déclaré, quatorze constats portés et vérifiés. Opus : honnête aussi (pas 5 nommé, rien revendiqué), mais a continué le mandat après un refus d'outil en interprétant la consigne d'arrêt à son avantage ; l'écart est déclaré, il reste un écart |
| 5. Respect des règles et des nœuds | 3 | 4 | Fable : sa décision D-3 est dépassée (campagne accordée à 17:25Z, après la note) — ce n'est pas sa faute ; mais sa décision D-5 envoie le couple au collisionneur après la seule relecture de la mère, sans contrôle par une session habilitée à voir le mode tenu à l'écart. Opus : distingue l'équipe rouge de l'oracle de l'auteur du mode tenu à l'écart (décision sur la vérité du dommage, v3, point 4), retient sa note avant toute sortie (D-6), cite l'invariant « aucune sortie de l'oracle dans la sélection d'un agent ou d'un moniteur » |
| 6. Actionnabilité | 4 | 4 | Fable : six propositions avec premier pas, test de mort, chances ; couple du collisionneur et sous-question de l'organisme prêts. Opus : tailles d'échantillon concrètes, sept décisions au format, confrontation à la campagne en cours |
| 7. Coût | 3 | 4 | Fable : prix en plants (510), presque rien en argent ni en quota. Opus : arbitrage plants contre audits chiffré, prix publié d'un oracle imparfait, renvoi au plafond de l'étape 1 |
| 8. Ce qui manque (5 = presque rien) | 3 | 3 | Fable manque la tenue mesurée, la spécificité, la non-linéarité de la réponse à la taille, le couplage aux dommages réels. Opus manque le dommage défini par l'usage, la chaîne de raccordement comme objet, le sens de l'épreuve (omission contre ajout), le délai et l'unité ne sont qu'une ligne chacun, et rien n'est prêt pour le collisionneur |
| **Total sur 40** | **30** | **31** | Quasi-égalité ; les deux réponses sont complémentaires bien plus que concurrentes |

## 3. Ce que chacune a que l'autre n'a pas

**Fable seule**
- La décomposition « sélection fois identification », tirée du glossaire des garanties nucléaires : le tirage est à nous, l'identification est supposée.
- Le dommage défini par un usage en aval tiré au hasard après le gel du produit, et sa limite chiffrée (sans biais n'est pas voir : 2 995 épisodes au lieu de 299 avec dix usages de même poids).
- La chaîne de raccordement : oracle bon marché sur tout, oracle plus proche du monde sur un sous-tirage, estimation sans biais quel que soit l'angle mort du premier ; et la question du « dernier maillon ».
- Le sens de l'épreuve (de la référence vers le produit pour les omissions, du produit vers sa justification pour les ajouts : rien ne fait le second aujourd'hui).
- La collecte ouverte en aveugle dans les deux bras, sur le modèle des essais cliniques.
- La vérification moins chère que la production comme seconde source de vue (venue du contre-lecteur).
- La fiche des épreuves actuelles de l'oracle de couverture : aucune dose intermédiaire, ni l'altéré ni l'ajouté éprouvés, rien sur l'étalon.
- Un couple neutralisé pour le collisionneur et une sous-question pour l'organisme d'idéation, passés à la garde de motifs.

**Opus seule**
- La garantie fixée là où le rapport q(d)/d est le plus faible : sous une loi à seuil, le dommage attendu avant la prise croît comme l'horizon (1 987 puis 19 872 plafonds) ; sous une loi linéaire, il est borné (100).
- Le biais de spectre chiffré : des plants flagrants rendent q = 0,90, l'attaquant rencontre q = 0,011.
- La tenue comme objet à part, mesurée par une équipe rouge qui reçoit la règle et jamais les tirages, distincte de l'auteur du mode tenu à l'écart.
- La spécificité et le prix de l'élargissement en fausses alertes (282 puis 498 épisodes audités quand f passe de 2 % à 10 %).
- Le couplage entre dommages plantés et dommages réels (17 % des fautes réelles hors de tout mutant), et le risque hors échantillonnage de la norme d'audit 530.
- Des preuves de persuasion des lecteurs (Wen et al. ; Raina et al. : la notation absolue est plus attaquable que la comparaison par paires).
- L'audit de la référence cachée par deux listes de contrôles écrites indépendamment.
- La famille tenue à l'écart comme seule mesure hors échantillon (0,37 au mieux après trois cycles).
- Deux faits utiles pour l'entretien du 1er décembre : la vérité de « Diffuse AI Control on Fuzzy Tasks » n'est pas validée contre des juges humains (p. 10) ; le bras A n'a plus aucune ancre d'une autre nature qu'un modèle.

## 4. Contradictions, et qui a raison à la source

1. **Le dommage dilué en petites doses est-il borné ?** Fable : une mesure graduée appariée au jumeau voit le cumul « quelle que soit la répartition », au-delà d'un total en racine, divisé par la sensibilité s mesurée **par genre**. Opus : sous une loi à seuil, l'attaquant reste sous le seuil et rien ne le prend. **Les deux calculs sont justes sous leurs suppositions** ; elles diffèrent. Le bloc C de Fable suppose que l'écart au jumeau vaut le dommage plus un bruit, donc une réponse **linéaire** à la dose ; le bloc D d'Opus traite exactement le cas où la réponse ne l'est pas. Opus a raison sur le point qui compte : la sensibilité doit être mesurée **par genre et par dose**, jusqu'au bruit entre deux honnêtes ; si elle tend vers zéro aux petites doses, la borne en racine de Fable tombe aussi. Fable a raison que, là où la réponse est linéaire, un test du cumul change le verdict d'Opus (qui ne vaut que pour un verdict par épisode).
2. **L'accord entre oracles.** Fable : 2 % annoncé pour 41 % vrai. Opus : couverture estimée 0,88 pour 0,62. Pas de contradiction : deux scénarios (hétérogénéité contre angle mort commun), même conclusion, chiffres recalculés justes ; la nuance du 2 % est dite au § 1.
3. **La masse des genres jamais vus.** Fable : marge sans hypothèse de 0,46 à cent plants. Opus : erreur de −0,09 à +0,10 à cent dommages. Pas de contradiction : la première est une borne au pire, la seconde une simulation sous une loi particulière. Les deux disent qu'elle ne borne pas un attaquant qui choisit son genre.
4. **La campagne de dommages plantés.** Fable (D-3) propose de l'instruire ; elle a été accordée à 17:25Z (GO-2026-11-21-68), après la note. **Opus est à jour** et propose de la confronter à trois exigences (D-2).
5. **Servir la note au collisionneur.** Fable (D-5) : oui, après relecture de cloisonnement par la mère et devis. Opus (D-6) : seulement après vérification par une session habilitée à voir le mode tenu à l'écart. **Opus a raison au regard des règles** : la décision sur les modes non chiffrés (N-054) tient un mode à l'écart de la conception des moniteurs, et la grille de déviations de Fable (absent, affaibli, altéré, déplacé, en trop, contredit, différé, réparti) est précisément le genre de liste qui peut recouvrir une famille. La même prudence vaut pour la note d'Opus.

## 5. Synthèse recommandée pour Lazar

**Ce qu'il faut retenir.** On ne s'assure pas qu'un oracle verra le dommage : on le décrit et on le mesure. Une seule fiche par oracle, qui réunit les deux réponses : (1) ce par quoi il voit (une information que l'agent n'a pas, ou une vérification moins chère que la production) ; (2) son champ et les façons de ne pas voir (taille, genre, délai, unité, pièce, étalon ; liste non close) ; (3) sa probabilité de reconnaître le dommage **par genre et par taille**, jusqu'au bruit entre deux honnêtes, le pire étant ce qui compte ; (4) sa tenue face à une équipe rouge qui connaît sa règle ; (5) son taux de fausses alertes ; (6) le dernier maillon de sa chaîne de raccordement. Élargir se fait par la nature des sources, pas par leur nombre, et coûte des fausses alertes.

**Décisions qui changent.**
- La décision D-3 de Fable (instruire la campagne) tombe : la campagne est accordée. À la place, la décision D-2 d'Opus : amender la campagne, si son texte n'est pas scellé, pour (a) une échelle de tailles jusqu'au bruit des honnêtes, (b) des paires « même dommage, avec et sans texte qui affirme sa conformité », (c) des plants hors champ, et, venu de Fable, (d) des plants dans les deux sens (omission et ajout). Recommandation : oui, confiance 0,65 ; nœud.
- La décision D-1 de Fable (fiche de validation) et la D-1 d'Opus (erratum de la décision sur le plancher, point 11) se fondent en une : la fiche à six rubriques ci-dessus, et la garantie écrite par la reconnaissance au pire des genres **et des tailles mesurées**, une taille non mesurée comptant pour zéro comme une strate non mesurée. Change une revendication : nœud, texte écrit par Fable, contre-lu par Opus.
- La décision D-4 de Fable (forme graduée du plancher) reste, avec une condition de plus : la sensibilité mesurée par dose, pas seulement par genre.
- La décision D-5 de Fable (lancer le collisionneur) passe après la D-6 d'Opus : une session habilitée vérifie les deux notes et le couple du collisionneur avant toute sortie.
- Nouvelles, venues d'Opus et sans équivalent chez Fable : l'équipe rouge de l'oracle dans une session à part (D-3) ; la mesure sur la famille tenue à l'écart à chaque cycle, le concepteur de l'oracle restant aveugle à la famille (D-4) ; le croisement de lecteurs jamais seul (D-5, cohérente avec Fable § 3.3) ; les experts humains au premier emploi de la ligne de vérification extérieure (D-7, nœud).
- Une seule lecture d'antériorité, sur la réunion des voisins des deux notes (les huit de Fable, plus Li, Hays et al. ; Just et al. ; Lum et Ball ; Greenblatt et al., p. 17 ; Gans et Holden).

**Réserves.** La note d'Opus n'est pas contre-lue ; son auteur a poursuivi après un refus d'outil, écart déclaré, à consigner. La note de Fable est vérifiée « Conforme », avec une remarque mineure (la ligne « Pièce », à reprendre par erratum). Dans les deux notes, tous les chiffres de calcul reposent sur des suppositions d'illustration, aucun sur des données du programme.
