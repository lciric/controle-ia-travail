# Lot 11 du véhicule NA-1 — exécutant de la passe X — v4

Écrit le 2026-11-22 (`date -u` : 13:00:20Z) par la session de l'organisme.

- **Version.** La v4 remplace la v3 (`../lot-11-passe-x-v3/`, vérifiée « Conforme », archivée sans changement). Elle porte la forme de la réponse 36 de Fable (`main` : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-36/relecture-fable-api.md`, `4b92f753…`, B.3, B.4, C.3), décidée par la mère à 12:46Z. L'écart à X-2 est accordé.
- **Textes servis.** Ils se trouvent dans `../passe-x-textes-groupes-v1/textes/` et sont formés par `former_textes_groupes_passe_x_v1.py`.
  - Ce sont trois groupes thématiques de six pièces, plus six moitiés de trois pièces pour la relance. Chacun porte le préambule fixe, puis ses pièces sous « [Pièce k sur 18] ».
  - Les dix-huit corps sont contrôlés contre la pièce v2 (`13928f87…`). Zéro motif à la garde de motifs.
  - Composition, faite par l'intitulé des fichiers, sans lecture des corps :
    - G1 : pièces 1, 2, 3, 9, 15 et 18 ;
    - G2 : pièces 4, 5, 6, 7, 8 et 17 ;
    - G3 : pièces 10 à 14 et 16.
- **Déroulé.**
  1. Garde de départ, puis essai d'effort par modèle : ce sont les requêtes de contrôle.
  2. Le groupe 1 part pour les neuf modèles.
  3. La barrière laisse passer la suite s'il y a au plus deux modèles en défaut de réglage.
  4. Les groupes 2 et 3 partent ensuite.
- **Garde de coupure.** Elle tient les cinq contrôles de B.4, par programme, et n'affiche aucun texte.
  - Un défaut ouvre une seule relance par unité :
    - transport : la même requête ;
    - réflexion épuisée : un cran d'effort en moins ;
    - texte coupé ou couverture incomplète : le groupe scindé en deux moitiés.
  - Un second défaut classe l'unité « sans réponse ».
  - Le repli Opus 4.6, puis Sonnet 4.6, sur refus de classifieur reste en place.
- **Pire.** P_X = 199,65 USD, soit 33 tentatives à 6,05.
  - Sous-parts : Luc 90,75 ; GEMINI_API_KEY 66,55 ; OPENAI_API_KEY_2 24,20 ; KIMI_API_KEY 18,15.
  - Chaque tentative est réservée à 6,05, puis comptée à son coût réel. Les tentatives sont donc souvent plus nombreuses que 33, tant que les sous-parts tiennent.
- **Épreuve.**
  - 74 essais passent (`test-passe-x-na-v4-pytest.txt`), dont le banc de douze coupures plantées, toutes rejetées.
  - 57 mutations sont toutes tuées, et le témoin T0 survit (`sortie-mutations-passe-x-na-v4.json`).
- **Lancement.** Configuration scellée : `lancement/configuration-passe-x-groupes-v3.json`. Plan : `lancement/plan-garde-depart-passe-x-v3.json` (9 couples). Contrôle à blanc conforme.
- **Non employé, déclaré.** Le budget de tâche d'Anthropic, ni documenté dans mes pièces ni éprouvé, et le mode d'arrière-plan d'OpenAI.
