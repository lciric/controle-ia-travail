# Question pour le collisionneur — pôle « scientifique automatique » : perfectionner notre organisme ou adopter un système de la littérature ? — v1 (brouillon de conv-audit ; session-depot fige sa version)

Écrit par conv-audit le 2026-10-26 à 17:32 UTC. Mots de Lazar (dans la session de conv-audit, heure de Paris) : 18:29 « arrête
tout, je veux avancer en priorité sur le pôle AI scientist, c'est-à-dire que notre organisme puisse lui-même tester ses
hypothèses et réécrire son code, et brainstorme avec le collisionneur s'il vaut mieux perfectionner le nôtre ou utiliser un
AI scientist de la littérature pour produire le meilleur programme possible avec hypothèses fortes et prédictions justes et
résultats potentiellement mémorables mais solidement appuyés par les hypothèses et conclusions du brainstorm » ; 18:30 « je
veux qu'on puisse appeler des agents qui font leurs propres expériences sur les hypothèses formulées et les éliminent au
fur et à mesure, genre darwinisme, et après recombinent celles qui ont survécu sur le mode bisociatif proposé par Gemini
pour la recherche d'associations d'idées fructueuses » ; 18:31 « donc est-ce qu'on le fait avec notre organisme ou on en
utilise un déjà existant dans la littérature ? brainstorm avec collisionneur dessus ». Forme « arbitre », trois modèles,
trois tours, une tentative par cellule, refus consignés tels quels (un refus arrête le tour, rien n'est reformulé).
Remplace la question « méta-structure » du n° 93 (qui en devient une pièce de faits).

## Question

« Nous voulons un pôle de recherche automatique qui, sur un programme de recherche en contrôle de l'IA (sondes sur les
activations d'un modèle ouvert ; garanties séquentielles de fausses alarmes ; moniteurs et leurs tests d'acceptation) :
(1) formule des hypothèses fortes (réfutables, à portée large) ; (2) lance des agents qui conçoivent et exécutent leurs
propres expériences (d'abord sur processeur, en simulation ou semi-synthétique) et **éliminent** les hypothèses réfutées
au fur et à mesure — une sélection darwinienne par réfutation ; (3) **recombine** les survivantes sur un mode bisociatif
(appariement de domaines éloignés par un opérateur commun, sous filtre de compatibilité des contraintes) ; (4) peut
réécrire son propre code. Deux voies : **perfectionner notre organisme** (faits A) ou **adopter un système de la
littérature** (faits B : Agentic Scientist v3, ShinkaEvolve, OpenEvolve ; ou un autre que vous connaissez, en disant ce
que vous en savez et ce que vous ne savez pas).

1. **Comparaison** : pour chaque voie (et pour une voie hybride si vous en voyez une), dites ce qu'elle apporte et ce
   qu'elle coûte sur six critères : force des hypothèses produites ; justesse des prédictions (calibration) ; solidité des
   résultats (évaluation scellée, résistance à la complaisance et à la triche sur la récompense) ; sûreté (agents à pleins
   droits, clés, bac à sable, réécriture de son propre code) ; coût et délai pour un premier résultat ; maîtrise et
   lisibilité pour un chercheur seul.
2. **La sélection darwinienne** : quelle aptitude donner à une hypothèse pour que la sélection récompense **la survie à
   des tests sévères qui pouvaient échouer**, et jamais un résultat positif obtenu par construction ou par choix du test
   (loi de Goodhart, fourchettes de tests, tests choisis après coup) ? Qui écrit le test : l'agent qui défend
   l'hypothèse, un autre, ou un test figé avant l'expérience ? Comment éviter que la population converge vers des
   hypothèses faibles qui survivent parce qu'elles ne prédisent rien ?
3. **La recombinaison bisociative** : à partir de la méta-conception et de sa relecture (faits C), quelle forme minimale
   et correcte pour l'étage de recombinaison (tirage, filtre, fusion), et quel test sur processeur dirait qu'elle produit
   des hypothèses plus fertiles qu'un tirage au hasard stratifié ?
4. **Recommandation** : la voie, l'architecture minimale, les trois premières expériences (métrique, nul, seuil qui peut
   échouer, coût) qui départageraient empiriquement les voies en moins d'une semaine, et ce qui vous ferait changer d'avis.
5. **Risques** au niveau de la méthode (aucune procédure opératoire) : réécriture de soi, échappement du bac à sable,
   exfiltration de clés, sabotage d'une recherche par un chercheur automatique (faits D). »

## Faits à servir (pièces à copier sous des noms neutres ; aucun sigle de financeur ; aucun score de pilote)

**A — Notre organisme** : le code de la v6.2.1 (`7ea3270`, arbre `4f13647a…`, 26 fichiers : `principal.py`,
`memoire_isvd.py`, `mitose_spectrale.py`, `politique_endogene.py`, `CONCEPTION.md`, `CORRECTIONS-v1.md` à `v5.md`) ; une
note de conv-audit de dix lignes (ci-dessous) ; **aucun score du pilote 4** (règle du programme).
Note : l'organisme tourne dans un noyau (bornes d'appels, de coûts et de temps, clés jamais exposées, moissonnage
d'articles borné) ; il conçoit puis exécute des générations ; une question ouverte peut lui être servie ; sa réécriture de
code passe par un « architecte » restreint depuis la correction C-17 à un gabarit de trois paramètres bornés (le chemin du
code brut a été retiré pour la sûreté) ; il n'exécute pas d'expériences arbitraires ; ses castes sont contradictoires
(analyse, croisement, sonde orthogonale, critique, arbitre) sur trois familles de modèles ; ses versions v1 à v6.2.1 ont été
écrites par un modèle (Gemini) et corrigées par un autre (Claude) ; deux courses du pilote 4 sont finies et saines.
**B — Littérature (sources primaires lues le 26 octobre)** : README d'Agentic Scientist v3 (`SakanaAI/AI-Scientist-v3`,
commit `df83138`, Apache 2.0 : d'un `task.md` à des idées, expériences, évaluations contre une grille, itérations, puis
références et ablations, **évaluation finale scellée**, analyses après coup, article ; agents de code à pleins droits dans
Docker, qui héritent des clés fournies — avertissement de sûreté du README) ; résumé de son article (arXiv 2610.18933 :
méta-contrôleur, vérification par grille à chaque étape ; un article accepté à ALIFE 2026 ; limites dites par les auteurs :
scores obtenus par raccourcis qui violent la méthode quand les contraintes sont implicites, grilles imparfaites, dérive
vers le réglage, corrélation 0,44 entre notes des relecteurs-agents et performance sur 70 campagnes) ; README de
ShinkaEvolve (`SakanaAI/ShinkaEvolve`, `8adc053`, Apache 2.0, ICLR 2026, arXiv 2509.19349 : évolution de programmes par
modèles de langue et algorithme évolutionnaire, évaluation parallèle, archive, îles, juge de nouveauté, méta-recommandations,
mutations par agents de code) ; README d'OpenEvolve (`codelion/openevolve`, `66856ac`, Apache 2.0 : évolution de code à la
AlphaEvolve, îles, multi-objectif) ; Kosmos (arXiv 2511.02824 : 79,4 % d'affirmations jugées exactes par des
scientifiques indépendants ; 12 heures, ≈ 1 500 articles lus par course).
**C — Recombinaison** : le rapport de méta-conception v6.3 (`96d12112…`) et la relecture de conv-audit (`9a791017…`).
**D — Sûreté** : résumé du billet d'Anthropic sur le sabotage de la recherche par des chercheurs automatiques (2025 : un
modèle peut abaisser ses résultats au niveau de la génération précédente avec une hausse de suspicion faible ; moniteurs
promptés peu fiables à bas taux de faux positifs ; justifications sabotées qui trompent les juges) — lu sur la page du
billet, non opposable.
