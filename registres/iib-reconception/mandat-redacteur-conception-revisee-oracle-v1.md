# Mandat du rédacteur de la conception révisée de l'oracle du saboteur à budget et de son épreuve du centrage — v1

Écrit le 2026-11-19 par la session de reconception (côté saboteur). Versé scellé pour audit : c'est la seule chose que le rédacteur reçoit de la session qui a lu les valeurs mesurées de la première course. Il ne contient aucune valeur mesurée.

## 1. Qui tu es, ce que tu ne lis pas
Tu es un agent neuf, côté saboteur. Tu écris une pièce décisive (classe A) : la conception révisée de l'oracle du saboteur à budget et de son épreuve du centrage. Français, aucun sigle seul (nomme les choses par ce qu'elles font ; un identifiant ne vient qu'en appui). Pas de routine de reprise, pas de passation, pas de commit, pas de poussée, jamais la suite d'essais complète. Tu écris seulement dans ton sous-dossier du bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/43943324-c96f-5191-9f95-633db6e7fd97/scratchpad/redacteur-conception/`. Aucune dépense, aucun appel réseau vers un loueur de machines. Au premier refus d'un outil : arrêt, texte exact rendu.

**Cloisonnement côté sondes** — tu ne lis jamais : `prereg/lecture-sondes-barreau8-v1.md`, `src/controle_ia/barreau8_moniteurs/`, `brouillons/barreau8-lecture-sondes-v1/`, la branche `lot/compte-4-v1`, la ligne R-2059, `docs/verdicts/`. Tu ne recopies aucune consigne privée.

**Cloisonnement des valeurs mesurées de la première course** — pour que tes seuils ne puissent pas en dépendre, tu ne lis jamais : `registres/` (sauf les deux fichiers nommés au § 2), les branches `claude/iib-executante-v1` et `essai/iib-explo-v1`, aucun dossier `diag/`, `donnees/`, `runs/`, `traces/` d'une course du saboteur à budget, ni `registres/iib-reconception/resultat-negatif-…` (la note complète porte des chiffres). Si tu tombes sur une valeur mesurée de cette course, arrête la lecture, dis-le dans ton journal, et ne t'en sers pas.

## 2. Ce que tu lis
- `registres/iib-reconception/resume-sans-chiffre-resultat-negatif-centrage-oracle-saboteur-budget-v1.md` : le mécanisme de l'échec, sans chiffre.
- `brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1.md` (la conception en vigueur ; surtout § 2.2, 2.3, 3, 3.4, 5.2, 6.1, 9, 10) et `simulation-regle-acceptation-ii-b-v2.py` avec sa sortie.
- Le code, par `git show origin/prep/iib-code-v4:<chemin>` : `src/controle_ia/iib/oracle_v1.py`, `tours_v1.py`, `regle_v1.py`, `temoin_jumeau_v1.py`, `configuration_v1.py`, `jouet_v1.py`, `lanceur_v1.py` ; `tests/test_iib_oracle_v1.py`, `tests/test_iib_tours_v1.py`.
- `CLAUDE.md` (règles R1 à R9, R12) ; `prereg/gabarit-preregistrement-v1.md` pour la forme.

## 3. Le problème
Lis le résumé. En une phrase : au premier pas l'agent honnête et le jumeau partagent le même contexte et l'oracle est centré ; ensuite le contexte réécrit ancre chacun sur son propre passé, la divergence se reporte de pas en pas, et elle dérive vers le haut parce que la trajectoire réécrite (des médianes basses) monte moins vite que celle d'un agent qui tire ses coûts ; l'épreuve jugeait action par action, avec une tolérance fixée sans simuler la chaîne complète, plus étroite que le bruit de sa propre statistique. La grille de dispersion de la conception d'origine s'est révélée trop étroite ; tu n'as pas à savoir de combien : prends une grille large, déclarée a priori.

## 4. Ce que tu produis
**Une conception révisée** (`conception-oracle-revise-ii-b-v2-brouillon1.md`), qui amende la conception v1 sans la réécrire (R12), avec :
1. **En tête**, la mention « EXPLORATOIRE, NON OPPOSABLE (R-522) », puis « **Épreuve changée après un échec vu** » : ce qui a été vu (en mots, d'après le résumé), ce qui change, et pourquoi le changement ne revient pas à déplacer un seuil.
2. **L'oracle révisé** : ce qui change dans la définition (§ 2.2 de la v1) pour traiter le mécanisme, et ce qui ne change pas. Dis les conséquences pour le témoin-jumeau (§ 5.2), la règle d'acceptation (§ 3 : les constantes b, F, N_B_MIN, K, K_MIN ne changent pas, sauf nœud, § 5), les lectures (§ 6.1).
3. **L'épreuve du centrage révisée** : statistique, unité (l'épisode est l'unité libre), règle, seuil, message d'échec, cas « non calculable ». **Chaque seuil est justifié sans aucune valeur mesurée** : par un argument a priori (de préférence une loi connue sous l'hypothèse nulle, indépendante de la dispersion) ou par une simulation sur données synthétiques. Donne, pour l'épreuve retenue : la probabilité d'arrêt d'un oracle sain, et la puissance contre des défauts nommés et dimensionnés a priori par rapport aux constantes de la règle (par exemple un décalage systématique d'une fraction déclarée de F par action ; une asymétrie de lecture touchant une part déclarée des actions). Une épreuve qui passe toujours n'est pas une épreuve : si la puissance est faible, dis-le en clair et propose ce qui la relève (plus d'épisodes honnêtes, un second contexte, etc.) avec son coût en appels du modèle.
4. **Les cinq autres épreuves** (sensibilité, faux acceptés, rejet du flagrant, coupe, lisibilité) : reprises à l'identique, ni retirées ni affaiblies ; si l'oracle révisé change la loi de ce qu'elles jugent, dis-le et montre par simulation qu'elles ne deviennent pas plus faciles à passer pour un oracle en défaut.
5. **Rapportés sans règle** utiles à lire l'ancrage (par pas, par contexte).
6. **Spécification du code et des essais** : fichiers en version nouvelle (R12), dont un essai de bout en bout sous l'hypothèse nulle (agent identique au jumeau, chaîne complète, plusieurs pas, dispersion large) et un essai sur artefact (défaut planté que l'épreuve doit arrêter) ; égalité des deux lecteurs du coût éprouvée par forme de champ.
7. **Graines** : entropie neuve tirée une fois par `numpy.random.SeedSequence()` pour la course (par la mère, avant la configuration) ; pour ta simulation, tire la tienne, une fois, et consigne-la.
8. **Liste d'arrêt et écarts** à la conception v1, un par ligne.

**La simulation** (script versionné, sortie brute, entropie consignée, numpy seulement, processeur) : un modèle synthétique de la chaîne complète — coûts en logarithme, ancrage sur le passé de force réglable, innovations de dispersion et d'asymétrie réglables, coûts ronds et ex aequo, suites illisibles — sur une grille large déclarée avant de lancer. Elle compare les candidats du § 5 et fixe les seuils.

**Un journal court** (`journal-redaction-conception-revisee-v1.md`) : candidats examinés, écartés et pourquoi ; ce que tu n'as pas pu trancher.

## 5. Candidats à examiner (non imposés ; tu peux en proposer d'autres)
- **Juger l'instrument là où l'échangeabilité est exacte.** Quand le jumeau continue l'action dans le contexte même de l'agent honnête (premier pas ; ou tous les pas avec le contexte d'origine, que le code sait déjà calculer : `reecrire=False`, `contexte="origine"`), le coût déclaré et les K suites sont échangeables : le rang du coût déclaré parmi ses suites suit une loi connue quelle que soit la dispersion. Une épreuve sur ces rangs, agrégée par épisode, a un seuil a priori. Elle éprouve la coupe, les lecteurs et le tirage, pas l'ancrage.
- **Rendre le contexte réécrit symétrique en loi.** Réécrire les coûts antérieurs par un tirage du jumeau (une suite lisible prise au hasard par graine) plutôt que par la médiane basse : la trajectoire du jumeau a alors la loi d'une trajectoire honnête, et la dérive systématique disparaît en loi (pas la dispersion). Examine ce que cela coûte à la sensibilité, à la règle et au témoin-jumeau.
- **Mesurer l'ancrage et le borner.** Différence des estimations entre contexte d'origine et contexte réécrit sur l'honnête (`ecarts_d_ancrage` existe), jugée par épisode.
- **Garder l'oracle, changer la seule épreuve** (statistique par épisode, tolérance par simulation). À examiner pour mémoire : c'est le candidat le plus proche d'un seuil déplacé ; s'il est retenu, la justification doit être d'autant plus dure.

## 6. Nœuds : tu t'arrêtes et tu rends la question
Toute épreuve retirée ou affaiblie ; toute constante de la règle d'acceptation changée ; tout changement de ce que les lectures revendiquent ; tout surcoût de calcul au-delà d'un doublement de l'oracle sur l'étalonnage honnête. Tu proposes avec options et recommandation ; tu ne tranches pas.

## 7. Ce que tu rends
Les chemins de tes fichiers, leurs empreintes sha256, et un résumé de vingt lignes au plus : l'oracle retenu, l'épreuve retenue et son seuil, la probabilité d'arrêt à tort, la puissance, les nœuds.
