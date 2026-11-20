# Rapport du rédacteur — corrections K1 et K2 de la conception « nouvelles attaques » (pièces v3) — v1

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevés de `date -u` : 02:12:35Z avant l'écriture des fichiers de remplacements, 02:14:02Z après les différentiels et avant ce rapport.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/conception-v2/mandat-redacteur-corrections-k1-k2-nouvelles-attaques-v3-v1.md` (`7eb7a3c6386a54cd6914008f55efebe00c4472c2b71c2d63e0374453a89b87b1`, vérifié contre son compagnon : « OK »).
- Ce qui fait foi : le contrôle `controle-differentiel-conception-nouvelles-attaques-v1-v2-v1.md` (`3ab2b0eb620ce98f73fd7f3b92f0738ecae57ebd1b6f1209eb2e5de42aed1a3d`, recalculée), § 4.
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre. **Aucun refus d'outil ni de classifieur.**
- Statut : pièces de travail, non contre-lues, non scellées.

## 1. Verdict

K1 (quatre remplacements) et K2 (six remplacements) sont appliquées à la lettre, par l'outil `scripts/remplacer_texte_exact_v1.py` (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, recalculée ; Python 3.13.18, `python3 -B`). Les trois appels rendent « FAIT », sans avertissement. Le devis v2, son programme et sa sortie ne sont pas touchés. Aucune pièce ne reçoit de méthode, de procédé ni de détail opérant.

**Dix-neuf remplacements en tout** : dix de fond (K1 : 4 ; K2 : 6) et neuf de tenue.

| pièce | K1 | K2 | tenue | total |
|---|---|---|---|---|
| question | 0 | 1 | 4 | 5 |
| ordre de course | 2 | 3 | 3 | 8 |
| rapport de conception | 2 | 2 | 2 | 6 |

## 2. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-nouvelles-attaques-v3/`. Chaque fichier a son compagnon `.sha256`.

| fichier | empreinte |
|---|---|
| `question-course-nouvelles-attaques-v3.md` | `2cf2aae035beef43e999e3cd8b0fb7ba3808649b3cc8b29661c1244b0540415b` |
| `ordre-course-nouvelles-attaques-v3.md` | `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22` |
| `rapport-redacteur-conception-nouvelles-attaques-v3.md` | `6c28636ce07f73b018e7746cb78a03672a224995ad0aff0d7602a6498174ee98` |
| `remplacements-question-course-nouvelles-attaques-v2-vers-v3.json` | `fed187ef2ae7a618cc1c3617730093a82aadb45ffcfc79d151c348e7fae411f8` |
| `remplacements-ordre-course-nouvelles-attaques-v2-vers-v3.json` | `f67c1bda01abfccaf85889007fab9f17e9f3ffd9e6b28459db32c1852e9a9bbb` |
| `remplacements-rapport-redacteur-conception-nouvelles-attaques-v2-vers-v3.json` | `e993fff160723e369eb54f78d479212416237ace2eb29780684413fb1cf0e995` |
| `question-course-nouvelles-attaques-v3.md.journal-remplacements-v1.json` | `7e6746f8b3b338e6d0ceb61a2055d511454072a670a4781cc05792b7ae549b81` |
| `ordre-course-nouvelles-attaques-v3.md.journal-remplacements-v1.json` | `309ddcfe9ca6cf13e708192db7cd4239bda48f5ea6efedaefc00d0410c73d210` |
| `rapport-redacteur-conception-nouvelles-attaques-v3.md.journal-remplacements-v1.json` | `3dcabf82ee54cb24f9602eb976b3951a84fbbff74425fe18f36e07466ae952f8` |
| `differentiel-question-course-nouvelles-attaques-v2-v3.diff` | `0fa31d2a4341b45b9c16c95730ce01b4a612f938cefd92db66d5429d084b712f` |
| `differentiel-ordre-course-nouvelles-attaques-v2-v3.diff` | `bb18f64fd6d0c2a6ec98e81b510efe2e684bc89f7f2cf8b15aa1a01d81233c99` |
| `differentiel-rapport-redacteur-conception-nouvelles-attaques-v2-v3.diff` | `24d11c6870ba31fe11e48f24c02d67350d44c5d9643b5855804ae1fdbf04bfe3` |

L'empreinte de ce rapport est dans son compagnon et dans ma réponse.

Cibles lues, empreintes recalculées, égales à celles du contrôle : question v2 `ebce0480…8ff4`, ordre v2 `1a18cd2e…2586`, rapport de conception v2 `831a2bc4…67f4`. Devis v2, lu par empreinte seulement : `714e4fc6a9a292626022adac4a5ddcc4f3e16fd14f81629b6b8a98cf89fcf028`, égale à celle du contrôle.

## 3. Ce qui est appliqué

**K1 et K2.** Les dix textes « ancien » et « nouveau » sont ceux du contrôle, § 4, au caractère près. J'ai relu les trois différentiels ligne à ligne : chacun des dix y figure, à l'endroit dit par le contrôle.

**Tenue (neuf remplacements).**

- Titres : « v2 » devient « v3 » dans les trois pièces (trois remplacements).
- Ligne de version : dans chaque pièce, la phrase « La v2 elle-même n'est pas contre-lue. » est remplacée par une seconde ligne « Version », qui dit que la v3 remplace la v2 (empreinte de la v2) après le contrôle de son différentiel (nom et empreinte du contrôle), que seules K1 et K2 sont appliquées, avec leur compte dans la pièce, que le devis reste en v2, que la v2 reste archivée, et que la v3 n'est pas contre-lue (trois remplacements). La ligne « Version » de la v2 reste, comme historique. Dans le rapport de conception, cette ligne renvoie aussi au présent rapport pour les empreintes des pièces v3.
- Renvois aux pièces sœurs : la question nomme l'ordre de course v3, et dit du devis qu'il reste en v2, avec son empreinte (deux remplacements) ; l'ordre de course nomme la question v3 (un remplacement).

Rien d'autre ne change.

## 4. Écarts et choix à connaître

1. **Une commande de lecture a échoué.** Un `grep -c -P` sur les quatre pièces, pour compter les espaces insécables, a été refusé par `grep` lui-même (code de caractère trop grand) ; rien n'a été lu ni écrit. Je l'ai relancé sans `-P`, sur les trois pièces v2 nommées par leur chemin complet : aucune espace insécable, aucune apostrophe typographique. Ce n'est pas un refus d'outil ni de classifieur.
2. **La phrase « La v2 elle-même n'est pas contre-lue. » disparaît** des trois pièces, remplacée par la ligne de version v3. C'est mon choix de tenue : la garder aurait laissé, dans une pièce v3, une phrase que le contrôle du différentiel rend inexacte.
3. **L'empreinte du devis v2 s'ajoute au renvoi de la question.** C'est un ajout de tenue au-delà du strict changement de nom ; il tient la phrase du mandat « le devis reste en v2 ».
4. **Les trois `diff -u` rendent le code 1**, ce qui est le code attendu quand les fichiers diffèrent.
5. Les en-têtes des différentiels portent des chemins et des horodatages ; un rejeu les comparera par leur corps.

## 5. Ce que K1 et K2 laissent tel quel, pour la mère

Je ne l'ai pas corrigé : le mandat interdit toute autre modification.

1. **Ordre de course v3, § 0, point 3** : « où la seule issue est l'aiguillage du portier (§ 5) » reste au singulier, alors que le § 5 dit désormais « ses seules issues ». La phrase reste juste, puisque l'aiguillage reste la seule source d'issue, mais elle ne nomme pas les trois classes.
2. **Ordre de course v3, § 3 et § 6** : la ligne de chaque génération et les mesures de l'héritage comptent les fiches au coffre, non les fiches hors case. Le contrôle dit que la garde du coffre (§ 11) ne change pas ; il ne dit rien du compte hors case sur la ligne de la génération.
3. **Rapport de conception v3, D2, option (b)** : elle n'est pas retouchée par K2, alors que l'option (b) de l'ordre de course sert désormais le compte des tentatives hors case. Le texte soumis à Lazar pour D2 ne le dit donc que dans l'ordre de course.
4. **Rapport de conception v3, § 2, § 3 et § 7** : ils décrivent toujours la session de la v1, comme en v2.

## 6. Refus

Aucun refus d'outil ni de classifieur.

— rédacteur neuf, modèle F
