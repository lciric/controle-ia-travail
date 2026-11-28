# Validateur renforcé des préenregistrements — rapport v2, erratum 1

- **Objet** : rapport `docs/notes/validateur-prereg-renforce-v1/rapport-validateur-renforce-v2.md` (`f775c0f7573960475a50d8df1aeb64f68bcb338c190ad0c248232ea8722ada11`). Ce rapport n'est pas réécrit : cet erratum prime sur lui pour les points ci-dessous.
- **Cause** : décision de la mère du 28 novembre 2026 sur la question ouverte du § 2 (archives `.tar` et `.zip` suivies). Les archives suivies (`.tar`, `.zip`, `.gz`, `.tgz`, `.tar.gz`, `.7z`) sont traitées comme les fichiers gardés. Leurs octets ne sont ni ouverts ni hachés : seul leur compagnon `.sha256` compte. Une citation d'archive sans compagnon donne un avertissement. Raison : elles peuvent contenir des fichiers gardés, et la garde doit se lire sans exception.
- **Auteur** : Opus 5.5, pièce de classe B, à relire par le contre-lecteur avec la v2.

## Ce qui change

1. **§ 2, ligne « 9, archives `.tar` et `.zip` suivies »** : elle est remplacée par la ligne suivante. « 9, archives suivies : traitées comme les fichiers gardés, sur décision de la mère du 28 novembre 2026. Ni ouverture ni hachage, seul le compagnon compte. Une archive citée avec une empreinte qu'aucun compagnon ne porte donne un avertissement ; une empreinte d'archive citée sans chemin reste inconnue (problème), puisqu'elle n'est jamais hachée. »
2. **Module** `src/controle_ia/prereg_renforce_v2.py`, modifié sur place (la v2 n'était pas encore vérifiée) :
   - `MOTIFS_ARCHIVES` (`.tar`, `.zip`, `.gz`, `.tgz`, `.7z` ; `.tar.gz` est couvert par `.gz`) entre dans la garde de `est_garde`, sans tenir compte de la casse ; les compagnons `.sha256` restent exemptés ;
   - la fonction `est_archive` est ajoutée ;
   - une empreinte appariée à une archive qu'aucun compagnon ne porte donne un avertissement « empreinte d'archive non vérifiée », et non le problème des autres fichiers gardés ;
   - comme pour tout fichier gardé, les archives sont sautées par l'index des fichiers suivis : 152 archives suivies du dépôt réel, sur 263 fichiers sautés en tout. Leurs lignes ne sont pas comptées par (c), et leur historique git n'est pas lu.
3. **Essais** `tests/test_prereg_renforce_v2.py` : 167 essais au lieu de 158. Les nouveaux :
   - `test_est_garde_archives` (7 formes, dont `.tar.gz` et `.ZIP`, et leurs compagnons exemptés) ;
   - un essai sain, `test_archive_saine_par_compagnon_sans_ouverture` : sept archives citées avec leurs compagnons, aucun problème, aucun avertissement ;
   - un essai d'artefact, `test_artefact_archive_sans_compagnon` : un avertissement pour l'empreinte appariée, un refus de compter les lignes, un problème pour l'empreinte nue, et l'archive dans `gardes_sautes`.
   Les deux derniers vérifient par le crochet d'audit qu'aucune archive n'est ouverte, et le premier que le compagnon, lui, est lu. Contre-épreuve : retirer les archives de la garde fait échouer 9 essais ; retirer la branche d'avertissement en fait échouer 1.
   Résultat : `PYTHONPATH=src python -m pytest -q tests/test_prereg_renforce_v2.py tests/test_prereg*.py` donne **233 réussis** (le rapport disait 224).
4. **§ 3 (relevé)** : inchangé. Les deux brouillons donnent les mêmes problèmes et avertissements (12 et 10 problèmes) ; les comptes des 183 pièces scellées sont identiques, contrôle par contrôle.
5. **Épreuve par mutants du § 1** : elle porte sur le module avant cet erratum (57 mutants tués). Les deux mutants propres aux archives sont tués comme dit au point 3 ; je n'ai pas rejoué les 57 autres.
