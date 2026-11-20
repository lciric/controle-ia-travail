# Vérification de la version 2 du verdict de la mesure « portée à 200 » de la ligne 3 — v1

Écrite le 2026-11-20 par le contre-lecteur neuf, le même que celui de `contre-lecture-verdict-portee-200-v1.md` (`bb0900abc376a5d804ddabb177ff6cd9c8d3cddcb148ac317699f1675be9230b`).

**Verdict : conforme, à sceller.**

## Ce qui a été comparé

Dossier `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/verdict-portee-200-v1/`.

| pièce | sha256 |
|---|---|
| `verdict-portee-200-ligne-3-v1.md` | `d27305c859d6c4ddcf6c2bd6a669a64f66c9cc69cb1d8b3f7e2f2a0fc39e0147` |
| `verdict-portee-200-ligne-3-v2.md` | `029287239e341e53755b2875aaefd7a75662a1e9e95b5dbe2e2bf6ab8d6fbaa9`, égale à son compagnon |

## Constats

1. La comparaison des deux versions par `diff` rend deux lignes changées, et elles seules : la ligne 1 (titre, « v1 » devenu « v2 ») et la ligne 60 (section 2, relecture 3).
2. À la ligne 60, le seul changement est la correction 1 de ma contre-lecture, portée mot pour mot : le texte « Neuf » est présent une fois dans la version 2 (`grep -c -F -e` : 1) ; l'ancre de l'« Ancien », « (d de 0,042 à 0,104) », n'y est plus (0). Le reste de la ligne est identique.
3. Rien d'autre ne change : ni la faute du banc, ni un compte, ni la puissance qui décide (701 répliques gagnées sur 2 000, soit 0,3505), ni l'issue B, ni la prédiction, ni ce que l'issue fait de l'étage 2, ni les écarts, ni les réserves, ni la table des pièces.

## Gestes

Quatre commandes simples, une par appel : `sha256sum` sur les deux versions, `diff` des deux versions, deux `grep -c -F -e` sur la version 2 ; lecture du compagnon de la version 2. Aucun programme lancé, aucune relance de la mesure, aucun commit, aucun réseau, aucune dépense.

Contre-lecteur neuf, modèle F.
