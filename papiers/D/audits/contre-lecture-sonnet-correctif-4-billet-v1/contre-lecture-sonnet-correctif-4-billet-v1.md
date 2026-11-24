# Contre-lecture du correctif 4 du manuscrit, du billet (correctif 3) et de la page de dépôt (correctif 3)

Contre-lecteur neuf (Claude Sonnet 5.5, effort élevé). Aucun fichier du dépôt modifié. Scripts et copies de travail : `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad/verif-c4/`.

## Verdict

- Pièce 1 (manuscrit, correctif 4) : **accepté avec corrections**. Les trois affirmations mathématiques nouvelles (agrégation par strate, borne de Jensen, d_TV = q) sont exactes, y compris aux cas limites. La référence est correcte. Une phrase de l'introduction va plus loin que le manuscrit (défaut 1) ; le reste est mineur.
- Pièce 2 (billet et page de dépôt, correctif 3) : **accepté avec corrections**. La condition générale est exacte. Mais la phrase sur les procédures d'entraînement retire les réserves de la remarque `rem:algos` (défaut 6), et la page de dépôt pointe encore vers la base du correctif 3 (défaut 9).

## Défauts

### Pièce 1

**1. [à corriger] Introduction, ligne 48 de `main-v4-correctif-4.tex` : « pure rejection acts as an output filter rather than as a training signal … procedures that genuinely act in the loop realize other laws ».**
Constat. La phrase est plus forte que le manuscrit, de trois façons.
- (a) Le manuscrit dit lui-même que, dans l'opérateur A, « the filter acts as a reward bonus η⁻¹ log β » (`rem:modelA`). Un bonus de récompense est un signal d'entraînement. Ce qui est exact, c'est l'identité des lois : π_A ∝ β·π_no, soit l'entraînement non surveillé suivi d'un seul rejet à l'inférence. « Rather than as a training signal » transforme une égalité de lois en affirmation de mécanisme.
- (b) « Pure rejection » est pris sans restriction. Or `rem:modelA` donne une autre formalisation de « jeter et recommencer » (rejet répété), qui agit à chaque tour d'entraînement et ne coïncide pas avec A. L'affirmation ne vaut que pour l'opérateur A tel que modélisé.
- (c) « Procedures that genuinely act in the loop realize other laws » contredit `rem:algos` (ii) et (iii). Le filtrage de la référence et la récompense corrigée R + η⁻¹ log β sont des procédures d'entraînement et réalisent exactement la loi A. Le mot « genuinely » est en outre non défini.
Correction proposée : « At this equilibrium, pure rejection as modelled by Operator~A has the same law as unmonitored training followed by a single rejection at inference (Remark~\ref{rem:modelA}); penalized training and repeated filtering realize other laws, while some in-loop procedures realize A exactly (Remark~\ref{rem:algos}). »

**2. [mineur] Section 2.1 (`sec:reward`), ligne 72 : notations p_s, R_s, Π_s non introduites.**
Constat. Seuls p_h, p_v, p_f et Π_h, Π_v, Π_f sont définis. L'indice générique s n'est jamais déclaré. R_s apparaît sans définition (R vaut 0 sur Π_h, mais R_s n'est pas posé). La notation β̄_s := E_{π₀}[β | Π_s] est bien introduite, en ligne.
Correction proposée : ajouter « for a stratum s ∈ {h, v, f}, p_s = π₀(Π_s) and R_s denotes the constant value of R on Π_s (R_h = 0, R_v = ΔR_v, R_f = ΔR_f) ». Préciser aussi que la borne de Jensen sous B suppose, comme pour A, la récompense constante sur la strate.

**3. [mineur] Même phrase : conséquence pour l'opérateur B non dite.**
Constat. Sous B, la moyenne β̄_s ne donne qu'une borne inférieure du poids de strate. Les bornes ne sont pas uniformes d'une strate à l'autre, donc aucune inégalité entre masses de strates ne se transfère. Un lecteur peut croire que les énoncés du théorème 1 sur B restent valables avec les survies moyennes.
Correction proposée : ajouter une clause du type « the Operator-B statements below therefore assume β constant on each stratum (or R_s + C = 0) ». Cette réserve suit de la phrase déjà ajoutée et la rend utilisable.

**4. [mineur] La référence `bartok2014` n'imprime pas l'identifiant d'objet numérique.**
Constat. Le registre `papiers/D/verification-references-v1/registre-references-v2.md` (ligne 9) prescrit « …967–997, 2014, doi:10.1287/moor.2014.0663 ». Le manuscrit s'arrête à « 967–997, 2014 ».
Correction proposée : ajouter `doi:10.1287/moor.2014.0663` à l'entrée.

**5. [mineur] Phrase sur R3 (ligne 244) : lisibilité, et une précision manquante.**
Constat. La fidélité est bonne : la phrase ne dit pas que d_TV est nécessaire, et elle dit que l'hypothèse, portant sur toute politique admissible, doit venir d'une restriction de la classe. Mais une parenthèse d'une ligne et demie sépare « which holds unconditionally » de « then any policy ». Elle contient un point-virgule, un « so that » et un « whereas » à l'intérieur de tirets cadratins. De plus, avec d_TV = q, seule la condition τ_min > q donne la garantie. Les cheaters de taux ≤ q restent non exclus, ce qui est cohérent avec le plancher des attaques rares (la remarque sur R3 le dit déjà).
Correction proposée : sortir ces deux phrases en une phrase distincte après l'énoncé, ou ajouter « (so δ_ind = q suffices, and cheating rates ≤ q remain unexcluded, as in Remark~R3) ».

**6. [mineur] Le script du correctif 4 n'est pas cité dans le manuscrit.**
Constat. La note de bas de page (`\thanks`) cite `verifier_exemples_papier_v4_correctif_1.py` et `verifier_correctif_3_v1.py`, mais pas `verifier_correctif_4_v1.py`. La section `sec:verif` ne mentionne pas non plus ses deux vérifications (agrégation, mélange).
Correction proposée : ajouter le script à la note et une ligne à `sec:verif`.

**7. [mineur, hors périmètre du correctif, préexistant] Preuve de la partie 3 (R3).**
Constat. L'énoncé suppose seulement |E_ord τ − E_trap τ| ≤ δ_ind pour toute politique admissible. La preuve passe par « ≤ d_TV ≤ δ_ind ». Elle ne traite donc que la voie par la variation totale. L'autre voie est immédiate (c'est l'hypothèse), mais la preuve ne le dit pas.
Correction proposée : ajouter « (under the hypothesis itself, this step is immediate) ». À traiter plus tard si l'on veut.

### Pièce 2

**8. [à corriger] Billet (item 4 du résumé du théorème 1) et page de dépôt (item 1) : réserves de `rem:algos` perdues.**
Constat. Le billet écrit « pure rejection is realized exactly by unmonitored training followed by rejection sampling at inference, by training against a monitor-filtered reference, or by the corrected reward R + η⁻¹ log β ». Le manuscrit dit trois choses de plus :
- (a) construire la référence filtrée en ajustant sur des échantillons acceptés n'y parvient qu'à la limite idéale ;
- (b) la récompense corrigée exige la survie par trajectoire β(π), pas seulement un verdict binaire, et là où β = 0 c'est une contrainte de support, non une récompense ;
- (c) tout est établi à l'optimum de Gibbs. Une méthode de gradient réelle ne l'approche qu'à la convergence et avec assez de capacité.
Sans ces réserves, un praticien peut croire qu'un moniteur binaire placé dans une boucle d'entraînement réalise « exactement » le rejet pur. C'est le point de lecture le plus risqué de la phrase, et il va plus loin que le manuscrit.
Correction proposée, en une clause de plus : « at the Gibbs optimum; the filtered reference is exact only in the ideal limit, and the corrected reward needs the survival probability β(π), not a binary verdict ».

**9. [à corriger avant dépôt] Page de dépôt, section Files : base encore le correctif 3 avec erratum 1.**
Constat. La page cite `manuscrit-arxiv/main-v4-correctif-3-erratum-1.tex` et la commande `pdflatex main-v4-correctif-3-erratum-1.tex`. La base passe au correctif 4.
Correction proposée :
- remplacer par `main-v4-correctif-4.tex` (et son PDF) dans les deux endroits ;
- ajouter `verifier_correctif_4_v1.py` et `exemples-verifies-correctif-4-v1.json` à la ligne des scripts ;
- aligner la mention « revised after an independent audit and a fidelity review » sur le manuscrit (« two fidelity reviews », correctif 4).
Selon R12, publier sous un nouveau nom (`README-v4-correctif-4.md`, billet idem), jamais en écrasant.

**10. [mineur] Phrase sur les procédures : deux imprécisions.**
Constat.
- (a) « Dropping them from an on-policy batch normalized by its full size is the penalty at C = 0 » omet « without baseline » et « the KL term being evaluated on the whole policy ». Avec une base constante b soustraite, le manuscrit donne B à C = −b. Le cas du lot rempli de survivants (récompense rescalée par 1/E[β], ni A ni B à pression inchangée) n'est pas signalé.
- (b) La phrase précédente demande de lire C comme l'écart R₀ + C, puis « C = 0 » apparaît sans qualification. Le manuscrit dit « raw score 0, hence C = 0, gap R₀ ». Ici « C = 0 » désigne le score brut, pas l'écart.
Correction proposée : écrire « scored 0, i.e. raw C = 0 (gap R₀) » et ajouter « without baseline, KL on the whole policy ».

**11. [mineur] Lisibilité et placement dans le billet.**
Constat. Trois sujets sont empilés dans un seul paragraphe de l'item 4 « niche parfaite » : la niche, la normalisation et les procédures. La phrase sur les procédures concerne les deux opérateurs en général, pas la niche. Elle serait mieux placée en section 2, après « Why Operator A is a choice, not a law ». Par ailleurs, la section 2 du billet pose toujours « C ≥ 0 » alors que l'écart R₀ + C peut être négatif. Le manuscrit précise que la forme de Gibbs vaut pour tout C réel et que les énoncés « C ≥ 0 » s'appliquent à l'écart seulement s'il est positif.
Correction proposée : déplacer la phrase sur les procédures en section 2, et ajouter une clause « (the gap may be negative; the Gibbs form holds, statements assuming C ≥ 0 apply to the gap only when non-negative) ».

**12. [mineur] Le billet ne reprend aucune des trois clarifications du correctif 4.**
Ni le filtre de sortie, ni la borne de Jensen, ni la précision sur R3. Ce n'est pas exigé. Mais le billet R3 dit « If d_TV ≤ δ_ind », forme plus étroite que l'hypothèse du manuscrit, alors que la voie par la variation totale n'est que suffisante. Un demi-mot suffirait (« for instance if … »).

## Ce qui a été vérifié et tient

**Référence `bartok2014`.**
- Crossref, DOI 10.1287/moor.2014.0663 : « Partial Monitoring—Classification, Regret Bounds, and Algorithms », Mathematics of Operations Research, vol. 39, no 4, pp. 967–997, novembre 2014. Les cinq auteurs correspondent (Bartók, Foster, Pál, Rakhlin, Szepesvári).
- arXiv:1102.2041 résout (interface d'arXiv) vers « Toward a Classification of Finite Partial-Monitoring Games » (Antos, Bartók, Pál, …). C'est bien un autre article.
- Le diff avec `main-v4-correctif-3-erratum-1.tex` ne contient exactement que les quatre changements annoncés (plus la note de bas de page).

**Agrégation par strate sous A.**
- Le poids ∫_{Π_s} β e^{ηR} dπ₀ = p_s β̄_s e^{ηR_s} est exact quand R est constant sur la strate, y compris avec β = 0 sur une partie (essai à la main : 4,712308 des deux côtés).
- Script du dépôt : erreur relative maximale 5,7·10⁻¹⁶ sur 20 000 tirages.

**Borne de Jensen sous B.**
- Le poids est p_s E[exp(η(β(R_s+C) − C))], c'est-à-dire l'espérance d'une exponentielle d'une fonction affine de β. Cette fonction est convexe quelle que soit la signe de R_s + C, car η > 0. La borne inférieure p_s e^{η[β̄R_s − (1−β̄)C]} est donc vraie dans les deux signes. Il n'y a pas de renversement du sens de l'inégalité.
- L'égalité a lieu si β est presque sûrement constant sur la strate, ou si R_s + C = 0. Dans ce second cas les deux côtés valent p_s e^{−ηC}.
- Mon propre essai, 100 000 tirages avec β ∈ {0, ½, 1} dans la moitié des cas, R_s et C dans [−6, 6] : 0 violation, et l'inégalité est stricte dans 75 000 cas où β n'est pas constant et R_s + C ≠ 0.
- Script du dépôt : 0 violation sur 20 000 tirages, 4 000 cas d'égalité corrects. Il n'échantillonne que β ∈ (0, 1) ; le cas limite est couvert par mon essai.

**Pièges par mélange, d_TV = q.**
- Si P_trap = (1−q)P_ord + qQ avec Q singulière par rapport à P_ord, alors d_TV(P_ord, P_trap) = q·d_TV(P_ord, Q) = q.
- Vérifié par le script (écart maximal 3,3·10⁻¹⁶ sur 5 000 tirages) et par mon essai à q ∈ {0, 0,3, 1}.
- Le cas support disjoint : d_TV = 1, hors du domaine δ_ind ∈ [0, 1). Avec une classe de politiques non restreinte, la politique qui triche exactement sur les contextes de piège donne un écart de 1. L'hypothèse du théorème est donc fausse sans restriction de la classe. La phrase du correctif le dit fidèlement et ne présente pas d_TV comme nécessaire.

**Condition générale du billet.**
- η(1−β_v)(R₀+ΔR+C) > log(1/β_v) est équivalente à η(ΔR+C) > log(1/β_v)/(1−β_v) avec C remplacé par l'écart R₀ + C. Elle découle de la normalisation de `sec:reward`.
- Dérivation à la main : les cotes furtif/honnête sont égales sous A et sous B, et la comparaison se réduit à B < A sur le poids de la strate visible.
- Contrôle numérique indépendant : 200 000 tirages (R₀ ∈ [−3, 3], C ∈ [−3, 5], β_v ∈ (0,1), η, p aléatoires) : 0 désaccord entre la condition et la comparaison directe des masses π_B(Π_f) et π_A(Π_f).
- Le manuscrit énonce la même condition (`sec:reward`). Le billet et la page sont fidèles sur ce point.

**Compilation.** Deux passes de `pdflatex` sur une copie : 12 pages, 0 référence indéfinie, 0 « ?? » dans le texte du PDF. Deux surcharges de boîte (9,9 pt et 3,8 pt, lignes 191 et 238–240), sans rapport avec le correctif. Le texte extrait du PDF livré est identique au mien.

**Script et empreintes.** Le script relancé sur une copie redonne exactement le JSON du dépôt (graine 202611241640). Les empreintes `.sha256` du `.tex`, du PDF, du script, du JSON, du billet et de la page sont toutes valides.

**Fichiers cités par la page de dépôt.** Tous existent dans le dossier de publication : `manuscrit-arxiv/main-v4-correctif-3-erratum-1.tex`, `verifier_exemples_papier_v4_correctif_1.py`, `exemples-verifies-papier-v4-correctif-1.json`, `verifier_correctif_3_v1.py`, `exemples-verifies-correctif-3-v1.json`. Les fichiers du correctif 4 existent mais ne sont pas cités (défaut 9).

**Fidélité du billet à `rem:algos` et `sec:reward`.** Le billet reprend correctement :
- l'équivalence « masquer la récompense = B à C = 0, pas A » ;
- les trois réalisations exactes de A ;
- le renvoi à la remarque.
Les réserves manquantes sont celles des défauts 8 et 10.
