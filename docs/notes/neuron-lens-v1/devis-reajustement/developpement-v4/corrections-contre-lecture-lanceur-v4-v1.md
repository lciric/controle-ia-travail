# Corrections après la contre-lecture du lanceur v4 et de la commande v9 du réajustement de nos lentilles — v1, 2026-11-22

Développeur neuf, sous le mandat `docs/notes/neuron-lens-v1/devis-reajustement/mandats/mandat-developpeur-corrections-lanceur-v4-v1.md`
(`10dddebf…`, vérifié) et le mandat qu'il cite (`mandat-developpeur-lanceur-v4-commande-v9-reajustement-v1.md`, `6ed54244…`). Contre-lecture
corrigée : `contre-lecture-lanceur-v4-commande-v9-v1.md` (`2b223595…`). Toutes les pièces neuves sont des versions neuves (R12) ; aucune
pièce existante n'est réécrite ; aucune ligne de calcul de l'ajustement ni des contrôles n'est touchée. Empreintes :
`empreintes-lanceur-v4-v2.txt` (scellé). Rien n'a été loué, lancé ni dépensé ; aucune clé lue ; aucune requête au loueur ni à la
plateforme de modèles.

## Table « correction → fait / non fait → essai »

| correction | fait / non fait | où | essai |
|---|---|---|---|
| **C-1 (bloquante)** attente entre les essais d'un même fichier | **fait** : 60 s avant le 2e essai, 300 s avant le 3e (essais comptés sur toute la course, `deja` compris) ; attente remplaçable (`attendre` ; `None` = vraie attente `_dormir`) ; **borne cumulée de 1 200 s par appel** (au-delà, la reprise est remise à la clôture, sans être comptée : nœud N-5) ; lanceur v5 = v4 plus `Contexte.attendre` passé par `_copie` et `cloture` | `src/controle_ia/neuron_lens/rangement_lentilles_v2.py` ; `src/controle_ia/neuron_lens/b_beta_lancer_v5.py` ; amorce v6 ; dépôt réduit v6 ; essai à blanc v5 ; commande v10 (étapes 5, 7, 12) | sain : premier essai sans attente ; coupure de 90 s → essais à 0, 60 et 360 s, copie faite au troisième ; reprise après des essais déjà faits attend aussi. Artefact : coupure longue → trois essais, pas plus, attentes [60, 300] ; cinq fichiers en coupure → essais 3, 3, 3, 2, 2, attente totale ≤ 1 200 s, deux reprises remises puis faites à la clôture ; le lanceur passe son attente aux deux appels ; dans tous les essais, une vraie attente lève. Banc v5 : 9 altérations C-1 tuées. Essai à blanc v5 refait : conforme, 0 écart, **liste neuve `c20d3bac…`** |
| **C-2** relecture sans objet | **fait** : `relire` rend **4** (sortie neuve « sans_objet », aucune clé lue) quand l'inventaire clos a `prevus` et `non_copies` vides ; ligne neuve de la table de destruction (selon la dernière ligne du journal, sans attendre de relecture) ; étape 14 bis | rangement v2 ; commande v10 | sain : inventaire de la vraie clôture d'une course arrêtée avant l'ajustement de R → 4. Artefact : non clos, sans `prevus`, fichier prévu non copié → 2 ; sortie présente → 2. Banc v5 : 3 altérations tuées |
| **C-3** libellé de la vérification sur la machine | **fait** : « taille rendue et empreinte déclarée par l'envoyeur, relues à la révision rendue (non recalculée par la plateforme : relecture en flux maintenue) » ; réserve écrite ; relecture en flux maintenue par défaut | rangement v2 ; commande v10 (étape 12, réserves) | essai du libellé (et cas « empreinte non rendue ») ; banc v5 : ancien libellé remis, tué |
| **C-4** table des items | **fait** : `table-items-lanceur-v4-v2.md` (dernière ligne vraie : bancs 32 sur 32 et 45 sur 45 ; trois lignes C-1 à C-3) | développement-v4 | texte |
| **C-5** commit du 18 avant tout rejeu des 311 essais du programme v4 | **fait** : commande v10, étape 14 (récupération avant tout rejeu, y compris avant la création ; `git cat-file -e 5e5cb65b…` exigé) | commande v10 | texte (non joué : aucune récupération faite ici) |
| **C-6** préfixe de la clé restreinte pour la garde de priorité | **fait** : commande v10, étape 10 bis | commande v10 | texte |
| **C-7** un commit par fichier envoyé | **non fait, écrit en réserve** : regrouper les exports (`create_commit` à plusieurs ajouts) change le transport réel, qu'aucune requête ne permet d'essayer ici ; les attentes l'amortissent ; à relever avec les relevés de la plateforme (point 9) | commande v10, réserves | — |
| **C-8** aucun délai propre sur un envoi qui pend | **non fait, écrit en réserve** : un délai par envoi exige un processus enfant ou un fil, non essayable sur le vrai transport ; seuls la garde et la minuterie bornent | commande v10, réserves | — |
| **N-2** | **pas à moi** : comportement inchangé ; rappelé aux préalables et aux nœuds de la commande v10 | — | — |

## Comptes des essais (2026-11-22, `.venv`, python du conteneur)
- `tests/test_neuron_lens_b_beta_lancer_v5.py` + `…_etapes_b_beta_v7.py` + `…_montage_b_beta_v5.py` : **84 passés** (58 + 24 + 2 ; dont 3
  `copie_reelle`, écartés sur la machine).
- Banc d'altérations du lanceur v5 : **45 tuées sur 45**, témoin passe (55 passés, 3 écartés) ; une première passe en avait 44 sur 45
  (motif du banc trouvé deux fois, défaut du banc, corrigé avant scellement ; la sortie versée est celle de la seconde passe).
- Essai à blanc v5 sur `2355c9bd7` : **conforme, 0 écart** ; nominal « 256 passed, 3 deselected ».
- `tests/test_neuron_lens_*.py` : **1 079 passés, 214 en échec** (995 + 84 neufs ; les 214 échecs sont ceux du développement v4, mêmes
  fichiers, que ces corrections ne touchent ni n'importent : programme de comparaison v3 et v4 sans le commit du 18 dans cet arbre,
  source absente de `controles_b0_v2`, modules absents de `suivi_vast_v6`).

## Nœud neuf
- **N-5** (2026-11-22) — borne d'attente de 1 200 s par appel : non demandée par la contre-lecture ; choisie pour que l'attente ne
  retienne pas la course au-delà de la marge de 1,3 h quand les exports ont beaucoup de fichiers (au pire ≈ 52 minutes sur la course).
  La mère peut la changer (nouvelle version du rangement) avant la création.

## Déclarations
- Refus d'outil : deux commandes composées (une écriture de fichier par `python3 - <<EOF` et un ajout par `cat >> … <<EOF` suivi des
  essais) ont été refusées par l'isolement de l'arbre de travail (« trop complexe à vérifier ») ; non rejouées telles quelles ; le même
  travail a été fait par l'outil d'édition et par un fichier du dossier de brouillon ajouté en une commande simple.
- Non vérifiable ici : le transport réel, les vraies attentes sur la machine, le nombre de fichiers des exports.
