# Contre-lecture 10, ciblée, de la commande v8 (amorce v6, suivi v4, dépôt réduit v10, essai à blanc v7, pièce `pip`) — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé au commit `736494b4` de `prep/neuron-lens-v1` par la session de reprise (après
14:53:53 UTC) ; rapport lu avant 15:00:15 UTC ; lecture seule (`sha256sum`, `diff`, `bash -n`, lecture ; 61 essais du suivi v4
exécutés, 61 passés ; aucun essai à blanc rejoué). Résumé fidèle (toutes les remarques reprises, formulations raccourcies) ; suites
dans l'en-tête de la commande v9.

**Verdict de tête** : P-2 à P-10 traitées (petits reliquats) ; P-1 (dépense) seulement en partie : la correction écrite à l'étape 7
contient une erreur de grammaire du shell (Q-1) et la persistance du `PATH` entre deux appels n'est pas assurée (Q-2) ; v8 non
scellable telle quelle ; corrections de texte seul ; pièces de code bonnes.

**Empreintes** (vérifié) : les 18 pièces du tableau de la v8 égales au tableau et aux compagnons ; v8 `afb08ad0…` et v7 `b36146d0…`
égales aux compagnons ; `2851f10e` et `736494b4` ne diffèrent que par la v8 et le journal v7 (et compagnons), hors liste du dépôt
réduit : la liste `801b0202…` reste valable ; amorce v5→v6 : 8 blocs ; dépôt réduit v9→v10 : nom de l'amorce et docstring.

**État des remarques de la contre-lecture 9** : P-1 partiellement (Q-1, Q-2) ; P-2 traitée (lsremote : code 14, message propre, aucun
« pousse », poussée réelle faite, seul `ls-remote` falsifié : la branche visée est bien prouvée) ; P-3 traitée (findko 14, findmuet 15
et fichier absent, cpko 15, index 15, etat 15, chacun son message ; restauration `checkout` déclarée ; voir Q-6) ; P-4 traitée, un
reliquat (Q-7) ; P-5, P-6, P-7, P-8, P-10 traitées ; P-9 traitée, un reliquat (Q-8) ; P-11 info.

**Table de destruction** contre `fin()` de l'amorce v6 (vérifié par lecture) : chaque dernière ligne possible est classée sans
destruction à tort ; états joués au journal v7 conformes (lsremote, findko, poussee → « fin sans poussee finale » → aussitôt ; findmuet,
cpko, index, etat, crochet, finale → « POUSSEE FINALE EN ECHEC » → pas sans la mère) ; échec de `pip` → « fin : arret code 1 (commit
verifie) », ligne 4, correct ; cas prudents → « toute autre ».

**Étapes 1, 7 et 8** : `PATH` à l'étape 7 non assuré (Q-1, Q-2) ; survie supposée, non éprouvée (Q-3) ; PID de la garde supposé juste
(commande simple ; si le shell avait le contrôle des tâches, `$!` serait un parent déjà mort : `ps -p` le révélerait) ; PID de la
minuterie faux (Q-1, vérifié par la grammaire).

**Verdicts** : commande v8 après corrections (Q-1 à Q-4) ; amorce v6 **en l'état** (Q-9 facultative ; branches neuves à déclarer, Q-6) ;
suivi v4 et essais **en l'état** ; dépôt réduit v10 **en l'état** ; essai à blanc v7 et journal après corrections mineures (Q-6, Q-7 ;
journal conforme à la v8 ; 18 dépôts = 17 clones et le distant ; chaque nouvel artefact prouve sa branche ; décompte des écarts juste
y compris depuis les sous-shells, seul un excès est possible) ; pièce `pip` après corrections mineures (Q-8).

**Remarques nouvelles**
- **Q-1. Bloquante.** Étape 7 : dans `D=$(…) && [ -n "$D" ] && setsid nohup bash -c "…" > log 2>&1 < /dev/null & echo …`, le `&` met en
  arrière-plan toute la liste `&&` (un sous-shell) : `D` reste vide dans le shell parent (« durée  s », rappel de l'étape 9 incalculable) ;
  `$!` est le PID du sous-shell ; l'arrêter à l'étape 13 laisse vivre le `bash -c` détaché, qui détruira plus tard : arrêt par PID (R10)
  non atteint. Correction : séparer le calcul du lancement ; chemin absolu de l'outil ; PID écrit par le processus lui-même dans un
  fichier.
- **Q-2. Bloquante.** Le `PATH` n'est exporté qu'à l'étape 1 ; l'état du shell ne persiste pas d'un appel d'outil à l'autre (supposé) :
  la minuterie et la garde partiraient vivantes et échoueraient à l'échéance sans bruit (« command not found » ; exception de
  `_vast_prix`). Correction : chemin concret ; préambule au début de chaque commande ; chemin absolu dans la minuterie ; `env PATH=…`
  pour la garde ; contrôle hors du shell courant avant de lancer.
- **Q-3. Moyenne.** Survie des processus détachés et accès à l'outil jamais éprouvés alors qu'un essai gratuit est possible (lancer
  `setsid nohup bash -c 'sleep 90; command -v vastai > témoin' &`, vérifier dans un appel suivant, vérifier l'arrêt par le PID noté).
- **Q-4. Mineure.** PID, durée, heure de création consignés seulement dans la conversation : les verser dans un fichier ; `ps -p` exigé
  « mort » à l'étape 13 ; commande `ps -p` manquante à l'étape 8.
- **Q-5. Mineure.** Aucune borne sur `D` : exiger une plage (par exemple 3600 à 36000 s).
- **Q-6. Mineure.** Branches neuves de la v6 ni jouées ni déclarées : « tete locale illisible », « liste des fichiers indexes
  impossible », « taille illisible », « fichier temporaire impossible », « copie de runs impossible » ; info : le second contrôle
  (`--diff-filter=AM`) ne voit pas un fichier détecté comme renommage.
- **Q-7. Mineure.** Essai v7 : le `grep` qui compte les formes dans les objets n'est pas contrôlé (code 2 → 0 sans écart) ; « les sept
  derniers artefacts à refus » imprécis : nommer `crochet`, `lsremote`, `findko`, `findmuet`, `cpko`, `index`, `etat`.
- **Q-8. Mineure.** Pièce `pip` : « lancée juste après le scellement de la contre-lecture 7 » à expliquer ; dernière ligne réelle en cas
  d'échec de `pip` : « fin : arret code 1 (commit verifie) » ; relevé non rejouable, empreinte non comparée à une autre source.
- **Q-9. Info.** En-tête de l'amorce v6 citant la commande v7 ; `journaux()` du suivi v4 plus appelée par `main` ; nom de fichier exclu
  avec une espace ambigu ; formule de `minuterie_s` non relue dans cette contre-lecture.

**Supposé** : formes réelles des sorties de l'outil, sérialisation de `--args`, clone HTTPS réel et chemin réel de la machine, survie
de la minuterie détachée, persistance de l'état du shell entre appels, comportement de `setsid` sous contrôle des tâches.

**Bloquant pour la location : oui**, tant que Q-1 et Q-2 ne sont pas corrigés ; Q-3 fortement conseillé avant la demande de feu.

**Note de la session de reprise** (après lecture, avant les suites) : Q-2 est vrai dans cet environnement (l'état du shell, variables
comprises, ne persiste pas entre appels d'outil) ; l'essai de survie (Q-3) a en outre montré que le shell a le contrôle des tâches :
`$!` y désigne un parent déjà mort de `setsid`, ce qui rend faux aussi le PID de la garde écrit en v8 (`essai-survie-processus-detaches-v1.txt`).
