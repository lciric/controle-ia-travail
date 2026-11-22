# Contre-lecture de la commande de création v3 (essai 3 du palier 0b) — v1

Contre-lecteur : sous-agent Opus neuf, lecture seule, n'ayant écrit aucune des pièces (classe B, demande de la mère de 07:32Z). Rapport recopié tel quel.

Verdict : Conforme avec réserves. Les trois commandes passent les contrôles du fabricant et de l'outil, et toutes les empreintes concordent. Il manque trois précisions avant l'envoi : le délai de 2 h entre fabrication et création, le sort du fichier `SORTIE` après l'envoi, et l'écart avec la voie (a) du devis v5.

1. **Diff des versions.** De la v1 à la v2, seuls changent les points que la v2 déclare. De la v2 à la v3, un changement n'est pas déclaré : le titre « ## Commandes, dans cet ordre, depuis la session du compte organisme » (lignes 17-18 de la v2) a disparu. Les trois commandes n'ont plus de titre de section, et la mention « dans cet ordre » est perdue. Sinon, rien ne change hors de ce qui est déclaré.

2. **Contrôles du code.**
   - `CONTROLE_IA_GITHUB_TOKEN_2` passe la forme de nom (ligne 50 du fabricant) et ne figure pas parmi les noms réservés (ligne 51).
   - `SORTIE` est absolu. `/home/user` n'est pas un dépôt git (`rev-parse` rend 128), donc la ligne 65 passe. Le dossier et les six fichiers sont absents, comme voulu.
   - Le troisième argument est l'empreinte complète `f61aea46…`. Aucune variable `FABRICANT_*` ni `CONTROLE_BANC` n'est posée. `.venv/bin/python` existe.
   - L'outil reçoit 2 arguments de position plus le mode ; les relevés sont neufs (ouverture en mode `x`). Codes attendus : 0 à blanc, 0 si Hetzner répond 201.
   - Réserve : le mode 700 du dossier parent n'est contrôlé par aucune des deux pièces. Il ne tient qu'au `mkdir -m 700`.
   - Réserve : le préalable 3 dit « contrôlées juste avant le fabricant », mais l'empreinte du texte réduit `061f7993…` ne peut être contrôlée que par le fabricant lui-même (ligne 132) et par l'outil (ligne 53).

3. **Empreintes sur disque.** Toutes concordent avec leur compagnon `.sha256` : commandes v1 `4129b36a…`, v2 `a4bb9308…`, v3 `e5d12b6a…` ; fiche `bc985b68…` ; devis v5 `452e7bcf…` ; contre-lecture de la v2 `2ff48cd6…` ; fabricant `a91f3403…` ; script v6 `f61aea46…` ; amorce `524cfc4a…` ; réducteur `b1a4d216…` ; outil `73046b31…`. Les quatre pièces épinglées concordent aussi : `b989db6e…`, `64b2c0ce…`, `ba39fe9b…`, `b333b2eb…`. Le texte réduit n'existe pas sur disque. Seul son compagnon `essais-resultats/v8/e0/v8.script-reduit.sh.sha256` porte `061f7993…`. La ligne GO-2026-11-22-04 est bien sur `origin/main`.

4. **« Après l'envoi ».**
   - (a) La garde des 2 h est cohérente avec le script. Un échec avant le pas a ne pousse rien (pas de `$V/.git`), et un jeton invalide au pas b (code 41) ne pousse rien non plus.
   - (b) Non écrit dans la commande : le script refuse si l'heure H0_PREVU date de plus de 7 200 s au démarrage de la machine (`AGE_MAX`, ligne 248, code 21, sans poussée). Les commandes 2 et 3 doivent donc suivre la commande 1 en moins de 2 h, sinon environ 2 h de serveur sont payées pour rien.
   - (c) L'arrêt du gardien est fixé à H0_PREVU + 94 h, et H0_PREVU est l'heure de fabrication, antérieure à la réponse. La destruction à H0 (réponse) + 98 h laisse donc au moins 4 h de marge : cohérent avec la fiche (point 3).
   - (d) Écart avec le devis v5, paragraphes 5 et 6 : la voie (a) recommandée crée, alimente, relève et détruit depuis le poste de Lazar, et écarte expressément le clonage depuis le serveur. La v3 suit une autre voie, autorisée par la ligne de GO et la fiche, mais elle cite la dépense « au devis v5 » sans nommer l'écart.

5. **Fuites du jeton.**
   - Aucune par ligne de commande : nom seulement, `printf` est une commande interne, `declare +x J`, puis `unset`.
   - Aucune dans les journaux : l'outil n'écrit que des empreintes, et la réponse est expurgée de `root_password` et `user_data`. Les fichiers annexes (`.sans-jeton`, `.charge.b64`, etc.) portent `@JETON@`.
   - Restes à traiter : (a) `/home/user/essai-3-sortie/donnees-demarrage` (mode 600) garde le jeton en clair après l'envoi, et la v3 ne prévoit ni de le retirer ni de le garder. (b) Le jeton reste dans les données de démarrage sur le serveur pendant toute sa vie (service de métadonnées, copie de cloud-init), pas seulement dans `/root/essai-3-secret/jeton`. Le rappel de révocation en fin d'essai est donc nécessaire.
   - (c) Le contrôle de branche (ligne 96) interroge le dépôt privé sans jeton : il dépend des accès du relais réseau de la session, sinon refus 8.
   - Aucun chemin non résoluble ne reste.

## Suite donnée (session de l'organisme)
Tous les points sont repris dans `commande-creation-production-essai-3-v4.md` (`aef39cc4…`), voir sa section « Différence avec la v3 ». La v4 est renvoyée au même contre-lecteur pour vérification des corrections.
