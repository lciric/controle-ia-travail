# Notice d'emploi — passe de recalcul de l'activité interne du barreau 8 (saboteur à budget), côté moniteurs — v7

> **Version 7 de cette notice**, écrite le 2026-11-24 par le développeur du côté des moniteurs (Opus 5.5, session fille de la mère `session_01Qi7Gr3Ggccg85kjmP654WC`, jamais exposée au saboteur), pour le **code de version 6** : `src/controle_ia/barreau8_moniteurs/passe_recalcul_v6.py`, essais `tests/test_barreau8_moniteurs_passe_v6.py` (modèle jouet seulement). Elle remplace, pour ce code, la notice version 6 (`docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v6.md`, `ad1c04191298fbd56e136a6fdb16e48074eb170ce987966ae18347bdb0bdc019`, écrite pour le code de version 5 ; elle reste intacte, R12). **Tout ce que la notice version 6 dit reste vrai pour le code de version 6, sauf ce que la section « Ce qui change » ci-dessous remplace** : livraison (six sortes de fichiers, noms, formats, découpage), règle « nul n'ouvre les fichiers de scores », arbre propre, fichiers de sondes à tirer de la branche `origin/donnees/t07-etape-a-v1`, codes de refus, mémoire et disque, essai à blanc pas à pas, garde des chemins.
>
> Textes qui font foi : le texte scellé `prereg/lecture-sondes-barreau8-v1.md` (`8e432cdc…`), lu avec l'additif 1 `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md` (`fc5b0610…`) et l'additif 2 `prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md` (`8e930aba…`). Le code n'en est qu'une exécution ; en cas d'écart, le texte prime (nœud de Lazar).

## Module, et ligne de commande exacte

**Module : `controle_ia.barreau8_moniteurs.passe_recalcul_v6`.** Depuis la racine du dépôt, `PYTHONPATH=src`, interpréteur de `.venv` (bibliothèques de `requirements-cpu.txt` : `transformers` 5.18.0 et `tokenizers` 0.23.2 sont **exigées** par la garde P3, égales à celles de l'extrait ; sur la machine de la carte, installer exactement ces versions).

**(a) Empreintes des modules chargés** :

```
PYTHONPATH=src .venv/bin/python -m controle_ia.barreau8_moniteurs.passe_recalcul_v6 empreintes-modules
```

**(b) Bordereau du code** (dix clés ; à écrire après le rapport scellé de la nouvelle conformité ; son chemin et son empreinte vont à la ligne `CODE-PASSE-IIB`, strictement postérieure à la ligne `SCELLEMENT-ADDITIF-2-SONDES-IIB`) :

```
PYTHONPATH=src .venv/bin/python -m controle_ia.barreau8_moniteurs.passe_recalcul_v6 bordereau-code \
  --racine . \
  --texte-scelle prereg/lecture-sondes-barreau8-v1.md \
  --additif prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md \
  --additif-2 prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md \
  --constantes docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-2-v1.json \
  --rapport-conformite <rapport scellé de la nouvelle conformité de la passe> \
  --notice docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v7.md \
  --devis docs/notes/rejeu-activations-saboteur-voie-a-v1/devis-passe-activations-saboteur-voie-a-v2.md \
  --accord <identifiant de la ligne d'accord de la passe, par exemple GO-2026-11-24-13> \
  --bordereau registres/bordereau-code-passe-barreau8-v6.json
```

L'accord : la ligne `GO-2026-11-24-13` du registre des accords (« go calcul rejeu ») cite l'empreinte entière du devis `9a4a794c…` ; la garde P0 exige qu'une ligne, et une seule, ait pour première cellule l'identifiant de l'accord et porte cette empreinte. La session mère choisit l'identifiant ; le code ne le devine pas.

**(c) Vérification des entrées** (`verifier-entrees`, sans poids ni carte, sans aucune écriture), **(d) essai à blanc** (`essai-a-blanc`), **(e) passe** (`passe`) : mêmes paramètres, seule l'action change ; un `--run-id` et un `--sortie` neufs à chaque commande ; `--debut-location` est une heure passée, à la seconde.

```
PYTHONPATH=src .venv/bin/python -m controle_ia.barreau8_moniteurs.passe_recalcul_v6 passe \
  --racine . --sortie <dossier neuf, hors du dépôt, sans « iib » ni « ii-b » dans son chemin> \
  --run-id AAAAMMJJ-HHMMSS-passe-barreau8 \
  --entropie 149333987590752343984325077404464904184 \
  --extrait docs/notes/rejeu-activations-saboteur-voie-a-v1/prealables-cote-expose-v7-brouillon/extrait-cote-expose-d13-v1.json \
  --taches donnees/20261007-082440-t05-extraction/taches-evaluation.json \
  --sondes-legeres donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz \
  --sondes-neuves donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz \
  --planchers donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz \
  --registre registres/sondes-iib-v1.md --registre-accords registres/go.md \
  --duree-max-heures <borne de la ligne d'accord> --depense-max-usd <borne de la ligne d'accord> \
  --prix-horaire-usd <prix de la location> --debut-location AAAA-MM-JJTHH:MM:SSZ \
  --identifiant-instance <identifiant de l'instance> --appareil cuda [--cache-modele <cache local hors du dépôt>]
```

L'entropie est celle du champ F-3 du texte scellé (inchangée par les additifs). L'extrait est accepté **quel que soit son chemin**, à la seule empreinte `1ff87c08f5170fa7319349aa8cc1fc17a72689bcadd52295aff7856a0fbf992f` (M-2) ; s'il est déplacé, donner son chemin neuf. **Les trois fichiers de la course ne sont pas des paramètres** : la passe les prend, sous `--racine`, aux chemins que l'extrait nomme : `diag/20261122-202132-iib-reel/ids-actions-evaluation-iib-v5.json` (`7eceb156…`), `…/adaptateur-eleve-iib-v5.pt` (`9c7808fb…`), `…/adaptateur-temoin-jumeau-iib-v5.pt` (`67ea25de…`), chacun avec son compagnon `.sha256`. Le fichier `config.json` de la révision doit être dans le cache du modèle (il est lu avant les poids, garde P3).

## Ce qui change du code de version 5 au code de version 6

| règle | ce que fait le code de version 6 | fonction |
|---|---|---|
| M-1, forme | lit l'objet JSON des identifiants, JSON strict (clés répétées et constantes non finies refusées), deux clés exactement, `avertissement` égal à « EXPLORATOIRE, NON OPPOSABLE (R-522) » ; aucun fichier des textes, aucun champ de coût | `lire_identifiants` |
| M-1, clause (a) | K × T × E clés d'épisode, rangées dans l'ordre du tri des chaînes de Python ; phase = partie avant la première barre oblique, égale au préfixe de la table suivi d'une condition de la table ; épisode non vide ; valeur = A listes ; clé d'action `<phase>/<épisode>/pas<t>` ; N clés distinctes | `garde_p3_structure` |
| M-1, ordre | ordre des clés d'épisode, puis des pas 0 à A − 1 ; c'est le champ `rang` de l'index et l'ordre des lots | `garde_p3_structure` |
| M-1, clause (b) | dans cet ordre, avant le chargement des poids : (1) versions de `transformers` et `tokenizers` chargées égales, comme chaînes, à celles de l'objet `versions` de l'extrait (clé absente ou version différente : « non tenue » avant toute action) ; (2) `tokenizer_config.json` à son empreinte, champ `clean_up_tokenization_spaces` booléen, lu ; (3) pour chaque action, `decode(ids, skip_special_tokens=True, clean_up_tokenization_spaces=<lu>)` égal à `decode(ids, skip_special_tokens=True)` ; arrêt à la première action qui diffère, la clé seule écrite ; (4) le texte du journal est ce décodage explicite, jamais écrit sur disque | `garde_p3_versions`, `lire_nettoyage_des_espaces`, `garde_p3_decodage` |
| M-1, clause (c) | 1 à J identifiants ; fin par un jeton de fin ou exactement J ; aucun jeton de fin intérieur ; chaque identifiant entier JSON (ni booléen, ni nombre à virgule, ni chaîne), entre 0 et V − 1, V = `vocab_size` de `config.json` de la révision, à son empreinte ; conversion en `int64` | `garde_p3_structure`, `garde_p3_vocabulaire` |
| M-1, clause (d) | condition = phase sans le préfixe ; épisode = tâche (E = 1), l'une des T tâches ; chaque couple (condition, tâche) une fois, avec un pas de chaque rang | `garde_p3_structure` |
| M-2 | extrait exigé à l'empreinte `1ff87c08…` (constante de la spécification) ; `fichiers_de_la_passe` à exactement trois clés : le fichier des identifiants et un fichier par adaptateur distinct, sous `diag/20261122-202132-iib-reel/`, aux noms de la table ; tout chemin `donnees/<run_id>/…` ou toute quatrième clé refusé | `garde_p1`, `lire_extrait_du_cote_expose`, `fichiers_de_la_course` |
| M-4 | la table neuve est lue par la garde P0 au chemin et à l'empreinte du bordereau ; elle doit dire « report », porter ses constantes, avoir exactement les quatre champs « couvert par l'additif 2 » et aucun champ « nœud » ; E = 1 et fichier des textes vide ; **toutes les constantes de forme de la passe sont remplacées par celles de la table**, et la spécification écrite dans le code doit leur être égale (sinon arrêt : ligne 24 de l'additif 1) | `exiger_table_neuve`, `specification_depuis_table` |
| M-5 et additif 1 | registre à huit clés ; une ligne par clé de scellement ; texte, additif 1 et additif 2 scellés et intacts (D-16, D-17), l'additif 1 postérieur au texte, l'additif 2 à l'additif 1 ; **exactement une** ligne `CODE-PASSE-IIB` strictement postérieure à la ligne de l'additif 2 (rang et heure) ; les lignes antérieures ne comptent pas ; bordereau à dix clés (`additif`, `additif_2`, `constantes` en plus) égal aux lignes ; rapport de conformité de la version 5 (`fa9158fb…`) refusé | `lire_registre_propre`, `lignes_comptees`, `garde_p0`, `lire_bordereau_du_code` |
| RP-7 | les sous-échantillons ne dépassent pas n15 et n7 de la table | `sous_echantillons` |
| RP-12 | motifs de chemins privés ajoutés par la table (aucun pour la course lue) ; invite de la table | `SurveillanceLectures`, `fichiers_de_l_invite` |

**Inchangé** : la livraison (six sortes de fichiers, noms, clés, formes, types, découpage, trace à vingt clés — elle écrit les versions de jetonisation effectivement comparées), les gardes P2, P4 à P7, P9, P10 et leurs seuils, la recette du contexte, la règle des sondes lues, l'ordre des conditions pour les lots (celui de la table : H, B50, B100, TJ100).

## Ce que la passe fait, dans l'ordre

1. Durée et dépense (P9) ; contrôle des dossiers de sortie et de la place libre (P8, P9).
2. Garde P0 (registre, trois textes scellés, ligne de code, bordereau à dix clés, table neuve, modules, rapport, notice, devis, accord) ; puis la spécification prend les constantes de la table, après contrôle d'égalité.
3. Garde P1 : extrait à son empreinte et à sa forme ; trois fichiers de la course ; tâches au chemin et à l'empreinte de la table ; sondes et planchers. Dossier du modèle (P8).
4. Garde P3 : versions de jetonisation ; lecture du fichier des identifiants ; clauses (a), (c), (d).
5. Règle des sondes lues ; manifeste.
6. Jetoniseur seul : borne du vocabulaire (`config.json`), réglage lu, égalité des deux décodages sur les N actions. **Les poids ne sont chargés qu'ensuite.**
7. à 12. Comme la notice version 6 (poids, P2, contextes, adaptateurs, P10, première passe, seconde passe, P7, livraison, contrôles de fin).

## Essai à blanc et vérification des entrées

Comme la notice version 6. Attendu de `verifier-entrees` sur la course lue : « entrees : conformes », 2 560 actions, P3 « tenue » avec 7 680 actions contrôlées (trois contrôles par action : structure, vocabulaire, décodage). Une divergence des deux décodages arrête dès cette étape, sans carte : la porter à la session mère (ligne 30 (c) de l'additif 2 : nœud de Lazar, aucune relance ni autre décodage avant son mot). Une version de jetonisation différente arrête aussi : remettre la machine à `transformers` 5.18.0 et `tokenizers` 0.23.2 et relancer sans autre changement (ligne 30 (b)).

## Essais (règle R5)

`tests/test_barreau8_moniteurs_passe_v6.py`, 145 essais, modèle jouet seulement, dont un en sous-processus qui lance réellement le module par `python -m`. Ceux de la version 5, portés au format JSON, plus ceux que l'additif 2 exige (M-5) : clé JSON répétée ; `avertissement` altéré ; troisième clé ; clés d'épisode non triées ; condition hors de la table ; épisode qui n'est pas une tâche ; tâche absente d'une condition ; A − 1 ou A + 1 pas ; booléen, nombre à virgule, chaîne, entier négatif, entier égal à V ; action vide ; J + 1 identifiants ; action courte sans fin ; fin intérieure ; version de `transformers` ou `tokenizers` différente ou absente de l'extrait (« non tenue » avant toute action et avant les poids) ; configuration sans le champ ; champ inversé sur une action où le nettoyage change un espace (arrêt à cette action, clé seule) ; quatrième clé et chemin sous `donnees/` dans `fichiers_de_la_passe` ; extrait d'une autre empreinte ; fichier sans compagnon ou d'une autre empreinte ; ligne `SCELLEMENT-ADDITIF-2-SONDES-IIB` absente ; ligne de code antérieure ; clé `additif_2` absente du bordereau ; table absente, d'une autre empreinte, disant « nœud », ou portant un champ couvert hors des quatre ; constante de forme différente de la table. L'artefact « un texte altéré d'un caractère » du texte scellé est sans objet (aucun texte versé).

Contrôle fait sur le dépôt, sans carte : l'extrait réel (`1ff87c08…`) est accepté par `lire_extrait_du_cote_expose` (forme conforme, trois rôles, versions `transformers` et `tokenizers` présentes et égales à 5.18.0 et 0.23.2), contrôlé par programme sans affichage de son contenu.

## Jamais exécuté ici

Le chargeur réel et la carte ; le vrai fichier des identifiants (sous `diag/`, que le côté des moniteurs n'ouvre pas) ; le vrai `config.json` et la vraie égalité des deux décodages sur le jetoniseur réel ; tout ce que la notice version 6 liste à la même section.
