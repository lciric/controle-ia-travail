# Papier C — vérification de la version c4 du préenregistrement et du brouillon 4 du devis du pilote — v1

- Contre-lecteur : le même qu'aux quatre passes précédentes (sous-agent Opus 5.5, `claude-opus-5-5`), le 2026-11-22.
  Branche courante, commit `b6879e2a5`.
- Pièces : texte c4, `51eea9c5d061a5c4f3d838512d69a1b4715530ca84e0cec803dd17e2870fcc99` (égale à son compagnon et à
  l'attendu) ; devis brouillon 4, `f7ba4a71fcb213343dad8ce7e848517f484e40284d49f4afefa336cad8fdc10f` (égale à son
  compagnon et à l'attendu).
- Interdits tenus ; aucune ligne de `registres/depenses.md` relue à cette passe ; aucune dépense ; aucun refus de
  permission ; écrit dans ce seul dossier.

**Décompte des remarques neuves : 0 bloquante, 0 majeure, 2 mineures (CY-01 pour le texte, CZ-01 pour le devis).**
**Avis.** Texte c4 : **scellable** au titre de la contre-lecture, sous les verrous restants (CY-01 se traite par
erratum de forme). Devis brouillon 4 : **scellable** (CZ-01 se traite par une phrase, sans nouvelle passe).

# Partie A — texte, version c4

## A.1 Différentiel
Programme `travail/construire_brouillon7_relance_c4_v1.py` rejoué vers mon bloc-notes : sortie `51eea9c5…`
(268 273 octets), journal identique octet pour octet ; remplacements exacts seulement. `diff` c3 → c4 relu en
entier : titre ; état en bref ; historique (nom et version c3) ; « Ce que change la version c4 » ; verrou 1 (erratum 1
des points ouverts v3) ; verrou 7 ; verrou 8 (devis brouillon 4) ; deux blocs du cadre du bras « saboteur sans
consigne » ; section « Contre-lecture ». **Aucun changement hors des 12 remplacements.**

## A.2 Remarques passées

| Remarque | État | Lieu |
|---|---|---|
| CX-01, honnête avec consigne face à un saboteur sans consigne | **levée** | Plan, section 3, « Cadre fixé dès maintenant » (« même contexte des deux côtés … consigne privée comprise, et ne diffèrent que par le modèle qui écrit ») ; « Ce que fixe le complément » (le contexte commun, donc les cellules honnêtes) |
| CX-02, « rapportées » et « critères de lecture » | **levée** | même paragraphe : « au titre du présent texte, elles ne confirment ni ne réfutent rien » ; le complément peut donner des critères propres, dont l'issue s'écrit « sur saboteur sans consigne » et ne remplace jamais une ligne du présent texte. Une seule lecture. |

**Compte d'épisodes** : juste. Organisme lu sous la condition honnête du présent texte : honnêtes H et HP_m
réemployés, saboteur S et SP_m, (n/2) × (1 + k_P) par organisme. Sous un autre contexte : en plus, une fois par
contexte, (n/2) × (1 + k_P) épisodes honnêtes (H et HP_m sous ce contexte), ce qui est le nombre de cellules
honnêtes par tâche.

**Cohérence** : le principe « même contexte » ne contredit ni la réserve 20 (il en est la réponse, et le saboteur du
bras reste « sans consigne de saboter en contexte »), ni la garde 24, ni les « Préalables » de l'étape 2, ni le
point 14 de la « Métrique » (le témoin lexical porte sur les cellules du présent texte et n'est pas touché).

**Ajout du rédacteur (différence de modèle entre les deux côtés)** : juste, et utile. Dans ce bras, la seule
différence qui reste est le modèle, et il porte à la fois le sabotage appris et l'entraînement lui-même (un réglage
fin peut déplacer une sonde lue sur le modèle de base sans rien de commun avec le sabotage). Demander au complément de
dire ce qu'il en fait est nécessaire. L'engagement est tenable : la branche « sinon une réserve écrite » est toujours
disponible ; « s'il en existe un » n'oblige à entraîner aucun modèle (un témoin honnête distillé de la même façon
serait le contrôle naturel de la famille (ii), mais il coûte un entraînement : sur devis, au complément).

**Verrous 1, 7 et 8, historique** : fidèles. Verrou 7 : la confirmation de la conduite est citée comme un message de
19:29Z, « à consigner à son registre » ; je la trouve au journal du rédacteur v5 (ligne de 19:29), non encore au
registre des décisions : le texte le dit justement.

### CY-01 — mineure — section « Contre-lecture » : la confirmation de la conduite est attribuée à mon rapport
- **Lieu** : section « Contre-lecture », paragraphe « Vérification de la version c3 ».
- **Citation** : « CW-01 à CW-03 levées (pour CW-01 : la lettre de la décision D-21 suivie par le texte est celle de
  la ligne d'accord, confirmée par la session de conduite) ».
- **Constat** : mon rapport (`265f62e7…`) écrit CW-01 « levée (sous la confirmation demandée à la conduite, qui ne
  relève pas du texte) » ; la confirmation est venue après, par message. La phrase la place dans le résumé de mon
  rapport.
- **Correction demandée** : « CW-01 levée sous la confirmation de la conduite, venue ensuite (message de 19:29Z,
  verrou 7) ». Erratum de forme, sans nouvelle vérification.

**Rien de tranché n'a bougé** : énoncés, prédictions, marges, seuils, D-1 à D-20, règle de la précision 38, hors du
`diff`. **Validateur** : section « Contre-lecture » à remplir et les mêmes dix-sept marqueurs.

# Partie B — devis, brouillon 4

## B.1 Remarques passées

| Remarque | État | Lieu |
|---|---|---|
| CE-01, dépense mesurée par le crédit du compte | **levée** (un chemin étroit de sous-compte : CZ-01) | § 5, « Dépense du pilote : comptée par instance » et « Le crédit du compte : un contrôle » ; § 4, ligne ; § 8 |
| CE-02, mode raisonné et second lancement | **levée** | § 5, deux projections ; § 1, cas (b) ; § 4, ligne et table : cohérents (arrêt par projection = nœud ; second lancement sur le seul mot du directeur) |
| CE-03, disque gardé au-delà de 2 heures | **levée** | § 5, « Après l'arrêt » (dans le plafond ; heure d'épuisement écrite au nœud) ; § 3 (37 heures par dollar à 0,027 USD/h) ; § 4, point 2 |
| CE-04, fichiers descendus | **levée** | § 2, « fichiers descendus » (motifs à l'addendum, un seul jeu de poids), « place calculée » ; § 5 (place au-dessus du disque de l'offre : pas de création) ; fourchette 0,978 à 0,9986 |

Reprises des passes précédentes : CD-01 et CD-06 désormais **levées** (par CE-01) ; CD-04 reste levée en partie,
acceptable (attendu non sourcé, dit tel quel, remplacé par deux mesures).

**Le plafond de 10 USD.** Cas sain : tenu. Second lancement : tenu (la dépense du premier est comptée par instance,
non par le crédit). Réseau cher : refusé avant création par la place calculée × prix au gigaoctet ; en marche, borné
par le recalcul toutes les 30 minutes. Recharge automatique ou autre instance active : sans effet sur la dépense
comptée ; le crédit n'est plus qu'un contrôle, qui ne peut qu'augmenter la dépense retenue, et qui n'arrête rien s'il
est « non exploitable ». Le seul dépassement possible est celui du point 2 du § 4 (disque gardé), posé au directeur.

**Point 2 du § 4** : posé loyalement. Les deux lectures sont dites (garder le disque et dépasser au seul prix du
disque, consigné ; ou détruire au plafond et perdre des sorties payées), avec ce que chacune coûte (le § 3 donne
l'ordre de grandeur : environ 37 heures par dollar) ; la recommandation suit la règle du programme « récupérer ce qui
est récupérable ».

**Contradiction avec le texte c4** : aucune. Le devis reste plus serré que le point 1.6 et la garde 3 (par lancement,
sur la carte, sous 10 USD), et ses préalables sont ceux de la garde 2.

**Ce que le brouillon 4 change hors de mes remarques** : rien d'autre que la mise à jour des renvois (texte c4,
rapport et table traités), l'étape 4 du § 7 (relevés dès avant la création) et le § 8 (ce que l'interface du loueur
donne par identifiant, renvoyé à l'auteur du lanceur). Tout suit d'une remarque ; rien n'élargit la dépense.

### CZ-01 — mineure — sans coût lu par identifiant, le calcul du lanceur peut rester sous la facture
- **Lieu** : § 5, « le calcul du lanceur : heures de marche (de la création à l'arrêt, à son horloge) × prix horaire
  relu » ; « si l'interface ne donne aucun coût par identifiant, c'est le calcul du lanceur ».
- **Constat** : quand l'interface ne donne pas de coût par identifiant et que le contrôle du crédit est « non
  exploitable », seul le calcul reste. Il compte de la création à l'arrêt selon l'horloge du lanceur, alors que le
  loueur facture de sa propre création à sa propre destruction (délais des appels, arrondis de facturation), et ne
  compte le réseau que pour les fichiers que le lanceur descend lui-même. L'écart est petit, mais c'est le seul chemin
  de sous-compte qui reste.
- **Correction demandée** : compter de l'appel de création à la confirmation de la destruction (et non à l'arrêt),
  heures arrondies au-dessus selon la règle de facturation du loueur si elle est connue, et ajouter une marge écrite
  (par exemple 10 %) au calcul quand aucun coût par identifiant n'est lu. Une phrase ; pas de nouvelle passe.

# Ce que j'ai lu, en fait
Le message de la session ; programme c4 (exécuté ; fonction principale) et son journal (comparaison) ; `diff` c3 → c4
complet ; validateur rejoué ; `diff` devis brouillon 3 → 4 complet (le brouillon 3 relu en entier à la passe
précédente) ; table de traitement de la vérification du devis (en entier) ; journal du rédacteur v5 (la seule ligne
de 19:29) ; `registres/decisions.md` (recherche de « 19:29 » et « D-21 », trois lignes de fin, sans lecture de
R-2059) ; noms des pièces du dossier. Non lus : la table de traitement de la vérification de c3 et la note des
différences c4 au-delà de ce que le `diff` montre ; l'erratum 1 des points ouverts v3 (son existence seule vérifiée) ;
aucune ligne de `registres/depenses.md`.

# Avis d'ensemble
- **Texte c4** : CX-01 et CX-02 levées ; aucun changement hors table ; **scellable**, sous l'erratum de forme CY-01 et
  sous les verrous restants (mot du directeur sur la précision 37 et sur D-22 ; module et configuration ; rapport de
  la grille ; taux de la réserve d'intention ; champs du scellement ; versement sur `main` ; consignation de la
  confirmation de D-21).
- **Devis brouillon 4** : CE-01 à CE-04 levées ; **scellable**, la phrase de CZ-01 ajoutée ou refusée par écrit.
- Je n'ai plus de remarque de fond sur l'une ou l'autre pièce.
