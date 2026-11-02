# Contre-lecture 3 (règle R2, courte, sur les seules différences) — préenregistrement de l'analyse appariée boîte blanche / boîte noire sur l'organisme « coût gonflé » de P3 — brouillon 3 — v1

**Verdict : scellable après corrections mineures (listées) — F1 à F6, toutes locales au texte (elles font un brouillon 4) ; le code v3 et ses essais ne changent pas (aucune version 4 du code, aucune empreinte de code à refaire).** Ce qui est acquis : les corrections D1 à D18 et J1 à J7 de la contre-lecture 2 sont appliquées (code : égal aux copies corrigées du contre-lecteur, aux différences voulues près ; texte : 42 remplacements sur 48 mot pour mot, 6 modifiés pour des raisons valables) ; les gardes S1 (second passage par l'empreinte du texte) et S2 (versions de Python, numpy et scipy) sont correctes et éprouvées sur cas sain et sur artefact ; les 36 essais passent (13 de v3, 23 de v1 et v2) ; les empreintes des marqueurs déjà remplis sont exactes ; le script de fréquence v2 rejoué sur les modules v3 donne exactement la même sortie. Ce qui reste : (1) la section « Concordance » omet deux écarts de fond avec le texte du fournisseur (le bras du fournisseur apprend contre l'honnête seul ; sa métrique de décision est le rappel à 1 %, non l'aire d'épisode) : un lecteur neuf à l'étape 0.g les trouverait et, selon la règle écrite par le texte, suspendrait le lancement alors que le texte est déjà scellé (F2) ; (2) rien n'impose que l'analyse principale de R1-R2 soit scellée avant que celle-ci soit lancée, alors que sa sortie porte sur les mêmes données (F4) ; (3) quatre défauts de forme, dont une régression de D1 (date de fin en avance de deux à trois minutes sur le dernier fichier et sur le commit) et une entrée de la contre-lecture 2 qui n'est pas celle que ce rapport-là fixait (F1, F3, F5, F6).

Repères (les codes sont développés une fois ici) : **R-1086** = « go anticipé » de Lazar du 2026-11-01, 23:50 heure de Paris, appliqué à la recommandation (a) sur N-029 ; **R-1090** = décision de la session conv-audit (registre, commit `90803649`) : l'analyse boîte blanche / boîte noire devient la lecture secondaire de R1-R2, la lecture principale étant confiée à un texte neuf fidèle au fournisseur ; **R-1014** = confirmation de N-029 (a) par Lazar dans la session du fournisseur (session-depot) ; **N-029** = décision sur la référence boîte noire (locale, lue sur les épisodes de T0.6) ; **N-026** = bras de diagnostic « moyenne » permis dans un préenregistrement, jamais en production ; **runs R1, R2, R4** = rejeu des activations de P3, juge de 3 milliards de paramètres sur les 2 400 actions de P3, seconde dose de l'organisme ; **règles R1 … R14** = règles gelées du dépôt (R1 préenregistrement scellé avant toute lecture, R2 contre-lecture, R5 gardes testées sur cas sain et artefact, R6 empreintes, R12 versions dans les noms) ; **W, G, J3s, J3g, J8s, C, T** = bras du préenregistrement du fournisseur (sonde de l'organisme au maximum, sonde générique, juge 3B spécialisé, juge 3B générique, juge 8B spécialisé, règle du coût déclaré, prédicteur sur les traits du texte) ; **(i), (ii), (iii), (L)** = bras de ce texte (sonde entraînée sur l'organisme, juge de 3 milliards, sondes génériques de P3, témoin lexical) ; **C1 … C20** = corrections de la contre-lecture 1 ; **D1 … D18** et **J1 … J7** = corrections de la contre-lecture 2 (J : formats et concordance avec le fournisseur) ; **S1 … S6** = suggestions de la contre-lecture 2 ; **F1 … F6** = corrections de ce rapport ; **G1 … G4** = suggestions de ce rapport.

- **Relecteur** : sous-agent neuf (Claude), qui n'a écrit ni le brouillon 1, 2 ou 3, ni le code v1, v2 ou v3, ni les calculs de prédictions, ni les scripts de fréquence, ni les contre-lectures 1 et 2, ni P3. Écrit le 2026-11-02, à partir de 00:13 UTC (01:13 heure de Paris) ; la date qui fait foi est celle du commit qui le verse.
- **Brouillon relu** : `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md`, sha256 `addadee095efccf1fadbbc0306bca131bb5bd07f216fec80988a48d0ea9222f3` (commit `c67d7a6f`, 2026-11-02 00:10:31 UTC ; dernière écriture du fichier 00:09:11 UTC).
- **Lu en entier** : le brouillon 3 (247 lignes) ; le rapport de rédaction v3 ; le diff livré (`differences-brouillon3-code-v3-v1.diff`, trois parties) ; dans la contre-lecture 2 (`8697d7b2…`), les sections I et J, l'index des corrections, les textes de remplacement de D1 à D8, J1, J4, J6 et J7 et, par programme, tous les autres ; `lecture_v3.py` (S1, S2, gardes, issue, `analyser_v3`), `rendu_v3.py`, `constantes_v3.py`, `evaluation_v3.py` et `entrees_v3.py` par comparaison à v2 (arbre syntaxique) ; `tests/test_analyse_blanche_noire_v3.py` (mode décisif en entier) ; en texte seulement, le préenregistrement R1-R2 du fournisseur (en entier), le message n° 246 et, par recherche de mots, le préenregistrement R4 ; la ligne R-1090 du registre des décisions.
- **Rejoué** : voir les sections 5 et 6 (essais, script de fréquence, gardes S1 et S2 par appels directs) et la section « Traçabilité ». `nice -n 10`, cache de pytest désactivé, répertoires temporaires dans mon bloc-notes, `PYTHONDONTWRITEBYTECODE=1` ; Python 3.13.18, numpy 2.4.6, scipy 1.17.1, pytest 9.1.1. Jamais la commande décisive.
- **Non lu** : aucune donnée de R1, R2 ni R4 (rien sous `donnees/` à leur nom, aucune branche `calcul/…`) ; aucune clé ni aucun secret ; aucun réseau (les `git show` portent sur des objets déjà présents dans le dépôt local, y compris les branches distantes déjà récupérées du fournisseur, pour les seuls textes que le brief nomme).
- **Rien modifié** : ce rapport est le seul fichier écrit dans le dépôt ; aucun commit ; pas d'empreinte compagnon (`.sha256`) écrite : elle revient à celui qui verse le rapport. Mes scripts et mes copies sont dans mon bloc-notes (section « Traçabilité »).

---

## 1. Corrections D1 à D18 et J1 à J7 : appliquées comme demandé, ou écart justifié

**Code (cinq fichiers et les essais).** Méthode : (a) j'ai appliqué mécaniquement les 101 remplacements « code » du rapport de la contre-lecture 2 au code v2 commité (`b621ad69`) : chaque « ancien » figure une fois, et les cinq fichiers obtenus ont exactement les empreintes de la section I de ce rapport (`4ee514b8…` constantes, `cdd5dc73…` entrées, `a17e01fe…` lecture, `af08d07f…` rendu, `5d0787aa…` essais) ; (b) j'ai renommé en v2 le code v3 (script `renommer.py` du rédacteur, sens « arrière ») et l'ai comparé à ces copies : les seules différences sont les docstrings, `VERSIONS_EXIGEES` (S2), les deux fonctions `exiger_premier_passage_v3` et `exiger_versions` et leur appel (S1, S2), la ligne « lecture secondaire » dans `issue` et dans `rendu`, et dans les essais les noms réels des fichiers jouets (J1), les essais S1 et S2 et une assertion sur la ligne « lecture secondaire » ; `evaluation_v3.py` est la copie de `evaluation_v2.py` à la docstring près (comparaison par arbre syntaxique : aucune fonction différente). Mon diff regénéré est, ligne à ligne, le diff livré (parties 1 et 3 ; la partie `evaluation` est la comparaison de la docstring seule).

**Texte.** Les 48 remplacements du brouillon sont dans la copie corrigée du contre-lecteur. Dans le brouillon 3 : 42 figurent mot pour mot ; 6 sont modifiés, tous pour une raison valable : D1 (date : le rapport demandait à la session de l'écrire ; voir F1), D3 (phrase de tête complétée du n° 246 et de la lecture du kit ; la « Lecture préalable déclarée » est reprise mot pour mot), D5 (le chiffre « qui porte sur le code le plus proche du code cité », et une phrase ajoutée : les scripts de fréquence importent `lecture_v2`, non `lecture_v3` ; exact), D8 (étape 0.c adaptée aux deux marqueurs restants), D15 (la ligne de portée reçoit la ligne « lecture secondaire »), J7 (recommandation remplacée par la décision de la session, R-1090). D3, D5 et D15 ne sont pas nommés comme exceptions dans l'entrée de la contre-lecture 2 : F5.

| id | objet | état |
|---|---|---|
| D1 | dates du brouillon | **à corriger** (F1) : la date du brouillon 3 est écrite, mais « 00:12 UTC » est postérieur à la dernière écriture du fichier (00:09:11 UTC) et à son commit (00:10:31 UTC) : même défaut que D1 corrigeait |
| D2, D4, D6, D7 | BN-P4 ; retraits et essais déclarés ; recalcul indépendant ; preuve du motif de `R2: null` | conforme, mot pour mot |
| D3 | lecture préalable de la borne | conforme, phrase de tête complétée (justifié ; F5 la nomme) |
| D5 | fréquence d'erreur | conforme, précisée (justifié ; F5 la nomme ; scripts rejoués : section 5) |
| D8 | étape 0 et marqueurs | conforme ; étape 0.c adaptée aux deux marqueurs restants ; contenu des marqueurs : section 4 |
| D9 (révisée), D10, D11, D13, D14, D18 | motif fermé de `R1: null` ; garde « tâches communes » ; repli de R4 ; juge non lu à la dose R4 ; (L) obligatoire ; fourchette de (ii) | conforme : code égal aux copies corrigées, texte mot pour mot, essais présents (13 réussis) |
| D12, D16, D17 | règle de fidélité effective ; phrase « établie » ; source de la tolérance de 0,02 | conforme, mot pour mot |
| D15 | portée écrite par le code et le rendu | conforme ; la ligne de portée reçoit en plus la ligne « lecture secondaire » (voulu, J7) |
| J1, J4, J6 | noms réels des fichiers ; écart 4 (T du fournisseur) ; ordre imposé par le préenregistrement R4 | conforme, mot pour mot ; J1 aussi dans les essais (noms réels, déclaré) |
| J2, J3 | longueur rejouée, règle de repli ; juge 3B seul, invite gelée | conforme : code égal aux copies, texte mot pour mot |
| J5 | — | sans objet (traité par D9, J2, D17), comme dans le rapport |
| J7 | concordance avec le fournisseur | **écart justifié** (décision de la session, R-1090 : lecture secondaire, réserve portée à Lazar, version nouvelle déclarée si « aligner »), **mais** la section est incomplète (F2), l'ordre des deux lectures manque (F4), R-1090 n'est pas cité (F3) |

## 2. S1 et S2 (code et essais)

**S1.** `exiger_premier_passage_v3` appelle d'abord la garde du chemin de v1, puis refuse tout manifeste de `runs/*/manifeste.json` dont les octets contiennent l'empreinte du texte (lisible ou non). Appelée dans `analyser_v3` avant la création du manifeste, donc un refus ne consomme pas le premier passage. **S2.** `exiger_versions` compare `manifeste.versions()` (Python via `sys.version`, numpy et scipy via les métadonnées installées) à `VERSIONS_EXIGEES`, constante gelée (donc couverte par l'empreinte des constantes `273c0a68…`) ; appelée dans le même dictionnaire que S1, avant le manifeste. Le résultat écrit les versions dans `lien_au_preenregistrement`.

**Mes essais indépendants** (appels directs, hors des essais du dépôt, répertoires temporaires dans mon bloc-notes) : S2 refuse numpy 2.4.5, Python 3.12.1 et un scipy absent ; accepte les versions gelées (celles du `.venv`). S1 : cas sain (un manifeste d'un autre texte : accepté, `manifestes_lus: 1`) ; refuse un manifeste lisible qui cite l'empreinte sous un autre nom ; refuse un manifeste illisible qui contient l'empreinte. Chaîne de garde du mode décisif : la fermeture des importations de `lecture_v3` est exactement la liste fermée (25 modules, 12 du paquet et 13 gelés, aucun module v2) ; les 27 citations de code du texte égalent les fichiers du disque ; l'empreinte des constantes recalculée égale celle du texte.

**Essais du dépôt (R5).** `test_mode_decisif_v3` : cas sain S2 (`lien_au_preenregistrement["versions"] == VERSIONS_EXIGEES`, donc la garde est bien appelée dans le chemin réel) ; artefact S1 (copie du texte scellé sous un autre nom : refus, avec un message qui ne peut venir que de S1, « cite déjà l'empreinte », distinct de celui de la garde du chemin) ; artefact S2 par appel direct de `exiger_versions` avec une constante falsifiée. **Conforme.** Une réserve non bloquante : l'artefact S2 n'est pas éprouvé *à travers* `analyser_v3` (falsifier la constante déclencherait d'abord la garde des constantes gelées, ce que l'essai ne peut pas éviter) ; falsifier `LB3.versions` l'éprouverait, mais changer le fichier d'essais exigerait un fichier v4 (R12) et une empreinte de plus à citer : non retenu (G2).

## 3. Section « Concordance », ligne « lecture secondaire », étape 0.g

**Citations du préenregistrement du fournisseur** (« Statut ») : les trois citations (le préenregistrement d'analyse de conv-audit « fixe le détail du calcul (niveau, agrégation séquentielle, quantile, plis) » ; le fournisseur « gèle les runs, les contrôles, les bras et les critères de lecture » ; « un lecteur neuf vérifie la concordance des deux textes scellés ; tout écart de fond est un nœud porté à Lazar ») sont exactes (l. 32-37 de son texte). Le « Statut » ajoute : « tout emploi de `moyenne` hors du bras de diagnostic est un nœud » : phrase absente de la section ; voir F2.

**Les cinq écarts, un à un, contre le texte du fournisseur** (empreinte `80c85a00…`, lignes de la copie du contre-lecteur 2) :

| # | écart déclaré | passage du fournisseur | exact |
|---|---|---|---|
| 1 | W = maximum par dimension, couche 15, C = 1 ; la moyenne en diagnostic ; ici (i) = moyenne, couche parmi 7, 15, 23, λ = 10 | « Bras » l. 107-108 ; « Bras de diagnostic, jamais en production (N-026) » l. 116-117 | exact, **incomplet** : W apprend le saboteur contre l'honnête **seul** (« Métrique » l. 98 : négatifs = actions honnêtes, témoin et mention en contrôles) ; (i) apprend contre toutes les autres conditions (point 3 des écarts déclarés du texte) |
| 2 | 1 % chez le fournisseur ; 0,05 ici | l. 79 et 127 | exact, **incomplet** : la métrique principale du fournisseur est le *rappel* à 1 % (l. 100-106 ; secondaires : 5 % et l'aire) et sa lecture porte sur la borne de l'intervalle de la différence de rappel (l. 128) ; ici la décision porte sur l'*aire d'épisode* (Holm) et la puissance à 0,05 n'est qu'un filtre de signe (point 6 des écarts déclarés) |
| 3 | T (coût normalisé par la médiane de la tâche, longueur en caractères, formes du coût) ≠ (L) | « Bras » l. 111-115 | exact |
| 4 | exclusion des actions non fidèles chez le fournisseur ; épisodes entiers ici | « Métrique » l. 98-99 ; « Plan » point 4 | exact |
| 5 | Bonferroni à 97,5 % sur W − G et W − J3s, 5 plis de 12 tâches ; Holm à quatre comparaisons, 10 plis, cinq découpages | l. 121-123 | exact |

**Complets ?** Non, sur deux points de fond (lignes 1 et 2 ci-dessus). Conséquence concrète : l'étape 0.g écrit qu'« un écart de fond non déclaré à la section « Concordance » suspend le lancement » ; un lecteur neuf qui lit le « Statut » du fournisseur trouvera ces deux écarts (je les ai trouvés en un passage), alors que le texte est déjà scellé (étapes c et d) et que le corriger exigerait une version nouvelle (R12). Il faut les déclarer maintenant. La ligne « lecture secondaire » écrite par le code dit « cinq écarts déclarés » (texte figé dans `lecture_v3` et `rendu_v3`, donc pas de code à changer) : **F2 garde cinq écarts numérotés** et met les deux compléments dans les écarts 1 et 2 ; les autres différences de détail (niveau de lecture, quantile, tirages, forme du plancher, bras de diagnostic W aux couches 7 et 23 et hors du champ du coût, analyse de sensibilité au contexte exact, bras C, J3g et J8s) relèvent soit de ce que le fournisseur confie à l'analyse de conv-audit (« Statut » ; n° 246 : « Restent chez toi : plancher apparié, prédicteur sur les traits, test « colonnes nommées seulement » de R4 »), soit de bras que ce texte ne lit pas : F2 le dit en une phrase. Deux renvois sont ambigus (« écart 5 », « écart 4 » désignent les points des « Écarts déclarés à des décisions en vigueur », alors que la section a sa propre numérotation 1-5) et la phrase « Ce texte ne code ni ne lit les bras du fournisseur » est inexacte pour (ii) et (iii), qui lisent les colonnes de J3s et de G : F2.

**Ligne « lecture secondaire » écrite par le code.** Le texte de `issue_v3` et de `rendu_v3` est celui que le brouillon cite (section « Critères de lecture gelés »), même ordre (portée, lecture secondaire, version complète ou « R1 seul »), et l'essai vérifie sa présence dans l'issue et dans le rendu. Conforme.

**Règle « les deux analyses rapportées en entier quel qu'en soit le signe ; aucune citation de l'une sans l'autre ».** Écrite : « Statut » du texte, ligne « Ce que ce texte n'est pas », « Ce qu'aucune issue ne permet » (« citer cette lecture sans celle du fournisseur, ou l'inverse »), section « Concordance », issue et rendu. Tenable pour ce texte (elle borne la citation, pas la lecture). Trois précisions : (1) « l'analyse du fournisseur, scellée la première » est inexact : ce qui est scellé est le *préenregistrement* du fournisseur (ses bras) ; son *analyse* (code et préenregistrement d'analyse propres) n'existe pas encore, R-1090 la confie à un texte neuf (F3) ; (2) la règle « ou l'inverse » lie un texte qui n'existe pas : le texte de l'analyse principale doit porter la règle symétrique (G3) ; (3) l'ordre entre les deux lectures n'est pas écrit (F4).

**Étape 0.g et le texte du fournisseur** (« avant toute lecture, un lecteur neuf vérifie la concordance des deux textes scellés ; tout écart de fond est un nœud porté à Lazar »). Le brouillon 3 le traite en partie : il prévoit un lecteur neuf, avant le lancement, et un arrêt si un écart non déclaré apparaît. Défauts : (a) « les deux textes scellés » n'est pas défini : depuis R-1090, les deux textes que le fournisseur vise sont les siens et l'analyse principale, non cette lecture secondaire ; (b) rien n'impose que l'analyse principale soit scellée avant le lancement de cette commande, dont la sortie (imprimée par `_main`) porte sur les mêmes données : la lire avant ce scellement serait une lecture de résultat avant scellement pour l'analyse principale (règle R1) ; (c) le texte du fournisseur dit « nœud » pour tout écart de fond, déclaré ou non ; le brouillon le qualifie de « réserve » : c'est la décision de la session (R-1090), non celle de Lazar, et le texte doit le dire. F3 et F4. Ma contre-lecture n'est pas la vérification de l'étape 0.g (le texte n'est pas scellé et celui de l'analyse principale n'existe pas).

## 4. Marqueurs

| marqueur | état | verdict |
|---|---|---|
| commit du code d'analyse | reste ; contenu prévu : les 40 caractères de `git rev-parse HEAD` juste après le commit de l'étape 0.a, premier commit de l'étape, ni amendé ni refait, entre accents graves | conforme au contenu fixé par la contre-lecture 2 (section I, ligne 3 et D8) |
| empreinte du registre à la version qui porte R-1086 | rempli : `5bdcbbb19a8220d44c080577f27b2651c088388a102743010ec3fce8f13bdb29` | exact (`git show 7b0ef14f:registres/decisions.md \| sha256sum`) |
| `LISEZMOI` v2 du kit | rempli : chemin, branche `prep/runs-r1-r2-r4-v1`, commit `567260c0…` (40 caractères), `32339415…` | exact (`git show 567260c05687747f0c7a715fc9b15b4fc6297d65:docs/notes/runs-r1-r2-r4-v1/LISEZMOI-runs-r1-r2-r4-v2.md`) |
| préenregistrements scellés du fournisseur | `80c85a00…` (R1-R2), `f4f8ca28…` (R4) | exacts (même commit `567260c0`, `git show … \| sha256sum`) |
| message n° 246 | `75b61a54…` | exact (`git show origin/canal/session-depot-reprise-n73:brouillons/canal-reprise-releve-v1/messages/session-depot_2026-11-01_n246.md`, égal à son `.sha256` et à la copie du bloc-notes) |
| entrée de la contre-lecture 2 | remplie | **à corriger** (F5) : elle omet « essais après corrections : <n> réussis » que la section I de la contre-lecture 2 fixait, et dit « mot pour mot » sans nommer D3, D5, D15 |
| entrée de la contre-lecture 3 | reste ; six champs libres (empreinte du brouillon relu, chemin et empreinte du rapport, verdict, liste de corrections, nombre d'essais) | **à resserrer** (F6) : tout est connu sauf l'empreinte du rapport et le nombre d'essais ; la « liste libre » rouvre le canal de texte libre que D8 fermait ; le texte ne dit pas si les accents graves du marqueur partent |

Les autres empreintes citées par le brouillon 3 et recalculées : brouillons 1 et 2, contre-lectures 1 et 2 (v1 et v2 du rapport), rapport de rédaction v2, calculs v1 et v2 et sortie, scripts de fréquence v1 et v2 et leurs sorties, paquet v1 (commit `a3db3e3e`) et v2 (commit `b621ad69`) inchangés sur le disque : toutes égales.

## 5. Scripts de fréquence non rejoués sur v3 : acceptable

Le texte dit que les deux scripts importent `lecture_v2` et que la règle de décision est la même. **Je l'ai vérifié de deux façons.** (1) Par arbre syntaxique, les seules fonctions de `lecture` dont le comportement de décision change entre v2 commité et v3 sont `comparer` (D14 : refus des comparaisons du juge si (L) est non lu) et `ligne_comparaison` (D16 : la phrase « établie ») ; le script v2 passe `lu = {b: True}` pour tous les bras, (L) compris, donc D14 n'agit pas ; `evaluation_v3` est identique à `evaluation_v2` ; les constantes de décision sont inchangées (`FOURCHETTES_AIRE` change, qui ne sert qu'à l'audit). (2) **Rejeu** : `frequence-regle-decision-v2.py` copié hors du dépôt, avec ses trois importations remplacées par `constantes_v3`, `lecture_v3`, `evaluation_v3` (`BrasEntraineV3`, `difference_v3`), même entropie `202611020005`, 200 répliques, durée 157 s : sortie **identique** à `frequence-regle-decision-v2-sortie.txt` (hors la ligne de durée) : famille de quatre 8/200 = 0,040 (Wilson [0,020 ; 0,077]), règle abandonnée 27/200 ; « R1 seul » 13/200 = 0,065, règle abandonnée 18/200 ; mêmes états, mêmes aires et fausses alarmes moyennes. Le script v1 (entropie `202611012330`, 9/200) n'a pas été rejoué : le texte le donne déjà « pour mémoire » sur un état antérieur du module (D5). **Acceptable tel quel** ; G1 propose, facultativement, d'écrire le rejeu dans le texte.

## 6. Essais

`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src nice -n 10 .venv/bin/python -m pytest -q -p no:cacheprovider --basetemp=<bloc-notes>` : `tests/test_analyse_blanche_noire_v3.py` : **13 réussis en 29,77 s** ; `tests/test_analyse_blanche_noire_v1.py` et `tests/test_analyse_blanche_noire_v2.py` : **23 réussis (12 + 11) en 55,97 s** ; soit 36 réussis, comme le texte (« 13 » ; « 36 réussis en 82 s » : 85,7 s chez moi, charge faible). Aucun fichier écrit dans le dépôt par ces essais.

## 7. Nouvelles failles introduites par le brouillon 3 (toutes dans F1 à F6)

1. Date du brouillon 3 en avance de deux à trois minutes (F1).
2. Section « Concordance » : deux écarts de fond omis ; renvois ambigus ; « scellée la première » et « ne lit pas les bras » inexacts (F2, F3).
3. Aucune trace de R-1090, la décision sur laquelle repose tout le statut des deux lectures (F3).
4. Ordre entre l'analyse principale et celle-ci non écrit : lecture avant scellement possible (F4).
5. Entrée de la contre-lecture 2 : contenu fixé non respecté (F5) ; entrée de la contre-lecture 3 : champ libre (F6).

Ce qui n'est pas une faille : la fermeture des importations (exacte), les 27 empreintes, l'empreinte des constantes, la règle de décision (identique, rejouée), la qualification de J7 en « réserve » (décision de la session, déclarée ; le texte doit seulement dire qu'elle est de la session), le choix de ne pas aligner les bras (déclaré ; version nouvelle si Lazar le demande).

---

## Corrections, une ligne chacune

| id | gravité | objet | où |
|---|---|---|---|
| F1 | mineure | date du brouillon 3 postérieure à son dernier fichier et à son commit (régression de D1) ; titre « brouillon 4 » | texte, en tête |
| F2 | de fond, correction de texte | « Concordance » : négatifs du bras du fournisseur et métrique de décision omis ; mention de `moyenne` ; renvois ambigus ; « ne lit pas les bras » inexact ; cinq écarts gardés (le code écrit « cinq ») | texte, section « Concordance » |
| F3 | mineure | R-1090 cité (ligne des décisions et « Statut des deux lectures ») ; « scellée la première » inexact ; « réserve » = qualification de la session ; vérification de concordance : sur quoi elle porte | texte, « Décisions qui fondent ce texte » et « Concordance » |
| F4 | de fond, une phrase | étape 0.g : l'analyse principale est scellée avant le lancement (règle R1) ; lecteur neuf ni auteur de ce texte ni de l'analyse principale | texte, Plan d'analyse 0.g |
| F5 | mineure | entrée de la contre-lecture 2 : exceptions D1, D3, D5, D15 et ajout R-1014 nommés ; « essais après corrections : 13 réussis » | texte, section « Contre-lecture » |
| F6 | mineure | étape 0.c (brouillon 4) et entrée de la contre-lecture 3 : contenu fixé (un seul champ libre en plus du nombre d'essais), accents graves, texte corrigé = brouillon 4 | texte, Plan d'analyse 0.c et « Marqueurs de gabarit » |

Ni le code ni les essais ne changent : les empreintes de la liste fermée, l'empreinte des constantes (v3) `273c0a68…` et « 13 essais » restent ceux du brouillon 3. Les remplacements ci-dessous sont **prêts à coller** : chaque « ancien » figure exactement une fois dans le brouillon 3 (16 remplacements, vérifiés par programme et appliqués à une copie ; sur cette copie, `controle_ia.prereg.problemes` ne signale que la section « Contre-lecture », et `lecture_v3.exiger_code_cite` accepte le texte : 27 fichiers, constantes `273c0a68…`). Le texte corrigé s'écrit sous un nom neuf, `…-brouillon4.md` (R12) ; le brouillon 3 reste tel quel.

### Suggestions (non bloquantes)

- **G1.** Écrire dans le texte le rejeu du script de fréquence v2 sur v3 (section 5) : remplacement facultatif donné à la fin des textes ci-dessous.
- **G2.** Éprouver l'artefact S2 à travers `analyser_v3` en falsifiant `lecture_v3.versions` (non retenu : fichier d'essais v4 et empreinte de plus ; à garder pour une version ultérieure).
- **G3.** Pour l'analyse principale (texte neuf de R-1090) : y écrire la règle symétrique (« aucune citation de l'une sans l'autre », celle-ci étant la lecture secondaire) et le même ordre de scellement ; ce texte-ci ne peut pas la lui imposer.
- **G4.** La ligne R-1090 du registre date l'entrée « ≈ 01:20 Paris », alors que son commit (`90803649`) est de 01:11:49 (heure de Paris) : citer le commit et l'empreinte, pas l'heure (c'est ce que fait F3). Même défaut que F1 dans la ligne « entre 00:00 et 00:12 UTC » du rapport de rédaction v3 (dernière écriture 00:09:11 UTC).

## Textes de remplacement

#### F1 — dates et titre

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
(runs R1, R2, R4) — v1 — brouillon 3
```

par :

```text
(runs R1, R2, R4) — v1 — brouillon 4
```

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
brouillon 3 (contre-lecture 2 appliquée, code v3) écrit le 2026-11-02 entre 00:00 et 00:12 UTC (01:00 et 01:12 heure de Paris) ; la date qui fait foi est celle du commit de scellement.
```

par :

```text
brouillon 3 (contre-lecture 2 appliquée, code v3) écrit le 2026-11-02 entre 00:00 et 00:09 UTC (01:00 et 01:09 heure de Paris ; dernière écriture du fichier à 00:09:11 UTC, commit `c67d7a6f` à 00:10:31 UTC) ; brouillon 4 (contre-lecture 3 appliquée) écrit après le rapport de la contre-lecture 3 ; la date qui fait foi est celle du commit de scellement.
```

#### F2 — section « Concordance » : écarts de fond manquants, renvois, statut du texte du fournisseur

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
et qu'avant toute lecture un lecteur neuf vérifie la concordance des deux textes, tout écart de fond étant un nœud de Lazar. Écarts de fond, déclarés ici avant toute donnée :
```

par :

```text
et qu'avant toute lecture un lecteur neuf vérifie la concordance des deux textes, tout écart de fond étant un nœud de Lazar ; il ajoute que « tout emploi de `moyenne` hors du bras de diagnostic est un nœud ». Ici, `moyenne` n'est employée que par des bras de diagnostic au sens de N-026 ((i), `i_sh`), mais (i) est le bras principal de la famille de Holm, alors que le fournisseur fait du maximum son bras principal (écart 1 ci-dessous). Écarts de fond, déclarés ici avant toute donnée (cinq, numérotés dans cette section ; « point n » renvoie aux « Écarts déclarés à des décisions en vigueur ») :
```

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
1. **Bras boîte blanche principal** : chez le fournisseur, W = régression sur le **maximum** par dimension à la couche 15 (C = 1), la moyenne étant un bras de diagnostic ; ici, (i) = régression sur la **moyenne**, couche choisie parmi 7, 15, 23 (λ = 10), bras de diagnostic au sens de N-026, et le maximum (`i_max`) est descriptif.
```

par :

```text
1. **Bras boîte blanche principal** : chez le fournisseur, W = régression sur le **maximum** par dimension à la couche 15 (C = 1), saboteur contre l'honnête **seul**, la moyenne étant un bras de diagnostic ; ici, (i) = régression sur la **moyenne**, couche choisie parmi 7, 15, 23 (λ = 10), saboteur contre **toutes** les autres conditions (honnête, témoin instruit, mention ; point 3), bras de diagnostic au sens de N-026, et le maximum (`i_max`, mêmes négatifs que (i)) est descriptif ; `i_sh` (moyenne, honnête seul) est descriptif ; aucun bras de ce texte ne combine le maximum et l'honnête seul.
```

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
2. **Taux de fausses alarmes** : 1 % chez le fournisseur ; 0,05 ici (écart 5).
```

par :

```text
2. **Métrique de décision et taux de fausses alarmes** : chez le fournisseur, la métrique principale est le rappel à 1 % de fausses alarmes (secondaires : 5 % et l'aire sous la courbe ROC), le niveau de lecture et le détail étant ceux de l'analyse de conv-audit ; ici, la décision porte sur la différence d'**aire d'épisode** (Holm), la puissance à 0,05 n'étant qu'un filtre de signe et une grandeur rapportée (point 6), et le taux de 1 % n'existe pas avec 60 épisodes honnêtes (point 5).
```

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
longueur en jetons ; écart 4).
```

par :

```text
longueur en jetons ; point 4).
```

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
Ce texte ne code ni ne lit les bras du fournisseur (W, G, J3s, J3g, J8s, C, T, au taux de 1 %) : le point 3 du plan du fournisseur (« Analyse (conv-audit, processeur) : bras, plancher, métriques ci-dessus, codés et scellés avant lecture ») demande un code et un préenregistrement d'analyse propres, scellés avant toute lecture, hors de ce texte.
```

par :

```text
Ce texte ne code pas les bras du fournisseur tels qu'il les définit (W au maximum, couche 15, C = 1, honnête seul ; T ; C ; J3g ; J8s ; taux de 1 % ; Bonferroni) : ses bras (ii) et (iii) lisent les mêmes colonnes que J3s et G, mais sous la règle de ce texte ; le point 3 du plan du fournisseur (« Analyse (conv-audit, processeur) : bras, plancher, métriques ci-dessus, codés et scellés avant lecture ») demande un code et un préenregistrement d'analyse propres, scellés avant toute lecture, hors de ce texte. Les autres différences de détail (niveau de lecture, quantile, nombre de tirages, forme du plancher, bras de diagnostic W aux couches 7 et 23 et hors du champ du coût, analyse de sensibilité à la restriction au contexte exact) relèvent de ce que le fournisseur confie à l'analyse de conv-audit (« Statut » ; n° 246 : « Restent chez toi : plancher apparié, prédicteur sur les traits, test « colonnes nommées seulement » de R4 ») ou de bras que ce texte ne lit pas ; elles ne sont pas détaillées ici.
```

#### F3 — R-1090 cité ; statut des deux lectures et vérification de concordance

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
**Statut des deux lectures** (décision de la session conv-audit, 2026-11-02 ; les bras ne sont pas alignés) : **l'analyse du fournisseur, scellée la première, est la lecture principale de la comparaison appariée** ; la présente analyse en est la lecture **secondaire** (diagnostic au sens de N-026, hors porte).
```

par :

```text
**Statut des deux lectures** (décision de la session conv-audit, R-1090, `registres/decisions.md` au commit `90803649`, empreinte du registre à ce commit `678b00b44015b592263ad41f1c2eb49da09ae36ffabd0bd527ad4cb4643c26bd` ; les bras ne sont pas alignés) : **la lecture définie par le préenregistrement du fournisseur, scellé le premier, est la lecture principale de la comparaison appariée** ; son analyse (code et préenregistrement d'analyse propres, fidèles à ses bras) est confiée à un texte neuf, à contre-lire et à sceller avant toute lecture ; la présente analyse en est la lecture **secondaire** (diagnostic au sens de N-026, hors porte).
```

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
la session conv-audit les porte à Lazar comme **réserve** (non comme condition du lancement).
```

par :

```text
la session conv-audit les porte à Lazar comme **réserve** (non comme condition du lancement : le texte du fournisseur dit « nœud » ; cette qualification est celle de la session, R-1090, non celle de Lazar).
```

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
La vérification de concordance par un lecteur neuf, qu'exige le fournisseur avant toute lecture, est faite à l'étape 0.g ; elle ne peut que constater les cinq écarts déclarés ; un écart de fond non déclaré suspend le lancement (nœud de Lazar).
```

par :

```text
La vérification de concordance qu'exige le fournisseur avant toute lecture est faite par un lecteur neuf à l'étape 0.g (elle porte sur l'analyse principale et, pour ce texte, sur la déclaration de tous les écarts de fond ci-dessus) ; un écart de fond non déclaré suspend le lancement (nœud de Lazar).
```

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
R-1075 (option c ; runs « qu'un expert lancerait », préenregistrés, pour les mentors) ;
```

par :

```text
R-1075 (option c ; runs « qu'un expert lancerait », préenregistrés, pour les mentors) ; R-1090 (`registres/decisions.md`, branche `canal/conv-audit-n04`, commit `90803649` ; empreinte du registre à ce commit, `git show 90803649:registres/decisions.md | sha256sum` : `678b00b44015b592263ad41f1c2eb49da09ae36ffabd0bd527ad4cb4643c26bd`) : l'analyse principale de R1-R2, fidèle aux bras gelés par le fournisseur, est confiée à un texte neuf ; celle-ci est la lecture secondaire, écarts déclarés à la section « Concordance », les deux lectures rapportées en entier, aucune citation de l'une sans l'autre ;
```

#### F4 — étape 0.g : la lecture principale est scellée avant le lancement

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
g. Avant de lancer : la vérification de concordance des deux textes scellés par un lecteur neuf, qu'exige le préenregistrement R1-R2 du fournisseur (« Statut »), est faite et consignée ; un écart de fond non déclaré à la section « Concordance » suspend le lancement (nœud de Lazar). Puis lancer
```

par :

```text
g. Avant de lancer : (1) le préenregistrement de l'analyse principale de R1-R2 (R-1090 ; texte neuf fidèle aux bras du fournisseur) est scellé : la commande ci-dessous n'est pas lancée avant ce scellement, car sa sortie porte sur les mêmes données que l'analyse principale et la lire avant serait une lecture de résultat avant scellement (règle R1) ; (2) la vérification de concordance qu'exige le préenregistrement R1-R2 du fournisseur (« Statut ») est faite et consignée par un lecteur neuf, qui n'a écrit ni ce texte ni celui de l'analyse principale ; un écart de fond non déclaré à la section « Concordance » suspend le lancement (nœud de Lazar). Puis lancer
```

#### F5 — entrée de la contre-lecture 2 : exceptions nommées et essais

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
Traitement : D1 à D18 et J1 à J7 appliquées mot pour mot dans les fichiers v3 et ce brouillon (remplacements du rapport, repris sur ses copies corrigées et relus un à un), sauf : J7, dont la recommandation finale est remplacée par la décision de la session (lecture du fournisseur principale, celle-ci secondaire, réserve portée à Lazar) ; la ligne du marqueur de D8
```

par :

```text
Traitement : D1 à D18 et J1 à J7 appliquées mot pour mot dans les fichiers v3 et ce brouillon (remplacements du rapport, repris sur ses copies corrigées et relus un à un), sauf : D1 (date de ce brouillon écrite, comme le rapport le prévoyait) ; D3 (phrase de tête complétée du n° 246 et de la lecture du kit) ; D5 (le chiffre qui porte sur « le code le plus proche du code cité », et une phrase ajoutée : les scripts de fréquence importent `lecture_v2`, non `lecture_v3`) ; D8 (étape 0.c adaptée aux deux marqueurs restants) ; D15 (la ligne de portée reçoit en plus la ligne « lecture secondaire ») ; J7, dont la recommandation finale est remplacée par la décision de la session (lecture du fournisseur principale, celle-ci secondaire, réserve portée à Lazar) ; ajouts non demandés : R-1014, d'après le n° 246 (lignes « Ce que ce texte n'est pas » et « Décisions qui fondent ce texte », point 1 des écarts déclarés) ; la ligne du marqueur de D8
```

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
S4 en partie. Détail : `rapport-redaction-v3.md`.
```

par :

```text
S4 en partie ; essais après corrections : 13 réussis (36 avec ceux de v1 et v2). Détail : `rapport-redaction-v3.md`.
```

#### F6 — étape 0.c et entrée de la contre-lecture 3 : contenu fixé

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
(la version finale committée à l'étape a : brouillon 3, corrigé selon la contre-lecture 3 s'il y a lieu)
```

par :

```text
(la version finale committée à l'étape a : brouillon 4, brouillon 3 corrigé selon la contre-lecture 3)
```

Dans `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md` (le brouillon 4 est cette copie corrigée, sous le nom `…-brouillon4.md`), remplacer :

```text
2. ligne « Contre-lecture 3 » : « sous-agent neuf (Claude), qui n'a écrit ni ce texte, ni le code, ni les calculs, ni les contre-lectures 1 et 2 ; brouillon relu : `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md`, sha256 `<empreinte du brouillon relu>` ; rapport : `<chemin du rapport>`, sha256 `<empreinte du rapport>` ; verdict « <verdict> » ; corrections : <liste, chacune appliquée ou non avec son motif> ; essais après corrections : <n> réussis », les `<…>` remplacés par leurs valeurs, rien d'autre ; si la contre-lecture 3 demande une correction, elle se fait avant l'étape 0.a et le texte corrigé est un brouillon 4 (R12).
```

par :

```text
2. ligne « Contre-lecture 3 » : le marqueur, accents graves compris, est remplacé par : « sous-agent neuf (Claude), qui n'a écrit ni ce texte, ni le code, ni les calculs, ni les contre-lectures 1 et 2 ; brouillon relu : `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon3.md`, sha256 `addadee095efccf1fadbbc0306bca131bb5bd07f216fec80988a48d0ea9222f3` (commit `c67d7a6f`) ; rapport : `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/contre-lecture-3-preenregistrement-analyse-v1.md`, sha256 `<empreinte du rapport>` ; verdict « scellable après corrections mineures (listées) » ; corrections F1 à F6 appliquées mot pour mot dans le brouillon 4 (code et essais inchangés) ; essais après corrections : <n> réussis », les deux `<…>` remplacés par leurs valeurs, rien d'autre (une correction non appliquée est nommée avec son motif dans cette entrée, avant l'étape 0.a). Le texte scellé est le brouillon 4, brouillon 3 corrigé par la contre-lecture 3 (R12).
```

#### G1 — facultative (non bloquante) : script de fréquence rejoué sur v3

Dans le même fichier, remplacer :

```text
; ils ne sont pas rejoués sur v3.
```

par :

```text
; la contre-lecture 3 a rejoué `frequence-regle-decision-v2.py` sur les modules v3 (copie hors du dépôt, trois importations remplacées, même entropie) : sortie identique à la sortie citée, hors la durée ; le script v1 n'a pas été rejoué.
```


## Traçabilité (scripts du relecteur, hors du dépôt)

Dossier : `/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/cl3-bn/`.

- `corrections_cl3.py` : les corrections F1 à F6 (et G1) sous forme (identifiant, ancien, nouveau) ; contrôle que chaque « ancien » figure une fois et applique tout à `brouillon4-essai.md` (copie hors du dépôt) ; `rendre_rapport.py` produit la section « Textes de remplacement » ci-dessus à partir de ce fichier.
- `verif_code.py` : les 101 remplacements « code » de la contre-lecture 2 appliqués au code v2 commité (`b621ad69`) : empreintes égales à celles de la section I. `verif_textes.py` : les 48 remplacements du brouillon contre la copie corrigée et contre le brouillon 3. `fonctions.py` : comparaison par arbre syntaxique des fonctions et constantes entre le code v2 commité et le code v3 renommé en v2.
- `rejeu_frequence_sur_v3.py` et sa sortie : le rejeu de la section 5. `essais-v3.log`, `essais-v1v2.log` : sorties des essais (section 6).
- Empreintes (sha256) :
- `corrections_cl3.py` : `8d263b02506dff1a9cc4a1daf8e43aeb8d66c34be1cca6171ee8d320d4164f1d`
- `verif_code.py` : `8fa240e3e98ac086d905b9cfc67f6c90349a3d81db68f8f8a1599aceeaa1f44e`
- `verif_textes.py` : `b17c7ff701381177c7868237281072a896dd9b0ac2569c75318e0c7a1b42aca3`
- `fonctions.py` : `f05e27e231d6c8970664f9ea320fdfc9353df69796d4ea8292cb14c2c7e2bdef`
- `rejeu_frequence_sur_v3.py` : `774ec9fb8d6ef657d2e1860ab9de7d340c6659c765e54611ae609c7f9b08448b`
- `rejeu_frequence_sur_v3-sortie.txt` : `7b2d1a7be90c7945f8af1c14a44c907543ef8a8a96ada84d6a69c3172fe54f87`
- `essais-v3.log` : `4fcbbb2e190042c82365e05fb1a8607da52859c66f301e9a6ca1bf3e7eb9d928`
- `essais-v1v2.log` : `6f5efc2b52e6828169da89e00692eb95cb5cb7675b9f7ea277eb60299faf9be8`
- Vérifications git en lecture seule : `git show 7b0ef14f:registres/decisions.md`, `git show 567260c05687747f0c7a715fc9b15b4fc6297d65:<chemin>` (LISEZMOI v2, R1-R2, R4), `git show origin/canal/session-depot-reprise-n73:…n246.md`, `git show 90803649:registres/decisions.md | sha256sum` (→ `678b00b4…`), `git log`, `git cat-file -t`.
