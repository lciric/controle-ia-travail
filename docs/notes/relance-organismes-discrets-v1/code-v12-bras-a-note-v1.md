# Code de l'instrument et de l'analyse du bras A des organismes discrets, version 12 — note du rédacteur — v1

Ce que la version 12 change, ce qu'elle laisse en limite écrite, et ce qu'il faut regarder en premier.

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`). À contre-lire par un autre modèle.
- **Références** : la vérification du code de la version 11 (`15b3f8528efb72d7d62df2d5ec638786f63c38e31847a56a6428e8dfdac5c6cc`) et ses pièces ; **le brouillon 35, qui fait foi** (`e62b4caec484f53c2afde2c7361136434eaa15ddb15b2f0e609c64edc3f757a2`), et sa note (`9dbe7c665c2da89eb7787cb2555a88c5b9b70c14cc558ceaf95c18643757f95f`, partie 4) ; la vérification du brouillon 35 (`765f906b830a72fbb3dc99a1fdb8b96b03d00c5c5b843379a6cf3f13ce563e0e`, C-1 et M-1), dont les deux corrections m'ont été données pendant le tour et que le brouillon 36 portera au texte.
- **Interdits tenus** : aucun interne de moniteur ouvert, ni par moi ni par mes programmes ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel réseau ni appel de modèle ; aucun sous-agent ; aucune dépense. `registres/`, `.claude/`, le journal et `prereg/` non touchés. Rien de committé. Aucun fichier existant modifié : la version 11 et le programme du constat en version 4 répondent toujours à leurs empreintes.
- **Heure** : 2026-11-20, 01:40Z.

## 1. Fichiers

Tous neufs, scellés par leur compagnon `.sha256`, non suivis par git.

| fichier | empreinte | ce qui change |
|---|---|---|
| `src/controle_ia/organismes_discrets/analyse_bras_a_v12.py` | `ba1acaa7c875c6a2cd00100d4f15c6d0216ca147d453206acc35873c93427c0d` | reprise de l'étape (n) ; un seul fichier de l'étape (m) par course ; confrontation des vingt lectures ; ouverture à cinq champs, acte à sept |
| `src/controle_ia/organismes_discrets/verdicts_bras_a_v12.py` | `89e4b8d0b51e1b8e5c4302ea1b82f719a57a6e7cde698532e4a6325edabd9a05` | un second fichier de l'étape (m) ne s'écrit pas ; `issues` lit la table C au rang d'origine ; « non rapportées : livraison refaite incohérente » |
| `src/controle_ia/organismes_discrets/graines_bras_a_v12.py` | `381878cd7ef7e23c6edb9fb4cf826fd8a1eb652b5497da8a39e99b2bd5146a8b` | `retire_l_inscription`, la fonction du retrait d'une configuration inscrite |
| `src/controle_ia/organismes_discrets/cloisonnement_bras_a_v12.py` | `be687467772fcc2deba4c3725137d784c4ce36f44a7d8b7c4699abc064461f89` | programmes autorisés : ceux de la version 12, et le programme du constat en version 5 |
| `src/controle_ia/organismes_discrets/configuration_bras_a_v12.py` | `8373851eef8723000871551a338a495d423f58bb345361cf5f19bbe8b768cca8` | rien, hors les noms et le brouillon de référence |
| `src/controle_ia/organismes_discrets/arrets_bras_a_v12.py` | `cc632df30501129003041ac74baa5b54646ce5b82d66a88473a3e3c99a18425d` | rien, hors les noms |
| `src/controle_ia/organismes_discrets/depots_bras_a_v12.py` | `db0aa22f0a7ef6d17a97ff5200603afabb543233a768582248224d1843519ffc` | rien, hors les noms |
| `src/controle_ia/organismes_discrets/mesures_bras_a_v12.py` | `7a1e6aab5e3e42169584daf91660cb42ad00444fae9536b078d3db8b5064601d` | rien, hors les noms |
| `src/controle_ia/organismes_discrets/permutation_etiquettes_bras_a_v12.py` | `20b78a8a3ecd7b19ba3144ffc2bcb4dc097640ff079f63495d8fdbfabd0c5b58` | rien, hors les noms |
| `scripts/constat_de_lancement_discretion_bras_a_v5.py` | `fd5fddcd893e2cee91765ced911948009eb09ebd3b2382bc585fb7e4700ce290` | **version 5 du programme** : la garde du registre ne se lève que par une révocation |
| `tests/aide_bras_a_v12.py` | `6ee51f87ef67e43b93337710a3ed9c4f57b9e853f0dafc043d84479724cc1cfb` | aides des essais |
| `tests/test_analyse_bras_a_v12.py` | `a7bf64aa446837ae42a750491496fc5790c86ab6a4a8f205e3260f77d19288dd` | 74 essais |
| `tests/test_graines_bras_a_v12.py` | `7fdde38d3bde18bac0309cec0754b9ea904013e41fd6a3a6ad37e46308337db5` | 110 essais |
| `tests/test_cloisonnement_bras_a_v12.py` | `1b39ba8e7ca3f277dc4ca32a7c0eabb62fe4ecafd18cb9410fe083369758c1cf` | 62 essais |
| `tests/test_verdicts_bras_a_v12.py` | `2f074902a946a7d0a0d8258d6271d5489e885335143199ed8cd905de6c3160fc` | 27 essais ; lit les phrases du brouillon 35 |
| `tests/test_mesures_bras_a_v12.py` | `6d4508c7a44351161e00ec9048670c1cef635e0ae7ebd06ef78630d101190f46` | 9 essais |
| `tests/test_permutation_etiquettes_bras_a_v12.py` | `b13c996354e48c78aa28175a4f851713dc78097b54a40d4ab7c8d3a4fbd863c2` | 9 essais |

Le relevé des défauts du texte est à côté de cette note : `defauts-du-texte-trouves-en-codant-v12.md`.

## 2. Essais

- **331 essais passent** : 291 dans mes six fichiers, 36 dans `tests/test_reponses_lecteurs_v5.py`, 4 dans `tests/test_epreuves_couverture_bras_a_v3.py`.
- **Commande** :
  `PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v12.py tests/test_verdicts_bras_a_v12.py tests/test_graines_bras_a_v12.py tests/test_cloisonnement_bras_a_v12.py tests/test_permutation_etiquettes_bras_a_v12.py tests/test_mesures_bras_a_v12.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py`
- Le dernier passage a été fait après le scellement des modules : l'essai de la garde statique sur l'arbre réel exige leurs compagnons.
- Données fabriquées dans les essais ; graines par `SeedSequence`. Durée : environ une minute et demie.

## 3. C-1 — après un arrêt à l'étape (n), seule l'étape (n) se rejoue

**L'essai d'attaque de la vérification, rejoué, s'arrête** (`test_apres_un_arret_a_l_etape_n_aucune_lecture_de_l_etape_m_ni_second_fichier`). Trois gardes le tiennent, et l'essai éprouve chacune seule, en neutralisant les deux autres :

1. **La ligne.** Une ligne de GO qui cite un fichier d'arrêt de l'étape (n) n'ouvre aucune lecture de l'étape (m) (`_exiger_la_ligne_de_reprise`, argument `etape`).
2. **La lecture.** Dès qu'un fichier de l'étape (m) est scellé dans la course, aucune lecture de cette étape ne s'ouvre, à quelque rang et sous quelque ligne que ce soit (`exiger_un_seul_fichier_de_l_etape_m`).
3. **L'écriture.** Un second fichier de l'étape (m) ne s'écrit pas (`verdicts_bras_a_v12.ecrire_fichier_de_l_etape_m`). Deux fichiers posés à la main dans une course : plus rien ne se lit, `issues` comprise.

**La reprise elle-même suit le brouillon 35** (`ouvrir_la_reprise_de_l_etape_n`, puis les fonctions de l'étape (n) déjà connues) :

- la ligne cite un fichier d'arrêt de l'étape (n), le module et le rapport ; l'acte de reprise est scellé avant toute lecture du fichier des scores refait ;
- rien de l'étape (m) n'est relu ni écrit au rang de la reprise : ni lecture rangée dans un cas, ni état, ni fichier, ni constats, ni ouverture ;
- l'empreinte du fichier des scores refait se lit dans la clé `scores_par_unite` de la sortie refaite ; un défaut de cette clé est un arrêt à l'étape (n), consigné avec l'empreinte du fichier de l'étape (m) d'origine ;
- l'étape (n) se joue sur le fichier de l'étape (m) **du rang d'origine** ; ce que la règle rapporte de chaque lecture se recompose de la sortie d'origine, sous la configuration du rang d'origine ;
- le fichier des grandeurs s'écrit dans le dossier de la livraison refaite et cite l'empreinte du fichier de l'étape (m) d'origine ;
- un nouvel arrêt à l'étape (n) se reprend de même : l'essai enchaîne deux reprises ;
- le rang d'origine est celui du dossier qui porte le fichier de l'étape (m), quel qu'il soit : un essai part d'un arrêt à l'étape (m), repris au rang 2, puis d'un arrêt à l'étape (n), repris au rang 3.

**Ce que l'appelant donne de plus** : la sortie d'origine (`sortie_d_origine`), à l'ouverture de la reprise, à la lecture du fichier des scores et au fichier des grandeurs. Le programme la reconnaît à l'empreinte que portent les constats de l'étape (m) ; une autre pièce est refusée. Pour une livraison ordinaire, elle ne se donne pas.

**Après une reprise aboutie**, `issues` se demande avec la sortie refaite et sa configuration : la table C vient du fichier d'origine. Sur la livraison d'origine, `issues` dit toujours « non rapportées : livraison refusée ».

## 4. Confrontation des vingt lectures (vérification du brouillon 35, M-1)

- **Ce que le code fait.** Lors d'une reprise de l'étape (n), les vingt lectures de la sortie refaite sont comparées à celles de la sortie d'origine, nombre pour nombre, **en fractions exactes** (`lectures_refaites_coherentes`). `0.520` vaut `0.52` ; `0.52000000000000000001` ne le vaut pas, alors que la virgule flottante ne voit pas l'écart.
- **Un écart n'est pas un arrêt.** Ni événement, ni fichier d'arrêt. Les grandeurs de l'étape (n) sont « non rapportées : livraison refaite incohérente ». Le fichier des scores refait n'est lu par aucune fonction, aucun fichier de grandeurs ne s'écrit, et le fichier de l'étape (m) reste tel quel.
- **L'écart est scellé** dans le dossier des arrêts : `livraison-refaite-incoherente-bras-a-<seize signes>.json`, quatre champs — l'événement, l'empreinte de la sortie refaite, celle de la sortie d'origine, celle de la configuration. `issues` le lit, et n'a donc pas besoin des deux pièces.
- **Trois choix que j'ai faits, faute de texte** (relevé, partie A, points 2 à 4) :
  - la confrontation se fait **après** l'acte de reprise : la ligne est donc dépensée ;
  - une livraison refaite incohérente **ne se reprend pas** : aucune ligne ne peut citer son constat ;
  - les lectures se comparent dans la même forme : une sortie refaite qui les donne en liste quand l'origine les range par dose est incohérente.

## 5. M-1 — le contrôle du premier départ ne sert plus au rejeu

- L'ouverture de lecture a cinq champs, l'acte de reprise sept : chacun porte l'empreinte du contrôle de lancement du premier départ, ou `null`.
- Un rejeu refuse tout contrôle que porte déjà une ouverture, un acte de reprise ou une trace de rejeu.
- La garde de sortie refuse un premier départ qui dirait un autre contrôle que celui de son ouverture ou de son acte.
- L'essai de la vérification est rejoué : contrôle sain avant le premier départ, lecture interrompue, ligne qui retire la configuration, aucun contrôle refait. Le rejeu ne part plus. Il part sous un contrôle refait et sain.
- L'acte d'une reprise de l'étape (n) porte lui aussi le contrôle le plus récent, qui doit être sain.

## 6. M-2 et M-3 — la garde du registre au constat : programme en version 5

- **Une inscription ne se lève que par une révocation.** Une configuration de rang 1 est refusée dès qu'une autre configuration de l'analyse est inscrite sans avoir été retirée par une ligne de type « révocation », entrée après elle, qui cite son empreinte entière (`graines_bras_a_v12.retire_l_inscription`).
- **La dispense « suivie d'une reprise » est retirée**, comme le demande la vérification du brouillon 35 (C-1). L'essai de la version 11 qui en dépendait est récrit ; un essai neuf rejoue la fenêtre sur une course : la ligne de reprise est inscrite, la configuration de rang 2 ne l'est pas encore, et une configuration de rang 1 donnée avec un autre dossier des arrêts est refusée.
- **Le constat de la configuration retirée sort malsain** : la ligne qui la retire cite son empreinte sans être sa ligne d'inscription. Un essai le fixe.
- Un abrégé ne retire rien ; ni une ligne d'un autre type, ni une révocation placée avant l'inscription, ni celle d'une autre empreinte.
- Le refus reste un arrêt du programme, sans constat ni fichier (code de sortie 2), comme à la version 4. La ligne 8.4 du brouillon 35 dit « constat malsain » : relevé, partie B.

## 7. Précisions A.1 à A.5

| précision | état |
|---|---|
| A.1, configuration inscrite puis abandonnée | portée : c'est M-3 |
| A.2, mêmes choix et « en attente » | déjà codée à la version 11 ; essais gardés |
| A.3, ce qu'un constat de pièce donnée peut ouvrir | déjà codée ; l'essai l'éprouve maintenant seule, la garde du seul fichier de l'étape (m) jouant avant elle |
| A.4, contrôle d'avant le premier départ | portée : c'est M-1 |
| A.5, ponctuation finale | déjà codée ; les douze lignes de la vérification sont rejouées telles quelles |

M-4 de la vérification (abrégés de moins de seize signes) : écart motivé, inchangé.

La ligne de l'écart à R9 : un essai fabrique une ligne de la même forme que GO-2026-11-19-97 — huit cellules, la phrase seule dans la quatrième — et la porte s'ouvre.

## 8. À regarder en premier

1. **Une limite que cette version ne ferme pas, et que j'ai vérifiée par un essai avant de l'écrire** : la même configuration, copiée octet pour octet dans un autre dossier de course, y ouvre une seconde première livraison sous la même ligne d'inscription. J'ai obtenu « ne repère pas » dans un dossier, « repère » dans l'autre. La garde du registre ne voit rien : une seule empreinte est inscrite. Le code ne peut pas la fermer seul. Relevé, partie A, point 1.
2. **Les trois choix de la confrontation** (partie 4). Le brouillon 36 peut les trancher autrement.
3. **`_livraison_d_origine`** : elle remonte les actes de reprise dont la livraison refusée porte un arrêt de l'étape (n). Tout ce qui dit « quel est le fichier de l'étape (m) de cette pièce » passe par elle.
4. **Les trois gardes de C-1 se recouvrent.** Dans l'essai tel quel, c'est la garde de la lecture qui parle la première. Deux essais de la version 11 attendaient « rien à reprendre » : ils reçoivent maintenant le refus du second fichier, et éprouvent l'ancienne garde seule.
5. **Le programme du constat est en version 5**, alors que le brouillon 35 nomme la version 4.

## 9. Portée de mes lectures et méthode

- **Lu** : `CLAUDE.md` ; la vérification du code de la version 11 en entier, ses pièces `attaques_v11.py` et `abandon_v11.py` en entier, les autres par leurs sorties ; la note du brouillon 35, partie 4 et réserves ; le brouillon 35 par passages (6.9, « Périmètre d'une reprise après un arrêt à l'étape (n) » ; les deux lignes neuves de 8.4 ; les conventions sur la garde du registre et le septième champ de l'acte) ; la vérification du brouillon 35, parties 2 à 6 ; mes fichiers de la version 11.
- **Non lu** : le reste du brouillon 35 ; les registres ; tout chemin cloisonné.
- **Méthode** : copie mécanique des fichiers de la version 11 sous leurs noms neufs, puis remplacements exacts par programme. Revue adverse avant tout scellement ; rien n'a été scellé avant le dernier passage des essais.
