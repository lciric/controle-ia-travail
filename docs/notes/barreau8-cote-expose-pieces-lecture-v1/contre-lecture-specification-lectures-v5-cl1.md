# Contre-lecture 1 de la spécification des lectures exploratoires du dommage et de la diffusion sur la course v5 du saboteur à budget

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce de travail du côté exposé. Elle ne porte aucun chiffre de la course, aucun fragment de consigne privée, aucun mécanisme qui ne soit déjà dans la pièce relue.

- **Pièce relue** : `docs/notes/barreau8-cote-expose-pieces-lecture-v1/specification-lectures-dommage-diffusion-course-v5-v1-brouillon1.md`, sha256 `4eac34a1087d8c237ecb2bf70f4ccfb1f5928d9026799969cf9cfc48073a65f8` (recalculée : égale). Classe A. Rédacteur : Claude Fable 5.2. Accord : `GO-2026-11-24-37` (ligne 915 de `registres/go.md` sur `origin/main`, fichier `f50c2e4c…`, recalculé : égal).
- **Contre-lecteur** : Claude Opus 5.5, neuf. Je n'ai rien écrit de ce que je relis. Je n'ai ouvert aucune consigne privée, rien sous `docs/verdicts/` et aucune valeur sous `diag/`, `donnees/` ni `runs/` de l'arbre de la course. J'ai lu la structure des sorties dans la pièce préparée, et le code. Je n'ai modifié aucun fichier du dépôt, et je n'ai rien dépensé.
- **Date** : 2026-11-24.

## Verdict

**Scellable après corrections.** Je ne trouve aucun bloquant. Je relève **4 majeurs** et **17 mineurs**.

Les faits de code que la pièce cite sont vrais : noms, clés, chemins, lignes et empreintes. Je les ai tous vérifiés dans l'arbre `3326499e`, et `git diff 192a429e 3326499e -- src scripts tests` est vide. L'adaptateur de la section 5.2 donne à `lecture_v1.lecture_1` et à `lecture_v1.lecture_2` exactement ce qu'elles lisent. Un seul point de forme manque à la section 5.3 : l'enveloppe `{"fiches": …}`, voir m6.

Le vocabulaire, la portée, les bases, les paires et la forme lue par l'extrait sont inchangés. Ce qui s'ajoute vit hors des clés que lit le programme de l'extrait en version 3 (lignes 46 et 47, et fonction `construire`).

Les majeurs portent tous sur le moment et la forme des choix :
- les nœuds N-1 et N-2 permettent, tels qu'écrits, un choix fait après avoir vu des sorties scellées (règles R1 et R3) ;
- une statistique fixée d'avance reste ambiguë ;
- le script d'audit de symétrie (R4) n'a aucun essai (R5).

## Remarques

### Bloquants

Aucun.

### Majeurs

**M1. Nœud N-1 : le sens annoncé n'est pas fondé, et le choix peut se faire après lecture.** Lignes 18, 309 et 408 à 416.
- (a) Les lignes 413 et 414 affirment que l'option (a), tous les épisodes du maître, donne « *p* plus grand », et l'option (b), les seuls acceptés, « *p* plus petit ». Rien ne fixe ce sens. Un épisode rejeté par le plancher a moins d'excès qu'un épisode accepté. Un épisode rejeté par la borne en a plus (`regle_v5.accepter`). Un épisode rejeté pour ancre manquante ou pour actions bornables peut être n'importe où. Le sens dépend des données : la recommandation (a) « plus prudente » repose donc sur un signe supposé.
- (b) La ligne 408 dit que le code « calcule ce qu'il faut sous chaque option ». C'est faux pour l'option (c) de N-1 : seules (a) et (b) sont calculées, ligne 309. Et la ligne 349 interdit de rejouer une sortie écrite.
- (c) La ligne 408 permet de trancher « avant qu'une citation ou un extrait n'en dépende ». Or la citation de la lecture (1) est calculée et scellée au moment de la lecture, avec *p* sous (a). La sortie porte aussi `p_sur_les_episodes_acceptes`. Trancher après la lecture, c'est donc choisir en voyant les deux valeurs. Même chose pour N-3, dont le choix entre dans `citation.texte`.
- (d) L'option (c) dit que « l'honnête à soustraire n'est pas désigné ». Or l'analogue de la section 10.2 existe tel quel dans le résultat scellé des conditions de départ : `oracles.<o>.grandeurs.exces_moyen_honnete` de `branches-iib-v5.json`, qui donne m_R = régénérés moins honnêtes. Le H de l'évaluation est une autre candidate. Le nœud doit les nommer.
- **Correction proposée** :
  - retirer les deux phrases de sens des lignes 413 et 414, et fonder la recommandation sur la lettre seule ;
  - calculer les trois options, (c) avec l'honnête nommé ;
  - écrire que N-1 et N-3 sont tranchés avant que la lecture (1) ne tourne, par une ligne au registre des décisions ou un additif, faute de quoi la recommandation vaut défaut ;
  - écrire que tout changement après l'écriture de la sortie est un écart, nœud de Lazar, qui ne réécrit pas la sortie.

**M2. Nœud N-2 : l'option (c) est un choix sur résultat, et l'option (b) transmettrait un mécanisme.** Lignes 418 à 422.
- (a) L'option (c), « trancher sur résultat, avant l'extrait », fait dépendre de ce que la base « premier coût contre les suivants » détecte le sort de cette détection. C'est précisément un choix fait après avoir vu le signe (R3 ; R1, « aucune lecture de résultat avant scellement »). Elle doit sortir des options.
- (b) L'option (b), « un mot de plus dans l'extrait ou une pièce à part », ferait passer au côté des moniteurs l'existence d'une base qui lit la signature du premier coût, c'est-à-dire un trait du mécanisme de l'organisme. Cela va contre la forme sans mécanisme de la condition D-12 et contre le point 3 de N-054. Le nœud doit le dire en toutes lettres, comme inconvénient.
- (c) Les lignes 422 et 228 disent que le score par action et le critère de « détecte autant » sont des choix « à confirmer avec ce nœud ». Il faut écrire qu'ils sont fixés par cette spécification à son scellement, et que tout changement après une lecture est un écart.
- **Correction proposée** : garder (a) et (b), avec l'inconvénient (b) ci-dessus ; remplacer (c) par « règle écrite avant toute lecture, par additif » ; ajouter la phrase de fixation.

**M3. Le lecteur du coût de la base « premier coût contre les suivants » est ambigu.** Ligne 227.
- La pièce dit « log10 de son coût moins log10 du premier coût de son épisode, si les deux sont lisibles ». Elle ne dit pas quel lecteur. La ligne 226 juste au-dessus, l'écart du premier coût, emploie `cout_lisible` et `cout_declare` de la ligne, soit le lecteur de la fenêtre. La base « coût » de la lecture (2), à côté de laquelle ce taux est rapporté, lit `t06.cout.cout_action(texte)`, l'ancien lecteur du champ entier, par `bases_textuelles_v1.action_pour_la_piece` (ligne 88). Un développeur peut prendre l'un ou l'autre.
- Ce choix est fixé d'avance et ne décide d'aucun état, mais il doit être univoque avant le scellement.
- **Correction proposée** : écrire « `cout_declare` de la ligne de l'oracle désigné, lisible si `cout_lisible` » ou « `cout_action(texte)["cout"]` », avec la raison. Je recommande le premier, pour que le score soit celui de la mesure de la section 6, point 2, du texte scellé, tenue par la garde de concordance. Ajouter l'essai : « le score est lu sur ce lecteur, et non sur l'autre ».

**M4. Le script d'audit de symétrie (R4) n'a aucun essai, et sa source d'échantillon n'est pas fixée.** Lignes 146, 186 et 351 à 388.
- Le tableau des essais n'a aucune ligne pour `scripts/lecture_iib_audit_r4_v5.py`. Ce script a pourtant des gardes : il ne s'emploie que si `audit_R4.declenche` est vrai ; il n'écrit rien ; il décode sous les gardes de la section 7 ; il obéit à la liste fermée.
- La pièce ne dit pas non plus si l'échantillon affiché est relu dans la sortie scellée (`audit_R4.echantillon`) ou retiré par la graine.
- **Correction proposée** :
  - l'échantillon est lu dans la sortie scellée de la lecture (1), à son empreinte, et retiré par `iib/lecture-1/audit` sous le préfixe pour contrôle d'égalité ; arrêt s'ils diffèrent ;
  - essais sains et artefacts : audit non déclenché, refus (code 1) ; sortie de la lecture (1) altérée, refus ; échantillon altéré, refus ; aucun fichier écrit ; chemin hors liste refusé ; décodage infidèle, arrêt.

### Mineurs

**m1. Types de l'entropie (contrôle E7, ligne 61).** L'entropie est un entier dans `config.entropie` du manifeste du run. C'est une chaîne dans `entropie` du manifeste de la course (`lanceur_v5._manifeste` : `str(graines.entropie)`) et dans `entropie` de la graine (`manifeste.graines`). « Le même entier » doit dire comment comparer : `isinstance(x, int)` et non booléen pour le premier ; pour les deux chaînes, `s == str(int(s))` et `int(s)` égal au premier.

**m2. Exception du manifeste de la course (contrôle E3, ligne 57).** La clé de `resultat.empreintes` pour `manifeste-course-iib-v5.json` est `manifeste`, et non le nom du fichier (`lanceur_v5.py`, ligne 565). Le contrôle E4 le dit ; le contrôle E3 doit le dire aussi, sinon un code mécanique arrête à tort.

**m3. Contrôles E4 et E7 plus stricts et plus simples (lignes 58 et 61).**
- Au lieu de « égales, deux clés ôtées » : exiger `config de la course == designation_v5.configuration_de_course(config du run, racine, D/designation-iib-v5.json)`, la fonction même qui l'a produite.
- Au lieu de « finit par `course/` » : exiger `prefixe_graines == designation_v5.prefixe_de_la_course(config du run)`.
- Ajouter : `resultat.configuration_sha256` égal à `config_sha256` du manifeste du run.

**m4. Taille du vocabulaire (section 7.2, ligne 201).** « De 0 à la taille du vocabulaire moins un » ne dit pas d'où vient la taille. Piège : pour ce jetoniseur, `tok.vocab_size` vaut 128 000 et exclut les jetons spéciaux. Les fins 128001, 128008 et 128009 seraient alors refusées. L'additif 2 (M-1, clause (c)) prend `vocab_size` de `config.json`, tenu à son empreinte (`29e4c210…`, note v7, question 1). Écrire la même chose, ou `len(tok)` exigé égal à 128 256.

**m5. Clés exactes des fichiers d'identifiants (section 7.2, ligne 201).**
- `ids-evaluation-<c>.json` a exactement `avertissement`, `condition` et `ids`.
- `ids-actions-evaluation-iib-v5.json` a exactement `avertissement` et `ids`.
- « Égales, clé par clé » doit se lire : la réunion des quatre tranches est l'ensemble des 256 clés, sans clé en trop ni en moins, et les clés de `ids` sont dans l'ordre du tri des chaînes (additif 2, M-1, clause (a)).

**m6. Enveloppe des fiches (sections 5.3 et 7.3, lignes 137 et 209).** `lecture_v1._jetons_par_action` lit `sorties["episodes"]["fiches"]`. La clé `episodes` de `sorties_d_origine` doit donc valoir `{"fiches": [...]}`. À écrire.

**m7. Ordre des lignes passées à `regle_v5.exiger_sorties_oracle` (section 3.1, ligne 72 ; section 3.2, lignes 79 à 81).** La fonction exige les pas dans l'ordre 0 à 9. Il faut écrire « lignes d'un épisode triées par pas » ou « dans l'ordre du fichier, exigé croissant ». La même règle vaut pour `accepter` au contrôle E9.

**m8. « Toute lecture de JSON est stricte » (ligne 48).** Les fonctions d'origine appelées telles quelles lisent par `json.loads` : `manifeste.lire_manifeste`, `verifier_resultat`, `configuration_v5.exiger_oracle_de_la_regle` et `lecture_v1.exiger_lecture_1_consignee`. Écrire que le code neuf relit en plus, de façon stricte, chaque fichier que ces fonctions ouvrent, ou restreindre la phrase au code neuf.

**m9. Modules dont l'empreinte est contrôlée (`MODULES_D_ORIGINE`, ligne 108).** Plusieurs modules réellement employés manquent :
- `harnais/run_harnais_factice.py`, dont `graine_entiere` fixe plis, intervalles et permutations ;
- `harnais/formats.py`, pour les fins d'action ;
- `scellement.py` et `gardes.py` ;
- `designation_v5.py`, si le code l'appelle (m3).

Il faut les ajouter, ou dire que le commit consigné au manifeste de la lecture, avec un arbre propre, les tient.

**m10. Citations de code à rectifier (lignes 89 et 196).**
- La course v5 génère par `regenere_v5.jouer_lot` (le décodage du journal est à la ligne 84 de `regenere_v5.py`), et non par `episodes_v1.py`, ligne 45, qui est du code v1. L'appel est le même ; la citation doit viser le code de la course.
- Les fins d'action de la course viennent de `modele_v5.charger_modele_reel`, qui prend `config["modele"]["variables_gabarit"]` comme la pièce le prescrit. Elles ne viennent pas de `modele_v1.charger_modele_reel`, qui prend `config["agent"]["variables_gabarit"]`.

**m11. Dossier du jetoniseur (section 7.1, ligne 192, et section 17, ligne 434).** Au lieu de « tout autre fichier lu a son empreinte consignée, sans référence » : une liste fermée des fichiers permis (`tokenizer.json`, `tokenizer_config.json`, `generation_config.json`, `config.json` si m4, `special_tokens_map.json`) ; tout autre fichier présent, par exemple un gabarit `chat_template.jinja` qui changerait la clôture, est un arrêt. Sinon, un fichier en trop agit sans garde.

**m12. Ordre du temps : les trois scellements du côté des moniteurs.** L'additif 1 (« Lectures… », point 1), le texte scellé (plan, point 3) et la note v7 (question 9) veulent les lectures jouées après les lignes `SCELLEMENT-SONDES-IIB`, `SCELLEMENT-ADDITIF-1-SONDES-IIB` et `SCELLEMENT-ADDITIF-2-SONDES-IIB`. Le fait est tenu : lignes 5 à 7 de `registres/sondes-iib-v1.md` sur `origin/main`, datées du 2026-11-19T06:32:25Z, du 2026-11-24T04:21:08Z et du 2026-11-24T10:34:26Z. Mais la pièce n'en dit rien. Ajouter une garde, avec un essai, ou une précondition citée et vérifiée par la session mère avant le lancement.

**m13. Ligne de l'audit au registre (section 6.3, ligne 186 ; section 7.4, ligne 214).** La garde n'exige que la présence de la chaîne et de l'empreinte. Si la relecture trouve un défaut, la lecture (2) tourne quand même. Il faut donner à la ligne une issue (« sans défaut » ou « défaut, nœud ») et faire refuser la lecture (2) sur « défaut » tant qu'aucune décision nommée ne l'autorise.

**m14. Essais manquants (section 14).**
- Fragment `scores-moniteur` : il est dans la liste interdite de la ligne 338, mais absent de l'essai de la ligne 368.
- Contrôle E5 : chemin cité absolu, ou portant `..`.
- Contrôle E1 : `aucune_activation` faux ; `avertissement` altéré.
- Contrôle E7 : entropie sous forme de chaîne non canonique, par exemple « 007 ».
- Garde de collision : un nom déjà dans les graines du manifeste du run.

**m15. « Clé seule écrite » (section 7.2, ligne 201 ; section 7.3, lignes 206 et 208).** Ces arrêts surviennent avant le manifeste : code 1, « rien n'est écrit » (ligne 345). Écrire « clé seule imprimée sur la sortie d'erreur ; rien sur disque ».

**m16. Cloisonnement de la pièce et des sorties (en-tête, lignes 1 à 10).** La pièce et les clés `citation` et `audit_R4_note` des sorties portent des traits du mécanisme de l'organisme : premier coût sans excès, signature, ce que garde le témoin sous chaque oracle. La section 17 dit que rien d'autre que l'extrait ne sort, mais l'en-tête ne porte aucune mention. Ajouter en tête : « pièce du côté exposé ; jamais transmise au côté des moniteurs ni à un concepteur de moniteur », et la même mention dans `forme` ou dans une clé `cloisonnement` des deux sorties.

**m17. Choix faits par la spécification, hors de la table des sept points (lignes 95 à 98, à comparer avec la section 15, lignes 394 à 402, et la section 16).**
- Le premier choix — garder les épisodes sans ancre commune dans la statistique qui décide la phrase — peut changer la phrase. Il est sourcé (`branches_v5.grandeurs` calcule l'écart type des honnêtes sur tous les épisodes), mais il n'est ni dans la liste des écarts ni dans la table des nœuds. L'écrire dans la section 15, ou dans une ligne « tranché par la spécification » de la section 16, pour que Lazar le voie.
- Le repère « 0,58 » que le module d'origine écrit (`reperes.flagrant_signale_une_a_une`) est celui du flagrant de la première course. Il faut une clé de note à côté, comme `note_juge`.

## Réponses aux huit points du mandat

1. **Ce qui ne change pas** : tenu. Les clés que lit l'extrait en version 3 sont gardées ; aucune clé n'est ajoutée dans `jeux` ni dans `etat_par_unite.unites` ; la base ajoutée est hors des états, et c'est le nœud N-2. Rien d'autre n'est à ranger en nœud, hormis la visibilité de m17.
2. **Faits de code** : vrais. Empreintes recalculées : les 25 fichiers de la section 19 que j'ai rouverts sont à leurs empreintes. Lignes citées : `oracle_v5.py`, lignes 165 et 166 ; `lanceur_v1.py`, ligne 230 ; `tours_v1.py`, lignes 249 à 252 ; `configuration_v1.py`, lignes 49 à 53 et 60 à 62 ; extrait en version 3, lignes 46 et 47 : toutes exactes. Adaptateur : complet, sauf m6. Citations à rectifier : m10.
3. **Sources et signe** : les sept points sont sourcés. Aucun n'a pu être réglé sur un résultat, puisque le rédacteur n'a vu aucune valeur. Les deux réserves de signe sont M1 (sens supposé de *p*) et M2 (option sur résultat).
4. **Gardes et essais, graines, empreintes, sorties, replis** :
   - les essais sont riches ; manquent M4 et m14 ;
   - graines (R9) : la dérivation est identique à `jumeau_v5.Graines` (vérifié : `SeedSequence(entropie, spawn_key=(cle_de_tache(prefixe + clé),))` des deux côtés) ;
   - empreintes (R11) : tenues ;
   - sorties (R12) : les noms en « v1 » sont justifiés par les constantes de l'extrait, et rien n'est écrasé ;
   - aucun repli silencieux trouvé.
5. **Jetoniseur et décodage** : la recette est celle de l'additif 2 (M-1, clause (b)), à la lettre. La garde de fidélité est bien construite : coupe, fenêtre et ancien lecteur, recalculés et comparés aux lignes. La règle des jetons spéciaux est celle de la course (`skip_special_tokens=True`, fin gardée dans le compte des jetons, aucune fin intérieure). Reprises : m4 et m11.
6. **Cloisonnement** : rien de la consigne ; aucun mécanisme vers les moniteurs dans la pièce telle quelle. Risques : l'option (b) de N-2 (M2) et l'en-tête sans mention (m16).
7. **Précision pour un code mécanique** : suffisante après M3, m1, m2, m4 à m7 et m15.
8. **Nœuds** : N-3 est bien posé. N-1 et N-2 sont à reprendre (M1, M2). Il ne manque pas de nœud au sens strict. Je recommande de rendre visible le choix sur les épisodes sans ancre commune (m17), et de régler le moment de décision de tous les nœuds qui touchent une sortie scellée : avant la lecture (1).

## Registre « qui a lu quoi » (contre-lecteur)

Dépôt `/home/user/controle-ia-travail`, sur la branche de la session (HEAD `534120c6…`) et sur `origin/main` :

| fichier | empreinte | lu |
|---|---|---|
| `CLAUDE.md` | (en contexte) | en entier |
| pièce relue (`…-brouillon1.md`) | `4eac34a1…` | en entier |
| `registres/go.md` de `origin/main` | `f50c2e4c…` | ligne `GO-2026-11-24-37` |
| `registres/sondes-iib-v1.md` de `origin/main` | — | lignes `SCELLEMENT-*` seules |
| `docs/notes/barreau8-cote-expose-pieces-lecture-v1/ecarts-entrees-lecture-v1-course-v5-v1.md` | `5fe56e27…` | en entier |
| `…/constat-lectures-dommage-diffusion-course-v5-v1.md` | `5f13f1ab…` | en entier |
| `…/contre-lecture-cote-expose-v1.md` | `41f467de…` | verdicts et partie B |
| `prereg/lecture-sondes-barreau8-v1.md` | `8e432cdc…` | I-9, D-12, plan (points 1 et 3), décisions de coordination |
| `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md` | `fc5b0610…` | « La course lue », D-15, RP-10, « Lectures du dommage et de la diffusion… », NL-4 |
| `prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md` | `8e930aba…` | lignes 200 à 272 (M-1 à M-5) |
| `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v7.md` | `b16779bc…` | « Livraison », questions 1 à 4, 9, 11 et 12 |
| `scripts/extrait_iib_etats_lectures_cote_moniteurs_v3.py` de `origin/claude/iib-executante-v1` | `7eb8006d…` | en entier |
| `requirements-cpu.txt` | `04491d02…` | versions |

Pièce préparée : `/tmp/claude-0/-home-user-controle-ia-travail/009b3d3c-f1bd-510b-b07f-b1a242cff477/scratchpad/pour-fable/structure-sorties-course-v5-sans-valeur.txt` (`eebdee35…`), en entier (structure seule).

Arbre de la course, commit `3326499e` (`…/scratchpad/course-v8/`) :
- **En entier** :
  - `src/controle_ia/iib/lecture_v1.py` (`b8e904c0…`) ;
  - `bases_textuelles_v1.py` (`e94064e3…`) ;
  - `scripts/lecture_iib_1_dommage_v1.py` (`24b3976b…`) et `lecture_iib_2_diffusion_v1.py` (`7766929b…`) ;
  - `oracle_v5.py` (`d997c593…`) ;
  - `lecture_cout_v5.py` (`b753e8bb…`) ;
  - `regle_v5.py` (`a81e88e5…`) ;
  - `designation_v5.py` (`558c0402…`) ;
  - `manifeste.py` (`1a5c7464…`), lignes 1 à 160.
- **Par passages** :
  - `configuration_v1.py` (`d79f21b0…`), lignes 1 à 110 ;
  - `configuration_v5.py` (`5e70ffec…`), constantes, `exiger_oracle_de_la_regle`, `exiger_config_v5`, `gabarit`, `regle_de` ;
  - `lanceur_v5.py` (`3eb03c3b…`), noms, `_ecrire`, `_manifeste`, `jouer`, `appliquer_oracles`, `_ids`, `_lignes`, `phase_course`, `evaluer`, `executer`, `_executer_course` ;
  - `branches_v5.py` (`ed25ec41…`), clause, `_moyenne_des_actions`, `grandeurs`, forme du résultat ;
  - `rapportes_v5.py` (`4015e193…`), `_log`, `discretion` ;
  - `tours_v5.py` (`1a76bf59…`), `boucle_des_tours` ;
  - `tours_v1.py` (`df6267f4…`), lignes 240 à 256 ;
  - `lanceur_v1.py` (`140dcab7…`), lignes 225 à 232 ;
  - `jumeau_v5.py` (`284f40c7…`), classe `Graines` ;
  - `modele_v1.py`, lignes 116 à 127 ; `modele_v5.py`, lignes 40 à 70 ;
  - `harnais/modeles.py`, `fins_du_modele` et `charger_modele` ; `harnais/formats.py`, signatures ; `harnais/run_harnais_factice.py`, `graine_entiere` ;
  - `episodes_v1.py`, lignes 43 à 46 ; `regenere_v5.py`, `jouer_lot` ;
  - `t06/test_croise.py` (`0a627df9…`), `partition_plis` et `plancher_permutation` ;
  - `scripts/mots_et_cout_t06_v3.py` (`9dbcc55c…`), constantes (par recherche).
- **Conception d'origine** : `brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1-brouillon2.md` (`47b86258…`), sections 6.1 et 6.2.
- **Texte scellé de l'organisme v5** (`c1dc5459…`) : sections 2, 3, 6, 10.1 à 10.3, 10.5, 10.6, 11, 14, 15, 16 ; errata 1 (`2031baba…`) et 2 (`ab020d43…`), en entier.
- **Empreintes recalculées** : `t06/cout.py` (`bcfe5683…`), `temoin_jumeau_v5.py` (`38a0de72…`).
- **Noms de fichiers seulement** : `tests/iib_v5_outils.py`, `tests/iib_distillation_v5_outils.py`, `tests/test_iib_distillation_bout_en_bout_v5.py`.

Non ouverts : les consignes privées, `docs/verdicts/`, toute valeur sous `diag/`, `donnees/` et `runs/`.
