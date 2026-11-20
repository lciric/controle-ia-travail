# Rapport du développeur — corrections C1 à C3 du code de l'étage sur processeur du palier 0b (code v3)

- Auteur : développeur, modèle L′. Pièce de travail (classe C). Travail du 2026-11-20, achevé vers 03:35Z (`date -u` ; premier relevé à 03:11Z, une fois les corrections écrites).
- Mandat : `heritage/palier-0b/code-v2/mandat-developpeur-corrections-code-palier-0b-v3-v1.md` (`a49438e591064c49cee23b47b8cac9ed9ed5c9b38fc2d0db17b271ee9c2c3d8d`), vérifié par `sha256sum -c` de son compagnon avant tout geste ; il garde l'objet et les interdits du mandat v2 (`024e94e5c48c1536ea2b4fec070b891963882ea1ec3644c58a06edd54d271739`, vérifié).
- Textes qui font foi, vérifiés par leur compagnon : préenregistrement v6 (`4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029`) ; contre-lecture du code v2 (`3778fb395dae1e2003ce8236f93c77cfbd6bc78c355417bf0b40e0b5e694c5e5`, « Conforme après corrections ») ; rapport du code v2 (`ca61bf7e89aefe7ffe9e7a62e80ff7da1653668542f8fbd8498909a10e409b75`).
- Point de départ : `code-v2/src`, `tests`, `outils-dev` copiés dans le bloc-notes ; les 48 fichiers ont l'empreinte de la table du § 7 du rapport v2 (outil `verifier_table.py`, « conformes 48, écarts 0 »).
- Code de l'organisme : la copie du dépôt `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/` (celle que nomme le préenregistrement), recopiée dans le bloc-notes pour ne rien écrire dans le dépôt ; ses seize fichiers sont contrôlés par `organisme.verifier_copie` à chaque essai de la garde 17 (au vert). Le code de l'organisme n'a pas été modifié.
- Environnement : Python 3.13.18 ; mêmes bibliothèques que le code v2.

## 0. Verdict

Les trois corrections sont faites ; deux notes (D4, D7) sont traitées, sans changer aucun résultat ; D5, D6, D8, D9 sont laissées pour l'erratum. **Chaque fichier d'essais lancé seul : huit fichiers, 71 passés, 0 échoué. Suite entière : 71 passés, 0 échoué (762 s).** Le fichier « aucune graine décisive » passe seul (0,05 s) et en suite entière. **Banc des défauts `mutations_v2.py` (50 défauts : les 41 de la v1 et neuf nouveaux), rejoué en entier : 50 appliqués, 50 vus, témoins tous au vert (41 sélections).** Mêmes graines, mêmes appels : les sorties du code v3 ont, clé par clé, les empreintes de celles du code v2 (57 sur 57). Aucun écart au texte tranché ; aucun refus d'outil.

## 1. Corrections, une par une

### C1 — l'essai « aucune graine décisive » échouait lancé seul

- Cause : `assert GR.REFUS and all(...)` ; seul, le fichier n'avait aucun refus consigné.
- Correction (`tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py`) : les quatre contrôles du journal sont gardés, sans exiger de refus préalable ; puis l'essai **éprouve lui-même le verrou** : une demande de graine par couche décisive (« decisif », « confirmation »), sans autorisation, chacune refusée (`GraineRefusee`), consignée dans `REFUS` à la suite des refus déjà présents, sans aucune entrée nouvelle au `JOURNAL` ni dans les étiquettes de la fabrique ; enfin `REFUS` non vide et fait des seules couches décisives, et les couches dérivées restent « essai » et « essai-de-forme ». Le sens est gardé et renforcé : en suite entière, il lit les refus des autres essais ; seul, il a les siens.
- Banc : défaut « refus-non-consigne » (le refus n'est plus écrit dans `REFUS`), essai joué seul. Je n'ai mis aucun défaut qui ouvre le verrou : il ferait dériver une graine de la couche décisive dans la copie mutée.

### C2 — bras 4b : la copie étrangère servie n'avait ni empreinte ni vérification

- `mecanique.jouer_source` : au bras 2, l'empreinte canonique de chaque vue (`registre.empreinte_vue`, SHA-256 du JSON canonique de la liste d'entrées) est prise au moment où le bras la reçoit (`empreintes_vues_bras_2`) ; la sortie porte aussi le numéro de la source (`source`).
- `mecanique.copie_scellee_4b(sortie_etrangere)` : la copie que l'orchestrateur dépose au bras 4b — la source étrangère, ses quatre vues du bras 2 et leurs empreintes ; une copie incomplète (bras 2 non joué) arrête. `jouer_jeu_diagnostic` dépose cette copie (paramètre `copie_etrangere_4b`, qui remplace `vues_etrangeres_4b` ; seul appelant).
- `registre.verifier_vue_etrangere_4b(vue, empreinte_deposee, source_propre, source_etrangere)`, appelée à chaque génération du bras 4b avant que la vue soit servie (et avant le retrait des champs pour le repli) : arrêt si la copie déposée vient de la source propre (« ce serait le bras 2 ») ; si une entrée servie est de la source propre ; si une entrée n'a pas été écrite par la continuation du bras 2 de la source étrangère (origine, source, bras de la provenance) ; si l'empreinte de la vue servie n'est pas celle déposée.
- Essais (dans l'essai de la garde 27) : cas sain — chaque génération du jeu à deux sources passe le contrôle, et les quatre vues de la source 1 servies à la source 0 le passent une à une ; artefacts — registre propre du bras 2 déposé (contrôle seul, et de bout en bout par `jouer_source` au bras 4b : arrêt dès la première génération), entrée de la source propre déclarée étrangère, copie altérée après le dépôt (un champ `gardee` changé), entrées de la course de la source étrangère (non de son bras 2), copie incomplète.
- Banc : cinq défauts — registre propre déposé au 4b (`jouer_jeu_diagnostic`) ; copie de la source propre acceptée ; entrée de la source propre acceptée ; empreinte non comparée ; contrôle retiré de `jouer_source`.

### C3 — `Mondes.__init__` exigeait `p_passage_vraie` plus que `strates_requises`

- `statistique.Mondes(rng, S, dose, f, passage_requis)` : `simuler` passe `"p_passage_vraie" in strates_requises(prop, dose, bras)`. Requise, la fréquence est lue par `_f` (strate vide : arrêt, comme avant) ; non requise, elle n'est pas lue et les passages valent None. Les tirages `rng.random((S, d))` sont faits dans tous les cas : le flux de la graine du monde est inchangé, donc tout le reste aussi. Employer des passages non tirés arrête (`jouer_bras`, avant la lecture) : jamais de repli.
- Essai neuf (`test_passage_vraie_exige_seulement_quand_les_strates_requises_l_exigent`) : un sourd à la dose 0,5 joue sans la strate du passage et rend exactement les mêmes M1 qu'avec elle ; le lecteur aux bras 1 à 3 à la dose 0,5 arrête sans elle ; des mondes tirés sans elle, servis au bras 3 d'un lecteur, arrêtent à l'emploi.
- Banc : défaut « passage-exige-sans-besoin ».

## 2. Notes D4 à D9

| note | sort | pourquoi |
|---|---|---|
| D4 (table des critères incomplète) | **traitée** | `analyse.table_des_criteres` arrête (`ArretAnalyse`) si `gardes` n'a pas exactement les gardes 1 à 27, ou si une garde autre que la 17 vaut None. Une table complète rend la même table qu'en v2 ; aucune issue ni lecture n'est ajoutée : une table partielle ne s'écrit plus. Essai : trois tables incomplètes arrêtent ; table complète, « C6 tenu » ; garde 17 None, « non établi » ; une garde en échec, « en échec ». Banc : « table-des-gardes-incomplete ». |
| D5 (mémoire du cache de `_loi_exacte`) | laissée | Code seul, mais la bonne taille se mesure à l'essai de forme (temps et mémoire), que ce mandat ne permet pas à pleine taille. |
| D6 (`Autorisation` sans comparaison à `PREENREGISTREMENT_SHA256`) | laissée | Lier le verrou à l'empreinte de la v6 est un choix de texte : le texte qui sera scellé n'est pas encore fixé (erratum attendu), et « contre-lu » ne se vérifie pas par programme. Pour l'erratum. |
| D7 (compteurs du jeu à sources étrangères perdus) | **traitée** | `mondes.generer_jeu_avec_etrangeres` cumule, par source, les compteurs de B1 (iii) : mondes sources tirés (y compris ceux des tours neufs), mondes cibles tentés (suites refaites comprises), tours retirés ; la suite les porte. Les compteurs ne font que compter : aucun tirage n'en dépend (les empreintes des registres et mesures du jeu sont celles du code v2). Essai : chaque suite du jeu compte des sous-lois de source acceptées. Banc : « compteurs-du-jeu-perdus ». |
| D8 (étalonnage, taille « nan ») | laissée | Changer « non atteignable » en arrêt change le sort d'un cas (dégénéré, mais réel) : c'est une règle de lecture, pour l'erratum. |
| D9 (plis non stratifiés) | laissée | Stratifier change les plis, donc les exactitudes : change des résultats. |

## 3. Essais

Lancement : `PYTHONPATH=<code-v3>/src HERITAGE_DEPOT=/home/user/controle-ia-travail HERITAGE_COPIE_ORGANISME=<bloc-notes>/code-organisme-94bfd92/orchestrator python3 -B -m pytest -q -p no:cacheprovider CHEMIN` (chemins absolus), par l'outil `lancer_essais.py` du bloc-notes : un processus par fichier, puis un processus pour la suite entière ; dossier courant dans le bloc-notes ; rien n'est écrit dans le dépôt.

| fichier d'essais | seul | durée seul |
|---|---|---|
| `etapes` | 5 passés | 31 s |
| `gardes` | 17 passés | 2 s |
| `mecanique` | **9 passés** (8 de la v2 et l'essai neuf de C3) | 282 s |
| `mondes` | 9 passés | 289 s |
| `organisme` | 5 passés | 118 s |
| `outils` | 15 passés | 9 s |
| `statistique` | 10 passés | 5 s |
| `zz_aucune_graine_decisive` | **1 passé** (échouait seul en v2) | 0,05 s |
| total, un processus par fichier | **71 passés, 0 échoué** | |
| **suite entière, un processus** | **71 passés, 0 échoué** | 762 s |

Journaux : `travail/essais-fichiers-v1.log`, `travail/essais-suite-v1.log` (bloc-notes). 5 + 17 + 9 + 9 + 5 + 15 + 10 + 1 = 71, le même compte qu'en suite entière. Les deux lancements ont tourné en même temps que le banc (quatre processeurs), d'où des durées voisines de celles de la contre-lecture.

Autres contrôles :
- Mêmes résultats que le code v2 (outil `empreintes_resultats.py`, graines « essai », couche statistique : lecteur réglé pour l'héritage à 0,5 et à 0, lecteur réglé pour la tenue à 0,25, sourd qui paie à 0,5, copieur à 0,25, 400 sources, bras 1 à 4b aux doses non nulles ; couche mécanique : le jeu à deux sources de la garde 27, bras 1 à 4b, registres, mesures, entrées servies) : **57 empreintes sur 57 identiques** entre le paquet du code v2 (dossier du dépôt, lu seulement) et celui du code v3.
- Remplacements du banc v2 : chacun trouvé exactement une fois dans le code v3 (outil `verifier_remplacements.py` : « défauts 50, problèmes 0 »).

## 4. Banc des défauts (règle R4)

`outils-dev/mutations_v2.py` : les 41 défauts de `mutations_v1.py`, repris à l'identique, et neuf nouveaux (C1 : 1 ; C2 : 5 ; C3 : 1 ; D4 : 1 ; D7 : 1). Joué en entier, en deux moitiés parallèles (même outil, identifiants donnés en argument ; témoins joués dans chaque moitié pour ses propres sélections).

Résultat : **50 défauts appliqués, 50 vus** ; témoins **au vert** dans les deux moitiés (21 et 20 sélections, 41 en tout). Chaque défaut est vu par un essai en échec (« 1 failed » ; aucun par une erreur de collecte ou d'import). Sorties : `outils-dev/mutations-v2-sortie-partie-a-v1.json` (29 défauts, 29 vus) et `outils-dev/mutations-v2-sortie-partie-b-v1.json` (21 défauts, 21 vus).

Les neuf défauts neufs :

| défaut | correction | fichier muté | essai qui le voit | durée |
|---|---|---|---|---|
| refus-non-consigne | C1 | `graines.py` | `zz_aucune_graine_decisive`, **fichier joué seul** | 0,3 s |
| registre-propre-au-bras-4b | C2 | `mecanique.py` (`jouer_jeu_diagnostic`) | `mecanique -k garde_27` | 39 s |
| copie-4b-de-la-source-propre-acceptee | C2 | `registre.py` | `mecanique -k garde_27` | 42 s |
| entree-propre-au-4b-acceptee | C2 | `registre.py` | `mecanique -k garde_27` | 42 s |
| empreinte-4b-non-verifiee | C2 | `registre.py` | `mecanique -k garde_27` | 41 s |
| bras-4b-sans-controle | C2 | `mecanique.py` (`jouer_source`) | `mecanique -k garde_27` | 43 s |
| passage-exige-sans-besoin | C3 | `statistique.py` | `mecanique -k passage_vraie` | 0,4 s |
| table-des-gardes-incomplete | D4 | `analyse.py` | `statistique -k regles_de_lecture` | 0,4 s |
| compteurs-du-jeu-perdus | D7 | `mondes.py` | `mecanique -k garde_27` | 40 s |

Les 41 défauts de la v1, rejoués sur le code v3 sans changement de leurs remplacements : 41 vus, dont les sept que la contre-lecture n'avait pas pu confirmer (S8 (i) 188 s, S8 (ii) 186 s, graines des bras, M10, S9, « atteint », sorties non vérifiées : vus).

## 5. Différentiels par fichier (`diff -u`, code v2 → code v3)

Fichiers changés : cinq modules (`registre`, `mecanique`, `statistique`, `analyse`, `mondes`), trois fichiers d'essais (`zz_aucune_graine_decisive`, `mecanique`, `statistique`), et un outil neuf (`mutations_v2.py`, donné en différentiel depuis `mutations_v1.py`, gardé intact). Les autres fichiers sont à l'octet ceux du code v2.

#### `1-registre.py.diff`

```diff
--- code-v2/src/controle_ia/heritage_etage_processeur_v1/registre.py
+++ code-v3/src/controle_ia/heritage_etage_processeur_v1/registre.py
@@ -255,7 +255,8 @@
 def verifier_registre_etranger(bras, sha_registre_servi_au_depart, sha_registre_etranger, sha_registre_source_propre):
     """Garde 27 : la copie du registre étranger n'est servie qu'aux bras 4a et 4b ; au bras 4a, la copie servie au départ a
     l'empreinte du registre de la course de la source étrangère, jamais celle de la source propre ; aucun bras du critère ne la
-    reçoit. `sha_registre_servi_au_depart` : None si rien n'est servi au départ (bras 1 et 2)."""
+    reçoit. `sha_registre_servi_au_depart` : None si rien n'est servi au départ (bras 1, 2 et 4b). Au bras 4b, rien n'est
+    servi au départ ; la copie servie à chaque génération est contrôlée par `verifier_vue_etrangere_4b` (code v3, C2)."""
     if bras == "4a":
         if sha_registre_servi_au_depart == sha_registre_source_propre:
             raise ArretRegistre("garde 27 : registre de la source propre servi au bras 4a (ce serait le bras 3) : arrêt")
@@ -269,6 +270,33 @@
     return True
 
 
+def empreinte_vue(vue):
+    """Empreinte canonique d'une vue servie (liste d'entrées ; une vue vide ou « aucune » vaut la liste vide)."""
+    return sha256_texte(json_canonique(list(vue or [])))
+
+
+def verifier_vue_etrangere_4b(vue_servie, empreinte_deposee, source_propre, source_etrangere):
+    """Garde 27 au bras 4b (code v3, C2 ; B7 bis : ce qui est servi à chaque génération est le registre que tient, à la même
+    génération, le bras 2 de la source étrangère, et « son empreinte est celle du registre de la source étrangère »). Avant de
+    servir la copie d'une génération : la copie ne vient pas de la source propre ; chaque entrée servie a été écrite par la
+    continuation du bras 2 de la source étrangère ; l'empreinte canonique de la copie servie est celle que l'orchestrateur a
+    déposée avec elle, prise sur la vue du bras 2 de la source étrangère au moment où ce bras l'a reçue. Arrêt sinon : le
+    registre de la source propre servi au bras 4b (ce serait le bras 2), ou une copie altérée ou d'une autre origine."""
+    propre, etrangere = f"source-{source_propre}", f"source-{source_etrangere}"
+    if etrangere == propre:
+        raise ArretRegistre("garde 27 : copie déposée au bras 4b venue de la source propre (ce serait le bras 2) : arrêt")
+    for e in vue_servie or []:
+        p = e.get("provenance") or {}
+        if p.get("source") == propre:
+            raise ArretRegistre("garde 27 : entrée de la source propre servie au bras 4b (ce serait le bras 2) : arrêt")
+        if p.get("source") != etrangere or p.get("bras") != "bras-2" or p.get("origine") != "continuation":
+            raise ArretRegistre("garde 27 : une entrée servie au bras 4b n'est pas du bras 2 de la source étrangère : arrêt")
+    if empreinte_vue(vue_servie) != empreinte_deposee:
+        raise ArretRegistre("garde 27 : la copie servie au bras 4b n'a pas l'empreinte de la vue du bras 2 de la source "
+                            "étrangère : arrêt")
+    return True
+
+
 def retour(entrees_de_la_generation):
     """Le retour ordinaire servi au proposeur : une classe (ou le statut de budget) et un coût par tentative."""
     out = {"retour": [{"classe": e["resultat"]["classe"], "cout_usd": e["resultat"]["cout_usd"]} for e in entrees_de_la_generation]}
```

#### `2-mecanique.py.diff`

```diff
--- code-v2/src/controle_ia/heritage_etage_processeur_v1/mecanique.py
+++ code-v3/src/controle_ia/heritage_etage_processeur_v1/mecanique.py
@@ -23,8 +23,9 @@
 from .mondes import BORNES_GELEES, ecrire_monde, ensemble_exclu, generer_suite, lire_csv, verifier_tranche_jamais_servie
 from .organisme import DesaccordOrganisme, comparer_verdicts
 from .proposeurs import PartsServies, proposer
-from .registre import (Registre, exiger_historique_vide, nouvelle_entree, provenance, verifier_bras_1_non_servi,
-                       verifier_cloisonnement, verifier_finale_sans_ecriture, verifier_registre_etranger)
+from .registre import (Registre, empreinte_vue, exiger_historique_vide, nouvelle_entree, provenance, verifier_bras_1_non_servi,
+                       verifier_cloisonnement, verifier_finale_sans_ecriture, verifier_registre_etranger,
+                       verifier_vue_etrangere_4b)
 
 ORIGINES_NON_PLANTEES = ("base", "composition", "copie")
 STRATES = ("vraie-source", "vraie-cible", "fausse") + tuple("non-plantee-" + o for o in ORIGINES_NON_PLANTEES)
@@ -230,12 +231,24 @@
             "appariees": sorted(vraies), "exclues_appariees": sorted(exclues)}
 
 
-def jouer_source(ctx, bras=("1", "2", "3"), suite=None, registre_etranger=None, vues_etrangeres_4b=None,
+def copie_scellee_4b(sortie_etrangere):
+    """La copie que l'orchestrateur dépose au bras 4b (garde 27 ; code v3, C2) : la source étrangère, la liste, par
+    génération, des vues du registre que tenait son bras 2 au début de cette génération, et l'empreinte canonique de chacune,
+    prise au moment où le bras 2 l'a reçue (`empreintes_vues_bras_2` de la sortie de la source étrangère)."""
+    vues, empreintes = sortie_etrangere["vues_bras_2"], sortie_etrangere["empreintes_vues_bras_2"]
+    if len(vues) != MONDES_CIBLES_D_EVOLUTION + 1 or len(empreintes) != len(vues):
+        raise ArretMecanique("garde 27 : copie du bras 2 de la source étrangère incomplète (bras 2 non joué ?) : arrêt")
+    return {"source": sortie_etrangere["source"], "vues": [list(v) for v in vues], "empreintes": list(empreintes)}
+
+
+def jouer_source(ctx, bras=("1", "2", "3"), suite=None, registre_etranger=None, copie_etrangere_4b=None,
                  historique_de_depart=None):
     """Joue une source. Rend {"suite", "registre_source", "bras": {bras: {mesure, reliquats, entrees_servies, registre}},
-    "frequences", "exclu", "vues_bras_2"}. `registre_etranger` (bras 4a : le registre de la course de la source étrangère) et
-    `vues_etrangeres_4b` (bras 4b : la liste, par génération, du registre que tient le bras 2 de la source étrangère au début de
-    cette génération) sont des copies scellées déposées par l'orchestrateur (garde 27)."""
+    "frequences", "exclu", "vues_bras_2", "empreintes_vues_bras_2", "source"}. `registre_etranger` (bras 4a : le registre de la
+    course de la source étrangère) et `copie_etrangere_4b` (bras 4b : `copie_scellee_4b` de la sortie de la source étrangère —
+    la liste, par génération, du registre que tient le bras 2 de la source étrangère au début de cette génération, avec
+    l'empreinte de chaque vue) sont des copies scellées déposées par l'orchestrateur (garde 27). Au bras 4b, chaque vue est
+    contrôlée avant d'être servie (`registre.verifier_vue_etrangere_4b`)."""
     exiger_historique_vide(historique_de_depart)
     exiger_taux_egaux({b: ctx.taux for b in bras})
     os.makedirs(ctx.dossier)
@@ -258,7 +271,7 @@
     sha_etranger = registre_etranger.empreinte_fichier() if registre_etranger is not None else None
     etiquettes = {}
     sortie = {"suite": suite, "registre_source": rs, "bras": {}, "frequences": freqs, "exclu": exclu, "vues_bras_2": [],
-              "sha_registre_source": sha_source}
+              "empreintes_vues_bras_2": [], "sha_registre_source": sha_source, "source": ctx.source}
     dossiers_bras = {b: os.path.join(ctx.dossier, f"bras-{b}") for b in bras}
     for b in bras:
         d = dossiers_bras[b]
@@ -280,15 +293,18 @@
             finale = gen == MONDES_CIBLES_D_EVOLUTION + 1
             mode = "sans_resultat_ni_gardee" if (ctx.repli and b != "1") else VUE_PAR_BRAS[b]
             if b == "4b":
-                if vues_etrangeres_4b is None:
+                if copie_etrangere_4b is None:
                     raise ArretMecanique("garde 27 : bras 4b sans registre étranger déposé")
-                vue = vues_etrangeres_4b[gen - 1]
+                vue = copie_etrangere_4b["vues"][gen - 1]
+                verifier_vue_etrangere_4b(vue, copie_etrangere_4b["empreintes"][gen - 1], ctx.source,
+                                          copie_etrangere_4b["source"])
                 if ctx.repli:
                     vue = [{k: v for k, v in e.items() if k not in ("resultat", "gardee")} for e in vue]
             else:
                 vue = r.vue(mode)
             if b == "2":
                 sortie["vues_bras_2"].append(r.vue("entiere"))
+                sortie["empreintes_vues_bras_2"].append(empreinte_vue(sortie["vues_bras_2"][-1]))
             verifier_cloisonnement(d, vue, [dossiers_bras[x] for x in bras if x != b] + [d_src])
             avant = r.octets()
             if finale:
@@ -320,5 +336,5 @@
         e = premieres[(k + 1) % S]
         ctx = ContexteSource(graines, bases[k], prop, dose, taux, os.path.join(dossier, f"source-{k}-diagnostic"), **kw)
         secondes.append(jouer_source(ctx, ("4a", "4b"), suite=suites[k], registre_etranger=e["registre_source"],
-                                     vues_etrangeres_4b=e["vues_bras_2"]))
+                                     copie_etrangere_4b=copie_scellee_4b(e)))
     return premieres, secondes
```

#### `3-statistique.py.diff`

```diff
--- code-v2/src/controle_ia/heritage_etage_processeur_v1/statistique.py
+++ code-v3/src/controle_ia/heritage_etage_processeur_v1/statistique.py
@@ -22,7 +22,7 @@
                          GENERATIONS_COURSE_SOURCE, MONDES_CIBLES_D_EVOLUTION, P_FAUSSE_BASE, PROBA_DEUX_TENTATIVES,
                          REPERE_LECTURE)
 from .cout import cout_lecture_par_appel, retrait_v1, retrait_v2_vectorise
-from .frequences import ArretFrequences, exiger_strates
+from .frequences import ArretFrequences, exiger_strates, strates_requises
 from .mondes import PAIRES_DE_LA_SOURCE, nombre_de_dependantes
 from .proposeurs import p_vraie, part_generaliste
 
@@ -38,9 +38,14 @@
 
 
 class Mondes:
-    """Tout ce que la graine du monde fixe pour S sources : classes des lois plantées et passages des compositions vraies."""
+    """Tout ce que la graine du monde fixe pour S sources : classes des lois plantées et passages des compositions vraies.
 
-    def __init__(self, rng, S, dose, f):
+    `passage_requis` (code v3, C3) : vrai si `frequences.strates_requises` exige `p_passage_vraie` pour le proposeur, la dose et
+    les bras joués (un lecteur aux bras 3 ou 4a, à dose non nulle). Sinon la fréquence n'est pas lue : les tirages du
+    générateur sont faits de même (le flux de la graine du monde ne change pas) et les passages valent None ; les employer
+    arrête (`jouer_bras`), jamais de repli."""
+
+    def __init__(self, rng, S, dose, f, passage_requis):
         d = nombre_de_dependantes(dose)
         self.S, self.d = S, d
         self.tient_src_v = rng.random((S, DOMAINES_A_LOI_SOURCE)) < _f(f, "p_tient_vraie_source")
@@ -51,7 +56,13 @@
             self.paires.append(perm[:, w * d:(w + 1) * d])
             self.tient_v.append(rng.random((S, DOMAINES_A_LOI_CIBLE)) < _f(f, "p_tient_vraie_cible"))  # d premières : dépendantes
             self.tient_f.append(rng.random((S, DOMAINES_A_LOI_CIBLE)) < _f(f, "p_tient_fausse"))
-            self.passage.append(rng.random((S, d)) < (_f(f, "p_passage_vraie") if d else 0.0))
+            u = rng.random((S, d))
+            if not d:
+                self.passage.append(u < 0.0)
+            elif passage_requis:
+                self.passage.append(u < _f(f, "p_passage_vraie"))
+            else:
+                self.passage.append(None)
 
 
 def _appels(rng, S, n_servi, paie, repere, regle):
@@ -216,6 +227,9 @@
             m = np.minimum(k, P)
             touches = _hypergeometrique(rng, dispo.sum(axis=1), P - dispo.sum(axis=1), m)
             examinees = _choisir_parmi(rng, dispo, touches)
+            if mondes.passage[w] is None:
+                raise ArretFrequences("passages des compositions vraies non tirés (p_passage_vraie non requise) mais employés "
+                                      f"au bras {bras} : arrêt (liste d'arrêt, point 4)")
             passent = examinees & mondes.passage[w]
             n_vp = passent.sum(axis=1)
             n_fp = _binomiale(rng, np.maximum(2 * m - touches, 0), _f(f, "p_faux_passage"))
@@ -288,7 +302,7 @@
     exiger_strates(f, prop, dose, bras)
     if sorted(f) != sorted(CLES_FREQUENCES):
         raise ArretFrequences("fréquences mal formées")
-    mondes = Mondes(rng_monde, S, dose, f)
+    mondes = Mondes(rng_monde, S, dose, f, "p_passage_vraie" in strates_requises(prop, dose, bras))
     src = course_source(rng_source, prop, mondes, f, taux, repere, regle, repli)
     roul = roulement(S, taille_tirage)
     etrangere = src.roule(roul) if "4a" in bras else None
```

#### `4-analyse.py.diff`

```diff
--- code-v2/src/controle_ia/heritage_etage_processeur_v1/analyse.py
+++ code-v3/src/controle_ia/heritage_etage_processeur_v1/analyse.py
@@ -202,7 +202,11 @@
 def table_des_criteres(c1_cases, c4_cases, puissances, c3_par_nombre, c5_parts, gardes):
     """La table des critères, sans issue. `c1_cases`, `c4_cases` : {case : statut} ; `puissances` : voir `n_de_l_etage` ;
     `c3_par_nombre` : {k : taux} ; `c5_parts` : {(dose, k) : part} ; `gardes` : {garde : (cas sain passé, artefact arrêté)}
-    (la garde 17 non jouée vaut None)."""
+    (la garde 17 non jouée vaut None). Code v3, note D4 : `gardes` porte exactement les gardes 1 à 27 de B9, chacune jouée sauf
+    la 17 ; une table incomplète arrête (C6 dit « toutes tenues », jamais sur une liste partielle)."""
+    if sorted(gardes) != list(range(1, 28)) or any(v is None for g, v in gardes.items() if g != 17):
+        raise ArretAnalyse(f"C6 : table des gardes incomplète (attendu les gardes 1 à 27, chacune jouée sauf la 17 ; reçu "
+                           f"{sorted(gardes)}) : arrêt")
     c4_tenue_par_nombre = {}
     for cle, st in c4_cases.items():  # clé : (nombre de sources, proposeur, taux d'échec)
         k = cle[0]
```

#### `5-mondes.py.diff`

```diff
--- code-v2/src/controle_ia/heritage_etage_processeur_v1/mondes.py
+++ code-v3/src/controle_ia/heritage_etage_processeur_v1/mondes.py
@@ -400,12 +400,15 @@
     """B7 bis (version 4, point 6) : les suites d'un jeu de sources où les bras 4a et 4b se jouent ; la source étrangère de la
     source k est la source k + 1 (la première pour la dernière). Les mondes sources sont tirés d'abord ; puis les mondes cibles
     de chaque source, séparés aussi de la source étrangère. Une suite retirée (tour neuf) change sa source : les mondes cibles
-    de la source qui la prend pour étrangère sont alors refaits. Rend la liste des suites."""
+    de la source qui la prend pour étrangère sont alors refaits. Rend la liste des suites. Code v3, note D7 : les compteurs de
+    B1 (iii) de chaque source (mondes sources tirés, mondes cibles tentés, suites refaites comprises, et tours retirés) sont
+    cumulés et portés par sa suite ; ils ne font que compter, aucun tirage n'en dépend."""
     S = len(bases)
     if S < 2:
         raise ArretGenerateur("B7 bis : au moins deux sources")
     tours = [0] * S
-    sources = [generer_source(graines, _base_du_tour(bases[k], 0), dose, bornes)[0] for k in range(S)]
+    cumul = [Compteurs() for _ in range(S)]
+    sources = [generer_source(graines, _base_du_tour(bases[k], 0), dose, bornes, cumul[k])[0] for k in range(S)]
     suites = [None] * S
     a_faire = list(range(S))
     garde = 0
@@ -416,6 +419,7 @@
         k = a_faire.pop(0)
         b = _base_du_tour(bases[k], tours[k])
         s = Suite()
+        s.compteurs = cumul[k]
         s.source = sources[k]
         paires = tirer_paires(graines.g(**b, monde="paires", role="paires"), dose)
         ok = True
@@ -431,9 +435,10 @@
             suites[k] = s
             continue
         tours[k] += 1
+        cumul[k].tours += 1
         if tours[k] >= bornes.tours_par_suite:
             raise ArretGenerateur(f"bornes de la construction épuisées : suite {k}, {bornes.tours_par_suite} tours")
-        sources[k] = generer_source(graines, _base_du_tour(bases[k], tours[k]), dose, bornes)[0]
+        sources[k] = generer_source(graines, _base_du_tour(bases[k], tours[k]), dose, bornes, cumul[k])[0]
         a_faire.insert(0, k)
         precedente = (k - 1) % S
         if precedente != k and precedente not in a_faire:
```

#### `6-test_zz_aucune_graine_decisive.py.diff`

```diff
--- code-v2/tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py
+++ code-v3/tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py
@@ -1,6 +1,12 @@
 """Essai final (annexe C ; liste d'arrêt, point 1) : à la fin de la suite d'essais, aucune graine des couches « decisif » ou
 « confirmation » n'a été dérivée dans ce processus ; toute tentative de le faire a été refusée et consignée. Ce fichier est nommé
-pour être joué le dernier (ordre alphabétique des fichiers d'essais)."""
+pour être joué le dernier (ordre alphabétique des fichiers d'essais).
+
+Code v3, correction C1 : l'essai passe aussi joué seul. Il provoque lui-même, en fin d'essai, une demande de graine de chacune
+des deux couches décisives sans autorisation ; chacune doit être refusée et consignée, et rien ne doit avoir été dérivé. Les
+refus déjà consignés par les autres essais du même processus (suite entière) sont lus de même."""
+
+import pytest
 
 from controle_ia.heritage_etage_processeur_v1 import graines as GR
 
@@ -10,5 +16,18 @@
     assert "decisif" not in derivees and "confirmation" not in derivees, derivees
     assert all(GR.couche_de(e) not in GR.COUCHES_DECISIVES for _, e in GR.JOURNAL)
     assert set(derivees) <= {"essai", "essai-de-forme"}, derivees  # aucun étalonnage, aucune couche mécanique ni d'audit
-    # les refus consignés sont tous des refus de couches décisives (essais des refus)
+    # les refus consignés par les autres essais sont tous des refus de couches décisives (essais des refus)
+    assert all(r.split("|", 1)[0] in ("couche=decisif", "couche=confirmation") for r in GR.REFUS)
+    # le verrou, éprouvé ici même : une demande par couche décisive, refusée, consignée, rien de dérivé
+    journal_avant, refus_avant = list(GR.JOURNAL), list(GR.REFUS)
+    g = GR.Graines()
+    demandees = []
+    for couche in GR.COUCHES_DECISIVES:
+        e = GR.etiquette(couche=couche, famille="essai-final", role="verrou")
+        demandees.append(e)
+        with pytest.raises(GR.GraineRefusee):
+            g.generateur(e)
+    assert GR.REFUS == refus_avant + demandees
+    assert GR.JOURNAL == journal_avant and g.etiquettes == []
     assert GR.REFUS and all(r.split("|", 1)[0] in ("couche=decisif", "couche=confirmation") for r in GR.REFUS)
+    assert set(GR.couches_derivees()) <= {"essai", "essai-de-forme"}
```

#### `7-test_mecanique.py.diff`

```diff
--- code-v2/tests/test_heritage_etage_processeur_v1_mecanique.py
+++ code-v3/tests/test_heritage_etage_processeur_v1_mecanique.py
@@ -1,7 +1,8 @@
 """Essais de la couche mécanique (B2) : le lecteur ne compose rien dans une course source et l'ensemble exclu d'un générateur
 sain y est vide ; garde 13 (générateur et copies) ; gardes 23 et 24 (S8) ; garde 27 (bras de diagnostic) ; le multiplicateur de
 la tenue ne s'applique pas aux entrées étrangères du bras 4b ; huit fréquences et strate vide ; reproductibilité à l'octet d'une
-source. Graines de la couche « essai »."""
+source. Graines de la couche « essai ». Code v3 : copie servie au bras 4b contrôlée (C2) ; strate du passage exigée comme
+`strates_requises` l'exige (C3) ; compteurs du jeu à sources étrangères (note D7)."""
 
 import os
 
@@ -111,6 +112,28 @@
         FR.exiger_strates({k: v for k, v in f.items() if k != "p_faux_passage"}, prop("sourd-paie"), 0.5, ("1", "2", "3"))
 
 
+def test_passage_vraie_exige_seulement_quand_les_strates_requises_l_exigent():
+    """Code v3, C3 : `statistique.Mondes` n'exige `p_passage_vraie` que si `frequences.strates_requises` l'exige (un lecteur
+    aux bras 3 ou 4a, à dose non nulle) ; ailleurs la strate vide ne bloque rien et ne change aucun nombre ; employée sans
+    avoir été tirée, elle arrête."""
+    g = graines()
+    sans_passage = dict(FREQUENCES_D_ESSAI, p_passage_vraie=None)
+    assert "p_passage_vraie" not in FR.strates_requises(prop("sourd-paie"), 0.5, ("1", "2", "3"))
+    a = _stat(g, sans_passage, "sourd-paie", 0.5, 200, "passage-non-requis")
+    b = _stat(g, FREQUENCES_D_ESSAI, "sourd-paie", 0.5, 200, "passage-non-requis")
+    assert all(np.array_equal(a[x], b[x]) for x in "123")
+    lecteur = prop("lecteur-heritage", **LECTEUR)
+    assert "p_passage_vraie" in FR.strates_requises(lecteur, 0.5, ("1", "2", "3"))
+    with pytest.raises(FR.ArretFrequences):
+        _stat(g, sans_passage, "lecteur-heritage", 0.5, 200, "passage-requis")
+    m = ST.Mondes(g.g(couche="essai", famille="passage-non-tire", role="monde"), 50, 0.5, sans_passage, False)
+    assert all(p is None for p in m.passage)
+    src = ST.course_source(g.g(couche="essai", famille="passage-non-tire", role="source"), lecteur, m, sans_passage, 0.25)
+    with pytest.raises(FR.ArretFrequences, match="non tirés"):
+        ST.jouer_bras(g.g(couche="essai", famille="passage-non-tire", bras="3", role="echantillonnage"), lecteur, m,
+                      sans_passage, 0.25, "3", src)
+
+
 def test_garde_23_equivalence_s8_ii(couches):
     g, f = couches["g"], couches["f"]
     rng = g.g(couche="essai", famille="garde-23", role="intervalle")
@@ -174,6 +197,34 @@
     assert P.propre_gardee(vue_etrangere, 1, "2") is True
     assert P.propre_gardee(vue_etrangere, 0, "4b") is False
     assert P.propre_gardee(premieres[0]["vues_bras_2"][3], 0, "2") is True
+    # note D7 (code v3) : les compteurs de B1 (iii) du jeu portent aussi les mondes sources tirés
+    assert all(s.compteurs.tirages["sous-loi-source"][1] > 0 for s in suites)
+    # code v3, C2 : au bras 4b, chaque copie servie est contrôlée par son origine et par l'empreinte déposée avec elle (cas
+    # sain : chaque génération du jeu ci-dessus, et ici les quatre vues de la source 1 servies à la source 0)
+    copie = MC.copie_scellee_4b(premieres[1])
+    assert copie["source"] == 1 and copie["empreintes"] == premieres[1]["empreintes_vues_bras_2"]
+    assert copie["empreintes"] == [R.empreinte_vue(v) for v in premieres[1]["vues_bras_2"]]
+    assert vue_etrangere and all(R.verifier_vue_etrangere_4b(v, s, 0, 1) for v, s in zip(copie["vues"], copie["empreintes"]))
+    # artefact : le registre propre du bras 2 servi au bras 4b (ce serait le bras 2)
+    propre = MC.copie_scellee_4b(premieres[0])
+    with pytest.raises(R.ArretRegistre, match="copie déposée au bras 4b venue de la source propre"):
+        R.verifier_vue_etrangere_4b(propre["vues"][0], propre["empreintes"][0], 0, propre["source"])
+    with pytest.raises(R.ArretRegistre, match="entrée de la source propre servie au bras 4b"):
+        R.verifier_vue_etrangere_4b(propre["vues"][3], propre["empreintes"][3], 0, 1)
+    ctx = MC.ContexteSource(g, bases[0], prop("lecteur-tenue", tau=2.0), 0.25, 0.25, str(tmp_path / "artefact-4b"))
+    with pytest.raises(R.ArretRegistre, match="venue de la source propre"):
+        MC.jouer_source(ctx, ("4b",), suite=suites[0], copie_etrangere_4b=propre)
+    # artefact : copie altérée après le dépôt (une entrée changée) : l'empreinte ne tient plus
+    alteree = [dict(e) for e in copie["vues"][3]]
+    alteree[0] = dict(alteree[0], gardee=not alteree[0]["gardee"])
+    with pytest.raises(R.ArretRegistre, match="n'a pas l'empreinte de la vue du bras 2"):
+        R.verifier_vue_etrangere_4b(alteree, copie["empreintes"][3], 0, 1)
+    # artefact : entrées d'une autre origine (la course de la source étrangère, non son bras 2)
+    course = premieres[1]["registre_source"].vue("entiere")
+    with pytest.raises(R.ArretRegistre, match="pas du bras 2 de la source étrangère"):
+        R.verifier_vue_etrangere_4b(course, R.empreinte_vue(course), 0, 1)
+    with pytest.raises(MC.ArretMecanique, match="incomplète"):
+        MC.copie_scellee_4b(secondes[0])  # une sortie sans bras 2 joué n'a rien à déposer
 
 
 def test_reproductibilite_a_l_octet_d_une_source(tmp_path):
```

#### `8-test_statistique.py.diff`

```diff
--- code-v2/tests/test_heritage_etage_processeur_v1_statistique.py
+++ code-v3/tests/test_heritage_etage_processeur_v1_statistique.py
@@ -163,11 +163,18 @@
     assert AN.s7({0.25: (0.1, 0.3), 0.5: (0.2, 0.79)}, {0.25: True, 0.5: True}) == "le repli coûte"
     assert AN.s7({0.25: (0.1, 0.3), 0.5: (0.7, 0.9)}, {0.25: True, 0.5: True}) == "indécis"
     assert AN.s7({0.25: (0.1, 0.3)}, {0.25: False}) == "sans objet"
+    toutes = {g: (True, True) for g in range(1, 28)}
     table = AN.table_des_criteres({(10, 0.25, 0.25): "tenue"}, {(5, "sourd-egal", 0.25): "tenue"},
-                                  {("heritage", 0.5): q, ("tenue", 0.5): q}, c3, {(0.5, 10): 0.9}, {1: (True, True), 17: None})
+                                  {("heritage", 0.5): q, ("tenue", 0.5): q}, c3, {(0.5, 10): 0.9}, {**toutes, 17: None})
     assert table["C6"].startswith("non établi") and table["C2_n"] == 10 and table["issue"].startswith("non prononcée")
-    table2 = AN.table_des_criteres({(10, 0.25, 0.25): "en échec"}, {}, {}, c3, {(0.5, 10): 0.7}, {1: (True, False)})
+    table_tenue = AN.table_des_criteres({(10, 0.25, 0.25): "tenue"}, {}, {}, c3, {(0.5, 10): 0.9}, toutes)
+    assert table_tenue["C6"] == "tenu"
+    table2 = AN.table_des_criteres({(10, 0.25, 0.25): "en échec"}, {}, {}, c3, {(0.5, 10): 0.7}, {**toutes, 1: (True, False)})
     assert table2["C1"] == "en échec" and table2["C5"] == "en échec" and table2["C6"] == "en échec"
+    # note D4 (code v3) : une table des gardes incomplète arrête, au lieu de passer « C6 tenu »
+    for incomplete in ({1: (True, True), 17: None}, {g: v for g, v in toutes.items() if g != 9}, {**toutes, 5: None}):
+        with pytest.raises(AN.ArretAnalyse, match="table des gardes incomplète"):
+            AN.table_des_criteres({(10, 0.25, 0.25): "tenue"}, {}, {}, c3, {(0.5, 10): 0.9}, incomplete)
 
 
 def test_point_4_et_taux_sur_des_sorties_plantees():
```

#### `9-mutations_v1-vers-v2.py.diff`

```diff
--- code-v3/outils-dev/mutations_v1.py
+++ code-v3/outils-dev/mutations_v2.py
@@ -4,7 +4,12 @@
 sinon le défaut est « non appliqué »), puis les essais nommés, lancés par `python3 -B -m pytest`. Un défaut est « vu » si les
 essais échouent. Avant tout défaut, chaque sélection d'essais est jouée sur le code sain et doit passer (« témoin »). Sortie : un
 fichier JSON. Arguments : bloc-notes, dossier de travail neuf, fichier de sortie, puis, en option, les identifiants à jouer.
-Aucun réseau ; graines « essai » des essais eux-mêmes."""
+Aucun réseau ; graines « essai » des essais eux-mêmes.
+
+Version 2 (code v3) : les 41 défauts de la version 1, repris à l'identique, et neuf de plus — C1 (refus d'une couche
+décisive non consigné, vu par l'essai final joué seul : un ; aucun défaut n'ouvre le verrou, ce qui ferait dériver une graine
+décisive), C2 (la copie servie au bras 4b : cinq), C3 (la strate du passage exigée sans besoin : un), notes D4 (table des
+gardes incomplète acceptée : un) et D7 (compteurs du jeu perdus : un)."""
 
 import json
 import os
@@ -142,6 +147,31 @@
      [t("statistique", "regles_de_lecture")]),
     ("sorties-non-verifiees", "analyse : sorties relues sans vérifier leur sceau", "analyse.py",
      [("        if _sha256(chemin) != attendu:\n", "        if False:\n")], [t("statistique", "reproductibilite")]),
+    # --- version 2 (code v3) ---------------------------------------------------------------------------------------------
+    # (aucun défaut n'ouvre le verrou des couches décisives : il ferait dériver une graine décisive dans la copie mutée)
+    ("refus-non-consigne", "C1 : refus d'une couche décisive non consigné (vu par l'essai final joué seul)", "graines.py",
+     [("            REFUS.append(texte_etiquette)\n", "")], [t("zz_aucune_graine_decisive")]),
+    ("registre-propre-au-bras-4b", "C2 : le registre propre du bras 2 déposé et servi au bras 4b (ce serait le bras 2)",
+     "mecanique.py",
+     [("                                     copie_etrangere_4b=copie_scellee_4b(e)))",
+       "                                     copie_etrangere_4b=copie_scellee_4b(premieres[k])))")], [t("mecanique", "garde_27")]),
+    ("copie-4b-de-la-source-propre-acceptee", "C2 : copie déposée au bras 4b venue de la source propre acceptée", "registre.py",
+     [("    if etrangere == propre:\n", "    if False:\n")], [t("mecanique", "garde_27")]),
+    ("entree-propre-au-4b-acceptee", "C2 : entrée de la source propre servie au bras 4b sans arrêt propre", "registre.py",
+     [('        if p.get("source") == propre:\n', "        if False:\n")], [t("mecanique", "garde_27")]),
+    ("empreinte-4b-non-verifiee", "C2 : empreinte de la copie servie au bras 4b non comparée à celle déposée", "registre.py",
+     [("    if empreinte_vue(vue_servie) != empreinte_deposee:\n", "    if False:\n")], [t("mecanique", "garde_27")]),
+    ("bras-4b-sans-controle", "C2 : la copie servie au bras 4b n'est pas contrôlée avant d'être servie", "mecanique.py",
+     [('                verifier_vue_etrangere_4b(vue, copie_etrangere_4b["empreintes"][gen - 1], ctx.source,\n'
+       '                                          copie_etrangere_4b["source"])\n', "")], [t("mecanique", "garde_27")]),
+    ("passage-exige-sans-besoin", "C3 : p_passage_vraie exigée par Mondes même quand strates_requises ne l'exige pas",
+     "statistique.py", [("            elif passage_requis:\n", "            elif True:\n")], [t("mecanique", "passage_vraie")]),
+    ("table-des-gardes-incomplete", "note D4 : table des gardes incomplète acceptée (« C6 tenu » sur une liste partielle)",
+     "analyse.py",
+     [("    if sorted(gardes) != list(range(1, 28)) or any(v is None for g, v in gardes.items() if g != 17):\n",
+       "    if False:\n")], [t("statistique", "regles_de_lecture")]),
+    ("compteurs-du-jeu-perdus", "note D7 : compteurs des mondes sources du jeu à sources étrangères perdus", "mondes.py",
+     [("        s.compteurs = cumul[k]\n", "")], [t("mecanique", "garde_27")]),
 ]
 # le défaut « strate vide » ne se voit que si la couche statistique ne lève pas non plus à l'emploi : second remplacement
 DEFAUTS[5] = (DEFAUTS[5][0], DEFAUTS[5][1], DEFAUTS[5][2], DEFAUTS[5][3], [t("mecanique", "strate_vide")])
```

## 6. Écarts et réserves

- **Aucun écart au texte tranché.** Les trois écarts de la contre-lecture (B7 bis à la dose 0,5 ; audit de présentation sur les traits de forme ; bruit de l'audit des doses par paires) vont à l'erratum ; le code n'y touche pas.
- Interface changée par C2 : `mecanique.jouer_source` prend `copie_etrangere_4b` (sortie de `copie_scellee_4b`) au lieu de `vues_etrangeres_4b` ; seul appelant : `jouer_jeu_diagnostic`. Sa sortie gagne `empreintes_vues_bras_2` et `source`. C3 : `statistique.Mondes` prend un cinquième argument, `passage_requis` ; seul appelant : `simuler`.
- Réserve C2 : l'empreinte déposée est prise dans le même processus que la vue (à l'instant où le bras 2 de la source étrangère la reçoit) ; elle protège contre une copie altérée ou d'une autre origine entre le dépôt et le service, et le contrôle de provenance protège contre le registre propre, même si la copie déposée était cohérente avec elle-même. Ce n'est pas un sceau sur disque : au bras 4b, la vue n'est pas écrite en fichier (comme en v2) ; le texte (B7 bis) ne le demande pas.
- Les sorties du banc v1 (`mutations-sortie-v1.json`, `mutations-sortie-v2.json`) sont celles du code v2, gardées telles quelles ; celles du code v3 sont `mutations-v2-sortie-partie-a-v1.json` et `mutations-v2-sortie-partie-b-v1.json`.
- Dans le dossier rendu, les compagnons `.sha256` des huit fichiers changés venaient du code v2 ; je les ai retirés avant de sceller à neuf (les compagnons des fichiers inchangés sont ceux du code v2, identiques).

## 7. Gestes à dire

- Une commande simple par appel ; aucun heredoc, aucun code en ligne passé à un interpréteur : chaque calcul passe par un fichier de script du bloc-notes (`travail/`). Calculs longs (essais, banc, empreintes) en tâche de fond ; aucun n'a eu à être arrêté.
- Graines : seulement la couche « essai » (essais, banc, outil des empreintes) ; aucune graine des couches « etalonnage », « mecanique », « mecanique-reglages », « audit », « decisif » ou « confirmation » dérivée ; les seules demandes de couches décisives sont celles des essais des refus, toutes refusées. Aucun taux de rejet, aucune puissance, aucune valeur p calculés.
- Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau ; aucun `git fetch` ni `git show` n'a été nécessaire ; aucune écriture dans le dépôt, aucun commit ; le dépôt a été lu seulement (code v2, pièces du palier 0a, copie du code de l'organisme, recopiée dans le bloc-notes) ; rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/` ; aucune valeur de clé.
- Aucun refus d'outil.

## 8. Fichiers et empreintes

Dossier rendu : `<bloc-notes>/dev-palier-0b-v3/code-v3/` (arborescence du code v2 : `src/`, `tests/`, `outils-dev/`, et ce rapport). Chaque fichier a son compagnon `.sha256`, au format de `sha256sum` lancé dans son dossier (écrit par `travail/sceller_tout.py`, même règle que `outils-dev/sceller_v1.py` ; compagnons des fichiers inchangés laissés tels quels, identiques). Ce rapport a son propre compagnon.

Fichiers changés ou neufs (les autres sont ceux du code v2, à l'octet) :

```
5e817dfaa7734ef3f607c978f7dcf981c9446de757909600a2001fbbf4101bfb  src/controle_ia/heritage_etage_processeur_v1/registre.py
fd0037fd3505f3e3167eae6687172778986535679fdd96b2624bd8c4b33e3abb  src/controle_ia/heritage_etage_processeur_v1/mecanique.py
c0619eb367b94a54ced73a26098c32c1a153b9b298c596e607dd5393b81a1643  src/controle_ia/heritage_etage_processeur_v1/statistique.py
73c92e370b46e5bc465679a7edc2beed1d6b1f6fc32bcab1116b027c954b13c9  src/controle_ia/heritage_etage_processeur_v1/analyse.py
08793942568a00b31568827067b53e60f2b91fc3aea061dc2357c99faf9955a5  src/controle_ia/heritage_etage_processeur_v1/mondes.py
d342fa2a4f775085e29dcce8f97cd38b5de1293f7fe9c111a4ca0428df3f3bb4  tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py
15d1a91792d6c49dd76a0b08c3a5145c7c2353bfdb4f6ba20d17cec17e925f70  tests/test_heritage_etage_processeur_v1_mecanique.py
26e3195b7f5e8e58d75bcf4a8766d79164cf2d8800cc807fa2f63ade128c2215  tests/test_heritage_etage_processeur_v1_statistique.py
9fd6fc696c49481d8cbbfeae8b795c388a2accaa2a713d55f5f1f0f4b0a20627  outils-dev/mutations_v2.py
4fae9ca06c1e37a8137aca5c2a610e4158090e61f9be53db7106ef24228bd10e  outils-dev/mutations-v2-sortie-partie-a-v1.json
4c57398668ec03e58b527560216652f67403c0fae16408e9ac8c012060923c80  outils-dev/mutations-v2-sortie-partie-b-v1.json
```

Table entière (51 fichiers) :

```
0513640b0cbaedcc0e832da8d96f022a3b231ea7cc6eab40062a96714c8629e2  outils-dev/chrono_statistique.py
af772fb9918a3e69ea1bde8a34c0ac68bc8622321e0e600d0d8c8766da02f3d2  outils-dev/chrono_suite.py
fefceead89b91a30eb738e12480ff96c0356c5b2b26f4d4b9d05b5825db737cf  outils-dev/diagnostic_conflits_etrangers.py
5bf7bd44a892ef4fb66981592247131d13fa7ca5e903e4d2cb483a6e9db4d965  outils-dev/diagnostic_etrangere.py
10af2b5ab0e2d88ab9f4a9b395a555044e4ec140108b7c8d20351bf9eb1f5c3e  outils-dev/diagnostic_forme_dependantes.py
8493e5f79964ba75ea8a89b18df3cb8629a25e7570955f0b26aba0a77a0b47ea  outils-dev/diagnostic_import.py
8b2ba07ba7a009b5fab7333e206d9734a6e4de0b943f312c52b2e1cdd1c36ea9  outils-dev/diagnostic_presentation.py
12a2da99ced510c42f03645f4068f14dffa3f86787431cbd7cb67ac3ec85c9cf  outils-dev/empreintes-attendues-palier-0a.txt
b182d5ed92e5e92b7a4a14b26bb47ca4fd80bd0ce9fc916a716d51a61cfaea9e  outils-dev/essai_equivalence.py
580190bfd609195a8e5999401c264b9d8c5842a6bb0571cd28b1cc7df875a8dc  outils-dev/essai_mecanique.py
7254490fe4be80b52fa7cc46e369dbb6fd8d38300265b9a98a82069a0fad56ce  outils-dev/mutations-sortie-v1.json
0f19dd4c146ef3a6df5c6cc95dea9dd343ce53824b9310212657f9b9445a9dc5  outils-dev/mutations-sortie-v2.json
4fae9ca06c1e37a8137aca5c2a610e4158090e61f9be53db7106ef24228bd10e  outils-dev/mutations-v2-sortie-partie-a-v1.json
4c57398668ec03e58b527560216652f67403c0fae16408e9ac8c012060923c80  outils-dev/mutations-v2-sortie-partie-b-v1.json
c5476e7b359b2c15b77795832d8f1849dc23bdc6d0aef7386b179170a4123fee  outils-dev/mutations_v1.py
9fd6fc696c49481d8cbbfeae8b795c388a2accaa2a713d55f5f1f0f4b0a20627  outils-dev/mutations_v2.py
c8a9ed8d7339129d311c787ad5f49c0ef7347c70cfae4b34fabf82f8e6fe6e55  outils-dev/sceller_v1.py
ff647eaf2ead2bd14a1a00a000f09dc142b805fbbeb6aaf87b74f225faaa72d6  outils-dev/verification-empreintes-organisme-v1.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  src/controle_ia/__init__.py
ba3d58e25b499a89d00bf9e2eab524d838297c9214277ba09823b656fe941935  src/controle_ia/heritage_etage_processeur_v1/__init__.py
73c92e370b46e5bc465679a7edc2beed1d6b1f6fc32bcab1116b027c954b13c9  src/controle_ia/heritage_etage_processeur_v1/analyse.py
11352fcd12b531c375abf40f68fdefcf45bc4feba822b3d88169bb852687bddd  src/controle_ia/heritage_etage_processeur_v1/audit.py
8758b015d523370d6d1a98ff3fdebbe0fdc823805abaf9aa1fd024f48d9d64a7  src/controle_ia/heritage_etage_processeur_v1/comparateur.py
37e848c2706a9c9d30673a1e8153f46ffa573b2d141229cffae73646ec2966c3  src/controle_ia/heritage_etage_processeur_v1/constantes.py
684aeed62fd8ecc902c42e503e8211385e275e5feee36dec6d6e922afc2014bb  src/controle_ia/heritage_etage_processeur_v1/cout.py
2173613ae03067c4ff3090f74644f86550ca1d127702ff41443d1dc6a574a799  src/controle_ia/heritage_etage_processeur_v1/enveloppe.py
fda98bba41c57cbd4860a62d93c7e12f3d23d098f148af0e79b48ec20417eee3  src/controle_ia/heritage_etage_processeur_v1/equivalence.py
f3c5113bf43c0ff9b507c53ac4327e4dccf8410176e57b747ce498ea1e46fdc8  src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
a47c8fa2acfd16caaeee3d420fdffe00adce9d7ab876c976f94b96108ad5b725  src/controle_ia/heritage_etage_processeur_v1/etapes.py
063df6e1e2c08d79531fce8b76f3e3dbc3fdb002af7657efb1773e33afb9beda  src/controle_ia/heritage_etage_processeur_v1/executeur.py
dce5db04472d049f350f08d56f65a8254fb58eb13f3f2b6a0c3ca2e95952fcd5  src/controle_ia/heritage_etage_processeur_v1/frequences.py
cf433337972c02baefe2f57323f036d98649b5b25fb8da1afd59bd12ab2e8c13  src/controle_ia/heritage_etage_processeur_v1/graines.py
4492c8545f6fc081eb267d851bd24a011fe4817cadad8b9606048bb26208dc1f  src/controle_ia/heritage_etage_processeur_v1/intervalles.py
fb24a9eaffdc98ee080db835d77ee2c419242ad4108ef60b440df8f1cb387536  src/controle_ia/heritage_etage_processeur_v1/lois.py
fd0037fd3505f3e3167eae6687172778986535679fdd96b2624bd8c4b33e3abb  src/controle_ia/heritage_etage_processeur_v1/mecanique.py
08793942568a00b31568827067b53e60f2b91fc3aea061dc2357c99faf9955a5  src/controle_ia/heritage_etage_processeur_v1/mondes.py
fb2f7b48234661c2c825e2dc0c1cb7b9a6f576ff6bdebb3a2196aa3efe9293f1  src/controle_ia/heritage_etage_processeur_v1/organisme.py
e0aa6b89501c4cfeaed67d748db02dba1cb015405c34a91955d70dc2e408ab83  src/controle_ia/heritage_etage_processeur_v1/proposeurs.py
9a386fc7d56cc3f10369ef066e1f9daae7f3e41e592dd9ab4cd2b7b6768c6417  src/controle_ia/heritage_etage_processeur_v1/rangs_signes.py
5e817dfaa7734ef3f607c978f7dcf981c9446de757909600a2001fbbf4101bfb  src/controle_ia/heritage_etage_processeur_v1/registre.py
c0619eb367b94a54ced73a26098c32c1a153b9b298c596e607dd5393b81a1643  src/controle_ia/heritage_etage_processeur_v1/statistique.py
fe150097f08f32f4eb8cf212f0da0b30acb8fbff9b0965d9807e42236d198e59  src/controle_ia/heritage_etage_processeur_v1/tirages.py
372229230356317c51990c0a45ed7e811e37ba2579e7b8c99f8d418bf7dbd236  tests/aides_heritage_etage_processeur_v1.py
444f30432e9551c50ef7fc34d6ca232c08478f5d207f13a47c79bbabdbf74f0e  tests/test_heritage_etage_processeur_v1_etapes.py
acd1954670935fc87778411602519916af0b7be8e08decce2aa86f7636996d12  tests/test_heritage_etage_processeur_v1_gardes.py
15d1a91792d6c49dd76a0b08c3a5145c7c2353bfdb4f6ba20d17cec17e925f70  tests/test_heritage_etage_processeur_v1_mecanique.py
493488e605a22a4b27ac2dda6e16d4b77264e9e86ea98cb2af6a06e9457d2eaf  tests/test_heritage_etage_processeur_v1_mondes.py
2697382c1ce050b590d956078796e5c9c5225ea1ad37d08c2ded011a47799461  tests/test_heritage_etage_processeur_v1_organisme.py
3162d852ce59c5eb263236bf9c154911a47ea8eb13d262794614953937ec0a4f  tests/test_heritage_etage_processeur_v1_outils.py
26e3195b7f5e8e58d75bcf4a8766d79164cf2d8800cc807fa2f63ade128c2215  tests/test_heritage_etage_processeur_v1_statistique.py
d342fa2a4f775085e29dcce8f97cd38b5de1293f7fe9c111a4ca0428df3f3bb4  tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py
```

Les empreintes des huit fichiers changés sont celles relevées avant le lancement des essais et du banc : le code n'a pas changé entre la suite au vert, le banc et le scellement.

Non rendus, laissés dans le bloc-notes : `code-organisme-94bfd92/` (copie), `travail/` (outils de ce travail : `verifier_table.py`, `lancer_essais.py`, `verifier_remplacements.py`, `empreintes_resultats.py`, `comparer_empreintes.py`, `lire_banc.py`, `assembler_rapport.py`, `sceller_tout.py` (même règle que `outils-dev/sceller_v1.py`, sur la liste de la table du rapport v2 et les fichiers neufs) ; journaux des essais ; empreintes des sorties v2 et v3 ; différentiels ; dossiers de travail du banc).

*Développeur, modèle L′.*
