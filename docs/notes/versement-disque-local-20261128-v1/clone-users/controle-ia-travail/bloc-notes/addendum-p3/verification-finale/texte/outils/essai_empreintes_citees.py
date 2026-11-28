"""Essai (3) de la vérification « texte face au code » : le module lit-il, dans le TEXTE FINAL, les lignes
« Module de l'addendum (sha256) : `…` » et « Tests du module (sha256) : `…` », et les compare-t-il aux fichiers exécutés ?

Dépôt git jouet sous verification-finale/texte/jouet/ (rien ailleurs). Copie du texte final (brouillon 6) où les
marqueurs sont remplis : empreintes réelles du module et des tests, 165 tests, empreinte du traitement ; marqueurs de la
contre-lecture 4 remplis de valeurs factices distinctes (sans objet pour la garde 1). Seule différence voulue avec le texte
final : le commit cité est celui du dépôt jouet (sinon `exiger_code_cite` ne peut pas s'y appliquer). Le module est chargé
depuis son chemin versé dans le jouet ; `exiger_garde_1` est la vraie fonction, sans remplacement.

Usage : PYTHONPATH=<dépôt>/src python -I -B essai_empreintes_citees.py <texte final> <module> <tests> <traitement> <jouet>
"""
import hashlib
import importlib.util
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True

texte_final, module_src, tests_src, traitement, jouet = map(Path, sys.argv[1:6])
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.prereg import problemes, sceller_prereg  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def git(*a):
    r = subprocess.run(["git", "-C", str(jouet), *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


if jouet.exists():
    shutil.rmtree(jouet)
jouet.mkdir(parents=True)
git("init", "-q", "-b", "main")
git("config", "user.email", "verif@example.invalid")
git("config", "user.name", "verif")
(jouet / "README").write_text("x\n")
git("add", "-A")
git("commit", "-q", "-m", "c0")
c0 = git("rev-parse", "HEAD")

CHEMIN_MODULE = "docs/procedures/P3-addendum-v1/complements_p3_v1.py"
CHEMIN_TESTS = "docs/procedures/P3-addendum-v1/test_complements_p3_v1.py"
PREREG = "prereg/P3-addendum-lecture-complementaire-v1.md"
mod, tst, pre = jouet / CHEMIN_MODULE, jouet / CHEMIN_TESTS, jouet / PREREG
mod.parent.mkdir(parents=True)
pre.parent.mkdir(parents=True)
shutil.copyfile(module_src, mod)
shutil.copyfile(tests_src, tst)
brut = texte_final.read_text(encoding="utf-8")


def remplir(sm, st, n="165"):
    t = brut.replace("`7a54d431d89745839220f882b41b13e8c62ecfdd`", f"`{c0}`")
    t = t.replace("<<EMPREINTE_MODULE>>", sm).replace("<<EMPREINTE_TESTS>>", st).replace("<<NOMBRE_TESTS>>", n)
    t = t.replace("<<EMPREINTE_TRAITEMENT>>", sha(traitement))
    for k, v in (("TEXTE", "a"), ("MUTANTS", "b"), ("CALCULS", "c")):
        t = t.replace(f"<<EMPREINTE_VERIFICATION_{k}>>", v * 64).replace(f"<<VERDICT_VERIFICATION_{k}>>", "scellable")
    return t


def ecrire_et_sceller(t, conforme=True):
    for x in (pre, Path(str(pre) + ".sha256")):
        if x.exists():
            x.unlink()
    pre.write_text(t, encoding="utf-8")
    return sceller_prereg(pre) if conforme else sceller(pre)


def charger(chemin, nom):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def essai(nom, f, attendu=None):
    try:
        r = f()
    except GardeArret as e:
        ok = attendu is not None and attendu in str(e)
        print(f"[{'CONFORME' if ok else 'ÉCART'}] {nom} : GardeArret « {e} »")
        return ok
    ok = attendu is None
    print(f"[{'CONFORME' if ok else 'ÉCART'}] {nom} : passe ({r})")
    return ok


print(f"texte final : {texte_final} sha256 {sha(texte_final)}")
print(f"module {sha(module_src)} ; tests {sha(tests_src)} ; commit jouet {c0}")
sm, st = sha(mod), sha(tst)
t_ok = remplir(sm, st)
print("marqueurs restants dans la copie remplie :", sorted(set(re.findall(r"<<[A-Z0-9_]+>>", t_ok))))
print("lignes lues par le module dans la copie remplie :")
m = charger(mod, "complements_jouet")
print("  module :", m.EMPREINTE_MODULE_CITEE.search(t_ok).group(0))
print("  tests  :", m.EMPREINTE_TESTS_CITEE.search(t_ok).group(0))
ecrire_et_sceller(t_ok)
print("problèmes de conformité R1/R2 du texte rempli et scellé (prereg.problemes) :", problemes(pre))
git("add", "-A")
git("commit", "-q", "-m", "c1")
R = jouet
resultats = []
# cas sain : le vrai texte rempli, le module chargé depuis son chemin versé
resultats.append(essai("sain : texte final rempli, module et tests versés",
                       lambda: {k: v[:12] for k, v in m.exiger_garde_1(R, PREREG, m.ENTROPIE_P3).items()}))
# artefact 1 : un octet ajouté au module après le scellement du texte
b = mod.read_bytes()
mod.write_bytes(b + b"\n# octet ajoute\n")
resultats.append(essai("artefact : module modifié", lambda: m.exiger_garde_1(R, PREREG, m.ENTROPIE_P3),
                       "garde 1 : module d'empreinte"))
mod.write_bytes(b)
# artefact 2 : tests modifiés
bt = tst.read_bytes()
tst.write_bytes(bt + b"\n# octet ajoute\n")
resultats.append(essai("artefact : tests modifiés", lambda: m.exiger_garde_1(R, PREREG, m.ENTROPIE_P3),
                       "garde 1 : tests d'empreinte"))
# artefact 3 : tests absents
tst.unlink()
resultats.append(essai("artefact : tests absents", lambda: m.exiger_garde_1(R, PREREG, m.ENTROPIE_P3),
                       "garde 1 : tests du module absents"))
tst.write_bytes(bt)
# artefact 4 : empreintes du module et des tests échangées dans le texte (rescellé)
ecrire_et_sceller(remplir(st, sm))
resultats.append(essai("artefact : empreintes échangées dans le texte", lambda: m.exiger_garde_1(R, PREREG, m.ENTROPIE_P3),
                       "garde 1 : module d'empreinte"))
# artefact 5 : empreinte du module citée en majuscules (hors de la forme lue)
ecrire_et_sceller(remplir(sm.upper(), st))
resultats.append(essai("artefact : empreinte hors de forme (majuscules)",
                       lambda: m.exiger_garde_1(R, PREREG, m.ENTROPIE_P3), "ne cite pas les empreintes"))
# artefact 6 : marqueurs laissés : scellement conforme refusé ; scellé de force, la garde 1 arrête
t_brut = brut.replace("`7a54d431d89745839220f882b41b13e8c62ecfdd`", f"`{c0}`")
resultats.append(essai("artefact : marqueurs laissés, sceller_prereg", lambda: ecrire_et_sceller(t_brut),
                       "marqueurs de gabarit restants"))
ecrire_et_sceller(t_brut, conforme=False)
resultats.append(essai("artefact : marqueurs laissés, scellé hors conformité, garde 1",
                       lambda: m.exiger_garde_1(R, PREREG, m.ENTROPIE_P3), "marqueurs de gabarit restants"))
# artefact 7 : module exécuté depuis un autre chemin (copie hors du chemin versé), texte sain
ecrire_et_sceller(t_ok)
ailleurs = jouet / "ailleurs" / "complements_p3_v1.py"
ailleurs.parent.mkdir()
shutil.copyfile(mod, ailleurs)
m2 = charger(ailleurs, "complements_ailleurs")
resultats.append(essai("artefact : module exécuté hors de son chemin versé",
                       lambda: m2.exiger_garde_1(R, PREREG, m2.ENTROPIE_P3), "garde 15 : module exécuté hors"))
shutil.rmtree(ailleurs.parent)
# retour au sain
resultats.append(essai("sain (retour) : texte final rescellé", lambda: {k: v[:12] for k, v in
                                                                         m.exiger_garde_1(R, PREREG, m.ENTROPIE_P3).items()}))
print(f"bilan : {sum(resultats)} conformes sur {len(resultats)}")
sys.exit(0 if all(resultats) else 1)
