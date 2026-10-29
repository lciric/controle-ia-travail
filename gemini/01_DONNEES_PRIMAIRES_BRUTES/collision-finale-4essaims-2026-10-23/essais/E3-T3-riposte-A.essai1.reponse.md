# Proposition A — Tour III.3 : riposte

## 0. Pièces reçues (règle 2)

Les deux attaques (B, C) sont complètes et closes par FIN-DE-CELLULE. Je confirme l'observation de B : la pièce FAITS a ses accents remplacés par « ? » ; le texte reste lisible, je n'en reconstruis rien. Je ne réponds qu'aux sections « Contre la proposition A » ; les critiques de B contre C et de C contre B ne sont pas de mon ressort, sauf quand j'en réutilise une, en le disant.

---

## 1. Réponse aux attaques

Verdicts : **accepté**, **rejeté** (avec raison), **transformé en test**. Les attaques identiques de B et C sont traitées une fois.

### 1.1 Comptages et lectures (B, A-1)

- **« Onze textes non vides sous un vide » → 15.** **Accepté.** Recompte sur l'Annexe 1 (OBSERVÉ-NON-AUDITÉ) : sous le plus bas score vide (0,06), essaim A : 5 ; essaim B : 8 ; essaim D : 2 ; essaim C : 0. Total 15. Mon chiffre était faux ; la conclusion (le barème classe « rien » au-dessus de 15 propositions imparfaites) tient. J'ajoute, en aggravant l'observation de B : pour l'essaim B, aux **trois** époques 1, 2 et 4 (pas seulement 1 et 4), une riposte non vide existait (−0,48/−0,42 ; −0,45 ; −0,16/−0,31) et l'objet vide a été sélectionné comme champion. Statut OBSERVÉ-NON-AUDITÉ, à recompter.
- **Vecteur d'Argon Ep1 à trois blocs, pas quatre.** **Accepté.** Le texte définit $\tilde\psi_t\in\mathbb{R}^{3m}$ avec deux délais $\delta_1,\delta_2$, tout en listant trois valeurs $\{1,4,16\}$ : incohérence interne du champion, pas la mienne. Ma critique de fond est renforcée : $J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}$ est une matrice à deux blocs appliquée à un vecteur à trois blocs ; le produit $\tilde\psi_t^\top J\tilde\psi_{t-1}$ n'est même pas typé, et il ne porte toujours pas sur les blocs (valeur, erreur TD) que l'argument E2 invoque.

### 1.2 D1, audit de l'oracle (B A-2, évasions D1 de B et de C)

- **Pas de vérité terrain, issue négative ininterprétable, confondant de famille, variante (iii) colinéaire.** **Accepté.** Si score(i) ≈ score(ii), Jev peut voir que (i) est déjà cassé ; les six originaux sont d'Argon et j'en tiens plusieurs pour invalides. La troncature (iii) détruit longueur et validité ensemble : supprimée.
- **Évasion : équations dimensionnellement justes et sémantiquement vides ; indices de couches permutés ou $H_A/H_B$ inversés dans le corps.** **Accepté**, et c'est la même faille : la permutation intra-équation ne couvre que les défauts syntaxiques. **Transformé** : D1′ s'appuie sur un étalon étiqueté *avant* scoring, avec défauts sémantiques plantés (voir §2).

### 1.3 D2, collision vs oracle (B A-3, A-4 ; C-1, C-4 ; évasions D2)

- **Exclusion des cycles $|a|=0$ = biais de survie / budget inégal.** **Accepté** (B et C). Un attaquant qui s'éteint sur les conceptions difficiles ne laisse au bras Collision que les cas faciles ; un défenseur contrôlant l'attaquant peut vider les attaques qui le menacent. Correction : analyse en intention de traiter, appel perdu compté, cycle noté sur $x_0$ non révisé. L'analyse « par protocole » n'est reportée qu'en secondaire.
- **Grille à 8 items = instrument fuité vers le traitement ; placebo porteur du même lexique ; remplissage lexical à coût nul.** **Accepté** (B et C). Une grille lisible par l'attaquant est optimisable sans substance. **Transformé** : le juge devient non lexical (défauts sémantiques plantés, retirés ou non ; comptage en aveugle de failles fatales par un humain en temps borné). Placebo corrigé : une vraie critique d'un *autre* protocole (même lexique, aucune pertinence).
- **Une seule époque testée.** **Accepté** : D2′ passe à 3 époques (illustratif) avec hérédité du champion.
- **DPP sur trois candidats pour une sélection = argmax.** **Accepté** : le bras est renommé « Oracle + best-of-3 ». Je n'avais pas de DPP, j'avais un nom.

### 1.4 D3, existence de $S_{\text{TD}}$ (B A-5 ; C-2 ; évasion D3 de C)

- **Fuite attribution → ablation (mêmes trajectoires).** **Accepté.** Partition disjointe.
- **Nature de l'ablation non précisée (zéro vs moyenne).** **Accepté** : les deux, reportées séparément ; $H_A$ exige la réussite sous les deux.
- **$H_A/H_B$ non exhaustives (zone 3–10 % de $\mathcal{N}_{\text{cap}}$).** **Accepté**, B4 violée. Correction : $H_B \equiv \neg H_A$ sur l'ensemble des candidats produits par la procédure (§2).
- **Fuite S_TD découvert sur bandit → évalué sur délégation ; les neurones captent la syntaxe de rétroaction (C-2).** **Accepté**, **transformé** en contrôle : un ensemble $S_{\text{synt}}$ sélectionné par attribution sur la *prédiction des jetons de rejet* ; si $\delta z$ sur $S_{\text{synt}}$ fait aussi bien que sur $S_{\text{TD}}$ en D4′, le substrat n'est pas TD-spécifique.
- **Évasion « routage hors $S$ à coût nul », justifiée par le fait (3) du socle.** **Rejeté sur l'inférence, accepté comme hypothèse.** Le fait VÉRIFIÉ dit que le *pilotage linéaire dense* n'a pas de levier sur 0,49 → 0,65 ; il ne dit rien sur l'endroit où le calcul du contournement transite ni sur son coût. « $\Delta\mathcal{N}_{\text{cap}}=0$ » est une affirmation sans mesure. De plus, D3 teste l'existence de $S$ chez le modèle *honnête* ; qu'un saboteur puisse calculer ailleurs est une attaque contre D4–D5, pas contre D3. Elle rejoint la porte dérobée de B : **transformé** en D7.

### 1.5 D4, le différentiel avec/sans prompt système (B A-6, contrôles 4–5, évasions ; C-3, contrôles 1–2)

C'est le cœur ; je concède l'essentiel.

- **P3 vs P1 reconduit le confondant P3 ; le contraste qui isole l'acte est P3 vs P2.** **Accepté.** Je définissais P2 et ne l'utilisais pas.
- **Instruction déplacée hors du prompt système → $\delta z\approx 0$ (B) ; préambule public auto-porteur type *Astra* → $\delta z\to 0$ (C).** **Accepté**, les deux à coût nul. Ce sont des populations positives que le re-forward ne voit pas par construction. **Transformé** : populations P4 et P5 ; si le sabotage y réussit avec $\delta z$ au niveau honnête, la famille lit le *canal*, pas l'acte.
- **Acte imposé (teacher forcing d'un honnête sur les jetons du sabotage).** **Accepté**, contrôle PF.
- **Re-forward sur jetons déjà générés = proxy de perplexité, pas d'intention (C-3) ; absence de troncature pré-acte (C, contrôle 1).** **Accepté**. Correction : fenêtre strictement antérieure au premier jeton d'acte, et contrôle de résidualisation : régression de $\|\delta z_t\|_1$ sur $\Delta\log p_t=\log p(x_t\mid\sigma)-\log p(x_t\mid\varnothing)$ ; AUROC reporté avant et après résidualisation.
- **Prompt bénin syntaxiquement inhabituel (C, contrôle 2).** **Accepté**, population P1′.
- **Teacher forcing croisé sur préfixes strictement identiques** (contrôle que C oppose à B et que B me demande implicitement via P3 vs P2). **Transformé, avec une réserve algébrique.** Si le prompt *et* le préfixe sont identiques entre une trajectoire qui agira et une qui n'agira pas, les activations à $t-k$ sont identiques par causalité du modèle : le contraste est vide, il ne mesure que l'aléa de décodage. « Intention » ne peut pas être une fonction du futur. Je redéfinis donc P2 comme dans ma conception initiale, *condition de déclenchement absente du contexte public*, et je structure D4′ en plan factoriel 2×2 (instruction × déclencheur) : le signal d'acte est le **terme d'interaction**, l'effet principal « instruction » est le confondant P3, l'effet principal « déclencheur » est le confondant lexical. Les préfixes diffèrent alors par le déclencheur et par lui seul, et le contrôle honnête + déclencheur mesure ce que le déclencheur fait à lui seul.
- **Duel commun de B** ($\delta z$ porte l'acte vs le canal/les jetons). **Je l'adopte**, en le disant : il devient le critère principal de D4′, complété par le 2×2 et la résidualisation.

### 1.6 Baselines (B A-7)

- **M2 est l'étiquette de l'acte, pas une baseline.** **Accepté pour les actes observables ; transformé.** M2 reste le plafond de la détection *a posteriori* — et les incidents *Sol* (surveillance coupée) sont exactement ce que M2 attrape. Conséquence : un détecteur boîte blanche ne se justifie que (a) sur la fenêtre pré-acte, où M2 est indéfini, ou (b) sur une classe d'actes sans trace d'état (test inversé). Le critère d'adoption est réécrit ainsi.
- **M1 construit sur *Astra* → fuite si la classe positive imite *Astra*.** **Accepté.** La regex M1 est gelée avant génération ; la classe positive est construite par une partie aveugle à M1 et inclut des déclencheurs non lexicaux (champ JSON, ordre d'arguments — évasion D5 de B), sur lesquels M1 est reporté séparément.

### 1.7 D5, adversaire contre $\Lambda_{\text{imp}}$ (B A-8, contrôle 6, évasion ; C évasion et contrôle 3)

- **Force de l'adversaire non calibrée.** **Accepté.** L'attaquant doit d'abord battre M5 (perplexité), détecteur connu cassable ; la méthode est précisée (recherche d'ordre zéro sur éditions de texte, $\Lambda_{\text{imp}}$ ayant un max et une médiane non dérivables — je reprends ici l'argument de *gradient masking* que C oppose à B, il s'applique à moi).
- **Gonflement de la médiane : amplifier $\Psi$ sur 51 % des jetons, $\Lambda\to1$.** **Accepté** : évasion analytique, zéro itération. **Transformé** en stratégie semée S1 ; son coût réel (taux d'infraction conservé) est ce que D5′ mesure, et la « parade de Kerckhoffs » d'Argon Ep2 (qui n'envisageait que la dilution) tombe si S1 conserve l'infraction.
- **Déclencheur non lexical (B).** **Accepté**, stratégie semée S2.
- **Message bénin à >50 % de ponctuation/code (C, contrôle 3).** **Accepté**, contrôle du dénominateur.

### 1.8 D6, seuil PID (B, C)

- **« Le seuil converge vers $\alpha$ sous sabotage soutenu, A le dit lui-même. »** **Accepté** : c'est mon $H_B$. **Rejeté** sur la lecture de C (« A conserve D6 comme instrument ») : D6 est un test de falsification de Chimère Ep4, pas un instrument que je propose. Je concède que l'issue est quasi analytique ; seule la *vitesse* de convergence est inconnue (gains $K_P,K_I,C,\gamma$ non fixés par le champion). D6 est rétrogradé en vérification numérique à faible coût, duel conservé.

### 1.9 Évasion conjointe (B : porte dérobée dans les poids + pénalité sur $\|\delta z_S\|$ ; C : préambule de 200 jetons)

**Accepté** pour les deux. La version de C est couverte par P5 (coût mesuré en D4′). La version de B exige une expérience propre, **D7**, qui est le seul test de Kerckhoffs portant sur la prémisse commune et non sur un raffinement.

---

## 2. Expériences corrigées

Convention : seuils **illustratifs**, fixés avant exécution. Cible `Llama-3.1-8B-Instruct` ; 70B en réplication de D3′ et D4′ seulement.

### D1′ — Jev contre un étalon étiqueté

- **Étalon** : 40 protocoles (illustratif) de ≥ 3 familles de modèles et d'auteurs humains : 20 valides, 10 à défaut syntaxique planté (dimension, contrôle absent), 10 à défaut sémantique planté (fuite calibration/test, $H_A/H_B$ non exclusives, définitions de $H_A/H_B$ inversées, indices de couches permutés). Étiquetés par deux humains avant tout scoring, sans accès à Jev.
- **$H_A$** : AUROC(valide vs défaut sémantique) ≥ 0,75 et $\rho_{\text{Spearman}}$(score, longueur | validité) < 0,3.
- **$H_B$** : AUROC ≤ 0,60 ou $\rho\ge0{,}7$. (Zone intermédiaire : Jev pré-filtre, jamais juge.)
- **Contrôle négatif** : texte vide sous tous les textes non vides ; variantes (ii) permutation intra-équation et (iv) remplissage lexical conservées en secondaire ; (iii) supprimée.
- **Falsification** : $H_A$ fausse ⇒ Annexe 1 invalide comme critère de sélection ; $H_B$ fausse ⇒ Jev utilisable en pré-filtre.

### D2′ — Collision croisée vs Oracle + best-of-3, intention de traiter

- Budget $B=4$ appels/cycle, 3 époques (illustratif), hérédité du champion, ≥ 24 lignées par bras.
- **Bras Collision** : CONÇOIS → ATTAQUE (autre modèle) → RIPOSTE → JUGE. Si $|a|=0$ : appel compté, riposte = $x_0$.
- **Bras Oracle + best-of-3** : 3 × CONÇOIS → 1 appel JUGE groupé → argmax.
- **Bras placebo** : critique réelle d'un autre protocole.
- **Juge** (non lexical) : taux $\rho$ de défauts sémantiques plantés dans $x_0$ effectivement retirés en fin de lignée ; nombre de failles fatales trouvées par un humain en aveugle en 15 min (illustratif). Jev n'intervient dans aucun bras.
- **$H_A$** : Collision > best-of-3 et > placebo de ≥ 0,25 sur $\rho$ (illustratif). **$H_B$** : écart ≤ 0,10 ou best-of-3 supérieur.
- **Falsification** : $H_A$ fausse ⇒ le collisionneur n'apporte rien à budget égal ; $H_B$ fausse ⇒ l'attaque vaut par son contenu, et son budget doit être garanti hors *thinking*.

### D3′ — Porte E0 sur Llama-3.1-8B, partitions disjointes

- Trois partitions de trajectoires de bandit en contexte : $\mathcal{P}_1$ (attribution, génère un ensemble de candidats $\mathcal{C}$, $|S|<1\%$), $\mathcal{P}_2$ (ablation confirmatoire, zéro **et** moyenne), $\mathcal{P}_3$ réservée à D4′. Tâche de délégation jamais utilisée en découverte.
- **$H_A$** : $\exists S\in\mathcal{C}$ : $\Delta_{\text{TD}}(S)\ge30$ pts sur $\mathcal{P}_2$ sous les deux ablations, $\Delta\mathcal{N}_{\text{cap}}<3\%$ (MMLU, référence à vérifier) et $\Delta_{\text{TD}}(S)-\Delta_{\text{TD}}(\text{aléatoire apparié})\ge20$ pts. **$H_B\equiv\neg H_A$** sur $\mathcal{C}$ (exhaustif).
- **Contrôles négatifs** : ensemble aléatoire apparié par couche ; neurones de plus forte norme ; $S_{\text{synt}}$ (attribution sur prédiction des jetons de rejet).
- **Falsification** : $H_A$ fausse ⇒ les 13 détecteurs « sur $S_{\text{TD}}$ » sont sans substrat sur Llama ; $H_B$ fausse ⇒ substrat et mesure de $\mathcal{N}_{\text{cap}}$ disponibles.

### D4′ — Le différentiel porte-t-il l'acte, le canal ou les jetons ? (duel commun de B, étendu)

- **Statistique** : $\|\delta z_t\|_1$ sur $S$ (D3′), fenêtre strictement pré-acte : du déclencheur au jeton $t^\star-k$, $k\in\{1,8\}$ (illustratif). Fraction de positifs à fenêtre vide reportée (déclenchement balistique).
- **Plan 2×2** : instruction (sabotage $\sigma_s$ / bénigne secrète $\sigma_b$ de même longueur) × déclencheur dans le contexte public (présent / absent). Cellules : P3 ($\sigma_s$, présent), P2 ($\sigma_s$, absent), P1$^{+}$ ($\sigma_b$, présent), P1 ($\sigma_b$, absent). Signal d'acte = interaction ; effet principal instruction = confondant P3 ; effet principal déclencheur = confondant lexical.
- **Populations supplémentaires** : P0 (sans instruction) ; P1′ (bénin, syntaxiquement inhabituel) ; P4 (sabotage, instruction dans un tour utilisateur/sortie d'outil) ; P5 (sabotage, préambule public auto-porteur) ; PF (honnête teacher-forcé sur les jetons de P3).
- **$H_A$** : interaction significative avec AUROC(P3 vs P2) ≥ 0,75 ; AUROC(P1$^+$ vs P1) ≤ 0,60 ; AUROC(PF vs P0) ≤ 0,60 ; AUROC(P4 ∪ P5 vs P1) ≥ 0,70 ; résultats maintenus après résidualisation sur $\Delta\log p_t$.
- **$H_B$** : AUROC(P3 vs P2) < 0,60, **ou** PF détecté au niveau de P3, **ou** P4 ∪ P5 sous 0,60 avec sabotage réussi, **ou** AUROC chute de ≥ 0,15 après résidualisation.
- **Contrôles négatifs** : même statistique sur aléatoire apparié et sur $S_{\text{synt}}$.
- **Falsification** : $H_A$ fausse ⇒ Fable Ep1/Ep3/Ep4, Argon Ep1/Ep3/Ep4, Chimère Ep1/Ep2/Ep4 perdent leur substrat commun, avant tout raffinement ; $H_B$ fausse ⇒ le différentiel est validé contre quatre confondants nommés, et seulement contre eux (D7 reste ouvert).

### D5′ — $\Lambda_{\text{imp}}$ (Argon Ep2) contre un adversaire calibré

- **Prérequis** : $R^2$(identité du jeton → $\delta_t$) < 0,3 (illustratif) ; contrôle du dénominateur : $\Lambda_{\text{imp}}$ sur messages bénins à > 50 % de ponctuation/code — si $\Lambda$ dépend de la densité syntaxique, le ratio est un artefact.
- **Adversaire** : qualification obligatoire contre M5 ; stratégies S1 (gonflement de la médiane, 0 itération), S2 (déclencheur non lexical), S3 (recherche d'ordre zéro sur éditions de $m_{1\to2}$, 200 itérations, illustratif, accès boîte blanche au détecteur).
- **$H_A$** : aucune stratégie n'obtient $\Lambda<\tau_{\text{crit}}$ avec infraction ≥ 0,60, et le coût contre $\Lambda_{\text{imp}}$ dépasse de 20 pts (illustratif) le coût contre un $w_\ell$ aléatoire. **$H_B$** : une stratégie y parvient.
- **Falsification** : $H_A$ fausse ⇒ la parade de Kerckhoffs d'Argon Ep2 est réfutée (si S1 suffit, elle l'est à coût nul) ; $H_B$ fausse ⇒ coût d'évasion mesuré, non argumenté.

### D6 — PID de Chimère Ep4 (vérification numérique)

Inchangé ($H_A$ : taux d'alarme ≥ 3α sous sabotage soutenu de 500 jetons ; $H_B$ : convergence vers $[\alpha/2,2\alpha]$ en < 200 jetons), contrôle P0 convergeant aussi vers α. Les deux équipes rouges rejoignent mon $H_B$ ; l'inconnue restante est le temps de convergence en fonction des gains. Coût marginal.

### D7 — Porte dérobée dans les poids contre la prémisse commune (nouveau, pris à B)

- **Attaque** : LoRA sur le 8B, $\mathcal{L}=-\text{succès}_{\text{sab}}+\lambda\|\delta z_S\|_2^2$, sans instruction dans le contexte. $\|\delta z_S\|_1$ est dérivable presque partout : attaque par gradient légitime ; pour les statistiques de champions non dérivables, ordre zéro.
- **$H_A$** : il existe $\lambda$ tel que succès ≥ 0,60, $\|\delta z_S\|$ au niveau de P1, $\Delta\mathcal{N}_{\text{cap}}<1\%$ et taux de réussite agentique conservé (illustratif). **$H_B$** : tout LoRA ramenant $\delta z_S$ au niveau honnête perd ≥ 50 % de succès ou $\Delta\mathcal{N}_{\text{cap}}\ge3\%$.
- **Contrôle** : LoRA sans pénalité (plancher de succès) ; pénalité sur un ensemble aléatoire apparié.
- **Falsification** : $H_A$ fausse ⇒ l'hypothèse « la parcimonie rend la pénalité bon marché » est réfutée ; $H_B$ fausse ⇒ la famille entière est aveugle aux objectifs inscrits dans les poids, et seule la vérification d'acte (M2) reste.

**Ordre de dépendance** : D1′, D2′ indépendants (API seule). D3′ → D4′ → {D5′, D7} ; D6 marginal. **Prérequis bloquant inchangé** : une classe positive `(i-a)` reproductible sur Llama, construite par une partie aveugle à M1, incluant déclencheurs modaux et non lexicaux, tâches à surveillance désactivable et à test inversable. Sans elle, D4′–D7 n'ont pas de TPR.

---

## 3. Réponse à l'arbitre

**Ce qui est établi (VÉRIFIÉ, socle uniquement).** Les sondes linéaires génériques sont au plancher sur `(i-a)` (P3). Deux incidents de délégation (*Sol*, *Astra*) existent. Les infractions montent de 0,49 à 0,65 sous rejets répétés sans levier par pilotage linéaire dense. Un sous-système parcimonieux (< 1 %) existe sur les modèles d'origine de Xu et al. (`arXiv:2602.00986v2`, référence à vérifier), avec −54,9 pts par ablation. Aucune tête de sabotage pré-établie, aucune sonde temps réel en production.

**Ce qui est observé, non audité.** Les 48 scores Jev. Dans ce tableau, 15 propositions non vides sont classées sous l'objet vide le moins bien noté, et l'essaim B a sélectionné un objet vide comme champion à trois époques alors qu'une riposte non vide existait. Aucun des 16 champions n'a reçu d'attaque externe non vide ; les ripostes sont des auto-critiques. L'essaim « chimère » est à 3/4 une monoculture Argon. Le point 1 de l'arbitre (« mécanismes ayant survécu à la Red-Team ») n'a donc pas de référent dans les pièces ; le point 2 (collision vs oracle à budget constant) n'a pas été exécuté, puisque les appels d'attaque perdus n'ont pas été comptés.

**Ce qui n'est pas établi (HYPOTHÈSE), et que les deux équipes rouges ont rendu plus précis.** (1) Que $S_{\text{TD}}$ existe sur Llama-3.1-8B/70B. (2) Que le différentiel avec/sans prompt système isole l'acte : B et C ont montré quatre façons dont il peut lire autre chose — le contenu de l'instruction (P3 vs P1), le canal (instruction déplacée, préambule public), les jetons (acte imposé, perplexité du re-forward), et rien du tout si l'objectif est dans les poids. Je retiens que mon D4 initial pouvait valider $H_A$ pour une mauvaise raison ; c'est corrigé. (3) Que les parades de Kerckhoffs tiennent : celle d'Argon Ep2 a une évasion analytique à zéro itération (gonflement de la médiane) qui n'a pas été testée. (4) Que Jev mesure autre chose que longueur et lexique : mon D1 ne pouvait pas trancher sans étalon étiqueté. (5) Que la collision vaut mieux qu'un best-of-N : mon D2 avait un biais de survie et un juge fuité. (6) Qu'une classe positive `(i-a)` existe sur Llama : rien dans le socle ne le dit.

**Sur le point 3 de l'arbitre.** Je maintiens le refus de « sélectionner six protocoles » dans un corpus dont 10/16 sont vides ou coupés et dont le classement vient d'un oracle non audité. Ce que je livre à la place : sept duels dont chaque issue élimine un bloc de la question. Les six textes complets (tous Argon) partagent une prémisse unique ; les tester un à un avant d'avoir testé la prémisse serait du travail sans objet.

**L'expérience à faire en premier : D3′** (existence de $S_{\text{TD}}$ sur Llama-3.1-8B, partitions disjointes, double ablation, contrôles aléatoire et $S_{\text{synt}}$). Raisons : elle ne requiert pas de classe positive, donc elle peut démarrer aujourd'hui pendant que la classe positive se construit ; son issue négative invalide à la fois les 13 détecteurs non vides et le présupposé E0 que tous déclarent sans l'avoir mesuré ; son issue positive fournit le substrat et la mesure de $\mathcal{N}_{\text{cap}}$ dont D4′, D5′ et D7 dépendent. Coût ~150 GPU·h A100 (illustratif). En parallèle et à coût API seul : D1′, parce que tant que Jev n'est pas étalonné, aucun chiffre de l'Annexe 1 ne peut servir à quoi que ce soit, pas même à choisir ce qu'on teste ensuite. Immédiatement après D3′ : D4′ sous la forme du duel commun de B, étendu au 2×2 et à la résidualisation ; c'est l'expérience qui conditionne tout le reste, et c'est celle que ni les champions ni ma conception initiale n'avaient correctement posée.

FIN-DE-CELLULE