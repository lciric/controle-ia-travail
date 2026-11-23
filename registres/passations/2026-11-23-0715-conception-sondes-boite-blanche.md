# Passation — session de conception des sondes de la boîte blanche (2026-11-23, 07:15Z)

Demande de la mère (reprise possible sur un autre compte, GO-2026-11-23-09). Aucune dépense, aucune instance, aucun registre commun modifié. Cette passation s'ajoute aux trois précédentes (`2026-11-22-1929-…`, `…-1936-…-additif-1`, `…-1942-…-additif-2`, `…-2100-…-additif-3`) ; elle ne les réécrit pas.

## Mandat
Consultée par Lazar (accords GO-2026-11-22-118 puis -126) : dire quelles sondes employer pour la boîte blanche après l'abandon des lectures génériques sur l'organisme à adaptateur unique. Exclue de la rédaction des critères de la première porte, de tout rôle aveugle sur les issues du test sur les adaptateurs jumeaux, de tout rôle côté attaque, de la contre-lecture de ses propres pièces. N'a ouvert ni le texte scellé du test sur les adaptateurs jumeaux, ni son code, ni ses sorties, ni le coffre, le bras d'attaque, le saboteur. Aucune dépense.

## Fait
- Réponse à Lazar : `demande-approfondie-et-reponse-v2.md` (509efeef…) et son additif 1 (84970a6b…) ; v1 gardée (dcc13b3e…). Portent des résultats.
- Consigne du développeur (60aef942…), erratum 1 (e9c8cde1…), erratum 2 (1e6ebdbe…).
- Texte des diagnostics préalables : brouillon 3 (e8dca00b…), **scellé par la mère** (`prereg/diagnostics-prealables-sondes-v1.md`, R-5056). Contre-lecture 7632bf9b…, vérification 74f21247….
- Note de conception v2, brouillon 2 (80d30420…) ; contre-lecture e42f5c57… ; vérification 5daed190… (« scellable après retouches mineures »).
- Devis de l'épreuve publique (397b887f…) et plan du calcul de puissance du banc (c7b808c0…), brouillons 1 non contre-lus.
- Bloc-notes versé : `docs/notes/conception-sondes-boite-blanche-fable-v1/bloc-notes-v1/` (voir son LISEZ-MOI : simulations sur données fabriquées, sorties brutes de la routine de reprise ; non versés avec leur raison : inventaires d'instances à jetons, copies déjà sur `main`, une extraction portant un identifiant de modèle, journaux internes des sous-agents).

## Reste (à faire par la session qui reprend, dans cet ordre)
1. **Table de correspondance des issues du test sur les adaptateurs jumeaux** (§ 7 de la note de conception, cinq conditions) : à écrire sur l'extrait servi par la mère (`docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/extrait-issues-et-phrases-gelees-b5f-v1.md`, empreinte `c228c773…`, branche `conducteur-b5f/lecture-v1`, commit `66ac7d78` ; ce seul fichier, vérifier l'empreinte avant lecture) ; issues annoncées : NI, C, S, D (E1, E2a, E2b), E, N, variantes sous huit familles, diagnostic toujours dit ; contre-lecture par un sous-agent d'un autre modèle ; scellement avant le verdict. C'est le plus pressé.
2. Note de conception, brouillon 3, avec les quatre retouches du rapport de vérification (anti-circularité « au sens accordé », annexe A écart 6, deuxième table du § 7 : identité « forte » ou « intermédiaire », classe « Contraire » : audit de symétrie si trop net).
3. Réponses aux questions Q1 à Q13 du développeur (dont Q12 : orientation du signe de l'interaction ; choix provisoires de la mère à confirmer ou corriger).
4. Contre-lecture du devis de l'épreuve publique (arithmétique § 5, pages du PDF, suppositions § 4) ; plan du banc à poids constants après le verdict et les diagnostics.

## Réserves
- Messages de la mère de 20:26Z à 20:36Z lus à 20:50Z ; travail fait entre-temps sans effet de dépense.
- Prédiction de l'étalon de transport changée entre brouillons 1 et 2, sans donnée, déclarée au texte.
- Pas de modification de `registres/etat.md` ; la suite de tests complète n'a pas été menée à terme (un échec connu, autre chantier).

## Branches et commits
Branche `prep/conception-sondes-boite-blanche-fable-v1`, demande de fusion 69 (brouillon). Tête avant cette passation : `78fa5c1a`. Fusion avec `main` : sans conflit au dernier contrôle.

## Tâches planifiées actives
`trig_01N4HEdRXUs6avMB9cQYsXgH` : reprise de la session le 2026-11-23 à 08:00Z (message à elle-même). Points de contrôle de la demande de fusion 69 : arrêtés.

## Instances actives
Aucune.
