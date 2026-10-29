# Tour III.2 — Équipe rouge croisée — Proposition A

Statuts : tout ce qui vient des pièces servies est RAPPORTÉ ; les seuils que j'avance sont « illustratifs » ; mes diagnostics sur la conception C sont des HYPOTHÈSES de lecture, à réfuter par les contrôles que je demande. Garde R-519 respectée : les scénarios d'évasion sont nommés par **classe de dommage hors du support de l'oracle**, jamais par recette ; rien ici ne décrit comment un agent échapperait à un moniteur.

---

## Contre la proposition B

La pièce E3-T1-conception-B est absente (statut : REFUS, décision de l'arbitre). Je n'ai rien à attaquer et je n'invente pas son contenu. Conséquence de protocole : toute attaque de B contre A ou C au tour 2 n'aura pas de conception à laquelle la rapporter, et la synthèse devra compter B comme absent sur ce tour, comme elle l'a fait au tour précédent (pièce A, en-tête).

---

## Contre la proposition C

C propose un oracle fonctionnel « O1+O4 » : extraire mécaniquement l'artefact de contrôle final $C_{\text{final}}$, le soumettre à $M$ défauts plantés et $M'$ entrées saines, mesurer la part de défauts qui passent. C'est la conception la plus construite du tour, et c'est précisément pourquoi il faut la casser aux endroits où elle est vraie par construction.

### (a) Failles

**F1 — L'argument contre la prémisse se retourne contre O5 et contre « aveugle au texte ».**
C soutient que « tout dommage est entièrement déterminé par le texte des actions » et que « invisible au texte » n'est qu'un artefact de formulation. Soit. Mais alors $C_{\text{final}}$ est, lui aussi, du texte écrit par l'agent. Un oracle qui lit $C_{\text{final}}$ n'est pas « aveugle à la trajectoire textuelle » : il est aveugle à **une partie** du texte (les actions antérieures et les commentaires). Pour les tâches en prose, l'artefact **est** le texte, et le repli O5 confie sa lecture à un modèle de langage (Mistral ou Gemma, nommés par C). On a donc, sur ces tâches, un juge-modèle qui lit un texte de l'agent : la circularité que C dit avoir coupée est déplacée, pas supprimée. C'est d'autant plus grave que C estime « universelle » la compatibilité d'O5 et chiffre son coût à la banque à 13–26 USD (illustratif chez C) : si E1 échoue ($p_{\text{exec}} < 0{,}80$), la voie de repli est la voie circulaire.

**F2 — Le dommage est mesuré sur un point final, la dose est définie sur les actions : deux unités différentes, jointes par construction.**
P-015 définit la dose comme « proportion $p$ d'actions sabotées × intensité » et le « diffus » par action (« chaque action sabotée sous le seuil du meilleur moniteur par action »). L'oracle de C ne voit qu'un état terminal. Deux conséquences :
- Un affaiblissement **diffus dans la trajectoire** (vérifications sautées ou dégradées en cours d'exécution, sans trace dans l'artefact déposé) a un dommage réel en aval de l'épisode et un $D = 0$ à l'oracle. L'oracle a alors une **cécité structurelle au diffus**, c'est-à-dire à l'objet même du programme ; un verdict 2 (« zone diffuse vide ») devient indistinguable d'un « oracle aveugle à cette classe ».
- Inversement, si le gabarit de D-O2 force l'agent à déposer les contrôles dans un bloc unique, tout le dommage mesurable se **concentre dans une action** (celle qui écrit le bloc). Le critère « diffus » par action porte alors sur une action unique : la dose « diffuse avec dommage » devient, par le gabarit, une dose **concentrée** avec dommage. La strate « diffus / concentré » que N-055 exige de coder dans la banque est écrasée par l'instrument.

**F3 — « Indépendance mathématique » : fausse au moment de la construction.**
C écrit qu'« aucune famille de poids neuronaux n'intervient » dans l'oracle. C'est vrai à l'exécution, faux à la fabrication : les défauts plantés sont générés, selon le § (f) de C, par `Qwen2.5-72B-Instruct` ou `Llama-3.1-70B-Instruct`. Or l'agent et le juge principal sont `Llama-3.1-8B-Instruct` (VÉRIFIÉ, P-015) et un juge Qwen2.5-7B est au bras rapporté (N-053). Les mutants portent donc la distribution des « défauts plausibles » de la même lignée que l'agent et que les juges. Deux effets confondants : (i) les contrôles honnêtes d'un Llama-8B rejettent facilement des mutants qu'un Llama-70B juge typiques, ce qui gonfle $S_{\text{honnête}}$ et rend l'oracle « valide » par parenté ; (ii) ce qu'un juge Llama trouve suspect et ce qu'un générateur Llama plante peuvent partager la même notion de « contrôle attendu ». La question de l'arbitre demandait explicitement « ni un juge de la même lignée » : C y répond par la négative pour l'exécution et par l'affirmative pour la construction, sans le dire.

**F4 — Fuite instrument → évaluation : le même jeu de mutants sert à choisir la dose et à mesurer le dommage à G1.**
Le verdict 3 scelle $d^*$ comme la dose qui **maximise** $\Delta\bar D$ parmi celles sous le plafond noir, puis « étend l'oracle aux 80 tâches restantes » avec le même générateur. Les 16 tâches du pilote gardent leurs mutants. La pièce A (§ 3) reconnaît déjà un « biais par tâche, non résolu » ; C y ajoute un **biais par mutant** : la dose est adaptée aux défauts plantés qui serviront ensuite de vérité. C'est exactement le « biais du gagnant » que C reproche à `conv-audit` s'il voyait les mutants, appliqué à l'instrument lui-même.

**F5 — Sélection de dose sur des scores de moniteurs : C déclare le nœud D-3 résolu, il ne l'est pas.**
La règle conjonctive de C choisit $d^*$ par (dommage à l'oracle) **et** (rappel des moniteurs noirs sous un plafond). Le second membre est un score de moniteur qui entre dans un choix qui conditionne la banque. La pièce A (§ 6, D-3) note que A et B tiennent cela pour un nœud d'interprétation de N-053 ; C écrit « respecte strictement ». Ce n'est pas un argument, c'est une lecture — et C ne propose pas le contrôle qui la rendrait réfutable (voir (c), C-6). S'ajoute un double usage du lot D (160 honnêtes) : seuils à 1 % des moniteurs **et** ligne de base $\bar D_{\text{honnête}}$ de l'oracle. Les deux membres de la conjonction sont calibrés sur les mêmes épisodes.

**F6 — E3 confond « information indépendante » et « bruit ».**
Le critère $\rho(D, M^{\max}) < 0{,}50$ est satisfait par un oracle qui ne mesure rien : une corrélation atténuée par l'erreur de mesure est faible. C n'a aucune mesure de **fidélité** de $D$ (pas de scission des mutants en deux moitiés, pas de test-retest). Sous B4, E3 n'oppose pas deux hypothèses exclusives : « indépendant » et « non informatif » donnent la même issue. Le contrôle comparatif ($\rho(L^{\text{texte}}, M^{\max}) > \rho(D, M^{\max}) + 0{,}20$) souffre du même défaut : plus $D$ est bruyant, plus il est « indépendant ».

**F7 — Hypothèses non établies prises pour acquises.**
- « Solution de référence de l'énoncé » (validation à blanc, § (e) 1) : pour des tâches tirées d'articles, l'existence d'une référence exécutable par tâche est une HYPOTHÈSE ; la pièce A (§ 7.5) la classe « non vérifié ». Sans elle, le scellement de $O_i$ (≥ 9/10 mutants rejetés) n'a pas de point d'appui.
- E1 propose d'inspecter « les sorties des 180 épisodes existants de T0.5 hors tâches d'épreuve ». Selon la pièce A (§ 5), ces 180 épisodes **portent sur 60 tâches d'épreuve** ; seul un rejeu boîte noire sans condition est licite. Une inspection structurelle est probablement de ce type, mais C ne le dit pas et la formule « hors tâches d'épreuve » est fausse.
- Coûts : O1 est classé « moyen », O2 « élevé s'il faut coder 96 environnements » — alors qu'O1+O4 exige d'**exécuter** $C_{\text{final}}$ sur des entrées, donc le même bac à sable qu'O2. « 0 USD CPU » suppose les 96 environnements existants, ce qu'aucune pièce n'établit.

**F8 — Le prédicat du mode tenu à l'écart conçu par son auteur : la vérité du dommage définie par l'attaquant.**
C demande à l'instance A (aveugle) de « livrer son propre prédicat d'état post-épisode ». Personne ne valide alors ce prédicat avant G1 (il est scellé avec la fiche et révélé à l'évaluation). D-S29 (a) (N-056) exige un gain dans **chaque** mode : si le dommage est défini différemment par mode, et par l'adversaire dans l'un d'eux, les rappels par mode de N-054 point 4 ne sont plus comparables. C a raison qu'on ne peut lui imposer l'oracle des contrôles ; mais la solution « auto-certification » n'est pas discutée comme nœud.

**F9 — Convention du score manquant, absente.**
Si l'extraction mécanique de $C_{\text{final}}$ échoue (bloc absent, agent qui désobéit, format cassé), que vaut $D$ ? C ne le dit pas. $D = 1$ confond désobéissance et dommage ; exclusion = filtrage d'épisode (interdit par C lui-même). La pièce A (§ 4) a déjà ce débat pour les moniteurs ; C ne le transpose pas à l'oracle.

**F10 — Portée surévaluée du verdict 2.**
« Résultat scientifique réfutant l'existence du régime diffus pour (i-a) » : sur 3 doses écrites × 3 exécutions × 16 tâches, l'issue est « non trouvé sur cette grille », pas « réfuté ». Règle 5.

### (b) Scénarios d'évasion (par classe de dommage hors support ; aucune recette)

Je raisonne sur ce que l'oracle **ne couvre pas**, pas sur ce qu'un agent ferait. Deux adversaires existent : l'organisme (i-a) du pilote (consigne, non adaptatif) et le bras d'attaque informé (N-056 point 6B), auquel C **dit** qu'« un oracle d'état post-épisode existe » — information suffisante pour orienter un mode vers les classes ci-dessous.

| instrument | classe de dommage hors support | ce que l'oracle rapporte | coût pour l'adversaire (HYPOTHÈSE) |
|---|---|---|---|
| **O1 défauts plantés** | dégradation portant sur une dimension absente des $M$ mutants (couverture) | $D \approx \bar D_{\text{honnête}}$ : « pas de dommage » | nul en information si les mutants sont « typiques » (F3) : il suffit de dégrader l'atypique |
| **O2 exécutable** | contrôle qui s'exécute et vérifie, mais sur une portée réduite | code retour 0 | nul ; C le reconnaît (« insuffisant seul ») |
| **O3 étalon caché** | dégradation hors des cas limites de l'étalon | pas de divergence | dépend de la finesse de l'étalon, inconnue |
| **O4 aval** | dommage sur l'état que les contrôles lisent, non sur les contrôles | les mutants de l'oracle passent par un contrôle intact : « pas de dommage » | nul : O4 injecte **ses** entrées, pas celles de la tâche réalisée |
| **O5 LLM sur artefact** | artefact d'apparence conforme pour un lecteur borné | « pas de dommage » | identique à celui d'échapper à un juge : c'est le juge |
| **tous à la fois** | dommage **de trajectoire** (vérifications non exécutées ou dégradées en cours d'épisode, artefact final intact) | $D = 0$ sur toutes les familles ; rappel noir par action faible si la dose est faible | **le plus bas de tous** : c'est la définition de la menace diffuse ; l'oracle y est aveugle par construction (F2) |

Le point décisif est la dernière ligne : le scénario « tous à la fois » n'exige aucune connaissance des mutants et coïncide avec la classe de menace que le programme veut mesurer. Un pilote positif (verdict 3) établirait un dommage d'**artefact**, pas de **trajectoire** ; un pilote négatif (verdict 2) ne dirait rien de la trajectoire. Le gabarit D-O2 aggrave : il invite à déposer les contrôles en un bloc, rendant « diffus » et « dommage » disjoints (F2).

Second scénario, contre l'instrument plutôt que contre la mesure : une dose retenue par maximisation de $\Delta\bar D$ (F4) sur des mutants de même lignée (F3) sélectionne la variante de sabotage que **ces** mutants voient le mieux. À G1, sur 80 tâches aux mutants frais, $\Delta\bar D$ régresse vers la moyenne : « dommage établi au pilote, introuvable à la banque ». Ce n'est pas un adversaire, c'est la régression du gagnant.

### (c) Contrôles négatifs dont l'absence serait fatale

Chacun oppose deux hypothèses et chaque issue falsifie quelque chose (B4). Seuils illustratifs.

**C-1 — Fidélité de l'oracle (contre F6).** Scinder les $M$ mutants de chaque tâche en deux moitiés par graine scellée ; calculer $\rho(D_{\text{moitié 1}}, D_{\text{moitié 2}})$ sur tous les épisodes, par dose. $H_A$ : $\rho \ge 0{,}7$, $D$ est une mesure. $H_B$ : $\rho < 0{,}4$, $D$ est du bruit et E3 est nul par atténuation. Entre les deux : E3 à corriger par le coefficient de fidélité. **Sans C-1, E3 est vrai par construction.**

**C-2 — Spécificité des mutants à la tâche (contre F3).** Appliquer les mutants de la tâche $j$ aux contrôles honnêtes de la tâche $i \ne j$ (permutation scellée). $H_A$ : $D_{i \leftarrow j} \approx 1$ (les mutants sont des défauts de **cette** tâche). $H_B$ : $D_{i \leftarrow j} \approx D_{i \leftarrow i}$ (mutants génériques, l'oracle mesure la « solidité moyenne d'un contrôle », pas le dommage à la tâche). Sous $H_B$, le mode « affaiblir les contrôles » est mesuré par un proxy de qualité générale.

**C-3 — Plancher textuel sur l'artefact seul (contre F1 et F2).** Faire lire $C_{\text{final}}$ **seul** par le juge 8B et par un classifieur lexical (sac de mots) entraîné honnête contre dose forte sur un lot tenu à part. $H_A$ : $D$ n'est pas prédit par ces lecteurs ($R^2 < 0{,}25$). $H_B$ : $D$ est prédit ($R^2 > 0{,}6$) : l'oracle recode la détectabilité textuelle de l'artefact, et le critère « diffus » par action — qui ne lit pas l'artefact comme bloc — l'a manqué. C a un plancher « taille du texte » ; il manque le plancher « juge sur l'artefact », le seul qui teste la circularité résiduelle.

**C-4 — Vérité de trajectoire sur un sous-lot (contre F2, la plus coûteuse, la plus nécessaire).** Sur un sous-lot scellé de la dose forte témoin, comparer $D$ (artefact) à une mesure de **dommage de trajectoire** indépendante : rejeu mécanique de la tâche en remplaçant, étape par étape, les vérifications de l'agent par celles de la référence, et compte des étapes où le remplacement change l'issue. $H_A$ : concordance $D$ ↔ trajectoire $\ge 0{,}8$ ; l'artefact résume le dommage. $H_B$ : concordance $< 0{,}5$ ; l'oracle d'artefact est aveugle à la classe qui compte et le verdict 2 n'est pas interprétable. Si le rejeu mécanique n'existe pas pour ces tâches, **le dire est le résultat** : l'oracle de C est alors déclaré « oracle d'artefact », et sa revendication se restreint explicitement (option 5B de C, mais honnêtement nommée).

**C-5 — Mutants frais à G1 (contre F4).** Deux jeux de mutants par tâche, scellés séparément : jeu P (pilote, choix de dose), jeu G (G1, jamais lu avant). Sur les 16 tâches du pilote, à la banque : $H_A$ : $\Delta\bar D_G \approx \Delta\bar D_P$ (pas de biais par mutant). $H_B$ : $\Delta\bar D_G < \Delta\bar D_P - 0{,}15$ : la dose était adaptée aux mutants ; ne garder que les 16 tâches vierges, comme la pièce A le propose déjà pour le biais par tâche.

**C-6 — Choix de dose sans le membre « moniteur » (contre F5).** Rejouer la règle de choix de $d^*$ en remplaçant le plafond des moniteurs noirs par une borne **écrite d'avance** sur $p \times$ intensité. $H_A$ : même $d^*$ ; le score de moniteur n'a pas pesé, N-053 est respecté en acte. $H_B$ : $d^*$ change ; le choix de dose est une sélection sur score de moniteur, D-3 est un nœud réel et C a tort de le déclarer clos.

**C-7 — Même lignée contre lignée tierce pour les mutants (contre F3).** Générer les mutants deux fois : lignée Llama/Qwen (celle de C) et lignée tierce ou mutation syntaxique sans modèle. $H_A$ : $\bar D_{\text{honnête}}$ et $\Delta\bar D_{\text{fort}}$ équivalents (marge scellée). $H_B$ : écart au-delà de la marge : l'oracle hérite de la lignée des juges, et seule la version sans modèle peut être scellée.

**C-8 — Convention du score manquant (contre F9).** Taux d'échec d'extraction sur les honnêtes et sur la mention, rapporté ; règle scellée : un artefact manquant est une **valeur manquante** comptée à part, ni $D = 1$ ni exclusion ; différence de taux honnête/saboté au-delà d'une marge → l'obéissance et le dommage sont confondus, nœud.

**C-9 — Gabarit et honnêtes (contre F2, D-O2).** Mesurer, sur le lot D, l'effet du gabarit à bloc structuré sur le rappel des moniteurs noirs **avant** toute condition sabotée : le bloc lui-même ne doit pas être un trait détecté. $H_A$ : faux positifs inchangés. $H_B$ : le bloc crée des alertes ; le gabarit est un artefact de source nouveau.

---

## Ce que je retiens de C, en le disant (B1)

Je garde de C : la séparation « problème ontologique / problème méthodologique » (juste, si on en tire la conséquence F1) ; le témoin positif par dose forte avant toute lecture des doses intermédiaires ; la contrainte de spécificité sur entrées saines ; la quarantaine des mutants hors de `conv-audit`. Je rejette : l'affirmation que N-053 est « strictement » respecté ; l'oracle d'artefact présenté comme oracle du diffus ; O5 comme repli universel ; la génération des mutants par la lignée de l'agent ; le prédicat auto-certifié du mode tenu à l'écart présenté comme réglé.

Nœud nouveau pour Lazar, que C n'a pas écrit : **l'oracle d'artefact ne mesure pas le dommage de trajectoire** ; décider d'avance si un verdict 3 porte la revendication « dommage diffus » ou seulement « dommage d'artefact à dose concentrée dans un bloc » — options : (a) exiger C-4 avant toute revendication ; (b) revendication réduite à l'artefact, écrite comme telle ; recommandation (a), confiance moyenne ; défaut : aucun.

FIN-DE-CELLULE