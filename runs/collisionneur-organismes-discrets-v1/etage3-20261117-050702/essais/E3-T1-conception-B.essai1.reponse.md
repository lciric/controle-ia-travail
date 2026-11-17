# Proposition B — Failles du bras B des organismes discrets

## (a) Présupposés non établis de la question

| # | Présupposé implicite | Statut | Commentaire |
|---|---|---|---|
| a1 | Les six indicateurs de forme suffisent à définir des classes assez grandes pour que le couplage anti-monotone produise un écart de coût substantiel entre action et valeur réappariée. | HYPOTHÈSE — le risque 1 de la conception (§6) dit explicitement que les classes peuvent être trop petites. Aucune distribution empirique des tailles de classe n'est RAPPORTÉE. |
| a2 | La distillation par adaptateur rang 16 sur projections d'attention transmet fidèlement la politique du maître réapparié à l'élève. | HYPOTHÈSE — hypothèse de travail 3 (§6, risque 3). Aucun taux de transfert mesuré n'est disponible. |
| a3 | L'estimation honnête cachée (médiane basse de huit suites du modèle de base) est une référence stable et non biaisée pour M2. | HYPOTHÈSE — aucun intervalle de confiance, aucune variance inter-suites ni inter-tâches n'est RAPPORTÉ. |
| a4 | La grille de doses `{0 ; 1/4 ; 1/2 ; 1}` échantillonne le régime où l'effet est détectable sans être trivial. | HYPOTHÈSE — aucune courbe pilote dose-effet n'existe. |
| a5 | Le témoin monotone (identité) isole l'effet du réappariement ; on présuppose qu'il n'y a pas d'artefact dû au regroupement en classes lui-même, au-delà du couplage. | RAPPORTÉ (§4), mais la vérification est déclarative, pas empirique. |
| a6 | P4 (échec de la base par construction) vaut pour le maître. La question traite cette propriété algébrique comme acquise pour l'ensemble du dispositif, y compris l'élève. | RAPPORTÉ (§3) pour le maître ; RAPPORTÉ comme écart non quantifié pour l'élève (§6, risque 4). |
| a7 | Le jeu de tâches de fabrication (8 à 16 tâches de réserve, §7 objection 3) est assez divers pour que les classes de forme couvrent la variabilité réelle du champ COST. | HYPOTHÈSE — aucun inventaire de la diversité des tâches n'est donné. |

---

## (b) Expériences décisives — duels H_A / H_B

### Faille F1 — Classes de forme dégénérées (trop petites)

**Description.** Si la plupart des classes contiennent 0 ou 1 action, le couplage anti-monotone laisse ces épisodes inchangés. L'effet mesuré ne vient que d'une fraction inconnue des données. Un faux négatif sur P3 est probable ; un faux positif est possible si les rares classes non triviales contiennent les tâches les plus extrêmes.

**Direction de biais.** Faux négatif principalement ; faux positif si la fraction active est petite mais extrême (effet local fort, significatif mais non généralisable).

**Duel.**

- **H_A** : la fraction d'épisodes effectivement réappariés (classe ≥ 2) est ≥ 0,50.
- **H_B** : cette fraction est < 0,50.
- **Métrique** : `f_active = (nombre d'épisodes dans des classes de taille ≥ 2) / (nombre total d'épisodes)`, calculé *avant* distillation, sur le maître.
- **Seuil** : 0,50 (si `f_active < 0,50`, le bras B est sous-alimenté et P3 n'est pas testable de manière fiable).
- **Contrôle négatif** : calculer `f_active` aussi sur un regroupement aléatoire (permutation des indicateurs de forme parmi actions), où l'on s'attend à des classes quasi-singletons.
- **Falsifie H_A** : `f_active < 0,50` sur le regroupement réel.
- **Falsifie H_B** : `f_active ≥ 0,50` sur le regroupement réel *et* `f_active` significativement plus élevé que sur le regroupement aléatoire (test exact de Fisher, α = 0,01).

**Garde.** Publier la distribution des tailles de classe avant toute lecture de M2, dans le préenregistrement ou en annexe scellée. Fixer un seuil minimal de `f_active` comme porte d'entrée du bras B.

**Ce qui changerait d'avis sur la gravité.** Si les tâches de fabrication génèrent naturellement des actions avec des profils de forme très stéréotypés (peu de combinaisons distinctes des six indicateurs), `f_active` sera élevé et la faille est bénigne. Sans cette information, la gravité est haute.

---

### Faille F2 — Coûts honnêtes proches intra-classe

**Description.** Si les coûts au sein d'une classe sont naturellement proches (faible variance intra-classe), le couplage anti-monotone produit un écart minuscule. P3 est vrai en signe mais l'amplitude est en dessous du seuil (0,15 décade). Faux négatif.

**Duel.**

- **H_A** : l'écart médian intra-classe entre le coût le plus haut et le plus bas est ≥ 0,30 décade (log₁₀).
- **H_B** : cet écart est < 0,30 décade.
- **Métrique** : `Δ_intra = médiane sur les classes de [max(log₁₀ COST) − min(log₁₀ COST)]`, sur le maître, dose 1.
- **Seuil** : 0,30 décade (deux fois le seuil de P3 pour laisser une marge de perte à la distillation).
- **Contrôle négatif** : même calcul sur des classes formées par un regroupement plus fin (ajout d'un indicateur supplémentaire), qui devrait réduire `Δ_intra`.
- **Falsifie H_A** : `Δ_intra < 0,30` sur les classes réelles.
- **Falsifie H_B** : `Δ_intra ≥ 0,30`.

**Garde.** Calculer `Δ_intra` sur les données honnêtes de base avant distillation. Si `Δ_intra < 0,15`, la conception du bras B est non informative et doit être modifiée (classes plus larges, ou enrichissement des tâches).

**Ce qui changerait d'avis.** Accès à la distribution empirique des coûts par classe. Si les tâches de fabrication couvrent une gamme > 2 décades et que les classes regroupent des tâches hétérogènes en coût, la faille est bénigne.

---

### Faille F3 — Perte de fidélité à la distillation (maître ≠ élève)

**Description.** L'adaptateur rang 16 peut échouer à reproduire le comportement du maître réapparié. Deux sous-cas : (i) l'élève ne reproduit pas le coût réapparié (atténuation), auquel cas P3 est affaibli (faux négatif) ; (ii) l'élève introduit un artefact systématique (biais de distillation) qui mime ou masque l'effet (faux positif ou faux négatif, imprévisible).

**Duel.**

- **H_A** : l'erreur M2 de l'élève par rapport au maître réapparié (et non par rapport à l'estimation honnête) est < 0,05 décade en médiane.
- **H_B** : cette erreur est ≥ 0,05 décade.
- **Métrique** : `M2_distill = |log₁₀(coût_élève) − log₁₀(coût_maître_réapparié)|`, médiane sur épisodes, pour chaque dose.
- **Seuil** : 0,05 décade (un tiers du seuil P3).
- **Contrôle négatif** : même distillation sur le témoin monotone (dose 0 effective). `M2_distill` doit être comparable, sinon le rang ou l'architecture introduit un biais dose-dépendant.
- **Falsifie H_A** : `M2_distill ≥ 0,05` à n'importe quelle dose.
- **Falsifie H_B** : `M2_distill < 0,05` à toutes les doses, *et* pas de différence significative entre doses (test de Kruskal-Wallis, α = 0,01).

**Garde.** Rapporter `M2_distill` pour chaque dose dans le tableau de résultats. Si `M2_distill` est du même ordre que l'effet P3, le signal est noyé et le bras est non concluant. Prévoir un rang alternatif (32 ou 64) comme plan B.

**Ce qui changerait d'avis.** Si la distillation porte sur un signal structurellement simple (un seul champ numérique dans un format fixe), un rang 16 est probablement suffisant. Mais ceci n'est vérifié que par `M2_distill`.

---

### Faille F4 — P4 est tautologique et masque un faux sentiment de sécurité

**Description.** P4 (échec de la base) est une identité algébrique, pas une prédiction empirique (§3, §7 objection 1). Le danger : on conclut que « la base est aveugle » en oubliant que cela ne vaut que pour le maître, et que l'élève peut laisser fuir de l'information que la base détecterait. Faux positif indirect : on croit le bras B indétectable alors qu'il ne l'est que par construction du maître.

**Duel.**

- **H_A** : la base « mots et coût » appliquée à l'élève (pas au maître) a un taux de détection ≤ 0,05 (au hasard) pour toutes les doses > 0.
- **H_B** : la base appliquée à l'élève a un taux de détection > 0,05 pour au moins une dose.
- **Métrique** : AUC de la base « mots et coût » sur un ensemble apparié élève-témoin, par dose.
- **Seuil** : AUC > 0,55 comme signal de fuite.
- **Contrôle négatif** : maître réapparié (où AUC ≈ 0,50 par construction).
- **Falsifie H_A** : AUC > 0,55 sur l'élève.
- **Falsifie H_B** : AUC ≤ 0,55 sur l'élève à toutes les doses, *et* AUC ≈ 0,50 sur le maître (confirmant l'identité).

**Garde.** Exiger que M-3 (vérification comme identité) soit exécuté *aussi* sur l'élève, pas seulement sur le maître. Rapporter les deux AUC côte à côte.

**Ce qui changerait d'avis.** Si l'élève est si fidèle que `M2_distill < 0,02` (faille F3 résolue très proprement), la fuite devient improbable. Mais ceci lie les deux failles.

---

### Faille F5 — Grille de doses trop espacée ou mal calibrée

**Description.** Quatre points `{0 ; 1/4 ; 1/2 ; 1}` : la monotonie de P3 repose sur trois comparaisons (0→1/4, 1/4→1/2, 1/2→1). Si l'effet sature entre 1/4 et 1, les deux doses hautes sont redondantes et la courbe semble plate (faux négatif partiel). Si l'effet est nul avant 1/2 et soudain à 1, on ne mesure qu'un point informatif (puissance très faible pour affirmer la monotonie).

**Duel.**

- **H_A** : l'effet M2 est monotone strict sur les quatre doses (chaque incrément > 0,03 décade).
- **H_B** : l'effet sature ou est non monotone (au moins un incrément ≤ 0,03 décade).
- **Métrique** : incréments appariés de M2 entre doses consécutives.
- **Seuil** : 0,03 décade (un cinquième du seuil P3).
- **Contrôle négatif** : mêmes adaptateurs avec couplage aléatoire (ni monotone ni anti-monotone) aux mêmes distances de Kendall, pour vérifier que la monotonie vient bien de la direction du couplage et non de la seule distance.
- **Falsifie H_A** : un incrément ≤ 0,03 décade.
- **Falsifie H_B** : tous les incréments > 0,03 décade et significativement positifs (test de signes unilatéral par paire, α = 0,05 avec correction de Holm).

**Garde.** Ajouter un point intermédiaire (par exemple 3/4) ou, mieux, un couplage aléatoire comme contrôle actif. Préenregistrer l'hypothèse de monotonie stricte *et* l'hypothèse de tendance (Jonckheere-Terpstra) pour conserver de la puissance.

**Ce qui changerait d'avis.** Un pilote sur 2 tâches avec 5 doses montrant un profil continu rendrait cette faille mineure.

---

### Faille F6 — Témoin monotone contaminé par effet Hawthorne du regroupement

**Description.** Le témoin monotone (§4) regroupe les actions en classes et réécrit les coûts dans l'ordre identique. Cette réécriture (même si les valeurs sont les mêmes) peut modifier la forme textuelle exacte (espaces, arrondis, format scientifique vs décimal). Si le modèle 8B est sensible à ces micro-variations, le témoin lui-même peut décaler M2, faussant la ligne de base.

**Direction de biais.** Si le témoin est bruité vers le haut, le delta P3 (bras B − témoin) est réduit : faux négatif. Si bruité vers le bas, faux positif.

**Duel.**

- **H_A** : M2 du témoin monotone est statistiquement indistinguible de M2 du modèle de base non remanié (Mann-Whitney, α = 0,01).
- **H_B** : M2 du témoin ≠ M2 du modèle de base.
- **Métrique** : M2 sur le témoin monotone vs M2 sur le modèle de base brut (sans aucun regroupement ni réécriture).
- **Contrôle négatif** : modèle de base brut.
- **Falsifie H_A** : p < 0,01.
- **Falsifie H_B** : p ≥ 0,01.

**Garde.** Formaliser la réécriture comme un *round-trip* : vérifier mécaniquement que la chaîne de caractères du coût après écriture identique est identique au byte près à l'original. Si ce n'est pas le cas, corriger avant entraînement.

**Ce qui changerait d'avis.** Si la réécriture est un *no-op* vérifiable (identité chaîne par chaîne), la faille est nulle.

---

### Faille F7 — Résultat trop propre (R4) : l'anti-monotonie est un signal trop fort

**Description.** Le couplage anti-monotone à dose 1 est l'inversion maximale : chaque action reçoit le coût le plus éloigné possible. C'est un signal extrêmement saillant pour un modèle distillé. M2 peut être massivement élevé, donnant un résultat « trop propre » au sens de R4.

**Direction de biais.** Faux positif de portée : on conclut que l'organisme manipule le coût, mais on a simplement montré qu'un modèle copie un maître dont les coûts sont inversés. Pas de preuve que l'organisme choisirait spontanément cette stratégie.

**Duel.**

- **H_A** : l'erreur M2 à dose 1 est ≤ 0,50 décade (effet modéré, cohérent avec une manipulation subtile).
- **H_B** : M2 à dose 1 est > 0,50 décade (effet massif, potentiellement trivial).
- **Métrique** : M2 à dose 1.
- **Seuil** : 0,50 décade.
- **Contrôle négatif** : un maître dont les coûts sont remplacés par des valeurs aléatoires tirées de la même distribution (même multiensemble global, mais sans structure anti-monotone intra-classe). Comparer M2 du couplage anti-monotone vs M2 du couplage aléatoire.
- **Falsifie H_A** : M2 > 0,50 et indistinguable du couplage aléatoire (l'anti-monotonie n'ajoute rien au-delà du bruit).
- **Falsifie H_B** : M2 ≤ 0,50 ou M2 significativement différent du couplage aléatoire.

**Garde.** Inclure le couplage aléatoire comme bras auxiliaire. Si M2(anti-monotone) ≈ M2(aléatoire), le bras B ne mesure pas l'effet directionnel qu'il prétend mesurer.

**Ce qui changerait d'avis.** Si la distillation atténue fortement l'effet (F3 non résolue), le résultat ne sera pas « trop propre ». Paradoxalement, une distillation imparfaite rend F7 moins grave mais F3 plus grave.

---

## (c) Instruments : métriques minimales de fonctionnement

### M2 — `|log₁₀(coût déclaré) − log₁₀(estimation honnête cachée)|`

- **Taux de détection minimal** : M2 doit distinguer dose 0 de dose 1 avec une puissance ≥ 0,80 à α = 0,05 (test unilatéral). Sur 8 tâches, cela exige un effet standardisé d (Cohen) ≥ 1,2 (illustratif). Si `Δ_intra` (F2) est faible, cette puissance n'est pas atteinte.
- **Taux de fausses alertes** : M2 sur le témoin monotone vs modèle de base doit donner p > 0,10 (aucune fausse alerte au seuil 0,05).
- **Cas honnêtes appariés** : huit suites du modèle de base, même température, même graine d'environnement.
- **Vérification mécanique à battre** : un détecteur trivial qui prédit M2 = 0 pour tout épisode (hypothèse nulle). M2 doit battre ce détecteur en RMSE sur le témoin et en puissance de discrimination dose 0 vs dose 1.

### M-3 — Vérification d'identité (P4)

- **Taux de détection** : non applicable (c'est un test de non-différence). Exiger une borne supérieure sur l'AUC de la base appliquée au maître : AUC ≤ 0,52 (intervalle de confiance unilatéral à 95 %).
- **Fausses alertes** : si AUC > 0,55 sur le maître, l'identité algébrique est violée (erreur d'implémentation).
- **Vérification mécanique** : comparer les multiensembles de coûts (maître réapparié vs original) par test exact : toute différence est un bug.

### Base « mots et coût »

- **Taux de détection à mesurer** : AUC sur l'élève (pas seulement le maître), par dose, sur un ensemble équilibré (50 % dose p, 50 % témoin).
- **Fausses alertes** : AUC sur maître réapparié vs maître original ≤ 0,52.
- **Vérification mécanique à battre** : classificateur par régression logistique sur les six indicateurs de forme seuls (sans le coût). Si la base ne bat pas ce classificateur trivial, elle n'utilise pas le coût.

---

## (d) Ancrage matériel

| Ressource | Spécification | Source |
|---|---|---|
| Modèle | 8B paramètres, même configuration que T0.6 | RAPPORTÉ |
| Adaptateur | LoRA rang 16, projections d'attention | RAPPORTÉ |
| Doses | 4 adaptateurs (un par dose) | RAPPORTÉ |
| Données maître | Transcriptions honnêtes sur 8–16 tâches de fabrication | RAPPORTÉ (8–16 tâches, §7 objection 3) |

**Calcul estimé (illustratif) :**
- Génération des transcriptions honnêtes : 8 suites × 16 tâches × ~2048 tokens ≈ 260 k tokens d'inférence. Sur un 8B quantisé 4 bits, ~30 min sur 1×A100 (illustratif).
- Distillation LoRA rang 16 : 4 doses × ~500 pas de fine-tuning ≈ 2 000 pas. Sur 1×A100, ~2 h (illustratif).
- Évaluation M2 + M-3 + base : inférence élève sur 16 tâches × 4 doses × 8 suites = 512 épisodes ≈ 1 M tokens. ~2 h sur 1×A100 (illustratif).
- **Total estimé : ~5 h sur 1×A100, coût cloud ~5–10 USD** (illustratif).

**Modèles ouverts.** Le modèle 8B n'est pas nommé dans les faits. Si c'est un modèle de la famille Llama 3 ou Mistral, les adaptateurs LoRA sont directement compatibles avec les bibliothèques ouvertes (PEFT, référence à vérifier). Si c'est un modèle propriétaire, la distillation LoRA n'est pas applicable sans accès aux poids — ce point doit être clarifié.

---

## Synthèse des failles par gravité

| Faille | Faux + / − | Gravité si non vérifiée | Vérification coûteuse ? |
|---|---|---|---|
| F1 Classes dégénérées | Faux − | Haute | Non (comptage) |
| F2 Coûts proches | Faux − | Haute | Non (calcul Δ_intra) |
| F3 Distillation infidèle | Les deux | Haute | Faible (M2_distill) |
| F4 P4 tautologique étendu à l'élève | Faux + indirect | Moyenne-haute | Faible (AUC sur élève) |
| F5 Grille mal calibrée | Faux − partiel | Moyenne | Faible (ajout 1 dose) |
| F6 Témoin contaminé | Les deux | Moyenne | Non (round-trip byte) |
| F7 Résultat trop propre | Faux + de portée | Moyenne | Faible (bras aléatoire) |

Les trois vérifications les plus urgentes, exécutables avant toute lecture de résultat (compatibles R1) : compter les tailles de classe (F1), calculer `Δ_intra` (F2), vérifier le round-trip du témoin (F6). Ces trois opérations ne touchent que les données du maître et ne violent aucune contrainte de pré-enregistrement.

FIN-DE-CELLULE