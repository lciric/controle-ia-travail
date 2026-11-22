# Rapport de l'auteur : script de démarrage de l'essai 3 (palier 0b), v6

Pièce de travail (classe C), écrite le 2026-11-22 vers 01:25Z par l'auteur des versions précédentes (modèle O), sur l'ordre de 00:16Z. Elle part de la v5, qui reste intacte. Les chemins ci-dessous sont relatifs à `v6/`, sauf indication.

## Verdict

Les marges sont positives avec un jeton de 100 signes :

| Lecture | Taille | Marge |
|---|---|---|
| JSON échappé en ASCII | **32 653** | **115** |
| Échappement HTML de Go | 32 708 | **60** |
| Octets bruts | 32 597 | 171 |

Fichiers : `essais/travail/fabricant/ud-sain.empreintes.txt` et `essais/travail/fabricant/tailles-json-ud-sain.txt`, ce dernier calculé à part en Python. Il a fallu (a) puis (b).

Le banc complet est joué sur le script livré. Tous les cas sont tenus.

Pendant la session :
- aucune machine, aucun appel à Hetzner ni à GitHub, aucun jeton réel lu ;
- aucun environnement listé ni affiché, aucun `sleep` isolé, aucun heredoc ;
- seuls mes factices ont été arrêtés, par identifiant ou par le `cgroup.kill` de leurs groupes de banc ;
- aucun commit ni poussée ;
- aucun refus de permission, de classifieur ou de garde.

## Pièces livrées (compagnon `.sha256` à côté de chaque fichier)

| Pièce | sha256 |
|---|---|
| `demarrage-machine-essai-3-v6.sh` (texte complet, pour la lecture) | `f61aea46033d63dec6fde0cd66455f5474e000d140d9d98c5f23ab61976aeeb2` |
| texte réduit mis dans la charge, porté par `E_SCRIPT` (`essais/travail/fabricant/ud-sain.script-reduit.sh`) | `061f79930face6fc7945c30fb5dbb6275563495b0ea0fe132ba82f1457137ce5` |
| `amorce-demarrage-essai-3-v6.sh` (= v5, noms v6) | `524cfc4a78a2b77c3cb5ad0c915628217e932c7cd58dbfebc80c4643f5d9d751` |
| `fabriquer-donnees-demarrage-v6.sh` | `53252968a041390af0d81c3285b00af9bb9a17229d29279c570b578f96625b62` |
| `reduire-script-v6.py` (réducteur, appelé par le fabricant) | `b1a4d2162c18967a13d2b27c01a926c534b3bbeecee77523e1caa1892ac2f5fa` |

## 1. Taille

**(a) Réduction.** Le fabricant retire du script mis dans la charge les lignes de commentaire entières (premier signe non blanc `#`, sauf le `#!` de tête) et les lignes vides. Il ne touche à rien d'autre. Le texte complet reste dans `v6/` et dans l'empreinte « script complet » du relevé du fabricant. `E_SCRIPT` porte sur le texte réduit.

Sur le script livré : 362 lignes, 31 retirées (`essais/travail/fabricant/ud-sain.reduction.txt`).

**Le garde-fou garde les lignes intérieures** ; il ne refuse pas. Un lecteur d'état suit les guillemets `'…'`, `"…"` et `$'…'`, les substitutions `$( )`, `${ }` et `` `…` ``, les lignes continuées par `\` et les documents en ligne (`<<`, `<<-`). Il refuse en 9 seulement si l'état reste ouvert en fin de texte.

**L'épreuve est indépendante du réducteur.** Elle exige trois choses, sinon le fabricant refuse en 9 :
- `bash -n` passe sur les deux textes ;
- `diff` ne montre que des retraits de lignes de commentaire entières ou de lignes vides ;
- la ligne 1 n'est jamais retirée.

Résultats : **8 sur 8 tenus** (`essais/travail/reduction/table.txt`).

| Cas | Attendu | Rendu |
|---|---|---|
| G1, sain | 0 | 0 |
| G2, garde-fou : chaînes sur plusieurs lignes, document en ligne, substitution, ligne continuée | 0, lignes intérieures gardées | 0 ; **7 lignes intérieures gardées sur 7**, le vrai commentaire retiré |
| G3, garde-fou : guillemet jamais fermé | 9 | 9 |
| **A1, une vraie ligne de code retirée** (`set -u -o pipefail`) | 9 | **9** |
| A2, une ligne gardée modifiée | 9 | 9 |
| A3, ligne 1 retirée | 9 | 9 |
| T1, réducteur naïf sur G2 | 9 | 9 (`bash -n`) |
| T2, réducteur naïf sur une chaîne seule | 0, chaîne perdue | 0 ; la valeur de `MULTI` change |

T2 montre que, dans une chaîne seule, **c'est le réducteur qui protège, non l'épreuve**.

**(b) Messages abrégés.** (a) ne suffisait pas. Aucun code de sortie ni aucun nom de fichier versé n'a changé : 57 lignes de message changées (`diff essais/travail/script-v6-avant-abreviation.sh demarrage-machine-essai-3-v6.sh`).

Les passes, gardées dans `essais/travail/fabricant-passe-3-abreviation-2-go-negatif/` :

| Passe | JSON ASCII | Go | Fichier |
|---|---|---|---|
| (a) seule | 33 201 | — | `fabrication-ud-sain-passe-1-reduction-seule.txt` |
| (b), 1er lot | 32 821 | — | `…-passe-2-abreviation-1.txt` |
| (b), 2e lot | 32 733 (marge 35) | 32 788 (**marge −20**) | `fabrication-ud-sain.txt` |
| (b), 3e lot | 32 653 (marge 115) | 32 708 (marge 60) | chiffres livrés |

Pour information seulement, la lecture « / échappé en \/ » donne 33 199, soit une marge de −431 (`tailles-json-ud-sain.txt`, ligne e). L'encodeur JSON de Go n'échappe pas « / ».

## 2. Fond

**(i) Code 88, sans aucun repli.** Le repli et ses fichiers sont retirés. Au début du pas (f), avant toute vérification ou tout lancement, le départ est refusé en 88 si :
- aucun cgroup v2 n'est monté ;
- le parent du groupe n'est pas un cgroup v2 ;
- la création échoue, ou `cgroup.kill` manque ;
- un essai d'inscription échoue (un sous-shell s'inscrit puis sort).

Le départ réel refuse aussi en 88 si sa propre inscription échoue. Le code est écrit dans `echec-demarrage-essai-3.txt`, puis versé.

Au banc, trois cas rendent 88, sans programme lancé : sans cgroup, chemin hors cgroup, et groupe non inscriptible. Ce dernier est un groupe sous un cgroup « threaded », où le noyau refuse l'inscription : « Operation not supported ».

**(ii) Au code 86, le groupe est arrêté.** `echouer86` fait `cgroup.kill`, puis contrôle que le groupe est vide (10 s au plus) et écrit le résultat dans le message 86. Un étranger, hors du groupe, n'est jamais visé.

**(iii) Filet à l'heure d'arrêt + 60 s.** La boucle de versement fait `cgroup.kill`, contrôle le groupe vide, et l'écrit dans `filet-essai-3.txt` et dans l'état versé. Elle ne s'achève qu'après le filet, ou si le groupe est vide à la fin du gardien (« filet inutile »). Le gardien scellé est inchangé.

**Limite acceptée** : un programme root peut quitter son groupe. Le dernier garde-fou reste la destruction de la machine à H0 + 98 h.

## 3. Banc complet sur le script livré `f61aea46…`

| Essai | Résultat | Fichier |
|---|---|---|
| Lot entier (47 cas de la v4 et 8 cas v5–v6) | **55 sur 55 tenus** ; jeton dans aucun fichier, aucune histoire, aucun `ps`, sauf le témoin t1 (2 fichiers, 47 lignes) | `essais/travail/lot-v6.txt` |
| Course R2 visant la copie privée, 300 exécutions par version | **v6 : 0 lecture divergente** (299 conformes, 1 refus 18) ; **v4, objet vrai : 230 divergentes** (62 conformes, 8 refus 18) : la course a de la puissance | `essais/travail/course/course.txt` |
| Cas d'arrêt, fonctions réelles extraites | **13 sur 13 tenus** | `essais/travail/cas-arret.txt` (en tête : script `f61aea46…`) |
| Réduction et épreuve | 8 sur 8 | `essais/travail/reduction/table.txt` |
| q1-j | objet vrai v2 : 2 fuites ; v6 : 0 ; témoin : 0 | `essais/travail/q1-j/resume.txt` |
| Fabricant | **20 sur 20 tenus** | `essais/travail/fabricant-essais/table.txt` |
| Garde de branche (s1) | 7 refus, 1 admission, distant inchangé | `essais/travail/cas/s1-sain/journaux/garde-branche.txt` |
| Assistant (s1) | jeton à l'hôte permis seul | `essais/travail/cas/s1-sain/journaux/assistant.txt` |
| Arguments (s1) | ÉGAL, 8 lignes | `essais/travail/cas/s1-sain/journaux/controle-argv.txt` |
| Copie privée (s1) | dossier 700, fichier 600 | `essais/travail/cas/s1-sain/journaux/droits-copie-privee.txt` |

Sur le fabricant : la table v4 comptait déjà 20 lignes. Le « 21 » annoncé plus tôt était une erreur de compte.

**Cas d'arrêt rejoués.** n8 (descendant en session neuve, père mort) est joué trois fois :
- par `arreter` : tout est mort ;
- **au code 86** (n8b, identité écrite d'un étranger) : `cgroup.kill`, le programme et le descendant sont morts, le groupe est vide, les deux étrangers vivent ;
- **au filet** (n8c) : « filet … : cgroup.kill ; groupe vide ».

Une passe 1 a été faite sur le même script, avec un défaut du coureur de banc seul (`h()` manquant, d'où une date vide dans le fichier du filet). Elle est gardée : `essais/travail/cas-arret-passe-1-sans-h.txt`.

**Cas nouveaux du lot**, tous tenus, 0 processus restant :

| Cas | Attendu | Rendu |
|---|---|---|
| reprise après `E_SCRIPT` absent, ou vide | 18 puis 18 | 18 puis 18 ; charge absente après le premier refus |
| descendant en session neuve, gardien refusé | 84 | 84 |
| descendant en session neuve, non chef | 86 | 86 ; « cgroup.kill : groupe vide » |
| sans cgroup / chemin hors cgroup / groupe non inscriptible | 88 | 88 ×3 ; programme non lancé |
| **filet réel** | 0 | 0 |

Le filet réel, en détail (`essais/travail/cas/r1v6-filet-descendant-session-neuve/`) :
- le gardien arrête le programme à l'heure d'arrêt (01:16:54Z) ;
- le descendant en session neuve lui survit : l'état versé montre 1 membre ;
- à 01:17:55Z, le filet fait `cgroup.kill` ; le groupe est vide et c'est écrit dans l'état.

Dans p2, f1 et le cas « chemin hors cgroup », le compteur « restants » rend 1. C'est le joueur de cas lui-même, dont un argument porte le chemin du cas.

## Écarts

1. **(b) a été appliqué en trois lots.** Le 2e lot laissait la marge Go à −20 : je n'ai pas arrêté, parce que (b) n'était pas épuisé, et j'ai abrégé d'autres messages. Seuls des textes de journal ont changé.
2. **Les marges sont étroites** (115 et 60). Toute ligne de code ajoutée plus tard devra être remesurée.
3. **Le fabricant dépend désormais de `/home/user/controle-ia-travail/.venv/bin/python`**, pour le réducteur. Il a un nouveau code de refus, 9.
4. Au code 86 et au filet, le groupe entier est arrêté. Ses membres sont attestés par le noyau.
5. Le dépôt factice partagé a été pris de `v5/essais/travail/` (déplacé, non recopié), puis **retiré à la fin**, comme `distant-avec-branche.git`. Il ne sert plus : le banc est complet. Les dépôts de chaque cas restent, mais leurs objets partagés sont partis.

## Non joué

- Le vrai cloud-init, apt, pip, GitHub et l'image debian-13.
- Le cgroup v2 de debian-13 sous systemd, créé depuis cloud-final.service.
- L'intervalle réel de 1 800 s, et le filet à H0 + 94 h + 60 s en vraie durée : au banc, l'heure d'arrêt est réglée à +170 s.
- Les codes 60, 62, 70 et 83.

## Chemins lus hors du dossier v6

Pièces et dépôt :
- `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-lanceur-v4/lancer-essai-3-v4.sh`
- `…/lancement-essai-court-mesure-v1/auteur-lanceur-v4/demarrer-essai-3-v4.sh`
- `…/lancement-essai-court-mesure-v1/auteur-lanceur-v3-gardien-v4/gardien-essai-3-v4.py`
- `…/lancement-essai-court-mesure-v1/auteur-lanceur-v3-gardien-v4/demarrer-gardien-essai-3-v4.sh`
- `/home/user/controle-ia-travail` : `git show origin/main:docs/notes/organisme-noeuds-2026-11-21-v1/pieces-v2/complement-1-v3-controle-lancement-palier-0b-essai-3-v2.md`, copié dans `essais/travail/complement-1-v3-v2.md`
- `/home/user/controle-ia-travail/.venv/bin/python` (réducteur, serveur factice, tailles, arguments)

Fichiers de l'auteur hors v6, dans `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-script-demarrage-essai-3/` :
- `essais/travail/jeton-factice.txt` et `essais/travail/jeton-factice-autre.txt`
- `v2/fabriquer-donnees-demarrage-v2.sh` (objet vrai de q1-j)
- `v4/fabriquer-donnees-demarrage-v4.sh` et `v4/amorce-demarrage-essai-3-v4.sh` (objet vrai de la course)
- `v4/essais/outils/lot-v4.sh` et `v4/essais/travail/fabricant-essais/table.txt` (comparaison des comptes)
- `v5/` : les pièces et le banc, copiés au départ ; `v5/essais/travail/distant/` et `distant-avec-branche.git`, déplacés puis retirés

Système :
- `/usr/bin/git`, `tar`, `gzip`, `base64`, `setsid`, `diff`, `sed`, `/usr/lib/git-core/git-http-backend`
- `/proc`, `/proc/self/mounts`, `/sys/fs/cgroup/unified` (groupes de banc créés et retirés : aucun ne reste)
