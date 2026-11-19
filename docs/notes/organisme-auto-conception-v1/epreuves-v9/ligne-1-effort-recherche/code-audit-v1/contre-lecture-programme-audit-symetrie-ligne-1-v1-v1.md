# Contre-lecture du programme à part de l'audit de symétrie de la ligne 1 (classe B), version 1

Contre-lecteur : modèle S, choisi parce que la seule place du modèle K sur ce compte est prise et que son autre version tire sur la même limite d'usage ; ce n'est pas un refus. Le code est écrit par le modèle L′ ; la mère en a été avertie et l'accepte (pièce de code, classe B).

**Verdict : Conforme.** Aucune correction demandée ; quatre observations sans effet sur le verdict (§ 5).

## 1. Pièces lues et empreintes

- Commit a64f6db9 de `lot/compte-organisme-v1` (existe ; les dossiers `code/` et `code-audit-v1/` de l'arbre de travail sont identiques à ce commit). Empreintes compagnons de `code/`, `code/essais/` et `code-audit-v1/` : toutes conformes. Programme : ca000bba… ; essais : 18031e62… ; rapport : fcd49e55… (égales aux empreintes annoncées).
- Ce qui fait foi : l'addendum 1 version 4 lu par `git show` sur le commit 45653e962 (c29628a0…), § 2 choix 5 « Complément retenu » et § 4.2 ; le préenregistrement scellé, « Audit de symétrie » et « Audit du générateur ».
- Lus en entier : le programme (476 lignes), le rapport du développeur, la sortie des mutations ; les essais lus par leurs noms et les passages sur les graines et les artefacts ; `etalonnage_ligne1_v2.py` (`audit_generateur`, `lire_courses`), `rejouer_journal_ligne1_v2.py` (`m1_nul_depuis_journal`) et `analyse_ligne1_v2.py` (`mesures_course`) relus pour les comparer.

## 2. Le programme fait-il exactement ces deux calculs, sans porte ni verdict ?

**Oui.**

1. **Complément du choix 5.** Il calcule les aires des traits seuls (identifiant, rang de la lignée, numéro au registre du premier essai de l'appel), étiquette d'effet, avec une carte « indéterminée » comptée non vraie (effet 0) et une carte non jugée hors de l'étiquette, par classe, avec l'intervalle à 95 % des 1 000 rééchantillons de la racine 2026111903 et de la tâche `etalonnage|audit|classe=<classe>`. Les cartes sont les `transformee` des 400 courses d'étalonnage de chaque classe, lues sur les sorties scellées (empreinte de chacune contre la liste scellée de l'étalonnage, garde A17 refaite, course et classe contrôlées). Le tuple de la porte est, champ pour champ, celui de `lire_courses` (je l'ai comparé) ; celui du complément ne diffère que pour la carte jugée indéterminée. Un intervalle tout entier hors de [0,45 ; 0,55] est nommé, sans arrêt ni ligne 0, comme la conduite écrite d'avance l'exige.
2. **Recoupement de M1-nul** (§ 4.2) : courses 0, 300, 599 de chaque classe, M1-nul de chaque bras recalculé depuis les décisions du journal et comparé à la sortie brute ; le programme écrit « concordant » ou « désaccord » avec le détail, ne prononce aucun verdict, ne choisit pas entre le journal et la sortie brute ; la note du compte rendu le dit. Un désaccord n'arrête rien dans le programme : il est rapporté pour Lazar, comme le texte le fixe.
3. Aucune garde de la liste d'arrêt n'est ajoutée ; les refus du programme (empreinte, cohérence des entrées, racine, recalcul de la porte, organisme non chargé) n'arrêtent que lui et ne lisent aucun chiffre de l'épreuve pour décider.

## 3. Les rééchantillons du complément sont-ils ceux de la porte ?

**Oui, par construction.** Le complément passe par le même appel `etalonnage_ligne1_v2.audit_generateur(cartes, list(range(n)), config, racine_r, classe)` que la porte, qui dérive `GRAINES(racine_r, "etalonnage|audit|classe=<classe>")` et la même boucle de tirages ; la liste des courses (0 à n−1) ne dépend pas des cartes, donc les rééchantillons sont identiques tirage par tirage. `GrainesConsignees` ne change pas la dérivation : elle appelle `Graines.__call__` de la classe mère (`graine_de_tache` de l'organisme) puis consigne racine, tâche et graine. Essai `test_complement_memes_reechantillons_que_la_porte` : interception de `GRAINES` et de `numpy.random.default_rng`, mêmes racine, tâche, graine et tirages que l'appel de la porte, par classe ; mutations m04 (autre tâche) et m05 (autre racine) vues.

## 4. Reprises par import, sans copie

**Oui.** Dans le fichier, aucune définition de `audit_generateur`, `auc_ponderee`, `ajuster_logistique`, `mesures_course`, `m1_nul_depuis_journal`, `lire_courses`, `verifier_code_configuration` : je l'ai vérifié (comptage nul des définitions) ; les objets sont ceux des modules v2. Essai `test_code_importe_est_le_code_v2_de_la_configuration`. Le programme écrit lui-même le lecteur des deux conventions (`carte_deux_conventions`), les lectures (ii) et (iv), la comparaison et les contrôles.

## 5. Jugement des choix de la main du développeur

1. **Recalcul de la porte comparé au bit près à la sortie scellée (refus neuf `RecalculPorteDifferent`)** : approuvé. C'est ce qui prouve, sur les vraies sorties, que les cartes lues et les rééchantillons sont ceux de la porte, et qu'il ne lit aucun chiffre de l'épreuve pour décider. Essais : sain, artefact, et refus dans le run entier ; mutation m07 vue. Observation : l'égalité au bit près suppose la même pile numérique entre l'étalonnage et l'audit ; sur une autre version de numpy ou de bibliothèque de calcul, le refus pourrait tirer à tort (il n'arrête que ce programme et renvoie à la mère). Les versions sont déjà au manifeste de l'étalonnage : une ligne dans le message de refus qui les rappelle serait un confort, non une correction.
2. **Recoupement plus strict que la lettre (couples (V, R) en plus de M1-nul, quatre lectures par bras)** : approuvé. Un M1-nul égal à 0 masque la disparition d'une promotion d'un monde à effet ; les quatre lectures (arrêts du journal, promotions du journal, fonction de l'analyse, calcul direct sur la sortie brute) sont des fonctions exactes des mêmes données, donc un « désaccord » ne peut venir que d'une divergence réelle. Le mot est plus exigeant que le § 4.2 et c'est dit au rapport ; j'y vois un renforcement, pas un écart de sens. Essais : sain (9 bras, 3 courses, 2 classes), artefact dans la sortie brute, artefact dans le journal avec chaîne refaite, promotions contre arrêts seuls ; mutations m09, m24 et voisines vues.
3. **Empreinte du manifeste exigée en argument** : approuvé. Le compagnon seul se refait avec le fichier ; l'empreinte portée au registre ne se refait pas. Essai : sortie changée, empreinte fausse, étalonnage changé, compagnon seul faux ; rien d'écrit.
4. **Racine 2026111999 employée par un artefact** : approuvé. Elle est disjointe de toutes les racines du préenregistrement (1900 à 1903), de la fumée (1990 à 1993) et de mes passages ; elle n'est dérivée que dans l'essai qui plante la dérivation étrangère, et le refus tombe avant toute écriture. Le contrôle final des racines passe.

## 6. R5 : chaque garde avec cas sain et artefact

| garde | cas sain | artefact |
|---|---|---|
| empreinte différente | `test_recoupement_cas_sain_concordant`, `test_complement_dans_le_run_entier` | `test_refus_empreinte_fausse` (cinq variantes), `test_refus_journal_rompu` |
| mode, racine, configuration | `test_verifier_mode_cas_sains_et_artefacts` | mêmes essais, mode et empreinte de configuration faux |
| cohérence des entrées | `test_verifier_coherence_cas_sain_et_artefacts` | mêmes essais, configuration, code, racine, courses absentes |
| recalcul de la porte | `test_recalcul_de_la_porte_cas_sain_et_artefact` | idem et `test_refus_porte_scellee_differente_dans_le_run` |
| lecteur des cartes (nom absent, course déplacée) | `test_complement_lecteur_egal_a_lire_courses_du_code_v2` | `test_lecteur_artefacts_nom_absent_et_course_deplacee` |
| organisme non chargé | run entier | `test_refus_organisme_non_charge` |
| racine dérivée hors du mode | run entier | `test_refus_racine_derivee_hors_du_mode` |
| commande en mode réel seul | — | `test_main_mode_reel_refuse_avant_toute_derivation` |

Le contrôle R4 du développeur (25 défauts, 25 vus, témoin sans défaut vert) correspond aux essais visés ; sa passe 1 (4 défauts non vus ou mal vus) est déclarée et corrigée. Aucun repli silencieux relevé : chaque refus lève une exception nommée ; aucun fichier n'est supprimé ni écrasé (noms neufs, `FileExistsError`).

## 7. Essais rejoués et graines

- Copie dans mon bloc-notes (dépôt `git init` à part, rien d'écrit dans le dépôt de travail) ; fichier de mémoire extrait de `65574043d` par `git show` : empreinte 43b01b43b1ec347ff02b456975d74c17e7a0e974e9b95e9ba4935bdb895f31a0 (conforme) ; les huit autres fichiers de l'organisme viennent de la copie du commit 94bfd92, empreintes égales à la configuration.
- **24 essais passés sur 24** (37 secondes), dernier essai compris : la racine des essais a été dérivée, aucune des racines 2026111901 à 2026111903 ne l'a été dans le processus des essais.
- Pendant cette contre-lecture, je n'ai exécuté que cette suite, des lectures de fichiers, des empreintes et des commandes `git` ; aucune graine des racines 2026111901 à 2026111903 n'a été dérivée de mon fait. Ni étalonnage, ni fumée, ni course ; aucun accès sous `archives-reponses-modeles/`.

## 8. Observations, sans correction

1. Voir § 5, point 1 : égalité au bit près de la porte, sensible à une pile numérique différente.
2. Le chemin réel de bout en bout (la commande qui passe tous les contrôles et calcule, racine 2026111903) n'a jamais tourné ; il ne diffère du chemin éprouvé en mode essai que par la racine, la configuration et la valeur du mode (même fonction `executer`). Le développeur le dit. Le premier vrai lancement est donc aussi le premier essai de ce chemin ; il n'arrête rien et n'écrit que des noms neufs.
3. Le programme n'est pas dans la liste du code v2 de la configuration : ni la configuration ni le lanceur ne le contrôlent ; son empreinte doit être portée au registre et comparée à celle de son manifeste de run (réserve 6 de l'addendum), et il doit être commis avant tout lancement du lanceur v2 (qui refuse un arbre sale sous `code/`). Le développeur le dit.
4. Les deux écarts déclarés par le développeur (un `python3 -c` en ligne pour afficher des versions, un `git status` sur tout le dépôt) n'ont laissé aucune trace dans le code ni aucun effet ; je les note sans conséquence. Le programme lui-même ne lance que des commandes `git` restreintes au dossier du code.
