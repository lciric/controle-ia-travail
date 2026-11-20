# Rapport du développeur — programme qui n'extrait que la carte de l'alarme, champ `meta` retiré — v1

Pièce d'instrument (classe B), à contre-lire par un autre modèle. Mandat : `mandat-developpeur-extraction-carte-alarme-v1.md` (empreinte vérifiée `53bf2bd70c8790b4c0dd378e3fcdd9fdc7578e07ef776cebd8345cbe0f137841`, OK). Masque scellé lu pour la structure : `masque_style_cartes_v1.py`, empreinte calculée `07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e` (conforme au préfixe `07ed8725…` du mandat). **Programme écrit et essayé sur fichiers synthétiques ; il n'a pas été joué.** Le vrai fichier des cartes et tout chemin sous `archives-reponses-modeles/` n'ont été touchés par aucune commande. Aucune carte lue.

Signé : développeur, modèle O.

## Fichiers (bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-extraction-carte-alarme/`)

| Fichier | Empreinte (sha256) |
|---|---|
| `extraire_carte_alarme_v1.py` | `79f2cc69245a0e00f2c9bc77202440447cbd0db32dc491a7c5dc8ed6bf539659` |
| `essais_extraire_carte_alarme_v1.py` | `4103e3e643253ed15590a6e19f6e36deb8226cdc106938e7e5460662159d0819` |

Chacun avec son compagnon `.sha256` dans le même dossier. Le sous-dossier `essais-temporaires/` ne contient que les fichiers synthétiques créés par les essais.

## Structure reprise du masque, à la lettre

Le masque décode le fichier entier en un objet de premier niveau `{identifiant: enregistrement}` (l'identifiant est la **clé**, l. 90-96), chaque enregistrement est un objet qui porte `contenu` (l. 97-98) ; `meta` et `empreinte` sont des clés de l'enregistrement, jamais lues par le masque (l. 10-11, l. 69-70). Le programme suit ce chemin : clé de premier niveau = identifiant, enregistrement = objet, `meta` = clé de l'enregistrement.

## Ce que fait le programme

1. Paramètres validés (empreinte : 64 caractères hexadécimaux minuscules ; identifiant non vide ; nombre entier ≥ 1).
2. Sortie vérifiée **avant** toute lecture des fiches : refus si la sortie ou son compagnon existe (y compris lien pendant), si la forme absolue ou résolue du chemin a un composant `archives-reponses-modeles`, si elle est sous `/home/user/controle-ia-travail` (forme écrite ou résolue des liens), si le dossier parent est absent.
3. Octets lus ; empreinte calculée sur les octets **avant** tout décodage ; refus si elle diffère (rien n'est décodé).
4. Décodage UTF-8 strict puis JSON, objets gardés en suites de paires (les clés en double restent visibles). Aucun message du décodeur n'est repris.
5. Premier niveau : refus si ce n'est pas un objet ; si l'identifiant gelé est absent ; s'il est présent plus d'une fois ; si une autre clé est en double ; si le nombre d'identifiants distincts diffère de 94.
6. Enregistrement visé : refus s'il n'est pas un objet ou a une clé en double ; la paire `meta` est écartée **avant** toute conversion (sa valeur n'est jamais convertie ni lue) ; refus s'il n'a pas `contenu` ; refus d'une clé en double dans tout objet imbriqué de la carte.
7. Écriture neuve (`xb`) d'un JSON à trois champs `carte`, `empreinte_fiches`, `identifiant` (UTF-8, `indent=1`), puis du compagnon `EMPREINTE  NOM\n`.
8. Écran : `FAIT` (sortie standard, code 0) ; ou `REFUS : motif` (erreur standard, code 2), motif sans valeur, sans identifiant, sans empreinte ni chemin ; toute erreur imprévue : `REFUS : erreur imprévue (TYPE) ; aucun détail affiché` (code 3), sans message ni trace. Aucune journalisation.

Le point d'entrée en ligne de commande n'accepte que `--fiches` et `--sortie` (abréviations refusées) et passe les constantes gelées ; le moyen interne `executer(fiches, sortie, empreinte, identifiant, nombre)` / `extraire(...)` sert aux essais.

## Essais et leur sortie

Commande (hors du dépôt) :

```
env -C /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-extraction-carte-alarme /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_extraire_carte_alarme_v1.py
```

Sortie :

```
..........................................                               [100%]
42 passed in 0.20s
```

(Premier passage : 41 réussis, 1 échec dû à l'essai lui-même — la corruption du JSON tombait dans une chaîne et laissait un JSON valide ; l'essai a été corrigé pour couper entre deux paires ; programme inchangé.)

Couverture, chaque garde sur le cas sain (qui les passe toutes) et sur un artefact (R5) :
- cas sain : sortie = la seule carte sans `meta`, trois champs dans l'ordre, empreinte et identifiant justes, compagnon juste, écran `FAIT` seul ; carte sans `meta` acceptée ; la valeur de `meta` et les autres cartes ne passent jamais par la conversion (espion) ;
- empreinte fausse (décodage interdit par un piège : non appelé ; l'empreinte n'apparaît pas à l'écran) ; un octet ajouté ;
- compte faux (93, 95, 1) ;
- identifiant absent ; identifiants voisins (préfixe, suffixe) non pris pour la cible ; identifiant en double (même carte, carte différente) ; autre clé en double ;
- premier niveau non objet ; carte non objet ; carte sans `contenu` ; `meta` en double dans la carte ; clé en double dans `contenu` ;
- JSON illisible semé d'une chaîne repérable (absente du message) ; octets non UTF-8 ; fichier absent ;
- sortie existante (non écrasée), compagnon existant, sortie en lien pendant ; sortie sous un dossier `archives-reponses-modeles` synthétique, directement et par lien ; sortie sous le dépôt, par chemin direct, par détour `./..`, par lien pendant (chemins sous le dépôt choisis inexistants : même une garde fautive n'y écrirait rien ; aucune écriture n'a eu lieu) ; voisin `…-autre` du dépôt non confondu ; dossier parent absent ; sortie vérifiée avant toute lecture des fiches (piège) ;
- paramètres mal formés ; erreur imprévue semée (message absent, aucune trace, code 3) ;
- constantes gelées ; la ligne de commande refuse un fichier synthétique sain (empreinte gelée seule), refuse `--empreinte`, `--identifiant`, une abréviation, un argument manquant ; écran réel d'un refus en processus à part (motif seul) ; écran réel du cas sain en processus à part (`FAIT` seul).

Dans tous les essais : aucune autre carte, aucun autre identifiant, rien de `meta` (chaînes semées), aucune trace dans la sortie ni à l'écran ; le texte de la carte visée n'apparaît jamais à l'écran.

## Commande unique de jeu (gabarit — à jouer par l'agent neuf, non jouée ici)

```
env -C DOSSIER_DE_SORTIE /home/user/controle-ia-travail/.venv/bin/python -B CHEMIN_DU_PROGRAMME/extraire_carte_alarme_v1.py --fiches /home/user/controle-ia-travail/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json --sortie DOSSIER_DE_SORTIE/carte-alarme-v1.json
```

- `DOSSIER_DE_SORTIE` : un dossier existant, hors du dépôt, sans composant `archives-reponses-modeles` (par exemple le bloc-notes du joueur) ; `carte-alarme-v1.json` et son compagnon ne doivent pas y exister.
- `CHEMIN_DU_PROGRAMME` : le dossier où le programme est versé ; vérifier d'abord `79f2cc69…` par `env -C CHEMIN_DU_PROGRAMME sha256sum -c extraire_carte_alarme_v1.py.sha256`.
- Attendu : `FAIT` et code 0, ou `REFUS : motif` (code 2) ou `REFUS : erreur imprévue (TYPE)` (code 3). L'écran ne porte jamais de texte de carte.

## Remarques

1. Mémoire : la bibliothèque standard décode le fichier entier ; toutes les cartes sont donc en mémoire **pendant** le décodage. Après lui, seuls restent : l'enregistrement visé (sans `meta`) ; et, le temps de la fonction de compte, l'ensemble des clés de premier niveau (pour compter et voir les doubles), effacé avant tout retour. Le texte décodé, les octets et l'arbre complet sont relâchés (`del`) dès l'extraction.
2. Gardes ajoutées au-delà de la lettre du mandat, toutes en refus explicite : enregistrement visé non objet ou sans `contenu` (structure différente de celle du masque) ; clé en double dans la carte (le masque, par `json.loads`, garderait la dernière en silence) ; autre clé de premier niveau en double ; dossier parent absent ; lien pendant à la place de la sortie ; erreur imprévue rendue par son type seul. Le contre-lecteur dira si l'une est de trop.
3. `meta` est retiré au seul premier niveau de l'enregistrement, là où le masque le place ; une clé `meta` qui serait **à l'intérieur** de `contenu` serait gardée (elle ferait partie du contenu que le masque lit).
4. `empreinte_fiches` dans la sortie est l'empreinte gelée, égale à l'empreinte calculée (le programme refuse sinon).
5. Le gabarit n'a pas été essayé avec `python -I` ; il l'a été avec `-B`, comme les essais. Le programme n'importe que la bibliothèque standard.

## Écarts

Aucun écart au mandat relevé. Lectures des fichiers par l'outil de lecture et par chemin complet ; fichiers écrits par l'outil d'écriture (aucun heredoc, aucun code en ligne) ; aucune écriture dans le dépôt, aucun commit ; aucun appel à un fournisseur de modèles.
