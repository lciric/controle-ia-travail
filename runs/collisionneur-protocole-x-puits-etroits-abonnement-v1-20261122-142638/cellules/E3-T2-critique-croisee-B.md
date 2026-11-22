# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces.** Les blocs FAITS et QUESTION ont le même texte visible et la même empreinte affichée. Je n'ai pas recalculé cette empreinte. Les cinq conceptions A, C, D, E et F sont présentes, chacune se termine par son marqueur, et aucune ne paraît coupée. Ma propre conception du tour III.1 n'est pas transmise, donc je ne m'y réfère pas.

**Statuts et chiffres.** Mes calculs ont le statut HYPOTHÈSE (calcul à relire). Règle 4 : aucun chiffre ci-dessous ne vient des faits. Tous sont illustratifs, y compris ceux que je recalcule à partir des chiffres illustratifs des pièces ; seules les constantes de formule sont des identités. Je ne change aucun statut affiché par une pièce. Quand une pièce affiche VÉRIFIÉ sans vérification jointe, je le signale comme un défaut de méthode.

**Divergence à trancher par l'arbitre.** Les chiffres 0,55 et 0,40 du titre reçoivent des statuts différents selon les pièces :
- A les traite comme RAPPORTÉS ;
- E les traite comme RAPPORTÉS, et la neutralité comme OBSERVÉ-NON-AUDITÉ ;
- F les traite comme OBSERVÉ-NON-AUDITÉ.

Le bloc FAITS ne leur attribue aucun statut.

**Notations.** p : fréquence marginale. Θ : fréquence conditionnelle à un état latent. c = écart-type(Θ)/p. k : nombre de positifs vérifiés disponibles pour estimer un rappel.

---

## Sur la proposition A

### (a) Défauts de méthode
1. **D2 : le verdict est fixé par un paramètre d'entrée.** A fait varier ρ « par comptabilité ». Or r* = (1+κ+sρ)/(1+ρ) décroît vers s quand ρ croît, donc tout crible avec r > s passe H_A pour ρ assez grand. Si ρ n'est pas mesuré (I4) et fixé avant le duel, c'est l'expérimentateur qui choisit l'issue : elle n'est pas observée.
2. **D3 : possible fuite vers le vérificateur.** Les classes d'accord sont définies par « même sortie sur des entrées de test ». Si ces entrées recoupent celles du vérificateur, l'identité de classe encode une partie du verdict, et le lien « classe lourde ↔ positif » est en partie construit.
3. **D3 : f n'a pas de loi de référence.** « Plus de la moitié des propriétés » suppose une loi sur les propriétés. Sans elle, f décrit le choix du banc, pas une quantité du problème.
4. **D4 : l'ampleur du décalage est choisie.** La couverture conforme n'est garantie que sous échangeabilité. Sa perte est prévisible pour un décalage assez grand, donc avec un seul décalage (« moitié plus longs ») l'issue H_B dépend de l'ampleur fixée. Une gamme de décalages donnerait une courbe réfutable.
5. **I1 : critère circulaire en régime rare.** Exiger « α inférieur au dixième de la borne inférieure de p » suppose une borne inférieure de p, qui est nulle tant qu'aucun positif n'a été vu. De plus, les mutants minimaux suivent une autre loi que les négatifs produits par le générateur : le α mesuré sur eux n'est pas le α sous μ.
6. **D2 : contamination possible du juge (HYPOTHÈSE).** Sur des bancs publics (tests, énoncés de type miniF2F), le petit modèle a pu voir les objets pendant son pré-entraînement. Couper le bassin en deux moitiés ne protège pas de cette fuite.

### (b) Conditions de perte de puissance
- **D1, valeur nominale.** z_nom = (1−p)^N avec Np = 3. L'erreur relative sur z_nom vaut environ 3/√(n_ref·p). Pour une précision de 10 %, il faut n_ref·p ≳ 900 positifs de référence. En dessous, le critère « z au-dessus du nominal » n'est pas jugeable, et ce poste manque au calcul de (d).
- **D1, hétérogénéité.** Au second ordre en c, E[(1−Θ)^N]/(1−p)^N ≈ 1 + (Np)²c²/2 = 1 + 4,5c². Atteindre le facteur 2 demande donc c² ≳ 0,22. Si Θ est le même pour les 400 campagnes (même version du générateur), sa variance entre campagnes est nulle et D1 ne peut pas identifier la dépendance.
- **D2.** Avec k positifs tous retenus, la borne δ^(1/k) ne dépasse r* que si k > ln(1/δ)/ln(1/r*). Quand ρ diminue, r* monte vers 1+κ ≥ 1, et le k requis diverge puis devient inaccessible.
- **D4.** Si P(T_cible > N_max) > δ, le quantile d'ordre 1−δ est censuré et la couverture n'est pas jugeable.
- **D5.** Le rapport des probabilités de succès tend vers 1 quand B·p ≫ 1 dans les deux bras, et sa variance diverge quand B·p ≪ 1. Il n'a de puissance que si P(succès, bras 1) est intermédiaire, ce qui exige une estimation préalable de p.

### (c) Contrôles négatifs dont l'absence serait fatale
- **D3.** Les entrées qui définissent les classes doivent être disjointes de celles du vérificateur.
- **D2.** Il faut des propriétés construites après le gel du juge, ou synthétiques.
- **D1.** p_ref doit être estimé sur des tirages indépendants des campagnes ; sinon le nominal partage Θ avec ce qu'il doit juger.
- **D4.** Il faut un décalage, à longueur égale, sur un attribut sans lien avec la difficulté.

---

## Sur la proposition C

### (a) Défauts de méthode
1. **Inégalité inversée (1.B).** Comme ln(1/(1−p0)) ≥ p0, on a ln(1/δ)/ln(1/(1−p0)) ≤ ln(1/δ)/p0, et non ≥. La première quantité est le minimum exact ; la seconde est une condition suffisante, plus coûteuse. Le « prix » de 1.B est à relire.
2. **« Domine strictement » (§4.2) oublie le coût du filtre.** Avec κ = c_F/c_prod, un filtre de rappel r = 1 ne bat le tirage brut que si κ < (1−q)ρ. C signale elle-même en (a)4 une analyse qui peut être PSPACE-complète, donc la domination est conditionnelle. A et E incluent ce terme ; je m'appuie sur eux.
3. **§3.3 : une borne inférieure qui baisse ne prouve pas que la probabilité baisse.** L'inégalité P(Z = 0) ≥ (1−p)^N vaut pour des indicatrices positivement associées (Esary, Proschan & Walkup, 1967, « Association of random variables, with applications »). Une covariance positive deux à deux ne suffit pas. « N_eff = N/τ_mix » n'est pas démontré et échoue dès que P(Θ = 0) > 0 (contre-exemple de F, P0-3 de A).
4. **Duel 1 : vrai par construction, plus une fuite.** Le « facteur 5 » découle de q_N ≤ 0,20 par simple arithmétique. Le contrôle négatif injecte des doublons par renommage et espaces, c'est-à-dire exactement les transformations que le normalisateur implémente : il ne vérifie que la conformité du code à sa propre écriture.
5. **Duel 3 : contrôle tautologique.** Le dénominateur de D est la variance après permutation. Appliquer D à la séquence permutée donne donc 1 par définition.
6. **Duel 2.**
   - ρ est fixé à 100 au lieu d'être mesuré.
   - Rien ne sépare les données d'entraînement du proxy de la réserve de test.
   - H_A annonce Γ ≥ 2, mais la décision retient 1,5.
7. **Duel 4 : confusion avec l'ordre de parcours.** L'approfondissement itératif favorise les objets courts. Si P est concentré sur des objets courts, le duel mesure l'ordre de parcours. P_ctrl (k ≤ 4) est un contrôle positif de l'énumérateur, réussi par construction.
8. **Unités incompatibles.** En (d), c_ver est en secondes-CPU et c_prod en secondes-GPU. ρ n'a de sens qu'après conversion dans une unité commune (point I4 de A).
9. **Statuts et zones intermédiaires.** Plusieurs énoncés portent VÉRIFIÉ avec une source dont le contenu, à ma connaissance, ne porte pas sur l'énoncé : Feller pour des « axiomes de coût positif », Knuth (1975) pour la décroissance de p avec la profondeur. Aucune vérification n'est jointe. Par ailleurs, les duels 1, 2 et 4 ne déclarent pas leurs zones intermédiaires (règle B4).

### (b) Conditions de perte de puissance
- **Duel 1.** r = 1 ne se juge que comme une borne : r ≥ δ^(1/k). Pour obtenir 0,99 à δ = 0,05, il faut k ≳ 300, donc N ≳ 300/p. Avec N = 10 000, cela demande p ≳ 0,03.
- **Duel 2.** Parmi n_rej objets rejetés, on attend n_rej·p(1−r)/(1−q) positifs. Si n_rej·p ≪ 1, 1−r n'est pas estimable et l'intervalle de Γ̂ n'est pas borné.
- **Duel 3.** Avec la formule de F, D − 1 ≈ (L−1)c²p. Pour L = 100 et p = 10⁻³, D ≥ 3 exige c² ≳ 20. Un Θ constant sur toute la séquence reste invisible.
- **Duel 4.** Si P(aucun succès dans B) ≥ 1/2 dans un bras, la médiane est censurée.
- **Générateur, en (c).** Le test de Kolmogorov-Smirnov sur les longueurs n'a aucune puissance contre une différence de μ(P) à loi des longueurs égale.

### (c) Contrôles négatifs dont l'absence serait fatale
- **Duel 1.** Des paires (x⁺ ∈ P, x⁻ ∉ P) qui diffèrent d'un seul nœud doivent rester dans des classes distinctes. La seule panne qui fait baisser r est la fusion abusive, et aucun contrôle ne la cherche.
- **Duel 2.** Le proxy doit être construit sur des données disjointes de la réserve.
- **Duel 3.** Il faut plusieurs sessions indépendantes et une permutation entre sessions.
- **Duel 4.** Il faut un énumérateur apparié à la loi des longueurs du générateur.

---

## Sur la proposition D

### (a) Défauts de méthode
1. **Duels 1 et 2 : des théorèmes, pas des expériences.** La preuve de D réfute déjà H_A, et D écrit que seule une preuve falsifierait H_B. L'une des deux issues est donc impossible, et B4 n'est satisfaite que formellement. Ce sont des réponses valables au point 5 (« preuve ») : il faut les compter comme preuves, pas comme expériences.
2. **Duel 3 : fuite dans le comparateur.** Le score est appris hors du banc, mais le « meilleur contrôle mécanique admissible » est choisi sur le banc gelé. Prendre le maximum de plusieurs contrôles évalués sur les mêmes données biaise le duel en faveur de H_B.
3. **Duel 3 : seuil « différence nulle » sur un banc fini.** Le banc est un échantillon de μ. Restreindre la conclusion au banc la rend exacte mais sans portée, et une seule session discordante suffit à trancher.
4. **(d) : coût et verdict indépendants par construction.** Avec un évaluateur exact et bon marché, c_v(x) ne dépend pas de V(x). Le régime soulevé par E et F, où le coût de vérification croît près des positifs, n'est pas testable sur ce banc.
5. **Statuts.** D donne VÉRIFIÉ à ses propres déductions, alors que A refuse de le faire. Je ne change rien : c'est à l'arbitre de trancher.

### (b) Conditions de perte de puissance
- **Duel 3.** Une session discordante contient forcément un positif. Leur nombre est donc au plus binomial (S ; 1−(1−p)^m). Si S·(1−(1−p)^m) est petit, le signe de la différence n'est que du bruit.
- **Mesure du vérificateur.** Avec K positifs sur le banc, P(accepté | S) n'est connu que par une borne en δ^(1/K).

### (c) Contrôles négatifs dont l'absence serait fatale
- Un score permuté entre objets, à loi et coût inchangés. Le score constant ne teste que le départage des ex æquo.
- Un comparateur mécanique choisi sur un banc distinct du banc d'évaluation.

---

## Sur la proposition E

### (a) Défauts de méthode
1. **Un non-rejet compte comme une réfutation.** En E1, « dans le cas contraire, H_A est réfutée » ; en E3, « si D ≤ 1,24, H_B est réfutée ». À faible puissance, l'hypothèse qui exige un rejet perd par défaut.
2. **E1 : le test ne teste pas le seuil, et une confusion s'ajoute.** Le test exact de Fisher éprouve un rapport des cotes égal à 1, pas Λ > 2. De plus, la loi uniforme sur L_{≤L}(G) se concentre sur les longueurs maximales quand le nombre d'objets croît exponentiellement avec la longueur : le duel compare alors des profils de longueur.
3. **E2 : issues non exclusives.** « Δ > 0 significatif » et « γ = 0 manque des solutions de la branche uniforme » peuvent survenir ensemble. La seconde clause n'est pas la négation de H_A.
4. **E2 : fuite non évitée (HYPOTHÈSE).** Le modèle de score Qwen2.5-1.5B est de la même famille que le générateur Qwen2.5-Coder-7B. Des données d'entraînement partagées rendraient leurs erreurs corrélées.
5. **E4 : la VPP dépend de p.** À α_V et β_V fixés, la VPP croît avec p. Mesurée sur des objets acceptés à un p plus élevé, elle surestime la VPP au p du puits. Il faut estimer α_V et β_V séparément. Si V et V* partagent la même spécification, une VPP proche de 1 est acquise par construction.
6. **(c) : critère sur V hors d'atteinte.** Zéro alerte sur 10 000 négatifs certifie α_V ≲ 3×10⁻⁴ à 95 %. Cela ne vaut 0,01·p que si p ≳ 0,03, donc pas dans le régime visé.
7. **Statuts.** VÉRIFIÉ est affiché pour l'identité bit à bit des blocs et pour des citations, sans vérification jointe.

### (b) Conditions de perte de puissance
- **E3.** Quand M·p ≪ 1, l'approximation χ² de la loi nulle de D est fausse et le seuil 1,24 n'est pas calibré. La puissance varie comme (M−1)c²p.
- **E4.** n₊ = 460 acceptés demandent environ 460/p tirages vérifiés. Cela dépasse les 60 000 appels prévus dès p ≲ 8×10⁻³.
- **E1.** Si P_hit est proche de 0 ou de 1 dans les deux bras, Λ̂ n'est pas défini ou vaut 1.
- **E2.** Sur 50 puits, si P(discordance) ≲ 0,1, on attend au plus 5 paires discordantes, ce qui est trop peu pour McNemar.

### (c) Contrôles négatifs dont l'absence serait fatale
- **E3.** Des blocs issus de sessions indépendantes. Sans eux, « H_B réfutée » est acquise d'avance.
- **E1.** Une loi uniforme stratifiée sur la loi des longueurs du générateur.
- **E4.** Des positifs certains soumis à V*, qui doit tous les accepter. Sinon, les faux négatifs de V* passent pour des fausses alertes de V.
- **E2.** Un modèle de score d'une famille indépendante de celle du générateur.

---

## Sur la proposition F

### (a) Défauts de méthode
1. **E1 : issue intermédiaire non déclarée.** Si D vaut entre 1,10 et 1,40, la règle « poursuivre jusqu'à séparation » a deux sorties possibles : soit elle ne termine pas, soit elle se fait par SPRT et termine en désignant à tort l'une des deux hypothèses. Autre défaut : « même contexte » et « appels consécutifs » sont deux estimandes différents (état latent ou autocorrélation), mesurés par une seule statistique.
2. **E2 : H_A et H_B ne couvrent pas tous les cas.** Un Lift dans ]1 ; 2[, ou un Lift ≥ 2 avec G_déd < 1,5, ne falsifie rien. De plus, G_déd est une fonction déterministe de U/N et de ρ : il mesure la répétition du générateur, pas la localisation des positifs.
3. **E3 : biais de sélection de l'audit.** τ_OOD est estimé sur les positifs trouvés par l'audit. Si la méthode d'audit ressemble à l'un des bras, τ n'est mesuré que sur les positifs que ce bras sait trouver.
4. **E4 : sortie du cadre et contrôle mal calibré.** Changer de configuration ou de prompt revient à utiliser d'autres générateurs, ce qui sort du cadre « tirages seuls » (A le note pour son D5). Sous l'oracle de hachage, des bras dont le taux d'objets distincts diffère peuvent légitimement donner R > 1. Le résultat « ≤ 1,05 » n'est donc pas garanti, et son échec passerait pour un bogue.

### (b) Conditions de perte de puissance
- **E1.** D'après la formule de F, D − 1 = (m−1)Var(Θ)/(p(1−p)). Avec m = 50, D ≥ 1,40 exige c² ≳ 0,4/(49p), soit environ 0,8 à p = 10⁻² et environ 8 à p = 10⁻³.
- **E2.** Si N_g·μ(c) ≪ 1 pour toute classe, le classement par fréquence n'est qu'un départage. Lift vaut alors 1 en espérance sous les deux hypothèses, et H_A tombe par construction.
- **E3.** Avec N_g = 256 et p = 10⁻³, on attend environ 0,26 positif par tâche, et la plupart des paires sont (0, 0). Le diagnostic « τ = 0 » sur une tâche n'est jamais jugeable : seule une borne supérieure de τ l'est.
- **E4.** R_adapt n'a de puissance que si P_unif-déd(B) reste loin de 0 et de 1.

### (c) Contrôles négatifs dont l'absence serait fatale
- **E3.** Des positifs d'audit obtenus en vérifiant exhaustivement les tirages des deux bras.
- **E4.** Un contrôle par hachage où le rendement en objets distincts est égalisé entre bras.
- **E1.** Des blocs égaux à des sessions indépendantes, avec la permutation à l'intérieur des sessions traitée à part.

---

## Ce qui peut être réfuté ici
- **Une inégalité inversée** chez C (1.B), vérifiable en une ligne.
- **Sept conditions de puissance calculées**, toutes des HYPOTHÈSES à relire : deux pour A-D1, une pour A-D2, C-duel 1, C-duel 3, E-E4 et F-E1.
- **Six défauts « vrai par construction » ou tautologiques** : A-D2, C-duel 1, C-duel 3, D-duels 1 et 2, F-E2 (G_déd), F-E4 (contrôle).
- **Deux règles de décision où un non-rejet vaut réfutation** : E1 et E3.

FIN-DE-CELLULE