# Vérification du devis v3 du service de la question v8 au collisionneur — v1

> Même contre-lecteur que `contre-lecture-devis-v8-v1.md` (230c7b4e…) et `verification-corrections-devis-v8-v1.md` (64045cf7…) : Claude Opus 5.5, sous-agent. 23 novembre 2026. Dépôt au commit 6310d57fb.
>
> Pièces vérifiées :
> - `devis-service-collisionneur-modes-v8-v3.md` (55283f60…, sceau tenu) ;
> - la version servie v2 (f3f47c08…) ;
> - `produire_version_servie_v2.py` et `essais_produire_version_servie_v2.py` ;
> - les deux listes de paires ;
> - `calculs/`, `calculs-devis-v3/` et `calculs-v3/`.
>
> Rien lu sous une branche `coffre/*` ni dans un chemin qui contient « coffre ». Aucun envoi, aucune dépense, aucun commit. Rejeux faits dans le bloc-notes de la session.

## Verdict

**Bon à soumettre à Lazar.** N-1 à N-5 et D-7 sont tenus. J'ai rejoué le programme : il redonne la version servie v2 au même octet. Les essais donnent 26 sur 26. La garde des révisions 8d et 8m ne trouve rien. Une recherche par programme ne trouve dans le texte servi aucun chemin vers une racine du dépôt, `brouillons/`, `donnees/`, `gemini/`, `rapports/`, `tests/`, `traces/` et `src/` compris, aucun chemin entre accents graves et aucune empreinte de commit. Le § 13 décrit juste le trou de la garde.

## 1. Les points demandés

| point | sort | constat |
|---|---|---|
| N-1, option (b) mal décrite | **tenu** | Les retraits hors de la garde passent désormais par une seconde liste fermée, scellée, dont chaque paire porte un nom et une raison. Elle est contrôlée par un programme v2 : chaque paire trouvée une seule fois, dans la zone, sans motif de la garde, sans chevauchement. L'ancienne option (b) devient « la version servie v1 », décrite justement. |
| N-2, `donnees/` | **tenu** | Le chemin `donnees/…` (v8 l. 169) et le commit (l. 155) sont retirés. L'enjeu de la décision 1 cite la condition de GO-2026-11-21-08, « aucun chemin interne, aucun nom », plus large que la garde. |
| N-3, faux sceau | **tenu** | Il est renommé `d-sceau-faux.json.sceau-faux-essai`. Les essais v2 ne laissent aucun faux sceau hors de leur dossier de travail. |
| N-4, artefacts et moteurs | **tenu** | Les empreintes des 16 moteurs sont fixées dans le programme, et les révisions 8d et 8m sont exigées. Une liste malformée donne un arrêt nommé. Les restes sont cherchés aussi sous une forme générale : tout chemin entre accents graves, toute empreinte de 40 caractères hexadécimaux. Les contrôles redondants (reste hors zone, lignes, différentiel, garde résiduelle) sont éprouvés par des mutants. |
| N-5, mention | **tenu** | La mention devient « [renvoi retiré] ». Les faits 16 et 17 se lisent « [source 21, ligne de [renvoi retiré]] » : plus léger, sans conséquence. |
| D-7, compagnons de `calculs/` | **tenu** | 23 compagnons sont présents (22 à la racine, 1 dans `servi/`), et tous se vérifient. |

## 2. Rejeux

| rejeu | résultat |
|---|---|
| `produire_version_servie_v2.py` | Je l'ai lancé sur une v8 témoin : tête factice portant la phrase prescrite, puis `calculs/servi/question-v8-depuis-le-titre.md`, 38a1a8e9…. Seule l'empreinte attendue de la v8 change, dans le programme comme dans les listes, qui sont rescellées. Moteurs 8d (b7803838…) et 8m (420394f9…). Résultat : code 0, 23 remplacements (21 de la garde, 2 nommés), **version servie f3f47c08… identique à celle versée**. |
| `essais_produire_version_servie_v2.py`, même témoin | Code 0, **26 essais sur 26** : le cas sain, et 25 artefacts et mutants refusés au code 2 sans écriture (listes de la garde et supplémentaire, v8 altérée, sortie existante, moteur inconnu ou d'empreinte fausse, moteurs exigés absents, reste dans le texte servi, cinq mutants, moteurs en désaccord). |
| Garde de motifs des moteurs 8d et 8m, sur la version servie v2 | aucune occurrence |
| `calcul_devis_v8_v3.py`, sur la version servie v2, dans un dossier neuf | sortie identique à `calculs-devis-v3/sortie-calcul-devis-v8-v3.txt` : pointe 19,99, plafond 26, deux coupures de Carbon de plus tolérées |
| Sceaux de `version-servie/`, `calculs/`, `calculs-devis-v3/` et du devis v3 | tous tenus |

## 3. Le § 13 du devis : le trou de la garde

- **Le constat du § 13 est exact.** Le motif « chemin interne » de la garde (`collisionneur_v9_v8d.py`, identique en 8m) admet une liste fixe de racines. J'ai sondé `` `brouillons/x/y.md` ``, `donnees/`, `gemini/`, `rapports/`, `tests/`, `traces/` et `` `src/autre/x.py` `` : la garde ne les refuse pas. `` `src/controle_ia/x.py` `` est refusé.
- **Le texte servi v2 ne passe aucun de ces chemins.** Recherche par programme sur le fichier f3f47c08… :

| motif cherché | occurrences |
|---|---|
| chacune des 16 racines suivies de « / », hors d'un mot : `brouillons`, `donnees`, `gemini`, `rapports`, `tests`, `traces`, `src`, `diag`, `docs`, `livrables`, `papiers`, `prereg`, `registres`, `runs`, `scripts`, `archives-reponses-modeles` | 0 pour chacune |
| chemin entre accents graves contenant « / » | 0 |
| empreinte de commit de 40 caractères hexadécimaux | 0 |
| nom de fichier à extension (`.py`, `.md`, `.json`, `.txt`, `.jsonl`, `.sha256`, `.diff`, `.csv`, `.yaml`) | 0 |
| `GO-`, identifiant de registre (`R-` suivi de chiffres), nom du dépôt | 0 |
| mots contenant « / » | « Deployment/hardware: » et « latency/throughput », des mots du texte, pas des chemins |

- **Seule remarque, de forme.** Le § 13 écrit « six racines », puis ajoute `src/` hors de `src/controle_ia/`. Le compte est juste, la phrase un peu ambiguë. Cela ne demande aucune correction avant la remise.
