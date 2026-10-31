# Proposition B — L'apprentissage profond peut-il identifier à lui seul les paramètres qui créent la fertilité ?

---

## (a) Ce que la question suppose sans que ce soit établi

Je liste chaque présupposé implicite de la question ou des pièces, avec son statut.

| # | Présupposé | Statut | Commentaire |
|---|---|---|---|
| P1 | Il existe des « paramètres qui créent la fertilité » distincts de ceux qui l'accompagnent, et ils sont récupérables dans les données de citations. | HYPOTHÈSE | C'est le cœur du programme. Rien n'établit qu'un petit nombre de variables latentes *cause* la fertilité plutôt qu'un réseau dense de causes faibles et contextuelles. |
| P2 | La fertilité d'un croisement est mesurable indépendamment du traitement (contact entre niches). | HYPOTHÈSE | La pièce `relecture-fable-reponse-5-v1.md` (RL5-13) note que les proxys (citations, reprise) ont leurs propres causes (effet Matthieu, visibilité). Aucun proxy validé n'est fourni. |
| P3 | L'ordre temporel des citations fournit « gratuitement » la condition auxiliaire requise par les théorèmes d'identifiabilité (Hyvärinen & Morioka 2016, Khemakhem et al. 2020). | HYPOTHÈSE | L'ordre temporel fournit une *variable auxiliaire* (le temps), mais les théorèmes exigent que le mécanisme génératif conditionné à cette variable satisfasse une non-stationnarité *suffisante* de la distribution des sources latentes. Que les citations scientométriques présentent cette non-stationnarité sous la forme requise (changements par segment, variation exponentielle des paramètres) n'est pas vérifié. |
| P4 | Les sous-domaines, décennies et pays constituent des « environnements » au sens de la prédiction causale invariante (Peters, Bühlmann, Meinshausen 2016 — SUPPOSÉ). | HYPOTHÈSE | La relecture (RL5-17) observe que le mécanisme causal lui-même change entre décennies (pratiques de citation, taille des équipes, pression à publier). Si le mécanisme causal varie entre environnements, la prédiction invariante rejette les variables causales au lieu de les retenir. Aucune vérification n'est faite. |
| P5 | Le démêlage non supervisé est impossible sans hypothèse (Locatello et al. 2019, SUPPOSÉ). | RAPPORTÉ — la pièce conv-audit Q6 l'affirme. Le théorème d'impossibilité porte sur le démêlage dans un auto-encodeur variationnel standard ; il ne couvre pas les modèles à variable auxiliaire ou à contrainte temporelle, ce que la même pièce reconnaît ensuite. L'affirmation est donc correcte mais sa portée est souvent surestimée. |
| P6 | Les « courses » de l'organisme (paires randomisées, dose de contact contrôlée) permettent d'identifier l'effet causal de la dose sur la fertilité. | HYPOTHÈSE | L'identification est valide *dans le monde de la course*, avec les agents et juges de la course. Le transport vers la science réelle (Pearl & Bareinboim 2014 — SUPPOSÉ) nécessite que les mécanismes reliant dose, confondeurs et fertilité soient les mêmes dans les deux mondes, ce qui n'est ni établi ni même discuté dans les pièces (RL5-11). |
| P7 | La non-gaussianité du bruit dans les données de citations permet la découverte de structure par LiNGAM (Shimizu et al. 2006 — SUPPOSÉ). | HYPOTHÈSE | LiNGAM exige un modèle linéaire avec bruit additif non gaussien et acyclique. Un graphe de citations est massivement non linéaire, cyclique à l'échelle des niches (A cite B, B cite A via un intermédiaire), et la distribution des citations (loi de puissance) ne garantit pas que les *résidus* après régression linéaire restent non gaussiens de manière informationnelle. |
| P8 | Un score de recouvrement (MCC, R², corrélation de permutation) sur des mondes inventés valide la méthode pour les données réelles. | HYPOTHÈSE | Un monde inventé ne valide la méthode que si son mécanisme génératif est assez proche du mécanisme réel. Or nous ne connaissons pas le mécanisme réel — c'est précisément ce que nous cherchons. Le test sur monde inventé détecte les échecs grossiers, il ne peut pas confirmer. |

---

## (b) Expériences décisives — duels H_A / H_B

Je propose cinq expériences, chacune en duel falsifiable.

### Expérience 1 — Le démêlage non supervisé retrouve-t-il les causes plantées ?

**H_A** : Un auto-encodeur variationnel (VAE) avec variable auxiliaire temporelle (iVAE, Khemakhem et al. 2020 — SUPPOSÉ) retrouve les facteurs causaux plantés dans un monde inventé avec un score de recouvrement MCC ≥ 0.7 et les distingue des facteurs purement accompagnateurs (MCC de ceux-ci ≤ 0.3).

**H_B** : Le même modèle ne sépare pas causes et accompagnateurs (MCC des deux groupes indiscernables, test de permutation p > 0.05).

- **Métrique** : coefficient de corrélation de Matthews (MCC) entre chaque latente apprise et chaque latente vraie, après appariement hongrois.
- **Seuil** : MCC ≥ 0.7 (causes) et MCC ≤ 0.3 (accompagnateurs), préenregistrés.
- **Contrôle négatif** : un facteur planté sans lien causal avec la fertilité mais corrélé par un confondeur commun (prestige). Si le modèle lui attribue un MCC > 0.3, il ne distingue pas cause et accompagnateur — H_A est falsifiée même si le MCC des vrais causaux est élevé.
- **Falsification** : H_A est morte si le contrôle négatif est recouvré aussi bien que les causes. H_B est morte si les causes plantées sont retrouvées et le contrôle négatif rejeté de façon stable sur ≥ 5 graines aléatoires.

### Expérience 2 — L'invariance entre environnements isole-t-elle des paramètres causaux sur données scientométriques ?

**H_A** : La prédiction causale invariante (ICP, Peters et al. 2016 — SUPPOSÉ), appliquée aux données OpenAlex découpées en environnements (sous-domaines), retient un ensemble S* non vide de paramètres, et S* prédit la fertilité dans un environnement tenu à l'écart (décennie ou pays jamais vu) avec une erreur ≤ 1.2× celle du meilleur modèle prédictif non contraint.

**H_B** : ICP retient l'ensemble vide (aucun paramètre n'est invariant) ou un ensemble S* dont l'erreur prédictive hors environnement est > 1.5× celle du modèle non contraint — signe que l'hypothèse d'invariance est violée.

- **Métrique** : erreur quadratique moyenne normalisée (NRMSE) sur l'environnement tenu à l'écart.
- **Seuil** : ratio NRMSE(ICP) / NRMSE(prédictif) ≤ 1.2 pour H_A, > 1.5 pour H_B. Zone 1.2–1.5 = indéterminé, augmenter les environnements.
- **Contrôle négatif** : appliquer ICP avec des environnements fictifs (découpage alphabétique des noms d'auteurs). Si S* est le même qu'avec les vrais environnements, l'invariance trouvée est un artefact — H_A falsifiée.
- **Falsification** : H_A est morte si S* = ∅ ou si le ratio dépasse 1.5 ou si le contrôle négatif passe. H_B est morte si ICP retient un ensemble non vide, prédictif hors échantillon, rejeté par le contrôle négatif alphabétique.

### Expérience 3 — Le modèle non supervisé prédit-il l'effet d'une intervention jamais vue dans la course ?

**H_A** : Les paramètres latents identifiés par iVAE (ou par un autre modèle à variable auxiliaire) sur les courses passées permettent de prédire le *signe* et l'*ordre de grandeur* (facteur 2) de l'effet d'une nouvelle dose de contact (jamais testée) sur la fertilité mesurée par un juge figé indépendant.

**H_B** : La prédiction échoue (signe opposé, ou effet observé hors de l'intervalle [prédiction/2, prédiction×2]).

- **Métrique** : signe de l'effet (concordance binaire) et ratio effet observé / effet prédit.
- **Seuil** : concordance du signe sur ≥ 4/5 interventions nouvelles, ratio dans [0.5, 2.0].
- **Contrôle négatif** : prédiction d'une dose connue pour n'avoir aucun effet théorique (par exemple, donner aux deux niches des titres de la *même* niche — pas de croisement). Si le modèle prédit un effet non nul, il hallucine — H_A est falsifiée.
- **Falsification** : H_A est morte si le signe est incorrect sur ≥ 2/5 ou si le contrôle négatif montre un effet. H_B est morte si les 5 prédictions sont dans la fourchette et le contrôle négatif renvoie zéro.
- **Remarque critique** : cette expérience teste *l'estimation* plus que *l'identification à lui seul*. Si un modèle purement prédictif (XGBoost sur les mêmes features, sans structure causale) fait aussi bien, alors la structure causale n'ajoute rien — critère supplémentaire emprunté à RL5-08 : le modèle causal doit battre le modèle prédictif d'au moins ε = 10 % (illustratif) en ratio moyen.

### Expérience 4 — Les facteurs « appris en pratique » sont-ils stables entre graines et données ?

**H_A** : Un VAE entraîné sur le graphe de citations d'OpenAlex (sous-domaine fixé, 2000–2020) retrouve les mêmes k premières composantes (à permutation et signe près) sur 10 graines aléatoires et sur deux moitiés aléatoires des données (corrélation de Spearman ≥ 0.8 après appariement hongrois).

**H_B** : Les composantes changent d'une graine à l'autre (corrélation de Spearman < 0.5 pour ≥ 3 composantes sur k).

- **Métrique** : corrélation de Spearman moyenne entre composantes appariées.
- **Seuil** : ≥ 0.8 (H_A), < 0.5 pour ≥ 3/k (H_B).
- **Contrôle négatif** : ACP linéaire sur les mêmes données — si le VAE n'est pas plus stable que l'ACP, le non-linéaire n'ajoute rien.
- **Falsification** : H_A est morte si instable. H_B est morte si stable et si le VAE surpasse l'ACP en stabilité et en corrélation avec des attributs connus (taille, âge, prestige — ces attributs servent de *diagnostic*, pas de preuve de causalité).

### Expérience 5 — Transport : la cause identifiée dans la course vaut-elle dans la science réelle ?

**H_A** : L'effet causal de la dose de contact, estimé dans les courses randomisées, prédit le signe de l'effet d'une expérience naturelle indépendante (par exemple : un déménagement à la Catalini 2018 — SUPPOSÉ — rapproche deux groupes de niches distinctes ; la fertilité entre ces niches augmente-t-elle ?).

**H_B** : Le signe observé dans l'expérience naturelle est opposé à celui estimé dans la course, ou l'effet est nul (intervalle de confiance à 95 % couvrant zéro).

- **Métrique** : signe de l'effet et p-value bilatérale.
- **Seuil** : concordance du signe, p < 0.05 côté expérience naturelle.
- **Contrôle négatif** : un déménagement qui rapproche deux groupes de la *même* niche — aucun croisement, donc aucun effet attendu sur la fertilité croisée.
- **Falsification** : H_A est morte si le signe est discordant ou si l'effet naturel est nul. H_B est morte si le signe concorde et l'effet est significatif.

---

## (c) Mesure minimale de fonctionnement pour chaque instrument nommé

### iVAE (auto-encodeur variationnel à variable auxiliaire)

- **Taux de détection** : proportion des facteurs causaux plantés retrouvés avec MCC ≥ 0.7, sur ≥ 20 mondes inventés variant en nombre de latentes (5, 10, 20), en ratio signal/bruit, et en proportion de confondeurs non observés.
- **Taux de fausses alertes** : proportion de facteurs non causaux (accompagnateurs) retrouvés avec MCC ≥ 0.7.
- **Cas honnêtes appariés** : chaque monde inventé contient *au moins autant* d'accompagnateurs que de causes. Un monde où toutes les latentes sont causales n'est pas un test.
- **Vérification mécanique à battre** : ACP + rotation varimax, même nombre de composantes. Si l'iVAE ne fait pas mieux (test de McNemar, p < 0.01), la variable auxiliaire temporelle ne fonctionne pas sur ces données.

### ICP (prédiction causale invariante)

- **Taux de détection** : proportion des vraies variables causales retenues dans S*, sur mondes inventés avec 3+ environnements.
- **Taux de fausses alertes** : proportion des non-causales retenues.
- **Cas honnêtes** : environnements dont le mécanisme causal est *identique* (condition requise) mais dont les distributions marginales changent ; et un jeu-piège où le mécanisme causal change entre environnements (ICP doit renvoyer ∅).
- **Vérification mécanique** : Lasso pénalisé avec sélection de variables par BIC. Si ICP ne fait pas mieux en taux de détection, l'invariance n'apporte rien.

### LiNGAM / PCMCI (découverte de structure)

- **Taux de détection** : proportion des arêtes causales vraies retrouvées (rappel).
- **Taux de fausses alertes** : proportion d'arêtes absentes déclarées présentes (1 − précision).
- **Cas honnêtes** : graphes à 10–50 nœuds, densité 1–3 arêtes par nœud, bruit à queue lourde (comme les citations), avec et sans variable cachée commune.
- **Vérification mécanique** : régression de Granger linéaire (pour PCMCI), tri par variance décroissante (pour NOTEARS — piège de la varsortabilité, Reisach, Seiler et Weichwald 2021, *NeurIPS* — SUPPOSÉ).
- **Seuil** : F1 ≥ 0.6 et supérieur de ≥ 10 points au F1 de la vérification mécanique. Sinon, l'instrument ne fonctionne pas sur des données de cette structure.

### Forêts causales / réseaux à deux têtes (estimation d'effets hétérogènes)

- **Taux de détection** : couverture de l'intervalle de confiance à 95 % sur l'effet de traitement conditionnel (CATE), mesurée sur des mondes inventés semi-synthétiques (données réelles, traitement et résultat simulés).
- **Taux de fausses alertes** : proportion d'unités pour lesquelles l'effet estimé a le mauvais signe.
- **Cas honnêtes** : mondes avec confondeurs observés *et* un confondeur non observé de force connue (pour tester la dégradation).
- **Vérification mécanique** : régression linéaire avec termes d'interaction. Si la forêt causale ne la bat pas en couverture, la non-linéarité n'ajoute rien.

---

## (d) Ancrage matériel

### Modèles ouverts utilisables

| Composant | Modèle ouvert | Licence | Référence à vérifier |
|---|---|---|---|
| iVAE | `ilvm` (implémentation de Khemakhem et al.) | MIT (SUPPOSÉ) | Khemakhem, Kingma, Monti, Hyvärinen 2020 — SUPPOSÉ |
| ICP | `InvariantCausalPrediction` (package R, Peters et al.) | GPL (SUPPOSÉ) | Peters, Bühlmann, Meinshausen 2016 — SUPPOSÉ |
| PCMCI | `tigramite` (Runge) | GPL-3 (SUPPOSÉ) | Runge et al. 2019 — SUPPOSÉ |
| NOTEARS | `notears` (Zheng et al.) | Apache 2.0 (SUPPOSÉ) | Zheng, Aragam, Ravikumar, Xing 2018 — SUPPOSÉ |
| LiNGAM | `lingam` (package Python) | MIT (SUPPOSÉ) | Shimizu et al. 2006 — SUPPOSÉ |
| Forêts causales | `grf` (package R, Athey, Tibshirani, Wager) | GPL-3 (SUPPOSÉ) | Wager et Athey 2018 — SUPPOSÉ |
| Régression symbolique | `PySR` (Cranmer) | Apache 2.0 (SUPPOSÉ) | Cranmer 2023 — SUPPOSÉ |
| VAE de base | PyTorch / JAX natif | BSD | — |

### Calcul nécessaire (illustratif)

| Étape | Données | GPU | Temps estimé |
|---|---|---|---|
| Mondes inventés (20 configurations × 10 graines × 5 méthodes) | ~1000 runs, ~10⁵ points chacun | 1 × A100 | ~50 h (illustratif) |
| iVAE sur sous-domaine OpenAlex (~10⁶ articles) | Plongements pré-calculés (SPECTER ou similaire, ~10⁸ paramètres) | 1 × A100 | ~24 h entraînement (illustratif) |
| ICP sur features tabulaires (~10⁵ paires × 50 features × 5 environnements) | CPU | 16 cœurs | ~2 h (illustratif) |
| PCMCI sur séries temporelles (~500 niches × 20 ans) | CPU | 16 cœurs | ~8 h (illustratif) |
| Forêts causales sur données de courses (~10³ paires par bras) | CPU | 4 cœurs | ~1 h (illustratif) |
| **Total estimé** | — | 1 A100 + serveur CPU | ~100 h GPU, ~50 h CPU (illustratif) |

**Coût** : ~200 $ en cloud GPU (illustratif, prix A100 spot ~2 $/h). L'essentiel du coût réel est le temps de construction des mondes inventés et de préenregistrement, pas le calcul.

### Ce qui manque et ne peut pas être estimé ici

- Le **nombre de courses randomisées** nécessaires pour l'expérience 3. Avec un effet attendu de Cohen's d ≈ 0.5 (illustratif, aucune base empirique), il faut ~64 paires par bras pour une puissance de 80 % à α = 0.05 (illustratif). Si l'effet est plus petit (d ≈ 0.2), il en faut ~400, ce qui peut représenter des mois de courses.
- La **disponibilité des données d'expériences naturelles** (programmes de conférences avec listes de participants, dossiers de financement avec scores) : aucune pièce ne confirme l'accès.

---

## Synthèse de la position B

La question de Lazar (« pourquoi pas l'apprentissage non supervisé ? ») mérite mieux que le « non » de la question 5 et mieux que le « oui sous hypothèses » de la question 6 :

1. **Le démêlage non supervisé standard ne peut pas identifier les causes** — c'est un théorème (Locatello et al. 2019 — SUPPOSÉ), pas une opinion. Mais ce théorème vise un cadre précis (VAE i.i.d. sans contrainte).

2. **Des variantes à variable auxiliaire ou temporelle *peuvent* identifier des latentes** — c'est aussi un théorème (Hyvärinen & Morioka 2016, Khemakhem et al. 2020 — SUPPOSÉ). Mais « identifier des latentes » signifie les retrouver à transformation affine près, pas prouver qu'elles sont *causales*.

3. **Passer de « latentes identifiées » à « causes de la fertilité » exige une étape supplémentaire** que l'apprentissage profond ne fournit pas seul : soit une intervention (nos courses), soit une hypothèse d'invariance testée, soit une structure identifiée sous non-gaussianité *et* acyclicité. Chacune de ces voies repose sur une hypothèse non triviale dont la violation détruit l'identification.

4. **La réponse honnête est donc** : l'apprentissage profond *non supervisé avec variable auxiliaire* peut identifier des *facteurs latents stables* dans les données scientométriques, ce qui est utile (réduction de dimension causalement motivée) mais insuffisant. Pour savoir lesquels de ces facteurs *créent* la fertilité, il faut les croiser avec une source d'identification externe. L'apprentissage profond est alors l'estimateur, pas l'identificateur. La pièce `reponse-conv-audit-question-6-v1.md` arrive à cette conclusion mais la formule de façon ambiguë (« identifie — pas à lui seul : avec l'hypothèse »), ce qui confond identification statistique (retrouver les latentes) et identification causale (prouver que ce sont des causes).

5. **Le critère de mort** de chaque voie est donné dans les expériences ci-dessus. La voie « tout par apprentissage profond non supervisé » est morte si l'expérience 1 échoue (le modèle ne distingue pas causes et accompagnateurs sur monde planté) *ou* si l'expérience 3 échoue (la prédiction d'intervention est incorrecte) *ou* si un modèle prédictif sans structure causale fait aussi bien (le « causal » n'ajoute rien).

FIN-DE-CELLULE