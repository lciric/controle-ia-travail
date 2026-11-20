# Contrôle du verdict v3 de l'étage 1 de la ligne 3, sur son différentiel avec la v2 — v1

Contre-lecteur, modèle F, le même que celui de la contre-lecture (`a5e2b23b…`) et du contrôle de la v2 (`controle-verdict-etage-1-ligne-3-v1-v2-v1.md`, `090d8dd50c295129c78beb669bb66fee2a018f49f40aa8c13fe553c1698542df`). Écrit le 2026-11-20, mêmes en-tête et interdits que le mandat de la contre-lecture.

## Verdict du contrôle

**« Conforme ».** Aucune correction exigée.

## 1. Pièces vérifiées

Compagnons vérifiés par `env -C` et `sha256sum -c`, tous OK ; empreintes recalculées égales à celles du mot :

| pièce | sha256 |
|---|---|
| `verdict-etage-1-ligne-3-v3.md` | `1628b4d76d126c1cff9de803a063be0c5a5fc061bc530d5619fd088927d799f3` |
| `differentiel-verdict-v2-v3.diff` | `b24b1eeabbf384d2594404ecda9146b555b7e9e4b09af6dfdc3178b771ee8f40` |
| `lecture-p3-etage-1-v1.json` | `1c200a892096cf264a2fa57a8c6da8b2ca94b8fdf5b85e5d34a7a39fad4e0d43` |
| `comparaison-p3-contre-lecteur-v1.json` | `db951a51baa07497b55b6c78272d55ec486b08f3ae2c5e2fabab1a99eeeb3e4c` |
| `verdict-etage-1-ligne-3-v2.md`, gardée | `f9835cbc2d5b088e011049a2138a9b6d2d4f78d46fd90c757faf415237bb5745` |

## 2. Le différentiel est fidèle, et rien d'autre ne change au fond

J'ai refait le différentiel de la v2 à la v3 par `diff -u` : il est égal à celui de l'agent du verdict, ligne pour ligne, hors les deux lignes d'en-tête (chemins et heures). Relu en entier, il a trois morceaux, qui portent quatre changements :

1. le titre et le paragraphe « Version 3 » (tenue de version) ;
2. la puce P3 du § 5 ;
3. le point 7 du § 8 ;
4. la liste des pièces du § 9 (tenue de version).

Le mot de l'étage 1, la taille voulue, les tables, les puissances, les autres lectures descriptives et les autres prédictions sont inchangés.

## 3. La correction sur P3 est portée mot pour mot

La puce P3 de la v3 est le texte exact de la correction 1 de mon contrôle : la même chaîne, du premier au dernier mot, se trouve une fois dans le verdict v3 et une fois dans mon contrôle (recherche par programme de la chaîne entière).

## 4. Le § 8, point 7 (c), est juste

Il dit trois choses, toutes exactes :

- en version 2, P3 restait non lue pour une raison que les mesures démentent ;
- en version 3, elle est lue sous ses quatre lectures et ses deux sens, par un programme de l'agent du verdict ;
- la raison de la version 2 s'appuyait sur une phrase de ma contre-lecture, que mon contrôle a retirée.

L'agent du verdict y déclare en plus un manquement de sa part (ne pas avoir recalculé lui-même). C'est honnête et suffisant ; la faute première est la mienne, dite au § 4 de mon contrôle de la v2.

## 5. Les chiffres de P3 contre mon rejeu

J'ai lu en entier `lecture-p3-etage-1-v1.json` et `comparaison-p3-contre-lecteur-v1.json`, et je les ai recollés à mon `rejeu-predictions-contre-lecteur-v1.json` (`987c33668941e68341cc67302455b8efaff5d97c1a39e7526af0a7f9f3cbbb7c`).

- **41 champs, aucun écart** : c'est exact. La colonne « contre_lecteur » de la comparaison porte bien mes valeurs.
- Les valeurs de l'agent diffèrent des miennes au plus à la seizième décimale (par exemple 0,00918250000000001 contre 0,0091825) : ce sont deux ordres de calcul des mêmes moyennes, non un écart.

| lecture | clause 1, plus grand gain (168 cellules) | clause 2 : sans gain / avec gain (18 cellules) | clause 2, plus grand gain |
|---|---|---|---|
| C contre majorité stricte | 0,0150 | 13 / 5 | 0,0092 |
| P contre majorité stricte | 0,0153 | 12 / 6 | 0,0150 |
| C contre poids égaux | 0,0008 | 12 / 6 | 0,0028 |
| P contre poids égaux | 0,0004 | 12 / 6 | 0,0100 |

Les chiffres de la puce P3 en découlent : 0,0153 ; 12 ou 13 sans gain ; 5 ou 6 avec gain ; 0,0150 au plus ; aucun gain de 0,02. Les mots des deux sens (« réfutée » sous la convention déclarée, « non réfutée » sous l'autre) sont les mêmes sous les quatre lectures.

## 6. Limites

- Je n'ai pas lu `lire_p3_etage_1_v1.py` ni `comparer_p3_contre_lecteur_v1.py` : ils ne m'étaient pas donnés à contrôler. Je juge leurs sorties, égales à mon rejeu indépendant.
- Aucun refus de permission, de classifieur ni de garde. Interdits tenus : aucune commande de liste, une commande simple par appel, aucun code en ligne, aucune écriture dans le dépôt.

## 7. Pièces de ce contrôle (même dossier que la contre-lecture, avec compagnons)

`mon-differentiel-verdict-v2-v3.diff` ; cette pièce.

Contre-lecteur, modèle F.
