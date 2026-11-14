# Journal de la note « proposeur modèle de langue contre le juge statistique » — v1

- **Rédacteur** : sous-agent rédacteur neuf (aucun identifiant de modèle consigné). Écrit le 14 novembre 2026, de 06:48 UTC (`date -u`) au scellement. Demande : session mère, pour Lazar (note LessWrong, candidat 2-c du tri).
- **Rien commité, rien poussé, rien publié, aucun message envoyé, aucune requête réseau.** Lectures interdites respectées (section 4).
- Clés des pièces : celles de `fiche-faits-note-organisme-v1.md`, section 1 (V, PRE, V3, TRI, N064, N067, O4L, PUB5, PUB-A1, QCW, CONF, REG). Numéros F : faits de la fiche.

## 1. Source de chaque phrase de `note-premiere-version-en-v1.md`

| n° | phrase (début) | source | remarque |
|---|---|---|---|
| T | Title: « A language-model proposer that reads a statistical judge's rules… 1 of 24 inside the null, 10 of 24 at its frontier » | F18, F27 ; TRI l. 140-143 | « rules » = « exact description » (V l. 36) |
| S01 | « In a small automated research system, language-model agents propose "laws" and a frozen statistical judge, code outside the agents, decides… » | PUB5 l. 3 ; PUB-A1 l. 78 | le calcul hors des agents est emprunté (N067 § 4 point 1) : dit comme description, pas comme apport |
| S02 | « A law is promoted only if its prediction, sealed before the outcomes are read, beats, through an e-process, the best fitted member of a null made of the laws the system already knows and their combinations. » | PUB5 l. 15 ; O4L § 4 (conditions a, b) ; PUB-A1 l. 11, 64 (membres du v9 : recombinaisons) ; R-2583 | **fragile** (section 3) ; « before the outcomes are read » et non « before the data exist » (O4L, condition b) |
| S03 | « These pieces are borrowed: … Feng, Giglio, Xiu … Liu, Liu, Liu, Mei; Pan, Ding, Giesecke … Ma et al. … POPPER. » | R-2587 (O4 dit comme assemblage, quatre citations) ; O4L § 0 et § 4 ; N064 l. 13 (POPPER) ; PUB5 l. 10, 15 | phrase calquée sur la phrase publiable de O4L § 4, raccourcie ; la clause « we did not find this combination » est **omise** (section 2) |
| S04 | « The question is narrower: … whose objective is to get a law promoted reads the judge's exact description, declared holes included, and, in one arm, also receives its verdicts? » | V l. 36 (description servie avec « Non couvert », etc.) ; PUB-A1 l. 7, 10 ; PUB5 l. 14 (incitation) ; TRI l. 140-141 | **fragile** (section 3) : « whose objective is… » touche à la consigne |
| S05 | « Preregistered; output sealed by hash before reading; outcome computed by frozen code; verdict by a reader who wrote none of the materials. » | F11 ; V l. 6, 19 ; PUB-A1 l. 13, 15 | la sortie et le verdict sont privés ; le texte scellé est public (F13 ; PRE) |
| S06 | « One provider, laws in a closed grammar. » | F02, F04 ; PUB5 l. 14 | le nom « Argon » est laissé au choix de Lazar |
| S07 | « Two judges: the candidate (v9) and its predecessor (v8), a check that the attack has teeth. » | F01, F05 ; PUB-A1 l. 7 | |
| S08 | « Two arms: with and without verdicts. » | F03 ; PUB-A1 l. 7 | |
| S09 | « 24 units per cell; a unit is one world instance with up to 16 attempts, promoted if any attempt is. » | F05, F06 ; V l. 25 ; PUB-A1 l. 7, 17 | « world instance » rend « carte » (V l. 72, « cartes de la course ») |
| S10 | « 1,478 calls, 114 USD; verdict of 10 November 2026. » | F08, F09, F10 | 114,0434 arrondi |
| S11 | « W2 lies inside v9's null: every promotion under v9 is false by construction. » | F14 | |
| S12 | « Earlier runs broke v8 on it, through a class v8 itself declares uncovered; v9 adds that class to its null. » | F15, F41, F43, F44 ; PUB-A1 l. 64 | « adds that class » : v9 ajoute les recombinaisons par morceaux (PUB-A1 l. 64) |
| S13 | « W2g mixes a new law into one sub-population (dose 0.40), at v9's declared frontier. » | F16 | |
| S14 | « A promotion there is not false by construction: does the proposer find a law that really replays? » | F16 ; PUB-A1 l. 11 | |
| S15 | « W2: under v9, 1 of 24 … (0.007 to 0.202), 3 of 24 without; under v8, 24 of 24. » | F18, F19, F20 | Wilson arrondi à trois décimales |
| S16 | « Frozen label: "resists (at this size)"; 1 of 24 is the most that label admits. » | F21, F22 | |
| S17 | « The four laws promoted under v9 replay 2 or 3 times in 200, none above α after Holm: multiplicity. » | F24 ; V l. 52, 83 | « multiplicity » = mot de l'audit (« multiplicité, pas défaut ») |
| S18 | « For scale, the per-unit ceiling at α = 0.05 over 16 attempts is 1 − 0.95¹⁶ ≈ 0.56. » | F26 ; PUB-A1 l. 80 ; recalcul 0,5599 | seul chiffre sans pièce scellée du dépôt de travail : page publique et calcul |
| S19 | « W2g: 10 of 24 with verdicts (0.245 to 0.612), 7 of 24 without; under v8, 23 of 24. » | F27, F28, F29 | |
| S20 | « Frozen label: "frontier crossed, robust", where "robust" qualifies the promoted laws, not the judge: 10 of the 17 … replay above α after Holm. The other 7 do not. » | F30, F31 ; PUB5 l. 18 (même glose) | seuil gelé 0,5 et la variante 12/17 laissés dans la fiche (place) |
| S21 | « Effect of the verdicts: not established (W2: 1 with, 3 without; W2g: 10 against 7, discordant units 5 against 2, McNemar p = 0.45). » | F34, F35 | « not established » rend « non tranché » ; p = 0,453 arrondi |
| S22 | « 8 of 11 signed predictions held; missed: 0 of 24 on W2, at least 12 of 24 on W2g, a replay share of at least 0.80. » | F36 | |
| S23 | « Two toy worlds, one provider, 24 units, 16 attempts. » | F25, F32 (bornes des lectures gelées) ; TRI l. 145 | « two toy worlds » : W2 et W2g ; un seul au nul (F25) |
| S24 | « The run was unusually clean (one failed call in 1,478) without a planted negative witness: a chain failure hitting both arms equally would go unseen. » | F38 ; V l. 82 | ce qui s'y oppose (rejeu à l'identique) laissé dans la fiche |
| S25 | « v9 is a candidate, not the production judge; its own validation reported a loss of power. » | F01, F45 ; PUB-A1 l. 52 | verdict de la validation du v9 non relu (fiche F45) |
| S26 | « Nothing about v9's declared holes, other providers or real data. » | F46 ; PUB-A1 l. 55 | dit comme limite, non comme suite |
| S27 | « By its preregistration, it is reported with the earlier runs: a first run (W1 not judgeable; W2 breached v8), two interrupted runs, and a clean rerun (W1 resisted v8 at 1 of 24; W2 broke v8 in 24 of 24 units with or without verdicts: reading the description was enough). » | F40 à F43 ; PRE l. 193 ; V3 l. 3-5, 22, 60 ; PUB-A1 l. 45-49, 61-63 | règle « jamais seule » tenue ; « the description was enough » = V3 l. 60 (« la description seule donne le trou ») et PUB-A1 l. 63 |
| S28 | « The sign is not new. » | N067 l. 119 (F49) | |
| S29 | « Under a frozen referee, language-model controllers admit zero false factors per submission (Qu, Chen, Wang, p. 15) » | F47 ; QCW p. 15, revérifiée ce matin | texte : « both LLM families admit 0.000 false factors per submission » |
| S30 | « CONFIRM serves its judge's diagnostics to a language model on 150 designed negative controls, and none of 10,716 evaluated candidates passes (pp. 9, 22). » | F48 ; CONF p. 6, 9, 22, revérifiées ce matin | |
| S31 | « Adaptive attacks on a reused holdout or a leaderboard date from 2015 (Dwork et al.; Blum and Hardt) » | N064 l. 14 ; PUB5 l. 13-14 | |
| S32 | « REUSE, Sargsyan and Hegazy et al. treat neighbouring threats. » | N067 l. 67 ; PUB5 l. 14 ; REUSE p. 32, Sargsyan p. 27, Hegazy p. 1-2 revérifiées | phrase volontairement vague (place) ; détail dans la fiche § 4 |
| S33 | « What this run adds, at most, is a small measurement of one form: a proposer that reads the judge's exact description, with an arm that receives the verdicts and one that does not, compared on a world where every promotion is false. » | N067 § 4 point 3 (forme resserrée de O12), **sans** « chargé de tromper » ni « libre dans ses propositions » (R-2581, nœud O12) | **fragile** (section 3) |
| S34 | « "Zero promotion is published, and 'frontier crossed' where a promotion is not false shows no weakness." » | TRI l. 149-150 (objection la plus dure, traduite) | |
| S35 | « Both halves are right. W2 replicates a published sign under a somewhat different attack, at small size, and the verdict arm showed no decided effect. » | F35, F47-F49 | |
| S36 | « W2g was not built to find a weakness: it checks that closing the hole did not leave the judge blind where it still has to discover. » | PUB-A1 l. 11 (« whether v9's price in power leaves the candidate blind where it matters, where the system still has to discover ») | |
| S37 | « Neither result is a successful attack. » | F25, F32 (lectures gelées) | inférence de rédacteur, conforme aux deux lectures |
| L | lien vers la page d'état et la page principale | PUB-A1 (en ligne à `be6b5af`) ; PUB5 l. 150, 246 | la page principale v5 n'est pas encore en ligne : la page d'état d'A1, elle, l'est |
| R | références | fiche § 4 | toutes les citations obligatoires (N-064, N-067 § 6, R-2587, TRI) y sont ; les moins liées à l'attaque sont groupées en une phrase |

Nombre de mots du corps (de « The question » à la fin de « The hardest objection ») : 798 par `wc -w`.

## 2. Laissé dehors, et pourquoi

1. **Consigne et stratégie du proposeur** (embargo, TRI l. 146) : mots de l'incitation (« rewarded if its law is promoted », PUB5 l. 14), forme des lois promues, « 42 des 48 lois reproduisent la loi du monde » et la manière de percer v8 (PUB-A1 l. 63) ; le code de l'attaque n'a pas été ouvert.
2. **Clause « non trouvé »** de la phrase publiable de O4L § 4 (« we did not find this combination… ») : elle dirait une conjonction non trouvée, ce que Lazar a écarté (R-2587 : jamais libre ni neuf) et que la lecture de O4L laisse ouverte (cinq pistes non lues, fiche § 5).
3. **Ce que N-067 cède** (fiche § 3, point 3) et les termes jugés plus forts que l'instrument (R-2581).
4. **Détails sans place** : seuil gelé 0,5 de « robuste » et la variante 12/17 (réserve 4) ; les sept cartes sous le seuil du contrôle par carte (réserve 3, F33) ; « λ\* à la limite » (F17) ; écart d'Argon (réserve 6) ; rôles (réserve 7) ; levée de la suspension lue sans le mot (F23) ; instrument (échos, lois distinctes, hors classe) ; 0 violation de monotonie (F37) ; dépenses des courses antérieures ; « Correction (2 November) » de la première course. Tous sont sur la page d'état publique, que la note lie.
5. **Décisions ouvertes** (prix du v9, sens de « rien au-delà de l'archive ») : seul « v9 is a candidate » est gardé ; le reste se lirait comme feuille de route.
6. **Autres résultats de l'organisme** (banc de tricheurs, course C1, mondes plantés) : hors sujet et, pour le banc, O11 n'est plus revendiquée (N067 § 4 point 4).
7. **Yang et Shi (2611.00643)** et 2606.11417 : « à citer si le point est abordé » (N067 § 6) ; le point n'est pas abordé.
8. **Nom du fournisseur** (« Argon », public sur la page) : à Lazar de le nommer ou non.
9. **Phrase du tri 2-c**, reprise en substance mais non mot pour mot : « ("frontier crossed, robust": 10 of the 17 promoted laws replay above α after Holm) » est gardé ; le reste est réparti.

## 3. Phrases les plus fragiles

1. **S02** (le nul « fait des lois connues et de leurs combinaisons ») : la page v5 dit « the best fitted combination of the already known laws » ; le rédacteur de la page a constaté que, dans le code public (`nul_v8.py`), le dénominateur est le meilleur de tous les membres du nul, pas la seule combinaison ajustée des lois connues (R-2583) ; O4L § 4, condition (a), demande que l'auteur de l'orchestrateur confirme la description. Ma reformulation (« best fitted member of a null made of the laws … and their combinations ») suit ce constat mais n'a pas été confirmée par l'auteur du code.
2. **S04 / S33** (l'objectif du proposeur et ce que la note ajoute) : « whose objective is to get a law promoted » est le strict minimum pour dire qu'il s'agit d'une attaque ; c'est déjà public (PUB5 l. 14), mais l'embargo interdit toute consigne : à couper si Lazar le lit comme une consigne. S33 reprend la forme resserrée de O12 (N-067 § 4 point 3), elle-même signalée plus forte que l'instrument dans sa lettre (R-2581) ; sans « chargé de tromper » ni « libre », elle reste une revendication de forme : « at most » et l'absence de toute clause « non trouvé » la bornent, mais un lecteur pourra demander pourquoi cette forme compte si l'effet du retour n'est pas établi.

Autres points d'attention : S18 n'a qu'une source publique et un calcul ; S27 dit « reading the description was enough » (V3 l. 60), proche d'une indication sur la manière de percer v8, mais déjà public (PUB-A1 l. 63, PUB5 l. 140) et sans détail.

## 4. Vérifications faites

- Empreintes des six pièces de la consigne : `python -m controle_ia.scellement verifier` → OK (tri `c51fadd6…`, verdict `e6e2f170…`, page v5 `ffc016ef…`, N-064 `387c9d4e…`, N-067 `966dd9dc…`, lecture O4 `f521e164…`) ; plus PRE `d306a8fa…`, V3 `7dade9ef…`, QCW `2a8ded01…`, les PDF des citations obligatoires présents sur `main` et les archives de LessWrong (`texte.txt`, `adresse.txt`) : OK. CONFIRM, Sargsyan, Hegazy extraits de la branche `prep/etat-de-l-art-niveau3-pieces-v1` par `git show` dans le bloc-notes : empreintes égales aux compagnons de la branche.
- Citations revérifiées sur le texte extrait par `pdftotext` : Qu, Chen, Wang p. 6, 12, 15 ; CONFIRM p. 6, 9, 22 ; REUSE p. 32 ; Sargsyan p. 27 ; Hegazy p. 1-2.
- Page d'état publique lue dans le clone local `/home/user/lciric/ideation-organism` (lecture seule ; `origin/main` = `be6b5af`, commit local non poussé `1168b02` = page v4) ; son contenu à `be6b5af` est identique au fichier de travail (`c549a31b…`).
- Registre : R-2580, R-2581, R-2583, R-2587, R-2590, R-2593, R-2594, R-2600, R-2603, R-2604, R-2646 lus. Aucune ligne postérieure à R-2587 ne revient sur O4 ni sur SSRN 6569258 (lignes 2546 à 2560 lues, recherche de mots sur les lignes 2585 à 2606).
- Lectures interdites : aucun fichier sous `diag/`, des runs de 7a ou 7b, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `prereg/T0.7-sondes-v0-v1.md`, ni du paquet de P3-bis. Lignes du registre lues au passage qui nomment T0.7 (R-2582, R-2588, R-2589, R-2597, R-2601, R-2629, R-2637) : aucune pièce ouverte, rien repris.
- Aucun identifiant de modèle de Claude dans les trois fichiers (recherche de mots faite avant scellement).
