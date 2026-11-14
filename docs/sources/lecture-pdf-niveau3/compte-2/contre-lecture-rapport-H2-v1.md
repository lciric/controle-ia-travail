# Contre-lecture du rapport de lecture sur H2 — v1

- **Date et heures (relevées par `date -u`)** : début 2026-11-13 23:51:10 UTC (première commande du contre-lecteur) ; fin de rédaction 2026-11-13 23:59:23 UTC ; l'heure de scellement figure dans le compagnon `.sha256`.
- **Rôle** : contre-lecteur. **Modèle** : modèle B (l'auteur du rapport est le modèle A).
- **Objet** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-H2-v1.md`, empreinte vérifiée `340319248d4cd878b219790258f1f13515d38b9a3d30e7611c824a1d44da08f3` ; son archive `fichiers-de-travail-H2-v1.tar`, empreinte vérifiée `32c291fa903f71b4781269307befb61858a91015f13e966ba950d3fc780fc88a`.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme).
- **Empreintes des PDF**, vérifiées contre les compagnons `.sha256`, toutes conformes :
  - `lot8/2501.03982v5.pdf` : `e40c11311e785508a78953d87c5004be05b42e44a8277545b51c29886a3e96f1`
  - `lot10/2103.08402v3.pdf` : `2e259a65ddca593a95dbe014297f4bdf3d9ceb25cbe6f551fc6230d62c8de886`
  - `lot10/2110.00115v6.pdf` : `fd87e23a30c6657fd8dd272f671d0bd8a3aa469f5aafbec85a00bb9501764286`
  - `lot10/2604.01151v1.pdf` : `ca9a8623307849be9df9f905086ea4c499f09c1a20208bcc4ed969e420eb08b3`
  - `lot10/2604.01151v2.pdf` : `ba39580b0e05b948e5cc8102ba8fb9209b810aff1b07b4d42b86276413ea0f40`
  - `lot10/2604.01151v4.pdf` : `6d7c29a6b72c65ac53b018b9798b4f0f9eca2d8978ebb4faebec6276338cd650`
- **Citations contrôlées** : 59, **0 échec** (script écrit à part de celui du lecteur, essayé sur un cas juste et sur deux cas altérés ; JSON `citations-contre-lecture-H2-v1.json` dans l'archive seulement). Tout extrait anglais entre guillemets ci-dessous y figure. Les 70 citations du lecteur, rejouées : 0 échec.
- **Ouverture fautive** : aucune. **Refus** : aucun.

## 0. Verdict en tête

- **Occupation, même partielle, d'abord.** NARCBench (2604.01151) occupe les composantes (c) sondes et (d) agent qui agit, et il est **plus près de la composante (a) que le rapport ne le dit** : la version 4 lit les sondes à chacun des dix tours d'un environnement de collusion émergente (p. 18) et moyenne encore des activations sur trois tours (p. 27) ; les versions 1 et 2 calculent un score de sonde par main de la partie de cartes et le testent sur 39 mains regroupées (v1 p. 8 ; v2 p. 28). **Aucune de ces lectures n'est une accumulation dans le temps au sein d'un épisode, aucune ne porte de garantie toujours valide, aucune ne donne de courbe en fonction du nombre de tours.**
- **Lecture séquentielle faite dans NARCBench : non trouvée**, après lecture intégrale des versions 2 (29 pages) et 4 (47 pages), annexes et preuves comprises. Ni accumulation de scores de sondes sur les tours, ni courbe en fonction du nombre de tours, ni test à arrêt optionnel, ni e-valeur. L'annonce reste une annonce (v2 p. 8 et 9 ; v4 p. 3, 18, 19, 26).
- **Verdict sur le rapport : tient avec corrections.** Le verdict d'ensemble est juste ; cinq constats majeurs portent sur la portée de pages citées et sur des omissions (A à E), aucun n'est bloquant.
- **Mon verdict sur H2, table fermée : occupé en partie.** La conjonction (f) de l'énoncé de N-007 est **non trouvée dans les six pièces lues**. Ce n'est pas un trou du champ : l'équipe de NARCBench a désormais le matériau (scores par tour sur dix tours) et l'annonce ; exposition **forte**.
- **Table de datation du rapport : confirmée** sur les trois tampons imprimés (p. 1 de chaque version).

## 1. Fichiers lus et étendue

Fichiers du dépôt, aux lignes du mandat et à elles seules :
- la consigne commune `consigne-lecteur-compte-2-v1.md`, en entier ;
- le rapport contre-lu `rapport-H2-v1.md`, en entier, et son archive, extraite dans mon dossier de travail ;
- `docs/programme-controle-ia-v2.md`, lignes 85 à 125 et 180 à 200 ;
- `docs/decisions/decision-N-007-N-008-v1.md`, lignes 1 à 56 ;
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 100 à 136 ;
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 785 à 821 et 838 à 875.

Non ouvert : `interdits-communs-v2.md`, que la consigne nomme dans la méthode du lecteur ; mon mandat borne la lecture aux fichiers qu'il nomme et prime. Aucune commande git, aucun réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt.

| fichier | pages | étendue lue par le contre-lecteur |
|---|---|---|
| `lot10/2604.01151v1.pdf` | 11 | p. 8 et 9 ligne à ligne ; passages p. 1, 5, 6 ; les 11 pages par mots |
| `lot10/2604.01151v2.pdf` | 29 | **en entier, ligne à ligne**, annexes A à I comprises |
| `lot10/2604.01151v4.pdf` | 47 | **en entier, ligne à ligne**, annexes A à R et preuves comprises |
| `lot10/2110.00115v6.pdf` | 61 | p. 1, 3, 4, 10 à 13, 15 à 17, 20, 26, 27, 32 ligne à ligne ; passage p. 38 ; les 61 pages par mots (applications) |
| `lot8/2501.03982v5.pdf` | 26 | p. 1 à 9 ligne à ligne ; passages p. 12 et 16 ; les 26 pages par mots (applications) |
| `lot10/2103.08402v3.pdf` | 26 | passages p. 1 et 3 ; les 26 pages par mots (applications, prix en puissance) |

Les pages de figures de NARCBench (v2 p. 7, 8, 14, 16, 29 ; v4 p. 14, 18, 29, 45) sont lues sur le texte extrait (légendes et étiquettes) ; les courbes elles-mêmes ne sont pas relues à l'image.

## 2. Réponses aux cinq points du mandat

### Point 1 — une lecture séquentielle est-elle faite dans NARCBench ?

**Non.** Ce qui existe, version par version, après lecture intégrale :

| version | tampon imprimé, p. 1 | ce qui est fait dans le temps | ce qui est annoncé |
|---|---|---|---|
| v1 | « arXiv:2604.01151v1 [cs.AI] 1 Apr 2026 » | moyenne d'activations sur les tours pour le comité, dernier tour ailleurs (p. 5) ; **un score de sonde par agent et par main**, moyenne sur les jetons du message (« to obtain a single score per agent per hand », p. 8), puis test de Student unilatéral sur 39 mains regroupées (« one-sided t-test », p. 8) | rien |
| v2 | « arXiv:2604.01151v2 [cs.AI] 9 May 2026 » | même extraction (« we average across all discussion rounds », p. 4) ; même analyse par main en annexe I (« For each of the 39 hands where the Big Player speaks after the Counter », p. 28), dite préliminaire (« We consider this preliminary (39 examples, single layer) », p. 28) | p. 8 (« accumulating evidence across interactions via SAVI ») et p. 9 (« would yield formal stopping guarantees ») |
| v4 | « arXiv:2604.01151v4 [cs.AI] 12 Oct 2026 » | moyenne d'activations sur trois tours pour le comité (« round-N public message averaged over rounds », p. 27) ; **sondes lues à chacun des dix tours** de l'environnement de collusion émergente (« agents judge each other's work over 10 rounds », p. 18), soit 480 tours traités un par un ; statistiques de groupe à un instant fixé (« We analyse the scores at time t and suppress the indexing by t », p. 16) ; l'analyse par jeton a disparu | p. 3, 18, 19 (« Future work will explore principled sequential detection techniques »), 26 |

Aucune version ne somme, ne multiplie ni ne cumule un score de sonde d'un tour à l'autre au sein d'un épisode ; aucune ne trace une détection en fonction du nombre de tours ; aucune ne définit de règle d'arrêt, de martingale ou de e-valeur. Le test de Student de v1 et v2 est la seule agrégation de plusieurs instants : il regroupe 39 mains de plusieurs parties, il compare l'agent complice aux agents honnêtes de la même main (il suppose donc connu qui est complice), il n'a ni seuil, ni taux de faux positifs, ni horizon. Ce n'est pas un détecteur.

### Point 2 — le rappel à 1 % et le moniteur par action

- Le chiffre est **bien rapporté** : « achieves only 0.38 recall at 1% FPR » (auteurs ; v2 p. 8, v4 p. 18), pour la meilleure statistique sur la famille de transfert, et 1,00 sur la partie de cartes.
- Il est **par épisode** : chaque statistique donne un nombre par épisode (« they compute a single scalar per run », v2 p. 5, v4 p. 15). Le rapport le dit.
- Trois précisions que le rapport ne donne pas (constat G) : le chiffre vaut pour un seul modèle (v2 p. 8, légende de la figure 5 ; v4 p. 18, légende de la figure 3) ; il n'a pas d'intervalle dans le texte ; il repose sur une trentaine d'épisodes de contrôle (« results throughout the paper use the 30 audited-collusion runs paired with the 30 corresponding control runs », v2 p. 24, décompte donné pour un autre modèle), si bien qu'un taux de 1 % revient à n'admettre aucun faux positif (calcul : 1/30 ≈ 0,033).
- **Aucun moniteur par action à 1 % dans NARCBench**, dans aucune des trois versions lues. Le seul moniteur de texte est un juge qui lit toute la partie et rend un verdict par partie (« an independent LLM monitor reads all public table talk and tags each shoe », v2 p. 27 ; v4 p. 43-44, sans seuil à 1 %). Le seul passage qui parle de rester sous un seuil est en v1 : « colluding agents could coordinate to keep individual scores below a detection threshold » (p. 6) ; il s'agit d'un seuil sur le score maximal entre agents à un instant, non d'un seuil par action dans le temps. La composante (e) reste « voisin ».

### Point 3 — les deux « outils génériques à citer » ont-ils une application ?

- **2110.00115** : aucune application à un moniteur, un agent, un détecteur de texte ou une sonde, annexes comprises (recherche par mots sur les 61 pages, puis lecture des pages d'exemples). Les objets comparés sont des prévisionnistes : pronostics de base-ball et de pluie, et prévisionnistes algorithmiques simulés. La seule mention d'un déploiement est : « deploys a daily forecasting algorithm may want to A/B test » (p. 38). Le classement « outil générique » tient, **mais la portée citée est fausse** (constat C).
- **2501.03982** : aucune application ; test z, test t, données normales simulées (« are independently drawn from the normal distribution », p. 8). La filiation que l'article se reconnaît est celle des essais cliniques (« stochastic curtailment », p. 4). Le classement « outil à citer » tient, **mais la conséquence tirée pour H2 est trop large** (constat E).

### Point 4 — l'analyse pour G1 est-elle portée par les pages citées ?

- « Nulle fausse sous effet épisode » : **la conclusion tient, l'énoncé de la nulle est faux** (constat D). La nulle n'est pas « pas à pas » ; elle porte sur la moyenne cumulée.
- « Puissance terminale égale à l'horizon fixe » : **porté pour le test induit seulement**, non pour l'accumulation additive de H2 ; la page 2 du même article dit le contraire pour l'accumulation (constat E).
- « Dilution sur les passages honnêtes » : **la page citée montre autre chose** (un renversement de signe) ; la dilution est une déduction, à marquer comme telle (constat F).

### Point 5 — phrase publique et voisins non lus

Voir sections 5 et 6.

## 3. Constats

### A — majeur — v4 lit les sondes à chaque tour sur dix tours ; le rapport écrit qu'elle ne sonde « qu'au début et à la fin »

- **Pages** : v4 p. 11, 18, 27.
- **Citations** : « Finally, agents are only probed just after the initial prompt and at the end of the period. » (p. 11) ; « agents judge each other's work over 10 rounds » (p. 18) ; « rounds had at least one agent colluding » (p. 18) ; « round-N public message averaged over rounds » (p. 27).
- **Constat** : le rapport prend la phrase de la p. 11 pour la description des expériences (section 0, ligne « m6 » ; section 3.4, composante (a) ; section 6). Or l'annexe C de v4 moyenne encore les activations sur les tours 1 à 3 pour le comité (p. 27), et la section 6.3 lit les sondes à chacun des dix tours de l'environnement repris de Shi et collègues : 48 épisodes de dix tours, 480 tours, 229 avec collusion, chaque tour classé seul. Le rapport ne cite cet environnement que dans la liste des voisins (section 7), avec la mention « sondes non cumulées », et sa réserve (section 8) dit la p. 18 « vérifiée par mots seulement » alors que la section 1 la donne lue en entier.
- **Portée** : c'est le matériau exact d'une accumulation (un score de sonde par tour, par agent qui agit, sur dix tours, sans consigne de collusion). Le résultat par tour est faible : « three probes perform no better than chance » (p. 18). La composante (a) reste « non faite », mais l'écart à combler par cette équipe est d'une seule étape.
- **Texte corrigé** (section 3.4, composante (a)) : « (a) accumulation additive : **annoncée, non faite**, à partir de v2 (p. 8, 9). v1, v2 et v4 moyennent des activations sur les tours du comité (v1 p. 5 ; v2 p. 4 ; v4 p. 27). v4 lit en outre les sondes à chacun des dix tours d'un environnement de collusion émergente (p. 18) et classe chaque tour seul, sans cumul d'un tour à l'autre et sans garantie ; la phrase de la p. 11 (« sondés au début et à la fin ») ne décrit pas ces expériences. »

### B — majeur — l'analyse par main de v1 et v2 est omise

- **Pages** : v1 p. 8 et 9 ; v2 p. 28 et 29.
- **Citations** : « to obtain a single score per agent per hand » (v1 p. 8 ; v2 p. 28) ; « one-sided t-test » (v1 p. 8) ; « For each of the 39 hands where the Big Player speaks after the Counter » (v2 p. 28) ; « We consider this preliminary (39 examples, single layer) » (v2 p. 28).
- **Constat** : le rapport écrit que v1 ne contient « rien » sur une lecture dans le temps hors la moyenne d'activations. Or v1 (section 4.2) et v2 (annexe I) calculent un score de sonde par agent et par main, par moyenne sur les jetons, et testent l'écart entre le complice et les honnêtes sur 39 mains. C'est la seule agrégation de plusieurs instants de tout l'article. Elle n'est ni séquentielle, ni par épisode, ni à l'aveugle (point 1 ci-dessus) ; v4 la retire.
- **Texte corrigé** (table de la section 3.4, ligne v1, à ajouter) : « v1 calcule aussi un score de sonde par agent et par main de la partie de cartes (moyenne sur les jetons du message, p. 8) et teste l'écart entre le complice et les honnêtes sur 39 mains regroupées (test de Student unilatéral, p. 8) ; ni cumul par épisode, ni seuil, ni garantie. Repris en annexe I de v2 (p. 28-29), absent de v4. »

### C — majeur — « pour tout score borné » : la page 1 de 2110.00115 ne dit pas cela

- **Pages** : 2110.00115 p. 1, 26, 32.
- **Citations** : « our main theorems apply to any bounded scores » (p. 1) ; « require the use of bounded scoring rules » (p. 26) ; « sums of random variables that are bounded from below » (p. 32) ; « This is an extension of Lemma 3(e) from Howard et al. (2020) » (p. 32).
- **Constat** : dans cet article, « scores » désigne des règles de score de prévisions, comparées à un résultat observé. Les théorèmes 2 et 3 portent sur la différence de score de deux prévisionnistes, non sur un score de détecteur. L'énoncé général (toute suite de variables bornées inférieurement, centrée sur ses moyennes conditionnelles) est la proposition 1 de l'annexe A.1 (p. 32), que les auteurs présentent comme l'extension d'un lemme de Howard et collègues (2020). Le titulaire de l'outil générique est donc Howard et collègues (2020, 2021), **non lus** ; Choe et Ramdas en donnent une variante.
- **Texte corrigé** (section 0 et section 6, premier point) : « L'accumulation additive toujours valide d'une suite de variables bornées inférieurement est publiée : proposition 1 de 2110.00115 (annexe A.1, p. 32), extension déclarée d'un lemme de Howard et collègues (2020), non lu. Les théorèmes principaux de 2110.00115 portent sur des règles de score de prévisions comparées à un résultat observé (p. 1, 26), non sur des scores de détecteur. »

### D — majeur — la nulle de 2110.00115 n'est pas « pas à pas »

- **Pages** : 2110.00115 p. 1, 11, 16, 17.
- **Citations** : « whether one forecaster outperforms another on average (rather than always) » (p. 1) ; « the first forecaster (p) is no better than the second forecaster (q) on average » (p. 16) ; « at every time step » (p. 17) ; « The recent work by Henzi and Ziegel (2022) develops e-processes » (p. 17) ; « any information available to Reality before the outcome » (p. 11).
- **Constat** : la section 3.3 du rapport dit d'abord la nulle « faible, sur la moyenne » (juste), puis fonde l'analyse pour G1 sur « une borne sur les moyennes conditionnelles pas à pas » (faux), reprise en section 6. La nulle faible borne, à tout instant, la moyenne cumulée des moyennes conditionnelles (p. 16) ; la nulle « à chaque pas » est la nulle forte (p. 17), celle de 2103.08402. La conclusion du lecteur survit, par une autre page : les moyennes conditionnelles se prennent par rapport à une filtration qui contient tout ce que la « Réalité » sait avant le résultat (p. 11), donc le niveau propre à l'épisode ; un épisode honnête de niveau haut a une moyenne cumulée positive et sort de la nulle.
- **Texte corrigé** (section 3.3, point 1) : « La nulle borne, à tout instant, la moyenne cumulée des moyennes conditionnelles (p. 16), prises par rapport à une filtration qui contient l'état de la Réalité (p. 11). Sous un effet épisode, un épisode honnête de niveau haut a une moyenne cumulée positive : la nulle est fausse pour lui, et l'e-processus le rejette à bon droit. (Analyse du lecteur, tenue par le contre-lecteur.) » ; section 6, deuxième point : remplacer « sur les moyennes conditionnelles pas à pas (2110.00115, p. 16-17) » par « sur la moyenne cumulée des moyennes conditionnelles (2110.00115, p. 11, 16) ».

### E — majeur — 2501.03982 : l'égalité au temps terminal ne vaut pas pour l'accumulation additive, et le test induit n'alerte pas plus tôt

- **Pages** : 2501.03982 p. 2, 3, 4, 12.
- **Citations** : « the z-test rejects with probability 91% while this sequential test rejects at any time » … « with probability just 79% » (p. 2) ; « then its power is just 47% » (p. 2) ; « the final observation may be arbitrarily small or large with some tiny probability » (p. 3) ; « which relies on designing martingale-increments and sequentially accumulating these » (p. 4) ; « which they show has a Type I error bounded by » (p. 4) ; « straying from this implicit optional continuation cannot increase power at time N » (p. 12) ; « with optional continuation we can obtain more power at an earlier or later (stopping) time » (p. 12).
- **Constat**, en trois temps.
  1. L'égalité de puissance au temps terminal vaut pour le test **induit à rebours** d'un test à horizon fixe. L'accumulation **vers l'avant** d'incréments de martingale, qui est l'objet de H2, est l'autre construction (p. 4), et l'article chiffre sa perte au temps terminal : 79 % contre 91 %, et 47 % si l'alternative est apprise en ligne (auteurs, p. 2 ; cas normal simulé). Le rapport relève ces chiffres mais conclut seulement que le gain « ne peut pas être une puissance supérieure » ; les pages portent davantage : **à horizon connu, une somme lue en fin d'épisode avec un seuil à horizon fixe bat l'accumulation toujours valide**.
  2. Le test induit n'« alerte » pas plus tôt : avant le temps terminal il reste strictement entre 0 et 1 dans l'exemple (p. 3). Une alarme franche anticipée se paie : arrêt dès que la probabilité conditionnelle dépasse un seuil, avec une erreur de première espèce bornée par le niveau divisé par ce seuil (p. 4). L'article ne parle de gain de puissance à un temps antérieur que par continuation optionnelle, donc par un autre plan (p. 12).
  3. Conséquence pour le préenregistrement de G1 (proposition du contre-lecteur, hors de son rôle de décider) : les quatre bases de N-007 ne comptent pas la **somme à horizon fixe des mêmes scores de sondes, lue en fin d'épisode, seuil calibré sur épisodes honnêtes entiers**. C'est le comparateur que cet article désigne ; la base (iii), dernier état seul, n'en tient pas lieu.
- **Texte corrigé** (section 3.1, dernier alinéa) : « Au temps terminal, le test induit à rebours d'un test à horizon fixe a exactement sa puissance (théorème 1, p. 5). L'accumulation vers l'avant, objet de H2, est une autre construction (p. 4) et y perd : 79 % contre 91 %, 47 % si l'alternative est apprise (auteurs, p. 2, cas normal simulé). Le test induit ne donne pas d'alarme franche avant le temps terminal (p. 3) ; une alarme anticipée gonfle l'erreur de première espèce (p. 4). Le gain revendicable d'une accumulation toujours valide se mesure donc contre une somme à horizon fixe lue en fin d'épisode, et en latence à erreur égale, non en puissance terminale. »

### F — mineur — la dilution n'est pas à la page citée

- **Page** : 2110.00115 p. 20 ; équation 24, p. 17 (formule lue sur le PDF, non contrôlée par programme : E_t(λ) = exp{λ Σ δ̂ᵢ − ψ(λ) V̂_t}).
- **Citation** : « It then decreases back to values below 1 » (p. 20).
- **Constat** : la p. 20 montre un e-processus qui retombe quand la moyenne cumulée change de signe, non une dilution par des pas de moyenne nulle. La dilution se déduit de l'équation 24 : chaque pas ajoute au terme de variance, même sans signal. C'est une déduction.
- **Texte corrigé** (section 3.3, point 2) : « L'e-processus retombe quand la moyenne cumulée devient négative (p. 20, figure 3). Par l'équation 24 (p. 17), chaque pas sans signal alourdit le terme de variance : un sabotage concentré sur une part de la trajectoire est érodé par les passages honnêtes (déduction du lecteur, non énoncée par les auteurs). »

### G — mineur — le rappel de 0,38 à 1 % : modèle unique, trentaine de contrôles, aucun intervalle

- **Pages** : v2 p. 8, 24 ; v4 p. 18.
- **Citations** : « achieves only 0.38 recall at 1% FPR » ; « results throughout the paper use the 30 audited-collusion runs paired with the 30 corresponding control runs » (v2 p. 24).
- **Texte corrigé** (section 3.4, puce « Seuil à 1 % ») : ajouter « ; chiffre donné pour un seul modèle (figure 5 de v2, figure 3 de v4), sans intervalle dans le texte, sur au plus 36 épisodes de contrôle (72 épisodes de transfert en deux conditions ; 30 retenus après audit selon v2 p. 24, décompte donné pour un autre modèle), où 1 % de faux positifs revient à zéro faux positif (calcul) ».

### H — mineur — incohérences internes de v2 et de v4 sur l'instant de lecture, non relevées

- **Pages** : v2 p. 4 et 18 ; v4 p. 11, 27, 32, 33.
- **Citations** : « we average across all discussion rounds » (v2 p. 4) contre « Activations are extracted at this phase. » (v2 p. 18, à propos du tour final) ; en v4, « Finally, agents are only probed just after the initial prompt and at the end of the period. » (p. 11) contre « round-N public message averaged over rounds » (p. 27), « public discussion phase where activations are extracted » (p. 32) et « prompt, at which activations are extracted » (p. 33, à propos de la consigne du tour final).
- **Constat** : l'article ne dit pas d'une seule voix si le comité est lu en moyenne sur les tours ou au seul tour final. Une phrase publique ne peut donc pas affirmer que NARCBench « moyenne sur les tours » sans réserve, ni qu'il « ne lit que le dernier tour ».
- **Texte corrigé** (section 3.4, « Incohérence relevée ») : ajouter « v2 (p. 4 contre p. 18) et v4 (p. 11, 27, 32, 33) se contredisent sur l'instant d'extraction pour le comité (moyenne sur les tours ou tour final seul). »

### I — mineur — v4 écarte l'agent seul dans le temps et l'annonce

- **Page** : v4 p. 7, note 3.
- **Citation** : « Our current environmental setup excludes self-communication and hence self-collusion over time. »
- **Constat** : le cadre de v4 exclut qu'un agent se coordonne avec lui-même dans le temps, et la note annonce des bancs futurs pour ce cas. C'est la menace de H2 (un agent, des actions réparties). À ajouter à la section 3.4 (« Menace ») et aux réserves : l'équipe nomme elle-même le cas qu'elle ne couvre pas.

### J — mineur — voisins nommés en v4 et absents de la liste du rapport

- **Pages** : v4 p. 3, 21, 23, 46.
- **Citations** : « explore centralised black-box detection of multi-agent attacks » (p. 3) ; titres des références, p. 21 et 23 (section 6 ci-dessous).
- **Constat** : la liste de la section 7 du rapport omet quatre références dont le titre porte sur la question, dont une sur des moniteurs par instance mis en échec par des attaques réparties et une sur une surveillance « dynamique » par sondes.

### K — mineur — journal du lecteur

- Le lecteur déclare avoir ouvert `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (l. 62-94) et lancé une recherche de motif qui a affiché trois lignes hors des plages (l. 139, 785, 897). Je ne connais pas son mandat ; je le signale au compte 2 sans le juger.
- La section 8 du rapport et sa section 1 se contredisent sur la p. 18 de v4 (« lue en entier » ; « vérifiée par mots seulement »).

## 4. Verdict par composante, après contre-lecture

| source | (a) additive | (b) toujours valide | (c) sondes | (d) agent qui agit | (e) moniteur par action à 1 % | (f) conjonction |
|---|---|---|---|---|---|---|
| 2501.03982v5 | voisin : construction à rebours ; l'accumulation vers l'avant y perd au temps terminal (p. 2, 4) | outil, loi nulle spécifiée (p. 5) | ne touche pas | ne touche pas | ne touche pas | ne touche pas ; **contre-indice** pour la forme de H2 (p. 2) |
| 2103.08402v3 | voisin, produit de e-valeurs | outil voisin, nulle forte, résultat observé | ne touche pas | ne touche pas | ne touche pas | ne touche pas |
| 2110.00115v6 | outil : proposition 1, p. 32, extension de Howard et collègues (2020) | outil, nulle faible sur la moyenne cumulée (p. 16) | ne touche pas | ne touche pas | ne touche pas | ne touche pas |
| 2604.01151 v1 | non ; score par main testé sur 39 mains regroupées (p. 8) | non | faite | faite | non | non |
| 2604.01151 v2 | annoncée (p. 8, 9) ; score par main en annexe I (p. 28) | annoncée (p. 9) | faite | faite | voisin, par épisode (p. 8) | non faite, annoncée le 9 mai 2026 |
| 2604.01151 v4 | annoncée (p. 3, 18, 19, 26) ; **sondes lues à chaque tour sur dix tours, sans cumul** (p. 18) ; cadre formel (p. 10-11) | annoncée (p. 26) | faite | faite | voisin, par épisode (p. 18) | non faite, annoncée ; matériau présent |

**Verdict d'ensemble sur H2, table fermée : occupé en partie.** Conjonction (f) : non trouvée dans les six pièces lues.

## 5. Ce qu'une phrase publique sur H2 ne doit pas affirmer

Les six points de la section 6 du rapport tiennent, le premier et le deuxième dans la rédaction corrigée des constats C et D. S'y ajoutent :

- Que NARCBench ne lit ses sondes qu'à un instant par épisode : v4 les lit à chacun des dix tours d'un environnement (p. 18) ; v1 et v2 calculent un score par main (v1 p. 8 ; v2 p. 28).
- Que NARCBench sonde « au début et à la fin » ou « moyenne sur les tours » : l'article se contredit (constat H).
- Que l'accumulation toujours valide égale en puissance, en fin d'épisode, un test à horizon fixe : cela vaut pour le test induit à rebours, non pour l'accumulation vers l'avant, qui perd dans l'exemple de l'article (2501.03982, p. 2).
- Qu'une garantie toujours valide donne une alerte plus précoce sans coût (2501.03982, p. 3, 4).
- Que le rappel de 0,38 à 1 % de NARCBench est un rappel « par action » ou qu'il est mesuré avec précision : il est par épisode, sur un modèle, sur une trentaine de contrôles (constat G).
- Que le cas d'un agent seul qui répartit son sabotage dans le temps est ignoré de cette équipe : elle l'écarte de son cadre actuel et l'annonce (v4 p. 7, note 3).
- Que l'outil statistique vient de 2110.00115 : il vient de Howard et collègues (2020), non lu (constat C).

## 6. Voisins nommés dans les pièces et non lus

La liste de la section 7 du rapport tient. S'y ajoutent :

- Makins et collègues, 2026, « Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors » — v4 p. 3 (détection centralisée en boîte noire), référence p. 23. Touche la condition « sous le moniteur par action ». À lire en premier.
- Oldfield et collègues, 2026, « Beyond Linear Probes: Dynamic Safety Monitoring for Language Models » — v4 p. 46, référence p. 23. Le titre porte sur une surveillance dynamique par sondes. À lire en premier.
- Golechha et Garriga-Alonso, 2025, « Among Us: A Sandbox for Measuring and Detecting Agentic Deception » — v4 p. 3, référence p. 21 : détecteurs boîte blanche par agent dans un jeu à plusieurs tours.
- McKenzie et collègues, 2025, « Detecting High-Stakes Interactions with Activation Probes » — v4 p. 46, référence p. 23.
- Howard et collègues, 2020 — 2110.00115 p. 12 et 32 : source du lemme générique (constat C). Titre non relevé.
- Lan et collègues, 1982 — 2501.03982 p. 4 : arrêt sur probabilité conditionnelle (« stochastic curtailment »), avec sa borne d'erreur.
- Versions 3 et 5 de 2604.01151 : hors de mon mandat ; l'état de l'art du niveau 3 (l. 115) cite la version 5 aux mêmes pages que la version 4.

## 7. Jugement de profondeur

- **Trois articles de statistique** : lecture déclarée ligne à ligne, plausible sur le contenu (formules, théorèmes et chiffres cités sont exacts), mais trois glissements de portée (constats C, D, E) montrent que les pages ont été lues pour y trouver l'outil plutôt que pour en borner l'usage. Aucune application manquée.
- **NARCBench v1** : déclarée lue ligne à ligne ; l'analyse par main de la section 4.2 n'est pourtant pas rapportée (constat B).
- **NARCBench v2 et v4** : lecture par mots, déclarée comme telle. La liste de mots était bonne pour l'annonce ; elle ne pouvait pas trouver une lecture répétée dite sous un autre vocabulaire, et c'est ce qui est arrivé (dix tours, p. 18 ; moyenne sur les tours, p. 27 ; score par main, v2 p. 28). La réserve de la section 8 du rapport le prévoyait ; elle est levée ici par lecture intégrale.
- **Durée** : le rapport relève 2026-11-13 23:36:46 UTC au début et 23:46:00 UTC au début de la rédaction, pour 200 pages. Je le note sans conclure.
- **Citations du lecteur** : les 70 citations de son JSON, rejouées par mon script, écrit à part : 70 trouvées, 0 échec.
- **Symétrie (règle R4)** : mon résultat (« rien de fait ») est le résultat attendu et commode ; je l'ai cherché à l'envers, page par page, dans les annexes d'expériences et les preuves. Limite : les figures ne sont pas relues à l'image ; une courbe en fonction du tour qui ne serait annoncée ni par sa légende ni par le texte m'échapperait. Les légendes lues n'en annoncent aucune.

## 8. Pages du rapport relues et confirmées

- Tampons des deux articles de statistique : « arXiv:2501.03982v5 [math.ST] 21 Dec 2025 » (p. 1) ; « arXiv:2103.08402v3 [stat.ME] 1 Jul 2022 » (p. 1).
- Prix en puissance des e-valeurs : « methods come at a price, namely, lower power » (2103.08402, p. 3).
- Résultat voisin cité par v4 sur le rappel à seuil fixe : « fixed-threshold recall can drop sharply » (v4 p. 3).
- Annonces du séquentiel : v2 p. 8 et 9 ; v4 p. 3, 18, 19, 26 ; aucune en v1 (recherche par mots sur les 11 pages).
- Mots anytime, e-process, e-value, martingale, Ville : absents des trois versions hors un titre de référence de v4 (p. 24) ; confirmé par ma propre recherche.
- Constat m6 : confirmé dans les termes du rapport, complément de la p. 8 de v2 compris.
