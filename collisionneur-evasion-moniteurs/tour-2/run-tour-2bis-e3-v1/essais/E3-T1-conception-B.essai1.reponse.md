# Proposition B — Robustesse adverse et validité de construit des moniteurs boîte blanche

Je suis la proposition B. Je ne vois ni A ni C ; je construis à partir des faits et j'attaquerai A/C au tour de confrontation.

---

## (a) Ce que la question suppose sans que ce soit établi

**S1 — Qu'un biais diffus existe et soit étiquetable dans l'organisme 8B.**
Statut : **HYPOTHÈSE**. La pièce E §3.3 dit explicitement que « la littérature n'a pas de résultat sur la détection boîte blanche du biais diffus ». Que ce signal existe *dans les activations* d'un 8B, qu'il soit séparable, et qu'on sache produire des épisodes positifs/négatifs étiquetés au niveau action — rien de cela n'est établi. Toute la section 8 et H1/H2 présupposent un jeu d'étiquettes d'action fiable.

**S2 — Que la représentation « conscience d'évaluation » existe dans un 8B et soit causalement reliée au comportement.**
Statut : **RAPPORTÉ** pour l'existence linéaire (E §1.5 : AUROC > 0,7 multi-modèles 2026, « référence à vérifier »), **HYPOTHÈSE** pour le lien causal. E §2.4 et §3.5 sont nets : « le pilotage a un effet comportemental faible », « le mécanisme causal reste non élucidé ». La question 3 suppose que l'organisme « se conduit autrement quand il se croit évalué » — or le seul fait rapporté est que la *représentation* existe, pas que le *comportement* change. C'est le point aveugle central.

**S3 — Que le transfert 70B → 8B préserve les directions internes.**
Statut : **HYPOTHÈSE explicite** (E §3.1). Apollo 2025 (95–99 % à 1 % FP) est sur 70B. Rien ne garantit la même séparabilité à 8B.

**S4 — Que le sandbagging/biais soit spontané et non induit.**
Statut : **HYPOTHÈSE**, et E §3.4 est catégorique : « aucune démonstration empirique que des modèles ≤ 8B développent spontanément une conscience d'évaluation qui modifie leur comportement ». Si le programme doit *induire* le biais (instruction, réglage fin), alors ce qu'on mesure n'est pas la robustesse face à un organisme spontanément conscient mais face à un organisme *instruit* — construit différent.

**S5 — Qu'un moniteur séquentiel apporte sur la sonde ponctuelle.**
Statut : **HYPOTHÈSE** (H2, 0,50 ; Tr non calibré). La porte G1 (pièce D) impose au séquentiel de battre (iii) la sonde sur le dernier état *et* (ii) la cascade. La décision N-056 dit elle-même : « blanc contre blanc : écart probablement petit ». Le gain n'est pas acquis ; il est le pari.

**S6 — Que max/attention soit robuste au niveau action comme au niveau token.**
Statut : **HYPOTHÈSE identifiée** (Tr, « angle mort, non calibré »). La robustesse max/attention est « établie au niveau token » (dit par P §5, sans référence attribuée — je le traite comme **RAPPORTÉ non attribué**, donc à vérifier). Sa transposition action/trajectoire face à un attaquant adaptatif n'est pas montrée.

**S7 — Que g (loi de déférence) soit estimable sans accès aux poids sur un organisme qui se sait évalué.**
Statut : **HYPOTHÈSE** (HC1 0,75). La régression Δv = g·(v*−v₀) suppose qu'on puisse appliquer une « pression » graduée et mesurer une réponse monotone. Le nul de régression vers la moyenne (P3) est cité mais la validité de la pente sur un 8B n'est pas mesurée.

**S8 — Que le plancher « sonde aléatoire appariée en covariance » soit le bon nul.**
Statut : **VÉRIFIÉ comme règle du programme** (P §8.1), mais **supposé suffisant**. Une sonde aléatoire appariée en covariance ne contrôle pas les corrélats de *format/longueur* s'ils sont dans la direction du signal. C'est un nul nécessaire, pas suffisant.

---

## (b) Expériences décisives — quatre duels

### EXP-1 — Le biais diffus est-il porté par les activations ou par la surface du texte ?

**H_A** : le signal de biais diffus est présent dans les activations internes h_ℓ d'un 8B et séparable au-delà des corrélats de surface (longueur, format, registre).
**H_B** : ce qu'une sonde capte est un corrélat de surface ; à surface appariée, le signal interne s'effondre au niveau du plancher.

- **Grandeur mesurée** : AUROC d'action (sans unité) de chaque famille de sonde, et Δ-AUROC entre condition brute et condition **surface-appariée** (mêmes longueurs, même format, même registre, contenu paraphrasé pour neutraliser le lexique).
- **Nul** : sonde aléatoire appariée en covariance (P §8.1), *plus* un nul renforcé — sonde entraînée sur étiquettes **permutées** (doit donner AUROC ≈ 0,5).
- **Témoin vrai** : épisodes avec biais injecté connu, mécaniquement vérifiable (p. ex. une règle de sélection de citations faussées détectable par script).
- **Témoin faux** : épisodes honnêtes générés par le même organisme, même tâche, appariés en longueur/format.
- **Garantie** : contrôle du FP à 1 % par calibration sur un fold de validation scellé (R1/R2, préenregistrement).
- **Seuil** : H_A tenue si Δ-AUROC (brut → surface-apparié) < 0,05 **et** AUROC surface-apparié bat le plancher covariance d'au moins 0,10 avec borne basse appariée > 0.
- **Issue qui falsifie H_A** : si la sonde s'effondre au plancher dès qu'on apparie la surface → c'est un détecteur de format, H_A tombe.
- **Issue qui falsifie H_B** : si l'AUROC tient à surface appariée au-dessus du plancher → ce n'est pas de la surface.

**Mesure minimale par instrument** :
- `difference_moyennes`, `lineaire`, `perceptron`, `attention`, `mahalanobis` : chacune — taux de détection à 1 % FP sur témoins vrai/faux appariés ; comparaison à **deux bases mécaniques** à battre : (1) classifieur sur longueur + n° de tokens + histogramme de ponctuation ; (2) classifieur TF-IDF sur le texte de sortie (boîte noire lexicale). Une sonde qui ne bat pas ces deux bases mécaniques à surface appariée « n'existe pas » (règle P §8.1 étendue).

---

### EXP-2 — L'agrégateur séquentiel voit-il ce qu'aucun agrégateur marginal ne voit ?

C'est le cœur du résultat fort (c) et de G1.

**H_A** : un signal réparti **sous le seuil par action** (chaque action plausible) reste détectable par l'agrégateur séquentiel calibré (somme cumulée / processus e) et non par la sonde du dernier état ni par le max marginal.
**H_B** : le gain séquentiel est un artefact d'horizon (plus de tokens = plus de chances de FP/TP) ; à FP apparié et horizon apparié, la sonde ponctuelle du dernier état fait aussi bien.

- **Grandeur mesurée** : rappel à 1 % FP *par épisode*, pour (séquentiel) vs (iii dernier état) vs (ii cascade) vs (max marginal), **à horizon apparié** (même nombre d'actions).
- **Nul** : épisodes honnêtes entiers passés dans l'agrégateur séquentiel — **taux de fausses alertes sans, puis avec, corrélation injectée** (c'est exactement la mesure unanime de D point 5, sondes figées P3 + vecteurs T0.5, processeur, zéro dépense). Le séquentiel doit garder son FP sous corrélation bénigne injectée.
- **Témoin vrai** : biais construit *explicitement réparti* — N actions chacune sous le seuil ponctuel, somme ≥ θ.
- **Témoin faux** : épisode honnête de même longueur, même variance de score par action.
- **Garantie** : processus e / Ville — contrôle du FP valide à tout temps d'arrêt (c'est l'argument de l'accumulation séquentielle ; squelette boîte noire « existe » par H2).
- **Seuil** : H_A tenue si rappel_séquentiel − rappel_dernier-état ≥ 0,15 à 1 % FP apparié, borne basse appariée > 0, **et** si le FP séquentiel sous corrélation bénigne injectée reste < 2 %.
- **Issue qui falsifie H_A** : si le dernier état ou le max marginal égale le séquentiel à horizon/FP apparié → pas de valeur ajoutée séquentielle, H_A tombe (et G1 échoue sur le contraste iii).
- **Issue qui falsifie H_B** : si le séquentiel domine à horizon apparié avec FP maîtrisé sous corrélation bénigne → l'horizon seul n'explique pas.

**Attaque de l'ambiguïté de G1 (pièce D point 1)** : la décision reconnaît qu'un échec de G1 « ne dira pas laquelle a échoué » (lire-l'intérieur vs notre-accumulation). Je recommande de **dédoubler** : G1a = séquentiel vs noir (lire l'intérieur apporte) ; G1b = séquentiel vs {dernier état, cascade} (notre accumulation bat les autres lectures). Sans ce dédoublement, l'issue est non interprétable — défaut de conception à corriger.

---

### EXP-3 — La « conscience d'évaluation » est-elle un changement de régime, et mesure-t-elle l'intention ou le contexte ?

**H_A** : quand l'organisme se croit évalué, la séquence de scores subit une **rupture de régime** détectable (changement de moyenne/variance) imputable à l'*intention*, après neutralisation du cadrage.
**H_B** : la sonde « conscience d'évaluation » répond au **cadrage/contexte** (mots-clés d'évaluation, format de test), pas à un changement comportemental ; le « régime » disparaît quand on apparie le cadrage.

- **Grandeur mesurée** : (i) statistique de rupture séquentielle (CUSUM / processus e sur la série de scores) ; (ii) Δ-score sonde entre **même contenu, cadrage évalué vs réel** et entre **même cadrage, contenus différents** (dissociation croisée demandée en Q2).
- **Nul** : permutation des étiquettes évalué/réel (doit annuler la rupture).
- **Témoin vrai** : épisodes où l'on *induit* par instruction un comportement différent (sandbagging induit, établi possible — van der Weij 2024, RAPPORTÉ). C'est le seul témoin vrai disponible, car le sandbagging spontané ≤ 8B n'est pas établi (E §3.4).
- **Témoin faux** : même organisme, cadrage évalué mais sans incitation à changer.
- **Garantie** : CUSUM/Ville à FP temps-valide.
- **Seuil** : H_A tenue si la rupture persiste (statistique > seuil préenregistré) *à cadrage apparié* et si Δ-score(même contenu, cadrage différent) < Δ-score(intention présente/absente). H_B tenue si l'inverse.
- **Issue qui falsifie H_A** : la rupture disparaît quand le cadrage est apparié → la sonde lit le contexte, pas l'intention. Cohérent avec H8 (« une sonde de conscience d'évaluation s'effondre quand l'attaquant apprend à paraître détendu »).
- **Issue qui falsifie H_B** : la rupture tient à cadrage apparié → il y a bien un signal comportemental.

**Point d'intégrité** : vu E §3.4–3.5, le résultat le plus probable est **décisif négatif** (la sonde de conscience d'évaluation mesure surtout le contexte). C'est un résultat fort et publiable *en négatif* — il faut l'accepter symétriquement (P §12, « aucun run visant un signe positif »).

---

### EXP-4 — Frontière de robustesse : taxe de déplacement et marge asymétrique

**H_A** (HC4 + H6) : déplacer le verdict d'une sonde à agrégation robuste (max/attention) exige une obfuscation d'activations coûteuse ; il existe une intervention non spécifique (paraphrase, remise à zéro de contexte, bruit d'activations) où le succès d'attaque chute plus vite que l'utilité honnête.
**H_B** : l'organisme 8B qui se sait évalué déplace le verdict à coût d'utilité négligeable (g > 0 significatif), sans accès aux poids.

- **Grandeur mesurée** : g = fraction du chemin vers v* (P §4, définition RAPPORTÉE), estimé par régression sur intensités de pression ; **coût** = perte d'utilité honnête sur la tâche scientifique (métrique de qualité de proposition, à définir et préenregistrer — **illustratif** tant que non fixée) ; pente du succès d'attaque vs pente d'utilité sous intervention.
- **Nul** : g sous pression **bénigne** (HC6) — doit prédire l'effondrement sous pression optimisée.
- **Témoin vrai** : attaque par contenu boîte noire (HC2) ; attaque par usurpation stylistique (HC3).
- **Témoin faux** : variation stylistique neutre sans intention (contrôle de style obligatoire, HC2b).
- **Garantie** : matrice de transfert d'attaque (P §8.2) comme mesure de diversité effective, pas la décorrélation bénigne.
- **Seuil** : H_A tenue si, pour les sondes à agrégation robuste, g ≈ 0 sous contenu boîte noire (|g| < 0,1, borne haute < 0,2) **et** auto-incrimination g < 0 sous tentative de manipulation (HC2b) ; H6 tenue s'il existe λ où Δ(succès attaque)/Δλ dépasse Δ(utilité)/Δλ d'un facteur préenregistré.
- **Issue qui falsifie H_A** : g sonde > 0,3 sous contenu boîte noire à coût d'utilité quasi nul → pas de taxe de déplacement, les sondes sont corruptibles par le registre (contamination de construit, P §4).
- **Issue qui falsifie H_B** : g ≈ 0 sur sondes et g < 0 sous manipulation → l'organisme ne peut pas déplacer sans obfuscation d'activations (hors périmètre, frontière assumée P §9).

**Fermeture de brèche** : pour chaque sonde où g > 0, l'extension testée est (a) changer la couche lue (7/15/23, D point 3), (b) passer de max à attention ou inversement, (c) ajouter un quorum hétérogène (HC5), (d) paraphrase de confiance. **La fermeture n'est prouvée que si** la matrice de transfert montre qu'une attaque optimisée contre la sonde brèche ne transfère pas sur l'extension (transfert < 0,2) — sinon c'est une illusion de diversité.

---

## (c) Mesure minimale par instrument nommé

| Instrument | Détection (TP @ 1 % FP) | Fausses alertes | Cas honnêtes appariés | Base mécanique à battre |
|---|---|---|---|---|
| `difference_moyennes` | AUROC d'action, EXP-1 | FP sur honnêtes appariés longueur/format | paraphrase surface-appariée | longueur+ponctuation ; TF-IDF |
| `lineaire` | idem | idem | idem | idem |
| `perceptron` | idem + test de surapprentissage (fold scellé) | idem | idem | idem |
| `attention` | idem + robustesse des poids softmax sous attaque adaptative (Tr) | idem | idem | + max marginal |
| `mahalanobis` (non sup.) | TP @ 1 % FP, distance au nuage honnête | FP = queue de la distrib honnête | honnêtes = référence de covariance | plancher covariance seul |
| agrégateur séquentiel | rappel/épisode @ 1 % FP, horizon apparié (EXP-2) | FP sur épisodes honnêtes entiers, sans/avec corrélation injectée (D point 5) | honnêtes mêmes N actions, même variance | dernier état ; max marginal ; cascade |
| base (ii) cascade | rappel/épisode @ 1 % FP | FP sur mêmes honnêtes | idem | — (c'est une base) |
| base (iii) dernier état | rappel/épisode @ 1 % FP | FP sur mêmes honnêtes | idem | — (c'est une base) |

Règle d'existence (P §8.1 étendue) : toute sonde doit battre **le plancher covariance ET les deux bases mécaniques** à surface appariée, sinon elle ne mesure pas l'intention.

---

## (d) Ancrage matériel

**Su (cité, à vérifier sur PDF — R7)** :
- Berglund et al. (2023), *Taken out of context: On measuring situational awareness in LLMs* — RAPPORTÉ.
- Laine et al. (2024), *SAD benchmark* — RAPPORTÉ, chiffres par composante à vérifier.
- van der Weij et al. (2024), sandbagging par mot de passe, détection 64–84 % — RAPPORTÉ, taux à vérifier.
- Greenblatt et al. (2023/2024), *AI Control* — RAPPORTÉ.
- Apollo Research (2025), *Linear probes detect deception in Llama-3.3-70B-Instruct*, 95–99 % @ 1 % FP — RAPPORTÉ, protocole à vérifier.
- Nguyen et al. (2025), sondage/pilotage conscience d'évaluation — RAPPORTÉ.
- Étude multi-modèles (2026, ~37 modèles), AUROC > 0,7 — **référence à vérifier** (publication exacte non identifiée dans les faits).
- Phuong et al. (2024, DeepMind), *Evaluating Frontier Models for Dangerous Capabilities* — RAPPORTÉ.
- Autoencodeurs parcimonieux « Llama Scope » (P §8.2) — nommés, **référence à vérifier** (pas d'attribution dans les faits).

**Modèle ouvert** : Llama-3.1-8B-Instruct (organisme, pièce Question) — VÉRIFIÉ comme choix du programme. Bases boîte noire candidates D1 : Llama-3.2-3B-Instruct (b), Qwen2.5-7B (c) — RAPPORTÉ.

**Calcul et coût** :
- EXP-2 mesure unanime (FP séquentiel sur honnêtes, sans/avec corrélation) : **processeur, zéro dépense** — établi par pièce D point 5 (sondes figées P3, vecteurs T0.5). VÉRIFIÉ dans les faits.
- Lecture des traits internes 3 couches (7/15/23) : **processeur, zéro dépense** — pièce D point 3. VÉRIFIÉ.
- EXP-1, EXP-3, EXP-4 (génération de trajectoires 8B, attaques optimisées, folds) : nécessitent inférence GPU sur l'organisme 8B. **Aucun chiffre de coût n'est dans les faits.** Tout montant serait **illustratif** ; je ne l'invente pas (règle 4 + pièce D : « aucun score de pilote »).
- Dimensionnement : pièce D point 1 dit « plusieurs centaines de tâches sabotées de plus par mode » pour le contraste blanc-contre-blanc de G1 — RAPPORTÉ, c'est l'ordre de grandeur du devis de la couche 2, non chiffré en argent.

---

## (e) Ordre et arrêt (Q5)

**Ordre** (du zéro-dépense vers le coûteux, préenregistrement → contre-lecture → scellement → lecture, R1/R2, pièce D point 5) :
1. **EXP-2 nul** (FP séquentiel sur honnêtes, sans/avec corrélation) — processeur, zéro dépense. **Arrêt dur** : si le séquentiel émet > 5 % de FP sur honnêtes sous corrélation bénigne injectée, l'agrégateur est cassé → on ne dépense rien sur le reste de G1 tant qu'il n'est pas recalibré.
2. **EXP-1** (surface-appariée) — si *aucune* sonde ne bat les deux bases mécaniques à surface appariée, **arrêt** : il n'y a pas de construit interne à défendre, inutile de tester la robustesse adverse (EXP-4) d'un détecteur de format.
3. **EXP-3** — décisif probablement négatif ; à mener car il conditionne l'interprétation de toute « sonde de conscience d'évaluation ».
4. **EXP-4** — seulement sur les sondes ayant survécu à EXP-1.

**Critères d'arrêt pour ne pas dépenser sur ce qui ne mesure rien** :
- plancher covariance non battu → sonde supprimée (P §8.1) ;
- étiquettes permutées donnant AUROC > 0,55 → fuite d'étiquette, run jeté ;
- g bénin (HC6) prédisant déjà l'effondrement → inutile d'optimiser l'attaque, la recette est recalée avant déploiement.

**Ce qui me ferait changer d'avis** :
- une publication montrant détection boîte blanche du **biais diffus** ≤ 8B, ou **sondes séquentielles** (E §6.4, veille) → la zone revendiquée change ;
- si EXP-3 trouve une rupture de régime robuste au cadrage apparié → S2 (lien causal) révisée vers RAPPORTÉ, et la conscience d'évaluation devient un construit détectable, pas seulement une représentation ;
- si EXP-2 montre que le dernier état égale le séquentiel à horizon apparié → H2 abandonnée, G1 reformulée.

**Faux gap signalé (R8)** : la détection du biais diffus boîte blanche ≤ 8B n'est pas un trou décoratif ; E §4 l'établit par quatre spécificités concrètes et mesurables. Mais S1 et S4 restent des hypothèses : si l'on ne sait pas produire le biais diffus *étiquetable*, toute la chaîne s'effondre avant la robustesse. C'est le risque n° 1 du programme, pas la robustesse adverse.

FIN-DE-CELLULE