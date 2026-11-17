# Contre-lecture (règle R2) — préenregistrement de la course à plusieurs générations, brouillon 5 — tour 2, v1

- **Lecteur** : modèle C, lecteur neuf ; je n'ai écrit aucune des pièces (ni les brouillons 1 à 5, ni la conception, ni le code du pilote, ni le verdict, ni le devis du banc, ni le programme des couples). Le rapport du tour 1 a été écrit par un autre lecteur de la même lettre ; je ne le tiens pas pour acquis : j'ai recontrôlé ses couples sur le brouillon 5.
- **Heures** (`date -u`) : début 2026-11-17 02:14:35 ; fin de rédaction : relevée par `date -u` juste avant le scellement.
- **Pièce lue** : `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon5.md`, `7100a978335893ffd3d0ae9ec142622361869621e8496be138b3f1d782f907f8` (égale à son compagnon). Sources du différentiel : brouillon 4 (`678163db…`) ; rapport du tour 1 (`57ac2055…`, empreinte recalculée égale) ; programme des couples `f87f0c90…` et son différentiel `09bf66ca…` (empreintes égales à leurs compagnons).

## Verdict (une ligne)

**Corrections** : les dix-huit couples du tour 1 sont appliqués fidèlement et le différentiel ne contient rien d'autre que l'en-tête et la section « Contre-lecture » ; **aucune majeure** ; **six mineures**, toutes de cohérence (dont trois nées de l'application même des couples) ; la pièce reste non scellable tant que les marqueurs [BANC…], [COMMIT-COURSE], [BLOCS-COURSE], [RACINE], [CHAMPS-COURSE] et [CHAMPS-X2] sont ouverts (dit par la pièce).

## 1. Différentiel brouillon 4 → brouillon 5 : rien d'autre que les couples

`diff` brut brouillon 4 / brouillon 5 : 214 lignes, en 21 blocs. Classement de chaque bloc :

| bloc (lignes du brouillon 4) | nature | conforme au rapport du tour 1 |
|---|---|---|
| 1 ; 3 ; 6 ; 8 ; 19 ; 49 (titre, statut, ordre des étapes, rédacteur, heures du brouillon 5) | en-tête | annoncé par le programme (COUPLES_EN_TETE) ; aucun chiffre du brouillon 4 touché ; heure 02:12:25 égale à l'heure d'écriture des fichiers (`ls`) |
| 104 (m-11) ; 343 (m-4, ligne X2) ; 448 (M-1) ; 454 (m-8) ; 584 et 597 (M-3, deux couples) ; 729 (m-1) ; 749 (m-2) ; 856 (m-6) ; 864 (m-7) ; 867 (M-4, deux cellules de la même ligne) ; 966 (m-10) ; 969 (M-2) ; 1010 (m-3) ; 1021 (m-4, point 5) ; 1030 (m-5) ; 1135 (m-9) | couples | **les dix-huit couples y sont, un par un** |
| 1089 ; 1099 ; 1101-1105 | section « Contre-lecture » | annoncé (phrase d'ouverture, contre-lecture 3, réponse, déclaration, « À faire ») |

Aucun autre bloc. Le différentiel scellé du rédacteur est un `diff -u` ; le mien est un `diff` brut du même couple de fichiers : mêmes blocs.

### Fidélité de chaque couple au rapport du tour 1

| couple | « nouveau » du rapport | brouillon 5 | lecture |
|---|---|---|---|
| M-1 | « …un « sans usage » que le journal du relais chiffre **reste un appel complet**, compté à part, sans arrêt… » | « …**n'est pas un échec : l'appel garde son état parmi ceux de ce point (complet, sans carte, tronqué, coupé, refusé)**, compté à part, sans arrêt… » | **retouche de forme déclarée**, même fond (aucun arrêt, compté à part) ; elle corrige un défaut réel du rapport (un appel tronqué sans usage rangé parmi les complets) ; acceptée |
| M-2 | texte du rapport | identique, caractère pour caractère | fidèle ; **liste incomplète, voir m-17** |
| M-3 (τ) | « …à P_CACHÉE = 0 et P_VUE = 0,25** (la valeur » | « …à P_VUE = 0,25 et P_CACHÉE = 0** (la valeur » | ordre inverse **déclaré**, pour que « (la valeur qui décide) » reste attachée à P_CACHÉE = 0 ; fond identique ; acceptée |
| M-3 (n) | gras fermé après « sans W₋ᵢ » | gras fermé après « génération 2 », rouvert sur « sans W₋ᵢ » | retouche de forme déclarée ; parité des `**` vérifiée sur la ligne 604 (sept, avec le gras ouvert à la ligne précédente : équilibré) ; acceptée |
| M-4 (deux cellules) | texte du rapport | identique | fidèle ; **lieu du contrôle à harmoniser, voir m-15** |
| m-1, m-2, m-3, m-4 (deux), m-5, m-6, m-7, m-10, m-11 | texte du rapport | identique, caractère pour caractère | fidèles |
| m-8 | « \n » dans la ligne | saut de ligne réel | retouche déclarée ; **conséquences non portées, voir m-12** |
| m-9 | « …avant le scellement de ce texte). » | « …avant le scellement du brouillon 4). » | retouche déclarée : la déclaration reste celle du rédacteur du brouillon 4 ; juste ; le commit `1df4ae9f` existe (2026-11-17 01:35:10 +0000, « Pièces scellées des travaux en cours »), antérieur au scellement du brouillon 4 |

Le brouillon 5 passe `controle_ia.prereg.problemes` : liste vide. Aucun marqueur de remplissage ni identifiant de modèle ajouté (la seule mention est le nom de famille de la ligne 1083, déjà signalé au tour 1, remarque facultative). Les « ancien » des corrections ci-dessous ont été comptés par programme : **une occurrence exacte chacun** dans le brouillon 5.

## 2. Vérifications refaites sur ce que les couples ont pu déranger

| contrôle | résultat |
|---|---|
| empreintes citées par les passages touchés (`57ac2055…`, `678163db…`, `f87f0c90…`, `1df4ae9f`) | égales |
| arithmétique de m-4 (plafond 2 USD ; 10 et 50 USD par million ; 52 000 octets) | 2 − 0,52 = 1,48 USD de sortie → environ 29 600 jetons, cohérent avec 29 395 ; **le point où la sortie s'annule est 200 000 octets à la borne exacte, environ 199 000 en partant de 29 395, et non 197 000 : voir m-13** |
| conformité aux conditions de GO-2026-11-13-01 et -02 et GO-2026-11-17-05 | inchangée (aucun couple n'y touche) ; la ligne X2 dit désormais que 2 USD par session est **déduit** (12 sur 6), juste ; plafonds 363 sous 365 et 56,20 sous 57 non touchés |
| R3 (aucun run visant un signe) | inchangé ; aucun couple ne touche aux prédictions ni à la lecture |
| R4 (symétrie) | inchangée ; A0 déclenché à G = 24 comme à G < 12 ; la ligne V reçoit FD (m-1) sans asymétrie |
| liste d'arrêt testable (R5) | M-4 ajoute un cas sain et un artefact à la garde 35 : testable ; **un point de lieu de contrôle à harmoniser (m-15)** ; m-6 et m-7 rendent les gardes 0 et 32 plus opératoires |
| cohérence avec la conception v7 | inchangée ; M-3 précise, sans la contredire, la règle de τ que la conception laissait au rédacteur |
| aucun identifiant de modèle | tenu (rôles C1, C2, E, X1, X2) |
| remarques facultatives du tour 1 | laissées non appliquées, comme la tâche l'exigeait ; aucune n'est promue ici |

## 3. Corrections exigées

Toutes mineures. Chaque « ancien » figure **une seule fois** dans le brouillon 5. Le fond est exigé ; la formule est libre si elle garde le sens.

**m-12. L'état « sans carte » (couple m-8) n'est pas porté par les quatre endroits qui énumèrent les états d'appel ; W-13, tel qu'écrit, listerait cinq états sans lui et ne dirait pas « cinquième » juste.** Le couple m-8 dit que W-13 « le lit comme un cinquième état non fautif », mais W-13 énumère déjà cinq états (échec compris) ; un appel sans carte, produit par le code, est donc hors de la liste du test W-13, qui le lirait comme écart (issue N). Même défaut dans la Métrique « Appels », le Plan d'analyse (point 8) et V-17. La règle de la « génération appauvrie » ne nomme pas non plus ce cas (il rend zéro carte admise).
- ancien : `| W-13 | **états des appels** (complet, tronqué, coupé, refusé, échec) :`
- nouveau : `| W-13 | **états des appels** (complet, sans carte, tronqué, coupé, refusé, échec) :`
- ancien : `compté, **sans arrêt** ; W-13 le lit comme un cinquième état non fautif.`
- nouveau : `compté, **sans arrêt** ; W-13 le lit comme un état non fautif de plus (cinq non fautifs, avec l'échec en sixième) ; ses cartes admises, zéro, entrent dans le compte de la « génération appauvrie » (« moins de 12 cartes admises » ci-dessus).`
- ancien : `Si les appels tronqués, coupés ou refusés d'une génération`
- nouveau : `Si les appels tronqués, coupés, refusés ou sans carte d'une génération`
- ancien : `- **Appels** : par proposeur et génération : complets, tronqués, coupés au plafond, refusés, en échec ;`
- nouveau : `- **Appels** : par proposeur et génération : complets, sans carte, tronqués, coupés au plafond, refusés, en échec ;`
- ancien : `8. **Comptes** (par monde et génération) : appels (complets, tronqués, coupés au plafond, refusés, en échec)`
- nouveau : `8. **Comptes** (par monde et génération) : appels (complets, sans carte, tronqués, coupés au plafond, refusés, en échec)`
- ancien : `| V-17 | états d'appel de D.12 : complet, tronqué, coupé au plafond, refusé (sans arrêt) ; échec`
- nouveau : `| V-17 | états d'appel de D.12 : complet, sans carte, tronqué, coupé au plafond, refusé (sans arrêt) ; échec`

(Le compte « cinq non fautifs » de la deuxième paire : complet, sans carte, tronqué, coupé, refusé.)

**m-13. Le chiffre « aucun vers 197 000 » est faux de quelques pour cent ; il vient de mon propre calcul au tour 1 (erreur du lecteur du tour 1, non du rédacteur).** Avec 10 USD par million en entrée (un jeton par octet au pire) et 50 en sortie, la sortie payable s'annule quand l'entrée coûte 2 USD, soit **200 000 octets** ; en partant de 29 395 jetons à 52 000 octets avec 2 000 jetons de moins par 10 000 octets, on tombe à zéro vers **199 000**. Le rédacteur l'a vu et l'a laissé ; un chiffre de pièce scellée ne se laisse pas faux (R6).
- ancien : `soit environ 19 800 à 100 000 octets et aucun vers 197 000 : calcul du lecteur`
- nouveau : `soit environ 19 800 à 100 000 octets et aucun vers 199 000 (200 000 à la borne exacte de 2 USD d'entrée au prix supposé) : calcul du lecteur du tour 1, refait au tour 2`

**m-14. Deux phrases sur les mondes sans tirage conforme se contredisent après M-3.** La règle de n dit qu'ils « ne comptent qu'au dénominateur de la règle de garde » ; la règle de τ (M-3) dit qu'ils sont « exclus et comptés à part ». Les deux sont compatibles (comptés à part, au rapport, sans entrer dans une statistique), mais la première phrase, lue seule, interdit le décompte à part.
- ancien : `ne comptent qu'au dénominateur de la règle de garde.)`
- nouveau : `n'entrent que dans le dénominateur de la règle de garde, et sont comptés à part au rapport pour n et pour τ.)`

**m-15. Après M-4, le lieu du contrôle des commits est dit hors de la machine pour le secret de calibration, mais D.3 dit « le code refuse de générer » pour le secret de test, sur la machine qui, selon la même garde, ne porte aucun jeton du dépôt.** Le contrôle des commits distants ne peut pas se faire depuis la machine qui génère ; la phrase de D.3 doit dire qui refuse.
- ancien : `**Le code refuse de générer** si l'empreinte du secret`
- nouveau : `**Le code refuse de générer** (le contrôle des commits est fait par le lanceur hors de la machine, qui ne porte aucun jeton du dépôt, comme pour le secret de calibration, garde 35 ; la machine ne génère que sur l'ordre du lanceur) si l'empreinte du secret`

**m-16. Q-4, Q-5 (étendue) et Q-6, devenus « non confirmés » (couple m-3), n'ont ni point dans « Points ouverts » ni ligne dans la table des marqueurs : la pièce dirait « ligne ouverte » sans que rien ne l'oblige à se fermer avant le scellement.** (Constat du rédacteur, retenu.)
- ancien : `un second cycle est une dépense nouvelle (nœud).`
- nouveau : `un second cycle est une dépense nouvelle (nœud).
11. **Q-4 (nul v8), Q-6 (retirage automatique) et l'étendue de Q-5 et de Q-8** : non confirmés par les conditions des lignes de GO (table « Tranchées ») ; mot de Lazar, ou, à défaut, décision de la mère consignée au registre, **avant le scellement**.`
- ancien : `| sous-choix de τ ; lecture de « code v68 gelé » ; taille des lois servies |`
- nouveau : `| sous-choix de τ ; lecture de « code v68 gelé » ; taille des lois servies ; Q-4, Q-6 (et étendue de Q-5, Q-8) non confirmés |`

**m-17. La liste du couple M-2 ne nomme pas deux autres mesures que le texte attribue au banc sans les définir** (constat (1) du rédacteur, retenu : même principe que M-2, « une mesure que la pièce ne définit pas est retirée » ; la ligne 272 dit « fréquences déformées par les rejets, mesurées au banc et déclarées » ; D.8 point 4 et V-21 renvoient le coût du calcul de d_nul à 48 feuilles « à mesurer au banc »).
- ancien : `doublons sur paires difficiles disjointes de celles du développement (brouillon 3 §16.1 point 5) ;`
- nouveau : `doublons sur paires difficiles disjointes de celles du développement (brouillon 3 §16.1 point 5), fréquences des sortes déformées par les rejets (D.1 « Régularités »), coût du calcul de d_nul à 48 feuilles (D.8 point 4, V-21) ;`

## 4. Remarques facultatives (aucune n'est exigée)

1. **M-1, retouche** : la nouvelle tournure range l'appel « sans usage » chiffré par le relais parmi « les états de ce point » sans lui donner d'état propre ; c'est cohérent avec la Métrique « Coût », qui le compte à part ; rien à changer.
2. **Ligne 1083** : le nom de la famille de modèles (déjà vu au tour 1, remarque 5) ; à garder ou retirer selon la mère.
3. **m-4** : le prix de X1 est supposé égal à celui de X2 (dit dans le texte) ; à confirmer à la location, avant l'appel (dit aussi).
4. **Constat (4) du rédacteur** (renvois au brouillon 3 que la liste de m-11 ne nomme pas : §3.6 en-tête de D.8, §4.1, §4.2, §16.2, sections 10 et 14, gardes 26 et 27, §19) : « et seulement là » borne les endroits, non les sections, comme le rédacteur le dit ; acceptable pour le texte d'un brouillon ; **à lever dans la version finale** par une liste exhaustive des renvois, ou par leur recopie.
5. **Constat (6) du rédacteur** (la ligne V range FD sous « progrès tardif » alors que FD ne prononce aucun progrès) : étiquette seulement ; sans effet sur l'issue ; à renommer en « lecture tardive » si la mère le veut.
6. Les points rapportés par le rédacteur à la mère (sous-choix de τ, « code v68 gelé », lettre A du rédacteur) restent à la mère ; voir plus bas.

## 5. Ce que le rédacteur du brouillon 5 déclare, et ce qui tient

- « Rédacteur : modèle A » alors que la consigne le nommait C : le rédacteur fournit sa raison (R-2982, R-2992) et demande confirmation à la mère ; je ne la donne pas.
- Sa déclaration d'incidents (récupération à profondeur 1 avec filtre `blob:none` depuis le dépôt principal, dans un dossier neuf du bloc-notes) est une lecture sans clone complet ; elle ne viole pas la lettre de la consigne (refspec, dossier neuf) ; à la mère de juger si le filtre convenait. Rien d'autre à relever.
- « Rien d'autre ne change » : **confirmé** par le `diff`.

## 6. Points pour la mère

1. **Verdict : corrections**, six mineures (m-12 à m-17), en couples exacts, appliquables par le même programme ; pas de nouveau tour sur le fond. Une vérification courte du différentiel brouillon 5 → brouillon 6 suffira (couples, en-tête, section « Contre-lecture »).
2. **Mots de Lazar nécessaires** (inchangés) : sous-choix de τ ; Q-4, Q-6 et l'étendue de Q-5 et Q-8 ; lecture d'E-2 (MR-2 ne satisfait pas la lettre de Q-13 (c)) ; tout relèvement d'un plafond de session ; second cycle du banc ; publication.
3. **Lettre du rédacteur** : le brouillon 5 dit « modèle A », avec réserve de lignée (second tour d'une autre lignée que A) ; je suis C : la réserve est levée par ce tour.
4. **Erreur de mon tour 1 à reprendre dans la correction** : « 197 000 » (m-13).
5. **Risque de fond, non corrigeable par la pièce** (inchangé depuis le tour 1) : troncatures de X1 et X2 à 2 USD, archive servie croissante des générations 2 et 3, calendrier court (13 jours) ; le devis de la course doit le chiffrer.
6. **Le brouillon 5 ne peut toujours pas se sceller** avant le banc, le code et la lecture du banc.

## Déclaration

- **Rôle** : lecteur neuf, modèle C, sous-agent d'un script d'orchestration ; aucune autorité de décision ; je n'ai modifié aucune pièce.
- **Écrit** : ce rapport seul (scellé, compagnon `.sha256`) ; au bloc-notes, hors dépôt : un `diff` brut des deux brouillons et un petit programme de comptage des occurrences des « ancien » (bibliothèque standard seule, lecture seule).
- **Lu** : rapport du tour 1 ; brouillons 4 et 5 (différentiel en entier, passages touchés et alentours, sections D.3, D.12, Seuil, Points ouverts, Préalables, Liste d'arrêt, Marqueurs, Contre-lecture) ; programme des couples (en-tête et couples d'en-tête) ; commit `1df4ae9f` par `git log` et `git show --stat` (lectures seules, dépôt principal, sans `GIT_DIR`, `GIT_WORK_TREE` ni `GIT_INDEX_FILE`) ; `src/controle_ia/prereg.py` par son appel (`problemes`).
- **Incidents de ma main** : (1) un premier appel du validateur a reçu le texte au lieu du chemin (erreur de ma part, aucun effet) ; (2) le validateur et le scellement sont lancés avec `PYTHONPATH=src` sous l'interpréteur du venv : des fichiers `__pycache__`, ignorés par git, peuvent en naître ; (3) aucune machine, aucun appel au loueur ni à un fournisseur de modèles, aucune dépense ; aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte ; aucun secret ; aucun monde ; je n'ai pas relu le code du pilote ni son verdict dans ce tour ; rien lu sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque ni du mode tenu à l'écart ; aucune valeur de clé, ni `env` ni `printenv` ; rien committé.
