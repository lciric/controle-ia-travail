# Tour du collisionneur sur « Regard ou raisons », consultations à part comprises : dépense et incidents — v1

Écrit le 14 novembre 2026 à 10:35 UTC (heure relevée par `date -u`) par l'opérateur neuf (Claude Fable 5.2) de la session
mère, sous **GO-2026-11-12-04** (tour 3 sur 4 ; plafond de ce tour 15 USD, consultations comprises ; mots de Lazar : R-2679,
R-2680, R-2682). Devis scellé avant tout appel : `devis-v1.md` (`90577048…`, scellé à 09:27:04), pire cas 2,08
(consultations) + 14,45 (collisionneur) = 16,53 USD, garantie de plafond par ordre de passage. Procédure : celle du tour 2
(R-2539), appliquée point par point.

## 1. Déroulé (heures de `date -u` et des consoles, UTC)

- 09:23:29 : début. Lecture de la consigne et des pièces du tour 2 ; empreintes vérifiées (script `4ad78ccc…`, programme des
  consultations `59c2fd36…`, ses essais `3a49df53…`, relais `67f36951…`, faits `87086190…`, question `f0481482…`).
- 09:25 → 09:27:04 : question servie extraite par programme (bloc « ## Question », `question-etage3-servie-v1.md`,
  `77156e04…`) ; essais hors réseau du programme des consultations rejoués, **19 sur 19**
  (`essais-consultation-a-part-sortie-v1.txt`) ; deux modes de devis ; devis écrit et scellé.
- 09:27:11 → 09:32:43 : **commande 1**, consultations à part, un appel chacune, un seul essai
  (`console-consultations-v1.log`) : Argon 09:27:11, Astra 09:30:27 ; code 0 ; dépense au barème du script **1,1274 USD**.
- 09:32:54 : **commande 2**, relais Kimi `relais_kimi_v4.py` (port 8789, plafond 3 USD, au plus 8 appels) ; son état
  (`relais-v1/etat-avant-v1.json`) rend `pid` 1906 et « variable de clé encore présente : non ».
- Plafond du collisionneur, calculé par la commande elle-même : 15,00 − 1,13 (1,1274 arrondi au centime supérieur) =
  **13,87 USD**.
- 09:33:07 → 10:33:43 : **commande 3**, étage III, un seul lancement (`console-run-e3-v1-lancement1-v1.log`), code 0,
  **10,01 USD**. Aucune reprise.
- 10:33:53 : état du relais relevé (`relais-v1/etat-apres-v1.json` : 3 appels, tous statut 200, 0,610754 USD, aucun refus,
  aucun écart de modèle servi, aucun usage absent) ; **relais arrêté par son numéro de processus, 1906** (R10), lu dans
  l'état et contrôlé par `ps` avant le signal ; arrêt vérifié (processus absent, port 8789 libre) à 10:33:53.
- 10:34:07 : `verifier` du run dans le bac à sable, hors réseau : **« tout tient »** (`verification-run-e3-v1.txt`).
- 10:34:35 : copie `cp -a` du run, des consultations et du relais vers ce dossier ; `verifier` sur la copie :
  **« tout tient »** (`verification-copie-run-e3-v1.txt` ; seul l'horodatage de `etat.md`, régénéré par `verifier`, diffère
  de l'original).

## 2. Consultations à part (`consultations-a-part-v1/`)

Prompt unique, le même pour les deux (`a844b8da…`, 12 682 caractères), modèle non nommé dans l'en-tête ; blocs FAITS
(`87086190…`) et QUESTION (`77156e04…`) aux empreintes servies au collisionneur. Kimi n'est pas consulté à part à ce tour.

| consultation | modèle servi | statut | fin | marqueur | jetons d'entrée | jetons de sortie | coût au barème du script, USD |
|---|---|---|---|---|---|---|---|
| Argon | `gemini-4-argon` | OK | STOP | oui | 3 563 | 14 538 | 0,7625 |
| Astra | `gpt-6-astra` | OK | stop | oui | 3 350 | 6 627 (dont 512 de raisonnement) | 0,3649 |
| **total** | | | | | | | **1,1274** |

**Les deux consultations sont valides** (fin normale, non tronquées, marqueur `FIN-DE-CONSULTATION` en dernière ligne,
modèle servi égal au modèle demandé). Aucun refus, aucune relance. Contenu non lu au-delà de ce contrôle.

## 3. Cellules du collisionneur (`run-e3-v1/`)

**15 cellules valides sur 15** (A `claude-fable-5-1`, B `claude-opus-4-6`, C `gemini-4-argon`, D `kimi-k3.1-pro` par le
relais, E `gpt-6-astra`, aux trois tours III.1, III.2, III.3) ; un seul essai par cellule (15 essais au journal) ; modèle
servi égal au modèle demandé ; marqueur de fin présent partout ; **aucun refus, aucune troncature, aucune absence
acceptée, aucune relance**. Contenu des cellules non lu : ni synthèse ni classement (un lecteur neuf croisera les sources).

## 4. Dépense relevée (journal du run et relevés des consultations, barème du script)

| espèce | modèle | collisionneur : essais (OK), entrée / sortie, USD | consultation, USD | total, USD |
|---|---|---|---|---|
| A | `claude-fable-5-1` | 3 (3), 106 710 / 42 022, 3,1682 | — | 3,1682 |
| B | `claude-opus-4-6` | 3 (3), 83 433 / 20 118, 2,7603 | — | 2,7603 |
| C | `gemini-4-argon` | 3 (3), 64 886 / 24 258, 1,8617 | 0,7625 | 2,6242 |
| D | `kimi-k3.1-pro` | 3 (3), 79 137 / 45 248, 0,6107 | — | 0,6107 |
| E | `gpt-6-astra` | 3 (3), 66 773 / 18 912, 1,6133 | 0,3649 | 1,9782 |
| **total** | | **10,0142** | **1,1274** | **11,1416** |

Sorties d'Astra comptées réflexion comprise (2 302 jetons de raisonnement sur les trois cellules, 512 à la consultation).

- **Total consigné de ce tour : 11,14 USD ≤ 15** (pire cas des devis 16,53 ; plafond du run 13,87, non atteint).
- **Cumul de la ligne GO-2026-11-12-04 : 23,38 + 11,14 = 34,52 USD sur 40** (reste 5,48 ; un quatrième tour à 15 USD ne
  tiendrait pas sous le plafond de la ligne sans décision).
- Kimi : 0,6107 au barème du script, égal au compte du relais (0,610754 ; 3 appels sur 8 permis, plafond 3).
- Sur les crédits de la clé `RR_ANTHROPIC_API_KEY_RIGAUD` (A + B) : **5,9285 USD au barème du script** ; au tarif public
  RAPPORTÉ aux tours 1 et 2 (Fable 5.1 10/50, Opus 4.6 5/25 ; non relu ici) : environ **4,09 USD** (B à 0,9201 au lieu de
  2,7603).
- Hors crédits de Claude, sous le même plafond de tour : Argon 2,6242, Astra 1,9782, Kimi 0,6107.

Ligne proposée pour `registres/depenses.md` : « 2026-11-14 | GO-2026-11-12-04, tour 3 sur 4 | collisionneur étage III à
cinq espèces et consultations à part d'Argon et d'Astra, question "Regard ou raisons" | 11,14 USD au barème du script
(collisionneur 10,01 ; consultations 1,13) | cumul de la ligne 34,52 sur 40 ».

## 5. Incidents, écarts et réserves, déclarés

1. **Aucun incident de fournisseur** : pas de refus, pas de troncature, pas d'échec de transport consigné, pas de reprise.
2. **Question servie** : la consigne de la mère fait servir « le bloc "## Question" de `question-v1.md`, mot pour mot » ;
   l'extrait (tout ce qui suit la ligne `## Question`, guillemets compris, sans la ligne de titre ni l'en-tête qui nomme les
   cinq sources) est versé à part, `question-etage3-servie-v1.md` (`77156e04…`) ; le fichier scellé de la mère n'est pas
   modifié. Dans le run, `question-etage3.md` porte la même empreinte.
3. **Programme des consultations** : la v1 du tour 2 n'impose pas trois modèles (`--modeles argon,astra`) ; elle est
   employée inchangée depuis son chemin, aucune v2 n'est écrite, aucun différentiel n'est donc versé. Ses essais rejoués
   portent sur les trois modèles (factices), comme écrits.
4. **« Réponse brute entière » des consultations** (réserve du tour 2, inchangée) : `reponse-brute.json` porte l'objet
   `Reponse` rendu par la fonction d'appel du script (texte, modèle servi, identifiant de réponse, fin, catégorie, usage,
   types de blocs, échec), non le corps JSON du fournisseur.
5. **Astra, cellule III.1** : 8 157 jetons de sortie comptés (dont 1 761 de raisonnement) pour un plafond demandé de 8 000,
   fin `stop`, statut OK, marqueur présent ; relevé tel quel, non interprété (le coût au barème compte les 8 157).
6. **Interpréteur** : l'environnement Python du bac à sable du tour 1 n'existe plus ; un environnement neuf a été créé dans
   le bac à sable de ce tour (`venv-coll`, Python 3.13.18, `anthropic` 2.3.0, installé depuis le registre de paquets),
   employé avec `-I -B` ; routine, sans dépense.
7. **Lancement** : depuis la session mère, sans crochet de garde ; les trois commandes lancées sont celles du devis, mot
   pour mot, une invocation chacune, en tâches de fond de la session (délais explicites : une heure pour les consultations,
   deux heures pour le relais et le run). La tâche du relais s'est terminée avec le code 144 : c'est l'arrêt demandé par son
   numéro de processus.
8. **Consoles et journaux** : recherche de motifs de clés (`sk-ant-`, `sk-`, `ghp_`, `hf_`, `AKIA`, `AIza`, et `org-`,
   `organization`, `workspace`, `proj_`, `api_key`, `Bearer `) sur toutes les sorties avant copie : **0 fichier touché** ;
   les fichiers sont versés **sans masque** (copies identiques aux originaux du bac à sable ; empreintes des originaux :
   `run-e3-v1/journal.jsonl` `6d619234…`, console du run `0873ae0a…`, console des consultations `783e0cde…`, console du
   relais `30160486…`, journal du relais `2cd63797…`, état du relais après `3257fdbf…`, avant `13331286…`). Les consoles
   portent le chemin du bac à sable.
9. Aucune écriture git ; rien d'intermédiaire versé dans le dépôt pendant le tour (devis, sorties de devis, essais et
   question servie scellés avant le premier appel ; le reste copié à la fin). `bilan-mere-v1.md` et `organisme-v1/` non
   ouverts. Aucune instance Vast ni serveur Hetzner touché.
