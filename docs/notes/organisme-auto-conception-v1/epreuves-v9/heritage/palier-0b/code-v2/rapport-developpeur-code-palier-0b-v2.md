# Rapport du développeur — code de l'étage sur processeur du palier 0b de l'héritage, reprise — v2

- Auteur : développeur, modèle L′. Pièce de travail (classe C). Travail du 2026-11-20, de 00:35Z à 02:50Z environ (`date -u`).
- Mandat : `heritage/palier-0b/mandat-developpeur-code-palier-0b-v2.md` (`024e94e5c48c1536ea2b4fec070b891963882ea1ec3644c58a06edd54d271739`), empreinte vérifiée sur disque avant tout geste ; lancement permis, selon la session mère, par `GO-2026-11-20-01` et la lecture R-4024 (lignes non relues par moi).
- Texte qui fait foi : préenregistrement v6 (`4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029`), vérifié ; contrôle du différentiel v6 lu. Lus en entier : le préenregistrement v6, le mandat, le LISEZ-MOI et les quinze modules du dossier versé, le rapport du rédacteur v4 (§ 6), le rapport du palier 0a, son manifeste, la sortie du calcul v2 ; lus en partie : le plan v5 (§ 1 à § 7 ; `9085bbe9…` vérifié), le devis v5 (§ 1, § 2 ; `30c87fa6…` vérifié), le code de l'organisme (passages de `tour_ferme_v64`, `tests_de_mort_v2`, `evaluateur_lois_v62`, `selection_pari`, `proposeurs_references_v59`, `a_blanc_v59`).
- Code de l'organisme : copie du dépôt (commit `94bfd92`) recopiée dans le bloc-notes ; les seize fichiers employés au palier 0a ont l'empreinte de son manifeste (outil `scripts/verifier_environnement_agent_v1.py --empreintes`, sortie `outils-dev/verification-empreintes-organisme-v1.json`, aucun écart). Le code de l'organisme n'a pas été modifié.
- Environnement : Python 3.13.18, numpy 2.5.3, pytest 9.1.1 (outil fourni, aucune anomalie).

## 0. Verdict

Le code de l'annexe C est écrit, conforme à la version 6 sauf les écarts du § 5, sous `src/controle_ia/heritage_etage_processeur_v1/` (23 modules) et `tests/` (huit fichiers d'essais et une aide), dans le bloc-notes. **Suite entière : 70 essais passés, 0 échoué** (720 s). Chaque garde de B9 a son essai, cas sain et artefact (§ 2). Défauts réintroduits un par un : 41 vus sur 41 au passage sur le code final (§ 3). **Deux constats demandent un mot avant le scellement** (§ 5.1, § 5.2) : la marge face à la source étrangère (B7 bis) épuise ses bornes à la dose 0,5 sur les graines d'essai ; et l'audit de présentation lit, **sur les traits de forme**, une différence entre lois dépendantes et indépendantes (exactitude 0,565 à taille réduite), qui ferait arrêter l'étape 3 si elle se retrouve à pleine taille. **Aucun refus d'outil.**

## 1. Ce qui est fait

### Modules (annexe C)

| module | objet |
|---|---|
| `constantes` | valeurs gelées de la v6, huit clés de fréquences |
| `graines` | racine `SeedSequence(2026111902)`, étiquettes en clair, couches disjointes ; « decisif » et « confirmation » refusées sans `Autorisation` (texte scellé et erratum, vérifiés par empreinte) ; journal du processus ; garde 20 |
| `lois` | grammaire de l'organisme (recopie de `evaluateur_lois_v62.proba`), forme unique, composition |
| `audit` | **écriture à part** de l'évaluateur et de la divergence, marges à 0,25 nat (dont B1 (e) et B7 bis), audit de présentation : traits de forme et de contenu, trois audits dont les doses par paires, quinze exactitudes ; forme → arrêt, contenu ou réunis → signalement « générateur non audité pour l'étage payant » |
| `mondes` | générateur constructif de B1 (marge de construction 0,30 nat, bornes 400 / 200 / 200, arrêt nommé « bornes de la construction épuisées »), comptes de tirages tentés et acceptés par sorte, rejets par niveau, tours ; B7 bis (`generer_jeu_avec_etrangeres`) ; fichiers des mondes ; garde 10 ; ensemble exclu ; étape 3 (`audit_du_generateur`) |
| `comparateur` | B3, sans juge ; table du palier 0a |
| `registre` | registre en ajout seul, chaîné, scellé ; trois vues ; projection vers la fiche **sans balise** ; gardes 2 à 9, 11, 27 |
| `executeur` | forme imposée recopiée à l'octet du tour fermé ; fonction d'écriture de l'invariant ; contre-calcul (garde 16) ; artefacts des gardes 17 et 24 |
| `enveloppe` | lots de douze au plus, un domaine par lot ; statut de budget ; seuil relu ; classement dans l'ordre du scellement ; échecs de l'expérimentateur |
| `cout` | coûts du devis, deux règles de retrait, garde 18, test de mort final hors budget |
| `proposeurs` | les neuf proposeurs de B7 ; course source sans composition ; tenue lue sur les entrées **de sa propre continuation** (même source, même bras) |
| `mecanique` | couche mécanique : course source, bras 1 à 4b, mesure finale (M1, D, I, lois fausses), M12 par loi et par monde ; garde 17 en ligne (`organisme`) ; jeu de diagnostic |
| `frequences` | les huit fréquences (strate vide = None), rapport par strate avec intervalle exact, S8 (i), strates requises, gel scellé |
| `statistique` | couche statistique aux huit fréquences ; une strate vide employée arrête ; source étrangère = suivante du même tirage |
| `equivalence` | S8 (ii) et la précondition de l'artefact de la garde 23 |
| `rangs_signes` | test exact de Pratt, Holm, lecture, règle de validité ; verrou d'étalonnage |
| `intervalles` | Clopper-Pearson, règle de confirmation, rééchantillonnage |
| `etalonnage` | dichotomie sur graines communes, jumelles, taille réduite, verrou et sortie fermée (garde 22), gel scellé, taille réalisée |
| `tirages` | tirages emboîtés par lots, lectures par tirage (codes, jamais un taux), sorties brutes scellées, manifeste (R9), essai de forme borné, refus des couches décisives avant toute simulation |
| `analyse` | relecture des sorties sous sceau, taux et intervalles, C1 à C6, n, m, M10, M11, S7, R (M7), S9, taille réalisée, table des critères **sans issue** |
| `etapes` | plan des cases de B8 (72 cases pour C1 et pour C4), étapes 4, 6, 6 bis et 7, cases à confirmer |
| `organisme` | l'étage de l'organisme lui-même (`tour_ferme_v64.jouer_etage`, étage v5, exécuteur factice, doublures), tranche écrite avec les fonctions de l'organisme ; copie vérifiée par empreinte, sinon « garde non jouée » |

### Les points du dossier versé que le mandat nomme

- `registre.description_balisee` : retiré ; la projection porte la description sans balise ; une balise dans la fiche arrête (garde 11, essai et défaut réintroduit).
- Fréquences par origine : arrêt sur strate vide, jamais de repli ; branchées dans la couche statistique ; **huit** fréquences, dont la strate des lois vraies du monde source (essai : la changer ne touche pas le bras 1 et change le bras 3 du lecteur).
- Audit de présentation : traits de contenu, lecture par paires de doses, tirages par loi comptés.
- Marge face à la source étrangère : branchée dans `generer_cible` (et voir § 5.1).
- **Bras 4b, multiplicateur de la tenue sur les entrées étrangères : corrigé** (la condition lit la source et le bras de la provenance) ; essai dans la garde 27 ; défaut réintroduit, vu.
- Garde 21 : essai rejoué, au vert (vecteur planté `[0, 0, 1, 2, −3, 4, 5, 6, 7]` : 0,0625 selon Pratt, 0,078125 si les zéros sont retirés avant de classer).

### Défauts trouvés dans mon propre travail, corrigés

1. Le lecteur composait les entrées de sa propre course source (leur origine est « course-source ») : l'ensemble exclu n'était pas vide (deux lois) sur la première source jouée. Corrigé (aucune composition dans une course source) ; essai et défaut réintroduit.
2. L'analyse dépaquetait mal les clés des cases de C4. Corrigé.
3. La garde 20 lisait des étiquettes recalculées à part : elle lit désormais les étiquettes réellement employées (défaut réintroduit « même graine dans tous les bras », vu).
4. Essais mal écrits, corrigés : garde 7 (valeur glissée dans le résultat et non dans le retour), garde 13 (artefact dépendant du hasard : une loi de la source recopiée que la course source n'avait pas engagée ; l'artefact recopie désormais les lois vraies de la source dans les domaines indépendants du monde final), garde 25 (une loi « proche » qui était identique, une softmax étant invariante par un même déplacement de toutes ses lignes), garde 17 sur une source (décompte), garde 27 (motif d'arrêt précis).

## 2. Essais : une garde de B9, un essai, cas sain et artefact

| garde | essai(s) | fichier |
|---|---|---|
| 1 | journal rejoué, sorties de juges et promotions permutées, clé remplacée : octets identiques ; trois écritures fautives (promotion, clé, juge) détectées | `gardes` |
| 2 | entrée d'un juge : champs neutres acceptés ; champ du registre, ou ligne glissée, arrêt | `gardes` |
| 3 | prédiction scellée éprouvée et écrite ; sans empreinte : refus d'éprouver ; modifiée : refus d'écrire | `gardes` |
| 4 | chaîne vérifiée ; entrée réécrite sur disque, entrée retirée, entrée réécrite à l'identique en mémoire et sur disque (seule la chaîne la voit) : arrêt | `gardes` |
| 5, 8, 19 | cas sain et artefact chacun | `gardes` |
| 6 | dossiers disjoints ; chemin d'un autre bras servi, dossier commun, dossier inclus : arrêt | `gardes` |
| 7 | vue et retour au grain ; valeur, distance, fraction, nombre hors grain : arrêt | `gardes` |
| 9 | registre identique avant et après ; écriture en génération finale : arrêt (mémoire et disque) | `gardes` |
| 10 | parts servies et tranches disjointes sur des mondes écrits ; une ligne de la tranche servie : arrêt | `gardes` |
| 11 | les deux listes (avec la description ; l'engagement seul) ; justification, prédiction, autre entrée, balise dans un champ : arrêt ; **et dans la consigne même que l'étage de l'organisme sert à l'expérimentateur** : la description y est dans la section balisée, sans justification ni empreinte de prédiction | `gardes`, `organisme` |
| 12 | promotion basculée : appariement identique ; version qui lit la promotion : détectée | `gardes` |
| 13 | générateur sain : ensemble exclu vide, aucune loi appariée par une copie (bras 2 et 3 du copieur : M1 = 0) ; générateur fautif : lois exclues, comptées pour aucun bras, rapportées | `mecanique` |
| 14 | treize tentatives : deux lots ; budget trop court : « non éprouvée (budget) », non gardée, coût nul, dit tel quel au retour | `gardes` |
| 15, 16, 18 | cas sain et artefact chacun (sens inversé ; gain constant ; retrait des plus chers d'abord) | `gardes` |
| 17 | dix tentatives de toutes sortes, échecs de l'expérimentateur compris (doublure « rien envoyé ») : aucun désaccord ; exécuteur au seuil inversé : désaccords détectés ; **une source entière de la couche mécanique, 1 308 tentatives : aucun désaccord** ; copie absente ou altérée : garde non jouée | `organisme` |
| 20 | étiquettes des bras ; même graine : arrêt ; mondes différents : arrêt | `outils` (et dans chaque source jouée) |
| 21 | énumération complète jusqu'à douze différences, zéros et ex æquo ; table du § 3.3 du plan ; zéros retirés avant : détecté | `outils` |
| 22 | étalonnage réel réduit : sortie aux seules clés permises ; test verrouillé pendant l'étalonnage ; « taux de rejet » ou « valeur p » dans la sortie : arrêt ; le module n'appelle aucun test | `statistique` |
| 23 | couche mécanique (12 sources pour les fréquences, 24 sources rejouées sous d'autres graines) contre la couche statistique (20 000 sources) : moyennes dans l'intervalle ; fréquence des lois vraies du monde source divisée par deux, bras 3 du lecteur, dose 0,5 : la précondition à 24 sources est vérifiée, puis arrêt | `mecanique` |
| 24 | fréquences saines : S8 (i) passe ; exécuteur qui rend « tient » à toute loi : arrêt | `mecanique` |
| 25 | marges du générateur de B1 rejugées par l'audit à part, forme unique, comptes ; audit de présentation sain (générateur sain par construction, § 5.2) ; deux lois trop proches : rejet ; dose inscrite : arrêt sur la forme ; poids des dépendantes doublés : signalé sur le contenu, mention « générateur non audité pour l'étage payant » ; bornes gelées : aucun arrêt ; bornes à un tirage et un essai : arrêt « bornes de la construction épuisées » | `mondes` |
| 26 | comptes plantés 500, 501, 5 235, 5 236 ; taille réalisée : réglage étalonné tenu, réglage faussé de 20 % « taille non tenue » | `outils`, `statistique` |
| 27 | registres étrangers servis aux bras 4a et 4b, empreintes ; registre propre au 4a, registre étranger à un bras du critère : arrêt ; tenue sans effet sur les entrées étrangères du 4b | `mecanique` |

Autres essais demandés : intervalle binomial contre la sortie du calcul v2 (intervalles, comptes 553 et 7 981, règle corrigée pour 24, 72, 96 et 144 cases) ; S9 contre la table du calcul v2 ; comparateur contre la table du palier 0a ; reproductibilité à l'octet (une source de la couche mécanique jouée deux fois ; les sorties d'une case jouées deux fois) ; sceau des sorties (un octet changé : arrêt de l'analyse) ; dérivation des graines (étiquette, clé, couches disjointes, refus des couches décisives, autorisation refusée sur un texte non scellé) ; couches décisives refusées au lancement, avant toute simulation et tout dossier ; plan des cases (72 et 72) ; étape 4 et étape 6 réduites ; manifeste ; **essai final `test_zz_aucune_graine_decisive_derivee`** : à la fin de la suite, aucune graine « decisif » ni « confirmation » n'a été dérivée, les seules couches dérivées sont « essai » et « essai-de-forme », et tous les refus consignés sont des refus de couches décisives.

Lancement : `PYTHONPATH=<bloc-notes>/src HERITAGE_DEPOT=/home/user/controle-ia-travail HERITAGE_COPIE_ORGANISME=<bloc-notes>/code-organisme-94bfd92/orchestrator python3 -B -m pytest -q -p no:cacheprovider <bloc-notes>/tests` (chemins absolus, une seule commande ; rien n'est écrit dans le dépôt).

## 3. Contrôle « trop beau » (R4) : défauts réintroduits un par un

Outil `outils-dev/mutations_v1.py` : pour chaque défaut, copie neuve de `src/`, remplacements exacts trouvés chacun une seule fois, essais nommés ; avant tout défaut, chaque sélection d'essais est jouée sur le code sain (« témoin »).

- Premier passage (sortie `mutations-sortie-v1.json`) : témoins au vert ; **39 défauts vus sur 41**. Les deux non vus : « registre propre au bras 4a » (la garde arrêtait encore, par sa seconde condition ; essai resserré sur le motif) ; « marge non relue » (artefact mal planté, § 1, défauts corrigés, point 4).
- Second passage, sur le code final (sortie `mutations-sortie-v2.json`) : témoins au vert ; **41 défauts vus sur 41**.

Les 41 défauts (détail dans les sorties) : zéros retirés avant de classer ; première marche de Holm à 0,05 ; condition des lois fausses sans « strictement » ; tenue appliquée aux entrées étrangères du 4b ; lecteur qui compose dans la course source ; repli silencieux sur strate vide ; fréquence source prise sur la fréquence cible ; double balisage ; seuil comparé à l'envers ; retrait des plus chers ; même graine dans tous les bras ; écriture en génération finale ; ligne de tranche servie ; comparateur qui lit la promotion ; intervalle binomial mal partagé ; grain ouvert ; épreuve sans empreinte ; chaîne non vérifiée ; historique accepté ; bras 1 servi ; cloisonnement ouvert ; juge qui lit le registre ; sens du seuil ignoré ; contre-calcul sans prise ; taux inégaux acceptés ; « non éprouvée » comptée en échec ; verrou d'étalonnage ouvert ; confirmation stricte ; registre propre au 4a ; bornes ignorées ; traits de contenu nuls ; marge non relue ; ensemble exclu jamais rempli ; « éliminée » lue « tient » ; S8 (i) sans prise ; S8 (ii) sans arrêt ; graines des bras non vérifiées ; M10 en valeur absolue ; S9 au rapport strict ; « atteint » sans les nombres suivants ; sorties relues sans sceau.

## 4. Silences comblés (choix du développeur, à relire)

1. **Un lot ne porte qu'un domaine** : l'étage de l'organisme n'a qu'une tranche par appel ; lots de douze au plus, dans l'ordre du scellement, domaines dans l'ordre de leur première tentative.
2. Garde 17 : identifiants servis par `tour_ferme_v64.identifiant_opaque` ; une tentative dont l'expérimentateur simulé a échoué est jouée à l'organisme avec la doublure « rien envoyé » (« non concluant ») ; scipy absent : bouchon qui lève s'il est appelé (comme au palier 0a).
3. B7 bis, « dans les deux sens » : lu à la fois comme les deux ordres de composition des lois étrangères et comme la plus petite des deux divergences (plus strict).
4. Dose du jeu de sources de la garde 27 : le texte ne la dit pas ; les essais la jouent à 0,25 (voir § 5.1).
5. S8 (ii) : l'intervalle de prédiction est lu sur 20 000 moyennes de n valeurs tirées avec remise parmi les valeurs de M1 de la couche statistique (au moins cent sources).
6. Étalonnage : au plus 40 pas de dichotomie ; une cible non convergée arrête ; aux taux 0 et 0,5, l'écart-type entre jumelles des réglages gelés est mesuré à l'étalonnage (la taille réalisée s'y rapporte).
7. Génération finale : même règle de retrait et même budget que les autres générations ; seul le coût de son test de mort est tenu à part.
8. M12 : une loi engagée par plusieurs bras sur un même monde compte une fois, avec l'origine de la première tentative dans l'ordre où les bras sont joués.
9. Graines : champ `tour` ajouté à l'étiquette (suite retirée) ; rôles `monde`, `episodes`, `partage`, `oracle-instances`, `paires`, `echantillonnage`, `echec`, `budget`, `retrait`.
10. Audit de présentation : jetons par expression régulière (mots, nombres avec exposant, signes) ; longueur en caractères ; trait de variance nulle réduit par un.
11. Le lecteur aux deux réglages (famille B) n'est tiré qu'à la taille 1 et au taux 0,25 (rapporté sans critère).
12. Manifeste d'un lancement : les étiquettes y sont résumées (nombre, empreinte de leur liste triée, couches), non listées.
13. Analyse : M10 à chaque nombre est lue sur les k premières sources de tous les tirages.
14. Couche statistique : le généraliste compte les entrées servies qui portent une classe (le statut de budget n'en est pas une).

## 5. Écarts et constats que je n'ai pas pu lever

1. **B7 bis à la dose 0,5 : la construction épuise ses bornes.** Les lois dépendantes ne se tirent pas ; quand l'une manque la marge face à une composition de la source étrangère, le texte fait retirer la suite. Sur les graines d'essai, une source compte de 0 à 20 compositions en conflit sur 28 selon le tour (12 tours par cas, `outils-dev/diagnostic_conflits_etrangers.py`) ; à la dose 0,5, 24 des 28 paires sont des lois dépendantes, et la probabilité d'un tour sans conflit est estimée entre 1,3 % et 8,6 % selon la source étrangère et la lecture de « dans les deux sens » (0,0133 et 0,049 pour la source étrangère de l'essai ; 0,085 et 0,086 pour une autre). Un essai à trois sources a épuisé les 200 tours. À la dose 0,25, l'essai à trois sources passe. Le code arrête comme le texte le veut (liste d'arrêt, point 2) ; il faut un mot (dose du jeu de la garde 27, ou erratum ; réserve 20).
2. **Audit de présentation, traits de forme, dépendantes contre indépendantes : un signal.** Sur 8 suites par dose (graines d'essai, 288 lois dépendantes, 480 indépendantes), la longueur du texte canonique diffère (305,46 contre 306,22 caractères, t = −4,1) et donne seule une exactitude équilibrée de 0,565 ; la cause est le nombre de signes moins (8,52 contre 9,08 par loi) : les sous-lois de la source passent un filtre sévère (environ 15 % d'acceptation, par moitié, entre elles), les indépendantes un filtre lâche (environ 92 %). C'est la réserve 17 qui se voit dans la forme. Réserve : les dépendantes partagent leurs sous-lois, l'échantillon est pseudo-répliqué, et l'ampleur à pleine taille n'est pas connue ; mais si l'étape 3 la retrouve au-dessus de 0,55, c'est un arrêt. Je n'ai rien changé au générateur (dessin gelé) ; la voie écrite est celle de la réserve 18. Conséquence pour les essais : le cas sain de la garde 25 pour l'audit de présentation est éprouvé sur un générateur sain par construction (lois tirées de la même loi quelle que soit leur sorte, 300 mondes par dose), non sur celui de B1.
3. **Bruit de l'audit des doses à pleine taille.** À 8 suites par dose, les exactitudes par paires de doses vont de 0,34 à 0,59 selon la graine de validation croisée, sans aucun trait de forme à |t| > 1,7. À 50 suites par dose (200 mondes), l'écart-type d'une exactitude équilibrée est de l'ordre de 0,025 (ordre de grandeur, non mesuré) : un générateur parfait dépasserait 0,55 sur l'une des cinq exactitudes de forme avec une probabilité qui n'est pas négligeable. Information pour la mère.
4. La copie de l'organisme est au commit `94bfd92`, non au commit `a41b7b50` que cite le rapport du palier 0a ; les seize fichiers employés ont exactement les empreintes de son manifeste.
5. Ce qui reste incomplet : l'analyse a les règles des critères, R, M9, M10, M11, S7, S9 et la taille réalisée, mais pas encore de programme qui lise toutes les sorties d'un lancement et écrive d'un coup tout ce que « Ce qui est rapporté » nomme (M8, M14, le généraliste, les reliquats n'ont que les fonctions générales) ; l'étape 9 se lance par `tirages.lancer_famille` sous la couche « confirmation », sans lien automatique depuis les comptes. Aucun essai de forme n'a été joué au-delà d'un essai du code à deux tirages.
6. Les trois remplacements de tenue du contrôle du différentiel v6 ne touchent pas le code ; non appliqués (hors de mon mandat).

## 6. Gestes à dire

- Ma première vérification de l'environnement a été lancée par une commande composée (`cd … && python3 -B scripts/verifier_environnement_agent_v1.py …`), contre « une commande simple à la fois » ; toutes les suivantes sont simples. Aucun heredoc, aucun bloc de code ou de texte passé à un interpréteur : chaque calcul passe par un fichier de script.
- Les outils de développement ont calculé, sur des graines « essai » seulement, des moyennes de M1, des tailles réduites (quelques réglages de τ et de K), des intervalles de prédiction et des exactitudes de l'audit de présentation à taille réduite ; aucun taux de rejet, aucune puissance, aucun taux de déclenchement, aucune valeur p sur un tirage simulé. Aucune graine des couches « etalonnage », « mecanique », « mecanique-reglages », « audit », « decisif » ou « confirmation » n'a été dérivée hors des essais de refus.
- Aucun appel à un fournisseur de modèles, aucune dépense, aucun réseau, aucune machine ; aucun commit, aucune poussée, aucune écriture dans le dépôt (`git status --porcelain` vide) ; rien lu ni touché sous `archives-reponses-modeles/` ; aucune valeur de clé.

## 7. Fichiers

Rendus (bloc-notes `dev-palier-0b-v2/`, arborescence du dépôt ; chacun avec son compagnon `.sha256`, au format de `sha256sum` lancé dans le dossier du fichier, écrit par `outils-dev/sceller_v1.py`) :

```
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  src/controle_ia/__init__.py
ba3d58e25b499a89d00bf9e2eab524d838297c9214277ba09823b656fe941935  src/controle_ia/heritage_etage_processeur_v1/__init__.py
319f29b3e94683961524c4ec37a5125597543b13330ecdab7aa9243f9e785af0  src/controle_ia/heritage_etage_processeur_v1/analyse.py
11352fcd12b531c375abf40f68fdefcf45bc4feba822b3d88169bb852687bddd  src/controle_ia/heritage_etage_processeur_v1/audit.py
8758b015d523370d6d1a98ff3fdebbe0fdc823805abaf9aa1fd024f48d9d64a7  src/controle_ia/heritage_etage_processeur_v1/comparateur.py
37e848c2706a9c9d30673a1e8153f46ffa573b2d141229cffae73646ec2966c3  src/controle_ia/heritage_etage_processeur_v1/constantes.py
684aeed62fd8ecc902c42e503e8211385e275e5feee36dec6d6e922afc2014bb  src/controle_ia/heritage_etage_processeur_v1/cout.py
2173613ae03067c4ff3090f74644f86550ca1d127702ff41443d1dc6a574a799  src/controle_ia/heritage_etage_processeur_v1/enveloppe.py
fda98bba41c57cbd4860a62d93c7e12f3d23d098f148af0e79b48ec20417eee3  src/controle_ia/heritage_etage_processeur_v1/equivalence.py
f3c5113bf43c0ff9b507c53ac4327e4dccf8410176e57b747ce498ea1e46fdc8  src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
a47c8fa2acfd16caaeee3d420fdffe00adce9d7ab876c976f94b96108ad5b725  src/controle_ia/heritage_etage_processeur_v1/etapes.py
063df6e1e2c08d79531fce8b76f3e3dbc3fdb002af7657efb1773e33afb9beda  src/controle_ia/heritage_etage_processeur_v1/executeur.py
dce5db04472d049f350f08d56f65a8254fb58eb13f3f2b6a0c3ca2e95952fcd5  src/controle_ia/heritage_etage_processeur_v1/frequences.py
cf433337972c02baefe2f57323f036d98649b5b25fb8da1afd59bd12ab2e8c13  src/controle_ia/heritage_etage_processeur_v1/graines.py
4492c8545f6fc081eb267d851bd24a011fe4817cadad8b9606048bb26208dc1f  src/controle_ia/heritage_etage_processeur_v1/intervalles.py
fb24a9eaffdc98ee080db835d77ee2c419242ad4108ef60b440df8f1cb387536  src/controle_ia/heritage_etage_processeur_v1/lois.py
587bc3f9e350671b4d94efeb778ee35b76e530df8b4b2eb532bf2063ad35bcb8  src/controle_ia/heritage_etage_processeur_v1/mecanique.py
593f61ea1d7a27f8c2197c790b221dd2ef55ec2da6d06c96053bece4275d6670  src/controle_ia/heritage_etage_processeur_v1/mondes.py
fb2f7b48234661c2c825e2dc0c1cb7b9a6f576ff6bdebb3a2196aa3efe9293f1  src/controle_ia/heritage_etage_processeur_v1/organisme.py
e0aa6b89501c4cfeaed67d748db02dba1cb015405c34a91955d70dc2e408ab83  src/controle_ia/heritage_etage_processeur_v1/proposeurs.py
9a386fc7d56cc3f10369ef066e1f9daae7f3e41e592dd9ab4cd2b7b6768c6417  src/controle_ia/heritage_etage_processeur_v1/rangs_signes.py
282ec49ee9734c72520cf75525c2a9dd45eb8f2833cc8c914e9660e263828404  src/controle_ia/heritage_etage_processeur_v1/registre.py
60e050e603ccb2e602d5a9a3b38bdb1edcca241151fcde623334d45e623cfb0e  src/controle_ia/heritage_etage_processeur_v1/statistique.py
fe150097f08f32f4eb8cf212f0da0b30acb8fbff9b0965d9807e42236d198e59  src/controle_ia/heritage_etage_processeur_v1/tirages.py
372229230356317c51990c0a45ed7e811e37ba2579e7b8c99f8d418bf7dbd236  tests/aides_heritage_etage_processeur_v1.py
444f30432e9551c50ef7fc34d6ca232c08478f5d207f13a47c79bbabdbf74f0e  tests/test_heritage_etage_processeur_v1_etapes.py
acd1954670935fc87778411602519916af0b7be8e08decce2aa86f7636996d12  tests/test_heritage_etage_processeur_v1_gardes.py
68c1cab3011500a926bbb4e268f282be3762ceeecd899e9934f5500742ac7446  tests/test_heritage_etage_processeur_v1_mecanique.py
493488e605a22a4b27ac2dda6e16d4b77264e9e86ea98cb2af6a06e9457d2eaf  tests/test_heritage_etage_processeur_v1_mondes.py
2697382c1ce050b590d956078796e5c9c5225ea1ad37d08c2ded011a47799461  tests/test_heritage_etage_processeur_v1_organisme.py
3162d852ce59c5eb263236bf9c154911a47ea8eb13d262794614953937ec0a4f  tests/test_heritage_etage_processeur_v1_outils.py
f9cb610180b74f2ce15b47586eb71aecf6f622827a28aad3d7c7c852a6798aa5  tests/test_heritage_etage_processeur_v1_statistique.py
f9e6f295cb3ff546097f8a0e24b08d2f481adcf302d1a9cfbf6291dc65efd1ce  tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py
0513640b0cbaedcc0e832da8d96f022a3b231ea7cc6eab40062a96714c8629e2  outils-dev/chrono_statistique.py
af772fb9918a3e69ea1bde8a34c0ac68bc8622321e0e600d0d8c8766da02f3d2  outils-dev/chrono_suite.py
fefceead89b91a30eb738e12480ff96c0356c5b2b26f4d4b9d05b5825db737cf  outils-dev/diagnostic_conflits_etrangers.py
5bf7bd44a892ef4fb66981592247131d13fa7ca5e903e4d2cb483a6e9db4d965  outils-dev/diagnostic_etrangere.py
10af2b5ab0e2d88ab9f4a9b395a555044e4ec140108b7c8d20351bf9eb1f5c3e  outils-dev/diagnostic_forme_dependantes.py
8493e5f79964ba75ea8a89b18df3cb8629a25e7570955f0b26aba0a77a0b47ea  outils-dev/diagnostic_import.py
8b2ba07ba7a009b5fab7333e206d9734a6e4de0b943f312c52b2e1cdd1c36ea9  outils-dev/diagnostic_presentation.py
12a2da99ced510c42f03645f4068f14dffa3f86787431cbd7cb67ac3ec85c9cf  outils-dev/empreintes-attendues-palier-0a.txt
b182d5ed92e5e92b7a4a14b26bb47ca4fd80bd0ce9fc916a716d51a61cfaea9e  outils-dev/essai_equivalence.py
580190bfd609195a8e5999401c264b9d8c5842a6bb0571cd28b1cc7df875a8dc  outils-dev/essai_mecanique.py
c5476e7b359b2c15b77795832d8f1849dc23bdc6d0aef7386b179170a4123fee  outils-dev/mutations_v1.py
7254490fe4be80b52fa7cc46e369dbb6fd8d38300265b9a98a82069a0fad56ce  outils-dev/mutations-sortie-v1.json
0f19dd4c146ef3a6df5c6cc95dea9dd343ce53824b9310212657f9b9445a9dc5  outils-dev/mutations-sortie-v2.json
c8a9ed8d7339129d311c787ad5f49c0ef7347c70cfae4b34fabf82f8e6fe6e55  outils-dev/sceller_v1.py
ff647eaf2ead2bd14a1a00a000f09dc142b805fbbeb6aaf87b74f225faaa72d6  outils-dev/verification-empreintes-organisme-v1.json
```

Notes : `lois.py` est repris sans changement du dossier versé (même empreinte que celle qu'en cite le préenregistrement) ; `mutations-sortie-v1.json` vient de la version de `mutations_v1.py` antérieure à une correction (le défaut « marge non relue » y mettait le seuil à 0, il le met à −1 depuis) ; `mutations-sortie-v2.json` vient de la version rendue. Le code n'a pas changé entre la suite entière au vert et le second passage du banc. Ce rapport a son propre compagnon.

Non rendus, laissés dans le bloc-notes : `verse-v1/` (copie du dossier versé), `code-organisme-94bfd92/` (copie du code de l'organisme), `tmp/` (sorties temporaires des outils et du banc de défauts), `heritage/palier-0b/code-v2/brouillon-constats.txt` (brouillon).
