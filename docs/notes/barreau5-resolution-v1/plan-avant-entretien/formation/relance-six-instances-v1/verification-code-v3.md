# Vérification des corrections du code des relances (barreau 5), commit d116bf78

Vérificateur : le contre-lecteur du code v2 (Opus 5.5), le 20 novembre 2026. Pièces lues :
- le rapport v3 ;
- l'additif v2 ;
- le différentiel `a74dfb49…` → `d116bf78bb2084b2d4f406535a6c6f0a23179efe` ;
- le registre propre de `origin/main` à jour (`f880e95d0`, sha256 `33ef7f6c…b49ffa`, cinq lignes à clé).

Je n'ai rien lu de `diag/`, des branches `donnees/`, d'aucun score ni d'aucun résultat. Je n'ai rien modifié au code et rien poussé.

## Verdict

**Conforme après ce couple** : un seul couple neuf, V-1. Il porte sur la procédure d'inscription et ne touche pas au code. Les six couples de la contre-lecture sont levés.

## Couples de la contre-lecture

| couple | levé ? | preuve |
|---|---|---|
| 1. La clé neuve casse le code de lecture figé (bloquant) | **levé** | Plus aucune clé neuve. `engagement_v1.py` a le blob `7d2b56368d…`, identique à l'octet à celui de `c76e7916…` (sha256 `565d4e51…536396` des deux côtés). Le commit des relances se lit dans la référence de la ligne de relance, par l'expression `_CODE_RELANCE_REF`. Il est exigé une seule fois, et différent du commit v1. Les mots « code des relances » doivent paraître une seule fois dans toute la référence. Aucune trace de `CODE-RELANCE-FORMATION-B5F` hors des essais qui prouvent son refus. |
| 2. Registre de course, arbre de la lecture (important) | **levé** | Les essais tournent sur le registre à cinq lignes plus la ligne de relance. L'additif v2 (§1, §4, C5) liste les cinq lignes inscrites. Il dit que le registre de course est égal à celui de `main` à l'octet, et que le code des relances n'entre pas dans l'arbre de la lecture. |
| 3. L'instance 6 citable (mineur) | **levé** | `INSTANCES_TOMBEES = (1, 2, 3, 4, 5, 7)`, avec refus « instance non tombée citée ». Les essais couvrent les cas sains et les artefacts. |
| 4. Filiation (mineur) | **levé** | `exiger_filiation_du_code_des_relances` est appelée à la commande et sur l'instance. Les essais couvrent la lignée correcte, l'ordre inversé, une autre lignée et un commit absent. L'aide d'essai du lanceur prend un commit v2 distinct. |
| 5. R12 (mineur) | **levé** | Exception écrite dans l'additif, en C5. Il reste à la consigner au registre des décisions (session mère). |
| 6. Plancher de l'amorce (mineur) | **levé** | `MIN_ESSAIS=244`. Je compte 244 essais dans le paquet, et l'essai d'égalité de l'amorce passe. |

## Points demandés

**2. `engagement_v1.py` est-il identique à celui de `CODE-LECTURE-B5F` ?** Oui, à l'octet. Même blob git `7d2b56368d5e1cc130b6bc2ad906cfd314065298` à `d116bf78` et à `c76e7916`. Même sha256 sur les fichiers extraits.

**3. Essais rejoués par moi.** Les sorties sont sous `$S/relance/verif-v3/`.
- **Paquet** (`tests/test_barreau5_familles_*.py`) au commit `d116bf78` : **244 passés, 0 échec**.
- **Lanceur et deux amorces** au commit `d116bf78` : **91 passés, 0 échec**.
- **Épreuve par retrait**, sur une extraction propre (`git archive`) de `31fca83b…`, avec les trois fichiers d'essais de `d116bf78` : **15 échecs, 1 erreur, 118 passés**. Les 16 sont exactement les essais neufs ou retouchés que nomme le rapport v3. L'erreur vient de `test_marche_reelle…`, dont le montage cherche une fonction absente du code v1.
- **Registre final** (`essai_registre_final.py`) : registre de `origin/main` à jour, plus la ligne de relance du rapport v3, § 7. La référence est remplie avec un chemin et une empreinte d'essai : 379 signes, ligne entière de 476 signes.
  - Lu par le **code de lecture figé** (`src` de `c76e7916` extrait) : six clés lues, relance `[1, 2, 3, 4, 5, 7]`, registre **accepté**. Artefact avec une ligne `CODE-RELANCE-FORMATION-B5F` : refusé.
  - Lu par le **code des relances** : relance `{GO-2026-11-19-86, [1,2,3,4,5,7], d116bf78…}`. Le commit v1 reste `ef800868…` et l'entropie reste celle de `CODE-FORMATION-B5F`. La filiation est vraie dans le dépôt de la session.
  - Artefacts refusés par le code des relances : mention absente ; mention en double ; mots « code des relances » répétés ailleurs dans la référence ; instance 6 ; autre accord.

**4. Le second appel de filiation, sur l'instance.**
- **Il est sûr.** Il ne fait qu'ajouter un refus, avant le manifeste et avant toute marche. Il ne peut rien admettre que la commande n'ait déjà admis.
- **Il fonctionne sur l'instance.** L'amorce clone avec `--filter=blob:none --single-branch --branch BRANCHE_CODE`, sans profondeur. Ce filtre retire les fichiers, pas les commits : tout l'historique de la branche est là. `git merge-base --is-ancestor` ne lit que des commits, et l'extraction partielle n'y change rien.
- **Le commit v1 y sera présent.** `ef800868…` est un ancêtre de `d116bf78…`, donc de tout commit de course qui en descend. Il est aussi déjà sur `origin`.
- Deux confirmations :
  - la marche de l'instance 6 a fait le même appel (`merge-base --is-ancestor <commit v1> HEAD`) dans un tel clone, et elle a fini ;
  - je l'ai rejoué sur un clone local à une seule branche (`formation-b5f/code-relance-v2`), avec extraction partielle de `src/` et du registre : filiation vraie. En local, le filtre des fichiers est ignoré par le serveur, mais il ne touche de toute façon pas les commits.
- **Seule condition** : la branche de course doit contenir `d116bf78` tel quel, sans réécriture ni écrasement de l'historique. Sinon, les deux appels refusent, et celui de la commande refuse d'abord, avant toute création.

**5. Plancher de l'amorce à 244.** Juste. Il égale le nombre d'essais du paquet (244 rejoués), et l'essai d'égalité de l'amorce passe parmi les 91.

**6. Autres régressions.** Aucune trouvée.
- Les nouvelles gardes ne vivent que dans le bloc de la ligne de relance et dans les branches `relance` de `executer` et `commande_de_creation`. Un registre sans ligne de relance se lit comme avant.
- Une première marche se compare toujours à `CODE-FORMATION-B5F`. Elle est refusée sous l'arbre des relances, ce qui est voulu : les premières marches sont finies.
- `depense_session` est inchangée pour les premières marches.
- Entropie, graines `-x1`, clé d'injection, coupures, branches de sortie et échéance d'arrêt : aucune ligne changée.
- Pour la lecture, rien ne change : `engagement_v1.py` est identique, aucune clé neuve, et le contenu de la ligne de relance est celui que lit le code figé.

## Couple neuf

**V-1. Important (procédure, pas de code) : contrôler la ligne avant de la commettre.**
- **Constat.** La ligne de relance ne se réécrit pas et ne se double pas. La garde de la référence est stricte : les mots « code des relances » ne doivent paraître qu'une fois, et la mention doit être bornée par « ; ». Une référence mal formée rendrait toute relance impossible sans nœud, et l'échéance est 07:30:16Z le 21. Par exemple, « vérification du code des relances <chemin> » ailleurs dans la référence suffirait. Le contrôle préalable n'est écrit que dans le rapport v3 (§ 7). L'additif v2 ne le demande pas.
- **Correction.** Écrire dans l'additif, en §4 point 2 ou en §5, au titre des devoirs de la session mère : « avant de commettre la ligne, le fichier du registre candidat est lu par `formation_v1.lire_code_et_accord` du code vérifié, qui doit rendre les instances 1,2,3,4,5,7 et le commit vérifié, et par `lecture_v1.relance_du_registre` du code figé à `CODE-LECTURE-B5F`, qui doit rendre [1,2,3,4,5,7] ; sinon la ligne n'est pas commise ». Le programme `$S/relance/essai_registre_final_v3.py` du développeur le fait déjà.

## Compte des essais rejoués

244 + 91 + 134 (épreuve par retrait : 15 échecs, 1 erreur, 118 passés) = **469**. S'y ajoutent l'essai du registre final (deux lecteurs, un cas sain chacun, six artefacts) et l'essai de filiation dans un clone à une seule branche avec extraction partielle.
