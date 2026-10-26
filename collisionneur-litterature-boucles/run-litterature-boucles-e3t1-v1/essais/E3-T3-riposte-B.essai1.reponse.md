# Proposition B · Tour III.3 · riposte

**Pièces reçues**
- **FAITS** : le bloc est présent mais explicitement vide. Je n'en tire rien.
- **QUESTION** : présente, non coupée.
- **E3-T1-conception-B, E3-T2-redteam-A, E3-T2-redteam-C** : présentes, terminées par FIN-DE-CELLULE, non visiblement coupées.
- Je n'ai pas vérifié les empreintes sha256.
- Je ne réponds qu'aux sections « Contre la proposition B ».

**Conventions**
- Le cadre de l'arbitre est **RAPPORTÉ**.
- Mes dispositifs sont des **HYPOTHÈSES**.
- « calcul » désigne un raisonnement explicite à partir de chiffres RAPPORTÉS ou illustratifs.
- Je ne cite aucune référence nouvelle. Celles de III.1 restent RAPPORTÉES, à vérifier.
- Je m'appuie sur trois éléments des équipes rouges et je le signale à chaque fois :
  - le retournement de signe proposé par A ;
  - le double contrôle ajout/retrait proposé par C ;
  - l'argument de C contre l'E3 de A (« la règle exacte gagne par construction sur des scores purs »), que je retourne contre mon propre E2.

---

## (a) Attaque par attaque

### Équipe rouge A

| ID | Verdict | Raison ou test |
|---|---|---|
| **F-B1** (contrôle permuté d'E2) | **Acceptée** | Calcul : permuter les scores entre tâches à l'intérieur d'une génération conserve la somme, donc l'écart agrégé G3 − G0. Mon contrôle condamnait l'analyste exact. Je le remplace par le retournement de signe aléatoire au sein de chaque paire (proposé par A) et par de vraies paires A/A tirées d'E1. |
| **F-B2** (E2 mesure la lecture du code) | **Acceptée, transformée** | E2 est scindé. E2a juge les scores et le texte de l'hypothèse, sans différence de code. La lecture du code revient au correcteur, évalué à part. Sur scores purs, la règle exacte est optimale par construction (argument de C contre A). E2a devient donc un test de **non-infériorité** du trio, pas un test de supériorité. |
| **F-B3** (le trio recopie la règle) | **Acceptée** | Le trio n'a accès ni aux p-valeurs ni à la sortie de la règle. Le bras « trio + sortie de la règle » est renvoyé au départage V2, hors E2a. |
| **F-B4** (plants de réglage = plants d'évaluation) | **Acceptée** | Partition scellée par empreinte. Les plants d'évaluation sont produits par une personne ou un processus qui n'a pas réglé les consignes. La règle vaut pour E2a, le filtre anti-copie et chaque ligne du § 7. |
| **F-B5** (P5 contredit l'auto-réécriture) | **Acceptée, transformée** | Fusionnée avec C-a3 dans E6 (§ b). L'unité testée devient la **condition de course** choisie avant la course. L'attribution à une différence n'est tentée que si celle-ci est séparable, et toujours par ajout sur G0 **et** retrait sur G3. |
| **F-B6** (seuil d'E1 sans conséquence, budget sans borne) | **Acceptée** | Le seuil est désormais relié au nombre de graines et au budget est plafonné (E1'). **Je corrige aussi une incohérence de III.1** : « borne supérieure ≤ 0,05 falsifie H_B » ne falsifiait pas σ_g > 0,035. La borne correcte est 0,035. |
| **F-B7** (E3 indécise) | **Acceptée sur le fond, chiffre rejeté** | `test` et la part tenue à l'écart sont deux ensembles de tâches distincts. Leurs écarts appariés sont indépendants et s'ajoutent en quadrature : √2 × 0,058 ≈ 0,082 (calcul, q = 0,2 illustratif), et non 2 × 0,058 ≈ 0,12. La conclusion tient : un seuil de 0,1 reste hors de portée (E3'). |
| **F-B8** (E4 dépend d'E1) | **Acceptée** | k devient une fonction de σ_plan, la valeur issue d'E1 (E4'). Le total de 50 courses de III.1 est retiré. |
| **F-B9** (les canaris réduisent la banque) | **Acceptée, rendue sans objet** | Le coût serait de √(60/50) ≈ 1,10 sur l'erreur type (calcul). Comme les canaris sont abandonnés (voir C-a1), la question disparaît. |
| **F-B10** (W0 n'est pas une ablation) | **Acceptée** | Le canal général d'appels doit être identique entre les bras : même budget, même interface. On consigne s'il expose des log-probabilités. E4' mesure la valeur ajoutée du canal dédié, rien de plus. |
| **F-B11** (règle réglée par des lecteurs de scores) | **Acceptée** | La règle est scellée par empreinte avant toute lecture de confirmation. Les versions de conception sont journalisées. |
| **Év-A1** (extraction des étiquettes par le score) | **Acceptée, transformée** | Le calcul de A tient : environ 1 bit par lecture, environ 20 courses pour 60 étiquettes. Le rationnement R2 réduit le canal sans le fermer. Ce canal est désormais mesuré par E5'-b. |
| **Év-A2** (canaris détectables par contradiction avec le contenu) | **Acceptée** | Des étiquettes tirées au hasard contredisent le contenu sur les items nets. Les canaris sont abandonnés. Le contrôle de détectabilité est transposé à E5'. |
| **Év-A3** (placebo détecté puis ignoré) | **Acceptée, transformée** | Audit d'indiscernabilité préalable, puis contraste placebo contre W0 pour détecter un « nocebo » (E4'). |
| **Év-A4** (paraphrase contre le filtre anti-copie) | **Acceptée sur la mesure ; gravité discutée** | La primitive ne rend aucune étiquette. Un contournement fournit la mesure d'un modèle sur un item de test, pas sa vérité. C'est une violation de règle à mesurer, avec un jeu rouge de transpositions isomorphes. Ce n'est pas en soi une fuite de vérité. Le danger réel vient de la combinaison avec le canal de score (E5'-b). |
| **Év-A5** (plafond contourné par le budget général) | **Acceptée** | Même correction que F-B10. |
| **Év-A6** (toutes les évasions à la fois) | **Acceptée** | Conséquence assumée : mes instruments **détectent**, ils n'empêchent pas. Les verrous préventifs restent le mot de Lazar à chaque relance et P4 (le correcteur ne voit que des traces). |
| **Ctrl-A1 à A5** | **Acceptés** | (1) Les A/A proviennent des rejouées d'E1, sans sélection sur l'écart. (2) La détectabilité est transposée à E5'. (3) L'indiscernibilité est vérifiée en E4'. (4) La règle est scellée. (5) Partition, comme F-B4. |

### Équipe rouge C

| ID | Verdict | Raison ou test |
|---|---|---|
| **C-a1** (canaris sans puissance) | **Acceptée** | Recalcul : P(≥ 9/10 \| p = 0,65) ≈ 0,086. Avec 10 canaris, une puissance de 80 % exige p ≈ 0,92, donc une fuite d'environ 84 % des items (calcul). E5 est remplacé par E5'. |
| **C-a2** (N_d fixé dans le calcul de puissance) | **Acceptée** | Mon « il faut l'unanimité » était tautologique une fois N_d posé. Je vérifie le cas de C : 13 contre 4 donne p ≈ 0,049 bilatéral, ce qui échoue au seuil de Holm. Correction ci-dessous : la puissance est **plus faible** que je ne l'écrivais. |
| **C-a3** (épistasie) | **Acceptée** | J'adopte le double contrôle de C (ajout sur G0, retrait sur G3) dans E6. |
| **C-a4** (d'où viennent les étiquettes des sondes) | **Acceptée** | Trou réel de III.1. W2 est suspendu tant que la source n'est pas spécifiée : P-org (textes étiquetés par l'organisme, au risque de tautologie) ou P-ext (corpus externe, indépendant de la banque, passé au filtre anti-copie). |
| **C-a5** (trois bras avec 30 courses) | **Acceptée** | Calcul : avec 3 contrastes sous Holm, le facteur passe de 2,8 à 2,394 + 0,842 ≈ 3,24. L'erreur type requise est ≤ 0,031, d'où k ≥ (0,14/0,031)² ≈ 21 par bras (σ illustratif). Le dessin devient étagé (E4'). |
| **C-b1** (règle de routage numérique contre l'audit du correcteur) | **Acceptée** | La recherche de sous-chaînes ne suffit pas. On ajoute un test **comportemental** : part des items de `test` dont la réponse change, comparée à des textes hors banque appariés. On ajoute aussi E5'-a. Pour viser un item, le correcteur doit d'abord avoir accès à ses caractéristiques. Une telle règle suppose donc une fuite en amont, que E5'-a détecte. |
| **C-b2** (textes ancres contre le placebo permuté) | **Acceptée** | Pour W1 (log-probabilités déterministes), un placebo indiscernable est probablement impossible (HYPOTHÈSE). W1 n'est donc comparé qu'à W0. |
| **C-b3** (famille de Holm réduite par l'analyste) | **Acceptée** | La famille est définie mécaniquement : toutes les hypothèses du registre, empreintes prises avant les scores. Une hypothèse ajoutée après coup est exploratoire et ne peut pas être conservée. L'erreur « famille réduite » est ajoutée aux plants du contre-lecteur. |
| **C-b4** (fuite ciblée sur 15 items incertains) | **Acceptée, chiffre corrigé** | P(≥ 9/10 \| p = 0,625) ≈ 0,064 (calcul), et non 4,8 %. La conclusion est inchangée : non-détection. Le gain de +0,125 est correct. Cette attaque fixe aussi où placer les items de E5'. |
| **C-b5** (évasion totale) | **Acceptée** | Même réponse qu'à Év-A6. |
| **C-c1** (indiscernabilité ; placebo appel par appel) | **Acceptée** | Trou de spécification : une permutation exige un lot. L'audit est intégré à E4'. |
| **C-c2** (contrôle d'épistasie) | **Acceptée** | Intégré à E6. |
| **C-c3** (sélection interne et inflation des faux positifs) | **Rejetée sur le fond, transformée en test (E7)** | La primitive ne voit aucune vérité de `test`, et G3 n'est pas choisie parmi des candidats notés sur `test`. Une sélection interne ne peut donc pas sélectionner sur le bruit de `test`. Mais cette réfutation dépend du filtre anti-copie, que je n'ai pas mesuré. D'où E7. |

### Puissance corrigée (C-a2), calcul

L'erreur type de l'écart apparié vaut environ √(q/n), où q est la discordance (légère surestimation, puisque var = q − Δ²). L'écart minimal détectable à 80 % de puissance vaut environ (z_{α/2} + 0,842) × √(q/n).

| q (illustratif) | n | α = 0,05 | α = 0,01 (Holm, 5 hypothèses) |
|---|---|---|---|
| 0,15 | 60 | 0,14 | 0,17 |
| 0,30 | 60 | 0,20 | 0,24 |

**Conclusion révisée (HYPOTHÈSE)** : sur course unique et petite banque, aucun effet de moins de 0,15 à 0,25 environ n'est éliminable ni conservable. Cela est compatible avec le « < 0,2 dans le bruit » de l'arbitre (RAPPORTÉ) : l'appariement ne gagne que si q est petit.

---

## (b) Expériences corrigées

Seuils et effectifs illustratifs, sauf mention « calcul ».

### Garde R : règle scellée (condition préalable, pas une expérience)

- La règle porte sur : le SESOI, α, la définition mécanique de la famille (registre avec empreintes), les verdicts soutenue / réfutée / indécise et la répartition de α entre rondes.
- Chaque version est journalisée.
- La version utilisée en confirmation est scellée avant toute lecture.

### E1' : variance entre graines et coût

- **H_A** : σ_g ≤ 0,035. L'erreur type n'est alors gonflée que de 12 % au plus (√(0,07² + 0,035²) ≈ 0,078, calcul de A), et une course par condition suffit.
- **H_B** : σ_g > 0,035.
- **Dessin** : 8 rejouées à chacun de deux niveaux :
  - (a) G0 figé ;
  - (b) course entière.
- On mesure aussi le **coût par course** à partir du journal du noyau.
- **Contrôle négatif** : réponses mises en cache, l'écart-type doit être nul.
- **Intervalle** : avec 7 degrés de liberté, l'intervalle à 95 % de σ vaut environ [0,66 s ; 2,04 s] (calcul, khi-deux).
- **Falsification** :
  - H_B est falsifiée si 2,04 s ≤ 0,035, soit s ≤ 0,017 ;
  - H_A est falsifiée si 0,66 s > 0,035, soit s > 0,053.
- **Zone indécise, budget borné** : aucune graine de plus. On planifie avec σ_plan = 2,04 s (valeur prudente).
- **Conséquences** :
  - nombre de graines par condition : n = ⌈(σ_plan/0,035)²⌉ ;
  - k d'E4' est calculé à partir de σ_plan ;
  - les SESOI atteignables sont recalculés et soumis à Lazar avant toute autre course.
- Les rejouées du niveau (b) fournissent les **A/A réels** d'E2a.

### E2a : trio contre règle, jugement statistique seul

- **Entrées du trio** : scores par tâche et texte de l'hypothèse. Pas de différence de code, pas de p-valeurs ni de sortie de la règle.
- **Cas d'évaluation** (partition scellée, distincte des cas de réglage) :
  - A/A réels issus d'E1', sans sélection sur l'écart ;
  - effets plantés dans les vecteurs de scores, de +0,05 à +0,15 (zone ambiguë) et à −0,125 (calcul de III.1) ;
  - 40 cas au total (illustratif).
- **Contrôle négatif** (repris de A) : retournement de signe aléatoire au sein des paires. Le trio doit répondre « indécise » au taux de la règle.
- **H_A** : le taux d'erreurs du trio (fausses éliminations + fausses conservations) n'excède pas celui de la règle de plus d'une marge de 0,05 (non-infériorité).
- **H_B** : il l'excède.
- **Falsification** :
  - si la borne supérieure de la différence d'erreurs est < 0,05, H_B est falsifiée et V3 reste admissible sur le volet statistique ;
  - si la borne inférieure est > 0,05, H_A est falsifiée : V3 tombe, et seules V1 ou V2 (veto de la règle) restent.
- **Limite déclarée** : E2a ne mesure pas ce que les agents apportent en proposition ni en diagnostic. Cela relèverait d'un E2b, non dimensionné ici.

### E3' : sur-ajustement adaptatif, version honnête sur sa portée

- **Métrique** : (G3 − G0) sur `test`, moins (G3 − G0) sur une **part témoin prélevée**. Cette part n'est jamais utilisée pour la conception ni lue de façon répétée. Ce n'est pas `test_final`.
- **Erreur type** (calcul, q = 0,2 illustratif) :

| Parts de n tâches | Erreur type ≈ √2 × √(q/n) | Écart minimal détectable (80 %) |
|---|---|---|
| n = 60 | 0,082 | 0,23 |
| n = 96 | 0,065 | 0,18 |

- Le plancher dû à l'échantillonnage des tâches ne baisse pas quand on ajoute des courses sur les mêmes tâches. Seule la part due aux graines baisse en 1/√k.
- **H_A** : la double différence ≤ SESOI, avec SESOI égal à l'écart minimal détectable calculé, et non 0,1.
- **H_B** : elle est > SESOI.
- **Contrôles** :
  - négatif : score rendu aléatoire, même format. La pente doit être nulle ;
  - positif : les vérités de `test` sont données à l'organisme. L'effet doit être détecté, sinon la mesure est aveugle.
- **Falsification** :
  - un dépassement significatif, absent du contrôle négatif, falsifie H_A ;
  - l'équivalence à la marge, avec un contrôle positif qui détecte, falsifie H_B.
- **Portée déclarée** : E3' ne voit que le sur-ajustement **grossier**. E3' peut réutiliser les courses d'E4'.

### E4' : primitive, dessin étagé

- **Prérequis** :
  - canal général identique entre les bras ;
  - source des étiquettes des sondes spécifiée (P-org ou P-ext), sinon W2 n'est pas testé.
- **Étape 0, indiscernabilité** :
  - un classifieur à l'aveugle reçoit les séries de retours ;
  - un organisme témoin cherche à distinguer primitive réelle et placebo après n appels.
  - Pour W1, la discernabilité est attendue (déterministe, ancres), donc **pas de placebo W1**.
  - Pour W2, placebo = sonde entraînée sur étiquettes permutées. Elle n'est admise que si l'audit est au niveau du hasard.
- **Étape 1, W1 contre W0** :
  - k = ⌈(σ_diff/0,036)²⌉ paires, avec σ_diff ≥ √2 × σ_plan (calcul) ;
  - 15 paires si σ_diff = 0,14 (illustratif).
  - **H_A** : gain W1 > W0 sur la part témoin.
  - **H_B** : équivalence à 0,1.
  - La supériorité falsifie H_B ; l'équivalence falsifie H_A.
- **Étape 2**, seulement si W2 est spécifié et passe l'étape 0 : W2, placebo-W2, W0.
  - Trois contrastes sous Holm, environ 21 courses par bras, soit environ 63 (calcul, σ illustratif).
  - **Test de nocebo** : si placebo < W0 de façon significative, l'organisme réagit à l'instrument et l'étape est invalide.
- Les budgets sont des fonctions de σ_plan, présentées à Lazar avant engagement.

### E5' : étiquettes contrefactuelles (remplace les canaris)

- **Items** : m items de `test` où G0 est incertaine, choisis par une procédure scellée. C'est là qu'une fuite rapporte (attaque C-b4).
- **Détectabilité** : un agent qui dispose des items et de la vraie table doit désigner les items retournés au niveau du hasard. Sinon, on choisit d'autres items.
- **Dessin** : courses appariées L1 (étiquettes vraies) et L2 (étiquettes des m items retournées), tout le reste identique.
- **Métrique** : D = accord avec L1 dans la course L1, moins accord avec L1 dans la course L2, sur les m items.
- **Puissance** :
  - borne pessimiste : erreur type ≤ √(0,5/m)/√k. Le bruit vient des graines seules, les items étant fixes, donc il baisse avec k ;
  - avec m = 30 et k = 4 paires : 0,065. Une fuite d'environ 18 % des items est alors détectable à 80 % (calcul). Les canaris n'en détectaient qu'environ 84 %.

**E5'-a, fuite hors du canal de score.**
- Les m items sont exclus du score servi, qui est identique dans les deux courses.
- Seuls restent comme canaux possibles le correcteur, les fichiers et les journaux.
- **H_A** : D compatible avec 0.
- **H_B** : D > 0.
- **Contrôles** :
  - positif : correcteur à qui l'on donne les étiquettes ;
  - négatif : pas de correction.
- **Falsification** :
  - D significatif falsifie H_A ;
  - l'équivalence avec un contrôle positif qui détecte falsifie H_B pour les fuites dont la taille dépasse le seuil calculé.

**E5'-b, canal de score.**
- Les m items sont inclus dans le score servi.
- D mesure alors le flux total des étiquettes vers le code, extraction de A comprise. Ce flux n'est **pas séparable** de l'adaptation honnête au score. C'est ce qui est mesuré, en complément d'E3'.

**Coût** : ces courses sont des courses d'instrument, inutilisables pour la conception. Environ 8 par variante (illustratif).

### E6 : attribution et épistasie (double contrôle repris de C)

- Pour une différence Δ séparable :
  - A0 = S(G0 + Δ) − S(G0) ;
  - R3 = S(G3) − S(G3 − Δ).
- **Verdicts** :
  - les deux supérieurs au seuil : soutenue ;
  - les deux équivalents à 0 : réfutée ;
  - divergents : épistasie, **indécise**, aucune élimination.
- **H_A** : A0 ≈ R3 (effet additif).
- **H_B** : A0 ≠ R3.
- Chaque issue falsifie l'une des deux.
- Si Δ n'est pas séparable, seule la comparaison des conditions de course sur n graines (issu d'E1') est admise.

### E7 : sélection interne (priorité basse, après E4')

- **Dessin** : étiquettes de `test` aléatoires, sans signal ; sélection interne best-of-1 contre best-of-20 sur la primitive.
- **H_A** : le taux de « gains » G0/G3 significatifs est indépendant du budget de sélection interne.
- **H_B** : il croît avec ce budget.
- **Falsification** :
  - une croissance significative falsifie H_A et révèle un canal entre la primitive et `test` (filtre anti-copie défaillant) ;
  - l'équivalence falsifie H_B.

### Instruments corrigés

| Instrument | Correction |
|---|---|
| **Contre-lecteur** | Nouveaux plants « famille réduite » ; contrôle mécanique contre les empreintes du registre. |
| **Correcteur** | P4 (traces seulement) en prévention ; test comportemental (changements de réponses sur `test` contre textes appariés hors banque) ; E5'-a. |
| **Filtre anti-copie** | Jeu rouge de transpositions isomorphes produites par un modèle ; taux mesuré, aucun 0,95 supposé. |

### Budget en courses (illustratif sauf formule)

| Expérience | Courses |
|---|---|
| E1' | 16 |
| E2a | hors ligne |
| E3' | réutilise E4' |
| E4' étape 1 | 2k, avec k fonction de σ_plan |
| E4' étape 2 | environ 63 si σ_diff = 0,14 |
| E5' | environ 16 |
| E6 | 2 à 4 par hypothèse attribuée |
| E7 | environ 10 |

Le total n'est pas fixé tant qu'E1' n'a pas donné σ_plan et le coût par course.

---

## (c) Réponse à la question de l'arbitre (une page)

**Ce qui est établi, au sens restreint.** Aucun fait n'est VÉRIFIÉ dans cette cellule. Toute la littérature que j'ai citée reste RAPPORTÉE, à vérifier. Seuls découlent d'un calcul explicite sur les chiffres RAPPORTÉS par l'arbitre :

1. Sur course unique et 60 tâches, avec Holm sur 5 hypothèses, l'écart minimal détectable est d'environ 0,15 à 0,25 selon la discordance (illustrative). Éliminer ou conserver en dessous ne vaut rien.
2. Répéter les graines sur les mêmes tâches réduit le bruit des graines, pas l'échantillonnage des tâches. Le sur-ajustement adaptatif ne se mesure donc que s'il est grossier : écart minimal détectable d'environ 0,18 à 0,23 (calcul, q illustratif).
3. Dix canaris ne détectent qu'une fuite quasi totale, environ 84 % des items.
4. Un retour de score exact sur 60 tâches porte au plus environ 5,9 bits par lecture (calcul de A). Le canal de score suffit à extraire des étiquettes en une vingtaine de courses. Le verrou préventif est la décision humaine de relancer, non un instrument.
5. Permuter les scores entre tâches ne fournit pas de contrôle nul pour un écart agrégé.

**Ce qui n'est pas établi** :
- la variance entre graines et le coût d'une course ;
- l'existence d'un effet utile de la primitive ;
- le fait qu'un trio d'agents décide au moins aussi bien qu'une règle scellée ;
- l'absence de fuite par la correction ;
- la source d'étiquettes des sondes, qui reste à définir ;
- la granularité du score rendu (S14) et ce que voit le correcteur (S8) ;
- l'indiscernabilité d'un placebo ;
- la transposition à notre cas des boucles publiées. À ma connaissance (RAPPORTÉ, à vérifier), celles-ci reposent sur un évaluateur quasi déterministe, propriété que notre boucle extérieure n'a pas.

**Voies et ce qui les départage** :
- **Boucle extérieure** : V1 (la règle décide), V2 (veto de la règle) ou V3 (agents libres). E2a fait tomber V3 ou la laisse admissible. Il ne départage pas V1 et V2 ; cela demanderait E2b, non dimensionné.
- **Boucle intérieure** : W0, W1 ou W2, départagées par E4'. W2 reste en attente d'une source d'étiquettes.
- **Information rendue** : R1, R2 ou R3, à juger sur E5'-b et E3', en sachant qu'aucun rationnement ne ferme le canal (calcul de A).

**L'expérience à faire en premier : E1'** (16 courses, illustratif), plus son relevé de coût. Elle fixe à elle seule :
- le nombre de graines par condition ;
- k d'E4' ;
- les SESOI atteignables ;
- le prix de tout le reste.

Elle fournit aussi les A/A réels d'E2a. Ses deux issues falsifient quelque chose (s ≤ 0,017 ou s > 0,053), et la zone indécise a une règle de planification prudente, sans dépense supplémentaire.

**En parallèle, sans course** : scellement de la Garde R, E2a hors ligne, spécification de la source des sondes, audit d'indiscernabilité.

**Ce qui changerait cet ordre** : si le coût par course rend 16 courses inacceptables pour Lazar, E2a et la Garde R passent seules en tête, et toute élimination reste « indécise » par défaut.

FIN-DE-CELLULE