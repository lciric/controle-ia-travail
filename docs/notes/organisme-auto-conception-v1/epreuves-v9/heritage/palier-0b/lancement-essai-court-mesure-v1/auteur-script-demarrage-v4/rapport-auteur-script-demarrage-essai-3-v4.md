# Rapport de l'auteur — script de démarrage de l'essai 3 (palier 0b) — v4

Pièce de travail (classe C), écrite le 2026-11-21 vers 23:55Z par l'auteur des versions précédentes (modèle O). Elle porte les quatre corrections R1 à R4 accordées par la mère à 22:53Z, et rien d'autre. Elles viennent de la contre-lecture S de la v3 (`…/contre-lecture-script-demarrage-v3-v1/contre-lecture-script-demarrage-v3-v1.md`, `baf3742e…d507`, « Conforme avec réserves »). La v3 reste intacte.

Règles tenues pendant la session :
- aucune machine créée, aucun appel à Hetzner ni à GitHub, aucun jeton réel lu ;
- aucun environnement affiché ni listé ;
- aucun `sleep` isolé ni aucun heredoc dans mes appels ;
- seuls mes factices ont été arrêtés, par identifiant ;
- aucun commit, aucune poussée ;
- aucun refus de permission, de classifieur ou de garde.

Le dépôt factice partagé a été refait pour la v4 (2,1 Go), puis retiré à la fin, comme les racines et les clones de chaque cas.

## Fichiers et empreintes (`v4/`, compagnon `.sha256` à côté de chacun)

| Pièce | sha256 |
|---|---|
| `demarrage-machine-essai-3-v4.sh` | `d20e90e169de4fb2f623fdde910b449bedca0fb3d5d2012535cdc1eea03442a4` |
| `amorce-demarrage-essai-3-v4.sh` | `392368340ddf202da1466d03cdee1fd2334fe09562f173b8f174d0452e7fc877` |
| `fabriquer-donnees-demarrage-v4.sh` (= v3, aux noms v4 près) | `12a4996596b0bbb18564658d4e8036f8b2b0eb7c7708e23e20922a62b1b83211` |

Banc : `v4/essais/outils/`. Les outils nouveaux sont :
- `cas-arret-v4.sh` et `prog-arret.sh`, repris du `cas-arret.sh` et du `prog.sh` du relecteur ;
- `course-amorce.sh`, repris de son `p1-course.sh` ;
- `fabriquer-depot-avec-branche.sh` ;
- le lot `lot-v4.sh`.

Résultats : `v4/essais/travail/`.

## Corrections

**R1, descendants orphelins.**
- Le départ v4 est désormais lancé dans une session neuve (`setsid -w`). Le lanceur y prend, en plus, sa propre session par le `setsid` du départ v4 : le programme est chef de sa session et de son groupe.
- `arreter` vise le programme et ses descendants, par la chaîne des parents. Il vise aussi tous les membres de la session du programme, sauf si c'est la session du script, et tous ceux de son groupe. Il envoie le signal de fin, puis force l'arrêt au bout de 30 s.
- Si le programme est déjà mort, `arreter` vise ce qui reste de sa session et de son groupe. Le noyau ne réattribue pas un identifiant de session ou de groupe tant qu'un membre vit.
- Le gardien v4, qui n'a pas changé, couvre la session, car elle se confond avec le groupe qu'il signale.

**R2, fenêtre de l'amorce.** Le script est copié une seule fois dans un fichier privé (dossier 700 de `mktemp`, fichier 600, sous umask 077). L'amorce hache cette copie, puis lit cette même copie.

**R3, identifiant réutilisé.**
- Une fonction `moi` compare l'heure de départ lue dans `/proc` à celle qu'a écrite le départ v4.
- Au code 5, le départ v4 a écrit « inconnu » ; la seule heure qu'il a écrite est alors `heure-lancement-essai-3.txt`. Le contrôle exige que l'heure de départ du processus tombe dans [lancement − 5 s, lancement + 2 s], l'horloge de démarrage de `/proc/stat` étant à la seconde.
- En cas d'écart : code 86, sans aucun arrêt (`identite5`).
- `arreter` fait la même comparaison avant tout arrêt. Avant l'arrêt forcé, il revérifie l'heure de départ de chaque cible, descendants compris, relevée lors de l'instantané.
- `arreter` refuse un identifiant écrit qui ne serait pas un nombre supérieur à 1.

**R4.** `E_SCRIPT` absent ou vide rend 18.

Défaut trouvé par le banc et corrigé : `moi` et l'attente appelaient `st` avec un identifiant vide non cité, ce qui faisait sortir le script sous `set -u`. Ils citent désormais l'identifiant (`"${1:-}"`, `"$P"`). Voir la passe 1, ci-dessous.

## Table des cas

| Lot | Résultat | Fichier |
|---|---|---|
| Lot complet : les 40 cas de la v3, le cas sain s1, 6 cas nouveaux | **47 sur 47 tenus** ; jeton factice dans aucun fichier, aucune histoire, aucun `ps`, sauf le témoin (2 fichiers, 45 lignes) | `travail/lot-v4.txt` |
| s1, arguments | ÉGAL au complément, 8 lignes | `cas/s1-sain/journaux/controle-argv.txt` |
| s1, garde de branche | 7 refus, 1 admission | `cas/s1-sain/journaux/garde-branche.txt` |
| s1, assistant | jeton à l'hôte permis seul, rien aux 6 autres demandes | `cas/s1-sain/journaux/assistant.txt` |
| Copie privée de s1 | dossier 700, fichier 600 | `cas/s1-sain/journaux/droits-copie-privee.txt` |
| Fabricant | 21 sur 21 | `travail/fabricant-essais/table.txt` |
| q1-j (`J` exporté) | objet vrai v2 : 2 fuites sur 2 ; v4 : 0 sur 2 ; témoin : 0 | `travail/q1-j/resume.txt` |
| **R1, R3 sur faux processus** (fonctions réelles extraites entre leurs repères) | **8 sur 8** (détail ci-dessous) | `travail/cas-arret.txt` |
| **R2, course** (remplacement atomique en boucle, 300 exécutions par version) | **v4 : 0 lecture divergente** (282 conformes, 18 refus 18) ; **v3, objet vrai : 1 divergente** (299 conformes) | `travail/course/course.txt` |

Détail des 8 cas de `cas-arret.txt` :

| Cas | Attendu | Rendu |
|---|---|---|
| n1 non chef, arbre | 86, tout le reste arrêté | 86 ; 5 identifiants arrêtés ; l'étranger sans lien vit |
| n2 chef | confirmé, rien tué | confirmé, rien tué |
| n3 programme mort | 86 sans arrêt | 86, rien tué |
| **n4 non chef, petit-fils orphelin** | 86, tout mort | **86 ; tout mort, orphelin compris** |
| n4b chef, orphelin (`arreter`) | tout mort | tout mort |
| **n5 identifiant repris par un étranger chef** | 86, ni adopté ni tué | **86 ; ni adopté ni tué** |
| **n6 identifiant repris par un étranger non chef** | 86, ni adopté ni tué | **86 ; ni adopté ni tué** |
| n7 heure de départ écrite autre (`arreter`) | rien tué | rien tué |

Cas nouveaux du lot (`lot-v4.txt`). Pour les trois cas d'orphelin, le faux programme a bien lancé le petit-fils : « petit-fils orphelin lancé », 1 fois chacun dans `journaux/programme.txt`.

| Cas | Correction | Attendu | Rendu |
|---|---|---|---|
| r4, `E_SCRIPT` absent | R4 | 18 | 18 |
| r4, `E_SCRIPT` vide | R4 | 18 | 18 |
| r4, charge sans script et `E_SCRIPT` vide | R4 | 18 | 18 |
| r1-n4 réel (code 5, non chef, orphelin) | R1 | 86, aucun processus restant | 86 ; 6 arrêtés, aucun forcé ; 0 restant |
| r1, orphelin, gardien refusé | R1 | 84, aucun processus restant | 84 ; 5 arrêtés ; 0 restant |
| r1, orphelin, arrêt de durée du gardien (code 5 confirmé) | R1 | 0, aucun processus restant | 0 ; signal au groupe ; tous les membres absents en 0,2 s ; 0 restant (`cas/r1-petit-fils-orphelin-arret-du-gardien/base/tenue/arret-gardien.txt`) |

Dans p2 et f1, le compteur « restants » rend 1 : c'est le joueur de cas lui-même, dont un argument porte le chemin du cas. Ce n'est pas un processus du script ; c'était déjà le cas en v3.

**Dénominateur.** Il y a eu une première passe de `cas-arret` : 2 cas en échec. Le faux programme n'était pas exécutable, et cette passe a révélé le défaut de `set -u` corrigé ci-dessus. Elle est gardée : `travail/cas-arret-passe-1-prog-non-executable.txt`. La seconde passe a été faite sur le script final (`d20e90e1…`, en tête de `cas-arret.txt`).

## Marge (jeton de 100 signes)

Fichiers : `travail/fabricant/ud-sain.empreintes.txt` et `travail/fabricant/tailles-json-ud-sain.txt`.

| Lecture | Taille | Marge |
|---|---|---|
| JSON échappé en ASCII | **31 948** | **820** |
| Échappement HTML de Go | 32 003 | **765** |
| Octets bruts | 31 904 | 864 |

Les deux marges demandées restent positives. Le fabricant (bash) et `tailles-json.py` (Python) donnent les mêmes nombres. La marge baisse de 2 325 en v3 à 820 en v4, parce que le script a grossi : session, identité, arrêt.

## Écarts

1. **L'heure de référence au code 5** est l'heure de lancement écrite par le départ v4, avec une tolérance de −5 s à +2 s, faute d'heure de départ écrite dans ce cas.
2. **Le départ est enveloppé par `setsid -w`.** Le mode « enfant » du faux `setsid` ne vise plus que le lanceur.
3. **La copie privée** est nommée `$CHARGE.script.XXXXXX/s.sh` (à côté de la charge), et non dans la charge : le pas (e) compte toujours cinq entrées dans la charge.
4. **Hors des quatre corrections**, deux protections : l'identifiant écrit doit être un nombre supérieur à 1, et l'identifiant est cité sous `set -u`.

## Ce qui reste non joué

- Le vrai cloud-init, le vrai apt, pip et GitHub, et l'image debian-13 (présence de gzip et de `setsid -w`) : supposés.
- Les codes 60, 62, 70 et 83, et l'intervalle de 1 800 s.
- Une réutilisation **réelle** d'un identifiant dans la fenêtre de 30 s de l'arrêt forcé : la revérification de l'heure de départ est écrite, mais elle n'est éprouvée que par n7 (heure écrite autre), non par une vraie reprise d'identifiant.
- Un programme mort au code 5 alors qu'il n'était pas chef de sa session : sa session ne se retrouve plus, et ses restes ne seraient pas visés.
- La reprise après un refus 18 rend 20, parce que le dossier à demi extrait reste (trouvaille du relecteur, m11, non corrigée : hors des quatre corrections).
