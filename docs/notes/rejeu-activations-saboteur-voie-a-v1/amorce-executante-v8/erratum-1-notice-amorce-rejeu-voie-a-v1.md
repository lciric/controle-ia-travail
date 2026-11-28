# Erratum 1 à la notice de l'amorce du rejeu — v1

Pièce de travail (classe C), exécutante v8. Règle R12 : le code et les essais scellés en version 1 (`src/controle_ia/rejeu_activations_voie_a_v1.py`, ee4cca1c… ; `tests/test_rejeu_activations_voie_a_v1.py`, 070d1b01…) restent tels quels. Les corrections faites après ce scellement (accord GO-2026-11-24-13 ; préparation de chaque commande sans secret, sauf HF_TOKEN pour la seule préparation « modele ») sont versées sous un nom neuf :
- code : `src/controle_ia/rejeu_activations_voie_a_v2.py` (le script de démarrage lance cette version) ;
- essais : `tests/test_rejeu_activations_voie_a_v2.py` (55 essais, tous verts ; les essais de la version 1 restent verts sur la version 1).
Partout où la notice, la passation et le compte rendu de la phase 1 nomment le module pour le lancement, lire la version 2. Les contre-lectures de l'amorce (et leurs vérifications) portent sur le code devenu la version 2 ; la contre-lecture de l'ordre et sa vérification portent sur la version 2 (essais 54 puis 55).
