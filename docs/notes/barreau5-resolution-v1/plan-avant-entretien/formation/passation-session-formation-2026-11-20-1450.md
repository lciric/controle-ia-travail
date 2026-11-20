# Passation de la session de formation du barreau 5 — 2026-11-20 14:50 UTC

Session `session_01QPDgKjCQYmTHUEjN63ThC8`. Fait suite à `passation-session-formation-2026-11-20-1220.md`. Mère : `session_01QPDgKgejkqwnuaJHJ31Ydo`. Aucun score, aucune sortie de marche lue.

## Fait depuis 12:20Z
- **Mot de Lazar GO-2026-11-20-51** : fonds rétablis ; disques inventoriés puis détruits (option a) ; relance des six marches tombées.
- **Disques des six instances arrêtées.**
  - Inventaire par `ls` et `du` du loueur seulement : noms et tailles, rien lu. Versé, scellé et poussé sur chaque branche de sortie, sous `traces-b5f/disque-arrete/` (commits 60fd7cb6 pour 7, 9973a244 pour 5, 80db2de9 pour 4, cb2589e4 pour 1, 4478011e pour 2, 1d5b183b pour 3).
  - Premier essai de destruction refusé par le contrôle de permissions de la session (rien joué), puis destruction sur le « go » de Lazar dans la session, 13:20:40 à 13:21:28Z, `verifier-destruction` prouvée pour les six. Pièce : `destruction-disques-arretes-2026-11-20-v1.md` (b921ca9f…).
- **Additif et code des relances.**
  - Le code figé refusait plus de deux relances. Un agent Fable a écrit l'additif et le code ; deux contre-lecteurs Opus 5.5 neufs les ont contre-lus, puis ont vérifié les corrections.
  - Le code de la v2 introduisait une clé neuve au registre ; le contre-lecteur l'a jugé non conforme, parce que cette clé aurait fait refuser le registre par le code de lecture figé. La clé a été retirée : le commit du code des relances est cité dans la référence de la ligne de relance.
  - Additif v3 jugé scellable, scellé par la mère (R-4301, 20e862a3…).
  - Code des relances d116bf78 conforme ; poussé sur `formation-b5f/code-relance-v2` sur le mot de la mère.
  - Programme `controler_registre_candidat_v1.py` jugé utilisable.
  - Écarts accordés par Lazar : GO-2026-11-20-59 (2) et GO-2026-11-20-60 (2). « go 30 usd » vise une autre course (GO-2026-11-20-52).
  - Toutes les pièces sont dans `relance-six-instances-v1/`.
- **Registre propre et commit de course.**
  - Ligne `GO-RELANCE-FORMATION-B5F` inscrite par la mère à 14:40:40Z : « GO-2026-11-19-86 ; instances 1,2,3,4,5,7 ».
  - Commit de course 4bdf0d22e4246b4fe431bd8754e26fea4ccd037f, fils de d116bf78, sur `course/barreau5-formation-v1` en avance rapide.
  - Registre contrôlé par les deux codes chez moi : « ACCEPTÉ ».
- **Cumul commun avant la relance** : 18,59 USD (heures × prix), sous la réserve de 24 USD. Les lignes d'engagement des relances ont été envoyées à la mère avant chaque création (`lignes-engagement-relances-v2.md`).
- **Six relances créées** par `relance`, `GO_ID=GO-2026-11-19-86`, crédit ≥ 5 USD vérifié avant chacune :

| n | identifiant | offre | prix loueur USD/h | créée (UTC) | run |
|---|---|---|---|---|---|
| 1 | 61655405 | 61652949 | 1,042 | 14:43:01 | 20261120-144237-b5f-formation-1-x1 |
| 2 | 61655453 | 61652947 | 1,042 | 14:43:27 | 20261120-144312-b5f-formation-2-x1 |
| 3 | 61655547 | 61652952 | 1,042 | 14:44:00 | 20261120-144338-b5f-formation-3-x1 |
| 4 | 61655585 | 61652951 | 1,042 | 14:44:26 | 20261120-144407-b5f-formation-4-x1 |
| 5 | 61655633 | 29019285 | 1,170 | 14:44:42 | 20261120-144431-b5f-formation-5-x1 |
| 7 | 61655818 | 34475474 | 1,237 | 14:45:56 | 20261120-144552-b5f-formation-7-x1 |

- **Veille** `outils/veille_b5f_multi_x1.py`, au lanceur du code des relances, avec `RELANCE=1` : le plafond commun compte les relances, et le commun vaut 18,59 USD fixes plus les relances. Garde éprouvée avant le lancement : cas sain accepté, coupure et plafond refusés.

## Reste
- Veiller les six relances jusqu'à leur fin. À chaque fin : branche `…-instance-<n>-x1`, preuve, `detruire` du lanceur du code des relances, joueur par l'identifiant, `verifier-destruction` (témoin 60988826).
- Ligne `SORTIES-FORMATION-B5F`, puis sel, table et `ENGAGEMENT-B5F` : sur le mot de la mère.

## Réserves
- Seules les copies `-x1` des instances 1, 2, 3, 4, 5 et 7 seront lues. Leurs premières copies ne sont pas versées : disques détruits, écart accordé.
- Tout programme au code v1 reste valable pour le registre, puisqu'aucune clé neuve n'a été ajoutée. Mais `detruire` et `depense` des relances passent par le lanceur du commit de course (`arbre-course-x1`).

## Prochaine action
Relancer la veille si elle sort :

    cd $S && PAS_VEILLE_S=600 python3 -I outils/veille_b5f_multi_x1.py b5f/veille-conf-x1.json b5f/veille-x1-etat.json b5f/veille-x1.txt

Codes de sortie, comme à la passation de 10:55Z.

## Instances (14:50Z)
- Relances en marche : 61655405, 61655453, 61655547, 61655585, 61655633, 61655818.
- Non touchées : 58936096, 58936099, 58936100 (intouchables) et 60988826 (témoin).
- Détruites : 61552174 (instance 6) et les six premières copies.
