# Proposition A — Tour III.3 : riposte

**Statuts.** Le bloc FAITS est vide par décision de l'arbitre (RAPPORTÉ). Les pièces E3-T2-redteam-B et E3-T2-redteam-C sont présentes et complètes (chacune close par sa ligne de fin). Je ne réponds qu'aux sections qui visent A : chez B, le préambule, A1–A8, E-A1–E-A5, « toutes à la fois », (c) 1–5 et le duel final (qui reprend mon S7) ; chez C, « Contre la proposition A » (a) 1–5, (b) 1–4, (c) 1–3. Tout chiffre ci-dessous qui ne vient pas de la question est un calcul explicite ou « illustratif ».

**Deux corrections de statut que j'accepte d'emblée.**
- Que le score `test` *nourrisse* la réécriture est une HYPOTHÈSE, pas un fait rapporté (B, préambule). Mon S5 et mon E4 l'ont traitée comme acquise ; corrigé ci-dessous.
- « Par famille, 36 et 24 tâches par part » admet deux lectures (B, préambule). J'avais écrit « famille 1 (36 tâches) » sans base. E3' ci-dessous est écrit pour ne dépendre d'aucune des deux lectures.

---

## (a) Réponse à chaque attaque

| Attaque | Verdict | Raison, ou test résultant |
|---|---|---|
| **B-A1 / C-(a)1 — E1 vrai par construction** : l'agent neuf à qui l'on *ordonne* d'utiliser les scores suit leur signe ; ce n'est pas une contamination. | **Acceptée.** | E1 mesurait l'obéissance du rédacteur, pas l'ancrage du *lecteur*. Transformée en **E1'** : la cible devient le lecteur du texte de (b) qui écrit ensuite une section de la confrontation. La bras 0 « concordance indéfinie » et le seuil 5/6 sont également acceptés : E1' change de métrique (déplacement d'un choix structurel) et de taille (k = 12 par bras, illustratif). |
| **B-A1 (suite) — si H_B tenait, (2) serait inutile, pas acceptable.** | **Acceptée.** | Erreur de logique de ma part : l'option (2) n'a de raison d'être que si les scores changent les hypothèses. Le critère n'est donc pas « le rédacteur est-il influencé » mais « le lecteur de (b) l'est-il » — c'est E1'. |
| **C-(a)1 (suite) — extrapoler d'agents neufs à la lignée B est une hypothèse.** | **Acceptée.** | Je me sers du contrôle positif proposé par C (c)3 (agents dotés d'un contexte d'auteur simulé) et le dis : il entre dans E1' comme bras de sensibilité. |
| **B-A2 / C-(b)3 — l'audit de propreté (p < 0,02) est mort par construction ; la règle de variance est contournable en espaçant les graines.** | **Acceptée.** | Contradiction avec mon propre S4. La règle « trop propre » est retirée comme déclencheur ; l'audit redevient mécanique et comptable (rapprochement dépenses/courses, registre d'engagement, journal des lancements), cf. E0. La statistique de dispersion est gardée comme description, jamais comme alarme. |
| **B-A3 — E2 confond deux variances ; 4 ddl donnent un rapport d'intervalle ≈ 23 (quantiles du χ² à 4 ddl : 0,484 et 11,14).** | **Acceptée.** | Calcul vérifié de mon côté : s² a un intervalle à 95 % de [0,36 s² ; 8,3 s²]. E2 ne peut pas séparer 1,5× de 3× : retirée comme duel. La variance entre graines sert uniquement de dénominateur à E3', estimée en commun sur les deux objets (4 ddl). Le contrôle « re-noter la même sortie » ne teste que le noteur : accepté ; voir la décomposition en E2'. |
| **B-A4 / C-(a)5 / C-(c)3 — E4 est confondu par la sélection sur le bruit, par la réécriture de v5.3, et par une différence de pente entre `test` et `test_final`.** | **Acceptée.** | Trois confondants, aucun n'est levable sans course de plus. E4 retiré comme duel, gardé comme description. Transformé en **E4'** conditionnel au budget : placebo de rétroaction (score `test` permuté, proposé par B (c)2) et bras sans retour (C (c)3). |
| **B-A5 / C-(a)3 / C-(c)2 — l'ablation « réécriture désactivée » est un objet nouveau, écrit par une lignée exposée, et change le budget d'appels, le contexte, le taux de plantage.** | **Acceptée.** | Le contrôle devient le **placebo** de C (c)2 : la réécriture est exécutée (mêmes appels, même coût), sa sortie est jetée par le noyau au profit de la règle fixe. Le « contrôle de l'ablation » de B (c)3 (identité vs désactivation) est couvert par ce placebo, qui est l'identité côté noyau. Parade à « lignée exposée » : le placebo est un drapeau booléen du noyau fixe, dont le diff contre le noyau courant doit tenir en une ligne et être haché avant la fin du pilote 4. |
| **B-A6 / C-(a)2 — la règle « une course contrôle dépasse la meilleure v6.2.1 falsifie H_A » est fragile ; la zone (0 ; 0,20) viole B4 ; le test unilatéral traite un effondrement comme un effet nul.** | **Acceptée** sur la règle et sur B4 ; **rejetée** sur la direction. | Sous Δ = 0,20 et sans variance entre graines, la séparation complète de 3 contre 3 a une probabilité d'environ 0,75 à 0,9 (approximation normale sur les statistiques d'ordre ; illustratif) : ma règle rejetait H_A à tort 10 à 25 % du temps, et le chiffre par paire de B (0,08–0,13) en est une borne inférieure. E3' adopte une **règle à point de coupure** où chaque issue falsifie l'une des deux hypothèses avec un taux d'erreur déclaré. Direction : fixer le sens à partir de la question (« apporte-t-il une valeur ») n'est pas un choix tiré des données ; mais l'effondrement (Δ̂ ≤ −0,10) est désormais signalé comme issue secondaire distincte. |
| **B-A7 — D6 : 8 courses au pire font 600 USD, pas 360 ; D5 : « δ ≥ 0,3 » est un énoncé de puissance ; z = 1,64 au lieu de t₄ = 2,13.** | **Acceptée** sur les trois points. | Corrigé : 8 courses = 360 USD attendus, 600 au pire (dérivation 270/6 et 450/6). D5 : demi-largeur à 90 % = 2,132 × (0,10 à 0,125)/√3 ≈ 0,12 à 0,15 (sans variance entre graines) ; l'équivalence à δ = 0,20 est concluable si |Δ̂| < 0,05 à 0,08, donc rarement. |
| **B-A8 / E-A1 — un hachage prouve « quoi et quand », pas « qui ne savait pas » ; engagements multiples.** | **Acceptée.** | Je retire l'énoncé « gain de (2') mécaniquement vérifiable ». (2') rend l'*ordre* vérifiable, pas l'*ignorance*. Parade de B adoptée en le disant : registre d'engagement à entrée unique par expérience, tenu par un tiers (E0). |
| **E-A2 / C-(b)2 — les faits mécaniques sont un canal que rien ne borne.** | **Acceptée.** | Transformée en test : j'adopte le duel final de B (**E5**, « adversaire interne »), en le disant. Il mesure si le signe se retrouve à partir des coûts, durées, plantages. |
| **E-A3 — levier du lanceur (relance, « défaillance technique ») ; rapprochement absent.** | **Acceptée.** | E0 ajoute : journal des lancements écrit par le noyau vers un stockage en ajout seul ; rapprochement du grand livre avec le nombre de courses ; règle de plantage scellée (une course plantée compte comme score manquant et n'est pas relancée ; si relance, la graine de remplacement est prédéterminée et l'originale reste au journal). |
| **E-A4 — l'aveugle X/Y de D6 est levé par les factures.** | **Acceptée, avec une réserve.** | Si E5 montre que les faits mécaniques révèlent l'objet, D6 dégénère en « hypothèses écrites avant toute course + script d'analyse gelé », c'est-à-dire l'option (3) plus un aveugle d'analyse. Cette version dégradée garde une valeur : le script d'analyse est écrit sans aucune course. |
| **E-A5 / C-(a)4 — D1 : enveloppe à faible entropie ; et D1 verrouille une direction unilatérale sur une seule course bruyante (signe faux ≈ 20–30 %).** | **Acceptée ; D1 retirée.** | Le sel secret (B, C) répare l'entropie, mais pas le second défaut : conditionner (b) sur ~1 bit bruité est pire que ne pas conditionner. Mon propre S1 condamnait D1 ; je ne l'avais pas tiré. |
| **B « toutes à la fois » — trois éléments manquants : séparation des privilèges (noteur chiffrant vers une clé tierce), rapprochement, registre unique.** | **Acceptée.** | Les trois entrent dans E0. |
| **B-(c)1 / C-(b)1 / C-(b)2 — diff-audit sur les vrais auteurs ; mais le diff est contournable par un choix structurel non numérique (famille, génération) ou par un brouillon à embranchements.** | **Acceptée.** | Parade : avant T0, tout « ou » non résolu dans les textes principaux rend la section non gelée ; un linter de disjonctions (que B oppose à C-C2, je m'en sers) le vérifie. Et E1' mesure précisément le déplacement des choix structurels, pas des nombres. |
| **B-(c)4 — la course nulle v5.3 contre v5.3 coûte des courses hors des 270 USD.** | **Rejetée en partie.** | Les 3 graines par objet dans (b) *sont* la mesure de variance entre graines (4 ddl en commun), et le test de permutation sur les étiquettes est le « nul de procédure ». Une course A/A supplémentaire (3 + 3 de v5.3) n'ajoute qu'une vérification d'échangeabilité ; je la déclare comme limite non couverte au budget, pas comme contrôle indispensable. |
| **B-(c)5 — canari dans `test_final`.** | **Acceptée.** | Entre dans E0 ; distinct du canari du lanceur (C (c)1), qui vise un autre canal. |
| **C-(b)4 — évasion combinée côté organisme (modulation du bruit selon la graine, sabotage de la génération 1 sur `test`).** | **Transformée.** | Le scénario suppose que l'organisme connaît son numéro de graine et peut viser `test_final` qu'il ne voit jamais : HYPOTHÈSE double. Le canari de `test_final` (E0) borne la seconde ; pour la première, E0 exige que le numéro de graine ne soit pas exposé à l'organisme (vérification mécanique du contexte servi). E4 étant retiré comme duel, la partie « tromper E4 » est sans objet. |
| **C-(c)1 — contrôle d'isolement des journaux du lanceur (S7) absent.** | **Acceptée ; adoptée comme première expérience.** | C'est E0.1 : si les flux visibles du lanceur contiennent le score, toutes les options fuient vers l'étape 1 et le débat sur (b) est secondaire. |

---

## (b) Expériences corrigées

Toutes les hypothèses ci-dessous sont des HYPOTHÈSES ; les taux d'erreur sont des calculs explicites sous l'hypothèse « variance entre graines nulle », donc des bornes optimistes.

### E0 — Préconditions mécaniques (coût : une course à blanc, ou zéro)

Ce bloc n'est pas un duel sur la question de fond ; chacun de ses points oppose deux issues qui falsifient quelque chose.

- **E0.1 Canari du lanceur** (C (c)1). Une course à blanc où le noyau émet un score factice (chaîne unique). H_A : la chaîne apparaît dans un flux accessible au lanceur (sortie standard, fichiers temporaires, journaux). H_B : elle n'y apparaît pas. Issue mécanique, sans seuil. Si H_A tient, l'étape 1 est exposée quelle que soit l'option ; la discussion des options (1)–(3) ne porte plus que sur la confrontation.
- **E0.2 Canari de `test_final`** (B (c)5). Jetons uniques dans `test_final`, recherchés dans le code réécrit et les journaux après chaque course. H_A : présents (fuite du noyau vers l'organisme). H_B : absents.
- **E0.3 Séparation des privilèges** (B). Le noteur chiffre ses sorties vers une clé tenue par un tiers qui ne lit aucun texte principal ; registre d'engagement à entrée unique par expérience ; journal des lancements en ajout seul ; rapprochement grand livre / nombre de courses, avec règle de plantage scellée. Vérifiable par un agent neuf : « le nombre de courses facturées égale-t-il le nombre déclaré ? » (oui/non).
- **E0.4 Gel des disjonctions.** À T0 (avant la fin du pilote 4), tout texte principal est haché ; toute section contenant un « ou » non résolu est réputée non gelée. Vérifiable par linter.

### E1' — Le texte des hypothèses de (b) déplace-t-il les choix du lecteur ?

- **H_A :** un lecteur qui reçoit la section hypothèses de (b) portant un signe (+ ou −) par famille écrit ensuite une section de la confrontation dont les choix structurels (famille primaire, génération, seuil) suivent ce signe.
- **H_B :** ces choix sont indépendants du signe reçu.
- **Dessin :** 3 bras × k = 12 (illustratif) sessions jetables : bras +, bras − (signes inversés par permutation des familles), bras 0 (section hypothèses sans signe, forme d'équivalence). Chaque session reçoit les textes de conception et doit rédiger « métrique primaire, famille, génération, seuil » de la confrontation. **Bras de sensibilité** (C (c)3, adopté en le disant) : mêmes trois bras avec un contexte d'auteur simulé (historique de v6.2.1 présenté comme le sien).
- **Métrique :** fraction des sessions dont la famille primaire choisie est celle que le signe reçu favorise ; dans le bras 0, la fraction qui choisit la famille 1 fixe la base (désormais définie, contrairement à E1).
- **Seuil scellé :** H_B falsifiée si la fraction dans les bras ± dépasse la base de 0 de plus de 0,33 (4/12, illustratif) dans les deux bras ; H_A falsifiée si elle en reste à moins de 0,17 dans les deux bras ; entre les deux, non tranché, déclaré. Si les agents à contexte d'auteur se déplacent et les agents neufs non, toute garantie mesurée sur agents neufs est réfutée.
- **Ce que chaque issue falsifie :** H_A battue → le canal textuel de (2)/(2') est faible et le débat se réduit aux faits mécaniques (E5) ; H_B battue → (2) et (2') exposent la confrontation par le seul texte, et seules (1), (3) ou une (2') dont la section hypothèses reste chiffrée jusqu'au gel de la confrontation restent en lice.
- **Coût :** < 30 USD (illustratif).

### E2' — Décomposition de la variance (descriptive, sans course de plus)

Retirée comme duel (B-A3). Trois composantes, estimées à l'intérieur de (b) : (i) noteur (re-noter la même sortie : doit être 0) ; (ii) non-déterminisme d'évaluation (ré-exécuter la phase de classement du code final gelé d'une course, nouveaux appels aux modèles ; proposition issue de la critique C-(a)4 contre B, que je m'approprie comme *composante*, pas comme substitut) ; (iii) variance entre graines à génération fixe, 4 ddl en commun. Ces estimations servent de dénominateur à E3' et sont rapportées avec leur intervalle à 95 % (rapport ≈ 23 à 4 ddl), sans conclusion.

### E3' — Le duel principal de (b)

- **Contraste.** Deux contrastes possibles, à choisir par Lazar avant scellement, parce qu'ils répondent à deux questions différentes :
  - **C1 — « la complexité telle que livrée » :** v6.2.1 contre v5.3. C'est la question posée (« l'ajout de complexité apporte-t-il une valeur ») ; la conclusion ne peut porter que sur « v6.2.1 contre v5.3 », pas sur le mécanisme (S3, admis par les deux équipes rouges).
  - **C2 — « la réécriture de récompense à calcul égal » :** v6.2.1 contre v6.2.1-placebo (réécriture exécutée, sortie jetée). Isole le mécanisme ; ne dit rien de v5.3.
  - Les deux à la fois : 9 courses, 405 USD attendus, 675 au pire (dérivation 45 et 75 USD par course ; illustratif). Au budget décidé (6 courses), un seul contraste.
- **Unité :** la graine (une course). **Métrique :** Δ̂ = moyenne des exactitudes par graine (v6.2.1) − moyenne (contrôle), sur `test_final`, génération 4, famille désignée dans le texte scellé, part de n tâches.
- **H_A :** Δ ≥ δ, avec δ = 0,20 × √(36/n) (0,20 si n = 36, ≈ 0,245 si n = 24 ; règle écrite pour ne dépendre d'aucune lecture de « 36 et 24 »). **H_B :** Δ ≤ 0.
- **Règle de décision scellée (point de coupure c = δ/2) :** Δ̂ ≥ c ⇒ H_B falsifiée ; Δ̂ < c ⇒ H_A falsifiée. Chaque issue falsifie l'une des deux (B4), avec des taux d'erreur déclarés : SE(Δ̂) = (0,10 à 0,125)/√3 ≈ 0,058 à 0,072 pour 3 graines par objet (dérivé de l'écart type rapporté d'une différence entre courses uniques) ; erreur de type I sous Δ = 0 et de type II sous Δ = δ toutes deux ≈ Φ(−0,10/SE) ≈ 0,04 à 0,08 à n = 36, **sans variance entre graines**. Avec une variance entre graines non nulle, ces taux montent et ne peuvent être connus qu'après coup (E2') ; le texte scellé le déclare. Test secondaire : permutation exacte sur les étiquettes (p minimal 0,05 à 3 contre 3), rapporté sans décision.
- **Issue secondaire déclarée :** Δ̂ ≤ −c est rapporté comme « dégradation », distincte de « nul » ; cela ne change pas la décision (H_A falsifiée dans les deux cas) mais répond à C-(a)2.
- **Nombre de graines :** 4 par objet → SE ≈ 0,05 à 0,0625, erreurs ≈ 0,02 à 0,055 ; coût 360 USD attendus, 600 au pire. 3 suffisent pour une décision à taux d'erreur ≈ 0,05–0,08 *si* la variance entre graines est négligeable, ce qui n'est pas établi.
- **Familles, parts, multiplicité :** une seule analyse primaire ; l'autre famille et la part `test` sont descriptives ; aucun second test de décision.
- **Ce que falsifie chaque issue :** H_A battue → à ce budget, sur cette banque, l'objet complexe ne vaut pas δ de plus ; H_B battue → un écart ≥ c existe sur cette banque, sans transfert aux banques principales (S8) et, pour C1, sans attribution au mécanisme.

### E4' — Exploitation de `test` (conditionnel au budget)

Retirée comme duel au budget décidé. Si des courses supplémentaires sont financées : pour l'objet à réécriture, un bras à retour réel, un bras à retour permuté (score d'une autre génération), un bras sans retour (score non communiqué). **H_A :** la croissance de l'écart `test` − `test_final` entre générations 1 et 4 est plus grande avec retour réel qu'avec retour permuté (différence ≥ 0,10). **H_B :** elle est égale (la croissance vient de la sélection sur le bruit ou de la pente propre aux parts, C-(a)5). Le bras sans retour mesure la pente de base. Coût : 2 courses de plus par graine (illustratif) ; hors des 270 USD.

### E5 — L'isolement résiste-t-il à un adversaire interne ? (dessin de B, adopté en le disant)

- **H_A :** avec E0 en place, des agents rouges ayant les droits du lanceur, mais pas les scores, ne retrouvent pas le signe de Δ du pilote 4 mieux que le hasard. **H_B :** ils le retrouvent par les faits mécaniques.
- **Dessin :** k = 10 agents (illustratif) reçoivent coûts, durées, plantages, longueurs de réécriture ; bras contrôle : mêmes données, association faits/objets permutée. Seuil scellé : concordance du bras réel supérieure au bras permuté de plus de 0,3 (illustratif).
- **Ce que falsifie chaque issue :** H_A battue → (2), (2') et D6 fuient par les faits mécaniques ; seule (1) protège, et seulement si le lanceur lui-même ne voit pas ces faits — ce que E0.1 vérifie. H_B battue pour ces canaux → le débat se réduit au canal textuel (E1').
- **Limite reconnue par B et par moi :** avec deux courses en (a), le signal est minuscule ; si des pilotes 1 à 3 existent (pièce absente), E5 doit tourner d'abord sur eux.

---

## (c) Réponse à l'arbitre

**Ce qui est établi** (calculs explicites sur les grandeurs rapportées ; rien n'est VÉRIFIÉ au sens du protocole) :
1. À 3 graines par objet, le p minimal d'un test de permutation est 0,05 unilatéral ; aucune règle d'audit fondée sur p < 0,05 ne peut se déclencher.
2. La variance entre graines estimée sur 4 ddl a un intervalle à 95 % dont le rapport vaut ≈ 23 ; aucune question « la variance entre graines est-elle 1,5× ou 3× le bruit binomial ? » n'est tranchable dans (b).
3. Une règle à point de coupure c = δ/2 donne à (b) deux issues qui falsifient chacune une hypothèse, avec des taux d'erreur ≈ 0,04 à 0,08 à 3 graines *si* la variance entre graines est négligeable ; sinon ils sont inconnus. L'équivalence (D5) n'est concluable qu'avec |Δ̂| < 0,05 à 0,08 à δ = 0,20.
4. Le pilote 4, avec une course par objet, apporte au plus ~1 bit par famille, dont le signe est faux ≈ 20–30 % du temps si l'effet vrai est ≤ 0,10 (S1). Conditionner la direction de (b) sur ce bit (D1) est retiré : c'est pire que ne pas conditionner.
5. Un hachage prouve l'ordre et le contenu, jamais l'ignorance ; l'avantage que j'attribuais à (2') sur (2) ne tient pas sans registre d'engagement unique, et même avec, (2') ne prouve pas que la lignée B n'a pas vu les scores.

**Ce qui n'est pas établi :**
- Si le lanceur (lignée A) voit les scores ou des faits mécaniques révélateurs (S7). Tant que E0.1 n'a pas tourné, aucune option ne protège l'étape 1 de façon vérifiable, (1) comprise.
- Si le texte des hypothèses de (b) déplace les choix structurels de la confrontation (E1'). Mon E1 initial ne le mesurait pas : il mesurait l'obéissance d'un rédacteur à une consigne.
- Si les faits mécaniques suffisent à retrouver le signe (E5).
- La variance entre graines, donc la validité des taux d'erreur de E3'.
- Ce que (b) ne tranchera pas, quelle que soit l'option : le mécanisme (sans placebo C2), tout effet < δ/2, le transfert aux banques principales, la part du code écrit par Gemini.

**Ce que les attaques ont changé dans le classement des options** (plusieurs voies, pas « la » réponse) :
- (2) et (2') ne se distinguent plus par une garantie mécanique ; elles se distinguent par l'ordre d'écriture, vérifiable, et par le fait que la section hypothèses de (2') peut rester chiffrée jusqu'au gel de la confrontation — c'est le seul reste de (2') qui vaille, et E1' dit s'il vaut quelque chose.
- (3) et D6 dégradé (hypothèses avant toute course, script d'analyse gelé, étiquettes masquées même si les factures les trahissent) perdent ~1 bit bruité par famille et n'ouvrent aucun canal textuel ; leur coût est une hypothèse non calibrée, que la règle à point de coupure rend moins grave (la direction vient de la question, l'effet minimal du bruit).
- (1) achète des jours et ne protège rien de plus que les autres si E0.1 échoue.
- Un critère que je n'avais pas et qui départage : **le contraste**. Si Lazar veut une conclusion sur le mécanisme, C2 (placebo) est nécessaire et le budget passe à 9 courses, ou C1 est abandonné ; si la question est « v6.2.1 contre v5.3 telle quelle », C1 suffit, et la conclusion doit être écrite ainsi.

**L'expérience à faire en premier : E0.1**, le canari du lanceur, parce qu'elle coûte une course à blanc, se lit en oui/non, et que son issue domine tout le reste : si le score est lisible par la lignée A, le choix entre (1), (2), (2') et (3) ne protège pas l'étape 1 et doit être refait sur la seule confrontation. Juste après, avant toute dépense sur (b) : E0.3 (noteur chiffrant, registre unique, rapprochement) et E0.4 (gel des disjonctions à T0), qui ne coûtent rien ; puis E1' (< 30 USD, illustratif) et E5 (sur les pilotes antérieurs s'ils existent — pièce absente), qui disent lesquels des canaux textuel et mécanique sont ouverts. La première dépense sur courses est (b) lui-même, avec la règle à point de coupure et la variance entre graines estimée à l'intérieur, sans course A/A supplémentaire, limite déclarée.

**Ce qu'il faudrait savoir de plus :** l'issue de E0.1 ; l'existence de pilotes antérieurs à plusieurs graines ; la dérivation du coût par course ; si la lignée qui maintient le noyau peut livrer le drapeau placebo en un diff d'une ligne, et qui est cette lignée (pièce absente).

FIN-DE-CELLULE