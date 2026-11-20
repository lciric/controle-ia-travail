# Rapport du développeur : code de formation v2, relance des six instances (barreau 5)

Écrit le 20 novembre 2026 par le rédacteur de l'additif 1 et développeur du code v2 (Claude Fable 5.2), sur le mandat `mandat-redacteur-additif-et-code-v2.md`. Pièce de travail ; le code qu'elle décrit est une pièce d'instrument, à contre-lire par un autre modèle avant l'inscription de `CODE-RELANCE-FORMATION-B5F`.

`$S` = `/tmp/claude-0/-home-user-controle-ia-travail/2e5ab823-f39e-5eb7-8014-a7e033a3a8e4/scratchpad`.

## 1. Les pièces

| pièce | chemin | repère |
|---|---|---|
| additif 1 (projet) | `$S/relance/additif-1-relance-six-instances-v1.md` | sha256 `491b60d43a8573fa5db8e9c9d76f2268210df6f892a4d51ae0743f5e42649e73` |
| code v2 | `$S/relance/code`, branche locale `formation-b5f/code-relance-v2` | commit `a74dfb4988dbe8024d5923f95999538b248d166c`, parent `31fca83b0c26cd035fe9e660d123e690a41b6271` ; un seul commit, jamais poussé |
| différentiel entier | `$S/relance/diff-code-relance-v2.patch` | sha256 `8e8c927c83db45894905b86cae73263f2a711f7156a2e5db608ed6b62bfcf7a3` |
| sortie de l'épreuve par retrait | `$S/relance/epreuve-par-retrait-sortie.txt` | 14 échecs, 118 passés, sur le code v1 |
| sortie de l'épreuve par mutation | `$S/relance/epreuve-par-mutation-sortie.txt` ; programme `$S/relance/mutations_v2.py` | 16 tuées sur 16 |

Empreintes au commit du code v2 (16 premiers signes) : `__init__.py` b8d53a9905ab172f (inchangé) ; `edition_cout_v1.py` 23002f43a02e057a (inchangé) ; `engagement_v1.py` 152f30ad555b2303 ; `formation_v1.py` 3ea661b7ebb37230 ; `lancer_b5f_formation_v1.sh` adac4b5b1d8eb9bd ; `amorce_b5f_formation_v1.sh` 514963d288f7be4c ; `tests/test_barreau5_familles_formation_relance_v2.py` d0cea5f25a7cbf2b.

Le commit ne touche ni `registres/`, ni `prereg/`, ni `docs/` (vérifié par `git diff --quiet`).

## 2. Le différentiel, commenté

Sept fichiers, 360 lignes ajoutées, 97 retirées ; 81 ajoutées et 42 retirées hors des essais.

### `src/controle_ia/barreau5_familles/engagement_v1.py`
- `CLES_REGISTRE` reçoit `CODE-RELANCE-FORMATION-B5F`. Sans cela, le registre entier est refusé dès que la ligne est inscrite. Rien d'autre.

### `src/controle_ia/barreau5_familles/formation_v1.py`
1. **Constantes** : `RELANCES_MAX` passe de 2 à 6 ; `ENVELOPPE_RELANCE_USD` de 56 à 147 ; `CLE_CODE_RELANCE = "CODE-RELANCE-FORMATION-B5F"`.
2. **`lire_code_et_accord`** :
   - lit la ligne neuve, facultative : contenu « `commit <40 signes>` » à la lettre (aucune entropie admise), instant postérieur à `GO-FORMATION-B5F` ;
   - la ligne de relance exige la ligne neuve, et un instant strictement postérieur au sien ;
   - la ligne de relance cite l'accord de `GO-FORMATION-B5F`, sinon refus (la relance entre sous le plafond commun de cet accord) ;
   - le résultat `relance` porte en plus `"commit"`, le commit du code des relances ; `commit` et `entropie` restent ceux de `CODE-FORMATION-B5F`.
3. **`commit_du_code(lu, relance)`**, neuve : rend (commit, clé) du code que joue la marche. Première marche : `CODE-FORMATION-B5F`. Relance : `CODE-RELANCE-FORMATION-B5F` ; sans ligne de relance, refus ; `relance` autre que vrai ou faux, refus.
4. **`exiger_code_au_commit`** et **`exiger_code_de_la_session`** : un argument `cle` de plus, qui ne sert qu'au message de refus (il nomme la ligne comparée). Défaut : `CODE-FORMATION-B5F`, comme avant.
5. **`executer`** (marche sur l'instance) et **`commande_de_creation`** (session) : le code comparé est celui de `commit_du_code`. Une relance se compare donc au code v2 ; une première marche, au code v1. Avec l'arbre du code v2, la commande d'une première marche est refusée : c'est voulu, les premières marches sont créées.
6. **`depense_session`** : le retour anticipé d'une relance est retiré. Le plafond commun de 200 dollars vaut pour toute marche ; le résultat d'une relance porte `"plafond": 200.0` au lieu de `None`.
7. L'entropie, les noms de familles, les graines, les coupures par instance, les branches de sortie, l'échéance d'arrêt : aucune ligne changée.

### `scripts/lancer_b5f_formation_v1.sh`
- Commentaires seulement (sous-commandes `relance` et `depense`, en-tête). Aucune ligne exécutée ne change.

### `scripts/amorce_b5f_formation_v1.sh`
- `MIN_ESSAIS` passe de 235 à 242, et son commentaire. **Changement non prévu par le mandat, mais forcé** : l'essai `test_texte_plancher_d_essais_egal_au_nombre_d_essais_du_paquet` exige l'égalité entre ce plancher et le nombre d'essais du paquet. L'amorce part en base 64 depuis le commit de la course : les relances reçoivent donc celle du code v2.

### Essais
- `tests/test_barreau5_familles_formation_relance_v2.py`, neuf : 7 essais.
- `tests/test_barreau5_familles_formation_v1.py` : 3 essais retouchés (ligne de relance ; borne à six instances et 147 dollars, renommé ; dépense sous le plafond commun, renommé).
- `tests/test_lancer_b5f_formation_v1.py` : 3 essais retouchés (cas `relance_sept_instances` ; relance unique ; dépense d'une relance, renommé), 1 essai neuf (`test_relance_au_code_de_la_ligne_code_relance_cas_sain_et_artefacts`), et l'aide `_registre_propre` qui écrit la ligne neuve.

## 3. Gardes changées ou neuves : cas sain et artefact (R5)

| garde | cas sain | artefact refusé |
|---|---|---|
| clé neuve connue du registre | la ligne se lit | clé voisine inconnue ; clé en double |
| contenu de la ligne du code des relances | « commit » et 40 signes | entropie ajoutée ; 39 signes ; sans le mot « commit » ; majuscules |
| son instant | après `GO-FORMATION-B5F` | avant |
| la ligne de relance exige la ligne du code | les deux lignes | ligne de relance seule |
| ordre des deux lignes | code puis relance | relance avant ; même instant |
| accord de la ligne de relance | celui de `GO-FORMATION-B5F` | `GO-2026-11-19-87` ; deux accords dans le contenu |
| six instances au plus | 1,2,3,4,5,7 ; parties | sept instances (garde isolée par une table de coupures retouchée) |
| 147 dollars au plus | 147 à trois membres ; 145 à deux | 158 ; 154 ; 148 (garde isolée) |
| code d'une relance, sur l'instance | comparé au commit de la ligne neuve | relance non citée ; pas de ligne de relance ; aucun manifeste écrit |
| code d'une relance, à la commande | commande imprimée | ligne qui cite le code v1 ; première marche sous le code v2 ; arbre de la session retouché |
| plafond commun pour une relance | cumul commun de 100 ou 150 | cumul commun de 198 ou 199,9 ; coupure de l'instance atteinte |

## 4. Compte des essais

Commande du mandat, jouée sur l'arbre du commit :

`cd $S/relance/code && PYTHONPATH=src $S/venv-b5f/bin/python -m pytest -q -p no:cacheprovider tests/test_barreau5_familles_*.py --basetemp=$S/relance/essais`

- **242 passés, 0 échec** (99,6 s). Code v1, même commande, avant tout changement : 235 passés. Écart : les 7 essais du fichier neuf.
- Essais voisins, hors de la commande du mandat mais dans l'arbre gelé : `tests/test_lancer_b5f_formation_v1.py` 37 passés ; `tests/test_amorce_b5f_formation_v1.py` et `tests/test_amorce_b5f_formation_entiere_v1.py` 54 passés. Soit 91.

## 5. Épreuve par retrait

Les trois fichiers d'essais du code v2 ont été joués sur une copie de l'arbre du commit `31fca83b…` (code v1) : **14 échecs, 118 passés**. Les 14 échecs sont exactement les essais neufs ou retouchés ; aucun autre essai n'échoue.

- Fichier neuf (7 sur 7) : `test_cle_du_code_des_relances_connue_du_registre_cas_sain_et_artefact`, `test_lignes_exactes_de_l_additif_les_six_instances_tombees`, `test_ligne_du_code_des_relances_cas_sain_et_artefacts`, `test_ligne_de_relance_exige_le_code_des_relances_et_l_accord_de_la_formation`, `test_commit_du_code_premiere_marche_et_relance_cas_sain_et_artefacts`, `test_marche_reelle_compare_le_code_au_commit_de_sa_ligne_cas_sain_et_artefacts`, `test_message_de_la_comparaison_du_code_nomme_la_ligne`.
- Essais de formation retouchés (3 sur 3) : `test_registre_relance_unique_cas_sain_et_artefacts`, `test_registre_relance_bornee_six_instances_et_enveloppe_de_147_usd`, `test_depense_deux_compteurs_la_relance_sous_le_plafond_commun`.
- Essais du lanceur (4 sur 4) : `test_commande_artefacts_aucune_commande_de_creation[relance_sept_instances]`, `test_relance_unique_cas_sain_et_artefacts`, `test_relance_au_code_de_la_ligne_code_relance_cas_sain_et_artefacts`, `test_depense_d_une_relance_sous_le_plafond_commun_et_sa_coupure`.

**En plus, par mutation du code v2** : chaque garde changée ou neuve retirée une à une (16 mutations : compte desserré, enveloppe desserrée, ligne de relance sans ligne du code, ordre des lignes, accord libre, instant de la ligne du code, contenu lu en préfixe, commit rendu pour une relance, comparaison sur l'instance, à la commande, de l'arbre de la session, plafond commun d'une relance, clé retirée du registre, comparaison supprimée, repli sur le code v1 sans ligne de relance). **16 tuées sur 16.**

## 6. Lignes de registre à inscrire

Registre propre `registres/barreau5-familles-jumelles-v1.md`, lignes ajoutées, dans cet ordre, instants strictement croissants (une seconde d'écart au moins). Les contenus sont lus à la lettre.

**Ligne 1**, après le scellement de l'additif, la contre-lecture du code v2 et la vérification de ses corrections :

- clé : `CODE-RELANCE-FORMATION-B5F`
- contenu exact : `commit a74dfb4988dbe8024d5923f95999538b248d166c`
  (si la contre-lecture fait changer le code, le commit change : reprendre alors celui du code vérifié)
- référence proposée : `additif 1 scellé <chemin> sha256 <64 signes> ; mot de Lazar GO-2026-11-20-51 ; code v2 = code de CODE-FORMATION-B5F plus les seuls changements de l'additif ; rapport du développeur <chemin> ; vérification <chemin> ; 242 essais ; entropie inchangée, celle de CODE-FORMATION-B5F`

**Ligne 2**, après la ligne 1, au plus tard à H + 54 heures (22 novembre 2026, 07:30:16Z) :

- clé : `GO-RELANCE-FORMATION-B5F`
- contenu exact : `GO-2026-11-19-86 ; instances 1,2,3,4,5,7`
- référence proposée : `mot de Lazar GO-2026-11-20-51 (décision : relance des six instances tombées faute de crédit, écart à « deux instances au plus » accordé, sous le plafond commun de 200 USD) ; additif 1 ; cumul commun relevé à l'inscription <montant> USD ; l'enveloppe GO-2026-11-19-87 n'est pas employée`

Les relances partent d'un **commit de course** : un commit fils de `a74dfb49…` dont seul `registres/` diffère, et dont le registre propre porte ces deux lignes. Ce commit doit être sur la branche du code que clonent les instances.

## 7. Commande de relance, jouée par la session

Dans un arbre de travail au code v2 (celui du commit de course), pour chaque instance N de 1, 2, 3, 4, 5, 7, dans cet ordre, au fil des offres :

```
GO_ID=GO-2026-11-19-86 bash scripts/lancer_b5f_formation_v1.sh relance RACINE N OFFRE.json COMMIT_DE_COURSE BRANCHE_CODE prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md AAAAMMJJ-HHMMSS-b5f-formation-N-x1
```

Le script n'appelle pas le loueur : il contrôle et imprime la commande de création, que la session joue aussitôt (l'échéance d'arrêt se compte depuis l'impression). Suivi de la dépense, pour toute marche, relance comprise :

```
bash scripts/lancer_b5f_formation_v1.sh depense N 3 CUMUL_INSTANCE PRIX_INSTANCE_H CUMUL_COMMUN PRIX_COMMUN_H 1
```

`CUMUL_COMMUN` et `PRIX_COMMUN_H` comptent désormais les relances. Je n'ai joué aucune de ces commandes contre le loueur.

## 8. Points ouverts

1. **Lectures hors de la liste du mandat.** Pour écrire le code, j'ai lu `engagement_v1.py` (lecteur du registre, liste des clés), la définition de `CHEMINS_GELES` dans `harnais/validation_reelle.py` (par recherche), et les essais du lanceur et des amorces. Ce sont des fichiers de code de la même chaîne, sans donnée ni résultat ; le mandat ne les citait pas. Je n'ai pas ouvert la garde de calcul. Un premier inventaire a listé les noms des fichiers du dépôt de travail (noms seulement, sortie non lue au-delà de l'aperçu).
2. **Règle des noms versionnés (R12).** Les fichiers sont retouchés sous leur nom « v1 » : la commande de marche, l'amorce et les essais portent ce nom, et le mandat demande un code minimal. La version est portée par le commit et par la clé neuve. À dire si un nom neuf est exigé.
3. **Garde ajoutée au-delà du strict nécessaire** : l'accord de la ligne de relance doit égaler celui de `GO-FORMATION-B5F`. Elle rend mécanique le point C6 de l'additif. Au contre-lecteur de la juger.
4. **Trois points de l'additif sont des lectures du mot de Lazar tel que relayé**, à confirmer : l'arrêt faute de crédit compte comme « tombée » (C1) ; les relances sont créées avant H + 30 heures (C7) ; la règle de la session avant l'inscription (cumul relevé de 45,98 dollars au plus, avec 7,02 dollars gardés pour la relecture). Je n'ai pas lu le devis : la réserve de la relecture et le reste pour la répétition générale et le stockage sont à vérifier par qui l'a lu. Le chiffre de 18,5 dollars de dépense vient du mandat.
5. **Heures.** H est déduite de la fin des créations donnée par le mandat : H = 20 novembre 2026, 01:30:16Z ; H + 54 heures = 22 novembre, 07:30:16Z ; H + 65 heures = 22 novembre, 18:30:16Z. À recouper avec la création de la première instance.
6. **Après l'inscription de la ligne 1, tout programme au code v1 refuse le registre** (clé inconnue). La session doit donc jouer le lanceur du code v2 pour tout ce qui lit le registre ; la destruction et sa vérification ne le lisent pas. Le code de lecture, figé à `CODE-LECTURE-B5F`, doit partir du code v2.
7. **Le plafond commun n'est tenu que par la session** (sous-commande `depense`), comme pour les premières marches. Sur l'instance, seule la minuterie à la coupure arrête. L'additif le dit.
8. **Le code ne sait pas que l'instance 6 n'est pas tombée.** Il borne le compte et la somme ; une ligne « 6,7 » passerait. Le contenu exact de la ligne 2 est tenu par la session mère.
9. **Le code ne vérifie pas que le commit du code v2 descend de celui du code v1.** C'est vrai par construction : `a74dfb49…` a pour parent `31fca83b…`.
10. **La colonne de référence de `GO-FORMATION-B5F`** dit encore que l'enveloppe `GO-2026-11-19-87` est « citée par toute ligne GO-RELANCE-FORMATION-B5F ». Cette ligne n'est pas réécrite ; l'additif prime.
11. **Rien d'impossible ni de contradictoire dans le mandat.** Le seul écart est le plancher d'essais de l'amorce (section 2).
