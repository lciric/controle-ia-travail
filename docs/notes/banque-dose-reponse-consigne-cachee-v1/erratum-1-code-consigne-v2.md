# Erratum 1 — module d'extraction v2 : déclaration du modèle des sous-agents — v1

Pièce de classe C (erratum d'une pièce de classe B), 2026-11-24. Fichier : `src/controle_ia/environnements/extraire_banque_dose_reponse_v2.py`, constante `MODELE_SOUS_AGENTS`, recopiée au manifeste du run.

La constante disait que les sous-agents étaient lancés « sans choix de modèle ». Depuis le mot de Lazar relayé par la mère (le modèle d'octobre est celui de cette session), le modèle est nommé explicitement à l'appel de chaque sous-agent, comme pour les diagnostics et l'essai de la consigne v2. La constante le dit désormais, et précise que l'effort n'est pas fixé à l'appel. Seul ce texte de déclaration change : aucune logique, aucune garde. Les 7 essais de la version 2 passent. La correction est faite avant l'ouverture du run d'extraction des 80 papiers.
