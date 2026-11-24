# Rapport d'analyse — Extraction rétrodictive sur processeur des foyers de tension et d'épicycles dans les sources de contrôle, d'alignement et d'interprétabilité (`<= 2024` vers `2025–2026`, version 1)

## Verdict exécutif

**VERDICT DE L'ÉPREUVE PRIMAIRE PRÉENREGISTRÉE : RÉFUTÉ.**
Sur les `502` documents canoniques éligibles (`92` à $t \le 2024$ hors révisions postérieures à `2024`, et `410` en `2025–2026`) répartis dans `11` sous-domaines techniques éligibles, le détecteur purement lexical et syntaxique de foyers de tension et d'épicycles mesuré à $t \le 2024$ **échoue franchement** à prédire le taux d'articles à forte formalisation ou reformulation théorique en `2025–2026` : l'aire sous la courbe caractéristique de réception vaut **$A(X, Z) = 0,1667$** (intervalle de confiance à `95 %` : `[0,0000 ; 0,4667]`), la corrélation des rangs de Spearman est **négative ($\rho_S = -0,6273$, valeur-$p$ unilatérale supérieure $p_{\text{perm}} = 0,9790$)**, le facteur d'enrichissement à la médiane tombe à **$E_{50\%} = 0,4400$** (test exact de Fisher unilatéral supérieur $p = 0,9870$), et le signal est battu à la fois par le hasard (`0,5000`), par la base de volume pur ($A(V, Z) = 0,4000$, soit $\Delta A_{\text{vol}} = -0,2333$) et par la base d'ancienneté moyenne des concepts ($A(A_{\text{âge}}, Z) = 0,5667$, soit $\Delta A_{\text{âge}} = -0,4000$).

L'audit de symétrie obligatoire (règle de symétrie des vérifications, `R4`) et l'analyse de différence temporelle préenregistrée établissent que cet échec n'est dû **ni à un bogue d'extraction** (`99,89 %` de réussite de `pdftotext`, `561` occurrences de tension extraites en amont, témoin nul « doit mourir » exact à `0,4919`), **ni à un unique sous-domaine aberrant** ($\rho_S \in [-0,7576 ; -0,5030]$ par omission unitaire), mais à un **biais structurel de registre disciplinaire** : les marqueurs lexicaux de surface opposent les sous-domaines expérimentaux d'attaque-défense (auto-encodeurs épars, portes dérobées, contournements d'invites — riches en aveux d'heuristiques et de fragilité, mais restant peu démonstratifs en `2025–2026`) aux sous-domaines mathématisés de longue date (audit séquentiel par martingales et calibration hors domaine — sobres en vocabulaire d'épicycles et saturés en théorèmes). Lorsque cet effet fixe disciplinaire est soustrait par projection temporelle ($\Delta\bar{R}_k$), l'inversion disparaît ($\rho_S = +0,1000$) sans toutefois dégager de pouvoir prédictif suffisant. Ce résultat négatif net valide empiriquement à `0,00` dollar américain l'avertissement théorique de la piste d'extraction sémantique des transgressions formelles (`IDE-2026-11-23-041`) : **un comptage lexical de mots-clés d'épicycles ne doit pas être branché en amont de l'organisme d'idéation**.

---

## 1. Traçabilité et empreintes cryptographiques sur 256 bits (règle `R6`)

Tous les chiffres rapportés dans le présent document proviennent exclusivement de l'exécution unique et sans retouche du code scellé avant course sur le préenregistrement scellé et contre-lu :

- **Préenregistrement scellé avant toute ouverture des documents** : `prereg-pas0-rang1-retrodiction-foyers-tension-2024-vers-2025-2026-v1.md` (`dcc8de2e34cf871eb380e385789b25e97e779182fbe681bb6739f102de6e2e67`), révisé après contre-lecture indépendante du brouillon 1 (`28dc3ab6949ff312e2156ae869128d0b8723793c98107bb74054d8c9f87dfd62`) par le sous-agent neuf `8ce0b993687504c727f5781919798801` dont le rapport est archivé sous `contre-lecture-r2-prereg-pas0-rang1-v1.md` (`4e2cd97dd77ea330b351586bd6dea6bc61dcda66ff132899504724d4c4e675a4`).
- **Extracteur déterministe scellé avant exécution réelle** : `extracteur_foyers_tension_rang1_v1.py` (`a28deb5d468fa127c9912645dd0619b56af0c292eb93aa749ab7f17adcc6d3c9`).
- **Suite d'essais unitaires de gardes d'arrêt scellée (6 essais sains/artefacts passés à 100 %)** : `test_extracteur_foyers_tension_rang1_r5_v1.py` (`36a94e89e4efa784cc1f9098a223806ed099c0716bed9c02eeee21babfea5d97`).
- **Résultats numériques bruts complets scellés** : `resultats-retrodiction-rang1-v1.json` (`319e729884c92f80b0fbc48b03e11fc74f66109c063a02bc8bb7d2fba9aef0d1`).
- **Environnement et coût** : Python `3.12.16`, NumPy `2.4.6`, SciPy `1.17.1`, `pdftotext` `24.02.0`, séquence maîtresse `SeedSequence(2026112401)`, dépense `0,00` dollar américain, dépôt git maintenu strictement en lecture seule au commit `ea9e544220b17873071a9868f619ad4f6fc48bca`.

---

## 2. Inventaire du corpus local et passage des cinq gardes d'arrêt (`R5`)

L'inspection préalable a confirmé que la branche distante `origin/idees/revue-bibliographique-v1` n'ajoute aucun fichier au format de document portable par rapport à `docs/sources/pdf/` sur la branche principale. Sur `docs/sources/pdf/` :

| Étape de filtrage et de contrôle d'intégrité | Effectif ou valeur mesurée | Statut de la garde d'arrêt |
|---|---|---|
| Fichiers au format de document portable présents sur disque | `1 121` | Inventaire complet |
| Documents canoniques uniques après dédoublonnage (`arXiv` sans version ou empreinte binaire) | `912` (`209` doublons/versions écartés) | Règle de version appliquée (`v1` min en $\le 2024$, `vK` max en `2025–2026`) |
| Garde n° 1 — Conformité et empreinte du préenregistrement scellé | Empreinte exacte vérifiée | **PASSÉE** |
| Garde n° 2 — Disjonction sur 6 directions, suffixes-préfixes et sous-groupes | `0` collision détectée | **PASSÉE** |
| Garde n° 3 — Extraction `pdftotext` et seuil minimal de `250` mots bruts | `911 / 912` valides (`1` échec à `208` mots : `rosin-belew-1996`, taux de panne `0,11 %` $\le 15 \%$) | **PASSÉE** |
| Garde d'étanchéité temporelle — Prépublications $\le 2024$ portant une mention `2025`/`2026` en ouverture | `21` révisions post-2024 détectées et exclues de l'épreuve primaire | **APPLIQUÉE** (testées à part en variante `c`) |
| Filtre d'éligibilité thématique « Contrôle, alignement, sécurité et interprétabilité » (primaire) | **`502` documents éligibles** : **`92` en amont ($\le 2024$)** et **`410` en aval (`2025–2026`)** | Hors-sujet financier/scientométrique et non-IA écartés |
| Garde n° 4 — Planchers d'effectifs (`>= 40` éligibles, `>= 30` rattachés) et non-nullité des écarts types | Amont : `92` éligibles (`49` rattachés) ; Aval : `410` éligibles (`362` rattachés) ; `0` écart type nul | **PASSÉE** |
| Garde n° 5 — Témoin nul « doit mourir » (`2 000` permutations aléatoires sous $H_0$) | Moyenne $A(X, Z^{(b)}) = 0,4919 \in [0,47 ; 0,53]$ ; erreur empirique de 1re espèce $= 0,0430 \le 0,070$ | **PASSÉE** (zéro fuite statistique) |

**Déséquilibre chronologique structurel du fonds local** : la répartition annuelle des `502` articles éligibles primaires (`resultats-retrodiction-rang1-v1.json`, lignes 53–68) montre que le fonds local du dépôt est fortement concentré sur la veille récente (`290` articles en `2026`, `120` en `2025`, contre `25` en `2024`, `19` en `2023`, et `48` répartis entre `2010` et `2022`). Sept des `18` sous-domaines techniques comptent ainsi moins de `3` articles amont dans `docs/sources/pdf/` alors qu'ils sont massivement représentés en `2025–2026` (notamment `AXE_18` agents autonomes : `0` contre `103` ; `AXE_01` sondes linéaires de mensonge : `1` contre `43` ; `AXE_04` pilotage d'activations : `1` contre `26` ; `AXE_13` fidélité de la chaîne de pensée : `1` contre `21` ; `AXE_09` désapprentissage : `0` contre `10`), laissant **`K_élig = 11` sous-domaines éligibles** ($\ge 10$ requis).

---

## 3. Résultats de l'épreuve primaire préenregistrée (`K_élig = 11` sous-domaines)

Sur la tranche aval (`410` articles), le seuil du quartile supérieur du score de reformulation et de caractérisation formelle vaut $Q_{0,75}(R) = +0,0248$, identifiant `103` articles de percée ou reformulation formelle majeure (`25,12 %`). Sur les `11` sous-domaines éligibles, la médiane de tension amont vaut $m_X = -0,0392$ et la médiane du taux de percées aval vaut $m_Y = 0,2165$ (aucun repli de plateau n'a été nécessaire).

| Métrique préenregistrée | Valeur observée | Seuil de confirmation | Seuil de réfutation | Lecture selon les critères gelés |
|---|---|---|---|---|
| Nombre de sous-domaines éligibles ($K_{\text{élig}}$) | **`11`** | $\ge 10$ | — | Effectif suffisant |
| Aire sous la courbe caractéristique de réception $A(X, Z)$ | **`0,1667`** (IC 95 % : `[0,0000 ; 0,4667]`) | $\ge 0,65$ | $\le 0,52$ | **Réfutation franche** (inversion sous `0,50`) |
| Corrélation des rangs de Spearman $\rho_S(X_k, Y_k^{\text{taux}})$ | **`-0,6273`** | $\ge +0,35$ | $\le +0,05$ | **Réfutation franche** (anti-corrélation marquée) |
| Valeur-$p$ unilatérale supérieure par permutation ($10\,000$ tirages) | **`0,9790`** | $\le 0,05$ | — | Non significatif dans le sens prédit |
| Facteur d'enrichissement à la médiane $E_{50\%}$ | **`0,4400`** | $\ge 1,35$ | $\le 1,00$ | **Réfutation franche** (`1/5` au-dessus de $m_X$ contre `4/6` en dessous) |
| Rapport de cotes régularisé de Haldane-Anscombe et test exact de Fisher descriptif | **`0,1852`** ($p_{\text{Fisher}} = 0,9870$) | — | — | Table $2 \times 2$ : `a=1, b=4, c=4, d=2` |
| Aire sous la courbe de la base de volume amont $A(V, Z)$ et écart $\Delta A_{\text{vol}}$ | $A(V, Z) = 0,4000$ ; **$\Delta A_{\text{vol}} = -0,2333$** | $\Delta A_{\text{vol}} \ge +0,05$ | $\Delta A_{\text{vol}} \le 0,00$ (si $\rho_{\text{part}} \le 0,05$) | **Dominé par la base de volume pur** |
| Aire sous la courbe de l'ancienneté moyenne $A(A_{\text{âge}}, Z)$ et écart $\Delta A_{\text{âge}}$ | $A(A_{\text{âge}}, Z) = 0,5667$ ; **$\Delta A_{\text{âge}} = -0,4000$** | $\Delta A_{\text{âge}} \ge 0,00$ | — | **Battu par l'ancienneté moyenne des concepts** |
| Corrélation partielle des rangs contrôlée pour le volume $\rho_{S,\text{partiel}}(X, Y \mid V)$ | **`-0,7108`** | $\ge +0,25$ | $\le +0,05$ (avec $\Delta A_{\text{vol}} \le 0$) | **Réfutation confirmée hors effet de volume** |
| Corrélation partielle contrôlée pour le volume et l'âge $\rho_{S,\text{partiel}}(X, Y \mid V, A_{\text{âge}})$ | **`-0,6821`** | $\ge +0,20$ | — | Négative après contrôle conjoint |

### Détail complet des 11 sous-domaines éligibles (classés par tension amont $X_k$ décroissante)

| Rang $X_k$ | Code et intitulé explicite du sous-domaine | $n_{\le 2024}$ | $n_{2025\text{–}2026}$ | Tension amont $X_k$ | Taux aval $Y_k^{\text{taux}}$ | Base amont $Y_k^{\text{taux}, \le 2024}$ | Accroissement $\Delta\bar{R}_k$ | Âge amont (ans) | $(I_X, Z_k)$ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `AXE_02` — Auto-encodeurs épars, superposition et dictionnaires de traits | 3 | 13 | **`+0,3306`** | `7,69 %` | `0,00 %` | `+0,0389` | `1,00` | `(1, 0)` |
| 2 | `AXE_08` — Portes dérobées, chevaux de Troie, empoisonnement et agents dormants | 11 | 54 | **`+0,1583`** | `18,52 %` | `18,18 %` | `-0,0982` | `0,36` | `(1, 0)` |
| 3 | `AXE_06` — Contournement des garde-fous d'invites et attaques adverses d'entrée | 11 | 97 | **`+0,0251`** | `21,65 %` | `9,09 %` | `+0,0126` | `0,45` | `(1, 0)` |
| 4 | `AXE_07` — Classifieurs de garde-fous, modération et entraînement au refus | 6 | 59 | **`-0,0035`** | **`23,73 %`** | `16,67 %` | `+0,0698` | `0,33` | `(1, 1)` |
| 5 | `AXE_15` — Équipes rouges automatisées et recherche adaptative d'attaques | 11 | 77 | **`-0,0279`** | `20,78 %` | `18,18 %` | `-0,0484` | `1,27` | `(1, 0)` |
| 6 | `AXE_05` — Apprentissage sur retours humains, suroptimisation de récompense et complaisance | 8 | 76 | `-0,0392` | **`27,63 %`** | `12,50 %` | `+0,2103` | `0,63` | `(0, 1)` |
| 7 | `AXE_11` — Protocoles de contrôle de l'intelligence artificielle et surveillance de sabotage | 4 | 49 | `-0,0989` | `10,20 %` | `0,00 %` | `+0,0256` | `0,25` | `(0, 0)` |
| 8 | `AXE_12` — Supervision évolutive, débat contradictoire et juges automatisés | 6 | 43 | `-0,1762` | `13,95 %` | `16,67 %` | `-0,1618` | `0,50` | `(0, 0)` |
| 9 | `AXE_10` — Tromperie stratégique, dissimulation de capacités et conscience d'évaluation | 4 | 55 | `-0,2526` | **`27,27 %`** | `0,00 %` | **`+0,3137`** | `0,00` | `(0, 1)` |
| 10 | `AXE_17` — Transfert hors domaine et calibration sélective des détecteurs | 7 | 23 | `-0,2604` | **`39,13 %`** | **`28,57 %`** | `-0,1960` | **`4,00`** | `(0, 1)` |
| 11 | `AXE_16` — Audit statistique séquentiel, valeurs de preuve et garanties toujours valides | 5 | 17 | `-0,2726` | **`76,47 %`** | **`20,00 %`** | `+0,0249` | **`2,00`** | `(0, 1)` |

*(Note : parmi les 7 sous-domaines non éligibles faute d'au moins 3 articles amont dans le fonds local, `AXE_01` sondes linéaires de mensonge affiche $X_{01} = +0,2286$ sur $n=1$ et $\Delta\bar{R}_{01} = +0,2241$ sur $n=43$ ; `AXE_04` pilotage d'activations affiche $X_{04} = +0,0238$ sur $n=1$ et $\Delta\bar{R}_{04} = +0,2251$ sur $n=26$ ; `AXE_13` fidélité de la chaîne de pensée affiche $Y_{13}^{\text{taux}} = 33,33 \%$ et $\Delta\bar{R}_{13} = +0,3675$ sur $n=21$.)*

---

## 4. Résultats des six analyses secondaires préenregistrées et de l'audit de symétrie (`R4`)

### 4.1 Synthèse des analyses secondaires `(a)` à `(f)`

1. **Analyse `(a)` — Contrôle de la tradition formelle initiale et projection temporelle $\Delta\bar{R}_k$** :
   - La corrélation partielle des rangs $\rho_{S,\text{partiel}}(X_k, Y_k^{\text{taux}} \mid Y_k^{\text{taux}, \le 2024}, V_k, A_{\text{âge}, k})$ reste négative à **`-0,6006`** sur le taux du quartile supérieur, parce que `AXE_16` passe de `20,00 %` à `76,47 %` et `AXE_10` de `0,00 %` à `27,27 %`.
   - En revanche, sur l'**accroissement continu du score moyen de formalisation projeté sur l'échelle amont** ($\Delta\bar{R}_k = \bar{R}_k^{2025\text{–}2026, (\text{base } \le 2024)} - \bar{R}_k^{\le 2024}$), l'anti-corrélation s'efface entièrement et devient légèrement positive : **$\rho_S(X_k, \Delta\bar{R}_k) = +0,1000$** (`AXE_17`, déjà très mathématisé en amont, recule à $\Delta\bar{R}_{17} = -0,1960$, tandis que `AXE_07`, `AXE_02` et `AXE_06` ont $\Delta\bar{R}_k > 0$). L'inversion primaire de `-0,6273` provient donc essentiellement de la différence statique de niveau formel entre sous-domaines, mais même corrigé en différence première, le signal lexical brut reste quasi nul (`+0,10`).
2. **Analyse `(b)` — Assignation primaire exclusive des articles ($n_{\min} = 2$, $K_{\text{élig}} = 11$)** :
   - Verdict descriptif identique (**`RÉFUTÉ`**) : $A(X, Z) = 0,1429$, $\rho_S = -0,5558$ ($p = 0,9587$), $E_{50\%} = 0,0000$. Fait notable : dans cette partition sans recouvrement, **l'ancienneté moyenne des concepts $A_{\text{âge}, k}$ atteint une aire sous la courbe de `0,8571`** — les sous-domaines les plus anciens de notre corpus sont aussi les plus mathématisés.
3. **Analyse `(c)` — Réintroduction des `21` révisions post-2024 d'identifiants $\le 2024$ ($K_{\text{élig}} = 14$)** :
   - Verdict descriptif identique (**`RÉFUTÉ`**) : l'élargissement à `14` sous-domaines éligibles accentue même le rejet ($A(X, Z) = 0,1020$, $\rho_S = -0,6484$, $p = 0,9941$).
4. **Analyse `(d)` — Décomposition par composante individuelle ($S_1$ à $S_5$)** :
   - Aucune des cinq familles lexicales ne produit de corrélation positive avec $Y_k^{\text{taux}}$ (`q` de Benjamini-Hochberg $= 0,9888$ partout) : $S_1$ (correctifs ad hoc : $\rho_S = -0,3909$, $A = 0,2667$), $S_2$ (dégradations de transfert : $\rho_S = -0,4679$, $A = 0,3667$), $S_3$ (contradictions empiriques : $\rho_S = -0,6886$, $A = 0,0833$), $S_4$ (fragilité et échecs d'échelle : $\rho_S = -0,4875$, $A = 0,2667$), $S_5$ (entropie terminologique : $\rho_S = -0,0364$, $A = 0,4500$ — seule composante neutre).
5. **Analyse `(e)` — Regroupements dyadiques inter-axes (`55` paires, procédure partielle de Mantel)** :
   - `14` des `55` paires d'axes présentent une émergence positive de synthèses formelles conjointes en `2025–2026` ($Z_{k\ell}^{\text{pont}} = 1$, notamment `AXE_05 + AXE_10` combinant suroptimisation de récompense et tromperie stratégique, et `AXE_10 + AXE_17` combinant tromperie stratégique et transfert hors domaine, toutes deux à co-occurrence amont nulle). Toutefois, la tension conjointe amont $X_{k\ell}$ ne les prédit pas : $\rho_{S,\text{partiel}} = -0,4405$ ($p_{\text{Mantel}} = 0,9945$), $A(X_{\text{paires}}, Z^{\text{pont}}) = 0,1672$ contre `0,4965` pour le produit des volumes.
6. **Analyse `(f)` — Permutation au niveau des `410` articles aval** :
   - En permutant directement les étiquettes $\text{Percee}(d')$ sur les articles tout en conservant intacte la matrice de recouvrement multi-axes, $p = 0,9578$ (très proche de `0,9790`), confirmant que le multi-rattachement ne fausse pas l'inférence.

### 4.2 Audit de symétrie (`R4`) et inspection qualitative des articles extrêmes

Le déclencheur négatif de l'audit de symétrie ($A(X, Z) \le 0,50$ et $\rho_S \le 0,00$) a été activé automatiquement (`declenche_negatif_ou_nul = true`) :
1. **Vérification de non-dégénérescence** : les extracteurs fonctionnent réellement sur les textes extraits (`561` occurrences de marqueurs de tension dans les `92` articles amont ; moyennes non nulles sur les cinq composantes $S_1\dots S_5$ et les trois composantes $F_1\dots F_3$). Le terme individuel le plus fréquent (`obfuscation`, `28,52 %` des occurrences brutes amont, concentré dans l'article de contournement d'activations `arxiv:2412.09565` d'empreinte `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9`) reste très en deçà du seuil d'alerte de `70 %` et est borné par l'écrêtage à `+5` écarts types de la seule composante $S_4$.
2. **Stabilité par omission unitaire d'un sous-domaine** : le retrait successif de chacun des `11` sous-domaines maintient $\rho_S$ dans `[-0,7576 ; -0,5030]` et $A(X, Z)$ dans `[0,1200 ; 0,3200]`. Même en retirant simultanément par la pensée `AXE_16` ou `AXE_17`, la pente demeure négative.
3. **Inspection des articles en tête de classement (`resultats-retrodiction-rang1-v1.json`, lignes 681–998)** :
   - En amont ($\le 2024$), les articles à score $T(d)$ maximal sont d'authentiques études de vulnérabilités et de frictions empiriques — par exemple `bailey-2025-obfuscated-activations-2412.09565.pdf` (`T = +1,075`, activant `AXE_02`, `AXE_06`, `AXE_08`) et `zeng-2024-beear-2406.17092.pdf` (`T = +0,783`, activant `AXE_05`, `AXE_08`), ainsi que des travaux fondateurs d'apprentissage adverse et d'optimisation robuste (`Wang-2019`, `sinha-namkoong-duchi-2018`) qui n'activent aucun des `18` lexiques spécialisés des grands modèles récents.
   - En aval (`2025–2026`), les articles à score $R(d')$ maximal sont dominés par des formalisations de **théorie des jeux de Stackelberg appliquée à l'alignement et aux attaques** (`2602.16984v1.pdf` `R = +4,052`, `theoretical-game-attacks-compositional-skills-2026-2605.01034.pdf` `R = +2,800`, `learning-structured-stackelberg-2025-2504.09006.pdf` `R = +2,710`, `sgpo-stackelberg-self-annotation-2025-2502.18099.pdf` `R = +2,353`, `stackelberg-games-alignment-preference-models-2026-2610.15008.pdf` `R = +2,273`) et par **l'audit séquentiel par martingales** (`2611.26592v1.pdf` `R = +1,944`). Or ces percées formelles proviennent d'une **importation d'outillage mathématique externe** (théorie des jeux à meneur-suiveur, martingales de test) dans les axes `AXE_05`, `AXE_10` et `AXE_16`, et non d'une continuation linéaire des articles les plus riches en plaintes lexicales d'heuristiques (`AXE_02`, `AXE_08`).

---

## 5. Conclusions méthodologiques et implications directes pour le programme (`C3`)

1. **Abandon immédiat des détecteurs purement lexicaux d'épicycles pour orienter l'organisme d'idéation** : l'épreuve tranche sans ambiguïté contre l'hypothèse qu'un repérage par expressions régulières de plaintes empiriques (`ad-hoc`, `brittle`, `fails to generalize`, `contradicts prior`) suffise à localiser les futures formalisations. Ce détecteur mesure le **degré d'empirisme rhétorique** d'une sous-communauté, lequel est structurellement anti-corrélé à sa propension à publier des théorèmes ($\rho_S = -0,6273$).
2. **Trois verrous identifiés à lever avant toute relance du chantier des signaux précurseurs (`C3`)** :
   - **Verrou de sélection du corpus** : le fonds local `docs/sources/pdf/` ayant été constitué par recherches thématiques ciblées en `2025–2026` (`410` articles aval contre `92` amont), plusieurs axes cruciaux (`sondes linéaires`, `chaîne de pensée`, `pilotage d'activations`, `désapprentissage`) manquent de leur base historique `2022–2024`. Toute évaluation rétrodictive future de `C3` devra opérer sur un **échantillon stratifié complet de l'archive ouverte `arXiv`** par année (`2021–2024` contre `2025–2026`) et non sur un dossier de travail constitué a posteriori.
   - **Verrou de représentation du signal amont** : une anomalie féconde en contrôle boîte blanche (par exemple la confusion entre identité du modèle et mensonge dans les sondes linéaires, ou l'échec du moniteur face au sabotage diffus) ne s'exprime pas par une surdensité de mots comme `workaround` ou `paradox`, mais par des **résultats quantitatifs mutuellement incompatibles entre deux articles partageant la même cible expérimentale** (homomorphisme frustré au sens de `IDE-2026-11-23-030` signal 2).
   - **Verrou de définition de la percée aval** : en alignement et en interprétabilité mécaniste, une percée majeure prend souvent la forme d'une **scission expérimentale d'un faux amalgame** (démonstration empirique d'une variable confondante ou d'un protocole de contrôle inédit) sans théorème numéroté ni équilibre de Stackelberg. La variable cible aval doit donc combiner la reconnaissance d'invariants conceptuels nouveaux et la normalisation intra-axe (différence première sur cohorte équilibrée) plutôt que la densité statique d'énoncés mathématiques.
