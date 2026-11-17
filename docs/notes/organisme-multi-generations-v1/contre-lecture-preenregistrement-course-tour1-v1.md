# Contre-lecture (règle R2) — préenregistrement de la course à plusieurs générations, brouillon 4 — tour 1, v1

- **Lecteur** : modèle C, lecteur neuf ; je n'ai écrit aucune des pièces (ni le brouillon 4, ni les brouillons 1 à 3, ni la conception, ni le code du pilote, ni le verdict, ni le devis du banc). Autre lignée que le rédacteur (modèle A).
- **Heures** (`date -u`) : début 2026-11-17 01:37:26 ; fin de rédaction 2026-11-17 01:49:30 (relevée par `date -u` juste avant le scellement).
- **Pièce lue en entier** : `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon4.md`, `678163db862978ae782e36adff0e4ce76e0cf4c4998e56bc88266b9745eb5c49` (égale à son compagnon ; 1 136 lignes).
- **Pièces lues pour la confronter** : conception v7 (`1f1b64df…`, §0 à §8 et les deux sections « Contre-lecture ») ; contre-lecture de la conception, tour 3 (`d94f75c1…`) ; brouillon 3 (`2dda3b74…`, §6, §8, §9, §10, §16 ; le reste par sondage) ; note de décision (`d2bcf581…`, Q-9) ; verdict v2 du pilote (`e64458e8…`, lu par `git show` sur la branche locale de suivi, copie au bloc-notes, empreinte recalculée égale) ; rapport du développeur v68 (`6635e43a…`, §7 en entier) et bloc des empreintes v71 (`8e76eac8…`) ; devis du banc v3 (par recherche ciblée) ; `calculs_brouillon4_v1.py` et sa sortie ; `sorties-v5/calcul-regle-v5.json` ; lignes GO-2026-11-13-01, -02, -16-08, -17-05 et R-2469, R-2492, R-2501, R-2504, R-2506, R-3001, R-3005, R-3050, R-3051 des registres.

## Verdict (une ligne)

**Corrections** : la pièce est bien construite et fidèle à la conception v7, elle n'est pas à refaire ; **quatre corrections majeures** (une règle d'arrêt qui se contredit, un banc dont le contenu n'est pas défini, une mesure de τ sous-spécifiée, une antériorité du banc que la liste d'arrêt ne teste pas) et **onze mineures** ; elle reste de toute façon non scellable tant que les marqueurs [BANC…], [COMMIT-COURSE], [BLOCS-COURSE], [RACINE], [CHAMPS-COURSE] et [CHAMPS-X2] sont ouverts (dit par la pièce).

## 1. Ce que j'ai vérifié, et qui tient

| contrôle | résultat |
|---|---|
| validateur `controle_ia.prereg.problemes` sur la pièce | liste vide : forme du gabarit tenue ; aucun marqueur « À REMPLIR » |
| empreintes citées | recalculées sur disque, **toutes égales** : conception v7, tours 1 à 3, conception v4 et sa contre-lecture, brouillons 1 à 3 et leurs lectures, note de décision, devis du banc v3, `monde_riche_v4.py`, sorties v4 et v5, calcul de la règle, scripts, gabarit, registre des GO (`c20084fb…`, inchangé), verdict v2 (`e64458e8…`), rapport v68, bloc v71, rapport v71 (`188d7910…`), trois fichiers de prédiction de MR-1 (`6a3d1444…`, `3ee96059…`, `b9032dd8…`, trouvés sous `sorties-v2/`, `sorties-v1/`, `sorties-v3/`) |
| `calculs_brouillon4_v1.py` | rejoué (`python3 -I`, sortie standard seule) : **sortie égale à `calculs_brouillon4_v1.json`** hors la version de l'interpréteur ; table des minimums à τ = 36/204 (2 sur 3, 3 sur 5, 4 sur 8, 5 sur 10, 6 sur 15, 7 sur 20, 10 sur 30) égale à celle de la pièce ; seuil du tiers (13 coupés sur 37 déclenchent l'arrêt, « au-delà de 12 ») égal ; coût par appel de C1 (2,21678 complet, 2,792996 tronqué) égal à (10,019552 − 5,585992)/2 et 5,585992/2 du verdict v2 ; chance 0,3056 = 1 − (10/12)² |
| table P0 | égale à `sorties-v5/calcul-regle-v5.json` : 0,9961 ; 0,0893 à 0,1709 à la borne haute (0,042965) ; 0,9995 à 0,9999 à 0,01 ; 0,91 à 0,96 à 0,02 ; 0,50 à 0,66 à 0,03 ; 0,14 à 0,25 à 0,04 ; 0,02 à 0,06 à 0,05 ; bascules 0,0283 / 0,0318, 0,0300 / 0,0336, 0,0463 / 0,0507 ; probabilité d'aucun monde sans tirage conforme 0,9103 et 0,666 (donc « 0,09 à 0,33 » pour au moins un). La borne haute 1 − 0,025^(1/84) = 0,042965 recalculée |
| arithmétique du plan | m = 24 + 12 + 5 + 4 + 1 + 2 = 48 ; log(48/0,05) = 6,87 ; log(48/(0,05 × 11)) = 4,47 ; T_pire = 24 + 13 = 37 ; crédits 18 + 12 + 6 × 37 × 1,5 = 363 sous 365 ; hors crédits 12 + 22,20 + 12 + 10 = 56,20 sous 57 ; X1 34,20 sous 35 |
| citations du verdict v2 | exactes : « trop propre pour l'hypothèse », phrase « Une issue P-2 favorable ne dit pas… », taux 0,21 / 0,27 / 0,09, 2 appels tronqués de la même source (553 s, 510 s, 5,585992 sur 10,019552), 73 cartes pour 14 appels, 3 lois `si_sinon` sur 42, `c = 6`, gabarit `e77d3041…` |
| aucun identifiant de modèle | recherche faite sur les noms de modèles et de fournisseurs connus du dépôt : seule occurrence, le nom de la famille de modèles à la ligne 1063 (pas un identifiant ; remarque facultative 5) |
| corrections de la conception portées | E-1 à E-9, R5-1 à R5-8, passes rapportées, G_cond, dénominateur sur les 24 mondes tirés, A0 déclenché à G = 24 comme à G < 12 : tous présents et conformes |

## 2. Conformité aux lignes de GO (point 2)

| condition (GO-2026-11-13-01 et -02, GO-2026-11-17-05) | traitement dans la pièce | lecture |
|---|---|---|
| conception de la famille revue contre-lue, avec la règle écrite d'avance | conception v7 jugée scellable (tour 3) ; règle recopiée mot pour mot (Seuil 6) | conforme |
| préenregistrement neuf contre-lu par un lecteur neuf et scellé | en cours (ce rapport) ; marqueurs listés | conforme, non achevé |
| code contre-lu : regroupement, représentant à tranche de choix appariée, réponses brutes, témoins par test | V-21, V-22, V-16, V-25 marqués [GO], « nommés un par un » | conforme ; **tout le bloc C est à écrire** (dit) |
| banc de calibration fait, n et seuils par leurs règles | ordre D-2, règle en dernier | conforme dans l'ordre ; **contenu du banc incomplet : majeure 2** |
| engagement du secret machine poussé avant la phrase | D.3, garde 35 | conforme pour la course ; **non testé pour le banc : majeure 4** |
| mondes vérifiés, empreintes inscrites ; devis revu sous le plafond ; jamais de ligne d'extension ; arrêt par identifiant | garde 28 ; « avant le lancement » 1 ; D.6 ; garde 32 | conforme |
| plafonds par rôle, parts par ligne, machine à 10 USD, essai à blanc au vrai bac | D.6, gardes 29, 32, 37 | conforme ; **le plafond de session de 2 USD de X2 n'est pas dans la ligne** (mineure 4) |
| échéance 2026-11-30 | garde 36, D.11 | conforme |
| GO-2026-11-17-05 : machine louée, secret et mondes seulement sur elle ; un seul banc complet, règle en dernier ; dénominateur = mondes tirés ; devis refait, pire cas sous 3 USD | D.2, D.3, L.0, Préalables 5 à 9 ; second cycle = nœud | conforme |

## 3. Corrections exigées

Chaque couple « ancien → nouveau » a été vérifié : l'« ancien » figure **une seule fois** dans la pièce (recherche exacte, programme sans écriture). Les tournures sont des propositions : le fond est exigé, la formule est libre si elle garde le sens.

### Majeures

**M-1. « Usage absent » est à la fois un arrêt et une mesure à part.** D.12 range « usage absent » parmi les sessions en échec (arrêt de la course, garde 13), alors que la Métrique « Coût » et W-9 disent « sans usage » compté à part, jamais estimé ; le rapport v68 (R-6 de la v67 : jetons de X1 comptés « sans usage ») montre que le cas existe, et les champs d'usage de X2 ne sont pas confirmés ([CHAMPS-X2]) : le premier appel de X2 pourrait arrêter la course alors que la dépense est bornée par le journal du relais.
- ancien : `absent, témoin d'isolement absent ou faux (garde 27).`
- nouveau : `absent du corps de la réponse **et** du journal du relais (la dépense de l'appel ne peut plus être bornée ; un « sans usage » que le journal du relais chiffre reste un appel complet, compté à part, sans arrêt : Métrique « Coût », W-9), témoin d'isolement absent ou faux (garde 27).`

**M-2. Le « banc complet » n'est défini que par les six étapes de D-2, mais le texte cite des mesures du banc qu'il ne définit nulle part.** La mesure de surdité (D.1 « Portée de C8 », L.2 PL-sourd, A6), la perte de la tranche de choix de 2 000 épisodes contre 400 (D.8 point 7), C7 sur les pièces gelées et les doublons sur paires difficiles étaient dans le brouillon 3 (§16.1 point 5) et dans le devis du banc v3 (« n, forme, f, τ, surdité ») ; le brouillon 4 les a laissées tomber de l'étape 8 des préalables. Lire PL-sourd « à la mesure de surdité du banc » est aujourd'hui lire une mesure sans définition (sentinelle, archive, nombre de graines, seuil) : la lecture gelée n'est pas complète.
- ancien : `8. **Banc complet** joué (étapes 1 à 6 de D-2, la règle en dernier), sorties poussées, machine détruite par identifiant (R10).`
- nouveau : `8. **Banc complet** joué (étapes 1 à 6 de D-2, la règle en dernier), sorties poussées, machine détruite par identifiant (R10). **Mesures du banc hors D-2 que ce texte cite** : mesure de surdité (D.1 « Portée de C8 », L.2 PL-sourd, A6), perte de la tranche de choix de 2 000 épisodes contre 400 (D.8 point 7), C7 sur les pièces gelées, doublons sur paires difficiles disjointes de celles du développement (brouillon 3 §16.1 point 5) ; chacune est **définie dans la pièce des règles du banc** (sentinelle, archive, nombre de graines, lecture), chiffrée au devis du banc, rapportée sans décider ; une mesure que la pièce ne définit pas est **retirée** de ce texte avec la phrase qui la cite.`

**M-3. Les paramètres de la simulation du banc ne sont pas fixés pour τ ni pour la règle de n.** La ligne FD se lit sur « les retenues réelles du monde (trois générations) » et la prédiction P9 compare à 36 sur 204 « sur trois générations » ; mais la règle de τ ne dit ni combien de générations sont simulées, ni à quelle valeur de P_VUE, ni comment les mondes sans tirage conforme y entrent. La règle de n juge contre « des retenues simulées d'une génération 2 » sans dire à quelle P_CACHÉE, ni comment former 8 lois quand il y a moins ou plus de 8 retenues. Ce sont des règles du banc : elles doivent être écrites ici (règle R1), puisque la pièce des règles « doit égaler » ce texte.
- ancien : `retenues, mesurée au banc sur les mondes de calibration avec le modèle de proposeurs synthétiques gelé, **à P_CACHÉE = 0** (la valeur`
- nouveau : `retenues **des trois générations simulées** (mêmes retenues et même définition de la fausse découverte que la ligne FD ; les mondes sans tirage conforme sont exclus et comptés à part), mesurée au banc sur les mondes de calibration avec le modèle de proposeurs synthétiques gelé, **à P_CACHÉE = 0 et P_VUE = 0,25** (la valeur`
- ancien : `archive de 8 lois faite des retenues simulées d'une génération 2, sans W₋ᵢ**, soit ≥ 0,5`
- nouveau : `archive de 8 lois faite des retenues simulées d'une génération 2 (génération 1 simulée **à P_CACHÉE = 0 et P_VUE = 0,25**, sur le flux de la passe qui décide ; la pièce des règles écrit comment former 8 lois quand il y a moins ou plus de 8 retenues, et ce que devient alors le monde), sans W₋ᵢ**, soit ≥ 0,5`

**M-4. L'antériorité du banc (E-7) n'est testée par aucune garde.** La conception exige que le code du banc, le modèle de proposeurs et la règle soient versés et poussés **avant** l'engagement du secret de calibration ; les préalables 6 et 7 le disent, mais la liste d'arrêt (garde 35) ne contrôle que « secret de test avant phrase ». Rien n'arrête un banc dont le code a été poussé après le secret. De plus, le contrôle des commits distants suppose un accès au dépôt privé : il ne doit pas se faire depuis la machine qui porte le secret.
- ancien : `phrase dont l'empreinte égale celle inscrite ; fichier du secret jamais écrasé |`
- nouveau : `phrase dont l'empreinte égale celle inscrite ; fichier du secret jamais écrasé ; **même garde pour le secret de calibration du banc**, avec en plus l'empreinte du code du banc, du modèle de proposeurs (P_CACHÉE = 0, P_VUE = 0,25, liste des passes) et de la règle de garde trouvée dans un commit poussé du dépôt de travail privé **antérieur** au commit de l'empreinte du secret de calibration (E-7) ; contrôle des commits fait par le lanceur **hors de la machine** (la machine ne porte aucun jeton du dépôt) |`
- ancien : `ordre inverse, empreinte absente ou non poussée, second secret sur la machine → refus de générer, code 2 (aucun monde tiré) |`
- nouveau : `ordre inverse, empreinte absente ou non poussée, second secret sur la machine → refus de générer, code 2 (aucun monde tiré) ; **code, modèle ou règle du banc poussés après le secret de calibration, ou secret de calibration réutilisé pour la course → refus de tirer les 24 mondes** |`

### Mineures

**m-1. La ligne V ignore FD.** Si la génération 1 ne retient rien, des fausses découvertes retenues en génération 2 ou 3 ne sont lues nulle part.
- ancien : `si une génération ultérieure retient une carte, la ligne P, P′ ou PL se lit **en plus** (« progrès tardif »)`
- nouveau : `si une génération ultérieure retient une carte, la ligne FD, P, P′ ou PL se lit **en plus** (« progrès tardif »)`

**m-2. Dénominateur de L.2 ambigu** (« au plus 48 » alors que chaque génération rend au plus 24 cartes et que les couples se lisent par (i, g)).
- ancien : `(au plus 24 ; au plus 48 sur les`
- nouveau : `(au plus 24 par génération, donc par couple (i, g) ; la somme des deux générations, au plus 48 sur les`

**m-3. Q-4, Q-5, Q-6, Q-8 : « figées » et « à confirmer » dans la même ligne.** R-2469 demandait la confirmation de Lazar « avec la ligne de GO » ; R-2492 ne nomme que Q-1, Q-3, Q-9 à Q-13 ; les conditions des lignes ne nomment que le regroupement (Q-8) et la règle de n (Q-5), ni le nul v8 (Q-4) ni le retirage (Q-6). La table s'intitule « figées » et la mère n'a pas à confirmer à la place de Lazar un choix que la ligne ne couvre pas.
- ancien : `**lus comme confirmés** par les conditions des lignes de GO (« regroupement », « n et seuils fixés par leurs règles ») | R-2469 ; GO-2026-11-13-01 ; à confirmer par la mère |`
- nouveau : `**non confirmés** : les conditions des lignes de GO ne nomment que le regroupement (Q-8) et la règle de n (Q-5), ni le nul v8 (Q-4) ni le retirage (Q-6) ; R-2469 demandait la confirmation de Lazar « avec la ligne de GO » ; ligne **ouverte** jusqu'à un mot de Lazar ou, à défaut, la décision de la mère consignée au registre | R-2469 ; GO-2026-11-13-01 |`

**m-4. Plafond de session de X2 présenté comme celui de la ligne.** GO-2026-11-13-02 donne 2 USD par session au proposeur X1 et seulement la part de 12 USD au proposeur X2 : pour X2, seule la part est nommée ; 2 USD est déduit (12 sur 6 sessions, marge nulle). Et la conséquence du retour de 2,34 à 2 USD n'est pas chiffrée alors que le rapport v68 la donne (Q-1 : 29 395 jetons de sortie payables à 52 000 octets d'entrée pour X1 et X2, 36 000 à 2,34 USD au pilote ; Q-6 : prix de X2 10 et 50 USD par million).
- ancien : `| proposeur **X2** | GO-2026-11-13-02 | 2 USD par session (part **12 USD** ; identifiant et prix confirmés avant l'appel) | 12,00 |`
- nouveau : `| proposeur **X2** | GO-2026-11-13-02 | la ligne ne nomme que la part de **12 USD** ; **2 USD par session déduit** (12 USD sur 6 sessions, conception v7 §5), à confirmer par la mère avec l'identifiant et le prix avant l'appel | 12,00 (marge nulle) |`
- ancien : `2 USD (ligne de GO) contre 2,34 (pilote) ;`
- nouveau : `2 USD (ligne de GO pour X1 ; déduit pour X2, dont la ligne ne donne que la part) contre 2,34 (pilote ; sorties payables de 36 000 jetons contre environ 29 000 à 2 USD, rapport v68 Q-1 ; au pire cas d'un jeton par octet, chaque 10 000 octets d'entrée de plus retire environ 2 000 jetons de sortie, soit environ 19 800 à 100 000 octets et aucun vers 197 000 : calcul du lecteur, prix de X1 supposé égal à celui de X2, 10 et 50 USD par million, rapport v68 Q-6 ; à refaire au devis de la course) ;`

**m-5. Ce que Lazar doit lire en clair omet E-2.** Le point 9 ne parle que de la règle ; MR-2 ne satisfait pas la lettre de Q-13 (c) que Lazar a retenue, et rien dans les registres lus ne montre qu'il l'ait lu sous cette forme (E-2 vient de la contre-lecture de la v4, après R-2492).
- ancien : `0,09 à 0,17 ; le banc ne garde pas contre des proposeurs qui ne masquent pas.`
- nouveau : `0,09 à 0,17 ; le banc ne garde pas contre des proposeurs qui ne masquent pas ; **et MR-2 ne satisfait pas la lettre de Q-13 (c)** (E-2 : composante invisible dans la marginale, non introuvable ; dépendance à l'archive logée dans les proposeurs), à dire à Lazar en clair avec le mot qui a retenu Q-13 (c).`

**m-6. Garde 0 : comment le code lit « GO de Lazar ».**
- ancien : `empreinte de la lecture inscrite et GO de Lazar sur elle, avant le premier appel payant`
- nouveau : `empreinte de la lecture inscrite et GO de Lazar sur elle (ligne du registre des GO lue par son GO_ID, comme la garde 36), avant le premier appel payant`

**m-7. Garde 32 : à quel instant commence l'horloge.** La machine sert aussi à l'essai à blanc, au secret, à l'attente de la phrase et à la génération des mondes, avant les 72 heures de la course ; le produit « 72 h × prix » ne couvre alors pas toute la location.
- ancien : `durée maximale **72 heures** ; 72 h × prix horaire (lu à la location, consigné) ≤ 10 USD`
- nouveau : `durée maximale **72 heures** pour la course ; (durée de préparation prévue au devis de la course, comptée dès la création de la machine : essai à blanc, secret, attente de la phrase, génération des mondes, plus 72 h) × prix horaire (lu à la location, consigné) ≤ 10 USD`

**m-8. État d'appel manquant : « sans carte ».** Le verdict v2 du pilote compte à part les appels lisibles sans aucune carte (`sans_carte`, 0 au pilote) ; D.12 et W-13 n'ont que complet, tronqué, coupé, refusé, échec.
- ancien : `- **Témoin positif par génération** (mesure) : part des appels répondus qui portent une composante autre que l'archive.`
- nouveau : `- **Témoin positif par génération** (mesure) : part des appels répondus qui portent une composante autre que l'archive.\n- **Appel sans carte** (réponse lisible, raison d'arrêt « fin normale », aucune carte admise au gardien) : état distinct de « complet » dans le relevé (le verdict v2 du pilote le compte à part), compté, **sans arrêt** ; W-13 le lit comme un cinquième état non fautif.`

**m-9. Déclaration : le commit des pièces de calcul.** Le rédacteur le signale dans son rendu (commit `1df4ae9f`, 01:35:10, par un autre processus, avant le scellement de la pièce à 01:36:20) ; la pièce dit seulement « rien committé ».
- ancien : `ni `env` ni `printenv` ; aucun fichier existant modifié ; rien committé.`
- nouveau : `ni `env` ni `printenv` ; aucun fichier existant modifié ; rien committé de ma main (les pièces de calcul ont été committées à 01:35:10 par un autre processus, commit `1df4ae9f`, avant le scellement de ce texte).`

**m-10. « Poussés » : dire où.** V-36 interdit de pousser vers le dépôt public sans mot de Lazar ; les préalables 6 disent « versés et poussés » sans préciser lequel.
- ancien : `6. **Versés et poussés** : code du banc, modèle de proposeurs (P_CACHÉE = 0, P_VUE = 0,25, liste des passes), règle de garde (E-7).`
- nouveau : `6. **Versés et poussés sur le dépôt de travail privé** (jamais sur le dépôt public de l'organisme : V-36 ; garde 35) : code du banc, modèle de proposeurs (P_CACHÉE = 0, P_VUE = 0,25, liste des passes), règle de garde (E-7).`

**m-11. Renvois au brouillon 3 sans statut.** Le texte dit « inchangé », « recopiée sans changement », « brouillon 3 §3.1 » (régularités publiques de MR-1), « §3.5 tient », « section 3.9 inchangée » sans recopier ; un texte scellé qui renvoie à un fichier non scellé doit dire ce qu'il en incorpore (règle R6).
- ancien : `| brouillon 3 de ce texte (gardé intact) |`
- nouveau : `| brouillon 3 de ce texte (gardé intact ; **ses sections 1, 3.1, 3.5, 3.6 point 4 et 3.9 et son §16.1 point 5 sont incorporées par renvoi là où ce texte les nomme « inchangées » ou les cite, et seulement là**) |`

## 4. Remarques facultatives (aucune n'est exigée)

1. **V-9** : « jamais la forte de K1 » ne couvre pas le cas où le trait de la composante de condition est le trait de K1 (8 traits, au plus 6 portent un effet) ; dans ce cas la condition est lisible dans l'archive dès la génération 0. À essayer au code, ou à déclarer.
2. **Garde 33** : elle contrôle l'empreinte du gabarit et les réglages d'effort et de réflexion, pas la borne de sortie en jetons, qui change pour X1 et X2 (36 000 au pilote, environ 29 000 à 2 USD) et décroît avec l'archive ; dire si la borne de sortie fait partie du « gabarit » dont p_c dépend (rapport v68, Q-4).
3. **Garde 31** n'inclut pas la ligne I (instrument en défaut) : un T-ELIM survivant au monde 1 n'empêche pas de dépenser le monde 2. Hérité du brouillon 3 ; à décider, pas à corriger d'office.
4. **Plan d'analyse 11 (e)** : « ce recalcul fait foi » puis « l'issue reste celle du premier calcul » ; hérité du brouillon 3 (A7), compris comme « le recalcul fait foi pour la réserve, pas pour l'issue » ; à rendre lisible dans la version finale.
5. **Ligne 1063** : la mention du nom de la famille de modèles est un nom de famille, non un identifiant ; à garder ou à retirer selon la mère.
6. **Garde 28** : sa colonne « artefact » (« aucun tirage conforme en 8 → refus ») ne vaut que pour les mondes de test ; au banc, g_r = 0 sans arrêt (D.1 le dit) ; un renvoi suffirait.
7. **Trois fichiers de prédiction** de MR-1 sont cités par nom et huit signes d'empreinte (`6a3d1444…`, `3ee96059…`, `b9032dd8…`) : j'ai retrouvé les fichiers et recalculé, les empreintes sont justes ; les chemins complets manquent à la table (règle R6).

## 5. Les huit points du rédacteur, un par un

| point | mon avis |
|---|---|
| sous-choix de τ | **nœud confirmé** : la note de décision (Q-9) ne le porte pas, R-2492 ne le nomme pas ; la part d'ensemble est le défaut recommandé par la note ; à soumettre à Lazar avant le scellement |
| lecture de « code v68 gelé » (M-1 de la conception) | la pièce suit la conception v7 (module neuf à noms neufs égal à la v4, essai R5-7), ce qui est cohérent avec la condition « code v68 contre-lu » ; mais le devis du banc v3 lit l'autre sens ; **à fermer dans la pièce des règles du banc avant le devis du banc complet** ; la phrase « la mère tranche » ne peut pas rester dans le texte scellé |
| bloc C du code entièrement à écrire | **confirmé** : le bloc écrit (rapport v68, bloc v71) est un code de pilote ; les quatre points [GO] sont à écrire, pas à contre-lire |
| règle D.12 des appels tronqués | **acceptable**, à condition de M-1 (« usage absent ») et m-8 (« sans carte ») ; elle suit le verdict v2 (deux tronqués non traités comme un arrêt) et ne choisit pas de signe ; la limite « moins de 12 cartes : génération appauvrie, sans arrêt » est sans pièce et sans conséquence sur l'issue, donc inoffensive |
| plafonds de X1 et X2 à 2 USD | bien vu ; voir m-4 : la ligne ne nomme que la part de X2 ; relever un plafond serait une dépense (nœud) |
| taille des lois servies à l'expérimentateur | **à trancher avant le gel du code** (V-26) : le rapport v68 (Q-9) donne 2 000 caractères pour 24 feuilles à ≈ 7 000 ; MR-2 permet 48 feuilles ; ce n'est pas une correction de la pièce |
| coût de C1 | chiffres recalculés, justes ; le risque réel est plus large que C1 (voir points pour la mère) |
| Q-4, Q-5, Q-6, Q-8 | voir m-3 |
| second cycle du banc | **nœud confirmé** par GO-2026-11-17-05 (« un seul banc complet ») |
| ordre des classes de fusion | **acceptable** comme proposition ; il ne sert qu'à l'étiquette de classe de D2 et à G_cond (qui compte déjà une fusionnée comme conditionnelle si un membre l'est) ; à fixer dans la pièce des règles, avant le banc |
| τ à P_CACHÉE = 0 ; seuil de 12 cartes | τ : choix cohérent avec la passe qui décide ; sa spécification est incomplète (M-3) ; 12 cartes : sans effet sur l'issue |
| publication | **nœud confirmé** (V-36, Q-10 (a)) |
| vérification courte du différentiel 2 → 3 | j'ai lu le brouillon 4 en entier et comparé aux sections 6, 8, 9, 10 et 16 du brouillon 3 : **aucun changement non annoncé** trouvé hors ceux de la table B4-1 à B4-15 ; la réserve est levée pour ce qui est de ces sections, pas du reste du brouillon 3 (sondage seulement) |

## 6. Points pour la mère (ce que la session mère doit trancher ou savoir)

1. **Verdict : corrections.** Quatre majeures et onze mineures, en couples exacts ci-dessus ; un brouillon 5 par programme, comme pour la conception ; puis un second tour, plus court, sur le différentiel.
2. **Mots de Lazar nécessaires** : (a) sous-choix de τ ; (b) Q-4 et Q-6 (et l'étendue de la confirmation de Q-5, Q-8) ; (c) lecture d'E-2 (MR-2 ne satisfait pas la lettre de Q-13 (c)) ; (d) tout relèvement d'un plafond de session (dépense) ; (e) un second cycle du banc ; (f) la publication.
3. **Risque de fond, non corrigeable par la pièce** : avec 2 USD par session pour X1 et X2, la règle de calcul au pire cas d'un jeton par octet laisse environ 29 000 jetons de sortie à 52 000 octets d'entrée (rapport v68 Q-1) et environ 19 800 à 100 000 octets ; le rapport v68 estime « six arbres pleins ≈ 30 000 jetons » ; en générations 2 et 3 l'archive servie grossit sans borne écrite (au plus 1 + 24 + 24 lois de 48 feuilles). Attendu : troncatures fréquentes de X1 et X2 (génération appauvrie), ou arrêt de la garde 38 si l'entrée dépasse la borne. Ce n'est pas faux, c'est probable ; le devis de la course doit le chiffrer, et la mère peut vouloir une borne écrite sur l'archive servie (par exemple le nombre de retenues servies) **avant** le gel du code, puisque le gabarit ne change pas mais le contexte oui.
4. **Calendrier** : 13 jours jusqu'au 2026-11-30 pour : code de la course et du banc (juge, regroupement, représentant, tests de mort, oracle, lanceurs, essais, banc de mutations, contre-lecture), pièce des règles, devis, banc, lecture du banc, brouillon final, contre-lecture finale, scellement, machine, secret, course (72 heures au plus). La pièce le dit (D.11). Prolonger les lignes serait un mot de Lazar.
5. **Lettre A du rédacteur** : « déduite » dans la pièce, comme dans la v6 et la v7 ; sans pièce qui l'établisse. Mon rôle de lecteur C est celui que la mère m'a donné.
6. **La règle de garde ne garde presque rien à P_CACHÉE = 0** (probabilité de tenir au-dessus de 0,9999 ; G = 24 le plus probable) : dit partout dans la pièce, à lire en clair par Lazar avant le banc (point 9 des points ouverts, avec m-5).
7. **Le brouillon 4 ne peut pas se sceller** avant le banc, le code et la lecture du banc ; il n'y a donc pas lieu de presser la correction des majeures avant la pièce des règles du banc, mais M-2 et M-3 doivent être faites **avant** elle, puisque la pièce « doit égaler » ce texte.

## Déclaration

- **Rôle** : lecteur neuf, modèle C, sous-agent d'un script d'orchestration ; aucune autorité de décision ; je n'ai modifié aucune pièce.
- **Écrit** : ce rapport seul (scellé, compagnon `.sha256`). Au bloc-notes, hors dépôt : copies du verdict v2, du rapport v68 et du bloc des empreintes v71 tirées par `git show` des branches de suivi locales (`origin/verdict/pilote-mr2-v74-v14-v1`, `origin/prep/pilote-mr2-v1`), sans nouvelle récupération ; le rapport du développeur v71 n'a été lu que par son empreinte.
- **Incidents de ma main** : (1) pour lire le verdict et le code du pilote, j'ai lancé `git show` **dans le dépôt principal** (lecture seule, aucune variable `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`) au lieu d'un dossier neuf du bloc-notes, parce que les branches de suivi y étaient déjà présentes (aucune récupération, aucun clone, disque à 1,2 Go libres) ; (2) un premier appel du validateur de forme a reçu le texte au lieu du chemin (erreur de ma part, aucun effet) ; (3) le validateur a été lancé avec `PYTHONPATH=src` sous l'interpréteur du venv : il peut avoir écrit des fichiers `__pycache__` ignorés par git. (4) Aucune machine, aucun appel au loueur ni à un fournisseur de modèles, aucune dépense ; aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte ; aucun secret ; aucun monde ; rien lu sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque, du mode tenu à l'écart ; aucune valeur de clé, ni `env` ni `printenv` ; rien committé.
