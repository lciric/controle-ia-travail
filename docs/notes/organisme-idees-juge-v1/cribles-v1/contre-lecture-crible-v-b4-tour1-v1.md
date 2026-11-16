# Contre-lecture du préenregistrement du crible (v), brouillon 4 — tour 4 — v1

- Contre-lecteur : sous-agent neuf, **modèle C** (identité dite en conversation seulement) ; auteur du brouillon 1 : modèle A ; corrections du brouillon 4 écrites par un rédacteur du modèle A (la pièce le dit) ; je n'ai écrit aucune pièce citée ; je n'ai lu ni les dossiers ni le rapport du premier lecteur (modèle B), qui n'en a pas rendu.
- Date (UTC) : lecture de 14:18:01Z à 14:28:41Z (`date -u`) ; lecture entière de la pièce.
- Pièce relue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-v-brouillon4.md`, empreinte entière `af6e6db3a74ef099f6f62da8ef1c2af7ddc703a2c9a18415b25f6dba27388f86` (vérifiée par `sha256sum`, égale à son compagnon). Brouillon 3 : `8a21f085d0caff7d2ec392e326b30c03616d67f066460eed54bae5aed5aeca6a` (égale à son compagnon et à la pièce). Rapport du tour 3 : `b693bf5d279c2b234807702cb23ab5c4d97e017ae06171dff28e44c64c3ac523` (égale). Programme d'application `appliquer-corrections-crible-v-brouillon4.py` (compagnon vérifié ; non exécuté). Programme `comptes-crible-v-brouillon4.py` et sa sortie (compagnons vérifiés ; sortie relue, voir point 3).
- Pièces lues : la pièce en entier ; le rapport du tour 3 en entier ; le différentiel brouillon 3 / brouillon 4 ; R-2977 et R-2982 de `registres/decisions.md` (par `grep` de ces seules lignes) ; la ligne GO-2026-11-15-06 de `registres/go.md` ; N-058 ; N-045 (point 3 et 4) ; la note des idées originales (section (v)) ; le bloc gelé et la procédure v14 du pilote (après `git fetch` par refspec de `lot/compte-organisme-v1` et `prep/pilote-mr2-compte-organisme-v1`, `git show` au commit demandé pour la procédure) ; la lecture des prix publics v2 (lignes de prix) ; `prereg/gabarit-preregistrement-v1.md` et `src/controle_ia/prereg.py` (fonction `problemes`). **Non lu** : tout ce que la consigne interdit (rien sous `diag/`, `runs/`, `donnees/` ; relevé de v67 non ouvert ; sortie du pilote non ouverte, lignes R-2981, R-2983 et R-2985 non lues ; 7a, 7b, T0.6, T0.7, P3-bis, bras d'attaque). Aucun appel de modèle, aucune dépense, aucune machine, aucun `pytest`.

## Verdict

**corrections.** Les 18 couples du tour 3 sont appliqués fidèlement (voir ci-dessous) et le validateur ne rend aucun défaut. Mais la pièce garde **cinq défauts majeurs** : une contradiction entre la lecture gelée de H-v et la description de l'issue la plus probable (B4-01), un étage 0 qui, tel qu'écrit, rend « non jugeable » une exécution où un appel est simplement coupé à B_a ou où la partie A est invalide (B4-02), une règle de dépassement de la réflexion de Pr-1 laissée en blanc alors que la liste d'arrêt est dite gelée (B4-03), un budget de durée dont quatre termes sont des blancs et qui n'est pas chiffré (B4-04), et l'absence de règle écrite d'avance pour refaire le devis d'après le pilote (B4-05) ; plus **sept séries de défauts mineurs** (B4-06 à B4-12). Pas de « a_refaire » : la conception tient ; tout se corrige par les couples ci-dessous. **5 majeures, 7 mineures** (B4-03, B4-04, B4-05 portent deux couples ; B4-07 deux ; B4-11 deux ; B4-12 cinq), **5 remarques facultatives**.

## Vérification de l'application des corrections du tour 3

1. **18 couples du rapport.** Lus par programme (bibliothèque standard, `python3 -I`, lecture seule) dans le rapport du tour 3 : 18 blocs `C3-…`. Chaque « ANCIEN » figure **une fois** dans le brouillon 3 ; chaque « NOUVEAU » figure **une fois** dans le brouillon 4. **Appliqués fidèlement, sans retouche** : C3-01a à C3-09.
2. **Différentiel.** Le brouillon 3 auquel j'applique moi-même les 18 couples, comparé au brouillon 4, ne diffère que par les sept couples propres que la pièce nomme (titre, ligne « Brouillon 4 » de l'en-tête, statut, validateur, tête de « Contre-lecture », point 11 de l'annexe A, entrée « Contre-lecture 3 »). **Rien d'autre.** Aucun ne touche un critère, un seuil, une graine ni une ligne d'arrêt.
3. **Entrée « Contre-lecture 3 »** : heures (14:01:47Z à 14:08Z), comptes (2 majeures, 7 mineures, 4 remarques), empreintes du rapport et du brouillon 3, nom du programme, rôle (corrections écrites par le modèle A, R-2982) : **exacts**. **Annexe A, point 11** : je l'ai refait par programme (bibliothèque standard, Clopper-Pearson par bissection, loi binomiale exacte, épargne en fractions) : W_min 4 de 16 à 22, 5 à 23 et 24 ; puissances 0,352 ; 0,804 (20 mondes à risque), 0,244 ; 0,681 (17), 0,287 ; 0,787 (24), 0,197 ; 0,671 (21) à p = 0,15 ; 0,26 ; seuils de k_R pour S_R ≥ 0,25 (appel des chers permis jusqu'à k_R = 12 à la part 0,71 et 13 à 0,75 sur 20 mondes ; 15 et 16 sur 24 mondes : exactement comme la pièce) ; grille de la probabilité de monde complet (0,8281 à r = 0,70 ; 0,9950 à 0,95) ; devis au pire 196,60 et 235,32 : **tous égaux** à la sortie recopiée.
4. **Validateur** : `controle_ia.prereg.problemes('…/crible-v-brouillon4.md')` rejoué : **liste vide**. Aucun identifiant de modèle hors les deux clés de configuration `opus55` et `fable52` que la pièce dit (remarque F-3).
5. **Empreintes citées** : recalculées par `sha256sum` et **égales** à celles de la pièce : note des idées originales, relevé des idées, `go.md` à `377a2a0c` (`4bcec4a0…`), conceptions v3 et v4 du monde riche, résumé v4, faits du collisionneur, les trois outils, `mesure_pilote_v4.py`, verdict v67, texte scellé de la boucle réelle, N-044, N-045, N-053, N-058, N-067, question de la course, catalogue, les deux modèles de forme, gabarit, `prereg.py`, devis du pilote, PDF 2609.17560v1, les quatre PDF des citations obligatoires, brouillons 1 à 3, rapports des tours 1 à 3, programme et sortie du point 11 ; texte scellé du pilote (`8aa33014…`) et procédure v14 (`20355627…`, au commit `2d35cafa…`), lecture des prix publics v2 (`b88253b8…`) par `git show`. Les deux programmes de l'annexe A (`comptes_cribles_v2.py`, `compte_certifiees_mr2_v1.py`) n'existent pas sur disque : je les ai extraits des blocs recopiés dans `crible-iii-brouillon1.md` et leurs empreintes sont **égales** (`f06bcfe7…`, `8c0432df…`).

## Réponses aux neuf points

**(1) R1.** Hypothèse, prédictions V1 à V7 (confirmation, réfutation, indécision), métrique, seuils, plan d'analyse, critères gelés, liste d'arrêt : présents. **Portes restantes** : (a) B4-01 : le texte gelé dit deux choses de l'issue « V1, V2, V3 vraies » (H-v « réfutée » contre « non éprouvée ») ; (b) B4-02 : l'étage 0 est ambigu avec trois lignes d'arrêt dont l'action n'est pas un arrêt ; (c) B4-03 : la règle du dépassement de Pr-1 est « fixée avant scellement » alors que l'étape 2 dit la liste d'arrêt gelée ; (d) B4-04 : quatre termes du budget de durée sont des blancs ; (e) B4-05 : rien n'écrit comment les coûts du pilote deviennent l'attendu du devis. Aucune de ces portes ne s'ouvre après lecture d'un résultat du crible : elles s'ouvrent après la lecture du pilote, ce qui reste permis, mais seulement par des règles écrites maintenant.

**(2) R3.** *Seuils 0,25 et 4 sur 20.* Étiquetés « choix de ce texte, de portée pratique, non déduit d'une donnée » : aucune justification par une donnée, avouée, et aucune voie vers un signe positif (les deux seuils jouent contre H-v : W_R = 0 est exigé pour « non réfutée », et S_R < 0,25 la réfute). Puissance refaite et exacte : 0,80 pour une perte à p = 0,26 sur 20 mondes à risque, 0,68 sur 17 (k_R = 3), 0,13 à p = 0,10 ; à 24 mondes (W_min = 5) 0,79 et 0,67 : **aucun gain**, dit par la pièce. Un crible qui ne voit pas une perte de 10 % à 15 % : dit. *Cas dégénéré.* L'issue « non éprouvable » est **définie et gelée** (k_R < 4 ou k_R > n_c − 4, prime sur l'étage 3, lecture de H-v) ; le crible reste **informatif pour l'ablation** (étage 5, QO1) et pour les parts de copies, **non pour la règle** : l'auteur lui-même donne V1 (k_R ≤ 3) à 0,65 et V6 à 0,6, donc plus d'une chance sur deux que H-v ne soit pas éprouvée. Le bras à archive enrichie est refusé par R-2977 (décision (a)) ; la sensibilité « archive fictive » ne rend que k_R et S_R, jamais W : elle ne peut pas éprouver la perte. **Écart non corrigé, laissé à la mère** : point pour la mère 3 et remarque F-2. *Distance dans un seul sens.* Écart **déclaré** (section « Écarts »), sensibilité au minimum des deux sens rapportée, biais dit du côté « épargne » : tenu ; remarque F-5 (une carte plus pauvre que K1 n'est pas une copie). **Contradiction trouvée dans la même zone : B4-01.**

**(3) Devis.** Recompte : 20 appels par proposeur, 80 en tout (96 à 24) ; plafonds 2,34 ; 2,00 ; 2,34 ; 3,00 (relus dans le bloc gelé : `argon` et `astra` 2,34 ; `opus55` 2 ; `fable52` 3 ; parts 9,36 ; 9,36 ; 8 ; 12 pour 4 mondes) ; pires 46,80 ; 40,00 ; 46,80 ; 60,00 ; machine 3,00 ; crédits 100,00 ; hors crédits 96,60 ; total 196,60 ; à 24 : 56,16 ; 48,00 ; 56,16 ; 72,00 ; 120,00 ; 115,32 ; 235,32 : **exacts**. Attendus : 20 × (0,25 + 0,80 + 1,00 + 1,60) = 73,00 + 0,30 = 73,30 ; crédits 48,00 ; hors crédits 25,30 : **exacts**. Fourchette aux prix publics : 79,95 à 92,75 ; crédits 39,60 à 49,20 ; hors crédits 40,35 à 43,55 : **exacts** ; au compte de la configuration (Pr-1 à 34 à 42) : 106,95 à 125,75, part des crédits 37,0 % à 39,1 % : **exacts**. Hypothèses de coût par appel (0,33 ; 0,66 ; 1,65 ; 1,32) : recalculées avec 16 500 jetons d'entrée et 30 000 de sortie, égales. Pires cas par proposeur : 53 024 jetons d'entrée et la borne de sortie donnent 2,33 ; 1,99 ; 2,33 ; 2,98 : cohérents avec les plafonds. Deux comptes des dollars : dits (prix public principal, prix de la configuration en sensibilité, prix de Pr-1 doublé le 1er décembre). Cohérence avec GO-2026-11-15-06 : ligne de type « calcul », parts séparées crédits / hors crédits, mot de Lazar cité, échéance 30 novembre, devis refait et contre-lu avant inscription : **conforme**, sous réserve de B4-10 (l'effort « high » du pilote manque à la ligne κv1) et B4-05 (la règle qui refait le devis). Part sur crédits : 50,9 % du pire cas, 49,5 % à 53,0 % de la fourchette publique : exacts ; « 100 % de ce que la configuration permet » : exact (les deux autres proposeurs sont hors crédits, la machine aussi). L'attendu de la note (73,30) est sous la borne basse de la fourchette de la pièce : dit. **Enveloppe d'ensemble** : point pour la mère 6.

**(4) Durée.** **Réponse nette : le code du pilote ne suffit pas ; il faut du code neuf et une procédure neuve, mais pas une configuration neuve** (la configuration v12, ses plafonds et ses parts restent ; seule la variante « plafond de 0,75 pour Pr-1 » en demanderait une, et elle n'est pas retenue). À écrire : lanceur pour N mondes et 4 N appels avec borne par appel B_a et M mondes à la fois (le lanceur du pilote est écrit pour 4 mondes et 16 appels), `mesure_crible_v_v1.py`, `lire_crible_v_v1.py`, programme de la partie A, procédure de machine dérivée de la v14, essais R5 et banc de mutations, contre-lecture du code, addendum d'empreintes, deux lignes de GO, éventuellement une sonde neuve. **Ce code, et non le préenregistrement, fixe la date de lancement** (« plusieurs jours, non mesuré », dit la pièce, dans une fenêtre de GO qui échoit le 30 novembre ; le prix public de Pr-1 double le 1er décembre). **Borne** : la pièce donne une règle (B_a = plus petit multiple de 300 s ≥ 1,5 fois le plus long appel répondu du pilote, au plus 3 600 s ; puis le taux, puis N, puis M de 1 à 2) mais **aucune table chiffrée** et quatre termes en blanc. Mon calcul, avec les durées typiques de la pièce (mise en place 0,5 h ; barrières 100 minutes comme [PROC-14] § 0 ; génération 1,0 h à 20 mondes, 1,2 h à 24, comptée trois fois ; mesure 1 h ; rapatriement 0,5 h) : B_a maximal qui tient sous 17 h : **N = 20, M = 1 : 1 859 s ; N = 20, M = 2 : 3 719 s ; N = 24, M = 1 : 1 460 s ; N = 24, M = 2 : 2 920 s** ; avec 2 h 40 de barrières au lieu de 100 minutes : 1 679 ; 3 358 ; 1 309 ; 2 619. Donc, **dès que le plus long appel répondu du pilote dépasse environ 1 200 s (B_a ≥ 1 800 s), le crible ne tient dans la minuterie qu'avec deux mondes à la fois**, et à 24 mondes il faut B_a ≤ 2 400 s ; la concurrence des relais est « non éprouvée » : B4-04 exige l'essai à blanc à la valeur de M. Si aucune case ne tient : « non lançable » et mot de la mère (la pièce le dit).

**(5) Liste d'arrêt, graines.** Chaque ligne a son essai sain et son artefact (R5) ; lignes neuves du tour 3 conformes (rejeu sous archive fictive, minuterie, B_a). Défauts : B4-02 (étage 0 contre actions « le crible continue », « partie A invalide ») ; B4-03 (ligne du coût d'un appel : règle en blanc). Graines : `numpy.random.SeedSequence`, racine = entier de l'empreinte du texte qui fera foi, clés `(r, 30)`, `(67, g, 30)`, `(99, b)`, `(97, k)`, `(98, w)` (racine : empreinte de `CARTES.json`) sans collision ; `graine_monde_pilote` reprise du pilote (relue dans le texte scellé du pilote, ligne de la graine du monde) ; R9 conforme. Le « 2 h 40 » des barrières n'est pas expliqué (B4-04).

**(6) N-058.** Le crible est borné à la génération 1, archive {K1}, aucun verdict dans l'archive ; la règle ne lit que les lois des cartes bon marché, K1 et un jeu public sans issue ; l'évaluation se fait sur l'oracle et le coût ; la dépendance indirecte au-delà de la génération 1 est dite (« Écarts », « Choix » 11) et renvoyée à Lazar avec le nœud d'adoption (R-2977). **Aucune violation de N-058.** Une réserve : la partie A lit la liste des « retenues » de v67, qui est un résultat du juge, contre la lettre de R-2977 (« sans aucun verdict du juge ») : dit par la pièce, borné « sans rien décider », mais voir point pour la mère 7 et remarque F-4.

**(7) Partie A.** Déclarée descriptive, « sur des données déjà vues (R-2977) », sans critère, sans verdict du juge sauf la liste des retenues, sortie scellée avant lecture, aucun seuil changé ; ligne d'arrêt avec son essai sain et ses artefacts. Je n'ai pas ouvert le relevé : je n'ai vérifié que ce que la pièce déclare (23 cartes, 11 + 12, archive de la génération 2 = K1 et 11 retenues : égal au verdict v67, V-2 et V-7). Rien à corriger hors F-4.

**(8) R7 et R8.** Aucun chiffre de l'état de l'art ; antériorités « à chercher » et « à vérifier », zone dite « séduisante » à vérifier plus durement ; citations obligatoires de N-064 et N-067 présentes avec empreintes (égales). Rien à corriger.

**(9) Validateur, identifiants, empreintes.** Voir « Vérification », points 4 et 5.

## Corrections exigées

Chaque « ancien » est une chaîne d'une seule ligne de la pièce, présente **une seule fois** (vérifié par programme, `python3 -I`, sur le brouillon 4, empreinte ci-dessus) ; aucun couple ne chevauche un autre ; les « nouveau » sont des propositions à écrire par l'auteur (modèle A) ; « \n » dans un « nouveau » = saut de ligne. Les chiffres que j'ai recomptés (point 4 ci-dessus) sont à refaire par programme et à recopier en annexe.

### Majeures

**B4-01 — « Réfutée » ou « non éprouvée » ? Deux lectures gelées de la même issue.** La section « Prédiction » dit : « V1, V2 et V3 vraies : … **perd** : H-v réfutée au crible ». Or V1 vraie est k_R ≤ 3, et la lecture gelée de H-v dit : « Si k_R < 4 … H-v est dite **non éprouvée au crible** quel que soit l'étage 3 ». « En dix lignes », point 7, dit « non éprouvée ». Une issue décrite deux fois, avec deux verdicts : c'est une porte de sortie (R1) et la phrase des « issues » est celle que la mère et Lazar liront.

`B4-01`
```
ANCIEN: **perd** : H-v réfutée au crible ; la lecture porte en fait sur l'ablation (H-v-a).
NOUVEAU: **perd** : étage 3 (b) « épargne avec perte établie » ; mais V1 vraie veut k_R < 4, donc H-v est dite **« non éprouvée au crible »** (section « Critères de lecture gelés », lecture de H-v), non « réfutée » : la règle se confond alors avec « jamais les chers » ; la lecture porte en fait sur l'ablation (H-v-a, étage 5).
```

**B4-02 — Étage 0 : « une ligne d'arrêt déclenchée » rend « non jugeable » des exécutions que la pièce veut jugeables.** La liste d'arrêt contient des lignes dont l'action n'est pas un arrêt : « appel plus long que B_a » (« appel coupé et compté échec ; le crible continue »), « partie A … invalide ; partie B inchangée », « fournisseur abandonné … arrêt du crible ; « non concluant » ». L'étage 0 les rend toutes « non jugeable (arrêt) : aucune issue lue, pas même l'étage 1 ». Lue à la lettre, une seule coupure à B_a (cas courant, B_a étant fixée à 1,5 fois le plus long appel du pilote) interdit de lire la partie B, et la partie A invalide aussi ; et « non concluant » ne peut pas sortir de la ligne « fournisseur abandonné ». Verdict gelé ambigu sur le cas le plus probable.

`B4-02`
```
ANCIEN: | 0 | une ligne d'arrêt déclenchée ; ou la mesure en erreur | « **non jugeable (arrêt)** » : aucune issue lue, pas même l'étage 1 |
NOUVEAU: | 0 | une ligne de la liste d'arrêt dont l'action est « arrêt » (code 3 compris), « défaut » ou « run invalide » déclenchée ; ou la mesure en erreur. **Ne comptent pas à l'étage 0** : la ligne « appel plus long que B_a » (appel coupé et compté « échec », le crible continue : lu à l'étage 1 par les comptes d'appels), la ligne « fournisseur abandonné… » (verdict « non concluant » : étage 1) et la ligne de la partie A (« partie A invalide, partie B inchangée » : la partie A est rapportée invalide, sans effet sur le verdict de la partie B) | « **non jugeable (arrêt)** » : aucune issue lue, pas même l'étage 1 |
```

**B4-03 — Règle du dépassement de la réflexion de Pr-1 : un blanc dans une liste d'arrêt dite gelée.** La ligne « coût d'un appel au-dessus de son pire cas » dit « règle … fixée avant scellement d'après la réflexion mesurée au pilote (borne, ou dépassement toléré jusqu'à une valeur écrite, ou arrêt) ». Or l'étape 2 dit sont gelés « … la liste d'arrêt » et ne liste pas cette règle parmi ce qui peut changer. Enjeu réel : le coût attendu d'un appel de Pr-1 au compte de la configuration est 1,7 à 2,1 USD pour un plafond de 2,34 (réflexion ajoutée hors de la borne de sortie) ; un seul dépassement parmi 20 à 24 appels déclenche l'arrêt (code 3) et, par l'étage 0, « non jugeable ». Il faut le défaut écrit maintenant et la seule modification permise nommée à l'étape 2.

`B4-03a`
```
ANCIEN: **règle du dépassement de la réflexion de Pr-1 fixée avant scellement d'après la réflexion mesurée au pilote (borne, ou dépassement toléré jusqu'à une valeur écrite, ou arrêt) : un seul appel ne doit pas rendre « non jugeable » 20 mondes payés sans que ce choix soit écrit**
NOUVEAU: **règle du dépassement de la réflexion de Pr-1, écrite d'avance : par défaut, tout dépassement du pire cas d'un appel arrête (code 3), inchangé ; la seule modification permise à l'étape 2 est de remplacer « arrêt » par « toléré, facturé, compté dans les dollars et rapporté » pour un appel de Pr-1 dont le coût compté ne dépasse son plafond de session que de la réflexion et reste sous X fois ce plafond, X = le plus petit multiple de 0,05 au moins égal à 1,25 fois le plus grand rapport coût compté / plafond mesuré sur les appels de Pr-1 du pilote, au plus 1,5, la somme restant sous la part de Pr-1 ; sans mesure du pilote qui le justifie, l'arrêt reste ; 1,25 et 1,5 sont des choix de pratique, non déduits d'une donnée**
```

`B4-03b`
```
ANCIEN: peuvent changer les montants du devis, B_a, M, le nombre de mondes (règle de la section « Taille »),
NOUVEAU: peuvent changer les montants du devis (règle d'avance de la section « Devis »), B_a, M, la tolérance de dépassement de la réflexion de Pr-1 (ligne « coût d'un appel » de la liste d'arrêt, règle écrite d'avance), le nombre de mondes (règle de la section « Taille »),
```

**B4-04 — Durée : budget de pire cas non chiffré, quatre termes en blanc, concurrence non essayée.** La pièce écrit « budget de pire cas = mise en place + barrières (2 h 40) + génération de N mondes (pire cas écrit) + ⌈N/M⌉ × B_a + mesure + rapatriement » et « chiffré dans une table » : aucune table, et quatre des six termes n'ont pas de valeur ni de règle ; M et « non lançable » dépendent pourtant de ce budget (étape 2 : seuls B_a, M, N, les montants peuvent changer). Les « 2 h 40 » ne se retrouvent pas dans [PROC-14] (phrase 60 min, feux 20 + 20 min, mondes lents jusqu'à 60 min : 100 minutes de barrières, 160 minutes avec les mondes lents), donc risque de double compte avec la génération. Mon calcul (réponse (4)) montre que la plupart des cases ne tiennent qu'avec M = 2, dont la concurrence « n'est pas éprouvée » : l'essai à blanc doit être joué à la valeur de M.

`B4-04a`
```
ANCIEN: budget de pire cas = mise en place + barrières (2 h 40) + génération de N mondes (pire cas écrit) + ⌈N/M⌉ × B_a + mesure + rapatriement, **≤ 17 h**, chiffré dans une table pour N = 20 et pour N = 24
NOUVEAU: budget de pire cas = mise en place + barrières + génération de N mondes + ⌈N/M⌉ × B_a + mesure + rapatriement, **≤ 17 h**, **chacun des quatre termes autres que les appels écrit en nombres dès ce texte** : trois fois sa durée mesurée au pilote (la génération rapportée à N mondes d'après les 4 mondes du pilote ; trois : choix de pratique, non déduit d'une donnée) ; barrières : 100 minutes (phrase 60, deux feux de 20, [PROC-14] § 0) ; les « 2 h 40 » de ce texte (100 minutes plus 60 minutes de mondes lents) ne se comptent qu'une fois, pas aussi dans la génération ; le budget est **chiffré dans une table pour N = 20 et pour N = 24, B_a de 1 800 à 3 600 s par pas de 600 s, M = 1 et M = 2**, avec la case « non lançable » écrite en clair
```

`B4-04b`
```
ANCIEN: essai à blanc avec proposeurs scriptés et vraies pièces servies ; puis les 4 N appels (80 ou 96).
NOUVEAU: essai à blanc avec proposeurs scriptés et vraies pièces servies, **joué à la valeur de M retenue** (M mondes servis à la fois, 4 M relais ouverts, quatre empreintes de corps égales par monde, une coupure à B_a simulée) ; puis les 4 N appels (80 ou 96).
```

**B4-05 — Aucune règle écrite d'avance pour refaire le devis d'après le pilote.** La pièce liste les « points à remesurer » (jetons, durées, taux, réflexion…) mais ne dit ni ce qui se refait (l'attendu et la fourchette ; non les pires cas, qui sont les plafonds × N), ni comment un coût mesuré (quatre appels par proposeur au pilote) devient l'attendu, ni si les montants des lignes de GO bougent (« montants à refaire sur le devis mesuré » le suggère à tort : ils sont les plafonds). La consigne de ce tour l'exige : « quels chiffres du devis seront refaits d'après le pilote, par une règle écrite d'avance ». Sans elle, le choix de la moyenne, du maximum ou de la médiane reste libre après lecture.

`B4-05a`
```
ANCIEN: **Points à remesurer d'après le coût réel du pilote MR-2** (relevé des relais, sans lire aucune issue) :
NOUVEAU: **Règle d'avance du devis refait** : (a) les pires cas (plafonds de session du bloc gelé × N, machine 3,00) et les montants des lignes de GO κv1 et κv2 **ne changent pas** avec le pilote, seulement avec N ; (b) l'attendu par appel d'un proposeur = moyenne arithmétique des coûts mesurés de **tous** ses appels du pilote (répondus, tronqués ou en échec, tels que facturés), au prix public puis au prix de la configuration, et la fourchette = leur plus petit et leur plus grand (quatre appels par proposeur : dit dans le texte) ; l'attendu du crible = N fois la somme des quatre moyennes, plus la machine (durée de la table de durée × prix horaire relu) ; (c) un coût mesuré au-dessus du plafond de session est dit tel quel et la règle de dépassement de la liste d'arrêt s'applique ; (d) rien d'autre ne se refait. **Points à remesurer d'après le coût réel du pilote MR-2** (relevé des relais, sans lire aucune issue) :
```

`B4-05b`
```
ANCIEN: montants à refaire sur le devis mesuré. **À N = 24**
NOUVEAU: montants : pires cas (plafonds × N), inchangés par le pilote (règle d'avance du devis refait, section « Devis »). **À N = 24**
```

### Mineures

**B4-06** — « Perte » : la phrase dit « 4 pour n_c de 16 à 20 » alors que la table de « Seuil » et « En dix lignes » (point 6) disent 4 de 16 à 22 et 5 à 23 ou 24 ; or n_c = 21 ou 22 est possible à 24 mondes tirés (minimum 20). La parenthèse est aussi restée ouverte.

`B4-06`
```
ANCIEN: n_c de 16 à 20 (annexe A, point 5) ;
NOUVEAU: n_c de 16 à 22, 5 pour n_c = 23 ou 24 ; annexe A, points 5 et 11) ;
```

**B4-07** — « En dix lignes », point 8 : depuis C3-08c, « (100 sur crédits, 96,60 hors crédits) » suit la parenthèse des 24 mondes et se lit comme leur ventilation ; or ces deux chiffres sont ceux de 20 mondes.

`B4-07a`
```
ANCIEN: **196,60 au pire** à 20 mondes (**235,32** à 24 mondes : crédits 120,00, hors crédits 115,32)
NOUVEAU: **196,60 au pire** à 20 mondes (100 sur crédits, 96,60 hors crédits ; **235,32** à 24 mondes : crédits 120,00, hors crédits 115,32)
```

`B4-07b`
```
ANCIEN: (100 sur crédits, 96,60 hors crédits), au-dessus des 183 de [NOTE] parce que
NOUVEAU: ; à 20 mondes, au-dessus des 183 de [NOTE] parce que
```

**B4-08** — « Épargne » : les sommes sur w ne disent pas sur quels mondes (a_w n'est défini que pour un monde complet) ; les dollars des mondes non complets, payés, ne doivent ni entrer ni être omis sans le dire.

`B4-08`
```
ANCIEN: **Épargne** S_R = 1 − Σ_w ($_b + a_w·$_e) / Σ_w ($_b + $_e) ; S_B = 1 − Σ $_b / Σ ($_b + $_e) ;
NOUVEAU: **Épargne** (sommes sur les n_c mondes complets, les mêmes pour tous les bras ; les dollars des mondes non complets sont payés, rapportés à part, hors de S) S_R = 1 − Σ_w ($_b + a_w·$_e) / Σ_w ($_b + $_e) ; S_B = 1 − Σ $_b / Σ ($_b + $_e) ;
```

**B4-09** — Intervalles : « percentile 95 % » pour L / n_c, « rééchantillonnage » sans méthode pour S_R et S_B, « percentiles 2,5 et 97,5 » pour V7 : une seule méthode, dite.

`B4-09`
```
ANCIEN: des mondes (10 000 rééchantillons, percentile 95 %).
NOUVEAU: des mondes (10 000 rééchantillons, bornes aux percentiles 2,5 et 97,5, comme pour V7 ; même méthode pour S_R et S_B).
```

**B4-10** — La ligne κv1 ne mentionne pas l'effort « high » envoyé à `opus55` et `fable52` (bloc gelé et ligne π1 du pilote) ; le lecteur de la ligne ne verrait pas le réglage que la pièce dit « inchangé ».

`B4-10`
```
ANCIEN: proposeurs `opus55` (Pr-2, plafond de session 2 USD, part 40) et `fable52` (Pr-4, 3 USD, part 60), un appel par proposeur et par monde,
NOUVEAU: proposeurs `opus55` (Pr-2, plafond de session 2 USD, part 40) et `fable52` (Pr-4, 3 USD, part 60), effort « high » envoyé aux deux (réglage du bloc gelé), un appel par proposeur et par monde,
```

**B4-11** — « Dollars » : la phrase des prix publics est coupée en deux par l'insertion du prix de Pr-1 du 1er décembre au milieu de la liste « 8 / 40 ; 4 / 20 ; 10 / 50 ; 2 / 10 » ; l'ordre des prix et des proposeurs n'est plus lisible.

`B4-11a`
```
ANCIEN: où le prix de Pr-1 double le 1er décembre : 4 / 20 à partir de cette date, rapporté en sensibilité avec celui de la configuration ; 8 / 40 ; 4 / 20 ; 10 / 50 ; 2 / 10 USD
NOUVEAU: 8 / 40 ; 4 / 20 ; 10 / 50 ; 2 / 10 USD
```

`B4-11b`
```
ANCIEN: par million pour Pr-4, Pr-2, Pr-3, Pr-1 jusqu'au 30 novembre) — **principal**
NOUVEAU: par million pour Pr-4, Pr-2, Pr-3, Pr-1 jusqu'au 30 novembre ; le prix de Pr-1 double le 1er décembre, 4 / 20, rapporté en sensibilité avec celui de la configuration) — **principal**
```

**B4-12** — « Choix et doutes » : R-2977 dit « recommandations de l'auteur sauf mention » ; les points 1, 7, 8 et 10 n'ont aucune recommandation (le format de décision en exige une, avec confiance et défaut), et l'entrée de l'ablation (étage 5) aux critères gelés de (v), ouverte depuis le tour 1, n'est pas un point numéroté. Sans cela, le défaut de 48 heures ne peut pas s'appliquer.

`B4-12a`
```
ANCIEN: points 1, 3, 7, 8, 10 encore ouverts, à trancher avant scellement)
NOUVEAU: points 1, 3, 7, 8, 10 et 10 bis encore ouverts, à trancher avant scellement ; recommandations ajoutées aux points 1, 7, 8, 10 et 10 bis, défaut de 48 heures)
```

`B4-12b`
```
ANCIEN: lignes à ces montants ?
NOUVEAU: lignes à ces montants ? Recommandation : oui (le bloc gelé fait foi ; un plafond plus bas arrêterait le crible) ; confiance 0,8.
```

`B4-12c`
```
ANCIEN: à décider sur la durée du pilote.
NOUVEAU: à décider sur la durée du pilote. Recommandation : appliquer la règle de B_a, de N et de M de la section « Devis » ; M = 2 seulement si l'essai à blanc le tient ; confiance 0,6.
```

`B4-12d`
```
ANCIEN: ≈ 0,10 USD, 8,07 au pire.
NOUVEAU: ≈ 0,10 USD, 8,07 au pire. Recommandation : l'exiger, le lanceur étant neuf ; confiance 0,55.
```

`B4-12e`
```
ANCIEN: (jamais monde par monde) : suffisant ?
NOUVEAU: (jamais monde par monde) : suffisant ? Recommandation : oui ; confiance 0,6.\n10 bis. **Étage 5 (ablation) aux critères gelés de (v)** : N-045 point 3 la dit « rapportée, hors des critères gelés » ; R-2977 ne la fait entrer aux critères gelés que pour (iii). Options : (a) étage 5 rapporté sans verdict, V4 lue sans zone de réfutation (avantage : lettre de N-045 ; inconvénient : la question QO1 du crible perd son verdict) ; (b) étage 5 gelé comme écrit (avantage : QO1 répond ; inconvénient : écart à N-045 point 3). Recommandation : (a) ; confiance 0,6 ; défaut après 48 heures : (a).
```

## Remarques facultatives (aucune n'est exigée)

- **F-1** : V1 (« k_R ≤ 3 sur 20 », réfutation « ≥ 8 »), V3 (« L_R ≥ 4 ») et V5 sont des comptes absolus ; à N = 24 ils ne sont plus à l'échelle (3,6 ; 4,8 ; 9,6). V1 et V6 peuvent être refaits à l'étape 2 ; V3 et V5 ne le peuvent pas : à dire (échelle gardée ou changée) dans le texte qui fera foi.
- **F-2** : puisque le champ du témoin positif du pilote sera lu avant le scellement et que V1 est donnée à 0,65, une règle d'avance de **pertinence** coûterait une ligne : si la part d'appels bon marché du pilote dont une carte va au-delà de K1 est au moins X, k_R ≥ 4 est improbable ; la mère décide alors, avant d'inscrire la ligne « calcul », entre lancer pour l'ablation seule (verdict « H-v non éprouvée au crible » connu d'avance), ajouter le bras à archive enrichie (écart à R-2977) ou ne pas lancer. X est à fixer par programme sur la loi binomiale des mondes, d'avance ; je ne propose pas de valeur sans calcul. Sans cette règle, le choix sera fait après lecture du pilote, mais avant toute lecture du crible : acceptable, non écrit.
- **F-3** : les clés `opus55` et `fable52` sont de fait des noms de modèles ; la pièce le dit (« noms gelés par l'empreinte de la configuration v12 », forme du pilote). Tenu ; à garder identique dans les lignes de GO.
- **F-4** : dans le verdict v67 (V-7, V-8) et les faits du collisionneur (l. 34), la génération 1 de v67 a **11 cartes, toutes retenues** : la liste des retenues de la génération 1 est donc toutes les cartes de la génération 1, et sa lecture n'apprend rien du juge. La partie A pourrait construire l'archive de la génération 2 comme K1 et toutes les cartes de la génération 1, sans lire le champ des retenues, et supprimer l'exception à « sans aucun verdict » de R-2977 (et la ligne d'arrêt qui la porte). Je n'ai pas ouvert le relevé ; à la mère de décider.
- **F-5** : une carte plus **pauvre** que K1 (K1 restreinte à son effet) n'est pas dans le nul engendré par K1 : d_nul(x → K1) est positive, elle n'est pas une copie, et la règle n'appelle pas les chers ; biais du côté « épargne », comme pour les copies par morceaux ; à ajouter aux « Écarts » (la sensibilité « minimum des deux sens » la rapporte déjà en partie).

## Points pour la mère

1. **Sceller telle quelle : non.** Cinq majeures. Les couples ci-dessus sont à faire écrire par le modèle A (R-2982) ; le lecteur du tour 5, s'il y en a un, doit être neuf (ni moi, ni le rédacteur, ni les lecteurs et rédacteurs des tours 1 à 3). Les corrections touchent l'étage 0, la ligne du coût d'un appel, l'étape 2 : ce sont des textes gelés, donc le tour 5 devrait relire ces seuls endroits.
2. **24 mondes** (déjà point 1 du tour 3) : la règle de R-2977 (24 si le taux d'appels répondus du pilote est sous 0,95) revient, sur 16 appels de pilote, à « 20 si aucun appel du pilote n'a échoué » ; à 24 mondes la puissance n'augmente pas (0,787 contre 0,804 à p = 0,26), le coût monte de 20 % (235,32 USD au pire contre 196,60) et la durée devient plus difficile (mon calcul, réponse (4)). **Décision avant scellement** : (a) garder la règle (écart de coût sans gain) ; (b) N = 20 dans tous les cas (écart à R-2977, mot de la mère) ; je recommande (b) ; confiance 0,6.
3. **Le crible éprouve surtout l'ablation, non la règle** (V1 à 0,65, V6 à 0,6). R-2977 a choisi (a) en le sachant. À dire à Lazar en une ligne avec la demande de ligne « calcul », et à décider si F-2 (règle de pertinence) entre dans la pièce.
4. **Étage 5** aux critères gelés de (v) : N-045 point 3 le dit « rapporté, hors des critères gelés » ; R-2977 ne le tranche que pour (iii) ; la pièce l'a gelé « à confirmer ». Défaut proposé à 48 heures : (a) rapporté sans verdict (point 10 bis, B4-12e). Si la mère garde (b), c'est un écart à N-045 à déclarer.
5. **Date de lancement** : fixée par le code neuf, non par le préenregistrement (réponse (4)) ; fenêtre du GO jusqu'au 30 novembre ; le prix public de Pr-1 double le 1er décembre. Risque : si le plus long appel répondu du pilote dépasse environ 1 200 s, le crible ne tient dans 17 h qu'avec M = 2 (huit sessions à la fois, concurrence non éprouvée, code et essai à blanc à M) ; à 24 mondes et B_a au-dessus de 2 400 s, « non lançable ».
6. **Enveloppe des cinq cribles** : (v) est à 196,60 USD au pire (235,32 à 24 mondes) ; l'attendu de la note (73,30) est sous la borne basse de la fourchette de la pièce (79,95 à 92,75 aux prix publics, 106,95 à 125,75 au compte de la configuration, qui est celui de la part). R-2977 compte 413,20 au pire pour (v) et (iii) à 20 mondes ; le compte des cinq (1 275 au pire) est à refaire sur les coûts mesurés avant d'inscrire une ligne.
7. **Partie A et « retenues »** : lire la liste des retenues est lire un résultat du juge, contre la lettre de R-2977 ; la pièce le déclare. Remarque F-4 : la liste est « toutes les cartes de la génération 1 », donc l'exception peut disparaître. À trancher.
8. **R-2977 et les points ouverts** : « recommandations de l'auteur sauf mention » ; B4-12 donne des recommandations aux points 1, 7, 8, 10 pour que le défaut de 48 heures s'applique ; la mère confirme que ce défaut vaut pour les points 1 et 3 (déjà demandé au tour 3, point 4).
9. **Lecteur du pilote** : il ne doit rendre que les comptes d'appels répondus, tronqués et en échec, les durées, les coûts et le seul champ du témoin positif. La pièce fait de V1 et V6 des prédictions **non à l'aveugle** après cette lecture (dit) ; si la mère veut l'inverse, il faut retirer la ligne « Le témoin positif du pilote » des points à remesurer (tour 3, C3-6).
10. **Après correction** : ajouter à « Contre-lecture » une entrée « Contre-lecture 4 » avec l'empreinte entière de ce rapport (lue dans son compagnon `.sha256`) et celle du brouillon 4 relu (`af6e6db3…`), mettre à jour le statut, nommer les couples propres.

## Incidents de ma main

- Aucun fichier écrit hors de ce rapport et de son compagnon d'empreinte, et de programmes de contrôle jetables dans le bloc-notes de ma session (dossier `c4` : contrôle des couples, recomptes, copies de lecture de la procédure v14 et du texte scellé du pilote tirées par `git show`). Aucune pièce existante modifiée.
- `git fetch` par refspec de deux branches (`lot/compte-organisme-v1`, `prep/pilote-mr2-compte-organisme-v1`) : met à jour leurs références distantes locales ; aucun clone.
- `grep` de `registres/decisions.md` : lignes R-2977 et R-2982 seulement affichées ; lignes R-2981, R-2983 et R-2985 **non** affichées ; aucun taux ni coût du pilote lu. Le rapport du tour 3 (lu, comme exigé) cite des comptes de marche du pilote dans ses « Incidents » : je n'en reprends aucun.
- `grep` du verdict v67 (docs, hors `diag/`, `runs/`, `donnees/`) et des faits du collisionneur (l. 34) : lignes sur les retenues et les durées d'appels de v67 affichées ; ces textes sont des pièces de `docs/`, non le relevé ; la ligne de verdict v67 sur une « loi plantée vue par les proposeurs » (touche signalée) s'est affichée à côté : non utilisée.
- Un premier appel du validateur avec le texte au lieu du chemin a échoué (erreur de ma main, sans effet) ; rejoué avec le chemin.
- Pas d'empreinte calculée sur un fichier interdit.
