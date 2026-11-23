# Devis — collisionneur sur la question neutre « éveil, allumage, anesthésie, transition de phase et signature mathématique » (v1)

- Écrit le 2026-11-23 vers 13:40Z par la session des collisionneurs (`session_016QhUrsc1rhjmmiLEmqPygF`). Classe A (devis) : à vérifier par un autre modèle avant la ligne d'engagement (condition de la mère).
- Accord : **GO-2026-11-23-19** (ligne renumérotée par la mère, ex-« -13 » des collisionneurs), plafond 40 USD, échéance le 30 novembre ; confirmé par Lazar à 08:43:33Z (événement `e4fb2d53-ab8d-4ab4-bbb2-098f658c4b28` : « go plafond 40 USD pour Carbon, Neon et le collisionneur »).
- Question servie : texte extrait par programme de `fable-max-v1/question-neutre-collisionneur-v1.md` (commit `26786e7b`, branche `claude/fable-max-conscience-emergence-v1`), copie `../test-neutralite-v1/texte-servi-question-neutre-v1.txt` (`aa2b7027…`), test de neutralité « neutre, 0,40 » (`../test-neutralite-v1/devinette-question-neutre-collisionneur-v1.md`, `f64ac2af…`). Si Fable porte les retouches du test, une v2 de la question remplacera la v1 et ce devis sera recalculé (l'écart de longueur est de quelques mots).
- Sortie brute du moteur : `devis-moteur-v8m-six-especes-question-neutre-v1-v1.txt`, produite par `PYTHONPATH=src python3 -B docs/notes/collisionneur-v9/collisionneur_v9_v8m.py devis --fable --opus --argon --astra --carbon --neon --faits Q --question Q` (moteur v8m, `collisionneur_v9_v8m.py`, empreinte vérifiée contre son compagnon, copié de la branche `runs/collisionneurs-reprise-v8d-v1`).

## Ce qui part

Étage III du moteur (trois tours : conception, critique croisée, réponse), six espèces, par la voie abonnement v6 (`voie_abonnement_v6.py`, contre-lue conforme ; script `vague_abonnement_v2.sh`) :
- **payantes, par l'interface** : Argon (`gemini-4-argon`), Carbon (`gemini-4-carbon`), Neon (`gemini-4-neon`), Astra (`gpt-6.2-astra`, seulement après la recharge du crédit d'OpenAI) ;
- **non facturées, par l'abonnement** : Fable 5.2 et Opus 5.5, en sessions filles sur kits (aucune clé d'Anthropic employée).
La « consultation de Carbon et Neon d'abord » demandée par Lazar est le premier tour de Carbon et Neon (réponses indépendantes à la question neutre) ; leurs réponses entrent ensuite dans la critique croisée avec les autres.

## Chiffres (moteur v8m, pire cas par cellule, en USD)

| tour | Argon | Astra | Carbon | Neon | payant |
|---|---|---|---|---|---|
| 1, conception | 1,67 | 0,48 | 2,33 | 1,50 | 5,98 |
| 2, critique croisée | 1,84 | 0,90 | 2,49 | 1,62 | 6,85 |
| 3, réponse | 1,91 | 1,07 | 2,56 | 1,67 | 7,21 |
| **total** | | | | | **20,04** |

- **Pire cas sans relance : 20,04 USD.** Consultation de Carbon et Neon seule (tour 1) : 3,83 USD.
- **Pire cas toutes relances** (deux relances par cellule de Google, une pour Astra, selon le moteur) : 57,67 USD, **au-dessus du plafond** ; le moteur vérifie le plafond de 40 USD avant chaque appel et s'arrête avant de le dépasser.
- **Attendu** (repère, non un engagement) : le dossier neutre précédent, même moteur, même étage, question trois fois plus courte, a coûté 12,50 USD réels, dont deux coupures de flux de Carbon comptées au pire. Avec une question de 1 094 mots au lieu de 294, l'entrée pèse peu devant la sortie ; je m'attends à 12 à 20 USD.
- Cellules Claude (Fable, Opus) : 0 USD par l'abonnement ; le moteur les chiffrerait à 12,94 USD par l'interface, voie qui n'est pas employée.

## Gardes
- Plafond `--plafond-usd 40 --ligne-usd 40` passé au moteur ; `GO_ID=GO-2026-11-23-19`.
- Pas de `--repli-lot` (refusé par la règle du plafond large pour Carbon, leçon du 22 novembre).
- Garde commune de Google `garde_google_v3` (réflexion explicite, plafond de sortie ≥ réflexion + 16 000 jetons) appelée par le moteur avant tout envoi.
- Panne technique (coupure de flux, quota, classifieur) : relance sur le même accord, consignée comme faux échec (GO-2026-11-22-77) ; refus d'un modèle (RECITATION, SAFETY) : ni rejoué ni contourné, nœud à Lazar.
- Astra : la cellule reste en attente tant que le crédit d'OpenAI n'est pas rechargé ; le dossier peut avancer sans elle seulement par décision de l'arbitre (`--accepter-absence`), qui revient à Lazar.

## Ligne d'engagement proposée (à envoyer à la mère après vérification)
« GO-2026-11-23-19 — collisionneur étage III, question neutre conscience et émergence v1 (aa2b7027…), moteur v8m, voie abonnement v6, six espèces ; pire cas 20,04 USD sans relance, plafond 40 USD tenu par le moteur ; attendu 12 à 20 USD. »
