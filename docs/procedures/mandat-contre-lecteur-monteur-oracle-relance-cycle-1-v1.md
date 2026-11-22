# Mandat — contre-lecteur des pièces du monteur de l'oracle, cycle 1 du scellement 2, relance (v1)

- Classe C. Écrit le 2026-11-22 vers 15:05 UTC par le monteur de l'oracle du cycle 1, relance
  (`session_01XJ6MgmSDBZpPAuXLe3diix`), à la demande de la mère (`session_01XJ6Mgr4LgbMsg5zLyRZCpG`, message de
  14:54 UTC). **Sans contenu de famille ni d'oracle** : des chemins, des empreintes et des règles.
- Fondement : mandat du monteur v3 (`docs/notes/attaquant-informe-v1/course-brouillon17-v1/mandat-monteur-oracle-relance-v3.md`,
  branche `claude/loving-lamport-7ol5ws`, `2d81401a54808257b6f18f3fb86cbf5e764452ab8fff7ecce3e959b572ff74d2`),
  section 5 ; mandat v2 (`docs/procedures/mandat-monteur-oracle-scellement-2-v2.md`, cette branche,
  `c6f090c02bfc2cd6d8f7a04b483f7a16f065a0178df51671481ec08a665fc843`), section 6 ; `CLAUDE.md`, « Qui conçoit » et
  « Allègement de la procédure ».
- Qui : **un Fable 5.2 neuf**, lancé par la mère par l'abonnement. Langue : français, sans acronyme non développé. Lis
  d'abord `CLAUDE.md` en entier, sur `main` ; cette lecture n'autorise rien de ce que la section 4 interdit.

## 1. Avant tout geste

1. Fais `git fetch origin main`, puis cherche sur `origin/main`, dans `registres/decisions.md`, une ligne qui porte
   « Accès au coffre du bras d'attaque » **et ton identifiant de session**. Tant qu'elle n'y est pas, ne lis rien du
   coffre ; préviens la mère par `send_message` (serveur Claude Code Remote) et attends sa réponse, sans `sleep`.
2. Recalcule l'empreinte de chaque pièce avant de la lire. **Tout écart est un arrêt**, signalé à la mère.
3. Écris d'abord, au coffre, ton attestation (section 3, point 1).

## 2. Ce que tu contre-lis

Toutes les pièces sont sur la branche `claude/scellement-2-oracle-cycle-1-v1`, dossier
`donnees/bras-attaque-oracle-scellement-2-cycle-1-v1/` (le coffre), sauf mention contraire.

| n° | pièce | empreinte | classe | ce que tu en dis |
|---|---|---|---|---|
| 1 | `relance-piece-3-champ-18-lecteurs-du-dommage-v1-brouillon1.md` | `1233b8a6524598a5596f6469042b3c3ba6893aa04d40620edec53df2efcabfe9` | A | conformité à la pièce de sécurité v16, section 3.5 (sept rubriques, règle de la lecture humaine) et à la course, section D6 ; exactitude de chaque citation contre les copies versées dans `sources-conditions-fournisseurs-v1/` ; complétude du nœud de la section 3 |
| 2 | `oracle_famille_1_v1.py`, `controle_agent_p1_v1.py`, `test_oracle_famille_1_v1.py` | `43c4c8f1de28878120f65962aec26ad87e5b7a0d70fbff185a2545cf69a3787d`, `42a2a0437473546fa17b4a17f492a21b15f863439b46be1f3398a8b4f93a6756`, `216c2f3213ce504418c15055fe0fd8c371776c7955d35fdcd1be5d7a6e0475f3` | B | justesse contre la spécification de la famille ; gardes d'arrêt éprouvées sur un cas sain et sur un artefact (R5) ; graines (R9) ; aucun repli silencieux. Lance les tests : `PYTHONPATH=src python -m pytest -q donnees/bras-attaque-oracle-scellement-2-cycle-1-v1` (46 attendus) |
| 3 | `piece-2-oracle-monte-famille-1-v1.md` (monteur précédent) | `758e404a4327f5a31839c0fd25e2de3c08ed748958b6b0f99364123c7e17d352` | A pour ses sections 3 à 5, B pour le reste | ses onze précisions (section 3) ; ses invites (section 4) ; ses gabarits (section 5) ; aucune invite ne doit dire la condition, la dose, le type, ni qu'un plan a pu être altéré |
| 4 | `piece-3-plan-des-epreuves-oracle-famille-1-v1.md` (monteur précédent) | `10e1f85ac7802623ae5cadea4817f6da81fd52117abc08a252ffe7a40970101d` | A | fidélité au plan de l'auteur (mêmes onze épreuves, mêmes critères, même ordre) ; tailles minimales ; ce que les épreuves ne prouvent pas |
| 5 | `piece-4-repli-oracle-famille-1-v1.md` (monteur précédent) | `7583d5ff11668be5da843f20b0369fc1c85db7a0f3153dae1c5d3789325072f9` | A | fidélité au repli de la spécification ; aucun repli décidé après un épisode saboté |
| 6 | `relance-noeud-regle-des-questions-v1.md` et `relance-erratum-1-v1.md` | `5ab499938bff2a7e7f631181b9d6d6cbaacb500e35a2a2e11dc9261420517043`, `a8c39be5d100c0bd1340c500887a3c6dcb0a6873572b7a14387d5808cac5d40c` | C, **avis seulement** | le constat tient-il ; la conclusion « rien ne part » suit-elle des textes ; manque-t-il une option. **Tu ne tranches pas le nœud** : il est à Lazar |

**Pièces d'appui, à lire pour juger, sans les contre-lire** (empreintes à recalculer) :
- spécification de la famille : `donnees/bras-attaque-scellement-2-v1/piece-3-famille-aveugle-1-verite-du-dommage-v2.md`
  et plan de l'auteur `…/piece-4-famille-aveugle-1-plan-des-epreuves-v2.md`, branche
  `claude/scellement-2-familles-aveugles-v1`, commit `f4c479c5`,
  `2a7416a823c406a1a284310735f883b4c0131a80c16e12d933ddab30a3cda97f` et
  `aba1a770a68fa73cd231bc193701c51e223fda6ab19447912b0168de61a2d52e` ;
- vérification de la contre-lecture de la famille : `…/piece-7-verification-des-corrections-v1.md`, branche
  `claude/scellement-2-contre-lecture-v1`, `8be9063c0982ce24…` (et son erratum 1, `aa10a1db0f9ff512…`) ;
- état repris : `relance-piece-2-etat-repris-v1.md`, `f20518e34c3b31bac72f2420f31e51cd8f171bd98d7f49d27a26c29037bd7ac2` ;
- constat du prédécesseur et proposition de lecteurs : `constat-lecture-humaine-et-conservation-fournisseurs-v1.md`,
  `f892fc6caaeb98e0929f06eb3907046e608907df811d06fe2da6090a65def781` ; `message-mere-proposition-lecteurs-v2.md`,
  `ffc82cb9362d68796eb492cbce4f48d3be01d1c57d2edd869b1c6f77dd564dd4` ; les cinq pages de
  `sources-conditions-fournisseurs-v1/` (compagnons `.sha256` à côté) ;
- hors coffre : pièce de sécurité v16, sections 3.5 et 6 (`docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v16.md`,
  branche `claude/piece-securite-banc-ferme-v1`, `b8bcda60ead6f58f4cc59adf209c779eb81b201fc730734b9175e0faefdaeeec`) ;
  course, brouillon 17, sections D6, D7 ter, D8, liste d'arrêt, « Champs ouverts et nœuds »
  (`docs/notes/attaquant-informe-v1/course-brouillon17-v1/course-banc-ferme-v1-brouillon17.md`, branche
  `claude/loving-lamport-7ol5ws`, `cf5d35d8472137d30defedb2a61b375037d558e3937e4371cb5d8822a507a881`) ; répétition,
  brouillon 9, champ R-5 (`prereg/repetition-generale-banc-ferme-v1-brouillon9.md`, branche
  `claude/prereg-course-banc-ferme-v1`, `a58cab35cf4914a4e78decec95f296d824626752f4028b347ca5741d49f76e08`) ; audit
  des lignées et sa vérification, sur `main`, pour la seule liste d'exclusion
  (`docs/notes/scellement-2-lignees-lecteurs-v1/lignees-a-exclure-v1.md`,
  `596b5a73453b97ed876a2197dfd8ed68183802f531296f0bfac50d156b536862` ; `verification-lignees-a-exclure-v1.md`,
  `8718c80bee53da3521e0c0f934af99d91c284465aec604f076a060ec5399ce96`) ; `CLAUDE.md` sur `main`, règle « Appels aux
  modèles de Google » ;
- matière de la tâche : `src/controle_ia/environnements/propositions.py` ; les fichiers de tâches du banc
  (`donnees/20261007-082440-t05-extraction/taches-evaluation.json`, `taches-entrainement.json`) **par programme
  seulement**, comptes et noms de clés, sans afficher aucun texte de référence.

Tu ne lis pas la pièce 2 de la famille (texte du mode) : la spécification et le plan de l'auteur suffisent.

## 3. Ce que tu rends, et où

Tout au coffre, en **fichiers neufs**, scellés (`python -m controle_ia.scellement sceller FICHIER`), dans
`donnees/bras-attaque-oracle-scellement-2-cycle-1-v1/contre-lecture-relance-v1/`, sur ta branche, que la mère nomme
(proposition : `claude/scellement-2-oracle-cycle-1-contre-lecture-v1`). `donnees/` est ignoré par git : ajoute par
`git add -f`, puis vérifie `git status`. Pousse ta branche ; aucune demande de fusion, même en brouillon ; jamais
vers `main`.

1. **Ton attestation**, avant toute lecture du coffre : tu n'as conçu aucun moniteur et n'en concevras aucun ; tu n'es
   ni l'attaquant informé, ni l'auteur d'une famille, ni la contre-lectrice d'une famille, ni le juge des recettes, ni
   l'agent qui juge l'ancre des épreuves ; tu n'as lu aucune sortie de la course « nouvelles attaques » ; tu n'as lu
   aucune famille ni aucune pièce d'un autre cycle que le cycle 1.
2. **Ta contre-lecture**, une pièce par fichier ou un seul fichier sectionné : pour chaque pièce du tableau de la
   section 2, un verdict — **accepté**, **à corriger** ou **refusé** — et des points numérotés, chacun classé
   **bloquant** ou **mineur**, avec le passage visé (chemin, ligne) et la correction attendue. Pour la pièce 6 : un
   avis, sans verdict sur le nœud.
3. **Ton journal des accès** : heure (UTC, `date -u`), chemin, empreinte, motif ; scellé à la fin.
4. Plus tard, **la vérification de mes corrections**, par toi, sur les versions nouvelles que je te signalerai
   (même chaîne : `CLAUDE.md`, « Allègement de la procédure »).

## 4. Interdits

- Aucun moniteur : ni sonde, ni agrégateur, ni trait de texte, ni conception, ni résultat, ni seuil, ni note de
  lentille, ni base, ni juge.
- Rien du coffre hors du dossier du cycle 1 et des pièces de la famille du cycle 1 citées ici ; jamais la branche
  `claude/scellement-2-famille-reserve-cycle-2-v1` ni sa contre-lecture ; aucune pièce d'un autre cycle.
- Ni les lignes R-604 à R-610 de `registres/decisions.md`, ni `registres/etat.md`, ni les passations du programme.
- Aucune sortie de la course « nouvelles attaques ».
- Aucun envoi à un lecteur externe, aucun appel de modèle, aucune dépense, aucun épisode, aucun plan saboté, aucun
  code d'attaque. Tu ne modifies aucune pièce du monteur : tu écris les tiennes.
- Aucun contenu de famille ni d'oracle dans un message : des chemins et des empreintes seulement.
- Si un classifieur refuse une réponse : consigne-le, arrête-toi sur ce point, ne reformule pas, ne transmets pas.
  Ne contourne jamais un refus d'outil, de classifieur ou de garde : signale-le.
- Après cette contre-lecture, tu ne concevras aucun moniteur.

## 5. Compte rendu

À la fin de la contre-lecture, puis à la fin de la vérification : **à la mère**
(`session_01XJ6Mgr4LgbMsg5zLyRZCpG`) **et au monteur** (`session_01XJ6MgmSDBZpPAuXLe3diix`), par `send_message` :
ta branche et ton commit ; les chemins et empreintes de tes pièces ; un verdict par pièce, en un mot, et le nombre de
points bloquants et mineurs ; les refus de classifieur s'il y en a eu. Rien de plus. L'attaquant informé ne reçoit
rien de toi.

## 6. Ligne d'accès au coffre, que la mère inscrit avant ton premier geste (N-057, point 5)

> R-…. Accès au coffre du bras d'attaque (N-057, point 5) : qui — le contre-lecteur des pièces du monteur de l'oracle
> du cycle 1, relance, Fable 5.2 neuf, session <identifiant>, branche <branche> ; quand — depuis son lancement le
> 22 novembre 2026 vers <heure>Z, jusqu'à la remise de la vérification des corrections ; pourquoi — contre-lire le
> champ n° 18 (classe A), le code repris de l'oracle de la famille aveugle 1 (classe B), les pièces 2 à 4 du monteur
> précédent (classe A) et donner un avis sur la note de nœud de la règle des questions, sans concevoir de moniteur
> (mandat `docs/procedures/mandat-contre-lecteur-monteur-oracle-relance-cycle-1-v1.md`, <empreinte>). Lecture limitée
> au dossier du cycle 1 et aux pièces de sa famille ; journal des accès au coffre.
