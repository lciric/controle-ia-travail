# Mandat du contre-lecteur Fable des deux instruments de la mère pour le juge de sélection — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026. Pièce de travail.

Destinataire : un contre-lecteur neuf, Claude Fable 5.2, d'un autre modèle que la mère (Opus 5.5). Mot de Lazar : « fait relire par fable ». Une contre-lecture Sonnet de la garde a été arrêtée avant sa fin ; son fichier partiel, `contre-lecture-garde-lignee-reconnue-v1.md`, est versé comme interrompu et non employé. Ne le lis pas.

---

La mère a écrit deux petits instruments pour le juge de sélection des cartes de la course d'auto-conception v9. Ils ne remplacent ni ne modifient les trois programmes scellés du juge.

## Pièce 1 — la garde de `lignee_reconnue` (pas encore employée)
- `docs/notes/organisme-auto-conception-v9-mere/juge-selection-manifeste-v1/garde_lignee_reconnue_v1.py` (`5aceb2abb67536381a37952c7cdc0ea602de58c1ff0194c34c791f9c8a4f8a61`) ;
- `essais_garde_lignee_reconnue_v1.py`, même dossier (`e9d183669422752d5f1951355a9b0482a8d453ffbc43a9bbe9641aa68b89b592`).
- Référence du format des lectures : le programme d'assemblage scellé, par `git show origin/lot/compte-organisme-v1:docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v5/assemblage_selection_v4_v2.py` (empreinte commençant par `2f5640da`), fonctions `valider_lecture` et `valider_liste_veto` seulement.

Juge :
1. Refuse-t-elle toute valeur de `lignee_reconnue` qui n'est ni une clé de `familles` du manifeste ni « aucune », dans les cartes comme dans les veto, ainsi que la lignée du lecteur hors de `familles` ?
2. Peut-elle écrire une note, une phrase, une raison ou la valeur fautive ?
3. Codes de sortie 0, 1, 2 : un cas sain et un artefact pour chacun ? Rejoue ses essais en commande simple : `.venv/bin/python -B -m pytest -q -p no:cacheprovider <chemin>`.

## Pièce 2 — l'extraction du cas X6 (déjà jouée : contre-lecture après coup, déclarée comme telle)
- v1 : `docs/notes/organisme-auto-conception-v9-mere/juge-selection-x6-v1/extraire_x6_journal_aiguilleur_v1.py` (`e2da19df…`) et ses essais (`39d282ee…`) ;
- v2 : `extraire_x6_journal_aiguilleur_v2.py` (`004fc6b769089748f969992de1c55a8d44a62df1e46fcf2211c7e8d71ad9dddb`) et ses essais (`0d721e7ec8967fe7813f272ac7244c1ef2a8def142cb479a3d35fe0249f3a127`), même dossier ;
- les pièces de l'agent Sonnet qui les a contre-lues et jouées : `contre-lecture-extraction-x6-v1.md` (`88ed7ece…`), `verification-extraction-x6-v2.md` (`e08ecda8…`) ;
- la règle de la mère, ligne R-4097 de `registres/decisions.md`, et sa source : `orchestrator/pole/aiguilleur_v53.py` au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` du dépôt de l'orchestrateur, lisible en lecture seule par `git -C /tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/orch show FETCH_HEAD:orchestrator/pole/aiguilleur_v53.py` (empreinte commençant par `a856cdaa`). Ne lis rien d'autre de ce dépôt.

Juge :
1. Le programme v2 pouvait-il écrire autre chose que des noms de clés, des comptes, des identifiants, un chemin, une empreinte et une taille ?
2. Le passage de la v1 à la v2 ne dépend-il que d'un nom de clé, sans aucune valeur du journal ?
3. La règle de R-4097 est-elle juste au regard du code de l'aiguilleur : les fiches « retenues » sont toutes celles qui n'ont pas reçu de passeport, et elles sont hors des 94 cartes à passeport, d'où `cartes_attendues` = 94 ?
4. Une fiche retenue pouvait-elle échapper au programme, par exemple un refus ou une réponse illisible classés autrement ?

## Ce que tu ne fais pas
- Tu n'ouvres pas la sortie de l'extraction (`sortie-extraction-x6-v1.json`, `sortie-extraction-x6-v2.json`) au-delà de ses noms de champs et de ses comptes : n'en recopie aucun identifiant.
- Tu n'ouvres rien sous `archives-reponses-modeles/`, aucune carte, aucune lecture, aucune transcription. Tu ne rejoues pas l'extraction.

## Règles
- Aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ; rien sous `/root/.claude/`.
- Pas de code en ligne passé à l'interpréteur (`python -c`, `python -`).
- Aucun nom de commande d'arrêt ou de recherche de processus par motif dans une commande. Aucune recherche de motifs sur un dossier large : chaque fichier s'ouvre par son chemin entier.
- Une commande simple à la fois. Écriture : ta sortie seulement. Ni réseau, ni dépense, ni commit.
- Au premier refus d'outil, de classifieur ou de garde, arrête-toi et dis-le.

## Sortie
`docs/notes/organisme-auto-conception-v9-mere/juge-selection-manifeste-v1/contre-lecture-fable-instruments-mere-v1.md`, scellée par `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.
- Verdict en tête, pièce par pièce : « conforme » ou « à corriger », avec des couples exacts (fichier, avant, après).
- Pour la pièce 2, dis si quelque chose remet en cause la liste X6 ou `cartes_attendues` = 94.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Le chemin et l'empreinte de ta sortie.
3. Cinq lignes au plus : les deux verdicts et ce qui menace le manifeste.
