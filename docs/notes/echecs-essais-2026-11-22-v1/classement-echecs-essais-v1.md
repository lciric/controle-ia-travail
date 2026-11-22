# Classement des 202 échecs de la suite d'essais de main — v1

Pièce de travail (classe C). Session fille `session_013QMaynAzxVeXMJgzyTyXRG`, mandat de la mère `session_013QMayjbmQUdDuDs2S3i3XD`, 22 novembre 2026, vers 19:00Z-19:40Z. Aucune dépense ; aucun résultat d'expérience lu ; aucun fichier scellé ni essai modifié.

## Verdict

202 échecs, tous rejoués sur le commit abf45a528 : **175 de classe A (date figée passée), 26 de classe B (état du dépôt), 0 de classe C (dépendance manquante), 1 de classe D (défaut réel, dans un essai).** 201 se reproduisent à l'identique ; le 202e (lentilles, seconde passe) passe seul et échoue selon l'ordre de chargement des fichiers d'essais, c'est le seul défaut.

Pièce d'entrée : `registres/essaim/vers-mere/2026-11-22-1905-organisme-echecs-suite-essais.txt` (branche `lot/compte-organisme-v1`, empreinte vérifiée `afcbdc8d01080ffef1f441ef34ff4b9add4006e2e9eaeaa1f76b0cd61af0cf84`). Le constat de l'organisme (environ 170 + 7 + 20) est confirmé dans ses grandes lignes ; les comptes exacts sont ci-dessous. Aucun des fichiers d'essais en cause n'a changé entre abf45a528 et `origin/main` eb6735934 : le classement vaut pour la main actuelle.

Détail par essai : `classement-par-essai-v1.tsv` (202 lignes : identifiant, classe, issue du rejeu, raison). Projet de liste : `projet-echecs-connus-v3.txt`.

## Méthode

- Copie de travail de abf45a528 (arbre de travail git, dans le bloc-notes de la session), environnement neuf `pip install -r requirements-cpu.txt` (torch 2.14.1 compris : le conteneur n'avait pas torch, ce qui aurait ajouté de faux échecs de classe C ; la suite de la mère, elle, l'avait).
- Rejeu par fichier des seuls essais en échec (166 identifiants sans paramètres, donc 237 cas joués, dont 36 paramètres sains qui passent), rapport JUnit pour lire le message de chaque cas ; pour les 27 cas d'amorce dont le message ne cite pas la sortie, second rejeu avec `--showlocals` pour lire la sortie de l'amorce.
- Essai d'ordre pour le seul cas non reproduit (voir D).
- **Refus noté** : un rejeu des amorces sous une horloge ramenée de douze jours (bibliothèque de falsification du temps chargée pour tout le conteneur) a été refusé par le classifieur de permissions. Il n'a été ni rejoué ni contourné. La classe A repose donc sur le texte des refus des amorces, pas sur une preuve positive (« passe à la bonne date »).

## Classe A — date figée passée (175)

Fichiers : `tests/test_t06_scripts.py` (8), `test_t06_v2_scripts.py` (12), `test_t06_v3_scripts.py` (16), `test_t06_v5_amorce.py` (31), `test_t06_v6_amorce.py` (32), `test_t06_v7_amorce.py` (32), `test_t06_v12_amorce.py` (32), `test_t06_v7_amorce_minuterie.py` (12).

Les essais figent `GO-2026-11-02-28` (valide du 2026-11-02 au 2026-11-16) et `FIN_GO = 1794873600` (2026-11-17T00:00Z), tandis que l'amorce lit l'heure réelle par `date`. Motifs lus dans les sorties :
- 165 cas : « destruction demandée (démarrage après l'échéance : aucun calcul) » (141 dans le message d'échec, 24 lus par `--showlocals`) ;
- 9 cas : « GO-2026-11-02-28 hors de sa période de validité (2026-11-02 → 2026-11-16) le 2026-11-22 » (6 dans le message, 3 par `--showlocals`) ;
- 1 cas : « échéance 1794873599 hors de ]maintenant, fin du GO] » (création des contrôles).

Ce sont les amorces de T0.6 (v2 à v12), instruments d'une ligne close. Le comportement testé (refuser après l'échéance) est sain ; c'est l'essai qui vieillit.

## Classe B — état du dépôt (26)

Listes ou comptes figés que le dépôt a dépassés (17) :
- listes de fichiers d'essais de T0.6 v11, v12, v13 (3) : fichiers ajoutés depuis (`tests/test_accb6_*.py`, …) ni listés ni exclus ;
- cibles invisibles v3, v4, v5 (6) : inventaires des constructeurs d'invite et liste des lecteurs admis de la clé « cibles » figés ; fonctions ajoutées depuis (formation et relecture du barreau 5, accumulation b6, relecture Fable par interface v1 à v4, lanceur v9 et seconde passe des lentilles). Même cas que les lignes v1 et v2 déjà dans `tests/echecs-connus-v2.txt` ;
- dépôt expurgé v7, v8, v9 (3) : 36 chemins ajoutés sous `runs/course-ideation-regard-ou-raisons-v1/` ni visés ni nommés ; v10, v11 (2) : 7 PDF ajoutés sous `docs/notes/percee-apres-blindfold-v1/…/sources/` non couverts ;
- formation du barreau 5 (1) : plancher `MIN_ESSAIS` = 235 figé, le paquet `tests/test_barreau5_familles_*.py` compte 814 essais ;
- mots et coût du bras A v1, v2 (2) : l'essai « clés de registre neuves » exige l'absence de `CODE-MOTS-ET-COUT-BRAS-A`, inscrite le 2026-11-19T09:13:20Z.

Fichiers attendus absents de main (9) :
- suivi des machines des lentilles v6 (5) : `src/controle_ia/neuron_lens/suivi_vast_v5.py` et `suivi_vast_v2.py` absents ; présents sur `prep/neuron-lens-v1` (avec leurs essais) ;
- contrôles b0 des lentilles v2 (2) : `docs/sources/neuron-lens-v2-addendum-20261114/kept-qwen3-8b.txt` absent ; présent sur `prep/neuron-lens-v1`, `calcul/neuron-lens-volet-a-v1`, `course/neuron-lens-volet-a-reduit-v10` ;
- chaîne b bis v6 (1) : `diag/20261118-154143-bbis-t07-v1/sondes-bbis.json` absent ; présent sur `donnees/t07-etape-b-bis-v2` (nom seulement vu, contenu non lu ; c'est une sortie de mesure) ;
- course d'idéation « bassins étroits » v3 (1) : le dossier du superviseur du run v2 vivait hors du dépôt (`/home/user/sorties-course-ideation-bassins-etroits-v2/…`), sur le conteneur de la course ; ailleurs la dépense est lue au plafond (20 USD) au lieu de 0,275477 USD. Non récupérable depuis le dépôt.

## Classe C — dépendance manquante (0)

Aucune dans la suite de la mère. Remarque : dans un conteneur sans `requirements-cpu.txt`, torch manque et une partie des essais (cibles invisibles, b5f, …) ne se collecte plus ; la routine de reprise suppose cette installation.

## Classe D — défaut réel (1)

`tests/test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py::test_cibles_du_corpus_jamais_celles_de_montage_v1_telles_quelles`. Passe seul, passe avec tout son fichier (34 sur 34) ; échoue (« Regex pattern did not match ») quand `tests/lentilles_sondes_bbis_jouets_v9.py`, ou tout module qui importe `lentilles_sondes_bbis.lanceur_v8` ou `lanceur_v9`, est chargé avant dans le même processus. Cause : ces lanceurs font `from . import corpus_pagine_v1`, ce qui pose l'attribut `corpus_pagine_v1` sur le paquet ; l'essai masque le module par `sys.modules[...] = None`, mais `from . import corpus_pagine_v1` dans `montage_v2.cibles_du_corpus` lit d'abord l'attribut du paquet et ne lève donc pas l'arrêt attendu. Le défaut est dans l'isolement de l'essai ; le code de production n'est pas en cause (le garde-fou « non branché » n'a de sens que si le module manque vraiment, et il manque alors pour tout le processus).

## Proposition (non appliquée)

**1. Classe A — date figée.** Décision : comment rendre ces 175 essais lisibles. Enjeu : une suite rouge en permanence cache les vrais échecs.
- (a) Liste `tests/echecs-connus-v3.txt` (nom neuf, R12), qui recopie les 14 lignes de la v2 et ajoute les 175 lignes A, chacune avec sa raison (projet prêt : `projet-echecs-connus-v3.txt`), plus un greffon v3 et la ligne de `tests/conftest.py` repointée. Avantage : rien ne change dans les amorces scellées ni dans les essais ; échec attendu strict, donc un retour au vert se voit. Inconvénient : 175 essais ne vérifient plus rien jusqu'à la fin des temps.
- (b) Horloge injectée : une variable `HORLOGE_UTC_S` honorée par l'amorce seulement si `AMORCE_ESSAI_LOCAL=1`, et que les essais posent avant l'échéance. Avantage : les essais vérifient de nouveau le comportement. Inconvénient : il faut une version neuve de chaque amorce (v2 à v12 sont citées par des pièces scellées) pour une ligne close ; coût élevé pour un instrument retiré.
- Recommandation : (a) pour les amorces de T0.6 existantes ; (b) comme règle pour toute amorce neuve (horloge injectable dès la v1, essais datés relativement à l'heure injectée). Confiance : bonne. Défaut sous 48 heures : (a).

**2. Classe B — listes figées (17).** Même traitement que les lignes v1 et v2 des cibles invisibles déjà inscrites : lignes ajoutées au projet v3, raison par ligne. Les essais plus récents de chaque famille (v12, v13 de la liste T0.6 si une v14 existe ; dépôt expurgé au-delà du v11) restent la garde vivante ; s'il n'en existe pas, une version neuve de l'essai est à écrire plutôt qu'une ligne de plus.

**3. Classe B — fichiers absents (9).** Récupérer d'abord, lister ensuite :
- verser sur main, depuis `prep/neuron-lens-v1`, `suivi_vast_v2.py`, `suivi_vast_v5.py` (et leurs essais, `.sha256` compris) et `kept-qwen3-8b.txt` : code et source, sans résultat ; à vérifier par empreinte avant versement ;
- `diag/…/sondes-bbis.json` est une sortie de mesure du bras b bis : son versement sur main touche au cloisonnement, c'est à la mère de dire ; à défaut, ligne au v3 ;
- le run v2 « bassins étroits » : non récupérable (dossier hors dépôt sur un conteneur fini) ; ligne au v3 avec cette raison.

**4. Classe C.** Rien à faire pour la suite ; rappeler dans la routine que la collecte suppose `requirements-cpu.txt` installé.

**5. Classe D — nœud.** Décision : corriger l'isolement de l'essai des lentilles (seconde passe). Options : (a) version neuve de l'essai qui, en plus de `sys.modules`, retire l'attribut `corpus_pagine_v1` du paquet par `monkeypatch.delattr(paquet, "corpus_pagine_v1", raising=False)` (Opus, classe B, contre-lecture) ; (b) ligne au v3 « dépend de l'ordre ». Recommandation : (a), l'essai garde une vraie garde ; confiance bonne ; défaut sous 48 heures : (a).

## Réserves

- Classe A prouvée par le texte des refus, non par un rejeu à date antérieure (refusé par le classifieur ; non contourné).
- Le rejeu s'est fait essai par essai, par fichier, et non dans l'ordre de la suite complète : un autre effet d'ordre que celui de D n'est pas exclu pour les 201 cas qui échouent de toute façon.
- Routine de reprise : empreintes de lancement conformes ; `verifier-arbre` signale 96 problèmes déjà présents, aucun de cette session ; suite complète non relancée (c'est la pièce même, 6 heures) ; Hetzner 177170935 « essai-3-palier-0b » en tâche pour l'organisme, non touché ; pas d'outil Vast dans le conteneur.
