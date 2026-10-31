### Bloc 1 — Le tableau complet face aux trois écueils

Le pré-pilote comprend au minimum (illustratif) : 4 proposeurs, 2 juges figés, 10 cases, 4 témoins plantés par case (longueur comparable aux fiches, RAPPORTÉ fait 3), 2 doublons plantés et 2 instructions glissées plantées par case.

#### 1. Influence croisée
- **Convergence**
  - *Mécanisme* : Le proposeur $P_i$ écrit une entrée libre au tableau en passe 1 ; le noyau la sert en lecture à $P_j$ avant la passe 2 ; $P_j$ en réutilise les termes dans sa fiche de passe 2.
  - *Protocole* : Écriture au tableau uniquement après le dépôt des fiches de passe 1 ; lecture restreinte aux résumés caviardés (VÉRIFIÉ, fait 2) et tronqués à 300 caractères (illustratif).
  - *Mesure* : Distance moyenne de Jaccard sur les trigrammes de caractères entre fiches de passe 2 de proposeurs distincts d'une même case. Seuil : baisse de distance $< 10\%$ (illustratif) par rapport au contrôle négatif (même case sans tableau). Effectif : 10 cases (illustratif). Rien de planté.
  - *Conclusion* : **évité sous condition** (baisse de distance $< 10\%$ au pré-pilote).

- **Poids du plus prolifique**
  - *Mécanisme* : $P_i$ dépose un volume de texte ou un nombre d'entrées dominant au tableau ; ce volume sature le contexte servi en lecture à $P_j$ en passe 2 et oriente ses fiches.
  - *Protocole* : Quotas stricts appliqués par le noyau : au plus 5 entrées par proposeur, 300 caractères par entrée, 1 500 caractères par proposeur et 6 000 caractères au total (illustratifs, calqués sur la coupe à 1 500 caractères de `memoire.py`, VÉRIFIÉ fait 7). Anonymisation des entrées.
  - *Mesure* : Part maximale d'un seul proposeur dans le texte du tableau et dans les idées distinctes comptées en passe 2. Seuil : part $\le 1/N + 0,15$ pour $N=4$ proposeurs (illustratif) contre le contrôle négatif (sans tableau). Effectif : 10 cases (illustratif). Doublons plantés pour étalonner le décompte d'idées.
  - *Conclusion* : **évité sous condition** (part maximale $\le 0,40$ au pré-pilote).

- **Atteinte au juge**
  - *Mécanisme* : Le tableau est servi par erreur au juge, ou $P_j$ recopie un passage du tableau dans sa fiche de passe 2 ; le juge lit la fiche, ou un commentaire du tableau signale l'anomalie d'un témoin planté, le rendant reconnaissable.
  - *Protocole* : Séparation physique des flux (le juge ne reçoit que les fiches validées et les témoins, VÉRIFIÉ fait 2) ; exclusion des témoins de tout ce qui est servi au tableau (principe de `memoire.py` et `proposeur.py`, VÉRIFIÉ faits 7 et 8) ; filtre de recouvrement mettant en quarantaine toute fiche de passe 2 ayant un sous-mot commun de plus de 50 caractères (illustratif) avec une entrée du tableau d'un autre proposeur.
  - *Mesure* : (1) Atteinte directe : taux de fiches servies aux juges contenant la chaîne inerte plantée au tableau ou un recouvrement $> 50$ caractères (seuil : 0). (2) Reconnaissabilité : écart de score moyen des juges figés sur les 4 témoins plantés par case (longueur comparable, RAPPORTÉ fait 3), servis avec tableau contre sans tableau (contrôle négatif). Seuil : écart $< 0,2$ point sur l'échelle du juge (illustratif). Effectif : 10 cases, 40 témoins (illustratif).
  - *Conclusion* : **évité sous condition** (recouvrement nul et écart sur témoins $< 0,2$ au pré-pilote).

#### 2. Instructions glissées
- *Mécanisme* : $P_i$ écrit dans une entrée libre du tableau un segment qui agit comme consigne lorsqu'il est lu par $P_j$ en passe 2, altérant la fiche de $P_j$.
- *Protocole* : Balisage en données pures (comme le préambule du collisionneur, VÉRIFIÉ fait 12), garde lexicale et caviardage existants (VÉRIFIÉ, fait 2), retrait des lignes portant au moins cinq nombres ou le vocabulaire du noyau et coupe de taille (repris de `memoire.py`, VÉRIFIÉ fait 7), et filtre de forme rejetant toute entrée hors gabarit déclaratif.
- *Mesure* : Un tiers plante 2 instructions glissées par case dans le tableau, chacune dotée d'une chaîne inerte unique. Statistique : fréquence d'apparition de la chaîne inerte dans les fiches de passe 2 des autres proposeurs (prise). Seuil : $0\%$. Contrôle négatif : entrées du tableau portant uniquement la chaîne inerte sans l'instruction glissée. Effectif : 10 cases, 20 instructions plantées (illustratif).
- *Conclusion* : **évité sous condition** (taux de prise de $0\%$ au pré-pilote).

#### 3. Surcroît de code
- *Mécanisme* : Le tableau complet exige des chemins et gardes nouveaux rattachés aux flux : (1) écriture libre au tableau par $P_i$, (2) lecture du tableau complet par $P_j$, (3) quota de taille par entrée/proposeur/total (flux $P_i \to$ tableau), (4) filtre structurel anti-instructions (flux tableau $\to P_j$), (5) filtre de recouvrement tableau $\to$ fiche (flux $P_j \to$ juge).
- *Protocole* : Reprise telle quelle du validateur de gabarit, du caviardage, de la garde lexicale et de l'anonymisation du noyau (`ideation_v2.py`, VÉRIFIÉ fait 2), de l'exclusion des témoins et du filtre de nombres/longueur de `memoire.py` (VÉRIFIÉ, fait 7), et du refus hors bloc structuré de `proposeur.py` (VÉRIFIÉ, fait 8).
- *Mesure* : Par rapport au noyau (VÉRIFIÉ, fait 2) : 5 éléments nouveaux à contre-lire et sceller (les éléments 1 à 5 ci-dessus ; le tableau minimal de la décision n'exige que 2 éléments : extraction automatique des titres/résumés de passe 1 et injection en lecture en passe 2). Par rapport au tableau minimal : 3 éléments nouveaux (écriture libre, filtre structurel, filtre de recouvrement).
- *Conclusion* : **évité sous condition** (que le directeur accepte de contre-lire et sceller 3 éléments nouveaux par rapport au tableau minimal, soit 5 par rapport au noyau).

---

### Bloc 2 — Trois conceptions sur un même estimand

#### Opérationnalisation de l'estimand
- **Idées distinctes** : Deux lecteurs modèles indépendants (sessions neuves, hors proposeurs et hors juges) étiquettent chaque paire de fiches validées d'une case comme « même idée » ou non, selon la règle : même mécanisme proposé et même cible de test. Accord exigé : $\kappa$ de Cohen $\ge 0,70$ (illustratif) ; en cas de désaccord, un troisième lecteur tranche à la majorité. On construit le graphe des fiches liées par ces paires : le nombre d'idées distinctes est le nombre de composantes connexes $C$ de ce graphe (généralisant sans condition d'acyclicité la formule $V - E$ du fait 4, VÉRIFIÉ).
- **Diversité** : $1 - \overline{\text{Jaccard}}$ sur les trigrammes de caractères entre les fiches représentatives (la plus longue de chaque composante connexe).
- **Unité de dépense** : Dollar (ou 100 000 jetons, en sommant entrée et sortie au tarif des modèles, illustratif).
- **Qualité jugée égale** : La moyenne des notes des juges sur les fiches validées ne baisse pas de plus de $\Delta = 0,25$ écart-type (illustratif) par rapport au tableau minimal, les juges étant validés par un écart $< 0,2$ sur les témoins plantés. Ce verdict de juge sert à choisir la conception du partage d'information (A, B ou C). Sous l'HYPOTHÈSE que ce choix d'orchestration échappe à la règle de composition des proposeurs (VÉRIFIÉ, fait 13), la note du juge est recevable. Si cette hypothèse ne tient pas, la qualité jugée est retirée du critère de décision (rapportée pour simple information) et l'équivalence est exigée uniquement sur le taux de validation mécanique du noyau (gabarit et garde lexicale, VÉRIFIÉ fait 2) et sur la stabilité des juges face aux témoins plantés.

#### Comparaison des trois conceptions
- **(A) Tableau minimal** (RAPPORTÉ, fait 5) : Lecture seule en passe 2 des titres et résumés d'une ligne de la passe 1 (même case). Permet d'éviter les redites ; ne permet ni échange, ni idéation conjointe, ni attribution de rôles par les proposeurs. Coût : $\sim 2\,000$ jetons lus/case, $0$ écrit (illustratif) ; 2 éléments de code par rapport au noyau. Piège : résumé d'une ligne trop pauvre pour détecter un doublon formulé sous un autre titre.
- **(B) Tableau complet** (RAPPORTÉ, fait 6) : Lecture et écriture libres. Permet l'échange, la co-construction et l'auto-attribution de rôles. Coût : $\sim 25\,000$ jetons lus et $\sim 6\,000$ écrits/case (illustratif) ; 5 éléments de code. Pièges : les trois écueils du bloc 1.
- **(C) Tableau intermédiaire** : En passe 2, lecture des résumés d'une ligne ET de « pistes » structurées déposées en fin de passe 1. Règles d'écriture : chaque proposeur dépose au plus 3 pistes typées dans une liste fermée (`[EXTENSION, CONTRE-EXEMPLE, FUSION, RÔLE]`), ciblant l'identifiant anonymisé d'une fiche de passe 1, limitées à 200 caractères sans texte libre hors gabarit (principe de `proposeur.py`, VÉRIFIÉ fait 8). Permet l'échange ciblé, la combinaison d'idées et la prise de rôle, avec moins de canaux d'instructions glissées que B. Coût : $\sim 6\,000$ jetons lus et $\sim 1\,500$ écrits/case (illustratif) ; 3 éléments de code. Piège : rigidité du typage.

---

### Bloc 3 — Les rôles

Il faut assigner trois rôles fixes (Explorateur, Critique-Vérificateur, Recombinateur, inspiré des rôles de `memoire.py`, VÉRIFIÉ fait 7), attribués **par l'orchestrateur par permutation circulaire** entre les cases (jamais au choix des proposeurs sur le tableau, ce qui nécessiterait un canal d'écriture libre propice aux instructions glissées et à la dominance du premier déclarant).

- **Chemin de fuite vers le juge et prévention** : La consigne de rôle servie au proposeur peut induire des marqueurs lexicaux (« Voici une recombinaison… », « En critique de… ») ou une structure de fiche spécifique que le juge voit et note différemment. Pour l'empêcher : (1) le gabarit de fiche imposé par le noyau est strictement identique quel que soit le rôle (VÉRIFIÉ, fait 2) ; (2) la garde lexicale (VÉRIFIÉ, fait 2) est étendue pour mettre en quarantaine ou caviarder les termes nommant les rôles et les références explicites aux identifiants d'autres fiches avant envoi au juge.
- **Mesure de l'effet des rôles** : Conformément au fait 13 (VÉRIFIÉ), ce choix (« dans quel rôle ») ne se juge pas sur les notes des juges. L'effet se mesure sur le nombre d'idées distinctes $C$ (composantes connexes, VÉRIFIÉ fait 4), la diversité trigramme et la dépense en dollars, en comparant trois conditions : (1) rôles assignés avec consigne de conduite, (2) sans rôle, (3) **contrôle négatif** : étiquettes de rôle servies au proposeur sans aucune instruction de conduite. Les témoins plantés vérifient seulement que l'étalonnage du juge ne dérive pas entre conditions. Pour vérifier que le juge ne reconnaît pas le rôle : un classifieur linéaire entraîné sur les trigrammes des fiches servies au juge (ou un lecteur modèle aveugle) doit prédire le rôle avec une exactitude ne dépassant pas le hasard ($1/3 + 0,05$, illustratif). Que le couple (idées distinctes, diversité) par dollar tienne lieu de l'oracle du monde planté du fait 13 est HYPOTHÈSE.

---

### Livrable (a) — Ce que la question suppose sans que ce soit établi

1. **HYPOTHÈSE** : L'apparition des 12 paires de doublons à la course 1 s'explique par le fait que la passe 2 ne voit pas ce qui a été écrit en passe 1 (RAPPORTÉ comme non mis à l'épreuve, fait 3).
2. **HYPOTHÈSE** : Fournir aux proposeurs la liste des titres et résumés d'une ligne en passe 2 (tableau minimal) suffit à réduire le taux de doublons sans abaisser le nombre total de fiches validées.
3. **HYPOTHÈSE** : Des gardes mécaniques (caviardage, bornes de taille, listes blanches de champs) suffisent à bloquer l'effet d'instructions glissées dans un canal d'écriture libre sans détruire l'échange d'idées.
4. **HYPOTHÈSE** : Les témoins plantés v2, de longueur comparable aux fiches (RAPPORTÉ, fait 3), ne deviennent pas reconnaissables par les juges lorsque les proposeurs échangent sur un tableau partagé (les témoins étant exclus du tableau comme dans `memoire.py`, VÉRIFIÉ fait 7).
5. **HYPOTHÈSE** : Le choix entre les conceptions A, B et C du tableau porte sur le protocole de communication et non sur la composition des proposeurs, échappant ainsi à l'interdit d'utiliser le verdict des juges (VÉRIFIÉ, fait 13).
6. **HYPOTHÈSE** : En l'absence de monde planté pour les proposeurs dans la course d'idéation, le nombre d'idées distinctes (composantes connexes, VÉRIFIÉ fait 4) et la diversité lexicale par dollar tiennent lieu d'oracle au sens de la décision N-058 (VÉRIFIÉ, fait 13) pour évaluer l'attribution de rôles.
7. **HYPOTHÈSE** : L'échange entre proposeurs (conceptions B et C) ou la différenciation par rôles augmente le nombre d'idées distinctes par unité de dépense par rapport à des passes indépendantes ou au tableau minimal.

---

### Livrable (b) — Expériences décisives en duel H_A contre H_B

Dans les trois duels, l'unité d'analyse est la **case** ($K = 10$ cases appariées au pré-pilote, illustratif, chaque texte de départ étant couru sous les conditions comparées avec les mêmes proposeurs). La dépendance entre les fiches d'un même proposeur au sein d'une case est traitée en agrégeant d'abord la métrique au niveau de la case (un score par case et par condition) et en appliquant un test des rangs signés de Wilcoxon par paires sur les $K$ cases (ou par bootstrap par grappes au niveau du proposeur).

#### Duel 1 : Conception C (Tableau intermédiaire) contre Conception A (Tableau minimal)
- **$H_A$** : À qualité jugée non inférieure (perte moyenne de note des juges $< 0,25\sigma$), la conception C produit au moins $20\%$ (illustratif) d'idées distinctes par dollar de plus que la conception A.
- **$H_B$** : La conception C produit un gain d'idées distinctes par dollar $< 20\%$ par rapport à A, ou dégrade la qualité jugée de $\ge 0,25\sigma$.
- **Métrique et seuil** : Ratio $R = C_{\text{idées}} / \text{Coût}(\$)$ par case, et note moyenne des juges $Q$. Seuil de décision : médiane des différences $\Delta R / R_A \ge +0,20$ avec $p < 0,05$ (Wilcoxon sur 10 cases, illustratif) ET $\Delta Q > -0,25\sigma$.
- **Contrôle négatif** : Course sans aucun tableau (état de la course 1, RAPPORTÉ fait 3) et conception C où les pistes servies en passe 2 sont remplacées par des pistes vides (vérifie que l'effet vient du contenu des pistes et non de l'allongement de la consigne).
- **Falsification** : Une médiane de $\Delta R / R_A < +0,20$ ou $\Delta Q \le -0,25\sigma$ falsifie $H_A$ ; l'inverse falsifie $H_B$.

#### Duel 2 : Conception B (Tableau complet gardé) contre Conception C (Tableau intermédiaire)
- **$H_A$** : Le texte libre de la conception B augmente le nombre d'idées distinctes par dollar d'au moins $15\%$ (illustratif) par rapport à la conception C, tout en maintenant un taux de prise des instructions glissées plantées égal à $0\%$ et une baisse de diversité trigramme $< 10\%$.
- **$H_B$** : La conception B n'augmente pas le nombre d'idées distinctes par dollar d'au moins $15\%$ par rapport à C, ou subit une prise d'instruction glissée ($> 0\%$), ou perd $\ge 10\%$ de diversité.
- **Métrique et seuil** : Ratio $R = C_{\text{idées}} / \text{Coût}(\$)$, taux de présence de la chaîne inerte dans les fiches de passe 2 ($\tau_{\text{prise}}$), et diversité trigramme $D$. Seuil : $\Delta R / R_C \ge +0,15$ ($p < 0,05$), $\tau_{\text{prise}} = 0$ sur 20 instructions plantées (illustratif), et $\Delta D / D_C > -0,10$.
- **Contrôle négatif** : Conception B avec instructions plantées réduites à la seule chaîne inerte sans consigne (étalonne le taux de recopie fortuite du traceur).
- **Falsification** : $\Delta R / R_C < +0,15$, ou $\tau_{\text{prise}} > 0$, ou $\Delta D / D_C \le -0,10$ falsifie $H_A$ ; le respect simultané des trois seuils falsifie $H_B$.

#### Duel 3 : Rôles assignés avec consigne contre Étiquettes de rôle sans consigne
- **$H_A$** : Sous la conception retenue, assigner des rôles avec consigne de conduite augmente le produit $(\text{idées distinctes} \times \text{diversité}) / \text{Coût}(\$)$ d'au moins $15\%$ (illustratif) par rapport au contrôle négatif (étiquettes de rôle sans consigne), sans que le rôle soit reconnaissable dans la fiche servie au juge (exactitude de prédiction du rôle $\le 1/3 + 0,05$).
- **$H_B$** : Les rôles avec consigne n'apportent pas ce gain de $15\%$ par rapport aux étiquettes nues, ou laissent transparaître le rôle dans les fiches ($> 0,38$ d'exactitude).
- **Métrique et seuil** : Indice $I = (C_{\text{idées}} \times D) / \text{Coût}(\$)$ par case (conforme au fait 13, VÉRIFIÉ, sans utiliser la note du juge) et exactitude $A_{\text{rôle}}$ d'un classifieur trigramme sur les fiches anonymisées. Seuil : $\Delta I / I_{\text{étiquette}} \ge +0,15$ ($p < 0,05$) et $A_{\text{rôle}} \le 0,38$ (illustratif).
- **Contrôle négatif** : Étiquettes de rôle servies aux proposeurs sans aucune instruction de conduite (isole l'effet de la consigne de rôle de l'effet d'amorçage du mot), doublé d'une condition sans rôle du tout.
- **Falsification** : $\Delta I / I_{\text{étiquette}} < +0,15$ ou $A_{\text{rôle}} > 0,38$ falsifie $H_A$ ; l'inverse falsifie $H_B$.

---

### Livrable (c) — Mesure minimale de chaque instrument nommé

| Instrument | Cas honnêtes appariés | Vérification mécanique à battre (Base) | Taux de détection (Rappel) & Fausses alertes (TFA) exigés | Contrôle négatif |
|---|---|---|---|---|
| **1. Détecteur de doublons** (lecteurs indépendants + graphe des composantes) | 30 paires de fiches honnêtes d'idées distinctes sur une même case, comparées aux mêmes 30 fiches où l'une est réécrite par un tiers pour exprimer la même idée sous un vocabulaire disjoint (doublon planté, illustratif). | Recouvrement de trigrammes de caractères entre deux fiches (seuil fixé à Jaccard $> 0,25$, illustratif). | Détection $\ge 0,85$ et TFA $\le 0,05$ sur les paires appariées, en battant le rappel de la base d'au moins $+0,20$ à TFA égal (illustratif). | Paires de fiches issues de textes de départ différents (doivent donner $0\%$ de doublons détectés). |
| **2. Garde contre les instructions glissées** (filtre de structure, nombres/vocabulaire noyau fait 7, et gabarit) | 20 entrées de tableau honnêtes, comparées aux 20 mêmes entrées dans lesquelles un tiers a inséré une instruction glissée porteuse d'une chaîne inerte (sans que la garde connaisse la chaîne inerte, illustratif). | Garde lexicale existante du noyau (`ideation_v2.py`, VÉRIFIÉ fait 2) combinée à une simple borne de taille (300 caractères). | En amont : détection $\ge 0,95$ et TFA $\le 0,05$ sur les entrées honnêtes. En aval (prise, mesurée par la recherche exacte de la chaîne inerte dans les fiches de passe 2) : réduction de la prise à $0\%$ contre la prise observée avec la base seule. | Entrées honnêtes où un tiers a inséré uniquement la chaîne inerte sans instruction glissée (vérifie que la garde ne déclenche pas sur le traceur et que la prise mesure bien l'instruction). |
| **3. Séparation d'avec le juge** (isolation du tableau, filtre de recouvrement $>50$ car., exclusion des témoins) | 20 fiches honnêtes servies aux juges, comparées aux 20 mêmes fiches où un extrait du tableau (de 60 caractères, porteur de la chaîne inerte) a été inséré par un tiers ; et 20 témoins plantés servis aux juges avec et sans tableau (illustratif). | Recherche exacte de la chaîne inerte dans le flux servi au juge. | Détection de $1,00$ (100%) et TFA $\le 0,02$ sur les fiches honnêtes (le filtre de recouvrement doit arrêter les reformulations partielles où la chaîne inerte est absente, battant ainsi la recherche exacte). Écart de score des juges sur témoins $< 0,2$. | État sans tableau (course 1, RAPPORTÉ fait 3) servant de ligne de base pour le score des témoins plantés et le taux de quarantaine des fiches honnêtes. |

---

### Livrable (d) — Ancrage matériel

Les coûts en jetons et le nombre d'éléments de code à contre-lire par conception (2 pour A, 5 pour B, 3 pour C) figurent au Bloc 2. Au tarif des modèles de l'orchestrateur (VÉRIFIÉ, fait 10), la dépense par course complète (10 cases, 4 proposeurs, 2 juges) est estimée à $12\$$ pour A, $28\$$ pour B et $16\$$ pour C (chiffres illustratifs). Aucun modèle ouvert n'est requis.

---

### Bloc 4 — Ce qu'il faut rapporter au directeur

- **Décision et enjeu** : Choisir entre le tableau minimal par défaut (A), le tableau intermédiaire à pistes typées (C) et le tableau complet (B) pour la course 2, afin d'éliminer les $41,4\%$ de fiches en doublon (VÉRIFIÉ, fait 4) et permettre l'échange d'idées sans compromettre l'étalonnage des juges ni la sécurité du protocole.
- **Options** :
  1. *Option A (Tableau minimal, défaut)* : Avantage : sécurité élevée et surcroît de code minimal (2 éléments). Inconvénient : aucun échange ni co-construction entre proposeurs.
  2. *Option C (Tableau intermédiaire à pistes typées + rôles permutés par l'orchestrateur)* : Avantage : permet l'échange ciblé et les rôles en fermant les canaux de texte libre (3 éléments de code). Inconvénient : expressivité limitée à la liste fermée des types.
  3. *Option B (Tableau complet gardé)* : Avantage : liberté totale de co-construction. Inconvénient : 5 éléments de code à sceller et exposition maximale aux trois écueils.
- **Recommandation et confiance** : Recommander conditionnellement l'**Option C** (confiance **moyenne**, car elle applique directement le principe éprouvé « moins de texte libre : moins de canaux » de `proposeur.py`, VÉRIFIÉ fait 8, tout en répondant au besoin d'échange). Tant que le pré-pilote n'a pas parlé, le défaut (Option A) tient. Basculer vers C (ou B) exige que les mesures du Bloc 1 au pré-pilote confirment l'évitement des trois écueils : (1) baisse de diversité $< 10\%$, part du plus prolifique $\le 0,40$, recouvrement nul chez le juge et dérive sur témoins $< 0,2$ ; (2) prise des instructions glissées plantées égale à $0\%$ ; (3) validation par le directeur du scellement de 3 éléments de code (ou 5 pour B).
- **Ce qui reste HYPOTHÈSE et ce que le pré-pilote doit mesurer** : Il reste HYPOTHÈSE que les pistes typées (C) et les rôles augmentent le nombre d'idées distinctes par dollar sans fuite vers le juge, et que le choix A/B/C échappe à la règle N-058 (VÉRIFIÉ, fait 13). Le pré-pilote doit mesurer les Duels 1, 2 et 3 ainsi que l'accord inter-lecteurs ($\kappa \ge 0,70$) du détecteur de doublons pour le lever.

FIN-DE-CELLULE