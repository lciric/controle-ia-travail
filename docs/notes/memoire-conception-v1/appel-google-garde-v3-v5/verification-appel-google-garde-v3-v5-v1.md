# Vérification — appel_google_garde_v3_v5.py

- Fichiers vérifiés :
  - `docs/notes/memoire-conception-v1/appel-google-garde-v3-v5/appel_google_garde_v3_v5.py` (3832e1be…) ;
  - `test_appel_google_garde_v3_v5.py` (1219cea9…).
- Les deux empreintes sont conformes à leurs compagnons. Commit 22b22dba.
- Vérification par le même contre-lecteur, en lecture seule et sans réseau. J'ai lu tout l'écart entre la v4 et la v5.

## Verdict

**Non conforme, une correction courte.** Neon est bien ajouté et son tarif est juste. Je ne trouve aucune régression par rapport à la v4.

Un défaut moyen : un journal associé absent est ignoré sans le dire, et le plafond commun peut alors être dépassé.

## Points vérifiés

1. **Neon — conforme.**
   - Modèle `gemini-4-neon`.
   - Niveau de réflexion « xhigh », donné par la garde.
   - Limite de sortie 65 536 en flux, prise dans la garde.
   - Tarif 3 / 15 USD par million. La page de prix scellée (40202cdd…, section « Gemini 4 Neon », onglet Standard) donne bien 3,00 en entrée et 15,00 en sortie, réflexion comprise. Aucune bascule datée n'y est écrite pour Neon, ce qui concorde avec `collisionneur_v9_v8c.py`, lignes 230 à 237.
   - Pire cas d'un appel à Neon : 1,47 USD.
2. **Plafond de 5 USD — conforme dans son principe.**
   - Le plafond est ramené à au plus 5 USD.
   - La dépense déjà faite est la somme de son propre journal et des journaux associés.
   - Un journal associé illisible est refusé.
   - Un journal associé identique au journal de l'appel est refusé, mais seulement s'il porte le même chemin (voir le point 2 de « Ce qui reste »).
3. **Absence de régression.**
   - Les 53 essais du dépôt passent.
   - J'ai rejoué mes mutations de la v4 sur la v5. Seuls changent les résultats que commande le passage de 3 à 5 USD : N11 (texte du message d'arrêt), N12 (le quatrième appel passe), N13 (deux appels passent après la bascule, au lieu d'un).
   - Six processus lancés ensemble sur un même journal donnent cinq réservations, puis un refus, soit 4,92 USD au plus.

## Ce qui reste

1. **Moyen, lignes 316 à 321 : un journal associé absent compte zéro, sans le dire.** C'est un repli silencieux, contraire à R5.
   - Mutation : trois appels à Carbon, 2,95 USD comptés au pire cas ; puis un appel à Argon dont le journal de Carbon est mal nommé (`carbonn.jsonl`).
   - Résultat : `depense_cumulee_avant_usd` vaut 0 au lieu de 2,95. L'appel part.
   - Avec le bon nom, le même appel compte 3,93.
   - Une faute de frappe suffit donc à dépasser le plafond commun.
   - **Correction** : refuser tout journal associé absent. Le lanceur de la course crée d'abord les trois journaux vides. Journaliser aussi, dans le `.json`, le total lu dans chaque journal.
2. **Faible : un lien symbolique vers son propre journal bloque le script.**
   - Le test d'identité compare `abspath`, qui ne suit pas les liens.
   - Si un journal associé est un lien vers le journal de l'appel, son verrou partagé attend le verrou exclusif que le même processus tient déjà.
   - Mutation : bloqué au-delà de 5 secondes. Rien ne part et rien ne coûte.
   - **Correction** : comparer avec `os.path.realpath`, ou avec `os.stat` (`st_dev`, `st_ino`).
3. **La question de la mère : deux appels lancés en même temps sur deux modèles différents.**
   - Il n'y a pas de dépassement.
   - Chaque appel tient le verrou exclusif de son propre journal pendant qu'il demande le verrou partagé de l'autre. Les deux s'attendent l'un l'autre : c'est un interblocage.
   - Mutation : deux processus, Argon et Carbon, associés l'un à l'autre, sont encore bloqués après 8 secondes. Rien n'est envoyé et rien n'est réservé.
   - **Ce n'est pas un défaut de dépense.** La course les lance l'un après l'autre, et le cas croisé ne coûte rien. Faible.
   - En revanche, la docstring annonce une protection contre un lancement parallèle par erreur. Ce cas-là bloque au lieu de refuser. Il faut soit l'écrire, soit corriger.
   - **Correction simple** : un seul fichier de verrou par course, pris en mode exclusif avant de lire les trois journaux. Autre voie : prendre les verrous de tous les journaux en mode exclusif, dans l'ordre trié de leurs `realpath`.
4. **Remarque, sans défaut.**
   - Un appel lancé sans `--journaux-associes` ne voit que son propre journal. Le plafond commun ne tient que si le lanceur passe toujours les trois journaux.
   - Une course gouvernée par l'ancien plafond de 3 USD doit passer `--plafond-usd 3`, sinon elle prend le défaut de 5 USD.
   - À partir du 30 novembre, le pire cas des trois modèles réunis vaut 1,97 + 1,97 + 1,47 = 5,41 USD, au-delà de 5. En série, le troisième appel passe tout de même, parce que les soldes des deux premiers remplacent leur pire cas par leur coût mesuré. Il ne passe pas si les deux premiers finissent en défaut sans usage.

## Fichiers

- Mutations :
  - `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/mutations_v5.py`
  - `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/parallele_v5.py`
  - `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/croise_v5.py`
- Sorties :
  - `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/sortie_v4.txt`
  - `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/sortie_v5.txt`

## Non vérifié

- Le nom réel que Google renvoie dans `modelVersion` pour Neon : le script refuse « models/… » et les suffixes « preview ».
- La facturation réelle.
- Le verrou sur un système de fichiers en réseau.
