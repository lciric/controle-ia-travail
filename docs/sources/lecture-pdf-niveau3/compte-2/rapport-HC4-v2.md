# Rapport du lecteur — HC4, « taxe de déplacement », sur quatre pièces du lot 11 (v2)

- **Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B.**
- **Rapport remplacé** : `rapport-HC4-v1.md`, `dceefa6a0c4bb9c921604cd3eec98ab7fa6270115b23bc07ed6a70521fa5886c` ; son archive : `fichiers-de-travail-HC4-v1.tar`, `d5c79196bcea9616c812b4057e1c9e98479bbbdd49e0f6bde7d8ee45284d4c1b`. Ces deux fichiers restent intacts (R12).
- **Contre-lecture intégrée** : `contre-lecture-rapport-HC4-v1.md`, `8fa4ab9baf757af42f44255b484c3b0ca865fc8b887c6c01bf4755473847e5b0` ; son archive : `fichiers-de-travail-contre-lecture-HC4-v1.tar`, `e7466a1f53ce016337caef2c2b6dfce0b037ae3f68586116925cdb9815ff75e2`. Les deux empreintes ont été vérifiées le 2026-11-13 à 23:47:20 UTC (`date -u`), et l'archive a été extraite dans un sous-dossier neuf de mon dossier de travail. La contre-lecture rend « tient avec corrections » : cinq constats majeurs (A à E), huit mineurs (F à M), aucun bloquant.
- **Heures** (`date -u`) :
  - version 1 : lecture le 2026-11-13 de 23:21:26 à 23:33 UTC ;
  - version 2 : reprise à 23:47:20 UTC ; relectures ligne à ligne de 23:47:40 à 23:49 UTC ; rédaction commencée à 23:49:24 UTC.

  L'heure de fin est celle du scellement (fichier compagnon `.sha256`).
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme). Tous ses interdits ont été tenus : aucune commande git, aucun réseau, aucun appel de modèle, aucun refus, aucune ouverture fautive.
- **Fichiers du dépôt lus, et seulement aux lignes du mandat** :
  - `docs/programme-controle-ia-v2.md`, l. 85-125 et 190-215. Relu en v2 : l. 101-106 et 193-195 ;
  - `docs/decisions/decision-N-013-v1.md`, l. 46-55 ;
  - `docs/decisions/decision-N-068-v1.md`, l. 1-115 ;
  - `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, l. 279-292 ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, l. 412-431. Relu en v2 : l. 417-422 ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, l. 509-535 et 696-726 ;
  - en v2, en plus : la contre-lecture et son archive, nommées ci-dessus.

  Aucun autre fichier n'a été ouvert, et en particulier aucun rapport d'un autre lecteur.
- **Pièces**. Chaque empreinte a été vérifiée contre son compagnon `.sha256`, avant la lecture puis après un redémarrage du conteneur. Les quatre sont conformes.

| pièce | empreinte sha256 | pages | étendue lue |
|---|---|---|---|
| `2601.04603v1.pdf` | `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` | 17 | p. 1-17 ligne à ligne. **En v2, relues ligne à ligne : p. 2-9.** Figures 2, 3 (p. 7-8), 4 (p. 14) et 5 (p. 16) lues sur l'image. |
| `2309.10253v4.pdf` | `f2b76387acd042a27db07e8093dc4f4f4b876eb28d6a16fcf886432b31f1ffac` | 26 | p. 1-26 ligne à ligne ; figures 5, 8 et 9 lues sur l'image |
| `2310.08419v4.pdf` | `590bf40aa58061928f54d01b7d53f0d5141bb2ecf4f01483c6849423934f44e4` | 34 | p. 1-34 ligne à ligne ; captures des p. 27-33 lues sur l'image. **En v2, relues ligne à ligne : p. 4-6 et 15.** |
| `2502.19537v5.pdf` | `4f991dbe01b2c853189b45e1b36906bf355a367550f96703cf320b6e9f291d3c` | 37 | p. 1-37 ligne à ligne. **En v2, relues ligne à ligne : p. 7-8.** |

- **Citations contrôlées par programme** : **137, 0 échec** (`citations-HC4-v2.json`, dans l'archive seulement). Ce sont les 79 citations de la v1, toutes reprises, plus 58 ajouts. Le script `verifier_citations_v1.py`, lancé par `python3 -I`, cherche chaque citation dans la page, avec et sans `-layout`, après normalisation. Il a d'abord été essayé sur un cas juste et sur trois cas altérés.
- **Contrôle des guillemets du rapport.** Un second script, `controler_guillemets_rapport_v2.py`, extrait chaque passage entre guillemets français de ce rapport et le cherche dans le JSON. Résultat attendu et obtenu : tout extrait anglais y figure. Les seuls passages absents du JSON sont en français (citations du programme, des décisions, de la contre-lecture, ou mots du verdict). Le relevé est dans l'archive : 98 passages trouvés dans le JSON, 46 passages absents, tous en français, vérifiés un à un.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi). Les noms de modèles qui apparaissent sont ceux des articles.

---

## 0. Verdict selon le sens de « juge »

Le sens de « juge » revient à Lazar. Je ne le tranche pas ; je donne le verdict sous chaque sens.

| sens de « juge » | verdict sur HC4 (table fermée) | ce qui le porte |
|---|---|---|
| **juge génératif** : le moniteur que la rhétorique déplace, celui de HC1 et de EC.1 | **« non trouvé dans les pièces lues »** | Aucune des quatre pièces n'attaque un juge génératif en tant que moniteur, ni ne mesure le coût de son déplacement. 2601.04603 est un voisin très proche et un contre-indice indirect, hors du périmètre restreint par N-068. |
| **tout modèle qui lit le texte**, classifieur affiné compris | **« occupé en partie »** | 2601.04603, p. 7-9 : une sonde et deux classifieurs affinés, rejoués sur les mêmes échanges d'attaque, à calibration égale. La comparaison ne porte que sur l'axe « taux de succès », en boîte noire, par transfert statique, pour une sonde de contenu nuisible. Le coût n'y est pas comparé, ni pour la sonde ni pour les classifieurs. |

**Sous les deux sens**, une chose n'est pas trouvée dans les quatre pièces : la comparaison du **coût** d'attaque (requêtes, jetons, calcul, temps, exemples de réglage fin) entre une sonde et un juge. Il manquerait pour cela :
- un cadre commun, avec une décomposition par régime d'accès ;
- une attaque qui s'adapte ;
- une sonde qui lit l'intention ou l'action de l'agent auteur, à taux de faux positifs fixé (N-068, point 8a).

HC4 est par ailleurs une zone peu cherchée (M14). Ce verdict ne vaut donc pas « trou du champ ».

**La lecture que les textes rendent la plus naturelle est « juge génératif ».**
- Programme v2, l. 106 (HC4) : « le déplacement que la rhétorique obtient gratuitement sur un juge ». Le juge y est défini par renvoi : c'est l'objet que la rhétorique déplace.
- Même programme, l. 102 (HC1) : « g stable par moniteur génératif » ; l. 105 (HC3) : « déplacent les juges génératifs » ; l. 194 (EC.1) : « g des juges génératifs ».
- N-013, l. 48, reprend la même tournure. N-068, section 4, compare la sonde « au g des juges génératifs sous les mêmes attaques ».

Deux éléments plaident pour la lecture large :
- le mandat glose le mot en « modèle qui lit du texte » ;
- l'état de l'art de niveau 3 (l. 420-421) range déjà « des classifieurs durcis » du côté du juge pour contester le mot « gratuitement ».

En v1, j'avais annoncé « occupé en partie » en tête, sous la lecture large. Ce choix ne décide plus du verdict (constat D).

---

## 1. Suite donnée à la contre-lecture

Pour chaque constat, j'ai relu les pages en cause avant de décider. Les citations sont toutes dans le JSON v2.

| constat | gravité | décision | où | motif |
|---|---|---|---|---|
| A — citation inexacte (ligne A3 du tableau de 2601.04603) | majeur | corrigé | section 2, point A3 | La v1 tronquait le début de la phrase entre guillemets. Le PDF imprime, p. 5, note 3 : « though this required substantial effort and automated tools ». La phrase complète est dans le JSON (p. 5). La page donnée en v1 (5) était juste ; c'est l'extrait qui était tronqué. Un contrôle des guillemets du rapport par programme est ajouté (en-tête). |
| B — coût déduit d'un taux de succès statique | majeur | corrigé | sections 0, 2 (composante (e)), 7, 8 | Relu p. 7 : jeu figé, « comprising approximately 7,000 exchanges designed to elicit harmful CBRN-related », sans attaquant qui interroge la sonde. Aucun coût d'évasion n'y est mesuré. La phrase de la v1 (« la sonde ne coûte pas plus cher à évader ») dépassait la pièce : elle est retirée. Le point devient un contre-indice indirect, hors du périmètre restreint par N-068. |
| C — origine des attaques et position de la sonde non établies | majeur | corrigé | section 2, « Ce que l'article fait » et limites | Relu. La sonde est entraînée sur un modèle (« We train a linear probe on top of a Claude Sonnet 4 using concatenated activations across all layers. », p. 7) qu'aucune campagne décrite ne protège : « We use this system to guard Claude Opus 4. » (p. 5) ; production : p. 9. L'article ne dit pas quel modèle a produit les 7 000 échanges, ni contre quel système ils ont été écrits (« As baselines, we compare against the first-stage and second-stage classifiers from Section 4. », p. 7). J'ajoute un point vu en relisant : les étiquettes d'entraînement de la sonde viennent d'un classifieur de texte (« replace the synthetic pipeline's hard labels with exchange-level soft labels produced by a Constitutional Classifier fine-tuned from Claude Sonnet 4 », p. 7). La sonde n'est donc pas indépendante du classifieur. |
| D — verdict de tête sous une seule lecture de « juge » | majeur | corrigé | section 0 | Les deux verdicts sont donnés. La lecture la plus naturelle est « juge génératif » (programme l. 102-106 et 194 ; N-013 l. 48 ; N-068 section 4), comme le dit la contre-lecture. Je n'y défère pas : je l'ai vérifié sur les lignes. |
| E — 2502.19537, point N3 rangé à tort « côté juge » | majeur | corrigé | section 5, tables des sections 5 et 6 | Relu p. 7-8. Le coût chiffré est celui du réglage fin du modèle surveillé. Le filtre de sortie est passif (« we allow LG to censor the entire output if it detects harmfulness whereas AMD still produces a response », p. 7), et il n'est mesuré qu'à 5 000 exemples (« fine-tuned on 5000 data points », p. 8). Ma mention « de 100 à 5 000 exemples » était fausse pour le filtre. L'explication par le préfixe de refus est une hypothèse des auteurs, contredite sur Mistral par leur tableau 8 (attaque implicite 0,74 contre NOICE 0,37 sous le filtre). Je garde une nuance (section 5) : c'est le point le plus proche d'un « réglage fin du modèle surveillé contre un moniteur textuel », mais le coût n'est pas imputable au filtre. |
| F — « 250-fold » se reconstruit (5 120 / 20) | mineur | corrigé | section 4, incohérence 2 ; section 8 | Relu p. 2, 6, 15. Le rapport 5 120 / 20 = 256 (calcul) reconstruit le facteur annoncé. C'est une reconstruction de lecteur, non imprimée. Elle contredit le budget du texte principal (256 000 requêtes, soit 12 800 fois, calcul). |
| G — requêtes par succès sans les échecs | mineur | corrigé | section 4, point P1 ; section 8 | Relu p. 6 : « the average number of queries used for successful jailbreaks ». Les échecs coûtent 90 requêtes (« Given a specific behavior, PAIR uses two stopping conditions: finding a successful jailbreak or reaching the maximum number of iterations. »). Requêtes attendues par succès (calcul) : 22,3 à 2 923,7. |
| H — juges dans la boucle ; « lowest FPR » contredit | mineur | corrigé | sections 3 et 4 | Relu p. 4-5. Le juge sert de critère d'arrêt (« Thus, the algorithm runs until a jailbreak is found or the maximum iteration count K is reached. », p. 4). Le tableau 1 donne 7 % de faux positifs au juge retenu, contre 4 % pour BERT : « we use Llama Guard as the JUDGE function, as it exhibits the lowest FPR while offering competitive agreement » (p. 5) est faux. Même chose pour GPTFuzzer : le juge note les gabarits (p. 12). |
| I — les 27 heures portent sur quatre attaques universelles | mineur | corrigé | section 2, point A1 | Relu p. 4 : « four jailbreaks were capable of answering all target queries at half the detail of a model without safeguards, with an average discovery time of 27 self-reported hours ». Figure 4 (p. 14, image) : temps moyens d'environ 30, 57, 33 et 30 h ; temps minimaux d'environ 5, 15, 12 et 30 h. Ma v1 attribuait à tort les 27 h aux 13 vulnérabilités. |
| J — unité de la figure 5 | mineur | corrigé | section 2, incohérences | Vu sur l'image, p. 16 : l'axe étiqueté en pourcentage est gradué de 0 à 0,1 et de 0 à 0,05. La configuration retenue y vaut environ 0,013 ; aux figures 2b et 2c (p. 7), elle vaut environ 1,4 %. Le tracé est en fraction sous une étiquette en pourcentage. |
| K — formulation de l'incohérence 3 de 2502.19537 | mineur | corrigé | section 5, incohérences | La phrase (« Table 4 shows ASRs for the attacked and original models. », p. 5) vaut pour Claude-3-Haiku. Le seul défaut est que les chiffres de GPT-4o sont au tableau 3, qui n'est pas cité là. |
| L — voisins non lus à compléter ; casse de deux titres | mineur | corrigé | section 10 | Ajoutés : Kantamneni et collègues (p. 10, 12), Bricken et collègues (p. 11), documents d'OpenAI de 2025 (p. 10). Tous les titres sont désormais recopiés avec la casse imprimée, et ils figurent dans le JSON. |
| M — la sonde tient la première porte du système de production | mineur | corrigé | section 2, point A4 ; section 11 | Relu p. 9 : « A lightweight linear probe monitors all exchanges during generation. When the probe score exceeds a threshold, the exchange is escalated to a second-stage external classifier. » Toute attaque réussie a donc franchi la sonde, seule ou dans l'ensemble (poids 0,55, lu sur le PDF, non contrôlé par programme). Ajout à la note pour HC2. |

Aucun constat n'est maintenu en réserve. Tous les constats sont justes sur pièces. Mes réserves propres restent à la section 9.

---

## 2. 2601.04603v1 — Cunningham, Wei et collègues, Constitutional Classifiers++

**Venue imprimée.** arXiv, cs.CR, 8 janvier 2026 (p. 1). Tous les auteurs sont d'une même entreprise.

**Ce que l'article fait.** C'est une défense contre les jailbreaks universels sur des questions chimiques, biologiques, radiologiques et nucléaires. Elle a quatre volets :
1. un classifieur d'échange, qui lit la sortie avec son entrée (§ 3) ;
2. une cascade à deux étages (§ 4) ;
3. des sondes linéaires sur les activations, assemblées ensuite avec un classifieur externe (§ 5) ;
4. un système « de production » : la sonde est le premier étage, et un ensemble sonde plus classifieur est le second (§ 6).

L'attaquant est toujours un utilisateur humain par interface (p. 15). Le modèle surveillé n'est jamais l'attaquant.

**Positions de la sonde (constat C)**
- **Système de production** : la sonde lit le modèle qui génère : « Claude Sonnet 4.5. As such, the probe uses activations from that model. » (p. 9).
- **Analyse statique** (p. 7-8) : la sonde est entraînée sur un modèle qu'aucune campagne décrite ne protège. La cascade protège un autre modèle (« We use this system to guard Claude Opus 4. », p. 5), le système de production un troisième (p. 9). L'article ne dit pas quel modèle a produit les 7 000 échanges, ni contre quel système ils ont été écrits.

  La position de la sonde reste donc indéterminée dans cette analyse : elle peut lire le modèle qui génère, ou relire un échange produit par un autre modèle. De même, on ne sait pas si les attaques étaient adaptées aux deux classifieurs de comparaison (ceux de la section 4) ou toutes transférées.
- Les étiquettes d'entraînement de la sonde sont produites par un classifieur de texte (p. 7, citation au constat C). La sonde est en partie distillée de ce classifieur.

**Points de coût d'attaque chiffrés**

| point | objet attaqué | attaque | combien | succès | nature | page |
|---|---|---|---|---|---|---|
| A1 | système « dernière génération » (classifieurs d'entrée et de sortie) | équipe rouge humaine, boîte noire | 695 000 requêtes ; quatre attaques universelles découvertes en 27 h déclarées en moyenne ; temps moyen de découverte d'une vulnérabilité à haut risque d'environ 30 h, minimal d'environ 5 h | 13 vulnérabilités à haut risque (0,01871 pour mille) | auteurs ; figure 4 | 4, 14 |
| A2 | classifieur d'échange seul | idem | 226 000 requêtes ; l'unique attaque universelle a demandé 100 h ; temps moyen d'environ 57 h, minimal d'environ 15 h | 2 vulnérabilités (0,00885 pour mille) | auteurs ; figure 4 ; (100 + 15)/2 = 57,5 (calcul) | 4, 14 |
| A3 | cascade à deux étages sans sonde | idem | 569 000 requêtes ; temps moyen de 33 h ; minimal d'environ 12 h | 5 vulnérabilités (0,00878 pour mille). Hors programme de primes, des experts trouvent des jailbreaks universels, « though this required substantial effort and automated tools » (note 3 ; non chiffré) | auteurs ; figure 4 | 5, 14 |
| A4 | système de production, **sonde en premier étage** : elle lit tout ; au-dessus d'un seuil, l'échange est escaladé (environ 5,5 % du trafic) vers l'ensemble | idem | environ 1 736 h estimées, environ 198 000 tentatives ; découverte en 30 h | 1 vulnérabilité (0,005 pour mille) ; aucune attaque universelle | auteurs | 9, 10 |
| A5 | **sonde seule** contre petit et très petit **classifieurs** | jeu statique d'environ 7 000 échanges, jamais utilisés à l'entraînement, rejoués à calibration égale (0,1 % de refus sur WildChat) | aucun coût mesuré | sonde environ 1,4 % (auteurs) ; petit classifieur environ 1,1 % ; très petit environ 4,5 % (figure 2a) ; ni intervalle ni test | auteurs et figure | 7, 8 |
| A6 | ensembles statiques | idem | — | sonde avec petit classifieur environ 0,45 % ; deux classifieurs environ 0,8 % (figure 3a). Le poids est « optimized per pair to minimize attack success rate on the test set » | figure | 8 |

**Ce qu'il faut savoir pour lire A1 à A4.** Les auteurs préviennent eux-mêmes que ces chiffres dépendent de l'effort : « Since different systems received varying levels of red-teaming effort, we primarily report the vulnerability discovery rate. » (p. 4) ; « The other metrics we consider are expected to have a much stronger dependence on the volume of red-teaming, which varies across systems. » (p. 14). Questions et primes changent d'une campagne à l'autre (p. 15). Ce ne sont pas des coûts d'attaque contrôlés.

**Ce qu'il faut savoir pour lire A5.**
- Une attaque compte comme parée si le classifieur « flags at any point » : « consider the attack successfully defended against if the exchange classifier flags at any point during model sampling » (p. 7).
- Les auteurs notent : « This may underestimate the attack success rate. » (p. 7).
- Ordre de grandeur des effectifs, si le dénominateur est le jeu entier (hypothèse non imprimée) : environ 98 échanges contre environ 77 (calcul). Sans intervalle, l'écart n'est pas établi.
- Le taux de la sonde dépend fortement de ses choix d'entraînement : environ 1,4 % à environ 15 % selon la perte (figure 2b) ; « Performance degrades as fewer layers are utilized for probing. » (p. 7).

**Points de coût de défense (calcul du défenseur), distincts d'un coût d'attaque**
- **D1.** Une sonde de toutes les couches coûte environ 377 000 opérations par jeton, contre environ 8 milliards pour une passe de Gemma 3 4B. Le rapport est d'environ 2,1 × 10⁴ (calcul ; formule lue sur le PDF, non contrôlée par programme). La phrase imprimée est : « The probe is thus several orders of magnitude cheaper than a small external classifier, rendering its marginal cost for per-token prediction effectively zero. » (p. 7).
- **D2.** Surcoûts de calcul relatifs : 100, 150, 27,8 et 3,5 (tableau 1, p. 10). D'où des réductions de 42,9, 7,9 et 5,4 fois (calcul, conformes aux réductions annoncées).
- **D3.** Une cascade sonde plus petit classifieur offre « a 100x reduction in compute costs » (p. 8, 9).

« Plusieurs ordres de grandeur » n'apparaît dans cette pièce que pour le coût de **défense** de la sonde, et dans le sens inverse de HC4.

**Ce que l'article ne fait pas**
- Aucune attaque dirigée contre la sonde, et aucune optimisation contre son score.
- Aucun régime « activations » ni « poids » appliqué à un moniteur. L'« obfuscation » des p. 2-4 est celle du texte de sortie.
- Aucun coût d'évasion séparé pour la sonde et pour les classifieurs.
- Aucun juge génératif sous rhétorique, aucun agent auteur. La propriété détectée est un contenu nuisible.

**Incohérences et réserves**
1. « 2.2x fewer » (p. 2) : 0,01871/0,00885 = 2,11 (calcul).
2. Les campagnes ne sont pas comparables entre elles (voir plus haut).
3. **R4** : poids des ensembles optimisés sur le jeu de test (p. 8).
4. Le décompte des requêtes ne garde que les utilisateurs dont plus de 5 % des requêtes sont refusées (p. 14). Ce filtre dépend du défenseur lui-même.
5. Figure 5 (p. 16) : l'axe est étiqueté en pourcentage mais tracé en fraction (constat J).
6. La p. 9 appelle « detection rate » ce qui est un taux de découverte de vulnérabilités. Défaut de mot, sans effet.

**Verdicts par composante**

| composante | verdict |
|---|---|
| (a) coût d'attaque mesuré | **occupée en partie** : requêtes et heures par vulnérabilité contre des systèmes de classifieurs, ou de sonde et classifieur (A1-A4). Ces chiffres ne mesurent pas le déplacement d'un moniteur isolé, et ils ne sont pas obtenus à effort constant. |
| (b) sonde | **occupée en partie** : taux de succès d'attaques rejouées contre une sonde (A5), sans coût, sans attaque qui s'adapte, position non établie ; plus le point A4 (sonde en premier étage d'un système franchi une fois en 30 h) |
| (c) juge | **voisin** (classifieurs affinés, non génératifs) |
| (d) comparaison dans un même cadre | juge génératif : **voisin très proche** ; lecture large : **occupée en partie** (axe « taux de succès » seulement, transfert statique, p. 7-9) |
| (e) prémisse | **contre-indice indirect, hors du périmètre restreint par N-068** : des attaques en boîte noire, non écrites contre la sonde, la franchissent à environ 1,4 %, contre environ 1,1 % pour un classifieur à calibration égale. Aucun coût d'évasion n'est mesuré. Un classifieur durci n'est pas déplacé gratuitement (100 h pour l'unique attaque universelle, p. 4). |

---

## 3. 2309.10253v4 — Yu, Lin, Yu, Xing, GPTFuzzer

**Venue imprimée.** arXiv v4, 27 juin 2024 (p. 1). Aucune venue n'est imprimée.

**Ce que l'article fait.** C'est un « fuzzing » en boîte noire de gabarits de jailbreak : graines humaines, mutation par un modèle de langue, jugement par un RoBERTa affiné. L'article précise : « given that we neither access the source code nor the weights of the models under examination » (p. 3).

**Points de coût chiffrés.** L'objet attaqué est toujours le modèle lui-même.
- **G1.** Contre Llama-2-7B-Chat, plafond de 500 requêtes par question. Requêtes moyennes selon les graines : 22,47 (cinq meilleures) ; 105,62 (valides) ; 177,54 (toutes) ; 358,91 (invalides). Questions percées : 46/46, 45/46, 43/46, 21/46 (tableau 3, p. 12). Phrase imprimée : « Remarkably, on average, it requires fewer than 23 queries to breach the defenses of the aligned Llama-2-7B-Chat. » (p. 11).
- **G2.** Budget de 50 000 requêtes pour 100 questions : premier gabarit à 47-60 %, cinq meilleurs à 87-96 % (p. 12).
- **G3.** Transfert : cinq meilleurs gabarits à environ 80 % sur Llama-2-70B (p. 14).
- **G4.** Référence en boîte blanche (GCG) à 500 pas, sous les gabarits humains contre les modèles commerciaux (p. 13-14, figure 5).
- **G5.** Coût global : plus de 300 millions de jetons (p. 9).
- **G6 (constat H).** Le juge de mesure est **dans la boucle d'attaque** : « The cumulative score for the jailbreak template is derived from the sum of the scores from these 100 responses » (p. 12). Il n'est pas visé comme moniteur ; ses faux positifs comptent comme des succès. Coûts de jugement : RoBERTa 37 s, GPT-4 1 h 27 min pour 1 540 réponses (tableau 1, p. 9).

**Ce que l'article ne fait pas.** Aucune sonde, aucun moniteur visé, aucune comparaison.

**Incohérences**
- « Appendix XXX » est resté non rempli (p. 16).
- La version « gpt-3.5-turbo-0631 » porte une date impossible (p. 4, 25, 26).
- La figure 9 (p. 24) a un axe « ASR (%) » gradué de 0 à 1,0.

**Verdicts.** (a) voisin ; (b) ne touche pas ; (c) ne touche pas ; (d) ne touche pas ; (e) contre-indice faible et indirect : un lecteur de texte durci n'est pas déplacé gratuitement (de 22 à 359 requêtes par question), mais ce n'est pas un moniteur.

---

## 4. 2310.08419v4 — Chao, Robey, Dobriban, Hassani, Pappas, Wong, PAIR

**Venue imprimée.** « Preprint. Under review. » (p. 1).

**Ce que l'article fait.** Un modèle attaquant affine en boîte noire une consigne contre une cible. Les trois stratégies sont rhétoriques : « each system prompt template is based on one of three criteria: logical appeal, authority endorsement, and role-playing » (p. 3). Le juge (Llama Guard) est **le critère d'arrêt** (constat H) : « Thus, the algorithm runs until a jailbreak is found or the maximum iteration count K is reached. » (p. 4).

**Points de coût chiffrés.** L'objet attaqué est toujours le modèle lui-même.
- **P1.** Avec au plus 90 requêtes par comportement, les requêtes par succès sont : Vicuna 10,0 ; Llama-2 56,0 ; GPT-3.5 33,0 ; GPT-4 23,7 ; Claude-1 13,7 ; Gemini 23,5. Taux de succès : 88 %, 4 %, 51 %, 48 %, 3 %, Claude-2 0 %, Gemini 73 % (tableau 2, p. 5).

  Ce compte ne retient que « the average number of queries used for successful jailbreaks » (p. 6). Si l'on compte les échecs à 90 requêtes, les **requêtes attendues par succès** sont (calcul, constat G) : Vicuna 22,3 ; Gemini 56,8 ; GPT-3.5 119,5 ; GPT-4 121,2 ; Llama-2 2 216 ; Claude-1 2 923,7 ; Claude-2 sans borne (aucun succès). C'est ce chiffre qui approche un coût d'attaque.
- **P2.** GCG en boîte blanche, pour comparaison : « run the attack for 500 iterations with a batch size of 512 for a similar computational budget of around 256,000 queries per behavior » (p. 6). Taux de 56 % et 2 %.
- **P3.** PAIR : 34 s, 366 Mo, environ 0,03 dollar ; GCG : près de deux heures sur A100 (p. 7, 8).
- **P4.** SmoothLLM (perturbation de l'entrée) et filtre de perplexité, rejoués sans attaque : « Both defenses are evaluated statically » (p. 7). Ni juge ni sonde.
- **P5.** Tableau 8 (AdvBench, « a representative 50-behavior subset of the AdvBench dataset », p. 15) : PAIR de 11,9 à 33,8 requêtes par succès ; GCG 5 120.

**Ce qui touche HC4 dans la méthode.** P2, P3 et P5 comparent deux régimes d'accès sur un même objet. L'attaque en boîte blanche y coûte bien plus de requêtes. Le coût dépend donc autant de l'algorithme que de l'accès : plus d'accès ne veut pas dire coût plus faible. C'est un voisin de méthode, sans sonde ni juge.

**Incohérences**
1. Le résumé dit « often », l'introduction dit « within twenty queries » (p. 2) ; le tableau 2 donne plus de 20 requêtes par succès pour quatre cibles sur six.
2. **Facteur 250 (constat F).** La phrase est : « Our results indicate that PAIR efficiently discovers prompt-level jailbreaks within twenty queries, which represents a more than 250-fold improvement over existing attacks such as GCG » (p. 2). Le facteur se reconstruit comme 5 120 / 20 = 256 (calcul, reconstruction non imprimée). Il contredit le budget du texte principal : 256 000 / 20 = 12 800 (calcul).
3. Les deux budgets de GCG (256 000 et 5 120) diffèrent d'un facteur 50 sans explication, sur deux jeux distincts (p. 6, 15).
4. La même configuration donne 88 % au tableau 2 et 93 % au tableau 7 (p. 9).
5. « Vicuna-17B » (p. 2).
6. **Constat H** : « we use Llama Guard as the JUDGE function, as it exhibits the lowest FPR while offering competitive agreement » (p. 5) ; le tableau 1 (p. 4) donne 7 % à ce juge et 4 % à BERT.

**Verdicts.** (a) voisin ; (b) ne touche pas ; (c) voisin : rhétorique en boîte noire contre un lecteur de texte, qui est le modèle lui-même ; (d) voisin de méthode (régimes) ; (e) contre-indice indirect : la rhétorique ne déplace pas gratuitement un lecteur durci (Claude-2 0 %, Llama-2 4 %, p. 5 ; jusqu'à environ 2 900 requêtes attendues par succès, calcul). « We also find that authority endorsement prompts are typically the least effective. » (p. 8).

---

## 5. 2502.19537v5 — Kazdan et collègues, NOICE

**Venue imprimée.** « Preprint. Under review. » (p. 1).

**Ce que l'article fait.** C'est une attaque par réglage fin sur des données d'apparence inoffensive. Le modèle réglé refuse, puis répond. Le régime est celui des **poids du modèle surveillé**, réglés par l'attaquant. Rien n'est adressé au filtre.

**Points de coût chiffrés (constat E)**
- **N1.** GPT-4o : 1 000 exemples, 3,3 millions de jetons, environ 85 dollars ; succès de 57 % contre 8,6 % (p. 5-6). Claude-3-Haiku : 72 % (tableau 4). Mesuré sans filtre de sortie.
- **N2.** Modèles ouverts, 5 000 exemples, environ 30 minutes sur 2 A100 (p. 21). Taux de succès avec le filtre Llama Guard : 0,47, 0,31 et 0,37 ; avec AMD : 0,48, 0,29 et 0,60 (tableau 8, p. 8). Le filtre est passif : « we allow LG to censor the entire output if it detects harmfulness whereas AMD still produces a response » (p. 7). Il n'est mesuré qu'à 5 000 exemples (« fine-tuned on 5000 data points », p. 8).
- **N3.** Courbe en fonction du nombre d'exemples (10 à 5 000) : seulement sans défense, avec AMD, et avec une défense « FRD » non définie (tableaux 16 et 17, p. 37). Le « 100 exemples » vaut sans défense : « Note that fine-tuning on as few as 100 comromises model safety. » (p. 36).
- **N4.** Le succès est noté par un autre juge, non attaqué : « harmfulness of the responses using GPT-4o (OpenAI et al., 2024) as a judge » (p. 7).

**Le mécanisme annoncé est une hypothèse des auteurs.** Ils écrivent : « NOICE has a higher ASR against LG than other attacks, likely because LG is deceived by the refusal prefix into thinking that the entire response is harmless. » (p. 7). Le tableau 8 la contredit en partie :
- sur Mistral, sous le filtre, l'attaque implicite garde 0,74 et NOICE 0,37 ;
- baisses relatives dues au filtre pour NOICE : 16 %, 11 % et 44 % (calcul) ;
- les données ouvertement nuisibles passent encore à 0,82, 0,47 et 0,58.

Le filtre laisse donc passer beaucoup sans être « trompé ».

**Nuance que je garde.** C'est le point des quatre pièces le plus proche d'un « réglage fin du modèle surveillé pour passer un moniteur textuel », c'est-à-dire du régime « poids » de HC4 côté juge. Mais aucun coût n'y est imputable au filtre, et l'attaque n'est pas optimisée contre lui.

**Ce que l'article ne fait pas.** Aucune sonde, aucune comparaison, aucune écriture dans le juge. Le filtre n'est pas appliqué à GPT-4o ni à Claude-3-Haiku.

**Incohérences**
- « seven times higher than previous fine-tuning attacks (see Table 5) » (p. 2) : les chiffres sont au tableau 3 ; 0,57 divisé par 0,086 / 0,06 / 0,043 / 0,013 donne 6,6 / 9,5 / 13,3 / 43,8 (calcul).
- « Llama 3 8b-Instruct, and Llama 3.1 7b-Instruct » (p. 7) : le tableau 7 donne « 70B ».
- Le renvoi « Table 4 shows ASRs for the attacked and original models. » (p. 5) ne couvre que Claude-3-Haiku ; les chiffres de GPT-4o sont au tableau 3 (constat K).
- « FRD » n'est pas défini.
- Les tableaux 11 à 15 ne disent pas quelle défense s'applique à chaque ligne.

**Verdicts.**
- (a) **voisin** : coût de réglage fin du modèle surveillé ; filtre appliqué après coup, à 5 000 exemples seulement ; aucun coût propre au filtre.
- (b) ne touche pas.
- (c) **voisin** : filtre de sortie passif, dont l'explication par le préfixe est une hypothèse contredite sur Mistral.
- (d) ne touche pas.
- (e) **ne tranche pas** : indice de faiblesse du filtre, pas une mesure du coût de son déplacement.

---

## 6. Table de synthèse (composante × pièce), mise à jour

| composante | 2601.04603 | 2309.10253 | 2310.08419 | 2502.19537 |
|---|---|---|---|---|
| (a) coût d'attaque mesuré | occupée en partie (systèmes, effort variable ; p. 4, 5, 9, 14) | voisin (p. 11-12) | voisin (p. 5-8, 15) | **voisin** (réglage fin du modèle surveillé ; p. 5-8, 21) |
| (b) sonde | occupée en partie (taux rejoués ; position non établie ; p. 5, 7-9) | ne touche pas | ne touche pas | ne touche pas |
| (c) juge | voisin (classifieurs affinés) | ne touche pas (juge dans la boucle, non visé) | voisin (juge dans la boucle, non visé) | voisin (filtre passif) |
| (d) même cadre | juge génératif : voisin très proche ; lecture large : occupée en partie (p. 7-9) | ne touche pas | voisin de méthode (régimes) | ne touche pas |
| (e) prémisse | contre-indice indirect, hors du périmètre restreint par N-068 | contre-indice faible | contre-indice indirect | ne tranche pas |

---

## 7. Ce qui reste revendicable (formulation exacte)

> « Le coût d'attaque — requêtes, jetons, calcul, temps, exemples de réglage fin — nécessaire pour obtenir un déplacement donné du score d'une sonde entraînée qui lit l'intention ou l'action de l'agent auteur, à taux de faux positifs fixé, comparé dans un même cadre au coût du même déplacement sur un juge génératif sous les mêmes attaques, par régime d'accès (contexte seul ; lecture des activations ou des poids ; écriture dans les poids), à durcissement déclaré et sous attaque qui s'adapte. »

- C'est **non trouvé dans les quatre pièces lues**, sous les deux sens de « juge ». Zone peu cherchée : ce n'est pas un trou du champ.
- Sous la lecture large, une composante est prise : la comparaison du **taux de succès** d'attaques rejouées en boîte noire, à calibration égale, entre une sonde de contenu nuisible et des classifieurs affinés (2601.04603, p. 7-9).
- La prédiction « de plusieurs ordres de grandeur » reste une prédiction. Aucune pièce ne la soutient ; la seule comparaison trouvée donne des taux voisins.

---

## 8. Ce qu'une phrase publique sur HC4 ne doit pas affirmer

Je ne rédige pas la phrase publique.

1. Qu'aucune comparaison d'une sonde et d'un modèle qui lit le texte, sous les mêmes attaques et à calibration égale, n'est publiée. Sous la lecture large, 2601.04603 en publie une, sur le taux de succès (p. 7-9).
2. Que les sondes sont plus, ou moins, robustes que les classifieurs face au contenu seul. Sur attaques rejouées, les taux sont voisins (environ 1,4 % contre 1,1 %), sans intervalle, avec une origine des attaques inconnue. La pièce ne dit rien du coût d'évasion.
3. Que la rhétorique déplace « gratuitement » un lecteur de texte durci :
   - 100 h pour l'unique attaque universelle contre un classifieur d'échange (p. 4) ;
   - PAIR : 0 % sur Claude-2 et jusqu'à environ 2 900 requêtes attendues par succès (calcul) ;
   - GPTFuzzer : de 22 à 359 requêtes par question.
4. Que « several orders of magnitude » (2601.04603, p. 7) mesure un écart de coût d'attaque. C'est le coût de **défense** de la sonde, plus faible.
5. Que les « requêtes par succès » de PAIR (10 à 56) sont un coût d'attaque contre un juge. Elles visent le modèle, elles omettent les échecs, et le juge n'est pas attaqué.
6. Citer le facteur « 250-fold » de PAIR comme un écart mesuré. Il se reconstruit à partir d'un budget nominal (5 120 / 20), contredit par le budget de 256 000 requêtes du texte principal.
7. Que le système de production de 2601.04603 (1 736 h, une vulnérabilité) mesure la robustesse d'une sonde seule. C'est une cascade sonde plus classifieur, testée à effort variable.
8. Que le coût par réglage fin de 2502.19537 (85 dollars, ou 1 000 à 5 000 exemples) est un coût de déplacement d'un juge.
9. Que le contenu seul ne franchit pas une sonde lue sur le modèle qui génère. Le système de production de 2601.04603 a été franchi une fois en boîte noire (p. 9). La lettre restreinte par N-068 n'est pas touchée par cette pièce.
10. Que « plusieurs ordres de grandeur » est observé quelque part dans ces pièces, entre une sonde et un juge.

---

## 9. Réserves

- **Sens de « juge »** : il revient à Lazar (section 0).
- **R4** : poids d'ensemble optimisés sur le jeu de test (2601.04603, p. 8) ; campagnes d'équipe rouge non comparables (p. 4, 14, 15).
- **Profondeur.** La v1 avait été lue en une douzaine de minutes ; la contre-lecture l'a jugée mince, à juste titre. Les défauts trouvés étaient des défauts de lecture critique (B, C, E, I), pas de transcription. Les relectures exigées sont faites (en-tête). Elles ont ajouté deux points : la distillation de la sonde à partir d'un classifieur (p. 7) et la sensibilité de la sonde à ses choix d'entraînement (figure 2b).
- **Valeurs lues sur les figures** : elles sont approximatives (nature « figure »).
- **Constat B2** (l. 140 de l'état de l'art v1, hors mandat, non ouverte) : les chiffres vérifiés de PAIR et de GPTFuzzer sont aux sections 3 et 4. La confrontation reste à faire par la session mère.

---

## 10. Voisins nommés dans les pièces et non lus

| voisin (titre tel qu'imprimé) | nommé dans | page |
|---|---|---|
| McKenzie et collègues 2025, « Detecting high-stakes interactions with activation probes » | 2601.04603 | 10, 12 |
| Cunningham et collègues 2025, « Cost-effective constitutional classifiers via representation re-use » (billet) | 2601.04603 | 10, 12 |
| Hua et collègues 2025, « Combining cost-constrained runtime monitors for AI safety » | 2601.04603 | 10, 12 |
| Sharma et collègues 2025, « Constitutional classifiers: Defending against universal jailbreaks across thousands of hours of red teaming » | 2601.04603 | 1, 13 |
| Kantamneni et collègues 2025, « Are sparse autoencoders useful? A case study in sparse probing » (« Others build classifiers using sparse auto-encoder features », p. 10) | 2601.04603 | 10, 12 |
| Bricken et collègues 2024, « Using dictionary learning features as classifiers » | 2601.04603 | 10, 11 |
| OpenAI 2025a et 2025b, classification en deux étages (« employ a lightweight topic filter to identify high-harm content areas ») | 2601.04603 | 10 |
| Youstra et collègues 2025, « Towards safeguarding LLM fine-tuning APIs against cipher attacks » | 2601.04603 | 5, 13 |
| Casper et collègues 2024, « Defending against unforeseen failure modes with latent adversarial training » | 2601.04603 ; 2502.19537 | 10, 12 ; 11 |
| Zou et collègues 2024, « Improving alignment and robustness with circuit breakers » | 2601.04603 | 10, 13 |
| Nikolić et collègues 2025, « The jailbreak tax: How useful are your jailbreak outputs? » | 2601.04603 | 3, 12 |
| Zeng et collègues 2024, « How johnny can persuade llms to jailbreak them » | 2310.08419 | 3, 11 |
| Chao et collègues 2024, « Jailbreakbench: An open robustness benchmark for jailbreaking large language models » | 2310.08419 | 5, 12 |
| Jain et collègues 2023, « Baseline defenses for adversarial attacks against aligned language models » ; Alon et Kamfonas 2023, « Detecting language model attacks with perplexity » | 2310.08419 | 7, 12 |
| Robey et collègues 2023, « Smoothllm: Defending large language models against jailbreaking attacks » | 2310.08419 | 7, 11 |
| Deng et collègues 2023, « Jailbreaker: Automated jailbreak across multiple large language model chatbots » | 2309.10253 | 13, 17 |
| Huang et collègues 2025, « Virus: Harmful fine-tuning attack for large language models bypassing guardrail moderation » (réglage fin contre un filtre de modération : voisin côté juge, régime poids) | 2502.19537 | 13 |
| Halawi et collègues, « Covert malicious finetuning: challenges in safeguarding llm adaptation » | 2502.19537 | 3, 13, 20 |
| Davies et collègues 2025, « Fundamental limitations in defending llm finetuning apis » | 2502.19537 | 1, 11 |
| Qi et collègues 2024, « On evaluating the durability of safeguards for open-weight llms » ; Tamirisa et collègues 2024, « Tamper-resistant safeguards for open-weight llms » ; Rosati et collègues 2024, « Representation noising effectively prevents harmful fine-tuning on llms » | 2502.19537 | 15 ; 16 ; 16 |
| Wang et collègues 2024, « Jailbreak defense in a narrow domain: Limitations of existing methods and a new transcript-classifier approach » | 2502.19537 | 17 |
| Yi et collègues 2025, « Probe before you talk: Towards black-box defense against backdoor unalignment for large language models » (défense en boîte noire, malgré le titre) | 2502.19537 | 18 |

Priorité de lecture si HC4 est cherchée plus avant :
1. McKenzie et collègues, puis Cunningham et collègues (sondes contre classifieurs) ;
2. Hua et collègues (moniteurs sous contrainte de coût) ;
3. Huang et collègues, « Virus » (réglage fin contre un filtre de modération, voisin côté juge, régime poids).

---

## 11. Note à part, sans verdict : ce qui touche HC2

**Système de production de 2601.04603 (constat M).** La sonde y tient la première porte : « A lightweight linear probe monitors all exchanges during generation. When the probe score exceeds a threshold, the exchange is escalated to a second-stage external classifier. » (p. 9). Elle escalade environ 5,5 % du trafic : « The first-layer probe escalated approximately 5.5% of traffic to the second-stage classifier. » (p. 9).

Toute attaque réussie a donc franchi la sonde, seule ou dans l'ensemble. Le point de coût publié est le suivant :
- une seule attaque, découverte en 30 h ;
- environ 198 000 tentatives et environ 1 736 h au total ;
- par le contenu seul, en boîte noire, avec des attaquants humains qui s'adaptent ;
- contre un système dont la sonde lit le modèle qui génère (p. 9).

Ce point ne sépare pas la sonde du classifieur. L'auteur du contenu adverse est un utilisateur externe, la propriété détectée est un contenu nuisible, et il n'y a aucune mesure du déplacement continu g.

**Analyse statique (constat C).** La position de la sonde n'est pas établie : elle peut être une sonde « du lecteur ». Ses étiquettes viennent d'un classifieur de texte. Et la sonde signale davantage de requêtes bénignes : « Moreover, we found that the flag rate on benign scientific requests was higher for the probe. » (p. 8).

C'est une matière pour le lecteur de HC2 ; je ne prononce rien à son sujet.
