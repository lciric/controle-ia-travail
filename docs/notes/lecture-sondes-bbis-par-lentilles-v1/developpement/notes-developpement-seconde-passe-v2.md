# Notes du développeur neuf de la seconde passe — note de rendu — v2

2026-11-21 (UTC). Mandat : `mandats/mandat-developpeur-seconde-passe-lentilles-v1.md` (`4a3cf535…`). Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md`
(`a2bbed7a…`), section « Code neuf ». La note v1 (`notes-developpement-seconde-passe-v1.md`) disait la mémoire de travail et le
découpage ; celle-ci dit ce qui est fait. Elle ne remplace pas la v1.

## 1. Ce qui est fait
Les sept sous-étapes de la note v1 sont closes, chacune par un commit poussé et une passation courte scellée :

| sous-étape | modules neufs (`src/controle_ia/lentilles_sondes_bbis/`) | essais (`tests/`) |
|---|---|---|
| 1 | `statistiques_v4` (statistique corrigée, règle de départage, comptes d'égalités) | `…_seconde_passe_statistiques_v1.py` |
| 2 | `constantes_v2`, `nos_lentilles_v1` (registre, fiche de rangement, condition de lecture, archive lue en flux) | `…_seconde_passe_nos_lentilles_v1.py` |
| 3 et 4 | `lecture_entree_v1` (lecture côté entrée par notre S), `comparaisons_lentilles_v1` | `…_seconde_passe_lecture_comparaisons_v1.py` |
| 5 | `reproduction_v1`, `audits_v2`, `phrases_v2` | `…_seconde_passe_phrases_reproduction_v1.py` |
| 6 | `montage_v2`, `lanceur_seconde_passe_v1` (horloge de 10 heures) | `…_seconde_passe_lanceur_v1.py` |
| 7 | — | table des essais, conformité, nœuds, empreintes, sortie du paquet |

Aucun fichier existant du dépôt n'est modifié : ajouts seuls (R12). Tout est joué sur jouets.

## 2. Ce qui a été lu
`CLAUDE.md` ; les deux mandats ; la passation et les notes du développeur de la première passe nommées par le mandat ; du texte
v2, au fil des sous-étapes : « Code neuf », « Vocabulaire », « Hypothèse », « Prédiction », « Entrées » (**sans** la liste « Jamais
ouverts », lignes 1320 à 1343, jamais lues), « Métrique », « Seuil », « Plan d'analyse », « Critères », « Liste d'arrêt », « Lignes
de registre », « Nœuds », les différences des brouillons 4 à 6 ; les modules de la première passe réemployés (`constantes_v1`,
`entrees_v3`, `montage_v1`, `lecture_v1`, `nuls_v1`, `statistiques_v1` à `v3`, `audits_v1`, `phrases_v1`, `lanceur_v7`) et leurs
jouets. **Ma mémoire de travail a été résumée une fois, pendant la sous-étape 6** : la continuité a tenu par les passations et le
brouillon des nœuds ; je ne peux plus attester, ligne à ligne, de ce qui a été lu en entier avant ce résumé — la note v1, § 4, et
les passations en gardent la trace. « Code neuf » a été relu en entier après le résumé, pour la note de conformité.
Jamais ouverts : `diag/`, `runs/`, `docs/verdicts/`, les
branches de données, de calcul et de verdict, aucune sortie, score, table ni verdict d'aucune passe, aucun fichier d'arrêt.

## 3. Expositions
Aucune exposition involontaire. Je n'ai vu d'intitulés des objets cloisonnés que ceux que portent les pièces que le mandat me
fait lire (le texte v2, les mandats, `CLAUDE.md`). Constat sans lecture : un dossier `__pycache__` daté de 16:00:15Z, antérieur
à mon départ, est présent à côté de la copie versée de `readout.py` sous `docs/sources/` ; je ne l'ai ni créé, ni ouvert, ni retiré.
Aucun refus d'outil à rendre. Rien n'a été lancé, loué ni dépensé ; aucun modèle, lentille ni corpus téléchargé ; aucune clé lue.

## 4. Environnement des essais (hors du dépôt, non versé)
Python 3.13 ; torch 2.14.1 (processeur seul), numpy 2.5.3, scipy 1.17.1, transformers 5.18.0, tokenizers 0.23.2, safetensors
0.8.0, huggingface_hub 1.33.0, pytest 9.1.1 — installés depuis l'index public des paquets dans un environnement du bloc-notes de
la session. L'essai opposable de la forme de l'archive vaut pour cette version de torch : à rejouer sur la machine du lancement.

## 5. Essais
Sortie du paquet entier : `sortie-essais-seconde-passe-v1.txt` (scellée ; commande et commit en tête). Non jouée : la suite
entière du dépôt (plus de deux heures). Essais des essais (altérations une à une sur une copie isolée) : voir la table, § 9.

## 6. Réserves
1. Les cibles du corpus des jetons gardés ne sont pas branchées (nœud N-dev-1) : le montage réel s'arrête, exprès.
2. Rien n'a tourné à taille réelle : ni temps, ni mémoire, ni espace mesurés pour la seconde passe.
3. Forme du descripteur de données d'une archive de plus de 4 Gio non éprouvée sur un vrai fichier.
4. Dix nœuds de lecture (N-dev-1 à N-dev-10) fixent des formes que le texte ne fixe pas : à contre-lire d'abord.
5. Les bouts en bout sont lents (environ dix minutes pour treize essais) ; ils partagent trois mondes miniatures par module.
6. Le nom d'un essai promet plus qu'il ne fait (`calcul_refuse_si_une_lentille_lue_n_a_pas_ete_montee_ou_si_le_montage_manque`
   n'éprouve que le montage manquant) ; deux essais ajoutés à côté éprouvent le reste. Vu par l'essai des essais.

## 7. Fichiers à donner au contre-lecteur
- le texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (« Code neuf », « Métrique », « Plan d'analyse », « Critères », « Liste d'arrêt ») ;
- le code : `constantes_v2.py`, `statistiques_v4.py`, `nos_lentilles_v1.py`, `lecture_entree_v1.py`, `comparaisons_lentilles_v1.py`,
  `reproduction_v1.py`, `audits_v2.py`, `phrases_v2.py`, `montage_v2.py`, `lanceur_seconde_passe_v1.py` ;
- les essais : les cinq fichiers `tests/test_lentilles_sondes_bbis_seconde_passe_*_v1.py` et les deux jouets
  `tests/lentilles_sondes_bbis_seconde_passe_jouets_v1.py`, `…_v2.py` ;
- dans ce dossier : `table-essais-seconde-passe-v1.md`, `conformite-code-au-texte-v2-scelle-v1.md`,
  `noeuds-et-precisions-seconde-passe-v1.md`, `empreintes-code-seconde-passe-v1.txt`, `sortie-essais-seconde-passe-v1.txt`,
  `outils/essai-forme-archive-torch-save-v1.py` et sa sortie, `outils/essai-des-essais-seconde-passe-v3.py` et les listes
  `outils/alterations-seconde-passe-*-v1.py`.
