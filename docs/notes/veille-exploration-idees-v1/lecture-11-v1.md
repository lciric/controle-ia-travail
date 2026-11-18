# Lecture 11 sur source — « Beyond Symmetric Agents: Cognitive Diversity and Multi-Agent Debate in Small Language Models » (Leonardo Ferreira, Gardenia Liu, Kaden Zheng, arXiv 2609.35875) — v1

Écrite le 18 novembre 2026 (vers 06:30 UTC). Aucun commit, aucune dépense, aucun résultat sous embargo ouvert. Lecture entière sur PDF : pages 1 à 9 (texte), 10 (déclarations), 10 à 12 (bibliographie), 12 à 24 (annexes A à L, tables 3 à 19). Figures 1 et 2 regardées à basse résolution, figure 3 par sa légende. En plus : le paquet de sources TeX d'arXiv, **dont j'ai relu les tables par modèle par un programme à moi**, pour reconstruire un bras que le papier annonce et ne rapporte pas.

Revendication visée par la table de veille : 12 (diversité et composition des proposeurs ; proposeurs de plusieurs fournisseurs, valeur de la diversité). J'ajoute un mot sur la 9 (le témoin « un modèle, vote à k, coût apparié »), que le travail touche par sa méthode.

Tous les chiffres ci-dessous viennent du **PDF lu**, page citée, sauf ceux de la section 6 marqués « mon recalcul ». Aucun n'est opposable au-delà : le papier est une prépublication, sans données publiées.

## 0. Verdict en trois lignes

1. **Le travail ne mesure pas ce que la table de veille lui prêtait : ce n'est pas un troisième contre-indice propre à la diversité des fournisseurs.** Il ne compare jamais, à budget apparié, une équipe de modèles différents à un seul modèle. Il compare une équipe qui **échange** (trois rondes de débat) à la **même équipe qui n'échange pas** (tirages indépendants, vote majoritaire). Sur l'axe « identité du modèle », le témoin qui gagne est donc lui-même une équipe mixte. L'hypothèse rejetée est « la diversité explique le gain du débat sur le vote », pas « un effectif de plusieurs fournisseurs ne vaut rien ».
2. **Sur la valeur d'un effectif mixte, le papier affirme dans les deux sens sans bras qui le montre.** Contre : « teams do not benefit from spanning more model families once member strength is accounted for » (p. 7) — aucune table, aucune statistique. Pour : mettre en commun les votes de plusieurs petits modèles « beats the best single model substantially » (p. 7) — mais contre ce modèle répondant une seule fois, pas à budget apparié. Le bras qui trancherait (l'équipe mixte contre un seul modèle, à nombre de générations égal) est annoncé page 3 et n'est jamais rapporté. Je l'ai reconstruit sur les tables publiées (section 6) : le vote de l'équipe mixte se range **près du vote du meilleur modèle de son palier à lui seul, et au-dessus de la moyenne du palier**. Indication non appariée, à moi, non opposable — mais c'est la lecture qui ne nous arrange pas : à budget égal, l'effectif mixte ne bat pas son meilleur membre, il dispense de savoir lequel c'est.
3. **Ce qui mord vraiment est de méthode, pas de résultat** : le témoin à nombre de générations égal ne suffit pas (à générations égales, le débat coûte 3,4 fois plus de jetons au total, p. 5) ; deux artefacts silencieux handicapaient un seul bras et fabriquaient à eux seuls le signe du résultat (p. 8, p. 19-20) ; une diversité imposée par consigne (personas) coûte de la précision aux petits modèles, et la redondance coûte plus que la diversité (p. 5). Le terrain est loin du nôtre (réponses fermées, petits modèles ouverts, pas de production d'idées), et les auteurs le bornent eux-mêmes (p. 9).

## 1. Source versée

Dossier : `docs/sources/pdf/veille-exploration-idees-v1/lecture-11-arxiv-2609.35875/` (chaque pièce a son compagnon `.sha256`).

| Pièce | Empreinte SHA-256 |
|---|---|
| `arxiv-2609.35875v1.pdf` (24 pages, 476 093 octets) | `5fc206ae43477775feb62eec79ecd74346ae5c245ccb9e63769e1f1bb5aa2027` |
| `page-abs-arxiv-2609.35875.html` (page de résumé d'arXiv) | `b71a3b0416131f84ed1d5dc80ba127c7974d8eeafe697b8b722588a8a377eb6c` |
| `arxiv-2609.35875v1-source.tar.gz` (sources TeX d'arXiv, 444 507 octets) | `0d8f17f5a07db69bb341b5cd85fd024b67474e98771e4877b1e0ddd7f64f7ca2` |
| `adresse.txt` (adresses, dates, version, refus, jusqu'où lu) | `7d302e3ab1b9e6e0de3ef2b2b3a56919f4d679206c11f3edff671964697de07a` |

Programme de recalcul et sa sortie : `docs/notes/veille-exploration-idees-v1/programmes-lecture-11-v1/recalcul_tables_publiees.py` (`f3ced847e5cb14eef304494722933dd3a81b9dcae97f6c840a2991a558d471b3`) et `recalcul-tables-publiees-sortie-v1.txt` (`878c0155480fb63356e48ea583b680cee169239d1c87dc2e33107f747f56fa02`). Lancé avec `python3 -I`, lit l'archive en mémoire, ne l'extrait pas.

Récupération le 18 novembre 2026 entre 06:17 et 06:20 UTC, par `curl`, sans contournement. Refus noté et non insisté : l'interface `export.arxiv.org/api/query` (429). Documents traités en données : jamais exécutés. **Aucune consigne adressée au lecteur** relevée ; le PDF reproduit ses gabarits d'invite (p. 21) et ses 50 personas (p. 22-24), c'est l'objet étudié.

**Code et données : annoncés, introuvables.** Le papier écrit « We release the full budget-matched, contamination-checked grid » (p. 9) et décrit une « accompanying code release » avec des tables CSV (p. 10). Aucune adresse dans le PDF, ni sur la page de résumé (pas de fichier annexe), ni dans les sources TeX (aucune adresse, aucune ligne commentée) ; deux recherches web n'ont trouvé ni dépôt ni page de relecture publique. Aucun commit à noter. La revue de littérature dite jointe « as supplementary material » (p. 2) n'est pas sur arXiv.

## 2. Date de première version

- **arXiv : une seule version, v1, samedi 26 septembre 2026, 19:38:16 UTC**, déposée par Leonardo Ferreira (page de résumé versée). Fichiers des sources datés du même jour, 18:44 à 19:00. Commentaire de la notice : « Submitted to ICLR 2027 » ; l'en-tête du PDF dit « Preprint ». Non relu par des pairs à ce jour.
- **Aucun dépôt de code public trouvé** : pas de premier commit à dater.
- **Par rapport au programme** : antérieur d'un mois aux décisions sur la diversité et la composition (N-044 et N-045, 25 octobre 2026) et de sept semaines à N-067 (13 novembre 2026). Le programme ne revendique aucune priorité sur les proposeurs de plusieurs fournisseurs (énoncé rangé parmi ceux « à ne pas déclarer libres publiquement en l'état ») : il n'y a rien à perdre en date, seulement une valeur à mesurer.

## 3. Ce que le travail fait

Un débat entre agents à la manière de Du et al. (2023) : à la première ronde chaque agent répond seul ; aux rondes suivantes chacun lit les réponses entières des autres et garde ou révise la sienne ; à la fin, vote majoritaire (p. 2, p. 21). Les auteurs font varier la « diversité cognitive » sur trois axes (p. 3) :

- **Personas** : une consigne système « You are {persona}. » par agent, prise dans 50 personas dits « extrêmes » (« a Zen master who communicates only through non-sequiturs, koans », p. 23). L'équipe est choisie, pour chaque modèle, par recherche exhaustive du trio (ou quintette, septuor) qui maximise le déterminant de la matrice des similarités entre personas, calculée dans les représentations du modèle lui-même (p. 3). Puis une **échelle de dose à 11 barreaux**, du trio le plus redondant au plus divers (p. 5).
- **Température** : tirages tous à la même température, ou étalés entre 0,5 et 1,0 (p. 6).
- **Identité du modèle** : équipes de modèles différents. Le vivier est partagé en « classes de lignée » (fournisseur × génération) ; deux modèles de la même classe ne siègent pas ensemble ; les équipes sont stratifiées par palier de capacité (fort, moyen, faible, selon la précision d'un agent seul). 80 trios, 30 paires (un modèle doublé), 40 quatuors à cinq sièges (p. 3, table 2 p. 7).

**Le témoin, partout** : autant de générations, sans échange. Pour un débat de 3 agents sur 3 rondes, neuf tirages indépendants d'une seule ronde, vote majoritaire. Pour une équipe mixte, les mêmes modèles « in the same proportions » (p. 6).

**Modèles** : 23 modèles à poids ouverts de onze fournisseurs, de 0,6 à 32 milliards de paramètres denses, plus quelques modèles à mélange d'experts jusqu'à 109 milliards (p. 1, table 3 p. 12) ; les équipes mixtes sont tirées des 19 modèles présents au gel du tirage. **Aucun modèle de frontière.** Les auteurs en font un choix : un modèle de frontière près du plafond « leaves debate nothing to improve » (p. 1-2).

**Tâches** (p. 4) : 100 expressions d'arithmétique, 100 problèmes de GSM8K, 100 questions de MMLU, 100 de CommonsenseQA — notées par correspondance exacte ou extraction de la lettre, par programme — et la biographie de 40 informaticiens, notée affirmation par affirmation par trois modèles juges qui ne débattent pas. Tranches d'appoint : MMLU-Pro, GSM-Symbolic, GPQA Diamond (p. 19-20). **Aucune tâche de production d'idées, aucune tâche ouverte hors la biographie.**

**Volume** : 5 736 lancements de 100 problèmes selon la somme de la table 4 (p. 13 ; le texte dit « 5,500+ »), plus 2 720 passes de jugement. Une graine de tirage des problèmes (42) pour presque tout ; une seconde (43) pour les trios mixtes et une tranche du socle homogène.

## 4. Ce qui est mesuré, ce qui est seulement affirmé

**Mesuré** (chiffres lus sur le PDF) :

- **Le débat bat l'agent seul, pas le vote à générations égales.** Moyenne sur 23 modèles et quatre tâches notées par programme : agent seul 80,4 ; débat 84,4 ; vote de neuf tirages 84,8 (table 1, p. 5). Sur CommonsenseQA le vote l'emporte de 2,3 points (p = 0,011, p. 4). Je retrouve la table 1 à 0,05 point près à partir des tables par modèle (mon recalcul, section 1 de la sortie).
- **Le coût n'est pas apparié quand les générations le sont** : jetons produits dans un rapport de 1,06, mais jetons totaux 3,42 fois et temps 1,61 fois ceux du vote, parce que le débat relit à chaque ronde les réponses des autres (p. 5 ; table 18, p. 21).
- **Personas** : les équipes les plus diverses perdent de 2,1 à 4,4 points sur GSM8K et CommonsenseQA (p. 5). Sur l'échelle de dose, la plus grosse chute est à l'entrée, du débat sans persona au trio le plus redondant : −4,3 points (GSM8K), −4,2 (MMLU), −7,3 (CommonsenseQA) ; du barreau 0 au barreau 10, la précision est « flat to mildly increasing » (+2,9 points sur MMLU, p = 0,003) (p. 5). D'où leur mot : « a persona tax, not a diversity tax ».
- **Température étalée contre température unique**, en tirages indépendants : rien (−0,11 à −0,41 point, tous p ≥ 0,34, p. 6).
- **Équipes mixtes : le débat perd contre le vote de la même équipe.** Trios : −1,04 point, intervalle à 95 % [−1,61 ; −0,52], 80 équipes, 320 cellules équipe-tâche, débat gagnant dans 83 sur 320, médiane exactement nulle ; répliqué à la seconde graine (−0,93) (p. 6-7, table 2). Paires : −2,68 et −1,63. Quatuors : +0,04 et +0,56, nuls. Pondérer les votes par la précision de chaque membre creuse l'avance du vote (table 11, p. 16).
- **La précision d'une équipe suit le palier de ses membres** : de 93,7 (trois forts) à 75,6 (trois faibles), ordre monotone, pour le débat comme pour le vote (table 12, p. 17).
- **Presque tout le gain du débat vient du premier échange** : 84,6 à une ronde, 87,2 à deux, plat ensuite (table 13, p. 17 ; colonnes non appariées en budget, la légende le dit).
- **Deux artefacts de mesure**, chacun corrigé après coup : (a) les transcriptions du débat débordent la fenêtre de contexte servie, les agents rendent une réponse vide comptée fausse ; l'écart débat-moins-vote passe de −1,84 point tel que lancé à −0,06 après relance à fenêtre de 131 000 jetons (p. 8) ; (b) sur GPQA Diamond, huit modèles à raisonnement n'avaient reçu que 4 096 jetons de réflexion faute d'être reconnus par leur nom, ce qui handicapait le **témoin** ; l'avance du débat (+3,2 points, non significative) devient −0,6 [−2,2 ; +1,0] après relance (p. 19-20).

**Par qui c'est jugé** : quatre tâches par programme (correspondance exacte, extraction de la dernière réponse énoncée). La biographie par trois modèles juges (Gemma-3-27B, GPT-OSS-20B, GPT-OSS-120B), sans annotation humaine (« absent human claim-level annotation », p. 9) ; l'accord entre juges de fournisseurs différents est modéré (kappa de Cohen 0,32 à 0,57, contre 0,76 entre les deux juges du même fournisseur, p. 17), et la pénalité des personas n'est significative que sous un des trois juges (p. 7, p. 17).

**Seulement affirmé, ou appuyé sur un bras qui ne le montre pas** :

- « Teams do not benefit from spanning more model families once member strength is accounted for » (p. 7), repris au résumé (« accuracy tracking member capability rather than heterogeneity »). **Aucune table ne le teste.** Dans les trios, l'hétérogénéité ne varie pas : la règle impose trois classes de lignée différentes à chaque équipe (p. 3). La table 12 montre que la capacité compte ; elle ne peut pas montrer que l'hétérogénéité ne compte pas.
- « Pooling votes from several different small models beats the best single model substantially » (p. 7 ; recommandation pratique, p. 22 : « mixed rosters lift weak deployments 10–20 points over their best member »). Le comparateur est le meilleur membre **répondant une fois** (« their own best member's solo accuracy »), contre neuf générations pour l'équipe : pas à budget apparié. Le papier, si strict ailleurs sur ce point, ne l'est pas ici.
- Le bras « débats homogènes de même taille comme témoins internes aux équipes » est annoncé (« homogeneous debates at matching sizes serve as within-team controls », p. 3) et **n'apparaît dans aucune table**.
- L'explication de la taxe des personas (« adopting any assigned cognitive frame consumes representational resources small models need », p. 8) : hypothèse, appuyée par une corrélation avec la capacité (ρ de Spearman +0,46, p = 0,027, 23 modèles).
- La phrase de clôture sur la récurrence en profondeur (« keep the iteration, drop the transcript », p. 9) : opinion.
- La mise à disposition du code et des données : annoncée, non constatée.

## 5. Verdicts par revendication

| Revendication du programme | Verdict | Preuve (page, citation courte) |
|---|---|---|
| **12 (c) — proposeurs de plusieurs fournisseurs ; valeur de la diversité** | **voisin** (pas « contredit », contrairement à la table de veille) | § 5.3, p. 6 : « a three-model team debating three rounds versus an ensemble of nine single-round samples from the same models in the same proportions » — le témoin est une équipe mixte. P. 8 : « everything model diversity contributes […] is captured by voting over the mixed roster; the deliberation layered on top subtracts a little ». Le papier contredit la valeur de l'**échange** entre agents divers, pas celle d'un effectif de plusieurs fournisseurs ; et il ne produit pas d'idées. |
| **12 (a) — trois bras de diversité (mission, contrainte câblée, rien)** | **voisin** | § 5.2, p. 5 : « The performance penalty is paid at the door » ; « personas of any kind cost small models accuracy, and maximal diversity is the least harmful way to pay ». Une diversité imposée par consigne est mesurée, avec une échelle de dose, mais sur des réponses fermées et de petits modèles ; aucun bras « contrainte câblée », aucun juge comme seule pression. |
| **12 (b) — la composition est une variable apprise ; le coût entre dans le signal** | **voisin** (nommé comme travail à venir, non fait) | § 7, p. 9 : « Future work should learn team composition rather than fix it ». Toutes les équipes sont fixées d'avance par tirage stratifié. Pour le coût : p. 5, « 1.6× the wall-clock and 3.4× the total tokens (generated tokens match at 1.06×) » — rapporté à côté de la précision, jamais dans un signal d'apprentissage. |
| **9 (non visée) — le témoin « un modèle, vote à k, coût apparié » avant toute voie chère** | **voisin** (le principe du témoin est ancien et pratiqué ici à grande échelle ; rien de séquentiel d'une génération à l'autre n'est appris) | P. 3 : « every debate configuration is paired with a generation-budget-matched self-consistency control (Wang et al., 2023) ». P. 9 : « voting over independent samples converts the same generation budget into at least as much accuracy with no exchange at all ». |

Aucune zone du programme n'est trouvée occupée ; aucune n'est déclarée libre sur la foi de ce papier (R8).

## 6. Lecture dure de ce qui nous arrange

Ce qui nous arrange ici, c'est de conclure « ce contre-indice ne nous touche pas ». Je l'ai donc éprouvé de trois façons.

**(i) Le bras manquant, reconstruit — mon recalcul, pas un résultat du papier.** La question qui touche la revendication 12 (c) est : à nombre de générations égal, le vote d'une équipe de trois modèles différents fait-il mieux que le vote d'un seul modèle avec lui-même ? Le papier a les deux moitiés dans des tables séparées : le vote de neuf tirages de chaque modèle (tables 6 à 9, p. 14-15) et le vote des équipes mixtes par palier (table 12, p. 17). J'ai reconstruit les paliers par la règle de l'annexe I (p. 21 : moyenne de l'agent seul sur GSM8K, MMLU et CommonsenseQA ; fort au-dessus de 85, faible sous 60) sur les 19 modèles du vivier, puis moyenné sur les quatre tâches :

| Palier | Vote de 9 tirages d'un seul modèle : moyenne du palier | … meilleur modèle du palier | Vote de l'équipe de trois modèles différents du palier (table 12) |
|---|---|---|---|
| fort (8 modèles) | 91,0 | 93,5 | 93,2 |
| moyen (7 modèles) | 85,2 | 89,8 | 88,2 |
| faible (4 modèles) | 63,3 | 75,0 | 76,7 |

Lecture : l'équipe mixte vote **au-dessus de la moyenne de ses membres possibles** (+2,2 ; +3,0 ; +13,4 points) et **à peu près au niveau du meilleur** (−0,3 ; −1,6 ; +1,7). Autrement dit : à budget égal, l'effectif mixte ne bat pas son meilleur membre ; il rapporte à peu près ce que rapporterait de savoir d'avance qui est le meilleur. C'est cohérent avec les deux contre-indices que le dépôt cite déjà (un tirage au hasard, un a priori fixe) plutôt qu'avec une valeur propre de la diversité.

Réserves, lourdes : comparaison **non appariée** (mêmes 100 problèmes par tâche, mais moyennes de groupes différents) ; paliers **reconstruits par moi** — et douteux pour le palier faible, où la règle ne range que 4 modèles, soit 4 trios distincts, quand le papier dit huit équipes par composition ; valeurs par modèle arrondies à l'unité ; températures différentes entre les deux bras (écart borné à 0,4 point par le papier, p. 7) ; le gain sur la moyenne mêle la décorrélation des erreurs et le simple fait qu'un vote à trois écarte le membre le plus faible. **Non opposable** : une indication de sens, à refaire sur nos propres mondes plantés.

**(ii) Le terrain.** Tâches à réponse fermée ; le canal par lequel plusieurs fournisseurs aideraient un organisme d'idéation (couvrir des bassins d'idées différents) n'est pas mesuré. Les auteurs l'écrivent : « domains valuing novelty or synthesis may reward diversity differently » (p. 9). C'est une limite de leur papier, pas une preuve pour nous : rien ici ne dit que la diversité aide en production d'idées.

**(iii) Le haut de l'échelle.** Deux indices du papier vont dans notre sens, et je ne m'y appuie pas : les équipes de trois modèles forts sont la seule composition où le débat bat significativement le vote (+0,44 point, table 12, p. 17), et le plus gros modèle du vivier voit ses équipes à personas battre le témoin sur deux tâches — « one model is an anecdote, not a trend » (p. 9). Les auteurs laissent ouverte la question pour les grands modèles (« whether larger models can convert diversity into genuinely deliberative gains is the natural follow-up », p. 8). Nos proposeurs sont des modèles de frontière : **le papier ne parle pas d'eux**, dans un sens ni dans l'autre.

**Réserves sur le papier lui-même** (symétrie : elles valent quel que soit le signe) :

- **Aucun préenregistrement, aucune correction de comparaisons multiples**, sur plusieurs dizaines de tests rapportés avec leur valeur p.
- **Les deux corrections d'artefact ont été décidées après lecture des résultats**, et chacune déplace le résultat vers la nullité. Elles sont bien argumentées (réponses vides comptées, relance à fenêtre large), mais sans les données on ne peut pas vérifier que le même audit a été fait dans l'autre sens.
- **Température non appariée dans deux comparaisons** : débats à personas à température 1,0 contre débat de référence étalé de 0,5 à 1,0 ; débat mixte étalé contre ensemble à 1,0 (table 5, p. 13). Les auteurs bornent l'effet à 0,4 point, mais par une ablation en tirages indépendants (p. 6), pas en débat. La « taxe d'entrée » des personas inclut donc cet écart.
- **Incohérence interne d'environ un point** : la moyenne simple des dix compositions de la table 12 donne 87,45 (débat) et 88,56 (vote), contre 88,4 et 89,4 à la ligne « trios » de la table 2, alors que chaque composition est dite compter huit équipes (mon calcul, section 4 de la sortie). L'écart débat-moins-vote, lui, bouge peu (−1,12 contre −1,04).
- **« Diversité de modèles » n'est pas « diversité de fournisseurs »** : la classe de lignée est fournisseur × génération (p. 3), donc une équipe « mixte » peut réunir deux générations du même fournisseur (le vivier compte trois Qwen3 et deux Qwen3.5 ; table 3, p. 12). Le papier ne rapporte rien par nombre de fournisseurs distincts.
- **Une graine, 100 problèmes par cellule** (40 sujets en biographie) ; les auteurs notent que la significativité par tâche bouge d'une graine à l'autre (p. 9).
- **Biographie** : la marge du témoin (64,6 contre 55,6, table 1) tient en partie à la mécanique de mise en commun des affirmations de neuf biographies, de l'aveu des auteurs (p. 17) ; juges modèles seuls.
- **Usage déclaré d'un agent** : un agent Claude a relu le code d'analyse et orchestré les campagnes, sous direction humaine (p. 10). Sans effet connu sur les chiffres ; à savoir.

## 7. Idée à prendre pour nos travaux

**Deux témoins et une garde pour le duel des proposeurs, tous à vérité plantée** (proposition ; rien n'est décidé ici, la décision revient à Lazar) :

1. **« Même effectif, sans échange »** : dès qu'une composition laisse des proposeurs lire les fiches des autres, rejouer le même effectif en tirages indépendants, au même nombre de générations, et lire les deux sur l'oracle du monde planté (structures retrouvées, témoins vrais promus, faux rejetés). C'est le témoin qui, chez Ferreira et al., absorbe tout le gain.
2. **« Le meilleur fournisseur seul, à k tirages »** : c'est le bras que ce papier annonce et ne rapporte pas, et le seul qui dise si plusieurs fournisseurs valent plus que le meilleur d'entre eux. Il complète les bras « hasard » et « a priori sans modèle » déjà proposés après N-067, et se confond en pratique avec le témoin « un modèle, vote à k, coût apparié » de N-045 v2 — à condition de le lancer **pour chaque fournisseur**, pas pour un seul choisi d'avance.
3. **Une garde de troncature par bras** (dans l'esprit de R5) : avant toute lecture d'une comparaison entre compositions, compter par bras les réponses vides ou tronquées (fenêtre de contexte, budget de réflexion) et refuser la lecture si les taux diffèrent ; compter le coût en **jetons totaux, lus et produits**, puisque des générations appariées ne donnent pas un coût apparié (3,4 fois, p. 5). Chez eux, ces deux artefacts faisaient à eux seuls le signe du résultat.

À citer, quand la diversité des proposeurs est discutée : ce papier comme voisin (méthode du témoin apparié, taxe des personas), avec sa borne de terrain. Pistes en sens contraire qu'il cite et que je n'ai pas lues : Zhang et al. 2025 (arXiv 2502.08788, « embrace model heterogeneity ») et Chen, Saha, Bansal 2023 (ReConcile, arXiv 2309.13007), donnés comme les résultats les plus régulièrement favorables à l'hétérogénéité des modèles (p. 2) ; et Choi, Zhu, Li 2025 (arXiv 2508.17536), le débat comme martingale sur la distribution des réponses initiales. Absents des notes du dépôt.

## 8. Limites de cette lecture

- Le papier n'a ni code ni données publics : aucun chiffre n'a pu être recalculé depuis des journaux, seulement la cohérence entre tables (table 1 retrouvée ; tables 2 et 12 non raccordées).
- Mon bras reconstruit (section 6) repose sur des paliers que j'ai déduits, et n'est pas apparié.
- Figure 3 non regardée ; figures 1 et 2 à basse résolution (à l'œil, les valeurs du barreau 10 de la figure 2 concordent avec les écarts « personas moins débat » de la table 1).
- Je n'ai pas lu les travaux cités par le papier ; je n'ai pas cherché de version antérieure hors d'arXiv au-delà de deux recherches web.
- Le dépôt du programme n'a été consulté que pour l'énoncé des revendications (N-044, N-045 v2, N-067, § 7) ; aucun résultat sous embargo ouvert.
