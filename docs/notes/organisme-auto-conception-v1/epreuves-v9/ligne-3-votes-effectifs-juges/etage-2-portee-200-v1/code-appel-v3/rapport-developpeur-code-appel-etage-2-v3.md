# Rapport du développeur — code d'appel de l'étage 2 à 200 témoins (ligne 3, organisme v9) — v3

Pièce d'instrument (classe B), écrite le 2026-11-20 par le même développeur, modèle O, sur le même mandat
(`mandat-developpeur-code-appel-etage-2-v1.md`, `d20e40d5…`, en-tête compris) et sur la correction bloquante de la mère
(14:10Z), rapportée par la coordination. La v2 (`code-appel-v2/`, programme `1a0b08d5…`, essais `b1767abb…`, rapport
`f79a5707…`) est gardée sans modification ; ses rapports (v1 et v2) valent pour tout ce que celui-ci ne change pas. Rien n'a
tourné contre un vrai juge ; aucune valeur de variable n'a été lue ; rien n'a été écrit dans le dépôt.

## 1. La correction de la mère, portée

- `VARIABLES_PERMISES` garde en plus : `HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY`, `https_proxy`, `http_proxy`, `no_proxy` ;
  `SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`, `NODE_EXTRA_CA_CERTS` ; `RR_ANTHROPIC_API_KEY_LUC`,
  `GEMINI_API_KEY` (par le nom seul).
- Constante neuve `VARIABLES_EXIGEES = ("HTTPS_PROXY",)` ; `exiger_environnement_epure` refuse le départ réel si une variable
  exigée manque (après le refus d'une variable hors liste, gardé tel quel).
- Rien d'autre ne change dans le programme (nom de version et en-tête mis à part).

Essais :
- `test_v3_depart_reel_exige_https_proxy` : cas sain, `HTTPS_PROXY` présente avec les noms relevés dans ce conteneur
  (`CURL_CA_BUNDLE`, `NODE_EXTRA_CA_CERTS`, `REQUESTS_CA_BUNDLE`, `SSL_CERT_FILE`, `HTTPS_PROXY`, `https_proxy`, `NO_PROXY`,
  `no_proxy`, plus `PATH` et `HOME`, valeurs factices) : la garde passe, le constructeur de service est appelé une fois ;
  artefact, `HTTPS_PROXY` absente : refus « variables exigées absentes » avant tout service.
- `test_v3_liste_blanche_elargie` : les douze noms sont dans la liste ; l'essai de refus d'une variable hors liste est gardé
  (ici et dans `test_environnement_epure_sain_et_artefact`, où l'artefact « mandataire refusé » de la v2 devient
  `ALL_PROXY`, qui reste hors liste).
- Essais de la v2 qui passaient un environnement vide au mode réel : ils passent désormais `HTTPS_PROXY` (valeur factice),
  sans quoi ils s'arrêteraient sur la garde neuve avant le refus qu'ils éprouvent ; leurs motifs attendus ne changent pas.

## 2. Constat bloquant, porté à la mère sans le trancher

**Les deux noms de clé sont dans la liste blanche, mais leur présence fait toujours refuser le départ.** La garde des noms de
clé, reprise du précédent et gardée sans changement (« rien d'autre ne change »), passe avant la liste blanche dans
`preparer_reel` : tout nom qui contient `API_KEY`, `TOKEN`, `SECRET`… est refusé (« la clé reste dans son relais »). Essai qui
le montre : `test_v3_nom_de_cle_dans_la_liste_blanche_mais_refuse_par_la_garde_des_cles` (les deux noms : la liste blanche les
accepte, le départ est refusé). De plus, l'orchestrateur épinglé refuse lui-même `GEMINI_API_KEY` dans l'environnement :
`pole/relais.py` l. 15-18 (`NOMS_DE_CLE`), employé par l'adaptateur du kit (`AdaptateurClaudeSDK.lancer`) et par l'adaptateur à
commande externe (`environnement_commande`) : chaque appel serait refusé par l'adaptateur. Si la mère veut que ces noms soient
présents au départ, il faut deux décisions : lever la garde des noms de clé du programme pour ces deux noms, et dire comment
les adaptateurs de l'orchestrateur (épinglés, non modifiables ici) les tolèrent — par exemple un environnement du programme
sans ces noms, les clés restant aux relais, comme au précédent. En l'état, le départ réel n'est possible que sans ces deux noms
dans l'environnement.

## 3. Sortie des essais

Commande exacte (sur ma copie) :

`env -C /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v3 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_epreuve_juges_reels_ligne_3_v3.py`

Résultat : **97 passed in 111.04s**, en tâche de fond, sur le programme 969653f2… et les essais 0a71fa77… ; aucun échec, aucun saut. 97 = les 93 essais de la v2, plus 4 : départ refusé sans HTTPS_PROXY (sain et artefact dans un essai), liste blanche élargie, et le constat du § 2 pour chacun des deux noms de clé.

## 4. Écarts

1. Les essais de la v2 du mode réel reçoivent `HTTPS_PROXY` (factice) dans leur environnement (§ 1) ; l'artefact
   `HTTPS_PROXY` de l'essai de l'environnement épuré devient `ALL_PROXY`.
2. Différentiels écrits dans mon dossier, hors de `code-appel-v3/` (`../diff-programme-v2-v3.txt`, `../diff-essais-v2-v3.txt`),
   recopiés ci-dessous par l'outil `../outils/inserer_diffs.py`.
3. Lecture d'un fichier de plus du clone : `pole/relais.py` (une recherche sur ce seul fichier).
4. Aucun refus de permission, de classifieur ou de garde.

## 5. Différentiels v2 → v3 (`diff -u`)

### 5.1 Programme

```diff
--- /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v2/epreuve_juges_reels_ligne_3_v2.py	2026-11-20 14:04:12.785208020 +0000
+++ /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v3/epreuve_juges_reels_ligne_3_v3.py	2026-11-20 14:10:59.489253742 +0000
@@ -1,5 +1,13 @@
 #!/usr/bin/env python3
-"""Épreuve des juges réels — ligne 3 de l'organisme v9 (votes effectifs des juges croisés), étage 2 à 200 témoins — v2.
+"""Épreuve des juges réels — ligne 3 de l'organisme v9 (votes effectifs des juges croisés), étage 2 à 200 témoins — v3.
+
+Version 3 (même développeur, règle R12 ; la v2, `epreuve_juges_reels_ligne_3_v2.py`, 1a0b08d5…, est gardée sans
+modification) : correction de la mère (14:10Z). La liste blanche `VARIABLES_PERMISES` garde en plus le mandataire réseau
+(HTTPS_PROXY, HTTP_PROXY, NO_PROXY et leurs formes en minuscules), les variables du paquet de certificats (SSL_CERT_FILE,
+REQUESTS_CA_BUNDLE, CURL_CA_BUNDLE, NODE_EXTRA_CA_CERTS) et les noms des deux clés employées (par le nom seul) ; le départ
+réel est refusé si HTTPS_PROXY manque (`VARIABLES_EXIGEES`). Rien d'autre ne change.
+
+Texte de la v2 :
 
 Version 2 (même développeur, règle R12 ; la v1, `epreuve_juges_reels_ligne_3_v1.py`, 586bc7e6…, est gardée sans
 modification) : les trois corrections de la contre-lecture `contre-lecture-code-appel-etage-2-v1.md` (4bcab58a…), à la
@@ -72,7 +80,7 @@
 from fractions import Fraction
 from pathlib import Path
 
-VERSION = "epreuve_juges_reels_ligne_3_v2"
+VERSION = "epreuve_juges_reels_ligne_3_v3"
 
 # --- plafond (une seule constante, égale à la ligne de GO lue) -------------------------------------------------------------
 PLAFOND_C = 8836            # 88,36 USD en centimes entiers : GO-2026-11-20-26 ; additif 3 v3, § 4.2
@@ -141,7 +149,12 @@
 # Liste blanche des variables permises au départ du mode réel, lancé sous `env -i` : celles du lanceur v9 (`NOMS_PERMIS`),
 # plus HOME (sonde du bac à sable du précédent), LC_CTYPE (posée par l'interpréteur lui-même quand il force un locale UTF-8
 # sous un environnement vide) et GO_ID (garde de calcul du dépôt).
-VARIABLES_PERMISES = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TZ", "TMPDIR", "HOME", "GO_ID")
+VARIABLES_PERMISES = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TZ", "TMPDIR", "HOME", "GO_ID",
+                      # v3, correction de la mère (14:10Z) : mandataire réseau, paquet de certificats, noms des deux clés
+                      "HTTPS_PROXY", "HTTP_PROXY", "NO_PROXY", "https_proxy", "http_proxy", "no_proxy",
+                      "SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS",
+                      "RR_ANTHROPIC_API_KEY_LUC", "GEMINI_API_KEY")
+VARIABLES_EXIGEES = ("HTTPS_PROXY",)                # v3 : sans mandataire, aucun appel n'aboutit dans ce conteneur
 NOM_DE_VARIABLE = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
 
 # --- statuts des adaptateurs de l'orchestrateur -----------------------------------------------------------------------------
@@ -1285,6 +1298,9 @@
     hors = sorted(n for n in environ if n not in VARIABLES_PERMISES)
     if hors:
         raise Refus(f"environnement non épuré : variables hors de la liste blanche ({hors}) : lancer sous env -i")
+    manquantes = [n for n in VARIABLES_EXIGEES if n not in environ]               # v3
+    if manquantes:
+        raise Refus(f"environnement : variables exigées absentes ({manquantes}) : sans mandataire, aucun appel n'aboutit")
     return sorted(environ)
 
 
```

### 5.2 Essais

```diff
--- /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v2/essais_epreuve_juges_reels_ligne_3_v2.py	2026-11-20 14:03:41.744442237 +0000
+++ /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v3/essais_epreuve_juges_reels_ligne_3_v3.py	2026-11-20 14:11:47.356471103 +0000
@@ -1,4 +1,8 @@
-"""Essais de `epreuve_juges_reels_ligne_3_v2.py` (pytest, service factice seul : aucun réseau, aucune clé, aucun relais).
+"""Essais de `epreuve_juges_reels_ligne_3_v3.py` (pytest, service factice seul : aucun réseau, aucune clé, aucun relais).
+
+Version 3 (R12 ; la v2 est gardée) : les essais de la v2 sur le module v3 ; ceux du mode réel passent un environnement qui
+porte HTTPS_PROXY (nom seul, valeur factice) ; essais neufs en fin de fichier : départ refusé sans HTTPS_PROXY, liste blanche
+élargie (correction de la mère, 14:10Z).
 
 Version 2 (R12 ; la v1 est gardée) : les essais de la v1, sur le module v2, plus les essais des corrections C1, C2, C3 de la
 contre-lecture et des décisions de la mère (2) et (3) (nom de la clé, environnement épuré), en fin de fichier.
@@ -21,7 +25,9 @@
 
 ICI = Path(__file__).resolve().parent
 sys.path.insert(0, str(ICI))
-import epreuve_juges_reels_ligne_3_v2 as M  # noqa: E402
+import epreuve_juges_reels_ligne_3_v3 as M  # noqa: E402
+
+ENV_BASE = {"HTTPS_PROXY": "http://127.0.0.1:1"}      # v3 : valeur factice ; seul le nom est lu par le programme
 
 L3 = M.DEPOT / "docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1"
 CALCUL = (L3 / "calcul_conditions_plafond_200_ligne_3_v2.py",
@@ -726,9 +732,9 @@
     ]
     for argv, env, motif in cas:
         with pytest.raises(M.Refus, match=motif):
-            M.preparer_reel(argv, env, jour, lire_registre=registre, construire_service=constructeur)
+            M.preparer_reel(argv, dict(ENV_BASE, **env), jour, lire_registre=registre, construire_service=constructeur)
     assert appels == []                                                  # aucun service construit, aucun relais touché
-    prep = M.preparer_reel(_argv(tmp_path, banque, h, decl, hd), {}, jour, lire_registre=registre,
+    prep = M.preparer_reel(_argv(tmp_path, banque, h, decl, hd), dict(ENV_BASE), jour, lire_registre=registre,
                            construire_service=constructeur)
     assert len(appels) == 1 and prep["contexte"]["ligne_de_go"]["id"] == "GO-2026-11-20-26"
 
@@ -864,13 +870,14 @@
 
 
 def test_environnement_epure_sain_et_artefact():
-    sain = {"PATH": "/usr/bin", "HOME": "/tmp", "LANG": "C.UTF-8", "LC_CTYPE": "C.UTF-8", "GO_ID": "GO-2026-11-20-26"}
+    sain = {"PATH": "/usr/bin", "HOME": "/tmp", "LANG": "C.UTF-8", "LC_CTYPE": "C.UTF-8", "GO_ID": "GO-2026-11-20-26",
+            **ENV_BASE}
     assert M.exiger_environnement_epure(sain) == sorted(sain)
-    assert M.exiger_environnement_epure({}) == []
+    assert M.exiger_environnement_epure(dict(ENV_BASE)) == ["HTTPS_PROXY"]
     with pytest.raises(M.Refus, match="non épuré"):
         M.exiger_environnement_epure(dict(sain, VARIABLE_HORS_LISTE="x"))
     with pytest.raises(M.Refus, match="non épuré"):
-        M.exiger_environnement_epure({"PATH": "/usr/bin", "HTTPS_PROXY": "http://127.0.0.1:1"})
+        M.exiger_environnement_epure(dict(sain, ALL_PROXY="http://127.0.0.1:1"))
 
 
 def test_mode_reel_environnement_liste_blanche_accepte(tmp_path, configuration):
@@ -882,8 +889,59 @@
     hd = M.sha256_octets(octets)
     Path(str(decl) + ".sha256").write_text(f"{hd}  declaration.json\n", encoding="utf-8")
     appels = []
-    env = {"PATH": "/usr/bin", "HOME": "/tmp", "LC_CTYPE": "C.UTF-8", "GO_ID": "GO-2026-11-20-26"}
+    env = {"PATH": "/usr/bin", "HOME": "/tmp", "LC_CTYPE": "C.UTF-8", "GO_ID": "GO-2026-11-20-26", **ENV_BASE}
     M.preparer_reel(_argv(tmp_path, banque, h, decl, hd), env, dt.date(2026, 11, 20),
                     lire_registre=lambda: {"texte": REGISTRE, "commit": "essai", "sha256": "essai"},
                     construire_service=lambda **kw: (appels.append(kw), (None, {}))[1])
     assert len(appels) == 1 and appels[0]["nom_cle_claude"] == "NOM_FACTICE"
+
+
+# --- v3 : correction de la mère (14:10Z) ----------------------------------------------------------------------------------------
+
+
+def _preparer(tmp_path, configuration, env):
+    import datetime as dt
+    banque, h = ecrire_banque(tmp_path, configuration["items_juge"])
+    decl = tmp_path / "declaration.json"
+    octets = M.json_octets({"fournisseurs": {"claude": {}, "argon": {}}})
+    decl.write_bytes(octets)
+    hd = M.sha256_octets(octets)
+    Path(str(decl) + ".sha256").write_text(f"{hd}  declaration.json\n", encoding="utf-8")
+    appels = []
+    M.preparer_reel(_argv(tmp_path, banque, h, decl, hd), env, dt.date(2026, 11, 20),
+                    lire_registre=lambda: {"texte": REGISTRE, "commit": "essai", "sha256": "essai"},
+                    construire_service=lambda **kw: (appels.append(kw), (None, {}))[1])
+    return appels
+
+
+def test_v3_depart_reel_exige_https_proxy(tmp_path, configuration):
+    """Cas sain : HTTPS_PROXY présente (avec les variables du mandataire et des certificats relevées dans ce conteneur) :
+    le départ passe la garde. Artefact : HTTPS_PROXY absente : refus avant tout service."""
+    noms_du_conteneur = ("CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS", "REQUESTS_CA_BUNDLE", "SSL_CERT_FILE", "HTTPS_PROXY",
+                         "https_proxy", "NO_PROXY", "no_proxy")
+    sain = {n: "valeur-factice" for n in noms_du_conteneur}
+    sain.update(PATH="/usr/bin", HOME="/tmp")
+    (tmp_path / "sain").mkdir()
+    assert len(_preparer(tmp_path / "sain", configuration, sain)) == 1
+    sans = {k: v for k, v in sain.items() if k != "HTTPS_PROXY"}
+    (tmp_path / "artefact").mkdir()
+    with pytest.raises(M.Refus, match="variables exigées absentes"):
+        _preparer(tmp_path / "artefact", configuration, sans)
+
+
+def test_v3_liste_blanche_elargie():
+    for n in ("HTTPS_PROXY", "HTTP_PROXY", "NO_PROXY", "https_proxy", "http_proxy", "no_proxy", "SSL_CERT_FILE",
+              "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS", "RR_ANTHROPIC_API_KEY_LUC", "GEMINI_API_KEY"):
+        assert n in M.VARIABLES_PERMISES
+    assert M.VARIABLES_EXIGEES == ("HTTPS_PROXY",)
+    with pytest.raises(M.Refus, match="non épuré"):                    # l'essai de refus hors liste est gardé
+        M.exiger_environnement_epure(dict(ENV_BASE, VARIABLE_HORS_LISTE="x"))
+
+
+@pytest.mark.parametrize("nom", ["RR_ANTHROPIC_API_KEY_LUC", "GEMINI_API_KEY"])
+def test_v3_nom_de_cle_dans_la_liste_blanche_mais_refuse_par_la_garde_des_cles(tmp_path, configuration, nom):
+    """Constat porté à la mère, non tranché : le nom est dans la liste blanche (garde de l'environnement épuré), mais la garde
+    des noms de clé, reprise du précédent et gardée sans changement, refuse toujours le départ si ce nom est présent."""
+    assert M.exiger_environnement_epure(dict(ENV_BASE, **{nom: "valeur-factice"})) == sorted([nom, "HTTPS_PROXY"])
+    with pytest.raises(M.Refus, match="noms de variables de clé"):
+        _preparer(tmp_path, configuration, dict(ENV_BASE, **{nom: "valeur-factice"}))
```

Développeur, modèle O.
