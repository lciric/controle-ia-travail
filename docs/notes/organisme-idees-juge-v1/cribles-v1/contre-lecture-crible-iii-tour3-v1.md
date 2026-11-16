# Contre-lecture du préenregistrement du crible (iii), brouillon 3 — tour 3 — v1

- Contre-lecteur : sous-agent neuf, **modèle C** (identité dite en conversation seulement) ; auteur de la pièce : modèle A ; je n'ai écrit aucune pièce
  citée, ni les rapports des tours 1 et 2. Le premier contre-lecteur de ce tour (modèle B), arrêté sans rapport : rien lu de lui ni de ses dossiers.
- Date (UTC) : Mon Nov 16 13:53:52 UTC 2026 (`date -u`) à la fin de la lecture ; rapport écrit juste après.
- Pièce relue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon3.md`, empreinte entière
  `bd1aff342bfc8f9842c27b688a354e3a24ea1b9029ae1119f092fc793ad4f7a3` (`sha256sum`, égale à son compagnon).
  Brouillon 2 : `713ea6a7f3c7a2b6a4ae627a6445a9ff06fd4acd3dfedee24fc3fd6630d0bd3d` (égale à son compagnon et à celle citée). Rapport du tour 2 :
  `9a7043b0b1c0a3eaa48262d539861631f7df11cabed264dee8cc21918f14105c` (égale). Programme d'application du brouillon 3 :
  `eee8912f40a43247b653009d2c42cbd9784bab7a3bb25d7139bfbf5d2611d172` (égale à son compagnon ; **non lu** : j'ai refait l'application par mon propre programme).
- Pièces lues : la pièce entière (annexe A en diagonale, inchangée d'après `diff`) ; le rapport du tour 2 entier ; la ligne R-2977 de `registres/decisions.md` (entière) et
  les lignes de ce fichier qui parlent des cribles (par `grep`, tronquées) ; la ligne GO-2026-11-15-06 de `registres/go.md` ; la procédure v14 (`git show` au commit `2d35cafa…`
  après un `git fetch` avec refspec ; empreinte `2035562740efe1e8…` vérifiée) et le texte scellé du pilote (candidat 6, `8aa33014667d…`, branche locale, `git show`) pour leurs relais et leurs
  gardes ; empreintes des documents cités recalculées. **Non lu** : tout ce que la consigne interdit, dont la sortie du pilote MR-2 v14.

## Verdict

**corrections.** Les 16 couples du tour 2 sont appliqués **à la lettre** et le différentiel ne contient rien d'autre que ce que la pièce déclare. La conception tient. Mais la pièce ne peut pas
être scellée telle quelle : **1 correction majeure** (la forme du crible peut encore être décidée après la lecture du pilote, alors que la forme fixe les deux relais dont le taux fixe N : porte de sortie
après lecture, R1) et **5 mineures**. Recommandation nette sur la forme : **la variante** (confiance 0,65). La pièce reste de toute façon non scellable tant que la forme n'est pas inscrite, et, si la variante est
retenue, un tour de plus est nécessaire (réécriture, voir section 5).

## 1. Les corrections du tour 2 sont-elles appliquées fidèlement ?

**Méthode.** J'ai extrait moi-même les 16 couples « ancien → nouveau » de la section 3 du rapport du tour 2 (32 blocs ; programme à bibliothèque standard, dans mon dossier du bloc-notes), vérifié que chaque
« ancien » figure **une seule fois** dans le brouillon 2, les ai appliqués, puis comparé le résultat au brouillon 3 par `diff`.

**Résultat** : le brouillon 3 est égal à « brouillon 2 + 16 couples » **sauf quatre endroits**, tous déclarés par la pièce (« Rien d'autre que les 16 couples, l'en-tête et la section Contre-lecture ne change ») :

1. titre (« brouillon 3 ») et nouvelle puce d'en-tête « Brouillon 3 » ;
2. ligne « Statut » (contre-lu deux fois ; **non scellable** tant que la forme n'est pas tranchée et inscrite) : plus ferme que le brouillon 2 mais conforme à D-03 ; reste dans « l'en-tête » ;
3. ligne « Validateur » (« aucun défaut sur ce brouillon 3 ») : **vraie**, `controle_ia.prereg.problemes` rejoué sur le brouillon 3 rend `[]` ;
4. section « Contre-lecture » : nouvelle puce « Contre-lecture 2 » (empreintes entières du brouillon 2 et du rapport, **exactes** ; verdict « 3 majeures, 11 mineures » **exact** ; traitement des 14 points D-01 à D-14,
   de D-02 et D-12 en deux couples chacun) et paragraphe « Tour suivant » mis à jour (liste de fichiers à donner : complète).

Aucun autre octet ne diffère ; l'annexe A est identique. Le traitement de D-03 (aucune décision inscrite ; ajouts « Si la variante est retenue » non appliqués) est fidèle au rapport.

**Passages touchés relus et vérifications refaites.**
- D-01 : à cinq files, jusqu'à 15 sessions de Pr-2 (S, H, D) et 5 de Pr-1 (une par monde : passe 1, puis B) ; à six files 18 et 6 : **exact** d'après l'ordre dans un monde (S, passe 1, H ensemble ; D et B à la réponse de la passe 1).
- D-02 : la ligne « mondes, appels, files » est cohérente (N − 15 mondes incomplets = 5 à 20, 9 à 24 ; 100 appels = 5N ; 60 et 40 = 3N et 2N). Voir E-03 : la liste « trois valeurs calculées » n'est pas close.
- D-07 : test des signes au niveau unilatéral 0,0125 : seuils exacts recomptés (n = 20 : 16 ; 21 : 17 ; 22 : 17 ; 23 : 18 ; **24 : 18**, P = 0,0113) : **exact**.
- D-09 : 4 × 7 200 s + 2 h = 10 h, sous les 17 h ; remplace bien les 12 h 30 de la procédure v14 (4 × 10 800 s + 30 min) ; la liste d'arrêt dit la même chose (« pire cas des files restantes + 2 h »).
- D-10 : r modulo F ; 20 mondes sur 5 files et 24 sur 6 : quatre mondes par file dans les deux cas ; fixée avant tout appel : **cohérent**.
- D-11 : 0,9961 → 0,996 ; **les autres probabilités du minimum recomptées** : 0,5149 et 0,9276 ; 0,8586 et 0,9961 ; 0,2249 et 0,7091 ; 0,0427 et 0,2943 : justes.
- D-12 : seuils absolus 14 et 10, dits ; cohérents avec la ligne de la table de mise à jour.
- D-08 : voir remarque facultative 1.
- Devis recompté : forme fidèle 60 × 0,80 + 40 × 0,25 + 0,30 = 58,30 ; au pire 60 × 2,00 + 40 × 2,34 + 3,00 = 216,60 ; variante 60 × 1,60 + 40 × 0,80 + 0,30 = 128,30 ; au pire 60 × 3,00 + 40 × 2,00 + 3,00 = 263,00 ;
  à 24 mondes (72 × 2,00 + 48 × 2,34 + 3,00) 259,32 : **justes** ; lignes de GO (120 ; 93,60 + 3,00 = 96,60 ; sonde 6,68 = 2,34 + 2,00 + 2,34) : justes.
- Empreintes citées (quinze documents de la liste et les quatre PDF) recalculées : **conformes**.

## 2. Réponses aux neuf points

**(1) R1.** Éléments tous présents (hypothèses, prédictions chiffrées et signe, métrique, seuils, plan, critères gelés étages 0 à 7, liste d'arrêt). **Portes de sortie restantes après lecture** : (a) la forme du crible « à trancher avant le scellement »
alors que le scellement vient **après** la lecture du taux du pilote, taux qui dépend de la forme (E-01, majeure) ; (b) le gel de III-6 « confirmé avant le scellement » : même défaut, plus faible (E-02) ; (c) la liste des valeurs calculées avant le scellement n'est pas close (E-03) ;
(d) la décision « nœud de la mère » de la table de mise à jour sur la borne par appel n'est pas bornée (E-06).

**(2) R3.** Statistique Δ_R = R_D − R_S, marge de 0,5 composante, égalités par l'ordre des noms : justifiées avant toute donnée (relu, inchangé depuis le tour 2). Puissance de P2 à l'effet prédit (+ 0,5 ; écart-type 1,0 à 1,2 ; seuil de la normale 2,24 pour une borne à 97,5 %) :
**refaite par moi** : 0,50 à 0,35 : confirmé. Le bras B qui réemploie la passe 1 : comparable à D sans fuite (texte servi égal à l'octet, ligne d'arrêt et artefact ; B est une session neuve ; la réponse brute de la passe 1 ne passe jamais ; coût de la passe 1 compté dans D **et** dans B) ; la dépendance entre B et D est dite. Aucun défaut.

**(3) Forme du crible et crédits de Claude — recommandation nette : la variante (le proposeur de la gamme moyenne choisit, celui de la gamme haute écrit ; le seul appel du haut sert de standard), confiance 0,65.**

Raisons, dans l'ordre.
- **Elle répond à la question de la note** : choisir les traits à moindre prix puis écrire la loi plus cher couvre-t-il plus par dollar qu'un appel du plus cher seul ; la passe chère est-elle nécessaire ? C'est une question de **palier de prix** au sein d'un rôle ; la variante la garde intacte,
  avec un écart de prix par jeton de 2 aux deux barèmes (4 / 20 contre 8 / 40).
- **La forme fidèle est fragile sur sa propre prémisse** : son « bon marché » (Pr-1 à 2 / 10) n'existe qu'au barème public offert **jusqu'au 30 novembre**, jour de fin de la ligne de GO ; au prix de la configuration (10 / 50) Pr-1 est **plus cher** que Pr-2 (4 / 20), et le devis de la pièce
  lui-même donne un écart d'écriture d'environ 2, non 3,2. La variante tient aux deux barèmes.
- **Consigne permanente de Lazar (crédits de Claude au maximum)** : variante : 125,30 sur 128,30 attendus sur crédits (98 %), et 3,00 hors crédits au pire (la machine) ; forme fidèle : 48,00 sur 58,30 (82 %) et 96,60 hors crédits au pire. La variante est la seule qui obéit à la consigne **et** à R-2977 (« celle qui répond à la question en mettant le plus possible sur crédits »).
- **Le pilote a exercé les trois relais utiles** : il a quatre proposeurs et quatre appels par relais ; la règle « taux de réussite par appel » de N est donc calculable aussi bien pour la paire de la variante que pour celle de la forme fidèle.
- **Coût de la variante** : + 70 USD attendus (+ 84 à 24 mondes), 263 contre 216,60 au pire (315 à 24 mondes) ; avec (v) : 196,60 + 263 = 459,60 sur l'enveloppe de 1 275. Dans l'enveloppe.

**La variante change-t-elle la question ? Oui, et la pièce doit le dire** : la question QO1 passe de « la frontière (un proposeur d'une autre maison, bon marché) est-elle nécessaire à l'écriture ? » à « le palier supérieur de la **même maison** est-il nécessaire à l'écriture ? ». La variante ne mesure plus un proposeur bon
marché d'une autre maison (ni un instrument local), et deux modèles d'une même maison peuvent converger (D proche de H) : cela ne touche pas à la validité. La lecture déplacée est celle de N-045 point 1 (modèle par rôle) : « un palier de moins par rôle ». La forme fidèle reste la seule à mesurer un moins cher d'une autre
maison ; si la mère la veut, à proposer **à part**, plus tard, sur devis propre, hors du barème promotionnel.

**Contre-arguments à connaître** : (i) la variante exige une réécriture (section 5) et un tour de plus ; (ii) les 263 USD au pire (315 à 24 mondes) sur crédits supposent un solde de crédits que je ne lis pas ; (iii) la borne de sortie du proposeur du haut (64 000 jetons) est **plus basse** que celle du palier moyen (89 000) : le risque de tronquage se déplace
sur l'écrivain cher (D, et S qui écrit six cartes seul), donc la réserve « B tronqué » devient « D et S tronqués » : à réécrire (section 5).

**(4) Devis.** Recompté (voir section 1) : 100 appels = 5 × 20 (60 de Pr-2 ; 40 de Pr-1) ; plafonds de session de la table (2,00 ; 2,34 ; relus dans le bloc gelé du pilote : 3 ; 2 ; 2,34 ; 2,34) ; attendu et pire cas justes ; sonde recommandée des deux gabarits neufs : 3 appels, 2,34 + 2,00 + 2,34 = 6,68 (2,00 sur crédits, 4,68 hors) ; au prix public attendu 1,05 à 1,40 ;
cohérence avec GO-2026-11-15-06 : une ligne « calcul » par crible sur devis refait et contre-lu, parts séparées, enveloppe de 1 275, échéance du 30 novembre, « essayé, non adopté » : respectée. **Réserve de calendrier** : la fin du 30 novembre est à deux semaines ; la chaîne lecture du pilote, N, simulations, code neuf, contre-lecture du code, addendum,
essai à blanc, machine (10 h au pire) tient, mais sans marge si un tour de réécriture de plus s'ajoute (variante).

**(5) Durée.** La pièce fixe : borne par appel 3 000 s, par monde 7 200 s (deux tours), cinq files de quatre mondes (six pour 24), affectation r modulo F, pire cas d'une file 8 h, garde de départ 10 h sous 17 h, essai à blanc à cinq files avec arrêt avant tout appel si les relais refusent la concurrence : **cohérent**.
**Réponse nette : il faut une configuration et un code neufs** (lanceur à files parallèles et à deux tours dépendants, gabarits, filtre, mesure, procédure de machine, essai à blanc) : le lanceur v74 du pilote est séquentiel et ne sert pas tel quel ; environ deux jours d'agents ; **la concurrence (15 à 18 sessions d'un même relais) n'a jamais été éprouvée**. La pièce le dit.

**(6) Liste d'arrêt, R5, graines.** Chaque ligne a son essai sain et son artefact (y compris les trois lignes du tour 1 et la ligne modifiée). Graines : `numpy.random.SeedSequence(entropy=racine, spawn_key=…)`, clés `(r, 40)`, `(12, r, t)`, `(99, b)`, `(97, k)` : sans collision pour r ≤ 23 (donc à 24 mondes). Minimum de 16 mondes complets sur N : règle présente,
probabilités justes, ligne d'arrêt « complets + non commencés < 16 » bien formée, artefact lu avec « N − 15 ». Seul défaut : la simulation de puissance annoncée n'a ni programme ni graines nommés (E-04).

**(7) Ablation de la frontière aux critères gelés.** Bien définie (B = écrivain bon marché sur les mêmes ensembles, même G2 à l'octet ; étage 5 ; réserve « B tronqué » et phrase interdite sous cette réserve). **Ne contredit pas N-045 point 3 hors du crible** : la pièce l'écrit (les courses restent « rapportées, hors des critères gelés » ; aucune course n'hérite du choix ; à dire à Lazar). Rien à corriger.
Sous la variante, « la frontière » devient « le palier supérieur » : à reformuler (section 5).

**(8) R7, R8.** Aucun chiffre de l'état de l'art non vérifié ; antériorités (LLM-Select, LLM-SR, plan de focalisations, FunSearch, AlphaEvolve, sélection la plus éloignée d'abord, Co-Scientist, CADS) marquées « à chercher » ou « à vérifier » ; « filtre déterministe sans juge » marqué zone séduisante à vérifier plus durement ; « aucune revendication ». Les empreintes des quatre PDF de la rubrique « Citations obligatoires » sont conformes ; je n'ai **pas** vérifié les numéros de pages de la citation de Co-Scientist (hors périmètre d'un chiffre).

**(9) Validateur, identifiants, empreintes.** `controle_ia.prereg.problemes` : `[]`. Identifiants de modèle : aucun nom de modèle ; la pièce emploie trois **clés de configuration** que le bloc gelé et les lignes de GO exigent (R-2690), déclarées comme telles : accepté, comme aux tours précédents. Empreintes : conformes (voir en tête).

## 3. Corrections exigées : ancien → nouveau

Chaque « ancien » figure **une seule fois** dans le brouillon 3 (vérifié par programme ; espaces et retours à la ligne du fichier). Majeure : E-01 (deux couples) ; mineures : E-02 à E-06.

### E-01 (majeure) — la forme du crible doit être fixée avant toute lecture du pilote (deux couples)

La forme fixe les deux relais « employés ici », dont le taux de réussite par appel fixe N (24 si sous 0,95) : décidée après lecture du pilote, elle s'ouvrirait selon les taux. Le gel de la forme, comme celui de III-6, doit précéder la lecture.

Ancien :

````
**À trancher par la mère avant le scellement** (R-2977 le confiait au contre-lecteur ;
````

Nouveau :

````
**À trancher par la mère avant toute lecture de l'issue du pilote** (la forme fixe les deux relais dont le taux de réussite fixe N : décidée après la lecture, elle s'ouvrirait selon les taux ; R-2977 le confiait au contre-lecteur ;
````

Ancien :

````
décision et date à inscrire ici
````

Nouveau :

````
décision, date et heure (`date -u`) à inscrire ici et dans `registres/decisions.md`, avant la lecture de l'issue du pilote
````

### E-02 (mineure) — gel de III-6 : une trace datée avant la lecture

Ancien :

````
la mère le confirme avant le scellement, jamais après lecture du pilote
````

Nouveau :

````
la mère le confirme par une ligne de `registres/decisions.md`, datée à l'heure (`date -u`), avant que le lecteur neuf du pilote rende sa lecture, jamais après
````

### E-03 (mineure) — la liste des valeurs calculées avant le scellement n'est pas close (deux couples)

Le correctif D-07 prescrit une quatrième valeur calculée avant le scellement (seuils exacts du test des signes à n = 21 à 24) que la clause « trois valeurs » ne nomme pas.

Ancien :

````
**hors** trois valeurs calculées
````

Nouveau :

````
**hors** quatre valeurs calculées
````

Ancien :

````
de P2 et le taux d'erreur de l'intervalle par percentile à N mondes (section « Taille »).
````

Nouveau :

````
de P2, le taux d'erreur de l'intervalle par percentile à N mondes (section « Taille ») et les seuils exacts du test des signes à n = 21 à 24 (annexe A, point 2 étendu).
````

### E-04 (mineure) — la simulation de puissance : programme et graines (R1, R9)

Ancien :

````
[MR2] et la partie A, quand la machine n'est plus chargée ; 24 mondes
````

Nouveau :

````
[MR2] et la partie A (programme sous un nom neuf, scellé avant son lancement ; graines `(96, s)` de `numpy.random.SeedSequence`, 10 000 tirages par cellule ; cellules : 20 et 24 mondes, effet nul puis effet prédit ; aucune donnée de crible), quand la machine n'est plus chargée ; 24 mondes
````

### E-05 (mineure) — III-5 : seule la part de H après filtre est calculable avant le crible

La part de D après filtre dépend des réponses de la passe 1 ; elle ne peut pas être « calculée sur les 12 mondes de développement (processeur) ».

Ancien :

````
la part **après** filtre est calculée sur les 12 mondes de développement (processeur) avant le scellement et recopiée ici
````

Nouveau :

````
la part de H **après** filtre (seule calculable sans réponse de proposeur) est calculée sur les 12 mondes de développement (processeur) avant le scellement et recopiée ici ; N_D ≤ 0,25 reste la prédiction pour D
````

### E-06 (mineure) — le nœud de la mère sur la borne par appel doit être borné

Ancien :

````
nœud de la mère avant le scellement (borne par appel probablement trop courte) |
````

Nouveau :

````
nœud de la mère avant le scellement (borne par appel probablement trop courte) ; seule décision permise : relever la borne par appel à 2 × l'appel le plus long du pilote, sans dépasser 3 600 s (deux tours en série doivent tenir dans 7 200 s) ; ni la borne de 7 200 s par monde ni la garde de départ ne changent ; décision datée avant le scellement |
````

## 4. Remarques facultatives (aucune correction exigée)

1. Ligne « limite de débit » : avec « plus de 5 % des appels d'un fournisseur, une fois au moins dix de ses appels faits », **une seule erreur** parmi les dix à dix-neuf premiers appels d'un fournisseur arrête le crible (1 sur 10 = 10 %), alors qu'une erreur au vingtième appel ne l'arrête pas (5 %, non « plus de 5 % ») : règle claire mais dépendante du moment ; elle est du côté sûr (arrêt, nœud de la mère) ; choix à connaître plutôt qu'à changer.
2. La ligne « Témoin commun » du devis (écartée, chiffres encore écrits) et les renvois à [CRIBLE-V] (brouillon non scellé : « Composantes comptées », « Hypothèses de coût », « Plafond de 0,75 ») : restes déjà signalés ; à supprimer ou à recopier dans la version qui fera foi.
3. La part de H après filtre (E-05) peut aussi servir de contrôle de la règle de Jaccard : si elle monte, le filtre éloigne du bruit sans proposeur.
4. Statut de l'en-tête : « contre-lu deux fois » devient « trois fois » au prochain brouillon.

## 5. Si la variante est retenue : ajouts à la liste du tour 2 (section 5 de son rapport), qui reste valable

1. **Tronquage asymétrique** : le proposeur du haut a la borne de sortie la plus basse (64 000, contre 89 000) et écrit à la fois S (six cartes seul) et D : réserve « B tronqué » → réserves « S tronqué » et « D tronqué » (trois appels ou plus au-dessus de la borne), phrase « perte établie sans le palier supérieur » interdite sous ces réserves ; sonde obligatoire si le plus grand appel du proposeur du haut dépasse 80 % de sa borne.
2. **Concurrence** : celle de la liste du tour 2 (15 sessions du proposeur du haut à cinq files, 18 à six ; 5 et 6 du palier moyen) ; l'essai à blanc la reprend.
3. **Taux de réussite par appel** : prendre ceux du **palier moyen et du proposeur du haut** (quatre appels chacun au pilote) : réécrire « des deux relais employés ici ».
4. **Lignes de GO** : κiii1 (les deux sur crédits, 260 USD ; à 24 mondes 312), κiii2 (machine seule, 3 USD) ; sonde : 7,00 sur crédits.
5. **Libellés** : « la frontière » → « le palier supérieur de la même maison » ; QO1 reformulée en tête ; la « Lecture de H-iii » dit qu'aucun proposeur d'une autre maison n'est mesuré ; étage 4 : le qualificatif « dépend du barème » devient sans objet (rapport de prix de 2 aux deux barèmes) ; sensibilité « prix de la configuration » vide.
6. **Calendrier** : tour de contre-lecture de la version réécrite, puis du code ; à poser avant le 30 novembre.

## 6. Points pour la mère (à trancher ou à savoir)

1. **Forme** : décider **avant toute lecture de l'issue du pilote** (E-01) ; ma recommandation : la variante, confiance 0,65 ; R-2977 confiait ce choix au contre-lecteur : si tu le tiens pour tranché par ce rapport, inscris-le (date et heure) et la pièce se réécrit ; vérifier le **solde de crédits de Claude** pour 263 USD au pire (315 à 24 mondes).
2. **Gel de III-6** : inscrire aussi avant la lecture (E-02). La lecture du pilote par un lecteur neuf est en cours ou à venir : l'ordre prime.
3. **N** : avec huit appels pour les deux relais, « sous 0,95 » revient à « au moindre échec » (un échec sur huit donne 0,875) ; 24 mondes sans condition coûterait + 20 % (environ + 12 USD attendus en forme fidèle, + 26 en variante) et supprimerait la bifurcation ; décision de la mère.
4. **Seuils absolus** (14 et 10) ou proportionnels (17 et 12 à 24 mondes) : à écrire avant le scellement.
5. **Écart à un texte** : N-045 point 3 (ablation hors critères gelés) mise aux critères gelés du crible par R-2977 ; non violé à la lettre, à dire à Lazar avec le nœud d'adoption.
6. **Prix promotionnel** de Pr-1 jusqu'au 30 novembre : un crible en forme fidèle qui déborderait changerait de question.
7. **Risque** : « non tranché » est l'issue la plus probable de P2 (puissance 0,35 à 0,50) même si III-2 est vraie ; ne pas le lire comme une absence d'effet. Code neuf (environ deux jours d'agents), concurrence jamais éprouvée.

## Incidents (de ma main)

- J'ai écrit dans mon propre dossier du bloc-notes (`…/scratchpad/c4`) trois petits programmes à bibliothèque standard (application des couples du tour 2, unicité des « ancien », comptes binomiaux et seuils du test des signes) et deux extraits de `git show` (procédure v14, texte du pilote) ; `python3 -I` ; quelques millisecondes ; aucun calcul lourd ; ni `pytest`.
- Un `git fetch` avec refspec (`lot/compte-organisme-v1`) : il a mis à jour la référence de suivi locale `origin/lot/compte-organisme-v1` (aucun fichier de travail touché) ; `git show` du texte du pilote sur la branche locale `origin/prep/pilote-mr2-compte-organisme-v1`, sans fetch ; aucun clone.
- `controle_ia.prereg.problemes` rejoué par `PYTHONPATH=src` et `.venv/bin/python` (lecture seule) ; `pdftotext` sur la première page du PDF de Co-Scientist (lecture seule).
- Je n'ai lu aucun dossier d'un autre agent du bloc-notes ; rien sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7, P3-bis, bras d'attaque ; rien de la sortie du pilote ; ni `env` ni `printenv` ; aucune clé lue ; aucun appel de modèle ; aucune dépense ; aucun fichier existant modifié ; aucun commit.
