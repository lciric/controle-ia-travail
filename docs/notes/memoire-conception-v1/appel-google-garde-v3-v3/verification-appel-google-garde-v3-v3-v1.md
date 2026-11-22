# Vérification des corrections — appel_google_garde_v3_v3.py

Pièces vérifiées : `docs/notes/memoire-conception-v1/appel-google-garde-v3-v3/appel_google_garde_v3_v3.py` (ab763f35…) et son fichier d'essais `test_appel_google_garde_v3_v3.py` (46cd2761…). Les deux empreintes sont conformes à leurs compagnons. Commit c3d839d7. Vérification faite par le même contre-lecteur, en lecture seule, sans réseau.

## Verdict

**Non conforme, de très peu.** Les trois points moyens de la v2 sont corrigés, et les points faibles aussi, sauf deux formes d'écriture de la limite de mots qui restent mal lues (point 5 ci-dessous).

La v3 tient le refus avant l'envoi, la dépense et le verrou : six processus lancés en même temps sur le même journal donnent trois appels acceptés et trois refusés, soit 2,95 USD réservés au plus.

Deux défauts restent sur la lecture de la réponse. Chacun se corrige en quelques lignes :
1. Une coupure de connexion du type `http.client.IncompleteRead` fait tomber le script : rien n'est journalisé.
2. Un texte `None` envoyé par le modèle est lu comme la réponse « None ».

## Points de la v2, un par un

| Point de la v2 | État | Preuve |
|---|---|---|
| 1. Modèle servi au nom suffixé | corrigé | « -lite » refusé (N1), « -001 » admis (V7) ; « -preview-… » et « models/… » refusés (V8, V9), ce qui reste du côté sûr |
| 2. Coût compté sur un usage partiel | corrigé | M8, M4, M5 et M9 comptent le pire cas, 0,983 USD |
| 3. Appels en parallèle | corrigé | verrou `fcntl` de la lecture jusqu'à la réservation ; six processus simultanés : codes [1, 1, 1, 3, 3, 3], trois réservations et trois soldes |
| 4. NaN, Infinity, montant négatif, solde sans réservation, ligne sans identifiant | corrigé | N2, N4, N3, V14 et V15 sont refusés avant l'envoi |
| 5. Morceau de flux mal formé | corrigé en partie | N9 donne `FLUX_ILLISIBLE` ; restent V3 à V6 (points 2 et 3 ci-dessous) |
| 6. Limite de mots écrite en lettres | corrigé | N5 et V10 refusés ; « en deux mots » est refusé aussi, ce qui reste du côté sûr |
| 7. Bascule du tarif | corrigé | le 30 novembre à 23:00Z, le tarif haut est appliqué (N8) |
| 8. Empreintes des gardes | corrigé | un compagnon faux est refusé (V16) ; énoncé de plus de 400 000 octets refusé (M15) ; ligne de plus de 20 000 signes refusée (V13) |

Les essais du dépôt passent : 38 sur 38. Les 18 mutations de la v1 et les 13 de la v2, rejouées sur la v3, donnent toutes le résultat attendu, sauf N10 (point 2 ci-dessous).

## Ce qui reste

1. **Moyen, lignes 282 à 290 : coupure de flux non attrapée.** `http.client.IncompleteRead`, et plus largement `http.client.HTTPException`, ne descendent pas de `OSError`. C'est pourtant l'erreur ordinaire d'un flux découpé qui se coupe. Mutation V1 : le script s'arrête sur une exception, sans `.json` et sans ligne de solde.
   - La dépense reste sûre : le pire cas réservé reste compté.
   - Mais le défaut n'est pas journalisé, ce que demande la règle « Appels aux modèles de Google ».
   - **Correction** : ajouter `http.client.HTTPException` au second `except`. Mieux : un `except Exception` final qui écrit un défaut `RESEAU_<type>`.
2. **Moyen-faible, ligne 192 : un texte `None` devient la réponse « None ».** `str(part["text"])` transforme `None` en la chaîne « None ». Mutations N10 et V3 : la réponse « None » est acceptée, avec le code de sortie 0. C'est contraire au point 11 de la docstring.
   - **Correction** : si `part["text"]` n'est pas une chaîne, `raise TypeError`, ce qui donne `FLUX_ILLISIBLE`.
3. **Faible, lignes 291 à 304 : types inattendus dans la réponse.** Ces valeurs ne sont pas contrôlées et font tomber le script après la réservation, sans `.json` :
   - un compte de jetons sous forme de chaîne dans `usageMetadata` (V4) ;
   - un `finishReason` qui n'est pas une chaîne, par exemple une liste (V5) ;
   - un `promptFeedback` qui n'est pas un dictionnaire (V6).
   - **Correction** : dans `lire_flux`, exiger des entiers pour les comptes, une chaîne pour `finishReason` et un dictionnaire pour `promptFeedback` ; sinon `FLUX_ILLISIBLE`.
4. **Faible : texte partiel perdu sur une coupure réseau.** Sur une coupure au milieu du flux (V2, délai dépassé), le défaut `RESEAU_TimeoutError` est bien journalisé. Mais le texte déjà reçu est perdu, parce que `lire_flux` ne rend rien quand il lève une exception. La règle « récupérer ce qui est récupérable » le demande.
   - **Correction** : accumuler le texte dans un état modifiable passé à `lire_flux`, puis l'écrire en `.defaut.md`.
5. **Faible, résiduel : deux formes de limite de mots passent sans être lues.**
   - « 10k mots » accompagné de « 3 mots-clés » donne une limite lue de 3 (V11).
   - « 5000 words » accompagné de « 3 mots » donne aussi 3 (V12).
   - Après l'appel, le défaut MAX_TOKENS reste attrapé.
   - **Correction possible** : refuser « mots » précédé d'un nombre suivi d'une lettre (`\d+\s*[kK]`), et refuser « words ».
6. **Faible : la protection des gardes dépend de leurs compagnons.** Les empreintes des gardes sont comparées à leurs compagnons, et non à une valeur écrite dans le script. Une garde modifiée puis rescellée passerait.
   - **Correction possible** : figer les deux empreintes attendues comme constantes dans le script, comme pour la page de prix.

Les deux choix écrits dans la docstring sont acceptables : le journal se scelle à la fin de la course, et les appels se font l'un après l'autre. Le verrou rend le second sans danger.

## Fichiers

- Mutations de la v3 : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/mutations_v3.py`. Elle contient M1 à M16, N1 à N13 et V1 à V16. L'essai à six fils V17 n'y donne pas de lecture fiable, parce que la redirection des sorties n'est pas sûre entre fils ; il est remplacé par l'essai suivant.
- Essai de six processus en parallèle : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/parallele_v3.py`.

## Non vérifié

- La forme réelle de `modelVersion` chez Google : si Google renvoie un suffixe de type « preview », le script le refusera.
- Le comportement réel de facturation lors d'une coupure.
- Le parallélisme sur un système de fichiers en réseau : le verrou `flock` y est moins sûr.
