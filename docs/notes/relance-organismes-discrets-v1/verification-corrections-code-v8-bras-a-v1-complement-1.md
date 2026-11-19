# Vérification des corrections du code du bras A, version 8 — complément 1 : écarts au brouillon 29

**Ce complément ne change pas le verdict de la vérification** (`verification-corrections-code-v8-bras-a-v1.md`, `e8786ca7…`) : **engageable après corrections**. Cette vérification était déjà scellée quand l'information sur le brouillon 29 est arrivée. Elle n'est pas réécrite (R12) ; ce complément s'y ajoute.

Le code de la version 8 s'écarte du brouillon 29 sur cinq points, que la version 9 doit porter. Un sixième écart, que la note du brouillon 29 attribue au code, n'existe pas.

- **Vérificateur** : Claude Opus 5.5, le même que pour la vérification.
- **Textes** : brouillon 29 (`4446b21e…`), par recherche seulement ; sa note (`f77b1f60…`), parties 1, 2 et 4. Le code est celui du commit `dd7790b0`. La tête, `d169b4a8`, n'ajoute que le brouillon 29.
- **Essai** : `brouillon29_v8.py` et sa sortie, sous `/tmp/claude-0/-home-user-controle-ia-travail/b7727ccc-db8b-5b89-bce1-17602831b69d/scratchpad/contre-lecture-code-v8/`.
- **Heure** : 2026-11-19T19:05Z.

## 1. Où la version 8 diverge du brouillon 29 (note, partie 4)

| point de la partie 4 | brouillon 29 | code version 8 | écart |
|---|---|---|---|
| 1. égalité de la famille sur les fractions | égales comme fractions (0,050 et 0,05) | `analyse_bras_a_v8.py`, l. 1129-1134 : compare les nombres lus **et** les fractions exactes des deux écritures. Deux écritures de la même fraction sont acceptées : un zéro final (`0.049975012493753120` contre `0.04997501249375312`) passe (essai) | **aucun**. La note du rédacteur du code (« doit s'écrire comme ») décrit mal son code. L'essai « 0,050 et 0,05 » demandé par le brouillon 29 passerait déjà |
| 2. acte de reprise à cinq champs | `sha256_de_la_configuration`, vérifié au rejeu | quatre champs ; au rejeu, seuls le module et le rapport sont confrontés | **oui** : à porter |
| 3. fichier des grandeurs de l'étape (n) | `grandeurs-de-l-etape-n-bras-a.json`, cinq champs ; dès qu'il existe, plus de rejeu de l'étape (n) | absent ; une étape (n) aboutie peut être rappelée | **oui** : à porter |
| 4. constat à sept champs | `ligne_de_go` en entrée et en champ (`null` pour une première livraison) ; l'analyse le confronte à la ligne de l'acte | six champs ; le programme retrouve les lignes employables ; l'analyse ne confronte rien | **oui** : à porter |
| 5. constat malsain | aucun fichier, cause affichée, sortie en échec | même chose | aucun. Ma recommandation M-3 (le sceller sous un nom versionné, pour garder la trace) reste une proposition au texte, que le brouillon 29 n'a pas retenue. Le code est conforme au texte |
| 6. registre courant qui porte tout l'état figé | arrêt sinon | même chose | aucun |
| 7. valeurs fictives | configuration et lignes d'appui, **plus les lignes de révocation** du registre courant | ne regarde que les lignes d'accord de l'état figé et les lignes d'inscription | **oui, mineur** : ajouter les lignes de révocation aux lignes regardées, et l'essai « ligne fictive ailleurs, rien n'arrête » (qui passe déjà en v8) |
| 8. constat écrit à la main | garde de procédure, aucun essai qui prétende le refuser | aucune garde dans le code ; mon essai : un constat écrit à la main passe | aucun |
| 9. `piece_source` | garde ordinaire, sans événement d'arrêt ni fichier d'arrêt | **événement d'arrêt** (garde « forme d'une livraison », champ `piece_source`), donc fichier d'arrêt et issue du point 21 (essai) | **oui** : à porter. Je suis d'accord avec le brouillon 29 : une pièce qui n'est pas la bonne n'est pas une livraison refusée pour sa forme |
| 10 à 12. dossiers, ordre de l'étape (m), formes reconnues | confirmés | conformes | aucun |

## 2. Ce que le brouillon 29 change à ma vérification

- **Point 4 de la vérification (partie A du relevé)** : le brouillon 29 traite les cinq points comme des précisions, comme je le recommandais. Il porte A.1 en 6.9 et A.2 à A.5 dans les conventions, en 6.9 et en 8.4.
- **C-1 (révocation reconnue à son type écrit à la lettre)** : le brouillon 29 laisse les formes de « inscrite » et de « révocation » « à confirmer » (demande 29 au lecteur habilité). Mon défaut tient tant qu'elles ne sont pas fixées. Je maintiens la recommandation prudente : toute ligne entrée depuis l'état figé qui nomme la ligne employée rend le constat malsain. La version 9 doit la porter, ou le texte doit fixer une autre forme. M-2 (une ligne qui retire la configuration la fait dire « inscrite ») tient de même.
- **M-1 (valeur ajustée rapportée contraire à l'état)** : le brouillon 29 écrit que les valeurs ajustées rapportées restent des nombres à virgule « et ne disent aucun état ». C'est la règle, et c'est un choix défendable. L'affichage peut encore tromper un lecteur du rapport : je recommande toujours d'accoler la valeur exacte, ou la mention « arrondie ».
- **M-4 (constat non lié au moment de la lecture)** : le septième champ `ligne_de_go` lie le constat à la ligne employée, non au moment. Mon essai (rejeu sous une ligne révoquée après le constat, sur l'ancien constat sain) reste conforme à la ligne 997 du brouillon 28, et donc au brouillon 29 sur ce point s'il garde cette ligne : je ne l'ai pas vérifié.

## 3. Fichiers ouverts pour ce complément
- `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon29-note-v1.md`, lignes 26 à 90.
- `src/controle_ia/organismes_discrets/analyse_bras_a_v8.py`, lignes 1124 à 1138.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon29.md` : empreinte seulement.
- Rien d'interdit n'a été ouvert. Aucun appel réseau, rien committé.
