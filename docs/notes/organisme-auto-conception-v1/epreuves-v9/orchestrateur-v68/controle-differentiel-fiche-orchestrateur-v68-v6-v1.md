# Contrôle du différentiel v4 → v6 — fiche des quatre décisions sur l'orchestrateur v68 — v1

- Signé : contre-lecteur, modèle O. J'ai écrit la contre-lecture de la v1, la vérification de la v2 et les contrôles de la v3 et de la v4 (`controle-differentiel-fiche-orchestrateur-v68-v4-v1.md`, `e538fcb34df66299682a0648234644cd0b64fb04c5978ae3fd0ff22baf57e2f4`). Je n'ai écrit ni la v6, ni ses remplacements, ni son rapport, ni son mandat. Le contrôle de la v5 a été annulé avant toute écriture ; je n'ai rien écrit sur elle. Contrôle fait le 2026-11-20, vers 00:44Z à 00:55Z (`date -u` : 00:50:04Z).
- Lecture seule du dépôt : `git fetch origin lot/compte-organisme-v1` et `git fetch origin main`, tête de branche `b9ac61e4f`, arbre propre. Une seule exécution : l'outil contre-lu `scripts/remplacer_texte_exact_v1.py` (`391db990…`), lancé par son chemin, sortie dans mon bloc-notes. Aucun code en ligne passé à un interpréteur, aucune écriture dans le dépôt, aucune commande sur le dossier d'archives interdit. Les deux refus d'outil du contrôle de la v5 annulé étaient l'arrêt voulu par la session ; aucun refus pendant ce contrôle.

## Verdict

**Conforme après corrections** (trois remplacements à texte exact, D1 à D3, § 4). Le différentiel v4 → v6 est exactement l'application des trois remplacements. C2 est fidèle à mon texte, la ligne de version est juste et rien d'autre ne change. Sur le point soulevé par le rédacteur, je lui donne raison : « rapport joint » ne mène plus au bon rapport, et la fiche ne doit pas aller à Lazar avec deux renvois qui ouvrent la mauvaise pièce.

## 1. Pièces (empreintes recalculées, toutes égales à leur compagnon `.sha256`)

| pièce | empreinte |
|---|---|
| fiche v6 | `9c43d54aa1efd541d4a2db70835090ccd4bc8f2a783cfa41cddb9a53f126221e` |
| remplacements v4 → v6 (3) | `0a37a8370cc956ae9178009c7a0f562ba0ba6f8a0b8c61d64a76a2b4c5256fd3` |
| journal de l'outil | `8f0814bdb254744ed10648ff6327a8162e997072c46a4259ee83fdde06e48193` |
| différentiel v4 → v6 | `f9b03569760bcff1c41195e89dbfcc9bbad30426c7043214a78e54db5058c2bc` |
| rapport du rédacteur de la v6 | `8f32fa33c854118b09189bdb85f396e3d1139d3edf61218ec38fbad19edacb6c` |
| note de retrait de la v5 | `abf9d404fb53b2dfb0c8e6b9ec3ded7e524ff9f21f83274ac87f0e968bf10c44` |
| mandat de la v6 | `8dbcdf4712b5299f2b4e1e1daadb4ef3470cb67e750f12beaea7f75749a5e41f` |
| fiche v4 ; mon contrôle de la v4 | `7910e74b…` ; `e538fcb3…` |
| rapports des rédacteurs de la v1 et de la v2 | `49df651bdbb6615ae5ead6343741d8f2f3ad5d0aef9b69eaf82d0af140c2bfda` ; `29ccc99d…` |

## 2. Les cinq points

**(1) Le différentiel est l'application des remplacements : établi.**
- J'ai rejoué l'outil contre-lu sur la v4 du dépôt avec le fichier de remplacements versé. Il rend « 3 remplacement(s) » et une sortie d'empreinte `9c43d54a…`, égale à l'octet à la v6 versée.
- J'ai refait un `diff -u` entre la v4 et la v6 : son corps (sans les deux lignes d'en-tête) a la même empreinte que celui du différentiel versé (`48bc2130…`). Il n'a qu'un bloc, aux lignes 1 à 8.
- Le chemin absolu dans l'en-tête du différentiel et le `cd … &&` déclarés par le rédacteur sont des écarts de forme sans effet. Ils n'appellent aucune correction.

**(2) C2 est fidèle à mon texte : oui.** La parenthèse de la ligne des sources est, à l'octet, le texte B de C2 de mon contrôle de la v4 : la même chaîne se trouve une fois dans mon contrôle et une fois dans la v6.

**(3) La ligne de version est juste.**
- Ses empreintes sont justes : v4 `7910e74b…`, mon contrôle `e538fcb3…`, v5 retirée `c5694a88…` (empreinte reprise de la note de retrait et du mandat).
- Ses renvois sont justes : le différentiel joint existe, et `GO-2026-11-20-03` est bien sur `main`, où il dit : « la correction C2 […] est faite par [le modèle F], non par une recopie ; […] la v5 recopiée est mise de côté, et une v6 sera écrite […] puis contrôlée ».
- Son statut (« différentiel v4 → v6 non encore contrôlé ») est exact à l'heure de l'écriture. Elle dit bien que le reste de l'en-tête parle de la v4.
- Elle n'affirme rien de faux et ne contient aucun identifiant de modèle.

**(4) Rien d'autre ne change : oui.** Selon l'outil, le rejeu et le différentiel à un seul bloc, le verdict, les quatre décisions, les options, les confiances, les tableaux, les réserves et les sections de différentiel de fin de fiche sont égaux à l'octet à la v4.

**(5) La question GO-89 / GO-76 reste posée sans être tranchée : oui.** Le verdict, point 3, et la phrase de la décision 2 sont inchangés depuis la v3. Il n'y a aucun identifiant de modèle dans la v6 (recherche faite) et aucun chiffre neuf sans chemin ni empreinte. La fiche n'est prête pour Lazar qu'après D1 à D3.

## 3. Le point « rapport joint » : tranché, une correction est nécessaire

Il y a trois occurrences actives dans la v6 (la quatrième, dans le tableau du différentiel v2 → v3, est historique et juste en son temps) :

1. **En-tête : « sont au rapport joint ( ».** Le singulier ouvre sur trois rapports et sur l'absence d'un quatrième. Surtout, la v6 a désormais un rapport qui lui est joint, et ce rapport ne porte pas les sources. C'est en partie de mon fait : C2 a corrigé la parenthèse sans le mot qui la précède. **À corriger (D1).**
2. **Décision 2, enjeu : « ligne JUG-038, voir le rapport joint ».** Le repère est dans le rapport du rédacteur de la v1 (`49df651b…`) : ligne 52 dans la table des sources, et surtout § 2, constat 1, qui établit que la garde est à la ligne JUG-038 de l'inventaire et non dans le complément 3. Les rapports de la v2 et de la v3 ne le portent pas. **À corriger (D2).**
3. **Décision 2, option (a) : « rapport joint, § 3, point 6 ».** Ce texte vient de ma correction 10 de la v1, quand « le rapport joint » était celui de la v1. Le repère y est bien (§ 3, point 6, ligne 69 : « Si l'étage v5 sait restreindre l'entrée de l'expérimentateur à l'engagement seul […] : non vérifié »). Le § 3, point 6, du rapport de la v3 parle d'autre chose. Comme C2 met le rapport de la v3 en premier, un lecteur ouvrirait la mauvaise pièce. **À corriger (D3).**

Les trois propositions du rédacteur sont justes. Je les donne en texte exact, avec le chemin et l'empreinte du rapport de la v1 (règle R6), qu'il n'avait pas vérifiés.

## 4. Corrections demandées (texte exact ; chaque A copié de la v6 et présent une seule fois)

D1. **En-tête, ligne des sources.** Remplacer « sont au rapport joint (rapport du rédacteur de la v3, » par « sont aux rapports des rédacteurs (rapport du rédacteur de la v3, ».

D2. **Décision 2, enjeu.** Remplacer « ligne JUG-038, voir le rapport joint » par « ligne JUG-038, voir le rapport du rédacteur de la v1, `rapport-redacteur-fiche-orchestrateur-v68-v1.md`, `49df651bdbb6615ae5ead6343741d8f2f3ad5d0aef9b69eaf82d0af140c2bfda`, § 2, constat 1 ».

D3. **Décision 2, option (a).** Remplacer « rapport joint, § 3, point 6 » par « rapport du rédacteur de la v1, § 3, point 6 ».

Ces corrections sont à appliquer par un rédacteur du modèle F, avec l'outil contre-lu, dans une v7, avec une ligne de version de même forme que celle de la v6. Un contrôle de leur différentiel suffira.

## 5. Remarques sans correction

- Dans l'en-tête de la v4 gardé à l'octet, « Statut : […] v4 non revérifiée » et « Mandat : […] v4 » restent ; la ligne de version de la v6 prévient le lecteur. C'est acceptable.
- Le nom de fichier de la note d'interruption porte un nom de modèle. La fiche ne le cite pas et le désigne par son empreinte : c'est juste.
- Mes pièces de rejeu sont dans `controle-fiche-v4/rejeu-v6/` de mon bloc-notes, non versées.
