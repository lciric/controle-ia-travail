# Journal de rédaction des décisions N-067 à N-070 (brouillons 1) — v1

Rédacteur neuf (sous-agent, Claude Opus 5.5), lancé par la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`. Travail du 13 novembre 2026, de 18:16 à 18:35 UTC (heures relevées par `date -u` ; l'horloge du conteneur avance lentement par rapport au travail fait, comme le notait déjà le lecteur C7). Je n'ai écrit ni le programme, ni les décisions d'origine, ni aucun rapport de lecture.

**Mandat** : écrire, au modèle de N-013 et N-064, une décision par collision partielle tranchée en bloc par Lazar (R-2555, option B (a)), en brouillon, plus ce journal ; sceller les cinq fichiers ; aucune écriture git ; contre-lecture à venir avant toute retenue.

## 1. Fichiers écrits

| fichier | empreinte (SHA-256) | objet |
|---|---|---|
| `docs/decisions/decision-N-067-v1-brouillon1.md` | `d83d067c122e8ae5d90f6170a14e0339a88ce242d7901a7af78c1ad774b9cf39` | organisme d'idéation : O2 et O11 resserrées ; O1, O3, O12, O17 en conséquence |
| `docs/decisions/decision-N-068-v1-brouillon1.md` | `76be8b44601db787f94aa8043dee9097c7b7d42e072b7bcd73a909c11fb486dd` | HC2 reformulée après MIRAGE |
| `docs/decisions/decision-N-069-v1-brouillon1.md` | `823a3c357ef66369cea09d7053871de88377c7c67fcb32196de295c14c76f7c8` | papier B : statistique de population et statistique spatio-temporelle resserrées |
| `docs/decisions/decision-N-070-v1-brouillon1.md` | `8b52e368bbfbcf914c9fa361b2dd70a30690248d3f93f352478026caab8aad29` | H9 repliée sur l'option (b) de N-035 |

Chacun a son compagnon `.sha256`, écrit par `controle_ia.scellement sceller`. Ce journal est scellé à son tour ; son empreinte est dans son propre compagnon.

**Numéros vérifiés libres** avant écriture : aucune occurrence de N-067 à N-070 dans `docs/decisions/` (branche `main`), dans `docs/decisions/` des branches `prep/etat-de-l-art-niveau3-v1`, `prep/etat-de-l-art-niveau3-pieces-v1`, `claude/upbeat-cray-dmauvv`, `prep/organisme-v65-v1`, `prep/pilote-mr2-v1`, ni dans `registres/decisions.md`, `registres/etat.md`, `registres/go.md` et les passations du 10 au 13 novembre. La branche `main` a avancé pendant mon travail (R-2556, `73da9bd3` ; R-2557, `b4d375c9`) : aucun de ces deux commits n'emploie ces numéros (vérifié après coup).

## 2. Sources lues et empreintes

### 2.1 Récupération

Seuls appels hors du conteneur : les deux récupérations nommées par le mandat,
`git fetch origin refs/heads/prep/etat-de-l-art-niveau3-v1:refs/remotes/origin/prep/etat-de-l-art-niveau3-v1` (tête `f0aaf0d1`) et
`git fetch origin refs/heads/prep/etat-de-l-art-niveau3-pieces-v1:refs/remotes/origin/prep/etat-de-l-art-niveau3-pieces-v1` (tête `10016a61`).
Les fichiers de ces branches ont été lus par `git show`, copiés dans le dossier de travail temporaire de la session (hors dépôt), et leur empreinte comparée à celle du compagnon `.sha256` lu sur la même branche.

### 2.2 Rapports et synthèses (tous conformes à leur compagnon)

| rapport | branche | SHA-256 |
|---|---|---|
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-provisoire1.md` | niveau3 | `8adb561d52b728114cfd0c3065fe6c6230262f1befaeb2fd9d9824270ecdc3ad` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-provisoire1-complement1.md` | niveau3 | `a4176d46d5ec24406b38c82e8c653916ee0369a9b4a540f7da6fa4b108c0e33f` |
| `…/niveau3-v1/rapports/rapport-C4-organisme-ideation-O1-O20-v1.md` | niveau3 | `164502a3ed94e0adf177e4e15bfd61fc95ea24633dc1c4a2b0cacf9effab1245` |
| `…/rapport-C7-contre-lecture-qu-chen-wang-dossier-c8-v1.md` | niveau3 | `63d8373761d28c62b556f35839bd7b9f277decf4dc2d6d1ad44ad1f2266f8fb2` |
| `…/rapport-C6-H9-cemri-hammond-references-statistiques-v1.md` | niveau3 | `36d26d20e284fbf9ecccb219df06765ffc9af025650cbaa520aaf79dceccabfa` |
| `…/rapport-C9-pieces-neuves-papiers-C-B-v1.md` | niveau3 | `23ec1f6ef8c4445cbb350ac249a8d37cc2d438da9f9253959a3d30821a2b3d54` |
| `…/rapport-D3-recherche-affirmative-papier-B-H9-v1.md` (ouvert, non exploité : pistes de moteur) | niveau3 | `a189a005494cd34546602016d20dca2bc61e1aa1f0cf64f9ecdc1e26eead8dab` |
| `…/rapport-C3-loi-de-deference-papier-C-v1.md` (ouvert, non exploité) | niveau3 | `d7efc7f252b6c9416702952871e5b67a2327ef61f1e4598135602bfa90266bba` |
| `docs/sources/lecture-pdf-niveau3/rapport-lot4A-organisme-O2-v1.md` | pièces | `5dfd5251b0592723a1481f0c3178e451f306c63e977b9b6bba4ce8d35b0abafa` |
| `…/rapport-lot1-HC2-mirage-karne-v1.md` | pièces | `9996f40cf5614e32c74bc4c97c79a8e88d65c76c6c4635d8ea38d034315c0f4b` |
| `…/rapport-lot3A-sondes-sabotage-injection-v1.md` | pièces | `64b728d63927e8c55a77c0e2372637f3ea9f769477e98bdd46db1d9481264b03` |
| `…/rapport-lot5A-sequentiel-multi-agents-v1.md` | pièces | `aef81e6e43b63f7aa0b2277308495dc9a7b0ccaea6e5c37a3d876fd5aac7b88f` |
| `…/rapport-lot7B-collusion-papier-B-v1.md` | pièces | `bf9b6af8f2d8a51ae406e8bcd2c53c3eff698826ecf916700ec7ae0dd206633c` |
| `…/rapport-lot7C-juges-papier-C-v1.md` | pièces | `2b03ede00f21e4b5f72cd4b4fb3b3356746e90ff5eefdf73a020661e44cd106f` |
| `…/rapport-lot7D-delegation-H9-v1.md` | pièces | `9f4c3b94203da70075c5cee057fe6f32ea8086b4369081692898009aebf394f2` |
| `…/rapport-lot12-pistes-H9-v1.md` | pièces | `382ed6e419074a19eecf54f173e551f26c4495e7555b845c65bdcf71ceeec9dd` |
| `…/rapport-lot2B-billets-moniteurs-attaque-v1.md` (§ 0.1 et 5.3 seulement) | pièces | `8b4b5af1f105f70c36650e9cc8febabcaa2c8bf87cea4fe485dfebf9fe5c6a41` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` (synthèse finale, **non contre-lue** ; sections 3, 4 sur HC2, 5, 7, 10 lues **après** mes premiers jets) | `main` | `e30a013d08b03e8ddc07637b186e38e2051bd221958b713cc27facd1abf45892` |

### 2.3 Documents de la branche `main` (énoncés d'origine)

Empreintes vérifiées contre les compagnons : `docs/programme-controle-ia-v2.md` (`2fd63bad…`, conforme aussi à `docs/sha256sums-lancement-v2.txt`) ; `docs/decisions/decision-N-064-v1.md` (`387c9d4e…`) ; `decision-N-013-v1.md` (`157d388e…`) ; `decision-N-035-v1.md` (`55df073d…`) ; `decision-N-005-N-006-v1.md` (`cd49afbc…`) ; `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md` (`08a3738a…`) et `…/note-anteriorite-popper-evaluator-v1.md` (`d1ab7049…`) ; `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (`c5465a9b…`). Registre : R-2555 (mot de Lazar), R-2172, R-2177, R-2180, R-2181, R-2184, R-2188, R-2190, R-622, R-2554, R-2556, R-2557.

### 2.4 PDF des pièces citées

Empreinte de chaque PDF recalculée (par `git show … | sha256sum` pour la branche des pièces, par `sha256sum` sur `main`) et comparée au compagnon : **toutes conformes**. Seize premiers caractères :
- organisme (N-067) : 2609.27051 `2a8ded0119a1db42` ; 2606.08106 `779f49607688fd06` ; 2609.33180 `20639707e89ee9b1` ; 2610.38392 `6a415ce487e61a71` ; 2609.02246 `9a2923ab00070a89` ; 2606.11417 `7ae148beb5c73d30` ; 2609.17560 `ef318a961de7d5f2` ; 2510.10232 `ad17c77e8f5f8e09` ; 2607.24300 `0a1434ea1c9b5338` ; 2607.00871 `fb50bba836f7db5e` ; 1506.02629 `dcfbb9aa401c6294` ; 1502.04585 `957ef4739df371a0` (tous sous `docs/sources/pdf/anteriorite-P-041-v2/c8/`, `main`) ; 2611.01449v2 `9a02cc6d6b9897c8` ; 2511.06701v4 `dfcd6dd1ee0bb136` ; 2610.24597v1 `e923a544b27f7f21` ; 2608.06621v5 `d4d4682b52cfcff9` ; 2611.06607v1 `add4e5be86142ce7` ; 2610.06432v1 `283d3e827032df04` ; 2611.04420v1 `731e03b1479e562d` ; 2611.00643v1 `62be7556ef33cbbd` ; 2610.11289v1 `d0655b6d49c5a5d2` (sous `docs/sources/pdf/niveau3-v1/lot4/`, branche des pièces).
- HC2 (N-068) : 2606.10304v1 `677fe27807039ea0` ; 2609.05797v3 `eb7be6cafe328086` ; 2608.21664v1 `7303ce0c3ad1d551` ; 2602.00750v2 `cf0bd3653fdc8a1f` ; 2602.08877v2 `cd1f2772d7b96bb6` ; 2610.18408v1 `411748554484dfb6` ; 2610.37679v1 `8640d1f07039965c` ; et, sur `main`, 2511.00554v1 `17708292f357ddee`, 2601.11516v4 `c4a36db54c9d679a`, 2509.21344v2 `aaac4ff91c909f9e`, 2609.36490v1 `eb6d5bbe9bfaff0a`, 2603.13791v1 `0b2b155024d67bae`.
- papier B (N-069) : 2601.05427v3 `e258cf0ade2a3801` (identique sous `lot3/` et `lot5/`) ; 2605.11135v2 `1cc342dafb631dea` ; 2611.02153v1 `65cc02df7485b253` ; 2611.10620v1 `2aa2fd973d5693a2` (identique sous `lot3/` et `lot7/`) ; 2212.07383v4 `a0a596319e1cc2ea` ; 2606.20746v1 `8d27cd7d20ef135f` ; 2609.03035v2 `bccdbe1b2dd753f2` ; 2610.24052v1 `0825bb533d9e3fd3` ; 2604.01151v5 `02527fd4f62ad9b9` (`main`).
- H9 (N-070) : 2608.07556v3 `fb51ecae3c549fd0` ; 2608.24569v2 `ca2e1cf0abf81a7a` ; 2605.08647v1 `274bc00ae0f48df3` ; 2605.10481v1 `92938c741f4bd724` ; 2605.05440v1 `fc43013689fe7342` ; 2502.14143v1 `3a8e798a29f77ca4` ; 2503.13657v3 `1b9e317a2a421e60` ; 2602.11865v1 `5bae1457b1d42dc4` ; 2609.27900v1 `b3ea2b3b15bdf22b` ; 2607.07097v1 `490935226b9447ff`.

### 2.5 Contrôle par sondage sur les PDF (R7)

Je n'ai pas relu les PDF ; chaque page des décisions vient d'un rapport dont le lecteur a contrôlé ses citations par programme. Pour éprouver ce relais, j'ai recherché 24 passages dans le texte de leur page (`pdftotext`, page seule, blancs réduits), sur 15 PDF : CONFIRM p. 3 et p. 9 ; MasDrift p. 2, 6, 23 ; 2611.10620 p. 12, 14, 22 ; MIRAGE p. 2, 20 ; AgentCollabBench p. 34 ; J-PACT p. 8 ; « Hard to Fool » p. 4 ; Qu, Chen, Wang p. 2, 6 ; 2608.21664 p. 7 ; Sun p. 1 ; Karne p. 6 ; REUSE p. 32 ; Helm p. 2 ; Gauthier p. 1, 5 ; Kale p. 4, 12. **Tous retrouvés.** Les deux recherches sur Gauthier (p. 1 et 5) portent sur un mot ou une locution (« anytime », « e-BH ») : contrôles faibles. Un premier essai sur Helm a échoué parce que j'avais cherché à la p. 1 un passage que le rapport 5-A situe p. 2 : erreur de ma part, corrigée, le passage est bien p. 2.

## 3. Choix de rédaction

**Communs aux quatre.**
- Modèle : en-tête de N-064 et de N-062 (brouillon), sections de N-013 ; mot de Lazar verbatim, puis la lecture de la mère pour B, recopiée du registre et marquée comme lecture.
- Chaque énoncé d'origine est recopié avec chemin et ligne. H9 n'est pas dans le programme v2 : ses lignes viennent de N-035.
- Les pages viennent des rapports ; chaque table nomme le rapport. Aucune affirmation n'est portée au-delà de ce qu'un rapport a lu sur PDF ; les pistes de moteur et les références de bibliographie non lues sont isolées dans une section « non vérifié », hors de tout énoncé.
- Les décisions ne touchent pas aux poids de confiance du programme (ceux de Lazar) ; elles disent seulement quand un contre-indice les rend moins sûrs.
- Chaque décision renvoie à la mère les gestes qui ne sont pas les miens : recopie sous `-v1.md`, ligne « revendication » dans `registres/go.md` (usage de N-064, GO-2026-11-09-01), mise à jour de la liste de `CLAUDE.md`.

**N-067 (organisme).** O2 ne garde que le nul des lois connues ; les trois autres composantes sont empruntées et citées, leur réunion avec le nul dite comme un assemblage. O4 devient seul porteur. O12 resserrée à la consigne de tromper, la lecture de la description exacte, la liberté du proposeur et le contraste des deux bras (lot 4-A sur CONFIRM). O11, O1, O17 : plus aucune revendication d'idée ; ce qui n'est pas trouvé (ampleur du banc, mutations du code du juge, banc de mutations du scellement, règle générale contre le repli silencieux) est décrit, sans priorité. O3 : le sceau cédé ; l'ensemencement par l'empreinte, non trouvé, décrit sans priorité. L'objet (hypothèses libres) qualifie l'assemblage, sans être revendiqué seul (N×N certifie déjà des hypothèses écrites par des modèles). Lettres des composantes de O2 : celles de C7, avec la correspondance du lot 4-A.

**N-068 (HC2).** Énoncé du lecteur du lot 1, repris, **plus l'ajustement du lot 3-A** (le plan apparié n'est pas neuf : 2610.18408, p. 4, 12), signalé aussi par la synthèse finale (section 7, point 2). Prédiction gardée dans son signe ; contre-indices rassemblés en une table avec la position de la sonde (lecteur, victime, auteur). Les propositions de conception des lecteurs (trois positions de sonde, évasion par un outil, témoin lexical, exposition contre engagement) sont rangées « à porter au préenregistrement, non fixées ».

**N-069 (papier B).** Deux énoncés séparés : statistique de population (formulation de 7-B, § 6.1) et statistique spatio-temporelle (formulations de 5-A, § 3 et 7-B, § 6.1, réunies). « Le cœur vierge » retiré. Le critère de la porte G2 n'est pas changé ; le contre-indice de 2611.10620 (p. 14) est dit. Le déclencheur de bascule est laissé à Lazar.

**N-070 (H9).** Repli (b) appliqué tel que N-035 l'écrit : retrait de l'hypothèse, consigné ; mesure descriptive sans revendication. J'ai pris pour contenu de cette mesure celle de l'option (a), décrite par rang de relais, avec et sans moniteur, située contre MasDrift et AgentCollabBench. Les quatre « encore revendicables » des lecteurs sont gardés comme questions, non revendiqués ; la lecture interne du sous-agent est signalée comme modification d'hypothèse.

## 4. Points incertains, à trancher par le contre-lecteur ou par Lazar

1. **O12 dans le périmètre de R-2555.** La synthèse finale (R-2557, section 7, point 1) écrit que la requalification de la forme de O12 n'est « pas couverte par la lettre de R-2555 ». Le mandat, lui, range O12 dans « ce qui s'en suit » et dit « la forme mesurée de O12 » encore libre. J'ai resserré O12 parce que garder la forme de N-064 affirmerait plus que CONFIRM (p. 9, 22), lu sur PDF, ne le permet. **À confirmer.**
2. **Écart entre le résumé du mandat et les lecteurs.** Le mandat dit « seule la comparaison au nul formé des lois connues (O4) et la forme mesurée de O12 restent libres ». Les lecteurs listent aussi comme non trouvés : l'ensemencement par l'empreinte (O3), l'ampleur et la combinaison du banc (O11), un banc de mutations du code du juge et du scellement (O11, O17), l'objet. Je ne les revendique pas comme apports ; je les décris comme non trouvés, sans priorité. Si la mère voulait leur retrait pur et simple des textes, ou au contraire leur maintien comme revendications étroites, il faut le dire.
3. **Citations ajoutées à la liste du mandat**, chaque fois parce qu'une recommandation suivie les nomme ou qu'un énoncé resserré en dépend : Hegazy, Jordan, Dieuleveut et PROCTOR (N-067) ; Kale et Vishwanath, 2610.18408 (N-068) ; Li et collègues, 2605.10481 (N-070, « à citer obligatoirement » selon 7-D). Elles sont marquées « ajout à la liste de la mère » dans les tables.
4. **Ajustement de HC2 par le lot 3-A** : la décision de Lazar dit « comme proposé (R-2180) » ; j'ajoute la précision du lot 3-A (plan apparié non neuf ; « en fonction de l'intensité »). C'est un resserrement de plus, pas un élargissement ; à confirmer.
5. **Contenu de la mesure descriptive de H9** : N-035 (b) ne dit pas ce que mesure la description ; j'ai repris la mesure de (a). À confirmer.
6. **O4 porte désormais seul la revendication du juge**, et c'est le verdict le plus fragile de tout le niveau 3. Une piste de priorité haute, non lue, peut l'occuper en entier : SSRN 6569258 (selon un résumé de moteur, tests de nouveauté par englobement contre 209 anomalies publiées, C4, § 5, piste 6). **Recommandation de lecture avant tout usage public de O4**, notamment avant l'enregistrement figé des pièces libres (R-2555, option C).
7. **Compte des composantes de O2** : C4 (trois), C7 (deux et une en principe), 4-A (trois) divergent ; la décision le dit et ne tranche pas, le resserrement ne dépendant pas de ce compte.
8. **Pièces non PDF** : un billet (« What Happens When a Collusion Probe Only Finds a Thin Signal? », lot 2-B, § 5.3) est cité en N-069 comme contre-indice faible, marqué « billet archivé en texte, non un PDF ». La mère peut préférer l'ôter.
9. **Synthèse finale lue tard** : elle est apparue sur `main` pendant mon travail (R-2557, non contre-lue). Je l'ai lue après mes premiers jets ; elle m'a fait ajouter l'ajustement du lot 3-A, le contre-indice indirect de 2602.08877 (lot 7-C), le rappel de HELIOS v5 (p. 18), le billet du 26 juillet 2026 et le statut de O13. Je n'en ai pas lu les sections sur le papier A ni sur HC1, HC3 à HC6.
10. **Profondeur de lecture des rapports** : plusieurs lecteurs n'ont lu les annexes que par recherche de termes (4-A, § 1 ; C7, § 7 ; C4, § 7) ; un « non trouvé » vaut pour ce qu'ils ont lu.
11. **Statuts de l'organisme hors périmètre** (O9, O10, O13, O19) : constatés dans N-067, section 10, non resserrés.

## 5. Constats annexes, pour la mère

- **Journal à la racine du dépôt** : `NODE_C_VOLETS_III_IV_H9.log` (versé au commit `35abfd16`, R-2066) porte « H9 » dans son nom. Je n'en ai lu que les premières lignes (chargement de Llama-3.1-8B-Instruct sur un processeur graphique loué, « VOLET=III_IV »). Provenance et objet non établis par moi ; aucune incidence sur N-070 telle qu'écrite. Si c'est une course touchant H9, elle n'a pas de préenregistrement à ma connaissance (R1) : à vérifier par la mère.
- **Lot 10 (versions de NARCBench)** : des PDF sont versés sous `docs/sources/pdf/niveau3-v1/lot10/` (2604.01151 v1, v2, v4) ; je n'ai trouvé aucun rapport de lecture correspondant sur la branche des pièces. La veille sur le déclencheur de bascule (N-069, section 9) en dépend.

## 6. Refus, interdits, écarts

- **Aucun refus** de contrôle de permissions ni de classifieur.
- Aucune écriture git (seuls `fetch` nommés, puis `show`, `ls-tree`, `log`, `rev-parse`, `status`, en lecture). Aucun registre modifié. Aucune dépense. Aucune valeur de clé lue ; aucune variable d'environnement listée.
- Chemins interdits non ouverts ; aucune recherche récursive traversant `docs/notes/bras-attaque/`, `donnees/`, `diag/`, `runs/` ni `registres/index-bras-attaque*` : les recherches ont porté sur des fichiers nommés ou sur des listes `git ls-tree` restreintes à `docs/decisions/`, `docs/sources/pdf/` et `docs/sources/lecture-pdf-niveau3/`.
- Les PDF, données non fiables, ont été copiés dans un dossier neuf du dossier de travail temporaire et traités par `pdftotext` seulement ; aucun interpréteur lancé depuis ce dossier.

Version 1 ; jamais réécrite (R12).
