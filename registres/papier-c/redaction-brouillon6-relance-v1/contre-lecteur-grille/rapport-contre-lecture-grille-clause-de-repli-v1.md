# Contre-lecture du rapport de la grille de la clause de repli (stabilité de rang du papier C) — v1

Contre-lecteur neuf, autre modèle (Opus 5.5) que l'auteur du rapport (Claude Fable 5.2) ; n'a écrit ni le rapport, ni
ses programmes, ni le texte. Fait le 2026-11-19. Instrument de méthode, classe B : mesure de conception sur données
simulées, jamais un résultat. Rien lu sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun fichier interdit ouvert ;
aucune dépense, aucun réseau, aucun autre agent ; aucune modification du dépôt ni du dossier `grille/`.

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/ea38fd7e-2b5a-5aae-9611-af6160a314d6/scratchpad/bloc-notes/`
(noté `bloc-notes/`).

## 1. Pièces lues et empreintes

| pièce | empreinte | état |
|---|---|---|
| `grille/rapport-grille-clause-de-repli-v1.md` | `8d1616fce0dc59ea6bd986e465ae24efd845e1db7954cb39d39399fbc1a6ea89` | conforme à l'attendu |
| `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-c2.md` (dépôt) | `7a8d57c8c8c9a3c3aa77c708e7d4aab46d0c19e0e3b6c5f2d66bbc5b94421f61` | conforme |
| `brouillons/…-2026-11-19-r1.md` (dépôt ; bloc « Stabilité de rang » seul, comparé au c2) | `e12f16fa1460149344cd5d68b614294ea502c4c7fc24bc86970cafcfbaafc8b2` | conforme à son compagnon |
| `grille/programmes/grille_commun_v1.py` | `6458120e…92a609c4e7` | égal au manifeste d'avant lancement |
| `grille/programmes/grille_ab_v1.py` | `7df353b1…a70b84a94` | idem |
| `grille/programmes/grille_c_v1.py` | `8844a04a…e18746f43` | idem |
| `grille/sha256sums-programmes-avant-lancement.txt` | `c5bc961a…5bd0a47b6` | daté 12:49:24 UTC, avant `FINI_c_passe0` (13:07) et `FINI_ab_passe0` (13:52) |
| `grille/sha256sums-sorties-v1.txt` | `9ab5c8a8…de2988048` | 198 lignes, toutes vérifiées « OK » |
| `grille/archive/*` (4 fichiers) | conformes à `grille/sha256sums-archive-v1.txt` | lus : `commun_b5_v1.py`, `t2_rang_temoins_partages_v1.py`, début de `t1_…` |
| Programmes du rédacteur, `registres/papier-c/redaction-brouillon6-relance-v1/redacteur/travail/rejeu-grille-c1/` (`commun_cb6_v1.py`, `u1_…`, `u3_…`) | non recalculées | lus pour l'écart 0,186 / 0,227 seulement |

Lus dans le texte c2 : verrou 10 (l. 178 à 184) ; bloc « Stabilité de rang » et clause (l. 543 à 589) ; Métrique,
points 1 à 13 (l. 666 à 795) ; Seuil (l. 935 à 937) ; Plan, section 2 (l. 1066 à 1096) et section 3 (l. 1098 à 1215) ;
réserve 15 ; Critères de lecture gelés ; liste d'arrêt 16 à 19.

## 2. Verdict d'ensemble

Le code est fidèle au texte sur les quatre points demandés (statistiques, trois lectures, règle « établie », seuil) : je
n'ai trouvé aucun écart, et cinq cases rejouées avec leur graine redonnent les sorties à l'identique. Le mécanisme
principal de C-P3c (même cellule S et même D₀ pour les deux gains d'écart) découle du texte, et je l'ai retrouvé avec un
programme indépendant. Deux points changent cependant la portée des conclusions :

- la conclusion « la clause joue pour C-P3c » ne tient sans condition que si l'on **ne tient pas compte** des tirages
  dégénérés (lecture (i) de l'ambiguïté A6). Avec la lecture (ii), les seize cases « aucune attaque » qui la portent
  deviennent illisibles (taux 0). La clause ne joue alors que par le second mécanisme, qui dépend de l'hypothèse G4 ;
- le texte r1 fait dépendre la version (a) de D-9 d'un rapport « qui couvre la grille entière ». Or le rapport dit
  lui-même (A1) que la « grille entière » n'a pas de sens exact. Tant que le texte ne donne pas une liste finie de
  cases, la condition n'est pas décidable.

Décompte : 1 bloquante, 3 majeures, 10 mineures.

## 3. Remarques

### CG-01 — bloquante — « grille entière » indécidable, alors qu'elle commande la version de D-9

- **Lieu** : texte r1, bloc « Stabilité de rang » (« la version (a) ne vaut que si le rapport de la grille entière […]
  est rendu avant le scellement […] ; s'il ne couvre pas la grille entière et C-P3c, la version (b) s'applique ») ; texte
  c2, l. 583 à 586 (la grille est écrite en plages : « écart type 0,3 à 0,6 », « κ jusqu'à 0,16 », « les trois juges
  pouvant différer ») ; rapport, A1 (« « La grille entière » n'a pas de sens exact ») et section 9 (« E40 à g = 0,20
  n'est joué par personne »).
- **Constat** : aucune simulation finie ne couvre des plages continues. Le rapport joue les bornes, un cas hétérogène par
  mécanisme et deux mélanges. C'est un choix raisonnable, mais ce n'est pas « la grille entière ». La case homogène
  d'erreur 0,4 à g = 0,20 manque même dans le plan propre du rapport. Faute d'une définition, savoir si la version (a) ou
  la version (b) s'applique devient une affaire de jugement, alors que le texte veut une condition mécanique.
- **Correction demandée** (au texte, avant le scellement, par son rédacteur, puis mot du directeur) : remplacer les
  plages par une **liste finie de cases**, écrite d'avance : modèles d'erreur, attaques, k, T, R minimal, nombre de
  tirages. Par exemple, les 8 modèles du rapport × 3 attaques × 2 × 2. Puis jouer les cases de cette liste qui manquent
  (au moins E40 à g = 0,20 pour C-P3a et C-P3b). Autre voie : que le directeur déclare par écrit que le jeu du rapport
  vaut « grille entière ». Au rapport : écrire en section 1 que la couverture est celle d'une liste choisie par lui, et
  non la grille du texte.

### CG-02 — majeure — la conclusion de C-P3c dépend de la lecture des tirages dégénérés (A6), ce que le rapport ne dit pas

- **Lieu** : rapport, section 1, ligne C-P3c ; section 6.2 : « les seize cases « aucune attaque » sous l'erreur seule
  suffisent, et elles ne dépendent ni de G4, ni de k_P, ni de la valeur du gain du plaidoyer » ; A6 (« La lecture (ii)
  ne charge pas la clause »). Texte, point 11 (l. 758 et 759), liste d'arrêt 17 et « Critères de lecture gelés » (« une
  statistique « non identifiable » est écrite telle quelle »).
- **Constat** : sans attaque, ĉ n'est pas identifiable pour les Ḡ nets des familles 1 et 4, qui sont deux des quatre
  évaluateurs de C-P3c. Le programme de C-P3c ne fait aucun rééchantillonnage, donc il ne peut pas voir ce cas. J'ai
  rejoué C-P3c avec un vrai rééchantillonnage (B = 1 000, 2 000 essais, seuil 0,0597) et compté la lecture (ii) :

  | case | part lisible | insertion (i) | insertion (ii) | contenu (i) | contenu (ii) |
  |---|---|---|---|---|---|
  | E30, g = 0, k = 3, T = 45 | 0,000 | 0,085 | **0,000** | 0,081 | **0,000** |
  | E30, g = 0,10, k = 5, T = 60 | 0,913 | 0,061 | 0,056 | 0,058 | 0,052 |
  | E60, g = 0,10, k = 5, T = 60 | 0,031 | 0,057 | 0,001 | 0,060 | 0,001 |
  | M616, g = 0,10, k = 3, T = 45 | 0,002 | 0,051 | 0,001 | 0,061 | 0,000 |
  | KH, g = 0,10, k = 5, T = 60 | 0,590 | 0,095 | 0,054 | non défini | non défini |
  | KH, g = 0,20, k = 5, T = 60 | 1,000 | 0,099 | **0,099** | non défini | non défini |
  | MH, g = 0,20, k = 3, T = 45 | 0,651 | 0,090 | 0,032 | 0,036 | 0,020 |
  | MH, g = 0,20, k = 5, T = 60 | 0,939 | 0,110 | **0,093** | 0,036 | 0,029 |

  Avec la lecture (ii), le premier mécanisme (S et D₀ partagés) ne fait plus passer le seuil dans les cases jouées. Le
  plus haut est 0,056 ± 0,005, dans E30 à g = 0,10, sous 0,0597. Seul le second mécanisme (compression propre à chaque
  juge, variante « insertion » de G4) le passe encore. Dans la variante « contenu », MH reste sous le seuil et KH n'est
  pas défini. **Sous (ii), la conclusion dépend donc de G4**, contrairement à ce qu'écrit le rapport.
- **Correction demandée** : au rapport, réécrire la ligne C-P3c de la section 1 et la phrase de la section 6.2 en
  conditionnel (« sous la lecture (i) de A6 ») et ajouter la lecture (ii) pour C-P3c, avec un rééchantillonnage, sur
  les cases KH et MH et sur E30 à g = 0,10 à R ≥ 8 000. Au texte : trancher A6 (voir CG-03).

### CG-03 — majeure — A6 doit être levée dans le texte avant le scellement

- **Lieu** : texte, point 11, liste d'arrêt 17, « Critères de lecture gelés » ; rapport, A6.
- **Constat** : l'ambiguïté est réelle. Le texte ne dit pas si une statistique de rang dont une composante Ḡ a plus de
  1 % de tirages dégénérés est encore lue. L'enjeu dépasse la clause. Sous (ii), C-P3a n'est jamais lisible sans attaque.
  Sa puissance s'effondre aussi : sur l'artefact « effet vrai 0,04 / 0,10 / 0,16 », « établie » tombe de 0,945 à 0,0075
  (sortie `ab_P6_g10_k5_T60_p0.json`, rejouée à l'identique). Sous (i), on lit un rang entre juges dont la loi n'a pas
  de destination identifiable, ce que le texte interdit ailleurs (ĉ « non identifiable »).
- **Correction demandée** : le texte dit expressément si la règle des 1 % porte sur ĉ et λ seuls (alors Ḡ reste lu, et
  la lecture est (i)) ou aussi sur les statistiques de rang qui emploient Ḡ (lecture (ii)). Il cite ensuite la ligne
  correspondante du rapport.

### CG-04 — majeure — formulation trop large de la conclusion de C-P3c

- **Lieu** : rapport, section 1, tableau : « **oui**, sous tout modèle où les deux gains d'écart suivent leur définition
  du texte ».
- **Constat** : la preuve couvre les modèles joués, sous la lecture (i). « Tout modèle » est faux en général. Un effet
  propre au couple juge × tâche (un juge lit de travers toute la tâche t, S comme SP), exclu par G5, s'annulerait en
  partie dans SP_t − S_t et affaiblirait le premier mécanisme. Le jugement « un trop beau résultat est une réserve »
  vaut aussi pour un résultat qui dit que la clause joue.
- **Correction demandée** : « oui, dans les cases jouées, sous la lecture (i) de A6 et les hypothèses G1, G2 et G5 ; le
  premier mécanisme ne dépend ni de G3, ni de G4, ni de k_P, ni du gain du plaidoyer ; sous la lecture (ii), seulement
  par le second mécanisme, qui dépend de G4 ». Déclarer G5 comme l'hypothèse dont la négation (effet juge × tâche)
  atténue le premier mécanisme.

### CG-05 — mineure — le rejeu des deux cases de C-P3b : règle écrite d'avance, mais inutile à la lettre

- **Lieu** : rapport, section 6.1, passe 1 ; `grille_ab_v1.py`, l. 16 à 18 (la règle) ; texte, l. 580 à 583.
- **Constat** : la règle est bien écrite avant tout résultat. `grille_ab_v1.py`, qui la porte, a la même empreinte dans
  le manifeste d'avant lancement (12:49:24 UTC) qu'à la fin, et ce manifeste précède la fin des deux passes. Le texte
  ne donne aucun droit au rejeu (A8), mais il n'en fallait pas : **à la lettre, 0,053 et 0,051 sont sous 0,0638, donc
  la clause ne joue pas dès la passe 0.** Le critère « net » (taux + 2 erreurs sous le seuil) vient du rapport, pas du
  texte. Le rejeu ne pouvait qu'ajouter une chance de déclencher la clause (seuil plus serré à 0,0569), donc il
  n'avantage pas la conclusion obtenue. La trace est un fichier non scellé du bloc-notes : il faut le sceller avec le
  rapport.
- **Correction demandée** : écrire que la lecture à la lettre se fait sur la passe 0 (aucun dépassement) et que la
  passe 1 est une information. Sceller le manifeste d'avant lancement.

### CG-06 — mineure — le nombre d'essais choisi déplace le seuil

- **Lieu** : texte, l. 581 et 582 (« R essais de la case, au moins 1 000 ») ; rapport, C-P3c à R = 8 000 (seuil 0,0549).
- **Constat** : à R = 8 000, des taux de 0,052 à 0,060 (E30, E40, E60 et M616 à g = 0,10) comptent comme « au-dessus ».
  À R = 1 000, ils ne compteraient pas. Rien ne change sous la lecture (i), car les cases sans attaque sont à 0,076 au
  moins. Sous la lecture (ii), ce sont ces cases-là qui décident. Le texte ne dit pas non plus si un dépassement peut
  être levé par un rejeu, ni comment traiter des dizaines de cases (A8 : environ 2 % de dépassements par case à un niveau
  vrai de 0,05).
- **Correction demandée** (texte) : fixer R par ligne, ou un R minimal et la règle d'un rejeu, avant de jouer.

### CG-07 — mineure — T = 30 tâches est permis par le plan, mais absent de la grille

- **Lieu** : texte, l. 1088 à 1094 et 1211 (n ∈ {60, 90, 120}, donc 30 à 60 tâches) ; clause, l. 583 (« 45 et 60
  tâches »).
- **Correction demandée** (texte) : ajouter T = 30 à la grille, ou écrire que la clause ne couvre pas n = 60.

### CG-08 — mineure — l'appariement des témoins vient des longueurs de la configuration brouillon 3

- **Lieu** : rapport, A10 ; texte, verrou 4, règle des témoins (l. 1074 à 1076).
- **Constat** : la mise en commun de témoins entre familles (celui de l'indice 1 entre les familles 1 et 4, qui porte le
  bras « bruit » jusqu'à 0,054) dépend des longueurs. Une configuration scellée différente pourrait changer les taux.
  Le second point de A10 (les longueurs du corpus A servent aux deux corpus) n'est pas une ambiguïté : la l. 1075
  apparie sur « la formulation remplie pour le corpus A ».
- **Correction demandée** : citer, à la clause, la configuration dont viennent les longueurs, et rejouer si les
  longueurs scellées diffèrent.

### CG-09 — mineure — le libellé « erreur sur v₀ seule » ne décrit pas le modèle joué

- **Lieu** : rapport, section 4, tableau (E30 : « erreur sur v₀ seule, borne basse ») ; `grille_commun_v1.py`, l. 60
  (`S = lambda s: (s, s, 0.0)`).
- **Constat** : le modèle « erreur seule » porte la même erreur sur v₀ et sur toute insertion (s₀ = σ). C'est le modèle
  de l'archive et de la réserve 15 (« si v₀ porte la même erreur d'insertion que les témoins »), donc il est fidèle au
  texte. Le libellé suggère pourtant σ = 0.
- **Correction demandée** : libellé « erreur d'insertion, la même sur v₀ et sur les insertions (s₀ = σ) ».

### CG-10 — mineure — la marge de C-P3b est faible là où la compression joue seule sans attaque

- **Lieu** : rapport, section 6.1 (K16 et KH sans attaque : jusqu'à 0,053) ; A3 (σ non fixé sous la compression).
- **Constat** : j'ai joué quatre cases neuves (sans attaque, k = 3, T = 45, R = 1 000, B = 1 000). Pour C-P3b :
  compression 0,16 avec σ = 0,2, 0,048 ; avec σ = 0,6, 0,041 ; compression homogène 0,10, 0,053 ; compression 0,04 /
  0,10 / 0,16 avec σ = 0,6, 0,044. Pour C-P3a : 0,036 à 0,043. Tout est sous 0,0638. Mais C-P3b est au niveau
  nominal (environ 0,05) dans cette région. Une recherche de cases sans fin finirait par passer le seuil par hasard,
  avec une probabilité d'environ 2 % par case.
- **Correction demandée** : fermer la grille par une liste finie (CG-01) ; rapporter ces quatre cases comme hors liste.

### CG-11 — mineure — dépassement du budget de calcul

- **Lieu** : rapport, section 9 (4,3 heures de processeur pour une borne d'environ une heure).
- **Constat** : il est déclaré ; il n'a aucun effet sur la méthode. Je le signale pour la mère et le registre.

### CG-12 — mineure — la paraphrase du mandat et le texte r1 diffèrent sur le cas « sans rapport complet »

- **Lieu** : mandat (« sans rapport complet, toutes sont rapportées sans verdict ») ; texte r1 (« la version (b)
  s'applique » : C-P3a et C-P3b sans verdict, C-P3c garde son verdict à deux lectures sous la clause).
- **Constat** : l'issue est la même en pratique. À deux lectures, C-P3c dépasse le seuil (bras principal jusqu'à 0,337),
  donc la clause la met sans verdict elle aussi. Les mots, eux, diffèrent.
- **Correction demandée** : aligner la ligne du registre sur le texte r1, ou l'inverse.

### CG-13 — mineure — l'écart 0,186 / 0,227 avec le rejeu du rédacteur

- **Lieu** : rapport, section 7, dernier paragraphe.
- **Constat** : les programmes du rédacteur (`commun_cb6_v1.py`, `u1_…`, `u3_…`) ont le même modèle que la grille :
  même juge N5 = MH, même profil, mêmes corpus, même appariement (configuration brouillon 3), même C-P3b. J'ai rejoué
  la case sur une graine neuve (passe 2) : lecture calibrée seule, C-P3b 0,196 (C-P3a 0,323). Les deux estimations de
  la grille (0,186 et 0,196) s'accordent. L'écart avec 0,227 fait environ 2,3 erreurs : c'est du hasard plausible
  parmi plusieurs comparaisons, sans indice de différence de code. Cette lecture n'entre dans aucun verdict.
- **Correction demandée** : citer ce rejeu à la place de « je ne l'ai pas rejoué ».

### CG-14 — mineure — pour le rédacteur : C-P3c n'a pas la garde que C-P3a a reçue

- **Lieu** : texte, l. 565 (C-P3a : p exact **et** p centré, à cause des témoins partagés) et l. 567 (C-P3c : p exact
  seul).
- **Constat** : trois liens entre évaluateurs de C-P3c découlent du texte : S et D₀ partagés, compression dans les gains
  bruts, témoin partagé entre les familles 1 et 4. Un p centré par tirage des tâches couvrirait les liens aléatoires (le
  premier et le troisième), mais pas le biais fixe du second. Je ne le recommande pas à la place de la clause, qui joue
  telle qu'écrite. Je le note pour une version future, sur nœud.

## 4. Fidélité du code au texte (point 1 du mandat)

Aucun écart trouvé. En détail :

- C-P3a : W sur les rangs de Ḡ (5 familles × 3 juges). p exact sur la loi des 7 776 affectations, avec un W critique
  de 0,64 et p = 0,0394 retrouvés. p centré = (1 + #{W* ≥ W}) / (B + 1), W* sur les rangs de Ḡ* − Ḡ
  (`grille_commun_v1.py`, l. 219 à 225). Conforme à la l. 565.
- C-P3b : les écarts intra-famille retirent la moyenne des trois juges de chaque famille (axe des juges, l. 228 et 229).
  Le τ observé et les τ* rééchantillonnés sont mis à plat dans le même ordre. p = (1 + #{τ* ≥ τ}) / (B + 1). Les tirages
  sont indépendants entre corpus (deux appels à `comptes`) et les mêmes pour les trois juges et les cinq familles
  (l. 182). Conforme à la l. 566.
- C-P3c : quatre évaluateurs (gains d'écart sous le plaidoyer et sous l'usurpation, Ḡ des familles d'indices 0 et 3,
  soit « flatterie et supplication » et « usurpation stylistique »). p exact sur 1 296 affectations, avec W critique
  0,8125 et p = 0,0417, retrouvés par un calcul indépendant. Conforme à la l. 567. Le sens « g > 0 vers la cible » est le
  même pour les quatre évaluateurs, ce qui est la condition pour comparer les rangs.
- Trois lectures : calibrée, ρ = 1, et ρ̂/r̂. ρ̂ est borné à [0,05 ; 1] avant la division, puis ρ̂/r̂ est borné à son
  tour. r̂ est le rapport « covariances entre témoins distincts / covariances entre v₀ et un témoin », sur tous les
  témoins retenus, recalculé dans chaque tirage (l. 148 à 170 et 207). « Établie » est la conjonction des trois
  lectures. Les gains d'écart sont les mêmes dans les trois lectures : c'est conforme, car les trois lectures ne portent
  que sur les composantes en Ḡ (l. 569).
- Seuil : 0,05 + 2 √(0,0475 / R), soit 0,0638 à R = 1 000 et 0,0549 à R = 8 000. Conforme.
- Gain d'écart (`gains_ecart`, l. 280 à 301) : D₀ = moyenne (S − H) ; g_m = −moyenne (SP_m − S) / D₀ ; Ḡ_P est la
  moyenne des g_m ; g_U se calcule de même. Conforme au point 13 (l. 773 à 775).
- Graines : `SeedSequence(20261119, spawn_key = (programme, case, passe))`. Les identifiants de case sont injectifs dans
  le plan joué, et les programmes 1 et 2 sont distincts. Conforme à R9.

## 5. Le modèle des gains d'écart (point 2 du mandat)

- **G1** (H et S de TC.2 et TC.3 b = contenus du corpus A de TC.1) : c'est la lecture du texte. Les l. 1111 et 1112
  donnent 2 × (2 + k_P) épisodes par tâche, avec un seul H et un seul S ; la l. 1135 dit « Corpus A : contenus H et S » ;
  les effectifs de la l. 1211 sont (n/2) × 2 × (2 + k_P). Le partage de S et de D₀ entre les deux gains d'écart vient de
  la définition du point 13 et de ce plan : **ce n'est pas une lecture du rapport.** Le premier mécanisme n'exige même
  pas que TC.1 et TC.2 partagent leurs contenus, seulement que les deux gains d'écart d'un juge partagent sa lecture de S.
- **G2** (épisodes neufs, vérité commune aux juges) : défendable, car l'agent régénère l'épisode sous chaque bras.
- **G3 et G4** : choix du rapport, déclarés. Le premier mécanisme n'en dépend pas. Je l'ai vérifié avec un programme
  indépendant (`rejeu/meca1_independant_v1.py`) qui remplace les deux Ḡ nets par des rangs tirés au hasard, R = 20 000,
  niveau exact 0,0417 :

  | cas | taux |
  |---|---|
  | S partagé, erreur 0,3, T = 45 | 0,075 ± 0,002 |
  | S relu à part | 0,043 ± 0,001 |
  | S partagé, SP et SU lus sans erreur | 0,137 ± 0,002 |
  | S partagé, erreur 0,6, T = 60 | 0,076 ± 0,002 |
  | S relu à part | 0,041 ± 0,001 |

- **Le second mécanisme** (compression propre à chaque juge, présente dans les gains bruts) n'est pas un artefact
  arbitraire. Le texte lui-même pose qu'une insertion comprime la lecture (réserve 15 ; l. 747 et 748), et le juge lit
  « le contenu complet, paragraphe compris » (l. 779). La variante « insertion » est donc l'extension la plus cohérente
  du modèle de la grille. Elle reste une hypothèse : le texte n'en décide pas (A5).
- **G5** : voir CG-04. Un effet juge × tâche affaiblirait le premier mécanisme. Il n'est pas dans la grille du texte.
- **Conclusion** : sous la lecture (i), la conclusion tient et ne dépend que de G1, G2 et G5, qui sont du texte ou
  neutres. Sous la lecture (ii), elle dépend de G4 (CG-02).

## 6. Mes rejeux (point 5 du mandat)

Programmes : copies conformes sous `contre-lecteur-grille/rejeu/programmes/` et `rejeu/archive/` ; programmes propres
`cp3c_lecture_ii_v1.py`, `ab_cases_neuves_v1.py`, `meca1_independant_v1.py` et lanceur. Empreintes figées avant le
lancement : `rejeu/sha256sums-programmes-contre-lecteur-avant-lancement.txt`
(`69475c06b2421d5a1f326232df13aab4d0ed12a9306da218ac7b18db7593bdf4`). Sorties :
`rejeu/sha256sums-sorties-contre-lecteur-v1.txt` (`d9ff193bb35b7082f198edd1e6bdb50fb35606352653d1b82b5dd0885731a0e4`).
Lot lancé de 14:07:34 à 14:12:45 UTC sur quatre cœurs, puis une case de 105 s : environ 23 minutes de processeur.
Python 3.13.18, numpy 2.5.3.

Rejeux à l'identique (même programme, même graine ; sortie JSON égale champ par champ, durée exceptée) :

| case | ligne | rôle | résultat |
|---|---|---|---|
| K16, g = 0, k = 3, T = 45, R = 1 000 | C-P3a et C-P3b | la plus proche du seuil (C-P3b 0,053) | identique |
| MH, g = 0,20, k = 5, T = 60 | C-P3a et C-P3b | artefact à deux lectures (0,153 et 0,131) ; lecture calibrée seule 0,186 | identique |
| P6, effet vrai, R = 400 | C-P3a et C-P3b | contrôle sur artefact (0,945 et 0,970) | identique |
| E30, g = 0, k = 3, T = 45, R = 8 000 | C-P3c | au-dessus du seuil (bras principal 0,083) | identique |
| K16, g = 0, k = 3, T = 45, R = 8 000 | C-P3c | sous le seuil (bras principal 0,041) | identique |

Mesures neuves : C-P3c sous les lectures (i) et (ii) (CG-02) ; quatre cases de compression hors du plan du rapport
(CG-10) ; MH sur graine neuve (CG-13) ; mécanisme 1 indépendant (section 5). J'ai aussi recompté, à partir des 100
sorties de C-P3c, les étendues et les cases au-dessus du seuil de la section 6.2 : 54, 45, 55, 32, 26, 35 et 24, égales
au rapport. Aucun ex æquo dans aucun bras défini. Les erreurs de Monte-Carlo sont bien calculées. Les comparaisons au
seuil de C-P3c sans attaque sont nettes, à plus de cinq erreurs.

## 7. Symétrie (point 6 du mandat)

Rien n'indique une simulation bâtie pour obtenir une conclusion. Les programmes ont été figés avant le lancement. La
règle du rejeu ne pouvait que favoriser un déclenchement. Des contrôles montrent que l'instrument voit un taux haut
(artefacts 1 à 5) et un taux bas (artefact 6). Le rapport dit lui-même que sa conclusion pour C-P3c dépend d'un modèle
qu'il a choisi. Deux réserves : le résultat « C-P3a et C-P3b propres » a été audité par des artefacts, mais le résultat
« C-P3c joue » n'a pas été soumis à l'ambiguïté A6, que le rapport a pourtant mesurée pour C-P3a et C-P3b (CG-02) ; et
la formulation « sous tout modèle » dépasse la preuve (CG-04). L'écart 0,186 / 0,227 n'appelle rien de plus que CG-13.

## 8. Ambiguïtés du texte (point 7 du mandat)

| ambiguïté | réelle ? | à lever avant le scellement ? |
|---|---|---|
| A1, grille en plages | oui | **oui**, liste finie (CG-01) |
| A2, « aucune attaque » croisée avec tous les modèles | faible : la lecture naturelle croise | non, si la liste finie la règle |
| A3, σ sous la compression | oui | oui, dans la liste finie |
| A4, profil par famille et gain sur le corpus B | oui, sans effet visible | à écrire dans la liste |
| A5, modèle des gains d'écart | oui | oui : le texte adopte le modèle du rapport, ou dit que la clause porte sur lui |
| A6, tirages dégénérés | **oui, décisive pour C-P3c** | **oui** (CG-02, CG-03) |
| A7, ex æquo | faible : verdicts continus (point 1), aucun rencontré | une phrase suffit |
| A8, droit au rejeu et cases multiples | oui | oui (CG-06) |
| A9, 1 000 ou 10 000 tirages | non : la clause dit « au moins 1 000 » | non |
| A10, longueurs des témoins | oui pour la configuration ; non pour le corpus B (l. 1075) | oui (CG-08) |
| T = 30 absent de la grille (relevé ici) | oui | oui (CG-07) |

## 9. Avis par ligne

| ligne | avis | pour trancher |
|---|---|---|
| C-P3a | **tient** sur les cases jouées : 0,003 à 0,049, aucune près de 0,0638 ; mes cases neuves 0,036 à 0,043 | liste finie de la grille (CG-01), avec E40 à g = 0,20 joué |
| C-P3b | **tient** sur les cases jouées et sur mes quatre cases neuves (0,041 à 0,053), à la lettre dès la passe 0 ; marge faible sous la compression seule, sans attaque | liste finie (CG-01) ; lecture à la lettre de la passe 0 (CG-05) |
| C-P3c | **tient sous la lecture (i)** de A6 : premier mécanisme, issu du texte, retrouvé indépendamment, indépendant de G3, G4 et k_P. **Indéterminée sous la lecture (ii)** : elle ne tient alors que si G4 vaut « insertion » | le texte tranche A6 (CG-03). Si (ii) : décider G4, ou jouer la lecture (ii) avec rééchantillonnage sur toute la liste finie, à R ≥ 8 000, et appliquer la clause à ce qui en sort |
