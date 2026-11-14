# Vérification courte du brouillon 2 (étape B bis de T0.7) — v1

- **Vérificateur** : sous-agent neuf, « modèle C » (aucun identifiant de modèle dans sa pièce) ; n'a écrit ni le texte, ni sa conception, ni la contre-lecture 1 ; ne sera lecteur d'aucun verdict. Début 12:09 UTC, fin voir pied (`date -u`).
- **Relus** : brouillon 1 (`a85eed3a…`, compagnon conforme) et brouillon 2 (`cbfec6aaa4c650443dcea7bac4d0c61bf4a8fdd34ec90572b434a45180184c88`, compagnon conforme) ; `pieces/couples-brouillon2-v1.py` ; contre-lecture 1 (`9c410746…`) ; conception, devis, nœuds v2 ; `pieces/calculs-bbis-v2.py` et sa sortie ; lignes R-2733, R-2736, R-2714, R-2716 ; en-tête de `src/controle_ia/t07/sondes_neuves_v1.py` (empreinte `d4d354e7…` égale à celle citée) ; sondages de T0.6 (l. 575) et T0.8 (douze traits). Tous les compagnons `.sha256` du dossier et de `pieces/` : conformes.
- **Non ouverts** (interdits respectés) : aucun `diag/`, `runs/`, `donnees/` de 7a ou 7b ; ni `lecture-sondes-t06.json`, ni sortie de T0.7 ; aucune pièce du bras d'attaque, du mode tenu à l'écart, de l'étiqueteur ; aucune valeur de clé. Aucun fichier lu n'est modifié (le rejeu a écrit dans le bac à sable seulement).

## Verdict

**Scellable après corrections** : six couples (K1 à K6, ci-dessous), tous courts, aucun ne touche un état, un seuil ou une puissance. Les huit majeurs et les onze mineurs sont fermés ou fermés autrement ; aucune contradiction avec la demande de Lazar (R-2716) ; la table d'issues est fermée (aucun trou ni chevauchement nouveau) mais le nœud 5 laisse trois marges de lecture (K1, K2, K3) et deux petites contradictions internes (K4, K5) demandent une ligne chacune.

## Contrôles mécaniques

- Rejeu de `couples-brouillon2-v1.py` sur une copie du brouillon 1 : 92 couples appliqués, les onze motifs de renommage comptés, **sortie à l'octet égale au brouillon 2** (`cmp` : identique ; empreinte `cbfec6aa…`). Aucun reste de « IA » (hors la mention citée au tableau m10) ; aucun reste de « témoins de sélectivité », de `S`, de `PIECE_HEWITT_LIANG_2019` ni de `CONTRE_LECTURE_1` hors du tableau de traitement.
- Rejeu de `calculs-bbis-v2.py` : sortie identique à `sortie-calculs-bbis-v2.txt`. Valeurs retrouvées : 0,0707 / 0,0719 (99 %), 0,0580 / 0,0589 (95 %), 0,6034 (nul), 0,5537 (réserve), 0,6408 et 0,6058 (T0.7). Devis v2 : 4,30 à 7,35 + disque 0,32 à 0,53 + téléchargement 1,00 à 2,00 = 5,62 à 9,88 ; P1 11,3 h = 18,80 ; P2 22,6 h = 37,53 ; P3 58,09 : exacts. Garde de débit : 2,15 h + 0,6 h + 2 440 × 1,2 × médiane = 11 h pour une médiane de 10,14 s : exact, « ≈ 10 s » correct.
- Marqueurs `<<…>>` : exactement dix, ceux de la liste de fin ; le validateur `prereg.problemes` ne relève que ces dix : `<<CODE_BBIS>>`, `<<ENTROPIE_BBIS>>`, `<<CODE_MOTS_ET_COUT_T06>>`, `<<EPREUVE_NIVEAU_DEUX_PLIS>>`, `<<LIGNE_GO_BBIS>>`, `<<MOT_LAZAR_ECART_CODE>>`, `<<MOT_LAZAR_NOEUD_1>>`, `<<MOT_LAZAR_NOEUD_2>>`, `<<MOT_LAZAR_NOEUD_3>>`, `<<VERIFICATION_COURTE_BROUILLON2>>`. Rien d'autre d'ouvert. Retirés comme dit : `PIECE_HEWITT_LIANG_2019`, `CONTRE_LECTURE_1`, `MOT_LAZAR_NOEUD_5`.

## (1) Constat par constat

| constat | état | note |
|---|---|---|
| M1 | **fermé** | E6 = D_TE > 0 et borne basse de DD > 0 ; E5 = DD ≤ 0 ou non calculable (ART écrit) ; crochet de I6 retiré ; nœud 5 réécrit ; DD « seule voie vers E6 » écrit à la Métrique et au Seuil ; m4 résolu du même coup. |
| M2 | **fermé autrement** | le nul est renommé, la citation retirée, les limites écrites, la capacité de mémorisation rapportée (scores d'apprentissage écrits fermés, aires à la lecture, rien sur l'instance : cohérent avec le point 8) ; garde de surface SC ajoutée, frontière conforme à l'en-tête de `sondes_neuves_v1` (interprétation (b), l. 34-35, vérifiée) et à `lire_action` (existe, `environnements/propositions.py`). « Autrement » : l'adversaire « tâches témoins » de R-2716 (1) devient un objet presque redondant avec le plancher ; c'est déclaré (HB-1, Métrique) mais pas dit à Lazar comme tel : voir (2), point a. |
| M3 | **fermé** | section D à six points (circularité, mode non joué, aucune sonde sans étiquette, réglage fin, 32 tâches, transfert entre familles, deux libellés) ; reprise en fin de I6. |
| M4 | **fermé** | trois cas sains (modèle nu, `S100` sous `S100`, `T100` sous `T100`, 8 épisodes) au plan point 3, à la liste d'arrêt et au code neuf ; l'artefact est gardé. |
| M5 | **fermé** | dépendance devenue marqueur ; repli au mercredi 18 à 12:00 UTC ; implémentation de repli spécifiée (point 8 bis), cohérente avec T0.6 l. 575 (sac de 1 000 mots, coût normalisé, forme du champ) et T0.8 (traits 1, 3, 4, 7 à 12) ; contrôle d'égalité seulement si le fichier existe ; calendrier et liste d'arrêt alignés. Deux précisions en K6. |
| M6 | **fermé autrement** | seuil 11 h au lieu de 5,65 h, motivé et recalculé (voir (4)) ; contrôlé par épreuves (médiane 2 s sain, 20 s artefact) ; deux défauts à corriger : K4 (contradiction avec « jamais arrêtée »), K6 (ordre des 20 premiers). |
| M7 | **fermé** | HB-3m, règle (a) à 95 %, R-MU, BB-P9, libellé « lecture dure ». |
| M8 | **(i) (iii) (iv) fermés ; (ii) fermé autrement** | écart au gabarit soumis au nœud 4 ; défaut du nœud 1 dit sans effet sur la porte ; nœud 2 reformulé (hôte déjà décidé, R-2711 (2)). Nœud 5 sans défaut avec deux libellés : voir (3) et K1 à K3 ; marqueurs sans défaut : K5. |
| m1 | fermé | étiquetage par condition déclaré, DOM-H. |
| m2 | fermé | base décisive choisie une fois, tenue fixe. |
| m3 | fermé autrement | épreuve de niveau en deux plis prescrite avant le scellement, repli 99,5 % ; son coût de calcul sur processeur et la puissance à 99,5 % ne sont pas écrits (K6). |
| m4 | fermé | par M1. |
| m5 | fermé | T0 défini ; I1 nomme doses lues et non calculables. |
| m6 | fermé | « section C de ce texte ». |
| m7 | fermé | « aucune valeur d'aire n'est prédite » ; inversion et inversion établie définies. |
| m8 | fermé | puissance conjointe de E6 et puissance d'apprentissage écrites. |
| m9 | fermé, avec reste | téléchargement sourcé à T0.6 (20 à 40 Go) ; disque de la relance compté (P2 = 37,53) ; reste : le disque haut est calculé sur 5,65 + 1,0 = 6,65 h (`calculs-bbis-v2.py` l. 113) et le devis ne dit pas d'où vient ce « + 1,0 h » (K6, sans effet sur le plafond). |
| m10 | fermé autrement | « IA » partout remplacé ; les autres abréviations restent, définies au vocabulaire, les phrases gelées en toutes lettres (déclaré « accepté en partie »). |
| m11 | fermé | créneau lundi soir ou mardi matin écrit. |

## (2) Rien de neuf contre la demande de Lazar (R-2716 (1), R-2714 (2))

Point par point : plan scellé avant toute exécution de B (plus strict que « lecture ») ; cellules fixées au point 9 ; mêmes découpages (blocs de tâches, plis de T0.6) ; relecture forcée sous le modèle nu et sous chaque dose ; validation croisée imbriquée ; adversaires plancher, « mots et coût », texte seul (LEX, ENC), « tâches témoins », séparation à texte égal ; table conjointe scellée d'avance ; deux verdicts de lecteurs neufs, « jamais le meilleur des deux » : **tout tient**. « Rester muette sur le jumeau » (R-2714 (2)) est maintenant écrit (MU, libellé dur) : la dérive signalée par M7 est corrigée. Les ajouts (SC, DOM-H, section D, repli de MC, garde de débit) sont descriptifs ou protecteurs et ne remplacent aucun élément demandé.
- **Point a (à dire à Lazar, pas à corriger dans le texte)** : « tâches témoins » est devenu un nul presque redondant avec le plancher. La contre-lecture 1 le demandait et le texte le déclare ; mais la lettre de R-2716 (1) nomme cet adversaire. Une ligne dans l'envoi des nœuds (« l'adversaire « tâches témoins » est rendu sous la forme d'un nul de réétiquetage, aux limites écrites ») suffit ; aucun nœud de plus.

## (3) Règle « choisi après lecture » et deux libellés du nœud 5 : fermée ?

**Fermée pour les états** (E0 à E6, I0 à I6, 28 paires, lignes C0 à C6 : les deux libellés et les deux variantes de P ne touchent ni états ni issue ; l'énumération couvre les libellés × 3⁴ qualifications de MU). **Pas encore sans marge de lecture**, trois points :

- **K1 (minute de référence du choix)** : « si Lazar choisit avant `LECTURE-BBIS` … sinon … après la lecture » (plan, point 11) ne dit pas de quelle lecture il s'agit. Lazar peut avoir lu le verdict de l'étape B (qui peut être scellé avant jeudi 19) puis choisir avant `LECTURE-BBIS` : le choix serait inscrit comme préenregistré alors qu'il est postérieur à une lecture de B, ce que R-2716 (1) (« plan scellé avant toute lecture de B ») interdit ; la garde du point 10 (a) ne vérifie que l'ordre des lignes propres. Un choix inscrit après le scellement est aussi un ajout à un texte scellé : il doit être borné.
- **K2 (effet du « libellé principal »)** : le texte ne dit nulle part ce que « désigner le libellé principal » change, puisque les deux libellés, les deux variantes C et tous les états sont toujours écrits ; un verdicteur peut y lire un titre, un ordre, ou une variante décisive.
- **K3 (trois sens de « plafond tient »)** : la ligne I6 s'intitule « plafond tient » (E6, sans condition sur MU) ; « Plafond tient, transfert échoue » = I6 suivi de T− ; la section D (1) emploie « plafond tient » sans qualificatif ; les libellés du nœud 5 portent aussi « plafond tient » (lecture dure = E6 et muette ; lettre = E5 ou E6). Trois lectures de la même formule, dont aucune n'est celle de I6 ; une phrase peut être citée au billet sous un libellé que le texte n'a pas voulu.
- Aussi à noter (non bloquant) : sous la variante « lettre », une dose en E5 donne P+ et la phrase C1 « ce qui est lu n'est pas seulement le texte » sans mention de l'artefact non écarté ; l'artefact est écrit à côté (R-ART, I5), mais C1 gagnerait à le dire.

## (4) Garde de débit à 11 h, repli du mercredi 18, calendrier jusqu'au dimanche 22

- **Garde à 11 h** : cohérente avec le devis. 11 h = heures de P1 (11,3 h au devis, arrondi à 11 : écart sans effet) ; une marche à 11 h projetés coûte ≈ 18,8 USD, une relance de même 37,5 USD < 40 USD ; la médiane déclenchante (10,14 s) est 2,5 à 5 fois l'hypothèse (2 à 4 s) ; arrêt avec instance gardée 12 h (0,08 × 12 ≈ 1 USD), nœud sur (r1) ou (r2), puis destruction par identifiant : cohérent avec l'issue I0 (« marche sans scores ») et le plafond. Chemin dégradé : arrêt vers 2,5 h de marche mercredi, attente jusqu'à 12 h, relance (r1) de ≈ 1 240 apprentissages : verdict samedi 21 au pire, dimanche 22 tenu ; le texte dit « calendrier inchangé (verdict visé vendredi 20) » : exact dans le cas nominal. Deux défauts : K4 (la liste d'arrêt dit encore « une marche lente mais vivante n'est jamais arrêtée »), K6 (les 20 premiers apprentissages ne sont pas définis en famille ; si la grille met les sondes linéaires avant les sondes à attention, la médiane sous-estime).
- **Repli de MC au mercredi 18 à 12:00 UTC** : cohérent. MC se calcule à la lecture, sur processeur, donc l'instance n'en dépend pas ; la règle (état à 12:00 mercredi) prime sur le marqueur de scellement (état lundi), sans contradiction ; le code de repli est écrit avant `CODE-BBIS` (mardi) ; la partie « code de la pièce » ne peut pas être éprouvée avant que la pièce existe (interface inconnue). La liste d'arrêt écrit « (avant l'instance) » : MC n'étant pas calculé sur l'instance, soit le dire, soit retirer (K6).
- **Calendrier** : lundi 16 sceller (défauts des nœuds 1, 2, 3 échus ; nœuds 4 et 5 sans défaut), mardi GO et code, mercredi instance, jeudi lecture, vendredi verdict, samedi marge (relance unique avant 12:00), dimanche échéance : tenable. **Trou** (K5) : `<<LIGNE_GO_BBIS>>` et `<<MOT_LAZAR_ECART_CODE>>` sont listés « à remplir avant le scellement » mais attendent un mot de Lazar sans défaut, et le calendrier place la ligne de GO mardi 17, après le scellement de lundi ; nouveauté du brouillon 2 : l'écart au gabarit au nœud 4 ajoute un marqueur sans défaut. Sans règle, un silence de Lazar bloque le scellement, donc l'étape B.

## (5) Marqueurs restants

Exactement les dix listés plus haut (contrôle par recherche et par `prereg.problemes`). Rien d'autre d'ouvert. `<<VERIFICATION_COURTE_BROUILLON2>>` se remplit avec ce rapport : chemin `brouillons/T0.7-etape-B-bis-v1/verification-courte-brouillon2-v1.md` et son empreinte `.sha256`.

## Corrections demandées (couples ancien → nouveau)

**K1** — plan, point 11, fin :
- ancien : « si Lazar choisit avant `LECTURE-BBIS`, son choix est inscrit (ligne `LIBELLE-BBIS`) et désigne le libellé principal ; sinon, aucun libellé n'est principal, et un choix fait après la lecture est écrit comme tel (« choisi après lecture »), jamais comme une lecture préenregistrée (R3). »
- nouveau : « si Lazar choisit **avant la première lecture de l'une ou l'autre étape** (le premier commit qui ajoute `lecture-t07.json`, ou `LECTURE-BBIS`, selon le plus ancien ; la garde du point 10 (a) vérifie que `LIBELLE-BBIS` lui est antérieure), son choix est inscrit (ligne `LIBELLE-BBIS`) ; sinon, un choix fait après l'une ou l'autre lecture, ou après le verdict de l'étape B, est écrit comme tel (« choisi après lecture »), jamais comme une lecture préenregistrée (R3). » Mettre le même texte aux « Nœuds » (plan, fin) et au nœud 5 de `noeuds-etape-b-bis-v2.md` (« avant la lecture de B bis » → « avant la première lecture, de B ou de B bis »).

**K2** — plan, point 11 (même endroit), ajouter après « son choix est inscrit (ligne `LIBELLE-BBIS`) » :
- nouveau : « … et fixe seulement l'ordre d'écriture : le libellé choisi titre le verdict et le billet, l'autre est écrit dessous en même taille ; sans choix, l'ordre est « lecture dure », puis « lettre de R-2716 » ; le choix ne change ni un état, ni l'issue I, ni une ligne C, ni une variante de la table C ; il n'est jamais décisif. »

**K3** — Critères B : ligne I6 et suffixe ; Critères D (1) :
- ancien : « | I6 **plafond tient** | le plus haut est E6 | »  → nouveau : « | I6 **au bout (au-delà de l'artefact)** | le plus haut est E6 | » ; ancien : « « **Plafond tient, transfert échoue** » = I6 suivi de T−. » → nouveau : « « **Au bout, transfert échoue** » = I6 suivi de T−. » ; ancien (D (1)) : « (1) un « plafond tient » dit » → nouveau : « (1) un « plafond tient » (l'un ou l'autre des deux libellés du nœud 5, ou la ligne I6) dit ». Ajouter à C1 : « (aux doses en E5 l'artefact d'adaptateur n'est pas écarté : R-ART) ».

**K4** — Liste d'arrêt, avant-dernière puce :
- ancien : « une marche lente mais vivante n'est jamais arrêtée ; »
- nouveau : « une marche lente mais vivante n'est jamais arrêtée, **hors la garde de débit** (plan, point 5) ; ».

**K5** — « Marqueurs à remplir avant le scellement », fin, et calendrier de lundi :
- ancien : « `<<LIGNE_GO_BBIS>>` (ligne de `registres/go.md` sur mot de Lazar) ; `<<MOT_LAZAR_ECART_CODE>>` ; »
- nouveau : « `<<LIGNE_GO_BBIS>>` (ligne de `registres/go.md` sur mot de Lazar ; **sans mot au scellement : « en attente ; la ligne `GO-BBIS`, inscrite après le scellement sur le mot de Lazar, fixe la coupure, au plus 40 USD ; aucune création sans elle »**) ; `<<MOT_LAZAR_ECART_CODE>>` (**sans mot au scellement : « en attente ; sans le mot de Lazar avant `GO-BBIS`, `CODE-BBIS` n'est pas inscrite et B bis n'est pas jouée »**) ; ». Mettre la même précision à la Liste d'arrêt (ligne Dépense) et au nœud 4.

**K6** — petites précisions (sans effet sur états, seuils, puissance) :
- plan, point 5 : « après les 20 premiers apprentissages de la marche » → « après les 20 premiers apprentissages de la marche, **pris dans un ordre d'exécution qui entrelace les deux familles (dix de chaque)** » ;
- Liste d'arrêt, repli de MC : « (avant l'instance) » → « (MC se calcule à la lecture, sur processeur : l'instance n'attend pas ce relevé) » ;
- Seuil, épreuve de niveau : ajouter « son coût de calcul sur processeur est écrit avec le résultat ; la puissance à 99,5 % est recalculée par une version neuve du script de calculs si ce niveau est retenu » ;
- devis v2 (Montants) : écrire « disque haut : 0,08 × (5,65 + 1,0 h) » avec la raison du « + 1,0 h » (ou le retirer) ; `conception-etape-b-bis-v2.md` l. 50 : « égalité aux aires du fichier de T0.6 exigée » → « exigée si le fichier existe » (pièce de conception, hors texte scellé) ;
- envoi des nœuds : une ligne sur « tâches témoins » rendu en nul de réétiquetage (point a de (2)).

## Ce qui est écrit, ce qui ne l'est pas

Les majeurs M1, M3, M4, M7 sont corrigés exactement comme dit ; M2, M5, M6, M8 le sont avec les restes ci-dessus. La vérification ne se prononce pas sur le fond des règles de l'étape B ni sur le code (inexistant), seulement sur le différentiel et sur la fermeture de la table.

- **Fin** (UTC, `date -u`) : voir ligne suivante.
- Fin (UTC, date -u) : 2026-11-14T12:14:24Z
