# Contre-lecture du correctif de la pagination de l'arbre du corpus (lanceur version 8 de la première passe de la lecture des sondes par la lentille publique) — v1

Rendu du contre-lecteur neuf, le 2026-11-21, sur Opus 5.5 (pas l'auteur du code). Je n'ai écrit ni le code, ni les essais, ni le mandat.
- Mandat : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-contre-lecteur-correctif-pagination-corpus-v1.md`
  (`92f1abb2605c221988efc1e757f6cfecc44138aeb88f25d73fc1106746fd7e67`, vérifié par `controle_ia.scellement verifier`).
- Code jugé : commit `11f1cee78` (fusion `6afd9c846`), branche `claude/brave-galileo-jhp684`, lue à `5f5020e7f`.

## 1. Verdict

**Conforme, aucun écart bloquant.** Le lanceur version 8 et le module `corpus_pagine_v1` peuvent remplacer le lanceur version 7 pour la
première passe :
- le seul changement de fond est la source des cibles des essais d'un octet du corpus ;
- le texte de lecture v1 scellé n'exige qu'« un octet d'un fichier de chaque jeu de données du corpus des jetons gardés », et le module
  le fournit ;
- le module lit l'en-tête `Link` dans la forme que sert réellement l'hôte (§ 4, point 1). Il suit donc les pages jusqu'à un fichier de
  données.

Trois corrections non bloquantes (§ 5).

## 2. Empreintes vérifiées

Pièces scellées, vérifiées « OK » par `controle_ia.scellement verifier` :
- mandat du développeur `c0c07faa…` ;
- note du développeur `6e996045…` ;
- outils `fabrique-lanceur-v8-v1.py` `85db1533…`, `essai-des-essais-corpus-pagine-v1.py` `5f9ec6d3…` et
  `sortie-essai-des-essais-corpus-pagine-v1.txt` `5b1fc9ee…`.

Pièces sans compagnon (code, essais, `requirements-cpu.txt`, `CLAUDE.md`), comparées par `sha256sum` aux empreintes du mandat et de la
note : toutes égales.
- `corpus_pagine_v1.py` : `77fb4356…`
- `lanceur_v8.py` : `0bba5d4e…`
- `lanceur_v7.py` : `a5d6fc7b…`, égal à celui du commit `cc7f4576`
- `montage_v1.py` : `199e5e18…`, non modifié

Le texte de lecture v1 a été lu par `git show origin/main:…` : `ca5066d7…`. Seuls le « Plan d'analyse » et les lignes qui parlent
d'octet, de montage et d'arbre ont été lus ; la section qui porte la liste « Jamais ouverts » a été sautée.

Le commit `11f1cee78` n'ajoute que des fichiers neufs. Il ne change qu'un fichier existant, `requirements-cpu.txt`, de deux lignes.

## 3. Essais rejoués (comptes seulement)

- Fichier du correctif et les trois fichiers d'essais du lanceur version 8 : **130 réussis**, 0 échoué, en 142 s.
  - Commande : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q tests/test_lentilles_sondes_bbis_corpus_pagine_v1.py
    tests/test_lentilles_sondes_bbis_lanceur_v8_*.py`.
  - Environnement : Python 3.13.18, torch 2.14.1, `requests` 2.34.2. Le venv est hors du dépôt, dans mon bloc-notes ; il est posé sur
    les paquets du `.venv` du dépôt, plus `requests` installé.
- Essai des essais rejoué : voir § 6.

## 4. Les six points

**Point 1 — forme réelle de l'en-tête `Link` : tenu.**
- **La forme réelle.** Le code source public de `huggingface_hub` 1.33.0, installé dans le `.venv`, a été lu dans
  `utils/_pagination.py`. Il suit les pages par `response.links["next"]["url"]`, « same "Link" header format as GitHub ». La
  bibliothèque précise que le lien suivant porte déjà la requête entière.
  - `list_repo_tree` bâtit `{endpoint}/api/{type}s/{repo_id}/tree/{quote(revision, safe="")}`. Le nom du jeu n'y est **pas** encodé.
  - Le client public JavaScript `@huggingface/hub` (`src/lib/list-files.ts`, lu par cdn.jsdelivr.net) bâtit l'adresse de même et lit
    `parseLinkHeader(res.headers.get("Link")).next`.
  - La forme citée en commentaire de ce client est `<https://huggingface.co/api/datasets/bigscience/P3/tree/main?recursive=1&cursor=…>;
    rel="next"`. L'adresse y est absolue, sur le même hôte, et la barre du nom du jeu n'est pas encodée.
- **Le module la lit.** J'ai construit un essai local, sans aucune requête, sur un `requests.Response` construit à la main. Le module y
  rend la même adresse que `requests.Response.links` sur sept formes : forme réelle avec curseur encodé `%3D` ; révision écrite en
  entier ; révision à `/` encodé ; nom du jeu à `/` encodé ; hôte en majuscules ; port explicite ; « prev » puis « next ».
  - Sur un lien relatif, `requests` rend le chemin brut et le module le résout contre l'adresse demandée, ce qui est mieux.
  - `r.headers` de `requests` est insensible à la casse, donc `get("Link")` lit aussi `link`.
- **La garde du lien.** Elle laisse passer la forme réelle, une révision écrite autrement et une révision à `/` encodé. La révision et la
  requête ne sont pas comparées : c'est voulu, et c'est juste.
  - Elle **refuse** trois formes : le nom du jeu à `/` encodé (`HuggingFaceFW%2Ffineweb-2`), l'hôte en majuscules et le port `:443`
    explicite.
  - Aucune des trois n'est la forme que montrent les sources publiques. Un refus tombe sur un arrêt nommé avant tout téléchargement
    long, jamais en silence. Ce n'est donc pas un refus à tort d'un lien réel connu.
  - Correction non bloquante 1 (§ 5).

**Point 2 — borne de 100 pages, plus petit chemin de la première page qui porte un fichier : tenu.**
- **Conformité au texte.** Le texte demande « un octet d'un fichier de chaque jeu de données » (« Plan d'analyse », point 4, réseau
  avant tout flux long). Il ne nomme pas le fichier. Prendre le plus petit chemin de la première page qui porte un fichier de données
  respecte donc la lettre.
  - Le fichier peut ne pas être sous `data/cmn_Hani/train`. L'essai d'un octet prouve l'accès au même jeu, à la même révision et au
    même hôte, ce que le texte demande ; il ne valide pas un fichier précis.
  - Le choix est déterministe pour un arbre donné. Il rend le résultat de l'ancien code quand la première page porte un fichier, ce que
    tient un essai d'égalité.
- **Suffisance.** À 1 000 entrées par page, 100 pages couvrent 100 000 entrées avant le premier fichier.
  - La première page de l'arbre réel ne porte que des dossiers. L'hôte sert donc des dossiers avant les fichiers, au moins en tête.
  - Ordre de grandeur, de mémoire publique et non vérifié : `fineweb-2` compte de l'ordre de quelques milliers de dossiers de langues.
    Avec les variantes « removed » et les sous-dossiers `train` et `test`, cela fait environ 10⁴ dossiers, soit une quinzaine de pages
    au pire avant un fichier.
  - La borne garde une marge d'un facteur supérieur à 5. Si elle était dépassée, l'arrêt nommé de la borne le dirait, avant tout
    téléchargement long.
  - Le temps reste raisonnable : au plus 100 requêtes à 60 s de délai chacune.

**Point 3 — lanceur version 8 égal à la version 7 à ce seul changement près : tenu.**
- `diff lanceur_v7.py lanceur_v8.py` donne exactement quatre changements :
  - sept lignes de docstring (paragraphe « Version 8 ») ;
  - l'import `from . import corpus_pagine_v1 as cp` ;
  - la ligne de `MODULES`, qui ajoute `corpus_pagine_v1` et remplace `lanceur_v7` par `lanceur_v8`, soit quatorze modules ;
  - l'appel `cp.cibles_corpus(voisin, transport)`.
- Le transport est construit à l'identique. `_versions()` relevait déjà `requests` en version 7.
- `exiger_fiche_code` parcourt `MODULES`. Une fiche sans l'empreinte de `corpus_pagine_v1.py`, ou avec une autre empreinte, refuse le
  départ : un essai sain et deux artefacts le tiennent.
- **Aucune clé exposée.**
  - Aucune fonction du module ne reçoit la clé.
  - `page_requests` appelle `_ouvrir(url, None, …)`, donc sans en-tête `Authorization`, comme l'ancien code pour l'arbre.
  - Les messages ne portent que le type de l'exception, la cible sans requête et le code. Un lien refusé n'est pas cité.
  - Le montage entier sur jouets n'écrit la fausse clé dans aucun fichier.

**Point 4 — essais du défaut et de la correction (R5), essai des essais : tenu.**
- Les artefacts qui reproduisent l'arrêt de l'ancien code :
  - `montage_v1.cibles_corpus` sur la même réponse paginée donne la phrase exacte « … aucun fichier de données dans l'arbre … » ;
  - l'artefact au niveau du lanceur : `lanceur_v7.monter` sur un monde des jouets à arbre paginé s'arrête sans aucun flux ;
  - de même sur le transport réel, avec une session fabriquée.
- Les cas sains : le module neuf sur la même réponse, le montage entier version 8 (sept essais d'un octet tenus, cinq pages lues sans
  clé, avant tout flux) et le transport réel sur une session fabriquée.
- Les gardes sont éprouvées des deux côtés :
  - borne, de part et d'autre du bord ;
  - lien hors de l'arbre, sept adresses jamais demandées ;
  - transport sans page, aucune requête ;
  - refus sur la première et la deuxième page ;
  - provenance absente ou illisible ;
  - lecture de l'en-tête sur douze formes.
- **L'essai des essais tient.**
  - Il défait douze lignes dans une copie jetable hors du dépôt et fait passer cette copie en tête des chemins d'import.
  - Le fait que les douze défaites tombent prouve que la copie est bien celle qui est lue : sinon, elles passeraient toutes.
  - Je l'ai rejoué (§ 6). Correction non bloquante 2 (§ 5).
- Les copies des essais version 7 vers version 8 ne diffèrent que par les noms de version et les trois accords déclarés : `page` et
  `suites` du transport des jouets, quatorze modules, double refus de la fiche. L'outil de fabrique rejoué rend les onze fichiers à
  l'octet près ; un essai le tient.

**Point 5 — `requests==2.34.2` : tenu.**
- La version est publiée au registre public des paquets : `pip index versions requests` la donne comme la plus récente.
- Elle s'installe sur Python 3.13.18 avec `urllib3` 2.8.0, `certifi` 2026.11.20, `idna` 3.20 et `charset-normalizer` 3.5.2.
- `pip check` ne trouve aucun conflit avec torch 2.14.1, transformers 5.18.0, huggingface_hub 1.33.0, etc.
- `huggingface_hub` 1.33 emploie `httpx` et non `requests`, ce qui explique le manque relevé. La ligne ajoutée est nécessaire et
  épinglée comme les autres.

**Point 6 — autres écarts bloquants : aucun.**
- Les trois arrêts nouveaux (borne, lien hors de l'arbre, transport sans page) ne figurent pas mot pour mot dans la « Liste d'arrêt »
  du texte.
  - Ils sont de la même famille : arrêt avant tout téléchargement long, nœud.
  - Ils ne font que refuser un repli silencieux (R5). Ils ne changent rien à ce que le texte exige.
- Une page illisible comme JSON remonte l'erreur de décodage, comme dans `montage_v1`. Cela reste sans exposition de la clé.
- Le `.venv` du dépôt n'a pas `requests`. Remarque d'environnement, pas du code : l'opérateur doit réinstaller `requirements-cpu.txt`
  avant le montage.

## 5. Corrections demandées (aucune bloquante)

1. **Non bloquante — garde du lien.**
   - Défaut : elle compare les chaînes brutes. Un lien légitime à l'hôte écrit en majuscules, au port `:443` explicite ou au nom du jeu
     à `/` encodé serait refusé, d'un arrêt nommé et sûr, mais coûteux s'il venait.
   - Correction : dans une version neuve du module si l'arrêt se produit, comparer sur `urllib.parse.urlsplit`, avec schéma `https`,
     hôte en minuscules sans port 443, et chemin passé par `unquote`. Inutile tant que l'hôte sert la forme publique documentée.
2. **Non bloquante — essai des essais.**
   - Défaut : la ligne « copie saine » n'entre pas dans le code de retour. Une copie saine qui tomberait afficherait « TOMBE
     (inattendu) », mais le script rendrait quand même 0 si toutes les défaites tombent.
   - Correction : dans une version neuve de l'outil, faire rendre 1 dans ce cas. Sans effet ici : la copie saine passe, dans la sortie
     scellée comme dans mon rejeu.
3. **Non bloquante — environnement.** Rappeler à l'opérateur, dans la fiche du montage ou dans la passation, d'installer
   `requests==2.34.2` par `requirements-cpu.txt`. Le `.venv` actuel du dépôt ne l'a pas.

## 6. Essai des essais rejoué

Rejoué avec l'interpréteur de mon venv, hors du dépôt : copie saine « passe » ; **12 défaites, 12 vues, 0 inaperçue**, code de retour 0.
Le résultat est identique ligne pour ligne à la sortie scellée `5b1fc9ee…`.

## 7. Cloisonnement, expositions, refus

- **Jamais ouverts ou lus :**
  - `diag/`, `runs/`, `docs/verdicts/` ;
  - les branches `calcul/*`, `donnees/*` et `verdict/*` ;
  - aucun `arret.json` ;
  - aucune sortie, aucun score et aucune table de l'apprentissage des sondes sur la tâche ni de la lecture par la lentille publique ;
  - aucun fichier « consigne-privee » ni « conception-ii-b » ;
  - la section « Entrées exactes, et ce qui n'est jamais ouvert » du texte v1.
- **Réseau :** aucune requête vers l'API de Hugging Face, aucun téléchargement de modèle ni de données, aucune clé lue.
  - Pages publiques lues : une recherche web et `cdn.jsdelivr.net` (code source public de `@huggingface/hub`).
  - Paquet installé dans mon bloc-notes : `requests` depuis le registre public des paquets.
- **Intitulé interdit vu :** aucun.
- **Dépôt :** aucun fichier de l'autre développeur touché, rien committé, aucun `git add`, `checkout`, `merge` ni `stash`.
- **Refus d'outil :** un refus de forme, déclaré et non rejoué. Une commande `sleep 240` suivie d'une lecture a été refusée ; l'attente
  s'est faite par une commande de fond.
