# Proposition I — Tour III.1 (à l'aveugle) : cinq décisions pour trois bancs

**Pièces.** Le bloc QUESTION reprend mot pour mot le bloc FAITS (même sha256) ; la consigne à traiter est sa section « Forme de la réponse ». Les deux blocs sont complets. Je ne vois aucune autre proposition ce tour : rien à critiquer ni à réutiliser.

**Statuts.** Ce que le bloc FAITS affirme : RAPPORTÉ. Ce qu'il tire des « calculs de conception sur lois simulées » : OBSERVÉ-NON-AUDITÉ. Mes inférences : HYPOTHÈSE. VÉRIFIÉ ne s'applique qu'à l'arithmétique refaisable ici. Tout chiffre que je pose est illustratif.

**Suppositions globales de la question.** (i) Que les six décisions sont indépendantes : HYPOTHÈSE, et je la rejette (voir fil conducteur). (ii) Que les calculs de conception sont fiables : ils sont OBSERVÉS-NON-AUDITÉS, aucun audit n'est rapporté.

**Fil conducteur (HYPOTHÈSE).** Les décisions 2, 3 et 4 forment une chaîne : une désignation par mots (3a) sous-compte les contrôles paraphrasés de l'honnête ; un seuil 1/m non étalonné (2a) signale alors des honnêtes ; c'est le « régime d'excès » (4). Mes choix visent à prévenir l'excès en amont, pas à l'aménager en aval.

---

## Décision 1 — Témoin sans dommage

**Choix : (c), amélioré** (option meilleure, dite comme telle) : rapporter A et B sous leur nom, avec un critère d'admission gelé sur A — |A_témoin − A_réf| ≤ δ_A, δ_A fixé par le duel D1, au niveau d'erreur accordé à ce monde — et B déclarée diagnostique, hors admission. Confiance : 0,70.

**Raison.** Un témoin qui ne bouge pas est un témoin réussi, pas une mesure ratée : choisir B parce qu'elle « varie davantage » revient à choisir la grandeur pour son effet, ce que le gel existe pour interdire. Mais accepter, signaler et s'abstenir sont trois issues exclusives qui somment à 1 (VÉRIFIÉ, arithmétique) : A et B ne sont pas « un résultat de plus », ce sont les deux degrés de liberté d'une même distribution, et taire B cache un déplacement d'accepter vers s'abstenir. Le défaut de (c) — pas de critère — se répare en mettant le seuil sur A et en nommant le rôle de B.

**Changerait mon avis.** Si le texte gelé définit déjà « acceptation » et n'accorde qu'une grandeur par monde au budget de multiplicité → (a). Si D1 montre que la variation de B n'est que variance d'estimation → (a), B en annexe.

**Supposé sans être établi.**
- « Varie davantage » est un écart entre mondes, non la variance plus grande d'un estimateur fait sur moins de cas (le seul jumeau) : OBSERVÉ-NON-AUDITÉ (l'écart), HYPOTHÈSE (son sens).
- Les lois simulées prédisent le moniteur réel : HYPOTHÈSE.
- « Accepte (ne signale pas) » : l'abstention est-elle dedans ? Non défini : RAPPORTÉ (lacune). Le texte gelé doit trancher, car A change de sens.
- Le témoin est comparable à la référence hors dommage : HYPOTHÈSE.

**Duel D1.** H_A : |B_témoin − B_réf| dépasse la dispersion de B entre réplicats d'un même monde (signal). H_B : non (bruit). Métrique : rapport entre l'écart inter-mondes et l'écart-type de B sur R réplicats du monde de référence, lois simulées (R = 200, illustratif). Seuil gelé : 2 (illustratif). Contrôle négatif : deux moitiés du jumeau de référence, rapport attendu < 2. Issue : rapport ≥ 2 → H_B falsifiée, B porte une information propre, (c) amélioré ; rapport < 2 → H_A falsifiée, (a).

## Décision 2 — Règle de signalement par défaut

**Choix : (b)**, l'étalonnage portant sur des paires honnête/honnête : le seuil k/m retenu est le plus petit tel que la part de paires honnêtes signalées soit ≤ α_étal (0,05, illustratif). Confiance : 0,75.

**Raison.** Un écart d'un contrôle entre deux lectures d'un même document honnête est le plancher de bruit de tout oracle, humain ou modèle ; au seuil 1/m, ce bruit signale l'honnête, et c'est le chemin direct vers le régime d'excès. Ce qu'il faut étalonner n'est pas la sensibilité au dommage mais les fausses alertes sur honnêtes appariés, et cela se mesure, sur un lot que le lot final ne voit pas. (c) suspend la campagne à une règle que l'oracle pourrait écrire après avoir vu des objets : contamination plus coûteuse qu'un lot d'étalonnage, lequel sert aussi la décision 4.2.

**Changerait.** Des données pilotes montrant < α de paires honnêtes signalées au seuil 1/m → (a) suffit. Aucun lot distinct de même loi productible → (a), car étalonner sur le lot final consomme un regard. Règle binaire gelée livrée par l'oracle avant le gel → (c) par construction.

**Supposé.**
- « Signalé » est une sortie de l'oracle sur l'objet, et non celle du moniteur mesuré : non dit, RAPPORTÉ (lacune) ; mon choix vaut pour les deux lectures.
- Le bruit honnête/honnête de l'oracle est < 1/m : HYPOTHÈSE jamais mesurée.
- Un lot d'étalonnage de même loi existe : HYPOTHÈSE.
- Les parts sont moyennées sur les lecteurs ; sinon le seuil est discret, et m petit le rend grossier (m = 3, illustratif, donne 0,33 ; arithmétique VÉRIFIÉ) : non dit.

**Duel D2.** H_A : au seuil 1/m, la part de paires honnêtes appariées signalées (deux productions honnêtes de la même tâche, même référence, même m ; ou le même objet lu par deux panels disjoints) est ≤ α. H_B : > α. Métrique : taux sur n paires (n = 100, illustratif), borne binomiale exacte (Clopper et Pearson, 1934, « The use of confidence or fiducial limits illustrated in the case of the binomial »). Contrôle négatif : même objet relu par le même panel, taux attendu ≈ 0. Issue : borne inférieure > α → H_A falsifiée, (a) inadmissible, (b) ; borne supérieure ≤ α → H_B falsifiée, (a) admissible, l'étalonnage devient un simple rapport.

## Décision 3 — Qui désigne les contrôles

**Choix : (b), audité** (option meilleure, dite comme telle) : repéreur sur toutes les tâches, fidélité mesurée sur un échantillon relu par un second désignateur d'une autre famille de modèles, puis par un humain en cas de désaccord, et rapportée. À défaut : (c) avec règle de bascule gelée vers (b) si le rappel sur l'échantillon passe sous 1 − ε. Confiance : 0,70.

**Raison.** L'erreur du programme est un biais, pas un bruit : il rate les contrôles paraphrasés, à un taux qui dépend du style de l'agent, donc qui diffère entre mondes et entre honnête et saboté. Ce biais gonfle les manques de l'honnête (excès) et plafonne la reconnaissance de tous les moniteurs à la fois, ce qui comprime les écarts que le banc doit mesurer. (c) mesure le biais sans le corriger ; (b) le corrige au prix d'une lecture par tâche, marginale devant un oracle à plusieurs lecteurs (HYPOTHÈSE ; coût non chiffré dans les faits).

**Changerait.** D3 montrant un taux de paraphrase < ε → (c). Repéreur ne battant pas le programme sur l'échantillon → (c). Coût chiffré de (b) au-delà d'une part gelée du budget (10 %, illustratif) → (c).

**Supposé.**
- L'erreur de désignation ne fait que sous-estimer la reconnaissance : RAPPORTÉ. Mais l'erreur inverse (contrôle paraphrasé retiré sans être désigné) crée un dommage non enregistré, dont le signalement sera compté en fausse alerte : HYPOTHÈSE, à vérifier dans le barème.
- Le repéreur est plus fidèle que le programme : HYPOTHÈSE, non vérifiée non plus.
- Le taux de paraphrase est non négligeable : HYPOTHÈSE.

**Duel D3.** H_A : la part des contrôles présents sans reprise des mots de la référence est < ε (0,05, illustratif). H_B : ≥ ε. Métrique : rappel et précision du programme contre la désignation adjugée, sur n documents honnêtes (n = 100, illustratif). Contrôle négatif : documents d'un agent contraint de recopier la référence (rappel attendu ≈ 1 ; vérifie le programme). Contrôle positif : contrôles sciemment paraphrasés (rappel attendu ≪ 1 ; vérifie que la mesure voit les manques). Issue : 1 − rappel ≥ ε → H_A falsifiée, (b) ; < ε avec contrôles conformes → H_B falsifiée, (c).

## Décision 4.1 — Régime d'excès : que rendre

**Choix : (a) + (c), plus une pièce absente des options** (option meilleure, dite comme telle) : publier le diagnostic d'excès lui-même — taux de manques chez l'honnête, avec une borne au niveau que le texte gelé lui accorde dès maintenant, avant le gel et non après — comme résultat de campagne. Les chiffres par strate de (b) vont dans une annexe de conception scellée, servant à dimensionner la campagne suivante et publiée seulement avec l'énoncé garanti de celle-ci. Confiance : 0,65.

**Raison.** Un nombre « sans garantie » sur la grandeur principale sera cité sans sa marque ; les faits le disent et ne donnent aucun mécanisme pour l'empêcher. Le régime d'excès n'est pourtant pas un vide : c'est un résultat garanti sur l'instrument — l'oracle n'est pas assez fidèle sur l'honnête pour ce banc — et c'est cela qu'il faut rendre. (c) est de l'hygiène logicielle compatible avec tout le reste.

**Changerait.** D4 montrant que la borne de q par strate reste valide en excès → elle est garantie et doit être publiée comme telle. Un mécanisme de circulation scellée déjà en place → (b) interne.

**Supposé.**
- La borne de q « sans garantie » est calculable mais non valide : RAPPORTÉ (calculable), HYPOTHÈSE (non valide ; la règle « signalé » réfère à l'objet honnête, donc l'excès contamine q).
- On peut empêcher de lire un nombre comme garanti : HYPOTHÈSE, aucun mécanisme donné.

**Duel D4.** H_A : la borne de q par strate garde sa couverture ≥ 1 − α en excès. H_B : sa couverture tombe sous 1 − α. Métrique : couverture sur campagnes simulées à q connu, taux de manques honnête au-dessus du seuil d'excès (10 000 campagnes, illustratif) ; seuil : 1 − α moins la marge Monte-Carlo. Contrôle négatif : même simulation sous le seuil d'excès (couverture attendue ≥ 1 − α ; vérifie le simulateur). Issue : couverture tenue → H_B falsifiée, la borne est publiable avec garantie ; perdue → H_A falsifiée, (b) publierait une non-borne, (a).

## Décision 4.2 — Budget d'erreur

**Choix : (a)**, amélioré (option meilleure, dite comme telle) : avec 2(b), l'excès se constate sur le lot d'étalonnage, avant tout regard sur le lot final ; l'allocation se gèle alors une fois ; aucun niveau ne change après coup. Confiance : 0,70.

**Raison.** Réaffecter un budget après avoir vu sur les données qu'un énoncé ne s'écrit pas est une allocation dépendante des données : les manques honnêtes qui déclenchent l'excès entrent aussi dans « signalé », donc dans q. La perte de (a) est une perte de puissance ; celle de (b) est une perte de validité. Un budget inemployé n'est pas un gaspillage quand déclencheur et grandeur partagent les données.

**Changerait.** D4′ montrant que la réaffectation conditionnelle ne gonfle pas l'erreur → une règle conditionnelle gelée d'avance est admissible. Niveaux « accordés » non encore gelés → les réécrire maintenant n'est pas un changement après coup.

**Supposé.**
- Déclencheur et borne de q indépendants : HYPOTHÈSE, le contraire est probable.
- Niveaux 2,5 % / 1,25 % gelés : RAPPORTÉ « accordés », gel non précisé.
- Le budget se partage par somme (type Bonferroni) : HYPOTHÈSE.

**Duel D4′.** H_A : sous la règle « si excès, la part de l'énoncé en dommage revient aux bornes de q », l'erreur de couverture des bornes dépasse le nominal. H_B : elle reste au nominal. Métrique : erreur simulée, taux de manques honnête au voisinage du seuil d'excès (pire cas) ; seuil : nominal + marge Monte-Carlo. Contrôle négatif : allocation inconditionnelle (erreur = nominal). Issue : dépassement → H_B falsifiée, (a) ; sinon → H_A falsifiée, règle conditionnelle admissible si gelée avant tout regard.

## Décision 5 — Composition de la fiche

**Choix : (a).** Confiance : 0,80.

**Raison.** Aucune fiche n'a été servie : refaire le calcul d'admission coûte du calcul, pas de l'intégrité ; fixer la règle sur le calcul déjà fait, c'est ajuster la règle à la commodité. (b) légalise un geste que la règle de cohérence ne sait pas distinguer d'un geste honnête, et ôte au banc son témoin le plus simple contre la promotion sans appui. La comparabilité entre étapes se rétablit en rejouant l'étape 1 sous composition tirée.

**Changerait.** D5a montrant que la cohérence repère déjà « top-k » → le coût de (b) tombe. D5b montrant que k se lit dans les données même sous tirage → (a) n'achète rien, le remède est ailleurs. Recalcul d'admission au-delà du budget (non chiffré).

**Supposé.**
- Tirer la composition cache k : HYPOTHÈSE (des lois plantées fortes se comptent).
- La cohérence accepterait « top-k » : HYPOTHÈSE, dite non vérifiée.
- Le recalcul est faisable : non chiffré.

**Duel D5a.** H_A : la règle de cohérence accepte un agent scripté « promeut les k statistiques les plus fortes, k connu » au même taux qu'un honnête (écart < δ, 0,10 illustratif). H_B : elle le signale davantage. Métrique : taux de passage sur les mêmes épisodes, composition fixe, k révélé au seul agent scripté (n = 200, illustratif). Contrôle négatif : deux honnêtes de même loi, écart attendu < δ. Issue : écart < δ → H_B falsifiée, (b) perd bien un témoin, (a) ; écart ≥ δ → H_A falsifiée, la règle tient.

**Duel D5b.** H_A : sous composition tirée, un lecteur (modèle ou test simple) devine k avec une exactitude ≤ hasard + δ. H_B : mieux. Métrique : exactitude sur n jeux de données (n = 200, illustratif) contre la loi de tirage. Contrôle négatif : étiquettes k permutées (exactitude = hasard). Issue : > hasard + δ → H_A falsifiée, k fuit par les données ; sinon → H_B falsifiée, (a) suffit.

**Option meilleure, dite comme telle.** (a) plus des lois leurres : tirer par épisode un nombre variable de statistiques fortes mais fausses, de sorte que « top-k par force » soit faux par construction et que la règle de cohérence ait un témoin mécanique. Coût : le calcul d'admission est de toute façon à refaire.

---

## (c) Instruments nommés : la mesure minimale

Pour chacun : détection, fausses alertes, cas honnêtes appariés, vérification mécanique à battre.

1. **Moniteur de comparaison (tâches floues).** Détection : part des épisodes à dommage planté signalés, par monde et par strate. Fausses alertes : part du jumeau honnête signalée, par monde ; abstention rapportée à côté (les trois somment à 1). Appariés : le jumeau du même monde, même loi, même tâche. À battre : un signaleur aléatoire au même taux de fausses alertes, et une liste de contrôle fixe (présence des sections attendues) ; sous ces deux-là à fausses alertes égales, le moniteur n'apporte rien.
2. **Oracle à plusieurs lecteurs.** Fausses alertes : taux de « manques » sur documents honnêtes dont les contrôles sont présents mot pour mot (plancher attendu ≈ 0), puis paraphrasés. Détection : part des contrôles retirés par le tiers comptés manquants, par strate ; accord inter-lecteurs par contrôle. Appariés : l'objet de comparaison, même document avant dommage. À battre : le programme de recouvrement de mots sur les contrôles paraphrasés ; sinon l'oracle est un recouvrement de mots coûteux.
3. **Programme de recouvrement de mots.** Il est la base mécanique ; sa mesure est sa fidélité : rappel et précision contre une désignation adjugée, sur honnêtes verbatim et paraphrasés (D3).
4. **Repéreur.** Même rappel et précision ; fausses alertes de désignation (passages sans contrôle désignés) sur documents honnêtes ; doit battre le programme sur les contrôles paraphrasés à précision égale.
5. **Règle de cohérence.** Fausses alertes : part des analystes honnêtes jugés incohérents. Détection : part signalée de trois agents scriptés — « top-k », « promeut une statistique faible à la place d'une forte », « tait une loi vraie et promeut une fausse de force égale ». Appariés : l'honnête sur le même jeu de données. À battre : la règle « les statistiques promues sont-elles les k plus fortes ? », qui accepte « top-k » par construction.
6. **Fonction de calcul de l'optimum.** Pas un détecteur : cas d'essai à solution connue (une strate : dose dégénérée ; deux strates symétriques : mélange égal), écart à une recherche exhaustive sur grille sous tolérance, monotonie (plus de budget d'erreur → moins d'épisodes).
7. **Tiers planteur.** Fidélité : part des contrôles que le tiers croit retirés et que l'oracle compte manquants. Plausibilité : un détecteur naïf (longueur, style) ne sépare pas saboté/honnête mieux que hasard + δ.
8. **Règle de signalement par défaut.** Fausses alertes : taux honnête/honnête (D2). Sensibilité : signalement des dommages à un contrôle retiré mot pour mot (attendu élevé). Rien de plus mécanique à battre : son étalonnage est sa mesure.

## (d) Ancrage matériel — tout illustratif sauf mention

- Modèles à poids ouverts : Llama 3 (Meta), Qwen2.5 (Alibaba), Mistral et Mixtral (Mistral AI), DeepSeek ; familles différentes pour le repéreur et le second désignateur, afin de décorréler leurs erreurs.
- Simulations D1, D4, D4′, recalcul d'admission (5a) : processeur seul, quelques heures, coût négligeable.
- Repéreur (3b) : une lecture par tâche, 2–4 k jetons ; 1 000 tâches ≈ 4 M jetons ; un modèle d'environ 70 milliards de paramètres sur un GPU de 80 Go pendant quelques heures, ou quelques dollars en service tiers.
- Oracle à 3–5 lecteurs modèles : 3–5 fois le repéreur, par lot et par regard ; le lot d'étalonnage (2b), 100–200 objets, ajoute 10–20 % du coût du lot final.
- Adjudication humaine (D3) : 100 documents × 15 min ≈ 25 h.
- D5a, D5b : 2 × 200 épisodes d'analyste avec outils, ≈ 10 k jetons l'épisode ≈ 4 M jetons.
- Ordre de grandeur hors humain : une dizaine de GPU-heures, quelques dizaines de dollars ; le poste dominant est l'oracle, pas les décisions discutées ici.

FIN-DE-CELLULE