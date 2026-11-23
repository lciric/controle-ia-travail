# Contre-lecture 1 de la relance courte de la machine 61875617 (brouillon 1)

Contre-lecteur : Claude Opus 5.5, neuf (rien écrit ici). Heure : 2026-11-22, vers 11:45Z. Rien lancé, rien dépensé, rien poussé ; outil de location : `--help` seul (version 1.11.2).
Texte lu : `sorties-relance/texte-relance-courte-61875617-v1-brouillon1.md`, sha256 `344325770e5888e729ac67e6604f09cc0d7a3d863556b12d6f0b7ba3f612ea48` (vérifié, conforme à l'annonce).
Code lu au commit c97231b38e56fd345a01426cb718b2de6fbfbc6c (empreintes de l'amorce, du lanceur de session et de `location_v1.py` conformes au tableau du texte).
Journal du loueur `logs-61875617-0646.txt` (sha256 `1e3d3057…ae47`, conforme) lu par grep des seuls mots permis.

## Verdict

**Jouable après corrections.** Le chemin du code est bien décrit (poussée par l'amorce, puis 180 s, puis destruction par la minuterie) ; la méthode « arrêt dans la fenêtre » est la seule sûre que je trouve. Un bloquant : la veille est aveugle si le journal du loueur ne se lit pas, et ses bornes de temps (15 min) tombent bien après la destruction (environ 3 à 5 min après le démarrage du conteneur). Un majeur : l'arrêt à la première poussée refusée jette sans besoin la seule chance de pousser.

## 1. Affirmations du texte vérifiées contre le code

| affirmation | verdict | ligne |
|---|---|---|
| Point d'entrée `bash -c "echo <b64> \| base64 -d > /root/amorce.sh && bash /root/amorce.sh"`, réécrit à chaque start, aucun fichier ne le neutralise | vrai | `lancer_iib_v3.sh` l. 317 |
| Compteur de démarrages, ligne `AMORCE IIB v1 DEMARRAGE n : …` (champs awk $1 AMORCE, $2 IIB, $4 DEMARRAGE, $5 n) | vrai | amorce l. 44-47 ; forme confirmée par la ligne 1 du journal versé |
| Échéance et dépense épuisée relues sur le disque ; 1796076000 = 2026-11-30T22:00:00Z ; 1795466525 = 2026-11-23T20:42:05Z (lundi) ; 1795462800 = 2026-11-23T19:40:00Z | vrai (`date -u -d @…`) | l. 162-173 ; journal versé l. 2 |
| Minuterie relancée à chaque démarrage, sortie dans `iib-minuterie.log` (jamais dans le journal du loueur) | vrai | l. 178 |
| Second démarrage sans marqueur : `iib-consigner.sh "redémarrage d'un run interrompu"` (timeout 1200 s), `git add -A runs diag`, ajout forcé des `ids-lot-*`, commit, trace, poussée de la branche extraite (`essai/iib-explo-v6`) seule | vrai | l. 195, 262-320, 348 |
| Trois tentatives, attentes 15 s puis 60 s | vrai (`POUSSEE_ATTENTE_S·k²`, défaut 15) | l. 269 |
| Lignes journal : « poussée : tentative k refusée », « branche $BRANCHE poussée ($1) », « poussée impossible ($1) … » ; elles vont au journal du loueur (`tee`, ligne 195 sans redirection) | vrai | l. 268-269, 312-313 |
| Puis `refus` → « refus : … », « refus annoncé : destruction demandée dans 180 s », `sleep 180`, fichier `iib-detruire`, la minuterie (pas de 5 s) envoie DELETE, réessais 30 min | vrai | l. 118-121, 110-117, 80-105 |
| Aucun calcul ne repart sur ce chemin | vrai (le lanceur n'est appelé qu'après le clonage, l. 243-412, jamais atteint) | l. 182-197 |
| Après 20:42:05Z le 23/11 : marqueur posé, consignation puis destruction **sans** les 180 s | vrai | l. 174-176, 186-190 |
| Poussée initiale faite à 23:30:08Z | vrai | journal versé l. 9 |
| `statut` lu par l'inventaire = `actual_status` (état du conteneur, non l'état voulu) | vrai | `location_v1.py` l. 230, 244-246 |
| Le lanceur scelle chaque lot (`_ecrire` → `sceller`), manifeste scellé sous `runs/<run>/` | vrai | `lanceur_v5.py` l. 132-142, 252-262 ; `manifeste.py` l. 72-76 |
| Outils déjà présents (aucune installation au second démarrage) | vrai en pratique : pas de ligne « outils absents » au premier démarrage | journal versé l. 1-14 |
| `vastai logs` : PUT `request_logs` puis attente du résultat 30 × 0,3 s, **lève** au-delà (~9 s) | non dit dans le texte ; vrai dans le code de l'outil | `vastai/api/instances.py` l. 10-17, 411-426 |

Aucune affirmation fausse relevée. Écart de forme : l'en-tête dit « classe A : ordre d'une course payante » ; la mère le traite en classe B. À trancher par la mère (sans effet sur le fond).

## 2. Bloquant

**B1 — veille aveugle : la destruction peut précéder toute borne.** Après le démarrage du conteneur, la destruction vient à environ « durée de la consignation + 185 s » (2 à 5 min). Or : (i) `vastai logs` peut échouer (attente de 9 s dépassée, erreur du loueur) ; le code de sortie n'est pas lu, la sortie d'erreur est passée à `decider`, qui rend `ATTENDRE` ; (ii) la borne « démarrage non vu » est de 900 s depuis le start. Si le journal reste illisible quelques minutes alors que le conteneur tourne, l'amorce pousse puis détruit avant tout arrêt. Corrections exactes, dans `jouer` :
1. Lire le code de `logs` : `( … "$VAST" logs … ); cl=$?` ; si `cl ≠ 0` ou fichier vide, `L="ILLISIBLE"` sans appeler `decider` ; compter les illisibles consécutifs ; **trois illisibles de suite après le start (environ 45 s) → `arreter "ARRETER : journal du loueur illisible 3 fois"`**.
2. À chaque relevé, lire aussi l'état (`etat "veille-$n"`) ; noter `RUN_VU` au premier `statut=running` ; **si `RUN_VU` est posé et qu'aucune ligne `DEMARRAGE ≥ 2` n'est vue 60 s après → arrêt**. Garder 900 s seulement pour l'attente de la mise en marche (« scheduling »), où un arrêt ne coûte rien.
3. Abaisser `PAS_S` de 10 à 5 s (un relevé ne coûte rien ; cycle réel environ 5 + 1 à 9 s).
4. Ajouter les essais à blanc : j7 (faux outil dont `logs` rend un code 1 trois fois → un seul `stop`) ; j8 (inventaire `running`, journal sans démarrage 2 → arrêt à 60 s, `BORNE` réduite).

## 3. Majeurs

**M1 — ne pas arrêter à la première poussée refusée.** Les trois tentatives et la ligne « poussée impossible » viennent **avant** la ligne « refus annoncé » ; la fenêtre de 180 s ne s'ouvre qu'après. Arrêter dès « tentative 1 refusée » (un refus passager du dépôt distant) ne gagne aucune sûreté et perd la seule poussée possible : tout démarrage futur détruit la machine (N6). Correction : dans `decider`, retirer le motif `*"poussée : tentative "*` ; ordre des motifs : `poussée faite` (ligne `branche $BR poussée (redémarrage d'un run interrompu)`), puis `poussée impossible`, puis refus, puis chemins et calcul inattendus. Garder la ligne « tentative » dans `lignes-d-issue.txt`. Essai d3 réécrit : « tentative 1 refusée » seule → `DEMARRAGE` ; « tentative 1 refusée » puis « branche … poussée (…) » → `ARRETER : poussée faite` ; « poussée impossible » → `ARRETER : poussée impossible`. Liste d'arrêt (§ 10) et N2 à mettre d'accord.

**M2 — mesurer la latence d'arrêt avant de jouer (préalable P10).** La coupure de 12:54Z est un arrêt par l'identifiant sur cette même machine. Relever dans `$D/surveillance.txt` (heures seules) l'écart entre la commande `stop` et la première lecture `statut=exited`. Si l'écart dépasse 90 s : nœud, mot de Lazar avant de jouer (la fenêtre utile après la ligne de poussée est d'environ 180 s moins un cycle de veille et la durée de l'appel `stop`). L'inscrire au compte rendu ; c'est la seule mesure de la réserve « délai entre stop et arrêt effectif ».

**M3 — moyen plus sûr que la fenêtre : aucun trouvé, le texte a raison.** `execute` n'admet que `ls`, `rm` et `du` (aide 1.11.2) : rien ne peut créer `iib-fin-normale` (seul chemin vers le sommeil, l. 186-193) ni `iib-detruire` ; supprimer `iib-minuterie.sh` ne sert à rien (réécrit l. 107) ; retirer `curl` et `python3` (l. 99 : « aucune destruction possible ») déclenche la réinstallation ou `refus_precoce` (l. 147-159) : à proscrire. `update instance --env/--args` recrée le conteneur, effet sur le disque non documenté : à proscrire. Garder la méthode, avec B1, M1 et M2.

## 4. Mineurs

- m1 — `D2` : écrire l'étape `mkdir "$D2"` (sans `-p`, refus s'il existe) avant P2, qui y écrit déjà ; aujourd'hui seule la phrase « refus s'il existe » le dit.
- m2 — essais à blanc : chaque essai passe `VAST="$D2/essais/faux-vastai"` **et** `D2="$D2/essais/<essai>"` explicitement ; le faux outil refuse tout identifiant autre que 61875617 et tout `destroy` ; un essai joué avec le vrai `$D2` poserait `start-fait` et bloquerait la vraie relance.
- m3 — § 7 : `for d in traces/iib-consignation-*/` et `find … -path '*iib*'` prennent aussi les traces anciennes de l'arbre au commit 43d6d067 (extraction partielle) ; restreindre aux chemins de `diff-name-status.txt` (`cut -f2 … | grep '^traces/iib-consignation-' | cut -d/ -f1-2 | sort -u`), sinon faux écarts.
- m4 — § 7 : `python` → l'interprète de la venv de la session (`$DEPOT/.venv/bin/python`, ou `python3 -I -B` avec `PYTHONPATH=src` posé en variable, non `-I`), pour ne pas dépendre de l'interprète courant.
- m5 — `etat()` écrit `inv-$1.json` brut avant le filtre : le masquer ou le supprimer après la ligne filtrée (aujourd'hui seuls `start.json`, `stop-*.json` et le journal sont masqués) ; la garde des secrets du versement le rattraperait, mais autant ne pas le garder.
- m6 — P7 contrôle le jeton de la session, pas celui de la machine (`GH_TOKEN`, nom `$JGHN` à la création) : dire dans P7 si c'est le même jeton ; sinon la réserve du § 9 suffit (M1 laisse au moins les trois tentatives).

## 5. Points tenus (sans correction)

Arrêt toujours par la constante 61875617 (`stop`, `logs`, `start`), refus des cinq identifiants intouchables, aucun `destroy`, un seul `start` gardé par `start-fait`, aucune boucle de relance (second `stop` seul, à 2 min), borne d'heure 19:40Z le 23/11 juste (marge de 62 min sur 20:42:05Z), dépense 0,80 USD au plus (40 min × 1,193 USD/h), vérification fichier par fichier avec `n_v = n_l`, garde des secrets par nombre seul, aucune sortie ouverte, rien poussé par l'exécutante.
