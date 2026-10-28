# Contre-lecture (R2) — « Le pari de signe, second type d'engagement du pôle — conception v1 »

- **Contre-lecteur** : sous-agent neuf, Opus 5.5. L'auteur de la pièce est Fable 5.1. Je n'ai écrit aucune ligne de la pièce.
- **Heures lues sur `date -u`** : début de la contre-lecture le mardi 27 octobre 2026 à 17:12:57 UTC ; rédaction du rapport à partir de 17:36:04 UTC.
- **Aucun fichier du dépôt n'a été modifié.** Tout ce que j'ai écrit est dans
  `/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-pari-signe/`.

**Fichiers de la pièce lus** (empreintes SHA-256 ; les trois sont conformes à leurs compagnons `.sha256`) :

| fichier (dossier `…/envois/pole-scientifique-automatique-v1/pari-de-signe/`) | SHA-256 |
|---|---|
| `conception-pari-de-signe-v1.md` | `50ce6842f0c087afa086db814222a5d0595f610f3cfda04d5a6a860b5d7822c0` |
| `simulation-dimensionnement-v1.py` | `6643f5f102d89b0e7a89b1905818cecab6b7a6d398da5b548fb7157e912a40f7` |
| `simulation-dimensionnement-v1-sortie.json` | `30b85423ca00f275844eed99ee81a673644b490e6f67854ad3f783d201ca1ea4` |

**Autres fichiers lus, et seulement ceux-là** :
- `orchestrateur-pole-v7/pole/selection_pari.py` (`9ff9d80f2b023401028d42d43211b9b7645c44ef6bfe0bacdc9847c5c63567d3`) : `trajectoire_numerateur`, `evaluer`, `_traj_urne`, et pour le contexte l'en-tête et les fonctions voisines.
- `orchestrateur-pole-v7/pole/cycle.py` (`a150eb00d5578a8bc4b558bda250d0f592a0a95079aa3fda179ffe9062c8c936`) : `appliquer_multiplicite`.
- Sur `main`, en lecture seule : `docs/programme-controle-ia-v2.md` (`2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c`), sections 4, 5, 8 et 10.
- Sur `main` : `docs/decisions/decision-N-007-N-008-v1.md` (`ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232`) et `docs/decisions/decision-N-054-v1.md` (`c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f`).

Je n'ai ouvert ni les lectures, ni les messages, ni les autres conceptions, ni `question-collisionneur-pari-de-signe-v1.md`.

**Mes scripts et leurs sorties** (même dossier ; interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B`, numpy 2.5.4) :

| fichier | rôle | SHA-256 |
|---|---|---|
| `contre-simulation-pari-signe-v1.py` | ma simulation indépendante : vectorisée, graines par `SeedSequence(7182818284)`, une graine dérivée par section | `cfc090707c4c46520fc324ba3a6cc1527eff326025ae8426cc091ed716ecec5b` |
| `contre-simulation-pari-signe-v1-sortie.json` | sa sortie : 1 000 répétitions de base ; 2 000 pour les niveaux ; 500 pour les jumeaux | `3526b766f29ea0fd99702da5ed7b1bbcd738e579c0e85a95f98682bde659067b` |
| `contre-simulation-complements-v1.py` | compléments : héritage, sélection, calibrage de 500 tâches ; graine `16180339887` | `ca98b83ceb355f698c2d1a7546752a07f2234db543a1f2315a7dab0aaf6326f0` |
| `contre-simulation-complements-v1-sortie.json` | sa sortie | `84bdc4c171724c9497016e6bbc161bc7af14b72e9813ed591257da7ca6c99aa7` |
| `contre-simulation-lecture-unique-v1.py` | test de Student lu une seule fois, comparé au pari ; graine `2718281828` | `3d0c2d7d846398da871d465d0a6b857765621be6caf43fbd70c8704cb71443ba` |
| `contre-simulation-lecture-unique-v1-sortie.json` | sa sortie | `212f8049b56133c18a8c0025bd52d85a5d057c0749ca3fb8a533cc776c97fc45` |
| `verification-analytique-signe-v1.py` | calculs exacts : espérance du signe, dérives, pente de la courbe de détection | `98f660f456e92898fcf0ee900eead3f6c86a7d70a902ba54a187b31e9e53c7f3` |
| `verification-analytique-signe-v1-sortie.txt` | sa sortie | `cc2850871dedb7ac0e2897dc69ad61aaf5df33ed8b654aaf7d5cc2cc7e5cdfdd` |
| `relance-script-auteur-sortie-v1.json` | relance du script de l'auteur (graine 20261027) : **identique à l'octet près** à la sortie citée | `30b85423ca00f275844eed99ee81a673644b490e6f67854ad3f783d201ca1ea4` |

---

## Verdict

**Amender, pas refaire.** L'ossature tient : la tâche comme unité, un contraste borné, un nul fixe, le produit Π(1 + λ·v), Ville, la garde par union des nuls, la variante sans remise. Les chiffres cités sont bien ceux de la sortie, et je retrouve leurs ordres de grandeur.

Mais quatre défauts touchent la garantie et bloquent tout usage décisif :
1. **La forme « signe » teste un autre nul.** Le mélange qui l'inclut n'est pas une surmartingale sous « E[v] ≤ 0 ». Reproduit : jusqu'à 0,74 de promotions sous un nul de moyenne nulle.
2. **Le bruit des seuils de calibrage fait promouvoir « A meilleur que B » entre deux moniteurs de même loi**, dans 13 à 19 % des cas, et la garde ne le voit pas.
3. **La dépendance par organisme casse le niveau** dès que l'affirmation dépasse les organismes du banc.
4. **H2a choisit sa sous-population sur les scores du comparateur.**

S'y ajoute un cinquième défaut : l'héritage de preuve sur une banque relue.

---

## Constats, du plus grave au moins grave

### C1 — La forme « signe » ne teste pas le nul déclaré : le mélange des deux formes n'est pas une surmartingale sous « E[v] ≤ 0 »

**Où dans la pièce.**
- Section 2.1 (« Signe pur »).
- Section 2.2 : « un mélange de surmartingales en est une : la garantie tient ».
- Sections 3.1 et 6 ; décision D-S2 ; contrôles 1, 3, 7 et 9.

**Ce qui est faux.**
- Le facteur 1 + λ·signe(v) n'a pas une espérance ≤ 1 sous E[v] ≤ 0. Le signe teste un autre nul : « P(v > 0) ≤ P(v < 0) », c'est-à-dire A ne fait pas mieux sur la majorité des tâches. Ce n'est pas « l'espérance du contraste est ≤ 0 ».
- **Contre-exemple exact.** v = +0,1 avec probabilité 0,9, et v = −0,9 avec probabilité 0,1. Alors E[v] = 0, mais E[signe] = +0,8. La composante signe à λ = 0,6 gagne alors +0,33 nat par tâche.
- **Argument général.** Pour le nul « toutes les lois sur [−1 ; 1] d'espérance ≤ 0 », toute e-valeur à un pas est dominée par 1 + λ·v avec λ ∈ [0 ; 1] (par l'enveloppe concave et un sur-gradient en 0). Aucune mise fondée sur le signe ne l'est.
- **Conséquence.** Le mélange n'est valide que pour l'intersection des deux nuls. Sa promotion établit « E[v] > 0 **ou** P(v > 0) > P(v < 0) ». Or G1, H1, H2, H3 et « rappel ≥ x » portent sur des **espérances** de rappel.

**Pourquoi les contrôles de la pièce ne le voient pas.** Les contrôles 1 et 3 et le niveau de la section 6 n'emploient que des nuls **symétriques** : échange de A et B, ±0,6 moitié-moitié, 0,5 contre 0,5. Sous ces nuls, E[signe] = 0.

**Reproduit.** Contre-simulation, sections C et I, 2 000 répétitions ; voir aussi `verification-analytique-signe-v1-sortie.txt`.

| nul de moyenne exactement nulle | 30 tâches | 60 | 100 | 150 | 250 | forme parts seule (maximum) |
|---|---|---|---|---|---|---|
| S1 : 90 % des tâches à +0,10, 10 % à −0,90 | 0,099 | 0,169 | 0,311 | 0,480 | **0,744** | 0,023 |
| S2, « mode écarté » : 80 % à +0,10, 20 % à −0,40 | 0,032 | 0,037 | 0,058 | 0,088 | 0,121 | 0,025 |
| « rappel ≥ 0,6 », rappel moyen vrai 0,6 (0,7 sur 80 % des tâches, 0,2 sur 20 %) | 0,082 | 0,162 | 0,289 | 0,475 | — | 0,012 |

- **Banque figée de moyenne exactement nulle** (90 tâches à +0,1, 10 à −0,9), en ordre secret uniforme : le mélange est promu dans **100 %** des ordres. La forme parts l'est dans 0,1 % des cas, la variante sans remise dans 0,2 %. Sur la même mécanique, le contrôle 3 de la pièce (±0,6) passe à 0,0105.
- **Le cas S2 est exactement celui de la fiche « tous modes » de G1** quand le blanc gagne un peu sur les modes fréquents et perd beaucoup sur un mode rare, par exemple le mode tenu à l'écart de N-054.
- **D'où vient la « puissance » du signe.** Sous l'alternative de 20 points (0,6 contre 0,4), aucune mise valide pour le nul de la pièce ne croît de plus de 0,163 nat par tâche (λ = 0,99). La composante signe, elle, croît de 0,238 nat par tâche à λ = 0,6. À 20 tâches :
  - la meilleure mise fixe valide promeut dans 0,65 des cas (section A) ;
  - le signe promeut dans 0,76 des cas.

  L'avantage de 0,77 contre 0,10 cité en 2.1 est donc le prix d'un autre nul.

**Gravité** : garantie touchée.

**Correction.**
- Pour toute affirmation d'espérance (G1, H1, H2, H3, « rappel ≥ x ») : forme **parts seule**, mélangée sur Λ (prix log 4).
- Si l'on veut aussi l'affirmation « A fait mieux sur la majorité des tâches » : une fiche séparée, avec le nul « P(v > 0) ≤ P(v < 0) » déclaré. Jamais un mélange des deux formes.
- Ajouter un contrôle fatal : nul asymétrique de moyenne nulle (S1, S2, la banque figée 90/10, « rappel ≥ x » à rappels asymétriques), avec promotion ≤ α exigée.
- **Coût de la correction.**
  - Faible pour les petits effets, où la forme parts fait même mieux que le mélange : 0,955 contre 0,940 à 100 tâches pour 10 points ; 0,878 contre 0,832 à 250 tâches pour 5 points.
  - Réel pour les grands effets sur peu de tâches : 20 points à 30 tâches passent de 0,90 à 0,69 ; à 40 tâches, de 0,98 à 0,97.

### C2 — Le bruit des seuils de calibrage fait promouvoir « A meilleur que B » entre deux moniteurs de même loi ; la garde ne peut pas le voir

**Où dans la pièce.**
- Verdict, point 3 : « le taux de faux positifs apparié par construction ».
- Sections 2.4 et 3.5 ; contrôle 6 ; section 6 ; décision D-S4.

**Ce qui manque.**
- Les seuils de A et de B sont deux quantiles à 99 %, estimés **séparément** sur un nombre fini d'épisodes honnêtes. Leurs taux de faux positifs réels diffèrent donc par le seul hasard du calibrage.
- Au point 1 %, la courbe de détection (le rappel en fonction du taux de faux positifs) est raide. En modèle binormal, sa pente vaut 14,5 pour un rappel de 0,40 à 1 %, et 10,5 pour un rappel de 0,80. **Un demi-point de faux positifs achète de 5 à 7 points de rappel.**
- Le pari est valide **conditionnellement aux seuils** : il établit correctement qu'aux seuils scellés, A rappelle plus que B.
- Mais l'affirmation scientifique « A détecte plus que B à taux de faux positifs égal » n'est pas protégée. La garde n'est dimensionnée que pour voir des asymétries de 5 à 10 points, alors que celles qui comptent sont de l'ordre de 0,5 point.

**Reproduit.** Section D (500 répétitions) et compléments.
- **Montage.** A et B sont des jumeaux en loi : même loi, bruits indépendants. Le rappel vrai est 0,40 à 1 % exact. Les seuils sont calibrés séparément selon la règle 2.4.
- **Lecture du tableau.** La première colonne est l'écart-type de l'écart vrai de rappel créé par le seul calibrage. La dernière donne la promotion de « A > B », garde comprise, avec le mélange ; la forme parts seule est entre parenthèses.

| calibrage honnête (tâches de 10 épisodes) | écart vrai de rappel induit (écart-type) | asymétrie vraie de faux positifs (écart-type) | 40 sabotées, 70 honnêtes, δ = 0,10 | 100 sabotées, 150 honnêtes, δ = 0,05 |
|---|---|---|---|---|
| 45 tâches | 9,1 points | 0,71 point | 0,128 (0,082) | **0,186 (0,202)** |
| 45 tâches, corrélation intra-tâche 0,3 | 10,9 points | 0,92 point | 0,076 (0,080) | 0,150 (0,158) |
| 200 tâches | 4,4 points | 0,31 point | 0,018 (0,002) | 0,078 (0,098) |
| 500 tâches | 2,8 points | 0,20 point | — | 0,036 (0,036) |
| 1 000 tâches | 2,1 points | 0,15 point | 0,010 (0,000) | 0,016 (0,026) |

- La garde ne retire presque rien : 0,216 sans garde, 0,186 avec.
- Ces chiffres valent pour un seul sens (« A > B ») ; dans les deux sens, c'est environ le double.
- **Plus l'épreuve est grande, plus la fausse promotion est probable.** La différence conditionnelle est réelle, et le pari finit par la voir.

**Gravité.**
- Garantie touchée pour l'affirmation scientifique : G1, et H1 « à taux de faux positifs égal ».
- La garantie formelle, conditionnelle aux seuils, tient.

**Correction.**
1. Ajouter un contrôle fatal « jumeaux en loi calibrés séparément », à la taille réelle du calibrage et de l'épreuve, avec ≤ α exigé.
2. Dimensionner le calibrage honnête par ce contrôle : de l'ordre de 500 à 1 000 tâches honnêtes de dix épisodes pour 100 tâches sabotées. C'est ce poste, et non la garde, qui domine le besoin en épisodes honnêtes ; il va au devis de la couche 2.
3. Écrire « aux seuils scellés sur un calibrage de taille C » au lieu de « au même taux », et retirer « apparié par construction ».
4. Option à évaluer : verser les tâches honnêtes de l'épreuve dans le calibrage, commun aux deux cellules. Le bruit de seuil baisse ; en échange, la garde perd ses données, mais elle ne voyait de toute façon que des asymétries de 5 à 10 points.

### C3 — Dépendance entre tâches par organisme : le niveau tombe dès que l'affirmation dépasse les organismes du banc

**Où dans la pièce** : section 3.2, décision D-S1, section 2.1 (l'unité).

**Ce qui manque.**
- Le pari suppose les tâches indépendantes. Or l'écart blanc-noir varie d'un organisme à l'autre, et plusieurs tâches partagent un organisme.
- Avec peu d'organismes, la moyenne de la banque s'écarte de zéro même quand la moyenne sur la population des organismes est nulle. Le pari lit alors 100 tâches comme 100 tirages indépendants, et il « découvre » cet écart.
- Une consigne jouée par plusieurs organismes crée en outre une dépendance croisée, consigne × organisme.

**Reproduit.** Section C5, 2 000 répétitions.
- **Montage.** 100 tâches. L'effet d'organisme sur l'écart est de moyenne nulle. Un écart-type de 0,5 en logit correspond à environ ±10 points de rappel ; 1,0 à environ ±20 points.
- **Lecture du tableau.** Chaque case donne la promotion pour un écart-type de 0,5 / pour un écart-type de 1,0 ; les formes parts et mélange donnent des valeurs voisines.

| nombre d'organismes | 2 | 4 | 5 | 10 | 25 | 100 (indépendance) |
|---|---|---|---|---|---|---|
| promotion | 0,25 / 0,34 | 0,16 / 0,25 | 0,14 / 0,24 | 0,08 / 0,17 | 0,03 / 0,07 | 0,02 / 0,02 |

**Ce que coûte la recommandation de D-S1.** D-S1 recommande « l'organisme comme unité quand plusieurs tâches le partagent ». C'est valide, mais il faut alors **au moins 7 (forme parts) ou 8 (mélange) organismes** pour qu'une promotion soit seulement possible, même si chacun donne v = +1 :
- calcul : ⌈log 80 / log 1,9⌉ = 7 et ⌈log 160 / log 1,9⌉ = 8 (section M) ;
- au seuil e-BH m/α = 240, il en faut 11 ou 12.

Avec les quelques organismes du programme, rien n'est promouvable.

**Gravité.**
- Garantie touchée si la fiche se lit comme une affirmation sur les organismes en général.
- Lecture trompeuse si elle reste conditionnelle aux organismes du banc.

**Correction.** Décider la portée ; c'est une décision manquante, voir plus bas. Deux options :
- **(a) Affirmation conditionnelle aux organismes du banc, dite telle.** La section 3.2 l'esquisse (« sur les tâches du banc T0.6 »). L'unité devient la **consigne**, avec toutes ses exécutions, pour couvrir la dépendance croisée.
- **(b) Affirmation sur les organismes en général.** L'unité est l'organisme, et il en faut une vingtaine ou plus.

Dans les deux cas, ajouter le contrôle fatal « grappes ».

### C4 — H2a choisit sa sous-population sur les scores du comparateur ; le contraste est dégénéré

**Où dans la pièce** : section 4, ligne H2 et précision (i).

**Ce qui est faux.**
- La pièce dit former la sous-population (« chaque action sabotée reste sous le seuil par action ») « sans fuite », parce qu'elle ne lit pas l'issue du séquentiel. Mais elle lit l'issue du **comparateur** : sur cette sous-population, le moniteur par action est aveugle aux actions sabotées, par construction.
- **Cas (a).** Le bras séquentiel ne partage pas les scores qui définissent la sélection : autre sonde, autre couche, contexte privé (que N-007 inclut dans la lecture), ou comparateur par action en boîte noire. Alors **tout** bras A gagne mécaniquement.
- **Cas (b).** Il les partage. Alors r_seq − r_action compare le taux d'alerte du séquentiel au **bruit** du moniteur par action : ses seules alertes possibles viennent des actions honnêtes des épisodes sabotés. Cela ne montre pas que l'accumulation « détecte » au-dessus de son propre hasard.
- Les points de fonctionnement mélangent deux niveaux. Le seuil « par action calibré à 1 % » de N-007 est fixé par action ; le seuil de 2.4 est fixé par épisode. Or un moniteur à 1 % par action, sur T actions, a un taux par épisode de l'ordre de 1 − 0,99^T.

**Reproduit pour le mécanisme** (section L et compléments, 1 000 répétitions).
- Montage : deux moniteurs par action jumeaux en loi, et une sélection faite sur les scores de B.
- Écart moyen sur la sous-population : **+0,088**, contre environ 0 sans sélection.
- Promotion de « A > B » : 0,98 avec le mélange à 40 tâches ; 0,999 avec la forme parts à 100 tâches ; 1,00 à 150.
- Le témoin faux de la pièce pour H2 (échange par tâche) ne teste pas ce mécanisme.

**Gravité** : garantie touchée dans le cas (a) ; lecture trompeuse dans le cas (b).

**Correction.**
- Écrire H2a comme une **détection au-dessus du hasard** : le rappel du séquentiel sur la sous-population, comparé à son propre taux de faux positifs. Deux formes possibles :
  - « rappel ≥ x », avec x = la borne haute certifiée de f_seq (8 à 15 % sur nos banques, d'après 2.4) ;
  - un contraste apparié entre épisodes sabotés et honnêtes d'une même consigne.
- Réserver le seuil par action à 1 % à la seule définition de la sous-population, et définir par épisode tous les points de fonctionnement des cellules.
- Ajouter un contrôle fatal : jumeau en loi soumis à la même règle de sélection.
- Ajouter un témoin faux propre à H2 : l'agrégateur séquentiel appliqué à des scores permutés entre épisodes.

### C5 — Héritage de preuve sur une banque relue

**Où dans la pièce** : section 2.2 (« même héritage de preuve dans la mémoire »), section 2.5 (redite = même signature), section 7.

**Ce qui manque.**
- Dans le juge v7, l'héritage multiplie des e-valeurs calculées sur des **tirages frais**, dont les graines dérivent de l'empreinte de l'engagement.
- Ici, les données forment une banque de scores **figée**. Une redite relit les mêmes tâches, seulement dans un autre ordre secret.
- Les deux e-valeurs sont alors presque identiques : corrélation 0,99 pour la forme parts, dont la richesse finale ne dépend pas de l'ordre. Leur produit n'est pas une e-valeur.

**Reproduit.** Compléments, 4 000 répétitions ; nul 0,5 contre 0,5, 100 tâches. Le tableau donne P(produit des e-valeurs ≥ 20).

| nombre de lectures k | 1 | 2 | 3 | 5 | 10 |
|---|---|---|---|---|---|
| forme parts, même banque | 0,004 | 0,022 | **0,053** | **0,106** | **0,159** |
| forme parts, banques disjointes | 0,004 | 0,004 | 0,004 | 0,005 | 0,003 |
| mélange, même banque | 0,015 | 0,029 | 0,043 | 0,068 | 0,104 |

**Gravité** : garantie touchée dès la troisième relecture.

**Correction.**
- N'accepter l'héritage qu'entre des parties d'épreuve **disjointes**.
- Une seule lecture par signature et par partie d'épreuve, dans l'esprit de N-050. La mémoire refuse tout héritage dont les tâches recouvrent une lecture précédente.
- Déclarer comment des générations successives se partagent une même banque. La règle e-BH contrôle chaque génération, pas la suite des générations sur la même épreuve.

### C6 — La traduction du critère de G1 perd l'essentiel de « à 1 % de faux positifs » et de « meilleure base noire »

**Où dans la pièce.**
- Section 2.4 (dernier tiret) et section 3.2 (le comparateur).
- Section 4, ligne G1 ; section 1, tableau ; section 9.

**(a) Le point de fonctionnement disparaît.**
- La formule « Au même taux nominal, sans asymétrie de faux positifs supérieure à δ », avec δ = 0,05 à 0,10, laisse A tourner à 6 à 11 % de faux positifs contre 1 % pour B.
- La pièce le reconnaît pour le contrôle 6 (« non bloqué » à δ = 0,10), mais le point 3 du Verdict le présente comme une garantie.
- Joint à C2, il ne reste de « à 1 % » que le seuil **nominal** du calibrage.

**(b) Le comparateur est plus faible que celui de N-008.** *Soupçonné : raisonnement, non simulé.*
- Fixer la « meilleure base noire » par une règle sur le développement est valide, puisque le choix ne dépend pas de l'épreuve.
- Mais l'affirmation devient « bat la base **choisie sur le développement** ». N-008 dit autre chose : « la meilleure base boîte noire, toutes variantes confondues ».
- Si plusieurs variantes se valent, le choix sur le développement en retient souvent une qui n'est pas la meilleure sur l'épreuve.
- La forme fidèle est l'**intersection-union** : un contraste par variante, et la promotion seulement si **tous** atteignent 1/α. C'est valide au niveau α sans correction de multiplicité ; la puissance est celle du contraste contre la variante la plus forte.

**(c) G1 ne doit pas dépendre des autres fiches de la génération.**
- Dans la règle e-BH « sur l'ensemble », le seuil dépend de m, donc du nombre d'autres fiches et de témoins jugés dans la génération ; les témoins comptent dans m (`appliquer_multiplicite`).
- Une porte doit avoir sa propre famille, fixée au préenregistrement, et une règle de décision entre modes : la fiche « tous modes » décide-t-elle ? chaque mode ? une intersection-union sur les modes mesurés ?
- N-054, point 2, restreint H1 aux modes mesurés et refuse que le seul mode « coût » la porte. La règle doit le dire.

**(d) La validité à tout instant a un prix.** *Reproduit* (`contre-simulation-lecture-unique-v1-sortie.json`, 2 000 répétitions).
- G1 se lit une seule fois (N-050). Comparons un test de Student apparié au niveau des tâches, lu une fois, au pari en forme parts.
- **Puissance.**
  - 20 points d'écart, 15 tâches : 0,95 pour Student, contre 0,003 pour le pari.
  - 10 points, 30 tâches : 0,79 contre 0,03.
  - 10 points, 100 tâches : 0,997 contre 0,955.
- **Niveau.** Student n'est **pas tenu** sous le nul asymétrique S1 avec peu de tâches : 0,12 à 15 tâches, 0,10 à 20, 0,07 à 30 et à 60, 0,06 à 100. Le pari reste à 0,017 au plus.
- Le choix est donc réel, et il appartient au préenregistrement de G1 : garantie non asymptotique du pari, contre un facteur 2 à 3 sur le nombre de tâches sabotées. N-054, point 4, fixe déjà des « intervalles par rééchantillonnage des tâches » pour l'expérience de lecture.

**(e) La pondération change l'objet mesuré.** Le rappel de N-054 est « par épisode », alors que le contraste de la pièce est une moyenne, par tâche, des parts. Les deux coïncident si le nombre d'épisodes par tâche est constant ; sinon la pondération est à déclarer.

**(f) Deux omissions.**
- Les planchers rapportés de N-008 (« tout signaler » ; « juge en une passe avec le même modèle ») n'apparaissent pas.
- Dans la section 1, « G1 : la même comparaison que H1 » est inexact : G1 compare des agrégations différentes, alors que H1 se lit à agrégation égale.

**Gravité** : lecture trompeuse.

**Correction.**
- Formuler le critère ainsi : « rappel supérieur aux seuils scellés sur un calibrage de taille C ; asymétrie de faux positifs certifiée inférieure à δ ; bruit de calibrage borné par le contrôle des jumeaux (C2) ».
- Comparateur par intersection-union ; famille propre à G1 ; méthode d'intervalle laissée en décision.

### C7 — Tableau hypothèse → forme : écarts aux énoncés de H1, H2, H3 et de N-054

**H1.**
- **« H1b promue = mieux parce que flou (la part revendicable, § 5 du programme) » réinterprète le programme.** Le § 5 dit : « Revendicable : la mesure spécifique diffus/flou », c'est-à-dire la mesure du gain dans ce régime. Il ne dit ni « interaction flou contre net », ni une cause (« parce que »). Faire porter la revendication par l'interaction est une **modification de revendication** : c'est un nœud de décision pour Lazar, pas une ligne de tableau.
- « Diffus » (sabotage étalé contre sabotage concentré) n'est codé nulle part ; la strate floue/nette ne le couvre pas.
- Les paires « voisines » sont à préciser :
  - chaque tâche appartient à une paire au plus ;
  - le départage est déclaré et aveugle aux scores ;
  - les tâches sans paire sont écartées par une règle aveugle aux scores.

**H2.**
- Les bases (ii), cascade de portes, et (iii), sonde sur le dernier état, que N-007 ajoute « pour H2 », manquent.
- Après N-007, la part revendicable est l'accumulation **additive** ; c'est donc le contraste r_additif − r_cascade qui la porte.
- Pour H2a, voir C4.

**H3.**
- « Domine » veut dire : à **chaque** N. C'est une intersection-union sur les N, pas une règle e-BH, qui ne livre que « certains N ».
- La sécurité du § 4 est un **infimum** sur les politiques rouges de P(alerte avant que le dommage atteigne θ). Le rappel n'en donne ni l'infimum ni l'échéance.
- La dominance de l'infimum se lit par intersection-union sur les modes : si le blanc bat le noir pour chaque mode, l'infimum blanc dépasse l'infimum noir.
- La part de chaque cellule doit compter les épisodes « alertés avant le dommage θ ». N-007 rappelle d'ailleurs qu'il faut alors un détecteur de rupture.

**G1 et N-054.**
- Les deux familles de bras du point 3 (génériques, spécialisés) n'apparaissent pas.
- L'expérience de lecture du point 4 (fraction de rappel gardée d'un mode à l'autre) non plus. Le rapport des rappels de deux modes compare des tâches **différentes** : sans paires construites, ce n'est pas un contraste apparié par tâche.
- Le mode tenu à l'écart est rangé parmi les « témoins », alors que c'est une strate d'évaluation.

**H8.** La ligne tient.

**Gravité** : lecture trompeuse ; pour H1b, nœud de décision.

### C8 — Dimensionnement optimiste sur sept points

**Où dans la pièce** : Verdict, point 4 ; sections 6 et 2.4.

Les chiffres cités ne sont pas faux : ce sont bien ceux de la sortie. Mais la table repose sur des hypothèses favorables. *Reproduit* (sections A, B, G, H et M).

**(a) Le tableau inclut la composante signe (C1).** En forme parts seule, la seule valide :

| écart de rappel | puissance (forme parts seule) |
|---|---|
| 30 points | 0,79 à 20 tâches |
| 20 points | 0,69 à 30 tâches ; 0,97 à 40 |
| 10 points | 0,58 à 60 tâches ; 0,955 à 100 |
| 5 points | 0,53 à 150 tâches ; 0,88 à 250 |

« Environ 40 tâches pour 20 points » tient ; « 0,92 à 30 » ne tient pas.

**(b) L'écart est supposé identique d'une tâche à l'autre.** Avec 20 points d'écart **moyen** mais hétérogène, en forme parts :
- moitié des tâches à +50 points, moitié à −10 : 0,75 à 40 tâches, 0,95 à 60 ;
- 70 % à +30 points, 30 % à −3 : 0,90 à 40 tâches.

**(c) Les contrastes d'interaction ne sont pas dimensionnés.** Ce sont pourtant eux qui portent H1b, H2b et H3b. En forme parts :
- 10 points d'interaction : 0,40 à 100 paires, 0,95 à 200 paires (soit 400 tâches par mode) ;
- 20 points : 0,46 à 50 paires, 0,998 à 100.

**(d) Le seuil réel est m/α, pas 1/α.** La table est calculée à 1/α, alors que la règle e-BH impose m/α et que les témoins comptent dans m.

**(e) Le besoin en tâches honnêtes est sous-estimé d'un ordre de grandeur.** Il faut 70 à 150 tâches honnêtes pour la garde, **plus** le calibrage, qui en demande 500 à 1 000 (C2). « Autant d'honnêtes » (Verdict, point 4) est donc trop bas.

**(f) La garde à δ = 0,02 sur 300 tâches est fragile.** Elle n'est plus certifiable quand les faux positifs se groupent par tâche (propension tirée d'une loi Bêta de somme 10) : 0,84 au lieu de 0,96. Les lignes δ = 0,10 à 70 tâches et δ = 0,05 à 150 tiennent (0,999 et 1,00).

**(g) Avec l'organisme comme unité, il faut 7 à 8 organismes au minimum** (C3).

**Gravité** : chiffres optimistes.

**Correction.**
- Refaire la table de la section 6 : forme parts seule, écart hétérogène, contrastes d'interaction, seuil e-BH réel, calibrage dimensionné par les jumeaux.
- Inscrire le poste honnête au devis de la couche 2 et au dossier du fonds.

### C9 — La règle e-BH est appliquée à la seule richesse du contraste, et la garde après coup

**Où** : sections 2.2, 3.5 et 7.1 de la pièce ; `cycle.appliquer_multiplicite`.

**Ce qui manque.**
- La pièce garde `trajectoire_log_w` égale à la richesse du contraste, « pour que e-BH ne change pas » ; la garde n'entre que dans `promue`.
- La règle e-BH retient donc les k* premières fiches selon la richesse du contraste, puis ne garde, parmi elles, que celles qui ont survécu.
- Une fiche qui « tire plus » (garde en échec) fait monter k*, puis disparaît. Le dénominateur rétrécit après coup, et la preuve de la règle e-BH ne couvre plus l'affirmation conjointe « mieux, sans asymétrie de plus de δ ».

**Mesuré, sans dépassement de α.** Section E : 2 000 générations de 20 à 40 fiches.
- Taux de fausses découvertes : 0,0007 à 0,011 selon la configuration avec la règle de la pièce (0,008 avec 10 fiches qui échouent à la garde pour 10 nulles ; 0,011 avec 30 pour 10), contre 0 à 0,0006 avec la correction.
- Le taux reste sous α dans toutes mes configurations. La garantie n'est donc **pas démontrée**, et l'inflation mesurée est faible : dépassement de α **soupçonné, non reproduit**.

**Correction.**
- E-valeur de la fiche = richesse du **minimum** des deux processus (contraste et garde), arrêtée au seuil m/α. Elle est valide sous l'union des nuls, et la règle e-BH s'applique alors telle quelle.
- Coût mesuré : 4,80 vraies fiches retenues sur 5, au lieu de 5,00.
- Le même motif existe dans v7 : le filtre `delta0` des filles s'applique après la règle e-BH. C'est hors de la pièce : soupçonné, à voir par son auteur.

**Gravité** : garantie touchée, mais faiblement (la preuve manque ; l'effet mesuré est petit).

### C10 — Le prix du mélange est donné avec trois valeurs incompatibles

- Section 2.2 : « au plus log 8 ≈ 2,1 nat contre la meilleure mise de la meilleure forme ». C'est juste.
- D-S2 : « prix log 2 ». Ce n'est vrai que contre le mélange en λ de la meilleure forme.
- Contrôle 9 : « perte ≤ log 4 nat » contre « la meilleure mise connue ». C'est faux pour un mélange à deux formes : la borne est log 8, atteinte quand une composante domine.

Avec la correction C1 (forme parts seule), le prix vaut log 4, et le contrôle 9 devient juste.

**Gravité** : chiffre faux (mineur).

### C11 — La règle des coefficients contredit les contrastes d'interaction de la pièce

- La section 2.1 impose « Σ|a_c| ≤ 1 pour que v ∈ [−1 ; 1] ».
- Or les contrastes d'interaction de la pièce ont pour coefficients (½, −½, −½, ½), soit Σ|a_c| = 2. Ils restent pourtant dans [−1 ; 1], parce que les parts sont dans [0 ; 1].
- La bonne condition est double :
  - somme des coefficients positifs, plus la constante, ≤ 1 ;
  - somme des valeurs absolues des coefficients négatifs, moins la constante, ≤ 1.
- Le gabarit du proposeur (section 7.3, « somme absolue ≤ 1 ») interdirait H1b, H2b et H3b, ou les forcerait à des coefficients de ¼, c'est-à-dire deux fois moins de signal.

**Gravité** : clarté, avec une conséquence sur le gabarit.

### C12 — Petits points

- **Section 3.4 et Verdict, point 2.** Le chiffre de N-007 (0,21 à 0,35 au lieu de 0,05) porte sur l'agrégateur **à l'intérieur d'un épisode**, sous effet d'épisode. C'est une analogie, pas une preuve pour les épisodes d'une même tâche. La démonstration de 3.4 se suffit d'ailleurs à elle-même (reproduite, voir plus bas).
- **« Organisme » a deux sens** : l'organisme modèle (section 3.2, D-S1) et l'organisme du pôle (D-S5).
- **Tâches à égalité.** Elles ne touchent pas la validité. Sous la forme signe, elles changent ce qui est mesuré : le signe devient conditionnel aux tâches non égales.
- **Contrôle 8.** Sa grille (20, 50, 100, 200 tâches) diffère de celle du tableau de la section 6 (15 à 250).
- **Contrôle 6.** « δ ≤ 0,04 certifiable, donc ≥ 200 tâches honnêtes » : δ = 0,04 ne figure pas dans la sortie. La sortie donne 0,03 : 0,36 à 150 tâches, 1,00 à 300.
- **Section 2.2.** « À moins de 0,15 de la meilleure forme partout » : l'écart vaut exactement 0,15 à 20 tâches (0,62 contre 0,77). Et « partout » ne couvre qu'un effet et quatre effectifs.
- **Arrondis.** La même valeur 0,995 est rendue 0,99 (ligne 20 points, 40 tâches) et 1,00 (effet aléatoire, 60 tâches).
- **Graines du script de l'auteur (R9).** Un seul flux aléatoire sert toutes les cellules : changer une cellule change toutes les suivantes. Il n'y a ni dérivation par cellule ni manifeste. La sortie est néanmoins reproduite à l'octet près.

---

## Ce qui tient (une ligne chacun)

- Forme parts : Π(1 + λ·v), avec λ ∈ [0 ; 1[ et v ≥ −1, est une surmartingale positive sous « tâches indépendantes et de même loi, E[v] ≤ 0 ». Ville s'applique ; le mélange en λ est valide (prix log 4).
- Hétérogénéité des tâches, pour la forme parts : valide. Nul symétrique : 0,027 à 0,030 ; nuls asymétriques S1 et S2 : ≤ 0,025.
- Section 3.4 (pourquoi pas l'épisode) : juste. Reproduit : 0,70 de promotions pour le pari par épisode ; 0,022 pour le pari par tâche.
- Section 3.5 (garde par union des nuls) : juste pour une fiche seule.
- Section 2.3 (sans remise) : μ_t est juste. Le plafond λ·(n − t + 1)/n suffit à garder le facteur positif (facteur minimal 0,19 et 0,46 dans mes banques), et le niveau tient (0,002 et 0,013).
- Calibrage sans aucun épisode saboté ni tâche d'épreuve (N-007) : respecté.
- Niveau absolu « rapporté, pas certifié » : honnête. Son ordre de grandeur est intrinsèque à toute borne valide à tout instant sur une variable bornée, qui demande environ log(1/α)/(θ − taux vrai) unités.
- La tâche comme unité, plutôt que l'épisode : bon principe, sous réserve de C3.
- Ligne H8 : juste (loi par instance, pas un pari de signe).
- Témoins vrais et faux fabriqués depuis les scores, avec le signal « pas de dents » : bon mécanisme, à compléter (voir la liste des contrôles).

## Chiffres de la pièce : vérification et reproduction

Tous les chiffres des sections 6 et 2.4, et du point 4 du Verdict, sont ceux de `simulation-dimensionnement-v1-sortie.json`, et la relance du script (graine 20261027) redonne ce fichier à l'identique. Ma simulation indépendante (autre graine, autre code, 1 000 répétitions ou plus) retrouve les ordres de grandeur.

| ligne de la pièce | cité | sortie de l'auteur | ma reproduction | forme parts seule (ma simulation) |
|---|---|---|---|---|
| 20 points, 30 tâches | 0,92 | 0,9225 | 0,899 | 0,686 |
| 20 points, 40 tâches | 0,99 | 0,995 | 0,984 | 0,967 |
| 10 points, 100 tâches | 0,95 | 0,945 | 0,940 | 0,955 |
| 30 points, 20 tâches | 0,98 | 0,9775 | 0,973 | 0,787 |
| 5 points, 250 tâches | 0,83 | 0,8325 | 0,832 | 0,878 |
| 20 points, 20 tâches : parts / signe / mélange | 0,10 / 0,77 / 0,62 | 0,1025 / 0,77 / 0,62 | 0,102 / 0,762 / 0,673 | — |
| niveau sous le nul 0,5 contre 0,5, 150 tâches | 0,020 | 0,020 | 0,0235 | 0,0115 |
| garde δ = 0,10, 70 tâches honnêtes | 1,00 | 1,0 | 1,000 | — |
| garde δ = 0,05, 150 tâches honnêtes | 1,00 | 1,0 | 1,000 | — |
| garde δ = 0,10, 50 / δ = 0,05, 100 | (non certifiables) | 0,75 / 0,7475 | 0,793 / 0,740 | — |
| garde δ = 0,03, 150 | 0,36 | 0,36 | 0,323 | — |
| garde δ = 0,02, 300 | certifiable | 0,9625 | 0,962 (0,837 si les faux positifs se groupent par tâche) | — |

## Contrôles fatals : ce qui manque

Les dix contrôles de la section 5 n'emploient que des nuls symétriques et des montages sans calibrage réel. À ajouter, chacun avec promotion ≤ α exigée :

| n° | contrôle | ce qu'il fait tomber aujourd'hui |
|---|---|---|
| 11 | nul asymétrique de moyenne nulle (S1, S2, banque figée 90/10, « rappel ≥ x » à rappels asymétriques) | le mélange (C1) |
| 12 | jumeaux en loi calibrés séparément, à la taille réelle du calibrage et de l'épreuve (remplace le contrôle 2, « B = A », trivial) | tout calibrage de moins de 500 tâches environ (C2) |
| 13 | grappes d'organismes et de consignes, selon la portée déclarée | moins de 10 à 25 organismes (C3) |
| 14 | sélection sur les scores d'un bras (H2a), avec des jumeaux en loi | H2a telle qu'écrite (C4) |
| 15 | héritage sur une banque relue k fois | k ≥ 3 (C5) |
| 16 | règle e-BH avec des fiches qui échouent à la garde (taux de fausses découvertes de l'affirmation conjointe) | règle de la pièce, faiblement (C9) |
| 17 | pour G1, si une méthode à n fixé est retenue : niveau sous le nul asymétrique | test de Student avec moins de 30 tâches (C6 d) |

Le contrôle 9 est à réécrire avec la borne log 4, après la correction C1.

## Décisions D-S1 à D-S6, et décisions manquantes

| décision | avis |
|---|---|
| D-S1 unité | **À reformuler.** La vraie question est la portée : les organismes du banc, ou la population des organismes ? Recommandation : affirmation conditionnelle aux organismes du banc, dite telle, avec la consigne (et toutes ses exécutions) comme unité. L'organisme ne devient l'unité que si la banque en compte une vingtaine (C3). La confiance de 0,8 est trop haute. |
| D-S2 forme | **Recommandation fausse** : le mélange n'est pas valide pour un nul d'espérance (C1). Remplacer par : forme parts seule pour toute affirmation d'espérance ; forme signe seulement dans une fiche séparée, avec son nul déclaré. |
| D-S3 nul | **Tient** (population). À compléter : une seule lecture par signature et par partie d'épreuve ; héritage seulement entre parties disjointes (C5). |
| D-S4 garde | **Le principe tient** : garde appariée bloquante, niveau absolu rapporté. Mais la recommandation surestime ce que la garde protège (C2, C6 a). Y ajouter le calibrage dimensionné par les jumeaux et la règle e-BH sur le minimum (C9). La confiance de 0,75 est trop haute. |
| D-S5 point de fonctionnement | **Tient.** À noter : chaque point de fonctionnement double le nombre de fiches (m), et à 5 % la garde δ = 0,05 égale τ. Lever l'ambiguïté du mot « organisme ». |
| D-S6 grille Λ | **Tient** : la grille reste lisible pour une contre-lecture. |

**Décisions manquantes** (proposer avec recommandation) :

| décision | question | recommandation |
|---|---|---|
| D-S7 portée et unité (C3) | Organismes du banc ou population d'organismes ? Consigne, organisme ou tâche comme unité ? | Organismes du banc ; la consigne comme unité. |
| D-S8 comparateur de G1 (C6 b) | Base choisie sur le développement, ou intersection-union sur toutes les variantes ? | Intersection-union. |
| D-S9 taille du calibrage honnête (C2) | Combien de tâches honnêtes pour borner le bruit de seuil ? | C'est une **dépense** : poste de devis de la couche 2, chiffré par le contrôle des jumeaux. |
| D-S10 règle de décision de G1 entre modes (C6 c) | Quelle fiche décide la porte, et dans quelle famille de multiplicité ? | Une famille propre à la porte, fixée au préenregistrement. |
| D-S11 méthode d'intervalle de G1 (C6 d) | Suite de confiance du pari (non asymptotique, 2 à 3 fois plus de tâches) ou intervalle à n fixé par rééchantillonnage des tâches (N-054 point 4 ; plus puissant, à éprouver sous nul asymétrique) ? | À trancher au préenregistrement de G1. |
| D-S12 relecture d'une même banque (C5) | Comment des générations successives se partagent-elles une épreuve ? | Une lecture par signature ; héritage seulement entre parties disjointes. |

**Nœud de décision**, hors de la pièce : faire de H1b la « part revendicable » de H1 est une modification de revendication (C7). Il revient à Lazar d'en décider.

## Pour reproduire

```
cd /tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-pari-signe/
/opt/venv-essaim-sim-v1/bin/python -I -B contre-simulation-pari-signe-v1.py --rep 1000 > contre-simulation-pari-signe-v1-sortie.json   # environ 1 minute
/opt/venv-essaim-sim-v1/bin/python -I -B contre-simulation-complements-v1.py "$PWD/contre-simulation-pari-signe-v1.py"
/opt/venv-essaim-sim-v1/bin/python -I -B contre-simulation-lecture-unique-v1.py "$PWD/contre-simulation-pari-signe-v1.py"
/opt/venv-essaim-sim-v1/bin/python -I -B verification-analytique-signe-v1.py
/opt/venv-essaim-sim-v1/bin/python -I -B copie-script-auteur-v1.py > relance-script-auteur-sortie-v1.json   # environ 45 secondes ; identique à la sortie citée
```

Correspondance entre les sections de `contre-simulation-pari-signe-v1.py` et les constats :

| section | contenu | constat |
|---|---|---|
| A | puissances | C1, C8 |
| B | garde | C8 |
| C | niveaux sous des nuls hétérogènes, asymétriques, en grappes | C1, C3 |
| D | jumeaux en loi | C2 |
| E | règle e-BH et garde | C9 |
| F | héritage | C5 |
| G | interaction | C8 |
| H | écart hétérogène | C8 |
| I | sans remise et banque figée | C1, « ce qui tient » |
| K | démonstration 3.4 | « ce qui tient » |
| L | sélection sur le comparateur | C4 |
| M | nombre minimal d'unités | C3, C8 |
