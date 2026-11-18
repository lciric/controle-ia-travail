# Rapport du développeur — correctif v2c de la course d'auto-conception de l'organisme d'idéation

Écrit le 2026-11-18 (`date -u` : 2026-11-18T15:54:35Z au début de l'écriture) par le développeur unique du correctif (modèle L′), branche `lot/compte-organisme-v1`. Fondement : mot de Lazar, 18 novembre 2026, « go (a), lance les deux correctifs ». **Aucune dépense, aucun appel à un fournisseur, aucun relais réel, aucun mode réel** : tout est hors ligne. R12 : ajouts seuls, aucun fichier existant modifié ni supprimé. La copie de l'orchestrateur (`/home/user/ideation-organism`, commit `a41b7b50`) est restée intacte (`git status --porcelain --untracked-files=all --ignored=matching` vide après chaque essai).

## Verdict

Défaut corrigé dans le programme d'épreuve v3 ; **la course n'avait pas ce défaut** (preuve ci-dessous) ; lanceur v3, additif, commandes v2c écrits, scellés ; 133 essais neufs passés, 108 essais existants passés encore ; essai à blanc et épreuve hors ligne rejoués (code 0). Reste, avant tout appel : la contre-lecture du modèle K (`course-v2/contre-lecture-correctif-v2c-auto-conception.md`).

## Pièces neuves et empreintes

| pièce | sha256 |
|---|---|
| `scripts/epreuve_temoins_auto_conception_v3.py` | `0c72dd8763537152b7339ca15ff439f759c062f0b33a6571a513029870eebd1b` |
| `scripts/lancer_course_auto_conception_v3.py` | `42001b2807337cfd4c10c6708b384f5f218201457eab95d309080c6c57949fef` |
| `docs/notes/organisme-auto-conception-v1/course-v2/additif-preenregistrement-course-auto-conception-v2c.md` | `7c76eba0340040b2c2d29cf3aa5015a194632ac24f3e558565a22424702b0cfd` |
| `docs/notes/organisme-auto-conception-v1/course-v2/commandes-exactes-course-auto-conception-v2c.md` | `8401a664216da7b225d93db7a083ca1e857c7ef9b22a5ee88ed6005f1d34d55c` |
| `tests/test_epreuve_temoins_auto_conception_v3.py` (25 essais) | `126893941e924d8f846f23c983d271e073c4d420bc293e58b3e4d2552d135d36` |
| `tests/test_lancer_course_auto_conception_v3.py` (108 essais) | `868943c43e286e565ab5fca767a0e31a559eee9a56abc5f8fecb1c5ffdf938a9` |
| `course-v2/essai-a-blanc-v2c/lanceur/manifeste-lanceur-depart.json` | `b5f1271108360233f8de3af2f69874f91eba65c2dc876640c2c50ce896411fb9` |
| `course-v2/essai-a-blanc-v2c/lanceur/manifeste-lanceur-fin.json` | `0ed078a36b3bd036e5668608a3fdb19e64834c485ed3b139f797b5621142141b` |
| `course-v2/essai-a-blanc-v2c/epreuve-hors-ligne-v3/epreuve-temoins-hors-ligne.json` | `de5a63b310d6e8e807d876a57a9424acc9f90c345705f398f1c44386cdd68e66` |
| `course-v2/essai-a-blanc-v2c/journaux/a-blanc-v2c.stdout.txt` | `753f84438a75d494e71d41c2c17ff3c3269d3988a355a9e684e277586873b485` |
| `course-v2/essai-a-blanc-v2c/journaux/epreuve-hors-ligne-v3.stdout.txt` | `8d5222fb5d979a1202a7f3562f887e1a509d4457b0632396349d4f602ad3ce4a` |
| `course-v2/essai-a-blanc-v2c/journaux/*.stderr.txt` (deux, vides) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Chaque pièce a son compagnon `.sha256` ; les autres fichiers de `essai-a-blanc-v2c/` (acte de gel, manifestes de l'orchestrateur, pièces d'essai) gardent le compagnon écrit par le programme qui les a produits, vérifié (`sha256sum -c`) après copie. Pièces reprises telles quelles : préenregistrement v2 `0d51e0b3…6763c6`, pièce de départ `e2689fa2…c1ded`, sonde d'Astra `802b840e…e8f43`, devis v2b `b2319472…5da0e`.

## Le défaut et la correction

- **Constaté** (sortie d'erreur versée, `9a0ca71e…`) : `reel()` de l'épreuve v2 remettait à `adaptateurs_reels_v56` les chemins interdits `[base des sessions, sortie/"sortie"]` mais passait `sortie/"appels"` comme dossier des agents ; `construire_options` (`pole/adaptateurs.py`, l. 297) refusait.
- **Reproduit hors ligne** : `test_cablage_de_la_v2_reproduit_le_defaut_constate` (adaptateurs réels construits par le lanceur v8 de la copie, mêmes arguments) lève le message exact de la sortie d'erreur.
- **Voie choisie** : dossiers d'appel sous la sortie interdite, `sortie/"sortie"/"appels"/<étiquette>/<témoin>` (chemin réel, `dossier_des_appels`), plutôt qu'élargir la liste interdite : la liste remise par l'orchestrateur reste celle qu'il construit lui-même (base des sessions, sortie), et chaque agent ne rouvre que son dossier ; la fiche voisine et les dossiers des autres rôles sont tous sous `sortie/"sortie"`, interdite.
- **Garde neuve avant tout appel et avant la transmission des plafonds** (`preparer_appels` → `verifier_dossiers_d_appel`) : `construire_options` de la copie épinglée jouée sur chacun des 33 dossiers du plan avec la liste de l'adaptateur et le rôle que `jouer` passe ; `allowRead` = le seul dossier ; chacun des 32 autres dossiers sous `denyRead` et hors de `allowRead` ; tout écart → `Refus` (code 2), rien dépensé. Rôle servi par commande externe (juge Argon) : « sans objet », écrit au rapport réel (`dossiers_d_appel`).
- **Inchangé, vérifié à l'octet par essai** : `lire_epreuve`, `verite`, `jouer`, `servir`, `identifiant_servi`, `controles_statiques`, `hors_ligne`, `charger_orchestrateur`, `fiche_servie`, les juges factices, `ecrire_scelle` ; constantes (plafond 5 USD, témoins, consignes, configuration, graines, bornes). Seuls changent : `VERSION`, `DECLARATION_EPREUVE` (`…-v3.json`), `RAPPORT_REEL` (`…-v3.json`), `LANCEUR` (v3), le nom de module du lanceur chargé, et `reel()` (plan calculé avant les adaptateurs, garde, `appels` passé à `jouer`, champ `dossiers_d_appel` au rapport).
- **Lanceur v3** : par rapport à la v2, ne changent que `Reglages` (champ `additif`), `verifier_additif` (neuve : empreinte épinglée, scellé, cite le préenregistrement et le programme d'épreuve épinglés), `verifier_contre_lecture` (cite l'additif et le lanceur au lieu du préenregistrement et du lanceur ; reste des règles identique), `charger_epreuve` (nom de module), `ecrire_registre_derive` (titre), `acte_de_gel` (ligne de l'additif), `executer` (ordre : pièces, additif, contre-lecture ; additif au manifeste ; suffixe d'alerte v3), `reglages_a_blanc` (contre-lecture d'essai qui cite l'additif) et les constantes nommées dans son en-tête. Toute autre fonction ou classe est identique à l'octet (essai `test_constantes_v3_et_rien_d_autre_ne_change`).

## Point 3 — la course place-t-elle les dossiers des agents sous un chemin interdit ? Oui : aucun défaut de cette sorte

Lecture du code de la copie : en moteur réel, `ideation_v8.executer` crée `base_sessions` (`tempfile.mkdtemp`) puis `adaptateurs_reels_v56(conf, sortie, base_sessions)` : l'adaptateur du kit reçoit `interdire_lecture = [realpath(base_sessions), realpath(sortie)]`. Le noyau (`OrchestreV55`) range chaque appel dans `self.session(*logique)` = `<realpath(base)>/generation-1/sessions/<16 hexadécimaux opaques>` (`verifier_emplacement_sessions` refuse une base sous la sortie ; `session` refuse un dossier hors de la racine ou sous la sortie) ; tous les appels (proposeurs, aiguilleur, juges, lecteurs, fusions) passent par `appel` → `session`. `OrchestreV56.__init__` joue en plus `verifier_lecture_interdite` (`construire_options` sur une session sonde, pour chaque rôle du kit). Les commandes externes (Argon, Astra, Carbon) ne passent pas par `construire_options` : la session n'est que leur dossier courant ; Kimi (non déclaré) n'emploie pas le dossier.

Preuve par essai (`test_course_dossiers_des_agents_sous_un_chemin_interdit_chaque_role`, `tests/test_lancer_course_auto_conception_v3.py`) : la pièce de départ scellée réelle et les commandes réelles d'Astra et de Carbon (extraites de `main`) → lanceur v3 → configuration assemblée (composition réelle : `prop-opus`, `prop-fable`, `prop-argon`, `prop-astra`, `prop-carbon`) → course jouée **par le vrai noyau** de la copie (`ideation_v8.principal`, moteur simulé, dans le processus de l'essai) ; chaque dossier d'agent relevé est passé à `construire_options` avec la liste de l'adaptateur Claude **réel** construit par `adaptateurs_reels_v56` sur la même sortie et la même base. Décompte de ce rejeu (relevé par un essai jetable hors dépôt qui réemploie les mêmes fonctions) : **385 appels, 385 dossiers distincts**, tous sous `<base>/generation-1/sessions/`, hors de la sortie, tous acceptés, `allowRead` = le seul dossier, `denyRead` = [base, sortie], aucun voisin lisible :

| étape / rôle / relais | appels | adaptateur réel |
|---|---|---|
| proposition / prop-opus / claude | 11 | `AdaptateurClaudeSDK` |
| proposition / prop-fable / claude | 11 | `AdaptateurClaudeSDK` |
| proposition / prop-argon / argon | 11 | `AdaptateurCommandeExterneV56` |
| proposition / prop-astra / astra | 11 | `AdaptateurCommandeExterneV56` |
| proposition / prop-carbon / carbon | 11 | `AdaptateurCommandeExterneV56` |
| aiguillage / aiguilleur / claude | 110 | `AdaptateurClaudeSDK` |
| juges / juge-opus / claude | 110 | `AdaptateurClaudeSDK` |
| juges / juge-argon / argon | 110 | `AdaptateurCommandeExterneV56` |

Les 385 dossiers (et pas seulement les 242 servis par le kit) passent la garde avec la liste de l'adaptateur Claude. `verifier_lecture_interdite` (garde du noyau) rend les deux rôles du kit. Artefacts (R5, `test_course_artefacts_sessions_hors_des_chemins_interdits_refusees`) : un dossier hors de la base et de la sortie → refusé par `construire_options` ; une base de sessions sous la sortie → `SessionsMalPlacees`. **Le lanceur v3 ne change donc rien à la course.** Pour l'épreuve, le même essai par adaptateurs réels est fait rôle par rôle (aiguilleur et juge-opus par le kit : 11 dossiers chacun acceptés, 32 voisins interdits ; juge-argon : commande externe, sans objet).

## Essais — décomptes exacts

Commande : `cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B -m pytest -q -rs -p no:cacheprovider <fichiers>`.

- **Neufs** : `tests/test_epreuve_temoins_auto_conception_v3.py` **25 passés** (5 essais de l'épreuve portés de la v2 ; 12 fonctions identiques à la v2 ; 1 constantes ; 7 neufs : défaut reproduit, v3 sain pour chaque rôle, deux artefacts R5, câblage de `reel()`, deux mutations) ; `tests/test_lancer_course_auto_conception_v3.py` **108 passés** (78 essais du lanceur v2 portés, 11 de la v2b portés, 19 neufs : additif, contre-lecture, rapport d'épreuve v2 refusé, une seule course sur v1/v2/v3, rien d'autre ne change, pièce de départ et sonde, essai à blanc, pièce de départ réelle acceptée telle quelle, course par le vrai noyau, artefacts). Ensemble : **133 passés, 0 échec, 0 sauté** (88 s).
- **Mutation (c)** : `test_mutation_sortie_appels_echoue_a_l_essai_neuf` — le v3 où `dossier_des_appels` rend `sortie / "appels"` lève `Refus` (« fiche voisine ») à l'essai neuf, le v3 non muté passe sur les mêmes entrées ; `test_mutation_de_reel_vers_sortie_appels_echoue` — le v3 où `reel()` repasse `sortie / "appels"` à `jouer` échoue au contrôle de câblage.
- **Existants** : `tests/test_lancer_course_auto_conception_v2.py tests/test_sonde_astra_courses_v1.py tests/test_astra_carbon_declares_auto_conception_v2b.py` **108 passés** (83 + 14 + 11), 0 échec, 0 sauté, rejoués après toutes les écritures.
- **Essai à blanc du lanceur v3** (dossier neuf hors dépôt) : code 0, 4 espèces d'essai × 11 cases, 88 cartes à passeport, `proposition`, `aiguillage`, `etiquettes`, `juges` jouées, `passe_tableau` et `fusions` retirées, cumul simulé 3,08, lots `74d988bd…` (= référence du préenregistrement), additif cité par l'acte de gel et le manifeste. **Épreuve hors ligne v3** : « témoins éprouvés hors ligne », 0 juge au hasard réussi sur 2 000, juge parfait réussi, juges à la longueur, au champ, indulgent et sévère échoués. Versés sous `course-v2/essai-a-blanc-v2c/`.

## Ce qui n'a pas été vérifié

- Aucun appel réel : le bac à sable du kit n'a pas été lancé ; la garde neuve prouve la cohérence de la liste interdite et du dossier (`construire_options`), pas son application par le bac (garde de l'orchestrateur, échec dur s'il manque).
- `AdaptateurClaudeSDK.lancer` n'a pas été appelé (il ouvrirait une session) : l'essai s'arrête à `construire_options`, appelée avec les arguments que `lancer` lui passe (lus dans le code de la copie).
- La course a été rejouée en moteur simulé : les dossiers de session ne dépendent pas du moteur (même noyau, même `session`), mais les relais, la porte à blanc, le registre des GO réel, les relevés et la contre-lecture ne l'ont été que par les essais du lanceur (monde simulé).
- Le registre des GO (`registres/go.md`) n'a pas été lu (hors périmètre) : la présence des lignes `GO-2026-11-18-20` et `-21` n'est pas vérifiée ici.
- `python -m controle_ia.scellement verifier-arbre .` n'a pas été joué (il lirait des dossiers hors du périmètre de cette tâche) ; seules les pièces neuves et les copies versées ont été vérifiées par empreinte.
- Argon et Carbon partagent `GEMINI_API_KEY` : le lanceur confronte chaque relais à sa part séparément, sans les additionner (sans effet sous dispense) ; dit aux commandes v2c, § 12.
- Les noms des dossiers d'appel de l'épreuve portent l'étiquette du rôle et l'identifiant du témoin, comme en v2 (la course emploie des identifiants opaques) : inchangé, dit.
