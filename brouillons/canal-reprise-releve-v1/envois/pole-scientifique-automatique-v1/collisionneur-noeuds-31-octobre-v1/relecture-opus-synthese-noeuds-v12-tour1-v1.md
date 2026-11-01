# Relecture indépendante (Opus) de la synthèse du tour 1 — collisionneur des nœuds de décision, question v12 — v1

- **Relecteur** : sous-agent neuf, modèle Opus 5.5 (`claude-opus-5-5`), lignée conv-audit, sur le mot de Lazar (R-746 de `registres/decisions.md` : « Opus relis les réponses qui vont arriver »). Je n'ai écrit ni la question, ni les critères, ni la synthèse, ni aucune cellule.
- **Date** : 2026-11-01, relevé `date -u` : `Sun Nov  1 06:25:46 UTC 2026` (début de lecture).
- **Limite** : rien lu sous `donnees/` (ni cellules, ni faits `faits-noeuds-v2.md`, ni `etat.md` du run). Je relis la synthèse contre la question, les critères et les pièces du dépôt accessibles sur la branche `canal/conv-audit-n04`. Aucun commit, aucun `.sha256` écrit, aucun fichier existant modifié, aucun appel de réseau ni de modèle, aucune clé lue.

## Pièces lues, empreintes SHA-256 recalculées (toutes égales à leur compagnon `.sha256`)

| Pièce | SHA-256 |
|---|---|
| Synthèse (lecteur Fable 5.1), copie extraite : `…/scratchpad/n58-envois/brouillons/canal-reprise-releve-v1/envois/session-depot/collisionneur-noeuds-v12-tour1-v1/synthese-noeuds-v12-tour1-v1.md` | `e4d5a5c94c37534a7481772af2f1150f325be38c46c356353520c44cf2f85aa5` |
| Critères scellés, même dossier : `criteres-lecture-noeuds-v12-tour1-v1.md` | `22edbf4751c205f6760a136963bfaebcede773bfdc3300e923ad8e5df4e3a529` |
| Question : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/collisionneur-noeuds-31-octobre-v1/question-noeuds-decisionnels-collisionneur-v12.md` | `a7fac44bd25c0b88f90c3ce50c23fa3a704675e57c3639ea0e4e56c1797102d3` |
| PDF cité par N10 : `docs/sources/pdf/2412.09565v2.pdf` | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` |

Le préfixe de la question annoncé par les critères et par la synthèse (`a7fac44bd25c0b88f90c…`) concorde avec mon recalcul. Pièces du dépôt citées mais **absentes de cette branche** (vraisemblablement sur `main`, non vérifiables ici, R11 : non déclarées absentes du dépôt, seulement hors de ma portée) : `docs/notes/ideation-organisme-v1/course-2/collisionneur-noeuds-v1/` (chemin des critères dans l'en-tête de la synthèse), `docs/notes/protocelles-collisionneur-v1/criteres-lecture-protocelles-tour1-v1.md`, `docs/notes/anteriorite-P-041-v1/collisionneur-dml1-v1/criteres-lecture-dml1-v1.md`, `docs/notes/gu-krenn-v1/prereg-gu-krenn-reproduction-et-hors-echantillon-v2.md`, R-910. Le dossier `docs/sources/pdf/demande-conv-audit-2026-10-31-v1/` contient bien 1702.07007, 1501.01332 et 2303.18211 (fait de DL-6 conforme) et aucun PDF de LiNGAM identifiable par son numéro.

## Verdict en une phrase

La synthèse est fidèle à la forme imposée et ses recalculs numériques sont presque tous exacts, mais son décompte de tête n'est pas reconstructible et se contredit en deux endroits (N6 : « neuf » accords larges pour onze listés et douze impliqués ; apports « seuls » qui sont repris), et une affirmation de recalcul sur la concordance de rangs (N11, « W ≥ 0,7 rejette le seul état intermédiaire », « p < 0,05 de réalisation nulle ») est fausse telle qu'écrite : **tenue sous condition**, décompte et N11 à reprendre avant le tour 2.

## 1. Respect des critères scellés

| Critère | Respect | Remarque |
|---|---|---|
| 1 (quatre espèces, cellules entières) | oui | — |
| 2 (annexe du tour 2 non lue) | oui, déclaré | colonne « tour 2 à venir » partout |
| 3 (niveau) | oui | deux passages de classe 1 comptés par classe seule |
| 4 (statuts) | oui | SUPPOSÉ de la question maintenus (N3, N9) ; C corrigée en N3 |
| 5 (inexactitudes) | **partiel** | voir § 3, erreur E3 : la « transposition » de B (0,89 attribué à un effet de 5 points, la pièce disant 1 point) est un chiffre attribué aux faits et différent : le critère 5 la classe « inexact sur les pièces » |
| 6 (six éléments) | oui | incomplétudes nommées (A N11, B N10, D confiances et portée du plafond) |
| 7–9 (accords, convergences, divergences) | oui sur la forme ; décomptes non reconstructibles (§ 2) | |
| 10–11 (symétrie, vrai par construction) | oui | réserves portées aux six accords concernés |
| 12 (apports seuls « jamais repris ») | **non respecté en deux cas** | § 2, erreur E2 |
| 13 (pièce sans dépense) | oui | reclassements « avec dépense » nommés |
| 14 (N1, R1) | oui | |
| 15 (N4, N6 calculs) | oui | |
| 16 (N5, défaut, choix un par un) | oui | |
| 17 (N9) | oui | |
| 18 (N10) | oui | |
| 19 (N11) | oui sur la forme | recalcul fautif sur W (§ 3, E1) |
| 20 (liens et ordre) | oui | |
| 21 (forme, décompte en tête) | oui | |
| 22 (traçabilité) | **partiel** | renvois « (T1, N3 (c)) », « A (T3) » sans nom de fichier ni section ; peu de renvois de cellule au format `E3-Tn-…-X.md`, section |
| 23 (rien tranché, aucune recommandation) | **léger écart** | « réserve que je retiens » (DL-5), « apport majeur », « ce chiffre rend la forme de C et D inapplicable » : le lecteur prend parti |
| 24 (questions du tour 2) | oui | seize divergences, sept accords trop propres |
| 25 (ordre, lecteur neuf nommé) | oui, à vérifier | critères scellés « ≈ 18:26 UTC », empreintes à 18:24 ; `date -u` de fin de lecture des douze cellules et des faits (45 811 mots) à 18:29:47 : délai court, cohérent seulement si le lecteur a été lancé avant 18:26 ; horodatages de lancement à confronter aux journaux de session-depot |

## 2. Cohérence interne (décomptes, renvois)

- **Accords (30)** : 1+1+2+6+14+1+1+4 = 30, et 26 larges + 4 à deux. Les 4 à deux se retrouvent (N5 : deux paires rivales ; DL-10 : deux paires). **Mais** pour N6 la tête implique 14 − 2 = **12** accords larges, le texte de N6 écrit « **Neuf** accords larges sur treize décisions » et en énumère **onze** (DL-1, 2, 4, 5, 7, 8, 11, 13 à quatre ; DL-3, 9, 12 à trois) ; le douzième est vraisemblablement DL-6 (option (1) pour les trois exemplaires versés), non nommé. Trois nombres pour une même grandeur : **erreur E4**. Pour N5, le texte décrit (c) écartée (vrai par construction, donc hors compte), choix 1, 5, 8, 10 à quatre, portée du plafond à trois, plus deux paires : 7, ou 6 si le choix 5 (« divergence de condition ») est exclu ; la règle d'exclusion n'est pas écrite.
- **Convergences (68)** : 13+6+8+4+10+4+5+18 = 68, conforme. « Au moins 24 retraits » : non vérifiable sans cellules.
- **Divergences** : 16 non résolues, numérotées (1) à (16) dans le corps et dans la liste du tour 2 : concordance exacte. 22 résolues : deux seulement sont nommées (N4, table des distances et population de la mesure) ; les vingt autres ne sont pas listées, donc non vérifiables.
- **Apports seuls (25 = 5+6+6+8)** : la somme est juste, la répartition n'est pas reconstructible depuis le texte. Comptés dans le corps : A 5 (N5 option (d), DL-3, DL-13, cohortes de N9, lien N3→N11) — conforme ; B **2** visibles (refus de hiérarchiser en N1, tolérance du pont de comptes en N9) pour 6 annoncés ; C 8 ou plus visibles (hachage du coffre, test d'invariance, garde de première arête, leviers sur sous-espaces nécessaires en N10, trois apports de N11, lien N5→N11) pour 6 annoncés ; D 5 visibles pour 8. **Et deux « apports seuls » sont repris**, contraire à la définition du critère 12 (« jamais repris ») : le pilote de variance scellé de D, « l'apport le plus cité du nœud » (N11), et le test d'invariance de C, sur lequel « les quatre convergent » (N5). La garde de première arête de C (N9) naît d'une critique de A : c'est une convergence au sens du critère 8 plutôt qu'un apport seul. **Erreur E2.**
- **Inexactitudes (4 = 0+2+1+1)** : somme juste. Renvoi « B (T1, N3 (c)) » : D-j n'a pas d'option (c), et le seuil B-ii appartient au test hors échantillon de N9 (même ligne 1449 des faits que l'inexactitude de D) ; le renvoi est au mieux elliptique (élément (c) de la cellule de B ?), à préciser. En N11, « B : retenu avec l'inexactitude signalée au décompte » renvoie à une inexactitude **absente** du décompte (les deux de B portent sur N3 et N4 ; la faute de B en puissance est classée « transposition », non inexactitude). **Erreur E3** (renvoi cassé, et classement contraire au critère 5).
- N9 : « 0,95 — la confiance la plus haute du tour, tous nœuds confondus » : C donne aussi 0,95 sur DL-4 (table de N6) ; ex æquo, non « la plus haute » à elle seule. Mineur.
- N1 : « la conjonction des variantes laisse 0,33 et 0,84 » ; la question donne 0,33 et **0,83** pour l'option D. Si la grandeur est la même, écart d'arrondi à vérifier sur les faits ; si elle diffère, la synthèse doit le dire. Mineur, exige les faits.

## 3. Calculs refaits

Conformes (recalculés en une ligne chacun) : 6,3178 − 3,4443 = 2,8735 ; 1 − C(6,2)/C(10,2) = 1 − 15/45 = 0,667 ; 28 × 0,5 = 14 et 28 × 0,7 = 19,6, racine(0,09/14) = 0,080, racine(0,09/19,6) = 0,068, 0,9^14 = 0,229, 0,9^19,6 = 0,127 ; (0,70/0,85)² = 0,678, (0,85/0,70)² = 1,4745, 2 600 × 1,4745 = 3 834 ; 150/118,6 = 1,265 et 140/118,6 = 1,180 ; racine(0,25/8) = 0,177 (maximum, remarque juste) ; (2,8)² × 0,4375/0,0625 = 54,9 ; racine(0,25/8 + 0,109/8) = 0,212, 1,96 × 0,212 = 0,415, (2,8)² × 0,355/0,04 = 69,6 ; test exact 0/8 contre 6/8 : p bilatéral = 2 × 28/8008 = 0,0070 ; 1,645 × racine(0,5/n) < 0,10 ⇔ n > 135,3 ; 1 − C(194,12)/C(200,12) = 0,3135 et 0,6865^20 = 0,00054 ≈ 0,0006 ; 0,5/0,11 = 4,5 erreurs types (« plus de quatre »).

**p minimal 1/6 (message de session-depot)** : exact pour une corrélation de rangs **entre deux** classements de trois bras (Spearman ou Kendall : 3! = 6 permutations, une seule donne ρ = 1 ; bilatéral 1/3). **Erreur E1, dans le recalcul du lecteur** : la synthèse calcule elle-même que trois classements indépendants concordent parfaitement avec probabilité (1/6)² = 1/36 ≈ 0,028, puis écrit « un seuil p < 0,05 a donc une probabilité de réalisation nulle » : c'est faux pour un test de concordance **à trois instruments** (W de Kendall, m = 3, n = 3), dont la concordance parfaite a p = 1/36 < 0,05. Énumération exacte des 36 issues (premier classement fixé) : W ∈ {0 (2), 1/9 (15), 1/3 (6), 4/9 (6), 7/9 (6), 1 (1)}. Donc « W ≥ 0,7 rejette le seul état intermédiaire possible » est faux deux fois : il existe quatre états intermédiaires, et W = 7/9 ≈ 0,78 **passe** le seuil 0,7 (P(W ≥ 0,7) = 7/36 ≈ 0,19 sous le nul) ; à deux instruments, W = (ρ + 1)/2 ∈ {0 ; 0,25 ; 0,75 ; 1}, et 0,75 passe aussi. La conclusion de fond (« non jugeable ») tient pour toute corrélation **par paire** ; pour la concordance à trois instruments, elle devient « jugeable seulement par l'unanimité, puissance très faible », ce qui ne change pas les cessions mais change la phrase qui les justifie et le message à Lazar. Quel test chaque espèce proposait (paire ou W) exige les cellules.

Non vérifiables sans les cellules : 0,037 « à trois instruments » et 0,11 « à deux » de A (égaux à 1/27 et 1/9 ; 1/9 est la probabilité que deux instruments s'accordent sur le premier bras d'un troisième, 1/27 suppose un bras désigné d'avance ou quatre instruments : possible décalage d'un rang) ; 0,89 / 0,80 de la pièce ; heures de N6 (SUPPOSÉ).

Vérifié sur le PDF empreinté (`2412.09565v2.pdf`) : p. 23, intervalle de confiance à 95 % de la corrélation couches–performance ; p. 25–26, l'entraînement du modèle renchérit l'attaque sans robustesse ; p. 26, orthogonalité non obtenue. Les attributions « pièce 24, p. 23 / p. 25–26 / p. 26 » de la synthèse sont cohérentes avec le PDF.

## 4. Ce que la synthèse omet ou déforme par rapport à la question

- **N11 (2)** : « combien » de ponts plantés n'est pas consolidé par espèce (seuls « au moins 50 » de B, « plus de 135 » et « douze » de C apparaissent, dans d'autres rubriques) ; « le risque que des ponts plantés ne ressemblent pas aux vrais » n'est pas traité comme rubrique (seulement indirectement : homologie de structure de C, récitation de D).
- **N11 (4)** : « la vérification hors du programme » demandée par la question n'est rapportée pour aucune espèce.
- **N6** : la question rapporte que le brouillon classe DL-2, DL-4, DL-6 en « périmètre interne d'une phase » (défaut à 48 heures) ; la synthèse ne dit pas si une espèce s'est prononcée sur ce point de hiérarchie (à relever à part, comme le critère 16 le fait pour N5).
- **N1** : options A, C, D, E : la synthèse note que nul ne les défend et que l'abandon est écarté « sans l'argumenter » : conforme.
- Aucun nœud posé n'est sans réponse (N1, N3, N4 avec CA1-04, N5 avec choix 1, 5, 8, 10 et portée du plafond, N6 DL-1 à DL-13, N9, N10, N11, liens, ordre). Les six liens de la question sont déclarés repris par les quatre (non vérifiable sans cellules).
- Le résumé de session-depot (30 / 16 / 25 / 4 ; p minimal 1/6 ; duels de N1 ; N11 (b), extension du monde ou sortie du bras méta) est fidèle à la synthèse ; il hérite de l'erreur E1 en présentant la non-jugeabilité sans restriction.

## 5. Verdict par nœud

| Nœud | Verdict | Motif |
|---|---|---|
| Décompte de tête | **à reprendre** | E2 (apports « seuls » repris ; répartition 5/6/6/8 non reconstructible), E3 (classement de la faute de B et renvoi cassé), E4 (N6) |
| N1 | tenu sous condition | condition : vérifier 0,84 contre 0,83 sur les faits ; « aucun des quatre duels ne tient » non jugeable sans cellules |
| N3 | tenu sous condition | condition : préciser le renvoi « (T1, N3 (c)) » de l'inexactitude de B |
| N4 | tenu | recalculs conformes ; divergence CA1-04 bien posée |
| N5 | tenu sous condition | le test d'invariance de C ne peut être à la fois « apport seul » et « mesure commune aux quatre » ; règle de comptage des accords (6 ou 7) à écrire |
| N6 | à reprendre (décompte seulement) | « neuf » / onze / douze accords larges ; point de hiérarchie DL-2, DL-4, DL-6 omis ; « réserve que je retiens » (critère 23) ; les divergences (6) à (10) sont bien posées |
| N9 | tenu | « la plus haute confiance » à nuancer (ex æquo DL-4) |
| N10 | tenu | attributions au PDF vérifiées |
| N11 | à reprendre | E1 (W et seuil p) ; renvoi d'inexactitude de B cassé ; pilote de variance de D compté « apport seul » bien que repris ; rubriques (2) « combien » et « ressemblance » et (4) « vérification hors programme » absentes |
| Liens et ordre | tenu | divergence (16) bien argumentée des deux côtés ; lien N1→N11 (extension du monde ou sortie du bras méta) bien sourcé à deux espèces |

## 6. Points qui exigeraient les cellules (ou les faits)

1. Les 22 divergences résolues et les 24 retraits : liste nominative.
2. La répartition des 25 apports seuls par espèce (B 6, D 8 en particulier).
3. Le test de concordance que chaque espèce proposait (corrélation par paire ou W à trois instruments), pour savoir si E1 change une cession.
4. Le contexte de l'inexactitude « B-ii = 0,50 » chez B (nœud et élément exacts).
5. Le chiffre de puissance de B en N11 (0,89 pour 5 points) et son classement (inexactitude ou transposition).
6. Les probabilités 0,037 et 0,11 de A et leur hypothèse.
7. 0,84 contre 0,83 (N1) et la ligne de la pièce 2 concernée.
8. Le bornage tronqué de la pièce 20 (N9-1) et l'affirmation que nulle espèce n'utilise rien au-delà.
9. La reprise des six liens de la question par les quatre espèces.
10. Les heures de lancement du lecteur (critère 25) dans le journal de session-depot.
