# Vérification des corrections (correctif 5, commit 9587940b)

Contre-lecteur : Claude Sonnet 5.5. Aucun fichier du dépôt modifié. Recompilation sur copie : `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad/verif-c5/tex/`.

## Verdict

**Accepté avec corrections mineures.** Les douze défauts sont traités : onze entièrement, le défaut 10 partiellement. Aucun défaut bloquant. Quatre défauts nouveaux, tous mineurs :
- une ligne qui déborde de 49 pt dans le PDF (A) ;
- une notation `R_0` utilisée dans le billet avant sa définition (B) ;
- une clause « statements on Operator B » un peu large (C) ;
- une virgule manquante dans la note de bas de page (D).

Compilation : deux passes de `pdflatex`, 12 pages, 0 référence indéfinie, 0 « ?? ». Le texte du PDF livré est identique à ma compilation. Les quatre empreintes `.sha256` du correctif 5 (`.tex`, PDF, billet, page de dépôt) sont valides. Le commit n'ajoute que les huit fichiers du correctif 5. Les fichiers cités par la page existent.

## Défaut par défaut

1. **Introduction : traité.** La formulation est reprise. Elle dit « pure rejection as modelled by Operator A », « penalized training and repeated filtering realize other laws, while some in-loop procedures realize Operator A exactly ». C'est cohérent avec `rem:modelA` et `rem:algos` (ii) et (iii). La contradiction avec le « reward bonus » a disparu.
2. **Notations : traité.** `s ∈ {h, v, f}`, `p_s = π₀(Π_s)` et `R_s` (« when R is constant on Π_s », avec `R_h = 0`, `R_v = ΔR_v`, `R_f = ΔR_f`) sont définis avant leur emploi, `ΔR_v` l'étant dès la ligne 66. `β̄_s` était déjà défini.
3. **Conséquence pour B : traité, avec une réserve (voir C).** La clause « these lower bounds are not uniform across strata, no comparison between stratum masses transfers » est exacte et suffit pour ce que je demandais.
4. **Identifiant d'objet numérique : traité.** Le DOI est ajouté à l'entrée `bartok2014`, sous la forme du registre.
5. **R3, supports disjoints et mélange : traité.** La parenthèse est redevenue la phrase d'origine, et le texte nouveau est placé après `eq:R3`, dans le même point de l'énumération. Ce qu'il dit est exact et fidèle à l'hypothèse :
   - supports disjoints : `d_TV = 1`, la voie par la variation totale ne donne rien, l'hypothèse doit venir d'une restriction de la classe ;
   - mélange : `d_TV = q`, donc `δ_ind = q` suffit, et les taux ≤ q ne sont pas exclus ;
   - la nouveauté de R3 n'est pas jugée, comme demandé.
6. **Scripts cités : traité.** La note de bas de page cite les trois scripts (voir D). La section `sec:verif` a une phrase qui décrit fidèlement ce que fait chacun des deux scripts ajoutés. Mais cette phrase déborde (voir A).
7. **Preuve de R3 : traité.** « Under the hypothesis itself, τ_trap ≥ τ_ord − δ_ind is immediate » est exact : |E_ord τ − E_trap τ| ≤ δ_ind donne directement E_trap τ ≥ E_ord τ − δ_ind. La voie par la variation totale suit comme cas particulier. La suite de la preuve est inchangée et reste correcte.
8. **Réserves de `rem:algos` : traité.** Billet et page disent maintenant :
   - « at the Gibbs optimum; gradient methods approach it only at convergence and with enough capacity » ;
   - référence filtrée « exact only in the ideal limit of fitting on accepted samples » ;
   - récompense corrigée : survie par exécution β(π), pas un verdict binaire, et « support constraint » là où β = 0.
   Toutes ces réserves sont fidèles au manuscrit.
9. **Page de dépôt : traité.**
   - La base est `main-v4-correctif-5.tex`, avec la commande `pdflatex` correspondante ;
   - `verifier_correctif_4_v1.py` et son JSON sont ajoutés ;
   - la mention est « v4, corrective 5 … two fidelity reviews ».
   Les fichiers cités existent tous.
10. **Procédures, deux imprécisions : traité partiellement.**
    - Traité : « raw score 0, i.e. raw C = 0, gap R_0 » ; « without baseline and with the KL term on the whole policy » ; « a constant baseline b … gives raw C = −b », qui concorde avec le manuscrit.
    - Non repris : le cas du lot rempli de survivants, que je citais en (a) (récompense rescalée par 1/E[β], ni A ni B à pression inchangée). Le billet ne l'affirme pas à tort. C'est une omission acceptable, que je laisse à ton arbitrage.
    - Nouvelle imprécision (mineure) : « Iterated filter-then-fine-tune realizes repeated rejection » omet que l'étape est un pas de RL régularisé par KL de taille η₁. Le fine-tuning supervisé seul (η₁ = 0) en est un cas particulier, ce qui reste exact. Suggestion : « Iterating filter, then a KL-regularized step of size η₁ (η₁ = 0: supervised fine-tuning on survivors), realizes repeated rejection ».
11. **Placement en section 2 et écart négatif : traité, avec une réserve (voir B).** La phrase est bien en section 2, après « Why Operator A is a choice ». La clause « The gap R₀ + C may be negative … apply to the gap only when it is non-negative » est ajoutée à l'item 4 et correspond au manuscrit.
12. **R3 dans le billet et la page : traité.** « If no admissible policy can tell traps from ordinary episodes by more than δ_ind (for instance if d_TV ≤ δ_ind …) » est fidèle à l'hypothèse du théorème. La voie par la variation totale est bien présentée comme exemple.
    - Remarque de forme : « traps with support disjoint from ordinary episodes have d_TV = 1 » est lâché sans conséquence dite. Un lecteur peut ne pas voir que cela signifie que cette voie ne donne rien.
    - Suggestion : ajouter « so that route then gives nothing ».

## Défauts nouveaux

**A. [mineur, à corriger] Manuscrit, `sec:verif`, lignes 282–283 : débordement de 49 pt.**
Constat. `pdflatex` signale `Overfull \hbox (49.39pt too wide) in paragraph at lines 282--283`. La ligne contenant `\texttt{verifier\_correctif\_3\_v1.py}` dépasse dans la marge à la page 10, le nom de fichier ne pouvant pas être coupé. Les deux autres surcharges (9,9 pt et 3,8 pt) existaient déjà dans le correctif 4 et ne sont pas liées.
Correction proposée : le même motif que l'existant dans la même section (`verifier\_\allowbreak correctif\_\allowbreak 3\_\allowbreak v1.py`) ou une reformulation qui place le nom en début de ligne.

**B. [mineur] Billet, section 2 : `R_0` et « gap » utilisés avant d'être définis.**
Constat. Le nouveau paragraphe « Which training procedures realize each operator » est en section 2 et parle de « gap R_0 » et de « raw C ». Mais `R_0` n'est défini que plus loin (section 3, item 4 : « with an honest reward R_0 ≠ 0, read C as the gap R_0 + C »). En section 2 la normalisation est à 0 sur l'honnête, donc R_0 est inconnu du lecteur à ce stade.
Correction proposée : une demi-phrase à la première occurrence : « (R_0 is the honest reward when it is not normalized to 0, see Section 3, item 4) ». Ou déplacer les mots « gap R_0 » après la définition.

**C. [mineur] Manuscrit, `sec:reward` : clause sur B un peu large.**
Constat. « the statements on Operator~B below take β constant on each stratum » est trop général. Théorème 2, R2 sous B porte sur une strate iso-récompense où β_loop varie, et R3 est un modèle contextuel. Ce ne sont pas des énoncés « à β constant par strate ».
Correction proposée : « the three-stratum statements on Operator~B below (Theorem~\ref{thm:selection} and Regime~R1) take β constant on each stratum ».

**D. [mineur] Manuscrit, note de bas de page : virgule manquante.**
Constat. La liste de scripts est devenue « A.py B.py and C.py » (séparés par une espace, sans virgule après le premier).
Correction proposée : ajouter la virgule après `verifier\_exemples\_papier\_v4\_correctif\_1.py`.

## Ce qui a été revérifié et tient

- Le diff `main-v4-correctif-4.tex` → `main-v4-correctif-5.tex` ne contient que les modifications listées (notes de bas de page, introduction, `sec:reward`, énoncé et preuve de R3, phrase de `sec:verif`, DOI).
- Les billet et page de dépôt ne contiennent que les changements annoncés par rapport aux versions du correctif 3.
- Les formules sont inchangées. La condition η(1−β_v)(R₀+ΔR+C) > log(1/β_v) vérifiée à la contre-lecture précédente (200 000 tirages, 0 désaccord) est toujours reprise telle quelle.
- La phrase de contribution sur R3 n'a pas été touchée, comme convenu.
