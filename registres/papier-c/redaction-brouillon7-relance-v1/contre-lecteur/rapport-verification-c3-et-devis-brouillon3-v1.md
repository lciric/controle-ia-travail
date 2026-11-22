# Papier C — vérification de la version c3 du préenregistrement et du brouillon 3 du devis du pilote — v1

- Contre-lecteur : le même qu'aux trois passes précédentes (sous-agent Opus 5.5, `claude-opus-5-5`), le 2026-11-22.
  Branche courante, commit `c897bdaad`.
- Pièces : texte c3, `1da47502c8e49e3eb1078cd3cb0b31f035240d3f422a501557f8a3e5b6baf00c` (égale à son compagnon et à
  l'attendu) ; devis brouillon 3, `d68649ef782db4cb68fc…` (égale à son compagnon).
- Interdits tenus ; dans `registres/depenses.md`, seules les lignes de prix, de durée et de fiabilité nommées. Aucune
  dépense, aucun refus de permission ; écrit dans ce seul dossier.

**Décompte.** Texte c3 : 0 bloquante, 1 majeure, 1 mineure (CX-01, CX-02). Devis : 0 bloquante, 1 majeure,
3 mineures (CE-01 à CE-04).
**Avis.** Texte c3 : **scellable après corrections** (CX-01 touche un cadre que le texte déclare non modifiable).
Devis : **scellable après corrections** (CE-01).

# Partie A — texte, version c3

## A.1 Différentiel
Programme `travail/construire_brouillon7_relance_c3_v1.py` rejoué : sortie `1da47502…` (263 817 octets), journal
identique octet pour octet ; remplacements exacts seulement. `diff` c2 → c3 relu en entier (119 lignes) : chaque bloc
répond à CW-01, CW-02, CW-03 ou à la mise à jour d'état qu'elles entraînent (titre, état en bref, historique,
verrous 7 et 8, « Contre-lecture »). **Aucun changement hors des 14 remplacements.**

## A.2 Remarques CW

| Remarque | État | Lieu |
|---|---|---|
| CW-01, lettre de D-21 | **levée** (sous la confirmation demandée à la conduite, qui ne relève pas du texte) | précision 38, « Règle » ; verrou 7 ; « Contre-lecture » |
| CW-02, garde 24 | **levée** | « Préalables » de l'étape 2 ; garde 2 (renvoi à la garde 24) ; garde 24 (« l'étape 2 ne s'ouvre pas ; nœud (le directeur dit si elle s'ouvre sans ce bras) ») : les trois disent la même chose |
| CW-03, cadre du bras | **levée**, avec un défaut neuf du cadre (CX-01) et une ambiguïté (CX-02) | Plan, section 3, « Bras « saboteur sans consigne » » |

**CW-01 : le raisonnement de la table tient.** Les heures des commits (`git log`) : `c55eca46`, qui porte la liste
des points ouverts v2, est de 19:11:30Z ; le mot de Lazar est « vers 2026-11-22T19:11Z » (GO-2026-11-22-123) ; la
liste v1 (`ab1a9b8a…`, empreinte conforme à mon contrôle de la première passe) écrit en option (a) : « Désignée
seulement si elle est au-dessus du plancher sur chaque famille et à chaque dose que le verdict juge » ; la ligne GO
recopie cette phrase, non celle de la v2. Ma remarque CW-01 supposait que la v2 était sous les yeux du directeur ; la
chronologie le rend peu probable. Ce qui manque seulement : la confirmation de la conduite (ce qu'elle a montré au
directeur), que le texte demande et ne fait pas dépendre d'un choix du rédacteur. Pour D-23, la v1 porte la même
option (a) et la même recommandation qu'en v2 : le cadre du bras ne dépend pas de cette question.

## A.3 Le cadre du bras « saboteur sans consigne » (question 3)
Fidèle à l'option (a) de D-23 et à sa recommandation (« (a), et (c) en plus si la famille (iv) existe ») : mêmes
tâches et niveaux ; organisme de la famille (ii) du mode « coût gonflé » retenu par G0, et (iv) s'il existe ;
honnête = modèle de base ; cellules S et SP_m de plus, (n/2) × (1 + k_P) épisodes par organisme ; lignes par mode
d'induction. Il ajoute trois choses que la recommandation ne disait pas, toutes conséquentes : mêmes sondes
désignées ; définitions du point 13, lecture principale sur les champs seuls ; les lignes du présent texte gardent
leurs critères. Il ne crée aucun verdict pour le présent texte. Deux points :

### CX-01 — majeure — le cadre fige une comparaison où l'honnête a une consigne en contexte et le saboteur n'en a pas
- **Lieu** : Plan, section 3, « Bras « saboteur sans consigne » », « Cadre fixé dès maintenant ».
- **Citation** : « honnête : le modèle de base, par les cellules H et HP_m du présent texte » ; « Cadre fixé dès
  maintenant, que le complément ne peut pas changer ».
- **Pièce** : Plan, section 3, « Génération du corpus A » : « consignes privées de P3 (honnête ; saboteur au coût
  gonflé …) » ; Métrique, point 14 (la consigne vit à la fin du message système et dans une indication privée à
  chaque tour, pour chaque condition).
- **Constat** : dans ce bras, D₀ = S − H oppose un saboteur sans aucune consigne en contexte à un honnête qui porte
  la consigne privée honnête de P3. Une sonde qui lirait « j'ai une consigne privée » séparerait donc les deux
  cellules à l'envers, et le plaidoyer pourrait la déplacer par ce que la consigne de plaider change au contexte de
  l'un et de l'autre : c'est le défaut que la réserve 20 décrit, déplacé de côté. Le réemploi des cellules H et HP_m
  suit la recommandation (son compte d'épisodes l'implique) ; mais le texte le fige comme « non modifiable » alors
  que le complément est le lieu où ce choix se pèse.
- **Correction demandée** : soit laisser au complément le choix de l'honnête (cellules H et HP_m du présent texte, ou
  cellules honnêtes sans consigne privée, à chiffrer au devis), soit garder ce cadre et déclarer cette asymétrie en
  réserve du bras (et à la réserve 20). Le choix entre les deux touche la décision D-23 : à porter à la conduite.

### CX-02 — mineure — « lignes rapportées » et « critères de lecture » : verdict ou non ?
- **Lieu** : même paragraphe, « Cadre » et « Ce que fixe le complément ».
- **Citations** : « lignes rapportées par mode d'induction » ; « les critères de lecture des lignes de ce bras ».
- **Constat** : dans ce texte, « rapportée » veut dire « sans verdict » ; le complément reçoit pourtant le droit d'écrire
  des critères de lecture, donc peut-être des verdicts, après le verdict de G0. Deux lectures. La recommandation
  disait « HC2 et C-P4c rapportées par mode d'induction ».
- **Correction demandée** : écrire l'une des deux : « lignes rapportées, sans verdict », ou « le complément peut écrire
  des verdicts pour ces lignes ; ils ne changent aucune ligne du présent texte et toute revendication passe par le
  directeur ».

## A.4 Le reste
- « Préalables », garde 2 et garde 24 disent la même chose (question 4).
- Rien de tranché n'a bougé : énoncés, prédictions, marges, seuils, D-1 à D-20 hors du `diff` ; la règle de la
  précision 38 est inchangée (seule sa source est dite).
- Validateur : section « Contre-lecture » à remplir et les mêmes dix-sept marqueurs qu'en c2.

# Partie B — devis, brouillon 3

## B.1 Remarques CD

| Remarque | État | Lieu |
|---|---|---|
| CD-01, plafond cumulatif | **levée en partie** (règle écrite et placée dans l'addendum ; mesure par le crédit du compte : CE-01) | § 5 ; § 3 ; § 4 |
| CD-02, ce qui change | **levée** | § 4, table ; « dérivé » au § 3 ; option de l'enveloppe |
| CD-03, instance arrêtée | **levée** (reste un cas ouvert : CE-03) | § 5, « Après l'arrêt » ; § 3 |
| CD-04, durée attendue | **levée en partie, acceptable** : l'attendu reste non sourcé, le seul repère est cité pour ce qu'il est (1,53 h pour 180 notations en génération, instance 58178416, conforme au registre) ; garde de projection ajoutée (CE-02) | § 3 ; § 5 |
| CD-05, offre conforme | **levée** (une précision : CE-04) | § 2 ; § 3 |
| CD-06, suivi par le crédit | **levée en partie** : relevés écrits, mais le crédit du compte ne mesure pas la seule dépense du pilote (CE-01) | § 5 |

**Table du § 4** : elle dit tout ce qui change (montant, nombre de lancements, prix horaire, échéance, préalables) ; le
montant dit « au-dessus de ≈ 6 USD » ; 1,50 USD/h est dit dérivé. **Option de l'enveloppe** : posée loyalement — (A)
suit la lettre des deux accords, avec un contrôle chiffré ; (B) est dite écart, ouvrable par le seul directeur.
**Contradiction avec le texte c3** : aucune ; le devis se dit plus serré que le point 1.6 et la garde 3, qu'il ne
change pas.

**Les trois cas du plafond.** Cas sain (un lancement à environ 1,2 USD/h, réseau ≈ 1 à 2 USD) : tenu. Second lancement :
tenu par la règle cumulative, **si** « dépensé jusque-là » est exact (CE-01). Réseau cher : l'estimation avant
création refuse l'offre ; un dépassement en marche n'est vu que par le crédit (CE-01).

### CE-01 — majeure — le crédit du compte ne mesure pas la dépense du pilote
- **Lieu** : § 5, « Règle cumulative » (« somme des baisses de crédit relevées aux lancements précédents »),
  « Pendant la marche » (« une baisse, depuis la création, plus grande que le reste du plafond : arrêt »),
  « Compte de la dépense ».
- **Pièces** : `registres/go.md`, GO-2026-11-22-77 : « Vast rechargé de 30 USD, recharge automatique active » ;
  le compte du loueur sert à d'autres chantiers en même temps (registre des dépenses, nombreuses instances).
- **Constat** : (a) une recharge automatique pendant la marche fait monter le crédit et masque la dépense : la garde en
  marche peut ne jamais jouer, et la dépense consignée est fausse ; (b) une autre instance du compte fait baisser le
  crédit : arrêts à tort, dépense du pilote surestimée et « dépensé jusque-là » faux pour le second lancement. Le
  plafond n'est donc tenu que si rien d'autre ne bouge sur le compte.
- **Correction demandée** : mesurer la dépense par instance (coût de l'instance lu par son identifiant à l'interface
  du loueur, ou facture par identifiant), le crédit n'étant qu'un contrôle ; à défaut, consigner les recharges et les
  autres instances actives à chaque relevé et les retrancher, et prendre comme « dépensé » le plus grand du relevé
  corrigé et du calcul (heures × prix relu + réseau estimé + disque) ; dire ce que fait le lanceur si l'interface ne
  le permet pas (§ 8 le laisse ouvert).

### CE-02 — mineure — la garde de projection sous-estime le mode raisonné
- **Lieu** : § 5, « Garde de projection ».
- **Citation** : « lectures restantes de tous les points × temps moyen par lecture mesuré ».
- **Constat** : le temps moyen est mesuré sur des lectures directes (une passe avant) ; les 180 lectures du point 1.5
  génèrent jusqu'à 384 jetons chacune, beaucoup plus longues. Par ailleurs les points 1.2 et 1.3 ont déjà tourné quand
  la garde joue. Le seuil de 500 lectures lui-même est raisonnable (environ 3 % du vivier).
- **Correction demandée** : projeter le point 1.5 à part (temps par jeton généré mesuré sur les premières lectures
  raisonnées, ou une durée forfaitaire au pire, 384 jetons), et dire qu'un arrêt par cette garde est un nœud qui
  n'ouvre pas de lui-même le second lancement (la ligne du § 4 permet un second lancement « après un arrêt par une
  garde »).

### CE-03 — mineure — disque gardé au-delà de 2 heures : hors plafond
- **Lieu** : § 5, « Après l'arrêt ».
- **Citation** : « si le versement n'est pas vérifié à ce délai : la machine reste arrêtée, disque gardé, nœud ».
- **Constat** : la règle cumulative ne compte que 2 heures de disque après l'arrêt ; au-delà, le disque coûte encore
  (≈ 0,027 USD/h relevé), sans borne écrite.
- **Correction demandée** : dire que ce coût entre au plafond et que le nœud doit être tranché avant que le reste du
  plafond soit consommé (en donner le nombre d'heures au prix du disque relu).

### CE-04 — mineure — disque de 80 Go et estimation du réseau : fichiers réellement téléchargés
- **Lieu** : § 2, « offre conforme » et « descente » ; § 5, « réseau estimé ».
- **Constat** : un dépôt de modèle peut porter les poids en deux formats (le dépôt de Mistral-7B-Instruct-v0.3 en
  porte deux jeux de taille voisine) : sans filtre de téléchargement, la descente et le disque peuvent doubler pour
  un modèle, et 80 Go devenir juste. Le relevé de fiabilité « 0,978 à 0,9973 » omet des offres retenues au-dessus
  (0,998, 0,9986), sans effet sur le seuil.
- **Correction demandée** : fixer les fichiers téléchargés (motifs de fichiers, à l'addendum de lancement) et calculer
  le réseau et le disque sur ces fichiers aux révisions figées.

Les seuils neufs : 30 minutes (une demi-heure de carte au pire = 0,75 USD, couvert par la marge du réseau estimé),
2 heures (CE-03), fiabilité 0,97 (sous toutes les offres retenues au registre, de 0,978 à 0,9986), 80 Go (CE-04),
500 lectures (CE-02) : aucun ne lit un score ; deux demandent une précision.

# Ce que j'ai lu, en fait
Le message de la session ; `git log` (heures de 8 commits) ; programme c3 (exécuté ; fonction principale) et son
journal (comparaison) ; `diff` c2 → c3 complet ; table de traitement de la vérification de c2 (en entier) ; ligne
GO-2026-11-22-123 (passe précédente) ; points ouverts v1 et v2, D-21 et D-23 (passes précédentes ; empreinte de la
v1) ; sortie du validateur rejouée ; devis brouillon 3 (en entier) et table de traitement du devis (en entier) ;
`registres/depenses.md`, lignes 226 et 227 (instance 58178416) et les lignes qui portent une fiabilité d'offre
(fragments) ; `registres/go.md`, ligne GO-2026-11-22-77 (passe précédente). Non lus : la note des différences c3
au-delà de son nom ; le `diff` complet devis brouillon 2 → 3 (le brouillon 3 est relu en entier, et ses changements
suivent la table de traitement) ; les additifs et journaux du rédacteur.

# Avis d'ensemble
- **Texte c3** : CW-01 à CW-03 levées ; **scellable après corrections** de CX-01 (choix à porter à la conduite) et de
  CX-02, puis la confirmation de la lettre de D-21 par la conduite et les verrous restants.
- **Devis brouillon 3** : CD-02, CD-03, CD-05 levées ; CD-01, CD-04, CD-06 levées en partie ; **scellable après
  corrections** de CE-01 et des mineures, ou leur refus écrit.
