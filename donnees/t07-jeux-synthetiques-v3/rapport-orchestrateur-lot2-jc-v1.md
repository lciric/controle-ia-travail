# Rapport de l'orchestrateur — lot 2 des jeux de T0.7 (J-C réécrit sous la consigne v3) — v1

- **Auteur** : orchestrateur neuf du lot 2 (Claude Opus 5.5), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`.
  Il n'a écrit ni T0.7, ni ses jeux, ni leur script, ni leurs contre-vérifications. **Exclu ensuite de tout rôle de lecteur de P3-bis.**
- **Heures** (relevées par `date -u`) : début 2026-11-10 08:14:36 UTC ; 8 essais rejoués 08:17:33 UTC ; journal des règles
  commencé 08:21:11 UTC, scellé 08:23:09 UTC ; dossier temporaire effacé 08:23:14 UTC ; ce rapport écrit ensuite (heure du
  scellement : celle de son compagnon `.sha256`).
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-lot2-jc-t07-v1.md`
  (`3790e04e0fb52b22d803835151bf27a1dc45d608f1426a83e890cc75de7c4645`, vérifiée avant lecture) ; interdits communs v2
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés), tenus en entier, règle 9 comprise.
  `main` au commit `a8a0b2e8` au départ (`60e8c0e5` à 08:23 UTC, avancé par la mère).

## 1. Verdict

1. **Point 1 fait** : règles de pré-contrôle de J-C fixées **avant tout écrivain** et scellées
   (`journal-jc-lot2-regles-fixes-v1.md`) ; outil C-1, C-2 (`e996c8bb…`) et **ses 8 essais rejoués avant usage : 8 sur 8** ;
   comptes de `regles-c1-c2-j-c-v1.md` retrouvés à l'identique (C-1 104, C-2 77 sur les 320 paires refusées) ; outil des règles
   fixes (`verif_lot_v1.py`, `a5fec775…`) éprouvé sur un cas sain et un artefact ; consigne d'écrivain prête et scellée
   (`consigne-ecrivain-jc-lot2-v1.md`), **non utilisée**.
2. **Arrêt après le point 1, comme la consigne le prescrit** (« Si tu ne peux pas lancer de sous-agents, arrête-toi après le
   point 1 et rapporte ») : **cette session n'a aucun outil de lancement de sous-agent** (ni `Agent` ni `Task` ; recherche dans les
   outils différés : « No matching deferred tools found »). Les points 2 à 4 ne sont pas faits : **aucun écrivain, aucune remise,
   aucun jalon, aucune aire, aucun assemblage v3, aucune contre-vérification, aucune clé**. J-C v3 n'existe pas.
3. **Moyen écarté, déclaré** : l'outil de sessions distantes (`create_session`) crée une session de premier niveau dans un autre
   conteneur, pas un sous-agent ; ses réponses vont à la session mère, non à cet orchestrateur ; elle aurait tout le clone sous
   les yeux, sans liste fermée. L'employer aurait contourné la condition d'arrêt de la consigne : **non utilisé**.
4. **Aucun refus** d'un contrôle de permissions ou d'un classifieur rencontré.

## 2. Sorties (dossier `donnees/t07-jeux-synthetiques-v3/`, chacune avec son compagnon `.sha256`)

| fichier | sha256 | rôle |
|---|---|---|
| `journal-jc-lot2-regles-fixes-v1.md` | `fb249517c739090073006624af3d0e5abef43986b6288cd5a6905d4fbe0c87a3` | règles P-1 à P-5 et procédure fixées avant le premier écrivain ; rejeux ; entrées (annexe 1) ; mise en place des outils (annexe 2) |
| `consigne-ecrivain-jc-lot2-v1.md` | `190fe049151a124c528801ef611d9e23de67aaf174887f1ed81856f120421d15` | consigne d'écrivain (anglais) : section 11 de la v3, compléments de la fille 12, C-1 et C-2 dits à l'écrivain, auto-contrôle |
| `generer_consigne_ecrivain_jc_lot2_v1.py` | `bed7596677f9eb7c06e91eabe20f7a6cfdab7c3b16a06ac8d836a2ec721e6cbd` | générateur de la consigne d'écrivain (contrôle les empreintes de ses sources) |
| `rapport-orchestrateur-lot2-jc-v1.md` | celle de son compagnon | ce rapport |

Non écrits (le lot s'arrête avant) : `domaine-cout-v3.jsonl`, journaux de pré-contrôle et de vérification, `provenance-v3.md`,
rapport et clé de contre-vérification. **Aucune ligne de registre écrite.** Aucune écriture git ; aucun `git fetch` (les deux
références permises étaient déjà dans le clone : `refs/remotes/origin/prep/fille-12-t07-v1` = `bd02ae3e`,
`refs/remotes/origin/donnees/tokeniseur-llama-3.1-8b-instruct-v1` = `03e3cbd9`).

## 3. Lu, et jamais ouvert

- **Lu** : la consigne et les interdits ; l'inventaire `docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/inventaire-jeux-t07-v1.md`
  (`c9910a54…`, vérifié) ; la consigne v3 `docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md` (`d9de50a6…`, vérifiée) ;
  R-1618, R-1660, R-1663, R-1668, R-1672, R-1674, R-1675, R-1696, R-2101 de `registres/decisions.md` (sortie d'un `git grep`
  borné à ce fichier) ; à `bd02ae3e`, par `git show` : les règles fixes, les règles C-1 et C-2, les trois outils, les deux
  consignes d'écrivain de la fille 12, les 32 entrées `entrees-jc/`, les 32 remises refusées `remises-jc/` (passées aux outils ;
  seules les sorties des outils ont été lues) ; la liste des fichiers du dossier de la fille 12 (`git ls-tree` borné à ce dossier) ;
  le dossier `donnees/t07-jeux-synthetiques-v2/` (liste, empreintes, compagnons ; contenu de `enonces-reserve-v2.jsonl` et des
  deux banques passé aux scripts) ; `src/controle_ia/scellement.py` (début) ; lignes 112-120 et 176-200 de
  `scripts/verifier_jeux_synthetiques_t07_v2.py` (règle N3) et ses options `--version`.
- **Jamais ouverts** : tout `lecture-sondes-t06.json` ; la lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et
  `runs/` ; `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ;
  l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; les textes d'actions de P3 ; **aucun fichier de P3-bis** ; la clé
  de contre-vérification du 7 novembre présente dans `donnees/t07-jeux-synthetiques-v2/` (seule son empreinte a été calculée,
  par `sha256sum` sur le motif `*.json` de ce seul dossier, sans récursion). Aucune recherche récursive ; aucun appel de modèle ni d'interface
  externe ; aucune dépense ; aucun `vastai` ; aucun secret lu.

## 4. Écarts et constats

- **E-L2-1** : arrêt après le point 1, faute d'outil de sous-agents (section 1) ; les points 2 à 4 restent entiers.
- **E-L2-2** (compléments fixés avant le premier écrivain, à déclarer dans la future `provenance-v3.md`) : C-1 et C-2 dits à
  l'écrivain (partie 3 de sa consigne, écart de type E-4) ; lot de la fuite lexicale (P-2) fixé aux deux tâches d'une remise ;
  sort d'une paire ou d'une tâche encore en défaut après le renvoi unique fixé (journal, 3 d) ; défaut dur du script officiel vu
  à un jalon admis comme déclencheur de renvoi (journal, 3 c, comme r12 chez la fille 12).
- **E-L2-3** : `verif_lot_v1.py` ne voit ni les ordinaux ni `node`, `flop(s)`, `petaflop(s)`, `exaflop(s)`, `mi300` que le
  script officiel compte dans N3 ; outil gardé tel quel, défauts vus aux jalons (journal, section 2).
- **Constat** : sur les remises refusées de J-C v2 passées par lots de deux tâches, r04 + r05 et r22 + r23 ne passent pas P-2
  (la fille 12 regroupait autrement) ; sans effet sur le lot 2.
- **Déclaré** : les aires du J-C v2 refusé ont été lues avant la fixation des règles (inventaire et registre) ; aucune règle n'en
  est tirée.
- **Lot 1** (constaté à 08:14 UTC, sans effet ici) : `dissimulation-v2.jsonl` (`32f41288…`) et `intention-autres-modes-v2.jsonl`
  (`5b040920…`) présents avec compagnons conformes ; `provenance-v2.md` absent à cette heure. Rien n'a été copié.

## 5. Pour reprendre le lot 2 (une session qui peut lancer des sous-agents)

1. Mettre en place la copie de travail des outils (journal, annexe 2) et rejouer les 8 essais.
2. Seize écrivains neufs Sonnet, deux tâches chacun, au plus deux en cours ; chacun reçoit la consigne
   `consigne-ecrivain-jc-lot2-v1.md`, ses deux entrées (journal, annexe 1), `<PYTHON>` et `<OUTILS>`, les interdits communs v2 ;
   rien de P3-bis.
3. Procédure du journal, section 3 (renvoi par pré-contrôle seul, au plus un par tâche ; aire aux seuls jalons 8, 16, 24, 32 ;
   ≥ 0,90 à 32 → arrêt et rapport).
4. Assemblage `--version v3` dans ce dossier, J-D et J-A copiés à l'octet du lot 1 (empreintes au journal) ; `verifier` complet,
   mêmes entrées scellées, code 0 ; contre-vérification à l'aveugle (32 paires, entropie neuve consignée, clé hors de vue et
   son empreinte écrite avant le lecteur, lecteur neuf Opus qui déclare n'avoir reçu aucun fichier de P3-bis ; seuils du § 9).
