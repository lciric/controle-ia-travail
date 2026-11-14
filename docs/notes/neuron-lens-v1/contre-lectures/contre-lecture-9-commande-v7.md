# Contre-lecture 9, ciblée, de la commande v7 (amorce v5, suivi v3, dépôt réduit v9, essai à blanc v6) — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé au commit `47d9326a` de `prep/neuron-lens-v1` par la session de reprise ; rapport
lu après 14:40:29 UTC ; lecture seule (`sha256sum`, `diff`, `bash -n`, `git show`, lecture ; 59 essais du suivi v3 exécutés ; essais à
blanc non rejoués). Résumé fidèle de son rapport (toutes les remarques reprises, formulations raccourcies) ; suites dans l'en-tête de
la commande v8.

**Verdict de tête** : remarques N-1 à N-12 traitées, sauf N-1 à demi (un fichier exclu reste perdu à la destruction, ce que la commande
dit) ; aucune régression ni fuite du jeton dans ce qui a été joué ; manques : preuve R5 des gardes les plus neuves (branches d'échec non
jouées) et un risque de dépense (P-1).

**Empreintes** (vérifié) : les 17 du tableau de la v7 et la v7 elle-même (`b36146d0…`) égales aux compagnons ; amorce v5, dépôt réduit
v9 et suivi v3 identiques aux commits `11ed9ec3`, `4f7e2265`, `47d9326a` ; liste `da640eb0…` identique aux journaux v5 et v6 (73
fichiers), commit réduit et paquet variables comme dit ; résumé de la commande conforme au journal v6 ; compteur du cas « crochet » 1
au journal v5, 0 au journal v6, amorce identique entre les deux. `bash -n` sans erreur ; 59 essais sur 59.

**État des remarques de la contre-lecture 8** : N-1 partiellement (P-6) ; N-2 traitée, réserve P-5 ; N-3 traitée, réserves P-2, P-3 ;
N-4 partiellement (P-4) ; N-5 traitée (formes réelles de `logs`, `instance`, `create` non vues avant la location ; « essayées à l'étape
2 » ne vaut que pour `instances`) ; N-6, N-7, N-8 a, b, d, N-9, N-11, N-12, § 3 traitées ; N-8 c non vérifiable ici (aucune pièce
versée) ; N-8 e, f, N-10 info.

**Table de destruction** contre les dernières lignes possibles de l'amorce v5 (par lecture de `fin()`, confirmée au journal pour les cas
joués) : aucune dernière ligne possible n'est classée dans une ligne qui détruirait à tort ; écarts : annotations imprécises (P-8) ;
variables exigées absentes et échec du clone d'entrée (aucune ligne `AMORCE`) → « toute autre », prudent ; signal pendant la course
(« fin : arret code 143 (course en cours) ») → « toute autre », prudent ; code 15 seulement via « POUSSEE FINALE EN ECHEC ».

**Base 64 et `+`/`/`** (vérifié par raisonnement) : un caractère `+` ou `/` demande un groupe de 6 bits commençant par cinq 1 ; les
octets du jeu ont le bit fort à 0 ; seul `_` (0x5F) a cinq 1 consécutifs, aux bits 3 à 7, en position absolue 8j+3, impaire, alors que les
groupes commencent aux positions 6m, paires : impossible, quel que soit le préfixe ; conclusion juste, cohérente avec 7 formes au
journal ; réserve info : la raison n'est pas dans la commande ; la sécurité n'en dépend pas (les deux familles sont produites pour tout
secret). Docstring du suivi : « 8 à 13 octets » trop large — de 8 à 10 octets aucun fragment base 64 seul, de 11 à 13 un seul sur
certains alignements ; la forme en en-tête est toujours couverte (supposé, calcul à la main).

**Remarques nouvelles**
- **P-1. Moyenne (dépense).** L'outil du loueur est « dans un environnement à part » et `VASTAI_OUTIL` n'est lu que par le suivi ; la
  création, la minuterie `( sleep "$D"; vastai destroy … ) &`, la destruction finale et la garde (`garde_depense_v3.py` l.104, 119)
  appellent `vastai` nu : hors du `PATH`, la minuterie échoue sans bruit à l'échéance. Correction : `export PATH=<environnement>/bin:$PATH`,
  exiger `command -v vastai` et `vastai show user --raw >/dev/null` au code 0 ; dire comment la minuterie survit à la fin de l'appel du
  shell (`setsid nohup …`) ; `D=$(…)` et la minuterie dans la même commande ; tuer le sous-shell laisse le `sleep` orphelin (inoffensif).
- **P-2. Moyenne (R5).** Branche « tête distante ≠ tête locale » jamais jouée. Artefact proposé : `git` enveloppe qui falsifie
  `ls-remote`, ou distant dont la référence ne bouge pas ; attendre l'échec et aucun « pousse ».
- **P-3. Moyenne (R5).** Branches d'échec non jouées : `find` en échec, restauration `checkout` impossible, copie impossible, écriture de
  l'état impossible, `git add` impossible (index verrouillé), second contrôle des fichiers indexés (code mort aux essais) ; non listées
  parmi les « Non couverts ». Les jouer ou les déclarer.
- **P-4. Mineure.** Essai : `objets()` masque les erreurs (`2>/dev/null`) ; un dépôt illisible compterait 0 ; compter les objets lus par
  dépôt ; poussées du dépôt réduit et des clones masquées ; « ERREUR grep » n'échoue pas l'essai ; témoin d'objets seulement un message
  de commit : ajouter un blob et un objet en paquet.
- **P-5. Mineure.** `[]`, `{}`, `null` restent des absences ; `absente` sans témoin sur `[]` rend vrai alors que la commande dit « liste
  non vide » : l'imposer (option) ou le dire ; `[]` légitime s'il n'y a plus d'autre instance ; le témoin doit durer jusqu'à l'étape 13.
- **P-6. Mineure.** Fichier exclu irrécupérable sans ssh : « pas sans la mère » ne laisse que payer plus ou perdre ; le dire ; inscrire
  les noms dans l'état poussé (`exclus_fichiers=`).
- **P-7. Mineure.** `instance`, `instances`, `logs` rendent 0 même sur erreur : code 1 si le résultat porte `erreur`.
- **P-8. Mineure.** Table : ligne 1 « code 10 ou autre échec avant l'arbre (`git worktree`, `rev-parse`) », retirer `git worktree` de la
  ligne 3 ; ligne « échec du clone d'entrée (`fatal:`, aucune ligne AMORCE) → destruction », ou dire que le repli est voulu.
- **P-9. Mineure.** « Aucun fichier ni objet git de la machine » trop large (fichiers que le loueur peut écrire depuis l'environnement,
  supposé) : « fichiers de l'arbre de travail et résultats poussés » ; l.141 « historique » contredit « reste à la tête » ; `pip` 26.2.2
  sans pièce versée (R6/R7).
- **P-10. Mineure.** `locale=$(git rev-parse HEAD)` non contrôlé ; liste du second contrôle lue par substitution de processus, son échec
  silencieux.
- **P-11. Info.** Liste des essais rapides sans `…_course_v4.py` ni `…_extraction_v1.py` (héritage déclaré « liste de la v3 ») ; code 14
  « en moins d'une minute » mesuré sans délai réseau (19 s) ; en-tête avant `clone` non persisté (supposé).

**Verdicts** : commande v7 après corrections mineures (P-1 d'abord, puis P-8, P-9, P-5, P-6, P-3) ; amorce v5 après corrections mineures
(P-10) ; suivi v3 et essais après corrections mineures (P-5, P-7, docstring) ; dépôt réduit v9 **en l'état** ; essai à blanc v6 et
journaux après corrections mineures (P-2, P-3, P-4), journal v5 en l'état.

**Supposé** : formes réelles des sorties de l'outil, `pip` 26.2.2, minuterie survivant à la session, fichiers du loueur, signaux, clone
HTTPS réel, calcul des fragments courts.
