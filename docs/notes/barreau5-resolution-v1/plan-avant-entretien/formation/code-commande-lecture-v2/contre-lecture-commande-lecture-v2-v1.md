# Contre-lecture du code de commande de la relecture, version 2 (additif 1 v2 au devis du barreau 5) — v1

- **Nature** : contre-lecture d'une pièce de classe B (code), écrite par Claude Opus 5.5, agent neuf, le 21 novembre 2026. Je n'ai écrit ni l'additif ni ce code. Mandat : `mandat-contre-lecture-commande-lecture-v2-v1.md` (`85e1de4306c65e10799c6f9f9ef32350131e14cc41dcac1f05122ad3b19efd4b`, égal à son compagnon), puis le message de la coordinatrice après le disque plein (mêmes règles).
- **Objet** : commit de commande `76c608b61d52549d4e0dceb9d07be0c5bea273f8`. Son parent `d532ed0ff` porte les épreuves seules, et le parent de celui-ci est le code figé `c76e79169eee337ce66c7d88f62d039e853eebfc`. `git diff --name-status c76e7916 76c608b6` donne trois « A » : le module, le lanceur et les essais.
- **Pièces lues**, empreintes vérifiées contre leur compagnon :
  - le rapport du développeur (`a9b3ce5a…`) ;
  - l'additif 1 v2 (`c3120d3a…`), en entier ;
  - la contre-lecture de l'additif (`bdb46a66…`), jusqu'au § 2.1 ;
  - la vérification (`905f2015…`) et le scellement (`02d1c52f…`) ;
  - le registre propre de main n'a pas de compagnon ; son empreinte, `41f5ec14…`, est égale à celle que donne le mandat. Je ne l'ai pas ouvert : l'essai du registre réel ne m'était pas nécessaire.
  - Le code, par `git show` au commit : les trois fichiers ajoutés ; dans `relecture_v1.py`, les lignes 180 à 260 et 950 à 1250 ; dans `lecture_v1.py`, les lignes 497 à 513 et les constantes `TEXTE` ; dans `engagement_v1.py`, les lignes 35 à 45 et 130 à 175 ; dans `formation_v1.py`, les lignes 1395 à 1423 ; `CHEMINS_GELES` (`validation_reelle.py`, ligne 71) ; les deux lanceurs.
  - Le diff des essais entre `d532ed0ff` et `76c608b6`.
- **Cloisonnement** : rien ouvert hors de la liste. Je n'ai pas lu le texte scellé : il a été extrait dans ma copie, que les essais recopient sans le lire. Rien n'a été ouvert sous `/root/secret-b5f-formation-v1/` ni sous `/root/.claude/`. Une sortie d'outil trop longue (l'additif) y a été rangée par l'outil ; je ne l'ai pas ouverte et j'ai relu l'additif par son chemin. Aucune commande au loueur, aucune clé, aucune poussée, aucun commit.
- **Copie** : un arbre de travail détaché et clairsemé à `76c608b6` (`src`, `scripts`, `tests`, `.claude`, plus deux fichiers de `prereg` recopiés sans être lus).

## Verdict

**Conforme après ces corrections** : liste fermée 1 à 4 ci-dessous, aucune bloquante.

Ce qui tient, prouvé par essai ou par mutation :
- Le corps recomposé est fidèle : `diff` ligne à ligne contre les lignes 1049 à 1099 de `relecture_v1.py` au commit, avec exactement deux blocs changés, et la même signature.
- Les quatre vérifications (a) à (d) mordent.
- Aucune substitution d'attribut.
- La commande est égale à l'octet à celle de la version 1, pour les deux pièces.

**Je ne lève pas de nœud.** Le montage n'est pas plus risqué qu'un code de lecture neuf. Il n'ajoute que trois fichiers. L'instance joue la version 1 par (a), et (b) avec (c) rendent la garde de l'arbre de la session au moins aussi stricte que celle de la version 1, puisque la tête doit égaler un commit cité à 40 signes.

Les quatre corrections ne touchent que le fichier d'essais. Il est dans `LISTE_FERMEE`, donc le commit de commande changera, et sa citation dans `GO-LECTURE-B5F` avec lui.

## Essais joués

- Depuis ma copie, `tests/test_commande_lecture_v2.py` : **111 passés, 1 sauté** (le registre réel, sans sa variable).
- Depuis l'arbre de commande, en lecture seule : `PYTHONDONTWRITEBYTECODE=1`, `-B`, `-p no:cacheprovider`, `--basetemp` hors de l'arbre, vidé aussitôt après. Les quatre fichiers ensemble : **201 passés, 1 sauté**, soit 24 + 43 + 23 + 111. `git status --porcelain` était vide avant et après, et la tête est restée à `76c608b6`.
- Dans ma copie, les essais de `relecture_v1` échouent en partie (15) pour une seule raison : `docs/` est absent de la copie clairsemée (« fichier absent sur disque »). Rejoués depuis l'arbre de commande, ils passent.

## Mutations jouées (dans ma copie, fichier rendu à l'octet après chacune)

Programme : `cl-commande-v2/muter.py`. Relevé : `cl-commande-v2/sortie-mutations-cl.txt`. Un premier relevé, faussé par le disque plein, est gardé à part sous `sortie-mutations-cl-disque-plein-invalide.txt` et n'est pas lu.

| mutation | ce qu'elle casse | rouge ? |
|---|---|---|
| X01 | formule du stockage avec un disque fixé à 300 au lieu du disque de la pièce | **aucun essai rouge (survit)** |
| X02 | (d) : `_CITATION.fullmatch` remplacé par `.search` | **aucun essai rouge (survit)** |
| X03 | (b) sans la clause « la tête est le commit de commande » | 2 rouges (`test_b_arbre_de_session_autre…`, `test_d_citation_d_un_autre_commit`) |
| X04 | (c) sans la borne « hors de la liste fermée » | 1 rouge (`test_c_…[hors_liste]`) |
| X05 | (b) : comparaison de l'index seul (`--cached`) | 1 rouge (`test_b_arbre_de_travail_change`) |
| X06 | (d) : nom de session rendu facultatif | 1 rouge (`test_d_format…`) |
| X07 | lanceur sans la garde du plan « decisif » | 1 rouge (`test_lanceur…refuse_toute_autre_sous_commande[args14]`) |

Elles s'ajoutent aux 21 mutations du développeur, dont je n'ai pas relu le relevé : il est hors de ma liste.

## Constats

**Constat 1 — `commande_lecture_v2.py`, ligne 132, et `tests/test_commande_lecture_v2.py`, `test_d_format_de_la_citation_lu_a_la_lettre`.**
- **Mode d'échec** : épreuve qui ne peut pas échouer (le format « lu à la lettre » n'est pas éprouvé en fin de chaîne).
- **Gravité** : non bloquant. Le code est juste : il refuse.
- **Preuve** : mutation X02 jouée, aucun essai rouge. Par appel direct, le code réel refuse trois artefacts que `.search` accepterait : la citation suivie d'un 65ᵉ signe hexadécimal (`…ffff0`), suivie de `xyz`, et suivie d'un texte libre sans « ; ».
- **Correction** : ajouter ces artefacts à la liste de `test_d_format…`, au moins `sain + "0"` et `sain + " note sans point-virgule"`.

**Constat 2 — `tests/test_commande_lecture_v2.py`, `test_portee_repetition_par_le_corps_recompose_la_borne_de_0_08_n_a_pas_bouge`.**
- **Mode d'échec** : épreuve qui ne peut pas échouer. Les valeurs 0,19, 0,40 et 0,50 donnent la même réponse à 150 Go et à 300 Go, donc le disque de la pièce dans la formule n'est pas éprouvé.
- **Gravité** : non bloquant. La branche de la répétition n'est atteinte par aucune entrée. Mais l'additif, § 3.3 et § 3.4, demande que le corps recomposé soit éprouvé sur cette branche.
- **Preuve** : mutation X01 jouée, aucun essai rouge. Calcul : 0,30 USD par Go et par mois donne 0,0616 à 150 Go (accepté) et 0,1233 à 300 Go (refusé par le mutant). Le code réel l'accepte (appel direct).
- **Correction** : ajouter le cas sain « repetition à 0,30, accepté », par `exiger_offre_lecture_v2` et par le corps recomposé. Toute valeur dans ]0,1947 ; 0,3893] discrimine.

**Constat 3 — `tests/test_commande_lecture_v2.py`, `test_d_ligne_de_l_accord_de_lecture_sans_la_citation`.**
- **Mode d'échec** : artefact qui pourrait échouer pour une autre raison. Le motif `match="GO-LECTURE-B5F"` est aussi dans le refus de la version 1 (« accord de lecture GO-LECTURE-B5F absent ou ≠ accord de la configuration »), atteint avant (d).
- **Gravité** : non bloquant. Aujourd'hui le contenu de la ligne est juste, et une mutation qui neutralise (d) rend l'essai rouge, puisque la commande serait rendue.
- **Preuve** : raisonnement, en lisant `exiger_registre_de_relecture`, au commit `c76e7916` de `relecture_v1.py`, lignes 230 et 231.
- **Correction** : resserrer le motif sur « ne cite pas, une fois et à la lettre » (et de même dans `test_d_format…`).

**Constat 4 — `tests/test_commande_lecture_v2.py`, paramètre `{"disk_space": 149}` de `test_memes_autres_bornes…`.**
- **Mode d'échec** : épreuve affaiblie après le code. La retouche de 299 à 149, l'une des trois « retouches d'essai » du commit, retire la frontière du disque de la relecture décisive (299 contre 300). Le seul autre artefact de disque est 200 (`test_les_autres_gardes…[disque]`).
- **Gravité** : non bloquant. Cette borne est rejouée de la version 1, inchangée.
- **Preuve** : raisonnement, sur le diff des essais entre `d532ed0ff` et `76c608b6`.
- **Correction** : rendre le cas `{"disk_space": 299}` pour le seul plan « decisif » (refus attendu dans les deux versions), en gardant 149 pour les deux.

## Ce qui a été cherché et tient

- **Garde du corps oubliée ou mal rejouée** : aucune. Le `diff` du corps compte deux blocs.
  - La garde du stockage.
  - La ligne 1073 remplacée par (d), (b), (c), aux places voulues : après (a), avant le texte scellé.
  - Les objets employés sont ceux de la version 1 (essai d'identité).
  - Les clauses de `lv.exiger_code_de_lecture_au_commit` sont toutes reprises :
    - l'ascendance, par (c) ;
    - l'arbre gelé de la tête, par (b), puisque la tête est le commit cité, puis par (c), qui n'admet que des ajouts de la liste ;
    - l'arbre de travail et les fichiers non suivis sous `src/`, par (b).
  - Mauvais objet : (b) et (c) portent sur `racine` et sur le commit lu dans le registre **au commit de la marche**, comme le veut l'additif. (a) garde `reg["commit_lecture"]`.
- **(c)** :
  - `--no-renames`, donc un renommage devient D plus A et est refusé ;
  - « M » refuse aussi un changement de mode, et « T » un changement de type.
- **Entrée et lanceur** : même nombre d'arguments que la version 1 (11 après « commande »), même ordre, `GO_ID` lu dans l'environnement. `_main` est fidèle à `_session … commande`.
- **Égalité à l'octet** : elle n'est pas comparée à elle-même. La version 1 est jouée depuis l'arbre figé, la version 2 depuis l'arbre de commande, au même instant. Aucun champ de la commande ne dépend de `racine`.

## Remarques hors liste (sans correction demandée)

- **Fichier ajouté en lien symbolique.** (c) admet un fichier ajouté (« A ») de la liste même s'il est un lien symbolique, éventuellement vers l'extérieur du dépôt. Le contenu du commit est épinglé par ses 40 signes et lu par la vérification. Aucune correction demandée ; une vérification du mode 100644/100755 par `git ls-tree` serait possible dans une version suivante.
- **« vérifiée » s'écrit avec un é composé (NFC).** Une ligne `GO-LECTURE-B5F` saisie en forme décomposée serait refusée. C'est un blocage, non un desserrement. À dire à celui qui écrira la ligne.
- **Le commit de la marche doit être présent dans le dépôt de l'arbre de commande.** C'est le cas avec deux arbres de travail d'un même dépôt ; un clone séparé devrait le récupérer d'abord. Il en va de même pour la branche distante des entrées.
- **Lignes d'attribution des commits** : décision de la mère, hors de ce jugement.

## Avis sur les cinq écarts nommés par le développeur

1. **`_RUN_LECTURE` récrit, non importé : garder.** C'est un second objet privé du corps. Le récrire est fidèle à la règle de l'additif sur `_montrer`. L'essai compare le motif et ses drapeaux, et vérifie qu'aucun nom privé n'est importé. L'identité retirée de l'essai était fausse par construction : `re` met en cache les motifs compilés, donc les deux objets sont le même.
2. **Garde ajoutée à l'entrée (`exiger_module_joue_depuis`) : garder.**
   - Elle ferme un vrai trou : (b) et (c) vérifieraient un arbre pendant que le code joué en viendrait d'un autre.
   - Avec `python -m`, le dossier courant passe avant `PYTHONPATH` ; la garde le couvre aussi.
   - Les modules de la version 1 viennent du même paquet que le fichier du module, donc du même arbre.
   - Elle ne desserre rien. Sa seule gêne, une `RACINE` différente de l'arbre du lanceur, est voulue.
   - Éprouvée : mutation M16 du développeur, et essai sain par le lanceur de l'arbre de commande.
3. **(c) exige la présence du module et du lanceur : garder.** C'est plus strict que la lettre, sans coût, et éprouvé (`test_c_…_sans_le_module_ou_sans_le_lanceur`).
4. **Le corps prend la tête de la session pour la branche « repetition » : garder.** Cette branche est inatteignable par l'entrée et par le lanceur, qui la refusent tous deux (X07 éprouve la garde du lanceur ; celle du module est éprouvée par l'essai de portée). Elle sert à l'égalité à l'octet voulue au § 3.3. Elle doit rester hors de `__all__` et sans entrée, ce qui est le cas. Son épreuve est à renforcer par le constat 2.
5. **Format de (d) (« vérifiée sha256 <64> », nom de session non vide) : garder.** L'additif laissait le format au développeur. Il est lu en entier ; la citation unique et le nom non vide sont éprouvés (X06 rouge). Ses artefacts sont à compléter par le constat 1. Voir aussi la remarque sur la forme composée de « é ».

## Relevé de méthode

- **Chaîne de raisonnement** :
  1. Empreintes des pièces.
  2. `git diff --name-status` : trois ajouts seulement.
  3. `diff` du corps (version 1, lignes 1049 à 1099, contre version 2, lignes 222 à 274) : deux blocs.
  4. Lecture de (a) à (d) contre la garde de la version 1 (`lecture_v1.py`, lignes 497 à 513).
  5. Lecture des essais, garde par garde, en cherchant les assertions vraies quelle que soit la garde.
  6. Mutations X01 à X07, choisies là où la lecture laissait un doute.
  7. Essais du paquet visé depuis l'arbre de commande, en lecture seule.
- **Objets de contrôle** : chaque mutation est prédite rouge ou survivante avant d'être jouée. X01 et X02 étaient prédites survivantes et ont survécu ; X03 à X07 étaient prédites rouges et sont rouges.
- **Limites** :
  - Je n'ai pas joué les essais du paquet entier, seulement ces quatre fichiers.
  - Je n'ai rien exécuté sur le dépôt réel, la ligne `GO-LECTURE-B5F` n'existant pas.
  - Je n'ai pas relu les 21 mutations du développeur.
- **Par où ce jugement pourrait être bon sans le mériter** : le montage n'est éprouvé que sur des dépôts d'essai, et mes mutations ne couvrent que sept points choisis par lecture.
