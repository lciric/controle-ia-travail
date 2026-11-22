# Rapport de l'auteur : fabricant v8, essai 3 (palier 0b)

Pièce de travail (classe C), écrite le 2026-11-22 vers 02:00Z par l'auteur des versions précédentes (modèle O), sur l'ordre de 01:54Z. Les chemins sont relatifs à `v8/`. La v7 reste intacte : son fabricant garde l'empreinte `68c7e050…`.

## Verdict

Le fabricant v8 est tenu partout. La marge est inchangée.

| Essai | Résultat |
|---|---|
| Épreuve v8 | 5 sur 5 |
| Fabricant | 20 sur 20 |
| q1-j | tenu |
| JSON échappé en ASCII | 32 653 octets, marge 115 |
| Échappement HTML de Go | 32 708 octets, marge 60 |

Pendant la session :
- aucune machine, aucun appel à Hetzner ni à GitHub, aucun jeton réel lu ;
- ni l'environnement ni la valeur d'aucune variable n'ont été affichés ;
- aucun `sleep` isolé, aucun heredoc ;
- aucun processus arrêté ;
- aucun commit ni poussée ;
- aucun refus de permission, de classifieur ou de garde.

## Pièces (compagnon `.sha256` à côté de chacune)

| Pièce | sha256 |
|---|---|
| `fabriquer-donnees-demarrage-v8.sh` | `a91f3403ba7b168ccf0bb126bc4731491a6024f6998c5d7e42292535e054fd2d` |
| `amorce-demarrage-essai-3-v6.sh` (copie inchangée) | `524cfc4a78a2b77c3cb5ad0c915628217e932c7cd58dbfebc80c4643f5d9d751` |
| `demarrage-machine-essai-3-v6.sh` (copie inchangée) | `f61aea46033d63dec6fde0cd66455f5474e000d140d9d98c5f23ab61976aeeb2` |
| `reduire-script-v6.py` (copie inchangée) | `b1a4d2162c18967a13d2b27c01a926c534b3bbeecee77523e1caa1892ac2f5fa` |

**Changements par rapport au v7.** Le diff ne touche que l'en-tête, la ligne d'emploi et 6 lignes ajoutées :
- L'amorce est épinglée sur `524cfc4a…`, empreinte écrite en dur. Le contrôle vient juste après son hachage, avant tout autre usage. Sinon : refus 9. Aucun fichier n'est encore écrit à ce stade.
- Après l'écriture du texte sans jeton, et avant toute donnée, le fabricant exige une seule ligne `E_SCRIPT=` : la ligne 4, égale à `E_SCRIPT=061f7993…`. Sinon : refus 9. Le nettoyage déjà en place retire les fichiers écrits.

## Épreuve (`essais/travail/v8/table.txt`, outil `essais/outils/essais-v8.sh`)

| Cas | Attendu | Rendu |
|---|---|---|
| E0, sain : v7 et v8 joués ensemble, même jeton factice, même H0 (01:56:01Z) | données identiques | codes 0 et 0. **Identiques octet pour octet** : données `5a67c913…`, texte sans jeton `404f57ae…`, charge `24b99467…`, texte réduit `061f7993…`. Une seule ligne `E_SCRIPT=`, la ligne 4 |
| B1, amorce modifiée d'un octet (dans un commentaire) | 9 | 9 (amorce `d78a080f…`) ; 0 fichier laissé |
| B2, amorce sans son contrôle d'empreinte (1 ligne retirée) | 9 | 9 (amorce `11a2dfe5…`) ; 0 fichier laissé |
| B3, amorce avec une seconde ligne `E_SCRIPT=0…0` (le cas B1 du vérificateur) | 9 | 9, par l'épinglage de l'amorce ; 0 fichier laissé |
| D1, seconde ligne `E_SCRIPT=` dans les données | 9 | 9 : « données : 2 ligne(s) E_SCRIPT= » ; 0 fichier laissé |

Les cas B et D jouent dans une copie du dossier du fabricant, où seule l'amorce change.

Pour B1 à B3, la copie du fabricant est contrôlée identique au v8.

Pour D1, une mutation a été nécessaire. L'épinglage de l'amorce arrête toute seconde ligne `E_SCRIPT=` avant qu'elle n'atteigne le second contrôle. J'ai donc changé, dans la copie, la seule ligne `E_AMORCE_EPINGLE`, en y mettant l'empreinte de l'amorce B3. Le diff le montre : 2 lignes, un retrait et un ajout.

## Marge

La marge est inchangée : 32 653 en JSON échappé en ASCII (marge 115) et 32 708 avec l'échappement HTML de Go (marge 60). Octets bruts : 32 597.

Sources : `essais/travail/v8/table.txt` (E0) et `essais/travail/v8/e0/tailles-json-v8.txt`, calculé à part.

## Fabricant et q1-j

**Fabricant** (`essais/travail/fabricant-essais/table.txt`) : **20 sur 20** tenus.
- F10 et F15 sont attendus en 9, comme en v7.
- Aucune sortie n'est laissée par les refus.
- 61 relevés de `ps`, dont 0 portant le jeton.

**q1-j** (`essais/travail/q1-j/resume.txt`) : objet vrai v2, 2 fuites ; v8, 0 ; témoin, 0.

Les dépôts factices de ce banc (un vide, un portant la branche) ont été créés puis retirés.

## Chemins lus hors de v8

- Les quatre pièces :
  - `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-lanceur-v4/lancer-essai-3-v4.sh`
  - `…/lancement-essai-court-mesure-v1/auteur-lanceur-v4/demarrer-essai-3-v4.sh`
  - `…/lancement-essai-court-mesure-v1/auteur-lanceur-v3-gardien-v4/gardien-essai-3-v4.py`
  - `…/lancement-essai-court-mesure-v1/auteur-lanceur-v3-gardien-v4/demarrer-gardien-essai-3-v4.sh`
- La vérification : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/verification-fabricant-v7-v1/verification-fabricant-v7-v1.md`, ainsi que la liste de ce dossier.
- `/home/user/controle-ia-travail/.venv/bin/python`.
- Dans `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-script-demarrage-essai-3/` :
  - `essais/travail/jeton-factice.txt` ;
  - `v2/fabriquer-donnees-demarrage-v2.sh`, objet vrai de q1-j ;
  - `v7/` : le fabricant v7 et son script, son amorce et son réducteur (comparaison E0, source des copies) ;
  - `v7/essais/outils/` : outils du banc, copiés.
- `/dev/urandom`, lu par l'essai F10.

## Outils du système employés

Par le fabricant v8, le banc (`essais/outils/`) et mes appels :
- **Shell et environnement** : `bash` (commandes internes `read`, `printf`, `echo`, `wait`, `umask`, `set`, `cd`), `env`.
- **Fichiers et dossiers** : `mkdir`, `rm`, `ls`, `cp`, `chmod`, `stat`, `find`, `xargs`.
- **Texte** : `cat`, `sed`, `grep`, `cut`, `tr`, `wc`, `head`, `tail`.
- **Empreintes et comparaison** : `sha256sum`, `cmp`, `diff`.
- **Chemins et dates** : `dirname`, `basename`, `date`.
- **Archive et encodage** : `tar`, `gzip`, `base64`.
- **Git** : `/usr/bin/git`, par l'espion `essais/outils/espion/git` dans q1-j, pour `init`, `ls-remote`, `hash-object`, `mktree`, `commit-tree`, `update-ref` et `for-each-ref`.
- **Processus** : `ps` et `sleep`, dans la boucle de guet `guetteur-ps.sh`.
- **Python** : `/home/user/controle-ia-travail/.venv/bin/python`, avec `-I`, pour `reduire-script-v6.py` et `tailles-json.py`.
