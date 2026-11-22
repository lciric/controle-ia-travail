# Collisionneurs v8d, compte rendu 14 : devis du rejeu à part des cellules d'Argon (GO-2026-11-22-08)

22 novembre 2026, vers 05:20Z. Avant tout appel.

**Cellules** : les dix cellules d'Argon de la réserve de R-4750, chacune écrite par la v3 sans réflexion (essai OK, script `collisionneur-v9-v3`, aucun niveau). La cellule « but » (…-152615), hors des cinq dossiers de R-4750, n'est pas comprise.

**Méthode** : programme `docs/notes/collisionneur-v9/reprise-v8d-v1/rejeu_argon_v8d_v1.py` (classe B, contre-lu avant l'envoi). Il importe la v8d telle quelle (empreinte b7803838… contrôlée) et appelle son `executer_cellule` : garde v3 des réglages de Google, niveau « high », plafond 65 536, provision 16 384, comptage de l'entrée, plafond, relance identique puis dernier recours déclarés, zéro pensée = défaut au code 10. **Mêmes entrées** : l'invite d'origine, fichier scellé de l'essai OK, empreinte contrôlée contre le journal et le sceau. **Dossiers neufs** `<origine>-rejeu-argon-v8d-v1` ; aucun dossier fini n'est écrit. Plafond global de 20 USD sur la somme des dossiers neufs, tenu par la garde de la v8d à chaque envoi.

**Pire coût** (entrée estimée à 2,5 caractères par jeton, sortie 65 536 + 16 384 au prix de sortie) :

| dossier d'origine | cellule | essai d'origine | invite (car.) | pire sans relance | pire avec relances |
|---|---|---|---|---|---|
| collisionneur-percee-controle-securite-v1-20261121-114810 | E3-T1-conception-C | 1 | 6645 | 1.6490 | 4.9471 |
| collisionneur-percee-controle-securite-v1-20261121-114810 | E3-T2-critique-croisee-C | 1 | 128035 | 1.8433 | 5.5298 |
| collisionneur-derive-de-regime-v2-20261121-131044 | E3-T1-conception-C | 1 | 6795 | 1.6493 | 4.9478 |
| collisionneur-derive-de-regime-v2-20261121-131044 | E3-T2-critique-croisee-C | 1 | 106300 | 1.8085 | 5.4254 |
| collisionneur-methodes-maths-v1-20261121-093850 | E3-T1-conception-C | 1 | 6724 | 1.6492 | 4.9475 |
| collisionneur-anteriorite-pilier-v1-20261121-131029 | E3-T1-conception-C | 1 | 5344 | 1.6470 | 4.9409 |
| collisionneur-anteriorite-pilier-v1-20261121-131029 | E3-T2-critique-croisee-C | 1 | 96459 | 1.7927 | 5.3782 |
| collisionneur-anteriorite-pilier-v1-20261121-131029 | E3-T3-reponse-C | 1 | 117031 | 1.8256 | 5.4769 |
| collisionneur-question-de-recherche-fusionnee-v1-20261121-153256 | E3-T1-conception-C | 1 | 14910 | 1.6623 | 4.9868 |
| collisionneur-question-de-recherche-fusionnee-v1-20261121-153256 | E3-T2-critique-croisee-C | 1 | 111350 | 1.8166 | 5.4497 |

Total : 17.3433 USD au pire sans relance ; 52.0300 USD si chaque cellule épuisait ses relances (2 chez Argon : relance identique, puis dernier recours), refusé avant l'envoi par le plafond.
Argon : niveau 'high', plafond 65536, provision 16384, prix (4.0, 20.0)

Lecture : **17,34 USD au pire sans relance, sous le plafond de 20.** Les relances ne partent que si elles tiennent sous le plafond (refus avant l'envoi sinon). Attendu d'après les cellules d'Argon de cette nuit : 0,5 à 1 USD par cellule, soit 6 à 9 USD.

Règle d'arrêt : tout code non nul arrête le rejeu ; une coupure de flux : une reprise ; une seconde : arrêt et compte rendu.
