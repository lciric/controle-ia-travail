# Rapport de rédaction — préenregistrement hors échantillon, brouillon 3 — v3 (traitement de la contre-lecture 2)

Rédacteur : le sous-agent auteur des brouillons 1 et 2 (il n'a écrit aucune contre-lecture). Contre-lecture 2 traitée :
`brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/contre-lecture-2-preenregistrement-essaim-hors-echantillon-v1.md`,
sha256 `6d46750a8211e9f0a72a832eeba608ffeef261bbe56a7b37c2d2ec44b12379cd` (commit `50e47e63`), sur le brouillon 2
(sha256 `922733605a856bdc6f0f3f452363d1063e4c2de31666e7333edc956be6aa16e0`). Ce fichier est le fichier de traitement
cité par l'entrée de forme fixe de la contre-lecture 2 dans le brouillon 3 ; il ne cite donc pas l'empreinte du
brouillon 3 (rendue hors fichier). Grille inchangée (`dbe1caf1…8007`). Rien n'a tourné sur la grille ; aucun commit ;
aucune empreinte compagnon ; aucun fichier existant modifié (R12 : modules et essais v3 neufs).

## Décision de routine (à consigner dans `registres/decisions.md`)

Code corrigé par des modules **v3 neufs** plutôt qu'en place : `blocs_hors_echantillon_v3`, `lecture_hors_echantillon_v3`,
`run_essaim_hors_echantillon_v3` (la commande citée), essais `tests/test_simulation_essaim_hors_echantillon_v3.py`. Les
modules v2 restent tels qu'au commit `01208043` ; la lecture v3 importe `LecteurHOv2`, `annoter` et `decompte` de v2
sans les modifier.

## Traitement, une ligne par point

- **M1** acceptée : l'étape 0.d nomme les marqueurs sans les écrire (texte proposé) ; essai : exactement deux marqueurs, une fois chacun, `<<CONTRE_LECTURE_2>>` absent.
- **M2** acceptée, dans le code (variante complète) : `blocs_hors_echantillon_v3` départage uniformément les ex aequo de C_t et mesure la loi de référence iid aux mêmes (K, T) (`Q/<cfg>/reference-iid/maxima`, `P/reference-iid/maxima`) ; 1/T retiré comme référence ; textes remplacés ; chiffres du contre-lecteur (≈ 0,216 et 0,148) repris et déclarés en « Transparence » ; ses scripts copiés sans changement dans `recalculs-contre-lecture-2/` (mêmes empreintes que son rapport ; compagnons `.sha256` laissés à la session principale) ; essais : départage uniforme, références et tâches présentes.
- **M3** acceptée : phrase des 47 cellules remplacée (39 / 4 / 4) ; lectures de HP.5a et HP.5b récrites dans `lecture_hors_echantillon_v3.LIGNES_E` (textes proposés), table recopiée ; essai.
- **M4** acceptée : « 7 prédictions indépendantes » et phrase de portée v3 (rejouée comprise) ; essai.
- **M5** acceptée : 45 cellules garanties ≤ γ (21 au-dessus, 22 en dessous, 2 fourchettes), ≤ 4,5·10⁻⁴ ; les 20 « au plus » sans garantie ; décompte des sens vérifié par un essai.
- **M6** acceptée : écart à v1 déclaré dans la rangée « audit de symétrie déclenché ».
- **M7** acceptée : `test_garde_equivalence_lanceurs` (lanceurs v2 et v3, artefact) ; phrase des gardes récrite.
- **M8** acceptée : point 1 de la parade gèle les empreintes du brouillon, des rapports de contre-lecture et des fichiers de traitement ; point 3 dit la troncature (40 / 80 entrées) et la portée (arbre séparé seul), avec Rb.
- **M9** acceptée : interdiction écrite du lanceur v1 (et v2) sur ce texte. Garde testée côté v3 : une réplication n'est acceptée que d'un run principal lancé par le lanceur v3 (`exiger_principal_v3`). Le lanceur v1 ne peut pas être bloqué sans modifier son code (R12) : un essai documente le danger (v1 sur ce type de grille calcule tous les blocs puis lève `KeyError` sur `entre_x`, et son run consomme le run unique).
- **M10** acceptée : portée de `audit_declenche` écrite au texte et dans `lecture.md`.
- **M11** acceptée : provenance de la résolution = rapport de la contre-lecture 1 (section B) ; bornes de HP.4 en comptes (11 311 à 16 980 ; 6 491 à 12 095 sur 20 000).
- **M12** acceptée : `test_grille_v2_memes_cellules_et_sens_que_v1` (texte proposé) ; essai de recopie porté sur le brouillon 3 (`test_table_E_et_marqueurs_du_brouillon3`) ; parenthèse « cellules neuves » récrite.
- **M13** acceptée : statut « brouillon 3 », auteur, entrée de forme fixe de la contre-lecture 2 remplie, marqueur `<<CONTRE_LECTURE_3>>` et note de fin.
- **Ra** appliquée : `certifier_puissances_S` avant le manifeste (aucun tirage, rien d'écrit si l'erreur certifiée dépasse 10⁻⁶) ; valeurs versées dans `puissances-exactes-S.json` ; essai « avant tout tirage » (aucun dossier `runs/` créé). Coût ≈ 12 s.
- **Rb** appliquée : journal git augmenté de `git worktree list --porcelain` et `git fsck --unreachable --no-reflogs` ; essai.
- **Rc** appliquée : en réplication, `lire_partielle` (sans scores ni « trop beau », marquée `partielle`) ; seule la lecture finale fusionnée est annotée ; essai.
- **Rd** appliquée : HQ.5 fondée aussi à T = 20 (loi de référence e10x20 : 0,15530 à m = 3, 0,70437 à m = 5), recalculée par `bornes_synchro_v2` (0,155295 et 0,704371, erreurs ≤ 10⁻⁹), concordant avec la contre-lecture 2.
- **Re** appliquée : l'essai de réplication v3 compare les états et verdicts finaux à `fusionner` appliqué aux lectures v1 (hors HS.3 et HP.4).

## Fichiers neufs (sha256)

| Fichier | sha256 |
|---|---|
| `src/controle_ia/simulation_essaim/blocs_hors_echantillon_v3.py` | `0cd67658bfe3a12c42eb2ccf67cbe415a9874916fd7f72e33990db1d9a68207c` |
| `src/controle_ia/simulation_essaim/lecture_hors_echantillon_v3.py` | `3c94ed0b4ee592173b0726313d09769983115930d56b90bdc6e851a70c31e56e` |
| `src/controle_ia/simulation_essaim/run_essaim_hors_echantillon_v3.py` | `d33de14cc179b0d7d4d6377120e2e26d0e7f005630feb293bfb03a36865861e9` |
| `tests/test_simulation_essaim_hors_echantillon_v3.py` | `7d5fa16fe88cc5145daf9066ff369c4a1f34021219650616a7402858a0517604` |
| `recalculs-contre-lecture-2/` (14 fichiers copiés) | empreintes identiques à la table du rapport de la contre-lecture 2 |
