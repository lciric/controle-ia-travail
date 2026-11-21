# Mandat du développeur neuf de la seconde passe — corrections après contre-lecture (lanceur de la seconde passe v2) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-21, sous les mots de Lazar « turbo max » et « go tu as
mon mot pour tout » (GO-2026-11-21-63). Pièce de travail (classe C) ; le code produit est de classe B (instrument). Français.

## Ce que ce mandat est
Il fait suite au mandat `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-seconde-passe-lentilles-v1.md`
(4a3cf535…), dont **toutes les règles valent pour toi** (ce que tu lis, ce que tu ne lis jamais, comment tu travailles, commits, aucune
règle nouvelle, refus jamais rejoués, rien ne se lance ni ne se dépense), sauf là où le présent mandat les complète. Le code de la seconde
passe est écrit (commit ffba6bed8, notes jusqu'à a7df1266) ; sa contre-lecture par un agent neuf d'un autre modèle a rendu **« pas
avant »** : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-code-seconde-passe-v1.md` (0c90e0f6…).
Ton travail : **corriger, par versions neuves seulement (R12), ce que cette contre-lecture demande**, et rien d'autre.

## Ordre de lecture (vérifie chaque empreinte scellée)
1. `CLAUDE.md` ; le mandat v1 ci-dessus ; **la contre-lecture 0c90e0f6… en entier**.
2. Les pièces du développeur précédent sous `developpement/` : `noeuds-et-precisions-seconde-passe-v1.md` (ecb803cc…),
   `conformite-code-au-texte-v2-scelle-v1.md` (c8e16b1e…), `empreintes-code-seconde-passe-v1.txt` (20cd3f7a…), ses passations courtes.
3. Le texte de lecture v2 scellé `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (a2bbed7a…), **sans sa liste « Jamais ouverts »**,
   seulement les sections que touchent les corrections (tu n'as pas à le relire en entier : la conformité est faite).
4. Les deux correctifs de la première passe dont la seconde hérite le défaut :
   - pagination de l'arbre du corpus : `corpus_pagine_v1.py`, `lanceur_v8.py` (l'appel explicite vers la ligne 414), la note
     `developpement/notes-correctif-pagination-corpus-v1.md` et sa contre-lecture `contre-lectures/contre-lecture-correctif-pagination-corpus-v1.md` ;
   - tokeniseur demandé par le script voisin du corpus : `cache_tokeniseur_v2.py`, `lanceur_v9.py`, la note
     `developpement/notes-correctif-tokeniseur-act-corpus-v1.md` (cecbad87…), et sa contre-lecture
     `contre-lectures/contre-lecture-correctif-tokeniseur-act-corpus-v1.md` (1e8c1704…, conforme).

## Le travail
1. **Bloquante B1** (module exécuté hors de la liste) : `corpus_pagine_v1` est exécuté par la seconde passe mais absent de ses `MODULES`.
2. **Bloquante B2** (défaut du tokeniseur hérité) : la seconde passe pose le cache par `montage_v1.poser_cache_tokeniseur` (vers la ligne
   212 de `lanceur_seconde_passe_v1.py`), essaie hors ligne seulement (vers 216), puis appelle `montage_v1.calculer_jetons_gardes`
   (vers 259) : elle s'arrêtera sur le même refus 401.
3. **Changement minimal attendu** : un `lanceur_seconde_passe_v2.py` neuf (et un `statistiques_v4` inchangé), avec :
   - `corpus_pagine_v1` et `cache_tokeniseur_v2` dans `MODULES`, et `MODULES_DIFFERENTS = ("statistiques_v4", "lanceur_seconde_passe_v2")`
     ou ce que la contre-lecture exige ;
   - les cibles du corpus prises explicitement de `corpus_pagine_v1`, comme `lanceur_v8` ;
   - la pose du cache par `cache_tokeniseur_v2.poser_cache_tokeniseur(...)`, l'essai en ligne et sans clé (fonction de `lanceur_v9`,
     importée ou recopiée, déclaré), puis `cache_tokeniseur_v2.exiger_cache` ; les deux champs neufs du rapport ;
   - **en cas d'échec de l'essai en ligne, relire le cache par `exiger_cache` pour nommer la cause** (révision du dépôt qui a bougé) :
     c'est la correction non bloquante 1 de la contre-lecture du tokeniseur, à faire ici dans la seconde passe ;
   - les jouets de la seconde passe listent les petits fichiers posés par l'arbre du dépôt du modèle.
   Si un module de la seconde passe (`montage_v2`, `phrases_v2`, `nos_lentilles_v1`…) doit changer, c'est une version neuve
   (`montage_v3`, `phrases_v3`, `nos_lentilles_v2`…), jamais une réécriture ; le lanceur v1 de la seconde passe reste tel quel.
4. **Les six non bloquantes** de la contre-lecture, chacune corrigée ou laissée avec une raison écrite :
   - la note des nœuds, ligne 21, inexacte (les copies de `lenses.py` et `transport.py` sont versées) : note neuve, pas de réécriture ;
   - `phrases_v2` lignes 264 à 268 : ligne d'ensemble non recopiée quand une seule lentille est lue au premier palier ;
   - `phrases_v2` ligne 258 : ligne recopiée sans vérifier que la lecture est inscrite ;
   - lanceur ligne 1157 : phrase « non calculable sur vingt » pour le recouvrement des moitiés ;
   - `phrases_v2` ligne 315 avec le lanceur lignes 928 à 936 : phrase de tête fausse « avant le nœud de la v1 » ;
   - `nos_lentilles_v1` ligne 343 : exiger une seule ligne « Lentille nommée ».
5. **Deux nœuds posés à Lazar** (le 2026-11-21 vers 18:15Z ; défaut (a) chacun à 48 heures, vers le 2026-11-23 18:15Z) : sans mot de
   Lazar d'ici là, **écris le code selon l'option (a)** de chacun, comme la contre-lecture les décrit :
   - lentille non lue dont le dernier palier ne se détermine pas : garder le choix du code ;
   - moment où l'état de la première passe est lu : garder le sens sévère et corriger la phrase de tête.
   Si Lazar tranche autrement, une version suivante le portera ; signale dans ta note les lignes qui en dépendent.
6. **L'essai dépendant de l'ordre** : `tests/test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py::test_cibles_du_corpus_jamais_celles_de_montage_v1_telles_quelles`
   tombe dès qu'un fichier chargé avant lui a importé `corpus_pagine_v1`. Dans la copie neuve pour le lanceur v2, retire aussi l'attribut
   du paquet, pas seulement l'entrée de la table des modules ; l'ancien fichier d'essai reste tel quel, mais dis comment le paquet entier
   passe (ou pourquoi l'échec reste, sans lien avec le code).
7. Essais : R5 pour chaque garde neuve (cas sain et artefact, dont la reproduction du refus 401 et d'un arbre paginé à deux pages par la
   seconde passe) ; essai des essais des gardes neuves ; le paquet `tests/test_lentilles_sondes_bbis_*.py` en entier, **comptes seulement**.
   Tout sur jouets ; aucune requête vers Hugging Face, aucune clé lue.

## Commits
Comme le mandat v1 : branche `claude/brave-galileo-jhp684` seulement ; fetch et merge en nommant la branche, jamais de poussée forcée ;
aucun nom de modèle ; chaque message finit par `Co-Authored-By: Claude <noreply@anthropic.com>` et
`Claude-Session: https://claude.ai/code/session_01Qi7Gr3vedYVukbyqBbHd7z`. Tu n'écris ni fiche ni ligne de registre.

## Rendu
Verdict en une à trois lignes ; commit ; fichiers neufs avec empreintes ; table « correction demandée → ce qui est fait → essai »
scellée dans `developpement/corrections-seconde-passe-v2-v1.md` ; mise à jour scellée des empreintes du code de la seconde passe
(`developpement/empreintes-code-seconde-passe-v2.txt`) ; comptes des essais ; nœuds ouverts ; expositions ; liste des fichiers pour le
contre-lecteur (la même contre-lectrice que la v1 vérifiera les corrections, sur un diff).
