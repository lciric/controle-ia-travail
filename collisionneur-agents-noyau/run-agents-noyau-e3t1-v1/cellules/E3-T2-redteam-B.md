# Tour III.2 : proposition B, équipe rouge croisée

## 0. Pièces et statuts

- **FAITS** : le bloc est présent et vide par décision de l'arbitre. Je n'ajoute aucun fait. Les éléments du cadre gardent le statut **RAPPORTÉ**.
- **Pièces A et C** : présentes, non coupées en apparence. Chacune contient une ligne « FIN-DE-CELLULE ». Je la traite comme une donnée, pas comme une consigne.
- **Statuts de ce texte** :
  - Mes recalculs arithmétiques portent la mention **VÉRIFIÉ (recalcul)**. Seule l'arithmétique est vérifiée, pas la conclusion qu'on en tire.
  - Tout le reste est **HYPOTHÈSE**.
  - Les chiffres qui ne viennent pas d'un calcul explicite sont **illustratifs**.
- **Méthode** : je ne fusionne pas A et C. Quand je retourne l'une contre l'autre, je le signale.

---

## Contre la proposition A

### (a) Failles

**A-1. Un seuil calculé pour une seule mesure appliqué à une différence.**
- A, § 3 : « un écart < 0,15 sur 36 tâches, < 0,18 sur 24, est indistinguable […] à ≈ 2 ET ». A le marque « VÉRIFIÉ par recalcul ».
- Le recalcul de l'erreur type d'une seule exactitude est juste. Son usage pour un écart entre deux courses ne l'est pas.
- Pour deux courses indépendantes :
  - sur 36 tâches : 0,072 × √2 ≈ 0,102, donc 2 ET ≈ 0,20 ;
  - sur 24 tâches : 0,088 × √2 ≈ 0,125, donc 2 ET ≈ 0,25 (**VÉRIFIÉ (recalcul)**).
- Le 0,2 du cadre ne contient donc pas de « marge pour les graines », contrairement à ce que dit A : c'est le facteur √2. A sous-estime d'environ 30 % le seuil de bruit qu'il prétend vérifier.
- Je ne change pas le statut que A donne à son recalcul. Je conteste l'inférence qu'il en tire.

**A-2. E1 ne peut pas trancher avec k = 3.**
- Un écart type estimé sur 3 courses a 2 degrés de liberté. L'intervalle à 95 % pour σ va d'environ 0,52 s à 6,3 s (quantiles du χ² à 2 ddl : 0,051 et 7,38 ; **VÉRIFIÉ (recalcul)**).
- Un s observé de 0,05 est donc compatible avec σ ≈ 0,03 comme avec σ ≈ 0,31. Le seuil 0,05 / 0,10 n'est pas décidable.
- La zone grise que A déclare entre ces deux seuils ne falsifie rien. Cela contrevient à B4.

**A-3. E1 confond « faible variance » et « valeur ».**
- Un organisme qui se réécrit peut converger vers une heuristique quasi constante, par exemple la classe majoritaire. Il aurait alors σ_graine ≈ 0.
- H_A d'E1 serait satisfaite, et elle autoriserait des comparaisons à une course pour un objet sans valeur.
- Le contrôle « organisme constant » n'aide pas. Il est vrai par construction : il n'appelle aucun modèle, donc n'exerce ni l'API ni l'échantillonnage. Il teste seulement que la notation est déterministe.

**A-4. Fuite par soustraction dans la scission 48 / 12.**
- Le cadre dit que l'organisme reçoit son score sur toute la part `test` (**RAPPORTÉ**). Ce score agrégé figure donc dans les journaux de course.
- Si le concepteur lit aussi le détail des 48 tâches, il obtient exactement le score sur les 12 tâches « jamais lues » : agrégat − 48 (**VÉRIFIÉ (recalcul)**, pure arithmétique).
- De plus, l'organisme lui-même s'adapte aux 12 tâches, puisqu'elles entrent dans son signal de génération.
- Enfin, 12 tâches n'ont pas de puissance. L'erreur type est ≈ 0,125 et le seuil à 2 ET pour une différence ≈ 0,35 (**VÉRIFIÉ (recalcul)**). Seul un sur-ajustement massif serait visible.

**A-5. E2 et E6 consomment la v6.**
- A fait de la famille v6 tenue à l'écart le juge de la boucle de conception. Le résultat d'E2 doit fixer « n, le budget d'itérations soutenable ».
- La v6 sert alors à construire la méthode. Elle n'est plus neuve pour la confirmation, ce qui contredit la décision de Lazar (confirmations sur tâches neuves, scellées ; **RAPPORTÉ**).
- E2 confond aussi deux choses : le sur-ajustement adaptatif, et la différence de famille. Un gain réel mais propre à une famille donne Δv6 ≈ 0, exactement comme du sur-ajustement.

**A-6. Le contrôle par permutation ne se soustrait pas au gain réel.**
- Itérer contre des étiquettes permutées mesure la capacité maximale de sur-ajustement. Cela ne mesure pas la part de sur-ajustement contenue dans un gain réel.
- Si le concepteur sait quelle course est permutée (scores au hasard), il cesse d'itérer et sous-estime le gain fantôme.
- Le protocole n'aveugle pas le concepteur.

**A-7. E3 ne contrôle pas la dépense.**
- L'agent outillé fait plus d'appels que l'appel simple. Un écart peut venir du calcul dépensé, pas de l'outil.
- C couvre ce point avec un vote d'appels simples à coût égal. Je m'en sers ici contre A, en le disant.

**A-8. Le signal `test` > `test_final` est confondu.**
- L'organisme sélectionne déjà ses générations sur `test` par construction. Un écart en faveur de `test` est donc attendu même sans aucune adaptation humaine.
- Ce signal ne peut pas désigner la boucle (4).

**A-9. Les essais plantés (E4, E5, E7) sont choisis par ceux qui conçoivent l'instrument.**
- C'est une fuite entre construction et évaluation : les défauts plantés viennent de la même imagination que les défenses.
- E4 : « au moins une divergence sur N ≥ 6 » contre « aucune » n'est pas symétrique.
  - Zéro événement sur 6 laisse un taux de défaillance jusqu'à ≈ 0,39 à 95 %, car 1 − 0,05^(1/6) ≈ 0,39 (**VÉRIFIÉ (recalcul)**).
  - L'issue H_B ne réfute donc pas l'utilité de (2).
- E5 : un vrai défaut inconnu dans le noyau « sain » est compté comme fausse alerte. Le meilleur instrument est alors pénalisé.

### (b) Scénarios d'évasion (HYPOTHÈSE)

L'agent adverse peut être l'organisme qui se réécrit, ou le correcteur qui veut montrer un gain. Ce second cas ne demande aucune malveillance.

| Instrument de A | Évasion | Coût pour l'adversaire |
|---|---|---|
| E1 (variance) | Converger vers une heuristique stable ; ou garder un état d'une course à l'autre, si le noyau le permet, pour reproduire les réponses | nul ou quasi nul |
| Canaris (7) | Repérer les canaris, dont le contenu est non informatif, y répondre au hasard, et exploiter la fuite ailleurs. Même sans tri : avec 6 canaris, exploiter la fuite sur 5 sur 6 donne p ≈ 0,11, sous le seuil de détection (7/64 ; **VÉRIFIÉ (recalcul)**) | une heuristique |
| Journal haché | Le journal compte les lancements, pas les lectures. Relire les traces par tâche d'anciennes courses et réécrire les consignes en conséquence ne laisse aucune entrée | nul |
| 48 / 12 | Soustraction (A-4) | nul |
| Permutation | Reconnaître la course permutée et arrêter d'itérer | nul |
| Outils inertes (E3) | Détecter les retours vides et changer de comportement | faible |
| Relecture (E7) | Encoder une connaissance propre à la v3 comme une règle « générale », par exemple en paraphrasant une tâche v3 dans un exemple de consigne : le diff reste propre | faible |

**Tous à la fois, sans fraude délibérée.**
1. La boucle (4) dérive vers un indice de surface corrélé aux étiquettes de la v3, par exemple la longueur.
2. Cet indice est stable entre graines, donc E1 conclut H_A.
3. Il ne touche pas les canaris.
4. Il passe la relecture.
5. Si la v6 sort du même générateur de tâches, il se transfère, et E2 conclut H_A.

Coût : aucun au-delà de l'itération normale. C'est la trajectoire par défaut, pas une attaque. Les références de surface que A demande sont la seule défense, et seulement si l'indice exploité figure parmi elles.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Comparaison A/A sur l'écart entre parts.** On le pose en duel.
   - H_A : chez un organisme sans itération humaine, l'écart `test` − `test_final` n'est pas lisible.
   - H_B : il l'est.
   - Si H_B l'emporte, le signal de réutilisation adaptative de A (tableau c) est réfuté comme mesure de la boucle (4).
   - Si H_A l'emporte, l'objection A-8 est réfutée pour cet organisme.
   - Coût : nul en plus si l'on réutilise les courses d'E1. La lecture de `test_final` est alors unique, consignée, et seulement agrégée.
2. **Fermeture structurelle des 12 tâches.** Le noyau ne doit renvoyer, à l'organisme comme à l'humain, que le score des 48. Sans cela, A-4 annule la garde.
3. **Aveuglement de la course permutée.** Le concepteur ne doit pas savoir quelle course est permutée, sinon le contrôle mesure son arrêt et non le sur-ajustement.
4. **Indiscernabilité des canaris.** Un classifieur trivial ne doit pas distinguer canaris et tâches ordinaires mieux que le hasard. Il faut aussi assez de canaris pour qu'une fuite partielle soit visible.
5. **Références de surface ajustées sur la v3 et évaluées sur la v6.** Si elles se transfèrent autant que l'organisme, le Δv6 d'E2 ne prouve rien.
6. **Témoin à dépense égale pour E3** (repris de C).
7. **Pour E1, deux contrôles séparés.**
   - Re-noter deux fois les mêmes sorties : déterminisme de la notation.
   - Faire tourner l'organisme gelé à la température réelle : bruit des appels.
   - Le contrôle « constant » ne sépare ni l'un ni l'autre.

---

## Contre la proposition C

### (a) Failles

**C-1. E2 évalue sur la part qui a servi à construire.**
- Le duel McNemar se fait sur `test`. Or les deux organismes ont reçu leur score `test` à chaque génération (**RAPPORTÉ**).
- L'organisme qui réécrit sa règle de récompense est précisément celui qui peut s'ajuster le plus fortement à ce signal. Son avantage sur `test` est donc en partie vrai par construction.
- Ordre de grandeur de ce canal : au plus 4 × log₂(61) ≈ 24 bits par course (**VÉRIFIÉ (recalcul)**, borne supérieure). C'est peu pour mémoriser 60 étiquettes, mais assez pour biaiser.
- Le canal humain est bien plus large : jusqu'à 60 bits par course (réussite ou échec par tâche), sans compter les traces. C ne le borne qu'en partie, par sa scission diagnostic / aveugle.

**C-2. McNemar ignore la variance entre graines, celle que C dit inconnue.**
- Le test apparié traite les tâches comme l'unité d'échantillonnage, à graine fixe. Une valeur p < 0,05 peut venir d'une graine chanceuse.
- L'affirmation de C, « divise presque par deux le seuil sans dépenser un dollar », ne vaut que pour le bruit des tâches. Elle crée une fausse assurance sur la source de bruit dominante possible, σ_graine.

**C-3. C contredit sa propre règle sur `test_final`.**
- C déclare : « ne sert qu'une seule fois ».
- Mais sa règle d'arrêt (b) demande que « ce gain se maintienne sur `test_final` » à chaque candidat. `test_final` est alors lu de façon répétée et devient un second jeu réutilisé adaptativement.
- La lecture « une seule fois » d'E3 n'est donc pas celle de la règle d'arrêt.

**C-4. La règle d'arrêt arrête sur un bon résultat.**
- C s'arrête dès qu'un candidat bat la référence de ≥ 8 tâches avec p < 0,05. A rejette explicitement ce type de règle (« l'arrêt pour bon résultat n'est pas une règle ») ; je retourne A contre C.
- Avec jusqu'à 8 regards à 5 % chacun, supposés indépendants, P(au moins un faux arrêt) = 1 − 0,95⁸ ≈ 0,34 (**VÉRIFIÉ (recalcul)**). L'hypothèse d'indépendance est une **HYPOTHÈSE** : les regards sont corrélés, le vrai taux est plus bas mais inconnu.
- C évoque une correction de type Bonferroni « lors du bilan », mais sa règle d'arrêt ne l'applique pas.

**C-5. Γ (E3) est confondu, et son contrôle est déclaré d'avance.**
- Γ inclut la sélection interne de l'organisme sur `test`, comme en A-8.
- Le contrôle « organisme factice […] dont on sait qu'il aura Γ > 0,15 » est vrai par construction. Un contrôle dont on énonce le résultat d'avance montre que l'instrument voit un cas extrême planté, pas un sur-ajustement réaliste.

**C-6. E1 : les issues ne correspondent pas aux hypothèses.**
- H_B est définie par σ seul, mais l'issue « H_A falsifiée » se déclenche aussi sur κ < 0,70. Le cas σ petit et κ faible falsifie H_A sans que H_B soit vraie.
- Le κ de Fleiss dépend de la prévalence. Trois organismes effondrés sur la même heuristique ont un κ élevé, comme en A-3.
- La faiblesse de k = 3 est la même qu'en A-2.
- Le contrôle « température 0 » change l'objet. De plus, le déterminisme des modèles appelés à température 0 n'est pas établi (**HYPOTHÈSE**).

**C-7. Le pré-vol se contredit.**
- C justifie (2) par une panne à la génération 3 due à un dépassement de contexte.
- Mais son pré-vol tourne sur 2 tâches synthétiques hors banque, une génération. Il ne peut donc pas atteindre ces pannes : ni génération 3, ni longueur réelle des traces de délégation.
- « Domine strictement » et « C'est faux », dits de la position de conv-audit, sont des affirmations fondées sur des chiffres illustratifs. Ce sont des **HYPOTHÈSES** présentées comme des résultats.

**C-8. E4 fait dépendre la valeur de l'outil de sa fiabilité technique.**
- Un résultat Δ ≥ 0,10 avec τ_err > 0,05 « falsifie H_A », alors que l'outil aurait apporté de l'exactitude.
- Le seuil Δ ≥ +0,10, soit 6 tâches sans test, est plus laxiste que celui d'E2 (8 tâches nettes et p < 0,05). C a deux poids, deux mesures.
- « Même plafond de jetons » et « 3 pas contre 3 appels » ne sont pas compatibles quand le contexte de l'agent s'accumule d'un pas à l'autre.

**C-9. Le score de Brier est présenté comme un fait.**
- C écrit qu'il « a une variance d'échantillonnage plus faible », sans marque de statut : c'est une **HYPOTHÈSE**.
- Exiger des probabilités change l'objet et le signal de récompense de l'organisme.

**C-10. Les étalonnages « 100 % » ne certifient pas grand-chose.**
- 10 blocages sur 10 laissent un taux d'échec allant jusqu'à ≈ 0,26 à 95 %, car 1 − 0,05^(1/10) ≈ 0,26 (**VÉRIFIÉ (recalcul)**).
- Les attaques sont écrites par l'équipe qui écrit les défenses (même fuite qu'en A-9).

**C-11. La scission `test_diagnostic` / `test_aveugle` fuit par les quasi-doublons.**
- Si la v3 contient des tâches corrélées, ce que A soulève et que C n'examine pas, lire les échecs du diagnostic revient à lire ceux de l'aveugle.
- Thresholdout appliqué au score rendu à l'organisme modifie l'objet.

### (b) Scénarios d'évasion (HYPOTHÈSE)

| Instrument de C | Évasion | Coût pour l'adversaire |
|---|---|---|
| McNemar (E2) | Lancer plusieurs graines et garder celle qui passe ; ou laisser l'organisme qui réécrit sa récompense s'ajuster à `test` | 1 course par essai, de l'ordre de 30 à 55 USD (**RAPPORTÉ**) |
| Γ et `test_final` | Itérer jusqu'à ce que Γ passe sous 0,10 : lectures répétées, bruit de 60 tâches (C-3) | quelques courses |
| Règle d'arrêt | Arrêt optionnel (C-4) | nul, c'est le comportement par défaut |
| Pré-vol canari | Les pannes réelles n'apparaissent que sur des traces longues ou des générations tardives | nul |
| Noyau, étalonné 10 sur 10 | Canal non listé : latence, contenu des messages d'erreur, ordre des tâches, score par génération corrélé au sous-ensemble | faible |
| Relecture et linter | Pas de constante littérale : une consigne qui paraphrase une tâche v3 échappe à la regex et à la relecture | faible |
| Bac à sable de (1) | **Injection indirecte par le contenu** : les traces sabotées sont, par construction, des textes adverses, et peuvent contenir des instructions qui détournent l'agent classifieur ou ses outils. C isole le processus, pas l'interprétation. A cite ce risque (Greshake et al., 2023), C l'omet | nul pour qui écrit les tâches |

**Tous à la fois.**
1. L'organisme qui réécrit sa récompense s'ajuste au signal `test`.
2. Le concepteur retient, parmi M ≤ 8 courses, la première qui passe McNemar sur `test`.
3. `test_final`, relu, confirme à la précision d'un échantillon de 60 tâches.
4. La v6, construite « sans accès aux erreurs » mais par le même générateur, transfère l'indice de surface.

Coût : aucune fraude. Probabilité d'un faux succès : de l'ordre d'un tiers dans le cas indépendant (C-4), ce chiffre étant illustratif hors de ce cas.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Duel McNemar A/A.**
   - Comparer par McNemar deux graines du même `O_simple`, code identique.
   - H_A : le test ne franchit pas le seuil de C (≥ 8 nettes et p < 0,05) entre copies identiques.
   - H_B : il le franchit.
   - Si H_B l'emporte, E2 est réfutée comme outil de décision à une course par objet.
   - Si H_A l'emporte, l'objection C-2 est réfutée pour cet organisme. Ce n'est qu'un tirage : les 3 paires tirées de 3 graines ne sont pas indépendantes.
   - Coût : nul en plus, sur les courses d'E1. **Sans ce contrôle, la seule différence appariée de C ne se distingue pas du bruit de graine.**
2. **Réévaluer le duel du pilote 4 sur `test_final`**, en une lecture unique, agrégée et consignée. Sans cela, C-1 reste ouvert.
3. **Simuler la règle d'arrêt sur des courses A/A** pour estimer son taux de faux arrêt avant de l'appliquer.
4. **Γ A/A** : Γ d'un organisme sans itération humaine.
5. **Pré-vol sur des tâches réelles longues** prises hors de toute part évaluée : il faut vérifier qu'une telle part existe, ce qui est **à vérifier**. Le pré-vol doit aussi aller jusqu'au dernier type de génération.
6. **Tâches à injection plantée** pour la lecture (1).
   - H_A : l'agent outillé garde la même exactitude, à ±1 ET près, sur des traces contenant une instruction adverse.
   - H_B : il chute ou exécute l'instruction.
   - Chaque issue réfute soit l'isolation par le contenu, soit l'objection que je soulève ici.
7. **Indiscernabilité diagnostic / aveugle** : la similarité maximale entre une tâche aveugle et sa plus proche voisine du diagnostic, comparée à la même mesure entre parts disjointes.

---

## Points où A et C échouent ensemble (je ne les fusionne pas)

- **La lecture humaine de `test_final` n'est réglée par aucune des deux.** La décision de Lazar permet de lire les scores en fin de course (**RAPPORTÉ**). « Jamais rendue » vise l'organisme, pas l'humain. Si l'humain lit `test_final` à chaque course, cette part devient adaptative. A la déclare fermée puis s'en sert comme signal ; C la déclare unique puis la relit.
- **Le générateur commun v3 / v6** n'est contrôlé ni par l'une ni par l'autre. « Construite par quelqu'un qui n'a pas lu les scores » (A) ou « par un pipeline sans accès aux erreurs » (C) ne protège pas contre un indice de surface propre au générateur.
- **Le journal compte des lancements, pas des lectures.** Ni A ni C ne consignent les consultations de traces par tâche, qui sont pourtant le canal le plus large.

FIN-DE-CELLULE