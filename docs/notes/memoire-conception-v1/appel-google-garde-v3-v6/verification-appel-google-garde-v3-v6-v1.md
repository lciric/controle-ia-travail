# Vérification — appel_google_garde_v3_v6.py

- Pièces vérifiées :
  - `docs/notes/memoire-conception-v1/appel-google-garde-v3-v6/appel_google_garde_v3_v6.py` (9a8b01c2…) ;
  - `test_appel_google_garde_v3_v6.py` (6443eca4…).
- Les empreintes sont conformes à leurs compagnons. Commit 27f4e278.
- Vérification par le même contre-lecteur, en lecture seule et sans réseau. J'ai lu tout l'écart entre la v5 et la v6.

## Verdict

**Conforme.** Les points 23 et 24 corrigent le défaut moyen et les deux défauts faibles de la v5, sans régression.

## Points de la v5, un par un

1. **Journal associé absent — corrigé.**
   - Une faute de frappe (`carbonn.jsonl`) produit un refus, et rien ne part.
   - Avec les bons noms, le `.json` note le total de chaque journal : `argon` 0 USD, `carbon` 2,94924 USD, `neon` 0 USD, soit 2,94924 USD au total.
2. **Lien symbolique et doublons — corrigé.**
   - L'identité des journaux est jugée par `realpath`.
   - Un lien symbolique vers son propre journal est refusé tout de suite, au lieu de bloquer.
   - Un journal associé donné deux fois est refusé.
3. **Interblocage croisé — corrigé.**
   - Tous les journaux de la course sont verrouillés en exclusif, dans l'ordre trié de leur chemin réel, de la lecture jusqu'à la réservation.
   - Deux processus lancés ensemble, Argon et Carbon, chacun associé à l'autre, se terminent tous les deux : une réservation et un solde par journal.
   - Près du plafond (3,5 USD déjà comptés, puis deux appels simultanés de 0,98 USD), un seul appel passe : codes de sortie [3, 1].
4. **Absence de régression.**
   - Les 57 essais du dépôt passent.
   - Mes mutations de la v5 (M, N, V, W) donnent sur la v6 une sortie identique à celle de la v5.
   - Six processus lancés ensemble sur un même journal donnent cinq réservations, puis un refus.

## Remarques, sans défaut

- Le solde (`ajouter_journal`) ne verrouille que le journal de l'appel. C'est suffisant : un solde ne fait que remplacer le pire cas réservé par le coût mesuré.
- Le plafond commun ne tient que si le lanceur passe toujours les journaux des trois modèles.

## Fichiers

- Mutations :
  - `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/mutations_v6.py`
  - `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/parallele_v6.py`
  - `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/croise_v6.py`
- Sortie des mutations : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/sortie_v6.txt`

## Non vérifié

- Le nom que Google renvoie réellement dans `modelVersion`.
- La facturation réelle.
- Le verrou `flock` sur un système de fichiers en réseau.
