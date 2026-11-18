# Rapport du développeur — correctif v10 de la course d'affinage des idées des mentors

- Écrit le 2026-11-18T23:21:53Z (`date -u +%FT%TZ`) par le modèle L', sur demande de la session principale, après la contre-lecture de la v9 par le modèle K (`course-v9/contre-lecture-preenregistrement-course-affinage-mentors-v9.md`, `615ef93b2be55f1342d5f1f78747b515862de34b5edf334acddc759eb4147002`, commit `74676380`, « Scellable après corrections. »), lue en entier. Branche neuve `prep/affinage-v10-compte-organisme-v1`, partie de `74676380` (tête de `origin/prep/affinage-v9-compte-organisme-v1`) ; rien de la v9 n'est modifié (ajouts seuls, R12).
- **Aucune dépense, aucun appel réseau vers un fournisseur, aucun relais réel, aucun lanceur sans `--a-blanc`.** Exécuté : lectures du code de l'orchestrateur épinglé (lecture seule), un rejeu de sa vraie classe de budget hors réseau (`PYTHONDONTWRITEBYTECODE=1`, `-B`), essais hors ligne, un essai à blanc (moteur simulé, dossier neuf hors dépôt). Aucune valeur de clé lue. Rien sous `diag/`, `donnees/`, `registres/`, `docs/notes/bras-attaque/` ; rien ouvert sous `/home/user/sorties-course-auto-conception-v4/`, `/tmp/pole-sessions-*` ni dans un journal de relais.

## 1. Verdict du développeur

Fait comme demandé. Le majeur et les deux mineurs de la contre-lecture sont des erreurs **de texte** ; je les ai vérifiés dans le code de l'orchestrateur épinglé avant d'écrire (§ 2) : **le constat 1 est juste**. Préenregistrement v10, devis v10, commandes v10 et gabarits v10 corrigés ; lanceur v10 = lanceur v9 à l'épingle du préenregistrement et aux chemins près, montré par un différentiel (§ 4) et par un essai qui reconstitue le lanceur v9 contre-lu à l'octet près à partir du v10. **Aucune garde, aucun chiffre, aucun argument de commande, aucun code de sortie, aucune pièce épinglée ne change** ; plafond d'arrêt 150 USD (GO-2026-11-18-14), configuration v9, composition et clé Minuit inchangés.

## 2. Vérification du constat 1 dans l'orchestrateur épinglé

Orchestrateur `/home/user/ideation-organism/orchestrator` (lecture seule ; empreintes égales à celles épinglées par le lanceur : `pole/budget_v56.py` `3a672aceeeee3cf83cd4e46ca461fdbaf3acd0a9552be24d2566627ce6b7c13e`, `pole/noyau_v56.py` `eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b`).

- `pole/budget_v56.py` l. 19-23 et 45-47 : au lancement, une étape **protégée** reçoit « plafond dur = max(plafond de relais ; S17 − cumul − attendu aux bases des étapes restantes non retirées) », fixé pour toute l'étape ; l. 142-148 (`plafond_dur`) : `centime_bas(max(relais, self.plafond - self.cumul - self.attendu_restantes(nom)))`, souple ; l. 177-190 (point 3) : étape protégée **non lancée** si `cumul + plafond de relais > S17` → `non_mesuree_budget` ; l. 191-196 : lancement ; l. 209-217 : étape protégée coupée (reste nul rencontré, ou coût au-delà du plafond dur) → `non_mesuree_budget` ; l. 219-220 : le plafond de relais ne sert qu'au drapeau `au_dela_du_plafond_de_relais`.
- `pole/noyau_v56.py` l. 147-161 : chaque appel est borné à `min(plafond de session, reste)`, le reste étant pris sous le plafond dur de l'étape ; reste nul → étape coupée, appel non lancé ; l. 262-263 : `reste` de l'étape = `plafond_dur_usd`.
- `pole/noyau_v54.py` l. 146-154 (`c13_ou_noeud`) et `pole/course2_v56.py` l. 346-353 : après une étape « non mesurée », nœud, la génération ne continue pas, rien n'est lu ; `demonstrations/ideation_v8.py` l. 152-157 : un nœud rend le code 2 de l'orchestrateur, donc le **code 6** du lanceur.
- Budget de la configuration v9 (inchangé depuis la v6) : proposition attendu 25 / relais 60 ; aiguillage 6 / 30 ; juges 14 / 50 ; étiquettes 0 / 0 ; passe « tableau » et fusions sacrifiables à 151 (retirées). Plafond dur de la proposition : max(60 ; 150 − 0 − 20) = **130 USD**.

**Rejeu de la vraie classe `BudgetV56`** (script hors dépôt, lecture seule, même résultat que celui de la contre-lecture v9, repris par l'essai `test_v10_regle_d_a1_rejouee_plafond_dur_souple_et_seuils`) :

| proposition ; aiguillage ; juges (USD) | plafonds durs reçus | issue |
|---|---|---|
| 24,70 ; 4,96 ; 11,47 (estimations) | 130,00 ; 111,30 ; 120,34 | tout joué, cumul 41,13 |
| 76,36 ; 21,12 ; 31,24 (hauts du devis) | 130,00 ; 59,64 ; 52,52 | tout joué, cumul 128,72 |
| 100,00 ; 0,00 ; 11,47 | 130,00 ; 36,00 ; 50,00 | tout joué (100 + 50 = 150) |
| 95,00 ; 6,00 ; — | 130,00 ; 41,00 ; — | juges non mesuré (budget), nœud |
| 100,01 ; 4,96 ; — | 130,00 ; 35,99 ; — | juges non mesuré (budget), nœud |
| 120,00 ; 4,96 ; — | 130,00 ; 30,00 ; — | juges non mesuré (budget), nœud |
| 120,01 ; — ; — | 130,00 | aiguillage non mesuré (budget), nœud |
| 129,99 ; — ; — | 130,00 | aiguillage non mesuré (budget), nœud |
| 130,00, appel suivant sans reste | 130,00 | proposition non mesuré (budget), nœud |

Seuils exacts : juges lancés si et seulement si proposition + aiguillage ≤ 100 USD ; aiguillage lancé si et seulement si proposition ≤ 120 USD ; proposition coupée seulement à 130 USD épuisés. Aucun dollar au-delà de 150 (point 3 et borne de chaque appel). Les deux mineurs (gabarit l. 23 : « configuration v6 » ; devis § 3 : le « haut » n'est pas une borne) sont justes aussi.

## 3. Pièces versées (scellées, compagnon `.sha256`)

| pièce | sha256 |
|---|---|
| `course-v10/preenregistrement-course-affinage-mentors-v10.md` (épinglé par le lanceur v10) | `7fc71712136cf20d86f3603eb581bc61dd6bc35fcfe0650b230cf659674a3856` |
| `scripts/lancer_course_affinage_mentors_v10.py` | `b08290254982744ba7985232ea54a354bfb31ef7f92ada682d32e349d3294577` |
| `course-v10/commandes-exactes-course-affinage-v10.md` | `ecf3eb7ddb6ea446c8633c9dd349ca88cfd308cc7030722b61c6328d3517d2c6` |
| `devis-course-affinage-mentors-v10.md` | `e007a137c73164a56ebccb2c1d7f4f0ee9c77b88d17b5597528d6bfde172d885` |
| `tests/test_lancer_course_affinage_mentors_v10.py` | `4e6516695fb086363fdc5fb46c8b609d15f8ea4b728431c841e532e91dc3b992` |
| `course-v10/declaration-relais-gabarit-course-affinage-v10.json` | `f43035d2b3f8114d88ae5abb513a9d6f765e4ab7ff7000a06579645db38db316` |
| `course-v10/releve-credits-gabarit-course-affinage-v10.json` | `80af2d6dc8262c009a453db233ba4ac7d069dbbd4e441c484269e6c909798c2c` |
| `course-v10/releve-prix-claude-gabarit-course-affinage-v10.json` | `566a4a5e84d34a07d4691c25021efc76b9fcb526ec15991b654f0625db58aa1c` |
| `course-v10/essai-a-blanc-v10/…` (15 fichiers) | leurs compagnons `.sha256` |
| configuration (inchangée, toujours épinglée) `course-v9/configuration-course-affinage-mentors-v9.json` | `e7378f89ae39eacd169ff912526a8e998e4f01f0aba235eeaa0bf12e4b195d5d` |

**Contre-lecture exigée par le lanceur v10** : `docs/notes/organisme-affinage-mentors-v1/course-v10/contre-lecture-preenregistrement-course-affinage-mentors-v10.md`, scellée, du modèle K, citant en entier `7fc71712136cf20d86f3603eb581bc61dd6bc35fcfe0650b230cf659674a3856` (préenregistrement v10) et `b08290254982744ba7985232ea54a354bfb31ef7f92ada682d32e349d3294577` (lanceur v10), première ligne sous `## Verdict` exactement `Scellable.`.

## 4. Lanceur v10 : le v9 à l'épingle et aux chemins près (différentiel)

`diff -U0 scripts/lancer_course_affinage_mentors_v9.py scripts/lancer_course_affinage_mentors_v10.py` : 59 lignes marquées, dont 24 d'en-tête (docstring : une ligne de titre remplacée par 23 lignes où la v10 se dit, puis « Texte de la v9 : » et le texte v9 inchangé). Le reste, en entier :

```diff
@@ -209 +231 @@
-VERSION = "lancer_course_affinage_mentors_v9"
+VERSION = "lancer_course_affinage_mentors_v10"
@@ -220 +242,2 @@
-COURSE = "docs/notes/organisme-affinage-mentors-v1/course-v9"
+COURSE_V9 = "docs/notes/organisme-affinage-mentors-v1/course-v9"
+COURSE = "docs/notes/organisme-affinage-mentors-v1/course-v10"
@@ -262 +285 @@
-RELEVE_PRIX = f"{COURSE}/releve-prix-claude-course-affinage-v9.json"
+RELEVE_PRIX = f"{COURSE}/releve-prix-claude-course-affinage-v10.json"
@@ -269 +292,2 @@
-SONDES_ASTRA_V2 = (f"{COURSE}/sonde-astra-course-affinage-v9-{{jour}}.json",
+SONDES_ASTRA_V2 = (f"{COURSE}/sonde-astra-course-affinage-v10-{{jour}}.json",
+                   f"{COURSE_V9}/sonde-astra-course-affinage-v9-{{jour}}.json",
@@ -272,0 +297 @@
+                         f"{COURSE_V9}/sonde-astra-commune-{{jour}}-v1.json",
@@ -306 +331 @@
-SORTIES_COURSES = tuple(Path(f"/home/user/sorties-course-affinage-mentors-v{k}") for k in (1, 2, 3, 4, 5, 6, 7, 8, 9))
+SORTIES_COURSES = tuple(Path(f"/home/user/sorties-course-affinage-mentors-v{k}") for k in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
@@ -314,5 +339,5 @@
-PREREG = f"{COURSE}/preenregistrement-course-affinage-mentors-v9.md"
-PREREG_SHA256 = "b24755fccdbb58906a21461c1dde7108f96aab73e12922a4f6fcc13265a54938"
-CONTRE_LECTURE = f"{COURSE}/contre-lecture-preenregistrement-course-affinage-mentors-v9.md"
-DECLARATION_RELAIS = f"{COURSE}/declaration-relais-course-affinage-mentors-v9.json"
-RELEVE_CREDITS = f"{COURSE}/releve-credits-avant-course-affinage-mentors-v9.json"
+PREREG = f"{COURSE}/preenregistrement-course-affinage-mentors-v10.md"
+PREREG_SHA256 = "7fc71712136cf20d86f3603eb581bc61dd6bc35fcfe0650b230cf659674a3856"
+CONTRE_LECTURE = f"{COURSE}/contre-lecture-preenregistrement-course-affinage-mentors-v10.md"
+DECLARATION_RELAIS = f"{COURSE}/declaration-relais-course-affinage-mentors-v10.json"
+RELEVE_CREDITS = f"{COURSE}/releve-credits-avant-course-affinage-mentors-v10.json"
@@ -321 +346 @@
-    "configuration": (f"{COURSE}/configuration-course-affinage-mentors-v9.json", "e7378f89…"),  # v9 : proposeur 3,00
+    "configuration": (f"{COURSE_V9}/configuration-course-affinage-mentors-v9.json", "e7378f89…"),  # v9 : proposeur 3,00
@@ -386,3 +411,3 @@
-DOSSIER_SORTIES = Path("/home/user/sorties-course-affinage-mentors-v9")
-SUFFIXE_RUN = "-course-affinage-mentors-v9"
-SUFFIXES_DEJA_LANCEE = tuple(f"-course-affinage-mentors-v{k}" for k in (1, 2, 3, 4, 5, 6, 7, 8, 9))  # une seule course, quelle que soit la version
+DOSSIER_SORTIES = Path("/home/user/sorties-course-affinage-mentors-v10")
+SUFFIXE_RUN = "-course-affinage-mentors-v10"
+SUFFIXES_DEJA_LANCEE = tuple(f"-course-affinage-mentors-v{k}" for k in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # une seule course, quelle que soit la version
@@ -1399 +1424 @@
-                    "(un seul exigé, R-3273) ; un autre jour : sonde neuve, rapports sous course-v9/")
+                    "(un seul exigé, R-3273) ; un autre jour : sonde neuve, rapports sous course-v10/")
@@ -1776 +1801 @@
-                               r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v9"), parts)
+                               r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v10"), parts)
```

(L'empreinte complète de la configuration, abrégée ci-dessus, est inchangée : `e7378f89ae39eacd169ff912526a8e998e4f01f0aba235eeaa0bf12e4b195d5d`.) La configuration reste lue sous `course-v9/` : `PIECES` est **égal** à celui du v9. Les rapports d'une sonde du jour faite par les commandes v9 (sous `course-v9/`) restent lus ; un seul rapport de sonde commune du jour reste admis parmi tous les chemins. « -v1 » n'attrape pas « -v10 » (`endswith`, essayé).

Preuves par essai (`tests/test_lancer_course_affinage_mentors_v10.py`) : `test_v10_lanceur_est_le_v9_a_l_epingle_et_aux_chemins_pres` retire l'en-tête v10, défait les seuls remplacements ci-dessus et retrouve le lanceur v9 contre-lu (`b0c7c50d…`) **à l'octet près** ; `test_mutation_v10_un_chiffre_change_est_vu` (artefact : 24 500 → 24 000, plus de retour au v9) ; `test_v10_constantes_du_lanceur` : les seules constantes qui diffèrent du v9 sont les quinze nommées (version, chemins, épingle, sorties), `PIECES`, `ARGUMENTS_COMMANDES`, `COMMANDES_EPINGLEES` et `EMPREINTES_ORCHESTRATEUR` égaux.

## 5. Textes corrigés

| constat | v9 (faux ou flou) | v10 |
|---|---|---|
| 1, majeur | préenregistrement l. 91, 223, 228 ; devis § 3 l. 39 ; rapport v9 point 1 ; commandes § 0 point 3 : « plafond dur de l'étape « proposition » : 60 USD », « l'orchestrateur coupe l'étape » | préenregistrement v10 : § Plafond (plafonds de relais 60 / 30 / 50 ; plafond dur souple 130 au lancement de la proposition ; seuils 100 et 120 ; nœud, code 6), liste d'arrêt « Pendant la course », critères de bonne fin, différentiel v8 → v9 marqué « texte de la v9 corrigé en v10 », différentiel v9 → v10 neuf ; devis v10 § 3 bis neuf (lettre du code, table du rejeu) ; commandes v10 § 0 point 3 et § 9 (code 6 par le budget) ; l'option « porter ce plafond d'étape à 70 » du rapport v9 est sans objet |
| 2, mineur | gabarit de déclaration v9 l. 23 : « configuration v6 » | gabarit v10 : « modèles Claude de la configuration v9 » (mêmes deux modèles) |
| 3, mineur | devis v9 § 3 : « haut » sans dire qu'il n'est pas une borne | devis v10 § 3 : colonne « haut (convention mixte, non une borne) » et une ligne : la borne est le pire cas, 150 |
| 4 à 7, information | — | rien de changé ; dits au différentiel v9 → v10 du préenregistrement (point 6) |

Mutations des textes dans les essais : la phrase fausse de la v9 réintroduite dans le préenregistrement v10 est attrapée ; « 130 USD » remplacé par « 60 USD » est attrapé ; le préenregistrement v9 aurait échoué au même contrôle ; le devis v10 ne contient la phrase fausse que dans la citation qui la dit fausse (essai `test_v10_devis`).

## 6. Essais

> **1070 passed in 756.68s, 0 skipped, 0 failed (264 v10 + 252 v9 + 235 v8 + 175 v7 + 125 v6 + 5 v6b + 14 sonde commune)**, commande du § 4 des commandes v10 (sept fichiers).

- `tests/test_lancer_course_affinage_mentors_v10.py` : **264** essais — les 252 essais v9 portés (lanceur v10, chemins `course-v10/`, commandes et gabarit v10 ; modules auxiliaires renommés `…_pour_v10` pour ne pas croiser ceux du v9 dans une même session) et **12 essais neufs v10** : différentiel reconstitué à l'octet, mutation d'un chiffre, constantes, une course v9 lancée bloque la v10, préenregistrement (plafond dur souple, phrases fausses absentes), mutation des textes, devis v10, commandes v10, gabarit de déclaration v10, gabarits des relevés v10, **règle d'A1 rejouée avec la vraie classe `BudgetV56`** de l'orchestrateur épinglé (sous-processus isolé, `-B`, empreinte de `pole/budget_v56.py` vérifiée), essai à blanc v10 versé (plafond dur 130,0 au manifeste de l'orchestrateur).
- Les fichiers d'essais v9, v8, v7, v6, v6b et de la sonde commune passent encore (inchangés) : 252 + 235 + 175 + 125 + 5 + 14 dans le même passage, aucun saut (`-rs` ne nomme rien) ; après le scellement des commandes et des essais, les 20 essais v10, de commandes et de gabarit rejoués : 20 passed.
- `python -m controle_ia.scellement verifier-arbre .` : 96 problèmes, tous hérités de la branche v9 (compagnons `.sha256` absents de fichiers que la v10 ne touche pas, par exemple sous `docs/notes/rapports-directeur/` et `docs/sources/pdf/`) ; **aucun sur une pièce v10** (vérifié après le scellement de ce rapport).

## 7. Essai à blanc v10

`--a-blanc` dans un dossier neuf hors dépôt (`…/scratchpad/essai-a-blanc-v10-20261118230819`, 23:08:19Z) : **code 0**, sortie d'erreur vide ; la vérification de l'orchestrateur épinglé accepte la configuration v9 ; acte de gel au nom du lanceur v10 (`b0829025…`) et du préenregistrement v10 (`7fc71712…`) ; cinq espèces, 160 cartes classées, parts au pire 150 / 150 / 48 / 48 ; base du devis 41,136, écart −35,536 (coût simulé 5,6) ; `reglages_carbon_v8` : sortie retenue 32 768, pire cas 2,571489 USD (1,285745 au prix du lot) ; **plafonds durs écrits par l'orchestrateur : proposition 130,0, aiguillage 135,2, juges 147,6, étiquettes 144,4** — le mécanisme que disent les textes v10. Versé sous `course-v10/essai-a-blanc-v10/` (15 fichiers et leurs compagnons) ; empreintes : manifeste du lanceur au départ `872f07b0f34282dac49e9eb980033927220419b51f89f775d8e67de4111409b2`, à la fin `ed75fcbbed7487227caef67b413e3c8d89f190189cc48cf772205ef486031826`.

## 8. Commandes v10

Autonomes (aucun renvoi à un texte de commandes antérieur ; chaque bloc se copie seul), chemins `course-v10/`, `/home/user/pieces-affinage-v10/`, `/home/user/sorties-relais-affinage-v10/`, `/home/user/sorties-lanceur-affinage-v10/` ; lancement **détaché** par `setsid nohup … < /dev/null &`, `GO_ID=GO-2026-11-18-14` sur la ligne ; § 2 : empreintes du lanceur v10, du préenregistrement v10, du devis v10 et des trois gabarits v10 ; extraction du lanceur v9 et des essais v9 ajoutée (les essais v10 les lisent) ; § 4 : sept fichiers d'essais ; § 5 : la sonde commune du jour cherchée aussi sous `course-v9/`. Aucune option de relais, aucune borne, aucun argument de commande ne change.

## 9. Points ouverts

1. **Régime « non mesuré (budget) »** (constat 1, désormais écrit) : il demande une proposition au-delà de 100 USD (juges) ou de 120 USD (aiguillage), soit Carbon seize fois au pire cas sans qu'A3 l'arrête et les autres proposeurs près de 3,00 USD par appel ; peu probable, non exclu, probabilité non chiffrée. L'issue est un nœud (code 6), sans dollar au-delà de 150. Le changer demanderait une configuration neuve (attendus ou plafonds de relais des étapes) : non fait, non demandé.
2. Repris de la v9 : coût réel des proposeurs Claude, d'Argon et d'Astra sous 3,00 non mesuré (d'où un « haut » qui n'est pas une borne) ; lecture de la documentation du fournisseur sur la pensée faite par la session principale ; délai de lot de Carbon borné à 1 620 s par l'orchestrateur épinglé ; part au pire de la clé de Google 198 (borne écrite, non une dépense possible ; écrêtage par clé à 150 envisageable dans une version suivante, constat 4 de la contre-lecture v9) ; essais datés du 18 au 30 novembre.
3. **Refus du crochet d'isolement** (rapporté) : une commande composée qui lisait le commit et l'état de `/home/user/ideation-organism` par `git` a été refusée (« commande trop complexe pour vérifier qu'elle reste dans l'arbre isolé »). Je ne l'ai pas rejouée sous une autre forme : la vérification du commit et de l'arbre propre de l'orchestrateur est faite par le lanceur lui-même (essai à blanc, `verifier_orchestrateur`) et par les essais ; j'ai lu les fichiers et leurs empreintes sans `git`. Aucun autre refus.

## 10. Ce qui n'est pas vérifié

Aucun relais réel ni appel amont ; commandes v10 écrites et recoupées par les essais, non jouées ; pensée de Carbon sur les consignes de l'affinage ; coût réel des proposeurs sous 3,00 ; `runs/` et `registres/` du dépôt non ouverts.
