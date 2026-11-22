# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHznpfBkfYsJBSkUszDQ`
- Heure (UTC) : 2026-11-22T12:54:54Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 70000, aucune relance, aucun repli vers un autre modèle, budget de tâche 40000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/chantiers-21-novembre-v1/question-seuil-devin-v1/consigne-reponse-question-v1.md` — sha256 bf15ef108e9b23ae144fe2856ac5f8d2ac24393b74db3fd0b54b650d69b4279f (compagnon : vérifié)
  - correction : `docs/notes/chantiers-21-novembre-v1/question-seuil-devin-v1/question-seuil-budget-devin-v3.md` — sha256 fd339e029e8fa389055e4b5a2c618619f33d0521df3a4af3b2dfe25909d67879 (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/question-seuil-devin-v1/remarques-vides-v1.md` — sha256 83b2b517f67f3ac629ab9e0d53ac194edd0392edb28d4c189b60994528a69a89 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 376ffc71fd566f376b89f43c5f9dad8f326f4dd8a1a7e6e2217458eaae62cb2e
- Jetons : entrée 1603, sortie 19398 (dont réflexion 15490), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 0.788744 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Réponse — seuil et budget de l'épreuve d'admission

## 1. Choix

**PROPOSITION** — Aucune des trois telle quelle. Je propose une option (d) : seuil de 0,0125 par test et 8 000 épisodes par test, avec trois amendements.

**FAIT RAPPORTÉ** — Le tableau croise deux leviers, le seuil (0,05 ou 0,0125) et le budget (4 000 ou 8 000), mais ne présente que trois des quatre combinaisons.

**CALCUL** — La combinaison manquante donne 4,9 % de fausses suspensions par admission sous indépendance. La plus petite fuite retrouvée vaut environ 0,066 à pile ou face et environ 0,15 à 5 % d'audit (chiffres de (b) divisés par √2).

**CALCUL** — Effet de chaque levier sur la plus petite fuite retrouvée :

| Levier | Facteur multiplicatif | Coût équivalent en épisodes |
|---|---|---|
| Seuil de 0,05 à 0,0125 | 1,11 | 22 % de plus pour compenser |
| Budget doublé | 0,71 | le double |
| Audit de pile ou face à 5 % | 2,29 | 5,26 fois plus pour compenser |

**PROPOSITION** — Le seuil est le levier le moins cher : je le paie pour ramener les fausses suspensions sous 5 % par admission.

**HYPOTHÈSE** — Une alarme fausse près d'une fois sur cinq se banalise et pousse à rééprouver jusqu'à ce que l'épreuve passe.

Amendements :

- **PROPOSITION** — Fixer d'abord, par secret, la taille de fuite jugée dangereuse. Dimensionner ensuite chaque test contre elle, avec une puissance d'au moins 0,9. Le budget n'a pas à être uniforme : le test sur la décision d'audit à 5 % est le maillon faible.
- **PROPOSITION** — Éprouver la décision d'audit à bras équilibrés si le tirage le permet. **HYPOTHÈSE** — Cela suppose que le canal de fuite ne dépend pas du taux d'audit.
- **PROPOSITION** — Après un rejet, exiger une correction du dispositif et juger la nouvelle épreuve en cumulant les données. **CALCUL** — Avec des réépreuves indépendantes, une fuite à la limite de détection passe chaque épreuve avec probabilité 0,2, donc 0,36 en deux tentatives.

## 2. Confiance

**PROPOSITION** — 0,6 que (d) soit préférable aux trois options. Contraint aux trois, je prends (c), avec une confiance de 0,4 : l'erreur coûteuse est la fuite manquée, et (c) domine (a) à seuil égal.

## 3. Ce qui me ferait changer d'avis

- **Coût.** **HYPOTHÈSE** — Si une fausse suspension ne coûte qu'une réépreuve du test en cause, sur données cumulées, je garde 0,05. **CALCUL** — Le surcoût attendu est alors d'environ 0,185 × 4 000 ≈ 740 épisodes par admission, contre environ 3 600 pour compenser la correction de Bonferroni sur quatre tests.
- **Conséquence.** **HYPOTHÈSE** — Si une suspension arrête l'agent ou engage le laboratoire à l'extérieur, je durcis le seuil sous 0,0125.
- **Taille dangereuse.** **PROPOSITION** — Si la fuite dangereuse vaut 0,2 ou plus, (b) suffit et coûte le moins. Si elle vaut 0,05 ou moins, aucune option ne suffit. **CALCUL** — Le budget croît comme l'inverse du carré de la fuite visée : la diviser par deux le quadruple.
- **Fuite concentrée.** **CALCUL** — Un signal jamais présent sous audit, présent dans 19 % des épisodes non audités, a une variation totale de 0,19. Il offre à l'agent environ 18 % d'épisodes sans aucun risque d'audit. **HYPOTHÈSE** — Si le danger vient de quelques fenêtres sûres, la variation totale n'est pas la bonne mesure. **PROPOSITION** — Il faudrait alors éprouver le taux d'audit parmi les épisodes que le prédicteur classe « non audités » avec le plus d'assurance.
- **Propriété du test.** **PROPOSITION** — Si les quatre tests partagent leurs épisodes, un seul maximum par permutation conjointe des secrets donnerait 5 % par admission avec moins de perte que Bonferroni, et (d) changerait de seuil. **HYPOTHÈSE** — Si les épisodes ne sont pas échangeables (dérive, mémoire de l'agent), l'exactitude tombe et il faut permuter par blocs.

## 4. Unité de contrôle

- **Le test.** **CALCUL** — À 0,05 par test, on a 18,5 % de fausses suspensions par admission. Sur dix admissions indépendantes, environ 87 %. **PROPOSITION** — Cette unité engage à accepter une alarme qui gonfle avec chaque cible ajoutée, ce qui dissuade d'en ajouter.
- **L'admission.** **CALCUL** — À 0,0125 par test, on a 4,9 % par admission, et environ 40 % sur dix admissions. La plus petite fuite retrouvée augmente de 11 %. **PROPOSITION** — C'est mon choix : c'est l'unité à laquelle la décision se prend.
- **Variante : le secret.** **FAIT RAPPORTÉ** — Un rejet suspend la garantie qui s'appuie sur ce secret, pas le dispositif entier. **CALCUL** — À 0,025 par test, on a 4,9 % par secret et 9,6 % par admission. **PROPOSITION** — C'est défendable si les deux garanties sont gérées séparément.
- **La vie du dispositif.** **CALCUL** — Partager 5 % sur dix admissions donne 0,00125 par test et une plus petite fuite retrouvée d'environ 0,107 à pile ou face. **PROPOSITION** — Cette unité engage à fixer d'avance le nombre d'épreuves, et rend chaque épreuve moins sensible à mesure que le dispositif dure, ce qui est à contresens pour la sûreté. Je préfère un test séquentiel qui cumule les données d'une épreuve à l'autre, remis à zéro à chaque modification matérielle du dispositif.

## 5. Erreurs et antériorités

**Chiffres**

- **CALCUL** — Les taux de 18,5 % et 4,9 % sont exacts sous indépendance.
- **CALCUL** — Je retrouve les fuites du tableau avec un seuil unilatéral divisé par trente (borne de Bonferroni sur la famille) et une proportion proche de 0,5. Le maximum par permutation est moins sévère si les prédicteurs sont corrélés. Pour (a) à pile ou face, la vraie valeur se situe entre 0,056 (un seul prédicteur) et 0,085.
- **CALCUL** — Pour (c) à 5 %, j'obtiens 0,137, soit environ 0,14 et non 0,13.
- **CALCUL** — Sans indépendance, la borne générale est 20 % pour (a) et (c), et 5 % pour (b). **HYPOTHÈSE** — Deux cibles d'un même secret sont positivement dépendantes. Le taux réel serait alors plus bas que 18,5 %.

**Raisonnement**

- **CALCUL** — Le test mesure l'avantage atteint par la famille après apprentissage, qui est au plus égal à la variation totale. La phrase sur le non-rejet ne vaut donc que pour une fuite exploitable par cette famille et apprenable sur la moitié d'apprentissage.
- **CALCUL** — À 5 % d'audit, cette moitié ne contient qu'une centaine d'épisodes audités. **HYPOTHÈSE** — C'est peu pour apprendre : les fuites réellement retrouvées seraient plus grosses que les chiffres du tableau.
- **HYPOTHÈSE** — La décision d'audit est tirée au sort : la permutation y est exacte par construction. La lecture du détecteur ne l'est pas. Si elle dépend légitimement du contenu de l'épisode, que l'agent voit, le nul d'indépendance est faux sans qu'il y ait fuite. Il faudrait alors un test conditionnel.
- **PROPOSITION** — Une puissance de 0,8 laisse passer une fuite limite sur cinq, ce qui est trop pour une admission de sûreté.
- **FAIT RAPPORTÉ** — Le budget est donné par test. Le tableau ne dit pas si les quatre tests partagent leurs épisodes, donc si l'admission coûte 4 000 ou 16 000 épisodes.

**Antériorités**

Je ne connais aucun texte qui traite exactement ce choix. Les références suivantes, toutes citées de mémoire, en sont voisines.

- Westfall et Young, 1993, *Resampling-Based Multiple Testing* : maximum par permutation (de mémoire, non vérifiée).
- Holm, 1979, « A simple sequentially rejective multiple test procedure » (de mémoire, non vérifiée). **CALCUL** — Pour l'événement « au moins un rejet », cette procédure coïncide avec Bonferroni : elle n'apporte rien ici.
- Lopez-Paz et Oquab, 2017, « Revisiting Classifier Two-Sample Tests » ; Ojala et Garriga, 2010, « Permutation tests for studying classifier performance » (de mémoire, non vérifiées).
- Goodwill et coauteurs, 2011, « A testing methodology for side-channel resistance validation » ; Whitnall et Oswald, 2019, « A Critical Analysis of ISO 17825 » : seuil, puissance et multiplicité en détection de fuite matérielle, le parallèle le plus proche (de mémoire, non vérifiées).
- Schuirmann, 1987, sur les tests d'équivalence par deux tests unilatéraux, titre non retenu (de mémoire, non vérifiée).
- Lan et DeMets, 1983, « Discrete sequential boundaries for clinical trials » ; Foster et Stine, 2008, « α-investing » ; Howard, Ramdas et coauteurs, 2021, sur les suites de confiance : contrôle sur la durée (de mémoire, non vérifiées).
- Candès et coauteurs, 2018, « Panning for gold » : tests d'indépendance conditionnelle par randomisation (de mémoire, non vérifiée).
- Greenblatt, Shlegeris et coauteurs, 2023, « AI Control: Improving Safety Despite Intentional Subversion » : audit à budget limité d'un agent non fiable (de mémoire, non vérifiée).
