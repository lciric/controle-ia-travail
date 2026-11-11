"""Mutations du harnais Lean v3 sur des copies (CLC2-08 de la contre-lecture courte `1fea30ab…`, R-2302).

Même méthode que la v2 (`mutations_harnais_v2.py`) : copie neuve par mutation, remplacement exact présent une seule fois (sinon
arrêt), **import tracé** vers la copie, `pytest -o pythonpath=<copie>/src <copie>/tests` sans `PYTHONPATH` hérité, délai de
180 s. Au moins une mutation par correction de la v3, et une par ligne survivante de CLC2-08 (n02, n04, n09, n10, n12, n15,
n17, n20, n21).

Usage : python -I -B mutations_harnais_v3.py RACINE_DE_L_ARBRE DOSSIER_DE_TRAVAIL ; code 0 si toutes les mutations sont tuées.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ESSAIS = ["tests/test_lean_essai_gardes_v3.py", "tests/test_lean_essai_executeur_v3.py",
          "tests/test_lean_essai_minuterie_v3.py"]
G, X, M, H3, H2 = "gardes_lean_v3", "executeur_bac_v3", "minuterie_v3", "hetzner_v3", "hetzner_v2"

MUTATIONS = [
    # CLC2-01 : lexique
    ("l01", "CLC2-01", G, 'if prec not in ("debut", "blanc", "ident", "ouvrant"):\n                raise ErreurLexicale(f"début de commentaire',
     'if False:\n                raise ErreurLexicale(f"début de commentaire'),
    ("l02", "CLC2-01", G, 'if prec not in ("debut", "blanc", "ouvrant"):\n                raise ErreurLexicale(f"chaîne collée au lexème',
     'if False:\n                raise ErreurLexicale(f"chaîne collée au lexème'),
    ("l03", "CLC2-01", G, 'if prec not in ("debut", "blanc", "ouvrant"):\n                raise ErreurLexicale(f"caractère collé',
     'if False:\n                raise ErreurLexicale(f"caractère collé'),
    ("l04", "CLC2-01", G, 'return (("a" <= c <= "z") or ("A" <= c <= "Z") or', "return (c.isalpha() or"),
    ("l05", "CLC2-08 n02", G, 'if c in "«»":\n            raise', "if False:\n            raise"),
    ("l06", "CLC2-01", G, "if j < n and (_suite_ident(source[j]) or source[j] in \"\\\"'«»\"):", "if False:"),
    # CLC2-02 : mots de G-L3+ (seconde ligne)
    ("t01", "CLC2-02", G, " + _occurrences(_RE_TYPES_META, masque)", ""),
    ("t02", "CLC2-02", G, 'motifs["G-L3+"] += [f"règle de tactique d\'Aesop', 'motifs["G-L3+"] += [] and [f"règle de tactique d\'Aesop'),
    ("t03", "CLC2-02", G, '"simproc", "dsimproc", "simproc_decl", "dsimproc_decl", ', ""),
    ("n09", "CLC2-08 n09", G, '_RE_DEBUG = re.compile(r"set_option\\s+debug\\.|skipKernelTC")', '_RE_DEBUG = re.compile(r"set_option debug\\.")'),
    ("n10", "CLC2-08 n10", G, 'if module.split(".")[0] not in IMPORTS_PERMIS:', "if False:"),
    # garde de fond
    ("g01", "fond : rejeu", G, 'elif not v["rejeu_ok"]:', "elif False:"),
    ("g02", "fond : imports", G, 'if not v["permis"]:', "if False:"),
    ("g03", "fond : axiomes", G, "hors = [x for x in axiomes if x not in AXIOMES_PERMIS]", "hors = []"),
    ("g04", "fond : genre", G, 'if a.get("genre") != "theoreme":', "if False:"),
    ("g05", "fond : aller-retour", G, 'if a.get("aller_retour") is not True:', "if False:"),
    ("g06", "fond : sûreté", G, 'if surete != "sure":', "if False:"),
    ("g07", "fond : impressions", G, 'if genre != "theoreme" and v["rejeu_ok"] and nom not in v["definitions"]:', "if False:"),
    ("g08", "fond : code", G, 'if verification.get("code") != 0:', "if False:"),
    ("g09", "fond : anomalies", G, 'motifs["G-L7"] += [f"noyau : {a}" for a in v["anomalies"]]', 'motifs["G-L7"] += []'),
    ("g10", "fond : nonce", G, 'elif fins[0].get("nonce") != nonce:', "elif False:"),
    ("g11", "fond : fin en dernier", G, 'if len(fins) != 1 or not objets or objets[-1].get("type") != "fin":', "if len(fins) != 1:"),
    ("g12", "CLC2-08 n04", G, 'anomalies.append(f"nom attendu {nom!r} sans ligne")', "pass"),
    ("g13", "fond : inventaire", G, "if f not in FICHIERS_ITEM]", "if False]"),
    ("g14", "fond : lignes non JSON", G, 'anomalies.append(f"ligne non JSON : {ligne[:120]!r}")', "pass"),
    ("g15", "fond : doublons", G, 'anomalies.append(f"nom attendu {nom!r} rapporté deux fois")', "pass"),
    # exécuteur
    ("x01", "CLC2-05", X, "        self.lanceur.temoin_montage(l, unite)\n", ""),
    ("x02", "fond : épinglage", X, "if not self.cfg.verificateur_sha256 or _sha256(self.cfg.verificateur) != self.cfg.verificateur_sha256:",
     "if False:"),
    ("x03", "fond : item en lecture seule", X, 'liaisons={"/item": (str(d_item), False),', 'liaisons={"/item": (str(d_item), True),'),
    ("x04", "fond : LEAN_PATH sans l'item", X, 'env=self._env(), sortie=d_sorties / "noyau.out"',
     'env=dict(self._env(), LEAN_PATH=self.cfg.lean_path + ":/item"), sortie=d_sorties / "noyau.out"'),
    ("x05", "CLC2-08 n20", X, '"-p", "IPAddressDeny=any",', ""),
    ("x06", "CLC2-08 n21", X, 'bw = ["bwrap", "--unshare-all",', 'bw = ["bwrap",'),
    ("x07", "note 3 : tampon périmé", X, 'and maintenant() - float(d.get("epoque", 0)) <= cfg.tampon_age_max_s):', "):"),
    ("x08", "CLL-15", X, 'if resultat == "timeout":\n        return "délai"', 'if resultat == "timeout":\n        return None'),
    # Hetzner
    ("h01", "CLC2-03", H3, "return all(i != int(ident) for i, _ in self.inventaire())", "return True"),
    ("h02", "CLC2-03", H3, "except (OSError, http.client.HTTPException, ValueError) as e:   # ValueError",
     "except (OSError, http.client.HTTPException) as e:   # ValueError"),
    ("h03", "CLC2-04", H3, "**{ETIQUETTE_CREATION: jeton}),", "),"),
    ("h04", "note 6", H3, 'if prix.get("devise") != "EUR":', "if False:"),
    ("h05", "note 6", H3, 'if d.get("meta", {}).get("pagination", {}).get("next_page"):', "if False:"),
    ("h06", "CLC2-06", H3, 'if [(f.get("id"), f.get("status")) for f in portes] != [(pare_feu, "applied")]:',
     'if pare_feu not in [f.get("id") for f in portes]:'),
    ("h07", "CLC2-08 n17", H2, 'if x.get("type") == "ipv4"', "if True"),
    # minuterie
    ("m01", "CLC2-03", M, "        except Exception as e:  # noqa: BLE001 — journalisée, retentée",
     "        except OSError as e:  # noqa: BLE001 — journalisée, retentée"),
    ("m02", "CLC2-03", M, '_ecrire(journal, {"destruction": "refusée", "identifiant": ident, "motif": str(e)[:200]})', "pass"),
    ("m03", "CLC2-08 n12", M, "return min(5.0 * 2 ** (n - 1), pause_max_s)", "return 5.0 * 2 ** (n - 1)"),
    ("m04", "CLC2-08 n15", M, "        except Exception as e:  # noqa: BLE001 — la minuterie ne meurt pas d'une lecture",
     "        except OSError as e:  # noqa: BLE001 — la minuterie ne meurt pas d'une lecture"),
    ("m05", "CLC2-04", M, "    _ajouter_journal_creations(journal_creations, entree)   # intention écrite AVANT l'appel\n", ""),
    ("m06", "CLC2-04", M, "detruits = rattraper_par_etiquette(client, jeton, journal, dormir, essais_max)", "detruits = []"),
    ("m07", "CLC2-07", M, "mot = verifier_mot_de_lazar(mot_de_lazar, chemin_go, dossier_decisions, jour)", "mot = mot_de_lazar"),
    ("m08", "CLC2-07", M, '"retenu": max(registre, declare or 0.0, journal)}', '"retenu": max(registre, declare or 0.0)}'),
    ("m09", "CLC2-07", M, 'if brut.count(",") + brut.count(".") > 1:', "if False:"),
    ("m10", "CLC2-07", M, 'if brut.startswith("-"):', "if False:"),
    ("m11", "CLC2-07", M, 'if anterieures:\n        if not mot_de_lazar:', 'if False:\n        if not mot_de_lazar:'),
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
    shutil.copytree(racine / "scripts" / "lean_essai_d1a_v3" / "artefacts_r5_v3",
                    dest / "scripts" / "lean_essai_d1a_v3" / "artefacts_r5_v3")


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
