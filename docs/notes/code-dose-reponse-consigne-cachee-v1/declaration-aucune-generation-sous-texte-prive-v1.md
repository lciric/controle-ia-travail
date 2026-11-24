# Déclaration du développeur — aucune génération sous texte privé — v1

Pièce de classe C, exigée par le mandat (`mandat-developpeur-code-course-dose-reponse-v1.md`, b8d2f5fc…) et par la « Liste d'arrêt » du texte scellé `prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md` (2263c5c4…), première puce.

Le développeur du code de la course de dose–réponse de l'organisme à consigne cachée (session fille de la mère `session_01Qi7Gr3Ggccg85kjmP654WC`, modèle Opus 5.5, branche `code/dose-reponse-consigne-cachee-v1`) déclare, le 24 novembre 2026 :

1. Aucune action n'a été générée, par aucun modèle, sous un texte de la pièce jointe `consignes-privees-dose-reponse-consigne-cachee-v4.json` (7a5f633c…) ni sous un texte du fichier scellé du premier test `prereg/P3-consignes-v1.md` (a68468fe…), ni par cette session, ni par le sous-agent de contre-lecture qu'elle a lancé (consigne écrite de ne pas les ouvrir).
2. Les seules générations faites l'ont été par un modèle jouet à poids aléatoires (vocabulaire de caractères, quatre couches), sous des textes privés **factices** écrits pour les essais (`tests/factice_dose_reponse_v1.py`), qui ne demandent rien sur le champ `COST`. En mode jouet, la course refuse les empreintes des vrais textes avant toute lecture de fichier (essai `test_mode_jouet_refuse_les_vrais_textes`).
3. De la pièce jointe, seules ont été lues la structure (clés, champs de place, facteur, proportion et pas écrits, longueurs) et les empreintes des consignes ; aucun texte n'a été affiché. `prereg/P3-consignes-v1.md` n'a jamais été ouvert ni affiché : seule son empreinte a été vérifiée (compagnon et `sha256sum`).
4. Aucun score, aucun verdict, aucune sortie de course n'a été lu (liste `qui-a-lu-quoi-developpeur-code-dose-reponse-v1.md`).
