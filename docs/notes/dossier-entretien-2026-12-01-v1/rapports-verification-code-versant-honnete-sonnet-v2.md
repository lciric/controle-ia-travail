# Rapports de Sonnet sur le code d'analyse v7 et sur la passe v2 du versant honnête — recopie — v2

2026-11-24, 18:31Z (`date -u`). Recopiés par la session « dossier de l'entretien », reprise (Opus 5.5), depuis le compte rendu par message du contre-lecteur (Claude Sonnet, sous-agent neuf, aveugle), qui n'a pas écrit ce rapport en fichier. Complète la v1 (`rapports-verification-code-versant-honnete-sonnet-v1.md`, a41e3e78…, versions 1 à 5) et la contre-lecture du code de la passe (`contre-lecture-code-passe-versant-honnete-sonnet-v1.md`, 57fb2daa…). Classe C. Recopie fidèle du fond.

## Code d'analyse v7 (src/controle_ia/versant_honnete_v7.py 58ca995f…, essais f0386b18…, commit ab094582) — corrections vérifiées

1. Le diff v6 → v7 ne contient que ce qui est annoncé : `existant` null ou NaN devient « absent » ; l'infini reste refusé ; l'arrêt « incomplets » est retiré ; le pont se calcule sur les écarts finis, avec la réserve « pont partiel ».
2. Scénarios rejoués : ligne absente, null ou NaN : pont partiel (639 sur 640) ; NaN écrit en JSON puis relu par `charger` : lu comme « absent », y compris pour la préparation v1 ; tous les existants absents : « non calculé », sans arrêt ; infini : arrêt.
3. Aucune garde du repassé n'est affaiblie : un repassé null, NaN ou absent arrête toujours ; il est gardé trois fois (ligne de lecture, `serie_depuis_lignes`, contrôle des comptes), si bien que deux mutations restent inoffensives par redondance, y compris l'ablation de deux gardes à la fois.
4. Mutations tuées : infini accepté, écarts non filtrés, réserve partielle absente, NaN existant non absent. 102 essais passent.

## Passe v2 (versant_honnete_passe_v2.py 1bef7200…), préparation v2 (4a1acf67…) et leurs essais — corrections vérifiées, un défaut

- 60 essais passent ; diff limité à l'annoncé. Mutations tuées : jeton de fin dans l'empan noté, contrôle négatif de la garde d'équivalence, tirage avec remise, source du juge, existants hors confirmation, garde de jetons absente ou aveugle, borne mémoire, NaN écrit par la préparation. Survivante : ablation de la garde explicite du doublon de tirage, équivalente tant que le tirage est sans remise ; aucun artefact ne l'éprouve directement (défaut faible).
- Défaut faible à moyen : la chaîne appelle encore la v6 (essais lignes 97, 378, 419 ; docstring ; bordereau `"lecteur": "…versant_honnete_v6.py"`). Correction : la v7 comme lecteur, et un essai de bout en bout par la v7 avec un existant null. Passe v3 en écriture.

Qui a lu quoi (contre-lecteur) : diff v6 → v7 du code d'analyse, ses essais par leurs résultats, diff v1 → v2 de la passe et de la préparation, noms des essais de la passe v2 ; aucune donnée du programme ; dépôt non modifié.
