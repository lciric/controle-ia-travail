# Contre-lecture de l'antériorité du « bras d'attaque informé » — brouillon 1

- **Date** : 10 novembre 2026, lecture entre 09 h 40 et 10 h 10 (temps universel coordonné).
- **Nature** : contre-lecture R2 par un sous-agent neuf (Claude, Opus 5.5). Je n'ai écrit ni la note, ni le bras d'attaque, ni aucune des pièces relues. Lecture seule : aucun commit, aucune commande git qui écrit, aucune dépense ; seul ce fichier est écrit, sans compagnon.
- **Réserve de famille** : la note demandait de préférence un lecteur d'une autre famille de modèles ; je suis de la même famille que son rédacteur. Mes concordances ne valent pas confirmation indépendante (R2, R13).
- **Jamais ouverts** : `donnees/*`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, tout `diag/*/lecture-sondes-t06.json`, tout résultat de sonde ou de moniteur du programme, les épisodes d'épreuve, les items de l'étiqueteur, `registres/decisions.md` (pas ouvert du tout), `runs/20261110-093836-bras-verdicts-v1/`, les autres pièces du commit `5b604ce5` hors de l'objet.

## Fichiers lus et empreintes

| Pièce | Empreinte sha256 | Contrôle |
|---|---|---|
| Objet : `docs/notes/anteriorite-bras-informe-v1/anteriorite-bras-informe-v1-brouillon1.md` | `f18d295e23db8beb611c0736d218a93b6b281356e5dc84c0775a33029e305996` | égale à l'attendu et au compagnon ; lue en entier (380 lignes) |
| 14 PDF versés, N1 à N14 (`docs/sources/pdf/anteriorite-bras-informe-v1/`) | celles du §0.4 de la note | 14 sur 14 : empreinte égale au compagnon **et** à la valeur imprimée ; en-tête `%PDF` |
| 29 fichiers E1 à E27 (`docs/sources/pdf/…`, E4 et E11 en deux fichiers chacun) | celles du §0.5 de la note | 29 sur 29 égales au compagnon et à la valeur imprimée |
| E28, soumission 36008, branche `origin/canal/conv-audit-n04` (commit `adc1be82…`) | `5d4ca052bce4cbe02d5d9eb262c7fd4f18dd746139a8453599b02d494648ed50` | extraite en lecture par `git show` vers le bloc-notes ; égale au compagnon de la branche et à la note |
| 16 notes du programme (table §0.1 de la note) | celles de la note | 16 sur 16 : chemin présent, empreinte égale à la note et au compagnon |
| Constitutional Classifiers++, `docs/sources/pdf/anteriorite-P-041-v1/2601.04603v1.pdf` (au dépôt, non cité par la note) | `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` | égale au compagnon ; lu p. 1, 2, 5, 7–10 |
| 2609.05797v3 (Karne), **copie de contre-lecture dans le bloc-notes, non versée** | `eb7be6cafe32808623e11ab7d3f94f232a8bdff5eebf8d449f1f47e3a598d178` | téléchargé depuis arxiv.org, en-tête `%PDF`, lu p. 1 |
| 2602.00750v2 (Rahman, Alouani), **copie de contre-lecture, non versée** | `cf0bd3653fdc8a1f83b45fe45a77ca806a6ac0c7e673aa55c05960f31e209bf7` | idem, lu p. 1 |
| Autres pages relues pour juger les verdicts | N8 `677fe278…` (p. 1, 6, 7, 18, 20) ; N12 `2d95945b…` (p. 1, 2, 4, 6, 8) ; E23 `f656c9b7…` (p. 2, 7, 8, 13, 20, 21) ; E8 `c4a36db5…` (p. 9–13) ; E7 `f6547ec8…` (p. 1–12, recherche) ; E9 `3b8158a5…` (p. 1–20, recherche) ; N1 `c0f7b6d7…` (p. 3–9, recherche) ; E4 `9c23a613…` (p. 26) ; E11 v4 `8d3ada9a…` (119 p., recherche) | — |

Scripts et sorties de contrôle, non versionnés : bloc-notes de session, `…/scratchpad/scripts/` (`verif_empreintes.py`, `extraire_citations.py`, `verif_citations.py`, `arxiv_q.py`, `arxiv_ids.py`, `compte.sh`) et `…/scratchpad/{citations.json, resultats_citations.json, tirage.json, arxiv/, s2/, pdf-neufs/}`.

---

## Verdict

**Non scellable en l'état : deux bloquants (CA-1, CA-2), tous deux corrigibles dans un brouillon 2 ; texte proposé ci-dessous.** Les citations sont exactes (92 sur 92 à la page indiquée) ; ce sont deux lectures de sources qui faussent les verdicts A1, A2 et A3.

Décompte : 2 bloquants, 5 à corriger, 8 à préciser.

---

## 1. Citations

### 1.1 Méthode

- **Population** : les 92 citations de la note rattachées à une page (« p. N : « … » »), dans l'ordre d'apparition (lignes 137 à 318). Les titres, lieux de publication et citations de notes du programme sont contrôlés à part (§1.4, §3).
- **Vérificateur écrit par moi**, indépendant de celui du rédacteur (non versionné, donc invisible) : `pdftotext -f P -l P` sur la seule page indiquée, en trois modes (défaut, `-raw`, `-layout`) ; correspondance « exacte » à l'espacement près, sinon « normalisée » : apostrophes et guillemets typographiques, ligatures, tirets, césure de fin de ligne (recollée ou gardée). Aucune tolérance sur les mots, les chiffres ni la casse.
- **Épreuve du vérificateur (R5)** : six altérations refusées (un chiffre, un mot, la casse, un chiffre tronqué, la bonne citation sur une mauvaise page, une citation de la v1 cherchée dans la v4) ; deux témoins sains acceptés.
- **Tirage** : `numpy` 2.4.6 (environnement `.venv` du dépôt), `rng = numpy.random.default_rng(numpy.random.SeedSequence(20261110))`, `rng.choice(92, size=25, replace=False)`, indices triés : **3, 4, 10, 14, 16, 19, 21, 24, 39, 40, 43, 46, 48, 52, 54, 57, 58, 65, 71, 72, 79, 83, 87, 90, 91**. Pour chacun, le contexte de la page a été lu pour juger aussi la fidélité du sens.

### 1.2 Les 25 citations tirées

| Indice | Ligne | Pièce | Page | Début de la citation | Sur la page ? | Sens |
|---|---|---|---|---|---|---|
| 3 | 138 | E2 | 1 | « reduced but persistent vulnerabilities… » | oui, mot pour mot | fidèle |
| 4 | 138 | E2 | 3 | « GPT-5 achieves high failure rates… » | oui, à la normalisation près (césure gardée, mode `-raw`) | fidèle (légende du tableau 1) |
| 10 | 140 | N3 | 1 | « In simple tasks, this level of control… » | oui, mot pour mot | fidèle |
| 14 | 142 | E3 | 2 | « We find that although current models… » | oui, mot pour mot | fidèle |
| 16 | 143 | E7 | 1 | « (ii) Obfuscated policy: … » | oui, mot pour mot | fidèle ; coupée avant le procédé, conformément à la règle de la note |
| 19 | 144 | N1 | 12 | « Our study focuses on only a single model… » | oui, mot pour mot | fidèle |
| 21 | 146 | E13 | 1 | « Linear probes, a model-internals approach… » | oui, mot pour mot | fidèle |
| 24 | 148 | E14 | 26 | « There's no particular reason to think… » | oui, à la normalisation près (apostrophe) | fidèle |
| 39 | 172 | N2 | 1 | « even with execution and monitor feedback… » | oui, mot pour mot | fidèle |
| 40 | 173 | E16 | 1 | « the success rate of model tampering attacks… » | oui, mot pour mot | fidèle |
| 43 | 190 | E11 v4 | 10 | « The probes outperformed every action-only text monitor » | oui, mot pour mot | fidèle |
| 46 | 192 | N8 | 1 | « the resulting outputs evade output-side detection… » | oui, mot pour mot | citation fidèle, mais la même page contredit la lecture que la note fait de N8 (CA-1) |
| 48 | 193 | N1 | 4 | « The naive approach one might take… » | oui, mot pour mot | fidèle |
| 52 | 210 | E4 | 9 | « This also means that an attacker does not necessarily need… » | oui, mot pour mot | fidèle |
| 54 | 212 | E6 | 1 | « the model successfully evades previously unseen safety monitors. » | oui, mot pour mot | fidèle |
| 57 | 215 | E28 | 8 | « The probe-targeted attack defeats its target but does not transfer. » | oui, mot pour mot | fidèle (le contexte parle du moniteur structurel et d'une sonde des couches tardives) |
| 58 | 216 | N7 | 1 | « introduce a hierarchy of such classes… » | oui, mot pour mot | fidèle |
| 65 | 242 | E15 | 16 | « This can be done by selecting alternate models… » | oui, mot pour mot | fidèle |
| 71 | 247 | N10 | 1 | « adds agents who receive the collusion instruction… » | oui, mot pour mot | fidèle |
| 72 | 247 | N10 | 1 | « We turn the controls into a protocol… » | oui, mot pour mot | fidèle |
| 79 | 269 | E18 | 1 | « No single monitor is robust to both » | oui, mot pour mot | fidèle |
| 83 | 272 | E20 | 1 | « we propose a lightweight sequential monitoring framework… » | oui, mot pour mot | fidèle |
| 87 | 275 | E23 | 1 | « text-level defenses miss covert attacks… » | oui, mot pour mot | fidèle |
| 90 | 299 | E27 | 1 | « Agents are evaluated on their ability… » | oui, mot pour mot | fidèle |
| 91 | 318 | E11 v1 | 1 | « Our probes achieve 98.8% AUC in SHADE-Arena… » | oui, mot pour mot | fidèle |

**25 sur 25 présentes sur la page indiquée.**

### 1.3 Au-delà du tirage

Les 92 citations ont toutes été passées au même vérificateur : **92 sur 92 présentes sur la page indiquée**, 82 mot pour mot (à l'espacement près), 10 à la normalisation près — 8 apostrophes ou guillemets typographiques, 1 ligature (E15 p. 17), 1 césure de fin de ligne (E2 p. 3). Aucune ne diffère d'un mot ni d'un chiffre.

### 1.4 Mentions d'identité, de lieu et de lecture (contrôlées, toutes exactes)

Dates et versions des N1 à N14 (tampon arXiv de la p. 1) ; pied « NeurIPS 2026 » de N1 p. 1 ; ICML (43e conférence) imprimé sur E7 p. 1 ; « Transactions on Machine Learning Research (07/2025) » sur E16 p. 1 ; E4 v2 du 8 février 2025 ; E11 v1 sous un autre titre ; N13 en v3 du 4 novembre 2026, le dépôt n'ayant que la v2 ; nombres de pages (N7 82, N9 70, N13 84, E11 v4 119) ; N4 « ten open-weight models … from 9B to 32B » (p. 1) ; N14 p. 2 (moniteur = grand modèle de langage, figure 2) ; E17 « distributed threat setting » (p. 1, la note ne donne pas la page) ; E4 p. 26 (coût en pas de gradient et en temps). Les affirmations « rien trouvé » contrôlées par recherche plein texte tiennent : FIBS v4 (aucune expérience d'évasion ; aucune analyse conjointe des erreurs), N13 (aucune sonde d'activations), N2 et E18 (aucune), E19 (« boîte blanche » = accès de l'équipe rouge au moniteur textuel), N1 (l'évasion « sémantique » est suivie par la sonde du modèle de base, p. 4, pas par un juge ; le transfert de la p. 7 est entre juges), E7 (pas de juge textuel sur les politiques évasives), E8 (les attaques « adaptatives » ne visaient ni la sonde ni le classifieur, p. 10).

---

## 2. Points de contre-lecture

### CA-1 — **bloquant** — N8 (MIRAGE) est mal lu ; A1, A2 et A3 en dépendent

- **Où** : §4, ligne 192 (« l'attaque n'est pas adaptée à la sonde ») ; §2, ligne 152 (« Mesuré par qui ? … **personne** ») ; §2, ligne 154 (contre-indices R4) ; §3 (N8 absent) ; §5, ligne 225 (« sans attaque ») ; §10 point 5 (N8 lu en p. 1 seulement).
- **Pourquoi** : la page 1 de N8, que la note cite, dit : « Across all tested adversarial budgets, every attack suppressing the subspace also destroyed encoding fidelity » (N8 p. 1, `677fe278…`). La section « Probe-Aware Adversaries on the Evaluated Budgets » (p. 7) évalue quatre modèles d'attaquant contre la même sonde « across the white-box-to-black-box spectrum (Table 7) », avec le succès compté seulement si la sonde est éteinte **et** le contenu exfiltré récupérable : « On the budgets we tested, no configuration simultaneously suppressed the encoding-subspace activation and produced a recoverable encoded output. » (p. 7). L'un de ces attaquants est sans gradient et agit sur le contenu : « A probe-aware attacker may not have access to gradients but can freely mutate the injection prompt. » (p. 18), dans un cadre d'agent sous injection indirecte (p. 20). N8 réunit donc : attaquant qui connaît la sonde, sans gradient, par le contenu, contre une sonde, dommage vérifié, cadre d'agent — et il **échoue** aux budgets éprouvés. C'est le voisin le plus proche de A1, une seconde occupation de la forme de A2 (plus proche que E3 : dommage vérifié et cadre d'agent), et un contre-indice de signe « pas d'évasion par le contenu » à ranger avec N4 et E3 (R4).
- **Correction proposée** :
  - Tableau A1, ligne à ajouter : « N8 (Revankar et collègues) | p. 1 : « Across all tested adversarial budgets, every attack suppressing the subspace also destroyed encoding fidelity » ; p. 18 : « A probe-aware attacker may not have access to gradients but can freely mutate the injection prompt. » | adversaires qui connaissent la sonde, dont un sans gradient agissant sur le contenu de la consigne injectée, contre une sonde fixe, dans un cadre d'exfiltration par un agent ; dommage vérifié (sortie encodée récupérable) ; aucune évasion aux budgets éprouvés (p. 7, tableau 7) | l'attaquant est un injecteur externe, pas l'agent qui choisit ses propres actions ; un seul dommage (exfiltration encodée) ; la sonde lit un calcul (l'encodage), pas une intention ».
  - « Mesuré par qui ? », texte de remplacement : « Revankar et collègues (N8) mesurent, dans un cadre d'exfiltration par un agent sous injection, des adversaires qui connaissent la sonde, dont un sans gradient qui agit sur le contenu, avec dommage vérifié : aucune évasion aux budgets éprouvés (p. 1, 7, 18). Dans ce corpus, personne ne mesure un attaquant qui **est** l'agent surveillé et choisit le contenu de ses propres actions contre des sondes gelées, sur un sabotage autre que l'exfiltration encodée. »
  - Contre-indices R4 de A1 : « N4, E3 **et N8** (pas d'évasion en contexte ou par le contenu) contre N3 et E2 (évasion partielle) ».
  - Tableau A2, ligne à ajouter : « N8 | p. 7 : « On the budgets we tested, no configuration simultaneously suppressed the encoding-subspace activation and produced a recoverable encoded output. » | quatre modèles d'attaquant contre la même sonde, de la boîte blanche à la boîte noire, par budget, succès exigeant le dommage | pas d'échelon réglage des poids ni renforcement ; forme des budgets à lire p. 18–20 ; attaquant injecteur ».
  - Verdicts : voir §4 ci-dessous. Le §8 (correction de l'état de l'art v1, l. 154) doit aussi citer N8 du côté qui **soutient** la ligne 154 (R4).
  - Lire N8 au-delà de la p. 1 (au moins p. 6–7, 13, 18–20) avant le brouillon 2, sans reproduire le catalogue d'attaques de la p. 13.

### CA-2 — **bloquant** — A3 « libre » : la recherche du contraire a manqué des voisins directs, dont un au dépôt ; la raison donnée est fausse

- **Où** : §1, ligne 120 ; §4, lignes 183–198.
- **Pourquoi** : la note justifie « libre » par « des mesures conjointes existent sans attaquant adaptatif ». Or :
  - **Constitutional Classifiers++** (2601.04603v1, `ba8ec657…`, au dépôt sous `docs/sources/pdf/anteriorite-P-041-v1/`, déjà rangé par la note P-041 « lecteur neuf », ligne 169, que la note dit avoir consultée) mesure la dépendance des erreurs entre une sonde et un classifieur textuel sur des contournements produits par des équipes rouges humaines : « We assess robustness using a dataset of jailbreaks collected from human redteaming, comprising approximately 7,000 exchanges » (p. 7) ; « Probes and external classifiers make more independent errors than pairs of external classifiers. » (p. 8, figure 3b) ; « we analyze the correlations between classifier predictions on our red-teaming exchange dataset (Figure 3b) » (p. 9). La cascade sonde + classifieur textuel a ensuite été éprouvée par une équipe rouge humaine adaptative : « Through extensive red-teaming comprising over 1,700 hours » (p. 1 ; détail p. 9).
  - **2609.05797v3** (Karne, non versé ; copie de contre-lecture `eb7be6ca…`) mesure sur les mêmes requêtes gardes textuels **et** sondes face à une réécriture du contenu dont l'intention est gardée et vérifiée : « Across four text guards, two activation probes, and Latent Guard » ; « Model and monitors miss the same prompts, and stacking monitors does not recover them. » (p. 1). Signe **contraire** à Constitutional Classifiers++ et à N8.
  - **N8** (CA-1) : sur les mêmes scénarios, la détection de sortie est trompée par l'encodage et la sonde ne l'est pas (p. 1), puis des adversaires qui connaissent la sonde échouent (p. 7).
  - La grandeur conditionnelle exacte de A3 (la sonde reste-t-elle muette **sachant** le moniteur textuel trompé, sous un attaquant informé des deux familles, sur un sabotage d'agent) n'est trouvée nulle part, ni par la note ni par moi. Mais la question qu'elle tranche est publiée, sous attaques génériques, avec des signes contraires : c'est la définition d'une revendication **voisine**, pas libre (R8 : zone séduisante, vérifiée plus durement).
- **Correction proposée** :
  - Tableau A3, lignes à ajouter : Constitutional Classifiers++ (citations ci-dessus ; « dépendance des erreurs sonde / classifieur textuel sur contournements d'équipes rouges ; cascade éprouvée par équipe rouge adaptative | pas de grandeur conditionnelle ; contournements, pas sabotage d'agent ; attaquant non informé de la conception des deux familles ») et 2609.05797 (« gardes textuels et sondes manquent les mêmes requêtes sous réécriture à intention gardée | attaque générique ; requêtes, pas sabotage d'agent ; **signe contraire** »), après versement et scellement du PDF.
  - Ligne N8, texte de remplacement : « sur les mêmes scénarios, la détection de sortie est trompée (p. 1) et la sonde ne l'est pas ; des adversaires qui connaissent la sonde échouent aux budgets éprouvés (p. 7) | l'attaque qui trompe le texte n'est pas adaptée au moniteur textuel ; pas de grandeur conditionnelle explicite ; attaquant injecteur ».
  - Verdict A3, texte de remplacement : « **Verdict A3 : voisine** (libre au sens étroit seulement). Raison : la question « la sonde se tait-elle quand le texte est trompé ? » est publiée sous attaques génériques, avec des signes contraires (2609.05797 : les mêmes requêtes échappent aux deux familles ; 2601.04603, N8, N12 : erreurs plutôt indépendantes) ; la probabilité conditionnelle sous un attaquant informé des deux familles, sur un sabotage d'agent, n'est pas trouvée. Ces contre-indices de signes opposés se citent ensemble (R4). »
  - Requêtes à ajouter à l'annexe A (celles qui ont fait sortir ces voisins) : `abs:probe AND abs:ensemble AND abs:classifier AND abs:jailbreak` ; graphe des citants de 2601.04603 ; `abs:"probe evasion" OR …` (voir §5).

### CA-3 — à corriger — A4-b : N8 et N12 ne sont pas « sans attaque » ; le sens faible du transfert est publié, avec des signes contraires

- **Où** : §5, ligne 225 (« E11, N6, N8 | voir A3 | mêmes éléments lus par les deux familles, **sans** attaque ») ; ligne 229.
- **Pourquoi** : l'encodage de N8 est une attaque conçue contre la détection textuelle (p. 1) ; N12 mesure des stratégies d'évasion visant les détecteurs textuels : « Text-level detectors degrade under several encodings; CIFT remains stable in this controlled setting » (N12 p. 6, `2d95945b…`) ; E9 part de charges qui échappent à l'analyse du texte (p. 1). Dans ces trois travaux, une attaque générique contre le texte **ne transfère pas** aux activations. 2609.05797 (p. 1) montre l'inverse : une réécriture du contenu trompe gardes textuels et sondes à la fois. Aucune attaque **adaptée** à une famille et mesurée sur l'autre n'est trouvée : le « libre » strict tient.
- **Correction proposée** : remplacer la ligne 225 par « N8 (p. 1), N12 (p. 6), E9 (p. 1) | attaques génériques conçues contre la détection textuelle, lues par des sondes qui ne sont pas trompées : transfert texte → activations **nul**, au sens faible ; 2609.05797 (p. 1) : réécriture qui trompe gardes textuels et sondes : transfert **positif**, au sens faible ; signes contraires, à citer ensemble (R4) » ; verdict « A4-b : **libre au sens strict** (attaque adaptée à une famille, mesurée sur l'autre), **voisine au sens faible** ».

### CA-4 — à corriger — A1 : antécédent de N3 et N4 omis

- **Où** : §2, ligne 131 et tableau A1.
- **Pourquoi** : l'audit littérature (`29b32f62…`, ligne 76, faille D3) cite, à côté de N3 et N4, Ji-An, Xiong, Wilson, Mattar et Benna 2025, arXiv 2505.13763v2, publié à NeurIPS 2025 selon l'audit (« vérifié p. 1 et p. 5 ») : le paradigme de neurorétroaction en contexte dont N4 est la suite, qui pose explicitement le risque d'évasion de la surveillance par activations (résumé). Son PDF figure dans `docs/notes/audit-controle-v1/sha256-pdf-v1.txt` (`b878d094…`) mais pas sous `docs/sources/pdf/`.
- **Correction proposée** : verser et sceller 2505.13763v2, le citer dans le tableau A1 comme antécédent publié de N3 et N4 (contrôle des activations en contexte, sans gradient), page à relire avant tout chiffre.

### CA-5 — à corriger — A5 : la transposition du témoin planté à l'évaluation de grands modèles existe déjà (pour l'élicitation)

- **Où** : §6, ligne 255 (« Non trouvé : leur emploi conjoint pour borner la force d'un attaquant dans l'évaluation de moniteurs de grands modèles »).
- **Pourquoi** : Greenblatt, Roger, Krasheninnikov et Krueger 2024 (2405.19550, « Stress-Testing Capability Elicitation With Password-Locked Models ») et Hofstätter et collègues 2025 (2502.02180, « The Elicitation Game ») plantent des capacités cachées pour éprouver la force des méthodes d'élicitation : même logique que A5, appliquée aux grands modèles, mais à l'élicitation de capacités, pas à l'évasion de moniteurs (résumés seulement, non opposables). Le verdict « voisine » tient ; la phrase « méthode publiée en apprentissage adverse » est incomplète.
- **Correction proposée** : verser et lire les deux PDF ; ajouter au tableau A5 « témoin planté de la force d'élicitation, en évaluation de grands modèles | pas de moniteur ; pas de nul « honnête contre honnête » » ; réécrire la raison : « publiée en apprentissage adverse (N5, E15) **et en élicitation de capacités des grands modèles (2405.19550, 2502.02180)** ; non trouvée pour borner la force d'un attaquant de moniteurs ».

### CA-6 — à corriger — les énoncés A1 à A6 ne sont ni reproduits ni sourcés

- **Où** : en-tête (« énoncés de la demande ») ; §1 ; §3.
- **Pourquoi** : la note juge six revendications dont elle ne donne que des résumés d'une ligne ; les « cinq régimes d'accès » de A2 ne sont jamais listés, alors que le verdict A2 compte les échelons de E3 « quatre sur cinq ». Un lecteur ne peut pas confronter un verdict à l'énoncé jugé ; une note d'antériorité scellée doit figer son objet (R1, R6).
- **Correction proposée** : ajouter un §0.0 « Énoncés jugés », mot pour mot, avec le chemin et l'empreinte du fichier source (ou, s'ils ne viennent que de la demande, la mention « transmis par la demande du 10 novembre, reproduits sans modification ») ; lister les cinq échelons de A2 et, dans le tableau A2, l'échelon de chaque condition de E3 et de N8.

### CA-7 — à corriger — un paramètre d'une évasion publiée, contraire à la règle de la note

- **Où** : §3, ligne 166, citation de E3 p. 23.
- **Pourquoi** : la citation donne un paramètre chiffré de l'évasion en contexte publiée par E3 et un élément de son procédé ; la note s'interdit tout paramètre d'attaque (ligne 7) et la citation n'est utile que pour établir l'existence d'un témoin.
- **Correction proposée** : remplacer la citation par « p. 23 : témoin « sans démonstration », qui retire les démonstrations et garde la seule consigne finale » (paraphrase sans chiffre), ou couper la citation après « triggered by the instruction alone ».

### CA-8 — à préciser — E3 compte trois régimes et un témoin, pas quatre échelons

- **Où** : §3, ligne 166 (« **quatre sur cinq** ») et ligne 177 ; la note écrit elle-même ligne 160 que le rapport lot3-Cc « en a tiré les trois régimes ».
- **Pourquoi** : le rapport lot3-Cc (`d8c7be40…`, ligne 44) décrit trois régimes : contexte seul avec verdicts binaires, écriture dans les activations, réglage fin à travers des sondes gelées. La condition « sans démonstration » (p. 23) est un témoin de ce premier régime, pas un régime d'accès.
- **Correction proposée** : « trois régimes (contexte avec verdicts binaires, dose selon leur nombre ; écriture dans les activations ; réglage fin à travers des sondes gelées) et un témoin sans démonstration » ; ne compter les échelons qu'une fois CA-6 fait.

### CA-9 — à préciser — HC5 : « revendicable » seulement au sens fort

- **Où** : §4, ligne 183 (« le « quorum par type d'accès » reste revendicable »).
- **Pourquoi** : `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (`c5465a9b…`) dit « Reste revendicable : le quorum par type d'accès au sens fort (juges génératifs et sondes lisant l'agent) » et range DeceptGuard (2603.13791) en « occupe en partie, au sens faible » (ligne 15 ; section HC5, lignes 293–312, dont la ligne 310).
- **Correction proposée** : « section HC5 : le quorum par type d'accès reste revendicable **au sens fort** (sondes lisant l'agent) ; au sens faible, il est occupé en partie par DeceptGuard 2603.13791 ».

### CA-10 — à préciser — citation d'une note du programme à corriger

- **Où** : §4, ligne 183, « E28 « compare seulement » ».
- **Pourquoi** : la note des soumissions (`3793b4c0…`, ligne 34) écrit « **comparé seulement** ».
- **Correction proposée** : « comparé seulement ».

### CA-11 — à préciser — autres voisins à verser ou à mentionner

- **A2 et A4-a** : 2602.00750v2 (copie de contre-lecture `cf0bd365…`, p. 1) : « we demonstrate that these detectors are not robust to adaptive adversaries » ; une attaque optimisée par gradient trompe à la fois toutes les sondes de dérive par couche « while preserving the effectiveness of the underlying injection » — échelon « gradient » avec dommage préservé, transfert entre sondes. ProbeFool (soumission 46803, citée par la note seulement en A4) : attaquant qui n'a que la décision de la sonde (note des soumissions, §1.3), échelon de A2.
- **A1** : 2603.25861 (résumé seulement) : évasion de sondes de tromperie qui émerge d'un entraînement à raisonnement cohérent, sans intention de cacher.
- **A3** : 2609.19101 (résumé : analyse des cas vus par la sonde et manqués par le moniteur textuel, hors attaque) ; 2611.00386 (résumé : dépendance entre décisions de garde-fous empilés, boîte noire) ; ESLD 2605.18918 et DeceptGuard 2603.13791 (au dépôt, déjà lus par le niveau 2, côté détection).
- **A6** : E23 contient une analyse d'évasion **simulée** de la sonde en plusieurs tours (suppression de la dérive des activations à dose croissante, section M, p. 7 et 20–21), mais « Robustness evaluation (section M) simulates drift suppression but does not test probe-aware generation. » (p. 8). C'est le plus proche, dans le corpus, d'un attaquant diffus qui connaît la sonde ; la ligne E23 du tableau A6 (« attaquant non adaptatif ») doit le dire. Le verdict « voisine » tient.

### CA-12 — à préciser — statut du brouillon

- **Où** : en-tête, ligne 5 (« **non scellé** »).
- **Pourquoi** : le fichier a un compagnon `.sha256` et le commit `5b604ce5` le dit « scellé ». Le mot désigne ici deux choses : empreinte posée (R6) et validation.
- **Correction proposée** : « brouillon empreinté (compagnon `.sha256`), **non validé**, ne fait pas foi ».

### CA-13 — à préciser — exposition signalée au §0.6

- **Où** : §0.6, ligne 110.
- **Pourquoi** : le rédacteur dit avoir lu l'en-tête d'un fichier qui nomme des modes de sabotage du programme ; je n'ai pas ouvert ce fichier (interdit) et ne peux pas vérifier ce qu'il contient. Je n'ai trouvé dans la note aucun passage qui ressemble à un mode de sabotage propre au programme ; ceux qu'elle nomme viennent des articles publiés.
- **Correction proposée** : consigner l'exposition dans les registres (qui, quoi, quand), au regard de la N-054 (mode tenu à l'écart), et vérifier que ce dossier n'est pas lisible par les sous-agents de conception.

### CA-14 — à préciser — E28 n'est pas sur la branche principale

- **Où** : §0.5, ligne 104.
- **Pourquoi** : le chemin ne se résout que par `git show` sur `origin/canal/conv-audit-n04` ; une branche peut bouger (R6).
- **Correction proposée** : citer aussi le commit (`adc1be8282a3a8bdf60a5952b4957e52eca2414a`) ou verser une copie scellée sur la branche principale.

### CA-15 — à préciser — la liste des citations contrôlées n'est pas versionnée

- **Où** : §0.3.
- **Pourquoi** : le script et la liste du rédacteur sont restés dans son bloc-notes ; ma vérification indépendante retrouve 92 sur 92, mais un troisième lecteur devra tout refaire.
- **Correction proposée** : verser la liste (pièce, version, page, citation) à côté de la note, scellée.

---

## 3. Faits sur le programme (renvois vérifiés)

| Renvoi de la note | Résultat |
|---|---|
| 16 notes du §0.1 : chemins et empreintes | exacts, compagnons égaux |
| « `docs/notes/anteriorite-P-041-v2/` n'existe pas » ; PDF sous `docs/sources/pdf/anteriorite-P-041-v2/` | exact |
| État de l'art v1, l. 154 | exact ; citation coupée avant « sur les poids (Bailey, Neural Chameleons, RL-Obfuscation) », sans trahir le sens |
| État de l'art v1, l. 82, 91, 92, 108 | exact (Hills et collègues ; adversaire de 2510.09462 ; « Hopman et al. 2025 ») |
| Niveau 2, H1 (identifiants listés, sans attaquant adaptatif), H2 (« occupe en partie » ; « occupe en partie, en boîte noire »), H3 (2607.07368), HC5 (« occupe en partie la matrice de transfert (entre sondes seulement) ») | exact ; HC5 nuancé « au sens fort » (CA-9) |
| Note des soumissions : « trois paliers d'information », 42390 combiné en boîte noire, ProbeFool | exact ; « compare seulement » au lieu de « comparé seulement » (CA-10) |
| Note P-041 v2 : composante 8b (PACE 2606.08106, « Propose, Don't Judge » 2609.27051, REUSE 2609.33180), 263 lignes, §5 point 10 (1902.06705 non lu au-delà de la p. 1) | exact |
| Audit littérature, D3 : 2608.21664 (p. 1, 3, 6), 2610.20179 (p. 1), empreintes égales à N3 et N4 | exact ; la même ligne cite 2505.13763, omis par la note (CA-4) |
| Rapport lot3-Cc : E3 lu en entier, coût de calcul non chiffré | exact ; trois régimes (CA-8) |
| Rapport lot2-A2a : tableau 3 de E8, p. 12 ; lot2-A4 : figure 4 de E1 ; lot2-A2b : évasion partielle par le contenu (2511.00554) | exact |
| Note P-041 « lecteur neuf », « recherche ciblée seulement » | exact, mais elle range Constitutional Classifiers++ (ligne 169) que la note n'a pas repris (CA-2) |

---

## 4. Verdicts par revendication

| Revendication | Verdict de la note | Verdict après contre-lecture | Pièces décisives |
|---|---|---|---|
| A1 | voisine | **voisine, forme occupée en partie par N8** ; reste : l'attaquant qui est l'agent surveillé, des sabotages autres que l'exfiltration encodée, des sondes d'intention | N8 p. 1, 7, 18 (CA-1) ; 2505.13763 (CA-4) |
| A2 | voisine, forme occupée en partie (E3) | **voisine, forme occupée en partie par E3 et N8** ; reste : cinq échelons dont le réglage des poids sur la même famille gelée, l'agent pour attaquant, le coût en requêtes et en calcul | N8 p. 7 ; lot3-Cc ligne 44 (CA-1, CA-8) |
| A3 | libre (vérification moyenne) | **voisine** (libre au sens étroit seulement) | 2601.04603 p. 1, 7–9 ; 2609.05797 p. 1 ; N8 p. 1, 7 ; N12 p. 6 (CA-2) |
| A4 | voisine ; A4-a occupée ; A4-b libre | A4-a **occupée** (confirmé : E4 p. 9, E5 p. 1, E6 p. 1, E3 p. 6, E9 p. 1, E28 p. 8 ; plus 2602.00750) ; A4-b **libre au sens strict, voisine au sens faible** | CA-3, CA-11 |
| A5 | voisine | **voisine** (inchangé), voisins à ajouter | N5, E15 ; 2405.19550, 2502.02180 (CA-5) |
| A6 | voisine | **voisine** (inchangé), E23 section M à mentionner | CA-11 |

Sous-parties occupées : les deux déclarées le sont vraiment (A4-a ; la forme de A2) ; s'y ajoutent la forme de A1 (N8) et, hors moniteurs, la méthode de A5 (N5, E15, et l'élicitation 2405.19550, 2502.02180).

---

## 5. Recherches arXiv neuves

Interface d'export d'arXiv, titres et résumés, tri par date de dépôt décroissante, 60 résultats au plus ; aucune requête ne contient de nom de personne, de programme ou de dépôt. Réponses brutes dans `…/scratchpad/arxiv/`.

| n° | Requête | Résultat utile |
|---|---|---|
| q01 | `abs:probe AND abs:ensemble AND abs:classifier AND abs:jailbreak` | **2601.04603** (Constitutional Classifiers++) — seul résultat ; manqué par la note |
| q02 | `abs:probes AND abs:"LLM judge" AND abs:evade` | N1 seulement |
| q03 | `abs:probes AND abs:"LLM monitor"` | 2609.19101 (sonde contre moniteur textuel, hors attaque) ; 2506.10805 (connu) |
| q04 | `abs:"white-box" AND abs:"black-box" AND abs:monitors AND abs:evade` | 2507.12691 (connu) |
| q05 | `abs:"linear probes" AND abs:"chain-of-thought" AND abs:obfuscat*` | rien |
| q06 | `abs:"reward hacking" AND abs:probe AND abs:judge` | N1 ; 2606.08893 (détection seule) |
| q07 | `abs:transfer AND abs:probes AND abs:"text-based" AND abs:monitor` | rien |
| q08 | `abs:"prompt injection" AND abs:probe AND abs:monitor` | 2610.18408, 2610.02413, 2610.37679, 2611.11172, N12 — détection, aucun attaquant adapté à la sonde |
| q09 | `abs:"independent errors" OR abs:"complementary signals"` | trop large, rien d'utile |
| q10 | `abs:"defense in depth" AND abs:probes` | DeceptGuard, 2606.17478 (connus) |
| q11 | `abs:probes AND abs:"adaptive attacks" AND abs:monitors` | rien de pertinent |
| q12 | `abs:evade AND abs:both AND abs:probe AND abs:monitor` | N8 ; 2606.11063 (sans sonde) |
| q13 | `abs:simultaneously AND abs:evade AND abs:probes` | **2602.00750** (évasion adaptative de plusieurs sondes à la fois) |
| q14–q15 | `abs:"activation-based" AND abs:"text-based" AND abs:monitors` ; `abs:"CoT monitor" AND abs:activations AND abs:evade` | rien |
| q16 | `abs:"optimization pressure" AND abs:"chain-of-thought" AND abs:probes` | 2610.29734 (entraînement à la surveillabilité, hors attaque) |
| q17, q19, q20, q24 | `"obfuscated reward hacking"` × probes ; `"encoded reasoning"` × probes ; `"internal monitors"` × `"external monitors"` ; `"activation steering"` × evade × `"LLM monitor"` | rien de pertinent |
| q18 | `abs:steganography AND abs:"linear probes"` | E9 (connu) ; 2601.22818 |
| q21–q22 | `abs:"password-locked"` ; élicitation × organismes × capacités cachées | **2405.19550**, **2502.02180**, 2608.29458 (A5) |
| q23 | `abs:neurofeedback AND abs:activations` | **2505.13763** (A1), N4 |
| q25–q32 | `"probe-aware"` ; `"probe evasion"` et variantes ; `"monitor-aware"` × probe ; `"self-obfuscation"` ; probes × `"chain-of-thought monitor"` × renforcement ; `"latent monitors"` × `"text monitors"` ; blanc × noir × adaptatif × agent ; probe × exfiltration × adversary | 2603.25861 (A1) ; 2602.00750 ; N8, E9 ; rien d'autre de pertinent |

Graphe des citations (par identifiant arXiv seulement) : les citants de E3 (2609.36490) et de N8 (2606.10304) n'ont pas pu être lus (limitation de débit) ; E2 (2511.00554) : un citant, sans rapport ; Constitutional Classifiers++ : 48 citants, dont **2609.05797** (A3, A4-b) et 2611.00386 (A3) retenus après résumé.

**Ce que ces recherches changent** : pour A3, deux voisins directs (2601.04603, 2609.05797) de signes contraires, plus N8 relu ; pour le transfert texte ↔ activations, aucune attaque **adaptée** à une famille mesurée sur l'autre (le « libre » strict de A4-b tient), mais un sens faible publié avec des signes contraires (2609.05797 contre N8, N12, E9).

---

## 6. Contenu interdit

Balayage de la note entière (procédés, paramètres, déclencheurs, consignes, encodages, budgets, couches, seuils) et lecture des contextes : **aucune recette, aucune description opératoire d'évasion**. Les citations sont coupées avant les procédés (E7 p. 1, N1 p. 5, N8 p. 1 où la note ne reprend pas la liste des encodages, E6 p. 1 où elle ne reprend pas le déclencheur). **Un passage contraire à la règle** : la citation de E3 p. 23 (ligne 166), qui porte un paramètre chiffré et un élément de procédé d'une évasion publiée (CA-7) ; il n'est pas recopié ici. Les nombres de E2 (seuil fixe de la sonde, taux d'échec) et de E4 (itérations de réentraînement du défenseur) sont des résultats ou des réglages de la défense, admissibles. Aucun mode de sabotage propre au programme n'est identifiable dans la note (sous la réserve de CA-13 : je n'ai pas lu la source citée au §0.6).

---

## 7. Ce que je n'ai pas pu vérifier

1. Les énoncés exacts de A1 à A6 et les cinq échelons de A2 : absents de la note (CA-6) ; je n'en ai pas cherché la source, possiblement dans un dossier qui m'est interdit. Mes verdicts portent sur les résumés du §1 de la note.
2. Le contenu du fichier signalé au §0.6 (interdit) et la non-ouverture de `registres/decisions.md` par le rédacteur (déclaration non vérifiable).
3. Les soumissions anonymes à ICLR 2027 au-delà des quatre archivées (OpenReview non interrogé) ; les billets hors arXiv ; les citants de E3, N8, N1, E11 et E28 (limitation de débit ou non interrogés).
4. N8 lu seulement sur les passages cités (p. 1, 6, 7, 18, 20) et par extraction de texte : le tableau 7 n'a pas été relu sur l'image de la page ; Constitutional Classifiers++ lu p. 1, 2, 5, 7–10 (la provenance exacte des 7 000 échanges d'équipes rouges n'est pas précisée p. 7) ; 2609.05797 et 2602.00750 lus en p. 1 sur des copies non versées ; 2405.19550, 2502.02180, 2505.13763, 2603.25861, 2609.19101, 2611.00386 en résumé seulement — **rien de ces lectures n'est opposable avant versement, scellement et lecture des pages (R7)**.
5. La citation « brèches analysées » (ligne 109, `LISEZMOI-v1.md` du collisionneur) : non ouverte.
6. Rien n'a été relu sur l'image des pages ; les figures (E1 figure 4, E3 figure 4a, E8 tableau 3, N8 tableau 7, Constitutional Classifiers++ figure 3) n'ont été lues que par leur texte extrait.
