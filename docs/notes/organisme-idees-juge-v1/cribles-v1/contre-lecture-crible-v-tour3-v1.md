# Contre-lecture du préenregistrement du crible (v), brouillon 3 — tour 3 — v1

- Contre-lecteur : sous-agent neuf, **modèle C** (identité dite en conversation seulement) ; auteur du brouillon 1 : modèle A ; corrections du brouillon 3 appliquées par un rédacteur du modèle C (la pièce le dit) ; je n'ai écrit aucune pièce citée. Le premier lecteur (modèle B) n'a rendu aucun rapport : je n'ai lu ni ses dossiers ni rien de lui.
- Date (UTC) : lecture de 14:01:47Z à 14:08Z (`date -u`) ; lecture entière de la pièce.
- Pièce relue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-v-brouillon3.md`, empreinte entière `8a21f085d0caff7d2ec392e326b30c03616d67f066460eed54bae5aed5aeca6a` (vérifiée par `sha256sum`, égale à son compagnon). Brouillon 2 : `05ce58137d0700c493f76d34caf8605fe604942ff868350801baaeaf70948593` (égale à son compagnon et à celle que cite la pièce). Rapport du tour 2 : `c04b8feede2540dbf85f7dd22741b3cfcb157d6a5ebc7a9c99dd8239611cf556` (égale). Programme d'application `appliquer-corrections-crible-v-brouillon3.py` : `b6283e507de731079bdec022cd36f74e83662900cc3c00dae7e2501e1e5f89b2` (égale à son compagnon ; lu en tête, non exécuté).
- Pièces lues : la pièce en entier ; le rapport du tour 2 en entier ; le différentiel `diff` brouillon 2 / brouillon 3 en entier ; la ligne R-2977 de `registres/decisions.md`, et par `grep` les lignes R-2981 à R-2985 (début de ligne seulement, voir « Incidents ») ; la ligne GO-2026-11-15-06 de `registres/go.md` (par `grep`) ; empreintes seules de la note des idées originales, du relevé, des décisions N-044, N-045, N-053, N-058, N-067, du gabarit, de `prereg.py`, des deux modèles de forme, du catalogue, de la question, des faits du collisionneur, du verdict v67 ; après `git fetch` des deux branches par refspec, le texte scellé du pilote (empreinte et lignes de plafonds du bloc gelé) et la procédure v14 (empreinte). **Non lu** : tout ce que la consigne interdit (rien sous `diag/`, `runs/`, `donnees/` ; relevé de v67 non ouvert ; sortie du pilote non ouverte ; 7a, 7b, T0.6, T0.7, P3-bis, bras d'attaque). Aucun appel de modèle, aucune dépense, aucune machine, aucun `pytest`.

## Verdict

**corrections.** Les 23 couples du tour 2 sont appliqués fidèlement et le différentiel ne contient rien d'autre que les sept couples propres que la pièce déclare ; le validateur ne rend aucun défaut. Mais les corrections appliquées laissent **deux défauts majeurs** (C3-1 : les dollars sont définis de trois façons incompatibles depuis la nouvelle définition du monde complet ; C3-2 : le rejeu sous archive fictive, « exécuté après la sortie principale », contredit la sortie unique scellée et n'a pas de ligne d'arrêt) et **sept séries de défauts mineurs** (C3-3 à C3-9). Pas de « a_refaire » : la conception tient, tout se corrige par les couples ci-dessous. **2 majeures, 7 mineures** (la majeure C3-1 porte deux couples, C3-2 deux ; la mineure C3-8 sept).

## Vérification de l'application des corrections du tour 2

1. **23 couples du rapport.** Lus par programme (bibliothèque standard, `python3 -I`, lecture seule) dans le rapport du tour 2 : 23 blocs `T2-…`. Résultat : chaque « ANCIEN » figure **une fois** dans le brouillon 2 ; chaque « NOUVEAU » figure **une fois** dans le brouillon 3. **Appliqués fidèlement, sans retouche** : T2-01a à T2-13.
2. **Différentiel.** `diff` des deux brouillons, puis reconstruction : le brouillon 2 auquel j'applique moi-même les 23 couples, comparé au brouillon 3, ne diffère que par sept hunks : titre, ligne « Brouillon 3 » de l'en-tête, statut, validateur, tête de la section « Contre-lecture », liste « À trancher en priorité » dite périmée, entrée « Contre-lecture 2 » ; ce sont les sept couples propres que l'entrée « Contre-lecture 2 » nomme. **Rien d'autre.** Aucun ne touche un critère, un seuil, une graine ni une ligne d'arrêt.
3. **Entrée « Contre-lecture 2 »** : heures (13:49:05Z à 13:57:37Z), comptes (4 majeures, 9 mineures, 5 remarques), empreintes du rapport et du brouillon 2, nom du programme : **exacts**. La pièce déclare l'écart de rôle à R-2982 (corrections écrites par le modèle C) ; il se retrouve.
4. **Validateur** : `controle_ia.prereg.problemes` rejoué sur le brouillon 3 (`.venv/bin/python -I`, fonction seule) : **liste vide**. Aucun identifiant de modèle hors les deux clés de configuration que la pièce dit.
5. **Empreintes citées** : celles que j'ai recalculées (brouillon 1, rapport du tour 1, note, relevé, N-044, N-045, N-053, N-058, N-067, gabarit, `prereg.py`, les deux modèles de forme, catalogue, question, faits du collisionneur, verdict v67, `go.md` à `377a2a0c`, texte scellé du pilote, procédure v14, brouillon 2, rapport du tour 2) sont **égales** à celles de la pièce ; le diff n'a ajouté que celles du rapport du tour 2 et du brouillon 2, égales. Non recalculées : celles de l'annexe A, du relevé de v67 (non ouvert), de la configuration v12 et du gabarit du pilote (déjà dites par le tour 2).
6. **Plafonds de session** relus dans le bloc gelé du pilote : 3 ; 2 ; 2,34 ; 2,34 USD (clés dans l'ordre fable, opus, argon, astra) ; parts 12 ; 8 ; 9,36 ; 9,36 ; machine 3,00. Le devis du brouillon 3 est inchangé par rapport au brouillon 2.

## Réponses aux neuf points

**(1) R1.** Hypothèse, prédictions V1 à V7 (zones de confirmation, de réfutation et d'indécision désormais complètes pour les sept, T2-8), métrique, seuils, plan d'analyse, critères gelés, liste d'arrêt : présents. La « porte de sortie » du monde complet est fermée (définition gelée, minimum 0,8 × N gelé, seule la probabilité de l'atteindre recalculée à titre d'information). **Portes restantes** : (a) B_a, M et la règle de dépassement de la réflexion de Pr-1 sont des blancs à remplir « d'après le pilote » sans règle écrite pour B_a, alors que N dépend de B_a (C3-7) ; (b) étape 2 et « points à remesurer » ne disent pas la même chose sur ce que le lecteur du pilote peut rendre pour V1 et V6 (C3-6) ; (c) les dollars (C3-1).

**(2) R3.** *0,25 et 0,05* : étiquetés « choix de ce texte, de portée pratique, non déduit d'une donnée » ; justification absente mais avouée : acceptable (pas de voie vers un signe positif : les deux seuils jouent contre H-v autant que pour elle). *Puissance* : binomiale exacte refaite par moi, 20 mondes (W ≥ 4) : 0,133 ; 0,352 ; 0,589 ; 0,804 ; 0,956 à p = 0,10 ; 0,15 ; 0,20 ; 0,26 ; 0,35 ; sur 17 mondes à risque : 0,244 ; 0,681 ; 0,897 à p = 0,15 ; 0,26 ; 0,35 ; **les chiffres de la pièce (0,13 ; 0,59 ; 0,80 ; 0,24 ; 0,68 ; 0,90) sont exacts**. À 24 mondes (W ≥ 5) : 0,287 ; 0,787 à 0,15 et 0,26 (24 à risque), 0,197 ; 0,671 (21 à risque) : **aucun gain**, que la pièce ne dit toujours pas (C3-5). *Table W_min(n_c)* refaite (bornes basses de Clopper-Pearson par bissection, 100 itérations) : 4 de 16 à 22 (0,0727 ; 0,0681 ; 0,0641 ; 0,0605 ; 0,0573 ; 0,0545 ; 0,0519) ; 5 à 23 et 24 (0,0746 ; 0,0713) ; avec 4 : 0,0495 à 23, 0,0474 à 24 : **exacte**. *Cas dégénéré* : l'issue « non éprouvée au crible » est définie et gelée (k_R < 4 ou k_R > n_c − 4), elle prime sur l'étage 3 ; le bras à archive enrichie est refusé par R-2977 : **tenu**. *Distance dans un seul sens* : écart déclaré, sensibilité du minimum des deux sens : **tenu**. *Épargne et k_R* : S_R ≥ 0,25 ⇔ k_R ≤ 12 à 0,71 (S = 0,2485 à 13) et ≤ 13 à 0,75 (S = 0,2625 à 13, 0,225 à 14) : **la correction T2-6 est exacte** ; à 24 mondes : k_R ≤ 15 à 0,71 (0,2662 à 15, 0,2367 à 16), k_R ≤ 16 à 0,75 (S = 0,25 exactement à 16) : non écrit (C3-5).

**(3) Devis.** Recompte : 20 appels par proposeur, 80 en tout ; plafonds 2,34 ; 2,00 ; 2,34 ; 3,00 ; pires 46,80 ; 40,00 ; 46,80 ; 60,00 ; machine 3,00 ; crédits 100,00 ; hors crédits 96,60 ; total 196,60 ; écart à la note 13,60 : **exacts**. À 24 mondes : 96 appels ; 9,68 × 24 + 3 = **235,32** ; crédits 120,00 ; hors crédits 56,16 + 56,16 + 3,00 = 115,32 : la pièce écrit « à l'avenant, + 20 % » et ne chiffre pas, alors que la ligne de GO, le résumé « En dix lignes » et la liste d'arrêt restent à 20 (C3-8). Part sur crédits : 100/196,60 = 0,509 ; 120/235,32 = 0,510 ; 39,60/79,95 = 0,495 à 49,20/92,75 = 0,530 : **exacts**. Les deux comptes des dollars (prix public principal ; prix de la configuration en sensibilité ; prix de Pr-1 doublé le 1er décembre, troisième compte rapporté) sont dits. Cohérence avec GO-2026-11-15-06 : type « calcul », parts séparées, mots de Lazar cités, échéance 30 novembre, « devis refait et contre-lu » : **conformes** ; l'enveloppe d'ensemble des cinq cribles : point pour la mère 5. **Les dollars du crible** (ce qui compte dans S_R) : voir C3-1, défaut majeur.

**(4) Durée.** **Réponse nette : le code du pilote ne suffit pas ; il faut une configuration et un code neufs** (lanceur pour N mondes et 4 N appels avec borne par appel et concurrence éventuelle, programme de mesure, programme de lecture, programme de la partie A, procédure de machine neuve, essais R5, banc de mutations, contre-lecture du code, addendum d'empreintes, deux lignes de GO) ; **la date de lancement dépend de ce code, non de ce préenregistrement** (la pièce le dit maintenant, T2-11). Bornes : 4 appels d'un monde en parallèle, donc par monde au plus B_a ; sans parallélisme entre mondes, N × B_a : 10 h à N = 20 et B_a = 1 800 s, 12 h à N = 24 ; avec 2 h 40 de barrières, ≈ 1 h de génération, 0,5 à 1 h de mesure : ≈ 14,2 à 14,7 h à 20 mondes (tient sous 17 h), ≈ 16,2 à 16,7 h à 24 (frôle ; M ≥ 2 ou B_a plus court, la pièce le dit). La table de durée de pire cas n'est pas écrite (promise au texte qui fera foi) : acceptable pour un brouillon. Défaut restant : B_a, M sans règle (C3-7).

**(5) Liste d'arrêt, graines.** Lignes neuves : minuterie (N = 20 ou 24), « appel plus long que B_a » (essai sain et artefact présents), partie A (liste des retenues permise : cas sain « lecture des seules lois, liste des retenues comprise », artefacts « champ `promue` » et « champ de rejet ou de mort ») : **conformes**. **Ligne manquante** : le rejeu sous archive fictive (C3-2). Graines : `numpy.random.SeedSequence`, racine = empreinte du texte qui fera foi ; clés `(r, 30)` avec r de 1 à N, `(67, g, 30)`, `(99, b)`, `(97, k)`, `(98, w)` : sans collision ; R9 conforme. Essai sain « 20 mondes conformes » : C3-8.

**(6) N-058.** Le crible est borné à la génération 1, archive {K1}, aucun verdict dans l'archive ; la dépendance indirecte au-delà est dite aux « Écarts » et au « Choix » 11, « à dire à Lazar avec le nœud d'adoption » (R-2977) ; le critère se juge sur l'oracle et le coût. La partie A lit la liste des retenues (un résultat du juge) : dit, borné « sans rien décider », ligne d'arrêt mise d'accord (T2-4). **Aucune violation de N-058.** Une réserve de fond pour la mère : la sensibilité à archive fictive lit des composantes de l'oracle pour bâtir l'archive ; elle est rapportée sans verdict et jamais lue par la règle de production : tenable seulement si C3-2 est appliquée.

**(7) Partie A.** Déclarée descriptive, « sur des données déjà vues (R-2977) », sans critère, sans verdict du juge, sortie scellée avant lecture, seuils non changés ; la lecture de la liste des retenues est dite comme seule exception. Je n'ai pas ouvert le relevé. Rien à corriger.

**(8) R7 et R8.** Aucun chiffre de l'état de l'art ; antériorités listées « à chercher », références « à vérifier », zone « séduisante » à vérifier plus durement ; citations obligatoires de N-064 et N-067 présentes. Rien à corriger.

**(9) Validateur, identifiants, empreintes.** Voir « Vérification », points 4 et 5.

## Corrections exigées

Chaque « ancien » est une chaîne d'une seule ligne de la pièce, présente **une seule fois** (vérifié par programme à la fin) ; les couples ne se recoupent pas ; les « nouveau » sont des propositions à écrire par l'auteur (modèle A) ; les chiffres que j'ai recomptés sont à refaire par programme et à recopier en annexe. Quand un « nouveau » contient « \n », c'est une ligne de table de plus.

### Majeures

**C3-1 — Les dollars, définis de trois façons.** Depuis la définition neuve du monde complet (T2-01a), la section « Métrique » dit trois choses incompatibles : (i) « couvertures, règle **et dollars** se calculent sur les appels répondus du monde » ; (ii) « les cartes … d'appels tronqués **comptent dans les dollars** » (un appel tronqué n'est pas répondu) ; (iii) « $_b(w), $_e(w) : dollars **des deux appels** de chaque moitié » (un monde complet peut n'avoir qu'un appel répondu par moitié). S_R, la mesure de l'étage 3 (a), en dépend : excluer les appels tronqués ou en échec (facturés) sous-compte la dépense, et d'autant plus que la moitié chère est tronquée (plafonds de session atteints). Le choix correct est celui du bras de référence : tous les appels lancés, payés. Même correction : dire le biais commun que le tour 2 demandait de dire (un appel absent abaisse la couverture de sa moitié, dans les deux sens).

`C3-01a`
```
ANCIEN: (définition gelée dès ce texte, écrite avant la lecture du pilote ; couvertures, règle et dollars se calculent sur les appels répondus du monde, les mêmes pour tous les bras)
NOUVEAU: (définition gelée dès ce texte, écrite avant la lecture du pilote ; couvertures et règle se calculent sur les appels répondus du monde, les mêmes pour tous les bras ; un appel absent abaisse la couverture de sa moitié, biais commun dans les deux sens (appel bon marché absent : ℓ_w gonflé ; appel cher absent : ℓ_w réduit), rapporté par la sensibilité « mondes à quatre appels seulement » ; les dollars se calculent sur les quatre appels lancés du monde, répondus ou non, tronqués et en échec facturés compris, tels que les journaux des relais les donnent)
```

`C3-01b`
```
ANCIEN: $_b(w), $_e(w) : dollars des deux appels de chaque moitié.
NOUVEAU: $_b(w), $_e(w) : dollars des appels de chaque moitié du monde (deux appels par moitié, répondus ou non, comme ci-dessus).
```

**C3-2 — Rejeu sous archive fictive : « exécuté après la sortie principale » contredit la sortie unique, et rien ne garde cet ordre.** La correction T2-03a fait de la sensibilité une fonction distincte « exécutée seulement après l'écriture de la sortie principale ». Or : la mesure « calcule, dans cet ordre … (4) … les sensibilités » et écrit **une** sortie scellée ; la liste d'arrêt arrête « une seule sortie scellée / seconde mesure : refus du lanceur ». Où s'écrit le résultat de la sensibilité, et comment ne pas la confondre avec une seconde mesure ? Et l'ordre, ainsi que « ne rend que k_R et S_R », est une garde neuve : R5 veut sa ligne, avec son essai sain et son artefact. La sensibilité lit des composantes de l'oracle : sans cette ligne, rien n'empêche qu'elle serve avant la sortie principale (N-058).

`C3-02a`
```
ANCIEN: sensibilités. Sortie scellée avant toute lecture, sans devis de monde ni loi plantée ;
NOUVEAU: sensibilités **sauf** le rejeu sous archive fictive (section « Métrique », « Sensibilités »), exécuté en dernier (5) par sa fonction distincte, après l'écriture et le scellement de la sortie principale, dans le même lancement, vers un second fichier scellé (ce n'est pas une seconde mesure). Sortie scellée avant toute lecture, sans devis de monde ni loi plantée ;
```

`C3-02b`
```
ANCIEN: | la fonction de décision reçoit autre chose que les lois de la moitié bon marché, K1 servie et le jeu public | arrêt ; défaut | signature conforme | un objet oracle, une issue ou une carte de la moitié chère passés : refus nommé |
NOUVEAU: | la fonction de décision reçoit autre chose que les lois de la moitié bon marché, K1 servie et le jeu public | arrêt ; défaut | signature conforme | un objet oracle, une issue ou une carte de la moitié chère passés : refus nommé |
| rejeu sous archive fictive exécuté avant l'écriture de la sortie principale, ou appelé par la production, ou rendant autre chose que k_R et S_R | arrêt ; défaut | exécuté après la sortie principale, par sa fonction propre, vers son second fichier | exécution simulée avant l'écriture : refus ; appel depuis la production : refus nommé ; fonction rendant W : refus |
```

### Mineures

**C3-3** — Le dénominateur de q_w : un monde complet peut n'avoir qu'un appel répondu dans la moitié bon marché ; « 2 à 12 » est faux (1 à 12).

`C3-03`
```
ANCIEN: (dénominateur : 2 à 12 dans un
NOUVEAU: (dénominateur : 1 à 12 (un seul appel répondu, d'une seule carte valide, suffit à une moitié) dans un
```

**C3-4** — Le banc de mutations ne tue ni la définition de « monde complet » par quatre appels, ni l'omission des dollars des appels non répondus, ni la garde B_a, ni l'ordre de la sensibilité : ce sont des gardes neuves (tour 2 et ce tour), donc des mutations.

`C3-04`
```
ANCIEN: la fonction de production appelée avec l'archive fictive ou avec une loi plantée. Toutes tuées pour la raison attendue.
NOUVEAU: la fonction de production appelée avec l'archive fictive ou avec une loi plantée ; « monde complet » défini par quatre appels répondus ; dollars des appels tronqués ou en échec omis ; appel plus long que B_a repris ou non compté en échec ; rejeu sous archive fictive exécuté avant l'écriture de la sortie principale. Toutes tuées pour la raison attendue.
```

**C3-5** — Puissance et épargne à 24 mondes : la règle R-2977 des 24 mondes se justifiait par le minimum de mondes complets ; ce minimum est maintenant presque sûrement atteint (monde complet = une moitié servie : à 0,875 par appel, P(monde complet) = 0,969 et P(n_c ≥ 16 sur 20) ≈ 0,9997) ; et à W_min = 5 le passage à 24 ne gagne aucune puissance. La pièce doit le dire (R3 : puissance) et écrire l'équivalence de S_R à 24 mondes, aujourd'hui laissée « sur 20 ».

`C3-05a`
```
ANCIEN: (annexe A, point 6) ; une perte d'un monde sur vingt passe presque toujours inaperçue.
NOUVEAU: (annexe A, point 6) ; une perte d'un monde sur vingt passe presque toujours inaperçue. **À 24 mondes** (W_min = 5 ; loi binomiale exacte, à recopier par programme en annexe) : « perte établie » avec la probabilité 0,29 à p = 0,15 et 0,79 à p = 0,26 quand les 24 mondes sont à risque, 0,20 et 0,67 sous k_R = 3 (21 mondes à risque), contre 0,35 et 0,80 à 20 mondes et 0,24 et 0,68 sous k_R = 3 : **aucun gain de puissance** à 24 mondes, pour + 20 % de coût ; avec la définition du monde complet de la section « Métrique », le minimum de 0,8 × N est presque sûrement atteint dans les deux cas (à titre d'information, annexe).
```

`C3-05b`
```
ANCIEN: « dans 14 mondes ou plus » à 0,75 ; lue à
NOUVEAU: « dans 14 mondes ou plus » à 0,75 ; à 24 mondes, « dans 16 mondes ou plus » à 0,71 et « dans 17 mondes ou plus » à 0,75 (S_R = 0,25 exactement à k = 16 à 0,75) ; lue à
```

**C3-6** — Étape 2 et « points à remesurer » se contredisent sur ce que le lecteur du pilote peut rendre pour V1 et V6 (« coûts et taux seulement » contre « le témoin positif … et seulement ce champ et les coûts ») ; le tour 2 (O-2) demandait de le dire. Je ramène l'étape 2 au texte plus large et dis que V1 et V6 ne sont plus des prédictions à l'aveugle ; **si la mère préfère l'autre sens (le témoin positif non lu), c'est le texte des points à remesurer qu'il faut changer, non celui-ci** (point pour la mère 3).

`C3-06`
```
ANCIEN: (dits écrits après lecture du pilote, coûts et taux seulement, et de la partie A)
NOUVEAU: (dits écrits après lecture du pilote : coûts, taux d'appels et le seul champ du témoin positif, appels dont une carte va au-delà de K1, rien d'autre, et de la partie A ; ni V1 ni V6 n'est alors une prédiction à l'aveugle, dit dans le texte qui fera foi)
```

**C3-7** — B_a, M : « fixés d'après la durée mesurée du pilote » sans règle ; or le taux du pilote, donc N, dépend de B_a (tout appel du pilote plus long que B_a compte en échec), et N fixe W_min, la puissance et le devis. Écrire l'ordre et la règle d'avance ; les trois nombres (1,5 ; 3 600 s ; M ≤ 2) sont des choix de pratique que l'auteur peut remplacer, sans donnée, à dire tels.

`C3-07`
```
ANCIEN: valeur et mondes en parallèle fixés avant le scellement d'après la durée mesurée du pilote, cette règle seule pouvant bouger), nombre de mondes à la fois M ;
NOUVEAU: valeur et mondes en parallèle fixés avant le scellement d'après la durée mesurée du pilote, par la règle suivante, écrite d'avance : **B_a d'abord** = le plus petit multiple de 300 s au moins égal à 1,5 fois la durée du plus long appel répondu du pilote, au plus 3 600 s ; **puis** le taux du pilote est lu avec cette B_a (section « Taille »), **puis** N, **puis** M = le plus petit entier de 1 à 2 pour lequel le budget de pire cas de la table tient sous 17 h, « non lançable » et mot de la mère s'il n'en est aucun ; les trois nombres 1,5 ; 3 600 s ; 2 sont des choix de pratique, non déduits d'une donnée), nombre de mondes à la fois M ;
```

**C3-8** — Les « 20 » restés écrits pour N = 20 (réserve que la pièce a laissée au tour 3) : le résumé, le dessin, l'étape 3, la ligne de GO, le point (4) des points à remesurer et l'essai sain de la liste d'arrêt se contredisent avec la règle des 24 mondes ; une ligne de GO écrite pour 20 mondes ne couvre pas la branche à 24 (pire cas 235,32). Un couple par endroit.

`C3-08a`
```
ANCIEN: 2. **Dessin** : 20 mondes MR-2 neufs du secret du crible, archive {K1}, une génération, **les quatre proposeurs du pilote
NOUVEAU: 2. **Dessin** : N mondes MR-2 neufs du secret du crible (N = 20, ou 24 si le taux d'appels répondus du pilote est sous 0,95), archive {K1}, une génération, **les quatre proposeurs du pilote
```

`C3-08b`
```
ANCIEN: appelés partout** (80 appels) ;
NOUVEAU: appelés partout** (80 appels à N = 20, 96 à N = 24) ;
```

`C3-08c`
```
ANCIEN: **196,60 au pire**
NOUVEAU: **196,60 au pire** à 20 mondes (**235,32** à 24 mondes : crédits 120,00, hors crédits 115,32)
```

`C3-08d`
```
ANCIEN: phrase, mondes, feu réel) ; essai à blanc avec proposeurs scriptés et vraies pièces servies ; puis les 80 appels.
NOUVEAU: phrase, mondes, feu réel) ; essai à blanc avec proposeurs scriptés et vraies pièces servies ; puis les 4 N appels (80 ou 96).
```

`C3-08e`
```
ANCIEN: Claude », « hors crédits ») ; montants à refaire sur le devis mesuré.
NOUVEAU: Claude », « hors crédits ») ; montants à refaire sur le devis mesuré. **À N = 24** (règle de la section « Taille ») : κv1 120,00 USD (Pr-2 48,00 ; Pr-4 72,00), κv2 115,32 USD (Pr-1 56,16 ; Pr-3 56,16 ; machine 3,00), 24 mondes ; les lignes s'écrivent pour le N que fixe cette règle, jamais pour l'autre.
```

`C3-08f`
```
ANCIEN: | monde sans tirage conforme en 8 ; C-16 ou C-17 en défaut | arrêt avant tout appel | 20 mondes conformes |
NOUVEAU: | monde sans tirage conforme en 8 ; C-16 ou C-17 en défaut | arrêt avant tout appel | N mondes conformes |
```

`C3-08g`
```
ANCIEN: risque d'arrêt par « coût au-dessus du pire cas », multiplié par 20 appels)
NOUVEAU: risque d'arrêt par « coût au-dessus du pire cas », multiplié par N appels)
```

**C3-9** — V7 : « borne haute à 95 % » sans méthode ni sens (unilatéral ou bilatéral) ; la zone d'indécision (« borne haute ≥ 0 ») ajoutée au tour 2 en dépend.

`C3-09`
```
ANCIEN: V7 : aucune pièce sur ces proposeurs devant ces mondes.
NOUVEAU: V7 : aucune pièce sur ces proposeurs devant ces mondes. Intervalle de la moyenne de C_E − C_B : rééchantillonnage des mondes, 10 000 rééchantillons, bornes aux percentiles 2,5 et 97,5 (intervalle bilatéral à 95 %) ; la « borne haute » de V7 est la borne à 97,5 %.
```

## Remarques facultatives (aucune n'est exigée)

- F-1 : V1 « k_R ≤ 3 sur 20 » et V3 « L_R ≥ 4 » sont des comptes absolus ; à N = 24 ils ne sont plus à l'échelle (3,6 ; 4,8). Les chiffres de V1 et V6 sont permis au refait (étape 2) ; à dire au texte qui fera foi si l'échelle est gardée ou changée.
- F-2 : à 16 appels de pilote (4 mondes × 4 proposeurs), « taux ≥ 0,95 » ne s'atteint qu'à 16 sur 16 : la règle de R-2977 revient à « 20 mondes si aucun appel du pilote n'a échoué, 24 sinon ». C'est ce qu'elle dit ; le dire en clair aiderait la mère.
- F-3 : cas d'un appel coupé par B_a : son coût est celui que les journaux du relais donnent, jamais le plafond ; si le relais ne le journalise pas, c'est la ligne « coupure sans trace dans le journal : arrêt » qui le couvre : bien.
- F-4 : O-1 à O-5 du tour 2 : O-3 (DISCERN) et O-4 (échelle de V1) restent sans effet.

## Points pour la mère

1. **Les 24 mondes ne servent plus à rien de ce que R-2977 leur demandait.** La décision (24 mondes si le taux d'appels répondus du pilote est sous 0,95) visait le minimum de mondes complets. Depuis le tour 2, un monde complet n'exige qu'une moitié servie : le minimum est atteint presque sûrement à 20 comme à 24 ; à W_min = 5 la puissance de 24 mondes est égale ou inférieure à celle de 20 (0,787 contre 0,804 à p = 0,26) ; le coût monte de 20 % (235,32 USD au pire contre 196,60). Les comptes de marche de R-2981 (2 appels tronqués) font prendre la branche à 24 presque sûrement. **Décision à prendre avant scellement** : (a) garder la règle écrite (écart de coût sans gain) ; (b) fixer N = 20 dans tous les cas (écart à R-2977, mot de la mère) ; je recommande (b) ; confiance 0,6. Sans effet sur les corrections ci-dessus.
2. **Étage 5 (ablation) aux critères gelés de (v)** : N-045 point 3 la dit « rapportée, hors des critères gelés » ; R-2977 ne la fait entrer aux critères gelés que pour (iii). Reste à trancher **avant scellement** (point 3 du tour 2, non tranché) ; je recommande de la rapporter sans verdict ; confiance 0,6.
3. **Lecteur du pilote** : pour V1 et V6, le témoin positif est lu ou non ? C3-6 aligne l'étape 2 sur « lu » ; si la mère veut l'inverse, la ligne « Le témoin positif du pilote … » des points à remesurer est à retirer (V1 et V6 restent alors à l'aveugle, au prix de chiffres moins informés). Le lecteur du pilote ne doit rendre que : comptes d'appels répondus, tronqués, en échec ; durées ; coûts ; et, si C3-6 est gardé, ce seul champ.
4. **Points 1 et 3 de « Choix et doutes »** : R-2977 dit « recommandations de l'auteur sauf mention » ; la pièce les laisse ouverts. À confirmer (plafonds à 2,34 ; garder les quatre proposeurs).
5. **Enveloppe d'ensemble** de GO-2026-11-15-06 : (v) est à 196,60 au pire (235,32 à 24 mondes) ; l'attendu 73,30 de la note est sous la borne basse de la fourchette de la pièce (79,95 à 92,75 aux prix publics, 107 à 126 au compte de la configuration) ; le registre R-2983 donne pour le pilote 11,08 USD sur crédits et 4,30 hors crédits (aux prix de la configuration, 4 mondes, 8 appels sur crédits) : par monde, ≈ 2,77 sur crédits contre 2,40 attendus pour Pr-2 et Pr-4 ; transposé à 20 mondes, ≈ 55 USD sur crédits contre 48 attendus. Je n'ai pas ouvert la pièce de dépense : à refaire par le compte organisme sur le coût mesuré, comme la pièce le dit ; le compte des cinq cribles est à refaire avant d'inscrire une ligne.
6. **Date de lancement** : fixée par le code neuf, non par le préenregistrement (réponse nette au point 4) ; fenêtre du GO jusqu'au 30 novembre ; le prix public de Pr-1 double le 1er décembre.
7. **Après l'application de ces corrections** : ajouter à « Contre-lecture » une entrée « Contre-lecture 3 » (ce rapport : empreinte entière lue dans son compagnon `.sha256` ; brouillon relu `8a21f085d0caff7d2ec392e326b30c03616d67f066460eed54bae5aed5aeca6a`), mettre à jour le statut, nommer les couples propres ; le lecteur du tour 4 doit être neuf (ni moi, ni le rédacteur, ni les lecteurs et rédacteurs des tours 1 et 2). Les corrections de ce tour sont à faire écrire par le modèle A (R-2982) ; si elles le sont par un autre modèle, le dire.
8. **Noms de champs de la partie A** (`retenues`, `promue`, rejet, mort) : à vérifier par le code avant l'essai sain (T2-4, point 7 du tour 2) ; je n'ai pas ouvert le relevé.

## Incidents de ma main

- Aucun fichier écrit hors de ce rapport et de son compagnon d'empreinte, et d'un programme de contrôle jetable dans le bloc-notes de ma session (lecture seule des pièces ; le contrôle des « ancien » de ce rapport y est lancé en lecture seule).
- `git fetch` par refspec de deux branches (`lot/compte-organisme-v1`, `prep/pilote-mr2-compte-organisme-v1`) ; aucun clone ; `git show` pour relire des lignes de plafonds et des empreintes.
- Le `grep` sur « R-2981 », « R-2982 », « R-2983 », « R-2985 » de `registres/decisions.md` a affiché le début de lignes qui rapportent des comptes de marche du pilote (« 14 mondes complets, 0 échec, 2 tronqués ») et des coûts du pilote (R-2983) : **comptes de marche et coûts, non une issue** ; je ne m'en sers que pour illustrer le taux par appel (C3-5, point pour la mère 1) et le coût (point 5), jamais comme issue du pilote. Je n'ai ouvert ni `retour/`, ni la branche de sortie du pilote, ni le relevé de v67, ni aucun fichier sous `diag/`, `runs/`, `donnees/`.
- Pas d'empreinte calculée sur un fichier interdit.

## Vérification des « ancien »

Contrôle (lecture seule, bibliothèque standard, `python3 -I`) : les 18 blocs `C3-…` de ce rapport (C3-01a à C3-09), chaque « ANCIEN » sur une seule ligne et trouvé **exactement une fois** dans la pièce (`8a21f085…`) ; aucun chevauchement entre les 18 ancrages ; 0 défaut. Application d'essai de ces 18 couples au brouillon 3, dans le bloc-notes de ma session : le validateur `controle_ia.prereg.problemes` rend **une liste vide** sur le résultat. Les calculs (loi binomiale exacte, bornes de Clopper-Pearson par bissection) sont à refaire par programme et à recopier en annexe par l'auteur.
