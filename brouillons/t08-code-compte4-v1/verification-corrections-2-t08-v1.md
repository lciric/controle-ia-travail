# Vérification de la seconde passe de corrections du code de T0.8 — v1

## 0. Identité

- **Rôle** : vérificateur de la seconde passe de corrections du code de T0.8, sous-agent de la session du compte 4, **modèle B** ; je poursuis la vérification courte (`brouillons/t08-code-compte4-v1/verification-courte-corrections-t08-v1.md`, `d12df4bd27f9…`), que j'ai écrite. Je n'ai écrit ni ce code, ni ses corrections, ni T0.8, T0.6, T0.7 ou P3-bis. Je ne corrige rien.
- **Heures** (`date -u`, relevées par la machine et insérées par programme) : premier relevé gardé sur disque 2026-11-14T03:34:12Z (lancement des essais, après la vérification des empreintes) ; fin 2026-11-14T03:46:12Z (relevée dans la commande qui a écrit ce fichier, avant le scellement).
- **Consigne** : `brouillons/t08-code-compte4-v1/consigne-verification-corrections-2-t08-v1.md`, `936f605b4ad1e3b6488c92277c1ea611594bb102c5ee8f0ee6b59f82ca1abab4` (`scellement verifier` : OK), lue en entier ; elle garde les interdits de la consigne précédente (`31c65716…`).
- **Code vérifié** : arbre `/home/user/t08-code-compte4-v1`, tête `453a71e1c6729d7ec5d43e3a4a0e3522dfd38579`, arbre de travail sans modification avant et après mes essais ; `git diff --quiet 47b20451 453a71e1 -- src/controle_ia/t08 tests` rend 0 (code et essais figés depuis `47b20451`). Renvois « fichier:ligne » à la tête.
- **Script** : `brouillons/t08-code-compte4-v1/verification-corrections-2-t08-v1-calcul.py`, `8acc080b346df3e04358f117c5a12b604c36a5ddcff861864387e85b056ca543` ; sortie recopiée à l'octet au § 6.3.

| fichier | empreinte vérifiée | parties lues |
|---|---|---|
| `brouillons/t08-code-compte4-v1/consigne-developpeur-corrections-2-t08-v1.md` | `dccd725f93e9…` (égale) | en entier |
| `registres-provisoires/compte-4-2026-11-14-v6.md` | `4029099988dd…` (égale) | en entier (C4-0036 à C4-0038) |
| `docs/notes/t08-code-compte4-v1/rapport-developpeur-corrections-2-t08-v1.md` (arbre) | `6803a5271bba…` (égale ; `scellement verifier` : OK) | en entier |
| différentiel `7a4d4e13..453a71e1` de `src/controle_ia/t08/` (658 lignes) | les sept empreintes du § 2 du rapport, recalculées : 7 sur 7 égales | en entier |
| différentiel des essais (592 lignes) | (mêmes empreintes) | noms des essais neufs ; `test_passage_a_blanc_cas_sain_et_artefacts` et les fabriques du comparateur, en entier ; le reste éprouvé par mutations |
| `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` | `7da0c383…` (vérifiée à la vérification courte ; relue par le script, A1) | l. 175, 176, 370 (en plus des lignes lues à la vérification courte) |
| code importé (arbre) | non recalculées | `manifeste.py` l. 119-131 (`lire_manifeste`) ; `harnais/validation_reelle.py` l. 71-73 |
| sorties factices de l'essai v3, `essai/t08-jouet-compte4-v3/a/` et `…/b/` (arbre) | comparées par programme (§ 4) | `lecture-t08.json` de `a/` (tables, fichiers ouverts, écarts, étapes) ; tous les fichiers des deux racines comparés à l'octet, les onze non identiques par leurs clés |

**Accès mécaniques déclarés.** Pour le point 6 de la consigne : `git rev-parse HEAD`, `git status --short` (vide), `git status --short --ignored` sur `essai/t08-jouet-compte4-v3` (deux dossiers `donnees/` ignorés), et `git diff --name-only` entre `47b20451`, `8c398190` et `453a71e1` sur les chemins gelés de `harnais/validation_reelle.py` (noms réduits à leurs dossiers par programme : seuls des dossiers de `essai/t08-jouet-compte4-v3/` et `docs/notes/t08-code-compte4-v1` ont été affichés). Les messages des essais d'inventaire sont comptés par programme, sans afficher de nom d'autrui. Le script copie `src/controle_ia/t08/`, les huit fichiers d'essais de T0.8 et `tests/conftest.py` dans le bloc-notes, avec trois liens vers `docs/`, `prereg/` et `brouillons/` de l'arbre ; il importe, pour ses sondes, les fabriques du fichier d'essais `test_t08_gardes_corrections_v1.py`. Aucun fichier de `registres/`, de P3-bis ni de T0.7 ouvert ; rien de `donnees/`, `diag/` ou `runs/` réels ; aucun appel réseau ; aucun sous-agent ; aucune écriture git ; aucun refus de permission, du crochet ni d'un classifieur ; l'essai de bout en bout n'est pas rejoué.

## 1. Verdict

**Citable par le texte candidat tel quel** : la tête `453a71e1` peut être citée par `COMMIT_CODE_T08`. VCT8-01 à VCT8-07 sont corrigés (6 « corrigé », 1 « corrigé avec réserve », 0 « non corrigé ») ; 22 mutations sur 22 font échouer leur essai ; 142 essais de T0.8 réussis ; inventaires inchangés ; phrases gelées égales (15 sur 15) ; déterminisme : 0 différent, retrouvé.
Constats neufs : **0 bloquant, 0 majeur, 3 mineurs**, dont aucun ne demande de changer le code avant de le citer.
Restent à la mère, hors du code : nommer ou confirmer l'entrée `manifeste_course` (Q-D2), fixer la forme de la ligne `CODE-T08` et jouer le passage à blanc sur le registre réel avant la course, éprouver la garde de l'instance sur le clone réel (§ 2, « Commit citable »).

## 2. Constats neufs

- **VCT8B-01 — mineur — l'entrée `manifeste_course` n'est pas nommée par le point 1 du plan (question Q-D2).** *Endroit* : `lecture_v1.py:105` (entrée requise), `:244-246` ; `entrees_v1.py:216-226` ; `essai_jouet_v1.py:91`. *Texte* : l. 176 : « **Données lues, et seulement elles** (liste blanche ; tout autre chemin est refusé par le code […]) », suivie des fichiers de 7b, de la pièce « mots et coût », de la pièce HD, des tâches et des consignes ; l. 184 : « manifeste par run (`controle_ia.manifeste`) ». *Analyse* : c'est un écart à la **lettre** de « seulement elles », sans portée sur le fond : (i) le fichier est une sortie de la course de T0.8 elle-même, comme `course-t08.json` et les six fichiers de la course que la lecture lit depuis la première version sans que le point 1 les nomme ; (ii) il ne porte aucune donnée de 7b, aucune sonde, aucun résultat (configuration, graines, commit, date) ; (iii) le lecteur n'en garde que l'identifiant du run, l'empreinte et `cree_le` ; (iv) il est rattaché à `course-t08.json` par l'empreinte de l'enveloppe (N12 tuée) ; (v) aucun motif interdit. Sans lui, l'antériorité ne peut être prise que sur la fin de la course (VCT8-03). *Gravité* : mineur. *Suite* : **à confirmer par la mère** ; le plus net est que le texte candidat, avant son scellement, nomme parmi ce que lit la lecture les sorties de la course de T0.8, manifeste compris (une phrase au plan, point 1 ou 5) ; ce n'est ni un seuil ni une règle de lecture, donc pas un nœud à mes yeux. Aucun changement de code.
- **VCT8B-02 — mineur — `ligne_cite_commit` accepte une ligne `CODE-T08` qui porte deux commits.** *Endroit* : `entrees_v1.py:338-347`. Script, C3 : une ligne dont la quatrième cellule est un **autre** commit et dont la cellule « chemin » porte le commit du marqueur est tenue pour citer le marqueur. Par ailleurs (sans gravité : refus visibles dès le passage à blanc) : un commit écrit en majuscules, abrégé, ou une clé entre accents graves ne sont pas reconnus. *Correction*, si la mère la veut : quand la quatrième cellule est un commit, exiger qu'elle soit celui du marqueur ; essai : l'artefact de C3. Sinon : fixer une seule forme (Q-D1) et le déclarer.
- **VCT8B-03 — mineur — passage à blanc : trois détails.** *Endroit* : `lecture_v1.py:145-181`. (a) Un registre absent du disque lève `FileNotFoundError`, non `GardeArret` (script, C4) : le passage s'arrête bien, mais autrement que ne le dit sa documentation. (b) Le paramètre `maintenant` permet de donner l'heure à la main (utile aux essais) : la mère l'appelle **sans** ce paramètre (heure de la machine). (c) Les lignes d'une autre forme dont la clé n'est pas reconnue (en-tête « clé » en minuscules, clé entre accents graves) sont rendues dans `registre.mal_formees` sans arrêter (script, C4) : la mère lit cette liste ; une ligne `GEL-T08` ainsi écrite ne serait pas lue par la pièce HD. Aucun n'empêche de citer.

**Commit citable (point 6 de la consigne).** `exiger_code_au_commit` (`course_v1.py:61-68`) compare le commit cité à la tête sur `CHEMINS_GELES` (tout l'arbre hors `prereg`, `brouillons`, `registres`, `docs`, `diag`, `runs`, `donnees`, `livrables`, `papiers`, `traces`, `CLAUDE.md` **à la racine**).
- Entre `8c398190` et `453a71e1`, aucun fichier des chemins gelés ne change (0 nom ; les douze fichiers changés sont sous `docs/notes/t08-code-compte4-v1`) ; entre `47b20451` et `8c398190`, seuls des fichiers de `essai/t08-jouet-compte4-v3/` changent (60 noms, chemins gelés : `essai/` n'est pas exclu, ni ses sous-dossiers `prereg`, `runs`, `diag`, qui ne sont pas à la racine).
- Donc : **oui**, `453a71e1` est citable, et une instance qui clone cette branche à cette tête passe ce contrôle (commit cité = tête). Citer `47b20451` serait refusé ; `8c398190` passerait aussi. Toute tête ultérieure passe si elle ne change que des dossiers exclus de la racine (les entrées de la liste blanche et les sorties y sont toutes) ; un commit de plus sous `essai/`, `tests/`, `src/` ou `scripts/` la ferait refuser. Même condition pour la lecture, là où la mère la joue.
- **Non vérifiable ici, à éprouver par la mère sur le clone réel** : (i) la tête distante de la branche (aucun réseau) ; (ii) la garde `exiger_instance_sans_interdits` (antérieure à ces passes, inchangée), qui refuse tout fichier **ou objet git** nommé `resume.json` ou `lecture-sondes-t06*` dans la copie de l'instance, historique compris : je ne peux pas lister les noms de l'historique de cette branche (recherche récursive interdite) ; si la branche du code, tirée de `main`, en porte un, la course réelle s'arrêtera avant tout calcul, quel que soit le commit cité. À jouer à blanc sur un clone fait comme celui de l'instance (ce contrôle est sans effet sur le choix du commit).

## 3. VCT8-01 à VCT8-07 revus

« tuée » : la mutation fait échouer l'essai nommé (script, D).

| constat | classe | endroit à la tête | essai sain et artefact ; mutations |
|---|---|---|---|
| VCT8-01 (majeur) | **corrigé** | `lecture_v1.py:886-905` (`ecarts_balises_imposees`), `:933-936` (réserve décidée sur `apres_troncature`), `:663` (écarts écrits aux descriptifs) | `test_reserves_masses_et_troncature` (bord de 10 points sur la grandeur de la lettre), `test_reserve_troncature_a_la_lettre_cas_c3` ; script, C1 : les deux cas de la vérification courte rendent ce que veut la lettre ; N01 et N02 tuées |
| VCT8-02 | **corrigé** | `essai_jouet_v1.py:176-189`, `:192-202`, `:205-253` ; en-tête `:10-17` ; règles déclarées dans la sortie | `test_comparateur_lecture_exclusion_declaree_et_controle_des_tables` ; N03, N04, N05 tuées ; essai v3 : 0 différent (§ 4) |
| VCT8-03 | **corrigé avec réserve** | `lecture_v1.py:111-142` (`controles_texte_et_registre`), `:145-181` (`passage_a_blanc_reel`), `:210-217`, `:244-246` ; `entrees_v1.py:216-226`, `:268-270`, `:338-347` | `test_registre_code_t08_forme_du_commit`, `test_controles_texte_et_registre_bornes`, `test_passage_a_blanc_cas_sain_et_artefacts`, `test_etape_a_mode_reel_cas_sain_et_artefacts`, `test_etape_a_artefacts_des_entrees` ; N06 à N14 tuées ; réserves : entrée `manifeste_course` (VCT8B-01), ligne à deux commits (VCT8B-02), détails du passage à blanc (VCT8B-03) ; forme des lignes à fixer par la mère (Q-D1) |
| VCT8-04 | **corrigé** (selon C4-0037 : limite déclarée) | `configuration_v1.py:260-268` (documentation) ; rapport, § 6 ; aucun changement de code | sans objet |
| VCT8-05 | **corrigé** | `temoin_distille_v1.py:146-148` (tout état autre que « présent » : « non lue (…) », registre non lu) ; `:196-198`, `:283-285` (formes de 7b absentes : arrêt) | `test_hd_registre_du_texte_de_validite_non_present_non_lu`, `test_hd_formes_de_7b_absentes_arretent` ; script, C2 ; N15 et N16 tuées |
| VCT8-06 | **corrigé** | essais seuls | `test_course_reelle_manifeste_7b_d_un_autre_run`, `test_course_jouet_premiere_action_egale_a_celle_de_h_arrete`, `test_echangeabilite_hors_bornes` (0,39 ; 0,40 ; 0,60 ; 0,61 ; absente) ; N17 (M35), N18 (M38), N19 (M61), N20 tuées |
| VCT8-07 | **corrigé** | `lecture_v1.py:279`, `:838-841`, `:861`, `:881-883` | `test_fichiers_ouverts_sans_repetition`, `test_lecture_complete_cas_sain` ; N21 et N22 tuées ; essai v3 (a) : 22 fichiers, 22 distincts, 17 à l'étape (a) (script, A2) ; nombres du rapport justes |

**Défauts neufs cherchés dans le différentiel** (critères de la vérification courte) : aucune garde retirée ou affaiblie (le contrôle du texte réel est déplacé, dans l'étape (a), après la lecture de `course-t08.json` et du manifeste de la course ; l'absence de texte reste refusée en tête d'étape ; rien n'est écrit avant) ; aucun repli silencieux neuf (une clé absente des comptes lève `KeyError` ; formes absentes : arrêt) ; aucun `try`/`except` neuf ; aucune fuite de `cibles` (aucun changement du côté des juges ni de la course) ; aucun appel réseau ni lecture de clé ; aucune moyenne ni médiane sur les jetons ; phrases gelées inchangées (`tables_v1.py` n'est pas dans le différentiel ; 15 sur 15 égales) ; aucun seuil ni règle de lecture autre que ceux du texte (la réserve « troncature » suit maintenant la l. 229). Les trois constats du § 2 sont tout ce que j'ai trouvé.

## 4. Déterminisme

Essai v3, `a/` contre `b/` (script, B), sans rien écrire dans l'arbre :
- **comparateur corrigé** : 52 fichiers ; 41 identiques à l'octet ; 4 égaux sur le contenu (`course-t08.json`, `tables-d-f-t08.json`, `lecture-t08.json` hors la clé exclue, registre factice hors la ligne `COURSE-T08`) ; 7 exclus ; **0 différent** ; contrôle des tables vrai dans chaque racine ; cinq règles déclarées dans la sortie : nombres du rapport retrouvés ;
- **contrôle indépendant du comparateur** : mêmes listes de fichiers ; 41 identiques à l'octet ; les 11 autres : les deux manifestes de T0.8 (seule clé différente : `cree_le`) et leurs compagnons ; les trois diagnostics (enveloppe : `manifeste_sha256` seule ; `resultat` : aucune clé, sauf `tables_D_F_fichier.sha256` dans `lecture-t08.json`) et leurs compagnons ; le registre factice (ligne `COURSE-T08` seule) ;
- **exclusion déclarée** : la seule clé `tables_D_F_fichier.sha256` ; `chemin` et `contenu_sha256` égaux (`e7f8045665a0…` des deux côtés) ; **dans chaque racine**, l'empreinte citée est celle du fichier des tables sur disque (`a` : `1a4741f99bcf…` ; `b` : `b9cbfa9245ab…`) ; le comparateur éprouvé par mutations (N03 à N05 tuées).
Le déterminisme est établi au sens demandé : à même entropie, toutes les données sont identiques à l'octet et tous les contenus égaux ; seul diffère ce qui porte la date de création d'un manifeste.

## 5. Questions Q-D1 à Q-D7

| question | le texte tranche-t-il ? | classe |
|---|---|---|
| Q-D1, deux formes lues pour `CODE-T08` | l. 9 : la ligne « cite » le commit « avant toute exécution » ; forme non fixée | **choix à confirmer par la mère** : compatible et strict (commit égal au marqueur) ; fixer une forme avant le scellement, l'éprouver par le passage à blanc ; ligne à deux commits : VCT8B-02 |
| Q-D2, entrée `manifeste_course` | l. 176 : « Données lues, et seulement elles » ; le fichier n'y est pas nommé (ni les autres sorties de la course) | **choix à confirmer par la mère** : écart à la lettre, sans portée sur le fond, mineur (VCT8B-01) ; à lever par une phrase du texte candidat ; pas un nœud à mes yeux |
| Q-D3, passage à blanc (heure de la machine ; `COURSE-T08` déjà inscrite : arrêt ; `LECTURE-T08-BASE-A` non exigée) | non (procédure de la mère) | **choix à confirmer par la mère** : plus strict que le texte, sans effet sur une lecture ; détails : VCT8B-03 |
| Q-D4, registre du texte de validité : tout état autre que « présent » rend « non lue » | l. 179 : registre « lu, jamais écrit » ; l. 193 : « non lue (<motif>) » | **conforme au texte** ; plus strict (un registre déclaré scellé, même conforme, n'est pas lu) : à savoir par la mère en écrivant la configuration (`scelle: false`) |
| Q-D5, réserve calculée pour les quatre juges-surveillants | l. 229 : « pour un juge » | **conforme au texte** (une lecture en une passe n'impose aucune balise : écarts nuls) |
| Q-D6, `contenu_sha256` vérifié aussi dans chaque racine | sans objet | **conforme au texte** (contrôle plus fort) |
| Q-D7, arrangements de l'essai de la course réelle | sans objet | **conforme au texte** : arrangements d'essai déclarés ; la garde visée est bien éprouvée (N17 tuée) |

Restent à la mère, inchangées : Q-C2, Q-C3, Q-C6, Q-1, Q-2, Q-4.

## 6. Essais rejoués

Depuis l'arbre, `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -p no:cacheprovider`.

### 6.1 Les huit fichiers `tests/test_t08_*_v1.py`

De 2026-11-14T03:34:12Z à 2026-11-14T03:36:20Z : `142 passed in 126.15s (0:02:06)` — **142 réussites, 0 échec** (nombre du rapport retrouvé ; 127 à `7a4d4e13`).

### 6.2 Les cinq essais d'inventaire

De 2026-11-14T03:37:13Z à 2026-11-14T03:38:05Z : `7 failed, 77 passed in 49.62s`. Éléments nommés (total / T0.8 / autres), comptés par programme au grain de la vérification courte :

```
test_cibles_invisibles_v1.py::test_inventaire_tout_constructeur_d_invite_est_examine : 20 / 5 / 15
test_cibles_invisibles_v1.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles : 5 / 2 / 3
test_cibles_invisibles_v2.py::test_inventaire_tout_constructeur_d_invite_est_examine : 9 / 5 / 4
test_cibles_invisibles_v2.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles : 3 / 2 / 1
test_t06_v11_liste.py::test_liste_reelle_et_exclusions_couvrent_exactement_les_fichiers_d_essais : 78 / 8 / 70
test_t06_v12_liste.py::test_liste_reelle_et_exclusions_couvrent_exactement_les_fichiers_d_essais : 66 / 8 / 58
test_t06_v13_liste.py::test_liste_reelle_et_exclusions_couvrent_exactement_les_fichiers_d_essais : 64 / 8 / 56
messages analysés : 7 sur 7
```

Mêmes nombres qu'à `7a4d4e13` (vérification courte, § 6.2) : aucun élément neuf de T0.8, éléments « autres » inchangés (70, 58, 56 dans les trois listes de T0.6).

### 6.3 Script

Commande : `cd <bloc-notes>/final && PYTHONDONTWRITEBYTECODE=1 /home/user/controle-ia-travail/.venv/bin/python /home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/verification-corrections-2-t08-v1-calcul.py <bloc-notes>/final`, de 2026-11-14T03:40:46Z à 2026-11-14T03:44:21Z ; code de sortie 0 ; sortie d'erreur : vide ; empreinte du script au lancement égale à celle du script scellé. Sortie recopiée à l'octet :

```

=== A1. Phrases gelées : parties A et B du script de la contre-lecture 1, rejouées à la tête ===
phrases gelées des tables D et F égales au caractère près : 15 sur 15 ; inégales : []
réserves et mentions présentes entre guillemets dans le brouillon 4 : 13 sur 13

=== A2. Sorties factices de l'essai v3 (a) ===
table D : ligne retenue D6 ; lignes écrites 6 ; phrase égale à la phrase gelée : True
table F : {'S100': ('F4', 9, True), 'S25': ('F4', 9, True), 'S50': ('F4', 9, True), 'S75': ('F4', 9, True)} (ligne, lignes écrites, phrase = gabarit gelé rempli)
fichiers ouverts : 22 (distincts 22) ; à l'étape (a) : 17 (distincts 17) ; manifeste de la course parmi eux : True ; run_course 20261114-030840-t08-course-jouet
écarts des balises imposées : 16 (juge, dose) ; clés ['apres_fin_de_reponse', 'apres_troncature', 'somme'] ; maximum après troncature 0.0444 ; réserves « troncature » : 0
point 8 bis : état 'lue' ; étapes ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'h bis', 'i']

=== B. Déterminisme : essai v3, `a/` contre `b/` ===
comparateur corrigé : fichiers 52 ; identiques à l'octet 41 ; égaux sur le contenu 4 ['course-t08.json', 'lecture-t08.json', 'tables-d-f-t08.json', 'scellements-v1.md'] ; exclus 7 ; différents 0 ; motifs {} ; contrôle des tables par racine {'a': True, 'b': True} ; deterministe True
   règle déclarée : runs/<run T0.8>/manifeste.json et compagnon — exclus
   règle déclarée : diag/<run T0.8>/*.json.sha256 — exclus
   règle déclarée : diag/<run T0.8>/*.json — `resultat` comparé en JSON canonique, enveloppe exclue
   règle déclarée : registres-factices/scellements-v1.md — comparé hors la ligne COURSE-T08
   règle déclarée : diag/<run lecture T0.8>/lecture-t08.json — `resultat` comparé hors la seule clé tables_D_F_fichier.sha256 ; chemin et contenu_sha256 égaux ; dans chaque racine, sha256 = empreinte du fichier des tables sur disque et contenu_sha256 = empreinte de son `resultat`
contrôle indépendant : mêmes listes de fichiers True (52) ; identiques à l'octet 41 ; non identiques à l'octet 11 :
   diag/20261114-030840-t08-course-jouet/course-t08.json : enveloppe, clés qui diffèrent ['manifeste_sha256'] ; `resultat`, clés qui diffèrent []
   diag/20261114-030840-t08-course-jouet/course-t08.json.sha256 : compagnon ou autre (octets différents)
   diag/20261114-030840-t08-lecture-jouet/lecture-t08.json : enveloppe, clés qui diffèrent ['manifeste_sha256'] ; `resultat`, clés qui diffèrent ['/tables_D_F_fichier/sha256']
   diag/20261114-030840-t08-lecture-jouet/lecture-t08.json.sha256 : compagnon ou autre (octets différents)
   diag/20261114-030840-t08-lecture-jouet/tables-d-f-t08.json : enveloppe, clés qui diffèrent ['manifeste_sha256'] ; `resultat`, clés qui diffèrent []
   diag/20261114-030840-t08-lecture-jouet/tables-d-f-t08.json.sha256 : compagnon ou autre (octets différents)
   registres-factices/scellements-v1.md : lignes qui diffèrent ['COURSE-T08'] (mêmes nombres de lignes : True)
   runs/20261114-030840-t08-course-jouet/manifeste.json : clés de premier niveau qui diffèrent ['cree_le']
   runs/20261114-030840-t08-course-jouet/manifeste.json.sha256 : compagnon ou autre (octets différents)
   runs/20261114-030840-t08-lecture-jouet/manifeste.json : clés de premier niveau qui diffèrent ['cree_le']
   runs/20261114-030840-t08-lecture-jouet/manifeste.json.sha256 : compagnon ou autre (octets différents)
a : sha256 citée 1a4741f99bcf… = fichier des tables sur disque : True ; contenu_sha256 e7f8045665a0…
b : sha256 citée b9cbfa9245ab… = fichier des tables sur disque : True ; contenu_sha256 e7f8045665a0…

=== C. Sondes directes ===
C1 H 20 % après troncature ; chaque dose 5 % après troncature et 15 % après fin de réponse : écart de la lettre 0.1500 (réserve due) ; réserves rendues (code, dose, écart, écart de la somme) : [('troncature', 'S25', 0.15, 0.0), ('troncature', 'S50', 0.15, 0.0), ('troncature', 'S75', 0.15, 0.0), ('troncature', 'S100', 0.15, 0.0)]
C1 H 0 % ; chaque dose 0 % après troncature et 15 % après fin de réponse : écart de la lettre 0.0000 (réserve non due) ; réserves rendues (code, dose, écart, écart de la somme) : []
C2 registre du texte de validité déclaré vivant (scelle: false) : ligne rendue (diag/x/sorties-hd-vadapt.json) ; comptés ouverts ['reg/validite.md']
C2 registre du texte de validité déclaré scellé par défaut, sans compagnon : 'non lue', motif 'non lue (registre du texte de validité : état « compagnon_absent », registre vivant sans compagnon attendu)' ; comptés ouverts []
C3 commit en quatrième cellule : lue True ; cite le commit du marqueur : True ; mal formées []
C3 commit dans le chemin, empreinte en quatrième cellule : lue True ; cite le commit du marqueur : True ; mal formées []
C3 autre commit en quatrième cellule, bon commit dans le chemin : lue True ; cite le commit du marqueur : True ; mal formées []
C3 bon commit en majuscules dans le chemin : lue True ; cite le commit du marqueur : False ; mal formées []
C3 commit abrégé (12 caractères) en quatrième cellule : lue False ; cite le commit du marqueur : None ; mal formées [(3, 'CODE-T08')]
C3 clé entre accents graves : lue False ; cite le commit du marqueur : None ; mal formées [(3, None)]
C3 date sans heure : arrêt : date '2026-11-20' sans fuseau : UTC attendu
C3 autre clé (SCELLEMENT-T08) à 40 caractères : lue False ; mal formées à clé lue [(1, 'SCELLEMENT-T08')]
C4 passage à blanc, cas sain : clés rendues ['CODE-MOTS-ET-COUT-T06', 'CODE-T08', 'LECTURE-T08-BASE-A_presente', 'RUN-CONFIRMATION-T06', 'SCELLEMENT-T08', 'anteriorite_sur', 'passage_a_blanc', 'registre', 'texte'] ; lignes lues ['CODE-MOTS-ET-COUT-T06', 'CODE-T08', 'RUN-CONFIRMATION-T06', 'SCELLEMENT-T08'] ; fichiers du dossier inchangés (rien n'est écrit) : True
C4 en-tête « clé » en minuscules : passe ; lignes d'une autre forme rendues [{'numero': 1, 'cle': None, 'cellules': 4}]
C4 heure du passage sans fuseau : arrêt : borne "l'heure du passage à blanc" sans fuseau : UTC attendu
C4 registre absent du disque : FileNotFoundError : [Errno 2] No such file or directory: '/tmp/claude-0/-home-user-controle-ia-travail/0bb788a

=== D. Mutations (copies jetables de `src/controle_ia/t08/` à la tête ; essais nommés rejoués) ===
copies égales à l'arbre : True ; témoin sans mutation, les huit fichiers d'essais : code 0 ; 142 passed
N01 VCT8-01  lecture_v1.py            tuée   : réserve « troncature » décidée de nouveau sur la somme — test_reserves_masses_et_troncature ; test_reserve_troncature_a_la_lettre_cas_c3 [2 failed]
N02 VCT8-01  lecture_v1.py            tuée   : réserve « troncature » : 11 points au lieu de 10 (≥ au bord exclu) — test_reserves_masses_et_troncature [1 failed]
N03 VCT8-02  essai_jouet_v1.py        tuée   : comparateur : empreinte citée non comparée au fichier des tables — test_comparateur_lecture_exclusion_declaree_et_controle_des_tables [1 failed]
N04 VCT8-02  essai_jouet_v1.py        tuée   : comparateur : contenu_sha256 non comparé au `resultat` des tables — test_comparateur_lecture_exclusion_declaree_et_controle_des_tables [1 failed]
N05 VCT8-02  essai_jouet_v1.py        tuée   : comparateur : toute la clé tables_D_F_fichier exclue (chemin et contenu compris) — test_comparateur_lecture_exclusion_declaree_et_controle_des_tables [1 failed]
N06 VCT8-03  lecture_v1.py            tuée   : CODE-T08 : citation du commit non exigée — test_passage_a_blanc_cas_sain_et_artefacts ; test_etape_a_mode_reel_cas_sain_et_artefacts [2 failed]
N07 VCT8-03  lecture_v1.py            tuée   : lecture réelle : antériorité sur COURSE-T08 seule (début de la course oublié) — test_etape_a_mode_reel_cas_sain_et_artefacts [1 failed]
N08 VCT8-03  lecture_v1.py            tuée   : antériorité non stricte (même seconde admise) — test_passage_a_blanc_cas_sain_et_artefacts ; test_controles_texte_et_registre_bornes [1 failed, 1 passed]
N09 VCT8-03  lecture_v1.py            tuée   : SCELLEMENT-T08 non comparée à l'empreinte du texte passé — test_passage_a_blanc_cas_sain_et_artefacts ; test_etape_a_mode_reel_cas_sain_et_artefacts [2 failed]
N10 VCT8-03  lecture_v1.py            tuée   : passage à blanc : COURSE-T08 déjà inscrite tolérée — test_passage_a_blanc_cas_sain_et_artefacts [1 failed]
N11 VCT8-03  lecture_v1.py            tuée   : passage à blanc : RUN-CONFIRMATION-T06 non comparée à RUN_7B — test_passage_a_blanc_cas_sain_et_artefacts [1 failed]
N12 VCT8-03  entrees_v1.py            tuée   : course-t08.json non rattaché au manifeste de la course lu — test_etape_a_artefacts_des_entrees [1 failed]
N13 VCT8-03  entrees_v1.py            tuée   : commit reconnu comme partie d'une chaîne plus longue du chemin — test_passage_a_blanc_cas_sain_et_artefacts ; test_registre_code_t08_forme_du_commit [2 failed]
N14 VCT8-03  entrees_v1.py            tuée   : quatrième cellule de 40 caractères lue pour toute clé — test_registre_code_t08_forme_du_commit [1 failed]
N15 VCT8-05  temoin_distille_v1.py    tuée   : registre du texte de validité lu dans un autre état que « présent » — test_hd_registre_du_texte_de_validite_non_present_non_lu [1 failed]
N16 VCT8-05  temoin_distille_v1.py    tuée   : formes de 7b absentes : pas d'arrêt à l'entrée de la lecture de la pièce HD — test_hd_formes_de_7b_absentes_arretent [1 failed]
N17 VCT8-06  course_v1.py             tuée   : appel de exiger_run_7b retiré de executer_course (M35) — test_course_reelle_manifeste_7b_d_un_autre_run [1 failed]
N18 VCT8-06  course_v1.py             tuée   : appel de exiger_sans_doublon retiré de executer_course (M38) — test_course_jouet_premiere_action_egale_a_celle_de_h_arrete [1 failed]
N19 VCT8-06  lecture_v1.py            tuée   : échangeabilité : `hors_bornes` toujours faux (M61) — test_echangeabilite_hors_bornes [2 failed, 3 passed]
N20 VCT8-06  lecture_v1.py            tuée   : échangeabilité : bords 0,40 et 0,60 comptés hors bornes — test_echangeabilite_hors_bornes [2 failed, 3 passed]
N21 VCT8-07  lecture_v1.py            tuée   : fichiers ouverts avec répétitions (résultat final) — test_fichiers_ouverts_sans_repetition ; test_lecture_complete_cas_sain [2 failed]
N22 VCT8-07  lecture_v1.py            tuée   : fichiers ouverts avec répétitions (étape (a)) — test_fichiers_ouverts_sans_repetition ; test_lecture_complete_cas_sain [2 failed]
bilan : 22 mutations ; tuées par un échec d'essai 22 ; survivent 0 [] ; autres 0 [] ; copies rendues égales à l'arbre : True
```

## 7. Limites

- Vérification différentielle (`7a4d4e13` → `453a71e1`) : le code inchangé n'est pas relu ; les essais neufs sont jugés par leurs noms, par deux lectures entières et par 22 mutations, non ligne à ligne.
- Les mutations disent qu'un essai échoue quand la garde est retirée, non qu'il couvre tous ses cas.
- Rien du mode réel n'est exécuté ; le registre réel, la forme réelle des lignes, le clone de l'instance et l'historique de la branche ne sont pas vérifiables ici (§ 2).
- L'essai de bout en bout n'est pas rejoué : le déterminisme repose sur les deux essais du développeur, comparés ici.
- La suite entière n'est pas rejouée : seuls les treize fichiers nommés le sont.
- Ce rapport ne nomme aucun modèle autrement que « modèle A » et « modèle B ».
