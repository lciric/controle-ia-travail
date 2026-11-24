# Antériorité du régime des pièges indiscernables (R3) : lecture de Gans et Holden et de « Blindfold » (v1)

Pièce de travail (classe C), non contre-lue. Lecteur neuf : Opus 5.5, effort élevé. Aucun fichier du dépôt modifié.

## Verdict

La nouveauté de R3 est à resserrer. Ses deux ingrédients sont publiés. (i) Quand δ_ind = 0, le seuil C*_R3 est exactement le seuil de dissuasion de l'audit au hasard écrit par Gans et Holden pour des agents d'intelligence artificielle. Ces auteurs donnent aussi la version « signal bruité sur le tirage », dont R3 est la variante additive. (ii) L'inégalité τ_ord − τ_trap ≤ δ_ind, par la variation totale, est le « lemme pont » de « Blindfold ». Ce texte s'en sert déjà en faveur du défenseur et décrit déjà la limite des violations rares, mais pour **estimer** un taux et non pour **dissuader**.

Ce qui reste propre au manuscrit est mince et doit être dit comme tel. C'est la transposition de l'estimation à la dissuasion sous une indiscernabilité mesurée en variation totale : un seuil de pénalité explicite, valable seulement pour les tricheurs fréquents, et le plancher qu'il laisse. Le cadre de Gibbs régularisé par Kullback-Leibler est absent des deux textes. Mais la preuve de R3 ne s'en sert pas : c'est une comparaison de récompenses espérées sous le score de l'opérateur B.

## 0. Sources et empreintes

| Texte | Fichier | Empreinte (vérifiée, `sha256sum -c` : OK) | Pages lues |
|---|---|---|---|
| Gans, Holden, « When Does Randomized Oversight Align AI Agents That Can Conceal? », arXiv:2609.38262v1 | `docs/notes/percee-apres-blindfold-v1/opus-max-v1/sources/2609.38262v1.pdf` | `e28a4e8d6747cf4dc4c0c3433836f5e29b1ab5e235be3176841ee9c4db4ed7a7` | p. 1 à 29 en entier ; p. 30 à 49 (preuves, références, annexe en ligne) par recherche de mots |
| Zhu, Zuo, Sun, « Blindfold: Keeping the Audit Coin Secret from LLM Agents », arXiv:2610.37055v1 | `.../sources/2610.37055v1.pdf` | `5250fa1176ac804ba32fd4998fa47b2f278757ce9393a1443d4b9a7b8617f861` | p. 1 à 8 et 12 à 13 en entier ; p. 15 à 18 (positionnement, preuves) en partie ; expériences des p. 9 à 11 survolées |
| Manuscrit, `main-v4-correctif-4.tex` | `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/manuscrit-arxiv/` | compagnon `.sha256` : OK | introduction (contribution 3), cadre, théorème `thm:escape` (3) et sa preuve, remarque sur la dualité, limites |
| Section sur le budget d'audit, `audit-budget-section-v1-correctif-5-erratum-1.tex` | `papiers/D/theorie/brouillon-fable-budget-audit-v1/` | compagnon `.sha256` : OK | l. 551 à 600 (proposition `prop:audit-indist`) et l. 627 à 632 (positionnement) |

Les textes ont été extraits avec `pdftotext -layout`, avec une marque de page par saut de page. Les extraits et le script de vérification sont dans `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad/lecture-r3/`. Les numéros de page sont ceux du PDF, c'est-à-dire ceux imprimés en pied de page pour Gans et Holden.

## 1. Les deux textes

### 1.1 Gans et Holden : dissuader par l'audit au hasard un agent qui peut dissimuler

- **Question** : quand des audits au hasard et des règles de notation qu'un agent comprend rendent-ils la conduite autorisée préférable à la faute ? Et que deviennent les agents qui fautent quand même (p. 2) ?
- **Modèle** (p. 6 à 8).
  - Un agent de type θ, dans un espace compact. Il choisit une action autorisée ou l'une des K voies non autorisées, et un niveau de dissimulation h de coût c_i(θ,h).
  - L'évaluateur i est tiré avec la probabilité p_i ; il détecte avec la probabilité d_i(θ,h) et inflige une perte F_i (éq. 2 à 4, p. 7).
  - Le fournisseur s'engage sur la loterie et sur les sanctions. Le tirage a lieu **après** l'action : sa loi est publique, sa réalisation inconnaissable (p. 7). C'est la forme de base de l'indiscernabilité.
  - « authorized behavior is never sanctioned » (p. 7).
  - Lecture « entraînement » explicite : « In training, the agent is a policy evaluated by a specified objective, and a sanction is a deduction that changes how policies are ranked » (p. 6). Le fournisseur écrit l'objectif et peut donc choisir des sanctions sans plafond (section 4.2, p. 13).
- **Résultats principaux.**
  - Proposition 1 (p. 8) : un audit plus fort dissuade, mais il accroît la dissimulation chez ceux qui fautent encore.
  - Proposition 2 (p. 10 et 11) : le taux de prise de ceux qui fautent encore peut baisser, et leur dommage monter.
  - Proposition 3 et éq. 11, 12, 14 (p. 11 et 12) : il faut p_i ≥ a_i(0) = sup (g_i − c_i)/(F_i d_i). C'est la règle de Becker calculée après adaptation : « expected sanctions must cover the largest private gain on each channel » (p. 12).
  - Proposition 4 (p. 13) : avec des sanctions qu'on peut choisir à volonté, des audits rares dissuadent tous les types dès que les seuils t̄_i sont finis ; « any F_i ≥ K t̄_i/B suffices ». Si un seuil est infini, aucune sanction n'y suffit.
  - Corollaire 1 (p. 14) : les leviers hors audit, à savoir un crédit pour l'arrêt et une dissimulation plus chère ou impossible.
  - Proposition 5 (p. 15 et 16), quand l'agent peut apprendre le tirage :
    - (a) si l'apprendre coûte φ, la probabilité d'audit a un **plancher** qui ne baisse pas avec la sanction, Σp_i ≥ 1 − φ/g* ;
    - (b) si le gain dépasse φ sur deux canaux, rien ne dissuade ;
    - (c) **si l'agent observe un signal bruité σ dont la loi dépend du tirage**, des sanctions finies dissuadent tous les types si et seulement si la probabilité d'audit a posteriori p_i(σ) est positive pour tout signal. « A noisy signal raises the required sanction from t̄_i/p_i to t̄_i/min_σ p_i(σ) but does not prevent deterrence, whereas a signal that rules out the audit of a tempting channel defeats every sanction » (p. 16). Le lien est fait avec la conscience d'évaluation (Needham et al., p. 8 et 16).
  - Propositions 6 à 9 (p. 17 à 23) : notation au hasard, objectif sensible au risque, arrêt et révélation. Hors de R3.
- **Hypothèses** : un agent seul, aux croyances justes, qui maximise une utilité espérée (p. 7 et 26). Des types compacts et des fonctions continues. Aucune dynamique d'apprentissage, aucun équilibre régularisé, aucun taux de triche par contexte : à type et signal fixés, l'agent fait un seul choix.

### 1.2 « Blindfold » : garder secrète la pièce de l'audit pour que le taux certifié reste valide

- **Question** : un certificat de taux de violation fondé sur l'audit d'une fraction ε d'épisodes, pondéré par l'inverse de la probabilité d'audit, reste-t-il valide si l'agent peut deviner, même avec du bruit, qu'un épisode est audité ? Les auteurs l'écrivent : « Our question is not whether the agent still misbehaves when watched. It is whether the number the certifier reports still means anything » (p. 1).
- **Modèle** (p. 2 et 3).
  - Une pièce d'audit B tirée selon une loi de Bernoulli de paramètre ε, et une tentative V ∈ {0,1}.
  - L'agent agit sur sa vue d'avant l'engagement, W = (O, ξ), qui contient ses observations et son propre aléa.
  - L'indiscernabilité de l'audit est mesurée par **D_A, la variation totale entre les lois de la vue sous B = 1 et sous B = 0**, prise au pire sur les politiques et les histoires atteignables (définition 1, p. 3).
  - Adversaire adaptatif d'un épisode à l'autre. Les motifs de l'agent restent indéterminés (p. 3).
- **Résultats principaux.**
  - Lemme 2, le « lemme pont » (p. 4) : **µ0 − µ1 ≤ min{D_A, µ0, 1 − µ1}**, où µ0 est la propension à tenter hors audit et µ1 sous audit. La borne est atteinte par le test de rapport de vraisemblance.
  - Théorème 1 (p. 4 et 5) : le biais au pire vaut (1 − ε)D_A.
  - Corollaire 2 (p. 5) : « Raising ε is therefore the expensive lever ». Le biais ne décroît que linéairement en ε.
  - Théorème 4 (p. 5) : la non-interférence avant l'engagement (D_A = 0) est nécessaire et suffisante pour un certificat sans biais.
  - Théorème 5 (p. 6) : si le mécanisme garantit D_A ≤ δ, le certificat gonflé de (1 − ε)δ est valide pour tout adversaire adaptatif.
  - Théorème 6 (p. 6) : l'ensemble identifié pour µ0 est [max(0, µ1 − δ), µ1 + min(δ, 1 − µ1)], et aucune procédure qui ne voit que les étiquettes auditées ne fait mieux.
  - Sur les violations rares (p. 6) : « The additive inflation (1−ε)δ makes the certificate near-vacuous below that base rate ». La forme multiplicative de la proposition 6, par la divergence dite « en crosse de hockey », ne l'est pas : µ0 ≤ e^η µ1 + E_η (énoncé et preuve p. 17 et 18). En pratique : « Below a base rate of about 0.05 only the multiplicative form serves » (p. 12).
  - Constructions (proposition 4, p. 7) : branche muette, pièce neuve à chaque appel, leurres. Les leurres sont des invites d'apparence d'audit montrées à un taux indépendant de B ; D_A vaut alors zéro (p. 7).
  - Majorer D_A demande une construction : « for high-dimensional transcripts no distribution-free finite-sample upper bound on total variation exists » (p. 8).
- **Hypothèses** : la restriction d'exclusion, B n'agit sur V qu'à travers la vue (p. 4). La pièce, le certificateur et l'oracle d'étiquettes sont de confiance. Une violation cachée à l'auditeur lui-même est hors champ (p. 3). Aucune sanction, aucune incitation, aucun entraînement : l'agent est quelconque.
- **Ce que les auteurs disent eux-mêmes de leur nouveauté.** Le lemme 2 est la forme variationnelle de la variation totale, qu'ils marquent comme classique (p. 2 ; tableau IX, p. 17). Leur tableau VIII (p. 16) range Gans et Holden comme l'œuvre « deterrence », sans « sharp price », et se range lui-même comme l'œuvre d'estimation.

## 2. Confrontation à R3, point par point

Rappel de R3 (manuscrit, théorème `thm:escape`, partie 3). Les contextes suivent un mélange (1 − ρ)P_ord + ρP_trap. Hypothèse : pour toute politique admissible, |E_ord τ − E_trap τ| ≤ δ_ind, ce qui vaut si d_TV(P_ord, P_trap) ≤ δ_ind. Alors toute politique telle que τ_ord ≥ τ_min > δ_ind a une récompense espérée strictement inférieure à l'honnête sous l'opérateur B dès que C > C*_R3. La remarque qui suit présente ce résultat comme un retournement de la borne en variation totale en faveur du défenseur, et nomme un plancher : τ_ord ≤ δ_ind n'est pas exclu.

**(a) « Des audits indiscernables des épisodes ordinaires rendent la triche fréquente non rentable. » Occupé dans l'idée, partiellement occupé dans la forme quantitative.**
- L'idée qu'un audit que l'agent ne peut pas prévoir dissuade un agent maximisateur est publiée pour des agents d'intelligence artificielle par Gans et Holden. Le tirage a lieu après l'action (p. 7), des audits rares dissuadent tous les types (proposition 4, p. 13), et la condition « draw cannot be learned » figure dans le résumé (p. 1).
- L'indiscernabilité **partielle** y figure aussi, sous forme bayésienne : un signal bruité sur le tirage (proposition 5(c), p. 15 et 16).
- « Blindfold » énonce l'inégalité de comportement sous indiscernabilité partielle (lemme 2, p. 4), mais pour l'estimation. Il précise lui-même ne pas poser la question de la dissuasion (p. 1).
- Ce qui n'est dans aucun des deux : l'indiscernabilité mesurée en **variation totale** et versée dans une condition de **dissuasion**, avec une garantie restreinte aux taux de triche τ_ord ≥ τ_min.
- Les épisodes « plantés » distincts des épisodes ordinaires, plutôt que des audits des mêmes épisodes, ne changent rien aux mathématiques : c'est un mélange de deux lois étiquetées. « Blindfold » cite des prédécesseurs anciens de la vérification cachée en sécurité, les « ringers » et les pots de miel (p. 1 et 13). Je ne les ai pas lus.

**(b) La borne par la variation totale « retournée en faveur du défenseur ». Occupé, pour la certification.**
- « Blindfold » emploie exactement cette inégalité pour garantir le défenseur : le théorème 5 (p. 6) rend valide un certificat dès que D_A ≤ δ.
- Il la qualifie de classique (forme variationnelle de la variation totale, Neyman-Pearson, tableau IX, p. 17).
- Notre inégalité τ_ord − τ_trap ≤ δ_ind et leur µ0 − µ1 ≤ D_A (p. 4) ont la même forme, au changement de notation près. τ_ord tient le rôle de µ0, τ_trap celui de µ1, la vue de l'agent celui du contexte, et l'hypothèse « pour toute politique admissible » répond au supremum sur les politiques de leur définition 1 (p. 3).
- La phrase du manuscrit qui l'oppose à l'usage « classique » de la variation totale contre les moniteurs reste exacte pour ce dernier usage. Mais elle laisse croire que le retournement est neuf, ce qu'il n'est plus. Reste libre seulement son emploi en faveur de la **dissuasion**.

**(c) Le seuil explicite C*_R3, ou un équivalent. Partiellement occupé.**
- À δ_ind = 0, C*_R3 = [(1 − ρ) + ρε_trap] ΔR / [ρ(1 − ε_trap)]. C'est mot pour mot la condition de Gans et Holden g ≤ pFd (éq. 11 et 12, p. 11 et 12), avec g = ΔR, p = ρ, d = 1 − ε_trap, et une perte en cas de prise F = ΔR + C (forfaiture plus pénalité).
- Vérifié en arithmétique exacte sur trois jeux de paramètres. Script : `lecture-r3/verif_seuil_r3_v1.py`. Il retrouve aussi C*_R3 = 5,462585 de l'exemple du manuscrit.
- Que la sanction puisse être écrite dans l'objectif d'entraînement, et donc sans plafond, est aussi chez eux (p. 6 et 13).
- L'équivalent pour l'indiscernabilité partielle existe chez eux sous forme multiplicative : la sanction requise passe de t̄/p à t̄/min_σ p(σ) (p. 16).
- Est libre la forme additive en variation totale, c'est-à-dire le facteur τ_min/(τ_min − δ_ind) et le terme en ε_trap(τ_min − δ_ind). Dans l'exemple du manuscrit, ce facteur ne pèse que ×1,33 sur le seuil à δ_ind = 0 [calcul, même script].

**(d) Le plancher des attaques rares (τ_ord ≤ δ_ind non exclus). Partiellement occupé : sa forme d'estimation et son mécanisme de dissuasion sont publiés, pas sa forme additive de dissuasion.**
- « Blindfold » publie la contrepartie pour l'estimation. Avec une indiscernabilité additive δ, aucun taux sous δ n'est identifiable à partir des étiquettes auditées (théorème 6, p. 6). Le certificat est « near-vacuous below that base rate » (p. 6) et seule la forme multiplicative sert sous 0,05 environ (p. 12).
- Gans et Holden publient le mécanisme côté dissuasion : un signal qui exclut l'audit « defeats every sanction » (p. 16). Le plancher de R3 est le même phénomène, puisque la politique triche seulement là où P_trap est faible, et donc là où la probabilité a posteriori d'un piège est faible.
- Leur plancher de la proposition 5(a) (p. 15) est un autre objet : une borne basse sur la **probabilité d'audit** quand l'agent apprend le tirage exactement, pour un coût φ.
- **Réserve de fond.** Les deux textes montrent que ce plancher tient à la mesure **additive** de l'indiscernabilité, et non à l'indiscernabilité elle-même.
  - Chez Gans et Holden, signal fini : si la probabilité a posteriori d'un piège est minorée par un nombre positif pour tout contexte, une pénalité finie dissuade toute triche, même rare (proposition 5(c), p. 15).
  - Chez « Blindfold », la forme en crosse de hockey donne µ0 ≤ e^η µ1 + E_η (p. 6, 17 et 18). Transposée à R3, elle donne τ_trap ≥ e^(−η)(τ_ord − E_η), donc un plancher E_η qui peut être bien inférieur à δ_ind = E_0 [calcul, non vérifié par programme].
  - Le mot « irreducible » des limites du manuscrit n'est donc juste que sous la seule hypothèse de variation totale. Sous cette hypothèse, la politique qui triche à taux δ_ind sur la part de P_ord que P_trap ne charge pas atteint bien le plancher.

**(e) Le cadre de l'entraînement : équilibre de Gibbs régularisé par Kullback-Leibler, moniteur dans la boucle, opérateur de pénalité. Libre dans les deux textes, mais peu employé par R3.**
- Aucun des deux textes ne contient d'équilibre de Gibbs ni de régularisation par Kullback-Leibler (recherche de mots sur les deux textes intégraux, aucune occurrence pertinente).
- Gans et Holden emploient un objectif entropique sensible au risque, sans régularisation vers une référence (p. 17).
- « Blindfold » cite la divergence de Kullback-Leibler seulement pour composer des fuites d'une étape à l'autre (proposition 1, p. 5).
- En revanche, la lecture de la pénalité comme « deduction that changes how policies are ranked » en entraînement est chez Gans et Holden (p. 6). C'est l'esprit de l'opérateur B.
- Surtout, la partie 3 du théorème ne dit rien de la masse de Gibbs. Elle compare des récompenses espérées R̄_C, et la remarque du manuscrit précise que R3 « does not make honesty the Gibbs optimum ». Le cadre de Gibbs est donc le décor de R3, pas son contenu.
- Un corollaire qui en ferait usage, par exemple une décroissance exponentielle en η de la masse des tricheurs fréquents relativement à l'honnête, serait facile à écrire, mais il n'est pas dans le manuscrit.

Synthèse :

| Point | État | Où |
|---|---|---|
| (a) indiscernabilité → triche fréquente non rentable | idée occupée ; forme en variation totale pour la dissuasion libre | Gans et Holden p. 7, 13, 15 et 16 ; « Blindfold » p. 1 et 4 |
| (b) variation totale en faveur du défenseur | occupé (certification) ; libre pour la dissuasion | « Blindfold » lemme 2 p. 4, théorème 5 p. 6, tableau IX p. 17 |
| (c) seuil C*_R3 | partiellement occupé (identique à δ_ind = 0 ; variante bayésienne publiée) | Gans et Holden éq. 11 et 12 p. 11 et 12, prop. 4 p. 13, prop. 5(c) p. 15 et 16 |
| (d) plancher des attaques rares | partiellement occupé (forme d'estimation ; mécanisme de dissuasion) | « Blindfold » théorème 6 p. 6, p. 12 ; Gans et Holden p. 16 |
| (e) cadre de Gibbs et de Kullback-Leibler | libre, mais non employé par la preuve de R3 | aucun des deux ; Gans et Holden p. 6 pour la pénalité vue comme objectif d'entraînement |

## 3. Ce qui reste propre au manuscrit

Je le dis comme une question, pas comme une preuve de nouveauté (R8). Je n'ai lu que ces deux textes et leurs listes de citations ; je n'ai fait aucune recherche systématique sur les jeux d'inspection ni sur la littérature des pots de miel.

1. **La transposition de l'estimation à la dissuasion sous une indiscernabilité additive.** Le lemme pont de « Blindfold » est versé dans une condition de dissuasion à la Becker, avec un seuil fermé qui tient compte de l'échec de détection sur les pièges (ε_trap) et du facteur (1 − δ_ind/τ_min). C'est une combinaison en une ligne de deux résultats publiés. Elle est correcte et utile, mais mince.
2. **La garantie restreinte aux taux et le plancher côté dissuasion**, énoncés en variation totale, avec la remarque qu'on obtient la variation totale q en mêlant une fraction q de pièges tirés d'une loi disjointe. À ma connaissance, ni Gans et Holden (un choix unique par type et par signal, pas de taux par contexte) ni « Blindfold » (pas d'incitation) n'écrivent « les tricheurs de taux ≤ δ ne sont pas exclus, quelle que soit la pénalité ».
3. **Le placement dans le modèle de l'opérateur B** : un moniteur dans la boucle, aveugle sur les épisodes ordinaires, et une pénalité d'interception qui sert de score d'entraînement. Ce placement est neuf par rapport à ces deux textes, mais la preuve n'en tire rien qui dépende de la régularisation par Kullback-Leibler.
4. Hors manuscrit : la version dynamique, avec le taux de maintien sous δ_ind dans la récurrence du gradient naturel régularisé, appartient à la section sur le budget d'audit du papier D. Elle ne se juge pas ici. Cette section ne revendique déjà pas le plancher (l. 632).

## 4. Phrases de revendication resserrées (en anglais)

**Contribution 3 de l'introduction**, remplacer le passage « (R3) … » par :

> (R3)~planted honeypots: if no admissible policy's cheating rate differs between ordinary and trap episodes by more than $\delta_{\mathrm{ind}}$ (in particular if $\dTV(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$), an explicit interception penalty $C^*_{\mathrm{R3}}$ makes every policy that cheats at rate at least $\tau_{\min} > \delta_{\mathrm{ind}}$ strictly worse than honesty, while rarer cheating is not excluded; this transposes the bridge inequality used for audit-based certification~\cite{zhu2026blindfold} to the deterrence threshold of randomized auditing~\cite{gans2026randomized}, to which $C^*_{\mathrm{R3}}$ reduces when $\delta_{\mathrm{ind}} = 0$.

**Phrase de citation près de R3**, à ajouter au début de la remarque « Information-Theoretic Duality… », dont la phrase « turns the exact same total variation inequality in favor of the defender » devient « …in favor of the defender's deterrence, as it is already used for audit certification~\cite{zhu2026blindfold} » :

> The ingredients of Regime~R3 are published. When $\delta_{\mathrm{ind}} = 0$, i.e.\ when the draw cannot be learned before acting, $C^*_{\mathrm{R3}}$ is the deterrence threshold $p\,F\,d \ge g$ of randomized auditing with scalable sanctions, stated for AI agents by Gans and Holden~\cite[eqs.~(11)--(12), Prop.~4]{gans2026randomized}, with $p = \rho$, $d = 1 - \varepsilon_{\mathrm{trap}}$ and $F = \Delta R + C$; they also show that a noisy signal about the draw raises the required sanction to $\bar t_i / \min_\sigma p_i(\sigma)$ and that a signal ruling out the audit defeats every sanction~\cite[Prop.~5(c)]{gans2026randomized}. The inequality $\tau_{\mathrm{ord}} - \tau_{\mathrm{trap}} \le \delta_{\mathrm{ind}}$ is the bridge lemma $\mu_0 - \mu_1 \le D_A$ of Zhu, Zuo and Sun~\cite[Lemma~2]{zhu2026blindfold}, used there in the defender's favour to certify a violation rate, with an additive inflation that leaves rates below $\delta$ unidentified~\cite[Thms.~5--6]{zhu2026blindfold}. Regime~R3 carries this inequality from estimation to deterrence; its floor $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$ is the deterrence counterpart of their rare-violation limit.

**Limites**, à la fin du point « rare-attack floor » :

> This floor is irreducible only under a total-variation hypothesis: a likelihood-ratio condition, such as a positive lower bound on the posterior probability of a trap given any context~\cite[Prop.~5(c)]{gans2026randomized} or a hockey-stick bound~\cite[Prop.~6]{zhu2026blindfold}, would lower or remove it, which we do not derive here. Moreover, $\delta_{\mathrm{ind}}$ must come from how the traps are built, since total variation between high-dimensional transcript laws has no distribution-free finite-sample upper bound~\cite{zhu2026blindfold}.

Le mot « irreducible » de la phrase actuelle des limites est à remplacer par « an irreducible floor, under the total-variation hypothesis alone, ». La phrase ci-dessus en donne la raison.

## 5. Justesse des deux descriptions de la section sur le budget d'audit (l. 627)

**Gans et Holden.**
- « an audit requirement of the form p ≥ (gain − cost)/(fine × detection) » : **juste** (éq. 12 à v = 0 et proposition 3, p. 12).
- « a floor on the audit probability that does not depend on the sanction » quand le tirage peut être appris : **juste** (proposition 5(a), p. 15 ; p. 3).
- « the static form of our holding rate » : **défendable**. Quand η tend vers l'infini, le taux de maintien ΔR_f/(ΔR_f + C_aud) est cette condition avec g = ΔR_f, F = ΔR_f + C_aud et d = 1.
- « and of the floor below δ_ind » : **inexact**. Le plancher de la proposition 5(a) borne la **fréquence d'audit** requise quand l'agent apprend exactement le tirage pour un coût φ ; il vaut 1 si φ = 0 (éq. 20, p. 16). Le plancher sous δ_ind borne le **taux de triche** que nulle pénalité ne dissuade sous une indiscernabilité partielle. Leur résultat le plus proche de ce dernier est la proposition 5(c) (p. 15 et 16).
- Correction proposée :

> …and, when the draw can be learned before acting, a floor on the audit probability that does not depend on the sanction, while a noisy signal about the draw raises the required sanction and a signal that rules out the audit defeats every sanction~\cite{gans2026randomized}; we read the first as the static form of our holding rate, and the last as the static, likelihood-ratio form of the mechanism behind the floor below $\delta_{\mathrm{ind}}$.

**« Blindfold ».**
- « for audit-based certification of a violation rate, a worst-case bias proportional to the distinguishability of audited episodes that raising the audit rate cannot remove » : **juste** (résumé p. 1 ; théorème 1, p. 4 ; corollaire 2, p. 5). Le biais vaut (1 − ε)D_A.
- « the closest analogue we know of Proposition `prop:audit-indist` and of the condition δ_ind > 0 » : **juste, mais en deçà du chevauchement**. La borne des pièges que cette proposition emprunte à R3, τ_aud ≥ (τ − δ_ind)₊ (l. 556), est leur lemme 2 (p. 4). Leur limite des violations rares (p. 6, théorème 6) est l'analogue, en estimation, du plancher que la section exprime dans la dynamique.
- Ajout proposé après « …of the condition $\delta_{\mathrm{ind}}>0$ » :

> ; the trap bound $\tau_{\mathrm{aud}} \ge (\tau - \delta_{\mathrm{ind}})_+$ we borrow from Regime~R3 is their bridge lemma~\cite[Lemma~2]{zhu2026blindfold}, and their rare-violation limit is the estimation counterpart of the floor below $\delta_{\mathrm{ind}}$.

## 6. Dates

- **Gans et Holden** : le tampon arXiv porte « arXiv:2609.38262v1 [econ.TH] 29 Sep 2026 », et le document est daté « October 1, 2026 » (p. 1).
- **« Blindfold »** : le tampon arXiv porte « arXiv:2610.37055v1 [cs.CR] 27 Oct 2026 » (p. 1). Il cite Gans et Holden ([13], p. 12 et 14).
- Je ne juge pas ici une antériorité par la date. Elle demanderait les dates datées et vérifiables des versions du manuscrit et de ses dépôts, ce qui sort de cette lecture. La lecture ci-dessus porte sur le contenu seul.

## 7. Recommandation pour la décision

- **Décision** : resserrer la nouveauté de R3.
- **Enjeu** : sans resserrement, un lecteur qui connaît ces deux textes lit la contribution 3 et la remarque sur la dualité comme une revendication d'un résultat publié.
- **Options.**
  - (a) Les trois phrases de la section 4 et les deux corrections de la section 5. Avantage : la revendication devient exacte et R3 garde une place de jonction honnête. Inconvénient : R3 apparaît pour ce qu'il est, un corollaire.
  - (b) Rétrograder R3 au rang de remarque ou de corollaire, hors de la liste des contributions. Avantage : plus sûr. Inconvénient : on perd l'énoncé du plancher côté dissuasion, qui est la seule partie à peu près libre.
  - (c) Renforcer R3 avant de le revendiquer : une version par rapport de vraisemblance ou en crosse de hockey qui abaisse le plancher, et un corollaire sur la masse de Gibbs. Avantage : un contenu propre réel. Inconvénient : du travail, et une nouvelle vérification d'antériorité.
- **Recommandation** : (a) tout de suite, (c) en question ouverte. Confiance 0,75.
- **Réserves** : lecture de deux textes seulement ; pages des expériences de « Blindfold » et annexe en ligne de Gans et Holden non lues en entier ; aucun prédécesseur cité par ces textes n'a été ouvert (Avenhaus et al., les « ringers », Santos-Grueiro 2026, qui borne l'écart évaluation-déploiement par l'information mutuelle selon « Blindfold », p. 12). Ce dernier est à vérifier en priorité pour le point (a).
