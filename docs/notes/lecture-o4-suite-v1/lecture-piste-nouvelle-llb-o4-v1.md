# Lecture de la piste nouvelle LLB contre O4 (juge au nul formé des lois connues) — v1

- **Lecteur et rédacteur : modèle I.** Aucune contre-lecture n'est faite ici (elle revient au modèle J, si Lazar la demande).
- **Heures (`date -u`, recopiées des commandes)** : début 2026-11-18T03:07:32Z ; empreinte du PDF et extraction du texte 2026-11-18T03:07:48Z ; début de rédaction 2026-11-18T03:11:21Z ; premier rejeu des listes 2026-11-18T03:11:31Z ; rejeu final des deux listes 2026-11-18T03:14:10Z.
- **Source.** Domke, *Large Language Bayes*, arXiv 2504.14025 v2 (23 octobre 2025, conférence NeurIPS 2025), `docs/sources/pdf/lecture-o4-v3/arxiv-2504.14025/2504.14025v2.pdf`, 63 pages, sha256 **7c0eee0567fc0c547ad0724ea1df385265c8f80778b3a6cfa6c46b06af2ead4a**, recalculé par moi, conforme à l'empreinte donnée.
- **Profondeur (détail en section 1).** PDF entier, annexes comprises ; code : aucun (par consigne ; la pièce déclare ne pas publier de code, p. 61).
- **Rejeux.** Citations du PDF : **42 sur 42** (`lecture-piste-nouvelle-llb-o4-v1-resultat-citations-pdf.json`, code de sortie 0). Extraits de code : **0 sur 0**, liste vide par consigne (`lecture-piste-nouvelle-llb-o4-v1-resultat-extraits-code.json`, code de sortie 0). Chaque passage entre guillemets français de cette note (29) est dans la liste des citations (contrôle automatique, hors dépôt) ; la liste porte en plus 13 passages d'appui, non recopiés dans la note (pages 1, 2, 3, 6, 7, 8, 10, 15, 32, 39).
- **Règles.** R7 (rien sans page), R8 (*non trouvé* = non trouvé dans ce qui est lu, à la profondeur dite), R4 (doute tranché contre notre revendication), N-067 : personne ici ne déclare O4 libre ; verdict en vigueur **occupée en partie** ; tout écart ou précision est un nœud (section 6). Pages = pages du PDF. Guillemets français : seulement des citations de l'article ; mots de nos notes en italique ; termes cherchés et noms de fichiers entre accents graves. Aucun nom de modèle de langue commercial n'est recopié.
- Aucune dépense, aucun accès réseau, aucun programme des clones lancé ni lu, aucun refus de permission, de crochet ou de classifieur rencontré.

**Verdict de la pièce, d'abord.** LLB n'est pas sans rapport : elle **prend (i)** (un modèle de langue propose des lois probabilistes formelles) et **occupe l'opérateur de (ii)** — une mise en commun des lois prédictives des propositions, pondérée par les données (vraisemblance marginale), que l'auteur nomme lui-même moyenne bayésienne de modèles. Elle ne forme pas cette mise en commun d'une **archive de lois connues** et ne s'en sert pas comme **nul** : la mise en commun est la sortie, pas l'adversaire. Aucun test, aucune règle de promotion, aucune validité à tout instant d'arrêt, aucun scellement. **Conjonction : non trouvée.** Verdict sur O4 inchangé : **occupée en partie** ; mais la forme *mise en commun ajustée de lois prédictives*, seule, n'est plus à nous (nœud 2).

## 1. Profondeur

| partie | pages | lecture |
|---|---|---|
| résumé, introduction, idée (§ 1-2), inférence (§ 3), expériences (§ 4), théorie (§ 5), discussion et travaux voisins (§ 6) | 1-10 | en entier |
| références, notation | 11-14 | en entier (titres des références ; aucune référence lue) |
| annexe B, résultats détaillés des huit problèmes | 15-44 | prose et légendes en entier ; code Stan des modèles d'exemple et figures parcourus, non lus ligne à ligne |
| annexe C (analyses), D (algorithmes 4 à 8), E (preuves) | 45-52 | en entier ; preuves lues, non vérifiées mathématiquement |
| annexe F, détails d'expérience, consigne système, validation des modèles | 53-54 | en entier |
| annexe G, exemples d'apprentissage en contexte | 55-60 | entrées lues ; sorties (pensées et code Stan) parcourues |
| liste de contrôle de la conférence | 61-63 | en entier |

Texte extrait par `pdftotext` (mode brut, découpé aux sauts de page : 64 segments, le dernier vide après le saut final, soit 63 pages). Recherche de termes sur le texte entier, page par page, après normalisation (NFKC, minuscules, césures recollées, espaces réduits), avec et sans trait d'union. Code : aucun lu. Le fichier `provenance-v1.md` du dossier de la pièce n'est pas lu (non nommé par la consigne).

## 2. Recherche de termes (texte entier)

| terme | pages | ce que donne le terme |
|---|---|---|
| `e-value`, `e-process`, `anytime`, `martingale`, `optional stopping`, `stopping` | aucune | absent |
| `sequential` | 11 | titre de la référence [7] (méthodes de Monte-Carlo séquentielles) ; sans rapport avec un test séquentiel |
| `likelihood ratio`, `Bayes factor` | aucune | absents ; les poids sont des vraisemblances marginales normalisées (p. 2, 4, 8), jamais nommées facteurs de Bayes ni comparées à un seuil |
| `model averaging` | 2, 3, 13, 14 | la sortie est dite une moyenne bayésienne de modèles (p. 2, 3) ; références [16], [18], [32] (p. 13) ; sigle BMA (p. 14) |
| `stacking`, `encompass`, `spanning` | aucune | absents |
| `benchmark`, `baseline`, `null` | aucune | absents ; la comparaison faite est la moyenne *plate* (`flat`, 19 pages, de 3 à 54) des mêmes propositions |
| `multiple testing`, `multiple comparison`, `false discovery`, `Bonferroni`, `Holm`, `p-value`, `threshold`, `hypothesis test` | aucune | absents |
| `test` | 5-7, 10, 28-43, 53, 57, 59, 61 | jours, positions ou données *de test* des problèmes ; *tested it experimentally* (p. 10) ; jamais un test statistique |
| `pre-regist`, `pre-commit`, `commit`, `hash`, `seal` | aucune | absents |
| `archive`, `library`, `reuse` | aucune | absents |
| `human-written`, `remember`, `cutoff` | 5 | précaution contre la mémoire du modèle de langue : problèmes et données neufs, date de mise en ligne (voir (iv-a)) |
| `promot`, `accept` | 54 seulement pour `accept` | acceptation d'un biais de normalisation ; aucune promotion |
| `coverage`, `calibrat` | 32 | couverture des intervalles à 88 % pour LLB comme pour la moyenne plate ; aucun test |

## 3. Lecture par composante

**P — juger contre le connu, non contre *aucun effet* : voisin (lointain).** Chaque proposition est jugée **relativement aux autres propositions du même tirage**, par son accord aux données ; sur la différence avec la moyenne plate : « the fundamental difference between the true posterior and “flat” posterior is that the former gives more influence to models that are more consistent with the observed data » (p. 3). Ce n'est ni un nul *aucun effet* ni un nul formé du connu. Le connu est même **écarté à dessein** : « To avoid the risk that the LLM would simply “remember” human-written models, these experiments use all-new problems and datasets. » (p. 5). Aucun modèle connu, aucune référence publiée ne sert d'étalon dans le texte lu ; les figures montrent seulement des repères (taux de base, estimateur du maximum de vraisemblance, densité vraie), sans règle. Je mets *voisin (lointain)* plutôt que *non trouvé* (R4) : le jugement relatif entre propositions par la vraisemblance est de la même famille que celui d'EVOSCM, que la v3 a porté *voisin*.

**(i) — proposeurs modèles de langue : pris.** « Given informal user text, an LLM generates a set of candidate formal models. Inference is performed on each and the posteriors are combined with weight proportional to the marginal likelihood. » (p. 2) ; « combines a large language model and a probabilistic programming language to define a joint distribution over formal models, latent variables, and data » (p. 1) ; dans l'algorithme des expériences, « Sample m(n) ∼ p(m|t) using an LLM. » (p. 53). Les propositions sont des **lois prédictives complètes** (programmes Stan qui définissent la loi jointe des données et des variables cibles), pas des énoncés verbaux.

**(ii) — nul = mise en commun ajustée des lois prédictives de l'archive : voisin (proche pour l'opérateur ; lointain pour l'archive et pour le rôle de nul).** Dit fort : **l'opérateur est publié ici pour des lois proposées par un modèle de langue.** La recette consiste à « generating many formal models from the large language model, performing approximate inference on each, and then doing a weighted average » (p. 1) ; les poids sont proportionnels à la vraisemblance marginale (p. 2, citation ci-dessus) ; l'auteur la range lui-même : « Note that the final posterior in Eq. (4) can be seen as an instance of Bayesian model averaging » (p. 2), « just with a prior over models that’s defined using an LLM » (p. 2), et cite la littérature classique de l'opérateur, par exemple « Hoeting, J. A., Madigan, D., Raftery, A. E., and Volinsky, C. T. Bayesian Model Averaging: A Tutorial. » (p. 13), « Wasserman, L. Bayesian Model Selection and Model Averaging. » (p. 13), « Kejzlar, V., Bhattacharya, S., Son, M., and Maiti, T. Black Box Variational Bayesian Model Averaging. » (p. 13) (références non lues). Ce qui manque, à la profondeur lue :
- **pas d'archive** : chaque problème part d'une description neuve ; les membres de la mise en commun sont les seules propositions du tirage courant ; `archive`, `library`, `reuse` absents ; les lois connues sont écartées à dessein (p. 5, ci-dessus) ;
- **pas de rôle de nul** : la mise en commun **est** la loi rendue à l'utilisateur, non l'adversaire qu'une proposition doit battre ; aucune proposition n'est opposée à une mise en commun d'autres lois ;
- **forme des poids** : probabilités a posteriori des modèles (prior du modèle de langue fois vraisemblance marginale, estimée par des bornes), non des poids ajustés pour la prédiction ; `stacking` absent. Je n'ai pas lu, dans cette session, si notre *nul d'archive ajusté* (LISEZMOI v7-v6, cité par la note d'englobement) ajuste ses poids d'une manière qui l'en distingue : je ne m'appuie pas sur cette différence.

**(iii) — e-processus ou statistique à validité à tout instant d'arrêt comme règle de promotion : non trouvé.** Tous les termes de la famille sont absents (section 2). Les poids sont doux ; rien n'est promu, rien n'est rejeté sur un critère statistique. Les seuls rejets sont syntaxiques : « Outputs from the LLM were rejected if they did not contain GOAL and MODEL blocks or if the code in the model block did not compile. » (p. 4) et « We thus reject all models that contain the string “target += ”, as if they did not compile. » (p. 54). Les données sont prises en un bloc ; aucune accumulation, aucun arrêt. Remarque de lecteur, **non opposable** (R7, hors de la pièce) : le rapport des vraisemblances marginales de deux lois est ce qu'on appelle un facteur de Bayes ; voir nœud 3.

**(iv-a) — prédictions engagées (scellées) avant que les données existent : voisin (lointain).** Par construction formelle, la loi proposée dépend de la seule description : « Denote the informal user text as t and a formal model as m. » (p. 2), la description comprenant « including anything they know about the phenomena under study, the types and shapes of the input data » (p. 2), et l'entrée du modèle de langue contenant « a DATA block describing the data » (p. 4) ; les exemples montrés ne donnent dans ce bloc que les types, les valeurs étant présentées à part (fig. 2, p. 5 ; B.1, p. 15). Les lois sont donc **fixées sans les valeurs**, au sens de la définition. Mais :
- les données **existent déjà** quand les lois sont produites (« I’ve recorded the precipitation in Amherst, Massachusetts for each day in December 2024. », p. 2) ;
- aucun engagement, aucun scellement, aucun horodatage (`commit`, `hash`, `seal`, `pre-regist` absents) ; je n'ai trouvé aucune vérification écrite que les valeurs ne passent pas dans l'entrée du modèle de langue ;
- la seule précaution temporelle porte sur la mémoire d'entraînement, non sur les prédictions : « any future work in this direction should not use these problems for evaluation with any LLM with a knowledge cutoff after the date this paper was first made public » (p. 5).

**(iv-b) — statistique calculée hors des agents : pris pour la statistique ; sans objet pour la promotion (il n'y en a pas).** Le modèle de langue ne fait qu'écrire les modèles ; l'échantillonnage, les bornes de vraisemblance marginale et les poids sont calculés par le programme probabiliste : « To approximate the marginal likelihood, we used importance-weighted variational bounds » (p. 53) ; la liste de contrôle le confirme : « It was used only for generating probabilistic models as described clearly in the text. » (p. 63). **Réserve qui touche notre propre (iv-b)** : la loi notée est **écrite par le proposeur**, et le texte reconnaît qu'un proposeur peut gonfler sa note par une densité non normalisée : « One can directly manipulate the target using the “target += ” construct, essentially leading to arbitrary changes with no probabilistic interpretation. » (p. 54). La garde est un filtre textuel sur une seule construction (p. 54, ci-dessus) ; pour les autres, « Checking usage of #1, #2, and #4 is not trivial to do programmatically » (p. 54), d'où des vérifications à la main : « we relied instead on spot checks in models given high weight » (p. 54) ; et un biais de normalisation des contraintes est accepté : « We simply accept this bias in practice, though note the bias is always downwards » (p. 54). Le calcul est hors du modèle de langue ; **l'objet calculé ne l'est pas** (nœud 4).

**Conjonction (i)+(ii)+(iii)+(iv-a)+(iv-b) : non trouvée** dans LLB, à la profondeur de la section 1. Ce constat ne dit rien du champ (R8) et ne change pas le verdict **occupée en partie**.

## 4. Réponses aux questions de la consigne

1. **La moyenne de modèles pondérée par la vraisemblance marginale est-elle une mise en commun ajustée de lois prédictives (ii) ?** Pour l'opérateur, **oui** : mélange des lois a posteriori (donc prédictives) des modèles proposés, poids ajustés aux données (p. 1, 2, 4, 53). Pour (ii) tel que la note d'englobement le définit, **non** : les membres ne sont pas les lois de l'archive, et la mise en commun n'est pas un nul. La forme seule est occupée, ici et dans la littérature que l'auteur cite (p. 2, 3, 13).
2. **Les propositions sont-elles jugées contre des modèles connus ou une archive ?** **Non**, dans le texte lu : contre les autres propositions du tirage (poids relatifs, p. 3, 8 ; dans un cas, deux modèles mieux notés sont mis en minorité : « they are essentially “outvoted” in the posterior by lower-scoring but more numerous models », p. 19), et la sortie est comparée à la moyenne plate des mêmes propositions (p. 3, 5-7, 15-44). Les modèles connus sont écartés à dessein (p. 5).
3. **Règle de promotion ? Test ? Validité à tout instant d'arrêt ?** **Aucune** ; aucun test ; aucune validité séquentielle (section 2). Seuls filtres : compilation et chaîne interdite (p. 4, 54).
4. **Engagement avant les données ?** **Non** au sens de (iv-a) : lois fixées sans les valeurs par définition (p. 2, 4), mais données préexistantes et rien de scellé ; précaution de mémoire d'entraînement seulement (p. 5).
5. **Calcul hors du modèle de langue ?** **Oui** pour la statistique (p. 53, 63) ; mais la loi notée est écrite par le modèle de langue, qui peut fausser la normalisation (p. 54).

## 5. Table de la pièce

| composante | LLB (arXiv 2504.14025 v2) | pages |
|---|---|---|
| **P** | **voisin (lointain)** : jugement relatif entre propositions du même tirage par la vraisemblance marginale ; ni *aucun effet* ni le connu ; connu écarté à dessein | 3, 5, 19 |
| **(i)** | **pris** : un modèle de langue propose des lois probabilistes complètes | 1, 2, 53 |
| **(ii)** | **voisin (proche pour l'opérateur)** : moyenne bayésienne des lois des propositions, pondérée par les données ; **sans archive, sans rôle de nul** | 1, 2, 3, 13 |
| **(iii)** | **non trouvé** : poids doux, aucun test, aucun seuil, aucun arrêt | 4, 54 ; termes : section 2 |
| **(iv-a)** | **voisin (lointain)** : lois fixées sans les valeurs par définition ; données préexistantes ; rien de scellé | 2, 4, 5 |
| **(iv-b)** | **pris** pour la statistique ; sans objet pour la promotion ; la loi notée est écrite par le proposeur (normalisation gardée en partie) | 53, 54, 63 |
| **conjonction** | **non trouvée** | — |

## 6. Nœuds pour Lazar (décisions à prendre ; rien n'est déclaré libre)

Le verdict en vigueur sur O4 reste **occupée en partie** ; seul Lazar le change. Les options prudentes (R4) sont indiquées ; elles ne sont pas des conclusions.

1. **LLB dans la note d'englobement.** Porter LLB comme pièce qui **prend (i)** et **occupe l'opérateur de (ii)** pour des lois proposées par un modèle de langue (moyenne pondérée par la vraisemblance marginale), sans archive ni nul, sans (iii), sans scellement. Option prudente : l'ajouter, et l'ajouter aux citations obligatoires de O4 (N-067) pour toute phrase publique qui décrit la mise en commun.
2. **Lettre de (ii) dans l'énoncé de O4.** La *mise en commun ajustée de lois prédictives*, dite seule, est publiée (LLB, p. 1-2 ; et la moyenne bayésienne de modèles qu'elle cite, p. 13, non lue). Ce qui reste non trouvé tient à **la composition** (lois de l'archive : connues et survivantes promues) et **au rôle** (nul à battre, non loi rendue). Option prudente : ne revendiquer ni l'opérateur ni la pondération par les données ; dire *mise en commun, à la manière d'une moyenne de modèles, des lois de l'archive, employée comme nul*, avec citation de LLB et de la littérature de la moyenne bayésienne. Décider aussi s'il faut faire lire [16], [18], [32] avant toute phrase publique sur la forme des poids.
3. **Distance sur (iii), remarque de lecteur non opposable (R7).** Le rapport des vraisemblances marginales entre une proposition et une loi de référence est un facteur de Bayes ; qu'un tel rapport, sous une loi nulle simple, soit une e-valeur est un fait de la littérature des e-valeurs que je **n'ai pas vérifié sur une source dans cette session**. Si c'est vrai, la distance entre la mécanique de LLB et (iii) est courte : opposer la vraisemblance marginale d'une proposition à celle d'une mise en commun d'archive. Décider s'il faut le faire vérifier (pièces déjà au dépôt : Choe et Ramdas, Henzi et Ziegel, Ma et al.) et s'il faut dire, dans l'énoncé, que la nouveauté éventuelle n'est pas la statistique mais son nul, son engagement scellé et sa garantie d'erreur (rejoint le nœud 10 de la v3).
4. **Réserve sur notre (iv-b).** LLB montre qu'une statistique calculée hors du proposeur ne protège pas quand **la loi notée est écrite par le proposeur** (densité non normalisée, p. 54). Décider s'il faut faire vérifier, dans notre mise en œuvre, que les lois scellées des fiches sont des densités normalisées (contrôle par programme, non par échantillon à la main), et s'il faut citer LLB pour cette réserve dans la forme du banc de tricheurs (N-064).
5. **Incohérence interne de la pièce.** Le problème de la pluie donne « Out of 1024 generated models, 960 (93.8%) compiled and allowed for inference. » (p. 6) et « Out of 1024 models generated, 742 (72.5%) compiled and allowed for inference. » (p. 15). Sans effet sur les statuts ; si un chiffre de LLB est cité, ne citer ni l'un ni l'autre sans le signaler.
6. **Pistes nommées par LLB, non lues.** Pour (ii) : [16] Hoeting et al. 1999, [32] Wasserman 2000, [18] Kejzlar et al. 2023 (moyenne bayésienne de modèles, dont une variante variationnelle en boîte noire). Pour (i) : [28] Requeima et al. 2024 (« Requeima et al. [28] suggest a scheme to make probabilistic prediction from natural language plus data. », p. 10), [33] Wong et al. 2023, [6] Choi et al. 2022, [4] Capstick et al. 2024, [29] Selby et al. 2024. Aucune n'est désignée par LLB comme test ou règle de promotion. Option prudente : lire [18] et [28] si (ii) ou (i) sont dits dans un énoncé public ; AutoDiscovery (nœud 9 de la v3) reste non lue.

## 7. Ce qui reste non lu

- Les **références** de la pièce, toutes (titres seulement, p. 11-13) ; en particulier [16], [18], [32] pour l'opérateur de (ii), et [28], [33] pour (i).
- Le **code Stan** des modèles d'exemple (annexe B, fig. 7 à 47) et des sorties d'exemple (annexe G), parcouru, non lu ligne à ligne ; les **valeurs des figures** ; la **vérification mathématique** des preuves (annexe E).
- La **version v1** d'arXiv et la **version de la conférence** : seule la v2 est lue ; les écarts ne sont pas connus.
- Le **code** : aucun lu (consigne) ; la pièce déclare : « It is difficult to provide code runnable by a third party given the usage of a local cluster and many non-portable modifications. » (p. 61). Je n'ai pas cherché de clone.
- Le fichier `provenance-v1.md` du dossier de la pièce (non nommé par la consigne).
- Rien de cette lecture ne porte sur les autres pistes de priorité haute (AutoDiscovery, *Assaying Anomalies*, Manning et al., Chen et Dim, Chen, Lopez-Lira et Zimmermann).

## 8. Incidents

- Aucun refus de permission, de crochet ou de classifieur. Aucune dépense, aucun accès réseau, aucun clone ouvert, aucun programme tiers lancé.
- Une première boucle de recherche de termes, lancée hors du dossier des pages, n'a rien trouvé faute de fichiers (erreur de chemin de ma part) ; refaite par un programme sur le texte entier, ce sont ces résultats qui sont rapportés (section 2).
- `pdftotext` rend 64 segments pour 63 pages (le dernier est vide, après le saut de page final) : sans effet sur la numérotation.
- Incohérence interne de la pièce sur le problème de la pluie (nœud 5).
