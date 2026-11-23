# Passation — rédacteur des devis de carte du bras A (Claude Opus 5.5) — 2026-11-23 0709Z

## Mandat
Écrire, à la place de Fable 5.2 (quota épuisé jusqu'au 29 novembre ; GO-2026-11-22-145), le devis de la course sur carte louée du bras A sur le texte v2 (mandat `docs/notes/relance-organismes-discrets-v1/mandat-redacteur-fable-devis-carte-v3.md`, `97165ddf75ddc67df4f41dfeddec6304c5dd749f747a0a6a5f7dd7d071db25ea`), puis, sur demande de la session du bras A confirmée par la session mère : le devis v4 (corrections de la contre-lecture), le devis de la carte des deux moniteurs à modèle de langue, la v5 (crochet de m4) et la v2 du devis des moniteurs. Cloisonnement du mandat tenu ; aucune dépense, aucune machine, aucun modèle extérieur.

## Fait (branche `relance-bras-a/devis-carte-v3`, demande de fusion en brouillon n° 79 vers `claude/pensive-bardeen-1fv7hw`)
| pièce (dossier `docs/notes/relance-organismes-discrets-v1/`) | empreinte | commit |
|---|---|---|
| `devis-bras-a-v3.md` | `be7ce98899ffdeda046aa7b65dfbf9e70a9a9fc15629130d4c3ffcbed06158e9` | `0206e87d` |
| `devis-bras-a-v4.md` | `f82514e9326df61f2fbd73f3eab644107f910aae620afe70b3d6ef9fcde7e0f3` | `643d4817` |
| `devis-bras-a-v5.md` | `40b999f825361ba94a45464921022ce74175733bd29b4fd98671269f7bb745f5` | `06416a69` |
| `devis-carte-moniteurs-bras-a-v1.md` | `6559f7886a599550090cde361fb7d5856631c27c3f008afb8e2bc3c46313fabc` | `76514065` |
| `devis-carte-moniteurs-bras-a-v2.md` | `c84f762247d39bdba38c70361ec1f8e877d3005882336b42a936f2c5fe037648` | `6f7394cd` |

Contre-lectures reçues : devis v3 (`d458ed7f…`, engageable après corrections), v4 (vérification `1d42bd6c…`, engageable), devis des moniteurs v1 (`c0e29904…`, engageable après corrections, cinq majeurs). Les v5 et moniteurs v2 sont jugés engageables par la session du bras A ; la vérification de la v2 des moniteurs n'est pas arrivée dans cette session.

Chiffres retenus : ligne 1 (128 épisodes de fabrication) ≈ 3,9 à 5,3 USD attendus, plafond 18 USD ; ligne 2 (projection, non demandée) ≈ 16,2 à 20,2 USD, plafond ≈ 47 à 50 sur débit mesuré, 85 sans ; carte des moniteurs ≈ 20,4 à 25,7 USD, plafonds de repli 55 + 55 = 110 USD.

## Versé dans cette passation
Dossier `docs/notes/relance-organismes-discrets-v1/devis-carte-redacteur-opus-pieces-de-travail-v1/` (programmes de calcul, scripts d'application des corrections, brouillons, essais, sorties, index), avec compagnons `.sha256`. Trois scripts d'application et le premier programme des moniteurs étaient perdus ou écrasés : reconstitués, et vérifiés par rejeu contre les empreintes déjà scellées (`faire-v5` → v5, `remplir-v4` → v4, `remplir-moniteurs-v1` → v1) ou contre la sortie consignée (programme moniteurs essai 1). Le bloc-notes ne contenait rien d'autre : pas de réponse de modèle, pas de secret (recherche faite ; deux faux positifs sur le mot « tokeniseur »). La copie de la contre-lecture du devis v3 dans le bloc-notes n'est pas versée : elle est déjà sur `claude/pensive-bardeen-1fv7hw`.

## Reste
- Le complément d'une page qui demandera la ligne 2 des devis de carte, à l'ouverture de l'étape (i), sur demande de la session du bras A (formule en 5.2 du devis v5 ; contenu en 5.5).
- Les décisions pour Lazar restent posées dans les devis (v5, section 9 ; moniteurs v2, section 7). Aucune ne m'a été répondue dans cette session.
- Vérification de la v2 du devis des moniteurs par le contre-lecteur (même contre-lecteur que la v1) : non reçue ici.

## Réserves
- Contre-lecteur et rédacteur du même modèle (Opus 5.5) : diversité de modèle non tenue, déclarée.
- Texte scellé non vu : les devis chiffrent le brouillon 55 (`cc55502a…`) ; à confirmer que le texte scellé n'en diffère que par l'entier racine, le titre et le statut.
- Lignes de GO citées sans lecture du registre des GO (cloisonnement).
- Débits des moniteurs supposés, aucun mesuré ; prix de la carte relevé le 18 novembre seulement.
- L'écart de tête de la v5 garde sa fin « , à préciser par la session mère », sans objet ; une v6 d'une ligne l'ôterait si on le veut.
- Routine de reprise raccourcie par le cloisonnement du mandat (ni état, ni arbre entier, ni instances, ni tests).

## Prochaine action
Attendre la demande de la session du bras A ; sinon rien. Aucune dépense à engager par cette session.

## Instances actives, tâches planifiées
Aucune instance de calcul. Aucune tâche planifiée active (la vérification de 23:11Z sur la demande n° 79 a été annulée). Abonnement aux événements de la demande de fusion n° 79 : actif.
