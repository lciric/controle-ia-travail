# Refus de crédit de Google et changement de clé refusé (24 novembre 2026, vers 21:55Z) — v1

- Classe C. Session des collisionneurs.
- **Panne.** À 21:48:12Z, au premier essai d'Argon au tour 3 des idées intéressantes, la clé que le moteur v8m lit par son nom (`GEMINI_API_KEY`) a rendu HTTP 402 « Your prepayment credits are depleted » (RESOURCE_EXHAUSTED). Le refus n'est pas compté (0,00 USD). Plus aucune cellule de Google ne peut partir par cette clé, dans aucun dossier. Faux échec, issue codée « jamais parti », reprise de droit sur les mêmes accords (GO-2026-11-22-77).
- **Consigne de la mère** (message reçu à 21:49:41Z, autonomie R-5322) : essayer une autre clé permise, dans les mêmes plafonds. Ce sont `GEMINI_API_KEY_2`, ou `GEMINI_API_KEY_FREE` pour Carbon et Neon (mot de Lazar, R-5294) ; jamais `GEMINI_API_KEY_3`.
- **Vérification sans coût faite** : la lecture de la fiche des modèles (`GET …/v1beta/models/<modèle>`, aucune génération) rend HTTP 200 pour les trois clés et les trois modèles (gemini-4-argon, gemini-4-carbon, gemini-4-neon). Elle prouve l'accès, pas le crédit.
- **Changement de clé refusé.** La relance des deux vagues avec `GEMINI_API_KEY` remplacée dans l'environnement par la valeur de `GEMINI_API_KEY_2` a été refusée par le classifieur du mode automatique de la session (« Unauthorized Access »), à 21:55Z.
  - Rien n'est parti.
  - Le refus n'est ni rejoué ni contourné : c'est un nœud porté à la mère et à Lazar.
  - Le moteur et la voie ne sont pas modifiés.
- **État des deux dossiers**, portes fermées côté Google :
  - idées intéressantes : tour 2 complet ; tour 3 en attente d'Argon, Carbon et Neon. La cellule Opus du tour 3 (session_016QhUrvMkCBbjUzQD6qyWA6) est en cours ; Fable attend le 28. Compteur : 14,63 USD sur 30 ;
  - conscience et émergence : tour 2 en attente de Neon, et de Fable jusqu'au 28. Compteur : 8,95 USD sur 40.
