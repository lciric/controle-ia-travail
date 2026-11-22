# Inventaire du départ — course « nouvelles attaques » à cinq espèces — v1

Lecture seule, 2026-11-22 vers 08:25Z. Aucun appel, aucune dépense, aucun commit. Sources : branche `lot/compte-organisme-v1` (HEAD `ddc02baa`, poussée sur `origin/lot/compte-organisme-v1`), dossier `docs/notes/ideation-nouvelles-attaques-v1/` ; `main` lu dans `/home/user/main-lecture` (HEAD `e5c0cb99`) : `prereg/ideation-nouvelles-attaques-v1/`, `registres/decisions.md` (R-4300 à R-4798, lignes filtrées), `registres/scellements-v1.md` (lignes NA), `registres/go.md` (trois lignes : GO-2026-11-20-67, GO-2026-11-21-30, GO-2026-11-22-35), `scripts/lancer_course_auto_conception_v9.py` (lu par extraits). Rien ouvert sous les chemins interdits.

## Verdict

**La course ne peut pas partir aujourd'hui.** Les trois textes de valeurs sont scellés, mais le véhicule n'est construit qu'aux lots 0 à 6 et 10 a (sur la branche, pas sur main) ; les lots 7, 8 et 9 (mesures, lanceur de course, épreuve des témoins et sonde de refus) n'existent pas ; l'additif du véhicule, les témoins scellés, les consignes scellées du portier et des juges, le tirage scellé et la pièce de relevés n'existent pas. Il n'y a donc ni épreuve des témoins ni sonde de refus. Ces deux étapes conditionnent le départ selon GO-30.

## 1. Préalables, un par un

### 1.1 Textes de la course (main, tous scellés, compagnons vérifiés « OK » par `controle_ia.scellement verifier`)

| pièce | chemin (main) | sha256 court | ligne de `registres/scellements-v1.md` |
|---|---|---|---|
| préenregistrement court v9 | prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v9.md | 864f39a7ecd4 | l. 65, PREREG-COURT-NOUVELLES-ATTAQUES-V9, 2026-11-20T13:21:20Z |
| additif 1 v5 | …/additif-1-preenregistrement-court-v9-mode-tenu-a-l-ecart-et-retrait-espece-6-v5.md | 9f731795cd8b | l. 68, ADDITIF-1-PREREG-COURT-NOUVELLES-ATTAQUES-V9-V5, 2026-11-20T14:37:11Z |
| devis v11 | …/devis-course-nouvelles-attaques-v11.md | 205e08f23ef9 | l. 69, DEVIS-NOUVELLES-ATTAQUES-V11, 2026-11-20T14:37:11Z |
| **complément de valeurs, lot 1, v3** | …/complement-valeurs-preenregistrement-court-v9-lot-1-v3.md | **b4ef87dc6d5c** | **l. 71, COMPLEMENT-VALEURS-NOUVELLES-ATTAQUES-V9-LOT-1-V3, 2026-11-20T14:52:59Z** (R-4307) |
| additif 1 au complément v3 (espèce 3 sur Minuit), v2 | …/additif-1-complement-valeurs-preenregistrement-court-v9-lot-1-v3-espece-3-sur-minuit-v2.md | ce76e0d6a0a6 | l. 77, ADDITIF-1-COMPLEMENT-V3-NOUVELLES-ATTAQUES-V2, 2026-11-21T06:23:13Z (R-4356) |

Le complément est donc **scellé**. Selon R-4303, la **pièce de relevés** scellée par la mère « vaut complément scellé au sens de GO-67 ». **Cette pièce n'est pas scellée** : aucune ligne dans scellements-v1.md. Elle est en deux temps (avant et après les lignes à part), avec ses cinq lignes à libellé fixe (additif au complément, § 6, l. 138-144) plus une sixième, la ligne de l'état 1 de la colonne (R-4442). Le programme de calcul de R-4306 reste à mettre à jour et à contre-lire.

Accords : GO-2026-11-21-30 (go.md l. 629 : 456 USD, échéance 27 novembre, conditions de départ de GO-67) ; GO-2026-11-22-35 (go.md l. 722, 2026-11-22T08:16:57Z, commit 4bc46139) : départ immédiat demandé, règle de repli neuve, écart aux textes scellés déclaré et accordé par Lazar. Aucune ligne du registre des décisions n'applique encore GO-35 (la dernière est R-4798, 08:17:17Z).

### 1.2 Épreuve des témoins : **non passée**
- Seul le gabarit existe : `docs/notes/ideation-nouvelles-attaques-v1/inventaire-allumage-v1/gabarit-temoins-plantes-course-nouvelles-attaques-v1.md` (branche, a84de0bf3168, R-4370).
- Ni les témoins écrits, ni les témoins scellés, ni leur table : non trouvés (aucune ligne de scellement).
- Le programme `epreuve_temoins` (lot 9) n'existe pas. `scripts/epreuve_temoins_auto_conception_v9.py` (main, 5be161fa35e3) est celui de la course d'auto-conception. Il a été versé comme base, il n'est pas l'épreuve de cette course.
- Ligne à part : 5 USD, rôles Claude (portier, juge de l'espèce 3) sur Minuit, juge de l'espèce 1 sur le deuxième relais (complément v3, l. 120-127).

### 1.3 Sonde de refus : **non passée**
- Le programme `sonde_refus` (lot 9) est non trouvé. Aucun résultat.
- Ce qui existe : la *sonde minimale de la clé Luc* (`sonde-cle-luc-20261120/journal-relais-sonde-luc.jsonl`, branche, c5beeaf82a69), dite « faite » par la V9 l. 411. Ce n'est pas la sonde de refus des espèces 1 à 5 (ligne à part de 1 USD).
- R-4444 : le jeu du lot 4 derrière le vrai relais attend une sonde bornée à 0,01 USD, sous une ligne de GO à part. Aucune trace qu'elle ait été jouée.

### 1.4 Véhicule NA-1, lot par lot

Tout le code du véhicule est **sur la branche `lot/compte-organisme-v1` seulement**. Aucun des dossiers ci-dessous n'est sur main (`git cat-file` négatif). Sur main il n'y a que la base (commit 61987a3a, fusion 623a1c0d, R-4385) : dossier orchestrateur-v68, lanceurs v9 et v10, épreuve des témoins v9. Le vérificateur est partout « modèle S », neuf. Aucun lot n'a de ligne au registre de scellement.

| lot | dossier (branche, sous docs/notes/ideation-nouvelles-attaques-v1/) | livré | vérification | sha256 court (vérif. ; manifeste) |
|---|---|---|---|---|
| conception v5 | conception-vehicule-v5/ | oui | contrôle « Conforme » (R-4442) | 4b369004733f ; conception 1b7f6822af20 |
| 0 (relevé) | lot-0-vehicule-na-v1/ | oui (relevé, sans code) | contre-lu avec la v2 (R-4415) | relevé 10ac79ecb0e0 |
| 1 et 2 | lots-1-et-2-vehicule-na-v2/ | oui | « Conforme », S (R-4465) | 674996b42d7c ; c4b209a8e315 |
| 2 (garde de motifs) v3 → v5 | lot-2-vehicule-na-v3/, lot-2-vehicule-na-v5/ | v5 en vigueur (v4 refusée au commit, R-4500) | v3 « Conforme » 9816b6e2dfab ; v5 « Conforme » | e840bf334110 ; b0f603a5ff79 |
| 3 v1 → v3 | lot-3-vehicule-na-v3/ | v3 en vigueur | « Conforme » (v1 3fe6c96322dc, v2 20b915005152, v3 a1de709252cc) | a1de709252cc ; 844b36f7e535 |
| 4 (surcharge d'`appel`, adaptateur Claude) | lot-4-vehicule-na-v1/ | oui | « Conforme », trois nœuds pour la mère | 3c8d1aa2d67b ; 5072e1927ac5 |
| 5 (lecteur, contrat, portier, registre) | lot-5-vehicule-na-v1/ | oui | « Conforme » | 7742a6490a14 ; f8fcb6285a37 |
| 6 (course, configuration, lanceur de l'orchestrateur, simulation) | lot-6-vehicule-na-v3/ (v1 récupérée incomplète, v2 « À corriger » e8992a546aeb) | v3 en vigueur | v3 « Conforme » ; table d'empreintes `sha256sum -c` code 0 | 0eedf5f9cfd7 ; 20c4065c585e |
| 7 (mesures, export, quarantaine) | — | **non trouvé** | — | — |
| 8 (lanceur de course `lancer_course_nouvelles_attaques_v1.py`, différentiel contre L9) | — | **non trouvé** (aucun commit, sur aucune branche locale, ne touche ce nom) | — | — |
| 9 (`sonde_refus`, `epreuve_temoins`, essai à blanc, mesure des consignes) | — | **non trouvé** | — | — |
| 10 a (colonne matière première, garde seule) | lot-10-a-vehicule-na-v1/ | oui | « Conforme », cinq réserves de couverture | b2e77af10732 ; df862562ec17 |
| 10 b (facultatif) | — | non écrit (hors chemin) | — | — |

Réserves ouvertes qui touchent le départ :
- Lot 6 v3 : `reserve-modele-de-menace-lot-6-v3-v1.md` (a92d3d4a9ef8). Quatre contournements par modification du programme en marche. Décision de la mère : séparation par processus, « prévue au lot suivant », non écrite. D'ici là, la réserve accompagne toute course qui ferait tourner du code d'organisme dans le même interpréteur.
- Lot 4 (vérification, § 5 et § 7) : D2 (« rien n'est ajouté à l'enveloppe ») **n'est pas tenue** par l'adaptateur seul. L'outil ajoute un bloc « # Environment » variable (1 052 à 1 080 octets), une phrase d'identité et un en-tête de facturation. Le nœud est pour la mère et l'additif. Un refus pour crédit du compte en amont n'est pas vu par le relais v2 : il est lu « cause non établie ». L'outil écrit une transcription par session sous son dossier de configuration (au lot 8 : maison de l'agent dans la sortie).
- R-4655 : un lot neuf, contre-lu, pour les corrections de la règle Google (lots 2 à 5 et 10 a, plus un audit du relais Google local). Son état est non trouvé.

### 1.5 Additif du véhicule : **non écrit, non scellé**
Aucun fichier et aucune ligne de scellement. Plusieurs pièces renvoient à lui pour leurs valeurs : R-4465, R-4479, R-4603 (arrêts à partir du n° 31), R-4442 (libellé de la sixième ligne). Il est dû scellé avant l'épinglage du lot 8 (conception v5, § 7).

### 1.6 Lanceur à utiliser
- Prévu : `scripts/lancer_course_nouvelles_attaques_v1.py` (lot 8). **Non trouvé.**
- Base du différentiel : `scripts/lancer_course_auto_conception_v9.py` (« L9 »), main, sha256 **1b47c1cf097e**…, 2 944 lignes. Il est propre à la course d'auto-conception et **ne peut pas servir tel quel** : la conception demande une table neuve des noms d'adaptateur à la place de L9 l. 539-540, et la fermeture de la fuite de L9 l. 2667-2669.
- Le lot 6 a écrit un lanceur *de l'orchestrateur* : `lot-6-vehicule-na-v3/paquet/orchestrator/demonstrations/lancer_orchestrateur_na_v3.py` (3a104c93a654). Le lanceur de course viendra l'appeler.

### 1.7 Machine
- La conception v5 (§ 1.2) retire la machine jetable du régime. Aucun serveur n'est exigé par écrit : le lanceur tourne dans un conteneur de session, avec des relais locaux (127.0.0.1) qui portent les clés.
- **Ce conteneur ne suffit pas en l'état.** L'orchestrateur de base (`lciric/ideation-organism`, commit a41b7b50) est absent : `/home/user/lciric/ideation-organism` n'existe pas. Sa lecture a été refusée une fois par le contrôle des permissions (R-4614). Le paquet v68 et les lots s'appliquent sur cette base. `bwrap` et `socat` sont absents (installés jadis chez l'organisme, R-4385, pour le bac à sable de l'outil). Présents : kit `claude_agent_sdk` 0.2.172 (celui du relevé du lot 4), outil `claude` 2.1.330 (le relevé portait sur l'outil embarqué 2.1.308), Unicode 15.1.0 sous les deux interpréteurs.
- Risque relevé : plusieurs courses ont été tuées par des redémarrages de conteneur (R-4525, R-4557, R-4796). R-4455 impose un lancement détaché, avec journal et identifiant écrits.

### 1.8 Clés, rôles, soldes

Répartition en vigueur (additif au complément, l. 54-58 et 120-144) :

| clé | rôles | part | variable attendue | présence ici |
|---|---|---|---|---|
| Minuit | juge et proposeur de l'espèce 3 ; portier et juge 3 à l'épreuve ; sondes des espèces 3 et 4 | 156,56 USD, diminuée par GO-30 de la reprise des collisionneurs (GO-2026-11-21-28) | `RR_ANTHROPIC_API_KEY_MINUIT` (L9 l. 100, 450) | présent |
| Luc | aiguilleur (portier) ; proposeur de l'espèce 4 | 125,63 USD ; il faut un reste d'au moins 212,71 (« tenu, de 1,29 USD ») | `RR_ANTHROPIC_API_KEY_LUC` (R-4368) | présent |
| Rigaud | aucun rôle (réserve du bras A, 8,35) ; tout envoi à Rigaud est un artefact de l'arrêt n° 12 | 0 | `RR_ANTHROPIC_API_KEY_RIGAUD` (refusée par L9) | présent |
| deuxième relais (Google, compte payant, la carte paie au-delà du crédit, GO-64) | juge de l'espèce 1 ; proposeurs des espèces 1 et 5 | 140,39 USD | `GEMINI_API_KEY` (R-4368, L9 l. 532) | présent (ainsi que `GEMINI_API_KEY_2`, `_3`, `_FREE`) |
| troisième relais (OpenAI, recharge automatique attestée par Lazar, R-4342) | proposeur de l'espèce 2 | 17,01 USD | `OPENAI_API_KEY` dans la liste de L9 ; le nom exact retenu pour la course est non trouvé (`OPENAI_API_KEY_2` existe aussi) | présents tous deux |

Absents ici : `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`. Aucune valeur n'a été affichée.

**Attention :** l'adaptateur Claude NA lève `CleDansEnvironnement` si une variable de clé est visible de l'orchestrateur. Le lanceur doit donc démarrer les relais avec les clés, puis l'orchestrateur sous un environnement réduit (`NOMS_PERMIS` de L9).

Soldes connus d'après les registres lus :
- Minuit : 162,56 USD au complément v3, avant les lignes à part. Ensuite viennent les dépenses des collisionneurs (4,86 USD selon R-4557, puis les reprises sous GO-28 et -45). **Reste du jour : non établi** dans les lignes lues.
- Luc : 213,999998 au complément. R-4595 : « LUC 193 USD ». R-4647 : « 39,59 USD dépensés, environ 153 restants ». Avec la réserve de l'étage 2 (88,36) libérée, la règle du complément (reste ≥ 212,71) est à recalculer à la pièce de relevés. Lue à la lettre, elle ne tient pas.
- Rigaud : 25 USD déclarés (R-4342).
- Deuxième relais : crédit relevé 60,92 EUR, compte payant.
- Troisième relais : recharge automatique, montant non relevé (R-4356).
- Somme des parts : 439,59 sous 456 (R-4356).

## 2. Ce qui manque pour lancer, dans l'ordre des dépendances

Heures de session, sans appel, sur le calendrier de la conception v5 (§ 8). Ce qui n'est pas au calendrier est estimé.

1. **Environnement** : copie de l'orchestrateur a41b7b50 (autorisation de lecture du dépôt, à Lazar : R-4614), application v68 puis des lots 2 v5, 3 v3, 4, 5, 10 a et 6 v3 par leurs programmes, `bwrap` et `socat`, contrôle de version de l'outil (2.1.330 contre 2.1.308 relevé). Environ 1 h une fois l'accès donné.
2. **Nœuds de la mère restés ouverts** : D2 (bloc « # Environment »), crédit d'amont, transcriptions de l'outil, séparation par processus (lot 6), lot de la règle Google (R-4655). Environ 1 à 3 h, plus les mots.
3. **Lot 7** (mesures, quarantaine) : environ 3 h.
4. **Additif du véhicule** (valeurs gelées, arrêts n° 31 et suivants, sixième ligne de la pièce de relevés, règle de repli de GO-35), écrit par F, contre-lu, scellé : environ 3 à 5 h. Il doit être prêt avant l'épinglage du lot 8.
5. **Lot 8** (lanceur, différentiel contre L9) : environ 6,5 h. Il dépend du lot 6 et de l'additif scellé.
6. **Pièces hors code**, en parallèle : liste des motifs déjà scellée (lot 2 v5) ; consignes du portier et des juges (D3), contre-lues, attestées « aucune recette » et scellées (3 à 4 h) ; attestation « aucune recette » n° 6 de la synthèse servie (point 6 de l'inventaire, non trouvée) ; tirage des cases et de la clé n° 30, joué deux fois et scellé (point 7 et A-1) ; témoins plantés écrits sur le gabarit, puis scellés après le tirage et la ligne de case.
7. **Lot 9** (sonde de refus, épreuve des témoins, essai à blanc, mesure des consignes), avec l'épreuve des arrêts n° 2, 3, 4, 14, 27, puis 11 et 12 étendu, et la garde de chaque arrêt sur cas sain et artefact : environ 4,75 h.
8. **Contre-lecture** du véhicule, de l'additif et de la garde ; confirmation de la répartition (D-1) ; devis final récrit sur la mesure des consignes (point 9 de l'inventaire) : environ 3 à 4 h.
9. **Pièce de relevés, premier temps** (reste de Minuit et de Luc, statuts des deux relais) : environ 1 h.
10. **Lignes à part payantes** : sonde de refus (1 USD) et épreuve réelle des témoins (5 USD), seuls appels avant la course. La sonde de 0,01 USD derrière le vrai relais (R-4444) se joue avant, sous sa ligne de GO.
11. **Pièce de relevés, second temps**, scellée, puis lettre de départ de la mère sous GO-30.

Ordre de grandeur restant : **25 à 35 heures de session** sur le chemin critique (7 → additif → 8 → 9 → contre-lecture → lignes à part), sans compter l'attente des mots. Le départ n'est pas « tout de suite ». L'échéance du 27 novembre reste tenable si rien ne se rend deux fois.

## 3. La règle de repli de GO-2026-11-22-35

Aujourd'hui, le code fait l'inverse de la règle. Un refus de classifieur est consigné et **non relancé** (arrêt n° 1). Un changement de modèle servi arrête le rôle (A2).

Où le code devrait changer (branche, `lot-4-vehicule-na-v1/paquet/orchestrator/pole/`) :

1. **`appel_garde_na_v1.py`** (d16d07bf9b10), classe du mélange `AppelGardeNA` :
   - **`_apres_retour_na`** (l. 404-445) : la branche `statut == "refus"`, hors `EVENEMENTS_MODELE`, compte l'arrêt n° 1 et rend « arrêt n° 1, consigné, non relancé », ou lève `ArretClassifieurNA`. Le repli doit se brancher ici : refus de raison « refusal », puis rejeu sur `claude-opus-4-6`, puis sur `claude-sonnet-4-6`, chaque repli consigné (modèle demandé, modèle servi, catégorie). La même fonction tient le contrôle A2 `na_servis` (l. 411-414 : « modèle servi changé entre deux appels du rôle »). Ce contrôle doit admettre le modèle de repli déclaré, sinon un repli réussi déclenche A2 sur l'appel suivant. Les listes `EVENEMENTS_MODELE` (l. 71, dont `system.model_fallback`) et `EVENEMENTS_CLASSIFIEUR` (l. 75, dont `system.model_refusal_fallback`) sont aussi à revoir.
   - **`appel`** (l. 327-402) : un rejeu est un envoi neuf. Il doit repasser les pas 2 à 5 (part de la clé avec le pire du modèle de repli, garde de motifs, ligne « envoi » au journal, égalité), puis `super().appel(..., modele=…)`, avec son coût ajouté au cumul. Le plus sûr est une boucle sur les modèles dans `appel`, non un rejeu caché dans l'adaptateur.
2. **`adaptateur_claude_na_v1.py`** (38baa2061d07) : `construire_options_na` (l. 49-60) hérite de `construire_options` du kit, qui fixe « aucun repli de modèle » (docstring l. 10). `lancer` (l. 103-131) appelle `verifier_modele_reel(modele)` du kit. Ce contrôle doit admettre les deux identifiants de repli. On peut aussi passer par l'option de repli du kit (événement `system.model_refusal_fallback`), mais elle se heurte au même « aucun repli ».
3. **Hors du dossier** : `adaptateurs.py` du kit (orchestrateur a41b7b50, non présent ici : `verifier_modele_reel`, `construire_options`, `_executer`, contenu non lu). Ensuite le barème et le contrôle de modèle du relais Claude (`pole/relais_reel_v2.py`, épinglé par L9 l. 515 ; le relais compte `refus_modele`), les pires par rôle et les parts (coût au tarif du modèle de repli), la configuration de course du lot 6 (`a11_modeles: []`), la ligne de génération du lot 6 (comptes « rapportés à part ») et le lot 8 (modèles permis, épinglage).

**Pièces scellées touchées** :
- La règle contredit la V9 scellée (864f39a7 : l. 372, arrêt n° 1 « non relancé » ; l. 98).
- Elle touche les coûts et pires du complément v3, de son additif et du devis v11 (« compté dans le devis »).
- GO-35 déclare cet écart et l'accorde. Il reste à l'écrire dans une pièce : additif du véhicule, ou additif à la V9 contre-lu.
- Le code des lots 4 et 6 n'est pas scellé : il est seulement vérifié « Conforme ». Le changer demande une v2 du lot 4, avec nouvelle vérification S, et sans doute une v4 du lot 6.
