# Lecture adverse de la note « proposeur modèle de langue contre le juge statistique » (candidat 2-c) — v1

**Verdict : « après corrections ».** La première version anglaise est publiable comme notes de la note que Lazar écrira, une fois corrigées six phrases plus fortes que leur pièce (M1 à M6) et complétée la liste de ce qui est emprunté (M7). Aucun bloquant : aucun chiffre faux, aucune recette d'attaque, aucun mot de primauté, aucune feuille de route, aucune citation obligatoire absente de la liste des références.

- **Lecteur** : lecteur adverse neuf, modèle B (autre que celui du rédacteur) ; n'a écrit ni la note, ni la fiche, ni le journal, ni aucune pièce citée. Écrit le 14 novembre 2026. Aucun identifiant de modèle dans ce rapport.
- **Rien publié, rien commité, rien poussé, aucun contact, aucune requête réseau.** Lectures interdites tenues (rien sous `diag/`, runs de 7a et 7b, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `prereg/T0.7-sondes-v0-v1.md`, paquet de P3-bis). Le code public de l'attaque (qui porte la consigne) n'a pas été ouvert.

## 1. Pièces lues et vérifications

| pièce | empreinte (début) | contrôle |
|---|---|---|
| `note-premiere-version-en-v1.md` | `5ffa224c…` | égale au compagnon |
| `fiche-faits-note-organisme-v1.md` | `c1f25deb…` | égale |
| `journal-note-organisme-v1.md` | `a0d87565…` | égale |
| verdict officiel d'A1-v4 | `e6e2f170…` | lu en entier (101 lignes) |
| `lecture-o4-englobement-v1.md` | `f521e164…` | §§ 0, 1, 4, 5, 6 |
| `decision-N-064-v1.md`, `decision-N-067-v1.md` | `387c9d4e…`, `966dd9dc…` | N-064 en entier ; N-067 §§ 3 à 9 |
| tri, entrée 2-c | `c51fadd6…` | l. 36-44, 132-156 |
| page publique v5 | `ffc016ef…` | égale à l'octet au `README.md` du clone public (tête `1a1a419`, en ligne depuis R-2648) ; l. 1-30, 130-150 |
| page d'état d'A1 (publique) | `c549a31b…` | lue en entier ; inchangée entre `be6b5af` et `1a1a419` |
| Qu, Chen, Wang (PDF) | `2a8ded01…` | p. 12 et 15 relues par `pdftotext` |
| CONFIRM (PDF, branche des pièces) | `9a02cc6d…` | p. 6, 9, 22 relues |
| `nul_v8.py`, `nul_v9.py` (code public) | — | en-têtes lus (membres du nul) |
| règles du site | `lw-politique-llm-mise-a-jour/texte.txt`, `lw-guide-nouvel-utilisateur/texte.txt` | lues |

Chiffres recalculés par ce lecteur : Wilson 1/24 = [0,0074 ; 0,2024], 10/24 = [0,2447 ; 0,6117], 24/24 = [0,862 ; 1], 23/24 = [0,7976 ; 0,9926] ; 1 − 0,95¹⁶ = 0,5599 ; McNemar exact 5 contre 2 = 0,453 ; corps de la note = 798 mots (`wc -w`). **Tous les chiffres de la note sont exacts et ont leur pièce** (seul 0,56 n'a qu'une source publique et un calcul, ce que le journal déclare).

## 2. Constats par gravité

### Bloquants : aucun

### Majeurs (phrase plus forte que sa pièce, ou cession non dite)

**M1 — la description du nul (S02, première phrase fragile).** « a null made of the laws the system already knows and their combinations » est **faux dans les deux sens**. (a) Trop fort : le nul ne couvre pas « leurs combinaisons » ; v8 ne porte que la mise en commun linéaire ajustée et chaque loi connue tempérée et inclinée, v9 ajoute les seules recombinaisons par morceaux à un niveau, et déclare encore des trous (`NON_COUVERT_V9`). La phrase contredit la note elle-même deux paragraphes plus bas (« a class v8 itself declares uncovered » : W2 est une combinaison des lois connues). (b) Incomplet : le nul porte aussi une bibliothèque fixe (« aveugle ») qui n'est pas faite de lois connues ; le dénominateur est le maximum sur tous les membres (en-têtes de `nul_v8.py` et `nul_v9.py`, publics ; constat de R-2583). La reformulation du rédacteur corrige « best fitted combination » en « best fitted member », mais garde le défaut (a).
- Avant : « …beats, through an e-process, the best fitted member of a null made of the laws the system already knows and their combinations. »
- Après : « …beats, through an e-process, the best-fitting member of the judge's null. That null is a fixed library plus members fitted on the laws the system already knows: in v8, their pooled mixture and a tempered version of each; v9 adds one-level piecewise recombinations. Neither covers every combination, and each lists what it leaves out. »
- Reste ouvert : la condition (a) de la lecture de O4 (§ 4) demande la confirmation de l'auteur de l'orchestrateur ; elle n'est pas donnée. La page v5 en ligne (l. 15) porte encore « best fitted combination of the already known laws » : même défaut, hors de cette lecture, à signaler à Lazar.

**M2 — « What this run adds, at most… » (S33, seconde phrase fragile).** Sans mot de primauté, mais « adds », placé après la liste des antériorités, se lit « absent de ces travaux » : c'est la clause « non trouvé » que le journal dit avoir retirée. Trois raisons de ne pas la tenir : (i) les pistes contre la forme de O12 ne sont pas lues (N-067 § 8 : Asher et al., 2606.27687, Dai et al. 2610.21040, Gençay 2608.27734) ; (ii) on ne sait pas si la règle exacte de l'arbitre est donnée au modèle chez Qu, Chen, Wang (N-067 § 8, code « sur demande ») ; (iii) CONFIRM compare déjà un bras qui reçoit le diagnostic du juge à un bras qui ne le reçoit pas (« failure-blind retry », p. 9 et tableau 12 p. 22), sur 215 affirmations retenues et non sur les contrôles négatifs : le trait distinctif se réduit à « les deux bras comparés sur un monde où toute promotion est fausse », et ce bras n'a rien tranché ici.
- Avant : « What this run adds, at most, is a small measurement of one form: a proposer that reads the judge's exact description, with an arm that receives the verdicts and one that does not, compared on a world where every promotion is false. »
- Après : « This run is one small measurement of a particular setup: the proposer reads the judge's exact description, and the arms with and without verdicts are compared on a world where every promotion is false. CONFIRM already compares diagnosis with failure-blind retry, on claims it withheld (p. 9, Table 12); I have not checked whether the setup as a whole appears elsewhere, and here the comparison came out undecided. »

**M3 — « whose objective is to get a law promoted » (S04).** Pas une recette : la phrase dit moins que la page v5 en ligne (l. 14, poussée sur le mot de Lazar, R-2648) et ne donne ni mots, ni structure, ni stratégie. Elle n'est pas plus forte que l'instrument (R-2581, B1). Son défaut est l'omission : sans « il ne lui est pas dit qu'une promotion serait fausse », « attack » et « objective » laissent croire à un proposeur chargé de tromper.
- Avant : « …a language-model proposer whose objective is to get a law promoted reads… »
- Après : « …a language-model proposer that is rewarded when its law is promoted (it is not told that a promotion would be false) reads… »
- Si Lazar lit la parenthèse comme une consigne, garder la phrase d'origine plutôt que la couper : sans elle, la note ne dit plus qu'il y a un adversaire.

**M4 — W2g « checks that… did not » (S36).** Le verbe présuppose le résultat ; la lecture gelée interdit « le v9 n'a pas de prix » et la page d'état dit « whether ».
- Avant : « it checks that closing the hole did not leave the judge blind where it still has to discover. »
- Après : « it asks whether closing the hole left the judge blind where it still has to discover; at this dose the proposer got laws promoted that replay, which says nothing about v9's price in power. »

**M5 — « Neither result is a successful attack » (S37) et « The other 7 do not » (S20).** Inférence du rédacteur, plus forte que les deux lectures gelées : sur W2, quatre suites ont été promues à faux (multiplicité) ; sur W2g, le statut des lois promues qui ne se rejouent pas n'est pas établi (la fiche interdit « the 7 other laws are false », la réciproque ne l'est pas davantage). Et « 7 » ne vaut que pour la famille de Holm du code gelé : 5 avec la famille par monde, lettre du texte scellé (réserve 4).
- Avant : « Neither result is a successful attack. » → Après : « Neither frozen label is a breach. On W2, four sequences in 48 were still promoted, at the rate multiplicity allows; on W2g, what the promoted laws that do not replay are is not settled. »
- Avant : « The other 7 do not. » → Après : « The other 7 do not (5 under the Holm family the sealed text describes, 7 under the one the frozen code uses; same label either way). »

**M6 — « W2 replicates a published sign » (S35).** Le signe publié est zéro admission ; ici 1/24 et 3/24, sur un monde jouet d'un autre domaine. « Replicates » dit trop.
- Avant : « W2 replicates a published sign under a somewhat different attack, at small size… »
- Après : « W2 has the same sign as published results (false promotions at or near zero), in a different setup and at small size… »

**M7 — cessions de N-067 non dites dans le corps (S01, S03).** La première phrase décrit la séparation de qui propose et de qui juge (O1) et le sceau avant lecture (O3) ; « These pieces are borrowed » n'énumère ensuite que le nul, l'e-processus et les e-valeurs. N-067 § 4, point 5, demande de **dire** que Qu, Chen, Wang revendiquent la priorité de la séparation ; les auteurs ne sont que dans la liste finale, sans ce qu'ils ont fait.
- Avant : « These pieces are borrowed: judging a candidate against what is already known… »
- Après : « Every piece is borrowed: separating who proposes from who judges (Qu, Chen, Wang, who claim its priority; PROCTOR); a plan hashed before the outcomes are read (CONFIRM; Zhang); control of multiple comparisons (Qu, Chen, Wang; CADS; Wang et al.); judging a candidate against what is already known… »

### Mineurs

- **m1 — Setup, écart déclaré absent.** « verdict by a reader who wrote none of the materials » est exact, mais l'audit et le verdict provisoire sont du même lecteur (réserve 7, publique). Ajouter : « (declared deviation: the audit and the provisional verdict share a reader) ».
- **m2 — prédictions.** Ajouter « three of the eight held exactly at their limit » (P1, P3, P8 ; verdict § 3, page d'état l. 26) : sans cela « 8 of 11 » flatte.
- **m3 — références sans version ni page.** Les pages citées (p. 15 ; p. 9, 22) dépendent de la version : écrire 2609.27051v1, 2611.01449v2, 2609.33180v2, 2511.06701v4, 2608.06621v5 ; Co-Scientist : Nature 655, 487-496 ; Liu et al. : « version dated April 2026 », lue sur une copie d'hôte de conférence, l'identité avec le PDF de SSRN n'étant pas vérifiée (R-2590, M3).
- **m4 — « two interrupted runs »** : sourcé (verdict de la troisième course, l. 113). Rien à changer.
- **m5 — « reading the description was enough » (S27)** : indique où est le trou, non comment le prendre ; déjà public sur les deux pages. Admis ; ne rien y ajouter (ni « 42 des 48 », ni « une loi par sous-population »).
- **m6 — 2606.11417** (audit scellé attaqué par retour scalaire ; N-067 § 6, « à citer si le point est abordé ») : le journal dit le point non abordé ; l'attaque par les verdicts rendus est pourtant le sujet de la note. À ajouter aux voisins. Yang et Shi : hors sujet, d'accord avec le journal.
- **m7 — lien.** La page d'état liée porte une feuille de route (« Next », v10, « a new attack against v9 ») et deux décisions ouvertes. Déjà public ; la note n'en reprend rien. À savoir avant de lier.
- **m8 — règles du site.** L'avertissement de tête est juste. Deux rappels : la voie admise est d'écrire en français puis de faire traduire mot à mot, sans réécriture ; le guide demande une introduction claire et, pour l'IA, un niveau élevé — la première phrase de Lazar doit dire le résultat et sa borne, pas le dispositif.

### Sans constat

- **Recette d'attaque** : aucune consigne, stratégie, loi promue, réponse ni forme gagnante. Embargo tenu.
- **Primauté** : aucun « first », « novel », « gap », « to our knowledge » ; O2 et O4 dits comme assemblage, jamais libres ; O1, sceau de O3, O17 non revendiqués (sous réserve de M7) ; forme de O12 sans « chargé de tromper » ni « libre » (sous réserve de M2).
- **Citations obligatoires** : les quatre de N-064, les onze de N-067 § 6, les quatre de R-2587, Qu, Chen, Wang p. 15 et CONFIRM p. 9 : toutes présentes.
- **Feuille de route** : aucune ; « Nothing about v9's declared holes, other providers or real data » se lit comme limite.

## 3. Les trois objections les plus fortes, et la réponse que les pièces permettent

1. **« Vous avez mesuré un théorème. »** L'inégalité de Ville borne chaque tentative par α ; 4 suites promues sur 48 sous v9, contre un plafond de 0,56 par unité, ne disent rien de plus. — Réponse permise : oui pour la borne (page d'état, « Theory already bounds part of the answer »). Ce que W2 éprouve, c'est le code et le certificat de v9, non le théorème : une seule loi promue rejouée au-dessus de α après Holm aurait signifié un défaut du certificat, du code ou du banc (page d'état, l. 10) ; aucune des 712 lois rejouées ne l'est. La note ne le dit pas : à ajouter en une phrase. Limite à dire : sans témoin négatif planté, un échec de chaîne égal dans les deux bras passerait inaperçu.
2. **« Votre attaquant est faible, donc "résiste" ne dit rien. »** Non chargé de tromper, grammaire fermée, un fournisseur, 16 tentatives, et le bras des verdicts ne tranche rien ; les dents sous v8 montrent seulement qu'il lit un trou que le juge déclare. — Réponse permise : le libellé gelé est « à cette taille » et la lecture gelée interdit « le taux est sous 0,05 » ; l'instrument est sain (part hors de la classe du v9 : 371 sur 373 ; lois distinctes 0,971) et le même proposeur bat l'ancien juge 24 fois sur 24. Rien sur un attaquant plus fort : la note le dit, la correction M3 le rend visible.
3. **« Le vrai résultat est ailleurs : votre juge de production tombe 24 fois sur 24 à la seule lecture de sa description, et le correctif a perdu de la puissance ; à la frontière, 7 lois promues sur 17 ne se rejouent pas. »** — Réponse permise : la brèche de v8 est dans une classe que v8 déclare non couverte ; les lois promues prédisent le monde et ne sont « fausses » qu'au sens du critère de nouveauté (page d'état, l. 63) ; ce n'est ni un défaut du nul ni la garantie de Ville battue. v9 est un candidat, sa validation a rendu « puissance perdue », issue attendue par écrit, et v8 reste en production. Le statut des 7 lois n'est pas établi (M5). La note porte ces faits, mais dispersés : Lazar gagnera à les mettre en tête de « What this does not show ».

L'objection du tri (« zéro promotion est publié ; frontière franchie ne montre aucune faiblesse ») est traitée par la note ; sa réponse tient après M4, M5 et M6.

## 4. Réserves de ce lecteur

- Les PDF de REUSE, Sargsyan, Hegazy, POPPER, Dwork, Blum et Hardt, Feng, Liu, Pan, Ma n'ont pas été rouverts : leurs descriptions sont prises de N-064, N-067 et de la lecture de O4. Seuls Qu, Chen, Wang (p. 12, 15) et CONFIRM (p. 6, 9, 22) ont été relus.
- La consigne du proposeur n'a pas été lue : le jugement « pas une recette » sur S04 repose sur la page v5 (l. 14) et sur R-2581.
- La description du nul proposée en M1 vient des en-têtes du code public, non d'une confirmation de l'auteur de l'orchestrateur.
- Rapport scellé, non commité.
