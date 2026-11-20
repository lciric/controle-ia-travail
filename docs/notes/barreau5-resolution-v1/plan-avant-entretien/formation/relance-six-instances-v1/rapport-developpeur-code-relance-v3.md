# Rapport du développeur, version 3 : code des relances corrigé après contre-lecture (barreau 5)

Écrit le 20 novembre 2026 par le rédacteur de l'additif 1 et développeur du code des relances (Claude Fable 5.2). Il répond aux deux contre-lectures (`contre-lecture-additif-v1.md`, `contre-lecture-code-v2.md`) et aux décisions de la session mère et de Lazar relayées avec elles. Le rapport de version 2 reste à côté, sans modification.

`$S` = `/tmp/claude-0/-home-user-controle-ia-travail/2e5ab823-f39e-5eb7-8014-a7e033a3a8e4/scratchpad`.

## 1. Les pièces

| pièce | chemin | repère |
|---|---|---|
| additif 1, projet v2 | `$S/relance/additif-1-relance-six-instances-v2.md` | empreinte : voir le message de remise (calculée après la dernière écriture) |
| code des relances, corrigé | `$S/relance/code`, branche locale `formation-b5f/code-relance-v2` | commit `d116bf78bb2084b2d4f406535a6c6f0a23179efe`, fils de `a74dfb4988dbe8024d5923f95999538b248d166c` ; jamais poussé |
| différentiel depuis le code des premières marches | `$S/relance/diff-code-relance-v3-depuis-le-code-v1.patch` | sha256 `1db0fe39b7754831d0112b65a95450b33ba1325a28a4cc1bfc0eac0d327cf36e` |
| différentiel depuis `a74dfb49…` | `$S/relance/diff-code-relance-v3-depuis-a74dfb49.patch` | sha256 `e8dca4efbd98ee838c53723bd40f11bd85493ac57e3674bae643e72caa044400` |
| épreuve par retrait | `$S/relance/epreuve-par-retrait-v3-sortie.txt` | 15 échecs et 1 erreur, 118 passés, sur le code v1 |
| épreuve par mutation | `$S/relance/epreuve-par-mutation-v3-sortie.txt` ; programme `$S/relance/mutations_v3.py` | 23 tuées sur 23 |
| essai du registre final | `$S/relance/essai-registre-final-v3-sortie.txt` ; programme `$S/relance/essai_registre_final_v3.py` | accepté par le code de lecture figé et par le code des relances |

Empreintes au commit `d116bf78…` (16 premiers signes) : `formation_v1.py` 1f3e67c31ae17a0c ; `lancer_b5f_formation_v1.sh` 465ef9b2447ea603 ; `amorce_b5f_formation_v1.sh` 6e413a48077b34bc ; `tests/test_barreau5_familles_formation_relance_v2.py` 321734eab5258a47 ; `engagement_v1.py` 565d4e51eccd8256 (inchangé).

Vérifié par `git diff --quiet` entre `31fca83b…` et `d116bf78…` : `registres/`, `prereg/`, `docs/` et `engagement_v1.py` sont identiques. Le blob de `engagement_v1.py` est `7d2b56368d5e1cc130b6bc2ad906cfd314065298`, le même qu'au commit de `CODE-LECTURE-B5F` (`c76e7916…`).

## 2. Table « couple → correction »

### Contre-lecture du code

| couple | gravité | correction faite |
|---|---|---|
| 1. La clé neuve casse le code de lecture figé | bloquant | Clé `CODE-RELANCE-FORMATION-B5F` retirée. `engagement_v1.py` rendu au fichier v1, à l'octet. Le commit du code des relances se lit dans la colonne de référence de `GO-RELANCE-FORMATION-B5F` : « `code des relances commit <40 signes>` », entre « ; » ou aux bords, une et une seule fois (les mots « code des relances » ne paraissent qu'une fois dans la référence), et différent du commit de `CODE-FORMATION-B5F`. Le contenu de la ligne ne change pas. Les messages nomment la ligne « GO-RELANCE-FORMATION-B5F (code des relances) ». |
| 2. Registre du commit de course, arbre de la lecture | important | Essais sur le registre à cinq lignes inscrites plus la ligne de relance ; essai du registre réel de la branche principale (section 6). L'additif dit : registre du commit de course égal à celui de la branche principale, à l'octet ; le code des relances n'entre pas dans l'arbre d'où part la lecture. |
| 3. Le code laisse citer l'instance 6 | mineur | `INSTANCES_TOMBEES = (1, 2, 3, 4, 5, 7)` ; une ligne qui cite une autre instance est refusée (« instance non tombée citée »). |
| 4. Filiation non vérifiée | mineur | `exiger_filiation_du_code_des_relances` : le commit de `CODE-FORMATION-B5F` est un ancêtre du code des relances (`git merge-base --is-ancestor`) ; commit absent, autre lignée ou ordre inversé : refus. Appelée à la commande de création et, en plus de ce que demandait le couple, sur l'instance avant la marche. L'aide d'essai du lanceur prend par défaut un commit v2 distinct, fils du code v1. |
| 5. Noms « v1 » gardés (R12) | mineur | Noms gardés ; exception écrite dans l'additif, C5 ; à consigner par la session mère au registre des décisions. |
| 6. Plancher d'essais de l'amorce | mineur | Remesuré : `MIN_ESSAIS=244`, avec son commentaire. |

### Contre-lecture de l'additif

| couple | gravité | correction faite dans l'additif v2 |
|---|---|---|
| 1. Premières copies non versées | bloquant | Section 1 (disques inventoriés par `ls` et `du`, détruits le 20 novembre entre 13:20Z et 13:21Z, inventaires sous `traces-b5f/disque-arrete/`), point C8 neuf, section 3 corrigée. |
| 2. La section 6 faisait du code lui-même un nœud | bloquant | C5 nomme les suites (essais, plancher de l'amorce, commentaires) ; section 6 : « autre que ceux de la section 2 et de leurs suites nommées en C5 ». |
| 3. Réserve de la relecture, répétition | important | Seuil de 24 dollars : 200 − 147 − 21 − 8, coupures du devis scellé `dc886195…`, section 4, données par la session mère ; répétition générale et volume de stockage interdits tant qu'ils pourraient prendre la part des relances. Les 45,98 dollars et le chiffre non référencé de 18,5 dollars sont retirés. |
| 4. Ce qui est imputé à Lazar ; « go 30 usd » | important | En-tête : « tel que le consigne la session mère » ; « go 30 usd » est le plafond d'une autre course (`GO-2026-11-20-52`) et ne borne rien de la formation. |
| 5. La ligne avant la première création | important | C7, section 3 et section 4 : avant 2026-11-21T07:30:16Z ; la borne de H + 54 heures reste, sans effet ici. |
| 6. Passages remplacés non écrits | important | Table « passage du texte → ce qui le remplace » en fin de section 2 ; libellé neuf du point 14 en C4. |
| 7. Écarts qui n'étaient pas des mots de Lazar | important | Remplacé par la décision reçue : les trois écarts sont accordés, `GO-2026-11-20-59 (2)` et `GO-2026-11-20-60 (2)`, cités à l'en-tête et en C1, C4, C5, C6. La « clé neuve » n'en fait plus partie. |
| 8. C1 trop générale | mineur | Libellé du contre-lecteur repris ; « avant qu'une famille soit formée » retiré. |
| 9. Contenu exact de la ligne tenu par personne | mineur | Le code tient les instances (couple 3 du code) ; la section 5 confie le contenu exact à la session. |
| 10. Validité de l'accord de calcul | mineur | Section 5 : vérification avant l'inscription ; sinon, nœud. |
| 11. Lectures déclarées, chiffres, H | mineur | Lectures complétées ; 18,5 dollars retiré ; H = 2026-11-20T01:30:16Z écrite. |
| 12. Chemin de scellement, noms de fichiers | mineur | Chemin proposé à l'en-tête ; exception à R12 en C5. Adapté : la référence de la ligne de relance cite l'additif, puisqu'il n'y a plus de ligne `CODE-RELANCE-FORMATION-B5F`. |

## 3. Ce que fait le code, depuis le code des premières marches

Six fichiers, 500 lignes ajoutées, 99 retirées, essais compris. Hors des essais :

- **`formation_v1.py`**
  - Constantes : `RELANCES_MAX = 6`, `ENVELOPPE_RELANCE_USD = 147.0`, `INSTANCES_TOMBEES`, `MENTION_CODE_RELANCE`, `CLE_CODE_RELANCE` (nom de la ligne dans les messages), `_CODE_RELANCE_REF`.
  - `lire_code_et_accord`, pour la ligne de relance, dans cet ordre : contenu lisible ; pas de doublon ; après `GO-FORMATION-B5F` ; accord égal à celui de `GO-FORMATION-B5F` ; six instances au plus ; 147 dollars au plus ; instances tombées seulement ; une et une seule mention du code des relances dans la référence ; commit différent de celui de `CODE-FORMATION-B5F`. Le résultat `relance` porte `"commit"`.
  - `commit_du_code` : (commit, nom de la ligne) du code que joue la marche.
  - `exiger_filiation_du_code_des_relances`, neuve.
  - `exiger_code_au_commit`, `exiger_code_de_la_session` : argument `cle`, pour le message seulement.
  - `executer` et `commande_de_creation` : pour une relance, filiation, puis comparaison au code des relances ; pour une première marche, comme avant.
  - `depense_session` : le plafond commun de 200 dollars vaut pour toute marche.
  - Entropie, noms de familles, graines, coupures par instance, branches de sortie, échéance d'arrêt : aucune ligne changée.
- **`lancer_b5f_formation_v1.sh`** : commentaires seulement.
- **`amorce_b5f_formation_v1.sh`** : `MIN_ESSAIS=244` et son commentaire.
- **`engagement_v1.py`** : aucun changement.

Remarque : avec la garde des instances tombées, le compte de six et l'enveloppe de 147 dollars ne peuvent plus être atteints seuls par un registre réel. Je les garde, parce que l'additif les énonce (C2, C3) ; chacune est isolée par un essai.

## 4. Compte des essais

Commande du mandat, sur l'arbre du commit `d116bf78…` :

`cd $S/relance/code && PYTHONPATH=src $S/venv-b5f/bin/python -m pytest -q -p no:cacheprovider tests/test_barreau5_familles_*.py --basetemp=$S/relance/essais`

- **244 passés, 0 échec** (97,8 s). Code des premières marches : 235. Écart : les 9 essais du fichier `tests/test_barreau5_familles_formation_relance_v2.py`.
- Essais voisins : `tests/test_lancer_b5f_formation_v1.py` 37 passés ; les deux fichiers d'essais de l'amorce 54 passés. Soit **91**. Les essais de l'amorce ont été joués avec `MIN_ESSAIS=244` ; seul le motif d'un cas du lanceur a changé depuis, et le lanceur a été rejoué après.

## 5. Épreuve par retrait et épreuve par mutation, refaites

**Par retrait.** Les trois fichiers d'essais du commit corrigé, joués sur une copie de l'arbre de `31fca83b…` (code des premières marches) : **15 échecs et 1 erreur, 118 passés**. Les 16 sont exactement les essais neufs ou retouchés ; aucun autre n'échoue.

- Fichier neuf, 9 sur 9 : `test_aucune_cle_neuve_le_registre_final_se_lit_par_le_lecteur_du_code_de_lecture_fige`, `test_ligne_exacte_de_l_additif_les_six_instances_tombees`, `test_instances_tombees_seulement_cas_sain_et_artefacts`, `test_code_des_relances_dans_la_reference_cas_sain_et_artefacts`, `test_ligne_de_relance_cite_l_accord_de_la_formation_cas_sain_et_artefacts`, `test_commit_du_code_premiere_marche_et_relance_cas_sain_et_artefacts`, `test_filiation_du_code_des_relances_cas_sain_et_artefacts`, `test_message_de_la_comparaison_du_code_nomme_la_ligne`, et `test_marche_reelle_compare_le_code_au_commit_de_sa_ligne_cas_sain_et_artefacts` (en erreur : son montage cherche une fonction que le code v1 n'a pas).
- Essais de formation retouchés, 3 sur 3 : `test_registre_relance_unique_cas_sain_et_artefacts`, `test_registre_relance_bornee_six_instances_et_enveloppe_de_147_usd`, `test_depense_deux_compteurs_la_relance_sous_le_plafond_commun`.
- Essais du lanceur, 4 sur 4 : `test_commande_artefacts_aucune_commande_de_creation[relance_sept_instances]`, `test_relance_unique_cas_sain_et_artefacts`, `test_relance_au_code_de_la_ligne_code_relance_cas_sain_et_artefacts`, `test_depense_d_une_relance_sous_le_plafond_commun_et_sa_coupure`.

Un premier passage donnait 14 échecs et 1 erreur : le cas `relance_sept_instances` passait sur le code v1, dont le message commence par les mêmes mots. Son motif attendu est devenu « 7 instances citées, 6 au plus » ; l'épreuve a été rejouée en entier.

**Par mutation.** Chaque garde changée ou neuve retirée une à une dans le code corrigé : **23 tuées sur 23**. Compte desserré ; enveloppe desserrée ; instance non tombée admise ; instance 6 comptée tombée ; mention de trop admise ; plusieurs commits admis ; borne de droite de la mention retirée ; borne de gauche retirée ; code des relances égal au code v1 admis ; accord libre ; commit rendu pour une relance ; comparaison sur l'instance ; à la commande ; plafond commun d'une relance ; arbre de la session ; commit de course ; comparaison supprimée ; repli sur le code v1 sans ligne de relance ; filiation non exigée sur l'instance ; à la commande ; filiation toujours vraie ; filiation à l'envers ; clé neuve ajoutée à `engagement_v1.py`.

## 6. Essai du registre final, lu par le code de lecture figé

- **Registre** : celui de la branche principale tel que le dépôt local le connaît (`origin/main` à `3a86f8362b6206dfecdff0b41faf78b1d682f39b`, sans mise à jour de ma part), sha256 `33ef7f6c…b49ffa`, cinq lignes à clé ; plus la ligne de relance de l'additif, avec en référence « code des relances commit d116bf78… ». Registre final d'essai : sha256 `37f4d828…996a148`.
- **Code de lecture figé** : `src` extrait du commit `c76e79169eee337ce66c7d88f62d039e853eebfc` dans `$S/relance/lecture-figee-v3`. Je n'ai lu aucun fichier de ce code ; j'ai appelé `lecture_v1.relance_du_registre`, comme le contre-lecteur.
  - `engagement_v1.py` : sha256 `565d4e51…536396`, égal à celui du code des relances.
  - Six clés lues ; relance lue : `[1, 2, 3, 4, 5, 7]`. **Accepté.**
  - Artefact, la même chose plus une ligne `CODE-RELANCE-FORMATION-B5F` : refusé, « clé CODE-RELANCE-FORMATION-B5F inconnue ».
- **Code des relances** (`d116bf78…`), même registre : relance lue `{'go_id': 'GO-2026-11-19-86', 'instances': [1, 2, 3, 4, 5, 7], 'commit': 'd116bf78…'}` ; code des premières marches `ef800868…` ; entropie inchangée.
- Filiation réelle : `ef80086821db08ffab42e23310a0b880ec72b9a4` est un ancêtre de `d116bf78…`.

Dans la suite d'essais, le même contrôle est tenu sans le code de lecture (absent de l'arbre des relances) : l'empreinte de `engagement_v1.py` est comparée à celle du fichier figé, et son lecteur lit le registre à six lignes.

## 7. Ligne de registre à inscrire

Une seule ligne, sur le registre propre, après le scellement de l'additif et la vérification du code, avant la première création :

- clé : `GO-RELANCE-FORMATION-B5F`
- contenu exact : `GO-2026-11-19-86 ; instances 1,2,3,4,5,7`
- référence proposée (moins de 600 signes) : `mot de Lazar GO-2026-11-20-51 ; écarts accordés GO-2026-11-20-59 (2) et GO-2026-11-20-60 (2) ; additif 1 scellé <chemin> sha256 <64 signes> ; code des relances commit d116bf78bb2084b2d4f406535a6c6f0a23179efe ; cumul commun relevé <montant> USD ; enveloppe GO-2026-11-19-87 non employée`
  (si la vérification fait changer le code, le commit change : reprendre celui du code vérifié)

**Contrôle à faire avant de commettre la ligne, parce qu'elle ne se réécrit pas** : une référence mal formée (mention absente, en double, sans « ; ») rendrait toute relance impossible sans nœud. Jouer d'abord, sur le fichier du registre candidat :

```
cd <arbre au code des relances> && PYTHONPATH=src python $S/relance/essai_registre_final_v3.py <registre de la branche principale, sans la ligne> <commit du code vérifié> relances
```

ou lire directement le fichier candidat par `formation_v1.lire_code_et_accord`.

Puis le **commit de course** : fils du commit du code vérifié, seul `registres/` diffère, registre propre égal à celui de la branche principale à l'octet.

## 8. Commande de relance, jouée par la session

Dans un arbre de travail au commit de course, pour N dans 1, 2, 3, 4, 5, 7, dans cet ordre, au fil des offres :

```
GO_ID=GO-2026-11-19-86 bash scripts/lancer_b5f_formation_v1.sh relance RACINE N OFFRE.json COMMIT_DE_COURSE BRANCHE_CODE prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md AAAAMMJJ-HHMMSS-b5f-formation-N-x1
```

Le script n'appelle pas le loueur : il contrôle et imprime. Suivi de la dépense, relances comprises dans le cumul commun :

```
bash scripts/lancer_b5f_formation_v1.sh depense N 3 CUMUL_INSTANCE PRIX_INSTANCE_H CUMUL_COMMUN PRIX_COMMUN_H 1
```

Je n'ai joué aucune de ces commandes contre le loueur.

## 9. Points ouverts

1. **« (2) » dans `GO-2026-11-20-59 (2)` et `GO-2026-11-20-60 (2)`** : repris tel que la session mère l'a écrit. Je n'ai pas lu ces lignes ; à elle de vérifier que la citation est exacte.
2. **Coupures de 21 et 8 dollars** : données par la session mère, d'après le devis scellé, section 4. Je n'ai pas lu le devis.
3. **Registre de la branche principale** : l'essai de la section 6 porte sur l'état connu du dépôt local (`3a86f836…`). Si une ligne s'ajoute avant l'inscription, rejouer le contrôle de la section 7.
4. **Lecture au-delà du mandat premier** : le registre propre de la branche principale (cité par le mandat, lu à un autre commit) et les deux contre-lectures. Le code de lecture figé a été extrait et appelé, non lu.
5. **Écritures dans les métadonnées git du dépôt principal** : le commit, et une copie de travail temporaire ajoutée puis retirée pour les épreuves.
6. **L'exception à R12** est écrite dans l'additif ; sa consignation au registre des décisions revient à la session mère.
7. **Le plafond commun et la réserve de 24 dollars ne sont tenus que par la session.** Sur l'instance, seule la minuterie à la coupure arrête.
8. **Temps** : vérification, scellement, inscription et six créations doivent tenir avant le 21 novembre 2026 à 07:30:16Z.
