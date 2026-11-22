# Collisionneurs v8d, compte rendu 30 : versement d'urgence (quota à 99 %)

Écrit à 2026-11-22T06:57:49Z (`date -u`).

**Poussé** sur `runs/collisionneurs-reprise-v8d-v1` : tout ce qui était sur le disque (cinq dossiers repris, dix dossiers du rejeu d'Argon, coercition en cours, journaux des enchaîneurs, questions, devis, comptes rendus 1 à 29, erratum des heures, passation, code de l'essaim v1 à v3 et brouillons de la v4).

**Ce qui tourne** (détaché) :
- enchaîneur v2 (processus 2274) : coercition en cours (Python 5566), puis problématique, revendications ;
- enchaîneur v3 (3066) : générale, papiers A, B, C, thèse boîte blanche ;
- enchaîneur v4 (5185) : étau, tâches de sabotage ;
- **verseur v1 (10282, `docs/notes/collisionneur-v9/reprise-v8d-v1/verseur_v1.sh`)** : commit et poussée toutes les 5 minutes tant qu'un enchaîneur tourne, puis une dernière fois. Rien de neuf n'est lancé.

**Arrêté** : le développeur de l'essaim (v4 inachevée, pour épargner le quota) ; ses brouillons de v4 sont versés tels quels, non scellés, non vérifiés. Reste de la v4 : la borne du brouillon (compte rendu 29) et trois non-bloquants.

**Ce qui serait perdu si le conteneur disparaissait** : au plus les 5 dernières minutes d'écriture des courses (le verseur rattrape le reste) ; les courses elles-mêmes s'arrêteraient (la cellule en vol, déjà comptée au journal au pire, serait à reprendre par `--reprise`) ; les bloc-notes hors dépôt (scripts de mutations, sondes des contre-lecteurs) ; le `.venv`.

Dépense de la session hors protocoles X : 37,89 USD. Protocoles X : coercition à 6,23 USD à 06:47Z ; les suivants au journal de chaque dossier.
