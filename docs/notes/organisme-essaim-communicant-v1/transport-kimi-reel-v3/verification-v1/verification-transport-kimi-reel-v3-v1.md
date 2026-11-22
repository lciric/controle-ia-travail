# Vérification du transport Kimi réel v3 — v1

- 22 novembre 2026, contre-lecteur de la v1 et de la v2.
- Aucun appel réel, aucune dépense ; seulement des serveurs locaux et une clé factice. Rien n'est écrit dans le dépôt.

## Verdict

**Conforme.** Rien n'est bloquant pour la fumée.

## Écarts entre la v2 et la v3 (`diff`)

- La seule ligne de code changée est la coupure : `non_vides > 2 * mt + 8`. La limite en octets, 12 × `max_tokens`, est inchangée.
- Ce qui change en plus, comme prévu :
  - les noms de version, les docstrings et les imports ;
  - `SHA_TRANSPORT` (`45c7a751…`, égal au fichier) ;
  - le nom du registre de la fumée, `fumee-kimi-v3` ;
  - le docstring du rejeu, qui déclare N19 et N19b ;
  - dans le faux serveur, la règle `un_caractere` ;
  - dans les épreuves, une assertion adaptée et 8 épreuves de la marge.
- Le plan de la fumée et ses arrêts ne changent pas.

## Rejeux

- **Épreuves : 120 réussies** (96,6 s).
- **Rejeu du contre-lecteur** : résultats identiques à ceux de la v2, hors ports et durées.
- **Mes artefacts N21 à N26** : identiques, sauf N22 (17 morceaux pour 16 jetons), maintenant accepté avec l'usage lu, comme voulu.

## Frontière (`frontiere-v3.json`)

| `max_tokens` | accepté | coupé |
|---|---|---|
| 1 | 10 morceaux | 11 morceaux |
| 16 | 40 morceaux | 41 morceaux |
| 2 000 | 4 008 morceaux | 4 009 morceaux |

- Deux champs dans un même delta comptent chacun pour un morceau.
- Limite en octets : 192 octets sont acceptés pour `max_tokens` = 16, 193 sont coupés.
