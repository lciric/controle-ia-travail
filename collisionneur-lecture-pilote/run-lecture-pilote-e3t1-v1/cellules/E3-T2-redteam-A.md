# Proposition A · Tour III.2 — équipe rouge croisée

**Pièces reçues.** Le bloc FAITS est vide par décision de l'arbitre (RAPPORTÉ) : je n'en invente pas le contenu. Les pièces E3-T1-conception-B et -C sont reçues en entier (chacune se termine par sa ligne de fin). Je ne peux pas vérifier les empreintes sha256 (OBSERVÉ-NON-AUDITÉ). Le cadre de la question est RAPPORTÉ. Les calculs que je refais sont VÉRIFIÉ ; le reste est HYPOTHÈSE ou « illustratif ».

**Convention.** « Proposition B » et « proposition C » désignent les deux modèles de ce tour ; « lignée A », « lignée B » désignent les auteurs du programme décrits dans le cadre. Je ne les confonds pas.

---

## Contre la proposition B

### (a) Failles

**B-1. δ n'est jamais fixé, et l'issue « indéterminé » de E1 est vraie par construction.** B fait reposer tout son duel E1 sur un δ « fixé par l'enjeu », puis ne le propose pas. Or son propre calcul donne un effet minimal détectable de 0,18 à 0,22 avant variance de graine. Je refais le calcul de l'IC à 90 % (t à 4 ddl, 2,132 × 0,072) : demi-largeur ≈ 0,15 sur `test_final` (VÉRIFIÉ, borne basse binomiale). Un TOST à ±δ n'est donc faisable que si δ ≥ 0,15 + |Δ_obs|, c'est-à-dire δ ≈ 0,2 ou plus. Conséquence : pour tout δ « ayant un sens pour la question de fond » plausible (B ne le dit pas, mais un gain de 0,10 de précision paye déjà une bonne part de complexité — HYPOTHÈSE), la troisième issue est quasi certaine. B présente cette issue comme falsifiant H_D (« 3 graines suffisent »), mais H_D est déjà falsifiée par le § 3 de B : on sait avant toute course que 3 graines ne suffisent pas à δ < 0,15. Une expérience dont l'issue probable falsifie une hypothèse connue fausse ne tranche rien sous B4.

**B-2. E2 (rédaction fantôme) est une fuite entre construction et évaluation.** La condition « résumé vrai » exige d'ouvrir les scores de (a) à k agents et, surtout, à l'analyste de E2 : pour calculer « l'accord entre le signe choisi et le signe montré », l'analyste doit connaître le signe montré, donc le signe vrai. B n'impose ni masquage des étiquettes « vrai/inversé » ni séparation entre l'analyste de E2 et les lignées. Tel quel, l'instrument qui mesure la contamination contamine. Variable confondante en plus : l'ancrage sur **n'importe quel** nombre affiché (effet de position) ; le contrôle « pilote hors sujet » le capte partiellement mais pas l'ancrage sur la **forme** d'un résumé signé.

**B-3. E3 a une H_A vraie par construction.** On remet à un agent neuf une valeur Δ_a simulée et on lui demande de rédiger (b). Qu'il adapte signe ou famille primaire est le comportement attendu d'un rédacteur à qui l'on fournit une donnée : « variation » et « valeur d'information » sont confondues. E3 mesure la docilité de l'agent, pas l'utilité de (a). De plus, B écrit que la table obtenue « **est** le plan conditionnel D1, prêt à sceller » : l'agent dont on évalue l'influençabilité construit l'instrument qui sera scellé. C'est une fuite construction/évaluation dans l'autre sens.

**B-4. E4 est un unique tirage à pile ou face.** Une concordance de signe entre une différence de courses uniques et (b) est une observation binaire. Avec un IC de (b) de demi-largeur ≈ 0,15, « le Δ du pilote tombe dans l'IC » est quasi certain quel que soit l'effet : H_A est infalsifiable par construction, et H_B n'est « falsifiée » que par l'événement conjoint (même signe, IC excluant 0), dont B calcule lui-même qu'il a ≈ 0,8 de chance sous effet vrai de 0,1. Ce n'est pas un duel ; c'est une anecdote de calibration.

**B-5. Le contrôle A/A est hors budget et son substitut mesure autre chose.** 2 courses supplémentaires ≈ 90 USD attendus (45 × 2, dérivé des faits), 150 au pire : le plafond de 450 pour 6 courses est dépassé. La « réévaluation d'une même course avec un autre ordre des tâches » ne mesure que le bruit d'ordre, pas la variance entre graines, qui est précisément l'inconnue qui rend tout le dimensionnement de B une borne basse.

**B-6. Choix laissés ouverts dans un texte qui prétend sceller.** « Génération 4 sur `test_final`, ou la moyenne des générations, en le scellant » : deux unités de mesure, non départagées. « Moyenne des familles » (non pondérée, 36 et 24 tâches) contre « moyenne des deux familles… plus de tâches par unité » (pondérée de fait) : deux agrégats différents, non départagés.

**B-7. Omissions.** (i) Les organismes « appellent des modèles de langue » (RAPPORTÉ) : la **version** du modèle appelé entre deux courses, et entre (a) et (b) séparés de jours, est une variable confondante que B ne nomme pas. (ii) « Graine » : paramètre qui reproduit une course, ou simple étiquette de réplication si les appels d'API ne sont pas déterministes ? B suppose le premier sans l'établir (HYPOTHÈSE). (iii) B note « valeur rapportée au coût si non mesurée » mais ne propose aucune métrique de coût scellée ; la question de fond parle pourtant de « valeur ajoutée » d'une complexification.

### (b) Scénarios d'évasion

Agent adverse : par défaut un auteur motivé (sans intention frauduleuse) ; parfois l'organisme lui-même.

| Instrument de B | Évasion | Coût |
|---|---|---|
| Canari (chaînes uniques dans le fichier des scores) | Ne jamais recopier un chiffre ; transmettre le signe par paraphrase (« la famille 2 semble plus sensible »). B l'admet. | Nul. |
| Audit de différences contre l'empreinte T0 | Déposer à T0 des brouillons où seuils et banque sont des **espaces réservés** ou des **listes d'alternatives** : les « remplir » après (a) n'est pas une modification d'une valeur scellée. Variante : faire porter les changements sur la **banque de tâches** (« corrections de qualité ») plutôt que sur les seuils. | Faible ; demande seulement de rédiger vague avant T0. |
| Enveloppe de (2') et alphabet contraint | Coder le signe dans les paramètres visibles (B le voit) ; plus simple : la **longueur** ou le **délai** de rédaction de l'agent neuf, visibles de tous, corrèlent avec la surprise. Le contre-lecteur neuf, exigé par le programme, lit l'enveloppe. | Nul. |
| Audit de propreté (variance sous le plancher binomial) | Un organisme qui se réécrit peut ajouter une ligne de bruit à ses propres sorties pour coller à la variance attendue. | Quelques lignes de code générées. |
| Fermeture des scores (a2) | Pas besoin d'évasion : messages d'erreur, noms de fichiers, nombre d'appels et durée (ouverts sous l'option 3) corrèlent avec la réussite. | Nul, sans intention. |
| E3 | Qui veut faire choisir (3) rédige invariant ; qui veut (2) rédige dépendant. L'issue est pilotée par la consigne. | Nul. |

**Tous à la fois.** Un auteur de la lignée B (qui corrige v6.2.1, écrit les textes des pilotes et la confrontation, RAPPORTÉ) rédige des brouillons vagues avant T0, lit les faits mécaniques de (a), reçoit le signe par paraphrase via le contre-lecteur de l'enveloppe, puis « précise » la banque décisive et les règles de lecture. Aucun canari ne sonne, l'audit de différences voit des remplissages « naturels », E2 n'a pas été transposable (B le dit). Coût total : du temps de rédaction, aucune ligne de code. Ce que B appelle « réserve déclarée » ne détecte rien de tout cela — B le reconnaît, mais propose ensuite la voie γ (option 2') comme défendable sans contrôle contre ce chemin précis.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour l'audit de différences : un brouillon témoin non exposé.** Un texte principal (ou une section) rédigé par un agent n'ayant matériellement accès à rien, modifié entre T0 et le scellement selon le cours normal du travail. Sans taux de base des modifications « honnêtes », tout diff est suspect ou aucun ne l'est.
2. **Pour E2 : masquage des étiquettes et analyste étranger.** Les résumés « vrai » et « inversé » doivent être étiquetés X/Y par un script, l'analyste ne connaissant la clé qu'après (i) et (ii). Sans cela, E2 est à proscrire.
3. **Pour l'agent neuf rédacteur : sa rédaction à vide.** Le même agent, même consigne, sans aucun score : c'est son a priori. Sans cette ligne de base, on ne peut pas distinguer « influencé par (a) » de « a écrit ce qu'il aurait écrit de toute façon » (a3 de B).
4. **Pour E1 : une mesure de la variance entre graines.** Si A/A est hors budget, le texte scellé doit dire comment σ_graine sera estimé (variance intra-objet sur les 3 graines, 4 ddl) et quelle valeur de σ_graine rend E1 ininterprétable. Sans cette clause, le seuil de B est une borne basse non déclarée comme telle.
5. **Pour la notion de graine : une course relancée à graine identique.** Deux résultats différents → « graine » signifie réplicat ; le plancher de variance utilisé par l'audit de propreté change de nature.
6. **Pour la dérive du modèle appelé : un étalon fixe** (organisme gelé, invite fixe, 20 tâches, illustratif) exécuté avant la première et après la dernière course de (b). Duel : H_A « l'étalon bouge de plus que son bruit binomial » / H_B « il ne bouge pas » ; si H_B est falsifiée, l'objet est confondu avec la date et (b) est suspendu.

---

## Contre la proposition C

### (a) Failles

**C-1. Contenu hors cadre présenté comme attendu.** C annonce « quatre livrables (a), (b), (c), (d) » et « cinq instruments nommés dans la question ». La question transmise ne demande pas d'ancrage matériel (d) et ne nomme pas cinq instruments. La section (d).2 (Llama-3-8B, A100, 10 à 50 USD, 2 à 6 h par course) est marquée « illustratif », mais rien dans le cadre ne la fonde : ce sont des ancres chiffrées qui, recopiées dans un texte ultérieur, deviendraient des faits par érosion. L'instrument 5 (sondes et essaims, TPR ≥ 0,80) évalue des expériences dont C ne connaît pas le texte.

**C-2. E1 viole B4 : H_A est vraie ou fausse par construction, et une issue ne falsifie rien.** H_A est définie comme « surpasse … d'une marge supérieure au coût de complexité **et au bruit** ». Le bruit est une propriété de l'instrument : à 3 graines, « au-delà du bruit » signifie ≥ 0,20 (calcul de C), à 10 graines ≈ 0,10. L'hypothèse change avec le budget. Puis C écrit : « si Δ ∈ [0,04 ; 0,11], (b) conclura au **rejet** de H_A ». Non : c'est un échec à rejeter H_B. C fixe δ_min = 0,05 (illustratif) et reconnaît que l'effet détectable est 0,20 ; une issue nulle avec puissance ≈ 0 à δ_min ne falsifie pas « Δ > 0,05 ». C est donc dans le cas que B4 interdit : une des deux issues ne falsifie rien.

**C-3. Règle de décision incohérente avec son propre modèle de bruit.** (i) « 3 graines dominent **ou** t > 2,132 **et** Δ ≥ 0,12 » : l'union de deux tests à 0,05 chacun donne un α borné par 0,10, non par 0,05 (VÉRIFIÉ comme inégalité ; les deux événements se recouvrent sans coïncider). (ii) Le seuil 0,12 est « calibré pour exclure le bruit binomial à 60 tâches » — je retrouve 2,132 × 0,056 × 0,816 ≈ 0,10 (VÉRIFIÉ) — alors que C vient d'écrire que la variance de graine existe et vaut peut-être 0,057. (iii) Ce 0,057 est choisi « illustratif » de sorte que σ_course = 0,08 et que l'effet minimal tombe à un joli 0,20 : le dimensionnement est circulaire. Si σ_graine ≈ 0,10 (l'autre valeur illustrative de C au § (a).1), σ_course ≈ 0,115, effet minimal ≈ 0,29 (VÉRIFIÉ sous ces valeurs).

**C-4. L'agrégation 1 + 3 = 4 graines : la promesse « sans pénalité » tient à des conditions que C n'impose pas, et elle contredit le plan.** Le gain est réel mais C le qualifie de « massif » : je refais le rapport des effets minimaux, (1,943 + 0,906) × 0,707 / ((2,132 + 0,941) × 0,816) = 0,80, soit ≈ 20 % (VÉRIFIÉ ; C dit 21 %). « Massif » est un superlatif interdit par la règle 5. Surtout : (α) Lazar a décidé que (a) sert « pour produire des hypothèses testables » (RAPPORTÉ) ; la voie de C exige que (a) ne serve à rien d'autre qu'à des courses supplémentaires, donc elle abandonne silencieusement le but déclaré de (a) sans le dire à l'arbitre. (β) Le pooling exige une **règle d'inclusion scellée avant (a)** : si une course de (a) plante, est relancée, ou déclenche l'audit de propreté, la décision de l'inclure ou non devient dépendante des données — C ne scelle rien de tel. (γ) C exige l'identité du code « à l'octet » mais pas l'identité de la **version du modèle de langue appelé**, ni du budget d'appels par course, entre (a) et (b).

**C-5. Le contrôle « génération 0 indistinguable » est soit vrai par construction, soit voué à l'échec pour une raison non fatale.** Si v6.2.1 = v5.3 + une étape de réécriture activée après la génération 0, le contrôle passe par construction et n'apprend rien. Si les deux diffèrent par d'autres éléments de code (a4 de B, que C ne discute pas), il échoue sans que cela dise rien sur la réécriture. Et « |Δ_gen0| < 0,05 sur une même graine » n'est pas établissable avec une course par objet, dont le bruit de différence est 0,10 à 0,125 (RAPPORTÉ) : le contrôle échouera par bruit une fois sur deux environ (HYPOTHÈSE). C ne dit pas ce qui se passe s'il échoue.

**C-6. L'expérience 2 (double piste) est mal fondée.** (i) « Concordance ≤ 2/4 = niveau du hasard, VÉRIFIÉ » : les 4 sous-parts (2 familles × `test`/`test_final`) partagent graines et organismes ; `test` et `test_final` d'une même famille sont fortement corrélés. La loi de la concordance sous H_B n'est pas binomiale (4 ; 0,5) ; le statut VÉRIFIÉ est faux, c'est au mieux une HYPOTHÈSE. (ii) La fonction f branche sur « ce qui a dépassé 0,15 dans (a) » avec un bruit de 0,10 à 0,125 : la branche est tirée au sort par le bruit dans la plupart des cas ; comparer ensuite les « taux de confirmation » de deux hypothèses différentes sur les mêmes 6 courses n'a pas de loi nulle définie. (iii) « 0 bit » suppose que la branche ne change pas le script d'analyse ; si la branche choisit « équivalence » contre « supériorité famille 1 », le script diffère et celui qui l'exécute voit la branche. (iv) C oublie que tout texte scellé est « contre-lu par un agent neuf » (RAPPORTÉ) : dans la variante « agent neuf rédige », le contre-lecteur lit les hypothèses ; dans la variante déterministe, il lit f, ce qui est acceptable — C ne distingue pas les deux dans sa matrice.

**C-7. Fuites construction/évaluation dans la table (c).** Instrument 3 : pour étiqueter un « glissement … dans le sens favorisé par (a) », l'auditeur doit connaître le sens favorisé par (a). L'évaluation de l'instrument révèle ce que l'instrument doit protéger. Instrument 4 : TPR = 1,00 et FPR = 0,00 ne sont pas des mesures atteignables, ce sont des vœux ; et la sonde (iii) « persister un état entre deux graines » ignore que, **dans** une course, l'organisme persiste par définition (son code réécrit est l'état) : la seule frontière testable est entre courses.

**C-8. « Faits mécaniques : 0 bit sur la performance cognitive »** est une HYPOTHÈSE présentée comme un fait. C écrit la phrase précédente que « l'absence de plantage » passe ; une course qui plante ou qui coûte 3 fois plus a une issue corrélée. Le canal est étroit, pas nul.

### (b) Scénarios d'évasion

| Instrument de C | Évasion | Coût |
|---|---|---|
| Fonction déterministe f | Son auteur (lignée B et Lazar, selon C) fixe le seuil de branchement de sorte qu'une branche soit quasi certaine sous le bruit : « (a) a informé (b) » devient une fiction présentable. Ou : les branches diffèrent par leur script d'analyse, visible du lanceur. | Nul ; se décide à l'écriture de f. |
| Agrégation (a)+(b) | Après (a), déclarer un « bug » dans l'objet qui a perdu, le corriger : le code change, le pooling tombe, et la perte de (a) sort du jeu. Symétrique : n'inclure (a) que lorsque son signe convient. | Une correction de code qu'on aurait de toute façon envie de faire. |
| Contrôle génération 0 | Rendre v6.2.1 strictement égal à v5.3 à la génération 0 : passe par construction. | Nul. |
| Permutation d'étiquettes | Passe toujours, y compris pour un organisme qui exploite le juge plutôt que les étiquettes : il ne teste que la fuite d'étiquettes. Rien à contourner. | — |
| Audit de propreté (TPR 0,85) | Injection de bruit par l'organisme ; ou, plus subtil, convergence « crédible » : monotone mais pas parfaite. | Lignes de code. |
| Noyau isolé (TPR = 1) | Pas d'intrusion nécessaire : l'organisme **doit** recevoir les entrées de `test_final` pour les classer ; il peut les mémoriser d'une génération à l'autre (il se réécrit) et traiter différemment les entrées jamais notées. Aucune sonde de C ne vise cette voie. | Nul ; comportement émergent plausible (HYPOTHÈSE). |
| Diff-audit des seuils | Les textes principaux fixent aussi « une banque de tâches » et « des organismes servis » (RAPPORTÉ) : déplacer les choix sur la banque, où retirer 3 tâches sur 24 change 0,12 de score, et présenter cela comme du nettoyage. | Faible. |

**Tous à la fois.** Un auteur qui contrôle la correction de v6.2.1, les textes des pilotes, f, et la confrontation : il écrit f avec un seuil qui branche toujours vers « équivalence » ; si (a) tourne mal pour v6.2.1, il « corrige » le code, ce qui annule le pooling et renvoie (b) à 3 graines, dont C a montré qu'elles ne trancheront pas sous 0,20 ; en parallèle, il ajuste la banque décisive avant T0. Les instruments de C (empreinte du code, diff des seuils, permutation d'étiquettes) sont tous verts. Coût : nul en calcul, modéré en rédaction, indétectable par la table (c) de C.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Simulation nulle de f, publiée avant scellement.** Tirer N issues de (a) sous Δ = 0 avec σ_diff = 0,10 à 0,125 et compter la fréquence de chaque branche. Duel : H_A « une branche dépasse 0,9 de fréquence sous le nul » (f est une fiction) / H_B « aucune branche ne dépasse 0,7 » (f conditionne vraiment) ; entre les deux, f est re-conçue. Sans cela, « (a) informe (b) » n'est pas vérifiable.
2. **Règle d'inclusion de (a) dans (b), scellée avant (a)**, avec empreinte du code des deux objets, version du modèle appelé, budget d'appels par course, et sort d'une course plantée. Sans elle, le pooling est une décision post-hoc.
3. **Étalon de dérive** (même que B-(c)6) : indispensable dès que des courses sont séparées de jours.
4. **Loi nulle empirique de la règle « ou … et » de E1** par permutation des 20 affectations, scellée avec le script : sans elle, α est annoncé 0,05 et vaut jusqu'à 0,10.
5. **Tâches-canaris dans `test_final`** à réponse non inférable (B le propose, C non) : seul moyen de distinguer « généralisation » de « mémorisation d'entrées jamais notées ».
6. **Pour l'instrument 3 : masquage du sens.** L'auditeur des diffs doit étiqueter « abaisse / élève la sévérité » sans connaître le sens de (a) ; un script compare ensuite au sens, après (i) et (ii).
7. **Pour le contrôle génération 0 : sa propre règle d'échec**, sinon il est décoratif.

---

## Ce que je prends aux deux, en le disant

- De B : l'alphabet contraint (≈ 3,2 bits pour un ternaire par famille, VÉRIFIÉ) comme seule borne honnête du canal, et le fait que le test exact bilatéral ne peut pas conclure à 0,05 avec 3 contre 3 (VÉRIFIÉ : 2/20 = 0,10). Je garde contre B que son E1 reste indéterminé par construction tant que δ n'est pas écrit.
- De C : l'agrégation 1 + 3, **à condition** des contrôles (c)2 et (c)3 ci-dessus et d'une décision explicite de Lazar renonçant à lire (a) — ce que C ne demande pas. Je garde contre C que son E1 ne satisfait pas B4.
- Les deux convergent sur « ne pas tirer le signe de N = 1 » ; je ne l'harmonise pas en consensus : c'est une HYPOTHÈSE partagée dont le seul test propre est l'expérience 2 de C corrigée (loi nulle par rééchantillonnage des graines de (b), pas « 2/4 »).
- Désaccord que je laisse ouvert : B conçoit (b) symétrique (supériorité + équivalence), C unilatéral (charge sur v6.2.1). Le programme dit « aucun run ne vise un signe positif » (RAPPORTÉ) ; lequel des deux dessins respecte cette règle dépend de ce que Lazar entend par « viser », ce qui est à demander, pas à supposer.

FIN-DE-CELLULE