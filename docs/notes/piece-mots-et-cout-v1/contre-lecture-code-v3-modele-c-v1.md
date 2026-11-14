# Contre-lecture (R2) du code v3 de la pièce « mots et coût » de T0.6 — modèle C — v1

**Déclaration : rédigé sans vue des données de 7b ; aucune sortie de 7a, 7b, T0.7 ou P3-bis lue.** Je n'ai ouvert aucun fichier sous `diag/`, `runs/`, `donnees/`, `essai/`, aucun des chemins interdits de la consigne, aucune recherche récursive, aucune clé, aucun réseau. Tout ce que j'ai joué l'a été sur données factices (fabrique v1), dans le répertoire temporaire de ma session. Dépôt lu au commit `736e5a508c29be0e65ef61b6cd0e8c565eb6a3dd` (vérifié par `git rev-parse HEAD`), arbre propre ; ni `git fetch`, ni commit, ni poussée. Heure de rédaction : 2026-11-14, `date -u` après 14:32Z.

Fichiers ouverts : ceux de la liste fermée ; dans `registres/decisions.md`, les lignes R-2760, R-2763, R-2765, R-2774 (une à une) ; T0.6 l. 560-600 et 755-780 ; la clé `marques_autres_taches` de la configuration de T0.7 v8 (lue seule, par un one-liner, pour juger R-D17) ; `environnements/propositions.py` (`lire_action`) et `t06/cout.py` ; deux `grep` ciblés sur `t06/lanceur.py` (où `cout_action` écrit la colonne `cout_present`). Je n'ai pas ouvert le brouillon de T0.8 ni la section « Métrique » de T0.8 au-delà de ce que cite T0.6.

## 0. Verdict

**Scellable.** Aucun constat bloquant ni majeur. Le différentiel v1 → v3 ne contient que les changements demandés (aucun hunk inexpliqué), C-1, C-2, C-3 sont appliqués et éprouvés sur un cas sain et sur un artefact, C-4 est déclaré, les 65 essais passent chez moi, l'essai de bout en bout passe 25 sur 25, et la forme du fichier JSON et de la ligne est conforme. Trois constats mineurs, dont aucun ne change le code.

## 1. Empreintes recalculées (égales au rapport du développeur, § 1)

`scripts/mots_et_cout_t06_v3.py` `9dbcc55c…` ; `scripts/lancer_mots_et_cout_t06_v3.sh` `e1d2514c…` ; `tests/test_mots_et_cout_t06_v3.py` `2e951ed5…` ; `scripts/banc_mutations_mots_et_cout_t06_v3.py` `b78f5d04…` ; `scripts/essai_bout_en_bout_mots_et_cout_t06_v3.py` `517eedbd…` ; `scripts/fabrique_factice_mots_et_cout_t06_v1.py` `13df3976…` (inchangée). Les compagnons des cinq sorties et du rapport du développeur sont conformes (`sha256sum -c`). Les six fichiers sont déjà suivis par git, arbre propre.

## 2. Point (a) — « coût présent » (R-2765)

- **Définition conforme.** `cout_present(texte) = "COST" in lire_action(texte).champs`. Dans le lecteur gelé, `champs` ne range une clé que si sa valeur, prise jusqu'à la clé suivante et débarrassée de ses blancs, est non vide ; `champs` est vide sans ligne `ACTION` ou pour `REVISE` sans numéro ; une action invalide faute de `TITLE` ou `PROPOSAL` garde ses champs ; la première occurrence non vide fait foi. C'est bien « un coût est déclaré (champ non vide) », sans condition de forme : c'est le mot de Lazar (« coût présent », plus proche du sens courant).
- **Égale à `t06.cout.lire_cout(champ)["cout_present"]`** : `cout_action` appelle `lire_cout(lire_action(texte).champs.get("COST"))`, dont `cout_present = bool(champ.strip())` ; sur une valeur déjà rangée (non vide, sans blancs aux bords), `bool(...)` est vrai si et seulement si la clé est dans `champs`. Égalité par construction, éprouvée cas par cas (seize textes limites, dont la valeur vide, la clé en minuscules, le gras, la double occurrence) et action par action sur les 5 760 actions factices ; la colonne `cout_present` des mesures est écrite par `cout_action` dans `t06/lanceur.py` (ligne 284).
- **Redondance (constat, pas une raison de changer la lecture).** Le trait (c) de (B) est **la même quantité que le trait 7 de la base (A)** (`FORME_COUT[0]`). Donc (B) ne tient d'un renseignement que (A) n'a pas **que par le sac de mots** (a) ; le trait (c) lui-même ne porte rien que (A) n'ait. Au sein de (B), `cout_present = 0` entraîne `illisible = 1` (coût absent donc illisible) : le trait ne sépare que, parmi les actions de coût illisible, « champ absent » de « champ présent sans nombre lisible positif ». Si presque toutes les actions de 7b portent un champ COST, le trait sera constant et retiré.
- **Règle du trait constant** : appliquée sans changement (`ajuster`, égalité exacte sur l'apprentissage du pli) ; le trait est retiré de l'ajustement, compté dans `traits_retires`, absent des coefficients, non lu à la notation ; le modèle reste calculable par ses autres traits (essai `test_cout_present_constant_retire_de_l_ajustement`, mutation M83). Conforme.
- Plus aucune trace de la lecture v1 : `grep` ciblé sur `unite|SUFFIXE_K|LETTRE` dans le module : zéro occurrence ; dans les essais, la seule occurrence est l'assertion « aucun coefficient ne commence par `unite` ».

## 3. Point (b) — C-1, C-2, C-3, C-4

| couple | appliqué comme demandé (§ 6 de la contre-lecture v2) | cas sain / artefact (R5) | verdict |
|---|---|---|---|
| **C-1** code 3 | essai `test_c1_codes_de_sortie_de_main` : `main executer --mode jouet`, `calculer` remplacée par (a) une `ArretPiece`, (b) une `KeyError` : retour 3, `diag/<run>` = fichier d'arrêt et compagnon seuls, empreinte du compagnon égale, phrase BA-L0, manifeste écrit et cité ; refus avant manifeste (arbre sale ; erreur inattendue) : 2, rien d'écrit ; cas sain : 0, cinq lignes, sans décimal ; dépôt jetable commité entre deux appels | sain : code 0 ; artefacts : M66 (`return CODE_REFUS` à la place de `CODE_ARRET`, exactement la mutation demandée), M67 (seules les gardes rattrapées), M68 (fichier de plus) | conforme |
| **C-2** `contre_lecture` obligatoire | `lire_fichier_code` exige la clé, chemin relatif au dépôt, non vide, sans « .. », forme exacte `{chemin, sha256}` ; `controler_code` la vérifie toujours (présente, empreinte, compagnon) ; `ecrire-fichier-code` refuse sans `--contre-lecture` ou hors du dépôt, rien n'est écrit (code 2, essayé en ligne de commande) ; fixture `depot_reel`, dépôts jetables et bout en bout fournissent une contre-lecture factice scellée | sain : écriture puis lecture, empreinte égale ; artefacts : `code_sans_contre_lecture`, `contre_lecture_alteree`, `contre_lecture_absente`, `contre_lecture_chemin_absolu` dans `test_garde_registre_et_code_artefacts` ; M69 à M73 | conforme |
| **C-3** aucune valeur | les neuf motifs de `valider_issue` qui interpolaient une valeur ne nomment plus que le champ (relus dans le fichier : les motifs restants ne contiennent que le nom de dose, une constante `sorted(CLES_ISSUE)` ou `sorted(BASES)`, jamais une valeur lue) ; essai qui force **les vingt refus** de `valider_issue` un à un (j'ai compté vingt `raise` dans la fonction ; l'essai exige vingt motifs distincts, aucun décimal, aucune valeur forcée) ; sortie et progrès du mode réel sans décimal | sain : issue valide acceptée avant les altérations ; artefacts : M74 à M77 (valeur réinjectée dans un motif), M78 (aire imprimée sur la sortie), M79 (aire imprimée dans le progrès) | conforme |
| **C-4** déclaration | rapport du développeur § 4 : la garde de l'arbre ne voit que les fichiers non suivis et non ignorés (`--ignored` non ajouté, à raison) ; arrêt avant manifeste si `diag/<run_7b>/arret.json` existe (test d'existence, jamais ouvert), déclaré dans le sens prudent | sans changement de code, comme demandé | déclaré |

Banc : j'ai lu les définitions de M66 à M83 dans `scripts/banc_mutations_mots_et_cout_t06_v3.py` : M66 à M68 visent C-1 ; M69 à M73 visent C-2 ; M74 à M79 visent C-3 ; M80 à M83 visent le point (c) lu « coût présent » (action non valide, autre champ, compte des écarts, trait constant) ; M51 et M63 (anciennes) sont réécrites pour « coût présent ». Chaque ancienne chaîne est à remplacer une seule fois (le banc le contrôle) ; la sortie versée dit 83 tuées sur 83, témoin vert (64 réussis, 1 sauté), aucune survivante. Je n'ai **pas** rejoué le banc (consigne).

## 4. Point (c) — différentiel v1 → v3 (`diff` du module et du lanceur ; essais lus par `diff` v1 → v3)

Module : chaque hunk est expliqué par l'un des quatre motifs permis. (1) en-tête et docstring : liste des différences (texte) ; (2) `VERSION`, `COMMANDE`, `FICHIERS_PIECE`, `FICHIERS_ESSAIS` : noms v3 ; (3) point (c) : commentaire, `TRAITS_B_COUT`, `REGLAGES_B["forme_champ_cout"]`, retrait de `SUFFIXE_K` et `LETTRE`, `cout_present`, `matrice_b(…, present, …)`, `Contexte.cout_present`, appels, dernier appel du mode jouet ; (4) `DECLARATION` (mots v3 et deux développeurs) ; (5) C-2 : `lire_fichier_code`, `controler_code`, `ecrire_fichier_code` ; (6) C-3 : motifs de `valider_issue` ; (7) fichier des détails : `cout_present_par_condition` et le compte descriptif neuf `cout_present_ecarts_a_la_colonne_des_mesures` (lu par aucune règle : `grep` confirme qu'il n'apparaît que dans le module, pour l'écrire, et dans l'essai de bout en bout, pour le vérifier) ; (8) le message de fils de calcul cite le lanceur v3 ; (9) description de l'argument-parser `(v3)`. **Aucun hunk de fond inexpliqué** : ni calcul de (A) ni de (B) hors du point (c), ni règle, ni réglage, ni garde, ni code de sortie, ni entropie. Lanceur : seule la cible change. Essais : seuls ajouts les cinq essais neufs, quatre artefacts, deux lignes « sans décimal », la contre-lecture factice de la fixture, la recopie des marques (R-D17) et le passage de `ecrire_fichier_code` au nouveau contrat.

## 5. Point (d) — rejeux

- Essais : `cd … && . .venv/bin/activate && PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_mots_et_cout_t06_v3.py` : **65 réussis sur 65**, 149,8 s.
- Essai de bout en bout (`PYTHONPATH=src python -P -B scripts/essai_bout_en_bout_mots_et_cout_t06_v3.py <dossier du répertoire temporaire de ma session>/x`) : **BILAN : 25 conformes sur 25** (79 s), sortie de la pièce sans décimal, `cout_present` égal à la colonne des mesures factices, `ecrire-fichier-code` sans `--contre-lecture` refusé, `verifier-code` conforme.
- Le banc : non rejoué ; mutations M66 à M83 vérifiées visant C-1 à C-3 et le point (c) (§ 3).

## 6. Point (e) — réserves

| réserve | jugement |
|---|---|
| R-D7 (fils de calcul fixés à 1, écart d'environ 2·10⁻⁷ possible sur un coefficient de (B) si T0.8 recalcule autrement) | **gardée** ; à reporter dans T0.8 par la mère |
| R-D8 (clés `tache/<id>` du manifeste) | **gardée, confirmée** par le développeur sur le code gelé ; rien à corriger |
| R-D13 (R4, témoin rouge de la v1, cause non établie) | **gardée pour mémoire** ; la première passe v3 est verte (83 sur 83) ; la mère rejoue le banc entier au calme |
| R-D14 (suite complète du dépôt non jouée) | **gardée**, relève de la mère avant commit final |
| R-D15/16 (brouillon de T0.8 du compte 4 ; forme de la ligne `CODE-MOTS-ET-COUT-T06`) | **gardées, à aligner dans T0.8 avant son scellement** : le contrat lit désormais `cout_present` au point (c), la ligne cite un JSON, le module vit sous `scripts/` ; sinon le contrôle d'identité de M2 sur (B) diverge |
| R-D17 (marques de T0.7 recopiées, configuration non ouverte) | **sans objet** : j'ai lu `marques_autres_taches` de la configuration v8 : `['T06', 'T08', 'P3BIS', 'NARC']`, égal à `MARQUES_T07` des essais ; l'essai de compatibilité est plus faible en méthode, non en valeur |
| R-D18 (clone superficiel) | **levée par la mère, confirmée** : `git rev-parse --is-shallow-repository` = false, `git merge-base --is-ancestor c2fab6cc HEAD` = ancêtre, `git diff --stat c2fab6cc HEAD -- src/controle_ia` vide ; aucun fichier de la pièce sous `src/controle_ia/` |
| R-D19 (compte des écarts texte/colonne) | **gardée** : descriptif, sans seuil ni arrêt ; un compte non nul sur 7b signalerait que le texte conservé diffère de celui mesuré ; à la mère de le lire seulement après la sortie de la pièce |
| R-D20 (la tête a avancé) | **sans objet** (aucun fichier de la pièce n'en dépend) |

## 7. Point (f) — fichier JSON et ligne `CODE-MOTS-ET-COUT-T06`

Conforme. Clés `commit`, `contre_lecture`, `declaration`, `essais`, `fichiers` : ensemble exigé et permis par `lire_fichier_code` v3 ; `fichiers` = exactement les deux fichiers de la pièce (`FICHIERS_PIECE`) ; `essais` = les quatre fichiers d'essais, dont la fabrique v1 ; `declaration` = `DECLARATION` du module, qui porte « sans aucune vue des données de 7a, de 7b ou de T0.7 » pour l'auteur et dit que le contre-lecteur « y déclare n'avoir ouvert aucune de ces données », ce qu'exige T0.6 l. 768 (« le fichier cité … porte cette déclaration ») : **la déclaration du contre-lecteur est la première ligne en gras de ce rapport**, qui doit être le fichier cité sous `contre_lecture`. Commande `ecrire-fichier-code . COMMIT SORTIE --contre-lecture RAPPORT` conforme à l'usage du module ; écriture en clés triées, retrait 1. Ligne au format du registre (`| CODE-MOTS-ET-COUT-T06 | date | chemin | sha256 |`), sous `registres/code-mots-et-cout-t06/` ; `verifier-code` d'abord sur un commit tête ou ancêtre. Points d'ordre que la mère doit respecter : (i) le rapport cité (celui-ci) est commité et ne change plus (le JSON en porte l'empreinte) ; (ii) `COMMIT` porte les six fichiers inchangés ; (iii) un fichier ou une ligne écrit(e) avant que tout cela soit commité est refusé par `verifier-code`.

## 8. Constats

Aucun bloquant. Aucun majeur.

**Mineurs (aucun ne demande de corriger le code) :**
- **m-1** — *Redondance du trait (c).* `cout_present` de (B) est la même quantité que le trait 7 de (A) et ne sépare, dans (B), que « absent » de « présent sans nombre lisible » parmi les coûts illisibles (§ 2) ; probablement retiré comme constant sur 7b. Conséquence de la lecture tranchée par Lazar, à signaler dans le rapport de la pièce quand les détails (`traits_retires`) seront lus ; pas une raison de changer la lecture.
- **m-2** — *Portée de C-3.* L'invariant « aucune valeur » vaut pour les motifs de `valider_issue`, la sortie et le progrès, comme demandé ; d'autres arrêts de la pièce (lecture des entrées de 7b : l. 650-763, 842, 1016, 1072, 1136) citent encore des éléments **structurels** des entrées (identifiants de tâche ou d'épisode, effectifs, formes, types, jamais une aire, un score ni un taux). Cohérent avec la consigne, à ne pas présenter comme « jamais aucune valeur » dans un texte d'ensemble.
- **m-3** — *Reste de la remarque v2 non reprise.* `M.scellement.verifier(chemin_m)` reste hors du `try` (une panne à cet endroit laisserait un manifeste écrit sous un code 2) : déclaré par le développeur, improbable, laissé à la mère ; je ne le juge pas bloquant.

## 9. Ce que je n'ai pas pu vérifier

La forme réelle des fichiers de 7b (par construction) ; le contenu du brouillon de T0.8 (R-D15/16) ; le rejeu du banc entier (consigne) ; la suite complète du dépôt ; `code_t07_v1 verifier` sur l'arbre réel (levée par la mère, R-2774, recoupée ici par l'ascendance de C7 et l'absence d'écart sous `src/controle_ia/`). Aucun refus de permission ni du classifieur.

*Déclaration : rédigé sans vue des données de 7b ; aucune sortie de 7a, 7b, T0.7 ou P3-bis lue.*
