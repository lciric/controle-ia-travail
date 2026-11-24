# Attestation sans secret pour le champ `AD-2` — vérification de la table des expositions contre la liste des exclus de l'ordre neuf (barreau 8, additif 1)

> **EXPLORATOIRE, NON OPPOSABLE (R-522) : attestation sans secret destinée au côté des moniteurs et à la session mère.** Conformément à la ligne 160 du brouillon 7 de l'additif 1, ce document ne comporte ni chemin ni empreinte de l'ordre neuf, aucun mécanisme du saboteur, aucun extrait de consigne privée et aucun contenu privé de l'ordre neuf.

- **Date et heure de vérification (temps universel coordonné)** : `2026-11-24T03:43:00Z`
- **Agent vérificateur** : sous-agent neuf habilité du **côté exposé** (`8f679a46f0f8fa95d2b414f233ddfa91`), inscrit avant lecture à la ligne `R-5200` de `registres/decisions.md` (sous `GO-2026-11-23-16`, `GO-2026-11-23-32` et `GO-2026-11-23-33`), exclu de tout rôle du côté des moniteurs ; n'a écrit ni l'ordre neuf, ni l'additif 1, ni aucun code ; n'a ouvert aucune sortie de course ni d'étalonnage (`essai/iib-explo-*`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/`).
- **Pièces de référence du côté des moniteurs vérifiées** :
  - Brouillon 7 de l'additif 1 (`scratch/redaction-additif-b8/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md`, empreinte `ab1d3b35f052aca400762042ec9c6bd23988ceb9249330e1718baa5092c71582`), lignes 150–161, 263–282 et 506–525 ;
  - Complétion de la ligne 516 dans `scratch/qui-a-lu-quoi-v22/valeurs-exactes-ad1-a-ad6.md` (lignes 26–34 et 79–91) ;
  - Registre « qui a lu quoi » version 22 scellé sur `main` (`registres/qui-a-lu-quoi-v22.md`, empreinte `7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4`).
- **Source contrôlée du côté exposé** : liste des exclus portée par l'ordre neuf scellé (en plusieurs pièces ; section désignée par la clé `exclus.section` de la pièce d'attestation de l'ordre `D-6`, incluant son renvoi à la liste des exclus de l'ordre de la première course), sans aucune divulgation de chemin, d'empreinte ni de contenu de l'ordre neuf dans ce document.

## Verdict `AD-2`

**CONFORME — AUCUN AGENT DE LA TABLE DES EXPOSITIONS NE FIGURE PARMI LES EXCLUS DE L'ORDRE NEUF.**

## Contrôle ligne par ligne (lignes 510 à 516 complétées)

| Ligne du brouillon 7 | Agent(s) nommé(s) dans la table des expositions | Présent dans la liste des exclus de l'ordre neuf |
|---|---|---|
| 510 | rédacteur de l'additif (brouillon 1, Fable 5.2, sous-agent neuf côté moniteurs) | **non** |
| 511 | auteur de la note de couverture (lecteur neuf, Opus 5.5, côté sondes, 21 nov. vers 18:16Z) | **non** |
| 512 | correcteurs des brouillons 2 et 3 (Opus 5.5) ; relecteur des corrections (Fable 5.2 par interface de programmation) | **non** |
| 513 | rédacteur des brouillons 5 et 6 (Fable 5.2, `session_016QhUrs5yLghTY6Gthp4k3P`) | **non** |
| 514 | contre-lecteur R2 du brouillon 6 et vérificateur final du brouillon 7 (Gemini 4 Carbon, `289f9a3a862f39f87ccb565b8aa65125`) | **non** |
| 515 | rédacteur du brouillon 7 (Gemini 4 Carbon, `a99cfcf7527baf9160bb77d7cb2dca01`) | **non** |
| 516 (complétée) | conductrice du côté des moniteurs (`session_013QMayjujdhnn94JyDTmgSs`) ; développeurs et contre-lecteurs initiaux des codes v1 à v5 (sous-agents de `session_013QMayjujdhnn94JyDTmgSs`, v21 ligne 281 ; nouveaux développeurs et contre-lecteurs non encore désignés au scellement) ; sessions mères (`session_013QMayjbmQUdDuDs2S3i3XD`, `session_016QhUrvi45g3jX5saFefVED`, session Antigravity `ff6e9350`) | **non** |

**Précision de gouvernance (hors liste d'exclus de l'ordre neuf)** : indépendamment de la liste d'exclus de l'ordre neuf (où aucune session mère ne figure), les sessions mères restent exclues par la règle `R13` et par leur rôle d'orchestration de tout rôle aval de lecteur des sondes, de juge ou d'auditeur, comme déjà consigné dans `registres/qui-a-lu-quoi-v22.md` (ligne 391). Les agents nommés en ligne 517 (lecteur des sondes, juge, auditeur) ne sont pas encore désignés au scellement et feront l'objet du contrôle `D-5` dans leur mandat.

## Texte de cellule prêt à l'emploi pour `AD-2` (strictement conforme à la ligne 160 : sans chemin ni empreinte de l'ordre neuf)

Une fois la présente attestation versée et scellée par la session mère (sous le chemin cible `<CHEMIN_ATTESTATION_AD2_SCELLEE>` et son empreinte `<SHA256_ATTESTATION_AD2>`), la cellule d'état de `AD-2` peut être remplie exactement ainsi :

```text
Table des expositions complétée ci-dessous ; attestation de la session mère (date -u : <HEURE_UTC_SCELLEMENT>) : vérification effectuée par sous-agent neuf habilité côté exposé (R-5200) contre la liste des exclus de l'ordre neuf (<CHEMIN_ATTESTATION_AD2_SCELLEE>, empreinte <SHA256_ATTESTATION_AD2>) — aucun agent nommé dans la table des expositions (lignes 510 à 516 complétées) ne figure parmi les exclus de l'ordre neuf.
```
