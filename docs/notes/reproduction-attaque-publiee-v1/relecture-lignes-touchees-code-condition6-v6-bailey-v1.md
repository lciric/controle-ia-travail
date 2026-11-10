# Relecture des lignes touchées v5 → v6 du code de la condition 6 — témoin Bailey — v1

- Lecteur : R2, sous-agent neuf. Je n'ai écrit ni le texte scellé, ni le code, ni les essais, ni les rapports, ni les
  sondes du relecteur précédent. Date : `date -u` = Tue Nov 10 14:14:38 UTC 2026 (fin des sondes).
- Je reçois d'office le `CLAUDE.md` du dépôt (`b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae`).
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `fcf40b58`, arbre
  propre avant ce rapport ; `origin/main` = `617d77d4`.
- Pièces lues et empreintes (SHA-256, sur disque) :
  - texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`), l. 330-340, 362-374 ;
  - rapport appliqué : `relecture-lignes-touchees-code-condition6-v5-bailey-v1.md` (`228799935a747fc64cebac15d6443731857aaacb6550cbb57083e1f66f115971`), § 2 (M-1, M-2) et conclusion ;
  - code, par `diff -u` : `lecture_v5.py` (`f322f78a…`) → `lecture_v6.py` (`2c205e95d1f0b92d77b0a02fa0122a157293d507b3133744e6f957e81216fbcc`) ;
    `instance_v5.py` (`0d170bfa…`) → `instance_v6.py` (`93983898a172d458db4fd3c0f4da9448f256b2586cee48e73ba0ca7bc198147e`) ;
    `lanceur_v5.py` (`8efc7464…`) → `lanceur_v6.py` (`cf73d706cb0c85f53166ea5a0a8acb0beea53b929de8e7255e06ab1f169406f4`) ;
    contexte des lignes touchées : `lecture_v6.py` l. 81-210 et `valider`, `lire`, `audit` en entier ; `instance_v6.py`
    l. 370-415 (lecteur de sortie), `reconstituer_etat`, `main` ; `lanceur_v6.py` `_arreter_en_cours`, `_tours_relus`,
    `_executer`, `_finir` ; `journaliseur_v3.py` (`9f75407c…`) l. 62-71, 194-327 ; `execution_v3.py` (`279f1f4f…`) l. 63-73 ;
  - essais : `tests/test_temoin_bailey_condition6_v6.py` (`19ab2009491dbce5dad3b8662f78822df1fdfd7e20af406388f3c2606b78b6e5`), par `diff -u` avec `…_v5.py` (`b10770cb…`).
- Non lu : tout le reste du dépôt ; aucun des répertoires ou lignes cloisonnés ; aucun journal, aucune note, aucun
  résultat ; aucune clé ; aucune requête réseau ; pas de `vastai`.
- Outils : `diff -u`, `sed`, `grep`, `sha256sum` ; `pytest` (venv du dépôt). Essais v6 : **33 passés** (40 s), avec
  `TEMOIN_BAILEY_CLONE` du clone obfusqué. Sondes du relecteur précédent rejouées sur la v6
  (`…/scratchpad/c6-v6/test_sondes_r2_v5_sur_v6.py`, `9824d508…`) : M-1, M-2, M-2-bis **échouent** (défauts levés),
  M-1-bis, M-3, M-4, contrôle passent — conforme à l'annonce. Sondes neuves de ce relecteur :
  `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/diff-c6-v6/test_sondes_r2_v6.py`
  (`7f12d19e569bdb564e0c092cae06e9d68527eec70e63e48f5965a5ec4c208a6e`) : P1 à P5 **passent** (chaque sonde affirme un
  défaut : il est présent).

## 1. Verdict

**Non conforme en l'état : M-1 est corrigé ; M-2 ne l'est qu'en partie.** Quatre corrections, toutes dans
`lecture_v6.py` (et leur report sur l'instance), plus deux essais. Aucune ne touche le texte. Après elles : relecture des
seules lignes touchées et des sondes P1 à P5 inversées ; puis l'addendum, après le mot de Lazar sur les lectures à
acter, avec la lecture de la dernière ligne coupée (§ 3, Q-1).

## 2. M-1 — conforme

`_executer` (La l. 1046-1052) : sur `MORT`, si `_tours_relus` rend `None`, la phase entre dans `arretees` avec
« coupure de l'hôte » ; `_finir` (l. 1210-1212) la retente avant `_rapatrier`, comme les autres arrêtées. Vérifié :
- `setdefault` ne remplace pas une cause déjà notée (`_arreter_en_cours` n'est pas sur ce chemin : `_cmd` rend « mort »
  sans l'appeler) ; la cause « coupure de l'hôte » est dans la liste fermée de l'instance ;
- la condition `nom in self.manifestes_phase` de `_finir` tient (posée en tête de `_executer`) ;
- la retente ne peut pas écraser un état écrit par la première tentative dont la réponse se serait perdue :
  `reconstituer_etat` relit le fichier et rend « déjà présent » ;
- `tours_complets` reste `None` : aucune relance (inchangé, voulu) ; l'échec de la retente est consigné au bilan
  (`etats_reconstitues[phase] = None`), jamais levé ;
- inscrire la phase **seulement** en cas d'échec suffit : en cas de succès l'état existe déjà sur l'instance.
- La sonde comportementale M-1 du relecteur précédent échoue désormais (deux écritures demandées, la seconde dans
  `_finir`).

Réserve d'essai (correction E-1 ci-dessous) : `test_M1_execution_morte_inscrite_dans_arretees` ne lit que le **source**
(`inspect.getsource` et une sous-chaîne dans 250 caractères) ; il ne prouve pas le comportement, et casserait sur un
simple reformatage. Le rapport v5 demandait l'essai « M-1 inversée (deux écritures demandées, la seconde dans `_finir`) ».

## 3. M-2 — choix de lecture et défauts

### Q-1. La lecture choisie est-elle sûre (R4, R5) ?

Le choix : dernière ligne sans `\n` et illisible → ignorée et signalée ; toute autre ligne illisible → `GardeArret`.
C'est la bonne forme : le journaliseur écrit ligne par ligne avec `\n`, `flush`, `fsync` (`journaliseur_v3.py`
l. 62-65), donc seule la dernière ligne d'un fichier peut être coupée par une coupure ; une ligne illisible ailleurs, ou
une dernière ligne illisible **terminée**, n'est pas une coupure et fait tomber une garde (essai
`test_M2_ligne_illisible_au_milieu_ou_finie_leve`, juste). Une ligne complète sans `\n` final (coupure juste avant le
`\n`) est lue telle quelle : son contenu est entier, sans risque.

Mais « ignorée » n'est neutre que si la ligne perdue ne pouvait pas retirer un tour du compte. Ce n'est pas toujours
vrai pour les deux journaux de gardes :
- une garde qui tombe écrit sa ligne « tombée » puis lève (`_garde`, l. 197-203) : c'est **la dernière ligne** du
  journal des gardes, celle-là même qu'une coupure à cet instant tronque ;
- elle peut porter un tour déjà marqué : la garde « suite des étiquettes » tombe dans `_nouveau_tour` **avant**
  l'incrément (l. 305-309), donc avec `tour` = e, le tour précédent, dont la ligne « MARK » peut déjà être imprimée.
  Ligne entière : le tour e a `garde_tombee`, K′ = e. Ligne coupée et ignorée : le tour e est compté, K′ = e + 1. La
  lecture rend alors un tour **de plus** que n'en rendrait le journal intact : c'est rendre lisible ce que la ligne
  perdue aurait retiré (R5). L'audit rejoue la plupart des gardes sur les notes et le journal technique, mais pas
  celle-là sur ce tour ; la sûreté ne doit pas reposer sur lui.
- Dans `gardes-lanceur-v3.jsonl`, une ligne « tombée » vaut pour tous les tours (`lanceur_tombe`) ; ces lignes sont
  écrites au démarrage (tour −1, avant tout « MARK »), le risque y est théorique, mais la même règle le couvre.

Correction C-3 (prudente, vers moins de verdict, jamais plus) : une dernière ligne coupée dans le journal des gardes ou
dans les gardes du lanceur se lit comme une garde tombée au dernier tour présent dans `tours_journal`. Coût : au plus un
tour, et nul dans le cas ordinaire (coupure pendant un tour en cours, déjà incomplet). À écrire à l'addendum avec la
lecture elle-même : « une dernière ligne sans fin de ligne est ignorée et signalée ; dans un journal de gardes, elle
retire du compte le dernier tour présent ». Coupée dans un autre journal (notes, technique, durées, empreintes de
fichiers), l'ignorer ne peut qu'ôter une marque, une note ou une fin de tour : le tour en cause devient incomplet, ou
l'audit relève un défaut ; jamais de tour en plus.

### Défauts

**M-2a (à corriger, bloquant pour la correction M-2). Coupure au milieu d'un caractère multioctet : `UnicodeDecodeError`
hors `GardeArret`.** Le journaliseur écrit avec `ensure_ascii=False` ; « tombée », « passée », les messages portent des
`é`. Une coupure entre les deux octets d'un `é` fait lever `p.read_text(encoding="utf-8")` (Le l. 90) avant toute
analyse ligne à ligne : ni ignorée, ni `GardeArret`, et le défaut M-2 reste entier à l'instance (`reconstituer_etat`,
`main` n'attrapent que `GardeArret`) comme à la lecture (`valider`). Sonde P1. Correction C-1 : lire en octets
(`p.read_bytes()`), découper sur `b"\n"`, décoder **chaque ligne** en UTF-8 strict, et traiter
`(UnicodeDecodeError, json.JSONDecodeError)` par la même règle (dernière ligne sans `\n` : ignorée et signalée ; sinon
`GardeArret`). Essai : P1 inversée.

**M-2b (à corriger). Le signalement n'atteint ni le verdict ni le bilan.**
- `lire` (Le l. 567-588), qui rend le verdict, ne reporte pas `lignes_tronquees_ignorees` (ni au retour anticipé, ni au
  retour complet ; sonde P3) ; or c'est `lire` qui ouvre le journal des **notes**, le seul que `valider` ne lit pas.
- À l'instance, `reconstituer_etat` et `tours` (et l'état normal de `executer`, I l. 461) calculent `tours_complets`
  et `gardes_tombees` après avoir ignoré une ligne, sans le dire dans l'état écrit ni dans la ligne `ETAT` (sonde P5) :
  « jamais en silence » n'est tenu qu'au moment où la conduite relira le transfert.
- Le signalement ne porte que `p.name` (Le l. 101) : `gardes-v3.jsonl` du pilote, de la reprise, du principal, de la
  relance, de `transfert-1` ou `transfert-2` se confondent (sonde P4), et un même fichier lu deux fois est compté deux
  fois.
- Aucun programme de lecture n'appelle encore `valider`/`lire` (grep) : rien ne garantit que la clé arrive au rapport.
Correction C-2 : signaler le chemin relatif à la racine lue (`str(p)` suffit, la racine est connue), sans doublon ;
`lire` rend `lignes_tronquees_ignorees` = celles de `valider` plus les siennes ; `reconstituer_etat` et `executer`
écrivent `lignes_tronquees_ignorees` dans l'état et dans `ETAT` ; à l'addendum, la ligne : « toute ligne coupée
ignorée est rapportée avec le verdict, par fichier et par exécution ». Essais : une exécution transférée dont le
journal des gardes a une dernière ligne coupée → la clé de `valider` **et** de `lire` la nomme avec son exécution ;
`tours --ecrire-etat` sur un tel dossier → l'état écrit la porte.

**M-2c (à corriger). `LIGNES_TRONQUEES`, état global de module, aliasé dans le résultat.** `valider` place **la liste
du module elle-même** dans `out` (Le l. 291-292) : toute lecture ultérieure (`lire`, un autre `valider`) modifie après
coup un résultat déjà rendu, et un second `valider` l'efface (`clear()`, sonde P2). À l'instance, la liste n'est jamais
vidée et s'accumule dans le processus. Le risque concret : un bilan sérialisé après une seconde lecture (pilote puis
principal, essais successifs) qui ne dit plus, ou dit faux, ce qui a été ignoré. Correction C-4 : supprimer l'état
global ; `lire_jsonl(chemin, signal: list | None = None)` ajoute à la liste passée par l'appelant, et chaque
`tours_journal`, `gardes_tombees`, `valider`, `lire`, `reconstituer_etat` porte sa propre liste ; à défaut, au moins
une copie (`list(...)`) à chaque retour de `valider`. Essai : P2 inversée.

**E-2 (essai).** `test_M2_valider_rapporte_les_lignes_tronquees` n'éprouve que la présence de la clé sur un dossier
vide ; à remplacer par l'essai de C-2.

## 4. Corrections exactes

| N° | Où | Quoi | Essai |
|---|---|---|---|
| C-1 | `lecture_v6.lire_jsonl` | lire en octets, décoder ligne à ligne ; `UnicodeDecodeError` traitée comme `JSONDecodeError` | P1 inversée |
| C-2 | `lecture_v6.lire`, `instance_v6.reconstituer_etat`, `executer` | signalement porté par le verdict et par l'état ; chemin, sans doublon | `valider` + `lire` + `tours --ecrire-etat` sur un journal coupé |
| C-3 | `lecture_v6.tours_journal` | dernière ligne coupée d'un journal de gardes : garde tombée au dernier tour présent | « suite des étiquettes » coupée après MARK e → K′ = e |
| C-4 | `lecture_v6` | plus d'état global (liste passée par l'appelant), ou copie à chaque retour | P2 inversée |
| E-1 | essais | M-1 éprouvé par comportement (sonde M-1 du relecteur précédent, inversée), non par lecture du source | — |

À acter à l'addendum (après le mot de Lazar) : la lecture de la dernière ligne coupée (Q-1, avec C-3) et son
signalement avec le verdict (C-2).
