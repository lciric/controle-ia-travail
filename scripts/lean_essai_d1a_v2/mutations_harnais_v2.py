"""Mutations du harnais Lean v2 sur des copies (CLL-14 de la contre-lecture `2077ae26…`, R-2300).

Pour chaque mutation : copie neuve de `src/controle_ia/{__init__,gardes}.py`, `src/controle_ia/lean_essai/`, `tests/conftest.py`,
des essais v2, de `pyproject.toml` et des artefacts v2 dans un dossier de travail ; remplacement exact (présent une seule fois,
sinon la mutation est déclarée inapplicable et le script échoue) ; **import tracé** (le module muté importé doit venir de la
copie) ; `pytest -o pythonpath=<copie>/src <copie>/tests` lancé dans la copie, sans `PYTHONPATH` hérité, délai de 180 s (une
boucle sans fin est arrêtée par délai, sur le PID de l'enfant). Tuée = au moins un essai échoue.

Usage : python -I -B mutations_harnais_v2.py RACINE_DE_L_ARBRE DOSSIER_DE_TRAVAIL ; code 0 si toutes les mutations sont tuées.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ESSAIS = ["tests/test_lean_essai_gardes_v2.py", "tests/test_lean_essai_executeur_v2.py",
          "tests/test_lean_essai_budget_go_v2.py", "tests/test_lean_essai_minuterie_v2.py"]
G, X, M, H1, H2, B, GO, S = ("gardes_lean_v2", "executeur_bac_v2", "minuterie_v2", "hetzner_v1", "hetzner_v2", "budget_v2",
                             "garde_go_v2", "sortie_v2")

# (identifiant, défaut visé, module, ancien, nouveau)
MUTATIONS = [
    ("m01", "CLL-01", G, 'if c in "«»":\n            raise', 'if False:\n            raise'),
    ("m02", "CLL-01", G, "if j < n and (_suite_ident(source[j]) or source[j] in \"\\\"'«»\"):", "if False:"),
    ("m03", "CLL-01", G, "if j < n and source[j] == '\"':\n                raise ErreurLexicale(f\"chaîne collée",
     "if False:\n                raise ErreurLexicale(f\"chaîne collée"),
    ("m04", "CLL-01", G, "if j < n and source[j] in \"\\\"'\":\n                raise ErreurLexicale(f\"littéral collé à un nombre",
     "if False:\n                raise ErreurLexicale(f\"littéral collé à un nombre"),
    ("m05", "CLL-02", G, 'if genres.get(nom) != "theoreme":', "if False:"),
    ("m06", "CLL-02", G, 'if surete != "sure":', "if False:"),
    ("m07", "CLL-03", G, "AUXILIAIRES.match(nom[len(r) + 1:])", "True"),
    ("m08", "CLL-03", G, 'inductifs = {n for n in imprimees if genres.get(n) == "inductif"}',
     "inductifs = set(imprimees) | set(attendus)"),
    ("m09", "CLL-04", G, 'if controle.get("code") != 0:', "if False:"),
    ("m10", "CLL-04", G, 'anomalies = [f"ligne brute hors JSON : {b[:120]!r}" for b in brut]', "anomalies = []"),
    ("m11", "CLL-04", G, 'if lignes and lignes[-1] == f"{MARQUEUR_FIN} {nonce}":',
     "if lignes and lignes[-1].startswith(MARQUEUR_FIN):"),
    ("m12", "CLL-04", G, "if len(infos) > 1:", "if False:"),
    ("m13", "CLL-04", X, 'entree=texte), f"bac-{item}-controle")', 'entree=None), f"bac-{item}-controle")'),
    ("m14", "CLL-04", G, 'if genre != "constantes" and (MARQUEUR_CONSTANTE in data or MARQUEUR_FIN in data):', "if False:"),
    ("m15", "CLL-05", M, "        except (ErreurHetzner, OSError) as e:\n            _ecrire(journal, {\"destruction\": \"échec\"",
     "        except () as e:\n            _ecrire(journal, {\"destruction\": \"échec\""),
    ("m16", "CLL-05", H2, "except (OSError, http.client.HTTPException, json.JSONDecodeError) as e:\n        raise ErreurHetzner(f\"échange",
     "except ZeroDivisionError as e:\n        raise ErreurHetzner(f\"échange"),
    ("m17", "CLL-06", M, "if anterieures and not mot_de_lazar:", "if False:"),
    ("m18", "CLL-06", M, '    verifier_devis(prix_usd, pas, deja["retenu"])\n', "    pass\n"),
    ("m19", "CLL-06", M, "reste = PLAFONDS_MACHINE[pas] - deja_depense_usd", "reste = PLAFONDS_MACHINE[pas] - 0.0"),
    ("m20", "CLL-06", M, "    except Exception:\n        detruire_par_identifiant(client, ident, NOM_MACHINE, journal, dormir, essais_max=essais_max)\n        raise",
     "    except Exception:\n        raise"),
    ("m21", "CLL-07 (survivante 6)", X, "pids = [int(x) for x in procs.read_text().split()]", "pids = []"),
    ("m22", "CLL-09", G, "if nom not in ATTRIBUTS_PERMIS:", "if False:"),
    ("m23", "CLL-09", G, "_RE_DERIVING.finditer(masque)]", '_RE_DERIVING.finditer("")]'),
    ("m24", "CLL-09", G, 'if not lu["enonces_bruts"].get(nom):', "if False:"),
    ("m25", "CLL-11", GO, "if go_id != go_pilote:", "if False:"),
    ("m26", "CLL-12", B, "with self.verrou:\n            if ident in self.en_vol:", "if True:\n            if ident in self.en_vol:"),
    ("m27", "CLL-13", X, 'self.reseau = exiger_reseau_ferme(cfg, relever, id_demarrage=id_demarrage) if cfg.mode == "bac" else None',
     "self.reseau = None"),
    ("m28", "CLL-13", X, 'if ecarts:\n        raise ErreurBac(f"réseau sortant non éprouvé fermé',
     'if False:\n        raise ErreurBac(f"réseau sortant non éprouvé fermé'),
    ("m29", "CLL-13", H2, "if not appliques:", "if False:"),
    ("m30", "CLL-15", X, 'if any(x.startswith("bwrap:") for x in texte_erreurs.splitlines()):', "if False:"),
    ("m31", "CLL-15", X, 'if resultat is None:\n        raise ErreurBac(f"systemd-run sans résultat',
     'if False:\n        raise ErreurBac(f"systemd-run sans résultat'),
    ("m32", "CLL-15", X, 'if resultat == "oom-kill":\n        return "mémoire"', 'if resultat == "oom-kill":\n        return None'),
    ("m33", "CLL-15", S, 'if incident_bac == "mémoire":\n        return _non("mémoire")',
     'if incident_bac == "mémoire":\n        return None'),
    ("m34", "CLL-08", G, 'lignes = [f"import {module}", "import Lean", ""]', 'lignes = [f"import {module}", ""]'),
    ("m35", "CLL-10", G, "(_root_.Lean.Name.toString n)", "(toString n)"),
    ("s1", "CLL-14 survivante 1", G, 'if not lu["enonces"].get(nom):', "if False:"),
    ("s2", "CLL-14 survivante 2", G, 'motifs["G-L7"] += [f"erreur du contrôle : {e}" for e in lu["erreurs"]',
     'motifs["G-L7"] += [] and [f"erreur du contrôle : {e}" for e in lu["erreurs"]'),
    ("s3", "CLL-14 survivante 3", X, 'liaisons={"/item": (str(d_item), False)}, chdir="/tmp",',
     'liaisons={"/item": (str(d_item), True)}, chdir="/tmp",'),
    ("s4", "CLL-14 survivante 5", G, 'if compilation.get("sortie_tronquee"):', "if False:"),
    ("s4b", "CLL-14 survivante 5", X, '"sortie_tronquee": tronq_c}', '"sortie_tronquee": False}'),
    ("s5", "CLL-14 survivante 4", G, 'if controle.get("sortie_tronquee"):', "if False:"),
    ("s5b", "CLL-14 survivante 4", X, '"nonce": nonce, "sortie_tronquee": tronq_k}', '"nonce": nonce, "sortie_tronquee": False}'),
    ("s7", "CLL-14 survivante 7", H1, '"public_net": {"enable_ipv4": True, "enable_ipv6": False}',
     '"public_net": {"enable_ipv4": True, "enable_ipv6": True}'),
    ("s8", "CLL-14 survivante 8", M, "if echeance > ECHEANCES_H[a.pas]:\n                raise",
     "if False:\n                raise"),
    ("s9", "CLL-14 survivante 9", M, "            verifier_devis(prix_usd, a.pas, a.deja_depense_usd)\n", "            pass\n"),
]


def copier(racine: Path, dest: Path) -> None:
    (dest / "src" / "controle_ia").mkdir(parents=True)
    for f in ("__init__.py", "gardes.py"):
        shutil.copy2(racine / "src" / "controle_ia" / f, dest / "src" / "controle_ia" / f)
    shutil.copytree(racine / "src" / "controle_ia" / "lean_essai", dest / "src" / "controle_ia" / "lean_essai",
                    ignore=shutil.ignore_patterns("__pycache__"))
    (dest / "tests").mkdir()
    for f in ["tests/conftest.py"] + ESSAIS:
        shutil.copy2(racine / f, dest / f)
    shutil.copy2(racine / "pyproject.toml", dest / "pyproject.toml")
    shutil.copytree(racine / "scripts" / "lean_essai_d1a_v2" / "artefacts_r5_v2",
                    dest / "scripts" / "lean_essai_d1a_v2" / "artefacts_r5_v2")


def env_propre() -> dict:
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP")}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env


def tracer_import(copie: Path, module: str) -> str:
    code = ("import sys; sys.path[:0] = [sys.argv[1] + '/src', sys.argv[1] + '/tests']; "
            f"import controle_ia.lean_essai.{module} as m; print(m.__file__)")
    p = subprocess.run([sys.executable, "-I", "-B", "-c", code, str(copie)], capture_output=True, text=True,
                       env=env_propre(), cwd=copie)
    chemin = p.stdout.strip()
    if p.returncode != 0 or not chemin.startswith(str(copie)):
        raise SystemExit(f"import non tracé vers la copie : {chemin!r} {p.stderr[-300:]}")
    return chemin


def lancer_essais(copie: Path) -> tuple[int, str]:
    cmd = [sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-c", str(copie / "pyproject.toml"),
           "--rootdir", str(copie), "-o", f"pythonpath={copie / 'src'} {copie / 'tests'}"] + [str(copie / e) for e in ESSAIS]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=env_propre(), cwd=copie, timeout=180)
    except subprocess.TimeoutExpired:
        return -9, "délai dépassé (boucle sans fin) : enfant arrêté par son PID"
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    return p.returncode, (lignes[-1] if lignes else p.stderr[-200:])


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    racine, travail = Path(argv[0]).resolve(), Path(argv[1]).resolve()
    travail.mkdir(parents=True, exist_ok=True)
    temoin = travail / "temoin"
    shutil.rmtree(temoin, ignore_errors=True)
    copier(racine, temoin)
    tracer_import(temoin, G)
    code, ligne = lancer_essais(temoin)
    resultats = [{"id": "témoin", "defaut": "aucune mutation", "code": code, "fin": ligne, "tuee": None}]
    if code != 0:
        print(json.dumps(resultats, ensure_ascii=False, indent=1))
        raise SystemExit("la copie témoin ne passe pas : mutations sans objet")
    for ident, defaut, module, ancien, nouveau in MUTATIONS:
        copie = travail / ident
        shutil.rmtree(copie, ignore_errors=True)
        copier(racine, copie)
        fichier = copie / "src" / "controle_ia" / "lean_essai" / f"{module}.py"
        texte = fichier.read_text(encoding="utf-8")
        if texte.count(ancien) != 1:
            raise SystemExit(f"{ident} inapplicable : {texte.count(ancien)} occurrence(s) dans {module}.py")
        fichier.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        trace = tracer_import(copie, module)
        code, ligne = lancer_essais(copie)
        resultats.append({"id": ident, "defaut": defaut, "module": module, "import": trace.replace(str(travail), "<travail>"),
                          "code": code, "fin": ligne, "tuee": code != 0})
        shutil.rmtree(copie)
    shutil.rmtree(temoin)
    survivantes = [r["id"] for r in resultats if r["tuee"] is False]
    print(json.dumps({"mutations": len(MUTATIONS), "tuees": len(MUTATIONS) - len(survivantes), "survivantes": survivantes,
                      "detail": resultats}, ensure_ascii=False, indent=1))
    return 0 if not survivantes else 1


if __name__ == "__main__":
    sys.exit(main())
