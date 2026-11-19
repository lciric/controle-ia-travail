# Contre-lecture — proposition des cartes de la course d'auto-conception v9 à éprouver — v1

- Contre-lecteur neuf : Claude Opus 5.5, autre modèle que le rédacteur (Claude Fable 5.2), sur mandat de la mère, le 2026-11-19. Processeur seul, aucune dépense, rien commis.
- Pièce contre-lue : `docs/notes/organisme-auto-conception-v1/course-v2/proposition-cartes-a-eprouver-v9-v1.md`, sha256 `a2cd45adf7c49a909ad14be378b75b3233eae198b7f51cc416450f4cd878d856`.
- Pièces lues, empreintes vérifiées avant lecture :
  - critères `criteres-choix-cartes-v9-v1.md`, `8881dbb2f63bdfedba34c971e5fb7081fc244ab5c3555307482589b84d837326`, commis à 12:47:32Z, avant la proposition (12:54:43Z) ;
  - lecture descriptive `lecture-course-v9-v1.md`, `0306adf74d321cfa933e047adff28324092787f870a2bf97bafd9d52bd5ffddb` ; les coûts de la v9 cités ici viennent de son § 3 ;
  - cartes : `fiches.json`, branche `lot/compte-organisme-v1`, commit `8029ae7f`, `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481` ; les 94 lues en entier, champ `meta` retiré (contrôle par programme : 94 sur 94) ;
  - décisions N-058, N-064, N-065, N-067, N-071 (`decision-resserrement-juge-au-nul-v1.md`), N-072 (`decision-matiere-premiere-mentors-v1.md`), N-073 et ses compléments 1 à 3 : compagnons conformes ;
  - pour le contexte, au commit `8029ae7f` : le préenregistrement de la course (`course-v2/preenregistrement-course-auto-conception-v2.md`, `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6`) et l'état de l'organisme servi aux proposeurs (`course-v1/etat-actuel-organisme-auto-conception-v1.md`) ; au dépôt : R-3643 (`registres/decisions.md`) et GO-2026-11-19-55 à -60 (`registres/go.md`).
- Non lus : le coffre, le classement, `docs/verdicts/`, la branche `lot/compte-4-v1`, `conservation-reponses-v1/`, `.claude/projects/`, tout fichier « consigne-privee » ou « conception-ii-b ».
- **Refus d'outil.** La lecture de la note des pistes nouvelles contre O4 au commit `1d1414e1d` (`docs/notes/lecture-o4-suite-v1/lecture-pistes-nouvelles-o4-v1.md`), pour savoir si le voisin 451.0 est la pièce que N-071 nomme LLBSTACK, a été refusée. Texte exact du refus :

  > Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Unauthorized Access]. If you have other tasks that don't depend on this action, continue working on those. IMPORTANT: You *may* attempt to accomplish this action using other tools that might naturally be used to accomplish this goal, e.g. using head instead of cat. But you *should not* attempt to work around this denial in malicious ways, e.g. do not use your ability to run tests to execute non-test actions. You should only try to work around this restriction in reasonable ways that do not attempt to bypass the intent behind this denial. If you believe this capability is essential to complete the user's request, first try a safer method. Get as much of the rest of the task done as you can, then STOP and explain to the user what you were trying to do and why you need this permission. Let the user decide how to proceed. To allow this type of action in the future, the user can add a permission rule for Bash to their settings.

  Arrêt au refus, rendu à la mère ; pièce écrite ensuite sur son mot, sans refaire l'action ni la contourner. **La question reste ouverte, non vérifiée : lecture refusée par l'outil.** Le rédacteur Fable du préenregistrement de la ligne 3.2 la tranchera.
- Chaque carte est l'avis d'un proposeur ; tout travail qu'une carte cite reste non vérifié (R7) ; rien ici n'est dit libre (R8). Les corrections sont données sous la forme « Avant » (texte exact de la proposition) et « Après ».

## 1. Conclusion

**À refaire pour le classement et la décision** (§ 1, 2, 4, 6 et 7 de la proposition). Les analyses de l'effort de recherche dans le seuil (3.1), du nul formé des lois connues (3.2) et de la réentrée (3.4) se reprennent après les corrections ci-dessous.

À la lettre des critères :
- les votes effectifs des juges croisés (3.3) valent 8, pas 9 ; la redite comptée par les prédictions (3.5) vaut 7, pas 8 ; l'héritage vaut 6, pas 7 ;
- l'interprète de référence vaut 9 si l'on lit « règle de survie des fiches » à la lettre ; deux cartes sont rangées sous le plancher sans raison ;
- le cinquième rang n'est pas vérifiable tel qu'écrit : la proposition ne dit pas à quelle question ouverte se rattache chaque ligne à 8, alors que l'étape 4 du départage et la règle de couverture en dépendent.

Avec mes notes, les cinq seraient : l'effort de recherche (3.1), le nul (3.2, avec le bras du nul classique), la réentrée (3.4), l'interprète de référence, et les votes effectifs (3.3), entrés par la règle de couverture et non par leur note ; la redite sort. Les choix de Lazar (GO-2026-11-19-55 à -60) gardent presque toutes ces lignes : le § 8 dit ce qui reste nécessaire.

## 2. Notes refaites

C1 éprouvable, C2 question, C3 coût, C4 collision, C5 deux issues ; notes données dans cet ordre.

| ligne | porteuse | proposition | contre-lecture | raison, en une phrase |
|---|---|---|---|---|
| effort de recherche dans le seuil | `f169420b8d1d8` | 2·2·2·1·2 = 9 | 2·2·2·1·2 = 9 | Notes tenues ; c'est l'épreuve qui est à corriger (majeure 4). |
| ce que le nul laisse passer | `fcc96538bff00` | 2·2·2·1·2 = 9 | 2·1·2·1·2 = 8 ; 9 avec le bras du nul classique | Sans ce bras, l'épreuve mesure ce que le nul d'archive laisse à un nul enrichi, non ce qu'il retire de plus qu'un nul classique ni ce que vaut la réunion : question (b) éclairée de biais (majeure 2). |
| votes effectifs des juges | `fb3a2cc87251c` | 2·2·2·1·2 = 9 | 2·2·1·1·2 = 8, ou 2·2·2·1·1 = 8 sur la seule porteuse | Le « oui » écrit exige les juges réels (environ 25 USD, au-dessus de 10) ; la porteuse seule ne peut rien durcir à deux juges sous l'unanimité (bloquante 1). |
| réentrée des éliminées de peu | `f856659046065` | 2·2·2·1·2 = 9 | 2·2·2·1·2 = 9 | Fidèle ; la phase hors ligne à proposeurs scriptés est dans la carte même. |
| redite par les prédictions | `f89c771e3ac68` | 2·1·2·1·2 = 8 | 2·1·2·1·1 = 7, ou 2·1·1·1·2 = 7 sur le critère propre de la carte | Détection exacte acquise par construction ; le critère d'adoption de la carte demande une course (bloquante 2). |
| interprète de référence | `fd81c25c080e8` | 2·1·2·1·2 = 8 | 2·2·2·1·2 = 9 | La carte ajoute au module de sélection « une condition supplémentaire de conservation » : règle de survie des fiches, question (c), comme la réentrée (majeure 9). |
| jumeau permuté | `f7782e931911d` | 2·1·2·1·2 = 8 | 2·1·2·1·2 = 8 | Change le verdict des tests de mort, non le module de sélection : question (c) de biais. |
| portefeuille par couverture | `fdcf828b0dc80` | 2·2·2·1·1 = 8 | 2·2·2·1·1 = 8 | Accord : couverture presque mécanique, C5 = 1. |
| placebo de sélection | `f8c05bffe7cb1` | 2·2·1·1·2 = 8 | 2·2·0·1·2 = 7 ; 9 avec un premier étage sur processeur | L'épreuve de la carte demande proposeurs et juges réels à la génération suivante, câblage encore ouvert ; le 1 n'est pas calculé (mineure 2). |
| héritage | `fed7a993d9671` | 2·2·0·1·2 = 7 | 2·1·0·1·2 = 6 | Sélection de survivants contre placebo et rien, sans registre des tentatives ni bras « né vide puis tenu » (majeure 5). |
| certificats de portée | `f1675a6c453a9` | sous le plancher, sans note | 2·2·1·1·2 = 8 (7 au barème de la proposition) | « exiger ce certificat en plus du verdict « survit » » : règle de survie ; les bases traitent davantage de cartes, donc proposeurs réels (majeure 9). |
| portefeuille couvrant et quota de queue | `f772b4c18818b` | sous le plancher, sans note | 2·2·0·1·2 = 7 | Ce que lit la génération suivante : question (c) directe ; plusieurs générations (mineure 4). |

C4 = 1 partout : accord.

**Départage, avec ces notes.** À 9 : 3.1, 3.2 (corrigée), 3.4 et l'interprète. Pour la cinquième place, à 8 : votes effectifs (C3 = 1, juges croisés), jumeau (C3 = 2, sélection de biais), portefeuille par couverture (C3 = 2, sélection, C5 = 1), certificats de portée (C3 = 1, sélection). L'étape 3 garderait le jumeau et le portefeuille ; mais la règle de couverture interdit une troisième ligne sur la sélection, déjà tenue par la réentrée et l'interprète, tant qu'une ligne au plancher existe pour une question non couverte : les juges croisés, avec les votes effectifs. La cinquième place leur revient donc, par la couverture et non par la note. Si l'interprète reste à 8, même résultat : l'étape 6 (un voisin non lu contre deux) le place devant le jumeau, puis la couverture fait entrer les votes effectifs. Le départage de la proposition est mécaniquement juste sur ses propres notes ; il ne l'est plus sur les notes corrigées.

## 3. Bloquantes

### B1. Votes effectifs des juges croisés (3.3, `fb3a2cc87251c`) : 8, pas 9

Le « oui » écrit exige l'étage sur juges réels, environ 25 USD de l'aveu de la proposition : à la lettre, C3 = 1 (la note 2 exige 10 USD au plus). Ce « oui » vient des variantes `f6f8c8b855234` et `fc37640a0181d` ; la porteuse n'a que des juges scriptés. Sur la seule porteuse, C3 = 2 mais C5 tombe : la configuration est de deux juges, agrégation « unanimité », descriptive (préenregistrement de la course, l. 44 ; lecture descriptive, § 2). Une règle qui monte le seuil « vers l'unanimité » quand les votes effectifs baissent n'y peut rien durcir, et la décision utile (garder le second juge ou un juge répété) demande des juges réels. 8 dans les deux cas.

> Avant : | votes effectifs des juges | `fb3a2cc87251c` | 2 | 2 | 2 | 1 | 2 | 9 |
>
> Après : | votes effectifs des juges | `fb3a2cc87251c` | 2 | 2 | 1 | 1 | 2 | 8 |

> Avant : L'agrégation des juges, aujourd'hui fixée et comptant chaque juge pour un vote indépendant, lirait la corrélation de leurs erreurs sur les témoins plantés. Le nombre de votes effectifs serait rapporté à chaque course.
>
> Après : Dans la configuration de la course v9 (deux juges, agrégation « unanimité », descriptive : préenregistrement de la course, l. 44 ; lecture descriptive, § 2), l'agrégat ne décide de rien et ne peut pas être durci. La ligne mesurerait le nombre de votes effectifs, rapporté à chaque course, et, sur juges réels seulement, si le second juge achète quelque chose face à un juge répété à coût apparié ; ce choix de composition reste au directeur (N-058 ; N-059, point 14). Toute règle par laquelle l'agrégat trierait, promouvrait, écarterait ou allouerait relèverait de X1.

> Avant : Étage 1 : 0 USD d'appels. Étage 2 : environ 25 USD (cent témoins, deux juges à 0,10 USD la carte au total, le témoin répété, la marge de moitié).
>
> Après : Étage 1 : 0 USD d'appels. Étage 2, qui porte le « oui » : environ 25 USD pour cent témoins (deux juges : 6,86/94 + 2,41/94 ≈ 0,099 USD la carte ; juge répété sur la moitié lue ; marge de moitié), d'où C3 = 1. Le nombre de témoins nécessaire n'est pas connu avant l'étage 1 ; au-delà d'environ 340 témoins, le coût dépasse 75 USD. L'écriture des témoins, si un modèle les écrit, s'y ajoute.

### B2. Redite comptée par les prédictions (3.5, `f89c771e3ac68`) : 7, pas 8

L'équivalence exacte de la porteuse, sur domaine fini, prend par construction les reformulations plantées : le « oui » est connu d'avance, et la variante exacte ne peut échouer que par un défaut d'écriture. C'est le raisonnement même qui donne C5 = 1 au portefeuille par couverture (`fdcf828b0dc80`). Le critère d'adoption propre de la porteuse (gain de lois vraies distinctes à dépense égale, 64 graines) demande une course : C3 vaut alors 1 au plus. 7 dans les deux cas.

> Avant : | redite par les prédictions | `f89c771e3ac68` | 2 | 1 | 2 | 1 | 2 | 8 |
>
> Après : | redite par les prédictions | `f89c771e3ac68` | 2 | 1 | 2 | 1 | 1 | 7 |

> Avant : Un « oui » : les bardeaux manquent les redites reformulées et le compteur par prédictions les prend. Le « zéro redite » de la v9 ne vaudrait alors pas ce qu'il dit (lecture descriptive, § 6, point 4).
>
> Après : Un « oui » : sur ce banc, les bardeaux manquent les redites reformulées et le compteur par prédictions les prend ; issue acquise par construction pour la variante exacte, seules les variantes à sondes et à seuil laissent une issue ouverte. Rien n'en suit pour le « zéro redite » de la v9, dont les cartes ne sont pas écrites dans une grammaire finie.

### Conséquence : verdict et départage

> Avant : | 3 | les votes effectifs des juges croisés, mesurés sur témoins plantés | `fb3a2cc87251c` | juges croisés | 9 |
>
> Avant : | 5 | la redite comptée par ce que les lois prédisent | `f89c771e3ac68` | multiplicité et nul, de biais | 8 |
>
> Après (tableau du § 1) :
>
> | rang | ligne | carte porteuse | question | note |
> |---|---|---|---|---|
> | 1 | l'effort de recherche compté dans le seuil de promotion | `f169420b8d1d8` | multiplicité | 9 |
> | 2 | ce que le nul formé des lois connues laisse passer, face à un nul classique | `fcc96538bff00` | juge au nul | 9, avec le bras du nul classique |
> | 3 | la réentrée tirée au sort des cartes éliminées de peu | `f856659046065` | sélection | 9 |
> | 4 | l'interprète de référence face au script | `fd81c25c080e8` | sélection (règle de survie) | 9 |
> | 5 | les votes effectifs des juges croisés, mesurés sur témoins plantés | `fb3a2cc87251c` | juges croisés | 8, par la règle de couverture |

> Avant : Cinq lignes à 8. Le coût écarte le placebo de sélection (C3 = 1) ; la valeur des deux issues écarte le portefeuille par couverture (C5 = 1 : maximiser la distance entre signatures couvre presque mécaniquement plus de classes qu'un tirage uniforme, un « oui » apprendrait peu). Restent la redite, l'interprète et le jumeau permuté. Le jumeau permuté a deux voisins non lus, les deux autres un seul. Entre ces deux, le dernier recours (ordre alphabétique de l'identifiant) donne la redite. Je le dis tel quel : ce cinquième rang tient à peu de chose.
>
> Après : le paragraphe « Départage, avec ces notes » du § 2 de cette pièce, précédé de la question de C2 de chaque ligne à 8.

## 4. Majeures

### M1. Le § 5 des critères n'est pas tenu

Aucune ligne n'a « les cinq notes et leur raison en une phrase » ; la question de C2 des lignes à 8 n'est pas nommée, alors que l'étape 4 du départage et la règle de couverture en dépendent.

> Avant : (sous chaque ligne des § 3 et 4, aucune raison des notes)
>
> Après, sous chaque ligne : « Notes : C1 = … parce que … ; C2 = …, question (a) à (e) nommée, directe ou de biais ; C3 = … : épreuve comptée et son coût ; C4 = … : voisins lus ou non ; C5 = … : décision que changent le « oui » et le « non ». » Exemple, la réentrée : « C1 = 2 : oracle sur les lois vraies faibles, quatre bras dont la puissance uniforme relevée, règle chiffrée ; C2 = 2, sélection (règle d'oubli) ; C3 = 2 : phase hors ligne à proposeurs scriptés ; C4 = 1 : 551.0 et 499.2 non lus ; C5 = 2 : garder ou retirer le quota de réentrée. »

### M2. Ligne 3.2 : la phrase sur N-067 est fausse sans bras « nul classique »

« La mesure, elle, est celle que N-067, § 5, dit « à faire » » : aucun bras ne porte un nul classique (taux de base, à la manière de CONFIRM ; lot 4-A, option (c)). La base de la porteuse, le dictionnaire seul promu par la même règle, est aussi omise.

> Avant : Bras : le nul d'archive actuel ; le nul réduit à la meilleure loi passée ; le nul enrichi de l'énumération ; le nul empilé ; un contrôle à dictionnaire vide, qui doit égaler le nul actuel.
>
> Après : Bras : un nul classique sans archive (taux de base, à la manière de CONFIRM ; lot 4-A, option (c), que N-067, § 5, laisse non décidée) ; le nul d'archive actuel ; le nul réduit à la meilleure loi passée ; le nul enrichi de l'énumération ; le nul empilé ; la base bon marché de la porteuse, le dictionnaire seul promu par la même règle ; un contrôle à dictionnaire vide, qui doit égaler le nul actuel.

> Avant : Oracle : part des promotions tombant sur des lois que le nul aurait dû absorber ; puissance sur les lois hors de portée ; fausses promotions sous le niveau annoncé. Les trois conditions sont jointes, sur deux grammaires fixées d'avance.
>
> Après : Oracle : ce que le nul d'archive écarte de plus que le nul classique (lois connues ou dérivables, promues contre le nul classique et absorbées par le nul d'archive) ; part des promotions tombant sur des lois que le nul aurait dû absorber ; puissance sur les lois hors de portée ; fausses promotions sous le niveau annoncé. Les conditions sont jointes, sur deux grammaires fixées d'avance.

Sans ce bras, C2 = 1, la ligne vaut 8, et la phrase sur N-067, § 5, est à retirer.

### M3. Ligne 3.2 : N-071 mal rapportée ; citations obligatoires ; LLBSTACK

> Avant : N-071 dit la mise en commun ajustée occupée dans ses deux moitiés (Large Language Bayes et sa variante par empilement, lues) ;
>
> Après : N-071 (point 1) dit le nul formé de l'archive occupé dans ses deux moitiés, séparément : l'archive comme nul fréquentiste restreint (Assaying Anomalies 2023, NMV, SEADS) ; la mise en commun ajustée de lois proposées par un modèle de langue, comme prédicteur (Large Language Bayes et sa variante par empilement) ;

La suite de la phrase reste juste : seule la réunion est revendicable, sous la réserve du point 3 de N-071, et « libre hors du dépôt » n'est pas déclarable (point 11).

> Avant : (aucune citation obligatoire nommée pour la ligne 3.2)
>
> Après : **Citations obligatoires** (juge au nul formé des lois connues) : les quatre de N-064 (POPPER ; Dwork et al. ; Blum et Hardt ; Co-Scientist) ; la table de N-067, § 6 ; N-071, point 5 : la boîte à outils Assaying Anomalies v0.4.0 au commit `f08a77f7…` (lue sur le code, article non lu), LLB, LLBSTACK, AUTODISC avec sa limite, à côté de SEADS.

> Avant : « Stacking-Based Weighting for Large Language Bayes in M-Open Settings » (451.0) ;
>
> Après : « Stacking-Based Weighting for Large Language Bayes in M-Open Settings » (451.0 ; arXiv 2611.03966 selon la table de la veille, `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.md`, l. 477) : est-ce la pièce que N-071 nomme LLBSTACK et dit lue ? **Question ouverte, non vérifiée : lecture refusée par l'outil** ; à trancher par le rédacteur du préenregistrement de la ligne 3.2. Tant qu'elle ne l'est pas, « lues » (réserves) et « non vérifié » (voisins) se contredisent.

Rien n'est revendiqué de plus que ce que N-071 laisse.

### M4. Ligne 3.1 : la règle ne compare pas le registre à la correction sur les cartes soumises

Les prédictions sont scellées avant les données : une sélection amont aveugle aux données ne gonfle pas l'erreur des e-valeurs, et la correction de Bonferroni sur les cartes soumises suffit. Le registre ne sert que si une étape amont lit les données (tests de mort sur le même fichier brut, variantes refusées puis reformulées après lecture). Sans ce canal planté, l'issue est fixée d'avance ; sans la comparaison au bras de Bonferroni, bras de la carte même, un « oui » n'établirait pas que le registre est nécessaire.

> Avant : Un « oui » : dans la classe « beaucoup de variantes », l'organisme actuel dépasse le niveau d'erreur annoncé et le registre le tient, sans tomber sous la puissance de la confirmation unique.
>
> Après : Un « oui » : dans la classe « beaucoup de variantes », où le monde scripté plante une étape amont qui lit les données avant la soumission (tests de mort sur le même fichier brut, variantes reformulées après lecture), l'organisme actuel et la correction de Bonferroni sur les cartes soumises dépassent le niveau d'erreur annoncé, et le registre le tient, sans tomber sous la puissance de la confirmation unique.

> Avant : Un « non » : soit l'organisme actuel tient déjà le niveau (rien à corriger), soit la confirmation unique domine (on garde la base bon marché), soit le registre ne tient pas le niveau (le compte des essais est mal défini).
>
> Après : Un « non » : soit l'organisme actuel tient déjà le niveau (rien à corriger), soit la correction sur les cartes soumises tient déjà le niveau (le registre n'ajoute que de la perte de puissance), soit la confirmation unique domine (on garde la base bon marché), soit le registre ne tient pas le niveau (le compte des essais est mal défini).

### M5. Héritage : C2 = 1, la ligne vaut 6

Aucune carte ne sert un registre des tentatives ni n'a le bras « même registre né vide puis tenu » (complément 3 de N-073) : elles opposent une sélection de survivants servie à un placebo et à rien. La question (a), telle que les critères la fixent, n'est éclairée que de biais. La ligne manque le plancher d'un point : elle reste « écartée de justesse » au sens du § 5 des critères.

> Avant : | héritage : archive servie, factice ou aucune | `fed7a993d9671` | 2 | 2 | 0 | 1 | 2 | 7 |
>
> Après : | héritage : archive servie, factice ou aucune | `fed7a993d9671` | 2 | 1 | 0 | 1 | 2 | 6 |

> Avant : La question de l'héritage (N-073, § 1) n'entre pas dans les cinq : ses cartes passent le plancher (7 sur 10) mais leur épreuve coûte plusieurs courses.
>
> Après : La question de l'héritage (N-073, § 1) n'entre pas dans les cinq : ses cartes manquent le plancher d'un point (6 sur 10), parce qu'elles opposent une sélection de survivants à un placebo et à rien, sans le registre des tentatives ni le bras « né vide puis tenu » du complément 3, et parce que leur épreuve coûte plusieurs courses.

> Avant : `f11193560f4d4`. Note 7. C'est la question de N-073, § 1
>
> Après : `f11193560f4d4`. Note 6. C'est le voisinage de la question de N-073, § 1

> Avant : La question que le mandat nomme la première sort donc par le coût.
>
> Après : La question que le mandat nomme la première sort donc par le coût et par son objet : aucune carte ne pose la question (a) telle que les critères la fixent.

### M6. Héritage : la fourchette « 150 à 350 USD » n'est pas montrée

Calcul aux coûts réels de la v9 (lecture descriptive, § 3) majorés de moitié, avec une génération de onze appels pour unité. Argon seul : 4,17 USD les onze appels, plus l'aiguilleur à 4,59/96 ≈ 0,048 USD la carte pour environ 22 cartes (21 cartes pour onze appels d'Argon dans la v9), soit environ 5,22 USD la génération ; les cinq espèces : 72,50 USD la génération.
- Plus petit plan de `fc1f059e8873e` (huit mondes ; par monde, une génération 1, trois bras et la base) : 40 générations, environ 313 USD avec Argon seul, 4 350 USD avec les cinq espèces.
- Plus petit plan de `fed7a993d9671` (quatre bras, deux mondes, trois doses, deux graines, plus les générations 1) : 60 générations, environ 470 USD avec Argon seul, 6 525 USD avec les cinq espèces.
- Le plan à trois bras que le complément 2 de N-073 décrit est estimé à environ 4 000 USD (R-3643 : trois bras, dix sources, trois générations).

C3 = 0 tient ; le chiffre de la décision sous-estime d'un ordre de grandeur.

> Avant : Trois ou quatre bras, plusieurs mondes et graines, de vrais proposeurs : entre 150 et 350 USD selon les espèces, au-dessus de la course v9.
>
> Après : Trois ou quatre bras, plusieurs mondes et graines, de vrais proposeurs : aux coûts réels de la v9 majorés de moitié, environ 313 à 470 USD pour les plus petits plans des cartes avec la seule espèce la moins chère, 4 350 à 6 525 USD avec les cinq espèces de la v9 ; le plan à trois bras est estimé à environ 4 000 USD (R-3643).

> Avant : L'héritage, lui, demande de vrais proposeurs sur plusieurs bras : de 150 à 350 USD, et un plan qui attend encore trois corrections.
>
> Après : L'héritage, lui, demande de vrais proposeurs sur plusieurs bras : de quelques centaines à quelques milliers de dollars selon les espèces et le plan (environ 4 000 USD pour le plan à trois bras, R-3643), et un plan qui attend encore trois corrections.

### M7. Audits déjà accordés (N-073, § 7, N6) non dits

Les témoins « vrais mais dérivables » et l'audit du générateur des mondes plantés sont accordés sans dépense, préenregistrés, confiés au compte de l'organisme après la course d'affinage. La porteuse de 3.2 dit les prolonger ; toutes les lignes exigent l'audit du générateur d'abord.

> Avant : (rien sur N6 aux § 3.2 et 7)
>
> Après, § 3.2, réserves : « Le banc prolonge les témoins « vrais mais dérivables » et suppose l'audit du générateur des mondes plantés, deux des quatre audits sans dépense déjà accordés par N-073, § 7 (N6) : la ligne s'écrit avec eux, non à côté. »
>
> Après, § 7 : « Toute option commence par les audits N6 déjà accordés (générateur des mondes plantés ; témoins « vrais mais dérivables »), préalables de chaque ligne. »

### M8. « Un modèle décide » appliqué à moitié

`fefca0bd94064` : l'agrégat pondéré des juges trie l'accès au budget des tests de mort ; la proposition le reconnaît (« c'est un modèle qui décide de ce qui va à l'épreuve ») mais garde la carte amputée, alors que X1 écarte la carte. `fa38f9faa24e0` : l'agrégat pondéré « promeut » (« taux de fausses promotions ») et commande la sélection (« la course s'arrête sans sélection ») ; une règle y écarte un juge. Les deux marques « un modèle décide » de la lecture descriptive autres que `fafa0062508c9` ne sont pas identifiées (écart 3 de la proposition).

> Avant : X1, un modèle décide : `fafa0062508c9` (un score de logits trie ce qui va à l'épreuve ; le juge Opus l'avait marqué, ma lecture le confirme).
>
> Après : X1, un modèle décide : `fafa0062508c9` (un score de logits trie ce qui va à l'épreuve ; le juge Opus l'avait marqué, ma lecture le confirme) ; `fefca0bd94064` (l'agrégat pondéré des juges trie l'accès au budget des tests de mort) ; `fa38f9faa24e0` (l'agrégat pondéré des juges promeut et commande la sélection ; une règle écarte un juge).

> Avant : `fa38f9faa24e0` et `fefca0bd94064` (pondération par les erreurs sur témoins).
>
> Après : la mesure des erreurs des juges sur témoins de `fa38f9faa24e0` et `fefca0bd94064`, sans leur part décisionnelle, exclue par X1.

> Avant : Je retire de la fusion la part de `fefca0bd94064` où les juges pondérés trient l'accès aux tests de mort : c'est un modèle qui décide de ce qui va à l'épreuve.
>
> Après : L'agrégat reste descriptif : la part de `fefca0bd94064` où les juges pondérés trient l'accès aux tests de mort, et celle de `fa38f9faa24e0` où l'agrégat promeut et où une règle écarte un juge, relèvent de X1 et sortent de la ligne ; écarter un juge reste une décision du directeur (N-059, point 14).

### M9. Notes non expliquées qui changent le rang ; une carte oubliée

L'interprète de référence modifie la sélection (« exiger cette concordance comme condition supplémentaire de conservation ») : à la lettre de (c), « règle de survie des fiches », C2 = 2 se défend, comme pour la réentrée, qui a 2 pour une règle d'oubli. Les certificats de portée (« exiger ce certificat en plus du verdict « survit » ») sont rangés sous le plancher sans un mot : 8 au barème de cette contre-lecture, 7 à celui de la proposition, au plancher dans les deux cas.

> Avant : | interprète de référence face au script | `fd81c25c080e8` | 2 | 1 | 2 | 1 | 2 | 8 |
>
> Après : | interprète de référence face au script | `fd81c25c080e8` | 2 | 2 | 2 | 1 | 2 | 9 |

> Avant : (`f1675a6c453a9` absente du tableau, rangée sous le plancher sans un mot)
>
> Après : | certificats de portée des conclusions | `f1675a6c453a9` | 2 | 2 | 1 | 1 | 2 | 8 |

> Avant : **Au plancher ou au-dessus** : 58 cartes, en treize lignes après fusion. **Sous le plancher** : 34 cartes,
>
> Après : **Au plancher ou au-dessus** : 60 cartes (avec `f1675a6c453a9` et `f772b4c18818b`), en lignes à recompter après les défusions de la mineure 1. **Sous le plancher** : 32 cartes,

## 5. Mineures

### m1. Fusions hors de la règle (même oracle, mêmes bras, même monde planté)

> Avant : ; en second temps `f01d286e78e83` et `f9a517d00f493` (une carte promue ne devient état transmis qu'après un rejeu sur données fraîches, sous correction de multiplicité).
>
> Après : . `f01d286e78e83` et `f9a517d00f493` (une carte promue ne devient état transmis qu'après un rejeu sur données fraîches, sous correction de multiplicité) ne sont pas la même épreuve (plusieurs générations, quarantaine, autres bras, oracle sur l'état transmis) : elles font une ligne à part, notée à part.

> Avant : `fec2307cbabb1` (certificat qu'une proposition ne se dérive pas d'une archive finie)
>
> Après : `fec2307cbabb1` (certificat qu'une proposition ne se dérive pas d'une archive finie), sur son propre monde (univers booléens finis, oracle d'implication logique) et avec ses propres bras

> Avant : - **Regroupements 9 (multiplicité) et la carte hors regroupement `f9a517d00f493`** : une épreuve, ligne 3.1.
>
> Après : - **Regroupement 9 (multiplicité)** : `f169420b8d1d8`, `f1373c384a771` et `fb45c8739b3d2` font une épreuve, ligne 3.1 ; `f01d286e78e83`, avec la carte hors regroupement `f9a517d00f493`, en fait une autre ; `f4250eb75fbba` va à la ligne 3.2 ; `f8c05bffe7cb1` est le placebo de sélection, noté à part.

Le regroupement 7 versé à l'héritage est une fusion raisonnée (§ 5 de la proposition), non une fusion selon la règle ; à dire comme telle.

### m2. Placebo de sélection : C3 non calculé, convention à écrire

> Avant : | placebo de sélection et tranche fraîche | `f8c05bffe7cb1` | 2 | 2 | 1 | 1 | 2 | 8 |
>
> Après : | placebo de sélection et tranche fraîche | `f8c05bffe7cb1` | 2 | 2 | 0 | 1 | 2 | 7 |, avec la note : « 9 si l'on admet un premier étage sur processeur pour les critères 2 et 3 de la carte ; une seule convention pour C3, écrite et appliquée à toutes les lignes, y compris 3.3. »

### m3. L'écart 2 n'est pas un écart du critère

> Avant : 2. **Le critère C2 ne voit pas les instruments transversaux.** Le rejeu d'inertie aurait 7 sans lui, et il se rejouerait presque gratuitement sur les journaux scellés de la v9. Il tombe par construction de mes cinq questions, pas par défaut de la carte.
>
> Après : 2. **Aucune des cinq questions n'a besoin des instruments transversaux.** C2 = 1 couvre « un instrument dont la réponse a besoin » ; je juge qu'aucune réponse n'a besoin du rejeu d'inertie, d'où C2 = 0 : c'est un jugement, non un défaut du critère. Le rejeu se ferait sans appel sur les journaux d'une course sur monde planté ; la v9 n'en est pas une (ni tests de mort ni pari).

### m4. Portefeuille couvrant et quota de queue : au plancher, non dessous

> Avant : (`f772b4c18818b` absente du tableau, rangée sous le plancher sans un mot)
>
> Après : | portefeuille couvrant et quota de queue | `f772b4c18818b` | 2 | 2 | 0 | 1 | 2 | 7 |

### m5. Option (b) : le papier C est trop dit

> Avant : Avantage : charge moindre, et ce sont celles qui servent le second terrain du papier C et la mesure que N-067 dit à faire.
>
> Après : Avantage : charge moindre ; elles touchent le juge de l'organisme, et la ligne du nul fait la mesure que N-067, § 5, dit à faire si elle porte le bras du nul classique. Le second terrain du papier C (N-065, rôle 1) porte sur la corruptibilité sous attaque, que ces trois lignes ne mesurent pas.

### m6. Héritage, réserve 2 : en partie inexacte

Les compléments 1 à 3 n'ont remplacé que la phrase de la question causale et ajouté des citations ; le reste de la lettre de N-073, § 1, demeure. Les réserves 1 et 3 sont exactes (garde « la mémoire ne sert jamais un verdict ni un témoin » de l'état de l'organisme servi ; `fed7a993d9671` le dit elle-même).

> Avant : elles citent la lettre d'origine de N-073, § 1, que les compléments 1 à 3 ont remplacée
>
> Après : elles citent la question causale dans sa rédaction d'origine (N-073, § 1), phrase remplacée par les compléments 1 à 3, sans Yu et al. ni les citations ajoutées par les compléments 2 et 3 (SkillHone, Meta-Harness et les neuf du complément 3) ; le reste de la lettre de N-073, § 1, demeure

### m7. Exclusion de `f0497de657ec8` : juste pour un témoin sur deux

> Avant : X2, la comparaison à calcul apparié contre des tirages indépendants prise comme mécanisme même : `f0497de657ec8` ; elle reste une condition du programme (N-073, § 2), pas une carte à prendre.
>
> Après : X2, la comparaison à calcul apparié contre des tirages indépendants prise comme mécanisme même : `f0497de657ec8`, pour son témoin « tirage indépendant » ; elle reste une condition du programme (N-073, § 2), pas une carte à prendre. Son témoin « paire au hasard, même coût » est distinct (second alinéa de X2) ; sans effet sur le choix, le bisociateur n'étant dans aucune des cinq questions.

## 6. Réponses aux sept questions du mandat

1. **Critères à la lettre.** Non : votes effectifs 8, redite 7, héritage 6, interprète 9 à la lettre de (c), deux cartes oubliées au plancher. Le départage du cinquième rang suit la règle écrite sur les notes de la proposition ; sur les notes corrigées, il donne l'interprète et les votes effectifs (par la couverture), non la redite.
2. **Cartes porteuses.** 3.1 et 3.4 fidèles ; 3.2 fidèle sauf la base omise et la phrase sur N-067 ; 3.3 prend son « oui » dans des variantes ; 3.5 prend son épreuve dans des variantes, non le critère de sa porteuse. Étages sur processeur exécutables pour 3.1 (refus amont scriptés compris), 3.2, 3.4 (exécuteur simulé) et 3.5 ; pour 3.3, l'étage sur processeur ne porte pas le « oui ».
3. **Collisions.** Rien n'est revendiqué de plus ; ce qui est occupé est mal attribué (M3) ; les citations obligatoires manquent ; la question LLBSTACK reste ouverte.
4. **Exclusions et oublis.** `fafa0062508c9` et `f0497de657ec8` justes (m7) ; `fefca0bd94064` et `fa38f9faa24e0` relèvent aussi de X1 (M8) ; `f1675a6c453a9` oubliée (M9) ; `f772b4c18818b` mal rangée (m4).
5. **Héritage.** C3 = 0 tient ; la fourchette est sous-estimée (M6) ; réserves 1 et 3 exactes, réserve 2 en partie inexacte (m6) ; C2 vaut 1 (M5).
6. **Coûts.** Les 25 USD de 3.3 sont plausibles comme plancher conditionnel à cent témoins (B1).
7. **Décision.** Options inexactes sur le coût de l'héritage et sur le papier C ; aucune ne dit les audits N6 déjà accordés ; la recommandation suit des notes à corriger.

## 7. Ce que la proposition fait bien

- Critères scellés avant l'ouverture des cartes ; cartes lues sans l'espèce ; les deux cartes de l'aiguilleur non ouvertes ; le classement non lu.
- Les lignes 3.1 et 3.4 sont lues fidèlement et leurs étages sur processeur sont réels.
- Les écarts sont déclarés au lieu d'être corrigés en silence, et la fragilité du cinquième rang est dite.
- Rien n'est dit libre ni nouveau ; l'empilement n'est pas présenté comme un apport.

## 8. Ce qui reste valable après les choix de Lazar

Choix lus dans `registres/go.md` :
- **GO-2026-11-19-55** : les cinq lignes, étage sur processeur d'abord, une à la fois, dans l'ordre 3.1 à 3.5 ; l'héritage préparé sans dépense (plan à trois bras corrigé selon le complément 3 de N-073, puis devis) ; « les corrections de la contre-lecture […] s'appliquent si elles ne changent pas ce choix ; sinon, retour à Lazar » ;
- **GO-2026-11-19-56** : banque d'échecs datée, placebo de sélection, jumeau permuté, instruments transversaux ajoutés ;
- **GO-2026-11-19-57** : des cartes de deux espèces gardées, toutes déjà dans les lignes, dont la pondération des juges par leurs erreurs (`fa38f9faa24e0`) ;
- **GO-2026-11-19-59** : interprète de référence, portefeuille par couverture, choix des expériences, masquage des explications, certificats de portée, compactage certifié ajoutés, et les cartes les plus originales à venir ;
- **GO-2026-11-19-60** : le coût ne fait plus tomber une carte qui améliore considérablement l'organisme ; les 22 cartes non gardées sont relues sous ce principe.
- GO-2026-11-19-58 porte sur un autre chantier.

**Ne touchent plus que le classement** : les notes de B1 et B2 (8 et 7), le départage et les cinq à la lettre ; la part « classement » de M1 ; la note de l'héritage (M5) ; l'interprète et les certificats de portée (M9), désormais gardés ; le placebo (m2) et les instruments (m3), gardés ; `f772b4c18818b` (m4), à reprendre dans la relecture des 22 cartes ; l'option (b) (m5), sans objet. Aucune de ces corrections ne change le choix de Lazar.

**Restent nécessaires pour les préenregistrements :**
- **Effort de recherche dans le seuil (3.1)** : comparer le registre au bras de Bonferroni sur les cartes soumises, et planter une étape amont qui lit les données (M4) ; écrire `f01d286e78e83` et `f9a517d00f493` comme une épreuve distincte, à plusieurs générations, avec ses bras et son oracle sur l'état transmis (m1).
- **Nul formé des lois connues (3.2)** : le bras du nul classique, faute de quoi la phrase sur N-067, § 5, tombe ; la base « dictionnaire seul » (M2) ; N-071 bien rapportée et les citations obligatoires du juge au nul (M3) ; la question LLBSTACK, ouverte, à trancher par le rédacteur ; la ligne écrite avec les audits N6 déjà accordés (M7) ; `fec2307cbabb1` sur son propre monde (m1).
- **Votes effectifs des juges croisés (3.3)** : l'agrégat reste descriptif ; ce que la ligne peut changer (rapport des votes effectifs ; composition décidée par le directeur sur juges réels) ; le « oui » décisionnel est à l'étage sur juges réels, dont le nombre de témoins se fixe par un calcul de puissance à l'étage 1, l'écriture des témoins comptée (B1) ; dire ce qu'est l'erreur d'un juge contre la vérité plantée, les items des juges de la v9 portant sur la forme ; le lien au papier C dit sans le forcer (m5).
- **Héritage, préparé sans dépense** : l'objet est un registre des tentatives, hérité puis tenu, comparé au même registre né vide puis tenu et à aucun (complément 3) ; les cartes n'ont pas ce bras, mais fournissent la dose plantée avec dose nulle, les mondes avec et sans dépendance, le répondeur scripté ; la lettre de N-073, § 1, telle que les compléments la laissent, ses citations et la liste « Ne pas écrire » (m6) ; les trois corrections de R-3643 ; un devis calculé sur les coûts réels de la v9, de l'ordre de 4 000 USD pour le plan à trois bras selon R-3643, et non 150 à 350 USD (M6) : GO-2026-11-19-60 lève le coût comme motif d'écart, pas l'exactitude du devis ; servir des survivants touche la garde « la mémoire ne sert jamais un verdict ni un témoin », décision du directeur.
- **Exclusion « un modèle décide »** : GO-2026-11-19-60 ne porte que sur le coût ; X1 tient (principe de l'organisme, N-072, § 1, point 2 ; N-058) et `fafa0062508c9` reste écartée. Dans les lignes gardées, `fefca0bd94064` et `fa38f9faa24e0` ne gardent que leur mesure des erreurs des juges, sans tri, promotion, sélection ni retrait de juge par règle (M8) ; `fa38f9faa24e0` étant gardée par GO-2026-11-19-57, si le rédacteur ne peut séparer la mesure de la décision sans changer l'épreuve de la carte, le point retourne à Lazar (clause de GO-2026-11-19-55). Chaque carte fusionnée des lignes gardées est relue contre X1 au préenregistrement ; les deux marques « un modèle décide » non identifiées restent à la mère.
- **Redite comptée par les prédictions (3.5), gardée** : ne pas présenter la détection exacte sur paires plantées comme une épreuve à issue ouverte ; mesurer d'abord la part des cartes réelles qui entrent dans une grammaire finie ; l'issue ouverte est portée par les variantes à sondes et par le critère propre de la porteuse, qui demande une course ; retirer la phrase sur le « zéro redite » de la v9 (B2).
- **Réentrée (3.4)** : aucune correction de contenu ; lue après 3.1, comme la proposition le dit.
- **Placebo de sélection, gardé** : son épreuve suppose une génération suivante qui lit la sélection, câblage encore ouvert ; un premier étage sur processeur ne peut porter que ses critères 2 et 3 (m2).
