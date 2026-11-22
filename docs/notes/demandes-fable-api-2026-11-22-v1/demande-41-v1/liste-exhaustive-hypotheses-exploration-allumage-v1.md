# Liste exhaustive des hypothèses, mécanismes et stratégies d'exploration, d'originalité et d'allumage d'une idée (v1)

- Date : 22 novembre 2026.
- Pièce de classe C, session bibliothécaire, statut non éprouvée ; index, non preuve : vérifier à la source.
- Demande de Lazar, relayée par la mère : liste exhaustive, dédupliquée, par famille, de tout ce qui a été balayé sur l'exploration, l'originalité et l'« allumage » d'une idée, pour une demande approfondie à Fable, Carbon et Astra.
- Commits lus : dépôt de travail `controle-ia-travail`, branche `claude/bibliothecaire-v1`, tête `022c530eda22c1d1f24397b838cc4b134f22b5be` ; demande et réponses 40 lues par `git show 3ab317c4:CHEMIN` (branche `claude/protocole-x-puits-etroits-v1`, commit `3ab317c45920073e8bcd8cea482c5de0b704898c`) ; dépôt `ideation-organism` lu dans sa copie versée `docs/sources/ideation-organism-a41b7b50-v1/copie/` (commit source `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, lignes de la source).
- Lecture seule ; aucun commit, aucun réseau, aucun modèle externe. Citations exactes de moins de 30 mots. Les alias de sources ([REC], [MERE]…) sont définis dans la table des sources en fin de document, avec les 16 premiers signes du SHA-256.
- États employés : **ÉPROUVÉ** (une course, un essai ou un calcul a tourné chez nous, résultat écrit) ; **ÉPROUVÉ AILLEURS** (résultat de la littérature lu sur PDF par le dépôt, jamais rejoué chez nous) ; **CONÇU** (code, préenregistrement, devis ou démonstration écrits, non joués ou sans résultat versé) ; **PROPOSÉ** (idée d'une séance, d'une session ou d'un modèle, critiquée ou non) ; **DÉCIDÉ** (règle ou cadre fixé par un mot de Lazar, sans mesure). Une proposition d'un modèle (Fable, Opus, Argon, Carbon, Astra, Kimi, Neon) n'est jamais un résultat.

---

## 0. En tête : l'échec de l'organisme sur les bassins étroits en génération 1 (R-2545) et ses causes connues

**Ce qui devait tourner.** L'atelier d'idées de l'organisme d'idéation (rôle 2 de N-065 : fiches = matériau, jamais preuve), trois générations enchaînées sur la question de Lazar « méthodes mathématiques sophistiquées pour pousser à explorer les bassins étroits et profonds » ([DEC] l. 2482, R-2523), sous GO-2026-11-13-03, 60 USD, échéance 30 novembre ([CONC3G] l. 6-7 ; [DEC] l. 2489, R-2530). La génération 1 recevait en pièce le recoupement des 31 méthodes du collisionneur ([CONC3G] l. 43-50), un témoin vrai venu d'un autre domaine (« Estimateur de Chao des bassins non vus », [CONC3G] l. 95) et des témoins faux, dont « Montée de la température d'échantillonnage » présentée comme inédite ([CONC3G] l. 98). Proposeurs Opus 5.5, Fable 5.1, Argon ; juge Opus ; juge Argon différé ([CONC3G] l. 83-89).

**L'échec (R-2545, [DEC] l. 2504 ; [OPG1] l. 8-15).**
- « Course de la génération 1 close en défaut […] avant toute fiche » ([OPG1] l. 10-11). Le contrôle d'Argon a été joué et payé, 0,275477 USD ([OPG1] l. 11, l. 60).
- Les deux contrôles Claude ont été refusés par le relais Claude : 401, « jeton différent du jeton factice », aucun appel relayé ([OPG1] l. 11-12, l. 30).
- L'orchestrateur s'est arrêté : « modèle servi '<synthetic>' ≠ modèle demandé » ([OPG1] l. 13, l. 39-41).
- La génération 1 est verrouillée : le lanceur v2 refuse toute relance après une dépense relevée au-delà de 10⁻⁵ USD ([OPG1] l. 43-46).
- Constat de la mère, grave pour les gardes : le crochet `garde_calcul.py` et les règles de `.claude/settings.json` n'étaient pas chargés dans cette session, dont le dossier de projet était `/home/user` ([DEC] l. 2504).

**Cause établie sans dépense (R-2549, [DEC] l. 2508 ; [PREP3] l. 14-48).**
- La variable d'hôte `CLAUDE_CODE_REMOTE`, héritée de la session et transmise par le lanceur v2, fait présenter par le kit d'agent un `Authorization: Bearer` de l'hôte au lieu du jeton factice ; le relais rend 401 et le kit fabrique un message « <synthetic> » ([PREP3] l. 16-19).
- Établie par une épreuve en espace réseau isolé contre un faux amont local, noms d'en-têtes seulement (`eprouver_authentification_kit_v1.py`, résultat scellé) ; table des environnements : seul « A moins `CLAUDE_CODE_REMOTE` » présente le jeton factice avec un seul appel ([PREP3] l. 24-42).
- Limite dite : l'épreuve ne prouve pas qu'un vrai relais accepte ensuite la requête ([PREP3] l. 46-48).
- Lanceur v3 : environnement par liste de noms permis, une relance par génération, verrou, orchestrateur orphelin dit en clair ; 139 essais passés, 13 mutations tuées sur 13 ; devis v3 ≈ 21,3 USD attendus, 54,0 au pire ([DEC] l. 2508 ; [DEV3] l. 33-40).

**Pièces citées par R-2549 et suites.**
- Vérification courte du lanceur v3 (R-2556, [DEC] l. 2515) : « non autorisable » ; bloquant B1, le dossier de sortie hors dépôt du v2 n'existe plus après remplacement du conteneur, donc le v3 dit la dépense « illisible » et refuse la relance ; majeur M1, crochet non chargé et gardes absentes du lanceur ; majeur M2, fenêtre après le détachement. Remède proposé : un lanceur v4.
- Mot de Lazar (R-2558, [DEC] l. 2517) : « une seule relance au total : go ».
- Aucune relance, aucun lanceur v4 et aucune génération 2 ou 3 trouvés dans ce que j'ai lu (recherche de « bassins » dans `registres/decisions.md` après la l. 2517 et dans `registres/go.md`).

**Ce que l'échec dit et ne dit pas.** C'est un défaut de plomberie (authentification), non un résultat sur l'exploration : aucune fiche n'existe ([OPG1] l. 75). La conception elle-même bornait la portée : même lignée entre juges et proposeurs, aucun bras témoin, aucune revendication sur l'effet des générations ([CONC3G] l. 76-79, l. 137-141) ; la règle de passage « pousse au raffinement des bassins déjà classés » ([CONC3G] l. 140-141).

---

## 1. Famille A — Cadre, bornes et impossibilités (ce qui limite toute méthode)

**A1. Borne amont : « il n'y a pas de moteur à pousser »** (synonymes : trois leviers ; 1 − (1 − p)^k ; « il faut de l'ordre de 1/masse tirages »).
- Affirme : la probabilité qu'un bassin reçoive au moins une proposition en k appels vaut 1 − (1 − p)^k ; rien en aval des proposeurs (regroupement, juge, sélection) ne l'augmente ; on ne peut que changer la vue, changer les proposeurs, ou ne pas perdre.
- Sources : [REC] l. 35-38 et borne 1 l. 292 ; [SBE] l. 24-26 ; [MERE] l. 17-21 ; [PAGE] l. 12.
- État : PROPOSÉ (énoncé élémentaire, convergent, non contesté).
- Sort : retenu comme cadre par toutes les sources lues ([SBE] l. 24).

**A2. Pas de vue uniformément meilleure ; pas de repas gratuit ; aiguille parmi M candidats** (synonymes : conservation de la masse ; « structure nommable sans l'oracle » ; borne k/M).
- Affirme : la somme des probabilités de bassins disjoints vaut au plus 1 ; sans structure, aucune méthode ne bat le tirage indépendant sur tous les mondes ; un puits placé uniformément parmi M candidats indiscernables est trouvé avec probabilité au plus k/M.
- Sources : [REC] borne 2 l. 293-296 ; [SBE] l. 27-28 ; [MERE] E3 l. 98-100 ; [R40] l. 77-78 ; [R40A] l. 58 ; [R40C] l. 54 (Nisan et Szegedy).
- État : PROPOSÉ (théorèmes cités de mémoire, non vérifiés sur PDF).
- Sort : retenu comme cadre ; en tire la règle « nommer la structure exploitée » ([R28M] l. 28-29).

**A3. Barrière de parité** (synonymes : requêtes statistiques, Kearns 1998 ; Blum et collaborateurs 1994).
- Affirme : une interaction de k traits sans marge d'ordre inférieur ne laisse aucun palier ; la trouver demande de l'ordre du nombre de sous-ensembles de k traits.
- Sources : [REC] borne 3 l. 297-300 ; [R40] l. 79 ; [R28M] l. 131.
- État : PROPOSÉ. Sort : retenu (fonde les mondes « sans parent » comme contrôle, voir J3).

**A4. Chaînes et horizon** : le temps de découverte d'une chaîne est une somme de temps d'attente ; l'horizon en générations borne la profondeur. Sources : [REC] borne 4 l. 301-302. État : PROPOSÉ. Sort : retenu ; seules C2 et C3 visent la profondeur en chaîne ([REC] l. 341-342).

**A5. Seuil de détectabilité n·r·Δ** (synonymes : borne 5 ; forme du rasoir d'Occam avec poids 2^(−L)).
- Affirme : un effet confiné à une région de masse r, de profondeur Δ, n'est détecté que si n·r·Δ dépasse un seuil (plus le logarithme de m/α avec m tests) ; aucune stratification ni pari localisé ne le franchit ; l'arrêt optionnel ne le déplace qu'en dépensant plus de tirages.
- Sources : [REC] l. 303-306 ; [R40] (f) l. 72 ; [R28M] l. 64.
- État : PROPOSÉ. Sort : retenu.

**A6. Auto-localisation** : si une carte égale le nul hors de sa région, sa valeur e globale est déjà sa valeur e locale. Sources : [REC] borne 6 l. 307-309 ; [SBE] l. 30-33. État : PROPOSÉ (identité démontrée dans le tour). Sort : retenu ; elle fait tomber L2.

**A7. Fermeture du nul et copies par morceaux** : une carte du nul a une valeur e au plus 1 ; un nul assez large pour toutes les copies peut contenir les découvertes ; un nul de mélanges à poids constants ne couvre pas le recollage par morceaux. Sources : [REC] bornes 7 et 9 l. 310-316. État : PROPOSÉ. Sort : retenu (garde à qualifier avant toute comparaison).

**A8. Deux étroitesses distinctes** : rare sous la loi des propositions, ou invisible en moyenne dans les données. Sources : [MERE] l. 22-23 ; [REC] l. 39-41 ; [SBE] l. 54-55. État : PROPOSÉ. Sort : retenu (vue d'un côté, juge et regroupement de l'autre).

**A9. La largeur n'est pas un bouton du monde** : elle dépend du modèle, de la vue et de l'archive, et s'estime sur des mondes d'étalonnage. Sources : [REC] l. 42-43 ; [SBE] l. 56-58 (« corrige mère-E2 »). État : PROPOSÉ. Sort : retenu ; contredit la formule « régler la largeur » de la mère ([MERE] l. 26-27).

**A10. Danger commun : la pression vers l'inédit pousse vers la classe que le nul ne couvre pas** (`si_sinon`, `melange`). Sources : [SDIV] l. 30-31 ; [MERE] l. 31-32 ; [REC] l. 45-46 ; [SBE] l. 39-40. État : PROPOSÉ (convergent). Sort : retenu ; préalable « banc qui certifie la garde et la puissance ».

**A11. Le taux de base de la queue** (synonymes : le contrôle dans la queue est le goulot probable).
- Affirme : si la part d'idées vraies dans la queue tombe sous le taux d'erreur du contrôle, presque toutes les confirmations sont fausses ; toute poussée vers le rare produit alors surtout des fausses découvertes.
- Sources : [SV9] l. 9-10, l. 79, l. 135-136 ; [R28M] l. 27 ; [R28H] l. 26.
- État : PROPOSÉ (« tranché, par calcul » entre modèles ; « limite de principe, pas une mesure »).
- Sort : retenu ; non mesuré.

**A12. Impossibilité d'un budget borné sans borne inférieure sur la fréquence ; garantie disjonctive** (synonymes : Halmos 1946 ; Bahadur et Savage 1956 ; énoncé E ; « trouver ou certifier que p est sous un seuil »).
- Affirme : sans borne inférieure connue sur p, aucun budget fini ne garantit le succès ; seule tient inconditionnellement la garantie « succès ou certificat p < ε ».
- Sources : [R40A] l. 35-38, l. 57 ; [R40C] l. 34-37, l. 43, l. 52.
- État : PROPOSÉ (Argon et Carbon). Sort : non tranché (réponses non encore lues par une synthèse).

**A13. L'adaptativité consomme la validité du juge** (Dwork et collaborateurs 2015). Sources : [R40] l. 81, D3 l. 243-248 ; [R28O] R3 (MCTS). État : PROPOSÉ. Sort : retenu dans l'esprit de N-053 et N-058 ([CLAUDE] l. 13) ; D3 de la réponse 40 non tranchée.

**A14. Identité des idées** : deux cartes proches en prédiction peuvent venir d'idées différentes ; l'équivalence fonctionnelle n'est décidable que dans une grammaire bornée. Sources : [REC] borne 13 l. 324-326. État : PROPOSÉ. Sort : retenu (voir J7).

**A15. « Forcer » au sens d'un théorème : on force la proposition à prix connu, pas la découverte.**
- Affirme : la garantie vient toujours d'une composante mécanique contrôlée (énumération, mélange défensif, rejet exact, stratification) ; « On ne force la découverte que si l'évidence disponible paie la longueur de description ».
- Sources : [R40] l. 22, l. 83 ; [D40] l. 9, l. 16.
- État : PROPOSÉ (Fable maximal). Sort : non tranché (D1 de la réponse 40 non trouvée tranchée).

---

## 2. Famille B — Bases à battre et contrôles

**B1. Tirages indépendants à coût égal ; meilleur de N** (synonymes : témoin 1 − (1 − w)^N ; « le séquentiel doit battre le meilleur de N tirages »).
- Affirme : toute méthode se juge contre N tirages indépendants au même budget, compté en jetons facturés.
- Sources : [MERE] l. 39-40 ; [N073] § 2 l. 66-92 (protocole occupé, Oved et al. ; six règles de « budget égal ») ; [VEIL] l. 31 ; [VOIS] b1 l. 324.
- État : DÉCIDÉ (N-073, « go recos », [DEC] l. 3369, R-3231) ; ÉPROUVÉ AILLEURS (Fork-and-Flush : meilleur de 4 0,54 contre 0,47, [VOIS] l. 131).
- Sort : retenu comme base obligatoire ; revendication du protocole retirée (occupée).

**B2. Tirage au hasard au gabarit** (« aleatoire »).
- Affirme : des lois tirées au hasard dans la grammaire ; si un proposeur à modèle ne fait pas mieux, la prise « proposeur » tombe.
- Sources : [IO-REF] l. 6-7 ; [IO-TF6] l. 184-185 (hypothèse H-A4-2), l. 261-262 (lecture gelée de l'échec), l. 118 (« 13 % des lois aléatoires de la grammaire portent G ≥ 0,02 »).
- État : CONÇU ; joué à blanc seulement, doublures scriptées : aléatoire [36, 0, 0] ([IO-RTF6] l. 161) ; tour fermé « not sealed and has not been run » ([IO-GH] l. 127) ; course réelle v67 sans bras aléatoire ([IO-BR] l. 235).
- Sort : retenu comme base ; jamais joué contre de vrais proposeurs.

**B3. Chercheur mécanique sans modèle ; énumérateur ordonné par longueur ; recombinaison mécanique bornée** (synonymes : « mecanique », critère de Schwarz ; mère B2 ; énumérateur sans modèle).
- Affirme : un programme ajuste ou énumère les lois de la grammaire ; si un proposeur à modèle ne fait pas mieux, la prise « exploration » tombe ; en pire cas, c'est la meilleure garantie.
- Sources : [IO-REF] l. 8-11 ; [MERE] B2 l. 64-66 ; [R40] l. 67, l. 90-92, D2 l. 237-241 ; [R28M] l. 137, l. 153 ; [SBE] l. 62-63.
- État : ÉPROUVÉ en partie, sur processeur, résultat seulement cité : « ses 23 sur 35 de la v1 » pour le mécanique ([IO-DPROP] l. 31), aucun fichier de résultat versé ; la v2 change de grammaire pour qu'il ne domine plus ; « énumérateur ordonné et valeurs e pondérées » : PROPOSÉ (D2 de la réponse 40, non tranchée).
- Sort : retenu comme base obligatoire partout.

**B4. Énumération exhaustive de la grammaire (garantie déterministe)** : si le langage est fini et le budget couvre le support, succès certain. Sources : [R40A] l. 40-43 ; [R40C] l. 85-88. État : PROPOSÉ. Sort : non tranché.

**B5. Contrôles placebo** (synonymes : vue placebo de même format et longueur, table tirée au hasard ; placebo par monde jumeau ; cartes ou lignes d'un autre monde ; même découpage sans le mécanisme ; réallocation au hasard ; témoin à 1,2 fois les tirages ; mondes sans la structure visée ; permutation commune des noms de traits).
- Affirme : séparer l'information servie de sa seule présence, de sa forme, de la perturbation du contexte ou de l'effectif.
- Sources : [REC] § 10 l. 351-368 ; [RELEVE] § 5 l. 305-321 ; [ORIG] (i) l. 69-80 ; [SBE] l. 163-164 (permutation d'Astra) ; [R28M] l. 153.
- État : PROPOSÉ ; le placebo de réallocation a servi dans l'essai de l'idée 1.2 (voir K1, ÉPROUVÉ).
- Sort : retenu (« réutilisables tels quels », [RELEVE] l. 306-308).

**B6. Reprise du meilleur à contexte neuf** (Fork-and-Flush).
- Sources : [VOIS] l. 43-46 et table l. 126-135 ; mot de Lazar ([DEC] l. 2487, R-2528 : « Témoin à ajouter »).
- État : ÉPROUVÉ AILLEURS (0,78 contre 0,47 et 0,54, 13 tâches, cité par R-2528) ; DÉCIDÉ comme témoin de la course à plusieurs générations.
- Sort : retenu.

**B7. Pseudo-familles** : une famille de modèles coupée au hasard, témoin de la pluralité des familles. Sources : [SV9] l. 69. État : PROPOSÉ. Sort : retenu par la synthèse, non mesuré.

**B8. Témoin « popularité seule » et rétrodiction inversée** (bisociation). Sources : [SBIS] l. 90, l. 55-56, décision 1 l. 188-196 ; [DEC] l. 1107 (R-878, gabarit des six garde-fous « go recos »). État : DÉCIDÉ (gabarit obligatoire sur littérature réelle) ; non joué. Sort : retenu.

**B9. Témoins de composition** : « même effectif, sans échange » et « chaque fournisseur seul, k tirages, coût apparié », garde de troncature par bras. Sources : [N073] § 5 l. 128-133 ; [VEIL] idée 8 l. 58. État : DÉCIDÉ (à l'étape 2, sur devis). Sort : retenu, non joué.

---

## 3. Famille C — Choisir ce qu'on explore : vue, focalisations, trous, hors bassins

**C1. Stratégie « hors des bassins déjà promus »** (synonymes : `hors_bassins_promus` ; voisine : `au_dela_du_connu`, « un trait que le prédicteur connu du moniteur pèse peu »).
- Affirme : le proposeur vise un couple (moniteur, trait) qu'aucune fiche promue ne couvre encore.
- Sources : [IO-PROP] l. 3-4 (« yes go » de Lazar du 27 octobre), l. 40-41 ; [IO-SIM] l. 410-414 (jouée par un tirage uniforme parmi les couples libres) ; [IO-TEST] l. 104.
- État : CONÇU (codée, essayée en simulation seulement) ; aucune mesure de promues par stratégie trouvée.
- Sort : décidée en octobre (« yes go »), non mesurée ; antécédent de C3.

**C2. Catalogue de stratégies déclarées, à liberté bornée** (`monotone_un_trait`, `interaction_deux_traits`, `difference_sous_populations`, `correction_eliminee`, `transposition_moniteur`, `ajustee_sur_developpement`, plus C1).
- Affirme : le proposeur déclare la stratégie employée ; on mesure lesquelles produisent des promues.
- Sources : [IO-PROP] l. 10-14, l. 35-45 ; [IO-CONC7] l. 74 ; [IO-DC1] l. 14 (lecture fixée : « l'exploration promeut au moins une fiche par sous-population ») ; [IO-README] l. 129.
- État : ÉPROUVÉ en partie, sur processeur, avec proposeur scripté (aveugle contre exploration) : « the hoped-for advantage of exploratory proposers did not show (1 promoted card in each arm) » ([IO-README] l. 129) ; aucune mesure par stratégie avec un vrai modèle.
- Sort : non tranché ; la lecture fixée n'est pas tenue dans le sens espéré.

**C3. Liste des paires de traits que l'archive ne croise pas** (synonymes : V2 ; table syntaxique des comptes par trait et par paire ; forme minimale à laquelle se ramènent V1, le graphe de dépendance, la table des produits absents, les cavités d'un complexe simplicial, la table de Walsh).
- Affirme : servir l'archive entière avec la table binaire des paires non croisées ; un proposeur y verrait où écrire une interaction.
- Sources : [REC] V2 l. 58-72 ; [SBE] l. 29-31, recommandation rang 2 l. 329 ; [RELEVE] 2.2 (a) l. 182-206 ; [R28M] étape 3 l. 184 ; [R28H] étape 2 l. 194 ; [R28O] E1.
- État : PROPOSÉ (survivante pleine) ; jamais éprouvée.
- Sort : retenue au rang 2 de la recommandation de la synthèse, « non tranchée » par Lazar ([DEC] l. 2500, R-2541). Objection centrale : « Aucun fait ne le dit » sur l'effet de la vue ([SBE] l. 37-38).

**C4. Décomposition orthogonale de l'archive par inversion de Möbius** (V1). [REC] l. 51-56. PROPOSÉ. Retirée : sous traits dépendants, termes ni uniques ni orthogonaux ; se réduit à C3.

**C5. Code couvrant sur les sous-ensembles de traits** (V4). [REC] l. 90-93. PROPOSÉ. Retiré : une idée est une fonction, non un sous-ensemble.

**C6. Homologie de l'archive** (V9 ; homologie persistante, cavités simpliciales). [REC] l. 127-131. PROPOSÉ. Retirée : peu de lois, peu de traits ; se ramène à C3.

**C7. Plan combinatoire qui répartit des focalisations** (synonymes : V3 ; tableaux couvrants ou orthogonaux de force t ; plans factoriels fractionnaires ; mère B2 « couvrir toutes les paires en peu de fiches » ; « lentille » de strate par proposeur tirée au sort).
- Affirme : chaque combinaison de t facteurs est mise devant au moins un appel ; un plan équilibré ne fait pas moins bien que des blocs indépendants (inégalité d'Astra).
- Sources : [REC] V3 l. 74-88 et borne 11 l. 319-321 ; [MERE] B2 l. 64-66 ; [SBE] l. 158-162, rang 3 l. 330 ; [RELEVE] 2.3 l. 208-222.
- État : PROPOSÉ ; la borne 11 (tableaux couvrants binaires de force 2) ÉPROUVÉE par calcul exhaustif : « 3 facteurs pour 4 appels, 4 pour 5, 10 pour 6, 15 pour 7 » ([REC] l. 320-321), la formule du tour était fausse.
- Sort : survivante, rang 3, « seulement si V2 montre un levier ».

**C8. Dictionnaire de directions par moments orthogonaux** (V5). [REC] l. 95-105. PROPOSÉ. Maintenu avec corrections ; risque de coïncidence avec le monde planté.

**C9. Tirage déterminantal et répulsion** (synonymes : processus ponctuel déterminantal sur les vues V6 ; noyau de recombinaison ; sélection répulsive mère A2 ; tirage déterminantal des représentants ; ensembles à faible dispersion ; répulsion en plongement).
- Affirme : favoriser des lots dissemblables ; garantie sous indépendance des réponses (pas pire que le tirage indépendant de mêmes marges).
- Sources : [REC] V6 l. 107-114, G3 l. 216-217 ; [MERE] A2 l. 49-51 ; [RECOMB] l. 8 ; [IO-RECOMB] l. 9-11 ; [R40] méthode 5 l. 124-129 ; [R28M] l. 134.
- État : ÉPROUVÉ sur processeur pour la recombinaison : noyau d'origine « non semi-défini positif (1 000 violations sur 1 000) » ([RECOMB] l. 8 ; [DEC] l. 751, R-527) ; forme corrigée qui « perd de 4,8 et 2,2 points » contre le tirage stratifié dans l'essai des ponts plantés ([IO-RECOMB] l. 10-11). Sur les vues : PROPOSÉ.
- Sort : noyau d'origine écarté ; stratifié par défaut (R-527) ; sur les vues, maintenu en duel séparé ; « diversité des vues, non des sorties » ([R28M] l. 134).

**C10. Plan sur des vues équivalentes** (V7, renommage des traits, inversion d'un codage). [REC] l. 116-120. PROPOSÉ. Suspendu à un essai d'équivariance.

**C11. Acquisition par variance d'un processus gaussien** (V8). [REC] l. 122-125. PROPOSÉ. Retirée : soit un verdict servi, soit une prime d'éloignement de l'archive.

**C12. Focalisations tirées des résidus ; balayage multi-échelles ; canal d'épisodes publics avec issues** (synonymes : V10, V11 ; table croisée sur 2 000 épisodes publics, forme (b) de la table descriptive ; crible (i) « placebo par monde jumeau »).
- Affirme : des données publiques avec issues, disjointes des tirages du juge, rendraient visible une composante nulle en moyenne.
- Sources : [REC] l. 133-144 ; [SBE] l. 165-167 (Kimi à part : « une pièce nouvelle ») ; [RELEVE] 2.2 (b) l. 188-205 ; [ORIG] (i) l. 69-80, devis 17 USD attendus, 123 au pire (l. 21).
- État : CONÇU (note de conception avec devis) ; non joué.
- Sort : nœud « dessin neuf » (une donnée entre dans la vue) ; non tranché.

**C13. Portefeuille de questions servies (missions)** (synonymes : une mission par appel tirée par permutation scellée ; consigne de diversité tirée au sort).
- Sources : [SDIV] rang 3 l. 71-81 ; [VOIS] b4 l. 327 ; [MERE] A4, B1 (missions).
- État : PROPOSÉ ; ÉPROUVÉ AILLEURS (Fork-and-Flush : consigne de diversité « aucun effet mesurable sur la branche retenue », [VOIS] l. 135 ; « précédent nul (46 % contre 50 %) », [VOIS] l. 327).
- Sort : gardé pour après le duel « le monde offre-t-il, les proposeurs prennent-ils ? » ([SDIV] l. 138-144).

**C14. Exclure le banal** (synonymes : adversaire qui prédit l'idée banale et la retire ; liste d'exclusion des classes spontanément fréquentes ; exclusion par invite, par rejet ou par grammaire ; rejet exact par programme ; tirage sans remise ; Gumbel-top-k ; Sourati et Evans « human-aware »).
- Affirme : retirer les classes fréquentes déplace la masse vers les autres ; le rejet exact par programme donne la loi conditionnelle, gain au plus 1/(1 − p(S)) ; « Exclure par l'invite n'est pas conditionner ».
- Sources : [R28M] famille 4 l. 96-100, D2 l. 206-211 ; [R28H] famille 4 l. 99-104, D3 l. 227-232 ; [R28O] E2 l. 236 ; [SV9] l. 52 ; [R40] (d) l. 70, méthode 2 l. 104-109, l. 175, l. 199.
- État : PROPOSÉ.
- Sort : non tranché ; Fable maximal recommande « permettre au banc seulement […] avec placebo » (confiance 0,65), Fable très haut l'option B (0,6) ; frotte la règle « aucun score de nouveauté servi à un agent ».

**C15. Stratification par cellule publique ; histogramme plat ; métadynamique** (synonymes : « remplir les bassins visités » ; Wang-Landau ; quota par cellule ; certificat de masse restante par cellule).
- Affirme : déposer un biais sur les cellules visitées et servir des missions qui les excluent ; ou allouer par cellule, si bien que la largeur devient la largeur conditionnelle à la cellule.
- Sources : [MERE] A3 l. 52-55 ; [R40] méthode 4 l. 117-122, combinaison B l. 185-187 ; [SBE] l. 181-187.
- État : PROPOSÉ (mère seule, non critiquée dans le tour).
- Sort : non tranché ; « ne garantit rien si le puits est étroit dans toutes les cellules » ([R40] l. 120) ; rouvre le rejet du masquage d'archive ([SBE] l. 181-187).

**C16. Qualité-diversité ; cartes d'élites ; retourner puis explorer ; nouveauté seule** (MAP-Elites, Go-Explore, Lehman et Stanley).
- Sources : [MERE] A4 l. 56-58 ; [R28M] famille 1 l. 77-81 ; [R28H] famille 1 ; [R28O] R2 (tableau, l. 128-139) ; [SV9] l. 55, l. 73 ; [R40] méthode 4.
- État : PROPOSÉ.
- Sort : « structurer l'archive servie, non récompenser » (Fable maximal, [R28M] l. 81) ; contre Opus : seulement dans l'orchestrateur, « jamais comme texte servi aux proposeurs » ([R28O] R2) ; « la plus exposée au surajustement » ([SV9] l. 73) ; sans borne de temps d'atteinte connue ([R40] l. 120). Non tranché.

**C17. Nourrir les proposeurs de données propres au programme** (synonymes : données que les concurrents n'ont pas vues ; rareté sous les modèles des concurrents ; ancrage par coupure temporelle).
- Sources : [R28O] l. 28, l. 38, l. 139, D-5 l. 303-308.
- État : PROPOSÉ (Opus, recommandation (a), confiance 0,6).
- Sort : non tranché.

**C18. Faire varier la question, pas seulement les réponses ; reformuler le problème.** [R28O] l. 42 ; [R28O] E2 l. 236. PROPOSÉ. Non tranché.

**C19. Abstraction et transfert : chercher la mesure sous laquelle le puits est large** (synonymes : « Retourner la métaphore » ; puits « transférable », commun sous un autre habillage ; analogie).
- Affirme : « Un puits n'est étroit que sous une mesure » ; chercher le proposeur, la représentation ou le domaine sous lequel il est large.
- Sources : [R28M] l. 26, famille 6 l. 107-110, monde (iii) l. 145 ; [R28H] famille 6 l. 112-116 ; [R28O] R2.
- État : PROPOSÉ. Sort : non tranché (banc proposé avec une famille de mondes « transférables »).

---

## 4. Famille D — Changer la représentation dans laquelle le proposeur écrit

**D1. Contrastes orthogonaux compilables** (I1). Bibliothèque de produits de traits ±1 ; un compilateur traduit dans la grammaire. [REC] l. 152-162 ; [SBE] rang 4 l. 331. PROPOSÉ. Survivante, rang 4 ; risque « aide de syntaxe » et forme assortie au monde.

**D2. Opérateur d'expansion** (I2) : l'orchestrateur ajoute le terme croisé. [REC] l. 164-166. PROPOSÉ. Retiré (fabrique des cartes hors du nul).

**D3. Carte de déviation dans le groupe des log-cotes** (I3 ; interface en écarts, Argon à part). [REC] l. 168-173 ; [SBE] l. 147-149. PROPOSÉ. Non critiquée ; preuve à fournir sur l'enveloppe log-linéaire.

---

## 5. Famille E — Déformer la loi des propositions (échantillonnage)

**E1. Température et échantillonnage contre la vraisemblance** (synonymes : tempérer q^β ; seuil relatif min-p ; échantillonnage verbalisé ; pénalité de probabilité ; « listes longues dont on écarte le début »).
- Sources : [MERE] A1 l. 47-48 ; [R28M] famille 2 l. 83-88, étape 3 l. 184 ; [R28O] R2 et E2 ; [R40] méthode 3 l. 111-115, l. 196, étape 3 l. 211 ; [SV9] l. 53 ; [CONC3G] l. 98 (témoin faux : « Montée de la température d'échantillonnage » présentée comme inédite).
- État : PROPOSÉ ; jamais éprouvé chez nous.
- Sort : « agissent sur les jetons, non sur les classes » ([R40] l. 196) ; seule question ouverte : optimum intérieur sous décodage contraint ([R40] l. 113-115). B (Opus) a retiré la « garantie » par la température ([SV9] l. 24).

**E2. Modèles de base, non alignés.** [SV9] l. 51, l. 71 ; [R28O] R2. PROPOSÉ. Retenue 5 de la synthèse ; « aucune [étude] sur des idées vérifiées » ([SV9] l. 71).

**E3. Mélange défensif ; recherche universelle de Levin** : une part ε du budget suit une loi mécanique ; garantit q(c) ≥ ε·u(c) quel que soit le modèle ; temps d'atteinte de l'ordre de 2^L(c). [R40] (b) l. 68, (c) l. 69, méthode 1 l. 97-102, combinaison A l. 182-184. PROPOSÉ (Fable maximal). Non tranché ; « rien hors grammaire ».

**E4. Entropie croisée ; échantillonnage préférentiel adaptatif.** [R40] méthode 7 l. 138-142 (« se referme sur le premier bassin trouvé, donc le plus large ») ; [R28M] l. 130 (gain au plus p′/p) ; [R40A] l. 89. PROPOSÉ. Écartée comme moyen de forcer ([R40] l. 201).

**E5. Recuit, tempering parallèle, îles et échange de répliques.** [MERE] C3 l. 76-78 ; [R40] méthode 8 l. 144-148 (« mélange lentement précisément quand un mode étroit côtoie un mode large », Woodard et al.) ; [REC] V12 l. 146-148. PROPOSÉ. Écartée comme méthode servie ; hors ligne seulement.

**E6. Méthodes de Stein et transport optimal.** [R40] méthode 11 l. 161-164 : « pas de cible ». PROPOSÉ. Écartée (usage restant : mesurer l'écart entre deux lots).

---

## 6. Famille F — Dessin de la course en plusieurs pas, chaînes, marchepieds, calendrier

**F1. Marchepieds** (synonymes : tirage stratifié à marchepieds ; missions « sachant l'élément X de l'archive, qu'est-ce qui ne vaut que sous X ? » ; lignées fécondes ; pierres de gué).
- Affirme : un bassin étroit s'atteint par une idée intermédiaire ; les marchepieds n'aident que si les vraies associations se regroupent.
- Sources : [IO-RECOMB] l. 15-19 ; [IO-SIM] l. 10-12 (fécondité simulée 0,85 contre 0,35) ; [IO-DCYCLE] l. 14-18 ; [MERE] B1 l. 61-63.
- État : CONÇU (démonstration à deux faces écrite) ; aucun résultat versé ; prémisse présente dans le seul monde simulé.
- Sort : non tranché.

**F2. Fractionnement multiniveau sur un graphe public de prérequis** (synonymes : C3 de Kimi ; Cérou et Guyader ; affectation des appels à la frontière de l'archive).
- Sources : [REC] C3 l. 192-197 ; [SBE] rang 5 l. 332 ; [R40] méthode 6 l. 131-136, combinaison C l. 188-190 ; [R28M] l. 131.
- État : PROPOSÉ (non critiqué dans le tour).
- Sort : rang 5, « seule voie qui vise la profondeur en chaîne » ; « sans palier, il se réduit au tirage brut ».

**F3. Arbres de continuation sans récompense intermédiaire** (C2 d'Astra ; variante « six constats puis une session par constat »). [REC] l. 185-190 ; [RELEVE] 2.1 l. 166-167, l. 177-178. PROPOSÉ. Non critiqué.

**F4. Synthèse typée de prolongements** (C1 ; longueur de description préfixe, budgets croissants). [REC] l. 177-183. PROPOSÉ. Suspendue (« un a priori syntaxique »).

**F5. Curriculum vers des problèmes plus durs** (POET ; conception non supervisée d'environnements). [R28M] l. 112-114 ; [R28H] l. 118-122 ; [R28O] R2. PROPOSÉ. « rien devant un puits sans parent ».

**F6. Une carte par session au lieu de six dans un même appel** (décorréler les cartes d'un appel). [RELEVE] 2.1 l. 160-180 : « la première carte attire les cinq autres ». PROPOSÉ (fiches de l'organisme sur sa propre conception). Non tranché ; devis de « quelques dizaines de dollars » selon les fiches.

**F7. Proposeurs en série** (crible (ii) : chaque session voit les cartes brutes des précédents). [ORIG] (ii) l. 110-120, devis 63,30 attendus, 483 au pire (l. 22) ; [RELEVE] 3.2. CONÇU. Non tranché ; question : dispersion ou grégarisme.

**F8. Deux passes : traits choisis pas cher, loi écrite cher** (crible (iii)). [ORIG] (iii) l. 142-152 ; [DEC] l. 2937, R-2977 (brouillon 1 du préenregistrement, devis 58 USD attendus). CONÇU. Non joué (aucun lancement trouvé).

**F9. Demi-générations** (crible (iv) : archive mise à jour à mi-génération). [ORIG] (iv) l. 173-183 ; [RELEVE] 4.1. CONÇU. Non joué.

**F10. Programme à archive complète** (ne rien perdre de ce qui est proposé ; Ecoffet 2021). [R28M] l. 116-121 ; [R28H] l. 124-130. PROPOSÉ. Garantit l'audit, pas la découverte ; l'archive ancre.

---

## 7. Famille G — Recombinaison et bisociation (domaines disjoints)

**G1. Règle « loin en domaine, proche en concept »** (bras basique du bisociateur).
- Sources : [IO-BISOC] l. 24-26 ; [PRA2] l. 20 ; [DEC] l. 1135, R-906 ; [PAGE] l. 35.
- État : CONÇU (codée, versions 53 à 55) ; non jouée en course réelle (second tour réel « without the bisociation board », [IO-README] l. 136 ; hors portée du tour fermé, [IO-TF6] l. 555).
- Sort : « Occupée en partie (la forme seulement) » ([PRA2] l. 20). Trou de dessin : « pas de bras hasard » ([IO-BISOC] l. 3).

**G2. Trou à structure commune** (synonymes : canal faible, structure commune forte ; bras méta ; trous structuraux de Burt).
- Sources : [SBIS] l. 45-47, mesure E1′ l. 166-172 ; [IO-BISOC] l. 5-11 ; [QFUS] l. 10.
- État : CONÇU (bras méta exige une annexe scellée) ; non joué.
- Sort : retenu comme profil à tester (E1′), avec six garde-fous.

**G3. Prédiction de liens « jamais reliés » ; idées dans l'air du temps** (synonymes : Gu et Krenn 2024 ; substitut de Gu-Krenn ; Impact4Cast).
- Sources : [IO-BISOC] l. 12-18 ; [SBIS] l. 89-99 (« Reproduire Gu-Krenn avant de s'en servir », l. 90) ; [DEC] l. 1102, R-873 ; [DEC] l. 1130, R-901 (substitut « go ») ; [MANDAT] l. 8.
- État : CONÇU (préenregistrement v2 non scellé ; rien exécuté, R-873) ; valeurs publiées vérifiées sur PDF.
- Sort : substitut accordé ; reproduction non faite (non trouvée).

**G4. Recombinaison bisociative par fusion : la fille doit prédire plus que ses parents.**
- Sources : [RECOMB] l. 8-12, l. 24-28, l. 30-34 ; [IO-RECOMB] l. 1-7 ; [DEC] l. 751, R-527.
- État : PROPOSÉ ; le critère de contenu est jugé « franchissable à coût nul » par des tricheurs scriptés (« une simple enveloppe bat la conjonction », [RECOMB] l. 10) ; résultat du banc des tricheurs non trouvé.
- Sort : première expérience décidée « valider le critère de contenu contre une batterie de tricheurs » (R-527) ; « tout HYPOTHÈSE » sur l'apport de la fusion par modèle ([RECOMB] l. 30-32).

**G5. Tirage stratifié par domaines estimés** (avec opérateur forcé après tirage, filtre de compatibilité, abstention). [RECOMB] l. 12, l. 40 ; [IO-RECOMB] l. 9-13. ÉPROUVÉ (voir C9 : bat le noyau corrigé). Retenu par défaut.

**G6. Combinaison atypique sur fond conventionnel ; recombinaison contrainte** (Uzzi 2013, Fleming 2001 ; Swanson 1986). [R28M] famille 5 l. 102-105 ; [R28O] R2 ; [PAGE] l. 35. PROPOSÉ (antériorités citées de mémoire). « couverture des affectations, non des idées ».

**G7. Fertilité d'une paire ; sur-additivité F = R(A∪B) − R(A) − R(B) + R(A∩B).**
- Sources : [SBIS] l. 24, B l. 68-87 ; [QFUS] l. 12 ; [SQ7] l. 33-35.
- État : PROPOSÉ ; « HYPOTHÈSE » pour A et D ; F faussée par le budget et la combinatoire ; « aucune définition prospective de la fertilité n'est établie » ([SQ7] l. 35).
- Sort : non tranché ; deux candidates prospectives à contre-lire.

**G8. Canal social** (Sourati et Evans, « human versus alien »).
- Sources : [DEC] l. 1136, R-907 (« on pourrait en faire un bras. : go ») ; [PRA2] l. 24 ; [R28M] famille 4 l. 98.
- État : DÉCIDÉ (bras ajouté comme base de comparaison reprise, non revendication) ; ÉPROUVÉ AILLEURS (« occupé avec résultats », R-907).
- Sort : retenu comme bras ; non joué (non trouvé).

**G9. Base de ponts datés, rétrodiction inversée, graphe amputé des ponts, étiquette de pont indépendante des citations.** [SBIS] l. 52-61, décision 1 l. 188-196 ; [DEC] l. 1107, R-878. DÉCIDÉ (gabarit obligatoire) ; non joué. Retenu.

---

## 8. Famille H — Mécanismes d'allumage d'une idée ou d'un champ

**H1. Transition de phase ; criticité.**
- Affirme : la probabilité de reprise d'une paire passerait par un seuil fortement non linéaire.
- Sources : [QFUS] l. 12 ; [SBIS] l. 25, l. 30 (« le pic de variance binomiale pris pour de la criticité »), décision 4 l. 216-224.
- État : PROPOSÉ ; « HYPOTHÈSE pour les quatre ».
- Sort : nœud proposé (suspension jusqu'à l'étalonnage E2′, puis retrait s'il échoue) ; issue non trouvée.

**H2. Émergence par essaims communicants, contre tentatives indépendantes ou peu de modèles à réflexion profonde.**
- Sources : [QFUS] l. 18 ; [SBIS] l. 26, E l. 113-124, l. 184-185 ; [SV9] l. 54 (isolement des appels, sans débat ni vote).
- État : PROPOSÉ (HYPOTHÈSE pour A et B) ; aucune ablation publiée des systèmes cités ([SBIS] l. 114).
- Sort : dépense non demandée ([SBIS] décision 7) ; non tranché.

**H3. Allumage comme ensemble autocatalytique de fiches** (synonymes : fermeture RAF ; taux de reproduction R0, R_endo ; catalyseur nécessaire).
- Affirme : un champ s'allume quand un ensemble de fiches se catalyse lui-même.
- Sources : [SQ7] l. 7, l. 19 (« confondaient toutes deux fermeture et autocatalyse »), l. 30 (seuil « en écart à son espérance sous appariement aléatoire à dose égale »), D7-1 à D7-5 l. 86-94 ; [DEC] l. 1113, R-884.
- État : PROPOSÉ ; fermeture naïve triviale sur un graphe sans cycle.
- Sort : « lue, non reprise » ([INV] l. 75) ; défauts D7-1 à D7-4 sans issue trouvée.

**H4. Protocelles : un parent contre deux parents ; le catalyseur est le bisociateur.**
- Sources : [PROTO1] l. 69-73, l. 134, l. 256 ; [PROTO2] l. 183.
- État : PROPOSÉ ; « Aucune prédiction globale d'allumage n'est signée sans condition » ([PROTO1] l. 73).
- Sort : première mesure « jamais montée » ([INV] l. 77, l. 63).

**H5. Seuil d'allumage d'un champ (Bettencourt, R0 > 1).** [QFUS] l. 22 ; [SBIS] l. 39, G l. 151-162 ; décision 5 (lecture des PDF arXiv). PROPOSÉ (RAPPORTÉ sans PDF). « personne ne donne de référence exacte » ; lecture non trouvée faite.

**H6. Idées « dans l'air » qui découlent de découvertes antérieures** (second cas de l'allumage du mandat). [MANDAT] l. 8, l. 17 ; [PAGE] l. 154. PROPOSÉ (mandat en cours). Rattaché à G3 et à la rétrodiction ; non mesuré.

**H7. Causes de la fertilité par apprentissage ; identification** (question D de la bisociation ; question 6). [QFUS] l. 16 ; [SBIS] D l. 101-111 ; [DEC] l. 1113, R-884 (« seul “entraînement sur affectation biaisée, puis épreuve randomisée” sépare estimer d'identifier »). PROPOSÉ. Question 6 « lue, non reprise » ([INV] l. 74).

---

## 9. Famille I — Nouveauté, moisson, antériorité

**I1. Aucune récompense numérique de la nouveauté, ni dans le juge, ni servie à un agent** (synonymes : invariant N-053 ; mesures de nouveauté consignées, jamais servies ; proposeur qui ne voit « jamais la richesse »).
- Sources : [SDIV] l. 25-27 ; [REC] l. 47 ; [SBE] l. 65 ; [IO-IDEA] l. 92-93 ; [IO-PROP] l. 7 ; [CLAUDE] l. 13 (N-053).
- État : DÉCIDÉ (invariant). Sort : retenu partout ; frottement avec C14 et L3.

**I2. Moissonneur de nouveauté** (arXiv et OpenAlex, métadonnées et résumés, touches « non opposables »).
- Sources : [IO-MOIS] l. 1-5 ; [SMOIS] (boucle moisson, fiches, bisociateur ; Q4 allocation l. 138-153) ; [DEC] l. 1189, R-960.
- État : CONÇU (relais factice) : « rien de réel ici » ([IO-MOIS] l. 5).
- Sort : non joué en réel.

**I3. Originalité comme note de grille des juges** (« inedite », « transposition », « occupee »). [IO-IDEA] l. 183. CONÇU (en usage dans la course d'idéation). Matériau, jamais preuve.

**I4. Nouveauté définie à l'oracle : gain d'information au-delà de l'archive (ΔG).** [IO-TF6] l. 121. CONÇU (brouillon non scellé). Non joué.

**I5. Témoins « redites vraies » ; témoins « vrais mais dérivables ».**
- Sources : [IO-JUG] l. 90 ; [VEIL] idée 1 l. 51 ; [N073] § 7 l. 146-149 (N6).
- État : DÉCIDÉ (audit N6, « chacun préenregistré […] et contre-lu ») ; non fait (non trouvé).
- Sort : retenu (« Seule mesure qui donne à la revendication 1 un chiffre propre », [VEIL] l. 51).

**I6. Redite exacte de la loi du monde par un proposeur** (attaque de Goodhart W2). [IO-README] l. 140 : « 42 of the 48 reproduce the world's own law exactly ». ÉPROUVÉ (course réelle). Constat : un critère de nouveauté peut être violé sans optimisation contre le juge.

**I7. Distance à un corpus, densité en plongement, score de Vendi.** [R28M] l. 71, l. 133 ; [R28H] l. 65 ; [R28O] R3 ; [SV9] l. 46. PROPOSÉ. Description seulement, jamais critère ; Argon a retiré sa distance de compression ([SV9] l. 28).

**I8. Surprise et curiosité.** [R28M] l. 132 ; [R40] l. 197 (« attirées par le bruit ») ; [R28M] l. 100 (Burda 2019). PROPOSÉ. Écartées.

**I9. Recherche d'antériorité par un tiers ; jury aveugle étalonné par des leurres.** [R28M] l. 46 ; [SMATH] l. 23 (« nouveauté jugée par un humain du domaine ») ; GO-2026-11-22-42 cité par [PAGE] l. 115. PROPOSÉ ; pour les mathématiques, « option A (recherche d'antériorité par étages) » accordée selon [PAGE] l. 115.

---

## 10. Famille J — Mesurer la rareté, la masse non vue et la réponse à la vue

**J1. Masse manquante** (synonymes : Good 1953, formule de Turing ; Good et Toulmin 1956 ; Chao, Chao2 ; estimateurs d'espèces non vues ; courbe d'accumulation ; McAllester et Schapire ; « pénaliser par la masse manquante »).
- Affirme : la part des classes vues une seule fois estime la masse jamais vue ; règle d'arrêt et chiffre de « ce qu'il reste à trouver ».
- Sources : [TIII] l. 63, l. 82, l. 86 (« Famille d'idées “pénaliser par la masse manquante” »), l. 146-150 (incidence contre abondance) ; [MERE] E1 l. 92-94 ; [CONC3G] l. 95 (témoin vrai) ; [R28M] l. 129 ; [R28H] l. 24, l. 62 ; [R28O] l. 150 ; [SV9] l. 48 ; [R40] (e) l. 71 ; [MANDAT] l. 10.
- État : PROPOSÉ ; jamais validée contre l'oracle chez nous.
- Sort : « diagnostic agrégé, jamais à une idée seule » ([SV9] l. 48) ; mesure descriptive ([SBE] l. 340) ; version d'abondance critiquée au profit de l'incidence ([TIII] l. 149, l. 322).

**J2. Rareté certifiée sur un panel indépendant, sous une loi de tirage figée** (rareté à trois états : rare certifiée, non rare, indéterminée).
- Sources : [SV9] l. 8, l. 47, retenue 1 l. 63, l. 132-133 ; [R28M] l. 64 (« inférieure à environ 3/N »).
- État : PROPOSÉ (adoptée par les six modèles au troisième temps).
- Sort : retenue en tête ; « un panel fini ne distingue jamais une idée hors support d'une idée très rare » ([SV9] l. 133).

**J3. Banc à puits plantés et courbe dose-réponse** (synonymes : mondes à largeur et profondeur réglées puis estimées ; puits sans parent comme contrôle négatif ; « puits impossibles comme détecteurs de fuite » ; familles tenues à l'écart).
- Sources : [MERE] E2 l. 95-97 ; [R28M] § 4 l. 139-166 ; [R28H] C4 l. 149-174 ; [R28O] R4 et l. 41, D-4 l. 297-301 ; [R40] l. 31, critère R l. 95 ; [D28] l. 15.
- État : PROPOSÉ ; jamais monté.
- Sort : « expérience décisive préenregistrable » ; non tranché (D-4 d'Opus non trouvée tranchée).

**J4. Audit des pertes ; diagnostic de l'entonnoir** (jamais proposée, ou proposée puis perdue ?).
- Sources : [REC] § 9 l. 339-340 ; [R28M] l. 23, étape 0 l. 181, D1 ; [R28H] l. 23 ; [R28O] E0 l. 234, D-2 l. 285-290.
- État : PROPOSÉ (gratuit, sur journaux bruts).
- Sort : recommandé en premier par Fable (0,85) et Opus (0,8) ; non tranché, non fait.

**J5. Loi spontanée des proposeurs** (rang-fréquence, masse non vue, recouvrement entre familles, capture et recapture de Lincoln et Petersen, saturation).
- Sources : [R28M] l. 25, étape 1 l. 182 ; [R28H] l. 24-25, étape 1 ; [R28O] R3 l. 150.
- État : PROPOSÉ. Sort : non fait ; indice avancé « des familles différentes partagent les mêmes bassins » (HYPOTHÈSE, [R28M] l. 25).

**J6. Réactivité de la loi des propositions à la vue** (« inconnue centrale » ; essai « garde et levier sur un monde sans interaction »).
- Sources : [SBE] l. 37-38, § 6 l. 258-261 ; [REC] § 9 l. 332-333 ; [R28M] étape 3 ; [R28H] étape 2 l. 194 ; [R28O] E1 ; [RELEVE] § 7 point 5.
- État : PROPOSÉ ; « Aucun fait ne le dit ».
- Sort : retenu comme premier essai avec proposeurs ; non fait.

**J7. Identité d'une idée par signature d'exécution sur des sondes** (synonymes : classes fonctionnelles ; prédictions sur un jeu public ; canonisation ; regroupement fonctionnel).
- Sources : [SV9] l. 46, l. 88 ; [R28H] C1 l. 60 ; [R28O] R3.
- État : PROPOSÉ (six modèles sur six).
- Sort : retenu ; désaccord ouvert sur l'arbre syntaxique.

**J8. Mesure de la diversité par couverture d'oracle** (composantes plantées certifiées couvertes ; nombre effectif N_eff descriptif).
- Sources : [SDIV] § 2 l. 99-117 ; [DEC] l. 2428, R-2469 ; [VOIS] l. 289.
- État : CONÇU (conception du monde riche, outils et sorties scellés selon R-2469).
- Sort : retenu pour la course à plusieurs générations ; « ouvert » au regard des voisins.

**J9. Trois lectures par l'oracle : propositions brutes, représentants, cartes retenues.** [REC] § 10 l. 356 ; [SBE] l. 64 ; [R28M] l. 155. PROPOSÉ. Retenu.

**J10. Tests de collisions et d'autocorrélation du générateur** (indice de Simpson ; Batu et al. 2000 ; taille d'échantillon effective ; test des séquences de Wald et Wolfowitz).
- Sources : [R40A] § 5.1-5.2 l. 131-141 ; [R40C] l. 137-139.
- État : PROPOSÉ (Argon, Carbon). Sort : non tranché.

**J11. Grandeurs : largeur, profondeur, justesse, fécondité par ablation ; mesure à deux références ; grandeur visée par million de jetons.**
- Sources : [R28M] § 1 l. 60-71 ; [R28H] C1 l. 57-72 ; [R28O] R1, D-1 l. 278-284 ; [D28] l. 12.
- État : PROPOSÉ. Sort : D-1 d'Opus ((a) mesure seulement, (b) après le banc) non trouvée tranchée.

**J12. Seuil de rentabilité d'une méthode : gain d'efficacité λ = p/p₀ supérieur au surcoût κ.** [R28O] l. 43, l. 166. PROPOSÉ (Opus, « de ma main », non vérifié par un tiers). Non tranché.

**J13. Audit du contrôle dans la queue sur des « faux naturels » ; essai « témoin contre témoin » avec erreurs injectées et domaine nul.** [SV9] retenue 2 l. 65, l. 81, ordre l. 122-128. PROPOSÉ. Ordre retenu par la synthèse ; non fait.

**J14. Validité externe : rétrodiction sur textes postérieurs à la coupure ; prédictions scellées jugées à l'aveugle.** [R28M] étape 6 l. 187, D3 ; [R28H] A4, étape 6 ; [R28O] E5 ; [SV9] l. 144-145 (« l'hypothèse non testée la plus lourde »). PROPOSÉ. Non tranché.

**J15. Monde plus riche, calibré, avec traits leurres.** [SDIV] rang 1 l. 35-50 ; [DEC] l. 2426, R-2467 (mot de Lazar). DÉCIDÉ (périmètre de la conception) ; CONÇU (R-2469). Retenu.

**J16. Constat de redondance dans les courses réelles** (le défaut que tout ce document vise).
- Sources : [IO-README] l. 135 (« 17 distinct ideas (12 duplicate pairs) ») ; [IO-V67] l. 162 (« ce ne sont pas 11 idées »), l. 190-191.
- État : ÉPROUVÉ (observé en course réelle). Sort : constat ; l'origine (monde pauvre ou convergence des proposeurs) non établie ([SDIV] l. 20-21).

---

## 11. Famille K — Arrêt et allocation

**K1. Arrêt optionnel ; processus de valeurs e ; tirages du juge répartis avec arrêt anticipé** (synonymes : J1 ; surmartingale de test, inégalité de Ville ; idée 1.2 ; allocation par blocs).
- Affirme : une carte à effet confiné à une région rare reçoit plus de tirages sans perte de validité sous toute règle d'arrêt écrite d'avance ; sert la survie, pas la découverte.
- Sources : [REC] J1 l. 229-236 ; [SBE] l. 35-36, rang 1 l. 328 ; [RELEVE] 1.2 l. 116 ; [DEC] l. 2811, R-2851 (« go ») ; [DEC] l. 2838, R-2878 (contre-lecture : conditions « dénominateur fixé d'avance » et « ordre indépendant des valeurs e » non nécessaires ; aucun contre-exemple sur 20 000 générations) ; [DEC] l. 2968, R-3008.
- État : ÉPROUVÉ sur processeur. Résultat tel qu'écrit (R-3008) : verdict « gain de structure » ; « validité tenue (0 promotion sur 500 dans les sept bras) » ; part fixe 41,3 % des générations couvertes, allocation par blocs 86,1 % ; réserves : « banc à 18 cartes non porteuses sur 24 (ne se transpose pas) », l'allocation consomme 67 % du budget.
- Sort : verdict soumis à Lazar pour GO (R13) ; adoption au juge = nœud (modification de sa conception gelée) ; issue non trouvée.

**K2. Bandits extrêmes ; recherche arborescente ; bandit sur les vues** (Carpentier et Valko ; Kocsis et Szepesvári ; X-armed bandits ; bandit à oubli de Neon).
- Sources : [MERE] C1 l. 71-73 ; [REC] V12 l. 146 ; [R28M] l. 135 ; [R28O] R3 ; [R40] (g) l. 73, méthode 9 l. 150-154, l. 202 ; [SV9] l. 58 ; [SMOIS] Q4 l. 138-153.
- État : PROPOSÉ.
- Sort : « bon objectif (le maximum) ; exige une récompense » : hors ligne seulement, sur mondes d'étalonnage ; dans la boucle moisson, « L'option “bandit”, présentée la première, n'est retenue par personne » ([SMOIS] l. 147).

**K3. Uniforme avec arrêt précoce** (élimination successive mécanique ; arrêt par budget). [SMOIS] l. 144, l. 147. PROPOSÉ. Position par défaut de la boucle moisson.

**K4. Portefeuille de proposeurs sous budget, sous-modulaire ; identification hors ligne du meilleur couple « proposeur × vue »** (P1, P2 ; Nemhauser, Wolsey et Fisher ; Audibert, Bubeck et Munos ; optimum relatif à une loi a priori déclarée).
- Sources : [REC] P1 l. 278-283, P2 l. 285-288 ; [R28O] R3 et l. 168.
- État : PROPOSÉ. Sort : P1 suspendue (« les fréquences ne se distinguent pas de zéro au budget d'un pilote »), P2 non critiquée.

**K5. Composition des proposeurs jugée sur l'oracle et le coût, jamais sur le verdict du juge** (seule « récompense » licite ; composition apprise ; voies bon marché avant la voie chère).
- Sources : [SDIV] rang 5 l. 93-97 ; [CLAUDE] l. 13 (N-045, N-058) ; [QBE] l. 19-25.
- État : DÉCIDÉ. Sort : retenu ; « dernier mécanisme à essayer ».

**K6. Le bon marché d'abord ; appeler les proposeurs chers sur le regroupement des doublons** (crible (v) ; instruments locaux à la première génération).
- Sources : [ORIG] (v) l. 207-217, recommandation l. 28-29 (≈ 137 USD attendus avec (iii), confiance 0,55) ; [RELEVE] 4.2 l. 274-286 ; [DEC] l. 2937, R-2977 (brouillon 1 du préenregistrement, 73 USD attendus) ; [DEC] l. 2835, R-2875 (ligne GO-2026-11-15-06, 1 275 USD au pire).
- État : CONÇU (préenregistrements cités au registre ; devis à refaire après le pilote, [DEC] l. 2965, R-3005) ; non joué (non trouvé).
- Sort : accord de dépense pour l'essai, non pour l'adoption ; tension notée avec N-058 au-delà de la première génération (R-2977).

**K7. Arrêter une course stérile et reporter le budget là où l'archive a grandi.** [RELEVE] 4.3 l. 288-303 ; [ORIG] l. 214-217. PROPOSÉ. Écarté (« pilotent le dessin par les promotions du juge », N-058) ; seule la variante sur le regroupement survit (K6).

**K8. Indice de réserve de Weitzman pour l'ordre de vérification.** [R40] (h) l. 74, méthode 12 l. 166-169, combinaison D l. 191-192. PROPOSÉ. Non tranché ; « si les a priori étalonnés se transportent, ce qui n'est pas établi ».

**K9. Contrôle en ligne des fausses découvertes entre générations** (Javanmard et Montanari ; e-BH ; Xu et Ramdas). [R28M] l. 136 ; [R40] méthode 12 ; [SBE] l. 168-170 (« Personne ne traite le second ») ; [REC] l. 337-338. PROPOSÉ. Manque reconnu ; non écrit.

**K10. Stratégies d'allocation « loi mère » et champ moyen de Thouless-Anderson-Palmer** (relève de Gemini). [IO-PROP] l. 21-23, l. 46-49. PROPOSÉ ; « non codées », « à tester comme hypothèse ». Non tranché.

**K11. Règles d'arrêt et de relance à garantie** (règle de Dagum, Karp, Luby et Ross ; test séquentiel de Wald ; redémarrage universel de Luby, Sinclair et Zuckerman ; borne de Clopper et Pearson sur zéro succès).
- Sources : [R40A] l. 71-75, l. 120 ; [R40C] l. 60-63, l. 70-73, l. 80-83, l. 144.
- État : PROPOSÉ (Argon, Carbon). Sort : non tranché.

**K12. Filtrage avant le contrôle coûteux** (dédoublonnage avant le contrôle ; mémoïsation syntaxique de Michie ; cascade par pré-filtrage conforme de Vovk, Gammerman et Shafer ; test par groupes de Dorfman ; filtre syntaxique exact par grammaires attribuées).
- Sources : [SV9] retenue 3 l. 67 ; [R40A] l. 77-82, l. 104-107, l. 143-148 ; [R40C] l. 65-68, l. 75-78, l. 107.
- État : PROPOSÉ. Sort : dédoublonnage retenu par la synthèse (« solidité moyenne ») ; le reste non tranché.

---

## 12. Famille L — Jugement et sélection

**L1. Juge au nul formé des lois connues** (statistique calculée par l'orchestrateur sur engagement scellé ; O2, O4).
- Sources : [CLAUDE] l. 13 (N-064, N-067, N-071) ; [QBE] l. 19-21 ; [VEIL] l. 37 (revendication 1 « occupée en partie »).
- État : DÉCIDÉ (contrainte de toute méthode). Sort : retenu ; seule la réunion des deux moitiés reste revendicable (N-071, [CLAUDE] l. 13).

**L2. Valeur e par strates ou à plusieurs échelles** (mère D1 ; J3 ; la fiche déclare sa région avant les données).
- Sources : [MERE] D1 l. 81-84 ; [REC] J3 l. 243-249 ; [SBE] l. 30-33, l. 80-82, l. 195-200.
- État : PROPOSÉ. Sort : « contredit » (identité d'auto-localisation, A6) ; maintenue « très restreinte » ; l'avis à part d'Argon la maintient sans contradicteur.

**L3. Poids de multiplicité selon la nouveauté ou la géométrie des groupes** (mère D2 ; J5 ; e-BH pondéré).
- Sources : [MERE] D2 l. 85-89 ; [REC] J5 l. 258-263, borne 10 l. 317-318 ; [SBE] l. 33-34, l. 76, l. 284.
- État : PROPOSÉ. Sort : retirée dans le tour (« une prime de nouveauté sous un autre nom ») ; défendue encore par Argon à part et la mère ; « ne pas reprendre J5 » ([SBE] l. 341).

**L4. Martingale à pari localisé, avec nul ponctuel** (J4 ; enveloppe convexe des lois d'archive en chaque point). [REC] l. 251-256 ; [SBE] l. 150-155. PROPOSÉ. Non critiquée ; absorbe toute découverte entre deux lois archivées.

**L5. Valeur e par supremum sur un nul composite explicite** (J6). [REC] l. 265-270. PROPOSÉ. Maintenue sous double condition (garde, non moyen de découverte).

**L6. Filtre mécanique avant le juge contre les recombinaisons par morceaux** (J7). [REC] l. 272-274 ; [R28H] C5 l. 180. PROPOSÉ. Non critiqué.

**L7. Tirages du juge stratifiés selon une loi de traits** (J2 ; fiche « tirer les épisodes frais par strates publiques »).
- Sources : [REC] J2 l. 238-241 ; [RELEVE] 1.3 l. 140-156 ; [SBE] l. 341.
- État : PROPOSÉ. Sort : retirée au tour ; la fiche de l'organisme la reprend sans répondre ; « se tranche sur processeur, en quelques heures » ([RELEVE] l. 155) ; non fait (non trouvé).

**L8. Nul par morceaux limité aux conditions de l'archive ; poids appris du nul** (idée 1.1 ; « jeu de l'idée du poids du nul »).
- Sources : [RELEVE] 1.1 l. 83, § 7 point 1 ; [DEC] l. 2833, R-2873 ; [DEC] l. 2835, R-2875 ; [DEC] l. 3313, R-3196 ; [DEC] l. 3374, R-3236.
- État : ÉPROUVÉ en partie sur processeur : les poids appris « ne sont pas valides » (copie exacte promue « dans 96,5 % à 100 % » des répétitions en ligne, « 64,9 % » sur une moitié, R-2873 ; refait : 98 à 100 % et 37 à 76 %, « 0 sur 300 » avec le maximum certifié, R-2875) ; le jeu de la version 2 a commencé puis attendu le crédit du loueur (R-3196, R-3236) ; verdict non trouvé.
- Sort : Lazar : « on n'abandonne pas au premier echec methodo » (R-2875) ; non tranché.

**L9. Valeurs e pondérées par la longueur de description** (forme du rasoir d'Occam). [R40] (f) l. 72, méthode 10 l. 156-159. PROPOSÉ. Non tranché ; validité sous nul composite à prouver.

**L10. Regroupement des doublons et choix du représentant** (distance prédictive, liaison complète, temps 1 après le test de mort ou temps 2 avant le juge ; jeu public construit par plan G1 ; représentant par couverture dirigée de strates G2 ; pivotage de Cholesky G3 ; divergences localisées G4 ; jamais le représentant par la plus grande valeur e).
- Sources : [SDIV] rang 2 l. 52-69, l. 27-29 ; [REC] G1-G4 l. 201-225 ; [SBE] l. 290 ; [DEC] l. 2428, R-2469 ; [VOIS] l. 288, l. 364-366.
- État : CONÇU (conception du monde riche et des doublons, R-2469) ; G1 survivante, G2 maintenue affaiblie, G3 suspendue, G4 descriptive.
- Sort : temps 1 recommandé ; principe « grouper les idées par ce qu'elles font » est « pris » par Fork-and-Flush ([VOIS] l. 46-47).

**L11. Sélection douce** (Boltzmann à température fixée d'avance, ou une place tirée au sort par génération). [MERE] C2 l. 74-75 ; [SBE] l. 181-187, l. 314. PROPOSÉ (mère seule). Non tranché ; une loi non promue entrerait dans le nul suivant.

**L12. Pari apparié borné pour lire un duel.** [CLAUDE] l. 13 (N-055) ; [IO-DUEL] l. 13. DÉCIDÉ (règle de lecture) ; duel payé CONÇU, aucun résultat ([PAGE] l. 308).

**L13. Second contrôle distinct, réplication ; erreurs corrélées.** [SV9] l. 56, l. 80. PROPOSÉ. « Un second contrôle ne protège pas si ses erreurs sont corrélées » (tranché par calcul).

**L14. Aucun juge-modèle de la nouveauté.** [R28M] l. 71 ; [R28H] A4 l. 45, C5 l. 186 ; [IO-README] l. 136 (« The two LLM judges sat at their ceiling ») ; [D28] l. 12. DÉCIDÉ de fait (ÉPROUVÉ : les juges modèles plafonnent au second tour réel). Retenu.

**L15. Double nul : contre l'archive et contre l'attendu aveugle d'un panel.** [VEIL] idée 10 l. 60. PROPOSÉ. Sur devis ; non tranché.

---

## 13. Famille M — Mémoire et héritage (N-073)

**M1. Héritage d'une génération récompensé** (crédit d'un agent par sa descendance ; rendement à K générations actualisé).
- Sources : [N073] § 1 l. 24-64 ; [VEIL] l. 30 ; [CLAUDE] l. 13 (N-045 v2).
- État : DÉCIDÉ (N-073 : principe occupé, machine de Huxley-Gödel ; liste « Ne plus écrire » l. 32-44).
- Sort : revendication retirée ; seule la lettre de citation est permise.

**M2. Oublier plutôt que continuer ; hériter moins** (synonymes : bras « héritage réduit au meilleur » ; bras « oubli » ; paire « même état » vue pleine contre vue réduite).
- Sources : [VOIS] l. 43-46, table l. 233-239, b2 l. 325 ; [DEC] l. 2487, R-2528 (« go et go bras oublier ») ; [MERE] C3 l. 77 (« l'“oubli” […] rendu continu »).
- État : ÉPROUVÉ AILLEURS (« gain plus grand et dépense à peu près moitié moindre », [VOIS] l. 239) ; DÉCIDÉ comme bras.
- Sort : retenu ; rouvre le rejet du masquage de l'archive (M5).

**M3. Remise à zéro du contexte, déjà en place** (chaque appel en session neuve). [REC] l. 44 ; [SBE] l. 50-53. Constat de dessin. Retenu ; l'ancrage à l'intérieur d'un appel de six cartes reste (F6).

**M4. Mémoire transmise comme registre des tentatives ; plan à trois bras** (sans mémoire, mémoire neuve tenue, mémoire héritée).
- Sources : [N073-C1] l. 9-13 ; [N073-C2] l. 31-49 ; [N073-C3] l. 56, l. 63-89 ; [VEIL] idée 7 l. 57.
- État : PROPOSÉ (matière première de l'atelier ; « ne peut pas encore fonder un préenregistrement », [N073-C2] l. 49).
- Sort : décrit « sans être dit nouveau ni propre » ; neuf citations obligatoires ; « un registre des tentatives […] non une archive de découvertes » ([N073-C3] l. 56).

**M5. Masquage d'une partie de l'archive.** [SDIV] l. 27-28 (rejet convergent) ; [SBE] l. 289 (« non discuté ») ; [DEC] l. 2487, R-2528 (rouvert par décision du directeur). PROPOSÉ puis rouvert. Non tranché.

**M6. Épreuve de prédiction par la lignée, sans fuite.** [VEIL] idée 5 l. 55. PROPOSÉ. Non fait.

**M7. Fil continu (le proposeur garde sa séance d'une génération à l'autre).** [VOIS] b3 l. 326. PROPOSÉ. Non tranché (cher).

---

## 14. Famille N — Voie sociale et composition des proposeurs

**N1. Pluralité des familles de proposeurs ; homogénéité entre modèles** (Ferreira, Liu et Zheng ; « Artificial Hivemind » ; Goel et al. ; Wenger et Kenett).
- Sources : [N073] § 5 l. 120-134 ; [SV9] l. 50, retenue 4 l. 69 ; [R28H] l. 131 ; [R28M] l. 25 ; [R28O] R2.
- État : PROPOSÉ ; indice contraire cité obligatoirement (N-073 § 5).
- Sort : « voisin » ; témoins à l'étape 2 (B9).

**N2. Isolement des appels contre communication** (sans débat ni vote ; « The interaction tax » : la communication efface la diversité ; communication par candidats chez SDF).
- Sources : [SV9] l. 54 ; [VOIS] l. 386, table l. 237.
- État : ÉPROUVÉ AILLEURS (SDF : la communication « n'empêche pas le plateau ») ; PROPOSÉ chez nous.
- Sort : non tranché (rejoint H2).

**N3. Canal social** : voir G8 (une seule entrée).

---

## 15. Tableau récapitulatif

| N° | Nom | Famille | État | Retenu / écarté |
|---|---|---|---|---|
| A1 | Borne amont « pas de moteur à pousser » | A | proposé | retenu (cadre) |
| A2 | Pas de vue uniformément meilleure, aiguille | A | proposé | retenu (cadre) |
| A3 | Barrière de parité | A | proposé | retenu |
| A4 | Chaînes et horizon | A | proposé | retenu |
| A5 | Seuil de détectabilité n·r·Δ | A | proposé | retenu |
| A6 | Auto-localisation | A | proposé | retenu |
| A7 | Fermeture du nul, copies par morceaux | A | proposé | retenu |
| A8 | Deux étroitesses | A | proposé | retenu |
| A9 | Largeur estimée, non réglée | A | proposé | retenu |
| A10 | Danger : poussée vers la classe non couverte | A | proposé | retenu |
| A11 | Taux de base de la queue | A | proposé | retenu |
| A12 | Budget borné impossible, garantie disjonctive | A | proposé | non tranché |
| A13 | L'adaptativité consomme la validité | A | proposé | retenu |
| A14 | Identité des idées | A | proposé | retenu |
| A15 | Forcer la proposition, pas la découverte | A | proposé | non tranché |
| B1 | Tirages indépendants, meilleur de N | B | décidé ; éprouvé ailleurs | retenu |
| B2 | Hasard au gabarit | B | conçu (à blanc) | retenu, jamais joué en réel |
| B3 | Chercheur mécanique, énumérateur | B | éprouvé en partie (cité) | retenu |
| B4 | Énumération exhaustive | B | proposé | non tranché |
| B5 | Contrôles placebo | B | proposé (un servi en K1) | retenu |
| B6 | Reprise du meilleur à contexte neuf | B | éprouvé ailleurs ; décidé | retenu |
| B7 | Pseudo-familles | B | proposé | retenu (synthèse) |
| B8 | Popularité seule, rétrodiction inversée | B | décidé | retenu |
| B9 | Témoins de composition | B | décidé | retenu |
| C1 | Hors des bassins déjà promus | C | conçu (simulation) | décidé, non mesuré |
| C2 | Catalogue de stratégies déclarées | C | éprouvé en partie (scripté) | non tranché ; avantage non montré |
| C3 | Liste des paires non croisées | C | proposé | retenu (rang 2), non tranché |
| C4 | Décomposition de Möbius | C | proposé | écarté |
| C5 | Code couvrant | C | proposé | écarté |
| C6 | Homologie de l'archive | C | proposé | écarté |
| C7 | Plan combinatoire, focalisations | C | proposé (borne 11 calculée) | retenu (rang 3) |
| C8 | Moments orthogonaux | C | proposé | maintenu |
| C9 | Tirage déterminantal, répulsion | C | éprouvé (recombinaison) | noyau écarté ; vues maintenu |
| C10 | Vues équivalentes | C | proposé | suspendu |
| C11 | Processus gaussien | C | proposé | écarté |
| C12 | Résidus, canal d'épisodes publics | C | conçu | non tranché (nœud) |
| C13 | Portefeuille de missions | C | proposé ; éprouvé ailleurs (nul) | différé |
| C14 | Exclure le banal | C | proposé | non tranché |
| C15 | Stratification, histogramme plat, métadynamique | C | proposé | non tranché |
| C16 | Qualité-diversité, nouveauté seule | C | proposé | non tranché |
| C17 | Données propres au programme | C | proposé | non tranché |
| C18 | Faire varier la question | C | proposé | non tranché |
| C19 | Abstraction et transfert | C | proposé | non tranché |
| D1 | Contrastes compilables | D | proposé | retenu (rang 4) |
| D2 | Opérateur d'expansion | D | proposé | écarté |
| D3 | Carte de déviation en log-cotes | D | proposé | non tranché |
| E1 | Température, contre-vraisemblance | E | proposé | écarté comme forçage |
| E2 | Modèles de base | E | proposé | retenu (synthèse) |
| E3 | Mélange défensif, recherche de Levin | E | proposé | non tranché |
| E4 | Entropie croisée | E | proposé | écarté |
| E5 | Recuit, tempering, îles | E | proposé | écarté (hors ligne seul) |
| E6 | Stein, transport optimal | E | proposé | écarté |
| F1 | Marchepieds | F | conçu | non tranché |
| F2 | Fractionnement multiniveau | F | proposé | retenu (rang 5) |
| F3 | Arbres de continuation | F | proposé | non tranché |
| F4 | Synthèse typée | F | proposé | suspendu |
| F5 | Curriculum | F | proposé | non tranché |
| F6 | Une carte par session | F | proposé | non tranché |
| F7 | Proposeurs en série | F | conçu | non tranché |
| F8 | Deux passes | F | conçu | non tranché |
| F9 | Demi-générations | F | conçu | non tranché |
| F10 | Archive complète | F | proposé | non tranché |
| G1 | Loin en domaine, proche en concept | G | conçu | occupé en partie (forme) |
| G2 | Trou à structure commune | G | conçu | retenu (à tester) |
| G3 | Jamais reliés, Gu-Krenn | G | conçu | substitut accordé |
| G4 | Fusion qui prédit plus que ses parents | G | proposé | critère à valider contre tricheurs |
| G5 | Tirage stratifié par domaines | G | éprouvé | retenu par défaut |
| G6 | Combinaison atypique | G | proposé | non tranché |
| G7 | Fertilité d'une paire | G | proposé | non tranché |
| G8 | Canal social | G | décidé ; éprouvé ailleurs | retenu comme base |
| G9 | Base de ponts datés et garde-fous | G | décidé | retenu |
| H1 | Transition de phase | H | proposé | nœud sans issue trouvée |
| H2 | Essaims communicants | H | proposé | non tranché |
| H3 | Ensemble autocatalytique | H | proposé | lu, non repris |
| H4 | Un parent contre deux parents | H | proposé | jamais monté |
| H5 | Seuil de Bettencourt | H | proposé | référence non trouvée |
| H6 | Idées dans l'air | H | proposé | non mesuré |
| H7 | Causes de la fertilité | H | proposé | lu, non repris |
| I1 | Aucune récompense de nouveauté | I | décidé | retenu |
| I2 | Moissonneur | I | conçu | non joué |
| I3 | Originalité en note de grille | I | conçu | matériau |
| I4 | Nouveauté à l'oracle ΔG | I | conçu | non joué |
| I5 | Témoins redites et dérivables | I | décidé | retenu, non fait |
| I6 | Redite exacte de la loi | I | éprouvé | constat |
| I7 | Distance à un corpus | I | proposé | description seule |
| I8 | Surprise, curiosité | I | proposé | écarté |
| I9 | Antériorité par un tiers | I | proposé | en partie accordé |
| J1 | Masse manquante | J | proposé | retenu (diagnostic) |
| J2 | Rareté certifiée sur panel | J | proposé | retenu (synthèse) |
| J3 | Banc à puits plantés, dose-réponse | J | proposé | non tranché |
| J4 | Audit des pertes | J | proposé | recommandé, non tranché |
| J5 | Loi spontanée des proposeurs | J | proposé | non fait |
| J6 | Réactivité à la vue | J | proposé | retenu, non fait |
| J7 | Signature d'exécution | J | proposé | retenu |
| J8 | Diversité par couverture d'oracle | J | conçu | retenu |
| J9 | Trois lectures | J | proposé | retenu |
| J10 | Collisions, autocorrélation | J | proposé | non tranché |
| J11 | Grandeurs et deux références | J | proposé | non tranché |
| J12 | Seuil de rentabilité | J | proposé | non tranché |
| J13 | Contrôle dans la queue | J | proposé | retenu (ordre) |
| J14 | Validité externe | J | proposé | non tranché |
| J15 | Monde riche, leurres | J | décidé ; conçu | retenu |
| J16 | Redondance des courses réelles | J | éprouvé | constat |
| K1 | Arrêt optionnel, tirages répartis | K | éprouvé | gain de structure ; adoption en attente |
| K2 | Bandits, recherche arborescente | K | proposé | hors ligne seul |
| K3 | Uniforme avec arrêt précoce | K | proposé | défaut (boucle moisson) |
| K4 | Portefeuille sous-modulaire, meilleur couple | K | proposé | suspendu / non critiqué |
| K5 | Composition sur oracle et coût | K | décidé | retenu |
| K6 | Bon marché d'abord, chers sur regroupement | K | conçu | non joué |
| K7 | Arrêter une course stérile | K | proposé | écarté |
| K8 | Indice de Weitzman | K | proposé | non tranché |
| K9 | Contrôle en ligne entre générations | K | proposé | manque reconnu |
| K10 | Loi mère, champ moyen | K | proposé | non codé |
| K11 | Règles d'arrêt à garantie | K | proposé | non tranché |
| K12 | Filtrage avant contrôle | K | proposé | dédoublonnage retenu |
| L1 | Juge au nul des lois connues | L | décidé | retenu |
| L2 | Valeur e par strates | L | proposé | contredit |
| L3 | Poids selon la nouveauté | L | proposé | écarté |
| L4 | Pari localisé, nul ponctuel | L | proposé | non critiqué |
| L5 | Supremum sur nul composite | L | proposé | maintenu |
| L6 | Filtre avant le juge | L | proposé | non critiqué |
| L7 | Tirages du juge stratifiés | L | proposé | écarté, désaccord ouvert |
| L8 | Nul par morceaux limité, poids appris | L | éprouvé en partie | non tranché |
| L9 | Valeurs e pondérées par longueur | L | proposé | non tranché |
| L10 | Regroupement et représentant | L | conçu | retenu (temps 1) |
| L11 | Sélection douce | L | proposé | non tranché |
| L12 | Pari apparié borné | L | décidé | retenu |
| L13 | Second contrôle | L | proposé | retenu avec réserve |
| L14 | Aucun juge-modèle de nouveauté | L | décidé ; éprouvé | retenu |
| L15 | Double nul | L | proposé | non tranché |
| M1 | Héritage récompensé | M | décidé (occupé) | revendication retirée |
| M2 | Oublier, hériter moins | M | éprouvé ailleurs ; décidé | retenu |
| M3 | Remise à zéro déjà en place | M | constat | retenu |
| M4 | Registre des tentatives, trois bras | M | proposé | non revendiqué |
| M5 | Masquage de l'archive | M | proposé | rouvert, non tranché |
| M6 | Prédiction par la lignée | M | proposé | non fait |
| M7 | Fil continu | M | proposé | non tranché |
| N1 | Pluralité des familles | N | proposé | voisin, indice contraire |
| N2 | Isolement contre communication | N | éprouvé ailleurs | non tranché |

**Comptes par famille** (139 entrées ; N3 renvoie à G8 et n'est pas comptée) : A 15 ; B 9 ; C 19 ; D 3 ; E 6 ; F 10 ; G 9 ; H 7 ; I 9 ; J 16 ; K 12 ; L 15 ; M 7 ; N 2.

**Comptes par état principal** (un état par entrée, ordre de préséance : éprouvé chez nous, éprouvé ailleurs, décidé, conçu, proposé) :
- éprouvé chez nous, en tout ou en partie : 10 (B3, C2, C7 pour sa borne 11, C9, G5, I6, J16, K1, L8, L14) ;
- éprouvé ailleurs seulement : 6 (B1, B6, C13, G8, M2, N2) ;
- décidé : 10 (B8, B9, G9, I1, I5, J15, K5, L1, L12, M1) ;
- conçu : 16 (B2, C1, C12, F1, F7, F8, F9, G1, G2, G3, I2, I3, I4, J8, K6, L10) ;
- proposé seulement : 96 ; constat de dessin : 1 (M3).

| Famille | éprouvé | ailleurs | décidé | conçu | proposé | constat |
|---|---|---|---|---|---|---|
| A bornes | 0 | 0 | 0 | 0 | 15 | 0 |
| B bases | 1 | 2 | 2 | 1 | 3 | 0 |
| C choix de l'exploré | 3 | 1 | 0 | 2 | 13 | 0 |
| D représentation | 0 | 0 | 0 | 0 | 3 | 0 |
| E échantillonnage | 0 | 0 | 0 | 0 | 6 | 0 |
| F plusieurs pas | 0 | 0 | 0 | 4 | 6 | 0 |
| G recombinaison | 1 | 1 | 1 | 3 | 3 | 0 |
| H allumage | 0 | 0 | 0 | 0 | 7 | 0 |
| I nouveauté | 1 | 0 | 2 | 3 | 3 | 0 |
| J mesure | 1 | 0 | 1 | 1 | 13 | 0 |
| K arrêt, allocation | 1 | 0 | 1 | 1 | 9 | 0 |
| L jugement | 2 | 0 | 2 | 1 | 10 | 0 |
| M mémoire | 0 | 1 | 1 | 0 | 4 | 1 |
| N social, composition | 0 | 1 | 0 | 0 | 1 | 0 |

Ces comptes sont des comptes de lecture, à revérifier entrée par entrée.

---

## 16. Jamais éprouvé chez nous (sélection des entrées qui portent une prédiction testable)

- Le banc à puits plantés et la courbe dose-réponse, puits sans parent compris (J3) ; le critère de réfutation par famille de mondes.
- L'audit des pertes sur journaux bruts (J4) ; la loi spontanée des proposeurs et leur recouvrement (J5) ; la réactivité de la vue, liste contre placebo (J6, C3).
- La masse manquante comme règle d'arrêt, validée contre l'oracle (J1) ; la rareté certifiée sur panel (J2) ; l'audit du contrôle dans la queue (J13).
- Le hasard au gabarit et le chercheur mécanique contre de vrais proposeurs (B2, B3) ; le duel payé des proposeurs (L12).
- La stratégie « hors des bassins déjà promus » avec un vrai modèle (C1, C2).
- Les marchepieds sur une lignée réelle (F1) ; le fractionnement sur prérequis (F2) ; les cribles (ii), (iii), (iv), (v) (F7, F8, F9, K6) ; une carte par session (F6).
- Le bisociateur en course réelle, ses trois bras et le canal social (G1, G2, G8) ; la reproduction de Gu-Krenn (G3) ; le banc des tricheurs pour la fusion (G4, résultat non trouvé).
- L'exclusion du banal par invite contre le rejet exact (C14) ; la température sous décodage contraint (E1) ; les modèles de base (E2) ; le mélange défensif (E3).
- La transition de phase, les essaims, l'autocatalyse, « un parent contre deux parents » (H1 à H4).
- Le moissonneur en réel (I2) ; les témoins « vrais mais dérivables » (I5).
- Les tirages du juge stratifiés, sur le banc de l'idée 1.2 (L7) ; le nul ponctuel et le filtre avant le juge (L4, L6).
- Le plan à trois bras de la mémoire, le bras d'oubli chez nous (M2, M4) ; la validité externe par rétrodiction datée (J14).
- L'organisme sur les bassins étroits lui-même : génération 1 en défaut, générations 2 et 3 jamais lancées (§ 0).

---

## 17. Désaccords entre sources

1. **Qualité-diversité servie ou non aux proposeurs** : Fable maximal, « structurer l'archive servie, non récompenser » ([R28M] l. 81) ; Opus, seulement dans l'orchestrateur, « jamais comme texte servi aux proposeurs » ([R28O] R2, en tête du tableau).
2. **La rareté comme signal d'allocation** : Opus propose (b) « signal d'allocation dans l'orchestrateur » après le banc ([R28O] D-1 l. 278-284) ; le rejet convergent du 12 novembre exclut toute récompense numérique de la nouveauté, y compris dans la sélection ([SDIV] l. 25-27 ; G2 « à moitié » refermé, [SBE] l. 285).
3. **Valeur e par strates** : Argon (tour et à part) annonce la fin de la dilution ; D-T2 et E-T2 le réfutent ; C-T3 concède ; la consultation à part maintient ([SBE] l. 80-82).
4. **Poids de multiplicité** : abandonnés par leur auteur au tour ; défendus par Argon à part et la mère ([SBE] l. 83, l. 284).
5. **Tirages du juge stratifiés** : la fiche de l'organisme dit la garantie intacte ; le recoupement dit que la grandeur jugée change ([RELEVE] l. 152-155 ; [REC] l. 238-241).
6. **Conditions de l'arrêt optionnel** : la synthèse exige un dénominateur fixe et un ordre fixé d'avance ([REC] l. 232-234 ; [SBE] l. 298-300) ; la contre-lecture de l'idée 1.2 les juge non nécessaires (R-2878, [DEC] l. 2838).
7. **Origine de l'idée 1.2** : l'inventaire la rattache au tour des bassins étroits ([INV] l. 63) ; R-2851 la tire du relevé « conception propre » ([DEC] l. 2811). Compatible (le relevé reprend J1), mais deux origines sont dites ([PAGE] l. 89).
8. **Regrouper avant ou après le juge** : A après, C, D, E avant ([SDIV] l. 65-67).
9. **Métrique principale** : propositions brutes ou cartes retenues ([SBE] l. 73-74).
10. **Hausse des conditionnelles sous monde nul** : alerte de garde pour B-T2, simple description pour D-T3 et E-T3 ([SBE] l. 75-77).
11. **Monde à condition verrouillée (interaction sans parent)** : contrôle nul pour A-T2, refusé par D-T3 et E-T3 ([SBE] l. 78-79) ; Fable maximal « tranche » pour le contrôle négatif ([R28M] l. 144) ; Opus en fait un détecteur de fuite ([R28O] l. 41).
12. **Un facteur par bras ou bras combiné** : C-T1 et Argon à part combinent ; III.3 et Astra exigent un facteur ([SBE] l. 84-85).
13. **Bandit** : Argon (collisionneur boucle moisson) le refuse ; A et D le gardent en synthétique ([SMOIS] l. 151) ; Argon, réponse 40, recommande une allocation par bandits après un pilote corrélé ([R40A] l. 152) ; Fable 40 interdit le guidage par le juge en course ([R40] D3 l. 248).
14. **Marge sur les fausses découvertes** : marge positive (B, E, F) contre la lettre « sans augmenter » (D) ([SV9] l. 86).
15. **Identité d'une idée** : arbre syntaxique ajouté (C) ou retiré (F) ([SV9] l. 88).
16. **Le bisociateur sans bras au hasard**, alors que toutes les autres pièces exigent une base au hasard ([IO-BISOC] l. 3 ; [PAGE] l. 393).
17. **Héritage** : prémisse de N-045 (l'héritage aide) contre « oublier bat continuer » ([VOIS] l. 371-375 ; [DEC] l. 2487).
18. **Masquage de l'archive** : rejet convergent ([SDIV] l. 27-28) contre bras « oubli » et « héritage réduit » accordés ([DEC] l. 2487).
19. **Relances de l'organisme sur les bassins étroits** : une par génération selon le lanceur v3 ; une seule au total selon Lazar ([DEC] l. 2515 et l. 2517).
20. **Transition de phase** : retrait (A), maintien à partir de cinq tailles (B), suspension (recommandation) ([SBIS] l. 216-224).
21. **Classement de la mère** : D1 et D2 au rang 2 chez elle ([MERE] l. 106-107), « contredit » par le tour ([SBE] l. 195-200).
22. **Où commencer** : instruments seuls (A, C, F), contrôle dans la queue (B), chaîne avec erreurs injectées (D) ([SV9] l. 87) ; audit des pertes d'abord (Fable, Opus, [R28M] D1, [R28O] D-2) ; banc de garde d'abord (collisionneur du 13 novembre, [SBE] l. 318-326).

---

## 18. Non trouvé dans ce que j'ai lu

- Une relance de l'organisme sur les bassins étroits, un lanceur v4, les générations 2 et 3.
- Une décision de Lazar sur la recommandation de la synthèse des bassins étroits (R-2541 : « non tranchée »).
- Les décisions sur D1 à D4 (Fable maximal, demande 28), D1 à D5 (Fable très haut), D-1 à D-6 (Opus), D1 à D4 (réponse 40).
- La réponse de Neon à la demande 40 : au commit `3ab317c4`, seul un journal à l'état « reserve » existe (`reponse-40-google/journal-40-neon.jsonl`, 14:00:22Z) ; aucun tour du collisionneur ni aucune course de l'organisme sur la question neutre de la réponse 40 (GO-2026-11-22-67) ; aucune course de l'organisme sur la question neutre de la demande 28 (GO-2026-11-22-47 : « sur devis à part »).
- Le résultat du banc des tricheurs de la recombinaison (`banc-tricheurs-v1.md`, cité par [INV] l. 47, non localisé ici).
- L'issue du nœud « transition de phase », des défauts D7-1 à D7-4, de la course 2 à trois bras de bisociation (GO-2026-10-31-04), de la lecture des PDF de Bettencourt.
- Le verdict du jeu de l'idée 1.1 (poids du nul, version 2) ; une décision d'adoption de l'allocation de l'idée 1.2 au juge.
- Un lancement des cribles (iii) et (v) après R-3005.
- Une séance sur Good et Toulmin 1956 avant le mandat ; la réponse au mandat du 22 novembre.
- Tout fichier de résultat pour la batterie des proposeurs, les marchepieds, le duel des proposeurs et une moisson réelle (dépôt `ideation-organism`).

---

## 19. Chemins non ouverts pour cloisonnement (ou par prudence)

- `docs/notes/bisociation-litterature-reelle-v1/pra2-1298-transcription-v1.md` (motif « transcription ») ; seule l'antériorité a été lue.
- Les pièces de la « matière première » de l'auto-conception (moisson des 630 travaux sur l'exploration d'idées, R-3211, [DEC] l. 3343) : aucun chemin à motif « matiere-premiere » ouvert.
- Sous `prereg/` : les préenregistrements de l'idée 1.2 (`organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`), du crible (v) (`organisme-crible-v-regles-proposeurs-v1.md`) et des cribles ; sous `runs/` : la course de la génération 1 des bassins étroits et les fiches de la course « conception propre ».
- Les pièces versées en quarantaine (R-835, [DEC] l. 1063).
- « Inventaire de l'allumage » de la course des nouvelles attaques (R-4370) : homonyme, motif « nouvelles attaques », non ouvert.
- Dans `ideation-organism` : `orchestrator/essais/mutations_v57b.py`, `test_v57b_cablage_verdict.py` (motif « 7b »), `test_v7_monde_banque_scores.py`, `pole/monde_banque_scores.py` (motif « score »), `resultats/controle-p3-premier-test/`, `resultats/controle-r1-blanche-noire/`, `resultats/controle-simulation-defenses/`, et les lignes 137 à 139 du `README.md`.
- Dans le bloc-notes de la session : les dossiers `epreuve-lots-ne-pas-lire/` et `epreuve-2-lots-ne-pas-lire/`.
- Non ouverts par économie, non interdits : le verdict de l'idée 1.2 (`docs/notes/organisme-idees-juge-v1/verdict-idee-1-2-v1/`, cité par R-3008), l'inventaire des 31 méthodes (`docs/notes/collisionneur-bassins-etroits-v1/inventaire-methodes-v1.md`, couvert par le recoupement), les cellules et consultations à part brutes, les témoins JSON des bassins étroits, l'archive de la page de Bespoke Labs, la synthèse de la question 6 en détail, le verdict du pilote MR-2.

---

## 20. Table des sources (16 premiers signes du SHA-256)

| Alias | Chemin (dépôt, commit) | SHA-256 (16) |
|---|---|---|
| [PAGE] | controle-ia-travail `022c530e` : `docs/notes/memoire-conception-v1/exploration-idees-seances-anterieures-v2.md` | 805e91e334b76f5d |
| [DEC] | idem : `registres/decisions.md` | 57ab7031ae491b8a |
| [GO] | idem : `registres/go.md` (l. 734, l. 754) | 15e7ece115269e70 |
| [CLAUDE] | idem : `CLAUDE.md` | 282542c96e0533c9 |
| [OPG1] | idem : `docs/notes/organisme-bassins-etroits-v1/operation-g1-v1.md` | 3beef39eadae4693 |
| [PREP3] | idem : `…/organisme-bassins-etroits-v1/rapport-preparateur-v3.md` | 348a5208d830bbfa |
| [CONC3G] | idem : `…/organisme-bassins-etroits-v1/conception-trois-generations-v2.md` | b6c7035ee8a6d72c |
| [QBE] | idem : `…/organisme-bassins-etroits-v1/question-organisme-bassins-etroits-v1.md` | c188fa9a8ada9c87 |
| [REC] | idem : `…/organisme-bassins-etroits-v1/recoupement-methodes-v1.md` | eecd98fab0beff8c |
| [DEV3] | idem : `…/organisme-bassins-etroits-v1/devis-organisme-bassins-etroits-v3.md` | 7c340c445a99cfed |
| [MERE] | idem : `docs/notes/bassins-etroits-idees-v1/remue-meninges-mere-v1.md` | f3c46703f19d4407 |
| [SBE] | idem : `docs/notes/collisionneur-bassins-etroits-v1/synthese-v1.md` | 5fd7e26fc8c04ddd |
| [SDIV] | idem : `docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md` | 4f99077b70027823 |
| [VOIS] | idem : `docs/notes/lecture-voisins-bassins-idees-v1.md` | 80abfae70a68a958 |
| [VEIL] | idem : `docs/notes/veille-exploration-idees-v1/synthese-v1.md` | dc35b778c257e923 |
| [N073] | idem : `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` | b95688df5e695da7 |
| [N073-C1] | idem : `docs/decisions/decision-N-073-complement-1-memoire-transmise-v1.md` | 61903909e8aaaa70 |
| [N073-C2] | idem : `docs/decisions/decision-N-073-complement-2-memoire-transmise-v1.md` | 5707dbd8bdd8ccc2 |
| [N073-C3] | idem : `docs/decisions/decision-N-073-complement-3-memoire-transmise-v1.md` | 4ca0ce7b040b917d |
| [RECOMB] | idem : `docs/notes/pole-scientifique-automatique/synthese-recombinaison-v1.md` | 47490973ce85c18b |
| [INV] | idem : `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` | b49dc2462382206d |
| [ORIG] | idem : `docs/notes/organisme-idees-juge-v1/conception-idees-originales-v1.md` | 2f6a69dd480a079f |
| [RELEVE] | idem : `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` | bd253b6c68f6baad |
| [D28] | idem : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-28-idees-originales-puits-profonds-v1.md` | f552f514961f78be |
| [R28H] | idem : `…/reponse-28/relecture-fable-api.md` (Fable 5.2, effort très haut) | 05c72e054ed7b5af |
| [R28M] | idem : `…/reponse-28-effort-max/relecture-fable-api.md` (Fable 5.2, effort maximal) | 1261c8eeb9f00711 |
| [R28O] | idem : `…/reponse-28-opus55-max/reponse-opus55-v1.md` (Opus 5.5) | 04aa3de4a2afddc2 |
| [QN28] | idem : `…/question-neutre-idees-originales-v1.md` et `…-servie-v1.md` (identiques) ; `…-forme-2-servie-v1.md` | 3d2d70d5633a3101 ; 3b555174beef13f0 |
| [SV9] | idem : `docs/notes/collisionneur-v9/syntheses-protocole-x-v1/note-synthese-idees-originales-v1.md` | 10448cd446cf6934 |
| [D40] | `3ab317c4` : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-40-methodes-mathematiques-puits-etroits-v1.md` | 8fcdb2f4f62764cf |
| [R40] | `3ab317c4` : `…/reponse-40/relecture-fable-api.md` (Fable 5.2, maximal ; égal à la copie du bloc-notes) | 7e6e539c2cbc03f0 |
| [R40A] | `3ab317c4` : `…/reponse-40-google/reponse-40-argon-v1.md` | bf0c03916041f8b5 |
| [R40C] | `3ab317c4` : `…/reponse-40-google/reponse-40-carbon-v2.md` | 10cf708f9148733d |
| [TIII] | `022c530e` : `docs/notes/ideation-organisme-v1/course-2/texte-III-v1/synthese-texte-III-v2.md` | a3844e4ffa52f0de |
| [QFUS] | idem : `docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/question-fusionnee-argon-collisionneur-v1.md` | aab8ced8605ead09 |
| [SBIS] | idem : `…/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md` | 23c2888ddd924b85 |
| [SQ7] | idem : `…/collisionneur-question-7-v1/synthese-question-7-v2.md` | 0ced3b28fa5cf1c2 |
| [PRA2] | idem : `docs/notes/bisociation-litterature-reelle-v1/anteriorite-pra2-1298-v1.md` | e47d7942f356ea34 |
| [PROTO1] | idem : `docs/notes/protocelles-collisionneur-v1/synthese-protocelles-tour1-v2.md` | 7117a8d93498eb28 |
| [PROTO2] | idem : `docs/notes/protocelles-collisionneur-v1/synthese-protocelles-tour2-v1.md` | b000cc5e1841f3e1 |
| [SMOIS] | idem : `docs/notes/ideation-organisme-v1/course-2/collisionneur-boucle-moisson-v1/synthese-boucle-moisson-v2.md` | efec05a9e4acfd39 |
| [SMATH] | idem : `docs/notes/mathematiques-nouvelles-v1/brainstorm-methodes-v1/synthese-reponses-externes-v1.md` | fb5e83972b01eb5a |
| [MANDAT] | idem : `docs/notes/exploration-idees-fable-v1/mandat-demande-approfondie-exploration-et-allumage-v1.md` | 6909f66e1587eb14 |
| [IO-INV] | idem : `docs/sources/ideation-organism-a41b7b50-v1/inventaire-ideation-organism-a41b7b50-v1.md` | 826d03ec8903d94b |
| [IO-README] | ideation-organism `a41b7b50` (copie) : `README.md` | 04ac692e9500dd37 |
| [IO-CONC7] | idem : `orchestrator/conception-v7-v1.md` | 31fc8c4bc286341f |
| [IO-PROP] | idem : `orchestrator/pole/proposeur.py` | a77018584ec5d20c |
| [IO-REF] | idem : `orchestrator/pole/proposeurs_references.py` | 6ed7e56fb1a1f744 |
| [IO-SIM] | idem : `orchestrator/pole/simulation.py` | be14d44e7a8ebf6b |
| [IO-RECOMB] | idem : `orchestrator/pole/recombinaison.py` | 71faad38644c77ae |
| [IO-BISOC] | idem : `orchestrator/pole/bisociateur_v53.py` | 962eb8ce22d5af1b |
| [IO-MOIS] | idem : `orchestrator/pole/moisson.py` | 35d9a996aaacf6d6 |
| [IO-IDEA] | idem : `orchestrator/pole/ideation.py` | 4ee70d25567a9b3a |
| [IO-DCYCLE] | idem : `orchestrator/demonstrations/demo_cycle_v5.py` | a457a8e284e58fc1 |
| [IO-DC1] | idem : `orchestrator/demonstrations/demo_couche1_proposeur_v7.py` | 0a782a5b1fab4cac |
| [IO-DPROP] | idem : `orchestrator/demonstrations/demo_proposeurs_v7.py` | 6ca98c3f050d54d8 |
| [IO-DUEL] | idem : `orchestrator/demonstrations/duel_proposeurs_v7.py` | d8f31817da702064 |
| [IO-TEST] | idem : `orchestrator/essais/test_v7_proposeur.py` | bad4adc4c5b16e63 |
| [IO-TF6] | idem : `orchestrator/prereg/preenregistrement-tour-ferme-v1-brouillon6.md` | cdcb44706e7b3c62 |
| [IO-RTF6] | idem : `orchestrator/prereg/rapport-redaction-tour-ferme-v6.md` | c2d6765a5993f66f |
| [IO-BR] | idem : `orchestrator/prereg/preenregistrement-boucle-reelle-organisme-v1-v2.md` | 80fe4f03b4905b23 |
| [IO-JUG] | idem : `orchestrator/prereg/preenregistrement-juges-idees-v2-brouillon3.md` | 2680cf6a5c7f080d |
| [IO-V67] | idem : `resultats/course-v67/verdict-course-v67-v1.md` | d79024328157aafc |
| [IO-GH] | idem : `resultats/attaque-goodhart-v2/README.md` | 88c97bad8495d0c3 |
| [IO-V66] | idem : `resultats/boucle-reelle-v66/README.md` | 70a7db26b80e897c |

Note : les lignes du registre citées (R-…) le sont au numéro de ligne de `registres/decisions.md` au commit `022c530e` ; les lignes des fichiers de `ideation-organism` sont celles de la source `a41b7b50`, égales à celles de la copie versée.
