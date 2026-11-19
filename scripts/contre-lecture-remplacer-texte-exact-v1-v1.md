# Contre-lecture de l'outil de remplacement de texte exact, version 1 (classe B)

Contre-lecteur : modèle S, choisi parce que la seule place du modèle K sur ce compte est prise et que son autre version tire sur la même limite d'usage ; ce n'est pas un refus. Le code est écrit par le modèle L′ ; la mère en a été avertie et l'accepte (pièce de code, classe B).

**Verdict : Conforme.** Aucune correction demandée ; cinq observations sans effet sur le verdict (§ 5).

## 1. Pièces et empreintes

Commit 3cef8569 de `lot/compte-organisme-v1` (existe ; les deux fichiers de l'arbre de travail sont identiques à ce commit). `scripts/remplacer_texte_exact_v1.py` (391db990…), `tests/test_remplacer_texte_exact_v1.py` (e71c606c…) et le rapport (4bd51d13…) : empreintes égales à celles annoncées et à leurs compagnons. L'outil lu en entier, ses essais lus pour leur structure, leurs refus et leurs contrôles de défauts.

## 2. L'outil fait-il ce que la spécification demande, et rien d'autre ?

Oui, ligne à ligne :
- **Entrées et sortie distincte** : cible et JSON lus à l'octet, jamais modifiés ; `--sur-place-interdit` est toujours vrai, aucune option n'écrit sur place ; la sortie, son compagnon, le journal et son compagnon sont refusés s'ils existent, même sous forme de lien symbolique (`lexists`), et créés en mode exclusif (`xb`).
- **Chaque ancien exactement une fois, occurrences chevauchantes comptées** (« aa » deux fois dans « aaa » : refus) ; deux anciens identiques ou deux zones qui se recouvrent : refus (zones contiguës permises) ; ancien vide : refus ; rien n'est écrit dans tous ces cas.
- **Application simultanée** aux positions de la cible d'origine ; contrôle interne indépendant avant écriture (longueur, octets hors zone à l'identique, texte neuf à sa place, UTF-8 strict de la sortie).
- **Chaque neuf une fois de plus après qu'avant** (k fois de plus pour k remplacements au même neuf).
- **Refus** : sortie existante, entrée absente ou illisible ou pas un fichier ordinaire, UTF-8 invalide, JSON mal formé, de la mauvaise forme, clé en double, constante non standard, substitut isolé, ancien égal au neuf, dossier de la sortie absent, sortie égale à la cible ou au fichier de remplacements.
- **Écrit** : la sortie, son `.sha256` (format `sha256sum`), le journal JSON et le compagnon du journal. Rien d'autre.
- **Bibliothèque standard seule** (`argparse`, `datetime`, `hashlib`, `json`, `os`, `sys`, `pathlib`, `__future__`) ; aucun réseau, aucun appel de processus, aucune suppression sauf le nettoyage de ses propres fichiers créés quand une écriture ou la relecture échoue (jamais un fichier préexistant : un fichier non créé par l'appel n'est pas dans la liste de nettoyage).
- **UTF-8 strict et fins de ligne à l'octet** : lecture et écriture en octets ; une marque d'ordre des octets de la cible est conservée ; celle du JSON est refusée.

## 3. R5 : chaque refus, cas sain et artefact

Les 55 essais couvrent : 11 cas sains (simple, octets et fins de ligne, suppression, zones contiguës, application simultanée, neufs identiques, neuf déjà présent, ancien non chevauchant, échappements JSON, option sur place, avertissement de fin de ligne), 20 artefacts de refus (ancien absent, double, chevauchant, zones, ancien répété, neuf par jonction, neuf dans l'ancien, ancien vide, sortie, compagnon, journal existants, sortie égale à la cible, lien pendant, dossier absent, cible absente ou dossier ou non UTF-8, JSON absent, options, écriture interrompue avec nettoyage), 14 artefacts du JSON, le contrôle de la bibliothèque standard et 9 défauts réintroduits un par un. Chaque défaut réintroduit est vu par l'essai visé, et l'essai passe sur l'outil sain (témoin). Aucun repli silencieux : tout refus rend le code 2 avec le motif et « Sortie non écrite ».

Essais rejoués : copie dans mon bloc-notes (dossier `scripts/` et `tests/` à part), **55 passés sur 55** (2,3 secondes). Je n'ai exécuté que cette suite et des lectures ; aucun accès sous `archives-reponses-modeles/` ; aucun code en ligne passé à un interpréteur.

## 4. Jugement des choix de la main du développeur

1. **k occurrences de plus pour k remplacements au même texte neuf** : approuvé. C'est la généralisation naturelle de « une fois de plus » ; avec k = 1 elle redonne la règle de la spécification. Essai « neufs identiques ».
2. **Texte neuf vide permis** : approuvé. Une suppression est un usage légitime ; le contrôle interne (longueur, octets hors zone) la couvre, et l'essai « suppression » le montre. Le texte ancien vide, lui, reste refusé comme demandé.
3. **Refus d'un neuf recréé par jonction avec ses voisins** : approuvé. Le compte du neuf avant et après est ce qui le détecte ; la règle se trompe du côté sûr (voir observation 2). Essai « jonction », défaut « contrôle retiré » vu.
4. **Fins de ligne étrangères signalées sans bloquer** : approuvé. L'avertissement est sur la sortie d'erreur et dans le journal ; il n'a lieu que si la cible a elle-même un style de fin de ligne.
5. **Heure dans le journal** : approuvé. Utile à la traçabilité ; la sortie et son compagnon restent reproductibles à l'octet près, seul le journal porte l'heure.

## 5. Observations, sans correction

1. L'outil écrit quatre fichiers (sortie, compagnon, journal, compagnon du journal) ; la spécification en nomme trois. Le quatrième suit la règle R6 (tout dépôt a son empreinte compagnon) et le rapport le dit ; j'y vois la lettre de R6 et non un écart.
2. La règle du neuf « une fois de plus » est stricte : elle refuse un remplacement qui raccourcit (« foo bar » remplacé par « foo » quand « foo » n'apparaissait qu'à cet endroit), parce que l'occurrence qui disparaît avec l'ancien n'est pas compensée. C'est la lettre de la spécification ; à connaître des agents suivants, qui devront alors étendre l'ancien ou le neuf. Même prudence pour un neuf qui chevauche lui-même (« aa » à côté d'un « a ») : refus, du côté sûr.
3. Un retour chariot seul (« \r » sans « \n ») n'est pas reconnu comme style de fin de ligne ; il n'est donc pas signalé. Sans conséquence pour des fichiers du dépôt.
4. Les essais ne couvrent pas un compagnon du journal préexistant isolé, ni une sortie égale au fichier de remplacements ; les gardes existent dans le code (même boucle `lexists` et même comparaison de chemins que les cas couverts).
5. Les essais lancent l'outil par un sous-processus (pour l'appeler « par son chemin » comme les agents le feront) ; l'outil lui-même n'appelle aucun processus.
