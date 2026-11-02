# Rapport de préparation — réception et lecture du run R1 relancé — v1

Sous-agent de préparation (Fable 5.1), 2 novembre 2026, pour la session conv-audit. Écrit **sans aucune donnée** : aucune
branche `calcul/…` ni fichier sous `donnees/<run>` lu ; aucun `git fetch`, aucun `checkout`, `switch`, `worktree`,
`stash` ni `reset` ; aucun commit, aucun `.sha256` ; aucun fichier existant modifié ; aucun appel de réseau ni de modèle ;
`nice -n 10`. Un seul essai en lecture seule sur les objets git : `git merge-tree --write-tree` (fusion anticipée, voir 2).
Trois fichiers neufs dans ce dossier, à sceller par la session (R6) : la procédure, le script, ses essais ; plus celui-ci.

## 1. Ce qui est prêt

- **Procédure** `procedure-reception-lecture-r1-relance-v1.md` : étapes A à I, chaque bloc avec ce qu'il doit afficher ;
  ordre : constat → arbre de la principale (recréé depuis `origin/analyse-principale-r1-r2-v1`, `83ce7a91`) → récupération
  par la seule refspec `+refs/heads/calcul/r1-r2-reel-v1:refs/remotes/origin/calcul/r1-r2-reel-v1`, « `donnees` = 0 »
  vérifié → fichiers listés et vérifiés par sceau sans ouverture → fiches écrites par le script, contrôlées par les
  lecteurs des deux analyses, scellées et commitées chacune dans son arbre (D2, D3) **avant toute lecture** → lancement
  décisif de la principale → fusion de `52eb34c8` (texte scellé de la lecture par épisode) et lancement de `lecture_v5`
  → fusion dans la branche de travail → secondaire (`lecture_v3`) → verdicts R13 (ce qu'il faut donner à chaque lecteur).
- **Script** `ecrire_fiches_reception_v1.py` (bibliothèque standard seulement, `python -I`) : écrit les deux fiches aux
  clés exactes (`entrees_v1.lire_fiche` : `format`, `redaction`, `R1{moyenne,maximum,complement,resultat}`, `motif_R1`,
  `R2{juge3b,juge8b,motif_juge8b}`, `motif_R2` ; `entrees_v3.lire_fiche_v3` : `R1{moyenne,maximum,manifeste,pointeurs}`,
  `R2{fichier,manifeste,pointeurs}`, `R4: null`), empreintes calculées et confrontées aux compagnons du fournisseur,
  noms attendus seulement, motifs fermés, pointeurs recopiés du code scellé du fournisseur (`29bd8e2e`, clés inchangées
  par l'addendum), aucun `.npz` ouvert ; sous `--ouvrir-resultats`, ouvre les seuls résultats JSON pour résoudre les
  pointeurs, lire `verdict_fidelite`, confronter `fichiers` aux `.npz` versés, et appliquer la **garde E19** :
  `tokenisation.episodes_non_resolus` doit égaler la liste déclarée par l'addendum v2 (`--episodes-non-inversibles-declares`,
  vide par défaut), sinon `ARRÊT` sans fiche ; une liste non vide concordante est écrite dans `redaction` avec
  `a_lazar: true`. Tout est consigné dans `redaction` (qui, quand, commit du versement, addendum v2 par chemin et
  empreinte, ce qui a été ouvert, inventaire des empreintes, empreinte du script). Rien n'est deviné : les noms de runs
  sont des paramètres ; une fiche existante n'est jamais écrasée (R12).
- **Essais** `tests/test_ecrire_fiches_reception_v1.py` : **12 réussis sur 12** en 0,7 s (`.venv`, `nice -n 10`), sur un arbre
  synthétique aux formats du fournisseur (compagnons, corps `{"run_id","manifeste_sha256","resultat"}`) ; cas sain validé
  par les deux lecteurs du dépôt (identiques aux commits cités `a8b7fdb2` et `326601cf`, vérifié par `git diff`) ; sans
  ouverture ; juge 8B absent ; artefacts (R5) : fichier manquant, nom inattendu, empreinte ≠ compagnon, empreinte déclarée
  par le fournisseur ≠ fichier, rejeu arrêté (motif fermé, refus sans `--ouvrir-resultats`), résultat et `arret.json`
  tous deux présents, épisodes non résolus non déclarés (E19), fiche existante, paramètres hors de forme. Les essais
  sont dans ce dossier, pas sous `tests/` du dépôt : un fichier ajouté sous `tests/` de la branche de travail entrerait
  dans la fusion de F et dans `git diff --quiet 5f2f9bf5 HEAD -- src tests` des arbres séparés (la lecture par épisode,
  étape (d), exige 0). À lancer par :
  `PYTHONPATH=src nice -n 10 .venv/bin/python -m pytest -q -p no:cacheprovider brouillons/preuves-mentors-v1/reception-r1-relance-v1/tests/test_ecrire_fiches_reception_v1.py`.

## 2. Ce qui a été vérifié sur le dépôt (sans donnée)

- Empreintes des trois textes scellés : principale `8e267952…` (`origin/analyse-principale-r1-r2-v1` = `83ce7a91`, parent
  `a8b7fdb2`), secondaire `1f6a6da2…` (`origin/analyse-blanche-noire-v3` = `7a238666`, parent `326601cf`), par épisode
  `26a3ff72…` (`prereg/analyse-par-episode-v1.md`, commité en `52eb34c8`, commit cité `5f2f9bf5`).
- Ordre des commits cités : `326601cf` ancêtre de `a8b7fdb2`, `5f2f9bf5` et `52eb34c8` ancêtres de la branche de travail ;
  `git diff 5f2f9bf5 52eb34c8 -- src tests` vide ; `a8b7fdb2 → 5f2f9bf5` n'ajoute que des fichiers sous
  `src/controle_ia/analyse_principale_r1_r2/` et `tests/` (code v3 à v5, essais) : la fusion de F ajoute des fichiers hors
  de la liste fermée de la principale, d'où l'ordre « principale lancée **avant** la fusion ».
- **Fusion anticipée** `git merge-tree --write-tree 83ce7a91 52eb34c8` : code 0, aucun conflit (objets écrits dans le
  dépôt, aucune référence ni arbre de travail touché).
- Aucune référence `calcul/*` dans le dépôt (constat du 2 novembre, inchangé) ; aucun arbre séparé ni branche locale
  `analyse-principale-r1-r2-v1` ou `analyse-blanche-noire-v3` : les deux arbres sont à recréer (B, D3).
- Environnement gelé : Python 3.13.18, numpy 2.4.6, scipy 1.17.1 (`.venv`) ; 2 cœurs, 7 Go.

## 3. Ce qui dépend de l'addendum v2 scellé (paramètres de la procédure)

| paramètre | source | effet si absent |
|---|---|---|
| `ADDENDUM_SHA` | message du fournisseur (n° 260 ou suivant) ; `git show <commit>:prereg/R1-addendum-relance-v2.md \| sha256sum` sur la branche `prep/…` déjà récupérée | A1 arrête (« paramètres remplis ») ; `redaction` cite l'addendum par chemin et empreinte |
| `NON_INVERSIBLES` | liste des épisodes que l'addendum v2 déclare non inversibles (vide attendue : rejeu à graine d'abord, table complète) | garde E19 du script ; une liste non vide va à Lazar avec les fiches (la décision N-A ne couvre que les épisodes nommés) |
| `VERSEMENT`, `REJEU` | message du fournisseur après la course (commit neuf en avance rapide, nom du run) | C arrête si `FETCH_HEAD` ≠ commit annoncé ; rien n'est deviné depuis l'arbre |
| concordance finale (P2) | lecteur neuf sur la version scellée du v2, points 1 à 6 de la dernière section de `concordance-addendum-r1-brouillon3-v1.md`, adaptés : rejeu à graine (deux modes, critère de passage), table v3, validation à l'aveugle sur les 147, seuil d'écart, règle « non inversible » | rien n'est récupéré avant (étape 0.e de la principale ; secondaire 0.g) |
| noms des juges | `20261102-004328-r2-juge3b-reel`, `20261102-005048-r2-juge8b-reel` (addendum v1, brouillon 3, « R2 » : R2 ne se relance pas) | à confirmer par `git ls-tree` en C |

## 4. Ambiguïtés des textes scellés pour la réception (à signaler, sans trancher)

1. **Branche du versement.** L'addendum v1 (brouillon 3, étape 2) fait pousser le script d'instance sur
   `calcul/r1-relance-reel-v1`, puis l'étape 3 « versement » dit `calcul/r1-r2-reel-v1` par commit neuf (comme le brief
   de cette tâche et la principale 0.f). La procédure ne récupère que `calcul/r1-r2-reel-v1` ; si le v2 garde une branche
   d'instance distincte, c'est au fournisseur de verser ; un run absent de `calcul/r1-r2-reel-v1` arrête en C.
2. **« Manifeste » de la fiche secondaire et racine des pointeurs.** Son texte (plan, point 1) appelle « manifeste du
   fournisseur » ce que son point 3 précise être `diag/<run>/rejeu-activations.json` (résultat rattaché), et dit les
   pointeurs « recopiés mot pour mot » du code du fournisseur ; or le corps écrit par `ecrire_resultat` est
   `{"run_id", "manifeste_sha256", "resultat": {…}}`, donc les chemins commencent par `"resultat"` (ses essais utilisent
   des documents plats). Le script écrit `["resultat", "verdict_fidelite"]`, etc., et les résout sous `--ouvrir-resultats` ;
   si la session lisait « manifeste » comme `runs/<run>/manifeste.json`, aucun pointeur ne se résoudrait (arrêt du code).
   Pointeurs écrits : R1 `fidelite_conforme`, `regle_repli`, `textes_sha256`, `couches` (exigés), `contexte_rejeu`,
   `regle_empan`, `modele` ; R2 `invite_sha256`, `contexte_juge`, `modele` (exigés par `exiger_juge_3b`). Les pointeurs
   `fidelite_ecart_max`, `fidelite_tolerance`, `fidelite_actions` ne sont pas écrits : ils désigneraient des nombres de
   `fidelite_toutes` / `fidelite_echantillon`, que le rédacteur de la fiche ne doit pas lire.
3. **Moment du commit de la fiche secondaire.** Son texte veut la fiche écrite « avant toute lecture » et commitée seule
   dans son arbre ; la principale veut sa propre fiche commitée avant son lancement. Les deux fiches sont écrites par un
   seul passage du script (D1) et commitées chacune dans son arbre (D2, D3) avant E : conforme aux deux textes, mais la
   fiche secondaire transite par l'arbre de la principale (copie à l'octet, empreinte vérifiée trois fois) : à dire au
   registre.
4. **Réserve N2 dans la fiche secondaire.** Le brief demande de la « citer par sa fiche » ; le texte scellé de la
   secondaire ne prévoit pas de clé pour cela (`redaction` libre) et N-026 interdit le bras « moyenne » en production. Le
   script ne l'écrit pas (il n'invente aucune clé hors de ce que les lecteurs tolèrent, et `redaction` est libre) ; la
   session peut l'ajouter à `redaction` à la main avant scellement (`"reserve_N2": {"chemin": …, "sha256": "c82b4d00…"}`),
   ou la citer au registre et par le lecteur R13 : à trancher par la session (routine).
5. **Règle d'équité du juge** (`consigne_dans_contexte`). Elle demande un jugement sur le texte du contexte déclaré : le
   script l'affiche (sans l'écrire) ; si la session y voit la consigne ou l'indication privée, la fiche secondaire doit
   porter `R2: null` avec ce motif et la preuve (valeur du pointeur) : cas non couvert par le script (fiche à la main),
   la principale n'ayant pas ce motif (ses motifs fermés : `sorties_non_livrees`, `garde_N029_du_kit`) : divergence
   entre les deux textes si le cas se présente (nœud).
6. **`verdict_fidelite` dans `rejeu-activations.json`.** Le code du fournisseur n'écrit ce résultat qu'avec « conforme » ;
   l'addendum le confirme (formats). Le script arrête sur toute autre valeur (« hors du format annoncé ») plutôt que
   d'écrire `R1` non nul avec un verdict que la principale refuserait : repli explicite, pas silencieux.
7. **Ligne 146 de la principale (E19).** Si `NON_INVERSIBLES` est vide, la ligne vaut telle quelle et aucune décision
   n'est à citer ; si non vide, le lecteur R13 reçoit la décision N-A et la liste ; la procédure ne décide pas si la
   décision de Lazar, écrite pour « les 7 − r épisodes que C-6 laisserait non résolus », couvre des épisodes déclarés non
   inversibles par un addendum v2 (texte neuf) : **à faire confirmer par Lazar avec la liste**.
8. **R4.** La secondaire porte `R4: null` (« run R4 absent », son rejeu n'est pas relancé, C-7) ; la principale ne lit
   pas R4. Rien n'est récupéré de R4 ; son dossier reste sur la branche et n'est pas ouvert.
9. **Arbre de la principale.** Son texte dit `git worktree add -b analyse-principale-r1-r2-v1 <dossier> <commit cité>` ;
   la branche existe déjà chez `origin` au commit du texte scellé : la procédure crée la branche locale depuis
   `origin/analyse-principale-r1-r2-v1` (HEAD = `83ce7a91`, parent = commit cité), sans reset.

## 5. Durées mesurées (données synthétiques, `.venv`, `nice -n 10`, 2 cœurs partagés)

| mesure | résultat |
|---|---|
| essais du script (12) | 0,7 s |
| script sur l'arbre synthétique (11 fichiers hachés) | < 1 s |
| `sha256sum` de trois fichiers de 59 Mo | 0,2 s ; `scellement verifier` sur les trois : 0,3 s |
| génération et écriture synthétiques à la taille réelle (2 400 × 3 × 4 096, trois `.npz` de 59 Mo non compressés) | 3,2 s |
| `lecture_v1.analyser` (principale, non décisif, 2 000 tirages, 200 directions de plancher) à la taille réelle | **9,8 s** (le texte annonce 1 à 5 min avec décompression) |
| `lecture_v5.analyser` (par épisode, non décisif) sur le même arbre | **2,0 s** |
| secondaire | non mesurée ici ; son texte (l. 64) : 5 à 8 min, ≈ 1 Go |

Durées par étape depuis le versement : table finale de la procédure — ≈ 20 à 30 minutes jusqu'aux trois sorties
scellées, puis 15 à 30 minutes de verdicts R13 en parallèle.

## 6. Annexe — ce que je n'ai pas fait

Aucune donnée de R1, R2, R4 ni P3 (les fichiers P3 de l'arbre n'ont été ni ouverts ni hachés) ; aucun `fetch` ; aucun
commit ni `.sha256` ; aucun fichier existant modifié ; l'arbre de travail est tel qu'avant (trois fichiers neufs et
celui-ci, non suivis). Une faute de ma part sans conséquence : une tentative de remplacement de la section H par un
document ici-même (`heredoc`) imbriqué a fait exécuter quelques lignes de la procédure dans un interpréteur de commandes
avec des variables vides ; toutes ont échoué avant d'agir (`checkout` d'une référence absente, `push` d'une refspec vide,
`cd` hors dépôt) ; vérifié ensuite : `git status`, `git reflog`, `git worktree list`, références, aucun changement.
