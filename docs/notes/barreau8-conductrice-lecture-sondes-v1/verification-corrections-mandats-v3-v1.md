# Vérification des corrections des projets de mandats du lecteur des sondes, du juge et de l'auditeur (lecture des sondes sur le saboteur à budget, barreau 8), version 3, brouillon 2 — v1

Pièce de travail, écrite le 2026-11-24 entre 16:30Z et 16:50Z par le contre-lecteur des projets de mandats du barreau 8 (sous-agent Opus 5.5 de la conductrice du côté des moniteurs, session `session_01Qi7Gr6acCdYGKsotBtUNvE`), auteur de la contre-lecture `contre-lecture-mandats-v3-brouillon1-v1.md` (`e9c3e339f0b19e430511022147c6c8f65f019160b5a81748ebc636b9ecca1251`), même contre-lecteur, règle des pièces d'instrument. Pièces vérifiées (commit `a85c9e893`), empreintes égales à leurs compagnons :

| pièce | empreinte |
|---|---|
| `projet-mandat-lecteur-sondes-v3-brouillon2.md` | `119e6040a4db728b587295d0f9c2b6e551ee2e6b062f88f01e790ccb797e0c3a` |
| `projet-mandat-juge-lecture-sondes-v3-brouillon2.md` | `b368e2eaf3ef656e6941a87af5e58fc47e27b10a3acade226e2edd8e2e245b60` |
| `projet-mandat-auditeur-lecture-sondes-v3-brouillon2.md` | `336e9958452179a035ca6392e7f9772b0a93b1e5274b43b03c6de38486ef9b75` |
| `ecarts-brouillon2-vers-v3-v1-erratum-1.md` | `2d1ca9c79bec24a611190e81695edf6c27594225cb3dbf4fcb9667cca4c6fed3` |
| `corrections-contre-lecture-mandats-v3-v1.md` | `832f0601eedd80a64ff9274dbc98ceb70f632cf108002355c9f39cfad5beb135` |

(tous dans `docs/notes/barreau8-conductrice-lecture-sondes-v1/`.)

## Verdict

**À corriger**, sur deux points majeurs, tous deux nés des corrections (le premier vient de ma propre proposition de la remarque M-6) :

1. **Contrôle du déclenchement de l'audit** (juge et auditeur, « Pour la session mère ») : la commande qui imprime le booléen lève une exception sur toute sortie des lignes S1, S3, S4 et L5, où le code n'évalue aucun déclencheur ; le mandat dit alors « rien n'est lancé » : **le juge ne serait jamais lancé** dans ces issues. Correction ci-dessous (V-1).
2. **Lancement détaché** (lecteur, étapes 1 et 3 ; auditeur, étape 3) : « LANCE » s'imprime **toujours**, même quand le lancement est refusé, et le contrôle du fichier `.pid` se fait en arrière-plan, sans verrou atomique. L'exécution unique tient en pratique, mais l'agent ne voit pas le refus. Correction ci-dessous (V-2).

Tout le reste est fait et juste : la bloquante, les onze majeures et les seize mineures, aux réserves près des mineures V-3 à V-5 et des deux constats que je n'ai pas pu vérifier sous mes interdits (« Non vérifié par moi »). Les trois écarts de forme sont acceptables. Le lancement détaché, une fois V-2 appliquée, est correct : une seule exécution, aucune relance, aucun chiffre affiché.

Comptes : 2 majeures, 3 mineures ; aucune bloquante.

## Remarques restantes

**V-1 (majeure ; juge, lignes 18 à 22 et 115 ; auditeur, lignes 18 à 22) — Le contrôle du déclenchement échoue quand la sortie n'évalue aucun déclencheur.**
- Constat : `_lecture_decisive` initialise `"declencheurs_de_l_audit": {}` (code, ligne 2462) et rend la sortie sans le remplir sous les lignes S1 (ligne 2472), S3, S4 et L5 (ligne 2495) ; la clé `audit_de_symetrie_declenche` n'existe alors pas. Essai fait sur deux sorties factices de même forme (`{"resultat": {"declencheurs_de_l_audit": {}}}` et la même avec `false`) : la commande du brouillon 2 lève `KeyError: 'audit_de_symetrie_declenche'` sur la première ; « Toute autre sortie (exception) : rien n'est lancé » bloque alors le juge. La commande `audit` du code lit, elle, `.get(...)` (ligne 2655) et refuse `[15]` : l'absence vaut « aucun audit ». L'erreur vient de ma proposition M-6, que le rédacteur a recopiée.
- Correction (texte exact, dans les deux blocs « Pour la session mère ») : remplacer `['audit_de_symetrie_declenche'] is True` par `.get('audit_de_symetrie_declenche') is True`, soit :

  ```
  cd /home/user/controle-ia-travail && .venv/bin/python -I -c "import json,sys; print(json.load(open(sys.argv[1], encoding='utf-8'))['resultat']['declencheurs_de_l_audit'].get('audit_de_symetrie_declenche') is True)" <chemin de la sortie de la lecture>
  ```

  (essai : « False » sur les deux sorties factices) ; et ajouter après « « False » : … » : « (la clé est absente sous les lignes S1, S3, S4 et L5, où la sortie n'évalue aucun déclencheur : le contrôle rend alors « False ») ». Juge, étape 4, après « Tu constates dans la sortie la valeur de `declencheurs_de_l_audit.audit_de_symetrie_declenche` » : ajouter « (clé absente, sous les lignes S1, S3, S4 et L5 : vaut faux) ».

**V-2 (majeure ; lecteur, lignes 122, 166 et 184 ; auditeur, lignes 123 et 138) — Le refus de lancer n'est pas visible, et le verrou n'est pas atomique.**
- Constat : dans `cd … && test ! -e <…>.pid && setsid nohup bash -c '…' < /dev/null > /dev/null 2>&1 & echo LANCE`, l'opérateur `&` porte sur toute la chaîne `cd && test && setsid …`, qui part en arrière-plan ; `echo LANCE` s'exécute toujours. Essai fait (commande factice, dans mon bloc-notes) : avec le `.pid` présent, rien n'est lancé, mais « LANCE » s'imprime. Le test du `.pid` est donc asynchrone, et le `.pid` n'est écrit qu'après le départ du processus de calcul : deux lancements à moins d'une fraction de seconde passeraient tous deux. L'agent ne voit pas un refus, ni un échec du `cd`.
- Correction (texte exact) : dans les trois lancements, remplacer `test ! -e <DOSSIER_JOURNAL>/<n>-<nom>.pid && setsid nohup bash -c '…' < /dev/null > /dev/null 2>&1 & echo LANCE` par :

  ```
  mkdir <DOSSIER_JOURNAL>/<n>-<nom>.verrou && { setsid nohup bash -c '…' < /dev/null > /dev/null 2>&1 & } && echo LANCE || echo "RIEN N'EST LANCÉ"
  ```

  (le contenu de `bash -c '…'` inchangé ; `<n>-<nom>` valant `1-reception`, `3-lecture` ou `3-audit`) ; et, dans les règles (lecteur, ligne 122 ; auditeur, ligne 138), remplacer « le lancement refuse de partir si le fichier `.pid` de l'étape existe déjà » par « le lancement refuse de partir si le verrou `<n>-<nom>.verrou` de l'étape existe déjà (sa création est atomique) ; « RIEN N'EST LANCÉ » imprimé : arrêt et report, aucune autre tentative ». Essai fait de cette forme : premier lancement « LANCE », second « RIEN N'EST LANCÉ », rien de lancé la seconde fois.

**V-3 (mineure ; lecteur, ligne 127 ; auditeur, ligne 126) — « relance-le » se lit mal à côté de « aucune relance ».** Correction : « relance alors **l'appel d'attente** (jamais l'étape), tant que l'étape n'est pas finie ».

**V-4 (mineure ; lecteur, lignes 43 et 159 ; auditeur, lignes 38 et 103) — `mkdir` sans `-p` : pas de procédure pour une relance décidée par la mère.** L'écart de forme est bon (un journal ancien ne se mêle pas au neuf), mais le chemin du journal est scellé dans le mandat : après un arrêt technique, l'étape 0 échouera. Correction (« Pour la session mère », lecteur et auditeur) : « Relance décidée par la session mère après un arrêt technique : constater par `kill -0` que le processus de l'ancienne tentative ne vit plus ; verser l'ancien journal ; puis le renommer `<DOSSIER_JOURNAL>-tentative-<k>` (jamais l'effacer) avant de relancer l'agent. »

**V-5 (mineure ; auditeur, étape 4, lignes 147, 148 et 153) — Cas de la relecture arrêtée.** Quand la relecture s'est arrêtée, `relectures` vaut la chaîne « relecture arrêtée : voir le défaut D3 » (code, ligne 2717) : « production relue égale » et « états relus égaux » n'existent pas, sans être « faux ». Correction : ajouter après le point 5 : « Si `relectures` vaut « relecture arrêtée : voir le défaut D3 », les points 4 et 5 ne sont pas relus ; ce n'est pas une relecture inégale : l'issue est AU-a par le défaut D3 (étapes 5 et 6). »

## Remarque par remarque : ce qui est fait et juste

| remarque | état | constat |
|---|---|---|
| B-1 | faite, juste | « Consignes du dépôt » dans les trois mandats (lecteur, ligne 113 ; juge, ligne 91 ; auditeur, ligne 89) : pas de routine de reprise ; ni `registres/etat.md`, ni passations, ni `registres/rappels.md`, ni `registres/decisions.md`, ni `registres/go.md` ; registre propre par un `grep` des huit clés seulement ; `git` borné à `git status --porcelain --untracked-files=all` (juge : aucune commande `git`) ; aucun essai du dépôt, aucune autre session |
| M-1 | faite, juste | section `1:8`, § 8 de la pièce de rang 1, premier élément de `ordre.pieces`, dans les trois mandats et les tables des champs ; égal au champ `exclus.section` de la pièce d'attestation (`8f6b5025…e76a`) |
| M-2 | faite, juste | `sha256sum` et `scellement verifier` des deux fichiers avant le scellement (lecteur, ligne 20 ; juge, ligne 24) et dans l'étape 0 (lecteur), l'étape 1 (juge) et l'étape 0 (auditeur) ; « empreintes seulement, jamais ouverts » |
| M-3 | faite, juste (écart de forme accepté, plus V-2 à V-4) | commandes en entier, en un seul appel, préfixées par `cd /home/user/controle-ia-travail` ; nom de la course tiré dans le même processus que la lecture et écrit au journal ; essai : `RUN_ID` bien rempli dans le processus détaché |
| M-4 | faite, juste | décision définitive avant le scellement, deux mandats neufs si la pièce arrive ensuite (lecteur, ligne 18) ; étape 0, second appel (`test ! -e` ou `sha256sum`) ; juge, étape 1 |
| M-5 | faite, juste | `<DESIGNATION_…>` dans les trois mandats ; chaque agent déclare son identifiant de session |
| M-6 | faite, mais voir V-1 | enchaînement juste (booléen contrôlé par la mère sans ouvrir la sortie ; juge lancé après le scellement du rapport ou avec « aucun audit » ; refus `[15]` écrit) ; la commande du booléen est à corriger (V-1) |
| M-7 | faite, juste | texte égal à la règle RP-9 (additif 1, ligne 444) et au code (`reserves_de_rp9`, lignes 2421 à 2435 ; `de_la_version_6`, ligne 323) |
| M-8 | faite | sixième réserve ajoutée, mot pour mot égale à la constante du code (lignes 111 et 112) ; lieu au texte scellé : voir « Non vérifié par moi » |
| M-9 | faite, juste | juge, « Règles », ligne 188 ; rendu limité à l'identifiant de ligne de la table (ligne 128) |
| M-10 | faite (écart de forme accepté, plus V-5) | lecture point par point : points 1 à 3 par l'absence de D1, D2, D3 ; points 4 et 5 dans `relectures` ; point 6 dans « longueurs (point 6), rapportées » : clés égales au code (lignes 2711 à 2718) |
| M-11 | faite, juste | règle complétée (juge, ligne 172), conditions de (iv) à (vii) et (x) nommées par les champs de la sortie (clés contrôlées : `designation_apres_la_premiere_sortie_de_l_evaluation`, ligne 1901 ; heure de remise, ligne 2997 ; `premiere_sortie_de_la_course`, ligne 1902 ; `sections_changees_ou_absentes`, ligne 1823) ; (v) lue dans la table neuve (code, ligne 2986) |
| m-1 | faite, juste | heures des pièces neuves cohérentes avec les fichiers (16:28Z) et le commit (16:29:06Z) ; erratum 1, point 1 |
| m-2 à m-9 | faites, justes | aux lieux dits par le relevé ; m-6 : le juge lit les aires dans la sortie (`aires_minimales_detectables.par_fraction`, code, lignes 2462 et 2848) et le fichier passe aux interdits |
| m-10 | faite, juste | auditeur, étape 4, point 1, à la lettre de l'additif 1, ligne 440 |
| m-11 | faite, juste | auditeur, étapes 5 et 6 (D3 recopié, issue AU-a) ; erratum 1, point 2 (code, lignes 1411, 1441, 2684, 2691 et 2695, contrôlées) |
| m-12 | faite, juste | auditeur, étape 1 ; erratum 1, point 3 (lignes 1532, 1533, 2867, 3068) |
| m-13 à m-16 | faites, justes | aux lieux dits par le relevé |

## Les trois écarts de forme

1. **Registre des accords, chemin seulement** (lecteur, ligne 98) : plus strict que ma proposition et suffisant ; le code contrôle la ligne (refus `[D-4]`). Accepté.
2. **`mkdir` sans `-p`** : accepté ; il empêche le mélange de deux tentatives ; voir V-4 pour la procédure de relance.
3. **Relecture inégale : rapport scellé « aucune issue : arrêt », porté à la mère** (auditeur, étape 4 ; juge, étape 4) : accepté. Le texte scellé (ligne 402) attend AU-a ou AU-b, mais la liste fermée (ligne 401) ne range pas une production relue différente parmi les défauts : écrire AU-b dirait « aucun défaut établi » sur une relecture qui ne se reproduit pas. L'arrêt avec rapport scellé et report, sans défaut inventé, est la règle commune des lacunes (« une combinaison que la table ne couvre pas : tu ne tranches pas »), et le juge la traite de même. Voir V-5 pour le cas voisin de la relecture arrêtée.

## Le lancement détaché

Contrôlé par lecture et par essai (commande factice dans mon bloc-notes, aucun code de la lecture lancé ; processus d'essai fini, aucun ne reste) :
- **Survie** : le processus lancé par `setsid nohup bash -c '…' &` est dans une session neuve et vit encore après la fin de l'appel qui l'a lancé : constaté.
- **Identifiant** : `$!`, écrit dans le `.pid`, est celui du processus de calcul lui-même (préfixe d'environnement et redirections compris) : constaté ; l'arrêt par `kill` sur cet identifiant vise donc le bon processus (règle R10).
- **Code** : `wait $!; echo $? > .code` écrit le code du processus de calcul (essai : 2 pour un processus fini en 2) : constaté.
- **Attente** : la boucle `until [ -f .code ]` avec double contrôle `kill -0` à une minute d'écart couvre le court intervalle entre la fin du processus et l'écriture du `.code` ; elle n'imprime que « FINI, code <n> » ou « PROCESSUS <n> ABSENT, SANS CODE » : aucun chiffre de sortie.
- **Une seule exécution** : garantie par le code lui-même pour la lecture une fois sa sortie écrite (`exiger_aucune_sortie`, ligne 2905 ; ligne `LECTURE-SONDES-IIB`, ligne 1518), et pour l'audit (`ecrire_resultat` refuse d'écraser) ; avant cela, par le verrou du journal : à rendre atomique et visible (V-2).
- **Aucun chiffre affiché** : sur la sortie standard, la commande `lecture` n'imprime que ses trois lignes (code, lignes 3059 à 3062 ; aucun autre `print` dans le code de la lecture ni dans le module des lectures descriptives) ; la réception n'est lue que par `head -n 1` ; `etats` n'imprime qu'une ligne ; le fichier des erreurs n'est lu qu'en cas de code non nul, à la ligne « REFUS » ou « ARRÊT : », à défaut à la dernière.
- **Arbre propre** : journal hors du dépôt, sorties de `nohup` envoyées à `/dev/null` : aucun fichier neuf dans l'arbre avant la lecture.

## Cloisonnement

Rien de neuf n'ouvre un interdit. Le contrôle du booléen n'imprime que « True » ou « False » et n'est pas une lecture à la main de la sortie. Le filtre de l'auditeur est inchangé. Les commandes d'inventaire n'impriment que tailles et empreintes. Les listes d'interdits sont harmonisées (`donnees/`, `diag/`, `runs/` hors des pièces nommées).

## Non vérifié par moi (hors de mes plages de lecture, pris sur la parole du rédacteur)

- Le lieu de la sixième réserve au texte scellé, « ligne 282 », et la phrase citée (« Elles sont exécutées par le code de la passe du côté exposé et attestées par la trace scellée, non observées : limite déclarée, que le verdict redit ») : la ligne 282 du texte scellé est hors des lignes 80 à 183 et 351 à 427 qui me sont permises. Si le renvoi était faux, le juge, qui lit le texte en entier, s'arrêterait (« si ce mandat et les textes scellés diffèrent ») : sans danger pour la lecture.
- L'ordre des champs de `champs_changes` dans la table neuve, que je n'ouvre pas : j'ai vérifié seulement que le code garde cet ordre pour chaque statut (lignes 2995 et 2996, puis `lignes_de_tete`, lignes 1993 à 2001).
- La ligne 6 du texte scellé (« Déclaration du mode de sabotage »), lue par le rédacteur.

## Ce que ce vérificateur a lu (pour le registre « qui a lu quoi »)

- En entier : les cinq pièces du tableau d'en-tête.
- `src/controle_ia/barreau8_moniteurs/lecture_sondes_v6.py` : lignes 1411, 1441, 2470 à 2472, 2493 à 2495, 2995 et 2996 ; recherche des lignes `print(` dans ce fichier et dans `lectures_descriptives_additif_1_v1.py` ; recherche de la ligne 2462 (en plus de ce que la contre-lecture avait déjà lu).
- Essais dans mon bloc-notes (`…/scratchpad/essai-detache/`) : commande factice `python3 -c` et `sleep`, deux sorties factices de même forme que la sortie de la lecture ; aucun fichier du dépôt modifié, aucun processus restant.
- `git log` des cinq derniers commits de la branche (titres), `git status`, `ls` et empreintes du dossier de la conductrice.
- **Non lus** : rien sous `diag/`, `donnees/`, `runs/`, `versement/`, `coffre/`, `docs/verdicts/` ; aucune pièce de la course, aucun ordre, aucune note d'interface ; ni la table neuve ni aucun registre sous `registres/` ; le texte scellé et les additifs hors des plages de la contre-lecture.
