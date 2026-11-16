# Contrôle indépendant : préparation à blanc de la relecture exploratoire v2 (v1)

Début : 2026-11-14 22:33:26 UTC. Fin : 2026-11-14 22:35 UTC (dernière lecture d'heure 22:34:49 avant écriture).

## Verdict

**Go avec réserves.** La préparation, jouée sous `unshare -n` avec les mêmes arguments que le point 4, donne exactement les
valeurs attendues (point 4 et K2). Mais la commande du point 4 telle qu'écrite ne peut pas être jouée « à blanc » avec une
sortie hors du dépôt : l'outil refuse (voir constat 1). Rien n'a été envoyé, aucune clé lue ni affichée.

## Constats

1. **Le point 4 refuse tout `--sortie` autre que `<racine>/docs/notes/organisme-conception-propre-v1/lecture-g1-v3-2/envois`**
   (code 2, garde C6 « un seul dossier d'envois »). Premier essai avec un dossier `mktemp -d` : refusé, rien écrit. Je n'ai pas
   contourné la garde. J'ai utilisé l'option prévue de l'outil, `--racine`, sur une racine temporaire (copie par `cp --parents`
   des seules pièces épinglées : 8 pièces, prix, trois pièces de la première lecture, fiches validées et manifeste de fin du
   run, avec leurs compagnons `.sha256`), et `--sortie` sous cette racine. Écarts avec la commande exacte : `--racine` ajouté ;
   `--sortie` et la racine hors dépôt. Tout le reste identique (fiches, attestation v2 du dépôt, effort medium, palier flex,
   plafond 6.5, dépense antérieure 0).
2. **Sortie de `preparer`** : `"pile": 43`, `"lots": [5,5,5,5,5,5,5,4,4]`, `"appels": 18`, `"palier": "flex"`, prix 5.0 / 0.5 /
   25.0, `"pire_cas_total_usd": 19.73713`, `"plafond_usd": 6.5`, `"appels_surs_au_pire_cas": 5`, `max_completion_tokens` 32768,
   `reasoning_effort` medium. Code 0. Toutes les valeurs attendues concordent.
3. **K2 sur le manifeste temporaire** : `outil-lecteur-conception-propre-v3-2-1 flex medium flex (5.0, 0.5, 25.0) 6.5 0.0 18 True b955e730 bb4f903f 1b7973f3`, identique à l'attendu. Champs lus seulement : aussi attestation `4bfacd35`, 23 fiches, 38 fichiers au manifeste, 78 fichiers dans le dossier, `service_tier` flex, `store` faux. Aucun texte d'envoi lu.
4. **Attestation v2** : compagnon vérifié (`OK`) avant la préparation.
5. **K1 rejoué** : six empreintes `OK`. **K8 (avant)** : une seule ligne (`manifeste-envois-v3-1.json`). `lecture-g1-v3-2` : **absent** dans le dépôt avant et après. `git status` propre avant mon rapport.
6. **Nettoyage** : j'ai effacé par chemin exact `/tmp/tmp.tnrhPpO9fM` (racine temporaire) et `/tmp/tmp.nFD6dk4nKe` (premier dossier, resté vide après le refus) ; les deux sont absents. (Un fichier d'aide `/tmp/claude-0/tmpdir-pab.txt` aussi.)
7. **Limite du blanc** : la racine temporaire ne contient pas le reste de `docs/` et `runs/`, donc `verifier_unicite` n'a pas été éprouvée contre le dépôt entier (K8 rejoué à la main suffit, une ligne). La garde de dossier unique est elle-même éprouvée par le refus du constat 1.

## Jugement sur r6 (un arrêt du premier appel tue le dossier unique) : la commande du point 6

Lu dans l'outil (sans rien envoyer) :

- Variables gardées : `PATH HOME HTTPS_PROXY https_proxy SSL_CERT_FILE OPENAI_API_KEY`. Dans cette session, ces six existent
  (noms seuls vérifiés ; valeurs de clé jamais lues). L'outil lit `SSL_CERT_FILE` pour son contexte TLS (ligne 755) et le
  mandataire par l'environnement (urllib) : donc le jeu gardé est **suffisant**. `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`,
  `NODE_EXTRA_CA_CERTS` ne servent pas à l'outil. `-I` ne gêne pas ces variables.
- `NO_PROXY`/`no_proxy` retirés : sans effet gênant (tout passe par le mandataire ; au pire cela corrige une exclusion).
- Clé : `lire_cle` refuse (absente, vide, caractère hors ASCII imprimable) **avant tout journal et tout envoi** : ce cas ne
  tue pas le dossier. Les erreurs de clé et de format sont donc sans risque pour r6.
- **Failles probables, non éprouvables hors réseau** : (a) le mandataire de l'agent doit laisser passer `api.openai.com` (liste
  d'hôtes autorisés) ; un 403 du mandataire ou un échec TLS survient après l'écriture de la ligne d'envoi au journal : « aucune
  reprise », dossier perdu. (b) clé valide mais sans accès au palier Flex ou au modèle servi. (c) délai de 1800 s dépassé pour un
  lot qui raisonne longtemps. Aucune de ces trois n'est une faute de la commande ; elles sont le risque r6 lui-même.
- Aucun défaut dans la commande : chemins relatifs (à jouer **depuis la racine du dépôt**), `exec` dans le sous-shell,
  `--envois-max 1`.

**Recommandation** : avant le point 6, un essai gratuit hors outil prouvant que le mandataire laisse passer l'hôte
d'OpenAI avec cette clé et ce certificat (par exemple une demande de liste des modèles, sans coût, par un geste séparé validé
par Lazar) ; je ne l'ai pas fait (interdit : aucun appel réseau). Sans cet essai, la probabilité d'un arrêt par
mandataire ou TLS reste inconnue, non nulle.

## Réserves

- Le point 4 doit être corrigé dans le rapport ou la note de lancement si un blanc est voulu : `--racine <temporaire>` est la
  seule voie, ou accepter l'absence de blanc.
- Aucune permission ni classifieur n'a refusé un geste de ma part ; le seul refus est celui de l'outil (constat 1).
- Rien envoyé ; sous-commande `envoyer` jamais jouée ; aucun identifiant de modèle de ma famille écrit ici (« modèle C »).
