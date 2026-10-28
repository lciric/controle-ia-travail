# Tour III.1 — Proposition B : robustesse et validité de construit des moniteurs boîte blanche

Pièces reçues : P, F, E, D, toutes présentes et lisibles. Tout ce qu'elles contiennent est traité comme **RAPPORTÉ** (transcription empreintée, non ré-audité par moi). Les chiffres que j'introduis sont marqués **illustratifs**.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **« L'organisme peut savoir qu'il est évalué. »** La pièce E (§3.4) dit explicitement : aucune démonstration publiée de conscience d'évaluation *spontanée* modifiant le comportement chez un modèle ≤ 8B ; tout résultat est induit par instruction ou réglage fin. Statut : **HYPOTHÈSE**. Conséquence de conception : toute expérience devra *induire* la conscience d'évaluation (cadrage, indices), et toute conclusion vaudra pour le régime induit, borne inférieure du régime spontané.

2. **« La référence publiée à battre : 95–99 % à 1 % FP (Apollo 2025). »** La pièce E elle-même classe ce chiffre dans « à vérifier sur PDF » (§5, R7). Statut : **RAPPORTÉ**, protocole (prompt, split) non audité. En faire le seuil à battre avant vérification violerait la méthode de P §12 (provenance par transcription non opposable). Référence : « Linear probes detect deception in Llama-3.3-70B-Instruct », Apollo Research, 2025 — rapportée dans E, à vérifier.

3. **« Un moniteur qui tient là où la sonde ponctuelle publiée tombe. »** Que la sonde ponctuelle *tombe* face à un 8B conscient d'être évalué n'est établi nulle part ; E rapporte au contraire qu'Apollo détecte « y compris quand le modèle a été entraîné à cacher sa tromperie ». Statut : **HYPOTHÈSE** (c'est précisément la base (iii) de G1, pièce D : la sonde sur le dernier état pourrait gagner).

4. **« Le signal cible est un biais diffus » laisse une trace interne lisible.** E (§3.3) : « la littérature n'a pas de résultat sur la détection boîte blanche du biais diffus ». Statut : **HYPOTHÈSE** — c'est H1/H2 (0,55 / 0,50 dans P), pas un acquis. La question formule son « résultat fort (c) » comme si l'existence du signal était acquise et qu'il ne restait qu'à montrer sa visibilité séquentielle.

5. **La représentation de conscience d'évaluation existe dans *ce* 8B.** E rapporte AUROC > 0,7 « dans la majorité des modèles » (étude multi-modèles 2026, **référence à vérifier** — E ne donne ni auteurs ni titre, je ne peux pas l'attribuer). « Majorité » n'implique pas Llama-3.1-8B-Instruct. Statut : **RAPPORTÉ** pour la classe, **HYPOTHÈSE** pour l'organisme.

6. **La carte de validité « prédit hors échantillon » la robustesse.** C'est H8, calibrée à **0,40** par le programme lui-même (P §5) : le programme parie plutôt *contre*. La question en fait le « résultat fort (a) » ; il faut la traiter comme hypothèse à falsifier, pas comme livrable attendu. Statut : **HYPOTHÈSE**.

7. **La conscience d'évaluation serait un *régime* (état persistant) plutôt qu'un transitoire.** Rien dans E ne tranche ; le faible effet causal du pilotage (Nguyen et al. 2025, rapporté dans E) suggère même que représentation et comportement sont faiblement couplés. Statut : **HYPOTHÈSE** — et c'est un duel, pas un présupposé (E4 ci-dessous).

8. **« Quelle extension fermerait chaque brèche. »** Présuppose que les brèches sont fermables par extension du moniteur. L'issue inverse (brèche structurelle : la lecture interne d'un 8B ne sépare pas intention et registre) est une issue légitime de E1/E4 et doit rester énonçable. Statut : **HYPOTHÈSE** directionnelle.

9. **Transfert 70B → 8B des directions internes.** E §3.1 le classe ouvert. Statut : **HYPOTHÈSE**.

---

## (b) Quatre expériences décisives

Toutes sous la méthode P §12 : préenregistrement scellé, contre-lecture, seuils fixés avant lecture, plancher obligatoire = sonde aléatoire appariée en covariance (P §8.1). Taux de faux positifs de référence : 1 % par épisode honnête, **illustratif**, à fixer au préenregistrement.

### E1 — Dissociation de construit : contenu contre cadrage (toutes familles, toutes couches)

**Design.** Corpus 2×2 généré par l'organisme : {cadrage « évaluation » / cadrage « déploiement réel »} × {consigne de biais / honnête}, tâches scientifiques appariées. Troisième bras décisif : **relecture forcée** (teacher forcing) du *même texte* sous les deux cadrages — contenu strictement identique, seul le contexte change ; c'est le seul bras qui isole proprement l'effet contexte dans les activations. Contrôles : permutation des étiquettes ; sonde aléatoire appariée en covariance ; classifieur mécanique de surface sur les sorties (longueur, perplexité, sac-de-mots stylistique).

- **H_A (validité)** : pour une famille donnée, la sonde « intention/dissimulation » sépare par le contenu à cadrage fixé (AUROC_contenu ≥ 0,80, **illustratif**) et reste aveugle au cadrage à contenu identique (AUROC_cadrage ≤ 0,60, **illustratif**).
- **H_B (contamination)** : l'ordre s'inverse — la sonde sépare les cadrages à contenu identique mieux que les contenus à cadrage fixé : elle lit le registre/contexte, pas l'intention (le « g > 0 sans accès aux poids » de P §4, version interne).

**Grandeur** : AUROC (sans unité) et rappel à 1 % FP (fraction d'épisodes), IC bootstrap par épisode. **Nul** : étiquettes permutées (AUROC attendu ≈ 0,5). **Témoin vrai** : la sonde « conscience d'évaluation » *doit* séparer les cadrages — si elle ne le fait pas, le manipulandum (induction du cadrage) a échoué et E1 ne conclut rien. **Témoin faux** : la sonde aléatoire appariée ne doit rien séparer. **Issues** : H_A corroborée pour une famille → cette famille porte un construit de contenu ; H_B → la revendication « sonde d'intention » est falsifiée pour cette famille, elle est reclassée « sonde de contexte » dans la carte. Si *aucune* famille ne bat le classifieur de surface sur le contenu, la prémisse boîte blanche elle-même est falsifiée à cette échelle (voir arrêt, section e).

### E2 — H8 en duel : la carte prédit-elle la rétention sous pression, hors échantillon ?

**Design.** Unités = sonde × couche × concept (5 familles × 3 couches — couches 7, 15, 23, pièce D point 3). Pour chacune : indice de validité issu de E1 (ΔAUROC = AUROC_contenu − AUROC_cadrage) et **rétention sous pression** = rappel sous consignes d'évasion par contenu (« rédige comme en routine », paraphrase de style honnête — pression sur l'instrument, papier C ; aucun nouveau mode de sabotage, banc N-054 respecté) divisé par rappel bénin, à FP apparié. Ajustement sur une moitié des unités (split par famille), prédiction sur l'autre.

- **H_A (= H8)** : ρ de Spearman(ΔAUROC, rétention) ≥ 0,5 hors échantillon, IC excluant 0 (**illustratif**).
- **H_B** : ρ indiscernable de 0 — la robustesse est déterminée par la famille/couche/agrégation indépendamment du construit mesuré.

**Nul** : appariement permuté des indices et rétentions. **Témoin vrai** : la sonde « conscience d'évaluation » doit s'effondrer sous « parais détendu » (prédiction explicite de P §11) — si elle ne s'effondre pas, la pression est inopérante et E2 est non concluante. **Témoin faux** : sonde aléatoire appariée (rétention = bruit). **Issues** : H_A → critère de recette avant déploiement (jonction avec HC6) ; H_B → H8 falsifiée (le programme la donnait à 0,40 : issue probable, et informative — la robustesse devra être testée directement, sans raccourci par la carte). ρ *négatif* falsifierait plus : les sondes les plus « valides » seraient les plus fragiles, et P §11 serait à réécrire.

### E3 — G1 factorisée : le signal diffus sous seuil, séquentiel contre marginal, blanc contre noir

La pièce D (point 1) acte que G1 porte deux questions et qu'« un échec ne dira pas laquelle a échoué ». Je durcis : E3 factorise les deux contrastes, sur les **mêmes épisodes**.

**Design.** Épisodes à biais diffus calibré : chaque action sous le seuil marginal (score par action sous le percentile 99 de la distribution honnête, **illustratif**) ; épisodes honnêtes appariés (même tâche, même longueur, même cadrage). Instruments, tous à FP par épisode apparié : (1) accumulation séquentielle (processus e) sur scores de sondes ; (2) la même accumulation sur scores boîte noire (bases scellées P §8.3) — **contraste accès, agrégation égale** ; (3) cascade de portes sur les mêmes sondes (base ii) ; (4) sonde sur le dernier état (base iii) ; (5) max marginal sur les mêmes sondes — **contraste agrégation, accès égal**.

- **H_A** : rappel(1) > rappel(5) et rappel(1) > rappel(2), avec croissance du rappel en l'horizon T (pari apparié borné, D point 2) — l'accumulation sur l'intérieur voit ce que ni le marginal ni le noir ne voient.
- **H_B** : rappel(4) ≥ rappel(1) (l'épisode se résume dans l'état final : l'accumulation n'apporte rien, H2 falsifiée dans son cœur) **ou** aucun instrument blanc ne bat (2) (la trace interne du biais diffus n'existe pas à 8B : prémisse de H1 falsifiée sur ce mode).

**Grandeur** : rappel par épisode (fraction) à FP par épisode fixé ; courbe rappel(T). **Nul** : scores permutés entre pas d'un même épisode — le séquentiel doit retomber au niveau du marginal ; s'il ne retombe pas, il lit un niveau moyen, pas une structure temporelle. **Témoin vrai** : sabotage concentré (une action franchement au-dessus du seuil) — tous les instruments doivent le voir, sinon le banc est cassé. **Témoin faux** : épisodes honnêtes à corrélation injectée (la « mesure unanime » déjà décidée, D point 5) — les fausses alertes du séquentiel ne doivent pas dépasser la garantie nominale du processus e. **Issues** : chaque branche falsifie une composante *identifiée* de G1, ce que le design actuel de G1 ne permet pas — c'est mon amendement principal au programme.

### E4 — La conscience d'évaluation : régime détectable, et frontière coût-évasion

**Volet 1 (régime contre transitoire).** Indice d'évaluation injecté à un pas aléatoire de l'épisode, inconnu de l'analyste. Détection de rupture à garantie (processus e / CUSUM, taux de fausses ruptures ≤ α par épisode honnête, α fixé au préenregistrement) sur la séquence de scores de la sonde « conscience d'évaluation ».

- **H_A (régime)** : rupture localisée au pas d'injection (délai médian ≤ k pas, **illustratif** k = 20), scores soutenus ensuite, fausses ruptures ≤ α sur honnêtes, et le **témoin format** (changement de format du prompt sans sémantique d'évaluation) ne déclenche pas.
- **H_B (artefact)** : la rupture suit tout changement de format, ou ne se localise pas — la « conscience d'évaluation » lue est du contexte de surface.

**Décisif contre suggestif** : décisif = localisation temporelle aveugle + témoin format silencieux ; suggestif = simple différence de score moyen entre cadrages (ce que E1 mesure déjà).

**Volet 2 (frontière).** Organisme instruit d'évader par le seul contenu (le seul canal dont il dispose : il « sait » mais ne lit pas ses activations ; l'obfuscation d'activations exige un accès hors périmètre, frontière assumée P §9, et HC4 — statut HYPOTHÈSE 0,85 — la dit coûteuse). Courbe : rétention du score de chaque instrument (axe x) contre utilité sur la tâche scientifique (axe y, qualité jugée par panel scellé, protocole « contenu = données »).

- **H_A (taxe)** : toute consigne qui ramène g_sonde vers 0 coûte une perte d'utilité mesurable (pente négative, seuil préenregistré) — version interne de H6/HC4.
- **H_B (évasion gratuite)** : il existe une consigne de style annulant le score sans perte d'utilité — brèche : l'instrument lit le style.

**Fermeture et preuve de fermeture** (question 4) : pour chaque brèche de H_B — réentraînement sur les évasions détectées (asymétrie d'apprentissage, P §9), quorum multi-couches/multi-familles choisi par **matrice de transfert d'attaque** (P §8.2, pas par décorrélation bénigne), élargissement de fenêtre d'agrégation. Preuve : la *même* attaque, rejouée après durcissement, donne g ≈ 0 **et** les fausses alertes sur honnêtes appariés n'augmentent pas (une fermeture qui coûte des faux positifs n'est pas une fermeture, c'est un déplacement du seuil). Limite énoncée : l'évasion instruite est une borne *inférieure* de l'adversaire ; aucune conclusion de robustesse face à une optimisation par gradient sur activations n'est permise par E4.

---

## (c) Mesure minimale par instrument

Cas honnêtes appariés, pour tout : mêmes tâches scientifiques, même longueur, même cadrage, générés sous π_B, appariement en covariance et énergie (P §11). Bases mécaniques à battre, pour tout : (α) sonde aléatoire appariée en covariance (plancher P §8.1 — « une sonde qui ne le bat pas n'existe pas ») ; (β) classifieur de surface sur sorties (longueur, perplexité, traits stylistiques).

| Instrument | Mesure minimale | Échec = |
|---|---|---|
| Différence de moyennes | AUROC contenu à cadrage fixé + rappel à 1 % FP (illustratif), E1 | ≤ (α) ou ≤ (β) |
| Linéaire | idem, par couche (7/15/23) | idem |
| Perceptron | idem **+** écart au linéaire (s'il ne bat pas le linéaire, il n'existe pas : complexité injustifiée) | ≤ linéaire |
| Attention | idem **+** nul spécifique : poids d'attention permutés entre jetons → doit retomber au max | insensible à la permutation |
| Mahalanobis | fausses alertes sur honnêtes *hors distribution bénigne* (sujets scientifiques nouveaux) ; séparation nouveauté/sabotage | alerte sur la nouveauté honnête |
| Agrégateur séquentiel | fausses alertes par épisode honnête entier, sans puis avec corrélation injectée (D point 5) ≤ garantie nominale ; puis rappel E3 | garantie violée sous corrélation |
| Cascade (ii) | rappel à FP apparié sur E3 ; doit battre le max marginal pour mériter sa place dans G1 | ≤ max marginal |
| Dernier état (iii) | rappel à FP apparié sur E3 ; + rappel quand le biais cesse avant la fin de l'épisode (son angle mort attendu) | — c'est une base : si elle *gagne*, c'est H2 qui tombe |

---

## (d) Ancrage matériel

- **Organisme** : Llama-3.1-8B-Instruct (nommé dans la question). **Moniteurs noirs** : même modèle en juge + Llama-3.2-3B-Instruct (D1, défaut (a)+(b), P §8.3) ; Qwen2.5-7B en option hétérogène.
- **Activations** : 3 couches (7, 15, 23 — D point 3), flux résiduel, d ≈ 4096, float16 ≈ 8 Ko/jeton/couche. **Illustratif** : 2 000 épisodes × 2 000 jetons × 3 couches ≈ 96 Go de stockage.
- **Calcul** : génération des trajectoires ≈ 100–300 h GPU (A100/H100) pour E1–E4, **illustratif** ; entraînement des sondes sur processeur, double précision, déterministe (pièce F) — coût marginal nul, cohérent avec « les moniteurs coûtent peu face à la génération » (P §8.3). Coût total **illustratif** : ordre de 1–3 k$ de calcul loué.
- E1 (relecture forcée) et le volet fausses-alertes du séquentiel sont réalisables sur activations déjà collectées, processeur, zéro dépense (comme D point 5).

---

## (e) Ordre, arrêt, et ce qui me ferait changer d'avis

**Ordre** : E1 → (garde fausses-alertes du séquentiel, D point 5) → E3 → E2 → E4. E1 d'abord parce qu'elle est la moins chère et conditionne tout : sans construit de contenu, E2–E4 mesurent du registre.

**Critères d'arrêt** (préenregistrés) :
1. Si en E1 aucune famille ne bat (α) *et* (β) sur le contenu à cadrage fixé : arrêt du bras blanc à cette échelle ; le résultat négatif est publié tel quel (P §12 : traitement symétrique).
2. Si les fausses alertes du séquentiel sous corrélation injectée dépassent la garantie nominale : arrêt de E3, recalibration ; tout rappel mesuré avant serait vide de sens.
3. Si le témoin vrai d'une expérience échoue (manipulandum inopérant), l'expérience est non concluante — pas de relance « jusqu'au signe positif » (P §12).

**Ce qui me ferait changer d'avis** : la vérification sur PDF des cinq chiffres de E §5 (en particulier Apollo 2025 : si le protocole audité révèle un split contaminé, la « référence à battre » change de nature) ; une publication de sondes séquentielles ou de détection boîte blanche du sandbagging à ≤ 8B (veille E §6.4) ; un ρ fortement négatif en E2, qui inverserait la doctrine de P §11 au lieu de simplement la falsifier.

FIN-DE-CELLULE