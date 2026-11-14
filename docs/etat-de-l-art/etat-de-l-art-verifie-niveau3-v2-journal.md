# Journal de la synthèse de l'état de l'art vérifié de niveau 3 — v2

Écrit le 2026-11-14, de 00:31:35 UTC (début de la lecture) à 2026-11-14 à 00:58:39 UTC (heures relevées par `date -u`). Auteur : sous-agent neuf, modèle A. Compagnon de `etat-de-l-art-verifie-niveau3-v2.md`. Mandat : synthèse v2 assemblant les rapports du compte 2 et appliquant la contre-lecture de la v1, transmis par la session qui m'a lancé.

## 1. Consignes tenues

- Consigne commune du compte 2 : `docs/sources/lecture-pdf-niveau3/compte-2/consignes-compte-2-v1/consigne-lecteur-compte-2-v1.md`, sha256 recalculé `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5`, égal à l'attendu ; lue en entier. Interdits communs v2 (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`), nommés par la consigne, lus en entier ; le plus strict tenu.
- Avant d'écrire : `ls` du seul dossier `docs/etat-de-l-art/` : aucun des trois fichiers de sortie n'existait (vérifié au début, puis de nouveau juste avant l'écriture).
- Aucune commande git, aucun appel réseau, aucun appel de modèle, aucune dépense, aucune valeur de clé. Aucune recherche récursive dans le dépôt. Aucune suppression. Rien ouvert sous `registres/`, `diag/`, `runs/`, `donnees/` ; rien de T0.7, de 7a ni de 7b. L'index nomme des journaux sous `registres-provisoires/` : non ouverts.
- Aucun nom ni identifiant de modèle du programme écrit dans un fichier ; j'ai évité aussi les noms des modèles étudiés par les articles. Une méthode d'attaque dont le nom contient celui d'une famille de modèles est désignée par son identifiant arXiv.

## 2. Sources et empreintes (toutes recalculées par `sha256sum`, toutes égales à leur compagnon `.sha256` et, pour le compte 2, à l'index)

| fichier | sha256 |
|---|---|
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` | `e30a013d08b03e8ddc07637b186e38e2051bd221958b713cc27facd1abf45892` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-journal.md` | `b9511aeaa92662a1ba8ba038cf1f223d328c70cd238423835c631aa751486780` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` | `f1580ddcedd495b5ce46391620f0d49ccf309d81f6ff1960cc5f4835776e5430` |
| `docs/decisions/decision-N-068-v1.md` | `ba6b2db355515cd660d676b733f4d467f8a9c055d4d8c6d997d4ef898caef889` |
| `docs/decisions/decision-N-069-v1.md` | `6e0d9d4036a848a67e0f5e14c1ed9b107c6ba1aa1041ab09ad73af69c427c370` |
| `docs/decisions/decision-N-070-v1.md` | `7c4ce2210b2e48db4f8349ed85cd50387586b3eb176d364be0d280647d25992f` |
| `compte-2/index-rapports-compte-2-v1.md` | `51f71174e00880362a195de0967f661c9a2559dd5c6ce20a3ca5331bf93698c2` |
| `compte-2/rapport-L-lot8-v2.md` | `8d9f2654f904454a7729f9f133bfd73a4ace916865a4efac7b90f5dba816bdc5` |
| `compte-2/rapport-T-lot8-v2.md` | `6d9d354a174ea1518d8b892428bc1d0c7ebc8fb5d60b796a5043ea96011a0ce6` |
| `compte-2/rapport-H6-v2.md` | `ff3b13a11aa9ba35eb9014ac2d7097f9cb2ede6d48f2cc5388c342cf34c4481a` |
| `compte-2/rapport-HC5-v2.md` | `6d19844335781289200d05d6b6034fab833a07a206670c25c307a637a6cfacec` |
| `compte-2/rapport-HC1-2607.00415-v2.md` | `0658406424181171b1c28dd168479fbd2beaa135f52d16659a9e2d511d962cc6` |
| `compte-2/rapport-HC6-v2.md` | `076ffddb1c75f2e2eb69b27218e6a7f96bae45c413d6601a711fffe3182b91cf` |
| `compte-2/rapport-Tr-v2.md` | `139596cfcfbc77765e69e705b0990fba38432da0552e3c1c42687691378174dc` |
| `compte-2/rapport-HC4-v2.md` | `6c368ebb74301a5b2cdcd047f641a0f516f67af371a10359350e7871c4ced948` |
| `compte-2/rapport-H1-v2.md` | `8b4b43f53a21c944c49a1f2cca7245598925854d0f7671b6c86740297f0060fd` |
| `compte-2/rapport-H2-v2.md` | `f801ee845437fb321a3f743460121430b71345ca5f7bb10537be847077a889a7` |
| `compte-2/rapport-papierB-v2.md` | `1c3033ba6d507b1eae6a1683408db1338008d702ddf23b2e8fc917e4cfae181a` |
| `compte-2/rapport-4B-partie1-v2.md` | `2fcefa4a5ce08db435eea08e30697a9354e608ef3d1b367a171078dcdc8bfe03` |
| `compte-2/rapport-4B-partie2-v2.md` | `c1708b9c82f8a78318a8817201f1fd5af68964fae6c52026f7e86510dd4e9f72` |
| `compte-2/contre-lecture-rapport-L-lot8-v1.md` | `4083822e6cb35bf9051975e64a87dfd5e1ca1ceab8d74c0d81b3994a9beb6a83` |
| `compte-2/contre-lecture-rapport-T-lot8-v1.md` | `3f950c920f54ede9e195b521af437cc2423764175611ab49479cd42099a89883` |
| `compte-2/contre-lecture-rapport-H6-v1.md` | `3ce3ac3cf73ea481dd7d04f411d9a30d74f6a0489f531d1cfa24d40f4825666e` |
| `compte-2/contre-lecture-rapport-HC5-v1.md` | `e241a0e0ef0d2b438c3755dce70686862dae10c08fbbf8322358908236a7da1c` |
| `compte-2/contre-lecture-rapport-HC1-2607.00415-v1.md` | `e4beb545a16af90bf07e4b09e4f8995832a27c0e5d40abddc699aea69aba8738` |
| `compte-2/contre-lecture-rapport-HC6-v1.md` | `87e1699c995de30e95dfb230f221c148d3fdfe45bfca8d1e7192ba9fabb6f48c` |
| `compte-2/contre-lecture-rapport-Tr-v1.md` | `2a530bfe34f97a3c5a00677d839e865439ebc6c6fefba7ec20d8413e5425cb44` |
| `compte-2/contre-lecture-rapport-HC4-v1.md` | `8fa4ab9baf757af42f44255b484c3b0ca865fc8b887c6c01bf4755473847e5b0` |
| `compte-2/contre-lecture-rapport-H1-v1.md` | `024f84a9440a0b273b5ec924a78c22ad43abcc87e2e010c5b203f8189675b0bf` |
| `compte-2/contre-lecture-rapport-H2-v1.md` | `708b48c23f0e116071c05edca5075c97a10306f0dbc08b2dcff5f13471bf1def` |
| `compte-2/contre-lecture-rapport-papierB-v1.md` | `fe25d39ffc77b65132325cd1b136c353c8e6292397d4dd19bf30cf910f749301` |
| `compte-2/contre-lecture-rapport-4B-partie1-v1.md` | `e9c5ad74cc5c6483c42916dc0ebc137f64d436fe3d88b26a368ec6373be10cf0` |
| `compte-2/contre-lecture-rapport-4B-partie2-v1.md` | `66127a9ccf390758827b6959581adf2f0c171e67db29f8a4da3244b381a64a85` |
| `compte-2/fichiers-de-travail-L-lot8-v2.tar` | `7f019f517946eb49663b9e5a66bd8c2d644192aa5caebf57097221bc5a838a5a` |
| `compte-2/fichiers-de-travail-T-lot8-v2.tar` | `86e8d707844497941d4e01f41052ce78e88af1207ca32d532185b97a385d8de8` |
| `compte-2/fichiers-de-travail-H6-v2.tar` | `20ee73a6319eb769978a160f02e6d6255f83735b0efcd9d22c40d6a5fceb5eb8` |
| `compte-2/fichiers-de-travail-HC5-v2.tar` | `a4db3b60a69a9e0494d53cdd10bb587f047f8c640cb8a10aaa87094a4f376ac4` |
| `compte-2/fichiers-de-travail-HC1-2607.00415-v2.tar` | `2fb9285626e5cc6596d3f77cada61ee9ea3eca7a1b9e51c315bba2bdcb2b370e` |
| `compte-2/fichiers-de-travail-HC6-v2.tar` | `74584a8e5b02e552eca96c624b2573458a18ebb4110593181e851f6233cd6fe4` |
| `compte-2/fichiers-de-travail-Tr-v2.tar` | `a944cda0b50f099b8db7d8aa4e935d579c973a5a76f2c2a6269b560f873f3c67` |
| `compte-2/fichiers-de-travail-HC4-v2.tar` | `c1c443d041d5dce9c245703f0a18a068cad59f0e91aadd7d5242bb254f341ace` |
| `compte-2/fichiers-de-travail-H1-v2.tar` | `e87a36c721ef07af3c7ec13d8ccca372fc74e19fd12c4abed96f0a8154e56f75` |
| `compte-2/fichiers-de-travail-H2-v2.tar` | `aa67b5105e48c1af0588daa48a9724f3b523035447f61741a2cd8ccb4e9dccc9` |
| `compte-2/fichiers-de-travail-papierB-v2.tar` | `6228dc62979435d790e6b4fc0d39a99600006d88f152661120b3ad306b7d7565` |
| `compte-2/fichiers-de-travail-4B-partie1-v2.tar` | `f4675df2a1de4d7244f507bd860d09397b3b073d57915bfc9a1df7d88e8c679b` |
| `compte-2/fichiers-de-travail-4B-partie2-v2.tar` | `17e2f9593439475ab4c7cd75dcb18200b85c4a98b98f4a0904a78eea34d98354` |

`compte-2/` abrège `docs/sources/lecture-pdf-niveau3/compte-2/`.

JSON de citations contrôlées extraits des archives, empreintes recalculées : L `bcef36f2…` (98 citations), T `e2f4f802…` (110), H6 `43cf3afc…` (106), HC5 `a873a58a…` (76), HC1 `63ae84da…` (69), HC6 `90dca5fc…` (76), Tr `d9df3316…` (86), HC4 `4f3e8184…` (137), H1 `88f3745d…` (76), H2 `a1e68f83…` (126), papier B `7563f48c…` (104), 4-B partie 1 `642f27f6…` (97), 4-B partie 2 `8a6a3bff…` (105) : 1 266 entrées au format `{"pdf","sha256","page","citation"}`, toutes bien formées. Les empreintes de L et de HC5 sont égales à celles que leurs rapports impriment ; les autres rapports ne les impriment pas.

## 3. Comptes

- PDF lus par le compte 2 : 33 fichiers distincts (31 travaux, NARCBench comptant trois versions), 36 lectures (2601.04603 lu par trois rapports, 2608.11247 par deux). Liste par lot : synthèse, section 10.1.
- Énoncés relus : L, T, H6, HC5, HC1, HC6, Tr, HC4, H1, H2, statistique de population du papier B, rôle 1 de N-065 (deux rapports) : douze énoncés, treize rapports.
- Extraits anglais dans la synthèse v2 : 11, tous repris d'un JSON contrôlé (section 5).

## 4. Ce que j'ai lu, et comment

- En entier : la consigne, les interdits communs, la synthèse v1, son journal, sa contre-lecture (923 lignes), N-068, N-069, N-070, l'index, les treize rapports v2.
- Contre-lectures du compte 2 : en-tête et section des verdicts de chacune (repérées par la liste de leurs titres et par recherche de « table fermée » ou « Verdict » dans ces fichiers nommés) ; pour L, aussi les sections 2 à 6. Les constats de chaque contre-lecture sont lus dans la table « suite donnée » du rapport v2 correspondant, qui en donne gravité, décision et motif.
- Archives v2 : extraites dans `archives-extraites/` (sous-dossier neuf de mon dossier de travail) ; listes de fichiers affichées ; seuls les JSON de citations ont été lus, par mon script lancé avec `python3 -I` depuis un dossier distinct. Aucun script des archives n'a été exécuté.
- Aucun PDF ouvert. Toute page citée dans la synthèse est celle du rapport nommé (ou de la v1 et de sa contre-lecture).

## 5. Contrôle des extraits anglais

- `pool_citations.py` rassemble les 1 266 citations contrôlées des treize JSON en un seul fichier de travail (`pool-citations.json`), avec pour chacune le rapport, le JSON et son empreinte. Ce fichier n'est pas archivé : il recopie des citations d'articles où figure un nom de modèle ; il se régénère par le script à partir des archives du compte 2.
- `controle_guillemets_v2.py` extrait tous les passages entre « » de la synthèse (266 passages), classe comme anglais ceux qui portent des mots outils anglais sans accents ni mots outils français, et exige que chaque extrait anglais figure, après normalisation des blancs et des apostrophes, comme sous-chaîne d'une citation contrôlée. Essai préalable : un extrait juste trouvé, un extrait altéré d'un mot refusé, un passage français ignoré (fichier `test_controle.md`). Résultat final : **11 extraits anglais, 0 sans source contrôlée**. Les passages sans marque française et sans mots outils anglais ont été relus à la main (noms d'équipes, mots français, chiffres) : aucun extrait anglais caché.
- `citations-synthese-v2.json` : les 11 extraits, chacun avec le PDF, l'empreinte du PDF et la page de la citation contrôlée qui le contient, et la source (rapport, JSON, empreinte du JSON). Un extrait (le nom d'un atelier) est attesté sur la première page d'un autre PDF que celui dont la synthèse parle à cet endroit ; la chaîne est la même.
- Les extraits anglais de la v1 sans source contrôlée au compte 2 ont été paraphrasés en français (titres des versions de 2610.12445, titre de la communication d'atelier de NeurIPS 2026, volet de stéganographie de NARCBench, phrases citées de 2606.08892, 2606.12476, 2603.15809, 2606.05384, 2611.04556, 2611.00643, MasDrift, et mots isolés du texte envoyé).

## 6. Choix de rédaction à connaître

- **Table fermée, une valeur par ligne.** H6 est donné en trois lignes (lecture « hors audit, aucun moniteur dans l'intervention » ; lectures intermédiaires ; lecture la plus large) et HC4 en deux (sens de « juge »), pour donner le verdict sous chaque lecture sans en choisir une ; les deux énoncés de N-069 ont chacun leur ligne. Les « voisin » et « non réexaminé » de la v1 sont rangés sous « non trouvé dans les pièces lues », avec la réserve écrite.
- **Point d'état H6** : porté tel quel, comme demande de Lazar en attente d'inscription, non comme décision.
- **Tr** : divergence de lettre entre lecteur et contre-lecteur ; je donne le plus dur (« occupé en partie »), selon la règle de la v1, et la divergence va aux nœuds ouverts.
- **Colonne « déclarable »** : règle écrite en tête de la section 1 de la synthèse ; T et HC6 passent à « oui sous les mentions » parce que ce que la contre-lecture de la v1 demandait pour lever la réserve est fait et qu'aucun rapport v2 ne demande une lecture « avant toute phrase publique » ; H9 passe à « non » (N-070) ; HC2 est déclarable sous l'énoncé de N-068, qui prévoit son enregistrement public. Ce partage est un constat sur les pièces ; il ne décide rien.
- **Suite donnée à la contre-lecture** : seize points corrigés, M4 en réserve maintenue (L : la pièce que visait C2 n'est pas versée). Les huit mineurs sont corrigés.
- **Phrases pour un jury** : reprises de la v1, corrigées par les textes de la contre-lecture ou resserrées par les rapports v2, toutes marquées « proposition, non publiée, à décider par Lazar » ; aucune ajoutée pour un énoncé que la v1 ne couvrait pas.
- **N-067** : non lue ; ce que la synthèse en dit vient de K-4B1 (section 1) et des consignes du dépôt, et le dit.

## 7. Ce que je n'ai pas fait

- Je n'ai rouvert aucun PDF ni recontrôlé aucune page sur fichier.
- Je n'ai lu en entier aucune contre-lecture du compte 2 hors celle de L ; je n'ai pas ouvert les archives des contre-lectures ni les versions 1 des rapports.
- Je n'ai pas lu N-067, ni le programme, ni aucune décision hors N-068 à N-070.
- Je n'ai lancé ni `verifier-arbre` ni les essais du dépôt (le mandat ne les demande pas et l'arbre contient des chemins interdits).
- Je n'ai pas contre-lu ce document.

## 8. Refus et ouvertures

Aucun refus d'un contrôle de permissions, d'un crochet ni d'un classifieur. Aucune ouverture fautive.

## 9. Archive

`docs/etat-de-l-art/fichiers-de-travail-synthese-niveau3-v2.tar` contient : `citations-synthese-v2.json`, les scripts `pool_citations.py`, `controle_guillemets_v2.py`, `cherche_pool.py`, le fichier d'essai `test_controle.md` et sa sortie, la sortie du contrôle final, mes notes de lecture par rapport (une méthode d'attaque y est désignée par son identifiant arXiv) et mon journal de travail. Ni PDF, ni texte extrait, ni contenu des archives du compte 2.
