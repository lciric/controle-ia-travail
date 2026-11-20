# Vérification de la v2 du programme d'extraction du cas X6

Agent neuf, Claude Sonnet 5.5, 20 novembre 2026. Pièce de travail.

Empreintes vérifiées : programme v2 `004fc6b7...ddb`, essais v2 `0d721e7e...a127` (conformes à l'envoi de la mère).

## Verdict : conforme
- `diff` programme v1 / v2 : en-tête et version, `ident` ajouté à CLES_ID, décodage des noms avec `errors="replace"`. Rien d'autre.
- `diff` essais v1 / v2 : chemin du programme chargé, et quatre essais ajoutés (clé `ident`, `id` et `ident` en désaccord, borne de profondeur dépassée, borne juste tenue). Rien d'autre.
- Essais v2 rejoués : seize réussis.

## Passage unique (sans rejeu)
Code de sortie 0, issue « conforme ». Sortie `sortie-extraction-x6-v2.json`, sha256 `f5c7cc1ccd83bd8648d44c0c409e8a5fe79fbedca3af429f4ad44fb31e3659eb`, scellée. Journal : un fichier, 957 octets, sha256 `e2ba2a33...95df` (identique au passage v1).
Comptes par classe : `a_corriger` = 2 ; deux objets à `classe` ; source de l'identifiant : clé 2, parent 0 ; doublons : aucun. La sortie ne contient que des noms de clés, des comptes, des identifiants et les empreintes ; vérifié par filtrage des lignes d'identifiants sans les recopier.

Le premier passage (v1, code 4) reste versé tel quel.
