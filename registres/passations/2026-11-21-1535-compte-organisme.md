# Passation — compte organisme — 2026-11-21 15:35Z

Session `session_01QPDgKejD5VCCQRiPVL6eb4`, branche `lot/compte-organisme-v1`. Suit `2026-11-20-2239-compte-organisme.md`. Demandée par la nouvelle mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`, message `vers-organisme/2026-11-21-1529-mere.md`). Le détail des faits du 21 est dans les trois états pour la mère (`registres/etat-compte-organisme-pour-la-mere-2026-11-21-1130-v1.md`, `…-1320-v2.md`, `…-1500-v3.md` — la v3 a été écrite vers 14:05Z malgré son nom) et dans `registres/essaim/vers-mere/2026-11-21-1413-organisme.md`.

## Ce qui tourne
**Rien.** Aucun agent en vol, aucun processus détaché. Relais de l'étage 2 (23274, 23457), geste 9 (30833), palier 0b essai 2 (16809) : absents (`stat` en échec) ; la machine a redémarré trois fois (vers 10:49Z, vers 13:30Z, vers 15:31Z). Aucune clé lue, aucune instance de calcul ouverte par cette session. Collisionneurs : retirés de ma liste par la mère (14:10Z).

## Fait le 21
- **Étage 2, ligne 3** (GO-2026-11-20-68, mot de Lazar 09:44Z) : relais de rang 2 lancés (manifeste `…/etage-2-portee-200-v1/relais-rang-2-v1/`, commit 61f74957) ; geste 9 fini à 10:18:12Z, `{"envois_partis": 1005, "cumul_compte_usd": "33.3702", "arret": null}` ; relais Claude à 2,710388 USD, 102 appels, 0 refus ; relais morts au redémarrage (complément 1 : `…/etage-2-portee-200-v1/execution-relance-v2-v1/`, c75c9094).
- **Palier 0b** : essai 2 tué par le redémarrage de 10:49Z (dossier `…/etapes-3-a-6-essai-2`, environ 3,6 Go, intact) ; essai 3 attend le complément de la mère.
- **Véhicule NA-1** : lots 4 et 5 versés (76186024), vérifiés **Conformes** (f47e4327).
- **Programme de vérification de la sortie des mondes v5** : versé (76186024), vérifié À corriger (22bd07f8), rapport v6 versé (f47e4327).
- **Vérité des témoins** (branche `verite-temoins/seuil-moniteurs-v1`) : v2 vérifiée Conforme (ff1aad8b).
- **Additif « matière première »** (GO-2026-11-21-41) : v1 (f47e4327) ; contre-lectures (edc8727b) ; v2 (664d6763) ; vérification des corrections **À corriger** (51e02c76 : fuite déplacée vers des pièces versées ; point délicat 10 à laisser ouvert). Annexe des objets de contrôle (`7406e537…`) gardée hors de cette branche ; versée pour récupération sur `prep/annexe-objets-controle-lecture-de-fin-v1`.
- **Référence hors course** : v1 (f47e4327) ; contre-lectures (edc8727b, À corriger et cassé) ; deux concepteurs de corrections interrompus par un classifieur (mandats v1 et v2, f7d7a626 ; brouillon récupéré 09e26462) ; options soumises à Lazar : `docs/notes/ideation-seuil-moniteurs-v1/reference-hors-course-v1/options-a-b-c-soumises-a-lazar-2026-11-21-v1.md`.
- **Contact externe** : brouillon de demande de crédits de recherche Google Cloud (b4efbcc7), à envoyer par Lazar s'il est éligible.

## Reste (dans l'ordre)
1. Additif « matière première » v3 : après la réponse de la mère sur le lieu des pièces qui révèlent les objets de contrôle (annexe v2 ou extension de la règle de lieu) ; valeur ouverte 13 pour le point délicat 10. Concepteur F, vérification par un autre modèle.
2. Référence hors course : suite décidée par la mère ou Lazar ; corrections 1 à 7 avant le scellement des critères (condition (a) de GO-2026-11-21-37).
3. Lots 6 et 10a du véhicule : après les errata de mandat de la mère.
4. Palier 0b essai 3 : après le complément de la mère.
5. Réponses de la mère en attente (son message de 14:10Z, point 3).

## Réserves
- Écarts de procédure des agents, dits dans leurs pièces : commandes de liste hors de leur dossier (contre-lecteur de l'additif, second concepteur de la référence, vérificateur), appels composés.
- Mes erreurs : nom « 1500 » de l'état v3 ; plus tôt, noms de modèles dans la vérification de la vérité (acceptés par la mère, R-4486).
- Pièces non versées faute de droit : relevé brut d'avant lancement du relais Claude et relevé du lot 4 au faux fournisseur (identifiants de modèles), dans le bloc-notes de la session.

## Prochaine action
Attendre la relance de la nouvelle mère ; ne rien lancer de neuf avant.
