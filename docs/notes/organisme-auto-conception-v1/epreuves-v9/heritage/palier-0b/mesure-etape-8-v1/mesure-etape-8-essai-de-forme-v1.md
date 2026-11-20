# Mesure de temps, de mémoire et de place disque de l'étape 8, couche « essai-de-forme » — v1

**EN ATTENTE DU MOT DE LAZAR.** Pièce de travail (classe C). Développeur, modèle O (le développeur du code v6), 2026-11-20 (`date -u` : 17:52Z à l'écriture). Permission de la mère (17:41Z), transmise par la session de coordination : une mesure de temps et de mémoire de l'étape 8 sous la couche « essai-de-forme », sans tirage décisif, sur processeur seul, sans lire aucun résultat. Mêmes interdits que le mandat du code v6 (`46a5e1a4…`). Code mesuré : le code v6 vérifié « Conforme » (`P0B/verification-code-palier-0b-v6-v1.md`, `a7d0b1bc53ab4dd11ac2072e61452c74710530079167d50cafd00182dc5ef1e7`, empreinte recalculée), sur une copie dans ce dossier (`code-v6/`), contrôlée contre la table du code v6 (`639335b9…`, 64 lignes) avant et après les mesures : aucun écart.

## 1. Ce qui a été joué

- Programme : `mesurer_etape_8_v2.py` (et sa version 1, pour une première série ; § 6). Il éprouve d'abord le verrou (une graine de « decisif » et une de « confirmation », demandées sans autorisation : chacune refusée, rien n'est dérivé) ; écrit des fichiers gelés **factices** (fréquences d'essai ; réglages plantés, toutes cibles atteignables : 89 cases, 61 au mode « tirages », 28 au mode « sources ») ; joue `etapes.etape_8` sous la couche « essai-de-forme », la seule qu'il accepte, à une taille réduite connue (`tailles`) ; mesure le temps écoulé de cet appel (`time.perf_counter`) et la mémoire résidente maximale du processus (`resource.getrusage(RUSAGE_SELF).ru_maxrss`) ; relève la taille en octets des fichiers écrits (`os.path.getsize`, sans les ouvrir), séparément pour les cases « tirages », les cases « sources » et le manifeste avec sa liste d'étiquettes ; contrôle qu'aucune couche autre que « essai-de-forme » n'a été dérivée ; relève l'état du cache de la loi exacte du test des rangs signés (`rangs_signes._loi_exacte.cache_info()`, un état interne du code, non une sortie).
- Commande (une par mesure, l'une après l'autre, aucune autre charge de ma part en même temps ; dossier courant : la copie du code) :
  `env -C <bloc-notes>/dev-palier-0b-v6/mesure-etape-8/code-v6 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B ../mesurer_etape_8_v2.py TIRAGES SOURCES <dossier neuf> <résultat neuf>.json`
- Tailles réduites : 50, 100, 200 tirages par case (200 est la borne de l'annexe C) ; 4 000 et 8 000 sources par case (deux et quatre lots de 2 000).
- Contrôles : chaque mesure a joué 89 cases ; couches dérivées : « essai-de-forme » seule ; les deux refus du verrou ont eu lieu. Rien n'a été lu des sorties au-delà de leur existence et de leur taille.

## 2. Mesures (série v2, Python 3.13.18, quatre processeurs partagés)

| tirages | sources | temps de l'étape 8 | mémoire résidente max | entrées du cache | disque « tirages » | disque « sources » | manifeste et étiquettes |
|---|---|---|---|---|---|---|---|
| 50 | 4 000 | 18,56 s | 577 064 Kio | 29 947 | 6 534 738 o | 5 964 472 o | 102 374 o |
| 100 | 4 000 | 31,02 s | 966 780 Kio | 48 982 | 12 657 799 o | 5 964 472 o | 127 822 o |
| 200 | 4 000 | 53,53 s | 1 590 484 Kio | 78 058 | 24 903 799 o | 5 964 472 o | 186 103 o |
| 100 | 8 000 | 36,05 s | 967 532 Kio | 48 982 | 12 657 799 o | 11 788 472 o | 161 584 o |
| 200 | 8 000 | 63,76 s | 1 591 360 Kio | 78 058 | 24 903 799 o | 11 788 472 o | 219 865 o |

Mémoire résidente avant l'étape 8 (imports, fichiers factices) : environ 36 200 Kio dans chaque mesure. Fichiers : `resultat-v2-<tirages>-<sources>.json`.

## 3. Extrapolation aux tailles gelées (10 000 tirages par case ; 200 000 sources par case), par `extrapoler_v1.py`

**Règle du temps et du disque : linéaire, y = a + b × tirages + c × sources, moindres carrés sur les cinq mesures.** Raison, tirée du code : au mode « tirages », chaque case simule ses tirages par lots indépendants de taille fixe (41 tirages de 48 sources, ou 125 de 16) et lit chaque tirage pour lui-même (une lecture par tirage et par nombre de la grille) ; au mode « sources », chaque case simule ses sources par lots indépendants de 2 000, sans lecture ; les tableaux écrits ont une taille proportionnelle au nombre de tirages ou de sources ; aucun calcul ne relie deux lots. Le coût est donc une somme de coûts par lot et par tirage, aux effets du cache près (§ 5).

| grandeur | a | par tirage (toutes les cases « tirages ») | par source (toutes les cases « sources ») | résidu max | **aux tailles gelées** |
|---|---|---|---|---|---|
| temps | −1,6 s | 0,2455 s | 0,00184 s | 1,6 s | **≈ 2 820 s, soit ≈ 47 min** (2 455 s pour les tirages, 368 s pour les sources), un processus |
| disque, cases « tirages » | 0,41 Mo | 0,12246 Mo | — | 2·10⁻⁵ Mo | **≈ 1 225 Mo** |
| disque, cases « sources » | 0,14 Mo | — | 0,001456 Mo | 10⁻¹⁴ Mo | **≈ 291 Mo** |
| disque, manifeste et étiquettes | 0,04 Mo | 0,00057 Mo | 8·10⁻⁶ Mo | 0,0015 Mo | **≈ 7 Mo** |
| **disque, total** | | | | | **≈ 1,52 Go** (mon calcul du rapport du code v6, tableaux seuls : ≈ 1,54 Go) |

**Règle de la mémoire : non linéaire en tirages, bornée par le cache.** La mémoire ne dépend pas du nombre de sources (4 000 contre 8 000 sources, au même nombre de tirages : même mémoire à 1 Mio près) ; elle croît avec le nombre de tirages, et elle suit le nombre d'entrées du cache `functools.lru_cache(maxsize=200_000)` de `rangs_signes._loi_exacte` (une entrée par jeu distinct de rangs ; il garde deux tableaux de queues de loi par entrée). Ajustement : mémoire résidente max ≈ −64 049 Kio + 21,17 Kio par entrée (résidu max 7 071 Kio). Les entrées croissent moins vite que les tirages (≈ 2 014 × tirages^0,69 sur les mesures à 4 000 sources) : le plafond de 200 000 entrées est atteint vers 775 tirages par case, bien avant 10 000. **Au plafond : ≈ 4,3 Go de mémoire résidente** pour le processus de l'étape 8, auxquels s'ajoutent les tableaux d'une case en cours (non mesurés à pleine taille ; de l'ordre de 0,1 à 0,3 Go pour la plus grande, cinq bras de 480 000 sources, d'après le code). **Borne haute, tirée du code** : une entrée garde au plus deux tableaux de 2 353 entiers de 64 bits (rangs doublés de 48 différences, somme au plus 2 352), soit environ 38 Ko, plus sa clé ; au plafond, au plus ≈ 8 Go. Une extrapolation linéaire en tirages (≈ 62 Go) serait fausse : le cache plafonne.

## 4. Ce que cela dit pour le lancement (constat, rien n'est tranché)

- Temps : de l'ordre de 45 à 60 minutes pour l'étape 8 entière, un processus, sur cette machine, si la règle linéaire tient (§ 5). L'étape 9, s'il y a des cases à confirmer, n'est pas mesurée : une case retirée coûte de l'ordre de dix fois une case de l'étape 8 en simulation (100 000 tirages contre 10 000), et sa lecture n'est faite qu'aux nombres retirés.
- Mémoire : de l'ordre de 4,5 Go, au plus de l'ordre de 8 Go, pour le processus.
- Disque : ≈ 1,5 Go pour l'étape 8, dont ≈ 0,7 Go de reliquat (rapport du code v6, § 8).

## 5. Limites

1. **Effet du cache sur le temps.** Aux tailles réduites, 75 % des appels à la loi exacte trouvent leur entrée au cache (234 701 succès pour 78 058 échecs à 200 tirages), et le temps par tirage baisse un peu quand les tirages croissent (0,249 s de 50 à 100 tirages, 0,225 s de 100 à 200). Après le plafond (vers 775 tirages), l'éviction LRU peut faire baisser ce taux de succès et monter le temps par tirage ; la règle linéaire ne le voit pas. Aucune mesure au-delà de 200 tirages n'a été faite (borne de l'annexe C), si bien que le temps à pleine taille est une extrapolation, non une mesure.
2. **Bruit de la machine.** Quatre processeurs partagés ; d'une série à l'autre, aux mêmes tailles, le temps a varié de quelques pour cent (31,02 s contre 29,88 s à 100 tirages et 4 000 sources), et la pente par source de 1,3 à 2,6 ms selon la paire de mesures ; l'ajustement sur cinq points la donne à 1,84 ms.
3. **Fichiers gelés factices.** Les réglages plantés (K, τ, φ, γ) ne sont pas ceux de l'étape 6 ; le temps de simulation des lecteurs dépend de K (paires examinées), et la loi exacte dépend des différences tirées : aux réglages réels, le temps et le nombre d'entrées du cache peuvent différer.
4. **Grille entière.** L'étape 8 lit chaque tirage à toute sa grille (12 ou 16 nombres, avec 6 à 9 en plus pour la famille B) : cette mesure ne suit donc pas la clause « deux nombres de sources » de l'essai de forme de l'annexe C, qui vise `tirages.essai_de_forme` ; elle en garde la couche, la borne de 200 tirages par case, et ne lit ni ne calcule aucun taux. Le coût de la lecture, qui domine, y est donc compté comme à l'étape 8.
5. **Mémoire d'une case à pleine taille** : non mesurée ; estimée d'après le code.
6. **Disque** : les tailles comprennent les compagnons `.sha256`, les descriptions `case.json`, le manifeste et la liste des étiquettes ; le système de fichiers peut arrondir l'occupation réelle par bloc (3 456 fichiers par lancement).

## 6. Gestes

- Série v1 (`mesurer_etape_8_v1.py`, même programme sans le relevé du cache) : 100 et 200 tirages, 4 000 et 8 000 sources, et un essai de bon fonctionnement à 5 tirages et 200 sources ; mêmes octets écrits que la série v2 aux mêmes tailles, mêmes mémoires à 1 Mio près, temps à quelques pour cent près. La série v2 a été jouée parce que la v1 montrait une mémoire qui croît avec les tirages ; seule la v2 sert à l'extrapolation. Fichiers : `resultat-<A|B|C|D>-…json`, `resultat-essai-5-200.json`.
- Aucune graine décisive dérivée ; aucune couche autre que « essai-de-forme » ; aucun fichier gelé des étapes 5 et 6 ; aucune sortie lue au-delà de son existence et de sa taille ; aucun appel à un fournisseur, aucune dépense, aucune écriture dans le dépôt, aucun commit ; aucune commande de recherche ni de liste de processus ; aucune commande d'arrêt ; aucun refus de permission, de classifieur ni de garde. Les dossiers de sortie (`run-*`) restent dans ce dossier du bloc-notes, non inventoriés au-delà de leurs tailles.

## 7. Fichiers (chacun avec son compagnon `.sha256` dans ce dossier)

`mesurer_etape_8_v1.py`, `mesurer_etape_8_v2.py`, `extrapoler_v1.py`, `resultat-v2-50-4000.json`, `resultat-v2-100-4000.json`, `resultat-v2-200-4000.json`, `resultat-v2-100-8000.json`, `resultat-v2-200-8000.json`, et ce rapport.

Développeur, modèle O.
