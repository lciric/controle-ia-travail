# Devis — collisionneur sur la question neutre « éveil, allumage, anesthésie, transition de phase et signature mathématique » (v2)

- Écrit le 2026-11-23 vers 13:45Z par la session des collisionneurs (`session_016QhUrsc1rhjmmiLEmqPygF`). Classe A. **Remplace la v1** (`devis-collisionneur-conscience-emergence-v1.md`, `057fabe5…`, qui reste), après la vérification d'un autre modèle (`verification-devis-opus-v1.md`, `91d5d1a6…`, verdict « à corriger », six défauts). Ce qui change est listé en fin de pièce. Vérification des corrections : par le même vérificateur.
- Accord : **GO-2026-11-23-19** (ligne renumérotée par la mère), plafond 40 USD, échéance le 30 novembre. Confirmation du plafond par Lazar : événement `e4fb2d53-ab8d-4ab4-bbb2-098f658c4b28` de cette session, 2026-11-23T08:43:33Z, « go plafond 40 USD pour Carbon, Neon et le collisionneur » ; **la confirmation reste à inscrire au registre par la mère** (la ligne dit encore « plafond à confirmer »).
- **Question servie : v2 de Fable**, `fable-max-v1/question-neutre-collisionneur-v2.md` (`961c828a…`, commit `211cbd80`), texte servi extrait par programme : `../test-neutralite-v1/texte-servi-question-neutre-v2.txt` (`db54b152…`). La v1 a été jugée neutre (0,40) ; la v2 n'y ajoute que les trois retouches du lecteur, contrôlées mot à mot par programme (`../test-neutralite-v1/devinette-question-neutre-collisionneur-v1.md`).
- Sortie brute du moteur sur la v2 : `devis-moteur-v8m-six-especes-question-neutre-v2-v1.txt` (`12396988…`), moteur v8m (`collisionneur_v9_v8m.py`, `420394f9…`, l'empreinte qu'exige la voie v6).

## Ce qui part, et la commande exacte

Étage III (conception, critique croisée, réponse), six espèces, voie abonnement v6 (`voie_abonnement_v6.py`), script `vague_abonnement_v2.sh` (`2f7c2ecb…`, compagnon écrit) :

```
bash docs/notes/collisionneur-v9/reprise-v8d-v1/vague_abonnement_v2.sh v8m DOSSIER docs/notes/conscience-emergence-v1/test-neutralite-v1/texte-servi-question-neutre-v2.txt GO-2026-11-23-19 max 40 --fable --opus --argon --astra --carbon --neon
```

avec `DOSSIER = runs/collisionneur-protocole-x-conscience-emergence-abonnement-v1-<horodatage>` ; **sans `--sortie-max`** (cette option porterait le pire cas sans relance à 38,04 USD et laisserait trop peu de marge aux kits Claude) ; sans `--repli-lot`. Effort passé à la voie : **`max`** (une seule valeur pour Fable et Opus ; Lazar a demandé « fable max » et « opus max »). Astra seulement après la recharge du crédit d'OpenAI ; tant qu'elle manque, la vague la laisse en attente ; avancer sans elle demande `--accepter-absence`, décision de Lazar.

- **Payantes, par l'interface** : Argon, Carbon, Neon, Astra.
- **Non facturées, par l'abonnement** (sessions filles sur kits, aucune clé d'Anthropic) : Fable 5.2, et **Opus 5.5, ajout déclaré sans dépense**. Lazar ne l'a pas nommé dans la liste du protocole X (« neon fable max argon carbon astra »), mais il a demandé « d'autres propositions à éprouver opus ? demande à opus max aussi ». Si Lazar le refuse, on retire `--opus`, sans effet sur la dépense.
- **Interprétation à déclarer** : la « consultation de Carbon et Neon d'abord » demandée par Lazar est lue comme le premier tour de Carbon et Neon, avec des réponses indépendantes à la question neutre, dont le point 1 demande des motifs plus spécifiques que « local gardé, global perdu ». Lazar peut la corriger en demandant une consultation à part ; elle coûterait de nouveau environ 3,83 USD au pire.

## Chiffres (moteur v8m, question v2, pire cas par cellule, en USD)

| tour | Argon | Astra | Carbon | Neon | payant |
|---|---|---|---|---|---|
| 1, conception | 1,67 | 0,48 | 2,33 | 1,50 | 5,98 |
| 2, critique croisée | 1,84 | 0,90 | 2,49 | 1,62 | 6,85 |
| 3, réponse | 1,91 | 1,07 | 2,56 | 1,68 | 7,22 |
| **total** | | | | | **20,05** |

(lu dans la sortie brute v2 ; l'écart d'un centime avec la v1, au tour 3 de Neon, vient des quelques mots ajoutés).

- **Pire cas sans relance : 20,05 USD.** Premier tour de Carbon et Neon : 3,83 USD.
- **Pire cas avec toutes les relances : 61,30 USD**, au-dessus du plafond. Le moteur prévoit deux relances par cellule de Google à plafonds égaux, et une pour Astra comptée à son plafond de relance de 32 000 jetons, soit 1,68, 2,10 et 2,27 USD selon le tour. Le moteur refuse tout envoi dont le pire cas dépasserait le plafond ou la ligne, par un arrêt nommé (code 4).
- **Ce qui se passe près du plafond** : les cellules Claude ne coûtent rien, mais le moteur les contrôle à leur pire cas nominal. Fable, au tour 3, compte 3,12 USD. Si les relances payantes dépassaient environ 37 USD avant le tour 3, la cellule de Fable serait refusée sans rien coûter. C'est à savoir, pas à corriger.
- **Attendu** (repère, pas un engagement) : 12 à 20 USD. Le dossier neutre précédent, même moteur, même étage et mêmes six espèces, a coûté 12,50 USD réels, dont deux coupures de flux de Carbon comptées au pire. Sa question était 3,7 fois plus courte (294 mots contre environ 1 090), mais c'est la sortie qui pèse le plus dans le coût.

## Gardes (inchangées)
Plafond et ligne à 40 USD avant chaque appel ; `GO_ID=GO-2026-11-23-19` ; garde commune de Google v3 ; panne technique, relance sur le même accord comme faux échec (GO-2026-11-22-77) ; refus d'un modèle, ni rejoué ni contourné, nœud à Lazar. Branches de kits `kits-abonnement/*` : **mot de Lazar requis pour ce compte avant tout kit poussé** ; sans lui, on retire `--fable --opus` et le dossier part avec les quatre espèces payantes.

## Ligne d'engagement proposée
« GO-2026-11-23-19 — collisionneur étage III, question neutre conscience et émergence v2 (db54b152…), moteur v8m, voie abonnement v6, effort max, sans sortie maximale ; espèces : Argon, Carbon, Neon, Astra (après recharge), Fable et Opus par l'abonnement (Opus : ajout sans dépense) ; premier tour de Carbon et Neon = consultation demandée ; pire cas 20,05 USD sans relance, 61,30 avec toutes les relances, plafond 40 USD tenu par le moteur ; attendu 12 à 20 USD. »

## Ce qui change depuis la v1 (défauts de la vérification)
1. Pire cas avec toutes les relances : 61,30 USD (relance d'Astra à son plafond de relance), au lieu de 57,67.
2. Commande exacte écrite, sans `--sortie-max`, effort `max`.
3. Opus déclaré comme ajout sans dépense ; effort `max` pour Fable et Opus.
4. Confirmation du plafond : référence de l'événement, inscription au registre demandée à la mère.
5. Lecture « consultation = premier tour » déclarée.
6. Compagnon de `vague_abonnement_v2.sh` écrit ; « 3,7 fois » au lieu de « trois fois ». En plus : question servie v2.
