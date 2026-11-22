# Papier C — note des différences entre les versions c2 et c3 du brouillon 7 de relance — v1

Date : 2026-11-22. Auteur : rédacteur du brouillon 7 de relance (session fille `session_013QMayk1rjSZrn2u9UAVhEp`).
Classe C.

- Source : version c2, `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c2.md`
  (`b375e6e7f0633c8433b9b5f095a7b95906e3930bd046d19c535e68e153c2c682`, 259 068 octets,
  2 419 lignes).
- Résultat : version c3, `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c3.md`
  (`1da47502c8e49e3eb1078cd3cb0b31f035240d3f422a501557f8a3e5b6baf00c`, 263 817 octets,
  2 468 lignes).
- Programme : `registres/papier-c/redaction-brouillon7-relance-v1/travail/construire_brouillon7_relance_c3_v1.py`
  (`0159e5d4aab1d4841d73d146d674317ab930afc3f88c161be847857d078120c2`) ; journal :
  `registres/papier-c/redaction-brouillon7-relance-v1/travail/construire_brouillon7_relance_c3_v1.journal.tsv`
  (`2ff9ca8c18dbeefb89ae188a82922a0d2de233440de6dfe7e02f619de49db417`).
- Méthode : 14 remplacements exacts (un fragment trouvé une fois, ou un bloc dont le début est trouvé une fois
  et la fin une fois après lui). Gardes de sortie : titres de section inchangés ; un seul « À REMPLIR » dans la
  section « Contre-lecture », aucun ajouté ni retiré ailleurs ; marqueurs de gabarit inchangés.
- Source : la vérification de la version c2 (rapport `52b9ce5f…`, remarques CW-01 à CW-03) ; table :
  `registres/papier-c/redaction-brouillon7-relance-v1/table-traitement-verification-c2-brouillon7-relance-v1.md`.

## 1. Ce qui ne change pas

Les énoncés, les prédictions, les marges, les seuils, la règle de HC2, les décisions D-1 à D-20, les précisions 1 à
40 (la précision 38 ne reçoit qu'une phrase sur la source de la lettre qu'elle suit : sa règle est inchangée),
l'audit de symétrie, les gardes 1 et 3 à 23.

## 2. Ce qui change dans une règle écrite

- Plan, section 3 : le cadre du bras « saboteur sans consigne » est écrit, le complément ne fixant que ce qui
  dépend du verdict de G0 (L-10) ; « Préalables » de l'étape 2 : le complément y est nommé (L-09).
- Garde 24 : « l'étape 2 ne s'ouvre pas ; nœud » (L-13) ; garde 2 : renvoi à la garde 24 (L-12).

## 3. Table des remplacements

| identifiant | lieu | remarque ou motif | forme | signes retirés | signes écrits |
|---|---|---|---|---|---|
| L-01 | titre | version neuve (R12) | fragment | 112 | 118 |
| L-02 | en-tête, « État en bref » | état après la vérification de la version c2 | fragment | 124 | 124 |
| L-03 | en-tête, « Nom (R12) » | version neuve (R12) | fragment | 93 | 187 |
| L-04 | en-tête, « Historique » | R12 : la version c2 entre dans l'historique | fragment | 120 | 451 |
| L-05 | en-tête, « Historique » | la version c1 est le point de départ de la version c2 | fragment | 71 | 68 |
| L-06 | en-tête, « Ce que change… » | paragraphe neuf : ce que change la version c3 | fragment | 102 | 1314 |
| L-07 | verrou 7 (contre-lecture) | vérification de la version c2 faite ; reste celle de la version c3 | fragment | 151 | 498 |
| L-08 | verrou 8 (accord de dépense du pilote) | devis en brouillon 3 | fragment | 95 | 95 |
| L-09 | Plan, section 3, « Préalables » de l'étape 2 | CW-02 | fragment | 79 | 262 |
| L-10 | Plan, section 3, « Bras « saboteur sans consigne » » | CW-03 : cadre retenu écrit ; CW-02 | bloc | 836 | 1958 |
| L-11 | Plan, section 8, précision 38, « Règle » | CW-01 : source de la lettre suivie | fragment | 164 | 548 |
| L-12 | liste d'arrêt 2 | CW-02 : renvoi à la garde 24 | fragment | 77 | 139 |
| L-13 | liste d'arrêt 24 | CW-02 : l'étape 2 ne s'ouvre pas | fragment | 48 | 127 |
| L-14 | section « Contre-lecture » | vérification de la version c2 consignée ; vérification de la version c3 à faire | fragment | 345 | 1169 |

Les empreintes de chaque fragment retiré et écrit sont au journal du programme.
