# Rapport du développeur — code d'appel de l'étage 2 à 200 témoins (ligne 3, organisme v9) — v2

Pièce d'instrument (classe B), écrite le 2026-11-20 par le même développeur, modèle O, sur le même mandat
(`mandat-developpeur-code-appel-etage-2-v1.md`, `d20e40d5…`, en-tête compris) et sur le message de la coordination qui
demande les corrections de la contre-lecture. La version 1 (`code-appel-v1/`, programme `586bc7e6…`, essais `d68e2c14…`,
rapport `c5df780d…`) est gardée sans modification ; son rapport vaut pour tout ce que celui-ci ne change pas. Rien n'a tourné
contre un vrai juge : aucun appel, aucune clé lue, aucun relais lancé, mode réel jamais lancé, aucune écriture dans le dépôt.

Pièce lue : contre-lecture `…/etage-2-portee-200-v1/code-appel-v1/contre-lecture-v1/contre-lecture-code-appel-etage-2-v1.md`
(`4bcab58a79459e66711bfb1105f833c8453448d2d93ef1fa06efe658b5628f98`, recalculée), verdict « À corriger », trois corrections.
Décisions de la mère (14:01Z), rapportées par la coordination, portées ici.

## 1. Les trois corrections, portées à la lettre

| | constat de la contre-lecture | ce que fait la v2 | lieu | essai neuf |
|---|---|---|---|---|
| C1 | une relance sur une autre banque est acceptée | la ligne d'ouverture du journal porte aussi `"plomberie"` ; à la relance, banque (empreinte) ou témoins de plomberie différents de l'ouverture : refus ; un rendu engagé au journal hors du plan : refus. Texte de la contre-lecture repris tel quel | `executer`, bloc `if relance:` (avant le manifeste) ; ligne d'ouverture | `test_c1_ouverture_porte_banque_et_plomberie` (sain : même banque, relance jusqu'au bout) ; `test_c1_relance_sur_une_autre_banque_refusee` (artefacts : autre banque, autre plomberie ; journal inchangé) ; `test_c1_rendu_du_journal_hors_du_plan_refuse` (artefact) |
| C2 | une panne entre la création du dossier d'appel et l'engagement bloque toute relance (`FileExistsError`) | `mkdir(parents=True, exist_ok=True)` | `jouer` | `test_c2_panne_entre_le_dossier_d_appel_et_l_engagement` (artefact : dossier laissé sous le premier identifiant tiré à la relance ; la relance part, rejeu en essai 2 sous cet identifiant, 1 005 envois) |
| C3 | le contrôle de la plomberie n'est pas rejoué à la relance | sur un rendu de plomberie déjà fini, `motif_plomberie` est rejoué sans envoi ; motif : arrêt, retour à la mère. Texte de la contre-lecture repris tel quel | `jouer`, début de la boucle sur le plan | `test_c3_controle_de_plomberie_rejoue_a_la_relance` (panne forcée entre le règlement du second rendu de plomberie et son contrôle ; artefact : plomberie illisible, arrêt à la relance, 2 envois, aucun du bloc A ; sain : plomberie lisible, 1 004 envois) |

Aucune autre ligne du compteur, du plafond, du plan ou des gardes ne change ; la reproduction du calcul v2 est rejouée en
entier et tient.

## 2. Décisions de la mère (14:01Z)

1. **Racine des identifiants opaques** : 2026111935, clé 4, confirmée. Rien à changer au code.
2. **Clé du juge Opus** : passée en argument par son **nom** seul (`--nom-cle-claude`) ; la mère nomme la variable de
   GO-2026-11-20-55. La v2 contrôle seulement la **forme** d'un nom de variable (`NOM_DE_VARIABLE`) ; aucune valeur n'est
   lue, aucune présence n'est vérifiée, ni en essai ni par moi. Le nom ne figure pas dans le code : il est à la commande de
   départ, donc à l'additif. Essai : un nom hors forme est refusé avant tout service (`test_mode_reel_refuse_avant_tout_service`).
3. **Environnement épuré** : le mode réel se lance sous `env -i` ; liste blanche en constante,
   `VARIABLES_PERMISES = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TZ", "TMPDIR", "HOME", "GO_ID")` — les noms permis du
   lanceur v9, plus `HOME` (sonde du bac à sable du précédent), `LC_CTYPE` (l'interpréteur la pose lui-même quand il force un
   locale UTF-8 sous un environnement vide) et `GO_ID` (garde de calcul du dépôt). `exiger_environnement_epure`, appelée dans
   `preparer_reel` juste après le refus des noms de clé : toute variable hors de la liste, présente au départ, est un refus
   (les noms seuls sont lus). Essais : `test_environnement_epure_sain_et_artefact` (sain : liste blanche, environnement vide ;
   artefacts : une variable hors liste, un mandataire réseau) ; `test_mode_reel_environnement_liste_blanche_accepte` (sain, par
   `preparer_reel`) ; artefact par `preparer_reel` dans `test_mode_reel_refuse_avant_tout_service`. **À relire par la mère** :
   la liste exclut tout mandataire réseau (`HTTPS_PROXY`…) ; les relais tiennent le réseau, le programme n'en a pas besoin
   d'après ma lecture du précédent ; si l'additif en veut un, il élargit la liste.
4. **« Tout refusé »** : le code garde l'arrêt de la plomberie ; rien n'est changé.
5. **Les six silences ajoutés par le contre-lecteur, acceptés par la mère avec mention** :
   - (15) `budget_depasse` classé retour obtenu (compté à son coût, non rejoué, verdict absent, arrêt au-dessus de 0,60) ;
     `tours_epuises` classé erreur (0,60, rejeu) — accepté ;
   - (16) « complets » du rapport d'exécution = rendus partis et revenus, verdict illisible compris ; le programme de lecture
     compte les verdicts lisibles — accepté ;
   - (17) après un arrêt pour crédit, toute relance est refusée sous la même ligne — accepté ;
   - (18) panne pendant le dépôt (après « fin » ou « arrêt ») : relance refusée, dépôt non refait ; journal et réponses brutes
     restent ; un dépôt refait depuis le journal serait une pièce à part — accepté ;
   - (19) registre lu sur `origin/main` local sans `git fetch` : la procédure de départ fait le `git fetch` avant ; le manifeste
     garde le commit et l'empreinte du registre lus — accepté ;
   - (20) environnement épuré — accepté, et porté au code (point 3).
6. **Interpréteur** : non figé ; il sera nommé à l'additif de code.

## 3. Sortie des essais

Commande exacte (sur ma copie) :

`env -C /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v2 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_epreuve_juges_reels_ligne_3_v2.py`

Résultat : **93 passed in 131.28s** au passage final, sur le programme 1a0b08d5… et les essais b1767abb… (un premier passage, avant une retouche du seul texte de l'en-tête et de l'usage du programme, rendait aussi 93 passed in 94.28s) ; aucun échec, aucun saut ; joués en tâche de fond. 93 = les 85 essais de la v1, plus 3 pour C1, 1 pour C2, 2 pour C3 (sain et artefact), 2 pour l'environnement épuré.

Les 85 essais de la v1 sont rejoués sur le module v2, inchangés sauf l'import et deux cas ajoutés à l'essai du mode réel ;
s'y ajoutent les essais du § 1 et du § 2.

## 4. Ce que l'additif de code doit porter (complète le § 9 du rapport v1)

- Fichiers et empreintes de cette version (table `table-empreintes-code-appel-v2.txt`), le commit qui les verse.
- Commande des essais (§ 3) et son résultat.
- Commande réelle, sous `env -i` : `env -i PATH=… HOME=… GO_ID=GO-… <interpréteur> -I -B epreuve_juges_reels_ligne_3_v2.py
  --reel --go-id GO-… --banque … --banque-sha … --declaration … --declaration-sha … --sortie … --plomberie tXX,tYY
  --nom-cle-claude <nom de la variable de GO-2026-11-20-55>` ; `git fetch` de `origin` juste avant.
- Racine 2026111935, clés 1 à 4 (dont 4 : identifiants opaques, confirmée par la mère).
- La constante `VARIABLES_PERMISES`.

## 5. Écarts

1. Hors des textes de la contre-lecture et des décisions de la mère, la v2 ne change que : le nom de version, l'en-tête du
   programme et des essais, le texte d'usage (il nomme `env -i`).
2. Les différentiels sont écrits dans mon dossier, hors de `code-appel-v2/` (`../diff-programme-v1-v2.txt`,
   `../diff-essais-v1-v2.txt`), et recopiés ci-dessous.
3. L'essai C3 force la panne en remplaçant, le temps de la première exécution, `motif_plomberie` du module par une fonction qui
   lève au second contrôle (`monkeypatch` de pytest) ; la relance joue la fonction d'origine.
4. Aucun refus de permission, de classifieur ou de garde.

## 6. Différentiels v1 → v2 (`diff -u`)

### 6.1 Programme

```diff
--- /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v1/epreuve_juges_reels_ligne_3_v1.py	2026-11-20 13:44:41.064374431 +0000
+++ /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v2/epreuve_juges_reels_ligne_3_v2.py	2026-11-20 14:04:12.785208020 +0000
@@ -1,5 +1,14 @@
 #!/usr/bin/env python3
-"""Épreuve des juges réels — ligne 3 de l'organisme v9 (votes effectifs des juges croisés), étage 2 à 200 témoins — v1.
+"""Épreuve des juges réels — ligne 3 de l'organisme v9 (votes effectifs des juges croisés), étage 2 à 200 témoins — v2.
+
+Version 2 (même développeur, règle R12 ; la v1, `epreuve_juges_reels_ligne_3_v1.py`, 586bc7e6…, est gardée sans
+modification) : les trois corrections de la contre-lecture `contre-lecture-code-appel-etage-2-v1.md` (4bcab58a…), à la
+lettre de ses textes. C1 : une relance relit l'ouverture du journal ; banque, témoins de plomberie ou rendu
+du journal hors du plan : refus. C2 : le dossier d'appel se crée sans refus s'il existe déjà (panne entre sa création et
+l'engagement). C3 : le contrôle de la plomberie est rejoué, sans envoi, sur un rendu de plomberie déjà fini. Et deux
+décisions de la mère (14:01Z) : (2) la clé du juge Opus passe en argument par son nom seul, de forme contrôlée ; (3) le
+mode réel part sous `env -i`, liste blanche `VARIABLES_PERMISES`, refus si une variable hors liste est présente au départ.
+Rien d'autre ne change.
 
 Plan de code : annexe A du texte v7 (`preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, 4e3680d9…), ligne 561 ;
 section « Étage 2 » (l. 243 à 305), « Liste d'arrêt » (l. 352 et suivantes), « Plafond : arrêt dur par compteur » (l. 380
@@ -63,7 +72,7 @@
 from fractions import Fraction
 from pathlib import Path
 
-VERSION = "epreuve_juges_reels_ligne_3_v1"
+VERSION = "epreuve_juges_reels_ligne_3_v2"
 
 # --- plafond (une seule constante, égale à la ligne de GO lue) -------------------------------------------------------------
 PLAFOND_C = 8836            # 88,36 USD en centimes entiers : GO-2026-11-20-26 ; additif 3 v3, § 4.2
@@ -128,6 +137,13 @@
 GO_FORME = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
 MOTS_PERIMETRE_GO = ("ligne 3", "etage 2")
 
+# --- mode réel : environnement épuré (v2, décision de la mère (3)) ---------------------------------------------------------------
+# Liste blanche des variables permises au départ du mode réel, lancé sous `env -i` : celles du lanceur v9 (`NOMS_PERMIS`),
+# plus HOME (sonde du bac à sable du précédent), LC_CTYPE (posée par l'interpréteur lui-même quand il force un locale UTF-8
+# sous un environnement vide) et GO_ID (garde de calcul du dépôt).
+VARIABLES_PERMISES = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TZ", "TMPDIR", "HOME", "GO_ID")
+NOM_DE_VARIABLE = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
+
 # --- statuts des adaptateurs de l'orchestrateur -----------------------------------------------------------------------------
 STATUTS_TECHNIQUES = ("erreur", "tours_epuises")    # refusé par le relais ou le fournisseur, coupé, en erreur
 EVENEMENTS_CHANGEMENT_DE_MODELE = ("assistant.model", "result.model_usage", "resultat.modele_servi",
@@ -898,6 +914,13 @@
                             "suite sous cette ligne")
             if etat_avant["fin"] is not None:
                 raise Refus("relance refusée : le plan est déjà servi en entier")
+            ouverture = journal.lignes[0]                                        # v2, C1
+            if ouverture.get("banque_sha256") != banque_sha or ouverture.get("plomberie") != list(plomberie_ids):
+                raise Refus("relance refusée : banque ou témoins de plomberie différents de ceux de l'ouverture du journal : "
+                            "aucune suite sous cette ligne")
+            ids_du_plan = {p["id"] for p in plan}
+            if any(l["rendu"] not in ids_du_plan for l in journal.lignes if l["type"] == "engagement"):
+                raise Refus("relance refusée : un rendu du journal n'est pas au plan : aucune suite sous cette ligne")
         lecture = {"engagements": len(compteur.engagements), "reglements": len(compteur.reglements),
                    "orphelins": compteur.orphelins(), "cumul_compte_lu": str(compteur.cumul())}
         manifeste = manifeste_d_execution(k_exec, relance, lecture, contexte, service, banque_sha, temoins_v2_sha,
@@ -909,7 +932,7 @@
                              "cumul_compte": str(compteur.cumul())})
         else:
             journal.ajouter({"type": "ouverture", "execution": k_exec, "version": VERSION, "plafond_c": PLAFOND_C,
-                             "session_c": SESSION_C, "banque_sha256": banque_sha})
+                             "session_c": SESSION_C, "banque_sha256": banque_sha, "plomberie": list(plomberie_ids)})
         arret = jouer(plan, par_id, service, compteur, journal, depot, arret_de_plomberie)
     finally:
         journal.fermer()
@@ -925,6 +948,11 @@
     for prevu in plan:
         s = rendus.get(prevu["id"])
         if rendu_fini(s) or prevu["juge"] in roles:
+            if prevu["bloc"] == "P" and arret_de_plomberie and rendu_fini(s) and prevu["juge"] not in roles:
+                motif = motif_plomberie(s, compteur, prevu["juge"])     # v2, C3 : contrôle sans envoi, rejoué à la relance
+                if motif:
+                    return journal.ajouter({"type": "arret", "motif": "plomberie : " + motif, "dernier_envoi_parti": dernier,
+                                            "cumul_compte": str(compteur.cumul()), "retour": "à la mère"})
             continue
         juge = service.juge(prevu["juge"])
         ad = service.adaptateurs[juge["fournisseur"]]
@@ -957,7 +985,7 @@
                                         "dernier_envoi_parti": dernier, "cumul_compte": str(compteur.cumul())})
             opaques.servis.add(opaque)
             dossier = service.dossier_appels / prevu["juge"] / opaque
-            dossier.mkdir(parents=True, exist_ok=False)
+            dossier.mkdir(parents=True, exist_ok=True)      # v2, C2 : panne possible entre cette création et l'engagement
             n = compteur.engager({"rendu": prevu["id"], "bloc": prevu["bloc"], "rang": prevu["rang"],
                                   "temoin": prevu["temoin"], "juge": prevu["juge"], "essai": essai, "opaque": opaque,
                                   "entree_sha256": sha256_octets(texte.encode("utf-8"))})
@@ -1250,6 +1278,16 @@
     return {"texte": p.stdout.decode("utf-8"), "commit": c.stdout.strip(), "sha256": sha256_octets(p.stdout)}
 
 
+def exiger_environnement_epure(environ) -> list:
+    """v2, décision de la mère (3) : le mode réel se lance sous `env -i` avec une liste blanche de variables
+    (`VARIABLES_PERMISES`) ; toute variable hors de la liste, présente au départ, est un refus (les noms seuls sont lus,
+    jamais une valeur)."""
+    hors = sorted(n for n in environ if n not in VARIABLES_PERMISES)
+    if hors:
+        raise Refus(f"environnement non épuré : variables hors de la liste blanche ({hors}) : lancer sous env -i")
+    return sorted(environ)
+
+
 def preparer_reel(argv, environ, aujourd_hui, lire_registre=lire_registre_main, construire_service=None) -> dict:
     """Refus avant tout, dans cet ordre : noms de clé dans l'environnement (par le nom seulement) ; chemins du coffre ;
     `--go-id` (et `GO_ID` s'il est posé, égal) valide au registre lu sur origin/main ; banque scellée à l'empreinte passée ;
@@ -1257,6 +1295,7 @@
     noms = sorted(n for n in environ if re.search(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", n, re.I))
     if noms:
         raise Refus(f"noms de variables de clé dans l'environnement ({noms}) : la clé reste dans son relais")
+    exiger_environnement_epure(environ)                                          # v2, décision de la mère (3)
     go_id = _argument(argv, "--go-id")
     if environ.get("GO_ID") not in (None, go_id):
         raise Refus("GO_ID de l'environnement différent de --go-id")
@@ -1265,6 +1304,8 @@
     sortie = Path(_argument(argv, "--sortie"))
     plomberie = (_argument(argv, "--plomberie") or "").split(",")
     nom_cle_claude = _argument(argv, "--nom-cle-claude")
+    if not NOM_DE_VARIABLE.match(nom_cle_claude):                               # v2, décision de la mère (2) : le nom seul
+        raise Refus("--nom-cle-claude : un nom de variable est exigé (le nom seul, jamais la valeur)")
     garde_chemins([banque, decl, sortie])
     registre = lire_registre()
     go = verifier_ligne_de_go(registre["texte"], go_id, aujourd_hui)
@@ -1367,8 +1408,8 @@
 def principal(argv=None) -> int:
     argv = sys.argv[1:] if argv is None else list(argv)
     if not argv or argv[0] != "--reel":
-        print("usage : --reel --go-id GO-… --banque B --banque-sha S --declaration D --declaration-sha S2 "
-              "--sortie DOSSIER_NEUF_OU_DE_RELANCE --plomberie tXX,tYY --nom-cle-claude NOM", file=sys.stderr)
+        print("usage (sous env -i, liste blanche VARIABLES_PERMISES) : --reel --go-id GO-… --banque B --banque-sha S "
+              "--declaration D --declaration-sha S2 --sortie DOSSIER_NEUF_OU_DE_RELANCE --plomberie tXX,tYY --nom-cle-claude NOM", file=sys.stderr)
         return 2
     try:
         prep = preparer_reel(argv, dict(os.environ), _dt.datetime.now(_dt.timezone.utc).date(),
```

### 6.2 Essais

```diff
--- /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v1/essais_epreuve_juges_reels_ligne_3_v1.py	2026-11-20 13:44:50.408374987 +0000
+++ /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v2/essais_epreuve_juges_reels_ligne_3_v2.py	2026-11-20 14:03:41.744442237 +0000
@@ -1,4 +1,7 @@
-"""Essais de `epreuve_juges_reels_ligne_3_v1.py` (pytest, service factice seul : aucun réseau, aucune clé, aucun relais).
+"""Essais de `epreuve_juges_reels_ligne_3_v2.py` (pytest, service factice seul : aucun réseau, aucune clé, aucun relais).
+
+Version 2 (R12 ; la v1 est gardée) : les essais de la v1, sur le module v2, plus les essais des corrections C1, C2, C3 de la
+contre-lecture et des décisions de la mère (2) et (3) (nom de la clé, environnement épuré), en fin de fichier.
 
 Chaque garde de la liste d'arrêt qui touche l'appel, sur un cas sain et sur un artefact (règle R5) ; la relance après
 panne ; la reproduction exacte, sur service factice aux coûts du calcul v2 des conditions du plafond
@@ -18,7 +21,7 @@
 
 ICI = Path(__file__).resolve().parent
 sys.path.insert(0, str(ICI))
-import epreuve_juges_reels_ligne_3_v1 as M  # noqa: E402
+import epreuve_juges_reels_ligne_3_v2 as M  # noqa: E402
 
 L3 = M.DEPOT / "docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1"
 CALCUL = (L3 / "calcul_conditions_plafond_200_ligne_3_v2.py",
@@ -718,6 +721,8 @@
         (_argv(tmp_path, banque, h, decl, "0" * 64), {}, "déclaration des relais"),
         (_argv(tmp_path, banque, h, tmp_path / "absente.json", hd), {}, "déclaration des relais"),
         (_argv(tmp_path, banque, h, decl, hd), {"EXEMPLE_API_KEY": "x"}, "noms de variables de clé"),
+        (_argv(tmp_path, banque, h, decl, hd), {"VARIABLE_HORS_LISTE": "x"}, "non épuré"),          # v2, mère (3)
+        (_argv(tmp_path, banque, h, decl, hd)[:-1] + ["nom-minuscule"], {}, "nom de variable"),     # v2, mère (2)
     ]
     for argv, env, motif in cas:
         with pytest.raises(M.Refus, match=motif):
@@ -748,3 +753,137 @@
     assert not any(k in x for x in lecture["rendus"] for k in ("classe", "item", "niveau"))   # aucune vérité au dépôt
     assert len(list((depot / "reponses-brutes").iterdir())) == 1004
     shutil.rmtree(racine)
+
+
+# --- v2 : corrections de la contre-lecture (C1, C2, C3) et décisions de la mère (2), (3) --------------------------------------
+
+
+def _panne_puis(tmp_path, fonctions, consigne, configuration, panne_a, banque=None):
+    items = configuration["items_juge"]
+    banque = banque or ecrire_banque(tmp_path, items)
+    racine = tmp_path / "run"
+    racine.mkdir()
+    banc = Banc(items, couts_au_facteur(1), panne_a=panne_a)
+    with pytest.raises(KeyboardInterrupt):
+        M.executer(racine, banque[0], banque[1], PLOMBERIE, faire_service(racine, banc, fonctions, consigne, configuration),
+                   {"commit_depot": "essai"})
+    return racine, banque
+
+
+def _relancer(racine, banque, fonctions, consigne, configuration, plomberie=PLOMBERIE, banc=None):
+    banc = banc or Banc(configuration["items_juge"], couts_au_facteur(1))
+    return M.executer(racine, banque[0], banque[1], plomberie,
+                      faire_service(racine, banc, fonctions, consigne, configuration), {"commit_depot": "essai"})
+
+
+def test_c1_ouverture_porte_banque_et_plomberie(tmp_path, fonctions, consigne, configuration):
+    racine, banque = _panne_puis(tmp_path, fonctions, consigne, configuration, 10)
+    ouverture = lignes_du_journal(racine)[0]
+    assert ouverture["banque_sha256"] == banque[1] and ouverture["plomberie"] == list(PLOMBERIE)
+    rapport = _relancer(racine, banque, fonctions, consigne, configuration)     # cas sain : même banque, même plomberie
+    assert rapport["arret"] is None and rapport["envois_partis"] == 1005
+    shutil.rmtree(racine)
+
+
+def test_c1_relance_sur_une_autre_banque_refusee(tmp_path, fonctions, consigne, configuration):
+    items = configuration["items_juge"]
+    racine, banque = _panne_puis(tmp_path, fonctions, consigne, configuration, 100)
+    autre = ecrire_banque(tmp_path, items, nom="autre-banque.json",
+                          contenu_de=lambda k, c: dict(c, titre=c["titre"] + " (autre banque)"))
+    assert autre[1] != banque[1]
+    avant = lignes_du_journal(racine)
+    with pytest.raises(M.Refus, match="banque ou témoins de plomberie différents"):
+        _relancer(racine, autre, fonctions, consigne, configuration)
+    with pytest.raises(M.Refus, match="banque ou témoins de plomberie différents"):
+        _relancer(racine, banque, fonctions, consigne, configuration, plomberie=("t01", "t03"))
+    assert lignes_du_journal(racine) == avant                                    # rien écrit, rien envoyé
+
+
+def test_c1_rendu_du_journal_hors_du_plan_refuse(tmp_path, fonctions, consigne, configuration):
+    racine, banque = _panne_puis(tmp_path, fonctions, consigne, configuration, 6)
+    journal = racine / "sortie" / "epreuve" / "journal-compteur.jsonl"
+    lignes = [json.loads(x) for x in journal.read_text(encoding="utf-8").splitlines()]
+    k = next(i for i, l in enumerate(lignes) if l["type"] == "engagement")
+    lignes[k]["rendu"] = "hors-du-plan|juge-opus|r1"
+    journal.write_bytes(b"".join((json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
+                                 for l in lignes))
+    with pytest.raises(M.Refus, match="n'est pas au plan"):
+        _relancer(racine, banque, fonctions, consigne, configuration)
+
+
+def test_c2_panne_entre_le_dossier_d_appel_et_l_engagement(tmp_path, fonctions, consigne, configuration):
+    racine, banque = _panne_puis(tmp_path, fonctions, consigne, configuration, 100)
+    avant = lignes_du_journal(racine)
+    orphelin = avant[-1]
+    assert orphelin["type"] == "engagement"
+    servis = {l["opaque"] for l in avant if l["type"] == "engagement"}
+    prochain = M.Opaques(servis).neuf()                                          # premier identifiant tiré à la relance
+    laisse = racine / "sortie" / "appels" / orphelin["juge"] / prochain
+    laisse.mkdir(parents=True)                                                   # artefact : dossier créé, aucun engagement
+    rapport = _relancer(racine, banque, fonctions, consigne, configuration)
+    apres = lignes_du_journal(racine)
+    rejeu = next(l for l in apres if l["type"] == "engagement" and l["n"] == orphelin["n"] + 1)
+    assert rejeu["opaque"] == prochain and rejeu["rendu"] == orphelin["rendu"] and rejeu["essai"] == 2
+    assert rapport["arret"] is None and rapport["envois_partis"] == 1005
+    shutil.rmtree(racine)
+
+
+@pytest.mark.parametrize("illisible", [False, True])
+def test_c3_controle_de_plomberie_rejoue_a_la_relance(tmp_path, fonctions, consigne, configuration, monkeypatch, illisible):
+    """Panne forcée entre le règlement du second rendu de plomberie et son contrôle ; à la relance, le contrôle est rejoué
+    sans envoi : plomberie illisible, arrêt, aucun envoi du bloc A (artefact) ; plomberie lisible, le plan continue (sain)."""
+    items = configuration["items_juge"]
+    banque = ecrire_banque(tmp_path, items)
+    racine = tmp_path / "run"
+    racine.mkdir()
+    original = M.motif_plomberie
+    appels = {"n": 0}
+
+    def controle_puis_panne(s, compteur, juge):
+        appels["n"] += 1
+        if appels["n"] == 2:
+            raise KeyboardInterrupt("panne simulée entre le règlement et le contrôle de la plomberie")
+        return original(s, compteur, juge)
+
+    monkeypatch.setattr(M, "motif_plomberie", controle_puis_panne)
+    banc = Banc(items, couts_au_facteur(1), illisible_pour=(lambda i, m: illisible and i == 1))
+    with pytest.raises(KeyboardInterrupt):
+        M.executer(racine, banque[0], banque[1], PLOMBERIE, faire_service(racine, banc, fonctions, consigne, configuration),
+                   {"commit_depot": "essai"})
+    avant = lignes_du_journal(racine)
+    assert sum(1 for l in avant if l["type"] == "reglement") == 2 and avant[-1]["type"] == "reglement"
+    monkeypatch.setattr(M, "motif_plomberie", original)
+    rapport = _relancer(racine, banque, fonctions, consigne, configuration)
+    eng = [l for l in lignes_du_journal(racine) if l["type"] == "engagement"]
+    if illisible:
+        assert rapport["arret"]["motif"] == "plomberie : réponse illisible"
+        assert rapport["envois_partis"] == 2 and not any(l["bloc"] == "A" for l in eng)
+    else:
+        assert rapport["arret"] is None and rapport["envois_partis"] == 1004
+    shutil.rmtree(racine)
+
+
+def test_environnement_epure_sain_et_artefact():
+    sain = {"PATH": "/usr/bin", "HOME": "/tmp", "LANG": "C.UTF-8", "LC_CTYPE": "C.UTF-8", "GO_ID": "GO-2026-11-20-26"}
+    assert M.exiger_environnement_epure(sain) == sorted(sain)
+    assert M.exiger_environnement_epure({}) == []
+    with pytest.raises(M.Refus, match="non épuré"):
+        M.exiger_environnement_epure(dict(sain, VARIABLE_HORS_LISTE="x"))
+    with pytest.raises(M.Refus, match="non épuré"):
+        M.exiger_environnement_epure({"PATH": "/usr/bin", "HTTPS_PROXY": "http://127.0.0.1:1"})
+
+
+def test_mode_reel_environnement_liste_blanche_accepte(tmp_path, configuration):
+    import datetime as dt
+    banque, h = ecrire_banque(tmp_path, configuration["items_juge"])
+    decl = tmp_path / "declaration.json"
+    octets = M.json_octets({"fournisseurs": {"claude": {}, "argon": {}}})
+    decl.write_bytes(octets)
+    hd = M.sha256_octets(octets)
+    Path(str(decl) + ".sha256").write_text(f"{hd}  declaration.json\n", encoding="utf-8")
+    appels = []
+    env = {"PATH": "/usr/bin", "HOME": "/tmp", "LC_CTYPE": "C.UTF-8", "GO_ID": "GO-2026-11-20-26"}
+    M.preparer_reel(_argv(tmp_path, banque, h, decl, hd), env, dt.date(2026, 11, 20),
+                    lire_registre=lambda: {"texte": REGISTRE, "commit": "essai", "sha256": "essai"},
+                    construire_service=lambda **kw: (appels.append(kw), (None, {}))[1])
+    assert len(appels) == 1 and appels[0]["nom_cle_claude"] == "NOM_FACTICE"
```

Développeur, modèle O.
