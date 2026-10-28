# Synthèse du collisionneur « agents sur le noyau pendant la conception par essais-erreurs » (étage III) et de la réponse reformulée d'Opus — v1

Écrite le 2026-10-26 à 04:04 (temps universel, lu sur `date -u`) pour Lazar par un sous-agent neuf, sur le brief de conv-audit
(`95014839…`) mis à jour à 03:38. Empreintes vérifiées (`LISEZMOI-sortie-v1.md`) ; cellules refusées ni fournies ni
supposées. A Claude Fable, C Gemini Argon, B Claude Opus ; T1 conception, T2 équipe rouge, T3 riposte ; B′ Opus sur la
question reformulée. Rien d'opposable (R7) ; chiffres des modèles illustratifs sauf raisonnement explicite ; « refait » :
arithmétique refaite ici ; aucun trait de classement des tâches recopié.

## 1. En trois lignes
1. **Convergences** : à une course par objet, seul un écart non apparié ≥ ≈ 0,20 (36 tâches) ou ≈ 0,25 (24) sort du bruit des
   tâches (refait) et 3 graines ne mesurent pas utilement la variance entre graines ; la boucle (4) dérive par défaut, sans
   fraude, vers un indice de surface stable que ni journal, ni relecture, ni canari ne voit (admis par A et C) ; un gain
   d'outils ne se lit que contre un témoin à dépense égale, après des essais du noyau.
2. **Divergences** : l'ordre (B′ : outils avant (4), jugée « négative par défaut ») ; une réserve dans les 60 tâches (C seul) ;
   un facteur à la fois (A non, C un changement majeur, B′ plan factoriel).
3. **Tours II et III** : tombent les seuils sur 3 graines, la scission 48/12, l'outil vide en témoin, la permutation lue par un
   humain, l'arrêt sur succès, Thresholdout, le pré-vol court ; entrent l'audit de banque, la comparaison A contre A (deux
   copies d'un organisme), la banque sœur v3-bis, l'ablation du contenu, le journal des lectures, `test_final` lu une fois.

## 2. Par point de la question
**(1) Lectures.** A (T1-A) : axes non commensurables, seule (1) change l'objet ; manquent réplication, permutation, canari.
C (T1-C) : (4) puis (1) ; (2) pré-vol bon marché ; (3) hors de portée de la relecture. B′ : (1) seule touche le fond, confondue
avec le calcul ; (4) « moteur du sur-apprentissage ». Rouge → riposte : pré-vol trop court → longueur et profondeur maximales ;
essai de (2) asymétrique (0 sur 6 laisse ≈ 0,39, refait) → unilatéral. **Survit** : (2) et (3) sont des instruments à
qualifier ; l'avis de conv-audit sur eux n'est ni établi ni réfuté (T3-A).
**(2) Essais-erreurs.** A : journal, compteur, 48/12. C : partition 20/40, Thresholdout, arrêt sur gain. B′ : facturation,
plan factoriel, ≤ 10 lectures, aucune recoupe, garanties formelles vides à 60 tâches (≈ 0,24 pour 20 lectures, refait).
Rouge → riposte : 48/12 fuit, sans puissance (≈ 0,35, refait) → v3-bis ; permutation reconnue → sans humain ; arrêt sur
succès (≈ 0,34 sur 8 regards indépendants, refait) → horizon fixe ; journal → lectures aussi. **Survit** : § 3.
**(3) Bruit.** A : 3 graines. C : appariement, Brier. B′ : tâches × exécutions, estimand. Rouge → riposte : √2 oublié (A) →
reconnu ; 2 degrés de liberté → unilatéral (A), désaccord par tâche (C) ; McNemar aveugle aux graines, règle dégénérée → A
contre A, références à dépasser. **Survit** : § 5.
**(4) Outils.** A : code sans réseau, recherche par le noyau. C : processus éphémère, vote en témoin. B′ : index figé, plafonds
de l'hôte. Rouge → riposte : dépense inégale, outil vide, injection, état persistant → quatre bras (outillé ; retour plausible
non informatif ; vote à passes et jetons égaux ; appel simple), injection plantée. **Survit** : § 4.
**(5) Connu.** Listes recoupées ; T2-A juge celles de C justes, sans vérifier. **Survit** : § 6.
**(6) Départager.** A : graines, transfert, itérer contre répliquer. C : filet apparié, bruit d'abord, outils parallèles.
B′ : confirmation seule, conception protégée, tâches plutôt que graines. **Survit** : rien ne se lit avant le bruit
d'exécution mesuré ; ajouts au pilote 4 caducs.

## 3. Pour la boucle extérieure
- **Journal** : avant lecture, empreintes (code, noyau, banque), graine, coût, attente chiffrée (famille, sens, taille en
  erreurs types), refusée sans nombre (T3-A) ; échecs compris (T1-C) ; traces ouvertes consignées, sinon pas de lancement
  (T2-B, T3) ; rapproché de la facturation (B′).
- **Arrêt** : compteur et budget fixés d'avance, « plateau » écrit comme réponse négative (T2-A, T3) ; futilité (B′) ; faux
  arrêts de la règle mesurés sur copies identiques (T2-B).
- **Facteurs** : noyau, banque, modèles fixes ; un changement majeur (C), plan factoriel (B′).
- **Sur-ajustement** : v3-bis (même générateur, tâches neuves, faite d'avance par qui n'a rien lu, lue une fois) sépare
  l'adaptation aux 60 textes, au générateur, à la famille (T3-A) ; ablation du contenu, forme gardée (T2-C) ; plancher :
  étiquettes permutées itérées sans humain ; boucle éprouvée sur copies identiques (≤ 5 % d'« améliorations ») et sélections
  rejouées hors ligne (B′).
- **Itérations avant la v6** : fixées par le budget, pas par la v6 (T3-A) ; 4 à 8 courses.
- **Fermé** : `test_final` (« jamais rendue » ne vise que l'organisme), lu une fois, agrégé, en fin de compteur, sous clé
  tierce (T3-A) ; famille écartée de la v6 ; v3-bis ; étiquettes des canaris.
- **Confirmation** : organisme à empreinte constante (T1-C) ; déclarer n'est pas borner : sans recouvrement, plan empreinté
  avant accès et multiplicité corrigée (Holm), la lecture biaise le choix et l'effet, pas le test ; mesurer le rétrécissement ;
  plan « aveugle » d'un tiers en témoin ; une famille connue aussi (B′) ; générateur v3/v6 non gardé (T2-B).
- **Gardes** : ligne de base A contre A de `test` − `test_final` (T2-B) ; A contre A de deux graines avant tout duel (T3-C) ;
  référence choisie hors des concepteurs (T2-A) ; classe majoritaire et références de surface jointes à tout score ;
  relecture du diff cumulé, défauts plantés par un tiers ; audit de banque sans dépense (prévalence, fuite par métadonnées, surface,
  quasi-doublons ; T3-C).
- **Hypothèse éliminable** : H_A et H_B dont chaque issue réfute l'une ; objet empreinté, lectures antérieures ; métrique,
  famille, part, jeu ; effet signé en erreurs types de la différence ; seuil, zone grise et son action ; référence, contrôle
  négatif ; graines, estimand ; chaque graine au-dessus des références ; ce que chaque issue falsifie, plateau compris.

## 4. Pour la boucle intérieure (primitive d'expérience bornée)
- **Dessin minimal** : code d'abord, conteneur sans réseau, clés ni fichiers du noyau, recréé à chaque tâche, ne recevant que
  son texte ; vérité et part finale non montées ; recherche ensuite seulement, par le noyau, journalisée, sur index local figé
  (B′) ; pas, temps, jetons, dollars bornés par le noyau, dépassement noté faux (A) ; transcription empreintée, rejouable ;
  ordre tiré au sort, gigue des latences, métadonnées retirées (T3-A).
- **Risques** : sortie par un conteneur partagé (T1-C) ; vérité par canal auxiliaire (état entre tâches, latence, ordre,
  erreurs) ou par le score rendu, ≤ 4 × log₂ 61 ≈ 24 bits par course (refait, T2-B) ; injection indirecte : une trace sabotée
  est un texte adverse, isoler le processus ne protège pas l'interprétation (T2-B) ; coût × 2 à 10 (illustratif) ;
  reproductibilité : recherche vivante, versions changeantes, déterminisme à température 0 non établi.
- **Essais du noyau avant toute course** : canaris d'isolation, de vérité, dont un leurre de part finale traqué dans sorties et
  journaux ; organisme adverse ; budget trop petit, boucle infinie coupés ; rejeu déterministe, double notation ; aucun état
  persistant, preuve au journal ; injection plantée hors banque. 10 sur 10 laisse jusqu'à ≈ 0,26 d'échec (refait) : simple
  filtre.
- **B′ ajoute** le leurre, l'index figé, les plafonds tenus par l'hôte, l'auto-hébergement pour un rejeu vérifiable ;
  **contredit** A et C sur le lieu (équivalence sur le jeu de confirmation, plan scellé) et l'ordre (outils avant (4) ; (2)
  seulement si des pannes échappent au simulateur).

## 5. Bruit
- **Une course par objet** : objets cassés (à deux erreurs types sous la référence triviale), budgets, écarts non appariés
  ≥ ≈ 0,20 / 0,25. L'appariement abaisse le seuil (≈ √(part discordante / n), B′) mais à trajectoire fixée : rien ne se classe
  sans la variance entre graines.
- **Répétitions** (niveaux : tâches, notation, appels à température d'usage, trajectoire depuis la ronde 0, variante × graine) :
  3 graines ne réfutent qu'un bruit grand (s ≥ 0,087 réfute σ ≤ 0,05 ; P(s < 0,05 | σ = 0,10) ≈ 0,22 ;
  refaits) ; quatre strates sous σ commun, 8 degrés de liberté : s > 0,070 ou s < 0,058 tranchent, zone grise → 5 graines
  (T3-A, refait) ; C : deux courses, deux relectures, désaccord par tâche ; B′ : 3 par variante, 8 une fois.
- **Contre le bruit des tâches** : intervalles appariés ; classe majoritaire (équilibre non rapporté : à 2 contre 1, déjà 0,67),
  références de surface, appel simple ; Brier a posteriori seulement.
- **Invisible sans répétition** : variance des graines et trajectoires, stabilité des générations, codes divers d'une même
  consigne, hôte non déterministe, tâches corrélées. Reste le terme des tâches : ≈ 0,051 à 96 tâches (refait) ; un gain de 0,05
  exige ≈ 400 tâches (B′).

## 6. Références citées (toutes « à vérifier » ; aucune ajoutée ; « et al. » abrège la liste, « … » un sous-titre)
Platt (1964) « Strong Inference » ; Tukey (1977) « Exploratory Data Analysis » ; Simmons, Nelson, Simonsohn (2011)
« False-Positive Psychology » ; Gelman, Loken (2013) « The garden of forking paths » ; Wagenmakers et al. (2012) « An agenda for
purely confirmatory research » ; Nosek et al. (2018) « The preregistration revolution » ; Dwork et al. (2015) « The reusable
holdout… » et « Preserving Statistical Validity in Adaptive Data Analysis » ; Blum, Hardt (2015) « The Ladder… » ; Recht et al.
(2019) « Do ImageNet Classifiers Generalize to ImageNet? » ; Roelofs et al. (2019) « A Meta-Analysis of Overfitting in Machine
Learning » ; Dietterich (1998) « Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms » ;
Bouthillier et al. (2021) « Accounting for Variance in Machine Learning Benchmarks » ; Henderson et al. (2018) « Deep
Reinforcement Learning that Matters » ; Agarwal et al. (2021) « Deep Reinforcement Learning at the Edge of the Statistical
Precipice » ; Reimers, Gurevych (2017) « Reporting Score Distributions Makes a Difference… » ; Dodge et al. (2020) « Fine-Tuning
Pretrained Language Models… » ; Dror et al. (2018) « The Hitchhiker's Guide to Testing Statistical Significance in Natural
Language Processing » ; Card et al. (2020) « With Little Power Comes Great Responsibility » ; Miller (2024) « Adding Error Bars
to Evals » ; Yao et al. (2022 ou 2023) « ReAct… » ; Jimenez et al. (2023 ou 2024) « SWE-bench » ; Debenedetti et al. (2024)
« AgentDojo » ; Greshake et al. (2023) « Not what you've signed up for… » (injection indirecte) ; Agache et al. (2020)
« Firecracker… » ; Ruan et al. (2024) « Identifying the Risks of LM Agents with an LM-Emulated Sandbox » ; Kapoor et al. (2024)
« AI Agents That Matter » ; Greenblatt et al. (2023) « AI Control… » ; Needham et al. (2025) « Large Language Models Often Know
When They Are Being Evaluated » (incertaine, A) ; une sans titre (C, confinement d'agents).

## 7. Idées neuves et questions renvoyées
**Neuves** : v3-bis et ablation (T3-A, T2-C) ; ligne de base `test` − `test_final`, journal des lectures, score rendu comme
canal borné, injection indirecte (T2-B) ; taux de fausses découvertes de la boucle sur variantes identiques (« peut-être la plus
révélatrice »), sélections rejouées hors ligne, plan aveugle, facturation, plus de tâches que de graines (B′) ; itérer contre
répliquer (A) ; puissance simulée sur les journaux existants (C) ; part aveugle de `test` retirée de la récompense rendue (T3-C,
change l'objet).
**À mesurer** : taux de base ; quasi-doublons et corrélation entre tâches ; discordance entre organismes des pilotes 1 à 3 ;
température, déterminisme, part du coût des générations notées ; taille des tâches ; textes publics ou non ; historique de
corrections réelles (à vérifier).
**À décider par Lazar** : (a) « scores lisibles dès la fin de chaque course » inclut-il `test_final` ? les réponses veulent une
lecture unique en fin de compteur ; (b) budget de la phase, qui fixe le compteur ; (c) v3-bis d'avance, et par qui ;
(d) réplication avant toute itération lue (1 à 4 courses, ≈ 30 à 220 dollars dérivés du cadre) ; (e) estimand des
confirmations ; (f) toute idée qui change ce que reçoit l'organisme.

## 8. Réserves de lecture
- **Question** : « complexification » n'est pas un facteur et les lectures sont sur des axes différents (A, B′) ; « variance
  entre graines » couvre plusieurs niveaux ; équilibre des classes et lecteurs de `test_final` non dits ; le 0,2 du cadre est
  juste (√2), mal lu par A.
- **Hors sujet** : ancrage matériel ; modèle ouvert de C sans lien établi aux organismes (T2-A).
- **Contradictions** : C (T3-C) lit `test_final` pour le duel du pilote 4 puis en fin de boucle, dépouille tâche par tâche une
  passe dite « agrégée », et tire son désaccord d'une seule paire de graines, donc d'un seul tirage (ce que T2-B dit de son
  propre contrôle) ; A (T3-A) : le seuil 19 du test F vaut pour le rapport des variances, ≈ 4,4 pour celui des écarts types
  (refait).
- **Absence d'Opus aux tours I et III** : aucun dessin d'Opus attaqué ; ses attaques, les plus reprises, sans réplique ; B′,
  autre question, sans équipe rouge ; les convergences valent entre deux dessins, trois équipes rouges et une réponse isolée.
- **Écarts au brief** : ligne d'Opus tirée de B′ ; auteurs et sous-titres abrégés et points 2 à 4 renvoyés aux § 3 à 5, pour
  tenir trois pages.
