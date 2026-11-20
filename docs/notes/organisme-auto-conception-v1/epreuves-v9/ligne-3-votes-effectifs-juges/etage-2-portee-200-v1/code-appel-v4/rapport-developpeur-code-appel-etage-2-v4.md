# Rapport du développeur — code d'appel de l'étage 2 à 200 témoins (ligne 3, organisme v9) — v4

Pièce d'instrument (classe B), écrite le 2026-11-20 par le même développeur, modèle O, sur le même mandat
(`mandat-developpeur-code-appel-etage-2-v1.md`, `d20e40d5…`, en-tête compris) et sur la décision de la mère R-4290 (14:15Z,
voie (i)), rapportée par la coordination. La v3 (`code-appel-v3/`, programme `969653f2…`, essais `0a71fa77…`, rapport
`91e7d0ca…`) est gardée sans modification ; les rapports v1 à v3 valent pour tout ce que celui-ci ne change pas. Rien n'a
tourné contre un vrai juge ; aucune valeur de variable n'a été lue ; rien n'a été écrit dans le dépôt.

## 1. La décision, portée

- `RR_ANTHROPIC_API_KEY_LUC` et `GEMINI_API_KEY` sortent de `VARIABLES_PERMISES`. Les clés vivent dans l'environnement des
  seuls relais, lancés à part, comme à la course v9 ; le code épinglé (précédent, lanceur, orchestrateur) ne change pas.
- La garde des noms de clé reste telle quelle (elle passe la première dans `preparer_reel`).
- Le mandataire (`HTTPS_PROXY` exigé ; `HTTP_PROXY`, `NO_PROXY` et les formes en minuscules permis) et les variables du paquet
  de certificats restent dans la liste.
- Le constat bloquant du rapport v3, § 2, est levé par cette décision : le départ réel se fait sans aucun nom de clé dans
  l'environnement du programme.
- Rien d'autre ne change dans le programme (nom de version et en-tête mis à part).

Essais :
- Les deux essais du constat de la v3 sont remplacés par :
  - `test_v4_aucun_nom_de_cle_mandataire_present_depart_accepte` (cas sain) : aucun nom de clé, mandataire et certificats
    présents (valeurs factices) ; le départ passe les gardes de l'environnement, de la ligne de GO, de la banque et de la
    déclaration, jusqu'au constructeur du service, appelé une fois (garde suivante, factice) ;
  - `test_v4_nom_de_cle_present_refus_nomme` (artefact, pour chacun des deux noms) : refus nommé par la garde des noms de
    clé (« noms de variables de clé dans l'environnement ([nom]) »), avant tout service ; le nom est aussi hors de la liste
    blanche (refus « non épuré » qui le nomme).
- `test_v3_liste_blanche_elargie` vérifie désormais que les deux noms ne sont pas dans la liste ; l'essai de refus d'une
  variable hors liste est gardé.
- Le reste est inchangé.

## 2. Sortie des essais

Commande exacte (sur ma copie) :

`env -C /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v4 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_epreuve_juges_reels_ligne_3_v4.py`

Résultat : **98 passed in 126.85s**, en tâche de fond, sur le programme 082d19d6… et les essais 072439a0… ; aucun échec, aucun saut. 98 = les 97 essais de la v3, moins les 2 essais du constat, plus le cas sain (1) et l'artefact pour chacun des deux noms (2).

## 3. Écarts

1. Différentiels écrits dans mon dossier, hors de `code-appel-v4/` (`../diff-programme-v3-v4.txt`, `../diff-essais-v3-v4.txt`),
   recopiés ci-dessous par l'outil `../outils/inserer_diffs.py`.
2. Le texte de la v3 recopié dans l'en-tête du programme (historique des versions) nomme encore la liste blanche de la v3 ;
   l'en-tête de la v4, au-dessus, dit qu'elle est corrigée.
3. Aucun refus de permission, de classifieur ou de garde.

## 4. Différentiels v3 → v4 (`diff -u`)

### 4.1 Programme

```diff
--- /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v3/epreuve_juges_reels_ligne_3_v3.py	2026-11-20 14:10:59.489253742 +0000
+++ /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v4/epreuve_juges_reels_ligne_3_v4.py	2026-11-20 14:16:05.072486422 +0000
@@ -1,5 +1,12 @@
 #!/usr/bin/env python3
-"""Épreuve des juges réels — ligne 3 de l'organisme v9 (votes effectifs des juges croisés), étage 2 à 200 témoins — v3.
+"""Épreuve des juges réels — ligne 3 de l'organisme v9 (votes effectifs des juges croisés), étage 2 à 200 témoins — v4.
+
+Version 4 (même développeur, règle R12 ; la v3, `epreuve_juges_reels_ligne_3_v3.py`, 969653f2…, est gardée sans
+modification) : décision de la mère (R-4290, 14:15Z, voie (i)). Les deux noms de clé sortent de `VARIABLES_PERMISES` : les
+clés vivent dans l'environnement des seuls relais, lancés à part, comme à la course v9 ; la garde des noms de clé reste telle
+quelle ; le mandataire (HTTPS_PROXY exigé) et les certificats restent. Rien d'autre ne change.
+
+Texte de la v3 :
 
 Version 3 (même développeur, règle R12 ; la v2, `epreuve_juges_reels_ligne_3_v2.py`, 1a0b08d5…, est gardée sans
 modification) : correction de la mère (14:10Z). La liste blanche `VARIABLES_PERMISES` garde en plus le mandataire réseau
@@ -80,7 +87,7 @@
 from fractions import Fraction
 from pathlib import Path
 
-VERSION = "epreuve_juges_reels_ligne_3_v3"
+VERSION = "epreuve_juges_reels_ligne_3_v4"
 
 # --- plafond (une seule constante, égale à la ligne de GO lue) -------------------------------------------------------------
 PLAFOND_C = 8836            # 88,36 USD en centimes entiers : GO-2026-11-20-26 ; additif 3 v3, § 4.2
@@ -150,10 +157,10 @@
 # plus HOME (sonde du bac à sable du précédent), LC_CTYPE (posée par l'interpréteur lui-même quand il force un locale UTF-8
 # sous un environnement vide) et GO_ID (garde de calcul du dépôt).
 VARIABLES_PERMISES = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TZ", "TMPDIR", "HOME", "GO_ID",
-                      # v3, correction de la mère (14:10Z) : mandataire réseau, paquet de certificats, noms des deux clés
+                      # v3, correction de la mère (14:10Z) : mandataire réseau, paquet de certificats ; v4 (R-4290) : aucun
+                      # nom de clé (les clés vivent dans l'environnement des seuls relais)
                       "HTTPS_PROXY", "HTTP_PROXY", "NO_PROXY", "https_proxy", "http_proxy", "no_proxy",
-                      "SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS",
-                      "RR_ANTHROPIC_API_KEY_LUC", "GEMINI_API_KEY")
+                      "SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS")
 VARIABLES_EXIGEES = ("HTTPS_PROXY",)                # v3 : sans mandataire, aucun appel n'aboutit dans ce conteneur
 NOM_DE_VARIABLE = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
 
```

### 4.2 Essais

```diff
--- /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v3/essais_epreuve_juges_reels_ligne_3_v3.py	2026-11-20 14:11:47.356471103 +0000
+++ /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v4/essais_epreuve_juges_reels_ligne_3_v4.py	2026-11-20 14:16:27.132487734 +0000
@@ -1,4 +1,8 @@
-"""Essais de `epreuve_juges_reels_ligne_3_v3.py` (pytest, service factice seul : aucun réseau, aucune clé, aucun relais).
+"""Essais de `epreuve_juges_reels_ligne_3_v4.py` (pytest, service factice seul : aucun réseau, aucune clé, aucun relais).
+
+Version 4 (R12 ; la v3 est gardée) : les essais de la v3 sur le module v4 ; la liste blanche ne porte plus aucun nom de clé
+(R-4290) ; les essais du constat de la v3 sont remplacés par un cas sain (aucun nom de clé, mandataire présent : départ
+accepté jusqu'à la garde suivante) et un artefact (un des deux noms présent : refus nommé).
 
 Version 3 (R12 ; la v2 est gardée) : les essais de la v2 sur le module v3 ; ceux du mode réel passent un environnement qui
 porte HTTPS_PROXY (nom seul, valeur factice) ; essais neufs en fin de fichier : départ refusé sans HTTPS_PROXY, liste blanche
@@ -25,7 +29,7 @@
 
 ICI = Path(__file__).resolve().parent
 sys.path.insert(0, str(ICI))
-import epreuve_juges_reels_ligne_3_v3 as M  # noqa: E402
+import epreuve_juges_reels_ligne_3_v4 as M  # noqa: E402
 
 ENV_BASE = {"HTTPS_PROXY": "http://127.0.0.1:1"}      # v3 : valeur factice ; seul le nom est lu par le programme
 
@@ -931,17 +935,30 @@
 
 def test_v3_liste_blanche_elargie():
     for n in ("HTTPS_PROXY", "HTTP_PROXY", "NO_PROXY", "https_proxy", "http_proxy", "no_proxy", "SSL_CERT_FILE",
-              "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS", "RR_ANTHROPIC_API_KEY_LUC", "GEMINI_API_KEY"):
+              "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS"):
         assert n in M.VARIABLES_PERMISES
+    for n in ("RR_ANTHROPIC_API_KEY_LUC", "GEMINI_API_KEY"):              # v4 (R-4290) : aucun nom de clé dans la liste
+        assert n not in M.VARIABLES_PERMISES
     assert M.VARIABLES_EXIGEES == ("HTTPS_PROXY",)
     with pytest.raises(M.Refus, match="non épuré"):                    # l'essai de refus hors liste est gardé
         M.exiger_environnement_epure(dict(ENV_BASE, VARIABLE_HORS_LISTE="x"))
 
 
+def test_v4_aucun_nom_de_cle_mandataire_present_depart_accepte(tmp_path, configuration):
+    """Cas sain (R-4290) : aucun nom de clé dans l'environnement du programme, mandataire et certificats présents : le
+    départ passe les gardes de l'environnement, de la ligne de GO, de la banque et de la déclaration, jusqu'au constructeur
+    du service (la garde suivante, ici factice)."""
+    env = {n: "valeur-factice" for n in ("HTTPS_PROXY", "https_proxy", "NO_PROXY", "no_proxy", "SSL_CERT_FILE",
+                                         "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS")}
+    env.update(PATH="/usr/bin", HOME="/tmp")
+    assert len(_preparer(tmp_path, configuration, env)) == 1
+
+
 @pytest.mark.parametrize("nom", ["RR_ANTHROPIC_API_KEY_LUC", "GEMINI_API_KEY"])
-def test_v3_nom_de_cle_dans_la_liste_blanche_mais_refuse_par_la_garde_des_cles(tmp_path, configuration, nom):
-    """Constat porté à la mère, non tranché : le nom est dans la liste blanche (garde de l'environnement épuré), mais la garde
-    des noms de clé, reprise du précédent et gardée sans changement, refuse toujours le départ si ce nom est présent."""
-    assert M.exiger_environnement_epure(dict(ENV_BASE, **{nom: "valeur-factice"})) == sorted([nom, "HTTPS_PROXY"])
-    with pytest.raises(M.Refus, match="noms de variables de clé"):
+def test_v4_nom_de_cle_present_refus_nomme(tmp_path, configuration, nom):
+    """Artefact (R-4290) : un des deux noms de clé présent dans l'environnement du programme : refus nommé, avant tout
+    service ; la clé vit dans l'environnement des seuls relais."""
+    with pytest.raises(M.Refus, match=f"noms de variables de clé .*{nom}"):
         _preparer(tmp_path, configuration, dict(ENV_BASE, **{nom: "valeur-factice"}))
+    with pytest.raises(M.Refus, match=f"non épuré.*{nom}"):             # hors de la liste blanche, refusé aussi par elle
+        M.exiger_environnement_epure(dict(ENV_BASE, **{nom: "valeur-factice"}))
```

Développeur, modèle O.
