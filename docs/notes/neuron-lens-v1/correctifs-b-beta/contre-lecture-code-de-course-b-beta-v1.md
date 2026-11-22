# Contre-lecture du code de course de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, Llama 3.1 8B Instruct) — v1

**Verdict : « à corriger ».** 1 point bloquant, 6 majeurs, 16 mineurs. Aucun point ne fausse un seuil ni une valeur lue par le code
des verdicts ; le point bloquant est un versement incomplet, certain et irréparable après la destruction de la machine (P.6) ; les
majeurs sont un contrôle d'audit sans effet, un banc qui chronomètre aussi l'écriture du fichier, l'absence d'essai de Drowse avant
l'ajustement, une reprise qui écrit un verdict « chaîne en défaut » à tort, un temps réservé non appliqué à la fin de l'audit, et des
gardes câblées jamais essayées.

- **Lecteur** : sous-agent neuf (R2), modèle Fable 5.2 (`claude-fable-5-2`) ; n'a rien écrit du code lu. Date : 2026-11-18 (UTC).
- **Branche** : `claude/lentilles-b-beta-course-v1`. Le sommet annoncé était `61a3ff47` ; pendant la lecture, la session autrice a
  ajouté `41c7f2e8` (commande v1 en brouillon, `tests/test_neuron_lens_montage_b_beta_v1.py`) : ce commit ne change aucun des fichiers
  contre-lus (vérifié par `git diff --stat 61a3ff47 HEAD`). La commande v1 n'est **pas** contre-lue ici.
- **Empreintes des fichiers contre-lus** (16 premiers caractères) : `b_beta_lancer_v1.py` `9e77f46dc9ff06f2` ;
  `controles_b_beta_v1.py` `c8497dc90e524f7b` ; `addendum_partie2_b_beta_v1.py` `e7a05104a3002ac5` ;
  `amorce_neuron_lens_b_beta_v1.sh` `2049194a1d727422` ; `depot_reduit_neuron_lens_b_beta_v1.py` `731bc401caacdfaa` ;
  `requirements-neuron-lens-b-beta-v1.txt` `ca961910f935fc9a`.

## Fichiers lus

- Font foi : `texte-gele-tranche-b-beta-v1.md` (entier) ; `addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md` (entier).
- Contre-lus en entier : `src/controle_ia/neuron_lens/controles_b_beta_v1.py`, `b_beta_lancer_v1.py`,
  `addendum_partie2_b_beta_v1.py` ; `tests/test_neuron_lens_controles_b_beta_v1.py`, `tests/test_neuron_lens_b_beta_lancer_v1.py` ;
  `scripts/amorce_neuron_lens_b_beta_v1.sh` (et sa différence avec l'amorce v7) ; `scripts/depot_reduit_neuron_lens_b_beta_v1.py` ;
  `requirements-neuron-lens-b-beta-v1.txt`.
- Lus pour vérifier les appels (non contre-lus) : `verdicts_b_beta_v4.py` (entier), `grandeurs_b_alpha_v1.py` (l. 63-215),
  `controles_b0_v2.py` (l. 24-52), `manifeste.py`, `scellement.py`, `prereg.py` et `gardes.py` (fonctions appelées),
  `b_alpha_lancer_v5.py` (recherches), début de `tests/test_neuron_lens_verdicts_b_beta_v4.py` et de
  `tests/test_neuron_lens_montage_b_beta_v1.py`.
- Code voisin au commit `849bfe16`, lecture seule, jamais importé ni exécuté : `neuron_lens/{paths,corpus,lenses}.py`, `arch.py`
  (l. 149-151, 280-303), `catalog.py` (l. 32-48, 97-142, 183-186), `transport.py` (l. 1-130, 240-262) ; `scripts/01`, `02`, `04`,
  `05` (l. 52-92), `06` (l. 335-360, 600-640), `07` (l. 36-150), `checks/causal_lens.py` (l. 56-255, 340-385),
  `checks/reads_at_firings.py` (l. 56-82, 108-192, 255-295), `checks/lens_compare.py` (l. 40-80) ; correctifs
  `causal_lens-graine-v1.diff`, `lens_compare-llama-v2.diff` (entiers), `06_activations-llama-v2.diff` et
  `provenance-chat-llama-v1.diff` (recherches) ; noms des fonctions d'essai de `essai-transport-llama-miniature-v3.py`.
- Drowse 6.1.4, lecture seule, jamais importé : `METADATA`, `drowse/__init__.py`, `lens/store.py` (l. 40-70, 120-232, 362-460 par
  recherche, 539-800, 862-1064), `lens/jlens.py` (méthodes de `JacobianLens`), `lens/key.py`, `lens/sources.py` (imports,
  l. 450-462), `base/{source_registry,atomic,paths,shards}.py` (imports, `select`, `generation_path`) ; fermeture des imports
  calculée par analyse syntaxique (outil ci-dessous).
- **Non ouverts** : aucun fichier de résultats ; la série repère `diag/20261117-015632-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json`
  n'a été que listée (présence sur la branche), jamais lue ; rien sur les sujets interdits ; rien dans `registres/`.

## Ce qui a été exécuté

- Les trois fichiers d'essais demandés : d'abord **123 passés, 2 sautés** (torch absent : `test_points_fixes_et_a4`,
  `test_resume_fit_et_moyennes`), puis, torch 2.14.1 une fois installé, **125 passés, 0 sauté**. Sur la machine, l'amorce arrête au
  code 12 si un essai est sauté : les deux essais à torch passent ici, donc ce n'est pas un piège.
- Le dépôt réduit construit depuis `HEAD` dans le dossier de travail (77 fichiers) ; dans cet arbre : les six fichiers d'essais de
  l'amorce, **189 passés, 0 sauté**, arbre resté propre ; `exiger_prereg_scelle` du texte gelé, `verifier_pieces` (22 pièces) et
  `creer_manifeste(decisif=True, …)` passent (graine de la tâche « b-beta-intervalles-B-2 » : entropie 20261118).
- Une simulation de la fin de course avec les **vraies** fonctions `etape_declencheurs`, `etape_audit_relance`,
  `etape_audits_controles`, `etape_verdicts` et des fichiers factices tirés de la référence publiée de Qwen3-8B
  (`…/scratchpad/outils-contre-lecture/simulation_fin_de_course.py`, non versée) : cas sain → « reproduit avec nos lentilles » ;
  garde (a) → fichier « chaîne en défaut » écrit à l'étape des déclencheurs ; A1 avec temps épuisé → « non conclu » ; A2 avec des
  exports de moitiés aux **matrices d'empreintes identiques** → contrôle tenu à tort (majeur M-1). Le câblage vers le code des
  verdicts (clés, formes, booléens, JSON) est donc juste.
- Outil d'analyse des imports de Drowse (`…/scratchpad/outils-contre-lecture/imports_drowse.py`, non versé).

---

## Bloquant

### B-1 — Trois sorties exigées par P.6 ne sont pas versées, et ne pourront plus l'être après la destruction
Texte gelé, P.6 : « empreintes et résumé de `07_drivers.py` ; compte et rang du jeton de début dans les jetons gardés ; contrôles des
matrices (identité, égalité à `npR`, nombre de couches) […] Rien d'autre ne survit à la machine ».
1. `b_beta_lancer_v1.py` l. 998-999 (`etape_pilotes`) : `rglob("*drivers*")` filtré par `is_file()` ne retient que les fichiers dont
   le **nom** contient « drivers ». Or `07_drivers.py` (l. 139-148) écrit 32 tables `data/catalog/<modèle>/neurons/drivers/L00.parquet`
   … `L31.parquet` (`catalog.neuron_table`, l. 97-98) et une table `heads/drivers.parquet`. Le dossier `drivers` est écarté, ses 32
   fichiers ne correspondent pas au motif : seule la table des têtes est empreintée. Les 32 tables que `reads_at_firings.py` lit
   (l. 146) ne le sont pas. *Correction* : empreinter tout fichier de `data/catalog/<modèle>/` dont le chemin contient un
   composant `drivers` ou dont le nom contient « drivers » ; exiger 32 + 1 fichiers ; garder la fin du journal comme résumé.
2. l. 914-918 (`etape_comptes_jetons`) : le **compte** du jeton de début (128 000) dans le corpus d'activations
   (`counts[128000]` du fichier de `03_token_counts.py`) n'est pas relevé ; le « rang » relevé est la position de l'identifiant dans
   la liste triée par identifiant, qui ne dit rien. Le fichier des comptes n'est pas versé. *Correction* : relever
   `counts[128000]` et le rang par compte décroissant parmi les jetons gardés (dire la règle d'égalité), et les écrire aussi en
   partie 2.
3. l. 871-872 (`etape_export`) : le résultat ne garde que les empreintes des exports et la liste des couches. Les valeurs des
   contrôles (écart maximal à l'identité par couche 0 à 27 ; écart maximal à `npR` par couche ; écart relatif de l'aller-retour par
   couche et par export) ne sont écrites nulle part : le lecteur neuf (P.7) n'aura que « l'étape a rendu un résultat ». De même les
   contrôles de B0 des trois lentilles de Neuronpedia (l. 649-653) ne rendent que des listes de problèmes. *Correction* : faire rendre
   ces valeurs par les gardes (ou les calculer à côté) et les écrire au résultat de l'étape.

Aucune de ces trois sorties n'entre dans un verdict ; mais l'écart à P.6 est certain, et le lieu L1 le rend définitif.

---

## Majeurs

### M-1 — Audits A2 et A3 : le contrôle « exports des moitiés d'empreintes différentes » ne peut pas échouer
`b_beta_lancer_v1.py` l. 1191 (`emp_moities = {k: json.dumps(ex[k], sort_keys=True) …}`), avec `_empreintes_home` l. 836-837 et
`controles_a2_a3` (`controles_b_beta_v1.py` l. 382). `ex[k]` est le dictionnaire {chemin relatif : empreinte} de **tout** le dossier
d'export. Or Drowse 6.1.4 nomme chaque fichier de matrice avec un identifiant tiré au hasard
(`base/shards.py` l. 32-41 : `…layer-<l>.gen-<uuid4>.safetensors`) et écrit ces noms dans `manifest.json`
(`store.py` l. 720-735) : deux exports ont toujours des chemins et un manifeste différents, même si leurs matrices sont identiques
octet pour octet. La simulation l'a montré (matrices d'empreintes égales, contrôle tenu). La garde (o) couvre en amont le cas
« même moitié exportée deux fois » (chaque export comparé à la moyenne de sa moitié), ce qui borne le risque ; le contrôle de l'audit
n'en est pas moins sans effet. *Correction* : lire `manifest.json` de chaque export, en tirer pour chaque (cible, couche) le nom du
fichier, comparer les **empreintes des fichiers de matrices** couche par couche, et exiger qu'elles diffèrent (au moins à chaque
couche de la cible `out`) ; essai avec deux exports factices de mêmes matrices sous des noms différents.

### M-2 — Banc : le temps du second document contient l'écriture du fichier d'ajustement
`b_beta_lancer_v1.py` l. 787-794 (`--docs 2`, second temps lu) ; code voisin `02_fit.py` l. 179-184 : pour le **dernier** document,
`save()` est appelé **avant** l'impression de « doc i/n … in X s ». Avec deux documents, le second est le dernier : son temps
comprend la copie vers le processeur et l'écriture d'environ 8,4 Gio (lentille R : (31 + 32) × 4 096² × 4 octets × 2 moitiés ; 8,6
pour S). Selon le disque, cela ajoute de l'ordre de 5 à 40 s à un temps attendu vers 11,5 s : compte rendu quasi certain (14,2 s),
arrêt à tort plausible (23,6 s). L'erreur va dans le sens sévère (jamais un départ à tort), mais la règle du banc ne mesure pas ce
que le texte nomme (« le second chronométré »). Le temps est en outre lu à une décimale (23,64 s imprimé « 23.6 » ne s'arrête pas).
*Correction, à trancher par la mère* (le texte dit « deux documents par lentille » ; la vérification du brouillon 3, n-6, renvoie la
manière de jouer le banc à la commande) : (a) banc à trois documents, temps du **deuxième** lu (`m.group(2) == "3"`, `temps[1]`),
déclaré dans la commande ; ou (b) garder deux documents et déclarer que le temps contient l'écriture, en acceptant le risque
d'arrêt à tort. Recommandation : (a).

### M-3 — Aucun essai de Drowse avant l'ajustement, alors que l'en-tête en annonce un
`b_beta_lancer_v1.py` l. 17-19 (« l'essai de chargement de Drowse […] tranche sur la machine »), l. 656-663 (`_drowse` : version
lue dans la métadonnée et empreinte de la roue, **aucun import**), l. 666-700 (`etape_b0`) ; amorce l. 240-243 (installation seule).
Aucun essai de B0 n'importe Drowse. Le premier import a lieu dans `04_export_rlens.py`, après les deux ajustements (8 à 15 h
payées) : un import en échec y donne un arrêt simple, les ajustements sont perdus (lieu L1). *Correction* : à B0, (1) un processus
enfant, hors ligne, sans clé, qui importe exactement ce que le code voisin emploie —
`from drowse.lens.store import LensProvenance, load_local_lens, save_lens`, `from drowse.lens.jlens import JacobianLens`,
`from drowse.lens.key import LensKey`, `import drowse.lens.sources` — échec = arrêt avant l'ajustement ; (2) mieux, après le banc et
dans la copie à part : `04_export_rlens.py` sur le fichier d'ajustement de deux documents du banc (il a un document par moitié),
puis `load_lens` et la garde (o) sur cet export — l'aller-retour entier, à la taille réelle, essayé avant de payer. (2) ajoute un
arrêt dans le sens sévère : à déclarer dans la commande. Voir aussi la déclaration de forme, plus bas.

### M-4 — Reprise de l'export après une relance de la machine : verdict « chaîne en défaut » écrit à tort
`b_beta_lancer_v1.py` l. 848-853 : `if not home.exists()` saute l'export si le dossier existe. Une machine relancée pendant
`04_export_rlens.py` laisse un dossier sans `manifest.json` (Drowse l'écrit en dernier, `store.py` l. 772-780) ; à la reprise,
l'export n'est pas refait, `load_local_lens` rend `None`, le voisin lève `FileNotFoundError`, la garde (o) se déclenche et le lanceur
écrit le **fichier de verdicts unique** « chaîne en défaut » : la course est finie, sur une simple relance. *Correction* : décider
par la présence du manifeste (`<home>/**/local/r/manifest.json`) ; sans manifeste et sans résultat d'étape, supprimer le dossier
partiel et refaire l'export (consigné au résultat). Même famille, moins grave (arrêt sans verdict, ou fenêtre de quelques
secondes) : points m-1 à m-3.

### M-5 — Temps réservé d'une heure : non appliqué à la fin de l'audit de relance, ni aux audits de contrôle
`b_beta_lancer_v1.py` l. 1164-1180. Le délai borne `measure` et `score` à la graine 1, mais `_grandeurs(ctx, 1, …)` (l. 1178 ;
échéance attendue 0,2 à 0,5 h, l. 143), qui produit le n exigé par le code des verdicts, tourne sans borne et sans contrôle après
coup ; `etape_audits_controles` (l. 1183) ne lit pas le temps restant. Un audit peut donc finir après l'heure et être compté
« joué », quand le texte dit « non joué » (« Critères de lecture gelés », fin : « si le temps réservé (1 h) […] empêche de finir un
audit, son issue est « non joué » »), ce qui peut changer le verdict d'ensemble (« non conclu » contre un verdict de mesure).
*Correction* : relire `_temps_restant` après les grandeurs de la graine 1 et au début (et à la fin) de `etape_audits_controles` ;
dépassé = « non joué » ; jouer les audits de contrôle (quelques secondes) **avant** la relance (ordre de `ETAPES`, l. 133-134), pour
qu'une relance longue ne les prive pas de leur issue ; essais avec l'horloge remplaçable.

### M-6 — R5 : les gardes telles que câblées dans les étapes ne sont essayées nulle part
`tests/test_neuron_lens_b_beta_lancer_v1.py` l. 83-93 : toutes les fonctions d'étape sont remplacées par des doubles. Les fonctions
pures de `controles_b_beta_v1` sont essayées (cas sain et artefact), mais jamais leur câblage : « premier lancement » décidé par
l'absence du journal et garde (q) (l. 803-811) ; contrôle que le banc n'a rien écrit dans l'arbre de la course (l. 795-796) et lecture
du journal du banc ; détection des fichiers antérieurs de la garde (s) et pose des liens durs avec la garde (k) (l. 1083-1096) ;
gardes (e), (h), (n), (o) dans `etape_export` ; garde (p) avant les pilotes ; `problemes_gardes`, `entrees`, `etape_declencheurs`,
`etape_audit_relance` (temps réservé, « non joué »), `etape_audits_controles`, `etape_verdicts` (intervalles compris) ; `_drowse`
n'est essayé que dans le fichier neuf `test_neuron_lens_montage_b_beta_v1.py`, absent du dépôt réduit et de la liste de l'amorce.
Les défauts B-1 (1), M-1 et M-4 auraient été vus par de tels essais. *Correction* : un essai de bout en bout sur dépôt jouet, avec
`ctx.executer` et `ctx.voisin_py` remplacés (ils sont faits pour cela) et de petits fichiers d'ajustement factices écrits par torch :
cas sain jusqu'au fichier de verdicts, puis un artefact par garde câblée (fichier `-T128` présent au premier lancement, point de
sauvegarde altéré à la relance, fichier `reads_at_firings-…pt` présent, `arch.fits` rendant `hub` avant les lectures, lien d'une autre
empreinte, export rendant `None` à une couche, matrice identité, 3 documents de pilotes, 15 contextes, temps épuisé). Ajouter ce
fichier et celui des gardes du montage aux essais de l'amorce et au dépôt réduit (avec `garde_depense_v4.py` s'il reste importé).

---

## Mineurs

- **m-1** `b_beta_lancer_v1.py` l. 907-909 : si la machine est relancée après la fin de `03_token_counts.py` et avant l'écriture du
  résultat, la reprise s'arrête pour toujours (« fichier de comptes déjà présent »). Conforme à « une seule fois », mais sans
  issue : décider par le journal (premier lancement) et, à la reprise, arrêter avec un message qui nomme la relance.
- **m-2** l. 787-793 : même chose pour le banc : à la reprise, le fichier de deux documents existe dans la copie à part, `02_fit.py`
  reprend à `next_doc = 2`, ne chronomètre rien, « banc en échec ». Supprimer les fichiers `-T128` de la copie du banc au début de
  l'étape (ils n'ont pas d'autre usage ; 17 Gio de disque rendus, voir m-16).
- **m-3** l. 1087-1090 : garde (s) à la reprise : si la machine est relancée entre l'écriture des sorties de `reads_at_firings.py`
  (l. 288-291 du voisin, tout à la fin) et le résultat de l'étape, la reprise écrit « chaîne en défaut (s) » pour des fichiers de
  cette même course. Fenêtre de quelques secondes. Ne juger (s) qu'au premier lancement (journal absent) ; à la reprise, arrêt
  simple. Et suivre la lettre du texte pour le motif : `data/checks/reads_at_firings-*.pt` (le code ne regarde que le nom de Llama ;
  suffisant en fait, le voisin ne fusionne que ce nom ; ne pas élargir le résumé, le dépôt voisin suit des résumés d'autres modèles).
- **m-4** l. 131-134 : les gardes (a) à (c), (e) et (j) sur la sortie de `score` ne sont jugées qu'à l'étape des déclencheurs, après
  `reads_at_firings.py` ; P.3, étape 5, les place avant l'étape 6. Aucun résultat faussé (rien n'est lu), jusqu'à une heure payée pour
  une course déjà en défaut. Appeler `defauts_score` et `defaut_j` à la fin de l'étape des grandeurs.
- **m-5** l. 1098 : `--device cuda` ajouté à `reads_at_firings.py --parts neurons` ; P.2 ne l'écrit pas. Sans effet (le défaut est déjà
  `cuda` hors Mac) ; le retirer ou le déclarer. `--ctx-batch 64` (l. 1013) est le défaut publié, écrit par M.1 : conforme.
- **m-6** l. 985-986 : le message du correctif (1) est cherché dans **tout** le journal de la passe ; après une relance, un message
  d'un premier essai suffit. Chercher dans le dernier segment (comme le banc, l. 790).
- **m-7** `controles_b_beta_v1.py` l. 171-184 et lanceur l. 469 : la différence entre moitiés est une recopie en numpy (float32) de
  `Accumulator.split_half` (torch) : même formule, mêmes types, valeurs égales à l'arrondi du flottant près (ordre des sommes
  différent), non au bit. Sans effet sur les seuils (0,10 ; 0,20 ; 10⁻⁶ en absolu). `resume_fit` a torch sous la main : y calculer
  aussi l'expression du dépôt mot pour mot et verser les deux. Conforme pour le reste : non arrondie, `nan` si une moitié est vide,
  cibles et nombres de couches (31, 32, 32, 32).
- **m-8** lanceur l. 512-513 et l. 680-681 : l'empreinte du code des verdicts (`8c07434f…`) et de ses essais (`1b63c8cb…`), fixées
  par l'addendum partie 1, § 4, sont relevées mais non comparées, et le nombre de tests (82) n'est pas exigé. Les valeurs présentes
  sont les bonnes (vérifié : `8c07434f…`, `1b63c8cb…`, 82 passés). Les ajouter aux pièces empreintées et exiger 82.
- **m-9** l. 729 (et l. 409) : à l'étape du corpus d'ajustement, en ligne et sans clé, le tokeniseur du dépôt sous licence est chargé
  **dans le processus du lanceur** ; cela repose sur le repli de la bibliothèque sur le cache. `05_act_corpus.py` fait de même et a
  tourné ainsi dans la tranche précédente. Plus sûr : poser `HF_HUB_OFFLINE=1` dans le processus après `01_lens_corpus.py`, avant le
  premier import (rien n'a encore importé la bibliothèque à ce moment de l'étape).
- **m-10** l. 1073-1074 et 1179-1180 : les contrôles (1) et (2) des audits A1 et A5 ne portent que sur la graine 0 ; ceux de la
  graine 1, déjà calculés (`g1`), ne sont pas joints. Contrôle (2) : « dose > 0 » (dose arrondie à 6 décimales), la norme de la
  colonne d'écriture n'est pas lue ; lecture raisonnable, à déclarer.
- **m-11** l. 867-868 : la clause « deux fichiers d'empreinte égale » de la garde (n) compare un fichier `.pt` de Neuronpedia à des
  fichiers `safetensors` d'une couche : elle ne peut pas se déclencher. La comparaison des matrices fait le travail ; le dire.
- **m-12** `controles_b_beta_v1.py` l. 482-491 : le nombre de pôles écrit par le correctif (4) (`rows`) n'est pas exigé égal à
  28 672 (M.2). L'exiger.
- **m-13** lanceur l. 1229-1237 : une erreur dans le calcul des intervalles (rapportés, sans critère) empêche l'écriture du fichier
  de verdicts, déjà calculé. Écrire le verdict d'abord, les intervalles dans un second fichier scellé ; ou attraper l'erreur,
  l'écrire dans le fichier, sans jamais toucher au verdict. L. 1156 : les motifs sont rangés sous la clé « score » au lieu des
  lettres des gardes (forme).
- **m-14** l. 1126-1136 : `problemes_gardes` dit « recomptées » ; seules (d), (f), (i) et l'identité sont relues, les autres
  lettres sont posées « tenues » parce que l'étape qui les porte a rendu un résultat. Juste (une garde manquée arrête), mais à dire
  tel quel, et lier chaque lettre au résultat d'étape qui la prouve.
- **m-15** `requirements-neuron-lens-b-beta-v1.txt` : PyYAML absent de la liste alors que Drowse l'importe (voir plus bas) ; `pytest`
  sans version. Amorce : la version de python (3.12.16 exigée par l'addendum, § 5) n'est comparée qu'à l'étape de la partie 2,
  après une heure de montage ; la lire avant `pip`.
- **m-16** mémoire et disque, à dimensionner dans la commande : `score`, les grandeurs par pôle et `lens_compare.py` chargent chacun
  les lentilles notées en mémoire (trois exports de Drowse, cibles `out` et `mid`, plus la fusion du voisin : de l'ordre de 8 Gio
  chacun ; trois lentilles de Neuronpedia) — compter 32 à 48 Gio de mémoire vive ; `reads_at_firings.py` charge deux fois chaque
  fichier d'ajustement (≈ 8,5 Gio) sans projection ; disque : 17 Gio d'ajustements, 17 Gio dans la copie du banc, 8,5 Gio de fichier
  temporaire à chaque sauvegarde, ≈ 13 Gio d'exports, poids, activations. L'export pourrait suivre l'ajustement de R, avant celui de
  S (le texte le permet : « à la fin de chaque ajustement […] → export ») : une garde (o) manquée coûterait 4 à 7 h de moins.

---

## Conformité vérifiée, point par point (sans défaut sauf renvoi)

| point | constat |
|---|---|
| ordre de P.3 | `ETAPES` suit les étapes 1 à 7 ; `lens_compare.py` après les comptes de jetons et la partie 2 ; fumée puis passe ; pilotes ; `measure`, `score` ; liens durs puis lectures ; `08_reads.py` non joué. Écart d'ordre : m-4. |
| arguments de P.2 | `01 --docs 1000 --revision 2fa015e4…` ; `02 --lens R\|S --model … --docs 1000 --seq-len 128 --full-length --save-minutes 60` (jamais `--shard`) ; `04 <fit R> --name dclm-llama`, puis `--half 0`, `--half 1` ; `05 --docs dclm=40000,zh=8000,code=8000,chat=8000` ; `lens_compare --lenses R:dclm-llama-even,R:dclm-llama-odd,npR --layers 2,7,12,18,23,28 --samples 0` (+ `--json` du correctif (4)) ; `score --lenses logit,J,npJpp,npR,R:dclm-llama,R:dclm-llama-even,R:dclm-llama-odd --tag b-beta` ; `reads_at_firings --parts neurons` (m-5) ; `NEURON_LENS_MODEL` posé pour tout enfant. |
| P.1 | `lens_docs(…, 1000, 128, SKIP_FIRST + 2, True)` et `rows_sha256` du voisin, mêmes arguments que `02_fit.py` l. 132 ; 932, 466/466, `a6afd972…`, empreintes des moitiés ; écart = arrêt avant l'ajustement. |
| (d), (f) | six essais empreintés avec leur nombre de tests, essais du dépôt sur le Qwen3 miniature, essai des crochets ; « sauté » et « échec » vus ; deux artefacts joués sur des copies (motifs uniques, vérifié) ; fumée. L'artefact « signe » inverse l'estimation dans l'assertion, non un terme de l'estimateur : à dire. Accès au tokeniseur : étape à part, arrêt simple (conforme). |
| (e), (n) | identité à 10⁻⁶ en float32, couches 0 à 27 : à B0 pour les trois fichiers de Neuronpedia (31 couches contiguës), après l'export et avant `score` pour notre R ; égalité à `npR` au même moment. Part « score » de (e) : code des verdicts. |
| (g), (h) | à la fin de chaque ajustement : 466/466, `next_doc` = `docs` = 932, longueurs, `rows_sha256`, `full_length`, différences et sommes finies ; 31 et 32 couches pour R, 32 et 32 pour S ; 31 couches `out` exportées. |
| (i) | trois moments : après `01` (provenance contre les deux publiées, lues par `git show HEAD:` et empreintées) ; après `05` (provenance réécrite égale à la publiée, identifiants, textes entiers des 932 documents contre les 40 000) ; de nouveau avant `measure`. Clés comparées présentes dans les provenances publiées (vérifié). |
| (k) | `arch.fits` appelé dans le même environnement juste avant la fumée, la passe, les pilotes (`hub` exigé) ; message du correctif (1) exigé au journal de la passe (m-6) ; liens durs posés **seulement** à l'étape des lectures, empreintes égales à celles de la fin d'ajustement, nos deux noms exigés. |
| (o) | trois exports ; erreur ou `None` à une couche 0 à 30 ; écart relatif de Frobenius à 10⁻³ contre `Accumulator.mean` recopié (entière, paire, impaire) ; avant `lens_compare.py` et `score`. Un `nan` est pris. |
| (p) | `meta["contexts"]` = 16 après `measure` ; 4, 2, 2 documents recomptés par l'expression de `07_drivers.py` l. 56 avant les pilotes. |
| (q) | copie à part pour le banc (dossier `data/fits` distinct, contrôlé) ; aucun fichier `-T128` au premier lancement ; point de sauvegarde relu avant toute relance. Non essayé câblé : M-6. |
| (r) | empreinte de `kept()` exigée avant la fumée, la passe, `lens_compare.py`, `07_drivers.py`, `reads_at_firings.py`. |
| (s) | avant `reads_at_firings.py` : m-3. |
| n recalculé | `grandeurs_b_alpha_v1` (règle de `score`), fidélité au JSON de `score` exigée ; pôles écartés par motif versés. |
| audits | A1/A5 : une seule relance, `--seed 1`, lentilles `logit,npR,R:dclm-llama`, étiquette `b-beta-graine1`, même résultat donné aux deux audits ; « non joué » sur délai (M-5 pour la fin) ; A2/A3 : M-1 pour les exports, le reste conforme ; A4 : permutation recalculée comme `reads_at_firings.py` l. 133 et 149 (un générateur à la graine 0, deux tirages par couche, aucun autre tirage entre), au plus 10 points fixes, fichier de S lu égal à l'ajustement ; A6 : dans le code des verdicts. |
| intervalles | 2 000 tirages ; `SeedSequence(20261118)` avec une clé par tâche (convention du manifeste du dépôt, non `spawn()` dans l'ordre) ; cinq tâches dans l'ordre B-2, B-3, B-4, B-6, B-7 ; pôles tirés au hasard et retenus, appariés pour une différence ; rapportés seulement. |
| fichier de verdicts | unique, jamais écrasé ; toute chaîne en défaut l'écrit puis arrête ; `suite` rend « fin » ensuite. |
| addendum partie 1 | empreintes du modèle (10 fichiers), des trois lentilles, des provenances, des correctifs et essais, du code voisin avant et après ; versions comparées à B0 (écart = arrêt avant l'ajustement) ; Drowse 6.1.4 et empreinte de la roue (amorce, code 18, puis B0) ; corpus d'activations et jetons gardés (89 498, `c37186ad…`) comparés juste après `03_token_counts.py`, avant `lens_compare.py` et la fumée ; deux relevés écrits une fois et scellés. Écart : m-8. |
| appels au code voisin | noms et chemins vérifiés : `data/fits/…-T128.pt`, `data/lenses/<nom>/`, `data/token_counts-<modèle>.pt`, `data/acts/<modèle>.pt` (fumée dans un fichier à part), `data/causal/<modèle>-causal[-seed1].pt`, `data/summary/causal_lens_<étiquette>_<modèle>.json` et `.log`, `data/summary/reads_at_firings_<modèle>.json`, `data/checks/reads_at_firings-<modèle>.pt` ; clés `targets[cible][lentille]["layer"\|"r_med"…]`, `["neurons"]["layers"][i]["read_S"\|"silent"]`, `layers[couche]["a vs b"]["top1_agree"]` ; format de la ligne « doc i/n (… tokens) in X s ». |
| secrets | clé présente aux deux seules étapes de téléchargement ; jamais dans l'environnement d'un enfant ; `token=False` pour Neuronpedia ; rien d'écrit ; balayage de la partie 2 et de l'arbre poussé. |

## Déclaration de forme : Drowse 6.1.4 installé sans ses dépendances

Métadonnée de la roue : `torch>=2.13.0`, `transformers>=5.22`, `huggingface-hub>=1.26`, `accelerate>=0.27`, `safetensors>=0.7.0`,
`pyyaml>=6.0`, `fastapi>=0.110`, `uvicorn[standard]>=0.44.0`. Par analyse syntaxique des imports (rien n'est importé) :
- `drowse/__init__.py` charge ses noms à la demande ; `drowse.lens.store`, `jlens`, `key` et tout ce qu'ils importent au niveau
  module (`drowse.base.atomic`, `paths`, `shards`, `source_registry`, `drowse.errors`, `drowse.lens.corpus`) ne demandent que
  **torch** et **safetensors** ;
- `save_lens` et `load_local_lens` appellent `_local_dir`, puis `select_local_lens`, qui importent `drowse.lens.sources` : ce module
  importe **`yaml`** (PyYAML) au niveau module (`sources.py` l. 29), et `drowse.base.hf`, `drowse.base.integrity` (bibliothèque
  standard ; `huggingface_hub` seulement dans des fonctions) ; `save_lens` importe aussi `drowse.lens.relp` (aucun paquet tiers) ;
- `transformers` n'est importé que dans `sources._config_dimensions` (l. 458), sur le chemin des lentilles externes, que ni
  `save_lens` ni `load_local_lens` ne prennent ; `accelerate`, `fastapi`, `uvicorn` ne sont pas sur ce chemin ; `datasets` seulement
  dans des fonctions de `drowse.lens.corpus` non appelées.

Conclusion : le seul paquet demandé à l'import et **absent de `requirements-neuron-lens-b-beta-v1.txt`** est **PyYAML**. Il arrive
en pratique comme dépendance de `transformers`, `huggingface_hub` et `datasets`, mais rien ne l'exige ni ne le fixe ici, et je n'ai pas
pu vérifier les métadonnées de ces versions. La borne `transformers>=5.22` non tenue ne gêne aucun module employé. L'interface
appelée par le voisin existe en 6.1.4 (`LensProvenance` et ses champs, `save_lens(lens, model_id, provenance, split_half=…)`,
`load_local_lens(model_id, "r")`, `JacobianLens(out, mid=, n_prompts=, d_model=, key=)`, `.jacobians`, `.matrix`, `.layers`,
`.sites`, `.key`, `.n_prompts`, `.d_model`, `LensKey("R")`). La déclaration est donc tenable, à deux conditions : écrire `pyyaml`
dans les exigences (version relevée en partie 2), et jouer à B0 l'essai de M-3 — faute de quoi l'incompatibilité éventuelle n'est
constatée qu'après les ajustements.

## Les essais couvrent-ils la table « Branches des gardes » de P.4 et les gardes du montage ?

| ligne de la table | couverture |
|---|---|
| (d) test sauté ; estimateur faussé | fonction pure essayée (« skipped », « failed », aucun test, fumée) ; motifs des deux artefacts vérifiés uniques sur l'essai réel ; les artefacts eux-mêmes ne sont joués que sur la machine, à B0 |
| (f) matrice perturbée de 10⁻³ | hors des trois fichiers : dans l'essai scellé du Llama miniature (ses artefacts), joué sur la machine seulement |
| (g) quatre artefacts | couverts (`nan`, somme non finie, `full_length` faux, document de 127 jetons), plus comptes, `next_doc`, empreinte, lentille |
| (h) S de 31 couches | couvert |
| (i) quatre artefacts | couverts (autre révision, deux identifiants permutés, `skip` 999, texte commun), plus identifiant commun |
| (j) 0,06 à deux couches ; 0,11 à une | couvert par les essais du code des verdicts (`test_vii_et_branches_j`, `test_bornes_j`) |
| (k) nos noms avant la passe ; empreinte du lien différente | couverts en fonction pure ; le câblage (pose des liens) ne l'est pas (M-6) |
| (l) pôle retenu de norme nulle | couvert côté verdicts (`test_a1_norme_nulle`) ; le calcul de « norme non nulle » dans le lanceur ne l'est pas |
| (p) 3 documents de la tranche DCLM | couvert en fonction pure, plus 15 contextes |
| (q) fichier `-T128` présent ; `rows_sha256` altéré | couverts en fonction pure ; la décision « premier lancement ou relance » ne l'est pas (M-6) |
| (r), (s) | couverts en fonction pure ; la détection des fichiers de (s) ne l'est pas |
| A1 (trois cas de zéros) ; rangs 2 et 3 | couverts par les essais du code des verdicts (`test_a1_zeros_du_temoin`, `test_rang_2_prime_sur_rang_3`) |
| gardes du montage | banc 11,5 / 15 / 24 s : couvert (plus 14,2 et 23,6 aux bornes) ; `rows_sha256` altéré et 931 documents : couverts ; dépense à 45,0 et 67,5 USD et empreinte de Drowse altérée : **absentes des trois fichiers**, présentes dans `tests/test_neuron_lens_montage_b_beta_v1.py` (commit `41c7f2e8`, non contre-lu ici, hors du dépôt réduit et de la liste de l'amorce) ; plafonds et minuterie : commande, non lue |

Réponse : oui pour les branches, au niveau des fonctions pures et du code des verdicts ; non pour les gardes telles que câblées dans
les étapes (M-6), ni, dans les trois fichiers demandés, pour la dépense simulée et l'empreinte de Drowse.

## Ce que cette contre-lecture ne couvre pas

La commande v1 et `garde_depense_v4.py` ; le code déjà contre-lu (verdicts, grandeurs, contrôles de B0, manifeste, scellement), lu
seulement pour ses appels ; l'exécution réelle du code voisin et de Drowse (interdite dans le conteneur) : les formats sont vérifiés
par lecture, l'aller-retour ne sera établi que par la garde (o) ou par l'essai proposé en M-3.
