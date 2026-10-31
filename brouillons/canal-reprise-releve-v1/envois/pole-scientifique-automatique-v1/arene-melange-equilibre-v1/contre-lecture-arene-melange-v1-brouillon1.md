# Contre-lecture (R2) — préenregistrement « arène : mélange d'équilibre contre défense unique réentraînée » v1, brouillon 1 — brouillon 1 de la contre-lecture

- Auteur : sous-agent Sonnet 5.5 neuf. Il n'a écrit ni le préenregistrement, ni le code, ni les essais, ni le calcul de puissance (auteur relu : sous-agent Opus 5.5, lignée conv-audit).
- Date (UTC) : 2026-10-31, 08:45 (relevé `date -u`).
- Branche `canal/conv-audit-n04`, HEAD `89462343` ; aucun fichier existant du dossier modifié par moi (seul ce rapport est nouveau).
- Texte relu : `preenregistrement-arene-melange-equilibre-v1-brouillon1.md`, empreinte `5129b8c26d384e92015142e6d80c1d29f922210975fc297ec487efab070284ce`.
- Empreinte de ce rapport : à calculer par l'agent parent après écriture (aucun compagnon écrit par moi, consigne).
- Fichiers lus, empreintes vérifiées par `sha256sum` (toutes conformes à leur compagnon et à ce que le préenregistrement annonce) :

| Fichier | Empreinte |
|---|---|
| `arene_melange_v1.py` | `6402dc6b2998d2f48262ddfe1d4d0d13b6a6115fcc8d01852c3b7c8182fd0d3b` |
| `essais/test_arene_melange_v1.py` | `52168b51dd2eff313af8dfcf4b7fbcd9c410f9111553240ba0687f0fa9a8d085` |
| `calcul-puissance-arene-melange-v1.py` | `65df7c5228b31ffb23a320009af278909e012973b1e76d42a05c7e1b215c1f5b` |
| `calcul-puissance-arene-melange-v1-sortie.txt` (désignée (M)) | `17863f83097d8380fae23dfbfdf00fc5e2ce3d7349ade194c2be020dbca63fda` |
| `essai-pilote-racine-essai-v2.json` | `f094b495381db7e342e73432ccb16abfe1bdc06498c4f77928cd7e2d7aff78c5` |
| `LISEZMOI-arene-melange-v1.md` | `955bb0ca7711c04fac3c493a8a6fbaf6f4c5208df7ee990e84a52d45759f43e2` |
| `brainstorm-malleabilite-et-arene-v1.md` (piste 3) | `08360a9402ff81d7d9146ed833d60e687f1be4d9acd0be3ab2867403dda8eb10` |
| `prereg/gabarit-preregistrement-v1.md` ; `src/controle_ia/prereg.py` ; `manifeste.py` ; `scellement.py` | `8cad4371…` ; `3b2e3ee5…` ; `1a5c7464…` ; `93beeb1c…` (ce dernier non listé dans le préenregistrement) |

## 0. Verdict

**Présentable après corrections.** Aucun constat bloquant. Huit constats majeurs (CM-01 à CM-08), neuf moyens ou mineurs (CM-09 à CM-17), un constat positif (CM-18).

Le code est sain : 25 essais réussis, rejeu bit à bit, programme linéaire correct, optimiseurs convergés, attaquant confirmé par un contrôle indépendant, aucune fuite de la racine de décision. Ce qui doit changer touche la **structure de la décision** (la comparaison principale est la moins informative), le **second budget δ et les marges d'équivalence**, la **couverture des gardes**, et la manière dont le texte présente le changement d'oracle, l'erreur de première espèce et le seuil S5. Aucune correction ne demande de toucher à la racine de décision ; la plupart demandent un nouveau pilote sur une racine d'essai fraîche (environ 20 minutes de mur sur 2 cœurs).

Fait nouveau, mesuré par moi sur la racine d'essai (5 tâches, non opposable, § B) : le **« ou » déterministe des neuf moniteurs mêmes de B** atteint (iii) ≈ 0,31 à δ1 contre 0,18 pour B, et (ii) ≈ 0,82 contre 0,40 : presque tout l'avantage de D vient de l'agrégation déterministe, pas du nombre de paramètres. À δ2, au contraire, ce « ou » est au-dessous de B (0,025 contre 0,037). Le pilote ne dit donc pas seulement « D ≥ B » ; il dit que le sens de la comparaison change avec δ.

## 1. Ce que j'ai fait (traçabilité)

- `sha256sum -c` sur tous les compagnons du dossier : conformes. Les empreintes des documents de contexte cités par le préenregistrement (brainstorm, réponse pont, comparaison, fusion v3 sur `origin/main`) : conformes.
- `python3 -m pytest -q` sur `essais/` : **25 réussis en 6,4 s** (avec `PYTHONDONTWRITEBYTECODE=1 -p no:cacheprovider` : aucun `__pycache__` créé).
- Script de puissance rejoué sur `essai-pilote-racine-essai-v2.json` : sortie **identique** à (M), hors lignes `time`.
- Deux tâches du pilote rejouées en configuration complète, dans un processus séparé du pilote (instance 7, δ1 et δ2) : dictionnaire de résultat **identique bit à bit** au fichier du pilote, hors temps mesurés. Cinq autres tâches rejouées dans mon diagnostic : 20 valeurs de (iii) sur 20 identiques à quatre décimales.
- Comparaison du code du pilote v2 (commit `5919719a`, empreinte `9ed8c8b5…`, retrouvée dans git) au code remis : **trois lignes de différence**, la vérification de l'empreinte du code dans `exiger_identite_prereg` (l. 150-152). L'affirmation « aucun changement de calcul » est vraie.
- Programme linéaire sur jeux de valeur connue (§ D).
- Diagnostics hors dépôt, **racine d'essai 20261291 / 20261292 seulement**, scripts dans `/tmp/cm_diag/` (non conservés dans le dépôt ; `diag.py` `74102e15…`, `temoins.py` `4919a753…`, `lecture.py` `374bc316…`) : statuts des optimiseurs, attaquants alternatifs, ré-optimisation de l'oracle, témoins serrés (§ B), simulation de la lecture des quatre tables à partir du pilote.
- Je n'ai rien lu sous `donnees/`, n'ai utilisé aucun réseau, aucune clé, ni la racine de décision, ni le mode décision ; rien modifié, rien commité, aucun compagnon écrit.

## 2. Réponses aux questions

### A. Changement d'oracle du défenseur (et seuil de contournement) — **tenu sous conditions, à corriger dans le texte**

**Est-ce une lecture au sens de R1 ?** Non, pas au sens strict. R1 vise la lecture d'un résultat de l'expérience décisive ; la racine d'essai est déclarée plomberie et puissance, et les racines de décision n'ont servi à aucun tirage : `RACINE` et `RACINE_TENUE` ne sont employées que dans les gardes et dans la branche `decision` de `main` (l. 135, 145-147, 859-866 de `arene_melange_v1.py`). Rien n'est scellé, donc il n'y a pas d'écart à un préenregistrement scellé. Les données de la décision seront fraîches : l'erreur de première espèce du test « B > A sous l'oracle détection » n'est pas touchée.

**Mais c'est une bifurcation de conception (R3).** L'oracle a été choisi parce que le contraste de l'hypothèse (B contre A) était nul sous la variante logistique. Le texte l'admet (l. 192). Le changement agit sur B seul : sur l'instance 0 à δ1, B passe de 0,070 (logistique, texte l. 192) à 0,196 (détection, pilote v2), A de 0,069 à 0,064. Mécanisme : sous la régression logistique chaque nouveau moniteur domine les précédents, l'équilibre est pur et B se réduit à A ; sous « détection » les moniteurs deviennent des spécialistes (support moyen 3,75 sur 9 [M § 6]). Le changement **fait exister le mélange**. Le pilote ne vaut donc rien comme preuve des signes P1 à P7 sur l'instance 0, et la portée de H1 est conditionnelle à ce choix.

**Il existe un argument de principe indépendant de l'observation, et c'est le bon** : le double oracle suppose une meilleure réponse pour le gain du jeu que l'on résout (détection au seuil α, matrice des gains) ; la régression logistique n'optimise pas ce gain ; sous elle le chemin « mélange » n'est pas exercé, ce qui rend le test muet (même logique que R5, « chemin non exercé »). Le texte met l'observation d'abord et le principe ensuite ; il faut inverser.

**Conditions d'acceptabilité** (cumulatives) :
1. Déclaration complète dans le texte scellé, y compris les **trois variantes essayées sur l'instance 0** (LISEZMOI l. 59). Fait en partie. L'observation « 0,070 contre 0,069 » n'est archivée dans aucun fichier : sans chemin ni empreinte (R6), elle ne peut pas fonder un chiffre ; la remplacer par la mesure ci-dessous.
2. Justification de principe en tête ; l'observation en note.
3. **Portée** : H1 et la phrase de synthèse deviennent explicitement « sous l'oracle détection ». Le bras A n'est pas « le protocole de Bailey » : le texte reconnaît (l. 156) que la variante logistique est plus proche de l'entraînement des sondes ; corriger l. 25, 46 et 74.
4. **Pilote logistique complet sur la racine d'essai** (48 tâches, environ 6 minutes de mur comme le pilote v1) pour remplacer l'anecdote d'une instance par un fait : part d'équilibres purs, B − A. Prédiction signée avant : sous « logistique », équilibres purs sur plus de la moitié des tâches, donc « non concluant : mélange dégénéré » (déclencheur déjà prévu, l. 209). Lazar doit savoir, en tranchant S13, que le choix « logistique » mène à un résultat attendu non concluant.
5. **Nouvelle racine d'essai** pour tout chiffre de prédiction ou de puissance, une fois la conception corrigée. Le pilote v2 contient l'instance 0 sur laquelle la conception a été choisie (1 instance sur 24 : contamination faible, puissance bâtie sur des écarts-types, mais l'éviter est gratuit). Les corrections de ce rapport changent de toute façon la conception, donc un nouveau pilote est de toute façon nécessaire.
6. Aucun autre réglage de conception ne change après ce nouveau pilote.

**Seuil de contournement 0,5 → 0,10 (S14).** Même catégorie, moins grave (mesure descriptive, piste 5). La raison de principe existe : un seuil absolu doit rester sous la détection de la cible non modifiée, sinon le coût est nul par définition. Mais 0,10 (« dix fois α ») est arbitraire et fixé en regardant le résultat, et `cout_contournement` (l. 573-598) n'a **aucune garde** « détection à δ' = 0 supérieure au seuil ». Plus grave, la « moitié des tâches censurées » (texte l. 68, 161) cache une réalité tranchée : par δ, dans le pilote v2, **B 96 % / C 100 % / D 100 % censurés à δ1, 0 % pour tous à δ2** (A : 12 % à δ1, 0 % à δ2). À δ1 la mesure est vide pour B, C et D ; à δ2 elle est sans censure. Correction : seuil relatif (fraction de la détection de la cible), garde sur la ligne de base, parts censurées rapportées par δ, ou, mieux, remplacer par la courbe V(δ') sur une grille de budgets (aucune censure).

### B. Les témoins — **à corriger** (CM-02, CM-03)

**D est-il le bon témoin de « capacité » ?** Il est le bon témoin du **nombre de paramètres** (vérifié : 63 paramètres de part et d'autre au tour T, test l. 217-219). Il n'est **pas** un témoin de capacité au sens fonctionnel, parce qu'il change aussi de famille de fonctions :
- D est une log-somme-exp de neuf scores affines : sa région de détection est le complément d'un polyèdre convexe contenant l'essentiel de la loi propre, c'est-à-dire un **détecteur d'anomalies** dans neuf directions. Au pilote, (ii) de D vaut 0,83 contre 0,38 pour B (B − D sur (ii) = −0,44 [M § 2]) : D détecte presque tout ce qui s'éloigne de l'origine, indépendamment de l'attaquant qu'il a vu.
- Son seuil unique à α partage le budget de fausses alertes, alors que chaque moniteur de B a le sien (α). Avec des queues gaussiennes ce partage coûte peu (seuil par moniteur de 2,33 à environ 3,06 écarts-types pour neuf moniteurs) ; c'est une propriété du monde choisi, à déclarer.
- Son oracle (m > 1) utilise le seuil gaussien approché, exact seulement pour un moniteur linéaire (docstring l. 314-315), et deux départs ; il est donc plutôt **défavorisé**, ce qui rend la lecture « D ≥ B » prudente, pas fragile.

**Témoins plus serrés proposés** (« finale seulement » : aucune trajectoire nouvelle, mêmes neuf moniteurs que B, mêmes deux attaquants finaux) :
- `B_unif` : les moniteurs de B avec des poids uniformes (isole le **poids d'équilibre** à moniteurs identiques ; C change aussi les moniteurs, donc B − C mélange deux effets).
- `B_alea` : poids tirés au hasard (loi de Dirichlet uniforme, graine dédiée).
- `B_ou` : « ou » déterministe des moniteurs de B (isole le **tirage au hasard** contre l'agrégation déterministe). Construction sans nouvelle classe : pour chaque moniteur, W' = λ·W/σ et b' = λ·(b − μ)/σ (μ, σ : moyenne et écart-type du score sur l'échantillon propre de calibration), empilés dans un `Moniteur` à neuf unités (la log-somme-exp du code tend vers le maximum quand λ grandit), seuil recalibré à α. J'ai pris λ = 4 et λ = 8 : résultats voisins.

**Mesure (racine d'essai, 5 tâches, non opposable ; B reproduit exactement le pilote à chaque tâche)** :

| Moyenne | B | B_unif | B_alea | B_ou (λ = 4) | D (pilote) |
|---|---|---|---|---|---|
| (iii), δ1 (instances 0-2) | 0,176 | 0,171 | 0,154 | **0,313** | 0,368 |
| (iii), δ2 (instances 0-1) | 0,037 | 0,040 | 0,030 | **0,025** | 0,028 |
| (ii), δ1 | 0,399 | | | **0,817** | |
| (ii), δ2 | 0,369 | | | **0,770** | |

Fausses alertes des variantes : 0,0089 à 0,0111. Lecture prudente (trois et deux tâches) : à δ1, remplacer le tirage au hasard par un « ou » déterministe des mêmes moniteurs multiplie (iii) par 1,8 et (ii) par 2 ; les poids d'équilibre ne se distinguent pas des poids uniformes (+0,005) mais B dépasse les poids aléatoires dans trois tâches sur trois (+0,012, +0,026, +0,030) : un effet des poids de l'ordre de 0,02, que B − C (trajectoire différente) ne peut pas montrer. À δ2, le « ou » est au-dessous de B dans les deux tâches (−0,010 et −0,013) : c'est le seul endroit où le tirage au hasard semble payer, au plancher.

**L'expérience peut-elle encore départager « équilibre » et « capacité » ?** Pour la question grossière, oui : le gain de B sur A n'est pas propre aux poids d'équilibre (B ≈ C), et une agrégation déterministe de même taille fait mieux à δ1. Pour la question fine, non, telle qu'elle est écrite : « D ≥ B » mélange nombre de paramètres, forme de la fonction et agrégation. Et le texte actuel place en position principale (H1, B > A) la comparaison que n'importe quel mélange gagne (le pilote donne des bornes basses de +0,11 et +0,03).

**À changer avant scellement** :
1. Ajouter `B_unif`, `B_alea`, `B_ou` au plan et aux Tables 3 et 4, avec marges propres ; signer d'avance les signes prédits (`B_ou` ≥ B à δ1, `B_unif` ≈ B, `B_alea` ≤ B). Coût : environ 9 s de processeur par tâche (+38 %), soit environ 110 minutes de processeur et 57 minutes de mur pour N = 100 : sous S8.
2. Réécrire la hiérarchie : H1 devient le **contrôle positif** (le mécanisme est exercé) ; la question centrale de la piste 3 devient « les poids d'équilibre et le tirage au hasard apportent-ils quelque chose à moniteurs identiques ? ». La phrase de synthèse ne peut citer « H1 confirmée » sans les lectures de B contre `B_unif`, `B_alea`, `B_ou`, D.
3. Ajouter à « ce que l'expérience n'autorise pas » : le monde est à queues gaussiennes et neuf moniteurs, favorable au « ou » déterministe ; rien sur des moniteurs à queues lourdes ou des dizaines de sondes ; D n'est pas « la capacité » mais une agrégation déterministe.

### C. Prédiction, puissance, seuils S1 à S14 — **à corriger**

**Chiffres.** Tous les nombres du texte que j'ai vérifiés (P1 à P7, résumé, S1, S4 à S9, S12, S14) correspondent à (M) ; (M) est reproduit à l'identique. Aucun écart de transcription trouvé.

**Les quatre tables.** Logique exhaustive et sans chevauchement (énumération des cas). Simulation de ma part, à partir du pilote pris pour vérité (24 instances rééchantillonnées à N = 100, 300 répétitions, intervalles à percentile, marges recommandées) : Table 1 ligne 5 dans 300 cas sur 300 ; Table 3 « D > B à δ1, ≈ à δ2 » (ligne 3) dans 300 sur 300 ; Table 4 « ≈ aux deux δ » (ligne 5) dans 296 sur 300. Défauts de rédaction : CM-13.

**S5 décide la lecture, et la table n'est pas stable autour de lui.** Même simulation, Table 2 : S5 = 0,02 → « régression avérée » 300/300 ; S5 = 0,03 → 298/300 ; **S5 = 0,05 → « régression non exclue » 192 fois, « avérée » 108 fois** : la vraie valeur du pilote (−0,058) est à la frontière de −0,05, la lecture se joue au hasard de l'échantillon. De plus : S5 = 0,03 dépasse S1 = 0,02, donc la table tolère un recul sur (ii) supérieur à l'effet minimal cherché sur (iii) ; le critère de choix du texte (plus petite tolérance dont la puissance sous écart nul dépasse 0,95) est un critère de puissance, pas de signification ; et la ligne « Choix sensible : Lazar fixe S5 en sachant que la valeur pilote est autour de −0,06 » (l. 116) lui laisse choisir la lecture. À faire : S5 fixé par principe (S5 = S1) et lecture **sans seuil** rapportée à côté (signe et intervalle de B − A sur (ii)). Le libellé « arbitrage, pas un gain net » (Table 2 ligne 2) n'est pas dérivé de la table : en poids égaux, gain moins perte vaut +0,069 à δ1 et −0,023 à δ2 au pilote.

**δ2 = 2,4 : quasi dégénéré pour (iii), informatif pour (ii).** Pilote : V(A) < α dans 23 tâches sur 24, moyenne 0,0008 (l'attaquant se cache mieux que la loi propre) ; B, C, D valent 0,037, 0,037, 0,033 avec des minima de 0,018 à 0,025 et des maxima de 0,045 à 0,053. Tout est au plancher : toutes les valeurs de B, C, D tiennent dans [0,018 ; 0,053], et l'écart observé sur une même instance ne dépasse pas 0,018 (B − C) ni 0,013 (B − D). Conséquences :
- S1 = 0,02 vaut 54 % du niveau de B : « confirmé à δ2 » veut dire « A est à zéro, B est à quatre fois α ».
- Les équivalences à δ2 sont **mécaniques** avec la marge 0,02 (tout couple parmi B, C, D est « ≈ »). Si l'on resserre la marge à 0,005, B − D (+0,005, intervalle au-dessus de zéro) devient « B > D » à δ2 pendant que D > B à δ1 : la Table 3 passe de la ligne 3 à la ligne 2 (« dépend de δ ») dans 270 cas sur 300. La lecture dépend d'une marge posée sur un plancher.
- La Table 4 ligne 5 (« ≈ aux deux δ ») n'a en fait qu'un δ informatif.
- Nuance apportée par mes témoins : c'est aussi à δ2 que le tirage au hasard semble payer face au « ou » déterministe. Écarter δ2 sans le mesurer perdrait ce signal ; le garder avec une marge absolue le masque.

À faire : pilote sur racine fraîche à plusieurs valeurs de δ (par exemple 1,2 ; 1,6 ; 2,0 ; 2,4), choix des deux δ de la décision **sur un critère de A seul** (par exemple V(A) ≥ 3α), marges d'équivalence relatives (fraction du niveau d'un bras ou de l'effet B − A), et règle « B > D » avec effet minimal (borne basse supérieure à la marge, non à zéro).

**Censure du coût** : voir A. S'y ajoute : l'écart B − A est une borne basse de l'écart vrai seulement si A n'est pas censuré (il l'est dans 12 % des tâches à δ1 : l'écart vaut alors 0 mais son signe vrai est inconnu) ; la bissection (l. 591-597) suppose une détection monotone en δ', non vérifiée ; la moyenne de fractions mêlant valeurs censurées à 1 et non censurées n'a pas d'interprétation propre.

**Erreur de première espèce (CM-05).** Le résumé (l. 30) annonce « erreur de première espèce ≤ 0,0013 (deux δ exigés) ». C'est la taille sous l'hypothèse nulle **aux deux δ à la fois** (deux tests presque indépendants, donc un produit). Pour une règle « aux deux δ » (intersection-union), la taille est celle du δ le plus défavorable : 0,019 à 0,053 par δ sans S1 [M § 3, erreur de première espèce]. La ligne 101 le dit, le résumé non : c'est ce que Lazar lira. Par ailleurs « estimation ≥ S1 et borne basse > 0 » n'est pas un test de « effet ≥ S1 » : à effet vrai égal à S1, la règle confirme dans 25 % des cas (S1 = 0,02, e = 0,02, N = 100 : 0,251 [M § 3]). C'est une règle « pertinence et significativité » ; la nommer ainsi.

**Autres.** La puissance de S1 est sans enjeu (le pilote est à bornes basses de +0,11 et +0,03) ; l'enjeu est S5, S6, S7. Confiances 0,85 / 0,8 / 0,7 / 0,75 : basses au regard des intervalles du pilote (erreur-type d'environ 0,004 à N = 100) ; si le doute porte sur le passage d'un monde à l'autre, le dire. P2 à δ2 (« ≈ 0 ») n'a pas de critère de réfutation. S10 : la règle « V(B) ≥ 0,99 » ne peut jamais se déclencher (maximum observé de V(B) : 0,26 ; D : 0,39) ; la garder (règle de Lazar), mais ajouter un seuil calibré.

### D. Code — **tenu, avec réserves mineures** (CM-09, CM-11, CM-14 à CM-17)

- **Essais** : 25 sur 25. **Reproductibilité bit à bit** : confirmée (deux tâches en configuration complète, § 1). Réserve : l'essai de reproductibilité (l. 211-219) tourne en petite configuration (d = 3, K = 2, T = 2), sans pool de processus, dans un processus où numpy est déjà chargé (les variables de limitation de fils, posées après l'import par pytest, ne s'appliquent pas) ; en mode ligne de commande elles sont posées avant l'import, et mon rejeu complet confirme.
- **Graines (R9)** : `gen` = `SeedSequence(entropy=racine, spawn_key=(…))` avec garde numpy ≥ 1.25 ; clés distinctes pour chaque rôle (0 à 13, plus 99), chaque tour (0 à 9, 99 pour le coût) ; la clé du rééchantillonnage `(code_delta, code_contraste, 0, 0, 99)` ne peut entrer en collision avec une clé de tâche (aucune tâche n'emploie le rôle 99) ; appariement entre δ par la loi cible (code 0). Réserve (CM-14) : `creer_manifeste` consigne `graines(["arene"], RACINE)`, dérivées du nom de tâche, que le code n'emploie pas ; le schéma réel n'est écrit que dans le mode essai (`schema_graines`), pas dans le manifeste de décision.
- **Meilleure réponse de l'attaquant** : sur 6 930 optimisations SLSQP de mon diagnostic, **statut 0 dans 100 %** (maximum 99 itérations pour une limite de 100, bras B ; aucune limite atteinte) ; sur l'entraînement du défenseur, 1 non-convergence sur 1 209 optimisations (bras D, limite de 300 itérations). Attaquants alternatifs sur 5 tâches : 14 départs structurés (une, deux ou trois composantes vers l'origine, avec ou sans rétrécissement d'écart-type), 150 départs tirés en plus, 1 024 échantillons de Monte-Carlo, 300 itérations. Écart (standard moins lourd, positif = l'alternatif trouve mieux) : A −0,0001, B +0,0002, C −0,0002, D +0,0019 en moyenne ; maximum +0,0054 (D, niveau 0,23). La borne haute (iii) est donc serrée au pilote ; le contrôle « renforcé » du texte (même optimiseur, plus de départs) est de la même famille, mon contrôle indépendant le confirme. Réserve (CM-09) : le code ne consigne ni statut ni nombre d'itérations de SLSQP, et saute **en silence** un départ non fini (l. 464-465) ; seule l'absence totale de départ fini arrête.
- **Oracle du défenseur** : les départs d'entraînement sont ordonnés par poids (l. 539-543) ; pour A, C, D (poids uniformes, tri stable) ce sont les attaques les plus anciennes, pour B les plus pondérées, et `departs_entr` tronque à 7 directions (l. 364). J'ai ré-optimisé 128 entraînements linéaires (A 40, B 40, C 40, D 8) avec toutes les directions de composantes et 20 départs aléatoires : gain d'objectif nul en moyenne, au plus 0,0013. L'asymétrie existe, sans effet mesuré. Non testé : l'oracle à plusieurs unités (D).
- **Programme linéaire** : correct. Jeu [[0,6 ; 0],[0,2 ; 0,4]] : p = (0,25 ; 0,75), q = (0,5 ; 0,5), valeur 0,3, conforme au calcul à la main ; pierre-papier-ciseaux décalé : uniforme, 0,5 ; jeu avec ligne dominée : (0,5 ; 0,5 ; 0), 0,5 ; cinq matrices aléatoires 4×5 : valeur égale à min_j(pG) et à max_i(Gq), et supérieure ou égale à la borne par force brute (200 000 tirages). Orientation (lignes = moniteurs qui maximisent) conforme à `trajectoire`. Réserve (CM-11) : équilibres **non uniques** (jeu constant → p = (1, 0, 0)) : le sommet est choisi par le solveur (version de scipy dans le manifeste) ; aucune règle de choix.
- **Double oracle non convergé** (CM-11) : valeur du jeu restreint moins V(B) = +0,204 − 0,168 = 0,037 à δ1 et +0,078 − 0,037 = 0,041 à δ2 (pilote). À δ2 l'écart dépasse l'effet B − A (0,037). B est un **itéré tronqué à huit tours**, pas un équilibre du jeu complet : le dire, rapporter l'écart par δ.
- **Garde de scellement** : `exiger_prereg_arene` s'exécute avant `creer_manifeste` (l. 859) et avant toute graine (l. 864) : scellé et conforme (`exiger_prereg_scelle`), puis identifiant, deux racines, empreinte de configuration, empreinte du fichier de code. Réserves (CM-14) : seul ce fichier de code est lié (pas `controle_ia/*`, pas les versions de numpy et scipy, que le manifeste consigne) ; les chaînes sont cherchées n'importe où dans le texte, rien ne compare S9, S11, S12, S13, S14 du texte à la configuration (contrôle manuel, l. 293) ; `--instances` n'est pas comparé à S4.
- **Aucune fuite de la racine de décision** : confirmé (recherche exhaustive des usages). Les fichiers d'essai portent 20261291 et 20261292. Réserve (CM-15) : la garde est au niveau de la ligne de commande ; `executer_tache` et `gen` accepteraient `RACINE` si un script les appelait directement.

### E. Règles — **R3 tenu avec réserve ; R4 et R5 à corriger**

- **R3** : tenu pour la décision (le texte signe les deux sens et annonce un résultat probablement défavorable à la piste 3, l. 72-74). Réserve : bifurcation de conception (A), et structure qui place en position principale le contraste le plus sûr (CM-02).
- **R4** : asymétrique (CM-07). (i) « B ≈ C », défavorable à la piste, déclenche l'audit ; « H1 réfutée » (Table 1 lignes 4 et 7) n'en déclenche aucun. (ii) Aucun déclencheur pour une surprise **favorable** sur B − C ou B − D (par exemple B > D à δ1, contraire au signe prédit). (iii) « V(B) ≥ 0,99 » est inatteignable. Correction : tout contraste dont la lecture contredit un signe prédit (P1 à P4) déclenche l'audit, dans les deux sens ; un seuil de « trop beau » calibré sur les maxima du pilote.
- **R5** (CM-08) : le code contient 28 `raise GardeArret` ; **19 ont un essai sain et artefact, 9 n'en ont pas**. Le texte n'en déclare que deux (l. 285-286). Les autres : loi d'attaque non finie (l. 188), scores propres non finis (l. 264), maxout sans graine (l. 350), entraînement non fini (l. 356 et 372), entraînement inconnu (l. 360), programme linéaire non résolu (l. 412), valeurs primale et duale différentes (l. 415). La liste d'arrêt cite `test_jeu_artefact` pour 412 et 415 alors qu'il ne couvre que la matrice (essai l. 111-114), et `test_moniteur_gardes` pour « scores non finis » alors qu'il ne couvre que les paramètres (l. 149-156). « Déclenchement réel observé en essai avec 60 itérations » n'a aucune trace. « Reproductibilité → arrêt » (l. 287) est un essai, non une garde d'exécution. Enfin `test_decision_refusee_sans_prereg_scelle` (l. 64-70) ne teste plus ce que dit son nom : depuis que le brouillon a son compagnon d'empreinte, `exiger_prereg_scelle` passe l'étape du scellé et refuse pour non-conformité (« scellé mais non conforme : Seuil ; Contre-lecture », vérifié) ; le cas « pas de scellé » n'est plus isolé. Aucun repli silencieux hors le `continue` (l. 464-465) ; la renormalisation des poids (1e-9) et les projections au-delà de 1e-6 sont déclarées.
- **« Ce que l'expérience n'autorise pas »** : bonne base. À ajouter : rien sur l'équilibre du jeu complet (itéré tronqué, écart 0,04) ; A n'est pas le protocole de Bailey ; tout est conditionnel à l'oracle détection ; monde à queues gaussiennes favorable au « ou » déterministe ; D n'est pas « la capacité ».

### F. Ce qui empêche de présenter les seuils à Lazar maintenant

À régler **avant présentation** (ils changent les valeurs ou les recommandations) :
1. S11 / S6 / S7 : δ2 au plancher, marges absolues mécaniques (CM-04) → nouveau pilote à plusieurs δ sur racine fraîche, marges relatives.
2. Structure de décision et témoins serrés (CM-02, CM-03) → change le plan, S4 et S8.
3. S13 : justification de principe en tête, portée de H1, pilote logistique sur 48 tâches, issue attendue de chaque option (CM-01).
4. S14 : seuil relatif, garde, parts censurées par δ (CM-10).
5. S5 : par principe, lecture sans seuil (CM-06). Retirer « Choix sensible » comme invitation à choisir en connaissant la réponse.
6. S2 et résumé l. 30 : taille de l'intersection-union, nature de la règle (CM-05).
7. S10 et déclencheurs d'audit symétriques (CM-07).

À régler **avant scellement** (code et essais, donc nouvelles empreintes) : CM-08, CM-09, CM-12, CM-14, CM-15 ; mettre à jour la ligne 7 (HEAD) et toutes les empreintes ; recalculer la puissance sur la nouvelle racine.

## 3. Constats

| Id | Gravité | Où | Constat | Correction |
|---|---|---|---|---|
| CM-01 | majeur | prereg l. 156, 192 ; LISEZMOI l. 59 | Oracle changé après observation sur une instance ; observation non archivée ; portée de H1 non conditionnée ; A présenté comme protocole de Bailey | § A, conditions 1 à 6 |
| CM-02 | majeur | prereg l. 52, 218-229, 265 | H1 (B > A) est principal et quasi certain ; la vraie question (poids, tirage, agrégation) est « qualifiante » | H1 en contrôle positif ; synthèse impossible sans les témoins |
| CM-03 | majeur | prereg l. 54, 241-263 ; LISEZMOI l. 82 | D mélange paramètres, famille de fonctions et agrégation ; B − C mélange poids et moniteurs | Ajouter `B_unif`, `B_alea`, `B_ou` (mesure § B) |
| CM-04 | majeur | prereg l. 121-126, 146, 243-263 | δ2 au plancher pour (iii) ; marges absolues mécaniques ; « B > D » à lb95 > 0 sans effet minimal | Pilote à plusieurs δ, choix sur A seul, marges relatives, effet minimal |
| CM-05 | majeur | prereg l. 30, 101 ; puissance l. 54-63, 127-130 | « Erreur ≤ 0,0013 » est la taille sous le double nul ; la taille de l'intersection-union est 0,02 à 0,05 par δ ; la règle n'est pas un test de « effet ≥ S1 » | Corriger résumé et S2 ; nommer la règle |
| CM-06 | majeur | prereg l. 116, 233-239 | S5 choisi par puissance, supérieur à S1, lecture instable à 0,05, choix « en connaissant » la réponse ; « pas un gain net » non dérivé | S5 = S1 par principe ; lecture sans seuil ; retirer la formule |
| CM-07 | majeur | prereg l. 140, 205-212 | Audit asymétrique ; « V(B) ≥ 0,99 » inatteignable | Déclencheur sur tout signe contraire à P1-P4 ; seuil calibré |
| CM-08 | majeur | prereg l. 271-293 ; essais l. 64-70, 111-114, 149-156 | 9 gardes sur 28 sans essai (8 non déclarées) ; deux couvertures affirmées à tort ; test du scellé déplacé de sens | Écrire les essais ; corriger la liste ; test sans compagnon et avec compagnon altéré |
| CM-09 | moyen | arene l. 461-470 | Statut et itérations de SLSQP non consignés ; départ non fini sauté en silence | Consigner, compter, arrêter au-delà d'un taux |
| CM-10 | moyen | prereg l. 161, 193 ; arene l. 573-598 | Coût par contournement : censure tranchée par δ, pas de garde de ligne de base, monotonie supposée, « borne basse » vraie si A non censuré, S14 choisi en regardant | Seuil relatif, garde, parts par δ, ou courbe V(δ') |
| CM-11 | moyen | prereg l. 56, 262 ; arene l. 393-416 | Double oracle non convergé (écart 0,04 ≈ effet à δ2) ; équilibres non uniques sans règle | Dire « itéré tronqué » ; rapporter l'écart ; règle de choix ou déclaration |
| CM-12 | moyen | prereg l. 285, 288 | Un arrêt en cours de run (garde) n'a aucune règle de reprise ; « plusieurs invocations → V0 fausse » rend un redémarrage non concluant ; pas de point de reprise (`pool.map` perd tout) | Écrire : arrêt sans résultat écrit → une reprise complète, même code, nouvel identifiant de run |
| CM-13 | mineur | prereg Tables 1, 2, P2 | Table 1 ligne 4 couvre « gagne à un δ, perd à l'autre » sous « le mélange perd » ; ligne 6 masque la ligne 8 quand un δ est confirmé et l'autre positif sous S1 ; Table 2 ligne 3 couvre « régression démontrée mais sous la tolérance » ; Tables 2 à 4 lues seulement après 5, 6, 8 (motif non écrit) ; P2 à δ2 sans réfutation | Lignes supplémentaires ; motif écrit |
| CM-14 | mineur | arene l. 141-152, 859-862 | Manifeste de décision sans schéma de graines ; seuils du texte non comparés à la configuration ; seul le fichier de code lié | Imprimer la configuration canonique dans le texte scellé et la comparer champ à champ ; ajouter `schema_graines` à `config` |
| CM-15 | mineur | arene l. 127-138, 705 | Garde de racine de décision au niveau de la ligne de commande seulement | Garde dans `executer_tache` ou `gen` avec drapeau posé par `decision` |
| CM-16 | mineur | arene l. 313-316, 349-366 | Oracle à plusieurs unités : seuil gaussien approché, deux départs, non vérifié | Déclarer ; biais défavorable à D |
| CM-17 | mineur | prereg l. 7, 79, 281 | HEAD de l. 7 périmé (`89462343` aujourd'hui) ; V = minimum de deux estimations fraîches (biais d'au plus 0,001 en faveur de l'attaquant) ; tolérance de fausses alertes 0,005 = 50 % de α, lâche pour détecter une dérive entre bras ; confiances basses | Mettre à jour au gel ; déclarer ; rapporter l'écart de fausses alertes entre bras |
| CM-18 | positif | — | Reproductibilité complète, puissance rejouée à l'identique, programme linéaire juste, optimiseurs convergés, attaquant confirmé, code du pilote v2 relié au code remis par 3 lignes, aucune fuite de la racine de décision, déclarations honnêtes des écarts | — |

## 4. Corrections demandées, dans l'ordre

Avant présentation à Lazar :
1. Nouvelle racine d'essai (à fixer sans lien avec un résultat, par exemple 20261293 / 20261294) ; pilote à plusieurs δ ; choix des δ sur A seul ; marges d'équivalence relatives ; règle « > » avec effet minimal (CM-04).
2. Plan : ajouter `B_unif`, `B_alea`, `B_ou` ; H1 en contrôle positif ; signes prédits signés ; recalcul de S4 et S8 (CM-02, CM-03).
3. Réécrire l'écart de conception n° 1 (principe d'abord, bifurcations listées, portée), pilote logistique sur 48 tâches, prédiction signée, issue attendue de chaque option de S13 (CM-01).
4. Corriger résumé l. 30 et S2 ; nommer la règle « pertinence et significativité » (CM-05).
5. S5 = S1 par principe, lecture sans seuil, retirer « pas un gain net » (CM-06).
6. Déclencheurs d'audit symétriques et seuil de « trop beau » calibré (CM-07).
7. S14 relatif avec garde ; parts censurées par δ, ou courbe V(δ') (CM-10).
8. Compléter « ce que l'expérience n'autorise pas » (§ E).

Avant scellement :
9. Les neuf essais de gardes manquants, le test du scellé sans compagnon et avec compagnon altéré, la liste d'arrêt corrigée (CM-08).
10. Statut et itérations de SLSQP consignés, départs non finis comptés (CM-09).
11. Règle de reprise après arrêt ; règle ou déclaration pour les équilibres non uniques ; écart du double oracle rapporté (CM-11, CM-12).
12. Configuration imprimée et comparée, schéma de graines au manifeste, garde de racine dans `gen` (CM-14, CM-15).
13. Lignes de tables supplémentaires (CM-13) ; HEAD, empreintes, puissance sur la nouvelle racine (CM-17).

## 5. Limites de cette contre-lecture

- Je n'ai pas relu les antériorités (toutes « SUPPOSÉ » dans le texte) et n'ai eu aucun accès au réseau.
- Mes diagnostics portent sur 2 à 5 tâches de la racine d'essai : ils confirment ou infirment des mécanismes, ils ne chiffrent pas des effets. Les chiffres des témoins serrés (§ B) sont non opposables.
- La simulation de lecture des tables (§ C) suppose que le pilote représente la vérité ; 300 répétitions, 1 500 rééchantillons chacune : ordre de grandeur, pas valeur.
- Les explications du polyèdre convexe et du coût du partage de seuil sont des raisonnements, non des expériences ; seul le résultat « le “ou” des mêmes moniteurs fait deux fois mieux à δ1 » est mesuré.
- Je n'ai lu de la bibliothèque `controle_ia` que `prereg.py`, `scellement.py`, `manifeste.py`.
- Le brouillon n'est pas scellé et ne doit pas l'être avant le traitement de chaque remarque (accepté, refusé et pourquoi) dans sa section « Contre-lecture ».
