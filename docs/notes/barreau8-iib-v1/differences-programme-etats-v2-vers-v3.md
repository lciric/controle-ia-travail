# Différences — programme des états v2 → v3, essais v2 → v3

Un seul changement de code : garde du run_id du manifeste scellé (mot de la mère, 2026-11-19 vers 04:38Z). Différences produites par `diff -u`.

```diff
--- scripts/extrait_iib_etats_lectures_cote_moniteurs_v2.py	2026-11-19 00:58:27.466745915 +0000
+++ scripts/extrait_iib_etats_lectures_cote_moniteurs_v3.py	2026-11-19 04:38:29.887933998 +0000
@@ -1,4 +1,8 @@
-"""Extrait des ÉTATS des lectures du dommage et de la diffusion du saboteur à budget, pour le côté moniteurs, v2.
+"""Extrait des ÉTATS des lectures du dommage et de la diffusion du saboteur à budget, pour le côté moniteurs, v3.
+
+v3 = v2 + un seul changement (mot de la mère du 2026-11-19 vers 04:38Z) : avant toute lecture et toute écriture, refus si
+l'argument `--run-id` diffère du `run_id` du manifeste scellé `runs/RUN/manifeste.json`, dont le sceau est vérifié, comme le fait
+déjà le programme de l'extrait de la passe (`extrait_iib_cote_moniteurs_v2.py`).
 
 v2 = v1 + couples P-01 à P-03 de la vérification de la note v4 et du programme des états (côté exposé) :
 - P-01 (ordre du temps) : rien n'est lu ni écrit tant que le registre propre du côté moniteurs (`--registre-sondes`,
@@ -19,7 +23,7 @@
 Aucun chiffre hors du nom du run, fixé au lancement, et des noms des conditions ; aucune autre phrase, aucune autre clé.
 Toute valeur hors vocabulaire, tout jeu ou unité manquant ou en trop : refus, sans imprimer la valeur refusée et sans rien écrire.
 
-    PYTHONPATH=src python scripts/extrait_iib_etats_lectures_cote_moniteurs_v2.py --racine . --run-id RUN \\
+    PYTHONPATH=src python scripts/extrait_iib_etats_lectures_cote_moniteurs_v3.py --racine . --run-id RUN \\
         --registre-sondes registres/sondes-iib-v1.md --sortie CHEMIN
 
 Écrit et scelle CHEMIN (jamais d'écrasement, R12) ; imprime son empreinte et celle du texte du côté moniteurs cité par la
@@ -93,8 +97,16 @@
     return run_id
 
 
+def exiger_run_id_du_manifeste(racine: Path, run_id: str) -> None:
+    """v3 : le nom du run est celui du manifeste scellé de la course (sceau vérifié) ; les noms ne sont pas imprimés."""
+    m, _ = _lire(racine / "runs" / run_id / "manifeste.json")
+    if m.get("run_id") != run_id:
+        raise GardeArret("manifeste : run_id différent de l'argument --run-id (non imprimés)")
+
+
 def construire(racine: Path, run_id: str) -> dict:
     exiger_run_id(run_id)
+    exiger_run_id_du_manifeste(racine, run_id)
     d = racine / "diag" / run_id
     l1, sha_1 = _lire(d / NOM_DOMMAGE)
     l2, _ = _lire(d / NOM_DIFFUSION)
@@ -133,7 +145,7 @@
 
 
 def main(argv: list[str]) -> int:
-    p = argparse.ArgumentParser(prog="extrait_iib_etats_lectures_cote_moniteurs_v2")
+    p = argparse.ArgumentParser(prog="extrait_iib_etats_lectures_cote_moniteurs_v3")
     p.add_argument("--racine", default=".")
     p.add_argument("--run-id", required=True)
     p.add_argument("--registre-sondes", required=True)
--- tests/test_iib_extrait_etats_lectures_v2.py	2026-11-19 00:59:14.754748726 +0000
+++ tests/test_iib_extrait_etats_lectures_v3.py	2026-11-19 04:38:48.378418085 +0000
@@ -1,4 +1,7 @@
-"""Essais de `scripts/extrait_iib_etats_lectures_cote_moniteurs_v2.py` (R5 : cas sains et artefacts), sur des lectures factices.
+"""Essais de `scripts/extrait_iib_etats_lectures_cote_moniteurs_v3.py` (R5 : cas sains et artefacts), sur des lectures factices.
+
+v3 = essais v2, chaque course factice recevant son manifeste scellé `runs/RUN/manifeste.json` (run_id = RUN), plus un cas sain
+et un artefact de la garde v3 (manifeste au run_id différent de l'argument).
 
 v2 = v1 + couples T-01 (garde d'ordre du temps : cas sain et huit artefacts), T-02 (même chaîne de lectures, forme du nom du
 run), T-03 (preuve de la non-ouverture du fichier des mots pondérés : crochet d'audit des ouvertures et dossier posé à son nom).
@@ -13,7 +16,7 @@
 from controle_ia.scellement import sceller
 
 RACINE_DEPOT = Path(__file__).resolve().parents[1]
-spec = importlib.util.spec_from_file_location("etats_v2", RACINE_DEPOT / "scripts" / "extrait_iib_etats_lectures_cote_moniteurs_v2.py")
+spec = importlib.util.spec_from_file_location("etats_v3", RACINE_DEPOT / "scripts" / "extrait_iib_etats_lectures_cote_moniteurs_v3.py")
 ex = importlib.util.module_from_spec(spec)
 spec.loader.exec_module(ex)
 
@@ -57,7 +60,14 @@
     return reg
 
 
+def _manifeste(r: Path, run_id=RUN) -> None:
+    p = r / "runs" / RUN / "manifeste.json"
+    if not p.exists():
+        _ecrire(p, {"run_id": run_id, "commit": "0" * 40})
+
+
 def _lectures(r: Path, l1=None, l2=None, l2_fn=None, mots=True) -> None:
+    _manifeste(r)
     d = r / "diag" / RUN
     sha_1 = _ecrire(d / ex.NOM_DOMMAGE, l1 if l1 is not None else _l1()) if l1 is not False else "0" * 64
     if l2 is not False:
@@ -318,3 +328,23 @@
     s.write_text("ancien")
     assert _jouer(tmp_path, s) == 1
     assert s.read_text() == "ancien"
+
+
+# --- v3 : run_id du manifeste scellé -----------------------------------------------------------------------------------------
+def test_v3_cas_sain_run_id_egal_au_manifeste(tmp_path):
+    _sain(tmp_path)
+    s = tmp_path / "e.json"
+    assert _jouer(tmp_path, s) == 0
+    m = json.loads((tmp_path / "runs" / RUN / "manifeste.json").read_text(encoding="utf-8"))
+    assert json.loads(s.read_text(encoding="utf-8"))["run_id"] == m["run_id"] == RUN
+
+
+def test_v3_artefact_manifeste_au_run_id_different(tmp_path, capsys):
+    autre = "20991231-000001-iib-explo-factice"
+    _manifeste(tmp_path, run_id=autre)
+    _sain(tmp_path)
+    s = tmp_path / "e.json"
+    assert _jouer(tmp_path, s) == 1
+    assert not s.exists() and not Path(str(s) + ".sha256").exists()
+    err = capsys.readouterr().err
+    assert "manifeste" in err and autre not in err
```
