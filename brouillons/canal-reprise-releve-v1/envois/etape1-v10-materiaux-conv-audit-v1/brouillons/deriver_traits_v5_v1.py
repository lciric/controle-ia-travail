"""BROUILLON (non exécuté sur les vrais traits) — dossier de traits dérivé pour la banque `confrontation-v5`, sans
réextraction. Écrit le 26 octobre 2026 par un sous-agent de conv-audit pour l'étape 1 v10 ; à reprendre par la lignée
qui a le droit d'ouvrir `donnees/traits-etape1-v1` (session-depot), sous un nom versionné, puis contre-lu.

Fondement (rapport `/var/tmp/etape1-v10-v1/LISEZMOI-v1.md`, point 2) : l'extraction (`extraire_activations_v2.py`,
`8286f4e7…`, l. 68 et 153) n'a donné au modèle que GABARIT_SYSTEME et `t["texte"]`, une tâche à la fois (lot de 1,
aucun état partagé) ; les 176 textes de la v5 sont, à l'octet près, des textes de la v1 (aucun doublon dans la v1).
Le trait d'une tâche v5 est donc celui de la tâche v1 de même texte.

Règle : pour chaque vue `traits-<vue>.npz` du dossier source (manifeste à l'empreinte `f1387a20…`), on associe chaque
tâche v5 à la tâche v1 de même empreinte de texte (UTF-8, sha256) — sans le fichier secret de la v5 ; on écrit les
176 vecteurs **rangés par identifiant v5** (l'ordre v1 était rangé par vérité), avec `ids` = identifiants v5 seulement ;
manifeste neuf : `sha256_banque` = empreinte de la v5, `fichiers`, `forme`, `n_tronquees` recomptée sur les 176,
provenance (empreintes du manifeste et des fichiers source, de ce script, des deux banques) ; **aucun identifiant v1**
ni table de correspondance n'est écrit (ni `jetons_par_tache` ni `troncatures` hérités : ils sont rangés par
identifiant v1). Refus (aucun repli) : banque d'une autre empreinte, texte v5 introuvable ou ambigu dans la v1,
identifiant source absent, forme ou nombre non fini, sortie non vide.

Usage : python -I deriver_traits_v5_v1.py SOURCE_TRAITS_16384/ BANQUE_V1.json BANQUE_V5.json SORTIE/
        python -I deriver_traits_v5_v1.py --essai BANQUE_V1.json BANQUE_V5.json DOSSIER_TEMPORAIRE/
"""
import hashlib
import json
import pathlib
import sys

import numpy as np

E_V1 = "f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc"
E_V5 = "28e3c728d9d1251d50da18d61827b9f99578721f9988e19e3a3e19909e5c6e46"
PARTS = ("train", "test", "test_final")


def emp(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(p):
    p = pathlib.Path(p)
    p.with_name(p.name + ".sha256").write_text(f"{emp(p)}  {p.name}\n", encoding="utf-8")


def correspondance(b1, b5):
    """identifiant v5 -> identifiant v1, par l'empreinte du texte ; refus si absent ou ambigu."""
    par_texte = {}
    for t in (t for n in PARTS for t in b1[n]):
        h = hashlib.sha256(str(t["texte"]).encode("utf-8")).hexdigest()
        if h in par_texte:
            sys.exit("v1 : deux tâches de même texte : correspondance ambiguë, refus")
        par_texte[h] = str(t["id"])
    c = {}
    for t in (t for n in PARTS for t in b5[n]):
        h = hashlib.sha256(str(t["texte"]).encode("utf-8")).hexdigest()
        if h not in par_texte:
            sys.exit("v5 : un texte absent de la v1 : il faudrait l'extraire (nœud de dépense), refus")
        c[str(t["id"])] = par_texte[h]
    if len(set(c.values())) != len(c):
        sys.exit("deux tâches v5 pour une même tâche v1 : refus")
    return c


def deriver(source, banque_v1, banque_v5, sortie):
    source, sortie = pathlib.Path(source), pathlib.Path(sortie)
    if emp(banque_v1) != E_V1 or emp(banque_v5) != E_V5:
        sys.exit("banques : empreintes différentes de f1387a20… (v1) ou 28e3c728… (v5), refus")
    if sortie.exists() and any(sortie.iterdir()):
        sys.exit(f"{sortie} existe et n'est pas vide (R12), refus")
    fm = source / "manifeste-traits.json"
    if fm.with_name(fm.name + ".sha256").read_text(encoding="utf-8").split()[0] != emp(fm):
        sys.exit("manifeste source : compagnon différent, refus")
    ms = json.loads(fm.read_text(encoding="utf-8"))
    if ms.get("sha256_banque") != E_V1 or ms.get("factice"):
        sys.exit("manifeste source : banque autre que la v1, ou traits factices, refus")
    b1 = json.loads(pathlib.Path(banque_v1).read_text(encoding="utf-8"))
    b5 = json.loads(pathlib.Path(banque_v5).read_text(encoding="utf-8"))
    c = correspondance(b1, b5)
    ids5 = sorted(c)  # rangés par identifiant v5 (opaque)
    sortie.mkdir(parents=True, exist_ok=True)
    tronquees_v1 = set(ms.get("troncatures") or {})
    m = {k: ms.get(k) for k in ("modele", "revision", "type_nombre", "couches", "agregations", "max_jetons",
                                 "gabarit_systeme", "sha256_gabarit", "config_modele", "environnement")}
    m.update({"banque": "banque-confrontation-v5.json", "sha256_banque": E_V5, "n_taches": len(ids5), "factice": False,
              "n_tronquees": sum(c[i] in tronquees_v1 for i in ids5), "fichiers": {},
              "derivation": {"script": pathlib.Path(__file__).name, "sha256_script": emp(__file__),
                             "regle": "trait v5 = trait v1 de même empreinte de texte ; lignes rangées par identifiant v5",
                             "source_sha256_manifeste": emp(fm), "source_sha256_banque": E_V1, "source_fichiers": {}}})
    for nom, f in sorted((ms.get("fichiers") or {}).items()):
        fs = source / f"traits-{nom}.npz"
        if emp(fs) != f.get("sha256"):
            sys.exit(f"{fs.name} : empreinte différente du manifeste source, refus")
        d = np.load(fs, allow_pickle=False)
        rang = {str(i): k for k, i in enumerate(d["ids"])}
        manquants = [i for i in ids5 if c[i] not in rang]
        if manquants:
            sys.exit(f"{fs.name} : {len(manquants)} tâche(s) sans trait source, refus")
        X = np.stack([d["X"][rang[c[i]]] for i in ids5]).astype(np.float32)
        if not np.all(np.isfinite(X)):
            sys.exit(f"{fs.name} : nombre non fini, refus")
        fo = sortie / f"traits-{nom}.npz"
        np.savez(fo, ids=np.array(ids5), X=X)
        sceller(fo)
        m["fichiers"][nom] = {"chemin": fo.name, "sha256": emp(fo), "forme": list(X.shape)}
        m["derivation"]["source_fichiers"][nom] = emp(fs)
    mo = sortie / "manifeste-traits.json"
    mo.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(mo)
    texte = mo.read_text(encoding="utf-8")
    fuite = [i for i in c.values() if i in texte]
    if fuite:
        sys.exit("le manifeste dérivé contient un identifiant v1 : refus")
    return m


def essai(banque_v1, banque_v5, tmp):
    """Cas sain et deux artefacts, sur traits synthétiques (vecteur = empreinte du texte, reproductible)."""
    tmp = pathlib.Path(tmp)
    b1 = json.loads(pathlib.Path(banque_v1).read_text(encoding="utf-8"))
    b5 = json.loads(pathlib.Path(banque_v5).read_text(encoding="utf-8"))
    ids1 = [str(t["id"]) for n in PARTS for t in b1[n]]
    vec = lambda s: np.frombuffer(hashlib.sha256(s.encode("utf-8")).digest(), dtype=np.uint8).astype(np.float32)  # noqa: E731
    src = tmp / "source"
    src.mkdir(parents=True)
    X = np.stack([vec(str(t["texte"])) for n in PARTS for t in b1[n]])
    f = src / "traits-couche16-dernier.npz"
    np.savez(f, ids=np.array(ids1), X=X)
    sceller(f)
    ms = {"sha256_banque": E_V1, "factice": False, "troncatures": {},
          "fichiers": {"couche16-dernier": {"sha256": emp(f), "forme": list(X.shape)}}}
    (src / "manifeste-traits.json").write_text(json.dumps(ms), encoding="utf-8")
    sceller(src / "manifeste-traits.json")
    m = deriver(src, banque_v1, banque_v5, tmp / "sain")
    d = np.load(tmp / "sain" / "traits-couche16-dernier.npz")
    textes5 = {str(t["id"]): str(t["texte"]) for n in PARTS for t in b5[n]}
    assert list(d["ids"]) == sorted(textes5) and len(d["ids"]) == 176
    assert all(np.array_equal(d["X"][k], vec(textes5[i])) for k, i in enumerate(d["ids"]))
    assert m["sha256_banque"] == E_V5 and m["fichiers"]["couche16-dernier"]["forme"] == [176, 32]
    print("essai sain : 176 traits, rangés par identifiant v5, égaux au trait du texte ; manifeste à l'empreinte v5")
    # artefact 1 : un identifiant v1 manquant dans la source -> refus
    np.savez(f, ids=np.array(ids1[1:]), X=X[1:])
    sceller(f)
    ms["fichiers"]["couche16-dernier"]["sha256"] = emp(f)
    (src / "manifeste-traits.json").write_text(json.dumps(ms), encoding="utf-8")
    sceller(src / "manifeste-traits.json")
    for nom, attendu in (("artefact-source-incomplete", "sans trait source"),):
        try:
            deriver(src, banque_v1, banque_v5, tmp / nom)
        except SystemExit as e:
            ok = attendu in str(e) or "banque autre" in str(e) or "refus" in str(e)
            print(f"artefact {nom} : refusé ({e}) ; attendu : {ok}")
            if not ok:
                return 1
        else:
            print(f"artefact {nom} : ACCEPTÉ À TORT")
            return 1
    # artefact 2 : manifeste source à l'empreinte d'une autre banque -> refus
    ms["sha256_banque"] = "0" * 64
    (src / "manifeste-traits.json").write_text(json.dumps(ms), encoding="utf-8")
    sceller(src / "manifeste-traits.json")
    try:
        deriver(src, banque_v1, banque_v5, tmp / "artefact-autre-banque")
    except SystemExit as e:
        print(f"artefact autre banque : refusé ({e})")
    else:
        print("artefact autre banque : ACCEPTÉ À TORT")
        return 1
    return 0


if __name__ == "__main__":
    if sys.argv[1] == "--essai":
        sys.exit(essai(*sys.argv[2:5]))
    deriver(*sys.argv[1:5])
    print("dérivé")
