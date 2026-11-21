# Récupération de la sortie partielle de l'essai 1 du programme 1 du palier 0b, étapes 3 à 6 — rapport v1

Classe C (travail). Agent neuf, 2026-11-21, de 08:39Z à 08:50Z environ. Demandé par la session mère à 08:38Z, précisé à 08:40Z (archive en tar non compressé à `/home/user/recuperation/`, comptes par dossier).

Dossier source, intact : `/home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6`. Aucun fichier n'y a été supprimé, déplacé ni modifié. Aucun contenu n'a été lu, sauf pour calculer les empreintes et pour l'archivage par `tar`.

## Ce qui a été fait

1. **Programme d'inventaire** `inventorier_dossier_v1.py` : bibliothèque standard seule, lecture seule. Il ne suit pas les liens et ouvre les fichiers avec `O_NOFOLLOW`. Le premier mode écrit une ligne par fichier, `chemin<TAB>taille<TAB>sha256`, triée par chemin en octets UTF-8. Les liens, les fichiers spéciaux et les erreurs vont sur des lignes à part, préfixées `#LIEN`, `#SPECIAL` et `#ERREUR`. Le mode écrit aussi un second TSV de comptes par dossier : fichiers directs et taille directe, fichiers récursifs et taille récursive, racine notée « . ». Les deux TSV sont compressés en gzip déterministe (`mtime=0`, sans nom de fichier, niveau 9). Le mode écrit enfin un résumé JSON trié. Pour chaque fichier, il compare taille et date de modification avant et après la lecture. Le second mode, `--verifier-tailles`, refait un parcours par `lstat` seul et compare les comptes et la taille totale au résumé.
   Le programme a d'abord été essayé sur un petit dossier d'essai, `scratchpad/essai-inventaire/` : un fichier, un lien, un dossier vide. Les résultats étaient conformes.
2. **Inventaire** joué une fois, de 08:42:07Z à 08:42:48Z :
   `python3 -I -B inventorier_dossier_v1.py DOSSIER inventaire-etapes-3-a-6-essai-1-v1.tsv.gz resume-inventaire-etapes-3-a-6-essai-1-v1.json comptes-par-dossier-etapes-3-a-6-essai-1-v1.tsv.gz`
   Sortie : `fichiers=687425 dossiers=232528 taille=1958715729 liens=0 speciaux=0 erreurs=0 modifies_pendant_lecture=0`.
3. **Stabilité du dossier**, sans recalcul des empreintes :
   - `du -sb` avant l'inventaire, juste après, puis après le tar : 1 958 715 729 octets à chaque fois. C'est la même valeur que la somme des fichiers : ce système de fichiers compte les dossiers pour 0 octet.
   - `--verifier-tailles` après l'inventaire, puis de nouveau après le tar : `IDENTIQUE`. On trouve 687 425 fichiers, 232 528 dossiers et 1 958 715 729 octets. La date de modification la plus récente est 2026-11-21T08:35:04Z, avant la coupure de 08:35:09Z : plus rien n'écrivait dans le dossier.
   - Aucun fichier n'a été modifié pendant sa lecture.
4. **Découpe** : non nécessaire. Le TSV compressé fait 27 706 102 octets, moins de 90 Mo.
5. **Place** avant l'archive : `df -B1 /home/user` donnait 9 402 290 176 octets libres. En pire cas, avec en-têtes, remplissage et noms longs, le tar ferait environ 3,73 Go.
6. **Archive** (consigne de la mère de 08:40Z, tar non compressé) :
   `mkdir /home/user/recuperation`
   `tar --create --file=/home/user/recuperation/palier-0b-programme-1-essai-1-v1.tar --sort=name --owner=0 --group=0 --numeric-owner --mtime='2026-11-21 00:00:00Z' --format=gnu -C /home/user/palier-0b-racine/diag/heritage-palier-0b-v1 etapes-3-a-6`
   GNU tar 1.35. `--format=gnu` est déjà le défaut de cette version ; il a été écrit pour figer le format. Les droits des fichiers sont gardés tels quels.
   Taille du tar : 3 583 508 480 octets. Le compagnon `palier-0b-programme-1-essai-1-v1.tar.sha256` est posé à côté.
   Place libre après le tar : 5 811 920 896 octets, au-dessus du plancher de 4 Go.
7. **Lecture de l'archive** : `tar -tf ARCHIVE --index-file=liste-tar-non-versee.txt` s'est terminé sans erreur. La liste est restée dans le dossier de travail et n'est pas versée. `wc -l` donne 919 954 entrées. `grep -c /$` donne 232 529 dossiers : les 232 528 sous-dossiers plus la racine. Il reste **687 425 fichiers, égal à l'inventaire**.

## Empreintes (sha256)

| Pièce | Taille (octets) | sha256 |
|---|---|---|
| `inventorier_dossier_v1.py` | — | `400cf87b684fa8b1622bf1776fe31e4e48aeea63a43f4ac9647df6b61f66724d` |
| `inventaire-etapes-3-a-6-essai-1-v1.tsv.gz` | 27 706 102 | `ff6c26d8fe0c8c7a59c370a7a2fe9e56f8a182f5ff0a7d69082dd103fbcccf95` |
| idem, TSV non compressé | 150 525 125 | `f09b4eb967484965f1d07d66e7eaea567fad2df1106ad9b212177c51e4559f19` |
| `comptes-par-dossier-etapes-3-a-6-essai-1-v1.tsv.gz` (232 529 dossiers + en-tête) | 1 575 615 | `d7187d4e6a4efe02f8a843acf51870cc5b9e033f1d013a9af3670335e9c2f10b` |
| idem, TSV non compressé | 34 166 160 | `f24a24f0d43a685f6c7e73ec641afabeff5f2c754417020d3925ff98ac20fa54` |
| `resume-inventaire-etapes-3-a-6-essai-1-v1.json` | — | `0954aa893965478f49ae5f12839928396dba1ffc228fd5f5697ca8ed056cfeb8` |
| `/home/user/recuperation/palier-0b-programme-1-essai-1-v1.tar` | 3 583 508 480 | `a346064c3f7f796cfa6df5f5fd496e0d28990086599ac65dfd8bc8047607bb1d` |

Parties découpées : aucune.

## Ce qui n'a pas été fait ou s'écarte de la mission

- L'archive suit la consigne de la mère de 08:40Z : tar non compressé à `/home/user/recuperation/palier-0b-programme-1-essai-1-v1.tar`. Ni `.tar.gz` ni `/home/user/recuperation-palier-0b-essai-1-v1/` n'ont été créés.
- Rien n'a été scellé par `controle_ia.scellement`, faute de demande ; les compagnons sont de simples `.sha256`. Rien n'a été commité.
- Aucune comparaison n'a été faite entre les empreintes de l'inventaire et le contenu du tar après extraction : il n'y a pas eu d'extraction. Seuls les comptes ont été comparés.
- Les dates sont toutes ramenées à `--mtime`, mais les droits des fichiers ne sont pas normalisés : les octets du tar dépendent donc des droits des sources.
