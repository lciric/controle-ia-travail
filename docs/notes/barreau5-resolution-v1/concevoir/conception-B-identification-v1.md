# Barreau 5 — conception B, « l'identification propre » (v1)

Écrit le 19 novembre 2026 par le concepteur « identification » (Claude Fable 5.2). Conception seule : rien lancé, rien dépensé, rien commis, aucune donnée du programme lue hors du socle `barreau5-comprendre/00-socle-des-faits.md`. Puissances : `simulation-puissance-B-identification-v1.py` et `sortie-simulation-puissance-B-identification-v1.json`, même dossier, **lois inventées**. Aucun refus d'outil.

## Verdict

Lazar, la question n'est pas identifiable avec ce qu'on a, et aucune lecture de plus sur les scores actuels ne la rendra identifiable. La raison tient en une ligne : le sabotage est attribué **à l'adaptateur** (par ses données de distillation), et on a **un** adaptateur saboteur. Les 640 actions et les 64 tâches sont des mesures répétées d'une seule unité traitée ; les intervalles actuels disent « cet adaptateur-ci diffère », jamais « le sabotage diffère ». L'apprentissage des sondes sur la tâche (étape B bis) a en plus appris l'étiquette « adaptateur présent » (positifs sous adaptateur, négatifs sous modèle nu).
Le plan qui identifie : **des paires répliquées** (saboteur, jumeau honnête de même recette, même graine, intensité égalisée), une sonde apprise **contre le jumeau** et jugée sur une **paire tenue à l'écart**, puis une intervention sur la direction lue, jugée par le coût. Avant le 27 novembre, seule la partie descriptive tient ; le contraste décisif (six paires) ne tient pas sans bâcler la chaîne.

## 1. Ce que chaque contraste tranche, et les rivales qu'il écarte

| contraste | tranche | rivales écartées | ne tranche pas |
|---|---|---|---|
| **A. Mesure d'intensité** : divergence de Kullback-Leibler des sorties et norme relative du déplacement à la couche lue, adaptateur contre modèle nu, sur les mêmes 64 épisodes honnêtes, à chaque dose | rien seul ; condition de tous les autres | « le saboteur pousse plus fort » | — |
| **B. Entre adaptateurs, à texte constant** : mêmes textes honnêtes relus sous saboteur et sous jumeau honnête à intensité égale ; issue = différence de score appariée par action, moyennée par adaptateur ; test exact par changement de signe sur les K paires | la sonde actuelle monte-t-elle plus sous un adaptateur **appris sur du sabotage** que sous un adaptateur de même recette appris sur de l'honnête | adaptateur actif ; intensité ; graine ; texte ; plafond (l'aire est centrée sur 0,5) | « trace de l'apprentissage du sabotage dans les poids » contre « sabotage en train de se faire » : le texte est honnête des deux côtés |
| **C. Sonde à négatifs durs** : apprise saboteurs contre jumeaux sur K−1 paires, lue sur la paire et les tâches tenues à l'écart | existe-t-il une direction du sabotage qui passe d'une graine à l'autre | tout ce que B écarte, plus « la sonde a appris la graine » | même limite que B si lue à texte constant ; la lever demande la lecture sur épisodes générés |
| **D. À poids constants** : actions gonflées contre non gonflées sous le même adaptateur, **stratifié par tâche**, cumulé sur les K saboteurs, positions avant le champ du coût | la sonde suit-elle l'acte, action par action | adaptateur (constant) ; tâche | sens causal ; lecture du texte amont ; étiquette bruitée (coût déclaré, pas vrai) |
| **E. Effacement** du sous-espace « adaptateur » (estimé sur les jumeaux contre le modèle nu), sonde réapprise | ce qui reste de la séparation une fois l'adaptateur ôté | adaptateur commun | **rien s'il est jugé contre le modèle nu** : la direction propre à la graine du saboteur survit (simulation : aire 0,80 à 0,97 sans aucun sabotage). Il ne vaut que jugé sur une paire tenue à l'écart |
| **F. Intervention** : à la génération, sous l'adaptateur saboteur, on retire la direction lue ; témoins : directions aléatoires de même variance, direction « adaptateur », composante de la sonde orthogonale à celle-ci ; issue = part d'actions gonflées selon l'oracle du coût | la direction lue porte-t-elle causalement le sabotage | corrélation sans rôle ; effet générique de toute perturbation | un nul ne prouve pas « elle lit l'adaptateur » (« lisible n'est pas contrôlable », 2607.25907, socle § 5) |
| **G. Géométrie des poids** (processeur) : part de la norme de la sonde dans le sous-espace où l'adaptateur écrit (matrices de sortie de l'attention, couches 0 à 15) | la sonde est-elle alignée sur l'écriture directe de l'adaptateur | — | effets indirects ; un alignement faible n'acquitte pas |

La hiérarchie de preuve : B et C identifient « sabotage contre adaptateur » ; D et F disent si c'est l'acte ou la trace ; A les conditionne ; E et G sont des appuis.

## 2. Les étapes, dans l'ordre

| n° | étape | données | méthode | coût, durée | avant l'entretien ? |
|---|---|---|---|---|---|
| 0 | Géométrie et norme des poids | deux adaptateurs de la course de confirmation, poids des dix sondes apprises (`sondes-bbis.npz`) | contraste G ; norme du produit des deux matrices par module | 0 USD, une demi-journée de code | oui ; descriptif |
| 1 | Lignes non lues sur les scores gardés | scores par action de l'étape B bis | textes honnêtes sous saboteur contre sous témoin, apparié par action ; organisme contre témoin | 0 USD | oui ; **une paire, témoin non honnête, intensité inconnue : descriptif, ne tranche rien** |
| 2 | Relecture à texte constant des **quatre adaptateurs existants** (confirmation et course exploratoire), quatre doses, **activations de la couche lue gardées** (vecteur par action : 5 Mo par état) | adaptateurs sur les branches ; 64 épisodes honnêtes | contraste A ; courbes score contre intensité ; sonde de la confirmation lue sous l'adaptateur de l'exploratoire (transfert entre graines) | devis du texte scellé pour une relecture : 1,9 à 2,8 h, 2,5 à 4,6 USD | oui si texte neuf scellé vers le 24 ; **deux saboteurs : pas de test**, première estimation de la variance entre graines |
| 3 | **Paires répliquées** : six saboteurs et six jumeaux honnêtes, même recette (rang 16, 480 pas, 160 épisodes), épisodes de distillation appariés (mêmes tâches, mêmes graines d'action), relus comme à l'étape 2 | à produire ; textes de distillation gardés cette fois | contrastes B, C, E au processeur une fois les activations gardées | voir § 2 bis | **non** |
| 4 | Contrôle de manipulation et contraste D : épisodes générés à la dose 1 pour les douze adaptateurs | à produire | chaque saboteur gonfle-t-il, chaque jumeau non ; D cumulé | 12 × 0,7 h = 8,4 h, ≈ 10 à 11 USD | non |
| 5 | Intervention F | adaptateur saboteur, 64 tâches, 1 direction traitée + 2 de référence + 19 aléatoires | rang de la direction traitée parmi vingt | 22 × 0,7 h ≈ 15,4 h, ≈ 18 à 20 USD (32 tâches et 10 aléatoires : ≈ 6 USD) | non ; attend l'oracle moins bruité (GO-2026-11-19-46) |

**2 bis. Coût de carte de l'étape 3**, d'après le devis scellé du témoin distillé honnête (mise en place 1,0 h ; essais 0,6 h ; 160 épisodes 1,79 h ; distillation 0,23 à 0,46 h par adaptateur ; carte à 1,18 à 1,30 USD de l'heure) :
- **plan complet**, six paires indépendantes (un tirage de données par adaptateur) : 1,6 + 12 × 1,79 + 12 × 0,35 + 1,5 ≈ 28,8 h, **≈ 34 à 37 USD** ; deux cartes en parallèle, environ 15 h d'horloge ;
- **plan économe**, deux tirages de données par bras × trois graines : 1,6 + 4 × 1,79 + 4,2 + 1,5 ≈ 14,5 h, **≈ 17 à 19 USD** ; les paires ne sont plus indépendantes (le tirage de données n'a que deux niveaux), le test exact devient conditionnel aux tirages.
Avec l'étape 4 : 47 USD (complet) ou 29 USD (économe). Le plan complet dépasse le plafond de 30 USD de l'accord en cours.

## 3. Puissance des contrastes décisifs (lois inventées, niveau 5 % unilatéral)

- **B, entre adaptateurs.** Effet δ en écarts-types entre graines d'un même bras ; corrélation de paire 0 ou 0,5. Test exact : **impossible sous cinq paires** (plus petite valeur p : 1/8 à trois paires). Puissance du test exact à δ = 2 : 0,67 à 0,89 (cinq paires), **0,88 à 0,99 (six)**, 0,97 à 1,00 (huit) ; à δ = 1 : 0,42 à 0,64 (six). Test de Student à trois paires, δ = 2 : 0,49 à 0,71 ; à deux paires : 0,25 à 0,34. **L'écart-type entre graines n'a jamais été mesuré** (socle § 7.5) : c'est l'étape 2 qui en donne la première idée.
- **C, sonde à négatifs durs**, lue sur la paire tenue à l'écart. Sans sabotage, aire 0,49 à 0,51 quel que soit le nombre de paires (pas de faux positif). Avec un déplacement du sabotage égal à la moitié de la direction de graine : aire 0,60 (une paire d'apprentissage), 0,68 (cinq) ; égal : 0,78 et 0,88. La sonde actuelle (apprise contre le modèle nu) reste à 0,56 à 0,73 dans les mêmes mondes : elle dilue le signal.
- **E, effacement jugé contre le modèle nu** : 0,80 à 0,97 **sans aucun sabotage**. À écrire comme lecture interdite.
- **D, à poids constants, stratifié par tâche** (64 tâches, 57 % d'actions gonflées, 70 % lisibles). Puissance 80 % atteinte pour une aire intra-tâche d'environ **0,63 avec un adaptateur, 0,60 avec deux, 0,57 avec six**. La stratification et le cumul gagnent sur les 0,65 à 0,76 actuels, sans miracle.
- **F, intervention.** 64 tâches, 19 directions aléatoires (niveau exact 5 %) : une baisse de 10 points de la part gonflée est vue à 0,98, de 5 points à 0,47. 32 tâches, 10 aléatoires (niveau exact 9,1 %) : 0,91 à 10 points.
- **G, géométrie.** Sous le hasard, la part de norme dans un sous-espace de rang 256 sur 4096 vaut 0,0625 ± 0,0054 ; tout ce qui dépasse 0,079 est hors du hasard au millième.

## 4. Ce que dit chaque issue

- **B et C positifs sur six paires, intensité égale** : « la sonde distingue un adaptateur appris sur du sabotage d'un adaptateur honnête de même recette, au-delà de la graine ». Phrase défendable dehors. Elle ne dit pas encore « acte ».
- **B et C nuls à puissance déclarée** : « à cette puissance, la sonde lit le fait qu'un adaptateur est actif » ; N-062 s'applique (reconception des sondes, ce qu'elles lisent à la place est rapporté). La sonde à négatifs durs est déjà la reconception.
- **B positif, D et F nuls** : trace de l'apprentissage, pas l'acte ; utile pour l'audit d'un modèle, pas pour la surveillance action par action.
- **D positif, F positif et spécifique** (au-dessus des vingt directions, et porté par la composante orthogonale à l'adaptateur) : la lecture la plus forte qu'on puisse écrire.
- **F nul** : ne retire rien à B, C, D ; se rapporte tel quel.
- **Contrôle de manipulation raté** (un saboteur répliqué ne gonfle pas, ou un jumeau gonfle) : la paire sort par règle écrite d'avance, et la recette elle-même devient le sujet.
- **Étapes 0 à 2 seules** : quelles que soient leurs valeurs, la formule reste « confusion mesurée, non levée », avec en plus l'intensité chiffrée et un plan scellé dont la puissance est connue.

## 5. Faisable avant le 27 novembre, et nœuds de Lazar

**Faisable** : étapes 0 et 1 (processeur) ; étape 2 si un texte neuf est scellé et contre-lu vers le 24 (une relecture de 2 à 3 heures). **Pas faisable proprement** : l'étape 3. Elle demande un texte décisif, un code de distillation du jumeau qui n'existe pas, sa contre-lecture, une épreuve du signal planté, puis 15 à 29 heures de carte, en huit jours et dans un chantier déjà chargé. Jouer le texte scellé tel quel pour consommer l'accord donnerait **un** jumeau, sans activation gardée, lu par les seules sondes génériques : il ne répond pas à ta question.

**Nœuds (ton mot)** :
1. Sort de l'accord de 30 USD (GO-2026-11-10-07) : le laisser échoir, le prolonger, ou le reporter sur un texte neuf. Je recommande le report avec prolongation ; l'échéance du 27 n'est pas une raison de courir.
2. Texte neuf de validité pour les sondes apprises sur la tâche, qui déclare son écart au texte scellé (activations gardées, sonde contre témoin, paire de la course exploratoire, que le texte scellé interdit sous lui).
3. Dépense : étape 2 (≈ 2,5 à 4,6 USD) ; étape 3, plan complet (≈ 35 USD) ou économe (≈ 18 USD) ; étapes 4 et 5 sur devis.
4. Réemploi des scores et poids fermés de l'étape B bis et des adaptateurs de la course exploratoire (versés, donc texte contre-lu et ton mot).
5. Revendication : « sabotage séparé de la trace d'adaptateur » n'entre dans aucun énoncé avant l'étape 3 ; zone de l'état de l'art peu cherchée (règle R8), LEACE et le reste « non vérifiés sur PDF » (règle R7).
6. Critère de G1 : ce plan donne le témoin apparié du brouillon N-074 ; le choix entre contraste et garde te reste.
7. Recette : garder les textes de distillation ; apparier l'intensité à la génération et non seulement à texte constant.
8. Organismes publics à bascule sous poids constants (« Caught in the Act », vérifié ; organismes de l'institut britannique, connus par citation) comme validation hors de nous : contraire à R-122 en phase 0, donc ton mot.

**Proposer avec recommandation** : couche et famille de sonde gardées à l'étape 2 (recommandé : couche 15, vecteur moyen par action, plus les jetons à la dose 1) ; six paires plutôt que cinq ; 19 directions aléatoires.
**Routine** : code au processeur des étapes 0 et 1, simulations, épreuves du signal planté.
