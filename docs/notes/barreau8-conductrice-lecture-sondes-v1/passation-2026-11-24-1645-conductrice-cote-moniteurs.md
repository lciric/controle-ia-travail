# Passation — conductrice du côté des moniteurs, lecture des sondes sur le saboteur à budget (barreau 8) — 2026-11-24 16:45Z

Session fille `session_01Qi7Gr6acCdYGKsotBtUNvE` de la mère `session_01Qi7Gr3Ggccg85kjmP654WC` ; Opus 5.5 ; jamais exposée au saboteur. Branche `barreau8/conductrice-lecture-sondes-v1` (main fusionné à `459f38c7`). Passation de jalon (consigne de Lazar relayée par la mère : à chaque jalon et à l'approche de la limite d'usage).

## Fait
- Plan du chemin critique v1 (`bb4793bb…`), envoyé à la mère.
- Recette de puissance (condition D-10) lancée à 15:48:37Z : course `20261124-154837-puissance-barreau8`, processus 1593, arbre à part `/home/user/b8-puissance-arbre` sur `main` `426b7200`, manifeste sans réserve. Rythme mesuré ~16 s par répétition : f = 1 fini vers 20:15–20:30Z ; sortie probablement écrite à l'épuisement du budget, vers 2026-11-25T03:49Z, dernières cases « non calculée ».
- Garde de réception r1 à r8 (D-11) : tenue, 15:50:30Z à 16:28Z, bordereau `85bae5dc…` ; sortie versée sans affichage, branche orpheline `reception/barreau8-sortie-garde-v1`, commit `274aac05…`, fichier `abf70d27…`.
- Disque de lecture (D-8) : sondes et planchers reconstitués, empreintes égales à la table des identités (`donnees/`, ignoré).
- Contrôle à blanc de l'attestation de l'ordre par le code v6 : passe (M-3 de l'additif 2).
- Mandats du lecteur, du juge et de l'auditeur, v3 brouillon 3 : `e92f3345…`, `9ae1baad…`, `66a5fb61…` ; contre-lecture, deux vérifications, « conforme » (`98826412…`) ; envoyés à la mère.
- Lignes proposées au registre des décisions : `registres/lignes-a-verser/conductrice-lecture-sondes-b8-v2.md` (`5d65050d…`).

## Reste
- Recette : surveiller ; à la fin, copier `diag/20261124-154837-puissance-barreau8/` et `runs/20261124-154837-puissance-barreau8/` de l'arbre à part vers la branche, committer, pousser, donner chemin et empreinte à la mère.
- Disque de lecture : jouer `preparer-disque-lecture-b8.sh` (copie versée : `docs/notes/barreau8-conductrice-lecture-sondes-v1/scripts/preparer-disque-lecture-b8.sh` ; recette : arbre neuf sur `origin/main`, refus si une des sept lignes manque, livraison rapatriée et ignorée par `info/exclude`, sondes copiées, lien `.venv`) quand la mère a versé extrait des états, attestation de la course, mandats scellés et sortie de la recette.
- Lancer le lecteur neuf sur désignation de la mère (mandat scellé), puis, si déclenché, rien d'autre : auditeur et juge sont lancés par la mère.

## Réserves
- Les lectures du dommage et de la diffusion (côté exposé) ne peuvent pas être jouées telles quelles ; spécification en cours (Fable, GO-2026-11-24-37), cible 27 ou 28 : elles bornent la date de lecture, non la recette.
- La notice v7 sous-estime la durée de la réception (≈ 38 min réelles) : la lecture et l'audit la rejouent ; lancement détaché écrit dans les mandats.

## Prochaine action
Mesurer la durée de la deuxième case de la recette ; compte rendu à la mère vers 18:00Z.

## Instances actives
Aucune machine louée, aucune dépense. Processus locaux : 1593 (recette).
