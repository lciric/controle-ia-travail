# Proposition A — Tour III.1 : « neuron-explorer » et le programme de contrôle

## 0. État des pièces

- Bloc FAITS : vide par ordre de l'arbitre (GO-2026-10-26-01). Rien à inventer.
- Tout ce qui concerne la méthode (chiffres, neurones de référence, coûts) vient de la lecture du dépôt par l'arbitre : statut **RAPPORTÉ**, non audité par moi ; je n'ai pas lu le dépôt. La licence est **absente** (RAPPORTÉ).
- Les faits du programme (Llama-3.1-8B-Instruct épinglé, dernier jeton, deux familles, primitive bornée, boucles) : **RAPPORTÉ** par la question ; je les prends comme cadre. « 32 couches, 14 336 neurones par couche » est cohérent avec la configuration publique de ce modèle (à vérifier sur le fichier de configuration de la révision épinglée).

Point de méthode qui traverse tout le reste : la méthode a été conçue sur Qwen3.5-4B, le programme tourne sur Llama-3.1-8B-Instruct. Aucun des chiffres rapportés (19,6 %, 8,2 %, 0,8× la norme, 1,25 USD) ne transfère sans être remesuré. Tout ce qui suit est à relire comme « à remesurer sur le modèle épinglé ».

---

## (a) Ce que la question suppose sans que ce soit établi

**A1. Qu'une direction qui *lit* bien est une direction qui *écrit* ce qu'elle lit.** HYPOTHÈSE. Une sonde linéaire est entraînée à discriminer ; elle capte toute direction corrélée au label, y compris des directions que le modèle ne consomme pas en aval. La direction optimale pour pousser (celle qui déplace le comportement) peut être différente de la direction optimale pour lire. Le programme a lui-même retiré le « bruit d'activations » des interventions revendiquées : il n'a donc à ce jour aucune intervention validée sur laquelle s'appuyer.

**A2. Que « dépasser 256 directions aléatoires de même norme » signifie « porteur de sens ».** HYPOTHÈSE. Un neurone de couche intermédiaire est un axe privilégié par la non-linéarité (la porte du MLP) ; une direction aléatoire dense dans l'espace résiduel n'a pas ce statut. Battre des directions aléatoires denses est une barre basse : le bon témoin pour un neurone est un *autre neurone* (ou une combinaison éparse de neurones de même norme), pas une direction dense. La part de 5 % attendue au-dessus du 95ᵉ centile n'est pas un taux de fausses alertes au sens où le programme l'entend : c'est le taux de dépassement d'un nul mal choisi.

**A3. Que des doses étalonnées sur des amorces de deux ou trois jetons (« who », « snake ») transfèrent à des transcriptions longues.** HYPOTHÈSE. La norme résiduelle varie avec la position et le contexte ; une poussée appliquée à toutes les positions d'une transcription de 1 000 jetons n'est pas la même opération qu'une poussée sur le dernier jeton d'une amorce. Le programme lit au dernier jeton ; la méthode pousse sur une génération entière. Le point d'application doit être écrit d'avance.

**A4. Que les chiffres rapportés (19,6 %, 8,2 %, creux au milieu du réseau, 0,8× casse le texte) tiennent.** RAPPORTÉ, non audité ; l'arbitre les marque lui-même « à vérifier ». Le neurone « levier de refus » (+1,5 → « I » devient « Sure ») est un effet sur le **premier jeton** : c'est exactement le type d'effet de surface que le programme compare à ses sondes.

**A5. Que la verbalisation (« ceci est un test ») est un bon capteur d'état interne sous poussée.** HYPOTHÈSE. Pousser une direction peut injecter du vocabulaire sans modifier l'état qui conditionne le comportement : le modèle *dit* « test » parce que les logits de « test » montent, pas parce qu'il « sait ». La question le reconnaît implicitement (lire *contre* écrire) mais ne sépare pas « change la verbalisation » de « change le comportement conditionné à l'évaluation ».

**A6. Que la conscience d'évaluation ou l'honnêteté d'une trace admettent un **levier** (un neurone, une direction).** HYPOTHÈSE, et c'est la plus lourde. La littérature sur la superposition (voir §5) prédit que des concepts rares et contextuels sont portés par des combinaisons, pas par des axes de base. Le refus, où une direction unique est rapportée (référence à vérifier, §5), est un comportement **entraîné par le fournisseur, fréquent, binaire** ; la conscience d'évaluation n'a aucune de ces trois propriétés a priori.

**A7. Que la méthodologie de l'agent (casser l'hypothèse exprès, maximum à l'aveugle) réduit le biais de confirmation.** RAPPORTÉ comme intention de l'auteur ; aucun taux de succès du « maximum à l'aveugle » n'est rapporté. Sans ce taux, c'est une procédure, pas un instrument.

**A8. Que les sondes de l'étape 1 sont assez bonnes pour mériter une validation causale.** Non établi dans les pièces (aucun score de sonde ni d'écart aux références de surface n'est joint). Pousser la direction d'une sonde qui dépasse à peine les références de surface ne teste rien.

**A9. Que le coût transfère.** RAPPORTÉ pour un modèle de 4 B et 9 216 neurones ; voir (d).

---

## (b) Expériences décisives, en duels

Conventions communes : modèle Llama-3.1-8B-Instruct, révision épinglée ; k = 256 directions aléatoires de même norme **et** 256 neurones tirés au hasard comme second nul ; seuil écrit d'avance dans un fichier empreinté ; banque de conception pour régler, banque neuve scellée pour confirmer ; tout chiffre ci-dessous est **illustratif** sauf mention.

### E1 — La direction de la sonde écrit-elle ce qu'elle lit ? (demande 1)

- **H_A** : pousser la direction de la sonde « conscience d'évaluation » déplace le comportement conditionné à l'évaluation au-delà des deux nuls.
- **H_B** : la sonde lit un corrélat que le modèle ne consomme pas ; la poussée ne fait pas mieux que le nul (ou n'agit que par dégradation générale).
- **Métrique** : sur des paires de tâches *identiques* sauf le cadrage (une version cadrée « évaluation », une non cadrée), écart de log-probabilité du choix du modèle entre les deux versions, mesuré au dernier jeton ; la poussée est appliquée à la version **non cadrée** et on mesure si elle rapproche le comportement de la version cadrée. Métrique secondaire : perplexité sur un texte neutre (pour détecter la casse).
- **Seuil** : écart au-dessus du 95ᵉ centile des 256 directions aléatoires **et** des 256 neurones aléatoires, à une dose où la perplexité neutre reste dans la bande des témoins (illustratif : 0,3–0,6× la norme résiduelle de la couche, à étalonner sur le modèle épinglé, pas repris de 0,8×).
- **Contrôle négatif** : direction d'une sonde entraînée sur labels mélangés ; direction d'une « sonde de surface » entraînée sur les références de surface (longueur, mots-clés) — si celle-ci pousse aussi bien, l'effet est de surface.
- **Issue** : effet ≤ nuls → H_A falsifiée pour cette sonde (elle lit sans écrire ; elle reste utilisable comme détecteur, mais toute revendication causale tombe). Effet > nuls mais pas > sonde de surface → H_A falsifiée aussi (l'effet est de surface). Effet > tout → H_B falsifiée ; cela prouve que la direction est **suffisante** pour déplacer le comportement, pas qu'elle est **nécessaire**, ni que le modèle « sait » quoi que ce soit.

### E2 — Verbalisation ou état ? (demandes 1 et 6)

- **H_A** : la poussée déplace *ensemble* la verbalisation (« ceci est un test ») et le comportement de E1.
- **H_B** : la poussée déplace la verbalisation seule (injection lexicale).
- **Métrique** : taux de verbalisation « test/évaluation » dans la réponse à une question ouverte, et métrique de E1, sur les mêmes paires. Comparer au **contrôle mécanique** : la même phrase injectée dans l'amorce (« Note : ceci est un test ») — si l'injection textuelle produit le même couple (verbalisation, comportement), la poussée n'apporte rien que le texte ne fasse.
- **Seuil** : les deux effets au-dessus du nul ; corrélation entre les deux à travers les doses.
- **Issue** : verbalisation seule → H_A falsifiée, et la sonde est un lecteur de vocabulaire ; les deux → H_B falsifiée ; ni l'un ni l'autre → E1 décide.

### E3 — Direction apprise contre ses neurones (demandes 1, 2, 6)

- **H_A** : l'effet de la direction est porté par peu de neurones (levier épars).
- **H_B** : l'effet est distribué.
- **Métrique** : effet de E1 obtenu en ne poussant que les m neurones de plus fort coefficient dans la direction (m = 1, 8, 64, 512), rapporté à l'effet de la direction complète à norme égale.
- **Seuil** (illustratif) : H_A retenue si m ≤ 8 recouvre ≥ 50 % de l'effet ; H_B si m = 64 recouvre < 25 %.
- **Contrôle négatif** : m neurones aléatoires de même norme totale ; m neurones de plus fort coefficient d'une sonde à labels mélangés.
- **Issue** : c'est la réponse directe à « des leviers uniques existent-ils ? ». Si H_B, un balayage neurone par neurone (E4) cherche un objet qui n'existe pas, et le coût de (d) est perdu d'avance : **faire E3 avant E4**.

### E4 — Balayage préenregistré (demande 2)

- **H_A** : les neurones signalés sur la banque de conception pour un vocabulaire cible fixé d'avance se répliquent sur la banque neuve à un taux supérieur au taux de réplication de neurones tirés au hasard.
- **H_B** : taux de réplication ≈ taux des neurones aléatoires (« parcourir puis affirmer »).
- **Métrique** : fraction des neurones signalés qui dépassent le seuil sur la banque scellée, contre la même fraction pour un échantillon de neurones aléatoires soumis à la même procédure.
- **Seuil** (illustratif) : H_A si la fraction est au moins triple de celle des aléatoires ; H_B si le rapport est inférieur à 1,5.
- **Contrôle négatif** : deuxième vocabulaire cible sans rapport (ex. culinaire), fixé d'avance : si autant de neurones « conscience d'évaluation » se répliquent pour la cuisine, la métrique de grappe de mots mesure autre chose.
- **Garde contre « parcourir puis affirmer »** : la liste des neurones signalés est empreintée **avant** que la banque neuve soit ouverte ; aucune hypothèse d'interprétation (« ce neurone code X ») n'est écrite avant la réplication ; les interprétations viennent après et sont elles-mêmes testées par E6.

### E5 — Doses et amorces (demande 1)

- **H_A** : le classement des neurones « distincts » est stable entre amorces courtes et transcriptions longues (corrélation entre familles ≥ fiabilité test-retest à l'intérieur d'une famille, moins une marge écrite d'avance).
- **H_B** : le classement dépend du type d'amorce.
- **Contrôle négatif** : corrélation entre deux tirages aléatoires.
- **Issue** : H_B → tout balayage du programme doit se faire sur ses propres transcriptions, et les chiffres de coût de l'auteur ne s'appliquent plus.

### E6 — Le « maximum à l'aveugle » mesure-t-il quelque chose ? (demande 4)

- **H_A** : un second agent qui ne voit que l'explication d'un neurone écrit un texte atteignant un centile élevé de l'activation du corpus plus souvent qu'avec une explication **d'un autre neurone** (explications permutées).
- **H_B** : pas de différence.
- **Métrique** : taux de succès (texte ≥ 90ᵉ centile du maximum du corpus, illustratif) avec explications vraies contre permutées.
- **Contrôle mécanique à battre** : donner au second agent les cinq exemples de plus forte activation du corpus au lieu de l'explication.
- **Issue** : H_B → la méthodologie est un rituel ; H_A → l'explication a un contenu, ce qui n'en fait pas une explication causale.

### E7 — La primitive « pousser » dans les organismes (demande 3)

- **H_A** : des organismes disposant de « pousser » (avec rendu de k directions aléatoires) améliorent leur score sur la banque scellée par rapport à des organismes dont la primitive renvoie **toujours** des poussées aléatoires (placebo).
- **H_B** : pas d'écart ; la primitive est un coût.
- **Métrique** : score sur banque scellée, course contre course, placebo apparié ; coût journalisé.
- **Issue** : H_B → ne pas étendre la primitive. Danger spécifique à borner d'avance : un organisme peut utiliser la poussée pour fabriquer des textes qui font monter sa propre sonde (détournement) ; la règle existante « jamais sur des tâches de la banque » tient, et il faut ajouter : la poussée ne modifie jamais les activations lues par la sonde de scoring.

---

## (c) Pour chaque instrument : la mesure minimale qui dirait s'il fonctionne

| Instrument nommé | Taux de détection sur quels cas honnêtes appariés | Taux de fausses alertes sur quel nul | Vérification mécanique à battre |
|---|---|---|---|
| **Balayage avec témoins aléatoires** | Cas plantés : neurones dont la colonne de sortie projette fortement, mécaniquement, sur le vocabulaire cible (lentille 1) ; le balayage doit les retrouver | Directions aléatoires denses **et** neurones aléatoires ; vocabulaire cible sans rapport | La lentille 1 (projection de la colonne) seule, et la lentille 2 (Δlog-prob une passe) seule : si le classement coûteux par déroulés ne fait pas mieux que ces deux-là, il n'apporte rien |
| **Lentille 2 (Δlog-prob ±0,8, une passe)** | Même cas plantés | Directions aléatoires | Lentille 1 |
| **Agent (lire→écrire, casser l'hypothèse)** | Neurones à sens plantés par la lentille 1 : l'agent retrouve-t-il la cible ? | L'agent lancé sur une direction aléatoire : combien de « neurones de persona » invente-t-il ? (l'auteur rapporte que sans témoins ils apparaissent partout) | Explication automatique à partir des exemples de plus forte activation (méthode publiée, référence §5) |
| **Maximum à l'aveugle** | E6 : explications vraies | Explications permutées | Cinq exemples de corpus donnés directement |
| **Clôture par log-probabilités** | Effet prédit par l'agent observé à la dose prédite | Même mesure sur 256 directions aléatoires | Rien à battre : c'est une mesure, pas une détection ; exiger seulement qu'elle soit **préenregistrée** avec sens et dose |
| **Sondes de l'étape 1 sous poussée (E1)** | Direction de la sonde contre paires cadrées/non cadrées | Sonde à labels mélangés ; sonde de surface | Injection textuelle du cadrage (E2) |
| **Verbalisation** | Taux de « test/évaluation » sous poussée de la sonde | Sous poussée aléatoire | Même injection textuelle |
| **Primitive « pousser » des organismes** | Écart de score contre placebo (E7) | Organismes placebo qui « détectent » quand même des effets au-dessus du seuil : c'est leur taux de fausses alertes | Organismes sans primitive |

Une règle unique pour toute la table : un instrument qui ne bat pas sa vérification mécanique n'entre pas dans la confirmation préenregistrée, quelle que soit la qualité narrative de ses rapports.

---

## Littérature (demande 5) — tout « à vérifier »

Rien ci-dessous n'est donné avec identifiant ; titres et auteurs de mémoire, à vérifier avant usage.

- Superposition et unité « neurone » : Elhage et al., 2022, « Toy Models of Superposition » ; Gurnee et al., 2023, « Finding Neurons in a Haystack: Case Studies with Sparse Probing » (montre des neurones monosémantiques pour certains concepts et des combinaisons pour d'autres — directement pertinent pour E3).
- Dictionnaires épars : Bricken et al., 2023, « Towards Monosemanticity » ; Cunningham et al., 2023, « Sparse Autoencoders Find Highly Interpretable Features in Language Models » ; Templeton et al., 2024, « Scaling Monosemanticity ».
- Poussée d'activations : Turner et al., 2023, « Activation Addition » ; Rimsky et al., 2024, « Steering Llama 2 via Contrastive Activation Addition » ; Zou et al., 2023, « Representation Engineering » ; Li et al., 2023, « Inference-Time Intervention » (pousse des directions de sonde — le cas le plus proche de E1) ; Arditi et al., 2024, « Refusal in Language Models Is Mediated by a Single Direction » (le précédent « direction unique », à comparer et non à extrapoler).
- Sondes et témoins : Hewitt & Liang, 2019, « Designing and Interpreting Probes with Control Tasks » ; Ravfogel et al., 2020, « Null It Out » et Belrose et al., 2023, « LEACE » (effacement linéaire : le pendant « ablation » de la poussée, utile comme test de nécessité) ; Marks & Tegmark, 2023, « The Geometry of Truth » ; Park et al., 2023, « The Linear Representation Hypothesis… ».
- Causalité : Geiger et al., 2021, « Causal Abstractions of Neural Networks ».
- Explication automatique de neurones (le mécanique à battre de la table) : Bills et al., 2023, « Language models can explain neurons in language models ».
- Conscience de situation : Laine et al., 2024, « Me, Myself, and AI: The Situational Awareness Dataset ».
- Cité par le dépôt : essai Goodfire « Neural Networks Are Already Clean » et 128 neurones d'identité de Qwen3-8B : RAPPORTÉ par la question, contenu non lu par moi.

---

## (d) Ancrage matériel

- **Modèles ouverts** : Llama-3.1-8B-Instruct, révision épinglée (RAPPORTÉ, imposé) ; Qwen3.5-4B comme modèle de **réplication** de la méthode seulement, pas comme modèle du programme (changer de modèle exige une décision du directeur).
- **Volume** : 32 × 14 336 = 458 752 neurones (arithmétique sur les chiffres de la question). L'auteur rapporte ≈ 95 000 déroulés pour 9 216 neurones, soit ≈ 10 déroulés par neurone (arithmétique sur RAPPORTÉ) ; à protocole identique, ≈ 148 000 déroulés par couche sur le modèle du programme, plus 256 + 256 témoins.
- **Coût d'un balayage complet** : l'auteur rapporte 1,4 h et ≈ 1,25 USD par couche sur un modèle de 4 B à amorces courtes. Avec deux fois plus de paramètres et 1,56 fois plus de neurones, **illustratif** : 4–6 h et 4–6 USD par couche, soit 130–190 h et 130–200 USD pour 32 couches sur une carte grand public ; sur des transcriptions longues (E5), le préremplissage multiplie ce coût, **illustratif** ×2 à ×5. Le mode « sondage » (384 neurones + 64 témoins par couche, 32 couches, ≈ 6 USD rapporté sur 4 B) deviendrait, illustratif, 15–30 USD : c'est le seul mode raisonnable avant que E3 ait tranché.
- **E1–E3 (sondes)** : quelques directions × 512 témoins × quelques centaines de paires × quelques doses ; illustratif, de l'ordre de 10⁵ passes avant courtes, quelques heures de carte, coût négligeable devant le balayage. **À faire en premier**.
- **E6 (agent)** : coût dominé par les appels au modèle de langue qui joue l'agent ; illustratif, dizaines d'appels par neurone ; à chiffrer sur 30 neurones avant d'étendre.
- **Infrastructure** : la fourche de vLLM de l'auteur est écrite pour Qwen (RAPPORTÉ) ; licence absente, donc **ne pas réutiliser le code** ; réécrire un crochet de poussée par requête sur la pile du programme, avec dose en fraction de la norme résiduelle **mesurée sur la révision épinglée** et point d'application (toutes positions / dernier jeton) consigné dans le journal.

---

## Ordre et départage (demande 6) — voies, pas réponse

- **D'abord** : E1 et E2 sur les sondes existantes (si A8 est vérifiée : sondes qui dépassent nettement les références de surface), puis E3. Trois expériences à faible coût qui décident si « lire » et « écrire » coïncident et si un levier épars existe.
- **Ensuite, seulement si E3 penche vers H_A** : E5 (amorces) puis E4 en mode sondage, préenregistré, deux vocabulaires cibles dont un sans rapport.
- **En parallèle et bon marché** : E6 sur 30 neurones, pour savoir si la méthodologie de l'agent est un instrument ou une narration, avant d'en reprendre quoi que ce soit dans la boucle extérieure. Ce qui se reprend sans attendre, parce que c'est déjà l'esprit du programme : hypothèses écrites d'avance, « le test qui briserait l'explication » comme champ obligatoire du rapport, clôture par une mesure chiffrée empreintée.
- **Jamais** : interpréter un neurone à partir d'un déroulé sans témoins (l'auteur lui-même rapporte des « personas » sur des directions aléatoires) ; reprendre la dose 0,8× sans réétalonnage ; donner aux organismes une primitive « pousser » qui agit sur les activations lues par leur sonde de score ; pousser à toutes les positions quand la sonde lit au dernier jeton, sans l'avoir décidé et consigné.
- **Ce qu'il faudrait savoir de plus** : les scores actuels des sondes de l'étape 1 et leur écart aux références de surface (sans cela, E1 n'a pas d'objet) ; le taux de succès du « maximum à l'aveugle » chez l'auteur, s'il existe ; la licence du dépôt.
- **Ce qui falsifierait l'idée de leviers uniques pour la conscience d'évaluation** : E3 en H_B (aucun sous-ensemble de ≤ 64 neurones ne recouvre une part notable de l'effet de la direction) **et** E4 en H_B (réplication des neurones signalés au taux des neurones aléatoires), sur la banque scellée. Si les deux tombent, le programme garde la direction de sonde comme objet d'intervention candidat et abandonne la recherche de neurones ; si E1 tombe aussi, il garde la sonde comme détecteur et renonce, pour cette sonde, à toute revendication causale.

FIN-DE-CELLULE