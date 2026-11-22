# Vérification de la partie 1, v2, de l'addendum des empreintes et des déclarations (tranche de l'ajustement de nos lentilles)

- **Vérificateur neuf** (R2) : n'a écrit ni relu aucune pièce de ce travail ; n'écrit que ce rapport (sans compagnon `.sha256` : un seul
  fichier permis ; à sceller par la session mère).
- Date (`date -u`) : 2026-11-18T05:41:58Z.
- Objet : `docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v2.md`, empreinte recalculée
  `0b418ed13b07fc2886f07367a1e478d90038e59e0c2bfd1bc65a03f3a5695596` (égale à l'attendue et à son compagnon `.sha256`).
- Version précédente : `…-partie1-v1.md`, `d50ce0bc5166df7aa1c627eb4bea61eee84e1d5e430fb6ad3f2a96c3c7bcef50`.
- Contre-lecture de la v1 : `contre-lecture-addendum-tranche-b-beta-partie1-v1.md`, `d3f54cac2adf35c032bf185389f6d9f9d6a1078542179e91d9dc9041fa7a6c10`.
- Texte gelé scellé : `texte-gele-tranche-b-beta-v1.md`, `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` (recalculée, égale).
- Code des verdicts : `src/controle_ia/neuron_lens/verdicts_b_beta_v4.py`, `8c07434f9db0e35e10eb806218da320bc0d6e404e41c4f60c495b35906d88b87` ;
  essais `tests/test_neuron_lens_verdicts_b_beta_v4.py`, `1b63c8cbbcdff180e0a3433ebeb139eea3c4aeeb13fcc3f694352219a4f7bb5a` (rejoués : 82 réussis).
- Partie 2 de la tranche des lentilles publiques (seul fichier de `diag/` ouvert, lignes 48 à 57) :
  `9612ae4e6c7906e05e8e0c249b32d6bc9b139bd82f51644936ee6435657cc6d1` (recalculée, égale à l'addendum).
- Non ouverts : `registres/` ; tout autre fichier de `diag/`. Rien d'exécuté ni d'importé depuis `/home/user/stdlogits`. Aucun autre
  fichier modifié, rien de committé. Sondes : script jetable hors du dépôt, entrée saine `sain()` des essais, module importé avec
  `PYTHONPATH=src`.

## Verdict

**À corriger** : 0 bloquante, **1 majeure neuve**, 6 mineures (2 restes de la reprise, 4 neuves).

La majeure et les neuf mineures de la contre-lecture sont reprises, et le diff ne touche rien d'autre. Tous les effets écrits au § 1.1
sont **justes** (rejoués par sonde). Reste une phrase **fausse** dans la déclaration : la borne « l'effet n'existe que pour
32 ≤ n < 48 » ne vaut pas pour la lecture contre ablation (B-7) ni pour le déclencheur de l'audit de B-7 par le haut (A5), et le retrait
de ce déclencheur a une conséquence sur le verdict d'ensemble, dans le sens favorable, qui n'est pas écrite. Rang « majeure » : jugement
du vérificateur (une déclaration d'effets faite pour être scellée avant toute donnée ne doit pas porter une borne fausse) ; la
correction tient en deux phrases et ne touche ni le code ni le texte gelé. Si la mère tient B-7 pour lue à part et range ce point en
mineure, rien d'autre ne s'oppose au scellement.

## Table des points repris (contre-lecture de la v1)

| point | état dans la v2 | vérification |
|---|---|---|
| majeure 1 (effet de la lecture 1 incomplet) | **corrigée pour B-2 et B-3 ; reste pour B-7** | Écrits et justes : clause `pass` (4 sur 12), clause `r_med` (3 sur 8), B-3 (4 sur 12), « si B-3 ne la porte pas », retrait du déclencheur d'A5, borne en « steer 1x ». Non écrits : les comptes de B-7 demandés par la contre-lecture (3 des 8 couches 8 à 15 ; 2 des 4 couches 26 à 29), remplacés par « même règle sur ses bandes » ; la borne est fausse pour B-7 (point neuf N1). |
| mineure 1 (lecture 2, effet favorable) | corrigée | Phrase d'effet présente ; sonde conforme. Le passage du verdict d'ensemble de « partiel » à « reproduit avec nos lentilles » n'est écrit qu'au niveau de B-2 (point neuf N4). |
| mineure 2 (refus de forme ; effet de la lecture 3) | corrigée | Deux refus de forme repris ; effet « sens sévère » écrit. |
| mineure 3 (heure de la v1) | corrigée | « 05:34 UTC » = `stat` de la v1 (05:34:00). |
| mineure 4 (moment de la partie 2) | corrigée dans l'en-tête ; **reste au § 5** | En-tête : relevé au fil des étapes, à B0 puis avant la première passe d'activations. Le § 5, inchangé, dit encore « nœud à la mère avant la première passe » pour une version de paquet, alors que l'en-tête relève les versions à B0, avant l'ajustement (point neuf N5). |
| mineure 5 (références de la tranche des lentilles publiques) | corrigée | Valeurs citées, égales à la source (voir (3) ci-dessous). |
| mineure 6 (`datasets`) | corrigée | 5.2.0 = ligne 57 de la partie 2 de la tranche des lentilles publiques. |
| mineure 7 (« ne change rien ») | corrigée, parenthèse inexacte | Voir (4) et point neuf N2. |
| mineure 8 (mots en clair) | corrigée en partie, **déclaré comme tel** au § 7 | Nommés : lecture contre pilotage (B-2), avance sur la lentille des logits (B-3), lecture contre ablation (B-7), lecture côté entrée (B-5), audit des deux codes (A6), garde (a), garde des jetons gardés (r), chaîne en défaut (b). Restent en sigle seul : « B-α » (§§ 1.1, 2, 3, 5), « garde (i) » (§ 3), « garde (f) » (§ 1.2, nommée par le titre seulement). |
| mineure 9 (branche) | corrigée | `claude/tender-rubin-mfxjva` aux deux endroits. |

**Diff v1 → v2** (relu ligne à ligne) : titre ; en-tête ; § 1.1 (trois lectures, lectures de forme) ; § 3 (paragraphe des valeurs
attendues à la place de la phrase sur `kept()`) ; § 4 (nom de la branche, une ligne) ; § 5 (`datasets` 5.2.0) ; § 7 ajouté. Rien
d'autre : §§ 1.2, 1.3, 1.4, 2, 6, les tables des §§ 3 et 4 et toutes les empreintes sont inchangés.

## (2) Effets du § 1.1 rejoués par sonde

Entrée : `sain()` (verdict « reproduit avec nos lentilles », B-2, B-3, B-7 « reproduit ») ; couche non lisible = n mis à 47.

| sonde | résultat | conforme au § 1.1 |
|---|---|---|
| `r_med` de notre R à 0,10 aux couches 16 à 23 ; 0, 1 ou 2 couches non lisibles dans 16 à 23 (les 28 paires) | B-2 « non reproduit », verdict « non reproduit avec nos lentilles » | oui |
| même entrée, **3** couches non lisibles dans 16 à 23 (les 56 triplets) | B-2 « autre », verdict « partiel » | oui (« 3 sur 8 suffisent ») |
| même entrée, 4 couches non lisibles dans 24 à 27 | B-2 « non reproduit » : la clause n'est pas neutralisée | oui |
| `pass` à 0,40 aux couches 16 à 27 ; 3 couches non lisibles (les 220 triplets) puis 4 (les 495 quadruplets) | 3 : « non reproduit » ; 4 : « autre », « partiel » | oui |
| écart à la lentille des logits mis à −0,05 aux couches 4 à 15 ; 0 ou 3 couches non lisibles, puis **4** (les 495 quadruplets) | 0 et 3 : B-3 « non reproduit », verdict « non reproduit avec nos lentilles » ; 4 : B-3 « autre », « partiel » | oui |
| B-2 rendue « autre » par 3 couches non lisibles, B-3 « non reproduit » | verdict « non reproduit avec nos lentilles » | oui (« si B-3 ne la porte pas ») |
| « ablate win », `r_med` à 0,45 aux couches 8 à 15 ; 0 ou 2 couches non lisibles, puis **3** | 0 et 2 : B-7 « non reproduit » par le haut, A5 déclenché ; 3 : B-7 « autre », **aucun audit déclenché** | oui (bande 8 à 15 partielle : déclencheur retiré) |
| « ablate win », `r_med` à 0,10 aux couches 26 à 29 ; 1 puis 2 couches non lisibles | 1 : « non reproduit » ; 2 : « autre » | oui (« même règle »), compte non écrit |
| « steer 1x », n = 48, 32, 31 à trois couches de 16 à 23 | 48 : « non reproduit » ; 32 : « autre », « partiel » ; 31 : chaîne en défaut (b) | oui |
| **« ablate win », n = 31 puis n = 0 à trois couches de 8 à 15** | B-7 « autre », A5 non déclenché, **aucune chaîne en défaut** | **non : contredit la borne (N1)** |
| témoin de notre R à 0,07 à deux couches lisibles | B-2 « autre », « partiel » | oui |
| même entrée, l'une des deux couches non lisible | B-2 « reproduit », verdict « reproduit avec nos lentilles » | oui (sens favorable) |
| témoin à 0,12 à une couche non lisible | chaîne en défaut (a) : la garde reste jugée à toutes les couches | cohérent |
| témoin à ±0,12 à la couche 10 d'une moitié, chacune des deux moitiés et des quatre cibles | chaîne en défaut (a), les 8 cas | oui (sens sévère) |
| témoin d'une moitié à 0,10 juste ; à 0,50 à la couche 28 ; `r_med` d'une moitié à 0,10 à la couche 29 | aucun défaut (strictement hors de ±0,10 ; couches 0 à 27 ; la garde (c) ne porte pas sur les moitiés) | cohérent |

**Effets encore non déclarés** : deux, tous deux sur la lecture contre ablation (N1) ; un troisième, déclaré à moitié (N4).

## (3) Valeurs neuves du § 3 et règle « écart = nœud »

Comparées à la partie 2 de la tranche des lentilles publiques, lignes 48 à 57 : `act-dclm.jsonl` `64657ecb…` (l. 48), `act-zh.jsonl`
`c3202db1…` (l. 49), `act-code.jsonl` `550944a2…` (l. 50), `act-chat-llama-3.1-8b-instruct.jsonl` `9dbf9f44…` (l. 51) ; liste
`catalog.kept` : 89 498 identifiants, `c37186add16770aa3c04bd0c16c417544b7e2a15b374ee85e47fbda7ec148d68` (l. 53, entière, égale) ;
`datasets` 5.2.0 (l. 57). **Toutes égales** ; le renvoi « l. 48-53 » est juste.

Règle « un écart n'est pas une chaîne en défaut, il est consigné et soumis à la mère avant la première passe d'activations » :
**compatible** avec le texte gelé.
- La garde des jetons gardés (r) du texte (l. 248-249) compare la liste à « celle consignée après l'unique `03_token_counts.py` », non
  à une valeur d'une autre tranche : un écart à la valeur de la tranche des lentilles publiques n'est donc pas (r). Dire « non chaîne
  en défaut » est exact.
- La liste d'arrêt du texte (l. 546) dit : « empreinte d'un fichier différente de celle écrite ici ou à l'addendum → arrêt ; message
  à la mère ». Une fois ces valeurs écrites à l'addendum, la ligne s'applique ; « consigné et soumis à la mère (nœud) », joint à
  l'en-tête (« tout écart entre les deux parties arrête la course à cette étape »), dit la même chose. Le mot « arrêt » n'est pas
  répété au § 3 (N3).

## (4) « Ajoute seulement des arrêts dans le sens sévère »

**Exacte sur le fond, inexacte dans sa parenthèse.**
- § 1.2 (essai renforcé de l'estimateur) : ajoute des cas qui doivent réussir et quatre artefacts qui doivent échouer, au même
  critère ; tout échec arrête avant l'ajustement. Sens sévère : exact.
- « la version de Drowse, § 5 » : cet arrêt est **déjà** dans le texte gelé (liste d'arrêt, l. 545 ; P.2, l. 341-342). Ce que le § 5
  ajoute, c'est le nœud sur une autre version d'un **autre** paquet. Et le § 3 de la v2 ajoute un second nœud (écart aux valeurs
  attendues), que la parenthèse ne cite pas. Les deux sont bien dans le sens sévère.
- Les lectures 1 et 2 ne sont pas des arrêts et la lecture 2 va dans le sens favorable ; la phrase ne les couvre pas, elle les annonce
  à part (« déclare en clair les lectures ») : pas de contradiction, puisque le texte gelé porte « chaque couche lisible » (l. 168) et
  « une telle bande rend la mesure partielle » (l. 125-126).

## Table des points neufs

| rang | lieu | constat vérifié | correction |
|---|---|---|---|
| **majeure N1** | § 1.1, lecture 1, puces « B-7 » et « bornes » | (i) « L'effet n'existe que pour 32 ≤ n < 48 pôles retenus » est **faux pour la lecture contre ablation (B-7) et pour le déclencheur d'A5** : leurs n sont ceux de « ablate win », que la garde du pilotage sans effet (b) ne regarde pas (elle ne lit que « steer 1x », couches 0 à 27). Sonde : n = 31 ou n = 0 à trois couches de 8 à 15 en « ablate win » → B-7 « autre », A5 non déclenché, aucune chaîne en défaut. Pour B-7, l'effet vit donc pour tout n < 48. (ii) **Conséquence non écrite du retrait d'A5, sur le verdict d'ensemble, dans le sens favorable** : A5 est, avec A1, la seule voie vers la chaîne en défaut (l) (témoin ou pilotage dégénéré, gardes (a) à (c) manquées sous la graine 1). Sonde : même entrée, relance dégénérée — 0 ou 2 couches non lisibles → « chaîne en défaut (l) » ; 3 couches non lisibles → aucun audit, verdict « reproduit avec nos lentilles ». La contre-lecture de la v1 écrivait « sans effet sur le verdict d'ensemble » : inexact par cette voie. (iii) Les comptes de B-7 demandés par la contre-lecture ne sont pas écrits. | Écrire : « B-7 (« ablate win ») : 3 des 8 couches 8 à 15, ou 2 des 4 couches 26 à 29, non lisibles suffisent, pour tout n < 48 (la garde (b) ne lit que « steer 1x ») ; la bande 8 à 15 partielle retire l'audit A5 et, avec lui, la relance à la graine 1 qui peut seule, hors A1, donner la chaîne en défaut (l) : effet possible sur le verdict d'ensemble, dans le sens favorable ». Restreindre la borne 32 ≤ n < 48 à B-2 et B-3. Nouvelle version (R12). |
| mineure N2 | en-tête, parenthèse | « (l'essai renforcé, § 1.2 ; la version de Drowse, § 5) » : l'arrêt sur Drowse est déjà dans le texte gelé ; les arrêts ajoutés sont le nœud sur la version d'un autre paquet (§ 5) et le nœud sur les valeurs attendues (§ 3). | Écrire : « (l'essai renforcé, § 1.2 ; l'écart aux valeurs attendues, § 3 ; la version d'un autre paquet que Drowse, § 5) ». |
| mineure N3 | § 3, dernière phrase | « consigné et soumis à la mère … (nœud) » ne dit pas que la course s'arrête ; seul l'en-tête le dit. Le texte gelé (l. 546) dit « arrêt ; message à la mère ». La fumée `06_activations.py --docs 64` et `lens_compare.py` (qui lit `kept()`) précèdent la passe complète : « première passe d'activations » ne dit pas laquelle. | Écrire « arrêt et nœud à la mère, avant `lens_compare.py` et la fumée de la passe ». |
| mineure N4 | § 1.1, lecture 2 | L'effet est écrit pour B-2 seule ; la sonde montre le verdict d'ensemble passant de « partiel » à « reproduit avec nos lentilles » (correction demandée par la contre-lecture, mineure 1). | Ajouter « et le verdict d'ensemble de « partiel » à « reproduit avec nos lentilles » ». |
| mineure N5 | § 5 contre l'en-tête | § 5 : autre version d'un autre paquet « relevée en partie 2 et nœud à la mère avant la première passe » ; en-tête : versions relevées et comparées à B0, avant l'ajustement, tout écart arrêtant « à cette étape ». Deux moments pour le même écart. | Aligner le § 5 sur l'en-tête (« à B0, avant l'ajustement »). |
| mineure N6 | § 1.1, lecture 1 | « (vérifiés par sonde par le contre-lecteur) » couvre toute la liste, alors que la contre-lecture dit B-7 « lu dans le code, non sondé ». La présente vérification a sondé B-7 (table ci-dessus). | Citer cette vérification pour B-7, ou garder « lu dans le code » pour toute la puce. |

Restes de la reprise, déjà dits dans la première table : sigles seuls (« B-α », « garde (i) », « garde (f) ») ; comptes de B-7.

## Non vérifiable

- Les renvois R-3190, R-3180, R-3171, R-3151, « option (a), recommandée par l'autrice », et les numéros de GO : dans `registres/`, non
  lu par consigne.
- §§ 1.2 à 1.4, 2, 4, 6 et les tables des §§ 3 et 4 : inchangés depuis la v1 (diff) ; non revérifiés ici, ils reposent sur la
  contre-lecture de la v1 (« vérifié sans constat »). Les empreintes de la table « Modèle » de la partie 2 de la tranche des lentilles
  publiques ne sont pas dans les lignes 48 à 57 : non relues.
- Que la tranche produise bien, octet pour octet, les mêmes fichiers `act-*.jsonl` et la même liste `catalog.kept` que la tranche des
  lentilles publiques : dépend du code voisin (non exécuté) et de la machine ; c'est l'objet du nœud du § 3.
- Les effets des lectures sous la relance à la graine 1 de l'audit A1 (une bande partielle sous une seule des deux graines rend la
  mesure « autre ») : lus dans le code, non sondés.
- « Reprise de `verdicts_b_alpha_v3.py` » : fichier d'une autre branche, non ouvert ; repose sur la contre-lecture de la v1.
