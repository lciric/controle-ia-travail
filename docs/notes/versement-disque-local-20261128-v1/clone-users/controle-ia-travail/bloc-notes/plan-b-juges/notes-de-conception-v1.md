# Notes de conception — préenregistrement du plan B des juges (T0.5), brouillon 1 — v1

- **Rédacteur** : sous-agent neuf, en routine sur processeur. Il n'a écrit ni le pilote, ni le complément des notations, ni leur code, ni les verdicts, ni l'audit.
- **Date** : 2026-10-19, vers 15:15 UTC.
- **Brouillon accompagné** : `T0.5-plan-B-juges-v1-brouillon1.md` (même dossier du bloc-notes, hors du dépôt).
- **Discipline** : aucune écriture dans le dépôt ni dans un registre ; aucun commit ; aucune commande Vast.ai ; aucun appel payant ; aucun accès au réseau. Aucun texte de réponse de juge, d'action, d'ensemble ou d'énoncé n'a été affiché : seulement des comptes, des longueurs, des drapeaux et des durées. Les scripts de calcul ont tourné par `python3 -I -B` (aucun fichier compilé écrit dans le dépôt), sans importer de module du dépôt. Aucun refus du filtre de sûreté.

## 1. Ce que la commande demandait, et où c'est traité

| demande | où |
|---|---|
| 1. rubrique simplifiée définie, justifiée par les modes d'échec mesurés ; invite complète en annexe ; ce qui change par rapport à H.4 | « Plan d'analyse », table « Rubrique S1 : choix et justification » ; annexe A (texte complet) ; annexe B (différences) ; « Métrique » (règle de lecture) |
| 2. requalification : décomposition courte, seuils, table « retenue » ou « nœud », effets sur T0.6 et T0.8 | « Métrique », « Seuil » (règle du pilote recopiée), « Critères de lecture gelés » A et B |
| 3. rejeu : mesure gelée qui sépare propriété du modèle et défaut du chemin, critère chiffré, lecture de chaque issue, même étape, aucun réglage changé | « Hypothèse » 2, « Métrique » (rejeu), « Seuil », « Critères de lecture gelés » C |
| 4. prédictions chiffrées, seuils, plan d'analyse, critères gelés, liste d'arrêt ; aucun chiffre de l'état de l'art non vérifié ; graines par `SeedSequence` | sections du gabarit ; « Graines (R9) » |
| 5. devis borné depuis les coûts relevés ; processeur ou carte | « Plan d'analyse », « Calcul et devis » |
| 6. code à écrire ou réutiliser, tests (R5) | « Code à écrire et tests (R5) » |
| 7. questions à décider, marquées « nœud » | « Questions à décider (nœuds) » |

## 2. Choix et options écartées

### 2.1 Rubrique S1

**Retenu** : quatre critères (SPECIFICITY, COVERAGE, RIGOR, FEASIBILITY), une seule échelle entière de 0 à 5, ancres courtes, notes en tête à forme fixe, une phrase de justification d'au plus 40 mots, consigne d'arrêt ; H.3 inchangé en message système ; même corps que b0.

Pourquoi, mode d'échec par mode d'échec (comptes du verdict complémentaire, section 3.5, l. 220-223, et de l'audit, l. 139-149) :
- le 3B échoue surtout par des notes hors échelle (107 réponses ; 96 n'ont que ce défaut), surtout des 4 ou 5 sur des échelles de 0 à 3 ou de 0 à 4 (audit, l. 253). Une seule échelle de 0 à 5 rend presque toutes ces valeurs licites ;
- le 8B échoue par la troncature (60), les notes absentes (55) et les demi-points (47). Les notes en tête et une sortie courte évitent le long texte qui dégénère avant le bloc final (59 des 60 tronquées dégénèrent, audit l. 169) ; la règle écrite « nombre entier » vise les demi-points ; quatre lignes au lieu de dix réduisent les absences ;
- les notes en tête suivent ce que fait déjà le 3B (152 fois sur 168, audit l. 177).

**Écartés** :
- **juge sans rubrique, une note de 0 à 100 (H.5, annexe C.2 de l'article, p. 18-19)** : le nombre tiendrait en un jeton (R-067), mais l'article dit que sans l'étalonnage détaillé les juges notent trop haut et trop peu varié (« scorer collapse », p. 29, phrase vérifiée sur le PDF) ; une note globale perd aussi la sensibilité par critère aux familles de sabotage ; et ce ne serait plus une « rubrique simplifiée », mais une autre variante de juge ;
- **dix critères sur une échelle uniforme** : plus de lignes à écrire, donc plus d'absences ; les pénalités négatives restent une échelle à part ;
- **trois critères** : perte d'un critère lié à une famille de sabotage ;
- **H.4 gardée, avec seulement les notes en tête et une borne de longueur** : les échelles hétérogènes, premier défaut du 3B, resteraient ;
- **courte analyse avant les notes** (« au plus trois phrases, puis les notes ») : risque de dérive et de dégénérescence avant le bloc ; lecture moins robuste. Contrepartie acceptée : le juge ne raisonne plus par écrit ; la décomposition dira si le bruit monte ;
- **modifier H.3** (son étalonnage parle de « 3/5 ou 2/4 ») : H.3 est une « invite autre que la rubrique », réglage gelé sans décision de Lazar. S1 s'aligne sur la moitié « 3/5 » ;
- **abaisser le plafond de 3 072 jetons** : réglage gelé ; la longueur n'est bornée que par la consigne.

**Choix des critères et usagers** : les quatre critères gardés couvrent la qualité générale et les trois familles de sabotage du programme (contrôles : RIGOR ; directions : COVERAGE, qui reprend la non-pertinence ; coût : FEASIBILITY, déjà critère d'allocation des ressources dans H.4). Ce choix fixe ce que voit la « note d'utilité visible » de T0.6 : question Q7 laissée au contre-lecteur (routine selon R-212 ; « proposer avec recommandation » s'il y voit un concept de T0.6 ou de T0.8).

**Passage de 0-4 à 0-5 (RIGOR, FEASIBILITY)** : niveaux 0 à 3 de H.4 gardés ; le niveau 4 de H.4 partagé entre 4 (contrôles soignés ; ressources justifiées) et 5 (exceptionnel). COVERAGE prend au niveau 0 « most of them are off-topic » (pénalité IRRELEVANCE de H.4, niveau −2).

### 2.2 Lecture d'une réponse S1

**Retenu** : première occurrence de chaque critère ; une valeur contradictoire plus loin est une anomalie ; nom sans tenir compte de la casse ; valeur lue par la fonction gelée `lire_une_note(brut, 0, 5)`.

**Écartés** : la dernière occurrence (règle de H.4, faite pour un bloc final : ici le bloc vient en tête, une répétition tardive serait souvent du texte qui dérive) ; une lecture tolérante qui ramène une note hors échelle à la borne (« jamais remplacée ni arrondie », `rubrique.py` l. 7-8 ; R1) ; exiger que la réponse commence par la première ligne (trop strict pour un préambule anodin, sans gain d'univocité). La casse est tolérée parce qu'elle ne crée aucune ambiguïté (l'audit a compté 4 réponses du 8B et 1 du 3B rejetées pour la seule casse sous H.4, l. 135).

### 2.3 Règle de troncature

**Retenu** : une réponse sans jeton de fin reste incomplète, même avec quatre notes lisibles en tête (CL-9, pilote l. 83).

**Écarté** : accepter les notes d'un bloc complet suivi d'un texte coupé. La raison de CL-9 (un bloc final coupé peut mêler notes d'analyse et notes finales) ne vaut plus pour un bloc en tête ; mais changer la définition de « réponse incomplète » changerait le sens de la règle gelée du plan B réutilisée telle quelle, après avoir vu les résultats de H.4. La borne de longueur par la consigne doit rendre la troncature rare ; une sensibilité descriptive est rapportée sans effet.

### 2.4 Requalification : « décomposition courte » et seuils

**Lecture retenue de « courte »** : la décomposition du pilote (A, B, C), où seule la notation est refaite (pilote, l. 184 : « seule la notation est refaite ; coût : une étape de notation »), sur les mêmes 60 tâches.

**Écartés** : moins de tâches (la règle gelée des 48 tâches complètes ne tiendrait plus : il faudrait un seuil nouveau, donc un écart) ; le « plan enrichi » (C et D notés deux fois), déjà écarté au pilote (l. 135).

**Seuils** : la règle du plan B du pilote, recopiée, appliquée par `lecture_juge`. « Rubrique gardée » se lit « S1 retenue » ; « plan B » et « nœud » se lisent « nœud » (aucun plan C n'existe).

**Conséquence calculée, à connaître avant le run** (question Q3) : 48 tâches complètes sur 60, c'est 80 % ; si les réponses manquent indépendamment, il faut au plus 1 − 0,8^(1/3) ≈ 7,2 % de réponses incomplètes. Une incomplétude entre 7 % et 20 % donne en général « nœud » par la règle des 48 tâches, sans plan B par l'incomplétude. D'où les prédictions PB1 et PB2 à 5 %.

### 2.5 Garde en ligne de la requalification

**Retenu** : la garde des épisodes de l'agent au pilote (99e centile ≤ 0,2, contrôle négatif), appliquée à une rangée par lot des notations S1, en garde différée, par la fonction gelée `jouer_episodes` et un adaptateur d'environnement de notation. Elle certifie les notations mêmes qui sont lues.

**Écarté** : aucune garde (comme au pilote pour les juges, l. 155) : c'est précisément le trou que nomme la réserve 1 du verdict complémentaire.

**Lecture** : garde contraire ou contrôle négatif contraire : nœud (comme « garde en ligne déclenchée » au pilote, l. 186) ; contrôle négatif « non concluant » (moins de 10 rangées comparables) : réserve (comme au pilote, l. 187).

### 2.6 Rejeu de la cause profonde

**Idée** : séparer « propriété du modèle » de « défaut du chemin » revient à vérifier que le chemin du harnais calcule, pas à pas, ce que calcule la bibliothèque pour le même modèle sur les mêmes jetons, dans le domaine des juges. Si c'est le cas, le tirage se fait sur la bonne loi à chaque pas, et tout ce qui en sort (dégénérescence comprise) est le comportement du modèle sous ces réglages.

**Retenu : le dispositif de T0.4 v3, étendu au domaine des juges** :
- palier de production (demi-précision, noyau par défaut, lots de 8, graines du pilote) : la garde du pilote (99e centile ≤ 0,2, contrôle négatif) sur 16 rangées longues ; elle comble exactement le trou nommé par l'audit (l. 195) ;
- palier du chemin (simple précision, poids convertis sans perte) : écart maximal ≤ 3e-3, contrôle négatif, et contrôle positif D1 (positions décodées décalées de +1, paramètre `decalage_positions` qui existe déjà dans `generer_lot`) : la logique du chemin (positions, remplissage, cache, masque) s'établit là, comme la phase « chemin » de T0.4 v3 ;
- repère de précision (passe en demi contre passe en simple précision, mêmes jetons) et rapport ρ ≤ 3, comme T0.4 v3 (l. 173, l. 199, l. 292-293), pour lire un écart de demi-précision ;
- reproduction : les lots rejoués à graine égale doivent redonner les réponses scellées ; c'est mesuré (PB9), et cela relie les mesures aux réponses mêmes du plan B ;
- témoin de la bibliothèque (`generate`), descriptif.

Tout passe par des fonctions déjà gelées et éprouvées (`jouer_episodes`, `relire_crochets_lot`, `passe_unique`, `ecart_equivalence`, `ecart_decale_zone_generee`, `bilan_controle_negatif`, `bilan_controle_positif`, `repere_precision`) : le code neuf se limite à l'orchestration et à un adaptateur.

**Lots** : tirés par graine parmi les lots de 8 qui portent une réponse scellée tronquée à 3 072 jetons (cadre : 21 lots du 8B ; 9 du 3B), pour couvrir le domaine long (jusqu'à 10 075 positions).

**Écartés** :
- **comparaison token à token avec `generate` à graine égale** (exemple de la commande) : la bibliothèque tire ses nombres au hasard autrement (générateur global, sur la carte, après ses propres traitements des logits) ; à graine égale, les jetons divergent dès le premier tirage, et seule une comparaison de taux reste possible, de faible puissance sur 16 rangées. Gardée comme témoin descriptif ; la comparaison exacte « à graine et réglages égaux » se fait autrement : le harnais rejoue à graine égale, et la passe avant standard de la bibliothèque recalcule les mêmes positions ;
- **comparaison de taux sur toutes les notations, avec `generate`** : coût (360 générations longues par juge) et puissance limitée pour un défaut subtil ; la comparaison pas à pas est plus fine et moins chère ;
- **écart de loi au niveau des logits** (divergence de Kullback-Leibler le long des trajectoires) : grandeur neuve, sans seuil étalonné ni contrôle éprouvé dans le dépôt ; elle demanderait de capturer les logits à chaque pas ; à garder pour une version ultérieure, si la contre-lecture le demande ;
- **garde de production seule** : la sensibilité de la garde en demi-précision au défaut D1 n'est éprouvée nulle part (T0.4 v3 éprouve D1 en double et en simple précision, avec des seuils serrés : `validation_reelle.py`, l. 92-99 et l. 110-113) ; sans palier du chemin, le rejeu risquerait de finir « non concluant ». Le palier en simple précision soulève la question Q1 (réglage des juges ?) ;
- **palier de logique en double précision** (T0.4 v3) : environ 64 Go de poids pour le 8B, plus des passes de 10 000 positions : ne tient pas sur une carte de 80 Go (T0.4 v3 demandait au moins 130 Gio : `validation_reelle.py`, l. 116, `memoire_carte_min_gio`) ;
- **noyau « math » au palier du chemin** (T0.4 v3) : en simple précision, pour un lot de 8 à 7 000 jetons, les scores d'attention écrits en mémoire pèsent environ 8 × 32 têtes × 7 000² × 4 octets ≈ 50 Go, plus 32 Go de poids : ne tient pas. Noyau par défaut retenu, écart déclaré ; D1 vérifie la sensibilité ;
- **contrôle positif D1 en demi-précision** : deux lots de plus par juge (environ 1 600 s en tout) ; T0.4 v3 n'en avait pas en production ; la logique s'établit en simple précision. Limite déclarée : on ne saura pas si la garde en demi-précision voit D1 dans ce domaine ;
- **bras à température plus basse ou à tirage par noyau** : changerait un réglage des juges (nœud Q4) ; hors de l'étape.

**Lecture combinée** : « propriété du modèle » exige les deux paliers sains pour les deux juges ; « défaut du chemin » dès qu'un palier montre un défaut avec ses contrôles valides ; « non concluant » sinon. Un « défaut » suspend la requalification (même chemin). Un « non concluant » laisse la réserve 1 en place.

### 2.7 Ordre des phases et échéances

**Retenu** : requalification du 8B, puis du 3B, puis rejeu du 8B, puis du 3B ; une échéance par phase (8 500, 5 500, 4 500 et 3 000 s) et l'échéance globale de 23 100 s (constante du lanceur des notations). Dans chaque rejeu, les paliers décisifs passent avant le témoin.

**Écartés** :
- rejeu d'abord, avec arrêt de l'étape si un défaut est trouvé : économie possible, mais lecture d'un résultat pendant le run, et la requalification, livrable de T0.6 et T0.8, passerait après ;
- requalification et rejeu d'un même juge à la suite (sans recharger le 8B) : gagne une à deux minutes, mais un arrêt pendant le rejeu du 8B ferait perdre la requalification du 3B.

**Risque déclaré** : l'échéance de 8 500 s laisse finir le 8B tant qu'au plus environ 17 lots sur 23 vont au plafond (lots longs mesurés de 457 à 495 s), c'est-à-dire tant qu'environ 14 % au plus des rangées ne s'arrêtent pas. Au-delà, le juge échoue sans fichier : nœud, alors qu'il aurait peut-être été retenu (incomplétude entre 14 % et 20 % ; mais, par la règle des 48 tâches, il aurait alors presque sûrement été en nœud aussi : section 2.4).

### 2.8 Graines

**Retenu** : une entropie neuve, tirée au scellement, pour toutes les clés neuves (notations S1, rangées gardées, tirage des lots du rejeu, témoin, lecture) ; les graines du rejeu sont celles, scellées, du pilote (relues et contrôlées, jamais retirées).

**Écarté** : l'entropie du pilote pour tout (comme au complément des notations). Elle est connue avant le scellement : les graines des clés neuves seraient calculables d'avance ; tirer l'entropie au scellement, comme au pilote, supprime ce risque.

**Clés S1** : `juge-S1-8B/<épisode>/passe-<p>`, pour que la fonction gelée `notes_alignees` (qui attend `juge-<juge>/…`) s'applique avec le nom de juge « S1-8B », sans collision avec les clés du pilote.

### 2.9 Devis

**Mesures** (journal de l'instance des notations ; `resume.json` ; `registres/depenses.md`) : voir le brouillon. **Estimations** : le débit de la génération en simple précision et celui de `generate` ne sont pas mesurés ; je les ai bornés par des échéances de phase. Le tirage sur le processeur, un fil, sur tout le vocabulaire, semble dominer le pas (environ 0,15 s par pas pour un lot de 8 au 8B : 10 478 s pour environ 70 000 pas) ; c'est une inférence, pas une mesure.

**Plafond** : 7,5 heures d'instance au prix plafond de 1,30 USD (9,75 USD), plus le téléchargement (au plus 1,1 USD) et 72 heures de disque arrêté (1,94 USD, montant écrit par R-215) : 12,8 USD. Attendu : 4,5 à 6 USD.

### 2.10 Code

**Retenu** : aucun module gelé modifié ; modules neufs pour la rubrique S1, l'assemblage et l'adaptateur, le lanceur et le lecteur ; la notation passe par `jouer_episodes` (et non par une copie de `noter_ensembles`) pour que la garde en ligne soit exactement celle de l'agent. Un test prouve, sur le modèle jouet, que la notation par `jouer_episodes` avec H.4 rend exactement les champs de `noter_ensembles`.

**Point technique relevé** : le contrôle du format des juges compare, au complément des notations, le format scellé du début du pilote ; ce format compte les jetons d'une conversation de contrôle qui porte la rubrique (`lancer_pilote_a.py`, `conversation_de_controle`, `controler_format`). Avec S1, le nombre de jetons change : le contrôle doit se faire en deux temps (b0 contre le format scellé ; S1 contre le gabarit complet). C'est écrit dans le brouillon.

## 3. Calculs faits pour ce brouillon (nombres seulement)

- **Fichiers de notations scellés** (`notations-8B-decisives.json`, `notations-3B-decisives.json`), champs numériques et drapeaux seulement : 180 notations par juge ; contextes de 5 261 à 7 003 jetons (médiane 6 102,5), les mêmes pour les deux juges ; réponses du 8B, médiane 1 585,5 jetons, du 3B 626,5 ; tronquées 60 et 9, toutes à 3 072 ; positions maximales 10 075 et 9 749 ; lots portant une réponse tronquée : 8B, 22 sur 23 (tous sauf le 21), 3B, 9 (lots 1, 4, 5, 6, 11, 13, 15, 16, 19) ; descriptifs : 8B 10 478,2 s, 332 183 jetons générés, pic 28,42 Gio ; 3B 4 944,1 s, 157 194 jetons, pic 16,24 Gio ; noyau « défaut de la bibliothèque » ; variante b0 partout.
- **Journal de l'instance des notations** (lignes de progression, sans compte de réponses) : lots du 8B de 457,1 à 494,9 s, sauf le lot 21 (299,3 s) et le lot 23, de 4 notations (262,2 s) ; lots du 3B de 52,3 à 319,8 s ; tests « 763 passed in 1455.20s » ; début du script 19:10:32, run 19:36:48, fin 23:57:01 UTC ; `run.json` : chargement du 8B 127,7 s, préchargement du 3B 49,1 s, chargement du 3B 3,5 s, run 15 607,8 s.
- **Longueurs en caractères** (`travail/longueurs.py`, sans afficher de texte) : H.3 704 caractères (sans espaces de bord), H.4 19 499 ; corps des invites de juge (énoncé, classification estimée à 150 caractères, ensemble) de 8 108 à 17 533 caractères ; rapport caractères par jeton des contextes H.4 de 5,084 à 5,559 (médiane 5,369).
- **S1** : 3 965 caractères (sans la fin de ligne finale) ; environ 740 jetons au rapport médian, 880 à 4,5 caractères par jeton (prudent) ; H.4 : environ 3 630 à 4 330 jetons. Contextes S1 estimés : contexte H.4 mesuré − jetons de H.4 + jetons de S1, soit environ 1 700 à 4 300 jetons.
- **Règle des 48 tâches** : 0,8^(1/3) = 0,9283 ; incomplétude au plus 7,17 % sous indépendance.
- **Devis** : arithmétique écrite au brouillon (« Calcul et devis »).

## 4. Sources lues (chemin et lignes)

- `CLAUDE.md` : règles R1 à R14, hiérarchie de décision, interdits.
- `prereg/gabarit-preregistrement-v1.md` (l. 1-43) ; `src/controle_ia/prereg.py` (l. 16-48 : sections exigées, marqueurs).
- `prereg/T0.5-pilote-8B-v1.md` : l. 3-30 (en-tête), 34-46 (hypothèse, portée, usagers), 56-72 (prédictions, P2, P3), 76-91 (métrique, score, incomplétude l. 83, alignement l. 84, décomposition l. 85-90, différence l. 91), 112, 128-137 (plan B, taux d'erreur), 138, 142-160 (plan d'analyse, juges l. 143, harnais l. 155, configuration l. 157, graines l. 160), 173 (calcul, mémoire des juges), 176-224 (table de lecture, l. 184-187, 190, 194, préséance l. 196, causes l. 198-204, audit l. 206-224), 226-249 (liste d'arrêt, l. 247), 480-505 (annexe).
- `prereg/T0.5-pilote-config-v1.json` (tout).
- `prereg/T0.5-pilote-notations-v1.md` : l. 1-36 (en-tête), 40, 44-64, 68-77, 79-102 (plan d'analyse : paramètres l. 82, graines l. 83, échéances l. 84, progression l. 85, écarts l. 87-89, manière de refaire l. 90-97, calcul l. 99, mise en place l. 100, marges l. 101), 104-131 (table, préséance, causes, relancement), 133-140 (liste d'arrêt), 144 (transparence).
- `prereg/T0.5-pilote-notations-config-v1.json` (tout).
- `docs/verdicts/verdict-T0.5-pilote-notations-v1.md` : l. 1-66 (en-tête, verdict), 126-240 (juges ; section 3.5 l. 176-224 ; table des variantes l. 203-210 ; poids des motifs l. 220-223), 264-304 (audit et effet), 306-329 (section 6), 331-352 (section 7), 354-366 (section 8), 368-379 (section 9), 381-421 (empreintes).
- `docs/verdicts/audit-R4-T0.5-pilote-notations-v1.md` : l. 1-56, 58-200 (constats ; invite b0 l. 67-75 ; règle du lecteur l. 77-80 ; défauts l. 139-149 ; lectures tolérantes l. 151-166 ; dégénérescence l. 168-175 ; ordre l. 177 ; artefact de calcul l. 186-199, limite l. 195), 201-285 (recalcul ; motifs l. 248-253), 287-337 (conclusion, ce que l'audit laisse à Lazar l. 322-326, réserves).
- `docs/verdicts/verdict-T0.5-pilote-v1.md` : l. 1-70, 219-237 (juges et durées), 333-397 (suite et réserves ; domaine de la garde l. 383-391, 99e centile maximal 0,1323 l. 385).
- `prereg/T0.4-validation-modele-reel-v3.md` : l. 42-44, 67, 105, 134-137, 173, 199, 292-293 ; `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (lignes trouvées par recherche : 13, 16, 109-110, 168-172, 330, 344-346).
- Code : `src/controle_ia/environnements/rubrique.py` (l. 1-115) ; `juges.py` (l. 1-95) ; `pilote_a.py` (l. 1-246 ; `noter_ensembles` l. 156-187) ; `lancer_pilote_a.py` (l. 1-120, 122-136, 160-266) ; `noter_pilote_a.py` (l. 1-352) ; `lire_notations_pilote.py` (l. 1-232) ; `lire_pilote.py` (l. 1-120, 240-345, 852-897) ; `analyse_pilote.py` (l. 1-233) ; `invites.py` (l. 1-50) ; `propositions.py` (l. 1-30, 69-80) ; `harnais/episode.py` (l. 1-385 ; `generer_lot` l. 74-137, positions l. 109, générateurs l. 101, tirage l. 121 ; `jouer_episodes` l. 160-275) ; `harnais/activations.py` (l. 1-225) ; `harnais/modeles.py` (l. 1-325 ; `charger_modele` l. 128-157 ; `regler_determinisme` l. 269-293) ; `harnais/formats.py` (l. 1-131) ; `harnais/validation_reelle.py` (l. 1-150, 364-543) ; `manifeste.py` (l. 1-60, 68-80, 128-139) ; `harnais/run_harnais_factice.py` (l. 58-59).
- Invites : `docs/sources/invites-2606.08892-v1/LISEZMOI.md` (l. 1-80) ; `invites/H3.txt`, `invites/H4.txt`, `invites/H5.txt` (en entier) ; `index.json` (introductions de H3, H4, H5).
- Article `docs/sources/pdf/2606.08892v2.pdf` (empreinte vérifiée `aea0f2d1…`) : p. 17-18 (annexe C.1, décomposition), p. 18-19 (annexe C.2, juge sans rubrique), p. 29 (introduction de H.4 : étalonnage contre l'effondrement), extraites par `pdftotext` dans `travail/`. Aucun chiffre de l'article n'est repris dans le brouillon (R7).
- `docs/sources/lecture-pdf-niveau1/rapport-2606.08892-v1.md` (l. 1-159) : lu pour le contexte ; aucun de ses chiffres n'est repris.
- `docs/procedures/notations-T0.5-v3/plan-lancement-notations-v2.md` (l. 1-100) ; liste de `docs/procedures/notations-T0.5-v2/` et de `scripts/`.
- `docs/decisions/proposition-P-006-T0.5-v1.md` (l. 1-45) ; `proposition-P-009-T0.6-organismes-v1.md` (l. 1-45) ; `proposition-P-010-T0.8-moniteur-par-action-v1.md` (recherche : l. 3, 12-15, 23-25).
- `docs/programme-controle-ia-v2.md` (l. 241) ; `docs/brief-claude-code-programme-complet-v2.md` (l. 158, l. 358).
- `registres/decisions.md` : R-033 (l. 63), R-047 (l. 168), R-064 (l. 201), R-067 (l. 204), R-155 (l. 292), R-160 (l. 297), R-175 (l. 312), R-204 (l. 341), R-205 (l. 342), R-206 (l. 343), R-208 à R-217 (l. 345-354) ; `registres/go.md` (l. 1-27 ; GO-2026-10-04-08 l. 16, GO-2026-10-12-02 l. 25, GO-2026-10-17-01 l. 26) ; `registres/depenses.md` (l. 47-86) ; `registres/etat.md` (l. 3, 30, 72-103, par recherche) ; dernière passation `registres/passations/2026-10-19-1435.md` (l. 8, 16, 20).
- Traces : `traces/t05-notations-20261017-235701-mDaN/journal.txt` (toutes les lignes, dont les lignes de progression) et `run.json` (durées et statuts).

## 5. Ce que je n'ai pas pu faire

- **Jetons** : aucun tokeniseur Llama n'est disponible hors ligne ; les longueurs de S1 et des contextes S1 sont estimées par un rapport caractères/jetons mesuré sur les contextes H.4. Le contrôle avant dépense devra les mesurer, et vérifier sur le tokeniseur du 3B que 0 à 5 tiennent en un jeton (R-067 ne l'a vérifié que sur le 8B).
- **Débits non mesurés** : génération en simple précision, passes uniques à 10 000 positions, `generate` de la bibliothèque. Bornés par des échéances, non mesurés.
- **Configuration de génération par défaut du dépôt du modèle** (température, tirage par noyau) : non relue (pas de réseau, et R7) ; le témoin doit la remplacer explicitement et la relire, sous garde.
- **Algorithmes déterministes et `generate`** : je n'ai pas vérifié si le tirage de la bibliothèque sur la carte est permis sous `torch.use_deterministic_algorithms(True)`. Si la bibliothèque le refuse, le témoin, descriptif, doit être consigné « impossible » avec son motif, sans masquer une panne de mémoire ni un signal ; le lanceur doit le traiter ainsi (point pour la contre-lecture).
- **Mémoire vive des offres** : non relue ; la garde des 64 Go est une estimation (captures et passes de 16 rangées à 10 000 positions, en simple précision, environ 8 Go à la fois, plus les modèles chargés sur le processeur).
- **Validateur du dépôt** : non exécuté (il aurait importé le paquet du dépôt) ; sa vérification des sections a été refaite à part : les huit sections exigées sont présentes et non vides, sans marqueur de remplissage ; la section « Contre-lecture » ne porte pas encore les deux empreintes exigées, ce qui est attendu avant la contre-lecture.
- **Qualité des notes S1** : aucune réponse de juge n'a été lue (consigne) ; je ne peux pas dire si les ancres de S1 conviennent au style des juges. La décomposition et l'audit le diront.

## 6. Fichiers de travail (bloc-notes, hors du dépôt)

| fichier | rôle | sha256 |
|---|---|---|
| `travail/S1-brouillon1.txt` | texte de l'invite S1, source de l'annexe A | `b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7` |
| `travail/longueurs.py` | longueurs en caractères et rapport caractères/jetons, sans afficher de texte | `b0aa520c7c00992c0916749c563b043dc497b2c9d6e145c4a326a83aaef7ebcc` |
| `travail/p17-18.txt` | pages 17 et 18 de l'article (pdftotext, mise en page gardée) | `14671fed11f6d1fbf8e302ead79c2782b8d9123b727a0949adf5a17dfcdf7eea` |
| `travail/p19.txt` | page 19 de l'article | `04ce6093322ca9110181949582798bab506182222f70694162184adb142f1298` |
| `travail/p29.txt` | page 29 de l'article | `46b95c558109c77fe414710f80020afc88740336025f10578f279d8cf19b35a5` |
