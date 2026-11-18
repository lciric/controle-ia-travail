# Devis — saboteur à budget (ii-b), course exploratoire — v1, brouillon 6

- **Statut** : **brouillon 6**, scellé comme brouillon, non contre-lu. Brouillon 5 (`devis-ii-b-v1-brouillon5.md`, `8ee9ead15fb5feadbffc41ffb3cd8d9abe8a8fc1d82b588f2957de93405e7e32`), brouillon 4 (`devis-ii-b-v1-brouillon4.md`, `08107e075e72a1711db812069574c6dc5fc2742ec7f1b690151fd1ff974aa580`) et brouillon 3 (`devis-ii-b-v1-brouillon3.md`, `016979ba01926f08be8ac243df75b716cf49ea63ea01e16dedd4302e61f991d4`) intacts (R12). **Aucune dépense n'est engagée par ce document** ; aucune ligne de GO n'y est écrite.
- **Brouillon 4 écrit** le 2026-11-18 vers 20:05 UTC (`date -u`) par le même rédacteur neuf que le brouillon 3 (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, mandat `docs/notes/barreau8-iib-v1/mandat-redacteur-ordre-exploratoire-iib-v1.md`, `55b1e348…`), après la contre-lecture `docs/notes/barreau8-iib-v1/contre-lecture-ordre-et-devis-iib-v1.md` (`d398bf5c4a7902b3821eab5879dfad1176b17adb2e50658166324e01ece22193`, vérifiée, lue en entier ; verdict du devis : « demandable après corrections »).
- **Arithmétique** : `calcul-devis-ii-b-v3.py` (`3ce44b68e8c1c86002e83d37506077947990c16bb8a6b8baf52b6a1929a129d0`), sortie brute `sortie-calcul-devis-ii-b-v3.txt` (`8eecd277527918146d3fb180f86b15ab9098305008e3628f32a3ab9f31f38bd8`), scellés. Elle reprend à l'identique les durées du calcul v2 (`d869c8e8…`, sortie `abe794be…`, intacts), dont proviennent les tables des § 2 à 5.
- **Brouillon 5** : écrit le 2026-11-18 vers 21:30 UTC (`date -u`) par un rédacteur neuf (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, même mandat), qui n'a écrit ni la conception, ni le code, ni leurs contre-lectures, ni les brouillons 1 à 4, et n'a pas ouvert la consigne privée. Fabriqué par programme depuis le brouillon 4 (`appliquer-brouillon5-ii-b-v1.py`, scellé dans ce dossier), recopié à l'octet hors des changements listés dans `differences-brouillon4-vers-5-v1.md`. Il porte les choix de Lazar du 2026-11-18 (`registres/go.md`, lignes `GO-2026-11-18-55` et `GO-2026-11-18-56`, points 3 et 4 ; registre des décisions, ligne `R-3435` ; ces seules lignes lues). **Aucun chiffre ne change** : le calcul v3 a été rejoué (`.venv/bin/python -I -B calcul-devis-ii-b-v3.py`), sortie identique à l'octet à `sortie-calcul-devis-ii-b-v3.txt` (`8eecd277…8bd8`) ; aucun calcul sous nom neuf.
- **Brouillon 6** : écrit le 2026-11-18 vers 22:55 UTC (`date -u`) par un rédacteur neuf (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, modèle Claude Fable 5.2), qui n'a écrit ni la conception, ni le code, ni leurs contre-lectures, ni les brouillons 1 à 5, et n'a ouvert ni la consigne privée ni la conception. Fabriqué par programme depuis le brouillon 5 (`appliquer-brouillon6-ii-b-v1.py`, scellé dans ce dossier), recopié à l'octet hors des changements listés dans `differences-brouillon5-vers-6-v1.md`. Il applique les deux couples de la contre-lecture du brouillon 5 qui touchent le devis (m1, m11 ; `docs/notes/barreau8-iib-v1/contre-lecture-ordre-et-devis-iib-brouillon5-v1.md` (`9ade0f1d3acaedee346fc082f764917d993545c10cf1d43706e9a3a2dd943a72`), lue en entier ; pour le devis : aucun chiffre ne change, plafond et coupure tenus, passe de recalcul hors de la ligne). La réserve R-1 de cette contre-lecture est levée : la ligne `R-3435` du registre des décisions porte, mot pour mot, le verbatim cité au § 0 (vérifié par programme par le rédacteur). Le commit du code revu est `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95` (contrôle court « autorisable », registre des décisions, ligne `R-3497`) : il est écrit dans la ligne d'engagement (§ 9). **Aucun chiffre ne change** : le calcul v3 a été rejoué de nouveau (`.venv/bin/python -I -B calcul-devis-ii-b-v3.py`), sortie identique à l'octet à `sortie-calcul-devis-ii-b-v3.txt` ; aucun calcul sous nom neuf.

## Traitement des remarques de la contre-lecture

| remarque | traitement | où |
|---|---|---|
| D-M1 dernière création | appliquée : dernière commande de création **à 23:00 UTC le 2026-11-25** ; P1 finit vers 2026-11-27T08:18Z (13,7 h avant la minuterie). Le couple donnait 08:19 ; le calcul v3 rend 08:18 (arrondi à la minute) | § 7 |
| D-M2 deux branches de l'activité interne non chiffrées | appliquée : les deux branches chiffrées dans le script v3, hypothèses écrites ; tranché depuis par Lazar, branche B (§ 0) | § 8.1 |
| D-m1 heures avant la coupure | appliquée, avec la formule du code lue par le contre-lecteur (prix de l'offre + 0,08 de stockage) : 38,4 h à 1,30, 35,8 h à 1,40 ; marges 5,1 et 2,5 h sur P1. Le brouillon 3 sous-estimait le prix horaire ; le pire cas reste couvert, avec moins de marge | § 6 |
| D-m2 plafond tenu par les gardes | appliquée : au plus 59,8 USD ; plus de 50 h d'arrêt dépasserait la ligne | § 6 |
| D-m3 1,12 USD/h sans chemin | consignée : la valeur vient de la consigne de la mère citée par le devis brouillon 2 ; je n'en ai pas le chemin. Elle reste dans la fourchette relevée 1,009 à 1,2133 (T0.6 candidat 12 r3, cité par le brouillon 2). Les durées de 7a et les prix relevés n'ont été relus ni par moi ni par le contre-lecteur | § 1 |
| D-m4 P1 à 2,10 en variante A | appliquée : sans objet (le code borne la carte à 1,30 dans les deux variantes) ; ligne retirée | § 5, § 6 |
| D-m5 ligne d'engagement | appliquée : elle cite le commit de lancement | § 9 |
| D-m6 essais du jetoniseur réel sur la carte | appliquée : 0,1 h en option (hypothèse : quelques minutes), 0,11 à 0,28 USD | § 8 |

## 0. La ligne d'accord inscrite

`registres/go.md`, ligne `GO-2026-11-10-08` (lue seule, par recherche de la clé) : type calcul, accordée par Lazar le 2026-11-10, **plafond 60 USD (« option B de M7 ; coupure à 55 USD »)**, **échéance 2026-11-27**, « A100 seule ». Le mot de Lazar recopié dans la ligne dit : « Lancer le saboteur à budget avant le 27, **avec l'activité interne enregistrée**. » La ligne porte aussi une lecture **écrite par la session mère** (ce ne sont pas les mots de Lazar) : la course part seulement après code rendu et contre-lu, devis inscrit en complément, ordre contre-lu et scellé, six épreuves de l'oracle passées. Elle cite « D-4, option (a) », dont le texte n'a été trouvé ni par moi ni par le contre-lecteur.

**Ce devis chiffre la course telle que le code v3 la joue : sans enregistrement de l'activité interne.** Les deux branches sont chiffrées au § 8.1. **Lazar a choisi la branche B** (« garder de quoi recalculer ») par son mot exprès : `registres/go.md`, ligne `GO-2026-11-18-55`, confirmée au registre des décisions, ligne `R-3435`, verbatim : « Ou veux-tu la recalculer plus tard sur une location à part (branche B : aucun code ne change, environ 4,2 à 4,7 dollars plus tard, résultat égal aux arrondis près) go ». La course n'enregistre rien ; on garde les textes exacts des actions et les deux adaptateurs ; l'activité se recalcule plus tard par une passe à part, avec son devis et sa ligne à part (§ 8.3). Les autres points de la note `noeuds-ii-b-pour-lazar-v2.md` (`be431ed5…5207`) sont tranchés par `GO-2026-11-18-56`, point 3 : nœuds 2 (a), 3 (a), 4 (B), 5 (a), 6 (b).

Contrôle (code v3, `d88e3d94`) : la ligne est lue à 60 USD du 10 au 27, refusée le 28 ; une configuration à 55 est acceptée, 75 refusée ; vérifié par le rédacteur sur une copie de la seule ligne, et par le contre-lecteur sur le registre entier.

## 1. Hypothèses (écrites, sourcées)

Inchangées depuis le brouillon 3, sauf la ligne du prix et les deux lignes neuves.

| grandeur | valeur | source |
|---|---|---|
| durée d'un épisode | 43,3 s | lecture A de 7a (`3c84c419…`, § 4), citée par le devis brouillon 2, § 1 ; non relue |
| durées fixes | 0,07 ; 0,58 ; 0,25 (hypothèse) ; 0,10 h | idem |
| distillation | 1,86 s par transcription et par époque | 7a (891 s / 480), cité par le brouillon 2 |
| jumeau honnête | 0,5 / 1,0 / 1,5 s attendu ; 3,0 s pire | non mesuré |
| épisodes, tours, actions | 96 d'étalonnage ; 32 par tour, 6 / 10 / 12 tours ; 256 d'évaluation ; 960 + 320 par tour + 320 + 2 560 actions | conception ; code v3 (`TEXTE`, `jouer_tour`) |
| prix A100 SXM4 80 Go | 1,12 USD/h central (consigne de la mère, sans chemin connu du rédacteur, D-m3) ; relevés 1,009 à 1,2133 (T0.6 candidat 12 r3, `c24e268e…`, cité par le brouillon 2, non relu) ; **borne 1,30** (code v3) ; 1,40 au pire | |
| prix du stockage pendant la course | + 0,08 USD/h, ajouté au prix de l'offre par la garde de dépense (`t06/session_v3.py` l. 95-100, lu par le contre-lecteur) | D-m1 |
| stockage arrêté ; téléchargement | ≤ 0,08 USD/h, 24 h / 48 h ; ≤ 0,05 USD/Go, 20 / 40 Go | code v3 |
| consignation de la minuterie | 2 400 s au plus, carte encore louée | amorce v3 |
| juge de T0.8 | hors des totaux (le code n'en joue aucune passe) | code v3 |

## 2. Heures de carte par étape (A100 ; juge hors des totaux)

| étape | bas | **central** | haut | pire P1 |
|---|---|---|---|---|
| fixe | 1,00 | **1,00** | 1,00 | 2,00 |
| étalonnage : épisodes | 1,15 | **1,15** | 1,15 | 2,31 |
| étalonnage : jumeau | 0,13 | **0,27** | 0,40 | 1,60 |
| maître : épisodes | 2,31 | **3,85** | 4,62 | 9,24 |
| filtrage : jumeau du maître et ancrage | 0,31 | **0,98** | 1,73 | 6,93 |
| distillation | 0,31 | **0,31** | 0,40 | 0,81 |
| évaluation : épisodes | 3,08 | **3,08** | 3,08 | 6,16 |
| évaluation : jumeau | 0,36 | **0,71** | 1,07 | 4,27 |
| **total** | **8,65** | **11,35** | **13,46** | **33,31** |

## 3. Attendu (stockage arrêté 24 h, téléchargement 20 Go)

| scénario | **total** |
|---|---|
| bas, 1,0889 USD/h | ≈ 12,3 |
| central, **1,12 USD/h** | **≈ 15,6** |
| central, 1,30 USD/h | ≈ 17,7 |
| haut, 1,30 USD/h | ≈ 20,4 |

**Attendu : ≈ 8,7 à 13,5 h de carte, ≈ 12 à 20 USD, central ≈ 16 USD.** Ces totaux comptent la carte au prix de l'offre ; la garde ajoute 0,08 USD/h de stockage pendant la course (D-m1), soit au plus 1,1 USD de plus au haut de l'attendu.

## 4. Coupure par point d'arrêt (inchangée)

| point d'arrêt | central (1,12 USD/h, 24 h, 20 Go) | pire P1 (1,40 USD/h, 48 h, 40 Go) |
|---|---|---|
| épreuves de l'oracle en échec | 2,42 h ; ≈ 5,6 USD | 5,91 h ; ≈ 14,1 USD |
| contrôle du tour 4 | 4,41 h ; ≈ 7,9 USD | 11,66 h ; ≈ 22,2 USD |
| fin du tour 12, moins de 48 acceptés | 8,20 h ; ≈ 12,1 USD | 22,08 h ; ≈ 36,8 USD |
| course entière | 11,35 h ; ≈ 15,6 USD | 33,31 h ; **≈ 52,5 USD** |

## 5. Pire cas (stockage arrêté 48 h, téléchargement 40 Go)

| scénario | heures | USD | sous la ligne (60) ? |
|---|---|---|---|
| **P1** sur A100 à 1,30 / **1,40** | 33,31 | 49,1 / **52,5** | oui |
| H200 NVL d'emblée (variante A seulement) à 4,70 | 13,46 | 69,1 | non |
| relance après une erreur de chaîne ou de mémoire | — | — | nœud de Lazar avant toute relance |

## 6. Plafond : les deux variantes côte à côte

| | **variante A** | **variante B** |
|---|---|---|
| ligne de GO ; coupure de la configuration | 80 ; 75 USD | **60 ; 55 USD** |
| conforme à la ligne inscrite (60) ? | non : ligne neuve exigée | **oui** |
| carte | A100 ≤ 1,30 ; fenêtre vide : H200 NVL ≤ 4,70 | A100 ≤ 1,30 ; **fenêtre vide : nœud** |
| heures avant la coupure, formule du code (offre + 0,08 de stockage ; 40 Go déduits), à 1,12 / 1,30 / 1,40 | 60,8 / 52,9 / 49,3 h (même formule, coupure à 75) | **44,2 / 38,4 / 35,8 h** |
| marge sur P1 (33,31 h) à 1,30 / 1,40 | 19,6 / 16,0 h | **5,1 / 2,5 h** |
| plafond tenu par les gardes : coupure + consignation (≤ 2 400 s de carte) + stockage arrêté 48 h | 75 + 0,99 + 3,84 ≈ 79,8 | **55 + 0,99 + 3,84 ≈ 59,8** (au plus ; marge 0,2 USD ; au-delà d'environ 50 h d'arrêt, la ligne serait dépassée : l'instance arrêtée est détruite sous 48 h) |
| marqueur `REPLI_H200_PERMIS` | oui | **non** |

(Les heures de la variante A avec la formule du code sont calculées à la main : (75 − 2,0) / (prix + 0,08) ; elles ne sont pas dans la sortie v3, qui ne rejoue que la coupure de 55.)

**La ligne inscrite correspond à la variante B.** **Variante B retenue** : nœud 4 (B) de la note v2, tranché par Lazar (`GO-2026-11-18-56`, point 3).

## 7. Calendrier

| grandeur | valeur | source |
|---|---|---|
| fin du GO | **2026-11-28T00:00:00Z** (1 795 824 000 s) | règle du code |
| échéance de la minuterie | **2026-11-27T22:00:00Z** (1 795 816 800 s) | proposée ; consignation et destruction finies avant la fin du GO |
| dernier jour de création | **2026-11-25** | proposé |
| **dernière commande de création** | **2026-11-25T23:00Z** : l'amorce rejoue le calendrier à l'heure de l'instance et refuse un démarrage daté du 26 (contre-lecture, O-M6) | calcul v3 |
| fin de P1 pour une création à 23:00 le 25 | 2026-11-27T08:18Z, 13,7 h avant la minuterie | calcul v3 |
| fin du haut de l'attendu | 2026-11-26T12:27Z | calcul v3 |
| fenêtre de recherche d'une A100 | 12 essais toutes les 15 min, environ 2 h 45 : **première recherche au plus tard vers 20:15Z le 25** pour que toute la fenêtre tienne avant 23:00Z | ordre § 5 |
| création | **jamais avant la création de 7b** (ligne du registre exigée par le code) ; si 7b n'est pas créée le 25, la course ne part pas sous cette ligne : on laisse passer le 27, une ligne neuve sera à demander à Lazar (nœud 2 (a), `GO-2026-11-18-56`, point 3) | code v3 ; nœud 2 |

Aucune place pour une seconde course sous cette ligne.

## 8. Ce qui reste hors de la course chiffrée

### 8.1 L'activité interne : deux branches (ordres de grandeur, non mesurés) ; **branche B retenue** (`GO-2026-11-18-55`, confirmée `R-3435`)

Hypothèses (script v3, en-tête) : modèle à 32 couches de taille 4 096 (architecture publique, non relue sur pièce) ; un vecteur en demi-précision par action et par couche : 8 192 octets ; 2 560 actions à l'évaluation, 7 360 au plus en tout ; capture pendant les épisodes sans surcoût de durée (7a capturait sur la moitié des actions au même débit, d'après le devis brouillon 2) ; passe de capture : 1,5 à 3,0 s par épisode (**hypothèse du rédacteur, sans source**). Chiffres de la contre-lecture (§ 5.2) rejoués.

| | **branche A : enregistrer pendant la course** | **branche B : garder de quoi recalculer, passe plus tard** |
|---|---|---|
| carte en plus, pendant la course | capture pendant les épisodes : ≈ 0 h ; passe après l'évaluation : 0,11 à 0,61 h (1,23 h au pire) | 0 h |
| dollars en plus, dans la ligne de 60 | ≈ 0 à 0,9 USD (1,7 au pire) ; P1 avec passe : ≈ 54,2 USD, 34,5 h, 1,3 h de marge sous la coupure à 1,40 | 0 USD |
| dollars plus tard, sur un devis et une ligne à part | — | 1,1 à 1,6 h de carte, **≈ 4,2 à 4,7 USD** attendus ; 2,2 à 3,2 h, **≈ 8,9 à 10,4 USD** au pire |
| disque | un vecteur par action : 21 Mo par couche (évaluation), 60 Mo (toutes phases) ; 0,67 et 1,93 Go pour 32 couches (8 et 22 morceaux de 90 Mo) ; tous les jetons générés : 8,4 et 24,1 Go **par couche** | quelques dizaines de Mo (adaptateurs, identifiants, textes) |
| envoi depuis l'instance | non borné par une garde du code | — |
| code et textes, avant la course | gardes à retirer ou assouplir, capture ou passe à écrire, étape des morceaux de l'amorce, essais, contre-lecture neuve ; conception et ordre en version nouvelle | rien d'obligatoire |
| décision préalable | quoi enregistrer (couches, jetons, précision) : un choix du côté des moniteurs | aucune avant la course |
| ce qu'on a à la fin | l'activité calculée pendant la location | de quoi la recalculer, **égale aux arrondis du calcul près, pas au bit près** |
| lettre de la ligne | tenue | non tenue à la lettre : mot exprès de Lazar, donné (`GO-2026-11-18-55`, `R-3435`) |

La colonne A est gardée pour mémoire : elle n'est pas chiffrée dans cette course. Si Lazar voulait la branche A, il le dit, la ligne `GO-2026-11-18-55` est remplacée, et l'ordre et ce devis passent en version nouvelle.

### 8.2 Autres

- Essais du jetoniseur réel joués sur la carte par l'amorce (si le directeur le choisit, ordre § 4 ter) : + 0,1 h (hypothèse), 0,11 à 0,28 USD (D-m6).
- Contre-lecture, corrections du code, essais sur processeur, répétition jouet, lectures (1) et (2) : 0 USD.
- Juge de T0.8, juge d'une autre lignée : devis et GO à part ; non joués par le code v3.
- Passe préalable des épreuves sur une location à part : **non retenue** (nœud 3 (a), `GO-2026-11-18-56`, point 3 : épreuves au début de la course, même carte, arrêt au premier échec) ; 0 USD.
- 7b, P3-bis, A1-v4 : lignes à part, jamais entamées.

### 8.3 La passe de recalcul de l'activité interne : une course à part (branche B)

- **Hors de ce devis et hors de la ligne `GO-2026-11-10-08`** (« 0 USD de plus dans GO-2026-11-10-08 », ligne `GO-2026-11-18-55`) : elle a son devis écrit, sa ligne au registre des accords et son préenregistrement scellé, à part (ordre brouillon 6, § 13). **Aucune dépense n'en est engagée ici.**
- Ordre de grandeur (§ 8.1, non mesuré ; repris dans `GO-2026-11-18-55`) : 1,1 à 1,6 h de carte, ≈ 4,2 à 4,7 USD attendus ; 2,2 à 3,2 h, ≈ 8,9 à 10,4 USD au pire.
- Ce qu'elle consomme de la course : les identifiants et textes exacts des actions (par phase et combinés), les deux adaptateurs, la configuration et le manifeste (commit de lancement, versions) ; le modèle de base à sa révision figée, que le programme ne garde pas.
- Ce qu'elle rend : l'activité interne, égale aux arrondis du calcul près, pas au bit près.

## 9. Ligne d'engagement (à écrire par la mère au registre des dépenses, à la création ; forme seulement)

« engagement : saboteur à budget (ii-b), course exploratoire, non opposable (R-522) (`<<GO_ID_IIB>>`, plafond `<<PLAFOND_LIGNE_IIB>>` USD, configuration `<<PLAFOND_CONFIG_IIB>>`) : ordre `<<CHEMIN_ORDRE_IIB>>` (`<<EMPREINTE_ORDRE_IIB>>`), lanceur `scripts/lancer_iib_v1.sh`, commit de lancement `<<COMMIT_LANCEMENT_IIB>>` (code revu `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`) ; branche de l'activité interne B (`GO-2026-11-18-55`, confirmée `R-3435`), passe de recalcul hors de cette ligne ; une carte A100 SXM4 80 Go ≤ 1,30 USD/h, disque ≥ 100 Go ; attendu ≈ 12 à 20 USD, pire cas ≈ 52,5 USD (au plus 59,8 tenus par les gardes) ; créée après 7b (`<<LIGNE_REGISTRE_CREATION_7B>>`) ; crédit Vast.ai relu à la création ».

Les marqueurs de cette ligne sont remplis par la mère au registre.
