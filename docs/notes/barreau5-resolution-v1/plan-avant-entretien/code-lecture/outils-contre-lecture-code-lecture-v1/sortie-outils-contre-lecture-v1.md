# Sorties des outils du contre-lecteur du code de lecture du barreau 5 — v1

Jouées le 20 novembre 2026 sur le code du commit `8c1d6918` (`lecture_v1.py` : `c3db0074…`). Aucune donnée : mondes fabriqués, dépôt git jetable, énumérations. Temporaires sous `/dev/shm/b5f-contre-lecture/`, copie de travail sous le bloc-notes de la session ; effacés.

## Essais rejoués (sans mutation)

Les quatre fichiers du paquet de lecture : **134 passés, aucun échec**, en 192 s.

## Mutations (`mutations-contre-lecture-v1.py`)

Témoins sans mutation verts : lecture, 83 passés ; sondes et relecture, 37 passés. **8 jouées, 2 attrapées, 6 manquées.** Aucune des six n'est équivalente : chacune change une sortie ou admet un registre que le texte refuse.

| id | fichier | défaut réintroduit | état | premier essai en échec |
|---|---|---|---|---|
| C1 | lecture | probabilité rapportée de « séparé » prise sur la somme des rangs positifs (nombre de la phrase au jury) | **manquée** | — |
| C2 | lecture | issue E sans que la séparation apprise soit établie | **manquée** | — |
| C3 | lecture | issue E sans valeur absolue (un grand écart négatif admis) | **manquée** | — |
| C4 | lecture | garde d'ouverture : épreuve à vérité plantée non exigée avant les scores, ni avant l'ouverture | **manquée** | — |
| C5 | lecture | garde d'ouverture : table reçue non comparée à `OUVERTURE-B5F` | **manquée** | — |
| C6 | lecture | E2b : rapport des poussées inversé | attrapée | `test_monde_force_seule_issue_d_force_non_ecartee` |
| C7 | lecture | M1 et M3 : tâches jouées par l'un des membres au lieu de tous | **manquée** | — |
| C8 | sondes | la sonde d'un pli note les actions de l'autre pli | attrapée | `test_jouet_de_bout_en_bout_relecture_sondes_puis_lecture` |

C8 n'est attrapée que par le jouet de bout en bout (deux minutes) ; aucun essai rapide des sondes ne la voit.

## Sondages (`sondages-contre-lecture-v1.py`)

| sondage | question | résultat |
|---|---|---|
| S1 | Sous l'issue « non interprétable », le résultat porte-t-il des lectures de sondes ? | **Oui.** Issue NI ; séparation apprise écrite ; épreuves écrites, dix différences de E3 ; sonde de comparaison et couches 7 et 23 écrites ; la phrase dit pourtant « rien n'est lu des sondes ». |
| S2 | Une famille sans sur-saboteur (T02) reste-t-elle dans M1 ? | **Oui.** M1 : dix familles, somme admise 3, T02 comprise. E1 : neuf familles, somme admise 1, sans T02. M3 : neuf familles. |
| S3 | Un fichier `.sha256` de l'arbre de lecture qui porte la table passe-t-il la garde d'ouverture ? | **Oui**, sous `table.sha256` comme sous `scores/notes.sha256` : l'ouverture se fait, issue S. Témoin : la même table sous `table.json` est refusée (« hors de l'inventaire »). |
| S4 | `exiger_code_de_lecture_au_commit` tient-elle son cas sain et ses artefacts ? | **Oui.** Acceptés : cas sain, commit de registre par-dessus, retour au sain. Refusés : arbre de travail changé sous `src`, fichier non suivi sous `src`, tête au code changé, commit absent. Aucun essai du dépôt ne le joue. |
| S5 | Le dénombrement et les seuils égalent-ils une énumération écrite ici ? | **Oui**, de 0 à 12 familles, aux deux niveaux ; seuils égaux à la table du texte (10 : 3 ; 9 : 1 ; 8 : 0 ; 7 et 6 : aucun à 99 % ; 7 : 2 et 6 : 0 à 95 %). Rangs des égalités et des zéros égaux au pire de tous les ordres sur 800 tirages. |
| S6 | Quelle est la plus petite « borne » que peut écrire la phrase E ? | Jamais négative : des différences toutes négatives rendent « contraire ». Mais elle peut être minuscule : un seul écart positif d'un millionième suffit à huit familles, trois à dix. |
