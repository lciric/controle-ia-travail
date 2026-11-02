# Proposition B — Boucle itérative moisson ↔ fiches ↔ bisociateur

## (a) Ce que la question suppose sans que ce soit établi

Chaque présupposé est accompagné de son statut tiré des faits servis.

**P1 — « Un embryon d'idée peut déclencher une moisson ciblée utile. »**
Statut : **HYPOTHÈSE**. Le moissonneur est CODÉ avec relais factice (v47, 444 essais sur 444), mais aucune moisson réelle par ce module n'a été exécutée (§ 2 : « relais réel, épreuve courte, première moisson réelle par ce module : aucune trace trouvée »). La moisson en vrac OpenAlex (197 681 œuvres) est distincte et ne passe pas par le relais du moissonneur. Aucune donnée ne montre qu'une requête dérivée d'une fiche ramène des résultats qui améliorent la fiche.

**P2 — « Le gain de nouveauté entre deux versions d'une fiche est mesurable. »**
Statut : **HYPOTHÈSE**. Aucune métrique de « progrès entre deux versions » d'une fiche n'est définie dans les faits servis. Le format d'une fiche (§ 3.2) contient des champs structurés (hypothèse, prédiction chiffrée, antériorités, critère de mort, vis-à-vis), mais aucune fonction de distance ou de gain n'est codée, testée, ni même spécifiée pour comparer deux versions successives.

**P3 — « Apparier fiches et articles avec les trois bras existants est faisable et utile. »**
Statut : **HYPOTHÈSE**. Les trois bras (basique, Gu-Krenn, méta) sont conçus pour apparier fiche–fiche. Le bras basique utilise des indicateurs d'axe et des étiquettes de concept posées par deux lecteurs sur des fiches (§ 7.1). Le bras Gu-Krenn utilise un vocabulaire de 37 960 concepts d'optique/physique quantique, absent du domaine du contrôle de l'IA (§ 7.2, couverture : § 5 de la pièce 3). Le bras méta utilise 6 niches et 20 structures nommées à la main (§ 7.3). Rien de cela n'est défini pour des articles moissonnés. L'épreuve du bras basique sur mondes inventés est « non concluante » (§ 7.1, verdict V5 faux).

**P4 — « La rétrodiction à date de coupure sur OpenAlex est un test valide pour des idées de méthode en contrôle de l'IA. »**
Statut : **HYPOTHÈSE**. La rétrodiction de Swanson (pièce 2) mesure la cooccurrence lexicale future sur arXiv (termes, pas concepts), dans un corpus dominé par la physique (74 %). Elle ne dit rien sur les idées de méthode. La pièce 2 le reconnaît : « L'issue mesurée est la cooccurrence lexicale future, pas une découverte féconde. » Le contrôle de l'IA est un champ jeune où la littérature est mince — le taux de base et la couverture conceptuelle seraient très différents.

**P5 — « L'allocation par bandit entre embryons est réalisable avec le gain de nouveauté comme signal. »**
Statut : **HYPOTHÈSE**. Aucun signal de « gain de nouveauté » n'est défini. Le bandit suppose un signal numérique par tour et par bras ; sans définition opérationnelle, la formulation est vide.

**P6 — « Les essais de la mémoire (pistes 1-3) s'étendent à la boucle moisson ↔ fiches. »**
Statut : **OBSERVÉ-NON-AUDITÉ** pour les essais eux-mêmes (mondes synthétiques, proposeur scripté), **HYPOTHÈSE** pour l'extension. Les essais montrent que la mémoire aide « si et seulement si les vraies associations se regroupent dans l'espace où le proposeur mesure la proximité » (pièce 4b). La piste 3 note explicitement : « Ne dit pas que la vérité se regroupe dans le monde réel. C'est la condition à vérifier sur données réelles. »

**P7 — « Gu et Krenn peut être repris 'tel quel' pour cette boucle. »**
Statut : contredit par les faits. Décision de Lazar : « on garde Gu-Krenn tel quel dès que c'est possible sans recoder nous-mêmes ». Or la pièce 3 (§ 5) montre que leur vocabulaire ne couvre pas le contrôle de l'IA. Aucun poids entraîné n'est publié (§ 3). Le substitut maison (§ 7.2) est SUPPOSÉ, conditionné à un seuil S31 non testé, et renvoie au collisionneur (D-j, nœud N3). « Tel quel » est donc impossible pour le domaine visé ; seule la méthode est transférable, ce qui revient à « recoder ».

**P8 — « Les tests de mort et le pôle peuvent valider les idées issues de la boucle. »**
Statut : **CODÉ NON ACTIVÉ** pour les tests de mort (v48-v56, jamais activés, § 9.2). La « prise idéation » (traduction fiche → loi prédictive testable) est **conçue, non construite** (§ 1.1). Le pôle a tourné sur un monde tautologique et une banque réelle sans résultat (« pas de dents », § 9.4.A.3). Aucune fiche de course n'est devenue une hypothèse testée (§ 10).

---

## (b) Expériences décisives

### Exp. 1 — La moisson ciblée apporte-t-elle de l'information absente de la fiche ?

**H_A** : Une requête dérivée des concepts et trous nommés d'une fiche retourne au moins une œuvre dont le résumé contient une information pertinente (antériorité, mécanisme, donnée) absente de la fiche et de ses antériorités citées, dans ≥ 50 % des fiches traitées.

**H_B** : La moisson ciblée retourne majoritairement du bruit (< 50 % des fiches enrichies) : les requêtes dérivées ramènent soit ce que la fiche cite déjà, soit des résultats non pertinents.

- **Métrique** : Taux d'enrichissement = nombre de fiches pour lesquelles au moins un résumé moisson contient ≥ 1 élément nouveau pertinent (jugé par un lecteur neuf qui voit la fiche avant et après), divisé par le nombre de fiches traitées.
- **Seuil** : 0,50. H_A retenue si taux ≥ 0,50 ; H_B retenue si taux < 0,50.
- **Contrôle négatif** : Moisson avec des requêtes tirées au hasard parmi les termes du vocabulaire (même nombre de requêtes, même quota de résultats). Si le contrôle atteint aussi ≥ 0,50, la moisson ciblée ne se distingue pas du bruit et H_A est falsifiée quand même.
- **Matériau** : 20 fiches de la course 1 (29 fiches validées, 27 éligibles, § 10), relais réel du moissonneur, arXiv et OpenAlex, métadonnées et résumés seulement. Lecteur neuf : un modèle distinct des proposeurs et juges (e.g. Opus 5.5 si non proposeur, sinon Fable 5.1).
- **Ce qui falsifie H_A** : taux < 0,50 ou taux du contrôle ≥ taux ciblé.
- **Ce qui falsifie H_B** : taux ≥ 0,50 et taux du contrôle < taux − 0,15 (marge de supériorité).

### Exp. 2 — L'affinement itératif produit-il un progrès mesurable ou une reformulation ?

**H_A** : Après k tours de moisson + affinement (k = 3), la version finale d'une fiche couvre strictement plus d'antériorités vérifiées, nomme un mécanisme plus précis (mesuré par le nombre de champs remplis et de prédictions chiffrées ajoutées), et ne régresse sur aucun champ, dans ≥ 60 % des fiches.

**H_B** : L'affinement ne fait que reformuler : la version finale ne couvre pas plus d'antériorités vérifiées, ou régresse sur un champ, dans > 40 % des fiches.

- **Métrique** : Δ_champs = (champs_remplis_v_finale − champs_remplis_v_initiale) ; Δ_antériorités = (antériorités_vérifiées_v_finale − antériorités_vérifiées_v_initiale) ; Δ_prédictions = idem. Progrès si les trois Δ ≥ 0 et au moins un > 0. Taux de progrès = fiches en progrès / fiches traitées.
- **Seuil** : 0,60.
- **Contrôle négatif** : Affinement sans moisson (le proposeur réécrit la fiche 3 fois à partir de la même information). Si le contrôle atteint le même taux, la moisson n'est pas la cause du progrès.
- **Ce qui falsifie H_A** : taux < 0,60, ou contrôle sans moisson ≥ taux avec moisson.
- **Ce qui falsifie H_B** : taux ≥ 0,60 et contrôle sans moisson < taux − 0,10.

### Exp. 3 — L'appariement élargi (fiche–article) sélectionne-t-il des paires plus fertiles que le hasard ?

**H_A** : Les paires fiche–article sélectionnées par le bras basique adapté (Jaccard des concepts sur les résumés, domaine = axe de la fiche vs. champ de l'article) ont un taux de fusion jugée « notable » par les juges-modèles (Kimi ⇄ Argon croisés, Opus 5.5) supérieur de ≥ 10 points de pourcentage à celui des paires tirées au hasard.

**H_B** : L'écart est < 10 points : le vivier élargi noie les fiches, et les paires sélectionnées ne sont pas plus fertiles que des paires aléatoires.

- **Métrique** : Taux de « notable » = fusions jugées notables / fusions totales, sur chaque bras.
- **Seuil** : 10 points de pourcentage d'écart.
- **Contrôle négatif** : 24 paires fiche–article tirées au hasard (même nombre que les 24 fusions prévues en course 2, § 7.4), fusionnées par Kimi sous la même consigne figée, jugées à l'aveugle.
- **Ce qui falsifie H_A** : écart < 10 points.
- **Ce qui falsifie H_B** : écart ≥ 10 points, avec les paires hasard < 15 % de notables (le contrôle doit avoir des dents).
- **Réserve** : avec 24 fusions par bras, l'intervalle de confiance sur un taux sera large (Wilson à 95 % ≈ ±20 points pour un taux de 50 %). À signaler dans le préenregistrement. Le test peut revenir « non concluant ».

### Exp. 4 — La rétrodiction à date de coupure est-elle valide pour le contrôle de l'IA ?

**H_A** : Sur OpenAlex/arXiv avec coupure à fin 2022, le taux de base de nouvelles cooccurrences (paires de concepts qui apparaissent ensemble pour la première fois en 2023-2025) dans le domaine cs.AI/cs.LG/cs.CR est ≥ 0,1 % des paires candidates, et au moins deux des trois méthodes de base (allocation de ressources, Adamic-Adar, Swanson) dépassent un tirage stratifié de ≥ 5 points de précision à 10 000 — le test a des dents.

**H_B** : Le taux de base est < 0,1 % ou aucune méthode de base ne dépasse +5 points — le champ est trop jeune ou trop petit pour que la rétrodiction lexicale distingue quoi que ce soit.

- **Métrique** : Taux de base (Wilson), précision à 10 000 par méthode, écart avec le tirage stratifié.
- **Seuil** : Taux de base ≥ 0,1 % ET au moins deux méthodes à ≥ +5 points.
- **Contrôle négatif** : Permutations des issues (20 permutations), comme dans la rétrodiction de Swanson (pièce 2, contrôle (a)).
- **Fuite à fermer** : Les modèles de langage utilisés comme proposeurs ont été entraînés après la coupure. Le test de rétrodiction ne doit utiliser que des méthodes de graphe (allocation de ressources, etc.), jamais un modèle de langage pour prédire les paires. Sinon le test est circulaire.
- **Ce qui falsifie H_A** : taux de base < 0,1 % ou < 2 méthodes à ≥ +5 points.
- **Ce qui falsifie H_B** : taux de base ≥ 0,1 % et ≥ 2 méthodes à ≥ +5 points.

### Exp. 5 — La boucle tourne-t-elle en rond ?

**H_A** : Après k = 5 tours, l'entropie de Shannon des concepts présents dans les fiches actives décroît de ≥ 20 % par rapport au tour 1 (convergence thématique, boucle qui tourne en rond).

**H_B** : L'entropie reste à ± 20 % du tour 1 ou augmente — la douane et la diversification maintiennent l'exploration.

- **Métrique** : H(concepts au tour t) / H(concepts au tour 1), où H est l'entropie de Shannon sur la distribution des étiquettes de concept dans les fiches actives.
- **Seuil** : 0,80 (baisse de 20 %).
- **Contrôle négatif** : Boucle sans douane (pas de filtre anti-redite, pas de garde de diversité). Si la boucle sans douane ne converge pas non plus, le test n'a pas de dents.
- **Ce qui falsifie H_A** : ratio > 0,80 (pas de convergence excessive).
- **Ce qui falsifie H_B** : ratio ≤ 0,80 (convergence confirmée), et le contrôle sans douane converge aussi (la douane ne protège pas).

---

## (c) Mesures minimales de fonctionnement de chaque instrument nommé

### c1 — Moissonneur (relais réel, arXiv + OpenAlex)

- **Taux de détection** : sur 20 fiches dont les antériorités sont connues (fiches de la course 1 avec les 23 papiers du dossier fermé comme vérité), la moisson ciblée retrouve ≥ 3 des 5 antériorités déclarées (ou un résultat plus récent du même groupe) dans ≥ 60 % des fiches.
- **Taux de fausses alertes** : sur les mêmes 20 fiches, la moisson retourne < 30 % de résultats jugés non pertinents par un lecteur neuf (résumé sans rapport avec l'hypothèse ni les données de la fiche).
- **Cas honnêtes appariés** : 10 fiches d'axes bien couverts (axes 1, 3) et 10 fiches d'axes maigres (axe 7, axe 2) — les taux sont rapportés séparément.
- **Vérification mécanique à battre** : recherche par mots-clés bruts (les 5 premiers mots du titre de la fiche, sans transformation) sur les mêmes API, mêmes quotas. Le moissonneur ciblé doit dépasser cette base de ≥ 15 points de taux de détection.

### c2 — Bisociateur (bras basique adapté au format fiche–article)

- **Taux de détection** : sur un lot de 40 paires dont 10 sont des paires « fertiles » plantées (une fiche et un article dont la combinaison fait émerger un mécanisme absent des deux, vérifié par un lecteur neuf), le bras sélectionne ≥ 7 des 10 fertiles dans ses 20 meilleures paires.
- **Taux de fausses alertes** : ≤ 15 des 20 meilleures sont non fertiles (≤ 75 % de faux positifs dans le top 20).
- **Cas honnêtes appariés** : 30 paires non fertiles sont tirées au hasard parmi les mêmes fiches et articles, en appariant les axes (même distribution d'axes que les 10 fertiles).
- **Vérification mécanique à battre** : Jaccard brut des mots du titre de la fiche et du titre de l'article (pas de concept structuré). Le bras adapté doit placer ≥ 2 fertiles de plus dans le top 20.

### c3 — Mémoire anti-redite (signature brute, seuil de fusion)

Déjà éprouvée (piste 1, pièce 4a). Mesure minimale résiduelle :
- **Taux de détection** : sur 200 paires (dont 100 paraphrases plantées), fausses fusions réalisées ≤ 5 % à un seuil de 5 % de fausses fusions (VÉRIFIÉ, pièce 4a : 0,000 pour paraphrase, copie renommée, jargon rare, changement d'échelle).
- **À vérifier sur des fiches réelles** : les essais utilisent des lois softmax synthétiques à deux traits. Le test minimal sur fiches réelles = 50 paires de fiches de la course 1 (17 idées distinctes, 12 paires de doublons, § 10) : la mémoire doit identifier ≥ 10 des 12 paires de doublons sans déclencher plus de 2 fausses fusions sur les 38 paires non-doublons.

### c4 — Garde de fuite (requêtes du moissonneur)

- **Taux de détection** : sur 50 requêtes dont 10 contiennent un texte de test ou un identifiant d'épisode (plantés, formats réalistes), la garde bloque les 10 (100 %, tolérance 0 — c'est une garde de sécurité, pas un classifieur statistique).
- **Taux de fausses alertes** : sur les 40 requêtes légitimes, la garde en bloque ≤ 2 (≤ 5 %).
- **Vérification mécanique** : recherche par expression régulière des formats d'identifiants connus. La garde doit attraper ≥ les mêmes 10 que l'expression régulière (elle peut attraper plus, mais pas moins).

### c5 — Tests de mort (bac à sable, machine jetable)

Statut : CODÉ NON ACTIVÉ. Mesure minimale avant activation :
- **Cas honnête** : 5 fiches dont la prédiction est vraie (simulée : la fiche prédit un fait calculable), 5 fiches dont la prédiction est fausse. Le bac exécute le script, lit RESULTAT:, applique le seuil gelé.
- **Taux de détection** : ≥ 4/5 vraies survivent, ≥ 4/5 fausses éliminées.
- **Taux de fausses alertes** : ≤ 1/5 vraie éliminée à tort.
- **Vérification mécanique** : un humain exécute le même script hors bac, vérifie RESULTAT:, compare. Accord ≥ 9/10.
- **Sécurité** : aucun accès superutilisateur de l'hôte (CL13, CL14 signalaient cette voie). Test = essayer `sudo`, `nsenter`, montage de `/proc/1/root` depuis le bac — les trois doivent échouer.

---

## (d) Ancrage matériel

### Modèles ouverts nécessaires

- **Proposeurs** (course 2) : Kimi K3.1 Pro (Moonshot, API payante) et Argon (Google/Gemini, API payante). Ni l'un ni l'autre n'est à poids ouverts.
- **Gu-Krenn — substitut** : le réseau entièrement connecté (4 couches de 600, ≈ 1,2 million de paramètres) est de taille triviale ; c'est la reconstruction du graphe et des traits qui coûte. Aucun modèle à poids ouverts requis pour cela, mais une machine avec ≥ 64 Go de mémoire (I-7, pièce 3).
- **Extension au domaine IA** : nécessite de relancer la chaîne RAKE sur arXiv cs.LG/cs.AI/cs.CL/cs.CR/stat.ML. RAKE est une bibliothèque ouverte (rake-nltk). Le réseau est entraînable sur processeur (banc d'essai : ≈ 1 h par tâche, pièce 3 § 2).

### Calcul nécessaire

| Composant | Ressource | Coût estimé | Statut |
|---|---|---|---|
| Moissonneur réel (relais, 20 fiches × 4 requêtes × 5 résultats) | API arXiv (gratuit) + OpenAlex (0,0001 $/page) | ≈ 0,10 $ (illustratif) | À lancer |
| Course 2 (128 fiches, 24 fusions, juges) | API Kimi + Argon + Opus 5.5 | ≈ 40–60 $ (illustratif, basé sur le coût de la course 1 : 37 $, § 10, avec plus de fiches) | Pré-pilote en attente |
| Rétrodiction domaine IA (Exp. 4) | Processeur, 4 cœurs, 15 Go | ≈ 0 $ (sur machine existante si corpus ≤ 1M documents) | Dépend de l'extraction du corpus |
| Reproduction Gu-Krenn, voie R-a (banc) | Machine louée, ≥ 16 Go mémoire, processeur | ≈ 1–5 $ (illustratif, 1 h de calcul sur machine louée) | Devis non écrit |
| Reproduction Gu-Krenn, voie R-b (expérience principale) | Machine louée, ≥ 64 Go mémoire, disque ≥ 100 Go, processeur ou carte graphique | ≈ 5–30 $ (illustratif, 8-30 h processeur ou 1,5 h carte graphique par IR) | Devis non écrit |
| Moisson OpenAlex 2023-2025 (test hors échantillon Gu-Krenn) | Allocation gratuite 1 $/jour ou API payante, ≥ 5 $ sur ≥ 1 semaine ; OU instantané public 744 Go | ≈ 5–20 $ (illustratif) | Non lancé |
| Tests de mort (bac à sable, machine jetable) | Machine jetable sans secret, 1 cœur | ≈ 0,50–2 $ par fiche (illustratif, 3 exécutions × 120 s) | CODÉ NON ACTIVÉ |
| Essais Exp. 1-5 combinés | API des proposeurs + lecteurs neufs, ≈ 100 fiches traitées | ≈ 20–40 $ (illustratif) | Rien lancé |

### Séquencement imposé par les dépendances

1. **D'abord** : Exp. 4 (rétrodiction domaine IA) — si H_B est retenue (champ trop jeune), toute la composante rétrodiction de la boucle est invalide pour ce domaine. Coût quasi nul.
2. **Ensuite** : Exp. 1 (moisson ciblée utile ?) — si H_B est retenue, la boucle moisson ↔ fiches n'a pas de raison d'être. Coût ≈ 5 $.
3. **Ensuite** : Exp. 2 (affinement vs. reformulation) et Exp. 3 (appariement élargi), en parallèle.
4. **Dernier** : Exp. 5 (convergence) — ne peut tourner que quand la boucle existe.

### Sur Q7 (ordre : boucle avant ou après la course 2 ?)

Les faits tranchent : la course 2 attend un pré-pilote (§ 1.2, § 7.4), le moissonneur n'a jamais servi en course (§ 2), la prise idéation n'est pas construite (§ 1.1), les tests de mort ne sont pas activés (§ 9.2). Construire la boucle complète avant la course 2 bloque tout. L'option qui préserve l'information est :

- Course 2 **sans** la boucle moisson ↔ fiches (comme prévu, moissonneur en option « aucune »), en activant les tests de mort sur une machine jetable (décidés mais non activés).
- En parallèle, lancer Exp. 1 et Exp. 4 pour savoir si la boucle a un fondement.
- La boucle ne serait construite qu'en génération 2, si et seulement si Exp. 1 et Exp. 4 retiennent H_A.

Cet ordre est un avis, pas un fait.

FIN-DE-CELLULE