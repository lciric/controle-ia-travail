# Devis — saboteur à budget (ii-b), course exploratoire — v1, brouillon 3

- **Statut** : **brouillon 3**, scellé comme brouillon, non contre-lu. Brouillon 2 (`devis-ii-b-v1-brouillon2.md`, `959df4513c0026580e5a1f8d1ffb25a3ff5afed33ed2682981c6c36c4082505a`) intact (R12). **Aucune dépense n'est engagée par ce document** ; aucune ligne de GO n'y est écrite.
- **Écrit** le 2026-11-18 vers 19:25 UTC (`date -u`) par un rédacteur neuf, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, sous le mandat `docs/notes/barreau8-iib-v1/mandat-redacteur-ordre-exploratoire-iib-v1.md` (`55b1e34824c918827a650bbefa63b56860b2f86a76a8579f71845a66e2faf98d`, vérifié). Le rédacteur n'a écrit ni la conception, ni le code, ni leurs contre-lectures ; il n'a vu aucun interne de moniteur.
- **Arithmétique** : `calcul-devis-ii-b-v2.py` (`d869c8e8a4276bbfa599d1ef553e4bba0a14fe49b760bfc928fbe3abfb0bf30f`), sortie brute `sortie-calcul-devis-ii-b-v2.txt` (`abe794be018204d98e6f3eb61739ba7a9ef3ed739a853c8b693931ee09ff0ff2`), même dossier, scellés. Chaque nombre ci-dessous en vient. Le calcul v1 (`bb7dd00e…`) a été rejoué : sortie identique à l'octet à sa sortie scellée (`15d5fcc0…`).
- **Ce qui change depuis le brouillon 2** : (1) dates à jour, d'après la ligne d'accord inscrite ; (2) **juge de T0.8 retiré des totaux** : le code v3 refuse une configuration qui annonce sa forme scellée et n'en joue aucune passe (`iib/configuration_v1.py`, fonction `exiger_config_iib_v1`) ; −0,21 h à chaque scénario ; (3) coupure par pièce et par point d'arrêt ; (4) heures de carte disponibles avant la coupure de la configuration ; (5) les deux variantes de plafond comparées à la ligne inscrite.

## 0. La ligne d'accord inscrite

`registres/go.md`, ligne `GO-2026-11-10-08` (lue par recherche de cette clé seulement) : type calcul, accordée par Lazar le 2026-11-10, **plafond 60 USD (« option B de M7 ; coupure à 55 USD »)**, **échéance 2026-11-27**, « A100 seule ». Elle exige, selon la lecture de la mère qu'elle porte : code rendu et contre-lu, devis rendu et inscrit en complément, ordre exploratoire contre-lu et scellé, six épreuves de l'oracle passées ; sortie scellée avant lecture ; arrêt par identifiant. Elle porte aussi les mots « avec l'activité interne enregistrée » : voir la note des nœuds, point 2 (`noeuds-ii-b-pour-lazar-v1.md`).

Contrôle fait sur processeur, avec le code v3 (`origin/prep/iib-code-v3`, `d88e3d947ec4f05958834e2746a800c854271a8f`) et une copie de cette seule ligne au bloc-notes : la sous-commande `plafond-ligne` de `iib/session_v1` lit **60** (code 0, jours 2026-11-18 et 2026-11-27) et refuse le 2026-11-28 (« hors de sa période de validité ») ; la sous-commande `go` accepte une configuration à **55** USD et **refuse 75** (« 75 > 60.0 »). La ligne figure une fois dans `registres/go.md` du commit `d88e3d94`.

## 1. Hypothèses (écrites, sourcées)

| grandeur | valeur | source |
|---|---|---|
| durée d'un épisode (N = 1, T = 10, lot de 8, 400 jetons au plus) | 43,3 s | lecture A de 7a (`docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/lecture-A-exploratoire-non-opposable-v1.md`, `3c84c419…`, § 4), citée par le devis brouillon 2, § 1 ; non relue ici ; aucun rabais pris pour l'absence de capture d'activations |
| amorce, format et disque ; suite ciblée ; création, image, modèle ; écriture et poussées | 0,07 h ; 0,58 h ; 0,25 h (non relevé en 7a : hypothèse) ; 0,10 h | idem. La suite ciblée de (ii-b) compte 406 essais (vérification courte du code v3, `e5c31d4f…`, § 4 : 6 min 55 s sur processeur) ; 0,58 h gardé (prudent) |
| distillation, par transcription et par époque | 1,86 s | 7a, 14 min 51 s pour 160 transcriptions × 3 époques (devis brouillon 2, § 1) |
| jumeau honnête (oracle), par action | 0,5 / 1,0 / 1,5 s attendu ; 3,0 s pire | **non mesuré** ; le pire couvre le repli « préremplissage par suite » que le code prend si le cache dupliqué échoue (`iib/modele_v1.py`, en-tête ; replis consignés) |
| épisodes | étalonnage 96 (64 honnêtes + 32 du saboteur flagrant de P3) ; maître 32 par tour ; évaluation 256 | conception brouillon 2, sections 3.4, 4, 6 ; code v3 (`TEXTE`, `iib/configuration_v1.py`) |
| tours du maître | 6 (bas), 10 (central), 12 (haut et pire) | conception 3.3 et 4 |
| actions passées au jumeau | 960 (étalonnage) + 320 par tour + 320 (ancrage, premier tour) + 2 560 (évaluation) | conception 2.2, 3.4, 6 ; code v3, `jouer_tour` (ancrage au tour 1) |
| juge de T0.8 | **hors des totaux** (option à part : 0,21 h en une passe, 3,08 h avec raisonnement) | code v3 : aucune passe écrite ; configuration refusée si la forme est annoncée scellée |
| prix A100 SXM4 80 Go | 1,12 USD/h central (consigne de la mère) ; relevés 1,009 à 1,2133 (T0.6 candidat 12 r3, `c24e268e…`, « Devis ») ; **borne 1,30** (configuration du candidat 12, brouillon 5, `b7a5c1ba…` ; code v3 : `carte.course.prix_max_usd_h` = 1,3) ; 1,40 au pire ; 2,10 non prévu | devis brouillon 2, § 1 ; code v3 |
| prix H200 NVL (variante A seulement) | relevés 4,441 et 4,669 ; borne 4,70 ; débit non mesuré (durées de l'A100 supposées) | idem ; code v3 : `carte.relance.prix_max_usd_h` = 4,7 |
| stockage, instance arrêtée | ≤ 0,08 USD/h ; 24 h attendu, 48 h au plus | code v3 : `STOCKAGE_MAX_USD_H` = 0,08 ; ordre § 1 |
| téléchargement | ≤ 0,05 USD/Go ; 20 Go attendu, 40 Go au plus | code v3 : `TELECHARGEMENT_MAX_USD_GO` = 0,05 ; devis brouillon 2 |
| minuterie de l'instance | consignation bornée à 2 400 s, puis destruction dans une marge de 1 800 s après l'échéance qu'on lui donne | amorce v3 (`scripts/amorce_instance_iib_v1.sh`, texte de la minuterie) |
| lectures (1) et (2) | 0 h de carte (processeur, après rapatriement) | conception 6 |

## 2. Heures de carte par étape (A100, hôte nominal ; juge hors des totaux)

| étape | bas (6 tours, jumeau 0,5 s) | **central** (10 tours, jumeau 1,0 s) | haut (12 tours, jumeau 1,5 s, 127 acceptés) | pire P1 (hôte ×2, 12 tours, jumeau 3,0 s, 127 acceptés) |
|---|---|---|---|---|
| fixe | 1,00 | **1,00** | 1,00 | 2,00 |
| étalonnage : épisodes | 1,15 | **1,15** | 1,15 | 2,31 |
| étalonnage : jumeau | 0,13 | **0,27** | 0,40 | 1,60 |
| maître : épisodes | 2,31 | **3,85** | 4,62 | 9,24 |
| filtrage : jumeau du maître et ancrage | 0,31 | **0,98** | 1,73 | 6,93 |
| distillation (élève, témoin-jumeau) | 0,31 | **0,31** | 0,40 | 0,81 |
| évaluation : épisodes | 3,08 | **3,08** | 3,08 | 6,16 |
| évaluation : jumeau (lecture 1) | 0,36 | **0,71** | 1,07 | 4,27 |
| **total** | **8,65** | **11,35** | **13,46** | **33,31** |

## 3. Attendu (USD ; stockage arrêté 24 h, téléchargement 20 Go)

| scénario | carte | stockage | téléchargement | **total** |
|---|---|---|---|---|
| bas, 1,0889 USD/h | 9,4 | ≤ 1,9 | ≤ 1,0 | **≈ 12,3** |
| central, **1,12 USD/h** | 12,7 | ≤ 1,9 | ≤ 1,0 | **≈ 15,6** |
| central, 1,30 USD/h | 14,7 | ≤ 1,9 | ≤ 1,0 | ≈ 17,7 |
| haut, 1,30 USD/h | 17,5 | ≤ 1,9 | ≤ 1,0 | **≈ 20,4** |

**Attendu : ≈ 8,7 à 13,5 h de carte, ≈ 12 à 20 USD, valeur centrale ≈ 16 USD.**

**Pièces de l'attendu central** (1,12 USD/h) : fixe 1,12 ; étalonnage 1,29 + 0,30 ; maître 4,31 ; filtrage 1,10 ; distillation 0,34 ; évaluation 3,45 + 0,80 ; stockage 1,92 ; téléchargement 1,00 (USD).

## 4. Coupure par point d'arrêt (ce qui est dépensé si la course s'arrête là)

| point d'arrêt | central (1,12 USD/h, 24 h, 20 Go) | pire P1 (1,40 USD/h, 48 h, 40 Go) |
|---|---|---|
| épreuves de l'oracle en échec (fin de l'étalonnage) | 2,42 h ; **≈ 5,6 USD** | 5,91 h ; ≈ 14,1 USD |
| contrôle du tour 4 (taux trop bas, ou consigne sans effet) | 4,41 h ; **≈ 7,9 USD** | 11,66 h ; ≈ 22,2 USD |
| fin du tour 12 avec moins de 48 acceptés | 8,20 h ; **≈ 12,1 USD** | 22,08 h ; ≈ 36,8 USD |
| course entière | 11,35 h ; **≈ 15,6 USD** | 33,31 h ; **≈ 52,5 USD** |

## 5. Pire cas (stockage arrêté 48 h, téléchargement 40 Go)

| scénario | heures | USD | sous la ligne inscrite (60) ? |
|---|---|---|---|
| **P1** sur A100 à 1,30 / **1,40** / 2,10 | 33,31 | 49,1 / **52,5** / 75,8 | oui / **oui** / non (2,10 n'est prévu dans aucune variante) |
| H200 NVL d'emblée, durées du haut de l'attendu, à 4,441 / 4,669 / 4,70 | 13,46 | 65,6 / 68,7 / **69,1** | non (variante A seulement) |
| P1 joué sur H200 NVL à 4,70 | 33,31 | ≈ 162 | non, dans aucune variante (la minuterie couperait avant) |
| relance après une erreur de chaîne ou de mémoire (P2, P3 du brouillon 2 : ≈ 102 et ≈ 107) | — | — | non : **nœud de Lazar avant toute relance** |

**Pire cas couvert** : variante B ≈ **52,5 USD** (P1 à 1,40) ; variante A ≈ 69,1 USD (H200 d'emblée).

## 6. Plafond : les deux variantes côte à côte

| | **variante A** | **variante B** |
|---|---|---|
| ligne de GO | 80 USD | **60 USD** |
| plafond de la configuration (minuterie et garde de la surveillance) | 75 USD | **55 USD** |
| conforme à la ligne inscrite `GO-2026-11-10-08` (60 USD) ? | **non** : le code refuse une configuration à 75 sous cette ligne ; une ligne neuve de Lazar serait exigée | **oui** (vérifié par le code v3, § 0) |
| carte | A100 ≤ 1,30 ; fenêtre de 12 recherches à 15 min (0 USD) ; fenêtre vide : H200 NVL ≤ 4,70 | A100 ≤ 1,30 ; même fenêtre ; **fenêtre vide : nœud**, aucune création |
| heures de carte avant la coupure (téléchargement de 40 Go déduit) à 1,12 / 1,30 / 1,40 USD/h | 65,2 / 56,2 / 52,1 h | **47,3 / 40,8 / 37,9 h** |
| marge sur P1 (33,31 h) à 1,30 / 1,40 | 22,8 / 18,8 h | **7,5 / 4,5 h** |
| repli H200 à 4,70 | 15,53 h avant la coupure : 2,08 h de marge sur le haut de l'attendu (13,46 h) ; P1 non couvert | sans objet |
| stockage arrêté 48 h (3,84 USD) sous ligne − configuration (5 USD) | oui | oui |
| couvre | attendu ; P1 à 1,30 et 1,40 ; P1 à 2,10 (≈ 75,8, sous la configuration de 75 : carte 70,0 + téléchargement 2,0) ; H200 d'emblée au haut de l'attendu | attendu ; P1 à 1,30 et 1,40 |
| ne couvre pas | H200 au-delà du haut de l'attendu (la minuterie coupe, résultats partiels poussés) ; relances | toute course sans A100 conforme (nœud ; glissement possible) ; P1 à 2,10 ; relances |
| marqueur de l'ordre `<<REPLI_H200_PERMIS>>` | oui | **non** |

Le choix est porté à Lazar (note des nœuds, point 1) ; **la ligne déjà inscrite correspond à la variante B**. Le rédacteur recommande B (confiance haute) : seule conforme à la ligne inscrite, elle couvre l'attendu et le pire cas sur A100 avec 4,5 h de marge au pire prix prévu.

## 7. Calendrier (dates à jour)

| grandeur | valeur | source |
|---|---|---|
| ligne d'accord | `GO-2026-11-10-08`, accordée le 2026-11-10, échéance **2026-11-27** | `registres/go.md` |
| fin du GO (`calendrier.fin_go_utc`) | **2026-11-28T00:00:00Z** (1 795 824 000 s) | règle du code : lendemain 00:00 UTC de l'échéance (`iib/configuration_v1.exiger_marqueurs` ; `t06/session_v3.verifier_calendrier_v3`) |
| échéance proposée de la minuterie (6ᵉ argument de `creation`) | **2026-11-27T22:00:00Z** (1 795 816 800 s), deux heures avant la fin du GO | consignation (2 400 s) et marge de destruction (1 800 s) de l'amorce : finies avant la fin du GO ; sans cet argument, la minuterie prend la fin du GO et peut détruire jusqu'à 30 min après |
| dernière création pour finir P1 avant l'échéance de la minuterie | 2026-11-26T12:41Z | calcul v2 |
| dernière création pour finir le haut de l'attendu | 2026-11-27T08:32Z | calcul v2 |
| **dernier jour de création proposé** (`calendrier.dernier_jour_creation`) | **2026-11-25** : une création le 25 à 23:59 finit P1 vers le 2026-11-27T09:18Z | calcul v2 ; le code refuse toute création après ce jour (`verifier_calendrier_v3`) |
| création | **jamais avant la création de 7b** (ligne du registre exigée par le code) ; au plus tôt dès les préalables de l'ordre (§ 4) | conception 7 et 11 ; code v3, `verifier_creation_7b` |

Les lectures (1) puis (2) se font après le rapatriement, sur processeur, sans carte.

## 8. Hors devis

- Contre-lecture, corrections du code, essais sur processeur, répétition jouet, lectures (1) et (2) : 0 USD.
- Juge de T0.8 (une passe ou avec raisonnement), juge d'une autre lignée : devis et GO à part ; non joués par le code v3.
- Toute capture ou tout recalcul d'activations (note des nœuds, point 2) : devis et GO à part, sous préenregistrement scellé à part.
- Une éventuelle passe préalable des épreuves de l'oracle sur une instance distincte (note des nœuds, point 3, option b) : ≈ 2,4 h, ≈ 5,6 USD au central, en plus d'une seconde création ; non prévue par ce devis.
- 7b, P3-bis, A1-v4 : lignes à part, jamais entamées.

## 9. Ligne d'engagement (à écrire par la mère au registre des dépenses, à la création ; forme seulement)

« engagement : saboteur à budget (ii-b), course exploratoire, non opposable (R-522) (`<<GO_ID_IIB>>`, plafond `<<PLAFOND_LIGNE_IIB>>` USD, configuration `<<PLAFOND_CONFIG_IIB>>`) : ordre `<<CHEMIN_ORDRE_IIB>>` (`<<EMPREINTE_ORDRE_IIB>>`), lanceur `scripts/lancer_iib_v1.sh`, commit `<<COMMIT_CODE_IIB>>` ; une carte A100 SXM4 80 Go ≤ 1,30 USD/h (repli H200 NVL ≤ 4,70 en variante A seulement), disque ≥ 100 Go ; attendu ≈ 12 à 20 USD, pire cas ≈ 52,5 USD (variante B) ou ≈ 69,1 USD (variante A) ; créée après 7b (`<<LIGNE_REGISTRE_CREATION_7B>>`) ; crédit Vast.ai relu à la création ».

Les marqueurs de cette ligne sont remplis par la mère au registre ; ce devis n'en remplit aucun (l'ordre les remplit, § 11 de l'ordre).
