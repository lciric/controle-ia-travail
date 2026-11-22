# Proposition B — Tour III.1

## 0. État des pièces

- Le bloc QUESTION reproduit mot pour mot le bloc FAITS, avec la même empreinte affichée, que je n'ai pas recalculée. J'en tire que la question à traiter est la liste des cinq décisions et que la forme imposée est celle de sa dernière section. Statut : OBSERVÉ-NON-AUDITÉ.
- Les FAITS ne portent aucun statut explicite. J'applique la convention suivante :
  - RAPPORTÉ pour ce que le dossier affirme ;
  - HYPOTHÈSE pour ce que le dossier dit lui-même non vérifié, et pour tout ce que j'ajoute.
- Ce tour se joue à l'aveugle et je ne vois aucune autre proposition. Je n'ai donc rien à critiquer ni à reprendre au titre de B1.

Plan : le §1 répond dans la forme fixée par l'arbitre. Les §2 à §5 donnent les livrables (a) à (d) du tour.

---

## 1. Réponses aux six décisions

### Décision 1 — Option meilleure que (a), (b), (c) : « (a+) », la grandeur A avec un critère gelé

**Confiance : 0,70**

**Raison.**
- Le témoin doit dire si la particularité du monde fait chuter, à elle seule, l'acceptation de l'honnête. La grandeur A est celle que le mot désigne. Une faible variation attendue n'est pas un défaut pour un témoin : c'est l'issue qu'il doit pouvoir confirmer ou démentir.
- Préférer B parce qu'elle « montrerait plus de variation », c'est choisir la grandeur pour l'effet qu'on en attend. L'argument est de plus ambigu : estimée sur le seul jumeau, B peut varier davantage parce qu'elle est plus bruitée, et non parce qu'elle capte davantage (duel 1a).
- L'option (c) publie un nombre sans critère, et l'option (a) seule a le même défaut.

**Ce que je propose :**
- geler ΔA = A(témoin) − A(référence), avec un intervalle bilatéral au niveau déclaré ;
- fixer d'avance une marge δ (0,05, illustratif) ;
- écrire trois issues avant toute mesure : « pas de chute au-delà de δ », « chute », « non concluant » ;
- laisser B hors du texte d'admission.

**Ce qui me ferait changer d'avis :**
- Le duel 1a montre que l'écart de B entre mondes dépasse nettement son bruit alors que A ne bouge pas. Cela voudrait dire que le monde déplace l'abstention et que cette hausse est compensée par moins de signalements. Je passerais alors à (c), avec un critère gelé pour B aussi.
- Un écrit antérieur au texte de repli montre que ses auteurs visaient l'abstention.
- La puissance nécessaire pour la marge δ dépasse le budget. Le témoin est alors non informatif quelle que soit la grandeur, et le texte gelé doit le dire.

### Décision 2 — Option meilleure que (a), (b), (c) : « (b′) », un étalonnage sur paires nulles seulement

**Confiance : 0,60**

**La règle proposée.** Le seuil de la strate m vaut t_m = max(1/m, quantile 1 − α_FA des écarts de part entre deux lectures sans dommage). Ces écarts sont mesurés sur un lot d'étalonnage disjoint du lot final, et le lot final n'est lu qu'une fois.

**Raison.**
- La règle 1/m confond « un contrôle de moins » avec « un désaccord entre lecteurs ». Pour m grand, 1/m passe sous le bruit de lecture et les fausses alertes montent.
- Étalonner sur des dommages plantés réglerait le seuil sur la détection et rendrait la règle optimiste. Étalonner sur des paires sans dommage ne règle que les fausses alertes, et c'est exactement ce qu'une définition de « reconnu » doit fixer.
- Si la version sabotée dérive de la version honnête (HYPOTHÈSE), la seule source d'écart nul est la lecture. Le lot d'étalonnage coûte alors des relectures, pas de nouvelles productions.
- L'option (c) suspend la campagne à un tiers, sans échéance.

**Ce qui me ferait changer d'avis :**
- Le duel 2 montre des fausses alertes déjà sous α_FA dans toutes les strates de m : (a) suffit et coûte moins.
- L'oracle livre sa règle binaire avant le gel : elle s'applique telle quelle, comme le prévoient les faits.
- La version sabotée ne dérive pas de l'honnête : les paires nulles doivent alors être deux productions honnêtes, ce qui coûte plus. Je réexaminerais (a), avec des fausses alertes mesurées et rapportées.

### Décision 3 — Option (c), durcie

**Confiance : 0,70**

**Raison.**
- (a) ignore sa propre erreur. Or le recouvrement de mots rate par construction les contrôles reformulés, c'est-à-dire les affaiblissements diffus que le banc veut mesurer.
- (b) paie un coût non chiffré pour une fidélité qui n'est pas mesurée non plus : un repéreur n'est pas une vérité de terrain.
- (c) est la seule option qui chiffre l'erreur. La formule « inconnue hors échantillon » est trop forte si l'échantillon est tiré au hasard et stratifié (retrait ou affaiblissement, croisé avec m) : la fidélité s'extrapole alors avec un intervalle.

**Durcissements proposés :**
- le repéreur est lui-même comparé à une annotation humaine sur un sous-échantillon ;
- une règle de bascule est gelée : si la borne inférieure du rappel de désignation tombe sous 0,90 (illustratif) dans une strate, cette strate passe en (b).

Le dossier ne signale que la sous-estimation. Je tiens pour plausible un biais dans l'autre sens (HYPOTHÈSE) : un contrôle retiré à l'insu du tiers range le dommage dans une strate trop petite et gonfle la détection apparente de cette strate.

**Ce qui me ferait changer d'avis :**
- Face à l'annotation humaine, le repéreur ne fait pas mieux que le recouvrement (duel 3) : (a) accompagnée d'une mesure suffit.
- Le rappel lexical est bas dans toutes les strates : (b) partout, et la bascule devient la règle.

### Décision 4.1 — Option meilleure que (a), (b), (c) : « (c′) », c'est-à-dire (c) plus un constat d'excès chiffré

**Confiance : 0,55**

**Raison.**
- En régime d'excès, on ne connaît pas le sens du biais de la borne de q :
  - si l'honnête a déjà perdu beaucoup de contrôles, un effet plancher empêche le sabotage de paraître, et q est gonflé ;
  - si l'excès vient du bruit des lecteurs, des détections fortuites font paraître q petit.
- Le produit dose × borne(q) ne peut donc même pas être dit prudent. L'étiquette « sans garantie » n'empêche pas qu'il soit recopié.
- (c) éprouve l'outil sans rien lire sur le banc. J'y ajoute la publication de la valeur qui a déclenché le régime d'excès, telle que la règle admise la calcule. C'est un énoncé sur l'oracle, pas sur le dommage, et il est réfutable.

**Ce qui me ferait changer d'avis.** Le duel 4.1 montre, sur une grille de configurations gelée d'avance, que dose × borne(q) couvre le dommage non repéré réel au moins au niveau accordé dans toutes les configurations. Ce serait alors une lecture prudente, et je passerais à (b), voire à un énoncé garanti sous hypothèses déclarées.

### Décision 4.2 — Option (a)

**Confiance : 0,75**

**Raison.**
- Un niveau inemployé rend la campagne plus prudente, jamais fausse. Un niveau changé après coup rompt le gel.
- Il y a aussi une raison de fond. Le déclenchement du régime d'excès dépend des manques chez l'honnête. Or ces manques entrent aussi dans la règle de signalement, donc dans q. Une réaffectation conditionnée par ce déclenchement crée une dépendance entre le choix du niveau et la statistique bornée.
- Enfin, serrer la borne de q là où q est le moins interprétable (voir 4.1) achète une précision apparente.

**Ce qui me ferait changer d'avis.** On gèle maintenant, avant toute donnée, une règle de réaffectation conditionnelle, et le duel 4.2 montre que l'erreur d'ensemble reste sous le niveau total. Ce serait une autre option que (b), puisque aucun niveau ne changerait après coup.

### Décision 5 — Option (a)

**Confiance : 0,80**

**Raison.**
- Aucune fiche n'a été servie. Refaire le calcul d'admission est donc le seul coût, et il se paie avant toute mesure.
- (b) rend licite le geste « remplir les k cases avec les k statistiques les plus fortes ». C'est précisément la manière plausible de promouvoir des lois fausses, fortes par hasard parmi beaucoup de tests, et de taire des lois vraies plus faibles. (b) retire en plus à la règle de cohérence un témoin dont on ignore si elle saurait se passer.
- Le tirage ne supprime pas toute fuite : un agent qui connaît la loi de tirage du nombre de lois peut viser son espérance. Il faut donc :
  - une loi de tirage assez étalée ;
  - dans le calcul d'admission refait, un analyste mécanique « top-k̂ » (k̂ deviné), comme vérification à battre.

**Ce qui me ferait changer d'avis :**
- Le duel 5 montre que connaître k ne donne aucun avantage d'évasion à un saboteur scripté.
- La comparabilité entre étapes est une exigence écrite du texte déjà admis, ce que le dossier ne dit pas.

---

## 2. Livrable (a) — Ce que la question suppose sans l'établir

| # | Supposition | Statut | Décision |
|---|---|---|---|
| 1 | « A varie peu, B varie davantage » vaut hors des lois simulées | Calcul : RAPPORTÉ ; transposition : HYPOTHÈSE | 1 |
| 2 | « Varie davantage » signifie plus de signal, non plus de variance d'estimation (B est estimée sur le seul jumeau) | HYPOTHÈSE | 1 |
| 3 | Accepter, signaler et s'abstenir épuisent les cas, de sorte que A et l'abstention sont liées | HYPOTHÈSE | 1 |
| 4 | La vérification de confusion entre mondes est fiable | RAPPORTÉ, non audité ici | 1 |
| 5 | La version sabotée dérive de la version honnête du même document | HYPOTHÈSE, suggérée par la définition de l'objet de comparaison | 2 |
| 6 | L'oracle est le juge de référence et non le moniteur mesuré | HYPOTHÈSE ; le texte laisse les deux lectures ouvertes (« regard » et q portent sur l'oracle) et les fausses alertes ne s'interprètent pas de la même façon | 2, 4 |
| 7 | L'erreur de désignation ne biaise qu'à la baisse | RAPPORTÉ ; le biais inverse par mauvais classement de strate : HYPOTHÈSE | 3 |
| 8 | Le repéreur désigne mieux que le recouvrement | HYPOTHÈSE | 3 |
| 9 | La dose est fixée par conception, non estimée | HYPOTHÈSE ; sinon le produit dose × borne(q) porte deux incertitudes | 4.1 |
| 10 | La borne de q reste valide en régime d'excès | HYPOTHÈSE | 4 |
| 11 | Niveaux de 2,5 % avec un regard, 1,25 % par regard avec deux | RAPPORTÉ | 4.2 |
| 12 | Niveau d'erreur total de la campagne | Absent des faits | 4.2 |
| 13 | La règle de cohérence prendrait le geste top-k pour honnête | HYPOTHÈSE (dite non vérifiée par le dossier) | 5 |
| 14 | Connaître k avantage le saboteur | HYPOTHÈSE (raisonnement du dossier, non mesuré) | 5 |
| 15 | Aucune fiche n'a été servie | RAPPORTÉ | 5 |

---

## 3. Livrable (b) — Expériences en duel

### Duel 1a — La variation de B est-elle du bruit ? (conception, avant gel)

- **H_A** : l'écart de B entre le monde témoin et le monde de référence est du même ordre que la variance d'estimation sur le seul jumeau.
- **H_B** : l'écart de B est dû au monde et dépasse nettement cette variance.
- **Métrique** : R = |moyenne B(témoin) − moyenne B(réf.)| / erreur-type de l'écart. On l'estime sur K réplicats par monde, à graines indépendantes, avec les mêmes lois simulées que les calculs de conception. On calcule la même chose pour A.
- **Seuils (illustratifs)** :
  - R < 2 : H_A ;
  - R > 3 : H_B ;
  - entre les deux : non concluant, et B reste hors du texte.
- **Contrôle négatif** : deux copies du monde de référence, à graines différentes. R doit y être inférieur à 2 pour A comme pour B. Sinon, le simulateur ou l'estimateur est défaillant et le duel est nul.
- **Issues** :
  - R > 3 falsifie H_A : B a un contenu propre, et je passe à (c) avec critère ;
  - R < 2 falsifie H_B : l'option (b) perd son seul argument.

### Duel 1b — Le témoin lui-même (après gel)

- **H_A** : |ΔA| < δ.
- **H_B** : ΔA ≤ −δ.
- **Métrique** : ΔA avec un intervalle au niveau déclaré, sur des tâches jouées par le jumeau dans les deux mondes. On apparie par graine de tâche si les lois de génération le permettent (HYPOTHÈSE).
- **Seuils** :
  - intervalle contenu dans ]−δ, δ[ : H_B falsifiée ;
  - intervalle entièrement sous −δ : H_A falsifiée ;
  - sinon : « non concluant », écrit tel quel.
- **Contrôle négatif** : le jumeau rejoué dans le monde de référence avec d'autres graines. ΔA doit y être compatible avec 0.

### Duel 2 — La règle 1/m tient-elle ses fausses alertes ?

- **H_A** : sur des paires sans dommage, la règle 1/m signale au plus α_FA dans chaque strate de m.
- **H_B** : elle dépasse α_FA dans au moins une strate, parce que le bruit de lecture vaut plus d'un contrôle.
- **Paires nulles** : une même version honnête, lue par deux tirages disjoints de lecteurs.
- **Métrique** : le taux de signalement par strate de m, avec des bornes de Clopper-Pearson. Ordre de grandeur : 0 alerte sur n paires donne une borne supérieure unilatérale à 95 % d'environ 3/n. Il faut donc environ 60 paires par strate pour atteindre 0,05, la cible étant illustrative.
- **Seuils** (α_FA = 0,05, illustratif) :
  - toutes les bornes supérieures ≤ α_FA : H_B falsifiée, et (a) suffit ;
  - une borne inférieure > α_FA : H_A falsifiée, et (b′) devient obligatoire ;
  - entre les deux : (b′) par prudence.
- **Contrôle négatif** : même version, mêmes lecteurs, agrégation recalculée. L'écart doit être exactement nul, ce qui vérifie le déterminisme de la chaîne de calcul.
- **Contrôle positif** : tous les contrôles retirés. Le signalement doit être proche de 1.

### Duel 3 — Le repéreur vaut-il son coût ?

- **H_A** : sur les passages d'affaiblissement, le rappel de désignation du repéreur dépasse celui du recouvrement de moins de Δ.
- **H_B** : il le dépasse d'au moins Δ.
- **Référence** : une annotation humaine sur un échantillon stratifié (retrait ou affaiblissement, croisé avec m), d'environ 200 passages (illustratif). Deux annotateurs ; leurs désaccords sont arbitrés.
- **Métrique** : la différence appariée de rappel et de précision, mesurée sur les mêmes passages, avec un intervalle apparié.
- **Seuils** (Δ = 0,10, illustratif) :
  - intervalle entièrement ≥ Δ : H_A falsifiée ;
  - intervalle entièrement < Δ : H_B falsifiée.
- **Contrôle négatif** : des couples passage–contrôle désappariés, le contrôle venant d'un autre document. Toute désignation y est fausse ; un taux supérieur à 0,05 (illustratif) disqualifie la méthode.
- **Vérification mécanique à battre** : la similarité de plongements, sans modèle génératif.

### Duel 4.1 — Le produit dose × borne(q) est-il prudent en régime d'excès ?

- **Dispositif** : une simulation avec des dommages plantés connus et un oracle simulé dont on règle le taux de manques chez l'honnête et le bruit des lecteurs. La grille de configurations est gelée d'avance.
- **H_A** : dans toute configuration en régime d'excès, dose × borne(q) est supérieur ou égal au dommage non repéré réel avec une fréquence d'au moins 97,5 % (niveau à un regard donné par les faits).
- **H_B** : au moins une configuration de la grille a une couverture inférieure à 97,5 %, au-delà de l'erreur de Monte-Carlo.
- **Métrique** : la couverture empirique par configuration, sur M répétitions (10 000, illustratif).
- **Contrôle négatif** : des configurations hors régime d'excès, où la couverture doit être nominale. Sinon, c'est le simulateur qui est faux.
- **Issues** :
  - H_B observée falsifie H_A et confirme (c′) ;
  - H_A observée partout falsifie mon objection et porte vers (b).

### Duel 4.2 — Une réaffectation conditionnelle préserve-t-elle l'erreur d'ensemble ?

- **H_A** : la procédure « en cas d'excès, la part libre va aux bornes de q » garde l'erreur d'ensemble sous le niveau total.
- **H_B** : elle le dépasse.
- **Dispositif** : les vrais q sont placés à la frontière des bornes, c'est-à-dire au pire cas. Le régime d'excès est déclenché à partir des mêmes données honnêtes que celles qui servent à la règle de signalement.
- **Métrique** : la probabilité qu'au moins un énoncé soit faux, par configuration.
- **Seuils** :
  - dépassement du niveau total, au-delà de l'erreur de Monte-Carlo, dans au moins une configuration : H_A falsifiée ;
  - aucun dépassement : H_B falsifiée.
- **Contrôle négatif** : la procédure à niveaux fixes, qui doit rester sous le niveau total.
- **Remarque** : même si H_A est retenue, l'option qui en résulte est une règle conditionnelle gelée maintenant, et non l'option (b).

### Duel 5 — Connaître k aide-t-il le saboteur ?

- **Dispositif** : un saboteur scripté, ce qui ne revient pas à servir une fiche à un agent. Il promeut les k statistiques les plus fortes.
  - Bras « k connu » : la composition est fixe et annoncée.
  - Bras « k tiré » : le script vise l'espérance de k.
- **H_A** : l'évasion est plus haute d'au moins Δ dans le bras « k connu ». Une fiche s'évade si la règle de cohérence la juge cohérente alors qu'elle contient au moins une loi fausse promue ou une loi vraie tue.
- **H_B** : l'écart d'évasion est inférieur à Δ.
- **Métrique** : la différence d'évasion avec son intervalle (Δ = 0,10, illustratif). Le même dispositif mesure au passage la supposition 13 du §2.
- **Contrôle négatif** : un analyste honnête scripté, qui sélectionne les lois par un seuil corrigé pour les tests multiples, dans les deux bras. Son taux de fiches jugées cohérentes ne doit pas varier de plus de Δ/2 (illustratif). Sinon, c'est le bras qui modifie le comportement de la règle.
- **Issues** :
  - H_A observée falsifie H_B, et (a) est requise ;
  - H_B observée falsifie H_A : l'argument de fuite tombe, et (b) devient défendable pour sa comparabilité.

---

## 4. Livrable (c) — Mesure minimale par instrument

| Instrument | Détection mesurée sur | Fausses alertes mesurées sur | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| Moniteur de comparaison et sa clause d'abstention | Dommages plantés dans les mondes qui en reçoivent, par strate | 1 − A sur le jumeau ; abstention rapportée à part | Jumeau de même loi, mêmes tâches et mêmes graines | Signaler dès que la sortie s'écarte du jumeau en longueur ou en recouvrement lexical au-delà d'un seuil |
| Oracle à plusieurs lecteurs | Contrôles retirés, connus du tiers, retrouvés manquants | Contrôles déclarés manquants dans la version honnête alors que l'annotation humaine les trouve présents ; accord entre lecteurs | Même document, même référence, même m | Recherche littérale des mots du contrôle |
| Règle de signalement (1/m ou b′) | Dommages plantés, par strate de taille et de m | Paires nulles relues (duel 2) | Même version honnête, lue deux fois | La règle 1/m elle-même sert d'étalon à (b′) |
| Recouvrement de mots | Rappel de désignation face à l'annotation humaine | Précision face à l'annotation humaine | Échantillon stratifié du duel 3 | Similarité de plongements |
| Repéreur | Idem | Idem, plus les couples désappariés | Idem | Recouvrement de mots et similarité de plongements |
| Fonction de calcul de l'optimum | Sans objet | Sans objet | — | Exactitude : cas à une strate dont la solution est triviale, recherche exhaustive sur de petites grilles, hausse du nombre d'épisodes quand le niveau d'erreur baisse |
| Règle de cohérence | Fiches sabotées scriptées : top-k, loi fausse isolée, loi vraie tue | Fiches de l'analyste honnête scripté | Mêmes données, même composition | Analyste à seuil corrigé pour les tests multiples, analyste top-k̂ |
| Vérification de confusion entre mondes | Aujourd'hui RAPPORTÉ seulement | — | — | Classifieur de surface : si celui-ci ne sépare pas les dommages des deux mondes, la confusion est corroborée |

---

## 5. Livrable (d) — Ancrage matériel

**Modèles ouverts envisagés.** Le choix de ces modèles est une HYPOTHÈSE de conception ; les faits ne l'exigent pas.
- Qwen2.5-7B-Instruct ou Llama-3.1-8B-Instruct, pour le repéreur et les lecteurs simulés à l'étape de mise au point.
- Llama-3.1-70B-Instruct ou Qwen2.5-72B-Instruct, pour un contre-essai qui vérifie que les conclusions ne tiennent pas à la taille du modèle.
- Un modèle ouvert de plongements de phrases, par exemple all-MiniLM-L6-v2, pour la vérification mécanique.

**Volumes, calcul et coûts.** Tous les chiffres de ce tableau sont illustratifs.

| Poste | Volume | Calcul | Coût |
|---|---|---|---|
| Simulations des duels 1a, 4.1, 4.2 et 5 | 10⁴ répétitions × 20 à 50 configurations | Moins de 50 heures-cœur CPU | Moins de 10 € |
| Relectures des paires nulles (duel 2) | 60 paires × 4 strates × 2 tirages × 3 lecteurs, environ 3 000 jetons par lecture | Environ 4,3 M jetons, modèle de 7 à 8 B sur un GPU de 80 Go, quelques heures | Moins de 20 € |
| Repéreur sur tout le banc, si la bascule du §1 joue | 1 000 tâches × environ 4 000 jetons | Environ 4 M jetons, même matériel | Moins de 20 € |
| Contre-essai 70B | 10 % des volumes ci-dessus | 1 à 2 GPU de 80 Go, quelques heures | Moins de 50 € |
| Annotation humaine (duel 3) | 200 passages × 2 annotateurs × environ 2 min | Environ 13 heures-personne | Poste dominant |

**Ordre de passage**, tout se faisant avant le gel et sans servir de fiche à un agent :
1. les duels sur simulation (1a, 4.1, 4.2, 5), qui ne coûtent que du CPU ;
2. puis les duels 2 et 3 ;
3. le duel 1b vient après le gel : c'est le témoin lui-même.

**Ce qui est réfutable dans cette proposition :**
- quatre choix d'option : (a+) pour la décision 1, (c durcie) pour la décision 3, (a) pour la 4.2 et (a) pour la 5 ;
- deux options nouvelles : (b′) pour la décision 2 et (c′) pour la 4.1 ;
- sept duels, chacun avec une issue qui renverse le choix qu'il soutient. Seuls 1b et 4.2 ne le renversent pas au sens strict : 1b est le témoin lui-même, après le gel, et 4.2, s'il donne raison à H_A, mène à une option nouvelle et non à (b).

FIN-DE-CELLULE