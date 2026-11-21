# Rapport du développeur : collisionneur v9 version 7, v1

21 novembre 2026, vers 17:30Z. Développeur : Claude Opus 5.5 (`claude-opus-5-5`). Pièce d'instrument (classe B), à vérifier par Fable 5.2. Mot de Lazar : GO-2026-11-21-63 (« relancer tous les collisionneurs là où ils se sont arrêtés, sans perte de données, en laissant les modèles Gemini réfléchir jusqu'au bout »).

Ce que je n'ai pas fait : aucun appel à un modèle, aucun comptage, aucune requête vers un fournisseur, aucune dépense ; aucune clé lue (essais sans `OPENAI_API_KEY` ni `GEMINI_API_KEY`, clés factices des doublures seulement) ; aucun commit ; `especes.json` d'aucun dossier touché. Sur la branche `origin/runs/collisionneurs-reprise-minuit-v1` (761c2c5a), je n'ai lu que les journaux (`journal.jsonl`, `journal*.txt`, `journal*.log`), les compositions, les états et la taille (non le contenu) de `faits.md` et `question-etage3.md`, et les seuls noms des fichiers de `essais/` et `cellules/` ; aucune réponse de modèle.

## Pièces lues

| pièce | empreinte |
|---|---|
| `collisionneur_v9_v6.py` (base) | `3c6a4cfb…` (sceau tenu) |
| `reflexion-relance-collisionneurs-opus-max-v1.md` | `28ce8440…` (sceau tenu) |
| `verification-collisionneur-v9-v6-fable-v1.md` | `523dda37…` (sceau tenu) |
| `contre-lecture-collisionneur-v9-v5-v1.md` | `77041a13…` (sceau tenu) |
| `test_collisionneur_v9_v6.py`, `collisionneur_v9_v5.py` | sceaux tenus |
| page de prix versée `docs/sources/prix/page-prix-gemini-api-20261121T134918Z.html` | `40202cdd…` |
| liste des modèles versée `liste-modeles-gemini-20261121T134904Z.json` | `eeec19e8…` |

## Verdict

**La version 7 est écrite ; les neuf corrections sont portées, toutes éprouvées par un cas sain et un artefact.**

- Essais de la version 7 : **270 passés, 1 sauté** (la copie du run « dopamine », non désignée, comme en v6). Essais de la version 6, rejoués sur la v6 : **201 passés, 1 sauté**.
- **25 mutations, une au moins par correction : toutes prises** (section 4).
- Copies des quatre dossiers à reprendre : `verifier` tient avant et après, le devis ne touche à rien, la reprise envoie exactement 5, 5, 1 et 10 cellules, la relance de la même commande n'envoie rien (section 3.2).
- Deux points à trancher par la mère avant la reprise des mathématiques et de la dérive v2 (section 5) : le devis pessimiste du script dépasse le reste de leur ligne.

## 1. Les neuf corrections et leur lieu dans le code

| n° | correction | lieu |
|---|---|---|
| 1 | **V-1 de Fable, au texte exact** (section 6) : la garde compare la sortie facturée à la sortie comptée au pire cas (plafond de l'envoi plus provision), et non plus les pensées au budget. Docstring de `juger`, code 6 de l'en-tête et commentaire de `STATUTS_GARDE` accordés. | `juger` (paramètre `max_tokens`), appel dans `executer_cellule` |
| 2 | **Champ `budget` par espèce de Google** : envoyé (`thinkingBudget = m["budget"]`), journalisé (`budget_reflexion`), lu par `reglage_en_defaut`. Contrôle à la composition : budget entier, positif, au plus la provision (sinon code 1). Carbon : budget 32 768, provision 49 152, plafonds 65 536. Neon : budget = provision = 32 768 (inchangé). | `CATALOGUE`, `BUDGET_CARBON_V7`, `demande_gemini` (corps commun au flux et au lot), `fixer_composition`, `reglage_en_defaut`, entrée du journal dans `executer_cellule`, ligne du `devis` |
| 3 | **Argon** : plafonds 32 768, budget 8 192, provision 16 384, prix 4 et 20 USD par million. Source citée dans le code : page versée `40202cdd…`, section « Gemini 4 Argon », lignes 347 (« $4.00 starting December 1, 2026 ») et 354 (« $20.00 … »), sortie « including thinking tokens » ; plafond : `outputTokenLimit` 32 768 de la liste versée. | `CATALOGUE`, commentaire au-dessus |
| 4 | **Opus** : plafond de sortie 64 000 dès le premier envoi. | `CATALOGUE` |
| 5 | **`--rejuger-essai CELLULE:N`**, sans réseau (détail section 2.1). | `ecarts_rejugement`, `rejuger_essai`, `rejugements`, `lire_rejugement`, `cellules_du_run` ; `verifier` (admission) ; `ecrire_etat` (« OK (rejugement de l'essai N) ») ; `principal` |
| 6 | **`--repli-lot`** : après une coupure en flux chez Google, l'essai suivant de la cellule passe par `batchGenerateContent` (détail section 2.2). | `appeler_gemini_lot`, `lire_json`, `annuler_lot`, `coupure_en_flux`, `executer_cellule` (choix du mode, prix du lot), `APPELANTS["gemini_lot"]`, `FRACTION_PRIX_LOT`, `lancer_etage`, `principal` |
| 7 | **Refus de crédit dans le flux d'Anthropic**, sans texte ni usage final : échec sans envoi, coût zéro, code 5 (détail section 2.3). | `refus_de_credit`, branche `error` de `appeler_anthropic` |
| 8 | **`--accepter-absence`** refuse tout ce qui n'est pas une cellule du run (code 1, avant toute écriture). | `principal`, `cellules_du_run` |
| 9 | Essai de la remarque 1 de Fable (texte exact) ; essais sur copies des quatre dossiers. | `test_v7_defaut_de_reglage_lu_sur_le_dernier_essai` ; `test_v7_copie_des_dossiers_a_reprendre` |

Journal : chaque essai porte en plus `budget_reflexion`, `mode_envoi` (`flux` ou `lot` chez Google, `null` ailleurs), `nom_lot` et `prix` (prix appliqués à cet envoi). Aucun autre champ ne change. Garde de la clé d'OpenAI : inchangée (`--cle-openai OPENAI_API_KEY_2`, préfixe exigé) ; éprouvée de bout en bout sur les quatre copies, `OPENAI_API_KEY` absente.

## 2. Choix à vérifier

### 2.1 Rejugement (correction 5)

- **Conditions** (`ecarts_rejugement`), lues sur la ligne de journal de l'essai : statut `REFLEXION_HORS_PROVISION` ; espèce de Google, celle de la lettre ; fin `STOP` ; `marqueur_fin` vrai ; usage lu, ni interruption ni échec ; modèle demandé égal à celui de la table et modèle servi conforme ; entrée facturée au plus la garde d'entrée ; **écart de total égal à zéro** (lu à la lettre : « écart nul ») ; **sortie facturée au plus le plafond plus la provision de cet essai** (celle du journal, 65 536 + 32 768 sous la v3), c'est-à-dire la sortie comptée dans son pire cas.
- **Ajouts, plus stricts que la section 8.5** : l'essai doit être le dernier de la cellule ; les sceaux du prompt et de la réponse doivent tenir et égaler les empreintes du journal ; le texte scellé doit finir par le marqueur. Je les crois dans l'esprit de « aux seules conditions » (ils ne font que refuser) ; à confirmer.
- **Écriture** : ligne `rejugement` d'abord (coût 0,0, sortie facturée, sortie comptée, motif, script), puis la cellule. Un arrêt entre les deux : la relance écrit la cellule sans seconde ligne ; `verifier` signale entre-temps « rejugement au journal sans cellule ».
- **`verifier`** admet une cellule écrite sans essai OK si elle a un seul rejugement, d'un essai présent, aux mêmes conditions, à la même empreinte ; il refuse deux rejugements, un rejugement plus un essai OK, un rejugement hors conditions.
- **Ordre dans `principal`** : composition scellée, script déclaré (`--reprise`), ligne, rejugement, absences, étage. Forme de l'option contrôlée avant toute écriture.
- Le rejugement ne coûte rien et ne compte rien : la dépense de l'essai, au coût réel, est déjà au journal depuis la v3.

### 2.2 Repli par lot (correction 6)

- **Quand** : `--repli-lot` donné, espèce de Google, et au moins un essai de la cellule interrompu en flux (coupure, délai, 5xx ; un essai sans `mode_envoi` au journal est un essai en flux, les versions d'avant n'ayant que le flux). Une fois coupée, la cellule reste en lot pour ses essais suivants, relance comprise. Sans l'option : flux, comme en v6.
- **Comment** : une requête de création (corps de génération identique au flux, budget compris), puis des relevés `GET batches/…` toutes les 30 s, chacun borné à 120 s, jusqu'au délai de l'espèce (5 400 s pour Carbon). Un relevé coupé est repris au suivant, sans coût. Au délai : annulation demandée (`:cancel`), envoi interrompu, compté au pire, nom du lot au journal. Lot échoué, annulé, expiré, réponse en erreur ou illisible, relevé refusé (4xx), création coupée ou sans nom lisible : interrompu, compté au pire. Création refusée avant traitement (4xx) : échec, coût zéro. Modèle servi lu dans la réponse (`modelVersion`), contrôlé par `juger` (code 3 sinon).
- **Prix** : moitié du prix de la table, pour le coût réel **et** pour le pire cas compté avant l'envoi (onglet « Batch » de la page versée : Carbon lignes 184 et 191, Argon lignes 403 et 410 ; « Batch API (50% cost reduction) », ligne 43). La table compte déjà le prix du 1er décembre, double du prix actuel.
- **Forme de l'interface : SUPPOSÉE**, d'après la documentation publique de Google, non versée ici : corps `batch.input_config.requests.requests[].request`, réponse `name`, états `BATCH_STATE_*` (et `JOB_STATE_*` acceptés), réponses sous `response.inlinedResponses` (liste, ou objet qui porte la liste). Jamais essayée en réel. Un écart de forme donne un envoi interrompu compté au pire (code 5), jamais une réponse fausse.

### 2.3 Refus de crédit (correction 7)

- **Critère** : événement `error` dans le flux, de type `invalid_request_error` ou `billing_error`, dont le message contient « credit balance » ; aucun texte reçu ; aucun usage final (`message_delta` porteur de `output_tokens`). Forme relevée deux fois le 21 novembre (journaux « méthodes maths », E3-T2-critique-croisee-A, et « dérive v1 », E3-T1-conception-B) : `message_start` reçu, un bloc de réflexion ouvert, puis l'erreur.
- **« Usage nul »** : je l'ai lu comme « aucun usage final et aucun texte ». L'usage de `message_start` (entrée annoncée) n'est pas compté ; il est écrit dans le message d'échec du journal, pour la trace. Le journal de la v3 ne garde pas cet usage : je ne sais pas ce qu'il valait dans les deux cas réels.
- Hors de ce critère (texte reçu, usage final reçu, autre type, autre message) : interrompu, compté au pire, comme en v6.
- Les 3,03 et 1,29 USD comptés à tort restent dans les journaux des runs (on ne réécrit jamais un journal) : la ligne des mathématiques garde ce compte.

### 2.4 Ce que je n'ai pas changé

- Neon : ni la provision ni le budget (la V-2 de Fable pour Neon n'est pas dans les neuf corrections).
- La relance d'une réponse coupée au même plafond (gardée, réserve 3 de la contre-lecture de la v5).
- Argon n'est pas sous la règle du plafond large (16 384 jetons de texte au-delà de la provision, sans plancher exigé).
- `devis-reprise` ne connaît ni le rejugement ni le lot : il compte la cellule à rejuger comme à envoyer, et le lot au prix plein. Il reste pessimiste.

## 3. Essais

### 3.1 Suites

Environnement à moi (venv dans mon bloc-notes). L'installation complète de `requirements-cpu.txt` a rempli le disque (95 %) : je l'ai retirée et n'ai gardé que `pytest==9.1.1`, la version de `requirements-cpu.txt` ; le script et ses essais n'emploient que la bibliothèque standard. Clés absentes de l'environnement, `TMPDIR` et `--basetemp` à moi.

| suite | résultat |
|---|---|
| `test_collisionneur_v9_v7.py` sur la v7 | 270 passés, 1 sauté |
| `test_collisionneur_v9_v6.py` sur la v6 | 201 passés, 1 sauté |

La partie reprise de la v6 est adaptée là où la v7 change, marquée « v9-v7 » : budget envoyé à Carbon (32 768) ; Argon (4 et 20, 16 384, plafonds 32 768) ; table comparée à la v3 avec les seuls changements voulus (Carbon, Argon, Opus) ; les trois essais de V-1 remplacés au texte exact de Fable, et l'essai de Carbon du 20 novembre accordé.

Section v7 (37 fonctions, 76 cas) :
- V-1 : seuil lu sur le plafond de l'envoi (premier plafond abaissé sur copie de la table : un jeton au-delà arrête, le bord passe) ; `juger` sans plafond lit la relance.
- Budget : envoyé, journalisé, pire cas sur la provision (Carbon, Argon, Neon) ; refus à la composition (absent, 0, au-delà de la provision, flottant, booléen) ; budget égal à la provision accepté ; `reglage_en_defaut` lit le budget ; un arrêt au code 9 sous la v6 (budget 49 152, fabriqué par la v6 elle-même) est renvoyé par la v7 (réglage changé).
- Argon : réglages, prix, lignes de la page versée relues par l'essai, limite de la liste, pire cas et coût réel.
- Opus : 64 000 au premier envoi, pire cas.
- Rejugement, sur un run fabriqué par la **v3 elle-même** (`850df311…`, Fable et Carbon, la réponse de Carbon reprise du run « percée » : 44 101 pensées, sortie facturée 55 125, fin `STOP`) : sain (cellule écrite depuis la réponse scellée, aucun envoi ni comptage pour elle, deux envois au tour III.3, pièce injectée avec son empreinte, `verifier` tient, dépense inchangée par le rejugement) ; idempotence (journal identique à l'octet, aucun envoi) ; reprise sans doublon après un arrêt entre ligne et cellule ; artefacts, tous au code 1, rien d'écrit, aucun envoi : fin `MAX_TOKENS`, marqueur absent, sortie au-delà de la sortie comptée, écart de total non nul, entrée au-delà de la garde, modèle non conforme (et statut `MODELE_DIFFERENT`), réponse altérée, réponse et sceau remplacés ensemble, essai qui n'est pas le dernier, six formes d'option refusées ; `verifier` : trois artefacts (conditions rompues au journal, deux rejugements, essai absent).
- Lot : sain après coupure (création, relevé coupé repris, relevé en cours, relevé fini ; corps, budget, clé en en-tête et jamais au journal, attentes, prix et pire cas du lot) ; réponse non imbriquée ; témoins sans option et sans coupure (flux) ; relance après un lot tronqué, en lot ; délai dépassé (annulation, pire cas, nom du lot) ; six artefacts comptés au pire ; création refusée à coût zéro ; modèle contrôlé ; option passée par la ligne de commande, les autres cellules restant en flux.
- Crédit : échec à coût zéro, un seul envoi ; quatre artefacts comptés au pire ; types reconnus.
- Absences : cinq noms refusés sans rien écrire (dossier non créé) ; refus sur un run existant, journal intact ; deux cellules acceptées.
- Remarque 1 de Fable, au texte exact.

### 3.2 Copies des quatre dossiers à reprendre

Méthode (`fabriquer_copie`, dans le fichier d'essais) : chaque copie est fabriquée depuis le seul journal et la seule composition du run, lus par `git show` sur la branche des versements (`REF_RUNS_COLLISIONNEURS`, défaut `origin/runs/collisionneurs-reprise-minuit-v1` ; `DEPOT_COLLISIONNEURS`). `especes.json` et son sceau sont les vrais, copiés à l'octet ; `faits.md` et `question-etage3.md` ont la longueur des fichiers versés et un contenu factice ; chaque essai du journal est rejoué en fichiers neufs : prompt construit par le script, réponse factice de la longueur journalisée (marqueur compris s'il y était), cellule pour chaque essai OK ; empreintes et pièces du journal recalculées, tout le reste gardé (statuts, usages, coûts, plafonds, ligne, absences, empreintes du script v3). L'essai parti sans ligne de journal du run « percée » (prompt seul, E3-T1-conception-B, essai 1) est refait de même. Branche absente : essais sautés.

Commande : celle de la réflexion d'Opus (section 7), cinq espèces, `--cle-anthropic MA_CLE --cle-openai OPENAI_API_KEY_2 --reprise`, ligne L, plafond P, option ; faux fournisseurs qui répondent selon l'adresse.

| dossier | dépense, reste de la ligne | option | cellules envoyées (créations) | comptages | après |
|---|---|---|---|---|---|
| percée (…-114810), L 28, P 27,5 | 10,27 ; 17,73 | `--rejuger-essai E3-T2-critique-croisee-E:1` | 5 (tour III.3) | 5 | 15 cellules, `verifier` tient, un rejugement, aucun essai 2 de Carbon au tour III.2 |
| dérive v2 (…-131044), L 24, P 23,2 | 9,84 ; 14,16 | idem | 5 | 5 | idem |
| antériorité (…-131029), L 28, P 26,4 | 14,72 ; 13,28 | `--repli-lot` | 1 (lot, essai 3 de E3-T3-reponse-E, prix 2 et 10) | 1 | 15 cellules, `verifier` tient |
| mathématiques (…-093850), L 28, P 28 | 6,23 ; 21,77 | — | 10 (tours III.2 et III.3) | 10 | 15 cellules, `verifier` tient |

Dans les quatre : `verifier` tient avant la reprise ; `devis-reprise` n'écrit rien et n'envoie rien ; aucun fichier d'avant n'est touché, le journal d'avant est un préfixe du journal d'après ; un seul changement de script déclaré ; la clé envoyée à OpenAI est celle de `OPENAI_API_KEY_2` ; la même commande relancée n'envoie rien.

Devis de reprise de la v7 sur ces copies (USD comptés ; longueurs réelles, textes factices ; Fable à 49 000) :

| dossier | reste | pire sans relance (III.2 + III.3) | avec relances | plafond de Fable retenu par le devis |
|---|---|---|---|---|
| percée | 17,73 | 15,86 (2,54 + 13,32) | 33,67 | 86 000 |
| dérive v2 | 14,16 | 15,73 (2,54 + 13,19) | 33,41 | aucun |
| antériorité | 13,28 | 2,55 (au prix plein ; le lot le divise par deux) | 5,11 | 128 000 |
| mathématiques | 21,77 | 28,45 (9,50 + 18,95) | 60,81 | aucun |

Pour percée et dérive v2, le tour III.2 compté (2,54) est la cellule de Carbon que le rejugement n'enverra pas.

## 4. Mutations

Chacune sur une copie, dans mon bloc-notes ; suite v7 entière rejouée (les copies des quatre dossiers comprises).

| mutation | essais en échec | prise |
|---|---|---|
| 1 V-1 : garde revenue aux pensées contre la provision | 5 | oui |
| 1 V-1 : plafond de l'envoi non passé à juger (relance lue) | 1 | oui |
| 2 budget : provision envoyée au lieu du budget | 5 | oui |
| 2 budget : non journalisé | 7 | oui |
| 2 budget : ignoré par reglage_en_defaut | 2 | oui |
| 2 budget : contrôle de composition retiré | 5 | oui |
| 3 Argon : prix 10 / 50 | 6 | oui |
| 3 Argon : provision 8 192 | 5 | oui |
| 4 Opus : premier plafond 22 000 | 2 | oui |
| 5 rejugement : fin STOP non exigée | 1 | oui |
| 5 rejugement : sortie non bornée | 1 | oui |
| 5 rejugement : écart de total non exigé nul | 1 | oui |
| 5 rejugement : dernier essai non exigé | 1 | oui |
| 5 rejugement : empreintes du journal non comparées | 1 | oui |
| 5 rejugement : ligne redoublée à chaque relance | 1 | oui |
| 5 rejugement : verifier ne l'admet plus | 4 | oui |
| 6 lot : option ignorée | 13 | oui |
| 6 lot : sans coupure préalable | 2 | oui |
| 6 lot : prix plein | 2 | oui |
| 6 lot : aucune annulation au délai | 1 | oui |
| 6 lot : état d'échec lu comme un succès | 1 | oui |
| 7 crédit : refus compté au pire (comme le v9-v6) | 1 | oui |
| 7 crédit : refus admis après du texte | 1 | oui |
| 8 absence : nom hors cellule accepté | 6 | oui |
| 9 remarque 1 : premier essai lu au lieu du dernier | 1 | oui |

25 mutations sur 25 prises.

## 5. Réserves et points pour la mère

1. **Devis au-delà du reste de la ligne : mathématiques (28,45 pour 21,77) et dérive v2 (15,73 pour 14,16).** C'est la borne pessimiste du script (critiques non écrites comptées au plafond de leur auteur, Opus désormais à 64 000), plus haute que les 17,8 de la réflexion d'Opus pour les mathématiques. La garde par envoi refuse avant tout dépassement (code 4), sans perte : la course peut s'arrêter avant la fin dans ces deux dossiers. La réflexion d'Opus dit déjà que `devis-reprise` n'est qu'indicatif ; à confirmer avant la reprise.
2. **Lot jamais essayé** : forme supposée (section 2.2). Un écart coûte au plus un pire cas au prix du lot et arrête au code 5.
3. **« Usage nul » du refus de crédit** : lu comme « aucun usage final, aucun texte » (section 2.3).
4. **Rejugement** : trois conditions ajoutées, plus strictes que la section 8.5 (section 2.1) ; écart de total exigé exactement nul.
5. Restent ouvertes, comme le disent Fable et Opus : le plafond synchrone de 65 536 (au-delà, « long decode », non employé), le niveau de réflexion par paliers de Google (aucun champ envoyé), la relance au même plafond d'une réponse coupée, Argon jamais servi au-delà de 32 768.
6. Disque : l'installation complète des dépendances a été retirée de mon bloc-notes ; aucun fichier hors de mon bloc-notes et des trois pièces ci-dessous n'a été écrit.

## Pièces écrites

| fichier | empreinte |
|---|---|
| `collisionneur_v9_v7.py` | `319a7b66b5b9…` |
| `test_collisionneur_v9_v7.py` | `7afaa354a85f…` |

Outils (bloc-notes, non durable) : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/dev-v7/outils/mutations_v7.py`, `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/dev-v7/outils/test_devis_copies.py`.
