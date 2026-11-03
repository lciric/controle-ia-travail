# Préenregistrement — pilote de l'exposant p : plan (évaluation, registre) sur Llama-3.1-8B-Instruct — v1, brouillon 1

Gabarit : `prereg/gabarit-preregistrement-v1.md` (R1, R2). Brouillon **non scellé**, à contre-lire par un sous-agent neuf (R2). Au scellement, il sera copié sous `prereg/pilote-exposant-p-v1.md`, chemin par défaut du script d'instance. Les marqueurs `<<…>>` restent jusque-là : le validateur `controle_ia.prereg` refuse de sceller tant qu'il en reste.

- Auteur : concepteur-rédacteur neuf du pilote (sous-agent ; aucun autre texte du dépôt), pour Lazar Ciric.
- Date (UTC) : 2026-11-03, rédaction de 08:50 à 09:10 (`date -u`).
- Commit du code d'analyse : <<COMMIT_SCELLEMENT>>
- Documents qui font foi (chemin + empreinte) :
  - `docs/programme-controle-ia-v2.md` — `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` ; `docs/brief-claude-code-programme-complet-v2.md` — `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` ; `CLAUDE.md` — `a2aabda8a181d46d9723bad44ad352b5e61650634e0f3bc4863451229af00b1b`.
  - Lecture du papier : `brouillons/pilote-exposant-p-v1/lecture-2606-24964-v1.md` — `3c550d93ae97e37309ef01a95e1829c946463edf1cd7013110c95c2eed815851`.
  - Chemin de la configuration du pilote : `brouillons/pilote-exposant-p-v1/config-pilote-exposant-p-v1.json` — `18b724d2e22e23c66a658aeaf5225bbebb38fb61d87b6ca4686f83ee6f80598c`.
  - Chemin des stimuli du pilote : `brouillons/pilote-exposant-p-v1/stimuli-pilote-exposant-p-v1.json` — `eae95d0ee4d4d9ddcb54d5847cc03f707d70018d3c9129a5764686852c2977a3`.
  - Références publiées converties : `src/controle_ia/pilote_exposant_p/references_publiees/references-publiees-v1.json` — `b594ee86b6d5ee1e6355203eca416815fc87e0e4c55eaf7f8b4b66675516375a` ; `grilles-publiees-v1.npz` — `c30a014a2e03aed0ce69dc43ea80488a7a47c0eb013f558c59c36f574ece9fbe` ; `directions-publiees-v1.npz` — `ced98c6285e0a6f7c0dd31189d2a00916b38fd764410fb32d9891821990380b0`.
  - Copie amont (MIT, commit `a9355d4001500708a40a255bacfe559e6dc269c0` de `github.com/FranciscoHS/fsec-paper`) : `amont/parametrize.py` — `35e855f048daeccdb6406a66658effd2401d12cafb83322297c55ff06d183303` ; `amont/superellipse.py` — `47d19c99147577d6670f5727eb23a8de5336f5677d3d2f6c342974d20dd0da0d`.
  - Simulation de puissance : `src/controle_ia/pilote_exposant_p/puissance.py` — `b78f36defe944719a0019d20d649d94a11324287c53d529a262f1d046acc0743` ; sortie `brouillons/pilote-exposant-p-v1/puissance-pilote-exposant-p-v1.json` — `35dc3bdf5cb02d28737f85331a13b532a0b28a4abb88bfdcd507cd2f13dba29f`.
  - Critères gelés codés : `src/controle_ia/pilote_exposant_p/analyse.py` — `86a619348b0b937ed5eef3c99868e7067ff7008fe22877f9ec9bcce0fc949429`.
- Tests attendus : `62` (fichiers `tests/test_pilote_exposant_p_v1.py`, `tests/test_manifeste.py`, `tests/test_scellement.py`, `tests/test_prereg.py`, tous passés, aucun sauté).
- Nœuds avant tout lancement : GO de Lazar sur le devis (`brouillons/pilote-exposant-p-v1/devis-pilote-exposant-p-v1.md`) ; scellement de ce texte, de la configuration et des stimuli ; verdict de contre-lecture traité.

## Hypothèse

**Question.** Dans sa réponse au mentor Stefan Heimersheim (question 1, option c), Lazar soutient ceci : une direction « je suis évalué », extraite par paires contrastives, se confond avec le **registre** (formel, artificiel, questionnaire contre conversation). Le pilote mesure, avec l'instrument du papier du mentor (Ferreira da Silva et Heimersheim, arXiv 2606.24964, éq. 8 à 13), si Llama-3.1-8B-Instruct traite une direction d'évaluation E et une direction de registre R comme des directions pures privilégiées sur leurs mélanges (exposant p > 2, comme les directions contrastives du papier), ou comme une paire sans concept (p proche de celui des différences aléatoires).

**Énoncé testé (H-P).** À la couche 2, dans le plan (E, R), l'exposant p de la superellipse de rupture du plateau diffère de celui des plans de différences aléatoires du même modèle, sur les mêmes ancres. L'énoncé est ouvert dans les deux sens. L'issue « égal », dans une marge fixée, est une réponse pleine, pas un échec.

**Directions.**
- **E** (évaluation − déploiement) : différence des moyennes sur 60 paires **à registre apparié**. 30 paires ont leurs deux membres formels, 30 leurs deux membres familiers. Dans une paire, les deux membres ont la même ouverture et le même registre ; seule la fin change (évaluation de l'assistant contre besoin réel d'une personne).
- **R** (formel − familier) : différence des moyennes sur 60 paires **à statut d'évaluation constant** : 30 paires dont les deux membres sont « évaluation », 30 dont les deux sont « déploiement ». Même contenu dans la paire.
- Les deux viennent du même plan 2 × 2 de 30 quadruplets (formel ou familier, croisé avec évaluation ou déploiement), règles R-S1 à R-S7 du fichier de stimuli : chaque direction est un contraste équilibré de l'autre facteur. Le contraste d'évaluation est placé près de la fin, selon la règle des invites du papier (mot porteur « at or near the end »).
- Les stimuli de l'échelle de conscience d'évaluation du programme (`echelle-v2.json`, branche `outils/echelle-conscience-eval-v3`) ont été examinés. Ce sont des invites de conversation longues, et leur cadrage d'évaluation est en tête, loin du dernier jeton : au protocole du papier (couche 2, dernier jeton), le contraste n'y est pas capté. Leurs 12 paires de cadrage, en dessous du minimum de 30, sont gardées comme contrôle descriptif (cos(E, E_échelle)).

**Rattachement au programme.** Le pilote ne teste aucune des hypothèses H1 à H9. Il touche la section 11 (validité de construit, transversale) et le construit « conscience d'évaluation » de H8. Il sert la réponse de Lazar au mentor. L'inscrire au programme serait une modification de revendication, donc un nœud de Lazar.

**Hypothèses de travail** (non testées ici, déclarées) :
- l'instrument du papier, validé sur le modèle de base, se transporte au modèle Instruct ; c'est contrôlé par le témoin positif sur le modèle de base et par les isotropes sur le modèle lu ;
- à la couche 2 et au dernier jeton d'invites courtes, E et R sont des directions surtout lexicales et sémantiques, comme les directions du papier. Le pilote ne dit rien des couches moyennes, des contextes longs ni du comportement ;
- p > 2 est nécessaire mais pas suffisant pour qu'une direction soit un trait (§7 du papier) ; des lectures rivales des plateaux existent (§6.2).

## Prédiction chiffrée et signe attendu

**Aucun pari de signe (R3).** Aucun run ne vise un signe positif. Les trois issues sont écrites d'avance, chacune avec son ordre de grandeur et sa phrase gelée (section « Critères de lecture gelés »). Δ = p̄(E, R) − p̄(différences aléatoires) :

| Issue | Ordre de grandeur de référence (publié ou calcul) | Ce qu'elle réfute |
|---|---|---|
| **au-dessus** (intervalle de Δ entièrement > 0) | si (E, R) se comportait comme une paire contrastive moyenne du papier sur Llama : Δ ≈ +0,4 à +0,7 (contrastives de Llama, moyenne 2,632, audit du code ; isotropes de Llama 1,930, calcul ; différences aléatoires de Gemma 2,05, §4.1) | p(E, R) = p(différences aléatoires) |
| **égal** (0 dans l'intervalle, intervalle dans ±0,2) | Δ ≈ 0, comme une paire sans concept | tout écart de plus de 0,2 dans un sens ou dans l'autre |
| **au-dessous** (intervalle entièrement < 0) | possible : des paires contrastives du papier ont p < 2 sur Llama (Français × Japonais 1,28 ; JavaScript × Rust 1,50, calcul sur `fits_llama_L2_thrpair_exact.pkl`) | p(E, R) ≥ p(différences aléatoires) |

Issues hors de ces trois : « non concluant » (0 dans l'intervalle, intervalle hors de ±0,2) ; « exclu » (|cos(E, R)| ≥ 0,1) ; « instrument non validé ».

**A priori du rédacteur** (déclaré pour la transparence, sans effet sur la lecture) : au-dessus 0,35 ; égal 0,25 ; au-dessous 0,10 ; non concluant 0,15 ; exclu 0,15 (supposé).

**Valeurs attendues des témoins** (elles fixent la validation de l'instrument, pas l'issue) :
- Wealth × Gender sur Llama-3.1-8B de base, sous-ensemble d'ancres 0 : p publié 3,003, intercepts 46,50° et 28,95° (code publié) ;
- moyenne des 17 plans isotropes sur le modèle lu dans [1,75 ; 2,25] (repère : 1,930 sur le modèle de base, calcul) ;
- directions Gender et Wealth extraites sur le modèle de base : cosinus ≥ 0,98 avec les directions publiées.

## Métrique

- **p d'un plan** (protocole du papier ; calcul fait par la copie amont, sans modification) :
  - grille de 31 × 31 points (α₁, α₂) ∈ [0, 60°]² en carte exponentielle, à norme constante (éq. 9) ;
  - perturbation du résidu du dernier jeton à la sortie du bloc 2 ; réponse = distance L2 à la sortie du bloc 30 (avant-dernière couche ; référence = l'ancre non perturbée) ;
  - grille médiane sur les 30 ancres d'un sous-ensemble ; seuil T = 0,5 × min des maxima des deux axes (éq. 3) ;
  - contour au niveau T, normalisation géodésique exacte (éq. 13), fenêtre de 60°, p borné dans [0,5 ; 10]. p vaut NaN si l'ajustement est impossible. Sorties consignées : nombre de points de contour, résidu (annexe B), intercepts.
- **p̄(E, R)** : moyenne des p du plan (E, R) sur S = 32 sous-ensembles disjoints de 30 ancres. Chaque ajustement suit le protocole du papier à 30 ancres.
- **p̄(différences aléatoires)** : moyenne des p des M = 60 plans de paires disjointes de différences aléatoires, moins les paires exclues par la règle du cosinus, sur le sous-ensemble 0.
- **Δ** = p̄(E, R) − p̄(différences aléatoires). Intervalle à 95 % : percentiles 2,5 et 97,5 de 10 000 rééchantillonnages conjoints avec remise des 32 sous-ensembles du plan lu et des plans de référence (`ajustement.bootstrap_difference`, graine de la tâche `bootstrap_difference`).
- **cos(E, R)** : cosinus signé des directions unitaires brutes, avant projection tangente. |cos| sert à la règle d'exclusion.
- Unités : p, Δ et cosinus sans dimension ; angles en degrés.

## Seuil

- **δ = 0,2**, marge d'équivalence. C'est environ la moitié du plus petit écart publié entre famille contrastive et famille sans concept (Gemma : 2,42 − 2,05 = 0,37, §4.1), arrondie au dixième.
- **Exclusion** : |cos(E, R)| ≥ 0,1, règle du papier (§4.1 ; annexe A). Même règle pour les plans de référence.
- **Niveau** : intervalle à 95 %. Taux simulés à Δ = 0 (calcul, `puissance-pilote-exposant-p-v1.json`) : faux « au-dessus » 2,8 %, faux « au-dessous » 3,0 %.
- **Puissance** (calcul, même fichier ; générateur calé de façon prudente sur le bruit publié) :
  - plan retenu (S = 32, M = 60) : Δ = +0,20 détecté « au-dessus » dans 90,7 % des cas, Δ = +0,15 dans 72,0 % ; Δ = −0,20 « au-dessous » dans 93,8 % ; Δ = 0 « égal » dans 86,8 % ; demi-largeur médiane de l'intervalle 0,11 ;
  - à titre de comparaison : S = 16 détecte Δ = 0,3 (0,2 dans 78,7 %) ; S = 8, M = 30, Δ = 0,4 ; avec S = 4, rien jusqu'à 0,4 à 80 %.
- **Instrument** (contrôles fixés d'avance, `analyse.py`) :
  - directions publiées : cos ≥ 0,98 pour Gender et Wealth ;
  - témoin positif sur le modèle de base, sous-ensemble 0. Si les ancres sont celles du papier (norme moyenne à 10⁻³ près de 2,379805), il faut |p − 3,003| ≤ 0,15 et des intercepts à ±2° (supposé : écarts numériques seuls). Sinon, p dans [2,420 ; 3,702], intervalle à 95 % du rééchantillonnage des ancres publiées (calcul) ;
  - isotropes sur le modèle lu : moyenne dans [1,75 ; 2,25], et au plus 20 % d'ajustements impossibles.

## Plan d'analyse

**Données.**
- Modèles : `meta-llama/Llama-3.1-8B-Instruct` (lu) et `meta-llama/Llama-3.1-8B` (témoin, modèle du papier), `bfloat16`, attention `sdpa`. Révisions relevées puis figées au chargement, consignées.
- Ancres : réserve de 10 000 entrées FineWeb-edu de 5 jetons, au protocole du code publié (`sample-10BT`, mélange graine 42, tampon 10 000), révision du jeu relevée et figée. Les 960 premières forment 32 sous-ensembles de 30 ; le sous-ensemble 0 est celui du papier si le flux est le même. Invites brutes, sans gabarit de conversation, BOS compris.
- Stimuli : fichier figé, règles R-S1 à R-S7 vérifiées par garde ; les invites du papier qui y sont recopiées redonnent les empreintes publiées.

**Plans** (ordre gelé ; « décisif » = nécessaire à la lecture) :

| Bloc | Modèle | Plans | Sous-ensembles | Statut |
|---|---|---|---|---|
| 1 | base | Wealth × Gender | 0 | décisif (témoin positif) |
| 2 | base | 17 isotropes du code ; Wealth × Gender | 0 ; 1 à 7 | descriptif |
| 3 | lu | 17 isotropes | 0 | décisif (instrument) |
| 4 | lu | (E, R) | 0 à 31 (0 seul si exclu) | décisif |
| 5 | lu | 60 différences aléatoires disjointes (120 directions, 30 différences chacune) | 0 | décisif (référence) |
| 6 | lu | (E, rdₖ) et (R, rdₖ), k < 10 ; famille contrastive (paires de Gender, Wealth, Age, Tense, Sentiment, filtre du cosinus) ; Wealth × Gender ; mixtes (Gender, rdₖ), (Wealth, rdₖ), k < 5 ; moitiés (E_A, R_A), (E_B, R_B) ; (E, Formal du papier) | 0 ; 0 ; 0 à 31 ; 0 ; 0 à 7 ; 0 à 7 | descriptif |

**Taille.** 230 plans de 30 ancres × 961 points, soit 6,6 millions de passes avant de 5 jetons (calcul). La puissance justifie S = 32 et M = 60 (section « Seuil »).

**Graines (R9).** `SeedSequence` d'entropie 2026110301 (configuration) ; tâches `differences_aleatoires`, `bootstrap_difference`, `bootstrap_ancres` ; manifeste par run (`runs/<run>/manifeste.json`). Les directions isotropes sont celles du code publié (graine 42 de torch), reproduites à l'identique et prises comme stimuli fixes.

**Comparaison principale.** Une seule (Δ) : aucune correction pour comparaisons multiples. Toutes les autres quantités sont descriptives et ne se lisent pas comme décisions :
- moyennes, avec intervalle, des familles (E, rd), (R, rd), mixtes, contrastive, témoin sur le modèle lu, moitiés, (E, Formal) ;
- rangs de p̄(E, R) dans les familles de différences aléatoires et contrastive ;
- cosinus E·R, E_naïf·R, E_naïf_inverse·R, E·E_échelle, E_A·E_B, R_A·R_B, R·Formal, E·Formal, E·Literary, R·Literary, Formal·Literary ;
- étendue de Δ quand on retire un sous-ensemble d'ancres ;
- sur le modèle de base : isotropes et Wealth × Gender sur 8 sous-ensembles, comparés aux valeurs publiées.

**Contrôles appariés.**
- Différences aléatoires : même estimateur sur des paires sans concept ; c'est la ligne de base la plus exigeante du papier.
- Isotropes ; témoin positif publié.
- Plans mixtes (trait du papier, différence aléatoire) : ils calibrent la lecture des plans (E, rd) et (R, rd), que le papier n'a jamais mesurés.

**Sorties** (`diag/<run>/`, scellées) : `plans.json`, `sorties.json`, `lecture.json`, `resume.json`, `grilles.npz` (grilles par ancre de chaque plan), et `arret.json` en cas d'arrêt.

### Écarts au papier, déclarés un par un

- E-01 — Modèle lu : Llama-3.1-8B-Instruct ; le papier mesure Llama-3.1-8B de base (`README` du code). Le témoin positif se fait sur le modèle de base.
- E-02 — Directions nouvelles E et R : le papier n'a aucune direction d'évaluation ni de registre formel ou familier dans ses 33 directions. `Formal` existe dans le code mais il est exclu au tracé ; il n'est ici que descriptif.
- E-03 — 60 paires par direction pour E et R ; le papier exige P ≥ 30 et en prend 30 en général. Les moitiés A et B (30 paires chacune, P du papier) servent à la fidélité.
- E-04 — Plan 2 × 2 en quadruplets, pour équilibrer le registre dans E et le statut d'évaluation dans R ; le papier utilise des paires simples.
- E-05 — 32 sous-ensembles de 30 ancres pour (E, R) et pour le témoin sur le modèle lu (960 ancres), avec moyenne des p ; le papier fait un seul jeu de 30 ancres. Chaque ajustement garde le protocole à 30 ancres. Les familles de référence n'utilisent que le sous-ensemble 0.
- E-06 — Différences aléatoires : 60 paires disjointes de 120 directions, tirées par `SeedSequence` (R9) ; le papier prend 40 directions et 780 paires (toutes les combinaisons), tirées avec la graine 42 de torch.
- E-07 — Isotropes : les 17 paires de référence du code ; le papier en prend 528, sur Gemma.
- E-08 — Intervalle : rééchantillonnage conjoint des sous-ensembles d'ancres et des plans de référence ; le papier rééchantillonne les directions en grappes, pour des moyennes de familles.
- E-09 — Passage avant : modèle complet avec crochets, en lots de 961 points ; le papier repasse les blocs sans masque explicite, en lots de 64. Les arrondis de `bfloat16` diffèrent.
- E-10 — Les plans de référence exclus par la règle du cosinus ne sont pas mesurés ; le papier les mesure puis les filtre.
- E-11 — Invites brutes sur un modèle Instruct (comme le papier, mais le papier ne mesure que des modèles de base) ; aucun gabarit de conversation.
- E-12 — Logiciels : `torch` 2.14.1, `transformers` 5.18.0, `datasets` 5.1.0 ; le papier ne donne pas ses versions.
- E-13 — Révision de FineWeb-edu figée au run ; les ancres peuvent différer de celles du papier. La règle du témoin positif couvre les deux cas.
- E-14 — Tolérances de l'instrument (isotropes, directions) : elles ne viennent pas du papier ; elles sont fixées ici.
- E-15 — Plans mixtes (trait, non-trait) : absents du papier ; descriptifs.

## Critères de lecture gelés

| Condition (dans cet ordre) | Issue | Phrase gelée (`analyse.PHRASES`) |
|---|---|---|
| un contrôle de l'instrument échoue | instrument non validé | « Instrument non validé, rien n'est lu (motif). » — aucune phrase sur E ni sur R |
| \|cos(E, R)\| ≥ 0,1 | exclu | « … la direction d'évaluation extraite à registre apparié et la direction de registre se recouvrent au-delà du seuil d'exclusion du papier (\|cos\| = x ≥ 0,1) : p n'est pas lu ; le recouvrement est le résultat. » |
| plus de 20 % d'ajustements impossibles pour (E, R) ou pour la référence | non concluant | « … non concluant … » (motif consigné) |
| intervalle de Δ > 0 | au-dessus | « … au-dessus de celui des différences aléatoires … : le réseau privilégie les directions pures E et R sur leurs mélanges plus que pour des paires sans concept ; c'est compatible avec une correction propre à chacune, ce n'est pas une preuve que E est un trait (p > 2 nécessaire, non suffisant, §7 du papier). » |
| intervalle de Δ < 0 | au-dessous | « … au-dessous … : les mélanges de E et R rompent le plateau plus tôt que la seule taille L2 ne le prédit ; aucun privilège des directions pures, au contraire. » |
| 0 dans l'intervalle, intervalle dans [−0,2 ; +0,2] | égal | « … indiscernable de celui des différences aléatoires … : écart dans ±0,2 ; à cette couche et sur ces ancres, rien ne distingue la paire (évaluation, registre) d'une paire sans concept. » |
| sinon | non concluant | « … non concluant (l'intervalle contient 0 et sort de ±0,2). » |

Chaque phrase porte les chiffres p̄(E, R), p̄(différences aléatoires) et Δ, avec leurs intervalles. Toutes sont bornées : couche 2, ancres de 5 jetons, réponse L2, modèle Instruct sans gabarit.

**Lecture des combinaisons** (descriptive, vocabulaire gelé) :
- « au-dessus », avec des plans mixtes (Gender, rd) et (Wealth, rd) de p proche de Wealth × Gender sur le modèle lu, et des plans (E, rd) au-dessus des différences aléatoires : on peut écrire « E se comporte comme une direction privilégiée dans les plans mixtes aussi ». Si les mixtes restent proches de 2, la lecture des plans (E, rd) n'est pas calibrée, et rien n'est dit de E seul ;
- « égal » ou « au-dessous » : aucune phrase sur l'absence de trait d'évaluation (§7 : p > 2 n'est pas suffisant, et p ≈ 2 n'exclut pas un trait mal aligné, §6.1) ;
- le rang de p̄(E, R) dans la famille contrastive du modèle lu est rapporté, jamais lu comme décision ;
- cos(E_naïf, R) contre cos(E, R) mesure ce que l'appariement du registre retire. C'est attendu par construction : on le rapporte, on ne le lit pas comme découverte.

**Audit de symétrie (R4)**, déclenché de la même façon dans les deux sens (`analyse.declencheurs_symetrie`) :
- toute issue tranchée (au-dessus, au-dessous, égal) entraîne l'audit complet : l'issue doit tenir quand on retire chaque sous-ensemble d'ancres ; on vérifie les résidus d'ajustement, le nombre de points de contour, les échecs, les intercepts ;
- demi-largeur de l'intervalle de Δ < 0,05 : réserve « trop beau » ;
- témoin positif égal à la valeur publiée à 0,01 près avec des ancres différentes : réserve ;
- résidu médian du plan (E, R) > 2 % (le papier n'en a aucun au-dessus de 2 %) : réserve.

Une réserve ne change pas l'issue gelée ; elle accompagne la phrase.

## Liste d'arrêt

| Condition | Action |
|---|---|
| Aucun GO consigné dans `registres/go.md` | rien ne se lance (garde de calcul) |
| Préenregistrement, configuration ou stimuli sans sceau, ou sceau non conforme ; citation absente ou en double | arrêt avant l'installation (script) |
| Branche `calcul/…` déjà présente sur le dépôt distant | arrêt avant l'installation |
| Accès refusé à l'un des deux modèles | arrêt avant les essais, consigné ; le jeton n'est jamais affiché |
| Dépendances du pilote non installables sans changer une version figée | arrêt avant les essais |
| Essais : autre chose que « 62 passed » | arrêt avant le run |
| Constantes de lecture de la configuration ≠ code d'analyse ; empreinte des stimuli, des références ou de la copie amont ≠ citée ; règle de stimuli violée ; invites du papier ≠ empreintes publiées | arrêt avant le manifeste (`GardeArret`) |
| Flux FineWeb-edu de moins de 10 000 entrées | arrêt, consigné |
| Directions publiées non reproduites, ou témoin positif hors tolérance | « instrument non validé » ; arrêt avant le modèle lu ; sorties écrites ; code 3 |
| Le tokeniseur du modèle lu ne lit pas les ancres comme celui du modèle de base | arrêt |
| Isotropes du modèle lu hors tolérance | « instrument non validé » ; arrêt ; code 3 |
| Grille non finie | arrêt |
| Durée projetée au-delà de 14 400 s avant un bloc décisif | arrêt ; un bloc descriptif est sauté et consigné |
| Délai externe de 270 min | TERM converti en arrêt consigné, KILL 5 min après |
| Toute exception | `arret.json` (motif, étape, plans faits), résultats partiels poussés |
| Fin | l'instance s'arrête par son identifiant (R10), consigné dans `registres/arrets.md` |

## Contre-lecture

En attente. Sous-agent neuf à désigner ; il lit les fichiers listés au rapport de rédaction (`brouillons/pilote-exposant-p-v1/rapport-redaction-pilote-exposant-p-v1.md`, section « Pour le contre-lecteur »). Empreinte du brouillon relu : <<EMPREINTE_BROUILLON_RELU>> ; rapport : <<CHEMIN_ET_EMPREINTE_DU_RAPPORT>> ; traitement de chaque remarque : <<TRAITEMENT_DES_REMARQUES>>.
