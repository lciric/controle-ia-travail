# Vérification des corrections : mandats de l'ouvreur et du lecteur du verdict du barreau 5, v2 — v1

Par le contre-lecteur de la v1 (Claude Opus 5.5), sous-agent du conducteur (`session_013QMayjM1PQPWkLifMw9HDR`), le 22 novembre 2026. Une seule passe courte, sous le même cloisonnement que la contre-lecture. Rien lancé, rien commité.

**Verdict : à corriger, par un seul point.** Le point V-1 rend un pas du lecteur du verdict injouable ; un erratum 2 au mandat du juge suffit. Les dix-neuf constats de la contre-lecture sont tous portés. Le mandat de l'ouvreur v2 est conforme.

Empreintes vérifiées, égales aux compagnons :
- `mandat-ouvreur-b5f-v2.md` : `3c3f1092…3bc6d6` ;
- `mandat-juge-verdict-b5f-v2.md` : `17aafef2…b6ce6d` ;
- `mandat-juge-verdict-b5f-v2-erratum-1.md` : `0e1b6cbb…a587e`.

## Constats de la contre-lecture : sont-ils portés ?

**Ouvreur — tous portés.**
- **O-1** : porté. Les deux listes (a) et (b) sont écrites et scellées avant le sel (pas 8). Le contrôle de (b) se fait par ses noms ramenés à leur base. Les deux empreintes sont calculées en mémoire. La table n'est écrite que pour (a). Les trois issues sont écrites, et aucune troisième liste n'est essayée (pas 11). L'écart est déclaré au § 2 ; l'accord qui le fonde reste au nœud 3.
- **O-2** : porté (préambule, pas 4, 6, 12 et 15 : `PYTHON_B5F`, chemins absolus, `pip` et `pytest` de l'environnement).
- **O-3** : porté (pas 7 : `3dff7bed…` dit commit de la pièce ; empreinte entière de la pièce écrite ; nœud 2).
- **O-4** : porté (`<GELES>`, avec les exclusions mêmes de `CHEMINS_GELES`, aux pas 2, 4 et 14).
- **O-5** : porté (§ 2 et § 9 : `marche-b5f/lecture-v1`, ou une branche neuve qui en descend ; jamais `main`).
- **O-6** : porté (pas 5).
- **O-7** : porté (pas 6).
- **O-8** : porté (§ 2, point 1).
- **O-9** : porté (§ 4, pas 13, § 9).
- **O-10** : porté (pas 17 et 18 : `formation.json` et `ouvrir-v1.json` retenus jusqu'au verdict, aucune copie de `intensites.json`).
- **O-11** : porté (en-tête et § 3 : « 53 à 105 » ; § 1 : exclusions ajoutées).

**Lecteur du verdict — tous portés.**
- **J-1** : porté (en-tête, § 1, § 7, § 9, § 6 ; arrêt si le modèle n'est pas Opus 5.5).
- **J-2** : porté avec l'erratum 1, qui prime. Mon motif `[^;]*;[^.]*` ne rendait rien ; essayé ici, le motif de l'erratum, `grep -o "sonde en échec[^.]*\."`, rend exactement la phrase attendue. Le § 3, point 2, de la v2 garde l'ancien motif : l'erratum le remplace, c'est à lire ensemble.
- **J-3** : porté (pas 7). Les trois substitutions sont conformes à `phrases` et à `lire` : K de E3 ; familles d'apprentissage à jumeau et sur-saboteur ; nombre des π du diagnostic.
- **J-4** : porté (§ 4 et § 6).
- **J-5** : porté (§ 2, § 6, § 9).
- **J-6** : porté (pas 2).
- **J-7** : porté (§ 3, point 6, et pas 5).
- **J-8** : porté (§ 1).

## Ce que la v2 change d'autre

**D-7, ouvreur (branche des scores lue dans `SCORES-B5F`, nœud 9).** Exact. `ligne_scores` exige que le commit soit sur `origin/donnees/barreau5-familles-jumelles-v1-lecture`, et `ouvrir` ne vérifie que l'empreinte de l'inventaire. L'arrêt au pas 6 sans erratum de chaîne est la conduite sûre. Remarque : `_RUN_LECTURE` et le pas 6 attendent un `RUN_ID` en `-b5f-lecture`. Une relance qui changerait ce suffixe tomberait aussi au nœud 9, ce qui est cohérent.

**D-6, lecteur du verdict (fichiers retenus) : V-1, à corriger.**
- Ce que dit la v2 : au § 2, « tu vérifies leur empreinte, tu ne les ouvres pas » ; au pas 2, « Les empreintes des fichiers retenus (§ 2) égalent celles que le conducteur donne. Un écart : arrêt » ; au § 7, l'arrêt sur une empreinte de fichier retenu différente.
- Pourquoi c'est injouable :
  - (i) `formation.json` et `ouvrir-v1.json` restent dans `<BN>/retenus/` du bloc-notes de l'ouvreur, autre session et autre conteneur. Un chemin absolu n'y donne pas accès, et aucun transfert n'est prévu.
  - (ii) `intensites.json` vit dans l'arbre fermé de la lecture, sur une branche `donnees/*` que le § 3 du même mandat interdit d'ouvrir. Son empreinte est déjà couverte par l'inventaire, que cite `SCORES-B5F`.
  - (iii) La table D-6 dit qu'`intensites.json` « n'est versé qu'après `VERDICT-B5F` ». C'est inexact : il est déjà versé sur la branche des scores. Le mandat de l'ouvreur dit seulement qu'il n'en fait aucune copie.
- Correction par erratum 2 : aucun critère ne lit ces fichiers, et le juge n'en a pas besoin.
  - Le juge recopie dans le verdict les chemins et empreintes des deux fichiers retenus, tels que le conducteur les donne, sans les vérifier.
  - `intensites.json` sort de la liste du § 2.
  - Retirer la dernière phrase du pas 2 et « fichiers retenus » du § 7.

**Remarques sans correction exigée.**
- **R-1.** Au pas 17 de l'ouvreur, le résultat versé avant le verdict porte lui-même `g_issue`, donc l'issue. Retenir `ouvrir-v1.json` « parce qu'il porte l'issue » n'ajoute donc rien. C'est sans danger : nul autre que le lecteur du verdict n'ouvre le résultat. Le dire suffirait.
- **R-2.** Au pas 16 de l'ouvreur, l'appel `python -m controle_ia.scellement verifier` « même interpréteur » demande aussi `PYTHONPATH=<BN>/racine/src`. Le pas 8 l'écrit ; le pas 16, non.

## Lu

Les trois pièces v2. Pour vérifier : `lecture_v1.py` (`lire`, l. 1267 à 1307, et quelques recherches par motif) au commit `c76e7916`, et la ligne 226 du texte scellé par les deux motifs. Rien d'autre de neuf ; rien de fermé.
