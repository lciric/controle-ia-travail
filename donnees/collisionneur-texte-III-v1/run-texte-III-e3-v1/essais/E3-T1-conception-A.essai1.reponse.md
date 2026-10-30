# Proposition A — tour III.1 (conception à l'aveugle)

Périmètre respecté : rien ici ne décrit une famille, une conduite ou un moyen ; tout porte sur des lois de probabilité, des estimateurs et des plans de mesure. Les références sont attribuées quand je peux le faire ; sinon « référence à vérifier ».

## (a) Ce que la question suppose sans que ce soit établi

1. Qu'une « réussite » ou un « échec » de la défense soit déjà défini et mesurable **par élément** d'une famille — HYPOTHÈSE (aucune définition dans les faits).
2. Que chaque famille produise **plusieurs éléments** mesurables, condition de la variance à deux niveaux — HYPOTHÈSE.
3. Qu'il existe une **population de familles** dotée d'une loi de tirage ; les faits (9) notent que les familles sont découvertes, pas tirées — HYPOTHÈSE pour la loi, VÉRIFIÉ pour la réserve.
4. Que les deux sources soient indépendantes — HYPOTHÈSE (le contexte dit « en apparence »).
5. Que l'appariement soit exact — OBSERVÉ-NON-AUDITÉ (lecteur unique, même lignée qu'une source, fait 6).
6. Que les comptes 28 et 25 soient exprimés dans la **même unité** — faux au sens strict : le fait 7 montre deux unités (34 ou 35 familles) — VÉRIFIÉ.
7. Que la population soit fermée pendant la mesure — HYPOTHÈSE.
8. Que le banc à deux régimes (aveugle, informé) soit réalisable sans dépense — VÉRIFIÉ pour la décision N-056, HYPOTHÈSE pour la réalisabilité.
9. Que les bancs publics fournissent des trajectoires étiquetables sous licence compatible — HYPOTHÈSE (fait 11).
10. Que cinq instances « de fournisseurs différents » soient indépendantes au sens des données d'entraînement — RAPPORTÉ pour la décision, HYPOTHÈSE pour l'indépendance.
11. Que le budget d'évaluation (éléments, calcul) soit connu — absent des pièces ; tout chiffre sera illustratif.

## (b) Duels décisifs sur estimateurs et définitions

**Duel 1 — Lincoln-Petersen contre bornes de Chao.**
H_A : les sources sont homogènes et indépendantes ; Lincoln-Petersen (LP) est approximativement sans biais pour N. H_B : hétérogénéité de capturabilité ou dépendance positive ; LP sous-estime, seules des bornes inférieures (Chao) sont défendables.
Métrique : avec une troisième source (tour III ou première instance scellée), les trois estimateurs LP par paire et l'ajustement d'un modèle log-linéaire avec terme d'interaction par paire (Fienberg, 1972, *The multiple recapture census for closed populations and incomplete 2^k contingency tables*). Seuil : test du rapport de vraisemblance du terme d'interaction, p < 0,05, ou écart entre estimations par paire supérieur à deux écarts types de Chapman (illustratif).
Contrôle négatif : mondes simulés à captures indépendantes et équiprobables, où le terme d'interaction doit être rejeté à moins de 5 % des réplicats ; sinon le code est faux.
Issues : interaction significative et estimations par paire discordantes → H_A falsifiée, on publie une borne inférieure. Interaction nulle et concordance → H_B falsifiée à la magnitude détectable (puissance à déclarer).

**Duel 2 — Borne « zéro échec » contre effectif efficace réduit par les grappes.**
H_A : la borne n ≥ ln α / ln(1 − ε) (fait 9) couvre la vraie part d'échec à 95 % dans les mondes où les familles sont groupées en grappes corrélées. H_B : la dépendance intra-grappe réduit l'effectif efficace et la couverture tombe sous 90 %.
Métrique : couverture empirique sur 10 000 mondes simulés (illustratif) à part d'échec ε₀ connue, corrélation intra-grappe ρ et nombre de grappes variés. Seuil : couverture < 0,90 falsifie H_A ; couverture ≥ 0,95 pour tout ρ ≤ ρ_max déclaré falsifie H_B sur cette plage.
Contrôle négatif : ρ = 0, où la couverture doit valoir ≥ 0,95 exactement selon la loi binomiale.

**Duel 3 — Appariement reproductible contre appariement lié à la lignée.**
H_A : trois lecteurs de lignées différentes, aveugles à la source, avec la même grille fermée, reproduisent l'appariement (κ de Fleiss ≥ 0,8, illustratif). H_B : κ < 0,6 et l'intervalle des N recalculés par lecteur dépasse l'écart type de Chapman.
Contrôle négatif : un jeu d'appariement synthétique à correspondance connue, où les trois lecteurs doivent atteindre κ ≥ 0,9.
Issues : κ faible → l'estimation de N devient un intervalle entre lecteurs, pas un point ; κ fort → l'objection « lecteur de même lignée » est écartée à ce niveau.

**Duel 4 — Population fermée contre population ouverte.**
H_A : la courbe d'accumulation (familles nouvelles par source ajoutée, ordre permuté) décroît et son extrapolation converge. H_B : le taux de nouveauté reste constant sur cinq sources.
Métrique : pente des deux dernières occasions sur la pente des deux premières ; seuil 0,5 (illustratif). Contrôle négatif : mondes simulés à N fini où la pente doit décroître. Issue : pente constante → tout N est caduc, on passe à une estimation de **taux** de découverte.

## (c) Mesure minimale des deux instruments

Les instruments sont l'**estimateur du nombre de familles** et la **mesure d'universalité**. Les « taux de détection / fausses alertes » du gabarit du tour s'y traduisent ainsi : déclarer l'universalité quand elle est fausse (fausse alerte au sens de la revendication) et ne pas la déclarer quand elle est vraie (défaut de détection).

*Estimateur de N.* Sur des mondes simulés à N connu (grille : N ∈ {30, 50, 100}, k sources ∈ {2, 3, 5}, hétérogénéité beta, dépendance par paire ; illustratif) : biais relatif, erreur quadratique, couverture de l'intervalle à 95 %. Base à battre : le compte brut S_obs, dont le biais vaut −(N − S_obs) et la couverture 0 dès que N > S_obs. Critère : |biais| < |biais de S_obs| et couverture ≥ 0,90 dans au moins 80 % des scénarios déclarés (illustratif).

*Mesure d'universalité.* Mondes appariés : d'un côté une défense vraiment universelle (ε = 0), de l'autre une défense à ε₀ ∈ {0,02 ; 0,05 ; 0,10}, même nombre de familles et d'éléments. Couverture de la borne sur ε ≥ 1 − α ; puissance = part des mondes à ε₀ où l'énoncé d'universalité est refusé. Base à battre : la proportion brute observée sans intervalle. Les deux instruments sont jugés sur des mondes où l'on contrôle la loi de découverte ; rien de plus.

---

## Bloc 1 — Quatre propositions préalables

### (a) Définition opérationnelle de l'universalité

**Option 1 — pire cas sur une classe déclarée.** À déclarer : la classe C (énumérée ou définie par un générateur), la métrique par famille M(f), le seuil τ, le protocole d'agrégation des éléments. Énoncé : « ∀ f ∈ C, M(f) ≥ τ ». N'autorise rien hors de C ; si C est définie par un générateur, le quantificateur n'est tenable qu'avec un échantillonnage dont la loi est déclarée, et l'énoncé redevient probabiliste. Vérification par un tiers : il rejoue M sur chaque f de C scellée. Faiblesse : fragile à une seule famille ; dépend entièrement de la qualité de C.

**Option 2 — écart vues / tenues à l'écart.** À déclarer : les deux ensembles (le second scellé), la statistique d'écart Δ = M̄_vues − M̄_écart, la tolérance δ, l'intervalle. Énoncé : « Δ ≤ δ avec confiance 1 − α ». Autorise une affirmation de **transfert**, pas de niveau absolu : une défense uniformément médiocre a Δ ≈ 0. Vérification : le tiers détient les scellés, compare les empreintes et rejoue.

**Option 3 — proportion ou quantile.** À déclarer : la loi G sur les familles (ou le mécanisme de découverte tenant lieu de loi), τ, ε, α, la règle d'arrêt. Énoncé : « avec confiance 1 − α, P_{f∼G}(M(f) < τ) ≤ ε ». Autorise une revendication quantifiée ; n'autorise rien sur une famille particulière ni hors de G. Vérification : le tiers vérifie que les familles ont été produites par le mécanisme déclaré avant la mesure (horodatage, scellés) et refait le calcul du fait 9 ou son équivalent.

**Option 4 — modèle hiérarchique.** M(f) suit une loi à effets aléatoires (par exemple logit-normale) estimée sur les familles vues ; l'énoncé porte sur la queue prédictive pour une famille nouvelle de même mécanisme. Autorise une prédiction scellée vérifiable ; suppose la forme de la loi, ce qui doit être soumis à analyse de sensibilité.

**Recommandation.** Option 3 pour la revendication centrale, assortie de l'option 2 comme test de transfert et de l'option 4 pour produire des prédictions scellées. L'option 1 n'est tenable que pour la liste finie des familles effectivement scellées.

**Classe déclarée contre inconnu.** « Universelle sur la classe déclarée » est un énoncé sur G. « Robuste à l'inconnu » n'est pas un énoncé mesurable : il n'a de contenu que relativement à un mécanisme de découverte dont on estime la **couverture** (masse manquante, bloc 1(d)). On peut donc écrire : « sur les familles produites par le mécanisme D, part d'échec ≤ ε ; la couverture estimée de D vaut ĉ ». La différence 1 − ĉ est l'aveu quantifié de ce qui reste hors portée. Toute formulation qui efface ce reste est à écarter.

### (b) Régime d'information

Deux bras (décision N-056, VÉRIFIÉ) : **aveugle** (le banc ignore l'existence et la forme de la défense) et **informé** (il connaît le protocole et les seuils, non les paramètres entraînés — HYPOTHÈSE quant à la granularité). Catégories d'information, chacune avec un bit déclaré « accessible / scellé » : existence de la défense ; liste des familles vues ; protocole de mesure ; seuils de décision ; résultats intermédiaires. L'écart de performance entre bras est lui-même une statistique à préenregistrer : s'il dépasse une tolérance déclarée, la mesure aveugle est suspecte d'optimisme.

Budget : nombre de familles n_f et d'éléments par famille n_e fixés par la simulation du bloc 1(c), plus un budget de calcul déclaré en heures-GPU (bloc (d), illustratif). Rapport par palier : palier 1 — mesures sur familles vues, seuils gelés ; palier 2 — familles tenues à l'écart du programme ; palier 3 — familles des cinq instances ; aucune modification de seuil après le palier 1, et toute analyse hors préenregistrement est étiquetée exploratoire.

Interdits entre construction et évaluation : contenu des familles scellées ; résultats par famille du palier 2 avant gel ; toute itération sur les paliers 2 et 3 ; le choix des seuils à partir d'un retour du banc. Le mode tenu à l'écart de la conception des moniteurs (N-054, VÉRIFIÉ) en est l'exemple existant.

### (c) Combien de familles, par simulation

Énoncé cible : avec confiance 1 − α, la part de G où M(f) < τ est ≤ ε.

Modèle génératif à déclarer : (i) familles groupées en K grappes ; (ii) probabilité d'échec par famille p_f tirée d'une loi beta dont les paramètres dépendent de la grappe (hétérogénéité) ; (iii) éléments d'une famille tirés en Bernoulli(p_f) ; (iv) corrélation intra-grappe ρ. Variance à deux niveaux : la variance de la proportion observée s'écrit comme somme de la composante entre familles et de la composante entre éléments divisée par n_e ; au-delà d'un n_e modeste, c'est le nombre de familles qui gouverne. L'effet de plan 1 + (m̄ − 1)ρ réduit l'effectif efficace de n_f à n_f / (1 + (m̄ − 1)ρ), m̄ étant la taille moyenne des grappes.

Repère chiffré (fait 9, VÉRIFIÉ) : 29, 59 et 149 familles sans échec pour ε = 0,10 ; 0,05 ; 0,02. Avec les 34 familles observées et zéro échec, la borne atteinte serait ε ≈ 0,084 (calcul 1 − 0,05^{1/34}, à refaire), et plus élevée dès que ρ > 0. Autrement dit, ε = 0,05 est hors de portée du stock actuel ; la revendication doit être formulée à ε = 0,10 ou attendre la découverte.

Règle d'arrêt séquentielle : suite de confiance (plutôt qu'un test à n fixe) permettant d'arrêter dès que la borne sur ε passe sous la cible ou dès qu'un échec la rend inatteignable ; référence à vérifier pour une suite de confiance adaptée aux proportions. Analyses de sensibilité : ρ ∈ {0 ; 0,1 ; 0,3}, K ∈ {3 ; 6 ; 12}, loi beta plus ou moins dispersée, n_e ∈ {10 ; 30} (illustratif).

Ce que la simulation démontre : la couverture et la puissance de la règle **sous les modèles déclarés**. Ce qu'elle suppose : que le mécanisme de découverte engendre une loi G stable et que les grappes réelles ressemblent aux grappes simulées. Les familles étant découvertes, la garantie porte sur « les familles que ce mécanisme découvre », et la fraction non couverte est estimée au bloc 1(d), pas ici.

### (d) Combien de familles encore inconnues

**Vérification.** 28 × 25 / 18 = 38,89 ; / 19 = 36,84. Chapman : 29 × 26 / 19 − 1 = 38,68 ; / 20 − 1 = 36,70. Les quatre valeurs du contexte sont exactes.

**Convention défendable.** Aucune des deux telle quelle : chacune mélange les unités, puisque n₁ est compté en unités d'Argon et n₂ en unités d'Opus. Il faut fixer la granularité avant de compter. En unités d'Opus (fines) : n₁ = 29, n₂ = 25, m = 19 → LP 38,2, Chapman 38,0. En unités d'Argon (grossières) : n₁ = 28, n₂ = 24, m = 18 → LP 37,3, Chapman 37,2 (calculs à refaire, formules données). L'écart type de Chapman vaut environ 2,7 (m = 18) et 2,2 (m = 19) ; l'écart entre conventions est inférieur à un écart type. La convention fine est préférable : fusionner détruit de l'information, scinder la conserve, et c'est la convention qui sera la plus proche de ce qu'une grille fermée peut rejouer.

**Hypothèses et sens des biais.**
- *Population fermée* : si de nouvelles familles apparaissent entre occasions, N n'est pas défini ; voir plus bas.
- *Indépendance des sources* : une dépendance positive (deux modèles entraînés sur des corpus voisins trouvent les mêmes familles) gonfle m et **sous-estime** N ; une dépendance négative, improbable ici, le surestime. Avec deux sources, l'indépendance est **non identifiable** ; aucun test interne n'existe.
- *Équiprobabilité de capture* : des familles faciles capturées deux fois et des familles difficiles jamais produisent le même effet qu'une dépendance positive : **sous-estimation**. Les bornes de Chao sont conçues pour ce cas (Chao, 1984, *Nonparametric estimation of the number of classes in a population*).
- *Appariement exact* : des fusions abusives gonflent m et sous-estiment N ; des correspondances manquées dégonflent m et surestiment N. Un lecteur de la lignée d'une source risque le premier sens.

Les trois premiers effets vont dans le même sens : LP et Chapman sont ici à lire comme des **bornes inférieures** ; 37 à 39 est un plancher plausible, pas un centre.

**Estimateurs avec plusieurs sources.**
- Chao2 pour données d'incidence : S_obs + ((T − 1)/T) · Q₁(Q₁ − 1) / (2(Q₂ + 1)), Q₁ familles vues une fois, Q₂ vues deux fois. Ici Q₁ = 16, Q₂ = 18 (unités d'Argon), T = 2 : ≈ 37,2 (calcul à refaire), borne inférieure peu informative à deux sources ; elle prend son sens à cinq.
- Good-Turing : couverture ĉ = 1 − Q₁ / (somme des incidences) = 1 − 16/53 ≈ 0,70 (calcul à refaire) : près de 30 % de la masse d'incidence est portée par des singletons, signe d'un stock loin d'être épuisé (Good, 1953, *The population frequencies of species and the estimation of population parameters*).
- Modèles log-linéaires sur la table 2^k (Fienberg, 1972) : avec k ≥ 3, les interactions par paire deviennent estimables ; l'interaction d'ordre k reste non identifiable et doit être déclarée nulle ou bornée.
- Modèles M_h, M_t, M_th à classes latentes (Otis, Burnham, White et Anderson, 1978, *Statistical inference from capture data on closed animal populations*).
- Approche bayésienne : loi a priori sur N (par exemple uniforme tronquée ou de Jeffreys) et sur les probabilités de capture, avec sélection de modèle ; produit un intervalle crédible qui intègre l'incertitude de modèle.

**Test d'indépendance.** Impossible à deux sources ; à k ≥ 3, test du rapport de vraisemblance des termes d'interaction ; à cinq, comparaison des modèles par critère d'information, avec sensibilité à l'interaction d'ordre supérieur fixée.

**Refus commun.** Une censure identique sur toutes les sources est une cellule « jamais capturée » structurelle : aucun estimateur de recapture ne la voit. Traitement : déclarer la classe censurée hors de la population revendiquée, consigner le refus tel quel (fait 14, VÉRIFIÉ), et borner la revendication par « parmi les familles que des sources de ce type acceptent d'énumérer ».

**Population ouverte.** Si le duel 4 montre un taux de nouveauté stable, N devient N_t ; on publie un taux de découverte par source ajoutée et son intervalle, et la revendication d'universalité devient indexée par la date et le nombre de sources ; la couverture de Good-Turing reste définie et devient la statistique principale.

## Bloc 2 — Données de départ à recommander

Principe : seules des données brutes, étiquetables par un lecteur à grille fermée, produites hors du programme, servent de familles extérieures ou d'occasion de capture supplémentaire. Le fait 11 (HYPOTHÈSE) n'a pas été vérifié ; ce qui suit l'est encore moins.

- **SHADE-Arena** : je crois qu'il s'agit d'un banc publié en 2025 par des auteurs d'Anthropic — référence à vérifier. Format, licence et niveau d'étiquetage : non connus de moi de façon fiable. Indépendance vis-à-vis du programme : forte en apparence, mais sa lignée est celle de deux des quatre modèles du collisionneur (fait 13), ce qui crée une dépendance de corpus à déclarer. Recouvrement avec l'entraînement des modèles de 8 et 70 milliards : à mesurer par test d'appartenance ; non vérifié.
- **ControlArena** : je crois qu'il s'agit d'un cadre logiciel ouvert d'un institut public britannique — référence à vérifier ; licence et format exacts non connus de moi. Avantage attendu : trajectoires rejouables ; coût de mise au format moyen (illustratif).
- **MonitoringBench, SLEIGHT-Bench, Liars' Bench** : je ne peux ni les décrire ni les attribuer ; présence du nom seulement dans les pièces (fait 10). Je ne les recommande pas avant lecture.

- **Journaux de refus (ii)** : indépendance nulle (produits par le programme) ; valeur pour la censure commune (bloc 1(d)) : ils permettent d'estimer la part de questions refusées et donc la taille de la classe censurée ; usage en recapture : non, pas une source d'énumération.
- **Propositions brutes d'une course précédente (iii)** : indépendance partielle (mêmes lignées) ; étiquetables par la grille ; utilisables comme **occasion de capture supplémentaire** à condition de dater et de sceller les empreintes avant appariement ; risque : contamination des défenses déjà conçues avec ces propositions.

Recommandation : (iii) comme troisième occasion de capture immédiate, (i) après vérification de licence et d'étiquetage, (ii) seulement pour la censure.

## Bloc 3 — Questions candidates pour le texte III

**Q1 — Estimer la couverture du mécanisme de découverte avec k ≥ 3 sources et la confronter à une prédiction scellée.**
1. Avantage : transforme « robuste à l'inconnu » en masse manquante estimée ; produit un nombre réfutable.
2. Piège : sources dépendantes par corpus commun → sous-estimation systématique de la masse manquante présentée comme couverture élevée.
3. Validation : prédiction scellée du nombre de familles inédites que livreront les cinq instances, intervalle de prédiction à 90 % ; si le compte observé sort de l'intervalle, le modèle de recapture est faux (5 sources, environ 25 à 35 familles chacune, illustratif).
4. Risque hors périmètre : faible ; la question ne manipule que des comptes et des tables d'incidence.

**Q2 — Mesurer l'écart vues / tenues à l'écart à deux niveaux, contre une prédiction scellée du niveau tenu à l'écart.**
1. Avantage : vérifiable par un tiers détenant les scellés ; sépare biais de sélection et niveau.
2. Piège : seuils ajustés après un premier regard sur les familles scellées ; ou n_e trop faible, qui noie l'écart dans la variance intra-famille.
3. Validation : au moins 15 familles tenues à l'écart (illustratif), tolérance δ fixée à l'avance ; revue extérieure des empreintes.
4. Risque : moyen, car la métrique M touche à la défense ; borné en ne publiant que des statistiques agrégées par famille.

**Q3 — Borner la part d'échec ε en corrigeant la dépendance par un effectif efficace déclaré.**
1. Avantage : énoncé probabiliste explicite, directement comparable au fait 9.
2. Piège : grappes définies après coup pour minimiser l'effet de plan ; ρ non estimable à moins de plusieurs familles par grappe.
3. Validation : couverture vérifiée sur mondes simulés (duel 2) puis sur les familles extérieures, où la part d'échec observée doit rester sous la borne annoncée ; cible ε = 0,10 avec 34 familles, ε = 0,05 avec 59 (fait 9, VÉRIFIÉ).
4. Risque : faible ; pure statistique de proportion.

**Q4 — Valider la reproductibilité de l'appariement et sa propagation dans N.**
1. Avantage : traite la faiblesse connue (lecteur unique, même lignée, fait 6) par une mesure, pas par un argument.
2. Piège : lecteurs non aveugles à la source ; grille révisée entre lecteurs.
3. Validation : trois lecteurs de lignées distinctes, κ ≥ 0,8 (illustratif), N publié comme intervalle entre lecteurs ; revue extérieure de la grille.
4. Risque : moyen ; la grille d'appariement frôle la description de familles. Bornage : seule la grille de **codage** (attributs formels) est publiée, jamais les contenus.

**Q5 — Mesurer l'écart entre bras aveugle et informé comme détecteur de fuite construction/évaluation.**
1. Avantage : exploite le banc déjà décidé en deux versions (N-056) ; l'écart est une statistique de contrôle qui ne coûte rien de plus.
2. Piège : les deux bras partagent les mêmes familles, donc un écart nul peut signifier une fuite commune plutôt qu'une absence de fuite.
3. Validation : prédiction scellée « écart ≤ δ », vérifiée séparément sur les familles des cinq instances ; δ illustratif à fixer par simulation.
4. Risque : élevé si l'on décrit ce que « informé » contient ; borné en ne déclarant que les catégories d'information du bloc 1(b).

## Bloc 4 — Organisation des cinq instances

**Consigne.** Options : identique à toutes ; différentes par instance ; identique plus une variante scellée tirée au sort. Avantage de l'identique : occasions de capture comparables, condition des modèles M_t. Inconvénient : maximise la dépendance par corpus. Recommandation : consigne identique, gelée par empreinte, suivie d'une seconde passe avec une consigne complémentaire également scellée, ce qui donne dix occasions au lieu de cinq et permet d'estimer l'effet d'occasion. Confiance : moyenne.

**Fuites entre instances.** Options : sessions séparées sans contexte partagé ; opérateurs humains distincts ; engagement par empreinte avant toute lecture. Recommandation : les trois ; chaque sortie est hachée et horodatée avant d'être ouverte, aucune sortie n'est lue par un humain avant que les cinq (ou les refus) soient scellées ; l'ordre d'exécution est tiré au sort et consigné. Confiance : élevée pour le scellement, faible pour la fuite par corpus commun, qu'aucune procédure n'élimine.

**Appariement sans lecteur unique.** Options : un lecteur ; trois lecteurs de lignées différentes ; comparaison mécanique (similarité déclarée) comme témoin. Recommandation : grille fermée publiée avant l'ouverture des scellés ; trois lecteurs aveugles à la source ; κ rapporté ; N publié sous forme d'intervalle (minimum et maximum sur lecteurs) ; la méthode mécanique sert de témoin négatif, non d'arbitre. Si une famille d'une instance en recouvre plusieurs d'une autre, la granularité fine est retenue (bloc 1(d)). Confiance : moyenne.

**Test d'indépendance.** Avec cinq sources : modèles log-linéaires et sélection par critère d'information (bloc 1(d)). Pour la corrélation de corpus entre fournisseurs : HYPOTHÈSE — mesurer, sur une batterie d'énumération **sans rapport avec le sujet**, le recouvrement par paire des listes produites ; ce taux sert de loi a priori sur l'interaction par paire dans le modèle. Avantage : estimable avant ouverture des scellés ; inconvénient : la corrélation sur un sujet neutre n'est pas celle sur le sujet d'intérêt. Confiance : faible.

**Sources multiples pour N.** Table 2⁵ à 31 cellules observées ; Chao2 comme borne inférieure ; modèles M_h, M_th ; variante bayésienne pour l'intervalle ; Good-Turing pour la couverture. Prédiction scellée avant ouverture de la cinquième instance : nombre de familles inédites attendues de celle-ci, calculé sur les quatre premières ; c'est le test le moins coûteux du modèle. Confiance : élevée sur la procédure, moyenne sur les hypothèses.

**Refus d'une instance.** Le refus est consigné tel quel et définitif (fait 14, VÉRIFIÉ) ; au plus trois consignes de repli plus étroites, scellées d'avance (fait 16, VÉRIFIÉ pour le protocole de bisociation ; HYPOTHÈSE pour son extension ici). Le refus est traité comme une source **absente**, jamais comme zéro capture ; l'estimation se fait sur les sources restantes, avec k ≥ 3 exigé. Un refus commun à toutes désigne une classe censurée, exclue de la revendication et déclarée. Option : sixième fournisseur de réserve prédésigné — HYPOTHÈSE. Confiance : élevée.

## (d) Ancrage matériel

Modèles ouverts de 8 et 70 milliards de paramètres (RAPPORTÉ). Les simulations de couverture (duels 1, 2 ; (c)) tournent sur processeur ordinaire : quelques heures, coût négligeable (illustratif). Les mesures M(f) sur n_f ≈ 35 à 60 familles et n_e ≈ 30 éléments représentent environ 1 000 à 2 000 passes d'inférence par modèle ; sur le 70 milliards, de l'ordre de quelques dizaines d'heures-GPU, soit quelques centaines d'euros en location (illustratif). Le banc en deux versions est monté sans dépense (N-056, VÉRIFIÉ).

FIN-DE-CELLULE