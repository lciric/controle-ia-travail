# Vérification des corrections du brouillon 2 de la spécification des lectures du dommage et de la diffusion sur la course v5

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce de travail du côté exposé ; elle ne doit jamais être transmise au côté des moniteurs. Elle ne porte aucun chiffre de la course, aucun fragment de consigne privée, et aucun trait de l'organisme qui ne soit déjà écrit dans la pièce vérifiée.

- **Pièce vérifiée** : `docs/notes/barreau8-cote-expose-pieces-lecture-v1/specification-lectures-dommage-diffusion-course-v5-v1-brouillon2.md`, empreinte `5968aa37bfb1931c8a828a5fa2ba6a4d9dc9dec2dfcdd008f16f82b7b8f30c3b`, recalculée et égale. Fichier des différences : `differences-specification-brouillon1-vers-2-v1.md`, empreinte `b2d08e35707e5d9bb9eddf15eb54d497cefced43af19154def1840d2e8e674a2`, recalculée et égale.
- **Vérificateur** : Claude Opus 5.5, auteur de la contre-lecture 1. La copie déposée dans le dépôt a l'empreinte `b20c67b0…`, égale à celle du bloc-notes.
- **Ce que je n'ai pas fait** : je n'ai ouvert aucune consigne privée, rien sous `docs/verdicts/`, aucune valeur des sorties de la course. Je n'ai modifié aucun fichier du dépôt.

## Verdict

**Scellable après trois corrections mineures.** Il ne reste ni bloquant ni majeur, et les 21 remarques de la contre-lecture 1 sont traitées. Les trois mineurs restants ne demandent pas de nouvelle vérification de fond : la session mère peut contrôler leurs corrections au simple constat. Elle peut aussi sceller le brouillon 2 tel quel et porter ces trois points par un erratum de classe A, contre-lu.

Les trois nœuds peuvent tous être tranchés avant toute lecture. Aucune de leurs options ne dépend d'un résultat. Aucune ne fait passer au côté des moniteurs un trait de l'organisme ; l'option (b) du nœud sur la base « premier coût contre les suivants » appelle une remarque, plus bas.

Les corrections n'ont rien introduit de faux :
- **Faits de code et empreintes** : vérifiés un par un (liste plus bas).
- **Vocabulaire, portée, bases, paires et forme de l'extrait** : inchangés. Aucune clé n'est ajoutée dans `jeux` ni dans `etat_par_unite.unites`.
- **Règles gelées** :
  - R1 et R3 : aucun choix n'est laissé pour après une lecture ;
  - R5 : chaque garde neuve a son cas sain et ses artefacts ;
  - R9 : la graine de l'audit est redérivée et comparée à celle que la sortie consigne ;
  - R11 : les empreintes sont tenues ;
  - R12 : le brouillon 1 est intact (`4eac34a1…`) et les noms des sorties sont inchangés.
- **Liste des différences** : un `diff` des deux brouillons ne montre aucun changement hors de cette liste.

## Remarques de la contre-lecture 1, une par une

| remarque | état | constat |
|---|---|---|
| M1 — part *p* de la phrase nulle | **levée** | Les phrases sur le sens de l'écart entre options sont retirées ; le texte dit maintenant ce sens inconnu d'avance (l. 483). Les trois parts sont calculées (l. 366-372). L'honnête de l'option (c) est nommé : `grandeurs.exces_moyen_honnete` existe dans `branches_v5.grandeurs`, et l'honnête de l'évaluation est écarté avec une raison juste, car il joue d'autres tâches que le maître. La part citée est fixée avant toute lecture (l. 374), et la règle commune ferme toute reprise après une sortie (l. 478). |
| M2 — base « premier coût contre les suivants » | **levée**, autrement que proposé | L'option sur résultat est retirée, et l'option « un mot de plus dans l'extrait » aussi. La section 7.6 fixe le sort de la base sous l'option (a), avec un envoi à Lazar sans condition, que la base détecte ou non. Score et critère sont arrêtés au scellement (l. 275 et 502). La voie choisie est plus prudente que la mienne, et je l'accepte. |
| M3 — lecteur du coût de cette base | **levée** | `cout_declare` de la ligne (l. 274), avec sa raison (garde de concordance) et un essai où les deux lecteurs du coût diffèrent (l. 447). |
| M4 — script d'audit sans essai | **levée** | Quatre gardes. L'échantillon est lu dans la sortie scellée, puis retiré à nouveau par le calcul exact du module d'origine (`sorted` des clés de `B100` et `TJ100`, `choice(n, k, replace=False)` trié, graine redérivée et exigée égale). Rien n'est écrit, et une ligne d'essais est ajoutée (l. 221-229, 448). Le calcul décrit est fidèle à `lecture_v1.lecture_1`. |
| m1 — types de l'entropie | levée | Contrôle E7, l. 90. |
| m2 — clé `manifeste` du résumé | levée | Contrôle E3, l. 86 ; `lanceur_v5.py`, ligne 565, vérifiée. |
| m3 — fonctions d'origine pour E4 et E7 | levée | `designation_v5.configuration_de_course` et `prefixe_de_la_course`, plus l'égalité de `configuration_sha256`. L'appel est sans effet de bord ; il vérifie le sceau de la désignation et refuse toute issue autre que `N` ou `P`. |
| m4 — taille du vocabulaire | levée | `vocab_size` de `config.json`, à l'empreinte `29e4c210…` (note v7, question 1), et `len(tok)` exigé égal. Le piège de `tok.vocab_size` est nommé et a son essai rouge. |
| m5 — clés exactes des fichiers d'identifiants | levée | Section 7.2. |
| m6 — enveloppe des fiches | levée | Sections 5.3 et 7.3. |
| m7 — ordre des pas | levée | Sections 3.1 et 3.2, avec un essai sur des lignes données dans le désordre. |
| m8 — lecture stricte du JSON | levée | L. 76 : la relecture stricte couvre aussi `configuration_de_course`. |
| m9 — modules à empreinte contrôlée | levée | Cinq modules ajoutés, empreintes recalculées et égales : `designation_v5` `558c0402…`, `run_harnais_factice` `43a24431…`, `formats` `98dbfa9b…`, `scellement` `93beeb1c…`, `gardes` `a83c48ce…`. |
| m10 — citations de code | levée | `regenere_v5.py`, ligne 84 (dans `jouer_lot`) ; `modele_v5.py`, lignes 59 et 60, vérifiées. |
| m11 — dossier du jetoniseur | **levée**, plus strictement que proposé | Liste fermée de quatre fichiers, tous à empreinte de référence ; `special_tokens_map.json` est exclu. C'est acceptable : la fin du jetoniseur et le gabarit sont dans `tokenizer_config.json`, l'ensemble des fins est contrôlé, la garde de fidélité tient le décodage, et un chargement qui ne tiendrait pas ces gardes s'arrête et ouvre un nœud (l. 532). |
| m12 — ordre du temps | levée, avec un reste (r2) | Contrôle T0. Les trois empreintes attendues sont celles des lignes 5 à 7 du registre propre sur `origin/main` (`645eeeb9…`), et leurs heures sont croissantes. |
| m13 — issue de la ligne d'audit | levée, avec un reste (r3) | Sections 6.3 et 7.4. Le motif `ISSUE=(SANS-DEFAUT\|DEFAUT-AUTORISE\|DEFAUT)`, non suivi d'une lettre ni d'un tiret, lit juste les trois issues. |
| m14 — essais manquants | levée | Section 14. |
| m15 — « clé seule écrite » | **levée en partie** (r1) | Corrigée aux sections 7.2 et 7.3, restée dans deux lignes de la section 14. |
| m16 — cloisonnement | levée | En-tête, et clé `cloisonnement` des trois sorties. |
| m17 — choix hors de la table des sept points ; repère 0,58 | levée | Section 15, lignes 8 à 10 ; section 16, « Tranché par la spécification » ; clé `note_reperes`. |

## Les trois nœuds

- **Règle commune** : les nœuds sont tranchés avant le scellement. Le texte est écrit sous l'option recommandée, avec le texte de rechange pour chaque autre option. Aucune option ne dépend d'un résultat, et tout changement après une sortie est un écart qui ne la réécrit pas.
- **Nœud sur la part *p*** : ses trois options sont tranchables avant toute lecture, et leurs trois textes de rechange ne touchent que la part citée.
- **Nœud sur la base « premier coût contre les suivants »** :
  - les options (a) et (c) sont tranchables et dans l'accord, à l'écart près que l'option (c) déclare ;
  - l'option (b) se tranche aussi avant lecture, mais elle exige un accord neuf et un additif au texte des sondes, et le texte le dit ;
  - au côté des moniteurs, elle ne ferait savoir qu'une chose : qu'une base non décrite du côté exposé peut rendre « réussit ». Ce n'est pas un trait de l'organisme. Ce point est à garder en vue si Lazar retenait cette option.
- **Nœud sur les deux phrases sans phrase écrite d'avance** : tranchable. Les phrases de rechange de l'option (b) sont exactes : « moins de 32 tâches » est bien la condition de « non calculable » dans `lecture_v1`.
- **Ce que le texte ne dit pas** : quel nœud la session mère peut trancher seule. Les options (b) des deux derniers nœuds disent elles-mêmes qu'il faut le mot de Lazar, et l'en-tête (l. 5) attend « le mot sur les trois nœuds ». C'est cohérent ; aucune correction n'est demandée.

## Défauts restants

Aucun bloquant. Aucun majeur.

**Mineurs.**

**r1. Reste de m15 (section 14, lignes 444 et 445).** Les lignes « décodage » et « fidélité » disent encore « clé seule écrite » et « clé et nom du champ seuls écrits ». Il faut les aligner sur les sections 7.2 et 7.3 : « imprimée sur la sortie d'erreur ; rien sur disque », et l'essai vérifie qu'aucun fichier n'est créé.

**r2. Racine des textes cités par le contrôle T0 (lignes 82 et 402).**
- « Le texte cité, pris sous la racine de l'arbre qui porte le registre » doit dire comment cette racine se calcule. Je propose : la racine est le répertoire parent du dossier `registres/` qui contient le fichier passé par `--registre-sondes`, et le registre doit être exactement `<racine>/registres/sondes-iib-v1.md`, sinon arrêt.
- La liste fermée doit dire que `ouvrir` accepte, pour ces fichiers seulement, cette seconde racine (de même pour le registre des décisions et le dossier du jetoniseur, déjà hors de la racine de lecture). Sinon, un code mécanique les refusera, ou les ouvrira hors de toute garde.

**r3. La dernière ligne de l'audit décide, même après un défaut (ligne 260 ; essai, ligne 440).** Telle qu'écrite, une ligne `ISSUE=SANS-DEFAUT` inscrite après une ligne `ISSUE=DEFAUT` débloque la lecture de la diffusion sans aucun accord. Or le texte veut qu'après un défaut, la lecture ne parte que par une décision nommée (l. 229).
- Je propose : si une ligne `ISSUE=DEFAUT` existe pour cette empreinte, la lecture ne part que si une ligne `ISSUE=DEFAUT-AUTORISE` portant un identifiant d'accord vient après elle. Une `SANS-DEFAUT` plus tardive ne suffit pas.
- L'essai change en conséquence : `DEFAUT` puis `SANS-DEFAUT`, refus.
- Contrôle facultatif : que l'identifiant d'accord existe dans `registres/go.md`.

## Faits revérifiés pour ce brouillon

- **Empreintes recalculées** dans l'arbre `3326499e`, toutes égales à celles qu'écrit le brouillon : `scellement.py` `93beeb1c…`, `gardes.py` `a83c48ce…`, `regenere_v5.py` `1b4c22ba…`, `modele_v5.py` `cca1e444…`, `harnais/run_harnais_factice.py` `43a24431…`, `harnais/formats.py` `98dbfa9b…`. Sur `origin/main` : `registres/sondes-iib-v1.md` `645eeeb9…`.
- **Lignes de code citées** : `lanceur_v5.py`, ligne 565 (`sorties["manifeste"] = _manifeste(…)`) ; `modele_v5.py`, lignes 59 et 60 (`FormatChat(tok, variables=m["variables_gabarit"])` et `fmt.fins = …`) ; `regenere_v5.py`, ligne 84 (`decode(dans, skip_special_tokens=True)`, dans `jouer_lot`).
- **Fonctions appelées** : `designation_v5.configuration_de_course` et `prefixe_de_la_course` ont la signature et l'effet que décrit le brouillon. `branches_v5.grandeurs` rend bien `exces_moyen_honnete`.
- **Additif 2 (M-1, clauses (b) et (c))** : la passe tient les fichiers du jetoniseur et `config.json` par la garde P2, et `vocab_size` vient de `config.json`. Le brouillon s'aligne sur cette lettre.

## Qui a lu quoi (vérification)

- **Lus en entier** : le brouillon 2 (`5968aa37…`) et le fichier des différences (`b2d08e35…`).
- **Comparaison** : `diff` du brouillon 1 (`4eac34a1…`, intact) et du brouillon 2.
- **Arbre `3326499e`** : `modele_v5.py`, lignes 59 et 60 ; `lanceur_v5.py`, ligne 565 ; empreintes des six fichiers ci-dessus.
- **Sur `origin/main`** :
  - `registres/sondes-iib-v1.md`, lignes `SCELLEMENT-*` seules ;
  - `prereg/lecture-sondes-barreau8-v1.md`, lignes trouvées par la recherche de « P2 ».
- **Pour le reste** : les lectures consignées dans la contre-lecture 1.
- **Jamais ouverts** : consignes privées, `docs/verdicts/`, valeurs des sorties de la course.
