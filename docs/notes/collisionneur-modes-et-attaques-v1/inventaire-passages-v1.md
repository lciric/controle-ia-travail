# Inventaire des passages « modes de sabotage » et « attaques » (et dossiers Neon et Astra)

Écrit à 2026-11-22T19:11:08Z (`date -u`). Classe C. Session cloisonnée. Inventaire seul : noms, empreintes, statuts, dépense ; aucun texte ni nom de mode.

## Dossiers (tous versés au coffre `coffre/modes-tenus-a-l-ecart-collisionneur-v1`, commit 2bdc2087e)
| dossier | espèces | cellules valides | absences acceptées | dépense USD | archive sha256 | fichiers |
|---|---|---|---|---|---|---|
| epreuve-carbon-argon-20261122 | especes=['argon', 'carbon'], lettres={'A': {'espece': 'argon', 'id': 'gemini-4-argon'}, 'B': {'espece': 'carbon', 'id':  | 3 | aucune. | 1.79 | 26bd1a0efccba3df… | 28 |
| modes-sabotage-20261122 | especes=['argon', 'astra', 'carbon', 'fable51'], lettres={'A': {'espece': 'argon', 'id': 'gemini-4-argon'}, 'B': {'espec | 12 | aucune. | 5.17 | 9bd06f19762b533a… | 116 |
| attaques-20261122 | especes=['argon', 'astra', 'carbon', 'fable51'], lettres={'A': {'espece': 'argon', 'id': 'gemini-4-argon'}, 'B': {'espec | 9 | E3-T1-conception-D, E3-T2-critique-croisee-D, E3-T3-reponse-D. | 9.64 | 1eaf6e3c3bc325cb… | 86 |
| neon-modes-sabotage-20261122 | especes=['astra', 'neon'], lettres={'A': {'espece': 'astra', 'id': 'gpt-6.2-astra'}, 'B': {'espece': 'neon', 'id': 'gemi | 6 | aucune. | 2.67 | 68656bacd3a95494… | 44 |
| neon-attaques-20261122 | especes=['astra', 'neon'], lettres={'A': {'espece': 'astra', 'id': 'gpt-6.2-astra'}, 'B': {'espece': 'neon', 'id': 'gemi | 6 | aucune. | 2.62 | 2c7c5d2b65aadd68… | 44 |

## Dépense par clé
- GEMINI_API_KEY : 17,72 USD ; OPENAI_API_KEY_2 : 4,18 USD ; total 21,90 USD, sous les 48,13 de GO-2026-11-21-08 (cadre GO-2026-11-22-95 et -112). Fable 5.1 par l'abonnement : non facturé (coûts théoriques 1,74 ; 3,65 ; 3,86 ; plus 0,92 pour la session hors dossier).
- Envois interrompus comptés au pire : Argon, tour de conception, « attaques » (1,66) ; Carbon, tour de réponse, « attaques » (2,43). Chacun a été repris une fois au même texte et a tenu. Aucun resserrement de question (règle GO-2026-11-22-109 non déclenchée).

## Sessions filles de Fable 5.1 (xhigh)
- « modes » : conception (session_013QMaykuhC7mkSW576hysPj : limite de l'abonnement, jamais partie, archivée ; relance session_013QMayo8hpcdT4Hiau5j4NK : versée), critique (session_013QMayjhEKGk3fjjFQgA5pd, voie fichier : versée), réponse (session_013QMayn6rgVgBZDQThoAhQX, voie fichier : versée).
- « attaques » : conception (session_013QMayntZ2dqXBeCvSFGXVD) : classifieur de sûreté (2 arrêts), bascule sur un second modèle ; versée hors dossier, au coffre. Absence de Fable acceptée sur les trois tours (décision de la chaîne, option (a), mère, après le mot du devis v3 § 6 point 4).
- Branches de kits du coffre : coffre/modes-tenus-a-l-ecart-kits/modes-sabotage-E3-T2-critique-croisee-D-v1 (dbc050e7) et …-E3-T3-reponse-D-v1 (2bc5dce4).

## Trieur
- Session neuve session_013QMayng3CwUpxUA1bVMY13 (Opus 5.5, high), sur la branche du coffre ; mandat mandats-v1/mandat-trieur-v1.md (5d04435c…), au coffre.
