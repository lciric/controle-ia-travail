# Contre-lecture de la différence brouillon 6 → brouillon 7 — lecture des sondes figées sur le saboteur à budget (barreau 8) — v1

## En-tête

- Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon7.md`, empreinte `8749b51816fca87987c3e163fd0b5e872164812f19287f102f95ad92c7fcf337` (vérifiée, égale à celle donnée ; 413 lignes).
- Point de départ : brouillon 6, `527ed753e2434f0fd542e8f9a8c62ebcbf9ea7b32c7a8564ebed7c924ae65521` (vérifiée). Différence faite par moi, par programme (`diff` : 37 blocs, 85 lignes marquées, 159 lignes de sortie ; puis différence mot à mot par `git diff --no-index --word-diff`, dans le dossier temporaire). La note des différences du rédacteur n'a servi qu'à comparer.
- Contre-lecteur : Opus 5.5 (`claude-opus-5-5`), neuf : n'a écrit aucun brouillon ni aucune contre-lecture antérieure de ce texte, ni la note d'interface ; ne connaît ni le sujet ni le mécanisme du saboteur.
- Heures (`date -u`) : début 2026-11-19 01:18:13 UTC ; fin : voir la dernière ligne.
- Exposition déclarée : la note d'interface dit le mode de sabotage, « coût » (seul) ; lu, déclaré (décision sur les modes de sabotage, N-054, point 3).

### Fichiers lus, avec plages (empreintes vérifiées égales à celles données)

| fichier | plage | empreinte |
|---|---|---|
| `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon7.md` | entier, lignes 1 à 413 | `8749b518…f337` |
| `…/prereg-lecture-sondes-barreau8-v1-brouillon6.md` | par la différence ; et en entier ses lignes 44, 214, 220, 276, 340, 343, 383, 384, 408 | `527ed753…5521` |
| `…/contre-lecture-brouillon6-v1.md` | entier | `2ab73c2f…3f587` |
| `…/differences-brouillon6-brouillon7-v1.md` | entier | `1f622b53…9eb7` |
| `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md` | entier (111 lignes) ; égale à son compagnon ; aucun renvoi de provenance suivi | `20c9ed6e…ce1` |
| `src/controle_ia/prereg.py` | entier (76 lignes) | `3b2e3ee5…c306`, égale à la citation du texte |
| `CLAUDE.md` | donné en contexte | — |

- Les deux notes d'identités des sondes : empreintes vérifiées (`fd7bf835…5da7`, `36caffb4…3398`), **non ouvertes** : la table des identités n'est pas dans la différence. `src/controle_ia/scellement.py` : empreinte relevée (`93beeb1c…ef2`), non lu.
- Rien d'autre. Aucun fichier sous `docs/verdicts/`, `donnees/`, `diag/`, `runs/`, `scripts/`, `registres/`, `src/controle_ia/iib/`, `src/controle_ia/barreau8_moniteurs/`, ni du dossier du saboteur ; aucun historique git ; aucun fichier d'un autre agent du dossier temporaire.
- **Lectures incidentes déclarées** : (1) la note d'interface, question (11), donne des noms de champs de l'oracle (noms seulement, sans valeur ni sens) ; (2) la note, point (e), nomme le chemin d'un fichier de consigne privée et d'autres chemins de la course : noms seulement, rien d'ouvert ; (3) un `ls` du dossier de la note, filtré par `grep` sur le nom de la version 6 : la sortie n'a montré que la note et son compagnon. Aucune ligne de valeurs rencontrée.

### Sortie exacte du validateur

`PYTHONPATH=src .venv/bin/python` → `prereg.problemes('brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon7.md')` :

`['section vide ou à remplir : Contre-lecture']`

- Marqueurs « À REMPLIR » : **exactement deux**, ligne 75 (F-3, entropie racine des graines) et ligne 413 (entrée « Contre-lecture 4 (finale, texte rempli) »). Conforme.
- Motif des entrées (`prereg.py`, ligne 29) : `^\s*-?\s*\**Contre-lecture (\d+)\**`. Entrées reconnues dans la section : `1`, `2`, `3`, `3` (la « Contre-lecture 3 bis » est lue comme une entrée « 3 » à part : le motif s'arrête au nombre), `4`. Chaque entrée est contrôlée sur son propre segment (deux empreintes distinctes exigées). Les deux entrées de numéro 3 **ne gênent pas** le validateur ; seul défaut, sans conséquence : un message d'erreur sur l'une d'elles dirait « contre-lecture 3 » sans dire laquelle.
- Essais sur copies, dans le dossier temporaire (script `verif7/essai.py`) :

| copie | sortie |
|---|---|
| entrée 4 remplie avec deux empreintes distinctes, entropie remplie | `[]` (attendu vide : conforme) |
| entrée 4 remplie, entropie encore ouverte | `['marqueur À REMPLIR restant hors des sections exigées']` |
| entropie remplie, entrée 4 ouverte | `['section vide ou à remplir : Contre-lecture']` |
| tout rempli, entrée 4 avec une seule empreinte | `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']` |
| tout rempli, entrée 4 avec la même empreinte deux fois | `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']` |
| tout rempli, entrée 3 bis privée de l'empreinte de son rapport | `['contre-lecture 3 sans ses deux empreintes (brouillon relu et rapport)']` |
| tout rempli, entrée 3 privée de l'empreinte de son rapport | `['contre-lecture 3 sans ses deux empreintes (brouillon relu et rapport)']` |

### Contrôles mécaniques

- **Conditions de départ** : D-1 à D-13, soit **13** ; aucune autre. Conforme.
- **Taille** : 98 672 640 + 73 728 000 + 1 055 129 600 + 275 251 200 = **1 502 781 440** octets ; marge 497 218 560. Inchangée, exacte.
- **Clés de registre** : six, orthographe constante (`SCELLEMENT-SONDES-IIB` ×6, `CODE-PASSE-IIB` ×12, `CODE-LECTURE-SONDES-IIB` ×6, `LIVRAISON-PASSE-IIB` ×4, `ETATS-COURSE-IIB` ×4, `LECTURE-SONDES-IIB` ×2). Conforme.
- **Renvois** : liste d'arrêt, lignes 3, 7, 10 et 15 ; lignes S1, S3, L2, L5, L6, AU-a ; passages (b-1) à (b-10) : chacun pointe sur le bon objet. Aucune contradiction de renvoi créée par la différence.
- **Extrait des états** : texte constant de `avertissement` égal, caractère pour caractère (comparaison par programme), à celui de la note version 6 ; les quatre clés de premier niveau, les clés `phrase`, `par_paire`, les quatre paires, les bases `cout`, `traits`, `mots_et_cout`, l'état `unite`, et la paire `B100-TJ100` à la seule clé `mots_et_cout` : **exactement ceux de la note version 6, à tous les niveaux**. Les quatre phrases du dommage et la phrase de la diffusion : égales, par programme. Treize états (3 paires × 4 clés + 1) : compte juste. Ce que le texte ajoute à la note (types, `null` permis à la seule `lecture_diffusion.phrase`, `run_id` non vide, sans saut de ligne, au plus 200 caractères) est plus strict, non contraire ; un refus n'a d'autre effet que d'arrêter la lecture et de porter le fait à la session mère.
- **Versions de la note** : toutes les citations hors historique sont en version 6 (en-tête, l. 23 ; table I, l. 54 ; I-9, l. 66 ; D-12, l. 96 ; garde d'alignement, l. 280). Les versions 5 et 3 ne paraissent qu'à la ligne 23, comme versions remplacées, avec leurs empreintes. Conforme.
- **Garde d'alignement** : l'empreinte citée, `177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424`, est celle de `tokenizer_config.json` à la question (1) de la note (égalité par programme). Le texte ne suppose plus aucune valeur : il exige un booléen, le lit, le passe explicitement ; l'empreinte du fichier fige son contenu, donc la valeur. Cas de refus : fermés, à un près (le fichier absent n'est pas nommé : remarque M-2).

## Table N-1 à N-11

| n° | appliquée ? | où, dans le brouillon 7 ; avis |
|---|---|---|
| N-1 (bloquante) | **oui, adaptation fidèle et plus stricte** | l. 44 : texte de remplacement repris mot pour mot ; l. 214 : titre repris, avec « avant le scellement » en plus ; l. 220 : « Règle du scellement » reprise sans « ou si un défaut (a) échoit » — juste, puisqu'aucun défaut (a) n'existe plus ; l. 218 : (a) « non retenue ». Règle générale à la l. 44 ; blocs alignés : témoin-jumeau (l. 144, l. 328), organisation de la passe (l. 188), taille (l. 212), sondes et couches (l. 301, l. 320). Vérifié : aucun défaut différent du texte ne reste (point 3 ci-dessous) |
| N-2 | **oui** | (b-5) corrigée (l. 226) ; (b-7) à (b-10) ajoutées (l. 228 à 231), textes repris mot pour mot. Reste une incomplétude de (b-10), sans effet après le scellement (M-3) |
| N-3 | **oui, mise en forme adaptée, mots fidèles** | l. 23 (adaptation déclarée : « lue par différence faite par programme avec la version 5, elle-même lue en entier ») ; l. 54 ; I-9 (l. 66) mot pour mot ; D-12 (l. 96) mise sur une ligne, mots du remplacement (deux phrases liées par « ; » au lieu de points) ; « Seuil », condition jugée (b) (l. 153) ; liste d'arrêt, ligne 3 (l. 388) mot pour mot |
| N-4 | **oui, mise en forme adaptée, mots fidèles** | Garde P3, clause (b) (l. 280), texte repris sur une ligne ; trace, liste fermée (l. 255) mot pour mot. Hypothèse de décodage retirée |
| N-5 | **oui** | B8-P5 et B8-P6 (l. 119, 120) ; plan, point 5 (l. 169) : clé `descriptif/<sonde>/<jeu>` ajoutée. Mot pour mot |
| N-6 | **oui** | P7 (l. 284) ; point (3) de « n'observe plus » (l. 271) ; r8 (l. 268), « quatre couples ». Mot pour mot |
| N-7 | **oui** | S2 (l. 344) et S5 (l. 347). Mot pour mot |
| N-8 | **oui** | « Passe avant » (l. 237) ; audit, contenu (1) (l. 378). Mot pour mot |
| N-9 | **oui, adaptation acceptée** | l. 52, l. 387, l. 413 : « Contre-lecture 4 (finale, texte rempli) ». Entrée « Contre-lecture 3 bis » ajoutée (l. 412) : ses faits sont ceux du rapport (neuf, différence 4 → 6, une bloquante, quatre à corriger, six mineures, deux empreintes justes). Le validateur la reconnaît (ci-dessus) |
| N-10 | **oui** | l. 7 (brouillon 6 fini à 01:04Z ; brouillon 7 daté) ; l. 209 (marge « avant l'index, la trace, le bordereau et les compagnons »). Observation : la l. 7 dit le brouillon 7 écrit « entre 01:12Z et 01:16Z », la note des différences « entre 01:12Z et 01:18Z » (elle compte sans doute sa propre écriture) ; sans conséquence |
| N-11 | **oui** | L6 (l. 353). Mot pour mot |

## Changements sans remarque correspondante

- l. 1 et l. 3 : numéro du brouillon (6 → 7). Attendu.
- l. 5 : « contre-lecteurs des brouillons 1, 3, 4 et 6 ». Conséquence de N-9 (entrée 3 bis). Juste.
- l. 313 : « (pour mémoire de ce que Lazar peut changer avant le scellement) ». Conséquence de l'alignement de N-1. Juste.
- Toutes les autres lignes changées relèvent d'une remarque (table ci-dessus). **Aucun changement hors remarque.**

## Point 3 — défaut, option ouverte, « d'un mot » après le scellement

- « Lazar peut … changer d'un mot » : six occurrences (l. 44, 144, 188, 212, 214, 301), toutes suivies de « avant le scellement » ; l. 328 aussi. Aucune ne peut jouer après.
- Défauts : l. 212 « (t1) », l. 320 « (a1), état de ce texte », l. 328 « (b), état présent de ce texte » : tous égaux à l'état du texte, chacun suivi de « après le scellement, aucun défaut n'échoit ». Aucun défaut différent du texte.
- Aucune décision « ouverte » ne reste (le seul « ouvertes », l. 111, dit que les lectures décisives sont ouvertes dans les deux sens).
- Reste des éléments dits « proposé(s) avec recommandation » hors des blocs de décision (niveau de la clause (3), l. 146 ; P3, P7, P10 ; tolérance de r7). Ils n'ont aucune option de remplacement, et le défaut d'une proposition avec recommandation est la recommandation, c'est-à-dire l'état du texte : **aucune latitude après le scellement**. Remarque sans correction.

## Remarques neuves

### M-1. Bloquante pour le scellement — la règle de la dernière contre-lecture interdit de verser l'entropie après elle

- **Passages** : liste d'arrêt, ligne 2 (l. 387) : « ou un texte soumis au scellement qui diffère du texte relu par la dernière contre-lecture ailleurs que dans cette entrée » → « pas de scellement » ; entrée 4, « Règle » (l. 413) : « le texte scellé ne diffère du texte relu par cette dernière contre-lecture que par cette entrée ».
- **Défaut** : l'entrée 4 était conçue pour une contre-lecture du **texte rempli** (entropie versée). Le cadre fixé plus haut fait de **ce** rapport, lu sur le brouillon 7 où F-3 est encore ouvert, l'entrée 4 ; l'entropie est tirée ensuite par la session qui scelle. Le texte scellé différera alors du texte relu à la ligne 75 (F-3), hors de l'entrée : la ligne 2 de la liste d'arrêt interdit ce scellement, et un texte scellé ainsi violerait à sa naissance sa propre liste d'arrêt (écart au préenregistrement). Aucune lecture de la règle ne l'évite.
- **Texte de remplacement** :
  - l. 387, remplacer « ou un texte soumis au scellement qui diffère du texte relu par la dernière contre-lecture ailleurs que dans cette entrée » par « ou un texte soumis au scellement qui diffère du texte relu par la dernière contre-lecture ailleurs que dans cette entrée et dans la cellule « état et raison » de F-3 (où seule l'entropie tirée remplace le marqueur), constaté par une comparaison faite par programme » ;
  - l. 413, remplacer « **Règle** : le texte scellé ne diffère du texte relu par cette dernière contre-lecture que par cette entrée ; » par « **Règle** : le texte scellé ne diffère du texte relu par cette dernière contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; ».

### M-2. Mineure — garde d'alignement : le fichier de configuration absent n'est pas nommé

- **Passage** : P3, clause (b) (l. 280).
- **Défaut** : la liste des refus avant chargement nomme le champ manquant, le type, l'empreinte et l'appel, pas le fichier absent ; la garde P1 ne couvre que les fichiers de la course et des sondes. L'empreinte « différente » le couvre sans doute, mais un cas de refus doit être nommé (cas fermés).
- **Texte de remplacement** : remplacer « **Si le champ manque, n'est pas un booléen, » par « **Si le fichier est absent, si le champ manque, s'il n'est pas un booléen, ».

### M-3. Mineure — le retour à (a), passage (b-10), laisse « Le texte est scellé sous (b) » dans le bloc

- **Passage** : l. 231. Sans effet après le scellement (texte scellé sous (b)) ; ne jouerait que si Lazar disait (a) avant.
- **Défaut** : sous (a), la « Règle du scellement » (l. 220) dirait encore « Le texte est scellé sous (b) », et les l. 217 et 218 « (b), appliquée » et « (a), non retenue ».
- **Texte de remplacement** : remplacer « (b-10) ce bloc de décision : son titre dit « texte écrit sous (a) », et la liste (b-1) à (b-10) reste comme mémoire de la différence. » par « (b-10) ce bloc de décision : son titre dit « texte écrit sous (a) » ; (b) y est dite « non retenue » et (a) « appliquée » ; sa « Règle du scellement » dit « Le texte est scellé sous (a). **Après le scellement, aucun défaut n'échoit** : tout passage à (b) est un écart au préenregistrement, nœud de Lazar. » ; la liste (b-1) à (b-10) reste comme mémoire de la différence. »

### M-4. Mineure — le texte scellé dirait « Il reste deux marqueurs ouverts » et « brouillon 7, non scellé »

- **Passages** : l. 52 ; l. 1 et l. 3.
- **Défaut** : la règle de M-1 interdit de toucher ces lignes au scellement ; le texte scellé affirmerait donc des marqueurs ouverts qui ne le sont plus, et un statut « non scellé ».
- **Texte de remplacement** (dans le brouillon qui suit) :
  - l. 52 : remplacer « **Il reste deux marqueurs ouverts : F-3 (entropie des graines) et l'entrée « Contre-lecture 4 (finale, texte rempli) » de la section « Contre-lecture ».** » par « **Au dernier brouillon, deux marqueurs restaient ouverts, et deux seulement : F-3 (entropie des graines) et l'entrée « Contre-lecture 4 (finale, texte rempli) » de la section « Contre-lecture » ; ils sont remplis au scellement, et rien d'autre ne change.** » ;
  - l. 3 : remplacer « **Statut : brouillon 7, non scellé comme préenregistrement.** » par « **Statut : brouillon 8, texte soumis au scellement ; il n'est scellé que si son compagnon `.sha256` et la ligne `SCELLEMENT-SONDES-IIB` le disent.** » (et, à la l. 1, « brouillon 7 » devient « brouillon 8 »).

### Observations sans correction du texte

- La note d'interface version 6 garde, dans son en-tête (sa ligne 6), « **Version 4** … la version 3, dans ce dossier, est remplacée par celle-ci » : en-tête périmé de la note, à signaler au côté exposé. Le texte la cite par chemin et empreinte : aucun effet sur lui.
- Le validateur ne contrôle pas que les deux empreintes de l'entrée 4 sont les bonnes (il en compte deux distinctes) : la comparaison faite par programme de la session mère tient lieu de ce contrôle.

## Procédure de remplissage (point 7), à la lettre

Elle vaut pour le texte relu par la dernière contre-lecture (le brouillon qui suivra, corrigé de M-1 ; les deux chaînes ci-dessous y restent uniques, vérifié sur le brouillon 7 : une occurrence chacune).

1. Copier le brouillon relu, octet pour octet, au chemin de scellement choisi par la session mère (nom versionné neuf, R12), qu'elle inscrira à la ligne `SCELLEMENT-SONDES-IIB`.
2. Tirer l'entropie **une seule fois**, sans essai préalable : `PYTHONPATH=src .venv/bin/python -c "import numpy as np; print(np.random.SeedSequence().entropy)"` ; consigner la commande, la version de numpy et l'heure UTC.
3. **Premier remplacement** (ligne 75, cellule « état et raison » de F-3) : remplacer la chaîne exacte
   `À REMPLIR — À FIXER : tirée par la session mère au scellement`
   par
   `<entier décimal tiré> (tirée une seule fois par la session mère au scellement : numpy.random.SeedSequence().entropy, numpy <version>, <AAAA-MM-JJTHH:MMZ>)`
   (aucun « À REMPLIR » ; le reste de la ligne `| F-3 | entropie racine des graines | … |` inchangé).
4. **Second remplacement** (ligne 413) : remplacer la ligne entière qui commence par `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` et finit par `versée avec l'empreinte du texte scellé.` par une seule ligne de la forme :
   `- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle <modèle>, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface ; vérification de la différence du brouillon <précédent> au brouillon <relu>. Brouillon relu : `<chemin>`, empreinte `<64 caractères>`. Rapport : `<chemin du rapport>`, empreinte `<64 caractères>`. Conclusion : « PRÊT : … ». **Règle** : le texte scellé ne diffère du texte relu par cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.`
   (la ligne doit commencer par `- **Contre-lecture 4` pour le motif du validateur, porter deux empreintes distinctes et aucun « À REMPLIR »).
5. Comparaison faite par programme entre le brouillon relu et le texte rempli : **exactement deux lignes changées, 75 et 413**, rien d'autre ; la verser avec l'empreinte du texte scellé.
6. `prereg.problemes(<texte rempli>)` doit rendre `[]` ; essai de cette garde sur un cas sain (le texte rempli) et sur un artefact (une copie où un seul des deux champs reste ouvert), versé (l. 50, R5) ; puis `sceller_prereg` ; puis la ligne `SCELLEMENT-SONDES-IIB` ; l'heure de scellement consignée à côté de l'heure de la première sortie de la course (D-7).

**Ce rapport ne peut pas être cette entrée 4** : il conclut « pas prêt » (M-1). L'entrée 4 sera le rapport de la vérification du brouillon corrigé.

## Conclusion

PAS PRÊT : liste fermée des corrections, à porter dans un brouillon 8 qui ne change rien d'autre (hors de sa date, l. 7) :
- **bloquante** : M-1 (liste d'arrêt, ligne 2, et « Règle » de l'entrée 4 : permettre le versement de l'entropie dans la cellule de F-3) ;
- **mineures** : M-2 (fichier de configuration absent nommé dans les refus de la garde d'alignement) ; M-3 (passage (b-10) complet) ; M-4 (ligne 52, statut et titre).

N-1 à N-11 sont toutes réellement appliquées, mot pour mot ou par adaptation fidèle ; aucun changement hors remarque ; aucune contradiction de renvoi ; extrait des états exactement conforme à la note version 6 ; garde d'alignement sur l'empreinte juste, sans valeur supposée. Une fois ces corrections portées, une vérification courte de la différence 7 → 8 par un contre-lecteur neuf (attendu : sept remplacements — deux pour M-1, un pour M-2, un pour M-3, trois pour M-4 — plus la date) peut tenir lieu de « Contre-lecture 4 (finale, texte rempli) ».

**Aucun refus d'outil.**

Fin : 2026-11-19 01:23:50 UTC.
