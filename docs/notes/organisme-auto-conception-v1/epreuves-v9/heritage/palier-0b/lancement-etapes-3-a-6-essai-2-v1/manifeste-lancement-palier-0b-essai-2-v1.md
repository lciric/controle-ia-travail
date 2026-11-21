# Manifeste du lancement détaché de l'essai 2 du programme 1 du palier 0b — v1

Écrit par un agent neuf le 2026-11-21 (`date -u` : après 08:43:55Z). Geste fixé par la pièce scellée de la mère, complément 1 v2 :
`/home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/controle-lancement-palier-0b-par-la-mere-v1-complement-1-v2.md` (502cbded…, commit 9d2eb0b6), lue en entier avant tout geste.

## Les six vérifications, avant tout lancement

1. `git -C /home/user/palier-0b-racine rev-parse HEAD` → `9d2eb0b6730758142838a86fb0f2c91676a009b4`. Attendu : identique. OK.
2. `env -C …/heritage/palier-0b sha256sum -c controle-lancement-palier-0b-par-la-mere-v1-complement-1-v2.md.sha256` → `controle-lancement-palier-0b-par-la-mere-v1-complement-1-v2.md: OK`. OK.
3. `sha256sum …/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py` → `1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14`. Attendu : identique (et identique à la ligne « empreinte du programme » du complément 1 v2). OK.
4. `git -C /home/user/palier-0b-racine status --porcelain` → une seule ligne : `?? diag/heritage-palier-0b-v1/`. Écart déclaré et accepté, voir plus bas. Aucune autre ligne. OK. (La même commande, relancée après le lancement, rend la même ligne seule.)
5. `stat /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-2` → `stat: cannot statx '…/etapes-3-a-6-essai-2': No such file or directory` (code de sortie 1). OK : le dossier des sorties n'existait pas avant le lancement.
6. `df -B1 /home/user` → système de fichiers `/dev/vda`, taille 270553174016 octets, occupés 64447700992, **libres 9433911296 octets (environ 9,4 Go)**, 88 % d'occupation. Relevé.

Version de Python de l'outil (`python3 --version`) : Python 3.13.18. L'interpréteur lancé est `/home/user/controle-ia-travail/.venv/bin/python`, dont `/proc/16809/exe` pointe vers `/usr/local/bin/python3.13`.

## Écart déclaré de l'état de l'arbre

La ligne `?? diag/heritage-palier-0b-v1/` est le dossier de l'essai 1 (`…/diag/heritage-palier-0b-v1/etapes-3-a-6`, environ 1,9 Go), gardé intact exprès jusqu'à son inventaire et son versement scellé. Écart déclaré et **accepté par la mère à 08:41Z**. Rien n'y a été lu ni touché. Le dossier de l'essai 2 se crée sous ce même dossier non suivi : la ligne d'état reste la même.

## Le lanceur

Chemin : `/home/user/journaux-palier-0b-essai-2-v1/lancer-essai-2-detache-v1.sh` (dossier créé par `mkdir` juste avant).
Empreinte : `6f268f53e93fbeda0ec6f705c6f6e6c69d3ed1a5a0f005d7f76a3576315b5521`, compagnon `lancer-essai-2-detache-v1.sh.sha256` à côté, vérifié par `sha256sum -c` : OK.

Contenu, trois lignes :

```
#!/bin/bash
setsid nohup env -C /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md /home/user/palier-0b-racine /home/user/palier-0b-racine/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-2 > /home/user/journaux-palier-0b-essai-2-v1/journal-essai-2.txt 2>&1 < /dev/null &
echo $! > /home/user/journaux-palier-0b-essai-2-v1/identifiant-processus-essai-2.txt
```

### Comparaison avec la commande du complément 1 v2, faite par programme

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/lancement-palier-0b-essai-2/`.

1. `grep -F "env -C /home/user/palier-0b-racine" <complément 1 v2>` redirigé dans `commande-complement-1-v2.txt` : 1 ligne, 696 octets, empreinte `17f140204a28c35ee2612278c7eea762d8b77af40fb72a44af1a1344c2437c35`.
2. Le même `grep -F` sur le lanceur, redirigé dans `commande-lanceur.txt` : 1 ligne, 791 octets, empreinte `5b66d6fc3344b41cf97711e35e77738e8f940a42dc9ee6222d38858b3c4c337f`.
3. `grep -o -F -f commande-complement-1-v2.txt commande-lanceur.txt`, redirigé dans `commande-extraite-du-lanceur.txt` : la commande du complément est trouvée mot pour mot dans la ligne du lanceur. 1 ligne, 696 octets, empreinte `17f14020…` (la même que le point 1).
4. `cmp commande-complement-1-v2.txt commande-extraite-du-lanceur.txt` : aucune différence (silence, code 0).
5. Écart de longueur : 791 − 696 = 95 octets, soit exactement le préfixe `setsid nohup ` (13 octets) et le suffixe ` > /home/user/journaux-palier-0b-essai-2-v1/journal-essai-2.txt 2>&1 < /dev/null &` (82 octets). Rien d'autre ne s'ajoute.

## Lancement

- Commande : `bash /home/user/journaux-palier-0b-essai-2-v1/lancer-essai-2-detache-v1.sh`. Elle a rendu la main tout de suite, sans sortie.
- **Heure du lancement** : 2026-11-21T08:42:45Z (heure de modification du fichier d'identifiant, `stat -c %Y` → 1795250565). `date -u` relevé juste après : Sat Nov 21 08:42:47 UTC 2026.
- **Identifiant de processus** : **16809**, lu dans `/home/user/journaux-palier-0b-essai-2-v1/identifiant-processus-essai-2.txt`.
- **Journal** (sortie standard et sortie d'erreur) : `/home/user/journaux-palier-0b-essai-2-v1/journal-essai-2.txt`.
- Dossier des sorties : `/home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-2`. Le programme l'a créé : 8,0 Ko à 08:43:32Z, contenu non lu.
- Place libre avant le lancement : 9433911296 octets.

## Preuve qu'il vit

| Heure (UTC) | `stat -c %n /proc/16809` | Taille du journal (`stat -c %s`) |
|---|---|---|
| 08:42:47 (juste après le lancement) | `/proc/16809` | — |
| 08:43:03 | — | 0 |
| 08:43:36 | `/proc/16809` | — |
| 08:43:55 (plus d'une minute après le lancement) | `/proc/16809` | 0 |

Dossier courant du processus (`readlink /proc/16809/cwd`) : `/home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6`, comme la commande le fixe.

Le journal est vide à la deuxième lecture, donc il n'a pas été lu. Ce n'est pas un écart : l'essai 1 n'avait laissé aucune ligne de sortie pendant ses deux heures, ce qui laisse penser que le programme écrit surtout à la fin.

## Ce qui n'a pas été fait

Aucun commit, aucun appel à un fournisseur, aucune dépense, aucun arrêt de processus. L'agent n'attend pas la fin du programme : la suite (quatre empreintes des manifestes, lignes « fréquences gelées : » et « réglages gelés : », code de sortie, ou à un arrêt la cause et l'inventaire) se fait ailleurs.
