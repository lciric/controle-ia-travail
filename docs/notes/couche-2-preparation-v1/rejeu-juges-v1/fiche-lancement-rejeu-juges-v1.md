# Fiche de lancement — rejeu des juges du pilote de T0.5 sur ses 180 textes — v1

Écrite par un sous-agent de la lignée « session-depot » le 29 octobre 2026 (UTC), sous **GO-2026-10-28-16** (plafond
4 USD). Elle complète le devis `devis-rejeu-juges-v1.md` (même dossier). Elle tient lieu de préenregistrement (R1) :
le module `src/controle_ia/environnements/noter_rejeu_juges_v1.py` la reçoit par `--prereg` et en contrôle la forme
(sections exigées par `prereg.py`), le sceau et les citations ci-dessous. Le script de l'instance en lit les chemins
avant toute installation. **Rien n'est lancé par ce document.** Les deux marqueurs entre chevrons et la section
« Contre-lecture » se remplissent au commit, après la contre-lecture R2. Tant qu'ils restent, ni le scellement
(`prereg.sceller_prereg`) ni le lanceur n'acceptent la fiche.

## Citations (une seule occurrence de chaque intitulé ; lues par le module et par le script de l'instance)

- Commit du code d'analyse : `<<COMMIT_CODE>>`
- Configuration du rejeu (empreinte canonique) : `07d7fd810528d9341c36132c4504d4dc6ba7205012e075b018be15ce20e185ed`
- Chemin de la configuration du rejeu : `docs/notes/couche-2-preparation-v1/rejeu-juges-v1/config-rejeu-juges-v1.json`
- Run du pilote rejoué : `20261012-105125-t05-pilote-reel`
- Chemin du manifeste du pilote rejoué : `runs/20261012-105125-t05-pilote-reel/manifeste.json`
- Épisodes du pilote rejoué : `45616303dc740b66c42095cd5317a8ddd63e89123e64dd86490e43429c7cd15c`
- Chemin des épisodes du pilote rejoué : `diag/20261012-105125-t05-pilote-reel/episodes.json`
- Chemin de l'arrêt du pilote rejoué : `diag/20261012-105125-t05-pilote-reel/arret.json`
- Run des notations rejouées : `20261017-193648-t05-notations-reel`
- Manifeste des notations rejouées : `9f143f7c1c9fd9d75f21807a0fa41035ae7110abe686fc7819130d3f6b435d38`
- Chemin du manifeste des notations rejouées : `runs/20261017-193648-t05-notations-reel/manifeste.json`
- Notations rejouées du 8B : `b103835bcd3bfc3117a53e335be6f37a1259102cc2a2a134acfc6e114cb3f1c4`
- Chemin des notations rejouées du 8B : `diag/20261017-193648-t05-notations-reel/notations-8B-decisives.json`
- Notations rejouées du 3B : `51548526c7590231b76473c2b4c9e619a092616b5f948830e735c466b037adab`
- Chemin des notations rejouées du 3B : `diag/20261017-193648-t05-notations-reel/notations-3B-decisives.json`
- Tâches du pilote : `287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa`
- Chemin des tâches du pilote rejoué : `donnees/t05-pilote-v1/taches-pilote-60-v1.json`
- Consigne du verdict d'abord : `7c8ef0c9a80ea40e0b9274780af5e98ee62335cbe7712d29ae15e664008d6cb3`
- Entropie : `37114382722285754842192283631495258186` (celle du pilote et des notations rejouées, reprise telle quelle)
- Tests attendus : `<<TESTS_ATTENDUS>>` (suite ciblée du script de l'instance : `tests/test_noter_rejeu_juges_v1.py`,
  `test_noter_pilote_a.py`, `test_pilote_a.py`, `test_manifeste.py`, `test_scellement.py`, `test_prereg.py` ; dernière
  ligne « N passed[, M warning(s)] in X s », rien d'autre)

Empreintes vérifiées le 29 octobre 2026 contre leurs sceaux (`sha256sum -c`). Configuration : empreinte canonique
recalculée par `lancer_pilote_a.empreinte_config` ; à recalculer si la contre-lecture la change.

## Hypothèse

Question d'instrument, sans signe recherché (R3). Pour chaque cellule (juge × variante), sur les 180 notations
décisives du pilote :
- H_A : au moins 0,99 des scores sont finis et appuyés quand le juge est lu par la probabilité du jeton de verdict ;
- H_B : moins de 0,99 ; la cellule doit être redéfinie avant toute banque.

Ce duel est celui du collisionneur (cellule E3-T1 de la conception B, l. 250-252 ; synthèse `37f85388…`, l. 327-328).
Cellules : 8B et 3B × « b0 relu », « verdict d'abord », « budget relevé » (devis, § 3).

## Prédiction chiffrée et signe attendu

- **b0 relu.** Une réponse tronquée reste sans score, d'où des bornes arithmétiques sur les comptes RAPPORTÉS par
  l'audit R4 (`d69a8700…`, l. 143-149, 252-253) :
  - 8B : au plus 120 sur 180 (0,667). Il faut s'attendre à 82 à 96 (0,46 à 0,53) : les 54 complètes, plus les 28 à
    demi-points seulement, plus une partie des 14 mixtes, si toutes sont appuyées ;
  - 3B : au plus 171 sur 180 (0,95). La fourchette est large, 50 à 160 (SUPPOSÉ), car les 96 notes hors échelle seules
    échouent probablement au seuil d'appui ;
  - **H_B dans les deux juges, certaine.**
- **Verdict d'abord.** Aucune borne. SUPPOSÉ : 8B ≥ 0,9 ; 3B entre 0,5 et 0,95 (tendance aux notes hors échelle). Les
  deux issues sont possibles ; aucune n'est visée.
- **Budget relevé** (composé avec b0 relu). Au plus b0 relu + 2 sur 180 pour le 8B (59 tronquées sur 60 sont
  dégénérées) et b0 relu + 1 pour le 3B. **H_B, certaine.**
- **Accord** (8B, b0 relu). SUPPOSÉ : 0,8 à 0,95 des critères. La note écrite a été tirée à la température 1 : la
  valeur la plus probable ne lui est égale qu'avec la probabilité de cette valeur.
- **Rythmes.** SUPPOSÉS (devis, § 4) : b0 relu ≈ 2,5 s par notation (8B) et ≈ 1 s (3B) ; verdict d'abord ≈ 6 s et
  ≈ 3,4 s ; budget relevé ≈ 28 s et ≈ 27 s par réponse prolongée.

## Métrique

**Lecture par la probabilité du jeton de verdict** (D-S13 telle que la citent le GO et R-671 ; module,
`lire_par_probabilite`). Pour chaque critère de la rubrique H.4, la lecture se fait après la dernière occurrence de
« CRITÈRE: » (expression de `rubrique.lire_notes`).
- Chaque valeur admise v de [lo, hi] a sa suite de jetons, encodée depuis le jeton qui porte le premier caractère
  après les deux-points.
- La **position de décision**, une seule par critère, est la première où ces suites divergent.
- La probabilité de v est le produit des probabilités conditionnelles de sa suite, à partir de cette position. Les
  branches hors du chemin écrit se lisent par passes forcées.
- La masse admise M est la somme de ces probabilités. La loi est renormalisée sur les valeurs admises ; la note lue est
  l'espérance.
- Score lu : 100 × max(0, somme des dix espérances) / 33.

**Jamais de moyenne ni de médiane sur des jetons.**

**Score fini et appuyé** d'une notation : les trois conditions suivantes réunies, sinon aucun score (jamais imputé),
motif consigné.
- Fenêtre complète :
  - b0 relu et budget relevé : réponse terminée par un jeton de fin (règle CL-9) ;
  - verdict d'abord : les dix critères apparaissent dans la réponse, et la lecture porte sur le bloc qui va du début de
    la réponse à la fin de la ligne où le dixième apparaît pour la première fois.
- Les dix positions existent : critère présent, valeur écrite après les deux-points.
- À chacune des dix positions, M ≥ 0,5 (`masse_min_appui`).

**Complétude d'une cellule** : k / n, k scores finis et appuyés sur n = 180. La cellule « budget relevé » se compose
ainsi : notations prolongées pour les réponses tronquées de b0 relu, notations de b0 relu pour les autres. Intervalle
de Wilson à 95 %.

**Alignement de l'instrument** : sur les critères à note écrite valide et lue, part où la probabilité renormalisée de
la note écrite est sous 0,001.

**Accord** : sur les notations où note écrite et lecture donnent toutes deux un score, deux mesures :
- part des critères où la valeur la plus probable égale la note écrite (ex æquo : la plus petite) ;
- écart absolu des scores sur 100, moyen et maximal.

**Rythmes** : secondes par notation par cellule (durée de la phase / notations), passes forcées, jetons générés, pic
de mémoire par phase.

## Seuil

- Complétude : **0,99** par cellule.
  - n = 180 : **H_A si k ≥ 179** ; H_B sinon.
  - H_B est « tranchée » si la borne haute de Wilson est < 0,99, soit **k ≤ 175**. Pour k de 176 à 178, H_B n'est pas
    tranchée.
  - H_A n'est jamais tranchée à n = 180 : 180 sur 180 donne une borne basse de 0,979. Le rejeu peut réfuter H_A, pas
    l'établir.
- Appui : M ≥ **0,5** à chaque position.
- Alignement : part improbable ≤ **0,02**. Au hasard, on attend au plus 6 × 0,001 = 0,006.
- Accord : part ≥ **0,90** → « concordant », sinon « discordant ». C'est un descriptif : aucune décision n'en dépend.

## Plan d'analyse

1. Récupération de la branche `calcul/rejeu-juges-v1`, contrôle des sceaux et du rattachement de chaque fichier au
   manifeste (`verifier_resultat`).
2. Lecture par la commande `python -m controle_ia.environnements.noter_rejeu_juges_v1 --lire <run>`, et par elle seule.
   Elle écrit `diag/<run>/lecture-rejeu-v1.json`, scellé, rattaché au manifeste.
3. Pour chaque cellule écrite : complétude (k, n, part, Wilson, H_A ou H_B, tranchée ou non), finis sans appui et finis
   écrits (descriptifs), alignement, accord, rythme. Une cellule non écrite (« échu » ou « non-commencé ») est « non
   mesurée ». Un budget relevé sans b0 relu du même juge est aussi « non mesuré ».
4. Compte rendu à Lazar : le verdict d'abord (quelles cellules tiennent H_A), puis les réserves. S'il y a lieu, une
   proposition avec recommandation sur la cellule des juges de la banque.

## Critères de lecture gelés

1. **Score fini et appuyé** : la définition de la section « Métrique », sans autre tolérance (ni troncature tolérée,
   ni note ramenée à la borne, ni critère imputé).
2. **Complétude** : H_A si k / n ≥ 0,99, H_B sinon, par cellule. Les cellules d'un même juge ne se combinent pas, sauf
   la composition déclarée de « budget relevé ».
3. **Alignement** : une cellule « désaligné » (part improbable > 0,02) se lit « non concluant (instrument désaligné) ».
   Son H_A ou son H_B n'est pas lu et l'audit R4 est déclenché. Le compte brut reste consigné (`lecture_brute`).
4. **Trop beau** (R4) : une cellule à 180 sur 180, ou dont toutes les masses dépassent 0,99, est auditée comme une
   cellule défavorable. L'audit relit vingt notations tirées au hasard (graine consignée) et la position de chacune
   des dix valeurs.
5. **Accord et rythmes** : rapportés, sans seuil de décision. L'étiquette d'accord n'est qu'un descriptif.
6. **Ce que la lecture décide** : quelles cellules (juge × variante) tiennent H_A, rien d'autre. Toute redéfinition de
   la cellule des juges dans la banque est une proposition à Lazar.

## Liste d'arrêt

Avant le manifeste (aucun run créé, code 1 du module) :
- configuration incomplète ou hors bornes : phases, durées, budgets 16 à 512 et 1 à 3 072, appui dans [0, 1], invite
  b0 seulement ;
- run réel sans fiche (R1) ;
- fiche non scellée ou non conforme ;
- commit du code différent de l'arbre gelé ;
- citation absente, en double ou différente : configuration, runs, manifeste et notations rejouées, épisodes,
  consigne, tâches, entropie ;
- invites altérées ;
- pilote dans un autre état que celui constaté (`charger_pilote_note`) ;
- notations rejouées absentes, non scellées ou rattachées à un autre manifeste ;
- paramètres des juges différents de ceux des notations rejouées ;
- demandes et notations désalignées (clé, empreinte de l'ensemble, nombre 180) ;
- lecture écrite refaite différente du score rejoué ;
- entropie différente de celle du pilote.

Après le manifeste (`arret.json` scellé, puis arrêt) :
- format d'un juge différent de celui du début du pilote ;
- format du 3B rechargé hors ligne différent ;
- contexte reconstruit d'une autre longueur que `jetons_contexte` ;
- réponse non tronquée présentée au budget relevé ;
- signal TERM (délai externe ou plafond de l'amorce), même avalé par une bibliothèque ;
- toute panne : mémoire, réseau, chargement.

Non-arrêts consignés :
- phase « échue » (sa durée maximale dépassée) : aucun fichier, la suivante commence ;
- phase « non-commencé » : le temps restant avant l'échéance globale est sous sa durée maximale ;
- notation sans score, avec motif.

Chaîne de l'instance (code 2 ou 1, résultats partiels et traces poussés) :
- branche de résultats déjà présente ;
- fiche ou fichier cité absent, ou sceau non conforme ;
- poussée initiale refusée ;
- carte indisponible ;
- tests en échec ou nombre différent de « Tests attendus » ;
- temps restant avant le plafond de l'amorce sous 20 minutes.

Lanceur (aucune création) :
- commit absent de `origin/main` ;
- pièces absentes ou non scellées ;
- marqueur restant dans la fiche ;
- commit du code non ancêtre du commit lancé ;
- jeton absent ;
- garde de calcul refusée ;
- autre instance sur le compte ;
- crédit sous 4,50 USD ;
- aucune offre conforme (A100 SXM4 80 Go, ≤ 1,43 USD/h, fiabilité ≥ 0,98, CUDA ≥ 13.0, mémoire vive ≥ 64 Go,
  téléchargement ≤ 0,01 USD/Go).

## Bornes de temps

- **Phases**, dans l'ordre de priorité de la configuration :

  | phase | durée maximale |
  |---|---|
  | 8B, b0 relu | 20 min |
  | 3B, b0 relu | 10 min |
  | 8B, verdict d'abord | 30 min |
  | 3B, verdict d'abord | 20 min |
  | 8B, budget relevé | 40 min |
  | 3B, budget relevé | 10 min |

  Une phase ne commence que si le temps restant avant l'échéance globale couvre sa durée maximale.
- **Échéance globale** du module : 85 minutes (5 100 s). Au-delà, plus aucune phase ne commence. Le dernier lot peut la
  dépasser d'au plus ≈ 4 minutes : un lot de budget relevé fait 1 024 pas.
- **Délai externe du run** : 95 minutes au plus (TERM converti en arrêt consigné, KILL 5 minutes plus tard). Il est
  borné par le temps restant avant le plafond de l'amorce, moins 13 minutes.
- **Amorce** : 130 minutes, puis KILL 5 minutes plus tard.
- **Arrêt de l'instance** par la session, par identifiant (R10), dès la fin de l'amorce lue dans le journal, et au plus
  tard à la création + 9 000 s (heure écrite par le lanceur). Pire cas facturé ≈ 3,9 USD (devis, § 6).

## Manifeste et graines (R9)

Run `AAAAMMJJ-HHMMSS-rejeu-juges-reel`. Le manifeste (`runs/<run>/manifeste.json`, scellé) porte :
- la configuration et son empreinte, les versions, le commit, cette fiche (chemin et empreinte) et la commande ;
- les **graines**, dérivées par `numpy.random.SeedSequence` de l'entropie du pilote, comme au pilote. Clés :
  - une par génération : `rejeu-v1/verdict-d-abord/<clé du pilote>` (360) et `rejeu-v1/budget-releve/<clé>` (69, les
    réponses tronquées) ;
  - plus `modele-jouet`, qui égale la graine du pilote.

Les phases b0 relu ne tirent rien. Résultats : `diag/<run>/rejeu-<juge>-<variante>.json`, `resume.json`, et
`arret.json` s'il y a lieu, tous scellés et rattachés au manifeste. Rien n'est écrit dans les dossiers du pilote ni dans
ceux des notations rejouées.

## Ce que ce rejeu ne décide pas

- Aucune lecture de T0.5 n'est refaite. Le verdict des notations (`d861605c…`) et la bascule vers le plan B (N-022)
  restent tels quels.
- Aucun chiffre opposable (R7) ; aucune mesure de justesse des juges.
- Aucun changement de modèle, d'invite publiée ni de rubrique. La consigne « verdict d'abord » est un ajout déclaré, à
  l'empreinte citée. Ce rejeu ne remplace pas le plan B (RS1), dont le code n'est pas sur `main`.
- Aucune redéfinition de la cellule des juges dans la banque : ce sera une proposition à Lazar.
- D-S13 : divergence de lecture entre le GO (probabilité du jeton de verdict) et les faits du collisionneur (bris
  d'égalité scellé, v4 § 2.4). Elle n'est pas tranchée ici (devis, § 2).

## Contre-lecture

À REMPLIR : sous-agent neuf (R2), fichiers donnés (devis, fiche, configuration, module, essais, amorce, script de
l'instance, lanceur), empreinte du brouillon relu, chemin et empreinte du rapport, traitement des constats.
