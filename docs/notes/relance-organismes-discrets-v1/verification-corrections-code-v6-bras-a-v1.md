# Vérification des corrections du code de l'instrument et de l'analyse du bras A, version 6 — v1

**Verdict : engageable après corrections.** Aucun défaut bloquant. Les quatre défauts à corriger de la version 5 sont tenus. Pour C-4, c'est en partie : les contournements de la contre-lecture précédente sont tous refusés ou signalés, mais l'exclusion par défaut de la garde statique en production n'écarte qu'un seul dossier. Des neuf mineurs, six sont tenus et trois le sont en partie (M-2, M-3 et M-6).

Les cinq choix nommés sont obligatoires et sans valeur par défaut, et aucune issue n'est codée en douce. L'événement d'arrêt ne porte que les cinq éléments de la définition unique : aucun nombre, aucun `motif`, aucun `calculable`, sur 25 arrêts provoqués et 290 arrêts tirés au hasard.

Il reste trois défauts à corriger avant le scellement :
- des causes d'arrêt que 6.9 ne nomme pas, dont l'issue dépend de la fiche 12 (C-1) ;
- une même ligne de GO qui ouvre autant de livraisons refaites qu'on veut (C-2) ;
- l'exclusion par défaut de la garde statique, qui ferait parcourir à l'instance d'analyse les dossiers d'internes des moniteurs (C-3).

Les 277 essais passent.

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), le contre-lecteur du code de la version 5. Il n'a écrit ni le code, ni les essais, ni aucun texte du dossier.
- **Code** : commit `b7354129`, branche `claude/pensive-bardeen-1fv7hw`. La tête est passée à `6694300a` (avis du rédacteur du texte) sans aucun changement sous `src/` ni sous `tests/`. Chaque module répond à son compagnon. Empreintes, abrégées :
  - `analyse_bras_a_v6.py` `0f8dbd56…` ;
  - `verdicts_bras_a_v6.py` `7c121e35…` ;
  - `arrets_bras_a_v6.py` `889c9f73…` ;
  - `configuration_bras_a_v6.py` `9cb04d8e…` ;
  - `graines_bras_a_v6.py` `9dffe607…` ;
  - `permutation_etiquettes_bras_a_v6.py` `477f3725…` ;
  - `cloisonnement_bras_a_v6.py` `b8252641…` ;
  - `mesures_bras_a_v6.py` `709785e2…`.

  Les six fichiers d'essais `tests/test_*_bras_a_v6.py` et `tests/aide_bras_a_v6.py` répondent aussi à leurs compagnons.
- **Textes** :
  - brouillons 22 (`ade786eb…`), 23 (`ed7823af…`) et 24 (`12609c04…`) ;
  - note du brouillon 24 (`86e17f6e…`) ;
  - fiches 9 à 12 (`decisions-bras-a-brouillon23-v1.md`, `f20abfed…`) ;
  - note du code v6 (`aa9b0508…`) et relevé v6 (`b1d3c0fa…`).
- **Essais** : la commande de la note donne **277 passés** (40 s) :

  ```
  PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_{graines_bras_a,mesures_bras_a,analyse_bras_a,verdicts_bras_a,permutation_etiquettes_bras_a,cloisonnement_bras_a}_v6.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py
  ```

  L'essai qui passe la garde sur le dépôt élague les chemins interdits avant tout parcours (`_programmes_du_depot_hors_des_chemins_interdits_a_la_relance`, même élagage que le mien) : rien d'interdit n'est ouvert.
- **Essais d'attaque** (bloc-notes, données synthétiques) : `/tmp/claude-0/-home-user-controle-ia-travail/b7727ccc-db8b-5b89-bce1-17602831b69d/scratchpad/contre-lecture-code-v6/`. Chacun a sa sortie `….sortie.txt` :
  - `attaques_regle_v6.py` : 50 cas, avec recherche de fuite dans la chaîne entière des messages d'exception ;
  - `attaques_fichiers_v6.py` : étape (m) et ses constats, arrêts consignés, livraison refaite, issue d'un arrêt ;
  - `attaques_cloisonnement_v6.py` : les 16 modules de la version 5, 6 neufs, 2 « internes » plantés, dans un faux dépôt ;
  - `attaques_graines_v6.py` ;
  - `fuzz_livraison_v6.py` : 400 livraisons altérées au hasard, graine fixe.
- **Heure** : 2026-11-19T16:50Z (`date -u`).

---

## 1. Défauts bloquants

Aucun.

## 2. Défauts à corriger

### C-1. Le code ajoute des causes d'arrêt que la liste de 6.9 ne nomme pas, et l'issue de chacune dépend de la fiche 12
- **Où** :
  - `analyse_bras_a_v6.py:871-882` et `:813-816` (`ranger_une_lecture`) ;
  - `:739-742` (`_les_vingt_lectures`) ;
  - `:1424-1450` (`_defaut_d_une_ligne_de_rang`).
- **Constat**. Tous ces arrêts lèvent le même événement que les refus écrits au texte (essais d'attaque, cas « valeur p arrondie », « aire 1.2 », « lecture hors de sa place », « borne rendue sans quantile ») :
  - valeurs p confrontées à leurs comptes à 1e-9 près ;
  - lecture rangée à une place qui n'est pas la sienne ;
  - nombre hors de 0 à 1 ;
  - borne rendue sans son quantile ;
  - borne remplie au cas E sous les rédactions (a) et (b).
- **Ajout du vérificateur au relevé du rédacteur**. À l'étape (n), des formes **devinées** du fichier des rangs arrêtent aussi :
  - `dose` doit valoir `dose-0.25` … `dose-1.00`, codé en dur, alors que pour les lectures la forme des doses est lue dans la configuration ;
  - `condition` doit valoir « honnete », ou la chaîne de la dose ;
  - `episode` doit être entre 0 et 7, et `pas` entre 0 et 9.

  Si le module écrit la dose autrement dans ce fichier que dans `lectures`, la lecture s'arrête à tort.
- **Pourquoi c'est à corriger avant le scellement** :
  - la rédaction (a) de la fiche 12 fait de tout arrêt la ligne A17 : sous elle, chacune de ces causes peut ôter son issue au désappariement ;
  - un contrôle qui ne figure pas au texte change donc la portée d'une règle que Lazar est en train de trancher ;
  - le premier contrôle (1e-9) peut arrêter à tort si le module arrondit ses valeurs p.
- **Ce qui le réglerait** : inscrire ces contrôles dans la liste des écarts de structure de 6.9 et en 8.4, avec leur précision, avant le scellement et avant que Lazar ne réponde à la fiche 12. C'est ce que recommande le rédacteur, sauf pour le premier. Ou bien les retirer du code. Mettre la forme des champs `dose` et `condition` du fichier des rangs dans la configuration scellée, comme pour les lectures. L'épreuve de forme avant toute dépense doit essayer chacun d'eux.

### C-2. « Une seule fois » : une même ligne de GO ouvre une deuxième, puis une troisième livraison refaite
- **Où** : `analyse_bras_a_v6.py:1059-1074` (`_exiger_lecture_permise`).
- **Essai d'attaque** (`attaques_fichiers_v6.py`). Après un premier arrêt consigné, la ligne `GO-2099-01-01-02` ouvre une livraison refaite. Elle est refusée à son tour, et son arrêt est consigné. La **même** ligne ouvre alors une troisième livraison, qui est lue.
- **Texte** : 6.9, rédactions (b) et (c), « la discrétion se lit alors sur elle, une seule fois » ; relevé du rédacteur, A.2.
- **Pourquoi c'est à corriger** : le texte est muet sur ce que la ligne doit porter. Le code en prend la lecture la plus lâche, et chaque reprise est une occasion de retouche. Faute de règle, la lecture prudente est l'arrêt.
- **Ce qui le réglerait** : refuser une livraison refaite dès que le dossier porte plus d'un arrêt consigné (ou plus d'un arrêt par ligne de GO), et lier la ligne à l'empreinte de la livraison refaite. La règle exacte est à poser au texte, et le relevé A.2 la pose déjà à Lazar.

### C-3. En production, la garde statique parcourt les dossiers d'internes des moniteurs, et peut y arrêter à tort
- **Où** : `cloisonnement_bras_a_v6.py`, `EXCLUS_COTE_HABILITE` (un seul préfixe, `…/bras_a_v2_habilite/`) et `DOSSIERS_GARDES = ("src", "scripts")`.
- **Constat** :
  - Appelée avec ses valeurs par défaut (« l'enchaînement de l'analyse lui donne `src` et `scripts` »), la garde ouvre par programme tout `src/controle_ia/t07/`, `t07bbis/`, `bases/` et `sondes/`, ainsi que `scripts/mots_et_cout_*` et tout module habilité rangé hors de ce dossier. Ce sont des chemins que la relance ne doit pas ouvrir.
  - Dans un faux dépôt, `src/controle_ia/t07/module_interne.py`, qui contient `"scores_par_unite"`, et `src/controle_ia/bases/module_interne.py` sont lus **et refusés** (`attaques_cloisonnement_v6.py`). Sur le vrai dépôt, ces dossiers peuvent nommer la clé `scores_par_unite`, et l'enchaînement s'arrêterait à tort.
  - L'essai du rédacteur ne le voit pas, parce qu'il élague ces chemins lui-même avant d'appeler la garde.
  - Le relevé du rédacteur (F.19) ne vise que le module habilité.
- **Ce qui le réglerait** : porter dans le module l'élagage que l'essai fait (préfixes exacts : `src/controle_ia/t07/`, `src/controle_ia/t07bbis/`, `src/controle_ia/bases/`, `src/controle_ia/sondes/`, `scripts/mots_et_cout_`, le dossier habilité, tout chemin de T0.8), élaguer avant tout parcours, et faire de cette liste le défaut. Elle est à confirmer par la session principale.

## 3. Défauts mineurs

- **M-1. Constats de l'étape (m) contrôlés sur leur seule forme.** Où : `analyse_bras_a_v6.py:1244-1282` (`exiger_fichier_de_l_etape_m`).
  - Essai d'attaque : un fichier de constats écrit à la main avec `journal_de_la_table_a = ["A15"]` et `lignes_de_la_table_a = []` est accepté, alors que `lire_table_a(["A15"]).lignes == ("A15",)`. Une empreinte de configuration inventée est acceptée aussi.
  - Il faut écrire les deux fichiers à la main (fonctions privées et `sceller`) : c'est de la fraude, pas de la mégarde.
  - Correction : relire `lire_table_a(journal)` à la lecture, et comparer les empreintes de la livraison et de la configuration à celles de la pièce donnée à l'étape (n) et de la configuration lue.
- **M-2. Issue d'un arrêt : `issues` se fie à l'argument `arret` de l'appelant.** Où : `verdicts_bras_a_v6.py:648-701`. Avec `arret=None` et `renvoi_base_verifie=False`, `issues` rend toujours « non lue » sans arrêt consigné. C'est la porte de la version 5. À l'inverse, un arrêt consigné à l'étape (n) sous la rédaction (b), omis par l'appelant, laisserait lire la table C. Correction : `issues` lit lui-même le dossier des arrêts consignés.
- **M-3. Mot de refus : une vraie ligne d'accord est refusée à tort.** Où : `graines_bras_a_v6.py`, `MOTS_DE_REFUS` (« refus » cherché comme sous-chaîne). La ligne « Livraison refaite du côté habilité accordée pour le bras A, après la livraison refusée du 20 novembre » est refusée (essai), alors qu'une ligne de ce genre nommera presque toujours la livraison refusée. Le registre lu est celui de l'arbre de travail : sur cette branche, GO-2026-11-19-70 n'y figure pas (essai, réserve 5 du rédacteur). Correction : chercher des formes de refus fixes et entières (« refusé : », « n'accorde pas »), et lire le registre de la branche principale.
- **M-4. Le fichier d'arrêt porte deux champs de plus que la définition unique.** `evenement` et `sha256_de_la_livraison`. Aucun n'est un nombre de la livraison, et l'empreinte sert à refuser une relecture, mais la définition dit « rien d'autre ». C'est à écrire au texte (« l'arrêt est consigné, avec l'empreinte de la livraison »). Autre limite, à écrire : l'exception garde dans sa trace d'appel les variables locales, dont la lecture entière. L'enchaînement ne doit en tirer que `constat()`, comme l'en-tête le dit.
- **M-5. `go_de_la_reprise` n'est pas revérifié par la garde de sortie.** Où : `analyse_bras_a_v6.py:1136-1137` : il est recopié du résultat. Retouché en `GO-2099-01-01-01`, le résultat passe (essai). Correction : relire la ligne d'accord, ou retirer ce champ du résultat.
- **M-6. Le choix « module corrigé » (fiche 11, option (c)) est codé comme l'option (a).** Ce n'est pas une issue en douce : sous (c), la fiche garde « indécis » pour les manques de données. Mais le code ne peut pas savoir que le module est corrigé. La différence entre (a) et (c) repose tout entière sur la version du module. Correction : sous ce choix, exiger dans la configuration l'empreinte du module corrigé, inscrite en 13.1.
- **M-7. Contenus rendus tels quels.** `effectifs`, `exclues` et les aires de l'agrégateur passent dans le résultat sans contrôle. C'est voulu, pour ne pas ajouter de cause d'arrêt (relevé D.16). Un texte quelconque, ou une liste de scores, y passe donc (essai). Ce n'est pas un arrêt manqué, mais le texte dit que l'instance d'analyse ne voit « aucun score, aucun texte ». Correction : rapporter ces champs par leur seule empreinte, ou dire au texte qu'ils sont rapportés tels quels.
- **M-8. Garde statique, contournements restants.** Ils sont déclarés par les limites (b) et (e) : `"-".join(générateur)`, une chaîne à trous faite de variables, un `iterdir` sans extension écrite (ni refusé ni signalé), un nom lu dans la pièce. Le remplacement du générateur d'un tirage authentique par `object.__setattr__` (`_generateur`) n'est pas dans `NOMS_DU_TIRAGE`. C'est de la fraude, et la limite (c) le couvre. Rien d'autre à demander.

## 4. Corrections de la version 5 → tenue ou non

| défaut v5 | jugement | preuve (essai d'attaque rejoué contre v6) |
|---|---|---|
| C-1 règle non liée à la pièce | **tenu** | retouche cohérente du résultat refusée ; une pièce re-scellée change l'empreinte et l'ancien résultat est refusé ; un dictionnaire est refusé. Le re-scellement au même chemin est refusé par `sceller` (R12) ; il faut retirer le compagnon à la main |
| C-2 déclarations de l'appelant | **tenu** (limite écrite) | plus d'argument : elles viennent de la configuration scellée. Une configuration écrite par l'appelant d'après la livraison passe, mais son empreinte est liée au résultat et aux constats. Sa provenance tient au registre (réserve 3) ; le texte doit la nommer (relevé C.8) |
| C-3 trois réglages non lus | **tenu** | statistique, doses de la famille, dose pour information : arrêt nommé chacun |
| C-4 garde statique | **tenu en partie** | des 16 modules de la v5 : 13 refusés, 1 signalé (`glob` + `.jsonl`), 1 témoin sain, 1 limite (b) ; neufs : `getattr`/`vars` sur `_JETON` et `RangsScelles` refusés. Exclusion par défaut → C-3 ci-dessus ; restes déclarés → M-8 |
| M-1 jeton, réemploi | **tenu** | jeton seul et `object.__new__` refusés ; réemploi refusé ; deux tirages refaits de la même clé donnent les mêmes nombres ; fraude par `_inscrire` ou `object.__setattr__` possible (limite écrite) |
| M-2 ligne de GO | **tenu en partie** | registre du dépôt, phrase fixe, une ligne qui refuse ne passe plus ; arrêt à tort sur « livraison refusée » → M-3 |
| M-3 étape (m) | **tenu en partie** | fichier (m) sans constats refusé ; constats écrits à la main sous A15 acceptés → M-1 |
| M-4 formes non reconnues | **tenu** | `lignes` et `champs` de forme inconnue : arrêt à l'étape (n) ; pièce de l'étape (n) exigée égale à celle des constats |
| M-5 dose ¼ et `calculable` | **tenu** | `calculable` faux au cas A, à la dose ¼ : arrêt (étape (m)) |
| M-6 issue d'une livraison refusée | **tenu en partie** | événement nommé ; trois issues par choix, un essai chacune ; l'appelant peut toujours dire « pas d'arrêt » → M-2 |
| M-7 essais manquants | **tenu** | retouche cohérente, garde sur le dépôt (élagage correct), secondes écritures |
| M-8 mélange de versions | **tenu** | la chaîne v6 n'importe pas l'analyse v5 (essai) ; `LONGUEUR_MIN` égale |
| M-9 comptes à virgule | **tenu** | `2000.0` lu comme 2000 ; `1999.5` : arrêt |

Bords du seuil de 1 % (rejoués) :
- **sous « tirages demandés »** : à 19 et 20 tirages dégénérés, cas A ; à 21, cas D.
- **sous « tirages calculés »** : à 20, cas D.
- **à 20 tirages dégénérés exactement**, sous « tirages calculés », un module qui compte encore sur les demandés provoque un arrêt (`motif` en désaccord) : c'est la conséquence écrite dans la fiche 9.

Famille de Holm :
- égalité exacte : `p_haut + 2⁻⁶⁰` donne un arrêt ;
- valeur absente, ou 1 alors que la valeur p est calculable : arrêt.

Cas C, D et E :
- la forme de la version 8 sous « tirages dégénérés » donne un arrêt (garde « intervalle dégénéré seul ») ;
- au cas C, une aire nulle est rapportée « non rendue » ;
- au cas C avec tirages nuls : admis, « indécis » ;
- le cas E suit le choix (« repère », « indécis » ou arrêt de la règle « intervalle impossible ») aux doses de la famille ; à la dose ¼, aucun arrêt.

## 5. Les cinq choix nommés et l'événement d'arrêt (question 2)

**Les cinq choix sont obligatoires et sans valeur par défaut** :
- schéma, seuil, intervalle impossible, moniteur non ajustable, issue ;
- ils sont lus du seul fichier scellé (`configuration_bras_a_v6.lire_la_configuration_scellee`) ;
- un choix absent, vide ou approchant est refusé, et un dictionnaire est refusé ;
- aucune fonction n'a de paramètre de choix par défaut, et aucune valeur n'est écrite dans le code hors des listes de valeurs permises (recherche sur tous les modules v6).

Le seuil de 1 % a un défaut écrit dans la fiche 9 : le code ne l'applique pas lui-même, et c'est à qui écrit la configuration de le porter.

**Aucune issue n'est codée en douce.**
- La ligne A17 n'apparaît que sous le choix « ligne d'arrêt de la course, en entier », dans `table_a_apres_un_arret` et `issues`.
- Sous les deux autres choix, la table A n'est pas touchée.
- Sous (b), une table C passée après un arrêt est refusée.
- Sous (c), un arrêt à l'étape (n) laisse la table C et rapporte les grandeurs de l'étape (n) « non rapportées : livraison refusée (garde : …) ».

Les six issues (trois choix × deux étapes) ont été rejouées.

**Événement**.
- `ArretDeLaLectureDeLaDiscretion` porte la garde ou la règle, le champ, le cas, l'étape, le moniteur et la dose, chacun contrôlé contre une liste fermée à la fabrication. Un champ `aire=0.7` est refusé (essai).
- Sur 25 arrêts provoqués, j'ai cherché dans la chaîne entière des messages (`__cause__`, `__context__`) les nombres et le `motif` de la lecture fautive : aucune fuite.
- La fouille de 400 livraisons altérées au hasard donne 290 arrêts, **tous des événements nommés**, aucune garde ordinaire ni autre exception. Les 110 qui passent ne touchent que des champs sans règle (`plis`, `exclues`, `effectifs`…) ou rendent une valeur égale à celle d'origine.
- Toute garde sur la sortie de la lecture commune donne l'étape (m), y compris à la dose ¼ (essai).
- Réserves : M-4, et l'élargissement du « champ » à six désignations de liste (relevé B.4, à écrire au texte).

## 6. Les deux écarts à mes propositions (question 3)

- **Lecture d'un dossier, signalée sans arrêt** : **acceptable**. Refuser `glob` et ses voisins arrêterait à tort huit programmes légitimes, et ma proposition admettait d'« écrire la limite en clair », ce qui est fait (limite (e)). Deux conditions :
  - la règle « le fichier des rangs est rangé dans un dossier qu'aucun lanceur ne parcourt » est une barrière de cloisonnement : elle doit être écrite au texte (3.5 (b) ou 13.2), pas seulement dans l'en-tête du module ;
  - le contre-lecteur de l'enchaînement doit recevoir la sortie de `listages_a_relire`.

  Un `iterdir` sans extension écrite n'est pas signalé (limite déclarée).
- **Constats de l'étape (m) dans un second fichier scellé** : **acceptable**. Il respecte « trois champs et eux seuls » des conventions. Deux conditions :
  - le texte doit nommer ce fichier (relevé C.10) avant le scellement ;
  - sa lecture doit rejouer ce qu'il affirme (M-1). Telle qu'elle est, elle ne contrôle que la forme.

## 7. Les trois défauts du texte qui touchent une règle (question 4)

- **A.1, contrôles hors de la liste de 6.9** : oui, **ils ajoutent des causes d'arrêt que le texte ne prévoit pas**. J'en ajoute une famille, les formes devinées du fichier des rangs. Voir C-1 : à inscrire au texte avant le scellement, faute de quoi la réponse de Lazar à la fiche 12 porterait sur un ensemble de causes plus large que celui qu'il lit. La borne remplie au cas E se rattache à « une clé qui contredit son cas » (la table dit `borne_haute` `null`) et peut être tenue pour écrite. Les quatre autres contrôles, non.
- **A.2, « une seule fois »** : le code choisit la lecture la plus lâche. Voir C-2.
- **A.3, arrêt à l'étape (n) sous (b)** : le code applique la lettre de la fiche 12 (b), « la table de discrétion déjà scellée est retirée elle aussi » : la table C n'est pas reçue. Aucune cause neuve. C'est bien la différence entre (b) et (c), déjà portée à Lazar.

## 8. Ce que je n'ai pas regardé
- Les parties inchangées depuis la version 5, selon le rédacteur : statistique de la variable principale, tables A et B, déclencheurs, aire conditionnelle (je n'ai relu que le chemin de lecture des rangs), `mesures_bras_a_v6.py` (un import changé, non vérifié par différence), `reponses_lecteurs_v5.py`.
- Les secondes écritures neuves de la statistique (`test_statistique_de_la_variable_principale_contre_des_secondes_ecritures_neuves`), passées mais non relues.
- Les brouillons 22 à 24 en dehors de 6.9 (lignes 700 à 721 du brouillon 24, par recherches) ; la note du brouillon 24, parties 2 à 7 ; les fiches 9 à 12 en entier. Je n'ai lu ni l'avis du rédacteur du texte (commit `6694300a`), ni les notes des brouillons 22 et 23, ni leurs vérifications.

## 9. Fichiers ouverts
- `CLAUDE.md`.
- Dans `docs/notes/relance-organismes-discrets-v1/` :
  - `code-v6-bras-a-note-v1.md`, `defauts-du-texte-trouves-en-codant-v6.md` et `decisions-bras-a-brouillon23-v1.md` (fiches 9 à 12), en entier ;
  - `preenregistrement-v2-brouillon24-note-v1.md`, lignes 38 à 112.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md` : en-tête par recherche, lignes 700 à 721 par recherches ciblées (« Commun aux trois rédactions », définition unique, « Deux sortes d'écart »).
- Code v6, en entier : `configuration_bras_a_v6.py`, `arrets_bras_a_v6.py`, `cloisonnement_bras_a_v6.py`, `graines_bras_a_v6.py`.
- Code v6 en partie : `analyse_bras_a_v6.py` (lignes 556 à 1452) ; `verdicts_bras_a_v6.py` (lignes 508 à 760) ; `permutation_etiquettes_bras_a_v6.py` (lignes 80 à 112).
- Essais : `tests/aide_bras_a_v6.py`, en entier ; `tests/test_cloisonnement_bras_a_v6.py` (lignes 145 à 230) ; `tests/test_analyse_bras_a_v6.py` (lignes 976 à 998) ; liste des essais de `tests/test_verdicts_bras_a_v6.py`.
- Noms de dossiers seulement (`find -printf '%h'`), pour savoir où se trouvent `t07`, `bases`, `sondes` et un éventuel module habilité. Aucun contenu lu, aucune empreinte prise.
- **Non ouverts** :
  - aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ;
  - aucune notice ni contre-lecture du côté habilité, aucune fiche de l'organisme d'idéation, aucune réponse de lecteur, aucune clé ;
  - aucun appel réseau ni de modèle, aucun sous-agent, rien d'installé, rien committé.

  Les essais d'attaque de la garde statique tournent dans un faux dépôt temporaire.
