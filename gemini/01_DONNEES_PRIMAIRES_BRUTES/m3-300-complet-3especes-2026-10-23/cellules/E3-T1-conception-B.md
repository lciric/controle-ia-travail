# Proposition B — Tour III.1 : conception ciblée

## 0. État des pièces reçues (règle 2)

L'en-tête de l'Annexe 3 annonce « zéro caractère coupé ». Le texte transmis le contredit. Je n'invente aucun contenu manquant.

- **Argon #01 (FSV-EGK)** : coupé dans la section 2, après « un ensemble $S_p$ de ». Section 3 absente.
- **Argon #02 (RNL-BB-VB-CK)** : coupé dans la section 3, après « réseaux récurrents ».
- **Argon #03 (RQRNS)** : coupé au milieu de la formule de fitness. Section 3 absente.
- **Argon #04 (MKB-Swarm)** : coupé au milieu de la formule d'utilité. Section 3 absente.
- **Argon #05 (BK-TPSB)** : coupé au titre de la section 3.
- **Argon #06 (BRB-HTUO)** : coupé au milieu de la section 2. Section 3 absente.
- **Argon #07 (CFZIB)** : coupé au titre de la section 3.
- **Argon #08 (RAH-S-FGC)** : la section 2 s'arrête sur une phrase complète. Il n'y a pas de section 3. La troncature est probable, mais je ne peux pas l'établir.
- **Argon #09 (KCS-PTS)** : coupé dans la section 3, après « Ét ».
- **Argon #10 (Peskir–McKean-Vlasov)** : coupé dans la section 2, sans ponctuation finale. Section 3 absente.

Autres défauts de transmission :
- **Annexe 2** : plusieurs noms de bassin sont tronqués, par exemple NDE-SPF, GMES-DA, RNL-BB-VB-C et DM-FK.
- **Encodage** : les accents sont corrompus (« ? ») dans les en-têtes. Le contenu reste lisible.
- **Empreintes** : je ne peux pas vérifier les empreintes sha256.
- **Version du protocole** : les faits citent « protocole v2.5 » alors que la consigne cite « v2 ».

**Position sur B1.** La question demande de « fusionner les meilleures briques » en une Loi Mère. Je ne le fais pas : ce serait du lissage. J'attaque les champions et je réutilise nommément cinq briques (§3). Je montre aussi qu'aucune loi $\mathcal{L}^*$ ne peut être évaluée tant que deux instruments n'ont pas été validés : `jev` et le détecteur de failles fatales.

---

## 1. (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Raison |
|---|---|---|---|
| P1 | Les scores `jev` sont de « vrais » scores de qualité. | **OBSERVÉ-NON-AUDITÉ** (faits). Le mot « vrais » n'est pas établi. | Aucune validation de `jev` contre une vérité externe n'est fournie. La formule du composite (Rigueur, Duels, Contrôles, Hyp=Rés) n'est pas donnée. |
| P2 | Les 300 explorateurs ont tous été évalués. | Contredit par l'Annexe 1 (OBSERVÉ-NON-AUDITÉ). | On compte 81 Fable + 95 Opus + 71 Argon = 247 sorties valides. Les 53 non valides ne sont pas décrites. |
| P3 | Les 30 champions sont intégraux. | Contredit (§0). | 10 sur 10 des champions Argon sont coupés ou probablement coupés. |
| P4 | Les écarts entre espèces reflètent leur manière de concevoir l'auto-organisation. | **HYPOTHÈSE** | Il existe au moins deux facteurs confondus : la troncature (§2.2) et le gabarit de consigne (§2.3). |
| P5 | Les vagues de déflation ont un « effet réel ». | **HYPOTHÈSE** | La « déflation » n'est pas définie. On ne dispose que d'agrégats, sans scores individuels. |
| P6 | Il existe une loi $\mathcal{L}^*$ composable à partir des briques. | **HYPOTHÈSE** | Les champions sont des propositions (statut HYPOTHÈSE). Aucune n'a été exécutée. |
| P7 | Un collisionneur figé à 3 tours est sous-optimal. | Le fait structurel est établi par la description même du protocole : la riposte du tour 3 n'est pas attaquée. La sous-optimalité en qualité reste une **HYPOTHÈSE**. | Un remède moins coûteux existe : un tour terminal d'attaque seule (E4). |
| P8 | Le « taux de nouvelles failles fatales » est observable. | **HYPOTHÈSE** | Les faits établissent qu'il n'existe ni tête de sabotage ni sonde. Aucun détecteur de faille fatale n'est validé. Un taux nul peut signifier que les attaquants sont saturés, pas que la proposition est solide. |
| P9 | La règle d'arrêt de Wald garantit ses risques α et β. | **HYPOTHÈSE** | Le SPRT (référence à vérifier) suppose des observations indépendantes. Ici, les tours successifs sont dépendants. |
| P10 | Le « point fixe de Nash-Popper » est un objet défini. | Non défini, donc non évaluable. | Aucune définition n'est donnée dans les faits ni dans la question. |
| P11 | Des duels à « budget constant » sont possibles avec 120 USD au total. | Le budget de 100 + 20 USD est **VÉRIFIÉ**. Son état restant après les 300 explorateurs n'est pas établi. | Voir §3 : 13 champions sur 20 demandent 120 USD **par bras**. |
| P12 | `jev` peut servir de plongement, de juge d'implication, de mesure de dérive ou de sensibilité de Fisher. | **HYPOTHÈSE** | Les faits disent seulement « classifieur/moniteur non génératif ». Sa fonction exacte n'est pas décrite. |
| P13 | Les API permettent d'obtenir des log-probabilités (utilisées par DDA-RS, GMES-DA, VFT-D). | **HYPOTHÈSE** | Les faits ne le mentionnent pas. |
| P14 | H4', H9, H5 et H7 sont des phénomènes réels sur lesquels une loi peut s'appuyer. | **HYPOTHÈSE** (faits) | Une loi qui les « traite » ne peut pas présupposer leur existence. |
| P15 | Il existe des GPU disponibles pour M1. | Le type (A100 80 Go / H200 NVL) est **VÉRIFIÉ**. La quantité n'est pas établie. | — |

---

## 2. Ce que les annexes montrent et ne montrent pas

Toutes les lectures de cette section sont **OBSERVÉ-NON-AUDITÉ**, puisque les annexes elles-mêmes le sont.

**2.1 Les vagues de déflation.**
- **Opus** : moyennes comprises entre 3,88 et 4,25, sans tendance monotone.
- **Argon** : moyennes comprises entre 0,51 et 0,80, avec le maximum en V01.
- **Fable** : les vagues V05, V06, V09 et V10 ont un minimum ≥ 3,85. Les autres vagues ont un minimum ≤ 0,87. Le maximum de Fable culmine en V02 (4,80), c'est-à-dire là où la moyenne est la plus basse (2,70).

Les agrégats sont compatibles avec un **mélange bimodal**. Quelques sorties quasi nulles, de l'ordre de 0,02, tirent la moyenne vers le bas. La remontée tardive de la moyenne tiendrait alors à la disparition de ces échecs, pas à un relèvement du plafond.

Sans les 300 scores individuels, on ne peut pas trancher. E6 le fait.

**2.2 Argon et la troncature.**
- Les colonnes Contrôles (0,04 à 0,11) et Duels (souvent ≤ 0,20) d'Argon sont basses.
- Or 9 champions Argon sur 10 perdent leur section 3, qui est précisément la section des duels et des contrôles.
- Exception partielle : MKB-Swarm place un $H_A\perp H_B$ dès sa loi. C'est le champion Argon qui a le score Duels le plus haut (0,68).

C'est l'indice le plus net des annexes. Il oppose « l'espèce compte » à « la troncature compte » (E1).

**2.3 Le cône détermine le nom.**
- L'indice de cône vaut k mod 10. Par exemple, k=014 donne Cone-04, k=091 donne Cone-01, k=056 donne Cone-06.
- Pour un même (vague, k), les trois espèces convergent vers le même bassin. Avec V01 et k=007, on obtient « Reine-Rouge-Price-Élites » chez Fable, « Reine-Rouge-Price-Elites » chez Opus et « RedQueen-Replicator » chez Argon. Avec V02 et k=012, on obtient RFOT/Franz-Parisi chez Fable et chez Argon.

Les concepts sont donc probablement injectés par la consigne de cône. Ils ne sont pas « conçus » par l'espèce, ce qui affaiblit P4.

Par ailleurs, les textes Argon traitent une autre tâche : ponts inter-silos, « fonction anti-vernis », ablations sur Llama. Ils citent aussi des modèles absents des ressources (« Gemini-Flash », « Claude-3.5-Sonnet » dans RQRNS) et des prix unitaires non sourcés (Argon #10). Ils ne répondent pas à la question de l'auto-organisation de l'essaim.

**2.4 La sélection DPP n'est pas un top par score.** Trois champions Argon (#07 à 0,85, #08 à 0,75, #10 à 0,71) sont absents du top 20 Argon de l'Annexe 2, dont le plancher est à 0,87. Le critère de qualité de la DPP n'est pas donné.

---

## 3. Attaques sur les champions (résistance à Goodhart et cohérence interne)

**3.1 Défaut commun : l'arithmétique budgétaire.** Treize champions allouent explicitement 100 + 20 USD, ou 120 USD, **par bras** : TGCR, Fable-RRPE, GFM-PSZ, KSLC, LMHC, FROD, BNYD, LBCS, CCP-DF, QBDA, SMSC, WIAD et VFT-D. Avec 2 à 4 bras, il faudrait entre 240 et 480 USD, pour 120 USD VÉRIFIÉS au total.
- Deux champions respectent le total : Opus-RRPE (25 + 5 USD × 4 bras) et GMES-DA (« divisés en 3 »).
- Cinq sont ambigus : DDA-RS, MRFP, NDE-SPF, MHPC et VIEIL-FDR.

Il s'agit d'une lecture du texte transmis, vérifiable par simple comptage.

**3.2 Défauts propres, tous vérifiables par un script ou un calcul.**

| Champion | Défaut | Verdict provisoire (HYPOTHÈSE) |
|---|---|---|
| GFM-PSZ | Le texte pose $f$ = (nombre de familles − 1) = 2, donc $n_{\text{eff}} \ge 3f+1 = 7$. Mais il compte aussi chaque famille comme un seul nœud, d'où $n_{\text{eff}} \le 3$. La condition d'adoption ne peut jamais être satisfaite. | S'effondre (contradiction interne). |
| QBDA | Il faut $\kappa \ge 2\lceil n\hat\rho\rceil+1$ chemins sommet-disjoints. Dans un graphe à $n$ nœuds, $\kappa \le n-1$. La condition devient donc infaisable dès $\hat\rho \gtrsim 0{,}5$, c'est-à-dire exactement quand H4' est forte. | La topologie s'effondre. Je garde ses canaris et son critère « intra ≈ inter ⇒ rejet », que je réutilise dans E3. |
| MHPC | Le texte affirme que « le juge n'intervient jamais », mais la vérité $y_t$ est « révélée par `jev` ». La règle logarithmique n'est propre que vis-à-vis de $y$. Goodhart revient donc par $y$. | Résistance à Goodhart non établie. |
| TGCR | « Si CUSUM ne déclenche jamais, H9 est réfutée. » C'est un non-sequitur : le silence peut venir de l'insensibilité de CUSUM. Il faudrait d'abord mesurer la détection sur une dérive plantée. | Falsification mal construite. |
| SMSC | Les propriétés du BTS (référence à vérifier) supposent de nombreux répondants et un a priori commun. Avec trois familles d'erreurs corrélées, c'est exactement H4'. | Garantie non transférable en l'état. |
| LMHC | Introduit un « juge LLM » $s_J$ absent du dispositif, ce qui ajoute un coût et une cible Goodhart. | Affaibli. |
| DDA-RS, GMES-DA, VFT-D | Supposent l'accès aux log-probabilités (P13) ou une sensibilité de `jev` (P12). | Instrument non établi. |
| VIEIL-FDR, MRFP, KSLC | Exigent de nombreuses répliques ou trajectoires (EDMD sur 20 trajectoires, $P(q)$ inter-répliques). Ce coût est incompatible avec 120 USD répartis entre plusieurs bras. | Infaisables à budget constant, sauf sur GPU local (§6). |
| Argon ×10 | Tronqués et hors sujet (§2.2, §2.3). | Non évaluables. Ce n'est pas un « effondrement » : on ne peut simplement pas les juger. |

**3.3 Briques que je réutilise, en le disant.**
- **BNYD** : contrôle C, avec le même nombre et les mêmes types de spawns mais une temporalité aléatoire.
- **CCP-DF** : θ* permuté, avec composition et distribution de phases conservées.
- **Opus-RRPE** : partage du budget entre bras et écart $\Delta_G$ entre score optimisé et score tenu à l'écart.
- **QBDA** : canaris et critère de falsification intra/inter.
- **WIAD** : SPRT sur items-pièges, retenu uniquement comme heuristique.

Ces briques survivent parce que leur effet se ramène à une vérité mécanique externe et que leur contrôle négatif conserve le volume. Je ne les fusionne pas en une loi : je les utilise comme **contrôles** dans les expériences de la §4.

---

## 4. (b) Expériences décisives

Toutes les prédictions ont le statut **HYPOTHÈSE**. Tous les seuils sont **illustratifs**.

Plusieurs expériences reposent sur un socle commun, le **corpus C-PLANT**. Il contient les 20 champions Claude, chacun décliné en trois versions :
1. **Version paraphrasée honnête**, sans faille ajoutée.
2. **Version à faille fatale unique plantée par script.** Les failles possibles sont : budget de 4 × 120 USD, contrainte rendue insatisfiable sur le modèle de GFM-PSZ, citation inventée, contrôle négatif supprimé, inégalité de falsification inversée.
3. **Version à faille sémantique plantée à la main**, qu'aucun script ne détecte.

La vérité terrain est connue par construction. C'est la seule réponse disponible au fait VÉRIFIÉ qu'il n'existe « aucune tête de sabotage pré-établie ».

### E1 — Troncature ou espèce ?

- **$H_A$** : le composite bas d'Argon est un artefact de la perte des sections 2 et 3.
- **$H_B$** : le composite bas d'Argon reflète le contenu, indépendamment de la longueur.

**Protocole.**
- (i) Couper les 20 champions Claude à la même position relative que les textes Argon, avant ou dans la section 2 ou 3, puis les rescorer avec `jev`. Coût : 0 USD.
- (ii) Relancer les 10 consignes Argon avec une limite de sortie plus haute. Que la cause soit la limite de sortie est une HYPOTHÈSE. Coût illustratif : ≤ 2 USD Gemini.

**Métrique.** Médiane du composite.

**Seuils (illustratifs).**
- $H_A$ est retenue si les Claude coupés ont une médiane ≤ 2,0 **et** les Argon complets une médiane ≥ 3,0.
- $H_B$ est retenue si les Claude coupés ont une médiane ≥ 3,5 **et** les Argon complets une médiane ≤ 2,0.

**Contrôle négatif.** Retirer des textes Claude le même nombre de caractères, mais **à l'intérieur de la section 1**, en conservant les sections 2 et 3. Si le score chute autant, `jev` est sensible à la longueur et non aux sections. C'est une troisième issue, qui invalide aussi P1.

**Ce qui est falsifié.**
- Si les Claude coupés restent ≥ 3,5, $H_A$ est fausse.
- S'ils tombent à ≤ 2,0, $H_B$ est fausse, et toute comparaison entre espèces fondée sur l'Annexe 1 devient nulle.

### E2 — `jev` mesure-t-il la solidité ou la forme ?

- **$H_A$** : `jev` distingue une proposition à faille fatale de sa jumelle honnête.
- **$H_B$** : `jev` est prédit par des traits de surface : longueur, nombre de sections, LaTeX, et mots-clés comme « contrôle négatif », « $H_A$ », « Wilcoxon » ou « p<0,01 ».

**Métriques.**
- AUC de `jev` sur les paires (jumelle à faille, jumelle honnête).
- R² d'une régression sur les seuls traits de surface pour prédire `jev`, sur les 247 sorties si les scores individuels sont fournis, sinon sur C-PLANT.

**Seuils (illustratifs).**
- $H_A$ est retenue si l'AUC est ≥ 0,75 **et** le R² de surface < 0,5.
- $H_B$ est retenue si l'AUC est ≤ 0,6 **ou** le R² de surface ≥ 0,8.

**Contrôle négatif.** Paires (honnête, paraphrase honnête). L'écart doit rester sous la marge dans ≥ 95 % des cas (illustratif). Sinon, le taux de fausses alertes de `jev` est rédhibitoire.

**Ce qui est falsifié.**
- Une AUC ≤ 0,6 falsifie l'usage de `jev` comme récompense dans **toute** version de $\mathcal{L}^*$.
- Une AUC ≥ 0,75 avec un R² < 0,5 falsifie la lecture « `jev` = rubrique de forme ».

### E3 — Monoculture ou chimère (H4')

- **$H_A$** : les ratés de détection sont plus corrélés au sein d'une famille qu'entre familles.
- **$H_B$** : il n'y a pas d'écart.

**Protocole.** Sur les 60 items de C-PLANT à faille sémantique ou honnêtes (illustratif), chaque famille (fable, opus, argon) attaque avec 2 variantes de consigne et 2 graines.

**Métrique.** Corrélation φ des ratés par paire d'attaquants, en distinguant intra-famille et inter-famille, avec un IC par bootstrap sur les items.

**Seuils (illustratifs).**
- $H_A$ est retenue si $\rho_{\text{intra}}-\rho_{\text{inter}}\ge 0{,}15$ avec un IC à 99 % excluant 0.
- $H_B$ est retenue si $|\Delta|<0{,}05$.

**Contrôles négatifs.**
- (i) Même modèle avec des consignes différentes. Si la diversité de consigne réduit ρ autant qu'un changement de famille, le levier « chimère » est la consigne et non les poids.
- (ii) Étiquettes de raté permutées entre items. On doit alors obtenir ρ ≈ 0.

**Ce qui est falsifié.**
- Un $\Delta$ nul falsifie le routage chimérique de *tous* les champions. C'est le critère de QBDA, que je réutilise ici.
- Un $\Delta$ positif qui survit au contrôle (i) falsifie $H_B$.

**Vérification mécanique à battre.** Les failles scriptables (budget, satisfiabilité, résolution de citations) sont exclues de la mesure. Le détecteur LLM n'a de valeur que sur les failles sémantiques.

### E4 — Nombre de tours adaptatif ou figé

C'est le duel central de la question. Les quatre bras disposent du **même nombre total de jetons**.

**Bras.**
- **F3** : collisionneur figé à 3 tours.
- **F3+A** : 3 tours, puis un tour terminal d'**attaque seule** sans réécriture. C'est le remède minimal au défaut structurel de P7.
- **AD** : on poursuit jusqu'à 2 tours consécutifs sans nouvelle faille fatale, avec un plafond $T_{\max}=6$ (illustratif). Une faille est confirmée soit par un script, soit par ≥ 2 attaquants de familles distinctes.
- **AD-perm** : les temps d'arrêt sont tirés dans la distribution empirique de AD, puis assignés au hasard. C'est le contrôle de la règle d'arrêt, sur le modèle du contrôle C de BNYD.

**Hypothèses.**
- **$H_A$** : l'adaptativité de T est le levier. Le taux résiduel de failles plantées en sortie est plus bas pour AD que pour F3+A, d'au moins δ.
- **$H_B$** : le seul levier est l'attaque terminale. Le résiduel de AD est ≥ résiduel de F3+A − δ.

**Métrique primaire.** Proportion des failles plantées encore présentes dans la version finale.

**Métrique secondaire.** Taux de « failles fatales » signalées à tort sur les jumelles honnêtes.

**Seuil.** δ = 0,10 (illustratif), avec un test de permutation apparié par item et α = 0,01.

**Ce qui est falsifié.**
- Si AD ≈ F3+A, l'adaptativité de T est falsifiée comme levier. C'est le présupposé de la question.
- Si AD < F3+A et AD < AD-perm, $H_B$ est falsifiée.
- Si AD < F3+A mais AD ≈ AD-perm, le gain vient de faire plus de tours en moyenne, pas de la règle d'arrêt. La règle « Wald / Nash-Popper » est alors falsifiée en tant que telle.

**Croisement avec E3.** On répète AD avec des attaquants mono-famille. S'ils s'arrêtent plus tôt et laissent plus de failles, cela confirme P8 : un taux nul de nouvelles failles traduit la saturation des attaquants, pas la solidité.

### E5 — Taille des sous-essaims $k_t$

Cette expérience réutilise les données d'E3 par sous-échantillonnage, sans coût supplémentaire.

- **$H_A$** : la détection sature. L'ajustement de $1-(1-p)^{k_{\text{eff}}}$ donne $k_{\text{eff}}\le 3$ à $k=8$.
- **$H_B$** : les attaquants sont quasi indépendants, avec $k_{\text{eff}}\ge 0{,}7k$.

**Contrôle négatif.** Étiquettes permutées entre items. On doit retrouver $H_B$. Si les données réelles l'ajustent aussi bien, $H_A$ est falsifiée.

**Ce qui est falsifié.** $H_A$ falsifie tout schéma $k_t$ croissant en monoculture. $H_B$ falsifie l'intérêt d'un $k_t$ appris : un $k$ fixe suffit.

### E6 — Effet des vagues

Cette expérience ne coûte rien, mais exige les 300 scores individuels, qui n'ont pas été transmis.

- **$H_A$** : le rang de vague améliore les scores parmi les sorties non échouées. Le seuil d'échec est à 1,0 pour Claude (illustratif).
- **$H_B$** : seul le taux d'échec varie selon la vague.

**Métrique.** Corrélation de Spearman entre vague et score sur les sorties non échouées, et régression logistique de l'échec sur la vague.

**Contrôle négatif.** Étiquettes de vague permutées.

**Ce qui est falsifié.**
- Un ρ de Spearman qui n'est pas significatif à α = 0,01 falsifie l'« effet réel » des vagues sur la qualité.
- Une tendance qui survit au contrôle falsifie $H_B$.

---

## 5. (c) Instruments nommés dans la question : la mesure minimale

| Instrument | Taux de détection, mesuré sur… | Taux de fausses alertes, mesuré sur… | Vérification mécanique à battre | Seuil minimal pour « fonctionne » (illustratif) |
|---|---|---|---|---|
| `jev-1.14.0` comme score | Les paires (faille plantée, jumelle honnête) de C-PLANT (E2). | Les paires (honnête, paraphrase honnête). | Une régression sur les traits de surface et la longueur du texte. Le test de troncature (E1). | AUC ≥ 0,75, fausses alertes ≤ 5 %, et un gain d'AUC ≥ 0,15 sur le modèle de surface. |
| `jev` comme capteur (plongement, dérive, $p(o\mid s)$, Fisher) | Pour la dérive : des consignes déléguées dont on modifie une contrainte par script. | Des reformulations fidèles de la consigne. | Une distance d'édition et un test d'inclusion de la contrainte par regex. | Battre la regex d'au moins 0,1 d'AUC. Sinon, la regex suffit. |
| Collisionneur / Red-Team comme détecteur de failles fatales | Les failles sémantiques plantées (E3, E4). | Les jumelles honnêtes. | L'union des scripts : somme des budgets par bras ≤ 120, satisfiabilité des contraintes, résolution Crossref/Semantic Scholar, présence d'un contrôle négatif. | Détection ≥ 0,7 sur les failles sémantiques, fausses alertes ≤ 0,1. Sur les failles scriptables, le script fixe la référence. |
| Règle d'arrêt « Wald / Nash-Popper » | La fraction des arrêts survenant alors qu'une faille plantée subsiste (E4). | Les arrêts tardifs sur des items honnêtes, qui gaspillent le budget. | Un $T$ fixe et la règle naïve « 2 tours vides ». | Arrêts prématurés inférieurs de ≥ 0,1 à ceux de la règle naïve, et victoire sur AD-perm. |
| Sélection DPP | La diversité, mesurée mécaniquement : nombre de cônes distincts et recouvrement de n-grammes entre champions. | Les champions tronqués ou hors sujet retenus (ici, 10 sur 10 chez Argon). | Un tirage aléatoire stratifié par cône, et le top par score. | Faire mieux que le tirage stratifié sur la diversité sans retenir de texte tronqué. |
| Vagues de déflation | La nouveauté inter-vagues : recouvrement des bassins et des n-grammes avec les vagues précédentes. | Les noms répétés d'une vague à l'autre ou d'une espèce à l'autre (§2.3). | Une déduplication par nom de bassin. | Recouvrement inférieur d'au moins un tiers à une vague témoin sans déflation, dont le coût est illustratif. |
| API de littérature comme vérificateur de citations | Des références inventées par perturbation : année, auteur ou DOI. | Des références réelles mal formatées. | Une recherche exacte par DOI. | Rappel ≥ 0,95 sur les inventions, fausses alertes ≤ 0,05. |

---

## 6. (d) Ancrage matériel et séquence exécutable

**Modèles.**
- `Llama-3.1-8B-Instruct` et `70B` (VÉRIFIÉ, projet `controle-ia`).
- Les API `claude-fable-5-1`, `claude-opus-5-5` et `gemini-4-argon` (VÉRIFIÉ).

**Calcul.**
- E1 à E6 ne requièrent **aucun GPU**.
- **8B en bf16** : environ 16 Go de poids, ce qui tient sur une A100 80 Go (illustratif).
- **70B en bf16** : environ 140 Go de poids, donc 2 × A100 80 Go ou une quantification. Une seule H200 NVL serait juste, faute de marge pour le cache KV (illustratif, à vérifier).

**Proposition M1 (HYPOTHÈSE).** On peut tester H9 sans budget API.
- Faire tourner sur GPU des chaînes de $k\le 8$ délégations entre instances de Llama-8B (illustratif).
- Utiliser une contrainte mécaniquement vérifiable, par exemple un outil interdit ou un format imposé.
- Ordre de grandeur : quelques GPU-heures pour 200 tâches (illustratif).

Limite : 8B et 70B appartiennent à la même famille de poids. Cela ne constitue pas une chimère pour tester H4'.

**Budget API (tous chiffres illustratifs, sous réserve que les 120 USD n'aient pas été consommés par les 300 explorateurs, cf. P11).**

| Poste | Claude (USD) | Gemini (USD) |
|---|---|---|
| E1 (relance Argon) | 0 | 2 |
| E2, E6 et scripts mécaniques | 0 | 0 |
| E3 et E5 (720 appels, à environ 0,03–0,08 USD l'appel) | 40 | 10 |
| E4 (4 bras partageant le même budget) | 45 | 6 |
| Réserve | 15 | 2 |
| **Total** | **100** | **20** |

**Séquence d'exécution.** Le point 3 de la question demande une spécification exécutable. Je la conditionne aux portes de validation.

```
0. Pré-enregistrer les seuils de E1 à E6 (fichier haché avant tout appel).
1. Phase 0, à 0 USD :
   a. Scripts mécaniques sur les 30 champions : budget, satisfiabilité, résolution des citations.
   b. Construire C-PLANT.
   c. E2, puis E1 (volet Claude), puis E6 (si les scores individuels sont fournis).
   PORTE 1 : si l'AUC de jev est ≤ 0,6, jev est retiré de toute récompense.
             Il reste au mieux un filtre.
2. Phase 1 : E1 (relance Argon, environ 2 USD Gemini).
   PORTE 2 : si la troncature explique l'écart, l'Annexe 1 n'entre pas
             dans le routage entre espèces.
3. Phase 2 : E3, puis E5 (hors ligne).
   PORTE 3 : si ρ_intra ≈ ρ_inter, le routage chimérique est abandonné.
             Si k_eff est faible, k est plafonné.
4. Phase 3 : E4 avec les 4 bras appariés, et la variante mono-famille si la réserve le permet.
   PORTE 4 : on adopte la règle de T qui gagne. Si c'est F3+A, on garde 3 tours + audit terminal.
5. Seulement ensuite : écrire L* en ne gardant que les leviers qui ont survécu aux portes 1 à 4.
   M1 se fait sur GPU local (chaînes Llama) : M2 et M1 sont lancés sur des instruments validés.
```

---

## 7. Ce qui peut être réfuté par cette proposition

1. `jev` est un instrument de solidité (E2).
2. Les écarts entre espèces viennent des espèces (E1).
3. Les vagues de déflation améliorent la qualité (E6).
4. La chimère réduit la corrélation des erreurs au-delà de la seule diversité de consigne (E3).
5. Ajouter des attaquants en monoculture augmente la détection (E5).
6. L'adaptativité de $T$ apporte quelque chose au-delà d'un tour terminal d'audit (E4).
7. La règle d'arrêt elle-même apporte quelque chose au-delà du nombre moyen de tours (E4, bras AD-perm).
8. GFM-PSZ et la topologie de QBDA sont déjà réfutés par le calcul (§3.2), sous réserve que le lecteur vérifie mon arithmétique.

FIN-DE-CELLULE