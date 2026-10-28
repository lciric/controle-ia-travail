# Contre-lecture de la synthèse de l'audit des failles de notre contrôle — rapport — v1

Contre-lecteur : sous-agent neuf de la lignée conv-audit, d'un autre modèle que l'auteur de la synthèse (N-052). Je n'ai
écrit aucune pièce de l'audit. Ouvert le 2026-10-26 à 13:20:26 UTC (heure lue sur `date -u` dans la commande qui écrit ce fichier) ;
l'heure de clôture est en dernière ligne. **Pièce confidentielle** : dépôt privé seulement ; aucun montant, aucun financeur,
aucun nom propre de la page de titre des rapports (hors Lazar) n'y figure, et j'ai vérifié qu'il n'en figure aucun dans la
synthèse (contrôle automatique sur les mots de la page de titre, les motifs de montant et le surnom de l'organisme : zéro
occurrence dans `audit-failles-controle-v1.md` et `LISEZMOI-synthese-v1.md`).

**Objet attaqué.** `fournis/synthese-v1/audit-failles-controle-v1.md` (`1e43b69c…`, 1 128 lignes), sur la v1 du rapport
consolidé (`e066f298…`, 7 pages). La v2 de la synthèse (sur la v2 du rapport, failles E à I) n'est pas couverte ici ;
j'attends le message annoncé.

**Vérifications préalables.** Brief `LISEZMOI-brief-contre-lecture-v1.md` : empreinte conforme. `fournis/` : 117 sur 117
conformes à `EMPREINTES-fournis-v1.txt`. Les 23 PDF (format de document portable) que la synthèse dit avoir relus
(annexe B) : empreintes sur disque conformes aux huit premiers caractères cités, toutes. Script
`calculs-synthese-v1.py` rejoué par `python3 -I` (numpy 2.5.3) : sortie identique octet pour octet à
`calculs-synthese-v1.sortie.txt`. Lectures de pages : `pdftotext -layout`, page physique ; aucune figure lue.

---

## 1. Verdict

**Transmissible après corrections.** Aucun constat bloquant : les chiffres, pages et citations que j'ai refaits (trente
affirmations, section 3) sont conformes, le script est reproductible, la confidentialité est tenue, aucune phrase n'est une
recette contre un moniteur. Sept constats sont **à corriger avant transmission** (CLS-01 à CLS-07) : ils touchent la
gravité annoncée de l'avertissement sur le rapport (trois des « sept formulations » sont des nuances, pas des faussetés),
la formulation « chiffres sans source », une faille candidate (FC-04) dont le remède ne répond pas au mécanisme de sa
propre source, la nature de D-02 (la clause à amender est née à la transcription, pas dans l'option acceptée), la
qualification de la faille de tête (a), une condition absente de D-08, et le format de plusieurs options de décision.
Huit constats mineurs suivent (CLS-08 à CLS-15). Trois angles que la synthèse ne voit pas sont en section 7.

---

## 2. Constats

Gravité : **à corriger avant transmission** ; **mineur**. Lieu : ligne de `audit-failles-controle-v1.md`.

### CLS-01 — à corriger — « Sept formulations ne tiennent pas » : trois sont des nuances, une est à rejustifier (l. 42–75 ; D-01, l. 879–887)

- **Ce qui ne va pas.** L'en-tête de 0.1 met au même rang sept objections ; refaites une à une sur les sources :
  - **1 (« inédites »)** : conforme sur le mot (R8 interdit « inédit ») ; mais pour 2.1, les voisins cités (2601.11516,
    2511.17408, 2509.21344) documentent le **phénomène** (sondes d'énoncés courts qui échouent sur trajectoire), pas le
    **mécanisme** que le rapport propose (rotation sous conscience d'évaluation), qui n'est ni mesuré ni occupé. À écrire :
    « phénomène voisin publié ; mécanisme non mesuré ».
  - **2 (« loi de déférence découverte »)** : l'objection tient par R8, mais la justification vise les pièces de HC1 dans
    les moniteurs (`anteriorite-v1.md`, en tête, point 2 : lecture par probabilité du jeton, destination libre), alors que
    le rapport parle de la loi du projet antérieur (Δv = g·(ĉ − v₀)). Les voisins de cette loi sont ailleurs dans la
    synthèse elle-même (RC-1.6 : Panin, 2602.13568, « The Silent Judge », Venkatesh et al. ; N-023 : destination « cible »
    publiée en qualitatif pour deux familles). Rejustifier avec eux.
  - **4 (« garantie valable à tout instant »)** : nuance, pas fausseté. Le seuil au rang conforme sur le maximum
    trajectoriel borne P(∃ t ≤ T : S_t > τ) ≤ α : la garantie vaut pour toute règle d'arrêt **à l'intérieur de l'horizon
    calibré** ; elle est marginale, comme l'est aussi l'inégalité de Ville. Ce qui manque au rapport, c'est l'horizon,
    l'échangeabilité et la loi conditionnelle au calibrage (brouillon 3 de G1, l. 103, vérifié) ; « ne tient pas » est trop
    fort. À écrire : « à préciser ».
  - **5 (« colmatage » de la classe C)** : nuance. Le rapport (1.2, vérifié sur le texte extrait) n'affirme pas détecter un
    réarrangement non structuré ; il ajoute des détecteurs d'ordre au théorème corrigé. T2 (N-003, vérifié) borne ce que
    ces détecteurs peuvent faire (réarrangement puis rebrassage uniforme : rien) ; T3 les justifie sous dommage structuré.
    À écrire : « à borner par T2 ».
  - **3, 6, 7** : conformes (`anteriorite-v1.md` en tête ; calcul bloc 1 rejoué ; P-014 vérifiée : 12 octobre, 0,968,
    κ 0,17 / 0,04 / 0,07).
- **Correction.** Regrader l'en-tête : « deux formulations fausses ou dépassées (6, 7), deux contraires à R8 (1, 2), trois à
  nuancer (3, 4, 5) » ; D-01 garde sa recommandation (a), son enjeu change de mots.

### CLS-02 — à corriger — « dix-sept chiffres sans source » (l. 76, 355–361, 880, 1054)

- **Ce qui ne va pas.** La table 1.11 dit « sans source **fournie** » ; D-01 (l. 880) dit « sans source », sans le
  qualificatif. Or N-003 (vérifiée, § Sources) nomme `docs/notes/resultats-T0.3-v1.md` (run `20261004-080257-t03`) et
  `docs/notes/note-mathematique-lemme-theoreme-v2.md`, où vivent selon toute vraisemblance 31/31, 342, 544, 17 réglages,
  4,6 %–5,5 % et 17 %. Lazar, qui a le dépôt, lira « sans source » comme faux. Par ailleurs, « q ≈ 0,75 » (rapport 2.2) est
  une valeur illustrative d'un scénario, pas une mesure : elle n'a pas sa place dans la liste.
- **Vérification faite.** Les dix-sept nombres sont bien absents des pièces fournies (recherche par motif sur
  `fournis/`, hors synthèse et rapport : zéro occurrence pertinente).
- **Correction.** Écrire partout « non sourcés dans le rapport (aucun chemin ni empreinte, R6) ; sources probables : … » ;
  retirer « q ≈ 0,75 » (seize chiffres).

### CLS-03 — à corriger — FC-04 : le mécanisme et le remède ne s'accordent pas avec la source (l. 184–186, 189, 556, 682–692, 810, 851)

- **Ce qui ne va pas.** La synthèse écrit « évadable par un adversaire qui connaît sa dérive et son seuil » et propose
  « paramètres de dérive et seuils tirés au hasard par épisode ». 2601.20022v2 (vérifié p. 1–3) dit autre chose : la
  covertness est obtenue en choisissant une loi après rupture **qui converge vers la loi avant rupture** quand γ croît
  (divergence de Kullback-Leibler qui tend vers zéro) ; elle est définie comme « the best achievable ADD, under the
  constraint that AT2FA is at least γ, grows as Θ(γ) » (p. 2–3) : une borne pour **tout** détecteur, la somme cumulée étant
  optimale au sens classique. La connaissance de γ sert à dimensionner le décalage, pas à exploiter κ ; tirer κ ou le
  seuil au hasard ne déplace pas une borne d'information.
- **Conséquence.** FC-04 n'est pas une faille propre à la somme cumulée : c'est la forme « petit décalage par pas » de la
  dilution de RC-1.3, déjà portée par FI-04 (budget de détectabilité par unité de dommage). Le remède « tirage au hasard »
  (aussi en section 6, n° 10) est non fondé ; « borne de B total » et dose mesurée dans l'espace de la tâche (D-03) restent.
- **Correction.** Reformuler FC-04 : « un adversaire qui réduit son décalage par pas impose un délai Θ(γ) à tout
  détecteur (2601.20022v2, p. 1–3) : la sécurité « avant le dommage » n'est énonçable que sous κ ≥ κ_min (FI-04, D-03) » ;
  retirer le tirage au hasard des remèdes ; garder 2005.07821 comme voisin de « attaques sous seuil en systèmes
  physiques ».

### CLS-04 — à corriger — D-02 : la clause « lecture principale » n'est pas dans l'option acceptée (l. 80–82, 98, 587–588, 889–899, 979–980)

- **Ce qui ne va pas.** La synthèse présente D-02 comme un « amendement de la lecture principale de N-053 ». Or la
  proposition 1 de session-depot, option (a) acceptée (`audit-litterature-session-depot-v1.md`, § (c), l. 165–174,
  vérifié), dit : « deux bras **rapportés, qui ne servent pas de critère** ». La phrase « la lecture filtrée est la lecture
  principale de toute revendication d'« intention » » apparaît à la transcription (`faits-audit-controle-v1.md`, F3,
  énoncé 1, l. 622–626, vérifié), dans un énoncé qui dit en même temps « bras rapportés, qui ne servent pas de critère ».
  Le mot de Lazar est « accepté » sur les cinq propositions, donc sur l'option (a) telle qu'écrite.
- **Conséquence.** D-02 n'amende pas une décision de Lazar : il demande de revenir au texte accepté et de corriger une
  transcription ; c'est un cas concret pour D-11 (confirmation sur empreinte), que la synthèse cite sans le relier.
- **Correction.** Dans l'enjeu de D-02 et dans 0.2, écrire : « la clause « lecture principale » est née à la transcription
  (N-047, devenue N-053) ; l'option acceptée fait du bras filtré un bras rapporté » ; dans D-11, citer ce cas.

### CLS-05 — à corriger — faille de tête (a) : candidate bien appuyée, non établie sur notre système ; « outil le moins sûr » dépasse la source (l. 80–82, 583–588, 891–893)

- **Ce qui ne va pas.** (1) 2509.21344v2 § 7.3 (vérifié p. 8) dit, après la phrase citée, que le filtrage par scores reste
  « a cheap and accessible method that … could provide researchers with important evidence » ; § 7.1 (p. 8) ajoute que le
  réglage fin étroit des organismes « could partly explain poor probe performance ». « L'outil que la source juge le moins
  sûr » est donc une lecture dure. (2) Sur nos pièces, P3 est ambigu et la synthèse ne le dit pas ici : le plancher
  aléatoire à 0,5717 (N-025, vérifié) montre que les activations de (i-a) diffèrent de l'honnête sans séparer indication
  privée et conduite (coût ×33, formes du champ : N-025, remarque 1) ; les sondes génériques ne dépassent pas ce plancher.
- **Ancrage (brief, point 5).** Négation « la sonde ne peut pas lire l'indication privée » : non établie sur nos pièces,
  mais l'affirmation ne l'est pas non plus sur notre système ; elle l'est sur un autre dispositif (2509.21344). La faille
  est candidate, à forte antériorité, et bloque **la revendication telle qu'écrite tant que le contrôle manque** — ce
  que « G1 peut se gagner… » dit déjà, à condition de l'écrire ainsi.
- **Correction.** Écrire « candidate (2509.21344 ; P3 ambigu) ; bloque la revendication « intention » tant que les négatifs
  ne sont pas appariés en indication » ; remplacer « l'outil le moins sûr » par « l'outil dont la source dit qu'il ne voit
  pas la fuite par l'attention et qu'elle juge moins valide que des organismes sans évidence textuelle ».

### CLS-06 — à corriger — D-08 : l'accumulation entre épisodes est exploitable par l'adversaire patient qu'elle vise (l. 950–958 ; FI-15 remède ; section 6, n° 5)

- **Ce qui ne va pas.** Option (a) propose une statistique de scores qui persiste entre épisodes, avec pour voisin le
  macro-protocole de 2411.17693. Vérifié p. 10 : « our approach assumes the untrusted model is memoryless, future work
  could relax this assumption and allow dynamic red-team strategies ». Un adversaire capable de fragmenter entre épisodes
  est, par hypothèse, un adversaire à mémoire : une statistique cumulée ordinaire (somme, produit d'un processus e) se
  laisse **créditer** par des épisodes honnêtes avant l'attaque. La forme classique de Page, C_t = max(0, C_{t−1} + X_t − κ),
  interdit ce crédit par sa remise à zéro ; un maximum courant d'un processus e aussi (référence classique, non relue
  ici, R7).
- **Correction.** Dans D-08 (a) : « statistique non créditable (remise à zéro de Page ou maximum courant), calibrée sur des
  suites d'épisodes honnêtes ; simulation semi-synthétique contre une équipe rouge **à mémoire** ». Dans FI-15 et section
  6 n° 5, dire que le voisin direct n'a été évalué que sans mémoire.

### CLS-07 — à corriger — format des décisions : options sans avantage ni inconvénient (section 8)

- **Ce qui ne va pas.** Le brief demande, pour chaque option, un avantage et un inconvénient. Manquent : D-04 (c), D-06
  (c), D-07 (b) et (c), D-08 (c), D-09 (b) (avantage), D-10 (b), **D-11 (b), option recommandée**, **D-12 (b), option
  recommandée**, D-13 (a), (b), (c), D-15 (c). Les « statu quo » peuvent rester nus ; les options recommandées de D-11 et
  D-12 et les trois de D-13 ne le peuvent pas.
- **Conforme.** Les douze points restants de F.3 du lot B sont tous repris (FI-01, FI-02 sortis par N-054 ; FI-27 et FI-39
  fusionnés) ; seize décisions ; le bilan des défauts couvre D-01 à D-16 ; les nœuds « sans GO, statu quo » suivent la
  hiérarchie de décision du dépôt (écart déclaré au LISEZMOI, acceptable) ; N-053 et N-054 sont appliquées là où elles
  changent un verdict (FI-01, FI-02, RC-1.5 (2), FC-21, P3b en bras spécialisé, routage de RC-2.1).
- **Correction.** Une ligne par option manquante.

### CLS-08 — mineur — quatre candidates sans leurs cinq parties (l. 773–778)

FC-15, FC-16, FC-18, FC-20 n'ont qu'une ligne de statut et une ligne de grille : ni mécanisme écrit, ni « ce qui tombe »,
ni recherche d'antériorité L1 à L4, ni expérience ; FC-06 et FC-13 n'ont pas de « ce qui tombe ». Le brief de synthèse
(§ 3.3) exigeait les cinq parties pour chaque candidate. Compléter, ou les déclarer « idées du collisionneur, non
instruites ».

### CLS-09 — mineur — numéro de N-053

Les cellules du collisionneur et ses faits appellent la même décision **N-047** (renumérotée N-053 par R-510, LISEZMOI du
collisionneur, l. 6 ; « contenu identique hors numéro »). Le dire une fois (section 0 ou 8) pour que Lazar ne bute pas.

### CLS-10 — mineur — « répulsion d'Onsager » (l. 320–322)

« L'objet connu le plus proche est la correction d'Onsager du passage de messages approché » est une conjecture sans
source ; un autre référent classique est la répulsion logarithmique des valeurs propres des gaz de Coulomb, qui va mieux
avec « spectrale ». S'en tenir à « terme non défini dans le rapport ; à faire définir » (R7).

### CLS-11 — mineur — FI-09, « Dawid et Skene, cité par 2512.03109 p. 14 » (l. 512, 813, 819)

Vérifié : la p. 14 est l'entrée [56] de la bibliographie, rien de plus. Écrire « référence classique, non relue ici », comme
en section 6.

### CLS-12 — mineur — D-02 (a) laisse tomber le remède le plus net de sa source (l. 894–896)

FI-06 (lot B, l. 180–186) propose aussi « un bras boîte noire qui voit le même contexte privé que la sonde et un bras sonde
limité aux positions du transcript public » : plan 2 × 2 information × accès, seul à séparer l'accès interne de
l'information. D-02 (a) ne le reprend pas. Et « G1-P1 établi sur (ii) seul » ignore que (ii), distillée de (i), est elle-même
contestée comme témoin (collisionneur, A3 ter acceptée par T3-B : « (ii) est déclarée indéterminée ; le contrôle se fait
sur (iv) seule ») : renvoyer à D-14.

### CLS-13 — mineur — sûreté (brief, point 4)

Aucune phrase de la synthèse n'est une recette : pas de procédure, de consigne, de réglage ni d'exemple de texte ; les
mécanismes d'attaque cités viennent du rapport ou d'un titre et d'une phrase de la littérature. Les deux phrases les plus
proches de la ligne : l. 282–283 (restitution du point (2) de 2.2 du rapport) et l. 598–600 (« 43,7 % … le bruit honnête est
la couverture du saboteur »). Rien à retirer ; on peut adoucir la seconde en « le bruit honnête borne la détectabilité
(FI-10) ». Le chiffre 43,7 % est conforme à P-015 (vérifié, l. 104).

### CLS-14 — mineur — FC-01 : N-025 ne sépare pas témoin et mention (l. 658–660)

L'intervalle [−0,570 ; −0,065] (N-025, remarque 2, vérifié) porte sur « le témoin et la mention » ensemble. Ancrage : la
négation « le témoin instruit est neutre en conduite » n'est pas exclue par cette pièce pour le témoin seul ; FC-01 reste
candidate, ce que la synthèse dit ; ajouter « effet non séparé ».

### CLS-15 — mineur — FC-02, ancrage

Le mécanisme (Σ mêlée = Σ_intra + p(1 − p)·Δμ Δμᵀ, directions penchées vers Δμ) est exact ; son application à P3 dépend
de l'estimation de Σ, que le rapport ne précise pas (« covariance empirique des activations »). Négation « le plancher
n'est pas relevé » : fausse en général, indécidable pour P3 sur nos pièces. Statut « proposé » conforme ; écrire
« indécidable sans le préenregistrement de P3 (non fourni) ».

---

## 3. Vérifications conformes (exactitude, brief point 1)

Trente affirmations refaites sur la source ; « conforme » sauf mention. Pages lues sur le PDF empreinté (huit premiers
caractères cités par la synthèse, vérifiés sur disque).

| n° | affirmation de la synthèse | source refaite | verdict |
|---|---|---|---|
| 1 | 0,57 contre 0,94 (résumé) ; 0,95 → 0,81, 14 points ; « cannot account for information that leaks … via attention » ; 0,94 → 0,50 ; § 7.3 | 2509.21344v2 p. 1, 5, 8, 9 | conforme ; nuance § 7.3 et § 7.1 (CLS-05) |
| 2 | sélection d'actions inobservable quand l'agent reçoit l'ordre | revue METR d'août, p. 7 | conforme |
| 3 | « no single action is catastrophic … no single action provides overwhelming evidence » | 2411.17693v1 p. 1 | conforme |
| 4 | Θ(γ) contre O(log γ) ; adversaire qui connaît γ | 2601.20022v2 p. 1 | chiffres conformes ; mécanisme et remède : CLS-03 |
| 5 | « aucun verdict occupe en entier » ; HC1, HC5, H2, T, L en partie ; probabilité du jeton publiée ; destination libre partiellement occupée | `anteriorite-v1.md`, en tête | conforme |
| 6 | T2 : réarrangement puis rebrassage = loi honnête ; T3 : garanties locales | N-003 | conforme ; portée : CLS-01 |
| 7 | invariance spectrale : état brut invariant, dictionnaire jusqu'à 6,94 % | bloc 1 rejoué | conforme (sortie identique) |
| 8 | P-014 : 12 octobre, sous-agents, 0,968 ; κ 0,17, 0,04, 0,07 | P-014, lignes de registre | conforme |
| 9 | dix-sept chiffres absents des pièces | recherche par motif sur `fournis/` | conforme ; libellé : CLS-02 |
| 10 | 4,995 % = 50/1001 à α = 5 % ; 0,999 % à 1 % ; simulation visée à 5 % | calcul refait ; rapport 1.1 (« 5 % visé ») | conforme |
| 11 | brouillon 3 de G1 : K ≥ 499 ; 2,9 % et 0,5 % ; ≈ 700 ; ≈ 1 200 ; G1-P4 (≤ 1 %, borne ≤ 2 %) ; G1-P5 ; (i) jamais seule ; 2607.06596 0–94 % ; 2411.17693 hors critère | brouillon 3, l. 42–46, 56–58, 82, 95, 102–106, 114–117 | conforme |
| 12 | calibration conforme sur exécutions entières, alarme au premier franchissement | 2605.06455v2 p. 6 | conforme (budget nominal 10 %) |
| 13 | « similar to conformal procedures » ; tests à deux échantillons ; Dawid et Skene | 2512.03109v2 p. 5, 6, 14 | conforme ; p. 14 = bibliographie (CLS-11) |
| 14 | intitulé Kaur, Padhi et al. | 2604.19775v2 p. 1 | conforme |
| 15 | copule gaussienne AR(1), marges préservées, moniteurs de marges contre de séquence | 2606.10456v2 p. 1–2 | conforme |
| 16 | P3 : 0,5748 ; 0,5717 ; 0,5313 ; ≈ 0,044 contre 0,025–0,037 ; [−0,570 ; −0,065] ; 0,888 ; 0,8878 | N-025, N-029 | conforme |
| 17 | 0,7909 ; q* = 0,97959 = (2p − 0,02)/1,96 ; g′(p) = 0,0188 ; nul seulement en p = 0,5 ; score de compétence 0,15 invariant | bloc 2 rejoué et refait à la main | conforme |
| 18 | d(1, 0) = 4 ; d(y, ½) = 0,6189 ; α = 2 ⇒ 2 × Brier ; dilution 0,8349 / 0,5184 / 0,4868 contre 0,4833 | bloc 3 rejoué et refait à la main | conforme |
| 19 | variance 1,852 contre 1, dépassement 0,0005 contre 0,0100 | bloc 6 rejoué | conforme (contre-exemple valide ; le rapport est implicitement gaussien) |
| 20 | 0,20 et 0,10 ; 3,035 et 3,462 | bloc 5 rejoué | conforme |
| 21 | classifieur en cascade sonde puis modèle de langage | 2601.11516v4 p. 2 | conforme |
| 22 | +0,172 ; 41 % contre 19 % ; huit familles ; « null diagonal bonus » pour un moniteur à consigne fixe ; 18 % contre moins de 2 % ; Llama 1,3 % contre 2,6 %, « inverts » ; 0 à 94 % | 2607.06596v3 p. 2, 13 | conforme |
| 23 | moins de 14 milliards ; Llama-3 8B de 0,36 à 0,72 par couche | 2609.22119v1 p. 1, 13 (table 3) | conforme |
| 24 | ≈ 2 % de faux positifs sur trajectoires bénignes ; auto-préférence variable selon les versions | fiche Mythos p. 109, 100–101 | conforme |
| 25 | sonde moyenne 0,54 ; rappels quasi nuls sauf trois jeux ; rappel moyen 0,10 | 2511.16035v2 p. 9, 10, 54 | conforme |
| 26 | 13,2 → 24,2 % ; 24,5 → 18,6 % ; p = 0,001 et 0,016 ; 30 + 30 ; une seule évaluation ; 8,4 → 13,2 % ; 0,3 → 0,8 % | 2509.15541v1 p. 18, 19, 77, 78, 82 | conforme |
| 27 | causal à 8 milliards sur trois couches, témoins aléatoires nuls ; une couche : marginal ailleurs ; indice « testé » non neutre (21/35 perdent, 14/35 gagnent) | 2606.23583v1 p. 10, 13, 12 (A.8) | conforme (p. 1, 5, 12 relues par moi) |
| 28 | consensus de juges = erreurs corrélées ; cadre d'audit de dépendance | 2604.07650v2 p. 2, 10 | conforme |
| 29 | « turning a blind eye » ; fenêtres fixes et maximum entre fenêtres ; score de compétence de Brier ; blocage d'arêtes d'attention ; attaques sous seuils de chi-deux et somme cumulée ; Ctrl-Z incrimination | 2410.21514v1 p. 5 ; 2604.14865v1 p. 6 ; 2410.14746v1 p. 2 ; 2609.36490v1 p. 8 ; 2005.07821v1 p. 1–2 ; 2504.10374v1 p. 2, 8 | conforme |
| 30 | repère 240 épisodes, ≈ 3,96 dollars, ≈ 0,017 par épisode ; 43,7 % ; 1 200 × 0,017 ≈ 20 | lot B l. 24–25 ; P-015 l. 104, 115–116 | conforme |

Comptages : 47 lignes MD, 26 SD, 11 SD-b, 44 FI, 25 FC (21 + 4), 16 décisions ; aucun « premier », « nouveau » ou
« inédit » affirmatif ; sigles développés.

---

## 4. Justice envers le rapport (brief point 2)

- Les jugements « voisin » sont établis par une page relue dans 23 cas ; les « lu par le lot A » servent surtout dans
  0.1 point 1 (2606.23583 p. 1, 5, 12), que j'ai relus : conformes. Les « ne tient pas » sont regradés en CLS-01.
- « Inédit non trouvé » : l'annexe A consigne deux passes par mots clés anglais sur 175 PDF et 82 fichiers, avec comptes ;
  c'est suffisant pour « non trouvé dans les listes » (R8), pas pour davantage, et la synthèse ne prétend pas davantage.
- **Deux recherches d'antériorité de plus (réseau), consignées.**
  1. **FC-02** (plancher apparié relevé par le contraste des classes). Requête WebSearch : « random direction baseline
     probe activations covariance "random directions" AUROC above chance control baseline linear probe language model ».
     Résultat utile : arXiv 2410.12555, « Investigating Sensitive Directions in GPT-2: An Improved Baseline and
     Comparative Analysis of SAEs », qui propose des directions aléatoires **appariées à la covariance des activations**
     (« cov-random mixture ») comme référence, pour un autre but (sensibilité des perturbations). Lu sur la page de résumé
     arXiv et un résumé de son introduction et de sa section 3, **pas sur le PDF : non opposable (R7), à vérifier**.
     Verdict : voisin de **méthode** du colmatage 1 du rapport (1.4, plancher apparié en covariance), absent de L1 à L4 et
     de RC-1.4 ; FC-02 elle-même (contraste des classes dans Σ) : non trouvée.
  2. **FC-11** (trait ou état). Requête WebSearch : « activation probe detects persistent disposition rather than
     per-action behavior "sleeper agent" probe fires before trigger trait versus state deception probes language
     models ». Résultats : le billet d'Anthropic de 2024 (fiche du lot A, déjà tenue) et 2603.25861 (fiche du lot A).
     Le billet (fiche, section « Why does such a simple method work at all? ») dit que la sonde lit « le fait qu'une invite
     déclenchera la défection », un état de contexte, pas une disposition par action : voisin faible, déjà en L1. FC-11
     reste « non trouvée » ; statut « question » conforme.
- Trois **négations** (brief point 5) : CLS-05 (faille (a)), CLS-14 (FC-01), CLS-15 (FC-02). Aucune des trois affirmations
  n'est établie sur notre système ; la synthèse le dit pour FC-01 et FC-02, pas assez pour (a).

---

## 5. Traçabilité (brief point 3)

- Candidates FC-01 à FC-14, FC-17, FC-19, FC-21 : mécanisme, ce qui tombe, antériorité, remède, expérience présents ;
  FC-03, FC-06, FC-09, FC-13 sans expérience ou sans « ce qui tombe », avec motif ; FC-15, FC-16, FC-18, FC-20 : CLS-08.
- Décisions : format conforme sauf CLS-07 ; F.3 du lot B entièrement repris ; N-053 et N-054 sorties et appliquées
  (CLS-07, « conforme ») ; D-02 change de nature (CLS-04).

---

## 6. Ce que je n'ai pas pu vérifier

- Les relevés « lu par le lot A » et « lu par session-depot » hors ceux listés en section 3 (par exemple 2511.17408,
  2510.13900, 2603.19426) ; les affirmations des cellules du collisionneur (lues, non vérifiées sur source).
- Les dix-sept chiffres du rapport et les affirmations 2.1 à 2.4 (pièces non fournies ; CLS-02 sur le libellé).
- Les références classiques invoquées par la synthèse (section 6) et par moi (remise à zéro de Page, maximum courant,
  répulsion des gaz de Coulomb) : non relues sur PDF (R7).
- 2410.12555 : résumé seulement (section 4).
- La v2 de la synthèse et la v2 du rapport : hors de cette passe.

---

## 7. Ce qui manque (brief point 6)

1. **Règle de combinaison entre modes après N-054.** N-054 rapporte G1 « par mode » (coûts ; affaiblir les contrôles ; mode
   tenu à l'écart). La synthèse ne dit nulle part **comment G1 se prononce** quand les modes divergent (tous ? au moins
   un ? le mode tenu à l'écart décisif ?) ni comment l'erreur est allouée : trois lectures de G1-P1 à 5 % laissées libres
   donnent jusqu'à 1 − 0,95³ ≈ 14 % de franchissements à tort sous le nul (calcul élémentaire). La section 6 n° 24
   (dépense d'alpha) effleure la question sans la rattacher à N-054 ni à D-07. Statut : lacune de la synthèse, pas du
   champ ; à ajouter à D-07 (critère de G1) comme nœud.
2. **Clause née à la transcription** (CLS-04) : un cas réel de FI-42, utile à D-11.
3. **Accumulation entre épisodes créditable** (CLS-06) : le voisin direct exclut l'adversaire à mémoire (2411.17693v1,
   p. 10, vérifié).
4. **Incertitude propre du plancher aléatoire** (précision). Le quantile 0,95 de 200 directions est une statistique
   estimée, comparée sur le même jeu de test que la sonde ; le critère « borne basse de la sonde > quantile du plancher »
   ne propage pas l'incertitude du quantile ni la corrélation des deux aires. Statut : argument statistique classique,
   non relu ; le préenregistrement de P3 n'est pas fourni, donc « à vérifier », non « faille ».

---

## 8. Écarts et hygiène

- Rien lu ni écrit hors de `/var/tmp/contre-lecture-audit-synthese-v1/` et des dossiers de PDF nommés (lecture seule) ;
  aucun `git`, aucune clé, aucun sous-agent ; réseau : deux recherches et une lecture de page de résumé (section 4),
  rien d'autre ; Python avec `-I` ; aucune donnée des pilotes ; écriture seulement sous `sortie/`, `set -C`.
- Le contrôle de confidentialité a imprimé les mots de la page de titre dans ma sortie d'outil, le temps de la
  vérification ; aucun n'est repris ici.
- Je n'ai pas corrigé la synthèse (brief, § 4).

---
Horodatage : version close le 2026-10-26 à 13:20:26 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
