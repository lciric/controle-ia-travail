# Rapport du rédacteur-développeur — étape F de R1 v4, version 2 : corrections K1, K2, K3 (code v8, v9, v5), listes fermées v2, brouillon 2 par scripts — v2

Rapport **additif** : il complète `rapport-developpeur-gardes-analyses-v1.md` (`879d2e9324c851d2b85126820db47a0de1b9aa786ed4bc16288f61fe4613cbe8`),
qui reste valable pour tout ce qui n'est pas repris ici (gardes de réception, déroulé décisif, formats synthétiques).

- **Qui, quand** : second rédacteur-développeur neuf (sous-agent, Claude Fable 5.1), le 5 novembre 2026, de 19:24 à
  20:00 UTC (`date -u`), sur la consigne v2
  `docs/notes/runs-r1-r2-r4-v1/etape-F-v1/consigne-developpeur-gardes-analyses-r1-v4-v2.md`
  (`57b2f9d281c1dc0ab07a6d98714ddae6b2cf812c22bf48bd6daa336a990c4447`, compagnon vérifié) et le brief T2 de la fille 7.
  Je n'ai écrit ni le code v6/v7/v4, ni le brouillon 1, ni la contre-lecture 1, ni les trois analyses, ni l'addendum v4
  de R1, ni la fiche de réception v4.
- **Où** : arbre `/home/user/wt/canal` (branche `canal/conv-audit-n04`, tête `64236ae4` au départ, par-dessus `c82dafeb`) ;
  clone de `main` (`ac37c0ed`) en lecture seule. Écart au texte de la consigne v2 (« aucun commit, aucune poussée »),
  ordonné par la mère à la fille 7 : **commit sur la branche et poussée à chaque jalon** (J1 `4b164694`, puis J2 à J5
  ci-dessous), jamais ailleurs. Aucun `.sha256` écrit ; aucun fichier existant modifié (versions neuves, R12) ; rien sous
  `donnees/` ni `diag/` ; aucune lecture de résultat sous `runs/` (manifestes seuls, pour leurs empreintes et un `grep`
  d'octets) ; aucune commande décisive ; rien d'extrait de `calcul/…` ; aucune clé, aucune dépense, aucun réseau hors
  `git push` sur la branche. Disque : 492 Ko sous `brouillons/etape-F-r1-v4-v1/`, 56 Ko pour le brouillon 2, 90 Ko de
  code et d'essais neufs.
- **Empreintes vérifiées avant d'écrire** : contre-lecture 1 `39d1d035329566e8dbac6bd6a4ee0ad900ce9ed0a37415696e590f4ace087392`
  et ses couples `faafe414747c3cec280dde10a053f935fcebfb13cbbb57dda5857193eead88d4` (compagnons OK) ; brouillon 1
  `5d3ab56c0c6b3faba393624967bce874839eb0cefcb4c7908b7b7d8954e3d245` ; rapport v1 `879d2e93…` ; **les trois empreintes des
  manifestes de la course v3 recalculées sur `runs/` du canal** avant d'être figées (K2) :
  `runs/20261103-072723-analyse-principale-r1-r2-v1/manifeste.json` `0587c398cc05f279251bbe747c3deaff1dee29cb191c94ce30090ce50a5e4643`,
  `runs/20261103-072805-analyse-par-episode-v1/manifeste.json` `79f2a758e0c36f1d4aaa54a78e039ffc802074fe03e222120aff81a78f1a2083`,
  `runs/20261103-072840-analyse-blanche-noire-v3/manifeste.json` `91f711c6eb903ca470b972a953ac12cdde31f211412a5629725895537d550adf`
  (égales à la consigne et à la contre-lecture) ; `grep` des octets sur les 54 manifestes de `runs/` : seuls ces trois
  citent un des trois textes (chemin ou empreinte) ou l'addendum ; aucun manifeste ne cite l'addendum.
- **Conditions d'exécution** : un autre sous-agent occupait la machine (jusqu'à 14 Go de mémoire vive, et le verrou des
  essais pendant de longues minutes) ; deux lancements d'interpréteur ont été tués (code 137, « Memory cgroup out of
  memory ») avant toute écriture ; depuis, chaque lancement attend plus de 4,5 Go disponibles. Aucune conséquence sur les
  fichiers.

## 1. Livrables (chemins et sha256)

Code (versions neuves, R12 ; le code v6, v7, v4 reste dans le dépôt, remplacé, hors des listes fermées, jamais chargé
par les versions neuves) :

| fichier | sha256 | rôle |
|---|---|---|
| `src/controle_ia/analyse_principale_r1_r2/constantes_v8.py` | `2e9b9f3a889b9f76cb83c1aa5090a9d219ebad6f4a66d7cfe74061f9e20b02cf` | constantes v6 + `PASSAGES_V3`, `COMMANDES_ADDENDUM` (K2) |
| `src/controle_ia/analyse_principale_r1_r2/entrees_v5.py` | `d8501b22070519a0e3b025d55ed67b98207a8edab2a04277a3691ee284b7ca7a` | gardes `texte`, `table-comparee`, `provenance`, inchangées, sur `constantes_v8` |
| `src/controle_ia/analyse_principale_r1_r2/lecture_v8.py` | `7697b10a791deec5b97ee9e3e32a6348281e83cfbd9bdc28a35861f0c3c52072` | K1, K2 (`PassageHorsListe`, code de fin 2) |
| `src/controle_ia/analyse_principale_r1_r2/constantes_v9.py` | `2828aed6c753cd6f02e7c9209064ec76dd7e484dbd180b2ddf75671d6c3da172` | constantes v7 sur le bloc v8 |
| `src/controle_ia/analyse_principale_r1_r2/lecture_v9.py` | `4e5bc4fdd0f16de1c1545d19744909e30f3bee28803b0c42f9885a6ee83e6c0c` | K1, K2 (par `lecture_v8`), K3 (`exiger_principale_sous_addendum`) |
| `src/controle_ia/analyse_blanche_noire/constantes_v5.py` | `c384b89ba73a3a833e4f8eeb05dfc6067257a0abbf0cbb8bbb80ffea811e82a5` | constantes v4 + liste close (recopiée) |
| `src/controle_ia/analyse_blanche_noire/entrees_v5.py` | `aa29158fb94bb5d8a6bd1d781a662104483b269f7dc8dd26ad4d77486ade4f25` | gardes inchangées sur `constantes_v5` |
| `src/controle_ia/analyse_blanche_noire/lecture_v5.py` | `c5e6717dbdfa4ce6d5b883d642c3025fc7ebeb9043ab4e53b12b4697e0394834` | K1, K2 (recopié, aucun module du paquet principal) |
| `tests/test_analyse_principale_r1_r2_v8.py` | `be496af0a8373d36c2f8443d097cd2ddb5a63276587945f1fb3cdb008191a5d5` | 4 essais |
| `tests/test_analyse_par_episode_v9.py` | `24703f425e295d5374cf54b0e7d57eb21becdaf0982759886fdc784eec28ebc9` | 3 essais |
| `tests/test_analyse_blanche_noire_v5.py` | `9067232ee5323cbfbcd3595e5aba0e12dd49b2f372f2669e6455e933f5967868` | 4 essais |

Empreintes des constantes citées par le brouillon 2 : principale, code v8
`0546b602a19503969461a08b0973736974baf0d5dc866ad8f277dfa69e51be89` ; par épisode, code v9
`e23108ec0b21268b9b6d5e9d25fb8cc6123422c76f155042cff4913ca2349be5` ; secondaire, code v5
`b8022ea414f07245c2f69535ef018706b85f1f93e873ca56a6dbdfef45991734`.

Brouillon 2 : `prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon2.md`
(`465b5334c4f47f6a1db5e3d757a46420087f0f3219fa3eac858653d048b3000b`) ; marqueurs (motif `<<[A-Z0-9_]+>>`) : exactement
`<<COMMIT_CODE>>` et `<<GO_LAZAR_SECOND_PASSAGE>>`, une fois chacun ; `controle_ia.prereg.problemes` : exactement deux
lignes attendues d'un brouillon 2 (« contre-lecture 2 sans ses deux empreintes » ; les deux marqueurs) ; **les trois
listes fermées du brouillon 2 vérifiées par le code lui-même** (`lecture_v8.exiger_code_cite`, `lecture_v9.exiger_code_cite`,
`analyse_blanche_noire.lecture_v5.exiger_code_cite` sur le texte : 22, 33 et 31 fichiers conformes, constantes égales).

Pièces de `brouillons/etape-F-r1-v4-v1/` (toutes neuves) :

| fichier | sha256 | rôle |
|---|---|---|
| `listes-fermees-generees-v2.md` | `2b2df0f6141210d17bc60e32bfa3adeb1b2ef60b2b301c3cc570c70b0f8fbf01` | les trois blocs (même forme que la v1 : vérifié par `diff` aux versions et empreintes près) |
| `generer-listes-fermees-v2.py` | `571fbf5fbf0a87fdd6ae97b480616a0d7d6723e77eb42f618538a5c987869648` | script qui les engendre depuis les modules |
| `couples-contre-lecture-addendum-gardes-v1.json` | `faafe414747c3cec280dde10a053f935fcebfb13cbbb57dda5857193eead88d4` | copie à l'identique des 15 couples (contre-lecture 1, `main`) |
| `appliquer-couples-v2.py` | `798d9a1f9900566e798608d00d89bba76104c077818eb5a171a131fd9500ce14` | applique des couples dans l'ordre, chaque « ancien » unique au moment de son application (ou un compte déclaré), arrêt sinon ; blocs par fichier |
| `brouillon1-plus-couples-C1-C15-v2.md` | `f1778b92d2f77300e9e9a060d24c6d9a4ebc50f7ee9e7696b2f51c2a2977922b` | sortie du premier script (brouillon 1 + C1 à C15) |
| `journal-couples-C1-C15-v2.md` | `15c7d7d88e3e1f3c168edb68ea6648973c3b9e6d58b97e3a47491ddaf56a0e7d` | journal : 15 couples, 1 occurrence chacun |
| `couples-substitutions-code-v8-v9-v5-v2.json` | `90dfb8b96b26e94ac60f34c2154c2b0a80ef862f26b64ca54742bdee037e1a4f` | second script : 1 bloc (listes) + 33 couples exacts S1 à S33 |
| `journal-substitutions-code-v8-v9-v5-v2.md` | `9efe79fa5776cd3b8ceb84c2522a802c002828cbd53ecfa380bb871b02f598d3` | journal : 34 opérations, 1 occurrence chacune |
| `differences-lecture-v6-v8-brut-v2.diff` | `73f751047ee90eaf54d09602cd5c97beea70aab8c05bd369638f065c74334d4d` | |
| `differences-lecture-v6-v8-hors-renommage-v2.diff` | `efb6e49800a078a828662ffeb4f87a6e91b0460d7b245c2de33b9cdc8aeb9130` | fond : K1, K2, `PassageHorsListe`, code de fin |
| `differences-constantes-v6-v8-brut-v2.diff` | `4397d54f4d421eb785609af18d232c542d6680db4e1c19769569be21cb51dacd` | `PASSAGES_V3`, `COMMANDES_ADDENDUM` |
| `differences-entrees-v4-v5-brut-v2.diff` | `f9b92635786694ffb7263af23d4b17e9770aa2f6ba7741dd9a22b3a0a6619f61` | constantes v8, texte de doc (K1) |
| `differences-lecture-v7-v9-brut-v2.diff` | `32bbe2881a6b7ea0ad35dceb52b70abe0bc535d274ba2455fc351f73d53e59b9` | |
| `differences-lecture-v7-v9-hors-renommage-v2.diff` | `f27610148096136ebe63bc4b5a9aa5cf3195ee3ae62f2fa4ff620ce1c93f416e` | fond : K1, K2, K3 |
| `differences-constantes-v7-v9-brut-v2.diff` | `08d7cc56b7b99c3d9290b6e84623ff3da5e9ba9cb986f0d4f834729a93545070` | |
| `differences-lecture-bn-v4-v5-brut-v2.diff` | `b2b4eb42a5766705b8668450279c8e66899f6b3ed7fc2c3fa398d497c01723c0` | |
| `differences-lecture-bn-v4-v5-hors-renommage-v2.diff` | `1f0a627eabc3fe8b0741168c92560ef501b29f67e2073683651148d9bea531f4` | fond : K1, K2 |
| `differences-constantes-bn-v4-v5-brut-v2.diff` | `1b3dc67c9f3081a8148a3e9ffe8c83bc6acae1db777e20535100c52024289200` | |
| `differences-entrees-bn-v4-v5-brut-v2.diff` | `2c14370c04712a39e196decd9b5519a9408de7922d1c6b360cbcaa5343a56647` | |
| `avancement-v2.md` | (fichier vivant, dernière ligne au commit J5) | |

Différentiels « hors renommage » : version précédente renommée par `sed` (v6→v8, K6→K8, `entrees_v4`→`entrees_v5`,
essai v6→v8 ; v7→v9, K7→K9, L6→L8, idem ; secondaire : v4→v5, C4→C5, « version 4 »→« version 5 », `analyser_v4`→`analyser_v5`,
`issue_v4`→`issue_v5`, `exiger_premier_passage_v4`→`_v5`), puis `diff -u` : il n'y reste que les changements de fond.

## 2. Ce qui a été fait (K1, K2, K3) et pourquoi ainsi

1. **K1** (`lecture_v8.analyser`, `lecture_v9.analyser`, `lecture_v5.analyser_v5`) : `exiger_reception_v4` est appelée
   **juste après `lire_fiche` (resp. `lire_fiche_v3`)**, si R1 est livré, **avant** `charger_p3`, `longueurs_textes`,
   `charger_r1`, les juges (principale, par épisode), avant `lire_principale` (par épisode) et avant `charger_run_v3`,
   `charger_activations_v3`, le juge (secondaire). Les gardes ne dépendent que du chemin du résultat cité par la fiche
   (`verifier_resultat`, `lire_manifeste` : fichiers JSON seulement). Essai : `numpy.load` remplacé par un piège qui lève
   tant que la garde n'a pas rendu et compte ses appels ; artefact de provenance → arrêt « garde provenance », zéro appel,
   rien d'écrit ; cas sain → zéro appel avant la garde, des appels après ; rejeu non validé → zéro appel. Les trois
   lectures ont le même essai.
2. **K2** (`lecture_v8.exiger_premier_passage_sous`, recopié dans `lecture_v5.exiger_premier_passage_v5` ; `lecture_v9`
   appelle celui de `lecture_v8`) : constantes gelées `PASSAGES_V3` (les trois runs → empreinte sha256 des octets de
   `manifeste.json`) et `COMMANDES_ADDENDUM` (`lecture_v8`, `lecture_v9`, `analyse_blanche_noire.lecture_v5`) dans
   `constantes_v8`, recopiées dans `analyse_blanche_noire.constantes_v5` (le paquet secondaire ne charge aucun module du
   paquet principal ; égalité des deux copies éprouvée). Règle, pour chaque manifeste sous `runs/` (octets lus) : ne cite
   ni le texte (chemin ou empreinte, règle des textes) ni l'addendum → ignoré, même illisible ; illisible et cite l'un
   des deux → arrêt ; cite l'addendum → commande propre : arrêt (second passage), commande sœur gelée : toléré, autre :
   arrêt ; cite le texte sans l'addendum → toléré seulement si `PASSAGES_V3[run]` = empreinte des octets, sinon arrêt.
   `passages` écrit `manifestes_lus`, `autres_analyses_sous_l_addendum`, `passages_anterieurs_du_texte_hors_addendum`
   et **`toleres`** (noms, dans l'ordre des dossiers). **Code d'arrêt distinct** : `PassageHorsListe(GardeArret)`, pris
   par `_main` avec le code de fin **2** (les autres gardes : 1) ; chaque message nomme le manifeste et se termine par
   « nœud de Lazar ». Les constantes gelées sont comparées, dans les essais, aux manifestes réels de `runs/` du dépôt
   (empreintes égales), et les cas sains et artefacts tournent sur des manifestes jouets dont l'empreinte est injectée
   par `monkeypatch` dans `PASSAGES_V3` (altérer `PASSAGES_V3` change l'empreinte des constantes, d'où les artefacts de
   liste passés par la garde directe quand l'addendum jouet cite déjà les constantes).
3. **K3** (`lecture_v9.exiger_principale_sous_addendum`, mode décisif seulement, après `lire_principale`, avant tout
   chargeur) : `version` = `constantes_v8.VERSION`, `lien_au_preenregistrement.addendum.sha256` = empreinte de l'addendum
   scellé, `reception_v4.run_rejeu` égal à celui reçu par cette lecture (ou tous deux nuls) ; écrit sous
   `principale.sous_addendum` (nul hors mode décisif). Essais : cas sain de bout en bout (principale v8 décisive, puis
   par épisode v9 décisive) ; artefacts sur le résultat scellé de la principale (version v7, autre addendum, autre rejeu,
   rejeu nul d'un côté).
4. **Rien d'autre ne change** : calcul, issue, rendu, graines, plis, listes fermées des versions précédentes vérifiées sur
   les textes, gardes de réception (les deux `entrees_v5` ne diffèrent de `entrees_v4` que par le module de constantes et
   une phrase de documentation). Les listes fermées neuves sont celles des versions précédentes des textes plus les
   modules neufs (22, 33, 31 fichiers, mêmes comptes qu'au brouillon 1) ; les modules v6, v7, v4 n'y figurent pas.

## 3. Traitement des seize points de la contre-lecture 1 et des quinze couples

| point | gravité | traitement |
|---|---|---|
| 1 gardes conformes | note | rien à changer ; `entrees_v5` = `entrees_v4` au module de constantes près |
| 2 rien d'autre ne change | note | tenu : différentiels hors renommage v2 ne montrent que K1, K2, K3 |
| 3 listes fermées exactes | note | regénérées par script (section 1), vérifiées par le code sur le brouillon 2 |
| 4 listes d'arrêt « inchangées » | à corriger | C1, C13 appliqués |
| 5 second passage non borné | bloquant | K2 (liste close) ; C10, C11, C14, C15 appliqués ; marqueur `<<GO_LAZAR_SECOND_PASSAGE>>` en tête |
| 6 lisibilité et borne | à corriger | C3, C12 appliqués ; S33 (code v8, v9, v5 dans C12) |
| 7 place des gardes | à corriger | K1 ; C8, C9 appliqués |
| 8 essais conformes | note | essais neufs pour K1, K2, K3 (section 4) |
| 9 commit cité | à corriger | C5 appliqué ; S4 (en-tête) |
| 10 lecture entre les commandes | à corriger | C7 appliqué ; commandes de la section 5 avec journal non affiché |
| 11 récupération | à corriger | C2, C4 appliqués ; S5 (« extraction » dans le Statut) |
| 12 préalable de réception | à corriger | C6 appliqué ; section 5, préalable |
| 13 nom du run de la réparation | note | inchangé (constante gelée) ; à revérifier au `checkout` par la mère |
| 14 K3 | note (facultatif) | fait (`lecture_v9`) ; S23 (Plan, point 5), S28 (point 8), S29 (liste d'arrêt) |
| 15 arrêt technique après le manifeste | note | dans C12 (appliqué) |
| 16 critères 3 et 4 de G0 | note | S28 : le verdict R13 lit `passages.toleres` contre la liste close et `principale.sous_addendum` |

Couples C1 à C15 : tous **acceptés**, appliqués dans l'ordre par `appliquer-couples-v2.py` (chaque « ancien » trouvé une
fois au moment de son application ; journal). Aucun couple n'a touché une empreinte. Les substitutions S1 à S33
(second script, couples exacts, une occurrence chacun ; bloc B1 pour les trois listes) sont listées avec leur motif dans
`couples-substitutions-code-v8-v9-v5-v2.json` ; en résumé : en-tête (titre, auteur, date, commit cité, ligne d'écart
avec marqueur, statut), chemins gelés v8/v9/v5, commandes décisives, modules et essais des trois blocs « avant → après »,
tests attendus, point 2, point 3.b et 3.c (titres, constantes `PASSAGES_V3` et `COMMANDES_ADDENDUM`, arrêt distinct),
point 5 (K3), point 7 (essais K1, K2, K3 ; comptes ; commande), point 8 (verdict), liste d'arrêt (arrêt distinct, K3),
limites (liste close gelée), marqueurs (deux), section « Contre-lecture » (entrée 1 écrite avec les deux empreintes et le
traitement ; entrée 2 à faire). Décision prise seul, à contre-lire : les couples C1 à C15 ont été appliqués **tels
quels**, puis seules les mentions de versions, d'empreintes et de comptes ont été substituées ; les phrases neuves (S4,
S22, S23, S25, S28, S29, S30, S31, S32) ne disent que ce que le code fait.

## 4. Essais (R5) : comptes

Environnement gelé `.venv` du dépôt principal (Python 3.13.18, numpy 2.4.6, scipy 1.17.1), `PYTHONPATH=src:tests`,
`-p no:cacheprovider`, `nice -n 10`, une suite à la fois sous `flock /home/user/wt/.pytest.lock`, données synthétiques
seulement. Commande, pour chaque suite `S` :
`flock /home/user/wt/.pytest.lock timeout 900 nice -n 10 python -m pytest -q -p no:cacheprovider tests/S.py`.

Essais neufs :

| fichier | essais | résultat | durée |
|---|---|---|---|
| `tests/test_analyse_principale_r1_r2_v8.py` | 4 | réussis | 5 s |
| `tests/test_analyse_par_episode_v9.py` | 3 | réussis (après deux corrections d'essai, section 2.2) | 8 s |
| `tests/test_analyse_blanche_noire_v5.py` | 4 | réussis | 12 s |

Essais anciens rejoués (une suite à la fois ; durée pytest, hors attente du verrou) :

| fichier | essais | résultat | durée pytest |
|---|---|---|---|
| `tests/test_analyse_principale_r1_r2_v1.py` | 20 | réussis | 15 s |
| `tests/test_analyse_principale_r1_r2_v2.py` | 4 | réussis | 7 s |
| `tests/test_analyse_principale_r1_r2_v6.py` (brouillon 1) | 4 | réussis | 13 s |
| `tests/test_analyse_par_episode_v1.py` | 12 | réussis | 10 s |
| `tests/test_analyse_par_episode_v2.py` | 18 | réussis | 22 s |
| `tests/test_analyse_par_episode_v7.py` (brouillon 1) | 3 | réussis | 5 s |
| `tests/test_analyse_r2_seul_v1.py` | 13 | réussis | 9 s |
| `tests/test_analyse_blanche_noire_v1.py` | 12 | réussis | 22 s |
| `tests/test_analyse_blanche_noire_v2.py` | 11 | réussis | 22 s |
| `tests/test_analyse_blanche_noire_v3.py` | 13 | réussis | 26 s |
| `tests/test_analyse_blanche_noire_v4.py` (brouillon 1) | 4 | réussis | 11 s |

Essais anciens : **114 réussis sur 114** (principale v1, v2, v6 : 28 ; par épisode v1, v2, v7 : 33 ; R2 seul v1 : 13 ;
secondaire v1, v2, v3, v4 : 40), de 19:43 à 19:57 UTC (attentes du verrou comprises). Essais neufs : **11 réussis sur
11**. Tests attendus écrits au brouillon 2 : principale 28 (20 + 4 + 4), secondaire 17 (13 + 4), lecture par épisode 61
(12 + 18 + 3 + 28) ; la suite complète du dépôt (`tests/`) n'a pas été relancée (machine partagée).

Ce que les essais neufs éprouvent, en plus de ceux du brouillon 1 (repris : gardes de réception, même calcul que la
version précédente, rejeu non validé, mode décisif, liste fermée, fermeture des importations) : K1 (piège sur
`numpy.load`, trois lectures) ; K2 (constantes gelées égales aux manifestes réels ; cas sain avec les trois manifestes
jouets gelés et une sœur sous l'addendum ; quatrième manifeste qui cite le texte ; toléré à l'empreinte gelée autre ;
toléré aux octets réécrits ; commande inconnue sous l'addendum ; manifeste illisible citant le texte, puis l'addendum ;
manifeste étranger illisible ignoré ; second passage ; `PassageHorsListe` sous-classe de `GardeArret`, `CODE_FIN_PASSAGE`
= 2 ; `toleres` par nom) ; K3 (unitaire et de bout en bout).

## 5. Commandes exactes pour la mère (conv-audit), dans l'ordre

Préalables (nœuds et registres) : contre-lecture 2 (R2, sous-agent neuf) du brouillon 2 et du code v8, v9, v5 ;
traitement ; brouillon final ; **GO de Lazar sur l'écart déclaré** (second passage, borné par K2 : marqueur
`<<GO_LAZAR_SECOND_PASSAGE>>` remplacé par la référence du GO) ; empreinte du brouillon final au registre, poussée ;
**réception v4 conforme** (C6) : `verifier_reception_r1_v4_v1.py` en code 0, recalcul de la table égal à l'octet (fiche
v4, section 7), consignée au registre avec ce qui a été vu (fiche v4, section 6) — sans cela, aucune commande décisive.

1. **Commit cité, scellement** (branche `canal/conv-audit-n04` ; `<N>` = numéro du brouillon final ; `<GO>` = référence
   du GO de Lazar) :
   ```
   git add src/controle_ia/analyse_principale_r1_r2/constantes_v8.py src/controle_ia/analyse_principale_r1_r2/entrees_v5.py \
     src/controle_ia/analyse_principale_r1_r2/lecture_v8.py src/controle_ia/analyse_principale_r1_r2/constantes_v9.py \
     src/controle_ia/analyse_principale_r1_r2/lecture_v9.py src/controle_ia/analyse_blanche_noire/constantes_v5.py \
     src/controle_ia/analyse_blanche_noire/entrees_v5.py src/controle_ia/analyse_blanche_noire/lecture_v5.py \
     tests/test_analyse_principale_r1_r2_v8.py tests/test_analyse_par_episode_v9.py tests/test_analyse_blanche_noire_v5.py \
     prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon<N>.md brouillons/etape-F-r1-v4-v1
   git commit -m "Addendum 1 gardes des analyses (R1 v4) : code v8, v9, v5 et essais, brouillon final"   # commit cité, ni amendé ni refait
   C=$(git rev-parse HEAD)
   sed -e "s/<<COMMIT_CODE>>/$C/" -e "s/<<GO_LAZAR_SECOND_PASSAGE>>/<GO>/" prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon<N>.md > prereg/addendum-1-gardes-analyses-r1-v4-v1.md
   diff prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon<N>.md prereg/addendum-1-gardes-analyses-r1-v4-v1.md   # deux lignes
   PYTHONPATH=src .venv/bin/python -c "from controle_ia.prereg import problemes, sceller_prereg; p='prereg/addendum-1-gardes-analyses-r1-v4-v1.md'; assert problemes(p) == [], problemes(p); print(sceller_prereg(p))"
   PYTHONPATH=src .venv/bin/python -c "from controle_ia.analyse_principale_r1_r2 import lecture_v8 as A, lecture_v9 as B; from controle_ia.analyse_blanche_noire import lecture_v5 as C; t=open('prereg/addendum-1-gardes-analyses-r1-v4-v1.md', encoding='utf-8').read(); print([len(m.exiger_code_cite(t)['fichiers']) for m in (A, B, C)])"   # [22, 33, 31]
   git add prereg/addendum-1-gardes-analyses-r1-v4-v1.md prereg/addendum-1-gardes-analyses-r1-v4-v1.md.sha256 && git commit -m "Addendum 1 gardes des analyses scellé" && git push origin HEAD:refs/heads/canal/conv-audit-n04
   ```
   (Si le commit cité porte d'autres fichiers du brouillon 2, par exemple les listes v2 et les journaux, le code cité ne
   change pas : seules les empreintes des onze fichiers de code et d'essais sont gelées.)
2. **Arbre séparé, environnement, essais** : comme au rapport v1, section 5.2, avec les suites
   `tests/test_analyse_principale_r1_r2_v1.py tests/test_analyse_principale_r1_r2_v2.py tests/test_analyse_principale_r1_r2_v8.py
   tests/test_analyse_par_episode_v1.py tests/test_analyse_par_episode_v2.py tests/test_analyse_par_episode_v9.py
   tests/test_analyse_blanche_noire_v1.py tests/test_analyse_blanche_noire_v2.py tests/test_analyse_blanche_noire_v3.py
   tests/test_analyse_blanche_noire_v5.py` : 101 réussis attendus.
3. **Récupération par refspec, seuls chemins** : comme au rapport v1, section 5.3 (`git fetch origin calcul/r1-r2-reel-v1`,
   `git checkout FETCH_HEAD -- <chemins>`, `.npz` par `git show` hors index, compagnons vérifiés sans ouvrir aucun `.npz`,
   témoin non récupéré) ; vérifier que le nom du run de la réparation est bien `20261104-234729-r1-v4-reparation-reel`
   (point 13 ; un autre nom arrête, à bon droit). **Préalable C6** après le versement : réception v4 conforme, consignée.
4. **Fiches de réception** : comme au rapport v1, section 5.4 (noms neufs, mêmes formats, aucun nombre de résultat).
5. **Commandes décisives** (chacune depuis la racine de l'arbre séparé, arbre propre ; **sorties standard et d'erreur
   redirigées vers un journal non affiché ; seul le code de fin est lu avant la commande suivante** ; sur code non nul,
   le seul message d'arrêt est lu — ligne `ARRÊT`, il ne porte aucune valeur ; journal scellé et committé avec les
   sorties ; **aucune issue lue avant que les trois sorties soient committées et poussées**, C7) :
   ```
   mkdir -p journaux
   R1=$(date -u +%Y%m%d-%H%M%S)-analyse-principale-r1-r2-v1
   PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_principale_r1_r2.lecture_v8 --fiche prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json --run-analyse $R1 --prereg prereg/analyse-principale-r1-r2-v1.md > journaux/$R1.log 2>&1 ; echo "code de fin : $?"
   # 0 : continuer ; 2 : passage hors liste close (K2), nœud de Lazar ; 1 : autre garde — dans les deux cas : grep -m1 '^ARRÊT' journaux/$R1.log, rien d'autre, signaler à Lazar
   PYTHONPATH=src python -m controle_ia.scellement sceller journaux/$R1.log
   git add runs/$R1 diag/$R1 journaux/$R1.log journaux/$R1.log.sha256 && git commit -q -m "Analyse principale R1-R2, course v4 (code v8)"
   R2=$(date -u +%Y%m%d-%H%M%S)-analyse-par-episode-v1
   PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_principale_r1_r2.lecture_v9 --fiche prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json --principale diag/$R1/analyse-principale-r1-r2-v1.json --run-analyse $R2 --prereg prereg/analyse-par-episode-v1.md > journaux/$R2.log 2>&1 ; echo "code de fin : $?"
   PYTHONPATH=src python -m controle_ia.scellement sceller journaux/$R2.log
   git add runs/$R2 diag/$R2 journaux/$R2.log journaux/$R2.log.sha256 && git commit -q -m "Lecture par épisode R1-R2, course v4 (code v9)"
   R3=$(date -u +%Y%m%d-%H%M%S)-analyse-blanche-noire-v3
   PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_blanche_noire.lecture_v5 --fiche prereg/fiche-reception-blanche-noire-v3-relance-v4.json --run-analyse $R3 --prereg prereg/analyse-blanche-noire-v3.md > journaux/$R3.log 2>&1 ; echo "code de fin : $?"
   PYTHONPATH=src python -m controle_ia.scellement sceller journaux/$R3.log
   git add runs/$R3 diag/$R3 journaux/$R3.log journaux/$R3.log.sha256 && git commit -q -m "Analyse secondaire R1-R2, course v4 (code v5)"
   git push origin HEAD:refs/heads/analyses-r1-v4
   ```
   Ordre : principale (code v8) ; lecture par épisode (code v9 : K3 exige la principale v8 sous l'addendum et le même
   rejeu) ; secondaire (code v5). Les journaux ne contiennent que `{"issue": …}` sur succès : ils ne sont ouverts qu'après
   la poussée des trois sorties. Puis `git merge` (jamais de rebasage) dans la branche de travail, poussée ; verdict R13
   par un sous-agent neuf, qui lit aussi `reception_v4`, `lien_au_preenregistrement.passages` (dont `toleres` contre la
   liste close) et `principale.sous_addendum`.

## 6. Reproduire les listes fermées du brouillon 2

`PYTHONPATH=src .venv/bin/python brouillons/etape-F-r1-v4-v1/generer-listes-fermees-v2.py` : sortie égale, à l'octet, à
`listes-fermees-generees-v2.md`, qui est le bloc B1 du brouillon 2 (de la ligne « Empreinte des constantes (analyse
principale, code v8) » à la ligne avant « ## Critères de lecture gelés »). Reproduire le brouillon 2 :
`python3 -I brouillons/etape-F-r1-v4-v1/appliquer-couples-v2.py prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon1.md
brouillons/etape-F-r1-v4-v1/couples-contre-lecture-addendum-gardes-v1.json <sortie1> <journal1>` puis la même commande
avec `<sortie1>`, `couples-substitutions-code-v8-v9-v5-v2.json`, `<sortie2>`, `<journal2>` : `<sortie2>` ne diffère du
brouillon 2 que par rien (la date du brouillon 2 est dans le couple S3, figée).

## 7. Réserves et trois risques

1. **Code de fin 2 non éprouvé par sous-processus** : les essais vérifient `PassageHorsListe` (sous-classe de
   `GardeArret`), `CODE_FIN_PASSAGE == 2` et le bloc `__main__` est le même dans les trois lectures, mais aucun essai ne
   lance `python -m … lecture_v8` dans un dépôt jouet jusqu'au code de fin (les gardes du mode décisif exigent le code
   importé sous la racine, `exiger_code_importe_sous`, non simulable hors processus sans artifice). La mère lit le
   code de fin ; un 1 là où un 2 était attendu ne change pas l'arrêt, seulement son nom.
2. **Liste close et manifestes futurs** : tout manifeste nouveau sous `runs/` qui cite un des trois textes par chemin ou
   empreinte (par exemple une course de R1 future, ou un run d'un autre outil qui recopierait le chemin d'un texte dans sa
   configuration) arrête les trois lectures ; c'est voulu (K2), mais la mère doit lancer les commandes dans l'arbre séparé
   au commit du scellement, sans autre manifeste ajouté. De même, la citation d'un texte « dans les octets » inclut les
   constantes des manifestes (la lecture par épisode de la course v3 cite le chemin du texte principal par
   `PREREG_PRINCIPALE`) : couvert par la liste close, mais une constante nouvelle citant un texte dans un manifeste
   d'une autre lignée arrêterait aussi.
3. **Brouillon 2 écrit par scripts, non relu par un tiers** : les phrases neuves (S4, S22, S23, S25, S28 à S32) et la
   section « Contre-lecture » (entrée 1 : traitement, verdict) sont de ma main et décrivent le code ; la contre-lecture
   2 doit les relire contre le code v8, v9, v5 et contre la contre-lecture 1 ; le brouillon 2 cite les empreintes des
   essais neufs : tout changement d'essai exigerait de regénérer les listes (section 6) et le brouillon. Le rendu de la
   lecture par épisode garde le titre « (code v5) » et écrit « (code v9) » à côté (réserve v1 maintenue).
