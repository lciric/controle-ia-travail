**Partie A : concordant sur le texte scellé.** `prereg/R1-addendum-relance-v3.md` au commit `139a81d3` (`88e262e2…`, égal à son compagnon) diffère du brouillon 2 qu'a lu notre concordance (`86c68b0e…`) exactement de la somme des deux patchs versés. C-1 à C-9 sont faits comme la concordance le demandait. Hors d'eux, il n'y a aucun changement de fond : seulement les trois ajouts annoncés (E16, ligne « Récupération », traitement de « Contre-lecture »), qui ne touchent ni une règle, ni une classe, ni un seuil. La commande de création du texte se transmet telle quelle, avec les valeurs de session-depot (§ A.6).

**Partie B : concordant sur le texte corrigé, non scellé.** `4c083453…` (commit `7bbc3f82`) diffère de `b5afc8b6…` exactement du patch versé. C-1 à C-8 sont faits, et rien d'autre ne change (C-9). Le texte permet les deux décisions du directeur, par un ajout chacune (§ B.3) :
- pour P-C6, à condition que « descriptive, non lue » porte sur « par les mêmes voies » seulement ;
- pour `episodes=`, le seuil est déjà écrit, mais la formule de projection manque : il faut l'écrire.

# Vérification des différences : addendum v3 de relance de R1 (scellé) et complément de validation (corrigé) — v1

- **Lecteur** : sous-agent neuf (Claude, Opus 5.5), règle R2. Je n'ai écrit ni l'addendum v3 de relance de R1, ni le complément de validation, ni leurs brouillons, ni leurs contre-lectures, ni nos deux concordances.
- **Date** : 3 novembre 2026, de 05:21 à environ 05:47 UTC (`date -u`).
- **Consigne** : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-differences-r1-complement-prompt.md`, `f8bd3998921b56c9522cc68c2468c00e1a6e7d54d6eb0f377cda1a618a463738` (conforme à son compagnon).
- **Récupération** : un seul `git fetch`, celui de la consigne, par refspec explicite (`prep/r1-relance-v3`, `prep/r1-complement-v1`), code 0. Ensuite, `git for-each-ref refs/remotes | grep -c donnees` = **0**.
- **Lecture** :
  - `git show`, `git diff` et `git log` sur le dépôt `/home/claude/controle-ia-travail` ;
  - `sha256sum`, `cmp` (comparaisons sans fichier intermédiaire), `grep`, `sed`, `awk` sur leurs sorties ;
  - lecture des pièces locales nommées par la consigne.
- **« l. »** : numéro de ligne de `git show <commit>:<chemin> | cat -n`.
- **Abréviations** :
  - « S » : le texte scellé de la partie A (`139a81d3`) ;
  - « T » : le texte corrigé de la partie B (`7bbc3f82`).

## A. Addendum v3 de relance de R1 (GO-2026-11-02-27)

### A.1 Pièces et empreintes (toutes recalculées)

| Pièce | Où | sha256 | Contrôle |
|---|---|---|---|
| S, texte scellé | `git show 139a81d3:prereg/R1-addendum-relance-v3.md` (573 l.) | `88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4` | égal à l'attendu ; compagnon au même commit égal |
| Brouillon 2 (lu par notre concordance) | `git show 49d29c8e:…` | `86c68b0ec323cfdce1a6a21d1fcee14ed8d0647f485906eb031e7ee6ac32746d` | égal |
| Brouillon 3 | `git show 6de29976:…` | `dcf51d015f4a195c7479b7ae504c06c2cb1154133a0e67759409eafdbb95e3d6` | égal à celui que S dit avoir relu (l. 569) |
| Patch 1 | `docs/notes/runs-r1-r2-r4-v1/relance-v3/corrections-apres-concordance-v1.patch` | `c1a4794dd4904b79c40446d20c19b31d018ef97c5fc75a1a3336f419b0b94830` | égal ; égal au compagnon |
| Tableau du patch 1 | `…/corrections-apres-concordance-v1.md` | `b3173f993a4836ad47c7b1f80cde484dc0d086d610cfd6599398f945bd07560e` | égal ; égal au compagnon |
| Patch 2 | `…/corrections-au-scellement-v1.patch` | `1366282bcb52c7dfdb06c7a2a946d128b073eb1ebf7e66b2e8b3c7829fe59144` | égal ; égal au compagnon |
| Note du patch 2 | `…/corrections-au-scellement-v1.md` | `e100c761f6360f99c9ec645a991029a05131405f6bb527ed43d1e6608e9977b7` | égal ; égal au compagnon |
| Notre concordance | `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v3-brouillon2-v1.md` | `8482b4cd39348104e80187b1470001f71fc6d857fc75344a32529b6dd37ade0b` | égal |
| Message n° 297 | `/home/claude/lectures/session-depot_2026-11-03_n297.md` | `5dc15fa28e17dc409f7a27e7964c2c4ad7895293ff656d7ae4ecb6ecf753c89f` | égal à l'empreinte que lui donne le n° 298 (l. 3) |
| Configuration v5, table v3, parent | au commit `139a81d3` | `acad6253…`, `ead8a668…`, `80c85a00…` | égaux ; compagnons égaux |
| Contrôles rejoués au scellement | `…/controles-avant-installation-au-scellement-v1.txt` au commit `04bc323a` | `8112f116d7efb8b42f58005b2c983144ac420ea9296f504f0e9b6bb233049ba4` | égal au compagnon. Il lit `88e262e2…` à la tête `139a81d3`. Le cas sain s'arrête en code 127 ; les six artefacts, en code 2. Il donne `prereg.problemes : []` |

- **Chaîne** : `49d29c8e` → `6de29976` → `139a81d3` → `04bc323a`, un parent chacun.
- **Code** : `git diff --stat f921fcec 139a81d3 -- src tests scripts` est vide.
- **Commit de scellement** : il ne porte que le texte et son compagnon, le compagnon de la configuration v5 (fichier inchangé), la note du scellement, son patch, et leurs compagnons.

### A.2 La différence est la somme exacte des deux patchs

- **Patch 1** : `git diff 49d29c8e 6de29976 -- prereg/R1-addendum-relance-v3.md` lui est identique à l'octet (`cmp` ; même sha256).
- **Patch 2** : `git diff 6de29976 139a81d3 -- …` lui est identique à l'octet.
- **Composition** : la chaîne est linéaire, donc `git diff 49d29c8e 139a81d3` est exactement la composition des deux patchs.
- **Décompte des lignes** :

  | Différence | Ajoutées | Retirées |
  |---|---|---|
  | Patch 1 | 84 | 37 |
  | Patch 2 | 10 | 2 |
  | Totale | 92 | 37 |

  Les deux lignes que retire le patch 2 avaient été ajoutées par le patch 1 : la fin de la ligne « Récupération » et le marqueur « À REMPLIR » du traitement final. D'où 84 + 10 − 2 = 92 et 37 + 2 − 2 = 37.
- **Relecture au mot près** : la différence totale compte 17 blocs. Relue avec `git diff --word-diff`, chacun de ses fragments relève d'une ligne du § A.3 ou du § A.4.

### A.3 C-1 à C-9 : chacun fait comme demandé

| Point | Demande (concordance, § 8) | S (lignes) | Vérifié contre |
|---|---|---|---|
| C-1 | Un seul moment ; recommandé : « avant la récupération » partout, fiche retirée des conditions de création, objet désigné | « Avant la récupération des sorties de la course par session-depot » à chaque endroit : E8 (d) et (e) l. 131 ; E18 l. 141 ; étape 1 l. 287-289 ; étape 3 l. 361-363 ; liste d'arrêt l. 475-480 (lancement) et l. 504-508 (« Récupération »). La citation du GO (l. 17-18) est inchangée : c'est sa lettre. Plus aucun « avant la création » ni « avant la lecture » ne vise la fiche ; les trois « avant la création » restants visent autre chose (une négation en E8, l'annonce d'une reprise en E21, les dépenses à revérifier). Objet désigné : « document de contrôles, distinct des fiches JSON de ses deux analyses scellées, écrites après le versement » (l. 131, 287-289, 504-506) | toutes les mentions de la fiche, relevées dans le brouillon 2 et dans S |
| C-2 | « G3 à G7, G9 et G10 » ; G8 resté dans la v2 (l. 172) | l. 153-155 | brouillon 1 de la v2 (`21a6e583`, `7915a3d6…`) : G8 à la l. 116 ; v2 scellée (`c2a8b6e1`, `9d17d640…`) : G8 à la l. 172 |
| C-3 | 91 épisodes par le budget d'étape (90 + 1), 2 par le budget d'épisode | l. 193-197, source « lignes 11, 69 et 201 » | verdict `64fab1a5…` (égal au compagnon). La l. 11 donne 90 non tentés et 3 coupés pendant leur repli ; la l. 69, l'épisode 56 coupé par l'échéance de l'étape ; la l. 201, deux au budget d'épisode et un à l'échéance de l'étape |
| C-4 | Nom de la fonction l. 134, docstring du fichier l. 4, assertion l. 173-177, `3d9237a5…`, « déclarés » | l. 162-171 | `tests/test_runs_nuit_v2.py` vaut `3d9237a5…` à `f921fcec` et à `139a81d3`, sans compagnon ; les l. 4, 134 et 173-177 sont celles citées. La citation de G10 est identique à la l. 118 du brouillon 1 de la v2 |
| C-5 | Nommer le paquet `controle_ia.analyse_principale_r1_r2`, branche `canal/conv-audit-n04` | E12, l. 135 | brouillon 1 de la v2, l. 114 (G6) : mêmes noms |
| C-6 | Une phrase sur les quatre engagements de la v2 (l. 179-181) | l. 177-181 | v2, l. 179-181 : table v3 citée, résultat scellé cité, configuration v5 sur la même table, concordance sur la différence avec le brouillon 3 de la v1 |
| C-7 | Branche source remplacée aux deux endroits de l'étape 7 (refspec l. 238, `R` l. 242), `-v2` après E21, `ae1ff089…` sans compagnon | E18 l. 141 ; étape 3 l. 364-370 | `procedure-relance-r1-v2.md` vaut `ae1ff089…` à `72f68fea` et à `139a81d3`, sans compagnon. Sa l. 238 est la refspec du `git fetch` ; sa l. 242, `R=…` ; sa l. 246, « rien à verser : arrêt » |
| C-8 | Lectures `etape=fidelite` et `etape=controle_negatif` de la course arrêtée rapportées ; un écart devient réserve d'instrument | E21, l. 144 | le module v3 écrit ces deux lignes (l. 395 et 405) |
| C-9 | « Ne lit pas le rejeu de R4 (fiche `R4` nulle ou `R4.activations` nul) » | l. 389-391 | notre script des fiches v1, l. 235 : `"R4": None` |

### A.4 Hors de C-1 à C-9

- **En-tête** (l. 3-9) : « brouillon 3 », date 00:23. Le § 9 de la concordance le permet (version, date).
- **E16** (l. 139) :
  - « champ `prereg` » devient « champ `preenregistrement` du manifeste de run (clés `chemin` et `sha256`, `src/controle_ia/manifeste.py` l. 104) ». C'est exact : la l. 96 construit `{"chemin", "sha256"}` et la l. 104 l'écrit sous `preenregistrement` ;
  - la phrase « la réserve tient […] sans effet sur toute lecture » reprend notre point 3 ;
  - il s'agit de forme et d'exactitude ; aucune règle ne change.
- **« Récupération »** (l. 506-508, patch 2) : session-depot apprend le scellement de notre fiche par notre message au canal (chemin, et empreinte vérifiée contre le compagnon) ; sans ce message, rien n'est récupéré. C'est la mise en œuvre de C-1 : un verrou, non un repli. Cela ne touche ni lecture, ni classe, ni seuil ; cela nous oblige (remarque 4 du § A.7).
- **« Contre-lecture »** (l. 531 et l. 545-573) :
  - « dans le brouillon 2 » ;
  - liste de nos corrections ;
  - traitement final rempli : brouillon 3 relu `dcf51d01…`, deux ajouts déclarés, « aucun refus », empreinte égale au compagnon.

  Tout y est exact.
- **Re-coupure** des l. 197-198 (réserve sur HG-2), sans aucun mot changé.
- **Rien d'autre** : la relecture au mot près de la différence totale le confirme.
- **Garde de forme**, refaite par lecture seule :
  - les huit sections que `prereg.problemes` exige (`SECTIONS`) sont présentes et non vides ;
  - il n'y a aucun « À REMPLIR » et aucun marqueur `<<…>>` ;
  - les quatre libellés lus par le script sont présents une fois chacun.

### A.5 Verdict A

**Concordant sur le texte scellé.** Raisons :
- la différence avec le brouillon 2 que nous avions lu est, à l'octet, la somme des deux patchs versés ;
- elle ne porte que sur C-1 à C-9, faits comme demandé, sur l'en-tête, et sur trois ajouts déclarés sans effet sur une règle, une classe ou un seuil (E16, ligne « Récupération », traitement de « Contre-lecture ») ;
- le code, la configuration et la table sont inchangés ;
- les contrôles d'avant l'installation ont été rejoués au commit de scellement.

### A.6 Commande de création

Chaque valeur que propose session-depot (n° 297, § 1, « Demande 2 ») est celle que S prescrit ou permet.

| Valeur proposée | Ce que dit S | Verdict |
|---|---|---|
| `COMMIT_SCELLEMENT=139a81d37fbd2255aff8d27698f84b47b9433221` | « commit de scellement de ce texte » (l. 327). Le commit qui pose le compagnon `88e262e2…` est `139a81d3…` (40 caractères, relus par `git log`) | prescrite |
| `VB=/opt/vastai-venv-v1/bin` | binaire « au chemin littéral `/opt/vastai-venv-v1/bin/vastai`, noté `$VB/vastai` » (l. 325-326) ; aucune version exigée | prescrite |
| `OFFRE` = la moins chère des offres conformes au filtre, au moment de la création | l. 332 : « OFFRE = la moins chère des offres conformes », recherche triée par `dph_total`. Sans offre conforme, rien n'est loué : nœud à Lazar (l. 395-396) | prescrite ; la lecture de 00:34 UTC (1,0933 USD de l'heure) est à refaire à la création |
| `GO_ID=GO-2026-11-02-27` | littérale (l. 335) ; E17 | prescrite |
| `--label r1-relance-v3` | littérale (l. 336) | prescrite |
| `BRANCHE=calcul/r1-relance-v3-reel-v1` | littérale (l. 337) ; E18 ; le script refuse une branche qui existe déjà | prescrite ; `-v2` seulement pour une reprise E21 |
| `PLAFOND_AMORCE_MIN=720`, `DELAI_REJEU_MIN=600` | littérales (l. 337) ; E9 | prescrites |

Les noms du bloc sont ceux que lit le code du commit lancé :
- l'amorce (`82f38687…`) lit `COMMIT`, `HF_TOKEN` et `GH_TOKEN` (exigés), puis `DEPOT_URL` et `PLAFOND_AMORCE_MIN` ;
- le script (`24744794…`) lit `BRANCHE`, `ETAPES` et `DELAI_REJEU_MIN`, et prend S comme préenregistrement par défaut (l. 47).

**Commande exacte à transmettre.** Rien n'y change. Les lignes 4-5 et 7-12 ci-dessous sont les l. 331-338 de S (`88e262e2…`), à l'octet. Les lignes 1-3 et 6 sont les seules ajoutées ; elles portent les valeurs que S prescrit (l. 325-327, et commentaire de la l. 332) :

```
cd /home/user/controle-ia-travail
VB=/opt/vastai-venv-v1/bin
COMMIT_SCELLEMENT=139a81d37fbd2255aff8d27698f84b47b9433221
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 datacenter=true reliability>=0.98 inet_down>=500 disk_space>=80 rentable=true dph_total<=1.40"
$VB/vastai search offers "$FILTRE" -o 'dph_total' --storage 80          # OFFRE = la moins chère des offres conformes
OFFRE=NNNNNNNN   # identifiant (colonne ID) de la première ligne de la recherche ci-dessus, lue au moment de la création ; aucune ligne : rien n'est loué, nœud à Lazar
$VB/vastai show instances                                                 # aucune instance oubliée
B64=$(git show "$COMMIT_SCELLEMENT:scripts/amorce_instance_r1_relance_v3.sh" | base64 -w0)
GO_ID=GO-2026-11-02-27 $VB/vastai create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label r1-relance-v3 \
    --env "-e COMMIT=$COMMIT_SCELLEMENT -e BRANCHE=calcul/r1-relance-v3-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e PLAFOND_AMORCE_MIN=720 -e DELAI_REJEU_MIN=600 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64 | base64 -d > /root/amorce.sh && ETAPES=rejeu bash /root/amorce.sh"
```

Sous la forme que propose session-depot : « commande exacte : bloc l. 330-339 du texte scellé `88e262e2…`, avec ces valeurs » (les siennes, inchangées).

**Conditions de S avant l'envoi de cette commande.** Elles ne changent pas la commande.
1. **Concordance consignée** : le rapport de concordance de conv-audit sur la version scellée doit être consigné par session-depot (chemin et empreinte) dans `docs/notes/runs-r1-r2-r4-v1/concordance-relance-v3-consignee-v1.md`, avec compagnon, et vérifié avant la commande (l. 281-284 et 475-478). Ce fichier, partie A, peut en tenir lieu une fois scellé par notre session. À `04bc323a`, ce fichier consigné n'existe pas encore.
2. **Ligne du GO** : le GO doit être valide le jour même, et la ligne GO-2026-11-02-27 doit figurer dans `registres/go.md` du dépôt d'où part la commande (l. 326).
   - Elle **manque** au commit `139a81d3`, car la branche a été tirée avant le GO.
   - Elle figure sur `origin/main` (`f38ae717`, l. 215 : 60 USD, échéance 2026-11-16, aucune révocation).
   - Il faut donc lancer depuis un arbre où elle figure (`main`), non depuis `prep/r1-relance-v3`.
3. **Dépenses** : les dépenses déjà engagées sous GO-27 sont à revérifier dans `registres/depenses.md` avant la création (l. 405-406). Il n'y en a aucune à `f38ae717`.
4. **Branche de résultats** : `calcul/r1-relance-v3-reel-v1` doit être absente du dépôt distant. Session-depot l'a vérifié ; le script le revérifie.
5. **Notre fiche de réception** : elle n'est pas une condition de la création (l. 287-289 et 479-480) ; elle l'est de la récupération (l. 504-508).

### A.7 Remarques (aucune condition)

1. **En-tête périmé.** S se dit encore « brouillon 3 (texte, non scellé) », et écrit « reste le traitement final […] puis le scellement » (l. 3-9).
   - Cela reste sans effet : le sceau, c'est le compagnon au commit `139a81d3`. Ni `prereg.problemes` ni les gardes du script ne lisent l'en-tête, et les contrôles rejoués au scellement sont conformes.
   - Il ne faut pas réécrire S (R12) ; le noter ici suffit.
2. **Empreintes du tableau du patch 1.** Le tableau cite, aux l. 12 et 148-149, un brouillon 3 `6035374f…` (565 l.) et un patch `00054c23…`.
   - Ce sont ceux du rédacteur, avant le complément E16 de session-depot (l. 152-154).
   - Les pièces versées sont `dcf51d01…` (citée par S, l. 569) et `c1a4794d…` (égal à `git diff`).
   - Sans effet.
3. **E16, « sans effet sur toute lecture ».** C'est exact pour nos deux analyses et pour notre script des fiches v1. Notre script v2 contrôlera `tokenisation.addendum` = `prereg/R1-addendum-relance-v2.md` comme provenance (R-3 de la concordance ; attente de S, l. 381-382). C'est un contrôle, non une lecture : c'est cohérent.
4. **Ce que nous devons pour la récupération** :
   - notre fiche scellée, avec son compagnon `.sha256`, à un chemin que session-depot peut lire ;
   - un message au canal qui en donne le chemin et l'empreinte.

   Sans ce message, rien n'est récupéré (l. 506-508) : c'est un blocage, jamais un repli.
5. **Refspec de l'étape 7.** À la l. 238 de la procédure, le nom de la branche source figure deux fois : source et destination de la refspec.
   - Les deux sont à remplacer, ainsi que `R` (l. 242).
   - Un remplacement partiel finit sur « rien à verser » (l. 246) : c'est un arrêt, sans repli silencieux.
6. **Garde de secours de session-depot** (n° 297 ; elle n'est pas dans S). Elle détruit l'instance à `T0 + 12 h 30`, soit 750 min.
   - Or le pire cas de S borne la vie de l'instance à 755 min : 720 min d'amorce, 5 min d'arrêt forcé, et au plus 30 min hors de l'amorce (l. 401-403).
   - Si l'image met plus de 25 min à démarrer, l'amorce peut encore tourner à 750 min. Ce serait une destruction sur une durée, ce que S exclut (l. 353).
   - Pour rester dans la règle « Arrêt » (l. 356-359), deux voies : poser la tâche à `T0 + 12 h 35` au plus tôt ; ou ne détruire à 12 h 30 que si le journal montre la ligne de fin de l'amorce, ou si l'instance ne répond plus.

## B. Complément de validation (GO-2026-11-02-30)

### B.1 Pièces et empreintes

| Pièce | Où | sha256 | Contrôle |
|---|---|---|---|
| T, texte corrigé | `git show 7bbc3f82:prereg/R1-addendum-relance-v2-complement-validation-v1.md` (698 l.) | `4c083453c4df6a922d16f4e6e299c31e14906c97afe9418d1f21c947dd4f53da` | égal ; sans compagnon (non scellé, comme annoncé) |
| Version lue par notre concordance | `git show c5293408:…` (587 l.) | `b5afc8b6e67622c04bebfee1315bb3e4602fe3e8c848d39344f8073d799e65ae` | égal |
| Patch | `docs/notes/runs-r1-r2-r4-v1/graine-complement-v1/corrections-apres-concordance-v1.patch` | `c93dfc355304ed05e348e847717faa3a1e5b1650d9ceaefd592b988681cb4713` | égal ; égal au compagnon |
| Tableau | `…/corrections-apres-concordance-v1.md` | `087f804311ad9559d409b04f2a643b08e03ef8592d0dfd629936855e44091781` | égal ; égal au compagnon. Il cite les bonnes empreintes : `b5afc8b6…`, `4c083453…`, `c93dfc35…` |
| Notre concordance | `brouillons/preuves-mentors-v1/complement-validation-rejeu-v1/concordance-complement-validation-v1.md` | `f4da389b80091dd6b3c4b511f270fe8243bcf2c68653afad04516c52b46a02c3` | égal |
| Message n° 298 | `/home/claude/lectures/session-depot_2026-11-03_n298.md` | `ebf37dc8a14dd9be403b962e22db996051a2506616399df0a41182f7a720413c` | aucune empreinte annoncée |

Le commit `7bbc3f82` a pour seul parent `c5293408`. Il ne porte que le texte, le patch, le tableau et leurs compagnons. `src`, `scripts` et `tests` y sont identiques à `c2a8b6e1` (cœur `resolution_graine_v1.py` : `cdc22b5a…`).

### B.2 Différence, C-1 à C-8, C-9

**Exactement le patch.** `git diff c5293408 7bbc3f82 -- <texte>` est identique au patch à l'octet : 12 blocs, 165 lignes ajoutées, 54 retirées, comme annoncé.

**C-1 à C-8, un par un** (lignes de T) :

| Point | Ce qui est écrit dans T |
|---|---|
| C-1 | (a) P-C7, passée de ≈ 24 h à ≈ 28 h, est déclarée : « Fusion » 17 (l. 621-623) et « Contre-lecture » (l. 673-675). (b) La clause de l'arbre gelé de `0e2a8871…` est remise (l. 30-32) et déclarée (« Fusion » 18, l. 624-626). (c) Le point 5 est rendu exact (l. 589-593). (d) « Une chose est perdue » : la sauvegarde des épisodes consignés à l'arrêt de dépense (l. 633-637). (e) `294a030c…` est dite version du rédacteur, et le patch mène à `b5afc8b6…` (l. 647-649) |
| C-2 | HC-2 est restreinte, pour les 7, aux empreintes, aux identifiants et au contrôle croisé (l. 166-170) ; « Fusion » 7 (l. 596-597) |
| C-3 | Chaque tâche ouvre une session neuve à chaque départ (l. 388-391). Armement (l. 417-431) : prompts sans identifiant avant la création ; aussitôt après, identifiant, `T0` et heure de destruction écrits, poussés et portés aux prompts ; second listing, qui vérifie aussi l'heure de départ de (ii) ; destruction immédiate si l'armement manque à 10 minutes ; destruction par l'identifiant du prompt seulement. Sans identifiant, sans `T0` ou sans prix au prompt, rien n'est détruit et une alerte part (l. 402-403 et 409). Journaux par `vastai logs <identifiant>`, masqués (l. 445-447) |
| C-4 | Quatre épreuves R5 des tâches (cas sain et artefact de chacune) et l'artefact de `merge-base` (`c2a8b6e1` → 1), consignés avant la création ; l'instance n'est créée qu'après (l. 295-297, 299-302, 381-385, 432-444). La dépense d'essai, recalculée, tient : de 16:42:40 à 18:13:07, à 1,187 USD de l'heure, ≈ 1,79 USD |
| C-5 | Filtre : lignes `AMORCE`, et de chaque ligne de progression l'heure, `etape=` et `episodes=` ; ni `resolus=`, ni `passes=`, ni `lecture=` (l. 445-451). L'alerte et la demande ne portent que la dépense, la durée de vie, le prix, l'heure de destruction et la durée du devis (l. 396-397). La décision d'extension ne dépend que de la dépense et de la durée (l. 450-451). Après une destruction, le journal relevé n'est lu pour aucun compte (l. 364, 367 et 451). Une destruction après la validation se lit « non éprouvé (dépense) », sans réserve sur la reproductibilité (l. 363-364) |
| C-6 | « Haut » est pris à la borne haute de la durée par épisode (≈ 9 difficiles). Le cas à ≈ 11 est chiffré : ≈ 34,5 h ; ≈ 48 USD au prix plafond et ≈ 41 USD à 1,187 USD de l'heure, au-delà de la destruction aux deux prix (l. 489 et 493-494). « Central » : ≈ 15 USD (≈ 13) pour 10,9 h (l. 488). P-C7 : « étape 0 seule » (l. 199). Recalculs : 34,5 × 1,40 = 48,3 ; 34,5 × 1,187 = 41,0 ; 10,9 × 1,40 = 15,3 ; 10,9 × 1,187 = 12,9 |
| C-7 | Enjeu : « au moins ≈ 258 à 305 USD, puis sans borne ». Mode commun des deux tâches : planificateur, compte et clé ; brief de reprise, § 9.1. Option (a) : le crédit borne tout le compte, qui est partagé (R-1051) ; d'où « aucune autre instance, ou un crédit égal à la somme des plafonds ». Recommandation inchangée (l. 502-524) |
| C-8 | Sur GO étendu : (ii) reportée à `T0 + H′` (même formule, sur `P′ − 0,5 USD`), seuils de (i) relevés (`P′ − 10` et `P′ − 0,5`), écrits et portés aux prompts (l. 410-413). La demande d'extension part dès que la durée projetée dépasse l'heure de destruction, à toute vérification, sans attendre 30 USD (l. 394-396 et 495-497). La partie facultative (disque compté comme prix horaire, frais de trafic) n'est pas reprise, ce qui est permis |

**C-9 : rien d'autre ne change.** Relue au mot près, la différence ne touche, hors de C-1 à C-8, que trois endroits :
- l'en-tête : « version corrigée […] non scellée », date (l. 4 et 9-11) ;
- la liste de « Contre-lecture » (l. 667-692) ;
- la phrase finale, mise d'accord avec l'ordre que fixe C-9 (l. 694-698).

Le marqueur « À REMPLIR » reste (l. 694), comme il se doit avant le scellement.

### B.3 Les deux décisions du directeur : ce que T permet, et les couples exacts

**P-C6, option (a).** T le permet sans autre changement, si la mention porte sur « par les mêmes voies » seulement.
- « mêmes voies » n'apparaît qu'une fois dans T (P-C6, l. 196).
- Rien ne lit cette part :
  - pour les 7, la métrique « résolution rejouée » ne compare que les empreintes, les identifiants et le contrôle croisé (l. 214) ;
  - HC-2 est restreinte de même (l. 166-170) ;
  - aucun critère ne lit la voie des 7 ; la ligne « voie, bascules… » vise les 54 (l. 361).
- Les autres parts de P-C6 sont lues par les critères des l. 362-365 : 7 sur 7, identifiants, contrôle croisé, table du sous-produit, lot, et les 3 de C-6. Dire P-C6 tout entière « descriptive, non lue » contredirait ces lignes, et il faudrait d'autres changements.

Couple (« ancien » : une seule occurrence, sur une seule ligne, l. 196) :

```json
{"ancien": "résolution 7 sur 7 par les mêmes voies, identifiants égaux au 2 novembre",
 "nouveau": "résolution 7 sur 7 par les mêmes voies (part descriptive, non lue : conséquence de C-2), identifiants égaux au 2 novembre"}
```

**`episodes=`.**

Ce que T contient déjà :
- un filtre qui ne garde que l'heure, `etape=` et `episodes=` (l. 447-449), sans `resolus=`, `passes=` ni `lecture=` ;
- une projection calculée « sur ces champs » seulement (l. 449 ; « sur l'heure et `episodes=` seulement », l. 495-496) ;
- le seuil : la durée de vie projetée dépasse l'heure de destruction de (ii), à toute vérification (l. 394-396 et 495-497) ;
- une alerte et une demande qui ne portent rien de ces champs (l. 396-397 et 450).

Ce qui manque : la **formule**, et l'application **mécanique**. Une phrase suffit. Elle n'utilise que l'heure et `episodes=`, comme le dit déjà « Coût et GO », et rien d'autre ne change dans T.

Sur quoi repose la formule :
- **Format des lignes**, au code cité (cœur `resolution_graine_v1.py`, `cdc22b5a…`, identique à `c2a8b6e1`) :
  - `PROGRES <heure> etape=validation episodes=147` au début de la boucle des épisodes (l. 1549) ;
  - puis `… episodes=k/147 resolus=… passes=…` tous les 10 épisodes et au dernier (l. 1574-1576).
- **Constante de 75 min**, tirée de « Coût et GO » (l. 482-483) : résolution rejouée ≈ 13 min 24 s, cibles et table ≈ 1 min, au plus une heure de vie après la fin de l'amorce. Cela fait 74 min 24 s, arrondies à 75 min.

Couple (« ancien » : une seule occurrence, l. 449) :

```json
{"ancien": "La durée de vie projetée de (i) ne se calcule que sur ces champs ;",
 "nouveau": "La durée de vie projetée de (i) ne se calcule que sur ces champs, par une règle écrite d'avance, portée au prompt de (i) et appliquée mécaniquement, sans autre lecture ni jugement, à chaque départ de (i) et à chaque reprise de la session de pilotage : `V0` = heure de la ligne `episodes=147` (début des épisodes de l'étape validation, cœur, l. 1549) ; `Vk` et `k` = heure et compte de la dernière ligne `episodes=k/147` (tous les 10 épisodes et au dernier, l. 1574-1576) ; fin de vie projetée `F = heure du départ + (147 − k) × (Vk − V0) / k + 75 min` (75 min : résolution rejouée ≈ 13 min 24 s, cibles et table ≈ 1 min, au plus une heure de vie après la fin de l'amorce, « Coût et GO ») ; avant la première ligne `episodes=k/147`, aucune projection ; après la ligne `episodes=147/147`, `F = heure du départ + 75 min` ; **seuil** : la demande d'extension part si et seulement si `F` dépasse l'heure de destruction de (ii) (`T0 + H`, ou `T0 + H′` après une extension) ; `resolus=` n'est jamais lu, ni pour `F` ni pour rien d'autre ;"}
```

La projection part de l'heure du départ, non de `Vk`, pour être prudente : un épisode long en cours la retarde au lieu de la masquer. Elle ne déclenche qu'une demande, jamais un arrêt.

**Déclarations, recommandées.** C-9 veut que la version scellée ne diffère de `b5afc8b6…` que par C-1 à C-8. Les deux ajouts relèvent de C-2 et de C-5 : il vaut mieux que la liste de « Contre-lecture » le dise. Chaque « ancien » n'a qu'une occurrence (l. 676 et l. 683) :

```json
{"ancien": "- C-2 : HC-2 restreinte, pour les 7,",
 "nouveau": "- C-2 (et sa conséquence, décision de Lazar relayée par conv-audit : à P-C6, « par les mêmes voies », part descriptive, non lue) : HC-2 restreinte, pour les 7,"}
{"ancien": "- C-5 : lecture aveugle : filtre des journaux ;",
 "nouveau": "- C-5 : lecture aveugle : filtre des journaux ; règle de la durée de vie projetée écrite d'avance (formule et seuil, sur l'heure et `episodes=` seulement), appliquée mécaniquement, `resolus=` jamais lu (condition de Lazar relayée par conv-audit) ;"}
```

### B.4 Verdict B

**Concordant sur le texte corrigé `4c083453…`.** Raisons :
- la différence avec `b5afc8b6…` est exactement le patch versé ;
- C-1 à C-8 sont faits ;
- rien d'autre ne change, hors de l'en-tête et de « Contre-lecture » (C-9).

Ensuite :
1. avant le scellement, ajouter les deux couples du § B.3, et de préférence les deux déclarations ;
2. la différence de `4c083453…` à la version scellée ne devra porter que sur ces ajouts, sur le marqueur « À REMPLIR » rempli et sur l'en-tête ;
3. cette différence se vérifie avant le lancement, comme le demande C-9.

### B.5 Remarque (aucune condition)

Supposons que la relance de R1 (GO-27) tourne encore quand le complément part, sous l'option (a) du nœud. Le crédit laissé devra alors couvrir les deux plafonds (40 + 60 USD) ; sinon, le complément attend la destruction de l'instance de R1. C'est la lettre de T (l. 517-518) ; à rappeler à Lazar avec le nœud.

## Annexe — commandes, écarts, ce que je n'ai pas fait

```
date -u
nice -n 10 git -C /home/claude/controle-ia-travail fetch -q --depth=60 origin +refs/heads/prep/r1-relance-v3:refs/remotes/origin/prep/r1-relance-v3 +refs/heads/prep/r1-complement-v1:refs/remotes/origin/prep/r1-complement-v1
git for-each-ref refs/remotes | grep -c donnees                       # 0
git log (filiation des deux branches) ; git show --stat <commits> ; git diff --name-only / --stat / --numstat / -U0 / --word-diff
git show <commit>:<chemin> | sha256sum | cmp | grep | sed | awk        # textes, patchs, notes, lignes de code citées, registres go.md et depenses.md
git diff --quiet c2a8b6e1 7bbc3f82 -- src scripts tests               # code 0
sha256sum (pièces locales) ; sha256sum -c (consigne)
```

- **Pièces locales lues** :
  - nos deux concordances, les messages n° 297 et n° 298 ;
  - le verdict `64fab1a5…`, trouvé par son compagnon sous `brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/` ;
  - la l. 235 de notre script des fiches v1 (`brouillons/preuves-mentors-v1/reception-r1-relance-v1/ecrire_fiches_reception_v1.py`), trouvé par `find` dans `brouillons/`.
- **Écarts, déclarés** :
  - plusieurs lectures brèves (`git show`, `grep`, `sed`) ont été lancées sans `nice -n 10` ; aucune ne faisait de calcul ;
  - `find`, `grep -r` et `ls` ont servi sur `brouillons/` et sur le dossier de ce rendu, hors des commandes `git` de la consigne ;
  - le `git fetch --depth=60` prescrit a écrit `.git/shallow` (7 bornes, 05:21 UTC). C'est un effet de la commande prescrite ; je ne l'ai pas touché.
- **Non fait** :
  - aucun fichier ouvert sous `diag/`, `runs/` ou `donnees/` ;
  - aucune branche `calcul/…` lue ;
  - aucun autre `git fetch`, aucun `checkout` ;
  - aucun commit, aucun `.sha256`, aucun fichier existant modifié ;
  - aucun appel de réseau hors du `git fetch` prescrit, aucun modèle, aucun `vastai` ;
  - aucun essai ni code Python lancé ;
  - `git ls-tree` n'a pas servi.
- **Seul fichier écrit** : celui-ci, sans compagnon ; il est à sceller par la session.
