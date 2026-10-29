# Proposition B — Tour III.2 : équipe rouge croisée

## 0. État des pièces

- Les pièces A, C, FAITS et QUESTION sont présentes. Leurs sha256 sont déclarés mais je ne les ai pas recalculés.
- FAITS : l'encodage est abîmé (les accents sont remplacés par « ? »). Le texte reste lisible et rien ne semble manquer.
- Annexe 3 : les champions Argon sont coupés, comme A et C l'ont relevé. Je n'utilise aucun contenu manquant.
- Une observation non signalée par A ni par C : les textes Argon ne suivent pas le même gabarit que les textes Claude. On y lit « Fonction objectif *anti-vernis* », « Pont inédit », des paires d'articles $(u,v)$ inter-silos et des ablations sur Llama. Statut : OBSERVÉ-NON-AUDITÉ (lecture de la pièce). La consigne reçue par Argon n'est pas transmise. L'espèce et la consigne sont donc peut-être confondues. Cette confusion traverse les deux attaques ci-dessous.

---

## Contre la proposition A

### (a) Failles

**A-F1. La vérité de terrain est construite avec les mêmes outils que la ligne de base. Le verdict sur `jev` est donc en partie fixé d'avance.**
- A fabrique cinq types de failles plantées.
- Trois d'entre eux sont définis par une vérification mécanique : (i) DOI non résolvable dans Crossref/S2, (ii) chiffre incohérent, (v) section Duel supprimée.
- A exige ensuite que `jev` batte « longueur + sections » et « Crossref + regex » (tableau (c)).
- Sur les types (i) et (v), la ligne de base est l'oracle même qui a servi à générer l'étiquette : son AUC vaut 1 par construction.
- Le critère « AUC `jev` − AUC(baseline) < 0,10 ⇒ ne fonctionne pas » est donc satisfait d'office sur ces strates.
- La conclusion « `jev` ne fonctionne pas » serait pour moitié un artefact du plan d'expérience.

**A-F2. Les « jumeaux honnêtes » ne sont pas honnêtes, de l'aveu même de A.**
- A affirme (A8) qu'aucun champion n'est exécutable tel quel : budgets à 120 USD par bras, 24 000 exécutions (chiffre illustratif de A).
- A prend pourtant ces mêmes champions Claude comme textes $x$ « honnêtes » dans E3, E4 et le tableau (c).
- Une alerte levée sur $x$ peut donc être une vraie détection comptée comme fausse alerte.
- Le taux de fausses alertes, et avec lui tout seuil « > 20 % », est biaisé dans un sens inconnu.

**A-F3. Effet plafond : E3 et E4 sont penchés vers $H_B$.**
- Les failles (i), (ii) et (v) sont triviales pour un Red-Team qui a accès aux outils. Elles seront presque toutes trouvées dès le premier passage.
- Dans E3, $H_B$ (« prolonger ne sert à rien ») gagne alors parce que les failles plantées sont faciles, pas parce que le collisionneur fixe suffit.
- Les failles que la question de l'arbitre vise (confondants, validité de construit, budget infaisable) n'existent pas dans le jeu de cibles.
- E3 répond donc à une autre question que celle posée. Statut : HYPOTHÈSE.

**A-F4. E4 confond famille de poids et compétence.**
- La cellule « autre famille » est majoritairement `Llama-3.1-8B` local, et Claude n'occupe que deux cellules.
- Le facteur « famille » devient donc « Llama 8B contre Claude » : compétence, longueur de contexte et suivi d'instructions varient en même temps que les poids.
- Second problème, plus grave pour l'inférence : comparer « effet famille » et « effet prompt » n'a pas de sens sans échelle commune.
  - L'ampleur de chaque effet dépend des niveaux choisis : quel écart de prompt ? quelles familles ?
  - On peut faire gagner l'un ou l'autre facteur en réglant le degré de « resémancement ».
- Le duel n'est pas identifié.

**A-F5. Étape 0 et E1 : corrélation de Simpson et gabarit non contrôlé.**
- La régression « score ~ longueur + sections » sur les 247 textes valides est dominée par la séparation entre espèces : Claude est long, avec sections, vers 4 ; Argon est coupé, vers 0,6.
- Un ρ > 0,8 (seuil illustratif de A) peut naître entièrement de cet écart inter-groupes.
- Ce ρ ne dit rien de la validité de `jev` à l'intérieur d'une espèce. Or A prévoit un STOP sur ce seul critère.
- Les sous-scores `Duels` et `Contrôles` dépendent par définition de la présence de la section Duel. Un juge *valide* donnerait lui aussi zéro à une section absente. Une forte corrélation avec « présence de section » est donc vraie par construction et ne réfute pas A1.
- Dans E1, apparier les longueurs ne contrôle pas le gabarit : Argon traite apparemment une autre tâche (point 0).
- Le contrôle « supprimer `BASSIN_MATH` à longueur égale » est impossible tel qu'écrit : cette ligne fait quelques dizaines de caractères, une section 3 plusieurs centaines.

**A-F6. Violations de B4 dans la propre conception de A.**
- E1 : la phrase « $H_A$ vraie falsifie "Argon ne sait pas concevoir" n'est pas réfuté » se contredit. L'issue $H_A$ ne falsifie rien de nommé.
- E5 : $H_A$ est définie par une corrélation de rang ≥ 0,5. $H_B$ est définie par deux deltas, Δ`jev` > 0,5 et ΔDOI ≤ 0. Ces deux statistiques sont différentes, si bien que les deux hypothèses peuvent être vraies ensemble, ou fausses ensemble. Elles ne sont pas exclusives.
- E2 : « effet de la consigne » contre « effet de l'historique » est mal posé. Une consigne de déflation de vague 10 encode par définition l'historique (bassins à éviter). La « consigne V10 appliquée en premier » n'a donc pas de sens séparable. De plus, $H_B$ réunit deux hypothèses distinctes (« historique » et « pas d'effet »).

**A-F7. Puissance.**
- E2 utilise 10 clones par cellule alors que la variance de Fable va de 0,03 à 4,80 (Annexe 1, OBSERVÉ-NON-AUDITÉ).
- Expliquer « ≥ 70 % » d'un écart de 0,86 avec n = 10 n'est pas résoluble. Ordre de grandeur illustratif : un écart-type intra-cellule de l'ordre de 1 donne une erreur standard de la différence d'environ 0,45.
- Chao1 calculé sur 3 failles par texte n'a pas d'estimand stable : les singletons et doubletons sont tirés de 3 objets.

**A-F8. Le refus total de $\mathcal{M}_1$ (A12) repose sur une prémisse trop forte.**
- Des tâches à vérité mécanique existent dans le périmètre `controle-ia` : la survie de contraintes à travers $k$ délégations, vérifiable par analyseur.
- C l'utilise dans M3-3 ; je m'en sers ici contre A, en le disant.
- A aurait pu tester H9 à coût faible sans attendre un banc annoté.

### (b) Scénarios d'évasion contre les instruments de A

Toutes les entrées de ce tableau ont le statut HYPOTHÈSE. Les coûts sont illustratifs.

| Instrument de A | Évasion par un auteur adverse | Coût |
|---|---|---|
| Oracle Crossref/S2 (types i) | Citer des DOI réels mais non pertinents, ou leur attribuer un contenu qu'ils n'ont pas. L'existence est vérifiée, la pertinence non. | ≈ 0 |
| Regex / comptage de sections (types iv-v) | Fournir un squelette complet ($H_A$, $H_B$, « contrôle négatif », « illustratif ») au contenu creux ou tautologique. | Quelques centaines de tokens |
| `jev` (si sensible au format) | Allonger le texte et ajouter des sections. Le test E5 ne le détecte que si le contrôle « best-of-n sur longueur » est bien exécuté. | Tokens supplémentaires |
| Red-Team calibré sur les failles plantées | Placer ses défauts hors des cinq types plantés : confondant non contrôlé, budget infaisable, construit mal défini. Le détecteur n'a jamais vu ces types et le rappel mesuré reste excellent. | 0 |
| Arrêt séquentiel « *m* passes sans faille nouvelle » | Lors d'une riposte, ne réécrire que des passages sous le seuil de nouveauté, ou introduire le défaut dans la réécriture qui précède l'arrêt. | 0 |
| Diversité par distance de compression | Paraphraser pour passer sous la similarité zlib tout en gardant le même contenu (fausse décorrélation), ou l'inverse. | ≈ 1 appel |

**Toutes les évasions à la fois.** Un même texte combine :
- des citations réelles mais hors sujet ;
- un squelette de sections complet ;
- un défaut d'un type non planté ;
- une voix paraphrasée.

Ce texte passe Crossref, la regex, la ligne de base « longueur + sections », le Red-Team calibré, l'arrêt séquentiel et la distance de compression. Surcoût illustratif : moins de 0,05 USD par proposition.

Le point commun est que tous les instruments de A vérifient des *propriétés de surface que la vérité plantée sait générer*. Aucun ne vérifie une propriété qu'elle ne sait pas générer.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Une strate de failles non mécaniques**, sans aucun oracle regex ou Crossref (confondant inséré, contrôle négatif qui ne contrôle rien). Sans elle, A-F1 et A-F3 fixent le verdict.
2. **Un jumeau édité sans faille.** On applique à $x$ la même procédure d'édition, par le même modèle et avec la même longueur de diff, mais sans injecter de faille. Sans ce contrôle, un détecteur peut repérer les traces d'édition et non la faille.
3. **Une famille d'injection disjointe de la famille de détection.** Si Claude plante et Claude détecte, E4 est contaminé par la corrélation H4' qu'il prétend mesurer.
4. **Pour E4 : Llama-3.1-8B contre Llama-3.1-70B**, même famille et compétences différentes (le matériel est VÉRIFIÉ disponible). Ce contrôle sépare compétence et poids.
5. **Pour l'étape 0 : des corrélations intra-espèce.** Sans elles, le STOP est un artefact de Simpson.
6. **Pour E1 : Claude réécrit dans le gabarit Argon** (anti-vernis, pont $(u,v)$). Ce contrôle sépare gabarit et espèce.
7. **Pour E5 : un best-of-n sur un score aléatoire.** Il donne la ligne de base de ΔDOI attribuable à la seule sélection.

---

## Contre la proposition C

### (a) Failles

**C-F1. M3-1 est vrai par construction.**
- C plante des biais « au Tour 3 par injection de prompt ».
- Le bras fixe T = 3 n'a, par définition, aucune attaque après le tour 3. Une faille plantée au tour 3 y survit donc avec une probabilité proche de 1.
- Le seuil de C, « TSF(Bras 2) ≥ 0,45 », est atteint d'office.
- Le duel compare « une attaque après la riposte » à « aucune attaque après la riposte ». Il ne compare pas une règle de Wald à un calendrier fixe.
- La bonne comparaison est T = 4 fixe, ou T = 3 suivi d'une attaque finale, à budget égal (voir (c)).

**C-F2. La règle d'arrêt de Wald ne fait pas ce que C annonce, d'après les paramètres illustratifs de C lui-même.**
- **Acceptation.** Une passe propre ajoute $\log(0{,}98/0{,}80) \approx 0{,}203$. Le seuil d'acceptation vaut $\log(0{,}95/0{,}05) \approx 2{,}944$. Le nombre de passes propres consécutives requis est donc $m = \lceil 2{,}944/0{,}203\rceil = 15$, et non « ≈ 2 ».
- **Rejet.** Une faille ajoute $\log(0{,}02/0{,}20) \approx -2{,}303$. Le seuil de rejet vaut $\log(0{,}05/0{,}95) \approx -2{,}944$. Partant de 0, une faille ne suffit pas à rejeter. Or le code remet `wald_lambda = 0.0` après chaque réécriture : le rejet est **inatteignable**.
- **Conséquence.**
  - Toute proposition est réécrite indéfiniment.
  - L'acceptation exige 15 passes Red-Team propres par proposition, ce qui est incompatible avec 15 USD pour trois expériences à trois bras.
  - $T^*$ est en pratique toujours égal à $T_{\text{budget}}$.
- La « loi d'arrêt adaptative » se réduit à une boucle bornée par le budget. Le bras 3 (arrêt aléatoire) devient indistinguable du bras 1 pour une raison mécanique, sans rapport avec $H_B$.

**C-F3. La « spécification exécutable immédiate » contient des branches inertes.**
- `BUDGET_CLAUDE` n'est jamais décrémenté dans la boucle. La condition `while (BUDGET_CLAUDE > 5.0)` reste donc toujours vraie. Combiné à C-F2, cela donne une boucle sans terminaison garantie.
- La condition `(c_mut > SEUIL_RHO_H4 or BUDGET_GEMINI > 1.0)` est toujours vraie, puisque `BUDGET_GEMINI` est une constante égale à 20 dans le code. Argon est donc appelé à chaque passe.
- Le routage chimère « conditionné à H4' », cœur du point (iv), est inerte par construction. Le bras 1 de M3-2, tel qu'il est spécifié, est le bras 3 (déclenchement non conditionnel).

**C-F4. Le contrôle anti-Goodhart fuit : `jev` construit l'instrument et l'évalue.**
- C affirme que $V_{\text{ext}}$ « ne dépend pas de `jev-1.14.0` ».
- Or $V_{\text{ext}}$ inclut la survie au test de Wald, et $z_t$ dépend de `jev_1_14_0.verifier_duel_et_controle_negatif` et d'une KL « évaluée par `jev` ».
- `jev` sert aussi à sélectionner les ancres $\mathcal{M}_2$ (`score_pont`, DPP), à calculer ACh et NE, et à piloter le CUSUM.
- Les fonctions prêtées à `jev` (vérification de duel, contradiction, similarité, score de pont) ne sont pas attestées dans le socle, qui décrit seulement un « classifieur/moniteur non génératif » (VÉRIFIÉ).
- La mention « Zéro Goodhart » dans le code est contredite par le code lui-même.

**C-F5. Un quorum byzantin à trois familles ne tolère aucune faute.**
- C reprend la borne $n \ge 3f+1$ (via Fable #06). Avec $n = 3$ domaines, on obtient $f_{\text{byz}} = 0$, donc un quorum « de $2f_{\text{byz}}+1$ » d'une seule famille : aucune protection.
- Si Fable et Opus, tous deux Anthropic, partagent une part de leur lignée (HYPOTHÈSE non exclue par C), il ne reste que deux domaines.
- « Neutralise structurellement H4' » est donc une affirmation sans support. Elle est formulée comme un résultat alors qu'elle n'est qu'une hypothèse.

**C-F6. Glissements de statut (règle 1).**
- C écrit que l'écart d'Argon « provient directement de la troncature systématique… et d'une dérive de consigne (`H9`) ».
  - H9 est une HYPOTHÈSE du Papier B, et la cause de l'écart n'est pas établie.
  - Le changement de gabarit (point 0) est une explication concurrente : Argon a peut-être reçu une autre consigne, ce qui ne serait pas une dérive.
- C conclut ensuite « Argon échoue à rédiger des protocoles complets » à partir de scores OBSERVÉ-NON-AUDITÉ qu'il attribue lui-même à la troncature. C'est circulaire.
- « Déplace l'exploration vers des cônes secondaires » (Opus) n'est soutenu par aucune donnée : l'Annexe 2 ne donne que les meilleurs scores par cône, pas leur distribution par vague.
- Les moyennes « 0,62 » et « 4,02 » sont des moyennes non pondérées de moyennes de vague, alors que les effectifs valides vont de 6 à 10. La pondération n'est pas signalée.

**C-F7. M3-2 : vérité de terrain impossible et volume confondu.**
- Les « pièges sycophantes » (affirmations fausses mais fréquentes) sont « vérifiés par API Crossref/S2 ». Or ces API attestent l'existence d'une référence, pas la vérité d'une affirmation. La métrique principale TRPS n'a pas d'oracle.
- Argon est moins cher. À budget égal, la chimère obtient plus d'appels de Red-Team. Le gain éventuel peut donc venir du volume et non de la décorrélation.
- Le bras 2 « même graphe » ne dit pas qui remplace Argon.

**C-F8. M3-3 : la conformité est vraie par construction.**
- L'analyseur vérifie des marqueurs de surface : statuts, « contrôle négatif », « illustratif ».
- Le réamorçage CUSUM réinjecte la consigne racine, qui contient exactement ces marqueurs.
- La conformité au sens de l'analyseur augmente donc mécaniquement par copie de tokens, que la substance soit respectée ou non.
- C reconnaît lui-même, dans son tableau (c), qu'une sous-tâche fidèle peut avoir une faible similarité lexicale avec la consigne. Son CUSUM `1 - jev_sim(consigne_racine, prop.texte)` pénalise pourtant exactement ce cas.
- Dans le code, le CUSUM s'accumule sur les **tours** $t$, alors que la loi le définit sur la **profondeur** $d$. Deux grandeurs différentes sont confondues.

**C-F9. L'ordre des dépenses engage le budget avant toute validation, et les chiffres de budget sont incohérents.**
- C ventile 85 USD Claude vers $\mathcal{M}_2/\mathcal{M}_1$ sous une loi $\mathcal{L}^*$ que ses propres duels n'ont pas encore validée.
- M3-1 seul est annoncé à 30 USD Claude par bras (illustratif), alors que l'enveloppe totale de l'étage M3 est de 15 USD.
- C prévoit « environ 120 appels » pour trois duels à trois bras et 25 à 40 tâches, soit environ 13 appels par bras pour 30 tâches. C'est arithmétiquement impossible, même avant C-F2.

### (b) Scénarios d'évasion contre les instruments de C

Toutes les entrées de ce tableau ont le statut HYPOTHÈSE. Les coûts sont illustratifs.

| Instrument de C | Évasion | Coût |
|---|---|---|
| CUSUM `jev_sim` (H9) | Recopier la consigne racine, ou ses phrases-clés, dans la sortie : la similarité reste haute pendant que la substance dérive. | Tokens de recopie |
| NE (contradiction maximale) | Formuler les désaccords au conditionnel, sans contradiction explicite. NE reste sous $\theta_N$, donc $k_t^{RT} = 0$ : aucun Red-Team n'est engendré. | 0 |
| ACh (couverture bibliographique) | Ajouter des citations réelles quelconques. ACh baisse, donc aucun explorateur n'est engendré. | ≈ 0 |
| Red-Team Argon (300 tokens, ne voit que `extraire_duel_HA_HB()`) | Placer le défaut hors de la section Duel : budget, matériel, définition des métriques. Argon ne le voit jamais. | 0 |
| $C_{\text{mut}}$ zstd (H4') | Faire paraphraser l'un des deux pôles pour faire chuter la compressibilité mutuelle à contenu identique. | ≈ 1 appel |
| $V_{\text{ext}}$ « 4 composantes présentes » | Fournir le squelette des quatre composantes, au contenu creux. | ≈ 0 |
| Wald avec remise à zéro | Avec le rejet inatteignable (C-F2), une proposition fautive n'est jamais éliminée. Elle survit jusqu'à épuisement du budget et occupe des appels au détriment des autres. | 0 |

**Toutes les évasions à la fois.** Un même texte combine :
- la recopie de la consigne racine ;
- des formulations au conditionnel ;
- des citations réelles hors sujet ;
- un défaut placé hors du Duel ;
- un squelette de quatre composantes.

Aucun signal de C ne se déclenche (CUSUM, NE, ACh, Argon, $V_{\text{ext}}$). Le seul verrou restant est l'exigence de 15 passes propres. Elle bloque autant les propositions saines que les fautives, et l'auteur adverse n'a qu'à attendre. Surcoût illustratif : de l'ordre de quelques centimes par proposition.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **M3-1 : un bras T = 4 fixe, ou T = 3 suivi d'une attaque finale, à budget égal, avec des failles plantées aux tours 1, 2 *et* 3.** Sans ce bras, C-F1 rend $H_A$ vraie d'office.
2. **Une simulation hors ligne de la règle de Wald** (coût 0) sur deux cas : des propositions sans faille plantée, pour mesurer le temps d'acceptation réel, et des propositions systématiquement fautives, pour vérifier que le rejet survient. Ce second cas échoue en l'état (C-F2).
3. **Un contrôle « `jev` permuté »** pour $z_t$, ACh, NE et le CUSUM, sur le modèle du contrôle C d'Opus #06. Sans lui, impossible de savoir si `jev` contribue ou si tout vient des appels génératifs.
4. **M3-2 : un contrôle à volume apparié**, où le même nombre d'appels Red-Team Anthropic remplace Argon. Il faut aussi un **Argon recevant un protocole permuté** (une autre cible) pour vérifier que sa contribution dépend du contenu.
5. **M3-3 : un placebo de réinjection** (texte neutre de même longueur que la consigne) et une conformité évaluée sur la substance, pas sur les marqueurs. Le réamorçage périodique aveugle prévu par C ne contrôle pas la copie de tokens.
6. **Le CUSUM sur sous-tâches légitimement spécialisées** (cas apparié que C décrit dans son tableau sans l'inclure dans ses expériences). Ce contrôle mesure le taux de fausses coupures.
7. **Un test unitaire de la spécification** : décrément du budget, branche chimère qui peut être fausse, rejet de Wald atteignable. Tant que ce test n'est pas passé, C-F3 interdit de parler d'« exécutable immédiat ».

---

## Bilan réfutable, sans hiérarchie de portée

- **A** : les duels E1, E3 et E5 ont chacun au moins un verdict prédéterminé par le plan d'expérience (A-F1, A-F3, A-F5). E1 et E5 violent B4 (A-F6). E4 n'est pas identifié tant que la compétence n'est pas contrôlée (A-F4). La position méthodologique de A (pas de `jev` dans la récompense avant test) n'est pas attaquée ici.
- **C** : M3-1 est vrai par construction (C-F1). La règle d'arrêt ne peut pas rejeter et exige 15 passes, non 2 (C-F2). Le routage chimère du code est inerte (C-F3). Les briques jugées « résistantes à Goodhart » ne le sont pas, car `jev` y construit et y évalue l'instrument (C-F4).
- **Commun à A et C** : aucun des deux ne contrôle la possible différence de consigne entre Argon et Claude (point 0). Toute comparaison inter-espèces reste confondue tant que cette consigne n'est pas produite. Statut : HYPOTHÈSE.

FIN-DE-CELLULE