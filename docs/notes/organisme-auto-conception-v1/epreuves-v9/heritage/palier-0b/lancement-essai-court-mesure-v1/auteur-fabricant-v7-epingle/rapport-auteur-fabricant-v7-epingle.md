# Rapport de l'auteur : fabricant v7 épinglé, essai 3 (palier 0b)

Pièce de travail (classe C), écrite le 2026-11-22 vers 01:55Z par l'auteur des versions précédentes (modèle O), sur l'ordre de 01:45Z. Les chemins ci-dessous sont relatifs à `v7/`.

## Verdict

**Le fabricant v7 épinglé est tenu partout.**

| Essai | Résultat |
|---|---|
| Épreuve de l'épinglage | 6 sur 6 |
| Cas du fabricant | 20 sur 20 |
| q1-j | tenu |
| Marge, JSON échappé en ASCII | 32 653 octets, **marge 115**, inchangée |
| Marge, échappement HTML de Go | 32 708 octets, **marge 60**, inchangée |
| Octets bruts | 32 597 |

Le cas sain est identique, octet pour octet, aux données du fabricant v6.

Pendant la session :
- aucune machine, aucun appel à Hetzner ni à GitHub, aucun jeton réel lu ;
- aucun environnement ni aucune valeur de variable affichés ;
- aucun `sleep` isolé, aucun heredoc ;
- aucun processus arrêté ;
- aucun commit ni poussée ;
- aucun refus de permission, de classifieur ou de garde.

## Pièces

Chaque fichier a son compagnon `.sha256` à côté.

| Pièce | sha256 |
|---|---|
| `fabriquer-donnees-demarrage-v7.sh` | `68c7e0507c8748a12dfbd642f777c159efb7b89dbf94a6f269a574d4c9b4a43a` |
| `demarrage-machine-essai-3-v6.sh`, copie inchangée | `f61aea46033d63dec6fde0cd66455f5474e000d140d9d98c5f23ab61976aeeb2` |
| `amorce-demarrage-essai-3-v6.sh`, copie inchangée | `524cfc4a78a2b77c3cb5ad0c915628217e932c7cd58dbfebc80c4643f5d9d751` |
| `reduire-script-v6.py`, copie inchangée | `b1a4d2162c18967a13d2b27c01a926c534b3bbeecee77523e1caa1892ac2f5fa` |

Le fabricant lit le script, l'amorce et le réducteur dans son propre dossier, d'où les copies. Le diff avec le fabricant v6 compte 10 lignes :
- l'en-tête et la ligne d'emploi, soit 4 lignes ;
- 6 lignes ajoutées après la réduction et l'épreuve. Elles vérifient, avec les empreintes écrites en dur, d'abord le script complet (`f61aea46…`), puis le texte réduit (`061f7993…`). Sinon, c'est un refus 9, et le nettoyage déjà en place retire tout fichier partiel.

## Épreuve (`essais/travail/epinglage/table.txt`)

| Cas | Attendu | Rendu |
|---|---|---|
| E0, cas sain : v6 et v7 joués ensemble, même jeton factice, même H0 (01:47:43Z) | identique | 0 et 0 ; données, texte sans jeton, charge et texte réduit **identiques** (données `3224a9a0…`, texte réduit `061f7993…`) |
| E1, A2 du contre-lecteur (chaîne multiligne, réducteur naïf) | 9 | 9, script complet autre ; 0 fichier laissé |
| E2, K1 du contre-lecteur (`case` dans `$( )`, réducteur réel) | 9 | 9, script complet autre ; 0 fichier laissé |
| E3, T2 de l'auteur (chaîne seule, réducteur naïf) | 9 | 9, script complet autre ; 0 fichier laissé |
| E4, script complet modifié d'un octet, dans un commentaire | 9 | 9, script complet autre ; 0 fichier laissé |
| E5, script réel, réducteur qui garde un commentaire | 9 | 9, **texte réduit** autre ; 0 fichier laissé |

E4 et E5 se complètent :
- dans E4, l'octet changé est dans un commentaire : le texte réduit serait resté le même, et seule l'empreinte du script complet arrête le cas ;
- dans E5, le script complet est juste et l'épreuve est muette : seule l'empreinte du texte réduit arrête le cas.

Dans E1 à E4, c'est l'empreinte du script complet qui refuse, avant celle du texte réduit.

Les tailles du cas sain, relues à part par `tailles-json.py`, sont dans `essais/travail/epinglage/e0/tailles-json-v7.txt`.

## Fabricant et q1-j

**Fabricant** (`essais/travail/fabricant-essais/table.txt`) : 20 sur 20 tenus. Aucune sortie n'est laissée par les refus, et le jeton n'apparaît dans aucun `ps`.

Deux attendus changent, parce que leurs scripts sont modifiés et donc refusés par l'épinglage :
- F10, « trop grand » : 6 devient 9 ;
- F15, « non ASCII » : 0 devient 9.

**q1-j** (`essais/travail/q1-j/resume.txt`) :
- objet vrai v2 : 2 fuites ;
- v7 : 0 ;
- témoin : 0.

## Écarts

1. L'épinglage interdit tout autre script, y compris au banc (`FABRICANT_SCRIPT`). Toute version future du script exigera donc un nouveau fabricant.
2. Le défaut de l'épreuve et le trou K1 du réducteur restent dans le code, comme l'ordre le demande. Ils n'ont plus d'effet : seuls les deux textes relus passent.
3. Les dépôts factices (un vide et un portant la branche) ont été créés pour ce banc, puis retirés.

## Chemins lus hors de v7

Pièces :
- `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-lanceur-v4/lancer-essai-3-v4.sh`
- `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-lanceur-v4/demarrer-essai-3-v4.sh`
- `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-lanceur-v3-gardien-v4/gardien-essai-3-v4.py`
- `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-lanceur-v3-gardien-v4/demarrer-gardien-essai-3-v4.sh`

Contre-lecture :
- `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/contre-lecture-script-demarrage-v6-v1/contre-lecture-script-demarrage-v6-v1.md`, la liste de ce dossier, et ses `outils/cas-fabricant.sh` et `outils/cas-fabricant-2.sh`, dont A2 et K1 sont recopiés dans `essais/outils/queue-a2-chaine.txt` et `queue-k1-case.txt`

Python :
- `/home/user/controle-ia-travail/.venv/bin/python`, pour le réducteur et `tailles-json.py`

Dossier de l'auteur, `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-script-demarrage-essai-3/` :
- `essais/travail/jeton-factice.txt`
- `v2/fabriquer-donnees-demarrage-v2.sh`, objet vrai de q1-j
- `v6/fabriquer-donnees-demarrage-v6.sh` et `v6/demarrage-machine-essai-3-v6.sh`, `v6/amorce-demarrage-essai-3-v6.sh`, `v6/reduire-script-v6.py` : comparaison E0 et source des copies
- `v6/essais/outils/` : outils du banc copiés

Système :
- `/usr/bin/git`, `tar`, `gzip`, `base64`, `diff`, `sed`, `cmp`
