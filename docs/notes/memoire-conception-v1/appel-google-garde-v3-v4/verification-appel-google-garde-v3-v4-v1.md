# Vérification des corrections — appel_google_garde_v3_v4.py

Pièces vérifiées : `docs/notes/memoire-conception-v1/appel-google-garde-v3-v4/appel_google_garde_v3_v4.py` (53e4fee9…) et son fichier d'essais `test_appel_google_garde_v3_v4.py` (97462079…). Les deux empreintes sont conformes à leurs compagnons. Commit 84fc0e4a. Vérification faite par le même contre-lecteur, en lecture seule, sans réseau. J'ai lu tout l'écart entre la v3 et la v4.

## Verdict

**Conforme.** Les points 16 à 20 corrigent tous les défauts restants de la vérification de la v3. Je n'ai trouvé aucun défaut nouveau.

## Points de la v3, un par un

1. **Coupure de flux — corrigé.** Une coupure `http.client.IncompleteRead` devient le défaut `RESEAU_IncompleteRead` (V1, W1). Une autre exception quelconque devient `ERREUR_<type>` (W2, W3). Un corps d'erreur HTTP illisible donne `HTTP_503` (W4). Dans chaque cas, le `.json`, son compagnon et la ligne de solde au pire cas sont écrits. La clé est masquée, même quand elle figure dans le message de l'exception (essai ajouté).
2. **Texte `None` — corrigé.** N10 et V3 donnent maintenant `FLUX_ILLISIBLE`.
3. **Types inattendus — corrigé.** Un compte de jetons en chaîne (V4), un `finishReason` en liste (V5), un `promptFeedback` en chaîne (V6), un compte booléen (W7) ou négatif (W8) donnent tous `FLUX_ILLISIBLE`, au pire cas.
4. **Texte partiel — corrigé.** Le texte reçu avant une coupure est gardé dans le `.defaut.md`, avec son compagnon (W1 : « PARTIEL »).
5. **Limite de mots — corrigé.** « 10k mots », « 2,5k mots » et « 5000 words » sont refusés (V11, W5, V12). « 400 mots » passe toujours (W6).
6. **Empreintes des gardes — corrigé.** Les valeurs figées dans le script sont égales aux empreintes réelles : 923679b5… pour `garde_google_v3.py`, 052ea1e2… pour `relecture_fable_api_v5.py`. J'ai essayé une garde modifiée puis rescellée avec un compagnon juste : elle est refusée par la valeur figée.

## Mutations rejouées

- Les 31 mutations de la v1 et de la v2 donnent le résultat attendu : M1 à M16 et N1 à N13.
- Les 16 mutations de la v3 donnent le résultat attendu : V1 à V16.
- Les 9 mutations nouvelles et les 2 essais ajoutés donnent le résultat attendu : W1 à W9, garde rescellée, clé dans une exception.
- Six processus lancés en même temps sur le même journal donnent les codes [1, 1, 1, 3, 3, 3] : trois réservations, trois soldes, 2,95 USD au plus.
- Les 47 essais du dépôt passent.

Fichiers des mutations :
- `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/mutations_v4.py`
- `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/parallele_v4.py`
- `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/v4_extra.py`

## Remarques, sans défaut

- Une fin STOP suivie d'une coupure (W9) est lue comme un défaut au pire cas. C'est le côté sûr.
- Le suffixe « preview » est refusé par choix, avec une liste fermée de noms. C'est acceptable : si Google renvoie un autre nom, le premier appel tombe en défaut, au prix de son pire cas, au plus 0,98 USD avant le 30 novembre.

## Non vérifié

- Les noms réels que Google renvoie dans `modelVersion`.
- La facturation réelle lors d'une coupure.
- Le verrou `flock` sur un système de fichiers en réseau.
