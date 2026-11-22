# Rapport de l'auteur : script de démarrage de l'essai 3 (palier 0b), v5, ARRÊTÉ sur la marge

Pièce de travail (classe C), écrite le 2026-11-22 vers 00:15Z par l'auteur des versions précédentes (modèle O). Elle porte les quatre corrections R2, R1, R3 et R4 bis de l'ordre de 23:57Z.

## Verdict : arrêté, la marge est négative

Avec un jeton de 100 signes, le fabricant v5 refuse en 6 : les données font **33 602 octets** en JSON échappé en ASCII, pour une limite de 32 768. La **marge est donc de −834 octets** (fichier `essais/travail/fabricant/fabrication-ud-sain.txt`). L'échappement HTML de Go ne peut que l'aggraver.

Comme l'ordre le prescrit, je m'arrête et je rends compte, sans rien retirer de moi-même. Le refus n'a laissé aucun fichier partiel : le dossier `essais/travail/fabricant/` ne contient que le relevé.

Sans données saines, rien de ce qui en dépend n'a été joué : le lot, la course, q1-j, les 21 cas du fabricant, la garde de branche, l'assistant et le contrôle des arguments.

Pendant la session :
- aucune machine, aucun appel à Hetzner ni à GitHub, aucun jeton réel lu ;
- aucun environnement affiché ni listé, aucun `sleep` isolé, aucun heredoc ;
- seuls mes factices ont été arrêtés, par identifiant ;
- aucun commit ni poussée ;
- aucun refus de permission, de classifieur ou de garde.

## Cause de la hausse (mesurée)

| Pièce | v4 | v5 |
|---|---|---|
| script, octets bruts | 14 522 | 18 366 |
| script, `gzip -9 -n` | 5 912 | 7 034 |
| amorce, octets bruts | 1 195 | 1 445 |

Le script compressé gagne 1 122 octets, soit environ 1 500 en base64. L'amorce en gagne 250. Le total passe de 31 948 à 33 602, soit +1 654. La hausse vient du groupe de contrôle (création, repli écrit, inscription, arrêt par le groupe), de la référence prise par le script et des commentaires.

Pistes, **non appliquées**, à trancher par la mère :
1. Retirer les commentaires du script de la charge : ils pèsent lourd, même compressés.
2. Abréger les messages du journal.
3. Faire passer l'amorce elle-même par gzip.

## Fichiers et empreintes (`v5/`, compagnon `.sha256` à côté de chacun)

| Pièce | sha256 |
|---|---|
| `demarrage-machine-essai-3-v5.sh` | `86318fec290dbf9de9f4dfdd458b275a6f752d992904ed77a65b27deab5dcce5` |
| `amorce-demarrage-essai-3-v5.sh` | `1900b9f3d988d0108966cb489decc2817180cca8df65f17ca3c8b600af768004` |
| `fabriquer-donnees-demarrage-v5.sh` (= v4, aux noms v5 près) | `e39a3aa7e5623a5f7f112d2ac6af9549655f46e5058550aa02859cc5540847a2` |

Banc : `v5/essais/outils/`. Il est adapté mais n'a pas été joué, sauf `sonde-cgroupe.sh` et `cas-arret-v5.sh`. Les adaptations :
- `jouer-cas.sh` donne un groupe de contrôle à chaque cas, accepte `DEUX_FOIS=1` pour une reprise, et nettoie par identifiant ;
- `lot-v5.sh` ajoute 9 cas ;
- `faux-programme.sh` ajoute `FAUX_EVADE` ;
- `prog-arret.sh` ajoute le mode `evade`.

## Corrections

**R2.** L'amorce lit la copie privée une seule fois en mémoire (`IFS= read -r -d '' TEXTE`, commande interne). Elle hache ces octets (`printf '%s' "$TEXTE" | sha256sum`), puis exécute ces mêmes octets (`eval "$TEXTE"`). Aucun fichier n'est rouvert après le hachage.

Le script ne dépend plus de `BASH_SOURCE`. La boucle de versement est lancée par `bash -c "$TEXTE"`. Ce texte ne porte aucun jeton, mais il paraît dans la ligne de commande de la boucle.

**La course sur la copie privée n'a pas été jouée** : le refus de taille est arrivé avant.

**R4 bis.** `E_SCRIPT` est contrôlé en tête, avant l'existence de la charge et avant toute extraction. Les cas de reprise (`r4bis-…-puis-reprise`, attendus 18 puis 18) sont écrits dans le lot, mais non joués.

**R1.** Le départ joue dans un sous-shell qui s'inscrit d'abord dans `cgroup.procs` d'un groupe propre au programme (`<cgroup2>/essai-3-programme`, premier cgroup2 de `/proc/self/mounts`), puis fait `exec setsid -w` du départ. Le programme et tous ses descendants naissent donc dans ce groupe.

`arreter` vise, en plus de l'arbre, de la session et du groupe :
- tous les membres du groupe de contrôle, y compris ceux qui naissent pendant l'attente ;
- il envoie le signal de fin, attend 30 s, puis fait un arrêt forcé par identifiant et `cgroup.kill`.

En repli, il n'y a pas de cgroup2, ou bien la création ou l'inscription est refusée :
- le repli est écrit dans `repli-groupe-de-controle-essai-3.txt`, dans le journal (« REPLI : … ») et dans l'état versé (« groupe de contrôle du programme : aucun ; repli : … ») ;
- l'arrêt se fait par l'arbre, la session et le groupe, comme en v4.

Sur le banc, le cgroup v2 est disponible et inscriptible à `/sys/fs/cgroup/unified` (fichier `essais/travail/sonde-cgroupe.txt`). Le descendant en session neuve dont le père est mort y est membre, et `cgroup.kill` l'arrête.

**R3.** La fonction `reference` lit elle-même `/proc/P/stat`, juste après le départ, sans tolérance. Elle accepte la lecture dans deux cas seulement :
- P est membre du groupe de contrôle, lu avant et après, avec la même heure ;
- en repli, le départ a rendu 0.

Au code 0, l'heure écrite par le départ doit être égale, au top près. La référence est écrite dans `depart-lu-par-le-script-essai-3.txt`. La fenêtre −5 s / +2 s et la lecture de l'heure de lancement sont retirées.

Sans référence : code 86, rien n'est arrêté. `moi` compare à la référence. `arreter` refait la comparaison avant tout arrêt forcé ; si P vit sans être le programme, aucun arrêt n'a lieu, même avec le groupe. Les lectures de `/proc` passent par `read`, sans fourche.

## Table des cas joués

| Essai | Résultat | Fichier |
|---|---|---|
| Sonde du cgroup v2 du banc | création, inscription, descendant en session neuve membre, `cgroup.kill` (zombie aussitôt), groupe retiré | `essais/travail/sonde-cgroupe.txt` |
| Cas d'arrêt, fonctions réelles extraites, 11 cas × (avec groupe, en repli) | **22 sur 22 tenus**, passe 1 | `essais/travail/cas-arret-passe-1-identifiants-en-double.txt` |

Ce qu'il faut savoir de cette passe :
- **Elle porte sur le script `53ebcf5e…`, et non sur le script livré `86318fec…`.** Elle a montré des identifiants en double dans la liste d'arrêt : sans effet, sinon un double signal. J'ai corrigé ce défaut par une seule ligne, l'ajout des membres du groupe sans doublon. La passe n'a pas été rejouée sur le script final, à cause de l'arrêt.
- Les cas nouveaux :
  - **n8** (descendant en session neuve, père mort) : tout est mort avec le groupe ; en repli, le descendant reste VIVANT, comme attendu (c'est la limite du repli) ;
  - **n9** (heure du départ autre d'un top) : 86, rien n'est tué ;
  - **n2 et n4, en repli au code 5** : 86, rien n'est tué. C'est la conséquence voulue de « aucune tolérance ».

## Écarts

1. **En repli, tout code 5 donne 86 sans rien arrêter, même si l'identité était vraie** : le cas « tardif », qui rendait 0 en v4, rendrait 86. Le programme continue alors sans gardien.
2. **Avec le groupe, un 86 laisse aussi le programme vivre**, alors que ses membres sont attestés par le noyau. J'ai appliqué l'ordre à la lettre (« sans rien arrêter »). Est-ce qu'on arrête le groupe au 86 ? À trancher.
3. **Le gardien v4, inchangé, arrête par groupe.** Un descendant en session neuve échappe à l'arrêt de durée du gardien ; seul `arreter`, dans le script, l'atteint. Le cas `r1v5-…-arret-du-gardien` du lot le montrerait (attendu : 1 restant). Il n'a pas été joué.
4. Sur la machine, le programme tourne en root et pourrait quitter son groupe ; cette menace n'est pas couverte.

## Non joué

- Tout le lot v5 (47 cas de la v4 et 9 nouveaux), la course R2 (v5 et l'objet vrai v4), q1-j, le fabricant (21 cas), la garde, l'assistant et les arguments. Tout est bloqué par la marge.
- La passe des cas d'arrêt sur le script final.
- Le cgroup v2 sur debian-13 sous systemd : un groupe à la racine `/sys/fs/cgroup`, pris depuis le groupe de cloud-final.service. Il est supposé, non éprouvé.

## Chemins hors du dossier v5 lus par le fabricant v5 et le banc

Pièces et dépôt :
- `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-lanceur-v4/lancer-essai-3-v4.sh` et `…/auteur-lanceur-v4/demarrer-essai-3-v4.sh` ;
- `…/lancement-essai-court-mesure-v1/auteur-lanceur-v3-gardien-v4/gardien-essai-3-v4.py` et `…/demarrer-gardien-essai-3-v4.sh` ;
- `/home/user/controle-ia-travail` : `fetch file://` du commit `d7f949ac` pour le distant factice, et `git show origin/main:` du complément 1 v3 pour le contrôle des arguments ;
- `/home/user/controle-ia-travail/.venv/bin/python`.

Fichiers de l'auteur, hors v5 :
- `…/scratchpad/auteur-script-demarrage-essai-3/essais/travail/jeton-factice.txt` et `jeton-factice-autre.txt` ;
- `…/scratchpad/auteur-script-demarrage-essai-3/v2/fabriquer-donnees-demarrage-v2.sh` (objet vrai de q1-j) ;
- `…/scratchpad/auteur-script-demarrage-essai-3/v4/amorce-demarrage-essai-3-v4.sh`, `…/v4/demarrage-machine-essai-3-v4.sh` et `…/v4/fabriquer-donnees-demarrage-v4.sh` (objet vrai de la course, à adapter).

Système :
- `/usr/bin/git`, `/usr/bin/tar`, `/usr/bin/gzip`, `/usr/bin/base64`, `/usr/bin/setsid`, `/usr/lib/git-core/git-http-backend` ;
- `/proc`, `/proc/self/mounts`, `/sys/fs/cgroup/unified`.

Le distant factice v5 (`essais/travail/distant/`, 2,1 Go) et `distant-avec-branche.git` sont gardés pour la reprise.
