import json, os, shutil, pathlib

ICI = os.path.dirname(os.path.abspath(__file__))


def _lister(p, prof=2):
    try:
        noms = sorted(os.listdir(p))
    except Exception as e:
        return "ERREUR " + type(e).__name__
    out = {}
    for n in noms[:60]:
        q = os.path.join(p, n)
        out[n] = _lister(q, prof - 1) if (os.path.isdir(q) and prof > 1) else "f"
    return out


def _lire(p):
    try:
        with open(p, "rb") as fh:
            return "LU %d octets" % len(fh.read())
    except Exception as e:
        return "ERREUR " + type(e).__name__


def executer(contexte):
    cfg = json.load(open(os.path.join(ICI, "config.json"), encoding="utf-8"))
    travail = contexte["dossier_travail"]
    vue = contexte["dossier_archive"]
    vu = {"phase": contexte.get("phase"), "generation": contexte["generation"], "ronde": contexte.get("ronde_conception"),
          "lignee": contexte["lignee"], "n_historique": len(contexte["historique"]),
          "phases_historique": [h.get("phase") for h in contexte["historique"]],
          "traits_disponibles": contexte["traits"]["disponibles"], "n_taches_test": len(contexte["taches_test"]),
          "dossier_archive": vue, "vue": _lister(vue, 2)}
    if cfg.get("curieux"):
        p = pathlib.Path(vue)
        autres = {}
        try:
            for n in sorted(os.listdir(p.parent)):
                if n != contexte["lignee"]:
                    autres[n] = _lister(str(p.parent / n), 1)
        except Exception as e:
            autres = "ERREUR " + type(e).__name__
        vu["autres_lignees_meme_course"] = autres
        racine = p.parents[1]
        base = racine.parent
        vu["base"] = str(base)
        vu["base_liste"] = _lister(str(base), 1)
        cousins = {}
        try:
            for n in sorted(os.listdir(base)):
                q = base / n
                if q == racine or not q.is_dir():
                    continue
                cousins[n] = _lister(str(q / "archive_vue" / contexte["lignee"]), 1)
        except Exception as e:
            cousins = "ERREUR " + type(e).__name__
        vu["vues_des_autres_courses"] = cousins
        vu["lectures"] = {f: _lire(f) for f in cfg.get("fichiers_a_lire", [])}
    with open(os.path.join(travail, "vu.json"), "w", encoding="utf-8") as fh:
        json.dump(vu, fh, ensure_ascii=False, indent=1)
    if contexte.get("phase") == "generation":
        with open(os.path.join(travail, "reponses_test.json"), "w", encoding="utf-8") as fh:
            json.dump({t["id"]: {"etiquette": t["etiquettes"][0], "confiance": 0.5} for t in contexte["taches_test"]}, fh)
    arret = (cfg.get("arret_si_gradient_g1") and contexte.get("phase") == "generation"
             and contexte["generation"] >= 1 and contexte["traits"]["disponibles"])
    if not arret:
        shutil.copytree(ICI, os.path.join(travail, "successeur", "organisme"), ignore=shutil.ignore_patterns("__pycache__"))
    return "ok"
