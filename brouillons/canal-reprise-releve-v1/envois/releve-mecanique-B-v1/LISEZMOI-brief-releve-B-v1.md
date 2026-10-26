# Brief — script du relevé mécanique (B) du pilote 4 — v1

De : conv-audit, le 2026-10-26 à 05:50:16 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : un sous-agent neuf de la lignée conv-audit. Tu n'as écrit aucune pièce de ce pilote ni de sa boucle extérieure.

## 1. Le but

Le pilote 4 fait tourner un organisme (la v6.2.1) en deux courses réelles : la course M, finie, et la course S, en cours.
Une boucle extérieure d'agents lira, pour chaque course, des **faits mécaniques** (identité, segments, unités, appels par
rôle et par statut, coûts, durées, recherches, mutation, mémoire, castes, événements), et rien d'autre de la course, pour
juger des hypothèses de conception. Ces faits passent par un **relevé (B)** : un fichier texte par course, à grammaire
fermée, sans aucun score ni aucun texte. Session-depot exécutera le script sur les courses réelles et poussera le relevé
sans l'afficher. **Toi, tu écris ce script et ses essais, sur des pièces de simulation seulement.**

## 2. Pièces

Dans `fournis/`, à vérifier contre `EMPREINTES-fournis-v1.txt` (dans ce dossier) avant lecture :

- `specification-releve-mecanique-B-v1.md` (`3ed32fe8…`) : la spécification, qui fait foi, **avec le complément du § 3**.
  Une v2 est en écriture chez un autre agent ; ses changements se limitent à l'identité et au cas sain de la course S, soit
  ce complément. Je te l'enverrai ; tu te recaleras dessus et le diras.
- `extrait-lignes-ecrites-au-LANCEMENT-par-les-lanceurs-v10-v11-v1.txt` : les lignes « - … » que les lanceurs v10 (course
  M) et v11 (course S) écrivent au `LANCEMENT.md`. C'est du code, pas des données de course.
- `serie-v13-simulation-lanceur-v10/` : la série v13, lanceur v10, mode simulation. Quatre cas sains : la v6.2 en un
  segment, en deux, en trois ; la v5.3. Pour chacun : `LANCEMENT`, extrait mécanique, journaux d'appels, liste
  `A-POUSSER`, chacun renommé avec le suffixe du cas ; ni archive ni liste fermée.
- `releve_appels_simulation_v3.py` (`1e9df693…`) : un relevé d'appels déjà écrit pour cette série, point de départ
  possible ; `releve-serie-v13-v1.txt` (`e99c1a48…`) : ses comptes, référence des essais (§ 6 de la spécification).
- `serie-v14/` : la série v14, lanceur v11, mode simulation, dossiers de course complets tels que le lanceur les laisse :
  `cas-sain-v6-2/pilote4-gemini-v6-2-v1/` (course M sous la forme du v11) ; `cas-sain-v6-2-s/pilote4-gemini-v6-2-s-v1/`
  (course S simulée après une course M saine simulée) ; `cas-seg-segment1/pilote4-gemini-v6-2-v1/` (course sous la forme
  du v11 en deux segments, avec des essais refusés au segment 2 avant celui qui passe, puis fermée ; les dossiers
  `segment-2-t1/` à `segment-2-t9/` sont les pièces de chaque essai du segment 2) ; à côté de chaque dossier, `sortie.txt`
  et `erreur.txt` du lanceur. Aucune course S en segments n'est fermée dans la série : le cas en segments est celui-là.

Toutes ces pièces sont synthétiques (simulation, aucun modèle réel). Dans les dossiers de course, tu n'ouvres que
`LANCEMENT.md`, `EMPREINTES-pilote-v1.txt`, `A-POUSSER-v1.txt` et leurs compagnons, `extrait-mecanique-v1.json` et
`journal-appels-*.jsonl` ; tu ne fais que hacher les autres fichiers. Tu n'ouvres jamais `reponse-question*`,
`question.md` ni rien sous `organisme/`, et tu ne décompresses jamais `ferme.tar.gz`. Le script fera de même.

## 3. Complément à la spécification (décisions de conv-audit)

- **Lignes d'identité** (extrait fourni) : les deux lanceurs écrivent au `LANCEMENT.md` « - organisme : N fichiers,
  empreinte d'arbre … ; question (<COURSE>) : sha256 … » (v10 l. 528 ; v11 l. 545), « - lanceur : <nom>, sha256 … »,
  « - préenregistrement : …, graine <GRAINE> de la course <COURSE> … » (numéros dans l'extrait) et « - dépôt : … ; HEAD :
  … ». Seul le v11 écrit les lignes de la porte « course v6.2 précédente » (l. 379 et 527).
- `identite.question` se déduit de l'empreinte de la question :
  `8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd` → `m` ;
  `a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289` → `s`.
- **Champs d'identité exigés** : nom et lignée de la course, graine, empreinte d'arbre et nombre de fichiers de
  l'organisme, empreinte de la question, nom et empreinte du lanceur, commit du segment 1. **Si l'un manque, ou si
  l'empreinte de la question n'est ni celle de M ni celle de S, le script refuse d'écrire** (code 3 ; motif : le nom du
  champ seulement). Pour tous les autres champs, la règle de la spécification vaut : sans valeur dans la source, `absent`.
- **Champ ajouté** au § 4.2 : `identite.porte_m_precedente = oui|absent` (`oui` si le `LANCEMENT.md` porte la ligne
  « - course v6.2 précédente : … ; lanceur attendu … » du v11 ; `absent` sinon, sans arrêt ; absent pour M par
  construction).
- **Courses réelles** (pour le LISEZMOI et les commandes de session-depot) : course M, nom `pilote4-gemini-v6-2-v1`,
  dossier `essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-v1-tentative2`, lignée `gemini-organisme-v6-2`, lanceur v10 ;
  course S, nom `pilote4-gemini-v6-2-s-v1`, dossier `essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-s-v1` (sans suffixe
  de tentative), lignée `gemini-organisme-v6-2-s`, lanceur v11. La question est servie à g001.
- Le relevé s'écrit dans un dossier de sortie à part, jamais dans le dossier de course, en création exclusive.

## 4. À écrire, sous `sortie/`

- `releve_mecanique_pilote4_v1.py` : bibliothèque standard seule, `python3 -I` ; sortie standard d'une ligne
  (`relevé écrit : <fichier> <empreinte>`) ; codes 0, 2, 3, 4 (spécification, § 7).
- `table-correspondance-releve-B-v1.json` : champ de source → clé du relevé (spécification, § 5) ; son empreinte est
  écrite dans le script, qui refuse une table d'une autre empreinte.
- `essais_releve_mecanique_pilote4_v1.py` et `journal-essais-releve-B-v1.log` (heures lues sur `date -u`).
- `LISEZMOI-releve-B-v1.md` : les réponses aux questions du § 8 de la spécification, établies sur les pièces de
  simulation (noms des champs de l'extrait et des journaux ; ce que le noyau consigne hors de l'archive ; nom du
  manifeste et clé de la graine ; règle de dédoublonnage entre segments ; unité qui sert la question) ; la liste des
  champs qui porteront `absent` en pratique et des fiches qui en deviennent « non observables » (spécification, § 9) ; les
  commandes de session-depot aux dossiers réels, sortie standard redirigée dans un fichier qu'il pousse sans le lire ;
  une table « point de la spécification → traitement ».
- Le compagnon `.sha256` de chacun (« empreinte, deux espaces, nom nu »).

## 5. Essais (R5)

- **Cas sains** : les quatre cas de la série v13, chacun reconstitué en dossier de course par ton harnais (fichiers
  remis à leur nom réel d'après `A-POUSSER`, liste fermée et compagnon fabriqués ; reconstitution déclarée), avec les
  comptes de `releve-serie-v13-v1.txt` et sans double compte entre segments ; les trois cas de la série v14, tels quels.
  Course S : `identite.question = s`, `unite.g001.question_servie = oui`, `identite.porte_m_precedente = oui`, rien de la
  course M recopié dans son relevé. Forme v10 : `identite.question = m`, `identite.porte_m_precedente = absent`.
- Deux exécutions donnent deux relevés identiques, hors de `releve.heure`. Aucune sortie standard ni d'erreur ne porte le
  motif `[0-9][.,][0-9]`.
- **Artefacts** : les dix du § 6 de la spécification ; et (11) une empreinte de question inconnue → refus ; (12) un
  `LANCEMENT.md` sans la ligne de l'organisme et de la question → refus ; (13) un champ d'identité exigé retiré (la ligne
  du lanceur) → refus ; (14) un décimal planté sous un nom de score dans un journal d'appels → non recopié, compté dans
  `sources.champs_ignores`.
- Sous les interpréteurs Python 3.11, 3.12 et 3.13 présents sur la machine (ceux des relectures du script de lecture).

## 6. Interdits

- Rien hors de ce dossier : aucune pièce d'une course réelle, aucun dossier `pilotes/`, aucune branche ni dépôt ; aucun
  `git`, réseau, sous-agent ni clé ; aucun fichier de banque (`banque-*.json`, `*-secret.json`, `*-cle.json`).
- Aucune valeur de score, même simulée, dans tes écrits ; aucun critère ni aucune stratégie de classement des tâches.
- Écrire seulement sous `/var/tmp/releve-mecanique-B-v1/` (`sortie/` pour les pièces, `travail/` pour les copies
  d'essai, vidé à la fin). Heures lues sur `date -u` dans la commande qui les écrit, jamais écrites d'avance. Python
  avec `-I`.

## 7. Fin

Réponse finale en quelques lignes : ce qui est fait, ce qui reste, écarts déclarés, empreintes des pièces.
