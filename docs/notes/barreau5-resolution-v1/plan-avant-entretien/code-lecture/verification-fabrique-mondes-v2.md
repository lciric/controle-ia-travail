# Vérification des corrections de la fabrique des mondes, du juge et du traducteur (barreau 5) — v2

**Verdict : « conforme ».** Les 21 couples sont appliqués à la lettre, l'erratum d'en-tête et la docstring du traducteur ne touchent aucun calcul, et mes huit mutations sont toutes tuées par les essais en vigueur. Deux retouches de texte sont conseillées, sans effet sur le verdict. La réserve de ma contre-lecture reste entière : aucun monde n'a passé la vraie garde.

- **Auteur** : le contre-lecteur de la fabrique, sous-agent de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`), Claude Fable 5.2 (`claude-fable-5-2`). Même mandat (`3c2ef07e…e745`), mêmes règles. 20 novembre 2026.
- **Pièce vérifiée** : `rapport-developpeur-fabrique-mondes-v2.md` (`dccc4217…4031`, empreinte vérifiée, lu en entier).
- Aucune donnée ; le programme de lecture n'est ni importé ni joué ; aucun outil refusé ; aucun commit.

## 1. Empreintes et égalités, par programme

Outil `outils-contre-lecture-fabrique-mondes-v1/verifier_corrections_v2.py` ; résultats `resultats-verification-corrections-v2.json`.

| pièce | empreinte lue | annoncée |
|---|---|---|
| fabrique `src/controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py` | `22560d9f4f814ef008ef050bdca626d4bcdcc5ffc139d8f88e8c7ce39c965dca` | égale |
| juge `…/juge_verite_plantee_v1.py` | `b35f0a7ff34c2a30b06f85760e7c04db16589a0b6010dd4d61ff66a9fb1d80f6` | égale |
| traducteur `…/traducteur_verite_plantee_v1.py` | `48fbfd88a004e7b6ef5f4df226c49e0e3bbed70f8e18a2a25baa0b5c9350d419` | égale |
| essais `tests/test_barreau5_familles_epreuve_verite_plantee_v1.py` | `826b3c0300f4c1e7ab9ce7c14ca9fa255e46bc9b4b5fdeeb46feb38eaddbbf79` | égale |

- **Fabrique.** L'état d'origine (`f41377ae…`) est retrouvé dans l'historique (commit `8cf0d3d13`) ; mes seize couples lui donnent `520b8215…9317`, comme annoncé. La fabrique en vigueur a le même arbre syntaxique que cet état, docstring de tête ôtée : aucune ligne de code ne diffère.
- **Juge.** `b35f0a7f…` est l'empreinte de ma copie corrigée (`resultats-verification-couples-v2.json`, `corrige_sha256`).
- **Traducteur.** Même arbre syntaxique que le mien (`d8355011…`), docstring ôtée ; mêmes octets après la docstring (sha256 du corps `56fbb4ba…`, celui que dit le développeur).

## 2. L'en-tête de la fabrique et la docstring du traducteur

Le diff (`outils-contre-lecture-fabrique-mondes-v1/diff-entete-fabrique-v2.txt`, 33 lignes) porte sur deux endroits : le dernier paragraphe de la docstring de tête, récrit selon m-3 et m-4, et le commentaire du paramètre `lignes_supplementaires`. Rien ne touche un calcul. Le texte neuf est juste. La docstring du traducteur ajoute sa provenance, le chemin d'appel et l'option `--accord` : juste aussi.

Retouche conseillée, de texte seul : la docstring du traducteur cite le programme de lecture à l'empreinte `d877d2de…`, celle de ma contre-lecture ; le programme en vigueur est `ed0999df…` (les phrases reconnues y sont toutes, vérifié dans ma contre-lecture, section 12).

## 3. Mes mutations, rejouées

Contre les essais en vigueur, dans une copie entière de `src/controle_ia`. Témoins : sans mutation, 155 passés, aucun sauté ; import cassé, échec. **Huit tuées sur huit** (trois sur huit avant).

| n° | tuée par |
|---|---|
| c1, V0 : bruit par jeton commun aux membres | `test_v0_bruits_par_jeton_independants` |
| c2, V0 : le sur-saboteur d'une autre loi | `test_v0_trois_membres_de_meme_loi` |
| c3, E2a : produit nul tenu pour positif | `test_verites_engagees` |
| c4, V7 : table hors de l'inventaire (récrite sur le nom neuf) | `test_v7_quatre_refus` (premier cas ; arrêt au premier échec, avant `test_v7_premier_cas_table_inventoriee`) |
| c5, V9 : saboteur sur ĝ | `test_ecart_qui_disparait_a_poussee_egale` |
| c6, V10 : D ou C exigée à 95 % | `test_juge_v10_niveau_de_d` |
| c7, V3 : D sans motif compte | `test_juge_v3_d_sans_motif_ne_compte_pas` |
| c8, V0 : « contraire » compte les « séparé » | `test_juge_bornes_au_plus` |

Les cinq essais demandés existent et tuent leurs cinq survivantes ; les onze essais repris passent.

## 4. La réserve du développeur : l'ordre des noms opaques

Rejouée : l'ordre renversé est tué dans le paquet entier (`test_table_et_registre_suivent_engagement_v1`) et survit dans un paquet minimal (149 passés, 6 sautés).

**C'est suffisant.** La seule référence de cet ordre est `engagement_v1` : un essai d'égalité avec lui est l'essai le plus fort qu'on puisse écrire, et la garde factice des essais, qui rederive les noms par la fonction de la fabrique elle-même, ne peut pas en tenir lieu. Dans le dépôt, l'essai joue (aucun sauté). Et le défaut ne peut pas donner une épreuve passée à tort : le programme refuserait toute table, les règles « au moins » et la règle de V0 manqueraient.

Retouche conseillée : cet essai et les deux autres essais d'égalité importent par `pytest.importorskip` ; si l'import cassait un jour, ils se sauteraient sans bruit. Un import ordinaire, ou une ligne de la routine qui exige « aucun sauté » pour ce fichier, ferme ce cas. Elle doit se faire avant le commit de `CODE-LECTURE-B5F`, ou pas du tout : les essais sont dans l'arbre gelé.

## 5. Ce qui reste

Inchangé depuis ma contre-lecture (`contre-lecture-fabrique-mondes-v1.md`, `e6ddb470…9fd`, sections 9 et 10) : l'essai de raccord sur la vraie garde avant le gel, le lieu où s'engage l'empreinte des vérités, l'entropie du premier passage ; la fabrique, le juge, le traducteur et leurs essais à commettre avant `CODE-LECTURE-B5F`.

Temporaires sous `/dev/shm/b5f-verification-fabrique-v2`, effacés par ce chemin.
