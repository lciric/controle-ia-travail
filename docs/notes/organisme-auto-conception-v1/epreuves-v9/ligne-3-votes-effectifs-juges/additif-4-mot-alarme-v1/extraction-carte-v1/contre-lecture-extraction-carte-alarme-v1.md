# Contre-lecture du programme qui n'extrait que la carte de l'alarme — v1

Pièce de travail (classe C) sur une pièce d'instrument (classe B). Signé : contre-lecteur, modèle S.
Mandat lu en entier, empreinte vérifiée (`3410e1fe…`, OK). Empreintes vérifiées contre leurs compagnons, toutes OK : mandat du développeur (`53bf2bd7…`), programme (`79f2cc69245a0e00f2c9bc77202440447cbd0db32dc491a7c5dc8ed6bf539659`), essais (`4103e3e643253ed15590a6e19f6e36deb8226cdc106938e7e5460662159d0819`), rapport (`4a1356c3…`), masque scellé (`07ed8725…`). Je n'ai touché ni au vrai fichier des cartes ni à rien sous `archives-reponses-modeles/`. Aucune écriture dans le dépôt, aucun commit.

## Verdict : Conforme

Aucune correction exigée. Trois suggestions facultatives (point 4) et une question pour la mère (point 3, remarque 2 bis).

## 1. Le code, lu en entier

- Empreinte calculée sur les octets avant tout décodage (`lire_octets_verifies`, l. 102) ; `decoder` n'est atteint qu'après. Un essai l'établit par piège.
- Structure lue comme le masque (l. 90-99 du masque) : premier niveau objet `{identifiant: enregistrement}`, enregistrement objet portant `contenu`, `meta` clé de l'enregistrement. Reproduite à la lettre (l. 134, 154, 162).
- Compte 94 : nombre de clés distinctes ; identifiant absent, double, autre clé double : refus distincts. Les clés en double restent visibles grâce aux paires (le masque les écraserait en silence ; c'est plus strict, en refus explicite, donc sans repli).
- Seule la carte visée est gardée ; `meta` écarté (l. 160) avant toute conversion ; sa valeur n'est jamais convertie ni lue (essai par espion). Les autres cartes ne servent qu'au compte et sont relâchées (`del`).
- Aucune autre carte, aucun autre identifiant, rien de `meta` en sortie, à l'écran ou en journal : les messages sont des motifs fixes ; aucun message de décodeur repris ; `except Exception` ne rend que le type ; pas de trace. L'identifiant gelé n'apparaît pas non plus dans les messages. Il n'y a aucune journalisation.
- Sortie refusée avant toute lecture des fiches : existe (lien pendant compris, compagnon compris), composant `archives-reponses-modeles` (forme absolue et résolue), sous le dépôt (formes absolue et résolue, voisin `-autre` non confondu), dossier parent absent. Écriture en `x`/`xb`, jamais d'écrasement.
- Ligne de commande : `--fiches` et `--sortie` seuls, `allow_abbrev=False`, constantes gelées passées en dur.
- Cas limites que j'ai ajoutés (fichier `sondes_contre_lecteur_v1.py`, 9 sondes, toutes passées) : nombre flottant `NaN` (accepté, écrit tel quel : le masque le lirait de même, pas un défaut) ; substitut Unicode isolé (refus code 2, rien écrit) ; BOM (refus) ; entier géant (refus, la limite de chiffres est une `ValueError`) ; imbrication très profonde (refus, rien écrit) ; `meta` dans `contenu` gardé ; clé `meta` écrite par échappement `meta` bien retirée ; sortie en chemin relatif acceptée ; échec d'écriture du compagnon : refus avec message dédié.

## 2. Essais rejoués

Sur copies, dans mon dossier, commande du mandat : `42 passed in 0.20s` (copies de mêmes empreintes que les originaux). Sondes ajoutées : `9 passed`.
Ce qui manque aux essais du développeur (aucun n'est bloquant) : `NaN`, substitut isolé, BOM, entier géant, imbrication profonde, échec d'écriture du compagnon, sortie en chemin relatif, clé `meta` échappée.

## 3. Les quatre remarques du rapport (cinq numérotées dans le rapport ; les quatre du mandat d'abord)

1. Mémoire : GARDER. Inévitable avec la bibliothèque standard ; le tout est relâché avant l'écriture, et rien n'est écrit ou affiché.
2. Gardes ajoutées : GARDER toutes. Chacune est un refus explicite, testée sur un cas sain et sur un artefact ; aucune n'est de trop.
   2 bis. À PORTER À LA MÈRE (ni correction ni défaut) : le programme garde toutes les clés de l'enregistrement sauf `meta` (ici `empreinte`, et toute autre clé que le fichier réel porterait). Le masque dit que `meta` porte l'espèce ; je n'ai pas pu vérifier, faute d'avoir le droit de lire le fichier, qu'aucune autre clé ne la porte. À la mère de confirmer, sur le texte de la ligne 3, que « la carte sans `meta` » veut bien dire cela.
3. `meta` au premier niveau de l'enregistrement seulement : GARDER. C'est la lettre du mandat et la structure du masque ; un `meta` à l'intérieur de `contenu` fait partie du contenu (sondé : conservé).
4. `-B` sans `-I` : voir point 4 ci-dessous ; recommandation d'ajouter `-I`, non exigée.

## 4. La commande de jeu

Juste et suffisante : chemin du fichier conforme au mandat, refus clairs, sortie neuve, vérification préalable de l'empreinte du programme prévue. Suggestions facultatives, au choix de la mère :
- Ajouter `-I` : `python -B -I …/extraire_carte_alarme_v1.py …`. Le programme n'importe que la bibliothèque standard, mais `-I` écarte `PYTHONPATH` et le site utilisateur. Je n'ai pas rejoué le programme en ligne de commande avec `-I` (impossible sans le vrai fichier) ; l'effet est connu du langage et le programme n'a besoin d'aucun chemin d'import.
- Écrire `DOSSIER_DE_SORTIE` en chemin absolu dans la commande jouée (un chemin relatif fonctionne, sondé, mais l'absolu évite toute ambiguïté avec le répertoire de l'`env -C`).
- Faire vérifier ensuite le compagnon par `env -C DOSSIER_DE_SORTIE sha256sum -c carte-alarme-v1.json.sha256`, et faire rapporter le code de sortie lu à l'écran.

## Écarts

Aucun. Lectures par l'outil de lecture, chemins complets ; pas de commande de liste ; une commande simple par appel ; fichiers écrits par l'outil d'écriture ; pas de code en ligne ; aucun refus de permission ni de garde.
