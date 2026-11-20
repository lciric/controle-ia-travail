# Vérification du code du palier 0b, version 5 (préenregistrement v11) — v1

- Vérificateur, modèle S (neuf : il n'a écrit ni le texte, ni le code v1 à v5, ni leurs vérifications). Pièce de travail (classe C) rendant un avis sur une pièce d'instrument (classe B). Travail du 2026-11-20.
- Mandat : `heritage/palier-0b/mandat-verificateur-code-palier-0b-v5-v1.md` (`749b0e5d503e146245d834d0f7219b113d098c06e6fdb88de127f1538854f83b`), empreinte vérifiée par `env -C` avant tout geste. Chaque pièce qui fait foi a été vérifiée contre son compagnon : mandat du développeur (`6d099bfc…`), texte v11 (`9faf31a3…`), contrôle v10 → v11 (`88c37d86…`), table (`56bddae7…`), vérification du code v4 (`183b17d2…`), rapport du développeur du code v5 (`a2966a3c…`) : tous « OK ».
- Environnement : Python 3.13.18, `.venv` du dépôt. Les essais et le banc se jouent sur une copie du dossier du code v5 (bloc-notes), avec `PYTHONPATH=src` et les deux variables que les essais exigent et que le mandat ne cite pas : `HERITAGE_DEPOT` (racine du dépôt) et `HERITAGE_COPIE_ORGANISME` (le dossier `orchestrator/` de `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/`, lu sans écriture). Sans elles, les essais échouent par construction (aides, règle R5). Un premier lancement sans elles a été arrêté par son identifiant et refait.

## 0. Verdict

**Conforme.** Aucune correction exigée. Table et compagnons exacts ; différentiels v4 → v5 limités aux points 1 à 6 et à NE-3 ; code lu contre la lettre du texte v11 sans écart ; suite entière 107 passés ; banc 113 sur 113 vus ; sorties 484 égales sur 489, les 5 qui changent relèvent chacune d'une règle changée. Seize silences : tous justes ; quatre sont à porter à la mère (n° 8, 14, 15, 16) et le reste à inscrire par l'erratum. Deux ajouts facultatifs à la liste de l'erratum (§ 6).

## 1. La table (point 1 du mandat)

- `env -C code-v5 sha256sum -c ../table-empreintes-code-v5.txt` : 58 lignes, 58 « OK » (24 sous `outils-dev/`, 24 sous `src/`, 10 sous `tests/`).
- Compagnons : un contrôle par fichier (outil de ma pièce, `verifier_compagnons.py` : une seule ligne « <empreinte>  <nom de base> », empreinte recalculée) : 59 fichiers (les 58 et le rapport), 0 mauvais, 0 sans compagnon, 0 orphelin.
- La table elle-même (`56bddae7…`) est égale à celle que le rapport annonce.

## 2. Les différentiels v4 → v5 (point 2)

`diff -rq code-v4 code-v5` : seuls diffèrent ou sont neufs, hors rapports :
- `src/` : `audit.py`, `constantes.py`, `etapes.py`, `graines.py`, `mecanique.py`, `mondes.py`, `tirages.py` (sept) ;
- `tests/` : `etapes`, `mondes`, `outils`, `statistique` changés, `verrou` neuf ;
- `outils-dev/` : `mutations_v4.py` neuf et ses deux sorties neuves.
Les 40 autres fichiers (dont `etalonnage.py`, `analyse.py`, `proposeurs.py`, `statistique.py` de `src/`) sont à l'octet ceux du v4. Les `diff -u` des sept modules et de trois fichiers d'essais ont été faits et lus (dans `diffs/` de mon bloc-notes) : chaque hunk relève d'un des points 1 à 6 ou de NE-3 ; aucun changement hors liste (les seuls hunks de forme sont des docstrings).

## 3. Le code contre la lettre du texte v11 (point 3)

- **Seuil d'arrêt** (`audit.lecture`, `seuil_d_arret`, `seuil_calibre`) : forme des trois audits des doses : A au plus 0,55 → tenue ; A au-dessus de 0,55 et de M + 2 σ₀ → arrêt ; au-dessus de 0,55 et au plus M + 2 σ₀ → « non départagée », avec mention. Seuil d'arrêt = `max(0,55, M + 2 σ₀)`. « Au plus » inclusif (`<=`, `>` strict), égalité éprouvée. Conforme à la section « Seuil » et au point 1 (version 11).
- **Zone médiane du contenu et des réunis** : `lecture` rend `NON_DEPARTAGEE`, rangée dans `non_departagees_sans_mention`, hors de la liste qui pose la mention ; `mention = MENTION si (signalement ou non_departagees de forme)` : une exactitude de contenu ou réunie de la zone ne pose ni signalement ni mention. Au plus 0,55, même au-dessus de M + 2 σ₀ : « au plus 0,55 », ni signalement ni mention. Conforme au point 2 et à la remarque 2 (lecture (i)).
- **Audits de lois** : forme au-dessus de 0,55 → arrêt ; contenu et réunis au-dessus de 0,55 → signalés avec mention, sans calibrage ; seuil d'arrêt 0,55 (forme), `None` (contenu, réunis). Conforme.
- **NE-3** : colonne `seuil_d_arret` à la table, plus grand de 0,55 et de M + 2 σ₀ pour la forme des doses ; `seuil_calibre` = M + 2 σ₀ pour les quinze. `lire_audit` exige A, σ₀ et M (refus sinon). Conforme au texte NE-3 du contrôle (§ 5).
- **Plis** : `generateurs_de_l_audit` dérive `role=plis` puis `role=permutation`, un seul de chaque ; `juger_suites_d_audit` et `audit_du_generateur` n'ont plus aucun paramètre générateur. Conforme au point 3 et au paragraphe « Précisions de la version 9 ».
- **Verrou** (`graines.Autorisation`) : (a) texte et pièce scellés au sens du dépôt (réécriture confrontée au module du dépôt sur neuf cas) ; (b) empreinte du texte recalculée, commit pris de la seule ligne « - Commit du code d'analyse : », GO dans la première colonne de `registres/go.md`, heure UTC en forme seule ; (c) quatre lignes « nom : valeur » dans l'ordre de R-4123 ; chaque module lancé comparé à la table et la table ne nomme sous `src/` aucun module non lancé ; (d) « sur `main` » non contrôlé (la mère en répond) ; (e) manifeste : trois champs, nuls ensemble hors couche décisive, `preenregistrement_sha256` refusé. `PREENREGISTREMENT_SHA256` retirée, en-tête de `constantes.py` corrigé. **Revérification** : `tirages.exiger_autorisation_pour` rappelle `autorisation.verifier()` au début de `lancer_famille`, avant toute simulation. Conforme au point 4 et à la remarque 4.
- **Compatibilité avec le texte réel** (contrôle ajouté par moi, sans tirage) : `lire_en_tete_du_texte` appliquée au texte v11 tel qu'il est (`lire_entete_reel.py`) lit le commit de l'en-tête (`3d332d2c…`) et une table de 51 lignes dont 24 sous `src/`, et `modules_lances()` rend 24 modules : la forme que le verrou exige est bien celle de l'en-tête existant ; l'erratum n'a qu'à remplacer la ligne et le bloc.
- **`lancer_etape_4` et garde 27 à trois sources** : `lancer_etape_4` joue `etape_4` (`bras-1-a-3/`) puis `etape_4_jeu_de_la_garde_27` (`jeu-de-la-garde-27/`), mêmes graines et même couche, lecteur réglé pour la tenue au réglage de l'étape 4 (τ = 2), trois sources, dose 0,25 ; ni proposeur ni nombre de sources en paramètres. `suite.etrangere` posée à la construction, `verifier_etrangeres_du_jeu` arrête si ce n'est pas la source suivante ; `verifier_source_etrangere` avant les bras 4a et 4b arrête si le dépôt ne vient pas de cette source. Conforme à la remarque 3 et à la garde 27 (registre de la source précédente servi : arrêt).
- **NE-3 dans les essais** : `_verifier_table` contrôle sur chaque table tirée l'équivalence « arrêt » ⇔ A au-dessus de `seuil_d_arret` pour la forme.

## 4. Essais et banc rejoués (point 4)

- **Suite entière**, un processus, tâche de fond : **107 passés, 0 échoué** (1 731 s, machine chargée). Compte égal à l'attendu ; l'essai « aucune graine décisive » est dans cette suite et passe.
- **Banc `mutations_v4.py`**, en deux parties parallèles (`--partie v3` et `--partie v4`), chacune jouant d'abord ses témoins : partie « v3 » : témoins au vert, **71 défauts appliqués, 71 vus** ; partie « neufs » : témoins au vert, **42 appliqués, 42 vus** ; **113 sur 113**. Chaque défaut est vu par un essai de code 1 (aucun code 2 ou plus, donc aucune erreur de collecte) ; les seuls codes 0 sont les témoins sur code sain.
- **Ce qui manque au banc** (sans effet sur le verdict) : (i) aucun défaut dédié à « la mention n'est plus posée par une exactitude de forme non départagée » ; je l'ai posé à la main dans une copie (`mention … si signalement else None`) : `test_garde_25_lecture_calibree_sur_valeurs_plantees` échoue, donc l'essai le voit, mais le banc ne le liste pas ; (ii) aucun défaut sur la tolérance des formes d'heure ni sur les blancs de la pièce (`lire_piece`) ; ils sont couverts par les artefacts du verrou, non par un défaut nommé. À ajouter à un banc v5, facultatif.

## 5. Les sorties v4 → v5 (point 6)

J'ai rejoué l'outil d'empreintes du développeur (un processus par paquet, v4 du dépôt et v5 de ma copie) puis son comparateur : **484 égales, 5 différentes, 0 seulement dans un paquet**, les cinq mêmes empreintes que le rapport :
- `audit/presentation/table` et `audit/presentation/lecture` : points 1, 2 et NE-3 (colonnes, listes, lectures) ;
- `etape_3/derivation` : point 3 (générateurs dérivés par l'étape, deux rôles) ;
- `etape_3/rapport/exactitudes` : point 3 (les plis viennent du rôle « plis » ; même valeur que `audit_presentation` nourri des deux générateurs, ligne `exactitudes_aux_generateurs_plis_et_permutation` égale) ;
- `tirages/manifeste_sans_versions` : point 4, (e).
Chacune relève d'une règle changée ; rien d'autre ne bouge (couche statistique, générateur, mécanique, jeu de la garde 27 à deux et trois sources : égaux à l'octet).

## 6. Les 16 silences déclarés (rapport § 2) et la liste de l'erratum (rapport § 6) (point 5)

| n° | objet | jugement |
|---|---|---|
| 1 | noms des quatre champs, forme « nom : valeur » | juste ; à inscrire (B8, remarque 4) |
| 2 | formes de l'heure | juste ; à inscrire. Précision à y mettre : `strptime` ne contrôle pas le jour de la semaine et tolère des nombres non remplis par un zéro ; « forme seule » le permet |
| 3 | forme de l'identifiant du GO | juste ; à inscrire |
| 4 | lecture de l'en-tête du texte | juste, et éprouvée sur le texte v11 réel (§ 3) ; à inscrire |
| 5 | « chaque module du code lancé » | juste ; à inscrire |
| 6 | « scellée » réécrit, confronté au dépôt | juste ; à inscrire |
| 7 | moment des vérifications | juste ; à inscrire. Limite à dire : la graine d'une couche décisive dérivée directement par `Graines.g` (hors `lancer_famille`) n'est pas revérifiée sur disque |
| 8 | manifeste : noms, nul ensemble ; GO et commit de la pièce non inscrits | juste pour les noms. **À la mère** : le champ `commit` du manifeste est donné par l'appelant et n'est comparé ni à celui de la pièce ni à celui de l'en-tête ; l'accord des modules avec la table tient lieu de contrôle du code (remarque 2 du rapport) ; décider si cela suffit |
| 9 | colonne du seuil d'arrêt hors des doses (0,55 pour les lois, `None` pour contenu et réunis) | juste (lecture fidèle à « n'arrêtent jamais ») ; à inscrire avec NE-3 |
| 10 | mots de la zone médiane | juste ; à inscrire |
| 11 | ordre et lieu de la dérivation | juste ; à inscrire (l'ordre des étiquettes est plis puis permutation ; il ne change aucune graine, les clés dépendant de l'étiquette seule) |
| 12 | programme de lancement de l'étape 4 | juste ; à inscrire |
| 13 | garde 27 : ce qui est comparé | juste ; à inscrire. Limite à dire : la comparaison est d'identité d'objet de la source ; l'intégrité de la copie déposée reste portée par les contrôles d'empreinte existants |
| 14 | racine de l'arbre et texte présentés | **à la mère** : à fixer au lancement des étapes 8 et 9 (aucun programme de lancement n'existe encore) |
| 15 | « sur `main` » | **à la mère**, comme la remarque 4 (d) le dit |
| 16 | les couches non décisives ne sont pas verrouillées | **à la mère** : le point 1 de la liste d'arrêt les interdit tant que l'erratum n'est pas contre-lu, ce que nul programme ne vérifie |

**Liste de l'erratum du commit** (§ 6 du rapport, neuf points) : juste et complète pour ce que le rapport et le texte demandent ; chiffres vérifiés (58 lignes, 24 fichiers sous `src/` dont 23 du paquet et `src/controle_ia/__init__.py`). Deux ajouts utiles, non exigés :
- à l'inscription de la ligne « Commit du code d'analyse » : l'erratum doit remplacer la ligne et le premier bloc « ``` » qui la suit, et aucune autre ligne du texte ne doit commencer par `- Commit du code d'analyse : ` (le verrou refuse s'il y en a deux) ; le bloc ne doit pas contenir le rapport ;
- aux points 3 et 5 : dire la clé neuve `non_departagees_sans_mention` du rapport de l'audit, la valeur `null` de `seuil_d_arret` pour le contenu et les réunis, et les clés rendues par `lancer_etape_4` (`frequences`, `comptes`, `garde_17`, `jeu_de_la_garde_27`).

## 7. Écarts, gestes

- Écart au mandat : les deux variables d'environnement des essais (§ « Environnement »), ajoutées au lancement ; sans elles les essais échouent par construction. Un premier lancement les ignorait ; il a été arrêté par son identifiant de tâche et relancé.
- Outils écrits dans mon bloc-notes seulement : `verifier_compagnons.py`, `lire_entete_reel.py` ; j'ai aussi relancé, sans les modifier, l'outil d'empreintes et le comparateur du développeur (lus en place) et posé une copie mutée à la main (`mut1/`, à la fin du § 4).
- Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille ; aucun appel à un fournisseur de modèles, aucune dépense ; aucune écriture dans le dépôt, aucun commit ; rien sous `archives-reponses-modeles/` ni `/root/.claude/` ; aucun refus de permission, de classifieur ni de garde.

Vérificateur, modèle S.
