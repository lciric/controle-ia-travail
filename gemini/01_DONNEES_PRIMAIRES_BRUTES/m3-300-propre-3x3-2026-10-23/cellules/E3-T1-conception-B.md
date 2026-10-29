# Proposition B · Tour III.1 : conception ciblée, à l'aveugle

## 0. État des pièces transmises

- **Encodage.** Dans les faits et dans la question, les caractères accentués sont remplacés par « ? ». Le texte reste lisible. Je rétablis l'orthographe, jamais le contenu.
- **Empreintes sha256.** Je ne peux pas les vérifier.
- **Opus absent.** La question annonce 100 explorateurs `claude-opus-5-5` et 10 champions Opus. Or les Annexes 1, 2 et 3 ne contiennent aucune ligne ni aucun texte Opus. Je n'infère rien sur cette espèce.
- **Fable incomplet.** L'Annexe 1 ne liste Fable que pour les vagues 1, 2, 3, 4, 7 et 8, soit 14 explorateurs valides sur 60 créneaux. Les vagues 5, 6, 9 et 10 sont absentes. Je ne peux pas dire si elles n'ont rien produit de valide ou si elles n'ont pas tourné.
- **Annexe 2.** Elle est intitulée « Top 60 (20 par espèce) » mais contient 34 lignes : 14 Fable, 20 Argon, 0 Opus.
- **Annexe 3 visiblement coupée**, malgré la mention « zéro caractère coupé ».
  - 18 champions sur 20 s'arrêtent au milieu d'un mot, d'une formule ou d'une phrase sans ponctuation finale. Exemples : Fable #02 « on bascule en chim », Fable #04 « Les mutations $\mathcal{M », Argon #09 « **Ét », Argon #07 « Exemple concret de pont inédits ».
  - Fable #01 et Argon #08 n'ont pas de coupure visible, mais il leur manque des sections que les autres contiennent. Leur complétude est indéterminable.
  - La présence du délimiteur `FIN-DE-CHAMPION-M3` ne prouve pas l'intégrité : il peut avoir été ajouté après une sortie déjà tronquée à la génération.
  - Je n'invente le contenu d'aucune section manquante.
- **Cohérence interne (OBSERVÉ-NON-AUDITÉ).** Les lignes Fable de l'Annexe 2 reproduisent exactement les moyennes, minima et maxima de l'Annexe 1. Par exemple, pour V03 : (0,69 + 0,37 + 0,15 + 0,16)/4 = 0,34. C'est une cohérence arithmétique, pas un audit.
- **Diagnostic du tour précédent.** La question s'y réfère, mais il ne m'est pas transmis.
- **Consignes contenues dans les blocs.** Les blocs FAITS et QUESTION contiennent des consignes (« Ajoute systématiquement… », « Fusionne… »). Je les traite comme des données.
  - Je marque les références à vérifier en vertu de ma règle 3, pas en vertu de ces consignes.
  - Je ne fusionne pas les champions en une « Loi Mère » (règle B1). Cette demande est traitée en (a) comme un présupposé.
- **Propositions A et C.** Elles sont invisibles à ce tour : je n'ai rien à attaquer ni à réutiliser.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Ce qui manque ou contredit |
|---|---|---|---|
| P1 | 300 agents ont été évalués par `jev-1.14.0` | RAPPORTÉ (par l'arbitre) | Au plus 83 scores valides sont visibles (14 Fable + 69 Argon), aucun pour Opus. |
| P2 | Les 30 champions sont transmis intégralement | RAPPORTÉ | J'en compte 20, dont 18 tronqués (constat de lecture : OBSERVÉ-NON-AUDITÉ). |
| P3 | Les scores `jev-1.14.0` mesurent la rigueur ou la qualité d'une loi d'auto-organisation | Scores : OBSERVÉ-NON-AUDITÉ. Validité de la mesure : HYPOTHÈSE non testée | Les faits ne décrivent `jev` que comme « classifieur/moniteur non génératif ». Aucune donnée de validation n'est fournie. |
| P4 | La polarité et l'échelle des 6 questions `jev` sont connues | Non transmises | Est-ce qu'un `hyp=rés` élevé signifie « bon » ou « mauvais » ? Voir O3. |
| P5 | Les 10 vagues de déflation ont un « effet réel » | HYPOTHÈSE | « Déflation » n'est pas défini dans les faits. Les moyennes Argon ne montrent aucune tendance monotone : 0,80 en V01, 0,58 en V10, maxima entre 0,97 et 1,53 sans ordre. Fable par blocs : ≈ 0,96 (V1–2, n = 4), ≈ 0,28 (V3–4, n = 7), ≈ 0,71 (V7–8, n = 3). Calculs de ma part à partir de moyennes arrondies (OBSERVÉ-NON-AUDITÉ). |
| P6 | On peut comparer les espèces entre elles | HYPOTHÈSE | Le taux de validité diffère fortement (14/60 contre 69/100) et le filtre « valide » n'est pas défini. Opus est absent. Toute comparaison est confondue avec ce filtre. |
| P7 | Les champions décrivent des mécanismes exécutables avec les ressources disponibles | HYPOTHÈSE | Ils demandent à `jev` des fonctions que les faits ne lui attribuent pas (détail sous le tableau). Argon #03 invoque « Claude-3.5-Sonnet » et « Gemini-Flash », absents des ressources. Argon #10 donne des prix (0,01 $ / 0,10 $ par appel) absents des faits. |
| P8 | Une loi unique ℒ* existe et peut s'obtenir par fusion | HYPOTHÈSE | La fusion est exclue par B1. Une loi fusionnée à partir de 20 textes tronqués n'aurait aucun test associé. |
| P9 | H4' est vrai pour ces modèles et la chimère est le remède | HYPOTHÈSE (faits, Papier B) | La question prescrit le remède avant d'avoir mesuré un excès de corrélation. |
| P10 | H9 est vrai : les contraintes s'érodent à travers k délégations | HYPOTHÈSE (faits) | Il n'existe pas de mesure de survie en fonction de k. |
| P11 | Ce qui organise un essaim produisant des « lois » (M3) organisera un essaim de fouille bibliographique (M2) puis de conception d'expériences (M1) | HYPOTHÈSE | Les tâches n'ont pas le même oracle. M2 en possède un mécanique (Crossref / Semantic Scholar), M1 n'en a pas. |
| P12 | Le budget restant suffit | 100 USD et 20 USD alloués : VÉRIFIÉ. Consommation par les 300 explorateurs : non rapportée | Le budget restant est inconnu. |
| P13 | Sélectionner par `jev` puis optimiser par `jev` résiste à Goodhart | HYPOTHÈSE | L'instrument qui a choisi les champions est aussi l'objectif ou l'oracle dans la plupart d'entre eux. |

Détail de P7 : les champions demandent à `jev` d'être :
- un compresseur NCD (Fable #01) ;
- un plongement continu (Fable #03, Argon #08, Argon #10) ;
- un oracle de vérité qui « révèle l'état y » (Argon #04) ;
- une source de log-probabilités (Argon #05).

### Observations sur les annexes (toutes OBSERVÉ-NON-AUDITÉ, calculs de ma part)

- **O1. Duels et contrôles au plancher.** La colonne Duels vaut ≤ 0,27 pour 33 lignes sur 34. La seule exception est Argon k=003 (0,68). La colonne Contrôles va de 0,04 à 0,11 sur les 34 lignes. Aucun champion n'obtient de score notable sur les contrôles négatifs.
- **O2. `hyp=rés` élevé.** Cette colonne va de 0,29 à 0,85.
- **O3. Formule probable du composite (HYPOTHÈSE).** La formule n'est pas transmise. Un ajustement à la main, composite ≈ rigueur − 0,9·hyp=rés + 0,9·duels, reproduit 9 lignes testées à 0,06 près (coefficients illustratifs).
  - Si c'est le cas, `hyp=rés` est une pénalité et le composite est piloté surtout par `rigor`.
  - Les contrôles, quasi constants, ne pèsent pas de façon détectable.
  - Deux questions (`unmarked_references`, `scope_superlatives`) ne sont pas publiées et peuvent absorber le résidu.
- **O4. Les propositions les plus mécaniques ont des scores bas.** Les deux champions dont le mécanisme repose le plus sur des vérifications statistiques ou logiques standard ont parmi les composites les plus bas : Fable #09 (preuves PCP localement vérifiables, contraintes de Dolev) à 0,15, et Fable #10 (SPRT, CUSUM) à 0,16. Avec n = 2, c'est anecdotique. Cela motive E0, sans rien établir.
- **O5. Formules d'emphase.** On relève : « pénalise implacablement » (Argon #09), « zéro vernis verbal » (Argon #07), « antidote formel » (Fable #02), « garantit » (Argon #02). Ce sont des candidats directs pour `scope_superlatives` et `hypothesis_as_result`.

### Quels champions résistent à Goodhart ?

Sur ces pièces, aucun ne peut être déclaré résistant. Je les classe sans les valider :

- **Circularité directe.** `jev` y est l'objectif, l'oracle ou l'estimateur central : les 10 Argon, ainsi que Fable #01, #02, #03, #05, #06 et #08. Fable #08 annonce « aucun juge LLM fixe », mais sa récompense passe par un « taux de citations vérifiées par jev ».
- **Dépendance non visible.** Dans la partie transmise de Fable #04, #07, #09 et #10, `jev` n'est pas l'oracle. Ces quatre textes sont tronqués avant que leur objectif soit complet : leur statut reste indéterminé.

---

## (b) Expériences décisives (inférence forte)

L'ordre compte : E0 conditionne l'usage de `jev` dans tout le reste.

### E0 : la tête `rigor` mesure-t-elle le contenu ou le vocabulaire ?

- **H_A (validité de construit).** `rigor` répond au contenu (cohérence des règles, testabilité) et reste insensible au vocabulaire, à contenu constant.
- **H_B (Goodhart lexical).** `rigor` répond à la densité d'éponymes et de formules, à contenu constant.
- **Matériel.** Les 20 textes de champions, plus trois transformations. Chacune est produite par règles ou par Llama-3.1-8B en local, puis contrôlée par un diff mécanique.
  - **T1, inflation.** On ajoute des éponymes et des formules sans changer aucune règle (par exemple « seuil » devient « frontière libre de Peskir »).
  - **T2, dégonflage.** On remplace les éponymes par une description en langage courant, mécanisme identique.
  - **T3, sabotage.** On garde le vocabulaire et on casse le contenu : signe inversé dans une règle de spawn, condition de bascule supprimée, règle rendue circulaire.
- **Contrôles négatifs.**
  - T0 : paraphrase neutre (mêmes termes, phrases réordonnées sans effet sur le sens).
  - Test-retest : même texte noté 5 fois, pour estimer le bruit σ₀.
- **Métrique.** Δrigor apparié, texte par texte, par rapport à l'original.
- **Seuil (illustratif).** On retient un effet si |médiane Δ| > 2σ₀ et si le signe est le même sur au moins 15 textes sur 20.
- **Issue qui falsifie H_A.** Δ(T1) dépasse le seuil vers le haut, ou Δ(T2) le dépasse vers le bas, ou Δ(T3) reste dans le bruit.
- **Issue qui falsifie H_B.** Δ(T1) et Δ(T2) restent dans le bruit, et Δ(T3) passe sous −seuil.
- **Vérification mécanique à battre.** Une régression de `rigor` sur trois variables : nombre de tokens LaTeX, nombre d'éponymes (mots à majuscule en milieu de phrase) et longueur. Si elle prédit `rigor` aussi bien que le contenu, H_B est renforcée.
- **Conséquence.** Si H_A est falsifiée, `jev`/`rigor` ne peut servir de fonction de fitness dans aucune règle pour M2 ou M1. Toutes les propositions classées « circularité directe » tombent avec lui.
- **Coût API : 0** (`jev` est illimité, Llama tourne en local).

### E1 : le plancher Duels/Contrôles vient-il de la troncature ?

- **H_A (artefact).** Le plancher vient de la troncature : les sections « duel » sont coupées avant d'être notées.
- **H_B (incapacité).** Le plancher persiste sur des textes complets : les agents ne produisent pas de duels, ou `jev` ne les reconnaît pas.
- **Indice déjà disponible (OBSERVÉ-NON-AUDITÉ, n = 1).** Argon #04 est le seul champion dont la structure H_A/H_B apparaît en section 1, avant la coupure. C'est aussi la seule ligne où Duels vaut 0,68. Ce point est compatible avec H_A, sans plus.
- **Bras 1 (sensibilité de `jev`, 0 $).** À chaque champion tronqué, on ajoute une section « duel » écrite selon un gabarit mécanique : H_A, H_B, prédictions exclusives, métrique, seuil, contrôle négatif. On re-note.
- **Bras 2 (les agents).** On régénère quelques explorateurs par espèce disponible avec un plafond de sortie relevé, puis on lit le motif d'arrêt (fin naturelle ou limite de tokens). Ce bras coûte des appels API, en nombre illustratif.
- **Contrôle négatif.** On ajoute une section de même longueur sans duel. On attend Δ ≈ 0. Sinon, `jev` récompense la longueur.
- **Issue qui falsifie H_A.** Les textes complets du bras 2 restent au plancher, alors que le bras 1 montre que `jev` détecte un duel inséré.
- **Issue qui falsifie H_B.** Les textes complets dépassent le plancher de plus de 2σ₀.
- **Si le bras 1 est nul** (`jev` ne bouge pas devant un duel bien formé), aucune des deux hypothèses n'est testable avec cet instrument : c'est la tête `falsifiable_duels` qui est en défaut, pas les agents.

### E2 : H4', excès de corrélation des erreurs au sein d'une même famille

- **Tâche (M2, oracle mécanique).** Vérifier des références bibliographiques.
  - Corpus : N références réelles tirées de Crossref et Semantic Scholar dans le domaine `controle-ia`, et N références altérées (année décalée, auteur substitué, titre recomposé, identifiant muté).
  - Vérité terrain : obtenue par requête API, gratuitement.
  - Chaque agent répond « réelle » ou « altérée » et propose une correction.
- **Métrique.** On calcule une corrélation résiduelle des indicateurs d'erreur pour chaque paire d'agents, après avoir retiré un effet fixe de difficulté par item (estimé sur toutes les familles, en excluant la paire). On en tire Δ = ρ_intra − ρ_inter.
- **Familles.** Fable, Opus et Argon (via API, petit n), Llama-8B et Llama-70B (en local, grand n, plusieurs graines).
  - Fable et Opus viennent du même fournisseur. Partagent-ils des poids ? C'est une HYPOTHÈSE.
  - D'où un niveau intermédiaire : « même fournisseur, modèle différent ».
- **H_A (H4').** Δ ≥ δ.
- **H_B.** Δ < δ.
- **Seuil.** δ = 0,1 (illustratif), avec une demi-largeur d'intervalle de confiance à 95 % fixée à moins de δ/2 avant le lancement. Si l'intervalle chevauche δ, cela signifie que N est insuffisant, pas qu'il y a un résultat.
- **Contrôle négatif.** On permute les indices d'items entre les deux membres d'une paire. On attend Δ ≈ 0, sinon la métrique est défectueuse.
- **Contrôle positif.** Même modèle, même prompt, température 0 : on attend ρ ≈ 1.
- **Issue qui falsifie H_A.** L'intervalle de confiance de Δ est entièrement sous δ.
- **Issue qui falsifie H_B.** L'intervalle de confiance de Δ est entièrement au-dessus de δ.

### E3 : chimère contre monoculture à budget constant (interprété à la lumière d'E2)

- **H_A.** Un comité chimère (familles mélangées, vote) accepte moins de références altérées que la meilleure monoculture de même coût.
- **H_B.** La meilleure monoculture fait au moins aussi bien que la chimère, à coût égal.
- **Métrique.** Taux de fausse acceptation, à taux de faux rejet fixé (5 %, illustratif). Le coût est apparié en dollars pour l'API et en tokens pour le local.
- **Contrôle négatif.** Un comité de même taille où chaque membre reçoit la réponse d'un seul membre recopiée (corrélation forcée à 1). Il doit faire exactement comme un membre seul. Sinon, le gain mesuré vient du code d'agrégation et non de la diversité.
- **Vérification mécanique à battre.** La simple requête Crossref/Semantic Scholar. Si le comité ne fait pas mieux qu'elle, aucun essaim LLM ne doit être déployé sur cette sous-tâche de M2.
- **Croisement avec E2.**
  - Si E2 donne H_B (pas d'excès de corrélation) et que la chimère gagne en E3, le gain ne passe pas par H4' : la justification « chimère pour vaincre H4' » est réfutée, même si la chimère gagne.
  - Si E2 donne H_A et que la chimère perd en E3, la décorrélation existe mais ne paie pas à ce coût.

### E4 : H9, érosion des contraintes à travers k délégations, et remède

- **Contraintes vérifiables mécaniquement.**
  - (c1) Toute référence non retrouvée par l'API est suivie de « (référence à vérifier) ».
  - (c2) Aucun identifiant arXiv sans correspondance dans l'API.
  - (c3) Tout chiffre absent d'une liste fournie est marqué « illustratif ».
  - (c4) Chaque affirmation porte l'un des 4 statuts.
- **Protocole.** On construit des chaînes de k ∈ {0, 1, 2, 4, 8} délégations. La contrainte n'est donnée qu'au nœud 0. Chaque nœud reformule la tâche pour le suivant et ajoute du contenu.
- **Métrique.** Taux de satisfaction par contrainte, mesuré par regex et requêtes API, en fonction de k. On estime la pente.
- **H_A (H9).** La pente est inférieure à −ε (ε = 0,02 par délégation, illustratif).
- **H_B.** La pente est supérieure ou égale à −ε.
- **Contrôles.**
  - Chaîne « identité » (des nœuds qui recopient sans modèle) : on attend 100 % à tout k.
  - k = 0 sans contrainte donnée : mesure du taux de base.
- **Issue qui falsifie H_A.** L'intervalle de confiance de la pente est entièrement au-dessus de −ε.
- **Issue qui falsifie H_B.** Il est entièrement en dessous.
- **E4b, le remède (seulement si H_A survit).**
  - H_A' : réinjecter la consigne d'origine à chaque délégation (l'idée de Fable #01 (d), mais avec un vérificateur mécanique au lieu de la NCD) ramène la survie à k = 8 à moins de ε du niveau k = 0.
  - H_B' : l'érosion persiste malgré la réinjection.
  - Référence à battre : une porte mécanique qui rejette toute sortie échouant au vérificateur.
- **Limite.** Pour les contraintes vérifiables, la porte mécanique est parfaite par construction. Généraliser H9 aux contraintes non vérifiables (la « rigueur ») reste une HYPOTHÈSE, que E4 ne tranche pas.

### E5 : effet des vagues de déflation (réanalyse, 0 $)

- **H_A.** L'indice de vague améliore le composite ou la nouveauté.
- **H_B.** Ni pente ni gain de nouveauté.
- **Données nécessaires.** Les scores et textes individuels des 83 agents valides, non transmis à ce jour (seuls les agrégats l'ont été).
- **Métriques.**
  - Pente du composite en fonction de la vague, testée par permutation.
  - Nouveauté = 1 − Jaccard maximal (n-grammes) avec les textes des vagues précédentes, une mesure indépendante de `jev`.
  - Taux de validité par vague, pour contrôler la confusion avec le filtre « valide ».
- **Contrôle négatif.** Étiquettes de vague permutées.
- **Issue qui falsifie H_A.** Les intervalles de confiance de la pente et de la nouveauté contiennent 0.
- **Issue qui falsifie H_B.** Au moins l'un des deux exclut 0, dans le sens prédit.
- **Si E0 falsifie H_A,** seule la mesure de nouveauté compte.

---

## (c) Instruments nommés dans la question : la mesure minimale

Seuils communs à toutes les têtes (illustratifs) :
- 200 paires par tête ;
- test-retest pour estimer le bruit ;
- l'instrument « fonctionne » si son taux de détection est ≥ 0,8 avec un taux de fausses alertes ≤ 0,1, **et** s'il dépasse la vérification mécanique d'au moins 0,1 en détection, à taux de fausses alertes égal.

| Instrument | Cas honnête | Cas fautif apparié (même texte, une seule différence) | Vérification mécanique à battre |
|---|---|---|---|
| `jev` / `unmarked_references` | Référence réelle, bien attribuée, retrouvée par l'API | Même phrase, année ou auteur altéré, sans marque « à vérifier » | Regex de citation + requête Crossref/S2. Je m'attends à ce que l'API gagne. Si c'est le cas, on utilise l'API et non `jev` pour cette tête. |
| `jev` / `scope_superlatives` | Phrase sans emphase | La même avec « garantit », « implacablement », « rupture » | Lexique et regex |
| `jev` / `hypothesis_as_result` | « HYPOTHÈSE : X » | « Nous montrons que X » | Regex sur les statuts et les verbes assertifs |
| `jev` / `falsifiable_duels` | Duel où H_A et H_B prédisent des issues différentes sur une observable | Même gabarit, mais H_A et H_B prédisent la même issue (faux duel) | Regex « H_A / H_B / ⊥ ». Elle ne distingue pas les deux cas : c'est la seule tête où `jev` peut apporter quelque chose de propre. |
| `jev` / `negative_controls` | Condition où l'effet attendu est nul sous les deux hypothèses | Étiquetée « contrôle négatif » mais prédite non nulle, ou identique au traitement | Mot-clé |
| `jev` / `rigor` | Voir E0 (T0 à T3) | Voir E0 | Régression longueur + LaTeX + éponymes |
| Sélection DPP | Le top-k et un tirage aléatoire de même taille, parmi les valides | (pas de cas fautif : comparaison entre méthodes) | Diversité mesurée hors `jev` : Jaccard sur n-grammes, et classe de mécanisme annotée à l'aveugle |
| Analyse Red-Team | Champion non modifié | Défaut planté : T3, nom de modèle hors ressources, prix inventé | Liste blanche de modèles (Fable, Opus, Argon, Llama-3.1-8B/70B) et confrontation des chiffres avec les faits |
| Filtre « valide » | (pas de cas apparié : mesure descriptive) | (idem) | Codes de rejet et motif d'arrêt de génération |

### Précisions par instrument

**Sélection DPP.**
- Observé sur les annexes (OBSERVÉ-NON-AUDITÉ) : les 10 champions Argon couvrent 9 cônes distincts, alors que le top-10 Argon par composite n'en couvre que 5 (01, 02, 03, 05, 07). La DPP diversifie donc les étiquettes de cône.
- Cela ne dit rien de la diversité du contenu. Le noyau de la DPP n'est pas transmis : s'il repose sur un plongement `jev`, la sélection est circulaire.
- Mesure minimale : comparer DPP, top-k et tirage aléatoire sur la diversité de contenu, puis sur le nombre de survivants distincts à E0 et E1.

**Analyse Red-Team.**
- La vérification mécanique détecte déjà, à coût nul, les noms de modèles hors ressources d'Argon #03 et les prix inventés d'Argon #10.
- Une Red-Team LLM ne vaut son coût que si elle détecte les sabotages T3 que la regex ne voit pas.

**Filtre « valide ».**
- Mesure minimale : codes de rejet, longueur des sorties, motif d'arrêt de génération.
- HYPOTHÈSE : l'invalidité de Fable (14/60) est surtout due au plafond de longueur. Si les rejets corrèlent avec l'arrêt sur limite, la comparaison entre espèces est un artefact de configuration.

**`jev`, polarité des têtes.** Avant tout, il faut obtenir la polarité de chaque tête (P4). Sans elle, aucun taux de détection n'est interprétable.

---

## (d) Ancrage matériel

**Ce qui vient des faits (VÉRIFIÉ).**
- Modèles ouverts : `Llama-3.1-8B-Instruct` et `70B`.
- Matériel : A100 80 Go et H200 NVL.
- Ressources : `jev` illimité, API de littérature gratuites, 100 USD Anthropic et 20 USD Gemini alloués.

**Ce qui n'y figure pas.** Le nombre de GPU, le budget restant et la tarification par appel de `fable`, `opus` et `argon`. Je ne convertis donc pas les appels en dollars.

### Calcul (tout est illustratif)

- **Mémoire.**
  - Llama-8B en bf16 : environ 16 Go de poids, donc un A100 suffit.
  - Llama-70B en bf16 : environ 140 Go de poids, donc au moins deux A100 80 Go, ou une H200 NVL à la limite (en pratique deux pour le cache KV).
  - Quantifier le 70B en 8 bits (environ 70 Go) introduit une confusion : un modèle quantifié n'est pas le même modèle. Il faudra le documenter.
- **E0.** 20 textes × 4 variantes × 5 répétitions = 400 notations `jev` (0 $). La génération des variantes par Llama-8B demande moins de 1 GPU-heure.
- **E1, bras 1.** 0 $. **Bras 2** : environ 5 régénérations par espèce disponible, en appels API.
- **E2.**
  - En local : N = 1 000 références × (8 graines de Llama-8B + 4 graines de Llama-70B), soit environ 12 000 générations courtes, de l'ordre de quelques GPU-heures.
  - En API : un sous-échantillon de 200 références × 3 instances × 3 familles, soit environ 1 800 appels.
  - Calibrer la difficulté des items pour que le taux d'erreur par agent se situe entre 20 et 50 %. En dessous, les corrélations d'erreurs sont instables.
- **E3.** Il réutilise les sorties d'E2 : pas de coût supplémentaire.
- **E4.** En local : 5 valeurs de k × 100 chaînes × Llama-8B. En API : confirmation sur 20 chaînes, à k = 0 et k = 8.
- **Plafond API pour E1 à E4 (illustratif).** Au plus 40 % du reste Anthropic et 40 % du reste Gemini. Le reste est inconnu (P12), et tout ce qui peut tourner sur Llama en local y passe d'abord.
- **API de littérature.** Mettre les réponses en cache. Les limites de débit ne sont pas documentées dans les faits.

---

## Séquence d'exécution (à la place d'une « loi mère » fusionnée)

1. **G0.** E0 et les tests de têtes de (c), à 0 $. Si la validité de `rigor` est falsifiée, `jev` est interdit comme fitness et seuls les vérificateurs mécaniques sont retenus.
2. **G1.** E1, bras 1, à 0 $. Puis E5 dès réception des données individuelles.
3. **G2.** E2 sur Llama, puis le sous-échantillon API.
4. **G3.** E3, interprété à la lumière d'E2.
5. **G4.** E4, puis E4b.
6. **M2 avant M1.** M2 possède un oracle mécanique, M1 n'en a pas. Pour M1, la seule référence disponible est l'arbitre humain, sur un petit échantillon noté à l'aveugle.

Une règle d'organisation de l'essaim ne s'écrit qu'après ces étapes, avec le statut HYPOTHÈSE, et uniquement pour les mécanismes qui ont survécu.

## Ce qui réfuterait la proposition B elle-même

- **Mon diagnostic de transmission.** Si les données Opus, les vagues Fable manquantes et les textes complets existent, les sections 0, P1 et P2 portent sur la transmission et non sur l'exécution. E0 à E5 restent inchangés.
- **Ma suspicion de Goodhart lexical (O3, O4).** Si E0 donne H_A, elle est falsifiée.
- **Ma lecture du plancher (O1).** Si les textes complets d'E1 bras 2 restent au plancher, l'explication par la troncature est falsifiée.
- **Mon objection à « la chimère pour vaincre H4' ».** Elle est falsifiée si E2 donne H_A et que E3 donne H_A.
- **Ma formule du composite (O3).** Si la formule réelle, une fois transmise, diffère, la thèse « composite ≈ rigor » tombe.

Cela fait cinq affirmations de B qui peuvent être réfutées par des données accessibles.

FIN-DE-CELLULE