# Lot 11 du véhicule NA-1 — exécutant de la passe X — v3

Écrit le 2026-11-22 (`date -u` : 12:48:17Z) par la session de l'organisme.

- **Version.** La v3 remplace la v2 (`../lot-11-passe-x-v2/`, archivée sans changement). La vérification de la v2 a rendu « Conforme avec réserves », sans point bloquant (`../lot-11-passe-x-v2/verification-v1/`).
- **Changements, tous sur les mots de Lazar relayés par la mère :**
  - **Pièce v2 à dix-huit pièces** (`../passe-x-piece-fusionnee-v2/pieces/`, `13928f87…`) et ses trois morceaux de six pièces. La 18e pièce vient de GO-2026-11-22-57.
  - **Neon en neuvième proposeur**, sur GEMINI_API_KEY, au niveau de réflexion xhigh, le plus haut qu'il admette selon la garde v3 (GO-2026-11-22-33, accordé à 12:35Z).
  - **Deux formes**, écrites dans la configuration :
    - « sans découpe » : P_X = 102,85 ;
    - « découpe Google » : trois morceaux par espèce Google, P_X = 139,15. C'est un écart à X-2, à accorder.
  - **Envois de la garde de départ et de l'essai de réglages sans redirection** (réserve de la vérification v2).
- **Épreuve.**
  - 83 essais passent (`test-passe-x-na-v3-pytest.txt`).
  - 44 mutations sont toutes tuées, et le témoin T0 survit (`sortie-mutations-passe-x-na-v3.json`).
- **Lancement.** Configurations scellées : `lancement/configuration-passe-x-sans-decoupe-v2.json` et `lancement/configuration-passe-x-decoupe-google-v2.json`. Plan de la garde : `lancement/plan-garde-depart-passe-x-v2.json` (9 couples). Les deux contrôles à blanc sont conformes.
- **Réserves de la vérification v2, consignées :**
  - le crédit Google n'est prouvé que par l'accès ;
  - un coût réel au-delà de 6,05 en cours de tentative n'est pas coupé ;
  - le suffixe numérique du modèle servi reste large ;
  - un 400 pour crédit à l'essai de réglages se lit « aucun niveau admis ». Il refuse quand même le départ.
