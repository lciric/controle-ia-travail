# Provenance des jeux synthétiques de T0.7 — J-D et J-A, dossier `donnees/t07-jeux-synthetiques-v2/` — v2

- **Écrit par** l'agent neuf « assembleur-vérificateur » (Claude Opus 5.5), sous-agent de la session mère
  `session_01QPDgKgACWyCkCN8HjqwNXy`, qui n'a écrit ni T0.7, ni ses jeux, ni leur script, ni leurs contre-vérifications ;
  il a lu des fichiers de T0.7 : **exclu ensuite de tout rôle de lecteur de P3-bis**.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-lot1-jeux-jd-ja-t07-v1.md`
  (`066ca534762924ec47a24b169f581aa8a0c50fa8be73a5534557509f574e37b0`, vérifiée avant lecture) ; interdits communs v2
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés, tenus en entier, règle 9 comprise) ;
  plan : inventaire `docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/inventaire-jeux-t07-v1.md`
  (`c9910a541dbfd80612fbe557a270b02acc99aef3e0f44c8095f676c3c8e0740b`, compagnon conforme), section 5, lot 1, points 1 à 6 ;
  décisions de la mère R-2101 (D-1 (a), D-3 (a), D-5 (a)).
- **Consigne des jeux qui fait foi** : `docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`
  (`d9de50a6f4f7a8add3465ad53a5b894703f70b8777b7f8e428417ebfcd73b485`, compagnon conforme), § 3 et § 10, étape 6.
- **Heures** (`date -u`) : travail commencé le 2026-11-10 à 07:53:10 UTC ; dossier créé à 07:56:14 UTC ; réassemblage à
  07:57:48 UTC ; vérification de 07:58:43 à 08:06:40 UTC ; contrôle de forme à 08:08:30 UTC ; provenance écrite à partir
  de 08:18 UTC ; heure du scellement : celle du compagnon `provenance-v2.md.sha256` (donnée dans le rapport à la mère).
- **Aucun** appel de modèle ni d'interface externe, aucune dépense, aucun `vastai` ; aucune ligne de registre écrite (la
  mère prononce l'acceptation et écrit `SCELLEMENT-JEUX-T07-JD` et `-JA`) ; écriture git : le seul `git fetch` à refspec
  explicite permis, `+refs/heads/donnees/tokeniseur-llama-3.1-8b-instruct-v1:refs/remotes/origin/donnees/tokeniseur-llama-3.1-8b-instruct-v1`
  (la branche `prep/fille-12-t07-v1` était déjà dans le clone, à `bd02ae3e`, non récupérée de nouveau).
- **Jamais ouverts** : tout `lecture-sondes-t06.json` ; la lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/`
  et `runs/` de 7a ; `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
  `docs/notes/bras-attaque/` ; l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; **les textes d'actions de P3**
  (`donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl`), passés au script par leur chemin, leur empreinte lue au journal
  du script. Recherches : `grep` sur des fichiers nommés, `git ls-tree` et `git show` sur des chemins nommés ; aucune
  recherche récursive.

## 1. Fichiers du dossier (chemins relatifs à la racine du clone ; chacun a son compagnon `.sha256`, R6)

| fichier | rôle | sha256 |
|---|---|---|
| `donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl` | **J-D** (320 paires, 640 séquences, 32 tâches) | `32f412888270a3c4b4bc347cf57055bd11b517000feceeaeed122476238ec228` |
| `donnees/t07-jeux-synthetiques-v2/intention-autres-modes-v2.jsonl` | **J-A** (160 « contrôles » + 160 « direction », 640 séquences, 32 tâches) | `5b0409209e66e6c29b69e675c5836cefbef966d9cc0a34412837cae837e2aacf` |
| `donnees/t07-jeux-synthetiques-v2/enonces-reserve-v2.jsonl` | énoncés de la réserve (32 lignes ; `identifiant`, `questions`, `classification`) | `a9e8839f886f9df1ce8270a347151bd11bee0e0742b425edf5914cd5c23d50f8` |
| `donnees/t07-jeux-synthetiques-v2/banque-instructions-v2.json` | annexe A | `230099ef0eece0c11c1ac1a2dfd563e5747292723ddd614eebe7bdbb37d1cc01` |
| `donnees/t07-jeux-synthetiques-v2/banque-incitations-v2.json` | annexe B | `eb6a424d20505819491608e2b8c277735157801bb1230304b5f616922ff91b56` |
| `donnees/t07-jeux-synthetiques-v2/mots-interdits-v2.json` | annexe C | `5d42ab633dd4dda055989a2609fc77e49accdb428f2acdbad0bdbaf9630cba76` |
| `donnees/t07-jeux-synthetiques-v2/journal-verification-v2.txt` | sortie du script officiel, trois jeux, code 0 (§ 8) | `58906bb4c6e609397f5ec0e04e0219314994f4442de641b93536e902233641cb` |
| `donnees/t07-jeux-synthetiques-v2/journal-enonces-annexes-v1.txt` | points 1 et 2 : extraction, égalités (outil recopié) | `867ec52dc9e4361f4045cb4a1a5d90637287d752415be299fdf69153be1e450e` |
| `donnees/t07-jeux-synthetiques-v2/journal-reassemblage-v1.txt` | point 3 : remises, commandes, journaux d'assemblage, garde d'égalité (outil recopié) | `36c2e6cf9928eb3e2e7b41f2199a9cfca2d1a52a5134ce54d673ccbb35db1080` |
| `donnees/t07-jeux-synthetiques-v2/journal-controle-forme-module-v1.txt` | point 5 : contrôle de forme par le module (outil recopié) | `b7f7c439e1ce514567d894de969eaa8d0d94ad4bff55d4fef06c6ee1e40c64c6` |
| `donnees/t07-jeux-synthetiques-v2/rapport-redacteur-jeux-v2.md` | rapport de l'écrivain (§ 12), **compilé**, déclaré comme tel | `31ad362aa584c9b451cfdeb0af443b3e7ad719146173c75777b0080bd6f99158` |
| `donnees/t07-jeux-synthetiques-v2/rapport-contre-verification-v2.md` | **copie à l'octet** du rapport de contre-vérification (§ 9) de la fille 12 | `3fb36d247cc1c96caa92a62c1075f326d7ca2c424b6ae1b53e550975c440f802` |
| `donnees/t07-jeux-synthetiques-v2/cle-contre-verification-v1.json` | **copie à l'octet** de la clé des réponses de la contre-vérification | `a4fb97c3c7026b6bf194140f3c78106b133b7a2c5784ea35a8d879488dfc3921` |
| `donnees/t07-jeux-synthetiques-v2/provenance-v2.md` | ce texte | voir son compagnon |

**Absent de ce dossier, par décision** : `domaine-cout-v2.jsonl` (J-C, version **refusée**, R-1675). Elle reste reproductible
à l'octet depuis `brouillons/t07-jeux-synthetiques-v2-suite-fille12/remises-jc/` r00–r31 (`bd02ae3e`, graine 20261105,
empreinte `6ac5694cd2e4da2ea37cf901013bc22664e5fd1035924925ee7f5e30bf282926`, retrouvée ici) ; elle n'a existé pendant ce lot
que dans un dossier temporaire effacé ensuite ; **elle n'est jamais citée au registre**. J-C réécrit : lot 2, dossier
`donnees/t07-jeux-synthetiques-v3/` (J-D et J-A y seront copiés à l'octet de ce dossier).

Marqueur `<<EMPREINTE_JEUX_SYNTHETIQUES>>` (§ 10, étape 6) : il attend les trois jeux et `provenance-v2.md` ; ce dossier n'en
porte que deux (J-D, J-A) ; le marqueur se remplit quand J-C réécrit est scellé (lot 2), ou selon la décision de la mère.

## 2. Entrées (chemins, empreintes, commits)

| entrée | chemin | sha256 | origine |
|---|---|---|---|
| tâches de réserve (scellé) | `donnees/20261007-082440-t05-extraction/taches-entrainement.json` | `8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd` | `main`, compagnon conforme |
| tâches d'évaluation (scellé, 64) | `donnees/20261007-082440-t05-extraction/taches-evaluation.json` | `76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e` | `main`, compagnon conforme |
| projection des énoncés remise à l'écrivain | `brouillons/t07-jeux-synthetiques-v2-brouillon1/enonces-reserve-projection-ecrivain.jsonl` | `a9e8839f886f9df1ce8270a347151bd11bee0e0742b425edf5914cd5c23d50f8` | égale sur `main` et à `bd02ae3e` ; sans compagnon |
| annexes A, B, C (sources des copies) | `brouillons/t07-jeux-synthetiques-v2-brouillon1/annexes/{banque-instructions,banque-incitations,mots-interdits}-v2.json` | `230099ef…`, `eb6a424d…`, `5d42ab63…` | égales sur `main` et à `bd02ae3e` ; sans compagnon |
| remises (64 fichiers) | listées une à une, avec leur sha256, au point 1 de `journal-reassemblage-v1.txt` | — | branche `prep/fille-12-t07-v1`, commit `bd02ae3e` |
| script de vérification et d'assemblage | `scripts/verifier_jeux_synthetiques_t07_v2.py` | `e53c9c2729cf17ac1b0f3c6fbf81169c1d568bbccb85fb1535981b4094341d22` | égal sur `main` et à `bd02ae3e` ; **sans compagnon** |
| essais du script | `tests/test_verifier_jeux_synthetiques_t07_v2.py` | `8c754af3536c5e769af87a28a9cdb34c749c554c16b1376492d5e9348eeda94d` | `main` ; rejoués pendant ce lot (essai ciblé, `--basetemp` sous le dossier temporaire du lot), de 08:21:20 à 08:21:31 UTC : **66 passés, code 0** (déclaration 6.6) |
| tokeniseur réel de Llama-3.1-8B-Instruct | `donnees/tokeniseur-llama-3.1-8b-instruct-v1/tokenizer.json` | `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` | branche `donnees/tokeniseur-llama-3.1-8b-instruct-v1`, commit `03e3cbd9`, extrait par `git show` hors de l'arbre, empreinte égale à son compagnon |
| textes interdits | `prereg/P3-consignes-v1.md` ; `donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl` | `a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c` ; `ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284` (lue au journal du script) | le second **jamais ouvert** |
| textes d'épisodes de T0.6 | course 7b | — | **absents à la vérification** (non encore produits) : contrôle 9 et remesure des jetons rejoués par la chaîne de T0.7 (consigne v3 § 7 et § 2 ; D-2 (a), R-2101) |
| module de T0.7 (contrôle de forme) | `src/controle_ia/t07/sondes_neuves_v1.py` | `b1c59783ed231c88c5671bc124b0a3f448e5b948b48677db2f361fe6d05c085d` | commit `8dc1cb09` de `prep/t07-module-v2`, `src/` extrait par `git archive` dans un dossier temporaire ; même empreinte aux têtes `d466930b` et `4f929f48` (relevé à 08:09 UTC) |
| clone de travail | `main` | — | commit `a931ec5d` au début du lot |

Graines : **20261105** pour l'ordre des membres (clé « ordre-membres », `SeedSequence` par paire, R9) ; **20261106**
seulement pour l'artefact de la garde d'égalité (R5), jamais versé. Contre-vérification à l'aveugle (§ 9) : entropie
`33841227082728018008930750252386043395`, clés `echantillon-dissimulation` = 1, `echantillon-domaine-cout` = 2,
`echantillon-intention-autres-modes` = 3 (lues dans `cle-contre-verification-v1.json`) ; empreinte de la clé poussée avant le
lecteur (commit `b4ba3be2`, 2026-11-07 11:05:30 UTC ; fichier
`brouillons/t07-jeux-synthetiques-v2-suite-fille12/contre-verification/empreinte-cle-contre-verification-v1.txt`,
`65a7e22b143acd8891130c856a6c4ef2cde651d0252de360c15dee0a9ce9fda3`), égale à l'empreinte de la copie versée ici.

## 3. Ce que ce lot a fait, et ce qu'il a trouvé

1. **Énoncés** (point 1) : extraits du fichier scellé par un outil de la session (`identifiant`, `questions`,
   `classification`, ordre du fichier ; `cibles`, `couts_rapportes`, `empreintes` jamais extraits) ; **égaux à l'octet à la
   projection** remise à l'écrivain (`a9e8839f…`), même contenu ligne par ligne, même ordre ; 32 identifiants, **aucun**
   parmi les 64 tâches d'évaluation. Scellés.
2. **Annexes** (point 2) : copiées à l'octet ; contenu égal, par programme, aux annexes A (quatre cadrages, 20 entrées en
   rotation F1 à F4, quatre de réserve à cadrage nul), B (8 entrées) et C (66 mots, même ordre) de la consigne v3. Scellées.
   Journal : `journal-enonces-annexes-v1.txt`, bilan 0 écart.
3. **Réassemblage** (point 3) : `assembler` du script officiel sur les 64 remises de `bd02ae3e`, graine 20261105, énoncés et
   annexes de ce dossier, réserve scellée : code 0, 0 paire en défaut. **Garde d'égalité** : J-D `32f41288…`, J-A
   `5b040920…`, J-C `6ac5694c…` **égales** aux empreintes du journal final de la fille 12 (`25fdff15…`) ; artefact (graine
   20261106) : les trois **inégales**, garde en code 1 (R5). La contre-vérification du 7 novembre, faite sur l'assemblage
   `full32d` de mêmes empreintes, vaut donc pour J-D et J-A versés ici. Journal : `journal-reassemblage-v1.txt`.
4. **Vérification scellable** (point 4) : `verifier` sans `--jeux` ni `--nombre-taches`, réserve et évaluation **scellées**,
   textes interdits de P3, épisodes de T0.6 déclarés absents, graine 20261105, tokeniseur réel : **code 0**, 0 défaut dur,
   0 réserve ; contrôles fichiers, 1 à 10 et annexes conformes ; aires du sac de mots à 32 plis (réponse entière / avant
   `COST`) : **J-A « contrôles » 0,815 / 0,802 ; J-A « direction » 0,736 / 0,741** ; J-C (refusé) 0,818 / 0,812 ; J-D sans
   objet (réponse identique dans la paire). **Égales au journal `25fdff15…`** : les lignes 20 à 151 des deux journaux sont
   identiques ; seules diffèrent la date, les chemins, les empreintes de la réserve et de l'évaluation (désormais les
   fichiers scellés) et le libellé des épisodes absents. Journal : `journal-verification-v2.txt`.
5. **Contrôle de forme par le module** (point 5) : `lire_jeu` accepte les deux fichiers (640 enregistrements, 320 paires,
   32 tâches chacun ; modes `aucun` ; `controles` et `direction`) ; `controler_disjonction` contre les 64 tâches
   d'évaluation scellées : 0 tâche commune ; trois artefacts refusés (position de `COST` décalée, J-D lu sous la clé de
   J-A, liste d'évaluation augmentée d'une tâche de J-A). Aucune activation, aucun modèle. Journal :
   `journal-controle-forme-module-v1.txt`.
6. **Manques** : **aucun** (32 tâches ; 10 paires de J-D et 5 + 5 de J-A par tâche ; aucune paire retirée ; aucune entrée de
   réserve de l'annexe A utilisée).

## 4. Modèles des sous-agents

| rôle | modèle | source |
|---|---|---|
| orchestratrice de J-D, J-A r00–r17 (et J-A « contrôles » r00–r07 réécrits) | fille 8, Claude Fable 5.1 | `docs/procedures/ordre-fille-12-jeux-t07-v1.md` (`00d87ea5…`) l. 3 |
| écrivains de la fille 8 | **non consigné** dans les pièces lues | — |
| auteur du script de vérification et de ses essais | développeur neuf, Claude Fable 5.1, sous-agent de la fille 8 | `docs/notes/g0-deux-semaines-v1/rapport-verifier-jeux-T0.7-v2-v1.md` (`11408b7c…`) l. 3 |
| orchestratrice de J-A « contrôles » r08–r17, de J-D et J-A r18–r31, des corrections et de la contre-vérification | fille 12, Claude Sonnet 5.5 | rapports v1 à v4 de la fille 12 ; R-1630 ; R-1672 |
| écrivains de la fille 12 (y compris corrections du contrôle 6 et du contrôle 9) | sous-agents neufs, lignée Sonnet | R-1672 ; R-1674 ; `rapport-jeux-T0.7-v2-suite-v4.md` § 2 |
| lecteur de la contre-vérification à l'aveugle | sous-agent neuf, lignée Opus (`model: opus`) | `rapport-contre-verification-v2.md` § 1 ; R-1675 |
| assembleur-vérificateur de ce lot (compilateur du rapport de l'écrivain) | Claude Opus 5.5 | ce texte |

## 5. Écarts à la consigne v3 et leur état (inventaire, section 3)

- **E-1** (vérification « code 0 » sur une réserve de travail et une évaluation factice) : **réparé** ; la vérification de ce
  lot lit les fichiers scellés (`8d20a698…`, `76cdeace…`) et rejoue le contrôle 2 contre les 64 vraies tâches d'évaluation.
- **E-2** (`enonces-reserve-v2.jsonl` jamais extrait ni scellé ; l'écrivain a reçu la projection sans compagnon) : fichier
  **extrait du fichier scellé, égal à l'octet à la projection, scellé ici** ; la remise sans compagnon reste un fait déclaré.
- **E-3** (dossier, copies, journal, rapports, provenance absents) : **réparé** par ce dossier ; `rapport-redacteur-jeux-v2.md`
  est **compilé** depuis les rapports v1 à v4 de la fille 12, le rapport du script et le registre, et déclaré comme tel
  (D-5 (a)) ; `rapport-contre-verification-v2.md` est une copie à l'octet de celui de la fille 12, dont le texte dit encore
  « Non scellé » (il est scellé ici, sans modification).
- **E-4** (écrivains ayant reçu la section 11 et des compléments décidés par la mère, R-1618, R-1660) : **déclaré** ;
  consignes d'écriture `brouillons/t07-jeux-synthetiques-v2-suite-fille12/consigne-ecrivain-fille12-v1.md`
  (`d6236ef8fafe1d5228594c6c7a2c792ddf7b7bc53e10d8fa1faa3d666bcbb9df`) et, pour J-C, `…/consigne-ecrivain-jc-fille12-v1.md`
  (`f97a4d7a7bce27a6aaeaeda1a1ef982257b75ada8a758682c4aa8d7fa4725123`) ; consigne d'écriture des écrivains de la fille 8 :
  non relue ici.
- **E-5** (corrections hors du renvoi unique) : **déclaré** ; quatre corrections de longueur en J-A (r00 p9, r12 p6, r12 p10,
  r22 p6 ; exception à R-1660 déclarée en R-1672, R-1674) et une en J-C (r03 p8, hors de ce dossier) ; trois reformulations
  au contrôle 9 (J-D r08 p4 et r19 p4, J-A r25 p1 membre B ; lecture de la mère, R-1674, R-1675) ; détail dans
  `rapport-redacteur-jeux-v2.md` § 4.
- **E-6** (contre-vérification) : lecteur Opus neuf, clé poussée avant lui ; J-C refusé (25,3 % > 25 %) ; **J-D et J-A
  gardés** (R-1675) ; J-A « contrôles » 16/16, « direction » 15/16, J-D 32 paires sans « non » ; réserve légère du lecteur
  sur JD-20. **D-3 (a)** (R-2101) : la clause « aucun fichier de P3-bis » de l'écrit (a) 2 est constatée tenue en substance
  (consigne du lecteur `be3d8a05…` à liste fermée sans fichier de P3-bis ; déclaration du lecteur) ; aucun nouveau jet.
- **E-7** (contre-lecture neuve du script et de ses essais avant le scellement des jeux, demandée par le rapport du script
  § 7 point 3) : **non faite par ce lot** (hors des sorties de sa consigne) ; décidée en D-5 (a) « pendant le lot 1, sans
  bloquer » : **point ouvert**, à confier par la mère. Ce lot a seulement rejoué les essais du script (tableau du § 2).
- **E-8** (rejeu du contrôle 9 contre les épisodes de 7b et remesure des jetons par la chaîne) : hors de ce lot ;
  décision D-2 (a), au module.

## 6. Déclarations propres à ce lot

1. **La vérification lit J-D et J-A par des liens symboliques.** Le mode `verifier` exige les trois jeux dans un même dossier
   sans `--jeux`, et J-C refusé ne doit jamais entrer dans ce dossier : la vérification a lu le dossier temporaire
   `/home/user/lot1-jeux-tmp/verification/`, où `dissimulation-v2.jsonl` et `intention-autres-modes-v2.jsonl` étaient des
   liens symboliques vers les fichiers **déjà scellés** de ce dossier et `domaine-cout-v2.jsonl` un lien vers le réassemblage
   temporaire ; le journal écrit donc des chemins temporaires, avec les empreintes des fichiers versés ici. Énoncés et
   annexes ont été lus directement dans ce dossier.
2. **Ordre des scellements** : énoncés, annexes, J-D, J-A et le premier journal scellés à 07:58:29 UTC, avant la
   vérification ; journaux de vérification, de réassemblage et de forme scellés après leur écriture ; rapport compilé et
   copies de la contre-vérification à 08:18 UTC ; ce texte en dernier.
3. **Outils de la session** (dans un dossier temporaire effacé à la fin du lot ; texte intégral et empreinte recopiés dans
   les journaux) : `extraire_enonces_annexes_v1.py` (`b8a7d04b67a99cd2f3f82554c2121780d5eca7e0ea2bb7e649cc5d813b758772`),
   `garde_egalite_reassemblage_v1.py` (`821657b36186605693e85fc9a81d36352e08fecd399d1e42695094dea7f38e21`),
   `controle_forme_module_t07_v1.py` (`646a04993428f1065ebcbe1bea61b83eec6a2b4d12d1c8a68996e1700cbc7de1`),
   `comptes_rapport_redacteur_v1.py` (`382afc7aadc2ac9afc940d4b30d1e3df4366d675b1cab5173648a40484c17fce`, texte en annexe du
   rapport compilé). La comparaison des annexes à la consigne (point 2) n'a pas été éprouvée sur un artefact : seules les
   gardes d'empreinte de ses entrées l'ont été implicitement ; la garde d'égalité (point 3) et le contrôle de forme
   (point 5) l'ont été.
4. **Précision sur le journal de forme** : il dit « artefacts en mémoire » ; l'artefact de `lire_jeu` a en fait été écrit
   dans un sous-dossier temporaire de `/home/user/lot1-jeux-tmp/`, effacé à la sortie de l'outil ; rien n'a été écrit dans
   ce dossier.
5. **Lignes attendues au registre** (forme de l'inventaire, 4.3 ; **écrites par la mère seule**, par
   `registre_v1.ajouter_ligne`, après son acceptation) :

       | SCELLEMENT-JEUX-T07-JD | <date -u> | donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl | 32f412888270a3c4b4bc347cf57055bd11b517000feceeaeed122476238ec228 |
       | SCELLEMENT-JEUX-T07-JA | <date -u> | donnees/t07-jeux-synthetiques-v2/intention-autres-modes-v2.jsonl | 5b0409209e66e6c29b69e675c5836cefbef966d9cc0a34412837cae837e2aacf |

   et, dans `registres/decisions.md` à la même date, les aires de J-A (« contrôles » 0,815 / 0,802 ; « direction »
   0,736 / 0,741 ; J-D sans objet). L'ordre d'exécution de l'étape A doit apporter ces deux fichiers et leurs compagnons
   sur l'instance (inventaire, 4.3).
6. **Essais du script, deux lancements** : un premier lancement (08:12:59 UTC, dossier temporaire par défaut de pytest,
   partagé sur la machine) a montré ses 66 essais passés (66 points, 100 %), puis s'est attardé à effacer d'anciens dossiers
   temporaires partagés sur un disque chargé ; je l'ai arrêté par son PID (5426, R10) à 08:21:05 UTC, avant la ligne de
   bilan. Le second lancement, avec un dossier temporaire dédié sous `/home/user/lot1-jeux-tmp/`, fait foi : 66 passés,
   code 0.
