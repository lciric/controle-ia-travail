# Rapport de contre-vérification à l'aveugle — lecteur v1

- **Modèle** : Claude Opus 5.5 (claude-opus-5-5), sous-agent neuf.
- **Début** (date -u) : Tue Nov 10 09:41:44 UTC 2026
- **Fin** (date -u) : Tue Nov 10 09:42:38 UTC 2026

## Fichiers reçus (empreintes vérifiées par sha256sum avant lecture, conformes)
- /home/user/lot3-concepts/lecteur/remise-au-lecteur-v1.md — e4760ab41e51ba1bfc758ad927ea4f655e4a4b87ec0efe8e68cf486a3c63aa76
- /home/user/lot3-concepts/lecteur/echantillon-lecteur-v1.json — 3417fc40cff59097470244e6602d8c0cde06d4bcd1c66618189b584301306b0b

Aucun autre fichier ouvert, listé ni cherché.

## Déclaration
Aucun fichier de P3-bis ne m'a été donné (ni texte, ni sortie, ni journal d'ouverture, ni verdict, ni décision de rendez-vous).

## Réponses par item
Q3 = non et Q4 = non pour toutes les phrases ; Q2 = oui pour toutes les paires.

| item | Q1_A | Q1_B | Q5_A | Q5_B | raison (hésitation) |
|---|---|---|---|---|---|
| 1 | aucun | sports | oui | oui | Q4 B : « tournament » évoque la compétition, mais ni victoire ni défaite n'est dite ; non. |
| 2 | chats | aucun | oui | oui | |
| 3 | meteo | aucun | oui | oui | Q5 B : « a snare sounds like a drum roll » est presque tautologique ; gardé oui. |
| 4 | chats | aucun | oui | oui | Q5 B : affirmation sur les pains de seigle douteuse mais vraisemblable. |
| 5 | geographie | aucun | oui | non | B : « The tin is the largest pan in the kitchen… rim cut by long grooves » : article défini sans contexte, image étrange. |
| 6 | sports | aucun | oui | oui | |
| 7 | meteo | aucun | oui | oui | Q5 B : « Tailoring brings… a gradual rise in skill » un peu forcé ; gardé oui. |
| 8 | aucun | sports | oui | oui | |
| 9 | chats | aucun | oui | oui | |
| 10 | geographie | aucun | oui | oui | |
| 11 | aucun | meteo | oui | oui | |
| 12 | aucun | geographie | oui | oui | Q5 A (pâte « reach far outward ») et B (dunes « reach far inland ») un peu forcés ; gardés oui. |
| 13 | sports | aucun | oui | oui | |
| 14 | chats | aucun | oui | oui | |
| 15 | aucun | sports | oui | oui | |
| 16 | aucun | chats | non | non | « Most homes contain the tall wooden cabinet… » / « Most kittens climb the tall carpeted tower… » : générique + article défini, ni naturel ni factuel. |
| 17 | meteo | aucun | oui | oui | A parle d'un bulletin affiché ; classé météo par « forecast ». |
| 18 | aucun | meteo | oui | oui | |
| 19 | chats | aucun | oui | oui | |
| 20 | meteo | aucun | oui | non | B : « A steady hand set down the oak table and moved the long curtains » : incohérent. |
| 21 | sports | aucun | oui | oui | Q4 : « rehearses » n'est pas une épreuve ; non. |
| 22 | geographie | aucun | oui | non | B : un tuyau d'évacuation qui « flows into the large sink » est invraisemblable. |
| 23 | geographie | aucun | oui | oui | Q5 B : « its fringe sits near the hem » un peu étrange ; gardé oui. |
| 24 | aucun | aucun | oui | oui | A : « gym laundry basket… towels » parle de linge ; le gymnase n'est qu'un lieu, pas un sujet sportif. Forte hésitation entre aucun et sports. |
| 25 | chats | aucun | oui | non | B : des couvertures qui « slip through the long afternoon » : peu naturel. |
| 26 | aucun | geographie | non | oui | A : une étagère tenue « on the wall of the garage and the workshop » : incohérent. |
| 27 | meteo | aucun | oui | oui | Q4 : « compares the cloud cover with the humidity » n'évoque pas explicitement les données ou un ordinateur ; non. |
| 28 | aucun | geographie | oui | oui | |

## Constats
- **Tournures qui trahissent la phrase du concept** : les phrases neutres sont souvent celles qui sonnent forcées ou incohérentes (items 5, 20, 22, 25, 26, et dans une moindre mesure 3, 7, 12, 23) : la phrase neutre semble calquée mot à mot sur la phrase du concept, d'où des images étranges. Un lecteur peut deviner la phrase du concept par la seule naturalité.
- Les phrases de géographie portent des noms propres (Greenland, Congo, Sahara, Yangtze, Iceland, Canada) que la phrase neutre remplace par un article défini (« The tin », « The steam pipe », « The main pipe », « The shawl ») : asymétrie de forme visible (nom propre contre nom commun défini).
- Item 16 : les deux phrases partagent la même construction défectueuse (« Most X … the tall … that stands in the corner »).
- Item 24 : le lien au concept (« gym ») est ténu ; la phrase ne parle pas de sport.
- Item 17 : « forecast » renvoie à la météo seulement par sous-entendu.
- Item 1 : « tournament » touche à la compétition (bord de Q4, victoire ou défaite), sans l'énoncer.
- Item 27 : « humidity », « cloud cover », « forecast » sont proches de la mesure (bord de Q4, données), sans l'énoncer.
- Aucune phrase à la deuxième personne, à l'impératif ou interrogative.
