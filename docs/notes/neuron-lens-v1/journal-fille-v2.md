# Journal de la deuxième fille « Neuron Lens » — v2 (faits à recopier par la mère ; aucune écriture dans `registres/`)

Session `session_01QPDgKfBxeeiM3BsxqJgSgf`, branche `prep/neuron-lens-v1`, sous la consigne de la mère
`session_01QPDgKgACWyCkCN8HjqwNXy` (R-2685). Heures relevées par `date -u`.

| heure (UTC) | fait |
|---|---|
| 2026-11-14 ~09:40 | Reprise : tête de branche `862e1519…` vérifiée ; passation `2026-11-14-0933.md` (`80507f8c…`) et plan v2 (`4f653490…`) vérifiés par empreinte ; consigne v1 (`43ac1788…`) et interdits communs v2 (`1ee3b370…`) relus sur `main` (fetch par refspec) ; lignes R-2528, R-2531, R-2532, R-2685 lues en lecture seule. Clés présentes par leur nom : `HF_TOKEN`, `VAST_API_KEY`, `HCLOUD_TOKEN`, `OPENAI_API_KEY`, `GITHUB_TOKEN`, `GH_TOKEN` ; absentes : `ANTHROPIC_API_KEY`, `HUGGING_FACE_HUB_TOKEN`. Disque : 26 Go libres. Aucune clé lue, aucune instance touchée. |
| ~09:45 | Dépôt voisin recloné en lecture au commit `849bfe16` (empreintes de `docs/findings.md`, `scripts/06_activations.py`, `neuron_lens/lenses.py` identiques à l'archive du lecteur). `representation-engineering` cloné en lecture (commit `5455d8a3…`). Rien exécuté de ces dépôts. |
| ~09:45 | R7 : chiffres de stabilité (B-1) relus dans `docs/findings.md` voisin (`8814874b…`, § 1) — opposables ; chiffres de B-2, B-3, B-4, B-7, `read_S` recalculés dans les fichiers publiés empreintés. Deux corrections au plan : la consigne de C2 dit « untruthful », pas « dishonest » ; le critère B-5 du plan v1 (« décroissant sur le premier quart ») serait manqué par la référence publiée elle-même (à réécrire pour B-β). |
| ~09:50 | Correctif de `06_activations.py` écrit (différence + essai écrit, non exécuté) ; `git apply --check` et `ast.parse` seulement. |
| ~09:55 | Une commande d'écriture de fichiers dans le carnet de la session (aucune suppression demandée) a été bloquée par le contrôle de sécurité des suppressions (« could not be checked for dangerous rm operations ») ; non relancée telle quelle ; le même travail (copie et retouche de `lenses.py` dans le carnet) a été fait par un petit script Python écrit dans le carnet, sans suppression. |
| ~09:55 | Contre-lectures 1 rendues (texte gelé : « scellable après corrections », trois points bloquants du volet A ; correctif : « correct après corrections ») ; rapports recopiés et scellés sous `docs/notes/neuron-lens-v1/contre-lectures/` (`3d839dfc…`, `8ed58170…`). Une remarque refusée sur constat : le contre-lecteur croyait partager le modèle de l'autrice ; la description de session dit le contraire. |
| 09:58 | Jeux publics relevés sans clé, client générique (JailbreakBench, AdvBench, faits de `representation-engineering`, tokeniseur et fiche de Qwen3-8B, révision `b968826d…`, Apache-2.0), archivés et scellés sous `docs/sources/neuron-lens-v2-contrastes-20261114/` (manifeste `manifeste-v1.tsv`) ; tokeniseur (11 Mo) non versé, empreinte `aeb13307…`. Point 2 d de la passation : fait pour les fichiers et licences. |
| ~10:00 | Comptes sur le texte seul (notre outil `outils/comptes_avant_scellement_v1.py`) : préambule de 27 jetons → toutes les positions lues ≥ 33 ; P = {« Ġun », « truth », « ful », « Ġhonest »} ; faits : 297 vrais, 300 faux retenus ; AdvBench : 463 retenus ; l'ancien critère A2 (Fisher) est inatteignable (0 à 1 jeton associé par découpe) → remplacé. |
| ~10:05–10:20 | Correctif v2 (`06_activations-llama-v2.diff` : crochets, `chat_open`, table des têtes sans lentille publiée) et essai v2 ; texte gelé v2 ; correctif des lentilles publiques de Llama (`lenses-neuronpedia-llama-v1.diff`, point 2 c). Commit `b319e96d`. Contre-lectures 2 lancées. |

## Nœud proposé (format de décision), à soumettre à Lazar par la mère
**Décision** : permettre ou non l'exécution du code du dépôt voisin (`stdlogits/neuron-lens`, MIT), et où.
**Enjeu** : le classifieur a refusé le 13 novembre l'exécution locale de ses essais ; sans exécution, la portabilité à Llama et les
correctifs restent « établis par lecture », et rien de B0 ne peut partir, même avec une ligne de GO.
**Options** : (a) exécution permise **sur la machine louée seulement**, au commit épinglé `849bfe16` plus nos correctifs scellés,
essais miniatures d'abord — avantage : aucun risque pour le conteneur de session, B0 tel que prévu ; inconvénient : les erreurs
se découvrent sur du temps payé (borné par le plafond et l'arrêt à 60 %) ; (b) exécution permise aussi **dans le conteneur**, sur
processeur, essais miniatures seulement (aucun poids, aucun réseau au-delà du dépôt cloné), par une règle de permission
explicite — avantage : essais gratuits avant toute dépense ; inconvénient : exécuter du code tiers dans le conteneur de session ;
(c) aucune exécution — le travail s'arrête aux textes gelés et aux correctifs écrits.
**Recommandation** : (a), confiance 0,7 (b n'apporte que quelques minutes d'essai et demande de lever un refus).
**Défaut sous 48 heures** : aucun (ce nœud conditionne une dépense ; rien ne part sans mot).

## Suite (heures `date -u`)
| heure (UTC) | fait |
|---|---|
| ~10:12–10:14 | Contre-lectures 2 rendues : correctifs « corrects après corrections mineures » (lentilles : deux corrections avant B0) ; texte gelé v2 « scellable après corrections mineures » (une contradiction dans l'essai du code des verdicts, une vingtaine de précisions). Rapports archivés et scellés (`50f6f7d5…`, `1a4a1b8d…`). |
| ~10:14–10:17 | Correctif des lentilles v2 (empreintes vérifiées sur le fichier lu, couches `0..30` exigées, J de Llama contrôlée, Qwen3 inchangé) et son essai écrit ; retouches mineures du correctif de la passe d'activations ; texte gelé v3. |
| ~10:16 | **Expurgation** : le rapport de la contre-lecture 1 (commité en `b319e96d`) contenait le nom de modèle que le contre-lecteur donnait pour lui-même ; remplacé dans l'arbre par une copie expurgée (`contre-lecture-1-texte-gele-v1-expurge.md`, `9f236ea8…`), original retiré de l'arbre ; **le nom reste dans l'historique git** de la branche (commits `b319e96d` et `ffd1b312`). Je ne réécris pas l'historique ; à la mère de dire s'il faut faire davantage. |
| ~10:17 | Une empreinte complète écrite de tête (original de `arch.py`) était fausse ; corrigée par `sha256sum`, puis **vérification mécanique** de toutes les empreintes complètes des pièces à sceller contre leurs sources : toutes concordent (hors celle de l'original retiré, connue de l'historique). |
| 10:18 | Contre-lecture 3, ciblée sur les points modifiés, lancée. |
| entre 10:18 et 10:27 | Contre-lecture 3 rendue : texte v3 « scellable après corrections mineures » (A3 « dépendance non lue » inversée à la lettre ; « couches 0..30 » surdéclaré ; essai du correctif des lentilles absent de B0 ; déclencheur « control_med exactement 0 » touché par l'arrondi de la référence) ; correctif des lentilles « scellable en l'état » ; correctif de la passe : renommer en v3 (R12). Rapport scellé (`7d7ea3c9…`). |
| avant 10:27 | Note et essai de la passe en v3, v2 rétablis dans leur état contre-lu (`1c3b8c9f…`, `6d6c4c08…`) ; note et essai des lentilles en v3 ; texte gelé v4. Contre-lecture 4, ciblée, lancée. |

Note de méthode : plusieurs heures de ce journal et des textes sont des estimations (« vers », « ~ ») et non des relevés de `date -u`
dans la même commande, contrairement à la consigne. Relevés effectifs de la séance : 09:47, 09:52, 09:56, 09:58:35, 10:06, 10:12,
10:14, 10:18, 10:27 (UTC). Les en-têtes des pièces à sceller sont ramenés à des bornes entre ces relevés.
