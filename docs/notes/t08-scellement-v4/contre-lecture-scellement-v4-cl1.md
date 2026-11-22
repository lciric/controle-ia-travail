# Contre-lecture du programme de scellement de T0.8, version 4 (cl1)

- Pièce de classe B (instrument). Contre-lecteur : Sonnet 5.5, neuf (n'a rien écrit de la pièce).
- Lu : branche `t08/scellement-v4`, commit `4c9c9b1b3`, différentiel intégral contre son parent (six fichiers ajoutés, 763 lignes, aucune pièce de la version 3 modifiée) : `finaliser-t08-scellement-v4.py`, `essais-controle-gel-t08-v5.py`, sortie des essais, compagnons (tous vérifiés : OK).
- Code de T0.8 rejoué : tête `12eb328a6` de `origin/t08/chaine-de-lancement-v1` (contient `exiger_marqueurs` et `exiger_marqueurs_au_texte`), en arbre propre. Aucun appel payant, aucune clé, aucune machine.

## Verdict : conforme

Les cinq points de la consigne de la mère sont tenus. Trois remarques mineures, aucune bloquante ni majeure.

## Essais rejoués

45 essais conformes sur 45 (sortie identique à celle du développeur, hors noms de dossiers temporaires). Aucune entropie tirée. v3 intacte (R12).

## Les cinq points

1. **Sept clés exactement** : le fichier écrit a les sept clés attendues ; types lus : `ENTROPIE_T08` entier, `GO_T08` {id, plafond_usd = 120 entier}, `EMPREINTES_ENTREES_7B` cinq clés, `manifeste.json` = `RUN_7B.manifeste_sha256` (contrôlé par `exiger_marqueurs`). Compagnon `.sha256` écrit ; `python -m controle_ia.scellement verifier` : OK.
2. **Une seule source** : chaque valeur est lue par une forme fixe (`FORMES`, correspondance entière) dans la chaîne même écrite à la place du marqueur ; aucune seconde saisie. Les valeurs du fichier sont comparées à l'écrit par `controler_place`.
3. **Code de T0.8 rejoué** : `exiger_marqueurs` puis `exiger_marqueurs_au_texte` joués en processus à part, sur le fichier et sur une copie scellée du texte écrit ; tête de l'arbre = commit cité, arbre propre, sinon arrêt (essai « autre tête » conforme).
4. **Contrôle « à la place »** : éprouvé sur cas sain et sur huit artefacts du développeur ; refusé aussi dans mes mutations ci-dessous.
5. **Même commit S** : le programme n'écrit ni la configuration ni ne commit ; il rappelle la consigne dans son dernier message. Non vérifiable à ce stade (voir m-3).

## Mutations à moi (script `mut.py` hors dépôt, dossier temporaire, brouillon 15 épinglé par rapport adapté)

| Mutation | Issue |
| --- | --- |
| M1 : empreinte du manifeste de 7b citée une seconde fois en fin de texte (section non gelée) | **refusée** : « 1 occurrence(s) hors des remplissages des marqueurs, 0 déclarée(s) » |
| M3 : entropie donnée = 120 (valeur déjà citée huit fois dans le texte) | **refusée** : « 8 occurrence(s) hors des remplissages » |
| M2 : remplissage du GO déplacé de sa place à une annexe en fin de texte | **acceptée** (voir m-1) |
| M4 : commit du code cité dans la ligne de dépense (remplissage d'un autre marqueur) | **acceptée** (voir m-2) |

## Remarques

- **m-1 (mineure)** : « à la place de son marqueur » n'est vérifié par position que pour les remplissages en section gelée (par le contrôle du gel) et pour les trois remplis par le programme (par construction). Pour `GO_T08` (rempli au brouillon 11, section non gelée), `controler_place` n'exige qu'une occurrence du remplissage n'importe où ; un déplacement passe (M2). Atténuation : le brouillon d'entrée est épinglé par empreinte et par le rapport de vérification, donc un déplacement suppose une brèche de R2. Suggestion : exiger la ligne ou la section du remplissage du GO, ou le documenter comme limite.
- **m-2 (mineure)** : les plages des sept remplissages sont exclues du compte ; une valeur citée à l'intérieur du remplissage d'un autre marqueur (M4) n'est pas vue. Suggestion : compter chaque valeur hors de son propre remplissage seulement.
- **m-3 (mineure)** : rien n'impose par programme que texte, configuration et fichier des marqueurs entrent dans le même commit S ; c'est une consigne imprimée. À tenir par la mère ou par un contrôle de commit au scellement.
- Observation : `plafond_usd` n'est contrôlé ni à 120 ni dans le texte autrement que par la forme `[1-9][0-9]*` ; le code de T0.8 exige seulement > 0. Sans conséquence si la mère relit le fichier avant S.
