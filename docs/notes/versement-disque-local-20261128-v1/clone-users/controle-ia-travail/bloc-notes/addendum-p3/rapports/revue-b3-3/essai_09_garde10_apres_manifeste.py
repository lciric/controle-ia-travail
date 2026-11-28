"""Essai 09 : ordre des gardes dans `executer`. La garde 10 (famille « attention » discordante avec `agregation`) n'est
passée que dans `analyser_addendum`, donc après la création du manifeste. Dépôt jouet construit comme le gabarit des
tests (aides du fichier de tests, sans copie), avec une seule différence : `agregation` de la sonde à attention écrite
« max » dans sondes-figees.json. Attendu à lire : où l'arrêt tombe, ce qui est écrit, et si un second passage reste
possible une fois la donnée corrigée (garde 9)."""
import json
import shutil
import tempfile
from pathlib import Path

import pytest

import commun  # noqa: F401
from commun import ICI, cp, tc

from controle_ia.premier_test_ia import lecture as lp
from controle_ia.scellement import empreinte

P = tc.P
base = Path(tempfile.mkdtemp(prefix="essai09-", dir=ICI))
try:
    d = base / "depot"
    d.mkdir()
    tc.git(d, "init", "-q", "-b", "main")
    tc.git(d, "config", "user.email", "test@example.invalid")
    tc.git(d, "config", "user.name", "test")
    shutil.copytree(tc.DEPOT / "src" / "controle_ia", d / "src" / "controle_ia",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (d / "README").write_text("x\n")
    tc.committer(d)
    c0 = tc._rev(d)
    import hashlib

    from controle_ia.manifeste import config_canonique
    sha_config = hashlib.sha256(config_canonique(tc.CONFIG_SOURCE)).hexdigest()
    tc._prereg_conforme(d / cp.PREREG_P3, [f"- Commit du code d'analyse : `{c0}`", f"- Entropie : `{cp.ENTROPIE_P3}`",
                                           f"- Configuration de P3 (empreinte canonique) : `{sha_config}`"])
    module, tests = d / cp.CHEMIN_MODULE, d / cp.CHEMIN_TESTS
    module.parent.mkdir(parents=True)
    module.write_bytes(Path(cp.__file__).read_bytes())
    tests.write_bytes(Path(tc.__file__).read_bytes())
    tc._prereg_conforme(d / cp.PREREG_ADDENDUM, [f"- Commit du code d'analyse : `{c0}`", f"- Entropie : `{cp.ENTROPIE_P3}`",
                                                 f"- Module de l'addendum (sha256) : `{empreinte(module)}`",
                                                 f"- Tests du module (sha256) : `{empreinte(tests)}` ; nombre de tests "
                                                 f"attendu : `1`"])
    tc.committer(d)
    src = tc._complet(tc._varier(tc._source(0, n_taches=12)))
    for s in src["sondes-figees"]["sondes"]:
        if s["nom"] == P[1]:
            s["agregation"] = "max"                     # seule différence : discordance avec les logits gardés
    tc._ecrire_run_source(d, tc.RUN_A, src)
    tc.committer(d)
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(lp, "TIRAGES_AIRE", 300)
        mp.setattr(lp, "TIRAGES_COUT", 2000)
        mp.setattr(lp, "exiger_code_importe_sous", lambda racine: None)
        lp.analyser(d, tc.RUN_A, tc.LEC_A, cp.PREREG_P3, cp.ENTROPIE_P3, autoriser_depot_sale=True)
    tc.committer(d)
    m = tc._charger_copie(d / cp.CHEMIN_MODULE, "complements_copie_essai09")
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(lp, "exiger_code_importe_sous", lambda racine: None)
        mp.setattr(m, "TIRAGES_AIRE", 200)
        mp.setattr(m, "TIRAGES_COUT", 2000)
        for run_add in ("20261020-150000-addendum-p3", "20261020-150001-addendum-p3"):
            try:
                m.executer(d, tc.RUN_A, tc.LEC_A, run_add, cp.PREREG_ADDENDUM, cp.ENTROPIE_P3)
                print(f"{run_add} : passage réussi")
            except Exception as e:  # noqa: BLE001
                ecrit = sorted(str(p.relative_to(d)) for p in (d / "diag" / run_add).glob("*")) if (
                    d / "diag" / run_add).exists() else []
                manif = (d / "runs" / run_add / "manifeste.json").exists()
                arret = (json.loads((d / "diag" / run_add / "lecture-addendum-p3.json").read_text())["resultat"]["arret"]
                         if ecrit else None)
                print(f"{run_add} : {type(e).__name__} : {str(e)[:150]} ; manifeste créé : {manif} ; écrit : {ecrit} ; "
                      f"arret : {arret and arret[:120]}")
            tc.committer(d)
finally:
    shutil.rmtree(base)
